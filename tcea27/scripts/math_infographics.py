"""Math-specific teaching diagrams using the conference infographic grammar."""
from pathlib import Path
from pm_infographics import diagram

def build(root):
 specs={
 'math-model-cycle':('Teach a number relationship',[('Predict','Think before|the demonstration'),('Model','Show the jumps|and explain'),('Check','Hear the|reasoning'),('Revise','Use a cue,|then try again')],'A representation is useful when students explain the relationship.',4),
 'math-graph-choice':('Choose a graph for the question',[('Categories','Compare counts|with a bar chart'),('Over time','Track change|with a line graph'),('Parts of a whole','Use a pie when|the parts exhaust it'),('Paired values','Show relationships|with a scatter plot')],'Start with the question and the structure of the data.',4),
 'math-graph-workflow':('Build and defend a graph',[('Enter','Garden A = 12|Garden B = 15'),('Display','Use a labeled|zero-baseline bar'),('Compare','Change the scale,|keep the data'),('Explain','Use values,|units, and labels')],'The actual difference stays three insects when the scale changes.',4),
 'math-fair-sample':('Check the evidence before the claim',[('Question','What do these|counts compare?'),('Sampling','Same area, time,|and effort?'),('Variation','What do repeated|counts show?'),('Claim','What can the|evidence support?')],'Two counts alone do not explain why the gardens differ.',4),
 'math-argument':('Make a mathematical explanation stronger',[('Claim','Name the display|and the question'),('Evidence','Use values, labels,|and calculations'),('Revision','Respond to a|different explanation')],'A revised explanation should address specific evidence.',3),
 'math-retrieval-cycle':('Build a recall check with feedback',[('Recall','Answer before|looking back'),('Explain','Show the|reasoning'),('Check','Read a targeted|explanation'),('Return','Try a new|example later')],'Retrieval and feedback reveal what needs another explanation.',4),
 'math-lesson-plan':('Plan the instruction, not just the tool',[('Goal','Name a concept|and success criteria'),('Strategy','Choose modeling,|discussion, or recall'),('Tool','Select a useful|representation'),('Evidence','Listen for the|student explanation')],'Choose the tool after the learning goal and evidence.',4),
 'math-ace-plan':('ACE · turn an experience into a lesson',[('Articulate','Name the idea|and strategy'),('Connect','Choose a tool|that serves it'),('Extend','Adapt to a new|classroom task')],'Include an observable explanation and a chance to revise.',3)}
 for name,args in specs.items():(root/(name+'.svg')).write_text(diagram(*args))
if __name__=='__main__':build(Path(__file__).resolve().parents[1]/'assets/infographics')

def numberline():
 return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 260" role="img" aria-label="Three jumps from four to seven"><title>Three jumps from four to seven</title><defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#237683"/></marker></defs><rect width="1000" height="260" rx="25" fill="#eaf5fc"/><g font-family="system-ui,sans-serif" fill="#082759"><path d="M60 185H950" stroke="#0a3476" stroke-width="5"/><g stroke="#0a3476" stroke-width="4"><path d="M80 173v24M360 173v24M640 173v24M920 173v24"/></g><g stroke="#237683" stroke-width="5" fill="none" marker-end="url(#arrow)"><path d="M80 167Q220 38 355 167"/><path d="M360 167Q500 38 635 167"/><path d="M640 167Q780 38 915 167"/></g><g font-size="26" text-anchor="middle"><text x="220" y="60">First jump</text><text x="500" y="60">Second jump</text><text x="780" y="60">Third jump</text></g><g font-size="37" text-anchor="middle" font-weight="800"><text x="80" y="239">4</text><text x="360" y="239">5</text><text x="640" y="239">6</text><text x="920" y="239">7</text></g></g></svg>'''
if __name__=='__main__':(Path(__file__).resolve().parents[1]/'assets/infographics/math-three-jumps.svg').write_text(numberline())
