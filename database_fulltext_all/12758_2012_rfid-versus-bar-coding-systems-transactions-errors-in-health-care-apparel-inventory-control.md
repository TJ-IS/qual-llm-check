---
otero_id: 12758
otero_key: "GNZGZE86"
title: "RFID versus bar-coding systems: Transactions errors in health care apparel inventory control"
authors: "Hau-Ling Chan; Tsan-Ming Choi; Chi-Leung Hui"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.08.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# RFID versus bar-coding systems: Transactions errors in health care apparel inventory control

Hau-Ling Chan, Tsan-Ming Choi ⁎, Chi-Leung Hui

Business Division, Institute of Textiles and Clothing, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong Special Administrative Region

## a r t i c l e i n f o

Article history: Received 2 September 2011 Received in revised form 27 March 2012 Accepted 11 August 2012 Available online 21 August 2012

Keywords: RFID Transactions errors Inventory control Health care apparel

## a b s t r a c t

In recent years, RFID technology has been a popular topic in inventory management. However, whether this technology is superior to the traditionally used systems such as bar-coding system is controversial. In fact, prior empirical studies have revealed that the (observed) successful read rate in real world RFID applications is just in between 60 and 70%. In this paper, motivated by this fact and the observed industrial practice of apparel control in health care organizations, we <sup>fi</sup>rst conduct an analytical study to reveal when RFID systems will outperform the bar-coding system (and vice versa) in terms of reduction of the amount of required safety stock. We then extend our analysis to a supply chain context which includes the upstream apparel-product supplier and the downstream health care organization. We analytically prove several important insights which include: (i) The ratios between the RFID and bar-coding systems' stock-taking costs and error variations will determine whether one system outperforms the other. (ii) No matter whether the health care organization changes its scanning system from bar-coding to RFID or from RFID to bar-coding, it will only bene<sup>fi</sup>t the health care organization but the supplier will suffer. (iii) A carefully designed surplus sharing contract can create a win–win situation under which both the supplier and the health care organization will have improvement (in cost or pro<sup>fi</sup>t) with the change of the scanning system. Implications are discussed.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction and related literature

The industry of textiles and clothing (fashion) is characterized by short product lifecycles and highly uncertain market demand [2,8]. Different philosophies have been developed to cope with market uncertainty, for instance, just-in-time inventory systems and ef<sup>fi</sup>cient consumer response programs [26]. Success for many fashion companies hence relies on effective and ef<sup>fi</sup>cient supply chain management scheme. Among various technological advances, RFID system is a tool which has been generally believed to be bene<sup>fi</sup>cial to fashion supply chain management. RFID system's idea is based on the use of radio frequency as a way of transmitting information. RFID tag, which is an integrated circuit with an antenna, can be attached to any product and package. With wireless technologies, companies can easily keep track of the RFID tag without any physical contact. Inventory tracking becomes easier than ever and many other probable applications of RFID technologies, such as customized services for customer relationship management, have been proposed. In the fashion industry, it is well-agreed that the use of information is a crucial part of supply chain management [7]. It helps to alleviate challenges such as the bullwhip effect and achieve important policies such as accurate response [14], and quick response [6,8]. The establishments of RFID technologies are widely believed to provide ef<sup>fi</sup>cient and effective tools to facilitate information <sup>fl</sup>ow and inventory visibility along the fashion supply chains [17]. In light of the successful cases of RFID implementation for tracking and controlling clothing in apparel retailing such as Marks and Spencer (M&S) [10] and Gap Inc. [1], its application has spread over to the health care industry such as handling the pharmaceutical inventory [4], monitoring Alzheimer patients [11], and managing bottle gas delivery [27]. Recently, it has also been extended to manage the health care apparel products to improve operations ef-<sup>fi</sup>ciency, reduce health care apparel inventory level, and attain substantial saving. Following are three RFID deployments in the health care organizations that illustrate the impact on apparel inventory management, distribution, and work<sup>fl</sup>ow of medical staff.

In 2006, a Norwegian health care center, St. Olav's Hospital, implemented an RFID-based uniform-tracking system to replace traditional paper-based system to cope with more than 130,000 work garments in daily operations [29]. The employees use their hospital identi<sup>fi</sup>cation cards to access the uniform storage locker, and once they have taken away the uniforms and closed the door, an RFID reader will be activated to read, count and update the number of uniforms remaining inside the locker. Additionally, when the quantity of uniforms falls below the preset level, they will replenish the locker up to the desired level. Another RFID reader is attached to speci<sup>fi</sup>c bin which collects used uniforms for laundering. The interrogator transmits the data to the back-end software, regarding the garment IDs and time of those garments submitted to laundry. This system saves an estimated 40 million kroner in space savings for the removal of conveyor system and the hospital believes in big saving each year compared to the manual system through improving inventory accuracy and labor reductions. The RFID system not only enhances the real time visibility of staff gar ments within the hospital, but also associates the patients' garments for automated distribution across different hospital sites. Another promising RFID adoption occurred in Switzerland. Four Geneva-based university hospitals were merged to form the University Hospitals of Geneva (HUG) in 1995 [37]. HUG is now a large scaled hospital that offers both inpatient and outpatient services. Each patient's garment is sewn with an RFID tag which stores only the item ID and information related to laundry service. Interestingly, this RFID system is used to identify and match the tops with the bottoms of the patient/staff garments, as well as the whole set of garment with the corresponding site after laundering. The automated garment distribution provides 24 hours 7 days a week service to employees and smoothens the garment handling process of collection, ironing, redistribution across 4 sites with 7 distributors, and 28,000 garments allocation per week ef<sup>fi</sup> ciently. Besides, it monitors the number of times that a piece of garment has been washed for determining whether the garments ful<sup>fi</sup>lled the quality claimed by the suppliers. Furthermore, the hospital reduces the garment inventory level and saves up to 30% of the total garment expenditure. Apart from tracking the uniforms, a public hospital in Northern Germany, the Bielefeld City Clinic, launches trails to evaluate the feasibility of adopting RFID system to ensure that beds and mattresses can be cleaned appropriately, in a time and cost ef<sup>fi</sup>cient way [39]. Beds and mattresses are equipped with passive RFID tags to distinguish one from another. Nurses depend on the patient's illness level to determine the type of cleaning of the bed, for example, a completed disinfection is needed if a patient is suffered from highly infectious disease. This information is input to the hospital's bed management software so that the cleaning staff can clean the beds and mattresses according to the instructions recorded. Once the laundering is completed, the system is updated to indicate the types of cleaning performed and record the number of beds and mattresses available. The clinic is expected to acquire cost saving from a lower stock level of beds and mattresses and fewer working time of the staff.

It seems that both fashion and health care industries can achieve sustainable bene<sup>fi</sup>ts if RFID system is adopted to deal with the apparel products in their operations. However, regarding the business value of RFID systems, industrial reports, white papers, newspapers, and magazines are all <sup>fi</sup>lled with guesses. For example, some industrial reports, such as AMR Report, have estimated that the use of RFID systems can reduce supply chain cost by 3 to 5% and increase revenue by 2 to 7% (see [2,24]). Doubtless to say, it is believed that none of the scanning system is 100% reliable and error-free to re<sup>fl</sup>ect the real data and inventory level [9,28]. Our discussions with various industrialists have indicated that RFID systems need not outperform the traditional systems such as bar-coding systems because the barcode system possesses a higher reliability on read rate [5]. There are actually failure cases with the use of RFID technologies in inventory management (see [31,38] for details). Existing studies also comment that RFID is also suffering from read rate inaccuracy [34,35] and the observed successful read rate in real world RFID application is often just in between 60 and 70% [13,16,20]. The stability of RFID on reading the tag depends on various environment factors such as tagged object, tag placement, angle or rotation, and read distance [30,41]. For example, a pilot study examines the reliability of the RFID for tracking the location of nurses, patients and medical equipment in a hospital [30]. The RFID antennas are placed at the ceiling over the patient's room entrance and at the bedside while the RFID tags are attached to different body positions (chest, neck or wrist) of the nurses. Results show that it is more appropriate to posit the tag near the chest but if two nurses walk under the antenna at the same time, the accuracy of the tag reading drops by about half. Therefore, when the tags are <sup>fi</sup>tted in the health care apparel for enhancing the inventory management, one has to take the tag position into the account that it will affect the RFID reading accuracy. As a result, we cannot simply conclude that RFID is superior to the barcode system in all situations without any in-depth investigation. To clearly show the literature positioning of this paper, a systematic comparison between this paper and the other closely related papers is shown in Table 1.<sup>1</sup> From Table 1, we can see that this paper is the <sup>fi</sup>rst one which analytically compares the inventory accuracy issue between the RFID and the bar-coding systems based on the respective transaction errors. In addition, this paper is rather unique because it also examines the supply chain coordination issue and focuses on healthcare related operations.

In this paper, we conduct an analytical study on developing the conditions in which RFID systems would be preferred when compared to bar-coding systems for apparel inventory control in the health care sectors. We also explore the respective business value of switching from bar-coding to RFID systems. By extending the study to a supply chain context (which includes an upstream supplier and the downstream health care organization), we further investigate whether and how win–win situation (i.e. both the supplier and the health care organization can have cost or pro<sup>fi</sup>t improvement with the change of the scanning system) can be achieved in the supply chain. Insights are generated.

The remainder of the paper is organized as follows. In Section 2, we consider the accuracy of scanning systems and introduce the related model for analysis. In Section 3, we compare the business value and derive the analytical conditions that RFID system outperforms the bar-coding system (or vice versa). If the health care organization changes the scanning systems, the impact on the supplier is analyzed and presented in Section 4. Following the analytical results, we propose the use of a surplus sharing contract to achieve win–win situation between the supplier and the health care organization in Section 5. We conclude in Section 6. To simplify our exposition: (i) we use the subscripts B and R to represent bar-coding system and RFID system respectively throughout the paper, (ii) all detailed mathematical derivations and proofs are provided in Appendix A.

## 2. Model

Following the work by Iglehart and Morey [19], we consider a challenge with inventory accuracy owing to the data error such as scanning error (i.e., the computer record does not give the true picture on inventory level) for apparel items in a health care organization. To start with, we focus on one product item and consider the health care organization is employing a multi-period periodic review inventory system with a stationary (s, S) policy. Demand is stochastic and would come from time to time. In the health care organization, transactions are recorded electronically by scanning methods. We compare two data scanning systems: RFID (R) and bar-coding (B). Since there are data errors, periodic stock checking is necessary and suppose that there are $N _ { i }$ periods between stock checking, where i∈{B,R}. Let h be the inventory carrying cost per item per period and J be the cost of conducting stock checking, where i∈{B,R}; J is given by $C _ { 1 } + C _ { 2 } T _ { i }$ where $C _ { 1 }$ refers to the <sup>fi</sup>xed cost of conducting stock taking (e.g., the use of full-time staff members), $C _ { 2 }$ refers to the time-dependent cost of conducting stock taking (e.g., the use of part time staff), and $T _ { i }$ represents the time required to conduct stock taking for i∈{B,R}. Notice that in this paper, we consider the commonly observed case in which $J _ { i }$ is a much bigger expense compared to the inventory holding cost incurred for an item. Following the literature [12,19,22], we model the data error $e _ { i , t } , \mathrm { f o r } t { = } 1 , 2 , . . . , N _ { i } ,$ as an independent, identically distributed (iid) random variable following a normal distribution with a zero mean and a variance $\sigma _ { i } ^ { 2 }$ (we call $\sigma _ { i } ^ { 2 }$ the error variation parameter for system i∈{B,R}),

Literature positioning of this paper (Yes ✓; No –).

<table><tr><td>Paper</td><td>Approach-Analytical modeling (A), empirical (E) or Computational simulation (C)</td><td>Factors contributing to inventory inaccuracy-Misplacement (M), Transaction error (T) or Shrinkage (S)</td><td>Coordination</td><td>Domain (industry)</td><td>RFID vs bar-coding</td></tr><tr><td>[19]</td><td>A</td><td>T</td><td>-</td><td>Not specified</td><td>-</td></tr><tr><td>[15]</td><td>C</td><td>M, T and S</td><td>-</td><td>Supermarket</td><td>-</td></tr><tr><td>[21]</td><td>C</td><td>S</td><td>-</td><td>Retail</td><td>-</td></tr><tr><td>[3]</td><td>A</td><td>M, T and S</td><td>-</td><td>Retail</td><td>-</td></tr><tr><td>[17]</td><td>A</td><td>S</td><td>√</td><td>Retail</td><td>-</td></tr><tr><td>[22]</td><td>A</td><td>T</td><td>-</td><td>Retail</td><td>-</td></tr><tr><td>[25]</td><td>C</td><td>S</td><td>-</td><td>Retail</td><td>-</td></tr><tr><td>[12]</td><td>A and C</td><td>M and T</td><td>-</td><td>Retail</td><td>-</td></tr><tr><td>[23]</td><td>A</td><td>S</td><td>-</td><td>Not specified</td><td>-</td></tr><tr><td>[33]</td><td>C</td><td>M and S</td><td>-</td><td>Not specified</td><td>-</td></tr><tr><td>[36]</td><td>A</td><td>M and S</td><td>√</td><td>Warehousing</td><td>-</td></tr><tr><td>[32]</td><td>A</td><td>T</td><td>-</td><td>Retail</td><td>-</td></tr><tr><td>[4]</td><td>A and E</td><td>S</td><td>-</td><td>Healthcare</td><td>√</td></tr><tr><td>[18]</td><td>C</td><td>M, T and S</td><td>-</td><td>Retail</td><td>-</td></tr><tr><td>This paper</td><td>A</td><td>T</td><td>√</td><td>Healthcare</td><td>√</td></tr></table>

$$
e _ {i, t} \sim N \left(0, \sigma_ {i} ^ {2}\right).\tag{1}
$$

In light of the presence of $e _ { i , t }$ in order to ensure that the data error will not deplete the safety stock between stock checking by a chance larger than 1−s (s represents the probability of having suf<sup>fi</sup>cient inventory shown in the data-<sup>fi</sup>le but insuf<sup>fi</sup>cient inventory in physical inventory due to scanning error), we need to <sup>fi</sup>nd the required amount of safety stock $\xi _ { i } ( N _ { i } )$ and determine the optimal frequency of stock checking $N _ { i }$ to correct the discrepancy between the data record and the actual inventory in-stock. Following Iglehart and Morey [19], it is easy to <sup>fi</sup>nd that $\xi _ { i } ( N _ { i } )$ can be derived as below,

$$
\xi_ {i} (N _ {i}) = \sigma_ {i} \sqrt {N _ {i}} \gamma (s),\tag{2}
$$

where $\gamma ( s ) = \phi ^ { - 1 } [ ( 1 - ( s / 2 ) ] > 0$ and $i \in \{ B , R \}$

We denote the total inventory cost per period with $\xi _ { i } ( N _ { i } )$ ) by $K _ { i } ( N _ { i } )$ and it is given as follows,

$$
K _ {i} (N _ {i}) = h \xi_ {i} (N _ {i}) + (C _ {1} + C _ {2} T _ {i}) / N _ {i}, i \in \{B, R \}.\tag{3}
$$

Notice that in $K _ { i } ( N _ { i } )$ , since $( C _ { 1 } + C _ { 2 } T _ { i } ) / N _ { i } { = } J _ { i } / N _ { i }$ is the cost of conducting stock checking (including manpower cost) per period, we consider in this paper the commonly observed case that it is bigger than the inventory holding cost for an item per period, i.e. $J _ { i } / N _ { i } { > } h \xi _ { i } ( N _ { i } )$

We can <sup>fi</sup>nd the optimal $N _ { i }$ which minimizes K<sub>i</sub>(N<sub>i</sub>), N<sub>i</sub>\*, by solving the <sup>fi</sup>rst order condition:

$$
\begin{array}{l} d K _ {i} (N _ {i}) / d N _ {i} = 0. 5 h \sigma_ {i} \gamma (s) N _ {i} ^ {- 0. 5} - (C _ {1} + C _ {2} T _ {i}) N _ {i} ^ {- 2} = 0 \Rightarrow \\ N _ {i} ^ {*} = \left(\frac {C _ {1} + C _ {2} T _ {i}}{0 . 5 h \sigma_ {i} \gamma (s)}\right) ^ {2 / 3}. \end{array}\tag{4}
$$

Notice that $K _ { i } ( N _ { i } )$ is a strictly convex function (refer to Appendix (A1) for the details).

Putting Eq. (4) back into Eq. (3) yields the optimal total cost for employing a scanning system i∈{B,R},

$$
K _ {i} \left(N _ {i} ^ {*}\right) = l \alpha_ {i} \sigma_ {i} ^ {2 / 3}\tag{6}
$$

where

$$
\alpha_ {i} = (C _ {1} + C _ {2} T _ {i}) ^ {1 / 3},
$$

$$
l = 3 (0. 5 h \gamma (s)) ^ {2 / 3}.\tag{7}
$$

8

## 3. RFID system versus bar-coding system

We now proceed to compare the business values of the RFID system and the bar-coding system. De<sup>fi</sup>ne:

$$
\Delta K = K _ {R} \left(N _ {R} ^ {*}\right) - K _ {B} \left(N _ {B} ^ {*}\right).\tag{9}
$$

It is obvious that ΔK represents the difference between the optimal inventory cost with RFID system and the optimal inventory cost with bar-coding system. When ΔK is negative, it means that the RFID system outperforms the bar-coding system (in yielding a smaller inventory cost) whereas a positive ΔK means that the bar-coding system performs better than the RFID system. Examining ΔK thus reveals the analytical conditions for one system to outperform the other one. From Eq. (9), we can show that

$$
\Delta K = l (\Omega - \delta),\tag{10}
$$

where

$$
\Omega = \alpha_ {R} \sigma_ {R} ^ {\frac {2}{3}},\tag{11}
$$

$$
\delta = \alpha_ {B} \sigma_ {B} ^ {\frac {2}{3}}.\tag{12}
$$

With ΔK expressed in Eq. (10), by simple re<sup>fl</sup>ection, we have Lemma 1 and Lemma 2.

Lemma 1. Suppose that a health care organization switches its scanning system from a bar-coding system to an RFID system, the expected business value of the RFID system is equal to −ΔK.

Lemma 2. (a) The RFID system outperforms the bar-coding system if and only $\begin{array} { r } { i f \Omega < \delta \Longleftrightarrow \Big ( \frac { C _ { 1 } + C _ { 2 } T _ { R } } { C _ { 1 } + C _ { 2 } T _ { B } } \Big ) < \Big ( \frac { \sigma _ { B } } { \sigma _ { R } } \Big ) ^ { 2 } . \left( b \right) } \end{array}$ The bar-coding system outperforms the RFID system if and only $\begin{array} { r } { i f \Omega > \delta \Longleftrightarrow \left( \frac { C _ { 1 } + C _ { 2 } T _ { R } } { C _ { 1 } + C _ { 2 } T _ { B } } \right) > \left( \frac { \sigma _ { B } } { \sigma _ { R } } \right) ^ { 2 } } \end{array}$

Lemma 1 gives us the closed-form expression of the bene<sup>fi</sup>t brought by switching the scanning system from bar-coding to RFID. To be speci<sup>fi</sup>c, from Eq. (10), we will see that the bene<sup>fi</sup>t of switching to RFID system is larger with the following cases<sup>2</sup>: (i) larger $\alpha _ { B }$ and/or larger $\sigma _ { B }$ (i.e. δ is larger), (ii) smaller α and/or smaller σ (i.e. Ω is smaller), and (iii) larger h and/or smaller s (i.e. l is larger). Here, case (i) “larger $\alpha _ { B }$ and/or larger ${ \sigma } _ { B } ^ { \ " }$ and case (ii) “smaller α and/or smaller $\boldsymbol { \sigma _ { R } } ^ { \prime \prime }$ are very intuitive because they refer to the cases in which it is less bene<sup>fi</sup>cial to employ the bar-coding system. In practice, if the RFID system keeps upgrading such that its error variation is reduced, a more signi<sup>fi</sup>cant inventory cost saving will result. This illustrates the happening of case (ii) (which is more natural to be realized compared to case (i)). For case (iii), having a larger h and/or a smaller s tends to yield a higher bene<sup>fi</sup>t when the health care organization switches to RFID. It is thus interesting to note that the bene<sup>fi</sup>t of using RFID system is related to the holding cost h and also the probability of having suf<sup>fi</sup>cient inventory shown in the data-<sup>fi</sup>le but insuf<sup>fi</sup>cient inventory in physical inventory due to scanning error (s). As a remark, in any of the above cases, the condition of Ωbδ must be held, otherwise, the health care organization does not have the motivation to switch to RFID system when no cost saving can be attained. Lemma 2 further shows the necessary and suf<sup>fi</sup>cient conditions for RFID systems to outperform the bar-coding system (and vice versa). A closer examination of the conditions reveal that they are all based on the two systems' stock-taking times (and hence costs) and error variations. Moreover, since there is a power of 2 for the ratio of error variations, we can see that the relative signi<sup>fi</sup>cance of the error variations ratio is higher than the stock-taking costs ratio. Last but not least, as the conditions are neat and easily computable, they help health care organizations to check and see whether the RFID system or the bar-coding system is more preferred. De<sup>fi</sup>ne:

Error variation ratio (R to $\begin{array} { r } { \mathsf { B } ) \colon \tau _ { R / B } \equiv \left( \frac { \sigma _ { R } } { \sigma _ { R } } \right) } \end{array}$

Stock-taking cost ratio (B to $\begin{array} { r } { \mathbb { R } ) \colon \rho _ { B / R } \varXi \bigl ( \frac { C _ { 1 } + C _ { 2 } T _ { B } } { C _ { 1 } + C _ { 2 } T _ { R } } \bigr ) } \end{array}$

<sup>þ</sup>As a remark, in many cases, it is well-argued that $\sigma _ { B } { < } \sigma _ { R }$ (because RFID system tends to yield a larger variation of errors compared to the more stable barcode system [40]). Moreover, since RFID can help reduce the time required for stock taking in the health care organization, we have: $T _ { B } > T _ { R } .$ . In this case, we can derive the analytical suf<sup>fi</sup>cient condition in which the bar-coding system outperforms the RFID system as summarized in Lemma 3.

Lemma 3. When $\sigma _ { B } { < } \sigma _ { R }$ and $T _ { B } > T _ { R } ,$ the bar-coding system outperforms the RFID system $i f \rho _ { B / R } { < } \tau ^ { 2 } { } _ { R / B }$

Proof of Lemma 3. All proofs are included in Appendix A.

Lemma 3 shows an interesting result (under the speci<sup>fi</sup>c special case when $\tau _ { R / B } > 1$ and $\rho _ { B / R } > 1 )$ which suf<sup>fi</sup>ces to let us check if the bar-coding system is better than the RFID system. Since it is totally possible to have the conditions in Lemma 3 all being satis<sup>fi</sup>ed, we argue that the commonly adopted bar-coding system can outperform the RFID system in some cases and hence it is important for the health care organization to double check the respective parameters before proceeding to conduct the switch of scanning system from bar-coding to RFID.

## 4. Changing scanning system and scenario analysis

In the previous section, we explore the analytical result by comparing the performance between the RFID and bar-coding systems. Lemma 2 gives the closed-form conditions under which RFID outperforms bar-coding system or vice versa from the perspective of the health care organization. Suppose that currently, the health care organization is using system i (either B or R) and after checking the conditions in Lemma 2, the health care organization will prefer system $i \in \{ B , R \}$ and make a change of the scanning system<sup>3</sup> (either from B to R, or from R to B). This decision is naturally bene<sup>fi</sup>cial (and indeed optimal) to the health care organization. However, is the change also bene<sup>fi</sup>cial to the supplier who supplies the product to the health care organization? Is it bene<sup>fi</sup>cial to the whole supply chain? We explore the answers to these questions in this section.

First of all, we consider the supplier as a simple supplier who produces the product at a unit production cost of c and supplies the product to the health care organization at a wholesale price w. The supplier adopts the make-to-order strategy in which it does not hold inventory in advance before the health care organization's order comes. As a result, the supplier's pro<sup>fi</sup>t is equal to the unit pro<sup>fi</sup>t margin times the health care organization's order quantity. Obviously, when we compare the health care organization's selection decision on the scanning system (i.e., choosing either B or R), the only implied difference in terms of quantity for the supplier is the corresponding amount of safety stock that the health care organization will hold.<sup>4</sup> Thus, the effective pro<sup>fi</sup>t that we need to consider for the supplier with respect to the health care organization's choice of scanning system is given below,

$$
\pi_ {i} = (w - c) \xi_ {i} \left(N _ {i} ^ {*}\right), i \in \{B, R \}.\tag{13}
$$

De<sup>fi</sup>ne:

$$
\Delta S = \xi_ {R} (N _ {R} ^ {*}) - \xi_ {B} (N _ {B} ^ {*}).\tag{14}
$$

ΔS represents the difference between safety stock requirements with RFID system and bar-coding system under optimal stock checking frequency.

From the de<sup>fi</sup>nition in Eq. (14), it is crystal clear that $\Delta S > 0$ (or ΔSb0) implies the situation in which the supplier will be bene<sup>fi</sup>ted when the health care organization changes the scanning system from bar-coding to RFID (or from RFID to bar-coding). It is easy to further derive that:

$$
\Delta S = \frac {\sqrt {3} \gamma (s)}{\sqrt {l}} (\Omega - \delta).\tag{15}
$$

For the health care organization's optimal choice, by Lemma 2, we have the following two cases:

Case 1. The health care organization prefers R to B if and only if $\Omega { < } \delta .$

Case 2. The health care organization prefers B to R if and only if Ω>δ.

With respect to the above two cases, in the following, we <sup>fi</sup>rst explore two scenarios in which it is optimal for the health care organization to make a change in the scanning system. We will then examine the respective impact on the supplier's effective pro<sup>fi</sup>t.

4.1. Scenario 1: The health care organization originally uses B and then changes to R

Under Scenario 1, the condition for R to be optimal for the health care organization is:

Ωbδ  i:e:ΔK < 0 :

Scenario 1a: If $\sigma _ { B } { \geq } \sigma _ { R } ,$ and ${ \underset { / 3 } { \underbrace { \alpha _ { B } } } } { > } { \alpha _ { R } } ;$ Since $\frac { \alpha _ { R } } { \alpha _ { B } } { < } 1$ and $\left( { \frac { \sigma _ { B } } { \sigma _ { R } } } \right) ^ { 2 / 3 } \geq 1$ , it is always true that $\frac { \alpha _ { R } } { \alpha _ { B } } < \left( \frac { \sigma _ { B } } { \sigma _ { R } } \right) ^ { ~ < / : }$ . Therefore, we have Ωbδ which implies $\Delta K { < } 0$ and $\Delta S { < } 0$

Scenario 1b: If $\sigma _ { B } { < } \sigma _ { R } ,$ and $\alpha _ { B } { > } \alpha _ { R } ;$

(i) When $\frac { \alpha _ { R } } { \alpha _ { B } } { < } \bigg ( \frac { \sigma _ { B } } { \sigma _ { R } } \bigg ) ^ { ~ \angle / = \angle ~ }$ , then Ωbδ which implies $\Delta K { < } 0$ and ΔSb0.

(ii) When $\frac { \alpha _ { R } } { \alpha _ { B } } > \left( \frac { \sigma _ { B } } { \sigma _ { R } } \right) ^ { 2 / 3 }$ , then Ω>δ which implies $\Delta K > 0$ and ΔS>0.

4.2. Scenario 2: The health care organization originally uses R and then changes to B

Under Scenario 2, the condition for B to be optimal for the health care organization is:

$$
\Omega > \delta (\text { i.e. } \Delta K > 0).
$$

Scenario 2a: I ${ \bf \sigma } _ { G B } 2 { \bf \sigma } \sigma _ { R } ,$ and $\alpha _ { B } { > } \alpha _ { R } { ; }$ then Ωbδ which implies $\Delta K { < } 0$ and $\Delta S { < } 0$

Scenario 2b: If $\sigma _ { B } { < } \sigma _ { R } , \mathop { \mathrm { a n d } } _ { \lambda } \alpha _ { B } { > } \alpha _ { R } ;$

(i) When $\frac { \alpha _ { R } } { \alpha _ { B } } { < } \bigg ( \frac { \sigma _ { B } } { \sigma _ { R } } \bigg ) ^ { < / - 1 }$ , then Ωbδ which implies $\Delta K { < } 0$ and ΔSb0.

(ii) When $\begin{array} { r } { \frac { \alpha _ { R } } { \alpha _ { B } } > \left( \frac { \sigma _ { B } } { \sigma _ { R } } \right) ^ { 2 / 3 } } \end{array}$ , then Ω>δ which implies $\Delta K > 0$ and $\Delta S { > } 0 .$

From the above scenario analysis, we have Lemma 4.

Lemma 4. When the health care organization changes its scanning system, (a) the health care organization will be benefited under Scenario 1a, Scenario 1b(i) and Scenario $2 b ( i i ) ; ( b )$ while the supplier will be better off under Scenario 1b(ii), Scenario 2a and Scenario 2b(i).

Lemma 4 indicates an interesting result: When we examine all the scenarios under which it is optimal for the health care organization to make a change of its scanning system, none of them will bene<sup>fi</sup>t the supplier. Thus, we <sup>fi</sup>nd that none of these scenarios will lead to a win–win situation in the supply chain for both the health care organization and the supplier at the same time. This is because health care organization switches from bar-coding to RFID system if and only if $\Delta K { < } 0 ,$ , however, it will lead to a reduction on the safety stock requirement $( \Delta S { < } 0 )$ and the supplier will suffer. Similar phenomenon can be observed when the health care organization switches from RFID to bar-coding system. In addition, it is interesting to note that ΔK and ΔS have the same sign which implies that win–win situation will not be achieved automatically. As we know, from the supply chain perspective, the occurrence of win– win situation has to satisfy a pre-requisite that the supply chain's performance (“total piece of cake”) must <sup>fi</sup>rst be improved upon the change of the scanning system (or else we can only achieve a win–lose situation). However, our analysis above indicates that with the change of the scanning system, the supply chain's performance may or may not be improved as the overall supply chain's surplus upon the change depends on the amount of improvement the health care organization receives and the amount of loss the supplier suffers. Lemma 5 summarizes the results.

Lemma 5. With the health care organization's optimal change of the scanning system, the supply chain's performance under Scenario 1a, Scenario 1b(i), Scenario 2a(ii), will: (i) be enhanced $i f \left| \Delta K \right| > \left| ( w - c ) \Delta S \right|$ (ii) be worse-off $i f \left| \Delta K \right| { < } { \big | } ( w - c ) \Delta S { \big | }$

## 5. Achieving win–win: Surplus sharing contract

From Section 4, even though the change of inventory scanning system can help reduce the health care organization's amount of required safety stock (and hence the corresponding inventory cost), we notice that the supplier is not bene<sup>fi</sup>ted and has to suffer. This will bring an issue that the supplier will be discouraged to work faithfully with the health care organization when the new scanning system is in place. This is obviously un-desirable in the context of supply chain management. As a result, in this section, we propose to use a surplus sharing contract to help achieve win–win improvement for both the supplier and the health care organization. To be speci<sup>fi</sup>c, when the supply chain's surplus upon the change of scanning system is positive (Lemma 5), i.e. $| \Delta K | > | ( w - c ) \Delta S | ,$ , one way to compensate for the supplier's loss when the health care organization changes its inventory scanning system is to share a fraction of surplus generated by the health care organization with the supplier. Under a surplus sharing contract, the supplier offers a lower wholesale price w<sub>s</sub> (i.e. w>w ) to the health care organization but receives a fraction, f, of the health care organization's surplus from inventory cost so that both parties will have the incentive to adopt the contract. To closely investigate this surplus sharing contract, we present the following:

(a) Consider the initial stage in Scenario 1 that no contract is executed in the supply chain. The health care organization (O) switches from B to R due to its better scanning performance, and it will attain cost saving $\Delta \pi _ { 0 , R }$ as follows:

$$
\Delta \pi_ {O, R} = - \Delta K - w \Delta S.\tag{16}
$$

Yet, the supplier (S) will suffer from selling fewer safety stock to the health care organization under Scenario 1a and Scenario 1b(i). As a result, it will diminish the pro<sup>fi</sup>t revenue of the supplier and the pro<sup>fi</sup>t change is de<sup>fi</sup>ned as $\Delta \pi _ { S , R }$ and shown in Eq. (17):

$$
\Delta \pi_ {S, R} = (w - c) \Delta S.\tag{17}
$$

Now, the pro<sup>fi</sup>t change of the total supply chain (SC) before the surplus sharing contract execution is denoted as $\Delta \pi _ { S C , R }$ as follows:

$$
\Delta \pi_ {S C, R} = - \Delta K - c \Delta S.\tag{18}
$$

(b) If a surplus sharing contract is executed in the supply chain, the health care organization will share a fraction of surplus from inventory cost saving with the supplier, but enjoy a lower purchasing price (i.e., wholesale price). The actual bene<sup>fi</sup>t of the health care organization is dependent of the parameters, f and w . Assume the order quantities of using bar-coding and RFID system are $I + \xi _ { B } ( N _ { B } ^ { * } )$ and $I + \xi _ { R } ( N _ { R } ^ { * } )$ , respectively, where I is the cycle stock level. The surplus of the health care organization (O) with the surplus-sharing contract (SS) is denoted as $\Delta \pi _ { O , R } ^ { S S }$ as follows:

$$
\Delta \pi_ {O, R} ^ {S S} = - (1 - f) \Delta K + (w - w _ {S}) I + w \xi_ {B} \left(N _ {B} ^ {*}\right) - w _ {S} \xi_ {R} \left(N _ {R} ^ {*}\right).\tag{19}
$$

On the other hand, the supplier receives a fraction of the health care organization's surplus but has to offer a lower wholesale price w . The pro<sup>fi</sup>t change of the supplier with the surplus sharing contract (SS) is $\Delta \pi _ { S , R } ^ { S S }$ and presented in Eq. (20).

$$
\Delta \pi_ {S, R} ^ {S S} = - f \Delta K - (w - w _ {s}) I - w \xi_ {B} \left(N _ {B} ^ {*}\right) + w _ {S} \xi_ {R} \left(N _ {R} ^ {*}\right) - c \Delta S.\tag{20}
$$

The pro<sup>fi</sup>t change of the entire supply chain (SC) with surplus sharing (SS) contract is represented by $\Delta \pi _ { S C , I } ^ { S S }$ <sub>R</sub>.

$$
\Delta \pi_ {S C, R} ^ {S S} = - \Delta K - c \Delta S.\tag{21}
$$

Similarly, when the health care organization switches the scanning system from R to B in Scenario 2, the analytical surplus and pro<sup>fi</sup>t change of each party can be determined as above and the results are summarized in Tables 2 and 3. By comparing the total supply chain surplus when there is a change of the scanning system, it is obvious that the performance of the entire supply chain is enhanced in both scenarios if surplus sharing contract is implemented when $| \Delta K | > | ( w - c ) \Delta S |$ . We have Lemma 6.

Lemma 6. When the health care organization switches the scanning system and under the condition that $| \Delta K | > | ( w - c ) \Delta S |$ , a win–win situation can be achieved by using the surplus sharing contract when: $( a ) \ \Delta \pi _ { O , R } ^ { S S } > 0$ and $\Delta \pi _ { S , R } ^ { S S } > 0$ under Scenario 1a and Scenario 1b(i); (b) $\Delta \pi _ { O , B } ^ { S S } > 0$ and $\Delta \pi _ { S , B } ^ { S S } > 0$ under Scenario 2b(ii).

Notice that Lemma 6 means that both supply chain members will be better off if the surplus sharing contract is properly set and adopted under Scenario 1a, Scenario 1b(i), and Scenario 2b(ii) with the condition that $| \Delta K | > | ( w - c ) \Delta S | ,$ . The key factors to successfully implement surplus sharing contract depend on two decisions: First, the bene<sup>fi</sup>t enjoyed by the health care organization from a lower purchasing price should be “attractive” when comparing to the surplus shared with the supplier from the inventory cost saving. Second, the supplier is able to receive substantial bene<sup>fi</sup>t from sharing surplus with the health care organization, in which it should be larger than the revenue loss from offering a lower wholesale price w .

Table 2  
Summary of the surplus sharing contract implementation under Scenario 1(a) and Scenario 1(b)i.

<table><tr><td>Under Scenario 1 (from B to R)</td><td>Before surplus sharing contract implementation</td><td>After surplus sharing contract implementation</td></tr><tr><td>Health care organization&#x27;s surplus</td><td> $\Delta\pi_{O,R} = -\Delta K - w\Delta S$ </td><td> $\Delta\pi_{O,R}^{SS} = -(1-f)\Delta K + (w-w_S)I + w\xi_B(N_B^*) - w_S\xi_R(N_R^*)$ </td></tr><tr><td>Supplier&#x27;s profit change</td><td> $\Delta\pi_{S,R} = (w-c)\Delta S$ </td><td> $\Delta\pi_{S,R}^{SS} = -f\Delta K - (w-w_S)I - w\xi_B(N_B^*) + w_S\xi_R(N_R^*) - c\Delta S$ </td></tr><tr><td>Total supply chain surplus</td><td> $\Delta\pi_{SC,R} = -\Delta K - c\Delta S$ </td><td> $\Delta\pi_{SC,R}^{SS} = -\Delta K - c\Delta S$ </td></tr></table>

## 6. Conclusion

In this paper, we focus on the data error of the scanning systems to re<sup>fl</sup>ect its accuracy on recording the inventory of apparel items in a health care organization. This is the performance indicator for system selection (either RFID or bar-coding system) from the health care organization's perspective because it relates to the amount of required safety stock and hence the inventory cost. From our analysis above, we have <sup>fi</sup>rst demonstrated in closed-form that the ratios between the two systems' stock-taking costs and error variations will determine whether RFID system will outperform the bar-coding system (and vice versa). We have further illustrated the corresponding implications which include: (i) When the health care organization contemplates the switch of scanning system, the relative signi<sup>fi</sup>cance of the error variations ratio should be higher than the stock-taking costs ratio (because of the “squared” effect). (ii) When it is optimal for the health care organization to switch from bar-coding to RFID scanning system, if the holding cost is higher or the probability of having suf<sup>fi</sup>cient inventory shown in the data-<sup>fi</sup>le but insuf<sup>fi</sup>cient inventory in physical inventory due to scanning error (s) is lower, the bene<sup>fi</sup>t of switching from the bar-coding system to the RFID system is larger. Next, we have extended our analysis to a supply chain context which includes an upstream supplier and the health care organization (as the downstream buyer). We have examined the supply chain in different scenarios and shown mathematically that no matter whether the health care organization changes its scanning system from bar-coding to RFID (or vice versa), the change will only bene<sup>fi</sup>t the health care organization but the supplier will always suffer. As a result, we have developed a new contract scheme known as “surplus sharing contract” and illustrated how the health care organization can achieve a win–win situation under which both the supplier and the health care organization can have improvement (in cost or pro<sup>fi</sup>t) with the change of the scanning system. We believe that this contract is important because it can guarantee that both the supplier and the health care organization will be bene<sup>fi</sup>ted under the change of scanning system and hence they will faithfully work together as supply chain partners in inventory management with respect to the changed scanning system. For future research, it will be interesting to conduct empirical study on whether and how our proposed surplus sharing contract can be implemented in practice. It will also be interesting to investigate if some other contracts can also achieve the win–win situation in the supply chain.

Table 3  
Summary of the surplus sharing contract implementation under Scenario 2b(ii).

<table><tr><td>Under Scenario 2 (from R to B)</td><td>Before surplus sharing contract implementation</td><td>After surplus sharing contract implementation</td></tr><tr><td>Health care organization&#x27;s surplus</td><td> $\Delta\pi_{O,B} = \Delta K + w\Delta S$  (22)</td><td> $\Delta\pi_{O,B}^{SS} = (1 - f)\Delta K + (w - w_S)I + w\xi_R(N_R^*) - w_S\xi_B(N_B^*)$  (25)</td></tr><tr><td>Supplier&#x27;s profit change</td><td> $\Delta\pi_{S,B} = -(w - c)\Delta S$  (23)</td><td> $\Delta\pi_{S,B}^{SS} = f\Delta K - (w - w_S)I - w\xi_R(N_R^*) + w_S\xi_B(N_B^*) + c\Delta S$  (26)</td></tr><tr><td>Total supply chain surplus</td><td> $\Delta\pi_{SC,B} = \Delta K + c\Delta S$  (24)</td><td> $\Delta\pi_{SC,B}^{SS} = \Delta K + c\Delta S$  (27)</td></tr></table>

## Acknowledgments

We sincerely thank the editor, and the three anonymous reviewers for their constructive comments and suggestions which led to a major improvement of this paper. We also thank Na Liu for her helpful suggestions on the earlier draft of this paper. Tsan-Ming Choi's research was partially supported by the RGC(HK)-GRF under project account of PolyU 5420/10H. Chi-Leung Hui's research was partially supported by the RGC(HK)-GRF under project account of PolyU 5171/10E.

## Appendix A. Derivations and proofs

## (A1). Detailed derivations for Section 2

According to the work by Iglehart and Morey [19], the amount of safety stock required is derived as:

$$
\begin{array}{l} \xi_ {i} (N _ {i}) = \sigma_ {i} \sqrt {N _ {i}} \gamma (s), \\ \text { where } \gamma (s) = \Phi^ {- 1} ((1 - (s / 2)) > 0 \text { and } i {\in} \{B, R \}. \end{array}\tag{A.1}
$$

We denote the total inventory cost per period with $\xi _ { i } ( N _ { i } )$ ) by $K _ { i } ( N _ { i } )$ and it is given as follows,

$$
K _ {i} (N _ {i}) = h \xi_ {i} (N _ {i}) + (C _ {1} + C _ {2} T _ {i}) / N _ {i}, i \in \{B, R \}.\tag{A.2}
$$

When $\begin{array} { r l } { \operatorname { E q . } } & { { } \left( \mathrm { A . 1 } \right) } \end{array}$ is substituted into Eq. (A.2), we have $K _ { i } ( N _ { i } ) = h \sigma _ { i } \sqrt { N _ { i } } \gamma ( s ) + ( C _ { 1 } + C _ { 2 } T _ { i } ) / N _ { i }$ , and we can <sup>fi</sup>nd the optimal $N _ { i }$ <sup>ð Þ ¼ ð Þ</sup>which minimizes $K _ { i } ( N _ { i } ) , N _ { i } ^ { * }$ <sup>Þ</sup>, by solving the <sup>fi</sup>rst order condition of $K _ { i } \ ( N _ { i } )$ :

$$
\begin{array}{c} d K _ {i} (N _ {i}) / d N _ {i} = 0 \Rightarrow 0. 5 h \sigma_ {i} \gamma (s) N _ {i} ^ {- 0. 5} - (C _ {1} + C _ {2} T _ {i}) N _ {i} ^ {- 2} = 0 \\ N _ {i} ^ {\frac {3}{2}} = (C _ {1} + C _ {2} T _ {i}) / (0. 5 h \sigma_ {i} \gamma (s)) ^ {- 1} \\ N _ {i} ^ {*} = \left(\frac {C _ {1} + C _ {2} T _ {i}}{0 . 5 h \sigma_ {i} \gamma (s)}\right) ^ {2 / 3}. \end{array}\tag{A.3}
$$

We can further check the second order condition of $K _ { i } \ ( N _ { i } )$ to determine the condition that the total inventory cost per period is minimized:

$$
\begin{array}{l} d ^ {2} K _ {i} (N _ {i}) / d N _ {i} ^ {2} = - 0. 2 5 h \sigma_ {i} \gamma (s) N _ {i} ^ {- 1. 5} + 2 (C _ {1} + C _ {2} T _ {i}) N _ {i} ^ {- 3} \\ d ^ {2} K _ {i} (N _ {i}) / d N _ {i} ^ {2} = \frac {1}{N _ {i} ^ {2}} \left(\frac {2 J _ {i}}{N _ {i}} - \frac {h \xi_ {i} (N _ {i})}{4}\right) \\ \therefore \text { If } \left(\frac {J _ {i}}{N _ {i}} - \frac {h \xi_ {i} (N _ {i})}{8}\right) > 0, \end{array}\tag{A.4}
$$

then $K _ { i } \left( N _ { i } \right)$ is a convex function.

Since $J _ { i } / N _ { i } { > } h \xi _ { i } ( N _ { i } )$ , Eq. (A.4) holds and hence $K _ { i } \ ( N _ { i } )$ is a strictly convex function.

Now, if we put Eq. (A.3) into Eq. (A.2), it will yield the optimal total cost for employing a scanning system i∈{B,R},

$$
\begin{array}{l} K _ {i} (N _ {i} ^ {*}) = h \sigma_ {i} \bigg (\frac {C _ {1} + C _ {2} T _ {i}}{0 . 5 h \sigma_ {i} \gamma (s)} \bigg) ^ {\frac {2}{3} \cdot \frac {1}{2}} \gamma (s) + (C _ {1} + C _ {2} T _ {i}) \bigg (\frac {0 . 5 h \sigma_ {i} \gamma (s)}{C _ {1} + C _ {2} T _ {i}} \bigg) ^ {\frac {2}{3}} \\ K _ {i} (N _ {i} ^ {*}) = 3 (C _ {1} + C _ {2} T _ {i}) ^ {\frac {1}{3}} (0. 5 h \sigma_ {i} \gamma (s)) ^ {\frac {2}{3}} \\ K _ {i} (N _ {i} ^ {*}) = l \alpha_ {i} \sigma_ {i} ^ {\frac {2}{3}}. \end{array}\tag{A.5}
$$

$$
\text { where } \alpha_ {i} = (C _ {1} + C _ {2} T _ {i}) ^ {\frac {1}{3}},\tag{A.6}
$$

$$
l = 3 (0. 5 h \gamma (s)) ^ {\frac {2}{3}}.\tag{A.7}
$$

(Q.E.D.)

(A2). Detailed derivations for Section 5

The pro<sup>fi</sup>t of the supplier depends on the corresponding amount of safety stock that the health care organization will hold. The effective pro<sup>fi</sup>t that we consider for the supplier with respective to the health care organization's choice of scanning system is:

$$
\pi_ {i} = (w - c) \xi_ {i} \left(N _ {i} ^ {*}\right), i \in \{B, R \}.\tag{A.8}
$$

The difference of the safety stock requirement between two scanning systems is denoted as:

$$
\Delta S = \xi_ {R} (N _ {R} ^ {*}) - \xi_ {B} (N _ {B} ^ {*}).\tag{A.9}
$$

By putting Eqs. (A.3) and (A.1) back to Eq. (A.8), it becomes

$$
\begin{array}{l} \Delta S = \frac {\alpha_ {R} \sigma_ {R} ^ {\frac {2}{3}} (\gamma (s)) ^ {\frac {2}{3}}}{(0 . 5 h) ^ {\frac {1}{3}}} - \frac {\alpha_ {B} \sigma_ {B} ^ {\frac {2}{3}} (\gamma (s)) ^ {\frac {2}{3}}}{(0 . 5 h) ^ {\frac {1}{3}}} \\ \Delta S = \alpha_ {R} \sigma_ {R} ^ {\frac {2}{3}} (\gamma (s)) ^ {\frac {2}{3}} \left[ \frac {3 ^ {\frac {1}{2}} (\gamma (s)) ^ {\frac {1}{3}}}{l ^ {\frac {1}{2}}} \right] - \alpha_ {B} \sigma_ {B} ^ {\frac {2}{3}} (\gamma (s)) ^ {\frac {2}{3}} \left[ \frac {3 ^ {\frac {1}{2}} (\gamma (s)) ^ {\frac {1}{3}}}{l ^ {\frac {1}{2}}} \right] \\ \Delta S = \frac {\sqrt {3} \gamma (s)}{\sqrt {l}} (\Omega - \delta). \end{array}\tag{A.10}
$$

Now we compare the pro<sup>fi</sup>t change of each party in the supply chain when the health care organization changes the scanning system:

Scenario 1 (switching from B to R):

(a) When there is no contract executed in the supply chain, the health care organization (O) switches from B to R due to its better scanning performance, and it will attain cost saving $\Delta \pi _ { O , R }$ as follows:

$$
\begin{array}{l} \Delta \pi_ {O, R} = [ K _ {B} (N _ {B} ^ {*}) - K _ {R} (N _ {R} ^ {*}) ] + w [ \xi_ {B} (N _ {R} ^ {*}) ], \text {   where   } \xi_ {R} (N _ {R} ^ {*}) <   \xi_ {B} (N _ {B} ^ {*}) \\ \Delta \pi_ {S, R} = - \Delta K - w \Delta S. \end{array}\tag{A.11}
$$

(a) The supplier (S) will suffer from selling fewer safety stocks and the supplier's pro<sup>fi</sup>t change $\Delta \pi _ { S , R }$ is shown as below: $\begin{array} { r l } & { \Delta \pi _ { S , R } = ( w - c ) \xi _ { R } ( N _ { R } ^ { * } ) - ( w - c ) \xi _ { B } ( N _ { B } ^ { * } ) } \\ & { \Delta \pi _ { S , R } = ( w - c ) \Delta S . } \end{array}$ ; where $\xi _ { R } ( N _ { R } ^ { * } ) < \xi _ { B } ( N _ { B } ^ { * } )$

A:12

Now, the pro<sup>fi</sup>t change of the entire supply chain (SC) before the surplus sharing contract executed is denoted as $\Delta \pi _ { S C , R } \mathrm { : }$

$$
\begin{array}{l} \Delta \pi_ {S C, R} = - \Delta K + w \Delta S + (w - c) \Delta S \\ \Delta \pi_ {S C, R} = - \Delta K - c \Delta S, \text {   where   } \Delta K <   0 \text {   and   } \Delta S <   0. \end{array}\tag{A.13}
$$

(b) If a surplus sharing contract is executed in the supply chain, the health care organization will share a fraction of surplus from inventory cost saving with the supplier, but enjoy a lower wholesale price. Assume the order quantities of using bar-coding and RFID system are $I + \xi _ { B } ( N _ { B } ^ { * } )$ and $I + \xi _ { R } ( N _ { R } ^ { * } )$ respectively, where I is the cycle stock level. The surplus of the health care organization (O) with surplus sharing contract (SS) is denoted as $\varDelta \pi _ { O , R } ^ { S S }$

$$
\begin{array}{r l} & {\Delta \pi_ {O, R} ^ {S S} = (1 - f) [ K _ {B} (N _ {B} ^ {*}) - K _ {R} (N _ {R} ^ {*}) ] + w [ I + \xi_ {B} (N _ {B} ^ {*}) ] - w _ {S} [ I + \xi_ {R} (N _ {R} ^ {*}) ]} \\ & {\Delta \pi_ {O, R} ^ {S S} = - (1 - f) \Delta K + (w - w _ {S}) I + w \xi_ {B} (N _ {B} ^ {*}) - w _ {S} \xi_ {R} (N _ {R} ^ {*}).} \end{array}\tag{A.14}
$$

The corresponding pro<sup>fi</sup>t change of the supplier (S) with the surplus sharing contract (SS) is:

$$
\begin{array}{l} \Delta \pi_ {S, R} ^ {S S} = f [ K _ {B} (N _ {B} ^ {*}) - K _ {R} (N _ {R} ^ {*}) ] + (w _ {S} - c) [ I + \xi_ {R} (N _ {R} ^ {*}) ] - (w - c) [ I + \xi_ {B} (N _ {B} ^ {*}) ] \\ \Delta \pi_ {S, R} ^ {S S} = - f \Delta K - (w - w _ {s}) I - w \xi_ {B} (N _ {B} ^ {*}) + w _ {S} \xi_ {R} (N _ {R} ^ {*}) - c \Delta S. \end{array}\tag{A.15}
$$

The pro<sup>fi</sup>t change of the entire supply chain (SC) with surplus sharing (SS) contract is represented by $\varDelta \pi _ { S C , R } ^ { S S } \mathrm { : }$

$$
\begin{array}{l} \Delta \pi_ {S C, R} ^ {S S} = - (1 - f) \Delta K + (w - w _ {S}) I + w \xi_ {B} (N _ {B} ^ {*}) - w _ {S} \xi_ {R} (N _ {R} ^ {*}) - f \Delta K - (w - w _ {s}) I \\ - w \xi_ {B} (N _ {B} ^ {*}) + w _ {S} \xi_ {R} (N _ {R} ^ {*}) - c \Delta S \\ \Delta \pi_ {S C, R} ^ {S S} = - \Delta K - c \Delta S, w h e r e \Delta K <   0 a n d \Delta S <   0. \end{array}\tag{A.16}
$$

Scenario 2 (from R to B):

(a) When there is no contract executed in the supply chain, Pro<sup>fi</sup>t change of the health care organization (O) is:

$$
\begin{array}{l} \Delta \pi_ {O, B} = [ K _ {R} (N _ {R} ^ {*}) - K _ {B} (N _ {B} ^ {*}) ] + w [ \xi_ {R} (N _ {R} ^ {*}) - \xi_ {B} (N _ {B} ^ {*}) ], \text {   where   } \xi_ {R} (N _ {R} ^ {*}) > \xi_ {B} (N _ {B} ^ {*}) \\ \Delta \pi_ {O, B} = \Delta K + w \Delta S. \end{array}\tag{A.17}
$$

While the pro<sup>fi</sup>t change of the supplier (S) is:

$$
\begin{array}{l} \Delta \pi_ {S, B} = (w - c) \xi_ {B} (N _ {B} ^ {*}) - (w - c) \xi_ {R} (N _ {R} ^ {*}), \text {   where   } \xi_ {R} (N _ {R} ^ {*}) > \xi_ {B} (N _ {B} ^ {*}) \\ \Delta \pi_ {S, B} = (w - c) [ \xi_ {B} (N _ {B} ^ {*}) - \xi_ {R} (N _ {R} ^ {*}) ] \\ \Delta \pi_ {S, B} = - (w - c) \Delta S. \end{array}\tag{A.18}
$$

Now, the pro<sup>fi</sup>t change of the entire supply chain (SC) is:

$$
\begin{array}{l} \Delta \pi_ {S C, B} = \Delta K + w \Delta S + [ - (w - c) \Delta S ] \\ \Delta \pi_ {S C, B} = \Delta K + c \Delta S. \end{array}\tag{A.19}
$$

(b) If a surplus sharing (SS) contract is executed in the supply chain, the pro<sup>fi</sup>t change of the health care organization (O) is: Δπ<sup>SS</sup><sub>O;B</sub>   1−f K<sub>R</sub> N-<sub>R</sub> −K<sub>B</sub> N-<sub>B</sub>    w I  ξ<sub>R</sub> N-<sub>R</sub>    −w<sub>S</sub> I  ξ<sub>B</sub> N-<sub>B</sub>

A:20

While the pro<sup>fi</sup>t change of the supplier (S) is:

$$
\begin{array}{l} \Delta \pi_ {S, B} ^ {S S} = f [ K _ {R} (N _ {R} ^ {*}) - K _ {B} (N _ {B} ^ {*}) ] - \{(w - c) [ I + \xi_ {R} (N _ {R} ^ {*}) ] - (w _ {S} - c) [ I + \xi_ {B} (N _ {B} ^ {*}) ] \} \\ \Delta \pi_ {S, B} ^ {S S} = f \Delta K - (w - w _ {s}) I - w \xi_ {R} (N _ {R} ^ {*}) + w _ {S} \xi_ {B} (N _ {B} ^ {*}) + c \Delta S. \end{array}\tag{A.21}
$$

Now the pro<sup>fi</sup>t change of the entire supply chain (SC) is:

$$
\begin{array}{l} \Delta \pi_ {S C, B} ^ {\mathrm{SS}} = (1 - f) \Delta K + (w - w _ {S}) I + w \xi_ {R} (N _ {R} ^ {*}) - w _ {S} \xi_ {B} (N _ {B} ^ {*}) + f \Delta K - (w - w _ {S}) I \\ - w \xi_ {R} (N _ {R} ^ {*}) + w _ {S} \xi_ {B} (N _ {B} ^ {*}) + c \Delta S \\ \Delta \pi_ {S C, B} ^ {\mathrm{SS}} = \Delta K + c \Delta S. \end{array}\tag{A.22}
$$

(Q.E.D.)

(A3). Detailed Proofs of Lemma 3 and Lemma 4:

Proof of Lemma 3. First, from Lemma 2b, we notice that the bar-coding system outperforms the RFID system if and only if Ω>δ. As a result, we have the following:

$$
\Omega > \delta \Longleftrightarrow \alpha_ {R} \sigma_ {R} ^ {\frac {2}{3}} > \alpha_ {B} \sigma_ {B} ^ {\frac {2}{3}} \Longleftrightarrow \rho_ {B / R} <   \tau_ {R / B} ^ {2}.\tag{A.23}
$$

Second, since $T _ { B } > T _ { R }$ and $\sigma _ { R } > \sigma _ { B } ,$ we have $\tau _ { R / B } > 1$ and $\rho _ { B / R } > 1$ . Moreover, we have $\tau _ { R / B } ^ { 2 } { > } \rho _ { B / R } { > } 1$ . Thus, Eq. (A.22) implies the following:

$$
\rho_ {B / R} <   \tau^ {2} _ {R / B} \Rightarrow \Omega > \delta .
$$

(Q.E.D.)

Proof of Lemma 4. Under Scenario 1, the health care organization and the supplier will be bene<sup>fi</sup>ted if $\Delta K { < } 0 \ ( \mathrm { i . e . } \ \Omega { < } \delta )$ and $\Delta S { > } 0 \ ( \mathrm { i } . \mathrm { e } . \ \varOmega { > } \delta )$ respectively and vice versa under Scenario 2.

(Q.E.D.)

## References

[1] P. Abell, Item tracking: myths and realities, RFID Journal (2003) (Available at: http://www.r<sup>fi</sup>djournal.com/article/view/484. Accessed on 30/08/2011).

[2] P. Abell, C. Quirk, ePC/RFID and its imminent effect on the supply chain, in: AMR Research Report, 2003.

[3] A. Atali, H.L. Lee, O. Ozer, If the inventory manager knew: value of RFID under imperfect inventory information, in: Technical Report, Graduate School of Business, Stanford University, 2006.

[4] Ö.E. Çakıcı, H. Groenevelt, A. Seidmann, Using RFID for the management of pharmaceutical inventory-system optimization and shrinkage control, Decision Support Systems 51 (2011) 842–852.

[5] C.C. Chen, R.E. Crandall, Y.C. Yu, Barriers to RFID adoption, in: Proceedings of the 10th Annual conference of Asia-Paci<sup>fi</sup>c Decision Sciences Institute, 2005, Available at: http://iceb.nccu.edu.tw/proceedings/APDSI/2005/SessionIndex/Information%20 Systems/Information%20Systems-02 pdf, Accessed on 20/07/2011

[6] T.M. Choi, Quick response in fashion supply chains with dual information updating, Journal of Industrial and Management Optimization 2 (3) (2006) 255–268.

[7] T.M. Choi, Pre-season stocking and pricing decisions for fashion retailers with multiple information updating, International Journal of Production Economics 106 (1) (2007) 146–170.

[8] T.M. Choi, C.H. Chiu, C.K.M. To, A fast fashion safety <sup>fi</sup>rst inventory model, Textile Research Journal 81 (8) (2010) 819–826.

[9] B. Chowdhury, M.U. Chowdhury, C. D'Souza, Challenges relating to RFID implementation within the electronic supply chain management—a practical

approach, Software Engineering, Arti<sup>fi</sup>cial Intelligence, Networking and Parallel/Distributed Computing 149 (2008) 49–59.

[10] J. Collins, Marks and Spencer to extend trial to 53 stores, RFID Journal (2006) (Available at: www.r<sup>fi</sup>djournal.com/article/articleprint/1412/-1/1. Accessed on 27/07/2011).

[11] J.M. Corchado, J. Bajo, Y. de Paz, D.I. Tapia, Intelligent environment for monitoring Alzheimer patients, agent technology for healthcare, Decision Support Systems 44 (2) (2008) 382–396.

[12] N. DeHoratius, A.J. Mersereau, L. Schrage, Retail inventory management when records are inaccurate, Manufacturing and Service Operations Management 10 (2) (2008) 257–277.

[13] R. Derakhshan, M. Orlowska, X. Li, RFID data management: challenges and opportunities, IEEE International Conference on RFID Gaylord Texan Resort (2007) 175–182.

[14] M. Fisher, A. Raman, Reducing the cost of demand uncertainty through accurate response to early sales Operations Research 44 (1) (1996) 87-99

[15] E. Fleisch, C. Tellkamp, Inventory inaccuracy and supply chain performance: a simulation study of a retail supply chain, International Journal of Production Economics 95 (3) (2005) 373–385.

[16] C. Floerkemeier, M. Lampe, Issues with RFID usage in ubiquitous computing applications, in: Pervasive Computing: Second International Conference, PERVASIVE, 2004.

[17] G.M. Gaukler, R.W. Seifert, W.H. Hausman, Item-level RFID in the retail supply chain, Production and Operations Management 16 (1) (2007) 65–76.

[18] C. Goebel, O. Gunther, The information value of item-level, in: Proceedings of the 44th Hawaii International Conference on System Sciences (HICSS), 2011, pp. 1–10.

[19] D. Iglehart, R. Morey, Inventory systems with imperfect asset information, Management Science 18 (8) (1972) 388–394.

[20] S.R. Jeffery, M. Garofalakis, M.J. Franklin, Adaptive cleaning for RFID data streams, in: Proceedings of the 32nd International Conference on Very Large Data Bases, 2006, pp. 163–174.

[21] Y. Kang, S.B. Gershwin, Information inaccuracy in inventory systems—stock loss and stockout, IIE Transactions 37 (2005) 843–859.

[22] A.G. Kok, K.H. Shang, Inspection and replenishment policies for systems with inventory record inaccuracy, Manufacturing and Service Operations Management 9 (2) (2007) 185–205.

[23] A.G.D. Kok, K.H.V. Donselaar, T.V. Woensel, A break-even analysis of RFID technology for inventory sensitive to shrinkage, International Journal of Production Economics 112 (2) (2008) 521–531.

[24] H. Lee, O. Ozer, Unlocking the value of RFID, Production and Operations Management 16 (1) (2007) 40–64.

[25] Y.Y. Leung, F. Cheng, Y.M. Lee, J.J. Hennessy, A tool set for exploring the value of RFID in a supply chain, Springer Series in Advanced Manufacturing, 2007.

[26] H. Mattila, R. King, N. Ojala, Retail performance measures for seasonal fashion, Journal of Fashion Marketing and Management 6 (4) (2002) 340–351.

[27] Y. Meiller, S. Bureau, W. Zhou, S. Piramuthu, Adaptive knowledge based system for health care applications with RFID-generated information, Decision Support Systems 51 (1) (2011) 198–207.

[28] K. Michael, L. McCathie, The pros and cons of RFID in supply chain management, in: Proceedings of the IEEE International Conference on Mobile Business, 2005, pp. 623–629.

[29] M.C. O' Connor, RFID tidies up distribution of hospital scrubs, RFID Journal (2007) (Available at: http://www.r<sup>fi</sup>djournal.com/article/view/3022. Accessed on 21/07/2011).

[30] K. Ohashi, S. Ota, H. Tanaka, L. Ohno-Machado, Comparison of RFID systems for tracking clinical interventions at the bedside, in: AMIA Annual Symposium Proceedings, 2008, pp. 525–529.

[31] M. Roberti, Wal-Mart suppliers discuss RFID, RFID Journal (2004) (Available at: http://www.r<sup>fi</sup>djournal.com/article/view/956. Accessed on 30/08/2011).

[32] E. Sahin, Y. Dallery, Assessing the impact of inventory inaccuracies within a newsvendor framework, European Journal of Operational Research 197 (2009) 1108–1118.

[33] A. Sarac, N. Absi, S. Dauzere-Peres, A simulation approach to evaluate the impact of introducing RFID technologies in a three-level supply chain, in: Proceedings of the 40th Conference on Winter Simulation, 2008, pp. 2741–2749.

[34] Y.J. Tu, S. Piramuthu, Reducing false reads in RFID-embedded supply chains, Journal of theoretical and Applied Electronic Commerce Research 3 (2) (2008) 60–70.

[35] Y.J. Tu, W. Zhou, S. Piramuthu, Identifying RFID-embedded objects in pervasive healthcare applications, Decision Support Systems 46 (2) (2009) 586–593.

[36] C. Uckun, F. Karaesmen, S. Savas, Investment in improved inventory accuracy in a decentralized supply chain, International Journal of Production Economics 113 (2008) 546–566

[37] A.M. Vilamovska, E. Hatziandreu, H.R. Schindler, C. Van Oranje-Nassau, H. de Vries, J. Krapels, Study on the requirements and options for RFID application in healthcare, RAND Corporation, 2009. (Available at: http://www.rand.org/pubs/ technical\_reports/2009/RAND\_TR608.sum.pdf. Accessed on 23/07/2011).

[38] R. Weinstein, RFID: a technical overview and its application to the enterprise, IT Professional 7 (3) (2005) 27–33.

[39] R. Wessel, German hospital expands bed—tagging project, RFID Journal (2007) (Available at: http://www.rfidiournal.com/article/view/3719/1. Accessed on 23/07/2011).

[40] G.R.T. White, G. Gardiner, G. Prabhakar, A.A. Razak, A comparison of barcoding and RFID technologies in practice, Journal of Information, Information Technology, and Organizations 2 (2007) 119–132.

[41] W. Yao, C.H. Chu, Z. Li, The use of RFID in healthcare: bene<sup>fi</sup>ts and barriers, The IEEE International Conference on RFID-Technology and Applications (2010) 128–134.

![](/api/attachments/GNZGZE86/fulltext/images/bb1f12d2cd6b6f7c4f2819466b7e9db8e56dd7c6b4340d0af88e74b2caa7fa5b.jpg)

![](/api/attachments/GNZGZE86/fulltext/images/f646cd495209b229b5a570fdea84830a600d9b17ec72d6c4eeb5f04f526d5c81.jpg)

Hau-Ling Chan is currently a PhD student at The Hong Kong Polytechnic University. Her current research interest focuses on logistics and supply chain management problems related to health care apparel. She has published papers in Decision Support Systems, and IEEE-IEEM International Conference Proceedings in Hong Kong, 2012.

Tsan-Ming Choi is currently an associate professor at The Hong Kong Polytechnic University. His current research interests mainly focus on information systems and supply chain operations management. He has published extensively in leading academic journals such as Automatica, Decision Sup port Systems, IEEE Transactions on Automatic Control, Production and Operations Management, and several other leading IEEE Transactions. He authored/edited ten research handbooks and ten special issues in academic journals. He is now an area editor/associate editor/guest editor of Decision Support Systems, European Management Journal, IEEE Transactions on Systems, Man, and Cybernetics—Part A, Information Sciences, Production and Operations Management, and various operations management/information systems journals.

![](/api/attachments/GNZGZE86/fulltext/images/24ca9cf0ca1cb494c9585dfbec15945737bc608447901c8867513117c50fde78.jpg)

Chi-Leung Hui gained an MSc in Technological Economics from the University of Stirling, UK in 1988, an MSc in Information Systems from the Hong Kong Polytechnic in 1992, an MSc (Eng.) in Computers in Manufacturing from the University of Hong Kong in 1995, a PhD from The Hong Kong Polytechnic University in 1999, a LLB (Hons) from the University of Wolverhampton, UK in 2004, an LLM degree in information technology and intellectual property law from the University of Hong Kong in 2008, and Diploma in Marketing from the Chartered Institute of Marketing, UK, in 1988 and the Certi<sup>fi</sup>ed Diploma in Finance and Accounting from The Chartered Association of Certi<sup>fi</sup>ed Accountants, UK, in 1991. He is a Chartered Engineer and is a chartered member of both the British Computer Society and the

Chartered Institute of Marketing. He has published over 50 refereed papers in journals such as Computers in Industry, IEEE Transactions on Engineering Management and IEEE Transactions on Systems, Man and Cybernetics—Parts A & C, and international conferences Dr Hui is an assistant professor at the Hong Kong Polytechnic University
