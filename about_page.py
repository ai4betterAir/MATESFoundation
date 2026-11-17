"""Render the approved organisational About page in both languages."""
import re
from html import escape


COPY = {
    "en": {
        "home": "Home", "about": "About", "title": "About MATES Foundation",
        "intro": "People coming together with a shared commitment to a better society.",
        "who": "Who we are",
        "paragraphs": [
            "MATES Foundation brings together people who want to contribute their time, knowledge and practical skills to support others. Our work is guided by care for people, respect for dignity and a belief in the value of shared effort.",
            "We aim to connect willing people with community needs through education, support and opportunities to learn and grow.",
        ],
        "photo": "Illustration of a plant, notebook and pen on a sunlit desk",
        "mission": "Our mission",
        "mission_copy": "Bring people together to support learning, respond thoughtfully to community needs and help create opportunities.",
        "vision": "Our vision",
        "vision_copy": "A society where people feel supported, learning is encouraged and everyone has the chance to move forward.",
        "values": "The values we work by",
        "value_rows": [
            ("Dignity", "Treat people with care and respect."),
            ("Inclusion", "Welcome people from different backgrounds."),
            ("Compassion", "Listen carefully and respond thoughtfully."),
            ("Responsibility", "Make careful commitments and share information clearly."),
        ],
        "approach": "How we work",
        "steps": [
            ("Listen to the need", "Understand what matters to people and communities."),
            ("Work together", "Bring time, skills and resources into a shared effort."),
            ("Act with care", "Plan practical support and communicate clearly."),
        ],
        "team": "How our team is organised",
        "groups": [
            ("Executive Committee", "Provides overall direction and oversight for the organisation."),
            ("Board of Executives", "Supports planning, coordination and implementation of our work."),
            ("Board of Coordinators", "Helps organise activities and maintain smooth coordination across our initiatives."),
        ],
        "profiles": "Names and photographs will be added as team profiles are confirmed.",
        "meet": "Meet our team", "explore": "Explore our initiatives",
        "clarity": "Building with clarity",
        "clarity_copy": "Confirmed program details, participation arrangements and official contact channels will be shared as they become available.",
        "footer": ["About", "Team", "Contact", "Privacy"],
    },
    "bn": {
        "home": "হোম", "about": "আমাদের সম্পর্কে", "title": "মেটস ফাউন্ডেশন সম্পর্কে",
        "intro": "সুন্দর সমাজ গড়ার অঙ্গীকার নিয়ে মানুষের একসঙ্গে পথচলা।",
        "who": "আমরা কারা",
        "paragraphs": [
            "যাঁরা নিজের সময়, জ্ঞান ও ব্যবহারিক দক্ষতা দিয়ে মানুষের পাশে দাঁড়াতে চান, তাঁদের একত্র করে মেটস ফাউন্ডেশন। মানুষের প্রতি যত্ন, মর্যাদার প্রতি সম্মান এবং সম্মিলিত প্রচেষ্টার মূল্যবোধ আমাদের পথ দেখায়।",
            "শিক্ষা, সহায়তা এবং শেখার ও এগিয়ে যাওয়ার সুযোগের মাধ্যমে সমাজের প্রয়োজনের সঙ্গে সহযোগিতায় আগ্রহী মানুষকে যুক্ত করাই আমাদের প্রচেষ্টা।",
        ],
        "photo": "রোদে আলোকিত টেবিলে গাছ, খাতা ও কলমের প্রতীকী ছবি",
        "mission": "আমাদের লক্ষ্য",
        "mission_copy": "শেখার সুযোগ বাড়াতে, সমাজের প্রয়োজনে বিবেচনার সঙ্গে সাড়া দিতে এবং নতুন সম্ভাবনা তৈরি করতে মানুষকে একত্র করা।",
        "vision": "আমাদের স্বপ্ন",
        "vision_copy": "এমন একটি সমাজ, যেখানে মানুষ সহায়তা পায়, শেখার উৎসাহ থাকে এবং সবার এগিয়ে যাওয়ার সুযোগ থাকে।",
        "values": "আমাদের মূল্যবোধ",
        "value_rows": [
            ("মর্যাদা", "প্রতিটি মানুষকে যত্ন ও সম্মানের সঙ্গে দেখা।"),
            ("অন্তর্ভুক্তি", "সব পটভূমির মানুষকে স্বাগত জানানো।"),
            ("সহমর্মিতা", "মন দিয়ে শোনা এবং বিবেচনা করে সাড়া দেওয়া।"),
            ("দায়িত্বশীলতা", "ভেবেচিন্তে অঙ্গীকার করা এবং স্পষ্টভাবে তথ্য জানানো।"),
        ],
        "approach": "আমরা যেভাবে কাজ করি",
        "steps": [
            ("প্রয়োজন বুঝি", "মানুষ ও সমাজের কাছে কী জরুরি, তা জানার চেষ্টা করি।"),
            ("একসঙ্গে কাজ করি", "সময়, দক্ষতা ও সম্পদ একত্র করে এগিয়ে যাই।"),
            ("যত্ন নিয়ে এগোই", "বাস্তবসম্মত সহায়তার পরিকল্পনা করি এবং স্পষ্টভাবে জানাই।"),
        ],
        "team": "আমাদের টিমের কাঠামো",
        "groups": [
            ("কার্যনির্বাহী কমিটি", "সামগ্রিক দিকনির্দেশনা ও তত্ত্বাবধান।"),
            ("নির্বাহী পর্ষদ", "পরিকল্পনা, সমন্বয় ও বাস্তবায়নে সহযোগিতা।"),
            ("সমন্বয়ক পর্ষদ", "বিভিন্ন উদ্যোগের কার্যক্রম ও যোগাযোগে সমন্বয়।"),
        ],
        "profiles": "পরিচিতি নিশ্চিত হলে সদস্যদের নাম ও ছবি যুক্ত করা হবে।",
        "meet": "আমাদের টিমকে জানুন", "explore": "আমাদের উদ্যোগ দেখুন",
        "clarity": "তথ্যে স্পষ্টতা",
        "clarity_copy": "কর্মসূচির বিস্তারিত, অংশগ্রহণের পদ্ধতি ও আনুষ্ঠানিক যোগাযোগের তথ্য নিশ্চিত হলে প্রকাশ করা হবে।",
        "footer": ["আমাদের সম্পর্কে", "আমাদের টিম", "যোগাযোগ", "গোপনীয়তা"],
    },
}


def build_about_pages(root):
    for lang, copy in COPY.items():
        prefix = "bn/" if lang == "bn" else ""
        assets = "../assets/" if prefix else "assets/"
        path = root / prefix / "about.html"
        source = path.read_text(encoding="utf-8")
        head, body = re.split(r'<body\b[^>]*>', source, maxsplit=1)
        header = body.split('<main id="main">', 1)[0]
        head = re.sub(r'<link rel="stylesheet"[^>]+inner\.css[^>]*>', '', head)
        head = head.replace('</head>', f'<link rel="stylesheet" href="{assets}about.css?v=1"></head>')
        head = re.sub(r'<title>.*?</title>', f'<title>{copy["title"]} | MATES Foundation</title>', head)
        head = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda match: match[1] + escape(copy['intro'], quote=True), head)
        head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda match: match[1] + copy['title'] + ' | MATES Foundation', head)
        paragraphs = ''.join(f'<p>{escape(text)}</p>' for text in copy['paragraphs'])
        values = ''.join(f'<div class="value-row"><dt>{title}</dt><dd>{description}</dd></div>' for title, description in copy['value_rows'])
        steps = ''.join(f'<article><span class="about-symbol step-{index}" aria-hidden="true"></span><div><h3>{title}</h3><p>{description}</p></div></article>' for index, (title, description) in enumerate(copy['steps']))
        groups = ''.join(f'<article><span class="about-symbol group-symbol" aria-hidden="true"></span><h3>{title}</h3><p>{description}</p></article>' for title, description in copy['groups'])
        footer_links = ''.join(f'<a href="{route}">{label}</a>' for route, label in zip(['about.html', 'team.html', 'contact.html', 'privacy.html'], copy['footer']))
        main = f'''
<main id="main">
  <section class="about-title">
    <div class="about-wrap">
      <nav class="about-breadcrumb" aria-label="{copy['about']}"><a href="index.html">{copy['home']}</a><span aria-hidden="true">/</span><span>{copy['about']}</span></nav>
      <h1>{copy['title']}</h1><span class="gold-rule" aria-hidden="true"></span>
      <p>{copy['intro']}</p>
    </div>
  </section>
  <div class="about-wrap about-content">
    <section class="who-section" aria-labelledby="who-heading">
      <h2 id="who-heading">{copy['who']}</h2>
      <div class="who-grid">
        <div class="about-photo"><img src="{assets}about-artwork.webp" width="1024" height="1536" alt="{copy['photo']}" fetchpriority="high"></div>
        <div class="who-copy">{paragraphs}</div>
      </div>
    </section>
    <section class="mission-vision" aria-label="{copy['mission']} / {copy['vision']}">
      <article><span class="about-symbol mission-symbol" aria-hidden="true"></span><div><h2>{copy['mission']}</h2><p>{copy['mission_copy']}</p></div></article>
      <article><span class="about-symbol vision-symbol" aria-hidden="true"></span><div><h2>{copy['vision']}</h2><p>{copy['vision_copy']}</p></div></article>
    </section>
    <section class="values-section" id="values" aria-labelledby="values-heading"><h2 id="values-heading">{copy['values']}</h2><dl>{values}</dl></section>
    <section class="approach-section" aria-labelledby="approach-heading"><h2 id="approach-heading">{copy['approach']}</h2><div class="approach-grid">{steps}</div></section>
    <section class="organisation-section" aria-labelledby="team-heading"><h2 id="team-heading">{copy['team']}</h2><div class="organisation-grid">{groups}</div><p class="profile-note">{copy['profiles']}</p><div class="about-links"><a href="team.html">{copy['meet']} <span aria-hidden="true">→</span></a><a href="initiatives.html">{copy['explore']} <span aria-hidden="true">→</span></a></div></section>
    <aside class="clarity-panel"><span class="about-symbol clarity-symbol" aria-hidden="true"></span><div><h2>{copy['clarity']}</h2><p>{copy['clarity_copy']}</p></div></aside>
  </div>
</main>
<footer class="about-footer"><div class="about-wrap"><a class="brand" href="index.html" aria-label="MATES Foundation"><img src="{assets}mates-foundation-logo.png" width="1672" height="941" alt="MATES Foundation"></a><nav aria-label="{copy['about']}">{footer_links}</nav></div></footer>
</body></html>'''
        path.write_text(head + '<body id="top" class="about-page">' + header + main, encoding="utf-8")
