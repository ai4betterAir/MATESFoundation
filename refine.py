"""Editorial and interactive presentation layer, run before localisation."""
from pathlib import Path
import json

def refresh_design(root,programs,icon):
    translations=json.loads((root/'translations-bn.json').read_text())
    edits=[
    ('A better tomorrow begins with how we care for one another today. Together, we can open doors, lift each other up and create opportunities that last.',
     'Everyone deserves the chance to learn, feel supported and build a better future. MATES brings people together to turn that belief into practical action.',
     'শেখার সুযোগ, প্রয়োজনের সময় সহায়তা আর সুন্দর ভবিষ্যৎ গড়ার অধিকার সবার। এই বিশ্বাসকে কাজে রূপ দিতে মানুষকে একত্র করে মেটস ফাউন্ডেশন।'),
    ('PEOPLE AT THE HEART OF CHANGE','PEOPLE FIRST. PURPOSE ALWAYS.','মানুষের পাশে, উন্নত সমাজের পথে'),
    ('One shared purpose.','Six initiatives. One purpose.','ছয়টি উদ্যোগ। একটি লক্ষ্য।'),
    ('A world of possibilities.','Together for a Better Society.','উন্নত সমাজ গড়তে একসঙ্গে।'),
    ('A helping hand.','Opportunity to learn.','শেখার সুযোগ।'),
    ('An open door.','Support when it matters.','প্রয়োজনের সময়ে সহায়তা।'),
    ('A shared future.','A future we build together.','একসঙ্গে গড়া ভবিষ্যৎ।'),
    ('We believe a better society is something we build together.','A better society grows when people have the support to move forward.','মানুষ এগিয়ে যাওয়ার সহায়তা পেলেই সমাজ এগিয়ে যায়।'),
    ('MATES Foundation is a charitable foundation with a simple purpose: to bring people together for the good of society. Our initiatives connect education, care and practical opportunity with a spirit of community.',
     'MATES Foundation connects people who want to help with the needs that matter in our communities. Our focus spans education, scholarships, community wellbeing, health, emergency assistance and practical skills.',
     'সমাজের প্রয়োজন আর সাহায্য করতে চাওয়া মানুষের মধ্যে সংযোগ গড়তে চায় মেটস ফাউন্ডেশন। শিক্ষা, বৃত্তি, সামাজিক কল্যাণ, স্বাস্থ্য, জরুরি সহায়তা ও ব্যবহারিক দক্ষতা—এই ছয়টি ক্ষেত্রেই আমাদের পথচলা।'),
    ('From supporting a learner’s next step to standing beside someone in difficult times, our vision begins with dignity, inclusion and a willingness to help.',
     'Our starting point is simple: listen with respect, understand the need and work together on a useful response. Every person deserves dignity, and every contribution can have a purpose.',
     'আমরা শুরু করতে চাই মন দিয়ে শোনা, প্রয়োজন বোঝা এবং একসঙ্গে কার্যকর সহায়তার পথ খোঁজার মাধ্যমে। প্রতিটি মানুষের মর্যাদা আছে, আর প্রতিটি অবদানই কাজে আসতে পারে।'),
    ('Six ways to make','Different needs.','প্রয়োজন নানা রকম।'),
    ('a meaningful difference.','One shared commitment.','পাশে থাকার অঙ্গীকার এক।'),
    ('Different needs. One shared commitment.','Find the cause that speaks to you.','আপনার আগ্রহের উদ্যোগটি বেছে নিন।'),
    ('Explore the areas at the heart of our vision.','Explore our six initiatives and see where you could contribute.','আমাদের ছয়টি উদ্যোগ জানুন, খুঁজে নিন আপনার অবদান রাখার জায়গা।'),
    ('Our focus areas are introduced here. Specific activities, eligibility and participation arrangements will be shared as each program is established.',
     'These are our areas of focus. Program dates, eligibility and ways to participate will be announced as activities are confirmed.',
     'এগুলো আমাদের কাজের মূল ক্ষেত্র। কার্যক্রম নিশ্চিত হলে সময়সূচি, অংশগ্রহণের শর্ত ও পদ্ধতি জানানো হবে।'),
    ('Good things happen','A better society needs','উন্নত সমাজ গড়তে চাই'),
    ('when we come together.','all of us.','আমাদের সবার অংশগ্রহণ।'),
    ('Find your way to help','Take the next step','এগিয়ে আসুন'),
    ('Your time. Your skills.','What can you bring?','আপনি কীভাবে যুক্ত হতে চান?'),
    ('Your willingness to care.','Start with what you can offer.','আপনার সামর্থ্য দিয়েই শুরু হোক।'),
    ('Bring your energy and compassion to a shared purpose.','Give your time, share your experience and help shape community activities.','সময় দিন, অভিজ্ঞতা ভাগ করুন, সামাজিক উদ্যোগ গড়ে তুলতে সাহায্য করুন।'),
    ('Explore how your organisation can help create opportunity.','Bring your organisation’s knowledge, resources and ideas into a shared effort.','আপনার প্রতিষ্ঠানের জ্ঞান, সম্পদ ও ভাবনা নিয়ে যৌথ প্রচেষ্টায় যুক্ত হোন।'),
    ('Find a meaningful way to contribute to the foundation’s vision.','Choose an initiative and explore practical ways to help it grow.','একটি উদ্যোগ বেছে নিন, সেটিকে এগিয়ে নিতে সহায়তা করুন।'),
    ('Helping make learning more accessible, so more people have the opportunity to grow.','Learning support, mentoring and resources to help more people move forward.','পড়াশোনায় সহায়তা, পরামর্শ ও শিক্ষা উপকরণের মাধ্যমে এগিয়ে যাওয়ার সুযোগ।'),
    ('Supporting educational aspirations where financial barriers stand in the way.','Helping students pursue their education when financial barriers get in the way.','আর্থিক বাধা পেরিয়ে শিক্ষার্থীদের পড়াশোনা চালিয়ে যেতে সহায়তার উদ্যোগ।'),
    ('Bringing people together through care, practical support and community connection.','Building connection and practical support for people in our communities.','মানুষের সঙ্গে মানুষের সম্পর্ক গড়া এবং প্রয়োজন অনুযায়ী বাস্তব সহায়তার উদ্যোগ।'),
    ('Encouraging health awareness and voluntary blood donation through community participation.','Encouraging health awareness, blood grouping and voluntary blood donation with authorised providers.','অনুমোদিত প্রতিষ্ঠানের সহযোগিতায় স্বাস্থ্যসচেতনতা, রক্তের গ্রুপ নির্ণয় ও স্বেচ্ছায় রক্তদানে উৎসাহ।'),
    ('A focus on compassionate, practical support for people facing unexpected hardship.','Working towards practical, compassionate support when unexpected hardship strikes.','আকস্মিক সংকটে সহমর্মিতা ও প্রয়োজনীয় সহায়তা নিয়ে পাশে দাঁড়ানোর প্রচেষ্টা।'),
    ('Helping people develop practical capabilities, confidence and pathways to opportunity.','Practical learning and mentoring to build confidence and prepare for new opportunities.','ব্যবহারিক শিক্ষা ও পরামর্শের মাধ্যমে আত্মবিশ্বাস বাড়ানো এবং নতুন সুযোগের প্রস্তুতি।'),
    ('No registration status, tax-deductibility, partnerships or delivered outcomes are claimed on this website. We believe these details should be shared accurately and transparently.',
     'We will share confirmed program information clearly, including how to participate, who activities are designed for and how support is managed. Trust grows through accurate information and responsible commitments.',
     'কার্যক্রমে কীভাবে অংশ নেওয়া যাবে, কাদের জন্য তা আয়োজন করা হচ্ছে এবং সহায়তা কীভাবে পরিচালিত হবে—এসব নিশ্চিত তথ্য আমরা স্পষ্টভাবে জানাতে চাই। সঠিক তথ্য ও দায়িত্বশীল অঙ্গীকারই আস্থার ভিত্তি।')]
    for old,new,bn in edits:translations[new]=bn
    # Bengali editorial refinements avoid literal, fragmented slogans.
    translations.update({'Together for a':'উন্নত সমাজ গড়তে','Better Society.':'একসঙ্গে।',
       'MATES Community Support':'মেটস সামাজিক সহায়তা','MATES INITIATIVES':'মেটসের উদ্যোগ',
       'Explore initiative':'বিস্তারিত জানুন','Get to know MATES':'মেটসকে জানুন',
       'Many ways to help.':'সহায়তার পথ অনেক।','Our intended focus':'আমাদের কাজের লক্ষ্য'})
    new_text={
      'EXPLORE WHAT MATTERS TO YOU':'আপনার আগ্রহের ক্ষেত্রটি জানুন',
      'Learning & opportunity':'শিক্ষা ও সম্ভাবনা','Care & support':'যত্ন ও সহায়তা','All initiatives':'সব উদ্যোগ',
      'Filter initiatives':'উদ্যোগ বাছাই করুন','Previous initiative':'আগের উদ্যোগ','Next initiative':'পরের উদ্যোগ',
      'Initiative spotlight':'একনজরে আমাদের উদ্যোগ','Read about this initiative':'উদ্যোগটি সম্পর্কে জানুন',
      'Every contribution starts with a conversation.':'প্রতিটি অবদানের শুরু হোক আলোচনায়।',
      'A few things you might want to know.':'আপনার কিছু প্রশ্নের উত্তর।',
      'How can I get involved?':'আমি কীভাবে যুক্ত হতে পারি?',
      'Start with your interests and the time or skills you can offer. Explore the volunteer and partnership options, then prepare an introduction on our contact page.':'আপনার আগ্রহ, সময় ও দক্ষতা দিয়েই শুরু করুন। স্বেচ্ছাসেবী কাজ ও অংশীদারত্বের সুযোগ সম্পর্কে জানুন, তারপর যোগাযোগের পাতায় একটি পরিচিতি বার্তা তৈরি করুন।',
      'Can organisations partner with MATES?':'প্রতিষ্ঠান কি মেটসের অংশীদার হতে পারে?',
      'Yes. We welcome conversations with educational institutions, community groups, businesses and professionals who share our purpose. Specific partnerships are agreed individually.':'হ্যাঁ। আমাদের উদ্দেশ্যের সঙ্গে একমত শিক্ষাপ্রতিষ্ঠান, সামাজিক সংগঠন, ব্যবসাপ্রতিষ্ঠান ও পেশাজীবীদের সঙ্গে আলোচনা করতে আমরা আগ্রহী। প্রতিটি অংশীদারত্ব আলাদাভাবে নির্ধারণ করা হবে।',
      'Are applications and donations open?':'আবেদন ও অনুদান দেওয়া কি চালু হয়েছে?',
      'Program applications and online donations are not open yet. Confirmed activities, eligibility and verified donation details will be published on this website.':'কর্মসূচিতে আবেদন ও অনলাইনে অনুদান দেওয়া এখনো চালু হয়নি। কার্যক্রম, যোগ্যতার শর্ত ও যাচাইকৃত অনুদানের তথ্য নিশ্চিত হলে এই ওয়েবসাইটে প্রকাশ করা হবে।',
      'Can I use this website in Bengali?':'ওয়েবসাইটটি কি বাংলায় ব্যবহার করা যাবে?',
      'Yes. Choose English or বাংলা in the header. The whole website is available in both languages, and your browser remembers your choice.':'হ্যাঁ। পাতার ওপরের অংশ থেকে English বা বাংলা বেছে নিন। পুরো ওয়েবসাইট দুই ভাষাতেই রয়েছে এবং আপনার ব্রাউজার ভাষার পছন্দ মনে রাখে।',
      'COMMON QUESTIONS':'সাধারণ জিজ্ঞাসা',
      'Building confidence through learning.':'শিক্ষার মাধ্যমে আত্মবিশ্বাস গড়ে তুলি।',
      'Making room for educational ambition.':'পড়াশোনার স্বপ্ন পূরণের সুযোগ তৈরি করি।',
      'Bringing people closer to support.':'সহায়তার বন্ধনে মানুষকে যুক্ত করি।',
      'Encouraging care for one another.':'একে অন্যের যত্নে এগিয়ে আসি।',
      'Standing beside people in hardship.':'সংকটে মানুষের পাশে দাঁড়াই।',
      'Preparing for the next opportunity.':'আগামীর সুযোগের জন্য প্রস্তুত হই।'
    }
    translations.update(new_text)
    titles=list(new_text)[-6:]
    spotlight='<section class="spotlight-section" data-initiative="education"><div class="wrap"><div class="spotlight-top"><span class="eyebrow">EXPLORE WHAT MATTERS TO YOU</span><div class="spotlight-controls"><span id="spotlight-position">01 / 06</span><button type="button" id="spotlight-prev" aria-label="Previous initiative">←</button><button type="button" id="spotlight-next" aria-label="Next initiative">→</button></div></div><div class="spotlight" aria-label="Initiative spotlight">'
    for i,p in enumerate(programs):
        slug,num,name,tag,desc,short,ic,focus,txt=p
        revised=next((new for old,new,bn in edits if old==desc),desc)
        spotlight+=f'<article class="spotlight-slide" data-slide="{i}" data-initiative="{slug}"'+(' hidden' if i else '')+f'><div class="spotlight-symbol">{icon(ic)}</div><div><h2>{titles[i]}</h2><p>{revised}</p></div><a class="button" href="{slug}.html">Read about this initiative <span>↗</span></a></article>'
    spotlight+='</div></div></section>'
    filters='<div class="initiative-filters" role="group" aria-label="Filter initiatives"><button type="button" data-filter="all" aria-pressed="true">All initiatives</button><button type="button" data-filter="learning" aria-pressed="false">Learning &amp; opportunity</button><button type="button" data-filter="care" aria-pressed="false">Care &amp; support</button></div>'
    faq='<section class="section faq-section"><div class="wrap faq-grid"><div><span class="eyebrow">COMMON QUESTIONS</span><h2>A few things you might want to know.</h2><p>Every contribution starts with a conversation.</p></div><div class="faq-list">'
    for q,a in [('How can I get involved?','Start with your interests and the time or skills you can offer. Explore the volunteer and partnership options, then prepare an introduction on our contact page.'),('Can organisations partner with MATES?','Yes. We welcome conversations with educational institutions, community groups, businesses and professionals who share our purpose. Specific partnerships are agreed individually.'),('Are applications and donations open?','Program applications and online donations are not open yet. Confirmed activities, eligibility and verified donation details will be published on this website.'),('Can I use this website in Bengali?','Yes. Choose English or বাংলা in the header. The whole website is available in both languages, and your browser remembers your choice.')]:
        faq+='<details><summary>'+q+'</summary><p>'+a+'</p></details>'
    faq+='</div></div></section>'
    translations.update({
        'COMMUNITY EVENTS':'সামাজিক কার্যক্রম',
        'Care in action.':'সহমর্মিতা যখন কাজে রূপ নেয়।',
        'Completed':'সম্পন্ন',
        'FOOD SUPPORT · 2026':'খাদ্য সহায়তা · ২০২৬',
        'Sharing Happiness of Ramadan & Eid':'রমজান ও ঈদের আনন্দ ভাগ করে নেওয়া',
        'In 2026, MATES Initiative provided food support to families in need during Ramadan and Eid.':'২০২৬ সালে রমজান ও ঈদ উপলক্ষে প্রয়োজনের সময়ে পরিবারগুলোর পাশে দাঁড়াতে খাদ্য সহায়তা দেয় মেটস ইনিশিয়েটিভ।',
        'The event brought the spirit of sharing into practical action, helping families celebrate the season with dignity and a sense of belonging.':'এই আয়োজনের মাধ্যমে পারস্পরিক সহযোগিতা ও ভাগ করে নেওয়ার চেতনা বাস্তবে রূপ পায়। লক্ষ্য ছিল পরিবারগুলোর পাশে থেকে মর্যাদা ও আনন্দের সঙ্গে উৎসব উদ্‌যাপনে সহায়তা করা।',
        'Food support':'খাদ্য সহায়তা',
        'Ramadan & Eid':'রমজান ও ঈদ',
        'Community care':'সমাজের পাশে'
    })
    event='<section class="section community-events" id="events"><div class="wrap"><span class="eyebrow">COMMUNITY EVENTS</span><h2>Care in action.</h2><article class="community-event"><div class="event-stamp"><span class="event-year">2026</span><span class="event-status">Completed</span><div class="event-symbol">'+icon('people')+'</div></div><div class="event-story"><p class="event-kicker">FOOD SUPPORT · 2026</p><h3>Sharing Happiness of Ramadan &amp; Eid</h3><p>In 2026, MATES Initiative provided food support to families in need during Ramadan and Eid.</p><p>The event brought the spirit of sharing into practical action, helping families celebrate the season with dignity and a sense of belonging.</p><div class="event-tags"><span>Food support</span><span>Ramadan &amp; Eid</span><span>Community care</span></div></div></article></div></section>'
    for f in root.glob('*.html'):
        source=f.read_text()
        for old,new,bn in edits:source=source.replace(old,new)
        source=source.replace('<header>','<div class="reading-progress" aria-hidden="true"><span></span></div><header>')
        source=source.replace('<body id="top">','<body id="top"><div class="site-watermark" aria-hidden="true"><img src="assets/mates-foundation-logo.png" alt="" width="1672" height="941" decoding="async"></div>')
        source=source.replace('href="assets/style.css"','href="assets/style.css?v=6"').replace('src="assets/site.js"','src="assets/site.js?v=4"')
        if f.name in ('index.html','initiatives.html'):
            source=source.replace('<div class="program-grid">',filters+'<div class="program-grid">',1)
        if f.name=='index.html':
            source=source.replace('<section class="purpose-strip">',spotlight+'<section class="purpose-strip">',1)
            source=source.replace('</main>',faq+'</main>')
        if f.name=='community.html':
            marker='<section class="section pale"><div class="wrap"><span class="eyebrow">EXPLORE MORE</span>'
            assert marker in source, 'Community event insertion point missing'
            source=source.replace(marker,event+marker,1)
        for p in programs:
            category='learning' if p[0] in ('education','scholarships','skills') else 'care'
            source=source.replace(f'<a class="program-card" href="{p[0]}.html">',f'<a class="program-card" data-category="{category}" data-initiative="{p[0]}" href="{p[0]}.html">')
        if f.stem in {p[0] for p in programs}:
            source=source.replace('<body id="top">',f'<body id="top" data-initiative="{f.stem}">',1)
        source=source.replace('↗','<svg class="arrow-svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 18 18 6M6 6h12v12"/></svg>')
        f.write_text(source)
    for key,value in list(translations.items()):
        if key.endswith('↗'):translations[key[:-1].rstrip()]=value.removesuffix('↗').rstrip()
    (root/'translations-bn.json').write_text(json.dumps(translations,ensure_ascii=False,indent=2)+'\n')
