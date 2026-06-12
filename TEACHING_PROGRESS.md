# Agent 教学进度记录

本文件记录 lelele 学习 Agent 的动态进度、课程效果、卡点、复习计划和教学画像更新。

`AGENTS.md` 是长期教学规则和课程大纲；本文件是随学习推进不断更新的教学日志。

## 当前课程进度

- 当前阶段：第 7 课进行中，最小 Plan-and-Solve 主流程已跑通。
- 当前课程：第 7 课，Plan-and-Solve。
- 下一步：总结第 7 课，补充计划步数限制、执行成本和上下文膨胀问题。

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
- 第 4 课：Prompt 是程序。
  - 已讲解 Prompt 作为“软代码”的直觉：角色、任务、格式。
  - 已确认当前结构化输出主线：新项目优先使用 Responses API + Structured Outputs；本课先体验 prompt-only JSON，再升级到 schema 约束。
  - 已创建空文件 `lessons/lesson_04/prompt_as_program.py`，由 lelele 自己写内容。
  - lelele 已完成 prompt-only JSON 输出版本，`client.responses.create(...)`、`response.output_text`、`json.loads(reply)` 目前运行正常。
  - 调试过 JSONDecodeError：原因是 `client.reponses.create` 拼错导致 `call_llm` 返回“模型错误：...”，不是纯 JSON；同时修正了 `confidence` 字段拼写。
  - 已讲解 Structured Outputs：`text.format` + `json_schema` + `strict` + `required` + `additionalProperties`。
  - lelele 已成功跑通 Structured Outputs，说明本机代理 `http://127.0.0.1:15721/v1` 支持 Responses API 的结构化输出。
- 第 5 课：工具调用。
  - 已讲解工具调用直觉：LLM 是大脑，Tool 是手，Agent 负责把两者串起来。
  - 已讲解函数参数、工具注册表 `tools = {"add": add}`、JSON 参数、`tool(**arguments)` 字典解包。
  - 已创建空文件 `lessons/lesson_05/tool_calling.py`，由 lelele 自己写内容。
  - lelele 已完成手搓版工具调用第一阶段：解析工具调用 JSON，按 `tool_name` 从 `tools` 中取函数，用 `tool(**arguments)` 执行，输出 `42`。
  - lelele 已完成手搓版工具调用第二阶段：LLM 通过 Structured Outputs 输出 `answer` 或 `tool_call`，Python 根据 `type` 直接回答或执行 `add` 工具。
  - 已验证两个分支：输入 `你好` 输出 answer；输入 `23+19等于多少` 触发 `tool_call` 并输出 `42`。
  - 调试过 strict schema 错误：嵌套 object 也需要 `additionalProperties: False`；严格模式下 `required` 需要包含 properties 中每个字段，因此教学阶段采用“所有字段必填，不用字段填空/0”的方案。
  - 已创建并跑通官方版 `lessons/lesson_05/official_tools.py`：使用 Responses API `tools` 参数声明 `add`，模型输出 `function_call`，Python 执行工具后以 `function_call_output` 回传，最终输出 `23 + 19 = 42`。
  - 已讲解对应关系：手搓版 `tool_name` 对应官方 `name`；手搓版 `arguments` 对应官方 `arguments` JSON 字符串；官方多 `call_id` 用于关联工具调用与工具结果。
  - 已澄清手搓版和官方版的流程差异：手搓版当前是“模型决策 -> Python 执行 -> Python 直接输出结果”；官方版是“两轮模型调用：模型提出 `function_call` -> Python 执行 -> 回传 `function_call_output` -> 模型生成最终回答”。
  - 已讲解工具调用安全边界：prompt 只是软提醒，tools/schema 是格式约束，真正的硬边界必须在 Python 执行层检查工具名、参数、权限和是否需要用户确认。

## 当前卡点

- 第 1 课反馈：如果面向完全零基础学习者，不能直接给完整代码。需要先解释每个语法积木，例如变量、`print()`、`input()`、`def`、参数、`if`、`while True`、`break`、`return`，并说明运行后能看到什么效果。
- 第 5 课反馈：课程为了推进工具调用主线，临时拓展过多，导致多个底层知识没有提前讲清楚。lelele 虽然能跑通代码，但对 `append`、`extend`、`+=`、OpenAI SDK 的 `response` / `output` / `output_text`、JSON Schema 的通用性、Python `dict` 与 JSON Schema `object` 的关系仍有黑箱感。
- 教学方式卡点：连续两三节课都以“先初步接触”为理由略过底层结构，导致后续概念越堆越多。需要讨论一套机制，避免继续出现“能跑但不真懂”的情况。

## 高频疑惑点

记录 lelele 反复询问、容易混淆、需要换方式解释的知识点。

- 函数定义与调用：`def fake_agent_reply(user_message):` 是什么，参数如何传进去，`return` 如何把结果送出来。
- 条件判断：`if` 如何决定执行哪段代码。
- 循环：`while True` 为什么会一直重复，`break` 如何停止。
- 输入输出：`input()` 会暂停等待用户输入，`print()` 会把结果显示到终端。
- 函数返回值：如果函数没有 `return`，Python 默认返回 `None`。
- 字符串与变量：`"user_message"` 是固定文字，`user_message` 才是变量里的用户输入。
- JSON 基础：`json.loads()` 可把 JSON 字符串转成 Python 字典；需要注意模型输出若夹杂解释文字，解析会失败。
- JSON 解析报错：`JSONDecodeError: Expecting value: line 1 column 1` 通常表示待解析字符串开头就不是 JSON，要先 `print(reply)` 看原始内容。
- Structured Outputs：prompt-only 是柔性约束，Structured Outputs 是 schema 约束，更适合程序稳定解析模型输出。
- 工具调用基础：`tools["add"]` 可以从工具注册表里取出函数；`tool(**arguments)` 会把字典参数展开成命名参数。
- 工具调用双模式：模型输出 `type=answer` 时直接回答；输出 `type=tool_call` 时由 Python 根据 `tool_name` 和 `arguments` 执行函数。
- 官方 function calling：模型只提出 `function_call` 请求，Python 真正执行函数，再把 `function_call_output` 回传给模型生成最终回答。
- 工具安全：Prompt 负责引导，tools/schema 负责描述和约束参数形状，Python 执行层负责真正把门。
- Python 列表操作：`append()` 是把一个东西整体塞进去；`extend()` 是把一串东西拆开逐个加入；`+=` 对列表近似等价于 `extend()`。需要用最小例子重讲。
- OpenAI SDK 返回对象：`response` 不是字符串，`response.output` 是结构化输出列表，`response.output_text` 是 SDK 提取出的文本。需要实际打印 `response`、`response.output`、`type(response.output)` 等观察。
- JSON Schema：JSON 和 JSON Schema 是通用数据格式/格式说明标准，不是 AI 专用；OpenAI Structured Outputs 只是借用了 JSON Schema。
- 类型对应关系：Python 的 `dict` 对应 JSON/JSON Schema 里的 `object`；Python 的 `list` 对应 JSON `array`；Python 字符串/数字/布尔/None 分别对应 JSON string/number/boolean/null。

## 需要复习的知识点

记录后续课程中要主动回炉的内容。

- Python 列表：`append`、`extend`、`+=`、嵌套列表。
- Python 字典：取值、函数作为字典 value、`**arguments` 解包。
- JSON 基础：JSON 字符串、`json.loads`、JSON object/array/string/number/boolean/null。
- JSON Schema 基础：`type`、`properties`、`required`、`additionalProperties`、strict schema 为什么要求更严。
- OpenAI SDK 返回结构：`response`、`response.output`、`response.output_text`、function_call item 的 `type/name/arguments/call_id`。

## 教学效果观察

记录哪些解释方式有效，哪些方式不适合 lelele。

- 当前观察：lelele 需要结构清晰、慢慢拆解、先给整体路线再进入细节。
- 教学主流程不使用 caveman，避免过度压缩影响理解；课后速记、复习卡片、短提醒可使用 caveman lite/full。
- 新观察：lelele 虽然有一点 Python 基础，但能敏锐发现课程对零基础学习者跳步的问题。后续讲代码时要先讲小片段的语法、效果和为什么这样写，再拼成完整程序。
- 有效方式：第 2 课采用“生活类比 -> 语法小积木 -> 组合成 messages -> 再解释 call_llm”的顺序，lelele 反馈能理解。后续继续保持这种拆法。
- 有效方式：第 3 课通过真实报错和运行现象解释 `None`、`return`、字段拼写、变量/字符串区别，效果较好。后续遇到 bug 时优先从“现象 -> 原因 -> 最小修复”讲。
- 需要避免：讲真实 API 时容易偏成“帮忙配置环境/写代码”的工程模式。后续要先保持教学模式：先解释概念图，再拆代码结构，最后才运行或改文件。
- 需要避免：涉及现代 API、模型、SDK、框架、库版本时，不凭记忆讲“当前推荐做法”。讲之前先查官方最新文档，再用教学语言解释。
- 有效方式：第 4 课开始前先查官方最新文档，再说明 Responses API、JSON mode、Structured Outputs 的区别，符合 lelele 对“不要用过时接口”的要求。
- 需要避免：不能连续多节课以“先初步接触”为由跳过关键底层。每当引入新语法、新标准、新 SDK 对象时，必须先回答三件事：它是什么、长什么样、怎么观察。
- 新观察：lelele 对“跑通但黑箱”非常敏感，能发现教学链路里未讲清的概念依赖。后续应在每节课开头列出“本课会用到的新语法/新对象/新标准”，并先补最小理解。
- 需要避免：重复讲已经讲过的语法或概念时，不说明是“刻意复习”还是“忘了之前讲过”。后续重复内容前必须先标注【新知识】、【复习】或【加深】，并说明为什么再次出现。

## 对 lelele 的学习画像更新

教学过程中持续更新，不固定死。

- 学习能力：强。
- 理解特点：抽象概念需要拆成生活例子和最小代码。
- 电脑基础：偏弱，需要补终端、文件、环境变量、依赖安装等基本功。
- 教学偏好：需要明确路线、分课推进、每课有语法基础、理论知识、代码实操。
- 教学节奏：代码实操应采用“先一行/一小段、解释效果、再组合”的方式；不要默认函数、参数、判断、循环已经理解。
- 资料偏好：lelele 希望课程内容贴近最新实践，尤其是 OpenAI API 这类变化快的内容；过时接口可以讲历史背景，但不能当主线。
- 学习风险：如果课程只推进功能而不打开底层结构，lelele 会形成“代码能跑但概念不稳”的不适感。后续需要更明确地区分“今天只预览”与“今天要掌握”，预览内容不能连续积压。
- 教学透明度：lelele 需要知道重复讲某个知识点是因为课程设计中的复习/加深，还是因为上下文没有正确继承。后续每次开课前应回看 `TEACHING_PROGRESS.md` 和必要时 `COURSE_OUTLINE.md`，重复讲时主动说明依据。

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
- 2026-06-08：第 6 课 ReAct 暂缓，新增第 5.5 课补地基。
  - 调整原因：第 4-5 课推进过快，Python 语法、JSON Schema、OpenAI SDK 返回结构存在未讲清的黑箱。
  - 调整内容：在 ReAct 前补一课，系统讲 `append/extend/+=`、dict/list 与 JSON 类型对应、JSON Schema 通用概念、OpenAI `response.output/output_text` 的真实结构。
  - 调整后下一步：先与 lelele 讨论以后如何避免跳步，再开始第 5.5 课。
- 2026-06-09：课程大纲从 `AGENTS.md` 迁移到 `COURSE_OUTLINE.md`。
  - 调整原因：`AGENTS.md` 同时承载协作规则和课程路线，职责过重。
  - 调整内容：`AGENTS.md` 保留教学协作规则和学习者画像；`COURSE_OUTLINE.md` 保存学习目标、项目学习取舍和完整课程大纲。
  - 调整后下一步：后续查教学规则看 `AGENTS.md`，查课程路线看 `COURSE_OUTLINE.md`，查动态进度看 `TEACHING_PROGRESS.md`。
- 2026-06-09：第 5.5 课已补 `append/extend/+=`、JSON/JSON Schema，并开始观察 OpenAI SDK 返回结构。
  - 已新增 `lessons/lesson_05/inspect_response.py`，专门打印 `response`、`response.output`、`response.output_text` 和 `response.output[0]` 的类型与字段。
  - 观察结果：第一次 tools 调用返回的 `response` 类型是 `openai.types.responses.response.Response`；`response.output` 是 list；其中第一项类型是 `ResponseFunctionToolCall`，字段包括 `type=function_call`、`name=add`、`arguments='{"a":23,"b":19}'`、`call_id=...`。
  - 关键理解：第一次工具调用时 `response.output_text` 为空，因为模型没有生成最终文本，而是生成了工具调用请求；最终给用户看的文本来自回传工具结果后的第二次响应。
  - 第 5.5 课已完成：已总结 `append/extend/+=`、JSON/JSON Schema、OpenAI `response/output/output_text`、工具调用第一次响应与最终响应的区别。
- 2026-06-10：第 6 课 ReAct 核心已开始。
  - 已按新机制标注本课知识状态：复习工具调用、while、if/elif、json.loads、tools 字典；加深 Observation 和 messages/history；新知识为 ReAct 的 Reason + Act 循环。
  - 已讲解 Thought / Action / Observation / Finish 的直觉关系。
  - 已创建空文件 `lessons/lesson_06/react_agent.py`，由 lelele 自己写内容。
  - lelele 已完成并跑通最小 ReAct：模型输出 `thought/action/arguments/finish`，Python 执行 `action`，把 `Observation` 放回 `messages`，循环直到 `finish`。
  - 已加入调试打印：User、LLM Reply、Action、Observation、Messages，帮助观察完整 ReAct 过程。
  - 已处理基础边界：最多循环 5 次，未知工具返回错误提示；prompt 中约束 finish 为空时必须有 action，action 为空时必须有 finish。
  - 已完成第 6 课收尾：讲解最大循环次数、未知工具处理、Observation 应写清楚、调试打印后续可升级为 debug/log，以及手搓 ReAct 与官方 tools 循环的关系。
- 2026-06-11：第 7 课 Plan-and-Solve 已开始。
  - 已按新机制标注本课知识状态：复习 list、for 循环、messages/history；加深状态记录；新知识为 Plan-and-Solve；预览 planner/executor 后续拆分。
  - 已讲解 ReAct 与 Plan-and-Solve 的区别：ReAct 是边想边做，Plan-and-Solve 是先规划再执行。
  - 已创建空文件 `lessons/lesson_07/plan_and_solve.py`，由 lelele 自己写内容。
  - lelele 已完成最小 Plan-and-Solve 主流程：`distinguish -> plan -> execute -> summarize`，并把意图判断拆到 `distinguish` 字段，避免污染 `finish`。
  - 已加入调试打印，能观察 Distinguish、Plan、Execute、Summary 各阶段的 prompt、raw reply、steps、results 和 final answer。
  - 已验证 daily 路径可正常回复；复杂问题可进入 plan 路径、生成 steps 并逐步执行。
  - 新边界：planner 可能生成过多步骤，例如 `怎么做一个agent` 生成 14 步，导致执行耗时、上下文变长、token 成本膨胀。后续应限制步骤数量，例如 prompt 要求 3-5 步，或 schema 给 `steps` 加 `minItems/maxItems`。
  - lelele 指出不能简单用 `steps[:5]` 粗暴截断，因为后续步骤可能很重要。更合理的策略是：如果步骤过多，让模型压缩/合并成 3-5 个高层步骤，并要求不要丢失重要信息。Python 截断只能作为最后兜底，不适合作为常规策略。

## 下次教学入口

第 7 课：Plan-and-Solve。

建议开场：

- 本课目标：让 Agent 先拆计划，再按步骤执行。
- 为什么学：ReAct 是边想边做，Plan-and-Solve 是先整体拆解，再逐步完成，适合更长任务。
- 学完能做什么：写一个先生成计划、再逐步执行并汇总结果的 Agent。
