---
otero_id: 13110
otero_key: "A3XMHUSP"
title: "Development of a hybrid methodology for ERP system selection: The case of Turkish Airlines"
authors: "Huseyin Selcuk Kilic; Selim Zaim; Dursun Delen"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.06.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Development of a hybrid methodology for ERP system selection: The case of Turkish Airlines

Huseyin Selcuk Kilic <sup>a</sup>, Selim Zaim <sup>b</sup>, Dursun Delen <sup>c,</sup>⁎

<sup>a</sup> Department of Industrial Engineering, Engineering Faculty, Marmara University, Kadikoy, Istanbul 34722, Turkey

<sup>b</sup> Department of Industrial Engineering, Faculty of Management, Istanbul Technical University, Macka, Istanbul 34367, Turkey

<sup>c</sup> Department of Management Science and Information Systems, Spears School of Business, Oklahoma State University, Tulsa, OK 74106, USA

## a r t i c l e i n f o

Article history: Received 30 March 2013 Received in revised form 4 June 2014 Accepted 10 June 2014 Available online 28 June 2014

Keywords: ERP MCDM Fuzzy logic AHP TOPSIS Airline industry

## a b s t r a c t

Enterprise resource planning (ERP) systems that aim to integrate, synchronize and centralize organizational data are generally regarded as a vital tool for companies to be successful in the rapidly changing global marketplace Due to its high acquisition—purchasing, installation and implementation—cost and the wide range of offerings, the selection of ERP systems is a strategically important and dif<sup>fi</sup>cult decision. Since there is a wide range of tangible and intangible criteria to be considered, it is often de<sup>fi</sup>ned as a multi-criteria decision making problem. To overcome the challenges imposed by the multifaceted nature of the problem. herein a three-stage hybrid methodology is proposed. The process starts with the identi<sup>fi</sup>cation of most prevailing criteria through a series of brainstorming sessions that include people from different organizational units. Then, due to the varying importance of the criteria, a fuzzy Analytic Hierarchy Process, which handles the vagueness inherent in the decision making process, is used to obtain the relative importance/weights of the criteria. These weighted criteria are then used as input to the Technique for Order Preference by Similarity to Ideal Solution method to rank the decision alternatives. As a real-world illustrative case, the proposed methodology is applied to the ERP selection problem at Turkish Airlines. Because of the collaborative and systematic nature of the methodology, the results obtained from the process were found to be highly satisfactory and trustworthy by the decision makers.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Undoubtedly, one of the most important and impactful developments in information technology in 1990s is the advent of ERP systems. Transforming the organizational structure of enterprises from functionally-focused to process-driven infrastructures, ERP has turned out to be one of the most extensively adopted/used business solutions of the recent history [3]. Although the positive effect of ERP-based IT systems became clear in the late 1990's [48], the importance of inventory control—which can be regarded as one of the <sup>fi</sup>rst main activity of modern manufacturing systems—has taken place in 1960s. That was followed by Materials Requirement Planning (MRP), in 1970s and Manufacturing Resources Planning (MRP II) in 1980s [45]. As a result, the use and the importance of computing information systems and their applications to improve effectiveness and ef<sup>fi</sup>ciency of business functions have increased signi<sup>fi</sup>cantly. Furthermore, because of the exponential increase in the competition in the globalized economy, coupled with ever so changing customer needs and wants, the complexity of the business processes has also risen. These all have led to ERP systems becoming an essential part of any modern day solution to the increasingly complex business environment [20].

By adopting ERP, it is aimed to plan and integrate the related resources of all the departments in an organization by combining the applications and work processes [16]. In other words, controlling the information within the whole company is considered as the main objective of ERP implementation [15,31]. The bene<sup>fi</sup>ts that can be obtained by implementing a successful ERP system are automated business process, timely access to management information and improved supply chain management through the use of e-commerce [26]. Moreover, productivity and working quality are increased via ERP systems by providing integration, standardization and simpli<sup>fi</sup>cation of processes [28]. Mostly because of these advantages, ERP systems are also being used in the small and medium enterprise and are regarded as a way of becoming and maintaining competitiveness [10].

Generally speaking, there are three phases that constitute ERP system life cycle. These phases are selection, implementation and use. Problem identi<sup>fi</sup>cation, requirements speci<sup>fi</sup>cation, evaluation of options and selection of system can be regarded as the activities within the ERP selection process. ERP selection is the <sup>fi</sup>rst phase and is regarded as the most critical success factor for ERP implementation [14].

There have been a number of methods used in the selection of the best ERP system for an organization. Some of the most popular ones are the scoring and ranking methods, mathematical optimization models and multi-criteria decision making models [44]. In addition to these individual models, hybrid methodologies are also used for selecting the best ERP systems [35]. Regardless of the method, during the selection process many criteria are taken into consideration. Some of the most prevailing criteria used in the selection of ERP system included product functionality, product quality, implementation speed, implementation approach, organizational credibility, experience, <sup>fl</sup>exibility, interface with other systems, price, market leadership, corporate image, and international orientation [33,46]. The nature and the importance given to each selection criterion change among these studies. As Baki and Çakar [4] stated, in some of the studies, the most important criteria are functionality and system reliability while, according to the other studies, the most important criterion is technical support for large <sup>fi</sup>rms and adaptability and <sup>fl</sup>exibility of software for small-tomedium sized companies.

Due to the crucial role that ERP systems play in today's organizations, the selection of the “right” system—that <sup>fi</sup>ts the needs and capabilities of the enterprise—is regarded as a critical and complex decision problem. With this study, we propose a fuzzy AHP weighted TOPSIS methodology to overcome the complexities of this decision making process. Even though there are a number of studies where Fuzzy, AHP and TOPSIS techniques are used individually or in some combination in the literature, this study offers additional contributions to the extant literature. First, to the best of our knowledge, this study is the <sup>fi</sup>rst to offer a systematic, easy to understand/apply three-stage MCDM methodology that consists of pre-evaluation, fuzzy AHP, and TOPSIS. Second, although there are a lot of successful applications of TOPSIS and/or AHP to wide range of MCDM problems in various industries/<sup>fi</sup>elds, there is not an application of Fuzzy AHP weighted TOPSIS methodology for the ERP selection problem (as can be inferred from the 266 articles analyzed in the study conducted by Behzadian et al. [5]). Third, an application case of the hybrid methodology is performed in a large-scale high-stake decision situation for an airline company (i.e., Turkish Airlines) to select the best possible ERP system. As it is known, case studies play a signi<sup>fi</sup>- cant role in demonstrating the ef<sup>fi</sup>cacy of new and improved methodologies in real life contexts. The chief reason is that the vast majority of real-world MCDM decision making problems are too complex to be solved “optimally” using closed-form solutions. At best, what we can do is to represent as much of the fuzzy/multifaceted nature of the real-world situation as we possibly can, and employ proven heuristic techniques in combination to solve the problem at its richest and most realistic representation. By doing so, we would hope to achieve a good solution that not only addresses the problem but also fosters high level of trust and con<sup>fi</sup>dence in everyone involved in the decision making process. Overtime, successful implementation of real-world cases such as the one included in this study help build knowledge repositories for speci<sup>fi</sup>c problem types (ERP selection problem, in this case) to learn from and to benchmark against.

The rest of the paper is organized as follows. A comprehensive literature review is provided in Section 2. The fundamentals about Fuzzy AHP and TOPSIS are explained in Section 3 and Section 4, respectively. Proposed hybrid methodology is presented and explained in Section 5. A detailed application case is provided in Section 6, and <sup>fi</sup>nally the conclusions and future research directions of the study are given in Section 7.

## 2. Literature review

Since the earliest developments of ERP systems have only emerged in the 1990s [3], the ERP studies and related literature are not old, but rather large. The literature about ERP systems can be analyzed under four main categories: ERP selection, ERP implementation, ERP risk management and general ERP projects. The published research on ERP system selection (as is the case in this study) and implementations constitute roughly about 75% of all published studies [2]. In order to provide a good coverage of the related literature in a concise manner, the scope of the review will be focused on the studies related speci<sup>fi</sup>cally to ERP system selection problem (however, as needed for completeness sake, other studies that relate to different but associated areas will also be cited).

There are a large number of research studies that investigate ERP related issues, from selection to adaption, while others study the research landscape of the phenomenon. For instance, Al-Mashari [3] provided a research agenda and a timeline for the need for further studies about ERP systems by investigating the published studies. He particularly focused on three subject areas: ERP adoption, technical aspects of ERP and ERP in IS curricula. Wei and Wang [50] developed a comprehensive methodology which considers both subjective and objective criteria while choosing the ERP software. By bene<sup>fi</sup>ting from the fuzzy set theory, quantitative criteria are regarded. An indicator called “fuzzy ERP suitability index” was used for determining the suitability of ERP alternatives and criteria importance weights. Baki and Çakar [4] determined the ERP selection criteria and obtained the importance/weights of the criteria by a survey among the <sup>fi</sup>rms in Turkey. A methodology including the critical factor assessment for the success of ERP implementation was proposed by Sun et al. [41].

Genoulaz et al. [15] performed a literature review about ERP systems. The literature was analyzed with respect to six categories such as implementation of ERP, optimization of ERP, management through ERP, the ERP software, ERP for supply chain management and case studies. Motwani et al. [32] <sup>fi</sup>rstly analyzed the properties and problems of the ERP implementation based on literature and case studies and then presented a framework showing the critical factors to be considered during all the phases of the implementation process. Verville et al. [49] investigated the critical success factors for the successful acquisition of ERP systems by conducting a survey among three organizations. Wei et al. [51] proposed an AHP based methodology for supplier selection problem. Ziaee et al. [56] presented a two stage approach. In the <sup>fi</sup>rst stage, ERP system properties are determined by collecting information about the possible ERP sellers. In the second stage, a mathematical model was proposed for minimizing the total cost related with procurement and integration.

Finney and Corbett [13] provided a literature review about the critical success factors in ERP implementation and analyzed them. Liao et al. [26] developed an ERP system selection model based on linguistic information processing. A survey was conducted by Velcu [48] to investigate the effects of ERP systems on the organization performance. Wu et al. [53] proposed an ERP selection methodology based on the tasktechnology <sup>fi</sup>t theory. With the help of the proposed methodology, it became easier to determine the locations of possible mis<sup>fi</sup>t. Factors important for the successful implementation of ERP systems were determined and discussed by Yang et al. [54].

Chou and Chang [9] determined the factors in<sup>fl</sup>uencing the ERP selection. Deep et al. [10] investigated the factors in the ERP selection for SME sector. Analytic Network Process (ANP) was used as a decision making tool for ERP selection problem by Perçin [35]. Razmi et al. [36] used fuzzy ANP for determining the readiness of an organization for ERP implementation. Saatçioğlu [37] analyzed the effects of bene<sup>fi</sup>ts, barriers and risks to the user satisfaction in ERP systems. Ünal and Güner [46] used AHP for ERP supplier selection in clothing industry. Şen et al. [42] proposed a combined decision making methodology handling both quantitative and qualitative factors via fuzzy set theory and random experiment based solution. Yazgan et al. [55] developed an ERP software selection methodology based on arti<sup>fi</sup>cial neural network and analytic network process.

A strategic modeling plan for the evaluation and selection of ERP systems was presented by Hakim and Hakim [17]. Best practices for the critical decisions in ERP selection and implementation were offered by Malhotra and Temponi [30]. Doom et al. [11] identi<sup>fi</sup>ed the success factors for ERP implementations in Belgian SMEs. Forslund and Jonsson [14] performed a study for obtaining the effects of different ERP life cycle phases on supply chain performance management. Maguire et al. [29] analyzed the environmental factors that are effective on the ERP implementation by conducting a case study in a <sup>fi</sup>rm. Schlichter and Kraemmergaard [39] presented a methodological framework for performing literature review about ERP studies. With respect to the proposed framework, the situation of ERP studies was determined. Şen and Baraçlı [43] developed a methodology based on fuzzy quality function deployment for determining the non-functional requirements in the ERP selection process. Factors affecting ERP system implementation effectiveness were investigated by Maditinos et al. [28]. Wickramasinghe and Karunasekara [52] determined the post-implementation effect of ERP systems on work regarding factors such as “problem solving support”, “job discretion, management visibility and cross-functionality”, and “authority and decision rights”.

The literature cited herein is just an exemplary sample of what has been studied in the area of ERP system selection. The quantity and quality of the published articles in this <sup>fi</sup>eld are a testament to both importance and the complexity of the ERP system selection problem. What differentiates our approach from the ones conducted previously is the following: <sup>fi</sup>rst, we developed and presented a systematic three-stage hybrid methodology to better guide the section process. Second, we combined the strengths and mitigated the weaknesses of two popular decision making methods—fuzzy AHP and TOPSIS—to better capture and represent the richness of the reality in the decision making process. Finally, we applied the proposed hybrid methodology to a highstake real-world decision making situation at a large airline company (i.e., Turkish Airlines) to illustrate its applicability and utility.

## 3. Fuzzy AHP

Analytic Hierarchy Process (AHP) developed by Saaty [38] has been one of the most widely used techniques for multi-criteria decision making problems. The priority values of both objective and subjective factors are obtained via pair-wise comparisons. There are mainly four consecutive levels in the AHP method. In the <sup>fi</sup>rst level, there is the objective function. In the second level, there are the attributes. In the third level, there are the sub-attributes and <sup>fi</sup>nally, in the last level, there are the alternatives [25].

Since crisp values are used in the AHP method, it is unable to handle the vagueness in the fuzzy decision making environment. Due to this reason, Fuzzy Analytic Hierarch Process (F-AHP) which utilizes fuzzy set theory introduced by Zadeh (1965) [57] was developed. There are numerous F-AHP approaches proposed by various authors. The earliest one is presented by van Laarhoven & Pedrycz [47] comparing fuzzy ratios described by triangular membership functions. Buckley [7] determined fuzzy priorities of comparison ratios having trapezoidal membership functions. Chang [8] proposed a new approach utilizing triangular fuzzy numbers for pair-wise comparison scale of F-AHP. Similar approaches are then proposed by different authors as well [6]. F-AHP with these various approaches are used in numerous studies including different applications such as job selection [22], energy alternatives selection [19], performance assessment systems in municipalities [21,23], supplier selection [25], among others.

Triangular fuzzy preference scale.

<table><tr><td>Saaty&#x27;s scale</td><td>Definition</td><td>Triangular fuzzy scale</td></tr><tr><td>1</td><td>Equally importance</td><td>(1, 1, 1)</td></tr><tr><td>3</td><td>Moderate importance of one over another</td><td>(2-4)</td></tr><tr><td>5</td><td>Essential or strong importance</td><td>(4-6)</td></tr><tr><td>7</td><td>Demonstrated importance</td><td>(6-8)</td></tr><tr><td>9</td><td>Extreme importance</td><td>(9, 9, 9)</td></tr><tr><td>2</td><td>Intermediate values between two adjacent judgments</td><td>(1-3)</td></tr><tr><td>4</td><td>Intermediate values between two adjacent judgments</td><td>(3-5)</td></tr><tr><td>6</td><td>Intermediate values between two adjacent judgments</td><td>(5-7)</td></tr><tr><td>8</td><td>Intermediate values between two adjacent judgments</td><td>(7-9)</td></tr></table>

In this study, F-AHP is used to <sup>fi</sup>nd the importance/weights of the selection criteria for ERP systems. To apply F-AHP, the procedure proposed by Buckley [7] is used and the steps of the procedure are as follows:

Step 1: Two elements (criteria or alternatives) are compared by the decision makers at each time by the linguistic scale which consists of the fuzzy preference scale as shown in Table 1 [34].

Let $\widetilde { d } _ { \mathrm { i j } } ^ { k }$ represent a set of the kth decision maker's preference of one element (i) over another (j) then; the pair-wise comparison matrices are constructed as shown in the Eq. (1).

$$
\widetilde {A} ^ {k} = \left[ \begin{array}{c c c c} \widetilde {d} _ {1 1} ^ {k} & \widetilde {d} _ {1 1} ^ {k} & ... & \widetilde {d} _ {1 n} ^ {k} \\ \widetilde {d} _ {2 1} ^ {k} & ... & ... & \widetilde {d} _ {2 n} ^ {k} \\ \ddots & \ddots & ... & \ddots \\ \widetilde {d} _ {n 1} ^ {k} & \widetilde {d} _ {n 2} ^ {k} & ... & \widetilde {d} _ {n n} ^ {k} \end{array} \right].\tag{1}
$$

Step 2: The arithmetic average $( \widetilde { d } _ { \mathrm { i j } } )$ of K decision makers' judgment values are computed as stated in the Eq. (2).

$$
\widetilde {d} _ {\mathrm{ij}} = \frac {\sum_ {k - 1} ^ {K} \widetilde {d} _ {\mathrm{ij}} ^ {k}}{\mathrm{K}}.\tag{2}
$$

Step 3: The fuzzy weights of each criterion are obtained via the geometric mean method proposed by Buckley [7].

Firstly, the geometric mean of fuzzy comparison value of criterion i to each criterion is computed as shown in the Eq. (3).

$$
\widetilde {r} _ {\mathrm{i}} = \left(\prod_ {\mathrm{j} = 1} ^ {n} \widetilde {d} _ {\mathrm{ij}}\right) ^ {1 / n}, i = 1, 2, \dots , n.\tag{3}
$$

Then, the fuzzy weight of the ith criterion represented by a triangular fuzzy number is found as in the Eq. (4).

$$
\begin{array}{c} \widetilde {w} _ {i} = \widetilde {r} _ {i} \otimes (\widetilde {r} _ {1} \oplus \widetilde {r} _ {2} \oplus \dots \oplus \widetilde {r} _ {n}) ^ {- 1} \\ = (l w _ {i}, m w _ {i}, u w _ {i}). \end{array}\tag{4}
$$

Step 4: Centre of Area (COA) method is used as the defuzzi<sup>fi</sup>cation method [9]. The nonfuzzy value M of the fuzzy numberw can be obtained via the Eq. (5):

$$
M _ {i} = \frac {l w _ {i} + m w _ {i} + u w _ {i}}{3}\tag{5}
$$

M<sub>i</sub> is a nonfuzzy number. The normalized weights N<sub>i</sub> are found by normalization.

Step 5: After obtaining each N , the global weights of all criteria W are obtained by multiplying the local normalized weights of criteria by the normalized weights of the related dimension.

## 4. TOPSIS

One of the famous multi criteria decision making techniques is perhaps the TOPSIS method, which is <sup>fi</sup>rst proposed by Hwang and Yoon [18]. In this method, the alternatives are ranked based on the distances from positive and negative ideal solutions. The best alternative is deemed to be the one having the nearest distance to the positive ideal solution and the farthest distance from the negative one [40]. Similar to AHP, there are a lot of applications of TOPSIS in various <sup>fi</sup>elds such as customer driven product design process [27], performance evaluation of cement <sup>fi</sup>rms [12], machine layout in cellular manufacturing system [1], and supplier selection [24]. The speci<sup>fi</sup>c steps of the methodology applied in the study are as follows:

Step 1: A decision matrix consisting of the evaluation values $( \mathrm { x _ { i j } } )$ of each alternative with respect to each criterion is normalized and $\Gamma _ { \mathrm { i j } }$ which represents the normalized criteria rating (i represents alternatives, j represents criteria) is obtained as in Eqs. (6) and (7).

$$
r _ {i j} = \frac {\frac {1}{x _ {i j}}}{\sqrt {\sum_ {i = 1} ^ {m} \frac {1}{x _ {i j} ^ {2}}}}, i = 1, 2, 3, \dots , m; j = 1, 2, 3, \dots , n \text {   for   minimization   objective }\tag{6}
$$

$$
r _ {i j} = \frac {x _ {i j}}{\sqrt {\sum_ {i = 1} ^ {m} x _ {i j} ^ {2}}}, i = 1, 2, 3,..., m; j = 1, 2, 3,..., n \text { for   maximization   objective } \tag {7}
$$

Step 2: Weighted normalized decision matrix is computed by applying the Eq. (8).

$$
v _ {i j} = r _ {i j} * w _ {j}, i = 1, 2, 3, \dots , m; j = 1, 2, 3, \dots , n\tag{8}
$$

Step 3: Positive ideal solution $( \mathrm { P I S } , \boldsymbol { \mathsf { A } } ^ { * } )$ and negative ideal solution (NIS, A<sup>−</sup>) are determined as indicated in the Eqs. (9) and (10).

$$
A ^ {*} = \left\{v _ {1} ^ {*},..., v _ {n} ^ {*} \right\} \text { maximum   values }\tag{9}
$$

$$
A ^ {-} = \left\{v _ {1} ^ {-},..., v _ {n} ^ {-} \right\} \text { minimum   values }\tag{10}
$$

Step 4: The distance of each alternative from positive ideal solution and negative ideal solution is computed as in the Eqs (11) and (12).

$$
d _ {i} ^ {*} = \sqrt {\sum_ {j = 1} ^ {n} \left(v _ {i j} - v _ {j} ^ {*}\right) ^ {2}}, i = 1, \dots , m\tag{11}
$$

$$
d _ {\mathrm{i}} ^ {-} = \sqrt {\sum_ {\mathrm{j} = 1} ^ {n} \left(v _ {\mathrm{ij}} - v _ {\mathrm{j}} ^ {-}\right) ^ {2}}, \mathrm{i} = 1, \dots , m\tag{12}
$$

Step 5: The relative closeness of each alternative with respect to the ideal solution is computed as in the Eq. (13).

$$
\mathrm{CC} _ {\mathrm{i}} = \frac {d _ {i} ^ {-}}{d _ {\mathrm{i}} ^ {*} + d _ {\mathrm{i}} ^ {-}}, \mathrm{i} = 1, \dots , m\tag{13}
$$

Step 6: The alternatives are ranked with respect to the values of CC and the biggest one is chosen as the best alternative.

## 5. Proposed hybrid methodology

The proposed hybrid methodology, consisting of three stages, has two main modeling components which are named as fuzzy AHP (a combination of fuzzy logic and AHP methods) and TOPSIS approaches. Since the decision making environment is usually fuzzy/uncertain in most multi-criteria decision making problems (with respect to the subjectivity of the criteria to be included in the process), instead of making unrealistic assumptions to justify a simpli<sup>fi</sup>ed non-fuzzy solution, we choose to use fuzzy logic and by doing so we aimed to capture the imprecision inherent in the decision situation. Furthermore, in order to cope with the size and complexity of the multi-criteria nature of the decision situation, we employed a hybrid methodology that takes advantage of the strengths of multiple complementary methods. The reason behind choosing the combination of fuzzy AHP and TOPSIS is based on these modeling techniques' strengths and suitability to the current decision situation. Selecting the most suitable (i.e., “the best”) ERP system is a complex and challenging decision in any industry. Each of these techniques brings capabilities as well as shortcomings to address speci<sup>fi</sup>c characteristics of this decision situation, including it being a highly complex multi criteria decision situation that requires the involvement of a group of decision makers and is mostly characterized by a number of non-deterministic (i.e., fuzzy) measures. Even though individually these MCDM techniques have their shortcomings, a methodology that synergistically combines the strengths of these techniques while mitigating the shortcomings is what is proposed herein as a logical MCDM solution to this complex problem. The speci<sup>fi</sup>c reason for systematically combining these techniques in our study can be explained as follows: within the <sup>fi</sup>rst stage of the problem, where the structure of the problem is determined, the decisions/tasks/criteria are naturally judgmental. This is where we determine the weights of the criteria, a technique that is capable of evaluating both tangible and intangible factors is needed, and at this point a highly regarded technique “fuzzy $\mathsf { A H P } ^ { \prime }$ which is also capable of incorporating vagueness/ imprecision of the decision situation is employed. In the following stage, another popular technique $" \mathrm { T O P S I S " }$ is used to evaluate and rank decision alternatives (using 1–10 evaluation scale). In short, they are complementary techniques and as explained, each of them provides a solution to different requirements of the decision making process. Besides the strength and suitability of these techniques, another motivation for using these techniques collectively is that, to the best of our knowledge, this is the <sup>fi</sup>rst study that uses fuzzy logic, AHP and TOPSIS for a complex and high-stake decision situation like ERP system selection problem. In a recent study Behzadian et al. [5] reviewed the use of these MCDM techniques in a variety of applications. Their study indicated that although there are a number of applications using TOPSIS and AHP either individually or collectively, there is not an application where all three are used collectively and/or on the ERP selection problem, based on the 266 articles that they had analyzed in their study.

The main stages of the proposed methodology (which shown in Fig. 1) can brie<sup>fl</sup>y be summarized as follows: The <sup>fi</sup>rst stage is to determine the criteria with respect to the requirements (needs and wants) of the company. The second stage is where the importance/weights of all the criteria are obtained via fuzzy AHP methodology, output of which is then used as input to the TOPSIS method. The third and the <sup>fi</sup>nal stage is where the best ERP software package is determined by utilizing TOPSIS methodology.

## 6. Application case

An application of the proposed hybrid methodology is performed at Turkish Airlines (THY), which is the largest airline company in Turkey, and one of the largest airlines in Europe. THY wanted to select an ERP system/package/vendor speci<sup>fi</sup>cally for its maintenance center, which is located at its hub Atatürk International Airport in Istanbul. The Turkish Airlines Maintenance Center, called THY Technic, is responsible for the maintenance, repair, and overhaul of THY's aircrafts, engines, and components.

To get the process started, <sup>fi</sup>rst of all, within the pre-evaluation stage, a focus group (it was also called the steering committee) consisting of managers at different managerial levels within the organization who are related to and are interested in the ERP system selection process is formed. Throughout the study, the decisions are made within this focus group of 35 people. After forming the focus group, <sup>fi</sup>rstly the criteria that represent the rich set of requirements and demands of the company executives are determined and organized under three main groups: technical criteria, corporate criteria and <sup>fi</sup>nancial criteria.

![](/api/attachments/A3XMHUSP/fulltext/images/a56be576d5257f84a5845871a78b2edf2e924d7e7b1366790b058d8c3802a748.jpg)  
Fig. 1. The main structure of the proposed hybrid methodology.

The sub-criteria under each main group/criterion are listed and brie<sup>fl</sup>y described here:

## 6.1. Technical criteria

Functionality: Under the functionality sub-criterion:

• The ERP package should be operable on multi-language and multicurrency basis.

• It should have such a structure as to enable running of certain applications or obtaining certain reports in a periodic manner.

• There should be structures recording many different characteristics of the materials and searching accordingly.

• Without destroying data integrity and coherence, it should be possible to make retroactive changes on data such as switching a completed purchase order to “open” status.

Compatibility: Under the compatibility sub-criterion:

• The program should be runnable on any Java Application Server, and reach the application via any internet browser.

• It should run on every operating system and should be compatible with all relational databases.

• It should be able to support applications such as SMS and should enable communication with customers and suppliers via e-mail or facsimile.

• It should run in an integrated manner with other software currently in use. In data communication, it should be able both to receive data from outside, as well as send data to external programs.

• It should be possible to transfer existing data in the current information systems to the new system initially.

• The software should consist of independent modules, and such modules should run both in integration as well as independent from one another. Within the framework of project plan, certain modules should possibly be put into operation later. All modules shall be fully compatible to each other.

Usability: Under the usability sub-criterion:

• Screen ergonomics of the software should be simple and consistent; all screens should have similar structures. It should be possible that more than one transaction is open at the same time, and it should be possible to shift between open transactions.

• Users should have access related help <sup>fi</sup>le from any transaction, helps <sup>fi</sup>les should relate in a simple wording understandable to the user.

• User should be capable of changing standard reports and forms. Data <sup>fi</sup>elds in the reports shall been able to be switched on and off.

• It should be possible to use visual elements such as charts, tables, and graphics when preparing a report for the results of data analysis and outputs of plan.

• Visual reporting should possibly be made. Gantt charts, graphics and such similar structures should possibly be created by users in a parametric manner.

Accessibility: Under the accessibility sub-criterion:

• The client should be able to access the ERP software without loading any program, over any hardware (desktop, hand terminal or notebook).

• Open source program codes are a substantial reason for preference.

• At later stages of the project, the software should provide access fo customers and suppliers for external utilization, as well as data input via barcode.

Security: Under the security sub-criterion:

• It should have at least 128 bit SSL Technology in terms of security.

• With respect to user authorization, authorization should be possible both in transaction basis as well as all <sup>fi</sup>elds or controls on the relevant transaction basis.

• Unused or expired data's should be removed from up to dated system and be archived without damaging the integrity of data.

• Operation performance of the software under a speci<sup>fi</sup>c user number and speci<sup>fi</sup>c data intensity should be good enough.

## 6.2. Corporate criteria

References: Under the references sub-criterion:

• Number of users using software of the company and number of projects realized should be good enough.

• In the event it is requested, the company shall provide letters of reference in connection with the projects it gave as reference, and relevant company shall be visited together for project investigation.

Adequacy of advisors and developers: Under the adequacy of advisors and developers sub-criterion:

• Number of the company's advisor and developers shall be suf<sup>fi</sup>cient that whenever required there shall be no problem in timely getting the service.

• Besides quantity, quality of advisors should be suf<sup>fi</sup>cient.

After sales service: Under the after sales service sub-criterion:

• The company should undertake to hold a consultancy and development of<sup>fi</sup>ce in Istanbul for a period of 3 years.

• It shall continue to develop and release new versions of the software and shall undertake to provide technical, maintenance and consultancy support to the existing version to be utilized in the project for a period of at least 10 years.

• Any working error to occur on the software and arising from codes shall be intervened within shortest notice and solution shall be provided as soon as possible.

• The company shall also respond to support requirements which may arise at new locations or locations abroad in the future.

Know-how sharing policy: Under the know-how sharing policy sub-criterion:

• Development environment utilized by the company is important, and by means of providing development training the company shall transfer such know-how to THY.

## 6.3. Financial criteria

Cost of the project should be assessed as the total of software, hardware and network costs. License cost, consultancy and training cost and maintenance cost comprising the software cost are such criteria to be assessed in detail.

Besides the criteria, four alternative <sup>fi</sup>rms are considered for the evaluation process. These four <sup>fi</sup>nalists were determined out of 12 <sup>fi</sup>rms that submitted full proposal to the formal RFP. Evaluation process included a thorough investigation of the <sup>fi</sup>rms' past performances, selfreferences, and independent industry studies. The <sup>fi</sup>nal four <sup>fi</sup>rms were AMOS, MXI, SAP and TRAX (listed alphabetically). In order to provide objectivity among the participants and the con<sup>fi</sup>dentiality of the <sup>fi</sup>rms, the alternatives were not explicitly named in the evaluation process, instead represented by letters A, B, C and D. The analytic hierarchy tree constructed for this problem is shown as in Fig. 2.

After the pre-evaluation stage, the steps of fuzzy AHP and TOPSIS are performed sequentially as explained in the following sub-sections.

Fuzzy AHP — Step 1: The steps of fuzzy AHP are performed to obtain the importance/weights of the criteria. The pair-wise comparisons for main criteria and the sub-criteria under each main criterion are determined.

The pair-wise comparisons based on the triangular fuzzy numbers for the three main criteria are determined as shown in Table 2 with the consensus of the decision makers.

The pair-wise comparisons based on the triangular fuzzy numbers for the sub-criteria under the technical main criterion are determined as shown in Table 3 with the consensus of the decision makers.

The pair-wise comparisons based on the triangular fuzzy numbers for the sub-criteria under the corporate main criterion are determined as shown in Table 4 with the consensus of the decision makers.

The pair-wise comparisons based on the triangular fuzzy numbers for the sub-criteria under the <sup>fi</sup>nancial main criterion are determined as shown in Table 5 with the consensus of the decision makers.

Fuzzy AHP — Step 2: For main and sub-criteria, the fuzzy weights (w ) are obtained after <sup>fi</sup>nding the geometric mean of fuzzy comparison values (r ) for each criterion.

The related $\widetilde { \boldsymbol { r } } _ { i }$ and $\widetilde { w } _ { i }$ values for each main criterion are shown in Table 6.

The related $\widetilde { \boldsymbol { r } } _ { i }$ and $\widetilde { w } _ { i }$ values for each sub-criterion are shown in Table 7.

Fuzzy AHP — Step 3: The non-fuzzy values (M ) of $\widetilde { w } _ { i }$ values and the normalized weights N are obtained for the main and sub-criteria. The related $\mathrm { M _ { i } }$ and N values for each main criterion are shown in Table 8.

The related M and N values for each sub-criterion are shown in Table 9.

Fuzzy AHP — Step 4: The global weights of all criteria $W _ { i }$ are computed by multiplying the local normalized weights of the criteria by the related dimension's normalized weights which are shown in Table 10.

For example, for obtaining the global importance weight of “functionality”, the local importance weight of functionality (0.369) is multiplied by the weight of the related dimension which is the importance weight of the technical criterion (0.405) and the global importance weight of functionality is obtained as 0.149 as shown in Table 11.

After obtaining the weights of the criteria via fuzzy AHP, TOPSIS methodology is performed to select the best alternative.

TOPSIS — Step 1: In this step, decision matrix as shown in Table 12 including the ratings of alternatives with respect to each criterion from 1 to 10 scales is normalized. While Company A was found to have a relatively better performance in terms of usability and accessibility, Company C had a better performance in terms of license, consultancy and maintenance. Company D, however, outperformed the other three companies in terms of functionality and references.

Using Eq. $( 7 ) ,$ normalized decision matrix is obtained depending on the maximization of selection criterion. The normalized decision matrix is shown in Table 13.

![](/api/attachments/A3XMHUSP/fulltext/images/070ca1f115bc1cb6e540667032ce8cfd6b06389fb26991c8046f65b9546eb805.jpg)  
Fig. 2. The hierarchical structure for the selection of ERP system.

TOPSIS — Step 2: Within the second step, the weighted normalized decision matrix is obtained as shown in Table 14.

TOPSIS — Step 3: The positive and negative ideal solutions are obtained for each criterion as shown in Table 15.

TOPSIS — Step 4: The distances of each alternative from positive and negative ideal solutions are obtained as shown in Table 16.

TOPSIS — Step 5: The relative closeness of each alternative with respect to the ideal solution is obtained as in Table 17.

TOPSIS — Step 6: The alternatives are ranked with respect to the values of CC from biggest to the smallest one and the ranking is obtained as A, D, C and B.

Regarding the last step of TOPSIS methodology, the alternative A is decided to be chosen as the ERP software for Turkish Airlines. This <sup>fi</sup>nding is not particularly surprising, as most ERP software evaluation decisions in maintenance are made today in increasingly complex environments where the theory of fuzzy decision-making can be of signi<sup>fi</sup>- cant use. In this study, the fuzzy AHP weighted TOPSIS methodology has been employed instead of using conventional TOPSIS approach.

## 7. Discussion and conclusion

Enterprise resource planning systems are making the enterprises more ef<sup>fi</sup>cient by integrating their cross-functional business processes over a common information system infrastructure. Having such an integrated information system allows stake holders to use the single version of the truth throughout the enterprise—small or large, local or multinational. Despite the obvious bene<sup>fi</sup>ts of an ERP system, many companies have failed to successfully implement it. In fact, many industry experts claim that about two-thirds of all ERP system initiatives were classi<sup>fi</sup>ed as unsuccessful; some are terminated before the completion, others were canceled shortly after the implementation. Some of the major reasons include higher than expected cost/time of implementation and the lack of suitability for the existing business practices.

Table 2  
Pairwise comparisons of the main criteria based on the triangular fuzzy numbers.

<table><tr><td>Main criteria</td><td>Technical criteria</td><td>Corporate criteria</td><td>Financial criteria</td></tr><tr><td>Technical criteria</td><td>(1, 1, 1)</td><td>(1-3)</td><td>(1, 1, 1)</td></tr><tr><td>Corporate criteria</td><td>(1/3, 1/2, 1)</td><td>(1, 1, 1)</td><td>(1, 1, 1)</td></tr><tr><td>Financial criteria</td><td>(1, 1, 1)</td><td>(1, 1, 1)</td><td>(1, 1, 1)</td></tr></table>

Because of the fact that there are a large number of ERP system offerings in the market place, each having different qualities and limitations, having a scienti<sup>fi</sup>cally sound selection process is a critical part of ERP system adoption/implementation. Depending on the size of the enterprise, and ERP system implementation may cost a few million dollars and may last up to six months to implement for smaller sizes, to costing hundreds of millions of dollars and lasting several years to fully implement for the large ones. Because it costs a great deal and it takes a long time to fully implement, ERP systems are among the most risky IT investment. Therefore, a thorough consideration of all options and criteria is not only an option but also a critical requirement to increase the likelihood of success.

Since there are a lot of criteria to be considered during this selection process, multi criteria decision making tools are widely to overcome this problem. In this study, an ERP system selection problem at a large airline company in Turkey is considered. First, based on the requirements and the demands of the company executives, the ERP selection criteria are determined. Then, the alternative ERP <sup>fi</sup>rms and their offerings are investigated and determined. After determining the criteria and solution alternatives, the proposed hybrid methodology, consisting of fuzzy AHP which incorporates the vagueness of the decision making process and TOPSIS, is applied and validated. Speci<sup>fi</sup>cally, the importance/ weights of the selection criteria are obtained via fuzzy AHP based on the triangular fuzzy preference scales. Then these weights are used in the TOPSIS methodology to reach the ranking of alternative ERP system suppliers.

The use of a hybrid selection/evaluation methodology proved to produce results that are both technically sound and organizationally acceptable. Knowing that the vagueness and complexity of the decision situation are handled using the strengths of two popular decision support methods makes the decision makers con<sup>fi</sup>dent in their <sup>fi</sup>nal selection. They feel that by breaking the complex problem space into smaller pieces, dealing with them at that granular level, and then aggregating them at the higher decision level have a much better chance of producing optimal (or near optimal) decisions.

It should be acknowledged that the present study is subject to some limitations. Perhaps the most serious limitation of this study is its narrow focus on a single case study in aviation industry. To generalize on the <sup>fi</sup>ndings and the viability/validity/value of the methodology, more

Table 3  
Pairwise comparisons of the technical criteria based on the triangular fuzzy numbers.

<table><tr><td>Technical criteria</td><td>Functionality</td><td>Compatibility</td><td>Usability</td><td>Accessibility</td><td>Security</td></tr><tr><td>Functionality</td><td>(1, 1, 1)</td><td>(2-4)</td><td>(1-3)</td><td>(2-4)</td><td>(2-4)</td></tr><tr><td>Compatibility</td><td>(1/4, 1/3, 1/2)</td><td>(1, 1, 1)</td><td>(1/3, 1/2, 1)</td><td>(1/3, 1/2, 1)</td><td>(1/3, 1/2, 1)</td></tr><tr><td>Usability</td><td>(1/3, 1/2, 1)</td><td>(1-3)</td><td>(1, 1, 1)</td><td>(1, 2, 3,)</td><td>(1-3)</td></tr><tr><td>Accessibility</td><td>(1/4, 1/3, 1/2)</td><td>(1-3)</td><td>(1/3, 1/2, 1)</td><td>(1, 1, 1)</td><td>(1/3, 1/2, 1)</td></tr><tr><td>Security</td><td>(1/4, 1/3, 1/2)</td><td>(1-3)</td><td>(1/3, 1/2, 1)</td><td>(1-3)</td><td>(1, 1, 1)</td></tr></table>

Table 4  
Pairwise comparisons of the corporate criteria based on the triangular fuzzy numbers.

<table><tr><td>Corporate criteria</td><td>References</td><td>Adequacy</td><td>After sales</td><td>Know-how</td></tr><tr><td>References</td><td>(1, 1, 1)</td><td>(1/3, 1/2, 1)</td><td>(1/3, 1/2, 1)</td><td>(1-3)</td></tr><tr><td>Adequacy</td><td>(1, 2, 3)</td><td>(1, 1, 1)</td><td>(1/3, 1/2, 1)</td><td>(1-3)</td></tr><tr><td>After sales</td><td>(1-3)</td><td>(1-3)</td><td>(1, 1, 1)</td><td>(1-3)</td></tr><tr><td>Know-how</td><td>(1/3, 1/2, 1)</td><td>(1/3, 1/2, 1)</td><td>(1/3, 1/2, 1)</td><td>(1, 1, 1)</td></tr></table>

real-world cases need to be performed. Another limitation of the individual methods is the independent structure of the selection criteria. Since the comparisons are made in a piece-meal/pairwise fashion, reaching the true optimal may not be possible. Also, for manageability purposes, various low-level criteria are grouped in clusters, by doing so, some detailed speci<sup>fi</sup>cations may have been lost. Finally, the methodology proposed in this study, as systematics as it may sound, is a heuristic one. That is, it does not guarantee <sup>fi</sup>nding the optimal solution. The “optimality” of the results is often subject to the richness (in terms of quantity and quality) of the participants; positively in<sup>fl</sup>uenced by their knowledge, experience and dedication.

For further studies, some of the other multi-criteria decision making techniques such as PROMETHEE, VIKOR and/or ELECTRE can be used in combination of (or with replacement to) the ones used in this study to assess the viability and utility of new hybrid methodologies. Another research direction would be to apply the proposed hybrid methodology to other MCDM situation to con<sup>fi</sup>rm its utility and generalizability.

Table 5  
Pairwise comparisons of the <sup>fi</sup>nancial criteria based on the triangular fuzzy numbers.

<table><tr><td>Financial criteria</td><td>License</td><td>Consultancy</td><td>Maintenance</td></tr><tr><td>License</td><td>(1, 1, 1)</td><td>(1/3, 1/2, 1)</td><td>(1-3)</td></tr><tr><td>Consultancy</td><td>(1-3)</td><td>(1, 1, 1)</td><td>(1-3)</td></tr><tr><td>Maintenance</td><td>(1/3, 1/2, 1)</td><td>(1/3, 1/2, 1)</td><td>(1, 1, 1)</td></tr></table>

Table 6  
The r and w values for the main criteria

<table><tr><td>Main criteria</td><td> $\widetilde{r}_{i}$ </td><td> $\widetilde{w}_{i}$ </td></tr><tr><td>Technical criteria</td><td>(1, 1.26, 1.44)</td><td>(0.29, 0.41, 0.54)</td></tr><tr><td>Corporate criteria</td><td>(0.69, 0.79, 1)</td><td>(0.20, 0.26, 0.37)</td></tr><tr><td>Financial criteria</td><td>(1, 1, 1)</td><td>(0.29, 0.33, 0.37)</td></tr></table>

Table 7  
The r and w values for the sub-criteria.

<table><tr><td>Sub-criteria</td><td> $\tilde{r}_{i}$ </td><td> $\tilde{w}_{i}$ </td></tr><tr><td>Functionality</td><td>(1.52, 2.22, 2.86)</td><td>(0.19, 0.39, 0.75)</td></tr><tr><td>Compatibility</td><td>(0.39, 0.53, 0.87)</td><td>(0.05, 0.09, 0.23)</td></tr><tr><td>Usability</td><td>(0.80, 1.32, 1.93)</td><td>(0.1, 0.23, 0.51)</td></tr><tr><td>Accessibility</td><td>(0.49, 0.70, 1.08)</td><td>(0.06, 0.12, 0.28)</td></tr><tr><td>Security</td><td>(0.61, 0.92, 1.35)</td><td>(0.08, 0.16, 0.35)</td></tr><tr><td>References</td><td>(0.58, 0.84, 1.32)</td><td>(0.09, 0.20, 0.47)</td></tr><tr><td>Adequacy</td><td>(0.76, 1.19, 1.73)</td><td>(0.12, 0.28, 0.62)</td></tr><tr><td>After sales</td><td>(1, 1.68, 2.28)</td><td>(0.16, 0.39, 0.82)</td></tr><tr><td>Know-how</td><td>(0.44, 0.59, 1)</td><td>(0.07, 0.14, 0.36)</td></tr><tr><td>License</td><td>(0.69, 1, 1.44)</td><td>(0.15, 0.31, 0.66)</td></tr><tr><td>Consultancy</td><td>(1, 1.59, 2.08)</td><td>(0.22, 0.49, 0.96)</td></tr><tr><td>Maintenance</td><td>(0.48, 0.63, 1)</td><td>(0.11, 0.2, 0.46)</td></tr></table>

Table 8  
The M and N values for the main criteria.

<table><tr><td>Main criteria</td><td>Mi</td><td>Ni</td></tr><tr><td>Technical criteria</td><td>0.413</td><td>0.405</td></tr><tr><td>Corporate criteria</td><td>0.278</td><td>0.272</td></tr><tr><td>Financial criteria</td><td>0.330</td><td>0.323</td></tr></table>

Table 9  
The M and N values for the sub-criteria.

<table><tr><td>Sub-criteria</td><td>Mi</td><td>Ni</td></tr><tr><td>Functionality</td><td>0.443</td><td>0.369</td></tr><tr><td>Compatibility</td><td>0.123</td><td>0.102</td></tr><tr><td>Usability</td><td>0.280</td><td>0.233</td></tr><tr><td>Accessibility</td><td>0.156</td><td>0.130</td></tr><tr><td>Security</td><td>0.197</td><td>0.164</td></tr><tr><td>References</td><td>0.254</td><td>0.205</td></tr><tr><td>Adequacy</td><td>0.340</td><td>0.274</td></tr><tr><td>After sales</td><td>0.457</td><td>0.368</td></tr><tr><td>Know-how</td><td>0.189</td><td>0.153</td></tr><tr><td>License</td><td>0.376</td><td>0.317</td></tr><tr><td>Consultancy</td><td>0.557</td><td>0.469</td></tr><tr><td>Maintenance</td><td>0.254</td><td>0.214</td></tr></table>

The importance/weights of the main criteria.

<table><tr><td>Main criterion</td><td>Importance weight</td></tr><tr><td>Technical</td><td>0.405</td></tr><tr><td>Corporate</td><td>0.272</td></tr><tr><td>Financial</td><td>0.323</td></tr><tr><td>TOTAL</td><td>1</td></tr></table>

Table 11  
The local and global importance/weights of the sub-criteria.

<table><tr><td>Main criteria</td><td>Sub-criteria</td><td>Local importance weight (Ni)</td><td>Global importance weight (Wi)</td></tr><tr><td rowspan="5">Technical</td><td>Functionality</td><td>0.369</td><td>0.149</td></tr><tr><td>Compatibility</td><td>0.103</td><td>0.042</td></tr><tr><td>Usability</td><td>0.233</td><td>0.094</td></tr><tr><td>Accessibility</td><td>0.13</td><td>0.053</td></tr><tr><td>Security</td><td>0.165</td><td>0.067</td></tr><tr><td rowspan="4">Corporate</td><td>References</td><td>0.205</td><td>0.056</td></tr><tr><td>Adequacy</td><td>0.274</td><td>0.075</td></tr><tr><td>After sales</td><td>0.368</td><td>0.100</td></tr><tr><td>Know-how</td><td>0.153</td><td>0.042</td></tr><tr><td rowspan="3">Financial</td><td>License</td><td>0.317</td><td>0.102</td></tr><tr><td>Consultancy</td><td>0.469</td><td>0.151</td></tr><tr><td>Maintenance</td><td>0.214</td><td>0.069</td></tr></table>

Table 12  
Decision matrix including the ratings of alternatives with respect to each criterion.

<table><tr><td rowspan="2">Alternative</td><td colspan="12">Criteria</td></tr><tr><td>Cr1</td><td>Cr2</td><td>Cr3</td><td>Cr4</td><td>Cr5</td><td>Cr6</td><td>Cr7</td><td>Cr8</td><td>Cr9</td><td>Cr10</td><td>Cr11</td><td>Cr12</td></tr><tr><td>A</td><td>7</td><td>8</td><td>9</td><td>9</td><td>6</td><td>8</td><td>8</td><td>7</td><td>8</td><td>7</td><td>6</td><td>5</td></tr><tr><td>B</td><td>4</td><td>6</td><td>5</td><td>6</td><td>6</td><td>5</td><td>6</td><td>7</td><td>8</td><td>8</td><td>7</td><td>6</td></tr><tr><td>C</td><td>6</td><td>4</td><td>3</td><td>5</td><td>6</td><td>3</td><td>5</td><td>7</td><td>8</td><td>9</td><td>9</td><td>7</td></tr><tr><td>D</td><td>9</td><td>8</td><td>7</td><td>8</td><td>6</td><td>9</td><td>8</td><td>7</td><td>8</td><td>6</td><td>5</td><td>4</td></tr><tr><td>Weight</td><td>0.149</td><td>0.042</td><td>0.094</td><td>0.053</td><td>0.067</td><td>0.056</td><td>0.075</td><td>0.100</td><td>0.042</td><td>0.102</td><td>0.151</td><td>0.069</td></tr></table>

Table 13  
Normalized decision matrix including the ratings of alternatives with respect to each criterion.

<table><tr><td rowspan="2">Alternative</td><td colspan="12">Criteria</td></tr><tr><td>Cr1</td><td>Cr2</td><td>Cr3</td><td>Cr4</td><td>Cr5</td><td>Cr6</td><td>Cr7</td><td>Cr8</td><td>Cr9</td><td>Cr10</td><td>Cr11</td><td>Cr12</td></tr><tr><td>A</td><td>0.519</td><td>0.596</td><td>0.703</td><td>0.627</td><td>0.500</td><td>0.598</td><td>0.582</td><td>0.500</td><td>0.500</td><td>0.462</td><td>0.434</td><td>0.445</td></tr><tr><td>B</td><td>0.297</td><td>0.447</td><td>0.390</td><td>0.418</td><td>0.500</td><td>0.374</td><td>0.436</td><td>0.500</td><td>0.500</td><td>0.528</td><td>0.507</td><td>0.535</td></tr><tr><td>C</td><td>0.445</td><td>0.298</td><td>0.234</td><td>0.348</td><td>0.500</td><td>0.224</td><td>0.364</td><td>0.500</td><td>0.500</td><td>0.593</td><td>0.651</td><td>0.624</td></tr><tr><td>D</td><td>0.667</td><td>0.596</td><td>0.547</td><td>0.557</td><td>0.500</td><td>0.673</td><td>0.582</td><td>0.500</td><td>0.500</td><td>0.396</td><td>0.362</td><td>0.356</td></tr><tr><td>Weight</td><td>0.149</td><td>0.042</td><td>0.094</td><td>0.053</td><td>0.067</td><td>0.056</td><td>0.075</td><td>0.100</td><td>0.042</td><td>0.102</td><td>0.151</td><td>0.069</td></tr></table>

Table 14  
Weighted normalized decision matrix.

<table><tr><td rowspan="2">Alternative</td><td colspan="12">Criteria</td></tr><tr><td>Cr1</td><td>Cr2</td><td>Cr3</td><td>Cr4</td><td>Cr5</td><td>Cr6</td><td>Cr7</td><td>Cr8</td><td>Cr9</td><td>Cr10</td><td>Cr11</td><td>Cr12</td></tr><tr><td>A</td><td>0.078</td><td>0.025</td><td>0.066</td><td>0.033</td><td>0.033</td><td>0.033</td><td>0.043</td><td>0.050</td><td>0.021</td><td>0.047</td><td>0.066</td><td>0.031</td></tr><tr><td>B</td><td>0.044</td><td>0.019</td><td>0.037</td><td>0.022</td><td>0.033</td><td>0.021</td><td>0.033</td><td>0.050</td><td>0.021</td><td>0.054</td><td>0.077</td><td>0.037</td></tr><tr><td>C</td><td>0.066</td><td>0.012</td><td>0.022</td><td>0.018</td><td>0.033</td><td>0.013</td><td>0.027</td><td>0.050</td><td>0.021</td><td>0.061</td><td>0.099</td><td>0.043</td></tr><tr><td>D</td><td>0.099</td><td>0.025</td><td>0.051</td><td>0.029</td><td>0.033</td><td>0.038</td><td>0.043</td><td>0.050</td><td>0.021</td><td>0.041</td><td>0.055</td><td>0.025</td></tr><tr><td>Weight</td><td>0.149</td><td>0.042</td><td>0.094</td><td>0.053</td><td>0.067</td><td>0.056</td><td>0.075</td><td>0.100</td><td>0.042</td><td>0.102</td><td>0.151</td><td>0.069</td></tr></table>

Table 15  
Positive ideal solution (A<sup>⁎</sup>) and negative ideal solution (A<sup>−</sup>) for each criterion.

<table><tr><td rowspan="2">Ideal solution</td><td colspan="12">Criteria</td></tr><tr><td>Cr1</td><td>Cr2</td><td>Cr3</td><td>Cr4</td><td>Cr5</td><td>Cr6</td><td>Cr7</td><td>Cr8</td><td>Cr9</td><td>Cr10</td><td>Cr11</td><td>Cr12</td></tr><tr><td> $A^*$ </td><td>0.099</td><td>0.025</td><td>0.066</td><td>0.033</td><td>0.033</td><td>0.038</td><td>0.043</td><td>0.050</td><td>0.021</td><td>0.061</td><td>0.099</td><td>0.043</td></tr><tr><td> $A^-$ </td><td>0.044</td><td>0.012</td><td>0.022</td><td>0.018</td><td>0.033</td><td>0.013</td><td>0.027</td><td>0.050</td><td>0.021</td><td>0.041</td><td>0.055</td><td>0.025</td></tr></table>

Table 16  
The distance of each alternative from positive and negative ideal solutions.

<table><tr><td>Alternative</td><td> $d^{*}$ </td><td> $d^{-}$ </td></tr><tr><td>A</td><td>0.044</td><td>0.066</td></tr><tr><td>B</td><td>0.071</td><td>0.034</td></tr><tr><td>C</td><td>0.066</td><td>0.056</td></tr><tr><td>D</td><td>0.054</td><td>0.071</td></tr></table>

Table 17  
The relative closeness (CC ) value for each alternative.

<table><tr><td>Alternative</td><td> $CC_i$ </td></tr><tr><td>A</td><td>0.600</td></tr><tr><td>B</td><td>0.326</td></tr><tr><td>C</td><td>0.461</td></tr><tr><td>D</td><td>0.570</td></tr></table>

## Acknowledgments

We appreciate the help and support that we have received from Turkish Airlines and its managerial team. We extend our deepest gratitude to Dr. Orkun Hasekioğlu, the head of the maintenance at Turkish Airlines, for his unwavering support and dedication to this project.

## References

[1] A. Ahi, M.B. Aryanezhad, B. Ashtiani, A. Makui, A novel approach to determine cell formation, intracellular machine layout and cell layout in the CMS problem based on TOPSIS method, Computers & Operations Research 36 (5) (2009) 1478–1496.

[2] D. Aloini, R. Dulmin, V. Mininno, Risk management in ERP project introduction: review of the literature, Information & Management 44 (2007) 547–567.

[3] M. Al-Mashari, Enterprise resource planning (ERP) systems: a research agenda, Industrial Management & Data Systems 102 (3) (2002) 165–170.

[4] B. Baki, K. Çakar, Determining the ERP package-selecting criteria: the case of Turkish manufacturing companies, Business Process Management Journal 11. (1) (2005) 75-86.

[5] M. Behzadian, S.K. Otaghsara, M. Yazdani, J. Ignatius, A state-of the-art survey of TOPSIS applications. Expert Systems with Applications 39 (17) (2012) 13051–13069.

[6] F.T. Bozbura, A. Beskese, C. Kahraman, Prioritization of human capital measurement indicators using fuzzy AHP, Expert Systems with Applications 32 (2007) 1100–1112.

[7] J.J. Buckley, Fuzzy hierarchical analysis, Fuzzy Sets Systems 17 (1) (1985) 233–247.

[8] D.-Y. Chang, Applications of the extent analysis method on fuzzy AHP, European Journal of Operational Research 95 (1996) 649–655.

[9] S.-W. Chou, Y.-C. Chang, The implementation factors that in<sup>fl</sup>uence the ERP (Enterprise Resource Planning) bene<sup>fi</sup>ts, Decision Support Systems 46 (2008) 149–157.

[10] A. Deep, P. Guttridge, S. Dani, N. Burns, Investigating factors affecting ERP selection in made-to-order SME sector, Journal of Manufacturing Technology Management 19 (4) (2008) 430–446.

[11] C. Doom, K. Milis, S. Poelmans, E. Bloemen, Critical success factors for ERP implementations in Belgian SMEs, Journal of Enterprise Information Management 23 (3) (2010) 378–406.

[12] İ. Ertuğrul, N. Karakaşoglu, Performance evaluation of Turkish cement <sup>fi</sup>rms with fuzzy analytic hierarchy process and TOPSIS methods, Expert Systems with Applications 36 (1) (2009) 702–715.

[13] S. Finney, M. Corbett, ERP implementation: a compilation and analysis of critica success factors, Business Process Management Journal 13 (3) (2007) 329–347.

[14] H. Forslund, P. Jonsson, Selection, implementation and use of ERP systems for supply chain performance management, Industrial Management & Data Systems 110 (8) (2010) 1159–1175.

[15] V.B. Genoulaz, P.-A. Millet, B. Grabot, A survey on the recent research literature on ERP systems Computers in Industry 56 (2005) 510–522

[16] T. Gürbüz, S.E. Alptekin, G.I. Alptekin, A hybrid MCDM methodology for ERP selection problem with interacting criteria, Decision Support Systems 54 (2012) 206–214.

[17] A. Hakim, H. Hakim, A practical model on controlling the ERP implementation risks, Information Systems 35 (2010) 204–214

[18] C.L. Hwang, K. Yoon, Multiple Attributes Decision Making Methods & Applications, Springer, New York, 1981.

[19] C. Kahraman, İ. Kaya, A fuzzy multicriteria methodology for selection among energy alternatives, Expert Systems with Applications 37 (9) (2010) 6270–6281.

[20] E.E. Karsak, C.O. Özogul, An integrated decision making approach for ERP system selection, Expert Systems with Applications 36 (2009) 660–667.

[21] H.S. Kilic, A fuzzy AHP based performance assessment system for the strategic plan of Turkish Municipalities, International Journal of Business and Management Studies 3 (2) (2011) 77–86.

[22] H.S. Kilic, E. Cevikcan, Job selection based on fuzzy AHP: an investigation including the students of Istanbul Technical University Management Faculty, International Journal of Business and Management Studies 3 (1) (2011) 173–182.

[23] H.S. Kilic, E. Cevikcan, A hybrid weighting methodology for performance assessment in Turkish municipalities, Communications in Computer and Information Science 300 (2012) 354–363.

[24] H.S. Kilic, An integrated approach for supplier selection in multi-item/multisupplier environment, Applied Mathematical Modelling 37 (14–15) (2013) 7752–7763.

[25] O. Kilincci, S.A. Onal, Fuzzy AHP approach for supplier selection in a washing machine company, Expert Systems with Applications 38 (2011) 9656–9664.

[26] X. Liao, Y. Li, B. Lu, A model for selecting an ERP system based on linguistic information processing, Information Systems 32 (2007) 1005–1017.

[27] M.-C. Lin, C.-C. Wang, M.-S. Chen, C.A. Chang, Using AHP and TOPSIS approaches in customer-driven product design process, Computers in Industry 59 (1) (2008) 17–31.

[28] D. Maditinos, D. Chatzoudes, C. Tsairidis, Factors affecting ERP system implementation effectiveness, Journal of Enterprise Information Management 25 (1) (2011) 60–78.

[29] S. Maguire, U. Ojiako, A. Said, ERP implementation in Omantel: a case study, Industrial Management & Data Systems 110 (1) (2010) 78–92.

[30] R. Malhotra, C. Temponi, Critical decisions for ERP integration: small business issues, International Journal of Information Management 30 (2010) 28–37.

[31] J. May, G. Dhillon, M. Caldeira, De<sup>fi</sup>ning value-based objectives for ERP systems planning, Decision Support Systems 55 (1) (2013) 98–109

[32] J. Motwani, R. Subramanian, P. Gopalakrishna, Critical factors for successful ERP implementation: exploratory <sup>fi</sup>ndings from four case studies, Computers in Industry 56 (2005) 529–544.

[33] D.L. Olson, Evaluation of ERP outsourcing, Computers & Operations Research 34 (2007) 3715–3724.

[34] T. Paksoy, N.Y. Pehlivan, C. Kahraman, Organizational strategy development in distribution channel management using fuzzy AHP and hierarchical fuzzy TOPSIS, Expert Systems with Applications 39 (3) (2012) 2822–2841.

[35] S. Perçin, Using the ANP approach in selecting and benchmarking ERP systems, Benchmarking: An International Journal 15 (5) (2008) 630–649.

[36] J. Razmi, M.S. Sangari, R. Ghodsi, Developing a practical framework for ERP readiness assessment using fuzzy analytic network process, Advances in Engineering Software 40 (2009) 1168–1178.

[37] Ö.Y. Saatçioğlu, What determines user satisfaction in ERP projects: bene<sup>fi</sup>ts, barriers or risks? Journal of Enterprise Information Management 22 (6) (2009) 690–708.

[38] T. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[39] B.R. Schlichter, P. Kraemmergaard, A comprehensive literature review of the ERP research <sup>fi</sup>eldover a decade, Journal of Enterprise Information Management 23 (4) (2010) 486–520.

[40] M.A. Sha<sup>fi</sup>a, M.M. Mazdeh, M. Vahedi, M. Pournader, Applying fuzzy balanced scorecard for evaluating the CRM performance, Industrial Management & Data Systems 111 (7) (2011).1105-1135.

[41] A.Y.T. Sun, A. Yazdani, I.D. Overend, Achievement assessment for enterprise resource planning (ERP) system implementations based on critical success factors (CSFs). International Iournal of Production Economics 98 (2005) 189–203.

[42] C.G. Şen, H. Baraçlı, S. Şen, H. Başlıgil, An integrated decision support system dealing with qualitative and quantitative objectives for enterprise software selection, Expert Systems with Applications 36 (2009) 5272–5283.

[43] C.G. Şen, H. Baraçlı, Fuzzy quality function deployment based methodology for acquiring enterprise software selection requirements, Expert Systems with Applications 37 (2010) 3415–3426.

[44] P.S. Tan, S.S.G. Lee. A.E.S. Goh. Multi-criteria decision techniques for context-aware B2B collaboration in supply chains, Decision Support Systems 52 (4) (2012) 779–789.

[45] E.J. Umble, R.R. Haft, M.M. Umble, Enterprise resource planning: implementation procedures and critical success factors, European Journal of Operational Research 146 (2003) 241–257.

[46] C. Ünal, M.G. Güner, Selection of ERP suppliers using AHP tools in the clothing industry, International Journal of Clothing Science and Technology 21 (4) (2009) 239–251.

[47] P.J.M. van Laarhoven, W. Pedrycz, A fuzzy extension of Saaty's priority theory, Fuzzy Sets and Systems 11 (1983) 229–241.

[48] O. Velcu, Exploring the effects of ERP systems on organizational performance: evidence from Finnish companies, Industrial Management & Data Systems 107 (9) (2007) 1316–1334.

[49] J. Verville, C. Bernadas, A. Halingten, So you're thinking of buying an ERP? Ten critical factors for successful acquisitions, Journal of Enterprise Information Management 18 (6) (2005) 665–677

[50] C.-C. Wei, M.-J.J. Wang, A comprehensive framework for selecting an ERP system, International Journal of Proiect Management 22 (2004) 161–169

[51] C.-C. Wei, C.-F. Chien, M.-J.J. Wang, An AHP-based approach to ERP system selection, International Journal of Production Economics 96 (2005) 47-62

[52] V. Wickramasinghe, M. Karunasekara, Impact of ERP systems on work and work-life, Industrial Management & Data Systems 112 (6) (2012) 982–1004

[53] J.-H. Wu, S.-S. Shin, M.S.H. Heng, A methodology for ERP mis<sup>fi</sup>t analysis, Information & Management 44 (2007) 666–680

[54] J.-B. Yang, C.-T. Wu, C.-H. Tsai, Selection of an ERP system for a construction <sup>fi</sup>rm in Taiwan: a case study, Automation in Construction 16 (2007) 787–796.

[55] H.R. Yazgan, S. Boran, K. Goztepe, An ERP software selection process with using arti<sup>fi</sup>cial neural network based on analytic network process approach, Expert Systems with Applications 36 (2009) 9214–9222.

[56] M. Ziaee, M. Fathian, S.J. Sadjadi, A modular approach to ERP system selection: a case study, Information Management & Computer Security 14 (5) (2006) 485–495.

[57] L.A. Zadeh, Fuzzy sets, Information and Control 8 (3) (1965) 338–353.

![](/api/attachments/A3XMHUSP/fulltext/images/95232846a0752ab6dabc3becde367732fa96a5a2916e53e405709389f9c0177c.jpg)

Dr. Huseyin Selcuk Kilic is currently an instructor in the Department of Industrial Engineering in Marmara University. He received the BSc, MSc and PhD degrees in Industrial Engineering from Istanbul Technical University. He studied in-plant logistics design for his PhD dissertation. His main research areas are plant logistics, reverse logistics, lean production, decision making and ergonomics. He has research papers in journals that include Applied Mathematical Modelling, International Journal of Advanced Manufacturing Technology, and Assembly Automation.

![](/api/attachments/A3XMHUSP/fulltext/images/bf7ce43b7b3a41f7706b81f6403cb26dd27d5d4941ca4f71e7c17ae56342e70d.jpg)

Dr. Selim Zaim has received his B.S. degree in Mechanical Engineering from Istanbul Technical University and his Ph. D. degree in Production and Operations Management from Istanbul University. Selim Zaim has been serving as a professor in the Faculty of Management at Istanbul Technical University. Zaim has published over 100 articles and papers in various journals and congress proceedings. His current scholarly interests focus on multivariate data analysis, supply chain management, data mining and multi-criteria decision making. Zaim reviews papers for a variety of journals. He is a member of Industrial Management and Development Associations and Quality Association in Turkey (KALDER).

![](/api/attachments/A3XMHUSP/fulltext/images/c6fa1465b9c77d6d08c6685bbb09bcbd25a7b23e162c3725db09cda98985846a.jpg)

Dr. Dursun Delen is the William S. Spears Endowed Chair in Business Administration, Neal Patterson Chair in Business Analytics, Research Director for the Center for Health Systems Innovation, and Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University (OSU). He received his Ph.D. in Industrial Engineering and Management from OSU in 1997. Prior to his appointment as an Assistant Professor at OSU in 2001, he worked for a privately-owned research and consultancy company, Knowledge Based Systems Inc., in College Station, Texas, as a research scientist for <sup>fi</sup>ve years, during which he led a number of decision support and other information systems related research projects funded by federal agencies, including DoD, NASA, NIST and DOE. His

research has appeared in major journals including Decision Support Systems, Decision Sciences, Communications of the ACM, Computers and Operations Research, Computers in Industry, Journal of Production Operations Management, Arti<sup>fi</sup>cial Intelligence in Medicine, Expert Systems with Applications, among others. He recently published four books: Advanced Data Mining Techniques with Springer, 2008; Decision Support and Business Intelligence Systems with Prentice Hall, 2010; Business Intelligence: A Managerial Approach, with Prentice Hall, 2010; and Practical Text Mining and Statistical Analysis for Non-structured Text Data Applications, with Elsevier, 2012. He is often invited to national and international conferences for keynote addresses on topics related to Data/ Text Mining, Business Intelligence, Decision Support Systems, and Knowledge Management. He served as the general co-chair for the 4th International Conference on Network Computing and Advanced Information Management (September 2–4, 2008 in Soul, South Korea), and regularly chairs tracks and mini-tracks at various information systems conferences. He is the associate editor-in-chief for International Journal of Experimental Algorithms, associate editor for International Journal of RF Technologies, and is on editorial boards of <sup>fi</sup>ve other technical journals. His research and teaching interests are in data and text mining, decision support systems, knowledge management, business intelligence and enterprise modeling.
