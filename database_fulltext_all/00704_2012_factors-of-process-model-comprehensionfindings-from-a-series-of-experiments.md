---
otero_id: 704
otero_key: "6X5WKFEC"
title: "Factors of process model comprehension—Findings from a series of experiments"
authors: "Jan Mendling; Mark Strembeck; Jan Recker"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.12.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Factors of process model comprehension—Findings from a series of experiments

Jan Mendling <sup>a,</sup>⁎, Mark Strembeck <sup>a</sup>, Jan Recker <sup>b</sup>

<sup>a</sup> Wirtschaftsuniversität Wien (WU), Augasse 2-6, 1090 Wien, Austria

<sup>b</sup> Queensland University of Technology, 126 Margaret Street, QLD 4000 Brisbane, Australia

## a r t i c l e i n f o

Article history: Received 29 October 2010 Received in revised form 28 November 2011 Accepted 22 December 2011 Available online 14 January 2012

Keywords: Business process modeling Model comprehension Experiment

## a b s t r a c t

In order to make good decisions about the design of information systems, an essential skill is to understand process models of the business domain the system is intended to support. Yet, little knowledge to date has been established about the factors that affect how model users comprehend the content of process models. In this study, we use theories of semiotics and cognitive load to theorize how model and personal factors in-<sup>fl</sup>uence how model viewers comprehend the syntactical information of process models. We then report on a four-part series of experiments, in which we examined these factors. Our results show that additional semantical information impedes syntax comprehension, and that theoretical knowledge eases syntax comprehension. Modeling experience further contributes positively to comprehension ef<sup>fi</sup>ciency, measured as the ratio of correct answers to the time taken to provide answers. We discuss implications for practice and research.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

In recent years, the documentation of business processes and the analysis and design of process-aware information systems has gained attention as a primary focus of modeling in information systems practice [10]. The so-called practice of process modeling has emerged as a key instrument to enable decision making in the context of the analysis and design of process-aware enterprise systems [11], service-oriented architectures [13], work<sup>fl</sup>ow operation [26] and web services [14] alike.

Process models typically capture in some graphical notation the tasks, events, states, and control <sup>fl</sup>ow logic that constitute a business process. Process models may also contain information regarding the data that is processed by the execution of tasks, which organizational and IT resources are involved, and potentially capture other artifacts such as external stakeholders and performance metrics, see e.g. Ref. [49].

Many bene<sup>fi</sup>ts are associated with business process modeling. For instance, practitioners have identi<sup>fi</sup>ed process improvement, communication and shared understanding as the most important process modeling bene<sup>fi</sup>ts [17]. A prerequisite for realizing these bene<sup>fi</sup>ts, however, is that the quality of process models are perceived as good by their audience, making the understandability of process models an important topic for research relevant to all potential uses of process models [2]. Several studies support this view. For instance, the perceived quality of a process model is a key factor contributing to organizational re-design project success [21]. Accordingly, our interest in this paper is to examine how analysts develop an understanding of process models.

More speci<sup>fi</sup>cally, we study (a) factors characterizing the process model in terms of the activity labels used in the models, (b) factors characterizing the person interpreting the models in terms of relevant modeling expertise, and (c) how these factors affect process model comprehension. The relevance of this research stems from companies making signi<sup>fi</sup>cant investments in process modeling training, with the view of developing a body of process modeling expertise. Indeed, modeler expertise has been established by surveys as an important factor for process modeling success [3] and modeling grammar usage [40]. Furthermore, prior experiments demonstrate that model factors (e.g., an increase in model complexity) affect understanding [45,47]. Notably, these experiments use abstract activity labels (A, B, C, etc.) in their process models, which, in turn, raises the question whether the usage of activity labels that carry real domain semantics leverages or impedes understanding.

The aim of the research reported here is to combine these preliminary insights in the de<sup>fi</sup>nition of a series of experiments. Accordingly, the contributions of this paper are threefold. First, we build on the cognitive load theory to conjecture that real activity labels should decrease syntactical process model understanding. This hypothesis is con<sup>fi</sup>rmed in our experiments. Second, we argue in line with prior research that higher modeling expertise results in better understanding performance. This hypothesis is generally con<sup>fi</sup>rmed, too. Third, we de<sup>fi</sup>ne different measures of expertise including theoretical knowledge, prior modeling experience, and intensity of modeling. The experiments show that theoretical knowledge is most signi<sup>fi</sup>cant with its impact on performance. Our <sup>fi</sup>ndings have implications for research on model understanding, in particular regarding cognitive load considerations, and for practice by demonstrating the relevance of theoretical knowledge of process modeling to understanding these models. This insight, in turn, is relevant to informing a staged teaching strategy that educates practitioners about how to read process models.

The rest of this paper is structured as follows. Section 2 introduces the theoretical foundations of process model comprehension. We identify matters of process model understanding and respective challenges. This leads us to factors of understanding. Section 3 describes the research design and Section 4 the results along with a discussion of threats to validity. Section 5 highlights implications for research and practice. Section 6 concludes the article.

## 2. Background

In this section, we discuss the background of our research. Section 2.1 summarizes which formal conclusions can be drawn from a process model and how understanding performance can be measured. Section 2.2 formalizes our hypotheses.

## 2.1. Process model comprehension

Process modeling has emerged as an important practice to guide decisions in systems analysis and design. In fact, process modeling is the number one reason to engage in conceptual modeling altogether [10], and also considered the number one skill demanded from IT graduates.<sup>1</sup> Analysts develop process models to capture relevant information about a business process they seek to re-design, analyze, or support with an appropriate information system. A business process that is in place to deal with a book order may, for example, contain a task to receive the order, which is followed by another one specifying that the book is to be sent to the customer who ordered it. A model of this process would, therefore, include sequences of graphical elements to describe these tasks and the order in which they have to be performed. Process models can be elicited through interviews with relevant stakeholders, or derived from organizational documents such as business policies [54]. Figs. 1 and 2 show two variants of a typical process model, conveying information about important tasks and the control <sup>fl</sup>ow that speci<sup>fi</sup>es the execution of these tasks.

In reaching an understanding about how individuals comprehend the content of process models, we realize that there is a broad spectrum of matters that can be understood from a process model. The SEQUAL model by Lindland et al. [24], for instance, distinguishes syntactic, semantic, and pragmatic dimensions of model quality. Consider Figs. 1 and 2, which show two structurally equivalent process models. The model of Fig. 1 contains activities that are labeled with capital letters. Therefore, this model can only be analyzed from a syntactical point of view. On the other hand, the model of Fig. 2 includes German language activity labels. As these labels point to a speci<sup>fi</sup>c real-world application domain (i.e., they describe which activities in the realworld domain specifically are to be executed), they enable the discussion of the model from a semantic point of view. If now this model is communicated in a particular context, e.g. it is communicated as a normative model, then we can also investigate its pragmatics. In this way, a process model can represent knowledge for action [22].

Semiotic theory postulates that comprehension, and consequently, communication, can be understood as a ladder: syntax (how do I faithfully combine grammatical elements in a process model? [7]) must be clear before semantics can be discussed, and semantics (what do the grammatical elements in a process model mean? [7]) must be clear before pragmatics can be considered. In this regard, it is a primary interest to analyze in how far stakeholders are able to understand process models on a syntactical level. Other interpretations are <sup>fl</sup>awed if syntax is not correctly understood. This is also acknowledged by prior studies that focus on formal and syntactical aspects of process models [44,45].

![](/api/attachments/6X5WKFEC/fulltext/images/bea7be92ab946cfb50561570497c861760ba780c7df967093cbe88171c0f78b7.jpg)  
Fig. 1. Model 4 with letters.

Looking at which factors in<sup>fl</sup>uence the comprehension of the syntactical content of process models, prior research has discussed several factors of process model understanding including model purpose [45], problem domain [23], modeling notation [1,15,48], visual presentation [34,39,46], and process model complexity [8,27]. Personal factors, on the other hand, have been less intensively researched to date. This is not to say that no research has been conducted. The experiment by Recker and Dreiling, for instance, operationalized the notion of process modeling expertise through a measure of familiarity with a particular modeling notation [41]. In an experiment by Mendling, Reijers, and Cardoso, participants were characterized based on the number of process models they created and the years of modeling experience they had achieved [30]. This study, furthermore, also indicated the speci<sup>fi</sup>c importance of theoretical process modeling knowledge. In the latter experiment the participants from TU Eindhoven with strong Petri net education scored better than other participants with less theoretical education in process modeling.

![](/api/attachments/6X5WKFEC/fulltext/images/d76526639c6df16fdf86aacda79bc997d9dca15aeaf81b06a7525eda3d82c007.jpg)  
Fig. 2. Model 4 with German text.

These studies emphasize the value of looking into more details for the impact of expertise, in a sense of previous experience with modeling, and in a sense of knowledge of fundamental process modeling concepts, which is the intent of our study.

Aside from these important personal factors, we also aim to examine model factors that have not received much attention in prior studies. Speci<sup>fi</sup>cally, we aim to investigate the effect of semantical information on formal syntactical process model understanding. Therefore, we consider model semantics as expressed in the textual labels, which are used to annotate the graphical activity constructs in a process model (see Fig. 2), and which are important to the usefulness of the models [32]. While one may expect that people might be able to better recall a model with textual information due to a broader activation of different concepts [25], there is an opposite effect to be expected when only questions about syntax are asked. The theoretical rationale for this expectation stems from the cognitive load theory [51]. The main assumptions of the cognitive load theory are limited working memory and its interaction with a practically unlimited long-term memory [51]. When individuals study new material (e.g., information about a business process from a process model) they increase their cognitive load, i.e., the burden on their working memory. This is important because working memory has the capacity to process approximately seven items of information at any given time [33]. Clearly, a long text label in comparison to a single letter implies a higher cognitive load. Textual labels might accordingly distract persons from drawing correct conclusions about formal and syntactical aspects of a process model because a larger share of the working memory is required to process the textual information and the domain information they represent. In this way, a variation of activity labels is an interesting treatment as it should be more detrimental to inexperienced model readers due to the implied cognitive load [52].

On the basis of these theoretical arguments, we de<sup>fi</sup>ne the following research objective: analyze business process models for the purpose of understanding with respect to their syntactical and semantic content from the point of view of model readers in the context of varying prior experience with modeling. Now we formalize our expectations in a set of testable hypotheses.

## 2.2. Hypotheses

In theorizing anticipated effects of the factors discussed above on process model understanding, we <sup>fi</sup>rst de<sup>fi</sup>ne our operationalization of process model understanding. Similar to [38], we investigate syntactic understanding from two angles, these being comprehension task performance (how faithfully does the interpretation of the process model allow the reader to comprehend the formal content of the model?) and comprehension task efficiency (what resources are used by the reader to comprehend the process model?). Both factors are important elements in Norman's theory of action [36], and relate to what Norman calls “the gulf of interpretation” (a difference between what the model tries to convey and what is interpreted by the model reader). The gulf of interpretation is an important measure of the performance of modeling efforts, because model comprehension by relevant stakeholders is a necessary prerequisite for various model application tasks, such as systems analysis, communication, design, organizational re-engineering, project management, end user querying and others [43]. In other words, for a model to be useful for any modeling-related task, it is imperative that the stakeholders doing these tasks are able to comprehend the model well (performance) and timely (ef<sup>fi</sup>ciency).

We now draw hypotheses regarding the effects of personal and model factors on model readers’ comprehension task performance and ef<sup>fi</sup>ciency. Fig. 3 shows our research model. The model proposes that process model understanding (in terms of comprehension accuracy and comprehension ef<sup>fi</sup>ciency) is a function of the characteristics of the model of the process, and of the characteristics of the user interpreting the model.

Our <sup>fi</sup>rst hypothesis addresses model factors. While prior studies have examined model characteristics such as model structure and complexity [31], our interest is in the textual labels that are used in process models to annotate the graphical constructs. Graphical constructs, and their relationships, are used to convey information about the structure of a process and its formal behavior. Textual labels used to annotate the graphical constructs, on the other hand, convey important information about the domain (e.g., what activity has to be performed, what is an important document, who within an organization is responsible for execution, and so forth). Based on this distinction, we expect that model readers will be able to more easily understand the formal, syntactical aspects of a process model, as expressed in the grammatical constructs and their relationships, when they are not presented with additional, semantic information about the application domain (in the textual labels). This is because the textual labels increase the cognitive burden on the model viewer in that the textual labels are an additional set of information material that needs to be processed by the working memory [52], but which is largely irrelevant to the comprehension of the formal content of a process model, which is the interest in our study.

![](/api/attachments/6X5WKFEC/fulltext/images/98d9464ddbaa00a3a4952a3228a54fda014040feb7a78759ea61e35108eb8181.jpg)  
Fig. 3. Research model.

We further expect that comprehension occurs quicker for people working with process models featuring abstract textual labels, because they require less effort to retrieve and assemble pieces of information in their working memory, when only having to consider graphical constructs but not additional textual information. We formalize these observations in the <sup>fi</sup>rst two hypotheses:

H<sup>1</sup>. The use of abstract labels will have no impact on comprehension task performance.

H<sup>1</sup>. The use of abstract labels will have a signi<sup>fi</sup>cant positive impact on comprehension task performance.

H<sup>2</sup>. The use of abstract labels will have no impact on comprehension task ef<sup>fi</sup>ciency.

H<sup>2</sup>. The use of abstract labels will have a signi<sup>fi</sup>cant positive impact on comprehension task ef<sup>fi</sup>ciency.

Next, we consider personal factors. First, we theorize that individuals with higher levels of knowledge about formal process model concepts such as deadlocks, soundness, concurrency and so forth will achieve better comprehension task performance and ef<sup>fi</sup>ciency. This is because, when interpreting a process model, these individuals can make use of prior knowledge, i.e., relevant knowledge material stored in long-term memory can be applied to reduce the cognitive load on their working memory, which will ease, and improve their understanding of the material (the process model) presented to them. Accordingly, we have:

H<sup>3</sup>. Users with higher levels of process knowledge will not have higher comprehension task performance.

H<sub>a</sub><sup>3</sup>. Users with higher levels of process knowledge will have signi<sup>fi</sup>- cantly higher comprehension task performance.

H<sup>4</sup>. Users with higher levels of process knowledge will not have higher comprehension task ef<sup>fi</sup>ciency.

H<sub>a</sub><sup>4</sup>. Users with higher levels of process knowledge will have signi<sup>fi</sup>- cantly better comprehension task ef<sup>fi</sup>ciency.

Second, we realize that modeling expertise is an important factor in process modeling [3,40]. Experienced modelers often possess a repertoire of workarounds for challenging modeling situations, and can often refer to their previous experiences and knowledge about modeling when attempting to interpret complex models. Less experienced modelers, on the other hand, often lack such knowledge, which, in turn, can be expected to affect their comprehension accuracy and ef<sup>fi</sup>ciency.

The resource allocation theory [19] suggests that when users build up experience in modeling, their demand for cognitive attentional effort required to perform the model-related tasks is reduced, thereby freeing cognitive resources that can be allocated to improving task performance and outcome production (i.e., better and faster understanding). This situation would suggest that experienced modelers can read process models better and with less effort. We distinguish between modelers that have modeled for a long time (i.e., that have modeling experience) and those that model often (i.e., that have modeling intensity), to be able to examine modeling experience in a more detailed manner. We state the following hypotheses:

$\mathbf { \Delta } H _ { 0 } ^ { 5 } .$ Users with higher levels of modeling experience will have equal comprehension task performance.

$\mathbf { \delta } _ { H _ { a } ^ { 5 } } ^ { 5 } .$ Users with higher levels of modeling experience will have signi<sup>fi</sup>- cantly higher comprehension task performance.

$\mathbf { { \cal H } _ { 0 } ^ { 6 } } .$ Users with higher levels of modeling experience will have equal comprehension task ef<sup>fi</sup>ciency.

$H _ { a } ^ { 6 } .$ Users with higher levels of modeling experience will have signi<sup>fi</sup>- cantly better comprehension task ef<sup>fi</sup>ciency.

$\mathbf { { \cal H } _ { 0 } ^ { 7 } } .$ Users with higher levels of modeling intensity will have equal comprehension task performance.

$H _ { a } ^ { 7 } .$ Users with higher levels of modeling intensity will have signi<sup>fi</sup>- cantly higher comprehension task performance.

$\mathbf { \delta H _ { 0 } ^ { 8 } } .$ Users with higher levels of modeling intensity will have signi<sup>fi</sup>- cantly better comprehension task ef<sup>fi</sup>ciency.

$H _ { a \cdot } ^ { 8 }$ Users with higher levels of modeling intensity will have signi<sup>fi</sup>- cantly better comprehension task ef<sup>fi</sup>ciency.

In the following, we describe design and results of a series of experiments we conducted to test these hypotheses.

## 3. Experiment description

For investigating the hypotheses, we de<sup>fi</sup>ne an experiment following established guidelines for experimental software engineering [4,18,55]. Because there is only limited research on cognitive load effects in the process modeling domain, we chose an experimental method as it affords a higher internal validity than other methods [9]. With this experiment de<sup>fi</sup>nition, we aim to analyze process models for the purpose of understanding with respect to comprehension task performance and comprehension task ef<sup>fi</sup>ciency. In particular, the analyses are conducted from the perspective of a reader of the model, and the experiment's context is given through persons with process modeling skills answering questions about the meaning of a process model.

## 3.1. Experiment design

To test our hypotheses, we selected $1 2 \times ( 4 { \times } 4 { \times } 4 )$ mixed balanced experimental design that allowed us to focus on personal factors and model characteristics while eliminating potentially confounding other variables (e.g., domain knowledge). Our experimental design featured one between-subjects factor and three within-subjects factors.

## 3.1.1. Experimental condition and tasks

The between-subjects factor, Label Type, had two levels. We provided participants with process models that contained either abstract or concrete labels. To operationalize this factor, we gathered a set of six process models from practice that capture business processes in two different domains, order processing and price calculation. The models were provided by a partner organization, which has these models in real use for process documentation purposes. The models were randomly selected from their collection of process models. The models could all be displayed on an A4 page and ranged from nine to twenty activities, and contained between six and <sup>fi</sup>fteen connectors. These characteristics are similar to those found in process model collections in practice [37]. Therefore, we deemed these models to be adequate experimental treatments given that the cases re<sup>fl</sup>ect modeling scenarios typically encountered in real-life process modeling practice. Based on the observation in Ref. [48] that EPCs appear to be easier to understand than Petri nets, we chose an EPClike notation without events. The participants received a short informal description of the semantics similar to ([29], p. 25). Finally, we drew all models in the same top-to-bottom style with the start element at the top and end element at the bottom. Altogether, each participant was challenged with four tasks (see Appendix A):

(1) self-assess process modeling intensity,

(2) self-assess process modeling experience,

(3) answer theoretical knowledge test, and

(4) answer process model comprehension questions.

## 3.1.2. Independent variables

To operationalize the between-subjects factor Label Type as an independent variable, for each of the process models used we constructed a variant where the activity labels were replaced by abstract capital letters as identi<sup>fi</sup>ers. Figs. 1 and 2 depict model number 4 of the models we used in our experiment. For the 6 models we identi<sup>fi</sup>ed 6 yes/no questions related to the structure and the process <sup>fl</sup>ow speci<sup>fi</sup>ed by the model. These questions together with questions on personal experience and knowledge of process modeling were packed into two variants of the questionnaire, one for models with original activity labels (textual labels), one for models with letters (abstract labels).

Aside from the between-subjects factor Label Type, we also de-<sup>fi</sup>ned three within-subject factors. The <sup>fi</sup>rst within-subjects factor Knowledge had four levels. The participants had to answer twelve theoretical yes/no questions before seeing the models about selected topics related to process modeling such as choices, concurrency, loops, and deadlocks (see Appendix A). These questions concern grammatical rules of process model logic, derived from fundamental work in this area [20] and as previously used in Ref. [28]. We transformed the knowledge score into an ordinal knowledge scale with four levels: very low (0–3 correct answers), somewhat low (4–6 correct answers), somewhat high (7–9 correct answers) and very high (10–12 correct answers). This ordinal measure served as a second independent variable. The second within-subjects factor Experience had four levels. The participants were asked for how long they have been involved with business process modeling. The variable was measured on an ordinal scale with four levels: less than one month, less than a year, less than three years, and longer than three years. This measure served as a third independent variable. Finally, the third within-subjects factor Intensity also had four levels. The participants had to indicate how often they work with process models. We used an ordinal scale with four options to answer: daily, monthly, less frequent than monthly, never. This measure served as a fourth independent variable.

## 3.1.3. Dependent variables

We use two dependent variables, comprehension task performance and comprehension task ef<sup>fi</sup>ciency. Comprehension Task Performance is calculated based on the answers given by the participant to the model comprehension questions. It captures the number of correct answers by the person. The maximum value is 36 for six questions on six models. This measure serves as an operationalization of formal process model understanding of a person.

Comprehension Task Efficiency is based on the task completion time that the participants invested in answering the different questions in the questionnaire. The measure is calculated by dividing the number of correct answers (Comprehension Task Performance) by the time it takes to complete the respective questions, and served as a second dependent variable in our study.

## 3.2. Experiment execution

We implemented the experiment in two ways. First, we de<sup>fi</sup>ned an online experiment in order to make access to practitioners with

Table 2

modeling experience more easy. The automated system further allowed us to record the answer times, randomly assign the subject to a label type, and randomly de<sup>fi</sup>ne the presentation order of the six models in the corresponding label type, thereby ensuring a balanced treatment. Participation was voluntary. As an incentive the participants received feedback about their test performance.

In 2007, we distributed the link to the experiment via the German mailing lists EMISA and WI as well as among students that followed courses on process modeling at the Vienna University of Economics and Business. Typically, both academics and practitioners with an interest in conceptual modeling and information systems development are registered with these lists. The questionnaire was started by 200 persons and completed by 46. From these 46 we excluded 4 people who spent less than 10 minutes time on the questionnaire since we assumed that to be the minimum time to provide meaningful answers. The remaining 42 persons and their answers to the 36 questions establish the <sup>fi</sup>rst part of the sample for our statistical analysis below. Altogether, 1512 answers are recorded in the sample. 65% of the participants had more than three years experience in process modeling.

To increase con<sup>fi</sup>dence in the conclusion validity of our study, we collected further data with paper-based replications of the experiment. The <sup>fi</sup>rst replication in April 2009 involved 23 graduate students from Vienna University of Economics and Business who followed a course on modeling. The second sample includes 22 graduate students who followed the same course in June 2009.<sup>2</sup> The third replication was conducted with 32 graduate students who followed the system analysis and design course at Humboldt-Universität zu Berlin. From all four experiments we collected data from altogether 119 persons. With each answering 36 questions, we get 4284 answers to model understanding questions.

These four experiments correspond to a strict replication according to Ref. [4], with the variation between the experiments being only in the institution of the participants and the mode of presentation (web versus paper). Because neither institutional af<sup>fi</sup>liation nor mode of presentation is a relevant factor in our study, our replication can be considered strict and therefore allows not only combination of experimental results but also pooling of data. To be able to examine any potential threats to validity stemming from the replication, we created two dummy variables, affiliation, and experimentMode, to examine whether experimental results differed signi<sup>fi</sup>cantly across the replications. Table 1 gives the results. All test results were insigni<sup>fi</sup>- cant, with p values ranging from 0.17 to 0.41, suggesting that none of the relevant data differed signi<sup>fi</sup>cantly for the dummy variables, thereby justifying to our pooling of the data.

Each of the experiments used feedback about the performance as an inducement. While this feedback was meant to be informative to practitioners, it served the students for the preparation towards their exams.

## 4. Data analysis and interpretation

In this section, we <sup>fi</sup>rst discuss distribution and correlation before we turn to hypothesis testing. Last, we discuss threats to validity.

## 4.1. Distribution and correlation analysis

Table 2 shows descriptive statistics for our measures. All results are in line with expectations. Table 3 gives the correlation matrix. First, we check for potential interactions between our betweensubject factor (label type) and our within-subject factors (experience, intensity, knowledge). The data in Table 3 clearly shows that no signi<sup>fi</sup>cant interaction terms are present between these factors, thereby suggesting independence of the experimental conditions used in our study. The insigni<sup>fi</sup>cant correlations of the between-subjects factor and the within-subject factors allow to run the hypothesis tests independently. Further inspection of Table 3 suggests that Label type and formal process knowledge (knowledge) are meaningful independent factors as they correlate signi<sup>fi</sup>cantly with the dependent measures. By contrast, experience and intensity do not correlate largely with the dependent measures but with each other. This correlation between intensity and experience, however, behaves in accordance with general expectations (in the sense that people that model longer often model more frequently, too). Next, the correlation between intensity and experience to knowledge is expected, as people with more intensive or overall longer process modeling experiences build up higher levels of knowledge about process modeling. The correlations between comprehension score and efficiency, likewise, were expected. Overall, we do not <sup>fi</sup>nd counter-intuitive correlations in Table 3. Note that in Table 2 we see that the sample size for the ef<sup>fi</sup>- ciency measure is 87, which is because we failed to accurately record task completion times in our experiment replication with the students in Berlin.

Table 1  
Test results regarding experiment replication.

<table><tr><td>Dependent variable</td><td>Dummy variable</td><td>Levels</td><td>N</td><td>Mean</td><td>Std. dev.</td><td>Sig.</td></tr><tr><td rowspan="6">Comprehension Task Performance</td><td rowspan="4">Affiliation</td><td>Original study</td><td>42</td><td>26.26</td><td>4.94</td><td>0.17</td></tr><tr><td>Replication 1</td><td>23</td><td>25.44</td><td>4.02</td><td></td></tr><tr><td>Replication 2</td><td>22</td><td>26.36</td><td>4.28</td><td></td></tr><tr><td>Replication 3</td><td>32</td><td>25.78</td><td>4.90</td><td></td></tr><tr><td rowspan="2">ExperimentMode</td><td>Online</td><td>42</td><td>26.60</td><td>4.49</td><td>0.23</td></tr><tr><td>Paper</td><td>77</td><td>25.58</td><td>4.25</td><td></td></tr><tr><td rowspan="5">Comprehension Task Efficiency</td><td rowspan="3">Affiliation</td><td>Original study</td><td>42</td><td>1.31</td><td>0.66</td><td>0.27</td></tr><tr><td>Replication 1</td><td>23</td><td>1.22</td><td>0.29</td><td></td></tr><tr><td>Replication 2</td><td>22</td><td>1.14</td><td>0.25</td><td></td></tr><tr><td rowspan="2">ExperimentMode</td><td>Online</td><td>42</td><td>1.31</td><td>0.66</td><td>0.41</td></tr><tr><td>Paper</td><td>45</td><td>1.18</td><td>0.28</td><td></td></tr></table>

## 4.2. Testing hypotheses on comprehension task performance

After screening the data, we now discuss the test of our predictions. We argued in our Hypotheses H<sub>a</sub><sup>1</sup>, H<sub>a</sub><sup>3</sup>, H<sub>a</sub><sup>5</sup> and H<sub>a</sub><sup>7</sup> that process model comprehension task performance would be positively impacted by

• the use of abstract labels,

• higher levels of formal process knowledge,

• higher levels of process modeling experience, and

• higher levels of process modeling intensity.

As a dependent measure, we used the process model comprehension task performance scores (0–36). We <sup>fi</sup>rst checked whether the data met the assumption of equal variances in the dependent measures across the levels of each independent variable. Levene's test was insigni<sup>fi</sup>cant (F=1.45, p=0.19), indicating that the data met this assumption. Hypothesis testing was completed individually for each of the four independent factors above, using SPSS Version 16.0. First, we performed an Analysis of Variance (ANOVA) for our between-subjects factor Label Type. Then, for each of the three factors formal process knowledge, process modeling experience, and process modeling intensity, we used a non-parametric Kruskal–Wallis test to examine our hypotheses, because a Kolmogorov–Smirnov test con-<sup>fi</sup>rmed that the normality assumption did not hold for these measures, i.e. Z=2.51 (knowledge), 2.68 (experience), 2.52 (intensity), all pb0.01. Therefore, we used the Kruskal–Wallis test, which is accepted as an alternative to ANOVA in case the considered variables are not normally distributed [50]. We examined the hypotheses individually because our correlation analysis suggested independence of the between-subjects and within-subjects factors. Also, our experimental design features three ordinal variables, for which we required nonparametric tests, and the Kruskal–Wallis test we selected considers one independent variable at a time. We chose this test over others (e.g., ANOVA, Mann–Whitney) because, <sup>fi</sup>rst, the Kruskal–Wallis test is the generalization of the Mann–Whitney test when there are more than two independent groups, like in our study (four levels) [16]. Second, even though we replicated the experiment to gather more data, the number of respondents overall is rather small, and the subgroups for each ordinal scale level are smaller. The distribution-free nature of non-parametric tests places few restrictions on the sample size in contrast with parametric tests, which rely on asymptotic properties or normality of the sample distribution [50]. Third, the ordinal measures used in our study called for the use of non-parametric methods, which yield higher power than corresponding parametric tests (e.g., ANOVA) [35]. Finally, rank-based non-parametric tests are not affected by outliers [16], which allows us to also consider those data where respondents took unusually long (or short) for answering the experimental questions. Table 4 gives the descriptive results and Table 5 gives the results from the statistical tests.

Descriptive statistics.

<table><tr><td>Type of variable</td><td>Variable</td><td>N</td><td>Mean</td><td>Std. dev.</td><td>Scale</td></tr><tr><td rowspan="4">Independent variables</td><td>Knowledge</td><td>119</td><td>2.66</td><td>0.84</td><td>1-4</td></tr><tr><td>Label type</td><td>119</td><td>1.47</td><td>0.50</td><td>1/2</td></tr><tr><td>Experience</td><td>119</td><td>2.75</td><td>1.21</td><td>1-4</td></tr><tr><td>Intensity</td><td>119</td><td>2.30</td><td>0.95</td><td>1-4</td></tr><tr><td rowspan="2">Dependent variables</td><td>Comprehension task performance</td><td>119</td><td>25.94</td><td>4.34</td><td>0-36</td></tr><tr><td>Comprehension task efficiency</td><td>87</td><td>1.22</td><td>0.52</td><td>0-inf.</td></tr></table>

Table 3 Correlation matrix.  
Table 4

<table><tr><td></td><td>Label type</td><td>Knowledge</td><td>Intensity</td><td>Experience</td><td>Comprehension task performance</td></tr><tr><td>Knowledge</td><td>-0.01</td><td></td><td></td><td></td><td></td></tr><tr><td>Intensity</td><td>0.08</td><td>0.31**</td><td></td><td></td><td></td></tr><tr><td>Experience</td><td>0.04</td><td>0.28**</td><td>0.24*</td><td></td><td></td></tr><tr><td>Comprehension Task performance</td><td>-0.08</td><td>0.42**</td><td>0.15</td><td>0.15</td><td></td></tr><tr><td>Comprehension Task efficiency</td><td>-0.35**</td><td>0.16</td><td>0.13</td><td>-0.11</td><td>-0.31**</td></tr></table>

米 Correlation is signi<sup>fi</sup>cant at the 0.05 level (2-tailed).  
\*\* Correlation is signi<sup>fi</sup>cant at the 0.01 level (2-tailed).

Perusal of the data in Tables 4 and 5 leads to the following observations.

$H _ { a } ^ { 1 }$ hypothesized higher comprehension task performance scores for the group of users working with models with abstract labels. Table 4 shows that the average comprehension task performance scores indeed were higher (mean score=26.45 vs. 25.48), and Table 5 con<sup>fi</sup>rms that the differences are signi<sup>fi</sup>cant $( F = 5 . 0 5 ,$ $\mathsf { p } { = } 0 . 0 3 )$ . These results lead to the rejection of null hypothesis H<sup>1</sup> and suggest people viewing models with no textual labels achieve a higher level of comprehension of formal syntactic aspects of process models.

$H _ { a } ^ { 3 }$ hypothesized higher comprehension task performance scores for users with higher levels of formal process knowledge. And indeed, we observe that comprehension task performance scores were higher, relatively, for users with very high knowledge levels, over those with somewhat high, and somewhat low knowledge (means=29.47, 26.57 and 23.80).<sup>3</sup> Table 5 suggests that the comprehension task performance across the four groups is signi<sup>fi</sup>cantly different $( C h i - 2 = 2 4 . 4 8 , \mathsf { p } = 0 . 0 0 )$ . We note, interestingly, that the group of users with very low knowledge performed somewhat better than the group with somewhat low knowledge (mean=24.78). A follow-up ANOVA analysis of these two groups, however, showed these differences to be insigni<sup>fi</sup>cant. A second-follow up ANOVA analysis of comprehension task performance based on the actual comprehension task performance scores (0–12) also yielded signi<sup>fi</sup>cant results $( d f = 1 1 , F = 2 . 0 5 , \mathtt { p } = 0 . 0 3 )$ ). Therefore, we suggest to reject the null hypothesis and tentatively accept hypothesis H<sup>3</sup>.

Descriptive results of model comprehension task performance scores.

<table><tr><td>Differences among groups</td><td>Treatment group</td><td>N</td><td>Mean</td><td>Std. dev.</td><td>Mean rank</td></tr><tr><td rowspan="2">Label type</td><td>Abstract labels</td><td>62</td><td>26.35</td><td>4.06</td><td>N/A</td></tr><tr><td>Textual labels</td><td>56</td><td>25.48</td><td>4.67</td><td>N/A</td></tr><tr><td rowspan="4">Knowledge</td><td>Very low</td><td>9</td><td>24.78</td><td>2.44</td><td>43.78</td></tr><tr><td>Somewhat low</td><td>41</td><td>23.80</td><td>4.66</td><td>45.42</td></tr><tr><td>Somewhat high</td><td>49</td><td>26.57</td><td>3.77</td><td>63.93</td></tr><tr><td>Very high</td><td>19</td><td>29.47</td><td>3.10</td><td>89.79</td></tr><tr><td rowspan="4">Experience</td><td>Less than one month</td><td>28</td><td>24.39</td><td>4.65</td><td>48.58</td></tr><tr><td>Less than a year</td><td>20</td><td>26.25</td><td>4.27</td><td>58.54</td></tr><tr><td>Less than three years</td><td>23</td><td>26.78</td><td>3.87</td><td>71.22</td></tr><tr><td>Longer than three years</td><td>47</td><td>26.32</td><td>4.36</td><td>60.33</td></tr><tr><td rowspan="4">Intensity</td><td>Never</td><td>26</td><td>24.81</td><td>3.38</td><td>46.09</td></tr><tr><td>Less than monthly</td><td>45</td><td>25.56</td><td>4.47</td><td>62.85</td></tr><tr><td>Monthly</td><td>32</td><td>27.56</td><td>4.23</td><td>63.67</td></tr><tr><td>Daily</td><td>15</td><td>25.60</td><td>5.24</td><td>64.02</td></tr></table>

H<sup>5</sup> and H<sup>7</sup> hypothesized higher comprehension task performance scores for users with higher levels of modeling expertise (in the sense of modeling experience and intensity). Table 4 shows that the comprehension task performance scores for the four groups of users (for both experience and intensity) follow an inverse U-shaped curve in that task scores increase for the users with very low, somewhat low, and somewhat high expertise (both for experience and intensity) but drop for the groups of users classi<sup>fi</sup>ed as very experienced/very intensive. The results from the Kruskal–Wallis test in Table 5 show, furthermore, that group differences for both factors experience and intensity are insigni<sup>fi</sup>cant (Chi−2=6.37, p=0.10 and Chi−2=5.70, p=0.13). In light of these results, we cannot reject the null hypotheses H<sup>5</sup> and $H _ { 0 } ^ { 7 } ,$ , suggesting that modeling expertise is not an important factor in explaining process model comprehension task performance.

## 4.3. Testing hypotheses on comprehension task efficiency

Next, we argued in our Hypotheses H<sup>2</sup>, H<sup>4</sup>, H<sup>6</sup> and $H _ { a } ^ { 8 }$ that process model comprehension task ef<sup>fi</sup>ciency (measured by the normalized ratio between comprehension task performance and comprehension task completion times) would be positively impacted by

• the use of abstract labels,

• higher levels of formal process knowledge,

• higher levels of process modeling experience, and

• higher levels of process modeling intensity.

Because during our conduct of the experiment at Humboldt-Universität zu Berlin we were unable to accurately record time measures for comprehension tasks, for this second analysis we had to exclude 32 entries from our data set, resulting in an effective sample size of 87. Again, we <sup>fi</sup>rst checked whether the data met the assumption of equal variances in the dependent measures across groups. Levene's test was insigni<sup>fi</sup>cant $( F = 1 . 3 0 , ~ \mathfrak { p } = 0 . 0 8 )$ , indicating that the data met this assumption. Hypothesis testing was completed in the same manner as above, using the same four measures as independent factors. As a dependent measure, we used the process model comprehension task ef<sup>fi</sup>ciency scores. The descriptive analysis results are displayed in Table 6 and Table 7.

Test results of model comprehension task performance scores.

<table><tr><td>Independent factor</td><td>df</td><td>Statistic</td><td>Sig.</td></tr><tr><td>Label type</td><td>1</td><td>5.05</td><td>0.03</td></tr><tr><td>Theory</td><td>3</td><td>24.48</td><td>0.00</td></tr><tr><td>Experience</td><td>3</td><td>6.37</td><td>0.10</td></tr><tr><td>Intensity</td><td>3</td><td>5.70</td><td>0.13</td></tr></table>

Perusal of the data in Tables 6 and 7 leads to the following observations.

H<sup>2</sup> hypothesized better comprehension task ef<sup>fi</sup>ciency scores for the group of users working with models with abstract labels. Table 6 shows that the average comprehension task ef<sup>fi</sup>ciency score, i.e., the ratio between correct answers and time taken to complete the answers, indeed were lower for this group (mean score=1.39 vs. 1.03). Table 7 shows that the group differences are signi<sup>fi</sup>cant $( F = 3 . 9 0 , p = 0 . 0 5 )$ . Therefore, the results suggest rejecting null hypothesis $H _ { 0 } ^ { 2 } ,$ which means that textual semantics, being a signi<sup>fi</sup>cant factor for how well people understand the formal content of process models, also signi<sup>fi</sup>cantly affects the effort that is required to reach this understanding.

H<sup>4</sup> hypothesized better comprehension task ef<sup>fi</sup>ciency scores for the group of users working with higher levels of formal process knowledge. We note from Table 7 that the differences in comprehension task ef<sup>fi</sup>ciency across the groups of users with different levels of knowledge are signi<sup>fi</sup>cant $( C h i - 2 = 8 . 3 8 , p = 0 . 0 4 )$ , and from Table 6 that the ef<sup>fi</sup>ciency scores are better for users with higher levels of knowledge. We note, however, that Table 6 also shows a somewhat unexpected exception. The group of users with low levels of knowledge completed their tasks the with the second-best ef<sup>fi</sup>ciency score (mean=1.34), superseded only by those with high levels of knowledge (mean=1.51). We note that these results may have been over-compensated through quick task completion, independent from correct results (as shown in Table 4). Indeed, it seems plausible that users with low knowledge levels just quickly selected answers without engaging in a thorough consideration of the content presented to them. Overall, the results are in line with our expectations, the null hypothesis H<sup>4</sup> is rejected.

$H _ { a } ^ { 6 }$ and $H _ { a } ^ { 8 }$ hypothesized better comprehension task ef<sup>fi</sup>ciency scores for users with higher levels of modeling expertise (in the sense of modeling experience and intensity). We note from Table 7 that the differences in task completion ef<sup>fi</sup>ciency across the user groups with different levels of modeling intensity are signi<sup>fi</sup>cant $( C h i - 2 = 9 . 0 9 , ~ p = 0 . 0 3 )$ , and provide the correct directionality (means=1.09, 1.19, 1.28 and 1.30). The results support hypothesis H8a. For modeling experience, however, the results are not in line with hypothesis H6a. There are <sup>fl</sup>uctuations in comprehension task ef<sup>fi</sup>ciency scores noted in Table 6 (means=1.36, 1.29, 1.01 and 1.21), and the Kruskal–Wallis tests suggests that the differences across the groups are insigni<sup>fi</sup>cant $( C h i - 2 = 4 . 2 9 , p = 0 . 2 3 )$ . Therefore, we cannot reject null hypothesis H<sup>6</sup>.

Descriptive results of model comprehension task ef<sup>fi</sup>ciency scores.

<table><tr><td>Differences among groups</td><td>Treatment group</td><td>N</td><td>Mean</td><td>Std. dev.</td><td>Mean rank</td></tr><tr><td rowspan="2">Label type</td><td>Abstract labels</td><td>44</td><td>1.39</td><td>0.60</td><td>N/A</td></tr><tr><td>Textual labels</td><td>42</td><td>1.03</td><td>0.32</td><td>N/A</td></tr><tr><td rowspan="4">Formal knowledge</td><td>Very low</td><td>9</td><td>1.34</td><td>0.39</td><td>54.50</td></tr><tr><td>Somewhat low</td><td>33</td><td>1.08</td><td>0.40</td><td>48.92</td></tr><tr><td>Somewhat high</td><td>33</td><td>1.24</td><td>0.42</td><td>65.98</td></tr><tr><td>Very high</td><td>11</td><td>1.51</td><td>0.85</td><td>71.68</td></tr><tr><td rowspan="4">Modeling experience</td><td>Less than one month</td><td>16</td><td>1.36</td><td>0.49</td><td>69.81</td></tr><tr><td>Less than a year</td><td>13</td><td>1.29</td><td>0.64</td><td>53.10</td></tr><tr><td>Less than three years</td><td>16</td><td>1.01</td><td>0.60</td><td>62.83</td></tr><tr><td>Longer than three years</td><td>41</td><td>1.21</td><td>0.44</td><td>58.13</td></tr><tr><td rowspan="4">Modeling intensity</td><td>Never</td><td>14</td><td>1.09</td><td>0.30</td><td>74.41</td></tr><tr><td>Less than monthly</td><td>37</td><td>1.19</td><td>0.58</td><td>64.22</td></tr><tr><td>Monthly</td><td>23</td><td>1.28</td><td>0.49</td><td>52.74</td></tr><tr><td>Daily</td><td>12</td><td>1.30</td><td>0.58</td><td>51.91</td></tr></table>

Table 7  
Test results of model comprehension task ef<sup>fi</sup>ciency scores.

<table><tr><td>Independent factor</td><td>df</td><td>Statistic</td><td>Sig.</td></tr><tr><td>Type</td><td>1</td><td>3.90</td><td>0.05</td></tr><tr><td>Theory</td><td>3</td><td>8.38</td><td>0.04</td></tr><tr><td>Experience</td><td>3</td><td>4.29</td><td>0.23</td></tr><tr><td>Intensity</td><td>3</td><td>9.09</td><td>0.03</td></tr></table>

## 4.4. Discussion of results

Our experimental study provides support for <sup>fi</sup>ve out of eight hypothesized factors of process model comprehension task performance and ef<sup>fi</sup>ciency (see Table 8). The results for hypotheses $H _ { a } ^ { 1 }$ and $H _ { a } ^ { 2 }$ suggest that a plus in semantical information in terms of text labels seems to be a burden when analyzing the syntactical content of a process. These <sup>fi</sup>ndings are in line with arguments that are founded on the grounds of cognitive load theory as well as the premise of the semiotic ladder. Hypotheses $H _ { a } ^ { 3 }$ to $H _ { a } ^ { 8 }$ are interesting to be discussed relative to each other. Theoretical knowledge turned out to be a strong indicator for both comprehension task performance and ef<sup>fi</sup>ciency on syntaxrelated comprehension of process models $( H _ { a } ^ { 3 }$ and $H _ { a } ^ { 4 } )$ . In contrast, modeling experience and intensity were found not to contribute significantly to either comprehension task performance or ef<sup>fi</sup>ciency, set aside the result obtained in relation to hypothesis H<sup>8</sup>. We interpret this result as an indication that theoretical knowledge is of paramount importance to understanding syntactical aspects of a process model, over and above any practical experience with the exercise of process modeling. Indeed, the non-signi<sup>fi</sup>cance of experience and intensity here might suggest that these factors are more important for the semantical interpretation of process models and that theory is the prerequisite for understanding syntax.

## 4.5. Threats to validity

The results of this experiment have to be discussed against different threats to validity. We focus on those threats of ([55], p. 67) that are most relevant for our experiment.

Conclusion validity is concerned with the relationship between treatment and outcome, and the conclusions drawn from it. Two aspects have to be considered: The <sup>fi</sup>rst aspect concerns the appropriateness of the statistical tests. As reported above, we have screened our data for conformance with the assumptions of the statistical tests we used (ANOVA, Kruskal–Wallis test). We used Levene's test to show that the dependent variables across the treatment groups shared approximately equal variance. We used the non-parametric Kruskal–Wallis test for our ordinal measures because the independent data was not normally distributed. A Kolmogorov–Smirnov test con<sup>fi</sup>rmed that the normality assumption did not hold for the measures knowledge, experience, or intensity (Z=2.51, 2.68, 2.52, all p=0.00). Therefore, we used the Kruskal–Wallis test, which is accepted as an alternative to ANOVA in case the considered variables are not normally distributed [50]. The second aspect concerns the effect sizes of the results. In order to reach a sample size suf<sup>fi</sup>cient to solve potential issues regarding the statistical signi<sup>fi</sup>cance, we conducted strict replications [4] of our experiment. In order to show that our replications did not induce bias into our analysis, we created two dummy variables, affiliation and experimentMode, to examine whether experimental results differed signi<sup>fi</sup>cantly across the replications. Af<sup>fi</sup>liation with one of the universities partaking in our study did not affect results for comprehension task performance or task completion time—the Kruskal–Wallis test was insigni<sup>fi</sup>cant $( \mathfrak { p } = 0 . 1 6$ and p=0.09). The mode of experiment (paper versus online), likewise, was an insigni<sup>fi</sup>cant factor, as shown in an independent samples t-test $( \mathfrak { p } = 0 . 2 0$ and $\mathsf { p } { = } 0 . 8 0$ for comprehension task performance and task completion time).

Summary of hypotheses tests.

<table><tr><td>Hypothesis</td><td>Result</td></tr><tr><td> $H_{a}^{1}$ : Label type → Comprehension task performance</td><td>Supported</td></tr><tr><td> $H_{a}^{2}$ : Label type → Comprehension task efficiency</td><td>Supported</td></tr><tr><td> $H_{a}^{3}$ : Knowledge → Comprehension task performance</td><td>Supported</td></tr><tr><td> $H_{a}^{4}$ : Knowledge → Comprehension task efficiency</td><td>Supported</td></tr><tr><td> $H_{a}^{5}$ : Experience → Comprehension task performance</td><td>Not supported</td></tr><tr><td> $H_{a}^{6}$ : Experience → Comprehension task efficiency</td><td>Not supported</td></tr><tr><td> $H_{a}^{7}$ : Intensity → Comprehension task performance</td><td>Not supported</td></tr><tr><td> $H_{a}^{8}$ : Intensity → Comprehension task efficiency</td><td>Supported</td></tr></table>

Internal validity demands that the treatment causes the effect. In order to avoid maturation and learning effects, we used a random sampling of the questions. Other threats relate to resentful demoralization and mortality. In general, we can assume that those who perform better would be less likely to interrupt or stop answering the questionnaire. This is presumably not a problem when this dropout is equally relevant for both treatments. As we observe in the results, it appears to require a higher cognitive load to inspect the models with text labels. Participants receiving this treatment might be more likely to give up due to higher mental effort. While we did not have drop outs in the student replications, we noticed some instances in which online participants failed to answer all questions. For the online participants (N=42), cases for the comprehension questions ranged from 0 missing answers to a maximum of 8 missing answers (out of 36 questions), with the mean being 1.69. We then performed a linear regression analysis to examine whether the number of missing answers has a signi<sup>fi</sup>cant effect on the number of correct answers. The regression model showed that number of missing answers was an insigni<sup>fi</sup>cant predictor $( \mathrm { t } = - 1 . 6 4 , \ \mathsf { p } = 0 . 1 1 )$ ), thereby alleviating concerns about internal validity of our results.

Construct validity can be related to potential interactions between the measures. To that end, <sup>fi</sup>rst, we inspected the measure correlations as reported above. We did not <sup>fi</sup>nd any unexpected correlations, but only those that establish con<sup>fi</sup>dence in the convergent validity of our comprehension measures (task performance and task ef<sup>fi</sup>ciency: $\mathrm { r } = - 0 . 3 1 , \mathrm { p } { < } 0 . 0 1 )$ and expertise measures (experience and intensity: r=0.24, pb0.05), and the discriminant validity of our model and personal factors (e.g., label type and knowledge: $\Gamma = - 0 . 0 1 , \mathfrak { p } { > } 0 . 0 5 )$

As reported above, we also cared to eliminate potential bias stemming from non-equivalency between the treatment groups, by conducting manipulation checks to assess differences between the groups of participants across treatments. We noted above that there were no signi<sup>fi</sup>cant differences in the independent and dependent variables used, based on independent samples t-tests using the experimental medium used (paper versus online), student cohort (two from Vienna University of Economics and Business versus one from Humboldt-Universität zu Berlin), or time of experiment (2007, April 2009, June 2009). These results indicate that the participants were effectively randomized across treatments. We can also assume that there was no hypothesis guessing by the participants as we did not even reveal that two different treatments were used. The students participated as a preparation for the exam while the practitioners expected to receive feedback on their performance.

External validity is concerned with how generalizable the results are to the wider population of process modelers. Our set of replications was particularly motivated by external validity considerations, since we aim to generalize to the population of professionals involved in process modeling initiatives. Our manipulation checks con<sup>fi</sup>rmed that our replications can be considered strict, thereby increasing the external validity of our <sup>fi</sup>ndings. One particular aspect of the external validity of the presented research relates to the extent to which the used models are representative for real-world models. As explained, we countered this threat by our choice of real process models from a partnering organization. A third important aspect that refers to a potentially limited external validity, relates to the involvement of students. We note that some of the students possessed prior practical experience with process modeling. Also, prior research found that students tend to have higher theoretical knowledge [45]. While we explicitly built both these factors into our research model, this could be seen as a limitation of this research, as the population in our study is potentially more knowledgeable of formal aspects of process modeling theory than the wider population. And indeed, our results con<sup>fi</sup>rm that theoretical knowledge is a key factor in explaining process model comprehension. One may argue, however, that process modeling students will form the next generation of junior analysts, and therefore our results may be predictive of the future generations of process analysts.

Last, we consider the effect of setting as a potential threat to external (as well as internal) validity: We used an online and a paperbased system. Therefore, participants either viewed process models on screen or as a printout. Both these practices are widespread in industry practice, where models are either provided through an intranet web page linked to a modeling tool (e.g., ARIS Web Publisher), or provided in print out format as part of process handbooks or manuals of procedures. Our study used both options, thereby increasing the external validity of the study. As noted above, we observed no statistical differences in relation to the experimentMode, thereby alleviating concerns about the internal validity of this treatment.

## 5. Implications

In this section, we discuss implications for research (Section 5.1) and for practice (Section 5.2).

## 5.1. Implications for research

The <sup>fi</sup>ndings presented in this paper have three major implications for research. First, we have shown that textual labels hamper syntax comprehension of process models. This <sup>fi</sup>nding emphasizes the relevance of cognitive load theory for interpreting comprehension phenomena in this context. This is in line with prior research that identi<sup>fi</sup>ed size and complexity as factors having a negative impact on process model comprehension [27], although a direct reference to cognitive load theory is missing in these works. Cognitive load theory might offer a useful perspective to study the impact of process model complexity on comprehension in a more detailed way in future research. We further identify research on textual labels, e.g., [32] to be an important extension of our work, given that we identi<sup>fi</sup>ed textual labels to be a potential barrier to syntactical process model comprehension. Indeed, future work may examine how textual labels could be speci<sup>fi</sup>ed in order to decrease the additional cognitive burden on the model viewer.

Second, research on expert performance has established a close link between expertise and the duration and extent of training [12,25]. Our <sup>fi</sup>ndings point to the fact that expertise is a taskspeci<sup>fi</sup>c phenomenon, as emphasized in Ref. [5]. Knowledge in theoretical aspects of process model syntax have been found as a signi<sup>fi</sup>- cant factor of comprehension while general modeling intensity and general modeling experience were not signi<sup>fi</sup>cant. We speculated that semantic comprehension might be much more dependent on these factors than syntactical comprehension appeared to be. This speculation suggests that experience might have a different impact on comprehension of syntax, semantics, and pragmatics of a process model. These levels of comprehension might even be in con<sup>fl</sup>ict with each other. This aspect requires a deeper investigation in future research, both from a theoretical and from a behavioral perspective.

Third, our research showed that there is a trade-off in understanding the formal, syntactical structure of a model and its semantical content (as conveyed through textual labels). In this paper, therefore, we chose to examine process model understanding in terms of comprehension of syntactical content. Other research, by contrast, has examined semantic understanding, e.g., [41] while neglecting the syntactical comprehension. Future research should now combine these streams of study to be able to assert the relevant factors important to syntactic and semantic understanding, as well as the interactions between understanding of syntax and semantics. Ultimately, this vein of research can then arrive at a body of knowledge informing pragmatic understanding of process models as representations of knowledge for action [22], and study the factors the in<sup>fl</sup>uence how individuals use process models to solve tasks such as organizational re-design, software speci<sup>fi</sup>cation, certi<sup>fi</sup>- cation and others.

## 5.2. Implications for practice

Our research has at least two relevant implications for practice. First, we note that the importance of theoretical knowledge for syntactical process model comprehension was supported by our tests. In contrast, practical experience does not seem to have a signi<sup>fi</sup>cant impact. These facts suggest that it is essential to provide formal process modeling education to staff members before letting them take part in a project. Such a training program should proceed in two stages. Initially, it should develop suf<sup>fi</sup>cient expertise in the syntactical rules of process modeling to ensure that practitioners appropriately understand the syntax of process models. Subsequently, the training program could proceed to more realistic process models that carry domain semantics, to teach practitioners how to reason about the processes being modeled. The recommendations in Ref. [42] could guide the development of a staged training program.

Second, we note that there are several situations in practice when syntactical aspects have to be investigated for a process model. This is, for instance, the case when a process model needs to be veri<sup>fi</sup>ed for soundness [53] before it is deployed in a work<sup>fl</sup>ow system. Our <sup>fi</sup>ndings suggest that a tool option to hide, or to abbreviate the activity labels, could help analysts when correcting a syntactically unsound model. The abbreviation would reduce the cognitive load of the modeler, which would permit her to focus her attention on control <sup>fl</sup>ow. Corresponding features are not yet part of nowadays modeling tools.

## 6. Conclusions

Using process modeling for the analysis and design of processaware information systems is an emerging, highly relevant domain of Information Systems practice. In this paper, we have described the formulation and execution of an experimental study to examine factors of process model comprehension.

We identify two key limitations to the work carried out. First, congruent to other studies, e.g. [6,32], we used post-graduate students as proxies for novice business analysts. Second, our operationalization of model comprehension was focused on the syntactical structure of a process model. Future work could investigate other aspects of understanding, for instance, through problem-solving tasks, e.g. [41]. In spite of the boundaries set by these limitations, we believe our work offers two central contributions. First, we provided a theoretical framework to de<sup>fi</sup>ne levels of process model comprehension task performance and ef<sup>fi</sup>ciency, and the set of factors relevant to reaching comprehension on basis of cognitive load theory and semiotic considerations. Second, our series of experiments examined two sets of relevant factors—model factors and personal factors. We found that theoretical knowledge and, to a small extent, process modeling expertise, are important personal factors, and also found a negative effect of textual domain semantics—a model factor—on the comprehension of the formal content of process models.

Our work extends the body of knowledge in the <sup>fi</sup>eld of process modeling, and thereby paves the way to more effective and ef<sup>fi</sup>cient process modeling—which will signi<sup>fi</sup>cantly increase the bene<sup>fi</sup>ts of process modeling in organizations [17], and also reduce associated direct and indirect costs. In moving forward, we discussed a number of speculations and possible directions for future research in our implications section. Most notably, it will be an important objective for future research to study the joint impact of various factors on different levels of comprehension, from syntactical to semantical to pragmatic.

## Acknowledgments

Dr. Recker's contributions to this work have partially been sponsored by a grant from the Australian Research Council (ARC DE120100776) and by a Fellowship from the Alexander-von-Humboldt Foundation.

## Appendix A. Experimental material

A complete sample workbook of the questionnaire used in the printout experiment is available with abstract models (http://www. mendling.com/2009-Fragebogen-Rahmen-ABCDEF-abstrakt.pdf) and with textual models (http://www.mendling.com/2009-Fragebogen-Rahmen-ABCDEF-konkret.pdf).

Task 1: process modeling intensity

• How often do you encounter process models in practice? (never, less than once a month, more than once a month, daily)

Task 2: process modeling experience

• When did you <sup>fi</sup>rst work with process models in practice? (less than a month ago, less than a year ago, less than three years ago, more than three years ago)

Task 3: theoretical knowledge

• After exclusive choices, at most one alternative path is executed (yes/no).

• Exclusive choices can be used to model repetition (yes/no).

• Synchronization is modeled in a Petri net by a place with two transitions in its preset (yes/no).

• Synchronization means that two activities are executed at the same time (yes/no).

• An inclusive OR can activate concurrent paths (yes/no).

• If two activities are concurrent, they have to be executed at the same time (yes/no).

• If an activity is modeled to be part of a loop, it has to be executed at least once (yes/no).

• Having an AND-split at the exit of a loop can lead to non-termination (yes/no).

• A deadlock is the result of an inappropriate combination of splits and joins (yes/no).

• Processes without loops cannot deadlock (yes/no).

• Both an AND-join or an XOR-join can be used as a correct counterpart of an OR-split (yes/no).

• A multiple choice activates either one or all subsequent paths (yes/no).

Task 4: comprehension questions for model 4 of Fig. 1

(1) Is U always executed, when T has been executed? (yes/no)

(2) If F is executed, has Z or E been executed? (yes/no)

(3) Is it possible to execute U as well as I after F? (yes/no)

(4) Can this process be completed by executing less than <sup>fi</sup>ve activities? (yes/no)

(5) When R is executed, is it possible that M has been executed before? (yes/no)

(6) Is it guaranteed that the process has neither deadlocks nor lack of synchronization? (yes/no)

## References

[1] R. Agarwal, P. De, A. Sinha, Comprehending object and process models: an empirical study, IEEE Transactions on Software Engineering 25 (4) (1999) 541–556.

[2] M.I. Aguirre-Urreta, G.M. Marakas, Comparing conceptual modeling techniques: a critical review of the eer vs. oo empirical literature, The DATA BASE for Advances in Information Systems 39 (2) (2008) 9–32.

[3] W. Bandara, Factors and measures of business process modelling: model building through a multiple case study, European Journal of Information Systems 14 (2005) 347–360.

[4] V. Basili, F. Shull, F. Lanubile, Building knowledge through families of experiments IEEE Transactions on Software Engineering 25 (4) (1999) 456–473.

[5] S. Bonner, N. Pennington, Cognitive processes and knowledge as determinants of auditor expertise, Journal of Accounting Literature 10 (1) (1991) 1–50.

[6] A. Burton-Jones, P. Meso, The effects of decomposition quality and multiple forms of information on novices’ understanding of a domain from a conceptual model Journal of the Association for Information Systems 9 (12) (2008) 784–802.

[7] A. Burton-Jones, Y. Wand, R. Weber, Guidelines for empirical evaluations of conceptual modeling grammars, Journal of the Association for Information Systems 10 (6) (2009) 495–532.

[8] G. Canfora, F. García, M. Piattini, F. Ruiz, C. Visaggio, A family of experiments to validate metrics for software process models, Journal of Systems and Software 77 (2) (2005) 113–129.

[9] T.D. Cook, D.T. Campbell, Quasi-Experimentation: Design and Analysis Issues, Houghton Mif<sup>fl</sup>in, Boston, Massachusetts, 1979.

[10] I. Davies, P. Green, M. Rosemann, M. Indulska, S. Gallo, How do practitioners use conceptual modeling in practice? Data & Knowledge Engineering 58 (3) (2006) 358-380

[11] A. Dreiling, M. Rosemann, W.M.P. van der Aalst, W. Sadiq, From conceptual process models to running systems: a holistic approach for the con<sup>fi</sup>guration of enterprise system processes, Decision Support Systems 45 (2) (2008) 189–207.

[12] K. Ericsson, A. Lehmann, Expert and exceptional performance: evidence of maximal adaptation to task constraints, Annual Review of Psychology 47 (1) (1996) 273–305.

[13] T. Erl, Service-oriented Architecture: Concepts, Technology, and Design, Prentice Hall, Upple Saddle Revier, New Jersey, 2005.

[14] C. Ferris, What are web services? Communications of the ACM 46 (6) (2003) 31–32.

[15] I. Hahn, I. Kim, Why are some diagrams easier to work with? Effects of diagrammatic representation on the cognitive integration process of systems analysis and design ACM Transactions on Computer-Human Interaction 6 (3) (1999) 181–213.

[16] M. Hollander, D.A. Wolfe, Nonparametric Statistical Methods, 2nd Edition John Wiley and Sons, New York, New York, 1999.

[17] M. Indulska, P. Green, J. Recker, M. Rosemann, Business process modeling: Perceived bene<sup>fi</sup>ts, in: S. Castano, U. Dayal, A.H.F. Laender (Eds.), Conceptual Modeling—ER 2009, Lecture Notes in Computer Science, Springer, Gramado, Brazil, 2009, pp. 458–471.

[18] A. Jedlitschka, M. Ciolkowski, D. Pfahl, Reporting experiments in software engineering, Guide to advanced empirical software engineering, Springer, 2008, pp. 201–228.

[19] R. Kanfer, P.L. Ackerman, T.C. Murtha, B. Dugdale, L. Nelson, Goal setting, conditions of practice, and task performance: a resource allocation perspective, Journal of Applied Psychology 79 (6) (1994) 826–835.

[20] B. Kiepuszewski, A.H.M. ter Hofstede, W.M.P. van der Aalst, Fundamentals of control <sup>fl</sup>ow in work<sup>fl</sup>ows, Acta Informatica 39 (3) (2003) 143–209.

[21] N. Kock, J. Verville, A. Danesh-Pajou, D. DeLuca, Communication <sup>fl</sup>ow orientation in business process modeling and its effect on redesign success: results from a <sup>fi</sup>eld study, Decision Support Systems 46 (2) (2009) 562–575.

[22] J. Krogstie, G. Sindre, H.D. Jorgensen, Process models representing knowledge for action: a revised quality framework, European Journal of Information Systems 15 (1) (2006) 91-102

[23] A. Lakhotia, Understanding someone else's code: analysis of experiences, Journal of Systems and Software 23 (3) (1993) 269–275.

[24] O. Lindland, G. Sindre, A. Sølvberg, Understanding quality in conceptual modeling, IEEE Software 11 (2) (1994) 42–49.

[25] P. Lindsay, D. Norman, Human Information Processing: An Introduction to Psychology, second edition Academic Press, 1977.

[26] D. Liu, M. Shen, Business-to-business work<sup>fl</sup>ow interoperation based on processviews, Decision Support Systems 38 (3) (2004) 399–419.

[27] J. Mendling, Metrics for process models: empirical foundations of veri<sup>fi</sup>cation, error prediction and guidelines for correctness, Lecture Notes in Business Information Processing, Vol. 6, Springer, Berlin, Germany, 2008.

[28] I. Mendling, M. Strembeck, Influence factors of understanding business process models, in: W. Abramowicz, D. Fensel (Eds.). Business Information Systems—BIS 2008, Lecture Notes in Business Information Processing, Vol. 7, Springer, Innsbruck, Austria 2008 pp. 142-153

[29] J. Mendling, W.M.P. van der Aalst, Towards EPC semantics based on state and context, in: M. Nüttgens, F.J. Rump, J. Mendling (Eds.), Proceedings of the 5th GI Workshop on Business Process Management with Event-Driven Process Chains (EPK 2006), German Informatics Society Vienna Austria 2006 pp. 25–48

[30] J. Mendling, H.A. Reijers, J. Cardoso, What makes process models understandable? in: G. Alonso, P. Dadam, M. Rosemann (Eds.), Business Process Management— BPM 2007, Lecture Notes in Computer Science, Vol, 4714, Springer, Brisbane, Australia. 2007 pp.48-63.

[31] J. Mendling, H.A. Reijers, W.M.P. van der Aalst, Seven process modeling guidelines (7PMG) Information and Software Technology 52 (2) (2010) 127–136

[32] J. Mendling, H.A. Reijers, J. Recker, Activity labeling in process modeling: empirical insights and recommendations, Information Systems 35 (4) (2010) 467–482.

[33] G. Miller, The magical number seven, plus or minus two: some limits on our capacity for processing information, Psychological Review 63 (2) (1956) 343–355.

[34] T. Moher, D. Mak, B. Blumenthal, L. Leventhal, Comparing the Comprehensibility of Textual and Graphical Programs: The Case of Petri Nets, in: C. Cook, J. Scholtz, J. Spohrer (Eds.), Empirical Studies of Programmers: Fifth Workshop: Papers Presented at the Fifth Workshop on Empirical Studies of Programmers, December 3–5, 1993, Ablex Pub, 1993, pp. 137–161.

[35] M.J. Nanna, S.S. Sawilowsky, Analysis of Likert scale data in disability and medical rehabilitation research, Psychological Methods 3 (1) (1998) 55–67.

[36] D.A. Norman, Cognitive engineering, in: D.A. Norman, S.W. Draper (Eds.), User Centered System Design: New Perspectives on Human-computer Interaction, Lawrence Erlbaum Associates, Hillsdale, New Jersey, 1986, pp. 31–61.

[37] S. Patig, V. Casanova-Brito, B. Vögeli, It requirements of business process management in practice—an empirical study, in: R. Hull, J. Mendling, S. Tai (Eds.), Business Process Management—BPM 2010, Lecture Notes in Computer Science, Vol. 6336, Springer, Hoboken, New Jersey, 2010, pp. 13–28.

[38] G. Poels, A. Maes, F. Gailly, R. Paemeleire, The pragmatic quality of resources–events– agents diagrams: an experimental evaluation, Information Systems Journal 21 (1) (2011) 63–89.

[39] H. Purchase, Which aesthetic has the greatest effect on human understanding? Graph Drawing: 5th International Symposium, Gd'97, Rome, Italy, September 18–20, 1997: Proceedings, Springer, 1997, pp. 248–261.

[40] J. Recker, Continued use of process modeling grammars: the impact of individual difference factors, European Journal of Information Systems 19 (1) (2010) 76–92.

[41] J. Recker, A. Dreiling, The effects of content presentation format and user characteristics on novice developers’ understanding of process models, Communications of the Association for Information Systems 28 (6) (2011) 65–84.

[42] J. Recker, M. Rosemann, Teaching business process modeling—experiences and recommendations, Communications of the Association for Information Systems 25 (32) (2009) 379–394

[43] J. Recker, M. Rosemann, M. Indulska, P. Green, Business process modeling: a comparative analysis, Journal of the Association for Information Systems 10 (4) (2009) 333–363.

[44] H.A. Reijers, J. Mendling, Modularity in process models: review and effects, Proceedings of BPM 2008, Springer, 2008, pp. 20–35.

[45] H.A. Reijers, J. Mendling, A study into the factors that in<sup>fl</sup>uence the understandability of business process models, IEEE Transactions on Systems Man and Cybernetics, Part A 41 (3) (2011) 449–462.

[46] H.A. Reijers, T. Freytag, J. Mendling, A. Eckleder, Syntax highlighting in business process models, Decision Support Systems 51 (3) (2011) 339–349.

[47] E. Rolón Aguilar, F. García, F. Ruiz, M. Piattini, An exploratory experiment to validate measures for business process models, First International Conference on Research Challenges in Information Science (RCIS), 2007

[48] K. Sarshar, P. Loos, Comparing the control-<sup>fl</sup>ow of epc and petri net from the end-user perspective, in: W. Aalst, B. Benatallah, F. Casati, F. Curbera (Eds.), Business Process Management, 3rd International Conference, BPM 2005, Nancy, France, September 5–8, 2005, Proceedings, LNCS 3649, 2005, pp. 434–439.

[49] A.-W. Scheer, ARIS—Business Process Modeling, 3rd Edition Springer, Berlin, Germany, 2000.

[50] C. Soh, M.L. Markus, K.H. Goh, Electronic marketplaces and price transparency: strategy, information technology, and success, MIS Quarterly 30 (3) (2006) 705–723.

[51] J. Sweller, P. Chandler, Why some material is dif<sup>fi</sup>cult to learn, Cognition and Instruction 12 (3) (1994) 185–223.

[52] J. Sweller, J. Van Merrienboer, F. Paas, Cognitive architecture and instructional design, Educational Psychology Review 10 (3) (1998) 251–296

[53] W.M.P. van der Aalst, Ch. work<sup>fl</sup>ow veri<sup>fi</sup>cation: <sup>fi</sup>nding control-<sup>fl</sup>ow errors using Petri-net-based techniques, Business Process Management, Vol. LNCS 1806, Springer Verlag, 2000, pp. 161–183.

[54] H.J. Wang, J.L. Zhao, L.-J. Zhang, Policy-driven process mapping (pdpm): discovering process models from business policies, Decision Support Systems 48 (1) (2009) 267–281.

[55] C. Wohlin, P. Runeson, M. Höst, M. Ohlsson, B. Regnell, A. Wesslen, Experimentation in Software Engineering: An Introduction, Kluwer Academic Publishers, 2000.

![](/api/attachments/6X5WKFEC/fulltext/images/01fffff1208ce4b557f1407cec8e3d39b8b6d1bd286b4feecec49a8ebda26885.jpg)

Jan Mendling is a Full Professor with the Institute for Information Business at Wirtschaftsuniversität Wien (WU Vienna), Austria. His research areas include Business Process Management, Conceptual Modelling and Enterprise Systems. He has published more than 100 research papers and articles, among others in ACM Transactions on Software Engineering and Methodology, Information Systems, Data & Knowledge Engineering, Decision Support Systems, Formal Aspects of Computing and Information & Software Technology. He is a member of the editorial board of three international iournals. His Ph.D. thesis has won the Heinz-Zemanek-Award of the Austrian Computer Society and the German Targion-Award for dissertations in the area of strategic information management. He is one of the founders of the Berlin BPM Community of Practice (http://www.bpmb.de) and organizer of several academic events on process management. He was program co-chair of the International Conference on Business Process Management 2010.

![](/api/attachments/6X5WKFEC/fulltext/images/0a24f4c1355623de49662402c74611da32333bbb4bb191d41cf437a0d6f76496.jpg)

Mark Strembeck is an Associate Professor of Information Systems at the Vienna University of Economics and Business (WU Vienna), Austria. His research interests include access control, role engineering, secure business systems, process modeling, model-driven software development, language engineering, and the modeling and management of dynamic software systems. Among others, he has published in ACM Transactions on Information and System Security, IEEE Security & Privacy, Software: Practice & Experience, and Information & Software Technology. He received his doctoral degree as well as his Habilitation degree (venia docendi) from WU Vienna. He is a key researcher at the Secure Business Austria Research Center (http://www.sba-research.org/ team/), and the Vice Institute Head of the Institute for Information Systems at WU Vienna (http://nm.wu.ac.at/).

![](/api/attachments/6X5WKFEC/fulltext/images/da5351a147c237f9893ab8466a0f01b630d7ffb1e6516b51714ab4e5dbd0a645.jpg)

Jan Recker is an Associate Professor of Information Systems Discipline at Queensland University of Technology. He received a B.Sc. IS and M.Sc. IS from the University of Muenster, Germany in 2004 and a Ph.D. in Information Systems from Queensland University of Technology in 2008. His main areas of research include methods and extensions for business process design and the usage of process design in organizational practice. He has been the author of more than 100 journal articles and conference papers on these topics, including publications in the Journal of the Association for Information Systems, Information Systems, the Communications of the Association for Information Systems, the European Journal of Information Systems, the Scandinavian Journal of Information Systems, and others. Dr. Recker is a member of the editorial board of four international journals and serves on the program committee of multiple IS conferences
