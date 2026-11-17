"""Render the approved Team directory with editable member profiles."""
import json
import re
from html import escape

from team_page import PORTRAIT


COPY = {
    "en": {
        "title": "Our Team", "home": "Home",
        "intro": "Working together with care, knowledge and commitment.",
        "note": "Member names and photographs will be added soon.",
        "committee": "Executive Committee", "committee_copy": "Our leadership and organisational team.",
        "executives": "Board of Executives", "executives_copy": "Supporting planning, coordination and delivery.",
        "coordinators": "Board of Coordinators", "coordinators_copy": "Connecting people and activities across our initiatives.",
        "pending": "Name to be added", "about": "Learn about MATES",
        "footer": ["About", "Team", "Contact", "Privacy"],
    },
    "bn": {
        "title": "আমাদের টিম", "home": "হোম",
        "intro": "সহমর্মিতা, জ্ঞান ও অঙ্গীকার নিয়ে একসঙ্গে পথচলা।",
        "note": "সদস্যদের নাম ও ছবি শিগগিরই যুক্ত করা হবে।",
        "committee": "কার্যনির্বাহী কমিটি", "committee_copy": "আমাদের নেতৃত্ব ও সাংগঠনিক টিম।",
        "executives": "নির্বাহী পর্ষদ", "executives_copy": "পরিকল্পনা, সমন্বয় ও বাস্তবায়নে সহযোগিতা।",
        "coordinators": "সমন্বয়ক পর্ষদ", "coordinators_copy": "আমাদের বিভিন্ন উদ্যোগের মানুষ ও কার্যক্রমের মধ্যে সংযোগ।",
        "pending": "নাম যুক্ত করা হবে", "about": "মেটস সম্পর্কে জানুন",
        "footer": ["আমাদের সম্পর্কে", "আমাদের টিম", "যোগাযোগ", "গোপনীয়তা"],
    },
}


def member_card(root, member, lang, pending):
    role = member['role_bn'] if lang == 'bn' else member['role']
    name = member.get('name')
    if lang == 'bn':
        name = member.get('name_bn') or name
    portrait = PORTRAIT
    image = member.get('image')
    if image:
        if not image.startswith('assets/team/') or '..' in image.split('/'):
            raise ValueError('Portraits must be local files under assets/team/')
        if not (root / image).is_file():
            raise FileNotFoundError(image)
        image_path = '../' + image if lang == 'bn' else image
        portrait = f'<img src="{escape(image_path, quote=True)}" alt="{escape(name or role, quote=True)}" width="360" height="360" loading="lazy">'
    hidden = '' if image else ' aria-hidden="true"'
    theme = member.get('initiative', '')
    return f'''<article class="member-card" data-member="{escape(member['id'], quote=True)}" data-initiative="{escape(theme, quote=True)}"><div class="member-photo"{hidden}>{portrait}</div><div class="member-copy"><h3>{escape(role)}</h3><p class="member-name{' pending' if not name else ''}">{escape(name or pending)}</p></div></article>'''


def build_team_directories(root):
    members = json.loads((root / 'team.json').read_text(encoding='utf-8'))
    committee = [member for member in members if member['group'] == 'executive-committee']
    presidents = [member for member in committee if member['role'] == 'President']
    leadership = [member for role in ['Secretary', 'Vice President'] for member in committee if member['role'] == role]
    other_members = [member for member in committee if member['role'] not in ['President', 'Secretary', 'Vice President']]
    executives = [member for member in members if member['group'] == 'board-executives']
    coordinators = [member for member in members if member['group'] == 'board-coordinators']
    for lang, copy in COPY.items():
        prefix = 'bn/' if lang == 'bn' else ''
        assets = '../assets/' if prefix else 'assets/'
        path = root / prefix / 'team.html'
        source = path.read_text(encoding='utf-8')
        head, body = re.split(r'<body\b[^>]*>', source, maxsplit=1)
        header = body.split('<main id="main">', 1)[0]
        head = re.sub(r'<link rel="stylesheet"[^>]+inner\.css[^>]*>', '', head)
        head = head.replace('</head>', f'<link rel="stylesheet" href="{assets}team.css?v=1"></head>')
        head = re.sub(r'<title>.*?</title>', f'<title>{copy["title"]} | MATES Foundation</title>', head)
        head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda match: match[1] + copy['title'] + ' | MATES Foundation', head)
        head = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda match: match[1] + escape(copy['intro'], quote=True), head)
        def cards(group):
            return ''.join(member_card(root, member, lang, copy['pending']) for member in group)
        footer_links = ''.join(f'<a href="{route}">{label}</a>' for route, label in zip(['about.html', 'team.html', 'contact.html', 'privacy.html'], copy['footer']))
        main = f'''
<main id="main">
  <section class="directory-title"><div class="directory-wrap"><nav class="directory-breadcrumb" aria-label="{copy['title']}"><a href="index.html">{copy['home']}</a><span aria-hidden="true">/</span><span>{copy['title']}</span></nav><h1>{copy['title']}</h1><p>{copy['intro']}</p><p class="directory-note">{copy['note']}</p></div></section>
  <section class="directory-section" id="executive-committee" aria-labelledby="committee-heading"><div class="directory-wrap"><div class="directory-heading"><h2 id="committee-heading">{copy['committee']}</h2><p>{copy['committee_copy']}</p></div><div class="president-row">{cards(presidents)}</div><div class="leadership-row">{cards(leadership)}</div><div class="committee-members">{cards(other_members)}</div></div></section>
  <section class="directory-section executive-band" id="board-of-executives" aria-labelledby="executives-heading"><div class="directory-wrap"><div class="directory-heading"><h2 id="executives-heading">{copy['executives']}</h2><p>{copy['executives_copy']}</p></div><div class="executives-grid">{cards(executives)}</div></div></section>
  <section class="directory-section" id="board-of-coordinators" aria-labelledby="coordinators-heading"><div class="directory-wrap"><div class="directory-heading"><h2 id="coordinators-heading">{copy['coordinators']}</h2><p>{copy['coordinators_copy']}</p></div><div class="coordinators-grid">{cards(coordinators)}</div><a class="directory-about" href="about.html">{copy['about']} <span aria-hidden="true">→</span></a></div></section>
</main>
<footer class="directory-footer"><div class="directory-wrap"><a class="brand" href="index.html" aria-label="MATES Foundation"><img src="{assets}mates-foundation-logo.png" alt="MATES Foundation" width="1672" height="941"></a><nav aria-label="{copy['title']}">{footer_links}</nav></div></footer>
</body></html>'''
        path.write_text(head + '<body id="top" class="team-directory">' + header + main, encoding='utf-8')
