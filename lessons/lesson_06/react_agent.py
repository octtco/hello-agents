import json
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
        api_key=api_key,
        base_url=base_url
    )

    reply = client.responses.create(
        model=model,
        input=messages,
        text={            
            "format": {
                "type": "json_schema",
                "name": "answer_result",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties":{
                        "thought":{
                            "type": "string"
                        },
                        "action":{
                            "type": "string"
                        },
                        "arguments":{
                            "type": "object",
                            "properties": {
                                "a": {"type": "number"},
                                "b": {"type": "number"}
                            },
                            "required":["a", "b"],
                            "additionalProperties": False,
                        },
                        "finish":{
                            "type": "string"
                        }
                    },
                    "required": ["thought", "action", "arguments", "finish"],
                    "additionalProperties": False
                }
            }
        }
    )
    return reply.output_text


class simpleAgent:
    def __init__(self):
        self.messages = [{
            "role": "system", "content": """
            你是一个智能助手。可以判断需要直接回答还是调用工具。
            所有的加法都必须走工具调用，
            thought是你的思考过程，
            action是工具名,
            arguments是工具参数,
            finish是最终回复，
            如果用户问题需要加法，第一轮 action 写 add，finish 写空字符串。
            如果 finish 是空字符串，action 必须是 add。
            如果 action 是空字符串，finish 必须有最终回答。
            当你看到 Observation 后，action 写空字符串，arguments 的 a 和 b 写 0，finish 写最终回答。
            """
        }]
        self.tools = {
            "add": add
        }

    def chat(self, user_message):
        self.messages.append({"role": "user", "content": user_message})
        print("=== User ===")
        print(user_message)
        reply = call_llm(self.messages)
        print("=== LLM Reply ===")
        print(reply)
        response = json.loads(reply)
        self.messages.append({"role": "assistant", "content": reply})
        for _ in range(5):
            if response["finish"] != "":
                break
            if response["action"] not in self.tools:
                return "模型请求了未知工具：" + response["action"]

            tool_name = response["action"]
            arguments = response["arguments"]
            print("=== Action ===")
            print(tool_name)
            print(arguments)
            tool = self.tools[tool_name]
            result = tool(**arguments)
            print("=== Observation ===")
            print(result)
            self.messages.append({
                "role": "user",
                "content": "Observation: " + str(result)
            })
            print("=== Messages ===")
            print(json.dumps(self.messages, ensure_ascii=False, indent=2))
            reply = call_llm(self.messages)
            response = json.loads(reply)
            print("=== LLM Reply ===")
            print(reply)
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
    print("Agent answer：" + str(data["finish"]))
        