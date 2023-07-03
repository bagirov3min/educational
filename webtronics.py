from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


# Модель данных для пользователя
class User(BaseModel):
    username: str
    password: str


# Модель данных для сообщения
class Message(BaseModel):
    id: int
    text: str
    author: str


# Хранилище пользователей
users = []

# Хранилище сообщений
messages = []


# Роут для регистрации пользователя
@app.post("/register")
def register(user: User):
    # Проверка на уникальность имени пользователя
    for existing_user in users:
        if existing_user.username == user.username:
            raise HTTPException(status_code=400, detail="Username already exists")

    users.append(user)
    return {"message": "User registered successfully"}


# Роут для аутентификации пользователя
@app.post("/login")
def login(user: User):
    # Проверка наличия пользователя в хранилище
    for existing_user in users:
        if (
            existing_user.username == user.username
            and existing_user.password == user.password
        ):
            return {"message": "Login successful"}

    raise HTTPException(status_code=401, detail="Invalid username or password")


# Роут для создания сообщения
@app.post("/messages")
def create_message(message: Message, user: User):
    # Проверка аутентификации пользователя
    authenticated = False
    for existing_user in users:
        if (
            existing_user.username == user.username
            and existing_user.password == user.password
        ):
            authenticated = True
            break

    if not authenticated:
        raise HTTPException(status_code=401, detail="Authentication required")

    message.author = user.username
    messages.append(message)
    return {"message": "Message created successfully"}


# Роут для получения всех сообщений
@app.get("/messages")
def get_all_messages():
    return messages


# Роут для получения сообщения по ID
@app.get("/messages/{message_id}")
def get_message_by_id(message_id: int):
    for message in messages:
        if message.id == message_id:
            return message

    raise HTTPException(status_code=404, detail="Message not found")


# Роут для удаления сообщения по ID
@app.delete("/messages/{message_id}")
def delete_message(message_id: int, user: User):
    # Проверка аутентификации пользователя
    authenticated = False
    for existing_user in users:
        if (
            existing_user.username == user.username
            and existing_user.password == user.password
        ):
            authenticated = True
            break

    if not authenticated:
        raise HTTPException(status_code=401, detail="Authentication required")

    for message in messages:
        if message.id == message_id:
            # Проверка на возможность удаления сообщения другим пользователем
            if message.author == user.username:
                raise HTTPException(
                    status_code=403, detail="You cannot delete your own message"
                )
            messages.remove(message)
            return {"message": "Message deleted successfully"}

    raise HTTPException(status_code=404, detail="Message not found")
