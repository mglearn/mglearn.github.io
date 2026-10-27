#!/usr/bin/env python3
"""Build the static site, readable PDFs, HTML alternatives and offline ZIP.
Optional authoring dependencies: reportlab and pypdf (validation only).
No dependencies are downloaded or loaded by the published website.
"""
from build import *
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderSVG
from reportlab.pdfgen import canvas
from functools import partial
from xml.sax.saxutils import escape as x
import zipfile,csv
D=R/'downloads'/SLUG;D.mkdir(parents=True,exist_ok=True)
URL='https://mglearn.github.io/tcea27/'+SP
qr=QrCodeWidget(URL,barLevel='M');bounds=qr.getBounds();w,h=bounds[2]-bounds[0],bounds[3]-bounds[1]
qr_image=Drawing(110,110,transform=[110/w,0,0,110/h,0,0]);qr_image.add(qr)
renderSVG.drawToFile(qr_image,str(R/'assets/images/session-qr.svg'))
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='Title27',fontName='Helvetica-Bold',fontSize=22,leading=27,textColor=colors.HexColor('#082759'),spaceAfter=17));styles.add(ParagraphStyle(name='Section27',fontName='Helvetica-Bold',fontSize=13,leading=17,textColor=colors.HexColor('#0a3476'),spaceBefore=13,spaceAfter=8,keepWithNext=True));styles.add(ParagraphStyle(name='Body27',fontName='Helvetica',fontSize=10.5,leading=15,spaceAfter=9));styles.add(ParagraphStyle(name='Small27',fontName='Helvetica',fontSize=8.5,leading=12,spaceAfter=6))
def para(s,style='Body27'):return Paragraph(x(str(s)),styles[style])
def footer(c,doc):
 c.saveState();c.setStrokeColor(colors.HexColor('#d7e1ef'));c.line(42,38,570,38);c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#53627a'));c.drawString(42,25,'MG Learn | TCEA 2027 | '+doc.title);c.drawRightString(570,25,str(doc.page));c.restoreState()
common={'session-handout':[], 'graph-analysis':[], 'strategy-reference':[], 'lesson-planning':[], 'ace':[]}
common['session-handout']=[('The session',S['title']),('Your 50-minute route','\n'.join(f'{a["start"]}-{a["end"]} min: {a["title"]}' for a in A)),('Participation','Think, vote, explain, check, revise. Use fingers, a neighbor explanation, paper, or optional browser controls. Stay in your seat; no account or submitted responses.'),('Featured tools','\n'.join(RES[i]['name']+'\n'+RES[i]['url']+'\nPurpose: '+RES[i]['instructionalUses'][0]+'.' for i in S['featuredTools'])),('Strategy connections','Teacher clarity; direct instruction; argumentation; mathematical problem solving; corrective feedback; retrieval practice; transfer strategies.'),('Before tomorrow','Choose one mathematical goal, one strategy, and one tool serving that goal. Decide what students will explain and how you will respond to a misconception.'),('Open the session',URL)]
common['graph-analysis']=[('Start with the question','What is being measured? Who or what was sampled? Is the question about categories, change over time, a distribution, or a relationship?'),('Check the display','Read the title, source, axis labels, units, intervals, and baseline. Look for omitted categories, unequal intervals, distorted areas, and missing context. Is the representation appropriate for the question?'),('Garden challenge','Synthetic data: Garden A = 12 insects; Garden B = 15 insects. Graph A has a vertical baseline of 0. Graph B has a vertical baseline of 10. Which exaggerates the visual difference?'),('Answer and reasoning','Graph B. The actual difference is 3 insects; 15 is 25% more than 12. The visible lengths above ten are 2 and 5, a ratio of 2.5. A zero baseline preserves bar-length comparisons of totals. Some line graphs can reasonably use nonzero baselines; always explain the context.'),('Student explanation prompts','My claim is ____. The axis and values show ____. My calculation is ____. A limitation of this dataset is ____. I would need more information about ____.'),('Sampling matters','Equal-area sampling and equal observation effort matter. Two isolated counts do not describe variation or establish why the locations differ. Collect repeated observations before drawing broader conclusions.'),('Choose a representation','Categories: bar chart. Ordered change: line graph. Parts exhausting a whole: pie chart. Paired numerical variables: scatter plot. Distribution: dot plot, histogram, or box plot as appropriate. The question and structure of the data determine the choice.'),('Source and further learning',RES['graph-lessons']['url'])]
common['strategy-reference']=[('Use this reference','Start with the mathematical goal. Identify the strategy, a tool that serves it, and observable reasoning. Values below are the current MetaX weighted mean effect sizes; they are not tool ratings or promises of gains.')]+[(s['name']+' | '+', '.join(s['relatedTools']),s['classroomExample']+'\nLearning evidence: '+{'teacher-clarity':'A learner states the goal and explains the success criteria.','direct-instruction':'A learner explains each step in a similar new example.','argumentation':'A claim includes labels, values, and a response to another explanation.','problem-solving':'A learner chooses a representation and checks its fit to the question.','feedback':'A revised explanation addresses the specific misconception.','retrieval':'A learner recalls and then corrects an explanation without looking back first.','transfer':'A learner adapts the reasoning to a new dataset or concept.'}[s['id']]+'\nMetaX influence: '+s['influenceName']+'; weighted mean d = '+str(s['effectSize'])+'. Verified '+s['verifiedDate']+'.\n'+s['limitations']+'\n'+s['effectSizeSource']) for s in DATA['strategies']]
common['lesson-planning']=[('Plan with the learning first','Choose a mathematical intention before selecting software. A tool is useful when it helps students represent, explain, or test an idea.')]+[(label,'__________________________________________________________________\n__________________________________________________________________') for label in ['Grade and mathematical concept','Relevant TEKS and source / date checked','Learning intention and success criteria','Student prior knowledge and likely misconception','Digital tool and instructional purpose','Instructional strategy and teacher model','Student activity and optional paper alternative','Assessment evidence: what students will explain or show','Feedback cue and opportunity to revise','Transfer task: a different concept, context, or dataset']]+[('Verify the standard','Use the current TEA Chapter 111 documents and your district sequence.\n'+RES['teks']['url'])]
common['ace']=[('ARTICULATE: Explain the mathematical idea','What does the representation show? Explain the reasoning in your own words.\n\n__________________________________________________________________\n__________________________________________________________________\n__________________________________________________________________'),('CONNECT: Relate it to another concept','How does the idea connect to another representation, strategy, or mathematical relationship?\n\n__________________________________________________________________\n__________________________________________________________________\n__________________________________________________________________'),('EXTEND: Apply it to a new problem','Change the dataset, starting point, or context. What stays the same? What must change?\n\n__________________________________________________________________\n__________________________________________________________________\n__________________________________________________________________'),('For the educator','Name the instructional strategy, choose a tool that serves the goal, and describe the evidence you will look for. Use the browser ACE builder to plan instruction; use this student-facing version to prompt mathematical explanation.')]
# A primary data record keeps both formats consistent and editable.
(R/'data/handouts.json').write_text(json.dumps(common,ensure_ascii=False,indent=2)+'\n')
for d in DATA['downloads']:
 blocks=common[d['id']];story=[para('TCEA 2027 | MIGUEL GUHLIN','Small27'),para(d['title'],'Title27'),para(S['title'])]
 html=''
 for title,text in blocks:
  story.append(para(title,'Section27'))
  for line in text.split('\n'):story.append(para(line) if line else Spacer(1,10))
  html+='<h2>'+e(title)+'</h2>'+''.join('<p>'+('<a href="'+e(line)+'">'+e(line)+'</a>' if line.startswith('https://') else e(line))+'</p>' for line in text.split('\n') if line)
 if d['id']=='session-handout':story.append(qr_image);html+='<img src="../../assets/images/session-qr.svg" width="150" height="150" alt="QR code linking to the math session page"><p><a href="'+URL+'">Open the session directly</a></p>'
 if d['id']=='graph-analysis':html+=pair('handout')
 story+=[Spacer(1,15),para('Original teaching materials by Miguel Guhlin / MG Learn. Research and resource verification: October 27, 2026. Reuse and adapt these original handouts with attribution. Linked tools, research, and standards retain their own terms.','Small27')]
 doc=SimpleDocTemplate(str(D/d['file']),pagesize=(612,792),rightMargin=45,leftMargin=45,topMargin=42,bottomMargin=50,title=d['title'],author='Miguel Guhlin / MG Learn',invariant=1)
 doc.build(story,onFirstPage=footer,onLaterPages=footer,canvasmaker=partial(canvas.Canvas,invariant=1))
 page('downloads/'+SLUG+'/'+d['id']+'.html',d['title'],heading('Printable resource',d['title'],d['description'])+section('<div class="prose">'+html+'<div class="actions">'+link(d['file'],'Download PDF')+'<button type="button" class="button ghost" data-print>Print this resource</button></div><p class="small muted">Original teaching materials by Miguel Guhlin / MG Learn. Reuse and adapt with attribution. Research and standards links retain their own terms. Verified October 27, 2026.</p></div>'),'downloads')
(D/'garden-insects.csv').write_text('Garden,Insects\nGarden A,12\nGarden B,15\n')
(D/'campus-temperature.csv').write_text('Time,Temperature_C\n09:00,18\n12:00,24\n15:00,27\n')
# Deterministic archive: includes the complete static companion, HTML alternatives,
# data, PDFs and local scripts; excludes development tools and the archive itself.
archive=R/'downloads/tcea27-offline-packet-protected.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(R.rglob('*')):
  rel=p.relative_to(R)
  if not p.is_file() or p==archive or rel.parts[0] in ['tests','scripts'] or p.suffix in ['.pyc','.zip'] or '__pycache__' in rel.parts:continue
  info=zipfile.ZipInfo('tcea27/'+str(rel),(2026,10,27,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16;data=p.read_bytes()
  if p.suffix=='.html':
   import re
   data=re.sub(rb'href="[^"]*tcea27-offline-packet-protected\.zip"',b'href="https://mglearn.github.io/tcea27/downloads/tcea27-offline-packet-protected.zip"',data)
  z.writestr(info,data)
print('Built 5 selectable-text PDFs with HTML alternatives and offline ZIP:',archive.stat().st_size,'bytes')
