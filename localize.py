"""Build complete Bengali pages from the English source and reviewed translations.
Uses the Python standard library only. Run through build.py.
"""
from html.parser import HTMLParser
from html import escape
from pathlib import Path
import json,re
ROOT_URL='https://ai4betterair.github.io/MATESFoundation/'
DIGITS=str.maketrans('0123456789','০১২৩৪৫৬৭৮৯')
class BengaliHTML(HTMLParser):
 def __init__(self,mapping):
  super().__init__(convert_charrefs=True);self.mapping=mapping;self.output=[];self.missing=set()
 def translate(self,value):
  key=value.strip()
  if not key:return value
  if key in self.mapping:new=self.mapping[key]
  elif not re.search('[A-Za-z]',key):new=key.translate(DIGITS)
  else:self.missing.add(key);new=key
  return value[:len(value)-len(value.lstrip())]+new+value[len(value.rstrip()):]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  for k,v in attrs:
   if v is None:continue
   if k in ('aria-label','alt','placeholder') and v!='you@example.com':d[k]=self.translate(v)
   if k in ('src','href') and v.startswith('assets/'):d[k]='../'+v
  if tag=='html':d['lang']='bn-BD'
  if tag=='meta' and (d.get('name')=='description' or d.get('property') in ('og:title','og:description')):d['content']=self.translate(d['content'])
  self.output.append('<'+tag+''.join(' '+k+('="'+escape(v,quote=True)+'"' if v is not None else '') for k,v in d.items())+'>')
 def handle_startendtag(self,tag,attrs):
  self.handle_starttag(tag,attrs)
  self.output[-1]=self.output[-1][:-1]+" />"
 def handle_endtag(self,tag):self.output.append('</'+tag+'>')
 def handle_data(self,data):self.output.append(escape(self.translate(data),quote=False))
 def handle_entityref(self,name):self.output.append('&'+name+';')
 def handle_charref(self,name):self.output.append('&#'+name+';')
 def handle_decl(self,decl):self.output.append('<!'+decl+'>')
 def handle_comment(self,data):self.output.append('<!--'+data+'-->')
def controls(text,bengali=False):
 button=re.search(r'<button class="menu-toggle".*?</button>',text).group(0)
 text=text.replace(button,'')
 selector='<div class="nav-tools"><label class="language-control"><span class="language-label">'+('ভাষা' if bengali else 'Language')+'</span><select id="site-language" aria-label="'+('ভাষা নির্বাচন করুন' if bengali else 'Select language')+'"><option value="en" lang="en"'+('' if bengali else ' selected')+'>English</option><option value="bn" lang="bn-BD"'+(' selected' if bengali else '')+'>বাংলা</option></select></label>'+button+'</div>'
 return text.replace('</nav></div></header>','</nav>'+selector+'</div></header>')
def build_locales(root):
 mapping=json.loads((root/'translations-bn.json').read_text())
 (root/'bn').mkdir(exist_ok=True)
 pages=sorted(root.glob('*.html'))
 missing=set()
 for f in pages:
  source=f.read_text()
  source=source.replace('<script src="assets/site.js" defer></script>','<script src="assets/language.js"></script><script src="assets/site.js" defer></script>')
  # Privacy: remember only the language choice, never form entries.
  source=source.replace('<h2>Hosting and cookies</h2>','<p>Your selected language is saved on this device so the website can remember your preference. Form entries are not saved.</p><h2>Hosting and cookies</h2>')
  parser=BengaliHTML(mapping);parser.feed(source);missing|=parser.missing
  bn=''.join(parser.output)
  for lang,text,path in [('en',controls(source),f),('bn-BD',controls(bn,True),root/'bn'/f.name)]:
   # Equivalent static pages are discoverable and shareable without JavaScript.
   alternates=''.join('<link rel="alternate" hreflang="'+l+'" href="'+ROOT_URL+prefix+f.name+'">' for l,prefix in [('en',''),('bn-BD','bn/'),('x-default','')])
   canonical=ROOT_URL+('bn/' if lang=='bn-BD' else '')+f.name
   text=text.replace('</head>',alternates+'<link rel="canonical" href="'+canonical+'"></head>')
   path.write_text(text)
 if missing:raise ValueError('Missing Bengali translations: '+repr(sorted(missing)))
 (root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+ROOT_URL+prefix+f.name+'</loc></url>' for f in pages if f.name!='404.html' for prefix in ('','bn/'))+'</urlset>')
