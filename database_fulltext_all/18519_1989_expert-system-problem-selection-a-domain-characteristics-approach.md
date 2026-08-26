---
otero_id: 18519
otero_key: "SYDRQGDN"
title: "Expert system problem selection: A domain characteristics approach"
authors: "Hemant K. Jain; Alok R. Chaturvedi"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(89)90028-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Expert System Problem Selection: A Domain Characteristics Approach

Hemant K. Jain

School of Business Administration, University of Wisconsin-Milwaukee, Milwaukee, WI 53201, USA

Alok R. Chaturvedi

Krannert School of Management, Purdue University, West Lafayette, IN 47907, USA

The first generation of commercial expert systems based on AI technology are now available in the market place. But in the available literature, one can find hardly any material on expert system problem selection. In this paper a number of popular and successful expert systems are analyzed. Domain-dependent and domain-independent problem characteristics have been identified, based on the analysis. To test our contention that these characteristics significantly contribute to the success of expert systems, a questionnaire survey involving a number of expert system developers was conducted. Based on this, a domain characteristic approach for expert system problem selection is presented.

Keywords: Expert systems, Artificial intelligence, Knowledge-based systems.

![](/api/attachments/SYDRQGDN/fulltext/images/d32d7de23203ecc96ab89410fa94c70e14c88c08e84f18a92aecb8ab4a24af14.jpg)

Hemant K. Jain is a Research Associate Professor of MIS in the School of Business Administration at the University of Wisconsin-Milwaukee. He also held faculty positions at Syracuse University and at the National Institute of Training in Industrial Engineering, Bombay. His research interests are: distributed system design and computer networking, design of centralized and distributed databases, group decision support systems, model management systems, model integration, and knowledge integration in multi-expert knowledge based systems. He received his B.S. in Mechanical Engineering from the University of Indore (India), a M. Tech. in Industrial Engineering from I.I.T. Kharagpur (India), and a Ph.D. from Lehigh University, Bethlehem, PA. He is a member of IEEE Computer Society, TIMS, and DSI.

## 1. Introduction

There is little doubt that the Artificial Intelligence (AI) technology in the form of expert knowledge-based system is out of its infancy. The first generation of commercial systems are now available in the marketplace. According to the estimates of the Cambridge, Massachusetts based research consultants Arthur D. Little, the AI market will be more than \$4 Billion, or 4% of the entire computer market by 1990, up from \$55 million in 1981 or one-tenth percent in 1984.

An expert system (ES), or a knowledge-based system, employs human knowledge to solve a problem that ordinarily requires human intelligence [1]. Even though expert systems technology is considered to be in its developmental phase, in the last few years there has been an overwhelming increase of interest in designing and implementing expert systems covering a wide variety of domains – from board games, medical diagnoses, and computer configuration to strategic planning in industry, government, and military [2,3]. However, in the available literature, there is little on expert

![](/api/attachments/SYDRQGDN/fulltext/images/8e7c5217b05223c78dbc88fc3562a5053dd6697a3d071d7837f39f02128d4163.jpg)  
Alok R. Chaturvedi is an Assistant Professor of MIS in the Krannert Graduate School of Management at Purdue University. His research interests include: artificial intelligence applications in manufacturing, conceptual aggregation and machine learning applied to decision making, knowledge acquisition support systems, use of AI in representing and retrieving uncertain data in databases, and model management systems. He has a B.Sc. degree in Mechanical Engineering

from Birla Institute of Technology, Ranchi, India and M.S. and Ph.D. degrees in Management Information Systems from the University of Wisconsin-Milwaukee. He is a member of ACM, AAAI, and DSI.

system problem selection. Researchers have put emphasis mainly on knowledge representation and reasoning. Available methodologies and advice for expert system problem selection are usually simple but insufficient for applications of even moderate complexity [14]. Developers are also often misled by the claims made by the manufacturers of expert systems development tools and embark on overambitious ventures [4].

In this paper, a situation-action framework $[15]$ is used to define problem domains and their solutions. This framework is used to analyze a number of popular and successful expert systems. Based on this, a number of domain-dependent and domain-independent problem characteristics have been identified. To test our contention that these characteristics significantly contribute to the success of expert systems and to determine the current practices of problem selection, a questionnaire survey involving a number of expert system developers was conducted. Thus this paper attempts to provide:

(1) Help in analyzing the domain characteristics.

(2) A methodology for expert system problem selection.

## 2. Situation-Action Framework for Expert System Problem Representation

The problems addressed by expert systems can be divided into two broad categories: those that can be solved using an analysis approach or using a synthesis approach. The analysis approach starts with a complex problem and successively breaks it down into a number of subproblems until a stage is reached when each individual subproblem can be solved. Expert systems have been more successful in using this approach for handling analytical problems, such as classification, interpretation, evaluation, assessment, and diagnosis. Synthesis on the other hand, starts with solving the subproblems and combining the solutions to get a good (preferably an optimal) solution to the complex problem. As a result, synthesis needs to search through a large number of possible paths, and this leads to a combinatorial explosion [5]. Solutions for such problems are, therefore, necessarily heuristic. Examples of synthesis problems are design, program construction, etc. Expert system technology, so far, has had limited success in dealing with this type of problems: XCON/XSEL is one example.

![](/api/attachments/SYDRQGDN/fulltext/images/c16b4b05c6f33a4ec6bfb3e2700c4ac7954186a3d903509302731dac7956be14.jpg)  
Fig. 1. A Situation - Action Framework of Problem Representation.

## 2.1. Problem Representation Framework

In the framework presented here, a problem is represented in a situation-action (SA) sequence (Figure 1). It consists of

(a) A set of initial situations, a set or sets of intermediate situations, and a set or sets of final or goal situations.

(b) A set of actions to transfer the problem from the initial situations to one or more intermediate situations, and finally to the goal situations. A single set of actions may transfer a problem from the initial to final situations.

(c) A set of rules to specify how various situations can be achieved by using different actions. Thus a solution to the situation-action problem is a sequence of actions that leads from the initial situations to the final desired situations.

The problems addressed by six popular expert systems are now discussed. These are analyzed and represented in the situation-action framework to illustrate its power and generality (Figure 2). It also demonstrates the ability of this framework to structure complex problems.

MYCIN [6,7] is an expert system used for consultative advice on diagnosis and therapy for infectious diseases. MYCIN's problem in the SA model can be represented as follows: the symptom of bacterial infection can be considered as the initial situation. A set of actions are taken in terms of gathering more information on the infection through culture and test reports. This additional information strengthens or weakens the evidence of the presence of certain bacteria (intermediate situation) and suggests other tests to be performed (action). This process eventually leads to the final diagnosis and suggests medication (final situation).

![](/api/attachments/SYDRQGDN/fulltext/images/9b6ea29f8e97e45c7fe6988ac3e53cad29fa05f4ddec4cbf0412ab08fd3a614b.jpg)  
Fig. 2. S-A Representation of Some ES.

The PROSPECTOR [8] is a consultation system to assist geologists working on certain problems in “hard rock” mineral exploration. The initial situation in this case is the information provided by the user, e.g., the major rock type, minerals, and alteration products. The system develops a hypothesis (action) about ore deposits. The system may then request more information (action) depending on whether it can arrive at a conclusion or not (intermediate situation). With more information to the hypothesis may be strengthened or abandoned for a new one (intermediate situation). This continues until a situation is reached where a conclusion can be drawn about ore deposits (final situation).

XCON/XSEL [9] is an expert system used by Digital Equipment Corporation for configuring VAX computer systems. It utilizes a list of items from the customer order (initial situation), configures (action) them into a computer architecture (intermediate situation), notes any additions, deletions, or changes needed in the order (action) to make the system complete and functional (intermediate situation) and prints out a set of detailed diagrams showing the spatial relationships among the components (final situation).

The Palladian Financial Advisor [10] is a commercially available expert system. It is designed to assist corporate executives in planning, formulating, evaluating and monitoring capital intensive projects and products. The initial situation for the Financial Advisor is the knowledge of the corporate structure, financial assumptions, tax position, accounting policies, and coporate terminology. The inbuilt knowledge helps generate (action) different scenarios (intermediate situation). Financial analysis, such as Net Present Value, Internal Rate of Return, Return on Investments, Earning Per Share, etc. (actions) are used to generate alternatives (final situation).

Mudman [11] is an expert system that provides diagnostic and treatment recommendations to the engineer responsible for maintaining desired properties of oil well drilling fluids. The Mudman system is provided with mud properties: such as density, plastic viscosity, yield point, oil water ratio, etc. (initial situation). The system then compares the mud properties with a desired target value (action). If there is a deviation (intermediate situation), the system diagnoses the possible causes (action) and provides a recommendation (final situation). If the system comes up with more than one hypothesis (multiple final situations), then they are ranked by confidence level.

CATS-1 (Computer Aided Troubleshooting System - 1) [8] was developed by General Electric Co. to help maintenance personnel trouble-shoot GE's diesel-electric locomotives. The user starts by selecting a possible problem area (initial solution). The system then gathers more information by asking questions (action). Based on the responses, the system hypothesizes possible causes (intermediate situation) and asks further questions (actions). This is repeated until the fault is diagnosed (final situation).

## 2.2. Problem Characteristics

Problem representation of these systems in situation-action models helps in defining the common characteristics of their problem domains. Based on the above analysis, some common characteristics were identified:

Causality: the relationship between the situations and the phenomena. For example, which bacteria causes a particular disease, presence of what kind of rock explains the presence of a certain ore deposit, etc.

Temporality: the time precedence relationship (or sequencing) between situations; i.e., which situations precede a given situation and which situations follow it. For example, financial assumptions of a company must be known before different scenarios are developed. The customer's requirements must be known before the system can be configured.

Uncertainty: exists when reasoning by strict logical implications is not considered possible; this may be due to the inadequacies of the knowledgebase, insufficient data, inaccurate facts, or due to stochastic relationships between propositions. For example in MYCIN if symptoms A, B and C are present then the possible cause of the disease may be bacteria X. However, symptoms A, B, and C do not guarantee the presence of bacteria X. There are a number of schemes for representing this type of uncertainty, such as the certainty factor.

Fuzziness: problems addressed by expert systems are generally complex; thus they cannot always be clearly defined. Therefore, certain situations can only be defined relative to some other ones. For example, if we say “the economy will remain strong next year,” the strength of the economy is being expressed in relation to another situation (this year).

Structure: a property which allows complex problems to be broken down into a number of small subproblems with defined boundaries. This makes problems much easier to handle.

## 2.3. Evaluation of Problem Characteristics

An automotive brake troubleshooting problem is used to illustrate the evaluation of problem characteristics.

If an expert system for troubleshooting the brake system of an automobile is to be developed, the following steps are required in characteristics evaluation:

(1) List all the input (initial) and output (final/goal) situations. This will help in analyzing the problem. For example, a symptom (such as “the pedal goes all the way to the floor when braking”) is an input or an initial situation, and the suggested remedies (like “adjust brake shoes”) will be the output or final situation of the system.

(2) Represent the problem in Situation-Action framework, as discussed in section 2: by analyzing the problem identify the possible actions and intermediate situations required to achieve the final situation (goal). This will help in dividing the problem into subproblems which are relatively easier to solve. Figure 3 represents a part of the example problem in S-A framework.

Table 2  
Table 1  
Evaluation of Problem Characteristics.

<table><tr><td>Char.</td><td>Eval.</td><td>Explanation</td></tr><tr><td>Causality</td><td>H</td><td>high causal relationship between “pedal going to the floor” and a phenomenon such as “worn liner” or “low fluid”.</td></tr><tr><td>Temporality</td><td>M</td><td>it is desirable to “check the level of brake bluid or the brake liner” first and not “the master cyclinder” because the latter is more expensive and a less likely cause, although nothing stops us doing otherwise.</td></tr><tr><td>Uncertainty</td><td>L</td><td>there are only three possible causes and, of these, “low brake fluid” and “worn brake liners” are more likely than “faulty master cylinder.”</td></tr><tr><td>Fuzziness</td><td>L</td><td>the wear of the liner and the level of brake fluid can easily be measured and compared with the standard.</td></tr><tr><td>Structure</td><td>H</td><td>The problem can be easily subdivided into different modules, such as master cylinder, brake liner, and fluid level.</td></tr></table>

![](/api/attachments/SYDRQGDN/fulltext/images/7a575278d5b557a6ab9fcbb1d783643de047b8c2ba937662df4c53d108c19f5a.jpg)  
Fig. 3. An Example of SA Representation.

(3) Evaluate the problem based on the five characteristics. Rate the problem as high, medium or low on these characteristics. Table 1 presents the evaluation of the sample problem.

In a way similar to that in the illustrative problem, the characteristics of the six expert systems were evaluated. The result of the evaluation is summarized in Table 2.

## 3. Research Methodology

A lot has been written about a handful of successful expert systems but hardly anything can be discovered about those expert system ventures that have failed $[16]$ . Moreover, in the literature there is very little discussion about the factors which influenced the success or failure of a given system. It is our contention that the characteristics of problem domain addressed by the expert system plays a very important role in the success of the system. Obviously, there are other factors responsible for a system success, but the focus of this paper is on domain characteristics. Our research attempts to identify a few key characteristics of expert systems problem domains that might contribute to success. The outcome of this effort is the description of characteristics that are important during problem selection. To this end, a questionnaire survey approach was undertaken.

Summary of the Evaluation of Problem Characteristics.

<table><tr><td rowspan="2">Charact.</td><td colspan="6">Expert Systems</td></tr><tr><td>MYCIN</td><td>PROSPECTOR</td><td>XCON</td><td>Palladian</td><td>Mud</td><td>CATS-1</td></tr><tr><td>Causality</td><td>H</td><td>H</td><td>L</td><td>M</td><td>H</td><td>H</td></tr><tr><td>Temporality</td><td>H</td><td>H</td><td>L</td><td>H</td><td>H</td><td>H</td></tr><tr><td>Uncertainty</td><td>M</td><td>H</td><td>L</td><td>H</td><td>H</td><td>L</td></tr><tr><td>Fuzziness</td><td>H</td><td>H</td><td>L</td><td>H</td><td>L</td><td>L</td></tr><tr><td>Structure</td><td>L</td><td>L</td><td>H</td><td>M</td><td>M</td><td>H</td></tr></table>

$\mathrm{H} = \mathrm{High}$  
$\mathbf{M} = \mathbf{M}$ cdium  
$\mathbf{L} = \mathbf{L}\mathbf{ow}$

The questionnaire was sent to 92 organizations nationwide. The population consisted of corporations, research laboratories, and universities. The expert system developers were asked the following:

(1) Problem domains addressed by their systems.

(2) Degree of structure, uncertainty, and fuzziness of the problem domain.

(3) How and why was an expert system solution chosen for their problem?

(4) Type of functions served by expert system, such as decision maker, advisor, or colleague.

(5) Parameters used to judge the success of the system.

(6) Problem characteristics that contributed to the success of the system.

(7) The extent to which validation of the system was considered at the time of problem selection.

The cognitive process involved in problem selection is not a formalizable phenomenon. Therefore, it is often difficult to interpret response data reliably so that generalized patterns emerge. The simple questionnaire, however, did help to overcome this difficulty.

## 4. Findings

The response to our questionnaire was quite encouraging, especially from the commercial organizations. In all, 28 responses were received; however, ten either did not have experience in developing expert system or felt that the information requested was classified. Because of the small sample size, no statistical analyses were performed. However, the information provided by the respondents and their experiences in developing expert systems were very valuable. Based on the responses, some interesting observations can be made, as follows.

## 4.1. Problem Domain and Characteristics

The expert systems developed by the respondents can be broadly classified into seven categories. For each category, the responses on problem characteristics (on a scale of 1 to 5) were averaged and mapped into High, Medium, and Low. Results are given in Table 3.

Diagnosis and Troubleshooting. The general diagnosis and troubleshooting problem is one of classifying an unknown object, event, or situation into some known classes on the basis of uncertain information about its characteristics. The knowledge-based systems approach to such problems effectively substitutes the knowledge and judgment of human experts for this function. These problems are highly structured and highly dependent on causal and temporal relationships, but are low on fuzziness and uncertainty.

Analysis and Data Interpretation. The systems can analyze large amount of sensed data in the form of a graph (electrocardiograms), electrical, or acoustical signals. The interpretive expert system helps the user to extract the signal from the noise such as that from underground geological structures. Such problems have high causality, uncertainty, and fuzziness, medium temporality, and low structure.

Control and Alarm Handling. In process control, the AI program is used to model, track and predict process and raw material behaviors. AI systems for equipment monitoring, factory monitoring, and alarm handling fall in this category. These problems are rated high on structure and causality, medium on temporality and fuzziness, and low on uncertainty.

Problem Characteristics of Different Functional Areas.

<table><tr><td rowspan="2">Charact.</td><td colspan="7">Expert Systems&#x27; Categories</td></tr><tr><td>Diag.</td><td>Anal.</td><td>Ctrl.</td><td>Dsgn.</td><td>Plg.</td><td>Asst.</td><td>I&#x27;face</td></tr><tr><td>Structure</td><td>H</td><td>L</td><td>H</td><td>H</td><td>L</td><td>H</td><td>H</td></tr><tr><td>Causality</td><td>H</td><td>H</td><td>II</td><td>L</td><td>L</td><td>H</td><td>H</td></tr><tr><td>Temporality</td><td>H</td><td>M</td><td>M</td><td>L</td><td>H</td><td>H</td><td>L</td></tr><tr><td>Uncertainty</td><td>L</td><td>H</td><td>L</td><td>L</td><td>H</td><td>L</td><td>M</td></tr><tr><td>Fuzziness</td><td>L</td><td>H</td><td>M</td><td>L</td><td>H</td><td>L</td><td>M</td></tr></table>

Design Systems. Such systems help in the design process and check the designs of other people for potential problems. This is particularly useful in the case of large systems design, where it is difficult to evaluate the effect of change in a part of the design. The problems are highly structured, but have low causality, temporality, uncertainty, and fuzziness.

Planning. There are two categories of planning systems. The first plan operations on a small scale, such as the sequence of actions for a robot or a sequence of procedures to manufacture a product. The other category operates on a macro level, such as sequencing operations and scheduling resources. Such problems have high temporality, uncertainty, and fuzziness; and low causality and structure.

Assistant / Advisor. Some systems assist or advise users about their domain problems. Some even have the capability of taking charge in the absence of a user. Such systems have high causality, temporality, and structure, and low uncertainty and fuzziness.

Intelligent Interfaces. AI-based user interfaces, especially natural language, insulate users from complex and hard-to-use hardware or software. These systems are high on causality and structure, medium on uncertainty and fuzziness, and low on temporality.

Of the expert systems developed by the respondents, 75% addressed diagnostic problems. The remaining 25% covered the other categories. About 70% performed as an advisor for human operators/users, about 15% could perform as subordinate and advisor, and the remaining 15% as decision maker, advisor and subordinate.

Table 4 summarizes the domain characteristics of the problems addressed by the survey expert systems.

Reviewing the responses, one can see that the majority of systems had following characteristics:

<table><tr><td>Structure</td><td>H/M</td></tr><tr><td>Uncertainty</td><td>M/L</td></tr><tr><td>Fuzziness</td><td>M/L</td></tr><tr><td>Causality</td><td>H/M</td></tr><tr><td>Temporality</td><td>H/M</td></tr></table>

Table 4  
Summary of Problem Characteristics Response.

<table><tr><td rowspan="2"></td><td colspan="5">Characteristics</td></tr><tr><td>Structure</td><td>Uncertain</td><td>Fuzzy</td><td>Causal</td><td>Temporal</td></tr><tr><td>High</td><td>57%</td><td>15%</td><td>15%</td><td>63%</td><td>40%</td></tr><tr><td>Medium</td><td>28%</td><td>43%</td><td>28%</td><td>22%</td><td>35%</td></tr><tr><td>Low</td><td>15%</td><td>42%</td><td>57%</td><td>15%</td><td>25%</td></tr></table>

Table 5  
Characteristics Contributing to the Success of the System as Ranked by the Respondents.

<table><tr><td>Characteristics</td><td>Rank</td></tr><tr><td>Structure</td><td>1</td></tr><tr><td>Causality</td><td>2</td></tr><tr><td>Temporality</td><td>3</td></tr><tr><td>Fuzziness</td><td>4</td></tr><tr><td>Uncertainty</td><td>5</td></tr></table>

## 4.2. Characteristics Contributing to the Success

All the respondents considered their system to be either extremely successful or very successful. They used surrogates, such as customer satisfaction, problem solving ability, and cost benefit analysis to measure the success of their system.

Table 5 shows the characteristics of the problem domain which contributed to the success of the system as ranked by the respondents (1 = most):

The other characteristics which contributed to the success of the system were ranked by the respondents as in Table 6 (1 = most).

## 4.3. Reasons for Selecting Expert System Solution

All the developers felt that an expert system was the only solution to the problem. About 87% of the respondents felt that the availability of knowledge engineers and domain experts were critical in selecting an expert system solution. The reasons for choosing an expert system solution to the problem were ranked as shown in Table 7.

Table 6  
Other Characteristics Contributing to the Success.

<table><tr><td>Characteristics</td><td>Rank</td></tr><tr><td>Results could easily be verified</td><td>1</td></tr><tr><td>Problem was well defined</td><td>2</td></tr><tr><td>No binary decision required</td><td>3</td></tr></table>

Reasons for Selecting Expert System Solution to the Problem as Ranked by Respondents.

<table><tr><td>Reasons</td><td>Rank</td></tr><tr><td>Problem suitable for expert system application</td><td>1</td></tr><tr><td>Genuine expert available</td><td>2</td></tr><tr><td>Wanted to experiment</td><td>3</td></tr><tr><td>Problem not too complex</td><td>4</td></tr></table>

4.4. Validation Issues at the Time of Problem Selection

For about 50% of the systems, validation was not considered critical during problem selection.

## 4.5. Difficulties Encountered

Undertaking the task of selecting a problem for building an expert system is not without difficulties. These were numerous – some unique for their domain and others domain independent. The difficulties encountered by the respondents included the following.

Defining the problem, parameters, and scope is the area of biggest concern for most of the developers. When a human expert solves a problem, he/she defines its discrete boundaries. For a computer program, the problem and parameters must be clearly defined and the scope should be fully specified. The Situation-Action framework can help in defining such boundaries and the scope.

Assistance from an expert or group of experts. A number of respondents found it difficult to find a domain expert, while others found that experts were usually constrained by time and were not readily available for interviews. Some respondents found that consistency in experts' cognitive process was lacking. This was due to their inability to articulate their cognitive processes. This problem was compounded when dealing with a group.

Integration with other systems. Most respondents felt that the usefulness of an expert system can only be fully realized if it can be integrated with other systems. Integration was a problem when there were multiple knowledge sources. Some felt this to be a critical design issue that must be addressed at the beginning of the project.

Deficiency of developmental tools. A number of respondents felt that the developmental tools lacked expressive power, adequate consistency checking mechanism, and delivery vehicles.

Inadequacy of knowledge engineering environment. Some respondents felt that the AI group in their organizations is relatively new. As a result, the knowledge engineering environment is lacking.

End-user support and acceptance. In some cases, due to the lack of understanding of AI technology, the end-user support and acceptance is difficult to achieve.

## 5. Problem Selection Guidelines

Based on the analyses and responses, the following problem selection guidelines have been developed (Figure 4):

(1) Identify a candidate expert system problem.

(2) Represent the problem in Situation-Action framework.

If a problem cannot be represented in the framework, then:

(a) the problem may be too complex to be solved by an expert system approach,

(b) the problem may not be sufficiently understood to provide the clear definition required by an expert system approach, and

(c) the problem may lack structure; this will make expert system development difficult.

![](/api/attachments/SYDRQGDN/fulltext/images/f73b4b5d92eefd86077ed24ddf415f363ffffa659f636e1f2e8eb12b46c179ae.jpg)  
Fig. 4. Domain Characteristic Approach to Expert System Problem Selection.

(3) Evaluate the problem based on the five characteristics. Rate the problem as medium, high, or low on these characteristics. This will prove to be useful in selecting the right tools and techniques during development.

(4) Using the S-A framework, define the subproblems.

(5) Based on the evaluation of the characteristics, the problem can be classified as one of analysis or synthesis. If the evaluation shows low to medium causality, temporality, and uncertainty, the problem can generally be classified as one of synthesis. Medium to high evaluation of these characteristics will mean that the problem is one of analysis.

Synthesis problems are generally hard to solve, due to combinatorial explosion. If the number of possibilities are small, then an optimal solution can be found, otherwise special heuristics are required. The development of an efficient expert system for such problems may require parallel processing machines $[13]$ . Analysis problems, however, are relatively easy and expert systems for such problems can be developed on traditional machines.

(6) If the candidate problem passes all of the tests, then check for availability of resources, such as domain expert, knowledge engineer, and development tools: they are critical to the success of the system. Waterman [12] discusses these aspects in detail.

(7) Finally, schemes for validating the results of the system should be considered before development starts.

## 6. Conclusion

This paper presents a situation-action framework for expert system problem selection. The framework allows one to represent a problem in terms of situation and action. This helps in defining and partitioning the problem into a number of subproblems. Five key problem characteristics are identified. The survey of expert system developers indicate that these characteristics significantly contribute to the success of the system. A candidate problem can be evaluated based on these characteristics. The results of evaluation indicate whether the problem is of analysis or of synthesis. Finally, guidelines for the expert system problem selection are presented.

It must be noted, however, that this study was aimed to be an initial exploration of the relationship between an expert system's domain characteristics and its perceived success rather than an experimental test of a plausible framework. Although the study presented in this paper in based on subjective questionnaire categories and with limited empirical analysis, it definitely suggests that such a relationship exists, and marks a step forward in our ability to use expert systems technology sensibly.

## References

[1] Hayes-Roth, F. et al., Building Expert systems, Addison Wesley Publishing Co., 1983.

[2] Blanning, R., “Expert Systems for Management: Possible Application Areas”, DSS-84 Tran., ed. Robert W. Zmud, pp. 69–77, 1984.

[3] Goul, M. et al., “The design of an Expert Subsystem for a Decision Support System with an Application to Strategic Planning”, Proceedings of an Eighteenth Annual Hawaii International Conf. on System Science, 1985.

[4] Martins, G.R., “The overselling of Expert Systems”, Datamation, Nov. 1984.

[5] Haugland, J., Artificial Intelligence: The very idea, MIT press, 1985.

[6] Barr, A., Cohen, P.R., Feigenbaum, E.F., The Handbook of Artificial Intelligence, Kaufman, Los Altos, Calif., 3 vols., 1981, 1982.

[7] Buchanan, B.G., Shortliffe, E.H., Rule-based Expert Systems, Addison-Wesley Publishing Co., 1985.

[8] Harmon, P., King, D., Expert Systems: Artificial Intelligence in Business, John Wiley & Sons, Inc., 1985.

[9] Scown, S.J., The Artificial Intelligence Experience. An Introduction, Digital Equipment Corporation, 1985.

[10] Literature provided by Palladian Software, Inc., Cambridge, Mass.

[11] Kahn, G., McDermott, J. "The Mud System", IEEE Expert, Vol. 1, No. 1, 1986.

[12] Waterman, D. Guide to Expert Systems, Addison-Wesley Publishing Co., 1986.

[13] Feigenbaum, E., McCorduck, P., The Fifth Generation, Addison Wesley, 1983.

[14] Kline, P., Dolins, B., Choosing Architectures for Expert Systems, CCSC Tech. Report#85-01-001, Texas Instruments, Inc. 1985.

[15] Jain, H.K., Chaturvedi, A.R., “Situation-Action Framework for Expert System Problem Selection,” Proc. of the annual IBSCUG North American Conference, Flint, Michigan, 1987.

[16] Stone, J., “Commercial Trends Seen at AAAI-87,” AI Magazine, vol. 8, no. 4, Winter 1987.
