import asyncio
import httpx
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from vector_db import to_db


headers = {"User-Agent": "Mozilla/5.0"}


async def fetch(client, url):
    try:
        resp = await client.get(url, headers=headers)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        print(f"Error fetching {url}: {e}")

    soup = BeautifulSoup(resp.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)

    return Document(page_content=text, metadata={"source": url, "phone": "pixel"})
    # return Document(page_content=text, metadata={"source": url, "phone": "ios 18"})


async def crawl():
    # with open("./data/pixel_data.json", "rb") as f:
    #     # with open("./data/ios_18_data.json", "rb") as f:
    #     urls = orjson.loads(f.read())

    # urls = urls[20:60]
    # # urls = urls[:10]
    # urls = GOOGLE_URLS
    urls = []

    splitter = RecursiveCharacterTextSplitter(chunk_size=1800, chunk_overlap=200)

    async with httpx.AsyncClient(timeout=20.0, follow_redirects=True) as client:
        tasks = [fetch(client, url) for url in urls]
        docs = await asyncio.gather(*tasks)

    chunks = splitter.split_documents(docs)

    to_db(chunks)


if __name__ == "__main__":
    print("Crawling and processing documents...")

    # GOOGLE_URLS = [
    #     "https://support.google.com/pixelphone/answer/14140287",
    #     "https://support.google.com/pixelphone/answer/12967594",
    #     "https://support.google.com/pixelphone/answer/7158570",
    #     "https://support.google.com/pixelphone/answer/15199831",
    #     "https://support.google.com/pixelphone/answer/14116441",
    #     "https://support.google.com/pixelphone/answer/7535206",
    #     "https://support.google.com/pixelphone/answer/6111329",
    #     "https://support.google.com/pixelphone/answer/7444033",
    #     "https://support.google.com/pixelphone/answer/2819525",
    #     "https://support.google.com/pixelphone/answer/2818748",
    #     "https://support.google.com/pixelphone/answer/7680439",
    #     "https://support.google.com/pixelphone/answer/14782427",
    #     "https://support.google.com/pixelphone/answer/6183600",
    #     "https://support.google.com/pixelphone/answer/6187458",
    #     "https://support.google.com/pixelphone/answer/6006564",
    #     "https://support.google.com/pixelphone/answer/6122841",
    #     "https://support.google.com/pixelphone/answer/12913009",
    #     "https://support.google.com/pixelphone/answer/9316333",
    #     "https://support.google.com/pixelphone/answer/7283669",
    #     "https://support.google.com/pixelphone/answer/2844832",
    #     "https://support.google.com/pixelphone/answer/2781850",
    #     "https://support.google.com/pixelphone/answer/15182154",
    #     "https://support.google.com/pixelphone/answer/13202895",
    #     "https://support.google.com/pixelphone/answer/7055029",
    #     "https://support.google.com/pixelphone/answer/9118387",
    #     "https://support.google.com/pixelphone/answer/2819524",
    #     "https://support.google.com/pixelphone/answer/4596836",
    #     "https://support.google.com/pixelphone/answer/9218411",
    #     "https://support.google.com/pixelphone/answer/6187455",
    #     "https://support.google.com/pixelphone/answer/6090599",
    #     "https://support.google.com/pixelphone/answer/13675043",
    #     "https://support.google.com/pixelphone/answer/7106961",
    # ]

    asyncio.run(crawl())
