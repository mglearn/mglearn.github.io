"""Render a private slide model using the saved TCEA27 deck identity.
This module contains only rendering code. Keep slide notes and plaintext outputs
outside public Git; seal the completed HTML with seal-presenter.cjs to publish.
"""
from pathlib import Path
from html import escape as e
import base64,json
ROOT=Path(__file__).resolve().parents[1]
def facilitator_content():
 profile=json.loads((ROOT/'design-system/facilitator-miguel.json').read_text());portrait='data:image/webp;base64,'+base64.b64encode((ROOT/profile['portrait']).read_bytes()).decode()
 return '<div class="portrait-layout"><img src="'+portrait+'" alt="'+e(profile['portraitAlt'])+'"><div><h3>'+e(profile['name'])+'</h3><p>'+e(profile['descriptor'])+'</p>'+''.join('<p>'+e(item)+'</p>' for item in profile['highlights'][:2])+'<div class="portrait-links no-advance"><a href="'+e(profile['bioSource'])+'" target="_blank" rel="noopener noreferrer">mguhlin.org ↗</a></div></div></div>'
def render_deck(slides,title,slug,photo_file,subject):
 assert slides[0]['start']==0 and slides[-1]['end']==50
 assert abs(sum(s['end']-s['start'] for s in slides)-50)<.00001
 for a,b in zip(slides,slides[1:]):assert a['end']==b['start']
 css=(ROOT/'assets/webdeck/deck-framework.css').read_text();js=(ROOT/'assets/webdeck/deck-framework.js').read_text();hub='https://mglearn.github.io/tcea27/sessions/'+slug+'/'
 js=js.replace('https://mglearn.github.io/tcea27/sessions/math-without-price-tag/',hub)
 skin=(ROOT/'assets/webdeck/tcea27-deck-theme.css').read_text();photo='data:image/webp;base64,'+base64.b64encode((ROOT/photo_file).read_bytes()).decode();body=''
 for i,s in enumerate(slides):
  kind=s.get('kind','');heading='' if kind in ['cover','divider'] else '<h2 class="slide-title">'+e(s['title'])+'</h2>'
  kicker='' if kind=='cover' else '<div class="slide-kicker">TCEA 2027 · '+e(subject)+'</div>';content=s['content']
  if kind=='cover':content='<img class="title-photo" src="'+photo+'" alt="'+e(s.get('photoAlt','Illustrative scene for the workshop'))+'"><div class="title-panel"><div class="cover-eyebrow">TCEA 2027 · '+e(subject)+'</div><h1>'+e(title)+'</h1><div class="subtitle">'+e(s.get('subtitle','Experience the ideas. Talk through the decisions. Plan a useful next step.'))+'</div><div class="meta">Miguel Guhlin</div></div>'
  notes='<p class="notes-meta">Suggested pacing '+str(s['start'])+'–'+str(s['end'])+' minutes</p><p>'+e(s['notes'])+'</p><p class="notes-source"><a href="'+hub+'" target="_blank" rel="noopener noreferrer">Session activities and sources</a> · <a href="https://mguhlin.org/media/2026/10/professional-learning-facilitator-guide.png" target="_blank" rel="noopener noreferrer">Facilitation planning reference</a></p>'
  body+='<section class="slide '+kind+(' current' if i==0 else '')+'" data-start="'+str(s['start'])+'" data-end="'+str(s['end'])+'"><div class="slide-body">'+kicker+heading+content+'</div><div class="slide-footer"><span class="brand">TCEA 2027 · '+e(subject)+'</span><span class="fac">Facilitator: Miguel Guhlin</span><span class="url">mglearn.github.io/tcea27</span></div><div class="notes">'+notes+'</div></section>'
 return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="referrer" content="no-referrer"><meta name="generator" content="Web Deck v5 (https://mguhlin.github.io/webdecks/) — developed by Miguel Guhlin - mguhlin.org"><!-- Built with Web Deck v5 · MIT · https://mguhlin.github.io/webdecks/ --><title>'+e(title)+' | Presenter webdeck</title><style>'+css+'</style><style>'+skin+'</style></head><body><div class="deck">'+body+'</div><button class="deck-lock no-print" type="button" onclick="window.name=String();location.reload()">Lock presenter resource</button><script>'+js+'</script></body></html>'
