---
otero_id: 16424
otero_key: "WADKTHC2"
title: "Knowledge-Aware Learning Framework Based on Schema Theory to Complement Large Learning Models"
authors: "Long Xia; Wenqi Shen; Weiguo Fan; G. Alan Wang"
year: "2024"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2024.2340827"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge-Aware Learning Framework Based on Schema Theory to Complement Large Learning Models

Long Xia, Wenqi Shen, Weiguo Fan & G. Alan Wang

To cite this article: Long Xia, Wenqi Shen, Weiguo Fan & G. Alan Wang (2024) Knowledge-Aware Learning Framework Based on Schema Theory to Complement Large Learning Models, Journal of Management Information Systems, 41:2, 453-486, DOI: 10.1080/07421222.2024.2340827

To link to this article: https://doi.org/10.1080/07421222.2024.2340827

![](/api/attachments/WADKTHC2/fulltext/images/a965960ae96f846482e81d081ffbc73dc691d94a76d15776083b4ecdd4eca328.jpg)

\+ View supplementary material

![](/api/attachments/WADKTHC2/fulltext/images/87363f4c08eeea715ddce3eee9c95502c248dca348ce119f7845d6012635ef98.jpg)

Published online: 24 Jun 2024.

![](/api/attachments/WADKTHC2/fulltext/images/6d0a515689519d514eb8303cc1ce3bc4c08542177819deafdabe399ff5bb7c69.jpg)

Submit your article to this journal

![](/api/attachments/WADKTHC2/fulltext/images/93ac885c80c01d462cbfa6fb0aa9554fddb9e29e53c1b3970dbaa058b0e656b1.jpg)

Article views: 464

![](/api/attachments/WADKTHC2/fulltext/images/41312709d97ca6cde5170e07a1b07b62144823cf0832d83c96338861bbb4c0c3.jpg)

View related articles

![](/api/attachments/WADKTHC2/fulltext/images/439988d81ab42723f80aea4f618cd7b180d58970d75dd4a9c17e822758938a2d.jpg)

View Crossmark data

Check for updates

# Knowledge-Aware Learning Framework Based on Schema Theory to Complement Large Learning Models

Long Xia<sup>a</sup>, Wenqi Shen<sup>b</sup>, Weiguo Fan<sup>c</sup>, and G. Alan Wang<sup>b</sup>

<sup>a</sup>Department of Management & Entrepreneurship, Love School of Business, Elon University, Elon, North Carolina, USA; <sup>b</sup>Department of Business Information Technology, Pamplin College of Business, Virginia Tech, Blacksburg, Virginia, USA; <sup>c</sup>Department of Business Analytics, Tippie College of Business, University of Iowa, Iowa City, Iowa, USA

## ABSTRACT

Despite tremendous recent progress, extant artificial intelligence (AI) still falls short of matching human learning in efectiveness and eficiency. One fundamental disparity is that humans possess a wealth of prior knowledge, while AI lacks the essential commonsense knowledge required for learning tasks. Guided by schema theory, we employ the design science research methodology to introduce a novel knowledge-aware learning framework to harness the knowledge-based processes in human learning. Unlike existing pre-trained large language models (LLMs) and knowledge-aware approaches that treat knowledge in considerably diferent ways from humans, our theoretically grounded framework closely mimics how humans acquire, represent, activate, and utilize knowledge. The extensive evaluations in the context of text analytics tasks demonstrate that our design achieves comparable performance to the state-of-the-art LLMs and enhances model generalizability and learning eficiency. This study takes a step forward by bringing cognitive science into building cognitively plausible AI and human-AI collaboration research.

## KEYWORDS

Knowledge-aware models; schema theory; knowledge graph; text analytics; deep learning; design science; artificial intelligence

## Introduction

Recent advances in machine learning, particularly deep learning, have facilitated the creation of artificial intelligence (AI) that exhibits impressive performance across a range of tasks within the field of natural language processing (NLP) [50]. Notably, the recent launch of ChatGPT, built on the generative pre-trained transformers (GPT), one of the largest language models, has garnered widespread global attention spanning various industries [76]. Despite these remarkable advancements, existing AI systems still fall short of achieving human-level performance in terms of learning effectiveness (e.g., accuracy) and efficiency (e.g., the amount of required training data) [48]. As highlighted by Sam Altman, the CEO of OpenAI—the organization behind ChatGPT—it is imperative to shift the focus away from creating larger models trained on extensive datasets. Instead, efforts should be directed towards enhancing AI’s learning capabilities while reducing the number of parameters, and fostering the development of AI systems that closely resemble human cognition and can augment human intelligence in an understandable manner [34, 64, 71].

Humans exhibit the remarkable ability to grasp new concepts from a single example and apply them to future tasks, while AI typically requires thousands or even millions of training examples to achieve comparable performance [48]. Even when the required data is available, the training process is computationally and economically expensive. For example, the latest GPT-4 model boasts over one trillion parameters and costs over \$100 million just for the pre-training step [47]. Despite the substantial costs, large language models (LLMs) occasionally commit factual errors and struggle with the most trivial logical inferences [28]. One plausible reason for this significant contrast in learning performance between humans and AI, especially those rooted in deep learning, is that current AI, while loosely inspired by the human brain’s structure, does not accurately mirror the intricacies of human learning processes [27]. Hence, a promising approach to attaining human-level performance is to develop cognitively plausible AI inspired by human intelligence and cognition [21].

The concept of cognitive plausibility refers to the extent to which a computational model can mimic human cognitive processes. These computational models are usually created by either directly approximating human cognitive learning processes or evolving from an underlying human cognitive model through a series of transformations. These transformations are designed to preserve the cognitive validity of the original model, ensuring that the computational models remain comparable to human cognitive processes [29, 54]. In the field of AI, cognitively plausible AI implies the design of AI learning models that aim to interact with humans in an intelligent, “human-like” manner [29, 83]. Particularly, a prevalent view underscores a fundamental distinction between humans and AI: humans possess an extensive reservoir of prior knowledge, whereas AI lacks the commonsense knowledge necessary for a grounded comprehension of the world, which would assist in the learning process<sup>i</sup> [38]. Consequently, while humans can draw upon their long-term memories to access relevant knowledge to support learning tasks, AI systems typically require a large volume of data to discern patterns in similar tasks [48]. Therefore, from the knowledge perspective, “a longstanding goal of artificial intelligence is to develop systems that continuously accumulate knowledge by consuming facts and rules about the world and reasoning over them” [90, p. 1]. Consequently, the central focus of this study revolves around the development of knowledge-aware models, which have emerged as one of the most dynamic research domains in AI research [41].

While widely used in existing studies [61, 85, 94, 100], the term “knowledge-aware models” lacks a formal definition. Following Ji et al. [38], we define knowledge-aware models as computational models that explicitly integrate external knowledge into the learning process. By leveraging external knowledge, these models potentially offer improved performance compared to models that do not leverage external knowledge. However, our literature review in the next section reveals that existing knowledge-aware models still inadequately capture the knowledge processes employed by humans during learning. For instance, certain knowledge-aware models [95, 98, 109] include external knowledge as additional word embeddings in their learning processes. Word embeddings, such as Google’s Word2Vec and Stanford’s GloVe, consist of dense vectors representing words, capturing their semantic meaning based on context. Words with similar meanings or those used in similar contexts are situated closely in the vector space [75]. However, each word in the vocabulary corresponds to a static vector, often conflating multiple meanings or senses into a single representation (termed the polysemy problem). Consequently, the incorporated knowledge lacks contextuality and specificity for individual learning instances.

Conversely, some other models [24, 56, 107] explore the structural relationships among external knowledge using graph convolution networks (GCNs). This graph-based approach reveals both direct and higher-order semantic relationships between knowledge embeddings, reflecting the contextual nuances of the training data [46]. However, these models fall short in effectively selecting relevant knowledge or do so through an ad-hoc method, without capturing how humans retrieve related knowledge from their long-term memory. Consequently, the external knowledge incorporated remains generic rather than tailored to the specific training context, and the polysemy problem persists.

The aforementioned discussion highlights a significant research gap: while current knowledge-aware models use external knowledge, in the forms of knowledge embeddings or graphs, to enhance semantic understanding in learning, the knowledge is often conflated with various connotations and is not contextually specific to the learning task. However, for humans to complete a particular learning task, of all the knowledge stored in our long-term memories, only certain parts of them are relevant and should be retrieved [67]. Inspired by the goal to improve AI’s capabilities of treating knowledge in a more human-like manner, our study seeks to develop a learning framework that can mimic how knowledge is processed during human learning. To achieve this goal, we aim to address three research questions:

(RQ1): Can we design a knowledge-aware framework, drawing inspiration from cognitive learning theory, that comprehensively mirrors the knowledge-based processes involved in human learning?

(RQ2): Is it possible for this cognitively plausible knowledge-aware learning framework to attain satisfactory performance without relying on LLMs?

(RQ3): Does this framework contribute to improving learning efficiency?

To answer these questions, we adopt the design science research (DSR) methodology [35] to propose a learning framework rooted in cognitive learning theories. Specifically, drawing on schema theory, we dissect how human learning can be conceptualized as a sequence of knowledge acquisition, representation, activation, and utilization processes. Subsequently, we craft a novel knowledge-aware learning framework that resembles these knowledgebased human learning processes. Our experiments show that our design consistently achieves comparable performance to the state-of-the-art methods, predominantly reliant on pre-trained LLMs. Notably, this comparable performance is achieved with a model comprising only 7.6 percent of the parameters found in LLMs, a training dataset as small as 10 percent of the original, and a nearly three times faster training speed, demonstrating the superior learning efficiency of our proposed learning framework. Furthermore, we conduct a series of ablation studies to validate the effectiveness of the key design components, and the robustness checks reinforce our framework’s robust performance, even when confronted with incomplete or noisy knowledge sources.

The combination of promising learning effectiveness, enhanced efficiency, and robust performance illustrates the potential of our novel knowledge-aware learning framework to steer AI closer to human-like learning and competence. This study highlights the pivotal role of cognitive science and theories in shaping AI development and furnishes compelling evidence to inform future endeavors in knowledge-aware AI research. Our schema theoryguided learning framework represents a substantial contribution to knowledge-aware AI research and the broader fields of cognitive science, design science research, and practical applications. A detailed discussion of these implications is presented in the Discussions section.

## Research Background: How is Knowledge Treated in AI Research

As this study primarily contributes to the knowledge-aware learning models, the following literature review will emphasize the knowledge dimension of human learning and the treatment of knowledge within existing AI research. Specifically, we categorize existing studies into two groups based on whether they incorporate explicit external knowledge into their model designs: pre-trained LLMs that implicitly encode knowledge, and knowledgeaware models that explicitly integrate external knowledge.

## Pre-Trained LLMs: Encoding Knowledge Implicitly

In recent years, pre-trained LLMs have emerged as dominant forces in the field of NLP [65]. Their supremacy can be attributed to the expressive transformer architecture and extensive pre-training, enabling them to assimilate substantial information within their parameters [22, 24, 90, 103]. A language model undergoes pre-training on extensive text corpora, followed by fine-tuning for specific downstream tasks. During this process, the model’s weights are iteratively updated, and the resulting weights could encode a vast reservoir of knowledge [89], which can then be applied to the target tasks [86, 90]. Numerous pretrained LLMs, such as BERT [22], XLNet [104], GPT [16], and RoBERTa [60], have been applied across various tasks, consistently delivering impressive results. Notably, pre-trained LLMs have propelled significant advancements in few-shot and zero-shot learning, enabling accurate predictions with minimal training samples or even none at all [16, 44]. For example, GPT-3, containing 175 billion parameters, exhibited robust performance across various NLP tasks in a few-shot setting [16].

Despite the impressive capabilities exhibited by LLMs, they also face some limitations compared to human learning. Pre-trained LLMs demand substantial volumes of training data, particularly during the pre-training phase [16, 22]. Even when ample data is available, the computational demands of model training and fine-tuning significantly diminish learning efficiency, falling notably short of human levels. More importantly, a crucial distinction lies in the nature of the knowledge acquired by these models, which is encoded in millions or even billions of parameters. This implies that the acquired knowledge assumes a non-symbolic and implicit form [26, 86], as opposed to explicit and symbolic representations in human learning. Such an implicit knowledge-learning paradigm also contributes to the black-box nature of deep learning. That is, while AI, including LLMs, has achieved remarkable results, it fails to align with human-centric learning objectives and as a result, the learning processes remain inscrutable from a human perspective [62, 90]. Given our goal is to apply a human-centered approach to develop AI systems that encapsulate human knowledge-based processes in a cognitively plausible manner, we excluded LLMs from our knowledge-aware framework design. However, since pre-trained LLMs have predominantly achieved state-of-the-art performance in a range of NLP tasks, we use them as benchmarks to comprehensively evaluate both the learning effectiveness and efficiency of our proposed design framework.

## Knowledge-Aware Models: Incorporating Explicit External Knowledge

In contrast, human knowledge is typically represented symbolically and explicitly, comprising sets of facts, concepts, rules, or principles [62], all readily representable and verbalizable [26]. During learning, knowledge starts in an implicit form and gradually becomes explicit as the learning advances [10]. Dienes and Perner [23] contend that explicit knowledge offers the necessary, and even sufficient, conditions for completing a learning task. Given its pivotal role, recent efforts have focused on harnessing the benefits of incorporating external knowledge into AI systems. Specifically, external knowledge can be used within knowledge graphs, serving as a rich and structured repository of commonsense knowledge. This knowledge is organized in the form of triples (concept1, relation, concept2), mirroring how humans store knowledge [38, 103]. As depicted in Figure 1a, knowledge is conveyed through the knowledge triples, with concepts as fundamental building blocks and relations between concepts as the adhesive that connects related concepts. A comprehensive knowledge structure can be constructed through the combination of multiple concepts and relations, as illustrated in Figure 1b.

Knowledge graphs, serving as repositories of explicit knowledge, play an important role in providing essential human knowledge to bolster AI learning. Their integration into AI models, often referred to as “knowledge-aware models,” has gained substantial traction in the pursuit of achieving human-level cognition and intelligence [108]. For instance, consider the task of building a text classification model to determine whether a news article with the headline, “Tim Cook announced a new lineup of products during the keynote event,” belongs to technology news. Humans effortlessly accomplish this task by drawing upon relevant prior knowledge from their long-term memory, suggesting that (Tim Cook; ChiefExecutiveOfficerOf; Apple) and (Apple; IsA; Technology Company). These two pieces of information, not explicitly present in the focal text, are instead stored in and retrieved from external background knowledge. As a result, introducing external human knowledge into knowledge-aware models enhances their performance by capturing context, nuances, and subtle relationships absent from the data [38, 68]. More importantly, this explicit knowledge is interpretable to humans. Consequently, incorporating external human knowledge facilitates the generation of interpretable explanations for the learning processes, enhancing the comprehensibility and explainability of AI models [52].

![](/api/attachments/WADKTHC2/fulltext/images/77ced504f47d5b398479b8715f8ca2cd57ac0ca53f05194defae0f2d138b1cb2.jpg)

![](/api/attachments/WADKTHC2/fulltext/images/b3049a505a3b03598918cce2418605e37b1d793c4ae9d7821a6e7f42598c61c5.jpg)  
Figure 1. Knowledge representations: (a) Knowledge represented in knowledge triples and (b) knowledge represented in a knowledge graph.

The first type of knowledge-aware model incorporates external knowledge as supplementary word embeddings in their learning processes. For instance, Wang et al. [95] retrieved external concept knowledge and fused it with word- and character-level information to construct text classification models. Zhang et al. [109] introduced ERNIE, employing a pre-training strategy that masks phrases or entities to learn synaptic and semantic knowledge, achieving favorable results across five NLP tasks. Wang et al. [98] introduced KEPLER, encoding textual descriptions of entities as additional embeddings in conjunction with an LLM and jointly optimizing knowledge embeddings and language models. However, since each word corresponds to a static vector, this approach combines multiple meanings or senses into a single representation, leading to a lack of contextuality and specificity for individual learning instances. Moreover, a significant drawback of treating external knowledge as additional embeddings is their failure to capture intricate relationships, particularly structural ones, which are essential in human learning [7, 25, 43, 63]. Consequently, we contend that external human knowledge has not been effectively modeled using this approach.

The second category of knowledge-aware models leverages GCNs to capture the structural relationships within the external knowledge [37, 72]. This graph-based representation could unveil semantic relationships, including higher-order ones, between knowledge embeddings. It also captures information across the nodes of the graph and the relationships conveyed through connections [46]. For example, Lin et al. [56] introduced a textual inference framework for commonsense question answering, utilizing structured external knowledge graphs for explainable inferences. This framework grounds question-answer pairs from the semantic space into the knowledge-based symbolic space as schema graphs. Dong et al. [24] proposed a novel knowledge graph distillation method to obtain a knowledge meta-graph bridging queries and passages in passage re-ranking tasks. They employed a pre-trained LLM as a text encoder and GCN over the knowledge meta-graph as a knowledge encoder. However, these models either neglect knowledge selection or handle it in an ad hoc manner, overlooking how humans retrieve relevant knowledge from their long-term memory. Consequently, the incorporated external knowledge remains generic rather than tailored to the specific training context [37, 72].

## Schema Theory: Knowledge-Based Processes in Human Learning

The development of knowledge in human learning has been extensively explored within the realm of cognitive science as a fundamental aspect of human cognition, involving the construction of a representation of the world through interactive experiences [26]. Within this context, prior knowledge assumes a crucial role as a cognitive element, involving the retrieval of pertinent information from long-term memory [20]. Specifically, efforts to elucidate the role of knowledge in human learning have been extensively explored by the schema theory [45], which offers a comprehensive theoretical framework for understanding human learning, proposing that learning can be conceptualized as a series of cognitive activities centered on the creation and application of schemas [11]. In this context, a schema is defined as a knowledge structure that signifies relationships among its constituent components [6]. Within the terminology of schema theory, these components are commonly referred to as “nodes” or “slots” [9]. More specifically, a schema represents general knowledge that is considered universally applicable to underlying concepts, encompassing objects, situations, events, and sequences of phenomena [79]. This accumulated knowledge, in the plural form of “schemata,” constitutes an individual’s background knowledge, stored in the long-term memory [9]. While the definitions of schema may vary in wording, they share a fundamental characteristic: the representation of an individual’s pre-existing knowledge, structured according to the relationships among its constituent parts [8, 67].

Once knowledge is acquired and structurally organized, of all the knowledge stored, only a subset of it is relevant to the immediate learning task and should be selectively activated [67]. Schema theory posits that learning is an interactive process, with efficient learning necessitating the ability to connect the learning task with one’s existing knowledge base [17]. The information embedded within the learning tasks often serves as cues, guiding learners to retrieve and activate the relevant knowledge schemas from their long-term memory to support the learning process [5]. In summary, the preceding discussion unveils two fundamental processes outlined by schema theory: (1) knowledge acquisition and representation and (2) knowledge activation and utilization. In the following, we will delve into a detailed examination of these essential knowledge processes.

## Knowledge Acquisition and Representation

The first question regarding human knowledge processes centers on how knowledge is acquired and stored within the mind [67]. First, it is imperative to recognize that knowledge is not an inherent, pre-existing mental entity but rather a product of learning and accumulation through direct and indirect exposure to the world [32]. As previously introduced, an individual’s schemata are repositories of knowledge already residing in memory. These schemata consist of subsidiary nodes or slots interconnected by relationships [80]. When individuals engage with the world, they connect their experiences with existing schemata, organizing them into concepts and relations, and supplementing these schemata by populating new slots [30]. This newly acquired knowledge seamlessly integrates into the broader reservoir of prior or background knowledge [5], concluding the knowledge acquisition process.

The characterization of a schema as a knowledge structure carries significant implications for elucidating knowledge acquisition and representation. A knowledge structure denotes the representation of an individual’s knowledge, encompassing a collection of concepts and the relationships between them [7, 25, 43, 63]. A knowledge structure and a schema, as proposed by Dorsey et al. [25], “denote the same underlying construct” (pp. 31- 32) and are difficult to draw distinctions. This construct of knowledge structures implies that human knowledge transcends mere declarative facts and straightforward aggregations of basic elements; rather, it assumes the form of a structural framework that dictates when and how a particular piece of knowledge applies within a given context [13, 25]. Isolated fragments of knowledge cannot exist independently in the mind; they must be seamlessly integrated into a cohesive global knowledge structure [67]. To illustrate, Anderson’s analogy [17] emphasizes that characterizing a house as a mere assortment of bricks, lumber, glass, metal, and plastic would be inadequate. Instead, these primitive components must be thoughtfully organized and structured to accurately represent a house.

## Knowledge Activation and Utilization

Following knowledge acquisition and representation, a subsequent question pertains to how relevant knowledge can be retrieved to support the learning process. An individual’s schemata encompass all the previously acquired knowledge structures stored in memory, and learners have to combine pertinent prior knowledge with task information to facilitate effective learning [30]. Within the expanse of an individual’s long-term memory, only select portions of knowledge are pertinent to a given task and necessitate retrieval [67], and hence, the activation of the appropriate knowledge schema (a discrete segment of knowledge) from the extensive array of schemata becomes imperative, constituting what is termed schema activation [5]. Precisely, schema activation is the mechanism by which stimuli inherent to the focal learning task indicate the direction or domain to search within and stimulate the retrieval of the relevant schema for the immediate task [69]. Within this framework, learning can fail for two primary reasons: (1) learners lack the requisite schema, or (2) the necessary schema resides within their memory but remains inactivated by the learners themselves [30, 67].

The final step involves integrating the retrieved knowledge schema with task-specific information and assigning values to different concepts and propositions. At this stage, the generated propositions interconnect with both their antecedent and subsequent counterparts, epitomizing not only the localized semantic relationships but also the broader associations within the learning task [67].

## Research Gaps and Our Work

While significant progress has been made in modeling knowledge, including incorporating knowledge via trainable model parameters and integrating external knowledge in explicit, symbolic forms, our theoretical examination grounded in schema theory reveals that these models diverge largely from human cognitive processes in their treatment of knowledge. Specifically, our preceding discussion highlights a substantial research gap for knowledgeaware models: existing model designs often lack a solid theoretical foundation, consequently failing to adequately encapsulate human knowledge-based processes in a cognitively tenable manner.

To bridge this research gap, this paper explores how AI can harness explicit human knowledge in a manner reminiscent of human cognition. The closest study akin to ours was conducted by Wang et al. [95], who fused external concept knowledge with wordand character-level information to construct text classification models. It is worth noting that our proposed knowledge-aware learning framework is significantly different from theirs in three fundamental aspects. First, their approach merely introduced external knowledge as supplementary vectors alongside word embeddings, neglecting to capture the structural relationships inherent in knowledge. As indicated by schema theory, humans process knowledge in a structured manner, assimilating and consolidating pertinent knowledge into structured frameworks. Second, humans possess an extensive array of diverse knowledge types, whereas their retrieved knowledge was confined to conceptual definitions—specifically, IsA relations. Hence, their external knowledge fell short of encapsulating the comprehensiveness of human knowledge. Third, while they did incorporate a knowledge selection mechanism to identify the top 10 concepts, their lexical-semantic analysis approach inadequately aligns with how humans utilize taskembedded cues to signify the direction or domain for activating relevant knowledge from long-term memory. In summary, these limitations can be traced back to the fundamental issue that their model lacked a theoretical foundation and, consequently, lacked cognitive plausibility. As a result, their model differs significantly from human cognition in its treatment of knowledge.

In our study, we introduce a novel knowledge-aware learning framework guided by schema theory, mirroring the knowledge-based processes inherent in human learning, spanning knowledge acquisition, representation, activation, and utilization. Critically, distinct from existing pre-trained LLMs and knowledge-aware approaches, our proposed design is deeply rooted in cognitive learning theories, rendering it both an augmentation of human intelligence and cognitively plausible. This design enhances AI’s learning capabilities, aligning them more closely with those of humans. In the subsequent section, we will delve into the details of the design process.

## Schema Theory Guided Knowledge-Aware Learning Framework

In this section, we introduce the detailed design rationale and processes of our framework. Specifically, we have followed the information systems design theory (ISDT), a structured framework that formalizes the pivotal elements to steer the design process [93]. The adoption of the ISDT paradigm serves a dual purpose: it ensures our study aligns seamlessly with previous design science research [1, 51, 70] and guarantees that the design has been executed effectively and feasibly [36]. The ISDT comprises four components: kernel theories, which provide a theoretical underpinning and govern the design; metarequirements, specifying the design objectives derived from the kernel theories; metadesigns, the concrete design artifacts postulated to fulfill these metarequirements; and testable hypotheses, instrumental in evaluating the design’s effectiveness. Table 1 encapsulates these four components as they relate to our proposed learning framework. In the next four subsections, we offer comprehensive discussions of each component.

Table 1. ISDT Components of the Schema Theory-Guided Knowledge-Aware Learning Framework.

<table><tr><td>1. Kernel Theory</td><td>Schema Theory</td></tr><tr><td>2. Metarequirements</td><td>The design should include four key elements suggested by kernel theory: (1) A large knowledge base to capture acquired knowledge; (2) organizing acquired knowledge into structural schemata, captured by concepts and the relations among them; (3) a schema activation mechanism to retrieve the contextually relevant knowledge schema from the large knowledge base; and (4) a learning model to integrate the activated knowledge schema with the focal information to make predictions.</td></tr><tr><td>3. Metadesign</td><td>To meet the metarequirements, the specific metadesign components are as follows:(1) Utilization of ConceptNet as a large human knowledge base to mimic the rich knowledge acquired during human learning stored in long-term memory.(2) Organizing knowledge, represented as knowledge triples (concepts and their relations), into structural schemata, which can be retrieved and activated during learning.(3) Use of a domain-specific contextual knowledge graph with edge weights to guide the knowledge activation process to retrieve the contextually relevant knowledge in a human-like manner.(4) Adoption of a deep learning model to integrate activated knowledge schema with focal document information to complete learning tasks.</td></tr><tr><td>4. Testable Hypotheses</td><td>Comprehensive evaluations of the effectiveness of the learning framework in processing and utilizing knowledge to improve the performance of text analytics tasks (learning effectiveness, efficiency, and robustness). Specific testable hypotheses are as follows:Hypothesis 1 (H1): Effectiveness of the complete design in improving the performance of a series of text analytics tasks in terms of learning effectiveness and efficiency.Hypothesis 2 (H2): Robustness of the design against noise and incompleteness in the knowledge base.Hypothesis 3 (H3): Effectiveness of each component in our design.Hypothesis 4 (H4): Relationships and interactions among different types of knowledge.</td></tr></table>

## Kernel Theory

Our kernel theory stems from the schema theory, which posits that human learning can be dissected into a sequence of knowledge-centric processes. As we engage with the world, we acquire knowledge by conceptualizing it into concepts and relationships [58] and represent the knowledge by interlinking it with our pre-existing knowledge stored in long-term memory. When confronted with a learning task, we activate pertinent knowledge and utilize it in conjunction with the focal task information to complete the learning. These knowledge-driven processes empower humans to acquire proficiency and effectiveness in learning, often from just a few instances [3].

In particular, one assumption regarding schema activation posits that certain words possess suggestive qualities, effectively signaling a specific schema [5]. For instance, the mention of “deep learning” may activate the “artificial intelligence” schema. However, more frequently, a solitary stimulus may be insufficient for precise schema activation, merely suggesting the relevance of several schemata [5]. Consider the mention of “apple,” which can evoke various schemata such as “fruit” or “technology company.” With the provision of additional stimuli like ‘iPhone” and “Tim Cook,” the possibilities narrow, and ideally, learners discern the most proper schema. Notably, the knowledge schemata stored in longterm memory are task- and context-independent, whereas the activation of schema is a dynamic process contingent upon the specific tasks at hand.

## Metarequirements

Consequently, to build a knowledge-aware learning framework that emulates human knowledge processing, the design should closely mirror the schema theory’s delineated processes. First, the design should encompass a large knowledge base to capture prior acquired knowledge (metarequirement 1), capturing a wide spectrum of prior knowledge akin to the vast wealth of commonsense and background knowledge that humans accumulate. Second, given that knowledge is not randomly stored but follows a structured pattern in the brain, our design should organize acquired knowledge into structural schemata (metarequirement 2), characterized by concepts and the relationships connecting them. Third, considering that a substantial volume of knowledge is encapsulated within schemata, and only a specific subset is pertinent, the design should encompass a schema activation mechanism (metarequirement 3) that determines which schema, among many, should be activated for a given learning task. Lastly, after activating the relevant knowledge, the design should include a learning model to integrate the activated schema with the focal information (metarequirement 4) to complete the learning.

## Metadesign

## Complete Design

The complete design is illustrated in Figure 2, comprising four core design elements aimed at fulfilling the aforementioned metarequirements. First, we adopt ConceptNet, a vast repository of human knowledge, to mirror the background knowledge we amass through our interactions with the world (metadesign element 1). Second, instead of treating knowledge independently, our framework organizes knowledge schemata, represented as knowledge triples (concepts and their relations), into knowledge structures, mirroring how humans represent and store knowledge in our minds (metadesign element 2). Third, we incorporate a schema activation mechanism, grounded in relevance scores denoted by edge weights, that assesses the pertinence of schemata to the focal learning tasks, enabling the activation of contextually relevant knowledge (metadesign element 3). Finally, our design features a learning model that combines a bidirectional long short-term memory (bi-LSTM) with a GCN, facilitating the integration of the activated knowledge schema with the focal document information in the final predictions (metadesign element 4). Subsequent subsections will delve deeper into each specific design element, discussing their rationale and how they correspond to the identified metarequirements.

![](/api/attachments/WADKTHC2/fulltext/images/737c83b2ff269c4f1a20ab03f8823bbff53c79d0c304d9425a148ac4ddea90e9.jpg)  
Figure 2. Illustration of the Complete Schema Theory-Guided Knowledge-Aware Learning Framework

## Metadesign Element 1: Large Knowledge Base as Acquired Knowledge

The knowledge housed in human long-term memory is characterized by extensive capacity, comprehensiveness, and multifaceted nature [20, 48]. To mirror these qualities in our knowledge-aware framework design, we use ConceptNet to represent a broad repository of human knowledge. Our reasons for choosing ConceptNet over other common knowledge bases, such as WikiData, Freebase, OpenCyc, DBPedia, and ATOMIC, are twofold. First, integrating concepts and relationships from many existing knowledge bases, ConceptNet is currently one of the largest commonsense knowledge bases available, encompassing approximately 3.1 million concepts and 38 million relations spanning a diverse spectrum of domains [87]. Second, compared to other popular commonsense knowledge databases, such as ATOMIC [82], which mainly focuses on inferential knowledge organized as only if-then relations, ConceptNet captures a wide range of semantic relationships and human knowledge, represented by 36 unique types of relations [87]. As a result, ConceptNet has become a key player in advancing the integration of human knowledge into AI research because of its large size and the wide range of everyday, practical knowledge it holds [57]. Since ConceptNet offers an unmatched level of detailed knowledge, we use it as our main source to mimic the vast amount of knowledge that humans keep in their long-term memory.

Specifically, knowledge in ConceptNet is structured in the form of knowledge triples, such as (Apple; IsA; Fruit), where concepts encompass nouns, adjectives, or verbs [87]. Note that the raw knowledge triples present in ConceptNet do not inherently constitute knowledge structures and, therefore, should not be immediately regarded as schemata. To faithfully mirror how knowledge schemata are represented in the human cognitive landscape, we must integrate pertinent knowledge into structured formats, which we will discuss next.

## Metadesign Element 2: Organizing Knowledge as Knowledge Structures

As discussed earlier, knowledge is not randomly organized but rather resides in schemata, which are akin to knowledge structures. Knowledge structures encompass the representation of knowledge using concepts and the intricate relationships connecting them [7, 25, 43, 63]. These structural attributes of schema closely parallel the knowledge triples found in ConceptNet. As illustrated in Figure 1, leveraging concepts as nodes and relations as edges, we possess the capability to reconfigure the knowledge triples extracted from ConceptNet into knowledge structures, mirroring the manner in which humans store knowledge within structured schemata. Consequently, the definition of schema as a knowledge structure and the characterization of ConceptNet as a knowledge graph harmonize seamlessly. Thus, we have transformed the knowledge triples procured from ConceptNet into substantial knowledge schemata, which will play a key role in the subsequent knowledge activation phase, as discussed in the next.

## Metadesign Element 3: Schema Activation Mechanism

Within the abundance of knowledge residing in schemata, only a select portion is relevant to the learning and should be retrieved—a phenomenon termed schema activation [67]. However, the schemata we have built serve as a comprehensive knowledge repository, akin to the background knowledge stored in the human long-term memory. Given its sheer volume, integrating the entirety of this knowledge base is often counterproductive, as the inclusion of irrelevant knowledge can compromise the learning process [106]. Humans adeptly connect the salient task information with their pre-existing knowledge to activate the pertinent schema needed to support learning [69]. However, the extensive schemata derived from ConceptNet lack any form of prioritization, rendering all knowledge on equal footing. Yet, it is imperative to exercise discernment in activating the pertinent knowledge schema. For example, in our news classification scenario, depicted in Figure 3a, we must activate (Apple; IsA; Technology Company) within the technology schema. However, due to the lack of weights, the current schemata do not allow such knowledge activations.

To address this issue, we propose a strategy aimed at ascertaining the relative importance of knowledge based on its relevance to the learning tasks. Schema theory posits that learning is an interactive process wherein learners construct meaningful knowledge representations using their schemata. External cues embedded in the text should guide learners toward the pertinent schema within their memory, aligning with the demands of the focal task [69]. To fulfill this, we have devised a strategy inspired by the term frequency-inverse document frequency (TF-IDF), a widely used technique in information retrieval research [2]. TF-IDF hinges on the premise that a term’s importance is directly related to its frequency within a specific document but inversely correlated with its prevalence across the entire corpus [2]. In our context, to quantify the significance of a knowledge triple in a learning task, we gauge its frequency within the designated domain (analogous to term frequency) against its prevalence in the broader scope of worldly knowledge (analogous to inverted document frequency). As such, the weights assigned to relations for a particular task can be calculated as follows:

![](/api/attachments/WADKTHC2/fulltext/images/08dc8fd0e0cab810cdea0d9959d12ac05fd0f6e019410bfaecb04180e10d9a2e.jpg)  
Figure 3. Structural knowledge graphs (a) without edge weights and (b) with edge weights (arbitrary numbers for demonstration purposes).

$$
W (w _ {i}, w _ {j}) = \frac {\# N _ {t a s k} (w _ {i} , w _ {j})}{\# N _ {g e n e r a l} (w _ {i} , w _ {j}) + 1}\tag{1}
$$

where $W \big ( w _ { i } , w _ { j } \big )$ denotes the score between concepts $w _ { i }$ and $w _ { j } , \# N _ { t a s k } \big ( w _ { i } , w _ { j } \big )$ is the frequency of a concept pair $\left( w _ { i } , w _ { i } \right)$ in the task corpus (e.g., all news articles for a news classification task), and $\# N _ { g e n e r a l } \left( w _ { i } , w _ { j } \right)$ is its frequency in the general and broader corpus. The implementation involved three steps, as depicted in Figure 4. First, to obtain $\# N _ { g e n e r a l } \left( w _ { i } , w _ { j } \right)$ , we utilized Wikipedia, one of the largest knowledge sources covering a wide range of domains [1], to calculate the frequencies of relations in the broader context of the world. We initiated the process by eliminating stopwords and non-English words from each article in the Wikipedia collection. We then employed a fixed-size sliding window with a size of 20 to scan the articles and capture the co-occurrence of concept pairs. This window size balance captured relevant long-distance relationships while maintaining contextual relevance, a practice adopted in prior studies [12, 15, 49]. Then, for our specific task (e.g., news classification), we followed a similar procedure to determine the cooccurrence of concept pairs as $\# N _ { t a s k } \Big ( w _ { i } , w _ { j } \Big )$ . Finally, to assign weights to relations, we compared their frequency in the task corpus to that in the general corpus, as outlined in Eq. (1).

For instance, in a news classification task, let’s consider the concept pair (Apple, Technology Company), which appears 120 times in the entire task corpus $( \# N _ { t a s k } \big ( w _ { i } , w _ { j } \big ) )$ and 999 times in the general Wikipedia collection $( \# N _ { g e n e r a l } \left( w _ { i } , w _ { j } \right) )$ ). Given that the relationship between these two concepts is “Apple is a technology company,” according to equation (1), the weight for the knowledge triple (Apple; IsA; Technology Company) in our schemata is calculated as $1 2 0 / ( 9 9 9 + 1 ) = 0 . 1 2$ . Similarly, for the concept pair (Apple, Fruit), it appears 10 times in the task corpus and 9,999 times in the general Wikipedia collection. Hence, for the relationship “Apple is a fruit,” the weight for the knowledge triple (Apple; IsA; Fruit) is computed as $1 0 / ( 9 , 9 9 9 + 1 ) \ = 0 . 0 0 1$ . Consequently, as shown in Figure 3b, based on these weights, the former relation is deemed more relevant to the specific task and should be activated.

![](/api/attachments/WADKTHC2/fulltext/images/551d77c8a6b6626cbab0817605c6e82fa96cdb564e98101d356fc4ed4a83ebaa.jpg)  
Figure 4. Illustration of the construction procedures of a contextual knowledge graph with weights.

It is worth noting that, from the TF-IDF perspective, a concept pair with a high weight has a high occurrence likelihood in the target corpus and a low occurrence likelihood in the general corpus (i.e., Wikipedia). In essence, concept pairs with high weights are suitable for capturing the distinctive characteristics of the target domain relative to the general domain. Importantly, this knowledge activation strategy aligns with human knowledge-based processes. Schema theory posits that schemata represent knowledge that is applicable to a broad array of situations and contexts, transcending specific instances [9]. This generality is pivotal to human learning as it enables the application of abstract, context-independent knowledge across diverse contexts and tasks [7]. Given that ConceptNet serves as a comprehensive knowledge base spanning various domains, our design seeks to align task information with the relevant segment of the generic knowledge schemata housed within ConceptNet through schema activation.

For implementation, for a given document, our knowledge activation process entails a topological expansion to retrieve all neighboring relations (one edge distance) from our knowledge base. These relations are then ranked based on their weights, and the top K relations (K being a hyperparameter) are activated. In cases where the number of relations falls short of K within one edge distance, we extend the search to two edge distances and rank all relations solely based on their edge weights, without differentiating edge distance. This knowledge activation process can be iteratively performed until the requisite knowledge volume is retrieved. It’s worth noting that these weights do not replace the relations between concepts; they are employed exclusively during the knowledge activation step to identify which relations are most pertinent to the task.

## Metadesign Element 4: Integrate Activated Schema with the Focal Document

Once we’ve activated the relevant knowledge, our next step involves constructing a model to complete the learning. As discussed earlier, schema theory underscores the interactive nature of learning, necessitating the integration of relevant background knowledge with task-specific information [17]. Therefore, our approach involves the fusion of information derived from the focal text with the retrieved knowledge schema. We employ two representations: text-based representation and knowledge graph representation. The former emulates how humans utilize local information within a document, while the latter captures activated external knowledge schema beyond the local text to mimic how humans recall and utilize knowledge stored in their long-term memories.

Specifically, we employ a GCN to embed our knowledge graph, which extends the capabilities of deep neural networks to graph-structured data [53]. For an input graph, a GCN efficiently disseminates information across the nodes, capturing the underlying relationships conveyed through connections [46]. Given that our contextual knowledge graph can go beyond one edge distance, we adopt the two-layer GCN model (source code: https://github.com/tkipf/gcn) introduced by Kipf and Welling [46]. The GCN operates directly on the activated knowledge schema, generating embeddings for individual documents based on the properties of connected concepts and relations. The resultant fixedlength embeddings, which are supposed to encapsulate external relevant knowledge for each document, are fed into the softmax classifier.

To capture the essential information embedded within the target document, we employ a bi-LSTM encoder to transform textual content into fixed-length embeddings. These embeddings are also input into the softmax classifier. In addition to pre-trained GloVe vectors, our encoder incorporates concept embeddings from knowledge triples, enabling the modeling of externally retrieved knowledge in tandem with the document’s focal information. To derive these concept and relation embeddings, we employ TransE, one of the first and most representative knowledge graph embedding models designed to learn continuous vector representations of entities and relations in a knowledge graph [14]. Despite its simplicity, TransE often achieves competitive performance compared to more complex knowledge graph embedding methods on various tasks [96]. In addition, TransE characterizes a triple (concept1, relation, concept2) following a common assumption concept1 + relation ≈ concept2. Given its simple architecture, TransE has an interpretable geometric interpretation making it easier to understand and interpret [39]. Moreover, due to its simplicity, TransE is also computationally efficient and scalable, making it suitable for large-scale knowledge graphs with millions of entities and relations [96]. Overall, TransE offers a balance of effectiveness, simplicity, efficiency, and interpretability, making it a popular choice for our knowledge graph embedding tasks, particularly when our goal is to project the knowledge-based processes inherent in human learning into the knowledgeaware learning framework design, rather than comparing different knowledge graph embedding techniques.

Specifically, to train the TransE model, we compile activated knowledge triples from all documents within the task corpus, forming the contextual knowledge graph from the preceding stage. The TransE model is then trained on these aggregated triples, generating node embeddings and relation embeddings for each edge. Notably, we opt for the contextual knowledge graph to train the TransE model instead of the complete knowledge triples found in ConceptNet. This decision allows us to capture contextually relevant, task-specific knowledge present in the contextual knowledge graph post-knowledge activation, as opposed to the general and contextindependent knowledge contained in the full ConceptNet knowledge graph. It is worth mentioning that other advanced knowledge graph embedding methods (e.g., TransH, TransR, TransD) can also be applied to our knowledge embeddings. We refer the audience to a review article [96] for other knowledge graph embedding techniques, which could be potentially compared and adopted for our design in future studies.

Table 2. Implementation details and parameters.

<table><tr><td>Design Element</td><td>Implementation Details</td></tr><tr><td>1. Large knowledge base as acquired knowledge</td><td>Knowledge graph: ConceptNet</td></tr><tr><td>2. Organizing knowledge as knowledge structures</td><td>Nodes: wordsEdges: relations between a pair of words</td></tr><tr><td>3 .Schema activation mechanism</td><td>Dataset: Wikipedia dump retrieved on February 20, 2020Pre-processing: removing stopwords and non-English wordsWord co-occurrence window size: 20Quality improvement: removing word pairs with frequencies less than 5Knowledge graph: ConceptNetExpanded knowledge graph size (K): 10~200 (100 delivered best results)</td></tr><tr><td>4. Integrate activated schema with focal document</td><td>GCN architecture: Two convolutional layers with 16 hidden layersGCN learning rate: 0.001Text encoder architecture: Two-layer bidirectional LSTM with hidden size 64Dropout: 0.5 in each layerEpochs: 200 with early stopping (no decrease of validation loss for 10 consecutive epochs)Batch size: 50Optimizer: AdamLearning rate: 0.01 with weight decay of 0.0005Word embeddings: pre-trained 300-dimension Glove vectors trained on a corpus of 840 billion tokensEntity and relation embedding algorithm: TransEEntity and relation embeddings size (concepts and): 100</td></tr><tr><td>5. Others</td><td>Deep learning libraries: Tensorflow and KerasCPU: Intel Core i7-13700KF with 32GB memoryGPU: NVIDIA GeForce GTX 3070 with 8GB memory</td></tr></table>

GCN, graph convolution networks; LSTM, long-short term memory.

## Design Summary

To summarize, our complete design framework operates as follows. First, to capture the knowledge acquisition, we employ the ConceptNet knowledge graph to resemble how humans store knowledge in long-term memory. Second, to model knowledge representations, we structure the knowledge gleaned from ConceptNet into organized knowledge structures to mirror the structural representation of knowledge in human cognition. Third, to achieve effective knowledge activation, we introduce a novel relevance scorebased approach, which selectively activates contextually relevant knowledge schemas. Finally, for knowledge utilization, we combine a bi-LSTM encoder with a GCN to seamlessly integrate the activated knowledge schema with focal document information. Our key design novelty and contribution are that, for the first time, guided by schema theory, our proposed learning framework uniquely replicates the entirety of human knowledge-based learning processes. Further implementation details are available in Table 2.

## Testable Hypotheses

Testable hypotheses are intended to evaluate how well the proposed metadesign satisfies our metarequirements [1, 93]. Our learning framework entails four evaluation aspects: (1) the design’s ability to enhance NLP performance to achieve a more human-like level, in terms of learning effectiveness and efficiency; (2) the robustness of design across diverse scenarios, similar to the robustness of human learning; (3) the effectiveness of individual design elements; and (4) the roles played by various types of knowledge in supporting learning. Addressing these four aspects necessitates multifaceted evaluation solutions [31, 36], all of which require the instantiation of our proposed design framework as a foundation for evaluating its effectiveness and applicability.

As illustrated in Table 1, we have formulated four testable hypotheses for evaluation purposes. To test H1, we evaluate the proposed framework’s performance across a range of text analytics tasks, encompassing both learning effectiveness and efficiency; to test H2, we assess the design’s robustness under diverse scenarios; to test H3, we conduct a series of ablation studies to affirm the effectiveness of key design components; and to test H4, we validate the relationships among different types of knowledge. In the following section, we will elaborate on the detailed experiments and results.

## Experiments and Results

To assess our proposed novel learning framework, we have instantiated it within the realm of text analytics, with a particular emphasis on its problem-solving capabilities— a specific cognitive task or activity that falls under the umbrella of learning [5]. Specifically, we have focused on two text analytics problem-solving tasks: text classification and natural language inferences (NLI). We have chosen these tasks for two compelling reasons. First, both tasks exhibit significant potential for enhancing business decision-making. Text classification, for instance, stands as one of the most widely employed text analytics techniques across various business applications, including opinion mining, social media analytics, and medical diagnoses [6, 7]. Meanwhile, NLI, crucial for language comprehension, plays an important role in diverse NLP systems, such as chatbots and question-answering systems [8, 9]. Second, these two tasks have undergone extensive research, resulting in well-established baselines. Notably, for both tasks, we have included both knowledge-aware models and state-of-theart pre-trained LLMs. For a comprehensive overview of the rationale behind incorporating each model and concise descriptions, please refer to Table 3.

## Experiment 1: Efectiveness of the Learning Framework

In our first experiment, we assessed the effectiveness of our learning framework by applying it to a series of text analytics tasks. Specifically, our focus encompassed four classification datasets and one NLI dataset, all of which have been widely used as benchmarks in NLP research. Table 4 shows the results of our experiment and the performance obtained from the benchmark methods (best results are in bold). There are two key insights.

First, our novel learning framework consistently outperformed existing knowledgeaware models, namely Text GCN and KIM, across all tasks. For instance, when compared to Text GCN, we achieved an impressive 8.3 percent increase in the F1 score for the Movie

Table 3. Baseline models and description.

<table><tr><td>Task</td><td>Model</td><td>Implicit or Explicit Knowledge?</td><td>Brief Description and Implementation</td></tr><tr><td rowspan="3">Text Classification</td><td>Text GCN</td><td>Explicit</td><td>Proposed by Yao et al. [105], Text GCN is a graph-based approach that builds a text graph for a corpus based on word co-occurrence and document word relations. We used the code released by the authors:https://github.com/yao8839836/text_gcn</td></tr><tr><td>BertGCN</td><td>Implicit</td><td>Developed by Lin et al. [59], BertGCN combines BERT with GCN. BertGCN has achieved state-of-the-art performance on a wide range of text classification datasets. Code:https://github.com/ZeroRin/BertGCN</td></tr><tr><td>MTL</td><td>Implicit</td><td>Proposed by Pilault et al. [77], MTL is a pre-training-based framework consisting of a new conditional attention mechanism and task-conditioned modules that facilitate knowledge sharing. Code:https://github.com/CAMTL/CA-MTL</td></tr><tr><td rowspan="3">Natural Language Inference (NLI)</td><td>KIM</td><td>Explicit</td><td>Proposed by Chen et al. [18], KIM is a neural network-based model that is enriched with external knowledge. We selected it for its similarities to our framework: it is also based on explicit knowledge and does not use pre-trained LLMs. Code:https://github.com/lukecq1231/kim</td></tr><tr><td>EFL</td><td>Implicit</td><td>Developed by Wang et al. [97], EFL is a pre-trained LLM-based approach that reformulates an NLP task into an entailment task. EFL improves existing state-of-the-art few-shot NLI methods. Code:https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples/few_shot/efl</td></tr><tr><td>DeBERTa</td><td>Implicit</td><td>Designed by He et al. [33], DeBERTa is a pre-trained LLM that includes a disentangled attention mechanism and enhanced mask decoder. DeBERTa improves the pre-training efficiency and performance of a collection of NLP tasks, including NLI. Code:https://github.com/microsoft/DeBERTa</td></tr></table>

GCN, graph convolution networks; LLM, large language model; NLP, natural language processing; NLI, natural language inferences.

Table 4. Model performance (F1) of our framework and state-of-the-art baseline approaches.

<table><tr><td>Task</td><td>Our Design (Percent)</td><td>Text GCN (Percent)</td><td>BertGCN (Percent)</td><td>MTL (Percent)</td><td>KIM (Percent)</td><td>EFL (Percent)</td><td>DeBERTa (Percent)</td></tr><tr><td>News Classifications (R52)</td><td>95.1</td><td>93.0</td><td>95.6</td><td>94.3</td><td></td><td>Not Applicable</td><td></td></tr><tr><td>Medical Classification (Ohsumed)</td><td>69.9</td><td>67.6</td><td>71.5</td><td>70.1</td><td></td><td></td><td></td></tr><tr><td>News Classification (20-News)</td><td>89.6</td><td>85.8</td><td>89.1</td><td>88.5</td><td></td><td></td><td></td></tr><tr><td>Movie Sentiment (MR)</td><td>84.4</td><td>76.1</td><td>85.3</td><td>84.5</td><td></td><td></td><td></td></tr><tr><td>NLI</td><td>91.7</td><td></td><td>Not Applicable</td><td></td><td>87.1</td><td>91.9</td><td>91.2</td></tr></table>

Note: GCN, graph convolution networks; NLI, natural language inferences.  
Best performance highlighted in bold.

Sentiment (MR) dataset, elevating it from 76.1 percent to 84.4 percent. These results underscore the ability of our learning framework to harness knowledge more effectively than prevailing knowledge-aware approaches. Second, our results indicate that we achieved comparable performance to state-of-the-art models, which predominantly rely on LLMs such as BertGCN and DeBERTa. Notably, while our framework only outperformed state-ofthe-art models in one dataset, 20-News, it is essential to highlight that our design does not necessitate computationally expensive training or fine-tuning processes with pre-trained

Table 5. Computational comparisons (20-News).

<table><tr><td colspan="2">Our Design</td><td colspan="2">BertGCN</td></tr><tr><td>Steps</td><td>Computational Time</td><td>Steps</td><td>Computational Time</td></tr><tr><td rowspan="2">Schema activation(Wikipedia processing and contextual knowledge graph building)</td><td rowspan="2">4.5 hours on CPU(24 threads)</td><td> $Bert pre-training^a$ </td><td>4 days on 64 TPU chips</td></tr><tr><td>Bert model fine-tuning (60 epochs)</td><td>2.73 hours on GPU</td></tr><tr><td>Text classification on 20-News(200 epochs with early stopping)</td><td>0.87 hours on GPU</td><td>Text classification on 20-News(50 epochs)</td><td>2.39 hours on GPU</td></tr><tr><td>Additional Comparisons</td><td></td><td></td><td></td></tr><tr><td>Our Design</td><td></td><td>BertGCN</td><td></td></tr><tr><td>Model size (# of parameters)</td><td>8.36 million</td><td>Model size (# of parameters)</td><td>109.6 million</td></tr><tr><td>Size of external data (Wikipedia)</td><td>2.5 billion tokens</td><td> $Size of external data for Bert pre-training^1$ </td><td>3.3 billion tokens</td></tr></table>

These training details were obtained based on $\mathsf { B E R T _ { b a s e } }$ directly from Devlin et al. [22], the original BERT paper. CPU, centra processing unit; TPU, tensor processing unit; GPU, graphical processing unit

LLMs. To illustrate the efficiency of our approach, we compared the training details between our design framework and BertGCN, a pre-trained LLM-based approach, as outlined in Table 5. This comparison underscores that our design operates more resourceefficiently, boasting a substantially smaller model size and shorter computational time. The fact that our framework achieves comparable performance to state-of-the-art models without relying on LLMs opens a promising avenue for future research in developing AI that closely resembles human learning.

## Experiment 2: Learning Eficiency

Furthermore, we sought to assess the potential for enhancing learning efficiency by examining our framework’s performance under reduced training data. While Experiment 1 primarily aimed to benchmark our design against existing models to affirm its effectiveness, Experiments 2–5 were to explore how various factors impact our design’s performance. Existing research shows the pivotal roles played by task types and domains in influencing model performance [73, 99]. Task domain pertains to the specific knowledge required to solve a problem, while task type indicates the nature of the transformation needed to convert input data into output [73]. To ensure the versatility of our testbed in capturing diverse task types and domains, we replaced two tasks from Experiment 1, namely MR and NLI, with two new tasks: Adverse Drug Event (ADE) Detection and PubMed Classification. A detailed description of each task can be found in Online Supplemental Appendix 1. By introducing these new tasks, our testbed covered different domains (i.e., medical and general), as well as diverse task types involving document, sentence, and word classifications. To evaluate learning efficiency, we gradually reduced the training data from 100 percent to 1 percent, while keeping other variables constant, including hyperparameters and testing data. We then conducted a comparison involving our learning framework, the knowledge-aware Text GCN, and the LLM-based BertGCN. The results are visualized in Figure 5, from which we derive the following key insights.

First, the results illustrate the robustness of our design with limited training data, consistently outperforming both baseline methods. For instance, in the case of task R52, our performance only dropped by a mere 5.9 percent when transitioning from the complete training dataset (0.924) to utilizing just 10 percent of it (0.865). In contrast, the baseline models exhibited significantly more substantial drops, with Text GCN decreasing from 0.931 to 0.748, and BertGCN plummeting from 0.956 to 0.624 when shifting from the full training data to 10 percent of it. These findings underscore our design’s exceptional ability to enhance learning efficiency under reduced training data conditions.

Medical Classification (Ohsumed)  
![](/api/attachments/WADKTHC2/fulltext/images/036a48e45180e143560b4562e41093ea68654b383064ec9ba0d416a3999b88de.jpg)

![](/api/attachments/WADKTHC2/fulltext/images/976f9502d2dbb0da37dad074518a2b159cfb8db5fbb974af60183bfbc5f246e7.jpg)

![](/api/attachments/WADKTHC2/fulltext/images/181173ab75a9f2acfc8c1852554da0a0e1d8c6ce3fc2027dc41b8fb708572c6a.jpg)

![](/api/attachments/WADKTHC2/fulltext/images/184a9ee438e334d4cf6887f889d7a90191edcb8e5df52c0f076c258cf78e304e.jpg)

![](/api/attachments/WADKTHC2/fulltext/images/76f0a70ae646f006c743b2e7afb47fd53c89d2f6659d7d811695ea9df44737e9.jpg)  
Figure 5. Performance comparisons using diferent ratios of the training dataset.

Second, under conditions of highly limited training data, we observed that Text GCN outperformed BertGCN. For example, in the case of task 20-News, Text GCN surpassed BertGCN when retaining less than 60 percent of the training data. This result is intriguing, considering that in Experiment 1, BertGCN consistently outperformed Text GCN across all tasks. We posit that the effectiveness of pre-trained LLMs hinges on their fine-tuning for the specific downstream task. In scenarios with scant data for fine-tuning, the performance of these models suffers significantly. This finding suggests that the data-intensive nature of LLMs, especially during fine-tuning, can severely limit their applicability in tasks with limited data availability.

A third noteworthy observation is the significant enhancement in learning efficiency across all tasks within our learning framework. This consistent improvement spans various task types and domains, indicating promising generalizability. Therefore, our design holds the potential for application in a wide array of tasks without necessitating substantial redesign or reengineering. This discovery carries a promising implication: our cognitive theory-guided AI design approach aligns our knowledge-aware model more closely with human-like learning, as human learning is renowned for its capacity to generalize knowledge to novel tasks and situations [48].

## Experiment 3: Parameter Sensitivity Analysis and Robustness Check

The preceding two experiments have confirmed the effectiveness and efficiency of our design in enhancing learning capabilities, thus supporting testable hypothesis H1. As highlighted by Lake et al. [48], beyond effectiveness and efficiency, human learning also demonstrates robustness through trial and error across various contexts. As a result, it is integral to evaluate the resilience of our design when confronted with imperfect or potentially problematic situations. Worth noting is that our framework relies on an external knowledge base, while all existing knowledge bases share common limitations, encompassing improper or erroneous relations, and are far from exhaustive [68]. Therefore, the absence and inaccuracies of relations pose critical challenges to our design. To address this concern, we conducted a series of experiments to assess the robustness of our design in the face of potential knowledge base incompleteness and noisiness (i.e., incorrect relations).

## Resilience to Knowledge Graph Incompleteness

The experiment was devised as follows: prior to employing ConceptNet, we randomly omitted a certain percentage of knowledge triples (i.e., 10 percent, 50 percent, or 90 percent) to simulate scenarios involving missing knowledge. Then, we conducted experiments using the incomplete knowledge graph, with results summarized in Table 6. Notably, each percentage drop was tested 10 times, and we present the average performance. It is noteworthy that with 10 percent knowledge relations missing, the performance shows minimal and statistically insignificant decreases. When we dropped 50 percent of the knowledge triples, we retained over 80 percent of the performance improvements, and for two out of the five tasks (R52 and 20-News), the performance decreases were statistically insignificant. However, upon reducing the knowledge triples by 90 percent, we preserved roughly 50 percent of the performance improvements for most tasks, but all performance decreases were statistically significant.

Table 6. Evaluations of the impacts of knowledge graph incompleteness<sup>a,b</sup>

<table><tr><td>Task</td><td>News Classifications (R52)</td><td>News Classifications (20-News)</td><td>Medical Classifications (Ohsumed)</td><td>PubMed Classification (PubMed_20K)</td><td>ADE Detection</td></tr><tr><td>Baseline</td><td>0.883</td><td>0.738</td><td>0.481</td><td>0.779</td><td>0.871</td></tr><tr><td>Complete KGs</td><td>0.924(100 percent)</td><td>0.823(100 percent)</td><td>0.612(100 percent)</td><td>0.897 (100 percent)</td><td>0.922(100 percent)</td></tr><tr><td>Drop</td><td>0.923(97.6 percent)</td><td>0.821(97.5 percent)</td><td>0.608(96.9 percent)</td><td>0.892 (95.8 percent)</td><td>0.92(96.1 percent)</td></tr><tr><td>10 percent KGs</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Drop</td><td>0.917(82.9 percent)</td><td>0.809(83.5 percent)</td><td>0.588(81.7 percent)**</td><td>0.874 (80.5 percent)*</td><td>0.913(82.4 percent)*</td></tr><tr><td>50 percent KGs</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Drop</td><td>0.904(51.2 percent)***</td><td>0.778(47.1 percent)***</td><td>0.534(40.5 percent)***</td><td>0.831 (44.1 percent)***</td><td>0.892(41.2 percent)***</td></tr><tr><td>90 percent KGs</td><td></td><td></td><td></td><td></td><td></td></tr></table>

All performances are weighed F1 scores; the numbers in parentheses are the percentage of improvement brought by the corresponding knowledge elements.

Table 7. Evaluations of impacts of noise in the knowledge graph<sup>a,b</sup>

<table><tr><td>Task</td><td>News Classifications (R52)</td><td>News Classifications (20 News)</td><td>Medical Classifications (Ohsumed)</td><td>PubMed Classification (PubMed_20K)</td><td>ADE Detection</td></tr><tr><td>Baseline</td><td>0.883</td><td>0.738</td><td>0.481</td><td>0.779</td><td>0.871</td></tr><tr><td>Complete KGs</td><td>0.924(100 percent)</td><td>0.823(100 percent)</td><td>0.612(100 percent)</td><td>0.897 (100 percent)</td><td>0.922(100 percent)</td></tr><tr><td>1 percent noise</td><td>0.924(100 percent)</td><td>0.821(97.6 percent)</td><td>0.610(98.5 percent)</td><td>0.892 (95.8 percent)</td><td>0.920(96.1 percent)</td></tr><tr><td>5 percent noise</td><td>0.922(95.1 percent)</td><td>0.820(96.5 percent)</td><td>0.608(96.9 percent)</td><td>0.887 (91.5 percent)</td><td>0.918(92.2 percent)</td></tr></table>

All performances are weighed F1 scores; the numbers in parentheses are the percentage of improvement brought by the corresponding knowledge elements. <sup>b</sup>The results were obtained by our framework without text representation portion. ADE, adverse drug event.

These results underscore the resilience of our framework when faced with missing knowledge, and substantial performance drops only became evident when more than half of the relations were absent. This finding suggests that our design can still draw upon sufficient useful knowledge to accomplish the tasks when an external knowledge base lacks a relatively small (e.g., 10 percent) to moderate (e.g., 50 percent) portion of its relations. However, as one might expect, as the knowledge graph’s incompleteness escalates (e.g., 90 percent of relations are missing), it becomes progressively challenging to supplement sufficient relevant knowledge, thereby impacting learning outcomes.

## Resilience to Noise in the Knowledge Graph

To assess our design’s sensitivity to potential noise within the knowledge graphs, we introduced noise into ConceptNet by randomly selecting a certain percentage of knowledge triples and assigning incorrect relations. We used two thresholds (1 percent and 5 percent) since most existing knowledge graphs typically maintain accuracy levels within the range of 99 percent to 95 percent [68]. Similarly, each threshold underwent 10 experimental runs, and Table 7 summarizes the results. We observed minimal and statistically insignificant framework decreases in both the 1 percent and 5 percent noise scenarios. This observation signifies that our approach showcases robustness when facing incorrect relations within external knowledge bases. This discovery carries significant implications, as it suggests that current knowledge graphs offer acceptable data quality for our approach. We encourage researchers to delve into this research avenue further.

In summary, these two experiments demonstrate the robustness of our learning framework in the context of incomplete and noisy knowledge graphs. Therefore, H2 is supported.

Table 8. Ablation study results.

<table><tr><td>Model</td><td>R52</td><td>20-News</td><td>Ohsumed</td><td>MR</td></tr><tr><td>Our Full Design</td><td>95.1 percent</td><td>89.6 percent</td><td>69.9 percent</td><td>84.4 percent</td></tr><tr><td>No GCN</td><td>92.2 percent</td><td>87.5 percent</td><td>66.8 percent</td><td>79.7 percent</td></tr><tr><td>No bi-LSTM encoder</td><td>91.8 percent</td><td>84.2 percent</td><td>67.2 percent</td><td>79.2 percent</td></tr><tr><td> $No knowledge activation^a$ (No contextual knowledge graph)</td><td>92.8 percent</td><td>86.9 percent</td><td>69.1 percent</td><td>81.9 percent</td></tr></table>

Knowledge triples were supplemented without selections. If knowledge triples retrieved were more than knowledge graph size K, then K random knowledge triples were incorporated. MR, movie sentiment; GCN, graph convolution networks; LSTM, long-short term memory.

## Experiment 4: Ablation Study

To gain deeper insights into the key design components within our framework, we conducted a series of ablation studies, removing one core element in each experiment. Our hypothesis centers on three facets that we believe contribute to the performance enhancements of our design: (1) an innovatively designed schema activation strategy to activate the contextually relevant knowledge; (2) a GCN-powered model to capture the retrieved knowledge schema, in the form of knowledge structure; and (3) a bi-LSTM encoder to model the information embedded in the focal document. The results in Table 8 validate the significant role played by these three pivotal design elements in enhancing the effectiveness of our proposed learning framework. Therefore, H3 is supported.

## Experiment 5: More Delicate Knowledge Mechanisms

In this experiment, we sought to explore an alternative application of our framework: delving into the distinct roles of various types of knowledge in the learning process. Cognitive science has posited the categorization of knowledge into three types: conceptual, procedural, and contextual knowledge [4]. Conceptual knowledge includes facts and concepts, serving as the foundation of learning, while procedural knowledge delves into the sequence of actions, comprising rules and steps required to achieve a specific objective [69]. Both conceptual and procedural knowledge constitute what is known as the content knowledge [19]. Contextual knowledge encapsulates information of the broader context, encompassing the situation, relevant concepts, and appropriate course of action to attain specific goals within the given context. In essence, it facilitates the activation of suitable conceptual and procedural schemas when faced with a learning task [92]. The learning process typically commences with the contextual schemata, which seek out the pertinent conceptual and procedural schemata required to address the learning task at hand [69].

Hence, we grouped knowledge into three distinct types and conducted an in-depth exploration of their roles and relationships. Specifically, for each task, we introduced varying knowledge types, either in isolation or combination, allowing for a granular assessment of their individual contributions. The primary evaluation findings are presented in Table 9. The implementation details, including knowledge definitions, grouping criteria, and additional results, are described in Online Supplemental Appendices 2 and 3. It is worth highlighting that, rather than employing the complete framework, we intentionally omitted the text representation component. This strategic omission enables us to pinpoint the distinct impacts arising from the different knowledge types. Consequently, the results delineated in Table 9 diverge from those in Experiment 1 (Table 4).

Table 9. Performance comparison with diferent types of knowledge<sup>a,b</sup>

<table><tr><td>Task</td><td>News Classification (R52)</td><td>News Classification (20-News)</td><td>Medical Classification (Ohsumed)</td><td>PubMed Classification (PubMed_20K)</td><td>ADE Detection</td></tr><tr><td>Classification Level</td><td>Document</td><td>Document</td><td>Document</td><td>Sentence</td><td>Word</td></tr><tr><td>Baseline</td><td>0.883</td><td>0.738</td><td>0.481</td><td>0.779</td><td>0.871</td></tr><tr><td>Conceptual</td><td>0.896(31.7 percent)</td><td>0.776(44.7 percent)</td><td>0.487(4.6 percent)</td><td>0.788 (7.6 percent)</td><td>0.875(7.8 percent)</td></tr><tr><td>Procedural</td><td>0.891(19.5 percent)</td><td>0.748(11.8 percent)</td><td>0.468(-9.9 percent)</td><td>0.781 (1.7 percent)</td><td>0.873(3.9 percent)</td></tr><tr><td>Contextual</td><td>0.895(29.3 percent)</td><td>0.757(20.0 percent)</td><td>0.589(82.4 percent)</td><td>0.876 (82.2 percent)</td><td>0.906(68.6 percent)</td></tr><tr><td>Conceptual and Procedural</td><td>0.908(61.0 percent)</td><td>0.792(63.5 percent)</td><td>0.444(-7.7 percent)</td><td>0.792 (11.0 percent)</td><td>0.879(15.7 percent)</td></tr><tr><td>Conceptual, Procedural, and Contextual</td><td>0.924(100 percent)</td><td>0.823(100 percent)</td><td>0.612(100 percent)</td><td>0.897(100 percent)</td><td>0.922(100 percent)</td></tr></table>

Note: <sup>a</sup>All performances are weighed F1 scores; the baseline performance was obtained with the model without incorporating any knowledge; the numbers in parentheses are the percentage of improvement brought by the corresponding knowledge types. <sup>b</sup>The results were obtained by our framework without text representation portion, hence, the results are diferent from those reported in Table 4 with the full learning framework. ADE, adverse drug efect. Best performance highlighted in bold.

The results in Table 9 yield intriguing insights that offer elucidations regarding H4. First, the consistently more substantial enhancement stemming from conceptual knowledge, in comparison to procedural knowledge, underscores the foundational significance of conceptual knowledge in the learning process. Second, our findings unveil synergistic effects, wherein the combined impact of multiple knowledge types surpasses the cumulative effect of each in isolation. For instance, the combined impact of conceptual and procedural knowledge for R52 amounted to 61.0 percent, whereas the sum of their individual effects is 51.2 percent (31.7 percent + 19.5 percent). Similarly, the cumulative effects of all three knowledge types reached 100 percent, in contrast to the sum of their individual effects at 80.5 percent (31.7 percent + 19.5 percent + 29.3 percent). Detailed group-wise comparisons are documented in Online Supplemental Appendix 2.

## Discussions

While the significance of knowledge is widely acknowledged in both human learning and AI, current knowledge-aware models often deviate from how humans engage with knowledge. In this study, drawing on cognitive science theories, we adopted the DSR methodology to introduce a schema theory-guided knowledge-aware learning framework to parallel humans’ knowledge-based learning processes. We have effectively addressed all the research questions we set out to explore.

Specifically, to address RQ1, we demonstrated that our framework is a pioneering effort to emulate the knowledge-based processes employed by humans during learning. Our research strategy, underpinned by cognitive theories, represents a significant technical innovation. It underscores our contribution to crafting AI that aligns with cognitive plausibility. To answer RQ2, we conducted a series of experiments, pitting our design against established benchmarks. Remarkably, our model achieves comparable performance compared to state-of-the-art models, without relying on pre-trained LLMs. For RQ3, our results illuminate our design’s substantial gains in learning efficiency: achieving comparable performance with significantly less training data and reduced training time. Moreover, we have extensively assessed the design’s robustness, and the results suggest that it maintains stability even when exposed to suboptimal knowledge, in terms of incompleteness and noise. Our findings hold profound implications for an array of domains, including AI research, cognitive science, design science, and technical IS and practice.

## Implications for Cognitively Plausible AI Research

This study is a pioneering endeavor in bridging human learning theories with the emerging field of cognitively plausible AI research. Cognitive plausibility has drawn increasing attention in AI development, in which AI models or systems are designed to mimic or approximate human cognitive processes and behaviors [29, 83]. The goal is to create AI systems that can reason, learn, and make decisions in ways that are more similar to humans [54]. Cognitive science, which delves into the intricacies of human cognition, has profoundly inspired AI advancements [26]. In alignment with this ethos, we have harnessed the DSR methodology to introduce a novel design framework. This learning framework seamlessly incorporates elements of human learning, drawing upon the underpinnings of schema theory. The demonstrable enhancements in learning outcomes underscore the profound influence of cognitive science and its theories on the landscape of AI development. Hence, this study not only sheds light on the endeavor of crafting AI that approaches human-level intelligence but also underscores the importance of integrating research ideas from diverse disciplines, such as AI, machine learning, cognitive science, information systems, and design science.

Moreover, this study constitutes a substantial contribution to the emerging development of knowledge-aware models. Extant NLP models have predominantly thrived on the foundation of pre-trained LLMs, exemplified by BERT and GPT-3, yielding remarkable outcomes. However, these LLMs encapsulate knowledge implicitly, entailing knowledge encoding solely through model parameters. As a result, they fall short of being cognitively plausible and interpretable. In stark contrast, our design employs a knowledge-aware framework inspired by cognitive theories, deftly modeling explicit knowledge that can be articulated and elucidated. Thus, the treatment of knowledge within our framework aligns with cognitive plausibility and explicability. As a result, the insights gleaned from our study bear the potential to inform the trajectory of future development efforts directed toward cognitively plausible knowledge-aware models.

## Implications for Cognitive Science

This study extends its impact to the domain of cognitive science. We have empirically demonstrated that contextual knowledge, when required, effectively governs the activation of contextually relevant knowledge to facilitate learning. This finding not only underscores the pivotal role of contextual knowledge in knowledge activation but also aligns with established principles in cognitive science. Furthermore, our computational evidence offers valuable insights that serve to elucidate certain inconclusive aspects of cognitive science research. For instance, Figure 6 presents four distinct perspectives elucidating the interplay between conceptual and procedural knowledge. In this study, we have specifically adopted and tested the first perspective (Figure 6a), positing that conceptual knowledge precedes procedural knowledge [88]. However, the literature presents alternative viewpoints, as depicted in Figure 6b-d [84].

![](/api/attachments/WADKTHC2/fulltext/images/ed9abce437890efab370917c85500c4fba7bdeecb8347fab9687fa4f1b0d34a2.jpg)  
Figure 6. Four diferent views of the relationship between conceptual and procedural knowledge.

Our research serves to clarify the dynamic between conceptual and procedural knowledge, highlighting their interdependence rather than independence. It sheds light on the existence of synergy effects between these two knowledge types. Furthermore, our results emphasize that an exclusive focus on procedural knowledge often leads to marginal improvements and, in some cases, compromised outcomes, while the inclusion of conceptual knowledge consistently yields benefits. This suggests that conceptual knowledge likely serves as the foundational bedrock upon which procedural knowledge is built, as exemplified in Figure 6a. Consequently, our approach introduces an innovative avenue, harnessing computational models to explore and substantiate cognitive learning theories. It is worth noting that we did not observe evidence supporting the reverse direction within our study setting. Future research endeavors may contemplate controlled experiments to investigate the bidirectional relationship between these two knowledge types.

## Implications for Design Science and Technical IS Research

Recognizing its tremendous opportunity, this study represents how IS scholars make timely and impactful contributions to AI and deep learning research, answering the call from Samtani et al. [81], who proposed a systematic framework to guide IS scholars to advance the scale, scope, and impact of deep learning research. Specifically, aligning with the learning-level novelty contribution proposed by Samtani et al. [81], we strived to leverage cognitive learning theories as a guiding framework for the development of a cognitively plausible knowledge-aware AI learning framework. Yet, a significant challenge lies in translating abstract cognitive science theories into tangible learning models. To tackle this challenge, we introduced several innovative design concepts. In particular, it is well-established that contextual knowledge plays a pivotal role in governing the activation of relevant knowledge in human learning [4]. To replicate this intricate process, we introduced a novel contextual knowledge graph. This unique knowledge structure operates by comparing the context of a given learning task to the broader, general context. We harnessed these contextual knowledge graphs to craft a knowledge activation mechanism that mirrors the way humans activate knowledge during the learning process. This study is a pioneering endeavor to model a cognitively plausible knowledge activation mechanism, drawing inspiration from cognitive learning theories. Note that the efficient retrieval of contextually relevant knowledge from noisy knowledge resources remains an open research question in its own right. This study reflects our concerted efforts to address this challenge from the design science and technical IS perspective.

## Implications for Practice

Our emphasis on text analytics stems from its increasing significance in both academic research and practical business applications. With a substantial portion of available data existing in textual formats, the relevance of text analytics cannot be overstated. Our framework, in practical terms, yields remarkable accuracy even when trained on significantly fewer instances. This capability is especially valuable when dealing with problems constrained by limited available data. As a result, practitioners and business decision-makers stand to gain substantially from enhanced text analytics models, even when data resources are constrained. Importantly, our learning framework’s versatility extends beyond text classification and NLI. Unlike existing fewshot or zero-shot models that often exhibit limited generalizability, our framework is generic in nature and could transcend the boundaries of text analytics tasks. Given that deep learning has received tremendous attention from the IS community to solve practical business problems spanning various domains [42, 101, 102], our cognitively plausible knowledge-aware learning framework holds promise for enhancing learning performance across various applications.

Furthermore, the knowledge-aware models are gaining increasing attention not only within the AI community but also across diverse business domains [40, 55, 66, 74, 91]. For example, in the medical field, Mohamed et al. [66] devised a drug-target interaction prediction model, framing it as a link prediction problem within biomedical knowledge graphs encompassing drugs and their potential targets. In the retailing industry, Revilla et al. [78] investigated human-AI collaboration models in predicting demand forecasts. Their results revealed that the richness of contextual knowledge associated with human learning (e.g., prior knowledge and industry-specific experience) ensures more accurate predictions. In crowdsourcing, Jin et al. [40] illuminated the impact of knowledge sharing on the performance of crowdsourcing participants. In the realm of innovation, Trantopoulos et al. [91] delved into the knowledge-based perspective of firms, exploring external knowledge search and absorption, and their influence on innovation performance. Given the increasing popularity of knowledge-aware applications in the business landscape, we encourage future researchers to further expand upon this cognitive theory-guided cognitively plausible knowledge-aware framework to enhance the performance of existing knowledge-powered business applications.

## Limitations

Despite the promising results demonstrated by our proposed framework, this study does have its limitations, which we acknowledge and address in the following sections, along with potential solutions.

## Quality of External Knowledge Bases

Most knowledge-aware models largely depend on the quality of the external knowledge base used to provide knowledge. We employed ConceptNet, one of the most comprehensive knowledge bases. While we conducted extensive evaluations in our main experiments and robustness checks, it’s important to recognize that the quality of the external knowledge base can inevitably influence results. Future research could explore strategies to enhance the quality of knowledge bases, thereby further improving performance.

## Dynamic Nature of Knowledge

Much of the existing research on knowledge-aware models has centered around static knowledge, where facts remain constant over time. Although our design incorporates a dynamic element through the knowledge activation process guided by constructed contextual knowledge, it is not entirely dynamic. This is because the external knowledge base we utilized, ConceptNet, remains static. Temporal information holds significance, as structured knowledge or schemas continually evolve, refine, and undergo corrections over time [38]. Future research might consider implementing a more dynamic knowledge base to emulate the ongoing refinement of knowledge structures (schemas) akin to those stored in human long-term memory.

## Impact of Diferent Types of Knowledge in Diferent Domains

Our study assesses the importance of various types of knowledge across different domains. While our framework exhibits robust performance, we focused primarily on one specific domain (i.e., the medical domain) in addition to the general domain. Future research endeavors could encompass testing in other specific domains. Such exploration could yield deeper insights into how different knowledge types influence learning performance across diverse domains.

## Conclusions

Despite considerable recent advancements, current AI still cannot match human learning in terms of both effectiveness and efficiency. One crucial distinction lies in the abundance of prior knowledge possessed by humans, whereas AI often lacks the foundational commonsense knowledge necessary for learning tasks. While the importance of knowledge is recognized in both human and AI learning, existing knowledge-aware models often diverge from the way humans interact with knowledge. Drawing on schema theory, we utilize the design science research methodology to introduce an innovative knowledge-aware learning framework aimed at leveraging the knowledge-based processes inherent in human learning. In contrast to prevailing pretrained LLMs and knowledge-aware approaches that approach knowledge quite differently from humans, our framework is theoretically grounded and closely mirrors human processes of knowledge acquisition, representation, activation, and utilization. Comprehensive evaluations within the realm of text analytics tasks illustrate that our approach achieves comparable performance to state-of-the-art LLMs while also improving model generalizability and learning efficiency. This research carries important implications across various domains, encompassing AI research, cognitive science, design science, and technical information systems and practice. Particularly, it has significantly advanced the integration of cognitive science with the development of cognitively plausible AI and research on human-AI collaboration.

## Notes

i We are using the term “learning,” which is an encompassing process that includes both knowledge and skills acquisition and applications, is a broader term and contains problemsolving. While problem-solving is to use prior acquired knowledge and skills to address a particular challenge or obstacle. This application of existing knowledge and skills to solve a specific problem is a subset of the overall learning process. In essence, problem-solving is a manifestation of learning in action.

## Disclosure statement

The authors have no conflicts of interest to disclose.

## Notes on contributors

Long Xia (lxia@elon.edu) is an Assistant Professor of Management Information Systems at the Love School of Business at Elon University. He received his PhD in Business Analytics from Virginia Tech. Dr. Xia’s research interests include deep learning, data science, design science, tourism and hospitality management, sharing economy, health IT, and social media analytics. His work has been published in such journals as Tourism Management, Decision Support Systems, Journal of Electronic Commerce Research, and Information Discovery and Delivery.

Wenqi Shen (shenw@vt.edu) is an Assistant Professor at the Pamplin College of Business at Virginia Tech. She received her PhD in Management Information Systems from Purdue University. Dr. Shen’s research interests include online virtual communities, social media and social dynamics, usergenerated content, the economics of information technologies, and firm information security. Her research has been published in such journals as MIS Quarterly, Management Science, Information Systems Journal, Journal of the Association for Information Systems, and Expert Systems with Applications, among others.

Weiguo Fan (weiguo-fan@uiowa.edu) is a Henry B. Tippie Chair Professor in Business Analytics at the Tippie College of Business, University of Iowa. He received his PhD from the Ross School of Business, University of Michigan. His research interests focus on the design and development of novel information technologies—information retrieval, data mining, text analytics, social media analytics, and business intelligence techniques—to support better business information management and decision-making. Dr. Fan has published more than 280 refereed journal and conference papers. His research has appeared in many premier journals such as Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Productions and Operations Management, IEEE Transactions on Knowledge and Data Engineering, and others.

G. Alan Wang (alanwang@vt.edu; corresponding author) is the Andersen Professor of Business Information Technology at the Pamplin College of Business at Virginia Tech. He received a PhD in Management Information Systems from the University of Arizona, Dr. Wang’s research interests include text mining, data mining, web and social media analytics, service computing, and quality engineering. He has published in Information Systems Research, Journal of Management Information Systems, MIS Quarterly Productions and Operations Management, Journal of Business Ethics, and Communications of the ACM, among others.

## References

1. Abbasi, A.; and Chen, H. CyberGate: A design framework and system for text analysis of computer-mediated communication. MIS Quarterly, 32, 4 (2008), 811–837.

2. Aizawa, A. An information-theoretic perspective of tf–idf measures. Information Processing & Management, 39, 1 (2003), 45–65.

3. Alba, J.W.; and Hasher, L. Is memory schematic? Psychological Bulletin, 93, 2 (1983), 203–231.

4. Alexander, P.A.; and Judy, J.E. The interaction of domain-specific and strategic knowledge in academic performance. Review of Educational Research, 58, 4 (1988), 375–404.

5. An, S. Schema Theory in Reading. Theory & Practice in Language Studies, 3, 1 (2013), 130–134.

6. Anderson, R.C. Schema-directed processes in language comprehension. In A.M. Lesgold, J. W. Pellegrino, S.D. Fokkema, and R. Glaser (eds.), Cognitive Psychology and Instruction. New York: Springer, 1978, pp. 67–82.

7. Anderson, R.C. The notion of schemata and the educational enterprise: General discussion of the conference. In R.C. Anderson, R.J. Spiro, and W.E. Montague (eds.), Schooling and the Acquisition of Knowledge. London: Routledge, 2017, pp. 415–431.

8. Anderson, R.C.; and Pearson, P.D. A schema-theoretic view of basic processes in reading comprehension. Handbook of Reading Research, 1 (1984), 255–291.

9. Anderson, R.C.; Spiro, R.J.; and Anderson, M.C. Schemata as scaffolding for the representation of information in connected discourse. American Educational Research Journal, 15, 3 (1978), 433–440.

10. Apeldoorn, D.; and Kern-Isberner, G. When should learning agents switch to explicit knowledge? In C. Benzmüller, G. Sutcliffe, and R. Rojas (eds.), Global Conference on Artificial Intelligence (GCAI), Berlin, 2016, pp. 174–186.

11. Arbib, M.A. Schema theory. The Encyclopedia of Artificial Intelligence, 2 (1992), 1427–1443.

12. Batmanghelich, K.; Saeedi, A.; Narasimhan, K.; and Gershman, S. Nonparametric spherical topic modeling with word embeddings. In K. Erk, and N.A. Smith (eds.), Proceedings of the 54<sup>th</sup> Annual Meeting of the Association for Computational Linguistics. Berlin: Association of Computational Linguistics, 2016, pp. 537–542.

13. Baxter, G.P.; Elder, A.D.; and Glaser, R. Knowledge-based cognition and performance assessment in the science classroom. Educational Psychologist, 31, 2 (1996), 133–140.

14. Bordes, A.; Usunier, N.; Garcia-Duran, A.; Weston, J.; and Yakhnenko, O. Translating embeddings for modeling multi-relational data. In C.J. Burges, L. Bottou, M. Welling, Z. Ghahramani, and K.Q. Weinberger (eds.), Advances in Neural Information Processing Systems. Lake Tahoe. 2013, pp. 2787–2795.

15. Boyd-Graber, J.; Mimno, D.; and Newman, D. Care and feeding of topic models: Problems, diagnostics, and improvements. In E.M. Airoldi, D. Blei, E.A. Erosheva, and S.E. Fienberg (eds.), Handbook of Mixed Membership Models and Their Applications, New York: Chapman and Hall/CRC, 2014, pp. 3–41.

16. Brown, T.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J.D.; Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; and Askell, A. Language models are few-shot learners. In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin (eds.), Advances in Neural Information Processing Systems. Virtual, 2020, pp. 1877–1901.

17. Carrell, P.L.; and Eisterhold, J.C. Schema theory and ESL reading pedagogy. TESOL Quarterly, 17, 4 (1983), 553–573.

18. Chen, Q.; Zhu, X.; Ling, Z.-H.; Inkpen, D.; and Wei, S. Neural natural language inference models enhanced with external knowledge. arXiv preprint arXiv:1711.04289 (2017).

19. Chi, M.T. Knowledge development and memory performance. In M.P. Friedman, J.P. Das, and N. O’Connor (eds.), Intelligence and Learning. Springer, 1981, pp. 221–229.

20. De Jong, T.; and Ferguson-Hessler, M.G. Types and qualities of knowledge. Educational Psychologist, 31, 2 (1996), 105–113.

21. Dellermann, D.; Ebel, P.; Söllner, M.; and Leimeister, J.M. Hybrid intelligence. Business & Information Systems Engineering, 61, 5 (2019), 637–643.

22. Devlin, J.; Chang, M.-W.; Lee, K.; and Toutanova, K. Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805 (2018).

23. Dienes, Z.; and Perner, J. A theory of implicit and explicit knowledge. Behavioral and Brain Sciences, 22, 5 (1999), 735–808.

24. Dong, Q.; Liu, Y.; Cheng, S.; Wang, S.; Cheng, Z.; Niu, S.; and Yin, D. Incorporating explicit knowledge in pre-trained language models for passage re-ranking. arXiv preprint arXiv:2204.11673 (2022).

25. Dorsey, D.W.; Campbell, G.E.; Foster, L.L.; and Miles, D.E. Assessing knowledge structures: Relations with experience and posttraining performance. Human Performance, 12, 1 (1999), 31–57.

26. Faust, O.; Hagiwara, Y.; Hong, T.J.; Lih, O.S.; and Acharya, U.R. Deep learning for healthcare applications based on physiological signals: A review. Computer Methods and Programs in Biomedicine, 161 (2018), 1–13.

27. Firestone, C. Performance vs. competence in human–machine comparisons. Proceedings of the National Academy of Sciences, 117, 43 (2020), 26562–26571.

28. Floridi, L. AI as agency without intelligence: On ChatGPT, large language models, and other generative models. Philosophy & Technology, 36, 1 (2023), 15–21.

29. Forbus, K.D.; and Hinrichs, T.R. Companion cognitive systems: A step toward Human-Level AI. AI Magazine, 27, 2 (2006), 83–83.

30. Gilakjani, A.P.; and Ahmadi, S.M. The relationship between L2 reading comprehension and schema theory: A matter of text familiarity. International Journal of Information and Education Technology, 1, 2 (2011), 142–149.

31. Gregor, S.; and Hevner, A.R. Positioning and presenting design science research for maximum impact. MIS Quarterly, 37, 2 (2013), 337–355.

32. Halkias, G. Mental representation of brands: A schema-based approach to consumers’ organization of market knowledge. Journal of Product & Brand Management, 24, 5 (2015), 438–448.

33. He, P.; Liu, X.; Gao, J.; and Chen, W. Deberta: Decoding-enhanced bert with disentangled attention. arXiv preprintarXiv:2006.03654 (2020).

34. Hern, A. ‘What should the limits be?’ The father of ChatGPT on whether AI will save humanity – or destroy it. 2023. https://www.theguardian.com/technology/2023/jun/07/whatshould-the-limits-be-the-father-of-chatgpt-on-whether-ai-will-save-humanity-or-destroy-it (accessed August 30, 2023).

35. Hevner, A.; and Chatterjee, S. Design science research in information systems. In A. Hevner and S. Chatterjee (eds.), Design Research in Information Systems. Springer, 2010, pp. 9–22.

36. Hevner, A.R.; March, S.T.; Park, J.; and Ram, S. Design science in information systems research. MIS Quarterly, 28, 1 (2004), 75–105.

37. Hu, L.; Liu, Z.; Zhao, Z.; Hou, L.; Nie, L.; and Li, J. A survey of knowledge enhanced pre-trained language models. IEEE Transactions on Knowledge and Data Engineering, (2023), 1–19.

38. Ji, S.; Pan, S.; Cambria, E.; Marttinen, P.; and Philip, S.Y. A survey on knowledge graphs: Representation, acquisition, and applications. IEEE Transactions on Neural Networks and Learning Systems, 33, 2 (2021), 494–514.

39. Ji, S.; Pan, S.; Cambria, E.; Marttinen, P.; and Philip, S.Y. A survey on knowledge graphs: Representation, acquisition, and applications. IEEE Transactions on Neural Networks and Learning Systems, (2021), 494–514.

40. Jin, Y.; Lee, H.C.B.; Ba, S.; and Stallaert, J. Winning by learning? Effect of knowledge sharing in crowdsourcing contests. Information Systems Research, 32, 3 (2021), 836–859.

41. Johnson, M.; Albizri, A.; Harfouche, A.; and Fosso-Wamba, S. Integrating human knowledge into artificial intelligence for complex and ill-structured problems: Informed artificial intelligence. International Journal of Information Management, 64 (2022), 102479.

42. Johnson, M.; Murthy, D.; Robertson, B.W.; Smith, W.R.; and Stephens, K.K. Moving Emergency Response Forward: Leveraging Machine-Learning Classification of Disaster-Related Images Posted on Social Media. Journal of Management Information Systems, 40, 1 (2023), 163–182.

43. Jonassen, D.H.; Yacci, M., and Beissner, K. Structural Knowledge: Techniques for Representing, Conveying, and Acquiring Structural Knowledge. New York: Routledge, 2013.

44. Kang, B.; Liu, Z.; Wang, X.; Yu, F.; Feng, J.; and Darrell, T. Few-shot object detection via feature reweighting. Proceedings of the IEEE/CVF International Conference on Computer Vision. Seoul: IEEE, 2019, 8420–8429.

45. Kim, J.U.; and Kishore, R. Do we fully understand information systems failure? An exploratory study of the cognitive schema of IS professionals. Information Systems Frontiers, 21, 6 (2019), 1385–1419.

46. Kipf, T.N.; and Welling, M. Semi-supervised classification with graph convolutional networks. arXiv preprint arXiv:1609.02907 (2016).

47. Knight, W. OpenAI’s CEO Says the Age of Giant AI Models Is Already Over. 2023. https:// www.wired.com/story/openai-ceo-sam-altman-the-age-of-giant-ai-models-is-already-over/ (accessed August 30, 2023).

48. Lake, B.M.; Ullman, T.D.; Tenenbaum, J.B.; and Gershman, S.J. Building machines that learn and think like people. Behavioral and Brain Sciences, 40 (2017), 1–72.

49. Lau, J.H.; Baldwin, T.; and Newman, D. On collocations and topic models. ACM Transactions on Speech and Language Processing (TSLP), 10, 3 (2013), 1–14.

50. LeCun, Y.; Bengio, Y.; and Hinton, G. Deep learning. Nature, 521, 7553 (2015), 436–444.

51. Li, J.; Larsen, K.; and Abbasi, A. TheoryOn: A design framework and system for unlocking behavioral knowledge through ontology learning. MIS Quarterly, 44, 4 (2020), 1733–1772.

52. Li, X.-H.; Cao, C.C.; Shi, Y.; Bai, W.; Gao, H.; Qiu, L.; Wang, C.; Gao, Y.; Zhang, S.; and Xue, X. A survey of data-driven and knowledge-aware explainable ai. IEEE Transactions on Knowledge and Data Engineering, 34, 1 (2020), 29–49.

53. Li, Z.; Liu, H.; Zhang, Z.; Liu, T.; and Xiong, N.N. Learning knowledge graph embedding with heterogeneous relation attention networks. IEEE Transactions on Neural Networks and Learning Systems (2021), 3961–3973.

54. Lieto, A. Cognitive Design for Artificial Minds. London: Routledge, 2021.

55. Lim, S.Y.; Jarvenpaa, S.L.; and Lanham, H.J. Barriers to interorganizational knowledge transfer in post-hospital care transitions: Review and directions for information systems research. Journal of Management Information Systems, 32, 3 (2015), 48–74.

56. Lin, B.Y.; Chen, X.; Chen, J.; and Ren, X. Kagnet: Knowledge-aware graph networks for commonsense reasoning. arXiv preprint arXiv:1909.02151 (2019).

57. Lin, J.; Zhao, Y.; Huang, W.; Liu, C.; and Pu, H. Domain knowledge graph-based research progress of knowledge representation. Neural Computing and Applications, 33 (2021), 681–690.

58. Liu, Y. An empirical study of schema theory and its role in reading comprehension. Journal of Language Teaching and Research, 6, 6 (2015), 1349–1356.

59. Lin, Y.; Meng, Y.; Sun, X.; Han, Q.; Kuang, K.; Li, J.; and Wu, F. Bertgcn: Transductive text classification by combining gcn and bert. arXiv preprint arXiv:2105.05727 (2021).

60. Liu, Y.; Ott, M.; Goyal, N.; Du, J.; Joshi, M.; Chen, D.; Levy, O.; Lewis, M.; Zettlemoyer, L.; and Stoyanov, V. Roberta: A robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692 (2019).

61. Ma, T.; Huang, L.; Lu, Q.; and Hu, S. Kr-gcn: Knowledge-aware reasoning with graph convolution network for explainable recommendation. ACM Transactions on Information Systems, 41, 1 (2023), 1–27.

62. Marino, K.; Chen, X.; Parikh, D.; Gupta, A.; and Rohrbach, M. Krisp: Integrating implicit and symbolic knowledge for open-domain knowledge-based vqa. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. Nashville, 2021, 14111–14121.

63. Marshall, S.P. Assessing schema knowledge. In N. Frederiksen, R.J. Mislevy, I.I. Bejar (eds.), Test Theory for a New Generation of Tests. New York, London: Routledge, 2012, pp. 155–180.

64. Meyer, D. OpenAI’s Sam Altman says giant A.I. models are over—but going small won’t appease regulators. 2023. https://finance.yahoo.com/news/openai-sam-altman-says-giant -164924270.html (accessed August 30, 2023).

65. Min, B.; Ross, H.; Sulem, E.; Veyseh, A.P.B.; Nguyen, T.H.; Sainz, O.; Agirre, E.; Heintz, I.; and Roth, D. Recent advances in natural language processing via large pre-trained language models: A survey. ACM Computing Surveys, 56, 2 (2021), 1–40.

66. Mohamed, S.K.; Nováček, V.; and Nounu, A. Discovering protein drug targets using knowledge graph embeddings. Bioinformatics, 36, 2 (2020), 603–610.

67. Nassaji, H. Schema theory and knowledge‐based processes in second language reading comprehension: A need for alternative perspectives. Language Learning, 52, 2 (2002), 439–481.

68. Nickel, M.; Murphy, K.; Tresp, V.; and Gabrilovich, E. A review of relational machine learning for knowledge graphs. Proceedings of the IEEE, 104, 1 (2015), 11–33.

69. Nishida, H. A cognitive approach to intercultural communication based on schema theory. International Journal of Intercultural Relations, 23, 5 (1999), 753–777.

70. Nissen, M.E. Dynamic knowledge patterns to inform design: A field study of knowledge stocks and flows in an extreme organization. Journal of Management Information Systems, 22, 3 (2005), 225–263.

71. Ozmen Garibay, O.; Winslow, B.; Andolina, S.; Antona, M.; Bodenschatz, A.; Coursaris, C.; Falco, G.; Fiore, S.M.; Garibay, I.; and Grieman, K. Six human-centered artificial intelligence grand challenges. International Journal of Human–Computer Interaction, 39, 3 (2023), 391–437.

72. Pan, S.; Luo, L.; Wang, Y.; Chen, C.; Wang, J.; and Wu, X. Unifying large language models and knowledge graphs: A roadmap. IEEE Transactions on Knowledge and Data Engineering, 99 (2024), 1–20.

73. Pan, S.J.; and Yang, Q. A survey on transfer learning. IEEE Transactions on Knowledge and Data Engineering, 22, 10 (2009), 1345–1359.

74. Peng, G.; Dey, D.; and Lahiri, A. Healthcare IT adoption: An analysis of knowledge transfer in socioeconomic networks. Journal of Management Information Systems, 31, 3 (2014), 7–34.

75. Pennington, J.; Socher, R.; and Manning, C.D. Glove: Global vectors for word representation. In A. Moschitti, B. Pang, and W. Daelemans.(eds.), Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP). Doha: Association of Computational Linguistics, 2014, pp. 1532–1543.

76. Perrigo, B. The A to Z of Artificial Intelligence. 2023. https://time.com/6271657/a-to-z-ofartificial-intelligence/ (accessed August 30, 2023).

77. Pilault, J.; Elhattami, A.; and Pal, C. Conditionally adaptive multi-task learning: Improving transfer learning in nlp using fewer parameters & less data. arXiv preprint arXiv:2009.09139 (2020).

78. Revilla, E.; Saenz, M.J.; Seifert, M.; and Ma, Y. Human–artificial intelligence collaboration in prediction: A field experiment in the retail industry. Journal of Management Information Systems, 40, 4 (2023), 1071–1098.

79. Rumelhart, D.E.; and Ortony, A. The representation of knowledge in memory. Schooling and the Acquisition of Knowledge, (1977), 99–135.

80. Sadoski, M.; Paivio, A.; and Goetz, E.T. Commentary: A critique of schema theory in reading and a dual coding alternative. Reading Research Quarterly (1991), 463–484.

81. Samtani, S.; Zhu, H.; Padmanabhan, B.; Chai, Y.; Chen, H.; and Nunamaker Jr, J.F. Deep learning for information systems research. Journal of Management Information Systems, 40, 1 (2023), 271–301.

82. Sap, M.; Le Bras, R.; Allaway, E.; Bhagavatula, C.; Lourie, N.; Rashkin, H.; Roof, B.; Smith, N.A.; and Choi, Y. Atomic: An atlas of machine commonsense for if-then reasoning. Proceedings of the AAAI Conference on Artificial Intelligence. San Francisco: AAAI Press, 2019, pp. 3027–3035.

83. Saxe, A.; Nelli, S.; and Summerfield, C. If deep learning is the answer, what is the question? Nature Reviews Neuroscience, 22, 1 (2021), 55–67.

84. Schneider, M.; Rittle-Johnson, B.; and Star, J.R. Relations among conceptual knowledge, procedural knowledge, and procedural flexibility in two samples differing in prior knowledge. Developmental Psychology, 47, 6 (2011), 1525–1538.

85. Shah, S.; Mishra, A.; Yadati, N.; and Talukdar, P.P. Kvqa: Knowledge-aware visual question answering. Proceedings of the AAAI Conference on Artificial Intelligence. Washington DC: AAAI Press, 2019, pp. 8876–8884.

86. Singhal, K.; Azizi, S.; Tu, T.; Mahdavi, S.S.; Wei, J.; Chung, H.W.; Scales, N.; Tanwani, A.; Cole-Lewis, H.; and Pfohl, S. Large language models encode clinical knowledge. Nature, 620, 7972 (2023), 172–180.

87. Speer, R.; Chin, J.; and Havasi, C. Conceptnet 5.5: An open multilingual graph of general knowledge. Thirty-first AAAI Conference on Artificial Intelligence. San Francisco: AAAI Press, 2017, pp. 4444–4451.

88. Star, J.R.; and Seifert, C. The development of flexibility in equation solving. Contemporary Educational Psychology, 31, 3 (2006), 280–300.

89. Sun, R.; Zhang, X.; Slusarz, P.; and Mathews, R. The interaction of implicit learning, explicit hypothesis testing learning and implicit-to-explicit knowledge extraction. Neural Networks, 20, 1 (2007), 34–47.

90. Talmor, A.; Tafjord, O.; Clark, P.; Goldberg, Y.; and Berant, J. Leap-of-thought: Teaching pre-trained models to systematically reason over implicit knowledge. Advances in Neural Information Processing Systems, 33 (2020), 20227–20237.

91. Trantopoulos, K.; von Krogh, G.; Wallin, M.W.; and Woerter, M. External knowledge and information technology: Implications for process innovation performance. MIS Quarterly, 41, 1 (2017), 287–300.

92. Turner, R. Adaptive Reasoning for Real-World Problems: A Schema-Based Approach. New York: Psychology Press, 2013.

93. Walls, J.G.; Widmeyer, G.R.; and El Sawy, O.A. Building an information system design theory for vigilant EIS. Information Systems Research, 3, 1 (1992), 36–59.

94. Wang, H.; Zhang, F.; Xie, X.; and Guo, M. DKN: Deep knowledge-aware network for news recommendation. In P.A. Champin, F. Gandon, and L. Médini (eds.), Proceedings of the 2018 World Wide Web Conference. Geneva, 2018, pp. 1835–1844.

95. Wang, J.; Wang, Z.; Zhang, D.; and Yan, J. Combining knowledge with deep convolutional neural networks for short text classification. In C. Sierra (ed.), International Joint Conference on Artificial Intelligence. Melbourne: AAAI Press, 2017, pp. 2915–2921.

96. Wang, Q.; Mao, Z.; Wang, B.; and Guo, L. Knowledge graph embedding: A survey of approaches and applications. IEEE Transactions on Knowledge and Data Engineering, 29, 12 (2017), 2724–2743.

97. Wang, S.; Fang, H.; Khabsa, M.; Mao, H.; and Ma, H. Entailment as few-shot learner. arXiv preprint arXiv:2104.14690 (2021).

98. Wang, X.; Gao, T.; Zhu, Z.; Zhang, Z.; Liu, Z.; Li, J.; and Tang, J. KEPLER: A unified model for knowledge embedding and pre-trained language representation. Transactions of the Association for Computational Linguistics, 9 (2021), 176–194.

99. Weiss, K.; Khoshgoftaar, T.M.; and Wang, D. A survey of transfer learning. Journal of Big Data, 3, 1 (2016), 1–40.

100. Wu, H.; Huang, C.; and Deng, S. Improving aspect-based sentiment analysis with Knowledge-aware Dependency Graph Network. Information Fusion, 92 (2023), 289–299.

101. Xie, J.; Chai, Y.; and Liu, X. Unbox the black-box: Predict and interpret YouTube viewership using deep learning. Journal of Management Information Systems, 40, 2 (2023), 541–579.

102. Xu, D.; Hu, P.J.-H.; and Fang, X. Deep learning-based imputation method to enhance crowdsourced data on online business directory platforms for improved services. Journal of Management Information Systems, 40, 2 (2023), 624–654.

103. Yan, R.; Sun, L.; Wang, F.; and Zhang, X. A general method for transferring explicit knowledge into language model pretraining. Security and Communication Networks, 2021 (2021), 1–8.

104. Yang, Z.; Dai, Z.; Yang, Y.; Carbonell, J.; Salakhutdinov, R.R.; and Le, Q.V. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d’Alché-Buc, E. Fox, and R.; Garnett (eds.), Xlnet: Generalized autoregressive pretraining for language understanding. Advances in Neural Information Processing Systems. Vancouver, 32 (2019).

105. Yao, L.; Mao, C.; and Luo, Y. Graph convolutional networks for text classification. Proceedings of the AAAI Conference on Artificial Intelligence. Honolulu: AAAI Press, 2019, pp. 7370–7377.

106. Yu, Y.; Huang, K.; Zhang, C.; Glass, L.M.; Sun, J.; and Xiao, C. SumGNN: Multi-typed drug interaction prediction via efficient knowledge graph summarization. Bioinformatics, 37, 18 (2021), 2988–2995.

107. Zhang, N.; Deng, S.; Sun, Z.; Wang, G.; Chen, X.; Zhang, W.; and Chen, H. Long-tail relation extraction via knowledge graph embeddings and graph convolution networks. arXiv preprint arXiv:1903.01306 (2019).

108. Zhang, Y.; Jiang, M.; and Zhao, Q. Explicit Knowledge Incorporation for Visual Reasoning. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. New Orleans, 2021, pp. 1356–1365.

109. Zhang, Z.; Han, X.; Liu, Z.; Jiang, X.; Sun, M.; and Liu, Q. ERNIE: Enhanced language representation with informative entities. arXiv preprint arXiv:1905.07129 (2019).
