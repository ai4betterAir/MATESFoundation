"""Create the Team page from editable roles, names and optional portrait paths."""
from html import escape
import json

PORTRAIT='<svg viewBox="0 0 120 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="60" cy="42" r="17"/><path d="M26 101c0-22 13-35 34-35s34 13 34 35" stroke-linecap="round"/></svg>'

def create_team_page(root,save,intro):
    members=json.loads((root/'team.json').read_text())
    translations=json.loads((root/'translations-bn.json').read_text())
    translations.update({
        'Team':'টিম', 'Our team':'আমাদের টিম', 'OUR TEAM':'আমাদের টিম',
        'Team | MATES Foundation':'আমাদের টিম | মেটস ফাউন্ডেশন',
        'The team and committee roles behind MATES Foundation.':'মেটস ফাউন্ডেশনের টিম ও পরিচালনা কমিটির পদসমূহ।',
        'One team.':'একটি টিম।','A shared purpose.':'একটি অভিন্ন লক্ষ্য।',
        'Working together to turn compassion, knowledge and commitment into a better society.':'সহমর্মিতা, জ্ঞান ও অঙ্গীকার নিয়ে একসঙ্গে উন্নত সমাজ গড়ার পথে।',
        'Our team page is taking shape. Names and photographs will be added soon.':'আমাদের টিমের পরিচিতি সাজানো হচ্ছে। সদস্যদের নাম ও ছবি শিগগিরই যুক্ত করা হবে।',
        'LEADERSHIP & COMMITTEE':'নেতৃত্ব ও পরিচালনা কমিটি',
        'People behind our purpose.':'আমাদের পথচলার মানুষ।',
        'INITIATIVE COORDINATORS':'উদ্যোগের সমন্বয়ক',
        'Six initiatives. Shared commitment.':'ছয়টি উদ্যোগ। সম্মিলিত অঙ্গীকার।',
        'Name to be added':'নাম যুক্ত করা হবে',
        'Want to be part of the effort?':'আমাদের সঙ্গে যুক্ত হতে চান?',
        'Share your time, skills or ideas and explore how you can contribute to the MATES community.':'আপনার সময়, দক্ষতা বা ভাবনা নিয়ে এগিয়ে আসুন। মেটসের সঙ্গে কাজ করার সুযোগ সম্পর্কে জানুন।',
        'Explore ways to get involved':'যুক্ত হওয়ার উপায় জানুন'
    })
    def card(member):
        role=member['role'];translations[role]=member['role_bn']
        name=member.get('name') or 'Name to be added'
        if member.get('name'):
            translations[name]=member.get('name_bn') or name
        initiative=member.get('initiative')
        theme=' data-initiative="'+escape(initiative,quote=True)+'"' if initiative else ''
        if member.get('image'):
            path=member['image']
            if not path.startswith('assets/team/') or '..' in path.split('/'):
                raise ValueError('Portraits must be local files under assets/team/')
            if not (root/path).is_file():raise FileNotFoundError(path)
            portrait='<img src="'+escape(path,quote=True)+'" alt="'+escape(name,quote=True)+'" width="360" height="360" loading="lazy" decoding="async">'
        else:portrait=PORTRAIT
        return '<article class="team-card"'+theme+'><div class="team-photo"'+(' aria-hidden="true"' if not member.get('image') else '')+'>'+portrait+'</div><h3>'+escape(role)+'</h3><p class="team-member-name'+(' pending' if not member.get('name') else '')+'">'+escape(name)+'</p></article>'
    body=intro('OUR TEAM','One team.<br><em>A shared purpose.</em>','Working together to turn compassion, knowledge and commitment into a better society.')
    body+='<section class="section team-section"><div class="wrap"><p class="team-intro-note">Our team page is taking shape. Names and photographs will be added soon.</p><div class="team-section-heading"><span class="eyebrow">LEADERSHIP &amp; COMMITTEE</span><h2>People behind our purpose.</h2></div><div class="team-grid committee-grid">'+''.join(card(m) for m in members if m['group']=='committee')+'</div></div></section>'
    body+='<section class="section pale team-section"><div class="wrap"><div class="team-section-heading"><span class="eyebrow">INITIATIVE COORDINATORS</span><h2>Six initiatives. Shared commitment.</h2></div><div class="team-grid coordinator-grid">'+''.join(card(m) for m in members if m['group']=='initiatives')+'</div></div></section>'
    body+='<section class="section"><div class="wrap team-invitation"><div><h2>Want to be part of the effort?</h2><p>Share your time, skills or ideas and explore how you can contribute to the MATES community.</p></div><a class="button" href="get-involved.html">Explore ways to get involved <span>↗</span></a></div></section>'
    save('team.html','Team','The team and committee roles behind MATES Foundation.',body)
    (root/'translations-bn.json').write_text(json.dumps(translations,ensure_ascii=False,indent=2)+'\n')
