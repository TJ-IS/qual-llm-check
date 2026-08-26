---
otero_id: 26389
otero_key: "S4E6X35V"
title: "Providing Decisional Guidance for Multicriteria Decision Making in Groups"
authors: "Moez Limayem; Gerardine DeSanctis"
year: "2000"
journal: "Information Systems Research"
doi: "10.1287/isre.11.4.386.11874"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.59.222.12] On: 05 February 2015, At: 12:34 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/S4E6X35V/fulltext/images/a7a9a340827b89a79852d68014a37d69856a6c8b9a86631343f8079c5984d5d8.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Providing Decisional Guidance for Multicriteria Decision Making in Groups

Moez Limayem, Gerardine DeSanctis,

To cite this article:

Moez Limayem, Gerardine DeSanctis, (2000) Providing Decisional Guidance for Multicriteria Decision Making in Groups. Information Systems Research 11(4):386-401. http://dx.doi.org/10.1287/isre.11.4.386.11874

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2000 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/S4E6X35V/fulltext/images/997a2ff77f4dbdd4bb0f06a445ba0652ee12a884551811d36bcf7d4dff2854f9.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Providing Decisional Guidance for Multicriteria Decision Making in Groups

Moez Limayem • Gerardine DeSanctis

Information Systems Department, City University of Hong Kong, Hong Kong The Fuqua School of Business, Duke University, Box 90120, Durham, North Carolina 27708–0120 ismoez@cityu.edu.hk • gd@mail.duke.edu

ntelligent user interfaces, particularly in interactive group settings, can be based on system explanations that guide model building, application, and interpretation. Here we extend Silver’s (1990, 1991) conceptualization of decisional guidance and the theory of breakpoints in group interaction to operationalize feedback and feedforward for a complex multicriteria modeling system operating within a group decision support system context. We outline a design approach for providing decisional guidance in GDSS and then test the feasibility of the design in a preliminary laboratory experiment. Findings show how decisional guidance that provides system explanations at breakpoints in group interaction can improve MCDM GDSS usability. Our findings support Dhaliwal and Benbasat’s (1996) conjecture that system explanations can improve decisional outcomes due to improvement in user understanding of decision models. Further research on intelligent agents, particularly in interactive group settings, can build on the concepts of decisional guidance outlined in this paper.

(Decision Support; Group Decision Support; Multicriteria Decision Making; User Interface; Intelligent Systems)

## 1. Introduction

Complex multicriteria problems are a key component of organizational life. Ethical choices, tradeoffs between cost and quality, and conflicts of preferences are all examples of multicriteria decisions. Multicriteria decision making models (MCDM) allow decision makers to choose among competing alternatives by weighing the relative importance of different criteria and then systematically evaluating how well alternative solutions meet these criteria.<sup>1</sup> Many multicriteria problems are resolved in group meetings (Hackman and Kaplan 1974). In group settings, MCDM take the form of aggregating individual weights and preferences and providing these as feedback for group discussion purposes (Bird and Kasper 1995, Bui and Jarke 1984, Dickson et al. 1991, Sengupta and Te’eni 1993, Tavana et al. 1996).

Despite their potential for improving decision making, MCDM and decision support systems embodying them are not readily applied and used. A number of years ago Evans (1984) reviewed 78 research articles on MCDM and found that a mere two MCDM were being regularly used in organizational settings. A key barrier to the use of MCDM, even those embedded in so-called user friendly support software, is their sheer complexity. MCDM comprise a procedure toolbox—a rich set of resources from which the user must develop a meaningful model and interpret the outputs in light of the problem at hand. The paradox of decision support for MCDM is that the process of applying modeling capability can enhance perceived problem complexity rather than reduce it, thereby lowering comfort with using decision models and reducing decision confidence. Indeed, several studies have found that decision makers avoid the use of MCDM decision aids and, when given a choice, prefer relatively unsophisticated decision models instead (Brockhoff 1985, Buchanan and Daellenbach 1987, Narasimhan and Vickery 1988). With this conundrum in mind, Dyer and colleagues (1992) called for researchers to incorporate behavioral and psychological support within MCDM systems.

The general challenge of promoting greater user understanding and appreciation of decision aids is a major research issue (Mackay and Elam 1992), and it is exaggerated in the case of MCDM, especially in group settings. Some scholars have called for the development of intelligent interface capabilities that provide explanations to users about how to develop and apply models; and there is a growing line of research that seeks to evaluate alternative approaches for building these capabilities (Dhaliwal and Benbasat 1996, Gregor and Benbasat in press). In group settings, explanation facilities are decidedly more complex to design than in settings where just one user interacts with the system. For this reason, GDSS research to date has been confined largely to design of human interventions to enhance user understanding and appreciation of modeling tools (e.g., Anson et al. 1995, Clawson et al. 1993, Dickson et al. 1993, Steeb and Johnston 1981). Here we establish the groundwork for design of intelligent agents for GDSS by exploring the feasibility of providing computer-based system explanations to groups as they use MCDM GDSS. Our goal is to contribute to research on intelligent interfaces for group decision support.

## 2. Decisional Guidance for MCDM Use in Groups

As a basis for designing explanation systems for MCDM GDSS, we build on Silver’s (1990) notion of decisional guidance. Automated decision guidance is the enrichment of decision models with cues that direct decision makers toward successful structuring and execution of model components. Designers of desktop decision aids have long called for the provision of flexibility and easy-to-use features (Angehrn and Jelassi 1994, Keen and Scott Morton 1978), but automated guidance is much more than this. A system with guidance “enlightens or sways its users as they structure and execute their decision making process—that is, as they choose among and use the system’s functional capabilities” (Silver 1991, p. 107). Guidance incorporates system-based explanations about why and how DSS capabilities can be employed, as well as strategic advice for building models and interpreting outputs in light of the task at hand (Dhaliwal and Benbasat 1996). In its most powerful form guidance is intelligent and is able to act without specific request by the user; intelligent guidance systems can monitor user behavior and provide customized explanations on an as-needed basis (Gregor and Benbasat 1999).

## 2.1. Goals of Decisional Guidance

MCDM modeling involves an extensive set of activities for a group: problem definition; identification and prioritization of evaluation criteria by group members; determination of individual preferences; aggregation of individual preferences into group judgments; “what if” model analysis based on various ways of combining criteria weights with alternative ratings or rankings; exploration of alternative ways of combining individual with group judgments in the model; refinement of individual and group preferences through consensus seeking; and final selection of a single solution or distribution of choice across a set of alternative solutions. Given the complexities, one might wonder whether groups would be better off without software and models, especially for judgment tasks, but the research to date suggests the reverse. In a meta-analysis of 64 studies comparing groups with and without GDSS support, Dennis et al. (1996) showed that groups benefit from decision modeling, in terms of improved decision quality, though models take time and effort to apply. An earlier meta-analysis of 29 studies by Benbasat and Lim (1993) reached the same conclusion. Despite decision quality benefits, use of GDSS technology generally reduces group consensus, decision confidence, and overall satisfaction. Only one of the studies reviewed in these analyses included MCDM capability within the GDSS (Dickson et al. 1991), but the results were the same: group consensus and satisfaction were lower in conditions of MCDM GDSS when compared to conditions of GDSS with simpler modeling tools (such as electronic voting on alternatives) or to conditions of groups with no support whatsoever.

Laboratory experiments show that decision makers avoid sophisticated decision aids, including GDSS and MCDM, because these tools reveal decisional conflict (Kottemann and Davis 1991, Watson et al. 1988). Buede (1992) and more recently Tuttle and Stocks (1997) emphasize the importance of promoting user understanding of decision aids, because, whether simple or complex, these tools present a cognitive load to the user. They argue that most software systems mistakenly place relatively more emphasis on ease of use than on decision makers’ understanding of the models themselves. In their review of explanations from intelligent systems, Gregor and Benbasat (1999) propose that explanations requiring limited cognitive effort will be used more readily and will be more effective with respect to performance, learning, and user perceptions. Buede and Maxwell (1995) compared several multicriteria methodologies in a laboratory experiment and found problem structuring support was more important to improving decision quality than the selection of a specific computational algorithm per se. Along the same lines, Buchanan (1994), after comparing three MCDM methods, concluded that the familiarity with the solution method was significantly correlated with confidence in the final solution.

With these findings in mind, we posit that design of decisional guidance for MCDM in group decision settings should have three major goals: (1) to enhance user understanding of the model inputs, processes, and outputs, (2) to improve decision outcomes by helping the group to navigate through the complex choices associated with MCDM modeling, and (3) to generate more positive perceptions on the part of users about their decision process, decision results, and the MCDM technology.

## 2.2. Guidance Capabilities

Research on MCDM techniques, decision support, and group decision making suggests two interdependent kinds of support needed for groups using MCDM GDSS. Cognitive support capabilities refer to explanations about how to develop and apply MCDM models. Group interaction support refers to operators that trigger the timing of system explanations as the group’s decision process unfolds. These are complementary capabilities that must be implemented together in order to be meaningful.

2.2.1. Support for Group Cognition. Cognitive feedback and feedforward capabilities should enable improved understanding of the decision modeling process in complex decision tasks. As Dhaliwal and Benbasat (1996) point out, the issue is not which form of cognitive support is relatively more effective, since both are known to be effective. Rather, the issue is operationalizing these capabilities in the DSS interface and then evaluating system effectiveness in terms of a multitude of decision-related outcomes. Cognitive feedback provides information about preference selections and the model’s structure (Te’eni 1991). Cognitive feedback draws attention to judgement inconsistencies and illustrates their causes, enables decision makers to understand their judgments and reduce their commitment to incorrect analysis, and helps decision makers to shape an adequate model of the decision making process (Balzer et al. 1989, Sengupta and Abdel-Hamid 1993). Olson et al. (1995), after comparing several multiattribute utility systems, concluded that “feedback concerning the consistency of decision maker responses should be regularly provided to make users comfortable and . . . yield results valuable to the user” (p. 743). Sengupta and Te’eni (1993) found cognitive feedback to facilitate group convergence as well, that is, to form and follow a decision rule in reaching a group choice.

Feedforward is the process of providing explanation prior to performing each step in the model building process (Bjorkman 1972). Feedforward provides explanation of MCDM procedures in advance of their use and can be operationalized as a set of heuristics for task performance. Feedforward is thought to attenuate cognitive strain by providing decision makers with information that otherwise should have been learned through feedback (Bjorkman 1972). Malloy et al. (1987), Cats-Baril and Huber (1987), and Sengupta and Abdel-Hamid (1993) have found that feedforward can enhance learning and improve decision making performance when it is presented in conjunction with feedback. Neither cognitive feedback nor feedforward have been designed or evaluated for use in GDSS settings.

2.2.2. Support for Group Interaction. Groups using electronic communication media often struggle with efficient information exchange (Hightower and Sayeed 1996). Key challenges are focusing the group’s decision process and keeping the conversation on track so that a decision model can be developed and applied (Wheeler and Valacich 1996). Supporting group interaction is more than a matter of cueing group members to follow a prescribed set of decision steps. Groups follow different sequences of decision making, with the number and order of development stages varying across groups (Poole 1981). Therefore, supporting group interaction requires accommodating flexibility in group process, even while restricting the group to a general decision model. Following Poole (1983a, 1983b) and Friedman (1989), decisional guidance can include operators that anticipate or detect “breakpoints” in group interaction. These are points in the group decision process where cognitive feedback and feedforward can be made available to the group:

(1) Normal breakpoints are shifts from one decisional step to another. Normal breakpoints are evident when decision makers complete a major step in a MCDM sequence, such as when they have finished weighting criteria or entering alternative solutions in the model. When a normal breakpoint occurs in the group’s MCDM process, feedforward can be triggered, providing information on how the current step in the MCDM modeling process relates to previous and next steps.

(2) Delay breakpoints are holding patterns wherein the group recycles through the same analysis or decision step. Delay breakpoints are evident when a group repeats a step in the MCDM process but fails to complete it, or when the group moves forward in developing the model without adequately completing a prior step. Suppose group members enter alternative problem solutions that they like as individuals, but they fail to discuss or agree on a list of alternatives; this is an example of a delay breakpoint. Similarly, if the group moves forward to calculate a MCDM model without having specified which set of weights on those criteria they would like to use in the model, this constitutes a delay breakpoint. When a delay breakpoint occurs, cognitive feedback can be triggered, suggesting as appropriate that the group move backward in the MCDM to complete an unfinished or partially finished previous step. For instance, guidance could recommend that the group go back and further clarify the definition of some criteria or specify weights on criteria. In this way, cognitive feedback would reveal conflicts or major inconsistencies across group members at delay breakpoints, focusing the group’s attention on understanding and resolving these modeling difficulties so that they can complete the current analytic step and move on in the MCDM process.

(3) Disruption breakpoints are conflict episodes or periods of uncertainty wherein group members disagree on how to use or interpret the information available to them to reach a decision. Disruption breakpoints occur when individual group members are overwhelmed with MCDM output or are out of sync with the rest of the group, operating at different points in the MCDM procedure. Disruption breakpoints also occur if the group collectively asks, “What does this result mean?” or if members proceed to calculate the MCDM model in ways that conflict with one another. To the extent that disruptions heighten users’ awareness of conflict or uncertainty on how to proceed, these breakpoints are motivational opportunities for use of decisional guidance (Gregor and Benbasat 1999). To avoid or resolve disruption breakpoints, cognitive feedback can be triggered to help the group in interpreting and distilling the multicriteria model output, thereby facilitating understanding of how the MCDM model relates to the specific problem that the group is addressing. Tables and graphs that summarize and explain commonalities and differences in members’ inputs can be used as aids to communicate this cognitive feedback. Feedforward can also be triggered at disruption breakpoints to summarize and explain the current step in the MCDM process, to provide explanation of model outputs, and to suggest how to proceed next.

In sum, the literature on decision guidance, system explanations, and group interaction suggests how guidance might be designed to improve MCDM use in groups: by provision of cognitive feedback and feedforward explanations that are provided during breakpoints in group interaction. Following Dhaliwal and Benbasat’s (1996) theoretical conjecture, these mechanisms are hypothesized to improve decision making due to their potential to improve user understanding of the MCDM modeling process. Figure 1 summarizes our research model.

Figure 1 Overview of the Research  
![](/api/attachments/S4E6X35V/fulltext/images/a1e71efe3ed0153b54740de93a5288b2555fd06fbbf749315a52696393e2223a.jpg)

## 3. Implementing and Testing the Guidance Concept

## 3.1. The MCDM GDSS

As a test bed for the automated guidance concept, we selected the MCDM module of a GDSS developed earlier by Dickson and colleagues (1992). The MCDM GDSS module consists of 30–50 data input and output screens (depending on the complexity of the particular model developed by the group). It is menu-driven and arranged in a hierarchical sequence such that users specify a MCDM model in a sequential manner, following a series of options in which data is entered by group members and viewed in an iterative fashion as the model is built. The MCDM is a compensatory additive process—the most widely used form of multicriteria modeling (Von Nitzsch and Weber 1993). As in other MCDMs, the modeling process consists of: (1) specification of alternative solutions to the problem, (2) defining of criteria for evaluating alternative solutions, (3) weighting of criteria, (4) evaluation of alternatives across criteria, using rating, ranking, or voting techniques for evaluation, (5) computation of weighted preferences for each alternative based on individual or group evaluations, and (6) selection of a final alternative solution, ranking of alternatives, or allocation of resources across the various alternatives. Within each of these six general steps, groups can specify the MCDM based on either individual preferences, average group preferences, or some combination of the two. Sensitivity analysis in which alternative computations of the model can be compared is also possible.

Though accepted for use in several organizational settings, this MCDM GDSS has failed to yield measurable advantages under controlled laboratory conditions unless an expert advisor works with the group as they use the MCDM model. The expert explains the model’s use and assures its appropriate application (Dickson et al. 1991, 1993). This finding is consistent with studies of other complex decision aids within GDSS (George et al. 1992, Reagan-Cirincione 1991) and suggests the potential value for automated guidance to improve MCDM GDSS.

## 3.2. Implementing Guidance

Table 1 summarizes guidance capabilities corresponding to each type of group support need in MCDM and describes our approach for implementing these guidance capabilities. We developed the interlocking components of cognitive feedback and feedforward within the MCDM GDSS, with these operators triggered as a function of normal breakpoints, delay breakpoints, and/or disruption breakpoints. As long as the group followed the major steps of MCDM, experiencing only normal breakpoints, the guidance system summarized the current step, described how the current step related to the previous and next steps, and displayed a status window identifying the current step and the next step. Feedforward was presented in the form of instructions that clarified the objective of each step in the decision model and explained how the step in question fit into the overall MCDM process. Here are examples of feedforward explanations within the Weighting of Criteria (Step 3 above) and Calculate Scoring (Step 5 above) functions. (Note that these are just a few examples. There were multiple feedforward explanations associated with each step in the MCDM.)

Table 1 Support Needs for MCDM GDSS, Corresponding Guidance Capabilities, and Our Implementation Approach

<table><tr><td>Support Needs</td><td>Guidance Capabilities</td><td>Implementation</td></tr><tr><td colspan="3">Support for group cognition</td></tr><tr><td>Cognitive feedback</td><td>Information about preference selections and MCDM structure; identification of consistencies and inconsistencies in judgments</td><td>Automated detection of uncompleted steps (e.g., missing entries of individual or group judgments); detection of wide varions in individual judgments on criteria or alternatives; flagging of points of variation with visual indicators on model input and output screens</td></tr><tr><td>Feedforward</td><td>Information about each step in the MCDM modeling task prior to its performance</td><td>Screens that summarize the current MCDM step in which the group is engaged; addition of status windows identifying each step and the subsequent step; visual tracking of group progress through the MCDM model</td></tr><tr><td colspan="3">Support for group interaction</td></tr><tr><td>Normal breakpoints</td><td>Shifts from one step in the MCDM to another; determining how output from one step should be used as input to the next</td><td>Feedforward is triggered when a normal breakpoint occurs</td></tr><tr><td>Delay Breakpoints</td><td>Holding patterns wherein the group recycles through a specific step in the model; determining when to repeat a step and when to move forward</td><td>Cognitive feedback is triggered when a delay breakpoint occurs</td></tr><tr><td>Disruption breakpoints</td><td>Periods of conflict or uncertainty about how to use or interpret model components or outputs; interpreting model results and determining how to proceed</td><td>Both feedforward and cognitive feedback are triggered when a disruption breakpoint occurs</td></tr></table>

## VIEW CRITERIA

Next, you should view the criteria on the public screen. Delete or combine duplicates. Make sure that the meaning of each criterion is clear. Change wording if necessary. Make sure you reduce the number of criteria to a manageable size.

## CALCULATE SCORING

The group should have already entered the criteria weights and the ratings of the alternatives. The purpose of this step is to compute the scores for the alternatives. That is, for each alternative the system multiples ratings by weights and sums them.

A perfect score is 100. The group can elect to choose average weights and average ratings, agreed upon weights and agreed upon ratings, any member’s weights and ratings, or any other combination of weights and ratings. The group is advised to perform a sensitivity analysis by trying out different combinations and observing their impact on the scores of the alternatives. When viewing the scores, it is helpful to perform a sort to observe the alternatives with the highest scores. If an alternative scores relatively low, a message will be displayed on the public screen suggesting its deletion.

When a delay breakpoint occurred in the group decision process, cognitive feedback suggested that the group revert in the MCDM sequence and provided cues for step completion. For example, if group members varied widely in their evaluations of alternatives on different criteria, the guidance system recommended that the group discuss and further clarify the criteria definitions before proceeding further. If group members’ ratings of each alternative in the model exceeded a preset cutoff value, then a feedback message automatically displayed the inconsistent ratings and advised that the group go back and sharpen their description of the alternatives, discuss their differences, and then re-enter evaluations. The feedback explanations also flagged alternatives that were consistently rated poorly (low scores) by all group members and advised that the group consider deleting them from the MCDM model. Three examples of cognitive feedback explanations follow. The first two resulted from evaluations of alternatives across criteria (Step 4 in the MCDM) and the third example was triggered by the result of a group’s calculation of scores (Step 5 in the MCDM).

EVALUATE ALTERNATIVES: The following possible problems were detected in your ratings:

2 out of 6 ratings showed wide disagreements among group members. This relatively high number may reflect a misunderstanding of the criteria.

Criterion 1 was flagged in at least half of the alternatives. Make sure that each group member understands this criterion.

Alternatives 1 and 2 were flagged in more than half of the criteria. This may reflect a misunderstanding of these alternatives.

EVALUATE ALTERNATIVES: You currently have 10 alternatives and 8 criteria. Thus, you will have to perform 80 ratings. Assuming it takes approximately 10 seconds to decide and enter one rating, it will take you approximately 13:20 minute(s) plus the additional time to discuss each item. At this point, the group may decide to go back and reduce the number of criteria by deleting or combining them.<sup>2</sup>

SCORING OF ALTERNATIVES: Using agreed upon weights AND Using agreed upon rates. Alternative 1 scored relatively low with the above combination of weights and ratings. The group may want to consider deleting this alternative.

In a group setting MCDM can produce a voluminous amount of information, including tables of each member’s weighting of each criteria; ratings of each alternative against each criteria; tables or graphs displaying the mean, median, and variance in weights or ratings across group members; information on average scores and individual scores; and results from running the model using all inputs (all criteria, all alternatives, all group members’ inputs) or some subset of inputs (one or more criteria, one or more alternatives, one or more group members’ inputs). Since “what if” analysis is typical in MCDM, a MCDM GDSS can produce many variations of model outputs should the group experiment with alternative approaches to specifying the MCDM model. Feedforward and feedback explanations were developed to summarize and interpret this output, to help groups manage disruption breakpoints. To support understanding of MCDM outputs and how to proceed, interpretive statements were added to tabular and graphical displays of MCDM results. Where the results revealed incomplete or inconsistent information in the group’s modeling results, the feedback guidance screen incorporated cues to repeat the decision step or move backwards in the decision model. Where results suggested complete and consistent information, the group was cued to move forward in the model. An example of a feedforward explanation within the Select Alternative (Step 6) of the MCDM follows:

## GRAPH ALTERNATIVE SCORING

The purpose of this step is to graphically represent the scores of the different alternatives using the combination of weights and ratings chosen previously by the group. This graph provides a way to compare the alternatives. As an alternative approaches 100, it more closely matches the group’s ideal solution.

At this point, the group may choose to go back to CALCUATE SCORING in order to choose another combination of weights and ratings and graph the scores using this option. The group may also elect to delete the alternative(s) with low scores.

An example of a cognitive feedback explanation within the Ratings of Alternatives (Step 4) of the MCDM follows:

<table><tr><td colspan="3">RATINGS OF ALTERNATIVES (2/2)</td></tr><tr><td>CRITERION ID#</td><td>AVERAGE RATING</td><td>LOW/HIGH</td></tr><tr><td>Alternative #1:</td><td></td><td></td></tr><tr><td>***criterion 1</td><td>6.0</td><td>3/9</td></tr><tr><td>criterion 2</td><td>3.5</td><td>3/4</td></tr><tr><td>criterion 3</td><td>5.5</td><td>5/6</td></tr><tr><td colspan="3">Alternative #2</td></tr><tr><td>criterion 1</td><td>3.5</td><td>3/4</td></tr><tr><td>***criterion 2</td><td>5.0</td><td>2/8</td></tr><tr><td>criterion 3</td><td>6.0</td><td>5/7</td></tr></table>

\*\*\*These ratings show a discrepancy that should be discussed further.

To summarize, cognitive feedback and feedforward explanations were embedded in all six major parts of the MCDM process. Within Gregor and Benbasat’s (1999) classification scheme, the explanations were supportive in their content (since reasoning was justified by linking the explanation to knowledge from which it was derived), multimedia in presentation format (since tables and graphs were provided in addition to text), and included both generic (always applicable) and case-specific (customized to the group) information. The guidance was provided automatically and did not require that group members explicitly ask for assistance. If group members repeated steps within the model (e.g., entering preference weights, displaying differences in alternative ratings), guidance was provided each time that the step was executed.

## 3.3. An Experimental Evaluation

Seventeen groups used the MCDM GDSS with the guidance capabilities outlined in Table 1. We compared these groups to 18 control groups that used the same MCDM GDSS without guidance. We first assessed the direct effects of guidance on group outcomes as follows:

Hypothesis 1. Groups receiving automated guidance will achieve higher consensus on their solution decisions than groups receiving no guidance.

Hypothesis 2. Groups receiving automated guidance will achieve greater model understanding than groups receiving no guidance.

Hypothesis 3. Groups receiving automated guidance will take more time to reach their decision than groups receiving no guidance.

Hypothesis 4. Groups receiving automated guidance will have more positive perceptions of the group decision process and outcomes than groups receiving no guidance.

Hypothesis 5. Groups receiving automated guidance will have more positive perceptions of the MCDM GDSS than groups receiving no guidance.

Next we assessed the mediating effect of user understanding of MCDM. In this way we could determine whether improvement in group outcomes was, indeed, due to improved user understanding of the modeling process (per Dhaliwal and Benbasat’s (1996) conjecture).

Hypothesis 6. Groups that achieve greater model understanding during the decision process will have more positive outcomes and perceptions than groups that achieve lower model understanding.

MBA students and upper level undergraduate student groups drawn from courses in which they worked together in teams participated in the study, with a balanced number of MBA and undergraduate groups assigned to each condition. Group size ranged from three to six members, though most groups had three or four members. Groups chose a preferred time slot to participate in the study, and we randomly allocated the time slots to one of the two experimental conditions. Participation in the research was voluntary, and students were given a modest number of course points for their participation.<sup>3</sup> Prior to the start of the experiment, all groups were given training in the MCDM GDSS in the form of a printed training guide and verbal instructions highlighting material in the guidebook. Training procedures were similar to those used by Dickson et al. (1991) in an earlier study with the same MCDM GDSS.

“The Foundation Task,” in which decision makers are asked to allocate a sum of \$500,000 among six competing philanthropic projects, was completed first by individual group members (to form a baseline of predecisional consensus), then by groups, and then again by individuals (to assess consensus). The background information provided to the decision makers does not allow them to choose an obvious best solution. Limayem (1992) provides detail on the use of this task for MCDM problem solving in groups. The Foundation Task is a multicriteria problem because it requires that decision makers define and weight criteria as well as choose among alternative problem solutions. The task is especially challenging for groups due to the need to collect and reconcile individual values on criteria, alternatives, weightings, ratings, and so on, in order to reach a group decision. Further information on the task, its procedures, and its scoring is available in DeSanctis et al. (1989), Dickson et al. (1991, 1993), Watson (1987), and Watson et al. (1988).

3.3.1. Procedure. The experiment took place in a group decision support system laboratory with tables arranged in a U-shaped pattern, swivel chairs with a computer terminal in front of each chair, and a projection facility at the front of the tables that constituted a public screen. Each group member first was asked to read a background statement for the Foundation Task and to allocate funds across the six competing projects, based on their personal judgment. They then were given training in MCDM GDSS use with guidance or without guidance depending on their experimental condition. Groups in the control condition used the system as described in the section “The MCDM GDSS” above. Groups in the automated guidance condition used the version of the system as described in “Implementing Guidance” above. Group members then worked together using the MCDM GDSS to allocate funds to the six projects requesting support. When a decision was reached, the group submitted a form reflecting its final allocation of funds. Then each group member filled out a post-meeting questionnaire to again individually allocate the \$500,000 to the six projects and to rate their perceptions of the meeting process, outcomes, and the MCDM GDSS technology.

3.3.2. Measurement. Group performance was measured in three ways: degree of group consensus, understanding of the MCDM modeling process, and amount of time spent formulating the group decision. Group consensus was measured using Spillman, Bezdek and Spillman’s (1980) formula as described by Watson et al. (1988). The formula uses a fuzzy set algorithm that identifies the degree of agreement among n group members on a set of i alternatives by identifying the degree of overlap in preference matrices for all possible pairs of alternatives $a _ { i } a _ { j }$ for all members of the group. The preference matrices of group members are compared to identify their degree of agreement, with the result scored on a scale ranging from zero (no overlap) to one (complete overlap).<sup>4,5</sup>

Model understanding was measured as a multiple choice test and included questions related to the MCDM inputs, computation, and outputs. Our approach to developing and validating this instrument proceeded as follows. First, multiple choice questions were generated to assess declarative and procedural knowledge about MCDM inputs, computation, and outputs. Second, the questions were reviewed and edited by several MCDM experts (operations researchers) who were familiar with the multicriteria model and the MCDM GDSS. Finally, the instrument was administered to 12 groups that participated in a pilot test and validated via interview and observation of the group members. The final version of the instrument consisted of 15 multiple choice questions.<sup>6</sup>

Decision time was measured as the number of minutes between the time when the group began the task (i.e., following training in the MCDM GDSS) and the time they announced they had reached a group decision.

Perceptions of the decision process and outcomes were measured as five self-report scales. (1) Perceived decision quality was based on an 8-item scale developed by

Gouran, Brown and Henry (1978) and used in earlier studies of group decision making and GDSS (DeSanctis et al. 1989, Easton et al. 1989, Niederman and DeSanctis 1996, Sambamurthy 1989, Watson et al. 1988, Zigurs et al. 1988). Cronbach’s alpha for this scale in our sample was 0.87. (2) Decision scheme satisfaction was measured using a 5-item scale developed by Green and Taber (1980) which also was used by Watson et al. (1988), Zigurs et al. (1988), Sambamurthy (1989), Easton et al. (1989), and Niederman and De-Sanctis (1996). Cronbach’s alpha for the scale in our sample was 0.90. (3) Decision confidence was measured using an 8-item scale developed and validated by Sambamurthy (1989) and indicates how committed group members were to their group’s decision and their beliefs about its appropriateness given the problem at hand. Cronbach’s alpha for this scale in our sample was 0.85. (4) Post-meeting understanding was measured as the extent to which group members understood others’ viewpoints at the end of the meeting. (5) Perceived depth of evaluation was the degree to which group members felt they critically assessed the alternatives and considered all the viewpoints in the group before making their final decision. Scales (4) and (5) consisted of two items each and were developed and validated by Sambamurthy (1989) and Niederman and DeSanctis (1996). Reliabilities for the scales in the current sample, based on Cronbach’s alpha, were 0.87 and 0.89, respectively.

We measured perceptions of the MCDM GDSS via three self-report scales of 4, 4, and 5 items respectively. Comfort indicated the degree to which group members enjoyed using the MCDM GDSS. Respect referred to the group appreciation of the system and the value they place on the support provided by the MCDM GDSS. Finally, challenge indicated the sense of achievement resulting from the use of the system. All three scales were developed and validated by Sambamurthy (1989) and used here in the same form as in his study. Reliabilities for the current sample, using Cronbach’s alpha, were 0.87, 0.86, and 0.85, respectively.

For all variables except decision time, which was based on a true group measure, and consensus, which was calculated using Spillman’s formula (see above), individual scores were averaged to create a group score. The analyses reported in the next section are based on these group scores.

## 3.4. Results

Means, standard deviations, and a summary of significant differences between guidance and control condi tions for all dependent variables are shown in Table 2. We first tested the moderating impact of group size and pre-meeting consensus on the dependent variables using a multivariate analysis of covariance (MAN-COVA) model. The results showed no significance in the covariates or their interaction. We then proceeded to test the hypotheses with multivariate analysis of variance (MANOVA) models. Assumptions of analysis of variance were met for these models, with the excep tion that the assumption of homogeneity of variancecovariance was violated for four of the 11 dependent measures (based on the H statistic distribution,<sup>7</sup> $p <$ 0.05). Since the number of observations in each condition was nearly equal, the violations should not meaningfully affect the analysis (Box 1954, Hair et al. 1995, Hayes 1981). Following the multivariate procedures, we ran 11 separate t-tests to test the hypothe sized differences between guidance groups and control groups. Although the t-test is robust, it requires independent samples, approximately normal distributed data, and equal population variances (Hayes 1981). Distributions for all dependent variables were normal (based on the Kolmogorov-Smirnov statistic, Hayes 1981). For the measures of model understanding, postmeeting understanding, and comfort and challenge, the approximate t-test was used with separate variance estimates. Pooled variances were used for all dependent variables where variances within treatments were not significantly different. Two-tailed tests were used in all cases. To control for the experiment-wise error rate associated with multiple t-tests, we applied Bonferonni’s adjustment to the decision criteria for tests of significance (i.e., the significance level of alpha was divided by the number of dependent variables in the model). Results indicated that automated guidance groups had greater model understanding and took more time to reach a decision than control groups. Group perceptions regarding their decision outcomes and the MCDM GDSS technology were more positive in the automated guidance condition than in the control condition, with the exception that there was no difference in decision confidence for the MCDM GDSS technology. These results generally support H2 through H5.

As a test of Dhaliwal and Benbasat’s (1996) conjecture that decision improvements from system explanation systems should be attributable to user learning about the modeling process, we used a Partial Least Squares procedure to estimate the path relationships among the major constructs in our research model (Figure 1). PLS-Graph version 2.91.02 (Chin 1994) was used to perform the analysis. Tests of significance for all paths were conducted using the bootstrap resampling procedure (Efron and Tibshirani 1993).<sup>8</sup> The estimated path effects and associated t-values are shown in Figure 2. All significant paths $( p < 0 . 0 5 )$ are indicated with an asterisk. Findings confirmed the earlier MANOVA analyses showing improvement in model understanding for groups using automated guidance, with a high explained variance in model understanding due to decision guidance $( R ^ { 2 } = 0 . 7 9 8 )$ . The paths linking model understanding and the remaining outcome variables are all significant, though the explained variance for consensus, decision confidence, challenge, respect, and time are low $( R ^ { 2 } < 0 . 2 0 )$

As a final test of the mediating role of model understanding, we applied Baron and Kenney’s (1986) approach for testing mediation via a series of regression equations that model the relationships among the mediator, an independent variable, and an outcome variable. The results were generally consistent with the PLS analysis. Considered together, the hierarchical regression and structural equation modeling analyses suggest that model understanding mediates decision scheme satisfaction most strongly. There are significant mediational paths for all of the other variables, but the strength of the mediation effect varies from relatively strong (decision quality, depth of evaluation, post meeting understanding, comfort) to relatively weak (consensus, decision time, decision confidence, challenge, respect).

Table 2 Means (Standard Deviations) and Tests of Differences Between Guidance and Control Groups

<table><tr><td>Dependent Variables</td><td>Automated Guidance (treatment) N = 17</td><td>No Guidance (control) N = 18</td><td>df</td><td> $t^b$ </td></tr><tr><td colspan="5">Objective variables (MANOVA test: Wilks lambda = 0.19, F = 39.97, df = 3.29, p &lt; 0.000)</td></tr><tr><td>Consensus</td><td>0.61 (0.23)</td><td>0.47 (0.17)</td><td>33</td><td>2.10</td></tr><tr><td>Model understandinga</td><td>14.63 (0.32)</td><td>11.78 (0.98)</td><td>20.7</td><td>11.68**</td></tr><tr><td>Decision time</td><td>70.18 (16.35)</td><td>55.56 (14.76)</td><td>33</td><td>2.78**</td></tr><tr><td colspan="5">Perceptions of the group decision process and outcomes (MANOVA test: Wilks lambda = 0.25, F = 15.95, df = 5.27, p &lt; 0.000)</td></tr><tr><td>Perceived decision quality</td><td>5.73 (0.41)</td><td>4.91 (0.60)</td><td>33</td><td>4.70**</td></tr><tr><td>Decision scheme satisfaction</td><td>4.25 (0.35)</td><td>3.33 (0.32)</td><td>33</td><td>8.27**</td></tr><tr><td>Decision confidence</td><td>5.31 (0.51)</td><td>4.56 (1.71)</td><td>33</td><td>1.74</td></tr><tr><td>Post-meeting understandinga</td><td>5.89 (0.40)</td><td>4.32 (1.80)</td><td>19.95</td><td>3.63**</td></tr><tr><td>Depth of evaluation</td><td>5.51 (0.55)</td><td>4.27 (1.65)</td><td>33</td><td>2.93**</td></tr><tr><td colspan="5">Perceptions of the MCDM GDSS (MANOVA test: Wilks lambda = 0.80, F = 2.42, df = 3.29, p &lt; 0.09)</td></tr><tr><td>MCDM GDSS comforta</td><td>5.42 (0.42)</td><td>4.72 (0.87)</td><td>24.91</td><td>3.06**</td></tr><tr><td>MCDM GDSS respect</td><td>5.30 (0.55)</td><td>4.73 (0.84)</td><td>33</td><td>2.35*</td></tr><tr><td>MCDM GDSS challengea</td><td>4.75 (0.36)</td><td>4.20 (0.73)</td><td>24.89</td><td>2.86**</td></tr></table>

<sup>a</sup>For these variables, the two conditions had unequal variances. Thus, the approximate t-statistic was used.

3.4.1. Followup Analysis. As a followup, exploratory analysis, we viewed videotapes of each group and took notes of what we thought were important issues and incidents. We made general observations about each group and then compared our notes for the guidance and control conditions. Our approach was very descriptive; we did not attempt systematic coding or counting of behaviors. Reviewing our notes, we observed that groups with guidance moved more smoothly through the decision process and were less likely to skip steps, avoid conflict resolution, or take unnecessary detours in their decision process. At times the discussions were contentious as group members articulated differences in viewpoint and attempted to persuade each other of one perspective or another. But group members appeared to trust the technology and accept its instruction; they rarely questioned or criticized the guidance. Guidance groups seemed to benefit from the flags placed by the system on items exhibiting disagreements in votes or ratings. Guidance groups tried hard to resolve their differences, eliminate the flags, and move through the MCDM process as smoothly as possible. The following kinds of comments were typical in groups supported by decisional guidance: “the system will tell us what to do next,” “there’s a flag, we should be careful,” “this is easy,” and “we should go back and better refine our criteria.”

Groups using the MCDM GDSS without decisional guidance, on the other hand, seemed more puzzled and confused by the MCDM technique. They were more likely to ask the experimental administrator questions about the task, experimental procedures, or the technology. Statements reflecting frustration of one sort or another were common. For example, “I don’t understand the purpose of this step,” “What should we do next?” “I have no idea why we are doing this,” or “Can we skip this step?” These groups appeared to sometimes overlook mistakes they made when executing some model components, leading to a ineffective or “ironic” (Poole and DeSanctis 1990) appropriation of the MCDM model. One of the more frequent blunders made by control groups when using the MCDM model was the use of vague or equivocal criteria which, in turn, led to problems during the evaluations of how well each alternative met the specified criteria. We also noted a trend among control groups to rely on one member of the group to play the role of a leader, teacher, or a facilitator for the others; one member seemed to dominate and serve as the person who answered questions about the MCDM model or gave direction to the others on how to proceed.

Figure 2 Results of PLS Analysis  
![](/api/attachments/S4E6X35V/fulltext/images/67085f60ee650ceecf3b40649da851ba07945a565b7d2e76499a93e0537a7fe5.jpg)  
Note. Tests of significance for all paths were conducted using the bootstrap resampling procedure (Efron and Tibshirani 1993).

## 4. Conclusion

In contrast to prior studies of MCDM and MCDM GDSS usability, we were able to show significant improvements in some outcomes when decision makers were guided in their use of MCDM GDSS with cognitive feedback and feedforward explanations. The automated guidance was implemented within a MCDM GDSS which, like other MCDM GDSS technologies, had been shown to be user-friendly (DeSanctis et al. 1994) but lacked the ability to yield important performance advantages (Dickson et al. 1991, 1993). We found that decisional guidance enabled groups to achieve greater model understanding and more positive perceptions of decision satisfaction, decision quality, post-meeting understanding, depth of evaluation, and comfort, respect and challenge with the technology. Group consensus and confidence did not directly improve with use of guidance. But our path analysis suggested that decision guidance improved understanding of the MCDM modeling process which, in turn, led to increases in consensus, decision quality, depth of evaluation, post meeting understanding, comfort, challenge, and respect. The mediating role of model understanding was not as strong as we anticipated for some of the variables, especially group consensus.

We leave it to future research to more fully explore whether model understanding can, indeed, lead to the range of objective and perceptual benefits that theory would predict. Two posers for researchers are, first, as Gregor and Benbasat (1999) point out, that learning and performance are closely linked and nearly always confounded; for example, it may be that a gain in consensus or depth of evaluation is behavioral evidence of greater learning about MCDM on the part of groups using guidance. To conceptually and empirically sort out the relationship between model understanding and outcomes is complex to say the least. Second, model understanding in the case of group decision makers includes both cognitive and interactive components and finding the ideal mix of these types of support may be difficult. How much support and of which sort will yield the greatest “payoff” in terms of improved user understanding and outcomes? Our satisfaction data suggest that significant improvements in perceived value can be obtained, but a more thoroughgoing study of the support-learning tradeoff may be critical to the long-term success of intelligent explanations systems.

There are, of course, important limitations that limit the scope of our design work and our experimental results. We incorporated guidance within one general MCDM GDSS; we did not fully expound the ways in which guidance might be added to more elegant or varied groupware systems or MCDM models. We implemented guidance only within an additive compensatory modeling approach. We tested the software on one multicriteria problem, and we examined a limited sample of student groups. The generalizability of our guidance design approach to other software systems, user populations, and problem contexts is yet to be explored. Finally, our guidance approach included the set of capabilities noted in Table 1. Future work might endeavor to isolate the relative impact of these guidance mechanisms across specific locations of the MCDM model. In concert with prior literature (see Balzer et al. 1989 for a review), we do not believe it worthwhile to focus on separating the effects of feedback and feedforward in MCDM; existing research clearly shows the need to combine these mechanisms in order to enhance user understanding. Rather, the lurking issue for further study is to identify at which points in the modeling process guidance is most powerful in its ability to enhance user understanding. If explanations could be designed to focus on those critical junctures, perhaps understanding of the modeling process could be deepened and the time required to use modeling systems could be reduced (rather than increased, as was the case in our study). Given the time pressures of modern organizational life, it seems critical that decision modeling systems be viewed by potential users as not only useful but efficient if they are truly to make their mark in everyday settings such as group meetings. The motivational “cost” of explanation facilities is that they take time to use and apply (Gregor and Benbasat 1999). Our system tried to limit user effort by making the explanations simple, automatic, and supportive (rather than prescriptive). But to the extent that learning can be further promoted without increasing user time requirements, greater acceptance of MCDM might result.

To conclude, our study is preliminary but offers the following contributions: It bridges research in knowledge-based explanations for DSS with GDSS research. It provides operationalization of the decisional guidance construct in the complex setting of MCDM and GDSS. It provides further evidence for Dhaliwal and Benbasat’s (1996) conjecture that cognitive feedback and feedforward explanations can jointly improve DSS success if they promote greater user understanding of underlying decision models, and it bolster’s Gregor and Benbasat’s (1999) view that supportive, multimedia, and case-specific explanations can reduce cognitive load and thereby foster greater usability of intelligent explanation systems. Our study moves GDSS beyond the study of human interventions for improving user outcomes (e.g., facilitation) into the realm of machine-based interventions to support group interaction and decision making and demonstrates the potential value of research on intelligent assistants to enhance MCDM success. Given the rather dismal state of affairs in the current literature with regard to usability of MCDM in general and MCDM GDSS in particular, further development and experimentation with the guidance concept would appear to be worthwhile.

## Acknowledgments

This research was supported by National Science Foundation grant SES-9109167 to G. DeSanctis, M. S. Poole, and G. W. Dickson and a grant from the Research Grants Council of the Hong Kong Special Administrative Region, China (Project No. CityU 1200/00H). The views expressed are those of the authors and not of the research sponsor. The authors gratefully acknowledge Janet Kelly, Barbara Klein, Joo Eng Lee-Partridge, Diane Lending, and Chelley Vician for their help with data collection for this study, and Wynne Chin for his helpful comments on an earlier version of this paper.

## References

Angehrn, A. A., T. Jelassi. 1994. DSS research and practice in perspective. Decision Support Systems 12(4) 267–275.

Anson, R., R. Bostrom, V. Wynne. 1995. An experiment assessing group support system and facilitator effects on meeting outcomes. Management Sci. 41(2) 189–208.

Balzer, W. K., M. E. Doherty, R. O’Connor. 1989. Effects of cognitive feedback on performance. Psychological Bull. 106 410–433.

Baron, R. M., D. A. Kenny. 1986. The moderator-mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations. J. Personality and Social Psych. 5(16) 1173–1182.

Benbasat, I., L-H. Lim. 1993. The effects of group, task, context, and technology variables on the usefulness of group support systems: A Meta-Analysis of Experimental Studies. Small Group Res. 24(4) 430–462.

Bird, S. D., G. M. Kasper. 1995. Problem formalization techniques for collaborative systems. IEEE Trans. Systems, Man, and Cybernetics 25(2) 231–242.

Bjorkman, M. 1972. Feedforward and feedback as determiners of knowledge and policy: notes on a neglected issue. Scand. J. Psych. 13 152–158.

Box, G. E. P. 1954. Some theorems on quadratic forms applied in the study of analysis of variance problems: 1. Effect of inequality of variance in the one-way classification. Ann. Math. Statist. 25 290–302.

Brockhoff, K. 1985. Experimental test of MCDM algorithms in a modular approach. European J. Oper. Res. 22 159–166.

Buchanan, J. T. 1994. An experimental evaluation of interactive MCDM methods and the decision making process. J. Oper. Res. Soc. 45(9) 1050–1059.

——, H. G. Daellenbach. 1987. A comparative evaluation of interactive solution methods for multiple objective decision models. European J. Oper. Res. 29 353–359.

Buede, D. 1992. Software review: Overview of the MCDA software market. J. Multi-Criteria Decision Anal. 1 59–61.

——, D. Maxwell. 1995. Rank disagreement: A comparison of multicriteria methodologies. J. Multi-Criteria Decision Anal. 4 1–21.

Bui, X. T. 1984. Building effective multiple criteria decision models: A decision support system approach. Systems, Objectives, Solutions. Association for Computing Machinery, New York, 4 3– 16.

——, M. Jarke. 1984. A DSS for cooperative multiple criteria group decision making. Proc. Internat. Conf. Inform. Systems 101–113.

Cass, K., T. J. Heintz, K. M. Kaiser. 1992. An investigation of satisfaction when using a voice-synchronous GDSS in dispersed meetings. Inform. Management 23(10) 173–182.

Cats-Baril, W. L., G. P. Huber. 1987. Decision support systems for ill-structured problems: An empirical study. Decision Sci. 19 350–372.

Chin, W. W. 1994. PLS-Graph manual. University of Calgary, 2500 University Drive N.W. Calgary, Alberta, Canada T2N 1N4.

Clawson, V. K., R. P. Bostrom, R. Anson. 1993. The role of facilitator in computer-supported meetings. Small Group Res. 24 547–565.

Dennis, A. R., B. Haley, R. J. Vandenberg. 1996. A meta-analysis of effectiveness, efficiency, and participant satisfaction in group support systems research. J. I. DeGross, S. Jarvenpaa, and A. Srinivasan, eds. Proc. Seventeenth Internat. Conf. Inform. Systems. Cleveland, OH. 278–289.

DeSanctis, G., M. D’Onofrio, V. Sambamurthy, M. S. Poole. 1989. Comprehensiveness and restriction in group decision heuris-

tics: effects of computer support on consensus decision making. Proc. Tenth Internat. Conf. Inform. Systems. Boston, MA. 131–140.

——, J. R. Snyder, M. S. Poole. 1994. The meaning of the interface: A functional and holistic evaluation of a meeting software system. Decision Support Systems: Internat. J. 11 319–335.

Dhaliwal, J. S., I. Benbasat. 1996. The use and effects of knowledgebased system explanations: Theoretical foundations and a framework for empirical evaluation. Inform. Systems Res. 7(3) 342–362.

Dickson, G. W., G. DeSanctis, M. S. Poole, M. Limayem. 1991. Multicriteria modeling and “what if” analysis as conflict management tools for group decision making. Proc. 11th Internat. Decision Support Systems Conf. The Institute of Management Sciences, Providence, RI.

——, J. E. Lee-Partridge, L. Robinson. 1993. Exploring modes of facilitative support for GDSS technology. MIS Quart. 17(2) 173– 194.

——, M. S. Poole, G. DeSanctis. 1992. An overview of the Minnesota GDSS research project and the SAMM system. R. P. Bostrom, R. Watson and S. T. Kinney, eds. Computer augmented teamwork: A guided tour. Van Nostrand Reinhold, New York. 163–179.

Dyer, J. S., P. C. Fishburn, R. E. Steuer, J. Wallenius, S. Zionts. 1992. Multiple criteria decision making, multiattribute utility theory: The next ten years. Management Sci. 38(5) 645–654.

Easton, A. C., D. R. Vogel, J. F. Nunamaker, Jr. 1989. Stakeholder identification and assumption surfacing in small groups: An experimental study. Proc. Twenty-Second Ann. Hawaii Internat. Conf. System Sci. 3 344–352.

Efron, B., R. J. Tibshirani. 1993. An Introduction to the Bootstrap. Chap man and Hall, New York.

Evans, G. W. 1984. An overview of techniques for solving multiobjective mathematical programs. Management Sci. 30 1268–1282.

Friedman, P. 1989. Upstream facilitation: a proactive approach to managing problem-solving groups. Management Comm. Quart. 3(1) 33–50.

George, J. F., A. R. Dennis, J. F. Nunamaker. 1992. An experimental investigation of facilitation in an EMS decision room. Group Decision and Negotiation 1 57–70.

Gouran, D., C. Brown, D. Henry. 1978. Behavioral correlates of per ceptions of quality in decision making discussions. Comm. Monographs 45 51–63.

Green, S. G., T. D. Taber. 1980. The effects of three social decision schemes on decision group processes. Organ. Behavior and Human Performance 25 97–106.

Gregor, S., I. Benbasat. 1999. Explanations from intelligent systems: Theoretical foundations and implications for practice. Management Inform. Systems Quart. 23(4) 497–530.

Hackman, J. R., R. E. Kaplan. 1974. Interventions into group process: An approach to improving the effectiveness of groups. Decision Sci. 5 459–480.

Hair, Jr, J., R. Anderson, R. Tatham, W. Black. 1995. Multivariate Data Analysis With Readings, 4th ed. Prentice Hall International Editions, Upper Saddle River, NJ.

Hayes, W. 1981. Statistics, 3rd ed. Holt, Reinhart and Winston, New York.

Hightower, R., L. Sayeed. 1996. Effects of communication mode and prediscussion information distribution characteristics on information exchange in groups. Inform. Systems Res. 7(4) 451–465.

Hiltz, S. R., D. Dufner, M. Holmes, S. Poole. 1991. Distributed group support systems: Social dynamics and design dilemmas. J. Organ. Comp. 1 135–159.

Ho, T. H., K. S. Raman, R. T. Watson. 1989. Group decision support systems: the cultural factor. In J. DeGross, J. C. Henderson, & B. R. Konsynski, eds. Proc. Tenth Internat. Conf. Inform. Systems. Association for Computing Machinery. Baltimore, MD. 119– 129.

Keen, P., G. W., M. Scott Morton. 1978. Decision Support Systems: An Organizational Perspective. Addison Wesley, Reading, MA.

Keeney, R. L., H. Raiffa. 1976. Decisions with Multiple Objectives. John Wiley, New York.

Kottemann, J. E., F. D. Davis. 1991. Decisional conflict and user acceptance of multicriteria decision-making aids. Decision Sci. 22 918–926.

Limayem, M. 1992. Automating decision guidance: design and impacts in a group decision environment. Unpublished Ph.D. dissertation, University of Minnesota, Minneapolis, MN.

Mackay, J. M., J. J. Elam. 1992. A comparative study of how experts and novices use a decision aid to solve problems in complex knowledge domains. Inform. Systems Res. 3 150–172.

Malloy, T. E., C. Mitchell, O. E. Gordon. 1987. Training cognitive strategies underlying intelligent problem solving. Perceptual and Motor Skills 64 1039–1046

Minch, R. P., G. L. Sanders. 1986. Computerized information systems supporting multicriteria decision making. Decision Sci. 17(3) 395–413.

Narasimhan, R., S. K. Vickery. 1988. An experimental evaluation of articulation of preferences in multiple criterion decision-making (MCDM) methods. Decision Sci. 19 880–888.

Neter, J., W. Wasserman, M. H. Kuther. 1985. Applied linear statistical models. Regression Analysis of Variance and Experimental Designs, 2nd ed. Richard D. Irwin, Homewood, IL.

Niederman, F., G. DeSanctis. 1996. The impact of a structured-argument approach on group problem formulation. Dec. Sci. 26(4) 451–474.

Olson, D. L., H. M. Moshkovich, R. Schellenberger, A. Mechitov. 1995. Consistency and accuracy in decision aids: experiments with four multiattribute systems. Decision Sci. 26(6) 723–748.

Poole, M. S. 1981. Decision development in small groups: I. A com parison of two models. Comm. Monographs 48 1–24.

——. 1983a. Decision development in small groups: II. A study of multiple sequences in decision making. Comm. Monographs 50(3) 206–232.

——. 1983b. Decision Development in Small Groups: III. A multiple sequence model of group decision development. Comm. Monographs 50(4) 321–341.

——, G. DeSanctis. 1990. Understanding the use of group decision

support systems: The theory of adaptive structuration. C. Steinfield and J. Fulk, eds. Perspectives on Organizations and New Information Technology. Sage, Beverly Hills, CA.

Reagan-Cirincione, P. 1991. Combining group facilitation, decision modeling, and information technology to improve the accuracy of group judgment. J. F. Nunamaker, Jr., ed. Proc. 25th Hawaii Internat. Conf. System Sci. IEEE Computer Society. 232–243.

Saaty, T. L. 1986. Axiomatic foundation of the analytic hierarchy process. Management Sci. 32 7.

Sambamurthy, V. 1989. Supporting group performance during stakeholder analysis: The effects of alternative computer-based designs. Unpublished Ph.D. dissertation. University of Minnesota, Minneapolis, MN.

Sengupta, K., T. K. Abdel-Hamid. 1993. An investigation of alternative feedback strategies in dynamic decision making. Management Sci. 39(4) 411–428.

——, D. Te’eni. 1993. Cognitive feedback in GDSS: improving control and convergence. MIS Quart. 17(1) 87–113.

Silver, M. S. 1990. Systems that support decision makers: Description and analysis. John Wiley and Sons, Chichester, UK.

——. 1991. Decisional guidance for computer-based decision support. MIS Quart. 15(1) 105–122.

Spillman, B., J. Bezdek, R. Spillman. 1980. Development of an instrument for the dynamic measurement of consensus. Comm. Monographs 46 1–11.

Steeb, R., S. C. Johnston. 1981. A computer-based interactive system for group decision making, IEEE Trans. Systems, Man, and Cybernetics SMC-11 544–552.

Tavana, M., D. T. Kennedy, P. A. Joglekar. 1996. Group decision support framework for consensus ranking of technical manager candidates. Omega, Internat. J. Management Sci. 24(5) 523–538.

Te’eni, D. 1991. Feedback in DSS: experiments with the timing of feedback. Decision Sci. 22 644–655.

Tuttle, B., M. H. Stocks. 1997. The effects of task information and outcome feedback on individual insight into their decision models. Decision Sci. 28(2) 421–442.

Vargas, Luis G. 1990. An overview of the analytic hierarchy process and its applications, European J. Oper. Res. 48 2–8.

Von Nitzsch, R., M. Weber. 1993. The effect of attribute ranges on weights in multiattribute utility measurements. Management Sci. 39(8) 937–944.

Watson, R. T. 1987. A study of group decision support system use in three and four-person groups for a preference allocation decision. Unpublished Ph.D. dissertation. University of Minnesota, Minneapolis, MN.

——, G. DeSanctis, M. S. Poole. 1988. Using a GDSS to facilitate group consensus: Some intended and unintended consequences. MIS Quart. 12(3) 463–478.

Wheeler, B. C., J. S. Valacich. 1996. Facilitation, GSS, and training as sources of process restrictiveness and guidance for structured group decision making: An empirical assessment. Inform. Systems Res. 7(4) 429–450.

Zigurs, I., M. S. Poole, G. DeSanctis. 1988. Computer support of group decision making: A communication-based investigation. MIS Quart. 12(4) 625–644.

Chris Higgins, Associate Editor. This paper was received on January 3, 1999, and was with the authors 7 months for 2 revisions.
