"""Render the approved bilingual homepage after the existing editorial build."""
from html import escape


COPY = {
    "en": {
        "nav": ["Home", "About", "Initiatives", "Team", "Contact"],
        "title": "Together for a Better Society.",
        "headline": "Together for<br>a Better<br><em>Society.</em>",
        "intro": "Education, compassion and opportunity. Bringing people together to support our communities.",
        "explore": "Explore our initiatives", "join": "Get involved",
        "event_label": "COMMUNITY SUPPORT · 2026",
        "event_title": "Sharing the Joy of<br>Ramadan &amp; Eid",
        "event_copy": "Food support for families during Ramadan and Eid.",
        "story": "Explore the story", "initiatives": "Six ways to make a difference.",
        "cards": [
            ("Education", "Support quality education and learning opportunities in our communities."),
            ("Scholarship Program", "Help students pursue their education through thoughtfully designed support."),
            ("Community Support", "Stand by families through community connection and practical support."),
            ("Health & Blood Donation", "Health awareness, blood grouping and voluntary donation."),
            ("Emergency Assistance", "Work towards practical support for people facing unexpected hardship."),
            ("Skills Development", "Build practical skills and capabilities for education, work and self-reliance."),
        ],
        "closing": "A better society starts with all of us.", "volunteer": "Become a volunteer",
        "footer": "Working together for education, compassion and opportunity.",
        "skip": "Skip to content", "menu": "Menu", "language": "Select language",
        "photo_alt": "Illustration of hands sharing a food parcel",
        "event_alt": "Illustration of food supplies with a lantern for Ramadan",
        "privacy": "Privacy & website information", "copyright": "© 2026 MATES Foundation. All rights reserved.",
    },
    "bn": {
        "nav": ["হোম", "আমাদের সম্পর্কে", "আমাদের উদ্যোগ", "আমাদের দল", "যোগাযোগ"],
        "title": "একসঙ্গে গড়ি একটি সুন্দর সমাজ।",
        "headline": "একসঙ্গে গড়ি<br>একটি সুন্দর<br><em>সমাজ।</em>",
        "intro": "শিক্ষা, সহমর্মিতা ও সুযোগ। মানুষের পাশে দাঁড়াতে আমাদের এই পথচলা।",
        "explore": "আমাদের উদ্যোগ দেখুন", "join": "যুক্ত হোন",
        "event_label": "সমাজসেবা · ২০২৬",
        "event_title": "রমজান ও ঈদের<br>আনন্দ ভাগ করে নিই",
        "event_copy": "রমজান ও ঈদে অসহায় পরিবারের জন্য খাদ্যসহায়তা।",
        "story": "বিস্তারিত দেখুন", "initiatives": "মানুষের পাশে দাঁড়ানোর ছয়টি উদ্যোগ",
        "cards": [
            ("শিক্ষা", "শিক্ষা ও শেখার সুযোগ পৌঁছে দেওয়ার প্রচেষ্টা।"),
            ("শিক্ষাবৃত্তি", "শিক্ষার্থীদের পড়াশোনা এগিয়ে নিতে সহায়তার উদ্যোগ।"),
            ("কমিউনিটি সহায়তা", "পরিবার ও সমাজের প্রয়োজনে পাশে থাকার প্রচেষ্টা।"),
            ("স্বাস্থ্য ও রক্তদান", "স্বাস্থ্যসচেতনতা, রক্তের গ্রুপ নির্ণয় ও স্বেচ্ছায় রক্তদান।"),
            ("জরুরি সহায়তা", "দুর্যোগ ও বিপদে মানুষের পাশে দাঁড়ানোর উদ্যোগ।"),
            ("দক্ষতা উন্নয়ন", "শিক্ষা ও কর্মজীবনের জন্য ব্যবহারিক দক্ষতা শেখার সুযোগ।"),
        ],
        "closing": "সুন্দর সমাজ গড়ার শুরু আমাদের সবার হাত ধরে।", "volunteer": "স্বেচ্ছাসেবী হোন",
        "footer": "শিক্ষা, সহমর্মিতা ও সুযোগের মাধ্যমে মানুষের পাশে থাকার অঙ্গীকার।",
        "skip": "মূল বিষয়বস্তুতে যান", "menu": "মেনু", "language": "ভাষা নির্বাচন করুন",
        "photo_alt": "খাদ্যসহায়তার একটি প্যাকেট তুলে দেওয়ার প্রতীকী ছবি",
        "event_alt": "রমজানের খাদ্যসামগ্রী ও ফানুসের প্রতীকী ছবি",
        "privacy": "গোপনীয়তা ও ওয়েবসাইটের তথ্য", "copyright": "© ২০২৬ মেটস ফাউন্ডেশন। সর্বস্বত্ব সংরক্ষিত।",
    },
}


def build_homepages(root):
    routes = ["index.html", "about.html", "initiatives.html", "team.html", "contact.html"]
    slugs = ["education", "scholarships", "community", "health", "emergency", "skills"]
    base = "https://ai4betterair.github.io/MATESFoundation/"
    for lang, copy in COPY.items():
        assets = "../assets/" if lang == "bn" else "assets/"
        prefix = "bn/" if lang == "bn" else ""
        nav = "".join(f'<a href="{route}"'+(' aria-current="page"' if i == 0 else '')+f'>{label}</a>' for i, (route, label) in enumerate(zip(routes, copy["nav"])))
        language_links = ('../index.html', 'index.html') if lang == 'bn' else ('index.html', 'bn/index.html')
        language = ''.join(f'<a href="{href}" lang="{code}" data-language="{code}"'+(' aria-current="true"' if code == lang else '')+f'>{label}</a>' for href, code, label in zip(language_links, ['en', 'bn'], ['English', 'বাংলা']))
        logo = f'<img src="{assets}mates-foundation-logo.png" width="1672" height="941" alt="MATES Foundation">'
        cards = "".join(f'''<a class="initiative-card card-{slug}" href="{slug}.html"><span class="initiative-icon icon-{i}" aria-hidden="true"></span><div><h3>{escape(title)}</h3><p>{escape(description)}</p></div><span class="card-arrow" aria-hidden="true">→</span></a>''' for i, (slug, (title, description)) in enumerate(zip(slugs, copy["cards"])))
        html = f'''<!doctype html>
<html lang="{'bn-BD' if lang == 'bn' else 'en'}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{copy['title']} | MATES Foundation</title>
<meta name="description" content="{escape(copy['intro'], quote=True)}"><meta name="theme-color" content="#062b4e">
<meta property="og:title" content="{copy['title']} | MATES Foundation"><meta property="og:description" content="{escape(copy['intro'], quote=True)}"><meta property="og:type" content="website"><meta property="og:image" content="{base}assets/mates-foundation-logo.png">
<link rel="canonical" href="{base}{prefix}index.html">
<link rel="alternate" hreflang="en" href="{base}index.html"><link rel="alternate" hreflang="bn-BD" href="{base}bn/index.html"><link rel="alternate" hreflang="x-default" href="{base}index.html">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Text:ital@0;1&family=Noto+Sans+Bengali:wght@400;500;600;700&family=Noto+Serif+Bengali:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{assets}home.css?v=1"><script src="{assets}language.js"></script><script src="{assets}home.js?v=1" defer></script>
</head>
<body id="top"><a class="skip" href="#main">{copy['skip']}</a>
<header class="home-header"><div class="header-inner"><a class="brand" href="index.html" aria-label="MATES Foundation">{logo}</a>
<button class="menu-toggle" aria-expanded="false" aria-controls="navigation">{copy['menu']} <span aria-hidden="true">☰</span></button>
<nav id="navigation" aria-label="{copy['menu']}">{nav}</nav><div class="language-switch" aria-label="{copy['language']}">{language}</div></div></header>
<main id="main">
<section class="hero"><div class="hero-copy"><h1>{copy['headline']}</h1><span class="gold-rule" aria-hidden="true"></span><p>{copy['intro']}</p><div class="hero-actions"><a class="button" href="initiatives.html">{copy['explore']} <span aria-hidden="true">→</span></a><a class="button outline" href="get-involved.html">{copy['join']} <span aria-hidden="true">→</span></a></div></div>
<div class="hero-visual"><img src="{assets}homepage-artwork.webp" width="1024" height="1536" alt="{copy['photo_alt']}" fetchpriority="high"></div></section>
<section class="event container" aria-labelledby="event-title"><div class="event-visual"><img src="{assets}homepage-artwork.webp" width="1024" height="1536" alt="{copy['event_alt']}" loading="lazy"></div><div class="event-copy"><span class="event-label">{copy['event_label']}</span><h2 id="event-title">{copy['event_title']}</h2><p>{copy['event_copy']}</p><a class="story-link" href="community.html">{copy['story']} <span aria-hidden="true">→</span></a></div></section>
<section class="initiatives container" aria-labelledby="initiatives-title"><h2 id="initiatives-title">{copy['initiatives']}</h2><span class="gold-rule" aria-hidden="true"></span><div class="initiative-grid">{cards}</div></section>
<section class="closing"><div class="closing-inner"><h2>{copy['closing']}</h2><a class="button" href="get-involved.html#volunteer">{copy['volunteer']} <span aria-hidden="true">→</span></a></div></section>
</main>
<footer><div class="footer-main"><a class="brand" href="index.html">{logo}</a><p>{copy['footer']}</p><nav aria-label="{copy['menu']}">{nav}</nav></div><div class="footer-bottom"><span>{copy['copyright']}</span><a href="privacy.html">{copy['privacy']}</a></div></footer>
</body></html>'''
        (root / prefix / "index.html").write_text(html, encoding="utf-8")
