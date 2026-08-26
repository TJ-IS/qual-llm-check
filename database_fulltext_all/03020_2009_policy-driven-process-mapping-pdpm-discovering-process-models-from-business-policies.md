---
otero_id: 3020
otero_key: "VR4WTDKQ"
title: "Policy-Driven Process Mapping (PDPM): Discovering process models from business policies"
authors: "Harry Jiannan Wang; J. Leon Zhao; Liang-Jie Zhang"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.08.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Policy-Driven Process Mapping (PDPM): Discovering process models from business policies

Harry Jiannan Wang <sup>a,</sup>⁎, J. Leon Zhao <sup>b</sup>, Liang-Jie Zhang <sup>c</sup>

<sup>a</sup> Department of Accounting and MIS, University of Delaware, Newark, DE, United States

<sup>b</sup> Department of Information Systems, City University of Hong Kong, Kowloon, Hong Kong, China

<sup>c</sup> IBM Research, Hawthorne, NY, United States

## a r t i c l e i n f o

Article history: Received 17 November 2008 Received in revised form 7 August 2009 Accepted 30 August 2009 Available online 6 September 2009

Keywords: Process mapping Business policy Process design Business process management

## a b s t r a c t

Analyzing business policies for discovering and validating business process models is a critical task in modern organizations, which is currently done in an ad hoc manner due to a lack of systematic methodologies. In this paper, we propose a novel methodology called Policy-Driven Process Mapping (PDPM) for extracting process models from business policy documents. Our research objective is to make process discovery from policy documents more systematic with fewer structural and semantic errors. To the best of our knowledge, PDPM is the <sup>fi</sup>rst formal approach to discovering process models from business policies.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Business policies enable the ef<sup>fi</sup>cient management of an organization by de<sup>fi</sup>ning the procedures and rules for its daily business operations [28]. Many of these business policies are used to specify some business processes, such as order ful<sup>fi</sup>llment, product development, travel reimbursement, and cash handling. We refer to these business policies as process policies. For instance, a travel reimbursement policy may de<sup>fi</sup>ne that a reasonable exception request form must be submitted if a travel reimbursement form is submitted later than 60 days after completing the travel. This policy speci<sup>fi</sup>es the condition under which a submission task must be executed. In order to describe a business process, a great number of process policies need to be established.

Although process policies are in place in many organizations, they often do not completely match the processes actually conducted in the <sup>fi</sup>eld due to imprecise, ambiguous, or incomplete process policies, and failure to update the policies as processes change [10]. Recently, many organizations have invested a great amount to revamp their business policies in order to comply with various regulatory requirements, such as Sarbanes–Oxley [7,9]. At the same time, organizations also need to adapt their business processes to meet the various changes in the business environment to maintain competitive advantages. Those changes further escalate their incompatibility, which may lead to problems such as miscommunication between the management and employees, misunderstanding of enterprise processes across different functions, and potential internal control de<sup>fi</sup>ciencies [7,12]. As such, discovering new process models from and validating existing process models with business policies are critical issues for modern organizations.

Process mapping has been adopted in companies as an effective technique to enable organizations to view their business system graphically at any level of detail and complexity [24]. Although many process mapping projects have successfully helped organizations achieve higher level of cross-functional collaborations and tangible cost reduction, traditional process mapping has been done in an ad hoc manner and tends to be resource-intensive and time-consuming due to the informal and ambiguous collection of process information [17,29]. Different from the traditional process mapping approach, there has been research on applying formal methods and theories, such as linear programming [1], cost optimization [38], computational experiments [16], and probability theory [11], to generate process models. Although those analytical process mapping methods provide rigorous process extraction procedures, few applications of those approaches have been found due to their restrictive assumptions. In addition, none of those analytical approaches use business policies as their inputs, and therefore they cannot be directly applied to process discovery based on business policies. Therefore, there is an imperative need for advanced process development tools that can leverage business policies for process discovery and validation.

In this paper, we respond to this need by proposing an innovative methodology for systematic process model mapping from business policies, which we refer to as Policy-Driven Process Mapping (PDPM). As shown in Fig. 1, PDPM builds on both traditional and analytical process design methods and advocates a new way of discovering process models. More speci<sup>fi</sup>cally, PDPM uses business policies as the inputs for process discovery and provides systematic guidelines for business analysts to ef<sup>fi</sup>ciently leverage policy documents. To the best of our knowledge, this is the <sup>fi</sup>rst systematic approach to the discovery of process models from business policies.

The rest of this paper proceeds as follows. In the next section, we present a case on travel reimbursement policies, which provides a conceptual foundation of our Policy-Driven Process Mapping (PDPM) approach. Then, we formalize the concepts of process policy and process map and discuss the details of PDPM procedure in Section 3. The PDPM approach is further demonstrated and validated in Section 4 via another case study and a prototype system. Related work is discussed in Section 5. Finally, we summarize our contributions and present our future research.

## 2. A case study on business process policies

In this section, we present a case study on the business policies for a major public university in the US and discuss the conceptual foundations of our Policy-Driven Process Mapping (PDPM) methodology. The business policy manual for the university is published online and is accessible to the public. The policy manual has nineteen sections covering various topics, such as accounting, <sup>fi</sup>nance, information systems, etc. For our case study, we focus on the “Travel Regulations” section, because travel approval and reimbursement processes are implemented in most organizations and are therefore representative. Furthermore, travel regulation processes involve many tasks, data items, resources and constraints, which make the corresponding process model non-trivial.

Travel policies in this case include several pages of documents. Due to the space limit, we simpli<sup>fi</sup>ed these documents into twelve policies as shown in Table 1. In real-world applications, this simpli<sup>fi</sup>cation process is not necessary and the original policies can be directly analyzed using our approach [21]. Table 1 includes several types of process policies. $P _ { 1 }$ through $P _ { 6 }$ can be referred to as “control <sup>fl</sup>ow policies,” which can be used to identify individual tasks and the sequences between tasks. For instance, $P _ { 1 }$ identi<sup>fi</sup>es a task, “Submit Travel Reimbursement Form” and $P _ { 5 }$ identi<sup>fi</sup>es that the task “Issue Check” should be executed after the task “Approve Travel Reimbursement Form.” Thus, we have the following observation:

• Observation 1 (Control Flow Identification): Business policies can be used to identify tasks and the sequences between tasks, i.e., the control flow.

We further found that business process policies can also be used to identify data items and the dependencies between data items. For example, as discussed in the previous paragraph, the two tasks “Issue Check” and “Approve Travel Reimbursement Form” are identi<sup>fi</sup>ed in a control <sup>fl</sup>ow policy, where the two data items “Check” and “Travel Reimbursement Form” can also be identi<sup>fi</sup>ed. In addition, that policy also implies a data dependency between “Check” and “Travel Reimbursement Form,” where a reimbursement check cannot be created before a travel reimbursement form is submitted. Intuitively, a task that produces a data item must be executed before all tasks that consume the same data item, which leads to our second observation:

![](/api/attachments/VR4WTDKQ/fulltext/images/579a92e414b7e451555c5ef29a003154f05c4f5dca9bdd05ac8a2ba6a9f69e1e.jpg)  
Fig. 1. Process mapping approaches.

Travel regulation policies from the business policy manual.

<table><tr><td>P1: All claims for the reimbursement of expenses for an approved university business travel are made on a Travel Reimbursement Form (TRF).</td></tr><tr><td>P2: If Travel Reimbursement Form (TRF) is submitted later than 60 days after completing the travel, a Reasonable Exception Request Form (RERF) must be submitted.</td></tr><tr><td>P3: If reasonable exception request is not approved, then the reimbursement amount will be taxable.</td></tr><tr><td>P4: If reimbursement amount (RA) exceeds the limit, a Travel Exception Form (TEF) must be filled.</td></tr><tr><td>P5: After the Travel Reimbursement Form (TRF) is approved, a check will be issued.</td></tr><tr><td>P6: If the quarterly travel exception review is denied, the reimbursed amount must be refunded.</td></tr><tr><td>P7: Department or unit head must approve the travel.</td></tr><tr><td>P8: Department or unit head must approve the reasonable exception.</td></tr><tr><td>P9: Disbursement Services Center (DSC) must review the reimbursement form.</td></tr><tr><td>P10: The Office of Business and Financial Services (OBFS) reviews the travel exception form.</td></tr><tr><td>P11: Higher Education Travel Control Board (HETC) reviews the travel exceptions quarterly.</td></tr><tr><td>P12: Bursar&#x27;s office (BO) is responsible to issue reimbursement check.</td></tr></table>

• Observation 2 (Data Flow Constraints): Business policies can be used to identify data items and the dependencies between data items, which constrain the execution order of tasks.

We also <sup>fi</sup>nd that some process policies explicitly de<sup>fi</sup>ne routing rules, which govern the execution order of tasks. For example, $P _ { 4 }$ speci<sup>fi</sup>es a routing rule, i.e. task “submit TEF” can be activated only when the condition, i.e. “the reimbursement amount exceeds the limit,” is true. Routing rule policies are often in the form of ‘if–then’ sentences, which can be used to imply control <sup>fl</sup>ow sequences. The rule of thumb is that if the condition clause contains a task $t _ { 1 }$ and the conclusion clause contains a task $t _ { 2 } , t _ { 1 }$ is executed before $t _ { 2 } .$ . Therefore, our third observation is as follow:

• Observation 3 (Routing Rules): Business policies can be used to identify process routing rules, which govern the execution order of tasks.

The three seemingly simple observations above are actually quite powerful since they indicate the possibility of extracting control <sup>fl</sup>ow models from narrative business policies. During the case study, we also found policies that are related to process models but cannot be used to derive control <sup>fl</sup>ows. For instance, some policies de<sup>fi</sup>ne various non-reimbursement expenses that are data items used in reimbursement approval tasks; other policies specify exception handling constraints, e.g., “if the dean will not be able to sign the form within two weeks, the vice dean is authorized to sign on his behalf.” To better classify process policies and facilitate their identi<sup>fi</sup>cation from nonprocess policies, a process policy taxonomy is built based on the case study as shown in Fig. 2. In particular, given that a process model consists of four major components, namely, control <sup>fl</sup>ow, data <sup>fl</sup>ow, organizational model, and constraints, the taxonomy contains four categories corresponding to those components [4,25,26,40]. We believe that the process policy taxonomy is useful for classifying most commonly used process policies and can also be extended to include more speci<sup>fi</sup>c policy types.

In this study, we are interested in developing a method to systematically discover process models from narrative process policies. In particular, given the three observations and the taxonomy, process policies of the following types are most useful for process extraction: task identi<sup>fi</sup>cation, task sequence, data dependency, and routing rule. So far, process policies such as the ones shown in Table 1 are not precisely represented and therefore cannot be formally analyzed. In the next section, we formalize process policies and process map based on the observations presented in this section and develop a policy-driven process mapping methodology.

![](/api/attachments/VR4WTDKQ/fulltext/images/c75be45d6ca3535877e60386c1ba780fa659ec013439d527c53a9297483c11d0.jpg)  
Fig. 2. Process policy taxonomy.

## 3. Policy-Driven Process Mapping methodology

In this section, we propose a Policy-Driven Process Mapping (PDPM) methodology to systematically construct process models from narrative process policies. We <sup>fi</sup>rst give the de<sup>fi</sup>nitions of process policy and process map. Then, we present a detailed PDPM procedure with mapping rules and algorithms. The travel reimbursement example is used throughout this section to illustrate the PDPM approach.

## 3.1. Formal definitions of process policy and process map

In Section 1, we describe process policies as business policies that de<sup>fi</sup>ne and constrain some aspects of business processes. We further analyze process policies by classifying them according to the process policy taxonomy presented in Section 2. In particular, we study process policies from four perspectives, namely, control <sup>fl</sup>ow, data <sup>fl</sup>ow, organizational model, and process constraints as commonly found in well-known process modeling paradigms, such as Work<sup>fl</sup>ow Management Coalition Notation [40], UML [25], and BPMN [26]. Based on the observations in the case study in Section 2, we formally de<sup>fi</sup>ne process policies as follows:

## De<sup>fi</sup>nition 1. Process policy

Let P be a <sup>fi</sup>nite set of process policies, $P = \{ p _ { 1 } , p _ { 2 } , . . . , p _ { n } \}$ . We de<sup>fi</sup>ne a process policy $p _ { i } \in P .$ as an 8-tuple: $p _ { i } { = } { < } p i d _ { i } , D _ { i } , T _ { i } , R _ { i } , C _ { i } , T S _ { i }$ $T R _ { i } , T D _ { i } >$ , where

• pid is the process policy ID, which is unique in order to identify the policy and $\forall p _ { i } , p _ { j } \in P , i \neq j , p i d _ { i } \neq p i d _ { j }$

$D _ { i } { = } \{ d _ { 1 } ^ { i } , ~ d _ { 2 } ^ { i } { , . . . , ~ d _ { m } ^ { i } } \}$ is the set of data items identi<sup>fi</sup>ed from p . $D = D _ { 1 } \cup D _ { 2 } \cup . . . , \cup D _ { n }$ is the set of all data items identi<sup>fi</sup>ed from P.

$T _ { i } = \{ t _ { 1 } ^ { i } , t _ { 2 } ^ { i } , . . . ,$ t<sup>i</sup>} is the set of tasks identi<sup>fi</sup>ed from $p _ { i \cdot } T { = } T _ { 1 } \cup T _ { 2 } \cup \ldots ,$ $\cup T _ { n }$ is the set of all tasks identi<sup>fi</sup>ed from P.

$R _ { i } { = } \{ r _ { 1 } ^ { i } , r _ { 2 } ^ { i } { , } { \ldots } , r _ { t } ^ { i } \}$ is the set of resources involved in p . We borrow resource de<sup>fi</sup>nition from work<sup>fl</sup>ow resource pattern research, whereas a resource is de<sup>fi</sup>ned as “an entity that is capable doing work…[,which] is classi<sup>fi</sup>ed as either human or non-human $\left[ 3 0 \right] . "$ $R = R _ { 1 } \cup R _ { 2 } \cup . . . , \cup R _ { n }$ is the set of all resources involved in P.

$C _ { i } = \{ c _ { 1 } ^ { i } , c _ { 2 } ^ { i } , . . . , c _ { k } ^ { i } \}$ is the set of routing constraints de<sup>fi</sup>ned in p , c<sup>i</sup> is either an expression or a statement that returns a Boolean value. $C { = } C _ { 1 } \cup C _ { 2 } \cup . . . , \cup C _ { n }$ is the set of all routing constraints de<sup>fi</sup>ned in P.

$T S _ { i } = T _ { i } \times T _ { j } \times C _ { k } = \{ ( t _ { a } ^ { i } , t _ { b } ^ { i } , c _ { c } ^ { i } ) \colon t _ { i } ^ $ <sub>a</sub><sup>i</sup> is executed before t<sub>b</sub><sup>i</sup> when c<sub>c</sub><sup>i</sup> is true} is the set of task sequences identi<sup>fi</sup>ed from p $\scriptstyle : { \cal { T S } } = { \cal { T S } } _ { 1 } \cup { \cal { T S } } _ { 2 } \cup . . . , \cup { \cal { T S } } _ { n }$ is the set of all task sequences identi<sup>fi</sup>ed from P.

$\bullet \ : T D _ { i } = T _ { i } \times D _ { i } \times O = \{ ( t _ { l } ^ { i } , \ : d _ { m } ^ { i } , \ : o ^ { i } ) \colon$ t<sub>l</sub><sup>i</sup> conducts an operation $o ^ { i }$ on $d _ { m } ^ { i } \big \}$ is the set of task–data relationships identi<sup>fi</sup>ed from $p _ { i } ,$ where $o ^ { i } \in { \cal O } =$ {r, w}, r represents read operation and w represents write operation. $T D = T D _ { 1 } \cup T D _ { 2 } \cup . . . , \cup T D _ { n }$ is the set of all task–data relationships identified from P.

$T R _ { i } = T _ { i } \times R _ { i } = \{ ( t _ { l } ^ { i } , r _ { k } ^ { i } ) \colon t _ { l } ^ { i }$ is executed by $r _ { k } ^ { i } \big \}$ is the set of task–resource relationships identi<sup>fi</sup>ed from $p _ { i } . \ T R = T R _ { 1 } \cup T R _ { 2 } \cup . . . , \cup T R _ { n }$

De<sup>fi</sup>nition 1 provides a formal template for parsing unstructured process policies into structured and unambiguous information on process models. For instance, if a travel reimbursement policy states “If Travel Reimbursement Form is submitted later than 60 days after completing the travel, a Reasonable Exception Request Form must be submitted,” De<sup>fi</sup>nition 1 provides the mechanisms to parse this policy as follows. We assign 1 as the ID for this policy, i.e., $p i d = 1 . { \mathrm { T h e n } }$ , two data items can be identi<sup>fi</sup>ed: $d _ { 1 } ^ { 1 } = " T r a v e$ l Reimbursement Form (TRF)” and $d _ { 2 } ^ { 1 } = " .$ “Reasonable Exception Request From $( R E R F ) ; \ "$ two tasks can be extracted: $t _ { 1 } ^ { 1 } = \ " S u b m i t \ T R F "$ and $t _ { 2 } ^ { 1 } = " S u b m i t R E R F ; "$ and there is one constraint: $c _ { 1 } ^ { 1 } = { } ^ { \ast } T R F$ submission later than 60 days after completing the travel.” Furthermore, we know that if c<sup>1</sup> is true, then t<sup>1</sup> is executed after t<sup>1</sup>, therefore de<sup>fi</sup>ning a task sequence relationship (t<sup>1</sup>, $t _ { 2 } ^ { 1 } , c _ { 1 } ^ { 1 } )$

Similarly, we can identify that d<sup>1</sup> is the output for t<sup>1</sup> and d<sup>1</sup> is the output for t<sup>1</sup>. According to De<sup>fi</sup>nition 1, this policy can be expressed as $p _ { 1 } = < 1 , \{ d _ { 1 } ^ { 1 } , d _ { 2 } ^ { 1 } \} , \{ t _ { 1 } ^ { 1 } , t _ { 2 } ^ { \bar { 1 } } \} , \emptyset , \{ c _ { 1 } ^ { 1 } \} , \{ ( t _ { 1 } ^ { 1 } , t _ { 2 } ^ { 1 } , c _ { 1 } ^ { 1 } ) \} , \{ ( t _ { 1 } ^ { 1 } , d _ { 1 } ^ { 1 } , w ) , ( \bar { t } _ { 2 } ^ { 1 } , d _ { 2 } ^ { 1 } , w ) \}$ Ø>. Note that because no resources can be identi<sup>fi</sup>ed from this policy, the corresponding sets are empty. Note that each of these policies can be formalized and stored in a knowledge base for systematic process analysis.

Based on De<sup>fi</sup>nition 1, the narrative process policies synthesized from the case study (see Table 1) can be formalized as shown in Table 2. The corresponding process elements, including 5 data items, 11 tasks, 6 resources and 5 process constraints, are also summarized in Table 2. Given the formalized process policies, a computational procedure will be developed in this paper to extract process models systematically. We refer to a process model as a process map, which is essentially a directed graph with speci<sup>fi</sup>c properties designed to simplify and facilitate policy-driven process mapping.

Table 2  
Formalized travel reimbursement process policies.

<table><tr><td>PID</td><td>Data items</td><td>Tasks</td><td>Resources</td><td>Constraints</td><td>Task sequences</td><td>Task–resource relationship</td><td>Task–data relationship</td></tr><tr><td>1</td><td> $d_1$ </td><td> $t_1$ </td><td> $r_1$ </td><td>NA</td><td>NA</td><td> $(t_1, r_1)$ </td><td> $(t_1, d_1, w)$ </td></tr><tr><td>2</td><td> $d_1, d_2$ </td><td> $t_1, t_2$ </td><td>NA</td><td> $c_1$ </td><td> $(t_1, t_2, c_1)$ </td><td> $(t_2, r_1)$ </td><td> $(t_2, d_2, w)$ </td></tr><tr><td>3</td><td> $d_2, d_3$ </td><td> $t_3, t_4$ </td><td>NA</td><td> $c_2$ </td><td> $(t_3, t_4, c_2)$ </td><td>NA</td><td> $(t_3, d_2, r)$ </td></tr><tr><td>4</td><td> $d_3, d_4$ </td><td> $t_5$ </td><td>NA</td><td> $c_3$ </td><td>(null,  $t_5, c_3$ )</td><td> $(t_5, r_1)$ </td><td> $(t_5, d_4, w)$ </td></tr><tr><td>5</td><td> $d_1, d_5$ </td><td> $t_6, t_7$ </td><td>NA</td><td> $c_4$ </td><td> $(t_6, t_7, c_4)$ </td><td>NA</td><td> $(t_6, d_1, r), (t_7, d_5, w)$ </td></tr><tr><td>6</td><td> $d_4, d_5$ </td><td> $t_8, t_9$ </td><td>NA</td><td> $c_5$ </td><td> $(t_8, t_9, c_5)$ </td><td> $(t_9, r_1)$ </td><td> $(t_8, d_4, r), (t_9, d_5, r)$ </td></tr><tr><td>7</td><td> $d_1$ </td><td> $t_6$ </td><td> $r_2$ </td><td>NA</td><td>NA</td><td> $(t_6, r_2)$ </td><td>NA</td></tr><tr><td>8</td><td> $d_2$ </td><td> $t_3$ </td><td>NA</td><td>NA</td><td>NA</td><td> $(t_3, r_2)$ </td><td>NA</td></tr><tr><td>9</td><td> $d_1$ </td><td> $t_{10}$ </td><td> $r_3$ </td><td>NA</td><td>NA</td><td> $(t_{10}, r_3)$ </td><td>NA</td></tr><tr><td>10</td><td> $d_4$ </td><td> $t_{11}$ </td><td> $r_4$ </td><td>NA</td><td>NA</td><td> $(t_{11}, r_4)$ </td><td>NA</td></tr><tr><td>11</td><td> $d_4$ </td><td> $t_8$ </td><td> $r_5$ </td><td>NA</td><td>NA</td><td> $(t_{12}, r_5)$ </td><td>NA</td></tr><tr><td>12</td><td> $d_5$ </td><td> $t_7$ </td><td> $r_6$ </td><td>NA</td><td>NA</td><td> $(t_7, r_6)$ </td><td>NA</td></tr></table>

Data Items: d<sub>1</sub>: Travel Reimbursement Form (TRF); d<sub>2</sub>: Reasonable Exception Request Form (RERF); d<sub>3</sub>: Reimbursement Amount (RA); d<sub>4</sub>: Travel Exception Form $( \mathrm { T E F } ) ; d _ { 5 } \colon$ Check. Tasks: t : Submit TRF; t : Submit RERF; t : Approve RERF; t : Make RA taxable; $t _ { 5 } { \mathrm { : } }$ Submit TEF; $t _ { 6 } { : }$ Approve TRF; t : Issue Check; $t _ { 8 } { \mathrm { : } }$ Review TEF quarterly; $t _ { 9 } { \mathrm { : } }$ Refund Check; $t _ { 1 0 } \colon$ Review TRF; $t _ { 1 1 } { : }$ Review TEF.  
Resources: $r _ { 1 } :$ Traveler; r : Department Head; $r _ { 3 } \colon$ Disbursement Services Center $( \mathrm { D S C } ) ; r _ { 4 } \colon$ Of<sup>fi</sup>ce of Business and Financial Services (OBFS); $r _ { 5 } \colon$ Higher Education Travel Control Board (HETC); $, r _ { 6 } { \mathrm { : } }$ Bursar's of<sup>fi</sup>ce (BO).  
Constraints: $c _ { 1 } { : }$ TRF is submitted later than 60 days after completing the travel; c : RERF is not approved; $c _ { 3 } \colon$ Reimbursement Amount exceeds the limit; $c _ { 4 } { \mathrm { : } }$ TRF is approved; $c _ { 5 } \mathrm { : }$ TEF quarterly review is not passed.

The process map is de<sup>fi</sup>ned as follows:

## De<sup>fi</sup>nition 2. Process map

Given a set of process policies $P = < D , \ T , \ R , \ C , \ T S , \ T D , \ T R > , \ a$ process map G based on P is de<sup>fi</sup>ned as a directed graph $G = < V , E >$ where:

$V = V _ { t } \cup V _ { c } \cup \{ s , e \} . \ : V _ { t }$ is the set of task vertices where $\forall v _ { t } \in V _ { t } , v _ { t } \in T ,$ − $\cdot ( \nu _ { t } ) \geq 1 , d ^ { + } ( \nu _ { t } ) = 1$ . Further, d<sup>−</sup>(v ) and $d ^ { + } ( \nu _ { t } )$ are the in-degree and out-degree of $\displaystyle \boldsymbol { v } _ { t }$ respectively; V is the set of decision vertices where $\forall \nu _ { c } \in V _ { c } , d ^ { - } ( \nu _ { c } ) \geq 1 , d ^ { + } ( \nu _ { c } ) = 2 ;$ s and e are the start and end vertices, respectively where $d ^ { - } ( s ) = 0 , d ^ { + } ( s ) = 1 , d ^ { - } ( e ) \geq 1 , d ^ { + } ( e ) = 0 .$ $E \subseteq V \times V$ is the set of directed edges among vertices in V.

De<sup>fi</sup>nition 2 implies some simplifying assumptions we make about the process map structure:

1) Tasks are executed sequentially. Parallelism is ignored at this stage to simplify the discovery of process models since it does not affect the correctness of the models and can be reintroduced later to improve process performance [38].

2) Each decision vertex has two and only two outgoing edges, which means that each decision vertex is an exclusive OR and its value is a Boolean value returned by the corresponding process constraint. It has been shown that an OR vertex can always be converted to a set of exclusive OR vertices [6].

3) The start node and every task can have one and only one outgoing edge. This does not restrict the model at all since multiple paths can be modeled by means of decision vertices.

4) Tasks, decision vertices, and the end node must have at least one incoming edge, which prevents dangling tasks/decision points and processes without terminations.

These assumptions help simplify the discovery of process models tremendously without affecting the correctness of the derived models. Given that our approach is the <sup>fi</sup>rst attempt to discover process models from business policies, it is important to focus on the core issues of our approach without being bogged down by unnecessary complications. For example, without considering parallel task executions, we can not only greatly simplify the process map by considering only one routing construct, i.e. decision vertex, but also avoid handling potential control <sup>fl</sup>ow anomalies caused by parallelism, such as deadlock and lack of synchronization [36,37]. As a follow-up step, optimization methods [13] can be applied to improve the ef<sup>fi</sup>ciency of a given business process model.

In addition, De<sup>fi</sup>nition 2 also provides the criteria for the syntactical correctness of a process map, which can be used to re<sup>fi</sup>ne the preliminary process models extracted from business policies. For instance, a process map that has a task with two outgoing edges is syntactically wrong because it is not clear which edge should be activated after the task completes. Note that these assumptions may lead to unstructured processes in terms of improper nesting and mismatched split–join pairs as discussed in [22], which can result in process map structural <sup>fl</sup>aws. In this study, we focus on the process mapping methodology and leave a thorough treatment on process model veri<sup>fi</sup>cation to future research. Next, we present a detailed procedure for extracting process models from process policies.

## 3.2. Policy-Driven Process Mapping procedure

Fig. 3 shows the procedure to extract a process map from the formalized process policies. We propose a set of new concepts to facilitate the extraction procedure, namely, task view, data view, structural constraints, and domain constraints. Each step of the procedure is discussed in detail next.

![](/api/attachments/VR4WTDKQ/fulltext/images/80ad30af9f9faeaa916c2a514a11480d3f96e3075c1e9d424d8944ce99358caf.jpg)  
Fig. 3. PDPM procedure.

```txt
Algorithm for drafting process map based on task view.

Algorithm 1:
Input:
a. initial process map G=<V, E>, where V=V_t ∪ V_c ∪ {s, e}, V_t=∅, V_c=∅, E=∅
b. the set of tasks identified from policies T={t_1, t_2,..., t_n}
c. the set of routing constraints identified from policies C={c_1, c_2,..., c_m}
d. task view TV, where tv_ij i=1, 2,..., n+m+1, j=1, 2,..., n+m+1
Output: first-cut process map G'
begin
for each t_n ∈ T, insert v_t^n to V_t//add task vertices
for each c_m ∈ C, insert v_c^m to V_c//add decision vertices
for each tv_ij ∈ TV//add arcs among tasks and decision points based on task view
if tv_ij = 1, i<n, j<n, then add (v_t^i, v_t^j) to E
if tv_ij = 1, n<i<n+m, j<n, then add (v_c^{i-n}, v_t^j) to E
if tv_ij = 1, i<n, n<j<n+m, then add (v_t^i, v_c^j) to E
if tv_ij = 1, n<i<n+m, n<j<n+m, then add (v_c^i, v_c^j) to E
end for
V' = V
E' = E
G' = <V', E'>
end
```

## 3.2.1. Step 1: Draft process map based on task view

According to Observations 1 and 3 in Section 2, task sequences and routing rules can be identi<sup>fi</sup>ed directly from business policies, which can help draft a <sup>fi</sup>rst-cut process map. For the formalized process policies, task sequences are represented as set $T S = T \times T \times C = \{ ( t _ { a } , t _ { b } , c ) \colon t _ { a }$ is executed before $t _ { b }$ when c is true}. Each distinct task $t _ { i } \in T$ is mapped into a task vertex $\boldsymbol { v } _ { t } ^ { i } { \in } V _ { t }$ and each distinct routing constraint $c _ { j } \in C$ is mapped into a decision vertex $\nu _ { c } ^ { j } \in V _ { c }$ . Task view is formally de<sup>fi</sup>ned as the following:

## De<sup>fi</sup>nition 3. Task view

Given $V _ { t } { = } \{ \nu _ { t } ^ { 1 } , \nu _ { t } ^ { 2 } { , } . . . , \nu _ { t } ^ { n } \}$ is the set of identi<sup>fi</sup>ed task vertices and $V _ { c } { = } \{ \nu _ { c } ^ { 1 } { , } \nu _ { c } ^ { 2 } { , } { \ldots } , \nu _ { c } ^ { m } \}$ is the set of identi<sup>fi</sup>ed decision vertices. A task view TV is de<sup>fi</sup>ned as a $( n + m + 1 )$ -square matrix, whose rows and columns correspond to the set $V _ { t } \cup V _ { c } \cup \{ s \}$ and $V _ { t } \cup V _ { c } \cup \{ e \}$ where s is the start node and e is the end node. $t v _ { i j } = 1$ if the corresponding task, decision, or start/end nodes are connected according to TS, otherwise $t v _ { i j } = 0$

Given the initial process map G, which is an empty graph, and task view TV, the algorithm shown in Table 3 is used to draft the process map. Based on the task view, a preliminary process map can be easily drafted. For instance, a TV matrix with three task vertices and two decision vertices is mapped into a draft process map in Fig. 4, where the four $" 1 " s$ are mapped into the four control <sup>fl</sup>ow links.

By applying Step 1 to the formalized travel reimbursement policies in Table 2, a draft process map can be extracted as shown in Fig. 5. Note that we choose UML activity diagrams to represent the process map in this paper, which can be replaced by any other graphical notations that can model the process components in De<sup>fi</sup>nition 2.

The process map shown in Fig. 5 is derived from the process information found in the policies. Although this map already provides some tasks and task sequences embedded in the policy documents, many tasks are still not connected. This situation leads to the following observation:

• Observation 4 (Process Map Enhancement): A given set of process policies may not be comprehensive enough to specify the entire business process explicitly and additional enhancements and refinements are needed to complete the process map.

As noted in Observation 2, the data <sup>fl</sup>ow constraints in process policies can imply control <sup>fl</sup>ow information, which are used next to enhance the process map as discussed in Step 2.

## 3.2.2. Step 2: Enhance the process map based on data view

In this step, the draft process map G' is enhanced by means of the identi<sup>fi</sup>ed task–data relationship TD, which indicates additional task sequences due to data dependency. A data view can be constructed as follows:

![](/api/attachments/VR4WTDKQ/fulltext/images/5c8b906ec05bda01383cfae9d8dc606af5888935afe6b46170c2761e795d0c3d.jpg)  
Fig. 4. Drafting process map based on task view.

## De<sup>fi</sup>nition 4. Data view

Given $V _ { t } { = } \{ \nu _ { t } ^ { 1 } , \nu _ { t } ^ { 2 } , { \ldots } , \nu _ { t } ^ { n } \}$ is the set of identi<sup>fi</sup>ed task vertices and $D = \{ d _ { 1 } , d _ { 2 } , . . . , d _ { k } \}$ is the set of identi<sup>fi</sup>ed data items. A data view DV is an n×k matrix whose rows correspond to the set $V _ { t }$ and whose columns correspond to the set $D . d \nu _ { i j } = w \mathrm { i f } \exists ( t _ { i } , d _ { j } , w ) \in T D . d \nu _ { i j } = r$ If $\exists ( t _ { i } , d _ { j } , r ) \in T D _ { \mathrm { \Omega } }$ , otherwise $d \nu _ { i j } = 0$

Based on the data view, additional edges between tasks can be identi<sup>fi</sup>ed. Intuitively, if a data item d is the output of task $t _ { 1 }$ and the input of $t _ { 2 } ,$ then an edge $\left( t _ { 1 } , \ t _ { 2 } \right)$ should be added. Formally, the algorithm shown in Table 4 is used to enhance process map $G ^ { \prime }$ with data view. For example, Fig. 6 shows how the draft process map in Fig. 4 can be enhanced using a data view. Note that the dashed lines are the added control <sup>fl</sup>ow links based on the data view matrix.

Based on the identi<sup>fi</sup>ed task–data relationships in Table 2, a data view can be constructed for the travel reimbursement process as shown in Table 5. Then, a new travel reimbursement process map with more control <sup>fl</sup>ow links can be derived based on the data view as depicted in Fig. 7. Steps 1 and 2 use all available information contained, either explicitly or inexplicitly, in process policies to construct the process map. In an ideal situation where process policies are thorough and complete enough to cover every aspect of the business processes, a complete process map should be successfully extracted after Steps 1 and 2. However, as we discussed in our Observation 4, real process policies are normally incomplete and may contain ambiguities, leading to incomplete process maps. The resulting travel reimbursement process in Fig. 7 indicates such problems, e.g. task $t _ { 1 }$ has <sup>fi</sup>ve outgoing links, task $t _ { 1 0 }$ has no outgoing link, and all decision vertices only have one outgoing link.

Additional re<sup>fi</sup>nements must be performed to make the process map more complete. These re<sup>fi</sup>nements can be done by process analysts by replying on their domain knowledge, which is often an ad hoc procedure. In this paper, we aim to make this procedure more systematic by enforcing some structural constraints as speci<sup>fi</sup>ed in the formal process map de<sup>fi</sup>nition, i.e. De<sup>fi</sup>nition 2, which is discussed next.

## 3.2.3. Step 3: Apply structural constraints

The previous two steps try to get as much information on the process map as possible by adding edges among task and decision vertices, which may result in a process map that does not conform to the process map de<sup>fi</sup>nition speci<sup>fi</sup>ed in De<sup>fi</sup>nition 2. Such process maps are usually not well organized and contain ambiguities. Thus, we say a process map is syntactically correct if it satis<sup>fi</sup>es all process map structure properties de<sup>fi</sup>ned in De<sup>fi</sup>nition 2, which gives us Observation 5 and is formally speci<sup>fi</sup>ed in De<sup>fi</sup>nition 5.

![](/api/attachments/VR4WTDKQ/fulltext/images/75803ac69ffc9110d01d30e59e661cbcd243c2c49cd1ed1c422ebb8093a726d7.jpg)  
Fig. 5. Travel reimbursement process map based on task sequences.

• Observation 5 (Use of Structural Constraints): The process map resulting from the task view and data view may not be structurally correct and needs to be revised by means of structural constraints.

## De<sup>fi</sup>nition 5. Syntactical correctness of process map

Given the task view TV of enhanced process map $G ^ { \prime \prime } { = } { < } V ^ { \prime \prime } , E ^ { \prime \prime } { > }$ where $V ^ { \prime \prime } = V _ { t } \cup V _ { c } \cup \{ s , ~ e \} , ~ V _ { t } = \{ \nu _ { t } ^ { 1 } , ~ \nu _ { t } ^ { 2 } , . . . , ~ \hat { \nu } _ { t } ^ { n } \} , ~ V _ { c } = \{ \hat { \nu _ { c } ^ { 1 } } , \nu _ { c } ^ { 2 } , . . . , ~ \nu _ { c } ^ { m } \} , ~ G ^ { m }$ is syntactically correct if and only if the following data hold:

1. ∀ $t { \nu _ { i j } } { { \in } { \cal T } } , \sum _ { \it \cdot \mathrm { ~ \sum ~ } _ { \it \cdot } } ^ { \mathrm { ~ } n \mathrm { ~ + ~ } m \mathrm { ~ + ~ } 1 } t { \nu _ { i j } } = 1 /$ /single outing edge for task vertices <sup>j=</sup> <sup>1</sup>and start node n + m + 1

2. ∀ $t \nu _ { i j } { \in } T V , \quad \sum _ { i = 1 } ^ { \cdots } \quad t \nu _ { i j } { \ge } 1 / / { \alpha } \mathrm { t }$ least one incoming edge for task vertices, decision vertices, and end node

3. ∀ $\begin{array} { l } { { t \nu _ { i j } { \in } T V , \ n { < } i { < } n + m + i , \sum _ { j = 1 } ^ { n + m + 1 } t \nu _ { i j } = 2 / } } \\ { { \ r \ { \mathrm { d e c i s i o n s } } . } } \end{array}$ /two outgoing edges fo

Definition 5 only considers process syntactical errors related to De<sup>fi</sup>nition 2, because our goal in this step is to re<sup>fi</sup>ne the process map generated by Steps 1 and 2 by removing basic process ambiguities. Other structural anomalies, such as improper use of routing constructs and subprocess anomalies [5], and related process veri<sup>fi</sup>cation are beyond the scope of this paper. In this step, the enhanced process map $G "$ is further re<sup>fi</sup>ned based on a set of structural constraints for syntactical correctness according to De<sup>fi</sup>nition 5.The enforcement of these structural constraints largely relies on the modeling experience and domain knowledge of the business analysts and thus cannot be fully automated. To help with this step, we provide some modeling techniques for applying the structural constraints as discussed next.

## Structural Constraint 1. Single task outgoing edge

If there exists tasks that have more than one outgoing edges, those edges must be merged.

Given multiple outgoing edges from a task, the following techniques can be used to achieve single task outgoing edge: a) eliminating edges that form closed control <sup>fl</sup>ow paths, b) grouping edges based on shared data items, and c) rearranging edges within each group based on domain knowledge. We use task $t _ { 1 }$ in Fig. 7 as an example to illustrate the intuition behind the techniques.

Task vertex $ { \boldsymbol { v } } _ { t } ^ { 1 }$ has <sup>fi</sup>ve outgoing edges leading to two decision vertices $ { \boldsymbol { v } } _ { c } ^ { 1 }$ and v<sup>3</sup> and three task vertices $\nu _ { t } ^ { 4 } ,$ , $\nu _ { t } ^ { 6 } ,$ and $\hat { \nu _ { t } ^ { 1 0 } }$ . After inspecting the <sup>fi</sup>ve vertices, we discover that $\nu _ { t } ^ { 4 }$ can be reached from v<sup>1</sup> by following two different paths: $ { \boldsymbol { v } } _ { t } ^ { 1 } \to  { \boldsymbol { v } } _ { t } ^ { 4 }$ and $\nu _ { t } ^ { 1 } \to \nu _ { t } ^ { 1 } \to \nu _ { c } ^ { 1 } \to \nu _ { t } ^ { 2 } \to \nu _ { t } ^ { \bar { 3 } } \to \breve { \nu } _ { t } ^ { 4 }$ , which form a closed control <sup>fl</sup>ow path from $ { \boldsymbol { v } } _ { t } ^ { 1 }$ to $\nu _ { t } ^ { 4 } .$ . Based on the semantics of the involved vertices in this closed path, it is not dif<sup>fi</sup>cult to determine that the edge from $ { \boldsymbol { v } } _ { t } ^ { 1 }$ to $\nu _ { t } ^ { 4 }$ can be eliminated because $\nu _ { t } ^ { 4 }$ must be executed after $\nu _ { t } ^ { 2 } .$ According to the data view in Table 5, we can create two groups for the rest four vertices: group 1 with v<sup>6</sup>, $\nu _ { t } ^ { 1 0 } ,$ , and $\nu _ { c } ^ { 1 } ,$ , which all read data items $d _ { 1 }$ (Travel Reimbursement Form), and group 2 with $ { \boldsymbol { v } } _ { t } ^ { 6 } ,  { \boldsymbol { v } } _ { t } ^ { 1 0 }$ , and $\nu _ { c } ^ { 3 } ,$ which all read data items $d _ { 3 }$ (Reimbursement Amount).

Then, we study the vertices within each group to determine their sequences and rearrange the edges as necessary. For the <sup>fi</sup>rst group, the task sequence should be $\overline { { \nu _ { t } ^ { 6 } } }  \nu _ { c } ^ { 1 }  \nu _ { t } ^ { 1 0 }$ , because the Travel Reimbursement Form must be approved by the department head before it can be reviewed by the University Disbursement Services Center. Therefore, we remove the edge from v<sup>1</sup> $\mathrm { t o } \ \nu _ { t } ^ { 1 0 }$ and create the edge from $\nu _ { c } ^ { 1 } \mathrm { t o } \nu _ { t } ^ { 1 0 } .$ For group two, we can determine based on the policies that the task sequence should be $\nu _ { t } ^ { 6 } \to \nu _ { c } ^ { 3 } \to \nu _ { t } ^ { 1 0 }$ . Given that we have $\nu _ { t } ^ { 6 } \to \nu _ { c } ^ { 1 } \to \nu _ { t } ^ { 1 0 }$ from the <sup>fi</sup>rst group, we can remove the edge from $ { \boldsymbol { v } } _ { t } ^ { 1 }$ to $v _ { c } ^ { 3 }$ and add edges between v<sup>1</sup> and $\nu _ { c } ^ { 3 } ,$ and $v _ { c } ^ { 3 }$ to $ { \boldsymbol { v } } _ { t } ^ { 1 0 }$ . After applying these techniques, there is only one outgoing edge for task vertex $\nu _ { t } ^ { 1 } .$ . During the case study, we found that these three techniques are very useful for enforcing Structural Constraint 1 to task vertices with many, e.g. more than three, outgoing edges. Note that these techniques can be used in any sequence and combination and may not be enough to merge all outgoing edges, in which case domain knowledge must be applied.

## Structural Constraint 2. Boolean decision outgoing edge

If a decision vertex has less than two outgoing edges, additional edges must be added. If a decision vertex has more than two outgoing edges, extra edges must be merged.

According to the process policy de<sup>fi</sup>nition, a constraint returns a Boolean value. Therefore, a decision vertex must have two and only two outgoing edges. Given that every decision vertex is derived based on a constraint, each decision vertex must have at least one outgoing edge. After applying Structural Constraint 1, some decision vertices may have two outgoing edges, such as $ { \boldsymbol { v } } _ { c } ^ { 1 }$ and $\nu _ { c } ^ { 3 } .$ . Adding edges to decision vertices relies on the domain knowledge of the business analysts. For example, an edge from $ { \boldsymbol { v } } _ { c } ^ { 5 }$ to e and an edge from $v _ { c } ^ { 4 }$ to e are added to specify that the process terminates when $c _ { 4 }$ or $c _ { 5 }$ returns a false value.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm for process map enhancement based on data view.

Algorithm 2:
Input:
    a. draft process map $G' = &lt;V', E'&gt;$
    b. the set of tasks identified from policies $V_t = \{v_t^1, v_t^2, ..., v_t^n\}$
    c. the set of data items identified from policies $D = \{d_1, d_2, ..., d_k\}$
    d. data view DV, where $dv_{ij}$ DV, $i = 1, 2, ..., n, j = 1, 2, ..., k$

Output: enhanced process map $G''$
begin
    for each $d_j, j = 1, 2, ..., k$
    initialize an output task set O, O = ∅
    initialize an input task set I, I = ∅
    for each $v_t^i, i = 1, 2, ..., n$
    if $dv_{ij} = w$ then add $v_t^i$ to O
    if $dv_{ij} = r$ then add $v_t^i$ to I
    end for
    for each $v_t^x \in O$
    for each $v_t^y \in I$
    if $(v_t^x, v_t^y) \notin E$, add $(v_t^x, v_t^y)$ to $E'$
    end for
    end for
end for
$E'' = E'$ $G'' = &lt;V', E''&gt;$
</div>

## Structural Constraint 3. No dangling vertices

There should not be any task and decision vertices without incoming or outgoing edges and the start/end node should have at least one outgoing/incoming edges.

This constraint ensures that all vertices are fully connected in the process map. Similar to Structural Constraint 2, business analysts need to manually check each dangling vertices and add edges based on his/ her domain knowledge. For example, an edge from $\nu _ { t } ^ { 4 }$ to $ { v _ { c } } ^ { 3 }$ and an edge from $\nu _ { t } ^ { 1 0 }$ to $v _ { c } ^ { 4 }$ can be added to the process map in Fig. 8.

By applying the above process map structural rules to the travel reimbursement process in Fig. 7, we get a new process map as shown in Fig. 8. Note that in this step, some edges, identi<sup>fi</sup>ed from Steps 1 and 2, have been removed. While Steps 1 and 2 can be automated by computer programs, this step still needs human intervention and cannot be fully automated because enforcing structural constraints need to take the semantics of tasks and routing constructs into consideration. The structural constraints and related modeling techniques discussed above are indispensable for generating correct process maps.

After Step 3, the process map is syntactically correct according to De<sup>fi</sup>nition 2. However, it may still contain problems. For example, $ { \boldsymbol { v } } _ { t } ^ { 7 }$ (issue the check) is linked to $ { \boldsymbol { v } } _ { t } ^ { 9 }$ (refund the check), which is logically wrong although this link is syntactically correct. We refer to those kinds of problems as Process Semantic Errors, which must be identi<sup>fi</sup>ed and corrected in the next step. We summarize the intuition in Observation 6.

• Observation 6 (Domain Constraints): The process map may contain semantic errors and needs to be reviewed by human experts and corrected based on their domain knowledge.

![](/api/attachments/VR4WTDKQ/fulltext/images/7760615bf0e35143c332603dd8b60d8f74a12919aa5953ec5381a9f16aa9fe7f.jpg)  
Fig. 6. Enhanced process map based on data view

Table 5  
Data view of travel reimbursement process.

<table><tr><td></td><td> $d_1$ </td><td> $d_2$ </td><td> $d_3$ </td><td> $d_4$ </td><td> $d_5$ </td></tr><tr><td> $V_t^1$ </td><td>w</td><td></td><td>w</td><td></td><td></td></tr><tr><td> $V_t^2$ </td><td></td><td>w</td><td></td><td></td><td></td></tr><tr><td> $V_t^3$ </td><td></td><td>r</td><td></td><td></td><td></td></tr><tr><td> $V_t^4$ </td><td></td><td></td><td>r</td><td></td><td></td></tr><tr><td> $V_t^5$ </td><td></td><td></td><td></td><td>w</td><td></td></tr><tr><td> $V_t^6$ </td><td>r</td><td></td><td>r</td><td></td><td></td></tr><tr><td> $V_t^7$ </td><td></td><td></td><td></td><td></td><td>w</td></tr><tr><td> $V_t^8$ </td><td></td><td></td><td></td><td>r</td><td></td></tr><tr><td> $V_t^9$ </td><td></td><td></td><td></td><td></td><td>r</td></tr><tr><td> $V_t^{10}$ </td><td>r</td><td></td><td>r</td><td></td><td></td></tr><tr><td> $V_t^{11}$ </td><td></td><td></td><td></td><td>r</td><td></td></tr><tr><td> $V_c^1$ </td><td>r</td><td></td><td></td><td></td><td></td></tr><tr><td> $V_c^2$ </td><td></td><td>r</td><td></td><td></td><td></td></tr><tr><td> $V_c^3$ </td><td></td><td></td><td>r</td><td></td><td></td></tr><tr><td> $V_c^4$ </td><td>r</td><td></td><td></td><td></td><td></td></tr><tr><td> $V_c^5$ </td><td></td><td></td><td></td><td>r</td><td></td></tr></table>

3.2.4. Step 4: Apply domain constraints.

We informally de<sup>fi</sup>ne process semantic errors as inappropriate edges between task and decision vertices resulting in process maps that are logically wrong. In this step, a thorough walkthrough of the process map should be conducted to identify and remove any semantic errors by applying domain constraints. Domain constraints specify how certain tasks are linked to one another, which is generated by domain experts. Some simple domain constraints can be enforced by computer programs. For example, approve or review a data item must happen after that data item is submitted, which represent a domain constraint concerning task sequence. This constraint can be checked and enforced by a computational procedure to the extent possible. However, many domain constraints contain complex semantic information about the whole process, and therefore, complete automation is dif<sup>fi</sup>cult if not impossible. Very often, new task or decision vertices are added as a result of correcting the errors. After reviewing the process map in Fig. 8, we identify two semantic errors: $ { \boldsymbol { v } } _ { t } ^ { 7 }$ (issue the check) is linked to v<sup>9</sup> (refund back the check), which contains a wrong business logic, and $\nu _ { t } ^ { 1 1 }$ (Review TEF) is linked to $ { \boldsymbol { v } } _ { t } ^ { 8 }$ (Review TEF quarterly), which results in the corresponding reimbursement request form not getting reviewed in $\boldsymbol { v } _ { t } ^ { 1 0 } .$ To remove those semantic errors, two decision vertices $v _ { c } ^ { 6 }$ and $ { v _ { c } } ^ { 7 }$ are added, as shown in Fig. 9.

The process derivation procedure described in the above four steps can also be conveniently depicted with a process matrix, shown in Table 6. Initially, the process matrix contains the Ps based on the given process policies. Then, the matrix is updated by adding Ds for the edges identi<sup>fi</sup>ed from the data view in Table 5. Next, the semantic analysis removes a number of edges as represented in the process matrix by the symbols of $P \to 0$ and $D \to 0 ,$ respectively. The edges added after applying structural and domain constraints are depicted with the symbol R. While the process maps modeled as UML activity diagrams are easy for process analysts to read, the process matrix is easier to use in a computational procedure. Note that the process matrix is closely related to the task view de<sup>fi</sup>ned previously.

In an ideal situation where organizations have process policies de<sup>fi</sup>ning every aspect of their business processes, complete process models should be extracted after the four steps discussed above. However, in the real world there are often discrepancies between documented business policies and actual operational processes. Therefore, a <sup>fi</sup>nal process review is necessary to ensure the process map completeness.

## 3.2.5. Step 5: Process review

In this step, the process map is reviewed to ensure it captures all tasks and constraints. Process review is crucial to achieve the completeness of the process map, especially when the process policies are not very detailed and/or have experienced many changes. This step usually includes review meetings with process owners, e.g., managers who oversee the process, and people who are conducting process operations. Given that a process map has been developed based on existing process policies (as described in Steps 1–4), this review is more focused and ef<sup>fi</sup>cient than the data collection in traditional non-policy-driven process mapping approaches. In addition, the meetings may result in the discovery that some parts of business processes are not documented, which helps improve the accuracy and completeness of the business policies.

![](/api/attachments/VR4WTDKQ/fulltext/images/de04d13e5d139a122da7898b4132e4bfd0ac77586866e1c2375f75dec9cb2c5e.jpg)  
Fig. 7. Enhanced travel reimbursement process map based on data view.

To the best of our knowledge, the policy-driven process mapping procedure presented in this section is the <sup>fi</sup>rst attempt to formalize the procedure of process mapping based on business policy analysis. PDPM advocates a new process mapping methodology and takes a critical step toward process discovery automation. Besides providing systematic guidelines during process mapping procedure, PDPM offers additional bene<sup>fi</sup>ts to process policy management. A process map help people visualize narrative policies so that it is easier to analyze them because graphical process maps are much easier to understand than textual documents. More importantly, this process map is dynamically linked to the policy texts by means of the PDPM procedure. For example, each task is linked to the sentences where it is identi<sup>fi</sup>ed from. This link was missing in the traditional static process maps, which cannot be easily maintained to cope with frequent policy changes. In addition, PDPM helps discover the inconsistency and incompleteness in process policies. For example, the algorithm shown in Table 4 infers additional control <sup>fl</sup>ow links based on data dependencies which may not be known to the business analyst otherwise. Similarly, the three structural constraints also provide guidance to business analysts on inferring additional control <sup>fl</sup>ow links. When the derived process map has missing links among tasks, it implies missing policies to specify the execution order among tasks. In the next section, we further demonstrate and validate the PDPM approach via several case studies.

![](/api/attachments/VR4WTDKQ/fulltext/images/52fb8141750a94278890f271da8df50b69a115d446944e8bb5c3e0821b12a72a.jpg)  
Fig. 8. Revised travel reimbursement process map based on structural constraints

![](/api/attachments/VR4WTDKQ/fulltext/images/39c0f25008946ee4f92e32bdc4f37e6a9f6853a510817355b8fe206588db895b.jpg)  
Fig. 9. Process map after removing semantic errors.

## 4. PDPM validation via case studies

In order to further validate the PDPM methodology, we conduct several case studies. Next, we present a case on product development in detail, summarize several additional cases, and discuss the lessons learned.

## 4.1. A case of product development

In this case study, we applied PDPM to construct the AS-IS product development process model for a medical equipment and reagent manufacturing company (referred to as ABC Systems). Over the years, the company has developed a huge amount of policy documents de<sup>fi</sup>ning the product development process and identifying the best practices within the company. A three-month study of various policy documents from individual departments within ABC Systems was conducted. The study resulted in <sup>fi</sup>ve sets of policy statements and process maps corresponding to the <sup>fi</sup>ve phases of the product development process, as described in Table 7.

By applying the PDPM approach, a number of process elements including tasks, data items, resources, and constraints were identi<sup>fi</sup>ed for each phase as shown in Table 8. The details on deriving the process map for Phase 1 of the product development process using PDPM are presented next.

Process matrix of the travel reimbursement process design.

<table><tr><td></td><td> $v_{t}^{1}$ </td><td> $v_{t}^{2}$ </td><td> $v_{t}^{3}$ </td><td> $v_{t}^{4}$ </td><td> $v_{t}^{5}$ </td><td> $v_{t}^{6}$ </td><td> $v_{t}^{7}$ </td><td> $v_{t}^{8}$ </td><td> $v_{t}^{9}$ </td><td> $v_{t}^{10}$ </td><td> $v_{t}^{11}$ </td><td> $v_{c}^{1}$ </td><td> $v_{c}^{2}$ </td><td> $v_{c}^{3}$ </td><td> $v_{c}^{4}$ </td><td> $v_{c}^{5}$ </td><td>e</td></tr><tr><td> $v_{t}^{1}$ </td><td>0</td><td>0</td><td>0</td><td>D→0</td><td>0</td><td>D</td><td>0</td><td>0</td><td>0</td><td>D→</td><td>0</td><td>P→0</td><td>0</td><td>D→0</td><td>D→0</td><td>0</td><td>0</td></tr><tr><td> $v_{t}^{2}$ </td><td>0</td><td>0</td><td>D</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{t}^{3}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>P</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{t}^{4}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>R</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{t}^{5}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D→0</td><td>0</td><td>0</td><td>D</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D→0</td><td>0</td></tr><tr><td> $v_{t}^{6}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>R</td><td>0</td><td>0</td><td>P→0</td><td>0</td><td>0</td></tr><tr><td> $v_{t}^{7}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>D</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{t}^{8}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>P</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{t}^{9}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>R</td></tr><tr><td> $v_{t}^{10}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>R</td><td>0</td><td>0</td></tr><tr><td> $v_{t}^{11}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{c}^{1}$ </td><td>0</td><td>P</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>R</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{c}^{2}$ </td><td>0</td><td>0</td><td>0</td><td>P</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>R</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{c}^{3}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>P</td><td>0</td><td>0</td><td>0</td><td>0</td><td>R</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $v_{c}^{4}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>P</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>R</td></tr><tr><td> $v_{c}^{5}$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>P</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>R</td></tr><tr><td>s</td><td>R</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Table 7  
Phases of ABC Systems' product development process.  
Table 9

<table><tr><td>Phase 1</td><td>Assess the business opportunity of the proposed product, understand customer needs, clarify the product concept, and assess technology feasibility</td></tr><tr><td>Phase 2</td><td>Determine product and process feasibility, define the product, plan the development and risk management activities of the project</td></tr><tr><td>Phase 3</td><td>Develop the commercialization plan, and execute the design, development, and verification of the product</td></tr><tr><td>Phase 4</td><td>Validate the product and prepare the inventory for market launch</td></tr><tr><td>Phase 5</td><td>Conduct post launch product improvements</td></tr></table>

The simpli<sup>fi</sup>ed policies for Product Development Process Phase 1 are summarized in Table 9. Based on the process map de<sup>fi</sup>nition (De<sup>fi</sup>nition $^ { 2 ) , }$ , we formalized the process policies as shown in Table 10. Fig. 10 shows the preliminary process map based on the task and data views, which validates Observations 1–3 on process policies, i.e., process policies contain rich information on business processes and preliminary process models can be extracted from narrative business policies. In addition, Fig. 10 further con<sup>fi</sup>rms Observation 4 by showing that process policies in the real world are usually incomplete and a complete process model cannot be derived solely based on the business policies.

We re<sup>fi</sup>ne Fig. 10 by applying structural constraints, resulting in the process map in Fig. 11. Although Fig. 11 is syntactically correct, it contains several semantic errors. For example, tasks $t _ { 8 } , t _ { 9 } , t _ { 1 0 } ,$ and $t _ { 1 2 }$ are all directly connected to the end nodes, which is logically wrong. This demonstrates that PDPM cannot be fully automated and how to systematically handle process semantic errors is a critical issue for PDPM. Eventually, we removed the semantic errors by introducing one task $t _ { 1 3 , }$ and two decisions with related constraints, c and $c _ { 8 } ,$ which leads to the <sup>fi</sup>nal process map shown in Fig. 12.

This case study further demonstrates the feasibility of PDPM using a different set of business policies from a different business domain than the aforementioned travel policies.

## 4.2. Additional case studies and lessons learned

When we discussed cases on the travel regulation and product development, we showed the simpli<sup>fi</sup>ed policy sentences (see Tables 1 and 9) to facilitate the demonstration of the PDPM approach. In actual process mapping projects, PDPM should be directly applied to policy sentences without simpli<sup>fi</sup>cation, which was how we applied PDPM to the case studies discussed in this paper. Besides the two case studies aforementioned, we have also conducted additional case studies based on real-world policy manuals from different business domains to validate PDPM methodology as summarized in Table 11.

Based on our experience with the case studies, we outline the bene<sup>fi</sup>ts of the PDPM methodology. First, the process policy template in PDPM provides systematic guidelines on how to parse policy sentences. Without the policy template, the business analysts do not have a clear idea on what to look for when analyzing policy sentences. Second, by parsing policy sentences into explicit process elements, inconsistencies are easier to identify. We developed a tool to facilitate the policy parsing as shown in Fig. 13, where process elements are stored in database once they are identi<sup>fi</sup>ed. With the help of this tool, naming inconsistencies for tasks, data, and resources can be identi<sup>fi</sup>ed more easily than otherwise. Third, policy incompleteness becomes apparent once the PDPM procedure is applied. In all cases, we found that after going through the PDPM procedure we can only get process fragments instead of complete process maps. The missing links among tasks indicate missing policies which are very dif<sup>fi</sup>cult if not impossible to identify by simply reading large volumes of the policy documents. In summary, the <sup>fi</sup>ve case studies in this paper help validate the feasibility of the PDPM methodology in real-world business settings. If adopted, this novel approach should have signi<sup>fi</sup>cant impact on the capabilities and ef<sup>fi</sup>ciency of process analysts in developing business process models and work<sup>fl</sup>ow technology.

Table 8  
Summary of derived process components from process policies.

<table><tr><td>Phases</td><td>Tasks</td><td>Data items</td><td>Constraints</td><td>Resources</td></tr><tr><td>Phase 1</td><td>12</td><td>7</td><td>6</td><td>6</td></tr><tr><td>Phase 2</td><td>10</td><td>4</td><td>2</td><td>5</td></tr><tr><td>Phase 3</td><td>14</td><td>8</td><td>4</td><td>5</td></tr><tr><td>Phase 4</td><td>11</td><td>8</td><td>0</td><td>4</td></tr><tr><td>Phase 5</td><td>8</td><td>4</td><td>0</td><td>5</td></tr></table>

Process policies for Phase 1 of ABC Systems' product development process.

<table><tr><td>P1: Marketing department presents the product concept.P2: Design department submits the product proposal based on the product concept.P3: PAC is responsible to evaluate the project proposal and verify if the project aligns well with the company strategy.P4: The product feasibility report is prepared based on a technology challenge map.P5: The product risk assessment is done by the PAC to determine whether it is feasible.P6: The PAC will formulate an Intellectual Property (IP) strategy for the project and submit it to the legal department for approval.P7: If the project requires IP sharing with third party, IP sharing and protection plan should be formulated.P8: If external partners are involved, Supply Management should formulate the partner selection plan.P9: A project budget proposal should be submitted and approved by PAC.P10: If the project budget exceeds $10 million, the project has to be approved by the finance department.</td></tr></table>

## 5. Related work

Identifying and analyzing existing organizational processes (a.k.a. AS-IS process models) is the foundation for any further process changes and improvements [20]. Process mapping refers to the methodologies and related tools that help organizations identify, understand, and improve their current AS-IS processes [17]. Existing process mapping methods can be classi<sup>fi</sup>ed as either mainly participative or analytical [29]. Participative approaches tend to obtain process information using

Table 10  
Formalized product development process policies.

<table><tr><td>PID</td><td>T</td><td>D</td><td>C</td><td>R</td><td>TS</td><td>TR</td><td>TD</td></tr><tr><td>1</td><td> $t_{1}$ </td><td> $d_{1}$ </td><td>NA</td><td> $r_{1}$ </td><td>NA</td><td> $(t_{1}, r_{1})$ </td><td> $(t_{1}, d_{1}, w)$ </td></tr><tr><td>2</td><td> $t_{2}$ </td><td> $d_{1}, d_{2}$ </td><td>NA</td><td> $r_{2}$ </td><td>NA</td><td> $(t_{2}, r_{2})$ </td><td> $(t_{2}, d_{2}, w), (t_{2}, d_{1}, r)$ </td></tr><tr><td>3</td><td> $t_{3}$ </td><td> $d_{2}$ </td><td> $c_{1}$ </td><td> $r_{3}$ </td><td> $(t_{3}, \text{null}, c_{1})$ </td><td> $(t_{3}, r_{3})$ </td><td> $(t_{3}, d_{2}, r)$ </td></tr><tr><td>4</td><td> $t_{4}$ </td><td> $d_{3}$ </td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td> $(t_{4}, d_{3}, w)$ </td></tr><tr><td>5</td><td> $t_{5}$ </td><td>NA</td><td> $c_{2}$ </td><td> $r_{3}$ </td><td> $(t_{5}, \text{null}, c_{2})$ </td><td> $(t_{5}, r_{3})$ </td><td> $(t_{5}, d_{3}, r)$ </td></tr><tr><td>6</td><td> $t_{6}, t_{7}$ </td><td> $d_{4}$ </td><td>NA</td><td> $r_{4}$ </td><td> $(t_{6}, t_{7}, \text{null})$ </td><td> $(t_{6}, r_{3}), (t_{7}, r_{4})$ </td><td> $(t_{6}, d_{4}, w), (t_{7}, d_{4}, r)$ </td></tr><tr><td>7</td><td> $t_{8}$ </td><td> $d_{5}$ </td><td> $c_{3}$ </td><td>NA</td><td> $(\text{null}, t_{8}, c_{3})$ </td><td>NA</td><td> $(t_{8}, d_{5}, w), (c_{3}, d_{4}, r)$ </td></tr><tr><td>8</td><td> $t_{9}$ </td><td> $d_{6}$ </td><td> $c_{4}$ </td><td> $r_{5}$ </td><td> $(\text{null}, t_{9}, c_{4})$ </td><td> $(t_{9}, r_{5})$ </td><td> $(t_{9}, d_{6}, w)$ </td></tr><tr><td>9</td><td> $t_{10}, t_{11}$ </td><td> $d_{7}$ </td><td> $c_{5}$ </td><td> $r_{3}$ </td><td> $(t_{10}, t_{11}, \text{null}), (\text{null}, t_{11}, c_{5})$ </td><td> $(t_{10}, r_{3}), (t_{11}, r_{3})$ </td><td> $(t_{10}, d_{7}, w), (t_{11}, d_{7}, r)$ </td></tr><tr><td>10</td><td> $t_{12}$ </td><td> $d_{7}$ </td><td> $c_{6}$ </td><td> $r_{6}$ </td><td> $(\text{null}, t_{12}, c_{6})$ </td><td> $(t_{12}, r_{6})$ </td><td> $(t_{12}, d_{7}, r)$ </td></tr></table>

Tasks: t : present product concept; $t _ { 2 } { \mathrm { : } }$ submit product proposal; $t _ { 3 } { \dot { : } }$ evaluate product proposal; t : prepare feasibility report; $t _ { 5 } { \mathrm { : } }$ evaluate product feasibility; t : formulate IP strategy; t : approve IP strategy; t : formulate IP sharing and protection plan; t : formulate partner selection plan; $t _ { 1 0 } \colon$ submit budget proposal; $t _ { 1 1 } { : }$ approve budget proposal; $t _ { 1 2 } { \mathrm { : } }$ approve big budget.

Data items: d<sub>1</sub>: product concept; $d _ { 2 } \colon$ product proposal; $d _ { 3 } \colon$ product feasibility report; d : IP strategy; d : IP sharing and protection plan; $d _ { 6 } \colon$ partner selection plan; d : project budget proposal.

Process constraints: $c _ { 1 } { : }$ the product conforms to the company strategy; c : product is feasible; $c _ { 3 } \mathrm { : }$ the product requires IP sharing with 3rd party; $c _ { 4 } { : }$ the product involves partnerships; $c _ { 5 } \colon$ the project budget is approved; $c _ { 6 } { \mathrm { : } }$ the project budget is greater than \$10M.

Resources: $r _ { 1 } :$ Marketing Department; r : Design Department; $r _ { 3 } \colon$ Product Approva Committee (PAC); r : Legal Department; $r _ { 5 } \colon$ Supply Management Department; $r _ { 6 } \mathrm { : }$ Finance Department.

![](/api/attachments/VR4WTDKQ/fulltext/images/87afe6520d8de6b3c224f64348b3382a84bb67f15e57a4fd8a0c46784afa9f2b.jpg)  
Fig. 10. Product development process based on task and data views.

![](/api/attachments/VR4WTDKQ/fulltext/images/f04494b6b90a7eec439deaef52d59ad5ec6c46e928af17255c47175f26221ffc.jpg)  
Fig. 11. Product development process after applying structural constraint

Table 11  
![](/api/attachments/VR4WTDKQ/fulltext/images/8dfc57148bed9a64dd5d28cc224ebffc24d533100efe1a6f8175cdabfe5e9ced.jpg)  
Fig. 12. Product development process after applying domain constraints

traditional data collection instruments such as interviews, meetings, and workshops [9,20,24,32], whereas analytical approaches aim to apply formal theories and techniques to derive the process models [11,29].

Prevailing process mapping/design practices conducted in industry is participative [17,29]. As a well-known business process modeling framework, ARIS (Architecture of Integrated Information Systems) has been widely adopted by industry practitioners and has been incorporated in several commercial product offerings from companies like SAP and IDS Scheer [32]. In ARIS, process models are constructed by analyzing and grouping relevant business objects from <sup>fi</sup>ve different views including function, organization, data, output, and control. Although extensive process reference models are provided to help expedite the development of AS-IS processes, most process information is gathered through interviews, workshops, document analysis, etc. The participative process mapping methods, such as the ARIS methodology, can collect most detailed process information, but they are time-consuming, resourceintensive, and ad hoc due to their subjective and manual nature [29]. In addition, although document analysis has been identi<sup>fi</sup>ed as a major means to get process information in many work<sup>fl</sup>ow development reference models, no detailed systematic procedures on how to extract process model based on policy documents have been reported [32,39].

In order to automate process discovery, several analytical process mapping/design approaches have been proposed [11,16,29,35]. Datta proposes an approach to extract process models by analyzing process execution behavior [11]. More speci<sup>fi</sup>cally, a set of activity sequences is <sup>fi</sup>rst collected by observing and recording the activities performed over a period of time, which serves as the input to the approach. Then, the Finite State Machine synthesis method is applied to infer potential recurring patterns out of those activity sequences, which are representative process behaviors, i.e., the process model.

Summary of additional case studies.

<table><tr><td>Policy manual</td><td>Business domain</td><td>TS</td><td>TW</td><td>TT</td><td>TD</td><td>TR</td><td>TC</td><td>TM</td></tr><tr><td>Travel regulation</td><td>Consulting firm</td><td>108</td><td>2056</td><td>23</td><td>19</td><td>3</td><td>11</td><td>~195</td></tr><tr><td>Travel regulation</td><td>Non-profit organization</td><td>42</td><td>979</td><td>19</td><td>22</td><td>2</td><td>10</td><td>~120</td></tr><tr><td>Procurement</td><td>Professional consortium</td><td>132</td><td>3247</td><td>25</td><td>24</td><td>6</td><td>14</td><td>~225</td></tr></table>

TS: total number of sentences; TW: total number of words; TT: total number of tasks, TD: total number of data items; TR: total number of resources; TC: total number of constraints; TM: total minutes used to analyze the policies.

A Product-Based Work<sup>fl</sup>ow Design (PBWD) approach is discussed in [29], which aims to extract a process model by analyzing the speci<sup>fi</sup>cation of the product produced by that process. Essentially, a product speci<sup>fi</sup>cation can be decomposed into data elements with logical dependencies. These data items can be potentially produced by different sets of tasks in different sequences. PBWD strives to derive a process model with a minimal number of tasks required to produce the product by applying cost optimization techniques. Several algorithms have also been developed to extract process models from structured event logs generated by transactional systems such as ERP, CRM, or work<sup>fl</sup>ow management systems [18,35]. To the best of our knowledge, none of the existing analytical process design approaches use unstructured policy documents as their input.

Therefore, Policy-Driven Process Mapping (PDPM) methodology is innovative by proposing a systematic approach for discovering process models from business policies, which leverages the research on both traditional and analytical process mapping. The detailed comparison results between PDPM and other three process mapping/ design approaches aforementioned are shown in Table 12, which further demonstrates PDPM's uniqueness. Note that ‘NA’ means the related information is not found in the corresponding approach.

Process model analysis is critical to determine the correctness and completeness of the process models resulting from process mapping projects. Petri nets have been widely applied as a formal approach to the veri<sup>fi</sup>cation of work<sup>fl</sup>ow structures, a.k.a. control <sup>fl</sup>ows [23,36,37]. After a process model is represented as a Petri net, many structural properties of

![](/api/attachments/VR4WTDKQ/fulltext/images/4f4bf3616a50b953ae1e287321596474fdb5c10113b6d87368e682849bb6d72b.jpg)  
Fig. 13. Screenshot of the policy parser.

Petri nets, such as soundness, liveness, safeness, and deadlock, can be applied to verify the process model [36]. Metagraphs are another formal process modeling approaches with strong analytical capability [3]. Metagraphs provide three different views of a process model, namely, task view, data view and resources view and are able to analyze interactions among those three views via matrix computations [2,3]. Data <sup>fl</sup>ow analysis is another important aspect of process model analysis. Based on the analysis of the inputs and outputs of tasks and their relationships, different types of process data anomalies, such as missing data, redundant data, and con<sup>fl</sup>icting data, are formally de<sup>fi</sup>ned and analyzed [31,34].

Soffer and Wand propose a goal-driven process analysis in [33]. In their approach, a process model consists of three components, a set of initial states, a set of goal states, and a set of transition laws. The laws specify when a set of states transit into another set of states. Two types of process model invalidity, namely, model invalidity and enactment invalidity are formally de<sup>fi</sup>ned, and possible solutions to correct those invalidities are also presented. Many graphical representations of process models have also been established and applied in process mapping practice, such as UML Activity Diagrams [25], BPMN [26], and EPC (Event-driven Process Chain) [32]. Those speci<sup>fi</sup>cations de<sup>fi</sup>ne the semantics of the graphical symbols and related rules. In this paper, we use UML activity diagrams to visually represent process models and leverage the concepts in process model analysis approaches to de<sup>fi</sup>ne the correctness and completeness of process models.

Another related research area is business rules research. The process policies in this paper are essentially business rules that are related to some aspects of business processes. Many rule representation languages have been developed to express business rules, enable rule reasoning, and facilitate rule extraction, reuse and integration [8,14,15,19]. There are also extensive implementation efforts in rule engines and development tools, such as JESS (http://www.jessrules.com/), CLIPS (http://clipsrules. sourceforge.net/), and JBoss Rules (http://www.jboss.com/products/ rules), which provide the platforms for rule execution and management. Recent research on Semantics of Business Vocabulary and Business Rules (SBVR) tends to develop a meta-model for the business rule semantics in order to express business rules in structured English [27]. SBVR rules can be easily understood by business people and also be processed by computers. SBVR can be used to analyze narrative process policies and the rule speci<sup>fi</sup>cation languages can be used to express those policies.

## 6. Conclusions

In this paper, we proposed an innovative process mapping approach by means of systematic process policy analysis, which is referred to as Policy-Driven Process Mapping (PDPM). PDPM is a new process mapping methodology different from the existing participative and analytical process mapping methods by leveraging business policies for process discovery. We applied PDPM approach to <sup>fi</sup>ve case studies to demonstrate its feasibility and developed a PDPM toolkit to facilitate the process mapping procedure. We formalized the concepts of process policy and process map, developed several new concepts such as task view, data view, and process map rules, and designed a set of process mapping algorithms. These artifacts build a foundation for systematic process policy analysis and thus take the <sup>fi</sup>rst step towards policy-driven process mapping automation.

To make the ideas presented in this paper of interest to business managers and practitioners, we distilled the practical ideas of PDPM into six observations, namely, control <sup>fl</sup>ow identi<sup>fi</sup>cation, data <sup>fl</sup>ow constraints, routing rules, process map enhancement, structural constraints and domain constraints. PDPM advocates a new way of building process models based on analysis of business policies. Therefore, the application of PDPM is restricted to organizations with business policies, preferably with a set of well-organized and comprehensive business policies de<sup>fi</sup>ning their key business processes. This limitation does not diminish the value of our research because recent regulatory requirements, such as Sarbanes– Oxley, require organizations to document their business processes more explicitly. Thus, PDPM can be adopted by most organizations to help them better understand and document their business processes.

Comparisons of process mapping approaches

<table><tr><td></td><td>ARIS [32]</td><td>PAA [11]</td><td>PBWD [29]</td><td>PDPM</td></tr><tr><td>Approach</td><td>Participative</td><td>Analytical</td><td>Analytical</td><td>Policy-driven</td></tr><tr><td>Inputs</td><td>Business documents</td><td>Activity sequences</td><td>Product specifications</td><td>Business policies</td></tr><tr><td>Modeling notation</td><td>Event-driven process chain</td><td>Process activity graph</td><td>Data dependency graph</td><td>UML activity diagram</td></tr><tr><td rowspan="4">Process perspectives</td><td>Control flow</td><td>Partial control flow</td><td>Data flow</td><td>Control flow</td></tr><tr><td>Data flow</td><td>Process states</td><td>Control flow</td><td>Data flow</td></tr><tr><td>Organization</td><td></td><td></td><td>Organization</td></tr><tr><td>Constraints</td><td></td><td></td><td>Constraints</td></tr><tr><td rowspan="3">Formal mapping methods and algorithms</td><td rowspan="3">NA</td><td>Finite state machine synthesis</td><td>Cost optimization</td><td>Policy formalization</td></tr><tr><td rowspan="2">Stochastic modeling</td><td>Data dependence</td><td>Algorithms</td></tr><tr><td>Production rules with uncertainty</td><td>Rules</td></tr></table>

Although PDPM cannot be fully automated because identifying and correcting syntactical and semantic errors and checking process completeness require human intelligence and business expertise (see Observations 4, 5, and 6), several algorithms at the core of PDPM can be computerized to assist business analysts. We also observed through the case studies in this paper that the identi<sup>fi</sup>cation of process elements requires signi<sup>fi</sup>cant domain knowledge on the part of the business analysts. We believe that further improvement of the parsing tool will enhance the ease-of-use of the PDPM approach. In order to reduce the cognitive load of applying PDPM, we are currently investigating algorithms that can assist process analysts with policy analysis tasks using text mining techniques and have gotten some encouraging results [21].

## References

[1] T.A. Aldowaisan, L.K. Gaafar, Business process reengineering: an approach for process mapping, Omega 27 (5) (1999) 515–524.

[2] A. Basu, R.W. Blanning, Metagraphs in work<sup>fl</sup>ow support systems, Decision Support Systems 25 (3) (1999) 199–208.

[3] A. Basu, R.W. Blanning, A formal approach to work<sup>fl</sup>ow analysis, Information Systems Research 11 (1) (2000) 17–36.

[4] A. Basu, A. Kumar, Research commentary: work<sup>fl</sup>ow management issues in e-business, Information Systems Research 13 (1) (2002) 1–14.

[5] H.H. Bi, J.L. Zhao, A formal classi<sup>fi</sup>cation of process anomalies for work<sup>fl</sup>ow veri<sup>fi</sup>cation, Proceedings of the 13th Workshop on Info. Technology and Systems, Seattle, WA, 2003, pp. 207–212.

[6] H.H. Bi, J.L. Zhao, Applying propositional logic to work<sup>fl</sup>ow veri<sup>fi</sup>cation, Information Technology and Management 5 (3–4) (2004) 293–318.

[7] A. Braganza, K.C. Desouza, Implementing Section 404 of the Sarbanes Oxley Act: recommendations for information systems organizations, Communications of the AIS 18 (2006) 1–46.

[8] F. Casati, S. Castano, M. Fugini, I. Mirbel, B. Pernici, Using patterns to design rules in work<sup>fl</sup>ows, IEEE Transactions on Software Engineering 26 (8) (2000) 760–785.

[9] C.G. Cobb, Enterprise Process Mapping: Integrating Systems for Compliance and Business Excellence. ASO Ouality Press. 2004.

[10] B. Curtis, M.I. Kellner, J. Over, Process modeling, Communications of the ACM 35 (9) (1992) 75–90.

[11] A. Datta, Automating the discovery of AS-IS business process models: probabilistic and algorithmic approaches, Information Systems Research 9 (3) (1998) 275–301.

[12] J. Dehnert, W.M.P.v.d. Aalst, Bridging the gap between business models and work<sup>fl</sup>ow speci<sup>fi</sup>cations, International Journal of Cooperative Information Systems 13 (3) (2004) 289–332.

[13] R.M. Dewan, A. Seidmann, Z.D. Walter, Work<sup>fl</sup>ow optimization through task redesign in business information processes, Proceedings of the 31st Hawii International Conference on Systems Sciences, Kohala Coast, Hawaii, USA, 1998.

[14] J.C. Giarratano, G. Riley, Expert Systems: Principles and Programming, Course Technology, 2005.

[15] B. Grosof, Representing e-business rules for the semantic web: situated courteous logic programs in RuleML, Proceedings of Workshop on Information Technologies and Systems, New Orleans, Louisiana, 2001.

[16] I. Hofacker, R. Vetschera, Algorithmical approaches to business process design, Computers & Operations Research 28 (13) (2001) 1253–1275.

[17] V.D. Hunt, Process Mapping : How to Reengineer Your Business Processes, Wiley, 1996.

[18] S. Hwang, W. Yang, On the discovery of process models from their instances, Decision Support Systems 34 (1) (2002) 41–57.

[19] J. Kang, J.K. Lee, Rule identi<sup>fi</sup>cation from web pages by the XRML approach, Decision Support Systems 41 (1) (2005) 205–227.

[20] W.J. Kettinger, J.T.C. Teng, S. Guha, Business process change: a study of methodologies techniques, and tools, MIS Quarterly 21 (1) (1997) 55–80.

[21] J. Li, H.J. Wang, Z. Zhang, J.L. Zhao, A policy-based process mining framework: mining business policy texts for discovering process models, Journal of Information Systems and E-Business Management (2009).

[22] R. Liu, A. Kumar, An analysis and taxonomy of unstructured work<sup>fl</sup>ows, Proceedings of Business Process Management, Nancy, France, 2005, pp. 268–284.

[23] R. Liu, A. Kumar, W. Van Der Aalst, A formal modeling approach for supply chain event management, Decision Support Systems 43 (3) (2007) 761–778.

[24] D. Madison, Process Mapping, Process Improvement and Process Management, Paton Press, 2005.

[25] OMG, UML Superstructure Speci<sup>fi</sup>cation, v2.0, 2005.

[26] OMG, Business Process Modeling Notation Speci<sup>fi</sup>cation, 2006.

[27] OMG, Semantics of Business Vocabulary and Business Rules Speci<sup>fi</sup>cation, 2006.

[28] T.R. Peltier, Information Security Policies and Procedures: A Practitioner's Reference, Auerbach Publication. 2004

[29] H.A. Reijers, S. Limam, W.M.P. van der Aalst, Product-based work<sup>fl</sup>ow design, Journal of Management Information Systems 20 (1) (2003) 229–262.

[30] N. Russell, W.M.P.v.d. Aalst, A.H.M.t. Hofstede, D. Edmond, Work<sup>fl</sup>ow resource patterns: identi<sup>fi</sup>cation, representation and tool support, Proceedings of Proceedings of the 17th International Conference on Advanced Information Systems Engineering (CAiSE 05), Porto, Portugal, 2005.

[31] S. Sadiq, M. Orlowska, W. Sadiq, C. Foulger, Data <sup>fl</sup>ow and validation in work<sup>fl</sup>ow modelling, Proceedings of the Fifteenth Conference on Australasian Database Dunedin, New Zealand, 2004, pp. 207–214.

[32] A.-W. Scheer, ARIS—Business Process Modeling, Springer, 2000.

[33] P. Soffer, Y. Wand, Goal-driven multi-process analysis, Journal of the Association for Information Systems 8 (3) (2007) 175–202.

[34] S.X. Sun, J.L. Zhao, J.F. Nunamaker, O.R.L. Sheng, Formulating the Data Flow Perspective for Business Process Management, Information Systems Research 17 (4) (2006) 374–391.

[35] W.M.P. van der Aalst, Veri<sup>fi</sup>cation of work<sup>fl</sup>ow nets, Proceedings of 18th International Conference on Application and Theory of Petri Nets, Toulouse, France (1997) 407–426

[36] W.M.P. van der Aalst, The application of Petri nets to work<sup>fl</sup>ow management Journal of Circuits, Systems and Computers 8 (1) (1998) 21–66.

[37] W.M.P. van der Aalst, Reengineering knock-out processes, Decision Support Systems 30 (4) (2000) 451–468.

[38] W. van der Aalst, T. Weijters, L. Maruster, Work<sup>fl</sup>ow mining: discovering process models from event logs, IEEE Transactions on Knowledge and Data Engineering 16 (9) (2004) 1128–1142.

[39] M. Weske, T. Goesmann, R. Holten, R. Striemer, A reference model for work<sup>fl</sup>ow application development processes, Proceedings of International Conference on Work activities Coordination and Collaboration (1999) 1–10.

[40] WfMC, Work<sup>fl</sup>ow Management Coalition Terminology & Glossary, 1999.

![](/api/attachments/VR4WTDKQ/fulltext/images/55332ec608d430471c77e5d36a9c8d1d07aeef1b7a5543e5bbd1c0f4ed36d1ea.jpg)

Harry Jiannan Wang is Assistant Professor of Management Information Systems in the Lerner College of Business and Economics at the University of Delaware. He received Ph.D. in Management Information Systems from the Eller College of Management, University of Arizona, and B.S. in Management Information Systems from Tianjin University, China. His research interests involve business process management, work<sup>fl</sup>ow technologies and applications, and services computing. He has published several research articles in academic journals and conferences such as International Journal of Web Services Research, Journal of Information Systems and E-Business Management, Communication of the AIS, International Conference on Information Systems (ICIS), Work

shop on Information Technologies and Systems (WITS), and Americas Conference on Information Systems (AMCIS).

![](/api/attachments/VR4WTDKQ/fulltext/images/d7f8ae189bca2c728a8cbd357341cd7787452afbdb1ad39c56f0d7b79b474ab1.jpg)

J. Leon Zhao is Head and Chair Professor in Information Systems, City University of Hong Kong. He was Eller Professor in the Department of Management Information Systems, University of Arizona before January 2009. He also taught previously at HKUST and College of William and Mary, respectively. He holds Ph.D. and M.S. degrees from the Haas School of Business, UC Berkeley, M.S. degree from UC Davis, and B.S. degree from Beijing Institute of Agricultural Mechanization. His research is on information technology and management, with a particular focus on work<sup>fl</sup>ow technology and applications in knowledge distribution, e-learning, supply chain management, organizational performance management, and services computing. Leon's research has been supported by NSF, SAP, and other sponsors. He received an IBM Faculty Award in 2005 for his work in business process management and services computing. Leon has been associate editor of Information Systems Research, IEEE Transactions on Services Computing, Decision Support Systems, Electronic Commerce Research and Applications, International Journal of Business Process Integration and Management, International Journal of Web and Grid Services, and International Journal of Web Services Research and is on the editorial board of Journal of Database Management. He has co-edited nine special issues in various IS journals. Leon has been chair or program chair for numerous conferences including the 5th International Conference on Design Science Research in Information Systems and Technology (DESRIST'10) the IEEF International Conference on Services Computing, Bangalore, India (SCC'09), the 2008 IEEE Symposium on Advanced Management of Information for Globalized Enterprises (AMIGE'08), the 2008 Arizona Exposium on Frontiers of Information Technology and Applications (FITA'08), the 2007 China Summer Workshop on Information Management (CSWIM'07), the 2006 IEEE Conference on Services Computing (SCC'06), the 2005 Workshop on Information Technology and Systems (WITS'05), and the 2003, Workshop on E-Business (WEB'03) among others, He has also served on many program committees in international conferences.

![](/api/attachments/VR4WTDKQ/fulltext/images/6f097b94cbd32214b8c5521b124b2c28af4998da71fc841791beaa3f0845a7ce.jpg)

Liang-Jie Zhang (LJ) is a research staff member (RSM) and program manager of application architectures and realization at IBM T.J. Watson Research Center. Currently, he leads the creation of Cloud Computing Open Architecture and associated application development technologies for the cloud. He is the worldwide leader of IBM's SOMA Modeling Environment (SOMA-ME), which is the model-driven SOA (Service-Oriented Architecture) solution design platform from IBM. He is also the worldwide co-leader of IBM's SOA Solution Stack (a.k.a. SOA Reference Architecture) project. He is the lead author of book “Services Computing” published in 2007 by Springer. He has published more than 140 technical papers in journals, book chapters, and conference proceedings. He has received 2 IBM Outstanding Technical Achievement Awards, 10 IBM Plateau Invention Achievement Awards, an Outstanding Achievement Award by the World Academy of Sciences, and an Innovation Leadership Award from Chinese Institute of Electronics. Dr. Zhang has 36 granted patents and 20 pending patent applications. As the lead inventor, he holds federated Web services discovery and dynamic services composition patents. He is the founding chair of IEEE Computer Society Technical Committee on Services Computing and IBM Research Services Computing Professional Interest Community (PIC). Dr. Zhang currently serves as the Editor-in-Chief of IEEE Transactions on Services Computing (TSC).
