'use strict';
const bengali=document.documentElement.lang==='bn-BD';
const copy={
 open:bengali?'মেনু খুলুন':'Open navigation',close:bengali?'মেনু বন্ধ করুন':'Close navigation',
 title:bengali?'মেটস ফাউন্ডেশন — আগ্রহ প্রকাশ':'MATES Foundation — Expression of interest',
 name:bengali?'নাম':'Name',email:bengali?'ইমেইল':'Email',interest:bengali?'আগ্রহের বিষয়':'Interest',
 unsent:bengali?'ব্রাউজারে তৈরি করা হয়েছে। এই বার্তাটি পাঠানো হয়নি।':'Prepared locally. This message has not been sent.',
 copied:bengali?'কপি করা হয়েছে। বার্তাটি পাঠানো হয়নি।':'Copied. The message has not been sent.',
 manual:bengali?'বার্তাটি নির্বাচন করে আপনার ডিভাইসের কপি করার পদ্ধতি ব্যবহার করুন।':'Select and copy the message using your device’s copy command.'
};
const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#navigation');
if(toggle&&nav){toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?copy.close:copy.open);nav.classList.toggle('open',open);});document.addEventListener('keydown',e=>{if(e.key==='Escape'){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label',copy.open);}});nav.addEventListener('click',e=>{if(e.target.closest('a')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');}});}
const current=location.pathname.split('/').pop()||'index.html';
document.querySelectorAll('nav a').forEach(a=>{if(a.getAttribute('href')===current)a.setAttribute('aria-current','page');});
const year=document.querySelector('#year');if(year)year.textContent=new Date().getFullYear().toLocaleString(bengali?'bn-BD':'en',{useGrouping:false});
document.querySelectorAll('.back-top').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});}));
const form=document.querySelector('#interest-form');
if(form){const params=new URLSearchParams(location.search);const kinds={volunteer:'Volunteering',partner:'Partnership',support:'Supporting an initiative'};const initial=params.get('initiative')||kinds[params.get('interest')];const select=form.elements.interest;if(initial&&Array.from(select.options).some(o=>o.value===initial))select.value=initial;form.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;const data=new FormData(form);const chosen=select.options[select.selectedIndex].textContent;document.querySelector('#prepared-message').value=`${copy.title}\n\n${copy.name}: ${data.get('name').trim()}\n${copy.email}: ${data.get('email').trim()}\n${copy.interest}: ${chosen}\n\n${data.get('message').trim()}\n\n${copy.unsent}`;const result=document.querySelector('#message-result');result.hidden=false;result.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth',block:'nearest'});});document.querySelector('#copy-message').addEventListener('click',async()=>{const field=document.querySelector('#prepared-message');try{await navigator.clipboard.writeText(field.value);document.querySelector('#copy-status').textContent=copy.copied;}catch{field.focus();field.select();document.querySelector('#copy-status').textContent=copy.manual;}});document.querySelector('#download-message').addEventListener('click',()=>{const text=document.querySelector('#prepared-message').value;if(!text)return;const url=URL.createObjectURL(new Blob([text],{type:'text/plain;charset=utf-8'}));const link=document.createElement('a');link.href=url;link.download='MATES-expression-of-interest.txt';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);});}


if(form&&bengali){
 for(const field of form.querySelectorAll('input,textarea')){
  field.addEventListener('input',()=>field.setCustomValidity(''));
  field.addEventListener('invalid',()=>{
   field.setCustomValidity('');
   if(field.validity.valueMissing)field.setCustomValidity('এই ঘরটি পূরণ করুন।');
   else if(field.validity.typeMismatch)field.setCustomValidity('একটি সঠিক ইমেইল ঠিকানা লিখুন।');
  });
 }
}


// Browse the initiative spotlight without changing page or shifting the layout.
const slides=Array.from(document.querySelectorAll('.spotlight-slide'));
if(slides.length){
 let index=0;
 const position=document.querySelector('#spotlight-position');
 const number=n=>n.toLocaleString(bengali?'bn-BD':'en',{minimumIntegerDigits:2,useGrouping:false});
 const show=next=>{
  index=(next+slides.length)%slides.length;
  slides.forEach((slide,i)=>{slide.hidden=i!==index;slide.classList.toggle('changing',i===index);});
  position.textContent=`${number(index+1)} / ${number(slides.length)}`;
 };
 document.querySelector('#spotlight-prev').addEventListener('click',()=>show(index-1));
 document.querySelector('#spotlight-next').addEventListener('click',()=>show(index+1));
 show(0);
}
// Filter focus areas while leaving their links and detail pages intact.
for(const filters of document.querySelectorAll('.initiative-filters')){
 const grid=filters.nextElementSibling;
 filters.addEventListener('click',e=>{
  const button=e.target.closest('button[data-filter]');if(!button)return;
  const filter=button.dataset.filter;
  for(const b of filters.querySelectorAll('button'))b.setAttribute('aria-pressed',String(b===button));
  for(const card of grid.querySelectorAll('.program-card'))card.hidden=filter!=='all'&&card.dataset.category!==filter;
 });
}
const progress=document.querySelector('.reading-progress span');
if(progress){
 let scheduled=false;
 const update=()=>{const available=document.documentElement.scrollHeight-window.innerHeight;progress.style.transform=`scaleX(${available>0?Math.max(0,Math.min(1,window.scrollY/available)):0})`;scheduled=false;};
 window.addEventListener('scroll',()=>{if(!scheduled){scheduled=true;requestAnimationFrame(update);}},{passive:true});
 window.addEventListener('resize',update);update();
}
