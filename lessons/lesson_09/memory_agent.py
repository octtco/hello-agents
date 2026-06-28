import json
from pathlib import Path
from openai import OpenAI

MEMORY_FILE = Path(__file__).parent / "memory.json"

api_key = "PROXY_MANAGED"
base_url = "http://127.0.0.1:15721/v1"    
model = "gpt-5.5"

def call_llm(messages):
    print("=== Call LLM ===")
    print("准备调用模型")
    print("Messages count:", len(messages))

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
            "format":{
                "type": "json_schema",
                "name": "plan_schema",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "keywords": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "reply": {
                            "type": "string",
                        },  
                        "thought": {
                            "type": "string"
                        }
                    },
                    "required":["keywords","reply", "thought"],
                    "additionalProperties": False
                }
            }
        }
    )

    print("=== LLM Raw Reply ===")
    print(reply.output_text)
    return reply.output_text

def load_memories():
    if not MEMORY_FILE.exists():
        return []
    
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
        return memory

def save_memories(memories):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memories, f, ensure_ascii=False, indent=2)

def add_memory(content, memory_type="note"):
    memories = load_memories()
    memory = {"content": content, "type": memory_type}
    memories.append(memory)
    save_memories(memories)
    return memory

def list_memories():
    return load_memories()

def search_memories(keyword):
    memories = load_memories()
    results = []
    for memory in memories:
        if keyword in memory["content"]:
            results.append(memory)
    return results

def extract_keywords(user_message):
    keywords = []
    prompt = "从用户问题中提取适合搜索记忆的关键词。用户问题是：" + user_message
    question = [{"role": "user", "content": prompt}]
    reply = call_llm(question)
    keywords = json.loads(reply)["keywords"]
    return keywords

def format_memories(memories):
    memory_text = ""
    for memory in memories:
        memory_text = memory_text + "- " + memory["content"] + "\n"

    return memory_text

def search_related_memories(user_message):
    keywords = extract_keywords(user_message=user_message)
    memories = []

    for keyword in keywords:
        memory = search_memories(keyword=keyword)
        memories.extend(memory)
    if memories == []:
        return "没有找到相关记忆。"
    memories_text = format_memories(memories)
    return memories_text

def answer_with_memory(user_message):
    memory = search_related_memories(user_message)
    messages = []
    messages.append({"role": "user", "content": "记忆是：" + memory + "用户问题是" + user_message})
    reply = call_llm(messages=messages)
    return reply


results = answer_with_memory("我现在学到哪里了？")
print(json.loads(results)["reply"])


