from langchain_community.document_loaders import FireCrawlLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import asyncio
from vector_db import to_db

URL = "https://support.google.com/pixelphone/"


async def crawl():
    loader = FireCrawlLoader(url=URL, mode="crawl", params={"limit": 5})

    # ✅ await async loader
    docs = await loader.aload()

    if not docs:
        print("No documents loaded")
        # return []

    splitter = RecursiveCharacterTextSplitter(chunk_size=1600, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    # print(chunks)
    return chunks


if __name__ == "__main__":
    chunks = asyncio.run(crawl())
    to_db(chunks)
