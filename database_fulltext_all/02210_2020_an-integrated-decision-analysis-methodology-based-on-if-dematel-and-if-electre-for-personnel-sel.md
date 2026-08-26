---
otero_id: 2210
otero_key: "HPEJDPHV"
title: "An integrated decision analysis methodology based on IF-DEMATEL and IF-ELECTRE for personnel selection"
authors: "Huseyin Selcuk Kilic; Ayse Ecenaz Demirci; Dursun Delen"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113360"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An integrated decision analysis methodology based on IF-DEMATEL and IF-ELECTRE for personnel selection<sup>☆</sup>

![](/api/attachments/HPEJDPHV/fulltext/images/f6ebeedd895d92e5ba2836ee229d3857afac9171ed0eef1595fa9367d46b0c57.jpg)

Huseyin Selcuk Kilic<sup>a</sup>, Ayse Ecenaz Demirci<sup>b</sup>, Dursun Delen<sup>c,d,⁎</sup>

<sup>a</sup> Department of Industrial Engineering, Marmara University, Kadıköy, Istanbul 34722, Turkey <sup>b</sup> Benson & Partners - IESF Executive Search and Management Advisory, Besiktas, Istanbul 34335, Turkey <sup>c</sup> Department of Management Science and Information Systems, Center for Health Systems Innovation, Spears Schook of Business, Oklahoma State University, Stillwater OK, USA

<sup>d</sup> Faculty of Management, Department of MIS, Halic University, Istanbul, 34445, Turkey

## A R T I C L E I N F O

Keywords: Business analytics Group decision-making IF-DEMATEL IF-ELECTRE Multicriteria decision-making (MCDM) Personnel selection

## A B S T R A C T

Due to its complex, time-demanding, and multifaceted structure, personnel selection is considered as a multi criteria decision-making problem, the framework of which includes both qualitative and quantitative criteria. Although various techniques have been proposed to address this problem in various industries, a robust methodology that is capable of explicitly considering the presence of uncertainty/vagueness is still a necessity. Therefore, with this study, we propose an integrated methodology that leverages Decision Making Trial and Evaluation Laboratory (DEMATEL) and Elimination and Choice Expressing the Reality (ELECTRE) methods under Intuitionistic Fuzzy (IF) environment. Within the proposed methodology, firstly, the IF-DEMATEL method is employed to obtain the importance-weights of the elicited criteria, and then the IF-ELECTRE method is formulated and applied to rank the candidates based on cardinal and ordinal evaluations. To illustrate the viability of the proposed methodology, an application case is performed at an air-filter manufacturing company. Hence, this study aims to contribute to the theoretical and practical extent of the related literature by proposing and illustrating an integrated analytics methodology capable of addressing personnel selection decisions in complex and imprecise real-world scenarios.

## 1. Introduction

Towards the end of the 20th century, factors such as globalization, growing demands, social and cultural shifts, and changing competitive landscape and related factors have compelled establishments worldwide to redefine their processes to focus on agility, and to minimize cost and enhance the quality of products or services in order to be more responsive to the changing needs and wants of the customers. In this context, human resources management has been a critical function for organizations since a qualified workforce is one of the most critical assets for attaining organizational goals and objectives. Human resources management deals with the endeavors and skills of people who work for the firm and usually characterized by the activities associated with the personnel-related goals of the organization. Management activities include forecasting the future demand for the workforce of the firm and developing strategies related to recruitment, training, and retention of employees. The human resources department in a company performs services that make a direct contribution to the performance of the enterprise. Moreover, human resources management influences the culture of an organization, which is usually defined by several dimensions, including policies and procedures, organizational structure, employee skills, characteristics of customers and competitors [64].

On the most visible level, the human resources department deals with the recruitment strategies in order to meet the corporation's needs by selecting the right person who could demonstrate the desired level of performance for the achievement of the business' goals. The personnel selection process is defined as an intricate organizational function that specifies the flow of candidates into and out of an organization to augment productivity [24]. Along with this aim, fast technological advancements and globalization have forced markets to desire more qualified and professional human resources [48]. Therefore, personnel selection is considered as a vital activity in the organizations supporting the company's goals at various levels, and in so doing, providing means to achieve a sustainable competitive advantage [1,20].

Broadly defined, decision-making is a process that consists of making a selection among feasible alternatives in an attempt to attain specific objectives, and in an ideal case, it determines the best choice for the specific needs [32]. Personnel selection is considered as a kind of multicriteria decision-making (MCDM) problem. MCDM problems involve more than one criterion and often with more than one conflicting objective to be considered collectively to reach the most plausible decision. MCDM tools include a high number of standalone or hybrid/ integrated solution methods and methodologies that aim to system atically deal with complex problems [54]. Imprecise constraints usually exist in corporations, limited availability and lack of suitability of suitable candidates, and the varied, often conflicting, preferences of all decision-makers (DMs) and state holders make identifying and hiring the best personnel a complicated endeavor. The structure of the personnel selection problem involves both qualitative and quantitative criteria, along with conflicting objectives. Hence, MCDM methods are deemed to be the most suitable decision support tools to handle the complex, multicriteria structure of the personnel selection problem.

Besides the ambiguity of expressions and the evaluations of decision-makers, they can also lack precision and be inexact. Hence, intuitionistic fuzzy (IF) sets, which are the extensions of traditional fuzzy sets, can be used to address these weaknesses, and therefore, have been regarded as a more appropriate tool than the standard fuzzy sets [16]. Because of the advantages and suitability of intuitionistic fuzzy sets for the multi-attribute decision-making problems, it is employed as a means to model and address vagueness in this study as an integral part of the proposed methodology. Diferent from the previous studies in the extant literature, in this framework, MCDM methods, including Intuitionistic Fuzzy Decision Making Trial and Evaluation Laboratory (IF-DEMATEL) and Intuitionistic Fuzzy Elimination and Choice Expressing the Reality (IF-ELECTRE) are synergistically used for the first time to address the complexities posed by the personnel selection problem under a group decision-making scenario.

The remainder of this paper is organized as follows. Section 2 provides a review of extant literature related to the criteria and methods used for personnel selection. Section 3 describes the proposed methodology and explains the fundamental techniques employed therein—IF-DEMATEL and IF-ELECTRE. Section 4 presents an application case to demonstrate the viability of the proposed methodology. Section 5 provides the results and discussion, and also includes comparison and sensitivity analysis. Section 6, the last chapter of the paper, ofers a summary and concluding remarks about the study.

## 2. Literature review

In the early 1900s, Frederick Taylor, who is known as the father of scientific management, paved the way for the development of the modern-day personnel functions. In his book, Shop Management [107], he provided a scientific method for the selection and training of workers. Besides, he introduced incentive systems to reward employees for highly efective performance for motivating and inspiring all employees. Taylor's primary objective was to achieve the optimal level of productivity by developing models and related practical policies for human resources management (HRM) [108,110].

Personnel selection is one of the most vital functions of HRM. It aims to establish the best matching between the applicants and the job description and is regarded as one of the main concerns of many employers [18]. Therefore, in practice, this discipline analyzes factors like candidates' personalities, education, abilities/skills, and interested areas as they relate to the work. It matches the requirements of a job description to the abilities/skills and qualifications of a candidate and does that by using systematic methods and tests [19]. Inaccurate selection leads to extra training, lower productivity, a rise in occupational accidents, and an increase in the workload of coworkers. Since there usually is a wide variety of criteria and a large pool of candidates involved in the personnel selection situation, it is often regarded as a complex, multifaceted, and multicriteria decision-making problem.

To illustrate the position, motivation, and contribution of the present study, the extant literature is reviewed from the perspectives of posed challenges, evolving trends, and proposed solutions. One of the motivational studies at this point is performed by Lievens et al. [69]; they concluded that labor market shortages, technological developments, applicant perceptions of selection procedures, and constructdriven approaches are the most critical trends. Anderson et al. [7], on the other hand, focused on four major themes in their study: candidate reactions to selection methods, attribution theory and research in the selection, distributive and procedural justice perspectives, and appli cant decision-making in the selection process. Similarly, McCarthy et al. [78] and Truxillo et al. [109] focused on the applicant perspectives within the personnel selection process. Anderson et al. [8], in a later study, investigated the future perspectives on employee selection. Specifically, they evaluated four themes—i.e., bimodal prediction, multilevel fit in the selection, application reactions and decision making, and tensions between research and practice—critical to the selection and assessment researches in the personnel selection process.

Considering the complexity of the selection process, various tech niques with diferent capability ranges have been proposed to address the problem in the literature. In a review, Anderson et al. (2008) investigated ten popular personnel assessment techniques, including in terviews, resumes, work-sample tests, biographical information, written ability tests, personal references, personality tests, honesty tests, personal contacts, and graphology. They also extended their study into an international comparison among the Netherlands, USA, France, Spain, Portugal, and Singapore. Woods et al. [116], in a recent study, focused on the digital personnel selection procedures and identified five dominant methods, including online applications, online psychometric testing, digital interviews, gamified assessment, and social media.

Since this study specifically focuses on personnel selection via the use of MCDM techniques, the literature review is focused on the recently published studies relevant to the subject matter. Thus, herein, forty-eight articles are examined in terms of criteria, solution methods, and application domains. While a summary of the complete list of studies is provided in Appendix Table A1, the most relevant and exemplary ones are also briefly explained in the following subsections.

## 2.1. Use of criteria and MCDM methods in personnel selection

In this section, we summarize the most relevant personnel selection studies, organized by application domain. The information technology industry is one of the most active sectors that used a variety of MCDM techniques in personnel selection. For instance, Chen [28] applied the fuzzy Technique for Order Preference by Similarity to an Ideal Solution (TOPSIS) method to evaluate candidates for the purpose of increasing overall productivity. Likewise, Mahdavi et al. [75] and Sang et al. [100] developed an analytical solution using fuzzy TOPSIS to obtain the most efective results for employee recruitment. Similarly, Canós and Liem (2008) proposed a soft computing-based aggregation method for human resource management. Chen et al. [29] developed a hybrid systematic decision-making model, which was a two-phase personnel recruitment decision support model to deal with the personnel selection efectively and eficiently. Similarly, Nabeeh et al. [80] applied Neutrosophic Analytic Hierarchy Process (N-AHP) based TOPSIS method to the personnel selection problem.

In the education sector, Jessop [53] specified weights for the personnel selection problem using Jaynes' principle of maximum entropy in case of few applicants. Saghafian and Hejazi [96] developed a model by using a modified fuzzy TOPSIS method for the academy. Gibney and Shang [43] benefited from the advantages of the AHP method, leading to efective personnel evaluation. Alguliyev et al. (2015) evaluated staf by a modified fuzzy VIKOR model. Celik et al. (2009) took the benefits of aggregating AHP and TOPSIS methods in a fuzzy environment for the selection of the most suitable senior lecturers. Vatansever and Öncel (2014) combined the fuzzy AHP method with the fuzzy TOPSIS method. Saad et al. [95] introduced a new approach for the recruitment problem consisting of the hamming-distance method with subjective and objective weights (HDMSOW's.). Finally, Kumar et al. [65] proposed an integrated methodology consisting of Simple Additive Weighting (SAW), Weighted Product (WP), AHP and TOPSIS methods for the se lection of the best candidate for a given academic position.

In the health sector, Liao and Chang [68] used ANP to select the most matching public relations personnel of hospitals. Shih et al. [103] proposed a model combining AHP and TOPSIS methods, contributing to online manager recruitment. Similarly, in the tourism sector, Stanujkic et al. [105] established a model for personnel selection by using the Stepwise Weight Assessment Ratio Analysis (SWARA) and Addictive Ratio Assessment (ARAS) methods. Urosevic et al. [112] proposed a hybrid model including Weighted Aggregated Sum-Product Assessment (WASPAS) and SWARA techniques.

In the production sector, Majozi and Zhu [77] maximized plant performance using fuzzy set theory. Rashidi et al. [90] determined the critical criteria in selection through a fuzzy system based on IF-THEN rules with a genetic algorithm. Zavadskas et al. (2018) applied the complex proportional assessment of alternatives to grey relations (COPRAS-G) for the selection of a project manager. Jasemi and Ahmadi [52] developed a new fuzzy ELECTRE based methodology for the personnel selection problem. Varajão and Cruz-Cunha [113] proposed a hybrid model based on AHP, and in the telecommunication sector, Kusumawardani and Agintiara [66] proposed the use of the Fuzzy AHP-TOPSIS method to personnel selection problem.

In the energy sector, Afshari et al. [4] and Ervural et al. [37] de veloped models based on fuzzy integrals for ranking applicants. Afshari et al. [2] built a linguistic fuzzy MCDM. They deduced that the model was able to evaluate candidates in a subjective manner and generally yielded more robust results in human resources problems. However, hybrid models are also used in this industry. Afshari et al. [3] proposed a model by using fuzzy linguistic variables, fuzzy simple additive weighting (SAW), and Delphi method. In the electric & electronics sector, Lin [70] used an integrated methodology comprising of ANP and fuzzy data envelopment analysis (fuzzy DEA) to cope with the personnel selection problem. Chen et al. [30] developed a model for per sonnel selection utilizing linguistic VIKOR. In the chemistry sector, Chen et al. [31] used a hybrid approach combining OWA and TOPSIS methods.

In the food and beverage industry, Zolfani et al. [125] established a model based on AHP and COPRAS-G. Chaghooshi et al. [27] merged fuzzy DEMATEL and fuzzy VIKOR. In the textile sector, integrated methods were used. Huang et al. [51] proposed a tool combining biobjective binary integer programming and fuzzy set theory with goal programming to select the best matching candidate. Ozdemir [81] used AHP with stochastic dynamic programming for personnel selection in the marketing department. In the military sector, Kabak et al. [57] constructed a fuzzy hybrid multicriteria decision-making tool via ANP, TOPSIS, and ELECTRE within a fuzzy environment. In the automotive sector, Saremi et al. [101] applied fuzzy TOPSIS to the Total Quality Management (TQM) consultant selection problem. In the banking and finance sector, Polychroniou and Giannikos [87] used the TOPSIS method for employee selection. They investigated the applicability of TOPSIS using actual data from a major Greek bank. Finally, in the security sector, Kosareva et al. [63] presented a model via KEmeny Median Indicator Rank Accordance (KEMIRA) technique. They inferred that the proposed method enabled them to weigh and amalgamate subjective and objective indicators. Besides the studies that included within specific sectors, there also are studies where the sector information is not stated explicitly. For instance, Salehi [97] proposed an integrated methodology, including F-AHP and F-VIKOR, in such a sector-neutral study. Similarly, Petridis et al. [85] collectively used the integration of AHP, TOPSIS, and non-linear programming models for the personnel selection problem.

Considering the reviewed studies, the criteria used for personne selection assumes a significant role in the selection process. There exist various criteria that are used for diferent job positions. However, based on the literature analyzed in this study, eleven diferent general criteria groups are determined as outstanding; these are knowledge and experience, personal characteristics and skills, education, foreign language, physical wellness and demographic features, salary request, vocational flexibility and capability, references, oral assessment, exam results and school reputation, technical skills, and requirements. Criteria found in the papers reviewed are grouped together with respect to the above listed eleven main criteria and provided in Appendix Table A1. According to the results, the most frequently used criterion is the personal characteristics and skills (used in 87.5% of the forty-eight studies analyzed). The other most frequently used criteria are knowledge and experience, technical skills and requirements, education, and foreign language. The relative percentages of the criteria are shown as a bar chart in Fig. 1.

Besides the criteria, the methods used to conduct the MCDM also play an essential role in the portrayal of personnel selection. Based on the analyzed studies, the most frequently used five methods are determined as Fuzzy TOPSIS, TOPSIS, AHP, Fuzzy Modelling, and Fuzzy AHP. Moreover, the sectoral representations in the extant literature are also determined. Based on the results, the top five sectors emerged as Education, Information Technology (IT), Production, Health, and Military.

As can be inferred from this collection of studies, the use of MCDM methods in personnel selection has been a highly active and equally popular research area for a long time in virtually any sector, primarily due to the complexity of the problem and the criticality of the outcome for the organizations. Although there have been numerous studies in this field, there is still ample room for further research, as is the case for the current study that approaches the problem from a more realistic perspective by including the fuzzy nature of the constructs involved in the decisioning process.

![](/api/attachments/HPEJDPHV/fulltext/images/44522527bce92b1f98a98a70ef8c9de84987f9e69824358dc21103c49b1922e0.jpg)  
Fig. 1. The percentages of the personnel selection criteria.

Table 1  
The analysis of the studies concerning criteria, alternatives, and evaluation type.

<table><tr><td rowspan="3">Author/subject</td><td colspan="4">Interactive criteria</td><td colspan="4">Outranking alternatives</td><td colspan="4">Evaluation Type</td></tr><tr><td colspan="2">ANP</td><td colspan="2">DEMATEL</td><td colspan="2">ELECTRE</td><td colspan="2">PROMETHEE</td><td colspan="2">CARDINAL</td><td colspan="2">ORDINAL</td></tr><tr><td>Crisp</td><td>Fuzzy</td><td>Crisp</td><td>Fuzzy</td><td>Crisp</td><td>Fuzzy</td><td>Crisp</td><td>Fuzzy</td><td>Crisp</td><td>Fuzzy</td><td>Crisp</td><td>Fuzzy</td></tr><tr><td>Tuzkaya et al. [111]/Material handling equipment selection</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Cakin and Ozdemir [21]/Supplier selection</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Govindan et al. [46]/Evaluation of green manufacturing practices</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Ehsan et al. [35]/Supplier selection</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Fetanat and Khorasaninejad [39]/Offshore wind farm site selection</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td></tr><tr><td>Hanane et al. (2015)/Supplier selection</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Kilic et al. [62]/ERP system selection</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Dincer et al. (2016)/Appraisal of agriculture banking</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Khorasaninejad et al. [60]/Prime mover selection in thermal power plant</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Peker [84]/Logistics social responsibility evaluation</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Samanlioglu and Ayag (2016)/Selection of machine tool</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Sari and Timor [102]/Supplier selection</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Gür et al. [49]/Selection of marketing strategies</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Kabadayi and Dag [55]/Machine selection</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Özcan et al. [82]/Selection of solar power plants</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Rahimi and Najafi [88]/Analysis of customer&#x27;s expectations and satisfaction</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td></tr><tr><td>Bongo et al. [12]/Identification of main stressors for air traffic controllers&#x27; workload</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Ozturk et al. (2018)/Supplier selection</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Demirci and Kilic (2019)/Personnel selection</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Kabadayi and Dag [56]/Performance evaluation in supply chain</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>THIS STUDY</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td></tr></table>

## 2.2. The integrated use of IF-DEMATEL and IF-ELECTRE: reasons and contributions

As stated by Gölcük and Baykasoğlu [47], although most of the MCDM methods assume that the criteria are independent, this is not usually true in real-world problems. One example of this can be ob served in the personnel selection problem, where there are interactions between the criteria, and this should be considered in the employed methodology. Considering the extant literature, two main techniques, namely ANP and DEMATEL, are applied to mitigate the interdependencies problem (see Table 1), and hence, gained broad acceptance. There is no discerning evidence that suggests one technique is always superior to the other in the literature. Depending on the conditions of the specific case, the choice can difer. Within the scope of our problem, DEMATEL, with the intuitionistic fuzzy version, is found to be more suitable since it overcomes the fuzziness in the decisionmaking environment and reflects the hesitancy of the decision-makers [121]. Furthermore, DEMATEL technique is considered to be a more practical technique to use in this study by also relying on its successful application in 346 studies between 2006 and 2016 in various sectors [104].

After determining the importance of the criteria, in the second stage of the personnel selection problem, outranking methods are considered as the suitable tools for collectively assessing the competing candidates in the personnel selection problem by evaluating the ordinal ranking that exists between the alternatives [58]. Among the outranking methods, the most efective and most commonly used techniques are PROMETHEE and ELECTRE [15,115]. Therefore, they are considered as potential solution methods herein. Although there is no consensus on the best of the two, as they both have their pros and cons. It is then clear that depending on the characteristics of the problem, the suitable technique needs to be identified and used. Regarding the personnel selection problem, IF-ELECTRE method is chosen because it helps to overcome the fuzziness in the decision-making environment, considers the hesitancies of the decision-makers, and provides the evaluation of both cardinal and ordinal evaluations of the alternatives. Moreover, the utilization of the ELECTRE technique in more than 500 studies within the last fifty years also provides credibility and motivation for choosing this technique.

To clarify the novelty of the proposed methodology within the extand literature, Table 1 is prepared. The studies having a similar structure as in this study are analyzed concerning interactive criteria, outranking alternatives, and evaluation type, and it is inferred that this is the first study utilizing IF-DEMATEL and IF-ELECTRE, including both fuzzy cardinal and ordinal evaluations for the personnel selection problem.

## 3. The proposed methodology

The integrated methodology proposed in this study consists of three main stages: Preparation, IF-DEMATEL, and IF-ELECTRE. Within the first stage (i.e., Preparation), the criteria that will be used in the personnel selection process, potential candidates, and the decision-makers (knowledge sources and/or evaluators) are determined. In the second stage, the IF-DEMATEL technique is formulated and applied to calculate the importance weights of all criteria. In the third and final stage, IF-ELECTRE is used to calculate and rank the candidates. A pictorial depiction of the proposed methodology, along with the detailed grouping of activities in the three consecutive stages, is given in Fig. 2.

## 3.1. IF-DEMATEL

DEMATEL method was developed by Gabus and Fontela [41] and used for revealing the mutual relationships among the criteria. Because of its strength in the analysis of interactions between factors, DEMATEL has been widely used for various problems including the determination of the website design parameters' importance [26], evaluation of the factors influencing the adoption of RFID [72], and evaluation of the green supply chain management performance [59]. However, DE-MATEL is known to be insuficient in handling uncertainty and vagueness that exists in many real-world MCDM situations, including the personnel selection problem. Hence, in this study, IF-DEMATEL is uti lized to provide the relative importance weights of the criteria, as the first stage in the proposed methodology. The steps involved in the IF-DEMATEL procedure are shown in Fig. 2. These steps are developed based on several previous studies, including Xie et al. [118], Büyü- közkan et al. [17] and Rahman et al. [89], and are provided in Appendix B with an explanatory table, Table B1, including the definitions of the abbreviations and symbols used within IF-DEMATEL steps.

![](/api/attachments/HPEJDPHV/fulltext/images/0487ab91096a580e1bf5c3cf0023b57cabccc20a7d33fcefe7344fbd5b3c7117.jpg)  
Fig. 2. The proposed integrated methodology.

## 3.2. IF-ELECTRE

ELECTRE method was developed by Benayoun et al. [11]. Since then, as stated by Govindan and Jepsen [45], various ELECTRE types have been proposed by a group of authors including “ELECTRE II (Roy and Bertier, 1971), ELECTRE III [93], ELECTRE IV (Roy and Hugonnard, 1982), ELECTRE TRI [94,123], ELECTRE IS [94], ELECTRE TRI-B [40], ELECTRE TRI-C [5] and ELECTRE TRI-nC [6]”. ELECTRE technique has been used in various decision analysis problems [45] including the ranking of British universities [42], ranking the relative competitiveness of regions [38], benchmarking the European Union member countries with respect to Digital Agenda key performance targets [86] and selection of the sites for renewable energy [36]. Different from the crisp ELECTRE method, which is based on outranking relations using the concordance and discordance indexes [79], IF-ELECTRE can consider the uncertainty and vagueness that exist in the structure of the problem, and hence, after obtaining the importance weights of the criteria as the outputs of IF-DEMATEL method, IF-ELECTRE is employed to rank the potential candidates. The steps of IF-ELECTRE are provided in Appendix C; however, before explaining the steps, the transformation process from ordinal evaluation to IF-evaluations warrants clarification [117].

In real-world practice, it is not always possible to obtain a cardinal evaluation where exact numerical values are assigned to the scoring of the criteria, and in such cases, ordinal evaluations which are based on the ranking data of alternatives can be chosen and performed. In this case, the rankings of the alternatives are determined, and Eqs. 1 and 2 are executed to calculate the membership (μ ) and non-membership (v ) values corresponding to the rankings. Therein, $\alpha _ { i j }$ indicates the number of alternatives that the $i ^ { \mathrm { { t h } } }$ alternative is better concerning the criterion j. Similarly, $\beta _ { i j }$ indicates the number of alternatives that are better than the i<sup>th</sup> alternative concerning the criterion j.

$$
\mu_ {i j} = \frac {\alpha_ {i j}}{m - 1}\tag{1}
$$

$$
v _ {i j} = \frac {\beta_ {i j}}{m - 1}\tag{2}
$$

The steps of the IF-ELECTRE method are provided in Appendix C [117]. Moreover, the definitions of the abbreviations and symbols are provided in advance, as in Appendix Table C1.

## 4. An application case for the proposed methodology

To demonstrate the implementation of the personnel selection process and to illustrate the viability of the proposed methodology, an application case is designed and executed. In this application case, an air filter manufacturing company is used. The specific problem was characterized as selecting and hiring the most suitable industrial engineer from the existing candidate pool. The company, at which the application is performed, focuses on the production of various types of air filters, including roll filters, panel filters, bag filters, and compact filters. The company has been a player in the sector for about ten years and growing rapidly with new investments to satisfy the continuously increasing customer demand. As a result of this growth, new personnel is required to be hired in various departments to keep up with the growing workload. To simplify the demonstration of the proposed methodology, in this application case, we focused on only one of the real personnel selection scenarios: the selection of an industrial engineer for the manufacturing planning department. In the existing personnel evaluation system, there is not a systematic and scientific process to follow; instead, most of the personnel selection related decisions are made based on a few interviews by corresponding department supervisors and managers. Therefore, the goal of this study is to provide the decision-makers an objective, coherent, and systematic approach to select the most suitable candidate. The implementation of the related steps of the proposed methodology to the current application case are provided in the following subsections.

Table 2  
Decision-makers' intuitionistic judgments.

<table><tr><td>DM1</td><td>Cr1</td><td>Cr2</td><td>Cr3</td><td>Cr4</td><td>Cr5</td></tr><tr><td>Cr1</td><td>(0,1,0)</td><td>(0, 1, 0)</td><td>(0.9, 0.1, 0)</td><td>(0.75, 0.2, 0.05)</td><td>(0.9, 0.1, 0)</td></tr><tr><td>Cr2</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.75, 0.2, 0.05)</td><td>(0.75, 0.2, 0.05)</td><td>(0.5, 0.45, 0.05)</td></tr><tr><td>Cr3</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td></tr><tr><td>Cr4</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.35, 0.60, 0.05)</td><td>(0, 1, 0)</td><td>(0.35, 0.60, 0.05)</td></tr><tr><td>Cr5</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.35, 0.60, 0.05)</td><td>(0.35, 0.60, 0.05)</td><td>(0, 1, 0)</td></tr><tr><td>DM2</td><td>Cr1</td><td>Cr2</td><td>Cr3</td><td>Cr4</td><td>Cr5</td></tr><tr><td>Cr1</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.9, 0.1, 0)</td><td>(0.9, 0.1, 0)</td><td>(0.9, 0.1, 0)</td></tr><tr><td>Cr2</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.75, 0.2, 0.05)</td><td>(0.75, 0.2, 0.05)</td><td>(0.35, 0.60, 0.05)</td></tr><tr><td>Cr3</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td></tr><tr><td>Cr4</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.35, 0.60. 0.05)</td><td>(0, 1, 0)</td><td>(0.35, 0.60, 0.05)</td></tr><tr><td>Cr5</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.5, 0.45, 0.05)</td><td>(0.35, 0.60, 0.05)</td><td>(0, 1, 0)</td></tr><tr><td>DM3</td><td>Cr1</td><td>Cr2</td><td>Cr3</td><td>Cr4</td><td>Cr5</td></tr><tr><td>Cr1</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.9, 0.1, 0)</td><td>(0.9, 0.1, 0)</td><td>(0.75, 0.2, 0.05)</td></tr><tr><td>Cr2</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.75, 0.2, 0.05)</td><td>(0.5, 0.45, 0.05)</td><td>(0.5, 0.45, 0.05)</td></tr><tr><td>Cr3</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td></tr><tr><td>Cr4</td><td>(0, 1, 0)</td><td>(0,1, 0)</td><td>(0.35, 0.60, 0.05)</td><td>(0, 1, 0)</td><td>(0.35, 0.60, 0.05)</td></tr><tr><td>Cr5</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.5, 0.45, 0.05)</td><td>(0.35, 0.60, 0.05)</td><td>( 0, 1, 0)</td></tr></table>

## 4.1. Preparation stage

Within the preparation stage, the personnel selection criteria are determined via obtaining the views/options of the stakeholders (i.e., plant manager, production manager, and human resource manager) within the company and via a thorough review of the extant literature. At the end of this knowledge elicitation, acquisition, and consolidation process, the specific criteria to use in this application case are determined to be as follows:

• Education (Cr1)

• Experience (Cr2)

• Technical Skills (Cr3)

Personality and Personal Skills (Cr4)

• Foreign Language (Cr5)

Also, the top five most likely candidates that meet and exceed the minimum requirements are identified from the candidate pool to be included in this personnel evaluation and selection process. In this application case, these candidates are named as Cnd1, …, Cnd5.

## 4.2. IF-DEMATEL application stage

In the second stage of the proposed methodology, the IF-DEMATEL technique is utilized so as to obtain the relative importance weights of the criteria, which would be used as inputs into the IF-ELECTRE stage.

The three decision-makers consisting of the plant manager, production manager, and human resource manager, are consulted, and their opinions are gathered using the systematic process of IF-DEMATEL. The related steps, which were explained previously in the related section, are executed, and details of which are provided in the following sections:

Step 1: Provide the structure of the problem by indicating the objective, criteria, and sub-criteria. Since the structure of the problem is determined in the preparation stage, the requirements of Step 1 are already performed with the identification of the six criteria and five candidates.

Step 2: Determine the evaluation scale. To operationalize this step, we used the linguistic terms provided in Appendix Table B2.

Step 3: Prioritize the decision-makers(DMs)/experts. There are three decision-makers, and these decision-makers have somewhat diferent and conflicting opinions on importance values. Inputs of the plant manager (DM1) are considered as “very important” and the remaining decision-makers, which are the production managers (DM2) and human resource manager (DM3), are evaluated as “important”. The formula provided in Eq. 7 is utilized, and the importance weights of the decision-makers are determined as follows:

$$
\lambda_ {1} = \frac {\left(0 . 9 + 0 * \left(\frac {0 . 9}{0 . 9 + 0 . 1}\right)\right)}{\left(\left(0 . 9 + 0 * \left(\frac {0 . 9}{0 . 9 + 0 . 1}\right)\right) + 2 * \left(0 . 7 5 + 0 . 0 5 * \left(\frac {0 . 7 5}{0 . 7 5 + 0 . 2}\right)\right)\right)} = 0. 3 6,
$$

$$
\lambda_ {2} = \lambda_ {3} = 0. 3 2
$$

Step 4: Determine the intuitionistic judgments of each DM/expert and aggregate their preferences via the intuitionistic fuzzy weighted averaging operator (IFWA). Each decision-maker's intuitionistic judg ment is provided, as shown in Table 2.

IFWA operator, which is indicated in Eq. 9, is applied, and the aggregated intuitionistic fuzzy relation matrix is obtained as in Table 3.

Step 5: Defuzzify the aggregated intuitionistic fuzzy relation. The aggregated intuitionistic fuzzy relation matrix is defuzzified via Eq. 10, and the results of the operations are shown in Table 4.

Step 6: Normalize the defuzzified aggregated intuitionistic fuzzy relation matrix. The defuzzified aggregated intuitionistic fuzzy relation matrix is normalized via Eqs. 11–12, and the results of which are shown in Table 5.

Step 7: Calculate the total relation matrix. The total relation matrix is calculated via Eq. 13, and the results of which are shown in Table 6.

Step 8: Perform normalization. Normalization is executed via Eqs. 14–15, and the importance weights of the criteria are obtained, as shown in Table 7.

Table 3  
Aggregated intuitionistic fuzzy relation matrix.

<table><tr><td>Aggregated</td><td>Cr1</td><td>Cr2</td><td>Cr3</td><td>Cr4</td><td>Cr5</td></tr><tr><td>Cr1</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.9, 0.1, 0)</td><td>(0.86, 0.13, 0.01)</td><td>(0.86, 0.13, 0.01)</td></tr><tr><td>Cr2</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.75, 0.2, 0.05)</td><td>(0.68, 0.29, 0.03)</td><td>(0.45, 0.50, 0.05)</td></tr><tr><td>Cr3</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td></tr><tr><td>Cr4</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.35, 0.60, 0.05)</td><td>(0, 1, 0)</td><td>(0.35, 0.60, 0.05)</td></tr><tr><td>Cr5</td><td>(0, 1, 0)</td><td>(0, 1, 0)</td><td>(0.45, 0.50, 0.05)</td><td>(0.35, 0.60, 0.05)</td><td>(0, 1, 0)</td></tr></table>

Table 4  
The defuzzified aggregated intuitionistic fuzzy relation matrix.

<table><tr><td></td><td>Cr1</td><td>Cr2</td><td>Cr3</td><td>Cr4</td><td>Cr5</td></tr><tr><td>Cr1</td><td>-1</td><td>-1</td><td>0.8</td><td>0.73</td><td>0.73</td></tr><tr><td>Cr2</td><td>-1</td><td>-1</td><td>0.55</td><td>0.39</td><td>-0.05</td></tr><tr><td>Cr3</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td></tr><tr><td>Cr4</td><td>-1</td><td>-1</td><td>-0.25</td><td>-1</td><td>-0.25</td></tr><tr><td>Cr5</td><td>-1</td><td>-1</td><td>-0.05</td><td>-0.25</td><td>-1</td></tr></table>

Table 5  
The normalized defuzzified aggregated intuitionistic fuzzy relation matrix.

<table><tr><td></td><td>Cr1</td><td>Cr2</td><td>Cr3</td><td>Cr4</td><td>Cr5</td></tr><tr><td>Cr1</td><td>-0.2</td><td>-0.2</td><td>0.16</td><td>0.146</td><td>0.146</td></tr><tr><td>Cr2</td><td>-0.2</td><td>-0.2</td><td>0.11</td><td>0.078</td><td>-0.01</td></tr><tr><td>Cr3</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>-0.2</td></tr><tr><td>Cr4</td><td>-0.2</td><td>-0.2</td><td>-0.05</td><td>-0.2</td><td>-0.05</td></tr><tr><td>Cr5</td><td>-0.2</td><td>-0.2</td><td>-0.01</td><td>-0.05</td><td>-0.2</td></tr></table>

Table 6  
The total relation matrix.

<table><tr><td></td><td>Cr1</td><td>Cr2</td><td>Cr3</td><td>Cr4</td><td>Cr5</td></tr><tr><td>Cr1</td><td>-0.178</td><td>-0.178</td><td>0.090</td><td>0.069</td><td>0.084</td></tr><tr><td>Cr2</td><td>-0.150</td><td>-0.150</td><td>0.057</td><td>0.030</td><td>-0.036</td></tr><tr><td>Cr3</td><td>-0.077</td><td>-0.077</td><td>-0.176</td><td>-0.146</td><td>-0.140</td></tr><tr><td>Cr4</td><td>-0.104</td><td>-0.104</td><td>-0.057</td><td>-0.175</td><td>-0.037</td></tr><tr><td>Cr5</td><td>-0.107</td><td>-0.107</td><td>-0.030</td><td>-0.049</td><td>-0.172</td></tr></table>

Table 7  
The importance weights of the criteria.

<table><tr><td>Criteria</td><td>D</td><td>R</td><td>D + R</td><td>D-R</td><td>Criteria importance</td></tr><tr><td>Cr1 (Education)</td><td>-0.112</td><td>-0.616</td><td>-0.728</td><td>0.503</td><td>0.2073</td></tr><tr><td>Cr2 (Experience)</td><td>-0.249</td><td>-0.616</td><td>-0.865</td><td>0.367</td><td>0.2199</td></tr><tr><td>Cr3 (Technical skills)</td><td>-0.616</td><td>-0.118</td><td>-0.733</td><td>-0.498</td><td>0.2076</td></tr><tr><td>Cr4 (Personality and personal skills)</td><td>-0.478</td><td>-0.271</td><td>-0.749</td><td>-0.207</td><td>0.1819</td></tr><tr><td>Cr5 (Foreign language)</td><td>-0.465</td><td>-0.300</td><td>-0.766</td><td>-0.165</td><td>0.1833</td></tr></table>

## 4.3. IF-ELECTRE application stage

Once we obtained the relative importance weights of the criteria as the result of the IF-DEMATEL, method. next. the IF-ELECTRE method is performed to obtain the ranking of the candidates. Depending on the type of criterion, either cardinal and ordinal scorings need to be em ployed. In this application case, the cardinal scoring is performed for the “experience” and “language” criteria, and ordinal scoring is performed for “education,” “technical skills,” and “personality & personal skills.”

Regarding the cardinal evaluations of the experience and language criteria, we decided to use the scales and evaluations stated in Table 8.

Moreover, similar to the experience level, the evaluation scale fo language scoring is also determined similarly, and shown in Table 9.

Table 8  
Evaluation scale for experience level.

<table><tr><td>Experience level</td><td>IF Number</td></tr><tr><td>Very high experience (exp. &gt; 15 years)</td><td>[0.90, 0.10, 0]</td></tr><tr><td>High experience (10 &lt; exp. ≤ 15 years)</td><td>[0.75, 0.20, 0.05]</td></tr><tr><td>Medium experience (5 &lt; exp. ≤ 10 years)</td><td>[0.50, 0.45, 0.05]</td></tr><tr><td>Low experience (1 &lt; exp. ≤ 5 years)</td><td>[0.35, 0.60, 0.05]</td></tr><tr><td>Very low experience (exp. ≤ 1 year)</td><td>[0,1,0]</td></tr></table>

Table 9  
Evaluation scale for language level.

<table><tr><td>Language Score Level</td><td>IF Number</td></tr><tr><td>Very high language score (sc. &gt; 85 pts.)</td><td>[0.90, 0.10, 0]</td></tr><tr><td>High language score (75 &lt; sc. ≤ 85 pts.)</td><td>[0.75, 0.20, 0.05]</td></tr><tr><td>Medium language score (60 &lt; sc. ≤ 75 pts.)</td><td>[0.50, 0.45, 0.05]</td></tr><tr><td>Low language score (40 &lt; sc. ≤ 60 pts.)</td><td>[0.35, 0.60, 0.05]</td></tr><tr><td>Very low language score (sc. ≤ 40 pts.)</td><td>[0, 1, 0]</td></tr></table>

Table 10  
Scorings for experience and language levels.

<table><tr><td>Candidate</td><td>Experience</td><td>Language</td></tr><tr><td>A</td><td>[0.75, 0.20, 0.05]</td><td>[0.35, 0.60, 0.05]</td></tr><tr><td>B</td><td>[0.90, 0.10, 0]</td><td>[0.75, 0.20, 0.05]</td></tr><tr><td>C</td><td>[0.50, 0.45, 0.05]</td><td>[0.90, 0.10, 0]</td></tr><tr><td>D</td><td>[0.50, 0.45, 0.05]</td><td>[0.75, 0.20, 0.05]</td></tr><tr><td>E</td><td>[0.35, 0.60, 0.05]</td><td>[0.90, 0.10, 0]</td></tr></table>

Hence, the candidates are evaluated with respect to the provided scales and IF-Number scorings are indicated, as shown in Table 10.

Besides cardinal evaluation, there is the ordinal evaluation of some of the criteria, including education, technical skills, and personality & personal skills. The ordinal evaluations of the candidates with respect to the related criteria are shown in Table 11.

Based on Eqs. 1 and 2, the transformation of ordinal evaluations to intuitionistic fuzzy values are calculated, and the results of which are shown in Table 12

After obtaining the cardinal and ordinal evaluations of the candidates with respect to the criteria, the related IF-ELECTRE method (and its individual steps) is performed as follows:

Step 1: Determining the concordance and discordance sets. The concordance and discordance sets, including the main, midrange, and weak ones, are obtained by operationalizing Eqs. 16–21, and the results of the execution are shown in Tables 13 and 15.

## Table 11

Ordinal evaluations of the three criteria.

<table><tr><td>Candidates</td><td>Education</td><td>Technical Skills</td><td>Personality &amp; Personal Skills</td></tr><tr><td>A</td><td>4</td><td>1</td><td>2</td></tr><tr><td>B</td><td>2.5</td><td>3.5</td><td>1</td></tr><tr><td>C</td><td>1</td><td>3.5</td><td>3</td></tr><tr><td>D</td><td>2.5</td><td>5</td><td>4.5</td></tr><tr><td>E</td><td>5</td><td>2</td><td>4.5</td></tr></table>

Table 12  
Intuitionistic fuzzy values for ordinal evaluations.

<table><tr><td>Candidates</td><td>Education</td><td>Technical Skills</td><td>Personality &amp; Personal Skills</td></tr><tr><td>A</td><td>[0.25, 0.75, 0]</td><td>[1,0,0]</td><td>[0.75, 0.25, 0]</td></tr><tr><td>B</td><td>[0.50, 0.25, 0.25]</td><td>[0.25, 0.50, 0.25]</td><td>[1, 0, 0]</td></tr><tr><td>C</td><td>[1, 0, 0]</td><td>[0.25, 0.50, 0.25]</td><td>[0.5, 0.5, 0]</td></tr><tr><td>D</td><td>[0.50, 0.25, 0.25]</td><td>[0, 1, 0]</td><td>[0, 0.75, 0.25]</td></tr><tr><td>E</td><td>[0, 1, 0]</td><td>[0.75, 0.25, 0]</td><td>[0, 0.75, 0.25]</td></tr></table>

Table 13  
Main, midrange, and weak concordance sets.

<table><tr><td>Main concordance</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>A</td><td>-</td><td>3</td><td>3</td><td>4</td><td>4</td></tr><tr><td>B</td><td>2</td><td>-</td><td>2</td><td>2, 4</td><td>2, 4</td></tr><tr><td>C</td><td>5</td><td>1, 5</td><td>-</td><td>1, 4, 5</td><td>4</td></tr><tr><td>D</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>E</td><td>5</td><td>3, 5</td><td>3</td><td>5</td><td>-</td></tr><tr><td>Midrange Concordance</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>A</td><td>-</td><td>-</td><td>2, 4</td><td>2, 3</td><td>1, 2, 3</td></tr><tr><td>B</td><td>1, 4, 5</td><td>-</td><td>4</td><td>3</td><td>1</td></tr><tr><td>C</td><td>1</td><td>-</td><td>-</td><td>3</td><td>1, 2</td></tr><tr><td>D</td><td>1, 5</td><td>-</td><td>-</td><td>-</td><td>1, 2</td></tr><tr><td>E</td><td>-</td><td>-</td><td>-</td><td>3</td><td>-</td></tr><tr><td>Weak Concordance</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>A</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>B</td><td>-</td><td>-</td><td>3</td><td>1, 5</td><td>-</td></tr><tr><td>C</td><td>-</td><td>3</td><td>-</td><td>2</td><td>5</td></tr><tr><td>D</td><td>-</td><td>1, 5</td><td>2</td><td>-</td><td>4</td></tr><tr><td>E</td><td>-</td><td>-</td><td>5</td><td>4</td><td>-</td></tr></table>

Table 14  
Concordance matrix.

<table><tr><td>Concordance Matrix</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>A</td><td>-</td><td>0.2076</td><td>0.4755</td><td>0.4669</td><td>0.6051</td></tr><tr><td>B</td><td>0.6016</td><td>-</td><td>0.4104</td><td>0.6704</td><td>0.5400</td></tr><tr><td>C</td><td>0.3215</td><td>0.4598</td><td>-</td><td>0.7842</td><td>0.5278</td></tr><tr><td>D</td><td>0.2604</td><td>0.1302</td><td>0.0733</td><td>-</td><td>0.3454</td></tr><tr><td>E</td><td>0.1833</td><td>0.3909</td><td>0.2687</td><td>0.3823</td><td>-</td></tr></table>

Based on Eq. (22) (with $\mathsf { w } _ { \mathrm { C } } = 1 , \mathsf { w } _ { \mathrm { C } } , = 0 . 6 7$ and $\mathbf { w } _ { \mathbf { C } ^ { \prime \prime } } = 0 . 3 3 )$ , the concordance matrix is constructed and shown in Table 14  
Based on Eqs. 23 and 24 (with $\mathbf { w _ { D } } = 1$ , w = 0.67 and $\mathbf { w _ { D } } \mathrm { , } = 0 . 3 3 )$ , the discordance matrix is constructed and shown in Table 16  
Step 2: Obtaining the concordance and discordance dominance

Table 15  
Main, midrange, and weak discordance sets.

<table><tr><td>Main Discordance</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>A</td><td>-</td><td>2, 4, 5</td><td>1, 5</td><td>5</td><td>5</td></tr><tr><td>B</td><td>3</td><td>-</td><td>1, 5</td><td>-</td><td>3, 5</td></tr><tr><td>C</td><td>2, 3, 4</td><td>2, 4</td><td>-</td><td>-</td><td>3</td></tr><tr><td>D</td><td>2, 3, 4</td><td>2, 4</td><td>1, 4, 5</td><td>-</td><td>3, 5</td></tr><tr><td>E</td><td>1, 2, 3, 4</td><td>2, 4</td><td>1, 2, 4</td><td>2</td><td>-</td></tr><tr><td>Midrange Discordance</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>A</td><td>-</td><td>1</td><td>-</td><td>1</td><td>-</td></tr><tr><td>B</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>C</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>D</td><td>-</td><td>3</td><td>3</td><td>-</td><td>-</td></tr><tr><td>E</td><td>-</td><td>1</td><td>-</td><td>1</td><td>-</td></tr><tr><td>Weak Discordance</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>A</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>B</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>C</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>D</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>E</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Table 16  
Discordance matrix.

<table><tr><td>Discordance Matrix</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>A</td><td>-</td><td>0.6048</td><td>1.0000</td><td>0.4000</td><td>0.7965</td></tr><tr><td>B</td><td>1.0000</td><td>-</td><td>0.8660</td><td>0.0000</td><td>0.4803</td></tr><tr><td>C</td><td>0.8819</td><td>1.0000</td><td>-</td><td>0.0000</td><td>0.4330</td></tr><tr><td>D</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>-</td><td>1.0000</td></tr><tr><td>E</td><td>1.0000</td><td>1.0000</td><td>1.0000</td><td>0.5879</td><td>-</td></tr></table>

Table 17  
Concordance and discordance dominance matrixes.

<table><tr><td>Concordance Dominance</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>A</td><td>-</td><td>0.5766</td><td>0.3087</td><td>0.3173</td><td>0.1791</td></tr><tr><td>B</td><td>0.1826</td><td>-</td><td>0.3738</td><td>0.1138</td><td>0.2442</td></tr><tr><td>C</td><td>0.4627</td><td>0.3244</td><td>-</td><td>0.0000</td><td>0.2564</td></tr><tr><td>D</td><td>0.5238</td><td>0.6540</td><td>0.7109</td><td>-</td><td>0.4388</td></tr><tr><td>E</td><td>0.6009</td><td>0.3933</td><td>0.5155</td><td>0.4019</td><td>-</td></tr><tr><td>Discordance Dominance</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>A</td><td>-</td><td>0.3952</td><td>0.0000</td><td>0.6000</td><td>0.2035</td></tr><tr><td>B</td><td>0.0000</td><td>-</td><td>0.134</td><td>1.0000</td><td>0.5197</td></tr><tr><td>C</td><td>0.1181</td><td>0.0000</td><td>-</td><td>1.0000</td><td>0.5670</td></tr><tr><td>D</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>-</td><td>0.0000</td></tr><tr><td>E</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.4121</td><td>-</td></tr></table>

matrix. After determining the concordance and discordance sets, the dominance matrixes are calculated with respect to Eqs. 25 and 26, and the results of which are shown in Table 17.

Step 3: Obtaining the aggregate dominance matrix. The aggregate dominance matrix is constructed by consolidating the concordance and discordance dominance matrixes by utilizing Eq. 27, and the results of which are shown in Table 18

Each candidate's dominance values over the other candidates are also shown as a stacked bar chart in Fig. 3. It can be seen, the total dominance value of candidate C is the biggest, while candidate D has no dominance over the other candidates. Moreover, when individually analyzed, it is seen that candidates A, B, C, and E have their highest dominance values over alternative D, which is the least dominant candidate. Finally, candidate C is the alternative that the other candidates have the least dominance over.

Step 5: Obtaining the final ranking of the candidates. The final ranking of the candidates is obtained via performing Eq. 28. The T values are calculated and sorted from highest to the smallest to obtain the ranking of the candidates, as shown in Table 19.

As can be inferred from Table 19, according to the proposed evaluation and selection methodology, candidate C (i.e., Cnd3) is the best of the five included in the process, and objectively and rationally speaking, should be the one to hire.

## 5. Results and discussion

In this section, a comparison is performed by utilizing crisp versions of DEMATEL and ELECTRE. Moreover, IF-DEMATEL is utilized with various hesitancy values, and its changing efects are analyzed. Finally, the results of the proposed methodology are elaborated in detail via a sensitivity analysis to assess the changing importance weights of the

Table 18  
Aggregate dominance matrix.

<table><tr><td>Aggregate dominance matrix</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>A</td><td>-</td><td>0.4067</td><td>0.0000</td><td>0.6541</td><td>0.5319</td></tr><tr><td>B</td><td>0.0000</td><td>-</td><td>0.2639</td><td>0.8978</td><td>0.6803</td></tr><tr><td>C</td><td>0.2033</td><td>0.0000</td><td>-</td><td>1.0000</td><td>0.6886</td></tr><tr><td>D</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>-</td><td>0.0000</td></tr><tr><td>E</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.5063</td><td>-</td></tr></table>

![](/api/attachments/HPEJDPHV/fulltext/images/de168105cc041237cfbb56ee371e991a3ae792a6fe21041b4c8befd973ab7aff.jpg)  
Fig. 3. Dominance value of each candidate over the other candidates.

Table 19  
The final ranking of the candidates.

<table><tr><td>Candidates</td><td>T values</td><td>Rank</td></tr><tr><td>A</td><td>0.3982</td><td>3</td></tr><tr><td>B</td><td>0.4605</td><td>2</td></tr><tr><td>C</td><td>0.4730</td><td>1</td></tr><tr><td>D</td><td>0.0000</td><td>5</td></tr><tr><td>E</td><td>0.1266</td><td>4</td></tr></table>

criteria.

## 5.1. Comparison with crisp DEMATEL and ELECTRE

The conventional DEMATEL, which is based on crisp evaluations, is also performed to realize the diferences between the obtained im portance weights of the criteria. Since the steps of the crisp and the intuitionistic fuzzy versions of DEMATEL are diferent, it is not ex pected to find the same importance weights, as seen in Fig. 4. The biggest diferences are obtained in the first and second criteria. However, the importance weights of the last three criteria came out as almost the same.

Moreover, diferent from the determined hesitancy value (0.05 in this study), the IF-DEMATEL method is applied with the hesitancy values of 0.10, 0.15, and 0.20. The results are shown in Fig. 5. When the hesitancy value changes, so do the importance weights, collectively indicating the existence of a monotonous trend within all the criter ia—while the first three criteria increase with chacing hesitancy values, showing a positive trend, the last two criteria decrease. Also, the standard deviation of criteria importance weights is calculated as 0.0149, 0.0164, 0.0179, and 0.0195, respectively. It is observed that the standard deviation increased with the increase in the hesitancy value for the considered case.

Similar to the comparison of crisp DEMATEL to IF-DEMATEL, crisp ELECTRE is also applied by utilizing the steps provided in the study of Yoon and Hwang [122]. As indicated in Table 20, there is a tie for the first rank between the candidates 2 and 3. However, the third, fourth, and fifth ranks belong to the same candidates as in IF-ELECTRE.

Besides, IF-TOPSIS is also applied to the same problem by utilizing the steps provided in the studies of Cavallaro et al. [25] and Kilic and Yalcin [61]. Since IF-TOPSIS is a distance-based technique, its structure is principally diferent from IF-ELECTRE, which has an outranking approach. Hence, diferent rankings are obtained for the first three positions, as seen in Table 21. However, the closeness coeficient (CC) values of the candidates having the first three ranks are observed to be very similar to each other. The last two ranks came out to be the same as in IF-ELECTRE.

To reveal the relationship between the rankings obtained from IF-ELECTRE and the other techniques, including crisp ELECTRE and IF-TOPSIS, Spearman's correlation coeficient of ranks, which gives the relationship degree between two ranked data, is obtained by applying the formulation provided in Eq. 3 [74]. Hence, it is found that between IF-ELECTRE and crisp ELECTRE, the correlation value is 0.975, which can be stated as a very strong relationship. Whereas, between IF-ELECTRE and IF-TOPSIS, it is obtained to be 0.7, which can be considered as a strong relation. Hence, it can be deduced that both values support the validation of the proposed technique.

$$
r _ {s} = 1 - \frac {6 \sum d ^ {2}}{n (n ^ {2} - 1)}\tag{3}
$$

![](/api/attachments/HPEJDPHV/fulltext/images/0e7687f4612f9f246b6ae1de92473dad2a6800a46b5ba56e8e6484c80b0e5c95.jpg)  
Fig. 4. Comparison of Crisp DEMATEL and IF-DEMATEL

![](/api/attachments/HPEJDPHV/fulltext/images/561805554634cd2e2000ba11bbc705fc3e34560e190102c67e07c34679673c80.jpg)  
Fig. 5. IF-DEMATEL results for various hesitancy values.

Table 20  
Crisp ELECTRE results.

<table><tr><td>Candidates</td><td>Cp</td><td>Cp rank</td><td>Dp</td><td>Dp rank</td><td>Final rank</td></tr><tr><td>A</td><td>0.490</td><td>3</td><td>-0.813</td><td>3</td><td>3</td></tr><tr><td>B</td><td>1.424</td><td>1</td><td>-1.352</td><td>2</td><td>1.5</td></tr><tr><td>C</td><td>0.949</td><td>2</td><td>-1.738</td><td>1</td><td>1.5</td></tr><tr><td>D</td><td>-1.574</td><td>5</td><td>3.287</td><td>5</td><td>5</td></tr><tr><td>E</td><td>-1.289</td><td>4</td><td>0.616</td><td>4</td><td>4</td></tr></table>

Table 21

IF-TOPSIS results.

<table><tr><td></td><td>S*</td><td>S-</td><td>CC</td><td>Rank</td></tr><tr><td>A1</td><td>0.561</td><td>0.464</td><td>0.453</td><td>2</td></tr><tr><td>A2</td><td>0.547</td><td>0.475</td><td>0.465</td><td>1</td></tr><tr><td>A3</td><td>0.576</td><td>0.468</td><td>0.448</td><td>3</td></tr><tr><td>A4</td><td>0.733</td><td>0.122</td><td>0.143</td><td>5</td></tr><tr><td>A5</td><td>0.722</td><td>0.162</td><td>0.183</td><td>4</td></tr></table>

## 5.2. Sensitivity analysis

A sensitivity analysis is performed via IF-ELECTRE, considering each criterion for the importance weights of 0.1, 0.3, and 0.5 in dividually. The analysis for the first criterion is shown in Fig. 6, and the rest is provided in Appendix D with Figs. D1-D4.

In total, fifteen scenarios are analyzed. In 60% of the scenarios, the ranking is as C-B-A-E-D; in 33.33% of the scenarios, the ranking of the first and second candidates exchange compared to the previous ranking with the final ranking of B-C-A-E-D. Lastly, in 6.67% of the scenarios, the ranking is as A-B-C-E-D. This scenario indicates that when the third criterion (i.e., Technical skills) has an importance weight of 0.5, can didate A should be selected. Considering all the scenarios, candidate C seems to have superiority over the other candidates. Moreover, candidate B also has the chance to be the first, especially when the criterion 2 (Experience) or criterion 4 (Personality and personal skills) have rela. tively high importance weights.

In addition to the sensitivity analysis, the importance weights ob tained from the application of crisp DEMATEL are also used in the IF-ELECTRE method. However, as can be seen in Table 22, which also includes “T values,” the ranking has not changed.

## 6. Summary and conclusions

Personnel selection is a challenging problem and a significant organizational matter due to the potential benefits obtained from making the right choices and equally damaging efects incurred from making the wrong choices. Inaccurate personnel selection decisions can lead to serious problems for the company in the long run. For instance, if the intrinsic characteristics of the recruited personnel do not match the job requirements and specifications, then the decision is deemed to be irrational, non-objective, and far from being an optimal choice. In the end, the wrong choices may lead to a multitude of problems, including the need for extra training, lower productivity/throughput, an increase in occupational incidents/accidents, and low morale among coworkers/ employees in the system. In essence, the wrong choices lead to both loss of money (financial means) and waste of precious time, thereby negatively afecting the organization's success and competitive posture. For these reasons, the selection of the best possible candidates through a scientific and systematic methodology is a necessity.

In this study, an integrated MCDM methodology that does not exist in the extant literature is developed and demonstrated. The proposed methodology is designed to benefit from the synergistic use of DEMATEL and ELECTRE methods, both of which under the enhanced intuitionistic fuzzy environmental constraints. Within the proposed methodology, after determining the related personnel selection criteria based on literature review and expert opinions, the importance weights of the associated criteria are calculated by the IF-DEMATEL method, and candidates are ranked by IF-ELECTRE method based on both car dinal and ordinal evaluations of all possible candidates.

An application case is performed in a manufacturing company so as to validate the proposed methodology. The proposed methodology is not specific to only human resource management or an application domain (a sector); rather, it can be used for any MCDM problems and sectors because of its easily generalizable framework for rational de cision modelling and characterization.

Such a decision support system that helps decision-makers in objectively and rationally identify and hire the best candidate out of the pool of candidates can make the personnel selection problem a straightforward, scientific, systematic, and practical organizational process. Hence, this study contributes to the extant literature theoretically by proposing a new integrated hybrid methodology capable of handling imprecise/fuzzy decision constructs. More specifically, this study can be regarded as the first study utilizing the integrated use of IF-DEMATEL and IF-ELECTRE, considering both cardinal and ordinal

![](/api/attachments/HPEJDPHV/fulltext/images/3b3165c7d28299fc75a2e5edeaffe5a344c80371981fba622dfdcc2138e6c670.jpg)  
Fig. 6. The sensitivity analysis concerning criterion 1.

Table 22  
The final ranking of the candidates when “Crisp DEMATEL” is used.

<table><tr><td>Candidates</td><td>T values</td><td>Rank</td></tr><tr><td>A</td><td>0.3724</td><td>3</td></tr><tr><td>B</td><td>0.4240</td><td>2</td></tr><tr><td>C</td><td>0.4639</td><td>1</td></tr><tr><td>D</td><td>0.0000</td><td>5</td></tr><tr><td>E</td><td>0.1227</td><td>4</td></tr></table>

evaluations within the personnel selection process. Beyond these contributions, the study is also subject to some limitations. One of the limitations is that the number of alternatives and criteria considered in the application is relatively small. For a larger case study, the computational operations and their explanations would be rather lengthy and hard to follow. The methodology, however, can be applied to problems of any size and level of complexity. For practical reasons, a userfriendly software of the proposed methodology can be developed for the entrance of the required data and the reporting of the results. Another limitation of the study is the simplicity of the method used for gathering the data/information from the experts. Since the number of experts considered for this case was three, and they were all working in the same location, a simplified, straightforwards interview method is deemed to be appropriate. However, when the number of experts increases, their world views significantly difer, and they are geographically far apart from each other, a Delphi-based method can be more appropriate. Further studies can include the consideration of how multiple candidates with diferent skill sets support or compete against one another in the personnel selection process, and the extensions and applications of the proposed methodology in various decision-making problems and application domains can be handled.

## Appendix A. Appendix

## Table A1

Literature review table about personnel selection.

<table><tr><td>Authors (Year)</td><td>Criteria</td><td>Solution method</td><td>Job Position (SECTOR)</td></tr><tr><td>Chen [28]</td><td>1*, 2*</td><td>FTOPSIS</td><td>System Engineer (2**)</td></tr><tr><td>Capaldo and Zollo [2-3]</td><td>2*, 11*</td><td>Fuzzy set theory</td><td>Unstated (1**)</td></tr><tr><td>Jessop [53]</td><td>2*</td><td>Jaynes&#x27; principle of maximum entropy</td><td>Unstated (3**)</td></tr><tr><td>Majozi and Zhu [77]</td><td>1*, 2*, 5*</td><td>Fuzzy Set Theory and MILP</td><td>Operator (4**)</td></tr><tr><td>Saghafian and Hejazi [96]</td><td>1*</td><td>FTOPSIS modified</td><td>Professor (3**)</td></tr><tr><td>Shih et al. [103]</td><td>1*, 5*, 9*, 11*</td><td>AHP and TOPSIS</td><td>Online manager (5**)</td></tr><tr><td>Tai and Hsu [106]</td><td>1*, 3*, 5*</td><td>Fuzzy data mining</td><td>Unstated (7**)</td></tr><tr><td>Gibney and Shang [43]</td><td>2*, 11*</td><td>AHP</td><td>Dean (3**)</td></tr><tr><td>Golec and Kahya [44]</td><td>1*, 2*, 11*</td><td>Competency based fuzzy model development</td><td>Unstated (1**)</td></tr><tr><td>Mahdavi et al. [75]</td><td>1*, 2*</td><td>FTOPSIS</td><td>System Analyst (2**)</td></tr><tr><td>Zavadskas et al. [124]</td><td>2*, 11*</td><td>COPRAS-G</td><td>Project manager (4**)</td></tr><tr><td>Celik et al. (2009)</td><td>1*, 2*, 3*, 4*, 8*, 9*, 11*</td><td>FAHP, FTOPSIS</td><td>Senior lecturer (3**)</td></tr><tr><td>Güngör et al. [48]</td><td>1*, 2*, 3*, 4*, 5*, 11*</td><td>FAHP</td><td>Unstated (1**)</td></tr><tr><td>Huang et al. [51]</td><td>1*, 2*, 11*</td><td>Bi objective binary integer programming and fuzzy set theory with goal programming</td><td>A group of people (purchaser, material handler, production planner, technician...) (7**)</td></tr><tr><td>Liao and Chang [68]</td><td>1*, 2*, 4*</td><td>ANP</td><td>Public Relations personnel (5**)</td></tr><tr><td>Polychroniou and Gia-nnikos [87]</td><td>1*, 2*, 3*, 4*, 5*, 6*</td><td>TOPSIS</td><td>Credit officer (7**)</td></tr></table>

(continued on next page)

Table A1 (continued)

<table><tr><td>Authors (Year)</td><td>Criteria</td><td>Solution method</td><td>Job Position (SECTOR)</td></tr><tr><td>Saremi et al. [101]</td><td>1*, 11*</td><td>FTOPSIS</td><td>TQM Consultant (7**)</td></tr><tr><td>Lin [70]</td><td>1*, 2*, 3*</td><td>ANP</td><td>Electrical engineer (7**)</td></tr><tr><td>Rashidi et al. [90]</td><td>2*, 3*, 4*, 5*, 10*, 11*</td><td>Fuzzy system based on IF-THEN rules with genetic algorithm</td><td>Project manager (4**)</td></tr><tr><td>Boran et al. [14]</td><td>1*, 2*, 9*</td><td>IF TOPSIS</td><td>Sales manager (7**)</td></tr><tr><td>Chen et al. [30]</td><td>1*, 2*, 4*</td><td>Linguistic VIKOR</td><td>Engineer (7**)</td></tr><tr><td>Chen et al. [31]</td><td>2*, 5*, 9*, 11*</td><td>OWA and TOPSIS</td><td>On-site business manager (7**)</td></tr><tr><td>Afshari et al. [3]</td><td>1*, 2*, 3*, 11*</td><td>Delphi method, fuzzy linguistic evaluation and fuzzy SAW method</td><td>Project manager (7**)</td></tr><tr><td>Kabak et al. [57]</td><td>2*, 5*, 11*</td><td>FANP, FTOPSIS, FELECTRE</td><td>Sniper (6**)</td></tr><tr><td>Zolfani et al. [125]</td><td>1*, 2*, 6*</td><td>AHP and COPRAS-G</td><td>Quality Control Manager (7**)</td></tr><tr><td>Afshari et al. [4]</td><td>1*, 2*, 3*, 11*</td><td>Fuzzy Integral Model</td><td>Project Manager (7**)</td></tr><tr><td>Kumar et al. [65]</td><td>1*, 2*, 6*, 11*</td><td>SAW, WP, AHP and TOPSIS</td><td>Asst. Prof. Dr. (3**)</td></tr><tr><td>Ozdemir [81]</td><td>1*, 2*, 3*, 8*, 9*, 11*</td><td>AHP with stochastic dynamic programming</td><td>Marketing Dept. (7**)</td></tr><tr><td>Rouyendegh and Erka-n [91]</td><td>1*, 2*, 3*, 4*, 5*9*, 11*</td><td>Fuzzy ELECTRE</td><td>Academic staff (3**)</td></tr><tr><td>Varajão and Cruz-Cu-nha [113]</td><td>1*, 2*, 3*, 4*, 11*</td><td>AHP and ICB (IPMA Competence Baseline)</td><td>Project Manager (4**)</td></tr><tr><td>Afshari et al. [2]</td><td>1*, 2*, 3*, 11*</td><td>Linguistic fuzzy model</td><td>Project manager (7**)</td></tr><tr><td>Saad et al. [95]</td><td>1*, 2*, 3*</td><td>Hamming distance method with subjective and objective weights (HDMSOW&#x27;s)</td><td>Lecturer (3**)</td></tr><tr><td>Vatansever and Öncel (2014)</td><td>1*, 5*, 11*</td><td>FAHP, FTOPSIS</td><td>Research assistant (3**)</td></tr><tr><td>Alguliyev et al. (2015)</td><td>1*, 2*, 8*</td><td>Modified fuzzy VIKOR</td><td>Information Technology Staff (3**)</td></tr><tr><td>Kusumawardani and Agintiara [66]</td><td>1*, 3*</td><td>FAHP &amp; TOPSIS</td><td>Human resources manager (7**)</td></tr><tr><td>Sang et al. [100]</td><td>1*, 2*</td><td>FTOPSIS</td><td>System Analyst Engineer (2**)</td></tr><tr><td>Stanujkic et al. [105]</td><td>1*, 2*, 3*, 4*, 11*</td><td>SWARA-ARAS</td><td>Sales manager (7**)</td></tr><tr><td>Liu et al. [71]</td><td>1*, 2*, 9*</td><td>VIKOR</td><td>Nurse (5**)</td></tr><tr><td>Chaghooshi et al. [27]</td><td>2*, 5*, 11*</td><td>FDEMATEL and FVIKOR</td><td>Project manager (7**)</td></tr><tr><td>Chen et al. [29]</td><td>1*, 2*, 3*, 4*, 10*, 11*</td><td>TPPRDSM (two-phase personnel recruitment decision support model), linguistic TOPSIS and linguistic PROMETHEE</td><td>Overseas marketing manager (2**)</td></tr><tr><td>Kosareva et al. [63]</td><td>1*, 2*, 5*, 11*</td><td>KEMIRA (KEmeny Median Indicator Rank Accordance)</td><td>Security Personnel (7**)</td></tr><tr><td>Salehi [97]</td><td>1*, 2*, 4*, 11*</td><td>FAHP and FVIKOR</td><td>Unstated (1**)</td></tr><tr><td>Urosevic et al. [112]</td><td>1*, 2*</td><td>WASPAS and SWARA</td><td>Sales manager (7**)</td></tr><tr><td>Heidary Dahooie et al. [50]</td><td>1*, 2*, 11*</td><td>SWARA and ARAS-G</td><td>BI expert (2**)</td></tr><tr><td>Jasemi and Ahmadi [-52]</td><td>1*, 2*, 7*, 9*</td><td>Fuzzy ELECTRE, TOPSIS</td><td>Industrial Engineer (4**)</td></tr><tr><td>Demirci and Kılıç [33]</td><td>1*, 2*, 3*, 4*, 7*, 10*, 11*</td><td>DEMATEL, ANP, ELECTRE</td><td>Engineer (4**)</td></tr><tr><td>Nabeeh et al. [80]</td><td>1*, 2*, 8*</td><td>Neutrosophic AHP, TOPSIS</td><td>Unstated (2**)</td></tr><tr><td>Petridis et al. [85]</td><td>1*, 2*, 9*, 11*</td><td>AHP, TOPSIS, Non-linear model</td><td>Internal auditor (1**)</td></tr></table>

Notes: 1\* Knowledge and experience; 2\* Personal characteristics and skills; 3\* Education; 4\* Foreign language; 5\* Physical wellness and demographic features; 6\* Salary request;  
7\* Vocational flexibility and capability; 8\* References; 9\* Oral assessment; 10\* Exam results and school reputation; 11\* Technical skills and requirements. 1\*\* Unstated; 2\*\* Information Technology; 3\*\* Education; 4\*\* Production; 5\*\* Health; 6\*\* Military; 7\*\* Other.

## Appendix B. IF-DEMATEL steps

Abbreviations and symbols used in IF-DEMATEL method.

<table><tr><td>Abbreviation/symbol</td><td>Definition</td></tr><tr><td>IFS</td><td>Intuitionistic Fuzzy Set</td></tr><tr><td> $\mu_k$ </td><td>Membership value</td></tr><tr><td> $v_k$ </td><td>Non-membership value</td></tr><tr><td> $\Pi_k$ </td><td>Hesitancy value</td></tr><tr><td> $\lambda_k$ </td><td>The importance weight of decision-maker “k”</td></tr><tr><td> $r_{ij}$ </td><td>Aggregated intuitionistic fuzzy relation value</td></tr><tr><td> $\beta$ </td><td>Risk preference</td></tr><tr><td> $\bar{r}_{ij}$ </td><td>Defuzzified value of the aggregated intuitionistic fuzzy relation</td></tr><tr><td>X</td><td>Normalized matrix of the defuzzified aggregated intuitionistic fuzzy relation matrix</td></tr><tr><td> $\lambda$ </td><td>Multiplier for the normalization process</td></tr><tr><td>T</td><td>Total relation matrix</td></tr><tr><td> $D_i$ </td><td>Row sum for criterion “i” in total relation matrix</td></tr><tr><td> $R_i$ </td><td>Column sum for criterion “i” in total relation matrix</td></tr><tr><td> $w_i$ </td><td>Raw importance value for criterion “i”</td></tr><tr><td> $W_i$ </td><td>Final importance value for criterion “i”</td></tr></table>

## B.1. Preliminary information about intuitionistic fuzzy sets (IFSs)

Considering the study of Atanasov (1986), the membership degree of the x element is set to A as $\mu _ { A } ( x )$ , the degree of non-membership as $\nu _ { A } ( x )$ and the hesitation index as $\pi _ { A } ( x )$ . Let (E) be a crisp fixed set and let $\mathbf A \subset \mathbf E$ is a fixed set. An IFS in $\mathsf { A } ^ { * }$ is indicated as in Eq. (4).

$$
\mathrm{A} ^ {*} = \{\langle x, \mu_ {A} (x), v _ {A} (x) | x \in E \rangle \}\tag{4}
$$

where $\mu _ { A } : E \to [ 0 , 1 ]$ and $\nu _ { A } : E \to [ 0 , 1 ]$ . In IFS theory, the sum of membership degree and non-membership degree is less than 1 as shown in Eq. (5) and the hesitation degree is computed as in Eq. (6).

$$
0 \leq \mu_ {A} (x) + v _ {A} (x) \leq 1\tag{5}
$$

$$
\pi_ {A} (x) = 1 - \mu_ {A} (x) - \nu_ {A} (x)\tag{6}
$$

Step 1: Provide the structure of the problem by indicating the objective, criteria, and sub-criteria.

Step 2: Determine the evaluation scale. Within the proposed methodology, the scale proposed by Büyüközkan et al. [17] is adopted as in Table B2.

Table B2  
Linguistic terms used in DEMATEL.

<table><tr><td>Definition of linguistic terms</td><td colspan="3">Intuitionistic Fuzzy Number</td></tr><tr><td>Very high influence (VH)</td><td>[0.90]</td><td>0.10</td><td>0.00]</td></tr><tr><td>High influence (H)</td><td>[0.75]</td><td>0.20</td><td>0.05]</td></tr><tr><td>Medium influence (M)</td><td>[0.50]</td><td>0.45</td><td>0.05]</td></tr><tr><td>Low influence (L)</td><td>[0.35]</td><td>0.60</td><td>0.05]</td></tr><tr><td>No influence (N)</td><td>[0.00]</td><td>1.00</td><td>0.00]</td></tr></table>

Step 3: Prioritize decision-makers. The prioritization is calculated via the scale and the equation proposed by Boran et al. [13] as shown in Table B3.

Table B3  
Linguistic scale for determining the importance of decision-makers.

<table><tr><td>Definition of linguistic terms</td><td colspan="3">Intuitionistic Fuzzy Number</td></tr><tr><td>Very important (VI)</td><td>[0.90]</td><td>0.10</td><td>0.00]</td></tr><tr><td>Important (I)</td><td>[0.75]</td><td>0.20</td><td>0.05]</td></tr><tr><td>Medium important (MI)</td><td>[0.50]</td><td>0.45</td><td>0.05]</td></tr><tr><td>Unimportant (U)</td><td>[0.35]</td><td>0.60</td><td>0.05]</td></tr><tr><td>Very unimportant (VU)</td><td>[0.10]</td><td>0.90</td><td>0.00]</td></tr></table>

For each of the decision-makers, the formula provided in Eq. 7 is utilized, and the importance weight of each decision-maker is obtained

$$
\lambda_ {k} = \frac {\left(\mu_ {k} + \Pi_ {k} \left(\frac {\mu_ {k}}{\mu_ {k} + v _ {k})}\right)\right)}{\sum_ {k = 1} ^ {l} \left(\mu_ {k} + \Pi_ {k} \left(\frac {\mu_ {k}}{\mu_ {k} + v _ {k})}\right)\right)}\tag{7}
$$

As seen in Eq. 8, the sum of the relative importance weights of decision-makers must be equal to 1.

$$
\sum_ {k = 1} ^ {l} \lambda_ {k} = 1\tag{8}
$$

Step 4: Determine the intuitionistic judgments of each expert (decision-maker) and aggregate their preferences via the intuitionistic fuzzy weighted averaging (IFWA) operator provided in Eq. 9 [119].

$$
r _ {i j} = I F W A _ {\lambda} (r _ {i j} ^ {(1)}, r _ {i j} ^ {(2)},..., r _ {i j} ^ {(l)}) = \lambda_ {1} r _ {i j} ^ {(1)} \bigoplus \lambda_ {2} r _ {i j} ^ {(2)} \oplus ... \bigoplus \lambda_ {l} r _ {i j} ^ {(l)} = = \Big [ 1 - \prod_ {k = 1} ^ {l} (1 - \mu_ {i j} ^ {(k)}) ^ {\lambda_ {k}}, \prod_ {k = 1} ^ {l} (\nu_ {i j} ^ {(k)}) ^ {\lambda_ {k}}, \prod_ {k = 1} ^ {l} (1 - \mu_ {i j} ^ {(k)}) ^ {\lambda_ {k}} - \prod_ {k = 1} ^ {l} (\nu_ {i j} ^ {(k)}) ^ {\lambda_ {k}} \Big ]
$$

$$
r _ {i j} = (\mu_ {i j}, v _ {i j}, \pi_ {i j}) \mu_ {i j} = (1 - \prod_ {k = 1} ^ {l} (1 - \mu_ {i j} ^ {(k)}) ^ {\lambda_ {k}}), v _ {i j} = (\prod_ {k = 1} ^ {l} (v _ {i j} ^ {(k)}) ^ {\lambda_ {k}}),
$$

$$
\pi_ {i j} = (\prod_ {k = 1} ^ {l} (1 - \mu_ {i j} ^ {(k)}) ^ {\lambda_ {k}} - \prod_ {k = 1} ^ {l} (\nu_ {i j} ^ {(k)}) ^ {\lambda_ {k}})\tag{9}
$$

Step 5: Defuzzify the aggregated intuitionistic fuzzy relation matrix via the formula proposed by Xie et al. [118] and shown in $\operatorname { E q . }$ 10 (β is taken as 0.5, risk neutral, in the application).

$$
\overline {{r}} _ {i j} = \mu_ {i j} - v _ {i j} + (2 \beta - 1) \pi_ {i j}\tag{10}
$$

$$
\mathrm{X} = \left[ \begin{array}{c c c} 0 & \dots & \overline {{r}} _ {1 n} \\ \vdots & \ddots & \vdots \\ \overline {{r}} _ {n 1} & \dots & 0 \end{array} \right]
$$

Step 6: Normalize the defuzzified aggregated intuitionistic fuzzy relation matrix (X) via Eq. 11 and obtain N as seen in Eq. 12.

$$
\lambda = m i n \left[ \frac {1}{\max 1 \leq i \leq n \sum_ {j = 1} ^ {n} | \overline {{r}} _ {i j} |}, \frac {1}{\max 1 \leq j \leq n \sum_ {i = 1} ^ {n} | \overline {{r}} _ {i j} |} \right] i, j \in \{1, 2,..., n \}\tag{11}
$$

$$
N = \lambda x X\tag{12}
$$

Step 7: Calculate the total relation matrix by applying the formula provided in $\operatorname { E q . }$ 13.

$$
T = N (I - N) ^ {- 1}\tag{13}
$$

Step 7: Determine the cause and efect groups by calculating the horizonta $( \mathbb { D } + \mathbb { R } )$ and vertical (D-R) axes. Positive (D-R) values indicate causa factors, whereas negative (D-R) values indicate efect groups.

Step 8: Perform normalization by applying the formula indicated in Eqs. (14–15) and obtain the final criteria importance weights.

$$
w _ {i} = \{(D _ {i} + R _ {i}) ^ {2} + (D _ {i} - R _ {i}) ^ {2} \} ^ {0. 5}\tag{14}
$$

$$
W _ {i} = \frac {w _ {i}}{\sum_ {i} w _ {i}}\tag{15}
$$

The output of the IF-DEMATEL is then fed into the IF-ELECTRE, where the alternatives are rank ordered.

## Appendix C. IF-ELECTRE steps

Table C1  
Abbreviations and symbols used in IF-ELECTRE method.

<table><tr><td>Abbreviation/symbol</td><td>Definition</td></tr><tr><td> $C_{kl}$ </td><td>Main concordance set</td></tr><tr><td> $C_{kl}'$ </td><td>Midrange concordance set</td></tr><tr><td> $C_{kl}''$ </td><td>Weak concordance set</td></tr><tr><td> $D_{kl}$ </td><td>Main discordance set</td></tr><tr><td> $D_{kl}'$ </td><td>Midrange discordance set</td></tr><tr><td> $D'_{kl}'$ </td><td>Weak discordance set</td></tr><tr><td> $D_{kl}^{*}$ </td><td> $D_{kl}, D_{kl}' \text{ or } D'_{kl}'$ </td></tr><tr><td>G</td><td>Concordance matrix</td></tr><tr><td> $g_{kl}$ </td><td>Concordance index between alternative “k” and alternative “l”</td></tr><tr><td> $g^{*}$ </td><td>Maximum of concordance indexes ( $g_{kl}$ )</td></tr><tr><td>H</td><td>Discordance matrix</td></tr><tr><td> $h_{kl}$ </td><td>Discordance index between alternative “k” and alternative “l”</td></tr><tr><td> $h^{*}$ </td><td>Maximum of discordance indexes ( $h_{kl}$ )</td></tr><tr><td> $X_{kj}$ </td><td>The evaluation of alternative “k” with respect to criterion “j”</td></tr><tr><td> $d(X_{kj},X_{lj})$ </td><td>The distance between alternative “k” and “l” with respect to criterion “j”</td></tr><tr><td> $A_{k}$ </td><td>Alternative “k”</td></tr><tr><td> $w_{j}$ </td><td>Weight of criterion “j”</td></tr><tr><td> $w_{c}$ </td><td>Weight of main concordance set</td></tr><tr><td> $w_{c'}$ </td><td>Weight of midrange concordance set</td></tr><tr><td> $w_{c''}$ </td><td>Weight of weak concordance set</td></tr><tr><td> $w_{D}$ </td><td>Weight of main discordance set</td></tr><tr><td> $w_{D'}$ </td><td>Weight of midrange discordance set</td></tr><tr><td> $w_{D''}$ </td><td>Weight of weak discordance set</td></tr><tr><td> $w_{D}^{*}$ </td><td> $w_{D}, w_{D'} \text{ or } w_{D''}$ </td></tr><tr><td>K</td><td>Concordance dominance matrix</td></tr><tr><td> $k_{kl}$ </td><td>Concordance dominance index between alternative “k” and alternative “l”</td></tr><tr><td>L</td><td>Discordance dominance matrix</td></tr><tr><td> $l_{kl}$ </td><td>Discordance dominance index between alternative “k” and alternative “l”</td></tr><tr><td>R</td><td>Aggregate dominance matrix</td></tr><tr><td> $r_{kl}$ </td><td>Aggregate dominance index between alternative “k” and alternative “l”</td></tr><tr><td> $T_{k}$ </td><td>Final ranking score of alternative “k”</td></tr></table>

Step 1: Determine the concordance and discordance sets.

Considering two alternatives $" \mathrm { A _ { k } } ^ { \prime \prime }$ and $^ { \dag } { } ^ { \left. \mathfrak { A } _ { \mathrm { l } } \right. \mathfrak { n } }$ , the concordance set ${ \bf c _ { \mathrm { k l } } }$ composes of the criteria where the alternative $" \mathrm { A _ { k } } ^ { \prime \prime }$ is preferred to alternative $^ { \mathrm { 4 } } \mathrm { A } _ { \mathrm { l } } ^ { \mathrm { 7 } } .$ . On the other hand, the discordance set is the complementary of the concordance set. Unlike in the crisp ELECTRE method, there are three types of concordance and discordance sets in IF-ELECTRE. These can be stated as main, midrange and weak sets as seen in Eqs. 16–18.

Main concordance set formula.

$$
C _ {k l} = \{j \mid \mu_ {k j} \geq \mu_ {l j}, v _ {k j} <   v _ {l j} a n d \pi_ {k j} <   \pi_ {l j} \}\tag{16}
$$

Midrange concordance set formula.

$$
C _ {k l} ^ {\prime} = \{j \mid \mu_ {k j} \geq \mu_ {l j}, v _ {k j} <   v _ {l j} a n d \pi_ {k j} \geq \pi_ {l j} \}\tag{17}
$$

Weak concordance set formula.

$$
C _ {k l} ^ {\prime \prime} = \{j \mid \mu_ {k j} \geq \mu_ {l j} a n d v _ {k j} \geq v _ {l j} \}\tag{18}
$$

Moreover, the related formulas for discordance sets are shown as in Eqs. 19–21:

Main discordance set formula.

$$
D _ {k l} = \{j \mid \mu_ {k j} <   \mu_ {l j}, v _ {k j} \geq v _ {l j} a n d \pi_ {k j} \geq \pi_ {l j} \}\tag{19}
$$

Midrange discordance set formula.

$$
D _ {k l} ^ {\prime} = \{j \mid \mu_ {k j} <   \mu_ {l j}, v _ {k j} \geq v _ {l j} a n d \pi_ {k j} <   \pi_ {l j} \}\tag{20}
$$

Weak discordance set formula

$$
D _ {k l} ^ {\prime \prime} = \{j \mid \mu_ {k j} <   \mu_ {l j} a n d v _ {k j} <   v _ {l j} \}\tag{21}
$$

Step 2: Obtain the concordance and discordance matrix.

The concordance matrix (G) consists of concordance indexes $\mathbf { g } _ { \mathrm { k l } }$ between $\mathbf { A } _ { \mathbf { k } }$ and $\mathbf { A } _ { \mathrm { l } }$ and it is defined as in Eq. 22.

$$
g _ {k l} = w _ {c} * \sum_ {j \in C _ {k l}} w _ {j} + w _ {c ^ {\prime}} * \sum_ {j \in c _ {k l} ^ {\prime}} w _ {j} + w _ {c ^ {\prime \prime}} * \sum_ {j \in c _ {k l} ^ {\prime}} w _ {j}\tag{22}
$$

$$
G = \left[ \begin{array}{c c c} - & g _ {1 2} \dots & g _ {1 m} \\ \vdots & \ddots & \vdots \\ g _ {m 1} & \dots & - \end{array} \right]
$$

The maximum value in the concordance matrix G is denoted by $g ^ { * }$ and expressed as the positive ideal point. The higher values of $^ \mathrm { g } \mathrm { k l }$ indicate the superiority of the alternative $\mathbf { A } _ { \mathbf { k } }$ to the alternative $\mathbf { A } _ { \mathrm { l } } .$ .

The discordance matrix (H) can be defined as in Eqs. 23 and 24.

$$
d (X _ {k j}, X _ {l j}) = \sqrt {0 . 5 * ((\mu_ {k j} - \mu_ {l j}) ^ {2} + (\nu_ {k j} - \nu_ {l j}) ^ {2} + (\pi_ {k j} - \pi_ {l j}) ^ {2})}\tag{23}
$$

$$
h _ {k l} = \frac {m a x _ {j \in D _ {k l} ^ {*}} w _ {D} ^ {*} * d (X _ {k j} , X _ {l j})}{m a x _ {j \in J} d (X _ {k j} , X _ {l j})}\tag{24}
$$

$$
H = \left[ \begin{array}{c c c} - & h _ {1 2} \dots & h _ {1 m} \\ \vdots & \ddots & \vdots \\ h _ {m 1} & \dots & - \end{array} \right]
$$

The maximum value in the discordance matrix H is denoted by h<sup>⁎</sup> and expressed as the negative ideal point. The higher values of $\mathbf { h } _ { \mathbf { k l } }$ indicate the superiority of the alternative $\mathbf { A } _ { \mathrm { l } }$ to the alternative $\mathbf { A } _ { \mathbf { k } }$

Step 3: Obtain the concordance and discordance dominance matrix.

The concordance dominance matrix (K) consisting of the elements $\mathbf { k } _ { \mathbf { k l } }$ is obtained as in Eq. 25.

$$
\mathbf {k} _ {\mathrm{kl}} = \mathbf {g} ^ {*} - \mathbf {g} _ {\mathrm{kl}}\tag{25}
$$

$$
K = \left[ \begin{array}{c c c} - & k _ {1 2} \dots & k _ {1 m} \\ \vdots & \ddots & \vdots \\ k _ {m 1} & \dots & - \end{array} \right]
$$

Where $\mathbf { k } _ { \mathbf { k l } }$ indicates the distance of each alternative from the positive ideal solution and higher value of it shows that $\mathbf { A } _ { \mathbf { k } }$ is less preferable than $\mathbf { A } _ { \mathrm { l } } .$ The discordance dominance matrix (L) can be stated as in Eq. 26.

$$
\mathrm {l_ {kl} = h^ {*} - h_ {kl}}\tag{26}
$$

$$
L = \left[ \begin{array}{c c c} - & l _ {1 2} \dots & l _ {1 m} \\ \vdots & \ddots & \vdots \\ l _ {m 1} & \dots & - \end{array} \right]
$$

Where $\mathbf { l } _ { \mathbf { k l } }$ indicates the distance of each alternative from the negative ideal solution and higher value of it shows that $\mathbf { A } _ { \mathbf { k } }$ is more preferable than $\mathbf { A } _ { \mathrm { l } } .$

Step 4: Obtain the aggregate dominance matrix.

The aggregate dominance matrix (R) is constructed via the integration of concordance and discordance dominance matrixes, as seen in Eq. 27.

$$
r _ {k l} = \frac {l _ {k l}}{k _ {k l} + l _ {k l}}\tag{27}
$$

$$
R = \left[ \begin{array}{c c c} - & r _ {1 2} \dots & r _ {1 m} \\ \vdots & \ddots & \vdots \\ r _ {m 1} & \dots & - \end{array} \right]
$$

Where ${ \bf r _ { k l } }$ indicates the relative closeness to the ideal solution, and it takes a value between 0 and 1.

Step $_ { 5 ; }$ Obtaining the final ranking of the candidates.

The final ranking of the alternatives is obtained from this matrix based on the values of ${ \overline { { T _ { k } } } } ,$ from the highest values to the lowest values, as indicated in Eq. 28.

$$
\overline {{T}} _ {k} = \frac {1}{m - 1} \sum_ {l = 1, l \neq k} ^ {m} r _ {k l}, k = 1, 2, \dots , m\tag{28}
$$

Appendix D. Sensitivity analysis results

![](/api/attachments/HPEJDPHV/fulltext/images/ecc1cd3d3710f36b593fdd702df35686153ceba5e2de9c4787d4bc40fa2b1e3f.jpg)  
Fig. D1. The sensitivity analysis concerning criterion 2.

Sensitivity analysis with respect to criterion 3  
![](/api/attachments/HPEJDPHV/fulltext/images/827dca97b3bb01cbe77c0a9581300e11b8a9898f62fd9c2d9fca78a606ae7c7d.jpg)  
Fig. D2. The sensitivity analysis concerning criterion 3.

Sensitivity analysis with respect to criterion 4  
![](/api/attachments/HPEJDPHV/fulltext/images/ab152a42ad825ff58428ac8091fb07280d9c27dbf03a6c5f9144fea3f5145cd8.jpg)  
Fig. D3. The sensitivity analysis concerning criterion 4.

![](/api/attachments/HPEJDPHV/fulltext/images/c306621e7cafc783b3f4176247d4f54906ee02bb6903b3766510a8f375536990.jpg)  
Fig. D4. The sensitivity analysis concerning criterion 5.

## References

[1] T.A. Adisa, E.L. Osabutey, G. Gbadamosi, C. Mordi, The challenges of employee resourcing: the perceptions of managers in Nigeria, Career Dev. Int. 22 (6) (2017) 703–723.

[2] A.R. Afshari, M. Nikolić, D. Ćoćkalo, Applications of fuzzy decision making for personnel selection problem: a review, J. Eng. Manag. Compet. 4 (2) (2014) 68-77.

[3] A.R. Afshari, R. Yusuf, A.R. Derayatifar, Project manager selection by using fuzzy simple additive weighting method, 2012 International Conference on Innovation Management and Technology Research (ICIMTR), IEEE, 2012, pp. 412–416.

[4] A.R. Afshari, R.M. Yusuf, A.R. Derayatifar, Linguistic extension of fuzzy integra for group personnel selection problem, Arab. J. Sci. Eng. 38 (10) (2013) 2901-2910.

[5] J. Almeida-Dias, J.R. Figueira, B. Roy, Electre tri-C: a multiple criteria sorting method based on characteristic reference actions, Eur. J. Oper. Res. 204 (3) (2010) 565–580.

[6] J. Almeida-Dias, J.R. Figueira, B. Roy, A multiple criteria sorting method where each category is characterized by several reference actions: the electre tri-nC method, Eur. J. Oper. Res. 217 (3) (2012) 567–579.

[7] N. Anderson, M. Born, N. Cunningham-Snell, Recruitment and selection: Applicant perspectives and outcomes, in: N. Anderson, D.S. Ones, H.K. Sinangil C. Viswesvaran (Eds.), Handbook of Industrial, Work and Organizational Psychology, Vol. 1 Sage Publications Ltd., 2002, pp. 200–218 Personne Psychology.

[8] N. Anderson, F. Lievens, K. Van Dam, A.M. Ryan, Future perspectives on employee selection: key directions for future research and practice, Appl. Psychol. 53 (4) (2004) 487–501

[11] R. Benayoun, B. Roy, B. Sussman, Une méthode pour guider le choix en presence de points de vue multiples, (1966) (Note de travail 49. SEMA-METRA. Direction-Scientifique).

[12] M.F. Bongo, K.M.S. Alimpangog, J.F. Loar, J.A. Montefalcon, L.A. Ocampo, An application of DEMATEL-ANP and PROMETHEE II approach for air trafic con trollers' workload stress problem: a case of Mactan civil Aviation Authority of th Philippines. J. Air Transp. Manag, 68 (2018) 198–213

[13] F.E. Boran, S. Genç, M. Kurt, D. Akay, A multicriteria intuitionistic fuzzy group decision making for supplier selection with TOPSIS method, Expert Syst. Appl. 36 (8) (2009) 11363–11368.

[14] F.E. Boran, S. Genç, D. Akay, Personnel selection based on intuitionistic fuzzy sets, Human Factors Ergon, Manuf, Sery, Ind, 21 (5) (2011) 493–503.

[15] A. Bufardi, R. Gheorghe, P. Xirouchakis, Fuzzy outranking methods: recent developments, Fuzzy Multi-Criteria Decision Making, Springer, Boston, MA, 2008, pp. 119–157.

[16] G. Büyüközkan, F. Göçer, Y. Karabulut, A new group decision making approach with JF AHP and IE VIKOR for selecting hazardous waste carriers Measurement 134 (2019) 66–82.

[17] G. Büvüközkan, S. Gülervüz, B. Karpak, A new combined IF-DEMATEL and IF-ANP approach for CRM partner evaluation Int, J. Prod Fcon 191 (2017) 194–206

[18] M. Branine. Graduate recruitment and selection in the UK: a study of the recent changes in methods and expectations, Career Dev. Int. 13 (6) (2008) 497–513.

[19] Byars, L.L. and Rue, L.W. (2000), Human Resources Management; Theory and Practice, London: Macmillan Press. Development on the Bottom Line (4th ed.), London: Pitman.

[20] R. Caers, C. Du Bois, M. Jegers, S. De Gieter, R. De Cooman, R. Pepermans, A micro-economic perspective on manager selection in nonprofit organizations, Eur. J. Oper. Res. 192 (1) (2009) 173–197.

[21] E. Cakin, A. Ozdemir, “Tedarikçi Seçim Kararında Analitik Ağ Süreci (ANP) ve ELECTRE Yöntemlerinin Kullanilması ve Bir Uvgulama", Afvon Kocatepe

Üniversitesi İktisadi ve İdari Bilimler Fakültesi Dergisi, Vol. 15 No.2 (2013), pp. 339–364.

[23] G. Capaldo, G. Zollo, Applying fuzzy logic to personnel assessment: a case study, Omega 29 (6) (2001) 585–597.

[24] K. Carlson, M. Connerley, The stafing cycles framework: viewing stafing as a system of decision events, J. Manag. 29 (2003) 51–78.

[25] F. Cavallaro, E.K. Zavadskas, D. Streimikiene, A. Mardani, Assessment of concentrated solar power (CSP) technologies based on a modified intuitionistic fuzzy topsis and trigonometric entropy weights. Technol. Forecast, Soc, Chang. 140 (2019) 258–270.

[26] S. Cebi, Determining importance degrees of website design parameters based on interactions and types of websites, Decis. Support. Syst. 54 (2) (2013) 1030–1043.

[27] A. Chaghooshi, A. Arab, S. Dehshiri, A fuzzy hybrid approach for project manager selection, Decis. Sci. Lett. (2016) 447–460 Vol. 5 No. 3.

[28] C.T. Chen, Extensions of the TOPSIS for group decision-making under fuzzy environment, Fuzzy Set Syst. 114 (1) (2000) 1–9.

[29] C.T. Chen, H.L. Cheng, W.Z. Hung, A two-phase decision-making method for handling personnel selection problem, 2016 12th International Conference on Natural Computation, Fuzzy Systems and Knowledge Discovery (ICNC-FSKD), JEEE, 2016, pp. 1021–1026

[30] C.T. Chen, P.F. Pai, W.Z. Hung, Applying linguistic VIKOR and knowledge map in personnel selection, Asia Pac. Manag. Rev. (2011) 491–502 Vol. 16 No. 4.

[311 Y. Chen. K.W. Li. S.F. Liu. An OWA-TOPSIS method for multiple criteria decision analysis, Expert Syst, Appl, 38 (5) (2011) 5205–5211.

[32] D. Delen, Prescriptive Analytics: The Final Frontier for Evidence-Based Management and Optimal Decision Making, Financial Times Press, Pearson Education: Upper Saddle River, New Jersey, 2019.

[33] A.E. Demirci, H.S. Kılıç, Personnel selection based on integrated multi-criteria decision making techniques, Int. J. Ady. Eng. Pure Sci. 31 (2) (2019) 163–178

[35] H. Ehsan, F. Milad, S. Shokrollah, Z. Narges, Selection of supplier in Lamerd cement company using innovative Dematel-Promethee I&II hybrid method, Asian J. Res. Social Sci. Humanit. 5 (4) (2014) 591–604.

[36] C. Erdin, G. Ozkaya, Turkey's 2023 energy strategies and investment opportunities for renewable energy sources: site selection based on ELECTRE, Sustainability 11 (7) (2019) 2136.

[37] B.C. Ervural, S. Zaim, O.F. Demirel, Z. Aydin, D. Delen, An ANP and fuzzy TOPSIS based SWOT analysis for Turkev's energy planning, Renew. Sustain. Energy Rev. 82 (1) (2018) 1538–1550.

[38] E. Fernandez, J. Navarro, A. Duarte, G. Ibarra, Core: a decision support system for regional competitiveness analysis based on multicriteria sorting, Decis. Support. Syst. 54 (3) (2013) 1417–1426.

[39] A. Fetanat, E. Khorasaninejad, A novel hybrid MCDM approach for ofshore wind farm site selection: a case study of Iran, Ocean Coast. Manag. 109 (2015) 17–28.

[40] J.R. Figueira, S. Greco, B. Roy, R. Słowiński, ELECTRE methods: Main features and recent developments, Handbook of Multicriteria Analysis, Springer, Berlin, Heidelberg, 2010. pp. 51–89.

[41] A. Gabus, E. Fontela, World problems, an invitation to further thought within the framework of DEMATEL, Battelle Geneva Research Centre, Switzerland, Geneva, 1972.

[42] C. Giannoulis, A. Ishizaka, A web-based decision support system with ELECTRE III for a personalised ranking of British universities, Decis. Support. Syst. 48 (3) (2010) 488–497.

[43] R. Gibney, J. Shang, Decision making in academia: a case of the dean selection process, Math. Comput. Model. 46 (7–8) (2007) 1030–1040.

[44] A. Golec. E. Kahva, A fuzzy model for competency-based emplovee evaluation and

[45] K. Govindan. M.B. Jepsen. ELECTRE: a comprehensive literature review on methodologies and applications, Eur, J. Oper, Res, 250 (1) (2016) 1–29.

[46] K. Govindan, D. Kannan, M. Shankar. Evaluation of green manufacturing practices

using a hybrid MCDM model combining DANP with PROMETHEE, Int. J. Prod. Res, 53 (21) (2015) 6344–6371

[47] İ. Gölcük, A. Baykasoğlu, An analysis of DEMATEL approaches for criteria interaction handling within ANP, Expert Syst. Appl. 46 (2016) 346–366.

[48] Z. Güngör, G. Serhadlıoğlu, S.E. Kesen, A fuzzy AHP approach top personnel selection problem, Appl. Soft Comput. 9 (2) (2009) 641–646.

[49] Ş. Gür, N. Bedir, T. Eren, Analitik ağ süreci ve PROMETHEE yöntemleri ile gıda sektöründeki orta ölçekli işletmeler için pazarlama stratejilerinin seçimi, Nevşehir Bilim ve Teknoloji Dergisi 6 (1) (2017) 79–92

[50] J. Heidary Dahooie, E. Beheshti Jazan Abadi, A.S. Vanaki, H.R. Firoozfar, Competency-based IT personnel selection using a hybrid SWARA and ARAS-G methodology, Hum. Factors Ergon. Manuf. Serv. Ind. 28 (1) (2018) 5–16.

[51] D.K. Huang, H.N. Chiu, R.H. Yeh, J.H. Chang, A fuzzy multicriteria decisionmaking approach for solving a bi-objective personnel assignment problem, Comput. Ind. Eng. 56 (1) (2009) 1–10.

[52] M. Jasemi, E. Ahmadi, A new fuzzy ELECTRE based multiple criteria method for personnel selection, Sci. Iran. 25 (2) (2018) 943–953.

[53] A. Jessop, Minimally biased weight determination in personnel selection, Eur. J. Oper, Res, 153 (2) (2004) 433–444

[54] D. Jyh-Fu Jeng, T. Bailey, Assessing customer retention strategies in mobile tele communications: hybrid MCDM approach, Manag. Decis. 50 (9) (2012) 1570–1595.

[55] N. Kabadayi, S. Dag, Bulanık DEMAEL ve Bulanık PROMETHEE Yöntemleri ile Kablo Üretiminde Makine Seçimi, Karadeniz Teknik Üniversitesi Sosyal Bilimler Enstitüsü Sosval Bilimler Dergisi, 7 2017, pp. 239–260 No.14.

[56] N. Kabadayi, S. Dag, Dealership performance evaluation in supply chain with DEMATEL and ELECTRE methods, Pamukkale Univ. J. Eng. Sci. 26 (1) (2020) 241–253.

[57] M. Kabak, S. Burmaoğlu, Y. Kazançoğlu, A fuzzy hybrid MCDM approach for professional selection, Expert Syst. Appl. 39 (3) (2012) 3516–3525.

[58] A. Kangas, J. Kangas, J. Pykäläinen, Outranking methods as tools in strategic natural resources planning, SilvaFennica 35 (2) (2001) 215–227.

[59] Y. Kazancoglu, I. Kazancoglu, M. Sagnak, Fuzzy DEMATEL-based green supply chain management performance: application in cement industry, Ind. Manag. Data Syst. 118 (2) (2018) 412–431.

[60] E. Khorasaninejad, A. Fetanat, H. Hajabdollahi, Prime mover selection in thermal power plant integrated with organic Rankine cycle for waste heat recovery using a novel multi criteria decision making approach, Appl. Therm. Eng. 102 (2016)

[61] H.S. Kilic, A.S. Yalcin, Modified two-phase fuzzy goal programming integrated with IF-TOPSIS for green supplier selection, Appl. Soft Comput. (2020) 106371.

[62] H.S. Kilic, S. Zaim, D. Delen, Selecting “the best” ERP system for SMEs using a combination of ANP and PROMETHEE methods, Expert Syst. Appl. 42 (5) (2015) 2343–2352.

[63] N. Kosareva, E.K. Zavadskas, A. Krylovas, S. Dadelo, Personnel ranking and se lection problem solution by application of KEMIRA method, Int. J. Comput. Commun. Control (2016) 51–66 Vol, 11 No.1.

[64] S.W. Kozlowski, Workforce Efectiveness: Acquiring Human Resources and Developing Human Capital, National Academies Press, Washington, DC, 2011.

[65] D.S. Kumar, S. Radhika, K.N.S. Suman, MADM methods for finding the right personnel in academic institutions, Int. J. u-and e-Serv. Sci. Technol. 6 (5) (2013) 133-144.

[66] R.P. Kusumawardani, M. Agintiara, Application of fuzzy AHP-TOPSIS method for decision making in human resource manager selection process. Procedia Comput Sci, 72 (2015) 638–646.

[68] S.K. Liao. K.L. Chang, Selecting public relations personnel of hospitals by analytic network process, J. Hosp. Mark, Public Relat. 19 (1) (2009) 52–63.

[69] F. Lievens, K. Van Dam, N. Anderson, Recent trends and challenges in personnel selection, Pers, Rev, 31 (5) (2002) 580–601.

[70] H.T. Lin, Personnel selection using analytic network process and fuzzy data en velopment analysis approaches, Comput. Ind. Eng. 59 (4) (2010) 937–944.

[71] H.C. Liu, J.T. Oin, LX. Mao. Z.Y. Zhang, Personnel selection using interval 2-tuple linguistic VIKOR method. Human Factors Ergon, Manuf, Service Ind. 25 (3) (2015 370-384.

[72] M.T. Lu. S.W. Lin, G.H. Tzeng, Improving RFID adoption in Taiwan's healthcare industry based on a DEMATEL technique with a hybrid MCDM model, Decis. Support. Syst. 56 (2013) 259–269.

[74] P. Madhu, C.S. Dhanalakshmi, M. Mathew, Multi-criteria decision-making in the selection of a suitable biomass material for maximum bio-oil yield during pyrolysis, Fuel 277 (2020) 118109.

[75] I. Mahdavi, N. Mahdavi-Amiri, A. Heidarzade, R. Nourifar, Designing a model o fuzzy TOPSIS in multiple criteria decision making, Appl. Math. Comput. 206 (2) (2008) 607–617

[77] T. Majozi, X.X. Zhu, A combined fuzzy set theory and MILP approach in integra tion of planning and scheduling of batch plants—personnel evaluation and allocation, Comput, Chem, Eng, 29 (9) (2005) 2029–2047.

[78] J.M. McCarthy, T.N. Bauer, D.M. Truxillo, N.R. Anderson, A.C. Costa, S.M. Ahmed, Applicant perspectives during selection: a review addressing “so what?."“What's

[79] A. Muñoz-Porcar, M.J. Alonso-Nuez, M. Flores-García, D. Duret-Solanas, The renewal of assets using a tool to aid decision making, Manag. Decis. 53 (7) (2015) 1412-1429.

[80] N.A. Nabeeh, F. Smarandache, M. Abdel-Basset, H.A. El-Ghareeb, A. Aboelfetouh, An integrated neutrosophic-topsis approach and its application to personnel se lection: a new trend in brain processing and analysis, IEEE Access 7 (2019) 29734–29744.

[81] A. Ozdemir, A two-phase multi criteria dynamic programing approach for per sonnel selection process, Problems and Perspectives in Management, 2013, pp. 98–108 Vol. 11 No. 2.

[82] E.C. Özcan, N.A. Ozcan, T. Eren, CSP Teknolojisine Sahip Güneş Enerjisi Santrallarının Kombine ANP-PROMETHEE Yaklaşımı ile Seçimi, Başkent Üniversitesi Ticari Bilimler Fakültesi Dergisi, 2017, pp. 18–44 Vol. 1 No.1.

[84] İ. Peker, An application related to logistics social responsibility evaluation with DEMATEL and ELECTRE methods, J. Econ. Bibliogr. (2016) 30–40 Vol. 3(1S).

[85] K. Petridis, G. Drogalas, E. Zografidou, Internal auditor selection using a TOPSIS non-linear programming model, Ann. Oper. Res. (2019) 1–27.

[86] M. Petrović, N. Bojković, I. Anić, M. Stamenković, S.P. Tarle, An ELECTRE-based decision aid tool for stepwise benchmarking: an application over EU digital agenda targets, Decis. Support. Syst. 59 (2014) 230–241.

[87] P.V. Polychroniou, I. Giannikos, A fuzzy multicriteria decision-making methodology for selection of human resources in a Greek private bank, Career Dev. Int. 14 (4) (2009) 372–387.

[88] M. Rahimi, A. Najafi, Analysis of Customer's expectations and satisfaction in Zanjan municipality using fuzzy multi-criteria decision making (FMCDM) approach, J. Optim. Ind. Eng. (2017) 47–57 Vol.10 No.21.

[89] N.A. Rahman, Z. Tarmudi, M. Rossdy, F.A. Muhiddin, Flood mitigation measres using intuitionistic fuzzy dematel method, Malavs. J. Geosci. (2017) 1–5 (MJG). Vol. 1 No.2.

[90] A. Rashidi, F. Jazebi, I. Brilakis, Neurofuzzy genetic system for selection of construction project managers, J. Constr. Eng. Manag. 137 (1) (2010) 17–29.

[91] B.D. Rouyendegh, T.E. Erkan, An application of the fuzzy ELECTRE method for academic staf selection, Human Factors Ergon. Manuf. Serv. Ind. 23 (2) (2013) 107-115

[93] B. Roy, ELECTRE III: Un algorithme de classements fondé sur une représentation floue des préférences en présence de critères multiples, Cahiers du Centre d'Etudes de Recherche Opérationnelle 20 (1) (1978) 3–24.

[94] B. Roy, D. Bouyssou, Aide multicritère à la décision: méthodes et cas, Economica, Paris, 1993, p. 695.

[95] R.M. Saad, M.Z. Ahmad, M.S. Abu, M.S. Jusoh, Hamming distance method with subjective and objective weights for personnel selection, Sci. World J. (2014) 1–9.

[96] S. Saghafian, S.R. Hejazi, Multi-criteria group decision making using a modified fuzzy TOPSIS procedure, Computational Intelligence for Modelling, Control and Automation, 2005 and International Conference on Intelligent Agents, Web Technologies and Internet Commerce, Vol. 2 2005, pp. 215–221.

[97] K. Salehi, An integrated approach of fuzzy AHP and fuzzy VIKOR for personne selection problem, Glob. J. Manag, Stud. Res. (2016) 89–95 Vol, 3 No. 3.

[100] X. Sang, X. Liu, J. Qin, An analytical solution to fuzzy TOPSIS and its application in personnel selection for the knowledge-intensive enterprise, Appl. Soft Comput. 30 (2015) 190–204.

[101] M. Saremi, S.F. Mousavi, A. Sanayei, TQM consultant selection in SMEs with TOPSIS under fuzzy environment, Expert Syst. Appl. 36 (2) (2009) 2742–2749.

[102] T. Sari, M. Timor, Integrated supplier selection model using ANP, Taguchi loss function and PROMETHEE methods, J. Appl, Quant. Methods (2016) 19–34 Vol.

[103] H.S. Shih, L.C. Huang, H.J. Shyur, Recruitment and selection processes through an effective GDSS. Comput, Math, Appl. 50 (10–12) (2005) 1543–1558

[104] S.L. Si, X.Y. You, H.C. Liu, P. Zhang, DEMATEL technique: a systematic review of the state-of-the-art literature on methodologies and applications. Math. Probl. Eng, 1 (2018) 1–33.

[105] D. Stanujkic, B. Djordjevic, D. Karabasevic, Selection of candidates in the process of recruitment and selection of personnel based on the SWARA and ARAS methods, Ouaestus Multidisciplinary Research Journal, vol. 7. 2015, pp. 53–64

[106] W.S. Tai, C.C. Hsu, A realistic personnel selection tool based on fuzzy data mining method, Joint Conference on Information Sciences, 2006.

[107] F.W. Taylor, Shop management, Harper & Brothers Publishing, New York: NY,

[108] F.W. Taylor, Scientific Management, Taylor & Francis: United Kingdom, Routledge, 2004.

[109] D.M. Truxillo, T.N. Bauer, J.M. McCarthy, N. Anderson, S.M. Ahmed, Applicant perspectives on employee selection systems, in: D.S. Ones, N. Anderson, C. Viswesvaran, H.K. Sinangil (Eds.), The SAGE Handbook of Industrial, Work & Organizational Psychology: Personnel Psychology and Employee Performance, 2018, pp. 508–532.

[110] H. Turan, Taylor's "scientific management principles": contemporary issues in personnel selection period, J. Econ. Bus. Manag. 3 (11) (2015) 1102–1105.

[111] G. Tuzkaya, B. Gülsün, C. Kahraman, D. Özgen, An integrated fuzzy multicriteria decision making methodology for material handling equipment selection problem and an application. Expert Syst, Appl, 37 (4) (2010) 2853–2863.

[112] S. Urosevic, D. Karabasevic, D. Stanujkic, M. Maksimovic, An approach to personnel selection in the tourism industry based on the SWARA and the WASPAS methods, Econ. Comput. Econ. Cybern. Stud. Res. 51 (1) (2017) 75–88.

[113] J. Varajão, M.M. Cruz-Cunha, Using AHP and the IPMA competence baseline in the project manager's selection process, Int. J. Prod. Res. 51 (11) (2013) 3342-3354.

[115] J.J. Wang, D.L. Yang, Using a hybrid multicriteria decision aid method for information systems outsourcing, Comput. Oper. Res. 34 (12) (2007) 3691–3700.

[116] S.A. Woods, S. Ahmed, I. Nikolaou, A.C. Costa, N.R. Anderson, Personnel selection in the digital age: a review of validity and applicant reactions. and future research challenges, Eur. J. Work Organ. Psychol. 29 (1) (2020) 64–77.

[117] M.C. Wu, T.Y. Chen, The ELECTRE multicriteria analysis approach based on Atanassov's intuitionistic fuzzy sets, Expert Syst. Appl. 38 (10) (2011) 12318–12327.

[118] H. Xie, W. Duan, Y. Sun, Y. Du, Dynamic DEMATEL group decision approach based on the intuitionistic fuzzy number, Telkomnika (Telecommunication Computing Electronics and Control) 12 (4) (2014) 1064–1072.

[119] Z. Xu, Intuitionistic fuzzy aggregation operators, IEEE Trans. Fuzzy Syst. 15 (6) (2007) 1179–1187.

[121] M. Yasmin, E. Tatoglu, H.S. Kilic, S. Zaim, D. Delen, Big data analytics capabilities and firm performance: an integrated MCDM approach, J. Bus. Res. 114 (2020) 1–15.

[122] K.P. Yoon, C.L. Hwang, Multiple Attribute Decision Making: An Introduction, Vol. 104 Sage publications, Newbury Park, California, 1995.

[123] W. Yu, ELECTRE TRI–aspects méthodologiques et guide d'utilisation, Document du LAMSADE, vol. 74, Université de Paris-Dauphine, Paris, 1992.

[124] E.K. Zavadskas, Z. Turskis, J. Tamošaitiene, V. Marina, Multicriteria selection of project managers by applying grey criteria, Technol. Econ. Dev. Econ. 14 (4) (2008) 462–477.

[125] S.H. Zolfani, N. Rezaeiniya, M.H. Aghdaie, E.K. Zavadskas, Quality control man ager selection based on AHP-COPRAS-G methods: a case in Iran, Econ. Res. Ekonomska istraživania 25 (1) (2012) 72–86.

![](/api/attachments/HPEJDPHV/fulltext/images/fdab6077806196383b59bb8118be1974c69cb4aad2f1e6cd94e6ee315fcb264d.jpg)  
Husevin S. Kilic works in the department of industrial engineering in Marmara University. He received his BSc MSc and PhD degrees in Industrial Engineering from Istanbul Technical University. He studied in-plant logistics design for his PhD dissertation. His main research areas are plant logistics, reverse logistics, lean production, decision making techniques and ergonomics. He has research papers in journals that include Applied Mathematical Modelling, Computers and Industrial Engineering, Decision Support Systems, International Journal of Advanced Manufacturin Technology, and Assembly Automation.

![](/api/attachments/HPEJDPHV/fulltext/images/752b266bd012b096c174ec96ffd6cc2ad095069c132660ae02bd490a68c9b695.jpg)

Ayse E. Demirci works for Benson & Partners - IESF Executive Search & Management Advisory Company as a research associate. She has received her bachelor's degree in Industrial and Systems Engineering at Yeditepe University, Istanbul, Turkey. She has completed her thesis titled “A Decision Support System Design for Quality Control.” Afterwards, she has studied decision making techniques for personnel selection in her master thesis titled “An Integrated Approach Based on ANP, DEMATEL and ELECTRE Methodologies for Personnel Selection with an Application in Industry” at Marmara University, Industrial Engineering Department. Her research areas include per sonnel selection, decision making techniques, quality conohain syst

trol techniques and supply chain systems.  
![](/api/attachments/HPEJDPHV/fulltext/images/e2b3561279a1655106e30d2f9d438cedb36675a26a5f55f5c14f4bb3929875d8.jpg)

Dursun Delen is the holder of Spears and Patterson Endowed Chairs in Business Analytics, Director of Research for the Center for Health Systems Innovation, and Regents Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University. He has authored/co-authored more than 100 journal papers and numerous peer-reviewed conference proceeding articles. His research has appeared in major journals including Decision Sciences, Journal of Production Operations Management, Decision Support Systems, Communications of the ACM. Computers and Operations Research, Computers in Industry, Journal of the American Medical Informatics Association, Artificial Intelligence in Medicine, International Journal of Medical Informatics,

Health Informatics Journal, among others. He has published 10 books/textbooks in the broad area of Business Intelligence and Business Analytics. He is often invited to national and international conferences and symposiums for keynote addresses, and companies and government agencies for consultancy/education projects on data science and business analytics related topics. Dr. Delen served as the general co-chair for the 4th International Conference on Network Computing and Advanced Information Management (held in Soul, South Korea), and regularly chairs tracks and mini-tracks at various information systems and analytics conferences. He is currently serving as the editor-in-chief, senior editor, associate editor and editorial board member on more than a dozen academic journals.
