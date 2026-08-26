---
otero_id: 16976
otero_key: "RHSTDP3Q"
title: "Decision support systems: Alternative perspectives and schools"
authors: "Charles B. Stabell"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90179-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision Support Systems: Alternative Perspectives and Schools

Charles B. STABELL \*

Norwegian School of Management, Bekkestua, Oslo, Norway

This paper reviews and compares four distinct decision support system (DSS) perspectives or ‘schools’: Decision analysis, decision research, decision calculus, and implementation process. Each school represents a relatively coherent perspective for DSS development; all four address the development and use of computer-based tools that support and aid managers in their role as decision makers. They differ, however, in terms of the nature of the decision situation envisaged, the phase of the decision process considered, the primary aims for a DSS development effort, the nature of the learning to be achieved and the phase of the development process that is emphasized. The purpose of the review is an attempt to establish a more constructive approach to understanding the central tenets and challenges for DSS. At the same time, the unique concerns and distinct contributions of the different schools suggest that it is difficult to define a single approach that satisfies equally well all considerations and all demands.

![](/api/attachments/RHSTDP3Q/fulltext/images/fd21e41d798eae403244c86c39d2373c539657da456d460313f741648a7367b4.jpg)

Charles B. Stabell is presently professor of administrative and cognitive sciences at the Norwegian School of Management, Bekkestua (Oslo), Norway, He did his Ph.D. work at the Sloan School of Management, MIT, and has formerly been on the faculty of the Graduate School of Business, Stanford University and the Norwegian School of Economics and Business Administration. Dr. Stabell is the editor of the Addison-Wesley series on Decision Support. His current re-

search interests are the decision research approach to the development of decision support systems, decision making in organizations, organizational design, and the economics of information systems.

\* In preparing this paper, I have received many valuable comments and suggestions from Anna Mette Fuglseth, ∅yvind Bøhren and Benn Konsynski.

## 1. Introduction

This article grew out of a frustration that I experienced when asked to give an introduction to Decision Support Systems and define what a DSS is. Implicit in the question is most often a notion that a DSS is a specific and well-delineated class of computer-based systems. This is not too surprising as the recent surge in interest in DSS has closely paralleled the dramatic developments in information technology these last 5–7 years. Examples from this development are the personal computer, dynamic spreadsheets, expert systems and telecommunication networks.

From my point of view, trying to define what is unique about DSS technology is not a very useful exercise. The technological building blocks – the hardware and the software components – in isolation distinguish only to a very limited extent DSS from other computer-based systems. The key characteristics of DSS are linked to the context where such systems are to be used, to why and how the systems are developed, and to how the systems are intended to be used: DSS are systems developed to support managers' decision making processes in complex and ill-structured decision situations [Keen and Scott Morton (1978)].

At en early IFIPS conference on DSS, George Huber (1980) introduced the distinction between 'dss' and 'DSS', where only the latter are computer-based. His point was to set computer-based decision support in perspective, and suggest that decision support is commonplace and a vital part of management in all organizations. And as a consequence he suggested that a key requirement for effective decision support is that the DSS fit the manager's dss. Huber was making an important point, but apparently failed to consider that the most distinct attribute of DSS is that it provides decision support by design: while 'dss' is a form for decision support that has evolved naturally, a 'DSS' is an artificial system [Simon (1981)]. The act of developing a DSS therefore also focuses attention on the decision making role of managers and thus also articulates decision support capabilities in the natural environment of the manager.

DSS are thus not a particular technology in a restricted sense, but primarily a perspective on management, the role of computer-based systems as a management tool and how to realise this vision in practice. There is therefore obviously also room for several different perspectives on DSS, just as there exists a number of different perspectives on management and on the potential role of new technology in management.

This paper presents and compares four relatively unique and distinct DSS ‘schools’:

\- decision analysis [see, e.g., Keeny and Raiffa (1976), Holloway (1979), Pitz (1981)],

\- decision calculus [see, Little (1971), Montgomery and Weinberg (1973), Lodish (1981)], - decision research [see, e.g., Scott Morton (1971), Gerrity (1971), Stabell (1983)],

\- implementation process [see, e.g. Keen (1980), Courbon et al. (1978), Ness (1975)].

Opinions will obviously differ on what might be defined as the relevant set of DSS schools. The four schools reviewed in this paper should be considered a first attempt at identifying a set of distinct and well-articulated perspectives on DSS development. They have both a commercial and an academic following. In other words, all four have been both used in practice and evaluated/extended through more systematic research efforts. They have in common that they consider both the development and the use of computer-based systems that support managers as decision makers.

The purpose of this review is to attempt a more constructive approach to the concept of a DSS. Decision support systems are usually contrasted with other systems. This was to a large extent the approach taken by Gorry and Scott Morton (1971) when they introduced the term. It often leads to a presentation that emphasizes, and possibly exaggerates, the new and salvatory aspects of DSS. By focusing the diversity of the concept, I think we can get a more realistic perspective on both the potential and the limitations of decision support systems.

By acknowledging that each school has made significant contributions, we also underline that to develop a successful support system necessitates that we choose approach. Even though we in practice neither can nor wish to follow any school in its pure form, I think that the diversity of schools tells us something about the difficulties of selecting an approach that can do everything for everybody. In order to find one's own approach, however, it is useful to be exposed to and understand the underlying assumptions and orientation of the different schools.

The remainder of the paper is organized as follows. First, the four schools are briefly reviewed in sections 2 to 5. This overview only outlines key points; those who wish a more comprehensive and complete presentation should consult the references. The outlines obviously do not try to cover all variants, but should rather be viewed as an attempt to destill and sharpen the central ideas and common elements in each school. Section 6 compares the four schools, while the final section considers the builders and providers of DSS technology, the ‘school’ that obviously has the greatest attention and the largest following in terms of resources and commitment.

## 2. Decision Analysis (DA)

Decision analysis (DA) is in many ways the oldest, the best established and the most articulate DSS-school. The foundations are modern microeconomic and statistical theory for decisions under uncertainty with multiple goals. DA is primarily known as a prescriptive school for how to make decisions; it provides a methodology for both structuring decision situations and making rational choices. The same fundamental perspective on decision making, however, is also the conceptual basis for more descriptive, behavioral research on how decisions are made [see, e.g., Hogarth (1980)].

In terms of the practice of decision making, DA was initially presented as a general methodology, without any reference to the use of computer-based systems. Computer-based decision aids were subsequently introduced as a means to facilitate the application of the methodology and thereby extend its use.

In common with most analytical methods, DA attacks complex problems by reducing them into smaller, manageable components. The unique characteristic of DA is how the problem is decomposed. According to the method, all decision situations both can and should be defined in terms of the following four elements:

\- options/alternatives,

\- events/states of nature with corresponding probabilities,

\- outcomes/results with corresponding probabilities,

\- goals/preferences.

A decision is viewed as a sequence of choices, that are conditioned by outcomes from earlier choices and the non-controllable intervening events. The decision process consists of identification of all events and corresponding outcomes that might be relevant to the realization of the decision maker's goals. The decision maker's preferences across the alternative outcomes and estimates of the probabilities for the different events, and thereby for the outcomes, are determined. The decision situation is frequently summarized in a decision tree or decision diagram.

The method is general and independent of the content (substance) of the decision situation. DA is therefore also most often applied in non-repetitive decision situations, involving either strategic decisions in organizations (e.g., location of a new airport or termination of business unit) or naive decision makers in a non-organizational context (e.g., looking for a job, education or a residence).

DA focuses the choice phase of the decision process. Problems (e.g., that the decision maker wants to build a new airport or get a job) are assumed to exist before the method is brought to bear on the decision. The method therefore has had little to provide the initial problem finding and problem defining phases of the decision process, other than to underline that these are critical activities for a successful application. The method does not support the post-choice phases of the decision process.

The decision maker is the key source of inputs. This pertains to the method's focus on the decision maker's subjective estimates and preferences. The approach does not restrict analysis to what is available from more formalized data sources, but is anchored to how the decision maker defines the decision situation. The method has also been designed to handle situations with multiple decision criteria that cannot be summarized in a single index.

The key criterion for decision quality is consistence: That a choice is consistent in terms of all information available concerning alternative events, judgement concerning uncertainty and the decision maker's preferences.

Studies of our ability to provide good estimates of probabilities and preferences, suggest that the human information processor is a ‘cognitive cripple’ who frequently resorts to simplifying heuristics in order to overcome a limited and finite information processing capacity [see, e.g., Tversky and Kahneman (1974)]. These results motivate both DA as a method and the use of computer-based tools as a means to ease the application of the method.

Computer-based versions of DA primarily help quantify the decision maker's own (subjective) preferences and probability estimates. The division of labor between decision maker and tool is such that the decision maker provides all the inputs and the system integrates this data by ranking the different choice alternatives identified. The dialog between user and system is designed to assist the decision maker estimate the relevant inputs and minimize distorting simplifications and biases.

In DA, the computer-based system most often is referred to as a decision aid. Compared to a reference to support systems, this term suggests a recognition that the system to a large extent is a simple tool in the form of a calculator that transforms (integrates) the data provided by the decision maker. By using the tool metaphor, the school seems to emphasize that the aid is no better than the decision maker that uses it.

## 3. Decision Calculus (DC)

The reference discipline [see Keen (1980)] for the decision calculus (DC) approach to DSS development is operations research (OR). The concept of a decision calculus was proposed by John Little (1971) in response to the perennial problem for traditional OR efforts: Lack of use or misuse in the decision process.

DC is a model-based set of procedures for processing both data and judgement. The model is the organizing element and is designed to support the manager's use of judgement and experience in the decision process. These goals are achieved by developing a model-based supported system that is

\- simple so that it is easy to understand,

\- easy to control and communicate with by permitting immediate and interactive modification of all inputs,

\- robust in the sense that it is difficult for the system to produce unrealistic results,

\- complete on important issues, and

\- adaptive so that the system can be updated as new information becomes available.

A key design philosophy that secures completeness is allowing for the input of subjective judgements on inputs and model parameters. Particularly in order to provide direct and immediate communication, Little (1971) prescribed the use of interactive computer-based systems as the preferred medium for realizing a decision calculus.

Conflicting design objectives such as simple, robust and complete imply difficult tradeoffs. They cannot be resolved in general terms, but must consider characteristics of the particular user and decision situation. Developing a decision calculus should therefore be anchored in the decision maker's own model of the decision situation [Montgomery and Weinberg (1973)]. The procedure used first elicits a verbalized version of the decision maker's intuitive model. This model can then be transformed into a formalised version in mathematical/analytical form. In the next step, all available data (both estimates based on historical data and the decision maker's own judgements) are used to calibrate the parameters of the model and the exogenous variables. The model-based support system is then used repeatedly through several decision cycles. Through tracking and evaluation of decision calculus results, the user can gradually improve both the model and the estimates of model parameters.

DC is best known for applications in support of marketing decisions [Little (1979), Lodish (1981)]. This can perhaps in part be attributed to that John Little, the first to expose the DC ideas, has been associated with marketing. However, it is probably also because marketing traditionally has worked with explicit models of consumer behavior. In this context, DC has primarily considered two major classes of models of consumer behavior: flow models and aggregate response models.

DC focuses the decision situation. The goal is better decisions through better models of the decision situation. DC typically targets the problem solving and choice phases of the decision processes. The approach is less concerned about supporting the problem finding phases of the decision process. Monitoring and evaluation of decision outcomes is primarily a means to follow-up and adjust model parameters and model structure.

## 4. Decision Research (DR)

While the decision calculus (DC) school primarily considers the model of the decision situation, the decision process and the decision maker are the central concerns for decision research (DR).

DR views DSS development as an effort to improve the manager's decision making process – an attempt to increase the effectiveness of how decisions are made. Design of the DSS must therefore be based on a mapping and diagnosis of the existing decision process. Diagnosis is the identification of problems (or opportunities for improvement) in current decision behavior. It involves determining how decisions are currently being made, specifying how decisions should be made, and understanding why decisions are not being made as they should be. Thus DR requires both describing current decision behavior and prescribing how decisions should be made.

DR has to a certain extent evolved from concerns in management information systems (MIS). However, the work associated with Herbert Simon and the Carnegie school's view of decision making behavior in organizations has been a main intellectual influence. The key contribution, beyond the fundamental view of management as primarily choosing what to do, is the recognition of managers in general as rational in a bounded sense [Simon (1977)]. Bounded rationality is a concept of rationality that recognizes contraints internal to the decision maker. It is a perspective that identifies two conceptually distinct roles for efforts to improve decision making. First there is a largely remedial role: Although bounded rationality implies that decision makers in general are rational given the constraints and limitations of their information processing capacity, it does not imply that all behavior is equally rational in all circumstances. From this perspective, DR is a means to identify and help reduce ineffective decision behavior.

Second, a DR effort might involve redefining the bounds of rational behavior by increasing the decision maker's apparent information processing capacity. Such increases can either be achieved by rearranging and transforming internal constraints through training and cognitive development, or by providing external extensions of the manager's internal information processing capacity through a DSS.

Development of DSS according to DR requires using multiple models, along with the empirical methods for applying them, to map current decision behavior. It is important that these models with methods are grounded in research on human decision behavior.

Another key principle for DR is that the support system should be designed to support the existing decision process, while use of the system should also stimulate and channel behavior towards the prescribed process.

DR considers primarily how to develop a DSS. The school has less to say about the system that is to be developed. This can is due to that the approach views computer-based support as only one of several possible means to improve decision making. Another reason that the school has not embraced a particular support system architecture is that system design should follow from the diagnosis of the current decision behavior. DR has therefore also primarily considered the analysis phase in DSS development.

## 5. Implementation Process (IP)

The implementation process (IP) school has many names and exists in numerous variants: middle-out design, adaptive design, l'approche évolutive, evolutionary development. As the label suggests, the common element is a concern for the implementation phase of the DSS development process. As such the IP-approach is grounded in, and is largely a response to, the early experiences with problematic and limited use of OR tools and management information systems in general.

Satisfied users is the primary goal. System use is most often the operational criterion for successful implementation. Here IP distinguishes between system installation and implementation. Installation only deals with the physical distribution of equipment and training of users in the mechanics of system use. Implementation also requires active use of the support system by the manager. However, the intent is securing system use, while less is said about how to secure useful uses of the system.

A central notion is that implementation is not an issue to be dealt with after a system has been designed. Successful implementation requires that it be considered right from the start of the system development process. Guidelines for successful implementation suggest that it is important to start simple, get started quickly, and gradually improve and extend the system as experience is gained through the interactions between user, system and builder. A good problem and a good user are often suggested as key prerequisites for effective development of support systems.

The system development process is viewed from a builder perspective. The approach is particularly concerned about the builder's role in the development process as she interacts over time with the user and the evolving system. The school distinguishes between the adaptive links that define three learning loops in an effective development process [Keen (1980)]: The cognitive loop where system use stimulates user-learning, while the user on the other hand develops new and personalized patterns of system use. The system evolution loop considers both the builder's learning of needs for system evolution based on a constant monitoring of system use, and system evolution through the builder's active adaptation and extension of functions and capabilities. The interaction between user and builder defines the implementation loop. This loop focuses on the builder's role as a change agent, assisting the user both clarify needs for support and make use of the evolving system.

The IP-approach is development process oriented. The approach has little to say about the system that is to be implemented. The development process thus has many properties of a non-directed change process, where the only common goal is that the system developed be used.

Learning in the development process is primarily embodied in the system that gradually evolves. The IP-school has less to say about user learning, other than that such learning requires an adaptive approach to system development. The approach is therefore also particularly concerned about means to secure a flexible development process that can adapt to possible unintended and unanticipated impacts of the support system.

## 6. Discussion

The four schools presented in outline form can now be summarized and analyzed by attempting a comparison across schools. First, however, let us underline what all schools apparently have in common. All four focus on management decision making, although the IP-approach is less explicit in terms of an exclusive decision focus. All emphasize support as the appropriate role for computer-based systems in this context. None deals explicitly with the distinction between operational, tactical and strategic decisions. This latter point is a clear shift in emphasis from the early work by Gorry and Scott Morton (1971).

Differences in approaches can be interpreted in terms of how each school views and approaches key aspects of the context, the role and the impact of the support system. Consider the type of decision situation, decision process focus, main goals, learning to be achieved, resolution of decision situation complexity, system development focus and reference discipline:

Type of decision situation. To what extent is the system designed to support repetitive decisions or a one-shot, infrequent decision. DC and DR have typically been applied in efforts to develop support for relatively repetitive decisions such as advertising budgeting or purchase and sale of securities. DA, on the other hand, has most often been applied to aid one-shot decisions. Although there are obviously many exceptions to this pattern, the differences can be attributed to fundamental characteristics of the four schools. Thus, DA is primarily useful in novel or unfamiliar decision situations where substantive knowledge is limited and that imply relatively irreversible choices. DR, on the other hand, presumes established decision procedures and behavior that can be mapped and diagnosed. Similarly, DC requires a relatively short decision cycle so that model parameters and model structure can be improved through feedback and tracking of decision outcomes. It is less clear how to classify the IP-school. However, this approach is often used by builders and consultants that have a time-limited relationship to the decision situation and decision maker. The relationship between the development effort and the decision situation is therefore in many ways as if the latter were a one-shot affair.

Decision process focus. The phase(s) or step(s) in the decision process to be supported. We distinguish the problem finding, problem solving, choice, realization and monitoring/control phases of the decision cycle. Choice is the primary target phase for both DA and DC, while DR is an approach that considers the whole decision cycle. One might say that the IP-approach also focuses the whole process. However, IP does this with little conscious attention to a decision process perspective.

Primary aims. The school's more or less explicit assumptions concerning the overall goal for DSS development efforts. Simplifying quite a deal, we can say that while DA primarily seeks to secure decisions that are consistent, DC sees development of a better model of the decision situation as the overriding goal. An improved decision process in terms of how decisions are made is the objective for a DR-based development effort, while use of the support system is the ultimate goal for the IP-school.

Learning. Where is the learning to be embodied, in the decision maker, decision process or the support system. It is primarily DR that explicitly considers decision maker and decision process learning, while the three other schools focus on learning that materializes in the support system or model-system. It is perhaps somewhat paradoxical to suggest that DA as a one-shot effort can have a learning orientation. However, DA considers decision making as a sequence of choices, where each step relies on probabilities that are revised in light of new information.

Handling lack of structure. We distinguish between two fundamentally different approaches to decision support: either support by bringing structure to the unstructured decision situation or support by aiding the decision maker embrace and explore the lack of structure in the situation. DA imposes a particular structure (alternatives, events, outcomes and preferences) on the decision situation. DC also structures the decision situation, but with models that are situation specific. For DR, the support system is designed to assist the decision maker explore and explicitly recognize uncertainty and complexity. IP can be seen as an approach that tests a structure for the decision situation (to see if it will be adopted and used).

Development process focus. The primary development activity considered. We distinguish between the analysis activities that conclude with a specification of system requirements, the design activities that produce both the functional design and a computer-based version of the system, and implementation that results in system use. IP is primarily concerned about implementation, although a key point for this school is that implementation needs explicit consideration throughout the entire system development process. Both DA and DR primarily focus the analysis phase, but for slightly different reasons: DA as both design and implementation are standardized and relatively simple activities. In DR, analysis is the most important activity and the school has relatively little to say about the design of the DSS. Design and evaluation of the model-tool is the central activity for the DC-approach.

Table 1 summarizes the main distinctions and differences. The final row attempts to distinguish the schools in terms of what might be defined as the reference discipline or professional roots of the school.

A main point for the review presented in table 1 is that it can be seen an outline of key issues for the development of DSS. It thus also defines core elements of DSS as a discipline and an application area. At the same time the table suggests that no single school emerges as the most appropriate for DSS development. Or stated differently, each school makes significant contributions, but is also incomplete in terms of a number of important dimensions.

A synthesis would seem to be called for. Our experiences the past 10–15 years suggest that it will be difficult to achieve a synthesis. One important reason is that it takes quite some time to master any single school. The potential for synthesis, however, can be tentatively outlined by considering subsets of the four schools.

DA and DC have in this sense much in common: Both focus the choice phase of the decision process; both try to structure and thereby simplify the decision situation. A main difference is however that DA is very much a general method that is meant to be applicable in any situation, while DC as a method emphasizes capturing and encoding the situation specific and unique aspects of the decision context. DA relies on a model of common elements in all decision situations, while DC focuses models of means—ends relationships.

The DR approach is relatively unique in that it deals explicitly with the differences between what is (description) and what ought to be (norm). In this sense, DR is the sole school that assumes that the main value of efforts to develop a DSS is related to learning and changes embodied in the manager as a decision maker. In this there is also an explicit assumption that the manager does not necessarily always know best, and that therefore all uses of support systems are not always desirable or effective.

Comparison of alternative DSS-schools.

<table><tr><td></td><td>Decision Analysis</td><td>Decision Calculus</td><td>Decision Research</td><td>Implementation Process</td></tr><tr><td>Type of decision situation</td><td>single shot</td><td>repetitive</td><td>repetitive</td><td>? (single shot)</td></tr><tr><td>Focus in decision process</td><td>choice</td><td>problem solving, choice</td><td>whole decision cycle</td><td>?</td></tr><tr><td>Primary aims</td><td>consistent decisions</td><td>better model</td><td>effective decision process</td><td>use of support system</td></tr><tr><td>Learning</td><td>conditional probabilities</td><td>model of decision situation</td><td>DMr &amp; decision process</td><td>support system</td></tr><tr><td>Handling lack of structure</td><td>impose a structure</td><td>structure</td><td>explore lack of structure</td><td>? (test structures)</td></tr><tr><td>Focus in DSS development process</td><td>analysis</td><td>design</td><td>analysis</td><td>implementation</td></tr><tr><td>Reference discipline</td><td>micro economics</td><td>OR</td><td>decision making in organizations</td><td>‘consulting’ OD</td></tr></table>

It is useful in this latter context to contrast the DR and IP approaches: While DR can be viewed as a method for a more ‘bureaucratic’, systematic goal-directed change process, IP is a more ‘happy warrior’, opportunistic change process that is not directed towards a clear goal. As apparent in table 1, IP is thus also the approach that is the least explicitly linked to the development of decision support systems. The contrast suggests the following potential and limitations of each particular school: IP is the approach that can secure use, but with only limited guarantee that it is not also misuse or ineffective use of the support system. DR, on the other hand, attempts to identify up front sensible uses in the context of a more effective decision process, but frequently ends up not being able to produce operational and implementable changes. Or restated in terms of Huber’s distinction between ‘dss’ and ‘DSS’, the DR-approach would seem to imply that effective decision support can only be achieved by design. IP, on the other hand, would seem to emphasize that establishing a viable (decision support) practice can only be realized through a natural, evolutionary process.

## 7. Concluding Remarks

It is perhaps useful and necessary to conclude by commenting one obvious omission in this review of alternative DSS schools and perspectives. Although I would maintain that the four schools considered represent the most important intellectual contributions, it is apparent that ‘builders’ of DSS technology might be considered the largest school in terms of number of actors involved and committed resources.

For this school technology is the key element. The road to better decisions is through better technological solutions. Most of the work in this school is in the form of DSS-generators and DSS design methods [see, e.g., Sprague and Carlson (1982)]. Generators and design methods, however, are only to a limited extent restricted to or focused on decision support [Stabell (1983)], but serve instead as a platform for the development of support systems in general. A main link to decision support is the identification of features that a generator must satisfy in order to serve as a basis for the development of effective decision support systems [see, e.g., Reimann and Warren (1985)]. Such requirement specifications for technological building blocks are useful, but I think the user is best served by a definition of the DSS-concept that is not bound to a particular technology.

The point is not that technology is of no importance. Rather, it is an argument for keeping our attention focused on the central theme: Better decisions and decision support. A viable DSS-school should provide a perspective on how we might apply any technology, existing and future, as a means to achieve these ends.

## References

Courbon, J.C., J. Grajew, J. Tolovi, Decision Support Systems: An Evolutionary Approach to Design and Implementation, Working paper, Institut d'Administration des Entreprises, Université de Grenoble (1978).

Engländer, T., m.rl., ed. Proceedings of the Eighth Research Conference on Subjective Probability, Utility and Decision Making, Budapest (1981).

Gerrity, T., The Design of Man-machine Decision Systems: An Application to Portfolio Management, Sloan Management Review 12(2) (1971) 59–75.

Gorry, G.A. and M.S. Scott Morton, A Framework for Management Information Systems, Sloan Management Review 13(1) (1971) 55–70.

Hogarth, R.M., Judgement and Choice: The Psychology of Decision (Wiley, New York, 1980).

Holloway, C.A., Decision Making under Uncertainty: Models and Choice (Prentice Hall, Englewood Cliffs, NJ, 1979).

Huber, G., Organizational Science Contributions to the Design of Decision Support Systems, in: G. Fick and R.H. Sprague jr., eds., Decision Support Systems: Issues and Challenges (Pergamon Press, London, 1980).

Keen, P.G.W., Adaptive Design for Decision Support Systems, Data Base 12 (1–2) (1980).

Keen, P.G.W. and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective (Addison–Wesley, Reading, MA, 1978).

Keeny, R.L. and H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs (Wiley, New York, 1976).

Little, J.D.C., Models and Managers: The Concept of a Decision Calculus, Management Science 16(8) (1971) B466–485.

Little, J.D.C., Decision Support Systems for Marketing Managers, Journal of Marketing 43 (Summer, 1979) 9–26.

Lodish, L.M., Experience with Decision-Calculus Models and Decision Support Systems, in: R.L. Schultz and A.A. Zoltners, ed., Marketing Decision Models (North Holland, Amsterdam, 1981).

Montgomery, D.B. and C.B. Weinberg, Modeling Marketing Phenomena: A Managerial Perspective, Journal of Contemporary Business (Autumn 1973) 17–43.

Ness, D., Interactive Systems: Theories of Design, Joint Wharton/ ONR Conference on Interactive Information and Decision Support Systems (The Wharton School, Department of Decision Sciences, University of Pennsylvania, Philadelphia, PA, 1975).

Pitz, G.F., Human Engineering of Decision Aids, in T. Engländer m.fl., ed, Proceedings of the Eighth Research Conference on Subjective Probability, Utility and Decision Making, Budapest (1981).

Reimann, B.C. and A.L. Warren, User-oriented Criteria for the Selection of DSS Software, Communications of the ACM 28(2) (1985) 166–179.

Scott Morton, M.S., Management Decision Systems: Computer Based Support for Decision Making (Division of Research, Harvard University, Cambridge, MA, 1971).

Simon, Herbert, The New Science of Management Decisions (Prentice Hall, Englewood Cliffs, NJ, 1977).

Simon, Herbert, The Sciences of the Artificial (MIT Press, Cambridge, MA, 1981).

Sprague, R.H. Jr. and E.D. Carlson, Building Effective Decision Support Systems (Prentice Hall, Englewood Cliffs, NJ, 1982).

Stabell, Charles B, A Decision-oriented Approach to Building Decision Support Systems, in: J. Bennett, ed., Building Decision Support Systems (Addison–Wesley, Reading, MA, 1983).

Tversky, A. and D. Kahneman, Judgement under Uncertainty: Heuristics and Biases, Science 185 (1974) 1124–1131.
