"""Apply the homepage's visual system to the remaining bilingual pages.

Runs after localisation and approved editorial edits so existing translated
content, form behaviour and future team profiles remain authoritative.
"""
import re


INITIATIVES = ["education", "scholarships", "community", "health", "emergency", "skills"]


def redesign_inner_pages(root):
    for prefix in ("", "bn/"):
        homepage = (root / prefix / "index.html").read_text(encoding="utf-8")
        header = homepage.split('<body id="top">', 1)[1].split('<main id="main">', 1)[0]
        footer = '<section class="closing">' + homepage.rsplit('<section class="closing">', 1)[1]
        footer = footer.replace('</main>', '', 1)
        footer = footer.replace(' aria-current="page"', '')
        fonts = homepage.split('<link rel="preconnect"', 1)[1].split('<link rel="stylesheet"', 1)[0]
        fonts = '<link rel="preconnect"' + fonts
        assets = "../assets/" if prefix else "assets/"
        for page in sorted((root / prefix).glob("*.html")):
            if page.name == "index.html":
                continue
            source = page.read_text(encoding="utf-8")
            head, rest = re.split(r'<body\b[^>]*>', source, maxsplit=1)
            main = rest.split('<main id="main">', 1)[1].split('</main>', 1)[0]
            head = re.sub(r'<link rel="stylesheet"[^>]+>', '', head)
            head = head.replace('site.js?v=4', 'site.js?v=5')
            head = head.replace('</head>', fonts + f'<link rel="stylesheet" href="{assets}home.css?v=1"><link rel="stylesheet" href="{assets}inner.css?v=1"></head>')
            stem = page.stem
            active = "initiatives.html" if stem in INITIATIVES else page.name
            page_header = header.replace(' aria-current="page"', '')
            page_header = page_header.replace(f'href="{active}"', f'href="{active}" aria-current="page"')
            # Language links always lead to the equivalent page, including 404.
            page_header = page_header.replace('href="../index.html" lang="en"', f'href="../{page.name}" lang="en"')
            page_header = page_header.replace('href="index.html" lang="en"', f'href="{page.name}" lang="en"')
            page_header = page_header.replace('href="bn/index.html" lang="bn"', f'href="bn/{page.name}" lang="bn"')
            page_header = page_header.replace('href="index.html" lang="bn"', f'href="{page.name}" lang="bn"')
            emblem = f'<img src="{assets}mates-foundation-logo.png" width="1672" height="941" alt="">'
            if stem in INITIATIVES:
                emblem = f'<span class="initiative-icon icon-{INITIATIVES.index(stem)}"></span>'
            main = main.replace('</h1>', '</h1><span class="gold-rule" aria-hidden="true"></span>', 1)
            hero_end = main.find('</section>')
            main = main[:hero_end] + f'<div class="page-emblem" aria-hidden="true">{emblem}</div>' + main[hero_end:]
            # Reuse the approved homepage icons across the six initiative cards.
            for index, slug in enumerate(INITIATIVES):
                pattern = r'(<a class="program-card"[^>]*data-initiative="' + slug + r'"[^>]*>.*?<span class="program-icon">)<svg.*?</svg>(</span>)'
                main = re.sub(pattern, lambda m: m[1] + f'<span class="initiative-icon icon-{index}" aria-hidden="true"></span>' + m[2], main, flags=re.S)
            classes = f'inner-page page-{stem}'
            if stem in INITIATIVES:
                classes += f' initiative-detail theme-{stem}'
            html = head + f'<body id="top" class="{classes}">' + page_header + '<main id="main">' + main + '</main>' + footer
            page.write_text(html, encoding="utf-8")
