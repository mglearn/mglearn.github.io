"""Purposeful native SVG diagrams for the cooperative workshop."""
from pathlib import Path
from html import escape as e
R=Path(__file__).resolve().parents[1]/'assets/infographics'
def wrap(body,title):return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" role="img" aria-label="'+e(title)+'"><title>'+e(title)+'</title><rect width="1200" height="400" rx="25" fill="#f8f3e5"/><g font-family="system-ui,sans-serif" fill="#082759">'+body+'</g></svg>'
def text(x,y,t,size=28,anchor='start',weight=500):return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{e(t)}</text>'
def build():
 body=''
 for i,(time,label,detail) in enumerate([('0–9','Play','Concept Bingo'),('9–18','Connect','Every voice'),('18–34','Explore','Two activities'),('34–42','Share','One discovery'),('42–47','Adapt','Classroom goal'),('47–50','Check','Explain again')]):
  x=25+i*195;body+=f'<rect x="{x}" y="80" width="180" height="240" rx="22" fill="'+['#e8f4fc','#e4f5ee','#fff3d7'][i%3]+'" stroke="#abc4d4"/>'+text(x+90,135,time,32,'middle',800)+text(x+90,205,label,31,'middle',800)+text(x+90,265,detail,24,'middle')
 (R/'coop-timeline.svg').write_text(wrap(body,'Our fifty-minute plan: play, connect, explore, share, adapt, and check'))
 body='<path d="M285 115L600 200L915 115M285 290L600 200L915 290" stroke="#28657a" stroke-width="5" fill="none"/>'
 for x,y,a,b in [(30,35,'Navigator','Invite others to guide the next click.'),(770,35,'Explainer','Say why the choice makes sense.'),(30,235,'Questioner','Ask for evidence or an example.'),(770,235,'Connector','Link our discovery to a learning goal.')]:
  body+=f'<rect x="{x}" y="{y}" width="400" height="125" rx="24" fill="#e7f3fa" stroke="#b79750"/>'+text(x+20,y+44,a,30,weight=800)+''.join(text(x+20,y+83+j*28,line,23) for j,line in enumerate(__import__('textwrap').wrap(b,30)))
 body+='<circle cx="600" cy="200" r="122" fill="#fff0cd" stroke="#28657a" stroke-width="4"/>'+text(600,165,'Our shared',28,'middle',800)+text(600,203,'explanation',30,'middle',800)+text(600,248,'Every voice matters',22,'middle')
 (R/'coop-roles.svg').write_text(wrap(body,'Four ways to contribute to one shared explanation'))
 body=''
 for i,(label,detail) in enumerate([('Think','Make your own choice.'),('Try','Work on the shared task.'),('Explain','Say why; ask a question.'),('Revise','Use the evidence to improve.')]):
  x=25+i*295;body+=f'<circle cx="{x+130}" cy="130" r="50" fill="#28657a"/><text x="{x+130}" y="145" text-anchor="middle" fill="white" font-size="40">{i+1}</text>'+text(x+130,230,label,34,'middle',800)+text(x+130,285,detail,22,'middle')
  if i<3:body+=f'<path d="M{x+195} 130h90l-18-12m18 12-18 12" stroke="#925100" stroke-width="6" fill="none"/>'
 (R/'coop-routine.svg').write_text(wrap(body,'Think independently, try together, explain with evidence, and revise'))
 body=''
 for i,(label,first,second) in enumerate([('Review and recall','Bingo','Quiz and Flashcard Studio'),('Puzzles and reasoning','Meme Puzzle','Fortune Wheel'),('Create and explain','Story Wheel','Dicebreaker Creator')]):
  y=30+i*125;body+=f'<rect x="25" y="{y}" width="1150" height="105" rx="22" fill="'+['#e7f3fa','#e5f5ef','#fff1d6'][i]+'"/>'+text(45,y+44,label,26,weight=800)+text(500,y+65,first,29,'middle',700)+text(960,y+65,second,26,'middle',700)+f'<path d="M620 {y+54}h85l-18-12m18 12-18 12" stroke="#28657a" stroke-width="5" fill="none"/>'
 (R/'coop-paths.svg').write_text(wrap(body,'Choose one path, with one tool for each exploration round'))
 terms=['Retrieval','Explain','Evidence','Feedback','FREE','Reflect','Shared goal','Check','Elaborate'];body=''
 for i,t in enumerate(terms):
  x=30+(i%3)*190;y=25+(i//3)*118;body+=f'<rect x="{x}" y="{y}" width="180" height="108" rx="15" fill="'+('#fff0cd' if i==4 else '#e5f3fb')+'" stroke="#28657a" stroke-width="2"/>'+text(x+90,y+61,t,27,'middle',750)
 for i,(a,b) in enumerate([('Think','Choose before comparing.'),('Mark','Show your first choice.'),('Explain','Tell us why it fits.')]):body+=text(680,65+i*115,a,32,weight=800)+text(680,112+i*115,b,28)
 (R/'coop-bingo.svg').write_text(wrap(body,'A concept Bingo card becomes a learning task when each choice is explained'))
if __name__=='__main__':build()
