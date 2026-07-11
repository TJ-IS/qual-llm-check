# 重新评估 workspace awareness 与其他基础概念：以 coding agent 独特问题为中心

> 状态更新：本文件是 38 号中间判断，已经被 39 号 Scopus 精确短语检索与定义审计修正。39 号文档显示，`workspace awareness` 在最新 Scopus 文献中大量用于 hybrid work、social presence / connectedness、AR/VR/robotics shared workspace 等语境，因此不应继续作为唯一基础概念的首选。当前更稳妥的主线是以 `situation awareness` 为基础，开发 `coding-agent task-state awareness / 编码代理任务状态觉察`。

## 1. 这次修正的出发点

前面 36 号文档因为 `workspace awareness` 在 Top11 IS database 和外部文献中的使用规模不如 `situation awareness`，把它降为相邻文献。这个判断需要修正。

如果我们的目标是开发一个 **coding-agent-specific UX concept**，那么核心标准不应是“哪个概念文献最多”，而应是：

1. 它是否直接描述 coding agent 使用中的重要现实问题；
2. 它是否在 coding agent 情境中出现传统概念不能直接照搬的断裂；
3. 它是否可以落到 individual / task level 的清晰测量；
4. 它是否能解释用户为什么愿意或不愿意使用 coding agent，以及如何改进工具设计。

按这个标准，`workspace awareness` 必须重新进入最核心候选，甚至可能比 `situation awareness` 更贴近我们从 Reddit 和现实使用中观察到的痛点。

## 2. workspace awareness 现在怎么看

经典 `workspace awareness` 关心的是：人在共享工作空间中，是否理解他人正在如何与共享对象互动，例如谁在做什么、在哪里做、改了什么、什么时候做、意图是什么，以及这些行动如何影响共同工作。

这和 coding agent 的痛点高度贴合：

- 用户不是只想知道 agent “可信不可信”，而是想知道 agent 正在代码库里做什么；
- 用户不是只想知道最终结果，而是想知道它改了哪些文件、运行了哪些命令、产生了哪些测试结果；
- 用户不是只想要解释，而是需要把 agent 行动与代码工作空间中的真实状态变化对应起来；
- 用户审批下一步时，需要理解当前 shared code workspace 已经发生了什么、下一步会发生什么。

因此，`workspace awareness` 的重要性不是来自“它在 IS database 里出现了多少次”，而是来自它精准击中了 coding agent 的共享工作空间问题。

## 3. 为什么不能直接照搬 workspace awareness

`workspace awareness` 不能直接照搬到 coding agent，原因不是“换了个情境”，而是原概念的几个前提发生了变化。

| 传统 workspace awareness 前提 | coding agent 中的断裂 |
| --- | --- |
| 行动者通常是人类协作者 | 行动者是会自主规划、调用工具、改代码、生成解释的 agent |
| 共享空间多是可视化或协作编辑空间 | 共享空间是代码库、terminal、diff、test、dependency、issue context 组成的技术工作空间 |
| 他人行动通常可通过 presence、cursor、object manipulation 被观察 | agent 的关键行动常常隐藏在搜索、命令执行、patch 生成、上下文推理和工具调用里 |
| 了解“谁在哪里做什么”通常已能支持协调 | coding agent 中还必须理解改动的代码语义、风险、约束和下一步影响 |
| 协作者的意图可通过社会线索和对话修正 | agent 的“意图”更多体现为 plan、tool trace、diff rationale、approval request，需要重新设计呈现方式 |

所以迁移的必要性很明确：传统 workspace awareness 关注 **human collaborator 与 shared workspace 的互动觉察**；我们要开发的是 **human user 对 autonomous coding agent 与 code workspace 互动的觉察**。

## 4. 如果以 workspace awareness 为唯一基础概念，新构念可以是什么

候选名：

> **Coding-agent workspace awareness**  
> 中文暂定：**编码代理工作空间觉察**

定义草案：

> 编码代理工作空间觉察是指，用户在与 coding agent 共同完成编程任务时，对 agent 如何与共享代码工作空间互动所形成的可操作理解程度。这种理解包括用户能否识别 agent 当前和刚刚执行的编程行动、这些行动影响了哪些代码对象和工具状态、这些变化对当前任务和约束意味着什么，以及批准或继续下一步可能使工作空间发生何种变化。

这个定义的高低程度是清楚的：

- 高觉察：用户能说清楚 agent 做了什么、改了哪里、为什么这些变化重要、哪些风险还没验证、下一步批准会影响什么；
- 低觉察：用户只能看到零散输出或最终摘要，难以把 agent 的行动、diff、命令、测试和任务目标连起来，只能机械审批、反复检查或干脆接管。

## 5. 这个概念为什么具有现实价值

这个概念能直接解释几类 coding agent 实际使用问题：

1. **CLI agent 不好用的一个核心原因**：用户难以持续看到 agent 与代码库互动的状态，只能在日志、diff、approval prompt 之间来回切换。
2. **审批疲劳**：频繁审批本身不是唯一问题；更关键的是每次审批时用户缺少足够的 workspace awareness，不知道这一步放行后会改变什么。
3. **过度信任或过度不信任**：用户不一定是“不信任 AI”，而是无法形成对 agent 工作状态的判断，只好盲信或全部重查。
4. **控制感下降**：控制感不是核心构念本身，而是低 workspace awareness 的重要后果；用户看不清 agent 如何改变工作空间，就更难感到自己能有效监督和介入。
5. **验证负担上升**：当 agent 行动痕迹与代码状态变化无法被快速理解，用户需要额外花时间重建发生了什么。

因此，它比“可读性”“透明度”“信任”“控制感”更接近 coding agent 的专属问题：用户需要和一个会实际改变代码工作空间的 agent 协作，而不是仅仅消费一个 AI 输出。

## 6. 和 situation awareness 的关系

`situation awareness` 的优势是定义和测量非常成熟，尤其是 perception、comprehension、projection 三层结构。但它的问题是太通用：飞行员、驾驶员、网络安全分析师、dashboard 使用者都可以有 situation awareness。

如果我们以 `situation awareness` 为唯一基础概念，必须额外努力说明为什么 coding agent 是特殊情境。

如果我们以 `workspace awareness` 为唯一基础概念，coding agent 的特殊性更自然：

> coding agent 的核心不是一般动态情境，而是 agent 在 shared code workspace 中持续产生可执行、可合并、可破坏的工作空间变化。

因此，当前修正后的判断是：

- 若目标是 **文献稳健性和测量传统**，`situation awareness` 更稳；
- 若目标是 **coding agent 独特性和现实痛点解释力**，`workspace awareness` 更贴切；
- 我们当前研究更强调后者，因此 `workspace awareness` 应该作为最强候选之一，甚至可以重新成为唯一基础概念。

## 7. 其他候选概念的比较

| 候选基础概念 | 能抓住什么 | 为什么不如 workspace awareness 适合作为主基础 |
| --- | --- | --- |
| situation awareness | 动态任务中的感知、理解、预测 | 很可测，但太通用；coding agent 独特性需要额外论证 |
| mutual understanding | 用户与协作者之间理解是否对齐 | 容易滑向“agent 是否理解用户”或双边心智对齐，不直接抓代码工作空间变化 |
| common ground | prompt、上下文、约束是否被双方纳入共同基础 | 适合解释对话和 grounding，但不够覆盖 agent 改代码、跑命令、产生日志和 diff 的工作空间痕迹 |
| transactive memory system | 用户是否知道 agent 擅长什么、自己该负责什么 | 适合解释任务分配和能力认知，但不是当前代码状态觉察 |
| shared mental model | 用户和 agent 对任务/流程是否有相似模型 | 人-agent 心智相似性难以定义和测量，且更像团队层或 dyadic congruence |
| transparency | 系统是否暴露信息 | 是设计属性，不是用户形成的认知状态 |
| explainability | 系统是否给出解释 | 是形成觉察的机制之一，不是觉察本身 |
| perceived control | 用户是否感到能影响过程和结果 | 更像后果；低 workspace awareness 会削弱控制感 |
| cognitive load / overload | 用户处理信息的负担 | 是使用成本或后果，不能直接说明用户缺失了哪种 coding-agent-specific 理解 |

## 8. 当前建议

我现在会把两个候选重新排序为：

1. **首选候选：workspace awareness → coding-agent workspace awareness**
2. **备选候选：situation awareness → coding-agent work-situation awareness**

更具体地说，如果我们想写出一个真正能让读者一眼看出 coding agent 独特性的构念，我更倾向于：

> 基础概念：workspace awareness  
> 新构念：coding-agent workspace awareness / 编码代理工作空间觉察

它的迁移逻辑比前一个版本更强：

> 从 human-human shared workspace 中的协作者行动觉察，迁移到 human-agent shared code workspace 中的 agentic action-state awareness。

这里的 `agentic` 不是装饰词，而是指 agent 会自主规划、调用工具、改动代码、请求审批，并使工作空间状态连续变化。用户体验问题也正发生在这里。

## 9. 下一步需要补强的证据

如果我们决定把 `workspace awareness` 重新作为唯一基础概念，下一步应补三类证据：

1. 精读 Gutwin and Greenberg 的 workspace awareness 框架，摘出原始定义、knowledge elements 和测量/实验方式；
2. 阅读 Dourish and Bellotti 的 shared workspace awareness 与 coordination 原文，明确 awareness 与 coordination 的关系；
3. 从 Reddit coding agent 评论中找自然语言证据，证明用户抱怨集中在 agent action trace、diff visibility、approval context、tool execution visibility、workspace state reconstruction 这些问题上。

这样我们就能把概念开发的叙事写成：

> 经典 workspace awareness 解释了协作系统中用户如何理解他人与共享工作空间的互动；但 coding agent 把“他人行动”变成了自主的、工具介导的、语义性的代码工作空间变更，因此需要开发 coding-agent workspace awareness 来描述用户能否对这种 agent-mediated workspace change 形成可操作理解。
