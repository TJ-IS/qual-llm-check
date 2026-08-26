---
otero_id: 19778
otero_key: "SVPUYNM9"
title: "How do individuals decide which modeling scripts to use during systems analysis and design?"
authors: "Mohammad Jabbari; Jan Recker; Peter Green"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113575"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# How do individuals decide which modeling scripts to use during systems analysis and design?

Mohammad Jabbari <sup>a,\*</sup>, Jan Recker <sup>b</sup>, Peter Green <sup>c</sup>

<sup>a</sup> Queensland University of Technology, School of Information Systems, Brisbane, Australia

<sup>b</sup> University of Hamburg, Hamburg Business School, Hamburg, Germany

<sup>c</sup> Queensland University of Technology, QUT Business School, Brisbane, Australia

## A R T I C L E I N F O

Keywords: Conceptual modeling Combined ontological completeness Ontological overlap Domain understanding Decision Representation theory

## A B S T R A C T

Because most information systems in real-world domains are complex, practitioners often use different types of conceptual modeling scripts to understand them. Modeling methods such as UML, for example, provide more than a dozen scripts for practitioners to use. We study how script readers decide which of several different scripts to use during systems analysis and design tasks. We carried out a free-simulation experiment to test how users select scripts based on two factors: combined ontological completeness and ontological overlap. We find that participants indeed decided to select more than one script to achieve a more complete domain representation. But, when they selected more than three scripts, they decided to remove scripts and reduce combined completeness to increase the clarity of the combined representation. Our results indicate that script readers prefer relatively less complete scripts with high levels of clarity over more complete, but more overlapping, script combinations. We detail the implications these findings have for the theory and the practice of conceptual modeling.

## 1. Introduction

A key activity in systems analysis and design is to develop and use representations, often graphical, of relevant features of the domain under examination [1]. These representations are called conceptual modeling scripts. Multiple types of scripts, often developed using different grammars, are usually used in combination [2]. For example, UML contains thirteen different grammars to design many different types of scripts, such as class diagrams, use case diagrams, activity di agrams, state diagrams, sequence diagrams, and others. BPMN 2.0 fea tures collaboration diagrams, process diagrams, and choreography diagrams. Several empirical studies indicate that IS professionals indeed often use multiple types of scripts in their analysis and design tasks [2–4]. They do so because IS have become ever more complex and any one script is not sufficient usually to represent all aspects of a system. When there is more than one modeling script available, IS professionals need to make a key decision: which script(s), among the available set of options, should they select for use in a task. Literature on decision making indicates that such decision making is an active process [5] that involves: 1) the identification of options, 2) the determination of ex pectations on each option, and 3) an expression of expected net value .

Surprisingly, however, research on how users decide to select and use multiple different scripts from a set of available options is very sparse. Studies about conceptual modeling abound [6], and they have investigated a wide variety of aspects. But they have almost exclusively focused on single modeling scripts or single modeling grammars, for example, how users comprehend scripts [7], whether visual cues added to script constructs affect their cognitive information processing per formance [8], how different symbol designs affect individuals’ ability to comprehend scripts [9], or how much domain understanding can be created from reading a single script [10].

We extend this literature. We designed and executed an experiment to study how script readers [11] decide which multiple available scripts to use to complete their analysis and design tasks. By script readers we refer to analysts and designers that interpret previously developed conceptual modeling scripts to make decisions or solve problems during systems analysis and design tasks, as opposed to script developers who build conceptual modeling scripts [11,12]. Addressing how script readers decide which modeling scripts to use is important because the decision which scripts to use can affect the communication between analysts, designers, and end users, and therefore improve early detection of systems analysis and design problems [13].

Through this work, we provide the first rigorous empirical evidence about the script selection decision. It is also the first direct test of Recker and Green’s [12] selection proposition. We proceed as follows. We re view relevant literature and then introduce Recker and Green’s [12] theory as the basis for our experimental hypotheses. Next, we describe how we designed and carried out our experiment, and then we discuss the results. Finally, we discuss theoretical and practical implications of our study, and its limitations.

## 2. Background

Using conceptual modeling scripts to support information systems analysis and design is a widespread practice in industry [3,14–16]. Scripts are used, for example, to configure enterprise systems [17], to redesign business processes [18], during auditing [19] and data ware house design [20], or in model-driven software engineering [4,21]. However, evidence also suggests that users normally use multiple scripts involving different grammars in these and other tasks, not just one script. For example, Dobing and Parsons [15] reported that 90% of UML users employ at least two different UML grammars in at least one-third of their projects. The use of multiple scripts is also common in process redesign. Recker [22] reported that over 30% of surveyed process mod elers access additional grammars when modeling business processes. Green, Rosemann, Indulska and Recker [23] reported that 80% of users of modeling tool environments selected and used multiple grammars in combination.

Multiple scripts are used for different reasons. Kim, Hahn and Hahn [24] suggested that multiple scripts are used to understand complex systems from different perspectives. For example, users may use different scripts such as entity relationship diagrams or UML Class dia grams to represent structural aspects while, to represent behavioral as pects of a domain, they use other scripts such as BPMN process models or UML Activity diagrams. Multiple scripts are also more common than thought during agile software development [25]. Gupta, Poels and Bera [26] demonstrate, for example, how using multiple scripts can reduce ambiguity in user stories and improve requirements engineering during agile development. These studies demonstrate that the use of multiple scripts is indeed prevalent. However, there is still a lack of under standing of how users decide which scripts to use together. The traditional argument on the selection of scripts mainly concerns selecting scripts based on the appropriate level of detail and task expectations [27]. For example, selecting a very simple script to communicate requirements with developers will be unrealistic, and in turn, would result in misleading requirements. On the other hand, selecting an overly com plex set of scripts to facilitate communication and understanding may lead readers to draw incorrect conclusions because it is generally harder to interpret complex scripts [28].

Few studies have focused on the decision-making process involved in selecting one script from multiple available scripts. For example, Fig and Recker [29] suggest that cognitive style and the nature of the task setting affect whether users will prefer a process presentation format over other formats such as text or structured text. Other studies report that practitioners often select those scripts that they feel are suitable to communicate with different stakeholders [3,30]. Users tend not to select scripts that are either difficult for all stakeholders to understand or that do not add sufficient additional value to justify their selection. For example, users often select use case diagrams for client verification while they select class diagrams for clarifying understanding of appli cation domains among technical members. The current literature sug gests that the choice of script depends on the usefulness of scripts as perceived by end users [15]. However, this literature focuses only on how users select one script over others. In contrast, we study how users select multiple different scripts based on how useful they perceive the scripts to be for a given problem.

## 3. Hypothesis development

There is a large literature on conceptual modeling that has provided guidelines for evaluating the quality of scripts and grammars. For example, structural frameworks have been proposed to guide conceptual modeling research [6,31,32], metrics have been developed and tested to evaluate and improve the quality of conceptual modeling scripts [33–35], and different theories and philosophical foundations of con ceptual modeling have been discussed [36–38].

Broad overviews of the conceptual modeling literature are available elsewhere [6,39]. Here, we focus on three main streams of work that are among the most widely pursued in this literature. One is informed by Moody’s research [35] on the visual syntax of conceptual modeling scripts and grammars. This line of research examines whether visual elements such as shapes or colors can make scripts more effective for users to understand [e.g., 9,40,41]. A second stream of work builds on Guizzardi’s research on ontological foundations of conceptual modeling [42]. This line of work explores whether following ontological guide lines such as concept isomorphism or part-whole relations helps users to create better conceptual modeling scripts [43,44]. The third stream of research has built on Wand and Weber’s ideas about representation and ontological analysis [45] to conduct research that explores how scripts can be constructed with grammars such that users maximize how much domain understanding they can glean from these scripts [10,46].

Each of these research streams has provided much needed insights into the quality and practice of conceptual modeling. However, the theoretical ideas pursued have had a strong focus on single grammars or single scripts. For example, researchers interested in visual syntax ele ments have explored how the use of a script can be improved by addi tional notation elements such as colors [8]. Additionally, researcher interested in ontological guidelines have explored how one grammar, such as UML, can be made better by enriching it with ontologically guided concepts [47]. Likewise, in empirical work that involves multiple grammars or scripts, most of the studies compare scripts to evaluate which one is “better” (e.g., [48]).

There is only one theoretical framework we are aware of that focuses explicitly on factors relevant to multiple scripts, not just one, which we could use to hypothesize about how individuals might decide which modeling scripts to use in combination. The theory of combined onto logical completeness and overlap [12] provides logic about decisions involved in the use of multiple scripts by users. It argues that the use of a particular combination of scripts will depend on two factors: the com bination’s Combined Ontological Completeness (COC) and Ontological Overlap (OO):

• COC refers to the level of representational coverage a set of scripts provides about some real-world phenomena;

• OO refers to the level of overlap of the same concepts represented across a set of scripts.

We point out that COC and OO are factors that measure the completeness and clarity of scripts, not grammars. Any one script can contain none, some, or all grammatical constructs from a grammar, and any one script may have a need for additional representations that are not provided by a chosen grammar. For example, the UML use case modeling grammar does not offer a grammatical construct to represent things [50]. However, it offers several constructs to represent classes of things. Whether or not one or more scripts contain, or ought to contain, representations for certain classes of things is a question of the scripts developed using one or more grammars.

Recker and Green [12] developed a selection proposition that is the basis for the study reported in this paper. In this proposition, they conjectured that, first, users will select multiple scripts to maximize the representational coverage of some relevant real-world phenomena . Users always have a desire to select multiple scripts because no one script can represent all potentially relevant aspects of a real-world phenomenon, according to theory [23,50,51]. Therefore, users will use multiple scripts in combination to overcome ontological deficits in a single script and to maximize combined ontological completeness across multiple scripts. Second, users will also seek to minimize overlap in the concept representations across the script combination to keep the coverage as simple and clear as possible [36,45]. Based on these two considerations, Recker and Green [12] suggest that if a user has access to a variety of conceptual scripts that can potentially assist with achieving goals of a model-based task, the user will decide on a combination of conceptual scripts with the aim of achieving maximal ontological completeness. However, they will decide to add scripts to their selection only while the level of overlap in the combination remains “bearable”, that is, when the level of confusion does not become too high.

To test the selection proposition, we operationalize it in two hy potheses: First, the use of conceptual modeling scripts occurs as part of a particular task e.g., gaining an understanding of a domain and a decision about which script or scripts combination to use is thus driven by per formance outcome expectations [12]. On the assumption that several scripts about a real-world domain are available, the selection step con cerns which script(s) would be chosen by users to maximize the level of domain understanding they can generate to complete an upcoming task. Recker and Green [12] suggest that readers will select a set of scripts from a number of available scripts to increase the ontological completeness of representation of some focal real-world phenomena because any one script will have construct deficit. Users will do so because they have a desire to have a more complete representation that provides all relevant information.

Users make decisions about which script(s) to use based on an evaluation of the potential value of alternatives to achieve certain task goals [52]. The outcome expectation of using scripts is to generate a complete and clear understanding of real-world phenomena [53]. Users create a mental model of real-world phenomena based on the informa tion directly presented in the scripts [54]. Obtaining a more complete mental model demands more information. Given a first selected script is deemed deficient in terms of allowing the user to achieve an adequate understanding of the model-based task, users will choose an additional script in which the selected script provides users with more information compared to the alternatives. Therefore, given a set of scripts, users will select additional scripts for task completion such that the ontologica completeness of the script combination is maximized. Hence, we pro pose the first hypothesis:

Hypothesis One. Given users start with a particular script, they will go on to select additional script(s) to maximize the ontological completeness of the script combination.

By increasing the level of ontological completeness of the represen tation of a domain, more information will be available for users to create and enhance a mental model of the represented real-world phenomena. On the other hand, through selecting additional script(s), the level of ontological overlap between scripts may also increase [55]. Increasing ontological overlap between scripts will decrease the clarity of repre sentation of the real-world phenomena because several representations are in the set of scripts that represent the same real-world phenomenon [45]. It is likely that higher levels of ontological overlap will lead to confusion and misunderstanding because users need to identify over lapping constructs and reconcile their meaning. The increase in the level of ontological overlap across scripts will also increase the complexity of the representation of the domain [28]. Therefore, while script readers will have a desire to add more information, after a certain point, users will avoid selecting additional scripts to manage the level of ontological overlap in the representation. In other words, we argue that script readers will try to maximize completeness but also follow the law of parsimony – they will seek the least number of different scripts with the most explanatory power to represent the real-world domain of interest. In turn, we argue that script readers will use additional scripts to reach a maximal level of completeness only if adding one more script will in crease the level of combined completeness and it is accompanied by a minimal level of increase in the overlap.

We also argue that developing a mental model is limited by the capability of individuals’ working memories. That is, an increase in ontological overlap between scripts will require additional reasoning to develop understanding. But, it will also increase the cognitive load [56]. The burden on the limited capacity of working memory can be reduced by using scripts that present multiple constructs that can be interpreted as a single element [57]. Thus, we argue that script readers will not select an additional script if adding another script only increases the ontological overlap. Hence, we propose:

Hypothesis Two. Given participants start their model-based task with a particular modeling script, they will select those additional script(s) that add/ s minimally to the level of ontological overlap in the resulting script combination.<sup>1</sup>

## 4. Research method

To the best of our knowledge, this work is the first study to test Recker and Green’s [12] selection proposition. To maximize internal validity, we therefore carried out a laboratory experiment to evaluate how scripts’ attributes affect readers’ selection of a combination of scripts.

## 4.1. Experimental design

Our study followed a free-simulation design [58]. In this design, subjects are placed in a controlled environment where they are free to behave (within the required boundaries of the study, e.g., the prescribed tasks) and they are asked to make choices as they see fit, thus allowing values of the independent variables to range over the natural range of the subjects’ experiences. No experimental treatments are provided. In our case, we placed participants in a controlled environment (computer lab) where they were given four different types of script and were free to decide which script or script combination to select that could help them to achieve a set of tasks presented to them.

## 4.1.1. Measures

We employed two independent variables and one dependent vari able. The two independent variables measured, first, the level of COC an additional script added to a set of one or more scripts, and second, the level of OO an additional script added. The dependent variable measured whether users selected a combination with maximal COC and minimal OO,<sup>2</sup> compared to any other available options.<sup>3</sup> Therefore, our dependent variable was a binary variable computed as:

Yes = 1 Whether the combination of scripts exhibited maximal COC and minimal OO No = 0

To capture the decision process and measure the selection choice(s), we also captured: (1) the types of script(s) selected by participants, and (2) the number of script(s) selected into the script combinations by participants during the selection process.

## 4.1.2. Materials

As a real-world case, we selected the “High Peak Bicycles” rental shop. The case features concepts, such as customer, bicycle, rent, and return. It was drawn from a standard systems analysis and design text book because the textbook featured a wide selection of different scripts for this case [59]. We developed a use case diagram, a class diagram, an activity diagram, and a state machine diagram (Table 1).

We developed four scripts, each constructed with a different UML grammar. We chose UML diagrams for several reasons. First, UML is a well-used conceptual modeling method with widespread adoption in practice [14,16]. Second, UML provides a wide variety of modeling scripts, each of which conveys different information [15]. Third, a substantial body of research has analyzed the relevant grammatical constructs of UML based on Wand and Weber’s representation theory [e.

g., 51, 60, 61, 62]. In turn, we could draw on established analyses to evaluate the levels of COC and OO. These script types were chosen for three reasons: First, together they specify a system’s purpose, structure, function, and behavior [63]. Second, these four diagrams are the most widely used UML diagrams IS professionals use in practice [3,15]. Third, they differ in ontological completeness and clarity [e.g., 51, 60, 61, 62], so participants can have different combinations with meaningful dif ferences in the levels of COC and OO. To manipulate our treatment variables, we performed an interpretation mapping [45] to analyze the representations offered by any one script in a given combination of scripts. That is, we mapped the constructs represented in each script to ontological constructs that describe things in the real-world [45]. We then conducted analyses to establish the levels of COC and OO for any possible combinations. Details and results of the interpretation mapping are available in Appendix A.

## 4.1.3. Tasks

As the task setting in our experiment, we decided to simulate typical transfer problem-solving tasks that systems analysts and designers are likely to face in their work. Transfer tasks examine users’ ability to use the knowledge gained from reading a combination of scripts, integrate them with their own prior knowledge, and develop creative solutions based on their mental model of how the domain works [64]. We defined two transfer problem-solving tasks (task definitions are available in Appendix B): a) to identify reasons for a stated problem in the domain, and b) to suggest solutions for a problem in the domain. Both tasks resemble common activities undertaken by professional analysts and designers [65–67]. To solve the first task, users had to understand and integrate different perspectives of the domain to be able to find reasons for the given problem. To solve the second task, users had to evaluate and compare how different perspectives are related to one another, then provide solutions associated with them. Our focus in the experiment was then to understand how users would make selections about scripts to use in the process of completing these problem-solving tasks, not their performance in the tasks themselves.

Table 1  
Scripts representing the High Peak Bicycles case.  
![](/api/attachments/SVPUYNM9/fulltext/images/e7337cd578ec969d8a4d9ce88beb7711d3c4b1af60f8577f17e450039d88a67a.jpg)

## 4.1.4. Covariates

To mitigate the impact of potential exogenous factors and to evaluate rival hypotheses throughout the experiment, we measured several control variables, in particular individual difference factors [68]. We operationalized individual differences by examining participants’ prior experience in conceptual modeling and their familiarity with the scripts used in the experiments. The rationale was to ensure that participants had experience with using relevant scripts and to evaluate their levels of experience [29]. Familiarity with scripts was also used as a potential exogenous variable, which could affect the usage of a script [29,69]. To that end, we adopted an existing script familiarity test [29].

## 4.1.5. Procedures

The experiment involves four steps. First, participants started with a pre-test that collected their demographic information and UML famil iarity levels. The second step was a short tutorial introduced the basics of a use case diagram, class diagram, state machine diagram, and activity diagram. No time limitation was placed on the tutorial and performing the tasks. In the third step, the free-simulation experiment for script selection began. In this step, participants were given two problemsolving tasks. In the next step, participants were provided with a use case diagram, class diagram, state machine diagram, and an activity diagram presenting the High Peak Bicycle case and they were asked to make selection decisions for the two problem-solving tasks [29].

We modeled the selection procedure as follows: Participants were provided with the problem-solving tasks and they saw which types of scripts were available to use but could not view the scripts. To view a script, participants had to choose the script to be included in their se lection at that point. Participants were free to start with any script. They could continue to add scripts to their selections if they felt they needed more scripts to be able to answer the questions. However, the selection of scripts was stepwise. In each step, participants were asked to either.

(a) confirm their present selection and proceed to complete the tasks, if they felt that the selected script(s) provided enough informa tion to accomplish the tasks, or

(b) select an additional script if they needed to do so.

In the latter case, the problem-solving questions, and the remaining script types available for selection were displayed again, and partici pants were again asked to choose an additional script or else to proceed to complete the tasks. These steps were repeated until participants confirmed their selection and proceeded to completing the tasks. In case participants had selected all four available scripts, they were asked whether they felt they could complete the tasks using all four scripts, or if they were not sure they could answer the questions (as an exit option).

After completing the presented problem-solving tasks with the se lection of scripts they preferred, as a last step in the experiment, par ticipants were asked to identify which script(s) they would like to remove if they had an opportunity to remove a script, or which script they felt were not useful in answering the questions. These measures allowed us to gather data for control checks and post-hoc analyses. Participants were also asked to rate the extent to which they relied on the information in each script they selected, their own knowledge, and the extent to which they made assumptions in completing the two problem-solving tasks. Questions and measurement items are available in Appendix B. This procedure ensured that participants only used in their tasks the scripts that they selected, and it allowed us to collect data to examine potential learning effects from selecting and unselecting scripts. It also enabled us to track whether participants compromised the levels of COC or OO in dependence on their present selection.

## 4.2. Participants

The target population for the experiments comprised users of con ceptual modeling scripts. The participants of this study were 131 un dergraduate students in a large university in Australia who completed courses related to systems analysis and design and conceptual modeling of real-world domains. Students were regarded as reasonable proxies fo junior working experts to make up the sample for this study for three reasons. First, prior studies have found little difference in performance between students and junior professionals [70]. Second, this research was relevant to the students who passed UML-related courses because they had covered the requirements of analysis, communication, system design, and modeling concepts. Finally, using students is common in conceptual modeling research [39], which allows for comparability of results. Participation was voluntary and remuneration through in centives was provided for participants in the study. The experiment was conducted using an online experimentation system and performed in university computer labs. It was monitored to ensure that individuals completed the experiment independently.

## 5. Data analysis

## 5.1. Preliminary tests

Our data analyses began with screening the data for its conformance with the assumptions of the designed tests. Table 2 presents descriptive statistics about our sample. We then assessed reliability and validity of the modeling familiarity measures through an exploratory factor anal ysis implemented in IBM SPSS Statistics 22. The results of the factor analyses indicated the modeling familiarity test measures were reliable (Cronbach’s Alpha was 0.78) and loaded appropriately (factor loading of 0.77).

## 5.2. Hypotheses testing

One hundred and seven (107) of the one hundred and thirty-one (131) participants (82%) selected more than one type of script. Only twenty-four (24) of the 131 participants (18%) selected one script to achieve the goals of the tasks in the experiment. Table 3 summarizes this

Table 2  
Descriptive statistics.

<table><tr><td>Constructs</td><td></td><td>Modeling familiarity</td><td>Diagram familiarity</td><td>Domain familiarity</td></tr><tr><td></td><td>Scale</td><td>1-7</td><td>Count.</td><td>1-7</td></tr><tr><td rowspan="2">Group A</td><td>M</td><td>4.48</td><td>2.42</td><td>4.09</td></tr><tr><td>SD</td><td>0.81</td><td>1.56</td><td>1.21</td></tr><tr><td rowspan="2">Group B</td><td>M</td><td>3.92</td><td>1.81</td><td>3.77</td></tr><tr><td>SD</td><td>1.03</td><td>1.3</td><td>0.96</td></tr><tr><td rowspan="2">Group C</td><td>M</td><td>4.14</td><td>1.91</td><td>3.88</td></tr><tr><td>SD</td><td>0.99</td><td>1.19</td><td>1.36</td></tr><tr><td rowspan="2">Group D</td><td>M</td><td>4.18</td><td>2.06</td><td>3.94</td></tr><tr><td>SD</td><td>0.91</td><td>1.37</td><td>1.46</td></tr></table>

Table 4  
Table 3  
Frequency of participants and the number of scripts in combination.

<table><tr><td>One script</td><td>Two scripts</td><td>Three scripts</td><td>Four scripts</td><td>All</td></tr><tr><td>24</td><td>31</td><td>41</td><td>35</td><td>131</td></tr><tr><td>18.32%</td><td>23.66%</td><td>31.3%</td><td>26.72%</td><td>100%</td></tr></table>

information.

## 5.2.1. Selection of a second script

Participants were free to start selecting any script they desired. Once they started to select a second script, we were able to evaluate if the COC and OO affected the selection of the additional scripts. Therefore, we started by evaluating the selection of a second script. Table 4 shows the descriptive statistics of the number of participants and the types of script they selected as the first and second choices. As presented in Table 4, participants selected a second script that added almost three units (2.84) of ontological completeness, on average, to the representational coverage of the script combination. The results of the correlation matrix indicate that the selection of the second script had a statistically sig nificant positive correlation with the level of COC added by the script (p = 0.00, Pearson Correlation = 0.72), while it also had a statistically significant but negative correlation with the level of OO added by the script (p = 0.00, Pearson Correlation = − 0.36). The correlations be tween constructs are presented in Table 5, with p-values in parentheses.

We used logistic regression analysis to test the predictors of the se lection of the second script (DV = 1, the selected scripts have maximal COC and minimal OO; DV = 0, otherwise) using the level of COC and the level of OO added by the second script, familiarity with the selected script, modeling familiarity, and familiarity with the domain as cova riates. The results of model fit, as presented in Table 6, suggest that between 59.3% and 79.4% of the variation in selecting to use a second script can be explained by the set of independent variables [71]. We ran hierarchical logistic regression analysis without (model one), and with, the COC and OO (model two) as factors. The results presented in Table 6 suggest that the ability of the model to predict the selection of a second script was higher for model two.

The Wald test [71] also supports that the level of COC added by the second script $( \beta = 4 . 0 1 , p = 0 . 0 0 )$ and the level of OO added by the second script $( \beta = - 4 . 2 2 , p = 0 . 0 1 )$ explain the selection of the script to

Frequency and descriptive statistics for second script selection.

<table><tr><td>Constructs</td><td>Mean</td><td>SD</td></tr><tr><td>Domain Familiarity</td><td>3.43</td><td>1.38</td></tr><tr><td>Modeling Familiarity</td><td>4.19</td><td>0.91</td></tr><tr><td>Familiarity with Selected Diagram</td><td>0.41</td><td>0.49</td></tr><tr><td>Level of COC Added by the Second Script</td><td>2.84</td><td>1.23</td></tr><tr><td>Level of OO Added by the Second Script</td><td>1.95</td><td>0.57</td></tr></table>

<table><tr><td>Started Script</td><td># (%)</td><td>Second Script</td><td># (total)</td></tr><tr><td rowspan="4">Script A) Use Case Diagram</td><td rowspan="4">47 (35.88)</td><td>Script B) Class Diagram</td><td>10 (19)</td></tr><tr><td>Script C) State Machine Diagram</td><td>9 (22)</td></tr><tr><td>Script D) Activity Diagram</td><td>22 (36)</td></tr><tr><td>None</td><td>6 (24)</td></tr><tr><td rowspan="4">Script B) Class Diagram</td><td rowspan="4">16 (12.21)</td><td>Script A) Use Case Diagram</td><td>5 (30)</td></tr><tr><td>Script C) State Machine Diagram</td><td>1 (22)</td></tr><tr><td>Script D) Activity Diagram</td><td>7 (36)</td></tr><tr><td>None</td><td>3 (24)</td></tr><tr><td rowspan="4">Script C) State Machine Diagram</td><td rowspan="4">19 (14.5)</td><td>Script A) Use Case Diagram</td><td>6 (30)</td></tr><tr><td>Script B) Class Diagram</td><td>3 (19)</td></tr><tr><td>Script D) Activity Diagram</td><td>7 (36)</td></tr><tr><td>None</td><td>3 (24)</td></tr><tr><td rowspan="4">Script D) Activity Diagram</td><td rowspan="4">49 (37.40)</td><td>Script A) Use Case Diagram</td><td>19 (30)</td></tr><tr><td>Script B) Class Diagram</td><td>6 (19)</td></tr><tr><td>Script C) State Machine Diagram</td><td>12 (22)</td></tr><tr><td>None</td><td>12 (24)</td></tr></table>

## Table 5

Construct correlation matrix for selection of second script.

<table><tr><td></td><td>Constructs</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>Domain Familiarity</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">2</td><td>Modeling</td><td>0.17</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>Familiarity</td><td>(0.07)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">3</td><td rowspan="2">Familiarity with the Selected Script</td><td>-0.15</td><td>0.04</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>(0.12)</td><td>(0.67)</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">4</td><td rowspan="2">Level of COC Added by the Second Script</td><td>-0.16</td><td>-0.09</td><td>0.08</td><td>1.00</td><td></td><td></td></tr><tr><td>(0.10)</td><td>(0.38)</td><td>(0.43)</td><td></td><td></td><td></td></tr><tr><td rowspan="2">5</td><td rowspan="2">Level of OO Added by the Second Script</td><td>0.03</td><td>-0.01</td><td>0.20</td><td>-0.13</td><td>1.00</td><td></td></tr><tr><td>(0.79)</td><td>(0.89)</td><td>(0.04)</td><td>(0.18)</td><td></td><td></td></tr><tr><td rowspan="2">6</td><td rowspan="2">DV (based on maximal COC and minimal OO)</td><td>-0.05</td><td>-0.01</td><td>-0.07</td><td>0.72</td><td>-0.36</td><td>1.00</td></tr><tr><td>(0.61)</td><td>(0.91)</td><td>(0.50)</td><td>(0.00)</td><td>(0.00)</td><td></td></tr></table>

## Table 6

Hierarchical logistic regression for the selection of second script.

<table><tr><td></td><td>B</td><td>S.E.</td><td>Wald</td><td>Sig.</td><td>Exp (B)</td></tr><tr><td colspan="6">Model One</td></tr><tr><td>Domain Familiarity</td><td>-0.09</td><td>0.15</td><td>0.38</td><td>0.54</td><td>0.91</td></tr><tr><td>Modeling Familiarity</td><td>0.01</td><td>0.22</td><td>0.00</td><td>0.98</td><td>1.01</td></tr><tr><td>Familiarity with Selected Script</td><td>-0.31</td><td>0.40</td><td>0.60</td><td>0.44</td><td>0.73</td></tr><tr><td>Constant</td><td>0.21</td><td>1.00</td><td>0.04</td><td>0.84</td><td>1.23</td></tr><tr><td colspan="6">Model Two</td></tr><tr><td>Domain Familiarity</td><td>-0.12</td><td>0.26</td><td>0.21</td><td>0.65</td><td>0.89</td></tr><tr><td>Modeling Familiarity</td><td>0.74</td><td>0.43</td><td>2.97</td><td>0.09</td><td>2.09</td></tr><tr><td>Familiarity with Selected Script</td><td>-0.52</td><td>0.77</td><td>0.45</td><td>0.50</td><td>0.60</td></tr><tr><td>Level of COC Added by the Second Script</td><td>4.01</td><td>1.13</td><td>12.63</td><td>0.00</td><td>54.93</td></tr><tr><td>Level of OO Added by the Second Script</td><td>-4.22</td><td>1.71</td><td>6.06</td><td>0.01</td><td>0.02</td></tr><tr><td>Constant</td><td>-8.23</td><td>3.20</td><td>6.63</td><td>0.01</td><td>0.00</td></tr></table>

<table><tr><td></td><td>Model One</td><td>Model Two</td></tr><tr><td>Chi-square</td><td>2.99</td><td>3.85</td></tr><tr><td>-2 Log Likelihood</td><td>146.34</td><td>50.93</td></tr><tr><td>Cox &amp; Snell R Square</td><td>0.01</td><td>0.59</td></tr><tr><td>Nagelkerke R Square</td><td>0.01</td><td>0.79</td></tr></table>

achieve the maximal COC and minimal OO in the combination. In line with hypotheses one and two. the results indicate that the more COC the second script added to the combination, the more likely it was that the participants would select the script. However, the negative beta value for the level of OO the script added to the combination indicates that the more OO the script added, the less likely a user was to select that script to add to the combination.

## 5.2.2. Selection of a third script

Based on the data presented in Table 3, 76 participants selected a third or a fourth script to add to the combination. We evaluated the determinant factors for selection of a third script for the combination of scripts. Table 7 presents the correlations between the factors. In line with the results for the selection of a second script, the correlation matrix indicates that the selection of a third script had a statistically significant positive correlation with the level of COC added by the third script $( p = 0 . 0 0$ . Pearson Correlation = 0.63). However, the level of OO had a statistically insignificant (positive) $( p = 0 . 1 7 ;$ , Pearson Correlation = 0.21) correlation to the selection of a third script.

To test how the levels of COC and OO added by the third script could predict the selection of a third script, we again estimated hierarchical logistic regression models. As presented in Table 8, and similar to the selection of the second script, the model with ontological factors was stronger in explaining the variations in the selection of the third script

Table 7  
Correlation matrix for the selection of the third script.

<table><tr><td></td><td>Constructs</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>Domain Familiarity</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Modeling Familiarity</td><td>0.14(0.22)</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Familiarity with the Selected Script</td><td>0.001(1.00)</td><td>0.17(0.14)</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>4</td><td>Level of COC Added by the Third Script</td><td>-0.03(0.79)</td><td>-0.12(0.32)</td><td>0.14(0.22)</td><td>1.00</td><td></td><td></td></tr><tr><td>5</td><td>Level of COC Added by the Third Script</td><td>0.01(0.93)</td><td>-0.003(0.98)</td><td>-0.02(0.90)</td><td>-0.27(0.02)</td><td>1.00</td><td></td></tr><tr><td>6</td><td>DV (based on maximal COC and minimal OO)</td><td>-0.09(0.38)</td><td>-0.14(0.15)</td><td>0.19(0.13)</td><td>0.63(0.00)</td><td>0.21(0.17)</td><td>1.00</td></tr></table>

## Table 8

Hierarchical logistic regression for the third script selection

<table><tr><td></td><td>B</td><td>S.E.</td><td>Wald</td><td>Sig.</td><td>Exp(B)</td></tr><tr><td colspan="6">Model One</td></tr><tr><td>Domain Familiarity</td><td>-0.10</td><td>0.17</td><td>0.33</td><td>0.56</td><td>0.90</td></tr><tr><td>Modeling Familiarity</td><td>-0.43</td><td>0.27</td><td>2.59</td><td>0.11</td><td>0.65</td></tr><tr><td>Familiarity with Selected Script</td><td>1.27</td><td>0.60</td><td>4.45</td><td>0.04</td><td>3.55</td></tr><tr><td>Constant</td><td>2.25</td><td>1.22</td><td>3.40</td><td>0.07</td><td>9.53</td></tr><tr><td colspan="6">Model Two</td></tr><tr><td>Domain Familiarity</td><td>-0.18</td><td>0.33</td><td>0.29</td><td>0.59</td><td>0.84</td></tr><tr><td>Modeling Familiarity</td><td>-0.18</td><td>0.57</td><td>0.10</td><td>0.75</td><td>0.84</td></tr><tr><td>Familiarity with Selected Script</td><td>1.82</td><td>1.16</td><td>2.48</td><td>0.12</td><td>6.17</td></tr><tr><td>Level of COC Added by the Third Script</td><td>4.11</td><td>1.19</td><td>11.98</td><td>0.00</td><td>61.11</td></tr><tr><td>Level of OO Added by the Third Script</td><td>5.18</td><td>2.09</td><td>6.15</td><td>0.01</td><td>178.09</td></tr><tr><td>Constant</td><td>-0.18</td><td>0.33</td><td>0.29</td><td>0.59</td><td>0.84</td></tr></table>

<table><tr><td></td><td>Model One</td><td>Model Two</td></tr><tr><td>Chi-square</td><td>6.84</td><td>6.35</td></tr><tr><td>-2 Log Likelihood</td><td>97.74</td><td>32.99</td></tr><tr><td>Cox &amp; Snell R Square</td><td>0.07</td><td>0.60</td></tr><tr><td>Nagelkerke R Square</td><td>0.10</td><td>0.81</td></tr></table>

(dependent variable: whether the selected scripts have maximal COC and minimal OO).

Table 8 also shows the results of logistic regression to assess the impacts of covariates and the treatment variables on the selection of a third script. Based on the results of the Wald test. both the level of COC $( \beta = 4 . 1 1 , p = 0 . 0 0 )$ and the level ${ \mathrm { o f } } 0 0 ( \beta = 5 . 1 8 , p = 0 . 0 1 )$ a third script added to the combination had a statistically significant effect on the selection of the third script. However, unlike the selection of the second script, the level of OO added by the third script had a positive effect on the selection of the script. These results could be because participants were looking for redundant information to confirm their understanding while, at the same time, looking for additional unique, clarifying in formation. However, in selecting a third script, only four options out of 24 possible remaining options existed where script readers could select a script without adding OO. For any other option, a third selected script added at least one-unit level to the OO of the script combinations. Therefore, we conducted a post hoc analysis to investigate the selection of more than two scripts in more detail.

## 5.3. Post-hoc analysis

To better understand the behavior of participants in script selection, we looked at participants’ decision processes in terms of two questions: First, which scripts did they rely on in answering the questions? Second, did they remove any script/s from the combination they had already selected?

To answer these two questions, Table 9 shows the number of scripts participants initially selected and then which scripts they ended up using in combination to answer the problem-solving questions. As presented in Table 9, 76 participants selected three or four scripts. But only 18 par ticipants used all scripts they had selected in combination. 58 out of 76 participants (76%) who selected a third or fourth script removed at least one of the scripts they had selected. Out of 41 participants that selected three scripts initially, only nine participants used all three scripts in combination to answer the questions, while 32 participants removed one (25) or two (7) scripts. We also found that only two participants that selected four scripts ended up using all four scripts to answer the problem-solving tasks.

Seven participants mentioned that they were not sure whether they could answer the questions using all four scripts. If we remove those seven participants, 93% of the participants who selected all four scripts ended up using three or less scripts in combination to complete their tasks. Overall, as presented in Tables 3 and 9, out of 131 participants, seven participants (5.3%) could not answer the questions; two partici pants (1.5%) used four scripts in combination; 26<sup>4</sup> participants (19.9%) used three scripts in combination to answer the questions; and 96<sup>5</sup> participants (73.3%) used two or less scripts in combination. Table 10 shows the number of users and types of scripts selected and dropped. These findings indicate that participants often preferred to remove some scripts from the combination, and as a result decreased the level of OO of their selected combination before they proceeded to complete the tasks they were presented with.

## 6. Discussion

We used a free-simulation experiment to evaluate data in light of two hypotheses about how users decide how many and which scripts to use for a systems analysis and design task. Our findings are in line with hypothesis one. We found that users added an additional script if it added to the level of COC of the script (combination) they had selected at that point. Specifically, we found that the level of COC an additional script added to the combination had a statistically significant positive impact on the selection of the script. This finding could be interpreted as

## Table 9

Number of scripts selected and number of scripts they used in combination to answer the questions.

<table><tr><td>No. of scripts selected initially</td><td>No. of participants in total</td><td>No. of scripts finally used for tasks</td><td>Share of Participants</td><td>Most frequently used script combination</td></tr><tr><td rowspan="3">Three scripts</td><td rowspan="3">41</td><td>3</td><td>9</td><td>use case, class, and activity</td></tr><tr><td>2</td><td>25</td><td>activity and use case</td></tr><tr><td>1</td><td>7</td><td>activity</td></tr><tr><td rowspan="4">Four scripts</td><td rowspan="4">35</td><td>4</td><td>2 + 7</td><td>all four scripts</td></tr><tr><td>3</td><td>17</td><td>use case, state, activity</td></tr><tr><td>2</td><td>6</td><td>activity and state/use case</td></tr><tr><td>1</td><td>3</td><td>activity</td></tr></table>

Table 10  
Frequency of types of scripts.

<table><tr><td rowspan="2">Types of scripts</td><td colspan="3">Number of users</td></tr><tr><td>Selected</td><td>Dropped</td><td>Used</td></tr><tr><td>Use Case</td><td>99</td><td>26</td><td>73</td></tr><tr><td>Class</td><td>67</td><td>25</td><td>42</td></tr><tr><td>State Machine</td><td>73</td><td>21</td><td>52</td></tr><tr><td>Activity</td><td>110</td><td>4</td><td>106</td></tr></table>

suggesting that script readers desire a complete representation of a domain [12].

In light of our expectations expressed in hypothesis two, we found that when script readers selected a second script to add to their script combination, the level of OO was a statistically significant and negative predictor of selection. However, we also found this was only the case initially, i.e., when users added a second script to a first. When users added a third script to a set of two scripts, the influence reversed and became statistically significant and positive. Because this result was a surprise, we set out to determine a possible explanation. Our post-hoc investigation of the collected data indicated that more than 76% of the participants who picked more than two scripts did not actually use all the scripts in combination. Indeed, they decided to remove some of them from the combination before they finally proceeded to complete their tasks. To illustrate the decision-making process we uncovered, Fig. 1 presents how users selected or removed additional scripts from the combination.

A notable finding for us was that, as users started removing some scripts from a combination they had built at that point, they decreased the level of OO, and they also decreased the level of COC. This finding suggests that participants compromise COC over OO. This may be the case because overlapping information increases the cognitive load required for processing the information presented across multiple script and the costs of cognitive overload outweighs their need to obtain further confirmatory information. Therefore, users decided to use less complete and less overlapping combinations rather than more complete and also more overlapping script combinations. In line with the pre diction of the theory of COC and OO, our findings tentatively suggest that the decision about which script to use in combination is governed by the principles of clarity over completeness [12]. Readers sacrifice completeness in order to have an “easier” script they can use.

## 6.1. Theoretical implications

Our research provides the first dedicated empirical evaluation of the selection proposition from the theory of Combined Ontological Completeness and Overlap [12]. We found that indeed the factors COC and OO help explain how users decide which and how many different conceptual modeling scripts to use in combination. Also, in line with the predictions of the theory, we found that script users compromised COC over OO in their decisions. This finding bears implications for the design of modeling grammars and ultimately scripts: To date, focus has always been given to grammars in terms of providing a set of constructs that will maximize the potential completeness of the scripts created using that grammar. However, our findings suggest that another design objective should be to clarify how different grammars can provide constructs to create scripts that contain ontological overlap to a reasonable extent, such that the scripts can correspond to each other and in turn effectively help users in their tasks.

Our findings also reveal that users at times also decide to remove some scripts from a combination they had originally selected. A possible explanation for this decision is that the script combination originally selected had exceeded a “bearable” level of OO. Our findings suggest the when the level of OO exceeds a bearable level, users start recognizing a noticeable increase in cognitive load or even overload. To follow-up on this proposition, it will be useful to use cognitive theories to investigate how different levels of OO can affect users’ performance in different task settings [9,40].

Finally, our findings indicate that most of the participants decided to use more than one script, but they did not decide to many (e.g., four) scripts in combination. Previous findings indicate that users perform better in model-based tasks when they use multiple scripts representing different perspectives of information systems [24,72]. However, too many scripts increase the complexity of the representation and thus add to the cognitive effort required to search for, and integrate, information presented across multiple scripts. An interesting study to the current literature could be developing predictions about how many scripts should be developed for different tasks to achieve optimal performance within each one [29.73].

## 6.2. Practical implications

Our findings inform a largely neglected aspect of conceptual modeling practice – how users decide which of different conceptual modeling scripts to use in combination. Two main practical implication flow from our work. First, the findings of this study provide practical guidance that can assist conceptual modeling practitioners in their de cision about which combinations of scripts to use for systems analysis and design tasks.

![](/api/attachments/SVPUYNM9/fulltext/images/c410c43b49713dcaafabf34314c2377ac198e3774e38b3dd305bf502477b9183.jpg)  
Fig. 1. How users proceed to select/drop scripts before tasks completion.

Second, while our study focused on script interpretation rather than script design, we believe that our findings also provide practical impli cations for script designing practices. This claim derives from the prin ciple that conceptual modeling is not an end in itself. Ultimately, every script is designed to be read by some user. A user can be the script developer, or another user who will use already developed scripts. Un derstanding how individuals select which scripts to use gives script de signers a priori ideas about what types of script they should develop. Our findings suggest that script designers should not only focus about completeness but also consider the parsimony principle in their design. Our participants preferred less complete but clear representations for their tasks, which could suggest that script design for overlap may even be more important than design for completeness – even a complete set of scripts will not help practitioners solve their problems if they gauge them to be too complex to process and hence prefer not to use them. Future work can examine the importance of completeness in composi tion to level of overlap between scripts.

## 6.3. Limitations

Several limitations pertain to our study. First, the experimental procedures, tasks, and scripts used in our experiment may not faithfully reflect the scale of real-world modeling in practice. For example, we were only able to consider some of the pragmatic and contextual factor (i.e., level of familiarity or domain knowledge) that may affect users choices of different scripts. In practice, there could be other pragmatic factors, such as organizational standards, modeling conventions, or tool support [3,23], that affect users’ decisions on which scripts to use. Second, for the experiments, we used a sample of students rather than a sample of practitioners, as is common in conceptual modeling research. We outlined our reasons for this sampling strategy but caution that the results may not be generalizable to expert practitioners.

Third, our experimental tasks were specified such that they focused on the use of conceptual modeling during systems analysis and design tasks. This design aspect is a simplification of reality, because most often analysts both design and then use scripts to discuss domain requirements with stakeholders. In such a setting, a person would likely have different preferences for choosing a script, depending on the process and effort involved in creating the scripts. Moreover, we did not evaluate different decision-making processes that stem from different systems develop ment methodologies (such as rigorous document-led approaches versus more contemporary agile approaches). Further studies are needed to evaluate how script readers decide which modeling scripts to use during agile software development life cycle.

Fourth, in our post-hoc test, we asked participants whether they removed any script(s) from the combination they had already selected. While they were free to remove at least one of their scripts, it is impossible for participants to “unsee” the information they may have already picked up at that point from the selected scripts. This situation could affect participants performance in the problem-solving tasks. However, the objective of this study was to evaluate the users’ decision process when multiple scripts are available. Future studies can re-design our experiment to evaluate how different selection decisions may affect participant performance by controlling the learning effects obtainable from initially selected and then removed scripts.

Fifth, we used a combination of four UML diagrams in our experi ment. UML features a wider range of diagrammatic scripts, and other grammars (such as BPMN or ERD) also exist. In fact, IS professionals occasionally use UML diagrams with other types of scripts, such as ERD or BPMN (e.g., [3,74]). Our focus on UML diagrams alone thus limits the the ability to generalize our findings. However, our primary objective in the experimental study was to control exogenous variables and increase internal validity. We used UML diagrams to avoid the potential extra neous effect of individuals’ different levels of familiarity with UML di agrams compared to other grammars, and to control for differences in notational elements that would vary between grammars (e.g., the shapes and colors of symbols) [9,41]. Our choice of the four UML scripts was guided by theoretical considerations (maximizing the contrast in completeness and overlap) as well as available empirical data on the relative usage of different UML scripts [15,30]. Future studies can repeat our experiment using combinations of scripts developed using grammars other than UML, or with different, or more, UML grammars.

Finally, we analyzed script combinations using an interpretation mapping on basis of published analyses of UML grammars conducted using representation theory [e.g., 50, 60, 61, 62]. Other types of map pings using different benchmarks could also be performed to establish differences in COC and OO. COC and OO as factors are not tied to a particular set of ontological constructs. For example, other researchers have used ontological constructs from Searle [75] or from the unified foundational ontology [42].

## 7. Conclusion

We provided a first empirical evaluation of the Theory of Combined Ontological Completeness and Overlap. Our findings show the impor tant role of COC and OO of script combinations on script selection by users that set out to complete systems analysis and design tasks. These findings provide an understanding of the use of scripts in practice, and in turn, can guide end-users in their decisions when choosing to use scripts and inform executive decision makers with regards to their investment to implement conceptual modeling initiatives. We hope that our work will lead to more effective and efficient use of conceptual scripts in systems analysis and design tasks.

## Funding

This study was partially supported through funding from the Australian Research Council (DE120100776 and DP140101815). We thank the editorial and review team for their helpful comments. All faults remain ours.

## Credit author statement

Mohammad Jabbari was involved in conceptualizing the study, writing the original draft, reviewing, editing, design of the methodol ogy, data collection, data analysis, and validation of the study.

Jan Recker was involved in supervision, conceptualizing the study, writing, reviewing, editing the paper, design of the methodology, acquisition of financial support for the project, and validation of the study.

Peter Green was involved in supervision, conceptualizing the study, reviewing, editing, acquisition of financial support for the project, and validation of the study.

## Appendix A. Details on the measurement of dependent variable

To define levels for our dependent variable, we proceeded in three steps.

Step one: Interpretation mapping

We followed established procedures for the ontological analysis of scripts, as demonstrated by Recker and Green [12] and detailed by others (e.g., [76,77]). We also followed the multi-coder mapping procedure, as described in Recker and Green [12], to establish the reliability of this mapping. We followed three steps: First, for each script, we identified grammar constructs represented in the script. We then individually and separately evaluated the meaning ascribed to each construct and the mapping rationale to map it to the corresponding ontological construct. To do so, we perused the mappings of UML grammars reported in the literature (e.g., [50,60,61,62]. This step was important because not all constructs provided via a gramma are presented in the scripts [78,79]. For example, the grammatical constructs, “system” or “extend”, are not represented in the use case diagram for High Peak Bicycles case. Moreover, interpretation mappings are not always a 1:1 correspondence of grammatical to ontological constructs [77]. Second, we met to discuss our interpretations and our rationales for our mappings. We then separately revised our individual mappings. Finally, the revised version of the interpretation mappings was discussed and refined in several meetings until we reached a full agreement on the mappings. Table A1 details the agreed rationale for each construct mapping by script type, and Table A2 summarizes the mapping by ontological construct.

## Table A1

Construct interpretation mappings by script type.

<table><tr><td>Script type</td><td>UML-Constructs/elements</td><td>Shapes</td><td>RT-Constructs</td><td>Rationale</td></tr><tr><td rowspan="5">Class Diagram</td><td>Class</td><td></td><td>Class</td><td>Class type shows types of things which share similar properties in general.</td></tr><tr><td>Member</td><td></td><td>Property</td><td>Specifies attributes of a class “Attributes are the names that we use to represent properties of things” (e.g., ID, Name).</td></tr><tr><td>Relationship Type</td><td></td><td>Coupling and binding mutual properties</td><td>Relationship types describe the binding mutual properties that couple two classes of things.</td></tr><tr><td>Operations</td><td></td><td>Transformation</td><td>An operation is a behavioral feature that may be owned by an interface and which defines how the state of a thing can be changed [62].</td></tr><tr><td>Cardinality</td><td></td><td>State law</td><td>Cardinality constraints describe a state law that constrains the values of a binding mutual property to certain conditions.</td></tr><tr><td rowspan="4">Use-Case</td><td>Use Case</td><td></td><td>Transformation</td><td>Use cases describe sets of actions as mappings that will change the state of the system.</td></tr><tr><td>Actor</td><td></td><td>Class</td><td>Actors are roles, which describe specific types of things (such as humans) [50].</td></tr><tr><td>Association</td><td></td><td>Binding mutual property</td><td>Associations draw linkages between actors and use cases such as which role are authoritative for carrying out an action.</td></tr><tr><td>Generalization</td><td></td><td>Excess</td><td>Generalizations between use cases do not carry any ontological meaning because they violate the “kind of” relationship that can exist between things (but not between processes changes of states [50]).</td></tr><tr><td>Activity</td><td>Activity</td><td>Check the Request</td><td>Transformation</td><td>Describes a change in a state of a thing [49].</td></tr></table>

(continued on next page)

Table A1 (continued )

<table><tr><td>Script type</td><td>UML-Constructs/elements</td><td>Shapes</td><td>RT-Constructs</td><td>Rationale</td></tr><tr><td rowspan="6"></td><td>Control flow</td><td></td><td>Lawful transformation</td><td>Describes the sequence of actions and the process. A control flow shows the flow of control from one action to the next. [62]. A transition is a relationship between two activities indicating the flow of the activities.</td></tr><tr><td>Fork node, join node</td><td></td><td>Excess</td><td>Synchronization bars do not carry any ontological meaning because they merely represent splitting and linking parallel flows of control, the meaning of which are captured in transitions.</td></tr><tr><td>Initial/final node</td><td></td><td>Event</td><td>Represent the end event and start event in processes [49]. The initial state and end state represent the start and end of the control flow.</td></tr><tr><td>Decision node</td><td></td><td>Excess</td><td>Decision nodes do not carry an ontological meaning. The control flows coming away from a decision node will have guard conditions which will allow control to flow if the guard condition is met.</td></tr><tr><td>Guard condition</td><td><img src="/api/attachments/SVPUYNM9/fulltext/images/b98d3e4d38aa9c566efc2302b1bcbe95de113bc1712237d7e23b85e6fde54f51.jpg"/></td><td>Stability condition</td><td>Specifies the states that are allowable under the transformation law [49].</td></tr><tr><td>Swimlane</td><td><img src="/api/attachments/SVPUYNM9/fulltext/images/1b5977d6d24336febe35dace9034e3c5f5472466d727848e4420b1fa1760f2e5.jpg"/></td><td>System and Class</td><td>Partitions the activity states in an activity diagram into groups, each group representing the business organization responsible for those activities [62].</td></tr><tr><td rowspan="5">State</td><td>State</td><td><img src="/api/attachments/SVPUYNM9/fulltext/images/0c9e62a6b274ccd32fe45faaecd7fdec85053a750a91eb9856aa5e8d813702d6.jpg"/></td><td>State</td><td>Represents the value of the property function of a thing</td></tr><tr><td>Initial/final state</td><td></td><td>Stable State</td><td>Initial State is the default starting state for the state machine. The final state is a special kind of state signifying that the enclosing region is completed.</td></tr><tr><td>Choice</td><td></td><td>Excess</td><td>Choice pseudo states do not carry an ontological meaning because they realize a dynamic conditional branch. It shows that the transitions should follow the guard conditions.</td></tr><tr><td>Guard Condition</td><td>[Request==rent]</td><td>Stability condition</td><td>Guard conditions describe properties that restrict the functions of a mutual property between things to a lawful subset.</td></tr><tr><td>Transition</td><td>Checkavailability</td><td>Transformation</td><td>A transition shows the flow of control from one state to the next. A transition is a relationship between two states indicating that an object in the first state will perform certain actions and enter the second state when a specified event occurs and specified conditions are satisfied [63].</td></tr></table>

## Table A2

Interpretation mapping of script constructs by ontological construct.

<table><tr><td>Ontological construct</td><td>Class</td><td>Use Case</td><td>Activity</td><td>State Machine</td></tr><tr><td>Thing</td><td></td><td></td><td></td><td></td></tr><tr><td>Class</td><td>*</td><td>*</td><td>*</td><td></td></tr><tr><td>Property in General</td><td>*</td><td></td><td></td><td></td></tr><tr><td>Hereditary Property</td><td></td><td></td><td></td><td></td></tr><tr><td>Binding Mutual property</td><td>*</td><td>*</td><td></td><td></td></tr><tr><td>State</td><td></td><td></td><td></td><td>*</td></tr><tr><td>State Law</td><td>*</td><td></td><td></td><td></td></tr><tr><td>Stable State</td><td></td><td></td><td></td><td>*</td></tr><tr><td>Event</td><td></td><td></td><td>*</td><td></td></tr><tr><td>External Event</td><td></td><td></td><td></td><td></td></tr><tr><td>Transformation</td><td>*</td><td>*</td><td>*</td><td>*</td></tr><tr><td>Lawful Transformation</td><td></td><td></td><td>*</td><td></td></tr><tr><td>Stability Condition</td><td></td><td></td><td>*</td><td>*</td></tr><tr><td>Coupling</td><td>*</td><td></td><td></td><td></td></tr><tr><td>System</td><td></td><td></td><td>*</td><td></td></tr><tr><td>Sum out of 15</td><td>6</td><td>3</td><td>6</td><td>4</td></tr></table>

## Step two: Overlap analysis

Next, we performed an overlap analysis [55]. To evaluate the level of COC of any possible combination of scripts, we counted those constructs of the scripts that corresponded to different ontological constructs. For instance, in the combination of use case-based script and class-based script, the ontological constructs of class, binding mutual property and transformation in the use case script did not add to the level of COC in the script combination because the same ontological constructs also appeared in the class script. Similarly, we measured the level of OO of any possible combination of scripts by counting those constructs of scripts in a combination that could be mapped to the same ontological construct. Table A3 shows the results of the overlap analysis for each possible pairwise, three or more scripts combinations.

## Table A3

COC and OO for combinations scripts.

<table><tr><td colspan="6">Combination of two scripts – High Peak Bicycle Case</td></tr><tr><td colspan="2">Diagram Type</td><td>Use Case Diagram</td><td>Class Diagram</td><td>Activity Diagram</td><td>State Machine Diagram</td></tr><tr><td colspan="2">Use Case Diagram</td><td></td><td>3</td><td>2</td><td>1</td></tr><tr><td colspan="2">Class Diagram</td><td>6</td><td></td><td>2</td><td>1</td></tr><tr><td colspan="2">Activity Diagram</td><td>7</td><td>10</td><td></td><td>2</td></tr><tr><td colspan="2">State Machine Diagram</td><td>6</td><td>9</td><td>8</td><td></td></tr><tr><td colspan="6">Combination of three or four Scripts – High Peak Bicycle Case</td></tr><tr><td></td><td>Use Case + Class + Activity Diagrams</td><td>Use Case + Class + State Machin Diagrams</td><td>Use Case + Activity + State Machine Diagrams</td><td>Class + Activity + State Machine Diagrams</td><td>Use Case + Class + Activity + State Machine Diagrams</td></tr><tr><td>COC</td><td>10</td><td>9</td><td>9</td><td>12</td><td>12</td></tr><tr><td>OO</td><td>3</td><td>3</td><td>3</td><td>3</td><td>4</td></tr></table>

COC of the combinations is given in the dark grey cells below the diagonal; OO is given in the light grey cells above

## Step three: Computation of dependent variable

On basis of the interpretation mapping and overlap analysis, we then defined our dependent variable as a binary variable whether participants selected a combination of scripts with maximal COC and OO. The dependent variable was coded as Yes (1) when the level of COC was higher and the level of OO was lower than any other possible combination and coded as No (0) when either COC was not higher or OO was not lower than any other possible combination. To compute the variable, we evaluated the level of COC and OO in each step when participants decided to add an additional script to the combination. Then we compared the level of COC and OO of the selected combination with other possible combinations. For instance, if participants started with the use case diagram, the dependent variable was coded as Yes (1) if they decided to use the activity diagram in the combination (COC = 7, OO = 2), otherwise it was coded as No (0). Similarly, we measured and compared the level of COC and OO when participants decided to use a combination of three scripts. Based on what participants have already selected, the dependent variable was coded as Yes (1) if adding the third script provided a combination with the maximal COC and minimal OO compared to any other possible combination. For instance, consider the previous case as described above, the dependent variable was coded as Yes (1) if participants decided to use the class diagram as the third scrip (COC = 10, OO = 3), and coded as No (0) if they decided to use the state machine diagram as the third script (COC = 9, OO = 3).

Appendix B. Measurement items

<table><tr><td colspan="2">Pre-study Tests</td></tr><tr><td colspan="2">Demographic Questions</td></tr><tr><td colspan="2">What is your gender?</td></tr><tr><td colspan="2">Male Female</td></tr><tr><td colspan="2">Are you an under- or post-graduate student?</td></tr><tr><td colspan="2">Under-graduate Post-graduate</td></tr><tr><td colspan="2">Have you ever learned UML (Unified Modelling Language)?</td></tr><tr><td colspan="2">Yes No</td></tr><tr><td colspan="2">Are you enrolled in a unit that teaches conceptual modelling in semester 2/2016, or have you completed such a unit in an earlier semester?</td></tr><tr><td colspan="2">Yes No</td></tr><tr><td colspan="2">Modeling Experience (Adapted from Burton-Jones and Meso [80] and Recker [69])</td></tr><tr><td colspan="2">Roughly, how many UML models have you:</td></tr><tr><td colspan="2">......Created to date? None</td></tr><tr><td colspan="2">......Read to date? None</td></tr><tr><td colspan="2">Familiarity with UML (Adapted from Recker [69])</td></tr><tr><td colspan="2">Please rate your agreement with the following statements about your familiarity with UML on a scale from 1 (strongly disagree) to 7 (strongly agree):</td></tr><tr><td colspan="2">(1) Overall, I am very familiar with UML.</td></tr><tr><td colspan="2">(2) I feel very confident in understanding models created with UML.</td></tr><tr><td colspan="2">(3) I feel very competent in using UML models.</td></tr><tr><td colspan="2">(4) Compared to a professional system developer or analyst, I would rate my level of experience in interpreting UML models as: (a scale from 1 (Very low) to 7 (Very high))</td></tr><tr><td colspan="2">Domain Knowledge (Adopted from Bera, Burton-Jones and Wand [10] and Burton-Jones and Meso [80])</td></tr><tr><td colspan="2">Please rate your level of knowledge and experience on a scale from 1 (Very low) to 7 (Very high):</td></tr><tr><td colspan="2">Compared to someone who works in a bicycle rental shop, I would rate my level of knowledge of activities in a bicycle rental shop (such as updating rent rates, preparing rental agreements, categorizing bicycle classes) as:</td></tr><tr><td colspan="2">Model Familiarity Test [the correct answers are written in bold] [29]</td></tr><tr><td>What type of model is this?UML Class diagramUML Component DiagramUML Object DiagramUML State Machine DiagramUML Activity DiagramI don’t know</td><td>What type of model is this?UML Component DiagramUML Class diagramUML Sequence DiagramUML State Machine DiagramUML Use Case DiagramI don’t know</td></tr><tr><td>What type of model is this?UML Use Case DiagramUML Class diagramUML Component DiagramUML Sequence DiagramUML Activity DiagramI don’t know</td><td>What type of model is this?UML Class diagramUML Sequence DiagramUML State Machine DiagramUML Communication DiagramUML Use Case DiagramI don’t know</td></tr><tr><td>What type of model is this?UML State Machine DiagramUML Activity DiagramUML Timing DiagramUML Communication DiagramUML Interaction Overview DiagramI don’t know</td><td>What type of model is this?UML Component DiagramUML Profile DiagramUML Package DiagramUML Development DiagramUML Object DiagramI don’t know</td></tr></table>

Conceptual model for online auditing, Decis. Support. Syst. 50 (3) (2011) 636–647.

## Measurement instruments for the experiment

Problem Solving Questions - Upcoming task for model selection (self-developed) 1. The managers of the Bicycle rental shop are interested in improving the overall revenue. Based on the information in the models, identify at least two ways how they can do so. 2. Customer feedback indicates that client satisfaction significantly decreased over the last six months. From the information in the models, identify at least two reasons why this could be the case. Use of Information –learning effect (Adapted from Burton-Jones and Meso [80]) On a 1–7 scale (“Not at all” to “A great extent”), to answer the previous two problem-solving questions…: [the questions may vary for each participant based on the scripts they have selected] To what extent did you rely on the information in diagram (A)? To what extent did you rely on the information in diagram (B)? To what extent did you rely on the information in diagram (C)? To what extent did you rely on the information in diagram (D)? To what extent did you rely on your general knowledge? To what extent did you make assumptions? Deselection of models (multiple answers are possible) (Self developed) If you had an opportunity to remove a diagram/s which, in hindsight, you feel was not useful in answering the questions, which diagram/s would you have removed? [the questions may vary for each participant based on the scripts they have selected] Diagram (A) Diagram (B) Diagram (C) Diagram (D) None of them

## References

[1] A. Burton-Jones, P.N. Meso, Conceptualizing systems for understanding: an empirical test of decomposition principles in object-oriented analysis, Inf. Syst. Res. 17 (1) (2006) 38–60.

[2] A.R. da Silva, Model-driven engineering: a survey supported by the unified conceptual model, Comput. Lang. Syst. Struct. 43 (2015) 139–155.

[3] M.A. Jabbari Sabegh, J. Recker, Combined use of conceptual models in practice: an exploratory study, J. Database Manag. 28 (2) (2017) 56–88

[4] J. Whittle, J. Hutchinson, M. Rouncefield. The state of practice in model-driven engineering, JEEE Softw, 31 (3) (2014) 79–85.

[5] G. Campanella, R.A. Ribeiro, A framework for dynamic multiple-criteria decision making, Decis. Support. Syst. 52 (1) (2011) 52–60.

[6] Recker, J., Lukyanenko, R., Jabbari , M., Samuel, B., Castellanos, A., From representation to mediation: a new agenda for conceptual modeling research in a digital world. MIS Quarterly. 45 (1a) (2021) 269-300.

[7] J. Mendling, M. Strembeck, J. Recker, Factors of process model comprehension—findings from a series of experiments, Decis. Support. Syst. 53 (1) (2012) 195–206.

[8] T.-F. Kummer, J. Recker, J. Mendling, Enhancing understandability of process models through cultural-dependent color adjustments, Decis. Support. Syst. 87 (2016) 1–12.

[9] K. Figl, J. Recker, J. Mendling, A study on the effects of routing symbol design on process model comprehension, Decis. Support. Syst. 54 (2) (2013) 1104–1118.

[10] P. Bera, A. Burton-Jones, Y. Wand, How semantics and pragmatics interact in understanding conceptual models. Inf, Syst, Res. 25 (2) (2014) 401–419.

[11] A. Gemino, Y. Wand, A framework for empirical evaluation of conceptual modeling

[12] J. Recker, P. Green, How do individuals interpret multiple conceptual models? A theory of combined ontological completeness and overlap, J. Assoc. Inf. Syst. 20 (8) (2019) 1210–1241.

[13] S. Lauesen, O. Vinter, Preventing requirement defects: an experiment in process improvement, Requir. Eng, 6 (1) (2001) 37–50.

[14] I. Davies. P. Green. M. Rosemann. M. Indulska, S. Gallo. How do practitioners use conceptual modeling in practice? Data Knowl. Eng, 58 (3) (2006) 358–380.

[15] B. Dobing, J. Parsons, Dimensions of UML diagram use: a survey of practitioners, J. Database Manag, 19 (1) (2008) 1–18

[16] P. Fettke, How conceptual modeling is used, Commun. Assoc. Inf. Syst. 25 (1) (2009) 571–592.

[17] A. Dreiling, M. Rosemann, W.M. van der Aalst, W. Sadiq, From conceptual process models to running systems: a holistic approach for the configuration of enterprise system processes, Decis, Support, Syst, 45 (2) (2008) 189–207.

[18] N. Kock, J. Verville, A. Danesh-Pajou, D. DeLuca, Communication flow orientation in business process modeling and its effect on redesign success: results from a field study, Decis. Support. Syst. 46 (2) (2009) 562–575.

[2o] N Prat J. Akoka I Comyn-Wattiau A UML-based data warehouse design method

[21] J. Hutchinson, J. Whittle, M. Rouncefield, Model-driven engineering practices in industry: social organizational and managerial factors that lead to success or failure, Sci. Comput. Program. 89 (2014) 144–161.

[22] J. Recker, “Modeling with tools is easier, believe me”—the effects of too functionality on modeling grammar usage beliefs, Inf. Syst. 37 (3) (2012) 213–226.

[23] P. Green, M. Rosemann, M. Indulska, J. Recker, Complementary use of modeling grammars, Scand. J. Inf. Syst. 23 (1) (2011) 59–86.

[24] J. Kim, J. Hahn, H. Hahn, How do we understand a system with (so) many diagrams? Cognitive integration processes in diagrammatic reasoning, Inform. Syst. Res. 11 (3) (2000) 284–303.

[25] H. Zhang, R. Kishore, R. Sharman, R. Ramesh, Agile integration modeling language (AIML): a conceptual modeling grammar for agile integrative business information systems, Decis. Support. Syst. 44 (1) (2007) 266–284.

[26] A. Gupta, G. Poels, P. Bera, Creation of multiple conceptual models from user stories–A natural language processing approach, in: International Conference on Conceptual Modeling, Springer, 2019, pp. 47–57.

[27] R.J. Brooks, A.M. Tobias, Choosing the best model: level of detail, complexity, and model performance, Math. Comput. Model. 24 (4) (1996) 1–14.

[28] A. Gemino, Y. Wand, Complexity and clarity in conceptual modeling: comparison of mandatory and optional properties, Data Knowl. Eng. 55 (3) (2005) 301–326.

[29] K. Figl, J. Recker, Exploring cognitive style and task-specific preferences for process representations, Requir. Eng. 21 (1) (2016) 63–85.

[30] B. Dobing, J. Parsons, How UML is used, Commun. ACM 49 (5) (2006) 109–113.

[31] H. Topi, V. Ramesh, Human factors research on data modeling: a review of prior research, an extended framework and future research directions, J. Database Manag. 13 (2) (2002) 3–19.

[32] Y. Wand. R. Weber. Research commentary: information systems and conceptua modeling—a research agenda, Inf, Syst, Res, 13 (4) (2002) 363–376.

[33] O.I. Lindland, G. Sindre, A. Solvberg, Understanding quality in conceptua modeling, IEEE Softw. 11 (2) (1994) 42–49.

[34] C.A. Gurr, Effective diagrammatic communication: syntactic, semantic and pragmatic issues, J. Vis. Lang. Comput. 10 (4) (1999) 317–342.

[35] D.L. Moody, The “physics” of notations: toward a scientific basis for constructing visual notations in software engineering, IEEE Trans. Softw. Eng. 35 (6) (2009) 756-779.

[36] Y. Wand, R. Weber, Mario Bunge’s ontology as a formal foundation for information systems concepts, in: P. Weingartner, G.J.W. Dorn (Eds.), Studies on Mario Bunge’s Treatise, Rodopi, Amsterdam, The Netherlands, 1990, pp. 123–149.

[37] G. Guizzardi, G. Wagner, J.P.A. Almeida, R.S. Guizzardi, Towards ontological foundations for conceptual modeling: the unified foundational ontology (UFO) story, Appl. Ontol. 10 (3–4) (2015) 259–271.

[38] R. Hirschheim, H.K. Klein, K. Lyytinen, Information Systems Development and Data Modeling: Conceptual and Philosophical Foundations, Cambridge University Press, Cambridge, Massachusetts, 1994.

[39] J. Recker, M. Indulska, P. Green, A. Burton-Jones, R. Weber, Information systems (2019) 735–786.

[40] R. Petrusel, J. Mendling, H.A. Reijers, How visual cognition influences process model comprehension, Decis, Support, Syst, 96 (2017) 1–16

[41] H.A. Reijers, T. Freytag, J. Mendling, A. Eckleder, Syntax highlighting in business process models, Decis. Support. Syst. 51 (3) (2011) 339–349.

[42] G. Guizzardi, T.A. Halpin, Ontological foundations for conceptual modelling, Appl. Ontol. 3 (1–2) (2008) 1–12.

[43] P.S. Santos Jr., J.P.A. Almeida, G. Guizzardi, An ontology-based analysis and semantics for organizational structure modeling in the ARIS method, Inf. Syst. 38 (5) (2013) 690–708.

[44] M. Verdonck, F. Gailly, R. Pergl, G. Guizzardi, B. Martins, O. Pastor, Comparing traditional conceptual modeling with ontology-driven conceptual modeling: an empirical study, Inf. Syst. 81 (2019) 92–103.

[45] Y. Wand, R. Weber, On the ontological expressiveness of information systems analysis and design grammars, Inf. Syst. J. 3 (4) (1993) 217–237.

[46] G. Shanks, E. Tansley, J. Nuredini, D. Tobin, R. Weber, Representing part–whole relations in conceptual modeling: an empirical evaluation, MIS Q. 32 (3) (2008) 553–573.

[47] J. Valaski, S. Reinehr, A. Malucelli, Deriving domain functional requirements from conceptual model represented in OntoUML, in: 19th International Conference on Enterprise Information Systems, Science and Technology Publications. Porto. Portugal, 2017, pp. 263–270

[48] I. Vessey, S.A. Conger, Learning to specify information requirements: the relationship between application and methodology, J. Manag. Inf. Syst. 10 (2) (1993) 177–202.

[49] J. Recker, M. Rosemann, M. Indulska, P. Green, Business process modeling-a comparative analysis, J. Assoc. Inf. Syst. 10 (4) (2009) 333–363.

[50] G. Irwin, D. Turk, An ontological analysis of use case modeling grammar, J. Assoc. Inf. Syst. 6 (1) (2005) 1–36.

[51] K.L. Siau, An analysis of unified modeling language (UML) graphical constructs based on BWW ontology, J. Database Manag. 21 (1) (2010) i–viii.

[52] J.D. Thompson, Organizations in Action: Social Science Bases of Administrative Theory, McGraw-Hill, New York, 1967.

[53] R. Weber, Ontological Foundations of Information Systems, Coopers & Lybrand and the Accounting Association of Australia and New Zealand, Melbourne, Australia. 1997.

[54] A. Gemino, Y. Wand, Evaluating modeling techniques based on models of learning, Commun. ACM 46 (10) (2003) 79–84.

[55] P. Green, M. Rosemann, M. Indulska, C. Manning, Candidate interoperability standards: an ontological overlap analysis, Data Knowl. Eng. 62 (2) (2007) 274–291.

[56] J. Sweller, P. Chandler, Why some material is difficult to learn, Cogn. Instr. 12 (3) (1994) 185–223.

[57] P. Soffer, Y. Wand, M. Kaner, Conceptualizing routing decisions in business processes: theoretical analysis and empirical testing, J. Assoc. Inf. Syst. 16 (5) (2015) 345–393.

[58] H.L. Fromkin, S. Streufert, Laboratory experimentation, Handbook Indust. Org. Psychol. (1976) 415–465.

[59] D. Whiteley, An Introduction to Information Systems, Palgrave Macmillan, London, England. 2013.

[60] J. Evermann, Y. Wand, Ontology based object-oriented domain Modelling: fundamental concepts, Requir. Eng, 10 (2) (2005) 146–160.

[61] J. Evermann, Y. Wand, Ontological modeling rules for UML: an empirical assessment, J. Comput. Inf. Syst. 46 (5) (2006) 14–19

[62] A.L. Opdahl, B. Henderson-Sellers, Ontological evaluation of the UML using the Bunge–Wand–Weber model, Softw. Syst. Model. 1 (1) (2002) 43–67.

[63] G. Booch, J. Rumbaugh, I. Jacobson, The Unified Modeling Language User Guide, 1999 15, Addison-Welsley Longman Inc, 2010, p. 285.

[64] R.E. Mayer, Thinking, Problem Solving, Cognition, 2nd ed., W.H. Freeman, New York 1992

[65] S. Alter, G.J. Browne, A broad view of systems analysis and design: implications for research, Commun, Assoc, Inf, Syst, 16 (50) (2005) 981–999.

[66] J.A. Hoffer, J.F. George, J.S. Valacich, Modern Systems Analysis and Design, 5th ed., Prentice Hall, Upper Saddle River, New Jersey, 2007.

[67] K.E. Kendall, J.E. Kendall, Systems Analysis and Design, 7th ed., Prentice Hall, Upper Saddle River, New Jersey, 2008.

[68] J. Mendling, J. Recker, H.A. Reijers, H. Leopold, An empirical review of the connection between model viewer characteristics and the comprehension of conceptual process models, Inf. Syst. Front. 21 (5) (2019) 1111–1135.

[69] J. Recker, Continued use of process modeling grammars: the impact of individual difference factors, Eur. J. Inf. Syst. 19 (1) (2010) 76–92.

[70] E. Arisholm, D.I. Sjøberg, Evaluating the effect of a delegated versus centralized control style on the maintainability of object-oriented software, IEEE Trans. Softw. Eng. 30 (8) (2004) 521–534.

[71] J. Pallant, SPSS Survival Manual: A Step by Step Guide to Data Analysis Using SPSS for Windows (Version 15), 3rd ed., McGraw-Hill Education, England, 2007

[72] A. Gemino, D.C. Parker, Use case diagrams in support of use case modeling: deriving understanding from the picture, J. Database Manag. 20 (1) (2009) 1–24.

[73] H. Ritchi, M. Jans, J. Mendling, H.A. Reijers, The influence of business process representation on performance of different task types, J. Inf. Syst. 34 (1) (2020) 167-194.

[74] M. Petre, UML in practice, in: Proceedings of the 2013 International Conference on Software Engineering, IEEE Press, San Francisco, California, 2013, pp. 722–731.

[75] S.T. March, G.N. Allen, Toward a social ontology for conceptual modeling, Commun. Assoc. Inf. Syst. 34 (70) (2014) 1347–1358.

[76] M. Rosemann, P. Green, M. Indulska, A reference methodology for conducting ontological analyses, in: H. Lu, W. Chu, P. Atzeni, S. Zhou, T.W. Ling (Eds.), Conceptual Modeling–ER 2004, Springer, Shanghai, China, 2004, pp. 110–121

[77] M. Rosemann, J. Recker, P. Green, M. Indulska, Using ontology for the representational analysis of process modelling techniques, Int. J. Bus. Process. Integr. Manag. 4 (4) (2009) 251–265.

[78] K.L. Siau, J. Erickson, L.Y. Lee, Theoretical vs. practical complexity: the case o UML, J. Database Manag. 16 (3) (2005) 40–57.

[79] M. Zur Muehlen, J. Recker, How much language is enough? Theoretical and practical use of the business process modeling notation, in: International Conference on Advanced Information Systems Engineering, Springer, Berlin Heidelberg, 2008, pp. 465–479.

[80] A. Burton-Jones, P.N. Meso, The effects of decomposition quality and multiple forms of information on novices' understanding of a domain from a conceptua model. J. Assoc, Inf, Syst, 9 (12) (2008) 748–802

Mohammad Jabbari is a lecturer in the School of Information Systems at Queensland University of Technology. He has a B.Sc. in Mathematics, a Master’s degree in IT Man agement, and a PhD in Information Systems. His current research interest focuses on representation theory, systems analysis and design, and representations for decision making.

Jan Recker is AIS fellow, Alexander von Humboldt fellow, professor of Information Systems and Digital Innovation at the University of Hamburg, and adjunct professor at Queensland University of Technology. His research focuses on systems analysis and design, digital innovation and entrepreneurship, and digital solutions for sustainable development.

Peter Green is a professor in the School of Accountancy, Queensland University of Technology. From 1999 to 2013, he was a professor of eCommerce at the University of Queensland. Peter has qualifications in accounting, computer science, and a PhD in commerce (information systems) from the University of Queensland. Peter’s research in terests focus on representation theory and its application to many different areas, including accounting information systems. His publications have appeared in journals such as MIS Quarterly, European Journal of Information Systems, Information Systems, Journal of the Association for Information Systems, and others.
