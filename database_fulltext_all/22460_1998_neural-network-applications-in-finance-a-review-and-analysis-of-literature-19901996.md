---
otero_id: 22460
otero_key: "F5JAQFET"
title: "Neural network applications in finance: A review and analysis of literature (1990–1996)"
authors: "Bo K Wong; Yakup Selvi"
year: "1998"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00050-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Neural network applications in finance: A review and analysis of literature (1990–1996)

Bo K. Wong $^{a,*}$ , Yakup Selvi $^{b}$

$^{a}$ Department of Finance and Decision Sciences, School of Business, Hong Kong Baptist University, Kowloon Tong, Hong Kong $^{b}$ Istanbul University, Turkey

Received 2 May 1997; accepted 12 May 1998

## Abstract

The field of neural network technology has been extensively studied in the last decade. This has led to considerable research on its use in various scientific applications and to the development of a diverse range of business applications. Consequently, an increasing amount of application efforts have concentrated on their development in the finance sector. In this paper, we investigated the trend of published applications for the period 1990–1996. The literature was examined according to (1) year of publication, (2) application area, (3) problem domain, (4) decision process phase, (5) level of management, (6) level of task interdependence, (7) means of development, (8) corporate/academic interaction in development, (9) technology/statistical technique integration, and (10) comparative study. Implications to neural networks developers/researchers and suggestions on future research are discussed. © 1998 Elsevier Science B.V. All rights reserved

Keywords: Neural networks; Finance application; Literature review

## 1. Introduction

Neural network technology was developed in an attempt to mimic the acquisition of knowledge and organization skills of the human brain. It offers significant support in terms of organizing, classifying, and summarizing data. It also helps to discern patterns among input data, requires few assumptions, and achieves a high degree of prediction accuracy. These characteristics make neural network technology a potentially promising alternative tool for recognition, classification, and forecasting in the area of finance, in terms of accuracy, adaptability, robustness, effectiveness, and efficiency in solving financial problems. Therefore, financial application areas that require pattern matching, classification, and prediction, such as bankruptcy prediction, loan evaluation, credit scoring, and bond rating, are fruitful candidate areas for neural network technology.

Great strides have been made in this technology in the last decade $[43]$ . This has led to increasing efforts, to use it in a wide variety of scientific applications and has contributed to the development of many different types of business applications. In the literature, an increasing amount of information has appeared, with a considerable portion focusing on the actual neural network development in the area of finance $[89]$ . The goal of this paper is to examine the historical trend of published finance applications and to explore potential research areas for the future.

## 2. Research methodology

To identify those journal articles that describe specific neural network applications in finance, an extensive search of the literature was conducted. Both, the scope of the bibliography and the criteria used in selecting articles are presented in Appendix A.

## 3. Classification

A final total of 64 articles (66 applications) were considered to be acceptable for the purposes of this study. As each article was reviewed, it was classified according to ten categories:

1. Year of publication.

2. Application area.

3. Problem domain (structured or semi/unstructured).

4. Decision process phase (intelligence, design, or choice).

5. Level of management (operational control, management control, or strategic planning).

6. Level of task interdependence (personal, group or organizational support).

7. Means of development (programming language or neural network tool).

8. Corporate/academic interaction in development (independent effort or corporate/academic joint efforts).

9. Technology/statistical technique integration.

10. Comparative study.

## 3.1. Classification by year of publication

Fig. 1 shows the distribution of articles published by year. Although, our search covered the period 1971–1996, we found no neural network finance applications published earlier than 1990.

## 3.2. Classification by application area

Table 1 shows the distribution of applications by application area and indicates that relatively more applications have been published in bankruptcy prediction of banks/thrifts, bankruptcy prediction of firms, and stock performance/selection prediction. These applications usually involve the interaction of many diverse variables that are highly correlated, frequently assumed to be nonlinear, unclearly related, and too complex to be described by a mathematical model. Many neural network finance application studies seem to suggest that neural networks perform as well or better than other sophisticated statistical techniques when it comes to analyzing time-series data, because they are capable of identifying and simulating nonlinear relationships in the data set, with no requirements of multivariate normal distribution or prior probability specification.

![](/api/attachments/F5JAQFET/fulltext/images/82a2684f179846187cd8b60416d230cad76aa1c208f2ad0332cb54e11aed36a2.jpg)  
Fig. 1. Yearwise distribution of articles.

Furthermore, the environment where these diverse variables exist is constantly changing. Therefore, the effectiveness of a model depends on how well it reflects the operating environment of the industry in terms of adjusting itself, as new observations are available. Neural networks not only accumulate, store, and recognize patterns of knowledge based on experience, but also constantly reflect and adapt to new environmental situations while they are performing predictions by constantly retraining and relearning $[8, 45]$ . As a result, they are more robust and accurate, with lower-prediction risks and less variance in their errors than the other statistical techniques.

## 3.3. Classification by problem domain

Managerial and other business decisions can generally be categorized, as being either structured or

Table 1  
Distribution of applications according to application area

<table><tr><td>Area</td><td>Totala</td></tr><tr><td>Bankruptcy prediction of firms [8, 10, 23, 49, 66, 81, 83, 87]</td><td>8</td></tr><tr><td>Stock performance/selection prediction [3, 40, 45, 72, 95, 96]</td><td>6</td></tr><tr><td>Bankruptcy prediction of banks/thrifts [53, 64, 75, 76, 77]</td><td>5</td></tr><tr><td>Bond trading [60, 61, 69]</td><td>3</td></tr><tr><td>Commercial loan application analysis [18, 28, 54]</td><td>3</td></tr><tr><td>Financial distress forecasting [1, 13, 14]</td><td>3</td></tr><tr><td>Real estate appraisal [6, 19, 93]</td><td>3</td></tr><tr><td>Bond rating [21, 42]</td><td>2</td></tr><tr><td>Credit evaluation [17, 37]</td><td>2</td></tr><tr><td>Futures price forecasting [29, 79]</td><td>2</td></tr><tr><td>Initial public offering pricing [30, 36]</td><td>2</td></tr><tr><td>Security performance prediction [50, 67]</td><td>2</td></tr><tr><td>Capital market index forecasting [92]</td><td>1</td></tr><tr><td>Checking account overdrafts [39]</td><td>1</td></tr><tr><td>Construction contract bond claims prediction [74]</td><td>1</td></tr><tr><td>Corporate health estimation [48]</td><td>1</td></tr><tr><td>Federal reserve decision-making [70]</td><td>1</td></tr><tr><td>Financial statement analysis and interpretation [46]</td><td>1</td></tr><tr><td>Future options hedging [35]</td><td>1</td></tr><tr><td>Future options pricing [35]</td><td>1</td></tr><tr><td>Future spot rates prediction [73]</td><td>1</td></tr><tr><td>Futures trading volume forecasting [38]</td><td>1</td></tr><tr><td>Insurance problem examination [84]</td><td>1</td></tr><tr><td>Interest rate prediction [57]</td><td>1</td></tr><tr><td>Intermarket analysis [62]</td><td>1</td></tr><tr><td>Loan evaluation [59]</td><td>1</td></tr><tr><td>Loan payment default classification [59]</td><td>1</td></tr><tr><td>Mortgage prepayment rate prediction [94]</td><td>1</td></tr><tr><td>Mortgage-backed security portfolios management [2]</td><td>1</td></tr><tr><td>Mutual fund net asset value forecasting [11]</td><td>1</td></tr><tr><td>Optimal stock portfolio selection [90]</td><td>1</td></tr><tr><td>Portfolio management [34]</td><td>1</td></tr><tr><td>Residential property values evaluation [15]</td><td>1</td></tr><tr><td>Stock market holding period return investigation [91]</td><td>1</td></tr><tr><td>Stock market volatility forecasting [20]</td><td>1</td></tr><tr><td>Stock’s systematic risk forecasting [88]</td><td>1</td></tr><tr><td>Treasury bond market prediction [63]</td><td>1</td></tr><tr><td>Total</td><td>66</td></tr></table>

$^{a}$ Total number of applications are more than the number of articles, because two articles have two applications each [35, 59].

semi/unstructured. It is not surprising to find that there is no application designed for structured financial decisions, since most of the real-world financial decisions are semi/unstructured, partially due to a certain degree of uncertainty in the knowledge. The sources of errors that create uncertainty can be, ambiguity, incompleteness, incorrectness, measurement, systematic errors, random errors, and reasoning [26]. Feedforward neural networks are especially good at addressing some of these problems [65]. Also techniques, such as fuzzy logic and genetic algorithms are incorporated into some neural networks and have greatly enhanced their ability to deal with relatively unstructured problems.

## 3.4. Classification by decision process phase

We further classified the neural network finance applications by three generic phases in the decision-making process. Approximately 98.5% (65) of the applications are developed for intelligence, 1.5% (1) for choice, and no applications were developed for the design phase.

Our survey results support the notion that, most of the neural network applications are developed for the intelligence phase (problem identification) of the decision process. In this, decision-makers search problems and opportunities continuously. In the finance area, the neural network is utilized to determine those firms/banks/thrifts that could go bankrupt, by determining their financial and operating health, based on their financial data. As a result, those institutions with potential financial troubles can be identified relatively early.

Since, a neural network is not the appropriate tool to identify alternative solutions, it is not surprising to find no applications in the design phase. In the choice phase, neural networks can be used to address some combinatorial optimization problems. Only one such application $[60]$ was identified in our survey. In this application, a hybrid system, called Neural logic network (NEULONET), was developed as a US future-bond-trading-advisory system by integrating neural networks with expert systems.

## 3.5. Classification by level of management

We further classified the applications by year, according to their management activities, as shown in Table 2. Approximately 30% (20) of the applications were for operational control and 61% (40) for management control, while only 9% (6) were for strategic planning.

These results substantiate Schocken and Ariav's beliefs that, neural networks are mostly used in the control level of management, since neural networks at this level are designed to optimize the use of capital, people, information, and other corporate resources. Furthermore, current personal computer-based neural network hardware and software packages, such as NeuralWorks Professional II/Plus and BrainMaker Profession, make neural networks easy to develop and use. These packages encourage finance managers, credit analysts, etc., to discover new and creative ways to make day-to-day decisions at the control level.

Table 2  
Distribution of applications by year of publication and managerial decision level

<table><tr><td>Year</td><td>Operational control</td><td>Management control</td><td>Strategic planning</td><td>Total</td></tr><tr><td>1996</td><td>7</td><td>5</td><td>-</td><td>12</td></tr><tr><td>1995</td><td>4</td><td>7</td><td>2</td><td>13</td></tr><tr><td>1994</td><td>7</td><td>9</td><td>-</td><td>16</td></tr><tr><td>1993</td><td>2</td><td>11</td><td>-</td><td>13</td></tr><tr><td>1992</td><td>-</td><td>6</td><td>2</td><td>8</td></tr><tr><td>1991</td><td>-</td><td>1</td><td>1</td><td>2</td></tr><tr><td>1990</td><td>-</td><td>1</td><td>1</td><td>2</td></tr><tr><td>Total</td><td>20</td><td>40</td><td>6</td><td>66</td></tr><tr><td>Percent</td><td>30.3</td><td>60.6</td><td>9.1</td><td>100</td></tr></table>

Neural networks' distinct classification capability allows them to support decision-making at the operational control level. Some typical applications include, credit or loan evaluations, bond rating, financial statement analysis, and intermarket analysis.

In view of their low face validity and inductive learning algorithms, neural networks are not suited for strategic planning. Our survey identified only six applications at this level: commercial loan application analysis $[54]$ ; construction contract bond claims prediction $[74]$ ; federal reserve decision-making $[70]$ ; financial distress forecasting $[13]$ ; real estate appraisal $[6]$ ; and optimal stock portfolio selection $[90]$ .

## 3.6. Classification by level of task interdependence

The neural network applications were then classified in terms of the type of decision-making for which they were designed. The level of task interdependence may exist at three levels; personal, group, and organizational [78]. At the personal level, neural network finance applications were designed to support a single user, or a single class of users, in a task. This task is distinct and relatively independent of other tasks. At the group level, applications were designed to support groups engaged in separate yet highly interrelated tasks. Finally, some decision-making exists at the organizational level, with diverse operations and individuals.

Our survey found that 80% (53) of the neural network finance applications are designed for personal decision-making. About 4.5% (3) of the applications are designed for group decision-making, while 15% (10) are designed for organizational decision-making.

The more common examples of personal support are, stock performance/selection prediction, bond rating, commercial loan analysis, and future price forecasting. Financial distress forecasting $[1]$ , investment management $[3]$ , and financial statement analysis interpretation $[46]$ are the examples of group support. The seven applications in organizational support are: bankruptcy prediction of banks/thrifts $[64, 75, 76, 77]$ ; bankruptcy prediction of firms $[83]$ ; futures trading volume forecasting $[38]$ ; and initial public offering pricing $[36]$ .

## 3.7. Classification by means of development

Generally speaking, neural networks can be developed either through the use of programming language or a neural network tool. Table 3 shows the distribution of neural network applications by the means of development and year. Out of 35 applications, that have reported the means of development, 37% (13) have been developed by using programming languages and 63% (22) by various tools. There appears to be no prominent increase in the use of one means of development over the other.

Table 3  
Distribution of applications by year and means of development

<table><tr><td>Year</td><td>Programming language</td><td>Tool</td><td>Not reported</td><td>Total</td></tr><tr><td>1996</td><td>1</td><td>3</td><td>8</td><td>12</td></tr><tr><td>1995</td><td>4</td><td>5</td><td>4</td><td>13</td></tr><tr><td>1994</td><td>3</td><td>3</td><td>10</td><td>16</td></tr><tr><td>1993</td><td>2</td><td>7</td><td>4</td><td>13</td></tr><tr><td>1992</td><td>1</td><td>3</td><td>4</td><td>8</td></tr><tr><td>1991</td><td>1</td><td>1</td><td>-</td><td>2</td></tr><tr><td>1990</td><td>1</td><td>-</td><td>1</td><td>2</td></tr><tr><td>Total</td><td>13</td><td>22</td><td>31</td><td>66</td></tr><tr><td>Percent</td><td>19.7</td><td>33.3</td><td>47</td><td>100</td></tr></table>

Distribution of applications by means of development and academic-business interaction

<table><tr><td>Academic-business interaction</td><td>Programming language</td><td>Tool</td><td>Total</td><td>Percent</td></tr><tr><td>Academic institution</td><td>12</td><td>15</td><td>27</td><td>77.2</td></tr><tr><td>Business-related institution</td><td>1</td><td>5</td><td>6</td><td>17.1</td></tr><tr><td>Joint effort</td><td>-</td><td>2</td><td>2</td><td>5.7</td></tr><tr><td>Total</td><td>13</td><td>22</td><td>35</td><td>100.0</td></tr></table>

Out of 13 applications, that have used programming languages as a means of development, eight used the C programming language and five used Pascal. Commonly used tools are NeuralWorks Professional II/Plus (6 applications) and BrainMaker Profession (5 applications).

Neural networks can be developed by academic institutions, business-related institutions, or through joint efforts. Table 4 shows the distribution of neural network finance applications by means of development and academic-business interaction. As shown in the Table 4, 77% (27) of the 35 applications that have reported the development were by an academic institution and 17% (6) by business-related institutions, while only 5.7% (2) were developed by joint efforts. The results seem to indicate that, there is no preference for the use of academic institutions in aiding neural network development. It is difficult to draw any conclusion on joint efforts, since there are very few applications reported.

## 3.8. Classification by corporate/academic integration

Our survey found that 62 applications (94%) were the result of the research efforts of either academicians or practitioners. Only three applications (4.6%) were the products of joint effort. One application could not be determined, due to insufficient information.

Joint research efforts can reveal a ‘middle ground’ for neural network applications development; projects that historically may not have been considered ‘challenging’ enough for academic research can still be important to an organization. Therefore, corporate/ academic joint efforts could help to produce more ‘real world’ applications. For example, the University of Texas at Austin and the Texas State Board of

Insurance used a neural network to develop an early warning system for predicting and monitoring insurer insolvency, 3 years ahead of time [8]. The system was proved to be successful, since it was easy to adapt and sensitive to economic change. Also, the University of Manitoba and the Canadian Wheat Board developed a neural network to forecast monthly future trading volumes 9 months ahead; the system outperformed the naive model for all commodities on the Winnipeg Commodity Exchange [38].

By combining resources and uniting academic expertise with corporate knowledge, joint efforts may prove to be cost-effective and increase the chance of success in the project. Also, since one can assume that the organization has a better understanding of its own functional interdependence than any outside researcher, joint efforts may also help researchers to develop organizational-level neural networks. It seems that these advantages have not yet been realized.

## 3.9. Classification by integration with other technologies and statistical techniques

The integration of neural networks with other technologies, such as decision support systems (DSSs), expert systems, fuzzy logics, genetic algorithms, or robotics can improve the applicability of neural networks in addressing various types of finance problems. Although, each technology has its own strengths and weaknesses, these technologies are complementary $[33]$ . Weaknesses of one technology can be overcome by strengths of another by achieving a synergistic effect $[58]$ . Such an effect can create results that are more efficient, productive, and effective than the sum of their parts $[4]$ .

Our research found that eight applications are integrated with other technologies. Seven of them are integrated with expert systems $[18, 54, 57, 60, 61, 69, 96]$ and one is integrated with fuzzy logic as well as expert systems $[90]$ .

The performance of neural network may be further improved by integrating with statistical techniques as evidence in three applications identified in our survey. Markham and Ragsdale [53] showed that, when a neural network model was combined with Mahalanobis Distance Measure statistical technique to predict bankruptcy of banks, the incidence of misclassification was significantly reduced, and therefore, a significant amount of money could be saved. Taha et al. [74] showed that neural network integration with discriminate analysis, regression, and logistic regression models provided better prediction accuracy of construction contract bond claims. Lee, Han and Kwon [49] proposed, three-hybrid neural network models and showed that they are very promising for bankruptcy prediction, in terms of predictive accuracy and adaptability.

## 3.10. Comparative studies of neural networks with statistical techniques

Statistical techniques are common and traditional approaches for solving financial problems that require pattern matching, classification, and prediction. Some typical examples are: corporate-bond rating; credit evaluation; and bankruptcy prediction. Neural networks may be viable alternatives to classical statistical models, since they are especially well adapted to finding solutions with a high level of accuracy in similar applications.

In our surveyed articles, 37 neural network finance applications compared the performance of neural networks with that of statistical techniques. Those more common techniques included discriminate analysis [1, 8, 13, 14, 17, 39, 42, 49, 66, 72, 75, 76, 77, 81, 87, 95], logit [17, 21, 23, 42, 64, 75, 76, 77], regression analysis [2, 11, 19, 42, 49, 83, 92, 93], and ID3 [39, 49, 59, 76, 77].

In these comparative studies, neural networks generally outperformed statistical techniques $[8, 10, 11, 13, 14, 19, 20, 23, 30, 34, 36, 38, 42, 48, 49, 59, 64, 67, 72, 75, 76, 77, 81, 83, 87, 88, 92, 94, 95]$ . But, in some cases, statistical techniques either were comparable or outperformed neural networks $[1, 2, 21, 39, 93]$ .

## 4. Profile of neural network finance application development

During the period covered, 66 applications (64 articles) on neural network finance applications were published. These articles were authored by a total of 129 persons. Of these, $\approx82\%$ (106 persons) were affiliated with different academic institutions and 14% (18 persons) were affiliated with different non-academic or business-related institutions. Five authors did not report their affiliations. Approximately 67% (86 persons) were affiliated with different US institutions and 30% (38 persons) were affiliated with different foreign institutions.

## 5. Implications to neural network developers and researchers

Our survey indicated that only a few neural networks are developed for supporting the strategic planning of decision-making. Developers should be extremely careful when they develop systems for this purpose. Two inherent limitations in neural networks jeopardize their use in strategic planning: (1) neural learning algorithms are inductive and have a requirement for large data sets and repetitive samples, while strategic decision-making focuses on unusual and nonroutine types of decisions; and (2) neural networks are unable to explain their decisions. The decisions are supported, neither by significance tests nor by deductive knowledge and, therefore, suffer from low-face validity. They, therefore, lack the kind of credibility that is critical in supporting decisions at the strategic level.

The design and choice phases of decision-making do not lend themselves naturally to neural network support, since this technology is not good in constructing or evaluating solutions. This possibly explains why we found no applications in the design phase and only one application in the choice phase.

However, developers should not totally ignore neural networks when addressing strategic planning or the design and choice phase of decision-making. This is especially true when the integration of neural networks with other technologies, such as expert systems, is possible. Researchers have addressed such potential integration $[76, 97]$ . In particular, Kuncicky et al. $[47]$ summarized four different neural network/expert system integration approaches: (1) connectionist expert systems – all or part of the functionality of an expert system is replaced with a neural network; (2) symbolic connectionist methods – constraint networks are built from symbolic structures, and then parallel constraint satisfaction is used to study high-level cognitive tasks; (3) conglomerate systems – expert systems and neural networks are used as building blocks to solve the larger problem; and (4) translation models - knowledge from an expert system is transferred to a neural network. These integrations, not only allow neural networks to address various types/ levels of decisions, but also greatly improve their quality.

In our survey, there were only three research studies on the integration of neural networks and statistical techniques. All were recently published and have proved that a combined approach is better than any one method in isolation. Also, it has been suggested that, combining forecasts should become part of the mainstream of forecasting practice to achieve more accurate results $[12]$ . Since, the neural network is considered to have great potential, as a powerful forecasting tool, its integration with other statistical techniques should improve the overall performance. Therefore, we believe that evaluating the performance of integrating neural networks, with statistical techniques to address finance problems, is likely to provide fruitful opportunities for developers in the future.

A majority of the neural network applications are developed by academicians. This implies that most neural network developers in companies still hesitate to use this technology in business. We believe that companies should explore the potential applications of neural networks and consider the option of joint efforts with academics as a means of developing business neural networks. Our survey has found only a few such cooperative efforts; however, some have already indicated benefits to developers through an efficient integration of resources. Other forms of joint efforts, such as company-to-company research and investment in an AI start-up company, should also be considered.

## 6. Conclusion

The future of neural networks in the finance area may see increased integration with other existing or developing technologies and statistical techniques. As advancements are made in AI technologies and computer-based related systems, there should be new opportunities to apply neural network technology for finance research. This would encourage or motivate academics and practitioners to collaborate in further exploration of the potential of neural networks.

## 7. Limitations of the study

It is necessary to be cautious in interpreting the results of this study, since the findings are based on data collected only from journal articles. The results will therefore, not include all real world neural networks. Furthermore, we have reviewed only academic/professional journal articles. Conference proceedings and doctoral dissertations are excluded, as we assume that high-quality research is eventually published in journals. Also, many foreign journals were not included, since they are not within the scope of our search methods.

## Appendix A

## Scope of the bibliography

The first and most important step in the literature retrieval process was the search of the ABI/INFORM database. The minicomputer-based version of this database was searched for the period covering 1971–1996. This step provided access to abstracts of articles from over 800 different business-related journals world-wide. By using the descriptors ‘neural network’ and ‘neural networks’, we were able to retrieve over 800 abstracts for review from the specified 26-year period.

Next, we manually searched the Business Periodical Index (BPI) for the period January 1980 through December 1996. The BPI, indexes 340 business-related periodicals. Only articles from journals not included in the ABI/INFORM database were considered for further review.

The next step involved a reference search of various textbooks on neural networks and related topics. Twenty-one textbooks were examined: Beale and Jackson [5]; Boullart; Krijgsman and Vingerhoeds [7]; Caudill and Butler [9]; Dagli [16]; Fausett [22]; Gallant [24]; Gelenbe [25]; Hecht-Nielsen [32]; Khanna [41]; Kosko [44]; Lisboa [51]; Lisboa and Taylor [52]; Murre [55]; Nelson and Illingworth [56]; Simpson [68]; Soucek [71]; Trippi and Turban [80]; Turban [82]; Wang and Takefuji [85]; Wasserman and Oetzel [86]; and Zahedi [97]. Most of the books are not very useful for our research, since most references are only on scientific applications.

The textbook search, together with the ABI/INFORM and BPI searches, provided articles from a wide variety of journals. However, it was decided that an additional 12 journals should be searched. The decision to include these additional journals was based on two reasons: (1) several journals known to publish neural network articles were either included only partially or not included in the ABI/INFORM database or the BPI; and (2) some of these additional journals are recognized by management information system (MIS) experts as being important to the field of MIS [27, 31]. These 12 journals are ACM DATABASE, AI Expert, Artificial Intelligence, Communications of the ACM, Expert Systems: International Journal of Knowledge Engineering and Neural Networks, IEEE Expert, IEEE Transactions on Neural Networks, IEEE Transactions on Software Engineering, IEEE Transactions on Systems, Man, and Cybernetics, Information Systems Research, Journal of Management Information Systems and Omega: The International Journal of Management Science.

## A.1 Selection criteria

Every article retrieved through the process described above was carefully reviewed before making a decision regarding its inclusion in this survey. We required each article to discuss the prototype or development of a neural network finance application. This requirement eliminated many of the articles retrieved from the ABI/INFORM database, since the descriptors used produced abstracts from numerous articles that did not describe finance applications. In addition, we examined the research methodology of each article retrieved. Only those articles based on rigorous research methods were included.

## References

[1] E.I. Altman, G. Marco, F. Varetto, Corporate distress diagnosis: Comparisons using linear discriminant analysis and neural networks (the Italian experience), Journal of Banking and Finance 18, 1994, pp. 505–529.

[2] A. Bansal, R.J. Kauffman, R.R. Weitz, Comparing the modeling performance of regression and neural networks as data quality varies: A business value approach, Journal of Management Information Systems 10(1), 1993, pp. 11–32.

[3] D.S. Barr, G. Mani, Using neural nets to manage investments, AI Expert 9, 1994, pp. 16–21.

[4] J.J. Barron, Putting fuzzy logic into focus: When dealing with ambiguous data, desktop fuzzy-logic applications deliver precise results, BYTE 4, 1993, pp. 111–118.

[5] R. Beale, T. Jackson, Neural Computing: An Introduction, Adam Hilger, Bristol, UK, 1990.

[6] R.A. Borst, Artificial neural networks: The next modeling/calibration technology for the assessment community, Property of Tax Journal 10(1), 1991, pp. 69–94.

[7] L. Boullart, A. Krijgsman, R.A. Vingerhoeds, Application of Artificial intelligence in Process Control, Pergamon, Oxford, UK, 1992.

[8] P.L. Brockett, W.W. Cooper, L.L. Golden, U. Pitaktong, A neural network method for obtaining an early warning of insurer insolvency, The Journal of Risk and Insurance 61(3), 1994, pp. 402–424.

[9] M. Caudill, C. Butler, Understanding Neural Networks: Computer Explorations, Volume 1: Basic Networks, Massachusetts Institute of Technology, Cambridge, MA, 1992.

[10] S. Chen, P. Mangiameli, D. West, The comparative ability of self-organizing neural networks to define cluster structure, OMEGA: International Journal of Management Science 23(3), 1995, pp. 271–279.

[11] W.-C. Chiang, T.L. Urban, G.W. Baldridge, A neural network approach to mutual fund net asset value forecasting, OMEGA: International Journal of Management Science 24(2), 1996, pp. 205–215.

[12] R.T. Clemen, Combining forecasts: A review and annotated bibliography, International Journal of Forecasting 5, 1989, pp. 559–584.

[13] P.K. Coats, L.F. Fant, A neural network approach to forecasting financial distress, Journal of Business Forecasting 10 (4) (1991–1992) 9–12.

[14] P.K. Coats, L.F. Fant, Recognizing financial distress patterns using a neural network tool, Financial Management 22(3), 1993, pp. 142–155.

[15] A. Collins, A. Evans, Aircraft noise and residential property values: An artificial neural network approach, Journal of Transport Economics and Policy 28(2), 1994, pp. 175–197.

[16] C.H. Dagli, Artificial Neural Networks for Intelligent Manufacturing, Chapman and Hall, London, UK, 1994.

[17] V.S. Desai, J.N. Crook, G.A. Overstreet, Jr., A comparison of neural networks and linear scoring models in the credit union environment, European Journal of Operational Research 95(1), 1996, pp. 24–27.

[18] P.-S. Deng, Automating knowledge acquisition and refinement for decision support: A connectionist inductive inference model, Decision Sciences 24(2), 1993, pp. 371–393.

[19] A.Q. Do, G. Grudnitski, A neural network approach to residential property appraisal, The Real Estate Appraiser 58(3), 1992, pp. 38–45.

[20] R.G. Donaldson, M. Kamstra, Forecasting combining with neural network, Journal of Forecasting 15, 1996, pp. 49–61.

[21] S. Dutta, S. Shekhar, W.Y. Wong, Decision support in non-conservative domains: Generalization with neural networks, Decision Support Systems 11(5), 1994, pp. 527–544.

[22] L. Fausett, Fundamentals of Neural Networks: Architectures, Algorithms, and Applications, Prentice-Hall, Englewood Cliffs, NJ, 1994.

[23] D. Fletcher, E. Goss, Forecasting with neural networks: An application using bankruptcy data, Information and Management 24(3), 1993, pp. 159–167.

[24] S.I. Gallant, Neural Network Learning and Expert Systems, Massachusetts Institute of Technology, Cambridge, MA, 1993.

[25] E. Gelenbe, Neural Networks Advances and Applications, Elsevier Science Publishers BV, Amsterdam, The Netherlands, 1991.

[26] J. Giarratano, G. Riley, Expert Systems: Principles and Programming, PSW-Kent, Boston, MA, 1989.

[27] M. Gillenson, J. Stutz, Academic issues in MIS: Journals and books, MIS Quarterly 15, 1991, pp. 447–452.

[28] L.W. Glorfeld, B.C. Hardgrave, An improved method for developing neural networks: The case of evaluating commercial loan creditworthiness, Computers and Operations Research 23(10), 1996, pp. 933–944.

[29] G. Grudnitski, L. Osburn, Forecasting S and P and gold futures prices: An application of neural networks, The Journal of Futures Markets 13(16), 1993, pp. 631–643.

[30] C. Haefke, C. Helmenstein, Forecasting Austrian IPO: An application of linear and neural network error-correction models, Journal of Forecasting 15(3), 1996, pp. 237–251.

[31] S. Hamilton, B. Ives, The journal communication system for MIS research, Database 14, 1983, pp. 3–14.

[32] R. Hecht-Nielsen, Neurocomputing, Addison-Wesley, Reading, MA, 1990.

[33] S.H. Huang, H.C. Zhang, Neural-expert hybrid approach for intelligent manufacturing: A survey, Computers in Industry 26(2), 1995, pp. 107–126.

[34] S.-Y. Hung, T.-P. Liang, V.W.-L. Liu, Integrating arbitrage pricing theory and artificial neural networks to support portfolio management, Decision Support System 18, 1996, pp. 301–316.

[35] A.W. Hutchison, A.W. Lo, T. Poggio, A nonparametric approach to pricing and hedging derivative securities via learning networks, The Journal of Finance 49(3), 1994, pp. 851–889.

[36] B.A. Jain, B.N. Nag, Artificial neural network models for pricing initial public offerings, Decision Sciences 26(3), 1995, pp. 283–302.

[37] H.L. Jensen, Using neural networks for credit scoring, Managerial Finance 18(6), 1992, pp. 15–26.

[38] I. Kaastra, M.S. Boyd, Forecasting futures trading volume using neural networks, The Journal of Futures Markets 15(8), 1995, pp. 953–970.

[39] M.W. Kattan, D.A. Adams, M.S. Parks, A comparison of machine learning with human judgment, Journal of Management Information Systems 9(4), 1993, pp. 37–57.

[40] J. Kean, Neural nets and stocks: Training a predictive system, PC AI 7(5), 1993, pp. 45–47.

[41] T. Khanna, Foundations of Neural Networks, Addison-Wesley, Reading, MA, 1990.

[42] J.W. Kim, H.R. Weistroffer, R.T. Redmond, Expert systems for bond rating: A comparative analysis of statistical, rule-based and neural network systems, Expert Systems 10(3), 1993, pp. 167–172.

[43] D.E. Kirrane, Machine learning, Training and Development Journal 44, 1990, pp. 24–29.

[44] B. Kosko, Neural Networks and Fuzzy Systems: A Dynamical Systems Approach to Machine Intelligence, Prentice Hall, Englewood Cliffs, NJ, 1992.

[45] L. Kryzanowski, M. Galler, D.W. Wright, Using artificial neural networks to pick stocks, Financial Analysts Journal 49(4), 1993, pp. 21–27.

[46] L. Kryzanowski, M. Galler, Analysis of small-business financial statements using neural nets, Journal of Accounting, Auditing and Finance 10(1), 1995, pp. 147–172.

[47] D.C. Kuncicky, S.I. Hruska, R.C. Lacher, Hybrid systems: The equivalence of the rule-based expert system and artificial neural network inference, International Journal of Expert Systems 4(3), 1992, pp. 281–297.

[48] R.C. Lacher, K.C. Pamela, S.C. Sharma, L.F. Fant, A neural network for classifying the financial health of a firm, European Journal of Operational Research 85(1), 1995, pp. 53–65.

[49] K.C. Lee, I. Han, Y. Kwon, Hybrid neural network models for bankruptcy predictions, Decision Support System 18, 1996, pp. 63–72.

[50] F.C. Lin, M. Lin, Neural networks can discern patterns among input data and thus are the perfect vehicle for analyzing financial data: Here's how, AI Expert 8, 1993, pp. 37–41.

[51] P.J.G. Lisboa, Neural Networks: Current Applications, Chapman and Hall, London, UK, 1992.

[52] P.J.G. Lisboa, M.J. Taylor, Techniques and Applications of Neural Networks, Ellis Horwood, West Sussex, UK, 1993.

[53] I.S. Markham, C.T. Ragsdale, Combining neural networks and statistical predictions to solve the classification problem in discriminant analysis, Decision Sciences 26(2), 1995, pp. 229–242.

[54] R.A. Marose, A financial neural-network application, AI Expert 5, 1990, pp. 50–53.

[55] J.M.J. Murre, Learning and Categorization in Modular Neural Networks, Lawrence Erlbaum Associates, Hillsdale, NJ, 1992.

[56] M.M. Nelson, W.T. Illingworth, A Practical Guide to Neural Nets, Addison-Wesley, Reading, MA, 1991.

[57] C. Nikolopoulos, P. Fellrath, A hybrid expert system for investment advising, Expert Systems 11(4), 1994, pp. 245–250.

[58] B.A. Osky, B.S. Vijayaraman, Integrating expert systems and neural nets: Exploring the boundaries of AI, Information Systems Management 12(2), 1995, pp. 47–54.

[59] S. Piramuthu, M.J. Shaw, J.A. Gentry, A classification approach using multi-layered neural networks, Decision Support Systems 11(5), 1994, pp. 509–525.

[60] T.-S. Quah, C.-L. Tan, K.S. Raman, H.H. The, B.S. Srinivasan, A shell environment for developing connectionist decision support systems, Expert Systems 11(4), 1994, pp. 225–234.

[61] T.-S. Quah, C.-L. Tan, K.S. Raman, B. Srinivasan, Towards integrating rule-based expert systems and neural networks, Decision Support Systems 17, 1996, pp. 99–118.

[62] M.A. Ruggiero, Jr., Training neural nets for intermarket analysis, Futures 23(9), 1994, pp. 42–44.

[63] M.A. Ruggiero, Jr., Build a real neural net, Futures 24(6), 1995, pp. 44–46.

[64] L.M. Salchenberger, E.M. Cinar, N.A. Lash, Neural networks: A new tool for predicting thrift failures, Decision Sciences 23(4), 1992, pp. 899–916.

[65] S. Schocken, G. Ariav, Neural networks for decision support: Problems and opportunities, Decision Support Systems 11, 1994, pp. 393–414.

[66] C. Serrano-Cinca, Self organizing neural networks for financial diagnosis, Decision Support Systems 17, 1996, pp. 227–238.

[67] S. Shi, L.D. Xu, B. Liu, Applications of artificial neural networks to the nonlinear combination of forecasting, Expert Systems 13(3), 1996, pp. 195–201.

[68] P.K. Simpson, Artificial Neural Systems: Foundations, Paradigms, Applications, and Implementations, Pergamon, Elmsford, NY, 1990.

[69] C. Siriopoulos, S. Perantonis, G. Karakoulos, Artificial intelligence models for financial decision making, Information Strategy: The Executive's Journal 11(1), 1994, pp. 49–54.

[70] P.A. Smith, O.H. Maclin, Have presidents influenced monetary policy: New evidence from an artificial neutral network, Studies in Economics and Finance 16(1), 1995, pp. 23–45.

[71] B. Soucek, Neural and Intelligent Systems Integration: Fifth and Sixth Generation Integrated Reasoning Information Systems, Wiley, Toronto, Canada, 1991.

[72] G.S. Swales, Jr., Y. Yoon, Applying artificial neural networks to investment analysis, Financial Analysts Journal 48(5), 1992, pp. 78–80.

[73] N.R. Swanson, H. White, A model-selection approach to assessing the information in the term structure using linear models and artificial neural networks, Journal of Business and Economic Statistics 13(3), 1995, pp. 265–275.

[74] M.A. Taha, S.C. Park, J.S. Russell, Knowledge-based DSS for construction contractor prescreening, European Journal of Operational Research 84(1), 1995, pp. 35–46.

[75] K.Y. Tam, M. Kian, Predicting bank failures: A neural network approach, Applied Artificial Intelligence 4, 1990, pp. 265–282.

[76] K.Y. Tam, Neural network models and the prediction of bank bankruptcy, Omega: The International Journal of Management Science 19(15), 1991, pp. 429–445.

[77] K.Y. Tam, M. Kiang, Managerial applications of neural networks: The case of bank failure predictions, Management Science 38(7), 1992, pp. 926–947.

[78] J.D. Thompson, Organization in Action, Mcgraw-Hill, New York, NY, 1967.

[79] R.R. Trippi, D. Desieno, Trading equity index futures with a neural network, The Journal of Portfolio Management 19(1), 1992, pp. 27–33.

[80] R.R. Trippi, E. Turban, Neural Networks in Finance and Investing, Probus, Chicago, IL, 1993.

[81] J. Tsukuda, S. Baba, Predicting Japanese corporate bankruptcy in terms of financial data using neural network, Computers and Industrial Engineering 27(1)–4, 1994, pp. 445–448.

[82] E. Turban, Decision Support and Expert Systems: Management Support Systems, Prentice Hall, Englewood Cliffs, NJ, 1995.

[83] G. Udo, Neural network performance on the bankruptcy classification problem, Computers and Industrial Engineering 25(1)–4, 1993, pp. 377–380.

[84] M.R. Versaggi, Understanding conflicting data, AI Expert 10(4), 1995, pp. 21–25.

[85] J. Wang, Y. Takefuji, Neural Networks in Design and Manufacturing, World Scientific, Farrer Road, Singapore, 1993.

[86] P.D. Wasserman, R.M. Oetzel, Neural Source: The Bibliographic Guide to Artificial Neural Networks, Van Nostrand Reinhold, New York, NY, 1990.

[87] R.L. Wilson, R. Sharda, Bankruptcy prediction using neural networks, Decision Support Systems 11(5), 1994, pp. 545–557.

[88] H.-G. Wittkemper, M. Steiner, Using neural networks to forecast the systematic risk of stock, European Journal of Operational Research 90, 1996, pp. 577–588.

[89] B.K. Wong, T.A. Bodnovich, Y. Selvi, A bibliography of neural network business applications research: 1988 – September 1994, Expert Systems 12(3), 1995, pp. 253–262.

[90] F.S. Wong, P.Z. Wang, T.H. Goh, B.K. Quek, Fuzzy neural systems for stock selection, Financial Analysts Journal 48(1), 1992, 47–52, 74.

[91] S.Q. Wong, J.A. Long, A neural network approach to stock market holding period returns, American Business Review 13(2), 1995, pp. 61–64.

[92] D. Wood, B. Dasgupta, Classifying trend movements in the MSCI USA capital market index – A comparison of regression, ARIMA and neural network methods, Computers and Operations Research 23(6), 1996, pp. 611–622.

[93] E. Worzala, M. Lenk, A. Silva, An exploration of neural networks and its application to real estate valuation, The Journal of Real Estate Research 10(2), 1995, pp. 185–201.

[94] Y. Yamamoto, S.A. Zenios, Predicting prepayment rates for mortgages using the cascade-correlation learning algorithm, The Journal of Fixed Income 2(4), 1993, pp. 86–96.

[95] Y. Yoon, G. Swales, Jr., T.M. Margavio, A comparison of discriminant analysis versus artificial neural networks, Journal of the Operational Research Society 44(1), 1993, pp. 51–60.

[96] Y. Yoon, T. Guimaraes, G. Swales, Jr., Integrating artificial neural networks with rule-based expert systems, Decision Support Systems 11(5), 1994, pp. 497–507.

[97] F. Zahedi, Intelligent Systems for Business: Expert Systems with Neural Networks, Belmont, Wadsworth, CA, 1993.

![](/api/attachments/F5JAQFET/fulltext/images/a4ce3272b5fb2142a1b1cb260272e2d34e1b02faf583dd1a218df3be4c3d8286.jpg)

Bo K. Wong is currently an associate professor of management information systems (MIS) in the Department of Finance and Decision Sciences at Hong Kong Baptist University. He was formerly a distinguished graduate faculty member, coordinator and professor of MIS in the Department of Management at Youngstown State University, Youngstown, Ohio, USA.

His current research interests are in neural network and genetic algorithm applications. He has published extensively in a variety of journals, including articles in Information and Management, Journal of Decision Support Systems, European Journal of Operational Research, Expert Systems: International Journal of Knowledge Engineering and Neural Networks, Journal of Systems Management, International Journal of Operations and Production Management, Information Systems Management, and other professional journals. He received the Youngstown State University Research Professorship Award in both 1991 and 1993, the Youngstown State University Distinguished Professorship Award for Scholarship in 1995, the Most Distinguished Research Paper Award in the Society for the Advancement of Information Systems, 1996, and was listed in Who's Who in 1993.

![](/api/attachments/F5JAQFET/fulltext/images/2b23d1a8a2d63fcea2d92d17c0d64eef7d9a4c86f64114b5a69589384541f80b.jpg)

Yakup Selvi is currently a Ph.D. candidate in accounting and a teaching and research assistant at Istanbul University, Department of Accounting, Faculty of Business, Avcilar-Istanbul, Turkey, 80850. He received his B.S. in Business Administration and M.S. in Marketing from Istanbul University and an M.B.A. from Youngstown State University (YSU), Youngstown, Ohio 44555. In addition, he worked at YSU as

a research assistant in the Department of Management. He has published in Expert Systems: International Journal of Knowledge Engineering and Neural Networks and was a recipient of the Most Distinguished Research Paper Award in the Society for the Advancement of Information Systems in 1996.
