/* Keep language choice across visits; no form values are stored. */
(function(){
 'use strict';
 const key='mates-language';
 const path=location.pathname;
 const isBengali=path.includes('/bn/');
 const current=isBengali?'bn':'en';
 function target(language){
  const url=new URL(location.href);
  // Use this script's path so both a local preview and GitHub project Pages work.
  const script=document.currentScript||document.querySelector('script[src$="/language.js"]');
  const scriptUrl=new URL(script.src,location.href);
  const base=scriptUrl.pathname.replace(/assets\/language\.js$/,'');
  const file=path.slice(path.lastIndexOf('/')+1)||'index.html';
  url.pathname=base+(language==='bn'?'bn/':'')+file;
  return url;
 }
 let preference;
 try{preference=localStorage.getItem(key);}catch{/* Language still works when storage is disabled. */}
 if(preference==='bn'&&!isBengali){location.replace(target('bn').href);return;}
 // A directly shared Bengali page remains Bengali even for a new visitor.
 if(isBengali){try{localStorage.setItem(key,'bn');}catch{}}
 document.addEventListener('DOMContentLoaded',()=>{
  const select=document.querySelector('#site-language');
  if(!select)return;
  select.value=current;
  select.addEventListener('change',()=>{
   const language=select.value;
   if(!['en','bn'].includes(language))return;
   try{localStorage.setItem(key,language);}catch{}
   // target() resolves the script from the DOM after the initial load.
   location.assign(target(language).href);
  });
 });
})();

