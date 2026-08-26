---
otero_id: 17015
otero_key: "JMD6KXYM"
title: "Decision support system concepts in expert systems: An empirical study"
authors: "Georgios I. Doukidis"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90021-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision Support System Concepts in Expert Systems: An Empirical Study

Georgios I. DOUKIDIS

Information Systems Department, London School of Economics, Houghton Street, London WC2A 2AE, UK

This paper reports on a survey carried out on 67 ES to investigate whether they employ DSS concepts. The author examines several DSS frameworks and proposes a questionnaire model to conduct the survey. The survey data are analysed and the paper concludes that the three fundamental DSS issues: semi-structured task, support, and effectiveness are explicitly applied in ES. It shows also that although both DSS and ES have similar aims, they accomplish them in completely different ways. The differences are in the boundary of problem space and the way to tackle problems.

![](/api/attachments/JMD6KXYM/fulltext/images/789b121d32cfd8c79480dcbf52c030c74a46b94094d49dd8e0ced3b352589763.jpg)

Georgios I. Doukidis received his B.Sc (1980) in mathematics from Thessaloniki University, and his M.Sc (1981) and Ph.D (1985) in Operational Research from the London School of Economics. Since 1984 he has been a lecturer in the Information Systems Department at the London School of Economics. His research interests include: Expert Systems Development (Knowledge Acquisition and Development Tools), Knowledge-based Management Support Systems, Simu lation and Artificial Intelligence, Intelligent Tutorial Systems and National Information Technology Policies. He has published approximately 15 papers in the above mentioned areas and he is the co-author of two books: 'Lisp; from foundations to applications' and 'Developing Expert Systems'. He is also co-editor of the book 'Knowledge-based Management Support Systems'.

## 1. Introduction

DSS and ES are two growing areas in computer applications, both aiming at supporting users in problem solving. ES features are currently employed in DSS applications which include knowledge representation techniques, 'expert systems' languages and intelligent interfaces. The strong shift in orientation of thinking and practice towards knowledge-based DSS is becoming more and more apparent.

Fox [12] argues that in the organisational environment various types of knowledge are required to decide what operations to perform, how and when. In order to provide support to decision-making and problem-solving activities what is needed is appropriate eliciting of knowledge and representation of that knowledge in the DSS framework. De Suranjan [8] therefore suggests that the incorporated intelligence in DSS should capture not only the knowledge of the decision maker/expert but also should include knowledge of some intentions and goals of the decision makers, as well as, knowledge of what they think the system can do. The most common KR schemes used in DSS frameworks are based upon predicate logic, semantic networks, production rules and frames. Bosman [5] emphasises that knowledge representation as a means to detect problems and generate alternatives should become a basic attribute of DSS in the future. Intelligence in DSS, through knowledge representation, is getting so popular that Humphreys [14] proposes a framework where intelligent approaches are based on how, when and at what level such support should be provided within the whole decision-making process.

Many writers, including Coelho [6] and Lee [18], propose the language Prolog and the technique of logic programming as tool for implementing DSS. The reasons for the wide use of Prolog are its flexibility and its ability to provide manipulation of logical expressions. Fox [12] uses SRL (a frame-based language) to demonstrate representational concept for decision support of a job-shop scheduling task. It seems that the popular languages within the ES community will become increasingly accepted if the need for knowledge (and hence the need for representing it) is well received within the DSS community.

ES user-support tools, and more specifically the intelligent interfaces, are becoming critical components in the decisionmaking and problem-solving process [9, 3 and 17]. These intelligent interfaces bring additional flexibility in the development process and more friendliness between user and system. The above result in the improvement of the system's efficiency and effectiveness.

Although there is a lot of discussion about the various ES concepts with actual and/or potential use in the DSS framework, not enough research has been done to analyse the opposite assumption. Pfeifer and Luthi [21] and Kurstedt [16] have discussed, from a theoretical perspective, the relationship between DSS and ES; and therefore have mentioned, to some extent, the combination of DSS concepts in the ES modelling approach. In this paper we report on a survey carried out on 67 ES to investigate empirically weather ES employ (and to what extent) DSS concepts.

The following section examines several DSS frameworks, compiles a list of key issues and proposes a general framework for dealing with DSS concepts which include: background, role, design features, components, prescriptive and descriptive view, stages of decision and levels of activities. This framework is used to conduct the survey. Section 3 overviews the survey by outlining the survey model.

Sections 4 and 5 analyse the results and conclude that three fundamental DSS issues (semi-structured task, support, and effectiveness) are explicitly applied in ES. It proves also that the main difference is that, although both DSS and ES have similar aims, they accomplish them in completely different ways. The differences are in the boundary of problem space and the ways to tackle problems.

DSS encourages the user to explore a wide problem-space. Instead of fixed problem-solving process, the system provides a flexible problem-solving environment of tools and data for the user to play with in his own way. On the other hand, the ES approach bounds the problem area into a well-defined domain. Past experience on repetitive tasks are formulated as a problem-solving process for future uses. System operation is goal-orientated (pre-defined) and is usually system-driven.

The survey also suggests that the difference in problem-space has implications in organisational applications. DSS mainly serve the strategic and management level whereas ES usually support operational activities.

## 2. A Framework For Dealing With DSS Concepts

This section present six dimensions under which the various DSS concepts can be identified and analysed. The six dimensions include: role, design features, components, prescriptive and descriptive views, stages of decision, and levels of activities. This section is based on views by Keen and Morton [15], Sprague [23], Pfeifer and Luthi [21], Stabell [26] and Bosman [5].

## 2.1. The Role of DSS

Our major concern here is the role of DSS taken from a user's point of view, which includes the goal, paradigm and domain. The following five issues fall within the scope of this group: semi-structured task, support decision-making, effectiveness, multi-objective, multi-domain, individual and group decision.

## (a) Semi-Structured Task

The term ‘semi-structured’ can be clarified by looking into the meaning of ‘structured’ and ‘unstructured’. Structured tasks are repetitive and routine to the extent that a definite procedure has been worked out to handle them. This kind of work seldom involves a manager. The decisions in these situations are so well understood that they have been given to clerks or have been automated by computers. An example of a structured task is inventory reordering (There is a number of mathematical models to determine the optimal reorder quantities).

Unstructured tasks are those that have no specific procedure to deal with. They may be novel or extremely complex. A manager tackles unstructured problems through his extensive experience, subjective judgement and, sometimes, by inspiration. These problems cannot be formulated precisely. Examples are hiring staff, research and development, fixing company policy, etc.

Semi-structured tasks are decisions where managerial judgement along will not be adequate, perhaps due to the size or complexity of the problem. On the other hand, mathematical/analytical models are also insufficient due to their simplified underlined assumptions. Therefore, manager and computer have to work together. Sprague [25] describes these tasks as TYPE 2 information activities which have the following characteristics:

\- Transaction: few transactions, but each is more costly or valuable than traditional DP.

\- Process: work is process-independent (that means one may achieve the same result in different way).

\- Output: output is not easily measured.

\- Data: work deals with concepts which are represented in a less well-structured form, usually with a great deal of ambiguity.

Examples of semi-structured tasks are bond-trading, budgeting, capital investment analysis, etc. So, how is DSS related to these 3 types of tasks? DSS is most effective in semi-structured tasks. That is where the system provides mathematical/analytical tools and models to evaluate the situation and the user adds his experience and judgement to make a decision. On the other hand, DSS is not necessary in structured tasks since a precisely defined computer program can do a better job. It is also not effective in unstructured tasks because of the lack of analytical tools to support it. However, one must note that the boundaries of structured, semi-structured and unstructured are by no means clear-cut and they are shifting by following development in decision making and in technology.

## (b) Support Decision Making

Since semi-structured tasks cannot be automated, and they are difficult for a 'barehanded' manager to handle effectively, the aim of DSS is to help the manager. The DSS itself does not make decisions, it merely provides the tools and data to amplify the capability of the manager. It is the manager who eventually makes the decision. The term 'support' has 2 'side' implication: i) To manipulate the tools in a flexible manner, the system must be user-driven and user-friendly. ii)

To simulate effectively, one has to understand the cognitive behaviour of the user.

## (c) Effectiveness

Traditional DP focuses on efficiency, that is to get things done quickly and cost-effectively. DSS focuses on effectiveness, that is to do the relevant things and do them in the best way. For example, an ‘accurate’ sales forecast is a matter of effectiveness but a ‘quick’ forecast is a matter of efficiency. Of course one can’t ignore the efficiency because the system has to respond within a reasonable time in an interactive session.

## (d) Multi-Objective, Multi-Domain

DSS is to support current and future decisions, the exact tasks of which are unknown at the time the system is being developed. Moreover, the system is expected to support a range of tasks rather than a specific one. Therefore, the system must be very flexible and capable of achieving different objectives. It also implies that a range of information and data from different domains are expected.

## (e) Individual and Group Decision

The discussion so far might give the impression that an individual manager uses DSS to make a decision. Well, this is not true most of the time. There are more group decisions than individual decisions. When designing a DSS therefore, it is important to know whether it is intended to serve one or a group of managers.

## 2.2. Design Features

Here we analyse the properties expected in system design which include: user-driven and interactive; user-friendly interface, primitives, 4GL; and adaptive development.

## (a) User-Driven and Interactive

As Pfeifer and Luthi [21] point out, 'To achieve the desired effect, the DSS must allow the user to confront a problem in a flexible personal way by providing the ability to manipulate the data and models.' The initiative should always be with the user. He can play with the model to evaluate the situation and the implications of his decision.

(b) Friendly Interface, Primitives, 4GL

As the system is user-driven, an easy-to-use interface is a crucial component. The interface may be in a graphical mode, natural language, menu dialog or, less desirably, command language.

Primitives are a set of non-procedural commands to enable a user to get what he wants without knowing how. As mentioned by Keen and Morton [15] and Pfeifer and Luthi [21], there can be 4 levels of support (access data, filter data, computation comparison and projection, provide useful models), and subsequently, we may have 4 level of primitives.

4GL is a very general term which may include a report generator, a graphic generator, application and spread-sheet packages. 4GL are basically simple non-procedural languages which provide built-in DBMS, statistics, report-generating routines. The aim is to enable quick and flexible development of applications without the needed of DP expertise. Clearly the properties: simple, user-driven, quick, DBMS, non-procedural, statistics command and report generation match well with the requirement of a DSS.

## (c) Adaptive Development

DSS have to evolve and learn from the environment because:

\- the decision environment is changing;

\- the user does not always know what he actually needs;

\- new models, techniques and technology are being introduced;

\- the user himself undergoes a learning process and expects the system to improve with him.

## 2.3. Components

If Sprague's [25] framework on DSS structure is adopted, then such a system will consist of 3 components: data sub-system, models system and dialog sub-system.

Data sub-system can be external, the system simply provides a virtual link to external databases. The interface may be in WIMP, natural language, command language or simply menu-type dialog. The model's sub-system enables the user to manipulate the models and tools in a flexible way.

The models associated can be classified into formal and informal.

Formal models include OR, simulation, statistics' models and, perhaps government regulations. These are rigorous models. With correct input, they can produce the best information. Informal models are soft models. They are created to solve problems based on past experience. As in expert systems, heuristics are formulated in a decision tree type model. With correct input, they produce reasonable suggestions (but may not be the best).

## 2.4. Prescriptive and Descriptive View

To support effectively, one must understand how a decision is made. Keen and Morton [15] emphasise the balance between prescriptive and descriptive perspectives in decision process. They indentify 5 views which are common in practice.

In an economic, rational concept (prescriptive) the decision-maker knows all the alternatives and is able to choose the best one. In a satisfying, process-orientated view (descriptive) managers do relatively limited analysis and choose a 'good enough' solution (It is also described as 'bounded rationality'). The organisation procedure view (prescriptive) highlights the communication and co-ordination structure, and the standard operating procedures by which decision-making is systematised and simplified. In a political view (descriptive) decisions are frequently dominated by bargaining and conflict among organisational sub-groups. In individual difference view (descriptive) an individual's personality and style strongly determine the choices and behaviour.

These views look into human decision-making in different ways. In DSS, prescriptive elements are manifested in formal models and descriptive elements are either formulated as informal models or left to the decision-maker.

## 2.5. Phases Of Decision

The stages of decision must be clarified before support is designed. A well-known framework is that proposed by Simon [24], who identifies 3 decision stages: intelligence, design, choice.

Intelligence is the stage where vital information is collected and evaluated. Design is the stage where alternative solutions are formulated. Choice is where a final decision is made from the alterna-

Table 1.

tives. Each stage needs different support because of the differences in the required data and tools. Besides, it is equally important to clarify which stage needs to be and can be supported (some stages may be well-structured or unstructured).

## 2.6. Level Of Organisational Activities

Anthony's [1] paradigm in organisational activities is widely accepted by management researchers. It is important in DSS because each level involves quite different activities.

The paradigm consists of 3 levels of activities: strategic planning (long-term planning concerning the decisions such as corporate objectives, resource allocation, etc.), management control (medium-term planning ensuring the company is moving towards the corporate objectives, e.g. budgeting, pricing, etc.), operational control (processes ensuring work is carried out as planned).

Keen and Morton [15] point out that variables such as accuracy, detail, time horizon, frequency of use, source and scope change across the levels. So it is important to know which levels of activities are to be supported. In a survey on 42 companies by Wagner [28], all applications reported were in the middle to top management area, such as strategic planning, budgeting, financial and economic forecasting. Clearly current DSS practice concentrates on strategic and management levels.

## 3. The Survey

In the survey, data were extracted from published ES cases. Since the aim is to investigate whether ES in general shares DSS concepts, the collection of cases spans different disciplines rather than being limited to business decisions (for which DSS was originally developed). The application areas are outlined in table 1.

Various writers have pointed out that decision-support should be and can be expanded outside the business management domain, and during the survey this trend was indeed observed. For example, in the CRI Directory of Expert Systems [7], many systems in the ‘decision support’ category concern medicine and engineering. Of course this does no imply DSS is the same as ES, it only means that the idea of decision-support has been expanded to a wide range of disciplines.

Overview of Application Areas.

<table><tr><td>Domain</td><td>No. of cases</td></tr><tr><td>Engineering</td><td>18</td></tr><tr><td>Finance</td><td>15</td></tr><tr><td>Manufacturing</td><td>8</td></tr><tr><td>Medicine</td><td>4</td></tr><tr><td>Administration</td><td>3</td></tr><tr><td>Agriculture</td><td>2</td></tr><tr><td>Teaching</td><td>2</td></tr><tr><td>Law</td><td>2</td></tr><tr><td>Other areas</td><td>13</td></tr><tr><td>Total</td><td>67</td></tr></table>

Table 2.

The Questionnaire Model.

```txt
Background
Application area:
Year:
Research/operation:
Role
support/replace:
semi-structured task:
effectiveness:
multi-objective:
individual/group decision:
Design features
User-driven:
Interactive:
Interface-WIMP:
Natural language:
Command language:
menu dialog:
Primitives:
4GL:
Adaptive development:
Components
Data sub-system:
Models sub-system-formal:
informal:
Dialog system:
Prescriptive/Descriptive view
Normative model:
Heuristic:
Regulation/instruction:
Stages of Decision
Intelligence:
Design:
Choice:
Level of activities
Strategic:
Management:
Operational:
```

Most of the cases were published after 1984. At the time of publication, about half of the systems are in prototype stage and the remaining half are in operation.

## 3.1. The Questionnaire Model

The questionnaire model is composed from the list of key concepts mentioned in the previous section. A sample is illustrated in table 2. Some entries in the questionnaire are modified to suit the ES context:

(a) 'year' refers to the year the paper was published.

(b) The ‘Research/Operation’ entry is to specify whether the system is in the research (prototype included) stage or in operation at the time of publication.

(c) While DSS supports users, ES, as claimed by some writers, are to 'replace' the user. So the entry 'support' is modified to 'support/replace'.

(d) 'User-friendly interface' is expanded to 4 sub-entries: WIMP, natural language, command language, menu dialog.

(e) In the prescriptive/descriptive dimension, 'normative model', refers to OR, statistics simulation, finance, economic models. 'Heuristic' refers to work experience. 'Regulation/instruction' refers to legal regulations and work instructions.

## 4. Overview of the Results

## 4.1. About the Role

(1) Support/replace: The following data are obtained.

<table><tr><td></td><td>percentage</td></tr><tr><td>support</td><td>87%</td></tr><tr><td>replace</td><td>13%</td></tr></table>

Clearly, the role of ES in most cases is to support a user. This matches with the aim to supply expert advice. Note that ES replace human experts but not the end users (they are usually non-experts).

(2) Semi-structured task:

<table><tr><td></td><td>percentage</td></tr><tr><td>semi-structured</td><td>100%</td></tr><tr><td>structured</td><td>0%</td></tr></table>

It is necessary to note that the boundary of semi-structured and structured is by no means clear cut. For example, XCON [19] (one of the most successful ES) deals with the configuration of computer system component (e.g. processor, I/O devices, wiring, etc.). The configuration expertise comes from experienced technicians because there is not algorithm for doing such work. The system has been in operation for a few years and has proven to be successful, reliable and performing better than technicians in most cases. So one might argue that the task has become structured. The ES approach is to structure the semi-structured task, but it is difficult to estimate how far the task is being structured. Can it deal with very special cases?

Therefore in this survey the original environment faced by human staff is considered. Subsequently, all of the cases are classified as dealing with semi-structured tasks (Note that many of the tasks are close to structured).

## (3) Effectiveness:

<table><tr><td></td><td>percentage</td></tr><tr><td>effectiveness</td><td>93%</td></tr><tr><td>efficiency</td><td>7%</td></tr></table>

Only 5 systems address themselves to improve efficiency. The remaining aim at better-quality work. Again, this matches with the aim of ES (i.e. to provide expert advice).

(4) Multi-objective:

<table><tr><td></td><td>percentage</td></tr><tr><td>multi-objective</td><td>3%</td></tr><tr><td>single-objective</td><td>97%</td></tr></table>

While DSS is so flexible that the user can perform a range of decision-making, ES is clearly not. The only 2 multi-objective ES (ROME [22] and P/G% [20]) are actually intelligent spreadsheet packages (that is why they can be multi-objective). In fact, many of the ES allow the user to select which goal to evaluate. However, they are not classified as multi-objective because these goals (objectives) are pre-defined. The system cannot evaluate any goal which is not in the knowledge bases.

## (5) Multi-domain:

<table><tr><td></td><td>percentage</td></tr><tr><td>multi-domain</td><td>13%</td></tr><tr><td>single-domain</td><td>87%</td></tr></table>

Again, multi-domain is clearly not common in ES. 87% of cases employ knowledge from well-bounded (more precisely, artificially bounded) single-domain. Multi-domains ES is more common in finance and business applications. For example, ESTEAM [4] and SAES [13] employ knowledge concerning accounting, economics, and business.

## (6) Individual/group decision:

The situation is clear. None of the covered systems explicitly accounts for group-decision.

## 4.2. Design Features

## (1) user driven:

User-driven ES are common in CAD-related areas. An example is ANALYST [2]. It is a tool developed for the CORE method for information systems analysis and design. The user can freely construct activities charts by moving the icons displayed on the screen. The system intervenes only when error is detected.

<table><tr><td></td><td>percentage</td></tr><tr><td>user-driven</td><td>15%</td></tr><tr><td>shared between system and user</td><td>13%</td></tr><tr><td>system-driven</td><td>67%</td></tr><tr><td>non-interactive</td><td>5%</td></tr></table>

The mode of operation in system-driven systems is rather standard. The system first requests the user to select a goal, then asks for necessary data during evaluation, and finally, returns a conclusion.

An example of shared-driven system is REACTOR [22]. It is an ES for power plant control. The control panel operator can evaluate the condition of the plant through the ES and makes adjustment. The ES itself also makes real-time monitor over the condition and can take automatic action in case of emergency.

By putting ‘user-driven’ and ‘shared’ into one group and ‘system-driven’ and ‘non-interactive’ into another group, we might have a clearer picture.

<table><tr><td></td><td>percentage</td></tr><tr><td>user/shared</td><td>28%</td></tr><tr><td>system/non-interactive</td><td>72%</td></tr></table>

It shows that in 72% of cases, the system controls the evaluation. The user simply supplies the data and has no control over evaluation.

## (2) User-friendly interface:

Basically, most of the systems are quite user friendly. The type of interface is as following.

<table><tr><td></td><td>percentage</td></tr><tr><td>WIMP</td><td>16%</td></tr><tr><td>natural language</td><td>7%</td></tr><tr><td>command language</td><td>4%</td></tr><tr><td>menu dialog</td><td>63%</td></tr></table>

Clearly, traditional menu dialog is still the most common form of user/system communication. New user system interface technologies such as WIMP and natural language processing have only a limited impact on ES. The popularity of system-driven menu dialog shows the persisting influence from the MYCIN type interface.

## (3) Primitives (non-procedural commands):

Primitives are found in 4 cases only and they are embedded in the system command language. They are not used because they are not suitable for system-driven systems (The aim of primitives is to enable easy user control).

## (4) 4GL:

The situation is very clear. Apart from primitives (which is a 4GL feature), none of the cases clearly claims or shows 4GL properties.

## (5) adaptive design:

Almost all cases undergo adaptive development (not clear in a few cases). There may be 2 reasons: a) To learn and evolve is one of the principle aims in ES. b) ES Structure (i.e. knowledge bases and inference engine) enables easy modification.

## 4.3. Components

The following data are obtained.

<table><tr><td></td><td>percentage</td></tr><tr><td>data sub-system</td><td>60%</td></tr><tr><td>models sub-system (formal)</td><td>48%</td></tr><tr><td>(informal)</td><td>100%</td></tr><tr><td>dialog sub-system</td><td>96%</td></tr></table>

37 (55%) ES have data, models (formal or informal) and dialog sub-systems.

Databases are involved in 60% of the cases. It means that 40% of the ES rely completely on the user to collect data. It also reflects that many of the data are non-numeric. In fact, symbolic data such as observations (eg. patient's symptoms and machine fault) and facts (e.g. qualification, situation) are very common, especially in systems without a database.

Many of the databases and DBMS are external. The ES access them for required data. Note that the role of the data sub-system in ES is quite different from what we generally expected. In most cases (except the user-driven systems), the required data are pre-defined in the knowledge bases and are not controlled by user. The user cannot use any database language to manipulate data.

In ES, heuristics are formulated into a tree or network structure. So, a ‘heuristic knowledge base’ can be regarded as an informal model. Whereas ‘formal knowledge base’ (e.g. base on normative model, regulations) can be regarded as a formal model. This survey shows that about half of the cases employ a formal model, but almost all cases employ a certain degree of heuristic and hence involve informal model.

On the other hand, all, except the non-interactive systems, have a dialog sub-system. If one observes that 55% of the ES have data, models (formal or informal) and dialog sub-system then it can be said that more than half of what are claimed to be ES have a conceptual DSS structure. It is suggested $[10,11]$ that the environment that is useful for decision support is resulted by the integration of an ES with a simulation model and a database.

## 4.4. Prescriptive / Descriptive

<table><tr><td colspan="2"></td><td>percentage</td></tr><tr><td rowspan="2">formal:</td><td>normative tools</td><td>33%</td></tr><tr><td>regulations/instructions</td><td>19%</td></tr><tr><td>informal:</td><td>heuristics</td><td>100%</td></tr></table>

A prescriptive view is concerned with what should be done. The main tools are normative models, regulations and work instructions. A descriptive view concerns what actually is done. The source of descriptive information is people's experience. In the survey, it is found that 33% of cases use normative tools. This shows that management sciences, although not uncommon, are relatively not as important in ES as in DSS. On the contrary, descriptive view shows its dominance. All cases more or less employ some heuristics. In many cases, the entire knowledge base is formed by work experience.

## 4.5. Stages of Decision

<table><tr><td></td><td>percentage</td></tr><tr><td>intelligence</td><td>72%</td></tr><tr><td>design</td><td>31%</td></tr><tr><td>choice</td><td>63%</td></tr><tr><td>more than 1 stage</td><td>54%</td></tr><tr><td>all 3 stages</td><td>16%</td></tr></table>

This shows that ES are concerned more with about providing information (intelligence) and a conclusion (choice) than giving different alternatives. This in fact matches the common ES target: to tell the situation and conclusion. Of course, some systems (31%) provide alternatives as well.

Note that only 16% of the cases support all 3 stages of decision-making. This might be lower than DSS in general. INTEREST RATE SWAPPING SYSTEM [22] is an ES which serves all 3 stages. Interest-rate swapping is a service provided by financial institutions arranging 2 companies to swap their loans. The system can provide information about the applicant company (intelligence), a list of suitable partners (design), and the best partner (choice).

## 4.6. Organisational Level of Activities

<table><tr><td></td><td>percentage</td></tr><tr><td>strategic</td><td>3%</td></tr><tr><td>management</td><td>24%</td></tr><tr><td>operational</td><td>78%</td></tr></table>

If DSS are concentrated on strategic and management work, ES are clearly doing the reverse. The majority of ES focus on operational tasks. The figure supports the argument that ES are to tackle repetitive problems since most operational tasks are repetitive. Heuristic cannot be formulated if the work is not repeated many times. Single shoot problems are better handled by human experts using DSS.

It is noted in the survey that many of the operational tasks are diagnostic/trouble shooting in nature. The system asks about symptoms/faults and gives advice on treatment/repair. This shows that a MYCIN type system is still the most popular in ES. (Note that the term ‘diagnostic’ in an ES context is not limited to medicine, it could be financial problems, business problems, etc.).

## 5. Conclusions

In recent years it has become apparent that ES and DSS both operate in the same application area – the area in which technology based systems provide advice and support for a range of human activities ranging from aiding diagnostic and fault finding activities to those concerned with planning and decision making. Doukidis et al. [11] and Turban [27] suggest that much can be gained from integrating the expert system and decision support approaches. They claim that the two approaches can complement each other, creating a powerful, integrated, computer-based system that can considerably improve managerial decision making.

The survey has shown that similar to DSS, ES address semistructured problems and they support users to improve the effectiveness of their work.

So, DSS and ES share similar aims. However, ES are less flexible and can support only rigidly defined goals under a well-bounded domain. The inflexibility is partially caused by the high system control over evaluation process. This implies that the user cannot manipulate the tools (knowledge) during the process to suit his own preference. Lack of user-control is also reflected by the absence of primitives and 4GL features. The tools employed in ES also differ from DSS. ES relies mainly on heuristics while DSS is based more on normative tools. In organisational aspect, ES is more common in providing information and advice for operational activities, whereas DSS is mainly for strategic planning and management control. Finally, the data/model/dialog DSS structure is found in roughly half of the ES.

How far does this empirical study match/contrast with theoretical work in this area. One DSS/ES contrast is from Pfeifer and Luthi [21], and the empirical study described here suggests 2 main mismatches:

\- In the ‘goal of the system’ entry, Pfeifer and Luthi argue that ES is to supply the complete solution. However, this survey shows that in 63% of cases the ES give a final choice, that means 37% of ES give only advice for a solution and therefore they are part of a modelling activity.

\- The user of DSS is limited to the manager in the contrast. This limits DSS to the management domain. As pointed out earlier, the DSS approach has been expanded to other areas and the user can be an engineer, technician, doctor, etc.

So, what concepts are shared by DSS and ES? The survey shows that 3 fundamental DSS issues: semi-structured task, support, and effectiveness are explicitly applied in ES. What is the difference? Although both DSS and ES have similar aims, they achieve them in completely different ways. The main differences are the boundary of the problem-space and the way to tackle problems.

DSS encourages the user to explore a wide problem-space. Instead of a fixed problem-solving process, the system provides a flexible problem-solving environment of tools and data for the user to play with in his own way.

The ES approach, on the other hand, bounds the problem-area into well defined-domains. Past experiences on repetitive tasks are formulated as problem-solving processes for future use. The system's operation is goal-orientated (pre-defined) and it is usually system-driven.

The difference in problem-space has implications in organisational applications. DSS mainly serve the strategic and management level but ES usually support operational activities. This phenomenon is well reflected in the survey results.

## Acknowledgement

I would like to thank Sumy Yuen for his enormous help in completing the survey and Katerina Kontogiani for the stimulating discussions on knowledge-based DSS.

## References

[1] R.N. Antony, Planning and Control Systems: A Framework for Analysis, Studies In Management Control (Harvard Business School, 1982).

[2] T. Bernold, ed., Expert Systems and Knowledge Engineering: Essential Elements of Advanced Information Technology (North Holland, 1985).

[3] W.R. Blanning, A System for Natural Language Communication, in: L.F. Pau, Ed., Artificial Intelligence in Economics and Management (North-Holland, 1986).

[4] A. Bonarini et al., A Knowledge Based Architecture for Cooperative Interactive Problem Solving: An Application to Financial Advice Giving, in: Esprit 85 Status Report Part 1 (North Holland, 1985).

[5] A. Bosman, Decision Support Systems: A Discipline or a Vision, in: E.R. McLean and H.G. Sol, eds., Decision Support Systems: A Decade in Perspective (IFIP, 1986).

[6] H. Coelho, DSS versus ES: The case of R&D Management, in: E.R. McLean and H.G. Sol, eds., Processes and Tools for Decision Support (North Holland, 1983).

[7] CRI, The CRI Directory of Expert Systems (Learned Information, Oxford, 1986).

[8] S. De, Integrated Problem Solving in Manufacturing, in: L.F. Pau, Ed., Artificial Intelligence in Economics and Management (North Holland, 1986).

[9] S. De, Providing Effective Decision Support: Modelling Users and their Requirements, Decision Support Systems, Vol. 2 (1986) 309–319.

[10] G.I. Doukidis, An Anthology on the Homology of Simulation with Artificial Intelligence, The Journal of the Operational Research Society, Vol. 38, No. 8 (1987) 701–712.

[11] G.I. Doukidis, F. Land and G. Miller (eds), Knowledge-based Management Support Systems (Ellis-Horwood Publishers, 1988).

[12] M.S. Fox, Knowledge Representation for Decision Support Systems, in: R.H. Sprague et al., Eds., Knowledge Representation for Decision Support (North Holland, 1985).

[13] M. Goul, On Building Expert Systems For Strategic Planners: A Knowledge Engineering Experience, Information and Management (March, 1987).

[14] P.C. Hamphreys, Intelligence in Decision Support, in: B. Brehmer et al., eds., New Directions in Research on Decision Making (North-Holland, 1986).

[15] P.G.M. Keen and M.S. Scott-Morton, Decision Support Systems, (Addison Wesley, 1978).

[16] H.A. Kurstedt, Responsive Decision Support Systems: A Board View Illustrates when to include Expert Systems, in: H.G. Sol, et al., eds., Expert systems and artificial Intelligence in Decision Support Systems (Reidel Publishers, 1987).

[17] O.I. Larichev, Problems of Man-Machine Interaction in Decisions Support Systems, in: L.B. Methlie and R.H. Sprague, eds., Knowledge Representation for Decision Support Systems (North-Holland, 1985).

[18] M.R. Lee, Epistemological Aspects of Knowledge-Based Decision Support System, in: H.G. Sol, ed., Processes and Tools for Decision Support (North-Holland, 1983).

[19] E. Mumford, Managing Complexity: The Design and Implementation of Expert Systems, in: G.I. Doukidis, F. Land and G. Miller, eds., Knowledge Based Management Support Systems (Ellis Horwood, forthcoming 1988).

[20] S. Nagel and J. Long, P/G% ANALYSIS: A Decision Aiding Program, in: L.F. Pau, ed., Artificial Intelligence in Economics and Management (North Holland, 1986).

[21] R. Pfeifer and H.J. Luthi, Decision Support Systems and Expert System: A C Oplementary Relationship, H.G. Sol et al., eds., Expert systems and Artificial Intelligence in Decision Support Systems (Reidel Publishers, 1987).

[22] W.B. Rauch-Hindin, Artificial Intelligence in Business, Science and Industry: Volume 2 – Applications (Prentice Hall, 1985).

[23] R. Sprague and E. Carlson, Building Effective Decision Support Systems (Prentice Hall, 1982).

[24] H. Simon, The New Science of Management Decision (Harper & Row, New York, 1960).

[25] R. Sprague, DSS in Context, in: E.R. McLean and H.G. Sol, eds., Decision Support Systems: A Decade in Perspective (IFIP, 1986).

[26] C.B. Stabell, Decision Support Systems: Alternatives Perspectives and Schools, in: E.R. McLean and H.G. Sol, eds., Decision Support Systems: A Decade in Perspective (IFIP, 1986).

[27] E. Turban, Decision Support and Expert Systems: Managerial Perspectives (Macmillan Publishers, 1988).

[28] G.R. Wagner, Decision Support System: The Real Substance, Interfaces (April, 1981).
