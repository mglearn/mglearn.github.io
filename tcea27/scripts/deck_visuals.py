"""Reusable original SVG infographic visuals. No private notes or generated text images."""
from html import escape as e
from pathlib import Path
COLORS=['#28657a','#76718e','#ae4e55','#925100','#0a3476']
def route(title,items):
 n=len(items);width=1200;step=(width-80)/n;body=''
 for i,(label,detail,icon) in enumerate(items):
  x=40+i*step;c=COLORS[i%len(COLORS)];cx=x+step/2
  body+=f'<rect x="{x+8}" y="100" width="{step-16}" height="235" rx="24" fill="white" stroke="#e3b764" stroke-width="3"/><circle cx="{cx}" cy="155" r="35" fill="{c}"/>'
  if icon=='bars':body+=f'<path d="M{cx-19} 172V155h10v17m8 0v-35h10v35m8 0v-25h10v25" fill="white"/>'
  elif icon=='talk':body+=f'<path d="M{cx-22} 140h44v27h-24l-12 12v-12h-8z" fill="none" stroke="white" stroke-width="4"/>'
  elif icon=='check':body+=f'<path d="M{cx-19} 155l13 13 26-29" fill="none" stroke="white" stroke-width="5"/>'
  elif icon=='target':body+=f'<circle cx="{cx}" cy="155" r="21" fill="none" stroke="white" stroke-width="3"/><circle cx="{cx}" cy="155" r="10" fill="white"/>'
  else:body+=f'<text x="{cx}" y="168" text-anchor="middle" fill="white" font-size="35" font-weight="800">{i+1}</text>'
  body+=f'<text x="{cx}" y="230" text-anchor="middle" fill="#082759" font-size="28" font-weight="800">{e(label)}</text><text x="{cx}" y="278" text-anchor="middle" fill="#172033" font-size="24">{e(detail)}</text>'
  if i<n-1:body+=f'<path d="M{x+step-3} 217h18m-8-8 9 8-9 8" fill="none" stroke="#925100" stroke-width="4"/>'
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" role="img" aria-label="{e(title)}"><title>{e(title)}</title><rect width="1200" height="370" rx="22" fill="#f8f3e5"/><g font-family="system-ui,sans-serif">{body}</g></svg>'
def build(root):
 specs={
 'pm-lifecycle':('Define, plan, coordinate, and review a school project',[('Define','Need and outcome','target'),('Plan','Owners and risks','talk'),('Coordinate','Track and inform','bars'),('Review','Verify usefulness','check')]),
 'pm-success-scorecard':('Four dimensions of a useful project scorecard',[('Reliable','Technical evidence','bars'),('Sustainable','Operating capacity','target'),('Useful','Teaching workflow','talk'),('Adopted','Use and support','check')]),
 'pm-change-models':('Questions about individual change',[('Understand','Why the change?','target'),('Support','What concerns?','talk'),('Know','What steps?','target'),('Do','Can I perform?','check'),('Sustain','What helps?','check')]),
 'pm-toolkit':('A small toolkit for better project decisions',[('Charter','Define scope','target'),('People','Map handoffs','talk'),('Updates','Enable decisions','bars'),('Scorecard','Check evidence','check')]),
 'math-route':('Represent, explain, and apply',[('Represent','Make the idea visible','bars'),('Explain','Use evidence and feedback','talk'),('Apply','Plan a new example','check')]),
 'math-success':('Three signs of a useful mathematical explanation',[('Read the scale','Use values and units','bars'),('Choose the display','Match it to the question','target'),('Plan the learning','Name the evidence','check')]),
 'feedback-loop':('Predict, model, explain, check, and revise',[('Predict','Think first','target'),('Model','Show why','bars'),('Explain','Compare','talk'),('Check','One cue','check'),('Revise','Try again','check')]),
 'ace-transfer':('Articulate, connect, and extend',[('Articulate','Name the idea','talk'),('Connect','Choose a useful tool','target'),('Extend','Change the context','check')]),
 'project-route':('Define the work, coordinate people, and verify the change',[('Define','Need and scope','target'),('Coordinate','Owners and dependencies','talk'),('Verify','Delivery and adoption','check')]),
 'project-success':('Scope, ownership, evidence, and a revised next step',[('Scope','Outcome and exclusion','target'),('Ownership','Dependency and decision','talk'),('Evidence','Delivery plus adoption','bars'),('Next step','Revise with a colleague','check')]),
 'project-update':('A usable project update names the next decision',[('Status','What changed?','bars'),('Blocker','What is waiting?','target'),('Owner','Who will act?','talk'),('Decision','What do you need?','check')])}
 for name,(title,items) in specs.items():(root/(name+'.svg')).write_text(route(title,items))
if __name__=='__main__':build(Path(__file__).resolve().parents[1]/'assets/infographics')
