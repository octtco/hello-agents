# lelele Agent 手搓课程

本课程基于 Hello-Agents 项目、`COURSE_OUTLINE.md`、`TEACHING_PROGRESS.md` 和 `lessons/` 实操代码重排。目标不是把原仓库 16 章从头硬啃，而是让 lelele 最终能不用现成 Agent 框架，自己用 Python 手搓一个可运行的 Agent。

## 课程原则

- 先直觉，再概念，再代码，再总结。
- 每课都包含：语法基础、理论知识、代码实操。
- 每次开新课前先说：本课目标、为什么学、学完能做什么。
- 讲代码时先拆小积木，再组合成完整程序。
- 重复知识点时标注：复习、加深、新知识。
- 涉及 OpenAI API、SDK、模型等变化快内容时，以当前官方文档或本机已跑通配置为准。

## 当前进度

- 已完成：第 1 课到第 8 课。
- 当前入口：第 9 课，记忆系统，已跑通最小记忆问答链路。
- 已完成本课当前链路：`memory.json` 保存记忆 -> 提取关键词 -> 搜索相关记忆 -> 格式化记忆 -> 让 LLM 根据记忆回答。
- 下一步：写 `decide_memory_action(user_message)`，让 Agent 判断用户消息应该新增记忆、查询记忆，还是普通聊天。

## 主线课程

### 第 1 课：电脑和 Python 最小生存

本课目标：知道代码文件是什么，终端是什么，Python 程序怎么跑。

- 为什么学：Agent 本质上也是一个程序，先要知道程序如何接收输入、处理、输出。
- 语法基础：变量、字符串、`print()`、`input()`、函数、`if`、`while True`、`break`、`return`。
- 理论知识：程序 = 输入 -> 处理 -> 输出。
- 代码实操：写一个假的命令行聊天 Agent，不接 LLM，只按规则回复。
- 实操文件：`lessons/lesson_01/fake_agent.py`。
- 原始参考：`docs/chapter1/第一章 初识智能体.md`、`docs/chapter2/第二章 智能体发展史.md`。
- 完成标准：能解释 `input()` 为什么会等待输入，`return` 为什么能把结果送回来。

### 第 2 课：LLM API 是什么

本课目标：知道大模型 API 本质上就是一个远程函数。

- 为什么学：Agent 的大脑通常来自远程模型，代码要能把消息送过去，再拿回回复。
- 语法基础：list、dict、函数返回值、环境变量直觉。
- 理论知识：API、请求、响应、message、role、`api_key`、`base_url`、`model`。
- 代码实操：手写 `call_llm(messages)`，完成一次模型调用。
- 实操文件：`lessons/lesson_02/llm_api_demo.py`。
- 原始参考：`docs/chapter3/第三章 大语言模型基础.md`。
- 完成标准：能说清楚 `api_key` 是谁、`base_url` 是去哪、`model` 是用哪个脑子、`messages` 是说什么。

### 第 3 课：第一个裸 Agent

本课目标：把 LLM 调用包成一个最小 Agent。

- 为什么学：只有一次模型调用还不是 Agent；Agent 需要保存目标、状态和对话历史。
- 语法基础：类、对象、`__init__`、`self`、方法。
- 理论知识：Agent = LLM + 目标 + 状态 + 行动。
- 代码实操：手写 `SimpleAgent`，支持 system prompt 和多轮对话。
- 实操文件：`lessons/lesson_03/simple_agent.py`。
- 原始参考：`docs/chapter1/第一章 初识智能体.md`、`docs/chapter7/第七章 构建你的Agent框架.md`。
- 完成标准：能解释为什么没有 `return reply` 会打印 `None`。

### 第 4 课：Prompt 是程序

本课目标：理解提示词不是玄学，而是给模型的软代码。

- 为什么学：Agent 的行为很大一部分来自 prompt 约束，prompt 写不好，程序会变得不稳定。
- 语法基础：多行字符串、字符串拼接、JSON 字符串、`json.loads()`。
- 理论知识：system prompt、角色、任务、输出格式、Structured Outputs。
- 代码实操：写一个只能按指定 JSON 格式回答的 Agent。
- 实操文件：`lessons/lesson_04/prompt_as_program.py`。
- 原始参考：`docs/chapter3/第三章 大语言模型基础.md`。
- 完成标准：能区分 prompt-only JSON 和 schema 约束。

### 第 5 课：工具调用

本课目标：让 Agent 学会用外部函数做事。

- 为什么学：LLM 负责判断和表达，工具负责真正计算、搜索、读写文件。
- 语法基础：函数参数、字典映射、模块导入、异常处理、`**arguments`。
- 理论知识：工具名、工具描述、工具参数、工具注册表、官方 function calling。
- 代码实操：写计算器工具和工具注册表，让 Agent 自动调用计算器。
- 实操文件：`lessons/lesson_05/tool_calling.py`、`lessons/lesson_05/official_tools.py`。
- 原始参考：`docs/chapter4/第四章 智能体经典范式构建.md`、`docs/chapter7/第七章 构建你的Agent框架.md`。
- 完成标准：能说明手搓版 `tool_name/arguments` 和官方 `function_call/call_id` 的对应关系。

### 第 5.5 课：补地基

本课目标：打开第 4-5 课里的黑箱。

- 为什么学：不能只会跑，要知道 OpenAI SDK 返回了什么，JSON Schema 到底约束了什么。
- 语法基础：`append()`、`extend()`、`+=`、字典取值、嵌套 object。
- 理论知识：JSON、JSON Schema、`response`、`response.output`、`response.output_text`。
- 代码实操：打印并观察 Responses API 的返回对象。
- 实操文件：`lessons/lesson_05/inspect_response.py`。
- 原始参考：`TEACHING_PROGRESS.md` 第 5.5 课记录。
- 完成标准：能解释为什么第一次工具调用时 `response.output_text` 可能为空。

### 第 6 课：ReAct 核心

本课目标：让 Agent 一边想，一边行动，一边观察结果。

- 为什么学：ReAct 是很多 Agent 行动循环的基本骨架。
- 语法基础：`while` 循环、`if/elif`、JSON 解析、工具字典。
- 理论知识：Thought、Action、Observation、Finish。
- 代码实操：复刻简化版 ReAct Agent，支持一步步调用工具。
- 实操文件：`lessons/lesson_06/react_agent.py`。
- 原始参考：`docs/chapter4/第四章 智能体经典范式构建.md`。
- 完成标准：能解释 Observation 为什么要放回 messages。

### 第 7 课：Plan-and-Solve

本课目标：让 Agent 先拆计划，再按步骤执行。

- 为什么学：复杂任务如果边想边做容易乱，先规划能降低混乱。
- 语法基础：列表遍历、状态记录、步骤编号、结构化输出。
- 理论知识：规划器、执行器、任务拆解、状态管理。
- 代码实操：写一个先生成计划、再逐步执行并汇总结果的 Agent。
- 实操文件：`lessons/lesson_07/plan_and_solve.py`。
- 原始参考：`docs/chapter4/第四章 智能体经典范式构建.md`。
- 完成标准：能说明为什么不能简单粗暴用 `steps[:5]` 截断计划。

### 第 8 课：Reflection 自我修正

本课目标：让 Agent 发现自己可能错了，并尝试修正。

- 为什么学：真实 Agent 需要检查和重试，不能一次输出就盲信。
- 语法基础：日志、历史记录、错误处理、硬规则兜底。
- 理论知识：反思、审查、重试、Evaluator、成本收益。
- 代码实操：写一个回答后自检，不合格就重答的 Agent。
- 实操文件：`lessons/lesson_08/reflection_agent.py`。
- 原始参考：`docs/chapter4/第四章 智能体经典范式构建.md`。
- 完成标准：能解释为什么不能只相信模型自己给自己打分。

### 第 9 课：记忆系统

本课目标：让 Agent 记住用户信息和过去发生的事。

- 为什么学：没有记忆的 Agent 每次都像第一次见用户；有记忆后才能延续上下文和个性化服务。
- 语法基础：JSON 文件、`Path`、文件读写、列表搜索、简单数据结构。
- 理论知识：工作记忆、长期记忆、情景记忆、语义记忆、遗忘。
- 代码实操：手写 JSON 记忆库，支持 `add / search / list`。
- 实操文件：`lessons/lesson_09/memory_agent.py`、`lessons/lesson_09/memory.json`。
- 原始参考：`docs/chapter8/第八章 记忆与检索.md`。
- 完成标准：能实现并解释 `load_memories()`、`save_memories()`、`add_memory()`、`search_memories()`。
- 当前进展：已完成最小记忆问答链路，能回答“我现在学到哪里了？”。
- 下一小步：规则版记忆路由器 `decide_memory_action(user_message)`，先输出 `add / search / chat`。

### 第 10 课：RAG 检索

本课目标：让 Agent 可以从资料里找答案，而不是只靠模型脑补。

- 为什么学：模型内置知识有限，RAG 能把外部资料临时交给模型。
- 语法基础：文本切块、排序、简单相似度、列表筛选。
- 理论知识：上下文窗口、chunk、embedding 的直觉、检索增强。
- 代码实操：写一个最小文档问答 Agent。
- 实操文件：建议新增 `lessons/lesson_10/rag_agent.py`。
- 原始参考：`docs/chapter8/第八章 记忆与检索.md`。
- 完成标准：能解释 RAG 和 Memory 的区别：资料库找知识，记忆库找经历和用户偏好。

### 第 11 课：上下文工程

本课目标：学会决定“该把什么信息塞给模型”。

- 为什么学：Agent 能力不是只看模型，还看你给模型的上下文是否合适。
- 语法基础：字符串拼接、消息裁剪、摘要字段、优先级排序。
- 理论知识：token 预算、上下文优先级、历史压缩、工具说明拼装。
- 代码实操：写 `ContextBuilder`，拼装 system、history、memory、tools。
- 实操文件：建议新增 `lessons/lesson_11/context_builder.py`。
- 原始参考：`docs/chapter9/第九章 上下文工程.md`。
- 完成标准：能说清楚 system、history、memory、tools 谁应该先放、谁可以裁剪。

### 第 12 课：智能体评估

本课目标：学会判断 Agent 到底有没有变好。

- 为什么学：没有评估，就只能凭感觉说“好像更聪明了”。
- 语法基础：测试样例、结果记录、简单评分表。
- 理论知识：成功率、工具调用正确率、幻觉、稳定性、成本。
- 代码实操：给前面的 Agent 写 5-10 个测试问题和评分函数。
- 实操文件：建议新增 `lessons/lesson_12/evaluate_agent.py`。
- 原始参考：`docs/chapter12/第十二章 智能体性能评估.md`。
- 完成标准：能用固定测试集比较两个版本 Agent。

### 第 13 课：协议选学

本课目标：知道 MCP、A2A、ANP 是在解决什么问题。

- 为什么学：当 Agent 不再只是单个脚本，就需要和工具、服务、其他 Agent 通信。
- 语法基础：客户端/服务端、请求/响应、配置文件。
- 理论知识：MCP 管工具，A2A 管 Agent 间通信，ANP 偏网络发现和协作。
- 代码实操：跑通一个最小 MCP 工具连接。
- 实操文件：`code/chapter10/`。
- 原始参考：`docs/chapter10/第十章 智能体通信协议.md`。
- 完成标准：能用自己的话说明 MCP 和普通函数工具的区别。

### 第 14 课：综合项目：研究助手 Agent

本课目标：把前面零件拼成一个不用框架的完整 Agent。

- 为什么学：单个功能不等于系统，毕业前要拼一次完整链路。
- 语法基础：项目结构、模块拆分、测试入口。
- 理论知识：LLM、Tool、Memory、Planner、Evaluator 的组合。
- 代码实操：手搓一个研究助手 Agent，支持搜索、记录、总结、评估。
- 实操文件：建议新增 `lessons/final_project/research_agent/`。
- 原始参考：`docs/chapter14/第十四章 自动化深度研究智能体.md`、`docs/chapter16/第十六章 毕业设计.md`。
- 完成标准：能完成一次小主题研究，并保存过程记录和最终总结。

### 第 15 课：毕业项目

本课目标：做一个属于 lelele 的完整 Agent 应用。

- 为什么学：课程最终目标不是看懂教程，而是能把 Agent 用到自己的真实需求里。
- 语法基础：README、依赖文件、运行入口、基础测试。
- 理论知识：需求拆解、功能边界、演示、复盘。
- 代码实操：从 3 个方向中选一个：学习助手、资料问答助手、研究助手。
- 实操文件：建议新增 `Co-creation-projects/lelele-Agent/` 或 `lessons/final_project/`。
- 原始参考：`docs/chapter16/第十六章 毕业设计.md`。
- 完成标准：别人能按 README 跑起来，并看到一个完整 Agent 工作流。

## 选学内容

- 低代码平台：`docs/chapter5/第五章 基于低代码平台的智能体搭建.md`。先不作为主线，适合了解产品形态。
- 现成框架：`docs/chapter6/第六章 框架开发实践.md`。先不作为主线，等手搓基本功稳定后再看。
- Agentic RL：`docs/chapter11/第十一章 Agentic-RL.md`。暂时不作为主线，属于训练模型阶段。
- 赛博小镇：`docs/chapter15/第十五章 构建赛博小镇.md`。适合后期做兴趣项目。

## 每节课固定收尾

- 本课总结：3-5 句话，用人话复述今天学了什么。
- 作业：一个最小代码任务，一个解释题。
- 下一课入口：说明下一课为什么自然接上今天。
- 进度记录：必要时更新 `TEACHING_PROGRESS.md`。
