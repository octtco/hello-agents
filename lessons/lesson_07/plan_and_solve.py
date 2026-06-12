import json
from openai import OpenAI

api_key = "PROXY_MANAGED"
base_url = "http://127.0.0.1:15721/v1"    
model = "gpt-5.5"

def call_llm(messages):

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
                        "distinguish": {
                            "type": "string"
                        },
                        "steps": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "maxItems": 5
                            }
                        },
                        "thought": {
                            "type": "string"
                        },
                        "finish": {
                            "type": "string"
                        }
                    },
                    "required":["distinguish","steps", "thought", "finish"],
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
            你是一个智能助手。碰到长任务可以先计划再执行。
            """
        }]

    def plan(self, goal):
        print("=== Goal ===")
        print(goal)
        prompt = "将下面的目标按步骤拆分,请只生成 3 到 5 个关键步骤，不要超过 5 步。,steps 填计划,distinguish为空，finish 为空: " + goal
        print("=== Plan Prompt ===")
        print(prompt)
        self.messages.append({"role": "user", "content": prompt})
        steps = call_llm(self.messages)
        print("=== Plan Raw Reply ===")
        print(steps)
        self.messages.append({"role": "assistant", "content": steps})
        data = json.loads(steps)
        print("=== Plan Thought ===")
        print(data["thought"])
        print("=== Plan Steps ===")
        print(json.dumps(data["steps"], ensure_ascii=False, indent=2))
        return data["steps"]

    def execute(self, state):
        num = 0
        results = []
        for step in state["steps"]:
            num += 1
            print("=== Execute Step " + str(num) + " ===")
            print(step)
            print("=== Previous Results ===")
            print(json.dumps(results, ensure_ascii=False, indent=2))
            prompt = "执行单步时：steps 为空,distinguish为空，finish 填这一步的结果。原始任务：" + state["goal"] + ",完整计划:" + str(state["steps"]) + ",当前步骤：" + step + ",前面步骤结果：" + str(results)
            print("=== Execute Prompt ===")
            print(prompt)
            self.messages.append({"role": "user", "content": prompt})
            result = call_llm(self.messages)
            print("=== Execute Raw Reply ===")
            print(result)
            self.messages.append({"role": "assistant", "content": result})
            data = json.loads(result)
            print("=== Execute Thought ===")
            print(data["thought"])
            print("=== Step Finish ===")
            print(data["finish"])
            results.append(data["finish"])

        return results

    def summarize(self, state):
        prompt = "总结时：steps 为空，distinguish为空，finish 填最终总结。请根据以下步骤结果，生成最终回答。原始任务：" + state["goal"] + ",完整计划:" + str(state["steps"]) + ",每步结果：" + str(state["results"])
        print("=== Summary Prompt ===")
        print(prompt)
        print("=== Summary Input Results ===")
        print(json.dumps(state["results"], ensure_ascii=False, indent=2))
        self.messages.append({"role": "user", "content": prompt})
        summary = call_llm(self.messages)
        print("=== Summary Raw Reply ===")
        print(summary)
        self.messages.append({"role": "assistant", "content": summary})
        data = json.loads(summary)
        print("=== Summary Thought ===")
        print(data["thought"])
        print("=== Summary Finish ===")
        print(data["finish"])
        return data["finish"]

        
    def distinguish(self, user_message):
        prompt = "如果属于日常对话则distinguish填‘daily’steps 为空，如果需要拆分计划则distinguish填‘plan’steps 为空, 输入是：" + user_message
        print("=== Distinguish Prompt ===")
        print(prompt)
        self.messages.append({"role": "user", "content": prompt})
        reply = call_llm(self.messages)
        print("=== Distinguish Raw Reply ===")
        print(reply)
        self.messages.append({"role": "assistant", "content": reply})
        data = json.loads(reply)
        print("=== Distinguish Thought ===")
        print(data["thought"])
        print("=== Distinguish Mode ===")
        print(data["distinguish"])
        return data["distinguish"]

    def chat(self, user_message):
        self.messages.append({"role": "user", "content": user_message})
        print("=== User ===")
        print(user_message)
        mode = self.distinguish(user_message)
        print("=== Mode ===")
        print(mode)
        if mode == "daily":
            answer_text = call_llm(self.messages)
            print("=== DailyMessage ===")
            print(answer_text)
            answer_data = json.loads(answer_text)
            answer = answer_data["finish"]
            self.messages.append({"role": "assistant", "content": answer_text})
        elif mode == "plan":
            steps = self.plan(user_message)
            state = {"goal": user_message, "steps": steps}
            results = self.execute(state)
            state = {"goal": user_message, "steps": steps, "results": results}
            answer = self.summarize(state)
        else:
            answer = "未识别到模式"

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
