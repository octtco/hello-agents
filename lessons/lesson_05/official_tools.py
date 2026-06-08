import json

from openai import OpenAI


def add(a, b):
    return a + b


def call_tool(name, arguments):
    tools = {
        "add": add
    }

    tool = tools[name]
    return tool(**arguments)


client = OpenAI(
    api_key="PROXY_MANAGED",
    base_url="http://127.0.0.1:15721/v1",
)

model = "gpt-5.5"

tools = [
    {
        "type": "function",
        "name": "add",
        "description": "计算两个数字相加的结果。",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number",
                    "description": "第一个数字。"
                },
                "b": {
                    "type": "number",
                    "description": "第二个数字。"
                }
            },
            "required": ["a", "b"],
            "additionalProperties": False
        },
        "strict": True
    }
]

input_list = [
    {
        "role": "system",
        "content": "你是一个智能助手。所有加法计算都必须调用 add 工具，不要自己心算。"
    },
    {
        "role": "user",
        "content": "23 + 19 等于多少？"
    }
]

response = client.responses.create(
    model=model,
    input=input_list,
    tools=tools,
)

input_list += response.output

for item in response.output:
    if item.type != "function_call":
        continue

    arguments = json.loads(item.arguments)
    result = call_tool(item.name, arguments)

    input_list.append({
        "type": "function_call_output",
        "call_id": item.call_id,
        "output": str(result),
    })

final_response = client.responses.create(
    model=model,
    input=input_list,
    tools=tools,
)

print(final_response.output_text)
