from langchain_core.prompts import ChatPromptTemplate
from config import llm
from vector_db import find_similar_docs
from rich import print

short_memory = []


async def generate_response(query: str, history):
    short_memory.append(query)
    similar_docs = find_similar_docs(" ".join(short_memory[-2:]))
    # print(similar_docs)

    with open("./prompt_v2.md", "r") as f:
        prompt_template = f.read()

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                prompt_template
                + """

# REMEMBER:
**Always fetch user devices from this**

# Previous Conversation:
{chat_history}

---

# Retrieved Documents

{retrieved_docs}

---

Your only purpose is to provide **friendly, clear, and accurate help for Google Pixel and iPhone iOS 18 devices**, especially for **senior users who may need patient and simple guidance**.

""",
            ),
            ("human", "{question}"),
        ]
    )
    model = prompt | llm

    print(history)

    async for chunk in model.astream(
        {
            "question": query,
            "retrieved_docs": similar_docs,
            "chat_history": history[-7:],
        }
    ):
        if chunk.content:
            yield chunk.content

    if history:
        yield "\n\n\n Sources : \n- " + "\n - ".join(
            links.metadata["source"] for links in similar_docs
        )
        # yield "\n\n\n Sources : \n- " + "\n - ".join(
        #     links.page_content[:256] for links in similar_docs
        # )

    # return response


if __name__ == "__main__":
    query = "volume button not working on pixel"
    print(generate_response(query).content)


# Do NOT overwhelm with too many bullet points.
