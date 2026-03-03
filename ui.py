import chainlit as cl
from llm import generate_response


@cl.on_chat_start
async def main():
    await cl.Message("""
        Hello 👋 Welcome to Saksham Support.
        Is this about:                     
        1️⃣ Your phone
        2️⃣ Something that may be a scam?
        """).send()

    cl.user_session.set("history", [])


@cl.on_message
async def on_message(msg: cl.Message):
    # print("User:", msg.content)
    response = cl.Message(content="")

    # if "phone" in msg.content.lower():
    # print(cl.user_session.get("history"))

    async for chunk in generate_response(
        msg.content, history=cl.user_session.get("history")
    ):
        if chunk:
            # print("AI:", chunk)
            await response.stream_token(chunk)

    await response.send()

    cl.user_session.get("history").append(
        ({"user": msg.content, "ai": response.content})
    )

    # else:
    #     print("coming soon")
    #     await cl.Message(content=f"Coming Soon !!").send()

    # else:
    #     print(2)
    #     phone_option = await cl.Message(
    #         content="Mention a phone model you want to know about.[ios or pixel]",
    #     ).send()

    #     if phone_option == "ios":
    #         query = "What should I do if my iPhone is overheating?"

    #     else:
    #         ...
