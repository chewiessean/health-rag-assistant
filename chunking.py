import json

def chunk_text(text, max_words=100, overlap_words=20):
    words = text.split()

    if len(words) <= max_words:
        return [text]

    chunks = []
    start = 0
    while start < len(words):
        end = start + max_words
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += max_words - overlap_words

    return chunks

with open("data/health_data.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

all_chunks = []

for item in raw_data:
    topic_chunks = chunk_text(item["text"], max_words=100, overlap_words=20)

    for i, chunk in enumerate(topic_chunks):
        all_chunks.append({
            "source": item["source"],
            "url": item["url"],
            "chunk_id": f"{item['source']}_{i}",
            "text": chunk
        })

print(f"Total {len(raw_data)} topics split into {len(all_chunks)} chunks.\n")

for chunk in all_chunks:
    print(f"[{chunk['chunk_id']}] ({len(chunk['text'].split())} words)")
    print(f"  {chunk['text']}\n")

with open("data/health_data.json", "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, ensure_ascii=False, indent=2)