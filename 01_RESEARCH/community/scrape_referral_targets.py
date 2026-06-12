#!/usr/bin/env python3
import re, json
from playwright.sync_api import sync_playwright

targets = [
    ('wikipedia_asuncion', 'https://en.wikipedia.org/wiki/Asunci%C3%B3n'),
    ('wikipedia_expat', 'https://en.wikipedia.org/wiki/Expatriate'),
    ('coworking_anahi', 'https://www.coworkingpy.com'),
    ('asuncion_center', 'https://www.asuncioncenter.com'),
    ('embajada_usa', 'https://py.usembassy.gov/'),
    ('embajada_uk', 'https://www.gov.uk/world/paraguay'),
    ('internations_about', 'https://www.internations.com/expats-in-paraguay/'),
    ('move_paraguay_about', 'https://moveparaguay.com'),
    ('gringoflix', 'https://www.gringoflix.com'),
]

results = {}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-blink-features=Automation'])
    ctx = browser.new_context(viewport={'width': 1280, 'height': 800}, user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    page = ctx.new_page()
    page.set_default_timeout(20000)

    for name, url in targets:
        try:
            page.goto(url, timeout=20000)
            page.wait_for_load_state('domcontentloaded', timeout=10000)
            page.wait_for_timeout(2500)
            html = page.content()

            results[name] = {'url': url, 'size': len(html)}

            title_m = re.search(r'<title[^>]*>([^<]+)</title>', html)
            if title_m:
                results[name]['title'] = title_m.group(1).strip()

            h1 = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
            if h1:
                results[name]['h1'] = h1.group(1).strip()

            desc_m = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]+)"', html)
            if desc_m:
                results[name]['description'] = desc_m.group(1).strip()

            paragraphs = re.findall(r'<p[^>]*>([^<]{80,})</p>', html)
            clean = [re.sub(r'<[^>]+>', '', p).strip() for p in paragraphs]
            relevant = [c for c in clean if any(kw in c.lower() for kw in ['expat', 'american', 'international', 'school', 'coworking', 'foreign', 'retiree', 'digital', 'immigrant', 'community', 'asuncion', 'paraguay']) and len(c) > 60]
            if relevant:
                results[name]['relevant_paragraphs'] = relevant[:8]

            phone_m = re.findall(r'[\+]?595\s*[\d\s\-]{8,}', html)
            if phone_m:
                results[name]['phones'] = list(set(phone_m))[:5]

            email_m = re.findall(r'[\w.-]+@[\w.-]+\.\w+', html)
            if email_m:
                results[name]['emails'] = list(set(email_m))[:5]

            links = re.findall(r'<a[^>]*href="(https?://[^"]+)"[^>]*>\s*([^<]{3,60})\s*</a>', html)
            social = [(l[1].strip(), l[0]) for l in links if any(kw in l[0].lower() for kw in ['facebook', 'instagram', 'youtube', 'twitter', 'linkedin'])][:10]
            if social:
                results[name]['social'] = social

            address_matches = re.findall(r'(?:Av\.\s+[^<,\n]{5,60},?\s*(?:Asunción|Luque|Encarnación|San Lorenzo)[^<\n]{0,30}|address[^<]{0,5}:?\s*[^<\n]{10,80})', html, re.I)
            if address_matches:
                results[name]['addresses'] = [re.sub(r'<[^>]+>', '', a).strip() for a in address_matches][:5]

            headings = re.findall(r'<h[1-4][^>]*>([^<]+)</h[1-4]>', html)
            results[name]['headings'] = [h.strip() for h in headings if len(h.strip()) > 5][:10]

            print(f'\n=== {name} ({len(html)} bytes) ===')
            print('TITLE:', results[name].get('title', 'N/A')[:80])
            print('H1:', results[name].get('h1', 'N/A')[:80])
            print('HEADINGS:', results[name].get('headings', [])[:6])
            if 'relevant_paragraphs' in results[name]:
                for r in results[name]['relevant_paragraphs'][:3]:
                    print('P:', r[:150])
            print('PHONES:', results[name].get('phones', []))
            print('EMAILS:', results[name].get('emails', []))
            print('SOCIAL:', results[name].get('social', [])[:5])

        except Exception as e:
            results[name] = {'url': url, 'status': 'error', 'error': str(e)[:100]}
            print(f'{name}: ERROR {e}')

    browser.close()

out_path = '/home/ai-whisperers/dentist/01_RESEARCH/community/referral-targets-research.json'
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print(f'\nSaved: {out_path}')