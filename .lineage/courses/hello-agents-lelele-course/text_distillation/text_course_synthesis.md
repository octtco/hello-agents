# hello-agents-lelele-course — Text Course Synthesis

This synthesis is generated from pure-text sources and OCR/notes artifacts.

## 关键概念

- =concept or "general",（Chapter8-Memory-and-Retrieval.md#407）
- inalTool** (`hello_agents/tools/builtin/terminal_tool.py`)：Terminal tool that supports file system operations and just-in-time context retrieval for agents（Chapter9-Context-Engineering.md#5）
- inalTool provides agents with **secure command-line execution capability**, supporting common file system and text processing commands, while ensuring system security through multi-layer security mechanisms. This design implements the "Just-in-time (JIT) context" concept mentioned in Section 9.2.2—agents don't need to preload all files, but explore and retrieve on demand.（Chapter9-Context-Engineering.md#376）
- inal.run({"command"："find . -name '*.py' -type f"}) # Fast, real-time（Chapter9-Context-Engineering.md#383）
- inal.run({"command"："grep -r 'class UserService' ."}) # Precise location（Chapter9-Context-Engineering.md#383）
- inal.run({"command"："head -n 50 src/services/user.py"}) # View on demand（Chapter9-Context-Engineering.md#383）
- inal.run({"command"："ls -lh /var/log/app.log"})（Chapter9-Context-Engineering.md#386）
- inal.run({"command"："tail -n 100 /var/log/app.log | grep ERROR"})（Chapter9-Context-Engineering.md#387）
- inal.run({"command"："grep ERROR /var/log/app.log | cut -d':' -f3 | sort | uniq -c"})（Chapter9-Context-Engineering.md#388）
- inal.run({"command"："head -n 5 data/sales.csv"})（Chapter9-Context-Engineering.md#391）
- inal.run({"command"："wc -l data/*.csv"})（Chapter9-Context-Engineering.md#392）
- inal.run({"command"："head -n 1 data/sales.csv | tr ',' '\n'"})（Chapter9-Context-Engineering.md#393）
- inal.run({"command"："rm -rf /"})（Chapter9-Context-Engineering.md#401）
- inalTool can only access the specified working directory and its subdirectories, cannot access other parts of the system:（Chapter9-Context-Engineering.md#403）
- inal = TerminalTool(workspace="./project")（Chapter9-Context-Engineering.md#404）
- inal.run({"command"："cat ./src/main.py"}) # ✅（Chapter9-Context-Engineering.md#405）
- inal.run({"command"："cat /etc/passwd"}) # ❌ Not allowed to access paths outside working directory（Chapter9-Context-Engineering.md#406）
- inal.run({"command"："cd ../../../etc"}) # ❌ Not allowed to access paths outside working directory（Chapter9-Context-Engineering.md#407）
- inal = TerminalTool(（Chapter9-Context-Engineering.md#411）
- inal.run({"command"："find / -name '*.log'"})（Chapter9-Context-Engineering.md#412）
- inal.run({"command"："cat huge_file.log"})（Chapter9-Context-Engineering.md#416）
- inal.run({"command"："ls -la"})（Chapter9-Context-Engineering.md#441）
- inal.run({"command"："cd src"})（Chapter9-Context-Engineering.md#442）
- inal.run({"command"："find . -name '*service*.py'"})（Chapter9-Context-Engineering.md#443）
- inal.run({"command"："cat user_service.py"})（Chapter9-Context-Engineering.md#444）
- inalTool supports various common file system operation patterns.（Chapter9-Context-Engineering.md#446）
- inal = TerminalTool(workspace="./my_project")（Chapter9-Context-Engineering.md#450）
- inal = TerminalTool(workspace="./data")（Chapter9-Context-Engineering.md#456）
- inal = TerminalTool(workspace="/var/log")（Chapter9-Context-Engineering.md#462）
- inal = TerminalTool(workspace="./codebase")（Chapter9-Context-Engineering.md#468）
- inalTool output can be part of the context:（Chapter9-Context-Engineering.md#484）
- inalTool：Secure command-line tool, supports instant file system access（Chapter9-Context-Engineering.md#634）
- inalTool provides file system operation capabilities, but Section 9.5.2 emphasiz：Are the current security mechanisms (path validation, command whitelist, permission check) sufficient? If the agent needs to access sensitive files or execute dangerous operations, how should a "human-machine collaborative approval" process be designed?（Chapter9-Context-Engineering.md#648）
- inalTool** (`hello_agents/tools/builtin/terminal_tool.py`)：终端工具，支持智能体进行文件系统操作和即时上下文检索（第九章 上下文工程.md#5）
- 当对话接近上下文上限时：对其进行高保真总结，并用该摘要重启一个新的上下文窗口，以维持长程连贯性。（第九章 上下文工程.md#40）
- 也称“智能体记忆”。智能体以固定频率将关键信息写入<strong>上下文外的持久化存储</strong>：在后续阶段按需拉回。（第九章 上下文工程.md#41）
- inalTool 为智能体提供了<strong>安全的命令行执行能力</strong>，支持常用的文件系统和文本处理命令，同时通过多层安全机制确保系统安全。这种：智能体不需要预先加载所有文件，而是按需探索和检索。（第九章 上下文工程.md#376）
- inal.run({"command"："find . -name '*.py' -type f"}) # 快速、实时（第九章 上下文工程.md#383）
- inal.run({"command"："grep -r 'class UserService' ."}) # 精确定位（第九章 上下文工程.md#383）
- inal.run({"command"："head -n 50 src/services/user.py"}) # 按需查看（第九章 上下文工程.md#383）
- inalTool 只能访问指定的工作目录及其子目录：无法访问系统其他部分：（第九章 上下文工程.md#403）
- inal.run({"command"："cat /etc/passwd"}) # ❌ 不允许访问工作目录外的路径（第九章 上下文工程.md#406）
- inal.run({"command"："cd ../../../etc"}) # ❌ 不允许访问工作目录外的路径（第九章 上下文工程.md#407）
- inalTool 的实现聚焦于两个核心功能：命令执行和目录导航。（第九章 上下文工程.md#419）
- inalTool 支持多种常见的文件系统操作模式。（第九章 上下文工程.md#446）
- inalTool 的真正威力在于与 MemoryTool、NoteTool 和 ContextBuilder 的协同使用。（第九章 上下文工程.md#474）
- inalTool 发现的信息可以存储到记忆系统中：（第九章 上下文工程.md#476）
- inalTool 的输出可以作为上下文的一部分：（第九章 上下文工程.md#484）
- inalTool提供了文件系统操作能力，但在9.5.2节中强调了安全性设计。请分析：当前的安全机制（路径验证、命令白名单、权限检查）是否足够？如果智能体需要访问敏感文件或执行危险操作，应该如何设计一个"人机协作审批"流程？（第九章 上下文工程.md#648）

## 方法流程

- extensibility is one of the important considerations in design. You now need to extend the `HelloAgents` framework to implement some interesting new features and characteristics.（Chapter7-Building-Your-Agent-Framework.md#525）
- 化的 ReActAgent 在保持核心逻辑不变的同时：提升了代码的组织性和可维护性，主要是通过提示词优化和与框架工具系统的集成。（第七章 构建你的Agent框架.md#245）
- 化的ReActAgent将执行流程分解为清晰的步骤：（第七章 构建你的Agent框架.md#263）
- 实现了智能的后端选择逻辑：（第七章 构建你的Agent框架.md#413）
- 的可扩展性是设计的重要考量因素之一。你现在要扩展 `HelloAgents` 框架：为其实现一些有趣的新功能和特性。（第七章 构建你的Agent框架.md#534）
- ing Layer：Document parsing, chunking, vectorization（Chapter8-Memory-and-Retrieval.md#263）
- ed_texts = []（Chapter8-Memory-and-Retrieval.md#308）
- ed_content = _preprocess_markdown_for_embedding(raw_content)（Chapter8-Memory-and-Retrieval.md#308）
- ed_texts.append(processed_content)（Chapter8-Memory-and-Retrieval.md#308）
- _time = time.time()：start_time（Chapter8-Memory-and-Retrieval.md#375）
- trade-offs can follow these rules of thumb:（Chapter9-Context-Engineering.md#43）
- 取舍可以遵循以下经验法则：（第九章 上下文工程.md#43）
- 1：Using Function Calling**（Chapter10-Agent-Communication-Protocols.md#99）
- 2：Using MCP**（Chapter10-Agent-Communication-Protocols.md#105）
- 1：Using Built-in Demo Server**（Chapter10-Agent-Communication-Protocols.md#211）
- 2：Connecting to External MCP Servers**（Chapter10-Agent-Communication-Protocols.md#220）
- 1：Through Smithery CLI（Chapter10-Agent-Communication-Protocols.md#537）
- 2：Configure in Claude Desktop（Chapter10-Agent-Communication-Protocols.md#540）
- 3：Use in HelloAgents（Chapter10-Agent-Communication-Protocols.md#542）
- 1：Clone from Official GitHub Repository (Recommended)**（Chapter12-Agent-Performance-Evaluation.md#106）
- 2：Load Official Data Using HelloAgents**（Chapter12-Agent-Performance-Evaluation.md#112）
- 1：Using BFCLEvaluationTool (Recommended)**（Chapter12-Agent-Performance-Evaluation.md#124）
- 2：Using One-Click Evaluation Script**（Chapter12-Agent-Performance-Evaluation.md#157）
- 3：Directly Using Dataset and Evaluator**（Chapter12-Agent-Performance-Evaluation.md#162）
- 1：Automatic Download Using HelloAgents (Recommended)**（Chapter12-Agent-Performance-Evaluation.md#342）
- 2：Manual Download**（Chapter12-Agent-Performance-Evaluation.md#351）
- 1：One-Click Evaluation Using GAIAEvaluationTool**（Chapter12-Agent-Performance-Evaluation.md#360）
- 2：Using Dataset + Evaluator (Flexible Customization)**（Chapter12-Agent-Performance-Evaluation.md#382）
- 1：运行HelloAgents评估（第十二章 智能体性能评估.md#132）
- 2：导出BFCL格式结果（第十二章 智能体性能评估.md#136）
- 3：运行BFCL官方评估（第十二章 智能体性能评估.md#137）
- 4：生成评估报告（第十二章 智能体性能评估.md#141）
- 2：导出GAIA格式结果（第十二章 智能体性能评估.md#369）
- 3：生成评估报告（第十二章 智能体性能评估.md#370）
- results：Deduplicate, limit tokens, format（Chapter14-Automated-Deep-Research-Agent.md#375）
- Description**:（Chapter14-Automated-Deep-Research-Agent.md#448）
- 1：Use .env file**（Chapter16-Graduation-Project.md#276）
- 2：Set directly in Notebook**（Chapter16-Graduation-Project.md#278）

## 质量标准

- Markdown文本 → 标题层次解析 → 段落语义分割 → Token计算分块 → 重叠策略优化 → 向量化准备（第八章 记忆与检索.md#272）
- get_weather(unit="celsius", city="Beijing")（第十二章 智能体性能评估.md#68）
- calculate(x=5)（第十二章 智能体性能评估.md#69）
- get_weather(city="Beijing")（第十二章 智能体性能评估.md#70）
- （1-5 分）：正确性、清晰度、难度匹配、完整性（第十二章 智能体性能评估.md#518）

## 模板资产

- 部分使用 Ant Design Vue 的组件：（第十三章 智能旅行助手.md#282）

## 迁移规则

- Case and Analysis：MYCIN System**（Chapter2-History-of-Agents.md#23）
- Layer：Intelligent Q&A, search, management（Chapter8-Memory-and-Retrieval.md#263）
- 层：智能问答、搜索、管理（第八章 记忆与检索.md#256）

## 案例线索

- We directly give the model instructions, requiring it to complete the sentiment classification task.（Chapter3-Fundamentals-of-Large-Language-Models.md#173）
- We first give the model a complete "question-answer" pair as a demonstration, then pose our new question.（Chapter3-Fundamentals-of-Large-Language-Models.md#176）
- We provide multiple examples covering different situations, allowing the model to have a more comprehensive understanding of the task.（Chapter3-Fundamentals-of-Large-Language-Models.md#181）
- Demonstration：** Suppose our mini corpus is `{"hug": 1, "pug": 1, "pun": 1, "bun": 1}`, and we want to build a vocabulary of size 10. The BPE training process can be represented by Table 3.1:（Chapter3-Fundamentals-of-Large-Language-Models.md#217）
- 我们直接向模型下达指令：要求它完成情感分类任务。（第三章 大语言模型基础.md#173）
- 我们先给模型一个完整的“问题-答案”对作为示范：然后提出我们的新问题。（第三章 大语言模型基础.md#176）
- 我们提供涵盖了不同情况的多个示例：让模型对任务有更全面的理解。（第三章 大语言模型基础.md#181）
- Messages = [（Chapter4-Building-Classic-Agent-Paradigms.md#28）
- 中的`ask_question()`方法同时使用了RAG检索和记忆检索。请分析：在什么情况下应该优先使用RAG？在什么情况下应该优先使用Memory？如何设计一个"智能路由"机制来自动选择最合适的检索方式？（第八章 记忆与检索.md#443）
- 中使用了"分层上下文管理"策略：即时访问（TerminalTool）+ 会话记忆（MemoryTool）+ 持久笔记（NoteTool）。请分析：这三层之间应该如何协调？什么信息应该放在哪一层？如何避免信息冗余和不一致？（第九章 上下文工程.md#650）
- s：**（Chapter13-Intelligent-Travel-Assistant.md#138）
- **（第十三章 智能旅行助手.md#138）
- output:（Chapter14-Automated-Deep-Research-Agent.md#136）
- **:（Chapter14-Automated-Deep-Research-Agent.md#312）
- 'progress':（Chapter14-Automated-Deep-Research-Agent.md#476）
- 'plan':（Chapter14-Automated-Deep-Research-Agent.md#477）
- 'task_summary':（Chapter14-Automated-Deep-Research-Agent.md#478）
- 'report':（Chapter14-Automated-Deep-Research-Agent.md#479）
- 'error':（Chapter14-Automated-Deep-Research-Agent.md#480）
- 'completed':（Chapter14-Automated-Deep-Research-Agent.md#481）
- 输出：（第十四章 自动化深度研究智能体.md#136）
- s:（Chapter16-Graduation-Project.md#202）

## 边界与风险

- ed Learning Ability：Cannot learn and improve from past successes or failures（Chapter8-Memory-and-Retrieval.md#13）
- int = 5,（Chapter8-Memory-and-Retrieval.md#105）
- =limit,（Chapter8-Memory-and-Retrieval.md#106）
- =3（Chapter8-Memory-and-Retrieval.md#115）
- ed capacity (default 50 items) + TTL automatic cleanup（Chapter8-Memory-and-Retrieval.md#152）
- =max(limit * 5, 20),（Chapter8-Memory-and-Retrieval.md#223）
- =3,（Chapter8-Memory-and-Retrieval.md#258）
- =per,（Chapter8-Memory-and-Retrieval.md#337）
- =5,（Chapter8-Memory-and-Retrieval.md#394）
- =limit（Chapter8-Memory-and-Retrieval.md#408）
- int = 10,（Chapter9-Context-Engineering.md#284）
- Return quantity limit（Chapter9-Context-Engineering.md#285）
- int = 20（Chapter9-Context-Engineering.md#294）
- number of notes to avoid context overload（Chapter9-Context-Engineering.md#371）
- the size of command output to prevent memory overflow:（Chapter9-Context-Engineering.md#414）
- Low, just database migration（Chapter9-Context-Engineering.md#610）
- Medium, affects multiple service classes（Chapter9-Context-Engineering.md#611）
- High, core business logic（Chapter9-Context-Engineering.md#612）
- 返回数量限制（第九章 上下文工程.md#285）
- 笔记数量：避免上下文过载（第九章 上下文工程.md#371）
- 命令输出的大小：防止内存溢出：（第九章 上下文工程.md#414）
- 低,只是数据库迁移（第九章 上下文工程.md#610）
- 中,影响多个服务类（第九章 上下文工程.md#611）
- 高,核心业务逻辑（第九章 上下文工程.md#612）
- 需要设置环境变量（第十章 智能体通信协议.md#154）
- 这里使用了`List[Attraction]`来表示景点列表：`default_factory=list`表示默认值是一个空列表。（第十三章 智能旅行助手.md#97）
- 必须按顺序执行,每个工具只能调用一次,输出必须是JSON格式...（第十三章 智能旅行助手.md#123）
- 本文档中部分示例使用 `npx` 启动 MCP（Model Context Protocol）服务。而在本节代码仓中：我们实际采用的是 `uvx` 方式。需要说明的是，`npx` 和 `uvx` 在设计理念上高度一致，区别仅在于所处的生态系统，`npx` 面向 JavaScript/Node.js（包来自 npm），而`uvx` 面向 Python（包来自 PyPI）。两种方式并无优劣之分，请大家在使用时按需进行选择。（第十三章 智能旅行助手.md#191）
- 我们没有把 Unsplash 封装成 Tool 或 MCP 工具：而是直接在 API 路由中调用。这是因为图片搜索不需要 Agent 的智能决策，只是一个简单的数据增强步骤。如果你想让 Agent 能够自主决定是否需要图片，或者选择不同的图片来源，可以考虑把它封装成 Tool。（第十三章 智能旅行助手.md#236）
- 这里使用了`Location`类型作为字段类型：这就是嵌套类型。问号`?`表示可选字段，对应后端 Pydantic 模型中的`Optional`。（第十三章 智能旅行助手.md#253）
- 这个函数的类型签名：参数是`TripPlanRequest`类型，返回值是`Promise<TripPlan>`类型。这意味着 TypeScript 会检查调用者传递的参数是否符合要求，也会检查返回值的使用是否正确。（第十三章 智能旅行助手.md#269）
- v-model：value`指令，它实现了双向数据绑定。当用户在输入框中输入内容时，`formData.city`会自动更新。当`formData.city`的值改变时，输入框的内容也会自动更新。（第十三章 智能旅行助手.md#288）
- v-if="tripPlan.budget"`这个条件渲染。因为预算信息是可选的(在 Pydantic 模型中定义为`Optional[Budget]`)：如果 LLM 没有生成预算信息，这个卡片就不会显示。这体现了前端对数据的容错处理。（第十三章 智能旅行助手.md#315）
- 这里使用了`JSON.parse(JSON.stringify(...))`来深拷贝对象。为什么不直接赋值？因为 JavaScript 中对象是引用类型：如果直接赋值，`originalPlan`和`tripPlan`会指向同一个对象，修改一个会影响另一个。深拷贝可以创建一个完全独立的副本。（第十三章 智能旅行助手.md#328）
- ed_sources = []（Chapter14-Automated-Deep-Research-Agent.md#394）
- ed_sources.append({（Chapter14-Automated-Deep-Research-Agent.md#398）

## 练习与行动

- **: After decision-making is complete, the agent executes specific actions through its actuators. This typically manifests as calling a selected tool (such as a code interpreter or search engine API), thereby influencing the environment with the intent to change its state.（Chapter1-Introduction-to-Agents.md#74）
- is not the end of the loop. The agent's action causes a **state change** in the **environment**, which then produces a new **observation** as result feedback. This new observation is captured by the agent's perception system in the next round of the loop, forming a continuous "perceive-think-act-observe" closed loop. It is through continuously repeating this loop that the agent gradually advances the task, evolving from the initial state toward the goal state.（Chapter1-Introduction-to-Agents.md#75）
- **: This is the specific operation the agent decides to impose on the environment based on its thinking, typically expressed as a function call.（Chapter1-Introduction-to-Agents.md#80）
- get_weather("Beijing")（Chapter1-Introduction-to-Agents.md#82）
- [The specific action you want to execute]（Chapter1-Introduction-to-Agents.md#100）
- format must be one of the following:（Chapter1-Introduction-to-Agents.md#101）
- must be on the same line, do not break lines（Chapter1-Introduction-to-Agents.md#102）
- _match = re.search(r"Action：(.*)", llm_output, re.DOTALL)（Chapter1-Introduction-to-Agents.md#142）
- _str = action_match.group(1).strip()（Chapter1-Introduction-to-Agents.md#142）
- get_weather(city="Beijing")（Chapter1-Introduction-to-Agents.md#151）
- get_attraction(city="Beijing", weather="Sunny")（Chapter1-Introduction-to-Agents.md#153）
- Finish[Today's weather in Beijing is sunny with a temperature of 26 degrees Celsius, very suitable for outdoor activities. I recommend you visit the Summer Palace to enjoy the beautiful lake views and ancient architecture, or go to the Great Wall to experience its spectacular scenery and profound historical significance. Hope you have a pleasant trip!]（Chapter1-Introduction-to-Agents.md#155）
- completed, final answer：Today's weather in Beijing is sunny with a temperature of 26 degrees Celsius, very suitable for outdoor activities. I recommend you visit the Summer Palace to enjoy the beautiful lake views and ancient architecture, or go to the Great Wall to experience its spectacular scenery and profound historical significance. Hope you have a pleasant trip!（Chapter1-Introduction-to-Agents.md#156）
- 并非循环的终点。智能体的行动会引起<strong>环境 (Environment)</strong> 的<strong>状态变化 (State Change)<：环境随即会产生一个新的<strong>观察 (Observation)</strong> 作为结果反馈。这个新的观察又会在下一轮循环中被智能体的感知系统捕获，形成一个持续的“感知-思考-行动-观察”的闭环。智能体正是通过不断重复这一循环，逐步推进任务，从初始状态向目标状态演进。（第一章 初识智能体.md#75）
- get_weather("北京")（第一章 初识智能体.md#82）
- 执行后：环境会返回一个结果。例如，`get_weather`函数可能返回一个包含详细天气数据的 JSON 对象。然而，原始的机器可读数据（如 JSON）通常包含 LLM 无需关注的冗余信息，且格式不符合其自然语言处理的习惯。（第一章 初识智能体.md#84）
- [你要执行的具体行动]（第一章 初识智能体.md#100）
- 的格式必须是以下之一：（第一章 初识智能体.md#101）
- 必须在同一行：不要换行（第一章 初识智能体.md#102）
- get_weather(city="北京")（第一章 初识智能体.md#151）
- get_attraction(city="北京", weather="Sunny")（第一章 初识智能体.md#153）
- Finish[今天北京的天气是晴朗的：气温26摄氏度，非常适合外出游玩。我推荐您去颐和园欣赏美丽的湖景和古建筑，或者前往长城体验其壮观的景观和深厚的历史意义。希望您有一个愉快的旅行！]（第一章 初识智能体.md#155）
- 完成，最终答案：今天北京的天气是晴朗的，气温26摄氏度，非常适合外出游玩。我推荐您去颐和园欣赏美丽的湖景和古建筑，或者前往长城体验其壮观的景观和深厚的历史意义。希望您有一个愉快的旅行！（第一章 初识智能体.md#156）
- (A)：Operations the agent can take based on the current state. For example, placing a stone at a legal position on the board.（Chapter2-History-of-Agents.md#111）
- **: After decision-making is complete, the action stage begins, managed by the **Execution Module**. Tool call instructions generated by the LLM are sent to the execution module. This module parses instructions, selects and calls appropriate tools from the **Tool Use** toolbox (such as code executors, search engines, APIs, etc.) to interact with the environment or execute tasks. This actual interaction with the environment is the agent's **Action**.（Chapter2-History-of-Agents.md#133）
- (Acting)：** This is the specific action the agent decides to take, usually calling an external tool, such as `Search['Huawei's latest phone']`.（Chapter4-Building-Classic-Agent-Paradigms.md#37）
- s requiring external knowledge：Such as querying real-time information (weather, news, stock prices), searching for knowledge in professional domains, etc.（Chapter4-Building-Classic-Agent-Paradigms.md#46）
- s requiring precise calculations：Delegating mathematical problems to calculator tools to avoid LLM calculation errors.（Chapter4-Building-Classic-Agent-Paradigms.md#46）
- s requiring API interaction：Such as operating databases, calling a service's API to complete specific functions.（Chapter4-Building-Classic-Agent-Paradigms.md#46）
- The action you decide to take, must be in one of the following formats:（Chapter4-Building-Classic-Agent-Paradigms.md#96）
- _match = re.search(r"Action：\s*(.*?)$", text, re.DOTALL)（Chapter4-Building-Classic-Agent-Paradigms.md#113）
- = action_match.group(1).strip() if action_match else None（Chapter4-Building-Classic-Agent-Paradigms.md#113）
- Search[Huawei latest phone model and main selling points]（Chapter4-Building-Classic-Agent-Paradigms.md#136）
- Finish[According to the latest information, Huawei's latest phones may be HUAWEI Pura 80 Pro+ or HUAWEI Mate 70. Among them, HUAWEI Mate 70's main selling points include top-level photography configuration, full focal length coverage, suitable for professional photography, excellent workmanship, and good outdoor drop resistance. While HUAWEI Pura 80 Pro+ emphasizes pioneer imaging technology.]（Chapter4-Building-Classic-Agent-Paradigms.md#139）
- Description：Clearly defines the goal of "decomposing problems."（Chapter4-Building-Classic-Agent-Paradigms.md#177）
- Completed ---（Chapter4-Building-Classic-Agent-Paradigms.md#223）
- =task,（Chapter4-Building-Classic-Agent-Paradigms.md#280）
- Write a Python function to find all prime numbers between 1 and n.（Chapter4-Building-Classic-Agent-Paradigms.md#286）
- 你决定采取的行动：必须是以下格式之一:（第四章 智能体经典范式构建.md#96）
- Search[华为最新手机型号及主要卖点]（第四章 智能体经典范式构建.md#136）
- Finish[根据最新信息：华为的最新手机可能是HUAWEI Pura 80 Pro+或HUAWEI Mate 70。其中，HUAWEI Mate 70的主要卖点包括顶级的拍照配置，全焦段覆盖，适合专业摄影，做工出色，并且具有良好的户外抗摔性能。而HUAWEI Pura 80 Pro+则强调了先锋影像技术。]（第四章 智能体经典范式构建.md#139）
- 完成 ---（第四章 智能体经典范式构建.md#223）
- 编写一个Python函数：找出1到n之间所有的素数 (prime numbers)。（第四章 智能体经典范式构建.md#286）
- Choose an action, the format must be one of the following:（Chapter7-Building-Your-Agent-Framework.md#251）
- {task}（Chapter7-Building-Your-Agent-Framework.md#277）
- s = [（Chapter7-Building-Your-Agent-Framework.md#502）
- 选择一个行动：格式必须是以下之一:（第七章 构建你的Agent框架.md#251）
- _notes = self.note_tool.run({（Chapter9-Context-Engineering.md#534）
- = proposal.get("task")（Chapter10-Agent-Communication-Protocols.md#389）
- = match.group(1).strip()（Chapter10-Agent-Communication-Protocols.md#393）
- List：Shows all subtasks and their status（Chapter14-Automated-Deep-Research-Agent.md#52）
- s_payload = self._extract_tasks(response)（Chapter14-Automated-Deep-Research-Agent.md#143）
- = TodoItem(（Chapter14-Automated-Deep-Research-Agent.md#144）
- _summarizer_instructions = """（Chapter14-Automated-Deep-Research-Agent.md#151）
- {task_title}（Chapter14-Automated-Deep-Research-Agent.md#152）
- {task_intent}（Chapter14-Automated-Deep-Research-Agent.md#152）
- TodoItem,（Chapter14-Automated-Deep-Research-Agent.md#165）
- _title=task.title,（Chapter14-Automated-Deep-Research-Agent.md#166）
- _intent=task.intent,（Chapter14-Automated-Deep-Research-Agent.md#166）
- _query=task.query,（Chapter14-Automated-Deep-Research-Agent.md#166）
- _summaries：List[Tuple[TodoItem, str]]（Chapter14-Automated-Deep-Research-Agent.md#194）
- _summaries=formatted_summaries,（Chapter14-Automated-Deep-Research-Agent.md#195）
- _summaries = []（Chapter14-Automated-Deep-Research-Agent.md#226）
- _summaries.append((task, summary))（Chapter14-Automated-Deep-Research-Agent.md#228）
- s1 = service._extract_tasks(response1)（Chapter14-Automated-Deep-Research-Agent.md#316）
- s2 = service._extract_tasks(response2)（Chapter14-Automated-Deep-Research-Agent.md#318）
- Task information（Chapter14-Automated-Deep-Research-Agent.md#340）
- _summaries：List[Tuple[TodoItem, str, List[str]]]（Chapter14-Automated-Deep-Research-Agent.md#363）
- _summaries：Subtask summary list, each element is (task, summary, source URL list)（Chapter14-Automated-Deep-Research-Agent.md#364）
- serial number（Chapter14-Automated-Deep-Research-Agent.md#370）
- title（Chapter14-Automated-Deep-Research-Agent.md#370）
- intent（Chapter14-Automated-Deep-Research-Agent.md#370）
- _summaries.append((task, summary, source_urls))（Chapter14-Automated-Deep-Research-Agent.md#462）
- Summarizer (Task Summarization Expert)：Responsible for summarizing search results for each subtask（Chapter14-Automated-Deep-Research-Agent.md#508）
- 总结 Agent 会从每个搜索结果中提取核心观点：合并相似信息，保留重要的数字、日期、名称等关键数据，并为每个观点添加来源引用。例如，对于"Datawhale 的基本信息"的搜索结果，总结 Agent 可能生成：（第十四章 自动化深度研究智能体.md#92）
- 标题：{task_title}（第十四章 自动化深度研究智能体.md#152）
- 意图：{task_intent}（第十四章 自动化深度研究智能体.md#152）
- 任务信息（第十四章 自动化深度研究智能体.md#340）
- _summaries：子任务总结列表，每个元素是(任务, 总结, 来源URL列表)（第十四章 自动化深度研究智能体.md#364）
- 序号（第十四章 自动化深度研究智能体.md#370）

## 待确认问题

- {question}（Chapter4-Building-Classic-Agent-Paradigms.md#97）
- =question,（Chapter4-Building-Classic-Agent-Paradigms.md#105）
- A fruit store sold 15 apples on Monday. The number of apples sold on Tuesday was twice that of Monday. The number sold on Wednesday was 5 fewer than Tuesday. How many apples were sold in total over these three days?（Chapter4-Building-Classic-Agent-Paradigms.md#217）
- 一个水果店周一卖出了15个苹果：周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？（第四章 智能体经典范式构建.md#217）
- ** {question}（Chapter7-Building-Your-Agent-Framework.md#253）
- =input_text,（Chapter7-Building-Your-Agent-Framework.md#267）
- = "A fruit store sold 15 apples on Monday. The number of apples sold on Tuesday was twice that of Monday. The number sold on Wednesday was 5 less than Tuesday. How many apples were sold in total over these three days?"（Chapter7-Building-Your-Agent-Framework.md#308）
- = "一个水果店周一卖出了15个苹果：周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？"（第七章 构建你的Agent框架.md#308）
- User question（Chapter8-Memory-and-Retrieval.md#391）
- 用户问题（第八章 记忆与检索.md#383）
- ⚠️ 缺少索引,email 字段未设置唯一约束（第九章 上下文工程.md#584）
- ✅ 设计合理（第九章 上下文工程.md#585）
- ⚠️ 缺少创建时间字段,不利于数据分析（第九章 上下文工程.md#586）
- = match.group(1).strip() if match else text（Chapter10-Agent-Communication-Protocols.md#373）
- {problem_a}（第十二章 智能体性能评估.md#590）
- {problem_b}（第十二章 智能体性能评估.md#591）
- 表述的清晰度（第十二章 智能体性能评估.md#592）
