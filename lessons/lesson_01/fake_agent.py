def fake_agent_reply(user_message):
    if user_message == "你好":
        return "你好 lelele，我是一个假的 Agent。"

    if user_message == "你会什么":
        return "我现在只会按规则回复，但以后会接入大模型。"

    if user_message == "Agent 是什么":
        return "Agent 就是能接收任务、自己处理、再给出结果的程序。"

    return "这句话我还不会回答。"


while True:
    user_message = input("你：")

    if user_message == "退出":
        print("Agent：下次见。")
        break

    reply = fake_agent_reply(user_message)
    print("Agent：" + reply)
