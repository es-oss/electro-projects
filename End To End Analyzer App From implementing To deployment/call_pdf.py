
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
) 

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = model.invoke(messages)
ai_msg

import base64
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

pdf_bytes = open("cv_pdf/cv.pdf", "rb").read()
pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
pdf_base64


pdf_bytes = open("cv_pdf/cv.pdf", "rb").read()
pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
mime_type = "application/pdf"

message = HumanMessage(
    content=[
        {"type": "text", "text": "Describe the document in a sentence."},
        {
            "type": "file",
            "base64": pdf_base64,
            "mime_type": mime_type,
        },
    ]
)
response = model.invoke([message])

from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


message = HumanMessage(
    content="Hello AI, suggest a self-learning roadmap for programming and AI for someone starting from scratch. Include the most important courses to take."
)


response = model.invoke([message])


print(response.content)


import time
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "q"]:
        print("Exiting the chat.")
        break
    
    message = HumanMessage(content=user_input)
    response = model.invoke([message])
    
    print("AI:", response.content)
    
    
    time.sleep(1)
