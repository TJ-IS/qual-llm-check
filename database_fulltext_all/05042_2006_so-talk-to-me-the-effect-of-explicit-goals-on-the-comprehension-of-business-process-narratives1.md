---
otero_id: 5042
otero_key: "GX825Q4K"
title: "So, Talk to Me: The Effect of Explicit Goals on the Comprehension of Business Process Narratives1"
authors: "William L. Kuechler; Vijay Vaishnavi"
year: "2006"
journal: "MIS Quarterly"
doi: "10.2307/25148761"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
So, Talk to Me: The Effect of Explicit Goals on the Comprehension of Business Process Narratives

Author(s): William L. Kuechler and Vijay Vaishnavi

Source: MIS Quarterly, Vol. 30, No. 4 (Dec., 2006), pp. 961-979

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/25148761

Accessed: 25-12-2015 00:10 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# So, TALK TO ME: THE EFFECT OF EXPLICIT GOALS ON THE COMPREHENSION OF BUSINESS PROCESS NARRATIVES $^{1}$

By: William L. Kuechler
Department of Accounting and Information Systems
University of Nevada at Reno
Reno, Nevada 89557-0205
U.S.A.
kuechler@unr.edu

Vijay Vaishnavi
Department of Computer Information Systems
Georgia State University
35 Broad Street, Room 902
Atlanta, GA 30303
U.S.A.
vvaishna@gsu.edu

## Abstract

Unstructured data, most of it text-based and computer-mediated, makes up a rapidly growing majority of the knowledge store of most organizations. Entire classes of information systems—knowledge management systems and enterprise content management systems—have emerged to monitor, manage, and support decision making from this primarily textual data.

IS research has treated text as a unitary variable. However, research from cognitive science strongly suggests that a deeper investigation of how text is comprehended would allow the development of more effective computer-based knowledge and communications systems. Our research extends IS research on the effects of information presentation on decision making by investigating the attributes of text rather than comparing text to other information presentation modes such as graphs or numbers. Our study also contributes to the sparse empirical IS research on problem formulation, the initial phase of decision making.

Informed by research on information presentation, decision making, and narrative comprehension, we designed a series of experiments that demonstrate that the explicit inclusion of goal information for activities in narrative descriptions of problematic business processes increases overall comprehension, decision-making confidence, and short and long term recall. Based on our experimental findings we propose that augmenting text-based IS to elicit and saliently present explicit goal information would significantly enhance the decision support capability of these systems especially for rapid, ad hoc decisions about business process situations.

Keywords: Decision support systems, decision making, human-computer interface, process comprehension

## Introduction

Most of the information on which businesspeople base their sense-making and decision-making is unstructured text (Weick and Browning 1986) and a rapidly increasing percentage of that data is computer mediated. Content management professionals estimate that 85 percent of an organization's knowledge store is in the form of unstructured data, predominantly text files (Robb 2004) and the volume of unstructured textual data is increasing at a greater rate than traditional structured data (White 2003).

Some of the more common business computer systems that integrally depend on text or whose sole function is to disseminate text are

\- E-mail

\- Case-based DSS

• Group decision support systems

\- Project documentation systems including design support systems

\- Knowledge management systems including enterprise portals

• On-line instruction and operation manuals

\- Help systems

In response to the increasing volumes of textual data and the increased understanding of its importance relative to traditional structured data (Peterson 2003), entirely new classes of computer information systems have recently entered the commercial marketplace. The primary function of these systems is to manage and support decision making from unstructured text. Enterprise content management (ECM) systems form the core of these new systems (Rosenblatt 2003); business intelligence systems (Betts 2004) and multiple data mining, monitoring (for legislative compliance), and knowledge management applications draw from the text in the ECM repositories (do Prado et al. 2004; Sullivan 2004). New forms of text-based decision support systems such as lessons learned systems (LLS) continue to be developed and have quickly gained wide acceptance (Weber et al. 2001).

In spite of this flurry of activity in the marketplace, there has been little research on improving the information systems presentation of captured text to support decision making. Not finding any formal study of text management systems, we surveyed the design descriptions of all text handling systems described in KM Magazine's annual product review. $^{2}$ We found that other than implementing some form of lexical analysis for categorization (Perrin and Petry 2003) or combining this technique with conceptual clustering of indices), $^{3}$ the systems reviewed (approximately 150) treat text as a unitary data type, capturing and presenting it with no greater insight than paper filing systems.

To more concretely motivate our research, we present a typical organizational scenario that demonstrates the use of text-based information systems in the problem formulation phase of decision making. In the scenario, John, a sales support engineer, is thrust into a situation that will require him to make decisions that will affect his organization and a client organization. The decision areas include what products to propose and what level of support agreement to suggest. These decisions depend on John first accurately defining the problem situation he faces. His primary information sources are the textual documents provided by his company's customer resource management (CRM) system.

[ringing phone] Hi. This is John.

[Sarah, John's supervisor] Hi John. Look, I've got Randall [sales] in my office and we've been talking about this meeting with First Credit tomorrow. We think we're going to need a bit more technical depth to convince them that our system solves all their problems. I'd like you to go with Randall and talk to their tech folks.

[John, rolling his eyes] Isn't Leslie handling First Credit?

[Sarah] Leslie's in Samoa for three weeks. I think most of the stuff is on line now.

[Sarah's voice, muffled] Randall, all the First Credit history is in the new CRM system, right? Letters, e-mails, RFP? [Sarah's voice, clear] Yeah, just log onto the CRM system, call up First Credit and click on Supporting Documents.

Key and common elements of this and the many similar scenarios which typify our research focus are (1) the sudden appearance of a problem solving situation requiring definition and context; (2) initial detailed information on the problem situation derives from computer mediated narrative descriptions; (3) the emphasis is on comprehending textual information rather than searching for it.

Similar scenarios can easily be envisioned or are set out in the descriptions of text-based support systems that have been developed for virtually all organizational functions including help desks (Roth-Berghofer 2004), market research (Marshall et al. 2004), accounting (Baker et al. 1998), and intellectual property management (legal) (Breitzman and Mogee 2002).

Research in IS on the effects of information presentation on decision making has an extended history. However, all prior IS research on information presentation modes has treated text as a unitary variable; the effects of varying text content and type have not been explored, despite a body of research from IS (Dilla and Stone 1997; Mao and Benbasat 2000) and the cognitive sciences (Lutz and Radvansky 1997; Simon and Hayes 1976) that suggests that problem formulation and thus problem solving and decision quality are strongly influenced by the alteration of specific aspects of text presentation. Our research extends prior information presentation research and suggests a new stream of information presentation research to explore the effects of text presentation on decision making. It also provides detailed design guidance for text-dependent systems. Our primary research question in this area is

RQ: How can the presentation capabilities of text-based information systems be enhanced to improve their decision support capabilities?

In this paper, we describe two experiments that demonstrate that the explicit inclusion of goal information for activities in narrative (a common type of text) descriptions of problematic business processes increases overall comprehension, decision-making confidence, and short and long term recall, thus greatly enhancing decision making.

Although the inclusion of goal information in narrative descriptions of process may seem intuitively beneficial, it is rarely done. First, many writers of process documentation, systems documentation, and even problem-describing narrative such as e-mails do not include goal information in their documents because it has become “transparent” to them. Such information becomes internalized and implicit (Nonaka 1994; Rulke and Zaheer 2001) and is no longer conscious information. In fact, as documented in the literature on knowledge engineering, this information can be the most difficult to extract from the experts on a given process or system (Diederich and Linster 1989; Steels and Lepape 1993). Also, a common school of technical writing stresses conciseness and precision and promotes laconic descriptions of things and actions over intentions (Houp 2002).

As our survey of current text-based commercial product offerings has shown, narrative-based information systems also largely ignore goal information. However, we believe that if strong enough evidence of the benefit of including goal information in narrative-based systems can be demonstrated empirically, then more developers and researchers will accept the challenges to gain the benefits. Based on our experimental findings, we propose that augmenting text-based IS to elicit and saliently present explicit goal information would significantly enhance the decision support capability of these systems.

In the next section of the paper, prior research on the effect of information presentation and text comprehension on decision making is reviewed in order to develop a research model for our study. We then describe our empirical study with reference to the model. Subsequent sections describe the experimental procedures, discuss the results, and conclude with a discussion of the implications of the results for research and practice.

## Prior Related Research

IS research on information presentation (IP) has a lengthy history; the topic was broadly popularized by the Minnesota experiments (Dickson et al. 1977). Information presentation in this context has traditionally referred to the different means of expression and representation of information such as text, graphs, numbers, and diagrams; more recently the term has come to include different access modes such as hypertext or conceptually clustered indices (Cole et al. 2003). Various streams of IP research have emerged through the years, investigating different dependent variables. However, the intent of all IP research is to improve the decision support capability of information systems and the common core assumption behind the research is that the mode of information presentation has significant effects on decision making. Thus the research model shown in Figure 1 is implicit in all IP research.

Early “individual differences” research on IP sought to determine the interaction of information presentation mode with individual decision making style (Dickson et al. 1977; Lusk and Kersnick 1979). This research stream has been muted since 1983 (Huber 1983). Cognitive fit research seeks to match presentation mode to decision task to minimize cognitive load on the decision maker (Dunn and Grabski 2001; Jarvenpaa 1989; Vessey 1991, 1994). Cognitive load is significant because it alters decision strategy (Todd and Benbasat 1991, 2000) and potentially decision quality. Another ongoing IP research stream explores the effect of presentation mode on specific decision tasks such as risk determination (Dilla and Stone 1997) or base-rate decisions (Roy and Lerch 1996). IP effects on comprehension (Lim and Benbasat 2002; Lucas and Neilson 1980) are typical of still another research stream that explores the ability of information systems to present key aspects of information more saliently, thereby improving mental model formation and decision quality. Our research most closely follows this latter stream in that it is focused on comprehension of information in the problem formulation phase of decision making, rather than the problem resolution phase.

![](/api/attachments/GX825Q4K/fulltext/images/5522cef0834bdde91bc25a2e41176dfde2823871edde4d3191130fd9ed9ebde0.jpg)  
Figure 1. General Information Presentation Research Model

During problem resolution, solutions are sought for a well-defined problem. Information system support may be provided by information retrieval and presentation (see the previous paragraph), assistance in operational model construction (Sen and Vinze 1997), or through expert system consultation (Liao 2005). During problem formulation, a problem situation is initially comprehended and defined. It is at this phase of problem solving that a mental model of the problem situation is first constructed and an incorrect model can stall the problem solving process indefinitely. In Sanderson and Murtagh's (1990) research on electronic circuit failure diagnosis, experimental participants who had formed incorrect mental models of the functioning of the circuit were never able to diagnose the problem (within the timeframe of the experiment) while all participants who formed a correct model made accurate diagnoses. Berthon et al. (1998) determined that although it is the least researched of problem solving activities, problem formulation is critical to successful problem solving and decision making. They indicate further that incorrect model formulation is not uncommon in organizational settings and misdirects the entire subsequent decision process.

Problem formulation has been shown to be highly dependent on the mode of problem presentation. Roy and Lerch (1996) and Dilla and Stone (1997), two IS information presentation studies that focused on problem formulation, found that varying problem presentation modes had significant effects on mental model formation. Even within a single mode of problem presentation, text, Simon and Hayes (1976) found that “innocent” changes in language had major effects on problem formulation. IS research on system generated explanations for expert system conclusions has proposed that different form and content for textual explanations significantly influences the understanding of and acceptance of system conclusions (Gregor and Benbasat 1999; Mao and Benbasat 2000).

As is evident from the scenario presented earlier, the focus of our research is to improve IS delivery of text-based information in a type of naturalistic decision making situation (Zsambok and Klein 1997) we term consultative: information is required quickly to define and diagnose a problem occurring outside the decision maker's normal domain (problem formulation). For our research, we have constrained the general model of Figure 1 to correspond to the work scenarios that motivate this research: information delivery is via computer mediated narrative, the environment is that of a typical organizational knowledge worker, and the task is diagnosis and subsequent elaboration of an organizational problem situation for decision making.

Our research model (Figure 2) has been informed by an extensive survey of text comprehension research from the fields of discourse processing (see Gamez and Marrero 2001), cognitive (see Lutz and Radvansky 1997) and educational psychology (see Narvaez et al. 1999), and management and decision science (see Gettys et al. 1987; Weick and Browning 1986). The most salient research used to develop the model is shown in Table 1.

Summarizing that research, a cognitive model, the situation model, is formed when readers seek to understand textual material. A functional view of the situation model is as a mental analogue of a semantic network, linking clauses (facts) presented in the text with prior knowledge to form a coherent, nomothetic web; the new situation presented in the text is made intelligible by the situation model (Zwaan and Radvansky 1998). The strength and coherence of the situation model is affected by reader (attitude), material content (the independent variable for our experiments), and material type. Text is frequently divided into four broad types: persuasion, exposition, literary text, and narrative. Our research is focused on narrative, a type of text that tells a story or describes a situation since it is pervasive in organizational communications. The results of text comprehension research (see Table 1) imply that the situation model could have significant effects on multiple facets of decision making: comprehension, solution count, and recall (the dependent variables for our experiments).

![](/api/attachments/GX825Q4K/fulltext/images/ad6c44a38f7c01569e261cf3e8365462d6552c2880b086ac718ac1dcb7e2b485.jpg)  
Figure 2. Narrative Goal Presentation Research Model

Table 1. Material and Reading Environment Variables Shown to Affect Comprehension

<table><tr><td>Text or Reading Environment Attribute</td><td>Effect on Comprehension</td><td>Reference</td></tr><tr><td>Genre (type) expectations</td><td>Reading time, recall of situational and surface information</td><td>Zwaan 1994</td></tr><tr><td>Concreteness</td><td>Positively affects recall, comprehensibility, and interest</td><td>Sadoski et al. 2000</td></tr><tr><td>Text coherence/ambiguity</td><td>Delay in constructing situation model until ambiguity is resolved</td><td>Mani and Johnson-Laird 1982</td></tr><tr><td>Material type</td><td>Expository texts favor evaluation of items in isolation; narrative favors evaluation of item relationships</td><td>Einstein et al. 1990</td></tr><tr><td>Goals for actors in “story” texts</td><td>Recall interference: uncompleted goals interfere with the recall of goals mentioned earlier in the text</td><td>Lutz and Radvansky 1997; Maglaino and Radvansky 2001</td></tr><tr><td>Causal information in text</td><td>Alters analysis of situations and thus decisions; virtually eliminates “framing effect biases”</td><td>Jou et al. 1996</td></tr><tr><td>Reader goals; reading purpose</td><td>Differential processing resources allocated to construction of the different models, especially text-based versus situation</td><td>Narvaez et al. 1999; Schmalhofer and Glavonov 1986</td></tr></table>

Of the many text presentation aspects suggested for investigation by prior research, the potential for goal information in narratives about process to increase both retention and accuracy of concept formation and diagnosis of problems was especially salient for us. $^{4}$ In our experiments, reader expectations and material type and content have been held constant, with the exception of the treatment—the inclusion or exclusion of goal information (independent variable) for activities in textual scenarios (narratives) of problematic business processes.

Our experiments are directed at some of the significant gaps in prior research. In the course of our extensive review of the IS, cognitive science, and discourse processes literature, we have discovered no studies of the effects of any of the aspects of text presentation on critical business decision quality variables. And, although some prior work has explored the effects of text comprehension on cognitive models, our experiments provide substantially more external validity than any prior work through the use of controls on subject attitude and more complex business process scenarios (see Dougherty et al. 1997; Huber et al. 1997; Jou et al. 1996; Kuhberger and Huber 1998). Task complexity is widely understood to have an effect on decision models and strategies (Payne et al. 1992; Todd and Benbasat 1991, 2000).

## Hypotheses

Experiment 1 investigates the short-term effects of including goal information for activities in an e-mail that describes a business process and a problem that has occurred with the process. With reference to Figure 2, explicit goal information in a narrative has been shown to contribute strongly to forming cognitive linkages between textual clauses (Albrecht and O'Brien 1995). Textually presented facts that are linked by intentional information or other (usually) less effective means have more intrinsic explanatory power and also form more relationships to prior knowledge (van den Broek et al. 2000). This should increase the ability of the reader (the decision maker) to make inferences and should also lead to a more coherent model that is recalled more accurately (Zwaan and Radvansky 1998). The more coherent situation model, which integrates more aspects of the textually presented situation, should decrease uncertainty about the situation and may lead to greater confidence in decisions made about problems occurring with the described process (Goslar et al. 1986). Further, goal information for actions should increase the salience of interactions between process actors and of process state changes leading to increased comprehension and diagnostic ability. Finally, more accurate diagnosis should more concretely and specifically direct actions, decreasing the number of proposed solutions to a problem. Thus the hypotheses for Experiment 1 are

H1a: The inclusion of goal information for activities in a narrative process description will result in better recall of explicitly stated information from the description.

H1b: The inclusion of goal information for activities in a narrative process description will result in increased confidence in decisions and judgments made concerning the process.

H1c: Explicitly stated goals for activities in the process description will result in increased comprehension of the process as indicated by accurate problem diagnosis and solutions to the process problems that are more concrete and coherent.

H1d: Explicitly stated goals for activities in the process description will function as constraints during solution generation resulting in fewer solutions.

Experiment 2 tests the long-term (one week) effects of activity goal information on process narrative comprehension. Long-term recall has a significant effect on the way decisions are actually made in naturalistic situations (Klein 1998). Especially when decision makers are busy and the review is tedious, as for most complex business processes, the decision makers do not review their notes at every sitting, but rely heavily on memory (Simon 1977). Thus, the more accurate the original situation model formed of a process, the better will be the long-term decisions regarding that process. Hypotheses for the experiment, therefore, are

H2a: The inclusion of goal information for activities in a narrative process description will result in better long-term recall of explicitly stated information from the description.

H2b: The inclusion of goal information for activities in a narrative process description will result in increased confidence in recall made concerning the process over the long term.

H2c: Explicitly stated goals for activities in the process description will result in increased long-term comprehension of the process as indicated by accurate problem diagnosis and solutions to the process problems that are more concrete and coherent.

## Experimental Variables and Procedures $^{5}$

## Pilot Study

As an initial assessment of our experimental procedures, we conducted a pilot study in which 15 subjects were given short business process scenarios to read, and were then questioned to determine their understanding, their inferences, their and decision processes. The session was recorded and transcribed, and an analysis of concurrent verbal protocols (Huber et al. 1997; Williamson et al. 2000) gave strong evidence that a detailed situation model was formed during the reading of business scenarios, and that the model was used to answer questions, draw inferences, and form conclusions about the material (Dougherty et al. 1997; Harte et al. 1994; Jou et al. 1996; Pennington and Hastie 1993). The pilot study gave evidence of the effectiveness of many of the specific data collection techniques and instruments used in our experiments.

## Experimental Design for Experiments 1 and 2

The experimental design illustrated in Figure 3 is identical for both experiments. Both utilized a single independent variable with two levels of the factor: the presence or absence of sentences describing goals for activities in a business process description document. The four dependent variables were recall of stated process details, decision confidence in decisions made with respect to solving a problem that was described in the process description document, comprehension of (the ability to make valid inferences about) the process and the problem that was described, and solution count (the number of unique solutions proposed) for the problem described in the process description document. A within-subjects design was chosen to minimize subject differences; a randomly selected, counterbalanced presentation order of documents was used to control for order effects.

## Experiment 1: Immediate Effects

Subjects. A total of 24 senior and graduate students enrolled in elective information systems classes participated in the experiment, 19 of whom were from a 14,000-student state university; the other 5 were from a 24,000-student state university. The average age was 24 years, and 42 percent of the subjects were female. Incentives for involved participation were \$15 and partial credit toward class grade.

Materials. Two different process description documents were required for the within-subjects design, each in two versions: one with and one without treatment sentences describing high-level goals for activities. Goals (or intentions or rationale) describe why a specific activity is performed as it is, and are non-detail prescriptive. For example, not storing inventory on the manufacturing site (just-in-time ordering) in order to keep inventory costs down is an example of an explicitly stated high-level goal for a manufacturing process. In our experiment, the intentional information was deliberately chosen to be widely understood by our subject pool, and this was confirmed in our pilot study, our confirmatory study (described later), and by subject protocols.

The descriptions were presented in the form of printed e-mail messages, identical in format to those used in the pilot study, which consisted of salutations, closings, and step-by-step descriptions of the processes. Enough information was given to infer a reason for the problem. However, this was not made explicit in the narratives. The scenarios were similar in length for each version (approximately 350 words, no goal version versus 440 words, goal version) and identical in number of interactions between actors.

## The other experimental materials were

\- Two tests of 12 true/false and short answer questions for determining prompted recall, one for each narrative scen-

![](/api/attachments/GX825Q4K/fulltext/images/f80d83c7541e2fea37ffd1576b763153c4039d1d2076730f8ab5323d12d763fd.jpg)  
Dependent Variables

Figure 3. Experimental Design

ario. All questions involved information explicitly stated in the narrative.

\- One set of five high-level probes used with both scenarios to determine retention and comprehension. In order of presentation to the subjects, they were (1) describe the original process; (2) describe the problem that occurred; (3) describe what went wrong with the process; (4) describe as many solutions to the problem as you can; and (5) pick the best solution from the ones you have proposed and describe why it is optimum.

\- An instrument similar to that used in Goslar et al. (1986) for measuring confidence in decisions made regarding ill-structured problems. The instrument contained seven questions, each rated on a seven-point Likert scale that measured decision confidence directly along with two factors that covary with decision confidence: willingness to take action on decisions and perceived clarity of decision related information. Some of the questions were included as validity checks as were negatively worded questions (to detect subjects circling all 5's, for example).

Procedure. After brief preparation for the concurrent verbal protocol, subjects were advised that they were to play the role of an analyst from a consulting firm who had been flown in at the last minute to review material generated by a fellow analyst who had fallen ill.

All subject responses were audio recorded (Ericsson and Simon 1993; Harte et al. 1994; Huber et al. 1997). After a single reading, the five free recall probes and the instruments for prompted recall and decision confidence were administered. The second process description narrative was treated identically. Before leaving the session, subjects were scheduled for the follow-up session (Experiment 2: long term effects) one week later.

Data Parsing and Coding. The analysis of concurrent verbal protocols (CVP) (Ericsson and Simon 1993; Williamson et al. 2000) as it has been specifically applied to decision research is detailed in Harte et al. (1994) and Todd and Benbasat (1987). The verbal responses to the probes were transcribed and broken into clauses, defined as any unit that expresses a unified predicate (Berman and Slobin 1994; Trabasso and Magliano 1996). The transcriptions were parsed into clauses, as used in reading comprehension research instead of protocols (Ericsson and Simon 1993) because the intent was to discern idea units (Sadoski et al. 2000) in the transcription rather than to infer thought processes from it.

Measures. There are multiple perspectives on comprehension (Anderson and Krathwohl 2001; Lim and Benbassat 2002; Mayer 1991) that all tend to cluster around the dictionary definition of the word understanding. Tests of comprehension of textual material typically involve measurement of inferences, the extrapolation of the material to new contexts or judgments about meaning and the ability to infer solutions to problems stated in the text (Byrnes 2001; Jou et al. 1996). We use diagnosis and solution score (solution richness) to triangulate on this complex construct.

The ability to remember specific facts or phrases from text is typically termed recall in the text comprehension literature (Anderson and Krathwohl 2001; Zwaan 1994). Recall and comprehension result from distinct cognitive processes and may not be correlated, that is, high recall may be accompanied by minimal understanding (Anderson and Krathwohl 2001; Byrnes 2001).

Decision confidence and short answer scores (prompted recall) were measured with instruments. All other measures were derived from analysis of the concurrent verbal protocol of responses to the five high-level probes. The solution score measure was suggested by an analogous measure in Nissen (2000) for evaluating the utility of business processes, which had been restructured in an experimental setting. The measures and their scoring are described in Table 2. Accuracy of recall and plausibility of inferences served as a manipulation check, assuring that observations were not the result of confusion or misunderstanding.

<table><tr><td colspan="2">Table 2. Experimental Measures</td></tr><tr><td colspan="2">Decision Confidence</td></tr><tr><td>Decision confidence</td><td>Three related factors: willingness to act, recall confidence, and recall clarity measured with a instrument: seven questions, each using a seven point Likert scale.</td></tr><tr><td colspan="2">Comprehension</td></tr><tr><td>Diagnosis:</td><td>The exact reason for the problem that occurred in the process narrative was never stated; thus this is a measure of an inference as to why the problem occurred. Scorings were 0 = no diagnosis, 1 = partial diagnosis, 2 = full, correct diagnosis.</td></tr><tr><td>Solution Score</td><td>Each solution received an integer rating: 0 (inconsistent, unworkably vague, or contradictory to stated facts in the narrative) or 1 (consistent and workable). Scores for all solutions were added to yield the solution score.</td></tr><tr><td colspan="2">Solution Count</td></tr><tr><td>Number of Solutions</td><td>A count of the number of distinct, explicitly stated solutions to the problem given in the narrative.</td></tr><tr><td colspan="2">Recall</td></tr><tr><td>Prompted recall</td><td>Measured with a 12-question short answer test for each process narrative. Scores were converted to the decimal fraction of correct answers (0.0 to 1.0) for the statistics.</td></tr><tr><td>Process Step Scores</td><td>A measure of how well the process was recalled during free recall. Each process was defined as series of nine steps. Each step was defined as (1) a communication (product or information) (2, 3) between two entities (4) occurring in a specified sequence and (5) resulting in a state change. Each step could be scored from 0 to 5 depending on whether and how well the elements of each step were recalled. Raw process step scores for each narrative ranged between 0 and 45; scores were converted to the decimal fraction of correct answers (0.0 to 1.0) for the statistics.</td></tr></table>

The first author coded all parsed transcriptions. Random samples of five subjects (20 percent) were scored by each of two other raters. Inter-rater agreement was measured with Cohen's kappa. After discussions to resolve differences $^{6}$ kappa's were acceptable (Landis and Koch 1977): .76 for process step scores and .86 for diagnosis.

## Experiment 2: Long Term Effects

This experiment tests the long term (one week) effects of the treatment on many of the same decision attributes measured in the first experiment, which tested immediate effects.

Subjects. The same subjects from Experiment 1 participated in this experiment.

Procedure and Materials. Subjects were seated at a PC that was running common e-mail software and were instructed to assume the same consultant roles they had assumed during the prior week's session (for Experiment 1). They were then instructed to read and type a reply to two urgent e-mail requests for information on the two scenarios, goal and no-goal, from the prior week's session. The presentation order of the e-mails was randomly chosen. Subjects were prompted to include as much detail as they could recall and any insights they had formed concerning the scenario and solutions for the problems that had arisen with it and were then presented with the same short-answer quiz used in Experiment 1. The process was repeated for the second e-mail.

Measures: Since in this experiment subjects were not being asked to make decisions about the processes, but rather to recall the solutions they had thought through the prior week, for this session we constructed a recall confidence instrument designed to measure how confident subjects felt in their ability to remember facts and judgments made about the two process descriptions. The same type of validity checks used in the decision confidence instrument were included in this instrument. The typed responses of the subjects to the e-mail requests for information were parsed and coded exactly as the transcriptions of the free recall sessions had been in Experiment 1, and so all other measures were identical to those described for that experiment.

## Results and Discussion

The Shapiro-Wilk test (Mittlehammer 1996) was run on all data sets to confirm that they came from normally distributed populations and that t-tests were appropriate for all continuous variables. Since the data was correlated (measures on the same subjects), paired-t tests were used. Diagnosis and solution score are ordinal measures and so both t-tests and Whitney-Mann U tests were run for these measures due to the ongoing debate on whether t-tests or nonparametrics are appropriate for ordinal measures (Mitchell 1986). In Table 3, p-values for the Whitney-Mann test are shown in parentheses.

ANOVA was used to check for order and instrument effects. Identical analyses were performed for both experiments. No significant order effects were found except for diagnosis for Experiment 1; this required splitting the diagnosis data set into two groups: Scenario-1-first and Scenario-2-first. The results of t-tests on both groups are shown in Table 3. No other order, instrument, or interaction tests were significant.

The direction of all measures was consistent with the experimental hypotheses. Goal information for activities in the process narrative resulted in better recall of process details, greater confidence in solutions generated for the problem situation, and greater comprehension of the process—indicated most meaningfully by greater accuracy of diagnosis of the problem. The improvement in prompted recall scores resulting from the goal information treatment was significant at the .05 level (p = .027); recall improvement was corroborated by the process step scores which measure more detailed unprompted recall (means of .825 versus .735, p = .065).

Diagnosis is an inference and the strongest indicator of the understanding of both the original process and the problem that occurred as indicated by this subject's goal treatment protocol: "The new fashion trend...decided they didn't need the vests and...that created the problem because, umm, the New York folks were using that notification [of vest completion] to order the cloth for the coats." The scenario never explicitly mentions the function(s) of the vest completion notification; however, the subject's extrapolation from stated facts to problem diagnosis is typical of correct responses. The higher diagnosis scores correlate with the improvement in solution scores (concreteness and coherence of solutions: means of 2.25 versus 1.41; p = .002), as would be expected. The fact that decision confidence factors were significantly higher for the goal condition combined with the higher scores for recall and comprehension indicates that subjects not only had a greater understanding of the material, but also were more willing to act on that understanding. For example, contrast one subject's responses to the decision confidence question on taking immediate action. For the goal treatment: "That's all the way to a seven, because they have to fix that quick." For the non-goal treatment: "Well, a four. [pause] That's pretty wishy-washy...make that a five." Considered in total, the results provide significant support for hypotheses H1a, H1b, and H1c.

H1d, the hypothesis that subjects would treat the goal information as a constraint on solutions and thus generate not only better but also fewer solutions was not supported (means of 2.75 versus 2.42, p = .15); goal treatment subjects actually generated slightly more solutions. Research on hypothesis generation and choice (Dougherty et al. 1997; Fisher et al. 1983; Gettys and Fisher 1979; Gettys et al. 1986) shows very robustly that subjects tend to generate very few hypotheses (solutions in our experiment are hypotheses) relative to any situation, even when extensively prompted to generate more. We saw evidence of this in the protocols for several subjects; one subject very cogently responded to our prompt for “Any other solutions?” by saying, “I’m not one to ramble on when I’ve come up with what seems a likely solution.” We had hypothesized that goal information would function as a constraint on the solution space and thus result in fewer solutions proposed. The constraining effect of the goal information was observed in the correctness of the solutions—almost no goal treatment solutions violated constraints implicit in the goals—however it may be that the richer understanding of the problem situation resulting from the goal treatment actually stimulated solution production. The statistics are inconclusive, but the increased problem-solving creativity hinted at by our findings is a significant enough effect to warrant further study.

## Long Term Effects

For Experiment 2 also, both measures of recall (process steps and prompted recall scores) were higher for the process narratives that had included activity goal information (see Table 4). Prompted recall scores were more significant for this experiment (p < .001 versus p = .027), and we propose that this is due to the short time between the reading of the material and the administration of the test in Experiment 1. Short-term memory effects benefitted recall in Experiment 1 but once these had faded, those subjects who had formed a more coherent situation model due to the goal information for activities showed significantly better recall on all long-term measures in Experiment 2. Recall confidence for the two process descriptions was significantly higher for the goal treatment (mean scores of 9.54 versus 7.82; p = .037).

Table 3. Means, Standard Deviations, and p-values for Experiment 1

<table><tr><td rowspan="2">Measure</td><td rowspan="2">p</td><td colspan="2">Goals</td><td colspan="2">No Goals</td></tr><tr><td>Mean</td><td>Std.</td><td>Mean</td><td>Std.</td></tr><tr><td>Decision Confidence</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Willingness to Act</td><td>.002</td><td>11.0</td><td>2.24</td><td>9.50</td><td>2.48</td></tr><tr><td>Recall Clarity</td><td>.060</td><td>8.46</td><td>2.72</td><td>7.08</td><td>3.23</td></tr><tr><td>Recall Confidence</td><td>.015</td><td>4.96</td><td>1.27</td><td>4.01</td><td>1.31</td></tr><tr><td>Comprehension</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Diagnosis (scenario 1 first)</td><td>.036(.004)</td><td>1.154</td><td>.92</td><td>.654</td><td>.94</td></tr><tr><td>Diagnosis (scenario 2 first)</td><td>&lt;.001(.031)</td><td>1.18</td><td>.75</td><td>.09</td><td>.08</td></tr><tr><td>Solution score</td><td>.002(.004)</td><td>2.25</td><td>1.41</td><td>1.31</td><td>.75</td></tr><tr><td>Solution Count</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Number of Solutions</td><td>.15</td><td>2.75</td><td>1.42</td><td>2.42</td><td>1.38</td></tr><tr><td>Recall</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Prompted recall</td><td>.027</td><td>.86</td><td>.15</td><td>.78</td><td>.15</td></tr><tr><td>Process steps</td><td>.065</td><td>.825</td><td>.21</td><td>.735</td><td>.18</td></tr></table>

<table><tr><td colspan="6">Table 4. Means, Standard Deviations, and p-values for Experiment 2</td></tr><tr><td rowspan="2">Measure</td><td rowspan="2">p</td><td colspan="2">Goals</td><td colspan="2">No Goals</td></tr><tr><td>Mean</td><td>Std.</td><td>Mean</td><td>Std.</td></tr><tr><td>Decision Confidence</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Recall Confidence</td><td>.037</td><td>9.54</td><td>2.9</td><td>7.82</td><td>2.64</td></tr><tr><td>Comprehension</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Diagnosis</td><td>&lt; .001(&lt; .001)</td><td>1.167</td><td>.83</td><td>.396</td><td>.76</td></tr><tr><td>Solution score</td><td>.078(.087)</td><td>1.02</td><td>.63</td><td>.71</td><td>.67</td></tr><tr><td>Solution Count</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Number of Solutions</td><td>.11</td><td>1.46</td><td>.66</td><td>1.21</td><td>.78</td></tr><tr><td>Recall</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Prompted recall</td><td>&lt; .001</td><td>.695</td><td>.29</td><td>.44</td><td>.31</td></tr><tr><td>Process steps</td><td>.002</td><td>.746</td><td>.21</td><td>.60</td><td>.27</td></tr></table>

Note that the measures, number of solutions and solution score, have far less variation for Experiment 2 than for Experiment 1 (compare Tables 3, 4). This was due to the tendency discussed earlier for subjects to propose few solutions under any conditions, and once a viable solution had been proposed, even strong prompting rarely resulted in additional contributions (see the discussion above for Experiment 1). For Experiment 2, subjects typically recalled only the solution they felt was best from the prior discussion (average number of solutions recalled = 1.46/1.21). Thus, since few solutions were recalled, and the ones recalled tended to be viable, the number of solutions and solution score measures tended to equalize across treatments in Experiment 2.

The results from Experiment 2 indicate that the inclusion of goal information for process activities in a process description narrative increases the strength of the situation model substantially, and this results in statistically significant long-term effects. The understanding of the process is increased according to two distinct criteria: recall of the explicitly stated facts of the process description, notably the steps of the process, and comprehension of the process as measured by the ability to correctly diagnose problems and propose effective, coherent solutions. Moreover, the treatment resulted in increased confidence that the process material and previously formed insights about it were being recalled correctly. The fact that the correct diagnosis was spontaneously communicated in descriptions of the situation to others much more often for the goal treatment is a meaningful effect. It appears that appropriate treatment of narrative not only allows readers to generate more accurate insights, but also fosters dissemination of this critical information in an organizational context.

## A Confirmatory Study

Following the two experiments, a confirmatory study was performed in order to (1) check the validity of the manipulations, (2) rule out an alternative explanation for the effects found in the main experiments: that the differences in length of the narratives (the goal narratives averaged 90 words longer than the non-goal) were responsible for the effects, and (3) confirm our earlier findings in an experiment with a much higher N (60).

To validate our manipulations, questions were asked for each intentional sentence in each narrative which would be answered correctly only if the information were correctly interpreted by the subjects as goals that constrain the process. For example, one goal sentence (found only in the goal version of the narrative) contained the information “This cloth [from Milan, Italy] is expensive, but it’s necessary to preserve New Man’s quality image.” The probe for the understanding of this goal was the question: “Could New Man save money by using cloth for the coats from Taiwan?” The vast majority of non-goal treatment subjects gave the answer “yes,” while the vast majority of the goal-treatment subjects answered “no,” and explained their reasoning using information from the goal sentence similar to this subject’s response: “They could, but their marketing campaign calls for the Italian cloth to set a quality image.” Overall, 100 percent of all subjects correctly perceived at least two of the goal sentences, 80 percent correctly perceived at least three of four goal sentences, and 70 percent correctly perceived all goal sentences indicating the manipulation was interpreted as intended by the subjects in the main experiments.

To address the possibility that differences in narrative length provide an alternative explanation for our findings, our confirmatory study held the amount of information constant across goal and no-goal versions of narratives and performed several of the tests from the two primary experiments. The results were consistent with our original findings. They are supported as well by the behavioral decision research that has shown that simply including more information about a topic that is not related to a specific decision about that topic results in a poorer decision and in greater confidence in those fallacious decisions (Davis et al. 1994; Oskamp 1965; Paese and Sniezek 1991). We conclude, then, that the difference in length of narratives is not a likely cause for the effects seen in the original study.

Table 5 displays the results of two tests of comprehension from the confirmatory study, which are statistically significant at the p = .01 level and corroborate the results of the main experiments.

## Final Discussion

Table 6 outlines the hypotheses and results for the entire series of studies. This data in combination with the qualitative results from the verbal and written protocols provides substantial support for our theoretical model (Figure 2), and also makes readily apparent that the inclusion of intentional information in narrative has a significant positive effect on business decision making. Since the experiments used narrative descriptions only, the results may not generalize to other text genres such as literary stories or argumentation.

<table><tr><td colspan="6">Table 5. Results of the Confirmatory Study</td></tr><tr><td rowspan="2">Measure</td><td rowspan="2">p</td><td colspan="2">Goals</td><td colspan="2">No Goals</td></tr><tr><td>Mean</td><td>Std.</td><td>Mean</td><td>Std.</td></tr><tr><td>Problem Description</td><td>.010</td><td>.94</td><td>.231</td><td>.80</td><td>.407</td></tr><tr><td>Diagnosis</td><td>.002</td><td>.33</td><td>.476</td><td>.09</td><td>.293</td></tr></table>

Table 6. The Study's Hypotheses and a Summary of the Results of the Experiments

<table><tr><td colspan="2">Hypothesis</td><td>Pilot</td><td>Experiment 1</td><td>Experiment 2</td><td>Confirmatory</td></tr><tr><td>H0a</td><td>Business process descriptions in e-mail format will be interpreted as narrative rather than exposition and will result in strong situations models used for recall and decision making as described in the reading comprehension and non-structured decision literature.</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td></tr><tr><td>H1a, H2a</td><td>The inclusion of goal information for process activities will result in better recall of explicit details from the description.</td><td>Not tested</td><td>Supported (short term)</td><td>Supported (long term)</td><td>Supported (short term)</td></tr><tr><td>H1b,</td><td>The inclusion of goal information for activities in a narrative process description will result in increased confidence in decisions and judgments made concerning the process.</td><td>Not tested</td><td>Supported</td><td>Indirectly supported</td><td>Not tested</td></tr><tr><td>H2b</td><td>The inclusion of goal information for activities in a narrative process description will result in increased confidence in recall of the process over the long term.</td><td>Not tested</td><td>Not tested</td><td>Supported</td><td>Not tested</td></tr><tr><td>H1c, H2c</td><td>Explicitly stated goals for activities in the process description will result in increased comprehension of the process as indicated by accurate problem diagnosis and solutions to the process problems that are more concrete and coherent.</td><td>Not tested</td><td>Supported (short term)</td><td>Supported (long term)</td><td>Supported (short term)</td></tr><tr><td>H1d,</td><td>Explicitly stated goals for activities in the process description will function as constraints during solution generation resulting in fewer solutions.</td><td>Not tested</td><td>Not supported</td><td>Not tested</td><td>Not tested</td></tr></table>

The sample size of 24 is consistent with similar studies in multiple areas (Mackay and Elam 1992). We note also that the within-subjects design yields two measures per subject, and provides much stronger results than the same N in a between-subjects design. Given the triangulation and manipulation checks we gained from protocol analysis, we believe the tradeoff in statistical significance was justified for this essentially exploratory study. The confirmatory study with N = 60 further mitigates sample size concerns.

The use of students in this study does not seem to prevent generalization to a target population since the students fit the target demographics of nonmanagerial knowledge workers quiet well. The average number of years of nonacademic work experience was 5+, and 20 (out of 24) of the subjects were working as knowledge workers more than 15 hours per week during the study. Examination of the protocols for both experiments points out the effectiveness of the role-playing suggestions in generating work-appropriate motivation toward experimental tasks.

Finally, although the study was more realistic than any previous laboratory experiment we have reviewed, many business processes are far more complex than the ones described in our materials. However, with nine departmental interactions each, our experimental process descriptions are as complex as many in-use business processes. Furthermore, complex processes of any sort are frequently decomposed by managers into subprocesses of lesser complexity (Simon 1977). Thus, although additional research focused on more complex processes is an obvious extension of this study, the results are immediately applicable to a subset of in-use work practices.

## Implications for Practice

IS practitioners have a near-term, pragmatic focus; the implications for them from this research derive almost entirely from the strong empirical support given to the benefits of elicitation and inclusion of goal information in narrative-based systems. As discussed in the motivation for our experiments, even though the inclusion of goal information in narrative seems intuitively desirable, it is, with few exceptions, ignored by commercial systems for managing textual information or those that use textual information to support systems development. We propose that our experimental results are strong enough to justify, even for developers who as a group are traditionally concerned with efficiency, the addition of a number of functional modules to narrative-based systems such as those enumerated in the introduction of the paper: (1) a narrative parsing module for automatically determining actors, activities, and stated goals (if any) for the activities; (2) a goal elicitation module for automated assistance in explicating the rationale for actions if left unstated; (3) provision for storage of elicited goal information; (4) the ability to index and retrieve narrative material by goal; (5) mechanisms to link goals to narrative and vise versa and to display narrative(s) by goal or to display goals associated with narrative(s).

The technical aspects of all of these five modules have been previously studied; automatic parsing is well documented in the research literature of education (Landauer et al. 2003), computer science (Datta 1998), and information science (Wong and Yao 1993). Automated goal elicitation has been widely discussed in the expert systems literature (Diederich and Linster 1989), and probably the richest current technology for automated questioning of computer system users can be found in descriptions of medical systems for symptom elicitation (Smith et al. 2000). Given this prior work, initial progress in the suggested directions could be rapid.

Perhaps more interesting are the capabilities gained from these functional modules. The obvious extension from the work described in this paper is the elicitation of goal information and its presentation with retrieved narrative so that the information is made more comprehensible and memorable. However, indexing and retrieval by goal permits types of analysis that are difficult now but which have very significant benefit. Consider the ability of a manager to query a text-based thread (of e-mails) on an international financial project by goal and find that significant effort was being expended on “trying to finalize transactions before the French banks close.” Many problem areas and process bottlenecks are immediately visible by scanning the intentions for actions, as managers who mine customer relationship management databases have found (Larivière and Van den Poel 2004). The same type of query could expose (for example) misallocations of effort in a programming project where many design decisions were linked to the activity goal “to minimize storage” in a project where storage had ceased to be an issue due to hardware changes.

## Implications for Research

The implications of the results of this study for research are broader than for practice to the degree that the results suggest a new information presentation research stream on narrative presentation based on a generalization of our research model. We have redrawn Figure 4 as a generalization of Figure 2 to illustrate some of the possibilities for future research in this area. Our empirical results suggest this is a rich area of study offering substantial benefit to practice and academic understanding alike, as well as one that is virtually untapped.

In addition to goal information (why an action is taken), prior comprehension research implies additional aspects of narrative could significantly affect decision making. They are actors (who), activities (what is being done), temporal information (when), and means-ends (strategic information). Like goal information, these aspects of a problematic situation are often implied rather than explicitly stated by those closest to a situation (the domain experts) and so are missed or ignored by systems consultants. Mode of presentation, for example, flat (extended narrative) or hierarchical (synopsis hyperlinked to supporting detail), is also a potential area of investigation. Also, the cognition phase of Figure 4

![](/api/attachments/GX825Q4K/fulltext/images/afc2a30c1cd2443778ac465f4e7fafa8dd3aac9188c339ec5c58ff749799cfd5.jpg)  
Figure 4. Narrative Presentation Research Model

makes clear that both the problem formulation and problem resolution phases of decision making can potentially be enhanced by content and mode of text presentation and thus each constitutes a separate subject for empirical investigation.

Our study, in and of itself, generalizes to a number of systems of interest to information systems.

1. Commercial information systems that capture narrative information for decision support, such as lessons learned systems (Weber et al. 2001), text mining repositories (Callaghan 2003), business intelligence gathering tools (Betts 2004), and other knowledge management systems. None of these tools currently elicit, store, or use goal information (including, potentially, goal information as an index to that information).

2. Design rationale systems for automatically documenting system development decisions. Several researchers have long suggested benefits from the explicit eliciting of goal information. However, many DR systems do not explicitly capture this information (Potts et al. 1994).

3. Requirements elicitation processes. Many manual requirements elicitation methods currently elicit goals for processes (Browne and Rogich 2001); however, others do not (Anton and Potts 1998), or do so only indirectly. We are aware of no automated requirements elicitation support systems with provision for goal elicitation and storage.

4. Automated workflow management systems. No workflow automation systems, either commercial systems or research prototypes, elicit and include rationale for documenting formal logic-based process descriptions.

IS design researchers (Hevner et al. 2004) would find challenging projects in the design and validation of any of the five narrative-goal subsystems mentioned above in the “Implications for Practice” section. Since the research model for this study (Figure 2) has been substantially validated, experimentalists could derive testable hypotheses from any of the dependent variables in the existing model or from extending that model based on its sources in reading comprehension research, hypothesis and choice research, and qualitative decision making research. Researchers who prefer field work could provide rigorous follow up and extension studies to the industry initiatives exploring beneficial aspects of narrative in organizational communication $^{7}$ and textual analysis of the WWW. $^{8}$

Research into the types of information that are best encoded and communicated as narrative, research into the content of narrative for most effective information transfer, and research into the synergy between narrative information presentations and formal information presentations are obvious extensions of this study. Since narrative descriptions of business processes are the foundation of most IS development as well as the basis for much management decision-making, research in narrative comprehension is applicable to both the development of information systems and the understanding and effects of information systems in organizations.

We plan to extend this study in two directions: (1) to explore the synergistic effects of narrative used in conjunction with formal techniques for programmer-level specification of function (see Kim et al. 2000; Storey et al. 1999), and (2) to explore the synergistic effects of narrative used in conjunction with formal techniques for communication of high-level requirements between multiple stakeholders in large scale system development projects (see Browne et al. 1997; van Lamsweerde 2000; Weiser and Morrison 1998).

## Conclusion

This study has begun to lay an empirical foundation for quantitative improvement of decision support from text-based knowledge capture and management systems. The general model of information presentation research was specialized to an investigation of the effects of a specific aspect of text presentation on decision factors. Our study demonstrated substantial benefit from the presentation of explicit goal information in narratives. The results of the experiments specifically demonstrate the potential value to IS researchers of extending this study to the myriad other aspects of computer mediated text presentation. Given the enormous and growing quantity of computer generated and mediated textual material, research results from this stream translate readily into benefits for practice.

## Acknowledgments

David Kuechler, a doctoral student in the CIS program at Georgia State University, contributed greatly to earlier versions of this paper before his untimely death in November 2002. We wish to thank the editor, the associate editor and the anonymous reviewers for their detailed and constructive comments on earlier versions of the paper. This work is partially supported by NSF Research Grants IIS-9811248 and IIS-9810901, and by a research grant to the second author from the Robinson College of Business, Georgia State University.

## References

Albrecht, J. E., and O'Brien, E. J. "Goal Processing and the Maintenance of Global Coherence," in Sources of Coherence in Reading, R. Lorch and E. O'Brien (eds.), Lawrence Erlbaum, Hillsdale, NJ, 1995, pp. 263-278.

Anderson, L. W., and Krathwohl, D. R. (eds.). A Taxonomy for Learning, Teaching and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives. New York, Longman, 2001.

Anton, A. I., and Potts, C. “The Use of Goals to Surface Requirements for Evolving Systems,” in Proceedings of the 20 $^{th}$ International Conference on Software Engineering, IEEE Computer Society Press, Los Alamitos, CA, 1998, pp. 157-166.

Baker, J., Sircar, S., and Schkade, L. “Complex Document Search for Decision Making,” Information & Management (34:4), 1998, pp. 243-250.

Beach, L. Decision Making in the Workplace: A Unified Perspective, Erlbaum, Mahwah, NJ, 1996.

Berman, R., and Slobin, D. “Appendix II: Glossing and Transcription Conventions,” in Relating Events in Narrative: A Crosslinguistic Developmental Study, R. Berman and D. Slobin (eds.), Erlbaum, Hillsdale, NJ, 1994, pp. 655-664.

Berthon, P., Pitt, L., and Morris, M. “The Impact of Individual and Organizational Factors on Problem Perception: Theory and Empirical Evidence from the Marketing-Technical Dyad,” Journal of Business Research (42:1), 1998, pp. 25-38.

Betts, M. “The Future of Business Intelligence,” Computerworld., June 21, 2004 (available online at http://www.computerworld.com Quicklink # 47332; accessed August 4, 2004).

Blanchette, I., and Dunbar, K. “How Analogies Are Generated: The Roles of Structural and Superficial Similarity,” Memory and Cognition (28:1), 2000, pp. 108-124.

Breitzman, A., and Mogee, M. “The Many Applications of Patent Analysis,” Journal of Information Science (28:3), 2002, pp. 187-205.

Browne, G. J., Ramesh, V., Pitts, M., and Rogich, M. “Representing User Requirements: An Empirical Investigation of Formality in Modeling Tools,” in Proceedings of the Americas Conference on Information Systems, J. N. D. Gupta (ed.), Indianapolis, IN, 1997, pp. 89-91.

Browne, G., and Rogich, M. “An Empirical Investigation of User Requirements Elicitation: Comparing the Effectiveness of Prompting Techniques,” Journal of Management Information Systems (17:4), 2001, pp. 223-249.

Byrnes, J. P. Cognitive Development and Learning in Instructional Contexts ( $2^{nd}$ ed.), Allyn and Bacon, Boston, 2001.

Callaghan, D. “Stratify Tool Searches Unstructured Data,” eWeek (20:30), 2003, p. 22.

Cole, R., Eklund, P., and Stumme, G. “Document Retrieval for E-mail Search and Discovery using Formal Concept Analysis,” Applied Artificial Intelligence (17:3), 2003, pp. 257-280.

Datta, A. “Automating the Discovery of AS-IS Business Process Models: Probabilistic and Algorithmic Approaches,” Information Systems Research (9:3), 1998, pp. 275-301.

Davis, F., Lohse, G., and Kotemann, J. “Harmful Effects of Seemingly Helpful Information of Forcasts or Stock Earnings,” Journal of Economic Psychology (15), 1994, pp. 253-267.

Dickson, G., Senn, J., and Chervany, N. “Research in Management Information Systems: The Minnesota Experiments,” Management Science (23:9), 1977, pp. 913-923.

Diederich, J., and Linster, M. “Knowledge Based Knowledge Elicitation,” in Topics in Expert System Design, G. Guida and C. Tasso (eds), Elsevier Science Publishers, Amsterdam, 1989, pp. 323-350.

Dilla, W., and Stone, D. “Representations as Decision Aids: The Asymmetric Effects of Words and Numbers on Auditors’ Inherent Risk Judgements,” Decision Sciences (28:3), 1997, pp. 709-743.

do Prado, H., de Olivera, J., Ferneda, E., Wives, L., and Silva, E. "Transforming Textual Patterns into Knowledge" in Business Intelligence in the Digital Economy, M. Raisinghani (ed.), Idea Group Publishing, Hershey PA, 2004, pp. 207-227.

Dougherty, M., Gettys, C., and Thomas, R. “The Role of Mental Simulation in Judgements of Likelihood,” Organizational Behavior and Human Decision Processes (70:2), 1997, pp. 135-148.

Dunn, C., and Grabski, S. “An Investigation of Localization as an Element of Cognitive Fit in Accounting Model Representations,” Decision Sciences (32:1), 2001, pp. 55-94.

Einstein, G. O., McDaniel, M., Owen, P., and Cote, N. “Encoding and Recall of Texts: The Importance of Material Appropriate Processing,” Journal of Memory and Language (29), 1990, pp. 556-581.

Ericsson, K., and Simon, H. Protocol Analysis: Verbal Reports as Data, MIT Press, London, 1993.

Fisher, S., Gettys, C., Manning, C., Mehle, T., and Baca, S. "Consistency Checking in Hypothesis Generation," Organizational Behavior and Human Performance (31), 1983, pp. 233-254.

Gamez, E., and Marrero, H. “Interpersonal Motives in Comprehension of Narratives,” Discourse Processes (31:3), 2001, pp. 215-240.

Gettys, C., and S. Fisher, S. “Hypothesis Plausibility and Hypothesis Generation,” Organizational Behavior and Human Performance (24), 1979, pp. 93-110.

Gettys, C. F., Mehle, T., and Fisher, S. “Plausibility Assessments in Hypothesis Generation,” Organizational Behavior and Human Decision Processes (37), 1986, pp. 14-33.

Gettys, C. F., Pliske, R. M., Manning, C., and Casey, J. “An Evaluation of Human Act Generation Performance,” Organizational Behavior and Human Decision Processes (39) 1987, pp. 23-51.

Goslar, M. D., Green, G., and Hughes T. H. “Decision Support Systems: An Empirical Assessment for Decision Making,” Decision Sciences (17:1), Winter 1986, pp. 79-91.

Gregor, S., and Benbasat, I. “Explanations From Intelligent Systems: Theoretical Foundations and Implications for Practice,” MIS Quarterly (23:4), 1999, pp. 497-530.

Harte, J., Westenberg M., and van Someren M. “Process Models of Decision Making,” Acta Psychologica (87), 1994, pp. 95-120.

Hevner, A., March, S., Park, J., and Ram, S. “Design Science in Information Systems Research,” MIS Quarterly (28:1), 2004, pp. 75-105.

Houp, K. W. Reporting Technical Information, Oxford University Press, New York, 2002.

Huber, G. “Cognitive Style as a Basis for MIS and DSS Designs: Much Ado About Nothing,” Management Science (29:5), 1983, pp. 567-579.

Huber, O., Wider, R., and Huber, O. W. “Active Information Search and Complete Information Presentation in Naturalistic Risky Decision Tasks,” Acta Psychologica (95), 1997, pp. 15-29.

Jarvenpaa, S. “The Effect of Task Demands and Graphical Format on Information Processing Strategies,” Management Science (35:3), 1989, pp. 285-303.

Jou, J., Shanteau, J., and Harris, R. “An Information Processing View of Framing Effects: The Role of Causal Schemas in Decision Making,” Memory and Cognition (24:1), 1996, pp. 1-15.

Kahneman, D., and Tversky, A. “The Psychology of Preferences,” Scientific American (246:1), 1982, pp. 160-173.

Kim, J., Hahn, J., and Hanh, H. “How Do We Understand a System with (So) Many Diagrams? Cognitive Integration Process in Diagrammatic Reasoning,” Information Systems Research (11:3), 2000, pp. 284-303.

Klein, G. Sources of Power: How People Make Decisions, MIT Press, Cambridge, MA, 1998.

Klein, G., and Crandall, B. “The Role of Mental Simulation in Problem Solving and Decision Making,” in Local Applications of the Ecological Approach to Human-Machine Systems (Volume 2), P. A. Hancock (ed.), Erlbaum, Hillsdale, NJ, 1995, pp. 1071-1078.

Kuechler, W., Vaishnavi, V., and Kuechler, D. “Supporting Optimization of Business to Business e-Commerce Relationships,” Journal of Decision Support Systems (31), 2001, pp. 363-377.

Kuhberger, A., and Huber, O. “Decision Making with Mission Information: A Verbal Protocol Study,” European Journal of Cognitive Psychology (10:3), 1998, pp. 269-290.

Large, A., Beheshti, J., Breulex, A., and Renaud, A. “Multimedia and Comprehension: A Cognitive Study,” Journal of the American Society for Information Science, 45(7), 1994, pp. 515-528.

Landauer, T. K., Laham, D., and Foltz, P. “Automatic Essay Assessment,” Assessment in Education: Principles, Policy & Practice (10:3), 2003, pp. 295-309.

Landis, J., and Koch, G. "The Measurement of Observer Agreement for Categorical Data," Biometrics (33), 1977, pp. 159-174.

Larivière, B., and Van den Poel, D. “Investigating the Role of Product Features in Preventing Customer Churn, by Using Survival Analysis and Choice Modeling: The Case of Financial Services,” Expert Systems with Applications (27:2), 2004, pp. 277-286.

Liao, S. “Expert System Methodologies and Applications—A Decade Review from 1995 to 2004,” Expert Systems with Applications (28:1), 2005, pp. 93-103.

Lim, K. H., and Benbasat, I. “The Influence of Multimedia on Improving the Comprehension of Organizational Information,” Journal of Management Information Systems (19:1), 2002, pp. 99-127.

Lucas, H. C., and Neilson, R. “The Impact of the Mode of Information Presentation on Learning and Performance,” Management Science (26:10), 1980, pp. 982-993.

Lusk, E., and Kersnick, M. “The Effect of Cognitive Style and Report Format on Task Performance: The MIS Design Consequences,” Management Science (25:8), 1979, pp. 787-798.

Lutz, M., and Radvansky, G. A. “The Fate of Completed Goal Information in Narrative Comprehension,” Journal of Memory and Language (36), 1997, pp. 293-310.

Mackay, J., and Elam, J. “A Comparative Study of How Experts and Novices Use a Decision Aid to Solve Problems in Complex Knowledge Domains,” Information Systems Research (3:2), 1992, pp. 150-172.

Magliano, J., and Radvansky, G. “Goal Coordination in Narrative Comprehension,” Psychonomic Bulletin and Review (8:2), 2001, pp. 372-376.

Mani, K., and Johnson-Laird, P. “The Mental Representation of Spatial Descriptions,” Memory and Cognition (10), 1982, pp. 181-187.

Mao, J., and Benbasat, I. “The Use of Explanations in Knowledge-Based Systems: Cognitive Perspectives and a Process-Tracing Analysis,” Journal of Management Information Systems (17:2), 2000, pp. 153-179.

Marshall, B., McDonald, D., Chen, H., and Chung, W. "EBizPort: Collecting and Analyzing Business Intelligence Information," Journal of the American Society for Information Science and Technology (55:10), 2004, pp. 873-891.

Mayer, R. E. Thinking, Problem Solving, Cognition, W. H. Freedman and Company, New York, 1991.

McCloy, R., and Byrne, R. “Counterfactual Thinking About Controllable Events,” Memory and Cognition $_{1}$ (28:6), 2000, pp. 1071-1078.

Mitchell, J. “Measurement Scales and Statistics: A Clash of Paradigms,” Psychological Bulletin (100) 1986, pp. 398-407.

Mittelhammer, R. Mathematical Statistics for Economics and Business, Springer-Verlag, New York, 1996, pp. 662-663.

Narvaez, D., van den Broek, P., and Ruiz, A. “The Influence of Reading Purpose on Inference Generation and Comprehension in Reading,” Journal of Educational Psychology (91:3), 1999, pp. 488-496.

Nissen, M. E. “An Experiment to Assess the Performance of a Redesign Knowledge System,” Journal of Management Information Systems (17:3), Winter 2000/2001, pp. 25-43

Nonaka, I. “A Dynamic Theory of Organizational Knowledge Creation,” Organization Science (5:1), 1994, pp. 14-37.

Oskamp, S. “Overconfidence in Case-Study Judgments” Journal of Consulting Psychology (29), 1965, pp. 261-265.

Paese, P., and Sniezek, J. “Influences on the Appropriateness of Confidence in Judgment: Practice, Effort, Information and Decision-Making,” Organizational Behavior and Human Decision Processes (48), 1991, pp. 261-265.

Payne, J., Bettman, J., and Johnson, E. “Behavioral Decision Research: A Constructive Processing Perspective,” Annual Review of Psychology (43), 1992, pp. 87-131.

Pennington, N., and Hastie, R. “Reasoning in Explanation-Based Decision Making,” Cognition (49), 1993, pp. 123-163.

Perrin, P., and Petry, F. “Extraction and Representation of Contextual Information for Knowledge Discovery in Texts,” Information Sciences (151), 2003, pp 125-152.

Peterson, T. “Digging Into Documents,” Computerworld (37:51), 2003, p. 28.

Potts, C., Takahashi, K., and Anton, A. “Inquiry-Based Requirements Analysis,” IEEE Software (11:2), March 1994, pp. 21-32.

Robb, D. “Text Mining Tools Take on Unstructured Data,” Computerworld, June 21, 2004 (available online at www.computerworld.com; Quicklink # 47385).

Rosenblatt, B. “Enterprise Content Integration: A Progress Report,” The Seybold Report (3:10), 2003 pp. 9-14 (available online at http://www.seyboldreports.com/; last accessed August 5, 2004).

Roth-Berghofer, T. "Learning from HOMER, a Case-Based Help Desk Support System," Advances in Learning Software Organizations, Proceedings Lecture Notes in Computer Science 3096, Springer-Verlag. Berlin, 2004, pp. 88-97.

Roy, M., and Lerch, J. “Overcoming Ineffectual Mental Representations in Base-Rate Problems,” Information Systems Research (7:2), 1996, pp. 233-247.

Rulke, D. L., and Zaheer, S. “Transitive Knowledge in Complex Organizations,” in Organizational Cognition: Computation and Interpretation, T. Lant and Z. Shapira (eds.), Earlbaum, Mahwah, NJ, 2001, pp. 80-90.

Sadoski, M., Gotez, E., and Rodriguez, M. “Engaging Texts: Effects of Concreteness on Comprehensibility, Interest and Recall in Four Text Types,” Journal of Educational Psychology (92:1), 2000, pp. 85-95.

Sanderson, P. M., and Murtagh, J. M. "Predicting Fault Diagnosis Performance: Why Are Some Bugs Hard to Find?," IEEE Transactions on Systems, Man and Cybernetics (20:1), 1990, pp. 274-283.

Schank, R., and Abelson, R. Scripts, Plans, Goals and Understanding; An Inquiry into Human Knowledge Structures, Erlbaum, Hillsdale, NJ, 1977.

Schmalhofer, F., and Glavanov, D. “Three Components of Understanding a Programmer’s Manual: Verbatim, Propositional and Situational Representations,” Journal of Memory and Language (25), 1986, pp. 279-294.

Sen, A., and Vinze, A. “Understanding the Complexity of the Model Formulation Process: A Protocol Analysis Approach,” Decision Sciences (28:2), 1997, pp. 443-473.

Simon, H. Administrative Behavior: A Study of Decision-Making Processes in Administrative Organizations, Free Press, New York, 1977.

Simon, H., and Hayes, J. “The Understanding Process: Problem Isomorphs,” Cognitive Psychology (8), 1976, pp. 165-190.

Smith, H. R., Ashton, R. E., and Brooks, G. “Initial Use of a Computer System for Assisting Dermatological Diagnosis in General Practice,” Medical Informatics & the Internet in Medicine (25:2), 2000, pp 103-109.

Steels, L., and Lepape. B. “Knowledge Engineering in ESPRIT,” IEEE Expert, August 1993, pp. 5-9.

Storey, M., Fracchia, F., and Muller, H. "Cognitive Design Elements to Support the Construction of a Mental Model during

Software Exploration," Journal of Systems and Software (44), 1999, pp. 171-185.

Sullivan, D. “Text Mining in Business Intelligence,” in Business Intelligence in the Digital Economy, M. Raisinghani (ed.), Hershey, PA, Idea Group Publishing, 2004, pp. 98-110.

Todd, P., and Benbasat, I. “An Experimental Investigation of the Impact of Computer Based Decision Aids on Decision Making Strategies,” Information Systems Research (2:2), 1991, pp. 87-115.

Todd, P., and I. Benbasat “Inducing Compensatory Information Processing through Decision Aids that Facilitate Effort Reduction: An Experimental Assessment,” Journal of Behavioral Decision Making (13), 2000, pp. 91-106.

Todd, P., and Benbasat, I. “Process Tracing Methods in Decision Support Systems Research: Exploring the Black Box,” MIS Quarterly (11:4), December 1987, pp. 493-514.

Trabasso, T., and Magliano, J. P. “Conscious Understanding During Comprehension,” Discourse Processes (21), 1996, pp. 255-287.

Trabasso, T. and Nickels, M. "The development of goal plans of action in the narration of a picture story." Discourse Processes (15), 1992, pp. 249-275.

van den Broek, P., Linze, B, Fletcher, C., and Marsolek, C. “The Role of Causal Discourse Structure in Narrative Writing,” Memory and Cognition (28:5), 2000, pp. 711-721.

van Lamsweerde, A. “Requirements Engineering in the Year 00: A Research Perspective,” in Proceedings of the 22 $^{nd}$ International Conference on Software Engineering, ACM Press, New York, 2000, pp. 5-19.

Vessey, I. “Cognitive Fit: A Theory-Based Analysis of the Graphs Versus Tables Literature,” Decision Sciences (22:1), 1991, pp. 219-241.

Vessey, I. “The Effect of Information Presentation on Decision Making: A Cost-Benefit Analysis,” Information and Management (27), 1994, pp. 103-119.

Weber, R., Aha, D, and Becerra-Fernandez, I. “Intelligent Lessons Learned Systems,” Expert Systems with Applications (20:1), 2001, pp. 17-34.

Weick, K. E., and Browning, L. “Arguments and Narration in Organizational Communication,” Journal of Management (12), 1986, pp. 243-259.

Weiser, M., and Morrison, J. “Project Memory: Information Management for Project Teams,” Journal of Management Information Systems (14), 1998, pp. 149-166.

Williamson, J., Ranyard, R., and Cuthbert, L. "A Conversation-Based Process Tracing Method for Use with Naturalistic Decisions: An Evaluation Study," British Journal of Psychology (91), 2000, pp. 203-221.

White, M. “Information Overlook,” EContent (26:7), 2003, p. 31.

Wong, S., and Yao, Y. “A Probabilistic Method for Computing Term-by-Term Relationships,” Journal of the American Society for Information Science (44:8), 1993, pp. 431-439.

Zsambok, C., and Klein, G. (eds.). Naturalistic Decision Making, Erlbaum, Mahwah, NJ, 1997.

Zwaan, R. A. “Effect of Genre Expectations on Text Comprehension,” Journal of Experimental Psychology (20:4), 1994, pp. 920-933.

Zwaan, R. A., and Radvansky, G. A. “Situation Models in Language Comprehension and Memory,” Psychological Bulletin (123), 1998, pp. 162-185.

## About the Authors

William L. Kuechler is an associate professor of Information Systems at the University of Nevada at Reno. He holds a BS in Electrical Engineering from Drexel University. Following a career in business software systems development, he received a Ph.D. in Computer Information Systems from Georgia State University. His research interests include interorganizational workflow and coordination, and the cognitive bases of information systems effectiveness and information systems development methods. He has published in IEEE Transactions on Knowledge and Data Engineering, Decision Support Systems, Information Technology and Management, IEEE Transactions on Professional Communications, Information and Management, Decision Sciences Journal of Innovative Education, the proceedings of WITS, HICSS, and other international conferences and journals. Dr. Kuechler is a member of IEEE, and a member of the ACM.

Vijay K. Vaishnavi is Board of Advisors Professor of Computer Information Systems at Robinson College of Business, Georgia State University. He holds a PhD from Indian Institute of Technology, Kanpur, and has conducted postdoctoral work at McMaster University, Canada. His research covers several areas including process knowledge management, semantic interoperability and information integration, virtual communities and directory services, interorganizational coordination, and object modeling and design. He has authored numerous research papers in these and related areas. The National Science Foundation and private organizations including IBM, Nortel, and AT&T have supported his research. His papers have appeared in IEEE Transactions on Software Engineering, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Computers, SIAM Journal on Computing, Journal of Algorithms, and several other major international journals and conference proceedings. Dr. Vaishnavi is an IEEE Fellow, a member of the IEEE Computer Society, a member of the ACM, and a member of the AIS.
