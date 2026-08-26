---
otero_id: 17356
otero_key: "YK8M2QNP"
title: "Studies in managerial problem formulation systems"
authors: "James F Courtney; David B Paradice"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90050-d"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Studies in managerial problem formulation systems

James F. Courtney and David B. Paradice
Texas A&M University, College Station, TX, USA

A series of projects to develop decision support systems for managerial problem formulation is described. Problem-solving theory from cognitive psychology is integrated with problem structuring techniques (cognitive mapping and structural modeling) to provide the theoretical foundation for the work. The first project involved the development and testing of graphics software to support problem formulation. Subsequent studies examined the use of this software in group decision-making, and extended the system to include a problem diagnosis module, statistical routines to test relationships before they were stored in the systems knowledge base, an advisory module, and a discovery module which searches the database for relationships as yet untested by users. Current work includes the addition of a dialectical module and extension of the system to support an organizational perspective on the management of causal knowledge.

Keywords: Problem formulation, Problem solving, Graphical interface, Decision support system, Expert system, Knowledge-based system, Automated discovery.

James F. Courtney is Tenneco Professor of Business Administration in the Business Analysis and Research Department at Texas A&M University. He received his Ph.D. in Business Administration (Management Science) from the University of Austin in 1974. His academic experience includes faculty positions at the Georgia Institute of Technology, Texas Tech University and the State University of New York at Buffalo. Other experience includes positions as Database Analyst at MRI Systems Corporation and Visiting Research Scientist at the NASA Johnson Space Center. His papers have appeared in several journals, including Management Science, Communications of the ACM, IEEE Transactions on Systems, Man and Cybernetics, MIS Quarterly, Decision Sciences, Decision Support Systems, the Journal of Management Information Systems, Database, Interfaces, the Journal of Applied Systems Analysis, and the Journal of Experiential Learning and Simulation. He is the co-developer of the Systems Laboratory for Information Management (Business Publications, 1981), a software package to support research and education in decision support systems, co-author of Database Systems for Management (second edition, Irwin Publishing Company, 1992) and Decision Support Models and Expert Systems (Macmillan Publishing, 1992). His present research interests are knowledge-based decision support systems, intelligent organizational systems and management information systems.

Correspondence to: J.F. Courtney, Business Analysis and Research Department, College of Business Administration, Texas A&M University, College Station, TX 77843-4217, USA, Tel: (409) 845-9541, Bitnet: Courtney@Tamcba.

## 1. Introduction

This paper summarizes a series of studies involving the development and testing of decision support systems (DSS) to assist in managerial problem formulation. Problem formulation refers to the process of deciding what variables are included in a problem domain and how those variables fit together and interact $[2]$ . Problem formulation has been recognized as a critical aspect of the modeling process $[5, 17,22,25]$ . If the decision-maker formulates the problem incorrectly, then a “Type III error” $[35]$ will occur; that is, the wrong problem will be solved. Since an optimal answer to the wrong problem may likely be worse than a good answer to the real problem, it makes sense to develop systems to help get the problem right. Although problem formulation studies have been reported in the literature of psychological organizational behavior, when this stream of research was initiated DSS researchers had not yet begun to develop systems to support the problem formulation process (as documented in $[9]$ ).

With this in mind, a series of projects was initiated in the early 1980's to determine how systems might be developed to support the problem formulation process. The purpose of this paper is to summarize the results of those projects and provide directions for future research in problem formulation systems. The research described here is unique even considering the more recent efforts by DSS researchers. This research stream has emphasized computer-based model development and manipulation, while other DSS-related research has emphasized computer-based automation of problem-solving heuristics. For example, Niwa [27] developed a system based on a knowledge base of experimental knowledge. This system contained rules designed to exploit a human user's ability to associate knowledge which was not related to other knowledge at the time of acquisition. The primary tool provided by the computer was an “association guidance” mechanism (i.e., heuristic) for relating pieces of knowledge. Cats-Baril and Huber [9] studied the effect of delivering heuristics for problem structuring to decision makers via computer. They found that computer-based delivery of these heuristics had no affect on any dependent variable they studied. Recently, Paradice [28] studied the use of question/answer process theory as a basis for guiding the development of cognitive maps for particularly wicked problem situations. His research suggests that systems are needed to assist problem solvers in identifying desired goal states, but such a system has not yet been developed and tested that is based on question/answer process theory.

The next section of the paper describes the theoretical foundations for this stream of research. After that, the experimental context is presented and the series of projects is described. As the research proceeded, it became clear that managerial problem formulation required a much broader view than had been taken at first. The implications of this finding are discussed in the section on future research.

## 2. Problem formulation research in cognitive psychology and systems engineering

The first research question to be faced was to determine what unique features would be required of a DSS to assist in problem formulation. Second, if such a system could be built, how could one be sure that it does indeed help a user formulate problems correctly? Answers to the first question were found in the literature on cognitive psychology and systems engineering.

Research in cognitive psychology relevant to problem formulation is based on various theories of human problem solving (see, for example, [16] or [26]). For the most part, these findings are based on rather simple problems, such as syllogisms and memorization of short word lists. The process can be described as consisting of two general phases: problem formulation (also called predecision [14,15]) and problem solving [38].

Problem formulation contains three phases [38]. Problem identification occurs when the problem solver perceives the need for a decision to be made. This phase is typically marked by concern or worry and the belief that a problem exists. Problem definition concerns the cognitive conceptualization of the problem situation. During definition, the problem solver determines the relevant properties of the problem situation. Problem structuring examines the relevant components of the problem situation in order to determine a strategy for addressing the problem. This phase is characterized by instrumental reasoning, from which a strategy for addressing the problem emerges.

Similarly, problem solving contains two phases [38]. Diagnosis occurs when the problem solver identifies a problem's causes. Consequently, causal reasoning characterizes this part of the process. Alternative generation occurs next and concerns the design of alternative courses of action.

Although convenient for discussion, this model of problem solving suggests a linear progression that may not always appear in problem solving processes. Problems, depending on the problem structure, the experience of the problem solver, and the impact of information gained at various phases, may require backtracking from later phases to earlier ones as the problem structure develops. Also, solutions to some problems give rise to other problems, implying a cyclical structure. However, the model serves the purpose of providing a means for examining an inherently unstructured process.

Experiments in problem formulation and problem solving have revealed several important characteristics of the process. The set of alternative acts that might solve a problem has been claimed to represent the inherent structure of a problem.

The ability to generate these alternative acts has been found to be positively influenced by divergent thinking $[14]$ . Subjects who exhibited divergent thinking abilities generated alternative act sets that were closer to the optimal set for a given problem. Additionally, the use of divergent heuristics increases the number of alternatives generated $[1]$ . However, the use of either convergent or divergent heuristics, as opposed to a limited heuristic strategy, resulted in high quality alternative generation. This work seems to indicate that structuring heuristics in general are supportive of the problem solving process.

As stated in [15, page 24], “The elements of decision problem structures – acts, states of the world, and outcomes – are inherent in decision tasks, and hence should be considered by a motivated decision maker who is faced with an important problem.” However, decision makers are not necessarily adept at generating these structures when they confront problems. Thus, problem solvers act with limited knowledge of problem structure, and in the worst case, produce a solution which is ineffective. If the most important part of predecision behavior from the point of view of decision analysis is developing problem structure [1,15,24,25], then aids to structuring problems should provide great benefits. Organization theorists believe that these problem structures are not only used to solve current problems, but also dictate how future information is filtered and interpreted [39]. Thus, determining the correct problem structure in a given situation has long range implications.

Studies have also shown that diagrams and images were useful in the problem understanding phase of the process $[16,31]$ . The right hemisphere of the brain, which is known to be associated with the manipulation of mental images, was found to be more active during the problem formulation phase of problem solving. Thus, it has been theorized that images and diagrams are effective ways of representing the understanding of a problem's structure $[16]$ . Paivio $[31]$ even proposed a “dual coding theory” founded on the belief that images are encoded differently in the brain than verbal and procedural knowledge.

In rather loosely related work, systems engineers developed “structural modeling” [5,17,22] and “cognitive mapping” [5], to represent the structure of a problem. These techniques, which are based on the mathematical theory of graphs, were developed independently of the research in cognitive science described above, and have little or no theoretical basis in cognition.

Cognitive maps are simply box and arrow diagrams in which boxes are used to represent variables and arrows represent relationships. Cognitive maps can also be represented in an “adjacency matrix,” formed by creating a row and column for each variable in the problem, then placing a 1 in each cell where there is an arrow from the variable in row i to the variable in column j. Zeroes are entered in other cells of the matrix. Signs may also be entered.

If weights on relationships are entered, then this is usually referred to as a structural model, rather than a cognitive map. Various matrix modeling techniques are available to analyze structural models.

Since work in cognition has indicated images were useful in problem structuring and structural modeling uses graphs to represent problem structure, it seems to follow that structural modeling would be a useful element in a decision support system to support problem formulation. The first research task was to integrate the work in these two fields and relate it to problem formulation in a DSS context. Fortunately, work in the two fields was quite compatible, even though done independently. Despite the fact that structural modeling uses both graphic and matrix forms, no software could be found to support the graphical aspect of the cognitive mapping process. Thus, the next step undertaken involved the development of graphic software to support the development of structural models of managerial problems, the domain of decision support systems.

## 3. Pracht's study

Pracht [32,33,34] developed this software, known as GISMO, a Graphical, Interactive, Structural Modeling Option. This system permits the interactive development of structural models in either graphic or tabular form. It is integrated with previously existing software for performing various kinds of mathematical analysis, including pulse analysis, matrix powering, etc. The question remained whether the system actually did help in formulating problems correctly.

To address this question, a rather complex managerial decision-making environment was needed. However, in order to know whether users were formulating problems correctly, it was necessary to know the actual problem structure. Since the actual structure of real managerial problems is not known with certainty, validation required another approach.

Validation against a simulated managerial environment was chosen for several reasons. The real relationship between variables in the simulated environment could be known by examining the source code of the simulation model. Thus, users could develop models of the simulated environment, and these could be compared to the real model (that is, the source code) to determine their accuracy. Furthermore, the initial tests in a laboratory environment could be conducted where better internal controls would ensure that the findings were derived from system use, and were not confounded by other factors.

Since it was not possible to obtain practicing managers neither in sufficient numbers nor for an appropriate length of time (several weeks) for adequate statistical power, senior business majors were used as subjects in this study. The use of student subjects continues to be debated in the literature. Some studies indicate the students respond similarly to managers, while others show them to behave differently [34]. However, the subject pool is a possible limitation of the experiment.

The Business Management Laboratory was the simulation selected. It is a rather complex simulation, requiring up to 50 decisions per round. It also provides a database and query language known as SLIM, which had been used by DeSanctis [12] and Kasper [20,21] in previous DSS studies. The SLIM database contains information on over 120 highly interrelated variables. The interaction between these variables is sufficiently complex that “finding” the underlying structure of the simulation is highly unlikely. In fact, the underlying structure is exceedingly complex. Thus, although the structure is programmed, it would not be generally described by subjects as “well structured” in the sense that a linear programming model or some other type of model (or set of such models) could be developed to reflect the structure. Consequently, subjects must create models of various aspects of the simulation in an attempt to cope with the complexity of the decision problem at hand. An informal survey conducted in class showed that many students who had made decisions in this simulated environment for 8 weeks still felt that many of the decisions were ill-structured.

Based on the research in cognition mentioned previously, it was hypothesized that subjects with good spatial ability would be most capable of using GISMO. Since Witkin's Group Embedded Figures Test had been used in several previous DSS studies and is related to spatial ability, it was used as the measurement instrument. A $2 \times 2$ factorial design was developed, based on a control group that did not use GISMO versus an experimental group that did, and field independence (high spatial ability) versus field dependence. Instruments were developed to test the ability of subjects to formulate the structure of the BML simulation. These instruments included structural models (drawn by hand by the control group), the ability to list factors important in two selected decision problems, and signed adjacency matrices filled in by the subjects.

Data analysis determined that field independents using GISMO more closely formulated the correct problem structure than any other group. Field independents without the software performed the worst of all groups. They had the cognitive ability to formulate the problem, but failed to use that ability in the absence of a tool like GISMO. Field dependents performed about the same with or without the tool. Their cognitive skills are such that they are ineffective in using the tool to formulate the problem structure.

This result may indicate that the methodology underlying automated tools is a critical factor in effective use of the tool. Where the methodology was compatible with the user's cognitive predisposition, the tool provided great support. When there was little relationship between the tool's methodological basis and the user's cognitive predisposition, the tool's impact was minimally effective.

## 4. Loy's small group experiment

Given the promising results of the Pracht study, Loy [23] decided to test GISMO in a small group decision-making context. The main objective of the experiment was to test whether small groups using GISMO would better understand the problem domain and perform better in terms of net income. However, since much of the research on small groups deals with techniques for structuring group interaction, the experiment was also designed to analyze the effect of GISMO with a structured decision process. The Nominal Group Technique (NGT) was chosen as the structured process to test because it is the most widely studied technique in the literature. Since most small groups making management decisions use an unstructured format, the NGT format was compared to “interacting groups” which were given no predefined rules regarding their interaction and were allowed to interact as they saw fit. This resulted in a $2 \times 2$ design with the factors GISMO use versus non-use, and NGT versus interacting groups. Again, BML was used as the experimental environment, and the instruments developed by Pracht were used to measure the accuracy of the problem formulation, and net income was used to measure decision quality.

One would hope that better problem domain understanding is associated with better decisions, thus, a correlation analysis was conducted to analyze the relationship between these variables. The results bear out this belief in that the correlation coefficient is between the two is 0.7 (p > r = 0.002).

Multivariate and univariate analyses of variance were conducted to test the hypotheses that the overall performance of groups as measured by decision quality and problem understanding was influenced by GISMO use, discussion format (NGT versus interacting group), and the interaction of these two independent variables. GISMO use was a significant variable in these analyses, the statistical significance being supported at an alpha level of 10 percent. Thus there is evidence to support the assertion that GISMO use helps small groups make better decisions.

There were no statistically significant differences between NGT and interacting groups for either dependent variable. Thus in this study, NGT was not found to be superior to interacting groups in terms of either decision quality or problem domain understanding.

Since Pracht's study showed that spatial ability has an effect on understanding, GEFT scores were used to develop a measure of group spatial ability and were included in the analysis. The GEFT variable was significant at an alpha of 5 percent. Thus there is evidence to support the assertion that GISMO use helps small groups to better understand a problem domain, especially when group members have high spatial ability as measured by the GEFT. The finding regarding spatial ability is consistent with Pracht's results regarding individuals.

Informal observations by the researchers and debriefing of subjects seemed to indicate that the discussions of the GISMO groups were much more focused and productive, communication was more effective, and the decision-making process went much more smoothly. Non-GISMO groups, even when using NGT, seemed to waste a great deal of time in circular discussions, and ended up rushing to make the decision at the end of the meeting (which was limited to 45 minutes for all groups). This may help to explain why GISMO groups outperformed their non-GISMO counterparts on both dependent variables, but these are opinions for which there is no statistical evidence.

NGT groups, especially those using GISMO, seemed to feel that the process was actually a hindrance and that they could have done better without it. The subjects just didn't seem to like NGT. Clearly it did not help in the decision process, at least in this environment. Again these are observations, not statistical facts, but they seem to help in understanding the result that NGT groups failed to outperform IG groups.

The results from Pracht's and Loy's studies may indicate that GISMO use provided several efficiencies that benefitted decision makers. The visual nature of the models supplemented the cognitive processes of individual decision makers, allowing them to bring cognitive capabilities to bear on the problem that otherwise may not have been utilized. Also, the graphical models provided a means to “store” a problem formulation, thus requiring less “redundant” mental effort to reformulate the strategic situation each time individuals or groups had to process results from the simulation. Taken together, these aspects of GISMO use result in a methodology that requires a lower “thinking cost” (i.e., less “units of thinking” to arrive at a decision) than would have otherwise been required [37]. On the other hand, the NGT methodology, with its regulated means of interaction, may require a higher thinking cost than perceived necessary, and thus may be perceived as a cumbersome decision-making approach.

## 5. Ata's diagnostic system

Whereas Loy made no refinements to the GISMO software, but rather tested it in a group context, Ata $[3,4,11]$ extended the system itself to include problem diagnosis. As noted earlier, problem diagnosis refers to searching for or hypothesizing about the causes of a problem. In a pioneering study based on protocol analysis, Bouwman $[8]$ found that financial analysts used relationships that he modeled as “causation trees” to diagnose financial statements. Causation trees are hierarchical diagrams similar to structural models. The root node of a causation tree is the “problem” for which potential causes are sought. For example, in financial analysis the problem might be an unexpectedly high ratio of debt to equity. Branches of the tree represent paths from the problem to variables representing base causes. For example, a high debt/equity ratio the level below the debt/equity node might simply be separate nodes for debt and equity. The debt node might have nodes under it for long-term and short-term debt. Short-term debt might be comprised of loans and accounts payable. The path from accounts payable to short-term debt to debt to debt/equity ratio is a possible explanatory path for a high debt/equity ratio (if accounts payable are unusually high).

Ata integrated Pracht's and Bouwman's work by using structural modeling techniques to represent causation trees. User models of the BML problem domain, including estimates of coefficients between pairs of variables, were inputs to Ata's system. Then, given some unexpected variation of a goal variable such as profit or sales revenue, the system used the variables and coefficients entered earlier by users to construct linear models of the problem area. Current data was dynamically extracted from the database and fed to models in an attempt to diagnose or explain the variation. If the model results were not significantly different from actual results, then the user's model was accurate and could be used as the basis for a diagnosis. If not, then the model itself was deficient and in need of improvement.

To test the system, models developed by Pracht's subjects were input and diagnoses of problem areas were attempted. This approach was very sensitive to the accuracy of the model, and the users' models were not very good. Even though GISMO helped user's formulate more accurate models, they were still not accurate enough for effective, semi-automated support of problem diagnosis. This deficiency led the way to the next project, which was designed to produce a system that could formulate more accurate representations of the BML problem domain.

## 6. Paradice's knowledge-based system

The Ata study found that many user-developed models were flawed. These errors were thought to be due to different cognitive biases identified in various studies (see $[36]$ for a review). Paradice $[29,30]$ developed SmartSLIM, a system that controlled these biases through the use of linear and higher order statistical models which used data from the SLIM database to test users' assertions about relationships in the BML domain at the time they were input. A dialogue was conducted with the user to determine whether the asserted relationship would actually be retained, and if so, to gather additional information about the relationship.

Early testing of the system indicated simple categorization of relationships into causal and noncausal classes would be inadequate for problem diagnosis. (Validation of the system is discussed below.) Put simply, the system generated models that tended to include all relationships in the knowledge base when asked to diagnose particular problems, due to the extent in which all variables in a complex managerial domain interact to some degree. These models were not very useful in structuring a particular problem context. Consequently, a revised taxonomy of managerial domain relationships, based primarily upon an analysis of relationships between data items in financial proforma statements, was developed and used [29]. In addition to representing cause and effect relationships between data items, the revised taxonomy explicitly considered the existence of data items that (1) act as upper and lower bounds on other data items, (2) redefine other data items, (3) combine with other data items to compose a data item, and (4) are correlated with other data items. The revised taxonomy supported model formulations that were much more parsimonious during the validation stage described below.

Since it was possible that an asserted relationship could be valid, but not statistically supported, the user could insert relationships even when statistical validity was not upheld. User-rejected relationships were stored in a “rejection base” for testing later by the system as additional data was added to the database.

This system also incorporated features of expert systems to represent model knowledge and provide a rather unusual advisory facility. Given a question about how to increase or decrease a target variable, the advisory module was capable of extracting relationships from the knowledge base (possibly input by different users), constructing a model of the target variable, and offering advice on what other variables could be manipulated to achieve the desired change in the target. The system used a breadth-first search to traverse a hierarchy of relationships in offering this advice. Thus, variables that most directly impacted the target variable were brought to the attention of the user first.

SmartSLIM was validated in a rather unique way. First, it was “trained” in the BML domain by inputting relationships in models developed by various users. The advisory module, along with other system features, was then used to answer the questions Pracht posed to his human subjects. One set of questions dealt with the level of confidence the respondent had in various decisions. The system’s confidence was based on various statistical measures including correlations and beta coefficients. It was confident in most marketing decisions, but not confident in the areas of plant and production, and unable to address questions in finance and administration. These results are due to deficiencies in the models used to train the system, which had few model components in production and financial areas but had well developed marketing concepts. In other words, the subjects that developed the models created models that had a strong marketing orientation. Still, the confidence levels illustrate how the system itself could use information in its own knowledge base to determine where it (and its users) needed additional knowledge.

Another test required the system to determine whether a relationship between two variables was positive, negative or zero. Eighteen (18) pairs of variables were included in the test. Pracht's subjects had identified an average of 12.9 of these relationships correctly. The system had enough information to answer only 12 of these cases, but got all 12 of those correct. Perhaps more importantly, it was correct in one case that was missed by 29 of 32 subjects and another missed by 22 subjects. Thus SmartSLIM could have afforded subjects the opportunity to improve their models, at least in the case of two relationships. In that sense the system improved on the problem diagnosis concept developed by Ata. It also demonstrated that computer-based knowledge support of the managerial domain will require complex knowledge modeling capabilities.

## 7. Billman's discovery modules

The architecture of SmartSLIM was based on Blum's RX project [7], which included a “discovery module” intended to search the database for relationships unknown to (or at least untested) by its users. The objective of this module was to improve representations of the problem domain without user direction. The rejection base was designed to support the discovery process, but only a crude implementation existed in SmartSLIM.

Billman [6] undertook the development of the discovery module. Whereas RX used statistical tests to search for relationships, Billman based her system on three different models for hypothesizing causal relationships. For brevity, only the module based on Einhorn and Hogarth's [13] model is described here. For a discussion of the other two approaches see Billman [6].

Einhorn and Hogarth develop a model of the way people evaluate the potential strength of a causal relationship between two variables. The “gross strength” measure between a potential cause x and effect y is defined by the equation:

$$
s (x, y) = T ^ {*} B ^ {*} L ^ {*} \left[ w ^ {*} C + (1 - w) S \right],
$$

where C is covariation or the frequency with which x and y occur and do not occur together, T is 1 if x precedes y in time, and is 0 otherwise, B is 1 if the change in x is large enough to be perceived and is 0 otherwise, L is a measure of the length of the causal chain between x and y, computed by multiplying the covariation of each link in the chain, w is a weight reflecting the attitude of the individual, and S is the “similarity” between the two variables. To illustrate similarity in a management context, two marketing variables might be perceived as more similar (more closely related) than a marketing variable and a production variable.

Note that if T is zero (the effect precedes the cause) the entire equation reduces to zero. The same is true for B – if the potential cause x is not recognized as such by the observer, then the equation goes to zero. Also, since covariation is between 0 and 1, the value of $s(x, y)$ decreases as the length of the causal chain from x to y increases.

One additional factor affects the perceived strength of the causal relationship, the number of other variables which may have caused the effect to occur. To account for this, the gross strength measure is reduced by a weighted sum of the gross strengths of all other possible causes. The weights reflect the perceived likelihood that the corresponding variable is the actual cause.

The Einhorn and Hogarth model is directed primarily at non-quantitative variables so that x and y either occur or do not. On the other hand, cognitive mapping and structural modeling deal with concept variables, which, in principle at least, are measurable. In developing an approach to automated discovery based on the Einhorn and Hogarth model, Billman extended the model to the case in which x and y can increase, decrease, or remain constant. Thus, her approach does not require variables that can be measured precisely, but can handle “soft data,” such as morale, stress, satisfaction, and so forth.

To describe how the approach was implemented, let $x'$ be the change in x from one period to the next. A threshold value representing B was selected (5% in the baseline case) and variables in a SLIM database were transformed using the mapping:

$$
x ^ {\prime \prime} = \left\{ \begin{array}{c l} 1 & \text { if } x ^ {\prime} > B \\ - 1 & \text { if } x ^ {\prime} <   B \\ 0 & \text { otherwise }, \end{array} \right.
$$

where the terms in braces correspond to an increase, decrease, and no change in x, respectively. Flags were set to indicate the time order of variables in the database, so that T was known. In the initial implementation, causal chain length was ignored, and only gross strength measures were calculated.

The system was tested in two ways: (1) by comparing its ability to find relationships which actually exist in the BML code, and (2) by comparing its results to a composite model built by integrating four of the best cognitive maps developed by subjects who had participated in 12 rounds of the BML simulation. Cost of goods sold was used as the test variable. There are 39 variables in BML that have an impact on cost of goods sold.

A problem arises in interpreting the gross strength measure. At what level of gross strength are we to say that a relationship has been discovered? Clearly if $s(x, y)$ approaches 1, we would say a relationship has been found, and if it approaches 0, the system believes no relationship exists. In the test case, if a gross strength of greater than 0.15 is taken as an indication that a relationship exists, then 30 of the 39 actual relationships would be “found” by the system and 6 spurious relationships would be hypothesized. The composite model based on experienced human subjects contained only 23 of the 39 relationships, but no spurious variables.

The system finds spurious relationships because it looks at the data blindly without regard to any underlying theoretical or logical rationale as a basis for a relationship. User intervention could be used to overcome this problem, suggesting a symbiotic human-machine relationship (as in [27]) in which the machine could present relationships and the human could validate them. This approach would exploit the talents of each participant. The computer would tirelessly examine combinations of variables, testing various statistical relationships or possibly drawing upon data item descriptions to direct its search through the database. The size of most complex corporate databases requires automated intervention like this. The human would then examine the relationships detected by the computer, drawing upon human judgment and experience to validate or reject relationships proposed by the computer. Thus, the computer's processing power is used to identify candidate relationships, and the human's evaluative power is used to endorse them.

## 8. Future research

Pracht's study indicated the methodological basis of an automated tool may impact the effectiveness of the tool's use. Studies need to be conducted that examine this supposition. CASE technology provides a particularly attractive environment for this study, as there are currently several methodologies that have been implemented and CASE use is becoming increasingly widespread.

Both Ata's and Paradice's work highlight the potential danger in using knowledge bases that are either flawed or incomplete. Knowledge bases are generally considered to be fragile and brittle: when they fail, they generally do not fail gracefully. Research into improving ways for a system to determine the level of it's own expertise is needed Some means for developing and using system meta-knowledge, knowledge about the system's knowledge, must be pursued. Such research could greatly reduce the fragile and brittle nature of knowledge base use.

Paradice's “rejection base” represents one of the first attempts to make use of “discarded” knowledge. His assumption in retaining this knowledge was that a relationship hypothesized by a user has an inherent worth, even if the current data does not support it. $^{1}$ He used the rejection base to drive a crude version of the discovery module prior to Billman’s work. An interesting avenue of research would be finding additional means for exploiting this “knowledge,” including heuristics for determining when rejected knowledge should be reevaluated.

Work is continuing on ways to improve the accuracy of cognitive maps produced by subjects operating in the BML domain. In an intriguing study, Hodges [18] is developing software based on dialectical theory. This software will take cognitive maps developed by users, form a diametrically opposed counter-map, and conduct a debate intended to lead the user to a fuller understanding of the problem domain and a more accurate representation thereof.

Another project under consideration would involve an attempt to develop software that would construct cognitive maps directly from documents describing problems the organization has analyzed in the past. When faced with important problems, organizations usually form a committee or task force to study the situation and make a recommendation as to how the problem should be solved. Reports produced by such teams often include a diagnosis of the problem's causes. A system that could scan these reports looking for phrases such as "A caused B" or "A was caused by B" might be able to construct at least a rough map of the environment. Rules for manual coding of such documents [5] could provide the basis for an expert system's approach to this problem. While the resulting map might not be perfect, human coders would at least have an initial map to begin with and could then take over and make the necessary corrections and additions. While the development of an automated mapper is clearly a nontrivial problem, the existence of computerized grammar and style checkers, the-sauri and other natural language processors suggest that such a system might be feasible.

One of the observations made during the course of these projects was that managerial problem formulation is not an isolated process that must be undertaken each time a problem or decision situation is faced. Rather, organizational domains, while dynamic, consist of a variable set and corresponding relationships that should be captured, made explicit and shared with appropriate people in the firm. This is made obvious by the use of a simulated environment in the projects described above. An accurate cognitive map of the BML environment, if passed from one subject group to the next, could be extremely helpful in the successors' decisionmaking activities.

Likewise, in the “real world,” mental maps are often passed from one cadre of managers to another. Decision-making processes could be improved by making those maps explicit, and storing them in a form where they can be manipulated, improved, used and shared. Exploring this hypothesis is the ultimate objective of our research now. It will hopefully lead to the development of systems for the support of “intelligent organizations,” or those that use artificial intelligence techniques at an organizational level rather than simply on narrow domain-specific problems related to only a small aspect of the organizational management process.

## 9. Summary

Problem formulation is an important part of the managerial decision-making process, but one that has only recently received much attention in the DSS literature. The series of projects described in this paper began with the objective of developing systems to support the problem formulation process. Pracht integrated concepts from cognitive psychology and structural modeling and developed graphics software to assist in problem structuring. An experiment testing the software's ability to assist in problem formulation led to the conclusion that the software was helpful to subjects with good spatial ability.

Since many management decisions are made in a group situation, Loy tested the software in a small group context. He found limited support for the contention that the software would be useful in helping groups arrive at more accurate problem formulations. Use of the Nominal Group Technique in conjunction with GISMO did not have any additional effect, and according to subject comments may have even hindered the process.

Ata extended the system to managerial problem diagnosis, and in the process discovered that his system was very sensitive to errors in model formulations. Even though GISMO was helpful in problem formulation, models developed by rather experienced subjects were still fraught with bias and were not accurate enough for an effective diagnosis.

Paradice incorporated statistical analysis and dialogues to mitigate the errors due to user bias. Validated relationships were stored in a knowledge base and an advisory system was developed to counsel users on how a target variable could be manipulated. This system was capable of answering the questions posed to Pracht's subjects at a rather high level of performance.

Billman extended the discovery module initiated by Paradice. Her work adapted that of Einhorn and Hogarth to a cognitive mapping environment. Her discovery module was able to locate relationships unknown to experienced subjects in the problem domain, but also discovered spurious relationships.

In summary, several conclusions can be drawn from these studies. First, tools can be developed to support problem formulation in a managerial domain, although one tool may not be effective in supporting all managers. Second, tools can also be developed to support managerial domain problem formulation by groups. However, the influences of group dynamics on the problem formulation process may render tools effective in some group settings ineffective in other group settings. Third, problem formulation systems can be used as a basis for supporting later stages of the problem solving process, such as problem diagnosis. When they are used in this manner, however, a critical concern must be the validity and scope of the knowledge base supporting the system. Fourth, creative aspects of problem solving, such as discovery of relationships between variables, can also be supported by computer-based systems. As the use of these system extends into the most abstract phases of the problem solving process, the interaction between the user and the system becomes more critical. Fifth, and finally, these studies have identified many interesting avenues for further research. These studies will require increasingly sophisticated systems to be developed by DSS researchers.

## References

[1] R.A. Abualsamh, B. Carlin and R.R. McDaniel, Jr., Problem Structuring Heuristics in Strategic Decision Making, Organizational Behavior and Human Decision Processes, 45 (1990) 159–174.

[2] R.L. Ackoff, Toward a System of Systems Concepts, Management Science 17, No. 4 (Jan. 1971) 661–671.

[3] N.H. Ata Mohammed, A Knowledge-Based Decision Support System for Managerial Problem Recognition and Diagnosis, Unpublished Ph.D. dissertation, (Texas Tech University, Information Systems & Quantitative Sciences Department, Lubbock, TX, 1985).

[4] N.H. Ata Mohammed, J.F. Courtney and D.B. Paradice, A Prototype DSS for Structuring and Diagnosing Managerial Problems, IEEE Transactions on Systems, Man, and Cybernetics 18, No. 6 (Nov./Dec. 1988) 899–907.

[5] R.M. Axelrod, The Structure of Decision (Princeton University Press, Princeton, NJ, 1976).

[6] B. Billman, Automated Discovery of Causal Relationships in Managerial Problem Domains, Unpublished Ph.D. Dissertation (Texas A&M University, Department of Business Analysis & Research, College Station, TX, 1988).

[7] R.L. Blum, Discovery, Confirmation and Incorporation of Causal Relationships from a Large, Time-Oriented, Clinical Data Base: The RX Project, Computer and Biomedical Research 15 (1982) 164–187.

[8] M.J. Bouwman, Human Diagnostic Reasoning by Computer: An Illustration from Financial Analysis, Management Science 29 (1983) 653–672.

[9] W.L. Cats-Baril and G.P. Huber, Decision Support Systems for Ill-Structured Problems: An Empirical Study, Decision Sciences 18, No. 3 (1987) 350–372.

[10] J.F. Courtney, G.R. DeSanctis and G.M. Kasper, Continuity in MIS/DSS Research: the Case for a Common Gaming Simulator, Decision Sciences 14, No. 3 (July 1983) 419–439.

[11] J.F. Courtney, D.B. Paradice and N.H. Ata Mohammed, A Knowledge-Based DSS for Managerial Problem Diagnosis, Decision Sciences 18, No. 3 (Summer 1987) 373–399.

[12] G.R. DeSanctis, An Examination of an Expectancy Theory Model of DSS Use, Unpublished Ph.D. Dissertation (Texas Tech University, Management Department, Lubbock, TX, Jan. 1982).

[13] H.J. Einhorn and R.M. Hogarth, Prediction, Diagnosis and Causal Thinking in Forecasting, Journal of Forecasting 1, No. 1 (1982) 23–36.

[14] P.D. Englemann and C.F. Gettys, Divergent Thinking in Act Generation, Acta Psychologica 60 (1985) 39–56.

[15] C.F. Gettys, R.M. Pliske, C. Manning and J.T. Casey, An Evaluation of Human Act Generation Performance, Organizational Behavior and Human Decision Processes 39 (1987) 23–51.

[16] J.G. Greeno, The Structure of Memory and the Process of Solving Problems, in: R.L. Solso, Ed., Contemporary Issues in Cognitive Psychology: The Loyola Symposium (Wiley, New York, 1973).

[17] F. Harary, R.Z. Norman and D. Cartwright, Structural Models: An Introduction to the Theory of Directed Graphs (Wiley, New York, 1965).

[18] W.S. Hodges, DIALECTRON: A Dialectic Engine for Strategic Planning, Ph.D. Dissertation (Texas A&M University, Department of Business Analysis & Research, College Station, TX, forthcoming).

[19] R.L. Jensen, The Business Management Laboratory Participant's Manual, (Irwin, Boston, MA, 1977).

[20] G.M. Kasper, The Effect of User-Developed DSS Applications on Forecasting Decision-Making Performance, the Journal of Management Information Systems 2, No. 2 (1985) 26–39.

[21] G.M. Kasper and R.P. Cerveny, A Laboratory Study of User Characteristics and Decision-making Performance in End-User Computing, Information and Management 9, No. 2 (1985) 87–96.

[22] G.G. Lendaris, Structural Modeling – A Tutorial Guide, IEEE Transactions on Systems, Man and Cybernetics (1980) 807–840.

[23] S.L. Loy, An Experimental Investigation of a Graphical Problem-Structuring Aid and the Nominal Group Tech-

nique for Group Decision Support Systems, Unpublished Ph.D. Dissertation (Texas Tech University, Information Systems & Quantitative Sciences Department, Lubbock, TX, 1986).

[24] H. Mintzberg, D. Raisinghani and A. Theoret, The Structure of ‘Unstructured’ Decisions, Administrative Science Quarterly 21, (1976) 246–275.

[25] I.I. Mitroff and T.R. Featheringham, On Systemic Problem Solving and the Error of the Third Kind, Behavioral Science 19, No. 6 (1974) 383–393.

[26] A. Newell and H.A. Simon, Human Problem Solving (Prentice-Hall, Englewood Cliffs, NJ, 1972).

[27] K. Niwa, A Knowledge-Based Human-Computer Cooperative System for Ill-Structured Management Domains, IEEE Transactions on Systems, Man and Cybernetics 16, No. 3 (May/June 1986) 335–342.

[28] D.B. Paradice, A Question Theoretic Analysis of Problem Formulation: Implications for Computer-Based Support, in: Questions and Information Systems (Erlbaum Publishers, Hillsdale, NJ, 1990.

[29] D.B. Paradice and J.F. Courtney, Controlling Bias in User Assertions in Expert Decision Support Systems for Problem Formulation, Journal of Management Information Systems 3, No. 1 (Summer 1986) 52–64.

[30] D.B. Paradice and J.F. Courtney, Causal and Non-causal Relationships and Dynamic Model Construction in a Managerial Advisory System, Journal of Management Information Systems 3, No. 4 (Summer 1987) 39–53.

[31] A. Paivio, Mental Representations: A Dual Coding Approach (Oxford University Press, New York, 1986).

[32] W.E. Pracht, An Experimental Investigation of a Graphical, Interactive Problem Structuring Aid for Decision Support Systems, Unpublished Ph.D. Dissertation (Texas Tech University, Lubbock, TX, 1984).

[33] W.E. Pracht, GISMO: A Visual Problem Structuring and Knowledge Organization Tool, IEEE Transactions on Systems, Man, and Cybernetics 16 (1986) 265–270.

[34] W.E. Pracht and J.F. Courtney, The Effects of an Interactive, Graphics-Based DSS to Support Problem Structuring, Decision Sciences 19, No. 3 (Summer 1988) 598–621.

[35] H. Raiffa, Decision Analysis (Addison-Wesley, Reading, MA, 1968).

[36] A.P. Sage, Behavioral and Organizational Considerations in the Design of Information Systems and Processes for Planning and Decision Support, IEEE Transactions on Systems, Man and Cybernetics 11 (1981) 640–678.

[37] S.M. Shugan, The Cost of Thinking, Journal of Consumer Research 7 (1980) 99–111.

[38] G.F. Smith, Defining Managerial Problems: A Framework for Prescriptive Theorizing, Management Science 35, No. 8 (1989) 963–981.

[39] J.B. Thomas and R.R. McDaniel, Interpreting Strategic Issues: Effects of Strategy and the Information-Processing Structure of Top Management Teams, Academy of Management Journal 33, No. 2 (1990) 286–306.
