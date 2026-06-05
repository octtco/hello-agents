# Agent 教学进度记录

本文件记录 lelele 学习 Agent 的动态进度、课程效果、卡点、复习计划和教学画像更新。

`AGENTS.md` 是长期教学规则和课程大纲；本文件是随学习推进不断更新的教学日志。

## 当前课程进度

- 当前阶段：第 3 课已完成，最小裸 Agent 已跑通。
- 当前课程：准备进入第 4 课，Prompt 是程序。
- 下一步：学习 system prompt、输出格式约束和失败案例，把提示词当成“软代码”来设计。

## 已完成课程

- 第 1 课：电脑和 Python 最小生存。
  - 已创建 `lessons/lesson_01/fake_agent.py`。
  - 已完成一个假的命令行聊天 Agent，包含输入、规则回复、退出循环。
  - lelele 表示第 1 课内容已经会了，可以进入第 2 课。
- 第 2 课：LLM API 是什么。
  - 已创建空文件 `lessons/lesson_02/llm_api_demo.py`，由 lelele 自己写内容。
  - 已讲解 `list`、`dict`、`messages`、`role`、`call_llm(messages)` 的直觉。
  - lelele 反馈本次语法解释方式可以，已经理解。
  - lelele 已完成假 `call_llm(messages)` 代码；运行结果为 `我收到了你的问题：API 是什么？`。
  - 已讲解第三方中转 API：普通调用是“代码 -> 官方服务器”，中转调用是“代码 -> 第三方 base_url -> 模型服务器”。
  - lelele 已理解真实调用的 4 个关键零件：`api_key` 表示我是谁，`base_url` 表示找谁，`model` 表示用哪个模型，`messages` 表示说什么。
  - lelele 指出 Chat Completions 不是当前新项目的最佳主线；后续真实调用改以 Responses API 为主，Chat Completions 只作为理解历史和迁移的对照。
  - lelele 使用本机代理 `http://127.0.0.1:15721/v1` 跑通真实 API 调用；key 由本机代理管理，脚本侧通过 OpenAI SDK 指向本机 `base_url`。
- 第 3 课：第一个裸 Agent。
  - 已讲解 `class`、对象、`__init__`、`self`、`messages` 作为对话历史的直觉。
  - 已创建空文件 `lessons/lesson_03/simple_agent.py`，由 lelele 自己写内容。
  - lelele 已完成最小 Agent 并成功运行，支持 `chat(user_message)`、保存 `messages`、调用真实 LLM、返回回复。
  - 调试过 `None` 输出问题：原因是 `chat()` 没有 `return reply`；同时修正了 `content` 拼写和变量/字符串混淆。

## 当前卡点

- 第 1 课反馈：如果面向完全零基础学习者，不能直接给完整代码。需要先解释每个语法积木，例如变量、`print()`、`input()`、`def`、参数、`if`、`while True`、`break`、`return`，并说明运行后能看到什么效果。

## 高频疑惑点

记录 lelele 反复询问、容易混淆、需要换方式解释的知识点。

- 函数定义与调用：`def fake_agent_reply(user_message):` 是什么，参数如何传进去，`return` 如何把结果送出来。
- 条件判断：`if` 如何决定执行哪段代码。
- 循环：`while True` 为什么会一直重复，`break` 如何停止。
- 输入输出：`input()` 会暂停等待用户输入，`print()` 会把结果显示到终端。
- 函数返回值：如果函数没有 `return`，Python 默认返回 `None`。
- 字符串与变量：`"user_message"` 是固定文字，`user_message` 才是变量里的用户输入。

## 需要复习的知识点

记录后续课程中要主动回炉的内容。

- 暂无。

## 教学效果观察

记录哪些解释方式有效，哪些方式不适合 lelele。

- 当前观察：lelele 需要结构清晰、慢慢拆解、先给整体路线再进入细节。
- 教学主流程不使用 caveman，避免过度压缩影响理解；课后速记、复习卡片、短提醒可使用 caveman lite/full。
- 新观察：lelele 虽然有一点 Python 基础，但能敏锐发现课程对零基础学习者跳步的问题。后续讲代码时要先讲小片段的语法、效果和为什么这样写，再拼成完整程序。
- 有效方式：第 2 课采用“生活类比 -> 语法小积木 -> 组合成 messages -> 再解释 call_llm”的顺序，lelele 反馈能理解。后续继续保持这种拆法。
- 有效方式：第 3 课通过真实报错和运行现象解释 `None`、`return`、字段拼写、变量/字符串区别，效果较好。后续遇到 bug 时优先从“现象 -> 原因 -> 最小修复”讲。
- 需要避免：讲真实 API 时容易偏成“帮忙配置环境/写代码”的工程模式。后续要先保持教学模式：先解释概念图，再拆代码结构，最后才运行或改文件。
- 需要避免：涉及现代 API、模型、SDK、框架、库版本时，不凭记忆讲“当前推荐做法”。讲之前先查官方最新文档，再用教学语言解释。

## 对 lelele 的学习画像更新

教学过程中持续更新，不固定死。

- 学习能力：强。
- 理解特点：抽象概念需要拆成生活例子和最小代码。
- 电脑基础：偏弱，需要补终端、文件、环境变量、依赖安装等基本功。
- 教学偏好：需要明确路线、分课推进、每课有语法基础、理论知识、代码实操。
- 教学节奏：代码实操应采用“先一行/一小段、解释效果、再组合”的方式；不要默认函数、参数、判断、循环已经理解。
- 资料偏好：lelele 希望课程内容贴近最新实践，尤其是 OpenAI API 这类变化快的内容；过时接口可以讲历史背景，但不能当主线。

## 大纲调整记录

每次调整课程大纲时记录：

- 调整时间
- 调整原因
- 调整内容
- 调整后下一步

- 2026-06-05：第 2 课真实 API 调用主线从 Chat Completions 调整为 Responses API。
  - 调整原因：lelele 指出 Chat Completions 已不是新项目最推荐主线。
  - 调整内容：保留 Chat Completions 作为历史对照；后续真实 `call_llm` 教学版优先使用 `client.responses.create(...)` 和 `response.output_text`。
  - 调整后下一步：重新讲 Responses API 版 `call_llm` 的结构。

## 下次教学入口

第 4 课：Prompt 是程序。

建议开场：

- 本课目标：理解提示词不是玄学，而是给模型的“软代码”。
- 为什么学：Agent 的行为不仅由 Python 控制，也由 system prompt 控制。
- 学完能做什么：写一个要求模型按固定 JSON 格式回答的 Agent，并观察提示词约束失败时会发生什么。
