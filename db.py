from config import DB_Session
from db_model import Chathistory

db = DB_Session()


def insert_into_db(user_msg, bot_msg, id):
    chat = Chathistory(user_chat=user_msg, chatbot=bot_msg, user=str(id))
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat


def find_recent_chats(id):
    return (
        db.query(Chathistory.user_chat)
        .filter(Chathistory.user == str(id))
        .order_by(Chathistory.id.desc())
        .limit(5)
        .all()
    )
