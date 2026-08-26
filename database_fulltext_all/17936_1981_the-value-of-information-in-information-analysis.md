---
otero_id: 17936
otero_key: "45N9TB7M"
title: "The value of information in information analysis"
authors: "Niv Ahituv; Malcolm C. Munro; Yair Wand"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90041-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Value of Information in Information Analysis\*

Niv Ahituv

Faculty of Commerce and Business Administration, The University of British Columbia, Vancouver, B.C. V6T 1Y8, Canada

Malcolm C. Munro

Faculty of Management, The University of Calgary, Calgary, Alberta T2N 1N4, Canada

Yair Wand

Faculty of Commerce and Business Administration, The University of British Columbia, Vancouver, B.C. V6T 1Y8, Canada

Information Requirements Analysis deals with defining the information needed for managerial purposes. It is considered as the first step of analysis in the development of an information system. This paper ties information requirements analysis with information evaluation. It is asserted that it is insufficient to simply find “needed” information items but also that such items should be evaluated in terms of their benefit.

Three approaches to information evaluation are considered – realistic, normative and subjective. It is asserted that the normative approach may sometimes be applied in lower organizational levels, while at higher levels subjective evaluation is used. Some examples are discussed in this context. Finally, we discuss some procedures for applying evaluation in information analysis.

Keywords: Information Evaluation, Information Requirements Analysis, Value of Information.

\* This paper was written while all the authors were affiliated with The University of Calgary.

An abridged version containing only some of the main ideas, references excluded, was presented in the 12th annual conference of the American Institute for Decision Sciences, Las Vegas, November 1980. It appeared in the proceedings under the title: "Information Requirements Analysis and Information Evaluation".

![](/api/attachments/45N9TB7M/fulltext/images/8cda6beef551d555efd9d0e6e2608461033bb25aab50167e20bad16dd3b309bb.jpg)

Niv Ahituv is an Assistant Professor at the Faculty of Commerce and Business Administration, The University of British Columbia. Formerly he lectured at The University of Calgary and at Tel-Aviv University, and managed the D.P. department at the Bank of Israel. He holds degrees of B.Sc. in Mathematics, M.B.A., M.Sc. and Ph.D., in Information Systems. His articles appeared in Computers and Operations Research, The Computer Journal, Information & Management, MIS Quarterly, and others. His main areas of interest are Economics of Computers, Information Economics, and Information Systems Management and Development.

![](/api/attachments/45N9TB7M/fulltext/images/a028005a7544139870436d6c2007a544c988a39d3ce0119328c60369c0e82c21.jpg)

Malcolm C. Munro is an Associate professor with the Faculty of Management, at The University of Calgary, in Calgary, Canada. He is a former chairman of the Management Science and Information Systems Area and is currently a co-editor of MIS Interrupt, an international MIS newsletter. He holds a B. Comm. with Honors from the University of Saskatchewan, and the M.S. and Ph.D. degrees in Management Information Systems from the University of Minnesota. His research interests include information requirements analysis and information evaluation.

![](/api/attachments/45N9TB7M/fulltext/images/63c9901216dd719c131f151f552c6dfec7367adf6ae9a955bd5e3a6d75c4fa2c.jpg)

Yair Wand is an Assistant Professor in the Faculty of Commerce and Business Administration at The University of British Columbia. He holds a D.Sc. in Operations Research from the Technion-Israel Institute of Technology. Before coming to U.B.C. he taught at the Faculty of Industrial Engineering and Management at the Technion and the Faculty of Management at the University of Calgary. He was also with IBM (Israel) Ltd. as a customer consultant. His research interests include development of interactive software for management, management information needs, and information evaluation models. His recent publications are in Decision Sciences, INFOR and Interfaces.

## 1. Introduction

The determination of information needs is a crucial part of the systems analysis and design process. This activity is called Information Requirements Analysis or, simply, Information Analysis (IA). It may be considered as the initial step of defining the "market needs" for a proposed information system. The importance of IA, its possible methodologies, and conceptual frameworks are widely discussed [1, 3,6,13,16,23,28,29,32,37].

Despite the importance of IA in system development, no methodology is widely accepted. On the research side, experimental work is rare [16,19,28,32]. This may be attributed to difficulties inherent in the analysis of information usage and the lack of techniques for assessing their benefits. These difficulties have at least three origins:

Firstly, the management process must cope with unanticipated situations; therefore, it may not be feasible to determine the related information needs in advance.

Secondly, even when problems are known in advance, the nature of human information processing is far from being fully understood [20].

Thirdly, the nature of most of the middle/upper level types of decision are such that it is very difficult to assess the benefits of an information system in tangible terms for use in cost/benefit analysis.

While these difficulties are severe obstacles from the methodological point of view, there exists a practical problem. Despite the oft-mentioned importance of Information Analysis, in practice it is neglected. One of several reasons for this is that most systems analysts have been involved in developing information systems for the operational levels of the organization. These applications (e.g., accounting and inventory control) tend to be structured so that most of the information requirements are obvious. As a result, systems analysts do not always perceive the importance of the IA phase when faced with less-structured situations. Another problem is that, while many steps of the systems development cycle are structured in nature (such as file design, program design and development), IA itself is essentially unstructured. The lack of structure in the IA process becomes particularly problematical when applied in a situation which is itself unstructured.

The above points to a need to bridge the gap between the abundant conceptual literature on the one hand and practical applications of IA activities on the other. To bridge the gap, two things are needed. Firstly, more sound experimental work should be carried out, such as testing and evaluating various IA methodologies in various situations. Secondly, experimental results need to be “translated” into the practitioners’ language; structured methodologies based on the research results should be developed.

The premise of this paper is that one of the key factors in IA experimentation is a better understanding of the concept of the value of information. In particular, tools for measuring the value of information are needed. These will enable researchers to conduct meaningful experimental research, and will enable practitioners to apply quantitative tools in the Information Analysis phase of systems analysis.

In this paper, the problems of incorporating information evaluation into IA research and practice are discussed. When and where these methods may be useful are suggested.

2. The Value of Information and Information Analysis

The goal of Information Analysis may be described as defining an information set to support decisions for a given situation. The three main dimensions of an information set are its content, timeliness, and format of presentation. Most works try to define how a situation can be characterized [25, 37], possible IA methodologies [3,16], and how to relate these three dimensions [2].

The content may be described as a list of information items or subsets. Thus, the result of the IA may be described as assigning to each possible information item in the environment a binary value: "needed", "not needed". This may be described as a dichotomous (0, 1) approach [17]. A refined approach would be to rank order the available data-items on a more detailed scale ranging from 'totally undesirable' up to 'highly desirable.'

The timeliness dimension mainly consists of two time-related attributes. The first is the "currentness" of the data: the time it takes from the occurrence of a relevant event until its effect is reflected in the database (i.e., coding, keytyping, validating, processing, and updating time). The second attribute is response time: the time it takes to provide a user with requested data that already exist in the data-base [14, page 83]).

The format dimension is primarily the medium by and shape in which the information is displayed (graphs, printed reports, visual display, etc.) see, for example, [2,40].

The fundamental challenge of the value approach in IA is to decompose the vague notion of 'information worth' into more concrete attributes, to find measures for the attributes, to investigate the trade-offs among them, and then to recompose an integrated value function for each alternative information set.

From the practical point of view, a value approach may be needed for:

1) comparing alternatives in terms of costs and benefits;

2) deciding on the order of implementation of parts of complex information systems, considering constraints on resources and time;

3) comparing needs of different users (departments or individuals). An example of this kind of application is the use of a Delphi technique [32].

The need to use the value of information is discussed in [17] and [21]. Also, the necessity of considering the potential utility of a system in enhancing decision making effectiveness is discussed in [18].

The authors are not aware of any commonly applied procedure for incorporating the value of information in the IA phase.

Although it is desirable to assign a real value to information (e.g., a dollar figure), this is usually not feasible, at least at the decision support level. At best, one can assign a relative value for information comparison purposes or perhaps compare alternatives by ranking them. There is a need, therefore, to find ways of measuring the (relative) value of information sets. Such measurement techniques may be the objectives of initial research or may be the tools which can be applied in eventual comparative research. Once developed and validated, these tools may be used as a part of more structured IA methodologies.

It should be noted that this use is similar to project selection and to the evaluation of existing information systems [22,31,36]. Indeed, a reliable technique can be used both as part of the IA effort and for later evaluation of the implemented system. The merit of this lies in facilitating communication between the users and the analysts.

## 3. The Value of Information

The most common approaches to the assessment of the value of information can be categorized as either realistic, normative, or subjective [2].

## 3.1. The Realistic Value Approach

Here the value of information is the change in actual performance due to the introduction of the information system. In this situation, the value of information is measured in terms of performance and, therefore, may be multidimensional. However, conversion of information value to monetary values is only possible if the performance measures themselves can be converted. This approach, though conceptually simple, is not always feasible: it is not always possible to prove a direct relation between new information and change in performance. The problem is even more intractable when we consider that we must know the value of information in advance of introducing the information system: thus changes in performance must be predicted. We conclude that, at best, the realistic value approach might be used in evaluating existing information systems.

## 3.2. The Normative Approach

Here, the value of information is calculated using a quantitative model of the relation between outcome measures and information. To do this, a model of the system is needed [9, page 90], usually a prohibitive demand.

The approaches to modelling are either analytic or simulative. The most comprehensive analytic approach is "Information Economics" which combines decision theory and utility theory to calculate the expected utility of a given information system. Information Economics assumes that the value of information can be assessed from users' perceptions encoded into event probabilities, and utility values assigned to possible outcomes of decisions. An information system is viewed as a probabilistic mapping from the set of possible events to a set of possible signals [8,10,24,26]. The results of such a model are only relative values of information. Other analytic modelings are of a less general nature and use concepts such as control theory [38,39].

Simulation models are of two kinds: in one kind, a system model is built with decision rules incorporated. Systems performance is evaluated under changing features of the input information such as time delay and probability of errors (e.g., [5,30]) In the other kind, decisions are made by human “decision makers” and performance is measured as a function of the information provided to them; e.g., the Minnesota experiments [33] and work by Mock [27].

The main problem with the normative approach is that since it is based on modeling, it may be very difficult to apply in non fully structured situations. Consequently, it is usually limited to operational level situations [5,30,35,38].

## 3.3. The Subjective Approach

In this approach, users are asked to evaluate some given information sets directly. The evaluation tool usually consists of a list of questions related to their various characteristics.

The main justification for this approach is that it combines the expertise and heuristic understanding of the users and implicitly incorporates human factors. These human factors include individual cognitive style [4] as well as factors which may improve the decision making environment without being really needed for a given decision [7, p. 452]. An obvious advantage is that subjective evaluations are relatively easy to conduct. The main disadvantage of subjective evaluations is that there is no direct relation between their results and any “real value” of information. They have the usual deficiencies of all subjective evaluations, such as semantic problems (possibility of fuzzy meaning) and inter-dependent data. By its very nature, a subjective evaluation is a purely relative tool. However, as indicated above, they can be used for comparative analysis.

## 4. Using Evaluation of Information in IA

In adopting an evaluation approach in Information Analysis, the nature of the evaluation problem must be considered. Evaluation problems may be classified according to two factors: system status and user level. Status refers to whether or not the information system already exists. If it exists, the evaluator is provided with data which are more concrete and real than if it does not. This factor may affect the selection of an evaluation approach.

User level refers to the organizational level served by the system. It is common to distinguish between four levels [14]. From bottom to top, the levels are Transaction Processing (TP), Operational Control (OC), Management Control (MC), and Strategic Planning (SP). It is likely that the higher the level, the less the realistic and normative approaches might be useful, because of the increasing complexity of the decision environment.

Table 1 exhibits a proposed typology of the appropriate information evaluation approach for the various combinations of status and level.

The following ideas are reflected in Table 1:

1) The higher the organizational level, the more difficult it is to determine tangible and measurable benefits; thus subjective evaluation becomes more essential in higher levels.

2) Realistic (revealed) value is obtainable only from analyses of changes in actual performance. Therefore, this approach is feasible only for existing systems (simulation of a proposed system is calssified under 'normative').

3) The normative approach requires modeling of the system, which can then be either analytically solved or tested via simulation. Modeling is possible only if the problem is structured (at least partly). Therefore, the approach is usually useful only for lower levels of decision problems. Even then, the results may serve only as an upper bound for the value of the information, since (in reality) decision makers do not operate optimally.

Table 1. Selection of Evaluation Approach as affected by Status and Level

<table><tr><td colspan="2">Status Existing</td><td>Proposed</td></tr><tr><td>Level</td><td>Information System</td><td>Information System</td></tr><tr><td>TP</td><td>realistic</td><td>normative</td></tr><tr><td>OC</td><td>realistic</td><td>normative</td></tr><tr><td>MC</td><td>realistic or subjective</td><td>subjective</td></tr><tr><td>SP</td><td>subjective</td><td>subjective</td></tr></table>

To sum up, there is no evaluation approach which is ultimately preferable, though the realistic approach seems to reflect the real impacts of the information system well. One must select an approach which is most suitable for the problem involved.

## 5. Examples

Here we discuss some examples of the evaluation of non-implemented information systems and show how they fall within the above classification scheme. The examples relate to the operational and management control levels.

Operational control is the only level for which quantitative modeling has proven feasible. Most models are for inventory or production control and assess the effects of a few information characteristics. The attribute investigated is usually timeliness of information, and sometimes accuracy. Examples of analytic models are [10], [35], and [38], (all these deal with inventory control). Examples of simulation models are [5] and [30] (these deal with production control).

Management Control generally uses subjective evaluation. Three examples are discussed below.

In research by Gallagher [11] involving an attempt to assess the monetary value of management reports the price managers were willing to pay for a report was correlated with their perceptions of the information characteristics and value. The price was understood as a subjective assessment in dollars. Another example appears in a study by Munro and Davis [28] where two techniques of generating information requirements for middle managers were compared; the information sets obtained by the two techniques (in different situations) were subjectively evaluated by the users. The evaluation tool was the same as used in [11]. A third example is given in [32] where information requirements of a group of managers were obtained using a modified Delphi technique. In each phase the users had to be subjective in evaluating information by assigning rank (importance) to the information items.

To summarize - while quantitative modeling is employed at the operational control level, requirements analysis at the management control level invariably employs subjective evaluation

## 6. Issues Related to Evaluation

The evaluation approach has only a small effect on the evaluation procedure; i.e., procedures using the different evaluation approaches are almost the same, regardless of the tools and type of value measured. The stages are as follows:

Firstly, one must determine the relevant attributes of contents, timeliness, and format of the information set.

Secondly, measures should be assigned to the various attributes, followed by definition of measurement techniques.

Thirdly, one should determine trade-offs among the attributes, so as to reduce the dimensionality of the evaluation. This is necessary to enable comparisons of various possible systems.

Finally, the measurement and the analysis must be performed, leading to some conclusions.

Prior to evaluation, the list of possible information items, which may be the components of the designed information set, must be generated by employing a particular technique of analysis. Such techniques could include decision analysis, data analysis, or any other method [16,23,28,32]. The idea is to detect all possible data items which are to be used by the decision maker.

One problem that should be carefully considered is the clarification for the user of the meaning of evaluation. A discussion about the evaluation tool with the user prior to its use it is therefore important and may contribute to the quality of the instrument (e.g., by identifying characteristics which do not appear in the instrument) and to the user's willingness to provide the evaluations.

Information characteristics may then be categorized as to content, timeliness, and format. The content itself may be categorized further to observed attributes (such as accuracy) and to perceived value to the user's function (usually in "decision making"). The latter is the most important yet most difficult to define: the user may be asked summarizing questions (probability of success, willingness to pay for a given report, etc.)

Several evaluation tools are described in the literature, for example, the semantic differential scale developed by Gallagher [11] and used in [28]. In this instrument, attributes of the information are expressed as bipolar adjectives (e.g., accurate-inaccurate) and the answer is expressed on a scale of, say, plus three to minus three. Another example is the Schultz-Slevin instrument [34] used in [19].

Other evaluation schemes are described in the context of project selection [22] and project evaluation of existing information systems [31,36].

Once user's evaluations have been obtained, they must be used to compare the various information items and information sets. Evaluation tools may consist of many items, therefore the resulting raw data cannot be used for comparison. The dimensionality of the data must be reduced. This is usually achieved by averaging over groups of evaluation items (characteristics). Two problems occur. First, how to define groups of related items, i.e., what is the "true" dimensionality of the value of the information. This subject is considered in the literature at the conceptual and normative level [1,10] and in some experimental work [40]. Second, various information characteristics have different significance in the eyes of the various users. As a result, an averaging process to reduce dimensionality may yield results which do not reflect the original views of the users. To overcome this obstacle, it is suggested that users be asked not only to evaluate the various characteristics but also assign relative importance to them. This can be done by either rank ordering the list of characteristics or by assigning them a scale value. These data can later be incorporated as weights into the averaging process. It is important to note that the data for each user should be processed using their views of the importance of characteristics.

The value measure obtained after dimensionality reduction will usually be multi-attribute. Further reduction to one score may only be possible if the trade-offs among the various attributes are known and measurable. In experimental research, multi-attribute values may be handled by analyzing each of the attributes separately. However, in practical application the candidate information items and sets have to be compared using all the attributes. Hence, there is a problem of ranking multi-attribute alternatives.

There are several possible ways of dealing with this problem [2,15]. One way is to ask the users to rank order the information items (or groups of information items) in terms of the score obtained on the various attributes and their value judgments of each of the attributes. Another way is to use a lexicographic order [15], in which the importance of the various attributes is first rank-ordered, and then attributes are compared by decreasing order of importance. Some small differences in values may be non-significant; therefore, some tolerance values have to be established in order to decide whether two values are really different. Another way may be to set constraints on some of the dimensions and to drop all possibilities which do not satisfy these constraints. In some cases, it may be possible to try to construct a user's combined utility function. Such an approach was applied to the evaluation of time sharing systems [12].

The above issues must be considered in applying an evaluation approach. Once data is available, one may use any approach which seems to fit. For the normative approach, these data would be used to calibrate the quantitative model that depicts the information system and the decision problem. For the realistic approach, the data should be used to prepare an appropriate experiment or field test which would identify differences in performance due to different information. For the subjective approach, the data would be used to develop statistical measures to estimate differences in subjective value.

In summary, three preparatory steps are involved in the evaluation:

1. information analysis, in which relevant data sets are defined.

2. information attributing, in which the relevant factors of the sets are identified.

3. tradeoffs identification, in which the dimensionality of the sets is reduced.

Once these steps are completed the road to evaluation is clear.

## 7. Conclusions

Two principal conclusions are reached: first, employing information evaluation procedures in information analysis is important; second, information evaluation approaches must be selected with regard to the organizational level at which the information users are operating. In particular, at the operational control level, some normative modeling may be possible; at higher levels, subjective evaluation is mostly used.

Another conclusion which seems interesting is that the evaluation procedure is not highly affected by the evaluation approach, i.e., there is a set of steps that should be taken in the Information Requirement Analysis phase, particularly related to information attributing and scaling, which is not dependent on the approach chosen for evaluation.

Finally, a comment should be made about the applicability of information evaluation in practice. There are several possible obstacles to successful implementation of some of the evaluation procedures.

First, there is no generally accepted set of information attributes. As well, there is no standard tool to assess or to measure the attribute values. Therefore, the analyst must devise appropriate evaluation tools for the situation under study. This may be a lengthy process, more than may usually be accommodated in practical systems analysis.

Secondly, the evaluation relies on information obtained from users. Therefore, its success depends on user cooperation and understanding. These are not always guaranteed, especially with highly sophisticated evaluation tools, which might deter the user.

Because of the above, the use of an evaluation scheme in the Information Analysis stage should be carefully considered. However, if an evaluation procedure is devised and employed, additional benefits are realized. First, the analyst will better understand what is important to users; second, users will better understand information traits, values and tradeoffs; and third, a tool which can be used in other phases of the system life cycle (in particular – post evaluation and periodical reviews) will be created.

## References

[1] C.R. Adams, "A Model for Studying the Relationships Between Decision Situations and Information Requirements", Proceedings of the 1972 Midwest AIDS Conference, N-9 to N-14.

[2] N. Ahituv, "A Systematic Approach towards Assessing the Value of an Information System", MIS Quarterly. Vol. 4, No. 4 (1980) pp. 61–75.

[3] M.L. Bariff, "Information Requirements Analysis: A Methodological Review", Working-Paper 76-08-02, The Wharton School, University of Pennsylvania, 1976.

[4] I. Benbasat, R.N. Taylor, "The Impact of Cognitive Styles on Information System Design", MIS Quarterly, Vol. 2 (1978), No. 2, pp. 43–54.

[5] D.F. Boyd, H.S. Krasnow, "Economic Evaluation of Management Information Systems", IBM Systems Journal, March 1963, pp. 2–23.

[6] R. Canning, "Getting the Requirements Right", EDP Analyzer, July 1977, Vol. 15, No. 7, pp. 1–14.

[7] G.B. Davis, "Management Information Systems: Conceptual Foundations, Structure, and Development", McGraw-Hill Book Company, 1974.

[8] J.S. Demski, "Information Analysis", Addison-Wesley Publishing Company, 1972.

[9] J. Emery, "Organizational Planning and Control", The McMillan Co., Collier-MacMillan Ltd, London, 1969.

[10] G.A. Feltham, "The Value of Information", The Accounting Review, Vol. 43 (1968) pp. 684–697.

[11] C.A. Gallagher, "Perceptions of the Value of Management Information System", Academy of Management Journal, Vol. 17 (1974), pp. 46–55.

[12] J.M. Grochow, "On User Supplied Evaluations of Time-Shared Computer Systems", IEEE Transactions on Systems, Man and Cybernetics, Vol. 3 (1973) pp. 204–206.

[13] J.A. Hoffer, "Information Requirements Analysis: An Experiential Review", Publication of the TIMS College on Information Systems, Vol. 3, No. 1, Jan 1977, pp. 1–25.

[14] P.G.W. Keen, M.S. Scott Morton, Decision Support Systems, Addison-Wesley Publishing Company, 1978.

[15] R.L. Keeney, H. Raiffa, "Decisions with Multiple Objectives: Preferences and Value Tradeoffs", John Wiley and Sons, New York, 1976.

[16] M. Kennedy and S. Mahapatra "Dynamics for Establishing the Flows of Information Needed for Effective Planning, Administration and Control", presented at the IFIP Congress, 1974.

[17] W.R. King and B.J. Epstein, "Assessing the Value of Information", Management Datamatics, Vol. 5 (1976), No. 4, pp. 172–180.

[18] W.R. King and D.I. Cleland, "The Design of Management Information Systems: An Information Analysis Approach", Management Science, 22(3), November 1975, pp. 286–97.

[19] W.R. King and J.I. Rodriguez, "Evaluating Management Information Systems", MIS Quarterly, September 1978, pp. 43–51.

[20] C.H. Kriebel, "The Evaluation of Management Information Systems", IAG Journal, Vol. 4 (1971), No. 1, pp. 1–14.

[21] B. Langefors, "Determining Management Information Needs: A Comparison of Methods", Discussion, MIS Quarterly, Vol. 1 (December 1977), pp. 53–56.

[22] H.C. Lucas Jr. and John R. Moore Jr., "A Multiple-

Criterion Scoring Approach to Information System Project Selection", INFOR, Vol. 14, No. 1 (February 1976) pp. 1–12.

[23] M. Lundeberg, "Information Analysis (IA) - an important method area in the analysis and design of information systems", Management Informatics, Vol. 3 (1974) pp. 45-56.

[24] J. Marschak, "Economics of Information Systems", Journal of the American Statistical Association, Vol. 66, No. 333 (March 1971) pp. 192–219.

[25] R.O. Mason and I.I. Mitroff, "A Program for Research on Management Information Systems", Management Science, Vol. 19 (1973) pp. 475–487.

[26] C.B. McGuire and R. Radner, "Decision and Organization", North Holland Publishing Co., 1972, Chapters 1, 5.

[27] T.J. Mock, "Comparative Values of Information Structures", Journal of Accounting Review, Empirical Research in Accounting: Selected Studies, Supplement to Vol. 7 (1969) pp. 124–159.

[28] M.C. Munro and G.B. Davis, "Determining Management Information Needs: A Comparison of Methods", MIS Quarterly, Vol. 1 (1977) pp. 55–67.

[29] M.C. Munro, Y. Wand "On Empirical MIS Research: The Case of Information Requirements Analysis", Working Paper 21–79, Faculty of Management, The University of Calgary, March 1980.

[30] R. Narasimhan, "A Simulation Analysis of Timelines and Accuracy of Information on System Performance", Proceedings of the 10th Annual Conference of the American Institute of Decision Sciences, St. Louis, October 78, pp. 143–145.

[31] S. Neumann and E. Segev, "A Case Study of User Evaluation of Information Characteristics for Systems

Improvement", Information & Management, Vol. 2 (1979), pp. 271–278.

[32] W. Remus, R.H. Sprague, and P. Pinto, "Assessing Information Needs Using a Modified Delphi Technique", Proceedings of the 8th Annual Conference of the National AIDS, pp. 543–545.

[33] P.G. Schroeder and I. Benbasat, "An Experimental Evaluation of the Relationship of Uncertainty in the Environment to Information used by Decision Makers", MISRC-WP-73-06, University of Minnesota, Aug. 1973.

[34] R.L. Schulz and D.P. Slevin, "Implementing Operations Research/Management Science", American Elsevier Publishing Company, Inc., 1975, pp. 153–183.

[35] E.A. Stohr, "Information Systems for Observing Inventory Levels", Operations Research, Vol. 27 (1979), pp. 242–259.

[36] E.B. Swanson, "Management Information Systems: Appreciation and Involvement", Management Science, Vol. 21, No. 2, (October 1974), pp. 178–188.

[37] W.M. Taggart and M.O. Tharp, "Dimensions of Information Requirements Analysis", Data Base No. 7, Summer 1975, pp. 5–13.

[38] C.S. Tapiero, "Optimization of Information Measurement with Inventory Applications", INFOR, Vol. 15 (1977), pp. 50–60.

[39] P.H. Wilmes and A. Herrmans, "The Impact of On-Line Information Systems on Corporate Strategic Decision-Making", Paper submitted to TIMS-ORSA, Los Angeles, November 1978.

[40] R.W. Zmud, "An Empirical Investigation of the Dimensionality of the Concept of Information", Decision Sciences, Vol. 9 (1978) pp. 187–195.
