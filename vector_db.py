from rich import print

from config import vector_store


def to_db(chunks):
    vector_store.add_documents(documents=chunks)

    print(len(chunks))
    # return vector_store.add_documents(documents=docs)

    return True


def find_similar_docs(query: str):
    # similar_docs = vector_store.max_marginal_relevance_search(query, k=3)

    # similar_docs = vector_store.as_retriever(
    #     search_type="mmr",
    #     search_kwargs={
    #         "k": 4,
    #         # "filter": {"user": str(id)}
    #     },
    # )

    similar_docs = vector_store.similarity_search(
        query,
        k=5,
    )
    # similar_docs = vector_store.similarity_search(query, k=5, filter={"phone": phone})
    # print(similar_docs)

    return [(doc.page_content, doc.metadata["source"]) for doc in similar_docs]


if __name__ == "__main__":
    print(find_similar_docs("volume button not working on pixel"))
