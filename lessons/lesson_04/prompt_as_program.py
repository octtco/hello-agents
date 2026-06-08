import os
import json
from openai import OpenAI


def call_llm(message):

    api_key = "Managed"
    base_url = "http://127.0.0.1:15721/v1"
    model = "gpt-5.5"

    client = OpenAI(
        api_key = api_key,
        base_url = base_url
    )

    try:
        response = client.responses.create(
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
                            "answer": {
                                "type": "string"
                            },
                            "confidence": {
                                "type": "number"
                            }
                        },
                        "required": ["answer", "confidence"],
                        "additionalProperties": False
                    }
                }
            }
        )

        reply = response.output_text
        return reply

    except Exception as error:
        return "模型错误：" + str(error)
    

system_prompt = """
你是一个严格的 JSON 输出助手。
你只能输出 JSON。
JSON 必须包含：
- answer：字符串，回答用户问题
- confidence：数字，表示你对回答的信心，范围 0 到 1
不要输出 JSON 以外的文字。
"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "API 是什么？"},
]

reply = call_llm(message=messages)
print("reply: " + reply)

data = json.loads(reply)

print("answer: "+ data["answer"])
print(data["confidence"])