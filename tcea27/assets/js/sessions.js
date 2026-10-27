/* Session metadata lives in data/sessions.json. The build emits static cards so
   sessions are discoverable without JavaScript and in the extracted packet. */
(() => {
 const published=(window.TCEA_DATA?.sessions||[]).filter(s=>s.status==='published');
 document.documentElement.dataset.publishedSessions=String(published.length);
 const cards=document.getElementById('session-cards');
 if(cards)cards.setAttribute('aria-label',published.length+' published session'+(published.length===1?'':'s'));
})();
