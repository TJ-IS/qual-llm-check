---
otero_id: 10296
otero_key: "WDWA24GR"
title: "A comprehensive framework of information system design to provide organizational creativity support"
authors: "Celina M. Olszak; Tomasz Bartuś; Paweł Lorek"
year: "2018"
journal: "Information & Management"
doi: "10.1016/j.im.2017.04.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: A Comprehensive Framework of Information System Design to Provide Organizational Creativity Support

Author: Celina M. Olszak Tomasz Bartus Paweł Lorek´

![](/api/attachments/WDWA24GR/fulltext/images/ff1510dc4022034a044aa817efee4109236bf0d0109feb77b63dc1b69253ec93.jpg)

PII: S0378-7206(17)30330-0

DOI: http://dx.doi.org/doi:10.1016/j.im.2017.04.004

Reference: INFMAN 2997

To appear in: INFMAN

Received date: 5-3-2015

Revised date: 3-4-2017

Accepted date: 15-4-2017

Please cite this article as: C.M. Olszak, T. Bartus, A Comprehensive Framework of´ Information System Design to Provide Organizational Creativity Support, Information and Management (2017), http://dx.doi.org/10.1016/j.im.2017.04.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

Celina M. Olszak (corresponding author) University of Economics in Katowice e-mail: celina.olszak@ue.katowice.pl

Tomasz Bartu<sup>ś</sup> University of Economics in Katowice, e-mail: tomasz.bartus@ue.katowice.pl

Paweł Lorek University of Economics in Katowice e-mail:pawel.lorek.@ue.katowice.pl

# A Comprehensive Framework of Information System Design to Provide Organizational Creativity Support

Abstract: This research is motivated by two considerations: (1) organizational creativity is a component that enhances the ability of organizations to retain their competitive advantage and (2) too little research has been conducted worldwide that focuses on the design of information systems to provide organizational creativity support. This research proposes a comprehensive and conceptual framework for the design of organizational creativity support systems. To address the objective of this study, two theories, the resource-based view and a multiagent approach, are used to build the model proposed. The customer opinions from websites concerning a consumer electronics product are used to validate such a system. The theoretical contributions, practical implications, and future directions of the study are presented and discussed.

Keywords: organizational creativity; design of organizational creativity support system; Resource-based View, intelligent agents

Highlights

• A design of information system to support organizational creativity is proposed.

RBV and a multiagent approach are used to achieve the research objective.

• An architecture of organizational creativity support system is proposed.

• Organizational creativity support system is built and tested.

• Four groups of intelligent agents are used in organizational creativity support system.

## 1. Introduction

Organizational creativity is considered one of the most actively developing research areas. It is asserted that it is a main vehicle of organizational development, the basis for staying on the market and innovative success [1,2,3,4]. Organizations face the need to constantly generate new and useful ideas that concern products, services, processes, managerial practices, and competitive strategies. They are required to have a strategic organization’s capability, meaning adapting to changing environmenta conditions through continuous acquisition of new information resources and the creation of new

#

configurations from them [5,6,7]. Effective support of acquiring, collecting, storing, and analyzing different information resources and discovering new knowledge and rapidly disseminating it are of crucial importance.

Several arguments can be found in the pertinent literature that IT enables organizations faster and easier access to information, improving creativity in business processes and better communication between employees and all stakeholders [8]. IT enables an organization to search and absorb new knowledge that is needed in organizational creativity and solving business problems. On the other hand, the practice shows that success from IT-based creativity support is still questionable. Organizations do not achieve the appropriate benefits from IT usage. Many organizations are not able to make IT an effective tool for creativity support. The reasons for this failure are not clear and still not well investigated. Therefore, the need for a more systematic and deliberate study of information system design to support organizational creativity is crucial.

Although there have been numerous studies on creativity over the past three decades, they have not addressed the essence of organizational creativity support systems (OCSSs) and their design. They have been mainly focused on creative problem solving, creative processes, and individual creativity support. The issue of the design of information systems for organizational creativity support is still insufficiently investigated. The research studies are fragmentary and scattered. There is a lack of a comprehensive framework of organizational creativity support and a lack of examples on how to design OCSSs.

The main task of this paper is to provide a theoretically and empirically grounded discussion on organizational creativity and the design of information systems to provide organizational creativity support. The study proposes a comprehensive, conceptual framework for the design of an OCSS. The idea of this study is to attempt to answer the following questions: (1) What is the essence of organizational creativity and its IT-based support? and (2) How to use the resource-based view (RBV) and a multiagent approach for the design of information systems for organizational creativity support? The search for answers to these questions is mainly conducted on the theoretical, methodological, and the empirical foundation. At the start, a critical review of the relevant literature is conducted to identify the organizational creativity issue and its computer support. Then, the theory of RBV and a multiagent approach are explored. The search for the appropriate literature employed different bibliographic databases, e.g., EBSCOhost, Emerald Management 75, ISI Web of Knowledge, ProQuest, and Scopus. Additionally, open access papers are explored. Finally, a comprehensive, conceptual framework for the design of information systems to support organizational creativity is proposed. The framework is grounded in RBV and a multiagent approach. RBV enables us to better know how to manage information resources and what should be done with them to support organizational creativity. In turn, a multiagent approach gives a sound basis to assist various human activities that are significant in the context of organizational creativity development. Finally, the idea of a prototype of a system based on different intelligent agents, such as searching agents, monitoring agents, capturing agents, and discovering and suggesting agents to design organizational creativity support, is described. The prototype, as an example of the proposed framework, was tested in a social media environment. Customer opinions from the consumer electronics sector were the center of the analysis. In the conclusion of this paper, theoretical contributions, practical implications, and future directions of the study are presented and discussed.

## 2. Related Works

## 2.1. Knowledge and Organizational Creativity

Creativity is closely related to knowledge. An organization’s success depends on its capability to create new knowledge that is then manifested in new, useful ideas and in innovations [1,2,3]. Knowledge is an organization’s most valuable resource because it embodies intangible assets, routines, and creative processes that are difficult to imitate. It is claimed that successful organizations are those that consistently create new knowledge, disseminate it widely throughout the organization, and rapidly include it in new products. According to Nonaka and Takeuchi [9], there are two forms of knowledge: explicit and tacit knowledge. Explicit knowledge is defined as knowledge that can be expressed formally. It is easily communicated and diffused through an organization. Explicit

#

knowledge may include trade journals, executive reports, speeches, project reports, etc. [10]. On the other hand, tacit knowledge consists of subject expertise, assumptions, and insights. This knowledge is critical in decision-making, creating a competitive advantage, and creativity and innovation. Organizations that want to survive on the market are required to have strategic capability for continuous acquisition of knowledge resources and the creation of new configurations [5,6,7]. This refers to discovering various patterns, generalizations, regularities, and rules in data resources [11,12]. Such data mining may be utilized to predict and to describe reality (e.g., customers’ preferences concerning new products, changes in product features).

Baron [13] advocated that creativity means the creation of something new, which is based on the exploration of different information resources (databases and knowledge bases). Creativity is compared to a knowledge system [14] used for solving different problems and increasing organizational effectiveness [15]. One of the most cited definitions of creativity says that the outcomes of creativity are ideas that are distinguished by novelty and usability [16,17]. Many authors highlight that these ideas are used to achieve some particular aims [18] and that they have a significant impact [19]. Mumford et al. [20] stated that creativity is crucial in the solving of semi-structured or unstructured problems.

Although the term “creativity” is rooted in psychology, it is used in different organizational contexts— in the context of business strategy, business processes, strategic management, competitive advantage, organizational development, leadership, and innovation. According to many scholars [21,22,23,24], “organizational creativity” means the capability to generate new and useful ideas that concern products, services, processes, managerial practices, and competitive strategies. Woodman [25] defined organizational creativity as the creation of a valuable, useful new product, service, idea, procedure, or process by individuals working together in a complex social system. New ideas must constitute an appropriate response to fill a gap in production, marketing, or the administrative processes of the organization [26]. Therefore, creativity could be seen as an important organizational capability [1], a possible source of organizational effectiveness and a source of competitive advantage. It is a collaborative psychological process that takes place in an organization and is affected by contextual and organizational factors [27]. According to Brennan and Dooley [28], creativity within an organizational context can be regarded as the sum of the following functions: the creative person, creative task, and the organizational context (culture). Sundgren and Styhre [29] noted that organizational creativity is something more than a collection of creative individuals. Thus, the mere presence of creative individuals in an organization does not guarantee organizational creativity because it is the result of the whole spectrum of organizational factors. Amabile et al. [30] pointed out that the extent to which people produce creative ideas depends not only on their individual characteristics but also on the work environment that they perceive around them. Styhre and Sundgren [29] argued that managers and leaders play a crucial role in supporting and enhancing organizational creativity. They must adopt unique styles based on agility, perceptiveness, and rapid decision-making. Rosa et al. [31] identified four management principles that can engender creativity and innovation in organizations: (1) to manage organizations so that their knowledge base is more diverse than what would occur naturally, (2) to encourage employees to embrace a collaborative and noncomplacent attitude toward work and the organization, (3) to make it possible for organization members to engage in the quick testing of ideas and solutions as they emerge, and (4) to reward employees and supervisors’ behaviors that support these principles and punish resistance to their implementation. On the contrary, some authors specified some barriers to organizational creativity. They include intolerance of differences, overly rational thinking, inappropriate incentives, and excessive bureaucracy [28].

Many authors point to a link between creativity and innovation. Baer [32] stated that creativity can be viewed as the first stage of an innovation process. Creativity is the starting point for any innovation. However, creativity is an individual and solitary process, and innovation is a more inclusive process involving many people. Brennan and Dooley [28] indicated that ability to stimulate innovation is highly dependent upon the stock of potential ideas and problem solving, which are products of an organization’s creativity processes. To promote innovation as an output of creativity, the organization must itself be creative and imbibe a culture of innovativeness [33]. From the innovation perspective,

#

knowledge provides the organization with the potential for novel action, and the process of constructing novel actions often entails finding new uses or new combinations of previously disparate ideas [26].

## 2.2. Creativity Support Systems

Shneiderman [34] stated that technologies that “enable people to be more creative more often” are referred to as creativity support systems (CSSs). Technically, the term CSS concerns a class of information systems encompassing diverse types of IS that share the enhancement of creativity [35]. CSS may be used to (1) enhance a user’s ability to perform creative tasks (the ability that the user possesses already), (2) support users in domain knowledge acquisition, to free up their creativity, and (3) give users new experiences concerning creative tasks, thus giving them new task-solving capabilities [36]. Shneiderman [34] argued that CSS should

• offer indices for work progress measurement, together with the possibility of generating alerts,

• contain libraries of images, thesauri, sketching interfaces, possibility of ideas mapping,

• support communication and collaboration, enable group work coordination,

• simplify knowledge coding in an electronic form.

Muller and Ulrich [37] and Klijn and Tomic [38] argued that CSS may be used for the following:

• information collecting – by simplification of searching, browsing, and visualization,

• defining linkages between information,

• creative processes – by loose associations, examination of solutions, composing of artifacts, and idea reviewing,

• disseminating the effects of creative cooperation.

Greene [39] stated that organizational creativity support software should be able to explore problem domains; teach and discover new problems; support collaboration; visualize domain interdependences; and simplify storing, classifying, and mining of notions. Woodman et al. [25] pointed out that IT tools should enable first of all information flow and communication in an organization. Lubart [40] and Ulrich and Mengiste [41] highlighted the importance of “what-if” analyses, data and processes visualization, and creative processes affect dissemination, visualization of ideas, human–computer dialogue in the problem solving process as well as advanced human–computer interaction, business plan support, and storing of users’ preferences. In turn, Dewett [42] claimed that three benefits appear to be particularly salient: the improved ability to link and enable employees, the improved ability to codify the organization’s knowledge base, and improved boundary spanning capabilities.

Davies et al. [43] claimed that CSSs refer to fuzzily defined domains, having unknown requirements, with fuzzily defined measures of success. CSSs are intended to support not precisely defined users; otherwise, their users behave in an unconventional way. Therefore, it is advocated that CSSs stimulate users’ imagination, the creation of new ideas, and model creative processes and enable brainstorming process, recombination of ideas, ranging of ideas according to different criteria, and identification of interdependences [44].

According to some scholars, two types of CSS are distinguished [34,35,45,46,47]: individual creativity support systems (ICSSs) and group creativity support systems (GCSSs). The main purpose of ICSSs is to increase the cognitive process, individual inspiration, and the learning and reasoning of individual persons. The most popular tools used in ICSSs include editors, visualization systems, brainstorming, e-mails, spreadsheets, databases and knowledge bases, scenarios, and modeling tools. In turn, GCSSs encompass several types of information systems, for example, group decision support systems, knowledge management systems, computer-mediated communication, which commonly support the process of idea generation and idea evolution as well as selection in groups. GCSS combines the properties of individual creativity support with collaboration and coordination support.

The analysis of the relevant literature allows us to state that there is not a comprehensive view on OCSS and its design. Of the papers reviewed in the literature search, none addressed this topic. A conceptual framework for the design of information systems to provide organizational creativity was not formulated, and no attempt was made to validate it.

We propose to extend the previous classification of CSS and introduce new type of CSS called OCSSs (Table 1).

Table 1: Creativity support systems

<table><tr><td></td><td>Individual creativity support system (ICSS)</td><td>Group creativity support system (GCSS)</td><td>Organizational creativity support system (OCSS) – new quantity of CSS</td></tr><tr><td>Essence</td><td>Creative problem solving, idea generation, creativity limited to narrow domain and individuals</td><td>Work groups, sharing knowledge, communication, creativity limited to selected organization&#x27;s units, departments</td><td>Continuous acquisition of new information resources and the creation of these new configurations (new knowledge, suggestions) to develop new and useful ideas concerning products, services, managerial practices and competitive advantages</td></tr><tr><td>Scope</td><td>Focused on single individual</td><td>Selected groups and teams</td><td>Dedicated to the whole organization and its changeable environment</td></tr><tr><td>Purpose</td><td>Increasing the cognitive process, creative problem solving, individual inspiration, learning and reasoning</td><td>Creating shared idea space, increasing group communication, group consensus</td><td>Increasing competitive advantage and an organization&#x27;s performance by offering rapid access to different, heterogeneous, dispersed information resources, their analysis, knowledge discovery, its visualization, and suggesting some opinions that may be the foundation for the creation of new and useful ideas</td></tr><tr><td>Theories</td><td>Cognitive theory, behavioral theory, motivation theory</td><td>Group decision-making theory, communication theory, design of group decision support systems</td><td>Strategic management, resource-based view, dynamic capabilities, design of management information systems</td></tr><tr><td>Tools</td><td>Editors, visualization systems, brainstorming, e-mails, spreadsheets, limited data bases and knowledge bases, scenarios and modeling tools</td><td>Group Decision Support Systems, Knowledge Management Systems, chat rooms, synchronic and asynchronous trainings, videoconferences, discussion forums, blogs, data marts</td><td>Knowledge bases, data warehouses, Business Intelligence, analytics, multiagent technology, neural networks, search engines, visualization tools, data mining, web mining, opinion mining</td></tr></table>

Source: Elaborated on: [34, 35,45,46,47].

OCSS opens a new emerging type of creativity support. In contrast to previous systems, OCSS is dedicated to the whole organization and its environment. Its purpose is to increase competitive advantage and an organization’s performance by offering rapid access to different, heterogeneous, dispersed information resources, their analysis, knowledge discovery, its visualization, and suggesting some opinions that may be the foundation for the creation of new and useful ideas.

## 3. Theory of organizational creativity support systems design

To address the mentioned objective of this study, two theories are proposed and used: RBV and a multiagent approach. RBV is applied to better know how to manage information resources and deal with them strategically to support organizational creativity. A multiagent approach is a critical and vital part of a theory for the design of OCSSs. Intelligent agents, as autonomous and proactive entities

#

(software), are used to build assistance in performing various human activities, including searching, collecting, and analyzing data; discovering new knowledge; suggesting new ideas; communicating and disseminating new ideas; and conducting different interactions with human participants.

## 3.1. Resource-based View

A new look at the issue of organizational creativity support opens within the RBV. It gives the foundation for a sustainable and comprehensive development of organizational creativity support and a sound basis for stating what information resources and capabilities should be followed in OCSS. RBV argues that the success of an organization’s strategy depends on the configuration of its resources and capabilities that are the basis to building key competences. Acquiring, configuration, reconfiguration, and the developing of available information resources are critical factors in creating a competitive advantage and creating value [48, 49]. An extended approach of RBV resources implies intangible categories including organizational, human, and networks [50]. According to RBV to provide competitive advantage, resources should be Valuable (enable an organization to implement a valuecreating strategy), Rare (are in short supply), Inimitable (cannot be perfectly duplicated by rivals), and Non-substitutable (cannot be countered by a competitor with a substitute) (VRIN). This knowledgebased resource approach of RBV encourages organizations to obtain, access, and maintain intangible endowments because these resources are the ways in which firms combine and transform tangible input resources and assets.

The concept of traditional RBV assumes that the information resources are static and do not consider changes in the turbulent environment of the organization. The answer to these challenges of the environment is dynamic capabilities (DC). The method of resource usage is at least as important as the value of these resources [51]. The benefits derived from the resource pool are transient, so organizations need to focus on continuous acquisition of new resources (information, knowledge) and the creation of these new configurations [5,52]. DC can usefully be thought of as belonging to three clusters of activities and adjustments [52]: (1) identification and assessment of an opportunity (sensing); (2) mobilization of resources to address an opportunity and to capture value from doing so (seizing); and (3) continued renewal (transforming). These activities are required if the organization is to sustain itself as markets and technologies change, although some firms will be stronger than others in performing some or all of these tasks. In the context of organizational creativity support, sensing involves exploring technological opportunities, probing markets, and listening to customers. Seizing refers to [53] (1) solution development (a company’s capability to generate different potential solutions, e.g., process design, concept development, idea refinement), (2) solution evaluation and selection (established procedures to allow for informed decision-making and thus for selecting the most adequate solution for a specific problem), and (3) solution detailing (a plan needs to be forward thinking and have control mechanisms). The last activity—transforming—includes unfreezing, changing, and re-freezing subcapabilities. Breaking up existing work structures and procedures is an important aspect when searching for new suggestions. The acceptance has to be fostered by actively communicating the changes and benefits that result from them. Changing subcapability refers to the actual implementation of the idea change. The last subcapability relates to all tasks necessary to foster internalization of the newly implemented ideas.

In the context of RBV, we interpret organizational creativity support as an information system that enables an organization to acquire, collect, and analyze different information resources and discover new knowledge to create new ideas that concern, among other things, new products, services, managerial practices, and competitive strategies. The RBV approach provides a valuable way for designers of OCSSs to think about how information resources relate to organizational creativity, performance, and competitive advantage. In particular, this approach provides a cogent framework to seek valuable and hard to imitate resources and to assess their strategic value. It helps designers and managers to understand the role of information within organizations.

## 3.2. Multiagent Approach

The concept of the agent in information systems dates back to the 1970s, when studies on programs called “intelligent” were undertaken [54]. The idea of an autonomous object and an interactive actor was presented in 1977 by Hewitt [55]. A new trend of research on agents appeared around 1990, and it

#

concerned the development of the theory and design of architectures of different types of agents, and the ability to communicate between them [56]. It is noted that although “agent” is frequently defined in the literature, there is no universal explanation of the term “agent.” It is often associated with the following notions: intelligent agent, intelligent software, wizards, knowbots, taskbot, userbot, software agent, softbots-intelligent, or software robots. In a particular case, the agent may be a human or an expert in the specific domain. According to Hewitt [55], an agent is an interactive object based on parallel processing, having some internal state and the ability to respond to messages of other objects (actors). The agent is an entity that performs some actions in a particular environment and is aware of the emerging changes. Moreover, it can react to such changes [57, 58]. The agent has a set of goals, certain capabilities to perform actions, and some knowledge (or beliefs) about its environment [59]. In addition, Thomsen [57] describes the agent as “a solution-oriented ensemble of capabilities including natural language processing, autonomous reasoning, proactive computing, discourse modeling, knowledge representation, action-oriented semantics, multimodal interaction, environmenta awareness, self-awareness, and distributed architectures.” IBM [60], in turn, defines intelligent agents as “software entities that carry out some set of operations on behalf of a user or another program, with some degree of independence or autonomy, and in so doing, employ some knowledge or representation of user’s goals and desires.”

Many authors emphasize the specific properties of the agents [59,61,62,63]. They include

• autonomy - the agent operates as an independent process, with no direct human intervention and has control over its actions and internal state,

• reactivity - the agent perceives its environment and promptly answers the perceived changes to its environment,

• pro-activity - the agent not only reacts to the changes to its environment but also manifests a goaloriented behavior and takes initiative,

• social ability - the agent can interact with other agents or humans, using an agent communication language,

• self-analysis - the agent is capable of analyzing and explaining its behavior and capable of detecting its errors or success,

• learning - the agent can adapt and improve by interaction with its environment,

• temporally continuous - the agent runs continuously in its environment, as long as necessary, to implement the task,

• mobile - the agent has an ability to move between different environments.

The belief, desire, intention (BDI) model is one of the most well-known models that is used for programming agents. The model consists of three components [64,65]: (1) Belief - represents the informational state of the agent (including itself and other agents). It may include rules of requesting, which lead to new belief formation; (2) Desire/Goal - reflects the agent’s motivation state. Examples of desires might be “find the best price, best customer”; (3) Intention/Plan - means that the agent starts to perform an action plan. Plans are sequences of the actions that the agent can perform to achieve one or more of its goals.

It has already been pointed out that its knowledge, its computing resources, and its perspective limit the capacity of an intelligent agent. Therefore, it requires forming communities of agents. These communities, based on a modular design, can be implemented, where each member of the community specializes in solving a particular aspect of the problem. The agents must be able to interoperate and coordinate with each other in peer-to-peer interactions [58]. This idea of the agents’ operation is nowadays described as a multiagent system. A multiagent system can be defined as a loosely coupled network of entities that work together to solve a problem that cannot be solved by an individual agent. These entities can show self-organization and complex behavior, even if the individual agent’s strategies are simple [66]. A multiagent system is a network of agents that are reasoning (problem solvers), cooperating, communicating, and negotiating to achieve a specific task. Individual agents can adapt their behavior to the changing environment in which they work [67,68]. A good example of agents’ co-operation is a teamwork in which a group of autonomous agents cooperate, both to develop their own individual goals and for the good of the whole system [69].

The above characteristics of the multiagent approach lead to the conclusion that such an approach can be widely used in the design of complex information systems for organizations. Particularly, it provides a basis for extending OCSSs with flexible, distributed, and intelligent features. Individual and intelligent agents may assist to search, acquire, monitor, discover, and deliver personalized information to various users according their preferences and profiles. They may be focused on providing filtered information of given domains (news, social events, and trends on the market). The advantage of the multiagent approach for the design of organizational creativity support is also the fact that the intelligent agents enable contacts with other agents, databases, and humans through various communication channels.

## 3.2. Proposition of a Comprehensive Framework of Information System Design to Provide Organizational Creativity Support

The suggested framework provides a comprehensive view on the design of information systems to provide organizational creativity support. This framework consists of six stages that are strongly interconnected and are of iterative nature. They include the following:

1. Problem finding and identification of major creative needs of organizations.

2. Acquiring information resources.

3. Information analysis, knowledge discovery, providing some suggestions concerning new ideas.

4. Evaluating and selecting discovered knowledge.

5. Communicating newly discovered knowledge in an organization and considering whether the new knowledge should be transformed into innovation; and

6. Evolving creative knowledge in an organization and organizational learning.

The proposed framework is discussed in the following respects (Table 2):

1. What are the human activities that are conducted in each stage of the proposed framework and how do they move the creative process forward?

2. What are the information resources at play in each stage, what needs to be done with them, and how RBV helps manage information resources and deal with them strategically?

3. What are the ways in which an OCSS might assist, given these activities and resources needs? More specifically, what sorts of agents should be incorporated into OCSS to accomplish this.

Table 2: The research framework—a comprehensive framework—for the design of an information system to provide organizational creativity support

<table><tr><td></td><td>Human activities</td><td>RBV</td><td>Intelligent agents</td></tr><tr><td>Finding problems</td><td>- Identification of creative needs- Specification of terms, phrases, keywords, ontology, business domains that express new business needs</td><td>- Identification and assessment of information resources that would be an inspiration for problem finding</td><td>- Searching and tracking huge amounts of information- Sorting and prioritizing of various documents significant for problem finding.- Storing the results of searching in the form of knowledge maps andsemantic maps</td></tr><tr><td>Milestone</td><td colspan="3">Hierarchization of information and knowledge, decomposition of knowledge, ontology, knowledge maps, semantic maps, list of terms, classes of terms, and relations between classes</td></tr><tr><td>Acquiring information resources</td><td>- Development of organizational culture based on facts and sharing knowledge (motivation to collect and to share information, communication)</td><td>- Elaboration of procedures and methods and the whole strategy to acquire information- Identification of gaps in information and knowledge</td><td>- Acquiring, monitoring, browsing selected information resources- Reacting quickly to some changes in information contents- Promptly answers the perceived changes</td></tr><tr><td>Milestone</td><td colspan="3">A repository to store up-to-date, reliable, complete, and relevant information useful while searching new ideas</td></tr><tr><td>Information analysis, knowledge discovery and providing some suggestions concerning new ideas</td><td>- Development of knowledge center- Motivation to create new knowledge and to share knowledge</td><td>- Elaboration of procedures and methods to discover new knowledge and its utilization- Describing what information sources should be explored in detail</td><td>- Searching some associations and patterns between data, reasoning, and learning- Visualizing discovered associations and patterns- Suggesting some recommendations concerning new ideas</td></tr><tr><td>Milestone</td><td colspan="3">Learning valuable facts from data and from newly discovered knowledgePool of recommendations for new ideas</td></tr><tr><td>Evaluating and selecting discovered knowledge</td><td>- Identification of implications of new knowledge on enterprise performance, competitive advantage, etc.</td><td>- Determining what criteria should be used to evaluate discovered knowledge</td><td>- Providing different documents, reports needed to evaluate new knowledge/ideas- Initiating interactions with human participants- Exchange knowledge among various agents</td></tr><tr><td>Milestone</td><td colspan="3">Pool of best suggestions from the whole pool of the generated ones</td></tr><tr><td>Communicating newly discovered knowledge in an organization</td><td>- Reach all potential departments and individuals who might be interested in utilization of new knowledge/idea</td><td>- Determining what kind of new knowledge and to whom it should be send- Orchestration of knowledge</td><td>- Helping in sharing and protecting knowledge- Presenting particular reports, and results- Sending e-mails to participants- Initiation of talks and forums</td></tr><tr><td>Milestone</td><td colspan="3">Knowledge dissemination</td></tr><tr><td>Evolving creative knowledge in an organization and organizational learning</td><td>- Integration of organization's knowledge with knowledge of customers, suppliers, alliances, etc.</td><td>- Knowledge nets- Learning organization</td><td>- Learning and interactions with others agents and programs- Exchange knowledge</td></tr><tr><td>Milestone</td><td colspan="3">Growth of knowledge, integration of knowledge, new creative needs, and overcoming actual knowledge borders</td></tr></table>

## Problem finding

## Human activities

Problem finding should be considered one of the most important steps in the whole model. It is strongly associated with creative needs of any organization. Problem finding requires an organization/user to specify its creative needs. The creative needs can be expressed in the form of some phrases, whole sentences, and keywords (concerning its business areas, business problems to solve, etc.), which may be the foundation to find some problems. This involves finding out which areas of an enterprise’s functions need changes (or which changes should be necessary in the near term) that would influence, for example, new products, new services, or new managerial practices. These changes may stem from a necessity to improve an organization’s competitive advantage, relationships with customers and suppliers, from willingness to become a leader in a particular sector, and from a desire to enter specific alliances. Various methods and techniques may be applied to know the creative needs better. They include the following: interviews, questionnaires, observations, and documentation analyses.

Creative needs should be examined on the level of an individual, particular employee groups, and the whole organization along with its environment. This also involves analyzing closer and more remote environments. Both internal and external information resources may be the inspiration for problem finding. This implies some necessity to track not only business reports, documents, and databases but also some public reports, scientific databases, patent collections, and the Internet, as well as to consider general trends on the market and activities undertaken by the competition and to pay attention to comments from readers on online news [70]. It is also worth mentioning that by problem finding, it is necessary to analyze the organizational culture, organizational climate, an organization’s styles of management, and its approach to sharing knowledge, group work, and communication.

## Resource-based View

A significant role is played by RBV at this stage. RBV facilitates the identification and the assessment of information resources in the context of problem finding. In addition, careful exploration should be given to what kind of information resources does RBV clarify and why, as well as what information is extremely important for an organization and how this information may help in problem finding. Furthermore, RBV should be helpful in the specification what kind of information is missing, what is incomplete, and from whom/where this information may be acquired. In other words, RBV provides knowledge on what kinds of resources are available and useful in problem finding.

## Intelligent agents

It is really important to support problem finding, although this phenomenon is relatively underestimated in the relevant literature [43]. Some attention is paid to a possibility of decomposition, problem hierarchization, and creation of generalizations with the help of IT [71]. Intelligent agents may replace humans in performing difficult, tedious, and time-consuming actions concerning searching and tracking various information resources that may provide an inspiration to find problems. On the basis of a user query (e.g., in the form of keywords, whole phrases, sentences, or business topics), intelligent agents can visit various information resources. The obtained results (links, documents, files, or databases) are grouped, stored, and then the most valuable sources of information are presented to the user. Intelligent agents are helpful in sorting and prioritizing various documents significant for problem finding. They themselves may specialize in searching specific sorts of information resources (e.g., social media, price comparison websites, patent catalogues, and knowledge portals), communicate with each other, and activate other agents to perform particular activities. Such agents may suggest and help detail (concretize and substantiate) the paths of problem finding, create knowledge maps, and semantic maps. Intelligent agents are also responsible for the permanent collection of user requests, choosing the most adequate methods and tools to serve such requests, and finally collecting the response and sending it back to the user.

The result of this stage should be hierarchization of information resources, decomposition of information (e.g., into smaller, related groups, and subproblems), knowledge maps, semantic maps, and a list of the main sources of information that may be helpful in problem finding. Such activities should facilitate the process of problem finding and further acquiring appropriate and detailed information.

## Acquiring information resources

## Human activities

When there is no knowledge of a given topic, particular individuals must quickly assimilate relevant information and undertake an attempt to acquire the information in question [10, 26]. The acquisition of information resources is one of the most difficult tasks to be undertaken in the whole model. This results from several factors, predominantly including the following:

• considerable dispersion and diversity of information resources,

• no access to numerous information resources,

• poor quality of data in different repositories (e.g., incoherence, inconsistent).

These steps call for the acquiring of both internal and external resources (indicated at the problem finding stage). The former may include paper files, documents that describe the enterprise’s mission and strategy of development, selected sales documents, financial documents, enterprise resource planning systems, databases, data warehouses, business intelligence systems, customer relationship management systems, supply chain management systems, decision support systems, and case history. Organizational creativity increasingly frequently requires acquisition of information that stems from external resources [8]. Such resources may include databases of patents, company reports, government records, library archives, scientific databases, and Internet resources including social media, blogs, and comparison websites. However, it is necessary to remember the imperfection of the human memory that is characterized by limited capability of storing different information. Therefore, different IT tools are recommended to acquire and collect huge amounts of diversified information

## Resource-based View

RBV reminds us that although organizations possess many information resources, only a few of them have the potential to lead the organization to a position of competitive advantage. RBV helps an organization to determine what resources are valuable, rare, inimitable, and nonsubstitutable and what information should be acquired, configured, and reconfigured to capture value from them.

## Intelligent agents

IT enables acquiring and coding huge amounts of diversified information that gets compared with organizational memory. In this context, impressive capacities are offered by intelligent agents together with databases, knowledge bases, data warehouses, in-memory applications, and knowledge portals [72]. Intelligent agents may be incorporated into the accomplishment of tedious and time-consuming tasks that concern acquiring, monitoring, and browsing huge amounts of information (indicated as important for finding problems at the first step of this framework). Users can also schedule intelligent agents to execute on a one-time basis, periodically, or based upon events. Many intelligent agents provide a set of options through which the users can scan the huge data warehouses and websites. Agents may quickly react to some changes in information content, promptly answer the perceived changes, and store the acquired information in databases. These databases may be analyzed later in detail and filtered by users. A result of this stage of the proposed framework should be the establishment of a repository that enables storage of up-to-date, reliable, complete, and relevant information useful while searching new ideas.

Information analysis, knowledge discovery, and providing some suggestions concerning new ideas

## Human activities

The third step of the proposed framework involves the analysis and discovery of new knowledge. The discovery of new knowledge may refer to discovery of (1) new functionalities/features of products, (2) new organizational practices (e.g., new customer service, new forms of cross-selling), (3) new logistics chains and alliances, (4) new technologies, and (5) changes in products design. To understand the importance of discovering new knowledge for an organization, it is necessary to be aware of its relationships with enterprises, industries, or the whole environment [73]. Knowledge may contribute to going beyond traditional business functions and processes, expanding the scope of activities undertaken by organizations, enriching its present functions, and transforming its supply chains into dynamic ecosystems.

The process of knowledge discovery should engage a broadly understood community of an organization that includes decision-makers, employees, customers, suppliers or external experts, and

#

representatives of public institutions [10]. Their diversified knowledge, competencies, and experience may prove useful while proposing original expertise that cannot be created by employees acting on their own. Knowledge discovery requires accessibility to diversified information resources. Therefore, different stakeholders of an organization should be informed which resources they can use. While generating new knowledge, different individuals, departments, and units (managerial personnel, entrepreneurship incubators or departments responsible for improvement recommendations) may turn out to be helpful. This stage of the model proposed, as probably none of the other stages, requires employees to be particularly motivated to create new knowledge and share their knowledge. A significant role is to be played here by management that they are supposed to support the development of organizational knowledge. Organizational culture, organizational climate, and freedom to act are factors that determine organizational creativity.

## Resource-based View

At this stage, RBV focuses on the importance of growth and reconfiguration of knowledge for an organization and its creativity is. RBV highlights that discovery of new knowledge refers to two activities that may be supported both for human or IT tools [74]. The first concerns the widely understood data exploration, and the second concerns data exploitation. Data exploration enables an organization to overcome the border of actual knowledge and its capabilities. This may refer to new technical capabilities, market experiences, and new relationships with the environment. In addition, the exploration is a conscious search for new knowledge sources, enriching of existing resources, adoption of new behavioral orientations, and acquisition of new competencies. Data exploitation concerns the use of existing knowledge bases. It is limited to actual resources and refers to their detailed analysis. RBV stresses that transformation of information resources enabling the development of a unique information resource base is the essence of this stage. Such an information base may be the foundation to provide new ideas.

## Intelligent agents

Intelligent agents can contribute to the growth and expansion of knowledge. Intelligent agents combined with data mining, artificial intelligence, and data visualization techniques [75] allow not only for the exploring of different sources of data but also for the identifying of specific relationships, interdependencies, and patterns in data [11]. Organizations may learn valuable facts from such data. They may point to, for example, different trends that are observed on the market, customer behaviors, or customer purchase preferences. On the other hand, intelligent agents combined with visualization techniques enable better perception and understanding of all interdependencies between different data.

It is also worth mentioning group work tools that may be used to discover new knowledge. These tools show that creativity is not obtained in social isolation. Individuals and groups continuously participate in creative and interactive processes. Employees create knowledge, present it to other members of their teams, and learn from others to eventually modify and enhance their primary ideas. Group work tools combined with intelligent agents allow members of project teams to communicate easily, thus overcoming barriers of time and geographical location. People may work in networks and use joint resources. By integrating information from various databases and from different users, intelligent agents may suggest some recommendations concerning new ideas.

## Evaluating and selecting discovered knowledge

## Human activities

Organizational creativity is an iterative process full of attempts and mistakes [43]. Hence, the process in question requires control, evaluation and selection of the analyzed information/discovered knowledge, and the best suggestions from the whole pool of the ones generated. It is difficult to suggest general criteria be taken into consideration by organizations. This is largely determined by organizational specifics. Novelty and usefulness of suggested ideas may be manifested in a different manner, e.g., new product functions, content, product aesthetics, user-friendliness, or improved product safety. It is worth identifying what implications they may have in the context of enterprise performance.

#

At this stage, RBV gives guidance as to how information resources and discovered knowledge should be compared to one another and perhaps, more importantly, how they can be compared with noninformation resources. RBV sets out a clear link between information resources and competitive advantage, providing a useful way to measure the strategic value of information resources. It is helpful in indicating how newly discovered knowledge may improve among other things, organization performance, sales, relationships with customers, and the position of an organization on the market.

## Intelligent agents

Intelligent agents incorporated with knowledge portals, visualization tools, and group work tools (including virtual conferences, discussion forums, and communities of practice) may turn out to be useful for evaluation, analysis of collected information, and newly discovered knowledge [45]. They allow members of project teams to communicate easily, work in networks, discuss, compare obtained results (new ideas), and evaluate them. Intelligent agents with visualization tools enable not only (as mentioned before) better perception and understanding of discovered data but also evaluation of newly discovered knowledge. They may provide different documents and reports needed to assess (evaluate) new ideas. Additionally, they may be used to initiate interactions with participants.

Communicating newly discovered knowledge in an organization and considering whether the new knowledge should be transformed into innovation

## Human activities

Communicating new knowledge and deciding whether it should be transformed into innovation make up, in principle, the core stage of the whole model. Such communication should reach all potential departments involved (production, marketing, customer service, etc.) and individuals who might be interested in its utilization.

## Resource-based View

RBV argues that having knowledge is insufficient if it does not lead to any innovation. What counts is having the ability to use this knowledge creatively [8]. Such ability is a key to creation of a competitive advantage. Simultaneously, the importance of velocity of organizations reallocating their resources to locations and areas where they can get the highest value should be recognized here.

## Intelligent agents

Intelligent agents may serve to distribute (send) new knowledge/ideas to individuals and whole communities. Intelligent agents allow for easier rooting of creativity in organizational culture. They may facilitate values, beliefs, and standards because they allow for quick transmission of different information to a group of people. Intelligent agents can be incorporated in knowledge portals, intranets, information bulletins, newsletters or employee forums, initiating various discussions and forums between them.

## Evolving creative knowledge in an organization and organizational learning

## Human activities

The last stage of the proposed framework focuses somewhat on the fact that organizational creativity is not a closed cycle but a continuous and dynamic process that should lead to the development of creative knowledge in any organization. OCSSs should be modified in an interactive manner. It means that organizations should continuously diagnose and predict their creative needs and develop the skills and the capabilities to build their innovative potential. This stage calls for identification of various limitations that may result in generating and evolving new knowledge, such as lack of competent persons or experts, insufficient access to some resources of knowledge, inappropriate orientation of knowledge resources, or lack of sufficient financial means.

## Resource-based View

RBV stresses that knowledge builds over time in the head of employees in the form of past decisions, processes in the organization, characteristics of products, interests of customers, and other experiences. This completes the generation of one piece of knowledge but simultaneously attempts to

#

integrate knowledge that comes from different users and various research domains. RVB reminds us that organizational creativity requires continued renewal and expansion of knowledge. It provides the capability for organizational learning, knowledge integration, and the creation of new creative needs.

## Intelligent agents

At the last stage of proposed framework, intelligent agents may be incorporated with several applications and knowledge portals that provide access to different, heterogeneous, distributed databases, warehouses, and documents. They may be helpful in combining various resources from various research domains. Simultaneously, intelligent agents may propose users participate in building and reconfiguring knowledge sources that can be used by various users and for different purposes. This step also leads to thinking whether new agents should be designed aimed at searching and analyzing new and poorly known domains and topics but is important for the further development of an organization.

## 4. Proof of concept of organizational creativity support system design

In this section, the prototype called organizational creativity in social media (OCSM) was presented as an example of the proposed framework being applied. The area of consumer electronics was chosen to illustrate how the proposed framework is used to build such a prototype and how organizations from this sector may draw inspiration to improve its products and services through in-depth analysis of consumer opinion.

Consumer electronics (smartphones, tablets, laptops, cameras, etc.) is one of the most dynamic sectors on the global market. Organizations that want to survive on this market and become a leader should respond quickly to feedback. According to the Boston Consulting Group [76], Polish Internet users are one of the most active groups of consumers in Europe. It is demonstrated not only by the quantity of products bought by Polish consumers (mobile phones, laptops, digital cameras, other gadgets, etc.) but also by their activity in discussion forums, where they express their opinions on the products purchased, compare them to competitors, or even propose some ideas related to their improvement [77]. Ceneo.pl is one of the largest forums in Poland where consumers report their opinions on the products they buy. This forum is used to test OCSM.

## 4.1. Example of organizational creativity in social media design

The example of OCSM design is discussed on the basis of the main steps of the proposed framework. In other words, this example illustrates how the prototype aligns with the proposed framework and how RBV and intelligent agents are used to build such a prototype and how specific users in an organization might interact with the prototype at each step. Four main sorts of intelligent agents, which are incorporated into the design of OCSM, are described (Figure 1). They include: searching agents, monitoring agents, capturing agents, and discovering and suggesting agents. These agents, attributed with functions, rules, and methods to work in the electronic consumer domain, are autonomous entities. They may work independently or collaborate with other agents and users. A manager agent is responsible for the reliability of the whole prototype and manages the operation of the individual agents. Different techniques and tools are applied to develop such a prototype. They concern mainly web mining, text mining, web scraping, web opinion mining, neural networks, search engines, conceptual graphs, and visualization techniques.

![](/api/attachments/WDWA24GR/fulltext/images/7755a1b8d7ce377c4ff72f3ca98276d89cc514e88b3b91542a3c567923ac2eb8.jpg)

![](/api/attachments/WDWA24GR/fulltext/images/11f68518c62155fd8dcfe9a4f8d6d5da68e4f5e63ab7272911b50c7860b525cc.jpg)  
Figure 1: The architecture of OCSM

When designing an OCSM, it was assumed that it should be flexible enough to allow (1) automatic searching and monitoring of various information resources (internal resources and external resources like: the Internet, social media) according to specific phrases and keywords to find particular problems in the domain of consumer electronics; (2) automatic acquisition of various data originating from different, dispersed, heterogeneous resources that may be helpful in searching new ideas concerning new products from consumer electronics; (3) automatic analyzing and discovering new knowledge (e.g., discovery of new product features); (4) automatic visualization of discovered knowledge (e.g., correlations among product features and consumer opinions); (5) automatic suggesting/recommending (e.g., what product features should be primarily improved, changed or what features should be removed); (6) automatic delivery of new knowledge to users, who based on their own knowledge and experience, make decisions on how it finally may be used; and (7) storing of collected, and analyzed knowledge to use by different users.

## Organizational creativity in social media in problem finding

Organizations from the consumer electronics sector in search of new problems and ideas should explore not only their own internal information resources, but their interest should increasingly focus on external resources (e.g., public data bases, patent bases, the Internet, and social media). The Internet, social media, and Ceneo.pl are places where customers express their opinions and preferences about various products (smartphones, tablets, etc.). Such opinions and preferences may be helpful in finding new designs, product functions, and solving a specific organization’s problems. Problem finding in OCSM is assisted mainly by searching agents. Searching agents, in an automatic way, perform tedious, time-consuming operations that concern searching huge amount of information, identifying their origin, access, and credibility. Users give particular key words and phrases that refer to the issue of consumer electronics (e.g., smartphone); with the help of searching agents, the list of relevant and adequate databases, papers, patent collections, links, and web sites (Figure 2) that may be important for problem finding are obtained. They may concern, for example, new technologies, trends in development of smartphones, and other mobile devices. Searching agents also help in the grouping problem domains, the mapping of fragments of knowledge, and visualizing the path of access to needed information. They facilitate the users to find linkages between knowledge portions according to the user profile.

![](/api/attachments/WDWA24GR/fulltext/images/757f063797d11050826a0f0d953e0c212ee0909d9c8bde737a68dc31f4d009ca.jpg)  
Figure 2: OCSM in problem finding  
At this stage, RBV helps establish what kind of information resources (patents, databases, links, papers, and other documents) should be searched in the context of given user requests and what new requests (including new phrases and keywords) should be considered during problem finding.

## Organizational creativity in social media in acquisition of information resources

OCSM uses two groups of agents to acquire information resources. They include capturing and monitoring agents. The task of capturing agents is to search and collect important information about features of the products and their characteristics; product characteristics of the competitors; characteristics of the Ceneo.pl user’s activity; characteristics of the competitor’s activity; characteristics of others users (customer and suppliers) related to the date and time of the activity

#

detection, area of activity, status, and the date and time of the capturing agents’ activation. They mostly acquire certain keywords, different phrases (“positive” and “negative”), or files. A user is provided with an application that allows for clicking a “Run Agents” button to initiate the capturing agent manually any time it is required. A user may quickly and intuitively download from the website information that represent the customers’ opinions concerning given products.

Monitoring agents are used to track the changes in opinions of the users on some smartphones in selected social media or price comparison websites. When the agent detects new content (e.g., new features of such product, new opinions on such product) posted in the price comparison website or in social media, it sends a signal that activates the capturing agent. This group of agents includes agents that monitor changes on (1) the opinions on some organization’s products and services (features, quality), (2) the opinions on some products of the competition, and (3) the opinions of the users (including customers and suppliers) of the other products.

Information collected by individual capturing agents are stored in CSV, SQL, XML, and XLS files and then are loaded to a database called opinion storage. Then, such data are processed and analyzed by discovering and suggesting agents.

## Organizational creativity in social media in the discovery of new knowledge and its evaluation

This stage of the proposed model is supported by discovering and suggesting agents. These agents are responsible for performing various analyses and discovering new knowledge that refer to the opinions of users, customers, and competitors on selected products. More precisely speaking, they: (1) identify features of the selected smartphones and link (associate) these features with the opinions of various customers, (2) carry out analysis on products and perform appropriate analysis focused, for example, on improving some features, (3) suggest some recommendations concerning changes/modifications to product features, and (4) draw up the characteristics of the customers (users activity, changes in preferences). Table 3 presents an example of a set of suggestions generated by the agent for a selected smartphone in the context of positive (“I like this”) and negative consumer opinions (“I hate this”).

The user receives a suggestion that in the first place, product features like appearance, display, functionality, should be improved. Then a product may be made more attractive for users by the organization adding brand unique features such as a fingerprint reader on the screen. The agent demonstrates that these features such as functionality, design, battery life, android, price, camera, and no USB 3.0 cable were evaluated as negative and suggests priority to remove/improve them. Interestingly, these features have been also rated positively by some users. This indicates that these features are very important for users and their evaluation vary individually. Thus, further exploration/data selection should consider criteria such as age, education, place of residence, and consumer gender. Discovered knowledge from such exploration may be useful to develop new and more personalized products. It should be highlighted that a positive rating should not always mean the need for further product improvement. The same concerns the issue of a negative rating. The final decision on the improvement or alteration of the product (e.g., given feature of the smartphone) should be supported by various additional analyses that contemplate business profits, fashion, or media image. The proposed analysis should be treated as important; however, only one of the many analyses should be considered by product development.

Table 3: Suggestions generated by discovering and suggesting agent

<table><tr><td colspan="2">“Positive” features - suggestions- should be still perfected</td><td colspan="2">“Negative” features – suggestions - should be removed or significantly improved</td></tr><tr><td>Product feature</td><td>Priority</td><td>Product feature</td><td>Priority</td></tr><tr><td>Appearance</td><td>Very high</td><td>Functionality</td><td>Very high</td></tr><tr><td>Display</td><td>Very high</td><td>Appearance</td><td>Very high</td></tr><tr><td>Functionality</td><td>Very high</td><td>Display</td><td>High</td></tr><tr><td>Android</td><td>High</td><td>Life battery</td><td>High</td></tr><tr><td>Battery life</td><td>High</td><td>Android</td><td>Medium</td></tr><tr><td>Apparatus</td><td>High</td><td>Price</td><td>Medium</td></tr><tr><td>Execution</td><td>High</td><td>Apparatus</td><td>Medium</td></tr><tr><td>Screen brightness</td><td>Medium</td><td>Lack of USB 3.0 wire</td><td>Medium</td></tr><tr><td>Waterproof</td><td>Medium</td><td></td><td></td></tr><tr><td>Smooth operations</td><td>Medium</td><td></td><td></td></tr><tr><td>Speed</td><td>Medium</td><td></td><td></td></tr><tr><td>SD slot card</td><td>Medium</td><td></td><td></td></tr><tr><td>Replaceable battery</td><td>Medium</td><td></td><td></td></tr><tr><td>Camera photo</td><td>Medium</td><td></td><td></td></tr><tr><td>Firm's applications</td><td>Medium</td><td></td><td></td></tr><tr><td>Fingerprint leader</td><td>Medium</td><td></td><td></td></tr><tr><td>Screen</td><td>Medium</td><td></td><td></td></tr><tr><td>Pulsometer</td><td>Medium</td><td></td><td></td></tr></table>

To make the conducted analysis more clear and intuitive for users, different visualization techniques were applied. Graph structures are useful methods to visualize data. To construct a graph structure, NetworkX 1.8.1 library was used [78]. Graph clustering was performed with the usage of the ForceAtlas2 algorithm that is available in the Gephi package [79,80,81]. All operations involving data processing were performed in the Python 2.7 environment.

Graph structures made the conducted analysis more intuitive and enabled the visualization of object– feature relationships (Figure 3). A graph always has three major vertices (nodes): a node that defines the product, a node that refers to advantages, and a node that refers to disadvantages. Other nodes refer to terms that describe a product. Graph edges have their own weights. Weights of connections in the graph mean the frequency at which a particular term appears. The more frequently appearing the feature, the higher is the weight of the connection with a node of advantages or disadvantages. The visualization presented uses colors to distinguish features attributed to objects. Each color allows for classifying a particular node to a given class of objects, e.g., in this case, advantages or disadvantages. Valuable information for a user is also provided by the size of ‘advantages’ or ‘disadvantages’ nodes. The size allows for quick assessment to find out if a particular object is connected with more positive or negative feedbacks.

quality replaceable battery fast wifi and gps

waterproofscreen

![](/api/attachments/WDWA24GR/fulltext/images/bc89a5b2ee4514836e22d64fe80ed0ef6b18ea8502929e22e80cba710fbb287f.jpg)

battery

price

weak battery handsfreie6aeint scanner

dialler hangs lot of unnecessary stuff

Figure 3: Visualization of the relationship between the features of the selected product and the users opinions (“positive,” ”negative”)

Many inspirations for the product development/improvement may be provided by the analysis of comparing various products together (e.g., competitive products and even products from different segments) (Figure 4).

![](/api/attachments/WDWA24GR/fulltext/images/d256ec702803e5bd24fe265adf66ce817e7152b1d797a9e19b5813b225ee1a8e.jpg)  
Figure 4: Example of data visualization

Figure 4 shows a graph where the nodes are described by the names of various products (e.g., competitive products) and associated with these products, the customer opinions. Smaller nodes labels are not visible due to zooming out the entire graph. The largest nodes represent the features of the products with the highest frequency of occurrence. In turn, the smallest nodes represent the features of the products with the lowest frequency of occurrence, usually associated only with one product. The edges illustrate the relationship of the products with customer feedback. A characteristic feature of this analysis is the presence of a large number of products with universal features (the central part of the graph—price, portable, stylish, fast) and products with unique characteristics prevailing (fingerprint scanner, HD video, extra security—the outskirts of the graph). In the present case, it is difficult to indicate what specific links exist between the various products. The identification of such relationships is, however, essential when comparing the product with other products. These characteristics may be unique (not found in other product). There may also be a reverse situation—they can be commonly found in other products. The example of visualization with a higher degree of data selection is shown in Figure 5. The data selection process consists of two stages. In the first stage, the chosen products are selected for detailed analysis. The purpose of this stage is to reduce the size of the graph. In the second stage, it is possible to zoom in the simplified graph and explore the revealed relations.

![](/api/attachments/WDWA24GR/fulltext/images/87b490c9585cfba29c17ae76a1d5d4801ce7e6dfa80832e3d2a1d05a2e792574.jpg)  
Figure 5: Example of data visualization

Three types of nodes are presented in Figure 5. The first type of node presents the analyzed products. The second type of node describes unique product features (strongly associated with the specific product). The nodes of this type are found in the direct neighborhood of the node representing a given product (e.g., the ring of nodes surrounding Product 1 on Figure 5). The third type of node includes those assigned to more than one product. Where a particular feature is present in more than one product, the node that represents it is placed at a distance proportional to the frequency of cooccurrence with each of the products. For example, the node representing the attribute “Speed” is placed in the central part of Figure 5, as it occurs in Product 1, 4, and 5. Moreover, this node has the same color as the node representing Product 5. The reason is that attribute ”Speed” is most often associated with Product 5.These nodes form specific links between the products and can be used to determine the relationship of similarity between one product and another.

Finally, newly discovered knowledge, its visualization, and some suggestions (e.g., concerning improving some products, introducing new features, and new functionalities), performed by OCSM, are stored in a database—called storage. Such collected knowledge, as well as the knowledge and experience of the user, may be the foundation to generate new ideas and then innovations.

## Organizational creativity in social media in communicating newly discovered knowledge and evolving creative knowledge in an organization and organizational learning

Discovered knowledge is mapped and presented in a knowledge portal. A knowledge portal is a space that some news (e.g., about innovations, business plans) and business activities are discussed, shared, and evaluated by managers, employees, and others users. Such a work space can facilitate communication and collaboration among organizational workers. Discussion forums, wiki, document management systems, intranets, and extranets are the main components of such a portal (Figure 6).

![](/api/attachments/WDWA24GR/fulltext/images/0c5fa44c48db80a7428d5396c6576eaebcab0d3af0dd8c40c51aa8049203e1c2.jpg)  
Figure 6: Knowledge portal for organizational creativity support

Intelligent agents incorporated in the knowledge portal help in finding people with a specific expertise and invite them to discussions, meetings, and knowledge sharing. Intelligent agents are helpful in supporting education and training. They provide a knowledge base for the less experienced users or for a user who just wants to learn more about a particular subject. Intelligent agents in a knowledge portal contribute not only to exchanging knowledge but also to combining new knowledge with already existing knowledge (e.g., customer relationships management systems or other enterprise systems) or replacing already existing knowledge with new knowledge.

## 4.2. Validation of organizational creativity in social media

The presented prototype is a kind of initial validation in the form of a proof of concept. It needs further validation and further application in practice. Regardless of this fact, we can now make an initial assessment of the OCSM. We notice both its advantages and disadvantages. Undoubtedly, among the OCSM strengths, there are

• system flexibility allowing to scan and extract data from various information resources such as the Internet and any social media,

• fast acquisition of data from selected social media,

• quick monitoring and reacting to changes in the contents of particular websites,

• cooperation and communication between agents,

• rapid combination of various resources,

• efficient knowledge discovering and codifying,

• visualization of domain interdependences.

When testing the OCSM, we also noticed its weaknesses. These are mostly

• the relatively long and complex processes of both software development and the configuration of software for the intelligent agents,

• the need to monitor and check the accuracy of the individual agents work, especially in the early stages of their work,

• the need to redesign the work of individual intelligent agents when changing the structures of data bases, web pages, etc.,

• unexpected server and ICT infrastructure downtime can destabilize the work of individual agents.

Summing up, the initial testing of OCSM has proven that such prototype can support mainly (1) tracking and acquiring of information from various social media (price comparison websites), (2) discovering new knowledge (e.g., some patterns, correlations among selected products and consumer opinions), (3) suggesting some ideas and changes (e.g., in product development/improvement), and (4) disseminating and exchanging new knowledge. OCSM provides the organization with relevant information (directly from customers, suppliers, and competitors) about their opinions, interests, and preferences. Such information may be useful in the evaluation of a product’s market position and in the determination of the direction of its further development. It may thus be important for the marketing department, promotion, or research and development department in the search for new and more attractive products.

## 5. Conclusions

Our study attempts to formulate a new, comprehensive framework for information system design to support organizational creativity. It consists of six stages that include (1) problem finding, (2) acquiring information resources, (3) information analysis, knowledge discovery, providing some suggestions concerning new ideas, (4) evaluating and selecting discovered knowledge/ideas, (5) communicating newly discovered knowledge in an organization and considering whether the new knowledge should be transformed into innovation, and (6) evolving creative knowledge in an organization and organizational learning.

The proposed framework incorporates well-established RBV theory and a multiagent approach. RBV provides the right framework for knowing how to manage information resources and deal with them strategically. The model advocates that RBV has a natural application to creativity support. It illustrates that creative processes depend on information flows of various sorts and a capacity of new knowledge discovery. In turn, the multiagent approach presents that particular human activities (important in the context of creativity development) may be supported by various intelligent agents.

The proposed framework is based on paradigms and rules presented by Hevner et al. [82] that refer to canons of design science in information systems research [82,83,84]. They describe how to conduct and evaluate a design process of information systems.

The proposed framework was applied and initially tested in a social media environment. As a result, an OCSS called OCSM was built. Customer opinions from the consumer electronics sector were the center of the analysis. The system consists of four types of agents. They assist and help perform various activities that concern mainly acquiring, analyzing, discovering new knowledge and suggesting some recommendations concerning new and useful ideas. Agents can also communicate with each other, exchange knowledge, and initiate communication with human participants.

Our study makes several theoretical contributions to the relevant literature. First, organizational creativity support is generally an unexplored field of research. Therefore, the current study contributes to the emerging literature on organizational creativity by investigating the issue of the design of information system to support organizational creativity. Second, the current study is one of the rare studies that propose a comprehensive and conceptual framework for the design of an information system to provide organizational creativity support. Third, this study demonstrates how RBV may be used to manage information resources and how a multiagent approach may be applied to support various human activities and tasks. Fourth, the current findings report that monitoring, data acquisition, and analyzing and discovering new knowledge, for the purpose of organizational creativity support may be effectively performed by utilizing intelligent agents. Discovered knowledge as well some suggestion recommended by the OCSS may be helpful for the users in the creation of new ideas. Finally, the current findings provide empirical significance that the design of an information system may play an important role in organizational creativity support. The conclusions of the current study contribute to the relevant literature regarding the importance of a comprehensive view on the design of an information system to provide organizational creativity support. These contributions are significant because the void in the literature regarding these types of conclusions is remarkable. The obtained findings and outcomes of this study should be useful for any designers of information systems as well as managers and organizations willing to use OCSSs.

There are limitations associated with this research that may narrow the scope of the findings and point to potential directions for future studies. The proposed system OCSM is a kind of initial validation of the proposed framework. It needs further validation and testing. OCSM may be inadequate to depict a full picture of acquisition, analysis of different information resources, and knowledge discovery for an OCSS. Therefore, future research studies may include design of new intelligent agents (to make more complex analysis) and more information, e.g., customer opinions on products (depending on the educational level, income, experience, individual cultural values, and loyalty) from different information resources.

## References

[1] T.M. Amabile, A model of creativity and innovation in organizations, in: B. M. Staw, L. L. Commungs (Eds.), Research in Organizational Behavior, Vol. 10, 1988, pp. 123-167.

[2] K.D. Elsbach, A.B. Hargadon, Enhancing creativity through ”mindless” work: A framework of work day design, Organization Science, Vol. 17, 2006, pp. 470-483.

[3] J.A. McLean, Place for creativity in management, The British Journal of Administrative Management, Autumn, 2009, pp. 30-31.

[4] S.J. Shin, J. Zhou, When is educational specialization heterogeneity related to creativity in research and development teams? Transformational leadership as moderator, Journal of Applied Psychology, Vol. 92, 2007, pp. 1709-1721.

[5] D.G. Sirmon, M.A. Hitt,. R.D. Ireland, B.A. Gilbert, Resource orchestration to create competitive advantage: Breadth, depth, and life cycle effects, Journal of Management, Vol. 37, 2011, pp. 1390- 1412.

[6] A. Arora, A. Nandkumar, Insecure advantage? Markets for technology and the value of resources for entrepreneurial ventures, Strategic Management Journal, Vol. 33, 2012, pp. 231-251.

[7] S.A. Zahra, H.J. Sapienza, P. Davidsson, Entrepreneurship and dynamic capabilities: A review, model, and research agenda, Journal of Management Studies, Vol. 43, 2006, pp. 917-955.

[8] R.B. Cooper, Information technology development creativity: A case study of attempted radical change, MIS Quarterly, Vol. 24, No. 2, 2000, pp. 245-276.

[9] I. Nonaka, H. Takeuchi, The knowledge-creating company, Oxford University Press, Oxford, 1995.

[10] D.M. Steiger, Decision Support as knowledge creation. A Business intelligence Design Theory, Interantional Journal of Business Intelligence Research, Vol. 1, No. 1, 2010, pp. 29-47.

[11] D.T. Larose, Discovering Knowledge in Data. An Introduction to Data Mining, John Wiley & Sons, Inc., New York, 2005.

[12] P.N.Tan, M. Steinbach, V. Kumar, Introduction do Data Mining, Addison-Wesley, New York, 2005.

[13] R.A. Baron, Entrepreneurship. An evidence-based guide, Edward Elgar, Cheltenham, 2012.

[14] M. Basadur, T. Basadur, G. Licina, Organizational Development, in: M.D. Mumford (Eds.), Handbook of organizational creativity, Academic Press/Elsevier, London/Waltham/San Diego, 2012, pp. 667–703.

[15] J.D. Houghton, T.C. DiLiello, Leadership development: The key to unlocking individual creativity in organizations, Leadership & Organization Development Journal, Vol. 11, 2010, pp. 230– 245.

[16] T.M. Amabile, The social psychology of creativity, Springer-Verlag, New York, 1983.

[17] J.J. Kao, Entrepreneurship, creativity and organization: Text, cases and readings, Prentice Hall, Englewood Cliffs, 1989.

[18] G.J. Puccio, M. Mance, M.C. Murdoch, Creative leadership. Skills that change, Sage, Thousand Oaks, 2011.

[19] S. Arieli, L. Sagiv, Culture and creativity: How culture and problem type interact in affecting problem solving, Proceedings of Academy of Management, San Antonio, 2011.

[20] M.D. Mumford, K.E. Medeiros, P.J. Partlow, Creative thinking: Processes, strategies, and knowledge, The Journal of Creative Behaviour, Vol. 46, 2012, pp. 30-47.

[21] Y.P. Gong, J.C. Huang, J.L. Farh, Employee learning orientation, transformational leadership, and employee creativity: The mediating role of creative self-efficacy, Academy of Management Journal, Vol. 52, 2009, pp. 765-778.

[22] M. Klijn, W. Tomic, A review of creativity within organizations from a psychological perspective, Journal of Management Development, Vol. 29, 2010, pp. 322-343.

[23] W. Choi, N. Madjar, Y. Yun, Perceived organizational support, goal orientation, Exchange ideology and creativity, Proceedings of Academy of Management, Montreal, 2010.

[24] J. Zhou, R. Ren, Striving for creativity. Building positive contexts in the workplace, in: K.S. Cameron, G.M. Spreitzer (Eds.), The Oxford Handbook of Positive Scholarship, Oxford Press, Oxford/New York, 2012, pp. 97-109.

[25] R. W. Woodman, J.E. Sawyer, R.W. Griffin, Toward a theory of organizational creativity, Academy of Management Review, Vol. 18, No. 2, 1993, pp. 293-276.

[26] S. Parjanen, Experiencing creativity in the organization: from individual creativity to collect creativity, Interdisciplinary Journal of Information, Knowledge, and Management, Vol. 7, 2012, pp. 109-128.

[27] A. Blomberg, Organizational creativity diluted: a critical appraisal of discursive practices in academic research, Journal of Organizational Change Management, Vol. 27, No. 6, 2014, pp. 935- 954.

[28] A. Brennan, L. Dooley, Networked creativity: a structured management framework for stimulating innovation, Technovation, Vol. 25, No. 12, 2005, pp. 1388-1399.

[29] M. Stundgren, A. Styhre, Creativity and the fallacy of misplaced concreteness in new drug development. A white headian perspective, European Journal of Innovation Management, Vol. 10, No. 2, 2007.

[30] T. M. Amabile, E.A. Schatzela, G.B., Monetaa, J. Steven Kramer, Leader behaviors and the work environment for creativity: perceived leader support, The Leadership Quarterly, Vol. 15, No. 1, 2004, pp. 5-22.

[31] J.A. Rosa, W.J. Qualls, C. Fuentes, Involvingmind, body, and friends: Management thatengenders creativity, Journal of Business Research, Vol. 61, No. 6, 2008, pp. 631-639.

[32] M. Baer, Putting creativity to work: the implementation of creativity ideas in organizations, Academy of Management Journal, Vol. 55, No. 5, 2012, pp. 1102-1119.

[33] M. Sirkova, V. Ali Taha, M. Ferencova, P.J. Safarik, An Analytical Study on Organizational Creativity Implications for Management, Polish Journal of Management Studies, Vol. 10, No. 2, 2014, pp. 179-187.

[34] B. Shneiderman, Creativity Support Tools: Accelerating Discovery and Innovation. Communications of the ACM, Vol. 50, No. 12, 2007, pp. 20-32.

[35] M. Voigt, K. Bergener, Enhancing creativity in groups – proposition of and integrated framework for designing group creativity support systems, Proceedings of 46th Hawaii International Conference on System Sciences, IEEE Computer Society, 2013, pp. 225-234.

[36] K. Nakakoji, Meanings of Tools, Support, and Uses for Creative Design Processes, Seoul, CREDITS Research Center: International Design Research Symposium’06, 2006, pp. 156-165.

[37] S. D. Muller, F. Ulrich, Creativity and Information Systems in a Hypercompetitive Environment: A Literature Review, Communications of the Association for Information Systems (CAIS), Vol. 32, No. 1, 2013, pp. 175-201.

[38] M. Klijn,W. Tomic, A review of creativity within organizations from a psychological perspective, Journal of Management Development, 2010, Vol. 29, No. 4, pp. 322-343.

[39] S. Greene, Characteristics of applications that support creativity, Communications of the ACM, Vol. 45, No. 10, 2002, pp. 100-104.

[40] T. Lubart, How can computers be partners in the creative process: classification and commentary on the special issue, International Journal of Human-Computer Studies, Vol. 63, No. 4-5, 2005, pp. 365-369.

[41] F. Ulrich, S. Mengiste, The Challenges of Creativity in Software Organizations, in: B. Bergvall-Kareborn and P. Nielsen (Eds.), Creating Value for All Through IT, Springer, Berlin Heidelberg, 2014, pp. 16-34.

[42] T. Dewett, Understanding the Relationship Between Information Technology and Creativity in Organizations, Creativity Research Journal, Vol. 15, No. 2-3, 2003, pp. 167-182.

[43] N. Davies, A. Zook, B, O'Neill, B. Headrick, M. Riedl, A. Grosz, M. Nitsche, Creativity Support for Novice Digital Filmmaking, in: Proceedings of the SIGCHI conference 2013, Paris, France, ACM, New York, 2013, pp. 651-660.

[44] B. Indurkhya, , 2013. On the role of computers in creativity-support systems, in: A. Skulimowski (Eds.), Looking into the Future of Creativity and Decision Support Systems, Progress & Business Publishers, Kraków, pp. 233-244.

[45] J.F. Nunamaker, R.O. Briggs, D.D. Mittleman, Lessons from a decade of group support system research, Proceedings of 28th Hawaii International Conference on System Sciences, IEEE Computer Society, 1996.

[46] M. Voigt, B. Niehaves, J. Becker, Towards a Unified Design Theory for Creativity Support Systems, in: K. Peffers, M. Rothenberger, B. Kuechel (Eds.), DESRIST, 2012, LNCS 7286, pp. 152- 173, Springer-Verlag, Berlin Heidelberg 2012.

[47] T. Heweet, M. Czerwinski, M. Terry, J. F. Nunamaker, L. Candy, B. Kules, E. Sylvan, Creativity Suport Tools Evaluation Methods and Metrics, in: Creativity Support Tools, A workshop sponsored by the National Science Foundation, June 13-15, 2005, Washington, retrieved from http://www.cs.umd.edu.hcil/CST.

[48] M. Wade, J. Hulland, Review: The Resource-Based View and Information Systems research: Review, Extansion, and Suggestions for Future research, MIS Quarterly, Vol. 28, No. 1, 2004, pp. 107-142.

[49] R. Cosic, G. Shanks, S. Maynard, Towards a Business Analytics Capability Maturity Model, in: Proceedings of the 23 Australasian Conference on Information Systems, Geelong, 2012.

[50] M.J. Ahn, A.S. York, Resource-based and institution-based approaches to biotechnology industry development in Malaysia, Asia Pacific Journal of Management, Vol. 28, No. 2 , 2011, pp. 257-275.

[51] D.H. Hsu, R.H. Ziedonis, Resource as dual sources of advantage: Implications for valuing entrepreneurial – firm patents”, Strategic Management Journal, Vol. 34, 2013, pp. 761-781.

[52] D.J. Teece, G. Pisano, A. Shuen, Dynamic capabilities and strategic management, Strategic Management Journal, Vol. 18, 1997, pp. 509–533.

[53] K. Ortbach, R. Plattfaut, J. Popelbuss, B. Niehaves, A Dynamic Capability-based Framework for Business Process management: Theorizing and Empirical Application, Proceedings of 45th Hawaii International Conference on System Sciences, IEEE Computer Society, 2012, pp. 4287-4296.

[54] S. Russell, P. Norvig, Artificial Intelligence: A Modern Approach, Prentice Hall, New Jersey, 2003.

[55] C. Hewitt, Viewing Control Structures as Patterns of Passing Messages, Artificial Intelligence, Vol. 8, No. 3, 1977, pp. 323-364.

[56] M. Wooldridge, N. Jennings, Intelligent Agents. Theory and Practice, Knowledge Engineering Review, Vol. 10, No 2, 1995, pp. 115-152.

[57] E. Thomsen, Agents uncovered, Intelligent Enterprise, Vol. 5, No. 15, 2002, pp. 45.

[58] I. Rudowsky, Intelligent agents, Proceedings of the Americas Conference on Information Systems, New York, 2004.

[59] L. Sterling, K. Taveter, The Art of Agent-Oriented Modeling, The MIT Press Cambridge, London, 2010.

[60] IBM's Intelligent Agent Strategy, white paper, retrieved on September 15 2012 from http://activist.gpl.ibm.com:81/White Paper/ptc2.htm.

[61] M. Wooldridge, An Introduction to Multi Agent Systems, John Wiley and Sons Ltd., New York, 2009.

[62] C.M. Olszak, T. Bartu<sup>ś</sup>, Multi-Agent Framework for Social Customer Relationship Management Systems, in: E. Cohen (Eds.), Issues in Informing Science and Information Technology, Vol. 10, Informing Science Institute, Santa Rosa, 2013, pp. 368-387.

[63] F. Bellifemine, G. Caire, D. Greenwood, Developing Multi-agent Systems with JADE, John Wiley and Sons Ltd., Chichester, 2007.

[64] J. Chang-Hyun, J. M. Einhorn, A BDI Agent-Based Software Process, Journal of Object Technology, Vol. 4, No. 9, 2005, pp. 101-121.

[65] J. Oijen, W. A. van Doesburg, F. Dignum, Goal-based Communications using BDI Agents as Virtual Humans in Training: An ontology Driven Dialogue Systems, in: J. Dignum (Eds.), Agents for Games and Simulations II, Springer-Verlag, Berlin Heidelberg, 2011, pp. 38-52.

[66] A. Bologa, R. Bologa, Business Intelligence using Software Agents, Database Systems Journal, Vol. 2, No. 4, 2011, pp. 31-42.

[67] D. Weyns, Architecture-Based Design of Multi-Agent Systems, Springer-Verlag, Berlin Heidelberg, 2010.

[68] R. Bordini, J. Hübner, M.Wooldridge, Programming Multi-Agent Systems in AgentSpeak using Jason, John Wiley and Sons Ltd., New York, 2007.

[69] V. Lesser, S. Abdallah, Multiagent Reinforcement Learning and Self-Organization in a Network of Agents, AAMAS 07, Honolulu, Hawaii, ACM, 2007.

[70] L. Qian, Z. Mi, Z. Xin ,Understanding News 2.0: A framework for explaining the number of comments from readers on online news, Information & Management, Vol. 52, Issue 7, 2015, pp. 764- 776.

[71] H. Coskun, P.B, Paulus, V. Brown, J.J. Sherwood, Cognitive stimulation and problem presentation in idea-generating groups, Group Dynamics: Theory, Research, and Practice, Vol. 4, No. 4, 2000, pp. 307-329.

[72] H. Chen, R.H.L. Chiang, V.C. Storey, Business Intelligence and analytics: from Big data to big impact, MIS Quarterly, Vol. 36, No. 4, 2012, pp. 1-24.

[73] A. Tiwana, E.R. McLean, Expertise integration and creativity in information systems development, Journal of Management Information Systems, Vol. 22, No. 10, 2005, pp. 13-43.

[74] D. Lavie, U. Stettner, M.L. Tushman, Exploration and Exploitation Within and Across Organizations. The Academy of Management Annals, Vol. 4, No. 1, 2010, pp. 109-155.

[75] J. Han, M. Kamber, J. Pei, Data Mining. Concept and Techniques, Morgan Kaufmann, New York, 2011.

[76] Polska Internetowa. Jak internet dokonuje transformacji polskiej gospodarki, The Boston Consluting Group, retrieved April 15 2015 from http://www.polskainternetowa.pl/pdf/raport\_BCG\_polska\_internetowa.pdf.

[77] Report of EUROPEAN COMMISSION, Functioning of the market for electric and electronic consumer foods, Brussel, 2012.

[78 ] networkx.github.io, retrieved January 10 2015 from https://github.com/networkx/.

[79] gephi.github.io/toolkit, retrieved January 10 2015 from https://github.com/gephi/gephi-toolkit.

[80] M. Jacomy, T. Venturini, S. Heymann, M. Bastian, ForceAtlas2, aContinous Graph Layout Algorithm for Handy Network Visualisation for the Gephi Software, PLoS ONE, Vol. 9, No. 6, 2014, retrieved January 10 2015 from http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0098679.

[81] M. Bastian, S., Heymann, M. Jacomy, Gephi: an open source software for exploring and manipulating networks. International AAAI Conference on Weblogs and Social Media, 2009, gephi.github.io.

[82] A.R. Hevner, S.T. March, J. Park, S. Ram, Design Science in Information Systems Research, MIS Quarterly, Vol. 28, No. 1, 2004, pp. 75-105.

[83] K. Peffers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A Design Science Research Methodology for Information Systems Research, Journal of Management Information Systems, Vol. 24, No. 3, Winter 2007-2008, pp. 45-77.

[84] H. Simon, The Sciences of the Artificial, MIT Press, Cambridge, MA, 1969.

## Biography

Prof. Celina M. Olszak, Ph.D.,D.Sc. – a professor of Management Information Systems at the University of Economics in Katowice, Poland. She is the chair of the Department of Business Informatics. She is also a DAAD and Swiss Government scholarship holder. She visited and took different courses at universities in Europe, the USA, and Australia. The author of 10 books and over 150 academic journal articles. Her research focuses on decision support systems, knowledge management, management information systems, business intelligence, big data, enterprise resource planning, and IT-based organizational creativity. She is a member of the Informing Science Institute in the USA, the PGV Network, and the Polish Academy of Sciences.

Tomasz Bartu<sup>ś</sup>, Ph.D, D.Sc. – an assistant professor of Management Information Systems at the University of Economics in Katowice, Poland. The author of over 20 journal articles. His research and teaching focuses on business intelligence, customer relationship management, multi-agent systems, and enterprise resource planning systems.

Paweł Lorek Ph.D, D.Sc. - an assistant professor of Management Information Systems at the University of Economics in Katowice, Poland. The author of over 10 journal articles. His research and teaching focuses on enterprise resource planning systems, big data, artificial intelligence, and neural networks.

## Acknowledgments

This paper has been supported by a grant: “Methodology for Computer Supported Organizational Creativity” from the National Science Centre in Poland, 2013/09B/HS4/00473.

Heartfelt thanks go to the Reviewers. Their professional guidance helped the authors give final shape to this paper.
