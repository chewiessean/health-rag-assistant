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

collected_data = []

for topic, url in urls.items():
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"WARNING: could not fetch page for {topic} (status: {response.status_code})")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    content_div = soup.find("div", {"id": "ency_summary"})

    if content_div:
        text = content_div.get_text(separator=" ", strip=True)
        collected_data.append({"topic": topic, "url": url, "text": text})
        print(f"+ {topic}: collected {len(text)} characters")
    else:
        print(f"- {topic}: content block not found, check the HTML structure")

    time.sleep(1)

with open("health_data.json", "w", encoding="utf-8") as f:
    json.dump(collected_data, f, ensure_ascii=False, indent=2)

print(f"\nTotal {len(collected_data)} topics saved.")