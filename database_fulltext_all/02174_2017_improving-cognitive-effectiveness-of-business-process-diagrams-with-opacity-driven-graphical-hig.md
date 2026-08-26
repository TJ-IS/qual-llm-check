---
otero_id: 2174
otero_key: "6UZPVPA8"
title: "Improving cognitive effectiveness of business process diagrams with opacity-driven graphical highlights"
authors: "Gregor Jošt; Jernej Huber; Marjan Heričko; Gregor Polančič"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.09.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving cognitive effectiveness of business process diagrams with opacity-driven graphical highlights

Gregor Jošt ⁎, Jernej Huber, Marjan Heričko, Gregor Polančič

Faculty of Electrical Engineering and Computer Science, University of Maribor, Smetanova ul. 17, SI-2000 Maribor, Slovenia

## a r t i c l e i n f o

Article history: Received 22 February 2017 Received in revised form 12 September 2017 Accepted 12 September 2017 Available online xxxx

Keywords: Business process diagrams Cognitive effectiveness Understandability Graphical highlights Complexity BPMN

## a b s t r a c t

In order to facilitate the communication between the stakeholders, business process diagrams must be easy to understand. This is challenging to achieve, since they can become large and complex. In our previous work, we proposed Opacity-Driven Graphical Highlights, a novel approach for increasing the cognitive effectiveness of business process diagrams by changing the opacity of graphical elements and provided a prototype implementation of the approach. The goal of this study was to empirically validate if our proposed approach positively impacts cognitive effectiveness of business process diagrams and if the users will find the prototype implementation useful. To this end an experimental research was conducted where speed, ease and accuracy of answering questions were observed along with the perceived usefulness of the prototype. Participants that used Opacity-Driven Graphical Highlights significantly outperformed those that used the conventional approach. We can conclude that using Opacity-Driven Graphical Highlights increases the cognitive effectiveness of business process diagrams, while the corresponding prototype is perceived as being useful.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

Business processes are core asset of organizations, which aim to facilitate the exchange of business-related operational and strategic information [1], necessary for performing effective decision-making [2]. Business processes can be represented in a form of business process models that capture both how the business works and how the value is created for various stakeholders [3]. It is a common practice to represent a business process model visually - in form of a business process diagram (hereinafter referred to as BPD) [1].

BPDs are commonly modeled in graph-oriented business process languages (i.e. visual notations) [4], which form an integral part of the language of software engineering and tend to be effective because they tap into the capabilities of the powerful and highly parallel human visual system. Notations may be more or less effective, where the cognitive effectiveness of the corresponding BPDs-based communication is mainly influenced by how the modeler and the reader understand the same BPD [5]. Regardless of the effectiveness of notations, BPDs can easily become large and difficult to understand [6] also due to the complexity of the nature of the problem, which needs to be solved [7].

Many principles were suggested in order to improve cognitive effectiveness, e.g. dual coding, visual expressiveness and complexity management [5]. Among those, some might be part of notations, e.g. elements, which enable a hierarchical decomposition of a BPD, or elements, which abstract parts of a BPD. Others might leverage the flexibility of the elements' non-standardized visual variables for enriching their information (e.g. associating a specific color with an organization's role). The application of these principles have demonstrated several benefits, e.g. improving comprehension of BPDs [8,9]. However, since these approaches intervene with the notation or BPD definition, they require that information of applied principle is stored in BPD's model or meta-model. While this is not an issue in case when the applied principle is part of a standard, it becomes critical when it is out of the scope of a standard (e.g. interoperability and compatibility issues between tools [9]). Thus, our motivation was to propose a novel approach for improving cognitive effectiveness of BPDs, which is notation and BPD independent and leverages the principle of visual expressiveness in order to make the BPD appear less complex [10]. This was achieved by introducing Opacity-Driven Graphical Highlights, which is based on manipulating the opacity of BPD's graphical elements. We also implemented a prototype software solution, which demonstrates the proposed approach.

In this paper, we present the results of the empirical study, conducted to investigate if the introduction of Opacity-Driven Graphical Highlights improves the cognitive effectiveness of BPDs (RQ ) and if users will find the corresponding prototype software solution useful $\left( \mathsf { R Q } _ { 2 } \right)$ These objectives were achieved by organizing our research and this paper as follows. The second section focuses on research background, namely BPDs and notations, complexity of BPDs and cognitive effectiveness of BPDs. The third section provides the related work, with the focus on approaches that tend to improve cognitive effectiveness of BPDs. The fourth section overviews our previous work, i.e. theoretical foundations, proposed set of Opacity-Driven Graphical Highlights and the implementation of the prototype. The fifth section presents the details of the empirical research, whereas the sixth section provides the analysis and results of the gathered data. The last section reviews the limitations along with the implications of this research and provides an overview of the future work.

## 2. Research background

## 2.1. Business process diagrams and notations

Business process modeling is the activity of graphically documenting and representing business processes [11], which is at the heart of modern organizations. Large organizations manage thousands of BPDs in their process repositories, since they form a knowledge base that enables a competitive advantage [12,13]. BPDs enable business users to understand the process and share such an understanding with the rest of the stakeholders [1] as well as to find possible points of improvements in the process [11]. Furthermore, BPDs are considered as one of the mechanisms to guide decision-making in the business processes [14]. This is reasonable, since BPDs can convey information clearer and more precise than ordinary language. Besides, due to the picture superiority effect, information represented visually is more likely to be remembered [5].

BPDs are created by using process modeling notations, which generally provide means to graphically represent activities, events, resources, roles, actors, functions, organization and hierarchy with the aim to compose a business process and its surrounding area [11]. To achieve this, process modeling notations primarily consist of graphical symbols, definitions of the meaning of each symbol and a set of compositional rules [5].

There are many notations that enable business process modeling. However, to reduce the risk of misunderstanding the conveyed information, it is preferred to model the BPDs using a notation, understood by all stakeholders [1]. Among those, BPMN is considered to be the de facto standard in business process modeling [15,16] and is one of the most widely used process modeling notations [11].

## 2.2. Complexity of business process diagrams

Since BPDs can grow to be large and difficult to understand [6], they can become a barrier rather than an aid in the communication. This is due to the fact that the amount of information, which can be effectively conveyed by BPD, is limited by human perceptual and cognitive abilities. In this light, perceptual limits address the situation, where the ability to visually recognize the distinction between diagram elements decreases with their number and proximity. Also, the number of elements that are understood at a time is limited by working memory capacity, which is considered to be a cognitive limitation [6,17].

BPDs can become complex [7], which can negatively affect their correctness, maintainability and understandability [18]. Moreover, if a BPD is complex, it can become harder to determine if it properly represents the business process and can potentially hinder the communication with stakeholders [19] [20]. Evaluation of the complexity of BPDs can be achieved by using measurements to assess whether a BPD is easy or difficult to understand. Such measurements are commonly referred to as complexity metrics [21].

## 2.3. Cognitive effectiveness of business process diagrams

As already stated, BPDs have to be effective in making the human communication and problem solving easier. This can be achieved by reducing the cognitive load, which represents the total amount of mental effort being used in the working memory at a point in time [22]. Therefore, BPDs have to be optimized for processing by the human mind, since the visual representation of BPDs offers little or no value for communication with computers [23]. As such, Cognitive Load Theory provides instructions on how to present information in a way that reduces the cognitive load and optimizes human understanding. Cognitive Load Theory further differentiates between intrinsic cognitive load, which derives from the complexity of the domain and extraneous cognitive load, which is dependent on how the information is presented [22].

In such manner, cognitive effectiveness of BPDs was summarized by Moody et al. as “the speed, ease and accuracy with which a representation can be processed by the human mind” [24]. However, cognitive effectiveness is not an intrinsic property of the BPDs. Rather, it is something that needs to be designed into them. Thus, not all BPDs are equally effective in making the human communication easier [24].

Moody [17] proposed a set of evidence-based principles for producing cognitively effective BPDs. Among those, emphasis has been recognized as a concept that dramatically improves understandability and problem-solving performance by highlighting BPD elements with higher relative importance, while the less important ones should be lowlighted.

## 3. Related work

There are many recommendations for improving the cognitive effectiveness of BPDs. In this light, Moody [17] focused on complexity management and suggested that large BPDs should be divided into smaller, cognitively manageable parts, an approach, which is also known as decomposition. The effectiveness of decomposition was empirically validated and the results showed that by reducing a model to chunks of manageable size, complexity was reduced and understanding improved [25]. In addition, Gruhn et al. [26] proposed the improvement of the BPDs' understandability by introducing three groups of workflow-related patterns, namely: (1) finding and removing unnecessary OR gateways, (2) empty sequence flows and (3) reducing the number of model elements.

The aforementioned recommendations can be implemented on dif ferent technical levels. On the level of the notation, several mechanisms, which address cognitive effectiveness by coping with complexity, are already implemented within notations, e.g. link events for modularization and sub-processes for hierarchy in BPMN [27,28]. To this end, studies that introduced additional elements had to intervene with the corresponding notation. For example, in order to simplify existing temporal BPMN constructs, Gagne & Trudel introduced Time-BPMN, an extension to BPMN [29].

On the level of BPDs' definitions, the mechanisms, which address cognitive effectiveness, tap into the flexible properties of the graphical elements. Commonly, these properties have to be written in the definition of BPD. In this manner, La Rosa et al. [19] identified eight notationindependent patterns, which generalize various approaches to change the visual representation of BPDs in order to reduce their complexity. Among them, Graphical Highlight pattern is most relevant for our study, since it can reduce the cognitive overhead. It refers to the features that change the visual aspect of elements, e.g. shape, line thickness and background color, which reduce the cognitive overhead of linking syntactic elements with their corresponding semantics. Besides, Kummer et al. [30] have also recognized color highlighting as the most widely used mechanism for reducing cognitive load. Furthermore, Reijers et al. [8] proposed the use of colors to highlight matching operator transitions (i.e. gateways). The authors formalized the concept for syntax highlighting in workflow nets and implemented it within a Petri net modeling tool. Afterwards, an experimental study was conducted, which explored the effects of highlighting on comprehension performance. The results showed that in the case of non-expert (novice) users, the highlighting significantly increased their performance when reading the BPDs. However, the results were not significant in the case of experts. The usage of colors in order to increase understandability of BPDs was observed by Müller & Rogge-Solti [9] as well. The authors investigated the capabilities of BPMN with the aim to produce easily understood BPDs in the light of healthcare domain. The focus was on dealing with the role information of specific tasks, which is supported in BPMN by using lanes. Nevertheless, as the authors noted, lanes can cause a rise in BPD size, so they presented an approach that uses colored tasks instead of lanes to capture such role information. This resulted in more compact, yet still understandable BPDs.

As evident from the above, our proposal represents a novel approach for increasing the cognitive effectiveness of BPDs. It differs to related work, since it does not intervene neither with the existing notations nor with the corresponding definition of a BPD. This is achieved by applying Opacity-Driven Graphical Highlights to existing BPDs, which are presented in the following chapter.

## 4. Overview of opacity-driven graphical highlights

In the following subchapters, we will provide an overview of the theoretical foundations for the Opacity-Driven Graphical Highlights (hereinafter referred to as Opacity Highlights), a diagram representation approach, which was introduced in our previous work [10]. To this end, we will provide a summary of theoretical foundations, the proposed set of Opacity Highlights and the description of the corresponding prototype software solution, which served as an instrument in our experimental investigation.

## 4.1. Theoretical foundations

Our proposed solution was motivated by the shortcomings of BPDs, as discussed in Chapters 2 and 3. We focused on the Graphical Highlight pattern, as proposed by La Rosa et al. [19], which changes the visual aspect of BPD elements to reduce the cognitive overhead of linking elements with their semantics (see Chapter 3). Several features are available to achieve aforesaid visual highlight and among those, color has been widely recognized as being one of the most cognitively effective visual variables [8,24,27]. This is reasonable, as human visual system can quickly and accurately distinguish between the variations in color [24]. However, if not used accurately, color can impair communication [27]. Also, as Smirnov et al. [13] stated, if coloring of elements is applied in large BPDs, it can become difficult to focus on emphasized elements. A similar notion was made by process modeling experts, who argue that Graphical Highlights are at risk of being overused, which can lead to unreadable BPDs [19]. Furthermore, the semantics of colors may differentiate between users and tools, which can lead to misinterpretations [9]. Those findings were considered when we proposed a solution [10], which preserves the strengths of color and minimizes its shortcomings by changing the opacity (a measure of color [31]) of BPD elements.

## 4.2. Proposed set of opacity-based graphical highlights

We applied opacity to BPDs in light of the aforementioned Opacity Highlights. Instead of introducing a specific color for highlighting the significant BPD elements, the opacity of insignificant ones is set to a value on an interval between 0 and 1. Endpoints are excluded from the interval, since 0 makes the foreground completely transparent, whereas 1 makes the foreground completely opaque. Reducing the opacity creates an impression that the irrelevant elements are transparent, while the relevant ones are highlighted. This is in accordance with Moody [17], who stated that one of the ways to create cognitively effective BPD, the most important parts should be highlighted, whereas less important ones should be lowlighted.

To identify relevant BPD elements, we classified Opacity Highlights into two categories, namely Structural and Behavioral Opacity

Highlights. This was based on the works of Dumas et al. [1], which define structural and behavioral correctness of BPDs. As such, Structural Opacity Highlights address specific elements, while the Behavioral Opacity Highlights focus on a sequence of elements (i.e. partial workflow). Each category of Opacity Highlights was derived from a survey of the relevant literature (see Chapters 2 and 3) and the typical questions regarding the process improvement [32]. We proposed six Structural and seven Behavioral Opacity Highlights, which were applied to BPMN, since it is the de facto standard for business process modeling [15]. In order for an element to appear transparent, we manipulated the opacity of the following attributes: labels inside, above or below the shape, fills of the graphical elements, markers and the lines of the graphical elements.

The six Structural Opacity Highlights focus on specific types of elements in the BPD, and are defined as tuples of elements (Table 1).

Conversely, Behavioral Opacity Highlights do not highlight a predefined types of elements, but represent a sub-flow within a BPD, consisting of Flow Objects and Sequence Flows. It is important to stress that each Behavioral Opacity Highlight has a source and a target, where user selects either one or both. Table 2 overviews the Behavioral Opacity Highlights.

As is evident from Table 1 and Table 2, the Structural Opacity Highlights always highlight a predetermined set of BPD elements, whereas the Behavioral Opacity Highlights highlight different sub-flows, depending on the user's selection.

## 4.3. A prototype software solution

In our previous study [10] we performed a proof of concept in form of a prototype software solution (hereinafter referred to as prototype). This was necessary in order to demonstrate the proposed set of Opacity Highlights. Besides, a vast majority of business analysts and business process practitioners rely on a software tool when performing their activities [33].

The prototype displays BPMN 2.0 diagrams and exposes the additional functionalities in order to support the full set of proposed Opacity Highlights. It is implemented in PHP programming language and uses Scalable Vector Graphics for drawing the BPD. Furthermore, AngularJS is used to retrieve the data without reloading the page. Based on the retrieved data, the predefined level of opacity for each element is applied. Fig. 1 represents the Graphical User Interface (hereinafter referred to as GUI) of the prototype implementation of Opacity Highlights.

As evidenced by Fig. 1, Opacity Highlights are accessed through the GUI in the following ways. Structural Opacity Highlights always address a predictable set of elements, so they can be activated through dedicated buttons at the top section of the prototype (indicated by the number 1 in Fig. 1). On the other hand, Behavioral Opacity Highlights are dependent on the user's selection, since they expose different sub-diagrams and are realized in the form of checkboxes (2). A sole exception is the Sub-flow Behavioral Opacity Highlight, where a sub-flow between

## Table 1

Structural opacity highlights.

<table><tr><td>Highlight name</td><td>BPMN elements that are highlighted</td></tr><tr><td>Input data</td><td>Data object (source), directed data association towards activity, corresponding activity (target).</td></tr><tr><td>Output data</td><td>Data object (target), directed data association towards data object, corresponding activity (source).</td></tr><tr><td>Delays</td><td>Timer intermediate event in normal flow, sequence flow, any flow node.</td></tr><tr><td>Deadlines</td><td>Boundary timer intermediate event, attribute that denotes the corresponding activity, activity.</td></tr><tr><td>Between-process communication</td><td>Flow node A (source or target), message flow, flow node B (source or target). note: flow nodes A and B either belong to or represent different pools.</td></tr><tr><td>Errors</td><td>Boundary error intermediate event, attribute that denotes the corresponding activity, activity.</td></tr></table>

Table 2 Behavioral opacity highlights.

<table><tr><td>Highlight name</td><td>BPMN elements that are highlighted</td></tr><tr><td>Sub-flow</td><td>A subset of all flow objects and sequence flows within a BPD, found between (and including) the source and target nodes. Note: user selects both source and target nodes, which must be within the same pool.</td></tr><tr><td>Process start sub-flow</td><td>A sub-flow with source node representing the selected start event, and target nodes all reachable end events.</td></tr><tr><td>Process end sub-flow</td><td>A sub-flow with source node representing the selected end event, and target nodes all reachable start events.</td></tr><tr><td>Exclusive branch sub-flow</td><td>A sub-flow with source node representing the selected sequence flow that follows the diverging XOR gateway, and target nodes all reachable end events.</td></tr><tr><td>Deadline sub-flow</td><td>A sub-flow with source node representing the chosen boundary timer event, and target nodes all reachable end events. Note: the deadline sub-flow also highlights the activity that the source node is attached to.</td></tr><tr><td>Error sub-flow</td><td>A sub-flow with source node representing the chosen boundary error event, and target nodes all reachable end events. Note: the error sub-flow also highlights the activity that the source node is attached to.</td></tr><tr><td>Data flow</td><td>Selected data object and associations, connecting all corresponding activities that use the selected data object as either input or output.</td></tr></table>

two elements is highlighted. This is addressed by providing two inputs, where user can select both the start and the end element (3). Furthermore, the prototype is designed in a way that Opacity Highlights can be disabled, so none of the features 1, 2 and 3 in Fig. 1 are available nor visible in the GUI. As such, the prototype only displays a conventional graphical representation of the selected BPD, which means that all elements of a BPD are represented with the same opacity.

## 5. Empirical research

The main purpose of this research was to investigate if the proposed Opacity Highlights positively impact cognitive effectiveness of BPDs and if the users will find the prototype useful. The following subsections describe the research model, followed by a description of the experimental design. The latter includes definition of the subjects and sampling, experimental process and the corresponding instruments. Finally, operation of the experiment is provided, addressing the preliminary tests and the actual experiment.

## 5.1. Research model

Based on the research background, the overview of related work and the proposed solution, the research model was defined as presented in Fig. 2.

Fig. 2 represents the scope of the experiment. An independent latent variable was defined, namely the diagram representation approach, with two levels: (1) Conventional and (2) Opacity Highlights. The “Conventional” acts as a representative of current process modeling tools, which does not exploit the opacity of BPD elements. On the opposite “Opacity Highlights” represents our prototype software solution, which changes opacity of elements of a BPD in order to expose parts of a BPD (as defined in Subchapter 4.2). In accordance with our previous work [10], the prototype changed the opacity to 0.2 when applied. To minimize the effects of a modeling tool on experimental results, both treatments were implemented with the same tool (our prototype solution) as describe in the experimental instrumentation (see Subchapter 5.2.3).

To investigate if Opacity Highlights positively impact cognitive effectiveness of BPDs and usefulness of the prototype, we observed five dependent variables. They correspond to both the definition of cognitive effectiveness, which is the speed, accuracy and ease of processing BPD representation by the human mind (Chapter 2.3), and the Technology Acceptance Model (hereinafter referred to as TAM). The latter is used to explain the potential user's acceptance and use of an information system [34] and is influenced by a number of variables, most notably perceived usefulness (PU) and perceived ease of use (PEOU). PU is defined as the degree to which users believe that using a system would increase their performance, while PEOU is defined as the degree to which users believe that using a system would be effortless [35].

![](/api/attachments/6UZPVPA8/fulltext/images/660954f2f9ec72a19941ee7f48d4dfbf90a5f9f8b640e0eb4f8a9f9d54c95f2a.jpg)  
Fig. 1. The prototype with “Data flow” behavioral opacity highlight activated.

Please cite this article as: G. Jošt, et al., Improving cognitive effectiveness of business process diagrams with opacity-driven graphical highlights, Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.09.003

![](/api/attachments/6UZPVPA8/fulltext/images/07df177411b9a28a0a42ffaaae1bd2eae54b3e45417c3aa18184f8ee59b5a874.jpg)  
Fig. 2. Research model.

Based on the definition of the cognitive effectiveness, the first identified dependent variable was accuracy, the degree to which the result of measurement conforms to the correct value. The accuracy was measured by the number of correct answers that the participants obtained (number of correct answers) divided by the number of all questions in the questionnaire (number of all questions, which is a constant). However, since the accuracy reports the percentage of correct answers, the quotient was multiplied by 100. The second dependent variable was speed, representing the rate at which someone operates. It was measured by the number of all questions, divided by the time needed to finish the questionnaire (total time). Additionally, because participants can potentially finish answering the questions faster but make more mistakes [36], another dependent variable, efficiency (number of correct answers divided by total time), was introduced. Also, in the scope of cognitive effectiveness, PEOU dependent variable was introduced. Furthermore, the usefulness of the prototype was observed with the fifth and final dependent variable, PU. Both of the TAM's variables (i.e. PEOU and PU) were measured by the level of agreement with standardized statements, based on seven levels Likert scale. Similar dependent variables and their corresponding measurements were also used by other authors, e.g. [8,37,38].

According to the stated research questions, the alternative and null hypotheses were formulated (Table 3). Based on the definition of cognitive effectiveness, the $\mathsf { R Q } _ { 1 }$ was tested with hypotheses $\mathrm { H } _ { 0 - 1 . 1 ^ { - } } \mathrm { H } _ { 0 - 1 . 4 }$ and RQ with $\mathrm { H } _ { 0 - 2 } .$ Hypotheses were used to test the effects of the diagram representation approach, which was either Opacity Highlights (OH) or Conventional (C), on the cognitive effectiveness of BPDs and the usefulness of the prototype.

Formal definition of the experiment hypotheses.

<table><tr><td>RQ</td><td>Null hypothesis</td><td>Alternative hypothesis</td></tr><tr><td rowspan="4"> $RQ_1$ </td><td> $H_{0-1.1}$ : accuracy (OH) = accuracy (C)</td><td> $H_{a-1.1}$ : accuracy (OH) &gt; accuracy (C)</td></tr><tr><td> $H_{0-1.2}$ : speed (OH) = speed (C)</td><td> $H_{a-1.2}$ : speed (OH) &gt; speed (C)</td></tr><tr><td> $^aH_{0-1.3}$ : efficiency (OH) = efficiency (C)</td><td> $^aH_{a-1.3}$ : efficiency (OH) &gt; efficiency (C)</td></tr><tr><td> $H_{0-1.4}$ : PEOU (OH) = PEOU (C)</td><td> $H_{a-1.4}$ : PEOU (OH) &gt; PEOU (C)</td></tr><tr><td> $RQ_2$ </td><td> $H_{0-2}$ : PU (OH) = PU (C)</td><td> $H_{a-2}$ : PU (OH) &gt; PU (C)</td></tr></table>

<sup>a</sup> Observed dependent variable efficiency is not directly a part of the cognitive effectiveness, as de ned by Moody [5], but was included based on its usage in the afore mentioned related studies.

Null hypotheses in Table 3 indicate that there are no differences between the groups, whereas the greater-than sign is used to indicate that the increase is hypothesized.

The independent latent variable with two levels (see Fig. 2) implies a two group design. We found it reasonable to conduct a posttest-only control group design, where subjects were randomly assigned to treatment and control groups. The treatment group was administered a treatment (i.e. Opacity Highlights diagram representation approach), whereas the control group was not given such a stimulus (i.e. Conventional diagram representation approach). Afterwards, the dependent variables were measured.

For each group, the experiment was conducted in two steps, each representing either a low or a high complexity BPD. This was done for the sake of increasing the external validity of our research as well as to observe if the impact of proposed Opacity Highlights will be greater if applied to more complex BPDs. The order in which we assigned BPDs to each participant was randomized; half of the participants received the high complexity BPD first, followed by the low complexity one, and vice versa for the other half. Randomization was done to minimize any effects that might occur because of the sequence in which participants received the BPDs.

## 5.2. Experimental design

## 5.2.1. Subjects and sampling

Both theoretical and empirical evidence suggests that changes in visual appearance significantly impact the understanding, which is especially true for non-experts [5,8]. While non-experts are commonly associated with undergraduate students [8,25], 85 undergraduate IT students from The Faculty of Electrical Engineering and Computer Science at the University of Maribor participated, having limited training and no professional experience in business process modeling.

Students were randomly assigned into one of the two groups (Opacity Highlights or Conventional diagram representation approach). All subjects participated voluntarily and were prior to experiment now aware of the Opacity Highlights and the corresponding prototype solution.

## 5.2.2. Experiment process

A detailed description of the experiment process is as follows. After deciding to join the experiment, the participants were randomly

G. Jošt et al. / Decision Support Systems xxx (2017) xxx–xxx

assigned to one of the two groups (OH and C). All participants listened to the introductory speech, along with the demonstration of the assigned diagram representation approach (OH or C). In the case of the OH, participants received a 15-minute lesson about the prototype, along with a description of how to use each OH.

Afterwards, participants received a web link to the questionnaire, where they began answering the questions in the following order. Firstly, participants answered questions regarding demographical details. Secondly, a set of questions, regarding the low (see Fig. 7 in Appendix A) and high (see Fig. 8 in Appendix A) complexity BPDs, were given (see Appendix B). We ensured the group equality by providing the same two BPDs for both groups (OH and C), along with the same set of questions. As already stated, the order in which BPDs were assigned was randomized. Participants had to answer to 13 questions one after another for each of the two BPDs, resulting in 26 questions in total. Thirdly, the standard TAM questions regarding the PEOU and PU were provided at the end of both low and high complexity BPDs. Finally, participants were given the option to provide any kind of feedback regarding the experiment or the diagram representation approach.

## 5.2.3. Experiment instruments

In order to perform the experiment process, two experiment instruments were used, namely the prototype and the questionnaire.

The prototype, described in Subchapter 4.3, was used for both groups, namely the OH and C diagram representation approach. In the case of the latter, OH were disabled by a system administrator and were therefore neither visible nor accessible. Moreover, the positioning and labeling of the BPD elements were identical for both approaches. The two BPDs in question were structurally based on the BPMN 2.0 non-executable non-normative examples from the official OMG's document.

Gateway Complexity Indicator (GCI) metric, as proposed by Sánchez-González et al. [39], was used to objectively identify the complexity of the BPDs. GCI is composed of the following gateway complexity metrics: Control-Flow Complexity (the complexity of split gateways by capturing the complexity of XOR-split, OR-split and AND-split constructs), Gateway Mismatch (the sum of gateway pairs which do not match each other), Gateway Heterogeneity (the frequency of different types of gateways used in a BPD), Average Gateway Degree (the average number of incoming and outgoing flows of the gateway constructs), Maximum Gateway Degree (the maximum number of incoming and outgoing flows of a decision constructs) and Total Number of Gateways (the number of decision constructs). However, it is important to stress that the calculation of GCI does not include Event-Based or Complex Gateways. Taking this into the consideration and to achieve the desired level of complexity, both BPDs had to be modified. The high complexity BPD had a GCI value of 14.84, which makes the BPD difficult to understand, whereas the low complexity BPD had a GCI value of 6.51, making the BPD easy to understand [39]. Additionally, the labels in both BPDs were anonymized to avoid domain bias in the participants. Instead of an actual label, each element in the BPD was assigned a prefix that corresponded with the element type (e.g. letter T for Task), followed by a random number. In this light, we ensured that the participants were not able to answer the questions in the experiment based on prior domain knowledge.

The second instrument, questionnaire, was distributed to the participants electronically, using LimeSurvey online survey software. Open and closed questions were provided to gather the demographic information. With respect to the low and high complexity BPDs, the closed questions were used in the experiment, which addressed exclusiveness, order and repetition. This is in accordance with Reijers et al. [8] and Moody [25], who observed the users' comprehension performance (see Chapter 3). Again, a list of questions for high complexity BPD can be seen in Appendix B. Closed questions were also used to obtain the PEOU and PU, whereas open questions were used to gather the participants' feedback regarding the experiment or the usage of the diagram representation approach. The questionnaire was designed in such a way, that we were able to record the time for each specific question automatically. To minimize the cognitive load on the participants and reduce the time, needed for switching between the two web applications (i.e. the prototype and the questionnaire), both were integrated into a single GUI. This was achieved by embedding the prototype within the questionnaire, as represented in the Fig. 3.

Fig. 3 provides the GUI of the experiment instruments, where the prototype (indicated by number 1 in Fig. 3) and the investigated BPD (2) are embedded within the questionnaire (3).

## 5.3. Operation

Two preliminary tests were conducted to ensure that the participants would understand and perform the experiment's tasks in a correct and consistent manner. Based on the feedback from the preliminary tests, the questionnaire was improved and the frame of the embedded prototype was enlarged. Additionally, we limited the duration of the experiment to 45 min

The experiment was executed in a computer classroom at our faculty. All the computers were of the same hardware and software configurations. The computer monitors were all of the same size (22 in.) and resolution (1920 × 1080). This was necessary, since we presumed that the different resolutions and sizes of the computer monitors could put some participants at disadvantage. For example, if the size and the resolution of the computer monitor is lower, the participant would have to scroll more during the experiment, which could directly influence their performance. Two assistants were supervising the experiment and also provided consistent instructions. During the experiment, no exceptions, that could affect the results, were detected.

## 6. Data analysis and results

Data analysis was performed using a spreadsheet application and SPSS Statistics. The responses were manually verified and all were accepted as valid. Afterwards, we analyzed the data. Based on the statistical tests' assumptions (e.g. if the data is normally distributed for each group), either independent t-tests or Mann-Whitney U Test was used to test the differences between OH and C diagram representation approaches. Results were considered significant at the α b 0.05 level.

This chapter is organized as follows. Firstly, we addressed the descriptive statistics, where the results of the experiment were reported. Secondly, considering the assumptions, appropriate statistical tests were used to test the hypotheses. Finally, the results were summarized.

## 6.1. Descriptive statistics

The descriptive statistics of the study variables, i.e. accuracy, speed, efficiency, PU and PEOU is represented in Table 4. Each dependent variable has higher values preferred. As evident, the minimum number of correctly answered questions per participant was 13 out of 26 (50%). This is in accordance with Reijers et al. [8], where the authors defined that the non-experts have to correctly answer at least 44% of the questions. Below this threshold, the participants are deemed to be either unfit or uncommitted to partake in the experiment and should be therefore omitted from further analysis. As this was not the case in our study, we did not omit any participants from the analysis.

Based on the descriptive statistics of the study variables (Table 4), the participants that answered questions using the OH diagram representation approach were more accurate (Median = 92.31%) compared to C diagram representation approach (Median = 80.77%). This is also visible from the corresponding box plots (Fig. 4), where the median is represented as a horizontal line in a box, which indicates the interval between the first and the third quartile. As evident, in the case of OH, the top whisker is absent, indicating that the last quartile and the

Please cite this article as: G. Jošt, et al., Improving cognitive effectiveness of business process diagrams with opacity-driven graphical highlights, Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.09.003

G. Jošt et al. / Decision Support Systems xxx (2017) xxx–xxx

![](/api/attachments/6UZPVPA8/fulltext/images/60dbc800781c90775e865aa8155f079d9c66ff62380545fd4275182546d24039.jpg)  
Fig. 3. Example of the online questionnaire.

maximum value were both 100% (i.e. all questions were correctly an swered by the participants).

Participants with OH also finished their work faster (Median = 0.0265) than their C counterparts (Median = 0.0224), as is visible in the left part of Fig. 5.

Efficiency was included based on its usage in the related studies (see Chapter 5). The box plots in the right part of Fig. 5 shows that the data was again in favor of OH (Median = 0.0265), compared to C (Median = 0.0201).

The results of both of the two TAM's variables (PEOU and PU) show the level of agreement with standardized statements, represented on seven levels Likert scale. With respect to PEOU, participants perceived OH as easier to use (Median = 6.19) than C (Median = 4.25). Similarly, participants also perceived OH as more useful (Median = 6.50), when compared to C (Median = 3.75). The corresponding box plots for both PEOU and PU are lined up side by side on a common scale, as can be seen in Fig. 6.

As evidenced by the Fig. 6, OH is superior in range and interquartile range of both PEOU (range = 3.13, interquartile range = 1) and PU (range = 2.13, interquartile range = 0.84) when compared to existing C diagram representation approach's PEOU (range = 5.25, interquartile range = 2.38) and PU (range = 5.38, interquartile range = 2.5).

## Table 4

Descriptive statistics of the study variables.

<table><tr><td>Dependent variable</td><td>Approach</td><td>N</td><td>Min</td><td>Max</td><td>Median</td><td>Mean (M)</td><td>Std. deviation (SD)</td></tr><tr><td rowspan="2">Accuracy [%]</td><td>C</td><td>41</td><td>50.00</td><td>100.00</td><td>80.77</td><td>80.77</td><td>10.981</td></tr><tr><td>OH</td><td>44</td><td>50.00</td><td>100.00</td><td>92.31</td><td>90.56</td><td>10.670</td></tr><tr><td rowspan="2">Speed [number of all questions/t]</td><td>C</td><td>41</td><td>0.0127</td><td>0.0297</td><td>0.0224</td><td>0.0223</td><td>0.0036</td></tr><tr><td>OH</td><td>44</td><td>0.0141</td><td>0.0363</td><td>0.0265</td><td>0.0269</td><td>0.0057</td></tr><tr><td rowspan="2">Efficiency [number of correct answers/t]</td><td>C</td><td>41</td><td>0.0112</td><td>0.0304</td><td>0.0201</td><td>0.0194</td><td>0.0045</td></tr><tr><td>OH</td><td>44</td><td>0.0120</td><td>0.0398</td><td>0.0265</td><td>0.0258</td><td>0.0064</td></tr><tr><td rowspan="2">PEOU [number]</td><td>C</td><td>41</td><td>1.38</td><td>6.63</td><td>4.25</td><td>3.95</td><td>1.501</td></tr><tr><td>OH</td><td>44</td><td>3.88</td><td>7.00</td><td>6.19</td><td>6.06</td><td>0.714</td></tr><tr><td rowspan="2">PU [number]</td><td>C</td><td>41</td><td>1.00</td><td>6.38</td><td>3.75</td><td>3.84</td><td>1.559</td></tr><tr><td>OH</td><td>44</td><td>4.88</td><td>7.00</td><td>6.50</td><td>6.39</td><td>0.557</td></tr></table>

To summarize the findings above, the participants that used OH performed better compared to C in all measured dependent variables, namely accuracy, speed, efficiency, PEOU, and PU.

## 6.2. Hypotheses testing

In order to determine if the aforementioned differences between the two approaches were significant, the following tests were performed. The data was firstly tested for normality, since dependent variables should be approximately normally distributed for each group of the independent variable to carry out an independent t-tests. Taking into the consideration our sample size (N = 85), we used the Shapiro-Wilk Test. The results of the test are represented in Table 5.

In case of OH group, the data representing accuracy, PEOU and PU values (Table 5) does not conform to normal distribution (p b 0.05). As such, the normality assumption was not met and a non-parametric alternative to independent t-test was used. However, the deviation from normality was not detected for both groups (OH and C) in the case of the dependent variables speed and efficiency (p N 0.05). Because other assumptions based on Green & Salkind [40] were also met, an independent t-test was used.

![](/api/attachments/6UZPVPA8/fulltext/images/bfc48dfa82a0c7a5863b2b9b9cdaa38c3e72a45a8c9d92c162868feeb05bb4b8.jpg)  
Fig. 4. The distributions of accuracy scores for OH and C diagram representation approach.  
Please cite this article as: G. Jošt, et al., Improving cognitive effectiveness of business process diagrams with opacity-driven graphical highlights, Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.09.003

Test of normality.  
![](/api/attachments/6UZPVPA8/fulltext/images/d73631db6af1e761d1eca6ebce5621dd1c85375e5244bfee1400f1f9a2f6b150.jpg)

![](/api/attachments/6UZPVPA8/fulltext/images/6520c20141f1496b2ba9dce058718af6d39ffe74c1bfbd18e3da0607a316a12c.jpg)  
Fig. 5. The distributions of speed (left) and efficiency (right) scores for OH and C diagram representation approach.

Considering the results above, Mann-Whitney U Test was used to evaluate differences in accuracy, PU and PEOU between OH and C. The results can be seen in Table 6.

Based on the results shown in the Table 6 and the descriptive statistics of the study variables (Table 4), the following can be concluded. Accuracy in the case of OH was significantly higher than in the case of C diagram representation approach, $U = 4 2 9 . 5 0 , p < 0 . 0 0 1$ . OH had an average rank of 53.74, while C had an average rank of 31.48. The results were in the expected direction, showing that the participants, which used OH were significantly more accurate when answering the questions than their C counterparts.

Furthermore, PEOU was evaluated significantly higher in the case of OH (average $\mathrm { r a n k } = 5 9 . 3 2 )$ when compared to C (average rank = 25.49), $U = 1 8 4 . 0 0 , p < 0 . 0 0 1$ . PU was evaluated significantly higher in the case of OH as well (average rank = 61.70), compared to those that used C (average rank = 22.93), U = 79.00, p b 0.001. Therefore, it can be concluded that the participants perceived OH as being easier to use and more useful than C.

As we did not detect that the data deviated from normality in the case of speed and efficiency, an independent t-test was conducted (Table 7). The Levene's test for equality of variances was significant for both dependent variables, namely speed and efficiency $\left( p < 0 . 0 5 \right)$ thus equal variances were not assumed when reporting the results of the independent t-test.

Fig. 6. The distributions of both PU and PEOU scores for OH and C diagram representation approach.  
![](/api/attachments/6UZPVPA8/fulltext/images/d14e3a3114928342fe270630d9b3dade44a2c607cab99429d28bece779b2a2cc.jpg)

As evident from the Table 7, the independent t-test was significant for the dependent variable speed, $t ( 7 3 . 1 5 7 ) = - 4 . 4 7 7 , p < 0 . 0 0 1$ . Participants that used OH $( \mathsf { M } = 0 . 0 2 6 9 , \mathsf { S D } = 0 . 0 0 5 7 , \mathsf { s e e T a b l e 4 } )$ ) were significantly faster than those using $\mathrm { \Delta \Gamma } ( \mathrm { M } = 0 . 0 2 2 3 , \mathrm { S D } = 0 . 0 0 3 6 )$ ) diagram representation approach. Similarly was concluded in the case of efficiency, where there was a significant difference between OH (M = $0 . 0 2 5 8 , \mathrm { S D } = 0 . 0 0 6 4 )$ and $\mathsf { C } \left( \mathsf { M } = 0 . 0 1 9 4 , \mathsf { S D } = 0 . 0 0 4 5 \right)$ diagram representation approach in favor of the former, $t ( 7 7 . 0 8 6 ) = - 5 . 3 5 0 , p <$ 0.001. This indicates that participants using OH solved more questions correctly per second than their C counterparts.

After the results of statistical tests were obtained, the hypotheses were evaluated and the corresponding findings reported (Table 8). Based on the results of the independent t-tests and Mann-Whitney U Test, we either failed to reject or rejected the null hypotheses in favor of the alterative hypotheses.

As evident from the table above, all of the null hypotheses were rejected in favor of their corresponding alternatives. As such, the results demonstrate that our proposed novel approach improves cognitive effectiveness $( \mathsf { R Q } _ { 1 } ,$ , hypotheses $\mathrm { H } _ { 0 - 1 . 1 ^ { - } } \mathrm { H } _ { 0 - 1 . 4 } )$ of BPDs when compared to its conventional counterpart. The participants in the experiment perceived the prototype as being useful than conventional diagram representation approach as well $( \mathsf { R Q } _ { 2 }$ hypothesis $\mathrm { H } _ { 0 - 2 } )$

Nevertheless, since the experimental treatments involved BPDs with two levels of complexity, we were able to additionally test if the Opacity Highlights still outperforms Conventional approach, if applied to individual diagrams (low and high complexity). In this light, we found statistically significant improvements when using Opacity Highlights for all dependent variables for BPDs of both complexities $( p < 0 . 0 5 )$ ). This is also in accordance with the results in Table 8.

## 7. Discussion

The main objective of this study was to provide an empirical investigation if using Opacity Highlights positively impacts cognitive effectiveness of BPDs and if the users will find the prototype implementation of Opacity Highlights useful. The cognitive effectiveness, defined by

<table><tr><td rowspan="2">Dependent variable</td><td rowspan="2">Approach</td><td colspan="3">Shapiro-Wilk</td></tr><tr><td>Statistic</td><td>df</td><td>Sig.</td></tr><tr><td rowspan="2">Accuracy</td><td>Conventional</td><td>0.972</td><td>41</td><td>0.396</td></tr><tr><td>Opacity highlights</td><td>0.823</td><td>44</td><td>0.000</td></tr><tr><td rowspan="2">Speed</td><td>Conventional</td><td>0.970</td><td>41</td><td>0.339</td></tr><tr><td>Opacity highlights</td><td>0.968</td><td>44</td><td>0.257</td></tr><tr><td rowspan="2">Efficiency</td><td>Conventional</td><td>0.984</td><td>41</td><td>0.816</td></tr><tr><td>Opacity highlights</td><td>0.981</td><td>44</td><td>0.677</td></tr><tr><td rowspan="2">PEOU</td><td>Conventional</td><td>0.956</td><td>41</td><td>0.115</td></tr><tr><td>Opacity highlights</td><td>0.894</td><td>44</td><td>0.001</td></tr><tr><td rowspan="2">PU</td><td>Conventional</td><td>0.960</td><td>41</td><td>0.153</td></tr><tr><td>Opacity highlights</td><td>0.901</td><td>44</td><td>0.001</td></tr></table>

Please cite this article as: G. Jošt, et al., Improving cognitive effectiveness of business process diagrams with opacity-driven graphical highlights, Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.09.003

Table 6  
Table 7  
Results of Mann–Whitney U test.

<table><tr><td></td><td>Accuracy</td><td>PEOU</td><td>PU</td></tr><tr><td>Mann-Whitney U</td><td>429.500</td><td>184.000</td><td>79.000</td></tr><tr><td>Wilcoxon W</td><td>1290.500</td><td>1045.000</td><td>940.000</td></tr><tr><td>Z</td><td>-4.193</td><td>-6.319</td><td>-7.248</td></tr><tr><td>Asymp. Sig. (one-tailed)</td><td>0.000***</td><td>0.000***</td><td>0.000***</td></tr></table>

⁎⁎⁎ Represent significance at P b 0.001.  
Table 8

Moody [5], was measured by observing the speed, ease and accuracy with which a BPD can be processed by the human mind. Based on the related work, our research model also included efficiency. Besides, the usefulness of the prototype was measured with TAM's PU.

By using the appropriate statistical methods, we were able to analyze if there were significant differences between the participants that used Opacity Highlights and those, which used the conventional diagram representation approach. The participants that used Opacity Highlights were faster, more accurate and more efficient than those that used conventional approach. Participants that used Opacity Highlights found this approach easier to use and more useful, when compared to their counterparts. Therefore, we can conclude that using Opacity Highlights increases the cognitive effectiveness of BPDs and that the corresponding prototype software solution was recognized as useful. Moreover, since PEOU and PU are the most important factors in explaining system use in TAM [41], we can conclude that the participants developed a positive attitude regarding our prototype.

The results of this study are in accordance with Reijers et al. [8], where authors proposed the usage of colors to highlight the matching operator transitions in workflow nets and provided a prototypical implementation. Non-experts, which used their solution, were significantly more accurate compared to those that did not use the highlights. The same was concluded in our study, where we used a measure of color, namely opacity. Besides, we did not focus only on one process element, but provided a more holistic approach that is notation and BPD independent and leverages the principle of visual expressiveness in order to increase cognitive effectiveness of BPDs.

Additionally, we also observed the impact of using the Opacity Highlights when applying them to individual BPDs. Results demonstrate that impact of using Opacity Highlights in case of BPDs with different complexity levels aligns with the general results, as discussed above. Nevertheless, we presume that the applicability of Opacity Highlights increases with the rise of complexity of BPDs.

## 7.1. Internal and external validity

The concerns regarding the internal and external threats to validity were investigated based on the work of Campbell & Stanley [42]. Table 9 represents the actions that were taken to counteract the internal validity threats, relevant for our experimental design.

As evident from the table above, the internal validity threats for posttest-only control group design were considered during the design phase of the experiment. Regarding the external validity threats, two were relevant. Firstly, the ‘interaction effects of selection biases and the experimental treatment’ were addressed by limiting the study to non-experts, which are becoming more active in the real-world business modeling projects. Besides, additional statistical tests were performed to ensure that the participants of the experiment had the same knowledge regarding the notation. Since this was the case, no responses were omitted from further analysis. Secondly, the ‘reactive effects of experimental arrangements’ were counteracted by not making the participants aware of the experiment's research questions and corresponding hypotheses. Besides, for the sake of increasing the generalizability of the results, low and high complex BPDs were investigated, where both were taken from BPMN specification as described in Subchapter 5.2.3. Generalizability of the results was considered also in the second experimental instrument, questionnaire, which consisted of tested statements or questions (e.g. process improvement interview questions [32]). Nevertheless, we acknowledge that there is a risk of generalizing the results, considering that the study was limited to non-experts.

Results of the independent t-test for equality of means (equal variances not assumed).

<table><tr><td>Dependent variable</td><td>t</td><td>df</td><td>Sig. (one-tailed)</td><td>Mean difference</td><td>Std. error difference</td></tr><tr><td>Speed</td><td>-4.477</td><td>73.157</td><td>0.000***</td><td>-0.0046</td><td>0.0010</td></tr><tr><td>Efficiency</td><td>-5.350</td><td>77.086</td><td>0.000***</td><td>-0.0064</td><td>0.0012</td></tr></table>

⁎⁎⁎ Represent significance at P b 0.001.

Hypotheses testing.

<table><tr><td>Null hypothesis</td><td>Findings</td></tr><tr><td> $H_{0-1.1}$ </td><td> $H_{0-1.1}$ rejected ( $p < 0.001$ ) in favor of  $H_{a-1.1}$ , based on the results of Mann-Whitney  $U$  test. The accuracy was significantly higher when using OH compared to the C.</td></tr><tr><td> $H_{0-1.2}$ </td><td> $H_{0-1.2}$ rejected ( $p < 0.001$ ) in favor of  $H_{a-1.2}$ , based on the results of independent t-test. Participants that used OH performed their work significantly faster when compared to the C.</td></tr><tr><td> $H_{0-1.3}$ </td><td> $H_{0-1.3}$ rejected ( $p < 0.001$ ) in favor of  $H_{a-1.3}$ , based on the results of independent t-test. The efficiency was significantly higher when using OH compared to the C.</td></tr><tr><td> $H_{0-1.4}$ </td><td> $H_{0-1.4}$ rejected ( $p < 0.001$ ) in favor of  $H_{a-1.4}$ , based on the results of Mann-Whitney  $U$  test. The PEOU was significantly higher when using OH compared to the C.</td></tr><tr><td> $H_{0-2}$ </td><td> $H_{0-2}$ rejected ( $p < 0.001$ ) in favor of  $H_{a-2}$ , based on the results of Mann-Whitney  $U$  test. The PU was significantly higher when using OH compared to the C.</td></tr></table>

## 7.2. The implications of experiment's results

The implications of this study can be applied to both theory and practice as follows. Since the related work does not address the opacity as a measure of color, we believe that our research complements the existing studies. The most important theoretical implication of this study is the empirical validation that the usage of Opacity Highlights improves cognitive effectiveness of BPDs. As such, researchers are encouraged to examine the possibility of using Opacity Highlights instead of other mechanisms for increasing cognitive effectiveness of BPDs. Besides, using the Opacity Highlights does not require any modification in the existing BPDs, as is the case in related work (see Chapter 3). Finally, Opacity Highlights can be applied to other diagrammatic languages and domains as well (e.g. UML and EPC). In light of practical

## Table 9

Control of internal validity threats.

<table><tr><td>Factors that jeopardize internal validity</td><td>Actions taken to counteract the threats</td></tr><tr><td>Maturation</td><td>The duration of the experiment was limited to 45 min to minimize fatigue of the participants. The order in which BPDs were assigned was randomized to ensure that the results were not impacted by the sequence in which participants received BPDs.</td></tr><tr><td>Instrumentation</td><td>The measuring instruments (see Chapter 5.2.3) were not changed during the experimental execution.</td></tr><tr><td>Statistical regression</td><td>The participants of the experiment were randomly assigned to both groups. As such, their previous knowledge about BPDs did not influence their assignment to a specific group.</td></tr><tr><td>Selection</td><td>All participants had equal chance of being assigned to the treatment or control group.</td></tr><tr><td>Experimental mortality</td><td>All participants made it through the entire experiment in both treatment and control groups.</td></tr></table>

Please cite this article as: G. Jošt, et al., Improving cognitive effectiveness of business process diagrams with opacity-driven graphical highlights, Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.09.003

implications, our prototype software solution was being recognized by participants as useful. Therefore, software vendors could integrate our solution into the existing tools for business process modeling and representation. This could lead to easier diagrammatic communication and faster as well as more accurate decision-making when using BPDs in both business and social sectors. We can assume that our solution will have an effect on both citizens and business analysists within the public and Government-to-Customer (G2C) processes.

## 7.3. Future activities

We will continue our work in the following directions. Firstly, we will investigate how different levels of opacity influence the cognitive effectiveness of BPDs. Secondly, even though the related work showed that using highlighting pattern does not significantly influence experts, we will perform a case study within the enterprise environment. Thirdly we plan to apply Opacity Highlights to the most commonly used business process modeling languages. Fourthly, as there is no reference framework addressing the categories and types of Opacity Highlights, we find it reasonable to further investigate and extend the current set of Opacity Highlights. Fifthly, we will conduct an experiment, where different approaches for increasing cognitive effectiveness will be compared. Finally, we plan to publish it in form of a free web-service, where users will be able to upload their BPDs and use our proposed set of Opacity Highlights. We also plan on informing software vendors of our solution, so they could integrate it in their existing products.

## 8. Conclusion

The main contribution of this paper is that it provides empirical insights about the impacts of applying Opacity Highlights to BPDs, in light of cognitive effectiveness as well as the perceived usefulness of tested prototype. The results from the study, which included 85 IT students, are as follows. Participants that used Opacity Highlights significantly outperformed those that used the conventional approach in all experi mental observations, namely accuracy, speed, efficiency and PEOU. Opacity Highlights also scored higher in the light of the perceived usefulness. We can conclude that using Opacity Highlights increases the cognitive effectiveness of BPDs while the corresponding prototype software solution is perceived as being useful by the experiment's participants. Our research supplements the related work, which states that the usage of color graphical highlights is perceived as useful and increases the ease of use. Moreover, because our solution does not interfere with existing approaches for improving cognitive effectiveness, researchers are encouraged to examine the possibility of applying Opacity Highlights to their work. Since BPDs are valuable organizational assets, which facilitate decision-making activities, we consider Opacity Highlights as a cognitive effective mechanism, which further simplifies those activities.

## Acknowledgments

The authors acknowledge the financial support from the Slovenian Research Agency (research core funding No. P2-0057).

Appendix A. The following two figures represents business process diagrams, which were investigated in our experimental proces  
![](/api/attachments/6UZPVPA8/fulltext/images/028182efdfecb4bc0b24ec9a0acb82c264fb3007d0d93d505f78f7fe7ae12fb6.jpg)  
Fig. 7. High complexity business process diagram.

![](/api/attachments/6UZPVPA8/fulltext/images/60b14cca00c10394586d773f9843534e674b19efc58c3498c68fcb6d57b19789.jpg)  
Fig. 8. Low complexity business process diagram

Please cite this article as: G. Jošt, et al., Improving cognitive effectiveness of business process diagrams with opacity-driven graphical highlights, Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.09.003

Appendix B. A list of questions regarding the high complexity business process diagram, which were used in the questionnaire is represented in the Table 10. The list of questions for the low complexity business process diagram was identical, except for the element labels

## Table 10

Sample questionnaire – high complexity business process diagram.

\# Questions regarding the business process diagram Answer the following questions: {true/false} 1 Is the document D05 an input for the task T38? 2 Is the document D10 an output of the task T28? 3 Is the task T06 performed immediately after a time delay in the process? 4 Does the task T11 have a deadline by which it has to be performed? 5 Does the task T16 send a message to the “Participant B” role? 6 Does the task T11 handle errors, if they occur during its execution? 7 Is task T06 performed between the tasks T22 and T68? 8 If the process starts with event E59, can the task T36 be performed? 9 If the process ends with event E56, can the task T83 be performed? 10 If the decision in G31 is always “Positive”, can the task T79 be performed? 11 If the task T51 exceeds the deadline, by which it has to be performed, can the task T68 be performed? 12 If an error occurs during the execution of task T83, can the task T50 be performed? 13 Is the document D18 an input for the tasks T46, T11 and T16?

## References

[1] M. Dumas, M. La Rosa, J. Mendling, H.A. Reijers, Fundamentals of Business Process Management, Springer-Verlag, Berlin Heidelberg, Berlin, Germany, 2013https:// doi.org/10.1007/978-3-642-33143-5.

[2] C.L. Citroen, The role of information in strategic decision-making, Int. J. Inf. Manag. 31 (2011) 493–501, https://doi.org/10.1016/j.ijinfomgt.2011.02.005.

[3] M. Trkman, J. Mendling, M. Krisper, Using business process models to better understand the dependencies among user stories, Inf. Softw. Technol. 71 (2016) 58–76, https://doi.org/10.1016/j.infsof.2015.10.006.

[4] O. Kopp, D. Martin, D. Wutke, F. Leymann, On the choice between graph-based and block-structured business process modeling languages, Modellierung Betrieblicher Informationssysteme (MobIS 2008), Stuttgart, Germany 2008, pp. 59–72.

[5] D. Moody, The “physics” of notations: toward a scientific basis for constructing visual notations in software engineering, IEEE Trans. Softw. Eng. 35 (2009) 756–779, https://doi.org/10.1109/TSE.2009.67.

[6] S. Smirnov, H.A. Reijers, M. Weske, A semantic approach for business process model abstraction, Proceedings of the 23rd International Conference on Advanced Information Systems EngineeringSpringer-Verlag, London, United Kingdom 2011, pp.497-511.https://doiorg/10.1007/978-3-642-21640-4.37

[7] K.B. Lassen, W.M.P. van der Aalst, Complexity metrics for workflow nets, Inf. Softw. Technol. 51 (2009) 610–626, https://doi.org/10.1016/j.infsof.2008.08.005

[8] H.A. Reijers, T. Freytag, J. Mendling, A. Eckleder, Syntax highlighting in business process models, Decis. Support. Syst. 51 (2011) 339–349, https://doi.org/10.1016/j.dss. 2010.12.013.

[9] R. Müller, A. Rogge-Solti, BPMN for healthcare processes, 3nd Central-European Workshop on Services and Their Composition ZEUS 2011, Karlsruhe, Germany 2011, pp. 65–72.

[10] G. Jošt, G. Polančič, Application of business process diagrams' complexity management technique based on highlights, Enterprise, Business-Process and Information Systems Modeling: 17th International Conference, BPMDS 2016, 21st International Conference, EMMSAD 2016, Held at CAiSE 2016, Ljubljana, Slovenia, June 13–14, 2016, ProceedingsSpringer International Publishing 2016, pp. 66–79, https://doi. org/10.1007/978-3-319-39429-9\_5.

[11] A. Pourshahid, D. Amyot, L. Peyton, S. Ghanavati, P. Chen, M. Weiss, A.J. Forster, Business process management with the user requirements notation, Electron. Commer. Res. 9 (2009) 269–316, https://doi.org/10.1007/s10660-009-9039-z.

[12] M. Kunze, A. Luebbe, M. Weidlich, M. Weske, Towards understanding process modeling – the case of the BPM academic initiative, Business Process Model and Notation: Third International Workshop, BPMN 2011, Lucerne, Switzerland, November 21–22, 2011. ProceedingsSpringer Berlin Heidelberg 2011, pp. 44–58, https://doi. org/10.1007/978-3-642-25160-3\_4.

[13] S. Smirnov, H.A. Reijers, M. Weske, T. Nugteren, Business process model abstraction: a definition, catalog, and survey, Distributed and Parallel Databases, 30, 2012, pp. 63–99, https://doi.org/10.1007/s10619-011-7088-5.

[14] J. Ghattas, P. Soffer, M. Peleg, Improving business process decision making based on past experience, Decis. Support. Syst. 59 (2014) 93–107, https://doi.org/10.1016/j. dss.2013.10.009.

[15] M. Chinosi, A. Trombetta, BPMN: an introduction to the standard, Computer Standards & Interfaces 34 (2012) 124–134http://dx.doi.org/10.1016/j.csi.2011.06.002

[16] G. Decker, F. Puhlmann, Extending BPMN for Modeling Complex Choreographies, On the Move to Meaningful Internet Systems 2007: CoopIS, DOA, ODBASE, GADA, and IS: OTM Confederated International Conferences CoopIS, DOA, ODBASE,

GADA, and IS 2007, Vilamoura, Portugal, November 25–30, 2007, Proceedings, Part ISpringer Berlin Heidelberg 2007, pp. 24–40, https://doi.org/10.1007/978-3- 540-76848-7\_4.

[17] D. Moody, What makes a good diagram? Improving the cognitive effectiveness of diagrams in IS development, Advances in Information Systems Development: New Methods and Practice for the Networked Society, Springer US, Boston, United States 2007, pp. 481–492, https://doi.org/10.1007/978-0-387-70802-7\_40.

[18] J. Cardoso, J. Mendling, G. Neumann, H.A. Reijers, A discourse on complexity of process models, Business Process Management Workshops: BPM 2006 International Workshops, BPD, BPI, ENEI, GPWW, DPM, semantics4ws, Vienna, Austria, September 4–7, 2006. ProceedingsSpringer Berlin Heidelberg 2006, pp. 117–128, https:// doi.org/10.1007/11837862\_13.

[19] M. La Rosa, A.H.M. ter Hofstede, P. Wohed, H.A. Reijers, J. Mendling, W.M.P. van der Aalst, Managing process model complexity via concrete syntax modifications, IEEE Trans. Ind. Inf. 7 (2011) 255–265, https://doi.org/10.1109/TII.2011.2124467

[20] L. Sánchez-González, F. García, J. Mendling, F. Ruiz, Prediction of business process model quality based on structural metrics (Conceptual Modeling – ER 2010 - 29th International Conference on Conceptual Modeling, Vancouver, BC, Canada, November 1–4, 2010. Proceedings), 2010 458–463, https://doi.org/10.1007/978-3-642- 16373-9\_35.

[21] G. Polančič, B. Cegnar, Complexity metrics for process models – a systematic literature review, Computer Standards & Interfaces 51 (2017) 104–117, https://doi.org/ 10.1016/j.csi.2016.12.003.

[22] D.L. Moody, Cognitive load effects on end user understanding of conceptual models: an experimental analysis, Advances in Databases and Information Systems: 8th East European Conference, ADBIS 2004, Budapest, Hungary, September 22–25, 2004. ProceedingsSpringer Berlin Heidelberg 2004, pp. 129–143, https://doi.org/10. 1007/978-3-540-30204-9\_9.

[23] D. Moody, J. van Hillegersberg, Evaluating the visual syntax of UML: an analysis of the cognitive effectiveness of the UML family of diagrams, Software Language Engineering: First International Conference, SLE 2008, Toulouse, France, September 29- 30, 2008. Revised Selected PapersSpringer Berlin Heidelberg 2009, pp. 16–34, https://doi.org/10.1007/978-3-642-00434-6\_3.

[24] D.L. Moody, P. Heymans, R. Matulevičius, Visual syntax does matter: improving the cognitive effectiveness of the i\* visual notation, Requir. Eng. 15 (2010) 141–175, https://doi.org/10.1007/s00766-010-0100-1.

[25] D. Moody, Complexity effects on end user understanding of data models: an experimental comparison of large data model representation methodsProceedings of the Tenth European Conference on Information Systems (ECIS’2002), Gdańsk, Poland 2002, pp. 482–496http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.98. 8983&amp:ren=rep1&amp:type=pdf

[26] V. Gruhn, R. Laue, Reducing the cognitive complexity of business process models2009 8th IEEE International Conference on Cognitive Informatics, IEEE 2009, pp. 339–345, https://doi.org/10.1109/COGINF.2009.5250717.

[27] N. Genon P. Heymans D. Amvot, Analysing the cognitive effectiveness of the BPMN 2.0 visual notation, Software Language Engineering: Third International Conference, SLE 2010, Eindhoven, The Netherlands, October 12-13, 2010, Revised Selected PapersSpringer Berlin Heidelberg 2011, pp. 377–396, https://doi.org/10.1007/978- 3-642-19440-5\_25

[28] Object Management Group (OMG), Business Process Model and Notation (BPMN) Version 2.0 Business, 50 2011.170 https://doi,org/10.1007/s11576-008-0096-z

[29] D. Gagne, A. Trudel, Time-BPMN2009 IEEE Conference on Commerce and Enterprise Computing, IEEE 2009, pp. 361–367. https://doi,org/10.1109/CEC.2009.71.

[30] T.F. Kummer, J. Recker, J. Mendling, Enhancing understandability of process models through cultural-dependent color adjustments, Decis. Support. Syst. 87 (2016) 1–12, https://doi.org/10.1016/j.dss.2016.04.004.

[31] A. Glassner, Interpreting alpha, Journal of Computer Graphics Techniques (JCGT). 4 (2015) 30–44http://jcgt.org/published/0004/02/03/.

[32] ITS Project Methodology (Process Improvement Interview Questions), http://its. umich.edu/about/methodology 2010, Accessed date: 3 December 2016.

[33] P. Harmon, C. Wolf, Business Process Modeling Survey, http://www.bptrends.com/ bpt/wp-content/surveys/Process\_Modeling\_Survey-Dec\_11\_FINAL.pdf 2011, Accessed date: 3 December 2016.

[34] W.R. King, J. He, A meta-analysis of the technology acceptance model, Inf. Manage. 43 (2006) 740–755, https://doi.org/10.1016/j.im.2006.05.003.

[35] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of infor mation technology, MIS Q. 13 (1989) 319–340, https://doi.org/10.2307/249008

[36] B. Albert, T. Tullis, D. Tedesco, Beyond the Usability Lab, 1st ed Morgan Kaufmann, Boston, United States, 2010https://doi.org/10.1016/B978-0-12-374892-8.00006-5.

[37] E. Rolón, L. Sánchez, F. García, F. Ruiz, M. Piattini, D. Caivano, G. Visaggio, Prediction models for BPMN usability and maintainability2009 IEEE Conference on Commerce and Enterprise Computing, IEEE, Vienna, Austria 2009, pp. 383–390, https://doi.org/ 10.1109/CEC.2009.53.

[38] R. Petrusel, J. Mendling, H.A. Reijers, et al., Decis. Support. Syst. 96 (2017) 1–16http://dx.doi.org/10.1016/j.dss.2017.01.005.

[39] L. Sánchez-González, F. García, F. Ruiz, J. Mendling, Quality indicators for business process models from a gateway complexity perspective, Inf. Softw. Technol. 54 (2012) 1159–1174, https://doi.org/10.1016/j.infsof.2012.05.001.

[40] S.B. Green, N.J. Salkind, Using SPSS for Windows and Macintosh: Analyzing and Understanding Data, 5th ed Prentice Hall, Upper Saddle River, New Jersey, United States, 2007.

[41] P. Legris, J. Ingham, P. Collerette, Why do people use information technology? A critical review of the technology acceptance model, Inf. Manage. 40 (2003) 191–204, https://doi.org/10.1016/S0378-7206(01)00143-4.

[42] D.T. Campbell, J.C. Stanley, Experimental And Quasi-Experimental Designs For Research, 1st ed. Wadsworth Publishing, Belmont, California, United States, 1963 doi:Y-BBS-IO 09 08.

Gregor Jošt received BSc in Computer Science & Informatics from the University of Maribor, Slovenia in 2010. Currently he is a Ph.D. student and a teaching assistant at the University of Maribor. His main research interests include empirical investigations of Process Modeling and Automation, Cloud Computing, Web technologies and Mobile solutions. He has participated in several research and applied projects and appeared as an author or co-author in several scientific and conference papers.

Jernej Huber received BSc in Computer Science & Informatics from the University of Maribor, Slovenia in 2009. Currently he is a Ph.D. student and a teaching assistant at the University of Maribor. His main research interests include empirical investigations of Process Modeling and Metrics, Mobile solutions and E-Commerce. He has participated in several researches and applied projects and appeared as an author or co-author in several scientific and conference papers.

Marjan Heričko is a full professor at the Institute of Informatics. He is the head of the In formation systems laboratory and Deputy Head of the Institute of informatics. He received his PhD in Computer Science from University of Maribor in 1998. His main research interests include all aspects of information systems development, software and service engineering, agile methods, process frameworks, software metrics and business process modelling. Dr. Heričko has been a project or work co-ordinator in several applied projects project or work co-ordinator in several international research projects and committee member and chair of several international conferences

Gregor Polančič is an assistant professor in Computer Science & Informatics at University of Maribor, Slovenia. He received his Ph.D. in Computer Science & Informatics from the same university in 2008. His main research interests include empirical investigations of Business Process Modeling and Management, IT management, IT acceptance, e-communication and e-collaboration. He has appeared as an author or co-author in more than 20 peer-reviewed scientific journals. In all, his bibliography contains more than 250 records.
