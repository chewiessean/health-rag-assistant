import requests
from bs4 import BeautifulSoup
import time
import json

urls = {
    "diabetes": "https://medlineplus.gov/ency/article/001214.htm",
    "diabetes_type2": "https://medlineplus.gov/ency/article/000313.htm",
    "flu": "https://medlineplus.gov/ency/article/000080.htm",
    "asthma": "https://medlineplus.gov/ency/article/000141.htm",
    "anemia": "https://medlineplus.gov/ency/article/000560.htm",
    "migraine": "https://medlineplus.gov/ency/article/000709.htm",
    "obesity": "https://medlineplus.gov/ency/article/007297.htm",
    "sinusitis": "https://medlineplus.gov/ency/article/000647.htm",
    "arrhythmias": "https://medlineplus.gov/ency/article/001101.htm",
    "epilepsy": "https://medlineplus.gov/ency/article/000694.htm"
}

headers = {"User-Agent": "Mozilla/5.0 (educational student project)"}

wanted_titles = ["Symptoms", "Causes", "Prevention", "Treatment"]

collected_data = []

for topic, url in urls.items():
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"WARNING: could not fetch page for {topic} (status: {response.status_code})")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    summary_div = soup.find("div", {"id": "ency_summary"})
    summary_text = summary_div.get_text(separator=" ", strip=True) if summary_div else ""

    extra_parts = []
    sections = soup.find_all("div", {"class": "section"})

    for section in sections:
        title_tag = section.find("h2")
        if title_tag and title_tag.get_text(strip=True) in wanted_titles:
            body = section.find("div", {"class": "section-body"})
            if body:
                title = title_tag.get_text(strip=True)
                content = body.get_text(separator=" ", strip=True)
                extra_parts.append(f"{title}: {content}")

    full_text = summary_text
    if extra_parts:
        full_text += " " + " ".join(extra_parts)

    if full_text:
        collected_data.append({"source": topic, "url": url, "text": full_text})
        print(f"+ {topic}: collected {len(full_text)} characters ({len(extra_parts)} extra sections found)")
    else:
        print(f"- {topic}: no content found, check the HTML structure")

    time.sleep(1)

with open("data/health_data.json", "w", encoding="utf-8") as f:
    json.dump(collected_data, f, ensure_ascii=False, indent=2)

print(f"\nTotal {len(collected_data)} topics saved.")