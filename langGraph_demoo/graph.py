from langgraph.graph import StateGraph, END, START
from typing import TypedDict
from dotenv import load_dotenv
import os
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
email = """"
Dear winner,
you have been selected as the lucky winner of our international lottery. to claim your prize,
Don't miss this opportunity!
"""


messages = [
        (
            "system",
            "You are a spam classifier. "
            "Return ONLY 'true' or 'false'. "
            "true = spam, false = not spam."
        ),
        ("human", email),
    ]

ai_msg = model.invoke(messages)
result = ai_msg.content[0]["text"]
    

result



class State(TypedDict):
    email: str
    is_spam: bool
    translated_email: str





def classify_email_mode_1(state: State):
    email = state["email"]   # لا تمسحه

    messages = [
        (
            "system",
            "You are a spam classifier. "
            "Return ONLY 'true' or 'false'. "
            "true = spam, false = not spam."
        ),
        ("human", email),
    ]

    ai_msg = model.invoke(messages)

    # الحل الصحيح
    result = ai_msg.text.strip().lower()

    return {
        "is_spam": result == "true"
    }



def routeril_node_2(state: State):
    
    if state["is_spam"] == True:
        return END
    
    else:
        return "summrizer"


def translate_node_3(state: State):
    email = state["email"]

    messages = [
        (
            "system",
            "You are a translator "
            "translate this email to arbic. "
            
        ),
        ("human", email),
    ]

    ai_msg = model.invoke(messages)
    translated_email = ai_msg.content[0]["text"]

   

    return {
        "translated_email": translated_email
    }



graph = StateGraph(State)

graph.add_node("classifier",classify_email_mode_1)
graph.add_edge(START, "classifier")

graph.add_conditional_edges(
    "classifier",
    routeril_node_2,
    [END, "summrizer"]
)

graph.add_node("summrizer",translate_node_3 )
graph.add_edge("summrizer", END)


agent = graph.compile()



from IPython.display import Image, display
display(Image(agent.get_graph(xray=True).draw_mermaid_png()))




result = agent.invoke({
    "email": "hi iam mohamed i am from egypt"
})

type(result)


result