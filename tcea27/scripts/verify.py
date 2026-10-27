#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re,base64
import json,zipfile,hashlib
R=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,text):super().__init__();self.refs=[];self.ids=[];self.h1=0;self.feed(text)
 def handle_starttag(self,t,a):
  a=dict(a)
  if 'id' in a:self.ids.append(a['id'])
  if t=='h1':self.h1+=1
  for key in ['href','src']:
   if key in a:self.refs.append(a[key])
files={p:Page(p.read_text()) for p in R.rglob('*.html')}
errors=[];links=0
for p,doc in files.items():
 if doc.h1!=1:errors.append(f'{p}: expected one h1')
 if len(doc.ids)!=len(set(doc.ids)):errors.append(f'{p}: duplicate IDs')
 for ref in doc.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  if u.path.startswith('/'):errors.append(f'{p}: site-root reference {ref}');continue
  t=(p.parent/unquote(u.path)).resolve() if u.path else p
  if t.is_dir():t=t/'index.html'
  if not t.exists():errors.append(f'{p}: missing {ref}')
  if u.fragment and t in files and unquote(u.fragment) not in files[t].ids:errors.append(f'{p}: missing fragment {ref}')
  links+=1
s=json.loads((R/'data/sessions.json').read_text());a=json.loads((R/'data/activities.json').read_text())
assert all('presenter' not in item and 'transition' not in item for item in a),'Private facilitation fields must not be published'
for name in ['presenter-guide.html','presenter-webdeck.html']:
 text=(R/'sessions/math-without-price-tag'/name).read_text()
 payload=json.loads(re.search(r'<script id="vaultPayload" type="application/json">(.*?)</script>',text).group(1))
 assert payload['algorithm']=='AES-256-GCM' and payload['iterations']>=600000
 assert len(base64.b64decode(payload['salt']))==16 and len(base64.b64decode(payload['iv']))==12
 assert 'data-presenter-step' not in text and 'class="notes"' not in text

assert sum(x['end']-x['start'] for x in a)==50
assert [x['start'] for x in a]==[0,5,15,35,45]
assert s[0]['title']=='High-Impact Teaching Math Tools Without the Price Tag'
for rec in json.loads((R/'data/strategies.json').read_text()):
 assert rec['effectSize'] is None or (isinstance(rec['effectSize'],(int,float)) and rec['effectSizeSource'].startswith('https://www.visiblelearningmetax.com/influences/view/') and rec['verifiedDate'])
 assert rec['limitations'] and rec['influenceName']
for rec in s:
 if rec['status']=='published':assert (R/'sessions'/rec['slug']/'index.html').is_file()
from pypdf import PdfReader
for p in (R/'downloads').rglob('*.pdf'):
 reader=PdfReader(p);text='\n'.join(page.extract_text() for page in reader.pages)
 assert len(text)>600,(p,'missing selectable text')
 assert 'MG Learn' in text and '2027' in text
 print(p.name,len(reader.pages),'pages; selectable text verified')
with zipfile.ZipFile(R/'downloads/tcea27-offline-packet-protected.zip') as z:
 assert z.testzip() is None
 assert 'tcea27/index.html' in z.namelist()
 assert 'tcea27/sessions/math-without-price-tag/presenter-guide.html' in z.namelist()
 assert len([n for n in z.namelist() if n.endswith('.pdf')])==5
 for name in ['presenter-guide.html','presenter-webdeck.html']:
  key='tcea27/sessions/math-without-price-tag/'+name
  assert z.read(key)==(R/'sessions/math-without-price-tag'/name).read_bytes(),'Offline presenter resource out of date'
 assert not any('..' in Path(n).parts for n in z.namelist())
if errors:raise SystemExit('\n'.join(errors))
print(f'Checked {len(files)} HTML pages, {links} local references, research provenance, 50-minute agenda, 5 PDFs and offline packet.')
