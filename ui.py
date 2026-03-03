import chainlit as cl
from llm import generate_response
import uuid

id = uuid.uuid4()


@cl.on_chat_start
async def main():
    await cl.Message("You want to know about your phone or scam check").send()


@cl.on_message
async def on_message(msg: cl.Message):
    # print("User:", msg.content)

    # if "phone" in msg.content.lower():
    print(id)
    response = generate_response(msg.content, id)
    await cl.Message(content=response.content).send()

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
