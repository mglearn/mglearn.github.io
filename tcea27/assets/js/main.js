(() => {
 'use strict';document.documentElement.classList.add('js');
 const toggle=document.getElementById('menu-toggle'),nav=document.getElementById('site-nav');
 toggle?.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);});
 document.addEventListener('keydown',event=>{if(event.key==='Escape'&&nav?.classList.contains('open')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.focus();}});
 let printDisclosures=[];window.addEventListener('beforeprint',()=>{printDisclosures=[...document.querySelectorAll('details')].map(d=>[d,d.open]);printDisclosures.forEach(([d])=>d.open=true);});window.addEventListener('afterprint',()=>printDisclosures.forEach(([d,open])=>d.open=open));
 document.querySelectorAll('[data-print]').forEach(b=>b.addEventListener('click',()=>window.print()));
 const search=document.getElementById('resource-search');
 if(search){
  const controls=['grade','type','subject','strategy','session'].map(id=>[id,document.getElementById('filter-'+id)]),cards=[...document.querySelectorAll('.resource-card')],keys={grade:'grades',type:'type',subject:'subjects',strategy:'strategies',session:'sessions'};
  function filter(){const q=search.value.trim().toLocaleLowerCase();let n=0;cards.forEach(card=>{const matches=(!q||card.textContent.toLocaleLowerCase().includes(q))&&controls.every(([id,c])=>!c.value||(card.dataset[keys[id]]||'').split('|').includes(c.value));card.hidden=!matches;if(matches)n++;});document.getElementById('resource-count').textContent=n+' resource'+(n===1?'':'s');document.getElementById('no-resources').hidden=n!==0;}
  search.addEventListener('input',filter);controls.forEach(([,c])=>c.addEventListener('change',filter));filter();
 }
 const focus=new URLSearchParams(location.search).get('focus'),activity=focus&&document.getElementById(focus);
 if(activity?.classList.contains('activity')){document.body.classList.add('project-focus');activity.classList.add('focused');}
})();
