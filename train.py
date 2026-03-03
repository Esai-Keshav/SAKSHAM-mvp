import asyncio
import httpx
import orjson
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from vector_db import to_db


headers = {"User-Agent": "Mozilla/5.0"}


async def fetch(client, url):
    resp = await client.get(url, headers=headers)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)

    # return Document(page_content=text, metadata={"source": url, "phone": "pixel"})
    return Document(page_content=text, metadata={"source": url, "phone": "ios 18"})


async def crawl():
    # with open("./pixel_data.json", "rb") as f:
    with open("./ios_18_data.json", "rb") as f:
        urls = orjson.loads(f.read())

    urls = urls[:6]

    splitter = RecursiveCharacterTextSplitter(chunk_size=1800, chunk_overlap=200)

    async with httpx.AsyncClient(timeout=20.0, follow_redirects=True) as client:
        tasks = [fetch(client, url) for url in urls]
        docs = await asyncio.gather(*tasks)

    chunks = splitter.split_documents(docs)

    to_db(chunks)


if __name__ == "__main__":
    asyncio.run(crawl())
