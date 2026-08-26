---
otero_id: 1552
otero_key: "E74CUPZM"
title: "An RFID network design methodology for asset tracking in healthcare"
authors: "Asil Oztekin; Foad M. Pajouh; Dursun Delen; Leva K. Swim"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.01.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An RFID network design methodology for asset tracking in healthcare

Asil Oztekin <sup>a</sup>, Foad M. Pajouh <sup>a</sup>, Dursun Delen <sup>b,</sup>⁎, Leva K. Swim <sup>a,c</sup>

<sup>a</sup> School of Industrial Engineering and Management, Oklahoma State University, Stillwater, OK 74078, USA

<sup>b</sup> Spears School of Business, Department of Management Science and Information Systems, Oklahoma State University, Tulsa, OK 74106, USA

<sup>c</sup> Stillwater Medical Center, Stillwater, OK 74074, USA

## a r t i c l e i n f o

Article history: Received 12 June 2009 Received in revised form 12 January 2010 Accepted 20 January 2010 Available online 28 January 2010

Keywords: RFID Reader placement Criticality index Healthcare Asset tracking Genetic algorithms

## a b s t r a c t

The purpose of this research is to provide decision makers with a methodology to optimize the design of a medical-asset tracking system constrained by a limited number of RFID readers. Using an enhanced formulation of the maximal covering location problem along with a new criticality index analysis metric (derived from the severity, frequency and dwell time of the critical medical assets) the optimal placement of the limited number of RFID readers is determined. The proposed methodology is implemented in a healthcare facility where the RFID system coverage has improved by 72% compared to the currently utilized expert/heuristic-based placement strategy.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

Effective and ef<sup>fi</sup>cient tracking of medical assets in healthcare facilities could be achieved by means of Radio Frequency Identi<sup>fi</sup>cation (RFID) system implementation. However, RFID systems are fairly new, complex, and often prohibitively costly to implement. Therefore, most of the time adequate number of RFID readers are not obtained and properly placed in these facilities for appropriate coverage. Due to the managerial as well as cost related constraints, the number of readers may also be <sup>fi</sup>xed and hence cannot be increased to improve the system performance (size of the total coverage <sup>fi</sup>eld). In such a scenario, the best way to make use of the current system would be to optimize the RFID reader placement. This research proposes a methodology based on a maximal covering location optimization for optimal placement of limited number of RFID readers. The proposed methodology is validated in an actual healthcare facility where a signi<sup>fi</sup>cant increase in the RFID system coverage performance was observed.

## 1.1. Motivation

Recently the importance of the service industry has increased considerably as the economies in developed countries have expanded towards a service orientation while gradually shrinking on the manufacturing base [13]. Among all service industries, the healthcare sector is perceived to be the fastest growing and the most critical due to the fact that it deals with human life and any de<sup>fi</sup>ciency in this sector can cause inevitable and incurable results [10]. Because of the unpredictable service demand and the complex infrastructure of hospitals, quickly locating the critical assets (which ironically have high utilization numbers) has been one of the perpetual problems in the healthcare service industry [14]. Consider the case where an intensive care unit (ICU) nurse is using an oxygen regulator with a stable patient and is called up to help in an emergency case. She would have to immediately go and take care of the patient in dire need rather than taking the oxygen regulator to its regular storage location. If a consecutive event occurs where the same asset (i.e., oxygen regulator) is needed, it would be hard for another nurse or doctor to locate it in a timely manner because it is not in its regular location, but in the ICU room where it was previously left. Therefore, real-time tracking and information sharing of medical assets emerges as a vital issue. Lack of proper tracking of these critical assets would result in poor service quality, low patient satisfaction, customer churn, loss of revenue and, more tragically, loss of the life of a patient [10].

Radio frequency identi<sup>fi</sup>cation (RFID) technology has risen to prominence among auto-ID technologies, which can provide the infrastructure enablement needed to maximize real-time tracking and information sharing of assets to improve underlying service systems [12]. RFID can be used to identify, track, sort and/or detect a wide variety of objects by means of radio frequency transmission using a wireless identi<sup>fi</sup>cation technology that communicates data by means of radio waves. Communication takes place between a reader (a.k.a. interrogator) and a transponder (a.k.a. a tag) where data is encoded in a chip embedded into the tag. Tags that are integrated with an antenna and packaged into a <sup>fi</sup>nished label can be either active (powered by a battery) or passive (powered by the reader <sup>fi</sup>eld) [11]. Because RFID does not require line-of-sight to identify an object and is capable of recognizing many objects at once, various <sup>fi</sup>elds have employed it. The top three fastest growing economic sectors (i.e., application areas) of RFID are predicted to be (a) retail services, (b) commercial services, and (c) healthcare services [26]. Furthermore, the increasing number of patents <sup>fi</sup>led on innovative uses of RFID in healthcare shows the importance and enormous potential of this technology [1,23,27]. Due to the aforementioned unpredictable and complex nature of healthcare facilities, currently more medical assets are af<sup>fi</sup>xed with RFID tags to be able to track their real-time locations and, hence, achieve real-time tracking and information sharing via the backend application of RFID systems.

## 1.2. RFID in healthcare service sector

The application areas for RFID technology in the healthcare service sector are growing exponentially, and a representative list would include door security, patient ID, inventory management, medical <sup>fi</sup>le management, pharmaceutical security, high-heat and sterilization, high accessibility, scalability, availability, error reduction at point of care, medications management, and real-time asset and employee tracking [8]. Among these different possible usages of RFID systems in healthcare, active tracking of critical assets that are shared resources is likely to become the mainstream area of RFID uses in medical settings [9,19,29]. Medical asset tracking with RFID has vital importance due to the complicated and unpredictable nature of healthcare facilities since the location of the assets change arbitrarily and continuously [20]. Therefore, tracking mobile and highly critical medical equipment has become a priority for healthcare system performance. Many hospitals lose equipment worth hundreds of thousands of dollars each year and also spend precious time searching for temporarily lost assets for patient care; these assets include medical devices (such as infusion pumps, portable X-ray machines and patient monitoring devices) as well as other mobile assets (such as wheelchairs, stretchers and gurneys) [25]. Without an asset tracking system, the central supply staff in a hospital may spend hours each day performing a “round-up” [13] of equipment, which is a time consuming manual search of every department for unused equipment or equipment that requires servicing [13]. Additionally, many high-value assets go underutilized while hospitals continue to overspend on additional assets (purchased or rented) in order to increase the timeliness of their services [25].

The healthcare community now sees tremendous bene<sup>fi</sup>ts in deploying RFID for item tracking (especially high-value mobile assets) and security along with maintaining the highest level of data integrity [21]. There are several obstacles in identifying and tracking objects and people within the hospital environment, which create dif<sup>fi</sup>culties in making real-time decisions [2] such as common usage of some assets by different departments, locating the assets in various local storages, locating healthcare providers, and following patients' recovery trends. In order to tackle these obstacles, Li et al. [16] proposed an integrated mobile healthcare service system to shorten the tracking time and increase the accuracy of positioning and identifying people with infection of SARS disease. Wu et al. [28] analyzed an RFID-based healthcare system that identi<sup>fi</sup>es the patient and compares drugs intake. This allows the healthcare providers to eradicate patient–drug mismatches, over dosages and drug errors. Booth et al. [3] pointed out other possible applications in the location of staff and patients, theft prevention, patient safety, incident audit trail, dynamic patient–equipment association, equipment status, and cost capture. Østbye et al. [20] speci<sup>fi</sup>cally focused on a study that analyzes whether an RFID-based infrared system would increase equipment utilization and decrease personnel time spent on searching for the assets in a hospital. This study revealed that the proposed

RFID-infrared integrated system improved the current control system's accuracy to detect various types of medical equipments in the healthcare facility where the case study was held.

By optimally placing RFID readers throughout the hospital, the search time for critical assets can be minimized and also fewer staff would be needed to perform the round-ups. Additionally, such a system enables a faster response to patient needs as equipment locations are known and are accessed more rapidly [13]. Thus, in emergency situations, RFID systems enable nurses to spend less time searching for equipment, while preventing materials managers from ordering excess amount of equipment [18]. Therefore, having an RFIDbased asset tracking system in hospital settings is proven to be costeffective and economically justi<sup>fi</sup>able [4].

An important issue in the design of RFID systems is the placement of readers to achieve optimal system performance [4]. Guan et al. [7] conducted a study to identify optimum reader placement. The objective was to minimize the number of readers with the constraint that all RTPs (read test points in sensor <sup>fi</sup>eld) should be covered and the interference level should be minimized. Similarly, Chakrabarty et al. [4] has also approached the same problem but from a slightly different direction; evaluating different types of readers, their objective was to identify the best combination of these reader types along with their required quantities to satisfy the objective of best possible sensor coverage.

## 1.3. Proposed method

The related research section reveals that there is a vacancy in literature to overcome the case where the RFID system has a <sup>fi</sup>xed number of readers (due to budget-related or other acquisition-related issues). Therefore, the main assumption in this research study is that the number of RFID readers cannot be increased and the available number of RFID readers is less than what would be needed for full coverage of the complete <sup>fi</sup>eld. Under such a scenario, rather than the minimization of the number of readers, the main optimization problem is to place scarce RFID readers so as to maximize the utility of the system (i.e., obtain the best sensor <sup>fi</sup>eld coverage). In this paper, we propose a methodology to handle such a case.

Maximal covering location problem [22] is shown to be an effective approach to solving this type of location speci<sup>fi</sup>cation problems. Therefore, this paper focuses on optimal RFID reader placement to track crucial assets using an improved maximal covering location problem. The enhancement is achieved with a criticality index analysis and the system is implemented and tested at a healthcare facility. Crucial assets can be de<sup>fi</sup>ned as expensive resources which are less in quantity. In case of emergency, it is vital for healthcare staff to easily and quickly locate them to avoid any serious harm to the patients or cause of deaths.

Fig. 1 summarizes the general framework of the proposed methodology. Given the speci<sup>fi</sup>cation of the problem as inputs (i.e., hospital <sup>fl</sup>oor plan, number of RFID readers and their read ranges, and expert knowledge), <sup>fi</sup>rst, a severity analysis of the critical assets is to be performed. The severity analysis is performed using a knowledge acquisition method where a survey (including questions with a <sup>fi</sup>vepoint Likert scale [17]) is conducted with the medical experts to incorporate their knowledge/information about the importance/ urgency level of the medical assets in a variety of medical settings. Then, the whole <sup>fl</sup>oor plan of the healthcare facility is to be divided into squares as a representation of grid points. By performing the frequency and dwell time analyses for each square and combining them with severity analysis, the criticality index of each square is to be determined. At this point, an optimization model based on a modi<sup>fi</sup>ed extension of MCLP is to be formulated. Since the complexity of the problem is high due to the large number of alternatives/combinations to evaluate, there needs to be a meta-heuristic approach (e.g., genetic algorithm (GA) or simulated annealing) to solve this problem. By the utilization of a colored map of grid points, the initial solutions for the GA algorithm are generated, and subsequently (through an iterative process) the “optimal” solution to the RFID reader locations is obtained. Since GA is a heuristic, the optimal solution is not really the global optimum, rather, a good enough solution under the terminating conditions.

![](/api/attachments/E74CUPZM/fulltext/images/77e01c63029a606d3893f8fa24025857a4e743869acd34199191b26860efa490.jpg)  
Fig. 1. The process <sup>fl</sup>ow of the proposed method.

The rest of the paper is organized as follows. Section 2 presents the proposed optimization model for the RFID reader placement problem. Section 3 provides a case study (an actual implementation at a healthcare facility) to validate the proposed methodology. Therein a comparison of the proposed methodology with the existing heuristic method is also provided. Finally, Section 4 summarizes the <sup>fi</sup>ndings and provides some concluding remarks.

## 2. A methodology for RFID network designs in healthcare facilities

## 2.1. Objective function and constraints

The <sup>fi</sup>rst step in our proposed method is to divide the whole <sup>fl</sup>oor plan into small squares as seen in Fig. 2. The <sup>fl</sup>oor can be considered as a grid that contains n squares, commonly called demand squares (DS) in a generic MCLP problem.

As seen in Fig. 3, a reader node $" \mathrm { A } "$ in the circle is de<sup>fi</sup>ned as a candidate place for the RFID reader which covers its surrounding demand squares based on its radius of reader range (RRR). Four demand squares are represented in Fig. 3, as a representative example. However, by dividing the <sup>fl</sup>oor plan into a different number of demand squares and considering various read ranges of RFID readers, the coverage of a reader node may vary. Here, there is a loss of information that stems from the fact that the <sup>fl</sup>oor plan is divided into square grids whereas the RFID reader coverage is de<sup>fi</sup>ned as a circular area. However, according to our calculations, this loss was not found to be very signi<sup>fi</sup>cant and hence is ignored in the modeling. In order to evaluate the reader coverage achieved after positioning a reader on a particular reader node, it is necessary to evaluate the criticality index of the demand squares it covers. It is proposed here to evaluate the criticality index of these squares by integrating severity, frequency, and dwell time of all assets which visit that particular demand square.

The brief de<sup>fi</sup>nitions of these three terms are as follows:

Severity (s ) The importance level of asset k in emergency cases as evaluated by experts based on a <sup>fi</sup>ve-point Likert scale. Frequency (f ) Number of times asset k passes through demand square i in a day.

Dwell time ((d<sub>t</sub>)<sub>ki</sub>) Average of time that asset k spends in demand square i in a day.

The criticality index of demand square i which is represented by $c _ { i }$ is calculated using the following equation:

$$
c _ {i} = \sum_ {k = 1} ^ {L} f _ {k i} ^ {*} (d _ {\mathrm{t}}) _ {k i} ^ {*} s _ {k}\tag{1}
$$

where k is the type of assets; $f _ { k i }$ represents the frequency of asset k in square i per day; $( d _ { \mathrm { t } } ) _ { k i }$ indicates the dwell time of asset k spent in demand square i per day; and $s _ { k }$ indicates the severity of asset k.

![](/api/attachments/E74CUPZM/fulltext/images/409c767b8fbabf2fb6f6eb6ddeb26ebc03f2de2e854f4252b934034687176c8d.jpg)  
Fig. 2. A <sup>fl</sup>oor plan representation divided into grid of squares.

![](/api/attachments/E74CUPZM/fulltext/images/4a9b095b3b9cd295d66df9499f7363dd9bd2c8080449f003926702cdc36feafb.jpg)  
Fig. 3. Reader node and the demand squares it covers.

A greater criticality value of a demand square indicates (1) a higher frequency of assets visits that particular demand square (referring to frequency), (2) a larger amount of time spent in that demand square (referring to dwell time), and/or (3) the severer assets are being utilized/stored in this demand square (referring to severity of asset).

By considering Fig. 3, coverage of reader node A is given by the addition of the criticality indices of demand squares $\left( c _ { 1 } , c _ { 2 } , . . . , c _ { t } \right)$ that it can cover based on its read range; namely the coverage will be $A = c _ { 1 } + c _ { 2 } + c _ { 3 } + \cdots + c _ { t }$ under the assumption that one reader can cover t number of demand squares. For Fig. 3 particularly, this value would be $A = c _ { 1 } + c _ { 2 } + c _ { 3 } + c _ { 4 }$ where $c _ { 1 } , c _ { 2 } , c _ { 3 } ,$ and $c _ { 4 }$ refer to criticality values of demand squares (DS<sub>1</sub>, DS<sub>2</sub>, $D S _ { 3 } ,$ and $D S _ { 4 }$ , respectively). Reader coverage de<sup>fi</sup>ned by A is obviously desired to be increased. However, if there are excessive number of RFID readers, their coverage areas would collide, which is called reader collision/ interference. Reader collision problems mainly occur in a dense reader environment where several readers try to interrogate tags at the same time in the same vicinity [15]. In the case of reader collision, the reading results can be unsatisfactory with coinciding read times, multiple read instances, and undesirable data integrity problems.

Having a <sup>fi</sup>xed number of readers, p, our objective is to locate these p readers on m candidate reader nodes to maximize possible coverage on the service <sup>fl</sup>oor. To achieve this goal, the mathematical model is formulated as follows:

$$
\text { Max } w _ {1} \left(\sum_ {i = 1} ^ {n} c _ {i} * y _ {i}\right) - w _ {2} \left(\sum_ {i = 1} ^ {n} \left(\sum_ {j \in N _ {i}} x _ {j}\right) - y _ {i}\right).\tag{2}
$$

Subject to

$$
m ^ {*} y _ {i} \geq \sum_ {j \in N _ {i}} x _ {j} \geq y _ {i} \quad \text {   for   } i = \{1, 2,..., n \} \text {   where   } N _ {i} = \left\{j | l _ {i j} \leq s \right\}\tag{3}
$$

$$
\begin{array}{l l} \sum_ {j = 1} ^ {m} x _ {j} = p \\ x _ {j} = 0, 1 & j = \{1, 2,..., m \} \\ y _ {i} = 0, 1 & i = \{1, 2,..., n \} \end{array}\tag{4}
$$

As de<sup>fi</sup>ned by Eq. (1), c is the criticality index of each demand square in the grid; y is a binary variable whose value is $" 1 "$ if demand square i is covered by at least one reader and $" 0 "$ otherwise; n is the total number of demand squares and m is the total number of reader nodes (candidate places for readers); $x _ { j }$ is a binary decision variable whose value is $" 1 "$ if a reader is located at reader node $j ,$ and $" 0 "$ otherwise. Therefore, $y _ { i }$ is dependent on $x _ { j } . \ N _ { i }$ is the set of reader nodes (j) that can cover demand square i. The distance between these reader nodes and demand square $i \ ^ { \ast } l _ { i j } ^ { \ \ast }$ should be less than the read range of the reader $" s "$

The objective function of this model (Eq. (2)) is to identify the optimal location of available readers by: (1) maximizing total covered criticality indices of demand squares by $\begin{array} { r } { z _ { 1 } = \sum _ { i = 1 } ^ { n } c _ { i } y _ { i } } \end{array}$ and (2) minimizing the reader collision by $\begin{array} { r } { z _ { 2 } = \sum _ { i = 1 } ^ { n } { \bigl ( } \sum _ { j \in N _ { i } } x _ { j } { \bigr ) } - y _ { i } } \end{array}$ . The <sup>fi</sup>rst objective (z ) is straightforward. The rationale for the second objective $\left( z _ { 2 } \right)$ is as follows: If multiple readers cover the same demand square(s), reader collision will occur. In order to minimize this possibility of reader collision, $z _ { 2 }$ will force the model to assign only one reader for the same demand square to be covered. These two objectives are formulated as a multi-objective function in which the weights of these two objectives are represented by $w _ { 1 }$ and $w _ { 2 } ,$ respectively (Eq. (2)).

By having at least one reader on one of the elements of $\begin{array} { r } { N _ { i } \big ( \sum _ { j \in N _ { i } } x _ { j } \ge 1 \big ) } \end{array}$ , demand square i will be covered $( y _ { i } = 1 )$ . On the other hand, demand square i will be an uncovered square $( y _ { i } = 0 )$ , if there is no reader on $N _ { i }$ reader nodes $\textstyle ( \sum _ { j \in N _ { i } } x _ { j } = 0 )$ . This constraint is formulated by Eq. (3). The constraint indicating that the total number of available readers is <sup>fi</sup>xed at p is represented by Eq. (4). Fig. 4 illustrates the schematic representation of the optimization model.

## 2.2. Implementation of the proposed methodology by genetic algorithms

When there is a large number of demand nodes in the model, the total number of constraints increases drastically. Therefore, the proposed method can be classi<sup>fi</sup>ed as an NP-complete (or NP-hard) problem. It is not possible to <sup>fi</sup>nd the global optimum solution of this problem using deterministic approaches (i.e., linear modeling). Hence, it is necessary to implement a meta-heuristic algorithm to overcome this issue and provide a suboptimal satisfying solution [24]. In this study, a genetic algorithm (GA) method is utilized. GA is a stochastic global search method which is a nature-inspired algorithm based on the process of natural biological evolution and is used to solve optimization problems [6]. The overall procedure using GA is illustrated in Fig. 5.

![](/api/attachments/E74CUPZM/fulltext/images/3fc2f452b2545db541d0cb53ad8158c3c651551e1d7866cbbec7370db51a6690.jpg)  
Fig. 4. Schematic representation of optimization model.

![](/api/attachments/E74CUPZM/fulltext/images/2ef08aa4f939aeccdc19174d2d24832250b14c4811bbff04909ae56f7905dc3c.jpg)  
Fig. 5. Genetic algorithm-based solution development process.

The <sup>fi</sup>tness function of the GA algorithm is given by Eq. (2). Each chromosome consists of p genes where genes represent the places where the readers are to be allocated. Therefore, each chromosome represents a solution set which exhibits the places of the readers in the service <sup>fl</sup>oor. After representing the solution in terms of a chromosome consisting of p number of genes, the initial population of solutions is randomly generated. After evaluating the <sup>fi</sup>tness of each potential solution in the population, the chromosomes are ranked based on their <sup>fi</sup>tness values. The ones with the best values are migrated to the next generation of solutions and the remaining better ones are given higher probability to be used as parents of the subsequent populations. During the reproduction process, the randomly selected parents are pushed through the mutation and crossover operations. In deciding whether to perform a mutation and/ or a crossover, two common variables are utilized: P (probability of doing crossover) and $P _ { \mathbf { M } }$ (probability of doing mutation). These variables are evaluated using a random number generator. Parents that take part in the mutation and the crossover are randomly selected, giving higher possibility to the ones with better <sup>fi</sup>tness values. The graphical representation of reproduction operators is shown in Figs. 6 and 7. In Fig. 6; numbers 90, 101, 20, 14, and 32 represent the places of the reader nodes. For crossover, two parents are selected randomly. As shown in Fig. 7, the crossover is performed using the one-point crossover method [5].

## 3. Case study

To validate the proposed methodology, a case study was performed at Stillwater Medical Center (SMC).

## 3.1. Introduction of the healthcare facility

SMC had an RFID system in place for three years to track the location of the certain medical assets. The assets which were important and/or dif<sup>fi</sup>cult to <sup>fi</sup>nd were af<sup>fi</sup>xed with active RFID tags so that in emergency situations these assets could be located quickly. However, SMC still faced problems with the ability to locate those assets on time. The reason for this was twofold: (1) There was limited number of RFID readers so full coverage of the <sup>fl</sup>oor cannot be achieved, and (2) The locations of these readers were not optimally determined. The readers were placed based on the experiences and estimation of the healthcare providers in SMC. The proposed methodology was used to maximize the coverage of the RFID system with this <sup>fi</sup>xed number of readers.

To demonstrate our proposed method, the third <sup>fl</sup>oor of SMC (which was the busiest <sup>fl</sup>oor in the medical center) was used in the case study. As illustrated in Fig. 8, there were three departments on this <sup>fl</sup>oor: (1) Intensive Care Unit (ICU), (2) Respiratory, and (3) Nursing. The assets were stored in various storage places according to convenience and/or usage pro<sup>fi</sup>les of those assets. Knowing the location of these storage places was necessary for conducting the frequency and dwell time analyses.

## 3.2. RFID tracking system in use

The RFID system being used by SMC was provided by WhereNet Corporation®. The system consisted of the following components: (1) whereport, (2) location sensor, (3) backend application, and (4) tags.

## 3.2.1. Whereports

In this system RFID readers are called as whereports. When a tag is in the read range of a whereport, the tag is sensed and located by the whereport. The whereport creates a spherical magnetic <sup>fi</sup>eld which interrogates the tag(s) within its sensing <sup>fi</sup>eld. Typical read range at various positions with the combination of power requirement and power level settings are given in Table 1. In general, the wider the read range, the greater the required power. The usual practice is to keep the power range at level 4 which gives spherical read range of 7 ft.

## 3.2.2. Location sensors

Location sensors are the devices which receive the signal from the whereports and then transmit it to the backend application. These sensors communicate with the whereports in their surrounding area.

![](/api/attachments/E74CUPZM/fulltext/images/9b6d6f5cc996da2f38ad9686b464bb0fb0d46cf32557222d68bc518d03405260.jpg)  
Fig. 6. A sample representation of mutation process.

![](/api/attachments/E74CUPZM/fulltext/images/1115190ab065fc59e80cb31a9c879921d934e1fa3576b53f19c5b9e2ced0d8cc.jpg)  
Fig. 7. A sample representation of crossover process.

The real-time locating system (RTLS) operates on 2.4 GHz RF, and the location sensor read range is approximately 350 ft.

## 3.2.3. Tags

The system uses active RFID tags. The positioning of these tags is such that they are unobstructed in relation to whereports at all directions. This enhances the signal exchange between the whereport and the tag.

## 3.2.4. Backend application

The system uses a GE IntelliMotion® backend database for recording tracking occurrences. This system is mainly used for collecting the data in real-time and visualizing the location of an asset at the time of need.

The present sensor distribution and coverage offered by these sensors are illustrated in Fig. 9. Since the location sensor offers coverage of about 350 ft in radius, whereas the whereports offer coverage of about 7 ft, the main problem of low RFID system performance stems from the poor positioning of the whereports rather than the location sensors.

## 3.3. Implementation of the RFID network design methodology

## 3.3.1. Severity analysis of assets

SMC had a number of medical assets which were insuf<sup>fi</sup>cient in quantity, but in emergency situations it was important to locate them in a timely manner. These assets were already af<sup>fi</sup>xed with active RFID tags and all assets that were used on the third floor are listed in Table 2. A survey was conducted with various departments regarding the importance of each asset as de<sup>fi</sup>ned in Section 2.1. The severity value indicates the degree of importance it has in helping rescue the life of a patient, which translates to the degree of importance placed on the ability to locate the asset in a timely manner. A <sup>fi</sup>ve-point Likert scale, ranging from extremely important (=5) to mildly important (=1) (representing a descending order of importance level) was utilized in acquiring the expert opinions. The severity values for all assets evaluated by the SMC healthcare providers are summarized in Table 2. It also tabulates the number of assets used on the third <sup>fl</sup>oor of SMC. A change in these numbers would de<sup>fi</sup>nitely affect the efforts spent in the time and motion analyses steps although they would not affect the computational complexity and scalability of our method. The only parameters affecting computational complexity and scalability are RFID reader range and grid points of the <sup>fl</sup>oors (demand squares).

## 3.3.2. Frequency and dwell time analyses

A time and motion study was conducted for the assets on the third <sup>fl</sup>oor to identify the path that each asset follows and the frequency of it passing through this path per day. These values were assigned as the frequency value, f , number of times asset k passes through demand square i per day. Using a similar method to the frequency analysis, the dwell times for each asset was also obtained. The dwell time was calculated as the time that an asset spends in a demand square for a day.

## 3.3.3. Criticality index analysis and initial solution for GA

The criticality index of each demand square was calculated by Eq. (1). Fig. 10 is the diagram of the third <sup>fl</sup>oor which shows different criticality index values of the demand squares with different colors, for example, red (dark-gray in black and white printing) corresponding to the highest criticality value and blue (light-gray in black and white printing) to the lowest. Since there were four readers to be used for this <sup>fl</sup>oor, the initial GA solution of the reader placement is also indicated in the colored map by the four circles (see Fig. 10).

![](/api/attachments/E74CUPZM/fulltext/images/ad556b05f2dc9eecf93bfdf40cc947591b204af4be891c9316f706ac62732cfd.jpg)  
Fig. 8. Plan for the third <sup>fl</sup>oor of SMC with its departments

Table 1  
Various ranges of whereports.

<table><tr><td>Power level setting</td><td>Any orientation range</td><td>Good orientation range</td><td>Release range</td></tr><tr><td>1</td><td>3.5</td><td>4</td><td>6</td></tr><tr><td>2</td><td>5</td><td>6</td><td>9</td></tr><tr><td>3</td><td>6</td><td>7</td><td>11</td></tr><tr><td>4</td><td>7</td><td>8</td><td>13</td></tr><tr><td>5</td><td>8</td><td>9</td><td>15</td></tr><tr><td>6</td><td>9</td><td>10</td><td>17</td></tr><tr><td>7</td><td>13</td><td>16</td><td>24</td></tr><tr><td>8</td><td>15</td><td>20</td><td>30</td></tr></table>

A careful analysis of the colored map revealed that nodes in blue zones could potentially be eliminated since the criticality index values of these nodes are the lowest (making them unlikely candidates for reader placement location). An example of this elimination procedure is graphically represented in Fig. 11.

## 3.4. Results of the case study

After implementing the proposed methodology by using 100 replications with different population sizes and selection probabilities for the GA algorithm, the best solution is obtained and summarized in Table 3. In this case study, the weights in Eq. (2) are set as equal for both objectives (z and z ). The current locations of the readers provided 14% coverage of the demand squares and are represented in Fig. 10 with circles. The implementation of our methodology improved this performance metric to 24.05% and the proposed locations of the RFID readers are marked with circles in Fig. 12. The results as well as the RFID reader locations are compared in Table 3. The maximum coverage of the system proposed by our methodology provided 72% more coverage than the existing heuristic placement of the readers by assigning the four readers to nodes 72, 145, 137, 169, which validates the viability of the proposed method.

Table 2  
List of critical asset with owning departments and severity values.

<table><tr><td>Name of the asset</td><td>Owning department(s)</td><td>Severity values</td><td>Number of the asset in system</td></tr><tr><td>Bed warmer</td><td>ICU</td><td>1.50</td><td>2</td></tr><tr><td>CPM machine</td><td>ICU</td><td>2.67</td><td>6</td></tr><tr><td>Doppler</td><td>ICU</td><td>2.33</td><td>2</td></tr><tr><td>ECG/EKG machine</td><td>ICU</td><td>2.42</td><td>1</td></tr><tr><td>Heat therapy pump</td><td>Nursing</td><td>2.00</td><td>1</td></tr><tr><td> $O_2$  regulator</td><td>ICU, respiratory, nursing</td><td>5.00</td><td>47</td></tr><tr><td>PCA pump</td><td>ICU, nursing</td><td>3.67</td><td>21</td></tr><tr><td>Sequential compression pump</td><td>ICU, nursing</td><td>3.00</td><td>39</td></tr><tr><td>Vital sound monitor</td><td>ICU</td><td>2.33</td><td>7</td></tr><tr><td>Bi-PAP</td><td>Respiratory</td><td>2.58</td><td>4</td></tr><tr><td>Wheelchair</td><td>ICU, respiratory, nursing</td><td>3.83</td><td>43</td></tr><tr><td>Ventilator</td><td>Respiratory</td><td>1.67</td><td>5</td></tr><tr><td>Continuous pulse oxymetry (CPO)</td><td>Respiratory</td><td>3.67</td><td>19</td></tr><tr><td>IV pumps</td><td>ICU</td><td>2.67</td><td>21</td></tr><tr><td>Entreal feeding pump</td><td>ICU</td><td>2.00</td><td>2</td></tr><tr><td>Misttent</td><td>Respiratory</td><td>1.67</td><td>5</td></tr><tr><td> $O_2$  cylinder</td><td>ICU, respiratory, nursing</td><td>4.87</td><td>54</td></tr></table>

In the <sup>fi</sup>rst sight, the performance of the proposed method could be perceived unsatisfactory with only 24.05% coverage. However, taking into account the fact that SMC currently has only four RFID readers (as shown with circles in Figs. 10 and 12) and the third <sup>fl</sup>oor of SMC is a rather large area inhabited with a large number of critical assets, the increase in the reader coverage (from 14% to 24.05%) is actually quite signi<sup>fi</sup>cant. The SMC decision makers agreed with this fact and decided to apply our solution to achieve more timeliness on tracking the critical assets.

Using the case study settings, we also investigated how the RFID reader placement and corresponding coverage levels would change if we change the de<sup>fi</sup>nition of the criticality index. Since different preferences may result in different de<sup>fi</sup>nitions of the criticality index, (for example, one might choose to use only the frequency as the determinative parameter of the criticality index, instead of the combination of severity, frequency, and dwell time), it would be a worthy effort to see how sensitive the placement and coverage of the readers are to these different de<sup>fi</sup>nitions of the index. The results of all feasible de<sup>fi</sup>nitions of the criticality index along with the current sensor <sup>fi</sup>eld coverage of the RFID readers are summarized in Table 4.

![](/api/attachments/E74CUPZM/fulltext/images/03e02a0fd4ff0d75bad1bdb66648272ca3f2c1af69256454a2fcf758d1994d41.jpg)  
Fig. 9. Present whereport and location sensor placement in SMC.

![](/api/attachments/E74CUPZM/fulltext/images/53fa2f9383a129f0cdcd737e570e073776e66e7f7c55ed4521d63aa58e02fd87.jpg)  
Fig. 10. Current placement of RFID readers (marked with white circles) in SMC.

As shown in Table 4, in addition to the Eq. (1), <sup>fi</sup>ve other possible ways to de<sup>fi</sup>ne criticality index values are explored: (1) frequency only, (2) dwell time only, (3) both dwell time and severity values, (4) both frequency and severity value, and (5) both frequency and dwell time.

Based on the results presented in Table 4, our proposed RFID network design method outperforms the current heuristic placement of the RFID readers in all possible de<sup>fi</sup>nitions of the criticality index. Improvements on the coverage of the sensor <sup>fi</sup>eld are observed for all different types of the criticality index de<sup>fi</sup>nitions. In particular, the improvement seems to be most (87%) when the criticality index is de<sup>fi</sup>ned as the combination of frequency and dwell time of the assets $\begin{array} { r } { ( c _ { i } = \sum _ { k } ^ { L } ) _ { i } \dag , , } \end{array}$ . Also the consideration of only frequency gave <sup>ð Þ Þ</sup>a high improvement with 81%. Both of these de<sup>fi</sup>nitions in fact rely on the assumption that all the assets have the same severity value because they do not incorporate this parameter (s ). However, for our case study this assumption and in turn these de<sup>fi</sup>nitions of criticality index are not acceptable since the severity values for each medical asset are considerably varying as shown in Table 2. Yet, these de<sup>fi</sup>nitions may be useful for other RFID settings where the assumption (that all assets are equally important) holds.

Table 3  
Summary results of the case study

<table><tr><td>Comparison</td><td>Node 1</td><td>Node 2</td><td>Node 3</td><td>Node 4</td><td>Coverage</td></tr><tr><td>Current system solution</td><td>72</td><td>145</td><td>107</td><td>73</td><td>14.00%</td></tr><tr><td>Proposed method solution</td><td>72</td><td>145</td><td>137</td><td>169</td><td>24.05%</td></tr></table>

## 4. Summary and conclusion

In this paper, we provided a detailed description of a decision support system aimed to maximize the sensor <sup>fi</sup>eld coverage by optimally placing the <sup>fi</sup>xed number of RFID readers. The underlying methodology utilizes a new parameter called criticality index to better evaluate the demand squares to determine the optimal location of the readers for maximum coverage of the service <sup>fl</sup>oor. The methodology is validated by a case study at a healthcare facility. The case study results showed that compared to the existing heuristic placement of the RFID readers, the proposed methodology improved the coverage of RFID readers on the hospital <sup>fl</sup>oor by 72%. For the cases where the number of readers are <sup>fi</sup>xed for some reason (such as limited budget for the RFID system deployment) and the service area is larger than what can be covered with the limited number of readers, the proposed methodology can be used to optimize the reader placement location and hence maximize the sensor <sup>fi</sup>eld coverage.

There are two noteworthy points in the study: (1) although the proposed modi<sup>fi</sup>ed MCLP-based methodology is validated with only four RFID readers in the case study section, the problem can be applied to any number of readers. This would only require changing the parameter p in Eq. (4). The case study was focused on only four readers to prove that there is an improvement in the RFID reader coverage compared to the current RFID setting of the healthcare facility on hand. (2) Given that the required parameters in Section 2.1 can be obtained, the proposed methodology can be implemented in any RFID-related setting (e.g. production systems, retail shop <sup>fl</sup>oors, security areas, etc.). In this study, it is illustrated through a medical asset tracking example, but the methodology can be generalized to different asset tracking systems that utilize an RFID system. This is feasible because the construction of the criticality index in Eq. (1) provides a comprehensive representation, making the underlying methodology adaptable to other RFID-related tracking systems.

![](/api/attachments/E74CUPZM/fulltext/images/880e65f03a07872ae64d2387ff2650c4664a98e8be9fad50e9de52c26615fe26.jpg)  
Fig. 11. Eliminating reader nodes with low criticality index values.

![](/api/attachments/E74CUPZM/fulltext/images/8e152fbd58eaabd8f2337d223c4255790b00b66a3a126826faedc99d357a426f.jpg)  
Fig. 12. Colored zones of <sup>fl</sup>oor plan indicating the criticality of each demand square.

Although the case study results are promising and validate the viability of the proposed decision support system, the study is not without limitations. It has a strong assumption that the number of RFID readers is <sup>fi</sup>xed due to some managerial reasons (e.g. budget constraints). The authors are in preparation of an extended methodology which would relax this assumption. The new methodology would address the scenarios where the number of readers can be increased to achieve full (100%) sensor <sup>fi</sup>eld coverage with the minimum possible number of readers. This extended methodology is intended to utilize the local set covering problem (LSCP) where the main objective is to minimize the cost of achieving a speci<sup>fi</sup>ed level of coverage for a given service <sup>fl</sup>oor layout with an arbitrary list of critical assets. Such a solution would provide the decision makers with the information of how many RFID readers (a mix of readers with varying read ranges) are needed at minimum to guarantee a certain level of coverage (up to 100%). Additionally, future directions of this research effort include adding other critical resources such as doctors and nurses to the mix of “assets” that need to be tracked/located in a timely manner at the time of emergency in a healthcare system. These extensions to the proposed methodology aim to <sup>fi</sup>nd the optimal number of RFID readers and their optimal placement subject to the desired level of system coverage, minimum reader collision, a given set of critical assets and a given speci<sup>fi</sup>cation of the service <sup>fl</sup>oor layout. Another interesting point of future research is to conduct a stability analysis for the model parameters. For instance, the recalculation of the severity value (as evaluated by the experts) may be of interest if the demand is dynamic throughout a working day. This analysis would be helpful especially if the RFID readers are portable and can be moved easily from one location to another within the same day. Additionally, the level of the business of a unit might be further analyzed in depth to see whether or not it affects the RFID reader locations as a critical factor. This would particularly have a great importance for the retails shop <sup>fl</sup>oors where various departments have the same assets being tracked but the number of customers they serve are far different than each other.

Table 4  
De<sup>fi</sup>nition of criticality index against coverage performance.

<table><tr><td>Sensor field coverageDefinition of criticality index</td><td>Current placement</td><td>Proposed method</td><td>Improvement</td></tr><tr><td> $c_{i} = \sum_{k=1}^{L} f_{ki}$ </td><td>12.9%</td><td>23.3%</td><td>81%</td></tr><tr><td> $c_{i} = \sum_{k=1}^{L} (d_{t})_{ki}$ </td><td>5.4%</td><td>7.5%</td><td>38%</td></tr><tr><td> $c_{i} = \sum_{k=1}^{L} (d_{t})_{ki} * s_{k}$ </td><td>10%</td><td>14.9%</td><td>49%</td></tr><tr><td> $c_{i} = \sum_{k=1}^{L} f_{ki} * s_{k}$ </td><td>9.8%</td><td>14.6%</td><td>49%</td></tr><tr><td> $c_{i} = \sum_{k=1}^{L} f_{ki} * (d_{t})_{ki}$ </td><td>12.6%</td><td>23.5%</td><td>87%</td></tr></table>

We can state that this study would ease the efforts of the managers to handle the strong constraints of their <sup>fi</sup>rms/companies. If the cost is the topmost severe constraint for an RFID-related setting, the managers would be willing to use our methodology to optimize the coverage of the <sup>fi</sup>xed number of RFID readers. In terms of the research implications, the study is the foremost one which incorporates GAbased maximal covering location problem into RFID implementations for a more ef<sup>fi</sup>cient asset tracking system.

## Acknowledgement

The authors gratefully acknowledge the support and help of all Stillwater Medical Center staff, especially Monica Redekopp, RN PhD, Director of Medical/Surgical Nursing Units; Elaine Ackerson, RN, Director of the Emergency Department and the Intensive Care Unit; Patricia Decker, CRT RCP, Supervisor of Respiratory Care; Chris Roark, Chief Information Of<sup>fi</sup>cer; Kathy Blasier, Director of Materials Management; Steven Taylor, CHFM CHSP, Director of Facilities; and Harold L. Duryea, GE Healthcare Site Manager.

## References

[1] C.O. Andreasson, J.C. Caputo, Systems and Methods for Tracking Pharmaceuticals within a Facility. U.S. Patent: 6935560 B2, dated Aug. 30, 2005.

[2] D. Avison, T. Young, Time to rethink health care and ICT? Communications of the ACM 50 (6) (2007) 69–74.

[3] P. Booth, P.H. Frisch, S. Miodownik, Application of RFID in an integrated healthcare environment, Proceedings of the 28th IEEE EMBS Annual International Confer ence, New York City, USA, 2006, pp. 117–120.

[4] K. Chakrabarty, S.S. Iyengar, H. Qi, E. Cho, Grid coverage for surveillance and target location in distributed sensor networks, IEEE Transactions on Computers 51 (2002) 1448–1453.

[5] H. de Garis, Genetic programming: building nanobrains with genetically programmed neural network modules, Proceedings of the International Joint Conference on Neural Networks, San Diego, CA, USA, 1990, pp. 511–516.

[6] D.E. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning Addison-Wesley Longman Publishing Co. Inc., Boston, MA, USA, 1989.

[7] Q. Guan, Y. Liu, Y. Yang, W. Yu, Genetic Approach for Network Planning in the RFID systems, Proceedings of the Sixth International Conference on Intelligent System Design and Applications, 2006, pp. 567–572.

[8] IBM, RFID: Real Solutions for Healthcare [online] (2005). Available from: https:// www-304.ibm.com/jct03004c/easyaccess/<sup>fi</sup>leserve?contentid=74696 [Accessed May 25th 2009].

[9] iSavent. Your gateway to RFID, GPS and Telemetric Information [online] (2006). Available from: http://site02.isavent.com/pdf/iSavent%20Products%20-%20iDiscovery. pdf [Accessed May 25th 2009].

[10] B. Kaplan, The medical computing “lag”: perceptions of barriers to the application of computers to medicine, International Journal of Technology Assessment in Health Care 3 (1987) 123–126.

[11] R. Krobn, RFID: it's about more than asset tracking, Journal of Healthcare Information Management 19 (2005) 20–23.

[12] Laran RFID, A Basic Introduction to RFID and its Use in the Supply Chain [online] (2004). Available from: http://www.ship2save.com/page\_images/wp\_printronix\_ rfid supplychain pdf [Accessed May 25th 2009].

[13] L.S. Lee, K.D. Fiedler, J.S. Smith, Radio frequency identi<sup>fi</sup>cation (RFID) implementation in the service sector: a customer-facing diffusion model International Journal of Production Economics 112 (2008) 587–600.

[14] S.H. Lee, A.W. Ng, K. Zhang, The quest to improve Chinese healthcare: some fundamental issues, International Journal of Health Care Quality Assurance 20 (2007) 416–428.

[15] K.S. Leong, M. Leng, The Reader Collision Problem in RFID Systems, IEEE International Symposium on Microwave, Antenna, Propagation, and EMC Technologies for Wireless Communications, Beijing, China, 2005, pp. 658–661.

[16] C.J. Li, L. Liu, S.Z. Chen, C.C. Wu, C.H. Huang, X.M. Chen, Mobile Healthcare Service System Using RFID, Proceedings of IEEE International Conference on Networking, Sensing & Control Taipei, Taiwan, 2004, pp. 1014–1019.

[17] R. Likert, A technique for the measurement of attitudes, Archives of Psychology 22 (1932) 1–55.

[18] E.W.T. Ngai, F. Riggins, RFID: technology, applications, and impact on business operations, International Journal of Production Economics 112 (2008) 507–509.

[19] E.W.T. Ngai, T.C.E. Cheng, S. Au, K. Lai, Mobile commerce integrated with RFID technology in a container depot, Decision Support Systems 43 (2007) 62–76.

[20] T. Østbye, D.F. Lobach, D. Cheesborough, A.M.M. Lee, K.M. Krause, V. Hasselblad, D. Bright, Evaluation of an infrared/radiofrequency equipment-tracking system in a tertiary care hospital, Journal of Medical Systems 27 (2003) 367–380.

[21] E. Paul, Reengineering medication management from the bedside using barcoding and wireless technology, HIMSS Publication 1 (2004) 61–69.

[22] S. Rahman, D.K. Smith, Use of location–allocation models in health service development planning in developing nations, European Journal of Operational Research 123 (2000) 437–452.

[23] M.E. Rodgers, 2007. Methods and Systems for Monitoring Quality and Performance at a Healthcare Facility. US. Patent: 2007/0162304 A1 dated Jul, 12, 2007

[24] E. Turban, J.E. Aronson, T.P. Liang, R. Sharda, Decision Support and Business Intelligence Systems, Pearson Prentice Hall, New Jersey, USA, 2007.

[25] S.F. Tzeng, W.H. Chen, F.Y. Pai, Evaluating the business value of RFID: evidence from <sup>fi</sup>ve case studies, International Journal of Production Economics 112 (2008) 601–613.

[26] U. Varshney, Pervasive Healthcare Computing: EMR/EHR, Wireless and Health Monitoring, Springer Science and Business Media, New York, NY, 2009.

[27] B. Walczyk, N. Patel, L. Hobby and J. Burgess. Monitoring People, Objects, and Information Using Radio Frequency Identi<sup>fi</sup>cation. U.S. Patent: 2006/0006999 A1, dated Jan. 12, 2006.

[28] F. Wu, F. Kuo, L.W. Liu, The Application of RFID on Drug Safety of Inpatient Nursing Healthcare, ACM International Conference Proceeding Series, 2005, pp. 85–92.

[29] Y.J. Tu, W. Zhou, S. Piramuthu, Identifying RFID-embedded objects in pervasive healthcare applications, Decision Support Systems 46 (2009) 586–593.

Mr. Asil Oztekin received his B.S. and M.S. degrees in Industrial Engineering from Yildiz Technical University (Istanbul, Turkey) in 2004 and Fatih University (Istanbul, Turkey) in 2006, respectively. During his M.S. studies, he worked as a graduate research assistant in the Usability Lab, leading the efforts of the usability evaluation and improvement strategies for Web-based information systems and the e-learning environment. Currently he is working towards a Ph.D. degree as a graduate research and teaching assistant in the School of Industrial Engineering and Management at Oklahoma State University. His research interests include quality improvement in complex service and manufacturing systems, medical informatics, data mining and RFID applications in healthcare. Mr. Oztekin is a member of IIE, INFORMS and ASQ.

Mr. Foad Mahdavi Pajouh received his B.S. and M.S. degrees in Industrial Engineering from Sharif University of Technology (Tehran, Iran) in 2004 and Tarbiat Modares University (Tehran, Iran) in 2006, respectively. He worked for Khodro Investment Development Company in Iran as an Industrial Engineer and as a Project Manager for System Simulation for four years (2004–2007). Currently, he is pursuing his Ph.D. degree in the School of Industrial Engineering and Management at Oklahoma State University. His research interests include mathematical programming, combinatoria optimization, data mining and knowledge management

Dr. Dursun Delen is an Associate Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University (OSU). He received his Ph.D. in Industrial Engineering and Management from OSU in 1997. Prior to his appointment as an Assistant Professor at OSU in 2001, he worked for a privatelyowned research company, Knowledge Based Systems Inc., in College Station, Texas, as a research scientist for <sup>fi</sup>ve years, during which he led a number of decision support and other information systems related research projects funded by federal agencies such as DoD, NASA, NIST and DOE. His research has appeared in major journals including Decision Support Systems, Communications of the ACM, Computers and Operations Research, Computers in Industry, Journal of Production and Operations Management, Arti<sup>fi</sup>cial Intelligence in Medicine, Expert Systems with Applications, among others. He recently published a book “Advanced Data Mining Techniques” with Springer. He is an associate editor for the International Journal of RF Technologies: Research and Applications, and serves on the editorial boards of the Journal of Information and Knowledge Management, International Journal of Intelligent Information Technologies, International Journal of Service Sciences, and Journal of Emerging Technologies in Web Intelligence. His research interests are in decision support systems, expert systems, data and text mining, knowledge management, business intelligence and enterprise modeling.

Dr. Leva K. Swim is the Director of Strategic Performance at Stillwater Medical Center; is a Clinical Data Consultant for the INTEGRIS Heart Hospital; and is also an adjunct professor in the School of Industrial Engineering and Management at Oklahoma State University. Dr. Swim began her career in the healthcare <sup>fi</sup>eld in 1986 when she was employed by The University Hospitals in the Management Analysis Department. She has also worked for INTEGRIS Health System from 1995 to 2007 as the Director of Decision Support. Dr. Swim holds B.S. and M.S. degrees in Industrial Engineering and Management from Oklahoma State University, and a Ph.D. degree in industrial Engineering from University of Oklahoma. Prior to entering the healthcare <sup>fi</sup>eld, Dr. Swim worked for two years as a Network Services Supervisor for Southwestern Bell Telephone Company. Her research interests include data mining, enterprise information system development for decision support, human factors in information system design, engineering project management, and total quality management.
