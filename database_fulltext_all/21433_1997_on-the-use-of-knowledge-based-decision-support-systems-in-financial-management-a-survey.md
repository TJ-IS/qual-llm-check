---
otero_id: 21433
otero_key: "UG9HFG6U"
title: "On the use of knowledge-based decision support systems in financial management: A survey"
authors: "C. Zopounidis; M. Doumpos; N.F. Matsatsinis"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00002-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the use of knowledge-based decision support systems in financial management: A survey

C. Zopounidis \*, M. Doumpos, N.F. Matsatsinis

Technical University of Crete, Department of Production Engineering and Management, Decision Support Systems Laboratory, University Campus, 73100 Chania, Greece

## Abstract

This paper presents an extended survey of the application of knowledge-based decision support systems (KBDSSs) in financial management. KBDSSs originated from the combination of decision support systems with expert system (ES) technology. Thus, initially, the implementation of both decision support systems and ESs in several fields of financial management is discussed. The existing problems and limitations of these two approaches are outlined, and the new methodological framework based on the use of KBDSSs and its application in financial management are presented. © 1997 Elsevier Science B.V.

Keywords: Decision support systems; Expert systems; Financial management; Knowledge-based decision support systems; Multicriteria decision aid

## 1. Introduction

Decision making in general, and specifically financial decision making, has been significantly improved, in the last two decades, through the rapid progress of information technology and computer science. Decision making in the financial management field is a very complicated process, where decision makers (managers of companies, managers of credit institutions, individual investors, etc.) face, on a daily basis, a large volume of information that should be examined in order to make the final decision concerning the performance or the viability of a firm, the granting or denying of a credit application, the construction and management of a portfolio, the choice of an investment, or the construction of a financial marketing plan.

The combination of decision theory with the new knowledge and the powerful tools offered by computer science and information technology, led to the development of new types of information systems able to support decision makers and improve the decision-making process.

Basically, the efforts in supporting the whole decision-making process focused in the development of computer information systems providing the support needed. Two types of systems were developed: (1) decision support systems (DSSs) and (2) expert systems (ESs). Although these two approaches were very promising, their implementation revealed several problems.

To overcome these problems without missing the advantages of both ESs and DSSs, a new type of intelligent system called a knowledge-based DSS (KBDSS) has been proposed. The basic characteristic of this new approach is the integration of ES technology with models and methods used in the decision support framework, such as mathematical programming methods, multicriteria decision aid methods, and multivariate statistical methods.

The aim of this paper is to present a survey of the implementation of KBDSSs in financial management. Initially, the previous work concerning the implementation of DSSs and ESs in several fields of financial management is presented (Section 2). Then, the new capabilities derived by the combination of knowledge, which is represented in an ES, with the powerful analytical tools used in DSSs, will be discussed through the presentation of some implementations of the new methodological approach based on KBDSSs (Section 3). The KBDSSs that are presented in Section 3 have been selected as some representative examples of the new methodological framework, covering several fields of financial management (i.e. credit scoring, financial analysis, portfolio selection and management, etc.). Finally, concluding remarks and future perspectives are presented (Section 4).

## 2. DSSs and ESs

The concept of DSSs was introduced, from a theoretical point of view, in the late 1960s. Klein and Methlie [30] define a DSS as a computer information system that provides information in a specific problem domain using analytical decision models as well as techniques and access to databases, in order to support a decision maker in taking decisions effectively in complex and ill-structured problems. Thus, the basic goal of a DSS is to provide the necessary information to the decision maker, in order to help him get a better understanding of the decision environment and the alternatives he faces.

The decision process in the field of financial management, as mentioned above, involves the analysis of a large volume of data and information. Therefore, the need to access large databases and perform computations in real time is vital. The applicability of the DSS technology to these kinds of tasks has already led researchers to implement DSSs in most of the fields of financial management, such as:

• financial planning [14,23,28,73];

• financial analysis [36,37,72,93];

\- portfolio management [19,68,90];

\- banking [31,38,74].

An extended review of the applications of DSSs in several areas of decision making, found in the international literature, is presented by Eom and Lee [13], while Er [17] discusses in detail the main characteristics and components of DSSs, describes some problems encountered in their implementation involving business and management areas, and presents the future trends of DSSs. Radermacher [59] presents the scope of DSSs, through the discussion of the notion of decision and related cognitive concepts, and describes the potential of DSSs in improving the decision-making process, while Eom et al. [15] carried out bibliographic research to identify the various subfields of DSS research, the contributing disciplines of DSS (MCDM (multiple-criteria decision making), MCDSSs (multicriteria decision support systems) and GDSS (group DSS)) and the subsets of functional management (financial management, marketing management, etc.) which have influenced the development of specific DSSs. Pomerol and Ibp [57] describe the main features of the existing MCDSSs, to explain their weaknesses and suggest necessary developments and research to meet in reality the decision makers' needs.

The contribution of DSS technology can be summarized as follows [82].

\- DSSs provide the necessary means for dealing with semi-structured and unstructured problems of high complexity, such as many problems from the field of financial management. Apart from the access to data and model bases that DSSs provide, they support all the stages of the decision process, i.e. the structuring of the problem, the selection of the proper alternative solution, and finally the implementation of the decision.

\- The support provided by DSSs may respond to the needs and the cognitive style of different decision makers, combining the preferences and the judgement of the every individual decision maker with the information derived by analytical decision models.

• The time and the cost of the whole decision process is significantly reduced. Through the use of DSSs, the decision maker can easily handle (storing, retrieval, update, etc.) a large volume of information and data concerning the problem under consideration. Furthermore, DSSs provide the means to analyse this information using sophisticated techniques and methods.

\- The support that is provided by DSSs responds to the needs of various managerial levels, ranging from top managers and executives down to staff managers.

Although DSSs proved to be an effective tool for every decision maker who wants to improve the quality and the effectiveness of his decisions, their application reveals several possible problems. The main problems can be summarized as follows $[17,30]$ .

\- The operation of every DSS is governed by specific assumptions. In cases where the decision maker is not familiar with these assumptions, then the use of a DSS may lead to incorrect conclusions and estimations.

\- The judgement and the interpretation of the derived results of a DSS is made by the decision makers, assuming that they have the necessary theoretical knowledge to understand the assumptions of the system, and to interpret the derived results in a most appropriate manner [60].

\- Many DSSs are not compatible with each other, forcing decision makers to retype data, making unnecessary effort which leads to a significant loss of time. Problems also arise from the lack of compatibility of several DSSs with existing databases and computer networks.

\- The basic features of DSSs need to be standardized so that they can be used by more decision makers, at the same time taking into account the preferences of each separate decision maker.

\- Finally, it should be noted that many of the DSSs which have been designed in the past are based only on the examination of quantitative criteria, such as financial ratios, which can hardly represent all the significant information affecting the overall operation of a firm (management, organization, market position, technical structure, etc.).

Apart from the DSS approach, another significant application of computer science in decision making is the ES. This is a relatively new approach in supporting decision makers to take decisions effectively in complex and ill-structured problem domains. The ES technology originated in techniques from the field of artificial intelligence, aiming to develop computer information systems which represent and exploit the knowledge of human experts on a specific problem domain, to draw conclusions and provide decision makers with recommendations. Thus, an ES can be defined as a computer program that represents the knowledge and inference procedures of an expert to solve complicated problems, providing possible solutions or recommendations [30]. The main characteristic and basic goal of an ES is its ability to simulate human logic and reasoning, to draw conclusions and to provide corresponding explanations concerning these conclusions.

As well as mathematical computations, the financial decision-making process involves judgemental procedures that the decision maker has to follow in order to take the proper decisions. ES technology is well adapted to this kind of task, and therefore has attracted the interest of many researchers in the financial management field.

Many essays can be found in the international literature concerning the implementation of ES technology in the financial management field. Some of the most significant essays concerning the implementation of ESs in several fields of financial management, such as portfolio management, accounting, assessment of bankruptcy risk, credit granting, financial analysis, investments and financial marketing, are mentioned below:

• portfolio management [54,66,78,79,81];

• accounting [7,12,20,48,77];

• assessment of bankruptcy risk [11,47,49];

\- credit granting [2,8,35,52,67];

• financial analysis [5,43,50,65];

• investments [26,51,85];

• financial marketing [3,29,42,45].

A comprehensive bibliography of the applications of ES technology in several business areas, including finance, from 1975 through 1989, can be found in [16], while O'Leary [53] reports the contribution of artificial intelligence techniques in the fields of accounting, finance and management.

It is clear that researchers in the financial management field have already tried to exploit ES technology, to represent the knowledge of human experts in order to provide recommendations, and to support the decision-making process. The major part of past work concerning the implementation of ESs in the assessment of corporate performance and viability focused on the acquisition of domain knowledge either from the experts or through the application of several inductive methods, and the representation of this knowledge in the ES using production rules, networks or frames.

The benefits of ES technology can be summarized as follows [30,82].

\- ESs operate and draw estimations and conclusions using the knowledge and experience of human experts. Furthermore, the explanation capability of ESs can help the decision maker to understand better the operation of the system and its assumptions, as well as the inference that the system follows to draw certain conclusions.

\- ESs draw conclusion much faster than humans, especially in complex problem domains where a large volume of information and data should be processed and analysed.

\- ESs provide the means to handle incomplete information and uncertainty. Uncertainty is a common problem that all decision makers face. The ES technology can provide estimations and conclusions in cases where all the necessary information is not available, although these conclusions may not be certain.

\- ES estimations are consistent. Unlike humans, an ES consistently examines and analyses all the available information and data in detail, without overlooking facts or possible solutions.

\- Through the use of ESs, the transfer of knowledge is achieved. ESs can be used by non-experts to solve complex decision problems, using the knowledge of experts in the problem domain under consideration. Therefore, through the continuous use of ESs a non-expert can learn the procedure, the heuristics, and the problem-solving methodology, in general, that an expert would use to solve a specific problem.

Although ESs can be very useful, providing expert advice as a human expert would, and explaining their reasoning and conclusions, they have some limitations and problems [30,55,56,82]:

\- One of the major bottlenecks in the ES development process is the elicitation of the experts' knowledge of the problem [1]. Human reasoning is often too complicated to be adequately represented in an ES. Complete representation of the domain knowledge may require numerous production rules. Therefore, the time needed to draw conclusions increases considerably.

\- Beyond the problems encountered in the knowledge acquisition and representation process, it should also be noted that the knowledge depends on the expert. Therefore, a different human expert could provide different knowledge, new heuristics and new solutions strategies.

\- An ES represents shallow knowledge [30]. The advantage of using shallow knowledge is that the ES will behave in a similar way to an expert. The basic disadvantage is that shallow knowledge concerns special-purpose methods which are suitable only in specific and narrowly defined problem domains. Thus, although ESs achieve high performance in a few narrow tasks, they are helpless elsewhere.

\- Users of ESs have natural cognitive limits. Humans often see only what they are prepared to see, ignoring other important information. The fact that the ES always has control of the inference process often causes misunderstandings of its role and of its aim. Thus, ESs are sometimes considered as a tool which replaces the decision maker in making decisions, rather than a tool to support the decision-making process.

\- Many ESs which have been designed in the past perform an incomplete risk analysis. They analyse the performance of the company only from its financial characteristics, and they do not take into account qualitative information concerning the commercial, managerial and production reality of the company. Even if this is not the case, they do not take into account the non-deterministic character of the assessment [55,56].

Several studies have tried to compare DSSs with ESs. Ford [18] explored the similarities and differences between DSSs and ESs, concerning their objectives and intents, their operational differences, their users, and their development methodology. He reached the following conclusions. As far as the objectives and intents are concerned, although the fundamental goal of DSSs and ESs is basically the same (the improvement of the quality of decisions), their underlying philosophies and objectives differ.

From the operational point of view, DSSs allow the user to confront a decision problem in a personal manner, providing the ability to manipulate data and models in different ways. On the other hand, ESs provide little flexibility in the way the decision problem is analysed. As far as the users are concerned, Ford argues that DSSs are primarily applied in the business or organizational fields, while ESs are typically associated with scientific research. The users of DSSs are involved in the development of the system, while the users of ESs do not participate in the development process. Finally, concerning their development methodology, both DSSs and ESs are designed through an iterative or prototyping approach.

Doukidis [9] carried out a survey of 67 ESs to investigate whether they employ DSS concepts. The survey was based on a questionnaire model composed of a list of key concepts of DSSs, such as their role, their design features, their components, and the phases of the decision they support. The results of this survey show that three fundamental issues of DSSs are employed in ESs: semi-structured tasks, support and effectiveness. The main differences concern the boundary of the problem space and the way that the problem is solved. Henderson [25] investigated the existence of synergy between DSS and ES research. He concluded that in many respects the similarities between these areas appear to dominate the differences. Finally, a critical review of DSSs and ESs can be found in [30].

## 3. KBDSSs

The review presented in the preceding section clearly shows that the implementation of DSSs and ESs in financial management significantly improves the financial decision-making process. However, some limitations and problems concerning the application of DSSs and ESs in financial management still exist.

To overcome these problems and to provide as complete support as possible to decision makers, a new type of intelligent system called a KBDSS [24,30] has recently been proposed. A KBDSS can be defined as a computer information system that provides information and methodological knowledge using analytical decision models, and providing access to data and knowledge bases to support decision makers in making decisions effectively in complex and ill-structured problem domains [30]. Therefore, the basic idea which characterizes and underlies the conceptual framework of KBDSSs is the combination of the capabilities provided by the classical DSS approach, such as access to data and information, and application of analytical decision models, with the reasoning and explanation capabilities provided by ES technology.

Turban and Watkins [83] describe the benefits of integrating ESs with DSSs, in terms of the possible contribution of these two types of systems to an integrated KBDSS. The benefits of this integration concern the database and its management, the model base and its management, the user interface, and the overall system capabilities. As far as the database and database management (DBMS) are concerned, DSSs provide database capabilities to ESs, while on the other hand ESs improve the construction, operation and capabilities of DBMSs, as well as the accessibility to large databases. Concerning the model base and the model base management system (MBMS), DSSs provide an initial problem structure through standard models and computations, and also provide data to models, and storage of models developed by the decision makers in the model base. The use of ESs improves the model base management, assists the generation of alternatives, provides support in selecting the appropriate models according to the available data, supports the structuring of the problem analysis process, helps the interpretation of the results of the models, guides the decision maker through the basic assumptions underlying the application of these models, and finally improves the sensitivity analysis and trial-and-error processes. The contribution of DSSs to the design of user-friendly interfaces mainly focuses on the incorporation of the appropriate presentation means which match the requirements of the decision maker. On the other hand, ESs provide explanations concerning the use of the system, communication with the decision maker using natural language, interactivity in the problem-solving process, and tutoring capabilities. Finally, concerning the overall system capabilities, DSSs help the decision maker to gain experience in data collection, as well as in the implementation of several scientific decision models, and they also incorporate the preferences and decision policy of the decision maker in the decision-making process. ESs using the knowledge and experience of experts can provide intelligent advice as well as explanations concerning their estimations and conclusions.

In this new methodological framework of KBDSSs, using the capabilities offered by multicriteria decision aid (MCDA) methods $[6,40,41,61,62]$ leads to the introduction of the term multicriteria knowledge-based decision support systems (MKBDSSs). MKBDSSs are well adapted to the decision-making process in complicated and ill-structured problems, where no algorithmic optimal solution can be found. The integration of an ES with multicriteria, multivariate statistical, or mathematical programming methods $[46]$ offers to decision makers the greatest possible support that could be provided throughout the decision-making process.

Recently, KBDSSs have been proposed in several fields of financial management, such as the ISPMS (Intelligent Stock Portfolio Management System) [33] and the PMIDSS (Portfolio Management Intelligent Decision Support System) [34] for portfolio selection and management; the LASS (Lending Analysis Support System) [10], the CGX system [63,75,76], and the CREDEX (CREDit EXpert) system [55,56] for credit granting problems; and the FINEVA (FINancial EVALuation) system [91,92] and the KABAL system [21,22] for financial analysis.

A brief presentation of the capabilities, the characteristics, and the operation of these systems follows.

## 3.1. The ISPMS

Lee et al. [33] developed an intelligent portfolio management system called ISPMS, which integrates quantitative optimization models with the capabilities of an ES. The system uses the quadratic programming model proposed by Markowitz [39] to provide normative decisions, and an ES to analyse the preferences of the decision maker and the expert knowledge. Therefore, the final recommendations of the system are not just based on the subjective knowledge of an expert, but they also take into account the preferences and the investment policy of the decision maker. Furthermore, the ES helps the decision maker to formulate his/her preferences as constraints in the quadratic programming model. Thus, the role of the ES is not to replace the decision maker, but to support him. The architecture of the proposed system is presented in Fig. 1.

![](/api/attachments/UG9HFG6U/fulltext/images/f1e37066fc34ae2d7eec01ebad08336ec366a51c208b6b2a89bef2714c9addac.jpg)  
Fig. 1. Architecture of the ISPMS (source: [33]).

The key components of the ISPMS are the following:

(i) There are two independent external relational databases. The first database provides information about individual stocks (stock prices, industrial sector, beta values, firms' ratios, past years' financial results, etc.). The second database concerns historical instances of investment decisions which may be updated to reflect new investments.

(ii) The knowledge base of the system is constructed based on both the historical database (through machine-learning techniques [58]), and the advice of an expert in stock investment (through the knowledge-acquisition system).

(iii) The preference-revelation system is used to capture the personal preferences of the investor. These preferences may involve the desired investment amount and/or the percentage of a specific stock (or a group of stocks) in the constructed portfolio, which are not included in the expert knowledge. For example, the following rule implies that the investor would like to invest at least \$10.000 in company XYZ, and that the amount invested in this firm should be at least 10% of the total invested amount:

$$
\begin{array}{l l} \text {IF} & \text {Company = XYZ} \\ \text {THEN} & \text {AMOUNT\geq 10.000} \\ \text {AND} & \text {PERCENTAGE\geq 0.1} \end{array}
$$

The possible conflicts between the preferences of the investor and the expert knowledge are resolved by a priori revelation and/or by interactive revelation. In the a priori revelation a parameter is defined for the preference base or for every separate preference rule, to determine if the conflicting expert knowledge should be overridden or not. According to the interactive revelation, the investor's preference is revealed whenever he disagrees with the expert's opinion.

(iv) Using an interpreter, the qualitative factors in the knowledge and preference base are associated with the quadratic programming model, by interpreting them as decision variables or additional constraints. For example, consider the rule:

$$
\begin{array}{l l} \text {IF} & \text {Company = C_{1}} \\ \text {OR} & \text {Company = C_{2}} \\ \text {THEN} & \text {AMOUNT\leq 100.000} \\ \text {AND} & \text {PERCENTAGE = 0.1} \end{array}
$$

From this rule, the following two constraints are derived:

$$
\begin{array}{l} M (x _ {1} + x _ {2}) \leq 1 0 0. 0 0 0 \\ x _ {1} + x _ {2} = 0. 1 \end{array}
$$

where M is the total invested amount, and $x_{1}$ and $x_{2}$ are the portions of the total invested amount which are invested in companies $C_{1}$ and $C_{2}$ respectively.

The integration of expert knowledge, personal preference, quadratic programming and machine learning constitutes the major advantage of the ISPMS system. This integrated architecture and concept of the ISPMS system could also be applied in the selection of bonds, personnel, and other complex multiple-criteria decision-making problems. Furthermore, it is worth noting that the development of the ISPMS system was achieved with the cooperation of a leading investment company in Korea.

## 3.2. The PMIDSS

Lee and Stohr [34] developed a prototype intelligent decision support system, PMIDSS, for portfolio management decision making. The prototype uses a mixed knowledge representation scheme: production rules, directed networks, and frames to achieve greater flexibility and efficiency. In PMIDSS, domain knowledge is divided into four different layers: general economy and stock market, industries, companies, and selected stocks. The knowledge (expertise) in each layer is used to forecast the stock market, to match the current economic situation to prototypic ones in the system, and finally to select the most promising stocks (Table 1).

The system initially determines general trends in the economy and stock market and analyses the observed data to forecast future movements in the stock market. This step uses question nets (a net with nodes representing questions to the decision maker and arcs representing the answers of the decision maker) for observation and a directed network representation, which is called an expectation derivation net, for analysis. In the second step, a collection of frames is used to select scenarios fitting the economic conditions. During the third step, a set of production rules uses the output of the expectation derivation net and the frames to determine if the situation is favourable for common stock investment. Once the problem context has been determined, the system formulates investor's objectives by using question nets (step four). In the fifth step, a directed network of frames is used to select a set of promising stocks. Finally, with a set of promising stocks selected, a management-science model (mean-variance analysis) is used to determine an optimal portfolio of stocks.

From this brief description of the PMIDSS system, it is clear that the development of this system mainly focused on the organization and representation of knowledge, aiming at structuring the appropriate decision-making process in portfolio selection and management problems. A future step would be the practical implementation of this representation scheme in real-world problems.

## 3.3. The LASS

The LASS was developed by Duchessi and Belardo [10] for commercial loan analysis problems.

The aim of the system is to structure the commercial loan analysis process, proposing the proper models which should be used and the analyses that the decision maker should take, according to the available data. Additionally, the system takes into account the applicability of several analytical models and techniques. Thus, the system provides guidance throughout the decision process, interpreting the derived results, and proposing the appropriate further steps that the decision maker should take.

The structuring of the analysis process is carried out through the knowledge base of the system. This knowledge base includes knowledge concerning the problem domain (i.e. commercial loan analysis) and the available data, the structuring of an analysis in this problem domain, and the financial modelling techniques that constitute the solution procedures. These three parts of the knowledge base are structured in a hierarchy from the most abstract concepts to the most specific concepts. The most abstract concepts define the problem domain and are related to several categories of loan analyses, such as commercial loan analysis, real estate loan analysis, personal loan analysis, etc. The more specific concepts provide the means to focus on specific areas of the loan analysis, such as capacity, collateral and capital. Each of these are further defined by more detailed structural elements. For example, capital analysis involves the analysis of the financial structure, profitability analysis and assets analysis.

The knowledge is represented in the knowledge base of the system through the combination of a semantic network with production rules. The semantic network provides a graphical representation of several concepts and objects, which are related to the loan analysis, as well as the relations among them (Fig. 2). The nodes of the network represent different concepts, while the links represent the relation of the concepts. For example, a relationship called “a kind of” (AKO) is used to represent knowledge such as “commercial loan analysis is a kind of loan analysis”. Combining a set of link types such as “a component of” (ACO), “determines” (D) and “modelled by” (MB), it is possible to represent more complicated knowledge, such as “profitability analysis is a component of capital analysis and it is modelled by return on investment and return on equity”.

Correspondence of problem-solving steps and knowledge-representation schemes in the PMIDSS (source: [34])

<table><tr><td>Domain</td><td>Problem-solving phase</td><td>Knowledge-representation scheme</td></tr><tr><td rowspan="4">Investment timing</td><td rowspan="4">Forecast stock market and match current situation with prototypes</td><td>Question nets</td></tr><tr><td>Networks</td></tr><tr><td>Frames</td></tr><tr><td>Production rules</td></tr><tr><td rowspan="3">Stock selection</td><td rowspan="3">Select stocks from a candidate set</td><td>Question nets</td></tr><tr><td>Network of frames</td></tr><tr><td>Production rules</td></tr></table>

The use of the semantic network is combined with the use of production rules. The production rules provide the means for moving across the several parts of the network, according to the available data and problem conditions. An example of a production rule of the LASS system is the following:

IF earnings are stable

AND revenue is increasing

THEN calculate a trend for gross margin and examine market conditions.

Through a powerful user interface, it is possible to move from the knowledge base to the model base which includes several analysis techniques. Through the user interface, it is also possible to transfer the results derived by the analytical decision models back in the knowledge base. The results are evaluated through the knowledge base and thus new analyses may be proposed (the interpretation of the obtained results is achieved). More specifically, the LASS performs the analysis of commercial loans in the following four phases:

1. Initially, the system attempts to collect information about the problem and the available data for subsequent analyses.

2. Next, the system begins to construct the analysis process according to the relationships represented in its knowledge base.

3. During the third phase, the actual analysis is performed for the loan officer, either automatically by the system or suggesting available models.

4. Finally, during the fourth phase of the process, the system activates other analysis, according to the results of the most recent analysis and the logical problem structuring provided by the results.

![](/api/attachments/UG9HFG6U/fulltext/images/5f43040bd13631c7611571113ba5398587ed8322b4badd5a036a172005d0807f.jpg)  
Fig. 2. Partial network representation of the LASS (source: [10]).

The LASS has been developed in a prototype form (it has not been commercially used yet), concerning only commercial loan analysis problems. Therefore, more rules could be included in its knowledge base to evaluate all kinds of loan applications and new more sophisticated models should be added in its model base to perform a complete loan analysis.

## 3.4. The CGX system

The CGX system [76] is a multicriteria intelligent decision support system for credit-granting problems. The credit-granting decision process is modelled through the multicriteria method AHP (analytic hierarchy process) [64,86], as a three-level hierarchical problem with the ultimate objective being one of deriving the perceived probabilities of default and payment of the loan (Fig. 3).

The first level of the process includes the goal of the credit-granting problem, which is the maximization of shareholders' wealth, the second level includes the evaluation criteria, and the third level includes the objectives (granting or denying a loan). It is important to note that the evaluation criteria include both financial ratios (debt capacity ratios, profitability ratios, liquidity ratios, etc.), as well as qualitative criteria (customer background, pay record, geographical location, business potential, etc.). Integrating the local weights of the final level with the appropriate global weights from the criterion level will yield a final set of weights for granting and denying credit. The weights for granting and denying credit are then integrated with the expected cash flows associated with the two outcomes, to determine the amount of loan to grant.

The input to the AHP involves relative comparison data in a pair-wise fashion for each level with respect to each of the elements in a preceding level of the hierarchy. The first level does not require any comparisons, since it contains only one element. In the second level, the decision maker has to compare the elements in a pair-wise fashion with respect to the element of the first level (the maximization of shareholders' wealth). In the third level, the two elements (granting and denying the credit) should be compared with respect to all the elements from the criteria level (level 2). This is a rather complicated and time-consuming task to be carried out by the decision maker, because each criterion includes a number of subcriteria and thus the number of comparisons is too large. An ES is included to support the decision maker in comparing the elements (objectives) of the final level with respect to the elements of the criteria level. Therefore, in this case the ES is used to draw partial conclusions which are aggregated through the AHP to draw the final estimations of the system. In this way, the combination of the personal preferences of the decision maker with the expert's knowledge is achieved. Furthermore, the combination of the ES with the AHP guides the analysis process, preventing the misinterpretation of the results by the decision maker and the overlooking of the basic assumptions of the system.

![](/api/attachments/UG9HFG6U/fulltext/images/96704bd1c7d87ca707175c419444e66b7240191484e03f284f14b9a36db7437c.jpg)  
Fig. 3. Modelling of the credit-granting process using the multicriteria AHP method (source: [76]).

The necessary information concerning each evaluation criterion (customer background, pay record, location, business potential, financial soundness, and the subcriteria), is included in a relational database, with valuable information concerning industry standards. The knowledge base of the system contains rules for the evaluation of each customer along with the evaluation criteria, using the information contained in the database of the system. The result of each rule is associated with an intensity value on the AHP measurement scale $[86]$ (e.g. the result “excellent” is associated with an intensity value of 9 on the AHP measurement scale).

The combination of the ES estimations with the multicriteria method AHP leads to a set of weights for denying and granting credit (possibilities of payment and default). These weights are integrated with the expected cash-flows associated with the granting and denying of credit, to compute the net present value (NPV). If the NPV is positive then the credit is granted, otherwise the credit is denied. The system also provides recommendations concerning the maximum amount of credit that should be granted.

Although the system offers suggestions regarding the granting or the rejection of a specific credit, it does not provide information about the competitive level between several credit applications (e.g. the credit applications are not compared to determine which one is the best to grant and which is the most risky). The CGX system has attracted the interest of many Fortune 500 corporations.

## 3.5. The CREDEX system

The CREDEX system [55,56] demonstrates the feasibility of a multi-expert approach driven by a meta-model in the assessment of credit risk. The system, using quantitative (economic and financial) and qualitative (social) data concerning the examined company and its business sector, as well as the bank's lending policy, provides a diagnosis of the company's functions (commercial, financial, managerial and industrial) in terms of weaknesses and strengths. The system integrates simple heuristics (surface knowledge), used by the experts when judging the acceptance or the rejection of a loan application, with a deeper understanding of the information aggregation process (deep knowledge), which is based on multi-attribute models. Fig. 4 presents the architecture of the CREDEX system.

In CREDEX, the level of risk associated with each loan application is determined through a multi-attribute aggregation process. Each function (subdomain) of the examined company is associated with a weight, which is defined either interactively by the decision maker or calculated as functions of the banking policy, the sector of activity, and the goal of the assessment. The characteristics of each function are associated with weights measuring the importance of these characteristics in assessing the quality of the corresponding function. The assessment of these characteristics leads to the determination of the elementary risks, which are aggregated, taking into account their importance, to obtain the partial assessments. Finally, the global assessment is achieved through the aggregation of the partial assessments.

![](/api/attachments/UG9HFG6U/fulltext/images/d17adb19120e3ea6f0d580943ffa41d431b9a3a99a17d5465e36498601dff9e2.jpg)  
Fig. 4. The architecture of the CREDEX system (source: [55,56]).

The integration of the experiential knowledge (representing shallow knowledge) with the deep knowledge concerning the multi-attribute aggregation process is controlled at a higher level by a meta-expert. The experiential knowledge is achieved through experiential experts which deduce the importance of the subdomain characteristics and provide an initial evaluation of the subdomain. A deeper analysis is carried out by the judgemental experts which combines the elementary risks with their importance to assess the partial risks. The meta-expert (meta-model) is responsible for determining which expert should be activated. A separate knowledge corresponds to each type of expert.

The CREDEX system demonstrates how the combination of an ES with simple multi-attribute models could help decision makers to structure the creditgranting problem using both qualitative and quantitative criteria, taking into account the knowledge of an expert credit analyst and the preferences of the decision maker as well. The ES is used to support the decision makers in determining the importance of each characteristic of a firm, and using simple multi-attribute models the final estimations of the system are derived. Furthermore, the use of a meta-expert for controlling the analysis process provides the capability of structuring the decision process according to the available data and the operating assumptions of the system. Thus, the possible misinterpretation of the derived results is prevented. Although the proposed structure of the CREDEX system seems to be very effective for the development of a powerful tool for credit-granting problems, it is mainly associated with the theoretical point of view, and it has not yet been applied in real-world problems to test its performance and efficiency.

## 3.6. The KABAL system

Hartvigsen [21] presented the KABAL knowledge-based system (“kabal” is the Norwegian word for patience) for financial analysis in the trade and industry portfolio in Norwegian savings banks (the system was developed with the cooperation of a Norwegian bank which uses it for the evaluation of firms’ performance). The KABAL system includes analysis of financial statements, guarantees, markets, and company management and organization. Fig. 5 gives an overview of the structure of the KABAL system, its different modules, and their relationships.

![](/api/attachments/UG9HFG6U/fulltext/images/b5ed4fd374d3bd1d17dc79f96a0a22ec3dd229dbbbc25e0925b343f6c1ae3fc4.jpg)  
Fig. 5. Structure of the KABAL system (source: [21]).

The heart of the KABAL system is its knowledge base. It contains knowledge concerning the analysis of financial statements. This analysis is accomplished through the examination of the companies' profitability, solidity, liquidity and financial structure. Each one of these four categories is further divided into more specific subcategories, which are evaluated across one or more financial ratios.

Table 2 presents an example of the analysis that the KABAL system performs, concerning the profitability of a firm.

The system also examines some external factors, such as inflation, the rate of interest on deposits, the bank overdraft, the average risk, and the average gross income of the branch that the firm belongs to.

In the development of the KABAL system, protocol analysis was used as the main acquisition technique to acquire knowledge from the expert financial analysts of a Norwegian bank. Protocol analysis is recursive and concurrent. In recursive protocol sessions the financial analyst is asked to look at previous cases of loan control, while in concurrent protocol sessions the analyst is asked to analyse a complex case expressing his actions until his final decision.

The basic characteristic of the KABAL system is the combination of both quantitative and qualitative criteria (market, management and organization) in the analysis of corporate performance. The system provides several tools for handling qualitative information, such as questionnaires and checklists. The knowledge base of the system evaluates the financial status of the firms, while the evaluation of the qualitative information concerning the operation of the firm is made by the decision maker with the assistance of questionnaires and checklists. A possible future direction in the development of the KABAL system could be the incorporation of another knowledge base to analyse the non-financial elements. Furthermore, the system does not distinguish companies according to their business sector. The business sector in which a firm belongs affects the assessment of its performance and therefore it should be examined during the evaluation process.

## 3.7. The FINEVA system

The FINEVA system [91,92] is a multicriteria KBDSS for the assessment of corporate performance and viability. The basic characteristic of the FINEVA system is the combination of an ES with a multivariate statistical method (principal components analysis) and a multicriteria method, to estimate the corporate performance and the viability of firms. The basic parts of the FINEVA system and the way they interact are illustrated in Fig. 6. A brief presentation of the system follows (a detailed description can be found in [44,91,92]).

<table><tr><td colspan="4">Profitability</td></tr><tr><td colspan="4">The company&#x27;s profitability, i.e. the operational performance of the company, is set to be relatively bad.</td></tr><tr><td></td><td>1980</td><td>1981</td><td>1982</td></tr><tr><td>Return on investment</td><td>27.78</td><td>22.49</td><td>15.58</td></tr><tr><td>Return on equity</td><td>15.72</td><td>10.15</td><td>5.52</td></tr><tr><td>Gross income</td><td>46.15</td><td>46.67</td><td>47.14</td></tr><tr><td rowspan="35" colspan="3">The reasons for the reduction of the return on investment are that the operation costs increase by costs of goods sold increase by wage bill increases by other operating costs increase by depreciation increases by total current assets increase by inventory semi and finished products increase by accounts receivable increase by The reasons for the reduction of the return on equity are that the total operating costs increase by total financial costs increase by average equity costs increase by The reasons for the growth of the gross income are that the interest charges increase by</td><td rowspan="35">5%3%6%9%20%51%62%40%</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr></table>

The database of the system includes all the necessary financial information for the computation of financial ratios and some additional qualitative information important to examine some aspects of a firm which cannot be assessed using financial ratios (quality of management, organization, market position, technical structure, etc.).

The ES part represents the methodology used by human experts in the field of financial analysis and it is used to provide an initial evaluation of firms, based on the examination of some financial ratios and qualitative criteria $[44]$ . Principal components analysis $[32,80]$ can be used by the decision maker to identify the most significant financial ratios and the behaviour of the firms.

The UTASTAR multicriteria method [71], an improved variant of the UTA method [27,69,70], ranks the firms from the most dynamic to the most bankrupt, or sorts them in classes of risk [87,88], and indicates the competitive level of firms. It also provides the relative importance of each criterion in the firms' ranking. In the case of corporate assessment, once the decision maker has expressed his judgement in the form of a ranking of the firms according to classes of risk (sometimes with the help of the ES results), the system, using the ordinal regression method UTASTAR, optimally estimates the multicriteria additive utility functions which are as consistent as possible with the decision maker's ranking. The mathematical expression of the additive utility function is given by the following equation:

$$
u (g) = p _ {1} u _ {1} \left(g _ {1}\right) + p _ {2} u _ {2} \left(g _ {2}\right) + \dots + p _ {n} u _ {n} \left(g _ {n}\right)
$$

where $g = (g_{1}, g_{2}, \ldots, g_{n})$ is the vector of the firm's performance; $u_{1}(g_{1}), u_{2}(g_{2}), \ldots, u_{n}(g_{n})$ are the estimated marginal utilities normalized between 0 and 1; $p_{1}, p_{2}, \ldots, p_{n}$ are the relative weights of utility $u_{i}(g_{i})$ associated to criterion $g_{i}$ ; and $u(g)$ is the global utility of g. A significant feature of this multicriteria method is that, besides the use of quantitative criteria (financial ratios), it also allows the use of qualitative criteria which examine some aspects of the firm that cannot be measured using quantitative techniques, such as the financial ratios.

![](/api/attachments/UG9HFG6U/fulltext/images/44969bade4ab92e474e56259e27d5de09c84679b6a9dc7bc6f8b2509822e3ee9.jpg)  
Fig. 6. Structure of the FINEVA system (source: [91,92]).

The estimation model derived by the UTASTAR multicriteria method is used as basic knowledge in the ES part (as a production rule based on the ranking or segmentation model) for the evaluation of new firms which are inserted in the database of the system. The navigation of the system through an application is presented in $[91,92]$ . The FINEVA system has already been applied in the assessment of corporate failure risk $[89]$ , and it has attracted the interest of a leading Greek commercial bank.

The combination of an ES with a multivariate statistical method and a multicriteria method is the basic characteristic of the system. Through the integration of these three parts, the preferences of the decision makers as well as the experts' knowledge are taken into account. The aim of the ES is not to replace the decision maker. Its role is supportive, providing an expert's estimation of the performance and the viability of the firms. The decision maker can incorporate this expert estimation in the UTAS-TAR model, to have the final recommendations of the system. A future development perspective of the system could be the incorporation in the system of knowledge concerning the business sector in which the firms belong. As mentioned in the description of the KABAL system, this is an important factor which should not be overlooked.

## 4. Concluding remarks and perspectives

Decision making in several fields related to financial management is often a very complicated and ill-structured task involving the exploitation and evaluation of various information, data, and alternative solutions or actions. Managers and individual financial decision makers (portfolio managers, financial analysts, credit managers, investors, etc.) face such problems on a daily basis and the existence of a tool which is able to support them in making the appropriate decisions is considered to be of vital importance.

The previous work considering this problem focused mainly in two separate approaches: DSSs and ESs. This paper presented past work concerning the implementation of both these approaches in several fields of financial management, described the existing problems, and illustrated the application and the new possibilities offered by the combination of ES technology with DSSs.

The new possibilities and perspectives offered by KBDSSs, as well as their contribution to the qualitative improvement of the decision-making process, especially in the financial management field, can be summarized by the following three main aspects.

\- Understanding the operation and the results of the system: incorporating a knowledge base in a DSS can help the decision makers to understand the results of the mathematical models. The knowledge base provides the necessary explanations concerning the reasoning process of the system, its basic assumptions, and its operation. Thus, the methodology used by the system can be clearly presented to the decision makers, helping them to learn the decision analysis process of the problem under consideration. At the same time, interpretation of the results is achieved, avoiding their misunderstanding and misinterpretation. The quantitative results are transformed to qualitative explanations, which are easier to understand, and are often of greater significance to the decision makers.

\- The objectiveness and the completeness of the results are ensured: the combination of the ES results with those derived from mathematical models and analytical techniques increases the objectiveness of the final results. The subjective results of the ES (which depend on the expert's knowledge) are not the final estimations of the system. Apart from the expert's knowledge, represented by the ES results, the decision maker is also provided with results derived from mathematical models from the fields of multicriteria analysis, multivariate statistical analysis and mathematical programming. The results of this combination correspond not only to the expert's opinion, but also to the preferences and the policy of the decision maker.

\- The structuring of the proper decision analysis is achieved: the usefulness and the suitability of decision analysis techniques often vary, depending on the available data of the examined decision problem. According to the existing data, the use of a certain analysis or a mathematical model may be unnecessary or even inappropriate and, consequently, the decision maker could be directed to incorrect estimations and conclusions. The knowledge concerning the problem domain represented in a knowledge base can be used to face such problems, recommending the decision analysis process and the appropriate analytical models, which correspond to the available data. Thus, the structure of the decision analysis is achieved, ensuring the effectiveness, the applicability and the validity of the decision analysis models and techniques.

As new technological advances in the fields of multicriteria decision making and artificial intelligence (e.g. neural nets $[4,84]$ ) are achieved, embedding them in the existing framework of KBDSSs could considerably increase the effectiveness of the provided decision support.

## References

[1] A. Barr and E. Feigenbaum, The Handbook of Artificial Intelligence, Vol. II (Pittman Books, 1982).

[2] A. Ben-David and L. Sterling, A Prototype Expert System for Credit Evaluation, In: L.F. Pau, Ed., Artificial Intelligence in Economics and Management (Elsevier Science, 1986) 121–128.

[3] O.J. Borch and G. Hartvigsen, Knowledge-Based Systems for Strategic Market Planning in Small Firms, Decision Support Systems 7 (1991) 145–157.

[4] J.E. Boritz and D.B. Kennedy, Effectiveness of Neural Network Types for Prediction of Business Failure, Expert Systems With Applications: An International Journal 9, No. 4 (1995) 503–512.

[5] M.J. Bouwman, Human Diagnostic Reasoning by Computer: An Illustration from Financial Analysis, Management Science 29, No. 6 (1983) 653–672.

[6] J.P. Brans, Ph. Vincke and B. Mareschal, How to Select and How to Rank Projects: The PROMETHEE Method, European Journal of Operational Research 24 (1986) 228–238.

[7] C.E. Brown and A. Wensley (Eds.), Special Issue on Expert Systems in Accounting, Auditing, and Finance, Expert Sys-

tems With Applications: An International Journal 9, No. 4 (1995) 433–608.

[8] T.P. Cronan, L.W. Glorfeld and L.G. Perry, Production System Development for Expert Systems Using a Recursive Partitioning Induction Approach: An Application to Mortgage, Commercial and Consumer Lending, Decision Sciences 22 (1991) 812–845.

[9] G.I. Doukidis, Decision Support System Concepts in Expert Systems: An Empirical Study, Decision Support Systems 4, (1988) 345–354.

[10] P. Duchessi and S. Belardo, Lending Analysis Support System (LASS): An Application of a Knowledge-Based System to Support Commercial Loan Analysis, IEEE Transactions on Systems, Man, and Cybernetics 17, No. 4 (1987) 608–616.

[11] P.J. Elmer and D.M. Borowski, An Expert System Approach to Financial Analysis: The Case of S and L Bankruptcy, Financial Management 17 (Autumn 1988) 66–76.

[12] R.K. Elliot and J.A. Kielich, Expert Systems for Accountants, Journal of Accountancy (September 1985) 126–134.

[13] H.B. Eom and S.M. Lee, Decision Support Systems Applications Research: A Bibliography (1971–1988), European Journal of Operational Research 46 (1990) 333–342.

[14] H.B. Eom, S.M. Lee, C.A. Snyder and F.N. Ford, A Multiple Criteria Decision Support System for Global Financial Planning, Journal of Management Information Systems 4, No. 3 (1987–1988) 94–113.

[15] S.B. Eom, S.M. Lee and J.K. Kim, The Intellectual Structure of Decision Support Systems (1971–1989), Decision Support Systems 10 (1993) 19–35.

[16] S.B. Eom, S.M. Lee and A. Ayaz, Expert Systems Applications Development Research in Business: A Selected Bibliography (1975–1989), European Journal of Operational Research 68 (1993) 278–290.

[17] M.C. Er, Decision Support Systems: A Summary, Problems, and Future Trends, Decision Support Systems 4 (1988) 355-363.

[18] F.N. Ford, Decision Support Systems and Expert Systems: A Comparison, Information and Management 8 (1985) 21–26.

[19] T.P. Gerrity Jr., Design of Man–Machine Decision Systems: An Application to Portfolio Management, Sloan Management Review 12 (1971) 59–75.

[20] J.V. Hansen and W.F. Messier Jr., A Knowledge-Based Expert System for Auditing Advanced Computer Systems, European Journal of Operational Research 26 (1986) 371–379.

[21] G. Hartvigsen, KABAL: A Knowledge-Based System for Financial Analysis in Banking, Expert Systems for Information Management 3, No. 3 (1990) 213–231.

[22] G. Hartvigsen, Limitations of Knowledge-Based Systems for Financial Analysis in Banking, Expert Systems with Applications: An International Journal 4 (1992) 19–32.

[23] R.L. Hayen, Applying Decision Support Systems to Small Business Financial Planning, Journal of Small Business Management (July 1982) 35–46.

[24] F. Hayes-Roth, Knowledge-Based Expert Systems, Computer 17, No. 10 (1984) 263–273.

[25] J.C. Henderson, Finding Synergy Between Decision Support Systems and Expert Systems Research, Decision Sciences 18 (1987) 333–349.

[26] S. Heuer, U. Koch and C. Cryer, INVEST: An Expert System for Financial Investments, IEEE Expert 3 (Summer 1988) 60–68.

[27] E. Jacquet-Lagrèze and Y. Siskos, Assessing a Set of Additive Utility Functions for Multicriteria Decision Making: The UTA Method, European Journal of Operational Research 10 (1982) 151–164.

[28] J. Jenkins, Computer Based Financial Planning, Omega: The International Journal of Management Science 1, No. 5 (1973) 539–550.

[29] J. Kastner, C. Apte, J. Giesmer, S.J. Hong, M. Karnaugh, E. Mays and Y. Tozawa, A Knowledge-Based Consultant for Financial Marketing, AI Magazine 7 (1986) 71–79.

[30] M. Klein and L.B. Methlie, Knowledge-Based Decision Support Systems with Applications in Business, 2nd edn. (Wiley, 1995).

[31] D. Langen, An (Interactive) Decision Support System for Bank Asset Liability Management, Decision Support Systems 5 (1989) 389–401.

[32] J. Lagarde, Initiation à l'Analyse des Données (Bordas, 1983).

[33] J.K. Lee, H.S. Kim and S.C. Chu, Intelligent Stock Portfolio Management System, Expert Systems 6, No. 2 (1989) 74–85.

[34] J.B. Lee and E.A. Stohr, Representing Knowledge for Portfolio Management Decision Making, Working Paper 101, Center for Research on Information Systems, New York University (September 1985).

[35] P. Lévine and J.-Ch. Pomerol, Knowledge Representation by Schemata in Financial Expert Systems, Theory and Decision 27 (1989) 147–161.

[36] B. Mareschal and J.P. Brans, BANKADVISER: An Industrial Evaluation System, European Journal of Operational Research 54 (1991) 318–324.

[37] B. Mareschal and J.P. Brans, BANKADVISER: Un Système Interactif Multicritère pour l'Evaluation Financière des Entreprises à l'Aide des Méthodes PROMETHEE, Revue d'Analyse Economique 69, No. 1 (1993) 191–205.

[38] B. Mareschal and D. Mertens, BANKS a Multicriteria, PROMETHEE-based Decision Support System for the Evaluation of the International Banking Sector, Revue des Systèmes de Décision 1, No. 2 (1992) 175–189.

[39] H. Markowitz, Portfolio Selection, Journal of Finance (March 1952) 77–91.

[40] J.M. Martel and N. Khoury, Une Alternative à l'Analyse Discriminante en Prévision de Faillite: Un Indice Multicritère, ASAC'94 (1994).

[41] R. Massaglia and A. Ostanello, N-TOMIC: A Support System for Multicriteria Segmentation Problems, In: P. Korhonen, Ed., International Workshop on Multicriteria Decision Support, Lecture Notes in Economics and Mathematics Systems 356 (Springer-Verlag, 1991) 167–174.

[42] N.F. Matsatsinis and Y. Siskos, MARKEX: An Intelligent

Decision Support System for Product Development Decisions, EURO XIV, Jerusalem (1995).

[43] N.F. Matsatsinis, A. Spiridakos and C. Zopounidis, Towards an Expert System for the Evaluation of the Financial Status of Small Firms, In: Y. Siskos, C. Zopounidis and K. Pappis, Eds., Management of Small Firms (Cretan University Editions, 1996) 101–109 (in Greek).

[44] N.F. Matsatsinis, M. Doumpos and C. Zopounidis, Knowledge Acquisition and Representation for Expert Systems in the Field of Financial Analysis, Expert Systems with Applications: An International Journal 12, No. 2 (1997) 247–262.

[45] E. Mays, C. Apte, J. Giesmer and J. Kastner, Organizing Knowledge in a Complex Financial Domain, IEEE Expert 2 (1987) 61–70.

[46] R.D. McBride and D.E. O'Leary, The Use of Mathematical Programming with Artificial Intelligence and Expert Systems, European Journal of Operational Research 70 (1993) 1–15.

[47] W.F. Messier and J.V. Hansen, Inducing Rules for Expert System Development: An Example Using Default and Bankruptcy Data, Management Science 34, No. 12 (1988) 1403–1415.

[48] R.H. Michaelsen, An Expert System for Tax Planning, Expert Systems 1 (1984) 149–167.

[49] M. Michalopoulos and C. Zopounidis, An Expert System for the Assessment of Bankruptcy risk, In: B. Papathanassiou and K. Paparrizos, Eds., Proceedings of 2nd Balkan Conference on Operational Research (1993) 151–163.

[50] G. Mui and W.E. McCarthy, FSA: Applying AI Techniques to the Familiarization Phase of Financial Decision Making, IEEE Expert (Fall 1987) 33–41.

[51] S.C. Myers, Notes on an Expert System for Capital Budgeting, Financial Management 17, No. 3 (1988) 23–31.

[52] E. Nikbakht and M.H.A. Tafti, Application of Expert Systems in Evaluation of Credit Card Borrowers. Managerial Finance 15, No. 5 (1989) 19–27.

[53] D.E. O'Leary, AI in Accounting, Finance and Management, International Journal of Intelligent Systems in Accounting, Finance and Management 4 (1995) 149–153.

[54] I. Pau and G. Giannoti, Technical Analysis of Future Markets (Prentice-Hall, 1986).

[55] S. Pinson, Credit Risk Assessment and Meta-Judgement, Theory and Decision 27 (1989) 117–133.

[56] S. Pinson, A Multi-Expert Architecture for Credit Risk Assessment: The CREDEX System, In: D.E. O'Leary and P.R. Watkins, Eds., Expert Systems in Finance (Elsevier Science, 1992) 37–64.

[57] J.C. Pomerol and L. Ibp, Multicriteria DSSs: State of the Art and Problems, Central European Journal for Operations Research and Economics 2, No. 3 (1993) 197–211.

[58] J.R. Quinlan, Learning Efficient Classification Procedures and Their Application to Chess and Games. In: R.S. Michalski, J.G. Carbonell and T.M. Mitchell, Eds., Machine Learning: An Artificial Intelligence Approach (Tioga, 1983) 463-482.

[59] F.J. Radermacher, Decision Support Systems: Scope and Potential, Decision Support Systems 12 (1994) 257–265.

[60] W.E. Remus and J.E. Kottemann, Toward Intelligent Decision Support Systems: An Artificially Intelligent Statistician, MIS Quarterly 10, No. 4 (1986) 403–418.

[61] B. Roy, A Multicriteria Analysis for Trichotomic Segmentation Problems, In: P. Nijkamp and J. Spronk, Eds., Operational Methods (Gower Press, 1981) 245–257.

[62] B. Roy and J. Moscarola, Procédure Automatique d'Examem de Dossiers Fondée sur une Segmentation Trichotomique en Présence de Critères Multiples, RAIRO Recherche Operationnele 11, No. 2 (1977) 145–173.

[63] B. Ruparel and V. Srinivasan, A Dedicated Shell for Designing Expert Credit Support Systems, Decision Support Systems 8 (1992) 343–359.

[64] T.L. Saaty, The Analytic Hierarchy Process (McGraw-Hill, 1980).

[65] J.A. Sena and L.M. Smith, A Sample Expert System for Financial Statement Analysis, Journal of Accounting and EDP 3 (Summer 1987) 15–22.

[66] B. Shane, M. Fry and R. Toro, The Design of an Investment Portfolio Selection Decision Support System Using Two Expert Systems and a Consulting System, Journal of Management Information Systems 3, No. 4 (1987) 79–92.

[67] M. Shaw and J.A. Gentry, Using an Expert System with Inductive Learning to Evaluate Business Loans, Financial Management 17 (Autumn 1988) 45–56.

[68] M.G. Singh and R. Cook, PRICE-STRAT: A Decision Support System for Determining Building Society and Bank Interest Rate Mixes, International Journal of Bank Marketing 4 (1986) 52–66.

[69] J. Siskos, Comment Modéliser les Préférences au Moyen de Fonctions d'Utilité Additives, RAIRO Recherche Opérationnele 14, No. 1 (1980) 53-82.

[70] J. Siskos, A. Spiridakos and D. Yannacopoulos, MINORA: A Multicriteria Decision Aiding System for Discrete Alternatives, Journal of Information Science and Technology 2, No. 2 (1993) 136–149.

[71] J. Siskos and D. Yannacopoulos, UTASTAR: An Ordinal Regression Method for Building Additive Value Functions, Investigação Operational 5, No. 1 (1985) 39–53.

[72] Y. Siskos, C. Zopounidis and A. Pouliezos. An Integrated DSS for Financing Firms by an Industrial Development Bank in Greece, Decision Support Systems 12 (1994) 151–168.

[73] R.H. Sprague Jr., Systems Support for a Financial Planning Model, Management Accounting 53 (1972) 29–34.

[74] R.H. Sprague Jr. and H.J. Watson, A Decision Support System for Banks, Omega 4, No. 6 (1976) 657–671.

[75] V. Srinivasan and Y.H. Kim, Designing Expert Financial Systems: A Case Study of Corporate Credit Management, Financial Management 17 (Autumn 1988) 32–44.

[76] V. Srinivasan and B. Ruparel, CGX: An Expert Support System for Credit Granting, European Journal of Operational Research 45 (1990) 293–308.

[77] P. Steinbart, The Construction of a Rule-Based System as a Method for Studying Materiality Judgements. Accounting Review 62 (1987) 97–116.

[78] J.M. Suret, E. Cormier and J. Roy, Un Système-Expert de Choix d'Actions, FINÉCO 1, No. 1 (1991) 39–60.

[79] C. Syriopoulos, G. Doukidis, G. Karakoulas, T. Liakopoulou and E. Skevophilax, An Advisor Expert System for Investments in Stock Market, Bulletin of Union of Greek Banks (3rd Quarter 1992) 78–83 (in Greek).

[80] B.G. Tabachnick and L.S. Fidell, Using Multivariate Statistics (Harper-Collins, 1989).

[81] K.Y. Tam, M.Y. Kiang and R.T.H. Chi, Inducing Stock Screening Rules for Portfolio Construction, Journal of the Operational Research Society 42, No. 9 (1991) 747–757.

[82] E. Turban, Decision Support and Expert Systems: Management Support Systems, 3rd edn. (Macmillan, 1993).

[83] E. Turban and P.R. Watkins, Integrating Expert Systems and Decision Support Systems, MIS Quarterly (June 1986) 121-136.

[84] R.L. Wilson and R. Sharda, Bankruptcy Prediction Using Neural Networks, Decision Support Systems 11 (1994) 545-557.

[85] J.L. Valentine, Applying Expert Systems to Investment, Financial Analysts Journal (November–December 1988) 48–53.

[86] F. Zahedi, The Analytic Hierarchy Process—A Survey of the Method and its Applications, Interfaces 16 (July–August 1986) 96–108.

[87] C. Zopounidis, A Multicriteria Decision-Making Methodology for the Evaluation of the Risk of Failure and an Application, Foundations of Control Engineering 12, No. 1 (1987) 45–64.

[88] C. Zopounidis, Evaluation du Risque de Défaillance de l'Entreprise: Méthodes et cas d'Application (Economica, 1995).

[89] C. Zopounidis, M. Doumpos and N.F. Matsatsinis, Application of the FINEVA Multicriteria Knowledge-Based Decision Support System to the Assessment of Corporate Failure Risk, Foundations of Computing and Decision Sciences 21(4) (1996) 233–251.

[90] C. Zopounidis, M. Godefroid and C. Hurson, Designing a Multicriteria Decision Support System for Portfolio Selection and Management, In: J. Janssen, C.H. Skiadas and C. Zopounidis, Eds., Advances in Stochastic Modelling and Data Analysis (Kluwer, 1995) 261–292.

[91] C. Zopounidis, N.F. Matsatsinis and M. Doumpos, FINEVA: A Multicriteria Knowledge-Based Decision Support System for the Assessment of Corporate Performance and Viability. In: E. Lopez Gonzalez, Ed., Proceedings of the International Conference on Intelligent Technologies in Human-Related Sciences, Vol. II (Leon, 1996) 175–182.

[92] C. Zopounidis, N.F. Matsatsinis and M. Doumpos, Developing a Multicriteria Knowledge-Based Decision Support System for the Assessment of Corporate Performance and Viability: The FINEVA System, Fuzzy Economic Review 1, No. 2 (1996) 35–53.

[93] C. Zopounidis, A. Pouliezos and D. Yannacopoulos, Designing a DSS for the Assessment of Company Performance and Viability, Computer Science in Economics and Management 5 (1992) 41–56.

![](/api/attachments/UG9HFG6U/fulltext/images/69be2348e9e5c2076388515b4f6b745f96472e5f5bade20b6008e814a066b2fa.jpg)

Constantin Zopounidis received his Doctorat D'Etat (1986) in management science, a D.E.A. (1982) in financial management from the University of Paris-IX Dauphine and a B.A. in business administration from the Macedonian University of Thessaloniki. He is a professor of financial management and operations research at the Technical University of Crete and a member of the Decision Support Systems Laboratory at the Department of Production Engineer

ing and Management. He was awarded the MOISIL Gold Medal and Diploma from the MOISIL International Foundation for his scientific work on multicriteria DSS and their application in the management of financial risks. He is the author of two books concerning venture capital and bankruptcy risk (Economica, Paris) and co-author of two other books concerning data analysis and multicriteria analysis (Kluwer Academic Publishers, Dordrecht). Furthermore, he has over 60 published articles, appearing in the following journals: Applied Stochastic Models and Data Analysis, Computational Economics, Decision Support Systems, European Journal of Operational Research, Foundations of Computing and Decision Sciences, Fuzzy Economic Review, Global Finance Journal, International Journal of Intelligent Systems in Accounting, Finance and Management, The Financier, among others. His current research interests focus on the areas of the management of financial risks and the design/development of multicriteria decision support systems for financial analysis and planning.

![](/api/attachments/UG9HFG6U/fulltext/images/e23448f648efbb343288aef14881e4d87b8f736ea9c87836474c16bb745a9b2e.jpg)

Michael Doumpos is a graduate student in the Department of Production Engineering and Management of the Technical University of Crete. He received his B.A. in production engineering and management from the Technical University of Crete and he is currently working on his Ph.D. thesis. His research interests focus on the areas of expert systems, decision support systems, multiple criteria decision making, and financial management. He is the co-author of a

book concerning the application of multicriteria knowledge-based decision support systems in the assessment of corporate performance and viability.

![](/api/attachments/UG9HFG6U/fulltext/images/d5abde494ed59ab45ac0895211bbf0410cd42e2c4da800daba7c875df2f9c71e.jpg)

Nikolaos F. Matsatsinis is an adjunct professor of decision support systems at the Technical University of Crete. He works as a special consultant at the Perfecture of Chania in Crete. He received his B.A. in physics from the Aristotle University of Thessaloniki and his Ph.D. in intelligent decision support systems from the Technical University of Crete, Department of Production Engineering and Management. He also has over 12 years of experience as a system and data

analyst. His research interests focus on the areas of expert systems, multiple criteria decision making, marketing management and the development of intelligent support systems for group decision making. He is the co-author of a book concerning the application of multicriteria knowledge-based decision support systems in the assessment of corporate performance and viability. Furthermore, he has over 13 articles published in several international journals and books.
