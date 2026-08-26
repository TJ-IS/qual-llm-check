---
otero_id: 18368
otero_key: "HQFKFZP7"
title: "On building expert systems for strategic planners: A knowledge engineer's experience"
authors: "Michael Goul"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90075-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On Building Expert Systems for Strategic Planners: A Knowledge Engineer's Experience

Michael Goul

Department of Decision and Information Systems, College of Business, Arizona State University, Tempe, AZ 85287, USA

Expert Systems are often touted as the next major research frontier for scholars interested in developing computer based applications to support business decision making activities. This paper explores the process of building an expert system for planners performing strategic situation assessment. A Situation Assessment Expert System (SAES), in experimental use at the Oregon State University College of Business is presented. The process of building this system has provided important insights for future system designers working in the strategic planning domain. The paper proposes a framework for future system construction.

Keywords: Expert Systems, Decision Support Systems, Strategic Planning, Situation Assessment, Strategic Issue Analysis, Environmental Scanning.

![](/api/attachments/HQFKFZP7/fulltext/images/8b31b08b84a721a8f7bb8f2259910b46e34bcf5ef409c77f70a207f3b9580223.jpg)

Michael Goul is an Assistant Professor of Computer Information Systems at the College of Business Administration of Arizona State University. He received a Ph.D. degree in Computer Science and a Master's degree in Business Administration from Oregon State University. Dr. Goul's research interests include the integration of decision support systems and expert systems, and artificial intelligence in business. His publications have appeared in the Journal of Management

Information Systems, and Decision Sciences.

## 1. Introduction

The art of strategic planning is characterized as a series of phases beginning with situation assessment [6], strategic issue analysis [21] or environmental scanning [9]. Planners formulate the business definition, determine the current position, identify assumptions, and determine issues in need of attention. The phases following situation assessment include strategy generation and evaluation, implementation, and monitoring.

Computers assist planners by aggregating data in meaningful ways, presenting results in a form conducive to human assimilation $[8,11,17,19]$ . There are usually different opinions of the picture painted by the data, and planners often choose to hire consultants to assist in interpretation and analysis [e.g., 3].

Advances in the field of artificial intelligence suggest that there is potential for building systems capable of acting as intelligent assistants to strategic planners. In the domain of strategic planning, an intelligent assistant's level of performance would probably be the performance of a planning specialist. Current expert systems (ES) perform tasks less complex than situation assessment, but researchers have begun to suggest ways to move the technology up the organizational ladder [7].

A new style of systems analyst, called a knowledge engineer, works closely with an expert to "mine" the expert's decision making process. Knowledge is encoded into a knowledge base, and an inference engine manipulates the knowledge base to perform a task. The algorithm is not necessarily an algorism of the expert's behavior; it is an interpretation of the process by the knowledge engineer, translated into a machine executable format.

This paper presents an investigation of ES designed for strategic planners; it focuses on practical results gleaned from developing an experimental Situation Assessment Expert System (SAES).

## 2. Related Work

Four areas of related work are the basis of a framework for building ES for strategic planning activities: 1) The nature of computer support for organizations, 2) Current frameworks for building ES, 3) A model of decision making that serves as a theoretical basis for SAES, and 4) The design criteria employed in building a Decision Support System (DSS).

## 2.1. Technology by Organizational Level

At the lower level of an organization, operational decisions are made on a routine basis. The middle level provides both operational and management control, involving the acquisition and use of resources. At the apex, decisions are strategic; they involve establishing policies, setting objectives, and selecting resources.

A typical organization's computer support uses some ES at the lowest level as an addition to traditional Transaction Systems (TS). At the middle level, Management Information Systems (MIS), and DSS are used in evaluating the effectiveness of: the work force, inventory policies, purchasing policies, etc. While MIS and DSS extract data from TS, ES have typically been implemented as stand-alone.

ES techniques have not generally been used at the top levels of the organization. Several reasons are:

1. Primitive Technology: Inference techniques are still somewhat primitive. Current constructs best fit domains where knowledge is easily codified. For example, there is wide disagreement as to how the systems can best combine evidence.

2. Benefits are Unclear: Knowledge engineers have concentrated on projects where the benefit can be easily evaluated. As one moves toward the top level of the organization, it becomes difficult to assess the quality of longer-term decision making.

3. Personnel Constraints: Trained knowledge engineers are in short supply.

4. Necessity for In-House Development: Many organizations are not aware of ES and its potential impact - ES that can be purchased often take precedence over systems developed in-house. Widely distributed systems are likely to solve generic problems, while most strategy problems are organization or industry specific.

5. Insufficient Experience: There is no widely adopted framework for building ES, especially for upper levels of the organization. In addition, current frameworks tend to neglect the needs of the end user.

## 2.2. Current Approaches to Building Expert Systems

There are currently two design methodologies for building ES: Heuristic [10] and Staged [16] approaches. There is very little work on the successes and failures of these, as most literature concentrates on the techniques for inferencing and knowledge base schemas, as well as validation of the system's performance. Designers have typically validated systems by seeking to answer the question, "Does the system produce the same decision as the expert when given a particular problem?" There has been little attempt to validate a system by attempting to answer the question, "Does the user of an ES make better decisions by using it?"

It is likely that few knowledge engineers follow a particular framework, partly because of the apparent variance of the process for each new project. In attempting to extend ES technology up the organizational pyramid, new frameworks are likely to take shape only by building actual systems.

The Heuristic approach relies on the rules-of-thumb presented in Figure 1. A recent framework, the Staged approach, is shown in Figure 2. There are two major differences in the approaches:

1. Retool vs. Reject Project: The heuristic approach suggests that the knowledge engineer build

Fig. 1. Heuristic Approach (Adapted from [10]).

![](/api/attachments/HQFKFZP7/fulltext/images/ba233ee9a170ff45f5cacd68c68f41842bf5032e6f3c291c6d22f08f2683db83.jpg)  
Fig. 2. Staged Approach (Adapted from [16]).

a new tool if normally used tools do not work. The staged approach suggests that projects requiring new tools be rejected.

2. Complex vs. Historical Techniques: The staged approach accepts conventional programming methods when the knowledge for a specific task is stable, numerical, and easily aggregated. The heuristic approach suggests that all ES require weighting procedures to reflect the strength of belief in inferences made by operations of the inference engine.

These differences suggest subtle disagreement between knowledge engineers on the process of constructing ES. The process is an art; it eludes complete description, even by those who practice it. However, with either approach, the system produced may not be fitted to the needs and desires of the end user.

## 2.3. A Decision Making Model as a Basis for the Framework

A nonroutine decision defies complete specification. Such is the nature of strategic planning. Current ES determine a solution given a problem. However, the major difficulty in nonroutine decision making is the inability to separate the real problem from symptoms or manifestations [4]. Therefore, as a first thrust for this technology, a focus on problem identification as opposed to problem solving is appropriate. The intent of the system should be to guide, tutor, and aid the decision maker in correct problem recognition and diagnosis: the activity performed by consultants for many organizations.

An expert system construction framework must be based on sound theoretical underpinnings. One major work provides this underpinning $[20]$ . Figure 3 presents this model of problem solving. The model decomposes the process into two discrete components: “problem finding” and “problem solving.” The problem finding component is the basis for the system described in this paper.

## 2.4. Decision Support System Design Tenets

DSS are designed mainly for use in the upper organizational levels. One process of DSS design is characterized by the acronym: “ROMC” [2]. First, DSS builders focus on those Representations familiar to the decision maker, and that are used in the task. Second, Operations on those representations become the focus. Third, the DSS builder targets built-in Memory aids. Last, Control is designed. These steps are combined with a development process called facilitative implementation and middle-out design.

Facilitative implementation and middle-out design result in a prototype system. While this may not contain all of the capabilities of the ultimate system, it is meant to require minimal programming effort. As soon as possible, the prototype is used and evolutions begin. A major goal is to promote user learning about the decision task.

The tenets underlying DSS design are characterized in Figure 4. There are three main loops: the cognitive loop includes the concepts of personalized use and user learning; the “implementation” loop involves the middle-out design and facilitative implementation concepts; and the “evolution” loop captures the ongoing process of improving the DSS [18].

## 3. The Mistakes of a Knowledge Engineer in Action

The framework for building ES for strategic planners was not devised before major work began on SAES. Here we present a post-development reflection of what went right and wrong during the process.

![](/api/attachments/HQFKFZP7/fulltext/images/64dcff15efc94340b3fbcc643c962ed5f49ebc0441ab099c238cfa2f9e6b4eb1.jpg)  
Fig. 3. Decision Making Model (Adapted from [20]).

3.1. Selecting the Problem and Building the Prototype Expert System

Existing expert system design frameworks suggest that useful, interesting problems [10] or minor, troublesome problems [16] are the best candidates for a knowledge engineer's attention. Further, problems that are well-bounded, are defined as precisely as possible, and take an expert about three hours to five weeks to solve, are suggested as appropriate expert system tasks [16].

![](/api/attachments/HQFKFZP7/fulltext/images/274d6c5deb3f52596f5a4606cbbe2d7c7d34339520ed82d2fca51c9349be202d.jpg)  
Fig. 4. DSS Design Criteria (Adapted from [18]).

While situation assessment is certainly a useful and interesting problem, it is far from being well-bounded and a minor, troublesome problem. Existing design definitions are simply too incomplete for building practical ES at the upper managerial level.

Relying on criterion from [10] and [16], a meeting was held with a strategic planning expert (an Oregon State University professor of Strategic Planning who has significant planning experience) to identify a preliminary approach aimed at situation assessment. From this initial encounter, it became apparent that the entire spectrum of potential applications was impossible to cover. Addressing organizational structure was chosen as a good start. Armed with two good sources ([1] and [5]), a prototype version was built to demonstrate the promise of the technology, and to secure a commitment for developing a complete system. The preliminary version was delivered, tested by the expert, and demonstrated to colleagues.

The prototype system, given information about an industry, the nature of production tasks, and other dimensions, along with the nature of the current organizational design, searched for theoretical inconsistencies between the current structure and a suggested structure based on rules derived from $[1\ and\ 5]$ . The output consisted of a listing of flagged inconsistencies along with the appropriate theoretical rule(s) deemed to apply.

The prototype created unexpected controversy. It seems the theory underlying the approach implied that structure follows strategy, while many users felt that strategy follows structure. Further, the system output was criticized for not going far enough; the identification of an inconsistency, did not, by itself, provide a foundation for action. Several considerations for future system builders from this experience are:

Problem #1: Any system relying on controversial theoretical underpinnings is likely to be doomed from the onset. Selecting organizational structure as a problem to be targeted ignored the disagreements between experts.

Rule-of-thumb #1. PROBLEM SELECTION: Do not begin working with an expert until you can identify a problem from the perspective of an ultimate system user (the decision maker [DM]). Know and understand the needs of the DM, and exactly what the ES should and should not do for the DM. Further, recognize cases where theory to support the DM is controversial and not supported by conclusive research findings.

Problem #2: Construction of the strategy ES began prematurely and was discarded, primarily because of a naive understanding of user needs.

Rule-of-thumb #2. SELECTING THE EXPERT: Involve an expert only after a problem has been identified. Choose the expert on the basis of documented abilities to tackle the problem. Make sure the expert's abilities are evaluated and approved by the DM. As a knowledge engineer, you work for the DM. Of course, the expert must willing to spend a great deal of time with you, and be willing to commit to project completion.

Problem #3: Securing commitment from the expert was not balanced with securing commitment from the DM. This resulted in a system that was difficult to use.

Rule-of-thumb 3. BUILDING THE PROTOTYPE: Design the prototype to secure commitment from both the expert and DM. Consider the system to be a discretionary tool, which may or may not be used. Concentrate on the interface initially, and place relatively small emphasis on capturing the full extent of the expert's knowledge.

## 3.2. The Evolving ES

After the initial experience with the prototype, a renewed effort began. Because little research has been done on the effect of ES on decision making performance, a secondary goal was to test for such effects. This implied that the DM would be the subjects of an experiment.

The DM were senior undergraduate students enrolled in a strategic planning class. In order not to contaminate the experiment, surrogates who were enrolled in a similar graduate (MBA) class were used to solicit needs. The major task in both courses is to perform case analysis. Given a case description, a student analyzes the subject organization of the case, assess the major strategic problems facing the organization, and details a plan of action to cope with the problems.

The MBA students had already completed several case assignments, and complained that their major difficulty was in correctly identifying the strategic problems facing the organization. After learning about ES theory, the students suggested that a system designed to aid in recognition of problems would be most helpful. This suggested the need for an ES for situation assessment.

When students analyze a case, they pass through several phases: first, a conscientious reading and analysis of all financial documentation; second, a brainstorming activity encompassing identification of applicable methods theory from textbooks, lecture notes, outside sources (such as periodicals and books), and other students enrolled in the course. This provides a perspective of the organization. Thus, the students assess the current state of the organization, and identify its strategic problems.

In summary, by interviewing potential system users, the goals of the system were determined. However, considerable time was spent attempting to determine how to accomplish those goals.

Rule-of-thumb #4. TARGET AN ELEMENT OF THE DECISION MAKING PROCESS: The knowledge engineer needs to understand how the decision maker operates. Know the theory behind decision making and understand the phase to be supported. In short, identify the crux of the process.

A prototype system was developed to be reviewed by the surrogate DM's. It contained very little knowledge, and was only intended to test the ideas behind the design, much of which was borrowed from the DSS literature. The design was acceptable, and this created excitement on the part of the MBA's and the expert. The following ideas were employed:

Rule-of-thumb #5. FOCUS ON REPRESENTATIONS FAMILIAR TO THE DM: Use objects in the system familiar to the system users. There should be no mystery. Inferences must be explained in terms of familiar representations.

Rule-of-thumb #6. GIVE CONTROL OF THE SYSTEM TO THE DM: System control must be based on the representations used. Make the user feel as if the expert advice is available at the user's whim.

Rule-of-thumb #7. PROVIDE MEMORY AIDS IN THE SYSTEM: Provide mechanisms for the DM to record thoughts and insights throughout a session. The observations should be recorded in a familiar representation. A lasting record should be made of the observations for later recall. A mechanism should be provided to allow the DM to interpret statements and conclusions made by the ES.

Rule-of-thumb #8. PUT THE DM IN DI-ALOGUE WITH THE EXPERT: The system should not be static, it should provide a mechanism allowing the DM to record thoughts regarding the quality and thoroughness of the advice. These thoughts must be forwarded to the expert and necessary adaptations made.

The representations used in the system should be familiar to the expert as well as the user. The expert can describe problem solving methods to the knowledge engineer in terms of these representations. It then becomes easier to encode expert knowledge, and this speeds development of the system.

Rule-of-thumb #9. BALANCE THE REPRESENTATIONS FAMILIAR TO THE DM WITH REPRESENTATIONS FAMILIAR TO THE EXPERT: Involve both the DM and the expert in selecting the representations to be used.

Finally, a lesson was learned from the prototype that failed; any expert system for strategic planning activities must somehow find an equilibrium that integrates the opinions of more than one expert. This leads to a dilemma: multiple expert opinion may lead to contradictions. While one final answer is desirable, it is through the culmination of various opinions and models that the best situation assessment can be made [6]. This is reflected in the following:

Rule-of-thumb: 10. INTEGRATE EXPERT OPINION WHILE CLEARLY NOTING DISAGREEMENTS: Instead of providing a system that has all of the advice of a single expert, allow the system to suggest advice that may be contradictory. The state of strategic planning is such that no single model or set of models has all of the answers; present the opposing views. Leave it to the DM to integrate the experts' opinions, in the same way as occurs when several consultants offer different advice.

## 4. SAES: An Expert System for Situation Assessment

The design of our ES discussed previously is described in [13] and [14]. This overview is presented only to emphasize how the ten rules-of-thumb were addressed. In our experiment to determine the effect of the system on decision making quality, we found that identification of strategic problems was improved for those subjects who used the expert system in strategic situation assessment (see [12 and 15]).

![](/api/attachments/HQFKFZP7/fulltext/images/a6218a5c19d8d966b9bcd99175c7c6bf13e31502f9c3962dbdfaf0eb2dd59175.jpg)  
Fig. 5. Main Menu.

![](/api/attachments/HQFKFZP7/fulltext/images/55955d15da8bf7fa5195e66811fd9c9f75272f825b6ff1cac088547c4aa39281.jpg)  
Fig. 6. System Advice Example.

The questions, folders for investigation, and expert advice were solicited through many long discussions with the expert, and much use of the system by the expert. The elapsed time to complete the system was two years; it contains approximately 475 rules. Care was taken to include multiple expert opinion, even though this created contradictions in the advice offered by the system. Sources for the knowledge came from reviews of periodical literature, relevant textbooks, and the knowledge and skills of the expert. The completed system was validated before use by colleagues familiar with strategic situation assessment.

The representations used in the system are desk, file cabinet, and file folders, and the computer screen includes diagrams and choices based on them. Inside each folder are three pamphlets, the first contains a series of questions to be answered by the DM, the second contains inferences, which, based on answers to the questions, suggest other folders relevant to the decision situation. The third pamphlet contains actual expert advice and the reasoning behind that advice.

The main menu of the system is presented in Figure 5. On the desk is a switch. If this is set to a “Guided Session,” the DM is given a tour through the folders, where questions are asked, other folders are suggested for exploration, and expert advice is offered, pertaining only to the context of the current situation.

By selecting a “Non-Guided Session” from the

![](/api/attachments/HQFKFZP7/fulltext/images/bf056f28a85711b313ccfa57b891686ba4be297719a7f01526b0dcd2228b58ae.jpg)  
Fig. 7. Advice Explanation.

![](/api/attachments/HQFKFZP7/fulltext/images/6135a189791439ffa0b24d38aafa650f10ee7815f8e61014304e273a74e82c8d.jpg)  
A MARKET SEGMENT IS COMPOSED OF GROUPS OF CONSUMERS WHO POSSESS SIMILAR CHARACTERISTICS AND/OR NEEDS.

Fig. 8. System Dictionary.

main menu, the DM may choose to investigate the pamphlets of any particular folder. The folders included in the system are: 1) Diagnostic questions, 2) Emerging industries, 3) Capacity expansion, 4) Buyers and suppliers, 5) Industry evolution, 6) Competitive actions, 7) Market signals, 8) Entry: New business, 9) Fragmented industry, 10) Mature industry, 11) Declining Industry, and 12) Global industry. When this selection is made, the DM is asked the questions in the folder, and based upon answers, expert advice and the reasoning for the advice is generated. An example of a particular piece of advice is presented in Figure 6. The menu of choices includes a mechanism for the DM to ask why the advice was suggested, a means for the DM to use a scratchpad to record personal observations, and a mechanism to record

![](/api/attachments/HQFKFZP7/fulltext/images/cf004fd9435e3133a60f54d39e5f49f1dfa684ab73fd260a22e9c80f2206250e.jpg)  
Fig. 9. Session Trace.

<table><tr><td>EXPERT ADVICE CATEGORY: ENTRY BARRIERS</td></tr><tr><td>INTRODUCTION: NEW ENTRANTS TO AN INDUSTRY BRING ADDED CAPACITY, THE DESIRE FOR MARKET SHARE, AND OFTEN SUBSTANTIAL RESOURCES. PRICES MAY BE BID DOWN OR COSTS INFLATED, THEREBY REDUCING PROFITABILITY.</td></tr><tr><td>1. EXPERT ADVICE:The greater the cost of product failure for the customer, the slower that customer will be in adopting the new product.</td></tr><tr><td>WHY:Customers will seek to thoroughly evaluate and test new products if the cost of product failure is high.</td></tr><tr><td>2. EXPERT ADVICE:The greater the costs of opening up a market, (customer education, regulatory approvals, and technological advancements) the more risky early entry is.</td></tr><tr><td>WHY:Firms entering later will have the advantage of the newest processes without paying the development costs for early technologies.</td></tr><tr><td>3. EXPERT ADVICE:The greater the probability that early competition and market segmentation are developed on a basis different from that which will be important later in industry development, the more risky early entry is.</td></tr><tr><td>WHY:Firms entering early may develop the wrong skills and face high changeover costs.</td></tr></table>

Fig. 10. Advice Summary.

suggestions for the expert developer of the system. Figure 7 demonstrates such an explanation. In addition to these, a dictionary of terminology used in the system is available for the DM to use at almost any point in the session. An example use of the dictionary is shown in Figure 8.

Two historical traces of the DM's session with the system are captured. The first gives every answer to the questions, all of the advice offered, and any comments left for the expert by the DM (See Figure 9). Another groups the advice offered by the system relative to the orientation of that advice; Figure 10 shows the advice generated in a session of the system related to “Entry Barriers.”

Design rules were addressed in this system as follows. First, as exemplified by the advice shown in the Figures, the system presents models deemed relevant to the DM's situation. The system does not produce solutions to problems, rather it aids the DM by suggesting applicable models of reasoning. By targeting this phase of the DM's actions, the orientation of advice to be included in the system became apparent. The representations in the system, e.g. file folders, desk, and pamphlets, are familiar to both expert and DM. Control is essentially in the hands of the DM. Guided and non-guided sessions can be dictated using the switch provided on the desk of the main menu. Memory aids are made available in: the scratch-pad for the DM to record insights, the dictionary to recall the definitions of terms or phrases, and the two types of traces permanently recorded for later use by the DM. To facilitate a dialogue between DM and expert, a “Remark” option is included in the system. The balance of selected representations is obvious. The DM seems to be at the electronic desk of an expert, free to peruse the contents of the expert’s file cabinet. The expert is preparing an office environment for system users. Further, the expert possesses an understanding of how the system can and will be used in terms of the representations, inferences and advice to be included in the system - both from a theoretical and object oriented viewpoint. Integration of multiple opinion is accomplished by directing the DM to actual sources for the advice offered by the system. In future systems, this could be accomplished by highlighting the disparities through system driven conclusions.

## 5. A Conceptual Framework for Design

This section generalizes the fundamentals into a framework for the development of future ES for strategic planners. Basic to this generalization is a view of an ES for strategic planners as a hybrid of a DSS. In essence, expert system technology has been adapted to support strategic decision making. This approach suggests that ES be used as a tool, rather than as a replacement for strategic planning personnel. Given this context, a framework for expert system development is best based on DSS design methods, however, the introduction of the expert as a major “player” in the development calls for a revision of current DSS design frameworks.

Figure 11 presents a modification to Figure 4. The three major loops remain, however, ES is substituted for System, and Knowledge Engineer for DSS Designer. An additional circle is introduced to represent the Expert. The two elements of the Cognitive Loop remain: the DM should learn by using the expert system, and expects a personalized interface. Similarly, the original Implementation and Evolution Loops remain.

![](/api/attachments/HQFKFZP7/fulltext/images/91a780a0f6e5afe7460dd4bfbed6ff83fb328b9ea67f4a8a9bdb231ae4091adc.jpg)  
Fig. 11. Expert System Design Criteria.

Two major differences are introduced to the model to represent the impact of including an expert into the adaptive design process. First, an additional cognitive loop between ES and Expert(s) is introduced. This reflects the need for validation of the evolving system, in terms of the necessity for guaranteeing that it produces the appropriate advice, consultation, and tutorial assistance for better decision making. Also, the communication between DM and expert is a necessary component to guide evolution of the ES, and to facilitate explanation of system conclusions. Second, an additional implementation loop is introduced between Knowledge Engineer and Expert(s). This loop reflects the selection of the appropriate expert(s), and the knowledge acquisition process, whereby the knowledge engineer builds an ES for the DM.

In this Figure, the rules-of-thumb numbers are presented on the arcs that they impact. Thus, on the user learning arc, rules 3, 7, and 10 apply. In terms of the personalized uses arc, rule 6 has the most impact.

The original implementation loop is most impacted by the facilitative implementation arc; this arc represents a view of the system as an evolving product, revised to reflect adjustments dictated by DM use of the prototype versions, but 4, 5, and 9 have impact on this.

Middle-out design suggests that the knowledge engineer be responsive to adaptations to the system suggested by the DM. Rules 1 and 2 impact this.

The evolutionary loop is impacted mainly by rule 8. Through this interaction, useful suggestions for evolution are likely to be determined. This rule also impacts the communication arc between Expert System and Expert(s).

The validation arc is most impacted by rule 9. This implies that the expert will be able to easily validate the system if familiar representations are used. Similarly, the knowledge acquisition arc between Expert(s) and Knowledge Engineer is aided by careful selection of representations.

The selection of the expert(s) arc is most impacted by rule 2. It suggests DM involvement in the selection of appropriate experts.

## 6. Summary

This paper has focused on an area only minimally addressed by current research: the process of knowledge engineering to develop ES for upper organizational levels. The DSS adaptive design process has been enhanced to introduce another major player: the strategic planning expert. The suggested design framework was based on an actual ES, and evolved from mistakes made in experience. While it will not be the last word on the process, it should contribute to better ES in the future.

The approach suggests that ES for strategic planners be viewed as a natural extension of a DSS. This implies that the Expert become a major player in the DSS design framework. However, more experience in developing such systems is necessary before better frameworks can be developed. This paper is limited because its conjectures are based on post-development reflections; future studies need to address the design framework during system construction, i.e., future ES construction should attempt to use a particular framework and offer advice on its limitations and benefits.

## References

[1] K. Azumi and J. Hage, Organizational Systems. (New York, NY: D.C. Heath and Company, 1972) pp. 264–281.

[2] J. Bennett, Building Decision Support Systems. (Menlo Park, Ca.: Addison-Wesley Publishing Company, 1983).

[3] W.R. Boulton, S.G. Franklin, W.M. Lindsay, and L.W. Rue, "How Are Companies Planning Now - A Survey." Long Range Planning. (Vol. 15, No. 1: February, 1982) pp. 82–96.

[4] H.J. Brightman, Problem Solving: A Logical and Creative Approach. (Atlanta, Georgia: College of Business Administration, Georgia State University, 1980).

[5] P. Connor, Organizations: Theory and Design. (Chicago, III.: Science Research Associates, Inc., 1980).

[6] G. Day, "Gaining Insights Through Strategy Analysis." The Journal of Business Strategy. Nov., 1981. pp. 51–58.

[7] V. Dahr, "On the Plausibility and Scope of Expert Systems in Management." Proceedings of the Nineteenth Annual Hawaii International Conference on Systems Sciences, 1986. Vol. 1, pp. 328–338.

[8] B.K. Dutta and W.R. King, “A Competitive Modeling Scenario System.” Management Science, 1980.

[9] L. Fahey and W.R. King, “Environmental Scanning in Corporate Planning.” Business Horizons, 1977.

[10] E.A. Feigenbaum and P. McCorduck, The Fifth Generation. (Reading, Mass.: Addison-Wesley, 1983).

[11] G.W. Gershefski, “Corporate Models - The State of the Art.” Management Sciences, 1970.

[12] M. Goul, The Inclusion of Expertise in a Decision Support System for Strategic Planning: An Empirical Study. Ph.D. Thesis. Oregon State University, 1985.

[13] M. Goul, B. Shane, and F. Tonge, “Use of an Expert Subsystem in Decision Recognition Channeling.” Proceedings of the Seventeenth Annual Hawaii International Conference on Systems Sciences, 1984. pp. 558–567.

[14] M. Goul, B. Shane, and F. Tonge, “The Design of an Expert Subsystem for a Decision Support System with an Application to Strategic Planning.” Proceedings of the Eighteenth Annual Hawaii International Conference on Systems Sciences, 1985. pp. 446–457.

[15] M. Goul, B. Shane, and F. Tonge, “Knowledge Based Decision Support Systems in Strategic Planning Decisions: An Empirical Study.” Journal of Management Information Systems, Vol. 2, No. 4, Spring 1986.

[16] P. Harmon and D. King, Expert Systems. (New York, NY: John Wiley and Sons, Inc., 1985).

[17] R.H. Hayes and R.L. Nolan, "What Kind of Corporate Modeling Functions the Best?" Harvard Business Review, 1974.

[18] P.G.W. Keen, “Decision Support Systems: A Research Perspective.” CISR Paper. (Cambridge, Mass. Sloan School of Management, MIT, 1980).

[19] W.R. King, “Achieving the Potential of Decision Support Systems: Strategic Planning Systems Design and Operation.” The Journal of Business Strategy, 1983. pp. 84–91.

[20] W.F. Pounds, “The Process of Problem Finding.” Industrial management Review. (11:1, 1969 - Fall) pp. 1–19.

[21] J.I. Rodriguez and W.R. King, “Competitive Information Systems.” Long Range Planning. Dec. 1977.
