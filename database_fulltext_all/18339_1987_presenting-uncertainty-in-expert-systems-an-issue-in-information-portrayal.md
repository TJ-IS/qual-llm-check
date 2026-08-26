---
otero_id: 18339
otero_key: "AK2F38AG"
title: "Presenting uncertainty in expert systems: An issue in information portrayal"
authors: "Donna Lamberti; William A. Wallace"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90053-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Presenting Uncertainty in Expert Systems: An Issue in Information Portrayal $^{1}$

Donna Lamberti $^{2}$ and William A. Wallace $^{2}$ Decision Sciences and Engineering Systems, Rensselaer Polytechnic Institute, Troy, NY 12180, USA

The issue of portrayal of uncertain information for use in expert system decision aids is addressed in this paper. Emphasis is placed on the clarity and comprehensibility of information displayed to decision makers in an uncertain environment. The influence of cognitive style in the processing of information is discussed, and alternative information portrayal techniques are presented for displaying uncertain information to command and control analysts in a military setting. Recommendations are made for empirical testing to assess the effectiveness of the various information portrayal techniques.

Keywords: Information portrayal, expert systems, decision support systems, cognitive style, decision making, intelligent interfaces, probabilistic information.

## 1. Introduction

Historically, most of the effort in developing expert systems (ES) was devoted to defining artifi-

![](/api/attachments/AK2F38AG/fulltext/images/1453ae030ceaec8b9968035382fd93c0b858b5b8b785796d23230eacd176be65.jpg)

Donna M. Lamberti received a B.A. degree in Experimental Psychology from Vassar College, Poughkeepsie, NY in 1982, and a M.S. degree in Cognitive Psychology/Human Factors, as well as a Ph.D. in Information Systems/Decision Sciences from Rensselaer Polytechnic Institute, Troy, NY in 1987. Her dissertation research was the development of an intelligent interface for a diagnostic expert system application. This work was sponsored by an IBM Fellowship for research in information systems.

She is currently a research staff member at the IBM Cambridge Scientific Center, Cambridge, MA. Her research interests include intelligent interface design for decision support technology, AI-based advisory systems for organizations, and the implementation of decision support/knowledge-based systems.

![](/api/attachments/AK2F38AG/fulltext/images/8b4a9f5a5de24c8e6cc8dbc021fd3f4c7990448060be7f807fac6f6ee74ce3f8.jpg)

William A. Wallace is Professor and Acting Chairman, Decision Sciences and Engineering Systems at Rensselaer Polytechnic Institute. As a researcher and a consultant in Management Science and Information Systems, Professor Wallace has over 15 years experience in developing, implementing, and evaluating decision support systems for industry and government. He is presently engaged in research and development on computer-based decision aids utilizing expert system technology. Professor Wallace has authored and co-authored 4 books and over 90 articles and papers. He has held academic positions at Carnegie-Mellon University and State University of New York at Albany, was a research scientist at the International Institute of Environment and Society, Science Center, West Berlin, Germany and a project engineer at Illinois Institute of Technology Research Institute, and is a Navy veteran. He was selected as a Visiting U.S. Faculty, Management Information Systems/Decision Support Systems, National Center for Industrial Science and Technology Management Development, Dalian, People's Republic of China, and implemented the first microcomputer based educational facility in the country. His research has been reported on by national and international media including Associated Press, Christian Science Monitor and Business Week. His educational background includes a B.Ch.E. from Illinois Institute of Technology and a Master of Science and Doctorate in Management Science from Rensselaer Polytechnic Institute.

cial intelligence (AI) rules and algorithms. This emphasis resulted in insufficient attention being paid to the usability, clarity, and comprehensibility of the information being displayed in ES technology. Consequently, invalid interpretation of the outputs was likely to occur, thereby compromising the decisions aided by these “tools”. The role of an expert system is to aid in the processing of information and the selection of a course of action; our objective is to find clearer portrayal methods for the information needed in decision making under uncertainty.

One of the most critical components of an ES is the interface between the system and its users. For users, this interface is the only part of the system that is meaningful: the rest is invisible. As the number of users of ES's continue to increase, their potential in aiding decision making cannot be realized until they are easier to understand. The interface must be designed to support unstructured and semi-structured decisions based on uncertain information. As Sprague [37] states, "much of the power, flexibility, and usability characteristics of a decision aid is derived from capabilities in the user interface". Currently, research examining expert systems' user interfaces is scarce. More effort needs to be placed on developing user interfaces that exploit the potential of expert systems to enhance the decision-making process.

The quality of information inputs into the decision process depends on at least four elements: relevance, timeliness, presentation, and distribution [26]. Relevance refers to the degree of completeness of required information for decision making, whereas timeliness generally refers to the age of the information (with impact on decision making). Distribution refers to the need to present the data to the right person at the right time – in the appropriate format.

Information presentation needs to address the question, “To what degree can the information be understood and used by decision maker?” The specific configuration of the output can impact the ability of the decision maker to acquire and understand concomitant information in limited time [31].

An operational environment with high stress and short response time, coupled with high volumes of data (often equivocal or erroneous), establishes the need for “tools” to help decision makers assess situations, generate options, and select alternatives. The specific format of knowledge output to system users is thus an important factor, particularly when numerous sources of knowledge are involved. To achieve these aims, presentation formats should provide tools for generating symbols, integrating graphic and textual messages, and adapting message formats to suit different decision situations.

In an effort to assess this situation, the U.S. Air Force, through the Rome Air Development Center (RADC), initiated a research program to investigate the use of artificial intelligence (AI) and operations research techniques to provide decision support for Air Force analysts and decision makers. This research program provided the context for our work.

## 2. Role of Cognitive Style

Even though the research findings on information portrayal (IP) techniques have been mixed [13], there have been significant findings on the advantages of graphic presentation over tabular format. These seem to be due to differences in both (1) the ways the human brain processes tabular and graphic data, and (2) the cognitive style of the user.

Two conceptual bases for human information processing, the “spatial analogy” and the “split brain” models, are relevant $[7,19,43]$ . The concept of “spatial analogy” is based on the capacity of the human mind to associate particular items of information with fixed locations in space. By addressing this tendency of the mind, the designer of a computer graphics system can enhance the mind’s natural capabilities.

In the “split brain” model, visual images, unlike analytical functions, seem to be processed simultaneously by both hemispheres of the brain, with many separate brain circuits active in processing different parts of the visual image. The result of this seems to be the formation of the “Gestalt”, a cognition which is supposedly “greater than the sum of its parts”. This “parallel processing” cognitive mode seems to make much more use of the inherent data processing capacity of both audition and vision. Consequently, humans can assimilate more data graphically than by reading words or tables.

Cognitive style can be viewed as a set of consistent and differentiated strategies that largely evolve in response to specialized information-processing and educational environments $[20,21,25]$ . In reviewing the many theories of cognitive style $[9,23,38]$ , two aspects appear to be especially relevant to the investigation of effective information portrayal techniques in expert systems. These are field independence-dependence, and systematic-heuristic decision styles.

The first classifies users as perceiving data as either: (1) patterns of data that are relatively independent of their context (high-analytic), or (2) discrete items embedded in their context (low-analytic). The second classifies users as: (1) systematic, searching the data for causal relationships that promote an algorithmic solution, or (2) heuristic, searching by trial-and-error ad hoc hypothesis testing.

While the cognitive style of users has received much more attention, the field is divided about its importance in design. Some researchers $[28,45]$ see a continuing need for attention to cognitive style. As noted by Robey $[29]$ , the increasing flexibility and capability of decision aids required both an examination of whether there is a “fit” between the user’s cognitive style and the characteristics of the decision aid and also the nature of the fit; e.g. does the expert system assist the user’s preferred style or complement the user’s basic style.

In contrast to those cited above, other researchers, such as Chervany and Dickson [14] and Huber [18], suggest increased research focus on situational and task variables, citing the small part of the variance in research results that can be explained by user personality variables. They note the lack of a unified body of theory of cognitive styles, partly because of the multiplicity of cognitive style measuring instruments.

Nevertheless, as Keen and Bronsema [21] point out, studies of cognitive style reflect two central assumptions: (1) systematic differences exist among individuals in terms of their perception, thinking, and judgement [29], and these differences influence choice of and response to information; and (2) the difference between managers' and analysts' cognitive styles is a major explanation of difficulties in system implementation.

These suggest the need for additional investigation of the role that cognitive style should play in IP design. A critique of previous studies by Taylor and Benbasat [38] identifies the high potential payoff from “sound research into the psychological characteristics of information system users”. It is our view that expert systems and their concomitant information portrayal techniques should be designed to be robust with respect to cognitive style.

## 3. Alternative Information Portrayal Techniques

The interaction between the user and the expert system is a critical issue for successful decision support. Consequently, research is needed in portraying complex information on visual displays. Emphasis on techniques to enhance human information assimilation (to maximize understanding of meaning) is important.

Certainly, in any operational environment there is a need for methods of information portrayal (IP) that present relevant information in the clearest, most precise manner possible. In this sense the purpose of the expert system as a decision aid is to help reduce the user's information processing load, while structuring the problem so that the user can make a decision.

In discussing the alternative IP techniques, we will refer to the expert system, DART, designed to provide decision support for an analyst in a military command and control situation: identifying critical targets in a near real-time environment. As previously noted, due to the tremendous volume of intelligence data, the identification and classification task is extremely difficult. Little or no message analysis and correlation are conducted and experience is an important factor in the identification effort. The DART aid will assist in message identification and classification.

DART uses a rule-based expert system to identify air defense positions, radio relay sites, and command/control nodes. Based on a selected goal, the expert system will access the rule network to analyze the available information. The system advises the user of the degree of belief in the chosen goal, based on the evidence.

Degree of belief calculations originate with the experts, who are polled for an ordinal ranking of rules. Together with the expert opinion and their own judgement, programmers convert this ranking into probability $(p)$ . This is converted to degree of belief $(db)$ by:

$$
d b = \log \left(\frac {p}{1 - p}\right) \times 1 0
$$

which makes the combinational operator addition. This initial degree of belief (prior db) exists on a scale of -100 to +100 and is propagated through the analysis using four types of rules. Three of the rule types employ standard boolean operators to test and modify degree of belief (and, or, not), while the fourth, called a baysian rule, is of an additive if-then form: "if a, then b with positive weight p and negative weight q." Propagation of degree of belief follows the form:

$$
\text { if   } a \text {   then   } d b (b) = d b (b) + p
$$

else db(b) = db(b) + q.

Degree of belief is propagated throughout the network until a determination concerning the goal is made. At this time, the user is given the final degree of belief in the analysis, again on a -100 to +100 scale, with +100 indicating certainly yes, -100 indicating certainly no, and 0 meaning a 50–50 chance.

DART focuses on enhancing information processing and thereby expanding the knowledge of the analysts with respect to incoming data and providing expert recommendations. Unclear information portrayal has significant implications; situations must be assessed, alternatives constructed and selected, and orders issued, often in a time frame of a few minutes. Without clear interpretation of the information presented by the decision aids, the quality of decisions will suffer.

Despite the fact that the DART aid was originally designed using alphanumeric coding on a black and white display, the methods of IP on the state of an uncertain environment were not effective. The DART aid was supposedly designed under general guidelines concerning IP using alphanumeric. However, when empirically tested, command and control analysts had difficulty, in terms of accuracy and speed, in identifying and classifying information on the display. These difficulties, consequently, hindered the analysts' ability to make fast, accurate decisions. It appears that the alphanumeric display format chosen was inappropriate to present information in a clear and unambiguous manner.

In attempting to develop alternative information portrayal formats, it was necessary to evaluate previous research examining alternative portrayal methods $[27,39,46]$ . After reviewing this body of literature, it was crucial to ask the question: Why were there problems with understanding the information presented on the DART display? Several difficulties were reported by the analysts. They were unable to understand the screen display: specifically the meaning of the probability numbers and their use in interpretation of the severity of the situation. This led to confusion and reduced analysts response speed. Guidelines specifying information presentation factors such as character size, format, density, amount, alphanumeric vs. symbolic displays, chunking and sequencing of information, color coding, highlighting, contrasting, and redundancy play a very important role in designing displays that enable operators to perform their tasks effectively and efficiently. However, after studying the material, it becomes apparent that the guidelines need to be applied with caution. It should not be assumed that a display designed according to these guidelines will always be effective in terms of user comprehension and task performance.

Emerging doctrine and advancing technology call for the development of improved information symbology, and considerable effort is being directed toward this goal $[8,35,40]$ . At the same time, innovation in computer graphic hardware and software has provided for cost-effective application of creative symbol-design features such as icons, color, vector projection, and graphic images. But the impact of various portrayal methods on decision making will depend largely on the extent to which the symbology can be perceived and interpreted by the user $[6]$ .

Although researchers acknowledge that mode of presentation may alter information use $[1,14,18,22,23,30]$ there is relatively little research which addresses the impact of form.

Historically, expert systems have employed numerical techniques to assess subjective degrees of belief in uncertain alternatives. In this approach, alternatives are easily ranked by their degrees of belief, and they are easily calculated by simple arithmetic rules [11].

However, the problem of IP is particularly acute when attempting to provide “measures of goodness” or “degree of certainty” associated with recommendations from expert systems. Objective degrees of belief generally do not behave as probabilities [42], so we must consider what interpretation to give to them, and whether probabilistic combining methods are valid.

General findings suggest that nonnumerically presented information weighs more heavily than numerically presented information after the content differences between the two message forms are eliminated [4]. Nonnumeric information may be more uncertainty absorbing than numeric information. It may absorb uncertainty by providing information that was preprocessed (evaluated) by the designers of decision aids and placed in a frame of reference for the user [4]. It is our contention that presenting numerics only will lead to confusion, and possible misunderstanding, with consequently ineffective use of the expert system. The numbers alone may be ambiguous – composed of salience and probability considerations.

Decision makers are required to perceive, process, and evaluate the probabilities of uncertain events. There is evidence of decision makers possessing serious biasing heuristics for probability estimation [44]. Rather than just accepting that humans are poor estimators of probability, information processing limitations should be understood. We propose that expert systems' interfaces should be designed to minimize the ambiguity associated probabilistic information, so that the user does not have to make judgements based only on the presentation of probability factors. Consequently, focus was placed on IP techniques [34] that aid in summarization and reporting complex information to minimize ambiguity.

Specifically, IP guidelines must be considered in conjunction with the type, value, and purpose of the information. For example, the information portrayed by the DART system represents an uncertain, risky environment requiring high levels of user confidence to make effective and timely decisions.

The alternative presentation techniques that we proposed for the DART system constituted the initial phase in redesigning the aid. Subsequent phases need to include empirical evaluation to determine the adequacy of the design.

Four different types of information portrayal are proposed. These consist of color, symbols, graphics, and numeric displays, as well as various combinations of such techniques. These combinations are demonstrated for four actual screens that are displayed while using DART.

The purpose is to determine whether an optimal means of encoding information could be derived from several encoding dimensions without varying the quantitative informational content from one dimension to the next. Therefore, this project concerned itself primarily with qualitative variations in the visual presentation of information, while holding the quantity of information displayed constant. The exhibits on the following pages show examples of displays with alternative presentations.

The use of symbols was chosen in an effort to reduce information overload and ambiguous data. The goal for the interface of the expert system was to minimize the debilitating impact of high volume information, resulting in omission, delay of response, filtering, and processing incorrect information. Thus, one of the primary factors which led us to the symbolic encoding of information was not only the vast quantity and complexity of the data, but the tendency and desirability for displaying a complex situation as completely as possible on a single display.

The effects of color coding have been studied by Christ [10], who found that the effectiveness of color depends upon experimental conditions, with search and identification tasks generally being enhanced by color.

It also seems that color improves task performance when used as partially redundant code for categories of information, e.g. where a category label, Degree of Belief, or symbol accompanies a specific category color. The analyst uses color to structure a more efficient search pattern. We conjecture that effective color coding enhances the analyst's ability to remember information, particularly where it is used to communicate relationships and dependencies (such as red to indicate a high level of certainty). Salomon [33] refers to this use as a "supplanting function". The color cue supplants a covert mental operation that the analyst would otherwise have had to activate. Also, users appear to view color as being pleasing or stimulating, perhaps indicating that it could have a positive effect on user acceptance of the system.

The first IP method uses symbols to represent uncertainty, such as the “measures of goodness”. In suggesting these alternatives, the basic screen design was not altered. On the right hand side there is a menu of options allowing the user to take action or gain additional information about the environment. In addition, standard command and control data, e.g. radar, latitude and longitude information, is presented along with the number of current messages awaiting a response from the

## Find a Message C3 Node

NODE: UICP
LATITUDE: 50 58 19 n
LONGITUDE: 10 0 46 e
DAY: 6

CELL NB
NORTHING: 472
EASTING: 711
TIME: 1616

CERTAINTY:

![](/api/attachments/AK2F38AG/fulltext/images/6e678d3d2d9ac51e7e7e54ab12acc3a74a782c19c299411ba87814176dface63.jpg)

Choose from:
1. Auto-Create a C3 Node
2. Create a C3 Network Node
3. Delete a C3 Network Node
4. Auto-Update a C3 Node
5. Update a C3 Network Node
6. Find the Message C3 Node
7. List C3 Network Nodes
8. Quit

Hit Return to Continue
Current Message
MSGID/TACREP /DSU/128/8304061628Z//
WHAT/UICP/061616Z//
WHERE/505814N/095801E/NB679470/1120/0425/000//

Fig. 1.

user. A message arises any time there is a potentially threatening change in the environment such as the appearance of enemy aircraft. The only change from the original screen was the addition of graphical displays that present the information on degree of belief or certainty.

A standard military symbol was chosen as an example. Both solid and iconic versions of the symbol are shown. Each version has a particular color associated with it, denoting level of certainty. In accordance with research findings [10], the colors range from red, which is DEFINITE, yellow-PROBABLE, green-POSSIBLE, to blue which stands for UNCERTAIN. In using color coding of information, emphasis is plaed on consistency and a limited number of different colors, since irrelevant colors can interfere with the ability to perform decision-making.

In the iconic symbols, several options exist for depicting the level of certainty. For example, the actual word can appear inside the symbol (see Fig. 1). Similar examples are shown in Figs. 2 and 3, portraying alternative hypotheses listed by DART. The symbols shown should represent whatever types of “aircraft” are stated in the hypotheses.

More than one symbol could be shown on the screen at the same time with the colors and confidence weights representing the certainty and degree of belief. Since the same military symbols are used across range of display configurations and tactical tasks, the deviation of generalized symbols is necessary.

In addition, graphic charts are used to depict certainty, degree of belief, and weight measures in DART. The screen shown in Fig. 4 is presented when the user chooses the menu option to explain DART's advice. Three basic types are possible: first is a line vector, in which each segment of the vector is associated with one of the four colors. Two versions depict the certainty measure; with the label words next to each segment, and with only the colors of the line segments.

In addition, for degree-of-belief, a normal distribution graph is also proposed, where each section of the curve can be represented in color. The number given for degree of belief can be shown on the curve (see Fig. 5). Also, a simple line segment broken into four categories can show the degree of belief in equivalent color. The label word associated with that particular category may or may not

## Find a Message C3 Node

: H H H H H H H H H H H H H H H H H H H H H H H H H

Choose from:

NODE:

CELL NB

1. Auto-Create a C3 Node

LATITUDE: 50 58 19 n

NORTHING: 472

2. Create a C3 Network Node

LONGITUDE: 10 0 46 e

EASTING: 711

TIME: 1616

3. Delete a C3 Network Node

4. Auto-Update a C3 Node

5. Update a C3 Network Node

## CERTAINTY:

6. Find the Message C3 Node

![](/api/attachments/AK2F38AG/fulltext/images/42e7c36b3650fac53cac00d44315438ac0901e0b96848f67b308d3ca01724ae1.jpg)

7. List C3 Network Nodes

8. Quit

Hit Return to Continue

Current Message
MSGID/TACREP /DSU/128/8304061628Z//
WHAT/UICP/061616Z//
WHERE/505814N/095801E/NB679470/1120/0425/000//

Fig. 2.

## Other Hypotheses:

: H H H H H H H H H H H H H H H H H H H H H

the message refers to:

Choose from:

1. Explain Advice

2. Print Other Hypotheses

![](/api/attachments/AK2F38AG/fulltext/images/5a2db554c2e57b566b2fd533a810bf04cf1d0e1254172855074b98945b375556.jpg)

3. Enter KE Mode

4. Quit

10 Messages Waiting

![](/api/attachments/AK2F38AG/fulltext/images/62df9f0846398039bc61f587b1255c7ffa37bb754ed0c94e52f9f56c59d013ee.jpg)  
Fig. 4.

## Supporting Evidence

1. message about but not collocated with an SA-4 Battalian CP

![](/api/attachments/AK2F38AG/fulltext/images/15e118176c5ae6d7871554fd3763868f6fd97135e5039fe53e6ebb5b39dedff0.jpg)

## Specify evidence to explain further: > Current Message

MSGID/TACREP /DSU/116/8304061614Z//
WHAT/POSSIBLE SA-4 BN/061609Z//
WHERE/505356N/102301E/NB973395/0650/0280/000//

be placed in the colored box (see Fig. 6).

Very little empirical research has examined the contribution of graphics to decision effectiveness.

## Best Advice on Current Message.

## Degree of Belief.

The findings of the few studies [19,26,46] are somewhat inconclusive, with the main conclusion that the effects of graphics are highly dependent on the task [46].

Yet, much has been written on the benefits conjectured to occur. Benbasat and Taylor [5] cite two: (1) revealing relationships between information elements, and (2) partitioning categories of information. Decision performance is believed to be facilitated through reduction of cognitive effort in resolving a decision situation and by increasing the likelihood that it will be remembered for later use [17].

Under conditions of uncertainty, there is a need to develop a model with an appropriate repertoire of responses. Consequently, graphs are used to aid in simultaneously discriminating among alternate possible states of uncertainty and estimation of their values. Graphs provide quick convergence in reconciling new data with uncertain value with existing concepts. Thus, in addition to possessing a summarizing effect, graphs have dimensionality. Researchers [13] contend that graphs can be remembered better than tables, and that information can be comprehended faster with a graph.

Keeping in mind that DART users and their

the message to a new Air Defense Regimental HQ

![](/api/attachments/AK2F38AG/fulltext/images/aab16e9a39562cfb0b46ed6342f9a62e03cc877c5b8e1f81ba4d4f19ca10d303.jpg)

![](/api/attachments/AK2F38AG/fulltext/images/7d30c523e30415ec74a92f20cdfb88cd0ce03814409cc2d74bd2c6c6679e02a9.jpg)

Specify Advice Interpreter Option
Current Message
MSGID/TACELINT/DSU/133/8304061628Z//
SOI/061619Z/LONG TRACK/504050N/094622E/NB546146/0740/0290/000//

Fig. 6.

tasks, several IP techniques were considered and, subsequently, rejected. Narrative presentation was ruled out, due to the lack of data summarization. Tabular format was not considered, since the data lost its meaningfulness when so presented. Flashing was considered, but rejected due to the possibility that it would distract the analyst.

In order to avoid the problem of “clutter” on a single display, we avoided using several different symbols: they can interfere or compete with one another. In choosing a candidate symbol, we considered two factors: (1) its meaningfulness; i.e. how well it portrays its referent; and (2) its discriminability, as reflected in the speed and accuracy of detecting and/or identifying it in the context of other symbols. In this sense, a partially redundant color code can serve as a built-in code reference.

In addition, the use of relative weights, values, or utilities to represent degree of uncertainty, without partially redundant symbology, color, or graphs, was rejected. Research [36,41] has shown that users of decision aids do not prefer uncertainty information associated with distinct decision results. Due to the complexity and multidimensionality of the information presented in DART, the display of probability weights alone does not effectively capture the meaningfulness of the uncertainty information. We suggest that the IP techniques will help the user to assess the accuracy of predictions based on actual observed outcomes. In choosing IP alternatives, we recommend that information extraneous to the decision process be excluded from the user interface.

## 4. Concluding Remarks

The problem of portraying uncertain information in expert systems has been identified. Alternative IP techniques were presented with respect to an expert system designed to provide decision support in command and control settings.

We recommend that these techniques be assessed in any endeavor concerning the display of measures of goodness/risk/uncertainty that are outputs of decision support systems to ensure that they support the cognitive style of the user.

The purpose of this research was to identify alternative IP techniques that match the information processing demands of the task with the information capabilities of the user. Experimental methodologies must be employed to assess the appropriateness of IP techniques. Experimentation should be conducted in a laboratory setting prior to “field” testing. The aim of laboratory experimentation is to determine cause-effect relationships by systematic variation of treatment variables and random assignment of subjects [15]. Simulation or “gaming” can then be employed to provide realistic situations [2]. The simulation methodology [16] has a rich tradition as part of military training activities. It has been used to study crisis management [12] and the impact of aids on crisis decision making [3].

In this method, the subjects are presented with an appropriate scenario; treatment variables include the various ways of portraying the measures of goodness. The subjects performance would be measured by (1) the number of correct decisions made (as measured by standard protocols from the scenarios); (2) latency of response (i.e. the time between the initiation of an event and when the action was taken); and (3) the number of inquiries for additional information. Hence, data can be collected unobtrusively, as part of the gaming experience. A scoring system can be devised by an expert panel to provide a common measure of performance on time and correctness of decisions [2].

Along with the testing and evaluation of the IP techniques the potential users' cognitive style should be assessed. The possible effect that cognitive style may have on information processing has implications on the design of portrayal methods. The purpose is not to specify a particular cognitive style, but to identify the range of cognitive styles of prospective users. This, in turn, will provide a specification of the degree of robustness needed in the information portrayal technology.

## References

[1] Anderson, H.H., "Algebraic Model for Information Integration", Technical Report 45, Center for Human Information Processing, University of California, LaJolla, CA, June 1974.

[2] Belardo, S., Pazer, H.L., Wallace, W.A. and Danko, W.D., "Simulation of a Crisis Management Information Net-

work: A Serendipitous Evaluation", Decision Sciences, Vol. 14, No. 4, Fall 1983, pp. 588–506.

[3] Belardo, S., Karwan, K.R. and Wallace, W.A., "An Investigation of Design Considerations for an Emergency Management Decision Support System", IEEE Transactions on Systems, Man and Cybernetics, Vol. SMC-14, No. 6, November/December 1984, pp. 795–804.

[4] Bell, J., “The Effects of Presentation Form on the Use of Information in Annual Reports”, Management Science, Vol. 30, No. 2, February 1984, pp. 169–185.

[5] Benbasat, I. and Taylor, R.N., “Behavioral Aspects of Information Processing for the Design of Information Systems”, IEEE Transactions on Systems, Man, and Cybernetics, Vol. SMC-12, No. 4, July/August 1982, pp. 439–450.

[6] Biberman, L.M. (ed.), Perception of Displayed Information, New York: Plenum Press, 1973.

[7] Bruner, J.S., Olver, R., and Greenfield, P.M., Studies in Cognitive Growth, New York: Wiley Press, 1966.

[8] Ciccone, D.S., Samet, M.G. and Channon, J.B., A Framework for the Development of Improved Tactical Symbology, U.S. Army Research Institute (Alexandria, VA), ARI Technical Report 403, August 1979.

[9] Chervany, N.L. and Dickson, G.W., “On the Validity of the Analytic-Heuristic Instrument Utilized in the Minnesota Experiments: A Reply”, Management Science, Vol. 24, No. 10, June 1978, pp. 1091–1092.

[10] Christ, R.E., “Review and Analysis of Color Coding Research for Visual Displays”, Human Factors, Vol. 17, 1975, pp. 542–570.

[11] Cohen, P., Heuristic Reasoning about Uncertainty: An Artificial Intelligence Approach, Stanford, CA: Dept. of Computer Science, Stanford University, 1983.

[12] Cooper, D.F., “On the Design and Control of Crisis Games”, Omega Vol. 6, 1978, pp. 460–461.

[13] DeSanctis, G., “Computer Graphics as Decision Aids: Directions for Research”, Decision Sciences, Vol. 15, No. 4, Fall 1984, pp. 472–481.

[14] Dickson, G.W., Senn, J.W. and Chervany, N.L., “Research in Management Information Systems: The Minnesota Experiments”, Management Science, Vol. 23, No. 9, May 1977, pp. 913–923.

[15] Franklin, H.L. and Streufert, S., "Laboratory Experimentation", in M. Dunnette (ed.), Handbook of Industrial and Organizational Psychology, Rand McNally, Chicago, IL, 1976.

[16] Gaines, R.S., Noslund, W.E., and Strauch, R., Combat Operations Decision-Making in Tactical Air Command and Control, Santa Monica, Rand Corporation, Note: N-1633-AF, December 1980.

[17] Gremillion, L.L. and Jenkins, M.A., "The Effects of Color Enhanced Information Presentations", Proceedings, Conference on Information Systems, Boston, MA, December 1981.

[18] Huber, G., “Organizational Information Systems: Determinants of Their Performance and Behavior”, Management Science, Vol. 28, No. 2, February 1982, pp. 138–155.

[19] Ives, B., "Graphical Users Interface for Business Information Systems", MIS Quarterly, Special Issue, 1982, pp. 15–47.

[20] Jung, C.G., Psychological Types, Princeton, N.J.: Princeton University Press, 1971.

[21] Keen, P.G.W. and Bronsema, G.S., “Cognitive Style Research: A Perspective for Integration”, in C.A. Ross (ed.), Proceedings of the Second International Conference on Information Systems, Cambridge, MA, 1981.

[22] Lucas, H.C., Jr., "An Experimental Investigation of the Use of Computer-based Graphics in Decision Making", Management Science, Vol. 27, No. 7, July 1981, pp. 757–768.

[23] Lusk, E.J. and Kersnick, M., "The Effect of Cognitive Style and Report Format on Task Performance: The MIS Design Consequences", Management Science, Vol. 25, No. 5, August 1979, pp. 787–798.

[24] Mason, R. and Mitroff, F., "A Program for Research in Management Information Systems", Management Science, Vol. 29, No. 5, May 1973, pp. 475–487.

[25] Newell, A. and Simon, H.A., Human Problem Solving, Englewood Cliffs, N.J., Prentice-Hall, Inc., 1972.

[26] Powers, M., Lashley, C., Sanchez, P., and Shneiderman, B., "An Experimental Comparison of Tabular and Graphic Data Presentation", International Journal of Man-Machine Studies, Vol. 20, 1984, pp. 545–566.

[27] Remus, W., “An Empirical Investigation of the Impact of Graphical and Tabular Data Presentations on Decision Making”, Management Science, Vol. 10, No. 5, May 1984, pp. 533–542.

[28] Robey, D. and Taggart, W., “Human Information Processing in Information and Decision Support Systems”, MIS Quarterly, June 1982, pp. 61–71.

[29] Robey, D., “Cognitive Style and DSS Design: A Comment on Huber’s Paper”, Management Science, Vol. 29, No. 5, 1983, pp. 580–582.

[30] Rosnow, R.L. and Arms, R.L., “Information Load and Consumers”, Journal of Consumer Research, Vol. 4, No. 3, December 1977, pp. 148–155.

[31] Rouse, S.H., Rouse, W.B. and Hammer, J.M., "Design and Evaluation of an Onboard Computer-based Information System for Aircraft", IEEE Transactions on Systems, Man, and Cybernetics, Vol. SMC-12, 1982, pp. 457–463.

[32] Sage, A.P., “Behavioral and Organizational Considerations in the Design and Process for Planning and Decision Support”, IEEE Transactions on Systems, Man and Cybernetics, Vol. SMC-11, 1981, pp. 640–678.

[33] Salomon, G., "Can We Affect Cognitive Skills Through

Visual Media? An Hypothesis and Initial Findings", AV Communication Review, Vol. 20, No. 4, Winter 1972, pp. 401–422.

[34] Samet, M.G., and Geiselman, R.E., “Developing Guidelines for Summarizing Information”, Human Factors, Vol. 23, No. 6, 1981, pp. 727–736.

[35] Sidorsky, R.C., Gellman, L.H. and Moses, F.L., Survey of Current Developments in Tactical Symbology: Status and Critical Issues, U.S. Army Research Institute (Alexandria, VA), Working Paper HF 79-03, May 1979.

[36] Slovic, P., “Consistency of Choice Between Equally Valued Alternatives”, Oregon Research Institute Research Bulletin, Vol. 14, No. 11, 1974.

[37] Sprague, R., "A Framework for the Development of Decision Support Systems", MIS Quarterly, Vol. 4, No. 4, December 1980, pp. 1–26.

[38] Taylor, R.N., and Benbasat, I., “A Critique of Cognitive Styles Theory and Research”, Proceedings of the First International Conference on Information Systems, 1980.

[39] Tullis, T.S., “An Evaluation of Alphanumeric, Graphic, and Color Information Displays”, Human Factors, Vol. 23, No. 5, 1981, pp. 541–550.

[40] Tullis, T.S., “The Formatting of Alphanumeric Displays: A Review and Analysis”, Human Factors, Vol. 25, No. 6, 1983, pp. 657–682.

[41] Tversky, A., Elimination By Aspects: A Theory of Choice", Psychological Review, Vol. 79, 1972, pp. 281–299.

[42] Tversky, A., and Kahneman, D., “Judgement Under Uncertainty: Heuristics and Biases”, Science, Vol. 185, 1974, pp. 1124–1131.

[43] Witkin, H.W., “Origins of Cognitive Style”, In M. Scheerer (ed.), Cognition: Theory, Research, Promise, New York: Harper and Row, 1964.

[44] Wright, W.F., "Cognitive Information Processing Biases: Implications for Producers and Users of Financial Information", Decision Sciences, Vol. 11, 1980, pp. 284-298.

[45] Zmud, R.W., "Individual Differences and MIS Success: A Review of the Empirical Literature", Management Science, Vol. 25, No. 10, October 1979, pp. 966–979.

[46] Zmud, R.W., Blocher, E. and Moffie, R.P., “The Impact of Color Graphic Report Formats on Decision Performance and Learning”, Proceedings, The 4th International Conference on Information Systems, Houston, TX, December 1983.
