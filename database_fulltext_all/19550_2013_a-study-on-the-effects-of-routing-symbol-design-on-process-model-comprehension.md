---
otero_id: 19550
otero_key: "MG6V5BSA"
title: "A study on the effects of routing symbol design on process model comprehension"
authors: "Kathrin Figl; Jan Recker; Jan Mendling"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.037"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A study on the effects of routing symbol design on process model comprehension Kathrin Figl <sup>a,</sup>⁎, Jan Recker <sup>b</sup>, Jan Mendling <sup>c</sup>

<sup>a</sup> Institute for Information Systems & New Media, UZAII, Augasse 2–6, A-1090, Vienna, Austria

<sup>b</sup> Queensland University of Technology, Information Systems School, 2 George Street, Brisbane QLD 4000, Australia

<sup>c</sup> Institute for Information Business, WU, Vienna University of Economics and Business, UZAII, Augasse 2–6, A-1090, Vienna, Austria

## a r t i c l e i n f o

Article history: Received 30 November 2011 Received in revised form 23 May 2012 Accepted 28 October 2012 Available online 2 November 2012

Keywords: Process modeling Notational design Routing symbols Comprehension Cognitive effectiveness

## a b s t r a c t

Process modeling grammars are used to create models of business processes. In this paper, we discuss how different routing symbol designs affect an individual's ability to comprehend process models. We conduct an experiment with 154 students to ascertain which visual design principles in<sup>fl</sup>uence process model comprehension. Our <sup>fi</sup>ndings suggest that design principles related to perceptual discriminability and pop out improve comprehension accuracy. Furthermore, semantic transparency and aesthetic design of symbols lower the perceived dif<sup>fi</sup>culty of comprehension. Our results inform important principles about notational design of process modeling grammars and the effective use of process modeling in practice.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Process models have been recognized as an effective means for documenting and communicating business processes, especially as a means for helping to discuss different viewpoints of stakeholders in projects such as the re-design of business processes [61] or the analysis and design of process-aware information systems [45]. Indications that process models indeed make a solid contribution in this area are, for instance, provided through a study of a large number of redesign projects [26].

Process models are created using process modeling grammars — sets of graphical symbols and rules describing how to connect the graphical symbols [78]. These symbols express relevant aspects of business processes, such as the tasks that have to be performed, the actors that are involved in the execution of tasks, relevant data, and, notably, the control flow logic that describes the logical and temporal order in which tasks are to be performed. In essence, the control <sup>fl</sup>ow logic of a business process de<sup>fi</sup>nes those points in the process where parallel or alternative paths might be taken, or where such paths merge. Such routing points characterize the convergence or divergence of process <sup>fl</sup>ows.

In process modeling grammars, convergence or divergence semantics are typically expressed through grammatical symbols named “Gateways”, “Connectors, or “Splits” and “Joins” [e.g., 62,74]. These routing symbols have been subjected to much academic debate. For instance, some scholars have argued that these symbols are ill-de<sup>fi</sup>ned from a formal perspective [e.g., 74]. They have also been found to be a key reason for modeling errors such as violation of deadlock and synchronization rules [24], and further argued to lead to understandability problems with practi tioners [35].

While all available process modeling grammars support the expression of convergence or divergence semantics in a business process, they utilize different visual symbols for doing so. This difference is of crucial importance for the quality of a grammar. In other domains, it has been found that the form of visual information representation can have a signi<sup>fi</sup>cant impact on the ef<sup>fi</sup>ciency of information search, explicitness of information, and problem solving [28], the comprehension and recall of graphical models [11,41] and even perceived usability [67].

Our objective in writing this paper, therefore, is to develop insights about the role of routing symbol design in process modeling grammars. We study how model users understand models created with different visual routing symbol designs by drawing on a theory of effective visual notations [39]. We examine four principles of routing symbol design (perceptual discriminability, pop out, semantic transparency and aesthetics) that should lead to improved process model comprehension. We then present an experiment that tests the impact of the four principles of routing symbol design on process model comprehension in terms of accuracy, ef<sup>fi</sup>ciency and perceived dif<sup>fi</sup>culty. The results demonstrate that the symbol design principles affect comprehension accuracy and dif<sup>fi</sup>culty in different ways. Comprehension ef<sup>fi</sup>ciency is not affected by symbol design.

We proceed as follows. First, we review the literature on factors that in<sup>fl</sup>uence the cognitive load of process model comprehension tasks. We then discuss relevant theoretical considerations pertaining to the visual design of routing symbols in process models and identify four relevant design principles. Next we describe our research model and the experimental design of the study. We then present our data analysis and results. After that, we discuss the results and limitations. We conclude by summarizing the substantive as well as methodological contributions of this research.

## 2. Theoretical background

## 2.1. Cognitive load in comprehending control flow logic in process models

The division of labor in companies poses a considerable challenge to analyzing business processes in a department-spanning manner. Process models have been suggested as a means of abstraction for fostering understanding, transparency and communication of such complex processes. Even though models reduce business processes to their essential components, the creation and understanding of process models still requires high cognitive effort in itself due to the limited information processing capabilities of the human brain [76].

In light of this limitation, the key design principle for process models is to support rather than demand higher-level reasoning processes. This can, for instance, be achieved by conveying visual cues to the next logical step in reasoning about a process-related problem, or by representing process information (e.g., tasks to be performed) in the context of adjacent locations (e.g., in the context of the routing symbols that describe important business rules pertinent to the execution of the task).

Fig. 1 depicts a process model speci<sup>fi</sup>ed in the BPMN grammar [44] to illustrate how visual cueing is typically implemented in process modeling grammars. The model illustrates an E-mail voting process, based on the example given in [43]. The process consists of several activities that are executed according to a pre-de<sup>fi</sup>ned order to reach the speci<sup>fi</sup>c process goal (to resolve an issue). Fig. 1 shows that in this order, several divergence and convergence decisions are made, all represented by different types of gateways, in this case using a diamond shape symbol. Modeling “either/or” choices is done via so-called XOR-Split Gateways (e.g. “assess reasons for not voting” or skip this activity). After splitting control <sup>fl</sup>ow, it may be required to merge it later in the process. Exclusive choices can also be used to model repetition (loop with “election deadline has not yet passed”). Modeling concurrent activities is done via so-called AND-gateways (e.g. “review status of discussion” and “moderate E-mail discussion”).

As the example shows, the diamond-shaped BPMN gateway symbols are intended to support the end users' interpretation and reasoning about the control <sup>fl</sup>ow logic of the process. While this reasoning process is fundamental to understanding the process, the body of literature on error analysis of process models suggests the existence of systematic reasoning fallacies concerning routing symbols [35]. We speculate that this may be traced back to systematic fallacies (so called ‘illusory inferences’) stemming from the visual design of the model or of the underlying process. These may occur when internally constructing or interpreting mental models on the basis of modeling-level connectives (like conjunctions, inclusive, or exclusive disjunctions) [22]. Concerning the example in Fig. 1, a variety of such cognitive errors could occur.

Models readers could, for instance, misinterpret the AND-gateway and think both concurrent activities have to start at the same point of time, or they could confuse XOR and AND gateways if they <sup>fi</sup>nd these gateway symbols dif<sup>fi</sup>cult to discriminate perceptually.

Cognitive errors in reasoning about a process model relate to the cognitive load associated with the reasoning task. Cognitive load describes how much of the human working memory is used in learning and knowledge acquisition tasks [69]. Its importance stems from its limitations: The human working memory is the main bottleneck for cognitive tasks as its capacity is restricted to only 7+/−2 units of information at any point in time [38]. Recent literature estimates working memory capacity even lower to 3–4 elements [12]. The cognitive load of a task rises if a user has to pay attention to high amounts of relevant units of information, which in turn burdens or even overloads his/her working memory, and consequently impairs problem solving ability, learning and knowledge acquisition [69]. A variety of prior studies in the area of conceptual modeling have demonstrated that a reduction of cognitive load can lead to improvements in objective measures like comprehension [19] as well as in subjective perceptions on ease of understanding [31].

Cognitive load theory distinguishes intrinsic and extraneous cognitive load. Intrinsic cognitive load is determined by the complexity of information, i.e., the amount of elements, and their relations and interactions. In the process domain, intrinsic load pertains to the complexity of the modeled process, and thus beyond the control of the process analyst modeling a process. In contrast to that, extraneous cognitive load is determined by the way information is represented [25]. Even for exactly the same problem or task, the relative dif<sup>fi</sup>culty may vary depending on different problem representations [27]. Therefore, extraneous load pertains to the way a process is modeled and is thus subject to the design choices made when describing a process in a model.

Modeling design choices especially relate to notational aspects — the choice of different visual symbols for describing a process in the model. Precisely, the modi<sup>fi</sup>cations may relate to the formal rules of a modeling grammar (its primary notation) or the way a speci<sup>fi</sup>c model is visualized (its secondary notation) [50]. While the primary notation is normally prescribed by the speci<sup>fi</sup>cation of a modeling grammar, it has been shown that secondary notation in<sup>fl</sup>uences process model comprehension, for instance, in terms of modularity [60], the grammatical style of text labels [36], or color highlighting [58]. These studies suggest that secondary notation is an important element in determining the extraneous cognitive load in understanding process models. Still, the research to date has focused on the secondary notation of models as a whole as opposed to the secondary notation of speci<sup>fi</sup>c model elements — such as routing symbols, which is the focus of our work in this paper.

## 2.2. Effective visual design of notational symbols

To discuss the secondary notation of routing symbols in process models, we turn to a theory of effective visual notations proposed by

![](/api/attachments/MG6V5BSA/fulltext/images/bc89c57bd1c8710099237df09c8d5ae82a2bd1558b2dbcb0c3e8c3072b898061.jpg)  
Fig. 1. Example for business process control <sup>fl</sup>ow logic (in BPMN).

Moody [39]. He suggests a set of principles for the visual design of notations used in information systems analysis and design.

Moody [39] uses the term “symbol set” as a synonym for the visual vocabulary of a modeling grammar. It compromises 1D, 2D and 3D graphic elements, such as example lines, areas and spatial relationships. For example, for depicting the routing behavior in business processes, process modeling grammars contain symbols made up of abstract graphics such as circles and diamond shapes.

In the following we will discuss the criteria which are relevant for discussing symbols and their demand of cognitive load. We build on the concepts from Moody's theory of effective notation design [39] and integrate it with an established framework on symbol characteristics [33].

## 2.3. Perceptual discriminability and pop out

Moody's theory [39] stipulates that notations of modeling grammars that fully exploit the range of visual variables (spatial dimensions like horizontal and vertical, as well as shape, size, color, brightness, orientation, and texture) have higher visual expressiveness. This proposition is based on the principles of perceptual discriminability and pop out.

Perceptual discriminability is de<sup>fi</sup>ned as “the ease and accuracy with which graphical symbols can be differentiated from each other” [39]. It concerns the (dis-) similarity of shapes and connecting lines used in process models. The basic argument is that symbols expressing different domain semantics should be perceptually discriminable through the use of different shapes and lines.

A second important factor for the perceptual expressiveness of symbols is the number of feature dimensions on which they differ [80]. According to feature integration theory [72], symbols can be detected most easily amongst other symbols if they differ in one visual variable only (e.g., color but not shape or size). They are detected pre-attentively and hence “pop out”, which means that they are easy to locate in a model. In contrast, search takes longer if the conjunction of several features is necessary to locate a symbol (e.g. searching a yellow circle among yellow and red squares and circles). Shape is the most important variable in this context [39]. As it is also used predominantly for discriminating objects, it is wise to use it as the primary distinguishing feature among different symbols. Additionally, redundant coding (e.g., a symbol is unique in shape and color) can help to prevent misinterpretations.

In consequence, symbols in a modeling grammar should differ appropriately and suf<sup>fi</sup>ciently in terms of visual variables in order to be perceptually discriminable. Further, they should pop out in one visual dimension to be easy to understand.

## 2.4. Semantic transparency

Semantic transparency describes whether the appearance of a symbol implies its corresponding concept. Moody [39] distinguishes between semantically immediate, opaque/conventional and perverse symbols on this continuum.

Icons, for example, belong to so-called concrete graphics that are easily associated with their referent real-world concepts, because there is a direct relationship between them and their meaning (e.g., a telephone icon to indicate a phone conference) [57]. Iconic representations for classes of activities could improve the understandability of process models as suggested by [34], but they are not yet commonly used. In contrast, abstract symbols typically used in process models have a rather distant relationship with their meaning, which is described as arbitrary [33]. Speci<sup>fi</sup>cally, routing symbols used in process modeling can be characterized as abstract and not as concrete since they mainly use features such as different shapes (e.g., rectangles or circles) [33].

Semantic transparency closely relates to learnability of symbols. If users can rely on previously-learned associations and symbols are semantically transparent, they will be learned more easily. Recker and Dreiling [53], for instance, showed that the ability to understand and read a model from a speci<sup>fi</sup>c process modeling grammar to another can be transferred surprisingly easy — partially because the semantic transparency of the two grammars compared was similar. However, many symbols used in modeling notations are abstract and have to be learnt explicitly [39]. In turn, the principle of semantic transparency would suggest that some routing symbols in process models are semantically more immediate than others. This fact should result in improved process model comprehension.

## 2.5. Aesthetics

Beyond perceptual discriminability, pop out and semantic transparency as important symbol design principles in modeling grammars, we realize that, up to some point, the design and appreciation of a symbol remains subject to subjective evaluation. This is because users may perceive different designs to be more aesthetic than others. Aesthetics are relevant for studying the effects of design on human understanding and evaluation, because users rate designs as more usable [71], and prefer it over others [63] if they perceive it as aesthetic. There is a history on exploring aesthetics in conceptual models and graphs [51] and indeed process models [15]; however, this stream of research has mainly focused on layout aesthetics of models as directed graphs. For instance, the authors in [51] propose rules to maximize symmetry and minimize edge crossings and bends to achieve more aesthetic diagrams. Design aesthetics pertaining to modeling grammar symbols, however, have not been examined.

Depending on the evaluated objects, researchers have looked at different criteria to determine aesthetic values, such as, for instance, balance or symmetry [29]. In general, good design should balance complexity and order. For instance, analyses of aesthetically pleasing screen designs revealed measures such as balance, proportions, symmetry or even distribution to be relevant [40]. “Ideal” proportions, combination of parts as a “unity” or “good” form and prototypicality are often considered design features related to aesthetic product design [75]. These studies suggest, in turn, that routing symbols that are perceived as more aesthetic than others will aid process model comprehension.

## 3. Hypotheses development

Our primary conjecture is that the visual design of routing symbols in process models will affect how well end users will comprehend the control <sup>fl</sup>ow of the modeled processes. More precisely, we argue that process model comprehension, measured in terms of accuracy, ef<sup>fi</sup>ciency and task dif<sup>fi</sup>culty [30], is a function of four attributes of routing symbol design, viz., perceptual discriminability, pop out, semantic transparency, and aesthetics.

This conjecture builds on the argument that inef<sup>fi</sup>cient visual routing symbol design will impair the comprehension of a process model because it induces additional extraneous cognitive load into the comprehension task. If, however, the notational constructs are designed such that they communicate the meaning of a process more ef<sup>fi</sup>ciently, model viewers should also be able to understand models better, faster and with more ease due to relatively lower extraneous cognitive load. We now discuss this conjecture in terms of four detailed propositions.

In our initial proposition, we explore how process model comprehension will vary depending on the perceptual discriminability of the routing symbols used in the model. Our argument is that routing symbols that have higher perceptual discriminability will induce lower extraneous cognitive load into the model comprehension task. Perceptual discriminability suggests that it will be easier and faster for model readers to perceptually process and differentiate the different visual components of the process model, thereby lowering the extraneous load of the cognitive processing task [39]. Lower extraneous load has been associated with increased comprehension accuracy [58], and decreased task dif<sup>fi</sup>culty perceptions [30]. Also, it has been argued (though not conclusively proven) that comprehension ef<sup>fi</sup>ciency can be increased [17]. Formally, we state:

H1a. Process model comprehension accuracy will be higher when process models contain routing symbols with high perceptual discriminability.

H1b. Process model comprehension efficiency will be higher when process models contain routing symbols with high perceptual discriminability.

H1c. Process model comprehension task difficulty will be lower when process models contain routing symbols with high perceptual discriminability.

Second, we turn to pop out effects of routing symbols. According to feature integration theory, perceptual processing of visual symbols is strengthened if the symbols contain one visual variable (e.g., shape, or color) with a unique value [52]. Such symbols appear to “pop out” from all other symbols without requiring much cognitive effort. In turn, we can expect that process models that contain routing symbols that are differentiated from all other visual symbols by a unique value in one visual dimension are more easily and perceptually processed faster, in turn aiding the cognitive processing task. Formally, we state:

H2a. Process model comprehension accuracy will be higher when process models contain routing symbols that are perceived to pop out.

H2b. Process model comprehension efficiency will be higher when process models contain routing symbols that are perceived to pop out.

H2c. Process model comprehension task difficulty will be lower when process models contain routing symbols that are perceived to pop out.

In our third proposition, we explore how process model comprehension changes when the semantic transparency of routing symbols varies. The semantic transparency principle suggests that good visual symbols provide cues to the meaning of their content (“form implies content”). Semantically transparent symbols reduce extraneous cognitive load because their meaning can either be directly perceived or easily deduced [49]. This would again suggest a cognitive of<sup>fl</sup>oading effect in which perceptual processing of symbols aids the subsequent cognitive interpretation process , which should result in better process model comprehension (in terms of accuracy, ef<sup>fi</sup>ciency and lower dif<sup>fi</sup>culty). We de<sup>fi</sup>ne the following three hypotheses:

H3a. Process model comprehension accuracy will be higher when process models contain routing symbols with high semantic transparency.

H3b. Process model comprehension efficiency will be higher when process models contain routing symbols with high semantic transparency.

H3c. Process model comprehension task difficulty will be lower when process models contain routing symbols with high semantic transparency.

In our last general proposition, we turn to the aesthetic design of routing symbols. Previous studies have demonstrated that users rate designs as more usable [71], and prefer it over others [63] if they perceive it as aesthetic. These <sup>fi</sup>ndings suggest that task performance (such as the task of comprehending a process model) may be increased if the task artifact is aesthetically pleasing, because it generates a positive affective response [3]. Affective response has been shown to be associated with, for instance, task persistency [5], which relates to task performance. These <sup>fi</sup>ndings suggest that comprehension performance (in terms of accuracy, ef<sup>fi</sup>ciency and perceived dif<sup>fi</sup>culty) may also be affected by the extent to which routing symbols are perceived to be aesthetically pleasant. We state:

H4a. Process model comprehension accuracy will be higher when process models contain routing symbols that are perceived to be aesthetic.

H4b. Process model comprehension efficiency will be higher when process models contain routing symbols that are perceived to be aesthetic.

H4c. Process model comprehension task difficulty will be lower when process models contain routing symbols that are perceived to be aesthetic.

## 4. Research method

To test our hypotheses, we chose an experimental method as it affords higher internal validity than other methods [10]. Speci<sup>fi</sup>cally, we selected a 1\*4 between-groups design that allowed us to focus on the four notational design factors whilst controlling for potentially confounding other variables (e.g., process modeling knowledge or domain complexity). We randomly assigned participants across groups and randomly assigned the order of tasks to control for learning effects.

## 4.1. Research design

Our design featured one between-subject factor (routing symbol design) and four dependent variables. Additionally, we considered the covariate prior process modeling method knowledge in our design.

The between-subjects factor, the design of routing symbols, had four levels (R<sub>EPC</sub>, R<sub>BPMN</sub>, R<sub>UML</sub>, R<sub>YAWL</sub>). The routing symbols were derived from four different popular process modeling grammars, viz., EPC, BPMN, UML AD and YAWL. These grammars are typically considered as appropriate representatives for the current set of available grammars in-use [56].

Concerning the manipulation of the variable “routing symbol”, we refrained from inventing arti<sup>fi</sup>cial notations for routing symbols (e.g., with very low semantic transparency or with in<sup>fl</sup>ated perceptual discriminability). This might have maximized the likelihood of significant negative effects on comprehension but would have led to in<sup>fl</sup>ated risk of type-2 errors. Instead, we decided to use realistic examples of construct notational design sets based on the design of existing process modeling grammars, so as to maximize relevance for practice and ensure ecological validity of our experimental design. This design allowed us to examine whether different design solutions as used in practice are equally good concerning support of comprehension or whether there are relevant differences.

To operationalize the quality of the design of the four routing symbol sets according to the four notational design attributes semantic transparency, perceptual discriminability, pop out and aesthetics, we collected perceptual rating measurements of the routing symbols alongside these dimensions, which allowed us to separate ‘good’ from ‘bad’ designs.

As dependent variables, we used four measures to examine process model comprehension, consistent with prior work in this area [8,47]. First, we calculated the number of correct answers in a model comprehension task as a measure of comprehension accuracy. Second, we collected the task completion time as a measure of comprehension efficiency. Third, we measured the perceived dif<sup>fi</sup>culty to complete the model comprehension tasks as a measure of the perceived cognitive load associated with comprehending process models. Fourth, as routing symbols directly relate to the understanding of the control <sup>fl</sup>ow (one particular element of a process model), we added a second measure of perceived dif<sup>fi</sup>culty of process model comprehension — a judgment of the difficulty of control flow comprehension speci<sup>fi</sup>cally.

Gemino and Wand [17] differentiate model comprehension tasks between problem-solving tasks in which newly developed mental models have to be integrated with deep knowledge structures and comprehension tasks. These two levels of measurements have also been referred to as “deep-level understanding” and “surface-levelunderstanding” [8]. As our research focuses on the effect of symbol design in otherwise informationally equivalent models on effective understanding and not on the different mental models evoked in users, ‘surface-level’ model comprehension tasks were the best choice of measurement. An additional factor for choosing “surface-level” comprehension tasks was that general interpretability of models is the basis for a variety of more speci<sup>fi</sup>c tasks such as process analysis or redesign [8].

Regarding the covariate, we captured data on prior method knowledge in process modeling because it was previously shown to in<sup>fl</sup>uence model understanding [21]. We measured prior method knowledge by using the set of process modeling method knowledge questions used by Mendling and Strembeck [37], which quizzes respondents' theoretical knowledge of process modeling. Their questions, notably, are grammar-independent and concern grammatical rules of process model routing logic, derived from fundamental work in this area [23], and address control <sup>fl</sup>ow criteria such as reachability, deadlocks, liveness and option to complete.

## 4.2. Procedures and materials

We used a paper questionnaire with <sup>fi</sup>ve different sections. The Appendix includes examples of the materials.

The <sup>fi</sup>rst section comprised questions about the participants' demographic data, academic quali<sup>fi</sup>cations and prior method knowledge. Participants were asked about the number of years they had worked in the IT-sector and the extent to which they had previously been involved with modeling in education and work. With these demographics, we can describe a sample frame similar to that in other studies on process model comprehension [35,53,59,60].

In the second section of the questionnaire we used the set of process modeling method knowledge questions used by Mendling and Strembeck [37] to measure prior method knowledge, which we used as a covariate in our data analysis. Additionally, we collected self-report data on the estimated amount of hours spent on learning process modeling.

The third section contained a tutorial on the process modeling grammar, in which the treatment was provided (as explained below). The tutorial was speci<sup>fi</sup>cally tailored to inform participants about the meaning of each symbol in the provided grammar and covered everything the participants needed to know to perform the subsequent comprehension tasks.

The fourth section of the questionnaire displayed four different process models with eight corresponding comprehension tasks for each model (viz., 32 questions in total). Participants in each of the four main study groups (according to the between-subject factor routing symbol design) got all four models in the same routing symbol design (viz., using the same grammatical design of the process model). For each model similar comprehension questions were asked. Additionally, for each set of comprehension questions related to each model, participants also indicate the perceived cognitive load of answering the set of questions, on basis of the perceived cognitive load scale described below. To avoid any order effects e.g., due to fading attention, we used two different sampling strategies. Speci<sup>fi</sup>cally the models and comprehension questions were arranged in different sequences. Participants were randomly assigned to one of the eight different questionnaires (four treatments of routing symbol design in two different sampling versions each).

The <sup>fi</sup>fth and last section of the questionnaire included questionnaire scales in which participants could rate the routing symbols (AND and XOR) in the models shown in accordance to the four relevant design criteria discussed (viz., semantic transparency, perceptual discriminability, pop out and aesthetics). Additionally, this section included a scale on perceived control <sup>fl</sup>ow comprehension as an additional measure of the cognitive load associated with the model comprehension tasks.

Subjects were allowed to spend as much time as desired for the completion of the experimental tasks. On average, the experiment took about 40 min to complete.

4.3. Manipulation of treatment: construction of model sets with different routing symbols

Although process modeling grammars emphasize different viewpoints on processes [66], they share several common elements. Fig. 2 shows the routing symbols selected for the experimental study, which are inspired by existing process modeling grammars EPC (routing symbols $\mathsf { R } _ { \mathrm { E P C } } )$ , UML Activity Diagrams (routing symbols $\mathrm { R } _ { \mathrm { U M L } } )$ and BPMN (routing symbols ${ \sf R } _ { \mathrm { B P M N } } )$ , and YAWL (routing symbols R ). Relative size is held constant in comparison to further symbols, so that all routing symbols used are of comparable size. Additionally, the orientation of the symbols used is similar, as they are in right angle or directly aligned to the edge <sup>fl</sup>ow direction. Therefore, shape $( S _ { \mathrm { G r a m m a r } } )$ remains the main variable that varies amongst the symbols used across the grammars considered. $S _ { \mathrm { E P C } }$ represents AND using a circle with a logical marker for ‘and’ in it ${ \binom { \dots , \dots , Y } { g } }$ and XOR by using a circle and an $" \mathrm { X " }$ marker. $\mathsf { S } _ { \mathrm { U M L } }$ has different symbols for these concepts: AND is depicted as a <sup>fi</sup>lled bar, while XOR is represented by a diamond-shaped symbol. S uses small rectangles with inscribed triangles. In the AND node, the triangle points inward, in the XOR node outward. S employs di amond symbols for both node types, using a plus marker for the AND.

Fig. 2 summarizes the notational details of the four process models used in our study. We can see that the models are structurally equivalent, and only different in their use of different symbols for the routing behavior. All further model elements were held constant across the model sets.

The models were developed as follows: First, we created Visio stencils to be able to model all necessary symbols in one tool providing high <sup>fl</sup>exibility for layout. We directly redraw the exact routing symbol designs from the tool ARIS for EPC (routing symbols $\mathsf { R } _ { \mathsf { E P C } } )$ , from examples given in the standard documents for UML Activity Diagrams (routing symbols $\mathrm { R } _ { \mathrm { U M L } } )$ and BPMN (routing symbols ${ \sf R } _ { \mathrm { B P M N } } )$ , and from the original research paper on YAWL (routing symbols $\mathrm { R } _ { \mathrm { Y A W L } } ) [ 7 3 ] ,$ respectively. Next, the model design was optimized according to process modeling guidelines [35]. Finally, we exchanged the routing symbols in each of the models.

We used four different models so that the selection of the particular domain depicted would not in<sup>fl</sup>uence results. The four models were selected from different domains such that we could expect that they are understandable for an average student with no special domain knowledge. Two of them stemmed from the business domain (product management and customer support, sales and distribution). The other two stemmed from uncommon domains: an emergency process plan for drinking water pollution and an e-mail election process (the last process was taken from the BPMN standard document [7]). Each of the four models used contained 21 activities. The amount of ANDs varied between 4 and 10, the amount of XORs between 4 and 11. The model size was held constant for all models, because prior research in the area of data modeling has shown that performance decreased in query composition tasks when larger models were used [6]. A suf<sup>fi</sup>cient level of complexity is required in empirical studies, because problems concerning the cognitive load may not be present for very small, manageable models, but only appear in more complex models. The models used are realistic examples of “normal” models, as models in practice contain about 19 tasks on average [48].

## 4.4. Measurement of dependent variables: comprehension accuracy, comprehension efficiency and perceived difficulty

For each model in the questionnaire we posed the same eight types of comprehension questions. The comprehension questions asked participants on four different issues concerning the control <sup>fl</sup>ow logic: concurrency, exclusiveness, order and repetition. Our questions were based on the measures developed and used in [35,58,59]. However, in comparison we formulated questions consistently, so that participants always had to consider two model elements (two activities) and their relationship for answering a question. This way, we ensured that the questions all speci<sup>fi</sup>cally addressed the routing of process activities in a model. We worded each question using day-to-day-language.

We took care that the wording in the questions is understandable, and we ran a pre-test in order to make sure that the participants understood the questions. Questions were selected speci<sup>fi</sup>cally to concern timely and logical relationships between tasks in a process, such that participants had to rely on using the diagrams to understand these relationships. In the comprehension questions, participants had a choice of ‘right’, ‘wrong’ or ‘I don't know’ to reduce the probability of guessing.

<table><tr><td></td><td>RUML</td><td colspan="2">RBPMN</td><td>REPC</td><td></td></tr><tr><td>AND</td><td><img src="/api/attachments/MG6V5BSA/fulltext/images/c85a89408d9ce0c8ec9f33faa7b09c6d2d6ac57a4829f8ce4ef6c4b5643e64e3.jpg"/></td><td colspan="2"><img src="/api/attachments/MG6V5BSA/fulltext/images/810715fa55381e1186ab77bf8acc8828d402a849fa7e43be048b13962eb367ff.jpg"/></td><td><img src="/api/attachments/MG6V5BSA/fulltext/images/ec8b68142c2eafb5a5fbb54d05bd78538bdc1baa186799c27f21b13704c98215.jpg"/></td><td><img src="/api/attachments/MG6V5BSA/fulltext/images/a5ce244dd693b38db5ffcbaa463b3bbe7425ebd1a31e5184f9528fe836da6add.jpg"/></td></tr><tr><td>Outer Shape</td><td rowspan="2">narrow rectangle(bar)</td><td colspan="2">symmetric diamond-shape</td><td>circle</td><td>rectangle</td></tr><tr><td>Inner Shape</td><td colspan="2">internal marker (“+”)</td><td>logical marker for‘and’ (“^”)</td><td>left- and right-sided open triangle</td></tr><tr><td>XOR</td><td><img src="/api/attachments/MG6V5BSA/fulltext/images/d0fe1ace88ab7f861635ff2d7b7427391946414862757fe54c0f7bbfe53834e2.jpg"/></td><td colspan="2"><img src="/api/attachments/MG6V5BSA/fulltext/images/78ed8d9c7af13ee14313b96aa3ffb5f29e2b4d21f433b644a5072a6d228fc908.jpg"/></td><td></td><td><img src="/api/attachments/MG6V5BSA/fulltext/images/281bf7ae96e656dcf8c64920543e677e22f9a201c7ccaf9dcea3d0294564e617.jpg"/></td></tr><tr><td>Outer Shape</td><td rowspan="2">diamond-shapewithout internalmarker</td><td colspan="2">symmetric diamond-shape</td><td>circle</td><td>rectangle</td></tr><tr><td>Inner Shape</td><td colspan="2">-</td><td>“X” marker</td><td>triangle</td></tr><tr><td></td><td><img src="/api/attachments/MG6V5BSA/fulltext/images/72ea4ca138e52ee952a5a5adccff5ae64a73971ebe50da29bc39119351e05f0e.jpg"/></td><td colspan="2"><img src="/api/attachments/MG6V5BSA/fulltext/images/e3b14f64a6bc894d8cb91f99edb105c7a01bf78ec827b4cceb3eadeefe52481e.jpg"/></td><td><img src="/api/attachments/MG6V5BSA/fulltext/images/f7fccba1f1e78dfda7917d76f07c7d0b13efeef1701eb32021d499267cb884b3.jpg"/></td><td><img src="/api/attachments/MG6V5BSA/fulltext/images/c1d61ed298643fdb16806109f3ffa2334b46d555272b5c85f04c14608a31406a.jpg"/></td></tr></table>

Fig. 2. Routing symbols derived from existing process modeling grammars and details of a drinking water supply process model containing the different routing symbols

Despite the use of the same wording, there is a large number of possibilities how to ask these questions, because any two activities can be targeted with the same question. We identi<sup>fi</sup>ed two basic variations: 1) the statement given in the question is correct or wrong and 2) the location of the chosen activities. For varying the location of activities consistently, we decided to use pairs of activities, which are either close (1 activity between them) or distant (>1 activity between them) according to the spatio-visual distance between them. As a consequence, we constructed the test material, varying correct and wrong answers as well as close and distant answers. This measure design allowed us to collect the total number of correct answers as a measure of comprehension accuracy.

To measure comprehension ef<sup>fi</sup>ciency, we recorded the self-report completion time for the comprehension questions. We asked participants to write down the point of time at the beginning and the end of the questions, similar to [53].

To measure perceived dif<sup>fi</sup>culty of the comprehension task, we included the 7-point single-item perceived cognitive load measure (anchored between “very dif<sup>fi</sup>cult” and “very easy”) developed in [32]. This measure was accompanying each model comprehension task.

Additionally, to measure the perceived control <sup>fl</sup>ow comprehension dif<sup>fi</sup>culty speci<sup>fi</sup>cally, we constructed a new scale with 4 items, which asked participants whether it had been easy to perceive loops (aspect repetition), concurrency, exclusiveness and sequence of activities (aspect order) in the four models.

4.5. Measurement of independent variable: notational evaluation of the routing symbol designs

To create measures for the independent variables, we constructed new four-item scales for each of the selected criteria: semantic transparency, visual discriminability, pop out and aesthetics. Self-construction of the scales was necessary, because there were no existing measures available for these constructs. More importantly, the nature of these constructs (dimension of the perceptual effectiveness of visual designs) demanded the construction of perceptional scales to evaluate individuals' beliefs about each of the dimensions.

Item construction for semantic transparency, pop out and visual discriminability was theoretically grounded in Moody's framework of desirable properties of effective visual notations [39] and followed established guidelines [54]. First, an item pool was generated with approximately 10 items per evaluated dimension. Then wordings were evaluated in a pre-test with 10 participants. The pre-test consisted of a card-sorting and a questionnaire in which each item candidate was rated according to its wording and its appropriateness to assess the respective dimension on a <sup>fi</sup>ve-point scale. The content validity of items was checked in an online card sorting test. We used a closed card sorting test with 6 pre-testers, in which they had to arrange the items to given dimensions as well as an open card sorting test with 4 pre-testers in which they could arrange the items to self-named groups. For the <sup>fi</sup>nal questionnaire the best four item candidates for each dimension were chosen to allow for suf<sup>fi</sup>cient reliability of scales. The visual discriminability scale was used to capture the perceptual discriminability of XOR and AND symbols. Additionally, both the XOR and the AND symbol sets were evaluated with the scales for semantic transparency, pop out and aesthetics, respectively. In turn, this approach allowed us to obtain measures for the visual design of the routing symbol sets in each of the models, as perceived by the participants working with the models.

## 4.6. Participants

Participants in the study were 154 information systems and business students from a European university. Table 1 shows selected demographic data about participants per cell. To account for expert– novice differences [49], we tried to <sup>fi</sup>nd participants with both high and low experience in modeling and recruited them from different classes with and without prior training in modeling. We selected business school students as they are a realistic proxy of the future end-users of business process models. Table 1 summarizes key demographic variables. We performed analysis of variance tests to screen for possible differences between the experimental groups' demographics, which yielded no problematic differences.

## 5. Results

## 5.1. Validity and reliability assessment

We started by assessing validity and reliability of the Likert-type measures for the symbol evaluation. First, we conducted a principal components analysis with all symbol evaluation items as well as the items measuring perceived control <sup>fl</sup>ow comprehension dif<sup>fi</sup>culty. Five factors emerged with eigenvalues greater than 1, explaining 74.1% of the total variance. The <sup>fi</sup>ve-factor solution was rotated to simple structure using Varimax. Table D.3 in the Appendix shows all factor loadings, cross-loadings, eigenvalues, and variance statistics. This <sup>fi</sup>rst analysis demonstrated that the four items from the questionnaire scale control <sup>fl</sup>ow comprehension loaded on one factor as expected (factor 5). Additionally, all items evaluating the AND symbol loaded on one factor (factor 1). Factor 2 comprises eight items from the original subscales for evaluating ‘pop out’ of XOR as well as ‘visual discriminability’ of AND and XOR. This is surprising, as visual discriminability items were asked symmetrically for AND and XOR, but seemed to relate more to the design of the XOR than the AND symbol. The factors 3 and 4 resemble further XOR symbol evaluation scales.

As symbol evaluation items were used twice in the questionnaire (to evaluate XOR and AND separately), in a second step, we performed exploratory factor analyses, with extraction and Varimax rotation of solutions with between 2 and 3 factors for XOR and AND items separately. An iteration of the factor analysis was conducted to eliminate problematic measurement items. During this process, it became apparent that the item “The meaning of the XOR/AND-symbol is easy to recognize based on its visual design.” did not load on the expected factor (originally an item for semantic transparency). Therefore, we excluded this item from further analysis. The resulting PCA indicated that there were 2 factors in the dataset with eigenvalues greater than 1; however the gradient of the scree slope suggested that a solution with three factors would be tenable, too. We chose to use the three factor solution, so that the factors could re<sup>fl</sup>ect the original questionnaire scales. In comparison to the <sup>fi</sup>rst factor, which accounted for 62% (XOR), respectively 65% (AND) of the variance, the proportion of variance explained by the further two factors was small (8% to 12%) before the varimax rotation.

To summarize this three-factor solution, it is apparent that the underlying structure displays a fairly unambiguous pattern of item loadings, in line with the postulated questionnaire scales. The factor loadings, cross-loadings, eigenvalues, and variance statistics are presented in the Appendix. Factors are conceptually clear, with 3–4 items loading at 0.7 or above at each factor (labeled “pop out”, “aesthetics” and “semantic transparency”) and exhibit only low cross-loadings. Factor structure and loadings are very similar for the items used to evaluate XOR as well as AND, demonstrating suf<sup>fi</sup>cient convergent and discriminant validity of our measurements.

To estimate reliability and internal consistency of our measures, we computed Cronbach's α, which should be greater than or equal to 0.7 to consider items to be uni-dimensional [42].

The reliability for the self-constructed scale “Subjective Dif<sup>fi</sup>culty of Control Flow Comprehension” including 4 items was good (α=0.77). Reliability of the newly developed scales for symbol evaluation were also satisfying (α=0.87–0.94). Additionally we calculated Cronbach's α for the subjective cognitive load items belonging to the problem-solving tasks of the four models (α=0.95). Cronbach's α for the general knowledge test on process modeling was 0.74. These results suggest adequate reliability. Deletion of any item produced no marked effect on the instrument's reliability score. In light of these results, we retained all items on these instruments.

Overall, the statistical results con<sup>fi</sup>rm that the developed measurement instruments are of appropriate validity and reliability.

## 6. Hypothesis testing

To examine our hypotheses, we ran four multiple regression analyses implemented in SPSS Version 19.0, one for each dependent variable (comprehension accuracy, comprehension ef<sup>fi</sup>ciency, and task dif<sup>fi</sup>culty in terms of the two measures — perceived cognitive load and perceived control <sup>fl</sup>ow comprehension dif<sup>fi</sup>culty), respectively. For all four multiple regression analyses we used the same variables as independent factors, viz., the average total factor scores for perceived semantic transparency, visual discriminability, pop out and aesthetics, as well as the total process modeling method knowledge score.

Table 1 Participants demographic data.

<table><tr><td rowspan="2"></td><td colspan="2"> $R_{UML} (n=44; 28\%)$ </td><td colspan="2"> $R_{BPMN} (n=48; 31\%)$ </td><td colspan="2"> $R_{YAWL} (n=21, 14\%)$ </td><td colspan="2"> $R_{EPC} (n=41, 27\%)$ </td><td colspan="2">Total (n=154)</td></tr><tr><td>Mean/amount</td><td>SD/percentage</td><td>Mean/amount</td><td>SD/percentage</td><td>Mean/amount</td><td>SD/percentage</td><td>Mean/amount</td><td>SD/percentage</td><td>Mean/amount</td><td>SD/percentage</td></tr><tr><td>Age</td><td>23.40</td><td>2.62</td><td>23.75</td><td>3.80</td><td>23.00</td><td>3.27</td><td>24.32</td><td>3.16</td><td>23.70</td><td>3.26</td></tr><tr><td>Gender</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Male</td><td>27</td><td>61%</td><td>34</td><td>71%</td><td>17</td><td>81%</td><td>24</td><td>59%</td><td>102</td><td>66%</td></tr><tr><td>Female</td><td>17</td><td>39%</td><td>14</td><td>29%</td><td>4</td><td>19%</td><td>17</td><td>41%</td><td>52</td><td>34%</td></tr><tr><td>Highest grade completed</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>High school</td><td>7</td><td>16%</td><td>13</td><td>27%</td><td>3</td><td>14%</td><td>3</td><td>7%</td><td>26</td><td>17%</td></tr><tr><td>Bachelor</td><td>34</td><td>77%</td><td>34</td><td>71%</td><td>17</td><td>81%</td><td>36</td><td>88%</td><td>121</td><td>78%</td></tr><tr><td>Master</td><td>3</td><td>7%</td><td>1</td><td>2%</td><td>1</td><td>5%</td><td>2</td><td>5%</td><td>7</td><td>5%</td></tr><tr><td>Participants with work experience in the IT-sector</td><td>15</td><td>34%</td><td>16</td><td>33%</td><td>3</td><td>14%</td><td>12</td><td>30%</td><td>46</td><td>30%</td></tr><tr><td>Participants with work experience with process models</td><td>4</td><td>9%</td><td>6</td><td>13%</td><td>2</td><td>10%</td><td>6</td><td>15%</td><td>18</td><td>12%</td></tr><tr><td>Participants with training on modeling basics</td><td>31</td><td>71%</td><td>33</td><td>69%</td><td>18</td><td>86%</td><td>36</td><td>88%</td><td>118</td><td>77%</td></tr><tr><td>Hours of training on modeling basics at university or school</td><td>27.00</td><td>36.37</td><td>28.00</td><td>33.51</td><td>31.24</td><td>45.76</td><td>24.34</td><td>23.93</td><td>27.12</td><td>33.72</td></tr><tr><td>Process modeling test score</td><td>65%</td><td>0.20</td><td>60%</td><td>0.20</td><td>68%</td><td>0.20</td><td>65%</td><td>0.22</td><td>64%</td><td>0.20</td></tr></table>

One assumption behind the use of multiple regression analysis is that the variables are measured on a continuous scale and are normally distributed. Our data screening con<sup>fi</sup>rmed that the measures for the dependent variables completion time, perceived cognitive load and perceived control <sup>fl</sup>ow comprehension dif<sup>fi</sup>culty as well as for the independent variables semantic transparency, pop out and aesthetics met these criteria according to one-sample Kolmogorov–Smirnov tests. The dependent variable comprehension score (skewness = −0.88, kurtosis=0.07), the process modeling knowledge test score (skewness=−0.30, kurtosis=−0.50) and perceptual discriminability (skewness=−0.90, kurtosis=−0.07) did not meet the criteria of normal distribution in this formal test. However, in large samples over 100 the impact of skewness and kurtosis on the results of the regression analysis diminishes and underestimation of variance disappears [70]. Therefore, we decided to use a linear regression model to analyze our data.

Our initial analyses using ordinary least square (OLS) regression models lead to unstable results of beta coef<sup>fi</sup>cients when adding or deleting one of the independent variables. For instance, if using perceived semantic transparency, visual discriminability, pop out and aesthetics as independent factors and comprehension accuracy as dependent variable, the model as a whole was signi<sup>fi</sup>cant and lead to a rejection of the joint hypothesis that these coef<sup>fi</sup>cients are zero (F= 4.14, p=0.02), but on the other hand all regression coef<sup>fi</sup>cients were insigni<sup>fi</sup>cant. Deleting one of the predictor variables changed the signi<sup>fi</sup>cance of predictors.

Such unstable results are typically an indicator for multicollinearity of predictor variables [16]. And indeed, pop out correlates strongly with the other symbol evaluations $( 0 . 6 1 - 0 . 7 4 , \mathfrak { p } = 0 . 0 0 )$ , and bivariate correlations of around 0.70 can already in<sup>fl</sup>ate the size of error terms, weakening the analysis [73]. As determining the relevance of individual predictors is especially relevant for addressing our hypotheses, we thus decided to use ridge regression models to overcome shortcomings of the OLS regression. Ridge regression can handle sets of independent variables with multicollinearity better than OLS regression, because it generates estimators with smaller standard error than OLS regression [13]. Ridge regression was discussed controversially in the 1980s, but recent enhancements of the algorithms lead to robust solutions, stable coef<sup>fi</sup>cients and high quality of <sup>fi</sup>t [68]. Table 2 reports the results of the ridge regression analyses showing the standardized beta coef<sup>fi</sup>- cients and signi<sup>fi</sup>cance levels.

The overall regression model for the dependent variable comprehension accuracy was signi<sup>fi</sup>cant, $\mathtt { R } ^ { 2 } = 0 . 1 5 , \mathtt { F } ( 6 , 3 9 ) = 3 . 5 3 , \mathtt { p } < 0 . 0 1$ The data in Table 2 further shows that pop out, perceptual discriminability and process modeling knowledge are signi<sup>fi</sup>cant predictors for process model comprehension, while semantic transparency and aesthetics are not. These results thus support H1a and H2a whereas hypotheses H3a and H4a must be refuted.

A regression of the subjects' responses on the comprehension ef<sup>fi</sup>- ciency measured in terms of time yielded a non-signi<sup>fi</sup>cant overall model. Therefore, hypotheses H1b–H4b were rejected.

In hypotheses H1c–H4c we expected that better symbol design in the dimensions perceptual discriminability, pop out, semantic transparency, and aesthetics will positively in<sup>fl</sup>uence perceptions of task dif<sup>fi</sup>culty of process model comprehension. We used two different measures for task dif<sup>fi</sup>culty (perceived cognitive load and perceived control <sup>fl</sup>ow comprehension dif<sup>fi</sup>culty) which yielded different results. For perceived cognitive load, our predictions were borne out: the overall regression model and all regressing coef<sup>fi</sup>cients were signi<sup>fi</sup>cant leading to a 33% explanation rate. However, we found that only pop out, perceptual discriminability and process modeling knowledge were positively related to perceived control <sup>fl</sup>ow comprehension dif<sup>fi</sup>culty, while semantic transparency and aesthetics were not. These results provide partial support for H3c and H4c and full support for H1c and H2c.

In addition to the regression analyses reported, we ran further analyses to clarify whether individual perceptions of symbol designs or the treatment of actual different routing symbols account for differences in model comprehension. To that end, we ran the same analyses as reported, but included the variable routing symbol design with four levels $( \mathrm { R } _ { \mathrm { E P C } } , \mathrm { R } _ { \mathrm { B P M N } } , \mathrm { R } _ { \mathrm { U M L } } , \mathrm { R } _ { \mathrm { Y A W L } } )$ as a further independent factor. As the ridge regression is part of the CATREG module in SPSS 19.0, it was possible to include a further variable on a nominal scale. Results demonstrated that the actual routing symbol design was not a signi<sup>fi</sup>cant predictor of process model comprehension. It thus seems that it is rather the individual perception of the symbol design than the property of the symbol itself, which determines the effect on comprehension.

In summary, we obtained strong support for our assertion that the perception of pop out and perceptual discriminability of symbols is positively associated with comprehension accuracy and task dif<sup>fi</sup>culty. Semantic transparency and aesthetics were related to perceived cognitive load. Thus, we are con<sup>fi</sup>dent that our results support the fundamental proposition we have sought to test in our research. We obtained no support for our hypotheses regarding the estimation of process model comprehension ef<sup>fi</sup>ciency (measured by task completion time). Table 3 summarizes our results.

## 7. Discussion

Our empirical study set out to test the in<sup>fl</sup>uence of routing symbol design on process model comprehension in terms of accuracy, ef<sup>fi</sup>- ciency and perceived dif<sup>fi</sup>culty.

From a general perspective, the study reported in this paper extends research into the development of a validated notational design theory for modeling grammars. Most notably, we provide a <sup>fi</sup>rst operationalization, measurement and test of the theory of visual notations by Moody [39].

The results obtained provide support for the nomological validity of Moody's design principles. We observed different levels of signi<sup>fi</sup>cance for our hypotheses on the four design attributes of routing symbols. In particular, pop out and perceptual discriminability showed a stronger effect on process model comprehension than semantic transparency and aesthetics. One possible explanation can be that pop out and perceptual discriminability of visual symbols are dimensions that directly relate to early stages of neural processing; differences in form of symbols can even be processed pre-attentively [79]. Therefore, they have a more direct effect on cognitive load involved in model comprehension tasks. It is not surprisingly that results are similar for both characteristics as they are closely related; symbols that are highly

Ridge regression analysis: <sup>fi</sup>nal model statistics.

<table><tr><td rowspan="3">Independent factors</td><td colspan="4">Dependent variables</td></tr><tr><td>Comprehension accuracy</td><td>Time</td><td>Perceived cognitive load</td><td>Perceived control flow comprehension difficulty</td></tr><tr><td>St. beta</td><td>St. beta</td><td>St. beta</td><td>St. beta</td></tr><tr><td>Process modeling knowledge</td><td>0.14***</td><td>-0.04</td><td>0.14***</td><td>0.14***</td></tr><tr><td>Perceptual discriminability</td><td>0.09*</td><td>-0.04</td><td>0.14***</td><td>0.10*</td></tr><tr><td>Pop out</td><td>0.09**</td><td>-0.2</td><td>0.13***</td><td>0.13***</td></tr><tr><td>Semantic transparency</td><td>-0.02</td><td>-0.02</td><td>0.11***</td><td>0.06</td></tr><tr><td>Symbol aesthetics</td><td>0.04</td><td>0.05</td><td>0.09*</td><td>0.04</td></tr><tr><td>F</td><td>3.69**</td><td>0.44</td><td>10.89***</td><td>6.06***</td></tr><tr><td>R2</td><td>0.15</td><td>0.03</td><td>0.33</td><td>0.22</td></tr></table>

\* p 0.01.

\*\*\* p≤0.001.

Table 3  
Summary of hypothesis testing results

<table><tr><td></td><td>Independent variable</td><td>Dependent variable</td><td>Results</td></tr><tr><td>H1a</td><td>Perceptual discriminability</td><td>Comprehension accuracy</td><td>Supported</td></tr><tr><td>H1b</td><td>Perceptual discriminability</td><td>Comprehension efficiency</td><td>Not supported</td></tr><tr><td>H1c</td><td>Perceptual discriminability</td><td>Task difficulty</td><td>Supported</td></tr><tr><td>H2a</td><td>Pop out</td><td>Comprehension accuracy</td><td>Supported</td></tr><tr><td>H2b</td><td>Pop out</td><td>Comprehension efficiency</td><td>Not supported</td></tr><tr><td>H2c</td><td>Pop out</td><td>Task difficulty</td><td>Supported</td></tr><tr><td>H3a</td><td>Semantic transparency</td><td>Comprehension accuracy</td><td>Not supported</td></tr><tr><td>H3b</td><td>Semantic transparency</td><td>Comprehension efficiency</td><td>Not supported</td></tr><tr><td>H3c</td><td>Semantic transparency</td><td>Task difficulty</td><td>Supported for perceived cognitive load, but not for perceived control flow comprehension difficulty</td></tr><tr><td>H4a</td><td>Aesthetics</td><td>Comprehension accuracy</td><td>Not supported</td></tr><tr><td>H4b</td><td>Aesthetics</td><td>Comprehension efficiency</td><td>Not supported</td></tr><tr><td>H4c</td><td>Aesthetics</td><td>Task difficulty</td><td>Supported for perceived cognitive load, but not for perceived control flow comprehension difficulty</td></tr></table>

discriminable will also be perceived easily and would be rated higher on the pop out scale. In contrast, semantic transparency and aesthetics relate to later stages of the perceptional processing. They re-<sup>fl</sup>ect a subjective impression of the quality of the symbol design, which is not directly related to the perceptual effectiveness in the cognitive task. We originally postulated that aesthetic design might have an in<sup>fl</sup>uence on model comprehension due to affective responses, and semantic transparency because of easy associations with existing knowledge structures which would enable cognitive of<sup>fl</sup>oading. Both modes of action are more likely to depend on individual graphic preferences and prior experiences stored in long-term-memory in comparison to the pre-attentative perception processes as re<sup>fl</sup>ected in pop out and perceptual discriminability.

Turning to the three different dimension of process model comprehension considered, we found that the effects of symbol design perceptions were not equally strong on the different dependent variables. Most notably, there was no effect on the comprehension ef<sup>fi</sup>ciency. On the forefront, this result suggest that secondary notation effects (visual design choices) do not impact interpretational ef<sup>fi</sup>ciency [8], viz., on the resource commitment required to gain a faithful understanding of a model. Another interpretation of that result is that participants could freely choose how much time they wanted to spend, and therefore time spent could also re<sup>fl</sup>ect their motivation to solve the comprehension tasks. In general, there is always a tradeoff between time spent and correctness of solution in cognitive tasks (referred to as speedaccuracy tradeoff; e.g. [4]). So, as speed was not a set target, participants could maximize accuracy if they wanted to.

Our results regarding comprehension ef<sup>fi</sup>ciency are in line with other conceptual modeling experiments to a certain extent. For instance, Batra and Davis [2] found no time differences when investigating performance differences between novices and experts, although there was a signi<sup>fi</sup>cant difference in quality of the outcome. Also Reijers et al. [58] found that the treatment “color highlighting” had a signi<sup>fi</sup>cant effect on understanding accuracy, but not on understanding speed. In turn, we believe that our <sup>fi</sup>ndings, coupled with the body of work to date, clearly point to a gap in understanding the reasons for differences in model comprehension ef<sup>fi</sup>ciency, and what the consequences are for the effective use of conceptual models for systems analysis and design.

Regarding perceived cognitive dif<sup>fi</sup>culty, we note that the reported effects of our independent variables on perceived control <sup>fl</sup>ow comprehension dif<sup>fi</sup>culty were similar to those on comprehension accuracy but somewhat different from those on perceived cognitive load of the task as a whole. These <sup>fi</sup>ndings suggest that the perceived control <sup>fl</sup>ow comprehension dif<sup>fi</sup>culty scale measures objective com prehension dif<sup>fi</sup>culty more closely, while perceived cognitive load might re<sup>fl</sup>ect a more subjective rating of the general task setting.

Our experimental setting also allowed us to clarify whether notational ef<sup>fi</sup>ciency is an object property and therefore characteristic of any notation, or dependent on user evaluations. Our results indicate that individu al ratings of symbol design were relevant for process model comprehension over and above the actual design of the symbols. Several theories can assist in providing an explanation for this result.

First, research on perception demonstrated in various ways how individual's preferences and motivational states can impact visual processing; so to say people “see what they want to see” [1]. Although most perceptional processes are bottom-up (the brain turns information from sense organs as eyes into a perception), still, top-down in<sup>fl</sup>uences (driven by higher-level cognitive processes as the users attitude towards the symbols used) can have a great impact and can lead to perceptional biases (e.g. hills appears steeper than they actually are) or even phenomena such as unattentional blindness [65]. In such a case, a negative <sup>fi</sup>rst impression of the symbols' design could lead to higher cognitive effort in the perception process needed for solving the comprehension tasks, leading both to lower performance and lower symbol evaluation. Additionally, differences in users' judgments of the symbols as well as in actual performances could re<sup>fl</sup>ect the fact that the ef<sup>fi</sup>ciency of visual perception can vary signi<sup>fi</sup>cantly between individuals (see e.g. [77]).

In addition to interpretations on the perceptional point of view, our results can also be interpreted through the lens of motivational theories. Research has shown that individual attitudes as achievement motivation or subjective dif<sup>fi</sup>culty mediate the relationship between objective task dif<sup>fi</sup>- culty and performance [9,20]. For instance, if individuals perceive increased task dif<sup>fi</sup>culty, they usually invest higher mental effort to protect performance as long as the tasks doesn't seem impossible to them. So, worse symbol design making the task more dif<sup>fi</sup>cult per se, could not only lead to a performance loss, but also to an increase of mental effort in motivated participants resulting in similar performance of the experimental groups. However, those individuals who would have had the subjective impression that the symbol design was bad could have been demotivated and performed worse. The evidence in the present analysis is too weak for any real conclusions regarding this issue, however. Future research could include the measurement of intrinsic motivation to clarify the mechanism why individual perceptions of symbol design have a stronger in<sup>fl</sup>uence on process model comprehension than the symbol design itself.

Finally, we note that our results con<sup>fi</sup>rm the relevance of secondary object attributes (perceptions of primary attributes) to understanding object-related behaviors [14]. Recker et al. [55] showed how perceptions of process modeling grammar primary notation characteristics determined behavioral evaluations of the process modeling grammar, such as perceived usefulness and perceived ease of use. While they found that both primary and secondary (perceptual) attributes of the primary notation of the grammar mattered to these evaluations, our results show that in terms of secondary notation, the secondary attributes are important over and above the primary attributes of visual design.

## 8. Implications and limitations

## 8.1. Implications for research

We identify several important theoretical and empirical <sup>fi</sup>ndings in our research.

First, this study is the <sup>fi</sup>rst to operationalize and measure four principles of effective visual notation design. Our factor analysis of the user evaluations of the symbols con<sup>fi</sup>rm that the criteria perceptual discriminability, semantic transparency, pop out and aesthetics are perceived as independent dimensions. Our work thus provides a measurement instrument that can be utilized in future studies on model comprehension; for instance, in studies that examine the interaction effects between ontological (primary notation) principles and visual (secondary notation) principles in conceptual models.

Future research could further extend our approach to investigate cognitive criteria in more detail and identify symbols that represent speci<sup>fi</sup>c criteria very well and very poorly, and subsequently determine their in<sup>fl</sup>uence on comprehension. However, our selection of symbols showed that it is very dif<sup>fi</sup>cult to <sup>fi</sup>nd symbols, which represent these criteria independently and it might not be possible to <sup>fi</sup>nd symbols that, for instance, are semantically transparent but not aesthetic.

Our paper additionally encourages the exploration of the amount of variance attributed to individual vs. symbol design factors. Future research could tease out the relevance of personal vs. language factors by measuring further aspects of individual attitudes or perceptional abilities.

Our work uses cognitive load theory and the limitations of working memory to provide a theoretical explanation of the cognitive effectiveness of different routing symbols. The results provide evidence that inef-<sup>fi</sup>cient design of symbols may place extra extraneous cognitive load on end user. Our results therefore add strength to a growing body of empirical work that applies cognitive load theory to the context of understanding visual models. While subjective measurement of cognitive load has been established as an ef<sup>fi</sup>cient and reliable instrument [46], it is desirable to adopt techniques developed in cognitive psychology to the study of conceptual model comprehension. First, there is the option to measure cognitive load based on secondary task performance, in which a distracting task is imposed over the original task [46]. Second, brain image processing and other techniques can be applied to directly measure cognitive load on the neurophysiological level. It would be valuable to study these instruments for model comprehension tasks, which might reveal more detailed insights into cognitive load effects in this domain.

## 8.2. Implications for practice

We believe our <sup>fi</sup>ndings inform speci<sup>fi</sup>cally modeling grammar and guideline development. Standards and descriptions for modeling grammars often do not give a reason why speci<sup>fi</sup>c symbols are chosen. Our study shows the relevance of visual symbol design and aims to motivate future modeling grammar developments to include user evaluation procedures for symbol choice as well. Other areas dependent on the use of symbols for instance conduct detailed user evaluations of different symbol variations as size, orientation, thickness of lines (see for example [64] for a study on prohibitive symbols). Such user evaluations bear the potential to reveal symbol design issues. The design of single symbols is important, but also their combination in a symbol set, so that visual discriminability of symbols can be warranted. Our study shows that the selection of shapes and symbols will affect whether models created with a modeling grammar will be easy and accurately understandable. To achieve, for instance, semantically transparent symbol design, it can be reasonable to use well known symbols known from other domains (e.g., mathematics) to allow for positive transfer effects.

The <sup>fi</sup>ndings from our study also suggest implications for the choice of a particular modeling notation. For instance, our experiment shows that the YAWL notation suffers from weak discriminability of the XOR and AND routing symbols. The assessments of the other symbols might be used as a source of inspiration for notational rework. Beyond this observation, we do not want to make direct statements about the underlying process modeling grammars used for our experimental routing symbols for two reasons. First, we sometimes had to choose one option when a modeling grammar offered several ones (e.g., in BPMN there are various options for XOR routing symbols). Second, we only considered the routing elements in our experiment. Dimensions such as visual discriminability though have to be considered relative to the whole set of symbols offered by a notation. As we focused on a subset of the symbols of each grammar, our study would not be able to re<sup>fl</sup>ect upon weaknesses outside this subset or between the considered symbols and the ignored ones.

## 8.3. Limitations

We now discuss potential threats to validity and how we addressed them in the experiment. These limitations constrain the interpretation of our results to the context in which we gathered the data.

The participants of our study were students who were familiar with process modeling in general, although they were not experts in this area. The results might differ if the experiment is replicated with experts in business process modeling or with experts with a stronger software engineering background. However, as the participants had received training in information technology, their level of modeling experience was likely to be equivalent to those of typical business users of process models in many organizations. A recent study even found graduate students to perform better in a process model comprehension experiment [59]. Also, our study concerned basic cognitive principles of visual design and comprehension, and would have been confounded by using participants with high level of domain knowledge as these participants would have relied on background domain knowledge to answer the comprehension tasks; which would have obscured the effects of the visual designs [47]. Still, future research could investigate the different cognitive demands and preferences of experts and novices for symbol choice. Here, it may well be the case that certain designs are better for untrained people than trained experts who know what to look for.

In designing our treatments, we had to trade off internal and external validity in light of ecological validity considerations. We chose for a treatment with symbols from real modeling languages and with models with realistic textual descriptions to warrant ecological validity. While the results are in line with our predictions and showed in the correct direction, the use of realistic models over models with arti<sup>fi</sup>cially in<sup>fl</sup>ated visual differences probably contributed to the rather low level of explained variance we observed in our results. This is because, for instance, users could have been able to partially derive information of symbols from the context or the semantic content of a process model. For instance, for the construction of a loop an XOR symbol is needed but not an AND symbol.

Finally, we discuss the experimental task order as a potential source of bias. In our study, participants had to rate the control <sup>fl</sup>ow symbols after completing the model comprehension tasks. To determine if they might have given different answers when asked about the visual design of the symbols without performing the comprehension tasks, we gathered additional data points on symbol rating through a follow-up study with a student population comparable with the initial population (viz., students in the same courses in the following year). In this follow-up study, students only rated the symbols without having to perform a comprehension test. A comparison of the symbol evaluations with and without comprehension tasks is displayed visually in Appendix E. A correlation analysis revealed high similarity of the variances observed in the ratings across the two groups (r =0.94, p=0.000), a further MANCOVA analysis showed no interaction effect between symbol ratings and point of time of rating. These results indicate that our study results about the in<sup>fl</sup>uence of symbol ratings on the variance in model comprehension remains valid, albeit we note a slight bias exhibited by the experiment task order, in that ratings were slightly lowered when performed after comprehension tasks. Still, we do not see evidence that this bias could have in<sup>fl</sup>uenced the regression results in any way, as this bias was consistent over all evaluations.

## 9. Conclusion

Our study provides empirical evidence of the importance of symbol design on (process) model comprehension. We found that notational characteristics such as perceptual discriminability and pop out are signi<sup>fi</sup>cantly associated with perceived cognitive load and model comprehension accuracy but not comprehension ef<sup>fi</sup>ciency.

In a broader sense, the results provide evidence for the utility of the theory of effective visual design of notations to the study of process modeling in practice and the management of process modeling initiatives in practice. In turn, our research adds to the growing body of experimental research on conceptual modeling practices, and adds to the inventory of relevant theories, complementing relevant, established principles based on ontological considerations [47], multimedia learning considerations [18] and secondary notation considerations [58]. The cumulative tradition of research of these studies, in turn, advances our understanding

## Appendix A. Example of model with comprehension questions

of the issues and challenges in an important <sup>fi</sup>eld of information systems practice, the effective use of modeling notations for the analysis and design of organizational and technological systems.

## Acknowledgements

Dr. Recker's contributions to this research have been supported by a grant from the Australian Research Council (ARC DE120100776) and by a Fellowship from the Alexander-von-Humboldt Foundation.

Table A.1  
Example of model with comprehension questions.

<table><tr><td></td><td></td></tr><tr><td rowspan="8"></td><td>Concurrency 1: “Prepare instructions for use” and “prepare manual” can be executed at the same point of time. (correct, close)</td></tr><tr><td>Concurrency 2: “Evaluate add-on products” and “send newsletter” can be executed in parallel. (wrong, distant)</td></tr><tr><td>Exclusiveness 1: In one process instance “develop a service plan” as well as “determine support level” can be executed. (correct, close)</td></tr><tr><td>Exclusiveness 2: The process steps “define after sales management objectives” and “organize event” are mutually exclusive. (wrong, distant)</td></tr><tr><td>Sequence 1: If “conduct market study” as well as “elaborate add-on services” are executed in a process instance, then “conduct market study” has to be finalized before “elaborate add-on services” can start. (wrong, distant)</td></tr><tr><td>Sequence 2: If “define market objectives” as well as “analyze new potential benefits” are executed in a process instance, then “define market objectives” is executed before “analyze new potential benefits”. (wrong, close)</td></tr><tr><td>Repetition 1: “Document customer satisfaction” can be executed more often than “define after sales management objectives”. (correct, distant)</td></tr><tr><td>Repetition 2: In each process instance “acquire new customers” is executed exactly as often as “initiate continuous customer support”. (correct, close)</td></tr></table>

## Appendix B. Subjective dif<sup>fi</sup>culty of control <sup>fl</sup>ow comprehension

(5 point scale from “totally disagree” to “totally agree”). [α=0.765]

It was easy to perceive in the models, which process steps …

• …are executed in a loop.

• …are executed in parallel (AND).

• … are mutually exclusive (XOR).

• … are executed in sequence.

## Appendix C. User evaluation of symbols

In the following, we ask you to rate the visual appearance of the AND as well as XOR symbols: [Cronbach's Alphas in brackets for XOR and AND items]

• Perceptual Popout $[ \alpha _ { \mathrm { X O R } } = 0 . 9 3 / \alpha _ { \mathrm { A N D } } = 0 . 9 3 ]$

o XOR/AND-symbols can be found quickly in a model.

o XOR/AND-symbols are easy to <sup>fi</sup>nd in a model.

o XOR/AND-symbols can be recognized immediately in a model.

o It is easy to recognize XOR/AND-symbols in a model.

• Semantic transparency $[ \alpha _ { \mathrm { X O R } } = 0 . 8 7 / \alpha _ { \mathrm { A N D } } = 0 . 8 9 ]$

o XOR/AND-symbols are intuitively understandable in a model.

o Even without explanation it is clear what a XOR/AND-symbol represents.

o One doesn't have to learn the meaning of the XOR/AND-symbol, to understand it.

• Aesthetics $[ \alpha _ { \mathrm { X O R } } = 0 . 9 3 / \alpha _ { \mathrm { A N D } } = 0 . 9 1 ]$

o The XOR/AND-symbol is optically pleasing.

o The XOR/AND-symbol is visually appealing.

o The XOR/AND-symbol is visually esthetic.

o The XOR/AND-symbol is well-designed.

• Visual discriminability [α = 0.94]

AND and XOR symbols are …..

o …dif<sup>fi</sup>cult to distinguish in a model.

o …well to distinguish in a model.

o …easy to confuse in a model.

o …easy to discriminate in a model.

## Appendix D. Factor analysis for symbol evaluation

## Table D.1

Factor loadings for XOR symbol evaluation items (PCA with varimax rotation).

<table><tr><td>Symbol evaluation items (XOR)</td><td>Factor 1 – perceptual pop out</td><td>Factor 2 – aesthetics</td><td>Factor 3 – semantic transparency</td></tr><tr><td>The XOR-symbol is visually aesthetic. (XOR, aesthetics)</td><td>0.17</td><td>0.86</td><td>0.27</td></tr><tr><td>The XOR-symbol is optically pleasing. (XOR, aesthetics)</td><td>0.40</td><td>0.77</td><td>0.24</td></tr><tr><td>The XOR-symbol is well-designed. (XOR, aesthetics)</td><td>0.43</td><td>0.74</td><td>0.25</td></tr><tr><td>The XOR-symbol is visually appealing. (XOR, aesthetics)</td><td>0.36</td><td>0.80</td><td>0.33</td></tr><tr><td>XOR-symbols can be found quickly in a model. (XOR, pop out)</td><td>0.83</td><td>0.24</td><td>0.28</td></tr><tr><td>XOR-symbols are easy to find in a model. (XOR, pop out)</td><td>0.86</td><td>0.27</td><td>0.22</td></tr><tr><td>It is easy to recognize XOR-symbols in a model. (XOR, pop out)</td><td>0.81</td><td>0.33</td><td>0.16</td></tr><tr><td>XOR-symbols can be recognized immediately in a model. (XOR, pop out)</td><td>0.86</td><td>0.30</td><td>0.18</td></tr><tr><td>Even without explanation it is clear what a XOR-symbol represents. (XOR, semantic transparency)</td><td>0.28</td><td>0.31</td><td>0.79</td></tr><tr><td>XOR-symbols are intuitively understandable in a model. (XOR, semantic transparency)</td><td>0.27</td><td>0.24</td><td>0.80</td></tr><tr><td>One doesn&#x27;t have to learn the meaning of the XOR-symbol, to understand it. (XOR, semantic transparency)</td><td>0.12</td><td>0.23</td><td>0.89</td></tr><tr><td>Eigenvalue</td><td>3.47</td><td>3.05</td><td>2.53</td></tr><tr><td>Percentage of variance</td><td>31.55</td><td>27.68</td><td>23.03</td></tr></table>

Total variance accounted for=82%.  
Item loadings at or above 0.50 are shown in bold for clarity.

Table D.2  
Factor loadings for AND symbol evaluation items (PCA with varimax rotation).

<table><tr><td>Symbol evaluation items (AND)</td><td>Factor 1 – perceptual pop out</td><td>Factor 2 – aesthetics</td><td>Factor 3 – semantic transparency</td></tr><tr><td>The AND-symbol is visually aesthetic. (AND, aesthetics)</td><td>0.25</td><td>0.83</td><td>0.23</td></tr><tr><td>The AND-symbol is optically pleasing. (AND, aesthetics)</td><td>0.43</td><td>0.76</td><td>0.27</td></tr><tr><td>The AND-symbol is well-designed. (AND, aesthetics)</td><td>0.41</td><td>0.68</td><td>0.29</td></tr><tr><td>The AND-symbol is visually appealing. (AND, aesthetics)</td><td>0.34</td><td>0.82</td><td>0.27</td></tr><tr><td>AND-symbols can be found quickly in a model. (AND, pop out)</td><td>0.83</td><td>0.35</td><td>0.23</td></tr><tr><td>AND-symbols are easy to find in a model. (AND, pop out)</td><td>0.82</td><td>0.33</td><td>0.27</td></tr><tr><td>It is easy to recognize AND-symbols in a model. (AND, pop out)</td><td>0.78</td><td>0.31</td><td>0.28</td></tr><tr><td>AND-symbols can be recognized immediately in a model. (AND, pop out)</td><td>0.81</td><td>0.32</td><td>0.29</td></tr><tr><td>Even without explanation it is clear what a AND-symbol represents. (AND, semantic transparency)</td><td>0.31</td><td>0.35</td><td>0.77</td></tr><tr><td>AND-symbols are intuitively understandable in a model. (AND, semantic transparency)</td><td>0.31</td><td>0.37</td><td>0.77</td></tr><tr><td>One doesn&#x27;t have to learn the meaning of the AND-symbol, to understand it. (AND, semantic transparency)</td><td>0.22</td><td>0.15</td><td>0.89</td></tr><tr><td>Eigenvalue</td><td>3.38</td><td>3.10</td><td>2.54</td></tr><tr><td>Percentage of variance</td><td>30.74</td><td>28.21</td><td>23.05</td></tr></table>

Total variance accounted for=82%.  
Item loadings at or above 0.50 are shown in bold.

Table D.3

Factor loadings for all symbol evaluation items (PCA with varimax rotation).

<table><tr><td></td><td>Factor 1 - AND-symbol</td><td>Factor 2 - XOR perceptual discriminability and pop out</td><td>Factor 3 - XOR aesthetics</td><td>Factor 4 - XOR-semantic transparency</td><td>Factor 5 - subjective difficulty of control flow comprehension</td></tr><tr><td>It was easy to perceive in the models, which process steps are executed in a loop. (subjective difficulty of control flow comprehension)</td><td>0.21</td><td>0.16</td><td>0.14</td><td>0.10</td><td>0.75</td></tr><tr><td>It was easy to perceive in the models, which process steps are executed in parallel (AND). (subjective difficulty of control flow comprehension)</td><td>0.25</td><td>0.18</td><td>0.02</td><td>0.17</td><td>0.78</td></tr><tr><td>It was easy to perceive in the models, which process steps are mutually exclusive (XOR). (subjective difficulty of control flow comprehension)</td><td>0.10</td><td>0.15</td><td>0.24</td><td>0.17</td><td>0.75</td></tr><tr><td>It was easy to perceive in the models, which process steps are executed in sequence. (subjective difficulty of control flow comprehension)</td><td>0.09</td><td>0.14</td><td>-0.03</td><td>-0.04</td><td>0.74</td></tr><tr><td>AND and XOR symbols are difficult to distinguish in a model (recoded). (perceptual discriminability)</td><td>0.17</td><td>0.81</td><td>0.09</td><td>-0.00</td><td>0.16</td></tr><tr><td>AND and XOR symbols are well to distinguish in a model. (perceptual discriminability)</td><td>0.24</td><td>0.82</td><td>0.08</td><td>0.02</td><td>0.22</td></tr><tr><td>AND and XOR symbols are easy to confuse in a model. (perceptual discriminability)</td><td>0.19</td><td>0.81</td><td>0.10</td><td>-0.01</td><td>0.18</td></tr><tr><td>AND and XOR symbols are easy to discriminate in a model. (perceptual discriminability)</td><td>0.19</td><td>0.84</td><td>0.08</td><td>0.06</td><td>0.16</td></tr><tr><td>The XOR-symbol is visually aesthetic. (XOR, aesthetics)</td><td>0.22</td><td>0.12</td><td>0.82</td><td>0.23</td><td>0.05</td></tr><tr><td>The XOR-symbol is optically pleasing. (XOR, aesthetics)</td><td>0.07</td><td>0.35</td><td>0.77</td><td>0.27</td><td>0.12</td></tr><tr><td>The XOR-symbol is well-designed. (XOR, aesthetics)</td><td>0.07</td><td>0.35</td><td>0.73</td><td>0.31</td><td>0.09</td></tr><tr><td>The XOR-symbol is visually appealing. (XOR, aesthetics)</td><td>0.19</td><td>0.31</td><td>0.76</td><td>0.33</td><td>0.14</td></tr><tr><td>XOR-symbols can be found quickly in a model. (XOR, pop out)</td><td>0.14</td><td>0.69</td><td>0.30</td><td>0.40</td><td>0.05</td></tr><tr><td>XOR-symbols are easy to find in a model. (XOR, pop out)</td><td>0.17</td><td>0.71</td><td>0.35</td><td>0.31</td><td>0.11</td></tr><tr><td>It is easy to recognize XOR-symbols in a model. (XOR, pop out)</td><td>0.16</td><td>0.71</td><td>0.38</td><td>0.21</td><td>0.13</td></tr><tr><td>XOR-symbols can be recognized immediately in a model. (XOR, pop out)</td><td>0.20</td><td>0.69</td><td>0.37</td><td>0.30</td><td>-0.02</td></tr><tr><td>Even without explanation it is clear what a XOR-symbol represents. (XOR, semantic transparency)</td><td>0.18</td><td>0.23</td><td>0.34</td><td>0.75</td><td>-0.01</td></tr><tr><td>XOR-symbols are intuitively understandable in a model. (XOR, semantic transparency)</td><td>0.19</td><td>0.16</td><td>0.28</td><td>0.72</td><td>0.28</td></tr><tr><td>The meaning of the XOR-symbol is easy to recognize based on its visual design. (XOR, semantic transparency)</td><td>0.17</td><td>0.46</td><td>0.44</td><td>0.43</td><td>0.11</td></tr><tr><td>One doesn't have to learn the meaning of the XOR-symbol, to understand it. (XOR, semantic transparency)</td><td>0.20</td><td>0.05</td><td>0.28</td><td>0.78</td><td>0.14</td></tr><tr><td>The AND-symbol is visually aesthetic. (AND, aesthetics)</td><td>0.65</td><td>0.08</td><td>0.55</td><td>0.02</td><td>0.04</td></tr><tr><td>The AND-symbol is optically pleasing. (AND, aesthetics)</td><td>0.73</td><td>0.14</td><td>0.49</td><td>-0.01</td><td>0.16</td></tr><tr><td>The AND-symbol is well-designed. (AND, aesthetics)</td><td>0.69</td><td>0.16</td><td>0.40</td><td>0.04</td><td>0.20</td></tr><tr><td>The AND-symbol is visually appealing. (AND, aesthetics)</td><td>0.71</td><td>0.12</td><td>0.53</td><td>0.03</td><td>0.10</td></tr><tr><td>AND-symbols can be found quickly in a model. (AND, pop out)</td><td>0.68</td><td>0.52</td><td>0.19</td><td>0.02</td><td>0.14</td></tr><tr><td>AND-symbols are easy to find in a model. (AND, pop out)</td><td>0.73</td><td>0.46</td><td>0.16</td><td>0.01</td><td>0.11</td></tr><tr><td>It is easy to recognize AND-symbols in a model. (AND, pop out)</td><td>0.68</td><td>0.44</td><td>0.12</td><td>0.05</td><td>0.19</td></tr><tr><td>AND-symbols can be recognized immediately in a model. (AND, pop out)</td><td>0.71</td><td>0.46</td><td>0.14</td><td>0.02</td><td>0.18</td></tr><tr><td>Even without explanation it is clear what a AND-symbol represents. (AND, semantic transparency)</td><td>0.81</td><td>0.07</td><td>0.00</td><td>0.29</td><td>0.04</td></tr><tr><td>AND-symbols are intuitively understandable in a model. (AND, semantic transparency)</td><td>0.78</td><td>0.05</td><td>0.03</td><td>0.36</td><td>0.19</td></tr><tr><td>The meaning of the AND-symbol is easy to recognize based on its visual design. (AND, semantic transparency)</td><td>0.76</td><td>0.28</td><td>0.08</td><td>0.11</td><td>0.11</td></tr><tr><td></td><td>Factor 1 – AND-symbol</td><td>Factor 2 – XOR perceptual discriminability and pop out</td><td>Factor 3 – XOR aesthetics</td><td>Factor 4 – XOR-semantic transparency</td><td>Factor 5 – subjective difficulty of control flow comprehension</td></tr><tr><td>One doesn't have to learn the meaning of the AND-symbol, to understand it. (AND, semantic transparency)</td><td>0.74</td><td>0.03</td><td>-0.18</td><td>0.36</td><td>0.09</td></tr><tr><td>Eigenvalue</td><td>6.90</td><td>6.41</td><td>4.54</td><td>3.03</td><td>2.83</td></tr><tr><td>Percentage of variance</td><td>21.57</td><td>20.03</td><td>14.17</td><td>9.48</td><td>8.85</td></tr></table>

Total variance accounted for=74.10%.  
Item loadings at or above 0.50 are shown in bold

## Appendix E. Symbol evaluation

![](/api/attachments/MG6V5BSA/fulltext/images/7b4d07eec21634f9fb19287084a4e8be35d21d761f7144b135f76914ab79d6fd.jpg)  
Fig. 3. Results of symbol rating in experimental and post-hoc group.

## References

[1] E. Balcetis, D. Dunning, See what you want to see: motivational in<sup>fl</sup>uences on visual perception, Journal of Personality and Social Psychology 91 (4) (2006) 612–625.

[2] D. Batra, J.G. Davis, Conceptual data modelling in database design: similarities and differences between expert and novice designers, International Journal of Man– machine Studies 37 (1) (1992) 83–101.

[3] P.H. Bloch, Seeking the ideal form: product design and consumer response, The Journal of Marketing 59 (3) (1995) 16–29.

[4] R. Bogacz, E.-J. Wagenmakers, B.U. Forstmann, S. Nieuwenhuis, The neural basis of the speed–accuracy tradeoff, Trends in Neurosciences 33 (1) (2010) 10–16.

[5] P.C. Bottger, M.A. Woods, Different determinants of task persistence and growth satisfaction: affective responses to performance, planning and job characteristics Australian Journal of Management 13 (2) (1988) 303–317.

[6] P.L. Bowen, R.A.O. Farrell, F.H. Rohde, An empirical investigation of end-user query development: the effects of improved model expressiveness vs . complexity, Information Systems Research 20 (4) (2009) 565–584.

[7] BPMI.org, OMG, Business Process Modeling Notation Speci<sup>fi</sup>cation. Final Adopted Speci<sup>fi</sup>cation, in, Object Management Group, 2006.

[8] A. Burton-Jones, Y. Wand, R. Weber, Guidelines for empirical evaluations of conceptual modeling grammars, Journal of the Association for Information Systems 10 (6) (2009) 495–532.

[9] R.L. Capa, M. Audiffren, S. Ragot, The interactive effect of achievement motivation and task difficulty on mental effort. International Journal of Psychophysiology 70 (2) (2008) 144–150.

[10] T.D. Cook, D.T. Campbell, Quasi-Experimentation: Design and Analysis Issues, Houghton Mif<sup>fl</sup>in, Boston, Massachusetts, 1979.

[11] K. Corral, D. Schuff, R.D. St, The impact of alternative diagrams on the accuracy of recall: a comparison of star-schema diagrams and entity-relationship diagrams, Decision Support Systems 42 (2006) 450–468.

[12] N. Cowan, The magical mystery four: how is working memory capacity limited, and why? Current Directions in Psychological Science 19 (1) (2010) 51–57.

[13] W.H. Crown, Statistical Models for the Social and Behavioral Sciences: Multiple Regression and Limited-Dependent Variable Models, Praeger, Westport, 1998.

[14] G.W. Downs Jr., L.B. Mohr, Conceptual issues in the study of innovation, Administrative Science Ouarterly 21 (4) (1976) 700–714.

[15] P. Ef<sup>fi</sup>nger, M. Siebenhaller, M. Kaufmann, An Interactive Layout Tool for BPMN, in: IEEE Conference on Commerce and Enterprise Computing, IEEE, Vienna, Austria, 2009, pp. 399–406.

[16] D. Farrar, R. Glauber, Multicollinearity in regression analysis: the problem revisited, The Review of Economics and Statistics 49 (1) (1967) 92–107.

[17] A. Gemino, Y. Wand, A framework for empirical evaluation of conceptual modeling techniques, Requirements Engineering 9 (4) (2004) 248–260.

[18] A. Gemino, Y. Wand, Complexity and clarity in conceptual modeling: comparison of mandatory and optional properties, Data & Knowledge Engineering 55 (3) (2005) 301–326.

[19] M. Genero, G. Poels, M. Piattini, De<sup>fi</sup>ning and validating metrics for assessing the understandability of entity-relationship diagrams, Data & Knowledge Engineering 64 (3) (2008) 534–557.

[20] M.S. Humphreys, W. Revelle, Personality, motivation, and performance: a theory of the relationship between individual differences and information processing, Psychological Review 91 (2) (1984) 153–184

[41] J.C. Nordbotten, M.E. Crosby, The effect of graphic style on data model interpretation, Information Systems Journal 9 (2) (1999) 139–155.

[21] V. Khatri, I. Vessey, V. Ramesh, P. Clay, P. Sung-Jin, Understanding conceptual schemas: exploring the role of application and IS domain knowledge, Information Systems Research 17 (1) (2006) 81–99.

[22] S. Khemlani, P.N. Johnson-Laird, Disjunctive illusory inferences and how to eliminate them, Memory & Cognition 37 (5) (2009) 615–623.

[23] B. Kiepuszewski, A.H.M. ter Hofstede, W.M.P. van der Aalst, Fundamentals of control <sup>fl</sup>ow in work<sup>fl</sup>ows, Acta Informatica 39 (3) (2003) 143–209.

[24] E. Kindler, On the semantics of EPCs: resolving the vicious circle, Data & Knowledge Engineering 56 (1) (2005) 23–40.

[25] P.A. Kirschner, Cognitive load theory: implications of cognitive load theory on the design of learning, Learning and Instruction 12 (1) (2002) 1–10.

[26] N. Kock, J. Verville, A. Danesh-Pajou, D. DeLuca, Communication <sup>fl</sup>ow orientation in business process modeling and its effect on redesign success: results from a <sup>fi</sup>eld study, Decision Support Systems 46 (2) (2009) 562–575.

[27] K. Kotovsky, J.R. Hayes, H.A. Simon, Why are some problems hard? Evidence from Tower of Hanoi, Cognitive Psychology 17 (2) (1985) 248–294.

[28] J.H. Larkin, H.A. Simon, Why a diagram is (sometimes) worth ten thousand words, Cognitive Science 11 (1) (1987) 65–100.

[29] T. Lavie, N. Tractinsky, Assessing dimensions of perceived visual aesthetics of web sites \$, Information Systems 60 (2004) 269–298.

[30] D. Leutner, C. Leopold, E. Sum<sup>fl</sup>eth, Cognitive load and science text comprehension: effects of drawing and mentally imagining text content, Computers in Human Behavior 25 (2) (2009) 284–289.

[31] A. Maes, G. Poels, Evaluating quality of conceptual modelling scripts based on user perceptions, Data & Knowledge Engineering 63 (3) (2007) 701–724.

[32] N. Marcus, M. Cooper, J. Sweller, Understanding instructions, Journal of Educational Psychology 88 (1) (1996) 49–63.

[33] S.J.P. McDougall, M.B. Curry, O.D. Bruijn, Measuring symbol and icon characteristics: norms for concreteness, complexity, meaningfulness, familiarity, and semantic distance for 239 symbols, Behavior Research Methods, Instruments, & Computers 31 (3) (1999) 487–519.

[34] J. Mendling, J. Recker, H.A. Reijers, On the usage of labels and icons in business process modeling, International Journal of Information System Modeling and Design 1 (2) (2010) 40–58.

[35] J. Mendling, H. Reijers, W.M.P. van der Aalst, Seven process modeling guidelines (7PMG), Information and Software Technology 52 (2) (2010) 127–136.

[36] J. Mendling, H.A. Reijers, J. Recker, Activity labeling in process modeling: empirical insights and recommendations, Information Systems 35 (4) (2010) 467–482.

[38] G.A. Miller, The magical number seven, plus or minus two: some limits on our capacity for processing information, Psychological Review 63 (1956) 81–97.

[39] D.L. Moody, The “physics” of notations: toward a scienti<sup>fi</sup>c basis for constructing visual notations in software engineering, IEEE Transactions on Software Engineering 35 (6) (2009) 756–779.

[40] D.C.L. Ngo, Measuring the aesthetic elements of screen designs, Displays 22 (3) (2001) 73–78.

[42] J.C. Nunnally, I.H. Bernstein, Psychometric Theory, 3rd ed. McGraw-Hill, New York New York 1994

[43] Object Management Group, BPMN 2.0 by Example, in, 2010.

[44] OMG, Business Process Modeling Notation, V1.2, in, Object Management Group, 2009.

[45] C. Ouyang, W.M.P. van der Aalst, M. Dumas, A.H.M. ter Hofstede, J. Mendling, From business process models to process-oriented software systems, ACM Transactions on Software Engineering Methodology 19 (1) (2009) 2–37.

[46] F. Paas, J.E. Tuovinen, H. Tabbers, V. Gerven, P.W. M, Cognitive load measurement as a means to advance cognitive load theory, Educational Psychologist 38 (2003) 63–72.

[47] J. Parsons, An experimental study of the effects of representing property precedence on the comprehension of conceptual schemas, Journal of the Association for Information Systems 12 (6) (2011) 401–422.

[48] S. Patig, V. Casanova-Brito, B. Vögeli, IT Requirements of Business Process Management in Practice — An Empirical Study, in: R. Hull, J. Mendling, S. Tai (Eds.), Business Process Management, Springer, Berlin/Heidelberg, 2010, pp. 13–28.

[49] M. Petre, Why looking isn't always seeing: readership skills and graphical programming, Communications of the ACM 38 (6) (1995) 33–44.

[50] M. Petre, Cognitive dimensions ‘beyond the notation’, Journal of Visual Languages & Computing 17 (4) (2006) 292–301.

[51] H.C. Purchase, D. Carrington, J.-A. Allder, Empirical evaluation of aesthetics-based graph layout, Empirical Software Engineering 7 (3) (2002) 233–255.

[52] P.T. Quinlan, Visual feature integration theory: past, present and future, Psychological Bulletin 129 (5) (2003) 643–673.

[53] J. Recker, A. Dreiling, The effects of content presentation format and user characteristics on novice developers' understanding of process models, Communications of the Association for Information Systems 28 (6) (2011) 65–84.

[54] J. Recker, M. Rosemann, A measurement instrument for process modeling research: development, test and procedural model, Scandinavian Journal of Information Systems 22 (2) (2010) 3–30.

[55] J. Recker, M. Rosemann, P. Green, M. Indulska, Do ontological de<sup>fi</sup>ciencies in modeling grammars matter? Management Information Systems Quarterly 35 (1) (2011).

[56] J. Recker, M. Rosemann, M. Indulska, P. Green, Business process modeling: a comparative analysis, Journal of the Association for Information Systems 10 (4) (2009) 333–363.

[57] J. Recker, N. Safrudin, M. Rosemann, How novices design business processes, Information Systems 37 (6) (2012) 557–573.

[58] H.A. Reijers, T. Freytag, J. Mendling, A. Eckleder, Syntax highlighting in business process models, Decision Support Systems 51 (2011) 339–349.

[59] H.A. Reijers, J. Mendling, A study into the factors that in<sup>fl</sup>uence the understandability of business process models, IEEE Transactions on Systems, Man, and Cybernetics — Part A 41 (2011) 449–462.

[60] H.A. Reijers, J. Mendling, R.M. Dijkman, Human and automatic modularizations of process models to enhance their comprehension, Information Systems 36 (5) (2011) 881–897.

[61] J. Sarkkinen, H. Karsten, Verbal and visual representations in task redesign: how different viewpoints enter into information systems design discussions, Information Systems Journal 15 (3) (2005) 181–211.

[62] A.-W. Scheer, ARIS — Business Process Modeling, 3rd ed. Springer, Berlin, Germany, 2000.

[63] B.N. Schenkman, F. Jonsson, Aesthetics and preferences of web pages, Behaviour Information Technology 19 (5) (2000) 367–377.

[64] K.-K. Shieh, S.-M. Huang, Factors affecting preference ratings of prohibitive symbols, Applied Ergonomics 34 (6) (2003) 581–587.

[65] D. Simons, C. Chabris, Gorillas in our midst: sustained inattentional blindness for dynamic events, Perception 28 (9) (1999) 1059–1074.

[66] P. Soffer, Y. Wand, Goal-driven multi-process analysis, Journal of the Association for Information Systems 8 (3) (2007).

[67] A. Sonderegger, J. Sauer, The in<sup>fl</sup>uence of design aesthetics in usability testing: effects on user performance and perceived usability, Applied Ergonomics 41 (3) (2010) 403–410

[68] L. Stan, Enhanced ridge regressions, Mathematical and Computer Modelling 51 (5–6) (2010) 338–348.

[69] J. Sweller, Cognitive load during problem solving: effects on learning, Cognitive Science: A Multidisciplinary Journal 12 (2) (1988) 257–285.

[70] B.G. Tabachnick, L.S. Fidell, Using Multivariate Statistics, Pearson Education, Inc., Boston, 2007.

[71] N. Tractinsky, A.S. Katz, D. Ikar, What is beautiful is usable, Interacting With Computers 13 (2) (2000) 127–145.

[72] A. Treisman, G. Gelade, A feature-integration theory of attention, Cognitive Psychology 12 (1) (1980) 97–136.

[73] W.M.P. van der Aalst, A.H.M. ter Hofstede, YAWL: Yet Another Work<sup>fl</sup>ow Language, Information Systems 30 (4) (2005).

[74] H.M.V. Verbeek, W.M.P. van der Aalst, A.H.M. ter Hofstede, Verifying work<sup>fl</sup>ows with cancellation regions and OR-joins: an approach based on relaxed soundness and invariants, The Computer Journal 50 (3) (2007) 294–314.

[75] R.W. Veryzer, Aesthetic response and the in<sup>fl</sup>uence of design principles on product preferences, Advances in Consumer Research Volume 20 (1993) 224–228.

[76] I. Vessey, Cognitive <sup>fi</sup>t: a theory-based analysis of the graphs versus tables literature, Decision Sciences 22 (2) (1991) 219–240.

[77] E.K. Vogel, M.G. Machizawa, Neural activity predicts individual differences in visual working memory capacity, Nature 428 (6984) (2004) 748–751.

[78] Y. Wand, R. Weber, Research commentary: information systems and conceptual modeling — a research agenda, Information Systems Research 13 (4) (2002) 363–376.

[79] C. Ware, Information Visualization, 2 ed. Elsevier. Morgan Kaufmann, San Francisco, 2004.

[80] W. Winn, Encoding and retrieval of information in maps and diagrams, IEEE Transactions on Professional Communication 33 (3) (1990) 103–107.

Dr. Kathrin Figl is an Assistant Professor in the Institute for Information Systems and New Media at the Vienna University of Economics (WU). She received her Doctoral (awarded with the Dr. Maria Schaumayer Award) and two Master's in Information Systems and Psychology both with honours, from the University of Vienna, Most of her applied research and teaching focuses on the intersection between information systems and psychology, including research on information systems education, human-computer-interaction and cognitive aspects of modeling. In 2010 she was awarded the excellent teaching award from the Vienna University of Economics for her lecture on information systems. She has authored more than 40 papers, including four best paper awards, in peer-reviewed journals and conference proceedings.

Dr. Jan Recker is Alexander-von-Humboldt Fellow, Professor for Information Systems and Woolworths Chair of Retail Innovation at Queensland University of Technology, Brisbane, Australia. His research focuses on usage of process design in organizational practice as well as IT-enabled business transformations and business innovations. He has written over 100 books, journal articles and conference proceedings, including publications in MIS Quarterly, Journal of the Association for Information Systems, Information Systems, European Journal of Information Systems, Information & Management, Scandinavian Journal of Information Systems, Decision Support Systems and others. He is Senior Editor for the Journal of IT Theory and Application, Associate Editor for Communications of the AIS, a member of the editorial board of several international journals and serves on the program committee of various conferences

Jan Mendling is a Full Professor with the Institute for Information Business at Wirtschaftsuniversität Wien (WU Vienna), Austria. His research areas include Business Process Management, Conceptual Modelling and Enterprise Systems. He has published more than 100 research papers and articles, among others in ACM Transactions on Soft ware Engineering and Methodology, Information Systems, Data & Knowledge Engineering Decision Support Systems, Formal Aspects of Computing, and IFFF Transactions on Soft: ware Engineering. He is member of the editorial board of three international journals. His Ph.D. thesis has won the Heinz-Zemanek-Award of the Austrian Computer Society and the German Targion-Award for dissertations in the area of strategic information management. He is one of the founders of the Berlin BPM Community of Practice ( http://www.bpmb.de) and organizer of several academic events on process management. He was program co-chair of the International Conference on Business Process Management 2010.
