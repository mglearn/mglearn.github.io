"""Original accessible teaching infographics; model summaries are paraphrased.
Visual direction: user-supplied infographic instructions; native SVG real text.
"""
from pathlib import Path
from html import escape as e

def diagram(title,items,takeaway,columns):
 rows=(len(items)+columns-1)//columns;body='';width=1120/columns;height=135 if rows>1 else 250
 for i,(label,detail) in enumerate(items):
  x=40+(i%columns)*width;y=78+(i//columns)*150;c=['#0a3476','#237683','#925100'][i%3];fill=['#e9f4fc','#e6f6f4','#fff5de'][i%3]
  body+=f'<rect x="{x+6}" y="{y}" width="{width-12}" height="{height}" rx="20" fill="{fill}"/><circle cx="{x+width/2}" cy="{y+36}" r="24" fill="{c}"/><text x="{x+width/2}" y="{y+45}" text-anchor="middle" fill="white" font-size="27" font-weight="800">{i+1}</text>'
  for j,line in enumerate(label.split('|')):body+=f'<text x="{x+width/2}" y="{y+88+j*31}" text-anchor="middle" fill="#082759" font-size="26" font-weight="800">{e(line)}</text>'
  if rows==1:
   for j,line in enumerate(detail.split('|')):body+=f'<text x="{x+width/2}" y="{y+160+j*32}" text-anchor="middle" fill="#172033" font-size="25">{e(line)}</text>'
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 460" role="img" aria-label="{e(title)}"><title>{e(title)}</title><defs><linearGradient id="head"><stop stop-color="#082759"/><stop offset="1" stop-color="#237683"/></linearGradient></defs><rect width="1200" height="460" rx="22" fill="white"/><rect width="1200" height="60" rx="18" fill="url(#head)"/><g font-family="system-ui,sans-serif"><text x="35" y="41" font-size="30" fill="white" font-weight="800">{e(title)}</text>{body}<path d="M30 394h190l25 26-25 26H30z" fill="#082759"/><text x="52" y="429" font-size="25" fill="white" font-weight="800">KEY IDEA</text><text x="266" y="428" font-size="25" fill="#082759">{e(takeaway)}</text></g></svg>'
def build(root):
 specs={
 'pm-adkar':('ADKAR · support individual change',[('Awareness','Why does|this matter?'),('Desire','What concerns|need listening?'),('Knowledge','What do I|need to know?'),('Ability','Can I do it|in practice?'),('Reinforcement','What keeps|it working?')],'Find the barrier before choosing the support.',5),
 'pm-kotter':('Kotter · coordinate organization-wide change',[('Explain the|need',''),('Build the|coalition',''),('Clarify the|direction',''),('Invite broad|participation',''),('Remove|obstacles',''),('Show early|progress',''),('Keep the|momentum',''),('Embed new|routines','')],'A rollout needs people, decisions, and sustained support.',4),
 'pm-kpi':('KPIs · connect delivery to adoption',[('Define','What outcome|will improve?'),('Measure','Baseline, target,|and calculation'),('Verify','Evidence source|and owner'),('Review','Check use and|act on barriers')],'A completed installation does not establish sustained use.',4),
 'pm-risk-response':('Risk · turn a concern into a response',[('Event','What might|go wrong?'),('Signal','What warning|will we watch?'),('Action','What response|is agreed?'),('Owner','Who acts and|checks again?')],'Separate an existing issue from a possible future risk.',4),
 'pm-milestones':('Milestones · make the handoff visible',[('Ready','Facilities verifies|the prerequisite'),('Tested','IT checks the|agreed service'),('Usable','Teacher checks|the workflow'),('Supported','Owner reviews|continued use')],'Name acceptance evidence and an owner at each handoff.',4)}
 for name,args in specs.items():(root/(name+'.svg')).write_text(diagram(*args))
if __name__=='__main__':build(Path(__file__).resolve().parents[1]/'assets/infographics')
