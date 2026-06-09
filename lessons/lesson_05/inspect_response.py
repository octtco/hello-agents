from openai import OpenAI


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
                "a": {"type": "number"},
                "b": {"type": "number"}
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
        "content": "所有加法计算都必须调用 add 工具，不要自己心算。"
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

print("type(response):")
print(type(response))
print()

print("response:")
print(response)
print()

print("type(response.output):")
print(type(response.output))
print()

print("response.output:")
print(response.output)
print()

print("response.output_text:")
print(response.output_text)
print()

first_output = response.output[0]

print("type(response.output[0]):")
print(type(first_output))
print()

print("response.output[0]:")
print(first_output)
print()

print("response.output[0].type:")
print(first_output.type)
print()

print("response.output[0].name:")
print(first_output.name)
print()

print("response.output[0].arguments:")
print(first_output.arguments)
print()

print("response.output[0].call_id:")
print(first_output.call_id)
