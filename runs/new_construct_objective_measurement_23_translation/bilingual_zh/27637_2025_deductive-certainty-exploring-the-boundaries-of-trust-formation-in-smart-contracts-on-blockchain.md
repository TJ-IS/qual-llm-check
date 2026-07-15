---
otero_id: 27637
otero_key: "PHUJTSS5"
title: "Deductive Certainty? Exploring the Boundaries of Trust Formation in Smart Contracts on Blockchains"
authors: "Daniel Obermeier; Joachim Henkel"
year: "2025"
journal: "MIS Quarterly"
doi: "10.25300/misq/2025/18501"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# DEDUCTIVE CERTAINTY? EXPLORING THE BOUNDARIES OF TRUST FORMATION IN SMART CONTRACTS ON BLOCKCHAINS<sup>1</sup>




---
奥特罗_id：27637
otero_key: "PHUJTSS5"
标题：“演绎确定性？探索区块链智能合约中信任形成的边界”
作者：“丹尼尔·奥伯迈尔；约阿希姆·汉克尔”
年份：“2025”
期刊：《管理信息系统季刊》
doi：“10.25300/misq/2025/18501”
查询：“构造”
来源：“https://ais.kexu.win”
图片下载：假
---
# 演绎确定性？探索区块链上智能合约中信任形成的边界<sup>1</sup>


Daniel Obermeier




丹尼尔·奥伯迈尔


Nova School of Business and Economics, Universidade NOVA de Lisboa, Campus de Carcavelos Carcavelos, PORTUGAL {daniel.obermeier@novasbe.pt}




新葡京大学商业与经济学院，卡卡维洛斯校园 卡卡维洛斯，葡萄牙 {daniel.obermeier@novasbe.pt}


Joachim Henkel TUM School of Management, Technical University of Munich, Munich, GERMANY {joachim.henkel@tum.de}




Joachim Henkel TUM 管理学院，慕尼黑工业大学，德国慕尼黑 {joachim.henkel@tum.de}


We offer a new perspective on trust formation in smart contracts on blockchain that is based on deduction rather than induction. This shift in perspective allows us to explore the boundaries of trust in IT systems, analyze the conditions under which trust becomes dispensable, and unpack the sociotechnical complexity of supposedly “trust-free” systems. Through this approach, we introduce three key concepts: deductive certainty, a state in which an individual has full knowledge of the other party’s future behavior based on deduction; the possibility of deductive certainty that an IT system may provide; and deduction-related trust, a new type of trust rooted in the possibility of deductive certainty. We use these concepts to analyze smart contracts on a blockchain as a technology that offers the potential for deductive certainty by enabling complete deduction. Our analysis reveals the conditions under which smart contract-based applications, also known as dApps, can become “trust-free” and why, in practice, they often are not. Based on a sample of 536 dApps and a user survey, we provide evidence supporting our theoretical claims. Our findings suggest that the possibility of deductive certainty plays a significant role in forming initial trust in dApps. However, we also find that new users rely on both deduction-related trust and classical inductive trust, with the two sources of trust reinforcing each other.




我们提供了基于演绎而不是归纳的区块链智能合约信任形成的新视角。这种视角的转变使我们能够探索 IT 系统中信任的边界，分析信任变得可有可无的条件，并揭示所谓“无信任”系统的社会技术复杂性。通过这种方法，我们引入了三个关键概念：演绎确定性，个体根据演绎充分了解对方未来行为的状态； IT 系统可能提供演绎确定性的可能性；演绎相关信任，一种植根于演绎确定性可能性的新型信任。我们使用这些概念来分析区块链上的智能合约，作为一种通过实现完全演绎来提供演绎确定性潜力的技术。我们的分析揭示了基于智能合约的应用程序（也称为 dApp）可以成为“免信任”的条件，以及为什么在实践中它们往往并非如此。基于 536 个 dApp 的样本和用户调查，我们提供了支持我们理论主张的证据。我们的研究结果表明，演绎确定性的可能性在形成对 dApp 的初始信任方面发挥着重要作用。然而，我们也发现新用户同时依赖演绎相关信任和经典归纳信任，这两种信任来源相互增强。


Keywords: Blockchain; smart contracts, decentralized applications, transactions, trust formation




关键词：区块链；智能合约、去中心化应用、交易、信任形成


## Introduction




＃＃ 介绍


Across various research disciplines, trust is widely acknowledged as a crucial precondition for all forms of organizational and interpersonal economic exchange (Fukuyama, 1995; Gefen et al., 2008; Rousseau et al., 1998; Zaheer & Venkatraman, 1995). With the proliferation of IT, IS scholars, in particular, have turned their attention to the consequences of trust and technology’s role in establishing and maintaining trusting relationships (e.g., Ba & Pavlou, 2002; Beldad et al., 2010; Gefen et al., 2003; McKnight et al., 2002a; Pavlou & Gefen, 2004). For instance, Gefen et al. (2003, p. 51) established that “trust is as important to online commerce as the widely accepted TAM useantecedents” and that technical features like a website’s usability or safety mechanisms built into it can influence trust. Pavlou and Gefen (2004) showed that IT-enabled systems like feedback mechanisms or escrow services engender consumer trust in online vendors and lead to more exchange on online marketplaces. Fang et al. (2014) found that the perceived effectiveness of such IT-enabled safeguards moderates the relationship between trust and online repurchase behavior.




在各个研究学科中，信任被广泛认为是所有形式的组织和人际经济交换的关键先决条件（Fukuyama，1995；Gefen 等，2008；Rousseau 等，1998；Zaheer 和 Venkatraman，1995）。随着信息技术的普及，信息系统学者尤其将注意力转向信任和技术在建立和维持信任关系中的作用的后果（例如，Ba & Pavlou，2002；Beldad 等，2010；Gefen 等，2003；McKnight 等，2002a；Pavlou 和 Gefen，2004）。例如，格芬等人。 （2003 年，第 51 页）指出“信任对于在线商务来说与广泛接受的 TAM 使用前提一样重要”，并且网站的可用性或内置安全机制等技术特征可以影响信任。 Pavlou 和 Gefen (2004) 表明，反馈机制或托管服务等 IT 支持系统可以增强消费者对在线供应商的信任，并导致在线市场上的更多交易。方等人。 (2014) 发现，这种 IT 支持的保障措施的感知有效性调节了信任与在线回购行为之间的关系。


Although this literature has contributed significantly to a better understanding of how IT can foster exchange by enhancing trust, it has been criticized for lacking focus on the relationship between trust and the IT artifact itself (Gefen et al., 2008). Existing research either follows the “computers are social actors” paradigm (Orlikowski & Iacono, 2001) and adapts trust concepts from the interpersonal domain (e.g., McKnight et al., 2011; Wingreen et al., 2019) or treats trust in the technology as part of the institutional surrounding injecting trust into the relationship with humans but does not treat the artifact as a trust object in its own right (e.g., Ba & Pavlou, 2002; Chawla, 2020; Pavlou & Gefen, 2004; Ratnasingam & Pavlou, 2003).




尽管这些文献对于更好地理解 IT 如何通过增强信任来促进交流做出了重大贡献，但它仍因缺乏对信任与 IT 工件本身之间关系的关注而受到批评（Gefen 等，2008）。现有的研究要么遵循“计算机是社会参与者”范式（Orlikowski & Iacono，2001），并改编人际领域的信任概念（例如，McKnight 等人，2011；Wingreen 等人，2019），要么将对技术的信任视为将信任注入与人类关系的制度的一部分，但不将人工制品本身视为信任对象（例如，Ba &帕夫卢，2002；查瓦拉，2020；拉特纳辛加姆和帕夫卢，2003；


We argue this perspective limits our understanding of trust in IT systems, as it neglects one of their key features: In contrast to the humans developing them, who are boundedly rational (Simon, 1957) and “self-interest seeking with guile” (Williamson, 1985, p. 47), computers are confined by the deterministic physical laws of their parts (Mytkowicz et al., 2009). Therefore, they require logical instructions to translate clearly defined inputs into prespecified outputs. As a result, it is easier to predict their actions and, depending on the effort one is willing to invest, even certainty about the outcome of an interaction can be attained. Based on this inherent difference, we propose a new perspective on trust formation in IT systems. Our perspective draws from epistemology and is inspired by Simmel’s (1930) notion of trust as weak inductive knowledge combined with some quasi-religious leap of faith. Building on this notion, we argue that prior trust formation literature has predominantly considered knowledge acquired through inductive processes as the basis for trust. While this perspective was largely sufficient in the past when most transactions still involved some form of not entirely predictable human execution, modern IT has gradually extended human interaction with agentic IS artifacts in the form of algorithms, allowing, in principle, the formation of conclusions about future outcomes through logical deduction. Recent advances in machine learning and AI have made such agents more powerful, but their behavior has also become increasingly difficult to understand. Our new perspective sheds light on the trust-related potential we risk losing if we obscure the deterministic nature of IT agents with extremely complex models and opaque training processes.




我们认为，这种观点限制了我们对 IT 系统信任的理解，因为它忽略了 IT 系统的一个关键特征：与开发 IT 系统的人类相比，人类是有限理性的（Simon，1957）和“狡诈的自利寻求”（Williamson，1985，第 47 页），计算机受到其部件的确定性物理定律的限制（Mytkowicz 等，2009）。因此，它们需要逻辑指令将明确定义的输入转换为预先指定的输出。因此，更容易预测他们的行为，并且根据人们愿意投入的努力，甚至可以获得交互结果的确定性。基于这种固有的差异，我们提出了 IT 系统中信任形成的新视角。我们的观点源自认识论，并受到齐美尔（Simmel，1930）的信任概念的启发，信任是弱归纳知识与某种准宗教信仰飞跃的结合。基于这一概念，我们认为，先前的信任形成文献主要认为通过归纳过程获得的知识是信任的基础。虽然这种观点在过去已经足够了，当时大多数交易仍然涉及某种形式的不完全可预测的人类执行，但现代 IT 已逐渐以算法的形式扩展了人类与智能 IS 工件的交互，原则上允许通过逻辑演绎形成关于未来结果的结论。机器学习和人工智能的最新进展使此类代理变得更加强大，但它们的行为也变得越来越难以理解。我们的新观点揭示了如果我们用极其复杂的模型和不透明的培训过程来掩盖 IT 代理的确定性本质，我们可能会失去与信任相关的潜力。


With our perspective, we introduce three novel concepts: deductive certainty, a status where trust (in the “core” of a system, see below) becomes dispensable because an individual has attained full knowledge of the other party’s future behavior based on deducing it from prespecified rules; the possibility of deductive certainty, a feature of an IT system that allows humans, in principle, to attain deductive certainty about the system’s reaction to a certain trigger; and deduction-related trust, a new type of trust originating from positive beliefs about the other party’s future behavior based on the possibility of deductive certainty through either a partial execution of the deductive process, its (full or partial) execution by a third party, or the mere apprehension of the possibility of deductive certainty. These concepts allow us to explore the boundaries of trust in IT systems, analyze under what conditions trust in the core<sup>2</sup> becomes dispensable, and unpack the sociotechnical complexity of supposedly “trustfree” or “trustless” systems by differentiating the possibility of deductive certainty as a technical feature from deductive certainty. This differentiation is crucial as it reveals that most users are not likely to attain deductive certainty, as a complete deductive process requires a great deal of effort and skills; among other things, the ability to understand (and translate to “human language”) a computer program’s source code. These concepts are also important in explaining how an IT artifact can create trust independently from its creator and can thus help researchers theorize the relationship between trust and the IT artifact, which is becoming more important in the age of IT agents.




根据我们的观点，我们引入了三个新颖的概念：演绎确定性，一种信任（在系统的“核心”中，见下文）变得可有可无的状态，因为个体通过从预先设定的规则中推断出对方的未来行为，从而获得了充分的知识；演绎确定性的可能性，IT系统的一个特征，原则上允许人类获得关于系统对特定触发的反应的演绎确定性；与演绎相关的信任，一种新型信任，源于对另一方未来行为的积极信念，这种信念基于通过部分执行演绎过程、由第三方（全部或部分）执行或仅仅对演绎确定性可能性的理解来实现演绎确定性的可能性。这些概念使我们能够探索 IT 系统中信任的边界，分析在什么条件下对核心<sup>2</sup>的信任变得可有可无，并通过区分演绎确定性作为技术特征的可能性与演绎确定性来揭示所谓“无信任”或“无信任”系统的社会技术复杂性。这种区分至关重要，因为它表明大多数用户不太可能获得演绎确定性，因为完整的演绎过程需要大量的努力和技能；除其他外，理解（并翻译成“人类语言”）计算机程序源代码的能力。这些概念对于解释 IT 工件如何独立于其创建者创建信任也很重要，从而可以帮助研究人员对信任与 IT 工件之间的关系进行理论化，这在 IT 代理时代变得更加重要。


To introduce these concepts, we first review the existing trust literature and explain why it has treated trust formation predominantly as an inductive process. Next, we discuss legal contracts and open source software as potential candidates that allow deducing a transaction’s outcome to some degree. We then introduce smart contracts on a blockchain as a new technology that offers the possibility of deductive certainty by allowing full deduction in conjunction with immutability and automated execution provided by the blockchain platform it runs on.




为了介绍这些概念，我们首先回顾现有的信任文献，并解释为什么它主要将信任形成视为归纳过程。接下来，我们讨论法律合同和开源软件作为潜在的候选者，它们允许在某种程度上推断交易的结果。然后，我们在区块链上引入智能合约作为一项新技术，通过允许完全演绎以及其运行的区块链平台提供的不变性和自动执行来提供演绎确定性的可能性。


Based on our new perspective, we hypothesize that the possibility of deductive certainty offered by a smart contractbased application (also called decentralized application or dApp) leads to increased usage of the application by enabling the formation of deduction-related trust. We further hypothesize that traditional induction-related trust cues remain relevant and equally lead to increased usage of the application. Finally, we hypothesize that the transaction risk and the cost of the deductive process moderate these direct effects.




基于我们的新视角，我们假设基于智能合约的应用程序（也称为去中心化应用程序或 dApp）提供演绎确定性的可能性，通过形成与演绎相关的信任，从而导致应用程序的使用量增加。我们进一步假设传统的归纳相关信任线索仍然具有相关性，并且同样会导致应用程序的使用量增加。最后，我们假设交易风险和演绎过程的成本调节了这些直接影响。


We tested our theoretical predictions using a survey employing a self-created dApp in conjunction with a novel sample of 536 dApps and found empirical support for our claims. Our survey suggested that deduction-related trust in the smart contract has discriminant validity, as it is empirically distinguishable from classical induction-related trust in the dApp provider and institution-based trust in the transaction environment. Our dApp dataset comprised applications that differ in whether they offer the possibility of deductive certainty (and thus the formation of deduction-related trust) and to what extent their vendor provides cues allowing its users to form induction-related trust. Using this variation, we found empirical evidence showing that dApps allowing the formation of deduction-related trust, and also those facilitating induction-related trust, are adopted by more users. Moreover, we found evidence of complementarity between the two types of trust. Overall, our empirical results suggest that smart contract-based apps are not trust-free but offer a new way to form trust independent of their providers’ characteristics.




我们使用自行创建的 dApp 和 536 个 dApp 的新颖样本进行调查，测试了我们的理论预测，并为我们的主张找到了实证支持。我们的调查表明，智能合约中与演绎相关的信任具有区分有效性，因为它在经验上与 dApp 提供商中的经典归纳相关信任和交易环境中基于机构的信任有区别。我们的 dApp 数据集包含的应用程序的不同之处在于它们是否提供演绎确定性的可能性（从而形成与演绎相关的信任），以及它们的供应商在多大程度上提供了允许用户形成与归纳相关的信任的线索。利用这种变化，我们发现经验证据表明，允许形成演绎相关信任以及促进归纳相关信任的 dApp 被更多用户采用。此外，我们发现了两种信任之间互补性的证据。总体而言，我们的实证结果表明，基于智能合约的应用程序并非无需信任，而是提供了一种独立于提供商特征来形成信任的新方法。


Our work makes two contributions, which we will elaborate on in greater detail in the discussion section. First, we contribute to the trust literature by introducing an epistemological perspective on trust formation and adding deductive certainty, the possibility of deductive certainty, and deduction-related trust as new constructs. Second, we contribute to the literature on the relationship between blockchain and trust by explaining under what conditions smart contracts on a blockchain can make trust (in the core) dispensable and when they are more likely to lead to a new type of trust (deduction-related trust). This allows us to bridge early work, which argues that blockchain can create “trustfree” systems (Beck et al., 2016; Hawlitschek et al., 2018; Notheisen et al., 2017), with more recent work arguing this new technology will merely induce a shift from interpersonal to system or algorithm-based trust (Chawla, 2020; Lumineau et al., 2021, 2023; Wang et al., 2022).




我们的工作做出了两项贡献，我们将在讨论部分更详细地阐述。首先，我们通过引入关于信任形成的认识论视角并添加演绎确定性、演绎确定性的可能性以及与演绎相关的信任作为新的结构，对信任文献做出了贡献。其次，我们通过解释在什么条件下区块链上的智能合约可以使信任（核心）变得可有可无，以及何时更有可能导致新型信任（与演绎相关的信任），从而为有关区块链和信任之间关系的文献做出贡献。这使我们能够将早期的工作与认为区块链可以创建“无信任”系统的工作联系起来（Beck et al., 2016; Hawlitschek et al., 2018; Notheisen et al., 2017），而最近的工作则认为这项新技术只会导致从人际信任转向基于系统或算法的信任（Chawla, 2020; Lumineau et al., 2021， 2023；王等人，2022）。


Our work also has important practical implications for dApp providers and IT developers in general. DApp providers should not assume that their dApps are “trust-free” but rather see offering the possibility of deductive certainty as an additional way to form (deduction-related) trust. At the same time, they should try to build classical, inductive trust by signaling their integrity, benevolence, and ability. IT systems developers and online vendors in general may want to consider the degree to which their systems allow deduction as a potential avenue to enhance their application’s trustworthiness and its adoption—especially in settings where the institutional enforcement of contracts might foreclose economic exchange, or in the case of AI agents, where increased complexity of the algorithm improves performance but obviates deduction.




我们的工作对于 dApp 提供商和 IT 开发人员来说也具有重要的实际意义。 DApp 提供商不应假设他们的 dApp 是“免信任”的，而应将提供演绎确定性的可能性视为形成（与演绎相关）信任的另一种方式。与此同时，他们应该通过表现出自己的正直、仁慈和能力来尝试建立经典的归纳性信任。一般来说，IT 系统开发人员和在线供应商可能会考虑他们的系统允许扣除的程度，作为提高应用程序可信度和采用率的潜在途径，特别是在机构执行合同可能会阻止经济交换的情况下，或者在人工智能代理的情况下，算法复杂性的增加提高了性能，但避免了扣除。


## An Epistemological Perspective on Trust Formation




## 信任形成的认识论视角


According to Mayer et al. (1995;712), trust is “the willingness of a party to be vulnerable to the actions of another party based on the expectation that the other will perform a particular action important to the trustor, irrespective of the ability to monitor or control that other party.” As it is an almost inevitable dimension of all human interactions, scholars from different disciplines have invested significant effort in studying the formation and effects of trust across different levels of analysis (Rousseau et al., 1998). We follow Bachmann and Zaheer’s (2006) classification of the trust literature into four levels of analysis (individual level, organization or inter-organization level, cross-level approaches, and society and economic level) and focus on the individual level. With more and more human interactions being conducted online, within this stream, IS scholars, in particular, have shifted their attention to trust formation in the context of IT-intermediated transactions and online commerce (Gefen et al., 2003; McKnight & Chervany, 2001; Pavlou & Gefen, 2004). In these settings, forming trust is especially challenging, as the exchange relationship’s impersonal and often one-time nature calls for new ways to form and maintain trusting relationships (Beldad et al., 2010; Stewart, 2003). To understand the sociotechnical complexities of trust formation in these environments, scholars have focused on the role of the IT systems in facilitating trust formation. For instance, they have studied online reputation mechanisms, escrow services, and mobile payment systems (Ba & Pavlou, 2002; Pavlou & Gefen, 2004; Zhou, 2012) and found that trust in the technology itself plays a crucial role in forming users’ beliefs and shaping their trusting behavior (McKnight et al., 2011; Ratnasingam & Pavlou, 2002).




根据梅耶尔等人的说法。 (1995;712)，信任是“一方愿意受到另一方行为的影响，其基础是预期另一方将执行对委托人而言重要的特定行动，无论监督或控制另一方的能力如何。”由于信任是所有人类互动中几乎不可避免的一个维度，不同学科的学者投入了大量的精力来研究不同层次分析中信任的形成和影响（Rousseau et al., 1998）。我们遵循 Bachmann 和 Zaheer (2006) 将信任文献分为四个分析层面（个人层面、组织或组织间层面、跨层面方法以及社会和经济层面），并重点关注个人层面。随着越来越多的人类互动在网上进行，在这一潮流中，信息系统学者尤其将注意力转向了信息技术中介交易和在线商务背景下的信任形成（Gefen et al., 2003; McKnight & Chervany, 2001; Pavlou & Gefen, 2004）。在这些环境中，形成信任尤其具有挑战性，因为交换关系的非个人性且通常是一次性的性质需要新的方式来形成和维持信任关系（Beldad 等，2010；Stewart，2003）。为了了解这些环境中信任形成的社会技术复杂性，学者们将重点放在 IT 系统在促进信任形成中的作用。例如，他们研究了在线信誉机制、托管服务和移动支付系统（Ba & Pavlou，2002；Pavlou & Gefen，2004；Zhou，2012），发现对技术本身的信任在形成用户信念和塑造他们的信任行为方面发挥着至关重要的作用（McKnight 等，2011；Ratnasingam & Pavlou，2002）。


Recently, with the advent of blockchain technology, online trust formation has attracted a new wave of interest, as blockchains are supposedly revolutionizing the role of trust in online interactions and radically reshaping e-commerce and related industries (Dutra et al., 2018). Early blockchain researchers formulated the vision of “trust-free” transaction systems (Beck et al., 2016) and developed initial proofs of concept (e.g., Notheisen et al., 2017).




最近，随着区块链技术的出现，在线信任形成吸引了新一波的兴趣，因为区块链被认为正在彻底改变信任在在线互动中的作用，并从根本上重塑电子商务及相关行业（Dutra 等人，2018）。早期的区块链研究人员制定了“无信任”交易系统的愿景（Beck 等人，2016）并开发了初步的概念证明（例如，Notheisen 等人，2017）。


Based on an extensive literature review, Hawlitschek et al. (2018) curbed the enthusiasm about fully “trust-free” systems by explaining that the notion of being “trust-free” is a “rather technical idea” and only applies to closed technical systems. The authors argue that beyond this technical system, whenever human interaction is required, trust will still be relevant and needs to be studied from a behavioral perspective. Relying on affordance theory and a case study design, Chen et al. (2023) also contributed to this perspective. Similarly, Wang et al. (2022) and Lumineau et al. (2023) argued that blockchain technology changes the nature of trust, how it is formed, and who is the target of trust. Regarding trust’s nature, they conjecture a shift from interpersonal trust toward trust in a technical system based on digital technology. Trust formation, they predict, will shift from process-based formation, where trust is formed through shared experience through direct collaboration, to characteristic-based formation, where trust is formed based on categorizing the counterparty within a specific societal group, and institution-based formation, where trust is formed through the availability of formal societal structures like laws and regulations. Finally, regarding the target of trust, they expect it to shift from the counterparty to the technical system and the party in charge of it.




Hawlitschek 等人基于广泛的文献综述。 （2018）通过解释“免信任”的概念是一个“相当技术性的想法”并且仅适用于封闭的技术系统，遏制了人们对完全“免信任”系统的热情。作者认为，除了这个技术系统之外，每当需要人类互动时，信任仍然是相关的，需要从行为的角度进行研究。 Chen 等人依靠可供性理论和案例研究设计。 （2023）也对这一观点做出了贡献。同样，王等人。 （2022）和卢米诺等人。 （2023）认为区块链技术改变了信任的本质、信任的形成方式以及信任的对象是谁。关于信任的本质，他们推测从人际信任转向基于数字技术的技术体系信任。他们预测，信任的形成将从基于流程的形成（信任是通过直接合作共享经验来形成）转变为基于特征的形成（信任是根据对特定社会群体中的交易对手进行分类而形成的）以及基于制度的形成（信任是通过法律和法规等正式社会结构的可用性而形成）。最后，关于信任的对象，他们希望信任的对象从交易对手转向技术系统及其负责方。


Although this research has contributed greatly to a better understanding of how blockchain technology can enhance interorganizational trust by shifting the focus from the counterparty to the IT system and its provider, it does not explain under what circumstances trust can become dispensable and thus leaves one of the biggest puzzles unanswered. Further, by emphasizing that the target of trust moves from the individual party to the blockchain system and its provider, it would predict that differences between providers on the same platform should matter less. However, as we show later, these differences are still of great importance.




尽管这项研究极大地促进了人们更好地理解区块链技术如何通过将焦点从交易对手转移到 IT 系统及其提供商来增强组织间信任，但它并没有解释在什么情况下信任可以变得可有可无，从而留下了最大的难题之一。此外，通过强调信任的目标从个体转移到区块链系统及其提供商，可以预测同一平台上的提供商之间的差异应该不那么重要。然而，正如我们稍后所展示的，这些差异仍然非常重要。


We argue that this gap has emerged due to a limited perspective on trust formation. Trust is commonly conceptualized as the outcome of a cognitive process (Gefen et al., 2003; McKnight et al., 1998).<sup>3</sup> As we demonstrate in the following section, adopting an epistemological perspective on this cognitive process reveals that the relevant trust literature has predominantly conceptualized trust as the outcome of an inductive process. While this perspective was largely sufficient in the past, when most transactions strongly depended on human intervention, today, many transactions and trusting relationships are mediated by formal programs and computer systems (Gefen et al., 2003). Unlike the human mind, which is only boundedly rational (Simon, 1990), these systems follow clearly defined protocols that can, in principle, be comprehended in a deductive process. Comprehensibility is, however, limited by the complexity of the protocol, which in some cases, especially with AI systems, is so high that it defies any deductive processing by a human. This shift thus prompts the question: what role does deduction play in this context? We argue that deduction can serve as an alternative trust formation process. This extension of the current literature is necessary as a deductive process allows us to reach full certainty and thus enables us to explain under what circumstances a “trust-free” system is possible. Furthermore, it allows us to analyze when individuals are more likely to resort to trust. Therefore, this perspective helps to connect the literature that argues for the existence of “trust-free” systems (e.g., Beck et al., 2016; Greiner & Wang, 2015; Notheisen et al., 2017) and the literature that argues for the inevitability of trust, even if a transaction is fully mediated by technology (e.g., Lumineau et al., 2023; Wang et al., 2022).




我们认为，这种差距的出现是由于对信任形成的视角有限。信任通常被概念化为认知过程的结果（Gefen 等人，2003；McKnight 等人，1998）。<sup>3</sup>正如我们在下一节中所论证的，对这一认知过程采用认识论视角表明，相关信任文献主要将信任概念化为归纳过程的结果。虽然这种观点在过去基本上是足够的，当时大多数交易强烈依赖于人为干预，但今天，许多交易和信任关系是由正式程序和计算机系统介导的（Gefen 等人，2003）。与人类思维不同，人类思维只是有限理性的（Simon，1990），这些系统遵循明确定义的协议，原则上可以在演绎过程中理解。然而，可理解性受到协议复杂性的限制，在某些情况下，尤其是人工智能系统，协议的复杂性非常高，以至于无法由人类进行任何演绎处理。因此，这种转变提出了一个问题：演绎在这种情况下扮演什么角色？我们认为演绎可以作为一种替代的信任形成过程。当前文献的这种扩展是必要的，因为演绎过程使我们能够达到完全的确定性，从而使我们能够解释在什么情况下“无信任”系统是可能的。此外，它使我们能够分析个人何时更有可能诉诸信任。因此，这种观点有助于将主张“无信任”系统存在的文献（例如，Beck等人，2016；Greiner＆Wang，2015；Notheisen等人，2017）与主张信任不可避免的文献联系起来，即使交易完全由技术中介（例如，Lumineau等人，2023；Wang等人， 2022）。


To develop this new perspective, we are inspired by Simmel’s (1930) notion of trust as “weak inductive knowledge” combined with some leap of faith (Möllering, 2001) and extend this idea by drawing on the philosophy of science literature. First, we review the literature and discuss why, so far, it has conceptualized trust predominantly as the outcome of an inductive process. Then, we explain why a deductive process can lead to trust and how this new type of trust differs from established induction-related forms of trust. Finally, we use this new perspective to discuss smart contracts as a new trustbuilding technology.




为了发展这一新视角，我们受到齐美尔（Simmel，1930）的信任概念的启发，即“弱归纳知识”与某种信仰的飞跃相结合（Möllering，2001），并通过借鉴科学哲学文献来扩展这一想法。首先，我们回顾文献并讨论为什么到目前为止，它主要将信任概念化为归纳过程的结果。然后，我们解释为什么演绎过程可以导致信任，以及这种新型信任与已建立的归纳相关形式的信任有何不同。最后，我们用这个新的视角来讨论智能合约作为一种新的信任构建技术。


## Inductive Perspective on Trust Formation in the Literature




## 文献中信任形成的归纳视角


Implicitly or explicitly, Simmel’s (1930) notion of trust as weak inductive knowledge combined with some leap of faith greatly influenced subsequent trust research (Möllering, 2001). It constitutes the idea that trust is not just a form of knowledge as it “presumes a leap to commitment, a quality of ‘faith’ which is irreducible” (Giddens, 1991, p. 19). The need for a leap of faith becomes apparent when considering the inductive nature of the knowledge on which trust is based. In an inductive process, knowledge is attained by generalizing from specific observations (Sternberg & Mio, 2009). Inductive conclusions are probable based on the given evidence but never certain (Copi, 2016). In a trust formation process, the trustor must collect evidence that allows the trustor to form positive beliefs about the trustee’s trustworthiness. Trustworthiness is the trustor’s perception that the trustee has characteristics that benefit them in an exchange relationship (McKnight et al., 2002a). Although researchers have linked many characteristics to trustworthiness, the most prominent are integrity (the degree to which the other party keeps promises and is honest), benevolence (the degree to which the other party cares about the trustor and is motivated to act in their interest), and ability (the capability to deliver what has been promised) as most other characteristics conceptually overlap with these (Doney & Cannon, 1997; Gefen et al., 2003; Mayer et al., 1995; McKnight et al., 1998). These characteristics are latent and thus must be generalized from observations in an inductive process. Only if the trustor has gathered sufficient positive beliefs about the trustee’s trustworthiness will the trustor feel confident enough to engage in trusting behavior and make themselves vulnerable to the trustee’s actions. The inductive nature of this process implies that it may be probable that the other party will not behave opportunistically, but never certain.




齐美尔（Simmel，1930）将信任视为弱归纳知识与某种信念的飞跃相结合，或隐或显地影响了后来的信任研究（Möllering，2001）。它构成了这样一种观念，即信任不仅仅是一种知识形式，因为它“假定了承诺的飞跃，是一种不可还原的‘信仰’品质”（Giddens，1991，p.19）。当考虑到信任所基于的知识的归纳性质时，信仰飞跃的必要性就变得显而易见。在归纳过程中，知识是通过对具体观察进行概括而获得的（Sternberg & Mio，2009）。归纳结论可能基于给定的证据，但从来不是确定的（Copi，2016）。在信任形成过程中，委托人必须收集证据，使委托人对受托人的可信度形成积极的信念。可信度是指委托人认为受托人具有在交换关系中对他们有利的特征（McKnight 等，2002a）。尽管研究人员将许多特征与可信度联系起来，但最突出的是正直（对方信守承诺和诚实的程度）、仁慈（对方关心委托人并有动力为自己的利益行事的程度）和能力（兑现承诺的能力），因为大多数其他特征在概念上与这些特征重叠（Doney & Cannon，1997；Gefen 等，2003；Mayer 等，1995；麦克奈特等人，1998）。这些特征是潜在的，因此必须通过归纳过程中的观察来概括。只有当委托人对受托人的可信度有足够的积极信念时，委托人才会有足够的信心进行信任行为，并使自己容易受到受托人行为的影响。这一过程的归纳性质意味着另一方可能不会采取机会主义行为，但永远无法确定。


Finding different sources or antecedents of these trusting beliefs is at the core of the trust formation literature. Drawing on diverse theoretical streams, scholars have identified numerous trust antecedents. McKnight et al.’s (1998) classification distinguishes personality-based trust, cognition-based trust, knowledge-based trust, calculative-based trust, and institutionbased trust. We focus our review on knowledge-based and institution-based trust, as they can have deductive elements— which we discuss later—and thus must be delineated from the new trust construct we introduce later. Given the nature of the trust object we focus on, we add technology-based trust to this list (McKnight et al., 2011).




寻找这些信任信念的不同来源或前因是信任形成文献的核心。学者们利用不同的理论流派，发现了许多信任的前因。 McKnight 等人（1998）的分类区分了基于人格的信任、基于认知的信任、基于知识的信任、基于计算的信任和基于制度的信任。我们的审查重点是基于知识和基于制度的信任，因为它们可能具有演绎元素（我们稍后会讨论），因此必须从我们稍后介绍的新信任结构中进行界定。鉴于我们关注的信任对象的性质，我们将基于技术的信任添加到此列表中（McKnight 等，2011）。


Knowledge-based or experiential trust is a positive belief arising when the trustor’s knowledge about the trustee allows the trustor to predict the trustee’s future behavior (e.g., Doney et al., 1998; Poppo et al., 2008b). In particular, familiarity with how the other party conducts business has been identified as an important source of knowledge-based trust (Gefen, 2000; Gefen et al., 2003; Gulati, 1995). This knowledge is based on past behavior and must be generalized to the trustee’s future behavior, which, again, is an inductive process.




基于知识或经验的信任是当委托人对受托人的了解允许委托人预测受托人的未来行为时产生的积极信念（例如，Doney et al., 1998; Poppo et al., 2008b）。特别是，熟悉对方如何开展业务已被认为是基于知识的信任的重要来源（Gefen，2000；Gefen 等，2003；Gulati，1995）。这种知识基于过去的行为，必须推广到受托人未来的行为，这又是一个归纳过程。


Institution-based trust originates from users feeling secure about a transaction’s environment because of third-party guarantees, safety nets, or other impersonal measures that make the correct execution of a transaction more likely (Pavlou & Gefen, 2004; Shapiro, 1987; Zucker, 1986). As institutionbased trusting beliefs are expectations generalized from the institutional environment to the specific instance (Wingreen et al., 2019), they are automatically available to all actors within the same institutional environment. Institution-based trust is fully or largely based on the inductive process of learning how reliable these measures are. While the legal system allows, to some extent, for deducing, e.g., the outcome of a contract-based transaction, such deduction has its limits since contracts can be violated, legal texts are phrased in (potentially ambiguous) natural language, and the law is enforced by (boundedly rational) humans. Thus, the formation of institution-based trust in the legal system also requires induction.




基于机构的信任源于用户对交易环境的安全感，因为第三方担保、安全网或其他客观措施使交易更有可能正确执行（Pavlou＆Gefen，2004；Shapiro，1987；Zucker，1986）。由于基于制度的信任信念是从制度环境泛化到特定实例的期望（Wingreen 等人，2019），因此它们自动可供同一制度环境中的所有参与者使用。基于机构的信任完全或很大程度上基于了解这些措施的可靠性的归纳过程。虽然法律体系在某种程度上允许推断，例如基于合同的交易的结果，但这种推断有其局限性，因为合同可能被违反，法律文本是用（可能不明确的）自然语言表述的，并且法律是由（有限理性的）人类执行的。因此，对法律体系基于制度的信任的形成也需要诱导。


Technology-based trust is the belief that the IT artifact mediating an exchange relationship is reliable, helpful, and functional (McKnight et al., 2011; Wingreen et al., 2019). Although some scholars have seen trust as an inherently human phenomenon that requires a volitional agent (i.e., an agent that has the power to choose) (Friedman et al., 2000), more recent research adopted a broader definition of trust seeing it arising in situations “when one has to make oneself vulnerable by relying on another person or object, regardless of the trust object’s will or volition” (McKnight et al., 2011, p. 3). This definition enables a shift in the trust object: Instead of trusting the intentions of the technology’s creators, trustors can form trusting beliefs about the technology itself. This differentiation is especially important in cases where the technology is created by a third party and thus independent of dyadic actions. Related to the concept of technology-based trust, Wang et al. (2022) introduced the notion of system-based trust and Chawla (2020) that of “algorithmic trust.”




基于技术的信任是指相信调解交换关系的 IT 工件是可靠的、有帮助的和功能性的（McKnight 等人，2011 年；Wingreen 等人，2019 年）。尽管一些学者将信任视为一种固有的人类现象，需要有意志的代理人（即有选择权的代理人）（Friedman et al., 2000），但最近的研究采用了更广泛的信任定义，认为信任出现在“当一个人必须通过依赖另一个人或物体而使自己变得脆弱时，无论信任对象的意愿或意志如何”的情况（McKnight et al., 2011, p.3）。这个定义使得信任对象发生了转变：信任者可以形成对技术本身的信任信念，而不是信任技术创造者的意图。当技术是由第三方创建并因此独立于二元行为的情况下，这种区别尤其重要。与基于技术的信任的概念相关，Wang 等人。 (2022) 引入了基于系统的信任的概念，而 Chawla (2020) 则引入了“算法信任”的概念。


Regarding the formation of technology-based trust, one group of researchers argues that it is a form of knowledge-based trust (e.g., Lippert, 2008; Pavlou, 2003; Thatcher et al., 2011). Another stream of research argues that “generalized expectancies are the basis for the formation of technologybased trust“ (Wingreen et al., 2019, p. 344). “Generalized expectancies” are based on experience from earlier, familiar situations that are generalized to a new, unfamiliar situation (Rotter, 1971). Hence, both explanations of the formation of technology-based trust focus on an inductive process. This view is supported by McKnight et al.’s (2011, p. 6) remark that the expectations of a technology being functional, reliable, and helpful “are perceptual, rather than objective in nature.”




关于基于技术的信任的形成，一组研究人员认为这是基于知识的信任的一种形式（例如，Lippert，2008；Pavlou，2003；Thatcher 等，2011）。另一种研究认为，“普遍预期是形成基于技术的信任的基础”（Wingreen 等人，2019 年，第 344 页）。 “广义期望”基于早期熟悉情况的经验，这些经验被推广到新的、不熟悉的情况（Rotter，1971）。因此，对基于技术的信任形成的两种解释都集中在归纳过程上。 McKnight 等人（2011 年，第 6 页）的评论支持了这一观点，即对技术功能性、可靠性和有用性的期望“本质上是感性的，而不是客观的”。


The above discussion shows that existing trust research sees trust as the outcome of an inductive process. We refer to this type of trust as induction-related trust. As an inductive process only allows conclusions with some probability but never certainty, the various types of induction-related trust can never lead to a situation where trust becomes dispensable.




上述讨论表明，现有的信任研究将信任视为归纳过程的结果。我们将这种类型的信任称为感应相关信任。由于归纳过程只允许有一定概率而非确定性的结论，因此与归纳相关的各种类型的信任永远不会导致信任变得可有可无的情况。


## Deductive Certainty and Deduction-Related Trust




## 演绎确定性和与演绎相关的信任


## Definitions




## 定义


In contrast to induction, deduction allows one to draw certain conclusions (Copi, 2016). It does so by logically linking premises with conclusions. If the premises are valid, which can be verified ex ante, then the conclusion becomes inevitable as a logical consequence (Johnson-Laird, 2001). According to Tarski (1990), a key feature of such a logical consequence is that it is knowable a priori. Hence, it does not require any form of empirical investigation. By verifying its premises and retracing the full chain of logical steps, one ascertains the conclusion. One understands it as one understands a mathematical proof. For example, we know that Pythagoras’s theorem holds not because we have inductively checked it repeatedly by comparing surface areas, but because we can read and understand its proof, or because we know that others have done so.




与归纳相反，演绎可以得出某些结论（Copi，2016）。它通过逻辑地将前提与结论联系起来来做到这一点。如果前提是有效的，可以事前验证，那么结论就成为必然的逻辑结果（Johnson-Laird，2001）。根据塔斯基（Tarski，1990）的说法，这种逻辑结果的一个关键特征是它是先验可知的。因此，它不需要任何形式的实证研究。通过验证其前提并追溯整个逻辑步骤链，可以确定结论。人们理解它就像理解数学证明一样。例如，我们知道毕达哥拉斯定理成立，不是因为我们通过比较表面积反复归纳检验了它，而是因为我们可以阅读和理解它的证明，或者因为我们知道其他人已经这样做了。


To delineate this form of certainty from the colloquial use of the term, which sees certainty as a high level of confidence, we refer to certainty attained through a logical-deductive process as deductive certainty.<sup>4</sup> When deductive certainty is reached, trust in the core of the system (see below) becomes dispensable, as there is no more uncertainty and no dependence on any other party—two fundamental prerequisites of trust (Mayer et al., 1995; McKnight et al., 1996).




为了从术语的口语使用中描述这种形式的确定性（将确定性视为高度的置信度），我们将通过逻辑演绎过程获得的确定性称为演绎确定性。<sup>4</sup>当达到演绎确定性时，对系统核心的信任（见下文）就变得可有可无，因为不再存在不确定性，也不再依赖任何其他方——这是信任的两个基本先决条件（Mayer 等人， 1995；麦克奈特等人，1996）。


Attaining deductive certainty thus requires two elements: A system amenable to logical analysis, offering the possibility of deductive certainty (“possibility” in the sense of “option,” not in the sense of “probability”), and the cognitive effort to perform this logical analysis. The possibility of deductive certainty, in turn, has three prerequisites. Transparency: All actions the object can take together with their triggering conditions must be auditable ex ante by the trustor. For example, a fintech app for stock trading would meet this requirement if its entire code base, including frontend and backend, were accessible for users to inspect. Deducibility: The chain of steps connecting triggers to actions must be processable by pure logic and leave no room for interpretation. For the fintech app, this means that every user action (e.g., clicking “buy stock”) is algorithmically linked to backend processes, enabling users to logically predict how their balance will update without ambiguity. Immutability: Ex post adaptations to the actions or triggering conditions that determine the object’s behavior must be excluded from the outset. Again, in the case of the fintech app, this ensures that the transaction logic, once specified, cannot be modified or interfered with—especially not during a trade. The effort and skill required to use the possibility of deductive certainty to attain full deductive certainty may, in fact, be considerable, and humans generally seek to strike a balance between cognitive effort and acceptable risk (e.g., Elsbach & Elofson, 2000; Gefen et al., 2003). Thus, it is unlikely that many agents will be willing or even able to rely on full deductive certainty. In the case of the fintech app, even if all requirements have been met, users would need the ability to read and understand frontend code (e.g., JavaScript), backend code (e.g., database queries), and APIs the app uses to connect with stockbrokers. Especially as every app might use a combination of different tools and languages, the cost of attaining full deductive certainty can become prohibitively expensive.




因此，获得演绎确定性需要两个要素：一个适合逻辑分析的系统，提供演绎确定性的可能性（“选择”意义上的“可能性”，而不是“概率”意义上的），以及执行这种逻辑分析的认知努力。演绎确定性的可能性又具有三个先决条件。透明度：对象可以采取的所有操作及其触发条件必须可由委托人事前审计。例如，如果用于股票交易的金融科技应用程序的整个代码库（包括前端和后端）可供用户检查，则该应用程序将满足此要求。可推论：连接触发器和动作的步骤链必须可以通过纯逻辑进行处理，并且不留有解释的空间。对于金融科技应用程序来说，这意味着每个用户操作（例如，点击“购买股票”）都通过算法链接到后端流程，使用户能够逻辑地预测其余额将如何更新而不会含糊不清。不变性：必须从一开始就排除对决定对象行为的动作或触发条件的事后适应。同样，就金融科技应用程序而言，这确保了交易逻辑一旦指定，就不能被修改或干扰，尤其是在交易期间。事实上，利用演绎确定性的可能性来获得完全的演绎确定性所需的努力和技能可能是相当大的，并且人类通常寻求在认知努力和可接受的风险之间取得平衡（例如，Elsbach & Elofson，2000；Gefen 等，2003）。因此，许多代理人不太可能愿意甚至能够依赖完全的演绎确定性。就金融科技应用程序而言，即使满足了所有要求，用户也需要能够阅读和理解前端代码（例如 JavaScript）、后端代码（例如数据库查询）以及应用程序用于与股票经纪人连接的 API。特别是由于每个应用程序都可能使用不同工具和语言的组合，因此获得完全演绎确定性的成本可能会变得非常昂贵。


However, because the trust literature understands trust as a complexity reduction mechanism that humans use to reduce the cognitive burden in their relationships with others (Luhmann, 1979), we argue that already performing parts of the deductive process can form the basis of trust, as well as the knowledge that others have or could have performed it. To emphasize that this trust is the outcome of a deductive rather than an inductive process, we refer to it as deduction-related trust.<sup>5</sup> Deductionrelated trust emerges through the formation of positive beliefs that although the other party’s behavior is not observable, there are rules in place that force the other party to deliver the promised outcome and that these rules can be proven ex ante. According to our definition, deduction-related trust is based on the belief in the possibility of deductive certainty (thus, it has the same prerequisites as the latter), possibly some deductive steps by the focal person or by others, and the general ontological conviction that cause-and-effect relationships can be verified by pure deductive logic. Therefore, deduction-related trust combines some deductive knowledge with the belief in the possibility of deductive certainty. This definition parallels Simmel’s (1930) perspective on trust as inductive knowledge combined with some quasi-religious faith. In the case of deduction-related trust, the leap of faith required to overcome the gap left by incomplete deductive knowledge may, partly or completely, rest on the ontological conviction that cause-andeffect relationships can be verified by pure deductive logic.




然而，由于信任文献将信任理解为一种复杂性降低机制，人类用它来减轻与他人关系中的认知负担（Luhmann，1979），因此我们认为已经执行部分演绎过程可以构成信任的基础，以及其他人已经或可能已经执行的知识。为了强调这种信任是演绎而非归纳过程的结果，我们将其称为演绎相关信任。<sup>5</sup>演绎相关信任是通过形成积极信念而产生的，即虽然对方的行为不可观察，但存在规则迫使对方交付承诺的结果，并且这些规则可以事前证明。根据我们的定义，与演绎相关的信任是基于对演绎确定性可能性的信念（因此，它具有与后者相同的先决条件），可能是焦点人或其他人的一些演绎步骤，以及因果关系可以通过纯粹演绎逻辑来验证的普遍本体论信念。因此，与演绎相关的信任将一些演绎知识与对演绎确定性可能性的信念结合起来。这个定义与齐美尔（Simmel，1930）关于信任的观点相似，信任是归纳知识与某种准宗教信仰的结合。在与演绎相关的信任的情况下，克服不完整的演绎知识留下的差距所需的信仰飞跃可能部分或完全依赖于本体论信念，即因果关系可以通过纯粹的演绎逻辑来验证。


## Delineation From Existing Forms of Trust and Trust Antecedents




## 现有信任形式和信任前因的描述


To provide conceptual clarity and to justify the introduction of the new construct of “deduction-related trust,” we show in the following how it differs from existing concepts. As deductionrelated trust refers to the cognitive process through which trusting beliefs are formed, rather than to their source (e.g., institutions or technology), established forms, under certain conditions, can be deduction-related as well. Since some forms of trust, such as personality-based trust, have, by definition, no deductive element, we focus on those forms that do allow for some deduction: knowledge-based trust, institution-based trust, and technology-based trust.




为了提供概念清晰度并证明引入“演绎相关信任”新结构的合理性，我们在下面展示它与现有概念的不同之处。由于与演绎相关的信任是指形成信任信念的认知过程，而不是其来源（例如制度或技术），因此在某些条件下，既定形式也可以与演绎相关。由于某些形式的信任，例如基于人格的信任，根据定义不具有演绎元素，因此我们重点关注那些允许进行某些演绎的形式：基于知识的信任、基于机构的信任和基于技术的信任。


Knowledge-based trust arises if the trustor’s knowledge about the trustee allows them to predict the trustee’s future behavior (e.g., Doney et al., 1998; Poppo et al., 2008a). In this sense, deduction-related trust can be seen as knowledge-based. However, knowledge-based trust is commonly conceptualized as experiential, based on familiarity with the trustee or a technology (Gefen et al., 2003; McKnight et al., 2011), which is in stark contrast to the concept of deduction.




如果委托人对受托人的了解使他们能够预测受托人的未来行为，基于知识的信任就会产生（例如，Doney 等人，1998；Poppo 等人，2008a）。从这个意义上讲，与演绎相关的信任可以被视为基于知识的信任。然而，基于知识的信任通常被概念化为经验性的，基于对受托人或技术的熟悉程度（Gefen et al., 2003; McKnight et al., 2011），这与演绎的概念形成鲜明对比。


Institution-based trust allows deduction to some extent if the institutional environment provides rules for a transaction that can be comprehended logically and ensures their execution. Laws, for example, allow some deduction, but because they neither guarantee that the other party will abide by them nor that they will be interpreted and enforced as expected, they do not allow a full deductive process and thus the possibility of deductive certainty. Third-party guarantees or recommendations, another potential source of institutionbased trust (Zucker, 1986), can only be verified through experience and thus induction. Institution-based trust can also originate from IT-enabled institutional mechanisms, like feedback mechanisms or escrow services (Pavlou & Gefen, 2004). As these systems rely less on human execution and more on deterministic rules encoded in computer code, they allow for the attainment of more knowledge about their future behavior through logical deduction. However, to provide the possibility of deductive certainty, all rules must be comprehensively and transparently defined for all parties to audit. Most IT-enabled institutional mechanisms violate this condition and, therefore, preclude deduction-related trust. One recent exception is blockchain platforms, which provide the institutional environment for transactions. As the rules of transactions are immutably predefined and publicly auditable, thus allowing deductive certainty, this kind of institutionbased trust can be deductive. However, this does not mean that, vice versa, deduction-related trust is an instance of institution-based trust, since the former can refer not only to the blockchain environment (the institution) but also, and most importantly, to a specific dApp. We will return to this key distinction later.




如果制度环境为交易提供了可以逻辑理解的规则并保证其执行，那么基于制度的信任就可以在一定程度上进行扣除。例如，法律允许一定的演绎，但由于它们既不保证对方遵守它们，也不保证它们将按预期解释和执行，所以它们不允许完整的演绎过程，从而不允许演绎确定性的可能性。第三方担保或建议是基于机构的信任的另一个潜在来源（Zucker，1986），只能通过经验和归纳来验证。基于机构的信任也可以源自 IT 支持的机构机制，例如反馈机制或托管服务（Pavlou 和 Gefen，2004）。由于这些系统较少依赖于人类执行，而更多地依赖于计算机代码中编码的确定性规则，因此它们允许通过逻辑演绎获得有关其未来行为的更多知识。然而，为了提供演绎确定性的可能性，所有规则都必须全面、透明地定义，以便各方审计。大多数IT支持的制度机制都违反了这一条件，因此排除了与扣除相关的信任。最近的一个例外是区块链平台，它为交易提供了制度环境。由于交易规则是不可更改的预定义且可公开审计的，从而允许演绎确定性，因此这种基于机构的信任是可以演绎的。然而，这并不意味着，反之亦然，与演绎相关的信任是基于机构的信任的一个实例，因为前者不仅可以指区块链环境（机构），而且最重要的是可以指特定的dApp。稍后我们将回到这个关键区别。


Technology-based trust: Deduction-related trust can be technology-based, but it does not have to be. Technologybased trust reflects positive beliefs about a technology’s characteristics (McKnight et al., 2011). Deduction-related trust can also be formed in a mathematical proof or, to some extent, in a legal contract. It reflects a belief in the provable nature of the logic shaping the behavior of the trust object. Although technology makes it easier to comprehend the rules of a transaction by logic, it does not guarantee the possibility of deductive certainty—for instance, if the rules executed by a technology are not visible to all parties.




基于技术的信任：与演绎相关的信任可以基于技术，但不是必须如此。基于技术的信任反映了对技术特征的积极信念（McKnight 等，2011）。与演绎相关的信任也可以在数学证明中形成，或者在某种程度上在法律合同中形成。它反映了对塑造信任对象行为的逻辑的可证明性质的信念。尽管技术使人们更容易通过逻辑理解交易规则，但它并不能保证演绎确定性的可能性——例如，如果一项技术执行的规则并非对所有各方都可见。


## Instances of Deduction-Related Trust




## 与扣除相关的信任实例


Deduction-related trust can be formed regarding not only mathematical proofs but also smart contracts on a blockchain and, to a certain extent, several other objects. We discuss these in turn.




与演绎相关的信任不仅可以针对数学证明，还可以针对区块链上的智能合约以及在一定程度上针对其他几个对象而形成。我们依次讨论这些。


Smart contracts are computer programs stored as bytecode on a blockchain (Fröwis & Böhme, 2017) that, once triggered, are executed automatically (Murray et al., 2019). They are not to be confused with legal contracts (Werbach, 2018). If the offering party discloses the smart contract’s human-readable source code, third parties (e.g., Etherscan) may verify that the source code corresponds to the executable code on the blockchain, and prospective users may then read and comprehend the transaction rules. Conditional on this verification, smart contracts fulfill the requirement of transparency. Also, deducibility is given by virtue of smart contracts being computer programs, which can be processed with deductive logic. Finally, smart contracts on a blockchain are immutable: If implemented correctly, the blockchain platform makes it prohibitively expensive for any party to modify a smart contract ex post (Holden & Malani, 2021; Raskin, 2016; Werbach, 2018) (a claim that itself can be checked deductively, given that the blockchain’s source code is typically open). Thus, smart contracts on a blockchain fulfill all prerequisites for deductive certainty and thus deductionrelated trust. We note that they are also automatically executed by virtue of running on the blockchain. However, we do not subsume this feature under the prerequisites of deductive certainty since it resides on the blockchain, not in the smart contract itself. We elaborate on this distinction below.




智能合约是作为字节码存储在区块链上的计算机程序（Fröwis & Böhme，2017），一旦触发，就会自动执行（Murray 等人，2019）。请勿将它们与法律合同混淆（Werbach，2018）。如果提供方公开智能合约的人类可读源代码，第三方（例如 Etherscan）可以验证源代码是否与区块链上的可执行代码相对应，然后潜在用户可以阅读并理解交易规则。以这种验证为条件，智能合约满足透明度的要求。此外，可推论性是通过智能合约作为计算机程序而给出的，可以用推论逻辑进行处理。最后，区块链上的智能合约是不可变的：如果正确实施，区块链平台会让任何一方事后修改智能合约的成本过高（Holden & Malani，2021；Raskin，2016；Werbach，2018）（考虑到区块链的源代码通常是开放的，这一说法本身可以进行演绎检查）。因此，区块链上的智能合约满足了演绎确定性的所有先决条件，从而满足了与演绎相关的信任。我们注意到，它们也是通过在区块链上运行而自动执行的。然而，我们不会将此功能纳入演绎确定性的先决条件，因为它驻留在区块链上，而不是智能合约本身。我们将在下面详细说明这种区别。


Legal contracts, in conjunction with the legal system, are a second candidate. They define obligations to perform actions in the future (Macneil, 1977). Legal contracts are auditable to the contracting parties and thus provide a certain transparency about the rules shaping the other party’s behavior. They also offer deducibility to some extent, given that they seek to pin down the parties’ obligations, the consequences of their actions, and, possibly, also how these obligations are enforced should a party decide to violate them. However, due to humans’ cognitive limitations and bounded rationality (Simon, 1957), legal contracts are typically incomplete (Williamson, 1985). Furthermore, contractual terms are written in natural language and hence may be ambiguous, which obviates a strict deductive interpretation. Thus, the conditions of transparency and deducibility are fulfilled to some extent, but not fully. The possibility of ex post negotiations of most contractual terms violates the third requirement, immutability. Thus, our arguments about deduction’s role in trust formation apply to legal contracts only to some extent.




法律合同与法律制度相结合，是第二个候选者。它们定义了未来执行行动的义务（Macneil，1977）。法律合同对缔约方来说是可审计的，因此为塑造另一方行为的规则提供了一定的透明度。它们还在某种程度上提供了推论，因为它们试图确定当事人的义务、其行为的后果，以及如果一方决定违反这些义务，则可能如何执行这些义务。然而，由于人类的认知局限性和有限理性（Simon，1957），法律合同通常是不完整的（Williamson，1985）。此外，合同条款是用自然语言编写的，因此可能会含糊不清，从而避免了严格的演绎解释。因此，透明度和可推演性的条件在一定程度上得到了满足，但并不完全满足。大多数合同条款事后谈判的可能性违反了第三个要求，即不变性。因此，我们关于演绎在信托形成中的作用的论点仅在某种程度上适用于法律合同。


Finally, open source software (OSS) is another potential case. Its source code is typically publicly available and amenable to inspection (Fitzgerald, 2006; Von Krogh et al., 2003). Thus, as for smart contracts, transparency and deducibility are given—provided its source code corresponds to the compiled version that the provider runs on its systems. This, however, is difficult or impossible to ascertain. By the same token, immutability is also questionable. Hence, deduction-related trust in OSS depends on whether the trustor trusts the other party to run a compiled version of a designated public source code. It can thus help to overcome doubts in the provider’s ability but not in its integrity and benevolence.




最后，开源软件（OSS）是另一个潜在的案例。其源代码通常是公开的并且易于检查（Fitzgerald，2006；Von Krogh 等人，2003）。因此，对于智能合约来说，只要其源代码与提供商在其系统上运行的编译版本相对应，就可以提供透明度和可推论性。然而，这很难或不可能确定。出于同样的原因，不变性也值得怀疑。因此，对OSS的推演信任取决于信任方是否信任对方运行指定公共源代码的编译版本。因此，它可以帮助克服对提供者能力的怀疑，但不能帮助克服对其诚信和仁慈的怀疑。


We thus find several instances that, to varying degrees, allow for the formation of deduction-related trust. To the highest degree, this is the case for smart contracts on a blockchain.




因此，我们发现了几个在不同程度上允许形成与演绎相关的信任的实例。在最高程度上，这就是区块链上的智能合约的情况。


## Smart Contracts, Dapps, Core, Periphery




## 智能合约、Dapps、核心、外围


Smart contracts seldom occur on their own. Usually, they are embedded in a web application that provides a graphical user interface. As these web applications run their business logic as a smart contract on a decentralized blockchain infrastructure, they are often referred to as decentralized applications or dApps (Cai et al., 2018; Leiponen et al., 2021). DApps, in turn, are embedded in the blockchain and the internet. We refer to the blockchain and the internet as the periphery of the transaction, which is generic and identical for all transactions on the blockchain, and to the transaction-specific dApp as its core. This distinction is central to our argument.




智能合约很少单独发生。通常，它们嵌入在提供图形用户界面的 Web 应用程序中。由于这些 Web 应用程序将其业务逻辑作为去中心化区块链基础设施上的智能合约运行，因此它们通常被称为去中心化应用程序或 dApp（Cai 等人，2018 年；Leiponen 等人，2021 年）。反过来，DApp 又嵌入到区块链和互联网中。我们将区块链和互联网称为交易的外围，对于区块链上的所有交易来说都是通用且相同的，而将特定于交易的dApp称为其核心。这种区别是我们论证的核心。


Previous research has established that users assess the IT artifact itself, the vendor, and the environment to build trust online (Gefen et al., 2003). Therefore, to understand the role of deduction-related trust in a smart contract on users’ overall trust perceptions, it is important to study it in the context of other trust cues provided by the dApp and the periphery.




先前的研究已经证实，用户会评估 IT 工件本身、供应商和环境来建立在线信任（Gefen 等，2003）。因此，要了解智能合约中与演绎相关的信任对用户整体信任感知的作用，重要的是在 dApp 和外围设备提供的其他信任线索的背景下研究它。


Visually, these dApps resemble other web applications, as they rely on websites as their frontend, but they differ technically and in their usage since they introduce two novel IT systems in their backend. Whereas classical web applications run their transaction logic as ordinary computer programs on centralized servers, dApps rely on blockchain platforms as their general transaction infrastructure and one or more smart contracts to define their specific transaction logic (Leiponen et al., 2021). This combination equips dApps with two main technical features: decentralized consensus (all networked parties jointly verify, accept, or reject transactions) and machine-based execution<sup>6</sup> (Lumineau et al., 2021). It also implies that dApps offer an unprecedented value proposition: DApps can rely on a shared version of the truth and automated transactions without requiring an intermediary or humans for their execution. Hence, they are not subject to the unpredictability of human actors, and dApp providers’ control over a specific transaction is significantly reduced.




从视觉上看，这些 dApp 类似于其他 Web 应用程序，因为它们依赖网站作为前端，但它们在技术和用法上有所不同，因为它们在后端引入了两种新颖的 IT 系统。经典 Web 应用程序将其交易逻辑作为普通计算机程序在中心化服务器上​​运行，而 dApp 则依赖区块链平台作为其通用交易基础设施以及一个或多个智能合约来定义其特定交易逻辑（Leiponen 等人，2021）。这种组合为 dApp 提供了两个主要技术特征：去中心化共识（所有网络各方共同验证、接受或拒绝交易）和基于机器的执行<sup>6</sup>（Lumineau 等人，2021）。它还意味着 dApp 提供了前所未有的价值主张：DApp 可以依赖事实的共享版本和自动交易，而不需要中介或人类来执行。因此，它们不会受到人类行为者不可预测性的影响，并且 dApp 提供商对特定交易的控制也显着减少。


There are two ways to transact with a dApp: users can navigate to the dApp’s website (frontend), connect their wallet (a third-party program that manages users’ public and private keys and allows them to initiate transactions), and send a transaction to the dApp’s smart contract deployed on the blockchain. This is by far the most common and easiest way. Alternatively, they can use their wallet to send a transaction directly to the smart contract’s address on the blockchain. In either case, the transaction occurs on the blockchain platform, where a set of decentralized nodes process and vote on the transaction’s validity. Thus, dApps separate control over offering a service from control over the respective execution of the transaction. As this dramatically limits the dApp providers’ agency from engaging in opportunistic behavior, early proponents of this new technology have argued that blockchain-based applications remove the need for trust in the dApp provider (Beck et al., 2016; Greiner & Wang, 2015).




与 dApp 进行交易的方式有两种：用户可以导航到 dApp 的网站（前端），连接钱包（管理用户公钥和私钥并允许他们发起交易的第三方程序），并将交易发送到部署在区块链上的 dApp 智能合约。这是迄今为止最常见和最简单的方法。或者，他们可以使用钱包将交易直接发送到区块链上的智能合约地址。无论哪种情况，交易都发生在区块链平台上，其中一组分散的节点对交易的有效性进行处理和投票。因此，dApp 将提供服务的控制与交易各自执行的控制分开。由于这极大地限制了 dApp 提供商的机构参与机会主义行为，这项新技术的早期支持者认为，基于区块链的应用程序消除了对 dApp 提供商的信任（Beck 等人，2016 年；Greiner 和 Wang，2015 年）。


For this to be true, two conditions must hold. First, the prospective user must know with certainty that the smart contract is free from mistakes and correctly specifies all actions and triggering conditions, as negotiated ex ante. Second, the prospective dApp user must also know with certainty that the periphery will execute the smart contract precisely as specified. Our epistemological perspective on trust formation clarifies that these conditions require a full deductive process. However, while the first condition can be fulfilled in principle, the number of prospective dApp users who are capable of a full deductive process is probably small, and humans are known for striking a balance between acceptable risk and effort (Elsbach & Elofson, 2000; Gefen et al., 2003). Thus, it is unlikely that many users reach full certainty in dApp transactions. Regarding the second condition, a fully deductive analysis of the periphery is excluded since the prerequisites of transparency, immutability, and deducibility are fulfilled for the blockchain but not the internet.




要做到这一点，必须满足两个条件。首先，潜在用户必须确切地知道智能合约没有错误，并按照事前协商正确指定所有操作和触发条件。其次，潜在的 dApp 用户还必须确切地知道外围设备将按照指定的方式精确执行智能合约。我们对信任形成的认识论观点表明，这些条件需要完整的演绎过程。然而，虽然原则上可以满足第一个条件，但能够进行完整演绎过程的潜在 dApp 用户数量可能很少，而且人类以在可接受的风险和努力之间取得平衡而闻名（Elsbach & Elofson，2000；Gefen 等人，2003）。因此，许多用户不太可能在 dApp 交易中获得完全的确定性。对于第二个条件，排除了对外围的完全演绎分析，因为区块链满足了透明性、不可篡改性和可推演性的先决条件，但互联网不满足。


This shows that for many users, adopting a new dApp involves uncertainty and the risk of losing money or personal data, not receiving the promised product or service, receiving it in lower-than-promised quality, or encountering other forms of opportunistic or fraudulent behavior in the provision of the service. If these doubts are not overcome, users will avoid adoption (Gefen, 2000). In such situations, trust can help, as it allows users to move forward despite uncertainty and risk (Luhmann, 1979). Past research has emphasized the importance of trust, especially in a web-based environment where the impersonal nature of a transaction eases opportunistic behavior (Friedman et al., 2000; Gefen, 2000;




这表明，对于许多用户来说，采用新的 dApp 涉及不确定性以及损失金钱或个人数据、未收到承诺的产品或服务、收到的质量低于承诺的质量或在提供服务时遇到其他形式的机会主义或欺诈行为的风险。如果这些疑虑没有得到克服，用户将避免采用（Gefen，2000）。在这种情况下，信任可以提供帮助，因为它允许用户在不确定性和风险的情况下继续前进（Luhmann，1979）。过去的研究强调了信任的重要性，尤其是在基于网络的环境中，交易的非个人性质减轻了机会主义行为（Friedman et al., 2000; Gefen, 2000;


Jarvenpaa et al., 2000; Ratnasingam & Pavlou, 2002; Stewart, 2003) and established that both specific trusting beliefs about the e-vendor (McKnight & Chervany, 2001) and the IT itself (McKnight et al., 2011; Ratnasingam & Pavlou, 2002; Wingreen et al., 2019) lead to trusting intentions, which are associated with greater intended use (Gefen et al., 2003) and adoption (Pavlou, 2003; Pavlou & Fygenson, 2006). Therefore, we argue that while trust is still relevant when users decide to adopt a dApp, dApps enable a much higher degree of deduction-related trust than any other existing technology, up to deductive certainty.




Jarvenpaa 等，2000；拉特纳辛加姆和帕夫卢，2002； Stewart，2003），并确定对电子供应商（McKnight 和 Chervany，2001）和 IT 本身（McKnight 等，2011；Ratnasingam 和 Pavlou，2002；Wingreen 等，2019）的特定信任信念会导致信任意图，这与更大的预期用途相关（Gefen 等，2003）和收养（Pavlou，2003；Pavlou & Fygenson，2006）。因此，我们认为，虽然当用户决定采用 dApp 时信任仍然相关，但 dApp 比任何其他现有技术都能实现更高程度的与演绎相关的信任，直至演绎确定性。


Following prior research and the two conditions we introduced above, trust in a dApp can be separated into a set of specific beliefs about the vendor and the transaction-specific IT (dApp), as the main trust objects, and general beliefs about the institutional transaction environment (blockchain and the internet in general) (Gefen, 2000, 2002; McKnight et al., 2002a; Pavlou & Gefen, 2004). To emphasize this difference, it is helpful to distinguish between the transaction-specific core and the non-specific periphery. The core is the dApp. Trust in the core means that the user believes that the vendor has correctly translated all clauses of a transaction into the smart contract (contracts) and has implemented the frontend (i.e., the dApps website) to call the smart contract correctly. The periphery is the blockchain infrastructure and the internet in general. Trust in the periphery is the belief that the blockchain infrastructure and the internet where the blockchain is embedded guarantee the smart contract’s immutability and automated execution. Whereas trust in the periphery can be transferred to all dApps on the same blockchain and can thus rely more heavily on experience and familiarity (induction-related trust), trust in the transaction-specific core has to be formed anew for every dApp. (Later on, we provide empirical evidence suggesting that trust in the periphery and trust in the transaction-specific smart contracts are indeed distinct constructs.) We acknowledge that induction-based trust in the transaction-specific core of a dApp can also be informed by its similarity to other applications. However, this still requires an assessment of the specific dApp, whereas trust in the periphery automatically generalizes to all dApps that share that periphery.




根据之前的研究和我们上面介绍的两个条件，对 dApp 的信任可以分为一组关于作为主要信任对象的供应商和特定于交易的 IT（dApp）的特定信念，以及关于机构交易环境（一般的区块链和互联网）的一般信念（Gefen，2000，2002；McKnight 等人，2002a；Pavlou 和 Gefen，2004）。为了强调这种差异，区分交易特定的核心和非特定的外围是有帮助的。核心是dApp。对核心的信任意味着用户相信供应商已将交易的所有条款正确翻译为智能合约（合约），并已实现前端（即 dApps 网站）以正确调用智能合约。外围是区块链基础设施和整个互联网。对外围的信任是相信区块链基础设施和嵌入区块链的互联网保证了智能合约的不变性和自动执行。虽然外围的信任可以转移到同一区块链上的所有 dApp，因此可以更加依赖经验和熟悉度（与归纳相关的信任），但必须为每个 dApp 重新建立对特定交易核心的信任。 （稍后，我们提供的经验证据表明，对外围的信任和对特定于交易的智能合约的信任确实是不同的结构。）我们承认，对 dApp 的特定于交易的核心的基于归纳的信任也可以通过其与其他应用程序的相似性来了解。然而，这仍然需要对特定 dApp 进行评估，而对外围设备的信任会自动推广到共享该外围设备的所有 dApp。


The level of trust in the periphery will likely differ between users, but for a given user, it should be the same for all dApps on the same blockchain. Accordingly, we chose dApps on a single blockchain (Ethereum) as our research context, which allowed us to focus on differences in specific trusting beliefs between the dApps. Further, we focused on a user’s first interaction with a dApp, as deduction-related trust should matter more in the initial stage of a trusting relationship, where only little experiential knowledge is available (Rousseau et al., 1998).




用户之间的外围信任级别可能会有所不同，但对于给定用户，同一区块链上的所有 dApp 的信任级别应该相同。因此，我们选择单个区块链（以太坊）上的 dApp 作为我们的研究背景，这使我们能够专注于 dApp 之间特定信任信念的差异。此外，我们关注用户与 dApp 的第一次交互，因为在信任关系的初始阶段，与推导相关的信任应该更重要，因为此时只有很少的经验知识（Rousseau et al., 1998）。


Figure 1 depicts the core and the periphery of a dApp transaction and distinguishes trust in the periphery from dAppspecific trust by showing all trust objects involved in users’ trust formation processes and the parties who develop the dApps (dApp provider) and verify the smart contract (a verification agency, such as Etherscan). Next, we discuss the different types of trust cues (induction-related and deduction-related) that dApp providers can offer to stimulate their prospective users’ trusting beliefs and their intention to adopt the dApp.




图1描绘了dApp交易的核心和外围，并通过显示用户信任形成过程中涉及的所有信任对象以及开发dApp（dApp提供商）和验证智能合约的各方（验证机构，例如Etherscan）来区分外围信任和dApp特定信任。接下来，我们讨论 dApp 提供商可以提供的不同类型的信任线索（归纳相关和演绎相关），以激发潜在用户的信任信念和采用 dApp 的意图。


![](/api/attachments/PHUJTSS5/fulltext/images/00742d775b0a7ece0e2321601978f10aed779be200a0a587dcc5087b1c08fae9.jpg)  
Figure 1. DApp Setup and Core vs. Periphery




![](/api/attachments/PHUJTSS5/fulltext/images/00742d775b0a7ece0e2321601978f10aed779be200a0a587dcc5087b1c08fae9.jpg)  
图 1. DApp 设置以及核心与外围设备


## Hypothesis Development




## 假设发展


## Possibility of Deductive Certainty and Deduction-Related Trust




## 演绎确定性和演绎相关信任的可能性


By running their core business logic as a smart contract on a blockchain and disclosing and verifying its source code, dApp providers can allow users to form deduction-related trust in the dApp. Doing so extends the transparency, deducibility, and immutability provided by the blockchain platform (periphery) to the specific transaction (core). By disclosing the smart contract’s source code and having it verified, the dApp provider creates transparency, allows the verification of immutability, and, together with the fact that the smart contract is a computer program that follows a strict logic executed by the blockchain protocol, facilitates deducibility. Offering the possibility to form deduction-related trust is a deliberate choice by the dApp provider, as only the machine-readable byte code is publicly stored on the blockchain, while the human-readable source code remains in the hands of the dApp provider (Fröwis & Böhme, 2017). If the provider elects to disclose the source code,<sup>7</sup> users can inspect its proper functioning by deduction because it is written in a deterministic computer language, and they can attain deductive certainty.<sup>8</sup> But even if the source code is openly available (as is typically the case with OSS), the question remains whether the disclosed source code corresponds with the executable bytecode stored on the blockchain.




通过将其核心业务逻辑作为区块链上的智能合约运行并公开和验证其源代码，dApp 提供商可以允许用户在 dApp 中形成与扣除相关的信任。这样做将区块链平台（外围）提供的透明度、可推论性和不变性扩展到特定交易（核心）。通过公开智能合约的源代码并对其进行验证，dApp 提供商可以创建透明度，允许验证不变性，并且加上智能合约是遵循区块链协议执行的严格逻辑的计算机程序这一事实，促进了可推论。提供形成与推导相关的信任的可能性是 dApp 提供商的故意选择，因为只有机器可读的字节代码公开存储在区块链上，而人类可读的源代码仍然掌握在 dApp 提供商的手中（Fröwis & Böhme，2017）。如果提供商选择公开源代码，<sup>7</sup>用户可以通过演绎来检查其正常功能，因为它是用确定性计算机语言编写的，并且他们可以获得演绎确定性。<sup>8</sup>但即使源代码是公开可用的（OSS 通常就是这种情况），问题仍然是所公开的源代码是否与区块链上存储的可执行字节码相对应。


To ensure this correspondence, either users will have to compile the source code and verify its correspondence, or the provider must have it verified by a third party, such as Etherscan. Such verification processes are not amenable to deductive analysis, and so users have to resort to induction in order to build trust in them. However, they are part of the periphery, not specific to the smart contract at hand nor to its provider. Hence, building induction-related trust in the verification is possible, which—in case of a positive verification—allows the extension of the dApp-specific possibility of deductive certainty about the dApp smart contract’s source code to its executable bytecode on the blockchain.




为了确保这种对应关系，要么用户必须编译源代码并验证其对应关系，要么提供商必须让第三方（例如 Etherscan）对其进行验证。这种验证过程不适合演绎分析，因此用户必须诉诸归纳才能建立对它们的信任。然而，它们是外围设备的一部分，并不特定于手头的智能合约或其提供商。因此，在验证中建立与归纳相关的信任是可能的，在积极验证的情况下，允许将 dApp 智能合约源代码的演绎确定性的特定可能性扩展到区块链上的可执行字节码。


We conclude that offering the possibility of deductive certainty by disclosing a smart contract’s verified source code allows interested parties to form deduction-related trust in the dApp, which increases the probability of them entering the proposed relationship governed by the smart contract. Hence, we hypothesize:




我们的结论是，通过公开智能合约经过验证的源代码来提供演绎确定性的可能性，允许利益相关方在 dApp 中形成与演绎相关的信任，这增加了他们进入智能合约管辖的拟议关系的可能性。因此，我们假设：


H1: Offering the possibility to attain deductive certainty leads to more users adopting a dApp.




H1：提供获得演绎确定性的可能性会导致更多用户采用 dApp。


Before turning to induction-related trust cues, we point out three mundane limitations to the possibility of deductive certainty. Firstly, the transaction a dApp promises has to be codifiable. Codifiability denotes the degree to which the (actual or hypothetical) legal contract underlying the transaction can be translated into an electronic format that can be processed by machines (Lumineau et al., 2021). Secondly, all inputs of a transaction have to be verifiable. Verifiability in this context refers to the ability to observe the true quality of the information provided by the transacting parties (Lumineau et al., 2021). The possibility of full deductive certainty applies exclusively to blockchain-only operations where the decentralized consensus ensures the integrity of the data, since any off-chain data— required for many use cases beyond cryptocurrency—could suffer from human error or manipulation. Finally, ex post adaptations to the smart contract have to be excluded (Halaburda et al., 2024). Such adaptations could happen if a smart contract relies on logic stored outside the immutable storage of the blockchain, e.g., in libraries. However, as Fröwis and Böhme (2017) show, the immutability of a smart contract’s logic can be proven in a deductive process based on the rules of the blockchain protocol.




在转向与归纳相关的信任线索之前，我们指出演绎确定性可能性的三个常见限制。首先，dApp 承诺的交易必须是可编码的。可编码性表示交易所依据的（实际或假设的）法律合同可以转换为可由机器处理的电子格式的程度（Lumineau 等人，2021）。其次，交易的所有输入都必须是可验证的。在这种情况下，可验证性是指观察交易方提供的信息的真实质量的能力（Lumineau 等人，2021）。完全演绎确定性的可能性仅适用于仅区块链的操作，其中去中心化共识确保了数据的完整性，因为任何链下数据（加密货币之外的许多用例所需的数据）都可能遭受人为错误或操纵。最后，必须排除对智能合约的事后调整（Halaburda 等人，2024）。如果智能合约依赖于存储在区块链不可变存储之外（例如图书馆中）的逻辑，则可能会发生这种适应。然而，正如 Fröwis 和 Böhme（2017）所表明的那样，智能合约逻辑的不变性可以在基于区块链协议规则的演绎过程中得到证明。


## Induction-Related Trust Cues




## 与归纳相关的信任线索


As discussed, potential users of a dApp may form deductionrelated trust in it, but will rarely arrive at deductive certainty. Thus, it is plausible that, in addition, they will resort to classical, induction-related trust cues about the dApp.




正如所讨论的，dApp 的潜在用户可能会对它形成与演绎相关的信任，但很少会达到演绎确定性。因此，此外，他们可能会诉诸关于 dApp 的经典的、与归纳相关的信任线索。


DApp providers can influence potential users’ perception of their trustworthiness by providing cues that allow their users to assess their integrity, benevolence, and ability (McKnight et al., 2002b). From prior research, we know that these cues can trigger different trust antecedents, induce positive beliefs about the dApp or its provider, and influence the users’ willingness to make themselves vulnerable to the dApp provider’s action. For instance, to create knowledge-based trust, the dApp provider can share the team’s educational and professional history to create a feeling of familiarity and the impression that the team is capable of developing a high-quality dApp and smart contract without bugs and security vulnerabilities. To create institutionbased trust, the dApp provider can advertise structural assurances built into or displayed on the website, like providing proof that the company is legally registered, seals of approvals (Nöteberg et al., 1999), privacy policy statements (Palmer et al., 2000), links to highly regarded companies (Stewart, 2003), or references to the blockchain as a secure transaction environment preventing them from interfering with the transaction (McKnight et al., 2002b). In this case, trust emanates from the feeling that the dApp and the provider are embedded in a secure institutional environment (Gefen et al., 2003). All these signals should lead to a more favorable assessment of the dApp provider’s integrity, benevolence, and ability, and hence influence its perceived trustworthiness (McKnight et al., 2002b), which, in turn, should spur more trusting behavior (e.g., Doney & Cannon, 1997; Gefen et al., 2003; Stewart, 2003).




DApp 提供商可以通过提供让用户评估其诚信、仁慈和能力的线索来影响潜在用户对其可信度的看法（McKnight 等人，2002b）。从之前的研究中，我们知道这些线索可以触发不同的信任前提，引发对 dApp 或其提供商的积极信念，并影响用户让自己容易受到 dApp 提供商行为影响的意愿。例如，为了建立基于知识的信任，dApp 提供商可以分享团队的教育和专业历史，以营造一种熟悉感和印象，即团队有能力开发没有错误和安全漏洞的高质量 dApp 和智能合约。为了建立基于机构的信任，dApp 提供商可以宣传网站内置或显示的结构保证，例如提供公司合法注册的证明、批准印章（Nöteberg 等人，1999 年）、隐私政策声明（Palmer 等人，2000 年）、备受推崇的公司的链接（Stewart，2003 年）或引用区块链作为安全交易环境，防止他们干扰交易（McKnight 等人）等人，2002b)。在这种情况下，信任源于 dApp 和提供商嵌入在安全的机构环境中的感觉（Gefen 等人，2003）。所有这些信号应该导致对 dApp 提供商的诚信、仁慈和能力进行更有利的评估，从而影响其感知的可信度（McKnight 等人，2002b），这反过来又应该刺激更多的信任行为（例如，Doney & Cannon，1997；Gefen 等人，2003；Stewart，2003）。


In addition to cues linked to the vendor’s trustworthiness, the vendor can also promote trust in the dApp itself by highlighting the immutability and automated enforcement of the smart contract, emphasizing the diligence and care they have invested in developing the contract, explaining the dApp’s functionality, or showing positive customer reviews regarding the dApp’s reliability and ease of use. These cues allow users to form technology-based trust by stimulating positive beliefs about the dApp (including the smart contract) as an object of trust by enabling inferences about its functionality, helpfulness, and reliability (McKnight et al., 2011).




除了与供应商的可信度相关的线索之外，供应商还可以通过强调智能合约的不变性和自动执行、强调他们在开发合约时投入的勤奋和细心、解释 dApp 的功能或展示客户对 dApp 可靠性和易用性的积极评价来促进对 dApp 本身的信任。这些线索允许用户通过对 dApp（包括智能合约）的功能、有用性和可靠性进行推断，激发对 dApp（包括智能合约）作为信任对象的积极信念，从而形成基于技术的信任（McKnight 等，2011）。


All these cues have in common that, due to their inductive nature, they only allow probabilistic statements about a dApp provider’s or the dApp’s trustworthiness and future behavior. Still, the more such cues that are available, the more trusting beliefs that users will form (McKnight et al., 2002b), and the more users will expect to gain the expected benefits from a transaction with a dApp. Accordingly, we hypothesize:




所有这些线索的共同点是，由于其归纳性质，它们只允许对 dApp 提供商或 dApp 的可信度和未来行为进行概率陈述。尽管如此，可用的此类线索越多，用户就会形成越多的信任信念（McKnight 等人，2002b），并且更多的用户期望从 dApp 交易中获得预期收益。据此，我们假设：


H2: Offering more induction-based trust cues leads to more users adopting a dApp.




H2：提供更多基于归纳的信任线索会导致更多用户采用 dApp。


## The Moderating Role of Risk and Cost of Deductive Certainty




## 风险和演绎确定性成本的调节作用


A core tenet of the trust literature is that trust is a complexity reduction mechanism that reduces humans’ cognitive burden in their relationships with others (Luhmann, 1979). Accordingly, it has been suggested that individuals apply a “cognitive miser” model in their trust formation process and strike a balance between minimizing their cognitive effort and their need to form sufficient confidence in their expectations about the other party’s future behavior (Liu & Goodhue, 2012; Taylor, 1981). Rather than processing all available trust cues and forming the highest level of trust possible, people might use an efficiency-oriented approach and focus on cues that are easy to process (Elsbach & Elofson, 2000). A great deal of research on information processing and decision-making argues that such simplifying approaches rely on hierarchical schemas (Brewer, 1988). For instance, the “dual process” literature argues that people initially use simple, often heuristic cues to evaluate others and only rely on more complex details if the obtained information does not suffice (Fiske & Taylor, 1991). Similarly, the elaboration likelihood model of persuasion (ELM), often used in the context of trust formation (Elsbach & Elofson, 2000; Yang et al., 2006; Zhou, 2012), suggests that individuals prioritize information and process it more or less accurately depending on their motivation and ability (Petty & Cacioppo, 1986). Extending this notion of efficiency to the cognitive processes shaping a user’s trust in a smart contract, we argue that the risk associated with a transaction and the cognitive effort required by the deductive process influence the extent to which users rely on induction- versus deduction-related trust.




信任文献的核心原则是，信任是一种降低复杂性的机制，可以减轻人类在与他人的关系中的认知负担（Luhmann，1979）。因此，有人建议个人在信任形成过程中应用“认知守财奴”模型，并在最小化认知努力和对对方未来行为的期望形成足够信心的需要之间取得平衡（Liu＆Goodhue，2012；Taylor，1981）。人们可能会使用以效率为导向的方法并专注于易于处理的线索，而不是处理所有可用的信任线索并形成尽可能高水平的信任（Elsbach＆Elofson，2000）。关于信息处理和决策的大量研究认为，这种简化方法依赖于分层模式（Brewer，1988）。例如，“双重过程”文献认为，人们最初使用简单的、通常是启发式的线索来评估他人，只有在获得的信息不够时才依赖更复杂的细节（Fiske＆Taylor，1991）。同样，说服的详细化可能性模型（ELM）通常用于信任形成（Elsbach & Elofson，2000；Yang et al.，2006；Zhou，2012），表明个人根据自己的动机和能力对信息进行优先排序并或多或少准确地处理信息（Petty & Cacioppo，1986）。将这种效率概念扩展到塑造用户对智能合约的信任的认知过程，我们认为与交易相关的风险和演绎过程所需的认知努力会影响用户依赖归纳与演绎相关信任的程度。


Risk plays a key role in individuals’ trust formation process as it creates the need for trust in the first place. Trust only becomes important when risk is present, as it helps individuals cope with uncertainty and the lack of control (Rousseau et al., 1998). Given trust’s integral role, scholars have explicitly modeled risk as an important variable in the nomological network of trusting behavior. They have proposed and provided evidence of a negative relationship between risk and trusting intentions (e.g., McKnight et al., 2002b). This finding implies that—ceteris paribus—the higher the level of risk associated with a transaction, the more trusting beliefs will be needed about the other party, given the same level of trusting intentions and trusting behavior. From an information processing perspective, a higher level of risk should interact with individuals’ trust formation efforts as it influences their motivation to seek and process trusting cues. In the context of a dApp, if the level of risk associated with a dApp is higher, users should have a higher need to form trusting beliefs. Consequently, they should also be motivated to process the information about the dApp more thoroughly. As both inductive and deductive information processing should lead to more knowledge, and hence stronger trusting beliefs, if users invest more time and effort, we hypothesize that a higher level of risk associated with a transaction should be linked to a stronger need for trusting beliefs, which consequently goes hand in hand with the increased salience of deduction-related as well as induction-related cues.




风险在个人信任形成过程中发挥着关键作用，因为它首先创造了信任需求。只有当风险存在时，信任才变得重要，因为它可以帮助个人应对不确定性和缺乏控制（Rousseau et al., 1998）。鉴于信任的不可或缺的作用，学者们明确将风险建模为信任行为法理网络中的一个重要变量。他们提出并提供了风险与信任意图之间负相关关系的证据（例如，McKnight 等人，2002b）。这一发现意味着，在其他条件不变的情况下，交易相关的风险水平越高，在信任意图和信任行为相同的情况下，就越需要对对方有更多的信任信念。从信息处理的角度来看，较高水平的风险应该与个人的信任形成努力相互作用，因为它会影响他们寻求和处理信任线索的动机。在 dApp 的背景下，如果与 dApp 相关的风险级别较高，则用户应该更需要形成信任信念。因此，他们也应该有动力更彻底地处理有关 dApp 的信息。由于归纳和演绎的信息处理都应该带来更多的知识，从而产生更强的信任信念，如果用户投入更多的时间和精力，我们假设与交易相关的更高水平的风险应该与对信任信念的更强烈的需求联系起来，从而与演绎相关和归纳相关的线索的显着性增加齐头并进。


H3a: The level of risk associated with a transaction positively moderates the relationship between the possibility of obtaining deductive certainty and the number of users adopting a dApp.




H3a：与交易相关的风险水平正向调节获得演绎确定性的可能性与采用 dApp 的用户数量之间的关系。


H3b: The level of risk associated with a transaction positively moderates the relationship between inductive cues and the number of users adopting a dApp.




H3b：与交易相关的风险水平正向调节归纳线索与采用 dApp 的用户数量之间的关系。


Besides the level of risk, the desire for efficiency in humans trust formation processes suggests that anticipated efforts also influence whether and how users form trust in a dApp. According to the information processing literature (see “dualprocessing,” Fiske & Taylor, 1991; or ELM, Petty & Cacioppo, 1986), the higher the anticipated effort of obtaining certain trust cues, the more likely users will be to deprioritize them in favor of easier-to-process cues. They will only resort to more complex trust-building cues if simple trust-building cues do not sufficiently allow the formation of trusting beliefs. Since the more complex the smart contract, the more time and cognitive effort will be required to deduce a future transaction’s outcome by reading and understanding a smart contract’s source code, we argue that increasing the complexity of a smart contract (i.e., higher cost of achieving deductive certainty) will make people forgo deductive belief formation and rely more on inductive trust cues.<sup>9</sup> This reasoning suggests a moderating effect of the cost of deductive certainty on how the possibility of deductive certainty and inductive cues impact the number of exchange relationships. Thus, we hypothesize:




除了风险水平之外，人类信任形成过程中对效率的渴望表明，预期的努力也会影响用户是否以及如何对 dApp 形成信任。根据信息处理文献（参见“双重处理”，Fiske & Taylor，1991；或 ELM，Petty & Cacioppo，1986），获得某些信任线索的预期努力越高，用户就越有可能降低它们的优先级，转而选择更容易处理的线索。如果简单的信任建立线索不足以形成信任信念，他们只会诉诸更复杂的信任建立线索。由于智能合约越复杂，通过阅读和理解智能合约的源代码来推断未来交易结果所需的时间和认知努力就越多，我们认为，增加智能合约的复杂性（即实现演绎确定性的成本更高）将使人们放弃演绎信念的形成，而更多地依赖归纳信任线索。<sup>9</sup>这一推理表明，演绎确定性的成本对演绎确定性的可能性如何产生调节作用归纳线索影响交换关系的数量。因此，我们假设：


H4a: The cost of achieving deductive certainty negatively moderates the relationship between the possibility of deductive certainty and the number of users adopting a dApp.




H4a：实现演绎确定性的成本负向调节演绎确定性的可能性与采用 dApp 的用户数量之间的关系。


H4b: The cost of achieving deductive certainty positively moderates the relationship between inductive cues and the number of users adopting a dApp.




H4b：实现演绎确定性的成本正向调节归纳线索与采用 dApp 的用户数量之间的关系。


Since we can only measure the effort required to achieve deductive certainty in transactions that allow for the possibility of deductive certainty, we cannot test H4a. Overall, our hypotheses lead to the research model depicted in Figure 2.




由于我们只能衡量在允许演绎确定性可能性的交易中实现演绎确定性所需的努力，因此我们无法测试 H4a。总的来说，我们的假设得出了图 2 所示的研究模型。


## Data and Methods




## 数据和方法


## Research Context




## 研究背景


The empirical context for this study is smart contract-based applications—called dApps—on the Ethereum blockchain. Ethereum was the first blockchain to offer the possibility of running smart contracts. With (as of May 2024) more than 510,000 daily active user accounts,<sup>10</sup> a daily transaction value of over \$10 billion, and a market cap of over \$197 billion, and Ether ETSs approved by the SEC,<sup>11</sup> the Ethereum blockchain is no longer a niche phenomenon and has the potential to meaningfully change online commerce. Though other blockchain platforms, such as EOS or Steem, also offer smart contracts, we prefer the Ethereum blockchain for our context because it offers the largest number of active applications based on smart contracts covering diverse application areas. Furthermore, its built-in programming language (Solidity) and standardized method for deploying and running smart contracts provide a comparable context and institutional environment for all the observation units in our sample.




本研究的实证背景是以太坊区块链上基于智能合约的应用程序（称为 dApp）。以太坊是第一个提供运行智能合约可能性的区块链。截至 2024 年 5 月，以太坊区块链拥有超过 510,000 个每日活跃用户账户、<sup>10</sup> 日交易额超过 100 亿美元、市值超过 1,970 亿美元，以及 SEC 批准的 Ether ETS，<sup>11</sup> 不再是一种小众现象，并且有可能对在线商务产生重大改变。尽管 EOS 或 Steem 等其他区块链平台也提供智能合约，但我们更喜欢以太坊区块链，因为它提供了数量最多的基于智能合约的活跃应用程序，涵盖了不同的应用领域。此外，其内置的编程语言（Solidity）和部署和运行智能合约的标准化方法为我们样本中的所有观察单位提供了可比的背景和制度环境。


To study how trust formation in dApps on Ethereum unfolds, we leveraged features of blockchain technology and smart contracts to create two novel datasets. The main dataset was created at the dApp level, enabling us to investigate how the various trust cues offered by different dApps relate to user adoption. We complemented this dataset with a dApp-based survey in order to come closer to causal claims and to provide evidence that induction-related trust and deduction-related trust are two empirically distinct trusting beliefs originating from different cognitive processes.




为了研究以太坊上的 dApp 中的信任形成如何展开，我们利用区块链技术和智能合约的功能创建了两个新颖的数据集。主要数据集是在 dApp 级别创建的，使我们能够调查不同 dApp 提供的各种信任线索如何与用户采用相关。我们通过基于 dApp 的调查补充了该数据集，以便更接近因果主张，并提供证据证明归纳相关信任和演绎相关信任是源自不同认知过程的两种经验上不同的信任信念。


## DApp Data




## DApp 数据


## Data Collection




## 数据收集


We collected a cross-sectional sample of 536 dApps running on the Ethereum blockchain. The dataset comprised on-chain transaction data to measure a dApp’s adoption and off-chain information regarding the trust cues the dApps offer. To adopt a dApp, users need to enter into a trusting relationship with the dApp provider and their dApp and send a transaction to the dApp’s smart contract. Sending the first transaction to the smart contract requires initial trust and is hence the trusting behavior of interest. Since some dApps allow for deductive certainty by publishing and having their contract’s source code verified, while others do not, and since dApps vary greatly in the inductive trust cues they provide, this setup is well-suited to testing our hypotheses.




我们收集了在以太坊区块链上运行的 536 个 dApp 的横截面样本。该数据集包含用于衡量 dApp 采用情况的链上交易数据以及有关 dApp 提供的信任线索的链下信息。要采用 dApp，用户需要与 dApp 提供商及其 dApp 建立信任关系，并向 dApp 的智能合约发送交易。向智能合约发送第一笔交易需要初始信任，因此是利益信任行为。由于一些 dApp 允许通过发布并验证其合约源代码来实现演绎确定性，而其他 dApp 则不允许，而且由于 dApp 提供的归纳信任线索差异很大，因此这种设置非常适合测试我们的假设。


![](/api/attachments/PHUJTSS5/fulltext/images/2822404e1a09d27bb912c2dd6842bacd75fa70d9f4341b77a3039e432da8a718.jpg)




![](/api/attachments/PHUJTSS5/fulltext/images/2822404e1a09d27bb912c2dd6842bacd75fa70d9f4341b77a3039e432da8a718.jpg)


We retrieved the data from three sources: State of the dApps, Etherscan.io, and Ethereum’s public dataset on Google BigQuery. State of the dApps (www.stateofthedapps.com) is a not-for-profit curated directory of dApps running on various blockchains, focusing on Ethereum. State of the dApps (terminated as of January 2023) was widely acknowledged in the blockchain community and actively supported and used by Vitalik Buterin, co-founder of the Ethereum blockchain.<sup>12</sup> Anyone could enter data in the directory, but the website’s authors controlled quality and integrity. At the time of collection (April 29, 2019), it listed a total of 1,892 Ethereumbased dApps. To be included in our sample, a dApp had to be live at the time of data collection (i.e., running on the Ethereum main net, not on one of its test nets, which excluded 763 projects) and have exactly one smart contract (excluding another 593 projects). The latter condition allowed us to link a smart contract’s adoption to a specific dApp. The dApps in our sample covered five categories: lotteries/games (238, 44.4%), finance (77, 14.4%), high risk (119, 22.1%), social (73, 13.7%), and others (29, 5.4%) (www.stateofthedapps.com, accessed April 11, 2019).




我们从三个来源检索数据：State of the dApps、Etherscan.io 和 Google BigQuery 上的以太坊公共数据集。 State of the dApps (www.stateofthedapps.com) 是一个非营利性的、在各种区块链上运行的 dApp 目录，重点关注以太坊。 State of the dApps（于 2023 年 1 月终止）得到了区块链社区的广泛认可，并得到了以太坊区块链联合创始人 Vitalik Buterin 的积极支持和使用。<sup>12</sup>任何人都可以在目录中输入数据，但网站的作者控制着质量和完整性。截至收集时（2019 年 4 月 29 日），总共列出了 1,892 个基于以太坊的 dApp。要包含在我们的样本中，dApp 必须在数据收集时处于活动状态（即在以太坊主网上运行，而不是在其测试网上运行，其中排除了 763 个项目）并且只有一个智能合约（排除了另外 593 个项目）。后一个条件允许我们将智能合约的采用与特定的 dApp 联系起来。我们样本中的 dApp 涵盖五个类别：彩票/游戏（238 个，44.4%）、金融（77 个，14.4%）、高风险（119 个，22.1%）、社交（73 个，13.7%）和其他（29 个，5.4%）（www.stateofthedapps.com，2019 年 4 月 11 日访问）。


For the first step in data collection, we automatically retrieved online data from three different sources: State of the dApps, Etherscan.io, and Google BigQuery. The first allowed us to identify relevant projects and retrieve high-level data, such as the website link, general project information, and the smart contract address. Etherscan.io (www.etherscan.io), an analytics platform for Ethereum, which is acknowledged as a reliable data source (Fröwis & Böhme, 2017), provided technical details about the smart contract, e.g., whether its source code has been published and verified, the date of deployment, and the smart contract’s source code.<sup>13</sup>




对于数据收集的第一步，我们自动从三个不同来源检索在线数据：State of the dApps、Etherscan.io 和 Google BigQuery。第一个允许我们识别相关项目并检索高级数据，例如网站链接、一般项目信息和智能合约地址。 Etherscan.io (www.etherscan.io) 是以太坊的分析平台，被公认为可靠的数据源（Fröwis & Böhme，2017），提供了有关智能合约的技术细节，例如其源代码是否已发布和验证、部署日期以及智能合约的源代码。<sup>13</sup>


At the transaction level, we used the public Ethereum dataset available on Google BigQuery.<sup>14</sup> To link the off-chain data on our dApps to the on-chain transaction records, we searched all Ethereum blockchain records for transactions sent to the smart contract addresses of the dApps in our sample and aggregated these transactions per dApp.




在交易层面，我们使用了 Google BigQuery 上提供的公共以太坊数据集。<sup>14</sup>为了将 dApp 上的链下数据链接到链上交易记录，我们在所有以太坊区块链记录中搜索发送到样本中 dApp 智能合约地址的交易，并汇总每个 dApp 的这些交易。


Our second step was to manually collect data related to each dApp and rate available inductive trust cues. We used two independent raters for this process. To ensure a common understanding, we derived a framework of relevant inductive cues from the literature on trust formation and online trust formation in particular (e.g., Gefen et al., 2003; Lim et al., 2006; Mayer et al., 1995; McKnight et al., 1998, 2002b). Subsequently, the raters assessed the first 10 dApps, discussed differences, and developed word anchors for each level of all variables.<sup>15</sup> Finally, each rater evaluated all 536 projects. If there was disagreement, we used mean values. The overall interrater reliability of subjective trust cues was acceptable (lowest Cohen’s kappa = 0.799) and consistent with other studies (Grégoire et al., 2010; Mueller & Shepherd, 2016)




我们的第二步是手动收集与每个 dApp 相关的数据，并对可用的归纳信任线索进行评级。我们在这个过程中使用了两名独立的评估者。为了确保达成共识，我们从有关信任形成和网络信任形成的文献中得出了相关归纳线索的框架（例如，Gefen et al., 2003; Lim et al., 2006; Mayer et al., 1995; McKnight et al., 1998, 2002b）。随后，评估者评估了前 10 个 dApp，讨论了差异，并为所有变量的每个级别开发了词锚。<sup>15</sup>最后，每位评估者评估了所有 536 个项目。如果存在分歧，我们使用平均值。主观信任线索的整体受试者间可靠性是可以接受的（最低 Cohen kappa = 0.799），并且与其他研究一致（Grégoire 等人，2010 年；Mueller & Shepherd，2016 年）


## Dependent Variable




## 因变量


Our dependent variable is the number of users who adopted a dApp (i.e., the unique number of users). It reflects the user’s decision to start a new trusting relationship with the party offering the dApp. According to the online trust formation literature (e.g., Kim & Prabhakar, 2002; McKnight et al., 1998; Zhou, 2011), such adoption behavior is only possible if users feel confident enough to make themselves vulnerable to the unknown dApp provider’s actions, hence if users have formed a sufficient level of initial trust.




我们的因变量是采用 dApp 的用户数量（即唯一用户数量）。它反映了用户决定与提供 dApp 的一方建立新的信任关系。根据在线信任形成文献（例如，Kim & Prabhakar，2002；McKnight 等，1998；Zhou，2011），只有当用户有足够的信心使自己容易受到未知 dApp 提供商的行为的影响，因此用户已经形成了足够水平的初始信任时，这种采用行为才有可能。


We calculated the number of unique users by leveraging the fact that all transactions contain a time stamp, sender, and recipient address. To obtain the number of users who adopted a dApp, we counted the unique senders<sup>16</sup> for each smart contract. Since this variable is highly right-skewed, we used its logarithm (Becker et al., 2019). Retrieving the number of unique users from the Ethereum blockchain is not a trivial task, and the number of contract users was not indicated on the company’s website. Hence, herding effects can be excluded.




我们利用所有交易都包含时间戳、发件人和收件人地址这一事实来计算唯一用户的数量。为了获取采用 dApp 的用户数量，我们计算了每个智能合约的唯一发送者<sup>16</sup>。由于该变量高度右偏，因此我们使用其对数（Becker et al., 2019）。从以太坊区块链中检索唯一用户的数量并不是一项简单的任务，并且该公司的网站上没有标明合约用户的数量。因此，可以排除羊群效应。


## Independent Variables and Moderators




## 自变量和调节变量


Induction-related cues: We measured induction-related cues with items commonly used in the literature to capture trusting beliefs (Mayer et al., 1995; McKnight et al., 1998; McKnight & Chervany, 2001). These cues relate to the perceived integrity, benevolence, and ability of the company offering a smart contract and have been confirmed as important by prior empirical research (Mayer & Gavin, 2005). All constructs were rated on a 5-point Likert scale with predefined word anchors for each level. Moreover, we rated perceived usefulness and perceived ease of use and the general website appearance on a 5-point Likert scale, and availability of third-party certificates and structural assurance as dummy variables, since these constructs have also been conceptually linked to trust formation (Gefen et al., 2003; Jiang et al., 2008; McKnight et al., 1998) and validated in the context of e-commerce and mobile banking (McKnight et al., 2002a; Zhou, 2012). Although multicollinearity was only moderately high—the highest variance inflation factor (VIF) was 7.7—we performed an exploratory factor analysis to take into account the theoretical linkages among our constructs, their high correlations, and other scholars’ concerns that results obtained by treating them as separate constructs might be driven by multicollinearity (Mayer & Gavin, 2005). This factor analysis supports a onefactor solution, where all of the above-mentioned variables load on the same factor. Cronbach’s alpha of 0.92 indicates sufficient internal consistency. To construct the factor variable, we used the corresponding variables’ factor scores. Below, we refer to these as inductive cues, as they reflect the inductive way these cues are processed to create induction-related beliefs.




归纳相关线索：我们使用文献中常用的项目来测量归纳相关线索，以捕获信任信念（Mayer et al., 1995; McKnight et al., 1998; McKnight & Chervany, 2001）。这些线索与提供智能合约的公司的诚信、仁慈和能力有关，并且已被先前的实证研究证实非常重要（Mayer & Gavin，2005）。所有结构均按照 5 点李克特量表进行评级，每个级别都有预定义的单词锚点。此外，我们采用 5 点李克特量表对感知有用性、感知易用性和一般网站外观进行评级，并将第三方证书的可用性和结构保证作为虚拟变量，因为这些结构在概念上也与信任形成相关（Gefen 等，2003；Jiang 等，2008；McKnight 等，1998），并在电子商务和移动银行的背景下得到验证（McKnight 等， 2002a；周，2012）。尽管多重共线性只是中等偏高——最高方差膨胀因子（VIF）为 7.7——我们进行了探索性因子分析，以考虑我们的构建之间的理论联系、它们的高度相关性以及其他学者的担忧，即通过将它们视为单独的构建而获得的结果可能是由多重共线性驱动的（Mayer & Gavin，2005）。此因子分析支持单因子解决方案，其中所有上述变量都加载到同一因子上。 Cronbach 的 alpha 值为 0.92，表明有足够的内部一致性。为了构建因子变量，我们使用了相应变量的因子得分。下面，我们将这些称为归纳线索，因为它们反映了处理这些线索以创建与归纳相关的信念的归纳方式。


Verified (smart contract) source code: We captured this dApp characteristic with a binary variable that indicates whether the smart contract’s source code was openly available and verified to match the bytecode running on the blockchain. This is in line with our argument that users can only achieve deductive certainty or form deduction-related trust if a smart contract’s source code is publicly available and verified by a third party as corresponding with the bytecode on the blockchain. We collected this variable based on an Etherscan.io public database, which provides a de facto standardized verification. All dApps in our sample with a verified source code had this verified immediately after deploying the contract on the main net and were only verified on Etherscan.io. Thus, all users of a dApp with a verified source code can rely on the same information.




经过验证的（智能合约）源代码：我们使用二进制变量捕获了此 dApp 特征，该变量指示智能合约的源代码是否公开可用并经过验证以匹配区块链上运行的字节码。这符合我们的论点，即只有智能合约的源代码公开且经第三方验证与区块链上的字节码相对应，用户才能获得演绎确定性或形成与演绎相关的信任。我们根据 Etherscan.io 公共数据库收集了这个变量，该数据库提供了事实上的标准化验证。我们样本中所有具有经过验证源代码的 dApp 在主网上部署合约后立即进行了验证，并且仅在 Etherscan.io 上进行了验证。因此，具有经过验证的源代码的 dApp 的所有用户都可以依赖相同的信息。


Risk associated with the smart contract: We operationalized the risk associated with the relationship using the transaction value as measured by the log of the mean amount of Ether (Ethereum’s internal cryptocurrency) sent to a smart contract for every user’s first transaction. While risk is generally determined by both the amount at stake and the perceived probability of losing it, the latter is unobservable.




与智能合约相关的风险：我们使用交易价值来操作与关系相关的风险，交易价值是通过每个用户第一笔交易发送到智能合约的以太币（以太坊的内部加密货币）平均数量的日志来衡量的。虽然风险通常由风险金额和损失风险的感知概率决定，但后者是不可观察的。


Cost of deductive certainty: To operationalize the cost of attaining deductive certainty, we used the log of the length of the source code, measured by lines of code. We argue that a longer source code is, ceteris paribus, the more it is associated with a greater effort to read and comprehend the code and, hence, with a greater effort to achieve deductive certainty.<sup>17</sup>




演绎确定性的成本：为了具体化获得演绎确定性的成本，我们使用了源代码长度的对数，以代码行数来衡量。我们认为，在其他条件不变的情况下，源代码越长，就越需要付出更大的努力来阅读和理解代码，从而需要付出更大的努力来实现演绎确定性。<sup>17</sup>


## Control Variables




## 控制变量


Besides our main explanatory variables, we controlled for the smart contract’s age and the dApp’s application category. Controlling for age is important, as an older dApp has had more time to attract users. It should also control for any reputation that might form over time. However, given that most dApps in our sample were fairly new at the time of data collection and had not been extensively covered in the media, reputation should not be a concern. We controlled for the dApp’s category, hence industry-specific effects, since entertainment or gaming applications might require a different level of trust than financial services. For a subset of dApps (n = 130), we could not identify a stand-alone website—these dApps were only presented on Stateofthedapp.com. Since those dApps were rated at 1 (the minimum value) for inductive trust cues, we introduced a dummy variable for having a website to account for potential systematic differences.<sup>18</sup> Finally, we controlled for whether the dApp was open source by adding a dummy variable indicating if the dApp operated under an open source or a proprietary license. Our sample comprised dApps under an open source license with a smart contract that was not verified and others under a proprietary license with a smart contract that was verified (44 no OS license and no verified smart contract; 56 only OS license; 192 only verified smart contract but not OS license;<sup>19</sup> 244 OS license and verified smart contract).




除了我们的主要解释变量之外，我们还控制了智能合约的年龄和 dApp 的应用程序类别。控制年龄很重要，因为较旧的 dApp 有更多时间来吸引用户。它还应该控制随着时间的推移可能形成的任何声誉。然而，鉴于我们样本中的大多数 dApp 在数据收集时还相当新，并且尚未被媒体广泛报道，因此声誉不应成为问题。我们控制了 dApp 的类别，从而控制了行业特定的影响，因为娱乐或游戏应用程序可能需要与金融服务不同级别的信任。对于 dApp 的子集（n = 130），我们无法识别独立的网站 - 这些 dApp 仅在 Stateofthedapp.com 上呈现。由于这些 dApp 的归纳信任线索评级为 1（最小值），因此我们引入了一个虚拟变量，以便通过网站来考虑潜在的系统差异。<sup>18</sup>最后，我们通过添加一个虚拟变量来控制 dApp 是否开源，该变量指示 dApp 是在开源许可下运行还是在专有许可下运行。我们的样本包括具有未经验证的智能合约的开源许可下的 dApp，以及具有未经验证的智能合约的专有许可下的其他 dApp（44 个没有操作系统许可，也没有经过验证的智能合约；56 个仅操作系统许可；192 个仅经过验证的智能合约，但没有操作系统许可；<sup>19</sup>244 个操作系统许可和经过验证的智能合约）。


## User Survey




## 用户调查


Our cross-sectional data did not allow for causal claims. For instance, there could have been an omitted variable bias: more thorough dApp providers may be more likely to disclose and verify their source code, as this is good practice, at the same time making them more successful at attracting users. Further, it did not allow us to assess whether induction-related trust and deduction-related trust were empirically distinguishable constructs and the outcome of two different cognitive processes. One could argue that the availability of a verified source code could constitute an additional inductive trust cue. The user survey addresses both issues.




我们的横截面数据不允许因果关系。例如，可能存在遗漏变量偏差：更彻底的 dApp 提供商可能更有可能披露和验证其源代码，因为这是良好的做法，同时使他们更成功地吸引用户。此外，它不允许我们评估归纳相关的信任和演绎相关的信任是否是经验上可区分的结构以及两种不同认知过程的结果。有人可能会说，经过验证的源代码的可用性可能构成额外的归纳信任线索。用户调查解决了这两个问题。


We used a novel survey dApp specifically developed to send questionnaires to dApp users on Ethereum (Weiss & Obermeier, 2021). The survey ran from October 2021 until March 2022, yielding a total of 119 responses. Our respondents ranged in age from 17 to 61, with an average of 31.5. Most had a background in computer science (38%) or engineering (30%) and at least a bachelor’s degree (87%). As Figure 3 depicts, participants varied significantly in their knowledge of blockchain technology and the Ethereum network and in their ability to read smart contract source code. While 21% indicated having no experience in reading Solidity code, 33% rated their ability as advanced or even expert.




我们使用了专门开发的新颖的调查 dApp，用于向以太坊上的 dApp 用户发送调查问卷（Weiss & Obermeier，2021）。该调查从 2021 年 10 月持续到 2022 年 3 月，共收到 119 份回复。我们的受访者年龄从 17 岁到 61 岁不等，平均年龄为 31.5 岁。大多数人拥有计算机科学（38%）或工程学（30%）背景，并且至少拥有学士学位（87%）。如图 3 所示，参与者对区块链技术和以太坊网络的了解以及阅读智能合约源代码的能力存在显着差异。虽然 21% 的人表示没有阅读 Solidity 代码的经验，但 33% 的人认为自己的能力是高级甚至专家。


We asked users about their demographics, experience, and knowledge in the field of blockchain, whether they care about a verified source code, to what extent they usually read the source code when considering interacting with a new dApp, and what the sources of their trusting beliefs are. We relied on the existing trust literature and a series of exploratory expert and user interviews to develop our survey.<sup>20</sup> Related to induction-related trust in the dApp (Construct 1), we asked participants to what extent they look for information about the dApp provider before deciding to transact with a new dApp (IND-extent) and if they would feel confident interacting with a dApp because they perceive the provider to be honest (IND-INT), benevolent (IND-BEN), or competent (IND-ABI). We based these items on the existing literature to ensure content validity. Second, related to deduction-related trust in the dAPP (Construct 2), we first asked our respondents if they care whether the dApp’s smart contract is openly available and verified (e.g., on Etherscan) and, if so, why they care about a verified source code. Afterward, we instructed them to assume that a smart contract is publicly disclosed and verified and asked them to what extent they would read a smart contract’s source code when deciding whether to interact with a new dapp (ded-extent) and if they would feel confident interacting with the dApp because they could read the source code if they wanted to (dedpos), because they could read the source code to see what it does (ded-read1), because the could read the source code to understand that it does what it is supposed to do (ded-read2), or because they could read the source code to ascertain that it is free from mistakes (ded-read3). Finally, we asked our participants questions related to potential trust stemming from the blockchain periphery itself (Construct 3). We asked them if they would feel confident interacting with a new dApp because the blockchain automatically executes the transactions (BC-AUT), because the blockchain ensures the immutability of records (BC-IMM), or because, on a blockchain, stored data is transparent (BC-TRA).<sup>21</sup>




我们询问了用户在区块链领域的人口统计、经验和知识，他们是否关心经过验证的源代码，在考虑与新的 dApp 交互时通常会在多大程度上阅读源代码，以及他们的信任信念的来源是什么。我们依靠现有的信任文献以及一系列探索性专家和用户访谈来开展我们的调查。<sup>20</sup>与 dApp 中感应相关的信任（构建 1）相关，我们询问参与者在决定与新 dApp 进行交易之前在多大程度上寻找有关 dApp 提供商的信息（IND 范围），以及他们是否因为认为提供商是诚实的 (IND-INT)、仁慈而有信心与 dApp 交互(IND-BEN) 或主管 (IND-ABI)。我们将这些项目基于现有文献，以确保内容的有效性。其次，与 dAPP 中与演绎相关的信任相关（构造 2），我们首先询问受访者是否关心 dApp 的智能合约是否公开可用并经过验证（例如，在 Etherscan 上），如果是，为什么他们关心经过验证的源代码。之后，我们指示他们假设智能合约是公开披露和验证的，并询问他们在决定是否与新的 dapp 交互时会在多大程度上阅读智能合约的源代码 (ded-extent)，以及他们是否有信心与 dApp 交互，因为如果他们愿意，他们可以阅读源代码 (dedpos)，因为他们可以阅读源代码来了解它的作用 (ded-read1)，因为他们可以阅读源代码以了解它做了它应该做的事情（ded-read2），或者因为他们可以阅读源代码以确定它没有错误（ded-read3）。最后，我们向参与者询问了与区块链外围本身产生的潜在信任相关的问题（结构 3）。我们询问他们是否有信心与新的 dApp 交互，因为区块链会自动执行交易 (BC-AUT)，因为区块链确保记录的不变性 (BC-IMM)，或者因为在区块链上存储的数据是透明的 (BC-TRA)。<sup>21</sup>


Figure 3. Survey Respondents’ Blockchain Knowledge




图 3. 调查受访者的区块链知识


![](/api/attachments/PHUJTSS5/fulltext/images/1e9649a5fcf8b7eda62bdce03e959252317f63b306431243e41771ab14f8d27e.jpg)




![](/api/attachments/PHUJTSS5/fulltext/images/1e9649a5fcf8b7eda62bdce03e959252317f63b306431243e41771ab14f8d27e.jpg)


![](/api/attachments/PHUJTSS5/fulltext/images/7697cf4154da58b4b8ff457e54360c5fbae084cfe0dbc4043aef1ebf833e9b22.jpg)




![](/api/attachments/PHUJTSS5/fulltext/images/7697cf4154da58b4b8ff457e54360c5fbae084cfe0dbc4043aef1ebf833e9b22.jpg)


![](/api/attachments/PHUJTSS5/fulltext/images/56dd2708acc1799f2cf91faf354f49a7526ee1d6dbc73aeee527461428897d95.jpg)  
Ability to read Solidity code (n=119) % of respondents  
NO = No experience; Beg = Beginner; Int = Intermediate; Adv = Advanced; Exp = Expert




![](/api/attachments/PHUJTSS5/fulltext/images/56dd2708acc1799f2cf91faf354f49a7526ee1d6dbc73aeee527461428897d95.jpg)  
能够阅读 Solidity 代码 (n=119) 受访者百分比  
NO = 没有经验；乞求=初学者； Int = 中级； Adv = 高级；经验 = 专家


<table><tr><td colspan="6">Table 1. Goodness of Fit CFA Models</td></tr><tr><td>Construct</td><td>Model</td><td> $\chi^2/df$ </td><td>CFI</td><td>TLI</td><td>RMSEA</td></tr><tr><td>Model 1</td><td>One factor model</td><td>3.88</td><td>0.56</td><td>0.47</td><td>0.16</td></tr><tr><td>Model 2</td><td>Two-factor model (induction-related trust)</td><td>1.82</td><td>0.91</td><td>0.87</td><td>0.08</td></tr><tr><td>Model 3</td><td>Two-factor model (deduction-related trust)</td><td>2.16</td><td>0.87</td><td>0.82</td><td>0.10</td></tr><tr><td>Model 4</td><td>Theoretically predicted model</td><td>1.15</td><td>0.98</td><td>0.98</td><td>0.07</td></tr></table>




<table><tr><td colspan="6">表 1. 拟合优度 CFA 模型</td></tr><tr><td>构造</td><td>模型</td><td> $\chi^2/df$ </td><td>CFI</td><td>TLI</td><td>RMSEA</td></tr><tr><td>模型1</td><td>单因素模型</td><td>3.88</td><td>0.56</td><td>0.47</td><td>0.16</td></tr><tr><td>模型2</td><td>双因素模型（归纳相关）信任）</td><td>1.82</td><td>0.91</td><td>0.87</td><td>0.08</td></tr><tr><td>模型3</td><td>双因素模型（扣除相关）信任）</td><td>2.16</td><td>0.87</td><td>0.82</td><td>0.10</td></tr><tr><td>模型4</td><td>理论预测型号</td><td>1.15</td><td>0.98</td><td>0.98</td><td>0.07</td></tr></table>


## Findings




## 调查结果


## Construct Validity




## 构造有效性


To empirically corroborate our conjecture that deductionrelated trust cues lead to a new type of trust and are not just another signal users rely on in an inductive process, we present results of a confirmatory factor analysis (CFA) based on our survey data demonstrating that deduction-related trust is a distinct construct describing a deductive process.<sup>22</sup> The Kaiser-Meyer-Olkin test (KMO 0.7) for sampling adequacy and Bartlett’s Test of Sphericity (p < 0.001) indicated that our data was suited for factor analysis (Gorsuch, 2014).<sup>23</sup> We computed different models to compare our theoretically predicted factors to alternatives. In Model 1, we loaded all items on one factor. For Model 2, we loaded all items related to construct 1 (IND-X) on one factor and all others on a second. For Model 3, we loaded all items related to construct 2 (DED-X) on one factor and all others on another. Model 4 is our theoretically predicted model comprising all three constructs. Table 1 reports the comparison.




为了从经验上证实我们的猜想，即与演绎相关的信任线索会导致一种新型信任，而不仅仅是用户在归纳过程中依赖的另一个信号，我们根据调查数据提出了验证性因子分析 (CFA) 的结果，证明与演绎相关的信任是描述演绎过程的独特构造。<sup>22</sup>Kaiser-Meyer-Olkin 检验 (KMO 0.7)，用于抽样充分性和Bartlett 球形度检验 (p < 0.001) 表明我们的数据适合进行因子分析（Gorsuch，2014）。<sup>23</sup>我们计算了不同的模型，以将理论上预测的因子与替代因子进行比较。在模型 1 中，我们将所有项目加载到一个因子上。对于模型 2，我们在一个因素上加载与构造 1 (IND-X) 相关的所有项目，在第二个因素上加载所有其他项目。对于模型 3，我们在一个因素上加载与构造 2 (DED-X) 相关的所有项目，在另一因素上加载所有其他项目。模型 4 是我们理论上预测的模型，包含所有三个结构。表 1 报告了比较结果。


Appropriate values of χ<sup>2</sup>/df should exceed 1 and be less than 5 (Salisbury et al., 2002). The Comparative Fit Index (CFI) and Tucker-Lewis Index (TLI) should exceed 0.9 (Salisbury et al., 2002). A root mean square error of the approximation (RMSEA) measuring a misspecification smaller than 0.05 is considered a good fit, smaller than 0.08 a reasonable fit, and exceeding 0.1 a poor fit (Kline, 2016). Only our theoretically predicted model (Model 4) fulfilled all goodness-of-fit criteria. This provides evidence that induction-related trust, deductionrelated trust, and trust in the blockchain periphery are distinct latent constructs.




χ<sup>2</sup>/df 的适当值应大于 1 且小于 5（Salisbury 等人，2002）。比较拟合指数 (CFI) 和 Tucker-Lewis 指数 (TLI) 应超过 0.9（Salisbury 等，2002）。测量错误指定的近似均方根误差 (RMSEA) 小于 0.05 被认为是良好拟合，小于 0.08 被认为是合理拟合，超过 0.1 被认为是较差拟合（Kline，2016）。只有我们的理论预测模型（模型 4）满足所有拟合优度标准。这提供了证据，证明与归纳相关的信任、与演绎相关的信任以及区块链外围的信任是不同的潜在构造。


To assess the discriminant validity of our three factors, we followed Rönkkö and Cho (2022), using their R function “discriminantValidity” from the semTool package to assess the correlations between our factors. The estimates of correlations were small in absolute value (the maximum being 0.23), and the ends of the 95% confidence intervals were sufficiently far away in absolute value from the suggested cut-off of 0.9 (the maximum being 0.52). Thus, our data support the discriminant validity of our proposed factors.




为了评估三个因素的判别有效性，我们遵循 Rönkkö 和 Cho (2022)，使用 semTool 包中的 R 函数“discriminantValidity”来评估因素之间的相关性。相关性估计值的绝对值很小（最大值为 0.23），并且 95% 置信区间的末端的绝对值与建议的截止值 0.9（最大值为 0.52）相差足够远。因此，我们的数据支持我们提出的因素的判别有效性。


We point out that the construct of deduction-related trust is clearly about deduction. This is reflected in the wording of its items and is further supported by descriptive evidence from the survey. Of our respondents, 54% indicated that they care about a verified source code “because I want to read it.” Regarding their ability to read Solidity code, 57% ticked intermediate or better (21% advanced, 12% expert). Furthermore, 49% stated that they seek to obtain at least a basic understanding of the source code. 18% reported that they attempt to gain at least an in-depth understanding, and another 5% reported conducting thorough security screenings. Thus, a considerable share of respondents reported that they seek to build firsthand deduction-related trust or even deductive certainty, are capable of doing so, and invest time to this end. They thus offer a basis for others to form secondhand deduction-related trust.




我们指出，与演绎相关的信任的构造显然是关于演绎的。这反映在其项目的措辞中，并得到调查的描述性证据的进一步支持。在我们的受访者中，54% 表示他们关心经过验证的源代码“因为我想阅读它”。关于阅读 Solidity 代码的能力，57% 的人选择中级或更好（21% 为高级，12% 为专家）。此外，49% 的人表示他们寻求至少对源代码有基本的了解。 18% 的人表示他们试图至少深入了解，另外 5% 的人表示进行了彻底的安全检查。因此，相当一部分受访者表示，他们寻求建立与演绎相关的第一手信任甚至演绎确定性，有能力这样做，并为此投入时间。因此，它们为其他人形成与二手扣除相关的信任提供了基础。


## DApp-Level Analysis




## DApp 层面分析


Table 2 presents descriptive statistics and correlations. We tested our hypotheses with a moderated OLS multiple regression analysis. Table 3 shows our regression models. Model 1 is a control model; Model 2 adds the direct effects of offering the possibility of deductive certainty (i.e., having a verified source code) and the factor comprising all inductive cues; Model 3 adds the interactions with transaction value, our proxy for risk associated with the transaction; and Model 4 adds an interaction between the direct effects to assess whether the possibility of deductive certainty and inductive cues are complements. Finally, in Models 5 and 6, we analyzed only dApps (n = 434) with a verified source code since the length of code, our measurement for the cost of attaining deductive certainty, can only be observed for those dApps. Accordingly, in Model 5, we introduced the length of code as a control variable, and in Model 6, we added the interaction of the length of code with inductive trust cues.<sup>24</sup>




表 2 列出了描述性统计数据和相关性。我们通过有调节的 OLS 多元回归分析检验了我们的假设。表 3 显示了我们的回归模型。模型1为控制模型；模型 2 增加了提供演绎确定性可能性（即拥有经过验证的源代码）的直接影响以及包含所有归纳线索的因素；模型 3 添加了与交易价值的交互，交易价值是与交易相关的风险代理；模型4增加了直接效应之间的相互作用，以评估演绎确定性和归纳线索的可能性是否是互补的。最后，在模型 5 和 6 中，我们仅分析了具有经过验证的源代码的 dApp (n = 434)，因为代码长度（我们对获得演绎确定性的成本的衡量标准）只能在这些 dApp 中观察到。相应地，在模型 5 中，我们引入了代码长度作为控制变量，在模型 6 中，我们添加了代码长度与归纳信任线索的交互作用。<sup>24</sup>


H1, predicting that a higher level of inductive cues is associated with a higher number of exchange relationships, is supported (Models 2, 3, 5, p < 0.001, Model 4, p < 0.05). Based on the coefficient in Model 2, increasing the factor score by one unit is associated with a 63.2% increase in the number of exchange relationships.




H1 预测更高水平的归纳线索与更多数量的交换关系相关，得到支持（模型 2、3、5，p < 0.001，模型 4，p < 0.05）。根据模型 2 中的系数，因子得分增加 1 个单位与交换关系数量增加 63.2% 相关。


Our results in Models 2 to 4 also support H2 (p < 0.001), which predicts that a disclosed and verified smart contract source code will be positively associated with user adoption. Based on the coefficient in Model 2, offering users a verified source code and thus the possibility to form deduction-related trust was associated with a 71% increase in the number of new users.




我们在模型 2 至 4 中的结果也支持 H2 (p < 0.001)，它预测公开和验证的智能合约源代码将与用户采用呈正相关。根据模型2中的系数，为用户提供经过验证的源代码，从而形成与扣除相关的信任的可能性与新用户数量增加71%相关。


H3a predicts a positive moderating effect of transaction value (our measurement of risk) on the association between a verified source code and user adoption. In Models 3 and 4, we found weak support for this hypothesis (p = 0.049 and $p = 0 . 0 6 5$ respectively).




H3a 预测交易价值（我们的风险衡量）对经过验证的源代码和用户采用之间的关联具有积极的调节作用。在模型 3 和模型 4 中，我们发现对这一假设的支持较弱（分别为 p = 0.049 和 $p = 0 . 0 6 5$）。


H3b predicts a positive moderating effect of transaction value on the association between inductive cues and adoption. However, the interaction coefficient was significant and negative in Models 3, 4, and 6, suggesting a negative moderation. As Figure 4 (left panel) illustrates, the association between inductive cues and the number of unique users was weaker for dApps with higher average transaction values.




H3b 预测交易价值对归纳线索和采用之间的关联具有积极的调节作用。然而，模型 3、4 和 6 中的交互系数显着且为负，表明存在负调节。如图 4（左图）所示，对于平均交易价值较高的 dApp，归纳线索与唯一用户数量之间的关联较弱。


H4a could not be tested with our data because having a verified source code operationalizes deduction-related trust.




H4a 无法用我们的数据进行测试，因为拥有经过验证的源代码可以操作与推导相关的信任。


H4b predicts a positive moderation of the length of code (cost of deductive certainty) on the association between inductive cues and user adoption. The regression coefficient was insignificant, so we could not reject the null hypothesis.




H4b 预测代码长度（演绎确定性成本）对归纳线索和用户采用之间的关联有积极的调节。回归系数不显着，因此我们不能拒绝零假设。


While we did not explicitly hypothesize complementarity between inductive cues and the possibility of deductive certainty, a positive and significant interaction (p < 0.001, Model 4) would suggest they complement each other. With a disclosed and verified source code, the association of inductive trust with user adoption was stronger. This finding is depicted in Figure 4 (right panel).




虽然我们没有明确假设归纳线索和演绎确定性的可能性之间的互补性，但积极且显着的相互作用（p < 0.001，模型 4）表明它们是相互补充的。通过公开和验证的源代码，归纳信任与用户采用的关联性更强。图 4（右图）描述了这一发现。


## Robustness Tests




## 稳健性测试


We conducted several robustness tests to control for peculiarities in our dataset.




我们进行了几次稳健性测试来控制数据集中的特殊性。


## Only dApps With Websites




## 仅具有网站的 dApp


Not all dApps listed on Stateofthedapp.com had a separate website allowing users to read about the dApp and form induction-related beliefs. DApps with no website had fewer users on average (mean<sub>site</sub> <sub>available</sub> = 3359; mean <sub>no</sub> <sub>site</sub> = 237; twosided t-test: p < 0.01). To account for this potential bias, we reran our analysis with a restricted sample of only dApps with a website (n = 406). We found support for H1 and H2; the complementarity term remained positive and significant in Model 3. All other interaction terms kept their sign but were no longer significant.




并非 Stateofthedapp.com 上列出的所有 dApp 都有一个单独的网站，允许用户阅读有关 dApp 的信息并形成与归纳相关的信念。没有网站的 DApp 平均用户较少（平均<sub>site</sub> <sub>available</sub> = 3359；平均<sub>no</sub> <sub>site</sub> = 237；双向 t 检验：p < 0.01）。为了解决这种潜在偏差，我们仅使用带有网站的 dApp 的有限样本重新进行分析（n = 406）。我们找到了对 H1 和 H2 的支持；模型 3 中的互补项仍然为正且显着。所有其他交互项保持其符号，但不再显着。


<table><tr><td colspan="19">Table 2. Summary Statistics and Correlations of dApp Data</td></tr><tr><td>Variables</td><td>N</td><td>Mean</td><td>SD</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>1. Log of new relationships</td><td>536</td><td>1.65</td><td>1.12</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Verified code</td><td>536</td><td>0.81</td><td>0.39</td><td>0.25***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Integrity rating</td><td>536</td><td>2.01</td><td>1.22</td><td>0.29***</td><td>0.04</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Benevolence rating</td><td>536</td><td>2.14</td><td>1.24</td><td>0.23***</td><td>-0.002</td><td>0.75***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Ability rating</td><td>536</td><td>1.98</td><td>1.29</td><td>0.30***</td><td>0.05</td><td>0.89***</td><td>0.74***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. Perceived usefulness</td><td>536</td><td>1.85</td><td>1.28</td><td>0.22***</td><td>-0.04</td><td>0.76***</td><td>0.82***</td><td>0.79***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7. Perceived ease of use</td><td>536</td><td>2.22</td><td>1.24</td><td>0.27***</td><td>0.06</td><td>0.82***</td><td>0.75***</td><td>0.83***</td><td>0.73***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8. Website appearance</td><td>536</td><td>0.00</td><td>0.98</td><td>0.29***</td><td>0.06</td><td>0.80***</td><td>0.76***</td><td>0.84***</td><td>0.76***</td><td>0.83***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9. Third-party certificates</td><td>536</td><td>0.08</td><td>0.28</td><td>0.30***</td><td>0.09**</td><td>0.41***</td><td>0.38***</td><td>0.44***</td><td>0.44***</td><td>0.38***</td><td>0.41***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10. Structural assurance</td><td>536</td><td>0.05</td><td>0.22</td><td>0.12***</td><td>0.04</td><td>0.32***</td><td>0.28***</td><td>0.36***</td><td>0.35***</td><td>0.29***</td><td>0.31***</td><td>0.48***</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11. Inductive cues (Factor)</td><td>536</td><td>2.27</td><td>1.36</td><td>0.29***</td><td>0.05</td><td>0.91***</td><td>0.87***</td><td>0.93***</td><td>0.86***</td><td>0.91***</td><td>0.92***</td><td>0.44***</td><td>0.35***</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>12. Website available</td><td>536</td><td>0.76</td><td>0.43</td><td>0.14***</td><td>0.06</td><td>0.51***</td><td>0.56***</td><td>0.48***</td><td>0.45***</td><td>0.56***</td><td>0.55***</td><td>0.17***</td><td>0.13***</td><td>0.61***</td><td>1</td><td></td><td></td><td></td></tr><tr><td>13. Age</td><td>536</td><td>16.35</td><td>5.14</td><td>0.19***</td><td>0.04</td><td>0.17***</td><td>0.28***</td><td>0.18***</td><td>0.28***</td><td>0.16***</td><td>0.15***</td><td>0.18***</td><td>0.10***</td><td>0.21***</td><td>0.10**</td><td>1</td><td></td><td></td></tr><tr><td>14. Log of transaction value</td><td>536</td><td>0.05</td><td>0.14</td><td>0.13***</td><td>0.11***</td><td>-0.15***</td><td>-0.22***</td><td>-0.15***</td><td>-0.18***</td><td>-0.12***</td><td>-0.10**</td><td>-0.12***</td><td>-0.22***</td><td>-0.17***</td><td>-0.11***</td><td>-0.24***</td><td>1</td><td></td></tr><tr><td>15. OS license</td><td>536</td><td>0.56</td><td>0.50</td><td>-0.13***</td><td>0.0003</td><td>-0.21***</td><td>-0.10**</td><td>-0.22***</td><td>-0.15***</td><td>-0.13***</td><td>-0.18***</td><td>-0.15***</td><td>-0.14***</td><td>-0.18***</td><td>-0.07*</td><td>0.09**</td><td>0.01</td><td>1</td></tr><tr><td>16. Length of code</td><td>434</td><td>2.59</td><td>0.38</td><td>0.18***</td><td>n/a</td><td>0.15***</td><td>0.02</td><td>0.15***</td><td>0.09**</td><td>0.10**</td><td>0.12***</td><td>0.13***</td><td>0.01</td><td>0.11**</td><td>-0.03</td><td>-0.14***</td><td>0.15</td><td>-0.01</td></tr></table>




<table><tr><td colspan="19">表 2. dApp 的汇总统计数据和相关性数据</td></tr><tr><td>变量</td><td>N</td><td>均值</td><td>SD</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td> <td>6</td><td>7</td><td>8</td><td>9</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>1。新的日志关系</td><td>536</td><td>1.65</td><td>1.12</td><td>1</td><td></td><td></td><td></td><td></td>< td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2.已验证代码</td><td>536</td><td>0.81</td><td>0.39</td><td>0.25***</td><td>1</td><td></td><td></td><td></td><t d></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3.诚信评分</td><td>536</td><td>2.01</td><td>1.22</td><td>0.29***</td><td>0.04</td><td>1</td><td></td><td></td ><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4.仁爱评分</td><td>536</td><td>2.14</td><td>1.24</td><td>0.23***</td><td>-0.002</td><td>0.75***</td><td>1</td><td> </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5.能力评分</td><td>536</td><td>1.98</td><td>1.29</td><td>0.30***</td><td>0.05</td><td>0.89***</td><td>0.74***</td><t d>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6.感知有用性</td><td>536</td><td>1.85</td><td>1.28</td><td>0.22***</td><td>-0.04</td><td>0.76***</td><td>0.82***</td><td >0.79***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7.感知的轻松程度使用</td><td>536</td><td>2.22</td><td>1.24</td><td>0.27***</td><td>0.06</td><td>0.82***</td><td>0.75***</td><td>0.83*** </td><td>0.73***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8.网站外观</td><td>536</td><td>0.00</td><td>0.98</td><td>0.29***</td><td>0.06</td><td>0.80***</td><td>0.76***</td><td>0.84*** </td><td>0.76***</td><td>0.83***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9.第三方证书</td><td>536</td><td>0.08</td><td>0.28</td><td>0.30***</td><td>0.09**</td><td>0.41***</td><td>0.38***</td><td>0.44***</ td><td>0.44***</td><td>0.38***</td><td>0.41***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10。结构性保证</td><td>536</td><td>0.05</td><td>0.22</td><td>0.12***</td><td>0.04</td><td>0.32***</td><td>0.28***</td><td>0.36***</td><td >0.35***</td><td>0.29***</td><td>0.31***</td><td>0.48***</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11。归纳线索（系数）</td><td>536</td><td>2.27</td><td>1.36</td><td>0.29***</td><td>0.05</td><td>0.91***</td><td>0.87***</td><td>0.93***</td><td>0.8 6***</td><td>0.91***</td><td>0.92***</td><td>0.44***</td><td>0.35***</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>12。网站可用</td><td>536</td><td>0.76</td><td>0.43</td><td>0.14***</td><td>0.06</td><td>0.51***</td><td>0.56***</td><td>0.48***</td><td>0.45** *</td><td>0.56***</td><td>0.55***</td><td>0.17***</td><td>0.13***</td><td>0.61***</td><td>1</td><td></td><td></td><td></td></tr><tr><td>13。年龄</td><td>536</td><td>16.35</td><td>5.14</td><td>0.19***</td><td>0。 04</td><td>0.17***</td><td>0.28***</td><td>0.18***</td><td>0.28***</td ><td>0.16***</td><td>0.15***</td><td>0.18***</td><td>0.10***</td><td>0 .21***</td><td>0.10**</td><td>1</td><td></td><td></td></tr><tr><td>14。交易日志值</td><td>536</td><td>0.05</td><td>0.14</td><td>0.13***</td><td>0.11*** </td><td>-0.15***</td><td>-0.22***</td><td>-0.15***</td><td>-0.18***</td><t d>-0.12***</td><td>-0.10**</td><td>-0.12***</td><td>-0.22***</td><td>-0.17* **</td><td>-0.11***</td><td>-0.24***</td><td>1</td><td></td></tr><tr><td>15。操作系统
许可证</td><td>536</td><td>0.56</td><td>0.50</td><td>-0.13***</td><td>0.00 03</td><td>-0.21***</td><td>-0.10**</td><td>-0.22***</td><td>-0.15***</td><t d>-0.13***</td><td>-0.18***</td><td>-0.15***</td><td>-0.14***</td><td>-0.18* **</td><td>-0.07*</td><td>0.09**</td><td>0.01</td><td>1</td></tr><tr><td>16。长度代码</td><td>434</td><td>2.59</td><td>0.38</td><td>0.18***</td><td>不适用</td><td>0.15***</td><td>0.02</td><td>0.15***</td><td>0.09**</td><td>0 .10**</td><td>0.12***</td><td>0.13***</td><td>0.01</td><td>0.11**</td> <td>-0.03</td><td>-0.14***</td><td>0.15</td><td>-0.01</td></tr></table>


Note:\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.0




注：\*p < 0.1； \*\*p < 0.05； \*\*\*p < 0.0


<table><tr><td colspan="7">Table 3. Regression Results</td></tr><tr><td>Variable</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5(verified only)</td><td>Model 6(verified only)</td></tr><tr><td colspan="7">Deduction-related trust</td></tr><tr><td>Verified source code</td><td></td><td>0.54*** (0.11)</td><td>0.49*** (0.11)</td><td>0.50*** (0.11)</td><td></td><td></td></tr><tr><td colspan="7">Induction-related trust</td></tr><tr><td>Inductive cues</td><td></td><td>0.46*** (0.05)</td><td>0.49*** (0.05)</td><td>0.18* (0.10)</td><td>0.50*** (0.06)</td><td>0.46 (0.32)</td></tr><tr><td colspan="7">Interactions</td></tr><tr><td>Verified code × Transaction value</td><td></td><td></td><td>1.13* (0.59)</td><td>1.05* (0.58)</td><td></td><td></td></tr><tr><td>Inductive trust cues × Transaction value</td><td></td><td></td><td>-0.50** (0.22)</td><td>-0.44** (0.22)</td><td>-0.44 (0.30)</td><td>-0.44 (0.30)</td></tr><tr><td>Inductive trust cues × Length of code</td><td></td><td></td><td></td><td></td><td></td><td>0.01 (0.12)</td></tr><tr><td>Inductive trust cues × Verified code</td><td></td><td></td><td></td><td>0.37*** (0.10)</td><td></td><td></td></tr><tr><td colspan="7">Controls</td></tr><tr><td>Transaction value</td><td>0.79** (0.31)</td><td>0.66** (0.29)</td><td>0.18 (0.43)</td><td>0.19 (0.42)</td><td>1.10*** (0.40)</td><td>1.10*** (0.40)</td></tr><tr><td>Open-source license</td><td>-0.37*** (0.09)</td><td>-0.22*** (0.08)</td><td>-0.21** (0.08)</td><td>-0.19** (0.08)</td><td>-0.23*** (0.09)</td><td>-0.23*** (0.09)</td></tr><tr><td>Website available</td><td>0.31*** (0.10)</td><td>-0.17 (0.11)</td><td>-0.16 (0.11)</td><td>-0.15 (0.11)</td><td>-0.10 (0.11)</td><td>-0.10 (0.11)</td></tr><tr><td>Category: Games</td><td>-0.44*** (0.14)</td><td>-0.22* (0.13)</td><td>-0.21* (0.13)</td><td>-0.20 (0.13)</td><td>-0.26* (0.14)</td><td>-0.26* (0.14)</td></tr><tr><td>Category: High risk</td><td>-0.05 (0.15)</td><td>0.20 (0.15)</td><td>0.19 (0.15)</td><td>0.21 (0.14)</td><td>0.18 (0.15)</td><td>0.18 (0.15)</td></tr><tr><td>Category: Other</td><td>-0.35 (0.22)</td><td>-0.29 (0.20)</td><td>-0.29 (0.20)</td><td>-0.30 (0.20)</td><td>-0.02 (0.24)</td><td>-0.02 (0.24)</td></tr><tr><td>Category: Social</td><td>-0.49*** (0.17)</td><td>-0.35** (0.15)</td><td>-0.35** (0.15)</td><td>-0.36** (0.15)</td><td>-0.50*** (0.17)</td><td>-0.50*** (0.17)</td></tr><tr><td>Age</td><td>0.07*** (0.01)</td><td>0.05*** (0.01)</td><td>0.05*** (0.01)</td><td>0.05*** (0.01)</td><td>0.07*** (0.01)</td><td>0.07*** (0.01)</td></tr><tr><td>Length of code</td><td></td><td></td><td></td><td></td><td>0.32*** (0.12)</td><td>0.32*** (0.12)</td></tr><tr><td>Constant</td><td>0.76*** (0.23)</td><td>0.68*** (0.22)</td><td>0.68*** (0.22)</td><td>0.65*** (0.21)</td><td>0.09 (0.40)</td><td>0.09 (0.40)</td></tr><tr><td>Observations</td><td>536</td><td>536</td><td>536</td><td>536</td><td>434</td><td>434</td></tr><tr><td> $R^2$ </td><td>0.19</td><td>0.33</td><td>0.34</td><td>0.35</td><td>0.40</td><td>0.40</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.18</td><td>0.32</td><td>0.32</td><td>0.34</td><td>0.39</td><td>0.39</td></tr><tr><td>Residual SE</td><td>1.01(df = 527)</td><td>0.92(df = 525)</td><td>0.92(df = 523)</td><td>0.91(df = 522)</td><td>0.87(df = 422)</td><td>0.87(df = 421)</td></tr><tr><td>F-statistic</td><td>15.36*** (df = 8; 527)</td><td>25.76*** (df = 10; 525)</td><td>22.29*** (df = 12; 523)</td><td>22.06*** (df = 13; 522)</td><td>26.06*** (df = 11; 422)</td><td>23.83*** (df = 12; 421)</td></tr></table>




<table><tr><td colspan="7">表 3. 回归结果</td></tr><tr><td>变量</td><td>模型 1</td><td>模型 2</td><td>模型 3</td><td>模型 4</td><td>模型 5（仅经过验证）</td><td>模型 6（经过验证）仅）</td></tr><tr><td colspan="7">推导相关信任</td></tr><tr><td>经过验证的源代码</td><td></td><td>0.54*** (0.11)</td><td>0.49*** (0.11)</td><td>0.50*** (0.11)</td><td></td><td></td></tr><tr><td colspan="7">感应相关信任</td></tr><tr><td>感应线索</td><td></td><td>0.46*** (0.05)</td><td>0.49*** (0.05)</td><td>0.18* (0.10)</td><td>0.50*** (0.06)</td><td>0.46 (0.32)</td></tr><tr><td colspan="7">互动</td></tr><tr><td>验证码 × 交易值</td><td></td><td></td><td>1.13* (0.59)</td><td>1.05* (0.58)</td><td></td><td></td></tr><tr><td>归纳信任线索×交易值</td><td></td><td></td><td>-0.50** (0.22)</td><td>-0.44** (0.22)</td><td>-0.44 (0.30)</td><td>-0.44 (0.30)</td></tr><tr><td>归纳信任线索×长度代码</td><td></td><td></td><td></td><td></td><td></td><td>0.01 (0.12)</td></tr><tr><td>归纳信任线索 × 已验证代码</td><td></td><td></td><td></td><td>0.37*** (0.10)</td><td></td><td></td></tr><tr><td colspan="7">控件</td></tr><tr><td>交易价值</td><td>0.79** (0.31)</td><td>0.66** (0.29)</td><td>0.18 (0.43)</td><td>0.19 (0.42)</td><td>1.10*** (0.40)</td><td>1.10*** (0.40)</td></tr><tr><td>开源许可证</td><td>-0.37*** (0.09)</td><td>-0.22*** (0.08)</td><td>-0.21** (0.08)</td><td>-0.19** (0.08)</td><td>-0.23*** (0.09)</td><td>-0.23*** (0.09)</td></tr><tr><td>网站可用</td><td>0.31*** (0.10)</td><td>-0.17 (0.11)</td><td>-0.16 (0.11)</td><td>-0.15 (0.11)</td><td>-0.10 (0.11)</td><td>-0.10 (0.11)</td></tr><tr><td>类别：游戏</td><td>-0.44*** (0.14)</td><td>-0.22* (0.13)</td><td>-0.21* (0.13)</td><td>-0.20 (0.13)</td><td>-0.26* (0.14)</td><td>-0.26* (0.14)</td></tr><tr><td>类别：高风险</td><td>-0.05 (0.15)</td><td>0.20 (0.15)</td><td>0.19 (0.15)</td><td>0.21 (0.14)</td><td>0.18 (0.15)</td><td>0.18 (0.15)</td></tr><tr><td>类别：其他</td><td>-0.35 (0.22)</td><td>-0.29 (0.20)</td><td>-0.29 (0.20)</td><td>-0.30 (0.20)</td><td>-0.02 (0.24)</td><td>-0.02 (0.24)</td></tr><tr><td>类别：社交</td><td>-0.49*** (0.17)</td><td>-0.35** (0.15)</td><td>-0.35** (0.15)</td><td>-0.36** (0.15)</td><td>-0.50*** (0.17)</td><td>-0.50*** (0.17)</td></tr><tr><td>年龄</td><td>0.07*** (0.01)</td><td>0.05*** (0.01)</td><td>0.05*** (0.01)</td><td>0.05*** (0.01)</td><td>0.07*** (0.01)</td><td>0.07*** (0.01)</td></tr><tr><td>代码长度</td><td></td><td></td><td></td><td></td><td>0.32*** (0.12)</td><td>0.32*** (0.12)</td></tr><tr><td>常数</td><td>0.76*** (0.23)</td><td>0.68*** (0.22)</td><td>0.68*** (0.22)</td><td>0.65*** (0.21)</td><td>0.09 (0.40)</td><td>0.09 (0.40)</td></tr><tr><td>观测值</td><td>536</td><td>536</td><td>536</td><td>536</td><td>434</td><td>434</td></tr><tr><td> $R^2$ </td><td>0.19</td><td>0.33</td><td>0.34</td><td>0.35</td><td>0.40</td><td>0.40</td></tr><tr><td>调整$R^2$ </td><td>0.18</td><td>0.32</td><td>0.32</td><td>0.34</td><td>0.39</td><td>0.39</td></tr><tr><td>剩余SE</td><td>1.01(df = 527)</td><td>0.92(df = 525)</td><td>0.92(df = 523)</td><td>0.91(df = 522)</td><td>0.87(df = 422)</td><td>0.87(df = 421)</td></tr><tr><td>F统计量</td><td>15.36*** (df = 8; 527)</td><td>25.76*** (df = 10; 525)</td><td>22.29*** (df = 12; 523)</td><td>22.06*** (df = 13; 522)</td><td>26.06*** (df = 11; 422)</td><td>23.83*** (df = 12; 421)</td></tr></table>


Note: p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01




注：p<0.1； \*\* p < 0.05； \*\*\* p < 0.01


![](/api/attachments/PHUJTSS5/fulltext/images/4f97ad24d08f67521e8bfabe8ee35738b6382f353ec737dad125b5aaf90080cb.jpg)




![](/api/attachments/PHUJTSS5/fulltext/images/4f97ad24d08f67521e8bfabe8ee35738b6382f353ec737dad125b5aaf90080cb.jpg)


![](/api/attachments/PHUJTSS5/fulltext/images/8671f14441ef4cee2c5d5ad66eb45ac05ce1a0ae9990ee9a9d08172f3ed8ceaa.jpg)  
Figure 4. Interaction Induction-Related Trust Cues  Transaction Value




![](/api/attachments/PHUJTSS5/fulltext/images/8671f14441ef4cee2c5d5ad66eb45ac05ce1a0ae9990ee9a9d08172f3ed8ceaa.jpg)  
图 4. 交互感应相关的信任线索  交易价值


## Restricting Outliers With High Average Transaction Value




## 限制平均交易价值较高的异常值


Seven dApps exhibited average logarithmic transaction values three standard deviations (SD = 0.14) above the mean (0.05). Although their leverage was below Cook’s distance of 0.5 in our initial model, a visual analysis suggests winsorization. After limiting outliers to the 95th percentile, the main effects and the complementarity term again remained robust, while the interaction terms lost significance.




七个 dApp 的平均对数交易值比平均值 (0.05) 高出三个标准差 (SD = 0.14)。尽管他们的杠杆率低于我们初始模型中 0.5 的库克距离，但视觉分析表明存在缩尾化。将异常值限制在第 95 个百分位后，主效应和互补项再次保持稳健，而交互项则失去了显着性。


## Coarsened Exact Matching




## 粗化精确匹配


With this robustness test, we aimed to reduce model dependence and bias. Simple t-tests for all independent variables between dApps with and dApps without a verified source code showed a significant difference regarding only third-party certificates. We matched our sample based on all variables except the number of unique users (the dependent variable), “verified source code” (the treatment variable), and the dApp’s category (since matching on category would have excluded too many observations; instead, we accounted for categories through dummy variables). We manually selected cutoffs for the coarsening and pruned areas with no matches. In total, we matched 64 dApps that had a verified source code with 64 dApps that did not have one. While this procedure did not allow us to control for unobserved confounders (Kennedy, 2011; Wooldridge, 2010), it should have mitigated a potential bias due to observable heterogeneity in our dataset. The results of our regression, after coarsened exact matching, provide evidence that having a verified source code is still positively associated with the number of users (β = 0.52; p < 0.01).<sup>25</sup>




通过这种稳健性测试，我们的目标是减少模型依赖性和偏差。对具有经过验证的源代码的 dApp 和不具有经过验证的源代码的 dApp 之间的所有自变量进行简单 t 检验，结果显示仅在第三方证书方面存在显着差异。我们根据除唯一用户数量（因变量）、“经过验证的源代码”（处理变量）和 dApp 类别之外的所有变量来匹配样本（因为类别匹配会排除太多观察结果；相反，我们通过虚拟变量来考虑类别）。我们手动选择粗化和修剪区域的截止值，但没有匹配。总共，我们将 64 个具有经过验证源代码的 dApp 与 64 个没有经过验证源代码的 dApp 进行了匹配。虽然这个程序不允许我们控制未观察到的混杂因素（Kennedy，2011；Wooldridge，2010），但它应该减轻由于我们的数据集中可观察到的异质性而导致的潜在偏差。经过粗化精确匹配后，我们的回归结果提供了证据表明，经过验证的源代码仍然与用户数量呈正相关（β = 0.52；p < 0.01）。<sup>25</sup>


## Discussion




＃＃ 讨论


## Summary




＃＃ 概括


In an effort to theorize the role of IT in users’ initial trust formation processes more clearly and contribute to prior work on technology-based trust (e.g., McKnight et al., 2011; Wingreen et al., 2019), we propose a new perspective on trust formation. Our core argument is that IT offers predefined rules encoded in deterministic computer code that can be processed by deduction. If these rules are disclosed, immutable, and automatically executed, users can process all steps of a transaction with pure logic and attain what we refer to as deductive certainty. In this case, trust becomes dispensable. Short of this, performing some steps of this deductive process, knowing that others have done so, and even knowing that a deductive analysis is possible, can lead to what we call deduction-related trust. Being the outcome of a cognitive process based on deduction distinguishes this new type of trust from established trust types, which are based on induction.




为了更清晰地理论化 IT 在用户初始信任形成过程中的作用，并为基于技术的信任的先前工作做出贡献（例如，McKnight 等人，2011；Wingreen 等人，2019），我们提出了关于信任形成的新视角。我们的核心论点是，IT 提供了用确定性计算机代码编码的预定义规则，可以通过推论进行处理。如果这些规则是公开的、不可变的、自动执行的，那么用户就可以用纯逻辑处理交易的所有步骤，并获得我们所说的演绎确定性。在这种情况下，信任就变得可有可无。除此之外，执行这个演绎过程的某些步骤，知道其他人已经这样做了，甚至知道演绎分析是可能的，可以导致我们所说的与演绎相关的信任。作为基于演绎的认知过程的结果，这种新型信任与基于归纳的既定信任类型不同。


We then argue that smart contracts on a blockchain are a case in point. They predefine all rules of a transaction, are immutable, and are automatically executed. If disclosed, they offer users the possibility of deductive certainty. Yet, as inspecting a smart contract requires skill and effort, and trust is known to be a complexity reduction mechanism, we expect that users will often content themselves with deduction-related trust, and hypothesize that they will supplement it with classical inductive trust formation depending on the risk associated with a transaction and the effort required to attain deductive certainty.




然后我们认为区块链上的智能合约就是一个很好的例子。它们预定义了交易的所有规则，是不可变的，并且自动执行。如果披露，它们将为用户提供演绎确定性的可能性。然而，由于检查智能合约需要技巧和努力，并且众所周知，信任是一种降低复杂性的机制，因此我们预计用户通常会满足于与演绎相关的信任，并假设他们将根据与交易相关的风险和获得演绎确定性所需的努力，用经典的归纳信任形成来补充它。


Our survey provides evidence that few participants conduct thorough audits of smart contracts, while most rely on some deductive steps. Thus, trust is still required. Our survey data also provides evidence that deduction-related trust in a specific smart contract is empirically distinguishable from inductionrelated trusting beliefs about the dApp and the dApp provider and general institution-based trust in the blockchain periphery.




我们的调查提供的证据表明，很少有参与者对智能合约进行彻底的审计，而大多数参与者依赖于一些演绎步骤。所以，信任还是需要的。我们的调查数据还提供了证据，表明特定智能合约中与演绎相关的信任在经验上与对 dApp 和 dApp 提供商的归纳相关信任信念以及区块链外围中基于一般机构的信任是有区别的。


Our dApp data analysis provides evidence that providing the possibility to achieve deductive certainty by revealing a smart contract’s source code and having it verified is associated with greater adoption (H1). We also found evidence that providing classic inductive cues still matters, and that smart contracts are thus not “trust-free” (H2). Furthermore, we found evidence that the higher the risk of the transaction, the more important deduction-related trust becomes (H3b). In contrast, risk negatively moderates the relationship between inductive cues and adoption, contradicting H3a.




我们的 dApp 数据分析提供的证据表明，通过揭示智能合约的源代码并对其进行验证来提供实现演绎确定性的可能性与更大的采用率相关（H1）。我们还发现证据表明，提供经典的归纳线索仍然很重要，因此智能合约并不是“无需信任”的（H2）。此外，我们发现证据表明交易风险越高，与扣除相关的信任变得越重要（H3b）。相反，风险对归纳线索和采用之间的关系产生负面调节，这与 H3a 相矛盾。


## Interpretation




＃＃ 解释


The support we found for hypotheses H1 and H2 emphasizes that while dApp providers can profit from system trust in the blockchain periphery (Lumineau et al., 2023), they also need to foster specific trusting beliefs about their dApp. These results also help to explain why dApps differ greatly in their trust perception and usage, even if they offer the same type of service on the same blockchain. Together with the evidence we present that deduction-related and induction-related trust are distinct constructs, the evidence supporting H1 and H2 suggests that deduction-related trust exists alongside rather than replaces classic inductive trusting beliefs. Evidence of complementarity between the possibility of deductive certainty and inductive cues emphasizes this finding.




我们发现的假设 H1 和 H2 的支持强调，虽然 dApp 提供商可以从区块链外围的系统信任中获利（Lumineau 等人，2023），但他们还需要培养对其 dApp 的特定信任信念。这些结果还有助于解释为什么 dApp 在信任认知和使用方面存在很大差异，即使它们在同一区块链上提供相同类型的服务。结合我们提出的演绎相关信任和归纳相关信任是不同结构的证据，支持 H1 和 H2 的证据表明，演绎相关信任与经典归纳信任信念并存，而不是取代经典归纳信任信念。演绎确定性与归纳线索的可能性之间的互补性证据强调了这一发现。


While our findings support H1, H2, and H3a, we found that risk negatively moderates inductive trust, contradicting H3b. With high risk, users seem to rely more on deduction-related trust at the expense of induction-related trust, presumably because it allows them to attain a higher absolute level of trust. H4a, stating that the cost of achieving deductive certainty negatively moderates the relationship between the possibility of deductive certainty and the number of adopters, could not be tested with our data because having a verified source code operationalizes deduction-related trust. Future studies could resort to matching, analyzing “twins” of dApps that differ only in the cost of deductive certainty to test this. Also, qualitative or survey-based approaches might be options. Finally, H4b was not supported. While surprising at first glance, this absence of a substitutive effect (in case of high cost of attaining deduction-related trust, users rely more on induction) is consistent with our finding of a complementary relationship between a verified source code and inductive trust cues.




虽然我们的研究结果支持 H1、H2 和 H3a，但我们发现风险会负向调节归纳信任，这与 H3b 相矛盾。在高风险的情况下，用户似乎更多地依赖于演绎相关的信任，而牺牲了归纳相关的信任，大概是因为它可以让他们获得更高的绝对信任水平。 H4a 指出，实现演绎确定性的成本负面调节了演绎确定性的可能性与采用者数量之间的关系，无法用我们的数据进行测试，因为拥有经过验证的源代码可以操作与演绎相关的信任。未来的研究可以诉诸于匹配、分析 dApp 的“双胞胎”，它们的不同之处仅在于测试这一点的演绎确定性成本。此外，定性或基于调查的方法也可能是选择。最后不支持H4b。虽然乍一看令人惊讶，但这种替代效应的缺乏（在获得推导相关信任的成本很高的情况下，用户更多地依赖于归纳）与我们发现的经过验证的源代码和归纳信任线索之间的互补关系是一致的。


In sum, our analysis provides evidence that smart contracts on a blockchain can become a powerful tool to build trust among strangers, as they allow for an unprecedented level of deduction. However, it also emphasizes that this new possibility depends on the parties’ actual enactment. This point is crucial as it underscores the risk of falsely assuming that smart contracts are inherently “trust-free,” which can expose parties to malicious actors. This vulnerability is evident in the numerous scams and hacks prevalent in the blockchain space. Therefore, it is important for users not to confuse deduction-related trust, which still allows for exploitation, with deductive certainty. On a related note, even with full transparency, deducibility, and immutability, the possibility of deductive certainty may be de facto absent when an IT system is so complex that even the best efforts of the most skilled expert will not suffice to comprehend it by deduction. Modern generative AI systems are a case in point. However, the concept of deductive certainty—and the associated cost of achieving it—could serve as important design principles for fostering trust in such systems.




总之，我们的分析提供了证据，表明区块链上的智能合约可以成为在陌生人之间建立信任的强大工具，因为它们允许前所未有的扣除水平。不过，它也强调，这种新的可能性取决于各方的实际颁布。这一点至关重要，因为它强调了错误地假设智能合约本质上是“无需信任”的风险，这可能会使各方面临恶意行为者的威胁。这种漏洞在区块链领域普遍存在的众多骗局和黑客攻击中显而易见。因此，对于用户来说，重要的是不要将仍然允许利用的演绎相关信任与演绎确定性相混淆。与此相关的是，即使具有完全的透明性、可推论性和不变性，当 IT 系统如此复杂以至于即使是最熟练的专家尽最大努力也不足以通过演绎来理解它时，演绎确定性的可能性实际上也可能不存在。现代生成式人工智能系统就是一个很好的例子。然而，演绎确定性的概念以及实现它的相关成本可以作为培养对此类系统的信任的重要设计原则。


Regarding the novelty of our findings, our concept of deduction-related trust differs from established forms of induction-related trust in fundamental ways. The most important difference lies in its formation through deduction, which allows for building trust in situations that do not allow for inductive trust formation. Furthermore, their respective effects on adoption should be moderated in different ways by the cost of achieving deductive certainty, as we hypothesize in H4a and H4b.




关于我们研究结果的新颖性，我们的演绎相关信任概念在根本上不同于现有的归纳相关信任形式。最重要的区别在于它是通过演绎形成的，这允许在不允许归纳信任形成的情况下建立信任。此外，正如我们在 H4a 和 H4b 中假设的那样，它们各自对采用的影响应该通过实现演绎确定性的成本以不同的方式来调节。


## Contributions to the Literature




## 对文献的贡献


Our work makes two contributions. First, we contribute to the trust formation literature in general—and the online trust formation literature in particular—by extending Simmel’s (1930) conception of trust as weak inductive knowledge in combination with a quasi-religious leap of faith, a view that has shaped much of the existing literature (Giddens, 1991; Möllering, 2001), through a deductive dimension. This new dimension recognizes the possibility that the knowledge required for a leap of faith can also be based on a deductive process and the belief in verifiable cause-and-effect relationships. This dimension is important as the focus of trust formation has shifted from interpersonal trust to institution, technology, and system-based trust (Ba & Pavlou, 2002; Lumineau et al., 2023; Pavlou & Gefen, 2004; Ratnasingam & Pavlou, 2002; Wingreen et al., 2019). Yet none of the existing theories account for the fact that IT artifacts and their technology-based behavior fundamentally differ from human behavior, as they follow explicated rules that can be comprehended by logic and therefore offer a different source of trust. Our new perspective on trust formation provides the tools to understand how technology-based trust differs from human-based trust and allows us to better understand the role of IT systems in trust formation. In particular, the new concepts of deductive certainty, the possibility of deductive certainty, and deduction-related trust that we introduce help in understanding the boundaries of trust and what is necessary to remove trust from transactions. Deduction-related trust provides an additional antecedent for technology-based and algorithmic trust, previously only considered a consequence of an inductive process (Chawla, 2020; McKnight et al., 2011). This could not only inspire scholars to revisit existing trust-building technologies and investigate the extent to which allowing deduction influences their effectiveness, but could also help developers design more trustworthy IT systems by optimizing the level at which they enable the deduction of future behavior.




我们的工作有两个贡献。首先，我们通过将 Simmel (1930) 的信任概念扩展为与准宗教的信仰飞跃相结合的弱归纳知识，这一观点通过演绎维度塑造了大部分现有文献 (Giddens, 1991; Möllering, 2001)，从而为一般的信任形成文献——特别是在线信任形成文献做出了贡献。这个新维度认识到信仰飞跃所需的知识也可以基于演绎过程和对可验证因果关系的信念的可能性。这一维度很重要，因为信任形成的焦点已从人际信任转向基于机构、技术和系统的信任（Ba & Pavlou，2002；Lumineau 等，2023；Pavlou & Gefen，2004；Ratnasingam & Pavlou，2002；Wingreen 等，2019）。然而，现有的理论都没有考虑到 IT 制品及其基于技术的行为与人类行为有根本不同的事实，因为它们遵循可以通过逻辑理解的明确规则，因此提供了不同的信任来源。我们对信任形成的新视角提供了工具来理解基于技术的信任与基于人类的信任有何不同，并使我们能够更好地理解 IT 系统在信任形成中的作用。特别是，我们引入的演绎确定性、演绎确定性的可能性以及与演绎相关的信任的新概念有助于理解信任的边界以及从交易中消除信任的必要条件。与演绎相关的信任为基于技术和算法的信任提供了额外的前提，以前仅被认为是归纳过程的结果（Chawla，2020；McKnight 等人，2011）。这不仅可以激发学者们重新审视现有的信任构建技术，并研究允许推演对其有效性的影响程度，还可以帮助开发人员通过优化未来行为推演的水平来设计更值得信赖的IT系统。


Second, we contribute to the literature on trust in the context of blockchain technology (Chen et al., 2023; Greiner & Wang, 2015; Hawlitschek et al., 2018; Lumineau et al., 2023; Notheisen et al., 2017; Wang et al., 2022) by responding to Lumineau et al.’s (2021) call to investigate the interplay between blockchain technology’s technical and social dimensions and how they affect the technology’s adoption and use in practice. By separating smart contracts’ technical features from the cognitive processes users employ to attain deductive certainty, we clarify the relationship between trust and blockchain technology and elucidate not only the point at which a smart contract becomes “trust-free” but also the point at which deduction-related trust becomes more likely. The introduction of the possibility of deductive certainty as a new concept enables us to bridge earlier and more recent perspectives on blockchain and trust. Early work posited that blockchains could create “trust-free” systems by eliminating the need for interpersonal trust (e.g., Beck et al., 2016; Notheisen et al., 2017), whereas more recent research merely suggests a shift from interpersonal to system-based or algorithm-based trust (e.g., Chawla, 2020; Lumineau et al., 2023; Wang et al., 2022). Our new perspective reveals that the former implicitly assumes that users enact the possibility of deductive certainty, while the latter overlooks this possibility, framing trust mainly as an inductive process. We furthermore show that whether the core of a transaction (i.e., the actions of the smart contract) is “trust-free” depends not only on whether the smart contract relies on external information, in line with the “trust frontier” proposed by Hawlitschek et al. (2018), but, importantly, also on the extent to which users enact the possibility of deductive certainty. Finally, our argument that the possibility of deductive certainty is a feature of a specific smart contract (enabled by the blockchain infrastructure) allows us to explain why different dApps offering the same type of service on the same blockchain platform may differ in trust perceptions and usage. This observation cannot be explained by the core argument present in the more recent literature, which argues that trust shifts from interpersonal trust to trust in the blockchain system (Chawla, 2020; Wang et al., 2022).




其次，我们响应 Lumineau 等人 (2021) 的呼吁，对区块链技术背景下的信任研究做出了贡献，即调查区块链技术背景下信任的相互影响。区块链技术的技术和社会维度以及它们如何影响该技术在实践中的采用和使用。通过将智能合约的技术特征与用户用于获得演绎确定性的认知过程分开，我们阐明了信任与区块链技术之间的关系，不仅阐明了智能合约变得“无需信任”的点，而且还阐明了与演绎相关的信任变得更有可能的点。演绎确定性作为一个新概念的可能性的引入使我们能够弥合区块链和信任的早期和最新观点。早期的研究认为，区块链可以通过消除人际信任的需要来创建“无信任”系统（例如，Beck 等人，2016 年；Notheisen 等人，2017 年），而最近的研究仅仅表明从人际信任转向基于系统或基于算法的信任（例如，Chawla，2020 年；Lumineau 等人，2023 年；Wang 等人， 2022）。我们的新观点表明，前者隐含地假设用户具有演绎确定性的可能性，而后者则忽视了这种可能性，将信任主要视为一个归纳过程。我们进一步表明，交易的核心（即智能合约的行为）是否“免信任”不仅取决于智能合约是否依赖外部信息，与 Hawlitschek 等人提出的“信任边界”一致。 （2018），但重要的是，还取决于用户在多大程度上发挥演绎确定性的可能性。最后，我们认为演绎确定性的可能性是特定智能合约（由区块链基础设施启用）的一个特征，这使我们能够解释为什么在同一区块链平台上提供相同类型服务的不同 dApp 在信任认知和使用方面可能有所不同。这一观察结果无法用最近文献中出现的核心论点来解释，该论点认为信任从人际信任转变为区块链系统中的信任（Chawla，2020；Wang 等人，2022）。


## Future Research




## 未来的研究


We hope that our research encourages trust scholars to explore the extent to which other IT systems that enable the deduction of future behavior can enhance users’ trust and adoption. Prominent candidates include the current debates on trust in AI-based agents and the growing field of explainable artificial intelligence. For instance, researchers could apply the concepts of deduction-related trust and the cost of deductive certainty in a controlled lab setting to examine user preferences regarding the trade-off between the cost of achieving deductive certainty and agent performance. Research could also explore whether the extent of users’ skill in attaining deduction-related trust regarding those systems influences how fast they experiment with and adopt new agents. Another interesting question for trust research more generally would be how deduction matters in trust formation outside the technical realm, particularly for legal contracts. For example, scholars could study what parts of legal contracts allow building deduction-related trust and investigate the conditions under which legal contracts lead to more deduction-related trust than smart contracts. Further, IS trust scholars could use our deduction-based perspective on trust formation and revisit established trust phenomena like the paradox of high initial trust (McKnight et al., 1998) in the online context and explore alternative explanations that consider the possibility of deductive certainty and deductionrelated trust.




我们希望我们的研究能够鼓励信任学者探索其他能够推断未来行为的 IT 系统在多大程度上可以增强用户的信任和采用。突出的候选者包括当前关于对基于人工智能的代理的信任的争论以及不断发展的可解释人工智能领域。例如，研究人员可以在受控实验室环境中应用与演绎相关的信任和演绎确定性成本的概念，以检查用户关于实现演绎确定性的成本和代理绩效之间权衡的偏好。研究还可以探讨用户获得对这些系统的推论相关信任的技能程度是否会影响他们试验和采用新代理的速度。更普遍而言，信任研究的另一个有趣问题是，在技术领域之外的信任形成中，推论如何发挥重要作用，特别是对于法律合同而言。例如，学者可以研究法律合同的哪些部分允许建立与扣除相关的信任，并研究法律合同在什么条件下比智能合同产生更多与扣除相关的信任。此外，IS 信任学者可以使用我们基于演绎的信任形成视角，重新审视在线环境中已建立的信任现象，例如高初始信任的悖论（McKnight 等人，1998），并探索考虑演绎确定性和演绎相关信任可能性的替代解释。


Regarding the study of smart contracts and blockchain, future researchers could build on our approach and use the rich data provided by the Ethereum blockchain to study questions related to platform economics, marketing, or entrepreneurship in the nascent field of blockchain applications. Researchers could also use our approach to target actual dApp users and collect data on their behavior instead of relying on a lab environment.




关于智能合约和区块链的研究，未来的研究人员可以在我们的方法的基础上，利用以太坊区块链提供的丰富数据来研究区块链应用新兴领域中与平台经济学、营销或创业相关的问题。研究人员还可以使用我们的方法来定位实际的 dApp 用户并收集他们的行为数据，而不是依赖实验室环境。


## Limitations




## 限制


Our study has limitations. The survey’s sample size and a potential response bias involving the likely overrepresentation of users more knowledgeable about smart contracts limit generalizability. However, the survey was not intended to determine the share of users who read smart contract source code but rather serves to demonstrate that some users indeed strive to come close to deductive certainty (and have the required skills for it) and most users care about deductionrelated trust. Relatedly, with blockchain applications becoming more widespread, future smart contract users will, on average, be less knowledgeable about blockchain technology than today’s users, which should further reduce the share of users who read smart contracts but should also increase the number of users who are familiar with and trust in dApps in general. Still, the problem of initial trust will remain whenever a user first interacts with a dApp, and the knowledge that others can attain deductive certainty about the dApp should help to build deduction-related trust. Another limitation of the survey is the low reliability of the trust in the blockchain periphery construct (Cronbach’s alpha = 0.54), caused by the low correlation of the “automated execution” and the “transparency” items.<sup>26</sup> While this construct is not integral to our theory, this finding suggests the need for caution in interpreting it.




我们的研究有局限性。该调查的样本量和潜在的反应偏差（涉及对智能合约更了解的用户可能过多）限制了普遍性。然而，该调查并不是为了确定阅读智能合约源代码的用户比例，而是为了证明一些用户确实努力接近演绎确定性（并拥有所需的技能），并且大多数用户关心与演绎相关的信任。与此相关的是，随着区块链应用变得更加广泛，未来的智能合约用户对区块链技术的了解平均将低于现在的用户，这应该会进一步减少阅读智能合约的用户比例，但总体上也会增加熟悉和信任 dApp 的用户数量。尽管如此，每当用户第一次与 dApp 交互时，初始信任问题仍然存在，并且知道其他人可以获得有关 dApp 的演绎确定性，这应该有助于建立与演绎相关的信任。该调查的另一个局限性是区块链外围结构的信任可靠性较低（Cronbach α = 0.54），这是由于“自动执行”和“透明度”项目的相关性较低造成的。<sup>26</sup>虽然这一结构不是我们理论的组成部分，但这一发现表明在解释它时需要谨慎。


Regarding the dApp data analysis, the possibility of deductive certainty could also be interpreted as a factor causing more positive induction-related beliefs. To account for this, we explicitly ignored the possibility of deductive certainty while coding established inductive dimensions and conducted interviews and a survey to discover whether users actually read the source code. Still, some issues may remain. Regarding effort and risk, the length of code and transaction value are only proxies; thus, our moderation analysis must be interpreted cautiously. Herding effects might have biased our results. However, since retrieving the number of unique users of a dApp from the Ethereum blockchain is not a trivial task, and the respective companies’ websites did not indicate this number, we assume that this bias is of minor importance. Endogeneity concerns remain. For instance, we could not fully control for companies’ advertising efforts. We tried to account for such effects by adding as many controls as possible. Reassuringly, since most dApps were small applications at an early development stage, we can assume that most user acquisition was done via the dApp’s website. An experimental study could help mitigate such concerns and improve internal validity. It would also allow the testing of H4a, which we could not test with our data. In terms of external validity, our results might have been biased by a high proportion of early users and comparatively simple smart contracts. On the other hand, firms engaging with more complex smart contracts in the future will likely be willing to employ specialists and invest more effort in checking smart contracts’ source code. Furthermore, our study is limited by an observability bias, as we could only observe conducted transactions.




关于 dApp 数据分析，演绎确定性的可能性也可以被解释为导致更积极的归纳相关信念的一个因素。为了解释这一点，我们在编码时明确忽略了演绎确定性的可能性，建立了归纳维度，并进行了访谈和调查来发现用户是否真正阅读了源代码。尽管如此，一些问题可能仍然存在。关于努力和风险，代码长度和交易价值只是代理；因此，我们的适度分析必须谨慎解释。羊群效应可能会使我们的结果产生偏差。然而，由于从以太坊区块链中检索 dApp 的唯一用户数量并不是一项简单的任务，而且各个公司的网站也没有标明这个数字，因此我们认为这种偏差并不重要。内生性担忧依然存在。例如，我们无法完全控制公司的广告力度。我们试图通过添加尽可能多的控件来解释这种影响。令人放心的是，由于大多数 dApp 在早期开发阶段都是小型应用程序，因此我们可以假设大多数用户获取都是通过 dApp 的网站完成的。实验研究可以帮助减轻此类担忧并提高内部有效性。它还允许测试 H4a，而我们无法用我们的数据进行测试。就外部有效性而言，我们的结果可能会因高比例的早期用户和相对简单的智能合约而产生偏差。另一方面，未来从事更复杂智能合约的公司可能会愿意聘请专家并投入更多精力来检查智能合约的源代码。此外，我们的研究受到可观察性偏差的限制，因为我们只能观察进行的交易。


## Conclusion




＃＃ 结论


Extant literature describes trust formation as a mostly inductive process. We provide evidence that for smart contracts and, to some extent, in other instances, a new type of trust exists that is based on deduction. Future research should explore the contingencies of deduction-related trust in more detail. In practice, a better understanding of deductionbased trust formation should help to facilitate transactions that otherwise would not take place.




现有文献将信任形成描述为一个主要是归纳过程。我们提供的证据表明，对于智能合约以及在某种程度上，在其他情况下，存在一种基于演绎的新型信任。未来的研究应该更详细地探讨与演绎相关的信任的意外情况。在实践中，更好地理解基于扣除的信任形成应该有助于促进原本不会发生的交易。


## Acknowlegments




## 致谢


This work was funded by Fundação para a Ciência e a Tecnologia (UID/00124/2025, UID/PRR/124/2025, Nova School of Business and Economics) and LISBOA2030 (DataLab2030 - LISBOA2030-FEDER-01314200).




这项工作由 Fundação para a Ciência e a Tecnologia (UID/00124/2025、UID/PRR/124/2025、Nova 商业与经济学院) 和 LISBOA2030 (DataLab2030 - LISBOA2030-FEDER-01314200) 资助。


## References




＃＃ 参考


Ba, S., & Pavlou, P. (2002). Evidence of the effect of trust building technology in electronic markets. MIS Quarterly, 26(3), 243-268. https://doi.org/10.2307/4132332




Ba, S. 和 Pavlou, P. (2002)。电子市场中信任构建技术效果的证据。 《管理信息系统季刊》，26(3)，243-268。 https://doi.org/10.2307/4132332


Bachmann, R., & Zaheer, A. (Eds.). (2006). Handbook of trust research. Edward Elgar Publishing. https://doi.org/10.4337/ 9781847202819




Bachmann, R. 和 Zaheer, A.（编）。 （2006）。信任研究手册。爱德华·埃尔加出版社。 https://doi.org/10.4337/9781847202819


Beck, R., Czepluch, J., Lollike, N., & Malone, S. (2016). Blockchain— The gateway to trust free cryptographic transactions. In Proceedings of the 24th European Conference on Information Systems.




Beck, R.、Czepluch, J.、Lollike, N. 和 Malone, S. (2016)。区块链——免信任加密交易的门户。第 24 届欧洲信息系统会议论文集。


Becker, T., Robertson, M., & Vandenberg, R. (2019). Nonlinear transformations in organizational research: possible problems and potential solutions. Organizational Research Methods, 22(4), 831- 866. https://doi.org/10.1177/1094428118775205




贝克尔，T.、罗伯逊，M. 和范登堡，R. (2019)。组织研究中的非线性变换：可能的问题和潜在的解决方案。组织研究方法，22(4), 831-866。 https://doi.org/10.1177/1094428118775205


Beldad, A., de Jong, M., & Steehouder, M. (2010). How shall I trust the faceless and the intangible? A literature review on the




Beldad, A.、de Jong, M. 和 Steehouder, M. (2010)。我该如何相信那些不露面和无形的东西？文献综述


antecedents of online trust. Computers in Human Behavior, 26(5), 857-869. https://doi.org/10.1016/j.chb.2010.03.013




在线信任的前因。计算机在人类行为中的应用，26(5), 857-869。 https://doi.org/10.1016/j.chb.2010.03.013


Brewer, M. B. (1988). A dual process model of impression formation. In Srull T & R. Wyer (Eds.), Advances in social cognition (pp. 1- 36). Erlbaum.




布鲁尔，M.B.（1988）。印象形成的双过程模型。见 Srull T & R. Wyer（主编），《社会认知的进展》（第 1-36 页）。埃尔鲍姆。


Cai, W., Wang, Z., Ernst, J., Hong, Z., Feng, C., & Leung, V. C. (2018). Decentralized applications: The blockchain-empowered software system. IEEE Access, 6, 53019-53033. https://doi.org/10.1109/ access.2018.2870644




蔡伟、王志、恩斯特 J.、洪志、冯 C. 和梁 V. C. (2018)。去中心化应用：区块链赋能的软件系统。 IEEE 访问，6，53019-53033。 https://doi.org/10.1109/access.2018.2870644


Chawla, C. (2020). Trust in blockchains: Algorithmic and organizational. Journal of Business Venturing Insights, 14, Article e00203. https://doi.org/10.1016/j.jbvi.2020.e00203




乔拉，C.（2020）。对区块链的信任：算法和组织。 《商业风险洞察杂志》，14，文章 e00203。 https://doi.org/10.1016/j.jbvi.2020.e00203


Chen, R. R., Chen, K., & Ou, C. X. J. (2023). Facilitating interorganizational trust in strategic alliances by leveraging blockchain-based systems: Case studies of two eastern banks. International Journal of Information Management, 68, Article 102521. https://doi.org/10.1016/j.ijinfomgt.2022.102521




陈 R. R.、陈 K. 和欧 C. X. J. (2023)。利用基于区块链的系统促进战略联盟中的组织间信任：两家东部银行的案例研究。 《国际信息管理杂志》，68，第 102521 条。https://doi.org/10.1016/j.ijinfomgt.2022.102521


Copi, I. M. (2016). Essentials of logic (2nd ed.). Routledge. https://doi.org/10.4324/9781315389028




科皮，I.M. (2016)。逻辑要点（第二版）。劳特利奇。 https://doi.org/10.4324/9781315389028


Doney, P., & Cannon, J. (1997). An examination of the nature of trust in buyer-seller relationships. Journal of Marketing, 61, 35-51. https://doi.org/10.1177/002224299706100203




多尼，P.，＆坎农，J.（1997）。对买卖双方关系中信任性质的考察。营销杂志，61，35-51。 https://doi.org/10.1177/002224299706100203


Doney, P., Cannon, J., & Mullen, M. (1998). Understanding the influence of national culture on the development of trust. Academy of Management Review, 23(3), 601-620. https://doi.org/10.5465/ amr.1998.926629




多尼，P.，坎农，J.，＆马伦，M.（1998）。了解民族文化对信任发展的影响。管理学院评论，23(3), 601-620。 https://doi.org/10.5465/amr.1998.926629


Dutra, A., Tumasjan, A., & Welpe, I. (2018). Blockchain is changing how media and entertainment companies compete. MIT Sloan Management Review, https://sloanreview.mit.edu/article/ blockchain-is-changing-how-media-and-entertainmentcompanies-compete/




Dutra, A.、Tumasjan, A. 和 Welpe, I. (2018)。区块链正在改变媒体和娱乐公司的竞争方式。麻省理工斯隆管理评论，https://sloanreview.mit.edu/article/blockchain-is-having-how-media-and-entertainmentcompanies-compete/


Elsbach, K., & Elofson, G. (2000). How the packaging of decision explanations affects perceptions of trustworthiness. Academy of Management Journal, 43(1), 80-89. https://doi.org/10.2307/ 1556387




埃尔斯巴赫，K. 和埃洛夫森，G. (2000)。决策解释的包装如何影响可信度的感知。管理学会杂志，43(1), 80-89。 https://doi.org/10.2307/1556387


Fang, Y., Qureshi, I., Sun, H., McCole, P., Ramsey, E., & Lim, K. (2014). Trust, satisfaction, and online repurchase intention. MIS Quarterly, 38(3), 407–428. https://doi.org/10.25300/MISQ/2014 38.2.04




Fang, Y.、Qureshi, I.、Sun, H.、McCole, P.、Ramsey, E. 和 Lim, K. (2014)。信任度、满意度、网上复购意愿。 《管理信息系统季刊》，38(3)，407–428。 https://doi.org/10.25300/MISQ/2014 38.2.04


Fiske, S., & Taylor, S. (1991). Social cognition. Mcgraw-Hill.




费斯克，S. 和泰勒，S. (1991)。社会认知。麦格劳-希尔。


Fitzgerald. (2006). The Transformation of Open Source Software. MIS Quarterly, 30(3), 587-598. https://doi.org/10.2307/25148740




菲茨杰拉德. （2006）。开源软件的转变。 《管理信息系统季刊》，30(3)，587-598。 https://doi.org/10.2307/25148740


Friedman, B., Khan, P. H., Jr., & Howe, D. C. (2000). Trust online. Communications of the ACM, 43(12), 34-40. https://dl.acm.org/ doi/pdf/10.1145/355112.355120




Friedman, B.、Khan, P. H., Jr. 和 Howe, D. C. (2000)。信任在线。 ACM 通讯，43(12), 34-40。 https://dl.acm.org/doi/pdf/10.1145/355112.355120


Fröwis, M., & Böhme, R. (2017). In code we trust? Measuring the control flow immutability of all smart contracts deployed on Ethereum. In J. Garcia-Alfaro, G. Navarro-Arribas, H. Hartenstein, & J. Herrera-Joancomartí (Eds.), Data Privacy Management, Cryptocurrencies and Blockchain Technology (pp. 357-372). Springer International Publishing.




Fröwis, M. 和 Böhme, R. (2017)。我们信任的代码？测量以太坊上部署的所有智能合约的控制流不变性。 J. Garcia-Alfaro、G. Navarro-Arribas、H. Hartenstein 和 J. Herrera-Joancomartí（编），数据隐私管理、加密货币和区块链技术（第 357-372 页）。施普林格国际出版社。


Fukuyama, F. (1995). Trust: The social virtues and the creation of prosperity. Free Press.




福山，F.（1995）。信任：社会美德和繁荣的创造。自由新闻。


Gefen, D. (2000). E-commerce: The role of familiarity and trust. Omega, 28(6), 725-737. https://doi.org/10.1016/S0305-0483(00) 00021-9




格芬，D.（2000）。电子商务：熟悉和信任的作用。欧米茄，28(6)，725-737。 https://doi.org/10.1016/S0305-0483(00)00021-9


Gefen, D. (2002). Reflections on the dimensions of trust and trustworthiness among online consumers. Database Advances in Information Systems, 33(3), 38-53. https://doi.org/10.1145/569 905.569910




格芬，D.（2002）。对网络消费者信任和可信度维度的思考。信息系统中的数据库进展，33(3), 38-53。 https://doi.org/10.1145/569 905.569910


Gefen, D., Benbasat, I., & Pavlou, P. (2008). A research agenda for trust in online environments. Journal of Management Information Systems, 24(4), 275-286. https://doi.org/10.2753/MIS0742-1222 240411




Gefen, D.、Benbasat, I. 和 Pavlou, P. (2008)。在线环境信任的研究议程。管理信息系统杂志，24(4), 275-286。 https://doi.org/10.2753/MIS0742-1222 240411


Gefen, D., Karahanna, E., & Straub, D. (2003). Trust and TAM in online shopping: An integrated model. MIS Quarterly, 27(1), 51- 90. https://doi.org/10.2307/30036519




Gefen, D.、Karahanna, E. 和 Straub, D. (2003)。在线购物中的信任和 TAM：集成模型。 《管理信息系统季刊》，27(1), 51-90。https://doi.org/10.2307/30036519


Giddens, A. (1991). Modernity and self-identity: self and society in the late modern age. Stanford University Press.




吉登斯，A.（1991）。现代性与自我认同：现代晚期的自我与社会。斯坦福大学出版社。


Gorsuch, R. L. (2014). Factor analysis (2nd ed.). Taylor & Francis. http://gbv.eblib.com/patron/FullRecord.aspx?p=1873793




戈萨奇，R.L.（2014）。因素分析（第二版）。泰勒和弗朗西斯. http://gbv.eblib.com/patron/FullRecord.aspx?p=1873793


Grégoire, D. A., Barr, P. S., & Shepherd, D. A. (2010). Cognitive processes of opportunity recognition: the role of structural alignment. Organization Science, 21(2), 413-431. https://doi.org/ 10.1287/orsc.1090.0462




格雷瓜尔，D.A.、巴尔，P.S. 和谢泼德，D.A. (2010)。机会识别的认知过程：结构调整的作用。组织科学，21(2), 413-431。 https://doi.org/10.1287/orsc.1090.0462


Greiner, M., & Wang, H. (2015). Trust-free systems—A new research and design direction to handle trust-issues in P2P systems: The case of Bitcoin. In Proceedings of the 21st Americas Conference on Information Systems.




格雷纳，M.，＆王，H.（2015）。无信任系统——处理 P2P 系统中信任问题的新研究和设计方向：以比特币为例。第 21 届美洲信息系统会议论文集。


Gulati, R. (1995). Does familiarity breed trust? The implications of repeated ties for contractual choice in alliances. Academy of Management Journal, 38(1), 85-112. https://doi.org/10.2307/ 256729




古拉蒂，R.（1995）。熟悉会产生信任吗？重复关系对联盟中契约选择的影响。管理学会杂志，38(1), 85-112。 https://doi.org/10.2307/256729


Halaburda, H., Levina, N., & Min, S. (2024). Digitization of transaction terms within TCE: Strong smart contract as a new mode of transaction governance. MIS Quarterly, 48(2), 825-846. https://doi.org/10.25300/MISQ/2023/17818




Halaburda, H.、Levina, N. 和 Min, S. (2024)。 TCE 内交易条款的数字化：强智能合约作为交易治理的新模式。 《管理信息系统季刊》，48(2), 825-846。 https://doi.org/10.25300/MISQ/2023/17818


Hawlitschek, F., Notheisen, B., & Teubner, T. (2018). The limits of trust-free systems: A literature review on blockchain technology and trust in the sharing economy. Electronic Commerce Research and Applications, 29, 50-63. https://doi.org/10.1016/j.elerap.2018. 03.005




Hawlitschek, F.、Notheisen, B. 和 Teubner, T. (2018)。免信任系统的局限性：区块链技术和共享经济中信任的文献综述。电子商务研究与应用，29, 50-63。 https://doi.org/10.1016/j.elerap.2018。 03.005


Holden, R., & Malani, A. (2021). Can blockchain solve the hold-up problem in contracts? Cambridge University Press.




霍尔顿，R. 和马拉尼，A. (2021)。区块链能否解决合约套牢问题？剑桥大学出版社。


Jarvenpaa, S., Tractinsky, N., & Vitale, M. (2000). Consumer trust in an Internet store. Information Technology and Management, 45- 71. https://doi.org/10.1023/A:1019104520776




Jarvenpaa, S.、Tractinsky, N. 和 Vitale, M. (2000)。消费者对互联网商店的信任。信息技术与管理，45-71。https://doi.org/10.1023/A:1019104520776


Jiang, P., Jones, D. B., & Javie, S. (2008). How third‐party certification programs relate to consumer trust in online transactions: An exploratory study. Psychology & Marketing, 25(9), 839-858. https://doi.org/10.1002/mar.20243




Jiang, P.、Jones, D. B. 和 Javie, S. (2008)。第三方认证计划如何与消费者对在线交易的信任相关：一项探索性研究。心理学与营销，25(9), 839-858。 https://doi.org/10.1002/mar.20243


Johnson-Laird, P. N. (2001). Mental models and deduction. Trends in Cognitive Sciences, 5(10), 434-442. https://doi.org/10.1016/S1364- 6613(00)01751-4




约翰逊-莱尔德，P.N.（2001）。心智模型和演绎。认知科学趋势，5(10), 434-442。 https://doi.org/10.1016/S1364-6613(00)01751-4


Kennedy, P. (2011). A guide to econometrics (6th ed.). Blackwell.




肯尼迪，P.（2011）。计量经济学指南（第六版）。布莱克威尔.


Kim, K. K., & Prabhakar, B. (2002). Initial trust abstract and the adoption of B2C e-commerce: The case of internet banking. The Data Base for Advances in Information Systems, 35(2), 50-64. https://doi.org/10.1145/1007965.1007970




Kim, K. K. 和 Prabhakar, B. (2002)。初始信任摘要与 B2C 电子商务的采用：以网上银行为例。信息系统进展数据库，35(2), 50-64。 https://doi.org/10.1145/1007965.1007970


Kline, R. B. (Ed.). (2016). Principles and practice of structural equation modeling (4th edition). Guilford Press.




克莱恩，R.B.（编）。 （2016）。结构方程建模原理与实践（第4版）。吉尔福德出版社。


Leiponen, A., Thomas, L., & Wang, Q. (2021). The dApp economy: A new platform for distributed innovation? Innovation, 24, 125-143. https://doi.org/10.1080/14479338.2021.1965887




Leiponen, A.、Thomas, L. 和 Wang, Q. (2021)。 dApp 经济：分布式创新的新平台？创新，24, 125-143。 https://doi.org/10.1080/14479338.2021.1965887


Lim, K., Sia, C., Lee, M., & Benbasat, I. (2006). Do I trust you online, and if so, will I buy? An empirical study of two trust-building strategies. Journal of Management Information Systems, 23(2), 233-266. https://doi.org/10.2753/MIS0742-1222230210




Lim, K.、Sia, C.、Lee, M. 和 Benbasat, I. (2006)。我在网上信任你们吗？如果信任，我会购买吗？两种信任建立策略的实证研究。管理信息系统杂志，23(2), 233-266。 https://doi.org/10.2753/MIS0742-1222230210


Lippert, S. K. (2008). Assessing post-adoption utilisation of an information technology within a supply chain management context. International Journal of Information Technology and Management, 7(1), 36-59. https://doi.org/10.1504/IJITM.2008. 015888




利珀特，S.K.（2008）。评估供应链管理环境中信息技术采用后的利用率。国际信息技术与管理杂志，7(1), 36-59。 https://doi.org/10.1504/IJITM.2008。 015888


Liu, B., & Goodhue, D. (2012). Two worlds of trust for potential ecommerce users: humans as cognitive misers. Information Systems Research, 23(4), 1246-1262. https://doi.org/10.1287/isre.1120. 0424




刘 B. 和古德休 D. (2012)。潜在电子商务用户的两个信任世界：人类作为认知守财奴。信息系统研究，23(4), 1246-1262。 https://doi.org/10.1287/isre.1120。 0424


Luhmann, N. (1979). Trust and power. John Wiley & Sons.




卢曼，N.（1979）。信任和权力。约翰·威利父子。


Lumineau, F., Schilke, O., & Wang, W. (2023). Organizational trust in the age of the fourth industrial revolution: Shifts in the form, production, and targets of trust. Journal of Management Inquiry, 32(1), 21-34. https://doi.org/10.1177/10564926221127852




Lumineau, F.、Schilke, O. 和 Wang, W. (2023)。第四次工业革命时代的组织信任：信任的形式、产生和目标的转变。管理探究杂志，32(1), 21-34。 https://doi.org/10.1177/10564926221127852


Lumineau, F., Wang, W., & Schilke, O. (2021). Blockchain governance—A new way of organizing collaborations? Organization Science, 32(2), 500-521. https://doi.org/10.1287/ orsc.2020.1379




Lumineau, F.、Wang, W. 和 Schilke, O. (2021)。区块链治理——组织协作的新方式？组织科学，32(2), 500-521。 https://doi.org/10.1287/orsc.2020.1379


Macneil, I. (1977). Contracts: Adjustment of long-term economic relations under classical, neoclassical, and relational contract law. Northwestern University Law Review, 72, 854-905.




麦克尼尔，I.（1977）。合同：古典、新古典和关系合同法下长期经济关系的调整。西北大学法律评论，72, 854-905。


Mayer, R., & Gavin, M. (2005). Trust in management and performance: Who minds the shop while the employees watch the boss? Academy of Management Journal, 48(5), 874-888. https://doi.org/10.5465/AMJ.2005.18803928




梅耶尔，R. 和加文，M. (2005)。对管理和绩效的信任：当员工监视老板时，谁来管理商店？管理学会杂志，48(5), 874-888。 https://doi.org/10.5465/AMJ.2005.18803928


Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). An integrative model of organizational trust. Academy of Management Review, 20(3), 709-734. https://doi.org/10.2307/258792




Mayer, R. C.、Davis, J. H. 和 Schoorman, F. D. (1995)。组织信任的综合模型。管理学院评论，20(3), 709-734。 https://doi.org/10.2307/258792


McAllister, D. (1995). Affect- and cognition-based trust as foundation for interpersonal cooperation in organizations. Academy of Management Journal, 38, 24-59. https://doi.org/10.5465/256727




麦卡利斯特，D.（1995）。基于情感和认知的信任是组织中人际合作的基础。管理学院杂志，38, 24-59。 https://doi.org/10.5465/256727


McKnight, H., Carter, M., Thatcher, J., & Clay, P. (2011). Trust in a specific technology. ACM Transactions on Management Information Systems, 2(2), 1-25. https://doi.org/10.1145/1985347. 1985353




麦克奈特，H.，卡特，M.，撒切尔，J.，＆克莱，P.（2011）。信任特定的技术。 ACM 管理信息系统汇刊，2(2), 1-25。 https://doi.org/10.1145/1985347。 1985353


McKnight, H., & Chervany, N. (2001). What trust means in ecommerce customer relationships: An interdisciplinary conceptual typology. International Journal of Electronic Commerce, 6(2), 35- 59. https://doi.org/10.1080/10864415.2001.11044235




麦克奈特，H.，＆切尔瓦尼，N.（2001）。信任在电子商务客户关系中意味着什么：跨学科的概念类型。国际电子商务杂志，6(2), 35-59。 https://doi.org/10.1080/10864415.2001.11044235


McKnight, H., Chervany, N., & Cummings, L. (1996). Trust formation in new organizational relationships. Management Information Systems Research Center, University of Minnesota.




麦克奈特，H.，切尔瓦尼，N.，＆卡明斯，L.（1996）。新组织关系中信任的形成。明尼苏达大学管理信息系统研究中心。


McKnight, H., Choudhury, V., & Kacmar, C. (2002a). Developing and validating trust measures for e-commerce: An integrative typology. Information Systems Research, 13(3), 334-359. https://doi.org 10.1287/isre.13.3.334.81




McKnight, H.、Choudhury, V. 和 Kacmar, C. (2002a)。开发和验证电子商务的信任措施：综合类型。信息系统研究，13(3), 334-359。 https://doi.org 10.1287/isre.13.3.334.81


McKnight, H., Choudhury, V., & Kacmar, C. (2002b). The impact of initial consumer trust on intentions to transact with a web site: A




McKnight, H.、Choudhury, V. 和 Kacmar, C. (2002b)。初始消费者信任对网站交易意图的影响：A


trust building model. Journal of Strategic Information Systems, 11, 297-323. https://doi.org/10.1016/S0963-8687(02)00020-3




信任建立模型。战略信息系统杂志，11，297-323。 https://doi.org/10.1016/S0963-8687(02)00020-3


McKnight, H., Cummings, L., & Chervany, N. (1998). Initial trust formation in new organizational relationships. Academy of Management Review, 23(3), 473-490. https://doi.org/10.2307/ 259290




麦克奈特 H.、卡明斯 L. 和切尔瓦尼 N. (1998)。新组织关系中初步信任的形成。管理学院评论，23(3), 473-490。 https://doi.org/10.2307/259290


Möllering, G. (2001). The nature of trust: From Georg Simmel to a theory of expectation, interpretation and suspension. Sociology, 35(2), 403-420. https://doi.org/10.1017/S0038038501000190




穆勒林，G. (2001)。信任的本质：从格奥尔格·齐美尔到期望、解释和悬置理论。社会学，35(2), 403-420。 https://doi.org/10.1017/S0038038501000190


Mueller, B. A., & Shepherd, D. A. (2016). Making the most of failure experiences: Exploring the relationship between business failure and the identification of business opportunities. Entrepreneurship Theory and Practice, 40(3), 457-487. https://doi.org/10.1111/etap. 12116




穆勒 (B. A.) 和谢泼德 (D. A.) (2016)。充分利用失败经历：探索商业失败与识别商业机会之间的关系。创业理论与实践，40(3), 457-487。 https://doi.org/10.1111/etap。 12116


Murray, A., Kuban, S., Josefy, M., & Anderson, J. (2019). Contracting in the smart era: The implications of blockchain and decentralized autonomous organizations for contracting and corporate governance. Academy of Management Perspectives, 35(4). https://doi.org/10.5465/amp.2018.0066




Murray, A.、Kuban, S.、Josefy, M. 和 Anderson, J. (2019)。智能时代的合同：区块链和去中心化自治组织对合同和公司治理的影响。管理学院观点，35(4)。 https://doi.org/10.5465/amp.2018.0066


Mytkowicz, T., Diwan, A., & Bradley, E. (2009). Computer systems are dynamical systems. Chaos: An Interdisciplinary Journal of Nonlinear Science, 19(3), Article 033124. https://doi.org/10.1063 1.3187791




Mytkowicz, T.、Diwan, A. 和 Bradley, E. (2009)。计算机系统是动态系统。混沌：非线性科学跨学科期刊，19(3)，文章 033124。https://doi.org/10.1063 1.3187791


Nöteberg, A., Christiaanse, E., & Wallage, P. (1999). The role of trust and assurance services in electronic channels: An exploratory study. In Proceedings of the International Conference on Information Systems.




Nöteberg, A.、Christiaanse, E. 和 Wallage, P. (1999)。电子渠道中信任和保证服务的作用：探索性研究。国际信息系统会议论文集。


Notheisen, B., Cholewa, J., & Shanmugam, A. (2017). Trading realworld assets on blockchain. Business & Information Systems Engineering, 59(6), 425-440. https://doi.org/10.1007/s12599-017- 0499-8




Notheisen, B.、Cholewa, J. 和 Shanmugam, A. (2017)。在区块链上交易现实世界的资产。商业与信息系统工程，59(6), 425-440。 https://doi.org/10.1007/s12599-017-0499-8


Orlikowski, W., & Iacono, S. (2001). Research commentary: Desperately seeking the “IT” in IT research—A call to theorizing the IT artifact. Information Systems Research, 12(2), 121-134. https://doi.org/10.1287/isre.12.2.121.9700




Orlikowski, W. 和 Iacono, S. (2001)。研究评论：在IT研究中拼命寻找“IT”——呼吁对IT工件进行理论化。信息系统研究，12(2), 121-134。 https://doi.org/10.1287/isre.12.2.121.9700


Palmer, J., Bailey, J., & Faraj, S. (2000). The role of intermediaries in the development of trust on the WWW: The use and prominence of trusted third parties and privacy statements. Journal of Computer-Mediated Communication, 5(3), Article JCMC532. https://doi.org/10.1111/j.1083-6101.2000.tb00342.x




Palmer, J.、Bailey, J. 和 Faraj, S. (2000)。中介机构在 WWW 信任发展中的作用：受信任的第三方和隐私声明的使用和突出。计算机介导的通信杂志，5(3)，文章 JCMC532。 https://doi.org/10.1111/j.1083-6101.2000.tb00342.x


Pavlou, P. (2003). Consumer acceptance of electronic commerce: integrating trust and risk with the technology acceptance model. International Journal of Electronic Commerce, 7(3), 101-134. https://doi.org/10.1080/10864415.2003.11044275




帕夫卢，P.（2003）。消费者对电子商务的接受度：将信任和风险与技术接受模型相结合。国际电子商务杂志，7(3), 101-134。 https://doi.org/10.1080/10864415.2003.11044275


Pavlou, P., & Fygenson, M. (2006). Understanding and predicting electronic commerce adoption: An extension of the theory of planned behavior. MIS Quarterly, 30(1), 115-143. https://doi.org/ 10.2307/25148720




Pavlou, P. 和 Fygenson, M. (2006)。理解和预测电子商务的采用：计划行为理论的延伸。 《管理信息系统季刊》，30(1)，115-143。 https://doi.org/10.2307/25148720


Pavlou, P., & Gefen, D. (2004). Building effective online marketplaces with institution-based trust. Information Systems Research, 15, 37- 59. https://doi.org/10.1287/isre.1040.0015




Pavlou, P. 和 Gefen, D. (2004)。通过基于机构的信任建立有效的在线市场。信息系统研究，15, 37-59。 https://doi.org/10.1287/isre.1040.0015


Petty, R., & Cacioppo, J. (1986). The elaboration likelihood model of persuasion. Advances in Experimental Social Psychology, 19, 123- 205. https://doi.org/10.1016/S0065-2601(08)60214-2




佩蒂，R. 和卡西奥波，J. (1986)。说服的阐述可能性模型。实验社会心理学进展，19, 123-205。 https://doi.org/10.1016/S0065-2601(08)60214-2


Poppo, L., Zhou, K., & Ryu, S. (2008a). Alternative origins to interorganizational trust: An interdependence perspective on the




Poppo, L.、Zhou, K. 和 Ryu, S. (2008a)。组织间信任的另类起源：从相互依存的角度看待组织间信任


shadow of the past and the shadow of the future. Organization Science, 19(1), 39-55. https://doi.org/10.1287/orsc.1070.0281




过去的影子和未来的影子。组织科学，19(1), 39-55。 https://doi.org/10.1287/orsc.1070.0281


Poppo, L., Zhou, K., & Zenger, T. R. (2008b). Examining the conditional limits of relational governance: Specialized assets, performance ambiguity, and long-standing ties. Journal of Management Studies, 45(7), 1195-1216. https://doi.org/10.1111/ j.1467-6486.2008.00779.x




Poppo, L.、Zhou, K. 和 Zenger, T. R. (2008b)。检验关系治理的条件限制：专业资产、绩效模糊性和长期关系。管理研究杂志，45（7），1195-1216。 https://doi.org/10.1111/j.1467-6486.2008.00779.x


Raskin, M. (2016). The law and legality of smart contracts. Georgetown Law Technology Review, 1(2), 305-341.




拉斯金，M.（2016）。智能合约的法律和合法性。乔治城法律技术评论，1(2), 305-341。


Ratnasingam, P., & Pavlou, P. (2002). Technology trust: The next value creator in B2B electronic commerce. In Proceedings of the 2002 IRMA International Conference (pp. 19-22).




Ratnasingam, P. 和 Pavlou, P. (2002)。技术信任：B2B电子商务的下一个价值创造者。 2002 年 IRMA 国际会议记录（第 19-22 页）。


Ratnasingam, P., & Pavlou, P. (2003). Technology trust in internetbased interorganizational electronic commerce. Journal of Electronic Commerce in Organizations, 1(1), 17-41.




Ratnasingam, P. 和 Pavlou, P. (2003)。基于互联网的组织间电子商务的技术信任。组织电子商务杂志，1(1), 17-41。


Rempel, J., Holmes, J., & Zanna, M. (1985). Trust in close relationships. Journal of Personality and Social Psychology, 49(1), 95-112. https://doi.org/10.1037/0022-3514.49.1.95




Rempel, J.、Holmes, J. 和 Zanna, M. (1985)。信任密切的关系。人格与社会心理学杂志，49(1), 95-112。 https://doi.org/10.1037/0022-3514.49.1.95


Rönkkö, M., & Cho, E. (2022). An updated guideline for assessing discriminant validity. Organizational Research Methods, 25(1), 6- 14. https://doi.org/10.1177/1094428120968614




Rönkkö, M. 和 Cho, E. (2022)。评估判别有效性的更新指南。组织研究方法，25(1), 6-14。 https://doi.org/10.1177/1094428120968614


Rotter, J. B. (1971). Generalized expectancies for interpersonal trust. American Psychologist, 26(5), 443-452. https://doi.org/10.1037/ h0031464




罗特，J.B.（1971）。对人际信任的普遍期望。美国心理学家，26(5), 443-452。 https://doi.org/10.1037/h0031464


Rousseau, D., Sitkin, S., Burt, R., & Camerer, C. (1998). Not so different after all—A cross discipline view of trust. Academy of Management Review, 23, 393-404. https://doi.org/10.5465/amr. 1998.926617




卢梭，D.，西特金，S.，伯特，R.，和卡默勒，C. (1998)。毕竟没那么不同——信任的跨学科观点。管理学院评论，23，393-404。 https://doi.org/10.5465/amr。 1998.926617


Salisbury, W. D., Chin, W. W., Gopal, A., & Newsted, P. R. (2002). Research report: Better theory through measurement—Developing a scale to capture consensus on appropriation. Information Systems Research, 13(1), 91-103. https://doi.org/10.1287/isre.13.1.91.93




Salisbury, W. D.、Chin, W. W.、Gopal, A. 和 Newsted, P. R. (2002)。研究报告：通过测量更好的理论——制定一个尺度以达成拨款共识。信息系统研究，13(1), 91-103。 https://doi.org/10.1287/isre.13.1.91.93


Shapiro, S. (1987). The social control of impersonal trust. American Journal of Sociology, 93(3), 623-658. https://doi.org/10.1086/ 228791




夏皮罗，S.（1987）。非个人信任的社会控制。美国社会学杂志，93(3), 623-658。 https://doi.org/10.1086/228791


Simmel, G. (1930). Philosophie des Geldes (5th ed.). Duncker & Humblot.




齐美尔，G. (1930)。哲学哲学（第五版）。邓克和洪布洛特。


Simon, H. (1957). Models of man; social and rational. Wiley.




西蒙，H.（1957）。人类的典范；社会性和理性性。威利。


Simon, H. (1990). Bounded rationality. In J. Eatwell, M. Milgate, & P. Newman (Eds.), Utility and probability (pp. 15-18). Palgrave Macmillan. https://doi.org/10.1007/978-1-349-20568-4\_5




西蒙，H.（1990）。有限理性。见 J. Eatwell、M. Milgate 和 P. Newman（编辑），效用和概率（第 15-18 页）。帕尔格雷夫·麦克米伦。 https://doi.org/10.1007/978-1-349-20568-4\_5


Sternberg, R., & Mio, J. (2009). Cognitive psychology (International student ed., 5th ed.). Wadsworth. http://www.loc.gov/catdir/ enhancements/fy1215/2007941973-d.html




斯滕伯格，R.，＆Mio，J.（2009）。认知心理学（国际学生版，第五版）。沃兹沃斯。 http://www.loc.gov/catdir/enhancements/fy1215/2007941973-d.html


Stewart, K. (2003). Trust transfer on the World Wide Web. Organization Science, 14(1), 5-17. https://doi.org/10.1287/orsc.14. 1.5.12810




斯图尔特，K.（2003）。万维网上的信任转移。组织科学，14(1)，5-17。 https://doi.org/10.1287/orsc.14。 1.5.12810


Tarski, A. (1990). Logic, semantics, metamathematics (Trans. J. Corcoran, 2nd ed.). Hackett.




塔斯基，A.（1990）。逻辑、语义、元数学（Trans. J. Corcoran，第二版）。哈克特。


Taylor, S. (1981). A categorization approach to stereotyping. In Cognitive processes in stereotyping and intergroup behavior (1st ed.). Psychology Press.




泰勒，S.（1981）。刻板印象的分类方法。在刻板印象和群体间行为的认知过程中（第一版）。心理学出版社。


Thatcher, J. B., McKnight, H., Baker, E. W., Arsal, R. E., & Roberts, N. H. (2011). The role of trust in postadoption IT exploration: An empirical examination of knowledge management systems. IEEE




Thatcher, J. B.、McKnight, H.、Baker, E. W.、Arsal, R. E. 和 Roberts, N. H. (2011)。信任在采用后 IT 探索中的作用：知识管理系统的实证检验。 IEEE


Transactions on Engineering Management, 58(1), 56-70. https://doi.org/10.1109/TEM.2009.2028320




工程管理学报，58(1), 56-70。 https://doi.org/10.1109/TEM.2009.2028320


Von Krogh, G., Spaeth, S., & Lakhani, K. R. (2003). Community, joining, and specialization in open source software innovation: A case study. Research Policy, 32(7), 1217-1241. https://doi.org/ 10.1016/S0048-7333(03)00050-7




Von Krogh, G.、Spaeth, S. 和 Lakhani, K. R. (2003)。开源软件创新的社区、加入和专业化：案例研究。研究政策，32(7), 1217-1241。 https://doi.org/10.1016/S0048-7333(03)00050-7


Wang, W., Lumineau, F., & Schilke, O. (2022). Blockchains. Cambridge University Press. https://doi.org/10.1017/978100905 7707




Wang, W.、Lumineau, F. 和 Schilke, O. (2022)。区块链。剑桥大学出版社。 https://doi.org/10.1017/978100905 7707


Weiss, J., & Obermeier, D. (2021). How blockchain can enhance trust and transparency of online surveys. In Proceedings of the International Conference on Information Systems.




Weiss, J. 和 Obermeier, D. (2021)。区块链如何增强在线调查的信任和透明度。国际信息系统会议论文集。


Werbach, K. (2018). The blockchain and the new architecture of trust. MIT Press.




韦巴赫，K.（2018）。区块链和新的信任架构。麻省理工学院出版社。


Williamson, O. E. (1985). The economic institutions of capitalism. Free Press.




威廉姆森，O.E.（1985）。资本主义的经济制度。自由新闻。


Wingreen, S., Mazey, N., Baglione, S., & Storholm, G. (2019). Transfer of electronic commerce trust between physical and virtual environments: Experimental effects of structural assurance and situational normality. Electronic Commerce Research, 19(2), 339- 371. https://doi.org/10.1007/s10660-018-9305-z




Wingreen, S.、Mazey, N.、Baglione, S. 和 Storholm, G. (2019)。物理和虚拟环境之间电子商务信任的转移：结构保证和情境常态的实验效果。电子商务研究，19(2), 339-371。 https://doi.org/10.1007/s10660-018-9305-z


Wooldridge, J. (2010). Econometric analysis of cross section and panel data (2nd ed.). MIT Press.




伍德里奇，J.（2010）。横截面和面板数据的计量经济学分析（第二版）。麻省理工学院出版社。


Yang, S.-C., Hung, W.-C., Sung, K., & Farn, C.-K. (2006). Investigating initial trust toward e-tailers from the elaboration likelihood model perspective. Psychology and Marketing, 23(5), 429-445. https://doi.org/10.1002/mar.20120




Yang, S.-C.、Hung, W.-C.、Sung, K. 和 Farn, C.-K.。 （2006）。从精细化可能性模型的角度调查对电子零售商的初始信任。心理学与营销，23(5), 429-445。 https://doi.org/10.1002/mar.20120


Zaheer, A., & Venkatraman, N. (1995). Relational governance as an interorganizational strategy: An empirical test of the role of trust in economic exchange. Strategic Management Journal, 16, 373-392.




Zaheer, A. 和 Venkatraman, N. (1995)。作为一种组织间战略的关系治理：对经济交换中信任作用的实证检验。战略管理杂志，16, 373-392。


Zhou, T. (2011). An empirical examination of initial trust in mobile banking. Internet Research, 21, 527-540. https://doi.org/10.1108/ 10662241111176353




周涛（2011）。对移动银行初始信任的实证检验。互联网研究，21, 527-540。 https://doi.org/10.1108/10662241111176353


Zhou, T. (2012). Understanding users’ initial trust in mobile banking: An elaboration likelihood perspective. Computers in Human Behavior, 28(4), 1518-1525. https://doi.org/10.1016/j.chb.2012. 03.021




周涛（2012）。了解用户对移动银行的初始信任：细化可能性视角。计算机在人类行为中的应用，28(4), 1518-1525。 https://doi.org/10.1016/j.chb.2012。 03.021


Zucker, L. (1986). Production of trust: Institutional sources of economic structure 1840-1920. Research in Organization Behavior, 8(1), 53-111.




扎克，L.（1986）。信任的产生：1840-1920 年经济结构的制度根源。组织行为研究，8(1), 53-111。


## About the Authors




## 关于作者


Daniel Obermeier received his Ph.D. from the Technical University of Munich and is an assistant professor of information systems at Nova School of Business and Economics, Universidade NOVA de Lisboa. His main research interest centers on how emerging technologies are reshaping economic forces on digital platforms and influencing platform governance. Currently, his research employs various causal inference techniques to investigate the impact of blockchain technology and AI on digital platforms. Daniel has published his work, among other outlets, in MIS Quarterly and top IS conferences, such as the International Conference on Information Systems, the Conference on Information Systems and Technology, or the Workshop on Information Systems and Economics. Daniel was a visiting scholar and postdoctoral researcher at NYU Stern and serves as a reviewer for top IS journals, such as MIS Quarterly, Management Science, Information Systems Research, and Journal of the Association for Information Systems. ORCiD: 0000-0002-1326-537X




丹尼尔·奥伯迈尔 (Daniel Obermeier) 获得博士学位。拥有慕尼黑工业大学博士学位，现任里斯本大学诺瓦商业与经济学院信息系统助理教授。他的主要研究兴趣集中在新兴技术如何重塑数字平台上的经济力量并影响平台治理。目前，他的研究采用各种因果推理技术来研究区块链技术和人工智能对数字平台的影响。 Daniel 曾在 MIS Quarterly 和顶级 IS 会议（例如国际信息系统会议、信息系统与技术会议或信息系统与经济学研讨会）等媒体上发表过他的作品。 Daniel曾是纽约大学斯特恩商学院的访问学者和博士后研究员，并担任MIS Quarterly、Management Science、Information Systems Research、Journal of the Association for Information Systems等顶级IS期刊的审稿人。 ORCiD：0000-0002-1326-537X


Joachim Henkel is a professor of technology and innovation management at TUM School of Management, Technical University of Munich. He holds a master’s degree in theoretical physics, a doctorate in economics, and a habilitation in management. After completing his Ph.D., he worked for two years with the consulting firm, Bain & Company. Joachim’s research areas are digitalization, patent licensing, standards, value capture, technology acquisitions, and open innovation. He has published his work, among other outlets, in Harvard Business Review, Rand Journal of Economics, Research Policy, and Strategic Management Journal. Joachim Henkel was an associate editor for Academy of Management Discoveries and serves on various editorial review boards. He has been a visiting scholar at University College London, MIT Sloan School of Management, Harvard Business School, Singapore Management University, and École Polytechnique de Paris. As a member of the Expertenkommission Forschung und Innovation, he advises the German Federal Government on Research and Innovation policy. ORCiD: 0000-0002-6065-0983.




Joachim Henkel 是慕尼黑工业大学 TUM 管理学院技术与创新管理学教授。他拥有理论物理学硕士学位、经济学博士学位和管理学博士学位。完成博士学位后，他在咨询公司 Bain & Company 工作了两年。 Joachim 的研究领域包括数字化、专利许可、标准、价值获取、技术收购和开放式创新。他的研究成果发表在《哈佛商业评论》、《兰德经济学杂志》、《研究政策》和《战略管理杂志》等媒体上。约阿希姆·汉高 (Joachim Henkel) 是管理发现学院的副主编，并在多个编辑审查委员会任职。曾任伦敦大学学院、麻省理工斯隆管理学院、哈佛商学院、新加坡管理大学、巴黎综合理工大学的访问学者。作为研究与创新专家委员会的成员，他为德国联邦政府提供研究和创新政策方面的建议。 ORCiD：0000-0002-6065-0983。
