import json
from openai import OpenAI

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
                        "draft": {
                            "type": "string"
                        },
                        "check": {
                            "type": "object",
                            "properties": {
                                "pass": {
                                    "type": "boolean"
                                },
                                "feedback": {
                                    "type": "string"
                                },
                                "score": {
                                    "type": "number"
                                }
                            },
                            "required": ["pass", "feedback", "score"],
                            "additionalProperties": False
                        },  
                        "thought": {
                            "type": "string"
                        }
                    },
                    "required":["draft","check", "thought"],
                    "additionalProperties": False
                }
            }
        }
    )

    print("=== LLM Raw Reply ===")
    print(reply.output_text)
    return reply.output_text

class simpleAgent:
    def __init__(self):
        self.messages = [{
            "role": "system", "content": """
            你是一个智能助手。不需要检查时，check.pass 填 true，feedback 填空字符串，score 填 0。
            """
        }]

    def check(self, user_message, draft):
        prompt = "你是一个严格审稿老师，不是鼓励老师。请根据原始问题检查回答。只要出现以下任意问题，就必须 pass=false：1. 没有回答原问题；2. 太空，没有具体步骤；3. 漏掉用户要求；4. 只说概念，没有可执行建议；5. 还有任何可以明显改进的地方。普通回答最高只能给 7 分；比较具体但仍可改进的回答最高只能给 8 分；只有完全满足问题、非常具体、没有明显改进空间时，才能给 9 分以上。评分低于 10 分时，pass 必须是 false。将检查结果写在 check 里。draft 置空。pass 是是否通过，feedback 是检查结果，score 是回复得分。原始问题是："  + user_message + "。待检查回复是：" + draft
        print("=== Check Prompt ===")
        print(prompt)
        self.messages.append({"role": "user", "content": prompt})
        feedback = call_llm(self.messages)
        print("=== Check Raw Reply ===")
        print(feedback)
        self.messages.append({"role": "assistant", "content": feedback})
        return feedback
        
    def revise(self, feedback):
        prompt = "上次的回复质量不够，需要根据检查结构修改。改正后的内容放在draft，check.pass 填 true，feedback 填空字符串，score 填 0。检查结果是" + feedback
        print("=== Revise Prompt ===")
        print(prompt)
        self.messages.append({"role": "user", "content": prompt})
        reply = call_llm(self.messages)
        print("=== Revise Raw Reply ===")
        print(reply)
        self.messages.append({"role": "assistant", "content": reply})
        return reply

        
    def chat(self, user_message):
        print("=== User ===")
        print(user_message)
        self.messages.append({"role": "user", "content": user_message})
        print("=== Draft Start ===")
        draft = call_llm(self.messages)
        print("=== Draft Raw Reply ===")
        print(draft)
        print("=== Check Start ===")
        feedback = self.check(user_message, draft)
        feedback_data = json.loads(feedback)
        print("=== Check Result ===")
        print("Pass:", feedback_data["check"]["pass"])
        print("Score:", feedback_data["check"]["score"])
        print("Feedback:", feedback_data["check"]["feedback"])
        check = feedback_data["check"]
        passed = check["pass"] and check["score"] >= 10 and check["feedback"] == ""
        print("Python Hard Pass:", passed)
        if passed:
            answer = json.loads(draft)["draft"]
            print("=== Final Path ===")
            print("检查满分且没有反馈，直接返回初稿")
            print("=== Final Answer ===")
            print(answer)
            return answer
        else:
            print("=== Revise Start ===")
            reply = self.revise(feedback)
            answer = json.loads(reply)["draft"]
            print("=== Final Path ===")
            print("检查未通过，返回修正版")
            print("=== Final Answer ===")
            print(answer)
            return answer
    
agent = simpleAgent()

while True:
    user_message = input("你：")
    if user_message == "退出":
        print("Agent：下次见")
        break

    reply = agent.chat(user_message=user_message)
    print("Agent answer：" + reply)
