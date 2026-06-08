import json
import os
from openai import OpenAI

def call_llm(message):
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

    reply = client.responses.create(
        model = model,
        input = message,
        text = {
             "format":{
                    "type": "json_schema",
                    "name": "answer_result",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties":{
                            "type": {
                                "type": "string"
                            },
                            "answer": {
                                "type": "string"
                            },
                            "tool_name": {
                                "type": "string"
                            },
                            "arguments": {
                                "type": "object",
                                "properties": {
                                    "a": {
                                        "type": "number"
                                    },
                                    "b": {
                                        "type": "number"
                                    }
                                },
                                "required": ["a", "b"],
                                "additionalProperties": False
                            },
                            "confidence": {
                                "type": "number"
                            }
                        },
                        "required": ["type", "answer", "tool_name", "arguments", "confidence"],
                        "additionalProperties": False
                    }
                }
        }
    )
    return reply.output_text

class simpleAgent:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": """
             你是一个智能助手。可以判断需要直接回答还是调用工具。
             直接回答就type写answer，回复写在answer里。
             使用工具就type写tool_call，工具名写在tool_name，
             所有的加法都必须走工具调用，
             可调用的工具是add，是用来做加法的，需要传两个数字参数，参数写在arguments。
             所有字段都必须填写。
             如果 type 是 answer，tool_name 写空字符串，arguments 里的 a 和 b 都写 0。
             如果 type 是 tool_call，answer 写空字符串。
             """}    
        ]
        self.tools = {
            "add": add
        }

    def chat(self, user_message):
        self.messages.append({"role": "user", "content": user_message})
        reply = call_llm(self.messages)
        self.messages.append({"role": "assistant", "content": reply})
        return reply
    


def add(a,b):
    return a + b

agent = simpleAgent()

while True:
    user_message = input("你：")
    if user_message == "退出":
        print("Agent：下次见")
        break

    reply = agent.chat(user_message=user_message)
    data = json.loads(reply)
    
    if data["type"] == "answer":
        print("Agent answer：" + str(data["answer"]))
    elif data["type"] == "tool_call":
        tool_name = data["tool_name"]
        arguments = data["arguments"]
        tool = agent.tools[tool_name]
        result = tool(**arguments)
        print("Agent toolcall：" + str(result))
    else:
        print("Agent：我没看懂模型返回的类型：" + data["type"])
        
