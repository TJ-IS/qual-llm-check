---
otero_id: 25095
otero_key: "K8FRYBJR"
title: "The Use of Explanations in Knowledge-Based Systems: Cognitive Perspectives and a Process-Tracing Analysis"
authors: ""
year: "2000"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2000.11045646"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Use of Explanations in Knowledge-Based Systems: Cognitive Perspectives and a Process-Tracing Analysis

Ji-Ye Mao, Izak Benbasat

To cite this article: Ji-Ye Mao, Izak Benbasat (2000) The Use of Explanations in Knowledge-Based Systems: Cognitive Perspectives and a Process-Tracing Analysis, Journal of Management Information Systems, 17:2, 153-179

To link to this article: http://dx.doi.org/10.1080/07421222.2000.11045646

![](/api/attachments/K8FRYBJR/fulltext/images/52a730089d77a2ae9042406e7dbb90ec1a0f06db1175e46a21bfd3ca8018b7e2.jpg)

Published online: 09 Jan 2015.

![](/api/attachments/K8FRYBJR/fulltext/images/78d56fcf792eeaff09dec31c2973c270539a7c2dd9dd6d7a8e3045cdc1f0bff7.jpg)

Submit your article to this journal

![](/api/attachments/K8FRYBJR/fulltext/images/d5b51ee38deb7e0d9c145db3aeb05a986842d597993542a9d98692ddca15989d.jpg)

Article views: 11

![](/api/attachments/K8FRYBJR/fulltext/images/ddf01a8743162f9d34e054f76ac2a679fbe7b703282a966f0bc28efeeeae0b10.jpg)

View related articles

# The Use of Explanations in Knowledge-Based Systems: Cognitive Perspectives and a Process-Tracing Analysis

JI-YE MAO AND IZAK BENBASAT

JI-YE MAO is Assistant Professor of Management Sciences at the University of Waterloo, Waterloo, Canada. He received his Ph.D. in management information systems in 1995 from the University of British Columbia. His research interests include human–computer interaction, end-user training, and knowledge management. He has studied the behavioral and cognitive issues related to electronic performance support systems, hypertext and hypermedia-based management support systems, and explanations in knowledge-based systems.

IZAK BENBASAT is CANFOR Professor of Management Information Systems, at the Faculty of Commerce and Business Administration, The University of British Columbia (UBC), Vancouver, Canada. He received his Ph.D. (1974) in Management Information Systems from the University of Minnesota. His current research interests are in: investigating the role of explanations in intelligent systems; measuring infor mation systems competence in line managers and business competence in information systems professionals, and the impact of these competencies on the successful deployment of information technologies; evaluating human–computer interfaces; and comparing methods for conducting information systems research.

ABSTRACT: This exploratory research investigates the nature of explanation use and factors that influence it during users’interaction with a knowledge-based system (KBS) for decision-making. It draws upon several cognitive perspectives to help understand when, why, and how explanations are used. A verbal protocol analysis was conducted based on a laboratory experiment involving a KBS for financial analysis. Major categories of explanation use were identified, and accounted for with relevant cognitive perspectives. Results show that explanations were requested to deal with comprehension difficulties caused by various types of perceived anomalies in KBS output. There were qualitative and quantitative differences in the nature and extent of explanation use between novices and experienced professionals. These results offer new insights to why explanations are useful and important, what factors influence explanation use, and what information should be included in explanations.

KEY WORDS AND PHRASES: explanations, explanations in expert systems, knowledgebased systems, verbal protocol analysis

EXPLANATION IS ONE OF THE MOST COMMON HUMAN PHENOMENA [41]. People give and receive explanations every day to understand their world. Similarly, explanation is essential to the interaction between users and knowledge-based (expert) systems (KBSs), describing what a system does, how it works, and why its actions are appropriate [47]. In most cases, KBSs assist or advise, rather than completely replace, human decision-makers. Since decision-makers must live with the consequences and risks associated with their decisions, they are unlikely to trust any advice they do not understand. Trust in a system is developed not only by the quality of its output, but also by evidence of how it was derived [46]. It is therefore imperative that KBS performance be transparent and understandable [10]. Explanation facilities and the capability to customize explanations were rated by users as the fourth and fifth most important factors, respectively, among 87 KBS shell capabilities [45]. It has been shown that explanation can make KBS conclusions more acceptable [53]. Explanation has become a fundamental feature of KBSs since MYCIN [25, 43], and most existing KBSs provide some form of explanation.

A recent survey of the field has shown that claims of the decline of KBSs are greatly exaggerated [14]. Whereas early applications of KBSs in industry “often over-chal lenged the technology, leading to poor results” [14, p. 59], since the mid-1980s designers have begun to focus on narrow and well-defined tasks, such as the granting of loans. For example, EvEnt, a system developed by a French bank called Evalog, has decreased the cost of processing loans tenfold, increased the bank’s loan processing capacity, and helped minimize the bank’s risk exposure [14]. Similarly, following the success of R1/XCON by Digital Equipment Corporation to configure computer systems, a wealth of configuration systems have been built for the construction of computers, communications networks, automobiles, and circuit boards [40]. Total sales of KBS development tools have grown an average of about 16 percent per year since 1988 [14]. Research on explanations has also evolved to develop hypermedia-based explanation facilities for KBS to provide context-sensitive explanations in the forms of text, audio, and video [19].

Moreover, the need for explanation is not limited to KBSs. Explanation facilities exist in other intelligent systems that contain a component of explicitly represented knowledge, such as intelligent tutoring systems, intelligent agents, and other complex systems [24, 27]. For example, it was observed that an explanation facility was needed as an integral part of Patient Advocate, an Internet-based “intelligent agent,” to give patients information about their health conditions [31]. Explanation can also potentially enhance trust between computer users and their “intelligent agents” [30]. In designing explanation facilities for these intelligent systems, valuable lessons can be drawn from the continuing research on explanations generated by KBS.

Prior research has primarily focused on how to provide explanations and the effects of such explanations. The applied artificial intelligence research on explanation has focused on design strategies, ranging from supplementing the reasoning trace with additional knowledge to completely reconstructing explanations based on a separate knowledge base [e.g., 8, 46, 51]. However, to a large extent, the quest for effective explanations has not been based on a strong cognitive foundation and empirical find ings on the needs of users. Whereas empirical research in information systems (IS) has studied the effects and the determinants of explanation use [e.g., 11, 33, 37, 53; cf. 24 for a comprehensive review], these prior empirical studies were not devoted to the cognitive aspects of explanation-seeking behavior or the nature of explanation use. Therefore, fundamental questions, such as why explanations are desirable and why KBS users request explanations, have not been addressed satisfactorily from a cognitive perspective.

This exploratory research is directed toward an understanding of explanation use based on cognitive theories and empirical evidence. It draws upon several relevant cognitive perspectives on explanation use as its theoretical background and backing for its findings from a verbal protocol analysis. It addresses, in particular, why and how KBS explanations are used for decision-making and how users’ level of domain expertise influences explanation use.

In this research, a laboratory experiment was conducted to observe the explanation acquisition and use behavior of decision-makers supported by a KBS for financial analysis. Process-tracing methods [16, 36, 48] were utilized to identify the nature of explanation use in the context of problem-solving. Concurrent verbal protocol data, in addition to computer logs of the entire user–KBS interaction process, were col lected to identify patterns of explanation use and to calculate descriptive statistics.

This paper is organized as follows: The next section will provide an overview of common explanation types in KBS and recent empirical studies. Following this, several relevant theoretical perspectives will be presented toward a cognitive foundation for studying explanation use. Then, the research method will be described, including details of the experimental setting and procedures for collecting verbal protocols. Next, the results of data analysis will be presented. Lastly, this paper concludes with a discussion of the key results and implications of this study.

Prior Research on Explanations

## Common Explanation Types

WHEREAS SEVERAL TYPES OF EXPLANATIONS have been proposed by applied artifi cial intelligence research [cf. 24, 44], only the most common ones—i.e., reasoningtrace, justification, and strategic explanations, which are the focus of this research—are briefly reviewed herein.

KBSs are able to provide explanations because they encode knowledge in a form of symbolic logic and the trace of the problem-solving process is available for generating explanations. For example, in MYCIN, superordinate goals can be traced upward along the rule chain to reveal why certain inputs from users are important, whereas subordinate goals and causal antecedents can be found downward to show how a particular conclusion is reached [10]. Before answering a question, a user can question the importance or relevance of the question with WHY [8] (user input is in capitalized letters; all other text is produced by MYCIN):

23) Is J. Smith a compromised host?

[i.e., WHY is it important to determine whether J. Smith is a compromised host?]

[3.0] This will aid in determining whether J. Smith is immunosuppressed.

[3.1] J. Smith is not a compromised host

then

it is definite (1.0) that J. Smith is not immunosuppressed.

[RULE343].

[back to question 23 . . .]

\*\*WHY

[i.e., WHY is it important to determine whether J. Smith is immunosuppressed?]

[4.0] . . .in order to determine whether J. Smith has received corticosteriods.

[4.1] J. Smith is not immunosuppressed

then

it is definite (1.0) that J. Smith has not received corticosteriods.

[RULE395]

[back to question 23 . . .]

\*\*WHY

Similarly, a user can inquire HOW a conclusion is reached.

\*\*HOW DID YOU DECIDE THAT ORGANISM-1 MIGHT BE AN E. COLI?

I used RULE021 to conclude that the identity of ORGANISM-1 is E.coli. This gave a cumulative CF of (0.47).

Then I used RULE084 to conclude that the identity of ORGANISM-1 is E.coli.

This gave a cumulative CF of (0.55).

Finally, I used RULE003 to conclude that the identity of ORGANISM-1 is E.coli. This gave a cumulative CF of (0.74).

Such explanations are known as reasoning-trace, or simply trace, explanations. They are relatively easy to create as a by-product of the reasoning-process of backward chaining systems. In addition to simplicity, which is the reason they are the prevailing form of explanation, the other major strength is the guaranteed consistence with the problem-solving process [46]. However, they are rigid, inflexible, and diffi cult to understand for the end users [e.g., 20, 34]. A major problem is that the knowledge most needed to provide a justification for the behavior of a KBS is not accessible in the rule trace [46]. For example, the justification for the tetracycline rule in MYCIN—“If the patient is less than 8 years old, don’t prescribe tetracycline”—lies outside of the rule base and is beyond the problem-solving knowledge. What is needed for the justification is the underlying causal process, e.g., drug deposition in developing bones and the social ramifications of permanently blackened teeth [8].

It has been suggested that explanations need to go beyond reasoning-trace to provide backing or first principles for KBS action. GUIDON [8] and XPLAIN [46] pro vided justification explanations to rationalize the behavior of KBS based on explicitly represented domain knowledge, e.g., a causal model or deep knowledge. In particular, the domain model of XPLAIN consisted of descriptive facts about the application domain, such as causal relationships and classification hierarchies, and a set of domain principles, such as methods and heuristics. Explanations provided by XPLAIN are known as “justification” because the main objective is to justify why what a KBS is doing is reasonable and appropriate, rather than merely to describe what has been done. For example, to justify “Why is serum calcium an important factor in digitalis administration?” the underlying deep knowledge is invoked, i.e., increased serum leads to higher automaticity, which may cause a change to ventricular fibrillation, a dangerous heart condition.

It is also recognized that information about the overall problem-solving strategy should be made available to users in the form of strategic explanations at the task level, focusing on the problem-solving approach. For example, NEOMYCIN [8] provided a strategic explanation for a diagnosis problem in terms of tasks to be com pleted, such as to “establish hypothesis space” and “explore and refine.” While this type of explanation is potentially useful for revealing the global strategy, there is no effective generic approach to providing it because the underlying knowledge is diffi cult to represent in a way that can be used as part of explanations. For example, in rule-based systems, much of the strategic information is implicit in the firing order of the rules and thus not accessible for explanation.

The above three generic types of explanations are considered most fundamental to explanation [5]. The reasoning-trace type remains the most common one due to its simplicity of design, while others tend to be too complicated to implement and too domain-specific for common use [50].

## Prior Empirical Studies

A comprehensive review of the empirical literature on explanation use is beyond the scope of this paper. Interested readers are referred to [12] and [24]. In general, IS researchers have focused on the effects of various types of explanations and determi nants of explanation use. Several studies have investigated the use of trace, justification, and strategic explanations. For example, Ye and Johnson [53] found that the justification type of explanation was requested more than the other two types. The effects of users’ domain expertise on explanation use were also studied [11, 53]. Novices requested significantly more explanations than experts, and explanations were equally effective in increasing users’ belief in and acceptance of the KBS for both groups [53]. Hsu [26] studied the effects of cognitive styles and interface designs on the use of KBS, focusing on knowledge transfer from KBS to novice users. It was found that the availability of explanations was important for transferring knowledge to novice users, and that the use of justification explanations resulted in a greater amount of knowledge transfer than using rule-trace explanations alone.

However, none of the prior empirical studies was aimed at understanding how explanations were used (as distinct from being requested) in any way in a decision-making process, and the nature of the use. Typically, in these studies, if an explanation was requested, it was assumed that it was indeed read and used, without investigating its role in the decision-making process. In some studies, just because explanations were available in certain experimental conditions, conclusions on explanation use were drawn without even a measure of the extent of explanation use. Therefore, other than user opinions, there exists no process-tracing data on why users request explanations, how explanations are used cognitively, and why users prefer one type of explanation to another. To date little is known from empirical work about the nature and extent of explanation use in the context of decision-making.

## Cognitive Perspectives on Explanation Use

THIS SECTION DRAWS UPON COGNITIVE THEORIES ranging from the cognitive effort perspective, explanation, question asking, discourse comprehension, to novice–expert differences, to help understand when, why, and how explanations are used.

## Cognitive Effort Perspective to Explanation Use

Users’ tendency to request explanations can be predicated based on several theoreti cal perspectives. The first is the cognitive effort perspective [35]. An individual typically considers the cost of taking a particular course of action against the benefits that will accrue from taking that action. Empirical research has confirmed that decisionmakers attend more to effort reduction than to decision quality maximization [39], that is, one is motivated to pursue the strategy requiring the least effort and yet pro viding an acceptable solution [2].

Closely related to the above theoretical perspective is the notion of the production paradox [4]. It refers to the conflicts between learning and working—two activities that have both costs and benefits, and are constantly present in work settings. Learning is inhibited by lack of time and working is inhibited by lack of knowledge. People are more concerned about getting their tasks done than gaining new knowledge, and tend to avoid learning if they can muddle through. However, the “cost” of learning may be reduced through the design of better learning support facilities, and convenient and easy to use interfaces [4].

Gregor [23] and Gregor and Benbasat [24] have extended the use of the cognitive effort perspective to the domain of KBS explanation use. They suggested that costbenefit trade-offs influence KBS explanation use, since such use is discretionary. In fact, empirical studies have shown that users request only a relatively small portion of the available explanations [e.g., 11, 24]. One plausible reason for this could be that users tend to create their own explanation before requesting one from the KBS. Knowl edgeable users who are capable of creating their own explanation rapidly and reliably are more likely to do so, with little effort. In general, however, to increase the use of KBS explanations, designers could influence the cost-benefit trade-off by enhancing the usefulness, accessibility, and ease of use of explanation facilities.

## Theories Pertinent to Explanation and Question Asking

Research in cognitive science and education on question asking [21] is useful for understanding explanation acquisition behavior. It has been observed that those who are knowledgeable often ask more questions and generate more comments on advanced subjects, but few on novice-level subjects; the situation is vice versa for novices [32]. Questions asked by novices are typically shallow, i.e., addressing only the content and interpretation of explicit material, rather than high-level questions that involve inferences, applications, and synthesis [18]. Furthermore, they are infrequently raised [13], since novices often fail to identify their own knowledge deficit [21]. For example, novices frequently miss contradictions and inconsistencies [13]. Failure to identify the deficits in knowledge means there is an inadequate cognitive foundation for asking questions, since questions arise from knowledge rather than ignorance.

Miyake and Norman [32] suggest that a proper knowledge structure is needed not only for formulating the question, but also for interpreting the response. The ability to ask questions during learning is determined by the existence of appropriate knowledge structures and the level of completeness of those structures with respect to the new material. Similarly, according to Schank and Abelson’s script theory [42], a higher level piece of knowledge identifies a lower-level “hole,” which may be filled with explanation. A central theme of Flammer’s [18] theory of question asking is that questions concern knowledge that the questioner lacks, but they presuppose available knowledge. In addition to a perceived deficit in knowledge, a low level of confidence in one’s own knowledge may lead to questioning, and the importance of the information for further actions and current goals may also influence question asking.

An explanation process starts with finding an anomaly, and then establishes the kind of explanation that will make it less anomalous [41]. A person interpreting an observation determines if it “makes sense,” by comparing it to some standard involving patterns, consequences, and reasons—for example, is the observed action recognized as part of an overall plan? As implied in cognitive theories of discourse comprehension [22], inferences are constructed during discourse comprehension based on readily available task information and domain knowledge. When coherence cannot be achieved via inferencing, anomalies are perceived. Graesser and McMahen [21] posit that it is anomalous information that triggers questions. Empirical studies have shown that the two most significant types of anomalies, among others, are the absence of critical information and the presence of contradictions [21].

In terms of the content of explanation, Schank [41] suggests a list of different types of knowledge, such as:

1. Plan (strategy): People explain the action of others by understanding where an action that is not understood fits within a broader plan.

2. Goals (why): An action can be explained by connecting it to the goal it is intended to achieve.

3. Scripts (how): They are simpler and fossilized plans in terms of a set of typical steps of action.

4. New facts: They are new knowledge necessary for making sense of things.

5. Laws of physics: Because of their incomplete knowledge, people often take a new law of physics as an explanation.

6. Rules of thumb: These are heuristics that can be taken as explanation.

7. Institutionalized rules: An action can be explained if the actor is behaving according to externally defined rules.

Whereas only a small subset of the knowledge elements is incorporated in existing KBS explanations, the above list can be useful for the systematic design and evaluation of KBS explanations.

In summary, cognitive perspectives on question asking and explanation provide a theoretical framework for identifying causes for explanation requests, and for determining what kind of information should be provided in explanations. More specifi cally, it appears that two conditions are necessary for explanation requests to occur. First, there is a perceived anomaly in KBS output, which causes comprehension dif ficulties if a user is not able to infer the goal, plan, or problem-solving procedure of KBS. The missing information should also be perceived as important for the user’s action and goal. Second, the user has the appropriate knowledge structure to perceive potential anomalies, and to interpret KBS explanations. Otherwise, KBS explanations may not be useful because they are not needed or cannot be understood and evaluated. These theoretical perspectives suggest that novice–expert differences may influence explanation-seeking behavior.

## Novice–Expert Differences

Problem-solving starts with understanding what the problem entails [38]. The prob lem-solver builds a cognitive representation of the problem. Whereas some of the information needed for this representation is explicitly stated in the problem statement, other information must be inferred. The problem-solver’s prior knowledge and experience interact with information explicitly stated in the problem to form the rep resentation. This is where the ability to access relevant information makes a difference. Experts and novices show substantial differences in the cognitive structures and processes that compose their ability to solve complex problems.

The variations can be characterized on three interrelated dimensions—amount, organization, and accessibility [38]. Amount relates to the number of specific con cepts available to a person. Experts in a given domain are thought to have a greater amount of declarative knowledge (concepts and facts) than novices. Organization refers to how an individual piece of information relates to others. Experts may organize information according to different conceptual categories than novices. Furthermore, an expert’s knowledge includes not only principles, but also an understanding of the conditions of their use. Accessibility is defined according to how easily a concept or a relation can be retrieved from memory. Experts are able to access information more easily and more rapidly than novices. This “automatic accessibility to relevant information helps to ease the bottleneck in attentional resources, freeing them for other processing components that increase performance competence” [38, p. 91].

There is also a difference in problem-solving strategies: Novices tend to analyze problems in terms of surface features, whereas experts are more able to break through the surface and identify common underlying problem structures [3, 7]. Moreover, strategies used by experts are goal-oriented, whereas novices are absorbed in perceiving and evaluating the immediate consequence of their actions. Whereas novices resort to the use of general problem-solving strategies—a highly complex inferencing activity—experts, in contrast, appear to use simpler, domain-specific recognition pro cedures when faced with a problem [1].

It is widely accepted that discourse comprehension improves when a reader has adequate background knowledge to assimilate a text [22]. Domain knowledge is believed to be a critical factor in discourse comprehension, and domain experts construct inferences with relative ease. Not only does domain knowledge make relevant information accessible to cognitive processes, but it also extends one’s processing capabilities. Experts are believed to be able to fill in the missing elements of the problem using domain knowledge and then simply match the configuration with an already stored pattern. In other words, domain expertise allows one’s knowledge to be accessible for use either automatically or with very low cost to the cognitive systems [6].

Furthermore, according to Kolodner [28], experts make use of two different types of memory: semantic and episodic. Domain-specific knowledge is stored in semantic memory, while episodic memory contains heuristics for the effective application of domain knowledge. Experts recognize the applicability of generic procedures to particular situations by identifying the similarities between current situations and previous ones. Novices also make use of semantic memory, although not to the extent of experts. However, novices have not yet developed the heuristics for applying their semantic knowledge to specific situations effectively. Therefore, it is the ability to use heuristics from episodic memory that differentiates experts from novices [28].

Therefore, the level of domain expertise is a key factor determining the use of KBS explanations. On one hand, because of their lack of knowledge and experience, novices should have a greater need for explanations to understand KBS output than experts. (In contrast, experts can recognize the relevance of KBS conclusions, and create their own explanations more easily than novices.) On the other hand, domain experts are expected to request more explanations in anomalous situations, since they are more likely to detect anomalies and inconsistencies in KBS output than novices.

Moreover, whereas experts are able to quickly create a nonarbitrary path for solving a problem, their strategy can be different from that of a KBS. Therefore, reasoning-trace can help explain conclusions, and may affect their acceptance of the conclusions. Because of experts’ ability to quickly recognize the application of generic procedures to particular situations and their goal-oriented problem-solving process, their need for the justification of KBS conclusions may be lower than that of novices.

## Research Method

## Experimental Task

THE EXPERIMENTAL TASK INVOLVED A FINANCIAL ANALYSIS CASE. Subjects were asked to assume the role of a corporate loan officer to evaluate an application for a multimil lion-dollar commercial loan by a hypothetical firm. They were told to use a KBS designed for loan evaluation to assess various aspects of the company’s financial health. Then, based on this assessment, they would decide if the loan should be ap proved, and, if so, the amount. It is a task that occurs infrequently and is dealt with at high organizational levels. A \$50 prize was promised to the top 20 percent of individuals in each experimental condition, based on the quality of their judgment in terms of how close their answers are to a benchmark provided by a panel of domain experts whose expertise was used to develop the KBS.

## Experimental KBS

A simulated KBS was adopted that allowed easier manipulation of explanation provi sion strategies and access to system usage data than commercial or proprietary KBS. To the users it appeared to be a fully functional KBS, but it had no inference ability other than displaying precomposed solutions. It was developed by Dhaliwal [11] with the help of a panel of six senior financial analysts, whose experience ranged from 12 to 23 years. The senior financial analysts were asked to analyze a commercial loan evaluation case—the same one evaluated by the experimental subjects later. Concur rent verbal protocols were collected to determine the types of analysis that the senior financial analysts performed with detailed reasoning processes and explanations. The results became the basis for developing the simulated KBS, named FINALYZER, written in C++ for Windows.

To validate the system, two accounting professors, three doctoral students in accounting/finance, and two junior financial analysts used the KBS. None of them was able to detect that it was not a fully functional KBS (i.e., it was designed to assist in analyzing one particular case only). The system was used in prior research, and was considered highly realistic and useful by the subjects [11]. Subjects also rated very highly the level of expertise displayed by the system, as it compared to the best hu man experts in industry.

FINALYZER performs financial analysis in terms of seven subanalyses, such as liquidity, capital structure, and profitability. It displays three types of screens for each of the subanalyses: (1) an information screen containing an index of domain concepts (financial ratios and procedures), for which explanations can be requested, (2) a data screen of relevant financial ratios calculated from the financial statements of the firm to be evaluated, and (3) conclusion screens presenting outcomes of the “evaluation” by the KBS, in the form of three or four specific conclusions (Figure A1 in Appendix A), where explanations can also be requested for each. The sequence of the screens is shown in Figure 1, which is consistent with the normal procedure of financial analy sis, i.e., calculating financial ratios first and then yielding judgments for making decisions and predictions.

![](/api/attachments/K8FRYBJR/fulltext/images/c5326dd787de66079e5fefda33fe4a2a995e1b86aee4b1a489a9e9902f8451d7.jpg)  
Figure 1. Schematic of the Experimental KBS

FINALYZER provides two categories of explanations: (1) input-related explanations describe the underlying domain knowledge in terms of financial ratios and procedures as input to the problem-solving process of each subanalysis, and (2) outcome-related explanations, including justification (why; see Figure A2 in Appendix A), reasoning-trace (how; see Figure A3), and strategic-explanations (Figure A4) for each conclusion (see Table 1 for definitions and Appendix A for example screen shots).

The experimental system has several unique features. First, whereas the how-ex planation for each conclusion reveals the reasoning-trace, the why-explanation in fact justifies the conclusion by referring to the underlying knowledge. Therefore, the why-explanation is different from the well-known why-explanation in MYCIN, which is generated from reasoning-trace to explain the relevance of input requested from users. Second, there is only one strategic-explanation for each subanalysis, which has three or four detailed conclusions (for example, four in the liquidity subanalysis), whereas there is a unique why- and how-explanation for each conclusion. This paper deals with the outcome-related (in terms of reasoning-trace, justification, and strategy) explanations only, because the input-related explanations are unique to FINALYZER as an experimental feature that is not available in existing KBS. Therefore, the term “explanation” will be used herein to refer to outcome-related explanations only.

## Subjects

This research involved both novices and experienced professionals as subjects. The 28 novice subjects were undergraduate students who were specializing in accounting, and MBA students who either had an accounting background or had taken accounting courses extensively. They all had taken at least one financial analysis course, but lacked work experience. Twenty-five experienced professionals whose work involved financial analysis also participated in this research. Although they were not really

Table 1. Explanations Provided by the Experimental KBS

WHY justifies the importance, and clarifies the implications, of a conclusion that is reached by the system. It makes reference to the underlying domain knowledge including principles, rules, heuristics, or higher level goals.

HOW presents a trace of the reasoning performed and intermediate inferences made to reach a conclusion, including reference to facts used as input to the reasoning process.

STRATEGIC clarifies the overall goal structure used by the system to reach a conclusion, and specifies the manner in which each particular assessment leading to the conclusion fits into the overall plan of assessments that have been performed.

masters in the trade, they possessed professional qualifications beyond the undergraduate degree, being either Certified General Accountant (CGA) or Certified Fi nancial Analyst (CFA). They had on average 9.6 years of post-qualifying work experience.

Only 10 experienced professionals and 10 novices were randomly selected and asked to think aloud in order to keep data analysis at a manageable level. However, computer logs kept track of the detail of user–KBS interaction, including the type and timing of each explanation request for all subjects.

## Data Collection Procedures

Experimental Procedures. The experiment was administered individually to each subject in a lab setting. The following steps were followed:

1. Subjects worked on a tutorial KBS that had the same features as the experi mental KBS, but dealt with a simple problem of consumer credit approval.

2. Subject worked on the financial analysis case without using KBS; the objective of this process was to get them familiar with details of the case, so that when given the KBS later they could focus on the analysis, instead of the basic facts.

3. For the thinking aloud subjects, two simple exercises were given to practice verbalization as suggested by Ericsson and Simon [16]. After practicing verbalizing, subjects were asked to go through again one of the analyses provided by the tutorial KBS while verbalizing. The training on thinking aloud usually took less than ten minutes to complete.

4. Subjects again worked on the financial analysis case, but this time with KBS support.

At each of the above stages, subjects were allowed as much time as they needed. The total time of the experiment ranged between one and a half and two hours.

Thinking Aloud Procedure. A verbal protocol analysis relies on verbal reports to gain information about the course and mechanisms of cognitive processes of the internal states of problem-solvers. The contents of thinking aloud and immediate retro spective reports (vis-à-vis those collected at the end of the experiment) are valid, and the validity and completeness of verbal reports can be enhanced by adopting appropriate methods [16].

The think-aloud instruction was: “Say out loud everything that passes through your mind for each step as you interact with the expert system.” There was also a supplementary instruction: “It does not matter if your sentences are not complete, since you are not explaining to anyone else. Just act as if you are alone in the room speaking to yourself loudly.” These instructions were provided to encourage more thorough protocols, and to discourage explaining subjects’ action, which could interfere with the natural cognitive process [16]. Subjects were also told that if they were silent for more than 10 seconds, they would be reminded to “keep talking.” The instructions were tested on two pilot subjects, and appeared to be understood and followed.

Additional measures were taken to deal with other potential causes of incomplete verbal protocols. First, prior research has shown that in discourse comprehension situations subjects may read frequently, and provide insufficient verbal protocol reports, because it is difficult to read silently and yet think aloud [49]. Therefore, subjects were asked to think aloud and read aloud, according to a procedure suggested by Waern [49]. Second, it is known that think-aloud instructions to subjects reading easy essay text tend to yield little verbalization beyond the reading of the text. The usual prescription to obtain informative think-aloud reports is to break up the continuity of the reading process. In this study, subjects were prompted by the KBS to provide an agreement rating on a scale from 1 to 7 for each conclusion displayed. Thus the continuity of the reading process was broken up in a natural way.

## Data Analysis and Findings

## Data Analysis Procedures

TAPE-RECORDED VERBAL PROTOCOLS of the entire user-KBS interaction were first transcribed, and then segmented as the first step of data analysis. The segmentation was done corresponding to screens of KBS display. Verbal reports were matched against each of the accessed KBS screens and labeled accordingly. Reading aloud of KBS output was differentiated (in italicized letters) from thinking aloud. Nineteen of the 20 subjects produced usable verbal protocols. (The recording quality was too poor for one of the subjects to be transcribed.)

According to Ericsson and Simon [16], where a theory of the cognitive process under investigation has already been postulated, predictions can be made about the information that subjects will attend to and report verbally. According to the cognitive theories reviewed earlier, anomalous situations are instances where explanations are most likely to be sought. Anomalies in this case are considered KBS conclusions or elements of conclusions that cause comprehension difficulties for a user for a variety of reasons—for example, the presence of unfamiliar domain concepts and procedures, results that contradict the user’s own understanding, or un known strategies or methods used by KBS. Reasoning-trace and justification explanations can help resolve some of the anomalies. Whereas reasoning-trace can help users understand the line of reasoning, justification can help them appreciate the implications of KBS conclusions.

Therefore, this verbal protocol analysis was focused on the identification of various types of anomalies perceived by subjects in KBS output and their resolution through explanation use. More specifically, the nature of explanation use was examined primarily based on verbal protocols that reveal users’ intention for requesting explanations and their reaction after reading KBS explanations—for example, surprise, disagreement, or agreement. The analysis also made use of supplementary context information indicative of users’ prior understanding and judgment of the problem. For example, users’ reaction to KBS output was analyzed, with consideration given to their prior comments and remarks on the financial statements and ratios. A key as sumption based on the cognitive effort perspective is that a person will not request an explanation if the person is able to quickly generate one of his or her own when an anomaly in KBS output is encountered.

Major categories of explanation use were identified from the transcribed verbal protocols, and the frequencies were tabulated. Illustrative examples were also identified, since verbal protocol analysis often consists of identifying examples of concepts or processes extracted from the verbalization as evidence of theories that predict them [16].

## Nature of Explanation Use

Three general categories of explanation use emerged from the verbal protocol data, corresponding to responses to varying degrees of perceived anomalies. Typical indicators and some brief examples are provided in Table 2 for each category. First, it is most common that users requested KBS explanations to understand a conclusion if they were unable to quickly generate an explanation of their own. The purpose typically was either to understand the significance (importance) of the conclusion, that is, “Why is this conclusion provided?” or to understand the process of reasoning, that is, “How did the KBS reach the conclusion?” One or more explanations for the conclusion might be requested, resulting in improved understanding of the problem-solving process of the KBS.

The second common scenario of explanation use occurred when users appeared to feel that a conclusion was more or less consistent with their own expectation and were willing to accept it, but not confident enough. In this case, KBS explanations were requested for verification. More specifically, the purpose was likely either for confirming and comparing with one’s own explanation, or for seeking supporting details to bolster one’s own explanation.

Third, the need for KBS explanation also arose when a KBS conclusion was either substantially different from—or opposite to—users’ prior judgment. In this case, KBS explanations were requested for resolving either surprise or contradiction.

A fourth category labeled Others was initially used to place all other explanation use that did not fit into the above three. For example, one user requested explanations for extra information for any negative assessment of the company by the KBS, indicating “If I see something negative, I want to know why or how they came to that conclusion.” However, eventually no major patterns of explanation use could be extracted from the Others category.

Table 2. Typical Explanation Use

<table><tr><td>Categories</td><td>Typical Indicators and Examples</td></tr><tr><td>1. Understanding1a. Understanding the significance or relevance of a conclusion that was unexpected and difficult to justify in terms of its significance (typically involving the why-explanation).</td><td>“Why is it important?” “Why do you say that?” or simply “Why?” in most cases. For example, a user read and paraphrased a KBS conclusion, “... not maintain enough investment to be competitive. Why do you say that? Why is that important?”</td></tr><tr><td>1b. Understanding the reasoning process of a conclusion whose significance was understood, but the reasoning process was not clear and hard to account for (typically involving the how-explanation only).</td><td>“How did they do that?” “Let’s see how they got that conclusion,” or in most cases simply “How?”</td></tr><tr><td>2. Verifying2a. Confirming or comparing with one’s own explanation quickly generated for an unexpected KBS conclusion.</td><td>“I have to agree, let’s see why and how” and “Makes sense” (after reading the conclusion but before reading KBS explanations). “That is what I expected,” “Yes, I noticed,” and “Yes, that’s what I thought” (while reading KBS explanations).</td></tr><tr><td>2b. Seeking supporting details when one could generate one’s own explanation, but needed some important details for support.</td><td>“Yes, it seems to be true. Let’s look at the figures.” “Where do they get the R&amp;D numbers (for this conclusion)? I don’t see any here.” “Let’s take a look at problems of . . .”</td></tr><tr><td>3. Resolving contradictions3a. Resolving surprise, i.e., the user had formed an opinion, thus expecting a different conclusion from KBS.</td><td>“That doesn’t seem to be consistent with anything so far, how?” “Where did you get that (conclusion)? That’s bizarre. How?” “I have no idea what they are talking about, let’s see Why . . . Let’s see How.”</td></tr><tr><td>3b. Resolving disagreement, i.e., the conclusion or some of its elements were contrary to what was expected.</td><td>“I don’t agree with that at all, . . . How did it do that?” “I don’t agree with that one . . .” and, “We have to disagree here. Let’s take a look, why and how.”</td></tr></table>

Verbal protocol reports revealed that, if users strongly agreed with the KBS, they were likely not to request explanations, as was also observed by Dhaliwal [11]. In particular, if users had formed an opinion beforehand (e.g., when reviewing the data), they would almost certainly not request any explanation when they later came across the same assertion. For example, when reviewing data, a subject stated: “The priceearning ratio has increased over time, so in the past five years. . . . So, I guess either the stock is overvalued or something.”

Table 3. Effects of Expertise on the Number of Explanations Requested

<table><tr><td></td><td>Mean Number of Explanation Requests</td><td>Standard Deviation</td><td></td></tr><tr><td>Novices (n = 28)</td><td>17.1</td><td>11.9</td><td>t = 0.33</td></tr><tr><td>Experienced Professionals (n = 25)</td><td>16.1</td><td>13.2</td><td>p = 0.77</td></tr></table>

This happened to be consistent with one of the KBS conclusions. Thus, when she read it later she concurred, without requesting any explanation, with, “Yeah, I agree, because its stock is overvalued. OK. I agree.” Similarly, an experienced professional proclaimed twice that the company should pay off its shareholders’ dividend, before reading the conclusion that proposed the same. When he saw the conclusion, he im mediately agreed strongly, and felt no need to request an explanation.

In summary, consistent with the cognitive effort perspective and theories on explanation and question asking, explanation requests typically arose from a user’s failure to generate a plausible explanation, a difficulty in doing it quickly with little effort, or low confidence in his or her own explanation. No explanation was requested if one’s expectation was confirmed (i.e., there were no perceived anomalies).

## Overall Explanation Requests

Table 3 indicates that there was no significant difference in the number of explanation requests between experienced professionals and novices. Moreover, the mean numbers in Table 3 represent less than 30 percent of the total 57 unique outcome-related explanations for the 25 individual conclusions provided by the experimental KBS, FINALYZER.

## Reasons for Explanation Requests

Contingency table analyses were conducted to compare novices and experienced pro fessionals in their reasons for explanation use. Frequency data were obtained by classifying each explanation request by utilizing a coding scheme similar to that in Table 2. To provide a basis for reliability assessment, the first author and a second coder independently classified the verbal protocols using the same coding scheme. The agreement level between the two coders was 73 percent, based on the three broad categories shown in Table 2 plus the Others category.<sup>1</sup> These four categories were used for the statistical analysis (see Table 4).

Although it might have been more desirable to analyze the data based on the six specific categories shown in Table 2, explanation use could only be reliably separated into four general categories. Furthermore, because of the small sample of verbal pro tocol, the data was too thin to be spread into more specific categories for the contingency table.<sup>2</sup> Therefore, an analysis based on the broader categories was a necessary trade-off between a coarse-grain but more reliable analysis and a fine-grain but less reliable one.

Table 4. Effects of Expertise on the Nature of Explanation Use

<table><tr><td rowspan="2">Frequency</td><td colspan="5">Categories of Explanation Use</td></tr><tr><td>Understanding</td><td>Verifying</td><td>Resolving Contradictions</td><td>Others</td><td>Total</td></tr><tr><td rowspan="2">Novices(n=10)</td><td>84</td><td>26</td><td>11</td><td>13</td><td>134</td></tr><tr><td>62.7%</td><td>19.4%</td><td>8.2%</td><td>9.7%</td><td>100%</td></tr><tr><td rowspan="2">Experienced Professionals(n=9)</td><td>52</td><td>38</td><td>13</td><td>11</td><td>114</td></tr><tr><td>45.6%</td><td>33.3%</td><td>11.4%</td><td>9.6%</td><td>100%</td></tr><tr><td rowspan="2">Total(n=19)</td><td>136</td><td>64</td><td>24</td><td>24</td><td>248</td></tr><tr><td>54.8%</td><td>25.8%</td><td>9.7%</td><td>9.7%</td><td>100%</td></tr><tr><td colspan="6">Pearson&#x27;s chi-square = 8.56 (DF = 3, p = 0.04)</td></tr></table>

Table 4 indicates that the nature of explanation use is significantly different be tween novices and experienced professionals. About 63 percent of explanations requested by novices were for understanding the reasoning process and its significance, whereas only 19 percent were for verification. For experienced professionals, understanding KBS output was also the most common use of explanations (46%), although not as much as for novices (63%). However, a third of the experienced professionals requests (versus 19% for novices) were for verification—that is, comparing and con firming KBS output with their own understanding.

Table 4 also reveals that about 10 percent of the explanations were requested to resolve contradictions. Less than 10 percent of the explanation use was put into the Others category. Table 4 is based on the coding generated by the first coder. As an additional reliability check, the same statistical analysis reported herein was also performed on the coding results by the second coder. The same pattern of significant results was obtained for the data sets of both coders. It appears the categorization based on the level (nature) of anomalies in KBS conclusion is generic and useful.

## Preference for Explanation Types

Detailed data on the request for various types of explanations (Table 5) were captured for each subject by software embedded in the experimental KBS. Novices and experienced professionals had different preferences for explanation types. Novices requested a higher proportion of justification (why) and strategic explanations than experienced professionals. Experienced professionals requested a much higher pro portion of reasoning-trace (how) explanations than novices. It is interesting to note that in terms of the total number of all explanations requested, the how-type was the only case where experienced professionals requested more explanations than novices, even though there were fewer experienced professionals. The strong preference for the reasoning-trace (how) explanation is evident despite the fact that the experimental KBS always displayed justification first. (As shown in Figures A2 to A4, the WHY button is to the left of the HOW button).

Table 5. Effects of Expertise on Preference for Explanation Types

<table><tr><td rowspan="2"></td><td rowspan="2">Count</td><td colspan="4">Explanation Type</td></tr><tr><td>Justification (Why)</td><td>Trace (How)</td><td>Strategy</td><td>Total</td></tr><tr><td rowspan="6">Expertise</td><td rowspan="2">Novices(n=28)</td><td>174</td><td>194</td><td>112</td><td>480</td></tr><tr><td>36.3%</td><td>40.4%</td><td>23.3%</td><td>54.4%</td></tr><tr><td rowspan="2">Experienced professionals(n=25)</td><td>122</td><td>221</td><td>60</td><td>403</td></tr><tr><td>30.3%</td><td>54.8%</td><td>14.9%</td><td>45.6%</td></tr><tr><td rowspan="2">Total(n=53)</td><td>296</td><td>415</td><td>172</td><td>883</td></tr><tr><td>33.5%</td><td>47.0%</td><td>19.5%</td><td>100%</td></tr><tr><td colspan="6">Pearson&#x27;s chi-square = 20.05 (DF = 2, p &lt; 0.001)</td></tr></table>

## A Special Case

Ericsson [15] provided theoretical arguments and empirical evidence that think-aloud instructions to subjects who read essay texts tend to yield little verbalization beyond the reading of the text, while more challenging and complex texts produce much more informative think-aloud reports. In this study, verbal protocols associated with difficult conclusions were expected to be more informative than others, since dealing with anomalies was considered the primary reason for explanation use.

The experimental KBS had one particularly “difficult” conclusion regarding the hypothetical firm’s self-production and R&D:

The increase in manufacturing payroll suggests increased self-production at the company. However, the low level of investment in research and development does not bode well for competing in the rapidly changing high technology product industry.

However, subjects received no information on self-production and R&D expenditure, except for a couple of ratios indicating in general terms that the investment level was low. In fact, the words “self-production” never appeared anywhere else. Therefore, this conclusion could be perceived as being highly anomalous, because it was diffi cult to reach from the information available.

The following example reveals how users tried to comprehend the difficult conclusion by requesting explanations. A subject started with reading, “Increase in manufacture . . . rapidly changing.” “I think, I know the why, I’m going to the how.” He then went on to request and read the how-explanation on the conclusion for the reasoning process “The industry is currently going through a shake-out phase as . . players. Yes. Integration. . . .” Then he went back to read again the difficult part of the conclusion: “So, low level of investment in research, I should go for why,” and read the why-explanation on the conclusion. Once again, he was not completely satisfied, and started to read the conclusion: “Increase in manufacturing payroll, I’m a little puzzled by that. I’ll slightly agree with that. . . .” It appeared that the conclusion came as a complete surprise, which caused the subject to try to get whatever additional information he could to resolve the anomaly.

Table 6. Differences in Requesting Explanations on a Difficult Conclusion

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Number of Subjects</td></tr><tr><td>Novices</td><td>Experienced Professionals</td><td>Overall</td></tr><tr><td rowspan="4">Explanations Requested</td><td rowspan="2">No</td><td>20</td><td>11</td><td>31</td></tr><tr><td>71.4%</td><td>44.0%</td><td>58.5%</td></tr><tr><td rowspan="2">Yes</td><td>8</td><td>14</td><td>22</td></tr><tr><td>28.6%</td><td>56.0%</td><td>41.5%</td></tr><tr><td rowspan="2">Total Number of Subjects</td><td></td><td>28</td><td>25</td><td>53</td></tr><tr><td></td><td>100%</td><td>100%</td><td>100%</td></tr><tr><td colspan="5">Pearson&#x27;s chi-square = 4.09 (DF = 1, p = 0.04)</td></tr></table>

Triggered by many verbal protocols similar to the above example, a contingency table analysis was performed to compare the use of explanations of this particular conclusion between novices and experienced professionals. Table 6 shows that only a small portion of novices (8 out of 28), requested any explanation. Presumably, the rest of them did not perceive anything anomalous. In contrast, over half of the experienced professionals (14 out of 25), requested one or more explanations to deal with the particularly difficult conclusion. The difference between the two groups was significant $( p = 0 . 0 4 )$ . Experienced professionals seemed to be more likely to detect anomalies in KBS reasoning and to request explanations to deal with the anomalies than novices.

## Conclusions and Discussion

THIS RESEARCH HAS TWO MAJOR CONTRIBUTIONS: theoretical perspectives on the nature of explanation use, and empirical findings. This section will discuss these two contributions, highlight their practical implications, and point out the limitations of this research.

## Theoretical Contributions

A rich theory base has been drawn from several perspectives toward a cognitive foundation for understanding explanation use. First, applying the cognitive effort perspective to explanation use, we have argued that users are primarily concerned with getting their tasks completed. They request explanations only when it is deemed necessary and essential for the task completion. Therefore, the explanation facility of KBS may get only limited and selective use. This study confirms that users typically utilize a relatively small amount of available KBS explanations (about 30% in this case), which is consistent with the cognitive effort perspective and earlier empirical findings on explanation use [24]. However, the fact that subjects requested 17 explanations on average for the 25 specific KBS conclusions (sometimes up to three for one conclusion) also suggests that the extent of explanation use can be significant, though selective.

Second, with respect to the trigger of explanation requests, it is established based on cognitive theories of explanation, question asking, and discourse comprehension that it is the perceived anomalies in KBS output—not necessarily real anomalies— that cause users to request explanations. On one hand, users will request explanations only if they perceive that there is something anomalous causing comprehension problems, as confirmed by the verbal protocol data. On the other hand, potential anoma lies may not be detected, because the knowledge structure needed for detecting the anomalies and for interpreting KBS explanations may not be available. Thus, a low level of domain knowledge does not necessarily lead to more explanation requests. The special case involving a particularly difficult KBS conclusion is highly illustrative of this phenomenon. It is in such cases that experienced professionals ask more questions (Table 6) because they have an adequate cognitive foundation to do so. Similarly, the lack of difference in the amount of explanations requested by novices and experienced professionals can be rationalized: Whereas novices have a stronger need for explanations due to the lack of domain expertise, experienced professionals are more likely to identify potential inconsistencies in the KBS output, which is the key to explanation requests.

Finally, users’ task domain expertise can influence their explanation use, because KBS output may appear anomalous for different reasons for novices and experts. The difference in their ability to access relevant knowledge and problem-solving heuristics leads them to use the explanations differently. Experienced professionals are more capable of rapidly creating their own rationalization for unexpected KBS conclusions, thus they are likely to use explanations as a source of confirmation. Conversely, novices, lacking the capability and having fewer problem-solving heuristics, rely on KBS explanations—both justification and trace—for understanding the basic mean ing, implication, and reasoning process of KBS. Together, the above three theoretical perspectives offer new insights into when, why, and how explanations are used. Their practical implications are presented after the discussion of the empirical results.

## Major Empirical Results

To our knowledge, this is the first time that empirical evidence on the nature and extent of explanation use has been collected via a process-tracing method. Major categories of explanation use are identified and accounted for under several cognitive perspectives. Qualitative and quantitative differences have also been found in explanation use between novices and experienced professionals. These results shed some light on why explanations may increase user acceptance of KBS output, as reported by Ye and Johnson [53].

Verbal protocol data show that KBS explanations were used for several purposes, such as understanding, verifying, and resolving contradictions. Both novices and experienced professionals used more explanations for understanding the significance and reasoning process of KBS conclusions than for other purposes. However, experi enced professionals used a higher proportion for verifying their own inference than did novices (Table 4), which is consistent with the theoretical perspectives. Pending confirmation by further studies, a systematic analysis of all potential usage of KBS explanation should help designers direct their effort and evaluate design strategies based on the intended explanation use and targeted user groups.

Experienced professionals requested proportionally more reasoning-trace (how) explanations about KBS conclusions and fewer justification (why) and strategic explanations than novices. The expertise effect on the preference for explanation types can be accounted for with theoretical perspectives on novice–expert differences. Experts’ knowledge makes it easier for them to detect anomalies in KBS output—for example, “holes” of missing reasoning, which can be filled with reasoning-trace explanations. Furthermore, since experts have better developed heuristics to solve a problem, they are more interested than novices in verifying the reasoning process of the KBS (see Table 4) through reasoning-trace explanations, in order to increase their trust in the KBS.

The justification and strategic explanations are potentially more critical for facilitating the comprehension of KBS output, because sense-making is fundamentally goal-driven [41]. Justification explanations in particular help convey the goal hierarchy or central theme of KBS output. The fact that experts’ domain knowledge is better organized makes it easier for them to infer the goal hierarchy. Experts’ knowledge allows them to recognize how a specific conclusion fits into the goal hierarchy for solving the problem more easily than novices, thus they have a lower need for justification explanations. Therefore, justification and strategic explanations are more important for novices, and less for the more experienced users.

## Limitations

To ensure the validity of our results, we chose to use a concurrent thinking aloud procedure, and instructed the subjects specifically to think aloud, rather than “explain aloud” [16]. No probing questions were asked about explanation use during the problem-solving process. Our think-aloud procedure was consistent with the conditions outlined by Ericsson and Simon [16]. Thus it should provide valid and complete verbal reports, although useful information is often buried in a large amount of irrelevant data. However, for some explanation use, there were not enough useful verbal reports—especially from experienced professionals—which might have adversely affected the reliability of the coding. This phenomenon occurred despite the requirement for the subjects to indicate an agreement with KBS output, which is not a common feature of KBS, and thus a potential threat to external validity. Nonetheless, our result is consistent with the literature that experts tend to provide fewer verbal reports than novices because of experts’ highly automatic problem-solving process [16].

In future studies, it would be worth trying other process-tracing methods with questioning (probing) or “explaining aloud,” which would involve a different trade-off between the validity and completeness of the verbal reports. Moreover, one of our results seems to contradict a study by Ye and Johnson [53], which found that justification was preferred to other types of explanations. Additional studies are needed to understand the reasons for the discrepancy.

## Implications and Concluding Remarks

The theoretical perspectives and empirical results have several practical implications. First, the link between perceived anomalies in KBS output and explanation requests is an important issue to explore and to take into consideration in design. This research justifies the importance of explanation with both cognitive theories and empirical evidence. KBS output may appear anomalous to users for one reason or another. If explanations are available, they will be used to address comprehension difficulties. Moreover, if a KBS is designed for a difficult and challenging task, the need for explanations is likely higher.

Second, this research can be useful for determining the content of KBS explanations. In particular, the design rationale and underlying knowledge of KBS should be carefully documented, and made easily available to the users as justification for the output. This is important, even if the users are primarily experienced professionals.

Third, it is important for designers to recognize the different needs of users, because users may have difficulties comprehending KBS output for various reasons. If a KBS is designed to serve users with varying levels of domain expertise, an explanation facility must be implemented to satisfy the diverse needs. For example, our results show that, for novices, justification based on the underlying task domain knowledge is almost equally important as reasoning-trace. However, the integration of additional knowledge just for explanation is not a trivial task. It is more likely to be cost-effective if a KBS is to be used by many novices, but it can be essential if the system is designed primarily for the use of novices.

Lastly, whereas prior studies have indicated that explanations are effective for increasing user acceptance of KBS conclusions [53], our study may be useful for designers to consider implementing features conducive to explanation use. To increase explanation use, it appears that KBS must not only make explanations more understandable, but also help novice users realize their knowledge deficit and provide convenient access to the underlying task knowledge. One possible means, which could be investigated further in future research, is to provide explanations to novices automatically [17] for more effective learning outcomes [33].

In conclusion, this research has examined various cognitive perspectives and verbal protocol data on explanation use. Results can be useful for constructing KBS explanations and for understanding why KBS users need explanations and when, to what extent, and what information should be included in the explanations. Our results have provided direct evidence of the usefulness and importance of explanations to both experienced professionals and novices interacting with an intelligent advice-giving system, and the types of explanations needed by users of diverse backgrounds. The theoretical perspectives and empirical results have important implications for explanation design in practice for both KBS and other intelligent system applications.

Acknowledgments: This research is supported by a research grant from the Natural Sciences and Engineering Research Council of Canada (NSERC).

## NOTES

1. Cohen’s Kappa [9], a commonly used measure of agreement for nominal scales, was also calculated. It is defined as the “proportion of agreement after chance agreement is removed from consideration”(p. 40). When obtained agreement equals chance agreement, Kappa equals zero. The Kappa coefficient was 0.54 (t = 11.8). The strength of agreement between the coders was considered “moderate.”According to Landis and Koch’s benchmark [29], the rela tive strength of agreement is “poor” for Kappa less than 0.20, “fair” between 0.21 and 0.40, “moderate” between 0.41 and 0.60, “substantial” between 0.61 and 0.80, and “almost perfect” between 0.81 and 1.00.

2. Performing analyses on the more specific categories would result in several cells in the contingency tables having expected frequencies smaller than 5, which would likely lead to inaccurate chi-square tests. The reason for this is that the contingency table model assumes a large sample size [52], particularly when the marginal categories are not equally likely.

## REFERENCES

1. Anderson, J.R. Skill acquisition: compilation of weak-method problem solutions. Psy chological Review, 94, 2 (April 1987), 192–210.

2. Beach, L.R., and Mitchell, T.R. A contingency model for the selection of decision strategies. Academy of Management Review, 3, 1 (January 1978), 439–449.

3. Birnberg, J.G., and Shields, M.D. The role of attention and memory in accounting deci sions. Accounting Organizations and Society, 9, 3 & 4 (November 1984), 365–382.

4. Carroll, J.M., and Rosson, M.B. Paradox of the active user. In J.M. Carroll (ed.), Interfacing Thought. Cambridge, MA: MIT Press, 1987, pp. 81–111.

5. Chandrasekaran, B.; Tanner, M.C.; and Josephson, J.R. Explaining control strategies in problem solving. IEEE Expert (Spring 1989), 9–24.

6. Chase, W.G., and Simon, H.A. The mind’s eye in chess. In W.G. Chase (ed.), Visual Information Processing. New York: Academic Press, 1973, pp. 215–281.

7. Chi, M.T.H.; Feltovich, D.J.; and Glaser, R. Acquisition of domain-related information in relation to high and low domain knowledge. Journal of Verbal Learning and Verbal Behavior, 18, 3 (June 1979), 257–274.

8. Clancey, W.J. The epistemology of a rule-based expert system: a framework for explanation. Artificial Intelligence, 20, 3 (May 1983), 215–251.

9. Cohen, J. A coefficient of agreement for nominal scales. Educational and Psychological Measurement, 20, 1 (Spring 1960), 37–46.

10. Davis, R.; Buchanan, B.; and Shortliffe, E. Production rules as a representation for a knowledge-based consultation program. Artificial Intelligence, 8, 1 (February 1977), 15–45.

11. Dhaliwal, J.S. An experimental investigation of the use of explanations provided by knowledge-based systems. Ph.D. dissertation, University of British Columbia, 1993.

12. Dhaliwal, J.S., and Benbasat. The use and effects of knowledge-based system explanations: theoretical foundations and a framework for empirical evaluation. Information System Research, 7, 3 (September 1996), 342–362.

13. Dillon, J.T. Question-answer practices in a dozen fields. Questioning Exchange, 1 (1987), 87–100.

14. Durkin, J. Expert systems: a view of the field. IEEE Expert (April 1996), 56–63.

15. Ericsson, K.A. Concurrent verbal reports on text comprehension: a review. Text, 8, 4 (1988), 295–325.

16. Ericsson, K.A., and Simon, H.A. Protocol Analysis: Verbal Reports as Data. Cambridge, MA: MIT Press, 1993.

17. Everett, A.M. An empirical investigation of the effect of variations in expert system explanation presentation on users’acquisition of expertise and perceptions of the system. Ph.D. dissertation, University of Nebraska, 1994.

18. Flammer, A. Towards a theory of question asking. Psychological Research, 43, 4 (December 1981), 407–420.

19. Ford, K.M.; Coffey, J.W.; Canas, A.; and Turner, C.W. Diagnosis and explanation by a nuclear cardiology expert system. International Journal of Expert Systems, 9, 4 (December 1996), 499–506.

20. Gilbert, N. Explanation and dialogue. The Knowledge Engineering Review, 4, 3 (September 1989), 235–247.

21. Graesser, A.C., and McMahen, C.L. Anomalous information triggers questions when adults solve quantitative problems and comprehend stories. Journal of Educational Psychology, 85, 1 (March 1993), 136–151.

22. Graesser, A.C.; Singer, M.; and Trabasso, T. Constructing inferences during narrative text comprehension. Psychological Review, 101, 3 (July 1994), 371–395.

23. Gregor, S.D. Explanations from knowledge-based systems for human learning and problem solving. Ph.D. dissertation, University of Queensland, Brisbane, 1996.

24. Gregor, S.D., and Benbasat, I. Explanations from intelligent systems: a review of theoretical foundations and empirical work. MIS Quarterly, 2000 (forthcoming).

25. Hayes-Roth, F., and Jacobstein, N. The state of knowledge-based systems. Communications of the ACM, 37, 3 (March 1994), 27–39.

26. Hsu, K.C. The effects of cognitive styles and interface design on expert systems usage: an assessment of knowledge transfer. Ph.D. dissertation, Memphis State University, 1993.

27. Johnson, H., and Johnson, P. Explanation facilities and interactive systems. Proceedings of the 1993 International Workshop on Intelligent User Interfaces. Marina Del Ray, CA: ACM Press, 1993, pp. 159–166.

28. Kolodner, J.L. Towards an understanding of the role of experience in the evolution from novice to expert. International Journal of Man-Machine Studies, 19 (November 1983), 497–518.

29. Landis, J.R., and Koch, G.G. The measurement of observer agreement for categorical data. Biometrics, 33, 3 (March 1977), 159–174

30. Maes, P. Agents that reduce work and information overload. Communications of the ACM, 37, 7 (July 1994), 30–40.

31. Miksch, S.; Cheng, K.; and Hayes-Roth, B. An intelligent system for patient health care. Autonomous Agents 97. Marina Del Ray, CA: ACM Press, 1997, pp. 458–465.

32. Miyake, N., and Norman, D.A. To ask a question, one must know enough to know what is not known. Journal of Verbal Learning and Verbal Behavior, 18, 3 (June 1979), 357–384.

33. Moffitt, K.E. An empirical test of expert system explanation facility effect on incidental learning and decision-making. Ph.D. dissertation, Arizona State University, 1989.

34. Moore, J.D., and Swartout, W.R. Pointing: A way toward explanation dialogue. In Pro ceedings of Eighth National Conference on Artificial Intelligence, vol. 1, 1990, pp. 457–464.

35. Payne, J.W.; Bettman, J.R.; and Johnson, E.J. The Adaptive Decision Maker. Cambridge: Cambridge University Press, 1993.

36. Payne, J.W.; Braunstein, M.L.; and Carroll, J.S. Exploring predecisional behavior: an alternative approach to decision research. Organizational Behavior and Human Performance, 22, 1 (August 1978), 17–44.

37. Pei, B.K.W; Steinbart, P.J.; and Reneau, J.H. The effects of judgment strategy and prompting on using rule-based expert systems for knowledge transfer. Journal of Information Systems, 8, 1 (Spring 1994), 21–42.

38. Rabinowitz, M., and Glaser, R. Cognitive structure and process in highly competent performance. In F.D. Horowitz and M. O’Brien (eds.), The Gifted and Talented: Developmental Perspectives. Washington, DC: APA, 1985, pp. 75–98.

39. Russo, J., and Dosher, B. Strategies for multiattribute binary choice. Journal of Experi mental Psychology: Learning, Memory and Cognition, 9, 4 (October 1983), 676–696.

40. Sabin, D., and Weigel, R. Product configuration frameworks—a survey. IEEE Intelligent Systems (July/August 1998), 42–49.

41. Schank, R.C. Explanation: a first pass. In J.L. Kolodner and C.K. Riesbeck (eds.), Experience, Memory, and Reasoning. Hillsdale, NJ: Erlbaum, 1986, pp. 139–165.

42. Schank, R.C., and Abelson, R.P. Scripts, Plans, Goals and Understanding: An Inquiry into Human Knowledge Structures. Hillsdale, NJ: Erlbaum, 1977.

43. Shortliffe, E.H. Computer-Based Medical Consultations: MYCIN. New York: Elsevier/ North-Holland, 1976.

44. Southwick, R.W. Explaining reasoning: an overview of explanation in knowledge-based systems. Knowledge Engineering Review, 6, 1 (March 1991), 1–19.

45. Stylianou, A.C.; Madey, G.R.; and Smith, R.D. Selection criteria for expert systems shells: a socio-technical framework. Communications of the ACM, 35, 10 (October 1992), 30– 48.

46. Swartout, W.R. XPLAIN: a system for creating and explaining expert consulting programs. Artificial Intelligence, 21, 3 (September 1983), 285–325.

47. Swartout, W.R. Explanation. In S.C. Shapiro and D. Eckroth (eds.), Encyclopedia of Artificial Intelligence, vol. 1. New York: John Wiley & Sons, 1987, pp. 298–300.

48. Todd, P., and Benbasat, I. Process tracing methods in decision support systems research: exploring the black box. MIS Quarterly, 11, 4 (December 1987), 492–512.

49. Waern, Y. Thoughts on text in context: applying the think-aloud method to text processing. Text, 8, 4 (June 1988), 323–350.

50. Wick, M.R., and Slagle, J.R. An explanation facility for today’s expert systems. IEEE Expert (Spring 1989), 26–35.

51. Wick, M.R., and Thompson, W.B. Reconstructive expert system explanation. Artificial Intelligence, 54, 1 & 2 (March 1992), 33–70.

52. Wickens, T.D. Multiway Contingency Tables Analysis for the Social Sciences. Hillsdale, NJ: Erlbaum, 1989.

53. Ye, L.R., and Johnson, P.E. The impact of explanation facilities on user acceptance of expert systems advice. MIS Quarterly, 19, 2 (June 1995), 157–172.

## Appendix A. Illustrations of the Experimental System

SOME SCREEN-SHOTS FROM FINALYZER are provided herein to illustrate its basic features. Due to the space limitation, not all of the different types of explanations are shown.

![](/api/attachments/K8FRYBJR/fulltext/images/6a415fdf10ee2ddcae08ea9e39b4974bbaa78bc387a2be1746b3904c74ab84a3.jpg)  
Figure A1. Example of Conclusion Screens

## WHY EXPLANATION - [FBW/H6-2.1xt]

1] higher sales by credit customers or lower sales bry cash customers

2] higher credit limits or longer payment terms offered to customers, or

![](/api/attachments/K8FRYBJR/fulltext/images/5fe464d4194e339da5773a9911e4778590217c820bb5cda2204d5de4d9ebf7d4.jpg)

3] poor collection practices or unrecorded bad debts.

NEXT SCREEN

Figure A2. Example of Justification Explanations (Why) (For the second conclusion in Figure A1)

![](/api/attachments/K8FRYBJR/fulltext/images/1591e9f015cc6e27a0916bf5649093f9382092d7c950903737489de08648f37e.jpg)  
Figure A3. Example of Reasoning-Trace Explanations (How) (For the first conclusion in Figure A1)

![](/api/attachments/K8FRYBJR/fulltext/images/8ab20787e4f41b6e24341492f0a81ba83c9e0b23e173d1206d4605aad522b286.jpg)  
Figure A4. Example of Outcome-Related Explanations (Strategic) (For the “short-term liquidity conclusions” including the two in Figure A1)
