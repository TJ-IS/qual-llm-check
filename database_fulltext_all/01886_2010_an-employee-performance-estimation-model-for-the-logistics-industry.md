---
otero_id: 1886
otero_key: "63VMYGJR"
title: "An employee performance estimation model for the logistics industry"
authors: "Yu-Jen Wu; Jiang-Liang Hou"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.11.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An employee performance estimation model for the logistics industry

Yu-Jen Wu <sup>1</sup>, Jiang-Liang Hou ⁎

Department of Industrial Engineering and Engineering Management National Tsing Hua University Hsinchu (300), Taiwan

a r t i c l e i n f o

Article history: Received 20 March 2009 Received in revised form 18 October 2009 Accepted 6 November 2009 Available online 18 November 2009

Keywords: Performance evaluation Logistics management Logistic information system Human resources management (HRM)

## a b s t r a c t

In the last decade, the growing economy in Taiwan has brought about rapid growth in the logistics demands of enterprises. An important goal in the <sup>fi</sup>eld of third party logistics (3PLs) is to improve the performance of logistics activities to enhance operation ef<sup>fi</sup>ciency and enterprise competency. However, the employee performance must be determined in order to improve the activity performance of 3PLs. Thus, the aim of this research is to develop an employee performance estimation (EPE) model that includes three modules: direct performance determination (DPD), indirect performance determination (IPD), and performance score analysis (PSA). Moreover, a web-based logistics information management (LIM) platform was established via the EPE model in order to assist the managers in collecting and maintaining shop-<sup>fl</sup>oor operation data and to identify low-performance logistics tasks as well as inexperienced employees. In addition, a real-world case was used to demonstrate applicability of the proposed model and platform. As a whole, this paper presents an integrated model with the aims to more accurately calculate employee performance and signi<sup>fi</sup>cantly reduce the workload of 3PL decision makers

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

As the economy continues to grow in Taiwan, enterprises require more cooperation with professional logistics service providers in order to accomplish logistics activities since the complexity of logistics activities (e.g., distribution or warehousing) has gradually increased. This has resulted in a drastic increase in the number of third party logistics (3PLs) established for the purpose of ful<sup>fi</sup>lling the logistics demands of enterprises. In order to enhance operation competency and ef<sup>fi</sup>ciency, some 3PLs have utilized a variety of automated techniques and management strategies to improve the performance of logistical tasks.

Although conventional 3PLs invest a large amount of money and time in their logistic operations, operation competency and ef<sup>fi</sup>ciency has not shown signi<sup>fi</sup>cant improvement because managers cannot systematically recognize either low-performance logistics tasks or inexperienced employees. Logistics managers do not take a systematic approach for determining the performance of operators. In addition, logistics-related data (e.g., operation time) from the shop <sup>fl</sup>oor cannot be accurately gathered and imported into a logistics database and thus, they cannot be employed for operator performance evaluation. Under such circumstances, 3PL managers have dif<sup>fi</sup>culties reusing and analyzing logistics-related data.

To overcome these problems, this research proposes a model aimed at determining the performance of different types of employees by utilizing the shop <sup>fl</sup>oor data of logistics activities. With regard to employee performance calculation, this research uses quantitative factors to estimate the operational performance of direct workers and indirect managers. Two performance reasoning modules are developed in this study:

• Direct Performance Determination: Used to determine the Real Performance (RP), Effective Performance (EP) and Derived Performance (DP) of direct workers.

• Indirect Performance Determination: Used to determine the Veri<sup>fi</sup>cation Performance (VP), Assessment Performance (AP) and Inference Performance (IP) of indirect managers.

The two modules can be combined to generate an integrated employee performance estimation model. In the proposed performance estimation model, the RP may <sup>fi</sup>rst be calculated via the duration and quantitative outputs of logistical tasks. Subsequently, several quality indices (e.g., the operator trend index and operator idle index) can be formulated to determine the EP and DP. The teamlevel trend index, team-level quality index, schedule index and budget index can be formulated to estimate the VP, AP and IP. The operator and manager performance indices (i.e., RP, EP, DP, VP, AP and IP) can be given to logistics managers in order to identify both lowperformance logistics tasks and inexperienced employees. In summary, the proposed performance estimation approach can be used in the logistics management systems of 3PLs to produce an automatic determination of employee performance in a logistics center.

By estimating the performances of all levels of employee, lowperformance logistics tasks as well as inexperienced employees can be determined so that the demands of 3PLs for improvement in operational competency and ef<sup>fi</sup>ciency can be ful<sup>fi</sup>lled.

## 2. Literature review

In the <sup>fi</sup>eld of employee performance evaluation research, related studies focus on evaluation schema construction and measurement item calculation. The previous groundwork is discussed below.

## 2.1. Evaluation schema construction

In a performance pyramid model [13], decision makers should determine performance evaluation factors based on organization levels. It is not only education levels and work experience that affect employee performance, but also job characteristics and workplace conditions [9]. In the past, many studies utilized literature reviews, expert interviews or questionnaire surveys to identify the appropriate performance evaluation factors of distinct industries. Sims et al. [15] employed interview and survey methodologies to determine how employees in the medical and manufacturing industries address task variety, task autonomy, task identity, information feedback, dealing with others, and friendship opportunity. In order to provide a comprehensive structure for performance evaluation, Coleman and Borman [4] <sup>fi</sup>rst generated twenty-seven citizenship performance behaviors, based on previous research, and developed a performance evaluation structure composed of the interpersonal, organizational job/task dimensions via questionnaire. In addition, the TQM key components (e.g., problem-solving abilities of employees) were regarded as important factors for employee evaluation since enterprise managers could understand the performance of implementing TQM by evaluating employee performance via TQM factors [5].

For room attendants and reception clerks in the hotel industry [3,12], nurse anesthetists in the hospital industry [17], and technicians in the paper industry [18], expert interview methodology was used to generate factors for candidate evaluation. The importance of the candidate evaluation factors for managers is analyzed via questionnaire. Performance evaluation schemas (i.e., factors and their corresponding levels) and factor weights may be obtained by the analytic hierarchy process (AHP) method. In order to ensure the applicability of candidate performance evaluation factors, Chen [2] and Laio [11] used the Delphi and AHP methods to establish evaluation schemas for advertising executives in the newspaper industry and technicians in the free-air television industry. A fuzzy multiple criteria algorithm may also be used to analyze the consistency of performance evaluation factors. The MIJE (Metal Industry Job Evaluation) system applied to evaluate employee performance in the metal industry should improve its evaluation factor weights since the development of IT technologies and working conditions have caused managers in the metal industry to stress new factors. Hence, a revised MIJE system is proposed, using the expert interview as well as AHP approaches for an optimal evaluation schema in line with the characteristics of the metal industry [8].

## 2.2. Measurement item calculation

For the scoring of employees using evaluation factors, the PDA (Performance Distribution Assessment) model proposed by Kane and Kane [10] requests supervisors to <sup>fi</sup>rst distribute a subjective score. The performance distributions for all employees can be established according to the frequencies occurring on different levels of the evaluation factors, while employee performance can be determined in terms of speci<sup>fi</sup>c statistics (e.g., the median or mode). Although the work behavior of R&D engineers in the software industry cannot be easily measured, measurements of the key competencies for all R&D engineers could be acquired by their managers via Q&A. Using the differences in the measurements and the optimal values of key competencies, R&D engineers may be classi<sup>fi</sup>ed into several groups through the use of normal distribution. Furthermore, the performance of R&D engineers can be rated on a basis of group rank [14].

In order to solve the problem of evaluating employee characteristics, Ahn and Chang [1] regarded the know-how and the human capabilities of employees as product- and process-related tacit knowledge. In this study, tacit knowledge is transformed into organizational and <sup>fi</sup>nancial performance by means of the DEA (data envelopment analysis) approach to investigate employee performance. It is not only regular work, but also job transfers and in<sup>fl</sup>uence activities that affect employee performance. Eguchi [6] used the time series concept to estimate the <sup>fi</sup>nancial pro<sup>fi</sup>ts that employees generate from regular work. He applied the opportunity cost concept to calculate the loss due to job transfers and in<sup>fl</sup>uence activities. He then applied the averages of the fuzzy linguistic variables to estimate expected employee performance using the probabilistic/possibilistic approach. In order to provide lists to managers for the assignation of employees to jobs, employee performance must <sup>fi</sup>rst be calculated according to the estimated results. In order to generate candidate employees, ranks of employees in distinct jobs may be determined on the basis of their job attributes and employee performance [16].

Regarding the bene<sup>fi</sup>ts generated by employee cooperation on a job, employee combinations should be emphasized as employee performance is calculated for assigning employees to jobs [19]. First, the employee rank of distinct jobs can be determined using the standard fuzzy arithmetic and then feasible employee combinations can be generated via the triangular fuzzy number. The optimal employee assignment plan for designated jobs can be determined according to the job characteristics and may be provided to relevant supervisors for operational planning. The model proposed by Golec and Kahya [7] quanti<sup>fi</sup>es the performance evaluation factors using the heuristic method and calculates the scores of employees using the factors dictated by the fuzzy rules. The employee assignment program can be determined by ranking employee scores.

As shown in the above literature review, previous studies for evaluating direct employee performance stressed the analysis of the performance evaluation factors and calculations of the factor weights. However. it is critical to transform the measurement items of direct employees in the evaluation factors into direct employee performance. The derived performance can be used to measure the behavior of the direct employee and the employee assignment plan. Few studies have been dedicated to the evaluation factors and the factor weights for indirect employees (e.g., managers). In contrast to previous studies, this paper focuses on employee performance evaluation within the logistics industry. Performance evaluation factors were established according to the characteristics and organizational structure of a distribution center (DC). By utilizing the shop <sup>fl</sup>oor operation data, a systematic and quantitative algorithm was also developed to automatically calculate the performance of the direct workers and indirect managers of a logistics center.

## 3. Employee performance estimation model

In order to assist 3PL managers in estimating employee performance, this research develops an employee performance estimation (EPE) model to determine the performance of direct workers and indirect managers. To enable a determination of personal performance for each employee in a DC, staff levels and organization units must be de<sup>fi</sup>ned to serve as input. After de<sup>fi</sup>ning the DC organization, this study utilized the operation data of logistics activities, the records from exception reports, work schedules, and budget plans to derive the performance of each employee (including direct workers and indirect managers). The proposed EPE model can be categorized into three modules (Fig. 1).

![](/api/attachments/63VMYGJR/fulltext/images/a5dd07b01bf3f5dcb29130e92ff297e1755126b6d43392decca8e0a350931814.jpg)  
Fig. 1. Process for employee performance determination.

## • Module I — Direct Performance Determination (DPD)

Based on the operation volume and work time of direct workers, the RP may be calculated. To address the error frequency of the logistics operations, EP and DP can be derived from the idle time of logistics activities and the growth trend of employee performance for each direct worker. This module focuses mainly on the performance estimation of the direct worker.

## • Module II — Indirect Performance Determination (IPD)

The DP of direct workers, error frequency, growth trend of employee performance and the progress management of a team are considered for estimating the VP. The AP can be determined by combining the VP and checking the budget consumption of the corresponding of<sup>fi</sup>ce. Then, the IP can be integrated with the derived AP. In short, this module can be utilized to estimate the performance of indirect managers.

## • Module III — Performance Score Analysis (PSA)

In the PSA module, the performance improvement scale of logistics tasks is denoted as an improvement rate. After deriving the improvement rate, the DP, VP, AP and IP can be transformed into performance scores (PSs).

The operations of the above three modules can be further divided into seven stages: RP calculation, EP computation, DP determination,

VP estimation, AP estimation, IP estimation and PS analysis. The details of a DC organization and the three performance estimation modules are described below.

## 3.1. Organizational structure of a DC

The organizational structure of a typical DC must <sup>fi</sup>rst be de<sup>fi</sup>ned before applying the employee performance estimation approach. The de<sup>fi</sup>ned organizational architecture can be regarded as the inputs for the EPE model.

In this section, the relationship $W R _ { i , j , k }$ between employees and operational divisions can be identi<sup>fi</sup>ed. $W R _ { i , j , k }$ can be used to denote a direct worker (where i=1 or 2) or an indirect manager (where $i = 2 ,$ 3 or 4). That is, in a DC, the direct worker set S(SE)(i.e., $\{ W R _ { i , j , k } |$ i=1,2}) comprises the <sup>fi</sup>rst-line operators and team-level managers while the indirect manager set S(ML) (i.e., $\{ W R _ { i , j , k } | i = 2 , 3 , 4 \} )$ includes: team-level managers, of<sup>fi</sup>ce-level managers and division-level managers. The organizational structure of a typical DC is illustrated in Fig. 2.

## 3.2. DPD module

The procedures to determine the performance of <sup>fi</sup>rst-line operators and team-level managers consists of three stages (i.e., RP

Table 2  
![](/api/attachments/63VMYGJR/fulltext/images/4e99575a3071aa88b8f17270a32eeb5700efb9835add19aedfe72b84703335b0.jpg)  
Fig. 2. The organizational structure of a typical DC.

Calculation, EP Calculation and DP Calculation) and are discussed as follows.

## 3.2.1. RP calculation for direct workers

At this stage, the logistics data must <sup>fi</sup>rst be acquired and may be used to calculate the RP of direct workers (including the <sup>fi</sup>rst-line operators and team-level managers). The procedure for calculating the RP of direct workers in logistics tasks is discussed below.

3.2.1.1. Step (A1): Determine the time interval for RP calculation. A time interval on the basis of the logistics operation days should be assigned before calculating the real performance of direct employees. The time interval T can be derived based on the prede<sup>fi</sup>ned starting day (t ) and ending day $\left( t _ { 2 } \right)$ for employee performance calculation.

3.2.1.2. Step (A2): Acquire logistics-related data for RP calculation. After determining the time interval T for employee performance calculation, the basic prede<sup>fi</sup>ned data regarding the direct workers $W R _ { i , j , k }$ $( i = 1 , 2 )$ and the logistics tasks LO $( l { = } 1 , . . . , p )$ should be acquired from the logistics information management (LIM) system. In addition to the basic prede<sup>fi</sup>ned data, the logistics operation data regarding the work date $C T _ { t } ,$ the operation volume $N ( W R _ { i j , k } , \ C T _ { t } , \ L O _ { l } )$ and the corresponding work time $T ( W R _ { i , j , k } , C T _ { t } , L O _ { l } )$ at interval T can also be acquired from the LIM system. In general, the logistics-related data that should be acquired prior to the employee performance calculation is summarized in Table 1.

3.2.1.3. Step (A3): Calculate RP of logistics tasks for direct employees. For a direct employee $W R _ { i , j , k } ,$ the real performance $R C ( W R _ { i , j , k } , T , L O _ { l } )$ for each logistics task LO at T indicates the average operation volume for the direct employee within a unit time. Based on the above concept, $R C ( W R _ { i , j , k } , T , L O _ { l } )$ can be obtained via one of the following equations and is summarized in Table 2.

Summary of the logistics-related data required for employee performance calculation.

<table><tr><td></td><td> $LO_1$ </td><td>...</td><td> $LO_l$ </td><td>...</td><td> $LO_p$ </td></tr><tr><td rowspan="2"> $CT_1$ </td><td> $N(WR_{i,j,k}, LO_1, CT_1)$ </td><td rowspan="2">...</td><td> $N(WR_{i,j,k}, LO_l, CT_1)$ </td><td rowspan="2">...</td><td> $N(WR_{i,j,k}, LO_p, CT_1)$ </td></tr><tr><td> $T(WR_{i,j,k}, LO_1, CT_1)$ </td><td> $T(WR_{i,j,k}, LO_l, CT_1)$ </td><td> $T(WR_{i,j,k}, LO_p, CT_1)$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td rowspan="2"> $CT_m$ </td><td> $N(WR_{i,j,k}, LO_1, CT_m)$ </td><td rowspan="2">...</td><td> $N(WR_{i,j,k}, LO_l, CT_m)$ </td><td rowspan="2">...</td><td> $N(WR_{i,j,k}, LO_p, CT_m)$ </td></tr><tr><td> $T(WR_{i,j,k}, LO_1, CT_m)$ </td><td> $T(WR_{i,j,k}, LO_l, CT_m)$ </td><td> $N(WR_{i,j,k}, LO_p, CT_m)$ </td></tr></table>

• On the basis of interval T:

$$
R C (W R _ {i, j, k}, T, L O _ {l}) = \sum_ {t = 1} ^ {m} N (W R _ {i, j, k}, C T _ {t}, L O _ {l}) / \sum_ {t = 1} ^ {m} T (W R _ {i, j, k}, C T _ {t}, L O _ {l}).\tag{1}
$$

• On the basis of the work date CT<sub>t</sub>:

$$
R C (W R _ {i, j, k}, T, L O _ {l}) = \sum_ {t = 1} ^ {m} \frac {N (W R _ {i , j , k} , C T _ {t} , L O _ {l})}{T (W R _ {i , j , k} , C T _ {t} , L O _ {l})} \Bigg / m.\tag{2}
$$

3.2.2. EP calculation for direct workers

Owing to the existence of defective items, the operation volume of logistics tasks is not exactly that of the quali<sup>fi</sup>ed volume of the logistics tasks. Thus, the volume of defective items must be deducted from the operation volume of the logistics tasks to generate a quality index prior to determining the EPs of direct workers. The procedure for calculating the EPs of direct workers is as follows.

3.2.2.1. Step (B1): Acquire operation error data of logistics activities. The operation error data of the logistics activities at T can be acquired from the LIM system in order to calculate the operation error rates of logistics activities. The operation error data of the logistics activities indicate the volume $\therefore n ( W R _ { i , j , k } , C T _ { t } , L O _ { l } )$ of errors induced by the direct workers $W R _ { i , j , k }$ while performing the logistic task LO<sub>l</sub> in $C T _ { t } .$

3.2.2.2. Step (B2): Derive operation error rates of logistics activities. For a direct worker, the quality index is de<sup>fi</sup>ned as the operation error rates $\mathcal { P } r ( W R _ { i , j , k } , T , L O _ { l } )$ of the logistics activities and can be determined using the ratio of the sum of en ${ \mathrm { W } R _ { i , j , k } } , C T _ { t } , L O _ { l } )$ to the sum of $N ( W R _ { i , j , k } ,$ $L O _ { l } , C T _ { t } )$ ) at T. That is, the quality index ${ \mathrm { \Sigma } } ^ { \prime } ( W R _ { i , j , k } , T , L O _ { l } )$ can be obtained by means of the following equation:

$$
e r (W R _ {i, j, k}, T, L O _ {l}) = \sum_ {t = 1} ^ {m} e n (W R _ {i, j, k}, C T _ {t}, L O _ {l}) \Bigg / \sum_ {t = 1} ^ {m} N (W R _ {i, j, k}, C T _ {t}, L O _ {l})\tag{3}
$$

Summary of RP for distinct direct employees and the logistics tasks.

<table><tr><td></td><td> $LO_{1}$ </td><td>...</td><td> $LO_{l}$ </td><td>...</td><td> $LO_{p}$ </td></tr><tr><td> $WR_{1,1,1}$ </td><td> $RC(WR_{1,1,1}, T, LO_{1})$ </td><td>...</td><td> $RC(WR_{1,1,1}, T, LO_{l})$ </td><td>...</td><td> $RC(WR_{1,1,1}, T, LO_{p})$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $WR_{2,M,n_{2,M}}$ </td><td> $RC(WR_{2,M,N_{2,M}}, T,LO_{1})$ </td><td>...</td><td> $RC(WR_{2,M,N_{2,M}}, T,LO_{l})$ </td><td>...</td><td> $RC(WR_{2,M,N_{2,M}}, T,LO_{p})$ </td></tr></table>

3.2.2.3. Step (B3): Calculate EP of logistics activities for direct workers. The EP of a direct worker in a logistics activity indicates the throughput of the logistics activity for the direct worker. Therefore, the EP of a direct worker for a speci<sup>fi</sup>c logistics task can be obtained by considering the in<sup>fl</sup>uence of the quality index on the corresponding RP. This idea is represented by the following equation:

$$
E C (W R _ {i, j, k}, T, L O _ {l}) = R C (W R _ {i, j, k}, T, L O _ {l}) \times [ 1 - e r (W R _ {i, j, k}, T, L O _ {l}) ].\tag{4}
$$

## 3.2.3. DP calculation for direct workers

Based on the EP of direct workers derived at the previous stage, the DP of direct workers can be determined by considering the trend indices and working time indices of the logistics activities. The procedure for deriving the DPs of direct workers is discussed in the following.

3.2.3.1. Step (C1): Calculate trend indices of logistics activities. For a direct worker, the trend index of a speci<sup>fi</sup>c logistic task can be used to indicate whether its corresponding EP signi<sup>fi</sup>cantly increases with time. The procedure for calculating the trend index is discussed in the following.

3.2.3.1.1. Step (C1-1): Acquire historical operation data for trend index calculation. Following Step (A2), the historical operation data in the working days $H C T _ { s } ,$ the historical operation volume $N ( W R _ { i , j , k } ,$ $H C T _ { s } , L O _ { l } )$ and the corresponding historical working time $T ( W R _ { i , j , k } ,$ $H C T _ { s } , L O _ { l } )$ at time interval $H T \left( \operatorname { f r o m } t _ { 1 } \tan t _ { 2 } \right)$ can also be acquired from the LIM system and used to structure the groundwork for comparing the difference in EP between time intervals T and HT.

3.2.3.1.2. Step (C1-2): Calculate historical EP of logistics activities for direct workers. In order to determine the variation of EP for a direct worker $W R _ { i , j , k }$ at T using the historical EP at HT, the average $H E C ( W R _ { i , j , k } ,$ $H T , L O _ { l } )$ and variance $H E C V ( W R _ { i , j , k } , H T , L O _ { l } )$ of the historical EP must be derived using the following equations:

$$
H E C (W R _ {i, j, k}, H T, L O _ {l}) = \sum_ {s = 1} ^ {n} H E C (W R _ {i, j, k}, H C T _ {s}, L O _ {l}) / n\tag{5}
$$

$$
H E C V (W R _ {i, j, k}, H T, L O _ {l}) = \frac {\sum_ {s = 1} ^ {n} \left[ H E C (W R _ {i , j , k} , H C T _ {s} , L O _ {l}) - H E C (W R _ {i , j , k} , H T , L O _ {l}) \right] ^ {2}}{n - 1}.\tag{6}
$$

3.2.3.1.3. Step (C1-3): Establish confidence interval of historical EPs for direct workers. After deriving $H E C ( W R _ { i , j , k } , H T , L O _ { l } )$ and $H E C V ( W R _ { i , j , k } ,$ $H T , ~ L O _ { l } )$ from the logistics activities of direct workers at HT, the con<sup>fi</sup>dence intervals of historical EPs for a direct worker $W R _ { i , j , k }$ can be established using the following equations with a signi<sup>fi</sup>cant level α:

$$
C _ {1} \left(W R _ {i, j, k}, H T, L O _ {l}\right) = H E C \left(W R _ {i, j, k}, H T, L O _ {l}\right) + Z _ {\frac {\alpha}{2}} \sqrt {\frac {H E C V \left(W R _ {i , j , k} , H T , L O _ {l}\right)}{n}}\tag{7}
$$

$$
C _ {2} \left(W R _ {i, j, k}, H T, L O _ {l}\right) = H E C \left(W R _ {i, j, k}, H T, L O _ {l}\right) - Z _ {\frac {\alpha}{2}} \sqrt {\frac {H E C V \left(W R _ {i , j , k} , H T , L O _ {l}\right)}{n}}\tag{8}
$$

where $C _ { 1 } ( W R _ { i , j , k } , H T , L O _ { l } )$ and $C _ { 2 } ( W R _ { i , j , k } , H T , L O _ { l } )$ represents the upper and lower limits of the con<sup>fi</sup>dence intervals for the historical EPs, respectively.

3.2.3.1.4. Step (C1-4): Determine values of trend indices for logistics activities. For a direct worker, the trend indices of the logistics activities indicate the status (e.g., increase, slack or decrease) of EPs after comparison with the historical EP. The values of the trend indices $T r I ( W R _ { i , j , k } , T , L O _ { l } )$ at T can be assigned as $^ { * } 1 ^ { * } , { } ^ { * } 0 ^ { * } 0 \Gamma ^ { * } - 1 ^ { * }$ according to the following rule. The value of $T r I ( W R _ { i , j , k } , T , L O _ { l } )$ ) is equal $\tan ^ { \mathfrak { u } _ { 1 } { \mathfrak { v } } }$ if EPs of the logistics activities at T are higher than the upper limits of con<sup>fi</sup>dence intervals of the historical EPs at HT. That is, the EP of the logistics activity at T obviously increases as compared with the historical EP.

$$
T r l (W R _ {i, j, k}, T, L O _ {l}) = \left\{ \begin{array}{l l} 1 & \text { if } E C (W R _ {i, j, k}, T, L O _ {l}) \geq C _ {1} (W R _ {i, j, k}, T, L O _ {l}) \\ 0 & \text { if } C _ {1} (W R _ {i, j, k}, T, L O _ {l}) > E C (W R _ {i, j, k}, T, L O _ {l}) > C _ {2} (W R _ {i, j, k}, T, L O _ {l}) \\ - 1 & \text { if } E C (W R _ {i, j, k}, T, L O _ {l}) \leq C _ {2} (W R _ {i, j, k}, T, L O _ {l}) \end{array} \right..\tag{9}
$$

3.2.3.2. Step (C2): Calculate working time index of logistics activities for direct workers. The working time index of a direct worker in a speci<sup>fi</sup>c logistics task can be used to indicate the busyness of the worker required to perform the corresponding logistics task. The procedure for calculating the working time index is discussed below.

3.2.3.2.1. Step (C2-1): Determine categories of working date within the predefined time interval. In order to accurately evaluate the busyness of the direct worker in performing the logistics tasks using the idle time of the corresponding workers at time interval T, the categories of the working date at T should <sup>fi</sup>rst be determined in order to identify on-job and off-job days. That is, the working date CT of the direct workers at T can be determined by distinguishing whether CT<sub>t</sub> belongs to the set of working days $N W D S e t ( W R _ { i , j , k } , \ T )$ . The set $N W D S e t ( W R _ { i , j , k } , T )$ is usually de<sup>fi</sup>ned by DC managers. Therefore, the number of elements in $N W D S e t ( W R _ { i , j , k } , T )$ is equal to the number of working days suggested by the DC managers for the direct workers at T.

3.2.3.2.2. Step (C2-2): Calculate total working time of the direct workers within the predefined time interval. After acquiring $N W D S e t ( W R _ { i , j , k } , T )$ , the total working time $T N W T ( W R _ { i , j , k } , T )$ , which the DC managers suggest for the direct workers to perform the logistics tasks at $T ,$ can be obtained using the following equation, in order to calculate the idle time of direct workers while performing the logistics tasks.

$$
T N W T (W R _ {i, j, k}, T) = D N W T \times N N W D (W R _ {i, j, k}, T)\tag{10}
$$

where DNWT is the daily working time of the direct workers proposed by the DC managers.

3.2.3.2.3. Step (C2-3): Calculate total idle time of the direct workers within the predefined time interval. To utilize the working time index to evaluate the busyness of direct workers, the idle conditions of the direct workers at T should be considered. Using $T N W T ( W R _ { i , j , k } , T )$ added to the sum of the operation time in which the direct workers perform the logistics tasks on the working days at T, the total idle time ${ T I D T } ( W R _ { i , j , k } , T )$ of a direct worker can be determined via the following equation.

$$
\begin{array}{l} T I D T (W R _ {i, j, k}, T) = T N W T (W R _ {i, j, k}, T) \\ \qquad - \sum_ {l = 1} ^ {p} \sum_ {t = 1} ^ {n} \Big \{T (W R _ {i, j, k}, C T _ {t}, L O _ {l}) | C T _ {t} \in N W D S e t (W R _ {i, j, k}, T) \Big \}. \end{array}\tag{11}
$$

3.2.3.2.4. Step (C2-4): Calculate idle time of each logistics activity for direct workers. The idle time $I D T ( W R _ { i , j , k } , T , L O _ { l } )$ of a direct worker in a speci<sup>fi</sup>c logistics task at T can be determined by distributing the total idle time in relation to the proportion of the corresponding logistics task. The proportion compares the ratio of the time in which the direct worker performs this logistics task to the time of the same direct worker perform all logistics tasks on the working days at T. Based on the above idea, the idle time $I D T ( W R _ { i , j , k } , T , L O _ { l } )$ of logistics tasks for a direct worker can be obtained via the following equation.

$$
\begin{array}{l} I D T (W R _ {i, j, k}, T, L O _ {l}) = T I D T (W R _ {i, j, k}, T) \\ \qquad \times \frac {\sum_ {t = 1} ^ {m} \left\{T (W R _ {i , j , k} , C T _ {t} , L O _ {l}) | C T _ {t} \in N W D S e t (W R _ {i , j , k} , T) \right\}}{\sum_ {l = 1} ^ {p} \sum_ {t = 1} ^ {m} \left\{T (W R _ {i , j , k} , C T _ {t} , L O _ {l}) | C T _ {t} \in N W D S e t (W R _ {i , j , k} , T) \right\}}. \end{array}\tag{12}
$$

3.2.3.2.5. Step (C2-5): Determine values of working time indices for logistics activities. The working time index of a speci<sup>fi</sup>c logistics task indicates the busyness of a direct worker in the corresponding logistics task. The quantitative values of the working time indices for the logistics tasks are the proportions of “the difference between the total working time and the idle time” to “the total working time”. Therefore, the values of the working time indices for direct workers can be formulated using the following the equation.

$$
\begin{array}{l} W t I (W R _ {i, j, k}, T, L O _ {l}) \\ = 1 - \frac {I D T (W R _ {i , j , k} , T , L O _ {l})}{\sum_ {l = 1} ^ {p} \sum_ {t = 1} ^ {m} \left\{T (W R _ {i , j , k} , C T , L O _ {l}) \mid C T _ {t} \in N W D S e t (W R _ {i , j , k} , T) \right\}} \end{array}\tag{13}
$$

3.2.3.3. Step (C3): Calculate DPs of logistics activities for direct workers. Based on $E C ( W R _ { i , j , k } , ~ T , L O _ { l } ) , T r I ( W R _ { i , j , k } , ~ T , L O _ { l } )$ and $W t I ( W R _ { i , j , k } , T , O L _ { l } )$ of a direct worker in a speci<sup>fi</sup>c logistics task, the DP of the direct worker in the speci<sup>fi</sup>c logistics task at T can be calculated using the following equation.

$$
\begin{array}{c} F C (W R _ {i, j, k}, T, L O _ {l}) = E C (W R _ {i, j, k}, T, L O _ {l}) \times [ 1 + T r W \times T r I (W R _ {i, j, k}, T, L O _ {l}) ] \\ \times W t I (W R _ {i, j, k}, T, L O _ {l}) \end{array}\tag{14}
$$

where the weight TrW of the trend index for the direct worker in the speci<sup>fi</sup>c logistics task at T represents the level of which the EP is greater or smaller than the historical EP as the con<sup>fi</sup>dence interval of historical EPs is utilized. The weight can be determined via the following equation. For example, TrW is the ratio of the difference between $E C ( W R _ { i , j , k } , \ T , \ O L _ { l } )$ and $E C ( W R _ { i , j , k } , \ T , \ O L _ { l } )$ the difference between $C _ { 1 } ( W R _ { i , j , k } , H T , O L _ { l } )$ and $H E C ( W R _ { i , j , k } , H T , O L _ { l } )$ if TrI is equal to “1”.

$$
T r W = \left\{ \begin{array}{l l} \frac {E C (W R _ {i , j , k} , T , O L _ {l}) - C _ {1} (W R _ {i , j , k} , H T , O L _ {l})}{C _ {1} (W R _ {i , j , k} , H T , O L _ {l}) - H E C (W R _ {i , j , k} , H T , O L _ {l})}, & \text {   If   } \quad T r I (W R _ {i, j, k}, T, O L _ {l}) = 1 \\ 0, & \text {   If   } \quad T r I (W R _ {i, j, k}, T, O L _ {l}) = 0 \\ \frac {C _ {2} (W R _ {i , j , k} , T , O L _ {l}) - E C (W R _ {i , j , k} , T , O L _ {l})}{H E C (W R _ {i , j , k} , H T , O L _ {l}) - C _ {2} (W R _ {i , j , k} , H T , O L _ {l})}, & \text {   If   } \quad T r I (W R _ {i, j, k}, T, O L _ {l}) = - 1 \end{array} \right.\tag{15}
$$

## 3.3. IPD module

In the DPD module, the performance (i.e., RP, EP and DP) of direct workers in distinct logistics tasks at T can be determined by utilizing the operational data of the logistics tasks. In addition to determining the performance of direct workers, the managerial bene<sup>fi</sup>ts obtained by indirect managers must be considered in order to evaluate the performance of indirect managers. The IPD module that determines the performance of team-level managers, of<sup>fi</sup>ce-level managers and division managers can be classi<sup>fi</sup>ed into four stages: DP Estimation, VP Estimation, AP Estimation and IP Estimation.

## 3.3.1. VP calculation for team-level managers

In addition to direct participation in the logistics tasks, the teamlevel managers must also be responsible for the performance of <sup>fi</sup>rstline operators, the performing quality of logistics activities and the achievement of the scheduled operation plans of the logistics tasks. Considering the duties of the team-level managers, the VPs of teamlevel managers can be determined by utilizing the average performance index, the average quality index and the schedule index. The following section describes the calculation procedure for the VPs of team-level managers.

3.3.1.1. Step (D1): Calculate integrated DPs of team-level managers. For a team-level manager $W R _ { i } = 2 , j , k ,$ the integrated DP can be determined by a summation of the derived performance $F C ( W R _ { i = 2 , j , k } ,$ T) multiplied with the corresponding weighting values $\beta _ { l } .$ The above idea can be expressed using the following equation.

$$
I F C (W R _ {i = 2, j, k}, T) = \sum_ {l = 1} ^ {p} \beta_ {l} \times F C (W R _ {i = 2, j, k}, T, L O _ {l})\tag{16}
$$

where the weighting value $\beta _ { l }$ denotes the dif<sup>fi</sup>culty of direct workers in performing logistics task $L O _ { l } .$ That $\mathrm { i } s , \beta _ { l }$ is the ratio of the ef<sup>fi</sup>ciency of LO to the ef<sup>fi</sup>ciency of all logistics tasks and can be expressed using the following equation:

$$
\beta_ {l} = \frac {N (W R _ {i = 1 , j , k} , T , O L _ {l})}{T (W R _ {i = 1 , j , k} , T , O L _ {l})} \Bigg / \sum_ {l = 1} ^ {p} \frac {N (W R _ {i = 1 , j , k} , T , O L _ {l})}{T (W R _ {i = 1 , j , k} , T , O L _ {l})}.\tag{17}
$$

3.3.1.2. Step (D2): Calculate average performance indices of team-level managers. The average performance index of a team-level manager at T is the average of the multi-DPs of all direct workers managed by the corresponding team-level manager. The procedure for calculating the average performance index of a team-level manager is discussed below.

3.3.1.2.1. Step (D2-1): Merge DPs of first-line operators in logistics activities. Following Step (D1), the blended-DP $M F C ( W R _ { i = 1 , j , k } , ~ T ,$ LO) of a <sup>fi</sup>rst-line operator assigned to the logistics tasks at T can be obtained via the following equation:

$$
M F C (W R _ {i = 1, j, k}, T, L O) = \sum_ {l = 1} ^ {p} \beta_ {l} \times F C (W R _ {i = 1, j, k}, T, L O _ {l}).\tag{18}
$$

3.3.1.2.2. Step (D2-2): Calculate average of blended-DPs of all firstline operators for team-level managers. The average performance index of a team-level manager indicates how well the team-level manager manages the <sup>fi</sup>rst-line operators performing the logistics tasks. The average performance index can be determined using the sum of blended-DPs for all <sup>fi</sup>rst-line operators divided by the number of <sup>fi</sup>rstline operators in the corresponding team. The above concept can be described using the following equation:

$$
A D C I (W R _ {i = 2, j, k}, T) = \sum_ {k = 1} ^ {n _ {1 j}} M F C (W R _ {i = 1, j, k}, T, L O.) \Bigg / n _ {1, j}.\tag{19}
$$

3.3.1.3. Step (D3): Derive average quality indices for team-level managers. For a team-level manager, the average quality index is de<sup>fi</sup>ned as a blended error rate of the direct workers assigned to logistics tasks managed by the team-level manager at T. The procedure for deriving the average quality index of a team-level manager is discussed below.

3.3.1.3.1. Step (D3-1): Blend error rates of first-line operators in logistics activities. Following Step (D1-1), a blended error rate mer $( W R _ { i = 1 , j , k } , T , L O )$ of the <sup>fi</sup>rst-line operator $W R _ { i } = 1 , j , k$ can be determined using the summation of error rates $e r ( W R _ { i = 1 , j , k } , \bar { T } , L O _ { l } )$ in the logistics tasks $L O _ { l }$ in a team multiplied with the corresponding weighting values $\beta _ { l } .$ Here, the weighting value $\beta _ { l }$ denotes the average level of dif<sup>fi</sup>culty in performing the corresponding logistics task for the <sup>fi</sup>rstline operators. The above idea can be expressed using the following equation:

$$
m e r (W R _ {i = 1, j, k}, T, L O) = \sum_ {l = 1} ^ {p} \beta_ {l} \times e r (W R _ {i = 1, j, k}, T, L O _ {l}).\tag{20}
$$

3.3.1.3.2. Step (D3-2): Calculate average of blended error rates of all first-line operators for team-level managers. The average quality index of a team-level manager shows the working quality with which he manages the corresponding <sup>fi</sup>rst-line operators performing the logistics tasks for his team. For a team-level manager, the average quality index $A D Q I ( W R _ { i = 2 , j , k } , T )$ can be determined using the average of the sum of $m e r ( W R _ { i = 1 , j , k } , \ T , \ L O )$ for the <sup>fi</sup>rst-line operators managed by the team-level manager. The equation for calculating $A D Q I ( W R _ { i = 2 , j , k } , T )$ is as follows:

$$
A D Q I (W R _ {i = 2, j, k}, T) = \sum_ {k = 1} ^ {n _ {1, j}} m e r (W R _ {i = 1, j, k}, T, L O.) \Bigg / n _ {1, j}.\tag{21}
$$

3.3.1.4. Step (D4): Calculate schedule indices for team-level managers. For a team-level manager, the schedule index shows his ability to control the logistics action plans. That is, a schedule index can be used to evaluate whether the team-level manager accurately implements the logistics action plans (e.g., arranging the logistics tasks and their corresponding operation volumes). The procedure for calculating the schedule index of a team-level manager is discussed below.

3.3.1.4.1. Step (D4-1): Calculate completion levels of logistics activities. Before calculating the schedule index of a team-level manager, the assigned operation volumes $P N ( C T _ { t } , \ L O _ { l } )$ of logistics tasks in $C T _ { t }$ must be <sup>fi</sup>rst acquired. Subsequently, the completion level of a logistics task within CT can be determined using the ratio of operation volume sum to the assigned operation volumes of the logistics tasks. The completion level $C D ( C T _ { t } , L O _ { l } )$ of a logistics task is represented by the following equation:

$$
C D (C T _ {t}, L O _ {l}) = \sum_ {k = 1} ^ {n _ {i j}} N (W R _ {i, j, k}, C T _ {t}, L O _ {l}) \Bigg / P N (C T _ {t}, L O _ {l}).\tag{22}
$$

After determining $C D ( C T _ { t } , L O _ { l } )$ within $C T _ { t } ,$ a completion level CD(T, LO ) of the logistics task within T can also be determined using the following equation:

$$
C D (T, L O _ {l}) = \sum_ {t = 1} ^ {m} C D (C T _ {t}, L O _ {l}) \Big / m.\tag{23}
$$

3.3.1.4.2. Step (D4-2): Calculate schedule indices of team-level managers. The schedule index of a team-level manager represents the percentage of completed logistics tasks. Thus, the completion level $C D ( T , L O _ { l } )$ of a logistics task within T must be combined to determine the schedule indices of team-level managers. The schedule index DSCI $( W R _ { i = 2 , j , k } , ~ T )$ of a team-level manager can be obtained using the following equation:

$$
D S C I (W R _ {i = 2, j, k}, T) = \sum_ {l = 1} ^ {p} \beta_ {l} \times C D (T, L O _ {l})\tag{24}
$$

3.3.1.5. Step (D5): Calculate VP for team-level managers. Before calculating VP, the integrated DP and the average performance indices of each team-level manager should be averaged because a team-level manager might participate in the logistics tasks with the <sup>fi</sup>rst-line operators and manage the <sup>fi</sup>rst-line operators while performing the logistics activities at the same time. Thus, integrated DPs $I F C ( W R _ { i = 2 , j , k } ,$ T) and the average performance indices $A D C I ( W R _ { i = 2 , j , k } , \ T )$ of the team-level managers should <sup>fi</sup>rst be averaged for VP derivation. Afterwards, considering the importance of the average quality index $A D Q I ( W R _ { i = 2 , j , k } , \ T )$ and the schedule index $\boldsymbol { D S C I } ( \boldsymbol { W R _ { i = 2 , j , k } } , \textit { T } )$ for team-level managers, the $\mathsf { V P } V C ( W R _ { i = 2 , j , k } , T )$ of a team-level manager $W R _ { i } = 2 , j , k$ can be derived based on the following equation:

$$
\begin{array}{l} V C (W R _ {i = 2, j, k}, T) = \left[ \frac {I F C (W R _ {i = 2 , j , k} , T) + A D C I (W R _ {i = 2 , j , k} , T)}{2} \right] \\ \times [ 1 - A D Q I (W R _ {i = 2, j, k}, T) ] \times D S C I (W R _ {i = 2, j, k}, T). \end{array}\tag{25}
$$

## 3.3.2. AP calculation for division-level managers

At this stage, the APs of division-level managers can be determined on the basis of their budget control performance. In the following, the calculation procedure for the budget index and the AP for a divisionlevel manager are discussed.

3.3.2.1. Step (E1): Calculate the blended VP of division managers. Following Step (D3-2), the blended VP $M V C ( W R _ { i = 3 , j , k } , \ T )$ of the division-level manager $W R _ { i = 3 , j , k }$ can be obtained by averaging the VPs $V C ( W R _ { i = 2 , j , k } , ~ T )$ for team-level managers $W R _ { i = 2 , j , k }$ in the same division at T. The above concept can be described using the following equation:

$$
M V C (W R _ {i = 3, j, k}, T) = \sum_ {k = 1} ^ {n _ {2, j}} V C (W R _ {i = 2, j, k}, T) / n _ {2, j}.\tag{26}
$$

3.3.2.2. Step (E2): Calculate budget indices for division-level managers. Before calculating the budget indices, both the budgets and expenditures of the jth division at T must <sup>fi</sup>rst be acquired. For a division-level manager, the budget index shows his/her ability to control the budget. The budget index can be used to indicate whether a division-level manager can effectively reduce expenditure. The division-level manager with a higher budget index is capable of reducing division expenditure. Accordingly, the ratio of the difference between the division budgets PE(j,T) and the division expenditures RE (j,T) and the division budgets can be used to determine the ability of a division-level manager to control a budget. Thus, the budget index FCI $( W R _ { i = 3 , j , k } , ~ T )$ of a division-level manager can be derived using the following equation:

$$
F C I (W R _ {i = 3, j, k}, T) = 1 + [ P E (j, T) - R E (j, T) / P E (j, T) ].\tag{27}
$$

3.3.2.3. Step (E3): Calculate AP for division-level managers. Because division-level managers control division expenditure, the budget indices $F C I ( W R _ { i = 3 , j , k } , T )$ should be considered while using the blended VP $M V C ( W R _ { i = 3 , j , k } , T )$ to calculate the AP of division-level managers $W R _ { i = 3 , j , k }$ at T. Accordingly, the $\mathsf { A P } _ { \mathit { I C } } ( W R _ { i = 3 , j , k } , T )$ of a division-level manager at T can be calculated using the following equation:

$$
I C (W R _ {i = 3, j, k}, T) = M V C (W R _ {i = 3, j, k}, T) \times F C I (W R _ {i = 3, j, k}, T).\tag{28}
$$

## 3.3.3. IP calculation for office-level managers

Of<sup>fi</sup>ce-level managers must propose the operation plans of a DC and the division-level managers must bring these plans into action. Thus, the performance of division-level managers can be used to evaluate the IPs of of<sup>fi</sup>ce-level managers. The following step reveals the IP calculation details for of<sup>fi</sup>ce-level managers.

3.3.3.1. Step (F): Calculate IP for office-level managers. Although of<sup>fi</sup>celevel managers do not directly participate in logistics tasks, they should be responsible for leading division-level managers in the management of their corresponding divisions. Therefore, the IP for of<sup>fi</sup>ce-level managers can be estimated using the APs of division-level managers. Based on the above idea, the IP $P C ( W R _ { i = 4 , j , k } , T )$ of an of<sup>fi</sup>celevel manager at T can be calculated by averaging the APs $I C ( W R _ { i = 3 , j , k } ,$ T) of division-level managers. The above concept can be expressed using the following equation:

$$
P C (W R _ {i = 4, j, k}, T) = \sum_ {k = 1} ^ {n _ {i = 4, j}} I C (W R _ {i = 3, j, k}, T) \Bigg / n _ {i = 3, j}.\tag{29}
$$

## 3.3.4. Calculation of standard performance score for employees

In addition to fundamental logistics management tasks (e.g., budget control), indirect managers should also be responsible for improving logistics activities to enhance operational ef<sup>fi</sup>ciency. In order to evaluate the bene<sup>fi</sup>ts generated by indirect managers, any improvement in performance brought about by indirect managers in logistics activities should also be considered while transforming the distinct categories of employee performance into the standard performance scores for all employees. As a result, any bottleneck of employees or logistics tasks can be identi<sup>fi</sup>ed using standard performance scores.

3.3.4.1. Step (G1): Calculate whole growth rate of EPs. The primary goal of an indirect manager is to improve the performance of logistics tasks for the purpose of enhancing the DC operation competency and ef<sup>fi</sup>ciency. In other words, the improvement of logistics tasks can enhance operation ef<sup>fi</sup>ciency. Thus, the entire growth rate of EPs represents the bene<sup>fi</sup>ts of improved logistics tasks in a DC. The following procedure reveals the process by which to obtain the entire growth rate of EPs.

First, the blended EP $M E C ( W R _ { i = 1 , 2 , j , k } , T , L O )$ of all direct workers at T must be integrated by using the weighting values $\beta _ { i }$ of logistics tasks combined with the EPs $E C ( W R _ { i = 1 . 2 , j , k } , T , L O _ { l } )$ of direct workers. Next, the entire EP $A E C ( W R _ { i = 1 , 2 ; \ ; \ , \ T } )$ of a DC can be obtained by averaging the blended EP $M E C ( W R _ { i = 1 , 2 , j , k } , \ T , \ L O )$ of direct workers at T. The above idea can be expressed using the following equations:

$$
M E C (W R _ {i = 1, 2, j, k}, T, L O) = \sum_ {l = 1} ^ {p} \beta_ {l} \times E C (W R _ {i = 1. 2, j, k}, T, L O _ {l})\tag{30}
$$

$$
\begin{array}{l} A E C (W R _ {i = 1, 2; \cdot}, T) \\ = \sum_ {i = 1} ^ {2} \sum_ {j = 1} ^ {b} \sum_ {k = 1} ^ {n _ {i = 1, 2, j}} M E C (W R _ {i = 1, 2, j, k}, T, L O \cdot) / 2 \times b \times n _ {i = 1, 2, j}. \end{array}\tag{31}
$$

Following the above formula for calculating $A E C ( W R _ { i = 1 , 2 ; ~ ; ~ } , T ) ,$ the entire historical EP $A H E C ( W R _ { i = 1 , 2 ; \ ; \ H T } )$ of direct workers at HT can be obtained using the following equation:

$$
\begin{array}{l} A H E C (W R _ {i = 1, 2 \cdot \cdot \cdot}, H T) \\ = \sum_ {i = 1} ^ {2} \sum_ {j = 1} ^ {b} \sum_ {k = 1} ^ {n _ {1 = 1, 2 j}} \left[ \sum_ {l = 1} ^ {p} \beta_ {l} \times E C (W R _ {i, 1, 2, j, k}, H T, L O _ {l}) \right] / 2 \times b \times n _ {i = 1, 2 j}. \end{array}\tag{32}
$$

Finally, the entire growth rate AECGR(T) of EPs at T can be derived using the ratio of the difference between “the whole EP for direct managers a $\mathbf { \nabla } T ^ { \prime }$ and “the whole historical EP for direct managers at $H T ^ { \prime }$ and “the whole historical EP for direct managers at $H T ^ { \prime }$ . The above idea can be represented using the following equation:

$$
A E C G R (T) = \left[ A E C \left(W R _ {i = 1, 2, \because}, T\right) - A H E C \left(W R _ {i = 1, 2, \because}, T\right) \right] / A H E C \left(W R _ {i = 1, 2, \because}, T\right).\tag{33}
$$

3.3.4.2. Step (G2): Calculate improvement weights. In a DC organization, higher level managers should be assigned a higher improvement weight when transforming the distinct employee performance indices into a standard performance score because they are responsible for managing a larger number of staff. These managers must spend more time and effort to enhance the EPs of direct operators by improving logistics tasks. In order to distinguish the difference between improvement bene<sup>fi</sup>ts generated by two levels of managers (e.g., the team-level and the division-level), this model assumes that the improvement weights for transforming the employee performance indices into a standard performance score follows a geometric series. Based on the above assumption, the improvement weight IBN(i,T) at T can be determined using the whole growth rate AECGR(T) of EPs and the organization level (i) corresponding to the employee. The above idea can be expressed using the following equation:

$$
I B N (i, T) = [ 1 + A E C G R (T) ] ^ {i - 1}.\tag{34}
$$

3.3.4.3. Step (G3): Calculate performance scores of all employees. In order to accurately estimate the contributions and analyze the performance of all employees, employee performance (i.e., DPs $F C ( W R _ { i = 1 , j , k } ,$ T), VPs $V C ( W R _ { i = 2 , j , k } , \ T )$ , APs $I C ( W R _ { i = 3 , j , k } , \ T )$ , IPs $P C ( W R _ { i = 4 , j , k } , \ T ) )$ derived in previous steps should be transformed into a standard performance score by utilizing the improvement weights IBN(i, T). Based on the above idea, the standard performance score $C S ( W R _ { i , j , k } , T )$ corresponding to each type of employee, including the <sup>fi</sup>rst-line operators, the team-level managers, division-level managers and of<sup>fi</sup>ce-level managers, at time interval T can be calculated based on their role in a DC.

$$
C S (W R _ {i, j, k}, T) = \left\{ \begin{array}{l l} F C (W R _ {i, j, k}, T) \times I B N (i, T) & \text {   If   } i = 1 \\ V C (W R _ {i, j, k}, T) \times I B N (i, T) & \text {   If   } i = 2 \\ I C (W R _ {i, j, k}, T) \times I B N (i, T) & \text {   If   } i = 3 \\ P C (W R _ {i, j, k}, T) \times I B N (i, T) & \text {   If   } i = 4 \end{array} \right..\tag{35}
$$

By analyzing the distribution of the standard performance scores for all employees taking part in logistics tasks, the employees who generate more bene<sup>fi</sup>ts to the DC can be identi<sup>fi</sup>ed. That is, the inexperienced employees and the low-performance logistics tasks can also be determined according to standard performance scores.

## 4. Logistics information management platform

In order to demonstrate the applicability of the proposed model, a web-based logistics information management (LIM) platform was established in this research. Under the LIM platform, four main modules are provided: Fundamental Logistics Data Maintenance (FLDM), Business Information Management (BIM), Shop Floor Status Report (SFSR) and Employee Performance Calculation (EPC). In the following, the LIM platform integrated with the employee performance calculation algorithms is introduced.

Before calculating employee performance, the fundamental logistics data (e.g., the logistics activities, the employees and the DC organization), must <sup>fi</sup>rst be maintained used the FLDM module (Fig. 3). Using the SFSR and BIM modules, the logistics operation data (e.g., the working days, the operation volume and the defect volume) as well as the business information (e.g., the division budget or the scheduled operation volumes of logistics tasks) can be imported into the LIM database by the administrators (e.g., team-level or divisionlevel managers) to serve as the inputs for the employee performance calculation (Fig. 4). Based on the above data, the LIM platform can automatically generate employee performance (i.e., RP, EP, DP, VP, AP and IP) for the decision makers of the DC using the EPC module (Fig. 5) as the user requests a employee performance calculation (e.g., the employee name or time interval). The LIM platform also provides tabulated and graphical interfaces to display the detailed data (Figs. 6 and 7) as well as the statistics (Fig. 8) regarding employee performance for the DC decision makers in order to assist them to analyze the performance of each employee.

In summary, the proposed model for employee performance calculation and the application modules developed under the LIM platform can be used in DCs to ef<sup>fi</sup>ciently and accurately identify lowperformance logistics tasks and inexperienced online employees in real time. Based on the bottleneck analysis of employees and logistics tasks, DC decision makers can improve low-performance logistics and assist inexperienced employees through effective training.

## 5. Case study

In order to verify the applicability of the employee performance estimation (EPE) model and logistics information management (LIM) platform, a real-world case, Nung Hsueh distribution center which is the largest logistics center of the printing industry in Taiwan, was used in this study. Three evaluation approaches, including the random

![](/api/attachments/63VMYGJR/fulltext/images/d530810870d097981debdc1c957a99e619379b10871cbc3cc677b95c4de01c16.jpg)  
Fig. 3. Interface for FLDM.

![](/api/attachments/63VMYGJR/fulltext/images/f76b32fff81312a2fc8962e494675e2ba04d89417e5e3d4fc6676e2a232c17b6.jpg)

![](/api/attachments/63VMYGJR/fulltext/images/fd2e38d2431dd52e6266a7e72ac23600d9e857562c7ec26add35b6a5bcd87faa.jpg)

approach, expert (i.e., the DC managers) evaluation and the EPE approach, were applied to evaluate the performance of employees (i.e., the <sup>fi</sup>rst-line operators, team-level managers, of<sup>fi</sup>ce-level managers and division-level managers) in Nung Hsueh distribution center. After that, the employees can be ranked based on their performance generated by the three evaluation approaches and the ranks of employee performance determined via the three approaches can be acquired. The related details, including collection of evaluation data, performance evaluation and evaluation approach analysis, can be discussed in the following.

Fig. 5. Display of employee performance.  
![](/api/attachments/63VMYGJR/fulltext/images/4ef0a4741468c8816d3e8cb47d6065522d6705b539803722df563c3a67b56edc.jpg)  
Fig. 6. Tabulated logistics data for employee performance calculation.

![](/api/attachments/63VMYGJR/fulltext/images/386ac24e2ea4edbcce8e54914618dc4bb10eb7cac27318086d013be6eb695a38.jpg)  
Fig. 7. Visualized display of employee performance.

## 1. Collection of evaluation data

The evaluation data of 36 distinct <sup>fi</sup>rst-line operators (A1, A2, …, A36), 12 distinct team-level managers (B1, B2, …, B12), 4 of<sup>fi</sup>ce-level managers (C1, C2, C3, C4) and 2 division-level managers was acquired via the operation records of the shop-<sup>fl</sup>oor and the business forms of the accounting department from the 1st to 30th September, 2007. The evaluation data was composed of the following items:

• The operation volumes, operation time and error volumes of employees in the logistics tasks

• The scheduled operation volumes of logistics tasks in the team-level units

• The budgets and expenditures determined in the of<sup>fi</sup>ce-level units

After acquiring the evaluation data, the evaluation data can to be summarized via the traditional statistics graphics for employee performance appraisal and be imported into the LIM platform to utilize the random approach, expert evaluation and the EPE approach to evaluate the employee performance.

## 2. Performance evaluation

The procedure to evaluate the employee performance and to determinate the employee performance ranks via the three approaches are described as follows:

• Random approach

The random numbers were used to generate the evaluation score (between 1 and 100) of employees and the employees were ranked based on their scores. Ten series of employee performance ranks can be obtained by repeating the above evaluation processes. In addition, the average and standard deviation of employee performance ranks for each employee can be calculated and be regarded as the nonprofessional evaluation results.

![](/api/attachments/63VMYGJR/fulltext/images/6eca8a4d160c7b6bb5fc2b0e35d2facc9e530cfca2118ade3d61a27fc4a15ed3.jpg)  
Fig. 8. Logistics statistics for employee performance calculation.

## • EPE approach

The EPE approach was used to estimate the employee performance, including the derived performance of <sup>fi</sup>rst-line operations, veri<sup>fi</sup>cation performance of team-level managers, inference performance of of<sup>fi</sup>ce-level managers and assessment performance of division-level managers. The employees were also ranked based on the employee performance and the employee performance ranks can be regarded as the systematical evaluation results.

## • Expert evaluation

Ten experienced DC managers were selected and requested to assign the appropriate scores between 1 and 100 to the employees based on the traditional statistics graphics of the employee performance in order to denote the grade of employee performance. The evaluation scores of employees in the 10 evaluation experiments can be acquired and the employees were ranked based on their scores. Furthermore, the average and standard deviation of employee performance ranks for each employee can be calculated and regarded as the professional but non-systematical evaluation results.

In the random and expert evaluations, the employees can be reranked based on their average ranks. The average and standard deviation of performance ranks and the <sup>fi</sup>nal performance rank for each employee can be summarized in Table 3.

## 3. Evaluation approach analysis

In order to evaluate the applicability of the three evaluation approaches, the variance of the evaluation scores, reasonableness and similarity of employee performance ranks can be analyzed based on the evaluation scores and employee performance ranks. The procedure to analyze the variance of the evaluation scores, reasonableness and similarity of the employee performance ranks are described as follows:

Table 4  
The ANOVA table of evaluation scores.

<table><tr><td>Evaluation approach</td><td>Source</td><td>SS</td><td>DF</td><td>MS</td><td>F</td><td>p-value</td></tr><tr><td rowspan="4">Random approach</td><td>Employee</td><td>54962.93</td><td>53</td><td>1037.04</td><td>1.31</td><td>0.081</td></tr><tr><td>Experiment</td><td>7290.56</td><td>9</td><td>810.06</td><td>1.02</td><td>0.423</td></tr><tr><td>Error</td><td>379161.80</td><td>477</td><td>794.89</td><td></td><td></td></tr><tr><td>Total</td><td>441415.30</td><td>539</td><td></td><td></td><td></td></tr><tr><td rowspan="4">Expert evaluation</td><td>Employee</td><td>16990.01</td><td>53</td><td>320.56</td><td>3.68</td><td>&lt;0.001</td></tr><tr><td>Expert</td><td>10115.08</td><td>9</td><td>1123.89</td><td>12.90</td><td>&lt;0.001</td></tr><tr><td>Error</td><td>41537.32</td><td>477</td><td>87.08</td><td></td><td></td></tr><tr><td>Total</td><td>68642.41</td><td>539</td><td></td><td></td><td></td></tr></table>

## • Analysis of the variance of evaluation scores

In order to analyze the difference of appraisal results in each evaluation experiment, the distinct evaluation experiments and employees were regarded as factors and the two-way analysis of variation (i.e., ANOVA) was used to analyze the evaluation scores determined via the random approach and expert evaluation (Table 4).

As shown in Table 4, the p-values of the null hypotheses (i.e., the evaluation scores are identical and the appraisal criteria applied to evaluate the employee performance are consistent in each evaluation experiment) in the random approach are less than 0.01 and the two null hypotheses of the random evaluation cannot be rejected. Therefore, the employee performance can be consistently evaluated via the identical appraisal criteria. However, employees with distinct performance cannot be effectively identi<sup>fi</sup>ed. In addition, the two null hypotheses of the expert evaluation approach should be rejected (i.e., p-valueb0.01). Although the employees with distinct performance can be effectively distinguished, the appraisal criteria of distinct experts are signi<sup>fi</sup>cantly different. In other words, the evaluation results are inconsistent for different experts. As a result, the evaluation results determined via the experts (i.e., the DC managers) have to be rechecked in order to obtain the reasonable performance evaluation. However, it might take the DC a lot of time and cost to recheck the evaluation results. Thus, a systematical approach (e.g., the EPE model) should be developed in order to acquire reasonable performance evaluation results.

Table 3  
Employee performance ranks of three evaluation approaches.

<table><tr><td rowspan="2">Employee</td><td colspan="3">Random</td><td>EPE</td><td colspan="3">Expert</td><td rowspan="2">Employee</td><td colspan="3">Random</td><td>EPE</td><td colspan="3">Expert</td></tr><tr><td>Avg.</td><td>Std.</td><td>Rk.</td><td>Rk.</td><td>Avg.</td><td>Std.</td><td>Rk.</td><td>Avg.</td><td>Std.</td><td>Rk.</td><td>Rk.</td><td>Avg.</td><td>Std.</td><td>Rk.</td></tr><tr><td>A1</td><td>26.7</td><td>8.9</td><td>36</td><td>5</td><td>9.3</td><td>6.59</td><td>2</td><td>A28</td><td>19.1</td><td>8.1</td><td>26</td><td>34</td><td>19.0</td><td>8.45</td><td>22</td></tr><tr><td>A2</td><td>15.7</td><td>7.6</td><td>11</td><td>6</td><td>15.6</td><td>9.18</td><td>14</td><td>A29</td><td>17.5</td><td>8.7</td><td>12</td><td>32</td><td>24.4</td><td>8.45</td><td>30</td></tr><tr><td>A3</td><td>20.6</td><td>11.7</td><td>28</td><td>4</td><td>15.1</td><td>11.37</td><td>13</td><td>A30</td><td>20.2</td><td>12.3</td><td>15</td><td>28</td><td>10.2</td><td>8.20</td><td>5</td></tr><tr><td>A4</td><td>15.5</td><td>9.5</td><td>8</td><td>10</td><td>17.1</td><td>9.46</td><td>18</td><td>A31</td><td>16.8</td><td>9.7</td><td>7</td><td>24</td><td>16.8</td><td>5.60</td><td>17</td></tr><tr><td>A5</td><td>20.0</td><td>8.9</td><td>24</td><td>11</td><td>9.7</td><td>8.32</td><td>3</td><td>A32</td><td>17.6</td><td>9.6</td><td>19</td><td>17</td><td>19.5</td><td>11.02</td><td>23</td></tr><tr><td>A6</td><td>18.3</td><td>10.2</td><td>16</td><td>20</td><td>14.4</td><td>10.21</td><td>11</td><td>A33</td><td>15.3</td><td>9.3</td><td>24</td><td>23</td><td>17.1</td><td>8.25</td><td>18</td></tr><tr><td>A7</td><td>14.9</td><td>9.7</td><td>5</td><td>19</td><td>12.8</td><td>8.11</td><td>6</td><td>A34</td><td>19.0</td><td>10.1</td><td>16</td><td>27</td><td>22.2</td><td>8.68</td><td>29</td></tr><tr><td>A8</td><td>23.3</td><td>11.1</td><td>33</td><td>33</td><td>21.1</td><td>8.65</td><td>27</td><td>A35</td><td>20.0</td><td>10.1</td><td>13</td><td>35</td><td>17.6</td><td>10.13</td><td>20</td></tr><tr><td>A9</td><td>25.7</td><td>4.8</td><td>35</td><td>30</td><td>14.3</td><td>8.61</td><td>10</td><td>A36</td><td>18.3</td><td>12.1</td><td>18</td><td>36</td><td>25.5</td><td>9.66</td><td>32</td></tr><tr><td>A10</td><td>21.3</td><td>11.0</td><td>29</td><td>14</td><td>14.0</td><td>8.69</td><td>8</td><td>B1</td><td>6.4</td><td>3.8</td><td>6</td><td>2</td><td>4.5</td><td>2.94</td><td>3</td></tr><tr><td>A11</td><td>11.4</td><td>6.1</td><td>3</td><td>18</td><td>20.2</td><td>8.87</td><td>25</td><td>B2</td><td>6.1</td><td>3.6</td><td>4</td><td>5</td><td>3.3</td><td>3.13</td><td>2</td></tr><tr><td>A12</td><td>7.7</td><td>6.4</td><td>1</td><td>15</td><td>15.7</td><td>10.01</td><td>15</td><td>B3</td><td>4.7</td><td>3.5</td><td>2</td><td>11</td><td>7.4</td><td>2.73</td><td>8</td></tr><tr><td>A13</td><td>20.3</td><td>12.6</td><td>27</td><td>2</td><td>8.8</td><td>5.78</td><td>1</td><td>B4</td><td>5.0</td><td>3.3</td><td>3</td><td>8</td><td>4.6</td><td>1.56</td><td>4</td></tr><tr><td>A14</td><td>15.1</td><td>10.5</td><td>6</td><td>3</td><td>12.9</td><td>9.20</td><td>7</td><td>B5</td><td>7.0</td><td>3.2</td><td>8</td><td>1</td><td>3.1</td><td>1.70</td><td>1</td></tr><tr><td>A15</td><td>14.5</td><td>5.9</td><td>4</td><td>7</td><td>19.5</td><td>10.05</td><td>23</td><td>B6</td><td>6.3</td><td>3.4</td><td>5</td><td>9</td><td>6.1</td><td>3.08</td><td>7</td></tr><tr><td>A16</td><td>15.5</td><td>11.2</td><td>8</td><td>9</td><td>15.0</td><td>8.32</td><td>12</td><td>B7</td><td>6.4</td><td>3.2</td><td>6</td><td>4</td><td>9.7</td><td>1.90</td><td>11</td></tr><tr><td>A17</td><td>26.7</td><td>8.9</td><td>23</td><td>13</td><td>21.0</td><td>5.87</td><td>26</td><td>B8</td><td>8.0</td><td>3.7</td><td>11</td><td>3</td><td>10.7</td><td>1.10</td><td>12</td></tr><tr><td>A18</td><td>15.7</td><td>7.6</td><td>8</td><td>25</td><td>28.5</td><td>8.11</td><td>35</td><td>B9</td><td>8.6</td><td>1.8</td><td>12</td><td>7</td><td>8.7</td><td>2.57</td><td>1</td></tr><tr><td>A19</td><td>19.9</td><td>10.4</td><td>22</td><td>31</td><td>27.6</td><td>7.12</td><td>33</td><td>B10</td><td>4.5</td><td>3.0</td><td>1</td><td>10</td><td>7.4</td><td>2.69</td><td>8</td></tr><tr><td>A20</td><td>15.5</td><td>10.7</td><td>19</td><td>29</td><td>28.4</td><td>6.68</td><td>34</td><td>B11</td><td>7.0</td><td>2.4</td><td>8</td><td>6</td><td>5.9</td><td>2.47</td><td>6</td></tr><tr><td>A21</td><td>19.2</td><td>10.3</td><td>30</td><td>26</td><td>29.0</td><td>6.43</td><td>36</td><td>B12</td><td>7.1</td><td>3.0</td><td>10</td><td>12</td><td>4.7</td><td>3.10</td><td>5</td></tr><tr><td>A22</td><td>19.0</td><td>9.8</td><td>2</td><td>1</td><td>14.1</td><td>11.09</td><td>9</td><td>C1</td><td>2.3</td><td>1.1</td><td>2</td><td>1</td><td>1.8</td><td>1.08</td><td>1</td></tr><tr><td>A23</td><td>21.4</td><td>12.0</td><td>34</td><td>16</td><td>25.2</td><td>8.95</td><td>31</td><td>C2</td><td>2.7</td><td>1.2</td><td>4</td><td>3</td><td>2.6</td><td>0.92</td><td>3</td></tr><tr><td>A24</td><td>10.3</td><td>6.0</td><td>30</td><td>21</td><td>21.3</td><td>9.83</td><td>28</td><td>C3</td><td>2.6</td><td>1.1</td><td>3</td><td>2</td><td>2.9</td><td>1.04</td><td>4</td></tr><tr><td>A25</td><td>24.7</td><td>8.9</td><td>32</td><td>8</td><td>9.8</td><td>7.59</td><td>4</td><td>C4</td><td>2.2</td><td>1.0</td><td>1</td><td>4</td><td>2.5</td><td>1.12</td><td>2</td></tr><tr><td>A26</td><td>21.4</td><td>5.7</td><td>21</td><td>12</td><td>16.4</td><td>8.44</td><td>16</td><td>D1</td><td>1.4</td><td>0.5</td><td>1</td><td>1</td><td>1.4</td><td>0.49</td><td>1</td></tr><tr><td>A27</td><td>22.5</td><td>9.1</td><td>14</td><td>22</td><td>18.9</td><td>9.35</td><td>21</td><td>D2</td><td>1.6</td><td>0.5</td><td>2</td><td>2</td><td>1.6</td><td>0.49</td><td>2</td></tr></table>

• Avg.: Average of employee performance ranks.  
• Std.: Standard deviation of employee performance ranks.  
• Rk.: Final employee performance rank.

## • Analysis of reasonableness of <sup>fi</sup>nal employee performance ranks

The <sup>fi</sup>nal employee performance ranks determined by experts were regarded as the nominal employee performance ranks. Reasonableness of the <sup>fi</sup>nal employee performance ranks can be determined by analyzing whether the <sup>fi</sup>nal employee performance ranks fall into the acceptable rank intervals accepted by the DC managers. The reasonableness of <sup>fi</sup>nal employee performance ranks determined via the EPE approach can be derived via the following procedure.

(1) Determine the con<sup>fi</sup>dence intervals of employee performance ranks based on the average and standard deviation of <sup>fi</sup>nal employee performance ranks. The con<sup>fi</sup>dence intervals can be regarded as the reasonable rank ranges of employee performance ranks accepted by the DC managers.

(2) Analyze whether the <sup>fi</sup>nal employee performance ranks fall into the reasonable rank ranges in order to obtain a reasonableness index for the <sup>fi</sup>nal employee performance ranks. If a <sup>fi</sup>nal employee performance rank falls into the reasonable rank range, the corresponding reasonableness index is “1”; otherwise, “0” is assigned.

(3) Accumulate the reasonableness indices of the EPE approach to obtain the total number of acceptable employee performance ranks. The number of acceptable employee performance ranks determined via the EPE approach is “49”.

(4) Determine the acceptance rate of <sup>fi</sup>nal employee performance ranks via the ratio of “the number of accepted employee performance ranks” to “the number of employees”. Therefore, the acceptance rate of the EPE approach is “90.74%” (i.e., 49/ 54).

As a result, the <sup>fi</sup>nal employee performance ranks determined via the EPE approach are acceptable by the DC managers. Therefore, the EPE model can effectively generate reasonable and acceptable performance evaluation results.

## • Analysis of similarity of <sup>fi</sup>nal employee performance ranks

The <sup>fi</sup>nal employee performance ranks of the expert evaluation were regarded as the nominal employee performance ranks. The consistency of the <sup>fi</sup>nal employee performance ranks derived via the random and EPE approaches between the ones derived via expert evaluation was analyzed. Before analyzing the consistency, the <sup>fi</sup>nal employee performance ranks have to be processed according to the following procedure.

Table 6  
Similarity analysis of the three evaluation approaches.

<table><tr><td>Index</td><td>Random vs. Expert</td><td>EPE vs. Expert</td></tr><tr><td>Similarity</td><td>51.06%</td><td>69.27%</td></tr><tr><td>Improvement ratio</td><td colspan="2">35.78%</td></tr></table>

(1) Determine the rank sequence pattern (e.g., A12→A22→ $\mathsf { A } 1 1 {  } . . .  \mathsf { A } 9 {  } \mathsf { A } 1 )$ with respect to each employee level based on the <sup>fi</sup>nal ranks (as shown in Table 3).

(2) Acquire the pairwise sequences of employees (e.g., (A12,A22), (A12,A11), …, (A9,A1)). The numbers of pairwise sequences for the <sup>fi</sup>rst-line, team-level, of<sup>fi</sup>ce-level and division-level employees are $C _ { 2 } ^ { 3 6 } = 6 3 0 , C _ { 2 } ^ { 1 2 } = 6 6 , C _ { 2 } ^ { 4 } = = 6 \mathrm { a n d } C _ { 2 } ^ { 2 } = 1$ . Therefore, the total number of pairwise sequences corresponding to each approach is 703 (i.e., 630+66+6+1).

(3) Identify the identical pairwise sequences in the “random and expert evaluations” and in the “EPE approach and expert evaluations”. In the random and expert evaluations, the numbers of identical pairwise sequences of the <sup>fi</sup>rst-line, team level, of<sup>fi</sup>ce level and division level employees are 319, 36, 3 and 1 respectively. In the EPE approach and expert evaluations, the numbers of identical pairwise sequences for the four distinct levels of employees are 446, 37, 3 and 1 respectively.

As shown in Table 5, among the 703 pairwise sequences with respect to the random evaluation, a total of 359 (i.e., 319+36+3+1) pairwise sequences (i.e., (A13,A1), (A13,A25), …, (C4,C2), (D1,D2)) are identical to the pairwise sequences with respect to the expert evaluation. That is, the similarity between the random and expert evaluations is 51.06% (i.e., 359/703). Similarly, the similarity between EPE approach and expert evaluations is 69.27% (i.e., 487/703). As a result, the improvement ratio of the similarity is 35.78% (Table 6).

According to the analysis results of the three approaches, the EPE model can effectively estimate the employee performance (similar to the results determined by several DC managers), and the employee performance generated by the EPE model can be accepted by the DC managers. Therefore, the inexperienced DC managers can used the EPE model to estimate the employee performance and regard the employee performance generated by the EPE model as the initial evaluation results in order to reduce the time and cost required for evaluating the employee performance.

Table 5  
Rank sequence patterns and pairwise sequences of three evaluation approaches.

<table><tr><td>Approach</td><td>Sequence</td><td>First-line</td><td>Team-level</td><td>Office-level</td><td>Division-level</td></tr><tr><td rowspan="3">Random (Ra)</td><td>Rank sequence pattern</td><td>A12→A22→A11→...→A9→A1</td><td>B10→B3→B1→...→B8→B9</td><td>C3→C1→C4→C2</td><td>D1→D2</td></tr><tr><td>Paired sequence</td><td>(A12,A22), (A12,A11), ... (A9,A1)</td><td>(B10,B3), (B10,B1), ... (B8,B9)</td><td>(C3,C1), (C3,C4), ... (C4,C2)</td><td>(D1,D2)</td></tr><tr><td>Number</td><td>630</td><td>66</td><td>6</td><td>1</td></tr><tr><td rowspan="3">EPE (Mp)</td><td>Rank sequence pattern</td><td>A22→A13→A14→...→A35→A36</td><td>B5→B1→B8→...→B3→B12</td><td>C1→C3→C2→C4</td><td>D1→D2</td></tr><tr><td>Paired sequence</td><td>(A22,A13), (A22,A14), ..., (A35,A36)</td><td>(B5,B1), (B5,B8), ... (B3,B12)</td><td>(C1,C3), (C1,C2), ... (C2,C4)</td><td>(D1,D2)</td></tr><tr><td>Number</td><td>630</td><td>66</td><td>6</td><td>1</td></tr><tr><td rowspan="3">Expert (Ex)</td><td>Rank sequence pattern</td><td>A13→A1→A5→...→A18→A21</td><td>B5→B2→B1→...→B7→B8</td><td>C1→C4→C2→C3</td><td>D1→D2</td></tr><tr><td>Paired sequence</td><td>(A13,A1), (A13,A5), ..., (A18,A21)</td><td>(B5,B2), (B5,B1), ... (B7,B8)</td><td>(C1,C4), (C1,C2), ... (C2,C3)</td><td>(D1,D2)</td></tr><tr><td>Number</td><td>630</td><td>66</td><td>6</td><td>1</td></tr><tr><td>Identical paired sequences between (Ra) and (Ex)</td><td></td><td>(A13,A1), (A13,A25), ..., (A18,A21)</td><td>(B5,B12), (B5,B11), ..., (B7, B7)</td><td>(C1,C4), (C1,C2), (C4,C2)</td><td>(D1,D2)</td></tr><tr><td>Number</td><td></td><td>319</td><td>36</td><td>3</td><td>1</td></tr><tr><td>Identical paired sequences between (Mp) and (Ex)</td><td></td><td>(A22,A3), (A22,A2), ..., (A35,A36)</td><td>(B5,B1), (B5,B8), ..., (B6,B3)</td><td>(C1,C3), (C1,C2), (C1,C4)</td><td>(D1,D2)</td></tr><tr><td>Number</td><td></td><td>446</td><td>37</td><td>3</td><td>1</td></tr></table>

## 6. Conclusion

To accurately estimate the employee performance in a DC, this paper developed an integrated model to calculate the employee performance based on the logistics operation data and business information. In the proposed model, three critical modules including DPD, IPD and PSA were developed to estimate the logistics performance of employees at distinct levels in a DC organization hierarchy. According to the proposed model, this paper also established a web-based LIM platform to reduce the workload of DC decision makers, to assist in the management of logistics operation data and to support the bottleneck analysis of employees and logistics tasks. In addition, the Nung Hsueh DC in Taiwan was used to analyze applicability of the EPE model and the LIM platform. According to analysis results of the random approach, EPE approach and expert evaluation, the proposed model and platform can effectively assist the inexperienced DC managers to acquire the employee performance accepted by the experienced DC managers. As a whole, this paper presents a feasible approach for LSPs to accurately determine employee performance.

However, the applications (e.g., identi<sup>fi</sup>cation of employees with signi<sup>fi</sup>cant performance increase or decrease) of employee performance are not investigated in this paper. In order to assist the DC managers to manage the employees and logistics tasks, the future research can focus on applying the employee performance generated via the EPE model to identify the employees with the signi<sup>fi</sup>cant performance increase or decrease and that might be bene<sup>fi</sup>cial to enhance the operation ef<sup>fi</sup>ciency.

## References

[1] J.H. Ahn, S.G. Chang, Assessing the contribution of knowledge to business performance: the KP<sup>3</sup> methodology, Decision Support Systems 36 (2004) 403–416.

[2] C.C. Chen, Performance appraisal of advertising executive in newspaper, Graduate School of Communication Management, Ming Chuan University, Masters Thesis, (2001).

[3] S.C., Chen, The performance evaluation model for reception clerks in the hospitality industry, Institute of Human Resource Management, Sun Yat-Sen University, Masters Thesis, (2005).

[4] V.I. Coleman, W.C. Borman, Investigating the underlying structure of the citizenship performance domain, Human Resource Management Review 10 (1) (2000) 25–44.

[5] D.L. Deadrick, D.G. Gardner, Performance distributions: measuring employee performance using total quality management principles, Journal of Quality Management 4 (2) (1999) 225–241.

[6] K. Eguchi, Job transfer and in<sup>fl</sup>uence activities, Journal of Economic Behavior and Organization 56 (2005) 187–197.

[7] A. Golec, E. Kahya, A fuzzy model for competency-based employee evaluation and selection, Computers & Industrial Engineering 52 (2007) 143–161.

[8] E. Kahya, Revising the metal industry job evaluation system for blue-collar jobs, Compensation Bene<sup>fi</sup>ts Review 38 (6) (2006) 49–63

[9] E. Kahya, The effects of job characteristics and working conditions on job performance, International Journal of Industrial Ergonomics 37 (2007) 515–523.

[10] J.S. Kane, K.F. Kane, The analytic framework: the most promising approach for the advancement of performance appraisal, Human Resource Management Review 2 (1) (1992) 37–70

[11] C.Y. Laio, Free-air television stations technicians performance appraisal research, Graduate School of Communication Management, Ming Chuan University, Masters Thesis, (2000).

[12] K.H. Liu, Application of analytical hierarchy process on the research of discussion of the performance appraisal of room attendant in hotel industry, Graduate School of Communication Management, Ming Chuan University, Masters Thesis, (2004).

[13] C.J. Mcnair, R.L. Lynch, K.F. Cross, Do <sup>fi</sup>nancial and non-<sup>fi</sup>nancial measures of performance have to agree? Management Accounting (November, 1990) 28–36.

[14] S.H. Ow, H.W. Chen, An overview of the development of a computerized employee performance measurement tool-ECAS, Chiang Mai University Journal 5 (2) (2006) 229–241.

[15] H.P. Sims, A.D. Szilagyi Jr., R.T. Keller, The measurement of job characteristics, Academy of Management Journal 19 (2) (1976) 195–212.

[16] P.L. Sonja, Personnel selection fuzzy model, International Transactions in Operational Research 8 (1) (2001) 89–105.

[17] H.M. Tsai, Constructing performance evaluation criteria with AHP for nurse anesthetist, Institute of Health Care Management, Sun Yat-Sen University, Master Thesis, (2005).

[18] J.T. Tzeng, A study on applying analytic hierarchy process to technician performance evaluation for the paper industry, Institute of Human Resource Management, Sun Yat-Sen University, Masters Thesis, (2004).

[19] S.B. Yaakob, S. Kawata, Worker's placement in an industrial environment, Fuzzy Sets and Systems 106 (3) (1999) 289–297.

Yu-Jen Wu is a currently Ph.D. student in the Department of Industrial Engineering and Engineering Management at NTHU. His research interests are knowledge management and logistics management

Jiang-Liang Hou is a professor in the Department of Industrial Engineering and Engineering Management at National Tsing-Hua University (NTHU). Dr. Hou received his Ph.D. in Industrial Engineering at NTHU and his research interests are knowledge management and logistics management. He has participated in several industrial projects with high-tech companies and non-pro<sup>fi</sup>t R&D centers in Taiwan.
