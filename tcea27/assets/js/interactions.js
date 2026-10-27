(() => {
 'use strict';
 function resetQuestion(q){q.querySelectorAll('input[type=radio]').forEach(i=>i.checked=false);q.querySelector('.answer').open=false;q.querySelector('.answer-feedback').textContent='Question reset. Predict again before checking.';}
 document.querySelectorAll('[data-challenge]').forEach(q=>{
  const reveal=q.querySelector('[data-reveal]'),reset=q.querySelector('[data-reset]');reveal.hidden=false;reset.hidden=false;
  reveal.addEventListener('click',()=>{q.querySelector('.answer').open=true;const selected=q.querySelector('input:checked');q.querySelector('.answer-feedback').textContent=selected?'You chose '+selected.closest('label').innerText.trim()+'. Compare your reasoning with the explanation, then revise.':'No choice is required. Read the explanation and compare it with your prediction.';});
  reset.addEventListener('click',()=>resetQuestion(q));
 });
 const restart=document.getElementById('restart-retrieval');if(restart){restart.hidden=false;restart.addEventListener('click',()=>{document.querySelectorAll('#retrieval-set [data-challenge]').forEach(resetQuestion);document.querySelector('#retrieval-set input').focus();});}
 const form=document.getElementById('ace-form');
 if(form){
  form.addEventListener('submit',e=>e.preventDefault());
  const status=document.getElementById('reflection-status');
  const text=()=>['ACE Math Reflection','',...['articulate','connect','extend'].map(id=>id.toUpperCase()+'\n'+document.getElementById(id).value.trim())].join('\n\n');
  document.getElementById('copy-reflection').addEventListener('click',async()=>{
   const value=text();try{if(location.protocol==='file:'||!navigator.clipboard?.writeText)throw Error('Clipboard unavailable');await navigator.clipboard.writeText(value);status.textContent='Reflection copied. Paste it into your notes to keep it.';}
   catch{const copy=document.createElement('textarea');copy.value=value;copy.setAttribute('aria-label','Reflection text to copy');form.append(copy);copy.select();try{if(!document.execCommand('copy'))throw Error();status.textContent='Reflection copied.';copy.remove();}catch{status.textContent='Automatic copy is unavailable. Select and copy the reflection text below.';copy.focus();}}
  });
  document.getElementById('print-reflection').addEventListener('click',()=>{const panel=document.querySelector('.print-reflection');panel.textContent=text();document.body.classList.add('print-only-reflection');window.print();});
  window.addEventListener('afterprint',()=>document.body.classList.remove('print-only-reflection'));
  form.addEventListener('reset',()=>{status.textContent='Responses cleared.';document.querySelector('.print-reflection').textContent='';});
 }
 document.querySelectorAll('[data-countdown]').forEach(timer=>{
  const select=timer.querySelector('select'),output=timer.querySelector('output'),start=timer.querySelector('[data-start]'),reset=timer.querySelector('[data-timer-reset]'),status=timer.querySelector('[role=status]');let remaining=Number(select.value),end=0,interval;
  const paint=()=>output.textContent=Math.floor(remaining/60)+':'+String(remaining%60).padStart(2,'0');
  function stop(){clearInterval(interval);interval=null;start.textContent='Start';select.disabled=false;}
  function tick(){remaining=Math.max(0,Math.ceil((end-performance.now())/1000));paint();if(!remaining){stop();status.textContent='Time to check and revise.';}}
  start.addEventListener('click',()=>{if(interval){tick();stop();start.textContent='Resume';return;}if(!remaining)remaining=Number(select.value);end=performance.now()+remaining*1000;interval=setInterval(tick,200);select.disabled=true;start.textContent='Pause';status.textContent='Discussion timer running.';});
  const clear=()=>{stop();remaining=Number(select.value);status.textContent='Timer reset.';paint();};reset.addEventListener('click',clear);select.addEventListener('change',clear);
 });
 const steps=[...document.querySelectorAll('[data-presenter-step]')];
 if(steps.length){
  const start=document.getElementById('presenter-start'),reset=document.getElementById('presenter-reset'),previous=document.getElementById('previous-segment'),next=document.getElementById('next-segment'),output=document.getElementById('presenter-elapsed'),progress=document.getElementById('presenter-progress'),pacing=document.getElementById('pacing-status');let index=0,elapsed=0,started=0,running=false,interval;
  [start,reset,previous,next].forEach(b=>b.hidden=false);
  const paintTime=()=>{const seconds=Math.floor((elapsed+(running?performance.now()-started:0))/1000);output.textContent=String(Math.floor(seconds/60)).padStart(2,'0')+':'+String(seconds%60).padStart(2,'0');const a=window.TCEA_DATA.activities[index];pacing.textContent=seconds>=3000?'50-minute session window complete':'Suggested segment window: '+a.start+'–'+a.end+' min';};
  function show(i){index=Math.max(0,Math.min(steps.length-1,i));steps.forEach((step,j)=>step.hidden=j!==index);previous.disabled=index===0;next.disabled=index===steps.length-1;progress.textContent='Segment '+(index+1)+' of '+steps.length+' · '+window.TCEA_DATA.activities[index].shortTitle;paintTime();}
  previous.addEventListener('click',()=>show(index-1));next.addEventListener('click',()=>show(index+1));
  start.addEventListener('click',()=>{if(running){elapsed+=performance.now()-started;running=false;clearInterval(interval);start.textContent='Resume timer';}else{started=performance.now();running=true;interval=setInterval(paintTime,250);start.textContent='Pause timer';}paintTime();});
  reset.addEventListener('click',()=>{running=false;elapsed=0;clearInterval(interval);start.textContent='Start timer';show(0);});
  document.addEventListener('keydown',event=>{if(event.altKey||event.ctrlKey||event.metaKey||event.target.closest('input,textarea,select,button,a,summary'))return;if(event.key==='ArrowRight'||event.key==='ArrowLeft'){event.preventDefault();show(index+(event.key==='ArrowRight'?1:-1));}});
  show(0);
 }
})();
