/* Optional notes remain in page memory; no network or browser persistence. */
(()=>{'use strict';
window.addEventListener('afterprint',()=>document.body.classList.remove('print-only-reflection'));
for(const form of document.querySelectorAll('.coaching-notes')){
 const status=form.querySelector('[role="status"]');
 const text=()=>[...form.querySelectorAll('textarea')].map(t=>t.dataset.label+'\n'+t.value).join('\n\n');
 form.addEventListener('submit',e=>e.preventDefault());
 form.addEventListener('reset',()=>{status.textContent='Notes cleared.';document.querySelector('.print-reflection').textContent='';});
 form.addEventListener('click',async e=>{
  const action=e.target.closest('[data-coaching]')?.dataset.coaching;if(!action)return;
  if(action==='copy'){
   try{await navigator.clipboard.writeText(text());status.textContent='Notes copied.';}
   catch{const field=document.createElement('textarea');field.value=text();document.body.append(field);field.select();const ok=document.execCommand('copy');field.remove();status.textContent=ok?'Notes copied.':'Use Download notes to save a copy.';}
  }
  if(action==='download'){const url=URL.createObjectURL(new Blob([text()],{type:'text/plain;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download=form.id+'.txt';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);status.textContent='Notes downloaded.';}
  if(action==='print'){document.querySelector('.print-reflection').textContent=text();document.body.classList.add('print-only-reflection');window.print();}
 });
}
})();
