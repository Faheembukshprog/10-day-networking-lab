import json
import sys
import time
import urllib.parse
import urllib.request

ENDPOINTS = [
    ("searxng-json", "https://search.ononoki.org/search?q={q}&format=json"),
    ("ddg-instant", "https://api.duckduckgo.com/?q={q}&format=json&no_html=1&skip_disambig=1"),
    ("wikipedia-opensearch", "https://en.wikipedia.org/w/api.php?action=opensearch&search={q}&limit=5&namespace=0&format=json"),
]


def query_endpoint(name: str, url_template: str, query: str) -> None:
    encoded_q = urllib.parse.quote(query)
    url = url_template.format(q=encoded_q)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "10-Day-Networking-Lab/Day7-Python-Probe",
            "Accept": "application/json",
        },
    )

    start = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            elapsed_ms = (time.perf_counter() - start) * 1000
            body = resp.read().decode("utf-8", errors="replace")
            print(f"\n=== [{name}] HTTP {resp.status} ({elapsed_ms:.1f} ms) ===")
            print("Content-Type:", resp.headers.get("Content-Type"))
            print("Server:", resp.headers.get("Server"))

            data = json.loads(body)
            if name == "searxng-json":
                for item in data.get("results", [])[:5]:
                    print(f" - {item.get('title')} -> {item.get('url')}")
            elif name == "ddg-instant":
                if data.get("AbstractText"):
                    print("Abstract:", data["AbstractText"][:220])
                for item in data.get("RelatedTopics", [])[:5]:
                    if isinstance(item, dict) and item.get("Text"):
                        print(" -", item["Text"][:140])
            elif name == "wikipedia-opensearch":
                titles = data[1] if len(data) > 1 else []
                urls = data[3] if len(data) > 3 else []
                for t, u in zip(titles, urls):
                    print(f" - {t} -> {u}")
    except Exception as exc:
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"\n=== [{name}] Failed in {elapsed_ms:.1f} ms: {exc} ===")


def main() -> None:
    query = " ".join(sys.argv[1:]).strip() or "tcp three way handshake"
    print(f"Query: {query!r}")
    for name, template in ENDPOINTS:
        query_endpoint(name, template, query)


if __name__ == "__main__":
    main()
