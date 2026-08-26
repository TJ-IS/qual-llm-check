---
otero_id: 17016
otero_key: "SKQGPC6D"
title: "Decision Support Systems: A summary, problems, and future trends"
authors: "M.C. Er"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90022-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision Support Systems: A Summary, Problems, and Future Trends

M.C. ER

Department of Computer Science, St. Patrick's College, National University of Ireland, Maynooth, Co. Kildare, Ireland.

This paper critically examines issues confronting Decision Support Systems (DSS) in the business/management area. Due to the lack of acceptable definition $\phi$ DSS, the characteristics and components of DSS are discussed in detail. It is pointed out that work activities that require decision making form a spectrum of problems ranging from structured problem to unstructured problem. It is further pointed out that personality and cognitive style can influence individuals' decision styles, and thus different decision aids will be sought. DSS development and applications are briefly described. Finally, the major problems facing current DSSs are outlined, and the future trends of DSS are described.

Keywords: Decision Support Systems, Types of Problems, Decision Styles, Development, Applications, Unsolved Problems, Future Trends

![](/api/attachments/SKQGPC6D/fulltext/images/63ad5f601f06f3e699aea56ab79a74318b7c020102e984e5f77d8d8838632e0a.jpg)

M.C. Er is Foundation Professor and Head of Department of Computer Science at St. Patrick's College, National University of Ireland. Previously he was W.F. James Chair Professor at the St. Francis Xavier University in Canada. Dr. Er has published numerous refereed papers in many international journals, and is a widely sought referee, regularly approached by many international journals to referee submitted research papers.

## 1. introduction

The development of the field known as Information Systems started as Electronic Data Processing (EDP), the Management Information System (MIS), and finally Decision Support System (DSS). EDP primarily deals with the transaction processing type of applications. This is quite expected given the fact that computers were originally designed and built for solving the problems of tedious calculations (such as calculating logarithm table and ballistic table) and laborious clerical tasks (such as census tabulation). The main purpose was to develop applications programs that were capable of automating manual works. Computerised systems so developed were piecemeal and isolated from each other. Furthermore, pure applications in EDP do not quite match the image of general-purpose computer which is capable of doing anything that is computable. In the mid 60's, the term Management Information System (MIS) was coined to signal a new attempt to develop integrated computer-based information systems that were capable of processing and supplying all information needed by management. As it turns out, this ambitious aim results in great disappointment due to the immaturity of technologies and methodologies (Dearden, 1972; Klein and Hirschheim, 1985). To complement EDP and also to shift the attention away from MIS, the term Decision Support System (DSS) was coined by Keen and Scott Morton (1978) to denote the other aspect of information processing, namely the provision of information for supporting management decision making. Hence EDP and DSS are complementary halves of Computer-Based Information System (CBIS) (see fig. 1).

Unfortunately, after a decade of the development of DSS, there is still no accepted definition of DSS. To quote one of the originators of DSS, Keen (1986) says:

‘Right from the start of the DSS movement, and even now, there has been no established definition of DSS.’

![](/api/attachments/SKQGPC6D/fulltext/images/a39e51cc6c494ebca1b7ff69b4712a1e9eb3d4d091052bdcd236ba59975e1e84.jpg)  
CRIS  
Fig. 1. Electronic data processing (EDP) and decision support system (DSS) are complementary halves of computer-based information system (CBIS).

This is very surprising and disturbing. One naturally raises questions about the future of DSS: will it follow the foot-steps of MIS? A field without definition has the flexibility of expansion and changing direction, but also has the danger of falling apart. Consequently, it is possible to generate heated debate and disagreement. As an example, are the followings DSSs or tools of DSSs:

• non-programmable calculator,

\- programmable calculator,

\- financial modelling,

\- spreadsheet,

\- statistics package,

\- PERT/CPM/linear programming,

\- simulation,

\- expert system.

For instance, non-programmable or programmable calculator can be used for calculation during decision making - is it a DSS? Similarly, PERT/CPM can be used for generating alternatives for facilitating decision making by changing parameters and assumptions - is it also a DSS?

One may argue that it is possible to use the intention of a design to differentiate DSS from non-DSS. However, it is easy to find counterexamples. For instance, is a statistics package a DSS? – clearly a statistics package was not intended to be a DSS but is used heavily in decision making under some circumstances. Similarly, some early financial modelling packages (Greenwood, 1969) that were not intended to be DSSs can be adapted to be DSSs by altering the user interface.

Nevertheless, some authors have attempted to define the term Decision Support System. Their definitions, however, can be faulted in one way or another. For instance, Keen and Scott Morton (1978) gave an earlier definition of DSS:

'The application of available and suitable computer-based technology to help improve the effectiveness of managerial decision making in semi-structured tasks.'

Here, the phrase ‘available and suitable computer-based technology’ does not have a unique meaning, and varies with time. Furthermore, the term ‘semi-structured tasks’ is undefined, and may vary from person to person. The reader is invited to consider whether or not computer simulation is a DSS.

Against this background, Owen and Volpato (1985) made an insightful comment from the practical point of view:

'A wide variety of computer based systems have been sold for many years under the label of Decision Support Systems. These have included financial modelling packages, information retrieval and statistical analysis systems. Most have failed to be used by executives, because they have not got to the heart of how most decisions are taken – that is on the basis of personal experience and subjective judgement, elements which were previously considered as being incapable of analysis but ones which are significantly powerful enough to alter any course of action.'

In the next two sections, we give a more precise characterization of DSS. In the subsequent sections, we discuss types of problems, decision styles, DSS development and applications, problems facing DSS and its future development.

## 2. Characteristics and Components of DSS

Faced with the difficulty of defining DSS, Sprague and Carlson (1982) felt easier to give a list of characteristics of DSS:

\- They tend to be aimed at the less well structured, under-specified problems that upper-level managers typically face.

\- They attempt to combine the use of models or analytic techniques with traditional data access and retrieval functions.

\- They specifically focus on features that make them easy to use by noncomputer people in an interactive mode.

\- They emphasize flexibility and adaptability to accommodate changes in the environment and decision-making approach of the user.

To this list, we add another characteristic of DSS:

\- They support but do not replace upper-level managers in decision making.

This characteristic is important as it differentiates DSS from Expert System.

Another approach taken by King (1983) is to characterize DSS by a list of components that any integrated DSS should have:

(a) decision models,

(b) interactive computer hardware and software,

(c) a data base,

(d) a database management system,

(e) graphical and other sophisticated displays,

(f) a modelling language that is 'user friendly'.

As the types of problems to be solved, domains of applicable knowledge, and types of targeted users are not specified, King's (1983) set of DSSs is larger than the set of DSSs normally perceived by others (Keen and Scott Morton 1978, Huff, 1985; Hogue, 1985; Meador, Guyote and Rosenfeld, 1986) in the area of information systems. For example, computer-assisted medical diagnosis and town planning are also included in King's set of DSSs.

## 3. Decision, Support and Systems

Commenting on the development of DSS in the last ten years, Keen (1987) suggested the needs to adopt a balanced approach to the three aspects of DSS – namely, Decision, Support and Systems. This is in response to the recent swing towards DSS building.

Although many management scientists use the term DSS without qualification, it is clearer to call it Management Decision Support System. The word decision in DSS implies problem solving. Indeed, decision and problem solving go hand-in-hand – in making decisions, one is solving problems; conversely, in solving problems, one is making decision at each step. Furthermore, problem solving implies the use of knowledge in the process of solving problem. Hence, applications of knowledge, in the form of models, need to be incorporated into DSSs. To be effective, it is essential to know whether a decision to be made will be made by an individual or a group based on single or multiple criteria.

The support aspect of DSS implies the use of computer and software technologies to support managers during the process of decision making. Hence it is necessary to understand preferences of people while they are making decisions. There are four types of support that can be provided to decision makers, and are summarized below:

(1) Passive Support. Provide decision makers with DSS that they are comfortable with to allow them to make autonomous decisions.

(2) Traditional Support: Provide DSSs to decision makers to mesh with the decision and its improvements.

(3) Extended Support: Alternatives are actively suggested by DSSs to decision makers.

(4) Normative Support: DSSs dominate the whole decision process, and managers are there to provide inputs and specifications.

The word system in DSS deviates from the meaning of system used in Checkland (1981). In the context of DSS, system implies a system of man-machine interactions and its design and implementation. An integrated approach, in this case, is important, especially if the system is to link with existing databases using computer networks.

## 4. Types of Problems and Decision Style

Generally speaking, there are three types of problems to be solved by management: structured, semi-structured, and unstructured. The boundaries between them, however, are not as clear cut as they sound. Sometimes the classification is also dependent on the existence of methods for solving the problems. For instance, before the advent of linear programming, profit maximization or cost minimization was considered as a semi-structured problem; nowadays, with the availability of simplex method, the problem is generally reduced to a structured problem.

Levels of Management Activities

<table><tr><td rowspan="4">Types of Problems</td><td></td><td>Operational Control</td><td>Management Control</td><td>Strategic Planning</td></tr><tr><td>Structured</td><td>inventory reordering quantity</td><td>Setting production level</td><td>Plant&#x27;s location</td></tr><tr><td>Semi-structured</td><td>Share trading</td><td>Setting budget</td><td>Capital acquisition</td></tr><tr><td>Unstructured</td><td>Package design</td><td>Selecting a new manager</td><td>Information systems portfolio</td></tr></table>

Fig. 2. The combinations of the types of problems and the levels of management activities.

The levels of management activities, generally, can be classified into operational control, management control, and strategic planning, which are performed by supervisory management, middle management, and top management, respectively. In general, supervisory management deals more with structured problems affected by internal factors, top management more with unstructured problems affected by external factors, with middle management sitting in the middle. The combinations of the types of problems and the levels of management are shown in fig. 2 (Huff, 1985).

<table><tr><td>Level number</td><td>Organizational level</td><td>Time span</td><td>Number of DSSs</td><td>Capabilities of DSSs</td></tr><tr><td>7</td><td>multinational corporation</td><td>20 ~ 50 yrs</td><td>none</td><td></td></tr><tr><td>6</td><td>corporate group</td><td>10 ~ 20 yrs</td><td>none</td><td></td></tr><tr><td>5</td><td>corporate subsidiary</td><td>5 ~ 10 yrs</td><td>none</td><td>articulation of goal setting</td></tr><tr><td>4</td><td>general management</td><td>2 ~ 5 yrs</td><td>very few</td><td>selecting from types</td></tr><tr><td>3</td><td>department managerial</td><td>1 ~ 2 yrs</td><td>a few</td><td>restructuring within fixed structure</td></tr><tr><td>2</td><td>Front line managerial</td><td>3 months ~ 1 yr</td><td>many</td><td>altering judgement on variables</td></tr><tr><td>1</td><td>shop and office floor</td><td>&lt; 3 months</td><td>many</td><td>judgement within fixed structured</td></tr></table>

Fig. 3. A spectrum of work activities and associated decision making.

Work activities, in a typical multi-national corporation, that require decision making span the whole spectrum of problem types, from structured problem to unstructured problem. An example is shown in fig. 3 (Humphreys, 1984; Phillips, 1984). Currently no DSS is capable of supporting management decision making beyond level 4, where strategic planning is crucial. Even at level 4, very few DSSs have been implemented for supporting general management.

On the other hand, very few existing DSSs (Ginzberg, Reitman and Stohr, 1982; Sol, 1983) take into account individual's decision style – this is very surprising. It is well known that personality influences one's decision style (Nutt, 1986), which in turn determines one's preference in selecting decision aids. In designing DSSs for individuals, clearly this aspect must be taken into account in order to maximize the effectiveness of DSSs.

For measuring cognitive style, it is generally agreed that the Myers-Briggs type indicator (MBTI) satisfies the predictive validity property. Cognitive style can be measured along two dimensions: preferred way of getting data and preferred way of processing data. In the former dimension, an individual may be classified as sensing (S) or intuition (N). In the latter dimension, an individual may be differentiated as thinking (T) or Feeling (F). A sensing individual prefers hard data that deal with specific problems. In contrast, an intuitive individual prefers holistic information that describes possibilities. On the other hand, a thinking type uses logic and other formal means for reasoning. In contrast, a feeling type places consideration of decision in personal terms. The combinations of these two dimensions yield the following four decision styles:

(1) Systematic (ST)

Systematic type individuals use quantitative measures on information and, prefer cost-benefit analysis and evaluation research as decision aids.

Speculative type individuals speculate future possibilities, and prefer decision trees with sensitivity analysis as decision aids.

(3) Judicial (SF)

Judicial type individuals concentrate on current situation, and prefer the use of decision groups.

(4) Heuristic (NF)

Heuristic type individuals place great emphasis on current possibilities, and prefer reaching decisions through mutual adjustment.

From the above discussion, it is self-evident that individuals with different decision styles prefer different types of decision support. For example, systematic decision makers prefer DSSs that can support cost-benefit analyses of hard data, whereas speculative decision makers prefer DSSs that can provide 'what-if' analyses. Thus the usual approach to providing all decision makers with the same DSS may not suit individuals' tastes, and hence decision making is less effective than it should be. Obviously more research efforts should be directed at matching DSSs with individuals' decision styles.

Furthermore, it is necessary to take into account individuals and circumstances that decision making is based on risk adverse or risk taking, so that

1. Decision support analysis
- structured interviews
- decision analysis
- data analysis
- technical analysis
- conceptual DSS orientation
- plans and prioritization

2. DSS software evaluation and selection
- identification of candidate vendors
- feature analysis
- benchmarks
- external site surveys

3. Prototype development
- scoping of prototype
- project evaluation criteria
- detailed design
- system construction
- testing
- demonstration
- evaluation

4. Operational deployment and support
- functional orientation
- operational training
- deployment
- maintenance

Fig. 4. A four-stage process for developing DSS.

more versatile DSSs can be developed. It is important to known that human decision makers generally do not make decisions based on the probability of success, because the penalty for a vital decision that turns out to be wrong is normally substantial.

In summary, decision technology should be centred on problem solvers (with experience, intuition and knowledge) supplemented by information technology (computers, software, databases, networks, and modelling) and preference technology (value judgements, time and risk preferences, and trade-offs) (Phillips, 1984).

## 5. DSS Development

Some practitioners have mistaken DSS to be spreadsheet, and thus thought that DSS development was as simple as purchasing a spreadsheet package. In fact, spreadsheet is a simplistic type of DSS. More complex and sophisticated DSSs suitable for supporting various decision making processes need to be developed and built in-house. Meador, Guyote and Rosenfeld (1986) proposed a four-stage process for developing a DSS: decision support analysis, DSS software evaluation and selection, prototype development, and operational deployment and support. Details may be seen in fig. 4.

![](/api/attachments/SKQGPC6D/fulltext/images/eaae7695cf5053427e525fefb83c597a7744ec52f061420f5e2461c936d15f98.jpg)  
Fig. 5. Keen and Scott Morton's (1978) predesign cycle.

In an earlier attempt, Keen and Scott Morton (1978) proposed a predesign cycle for developing DSS (fig. 5). Indeed, if one knows where the problems is, one has solved half of the problem (Landry, Pascot and Briolat, 1985). For really unstructured problem, it is generally hard to pinpoint where the problem is. Perhaps the use of problematique is a better word for describing the situation, rather than problem or problematical.

## 6. DSS Applications

Hitherto, most DSSs are applied to structured and semi-structured problems. A list of existing DSS applications, non-exhaustive of course, is given below:

## • Corporate financial planning

\- loan amortization

\- depreciation

\- lease versus buy

– discounted cash flow and net-present value

\- break-even analysis

• Marketing analysis

\- forecasting

\- sales analysis

\- promotion analysis

\- consumer sales audits

• Real estate investments

\- financing alternative

\- cash flows

\- impact on taxes

\- payoff

\- Mineralogical exploration

\- Transportation routing

\- Porfolio analysis.

Obviously, more DSS applications can be added to the list, and the limitations are human's creativity and imagination.

## 7. Problems Facing DSSs

After a decade of building, developing and using DSSs, many problems have surfaced and need to be solved eventually. We list below some of the commonly seen problems:

## (1) Data capture and collection

How to capture and collect data remains an unsolved problem. Many DSSs are not compatible with each other, forcing decision makers to retype data and thus creating unnecessary duplication of data and efforts. Problems also arise from the non-compatibility of purchased DSSs with existing databases and computer networks.

## (2) Data integrity and secutiry

Duplication of data poses a data integrity problem whereby data are at different cycles of update. Furthermore, the scattering of sensitive data at different places poses the security problem which is hard to control.

## (3) Unstructured problems

There is a need to extend DSSs to solve unstructured problems which are commonly faced by top executives who make vital decisions.

## (4) Management of DSSs

With small DSSs built and forgotten, and large DSSs constantly under modifications without documentations, there is a real need to manage the process and product of DSS development. Otherwise the whole thing is running out of control, especially when key developers resign.

## (5) Cost-effectiveness

Is a DSS cost effective? Clearly some justifications are needed before committing personnel and monetary resources to the development of a DSS. The traditional cost-benefit analysis may not be the best approach for assessing the benefit of an innovation. Keen (1981) proposed the value analysis which stresses value first and cost second. However, is there a better way for assessing opportunity cost?

## (6) Standardization

There is a need to standardize some basic features of DSSs so that they can be used by more decision makers but at the same time taking into account individual differences in terms of decision style. Is there a way that the conflicting requirements can be resolved?

## (7) Individual versus group DSSs

How to support individual decision makers during a group meeting is also a pressing problem to be resolved. Should all individuals use the same DSS and see the same thing, or should individuals be allowed to use their tailor-made DSSs during a group decision making?

(8) Data are not independent of spreadsheets
Data used by a spreadsheet normally cannot be used by different spreadsheet, resulting in data being tied up with spreadsheets. An agreeable industrial standard for all spreadsheets may not come easy.

## 8. Future Trends of DSS

Despite the fact that there is no acceptable definition, DSS is here to stay simply because it complements the transaction processing aspect of EDP. However, it will take some time before DSS reaching a mature stage. As it stands, the following future trends of development of DSS are identifiable:

## (1) Group DSS

Group decision making plays a major role in determining corporate affairs (Young, 1983). How to design and develop group DSSs for supporting group meetings is a complex task because of the complex combination of people, places, time communication networks, individual preferences, and other technologies. A group meeting can be conducted at the same place, or at different places attended by different groups of people using teleconferencing techniques. On the other hand, a group meeting can be conducted during a fixed period of time, or it is just an unlimited on-going process. Group DSS is supposed to support any one of the possible combinations (DeSanctis and Gallupse, 1985).

## (2) Decision support centre

Decision support centre is an emerging concept (Owen and Volpato, 1985). A decision support group, staffed by information systems professionals who understand the business environment, form the core of decision support centre, with advanced information technology. A decision support centre is usually located in close proximity to top management so that instant decision support can be provided. A decision support group will readily develop or modify DSSs to support top management in making urgent and important decisions.

## (3) Strategic DSS

DSS for supporting strategic management is a well recognised area of importance and significance (King, 1984). It is an area where DSS can make a substantial impact on the top management and the corporation. The generic SICIS issue tree (King, 1984) sounds trivial, and the SPIRA process for achieving information-based strategic comparative advantage (King, 1984) resembles Checkland's (1981) soft system methodology.

## (4) Intelligent DSS

Some authors, notably Nolan (1986), suggest the adaptation of artificial intelligence (AI) and expert systems techniques to DSS. However, most authors under-estimate the difficulties in representing common-sense knowledge which is an unsolved problem in AI.

## References

Checkland, P.B. (1981), Systems Thinking, Systems Practice, John Wiley: Chichester.

Dearden, J. (1972), MIS is a Mirage, Harvard Business Review, Vol. 50, No. 1, pp. 90–99.

DeSanctis, G. and Gallupe, B. (1985), Group Decision Support Systems: A New Frontier, Data Base, Vol. 16, No. 2, pp. 3–10.

Ginzberg, M.J., Reitman, W. and Stohr, E.A. (1982), Decision Support Systems, North-Holland: Amsterdam.

Greenwood, W.T. (1969), Decision Theory and Information Systems, South-Western Pub.: Cincinnati.

Hogue, J.T. (1985), MIS Manager's Guide to Decision Support Systems, Data Processing Management, pp. 1–8.

Huff, S.L. (1985), Decision Support Systems, Computer Programming Management, pp. 1–11.

Humphreys, P. (1984), Levels of Representation in Structuring Decision Problems, Journal of Systems Analysis, Vol. 11, pp. 3–22.

Keen, P.G.W. (1981), Value Analysis: Justifying Decision Support Systems, MIS Quarterly. Vol. 5, pp. 1–15.

Keen, P.G.W. (1987), Decision Support Systems: The Next Decade, Decision Support Systems 3, 253–265.

Keen, P.G.W. and Scott Morton, M.S. (1978), Decision Support Systems: An Organizational Perspective, Addison-Wesley: Reading, MA.

King, W.R. (1983), Achieving the Potential of Decision Support Systems, Journal of Business Strategy, Winter, pp. 84–91.

King, W.R. (1984), Strategic Management: Decision Support Systems, in manuscript.

Klein, H.K. and Hirschheim, R. (1985), Fundamentals Issues of Decision Support Systems: A consequentialist Perspective, Decision Support Systems, Vol. 1, pp. 5–24.

Landry, M., Pascot, D. and Briolat, D. (1985), Can DSS Evolve Without Changing Our View of the Concept of 'Problem'? Decision Support Systems, Vol. 1, pp. 25–36.

Meador, C.L., Guyote, M.J. and Rosenfeld, W.L. (1986), Decision Support Planning and Analysis: The Problems of

Getting Large-Scale DSS Started, MIS Quarterly, Vol. 10, pp. 159–177.

Nutt, P.C. (1986), Decision Style and Its Impact on Managers and Management, Technological Forecasting and Social Change, Vol. 29, pp. 341–366.

Owen, D. and Volpato, M. (1985), Focusing High Technology on the Executive Decision-Making Process, The Australian Director, Vol. 15, April/May, pp. 20–24.

Pillips, L.D. (1984), Decision Support for Manager, in The Managerial Challenge of New Office Technology, (ed) H. Otway and M. Peltu, Butterworths: London, pp. 80–98.

Sol, H.G. (1983). Processes and Tools for Decision Support, North-Holland: Amsterdam.

Sprague, R.H. jr and Carlson, E.D. (1982), Building Effective Decision Support Systems, Prentice-Hall: Englewood Cliffs, New Jersey.

Sprague, R.H. jr and McNurlin, B.C. (1986), Information Systems Management in Practice, Prentice-Hall: Englewood Cliffs, New Jersey.

Young, L.E. (1983), A Corporate Strategy for Decision Support Systems, Journal of Information Systems Management, Vol. 1, No. 1, winter.
