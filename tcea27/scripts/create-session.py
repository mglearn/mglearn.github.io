#!/usr/bin/env python3
"""Create a new draft landing page using the saved TCEA27 visual identity."""
from pathlib import Path
from html import escape
import argparse,json,re,runpy
parser=argparse.ArgumentParser();parser.add_argument('session_id');args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
records=json.loads((root/'data/sessions.json').read_text());record=next((s for s in records if s['id']==args.session_id),None)
if not record:raise SystemExit('Add a real draft record to data/sessions.json first.')
if record.get('status')!='draft':raise SystemExit('Scaffold a draft session; publish only after its content is complete.')
slug=record['slug']
if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug):raise SystemExit('Use a lowercase, hyphen-separated slug.')
relative=f'sessions/{slug}/index.html';target=root/relative
if target.exists():raise SystemExit('This session already exists; edit it without overwriting it.')
body=(root/'design-system/session-body.html.tpl').read_text()
values={'TITLE':record['title'],'SHORT_DESCRIPTION':record['shortDescription'],'DESCRIPTION':record['fullDescription'],'DURATION':record['durationMinutes'],'FORMAT':record['format'],'AUDIENCE':' · '.join(record['audience']),'PRESENTERS':', '.join(p['name'] for p in record['presenters'])}
for key,value in values.items():body=body.replace('__'+key+'__',escape(str(value)))
body=body.replace('__OBJECTIVES__','<ul>'+''.join('<li>'+escape(item)+'</li>' for item in record['learningObjectives'])+'</ul>')
shared=runpy.run_path(str(root/'scripts/build.py'))
shared['page'](relative,record['title'],body,'sessions')
print('Created themed draft session:',target)
