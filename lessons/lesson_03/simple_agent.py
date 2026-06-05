import os
from openai import OpenAI

def call_llm(messages):

    api_key = "PROXY_MANAGED"
    base_url = "http://127.0.0.1:15721/v1"
    model = "gpt-5.5"

    if api_key is None:
        return "缺少apikey"
    elif base_url is None:
        return "缺少baseurl"
    elif model is None:
        return "缺少model"
    
    client = OpenAI(
        api_key = api_key,
        base_url = base_url
    )

    try:
        response = client.responses.create(
            model = model,
            input = messages
        )
        return response.output_text
    except Exception as error:
        return "模型错误：" + str(error)
    

class SimleAgent:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": "你是一个耐心的 Python 老师。"}    
        ]
    def chat(self, user_message):
        self.messages.append({"role": "user", "content": user_message})
        reply = call_llm(self.messages)
        self.messages.append({"role": "assistant", "content": reply})

        return reply

agent  = SimleAgent()

while True:
    user_message = input("你：")
    if user_message == "退出":
        print("Agent：下次见")
        break

    reply = agent.chat(user_message=user_message)

    print("Agent：" + str(reply))
    