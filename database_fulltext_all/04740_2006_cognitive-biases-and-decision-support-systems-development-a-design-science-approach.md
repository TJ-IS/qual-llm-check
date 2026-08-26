---
otero_id: 4740
otero_key: "WDKEBQY2"
title: "Cognitive biases and decision support systems development: a design science approach"
authors: "Jene"
year: "2006"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.2006.00208.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cognitive biases and decision support systems development: a design science approach

David Arnott

Faculty of Information Technology, Monash University, Victoria 3800, Australia, email: david.arnott@infotech.monash.edu.au

Abstract. This paper presents design science research that aims to improve decision support systems (DSS) development in organizations. Evolutionary development has been central to DSS theory and practice for decades, but a significant problem for DSS analysts remains how to conceptualize the improvement of a decision task during evolutionary DSS development. The objective of a DSS project is to improve the decision process and outcome for a manager making an important decision. The DSS analyst needs to have a clear idea of the nature of the target decision task and a clear strategy of how to support the decision process. Existing psychological research was examined for help with the conceptualization problem, and the theory of cognitive bias is proposed as a candidate for this assistance. A taxonomy of 37 cognitive biases that codifies a complex area of psychological research is developed. The core of the project involves the construction of a design artefact – an evolutionary DSS development methodology that uses cognitive bias theory as a focusing construct, especially in its analysis cycles. The methodology is the major contribution of the project. The feasibility and effectiveness of the development methodology are evaluated in a participatory case study of a strategic DSS project where a managing director is supported in a decision about whether to close a division of a company.

Keywords: decision support systems, systems development, cognitive bias, behavioural decision theory, design science

## INTRODUCTION

Decision support systems (DSS) is the area of information systems (IS) devoted to supporting and improving human decision-making. The DSS field began in the early 1970s as a radical alternative to large-scale management IS (MIS). Over time, major changes in information technology (IT) have enabled new decision support movements. Financial modelling software and spreadsheets created a boom in personal DSS in the early 1980s; 5 years later, multi-dimensional modelling and online analytical procesing technology enabled the deployment of largescale executive IS (EIS). Advances in storage technology and data modelling in the mid-1990s led to the data warehousing and business intelligence movements (Arnott & Pervan, 2005). Despite this substantial technical progress, laboratory experiments investigating the influence of DSS on decision performance have reported mixed, often disappointing, outcomes (Benbasat & Nault, 1990). In contrast, the results from case study research show that a focus on decision-making and tailored support can lead to successful systems (e.g. Courbon, 1996; Igbaria et al., 1996; Botha et al., 1997). A persistent theme in descriptions of successful IS for managers is the use of evolutionary systems development methods (Poon & Wagner, 2001).

Evolutionary development has been central to DSS theory and practice for decades. Sprague & Carlson (1982, p. 132) argued, ‘DSS must evolve or grow to reach a “final” design because no one can predict or anticipate in advance what is required. The system can never be final; it must change frequently to track changes in the problem, user, and environment because these factors are inherently volatile’. As a result, the functionality of a DSS evolves over a series of development cycles where both the client and the systems analyst are active contributors to the shape, nature and logic of the system (Arnott, 2004). While there is universal acceptance of the value of evolutionary development for decision support projects, there is little advice available to system developers about how to proceed with evolutionary DSS development. The objective of a DSS project is usually to improve the decision process and outcome for a manager making an important decision. The DSS analyst needs to have a clear idea of the nature of the target decision task and a clear strategy of how to support the decision process. A persistent problem for analysts is how to conceptualize the aspects of the decision task that need improvement during the various iterations of the evolutionary development process. This problem is the focus of this paper.

System development is fundamentally a process of design. Hevner et al. (2004), in a discussion of the role of design theory in IS, clearly articulated the nature of the problem that DSS analysts face: ‘the existing knowledge base is often insufficient for design purposes and designers must rely on intuition, experience, and trial-and-error methods’ (p. 99). Given the strategic nature of most DSS to organizations, any guidance to help analysts cope with a trialand-error design situation could lead to more effective systems. It follows that because DSS is fundamentally about decision-making, a DSS analyst should have considerable knowledge about human decision processes and how to improve them. Further, DSS development methods should support the analyst’s strategies for decision improvement. This paper reports a design science project that attempts to provide guidance to analysts developing a DSS. It grounds this guidance in an important part of behavioural decision theory – the theory of cognitive bias. The outcome of the research project is a systems development methodology that is effective in developing strategic personal DSS.

The paper is organized as follows: first, the research method and design are presented. A feature of this section is the synthesis of a design science research method from previous studies and frameworks. Next, the theoretical background of the project in judgement and decision-making is defined. The development of a taxonomy of cognitive biases is an important contribution of this section. The fourth section presents the major contribution of the research project: a DSS development methodology that uses cognitive biases as a focusing construct. This methodology is then tested in a strategic DSS project where a managing director is supported in a decision about whether to close a division of a company. Finally, the limitations, professional and theoretical contributions and future directions of the research are discussed.

## DESIGN SCIENCE AS A RESEARCH METHOD

As mentioned in the Introduction, this project addresses the development of a DSS and, in particular, considers how to conceptualize the improvement of a decision task during evolutionary DSS development. The research uses a design science approach. Design science is an alternative, or complement, to the natural science approach that is dominant in IS research. In design science, the researcher ‘creates and evaluates IT artefacts intended to solve identified organizational problems’ (Hevner et al., 2004, p. 77). March & Smith (1995) clearly draw the distinction between natural and design science: ‘Whereas natural science tries to understand reality, design science attempts to create things that serve human purposes’ (p. 253).

Design science is particularly relevant to IS research because it helps to address two of the current controversies of the discipline: the role of the IT artefact in IS research (Orlikowski & Iacono, 2001) and the low level of professional relevance of many IS studies (Benbasat & Zmud, 1999). These controversies are addressed by making systems and methods the unit of analysis and by evaluating research outcomes in an organizational context, preferably in a real IT application. Figure 1 presents the research method used in this project. On the left-hand side of the figure are five distinct research processes. These are adapted from Vaishnavi & Kuechler (2005), who proposed a design research methodology with the following major process steps: awareness of problem, suggestion, development, evaluation and conclusion. They also identified knowledge feedback flows between the steps. The method in Figure 1 also includes aspects of other frameworks and models for conducting design science research in IS. Gregg et al. (2001) developed a design science-style software engineering research methodology framework for IS that comprises three interrelated phases: conceptualization, formalization and development. They argued that rigorous design research must address at least two of the three phases. In Figure 1 conceptualization is covered by the problem recognition and suggestion steps, and development is addressed by artefact development and evaluation. March & Smith (1995) proposed build and evaluate as the two fundamental design research processes. Build effectively covers the first three processes in Figure 1. Teasing out build into three subprocesses makes the research design much clearer and the execution much easier.

The right-hand side of Figure 1 shows how the current project uses the design science methodology. The first process, problem recognition, has already been addressed in the Introduction, with the problem being defined as ‘how to conceptualize the aspects of the decision task that need improvement during the various iterations of the evolutionary development’. In the second process, suggestion, the idea of cognitive bias is proposed as a focusing construct. The third phase, artefact development, is the heart of a design science project. March & Smith (1995) define IT design artefacts as constructs, models, methods, or instantiations. The artefact at the core of this project is a DSS development method. The instantiation of the design artefact in this project is the development of a strategic DSS using the new methodology. In the fourth phase, evaluation, researchers can use a variety of methods and techniques from both positivist and interpretive IS traditions. Hevner et al. (2004) provide a set of guidelines for design science research in IS and identify five classes of methods for evaluating design artefacts. Their first class of evaluation, observational, comprises case studies and field studies. This project uses a participatory case study to study the design artefact intensively in an organizational context. The aim of the evaluation stage of this project is to test the feasibility of using the development method in the field, and also to test its effectiveness in use. The details of the design of this empirical study are presented in the section on research design.

![](/api/attachments/WDKEBQY2/fulltext/images/df31dde76d43a61efdbd0c24572a551a951a27dea8b939f040b520f636b5cbac.jpg)  
Figure 1. A design science research method applied to evolutionary decision support systems (DSS) development.

## THEORETICAL BACKGROUND

This section addresses the suggestion stage of the design science research method. In trying to conceptualize the improvement of a decision task during evolutionary DSS development, a number of alternative theories of decision-making may be useful. DSS theory has been dominated by the process-oriented model of decision-making associated with the Nobel laureate Herbert Simon (Simon, 1960). Simon’s model was an integral component of the framework that first defined DSS (Gorry & Scott Morton, 1971) and was part of the theoretical foundation of the most influential early DSS books (Keen & Scott Morton, 1978; Sprague & Carlson, 1982). Despite the importance of Simon’s original theory to the history of DSS, more recent contributions to decision-making theory need to be better integrated into DSS theory. Angehrn & Jelassi (1994) argue that Simon’s theory ‘has become a serious obstacle for the evolution of DSS theory and practice’ (p. 269). Elam et al. (1992) argue that research on behavioural decision-making needs to be integrated with research on the effect of DSS on decision-making. One aspect of behavioural decision theory that is of potential value to DSS researchers and systems analysts involved in developing DSS is the notion of predictable bias in decision-making.

## Cognitive biases

Cognitive biases are cognitions or mental behaviours that prejudice decision quality in a significant number of decisions for a significant number of people; they are inherent in human reasoning. Cognitive biases are often called decision biases or judgement biases. One way of viewing cognitive biases is as predictable deviations from rationality. A rational choice is one based on the decision-maker’s current assets and the possible consequences of the choice (Hastie & Dawes, 2001, Chapter 1). Many cognitive biases have been identified by decision theory researchers. Following a detailed literature review and analysis, 37 biases were identified. They are presented in Table 1. This taxonomy arranges biases into categories of memory, statistical, confidence, adjustment, presentation and situation biases. Memory biases have to do with the storage and recall of information. Statistical biases are concerned with the general tendency of humans to process information contrary to the normative principles of probability theory. Confidence biases act to increase a person’s confidence in his or her prowess as a decision-maker. An important aspect of confidence bias is the curtailment of the search for new information about the decision task. Presentation biases should not be thought of as only being concerned with the display of data. They act to bias the way information is perceived and processed, and are some of the most important biases from a decision-making perspective. Situation biases relate to how a person responds to the general decision situation and represent the highest level of bias abstraction. It is important to recognize that all these cognitive biases are not necessarily as discrete as the taxonomy implies, and that they are likely to overlap in definition and effect. Further details of the individual biases and bias taxonomies can be found in Arnott (2002).

The research on biases summarized in Table 1 indicates a predictable propensity of human decision-makers towards irrationality. While the nature of the underlying psychological processes that lead to biased behaviour is the subject of considerable debate (Keren, 1990; Gigerenzer, 1991; 1996; Dawes & Mulford, 1996), the experimental findings on cognitive biases show persistent biasing in laboratory studies. This behaviour has also been shown in many cases to generalize to real-world situations, albeit with a reduced effect (Joyce & Biddle, 1981; Wright & Ayton, 1990). Normally excluded from consideration in cognitive bias research are factors that influence decisions arising from psychological pathology, religious belief or social pressure (including customs, tradition and hero worship). The role of intelligence and individual differences in cognitive bias research has been largely ignored, as have the effects of viscera or ‘hot’ factors on decision-making (Loewenstein, 1996).

Table 1. Taxonomy of cognitive biases

<table><tr><td>Bias</td><td>Description</td><td>Indicative references</td></tr><tr><td colspan="3">Memory biases</td></tr><tr><td>Hindsight</td><td>In retrospect, the degree to which an event could have been predicted is often overestimated</td><td>Fischhoff (1982a); Mazursky &amp; Ofir (1997)</td></tr><tr><td>Imaginability</td><td>An event may be judged more probable if it can be easily imagined</td><td>Tversky &amp; Kahneman (1974); Taylor &amp; Thompson (1982)</td></tr><tr><td>Recall</td><td>An event or class may appear more numerous or frequent if its instances are more easily recalled than other equally probable events</td><td>Tversky &amp; Kahneman (1981); Taylor &amp; Thompson (1982)</td></tr><tr><td>Search</td><td>An event may seem more frequent because of the effectiveness of the search strategy</td><td>Tversky &amp; Kahneman (1974); Bazerman (2002)</td></tr><tr><td>Similarity</td><td>The likelihood of an event occurring may be judged by the degree of similarity with the class it is perceived to belong to</td><td>Horton &amp; Mills (1984); Joram &amp; Read (1996)</td></tr><tr><td>Testimony</td><td>The inability to recall details of an event may lead to seemingly logical reconstructions that may be inaccurate</td><td>Wells &amp; Loftus (1984); Ricchiute (1997)</td></tr><tr><td colspan="3">Statistical biases</td></tr><tr><td>Base rate</td><td>Base rate data tends to be ignored when other data are available</td><td>Fischhoff &amp; Beyth-Marom (1983); Bar-Hillel (1990)</td></tr><tr><td>Chance</td><td>A sequence of random events can be mistaken for an essential characteristic of a process</td><td>Wagenaar (1988); Ayton et al. (1989)</td></tr><tr><td>Conjunction</td><td>Probability is often overestimated in compound conjunctive problems</td><td>Bar Hillel (1973); Teigen et al. (1996)</td></tr><tr><td>Correlation</td><td>The probability of two events occurring together can be overestimated if they have co-occurred in the past</td><td>Tversky &amp; Kahneman (1973); Alloy &amp; Tabachnik (1984)</td></tr><tr><td>Disjunction</td><td>Probability is often underestimated in compound disjunctive problems</td><td>Bar Hillel (1973); Bazerman (2002)</td></tr><tr><td>Sample</td><td>The size of a sample is often ignored in judging its predictive power</td><td>Nisbett et al. (1983); Sedlmeier &amp; Gigerenzer (1997)</td></tr><tr><td>Subset</td><td>A conjunction or subset is often judged more probable than its set</td><td>Thuring &amp; Jungermann (1990); Briggs &amp; Krantz (1992)</td></tr><tr><td colspan="3">Confidence biases</td></tr><tr><td>Completeness</td><td>The perception of an apparently complete or logical data presentation can stop the search for omissions</td><td>Fischhoff et al. (1978); Hogarth (1987)</td></tr><tr><td>Control</td><td>A poor decision may lead to a good outcome, inducing a false feeling of control over the judgement situation</td><td>Greenberg (1996); Hastie &amp; Dawes (2001)</td></tr><tr><td>Confirmation</td><td>Often decision-makers seek confirmatory evidence and do not search for disconfirming information</td><td>Russo et al. (1996); Heath (1996)</td></tr><tr><td>Desire</td><td>The probability of desired outcomes may be inaccurately assessed as being greater</td><td>Olsen (1997); Hastie &amp; Dawes (2001)</td></tr><tr><td>Overconfidence</td><td>The ability to solve difficult or novel problems is often overestimated</td><td>Brenner et al. (1996); Keren (1997)</td></tr><tr><td>Redundancy</td><td>The more redundant and voluminous the data, the more confidence may be expressed in its accuracy and importance</td><td>Remus &amp; Kotterman (1986); Arkes et al. (1989)</td></tr></table>

Table 1. Cont.

<table><tr><td>Bias</td><td>Description</td><td>Indicative references</td></tr><tr><td>Selectivity</td><td>Expectation of the nature of an event can bias what information is thought to be relevant</td><td>Schwenk (1988); Kahneman &amp; Tversky (1973)</td></tr><tr><td>Success</td><td>Often failure is associated with poor luck, and success with the abilities of the decision-maker</td><td>Miller (1976); Hogarth (1987)</td></tr><tr><td>Test</td><td>Some aspects and outcomes of choice cannot be tested, leading to unrealistic confidence in judgement</td><td>Einhorn (1980); Christensen-Szalanski &amp; Bushyhead (1981)</td></tr><tr><td colspan="3">Adjustment biases</td></tr><tr><td>Anchoring and adjustment</td><td>Adjustments from an initial position are usually insufficient</td><td>Chapman &amp; Johnson (1994); Ganzach (1996)</td></tr><tr><td>Conservatism</td><td>Often estimates are not revised appropriately on the receipt of significant new data</td><td>Fischhoff &amp; Beyth-Marom (1983); Nelson (1996)</td></tr><tr><td>Reference</td><td>The establishment of a reference point or anchor can be a random or distorted act</td><td>Tversky &amp; Kahneman (1974); Bazerman (2002)</td></tr><tr><td>Regression</td><td>That events will tend to regress towards the mean on subsequent trials is often not allowed for in judgement</td><td>Kahneman &amp; Tversky (1973); Joyce &amp; Biddle (1981)</td></tr><tr><td colspan="3">Presentation biases</td></tr><tr><td>Framing</td><td>Events framed as either losses or gains may be evaluated differently</td><td>Kahneman &amp; Tversky (1979); Kunberger (1997)</td></tr><tr><td>Linear</td><td>Decision-makers are often unable to extrapolate a non-linear growth process</td><td>Wagenaar &amp; Timmers (1979); Mackinnon &amp; Wearing (1991)</td></tr><tr><td>Mode</td><td>The mode and mixture of presentation can influence the perceived value of data</td><td>Saunders &amp; Jones (1990); Dusenbury &amp; Fennma (1996)</td></tr><tr><td>Order</td><td>The first or last item presented may be overweighted in judgement</td><td>Yates &amp; Curley (1986); Chapman et al. (1996)</td></tr><tr><td>Scale</td><td>The perceived variability of data can be affected by the scale of the data</td><td>Remus (1984); Ricketts (1990)</td></tr><tr><td colspan="3">Situation biases</td></tr><tr><td>Attenuation</td><td>A decision-making situation can be simplified by ignoring or significantly discounting the level of uncertainty</td><td>Beer (1981); Hogarth (1987)</td></tr><tr><td>Complexity</td><td>Time pressure, information overload and other environmental factors can increase the perceived complexity of a task</td><td>Maule &amp; Edland (1997); Ordonez &amp; Benson (1997)</td></tr><tr><td>Escalation</td><td>Often decision-makers commit to follow or escalate a previous unsatisfactory course of action</td><td>Northcraft &amp; Wolf (1984); Drummond (1994)</td></tr><tr><td>Habit</td><td>An alternative may be chosen only because it was used before</td><td>Hogarth (1987); Slovic (1975)</td></tr><tr><td>Inconsistency</td><td>Often a consistent judgement strategy is not applied to an identical repetitive set of cases</td><td>Showers &amp; Charkrin (1981); Moskowitz &amp; Sarin (1983)</td></tr><tr><td>Rule</td><td>The wrong decision rule may be used</td><td>Sage (1981); Goodwin &amp; Wright (1991)</td></tr></table>

## Debiasing

Debiasing is a procedure for reducing or eliminating biases from the cognitive strategies of a decision-maker. Keren (1990, p. 523) proposed a debiasing framework based on medical diagnosis and prescription. This framework aims to:

1 Identify the existence and nature of the potential bias. This includes understanding the environment of the bias and the cognitive triggers of the bias;

2 Consider alternative means for reducing or eliminating the bias;

3 Monitor and evaluate the effectiveness of the debiasing technique chosen. The possibility of negative side effects should be a particular concern.

In step 2, Keren distinguished between procedural techniques, where the user is unaware of the internal structure of the problem and hence the operation of the bias, and structuremodifying techniques, whereby the user can manipulate the internal structure of the task. Most reported debiasing research is of a procedural nature, although the deeper understanding of the task and biases required for structure modifying may lead to more effective outcomes.

In one of the most influential works on debiasing, Fischhoff (1982b) proposed a classification of debiasing methods that focused on the source of bias. Sources were identified as faulty decision-makers, faulty tasks and mismatches between decision-makers and tasks. Fischhoff’s category of faulty tasks implies that a redesign of the task environment may have an effect on cognitive biases. Klayman & Brown (1993) support this view and suggest that redesigning the task environment is an alternative to debiasing the individual decision-maker. IS has much to offer in this area, as task and process redesign is a core activity in systems analysis and design (Avison & Fitzgerald, 1995, Chapter 3).

The aspect of Fischhoff’s classification that has attracted the most attention is his strategy for ‘perfecting individuals’. This assumes that the primary source of biased judgement is the decision-maker, rather than the task. Kahneman & Tversky (1982) distinguish between those situations where people lack competence (comprehension errors) and those where they are competent but fail on a given decision (application errors). A debiasing strategy for an application error needs to focus on educating the decision-maker about the decision task, relevant biases and decision rules. Comprehension errors are more difficult to overcome than application errors. Fischhoff’s strategy to overcome these errors is an escalation design where each level represents an increase in the degree of support provided to the individual. The steps in this escalation of involvement are as follows:

1 Warn the decision-maker about the possibility of bias, without providing a description of its nature.

2 Describe the nature of the bias. This description should include the direction (positive or negative influence) and the strength of the bias.

3 Provide feedback. This feedback should personalize the warning and description of the bias and the decision-maker’s reaction to the bias for the target task.

4 Provide an extended programme of training, with coaching, feedback, discussion or any other intervention that will overcome the bias effect.

Fischhoff’s third category, mismatch between decision-maker and task, addresses Kahneman and Tversky’s application errors in that the decision-maker is thought to have the requisite cognitive skills but somehow they are not applied effectively. Fischhoff calls the debiasing strategies in this category cognitive engineering.

Bazerman (2002, pp. 155–157) suggested a general debiasing strategy based on the Lewin–Schein model of social change (Lewin, 1947; Schein, 1962). The Lewin–Schein model views change as a sequence of unfreezing, moving and refreezing processes. Unfreezing involves altering the forces on an individual such that the current equilibrium is disturbed to the extent that the individual wants to change. This can result from external direct pressure or indirectly by a reduction in the forces that constrain change. Moving involves instruction into the nature of change and the actual process of learning new social behaviours. Refreezing involves integrating the changes into the personality or cognitive make-up of the individual. Bazerman used the Lewin–Schein model because he argues that debiasing must be guided by a psychological framework for change. Bazerman believes that unfreezing is the key to debiasing for three reasons. The first is that decision-makers are likely to have used their current strategy for a considerable time and that any change will be psychologically disturbing. People will avoid disturbing information that questions their cognitive abilities. Second, most managers (who are the principal users of DSS) will have been rewarded for their current decision-making strategies. Indeed, their successive promotions will probably have been based on the results of their intuitive strategies. Third, individuals tend to keep cognitions in order and debiasing is a threat to this order or cognitive balance.

Bazerman terms the moving stage of the Lewin–Schein model as change. He prescribes three steps for decision-making change: clarification of the existence of cognitive biases, explanation of the causes of the biases and reassurance that the biases are not a threat to the decision-maker’s self-esteem (Bazerman, 2002, p. 156). It is important for the decision-maker to realize that everyone’s decision-making is biased and that debiasing is meant to make an already effective decision-maker even more effective. Refreezing is important as biases can easily resurface after the effort of the moving/change stage is over. The decision-maker needs to continually use the new approach to ensure that it becomes the dominant cognitive process.

In summary, human decision-making is subject to cognitive biases that can often adversely affect decision quality. It is important for managers to realize that cognitive biases may lead to serious errors of judgement in strategic decisions. The theory of cognitive biases and the process of debiasing provide a conceptual foundation for improving decision performance in a DSS project. If developing DSS can help to overcome the negative effects of one or more biases, then the process and outcome of decision-making should be improved.

## A DSS DEVELOPMENT METHOD

This section addresses the third process in the design science research method, artefact development. The design artefact in this project is a DSS development method that uses cognitive bias as a focusing construct. A model of the development method is presented in Figure 2. It conceptualizes DSS development at two levels: a major cycle level, represented by dark circles, and a development activity level, represented by white ellipses. The major cycles are initiation, analysis and delivery.

Figure 2 attempts to portray DSS development in a realistic manner. It is unlike most systems development schematics in that it does not indicate procedural flow through a model using arrows that link discrete elements. The development of the first generation of a DSS is often presented visually as involving left-to-right progress in the model, which obscures the fact that many activities overlap in time and nature. For example, it is common for system construction, system use and design to be undertaken in rapid succession, sometimes simultaneously. Figure 2 shows that the major cycles are linked by shared activities – planning and resourcing links initiation and analysis cycles, and design links analysis and delivery cycles. This attempts to capture the organic nature of DSS development, although it is very difficult to depict the dynamics of DSS development in a static, two-dimensional diagram.

## Initiation cycles

Initiation cycles are triggered when the client realizes the need for a new DSS application or recognizes the need for significant change to an existing application. This realization means that the decision-maker sees that some improvement to decision-making is required. This makes unfreezing easier than if a system development project is imposed, as is often the case with large-scale operational systems. If a DSS is using a debiasing strategy, it is ethically important to make the client aware of the nature of the strategy. Debiasing can be more personally challenging than other DSS development approaches, and the manager/client has the right to choose the level of cognitive process intervention that they are comfortable with. During initiation, the general problem area or decision is defined, resources are allocated and stakeholders engaged. An initiation cycle is completed when a decision is made by the client to continue with the development of the application.

![](/api/attachments/WDKEBQY2/fulltext/images/0bb2511268a4757f52ef2e67c551e31f97fccbe9c4a9059d025f3775caf0632c.jpg)  
Figure 2. A model of decision support systems development

## Analysis cycles

In the decision diagnosis activity, an analyst develops an understanding of the decision in sufficient detail to form a basis for the technical design of the IS. This description is used as a foundation for the design of the user interface, system logic, data structures and network requirements. The frameworks for debiasing discussed in the third section can be used as part of the decision diagnosis activity. Decision diagnosis is part of the unfreezing stage of the Lewin–Schein model and can also involve the moving/change stage. The cognitive engineering strategies of Fischhoff (1982b) are useful at the start of debiasing. They are:

 Make the decision-maker articulate what they know about the decision.

 Encourage decision-makers to search for discrepant information or information that challenges the adopted or preferred position.

 Offer ways to decompose the problem into more understandable subproblems or themes.

 Consider a wider set of decision situations or scenarios. Then, consider the nature of the current situation in light of the expanded conception.

 Propose alternative formulations of the problem. For example, reformulate a production problem as a marketing problem.

The analyst can work through some, or all of these steps, depending on the nature of the project. After this process, the manager will have become accustomed to thought experiments about the decision task and will be ready to explicitly consider cognitive biases. Keren’s diagnosis and prescription framework, Fischhoff’s perfecting individuals escalation design and Bazerman’s steps for decision-making change (all presented in the section on debiasing) can be combined into a strategy that can be used to approach debiasing. The steps in this combined approach are:

1 Identify the existence and nature of the potential bias.

2 Identify the likely impact and the magnitude of the bias.

3 Consider alternative means for reducing or eliminating the bias.

4 Reassure the user that the presence of biases is not a criticism of their cognitive abilities.

The taxonomy presented in Table 1 can be used to help with the identification of biases. The analyst should start bias identification at the highest level of the taxonomy (the memory, statistical, confidence, adjustment, presentation and situation categories) and judge if there is any likely effect under each classification. The analyst may then proceed to the individual bias level. The descriptions that are provided in Table 1 for each individual bias are useful with this identification.

In identifying the likely impact and magnitude of the bias or biases, the analyst is specifically interested in that subset of the identified biases that may have a strong negative influence on the target decision. The selection of the method for reducing or eliminating the bias will depend on the particular bias and the particular decision-maker. The citations for each bias in Table 1 can be consulted to provide additional knowledge about the bias and possible corrective action. The nature of the bias and the debiasing strategy will then guide the systems design activity. The systems analyst will consider what is possible to implement in an IT-based system, and this may cause a change in the debiasing approach.

## Delivery cycles

The delivery cycles involve both iterations and parallel application of design, system construction and use. These cycles cover the moving/change and refreezing stages of the Lewin– Schein model. The use of a DSS can be viewed as a process of feedback and training. Training will be more effective when the decision-maker, having misunderstood the basic principles of the task, has the experience and ability to realize this, and learn what is required. This form of debiasing also relies on the bias being triggered by the characteristics of the task. Analyst and client learning has always been a central theme in DSS development (Keen, 1980; Courbon, 1996). By using the system, the decision-maker will change his or her understanding of the decision task and the biases associated with that task. In reaction to this new understanding, the systems analyst should redesign the DSS and construct new versions or applications. In this sense, a DSS can be viewed as a learning system. Keen’s (1980) adaptive design model remains the most cited exposition of this cycle. Courbon (1996, p. 119) describes these cycles as sequences of ‘action – whenever the designer implements a new version and the user works with it and . . . reflection, i.e. the feedback where the user and the designer think about what should be done next based on the preceding active use’. Often the action of a delivery cycle triggers a new analysis cycle and occasionally a new initiation cycle.

The DSS analyst should pay particular attention to refreezing the decision process. Refreezing will be enabled by the continued use of a stable DSS. Given the probability of many iterations of the delivery cycle, it could be that a decision-maker might remain in a constant state of moving/change that may be psychologically stressful. The DSS may even be abandoned. On the other hand, if the moving/change stage is completed too quickly, the possible benefit of the DSS development will be reduced. An important activity during delivery cycles is to monitor and evaluate the effectiveness of the chosen debiasing technique (Keren, 1990). In particular, the possibility of negative side effects of the debiasing effort, including the triggering of other cognitive biases, should be assessed.

## AN EMPIRICAL STUDY OF BIAS-FOCUSED DSS DEVELOPMENT

The development of a design artefact is the major creative stage of the design science research method. The evaluation of the artefact is the next stage of the project. As foreshadowed in the second section of this paper, this project uses a case study of a real DSS implementation to evaluate the feasibility and effectiveness of the development methodology. The present section begins with the design of the case study. This is followed by a description of the project and a discussion on the evaluation of the development method.

## Research design

The empirical study used a single case design (Yin, 1994, Chapter 2). The unit of analysis was the system development process. An intensive case study captures more detail than a survey (Galliers, 1992), especially in identifying the nature and important characteristics of the systems development process (Benbasat et al., 1987). The selection of the case was opportunistic. It can also be termed an instrumental case study in that the actual case was less important than the process being studied (Stake, 1994, p. 237).

The data collection technique was participant observation (Cole, 1991; Atkinson & Hammersley, 1994). The author was the systems analyst for the DSS project, and two systems developers, one of whom who was a masteral student, programmed the applications. Although the researcher was involved in the DSS project, the method cannot be strictly categorized as action research as there was no process of theory building through iterations of planned intervention, reflection and learning (Baskerville & Wood-Harper, 1998, p. 101). This is partly due to the very short 5-week project lifetime. The main benefit of participant observation for this project was access to senior staff members and organizational processes (especially meetings and project discussions) which would not have been possible in non-participant observation (Cole, 1991). Everyone involved in the DSS project was aware that the case was being used for research into systems development. The development team recorded their experiences in diaries, and some sessions between the client and the systems analyst were audiotaped and transcribed. In addition, the analyst kept a meta-diary that reflected on the overall development process in the spirit of Schon (1983). A condition for approval of the research project by the university ethics committee was anonymity for the organization and subjects and, as a result, the identity of the organization was disguised. The essential elements of the project description were unaltered.

## Project description

## Context

‘Delta Consulting’ is a business services firm whose services include strategic consulting, project management, training and IT development. These areas reflect the interests of the founders, who mostly came from an academic environment, except one, who came from a large multi-national consulting firm. Delta has five office staff and 26 principal consultants. When required, external contractors are employed for specific projects. The service and product portfolio of Delta was under formal review by the board of directors. All areas of the company were profitable, although the training area was barely breaking even. The board had commissioned an external consultant (who was not considered a competitor) to review Delta’s performance and prospects. His report recommended that Delta maintain its core activities of strategic consulting and project management at the current level. He recommended that the training area be wound up and that a strategic alliance with a specialist training provider be investigated. He argued that the time and energy that Delta would save from this alliance could be devoted to the IT development area, which he believed had a huge potential for revenue growth. Delta’s training services involved 19 courses that ranged from half-day to three-day programmes. Most of Delta’s consultants were involved in training, but the only full-time employee in the area was the training manager. The board considered the external consultant’s report and other briefing information, and after 15 minutes of discussion there was a general feeling that the closure of training services was a desirable strategy, although no final decision was taken. The possible closure of the training area was flagged as an item for detailed discussion and decision at a board meeting in 2 months’ time. After the meeting, the managing director began to have reservations about the external consultant’s recommendation and the prospect of Delta not having a training function. At this time, the board meeting to consider the training area closure was 5 weeks away.

## First initiation cycle

Although the managing director had to recommend formally a course of action to the board, he had the strong impression that the decision was largely his and that the board would probably adopt his recommendation, as it had on numerous other occasions. However, with only 5 weeks available, he was unsure of the correct strategy. To help his decision process, he engaged a consultant systems analyst to develop a DSS, triggering the first initiation cycle of the project. He had no firm idea about what support he needed, just that he needed more information and more options. There was no need for the analyst to explicitly address unfreezing the decision-making process as the manager had effectively unfrozen himself when he identified the need for specialist support. The decision problem was classified as a possible application error (Kahneman & Tversky, 1982) in that the managing director was a competent decision-maker but was faced with a decision situation that he had not encountered before. The analyst discussed with the managing director the general notion of cognitive biases and outlined the degree and nature of the possible interventions into his decision-making processes that could accompany a bias-focused DSS development. The manager agreed to follow a bias-focused strategy. The analyst began the first analysis cycle with a number of unstructured conservations with the managing director. He studied the financial documentation that was presented to the board, as well as the external consultant’s report.

## First analysis cycle

The project then moved from planning and resourcing to a decision diagnosis activity. The training closure decision was modelled by using functional decomposition (Avison & Fitzgerald, 1995, p. 62) and influence diagrams (Bodily, 1988). The decision was then analysed for the influence of any major cognitive biases by using the taxonomy presented in Table 1. It became apparent that the confirmation bias was likely to have a major negative impact on the decision, as the information available to the board seemed to support strongly a closure strategy. The confirmation bias acts against a fundamental principle of the scientific method, which holds that information that refutes a hypothesis is more valuable than information that supports it. However, under the confirmation bias, people tend to search for information that confirms their hypotheses and gloss over, or even actively ignore, disconfirming information (Evans, 1989; Russo et al., 1996). The only known previous work on the confirmation bias and DSS is Ang (1992). The analyst researched the confirmation bias in the psychology literature to better understand the effect. After this he undertook a series of semi-structured interviews with the managing director to elucidate the hypotheses or propositions that were addressed by the managing director and the board when the prima facie case to close the training area was made. The information sources known to be used by the managing director and the board were then attributed to the various propositions, and the information was classified as being confirming, disconfirming or neutral. As can be seen in Table 2, virtually all of the information was found to be confirming in nature.

During this diagnostic activity, the analyst began to develop a vague idea of what sort of DSS could help the managing director; it would probably have a data focus, rather than a model focus, but it would probably not be a standard database application. This vague speculation about the IS marked the start of design activities in the engagement. The next event in the project was deeply symbolic. Rather than refer to the project as the ‘training closure decision’, through a number of conversations, the analyst convinced the managing director to rename the project the ‘training area evaluation’. This neutral reframing of the decision task was noticed and commented on by a number of company staff. It was the first time that they knew the training area closure was not a ‘done deal’ and that the managing director was considering other strategies.

To counter the effect of the confirmation bias, the analyst adopted the escalation approach to debiasing ‘perfectible individuals’, which was discussed in the third section of this paper (Fischhoff, 1982b). The analyst described to the managing director the nature of the confirmation bias and briefed him on the results of the information stream analysis. They mutually decided to develop a system that would attempt to reduce the effect of overconfirmation in the target decision. A search for possible disconfirming information was undertaken, led by the managing director and assisted by Delta’s office manager. Much of this information was of a qualitative nature and was included in documents such as office memos and consultant performance reviews.

Table 2. Information used by the board for the prima facie closure decision

<table><tr><td>Information</td><td>Type</td><td>Source</td><td>Decision impact</td></tr><tr><td>Profit and loss statements (YTD and last 2 years)</td><td>Quantitative</td><td>Office manager</td><td>Confirming</td></tr><tr><td>Report on the future of Delta Consulting</td><td>Qualitative</td><td>Consultant&#x27;s report</td><td>Confirming</td></tr><tr><td>Revenue and expenditure forecasts (Total company, next 3 years)</td><td>Quantitative</td><td>Consultant&#x27;s report</td><td>Confirming</td></tr><tr><td>Revenue and expenditure forecasts (By divisions, next 3 years)</td><td>Quantitative</td><td>Consultant&#x27;s report</td><td>Confirming</td></tr><tr><td>Course attendance history (last 3 years)</td><td>Quantitative</td><td>Training manager</td><td>Neutral</td></tr></table>

YTD, year-to-date.

## First delivery cycle

The first delivery cycle produced a DSS, which became known as the intelligence system. The system was named by the managing director. It was constructed by using hyperlinked documents on a dedicated personal computer; in essence it was an unpublished web site. The document navigation tree was based on the decision influence diagram and a hierarchy chart of identified hypotheses. In this way, the theory of confirmation bias was used to provide the physical structure of the IS. Financial statements and other board reports were pasted into the relevant documents, as was relevant disconfirming information. The system was then used by the managing director to explore the training area decision. All other board members were given access to the system. While the document structure implied which information sources could be used to arrive at the decision, the system did not force a set retrieval pattern on the user. The developer inserted as many hyperlinks as possible into each document to allow users to follow hunches that were triggered by system use. While using the system, the managing director repeatedly asked for additional information to be added, as did another director who briefly used the system. These minor delivery cycles significantly increased the amount of information contained in the Intelligence System but did not significantly change the logic or structure of the system.

## Second initiation cycle

While using the intelligence system, the managing director developed new ideas about the role of the training area. He began to wonder if training was generating business for the other areas of Delta or if it was important in retaining clients. The possible presence of a cross-subsidy was difficult to assess as the additional business generated by the training activities could follow the initial work by a significant period of time, or be from a seemingly unrelated client because a person previously related to Delta through training could have changed employer. These ideas triggered the second initiation cycle of the project. The managing director called this second stage the subsidy system, because it emerged from his training cross-subsidy hypothesis.

## Second analysis and delivery cycles

The subsidy system was not a discrete decision support application or set of applications in the sense of the intelligence system. Rather, it is best described as a series of ephemera – applications that existed sometimes for hours, sometimes for days. This phase of the overall project was characterized by chaotic analysis and design cycles. Design cycles were much more numerous and used more human resources than the analysis cycles, although it was hard at times to tell when one cycle ended and another began.

The people involved with the intelligence system were also involved with the subsidy system. The managing director was personally involved in virtually every DSS application and devoted significant time to the ‘system’. He indicated that the project was one of his highest priorities and asked to be interrupted if new reports became available. The analyst and system developers worked full-time on the project and at times their effort was augmented by a company IT consultant. The office manager was more involved in this stage of the project than for the intelligence system. His main role was as a data provider for models and databases developed by the development team.

The applications that made up the subsidy system were organized around questions articulated by the managing director. Once a question was defined, the analyst and programmers built an information system as quickly as possible and populated it with data. Applications were developed by using relational database and spreadsheet packages. Answering some of the questions involved non-IT support or data gathering, e.g., asking a long-standing client about an issue at a business lunch to inform system development. Table 3 illustrates how the managing director’s questions guided the development of the subsidy system applications.

## Recommendation to the board

As a result of using the various applications that made up the subsidy system phase of the project, the managing director decided to retain the training area of Delta. He believed that consultants benefited significantly from the formalization of knowledge and experience that was required to conduct a training course. He believed that this benefit manifested in increased consultant performance and in increased sales. That is, he believed that a significant cross-subsidy existed between training and the core consulting areas. He also discovered that the consultants enjoyed the training work and that this contributed to their decision to remain with Delta. This was an important finding because maintaining a high quality staff establishment in the highly mobile consulting industry is very difficult. Using material from the decision support applications, the managing director prepared a paper for the board that recommended retaining the training function. As predicted, the board accepted the managing director’s recommendation and resolved to investigate potential efficiencies in other areas.

Table 3. Example applications from the subsidy system

<table><tr><td>Question</td><td>IT-based decision support</td><td>Data sources</td><td>Non-IT-based decision support</td></tr><tr><td>How many of our clients for strategic consulting were initially clients of the training area?</td><td>Databases</td><td>Client files, training mailing list</td><td>Managing director contacts selected clients</td></tr><tr><td>Is there a relationship between consultant participation in training and their consulting performance?</td><td>Databases, spreadsheets</td><td>Sales data, consultant staff files, training evaluations, survey</td><td>Managing director has conversations with selected project leaders and consultants, formal survey of all consultants</td></tr><tr><td>What are the infrastructure and HR costs of expanding IT development?</td><td>Spreadsheets</td><td>Generic building cost data, HR budget</td><td>Office manager consults with Building owner</td></tr></table>

IT, information technology; HR, human resources.

## Reflection and discussion

The first issue is whether Delta’s DSS project can be considered successful. The assessment of success is a difficult problem for design research studies because it is impossible, after the research intervention, to determine if an alternative intervention would have been more successful or have led to a different outcome. The main argument indicating a successful project is the opinion of the managing director. In a study of DSS success factors, Finlay & Forghani (1998) argued that success is ‘equated with repeat use and user satisfaction’ (p. 54). In this case, the managing director regarded the project as a success; he even offered a bonus payment to the development team, citing the importance of the outcome to Delta as the reason for the offer. His continued personal involvement in the project equates with repeat use, which reinforces the ‘success’ evaluation. A common occurrence in DSS projects is that the commissioning manager has already made his or her decision before project initiation and wants a DSS developed to justify this decision. This situation is unlikely to have occurred in this case. The bias-focused approach adopted by the project represented a significant challenge to the managing director’s cognitive strategies and required much more personal involvement than a standard DSS engagement. If his objective in commissioning the project was post-decision justification, a less demanding development process could have been followed.

The case study was conducted to evaluate the design artefact at the centre of this design science project: a DSS development methodology that uses cognitive bias theory as a focusing construct. The case study shows that the development method is both feasible and effective. Using a decision-debiasing approach within an evolutionary development method, the systems analyst had a clear strategy for improving decision performance using a DSS. The new development method adds a psychological theory of cognitive process change to DSS development. In the case study, the process of change involved the agreed intervention in the decisionmaking process of an experienced and successful executive. The approach in Delta’s project was a combination of cognitive engineering and procedural debiasing.

The case study was also a classical evolutionary DSS development in the spirit of Keen (1980) and Courbon (1996). By using the DSS, the managing director learnt more about decision tasks, which triggers system evolution. Sometimes this evolution involves changes to an application; sometimes it leads to the development of new applications. Two clusters of adaptive loops defined the major development cycles of the engagement. The analysis cycles that linked planning and resourcing, decision diagnosis, and design were quite chaotic and occurred over short periods of time. The loops clustered in systems delivery were more orderly and tended to be cycles of design to system construction to use to design again. As with many DSS, the development activities were non-linear, and often aspects of the development process proceeded in parallel and in an opposite direction to that normally assumed. For example, in the subsidy system, some database applications were built (delivery cycle) in order to begin understanding the nature of the question that was guiding development (analysis cycle). This is contrary to the normal instantiation of a classical systems development life cycle.

The interpretation of the subsidy system as a series of ephemera may be of considerable theoretical and practical importance. Most IS research is focused on projects that are relatively large and stable. In the DSS domain, it may be that the majority of systems are more like the ephemera that composed the subsidy system. As in the case of the company’s training area decision, the impact of these microsystems on an organization may be much more significant than a high-cost, large-scale operational system. This is because the decisions based on the use of ephemeral DSS can determine the strategic success or failure of an organization. Further research into the ephemeral nature of many IS is needed.

## CONCLUSION

This paper has presented design science research that aims to improve DSS development in organizations. The first stage of the research was the recognition that conceptualizing the improvement of a decision task during evolutionary DSS development is a significant problem for DSS analysts. The second stage investigated existing psychological research to see if any theory could help solve the problem. The theory of cognitive bias was proposed as a candidate for this assistance. A taxonomy of 37 cognitive biases that codifies a complex area of psychological research was developed. The third stage of the project involved the construction of the design artefact: an evolutionary DSS development methodology that uses cognitive bias theory as a focusing construct, especially in its analysis cycles. The systems development methodology is the major contribution of the project. The fourth stage of the project involved the evaluation of the methodology. Its feasibility and effectiveness was successfully tested in a participatory case study of a strategic DSS project.

The design science research presented in this paper is subject to a number of limitations. The participatory observation approach of the case study can have a number of biases, including the need to take advocacy rather than observer roles, becoming a supporter of the group under study and not having enough time for observations (Yin, 1994, p. 89). These biases were minimized by keeping knowledge of the potential problems explicit throughout the project. There was ample time for observation and reflection during the project. With respect to advocacy bias, it was inevitable that the researcher engaged in some advocacy for the development method. However, the researcher did not become a supporter of the client, or an advocate of any decision alternative or the project outcome. The next limitation is the difficulty in generalizing a single case study to other engagements. In design science research, the aim of the evaluation phase is to demonstrate the feasibility and effectiveness of the design artefact. The case study in the fifth section has arguably demonstrated such feasibility and effectiveness, but as identified by other researchers, design science research outcomes in one project may not generalize to other projects (Markus et al., 2002). It is essential that further cases or action research studies be undertaken, possibly using a replication logic (Yin, 1994, p. 36).

The goal of design science research is utility, especially through the creation of new methods and technologies that are useful in practice. The systems development method described in this paper is at an early stage of development. Considerable further research is required to enable practising systems analysts to use it with confidence. The method requires systems analysts to have a reasonable understanding of behavioural decision theory, and this understanding is particularly important for cognitive bias identification. The bias taxonomy is a useful starting point for this activity, but more research is required to develop an identification process or method that is operationally effective. One possible direction could be the development of a web-based assistant for bias identification. Another important area for further research is the psychological contract between the client/user and the DSS analyst. The bias-focused DSS methodology could place the client in a potentially stressful situation as it challenges the decision-making processes of the manager. The analyst needs to be both aware of, and sensitive to, this challenge. Further research is required to produce strategies and guidelines to assist the analyst with establishing and maintaining this contract.

The final reflection involves the research methodology used in this project. Design science is an important movement in IS research (Markus et al., 2002; Hevner et al., 2004). It can help the discipline address its problem of professional relevance and can help bring the IT artefact to the centre of IS research. This project has shown that design science can tackle IS problems of both theoretical and practical importance.

## REFERENCES

Alloy, L.B. & Tabachnik, N. (1984) Assessment of covariation by humans and animals: joint influence of prior expectations and current situational information. Psychological Review, 91, 112–149.

Ang, D. (1992) An investigation into the use of a decision support system to reduce the confirmation bias. Unpublished Master of Computing Minor Thesis. Monash University, Melbourne, Australia.

Angehrn, A.A. & Jelassi, T. (1994) DSS research and practice in perspective. Decision Support Systems, 12, 257–275.

Arkes, H.R., Hackett, C. & Boehm, L. (1989) The generality of the relation between familiarity and judged validity. Journal of Behavioural Decision Making, 2, 81–94.

Arnott, D. (2002) A Taxonomy of Decision Biases (Techni cal Report. No. 2002/01). Decision Support Systems Laboratory. Monash University, Melbourne, Australia. [WWW document]. URL http://dsslab.sims.monash.edu. au/taxonomy.pdf.

Arnott, D. (2004) Decision support systems evolution: framework, case study and research agenda. European Journal of Information Systems, 13, 247–259.

Arnott, D. & Pervan, G. (2005) A critical analysis of decision support systems research. Journal of Information Technology, 20, 1–21.

Atkinson, P. & Hammersley, M. (1994) Ethnography and participant observation. In: Handbook of Qualitative Research, Denzin, N.K. & Lincoln, Y.S. (eds), pp. 248– 261. Sage Publications, Thousand Oaks, CA, USA.

Avison, D.E. & Fitzgerald, G. (1995) Information Systems Development: Methodologies, Techniques and Tools, 2nd edn. McGraw-Hill, Maidenhead, UK.

Ayton, P., Hunt, A.J. & Wright, G. (1989) Psychologica conceptions of randomness. Journal of Behavioural Decision Making, 2, 221–238.

Bar-Hillel, M. (1973) On the subjective probability of compound events. Organizational Behavior and Human Performance, 9, 396–406.

Bar-Hillel, M. (1990) Back to base rates. In: Insights in Decision Making, Hogarth, R. (ed.), pp. 200–216. Uni versity of Chicago Press, Chicago, IL, USA.

Baskerville, R. & Wood-Harper, A.T. (1998) Diversity in information systems action research methods. European Journal of Information Systems, 7, 90–107.

Bazerman, M.H. (2002) Judgement in Managerial Decision Making, 5th edn. Wiley, New York, NY, USA.

Beer, S. (1981) Brain of the Firm, 2nd edn. Wiley, Chich-ester, UK.

Benbasat, I., Goldstein, D.K. & Mead, M. (1987) The case research strategy in studies of information systems. Management Information Systems Quarterly, 11, 369– 386.

Benbasat, I. & Nault, B. (1990) An evaluation of empirical research in managerial support systems. Decision Support Systems, 6, 203–226.

Benbasat, I. & Zmud, R.W. (1999) Empirical research in information systems: the question of relevance. MIS Quarterly, 23, 3–16.

Bodily, S.E. (1988) Modern Decision Making: A Guide to Modelling with Decision Support Systems. McGraw-Hill, New York, NY, USA

Botha, S., Gryffenberg, I., Hofmeyer, F.R., Lausberg, J.L., Nicolay, R.P., Smit, W.J., et al. (1997) Guns or butter: decision support for determining the size and shape of the South African National Defence Force. Interfaces, 27, 7–28.

Brenner, L.A., Koehler, D.J., Liberman, V. & Tversky, A. (1996) Overconfidence in probability and frequency judgements: a critical examination. Organisational Behaviour and Human Decision Processes, 65, 212– 219.

Briggs, L.K. & Krantz, D.H. (1992) Judging the strength of designated evidence. Journal of Behavioral Decision Making, 5, 77–106.

Chapman, G.B., Bergus, G.R. & Elstein, A.S. (1996) Order of information affects clinical judgement. Journal of Behavioral Decision Making, 9, 201–211.

Chapman, G.B. & Johnson, E.J. (1994) The limits of anchoring. Journal of Behavioral Decision Making, 7, 223–242.

Christensen-Szalanski, J.J. & Bushyhead, J.B. (1981) Physicians use of probabilistic judgement in a real clinical setting. Journal of Experimental Psychology: Human Perception and Performance, 7, 928–935.

Cole, R.E. (1991) Participant observer research: an activist role. In: Participatory Action Research, Whyte, W.F. (ed.), pp. 159–166. Sage Publications, Newbury Park, CA, USA.

Courbon, J.-C. (1996) User-centered DSS design and implementation. In: Implementing Systems for Supporting Management Decisions: Concepts, Methods and Experiences, Humphreys, P., Bannon, L., McCosh, A., Milgliarese, P. & Pomerol, J.-C. (eds), pp. 108–122. Chapman & Hall, London, UK

Dawes, R.M. & Mulford, M. (1996) The false consensus effect and overconfidence: flaws in judgement or flaws in how we study judgement. Organisational Behaviour and Human Decision Processes, 65, 201–211.

Drummond, H. (1994) Escalation in organisational decision making: a case of recruiting an incompetent employee. Journal of Behavioral Decision Making, 7, 43–56.

Dusenbury, R. & Fennma, M.G. (1996) Linguistic-numeric presentation mode effects on risky option preferences. Organisational Behaviour and Human Decision Processes, 68, 109–122.

Einhorn, H.J. (1980) Learning from experience and suboptimal rules in decision making. In: Cognitive Processes in Choice and Decision Making, Wallsten, T.S. (ed.), pp. 1–20. Erlbaum, Hillsdale, NJ, USA.

Elam, J.J., Jarvenpaa, S.L. & Schkade, D.A. (1992) Behavioural decision theory and DSS: new opportunities for collaborative research. In: Information Systems and Decision Processes, Stohr, E.A. & Konsynski, B.R. (eds), pp. 51–74. IEEE Computer Society Press, Los Alamitos, CA, USA.

Evans, J.St.B.T. (1989) Bias in Human Reasoning: Causes and Consequences. Lawrence-Erlbaum, London, UK

Finlay, P.N. & Forghani, M. (1998) A classification of success factors for decision support systems. Journal of Strategic Information Systems, 7, 53–70.

Fischhoff, B. (1982a) For those condemned to study the past: heuristics and biases in hindsight. In: Judgement under Uncertainty: Heuristics and Biases, Kahneman, D., Slovic, P. & Tversky, A. (eds), pp. 335–351, Cambridge University Press, New York, NY, USA.

Fischhoff, B. (1982b) Debiasing. In: Judgement Under Uncertainty: Heuristics and Biases, Kahneman, D., Slovic, P. & Tversky, A. (eds), pp. 422–444. Cambridge University Press, New York, NY, USA.

Fischhoff, B. & Beyth-Marom, R. (1983) Hypothesis evaluation from a Bayesian perspective. Psychological Review, 90, 239–260.

Fischhoff, B., Slovic, P. & Lichtenstein, S. (1978) Fault trees: sensitivity of estimated failure probabilities to problem representation. Journal of Experimental Psychology: Human Perception and Performance, 4, 330– 344.

Galliers, R.D. (1992) Choosing information systems research approaches. In: Information Systems Research: Issues, Methods and Practical Guidelines, Galliers, R.D. (ed.), pp. 144–162. Blackwell Scientific, London, UK.

Ganzach, Y. (1996) Preference reversals in equalprobability gambles: a case for anchoring and adjust-

ment. Journal of Behavioral Decision Making, 9, 95– 109.

Gigerenzer, G. (1991) How to make cognitive illusions disappear: beyond heuristics and biases. Psychological Review, 103, 592–596.

Gigerenzer, G. (1996) On narrow norms and vague heuristics: a reply to Kahneman and Tversky. European Review of Social Psychology, 2, 83–115.

Goodwin, P. & Wright, G. (1991) Decision Analysis for Management Judgement. Wiley, Chichester, UK.

Gorry, G.A. & Scott Morton, M.S. (1971) A framework for management information systems. Sloan Management Review, 13, 1–22.

Greenberg, J. (1996) ‘Forgive me, I’m new’: three experimental demonstrations of the effects of attempts to excuse poor performance. Organisational Behaviour and Human Decision Processes, 66, 165–178.

Gregg, D.G., Kulkarni, U.R. & Vinze, A.S. (2001) Understanding the philosophical underpinnings of software engineering research in information systems. Information Systems Frontiers, 3, 169–183.

Hastie, R. & Dawes, R.M. (2001) Rational Choice in an Uncertain World. Sage, Thousand Oaks, CA, USA.

Heath, C. (1996) Do people prefer to pass along good or bad news? Valence relevance of news as predictors of transmission propensity. Organisational Behaviour and Human Decision Processes, 68, 79–94.

Hevner, A.R., March, S.T., Park, J. & Ram, S. (2004) Design science in information systems research. MIS Quarterly, 28, 75–106.

Hogarth, R. (1987) Judgement and Choice: The Psychology of Decision, 2nd edn. Wiley, Chichester, UK.

Horton, D.L. & Mills, C.B. (1984) Human learning and memory. Annual Review of Psychology, 35, 361–394.

Igbaria, M., Sprague, R.H. Jr, Basnet, C. & Foulds, L. (1996) The impacts and benefits of a DSS: the case of FleetManager. Information and Management, 31, 215– 225.

Joram, E. & Read, D. (1996) Two faces of representativeness: the effects of response format on beliefs about random sampling. Journal of Behavioral Decision Making, 9, 249–264.

Joyce, E.J. & Biddle, G.C. (1981) Are auditors’ judgements sufficiently regressive? Journal of Accounting Research, 19, 323–349.

Kahneman, D. & Tversky, A. (1973) On the psychology of prediction. Psychological Review, 80, 237–251.

Kahneman, D. & Tversky, A. (1979) Prospect theory: an analysis of decision under risk. Econometrica, 47, 263– 291.

Kahneman, D. & Tversky, A. (1982) Intuitive prediction: biases and corrective procedures. In: Judgement under Uncertainty: Heuristics and Biases, Kahneman, D., Slovic, P. & Tversky, A. (eds), pp. 414–421. Cambridge University Press, New York, NY, USA.

Keen, P.G.W. (1980) Adaptive design for decision support systems. Data Base, 12, 15–25.

Keen, P.G.W. & Scott Morton, M.S. (1978) Decision Support Systems: An Organisational Perspective. Addison-Wesley, Reading, MA, USA.

Keren, G. (1990) Cognitive aids and debiasing methods: can cognitive pills cure cognitive ills. In: Cognitive Biases, Caverni, J.P., Fabre, J.M. & Gonzalez, M. (eds), pp. 523– 555. North-Holland, Amsterdam, the Netherlands.

Keren, G. (1997) On the calibration of probability judgments: some critical comments and alternative perspectives. Journal of Behavioral Decision Making, 10, 269–278.

Klayman, J. & Brown, K. (1993) Debias the environment instead of the judge: an alternative approach to reducing error in diagnostic (and other) judgement. Cognition, 49, 97–122.

Kunberger, A. (1997) Theoretical conceptions of framing effects in risky decisions. In: Decision Making: Cognitive Models and Explanations, Ranyard, R., Crozier, W.R. & Svenson, O. (eds), pp. 128–144. Routledge, London, UK.

Lewin, K. (1947) Group decision and social change. In: Readings in Social Psychology, Newcomb, T.M. & Hartley, E.L. (eds), pp. 330–344. Holt, New York, NY, USA.

Loewenstein, G. (1996) Out of control: visceral influences on behavior. Organisational Behaviour and Human Decision Processes, 65, 272–292.

Mackinnon, A.J. & Wearing, A.J. (1991) Feedback and the forecasting of exponential change. Acta Psychologica, 76, 177–191.

March, S. & Smith, G.F. (1995) Design & natural science research on information technology. Decision Support Systems, 15, 251–266.

Markus, M.L., Majchrzak, A. & Gasser, L. (2002) A design theory for systems that support emergent knowledge processes. MIS Quarterly, 26, 179–212.

Maule, A.J. & Edland, A.C. (1997) The effects of time pressure on human judgement and decision making. In: Decision Making: Cognitive Models and Explanations, Ranyard, R., Crozier, W.R. & Svenson, O. (eds), pp. 189–204. Routledge, London, UK.

Mazursky, D. & Ofir, C. (1997) ‘I knew it all along’ under all conditions? Or possibly ‘I could not have expected it to

happen’ under some conditions? Organisational Behaviour and Human Decision Processes, 66, 237–240.

Miller, D.T. (1976) Ego involvement and attributions for success and failure. Journal of Personality and Social Psychology, 34, 901–906.

Moskowitz, H. & Sarin, R.K. (1983) Improving the consistency of conditional probability assessments for forecasting and decision making. Management Science, 29, 735–749.

Nelson, M.W. (1996) Context and the inverse base rate effect. Journal of Behavioral Decision Making, 9, 23–40.

Nisbett, R.E., Krantz, D.H., Jepson, C. & Ziva, K. (1983) The use of statistical heuristics in everyday inductive reasoning. Psychological Review, 90, 339–363.

Northcraft, G.B. & Wolf, G. (1984) Dollars, sense and sunk costs: a life cycle model of resource allocation decisions. Academy of Management Review, 9, 225–234.

Olsen, R.A. (1997) Desirability bias among professional investment managers: some evidence from experts. Journal of Behavioral Decision Making, 10, 65–72.

Ordonez, L. & Benson, L. III (1997) Decisions under time pressure: how time constraint affects risky decision making. Organisational Behaviour and Human Decision Processes, 71, 121–140.

Orlikowski, W.J. & Iacono, C.S. (2001) Desperately seeking the ‘IT’ in IT research – a call for theorizing the IT artifact. Information Systems Research, 12, 121–134.

Poon, P. & Wagner, C. (2001) Critical success factors revisited: success and failure cases of information systems for senior executives. Decision Support Systems, 30, 393–418.

Remus, W.E. (1984) An empirical investigation of the impact of graphical and tabular data presentations on decision making. Management Science, 30, 533–542.

Remus, W.E. & Kottemann, J.E. (1986) Toward intelligent decision support systems: an artificially intelligent statistician. MIS Quarterly, 10, 403–418.

Ricchiute, D.N. (1997) Effects of judgement on memory: experiments in recognition bias and process dissociation in a professional judgement task. Organisational Behaviour and Human Decision Processes, 70, 27–39.

Ricketts, J.A. (1990) Powers-of-ten information biases. MIS Quarterly, 14, 63–77.

Russo, J.E., Medvec, V.H. & Meloy, M.G. (1996) The distortion of information during decisions. Organisational Behaviour and Human Decision Processes, 66, 102– 110.

Sage, A.P. (1981) Behavioural and organisational considerations in the design of information systems and processes for planning and decision support. IEEE

Transactions on Systems, Man and Cybernetics, 11, 640–678.

Saunders, C. & Jones, J.W. (1990) Temporal sequences in information acquisition for decision making: a focus on source and medium. Academy of Management Review, 15, 29–46.

Schein, E.H. (1962) Management development as a system of influence. Industrial Management Review, 2, 59–77.

Schon, D.A. (1983) The Reflective Practitioner: How Professionals Think in Action. Ashgate, Aldershot, UK.

Schwenk, C.R. (1988) The cognitive perspective on strategic decision making. Journal of Management Studies, 25, 41–55.

Sedlmeier, P. & Gigerenzer, G. (1997) Intuitions about sample size: the empirical law of large numbers. Journal of Behavioral Decision Making, 10, 33–51.

Showers, J.L. & Charkrin, L.M. (1981) Reducing uncollectable revenue from residential telephone customers. Interfaces, 11, 21–34.

Simon, H.A. (1960) The New Science of Management Decision. Harper & Row, New York, NY, USA.

Slovic, P. (1975) Choice between equally valued alternatives. Journal of Experimental Psychology: Human Perception and Performance, 1, 280–287.

Sprague, R.H. Jr & Carlson, E.D. (1982) Building Effective Decision Support Systems. Prentice Hall, Englewood Cliffs, NJ, USA.

Stake, R.E. (1994) Case studies. In: Handbook of Qualitative Research, Denzin, N.K. & Lincoln, Y.S. (eds), pp. 236–247. Sage Publications, Thousand Oaks, CA, USA.

Taylor, S.E. & Thompson, S.C. (1982) Stalking the elusive ‘vividness’ effect. Psychological Review, 89, 155–181.

Teigen, K.H., Martinussen, M. & Lund, T. (1996) Linda versus World Cup: conjunctive probabilities in three-event fictional and real-life predictions. Journal of Behavioral Decision Making, 9, 77–93.

Thuring, M. & Jungermann, H. (1990) The conjunction fallacy: causality vs. event probability. Journal of Behavioural Decision Making, 3, 51–74.

Tversky, A. & Kahneman, D. (1973) Availability: a heuristic for judging frequency and probability. Cognitive Psychology, 5, 207–232.

Tversky, A. & Kahneman, D. (1974) Judgment under uncertainty: heuristics and biases. Science, 185, 1124– 1131.

Tversky, A. & Kahneman, D. (1981) The framing of decisions and the psychology of choice. Science, 211, 453–458.

Vaishnavi, V. & Kuechler, B. (2005) Design research in information systems. [WWW document]. URL http:// www.isworld.org/Researchdesign/drisISworld.htm (accessed 20 March 2005).

Wagenaar, W.A. (1988) Paradoxes of Gambling Behav iour. Lawrence Erlbaum, East Sussex, UK.

Wagenaar, W.A. & Timmers, H. (1979) The pond-and duckweed problem: three experiments on the misperception of exponential growth. Acta Psychologica, 43, 239–251.

Wells, G.L. & Loftus, E.F. (eds) (1984) Eyewitness Testimony: Psychological Perspectives. Cambridge University Press, New York, NY, USA.

Wright, G. & Ayton, P. (1990) Biases in probabilistic judge ment: a historical perspective. In: Cognitive Biases, Caverni, J.P., Fabre, J.M. & Gonzalez, M. (eds), pp. 425–441. North-Holland, Amsterdam, the Netherlands.

Yates, J.F. & Curley, S.P. (1986) Contingency judgement: primacy effects and attention decrement. Acta Psychologica, 62, 293–202.

Yin, R.K. (1994) Case Study Research: Design and Meth ods, 2nd edn. Sage Publications, Newbury Park, CA, USA.

## Biography

David Arnott is Professor of Information Systems at Monash University, Melbourne, Australia and Associate Dean, Education of Monash’s Faculty of Information Technology (IT). His current research areas include the development of IT-based systems for managers, business intelligence, data warehousing and IT governance. He is the author of more than 60 scientific papers in the decision support area, including papers in journals such as the European Journal of Information Systems, Information Systems Journal, Decision Support Systems and the Journal of Information Technology.
