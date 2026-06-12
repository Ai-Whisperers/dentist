#!/usr/bin/env python3
import re
from playwright.sync_api import sync_playwright

scrape_targets = [
    ('wikipedia_py', 'https://en.wikipedia.org/wiki/Paraguay'),
    ('expat_forum', 'https://www.expat.com/forum/viewforum.php?f=51'),
    ('move_paraguay', 'https://moveparaguay.com/expat-life-in-paraguay/'),
    ('us_embassy', 'https://py.usembassy.gov/'),
    ('uk_embassy', 'https://www.gov.uk/world/paraguay'),
    ('internations_asuncion', 'https://www.internations.com/expats-in-paraguay/moving-to-paraguay'),
    ('numbeo_cost', 'https://www.numbeo.com/cost-of-living/country_result.jsp?country=Paraguay'),
    ('r_paraguay', 'https://www.reddit.com/r/Paraguay/'),
    ('r_expats', 'https://www.reddit.com/r/expats/search/?q=Paraguay+immigrant+foreigner'),
    ('r_digital_nomad', 'https://www.reddit.com/r/digitalnomad/search/?q=Paraguay'),
]

results = {}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
    ctx = browser.new_context(viewport={'width': 1280, 'height': 800}, user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    page = ctx.new_page()
    page.set_default_timeout(15000)

    for name, url in scrape_targets:
        try:
            page.goto(url, timeout=15000)
            page.wait_for_load_state('domcontentloaded', timeout=8000)
            page.wait_for_timeout(1500)
            html = page.content()

            results[name] = {'url': url, 'status': 'ok', 'size': len(html)}

            headings = re.findall(r'<h[1-3][^>]*>\s*([^<]{10,})\s*</h[1-3]>', html)
            if headings:
                results[name]['headings'] = headings[:12]

            paragraphs = re.findall(r'<p[^>]*>([^<]{60,500})</p>', html)
            expat_para = [re.sub(r'<[^>]+>', '', p).strip() for p in paragraphs if any(kw in p.lower() for kw in ['expat', 'foreign', 'american', 'european', 'immigrant', 'retiree', 'nomad', 'remote', 'asuncion', 'migrate', 'relocat']) and len(re.sub(r'<[^>]+>', '', p)) > 80]
            if expat_para:
                results[name]['expat_content'] = expat_para[:5]

            lists = re.findall(r'<li[^>]*>([^<]{15,150})</li>', html)
            if lists:
                results[name]['list_items'] = lists[:15]

            links = re.findall(r'<a[^>]*href="(https?://[^"]+)"[^>]*>([^<]{5,60})</a>', html)
            useful_links = [(l[1].strip(), l[0]) for l in links if any(kw in l[1].lower() for kw in ['expat', 'international', 'school', 'cowork', 'embassy', 'visa', 'immigr', 'relocat']) or any(kw in l[0].lower() for kw in ['expat', 'international', 'school', 'cowork', 'embassy', 'visa'])]
            if useful_links:
                results[name]['useful_links'] = useful_links[:10]

            tables = re.findall(r'<table[^>]*>(.*?)</table>', html, re.DOTALL)
            table_data = []
            for t in tables[:2]:
                rows = re.findall(r'<tr[^>]*>(.*?)</tr>', t, re.DOTALL)
                row_texts = []
                for row in rows[:8]:
                    cells = re.findall(r'<t[dh][^>]*>([^<]+)</t[dh]>', row)
                    if cells:
                        row_texts.append([re.sub(r'<[^>]+>', '', c).strip() for c in cells])
                if row_texts:
                    table_data.append(row_texts[:5])
            if table_data:
                results[name]['tables'] = table_data

            print(f'\n=== {name} ({len(html)} bytes) ===')
            if 'headings' in results[name]:
                print('H:', results[name]['headings'][:6])
            if 'expat_content' in results[name]:
                for c in results[name]['expat_content'][:3]:
                    print('P:', c[:150])
            if 'useful_links' in results[name]:
                print('L:', results[name]['useful_links'][:5])
            if 'list_items' in results[name]:
                print('LI:', results[name]['list_items'][:8])
            if 'tables' in results[name]:
                for i, t in enumerate(results[name]['tables'][:2]):
                    print(f'T{i}:', t[:3])

        except Exception as e:
            results[name] = {'url': url, 'status': 'error', 'error': str(e)[:100]}
            print(f'{name}: ERROR {e}')

    browser.close()

import json
out_path = '/home/ai-whisperers/dentist/01_RESEARCH/community/expat-scraped-data.json'
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print(f'\nSaved: {out_path}')