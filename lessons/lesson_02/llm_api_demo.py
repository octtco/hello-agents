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
        base_url = base_url,
    )

    try:
        response = client.responses.create(
            model = model,
            input = messages,
        )

        return response.output_text

    except Exception as error:
        return "调用模型失败：" + str(error)


messages = [
    {"role": "system", "content": "你是一个 Python 老师。"},
    {"role": "user", "content": "API 是什么？"},
]

reply = call_llm(messages)
print(reply)
