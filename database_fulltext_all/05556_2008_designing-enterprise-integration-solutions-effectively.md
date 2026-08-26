---
otero_id: 5556
otero_key: "K438AST3"
title: "Designing enterprise integration solutions: effectively"
authors: "Karthikeyan Umapathy; Sandeep Purao; Russell R Barton"
year: "2008"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2008.39"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing enterprise integration solutions: effectively

Karthikeyan Umapathy<sup>1</sup>, Sandeep Purao<sup>2</sup> and Russell R. Barton<sup>3</sup>

<sup>1</sup>School of Computing, University of North Florida, U.S.A.; <sup>2</sup>College of IST, Pennsylvania State University, U.S.A.; <sup>3</sup>Smeal College of Business, Pennsylvania State University, U.S.A.

Correspondence: Karthikeyan Umapathy, School of Computing, University of North Florida, 3214 Mathews Building (15), Jacksonville, FL 32224, U.S.A. E-mail: k.umapathy@unf.edu

## Abstract

The design of large and complex enterprise integration solutions is a difficult task. It can require solutions that are unique because of constraints from the current set of legacy applications. Design knowledge for enterprise integration solutions is, therefore, difficult to articulate and reuse. In particular, the nature and form of knowledge for conceptual design of integration solutions is difficult to pin down. In this paper, we investigate whether design knowledge for enterprise integration in the form of patterns can be reused to develop systems integration solutions, and whether such reuse leads to more effective design outcomes. The research follows design science guidelines in which we describe a research artifact, and evaluate it to assess whether it meets the intended goals. The results indicate that approaches to facilitate reuse of conceptual design knowledge are feasible in the domain of enterprise integration, and that such reuse does, in fact, lead to more effective design solutions. European Journal of Information Systems (2008) 17, 518–527. doi:10.1057/ejis.2008.39

Keywords: enterprise integration; design science; integration patterns; speech acts; integration solutions; design knowledge

## Introduction

Enterprise integration, sometimes referred to as systems integration, is the journey that an organization undertakes to interconnect its silo-ed business functions and work practices to streamline organizational processes. The solutions often take the form of connecting stovepipe legacy applications (referred to as EAI – enterprise application integration (Markus & Tanis, 2000)) or imposing and customizing enterprise systems packages (referred to as ERP – enterprise resource planning software (Lee et al., 2003)). Regardless of the solution chosen, bottom-up EAI or topdown ERP, the integrated solutions are intended to support and facilitate cross-functional business processes (Sharif et al., 2005). Such support has been shown to be an important pre-requisite for effective participation in a competitive global market, where organizations need to be agile and flexible (Agarwal & Sambamurthy, 2002). Because of the (perceived) unique nature of each enterprise integration project and the significant organizational change burden associated with the deployment of integration solutions, much research related to the design of enterprise integration solutions is dominated by either (a) a technology perspective, for example, devising more efficient middleware implementations (Gorton, 2006), or (b) investigation of organizational concerns such as transformation and change management (Gleghorn, 2005). We acknowledge the importance of these streams of research.

Our emphasis in this paper is, however, on the ‘middle’ that is excluded by these research streams: strategies for conceptual design of enterprise integration solutions. Like other domains, the design activity for enterprise integration involves identification of issues and exploration of various design strategies that may address those issues (Gero, 1990). Design strategies can then be employed to address specific design problems, known as design knowledge (Purcell & Sodersten, 2001). In particular, we investigate whether knowledge for conceptual design of enterprise integration solutions, which is rarely codified, can, in fact, be accessed and reused; and whether such reuse contributes to more effective design outcomes. The paper briefly positions current efforts related to design of enterprise integration solutions including the form of design knowledge it utilizes, demonstrates our approach to reuse this design knowledge including the obstacles we attempt to overcome, and describes results of an empirical evaluation to assess its effectiveness.

## Designing enterprise integration solutions

The first pre-requisite for designing enterprise integration solutions is to understand integration requirements, that is, no different from other design endeavors. Integration requirements are often represented in the form of Business Process Models (BPMs) (Aalst et al., 2003b), which embody a control-flow perspective (WfMCTerminology, 1999). They represent different tasks that must be performed, and actors such as individuals and legacy systems that perform these tasks. The tasks are logically interlinked to form the end-to-end process (Zhu et al., 2004). The compiled process represents a number of constructs including the business tasks, their sequencing, decision points, and events. Representations to depict these tasks include BPM techniques which are, in part, based on ideas contained in Petri Nets (Aalst et al., 2003b). The Business Process Modeling Notation (BPMN) (BPMN, 2006), which contains these ideas, is emerging as a de facto standard. BPMN models show tasks performed by disparate systems, tasks that can be automated, kinds of exchanges that take place between systems, and areas where business rules need to be enforced (Popkin, 2005). BPMN models, thus, primarily capture details of business activities and control-flow between the tasks (White, 2004). They are composed of (Ouyang et al., 2007): (i) set of activities, each depicting business events or tasks performed by humans or software applications; and (ii) control nodes such as AND-split, AND-join, OR-split, ORjoin, XOR-split, and XOR-join. Activities and control nodes can be connected to describe end-to-end business processes. We acknowledge that the complete BPMN notation contains other constructs such as swimlanes and others. In spite of their inclusion, however, designers often choose to focus on the subset of constructs focusing on control-flows because it describes activities and order of execution (Aalst et al., 2003a).

The second pre-requisite for developing effective enterprise integration solutions is the expertise that the enterprise integration professional brings to the project. Because of the scale and complexity of large-scale enterprise integration efforts and their potential impact, such expertise (whether acquired as experience or codified as design knowledge) remains an important input to the process (Lam, 2005). Few efforts in prior research have attempted to codify conceptual knowledge for designing enterprise integration solutions. One significant exception, which in essence represents repeated patterns observed in practice, abstracted and articulated, are the Enterprise Integration Patterns (EIP) (Hohpe & Woolf, 2004). These patterns<sup>1</sup> are abstract, that is, they do not provide implementation code or wrappers; instead, they provide recurring solutions that designers adapt to solve integration problems. Examples of EIP include ‘message expiration,’ which reminds the designers to incorporate mechanisms similar to exception handling, and ‘publish-subscribe,’ which describes how channels may be designed to deliver a particular event to multiple subscribers. Of the seven categories that Hohpe and Woolfe propose (integration styles, endpoint patterns, system management patterns, channel patterns, message construction patterns, routing patterns, and transformation patterns), the first three focus on exchanging documents, producing or consuming messages, and managing performance of messaging systems, respectively. The last four outline different ways of integrating systems based on how they transport, construct, route, and transform messages, respectively. Patterns in these four categories provide abstract solutions for designing messaging mechanism between legacy applications (Hohpe & Woolf, 2004). These patterns are the focus of this research. These EI Patterns suggest possible ways to interconnect legacy applications by using messaging primitives described in message-oriented middleware for interconnecting systems (Banavar et al., 1999). Each pattern, thus, includes (i) sender(s), (ii) receiver(s), (iii) kinds of messages exchanged between senders and receivers, and (iv) descriptors such as problem context, constraints for its usage, and example scenario.

Based on the description above, we frame the problem of designing enterprise integration solutions as one that involves (a) understanding integration requirements described in BPMN models and (b) identifying EI Patterns that address these requirements. The description also makes it evident that the two – BPMN models and EI Patterns – follow different perspectives that may be incompatible. BPMN models build upon the control-flow perspective to describe tasks (business activities) and the logic of execution for the set of tasks. On the other hand, EI Patterns capture message flows that represent information and commands that are passed between actors. Put another way, the former deals with sequencing business activities, whereas the latter is concerned with interconnecting the legacy systems. In spite of the potential for reuse that the EI Patterns provide, this contrived mapping can be a significant obstacle for the designers. Mapping the two – BPMN models and EI Patterns – constitutes a non-trivial challenge for integration designers, who must utilize: (a) their understanding of integration requirements (expressed in BPMN models), and (b) their stock of design knowledge (expressed as EI Patterns). Such application of design knowledge to the problem at hand requires rules or heuristics that dictate application of the latter to the former.

A precursor to devise such rules or heuristics is a specific mediator that can help bridge the gap between the task and control-oriented specification of requirements, and the actor and information-passing-oriented articulation of design knowledge for enterprise integration. Elsewhere, we have argued for the appropriateness of speech acts (Searle, 1969) as an effective mediator for this purpose (Umapathy & Purao, 2007). We build our argument on the premise suggested by speech act theory (Searle, 1969) that language can be used not only as a signification of a situation or fact, but also to perform action (Goldkuhl & A<sup>˚</sup> gerfalk, 2000). Speech acts distinguish between illocutionary acts (actions performed by the speaker) and perlocutionary acts (intended effects on the hearer). They represent a bridge between the two perspectives because they can be (a) mapped against control-flows (with their focus on sequences of tasks) as well as (b) used to augment messaging primitives with semantic content. We develop these ideas further in the next section toward a mechanism that (a) represents actions to accomplish tasks, and (b) designs content and rules for message exchanges that accomplish those actions (Johannesson & Perjons, 2001). Together, their intent is to support interactions among participants in a business process (Lim et al., 1997).

## Knowledge reuse for designing enterprise integration solutions

Our approach to facilitate reuse of design knowledge related for conceptual design of enterprise integration solutions uses the mapping described above (and shown in Figure 1). Integration requirements are described in BPMN models that capture the logical execution of tasks along with the performer of each task. A change in the performer in adjacent tasks provides a clue for identifying interactions among tasks. These interactions are examined to discover the tasks and the cardinality of this interaction relationship (i.e., one-to-one, one-to-many, or many-to-one). This initial reasoning phase does not provide sufficient information to decide pattern(s) appropriate for a given requirement but does allow initial narrowing of the search space. To further reduce the search space (and sometimes to identify the one appropriate pattern), we utilize action types that reflect the performers’ intent for performing the task (Moore, 2001). These action types correspond to high-level business actions that the actor performs through means of communication directed toward other actor(s) (Lind & Goldkuhl, 2001). Our approach maps each task in the interaction against a small set of possible speech acts using its associated action type. Arranged to follow the set of tasks, these interactions among speech acts can finally be mapped against representation of EI Patterns, which are specified and stored as sequences of speech acts. As mentioned in the previous section, EI Patterns describe kinds of messages exchanged between systems. We represent these for each EI Pattern as a sequence of speech acts. The components necessary for realizing the above, therefore, include: (a) a parsimonious set of speech acts appropriate for representing EI Patterns, (b) representing EI Patterns as sequences of speech acts, (c) a set of action types that depict high-level business actions to categorize tasks in the BPMs, and (d) a mapping between action types and speech acts that can be used to access the EI Patterns.

![](/api/attachments/K438AST3/fulltext/images/65a3ba6d7bf383c00debc781f6f74ca66de26b9e71855edfecff5d03e8b759b3.jpg)  
Figure 1 Mapping sets of tasks against integration patterns.

The first component, a parsimonious sequence of speech acts, is obtained from a meta-analysis of prior work including that by Moore (2001) and Johannesson & Perjons (2001). This yields the speech acts: Acknowledge, Cancel, Direct, Fulfill, Inform, Propose, and Query (Umapathy & Purao, 2007). The second component requires construction of a sequence that utilizes this parsimonious set of speech acts for each EI Pattern. Figure 2 provides two examples along with the rationale for the representation. The third component, high-level business actions. to categorize tasks is obtained from business activity behaviors described in the Unified Modeling Language (UML) specification (UML, 2005). Eleven action types result from this analysis including: Accept with no receipt send, Reject with no receipt send, Invoke, Declare completion of task, Accept and send receipt, Provide information, Raise Exception, Reject and send receipt, Propose to perform task, Request for Information, and Request to cancel task. The final, fourth component, a mapping between action types and speech acts, was constructed by the researchers. As an example, the action Invoke is mapped against the speech act Direct, the action Declare completion of task is mapped against the speech act Fulfill.

![](/api/attachments/K438AST3/fulltext/images/e61274bb8d38617d8f93f0efb2dfebdfb4e44f8750883585bf1cecf97259db32.jpg)  
Figure 2 Enterprise integration patterns as sequence of speech acts.

Consider a fragment of a business process<sup>2</sup> shown in Figure 3. It depicts an integration requirement, that is, an interaction in business process among multiple performers. It involves multiple tasks (marked by numbers in the figure): a loan broker forwards information about a client as way to obtain a quote from three (N41) different banks; the banks generate a quote and respond. In this example, Task 1 is best represented by the action type ‘Accept and send receipt,’ Tasks 2–4 are best represented by the action type ‘Provide information.’ Based on the mapping between action types and speech acts, we determine that each task represents the speech act ‘Inform.’ Comparing the sequence against those available as predefined speech act sequences for EI Patterns suggests the ‘Publish-Subscribe Channel’ (see Figure 2) as an appropriate pattern. The intent in the example outlined above is to assist the designers in choosing the appropriate EI Patterns based on their interpretation of the action types, not forcing a specific interpretation of action types on the designers.<sup>3</sup>

The design artifact we have developed to facilitate this assistance to the designer includes a knowledge base (Sowa, 2000) that captures relationships and constraints among concepts such as task, action types, speech acts, and EI Patterns. The knowledge base uses OWL (OWL, 2004) to capture and express these, and utilizes the Bossam OWL Reasoner (Bossam, 2006), which allows us to make inferences about appropriate EI Patterns for a given set of tasks described in business processes. Further technical details outlining the structure of the knowledge base are available elsewhere (Umapathy & Purao, 2008). A methodology to access and reuse design knowledge for enterprise integration can utilize this artifact (which contains the knowledge base and heuristics). Designers can use it to decompose business processes into interactions, and then identify appropriate integration patterns for each identified interaction. Figure 4 shows the architecture of the design artifact. It consists of a business process diagram editor for developing BPMs, process files store is used for storing BPMs, an interaction extraction algorithm based on performer changes to identify business process fragments, a pattern inference engine utilizing the Bossam Reasoner to identify integration patterns for each process fragment, and pattern knowledge base that contains OWL knowledge base.

![](/api/attachments/K438AST3/fulltext/images/029dd228c25535e59747b26728b95de1a7fa4771537e9693148deb1978bdbc10.jpg)  
Figure 3 Sample BPMN fragment depicting an integration requirement.

![](/api/attachments/K438AST3/fulltext/images/73e36a4c3b662e399bc1de014bf767540fc40cba3fba509ae8a331c231b6b45a.jpg)  
Figure 4 Architecture of the design artifact.

## Empirical evaluation

Design science principles suggest that theoretical constructs embodied in the artifact should be evaluated to demonstrate the appropriateness and utility of their usage (Hevner et al., 2004). In our case, this means that effectiveness of the use of speech acts to access and reuse conceptual design knowledge (i.e., EIP) should be evaluated. The evidence for this would be provided by the relative effectiveness of integration solutions (Tvedt & Collofello, 1995). Toward this end, we compared integration solutions obtained with the aid of speech acts against those obtained without the aid of speech acts (Eickelmann & Richardson, 1996) following a controlled experimentation strategy (Shadish et al., 2001). A metric was developed to measure the evidence of effectiveness in the form of an assessment scheme for design errors. Measuring design errors is a complex task because there are no automated means for detecting design defects (Tahvildar & Kontogiannis, 2004). Due to lack of validated metrics to detect design errors in integration solutions, the best way to measure design errors is, therefore, to compare design solutions against those that an expert designer might develop (Purao et al., 2003). Our approach to develop the metric and the assessment scheme, therefore, contained the following elements.

First, we acknowledge that each integration pattern has its own terms of use along with constraints and tradeoffs (Wasserman, 1996; Voka´cˇ et al., 2004). As a result, improper use of a pattern can lead to design defects that can potentially cause execution failure (Alencar et al., 1999; Prechelt, 2001). These design defects can be measured by detecting design errors in the solutions (Wasserman, 1996). The effectiveness of design support for accessing and identifying patterns, consequently, can be measured in terms of the amount of design errors produced (Jankowski, 1997). Second, integration solutions are also affected by the selection of integration patterns that are consistent with one another, because the selection of patterns that constrain the interactions of other patterns can lead to internally inconsistent designs (Alencar et al., 1999). Together, the two suggest a measurement scheme that not only takes into account the traditional errors of omission and commission but also inconsistency errors. The first two account for false negatives and false positives (Fielding & Bell, 1997). False negatives are known as Type I errors that measure the completeness of solutions (Moody et al., 2002) such as requirements with no or missing patterns (Purao et al., 2003). False positives are known as Type II errors that measure the correctness of the solutions (Moody et al., 2002) such as requirements with incorrect patterns (Purao et al., 2003). Finally, inconsistency errors are Type III errors, such as requirements with inferior patterns (i.e., patterns with similar structures that can improve performance were ignored) (Moody et al., 2002). The errors were classified as major (errors that may seriously affect the execution of the integration solutions), and minor (any other errors), penalizing for former more than the latter. Table 1 provides a summary of the assessment scheme with examples.

A straightforward hypothesis then dictated the evaluation based on the following argument: effective design support will have a higher likelihood of avoiding design errors (Girczyc & Carlson, 1993), that is, designs produced with the support of speech acts will contain fewer design errors compared to designs produced without the support of speech acts. To test the hypothesis, the research prototype was modified to two versions: one with ability to design integration solution with the support of speech acts and other that required the designer to select the integration patterns (without support of speech acts).

The experimental procedure involved randomized repeated samples with different versions (with and without speech acts) for an online retailer warehouse replenishment process of a fictional online retail company. The subjects were provided a detailed BPM and requested to design an integration solution by accessing and selecting appropriate integration patterns with the aid of the research prototype. Each subject performed a list of tasks using the research prototype:

\- Run the research prototype.

\- Open a given business process.

\- Browse each process fragment in the process (i.e., integration requirement).

\- Run the speech act enhanced pattern reasoner (avail able in one version of the prototype).

\- Browse integration patterns for each interaction (shortlist in one version of the prototype).

\- Select integration pattern(s) for each interaction.

\- Submit the design summary report.

The subjects were recruited from a pool of students enrolled in an ‘Advanced Enterprise Integration’ course (second in a two-course sequence), which provides deep understanding of integration techniques across multiple application settings. To test the research hypothesis, three separate two-sample t-tests were performed for each dependent variable (Montgomery, 2001) using SPSS (SPSS, 2006).

Table 1 Design error assessment scheme

<table><tr><td rowspan="2">Error type</td><td colspan="2">Error categorization</td></tr><tr><td>Minor</td><td>Major</td></tr><tr><td>Omission errors (Type I)</td><td>N.A.</td><td>3</td></tr><tr><td>Example</td><td>All errors of Type I are considered major errors</td><td>Pattern missing for identified integration requirement</td></tr><tr><td>Commission errors (Type II)</td><td>1</td><td>3</td></tr><tr><td>Example</td><td>Using Recipient List pattern instead of Publish-Subscribe pattern</td><td>Using Splitter pattern instead of Aggregator pattern</td></tr><tr><td>Inconsistency errors (Type III)</td><td>1</td><td>3</td></tr><tr><td>Example</td><td>Using two independent Point-to-Point channel patterns instead of Request-Reply pattern</td><td>Using independent Point-to-Point channel patterns for each data types instead of Datatype channel pattern</td></tr></table>

Table 2 Descriptive statistics for Box-Cox transformed dependent variables

<table><tr><td rowspan="2"></td><td rowspan="2">Lambda (λ)</td><td rowspan="2">Sample (N)</td><td rowspan="2">Mean</td><td rowspan="2">SD</td><td colspan="2">Skewness</td><td colspan="2">Kurtosis</td></tr><tr><td>Statistics</td><td>SE</td><td>Statistics</td><td>SE</td></tr><tr><td>Omission errors</td><td>1.45</td><td>58</td><td>114.823</td><td>44.884</td><td>0.188</td><td>0.314</td><td>0.142</td><td>0.618</td></tr><tr><td>Commission errors</td><td>0.00</td><td>58</td><td>1.018</td><td>0.405</td><td>-0.029</td><td>0.314</td><td>0.232</td><td>0.618</td></tr><tr><td>Inconsistency errors</td><td>0.10</td><td>58</td><td>2.214</td><td>0.942</td><td>0.043</td><td>0.314</td><td>0.351</td><td>0.618</td></tr></table>

## Results

Several assumptions were tested for the two-sample ttests. The first was independence and normal distribution for all dependent variables (Morgan et al., 2007). Departures from normality were detected using a combination of skewness and kurtosis coefficients as well as by assessing normal probability plots (Stevens, 2002). If the absolute ratios of skewness and kurtosis to their respective standard errors are less than 2, then the assumption of normality is not rejected (Leech et al., 2007). The observation of normal probability plots and the combination of skewness and kurtosis coefficients indicated that the dependent variables did not follow a normal distribution. To correct for non-normality, Box-Cox transformations were performed. For each variable, the lowest mean square error (MSE) and the corresponding appropriate maximum likelihood estimate (l) was obtained by running the Box-Cox SPSS syntax (BoxCoxSPSS, 1998), and each variable was transformed with a Box-Cox transformation equation (Montgomery, 2001).

$$
y ^ {\lambda} = \left\{ \begin{array}{l l} \frac {y ^ {\lambda} - 1}{\lambda}, & \text {when} \quad \lambda \neq 0 \\ \log y, & \text {when} \quad \lambda = 0 \end{array} \right.
$$

Table 2 provides descriptive statistics for Box-Cox transformed variables along with the maximum likelihood estimate (l). The observation of normal probability plots and the combination of skewness and kurtosis coefficients for transformed variables indicate that they follow nearly normal distributions.

The premise of the research hypothesis is that the research prototype with speech acts has a positive effect on the dependent variables – omission, commission, and inconsistency errors. Three separate two-sample t-tests were used to assess whether different versions of the research prototype have any effect on the (transformed) dependent variables. Table 3 provides a summary for each dependent variable for different research prototype versions.

We found that with respect to omission errors, Levene’s test for assumption that the variances of the two groups are equal is violated (i.e., P40.05). Therefore, the equal variances not assumed t-test statistics was used for analysis. The result from the analysis indicates that there is a significant difference between research prototype versions for omission errors. For commission errors, Levene’s test for assumption that the variances of the two groups are equal is not violated (i.e., P40.05). Therefore, the equal variances assumed t-test statistics was used for analysis. The result from the analysis indicates that there is a significant difference between research prototype versions for commission errors. For inconsistency errors as well, Levene’s test for assumption that the variances of the two groups are equal is not violated (i.e., P40.05). Therefore, the equal variances assumed t-test statistics was used for analysis. The result from the analysis indicates that there is no significant difference between research prototype versions for inconsistency errors. Table 4 provides a summary of Levene’s test and two-sample t-test results.

The results, therefore, indicate that both omission and commission errors have significant difference between research prototype versions. Table 5 shows that 95% confidence intervals for mean difference between research prototypes for omission errors extends from 2.037 to 48.133 and for commission errors extends from 0.328 to 0.666. Because zero is not included in both intervals, the data support the hypothesis that the research prototype with speech acts produces less design errors than the research prototype without speech acts at 5% level of significance. The comparison of means test indicates a substantial relationship (0oeffect sizeo1) between design support groups and omission errors variable. The comparison of means test indicates a substantial and high relationship (effect size41) between design support groups and commission errors variable.

Table 3 Descriptive statistics for design support groups

<table><tr><td></td><td></td><td>Sample size (N)</td><td>Mean</td><td>SD</td><td>SEM</td></tr><tr><td rowspan="2">Box omission errors</td><td>Without speech acts</td><td>29</td><td>127.366</td><td>55.186</td><td>10.248</td></tr><tr><td>With speech acts</td><td>29</td><td>102.281</td><td>27.015</td><td>5.017</td></tr><tr><td rowspan="2">Box commission errors</td><td>Without speech acts</td><td>29</td><td>1.266</td><td>0.330</td><td>0.061</td></tr><tr><td>With speech acts</td><td>29</td><td>0.769</td><td>0.313</td><td>0.058</td></tr><tr><td rowspan="2">Box inconsistency errors</td><td>Without speech acts</td><td>29</td><td>2.060</td><td>1.029</td><td>0.191</td></tr><tr><td>With speech acts</td><td>29</td><td>2.368</td><td>0.836</td><td>0.155</td></tr></table>

Table 4 Two-sample t-test for each dependent variables

<table><tr><td rowspan="2" colspan="2">Dependent variable</td><td colspan="2">Levene&#x27;s test</td><td colspan="3">t-test for equality of means</td></tr><tr><td>F</td><td>Significant</td><td>t</td><td>d.f.</td><td>Significant (two-tailed)</td></tr><tr><td rowspan="2">Box omission errors</td><td>Equal variances assumed</td><td>10.198</td><td>0.002</td><td>2.199</td><td>56</td><td>0.032</td></tr><tr><td>Equal variances not assumed</td><td></td><td></td><td>2.199</td><td>40.691</td><td>0.034</td></tr><tr><td rowspan="2">Box commission errors</td><td>Equal variances assumed</td><td>0.012</td><td>0.913</td><td>5.889</td><td>56</td><td>0.000</td></tr><tr><td>Equal variances not assumed</td><td></td><td></td><td>5.889</td><td>55.836</td><td>0.000</td></tr><tr><td rowspan="2">Box inconsistency errors</td><td>Equal variances assumed</td><td>0.136</td><td>0.714</td><td>-1.251</td><td>56</td><td>0.216</td></tr><tr><td>Equal variances not assumed</td><td></td><td></td><td>-1.251</td><td>53.742</td><td>0.216</td></tr></table>

Table 5 Comparison of means for dependent variables

<table><tr><td rowspan="2">Dependent variable</td><td rowspan="2">Mean difference (A)</td><td rowspan="2">SED</td><td colspan="2">95% CI of the difference</td><td rowspan="2">Pooled SD</td><td rowspan="2">Effect size (d)</td></tr><tr><td>Lower</td><td>Upper</td></tr><tr><td>Box omission errors (equal variances not assumed)</td><td>25.085</td><td>11.410</td><td>2.037</td><td>48.133</td><td>41.100</td><td>0.610</td></tr><tr><td>Box commission errors (equal variances assumed)</td><td>0.497</td><td>0.084</td><td>0.328</td><td>0.666</td><td>0.321</td><td>1.547</td></tr><tr><td>Box inconsistency errors (equal variances assumed)</td><td>-0.308</td><td>0.246</td><td>-0.801</td><td>0.185</td><td>0.932</td><td>0.330</td></tr></table>

(A) – mean difference between design support WITHOUT speech acts and WITH speech acts. (d) – effect size d ¼ A/pooled SD, where in pooled SD is average of SD for two groups.

As the analysis above reveals, the two-sample t-tests analysis of the effects of design support levels indicated that there is a significant difference between the research prototypes – indicating a role for speech acts in support of access and reuse of conceptual design for developing enterprise integration solutions. The analysis, however, also indicates that omission and commission errors are significantly different between the two research prototype versions; and inconsistency errors are not significant. Thus, the research prototype with speech acts is effective at reducing errors caused by the selection of patterns that do not satisfy the integration requirements. This outcome points to the role that speech acts play in restricting the search space of patterns that are appropriate (i.e., potentially beneficial) for a given set of requirements.

The insignificance of inconsistency errors indicates that the research prototype with speech acts is not effective at reducing errors caused by the selection of conflicting patterns and/or inferior patterns. The research prototype did not include any indications of conflicts among selected patterns or to provide comparisons of one pattern against other related patterns. The insignificance of inconsistency errors suggests possibilities that can be explored for extending the design artifact to warn designers about conflict resolutions and to provide comparisons of related patterns.

Reflecting on what we have accomplished so far, we can characterize the design artifact (Hevner et al., 2004; Carlsson, 2006) as one that provides heuristics to designers for developing integration solutions. The description of prior research we have leveraged shows that these have been constructed with appropriate theoretical foundations (Weber, 2003), and the empirical evaluation shows that they are relevant and applicable (Brocke & Buddendick, 2006).

## Discussion

The aim of this research is to explore whether it is possible to develop approaches that can facilitate knowledge reuse for enterprise integration (a category of problems that is traditionally considered to be complex and where conceptual design knowledge is not only difficult to codify but also difficult to reuse partly due to the unique nature of design situations). We have described a design artifact that embeds a methodology for assisting designers in developing integration solutions based on design strategies represented in integration patterns. The methodology includes a speech acts-based mechanism for accessing and selecting appropriate integration patterns for designing integration solutions. To facilitate the assessment of speech acts-based mechanism, two different versions of a research prototype were developed – one embedded with a speech acts-based mechanism and another without. The two versions provided the platforms during evaluation for which subjects were drawn from an advanced enterprise integration course. Design errors in solutions developed by subjects using the two versions were compared to assess effectiveness of the speech acts-based methodology.

Drawing on Purao et al. (2002), we argue that the exact make-up of an individual who becomes an enterprise integration professional is likely to be not known. Our sample draws on individuals who have (a) worked in industry in one or more internship positions, (b) undergone a two-course sequence explicitly targeted to enterprise integration fundamentals and techniques, and (c) participated in a real-world, industry-sponsored integration project working with an external client. As a result, our sample does, at least to some extent, represent individuals who will become enterprise integration professionals. Nevertheless, we caution against using the results as definitive because a field study has not been completed with the research prototype. With this caveat, we now proceed to a discussion of the results.

Our analysis involved two-sample t-tests on the data gathered to test the hypothesis that the solutions produced using the research prototype with speech acts contains fewer design errors than the research prototype without speech acts. This evaluation shows that the speech acts-based mechanism is effective at reducing design errors, and thereby produces quality solutions.

## About the authors

Karthikeyan Umapathy is currently working as an Assistant Professor of Information Systems at the School

Further analysis showed categories that were the largest contributors to this reduction in design errors: omission and commission errors. This is a significant finding because it shows that design support similar to the one we have developed can overcome the problem of ‘reusing too much’ pointed to in prior work (Bolloju, 2004; Parsons & Saunders, 2004; Leung & Bolloju, 2005), where novice designers cannot distinguish between those parts of prior knowledge that is applicable to the current context and those that are not.

A more direct conclusion may be that prima facie, a speech acts-based mechanism for selection of appropriate integration patterns based on integration requirements is demonstrated to be effective. However, in order to develop comprehensive integration solutions, a path toward eventual implementation of the solution must be provided. Web services are likely to be ideal platform for implementing enterprise integration solutions because they are platform-independent. We are working toward extending the research prototype to generate service composition and service conversation specifications based on integration solutions. Elsewhere, we present a preliminary approach to generate such web service conversation specifications based on the patterns selected by the methodology described in this paper (Umapathy & Purao, 2006).

## Conclusion

This research was conducted in accordance with design science guidelines (Hevner et al., 2004) to develop a software artifact embedding a mechanism that helps designers develop integration solutions based on recurring solutions captured as patterns. This paper provides a rationale for using a speech acts-based mechanism for accessing and selecting appropriate integration patterns, followed by an assessment of the mechanism based on a controlled experiment for which two different versions of the research prototype were used. Results of the evaluation, which compared results produced by the version with the speech acts-based mechanism against those produced without, showed that the former is effective at reducing design errors. The findings indicate that speech act-based mechanisms can be effective in reducing the complexity surrounding challenging tasks such as design ing integration solutions. This finding also contributes to existing literature related to design knowledge reuse and reuse of patterns toward this end as well as design strategies in the context of enterprise integration. The results outlined in the paper report preliminary analyses. Additional analyses and further empirical studies are also possible and remain on our future research agenda.

of Computing, University of North Florida. He received his Ph.D. in Information Sciences and Technology from the Pennsylvania State University. His research interests are interoperability among information systems, serviceoriented computing, web services, systems integration, and IT standardization. His research works are published in various conferences such as AMCIS, Conceptual Modeling (ER), International Conference on Web Services, and Service Computing Conference; and journals such as Information Systems Frontier (ISF) and Journal of Computing and Information Science in Engineering (JCISE). Sandeep Purao is on the faculty at the College of Information Sciences and Technology, Pennsylvania State University, University Park, PA. Prior to joining Pennsylvania State University, he was on the faculty at Georgia State University. His research focuses on the design, evolution, and management of complex techno-organizational systems. His current projects include processfocused composition and monitoring of service-based systems, risk mitigation in large-scale organizational IT integration projects, and investigation of web service standardization processes. His work has been published in journals such as Communications of the ACM, IEEE Transactions on Systems, Man and Cybernetics-A, ACM Computing Surveys, and Information Systems Research; and conferences such as International Conference on Infor-

## References

AALST W, HOFSTEDE A, KIEPUSZEWSKI B and BARROS AP (2003a) Workflow patterns. Distributed and Parallel Databases 14(1), 5–51.

AALST W, HOFSTEDE A and WESKE M (2003b) Business process management: a survey. In Business Process Management (BPM): International Conference, pp 1–12 Lecture Notes in Computer Science, Springer-Verlag GmbH, Eindhoven, The Netherlands.

AGARWAL R and SAMBAMURTHY V (2002) Principles and models for organizing the IT function. MIS Quarterly Executive 1(1), 1–16.

ALENCAR P, COWAN D, DONG J and LUCENA C (1999) A pattern-based approach to structural design composition. In International Computer Software and Applications Conference (COMPSAC), (I-LING Y, Ed.). pp 160–165.

BANAVAR G, CHANDRA T, STROM R and STURMAN D (1999) A case for message oriented middleware. In International Symposium on Distributed Computing (DISC) (JAYANTI P, Ed.), pp 1–17, Bratislava.

Russell R. Barton is a Professor of Supply Chain and Information Systems in the Smeal College of Business at Pennsylvania State University, Associate Director of the Center for the Management of Technological and Organizational Change, and Co-Director of the Master of Manufacturing Management Degree Program, offered jointly by the Colleges of Engineering and Business. He has published over 70 refereed papers in the fields of applied statistics, engineering design/new product development, optimization and simulation, and authored a book entitled Graphical Methods for the Design of Experiments, published by Springer-Verlag. He is a Senior Member of the IIE and a Senior Member of the IEEE, a Board Member for the INFORMS Section on Quality, Statistics and Reliability, and the INFORMS Section on Data Mining. He was Program Chair for the 2007 Winter Simulation Conference and Past President of the 500- member INFORMS Simulation Society.

BARROS A, DUMAS M and HOFSTEDE AHMT (2005) Service interaction patterns. In Business Process Management pp 302–318, Springer-Verlag, Nancy.

BOLLOJU N (2004) Improving the quality of business object models using collaboration patterns. Communications of the ACM 47(7), 81–86.

BOSSAM (2006) Bossam Rule/OWL Reasoner. Minsu Jang. http:// mknows.etri.re.kr/bossam/FrontPage

mation Systems, IEEE Service-oriented Computing Conference, and International Conference on Conceptual Modeling. He currently serves as an Associate Editor for MIS Quarterly. He holds a Ph.D. in Management Information Systems from the University of Wisconsin-Milwaukee. He is a member of AIS, ACM, and IEEE.

BOXCOXSPSS (1998) Box-Cox Transformation SPSS Syntax. Department of Statistics. Texas A&M University, College Station, TX.

BPMN (2006) Business process modeling notation specification. Object Management Group, Inc. (OMG). http://www.bpmn.org/Documents/ OMG%20Final%20Adopted%20BPMN%201-0%20Spec%2006-02-01. pdf.

BROCKE JV and BUDDENDICK C (2006) Reusable conceptual models – requirements based on the design science research paradigm. In International Conference on Design Science Research in Information Systems and Technology (DESRIST), pp 576–604, Claremont, CA.

CARLSSON SA (2006) Towards an information systems design research framework: a critical realist perspective. In International Conference on Design Science Research in Information Systems and Technology (DESRIST), pp 192–212.

EICKELMANN NS and RICHARDSON DJ (1996) An evaluation of software test environment architectures. In International Conference on Software Engineering (ICSE), pp 353–364, IEEE, Berlin.

FIELDING AH and BELL JF (1997) A review of methods for the assessment of prediction errors in conservation presence/absence models. Environmental Conservation 24(1), 38–49.

GERO JS (1990) Design prototypes: a knowledge representation schema for design. AI Magazine 11(4), 26–36.

GIRCZYC E and CARLSON S (1993) Increasing design quality and engineering productivity through design reuse. In International Conference on Design Automation, (DUNLOP AE, Ed.), pp 48–53, ACM Press, Dallas, TX.

GLEGHORN R (2005) Enterprise application integration: a manager’s perspective. IT Professional 7(6), 17–23.

GOLDKUHL G and A<sup>˚</sup> GERFALK PJ (2000) Actability: a way to understand information systems pragmatics. In International Workshop on Organisational Semiotics. Staffordshire University, Stafford.

GORTON I (2006) A guide to middleware architectures and technologies. In Essential Software Architecture (GORTON I, Ed.), pp 41–90, Springer-Verlag, Berlin.

HEVNER AR, MARCH ST, PARK J and RAM S (2004) Design science in information systems research. MIS Quarterly 28(1), 75–105.

HOHPE G and WOOLF B (2004) Enterprise Integration Patterns. Addison-Wesley, Boston, USA.

JANKOWSKI D (1997) Computer-aided systems engineering methodology support and its effect on the output of structured analysis. Empirica Software Engineering V2(1), 11–38.

JOHANNESSON P and PERJONS E (2001) Design principles for process modelling in enterprise application integration. Information Systems 26(3), 165–184.

LAM W (2005) Investigating success factors in enterprise application integration: a case-driven analysis. European Journal of Information Systems 14(2). 175–187

L J, S K and H S (2003) Enterprise integration with ERP and EAI. Communications of the ACM 46(2), 54–60.

LFECH NL. BARRETT KC and MORGAN GA (200Z) SPSS for Intermedigte Statistics: Use and Interpretation. Lawrence Erlbaum. Associates. New York, USA.

LEUNG FSK and BOLLOJU N (2005) Object-oriented analysis using patterns: a review and research opportunities. In Pacific-Asia Conference on Information Systems (PACIS), pp 1463–1469 Bangkok, Thailand.

LIM SH, JUSTER N and PENNINGTON AD (1997) The seven major aspects of enterprise modelling and integration: a position paper. ACM SIGGROUP Bulletin 18(1), 71–75.

LIND M and GOLDKUHL G (2001) Generic layered patterns for business modelling. International Working Conference on the Language-Action Perspective on Communication Modelling (LAP).

MARKUS ML and TANIS C (2000) The enterprise systems experience – from adoption to success. In Framing the Domains of IT Management Research: Glimpsing the Future through the Past (Zmud RW, Ed.), pp 173–207, Pinnaflex Educational Resources, Cincinnati, OH.

MONTGOMERY DC (2001) Design and Analysis of Experiments. John Wiley & Sons, Inc. Hoboken, USA.

MOODY DL, SINDRE G, BRASETHVIK T and SøLVBERG A (2002) Evaluating the Quality of Process Models: Empirical Testing of a Quality Framework. Springer -Verlag, Tampere.

MOORE SA (2001) A foundation for flexible automated electronic communication. Information Systems Research 12(1), 34–62.

MORGAN GA, LEECH NL, GLOECKNER GW and BARRETT KC (2007) SPSS for Introductory Statistics: Use and Interpretation. Lawrence Erlbaum Associates, New York, USA.

O C, D M, H AHMT and A WMPVD (2007) Patternbased translation of BPMN process models to BPEL web services. International Journal of Web Services Research (JWSR) 5(1), 42–62.

OWL (2004) OWL web ontology language overview. W3C. http://www. w3.org/TR/owl-features/.

PARSONS J and SAUNDERS C (2004) Cognitive heuristics in software engineering applying and extending anchoring and adjustment to artifact reuse. IEEE Transactions on Software Engineering 30(12), 873–888.

POPKIN J (2005) Improving regulatory compliance with business process modeling. Business Integration Journal, http://bijonline.com/index.cfm?section ¼ article&aid ¼ 212.

PRECHELT L (2001) Accelerating learning from experience: avoiding defects faster. IEEE Software 18(6), 56–61.

PURAO S, ROSSI M and BUSH A (2002) Towards an understanding of the use of problem and design spaces during object-oriented system development. Information and Organization 12(4), 249–281.

PURAO S, STOREY VC and HAN T (2003) Improving analysis pattern reuse in conceptual design: augmenting automated processes with supervised learning. Information Systems Research 14(3), 269–290.

PURCELL T and SODERSTEN K (2001) Design education, reflective practice, and design research. In Design Thinking Research Symposium. Delft University of Technology, the Netherlands.

SEARLE JR (1969) Speech Acts: An Essay in the Philosophy of Language. Cambridge University, Cambridge.

S WR, C TD and C DT (2001) Experimental and Quasiexperimental Designs for Generalized Causal Inference. Houghton Mifflin Company, Boston, USA.

SHARIF AM, IRANI Z and LOVE PED (2005) Integrating ERP using EAI: a model for post hoc evaluation. European Journal of Information Systems 14(2), 162–174.

SOWA JF (2000) Knowledge Representation: Logical, Philosophical, and Computational Foundations. Brooks/Cole, Pacific Grove, CA.

SPSS (2006) SPSS for Windows. SPSS Inc. Chicago, USA.

STEVENS JP (2002) Applied Multivariate Statistics for the Social Sciences. Lawrence Erlbaum, Mahwah, USA.

TAHVILDAR L and KONTOGIANNIS K (2004) Improving design quality using meta-pattern transformations: a metric-based approach. Journal of Software Maintenance and Evolution: Research and Practice 16(4–5), 331–361.

TVEDT JD and COLLOFELLO JS (1995) Evaluating the effectiveness of process improvements on software development cycle time via system dynamics modelling. In International Computer Software and Applications Conference (COMPSAC), (BENJAMIN WW, Ed.), pp 318–325, IEEE, Dallas, TX.

UMAPATHY K and PURAO S (2006) Designing enterprise solutions with web services and integration patterns. In IEEE International Conference on Services Computing (SCC), pp 111–118 IEEE Computer Society.

UMAPATHY K and PURAO S (2007) Exploring alternatives for representing and accessing design knowledge about enterprise integration. In International Conference on Conceptual Modeling (ER), Auckland, New Zealand.

UMAPATHY K and PURAO S (2008) Representing and accessing design knowledge for service integration. In IEEE International Conference on Services Computing, pp 67–74, IEEE Computer Society, Honolulu, HI.

UML (2005) Unified modeling language. Object Management Group (OMG). http://www.uml.org/.

VOKA<sup>´</sup> <sup>ˇ</sup>C M, TICHY W, SJøBERG DIK, ARISHOLM E and ALDRIN M (2004) A controlled experiment comparing the maintainability of programs designed with and without design patterns – a replication in a real programming environment. Empirical Software Engineering 9(3), 149-195.

WASSERMAN AI (1996) Toward a discipline of software engineering. IEEE Software 13(6), 23–31.

WEBER R (2003) Editor’s comments: still desperately seeking the IT artifact. MIS Quarterly 27(2), iii–xi.

WFMCTERMINOLOGY (1999) Workflow management coalition terminology & glossary. The workflow management coalition specification. http://www.wfmc.org/standards/docs/TC-1011\_term\_glossary\_v3.pdf.

WHITE SA (2004) Introduction to BPMN. IBM. http://www.bpmn.org/ Documents/Introduction%20to%20BPMN.pdf.

WSDL-ADJUNCTS (2007) Web services description language (WSDL) version 2.0 part 2: adjuncts. W3C. http://www.w3.org/TR/wsdl20- adjuncts/.

ZHU J, TIAN Z, LI T, SUN W, YE S, DING W, WANG CC, WU G, WENG L, H S, L B and C D (2004) Model-driven business process integration and management: a case study with the Bank SinoPac regional service platform. IBM Journal of Research and Development 48(5/6), 649–670.
