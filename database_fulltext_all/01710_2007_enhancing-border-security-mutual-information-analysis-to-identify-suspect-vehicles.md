---
otero_id: 1710
otero_key: "J3H7ETNH"
title: "Enhancing border security: Mutual information analysis to identify suspect vehicles"
authors: "Siddharth Kaza; Yuan Wang; Hsinchun Chen"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.09.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Enhancing border security: Mutual information analysis to identify suspect vehicles

Siddharth Kaza <sup>a,⁎</sup>, Yuan Wang <sup>b</sup>, Hsinchun Chen

<sup>a</sup> Department of Management Information Systems, Eller College of Management, The University of Arizona, Tucson, AZ 85721, United States <sup>b</sup> Department of Economics, Eller College of Management, University of Arizona, Tucson, AZ 85721, United States

Received 14 March 2006; received in revised form 25 July 2006; accepted 3 September 2006 Available online 19 October 2006

## Abstract

In recent years border safety has been identified as a critical part of homeland security. The Department of Homeland Security searches vehicles entering the country for drugs and other contraband. Customs and Border Protection (CBP) agents believe that such vehicles operate in groups and if the criminal links of one vehicle are known then their border crossing patterns can be used to identify other partner vehicles. We perform this association analysis by using mutual information (MI) to identify pairs of vehicles that may be involved in criminal activity. CBP agents also suggest that criminal vehicles may cross at certain times or ports to try and evade inspection. We propose to modify the MI formulation to include these heuristics by using law enforcement data from border-area jurisdictions. Statistical tests and selected cases judged by domain experts show that modified MI performs significantly better than classical MI in identifying potentially criminal vehicles. © 2006 Elsevier B.V. All rights reserved

Keywords: Mutual information; Border safety; Intelligence and security informatic

## 1. Introduction

In recent years border safety has been identified as a critical part of homeland security. The national strategy for homeland security [20] calls for the creation of “smart borders” that provide “greater security through better intelligence, coordinated national efforts, and unprecedented international cooperation against the threats posed by terrorists, the implements of terrorism, international organized crime, illegal drugs, illegal migrants, cyber crime, and the destruction of natural resources.” In addition, the report also emphasizes that information sharing systems are the foundations to improve the nation's security infrastructure.

The Department of Homeland Security (DHS) monitors vehicles entering and leaving the country, recording their license plates with a date and time of crossing using license plate readers. Customs and Border Protection (CBP) agents search vehicles for drugs and other contraband. Thorough checks are done for vehicles on watch lists (known as target/suspect vehicles) and on random vehicles as well. This process is time consuming and if the waiting times become too long, the flow of people, vehicles, and commerce is impaired. So agents at the border are under pressure to balance security needs with operational efficiency.

CBP field agents and analysts believe that vehicles involved in illegal activity (especially smuggling) operate in groups. When one vehicle approaches the check-point, the others wait and join the line only if the vehicle crosses into the U.S. successfully. This ensures that the others can turn back if the vehicle before them is inspected and caught. If the criminal links of one vehicle in a group are known, then the group's crossing patterns and frequency can be used to identify other partner vehicles. Domain experts also suggest that frequently crossing vehicle pairs become interesting only if one (or both) of the vehicles has a criminal history. So, law enforcement data can be used as a good anchor to perform such analysis and identify quality target vehicles. In a previous study [18] we found that criminal associations of vehicles crossing the border may be recorded in local law enforcement databases in borderarea jurisdictions. However, CBP does not always have access to criminal records of vehicles and sometimes lacks the methods to efficiently perform such analysis on millions of crossing vehicles.

We perform this association analysis by using mutual information (MI) to identify pairs of vehicles crossing together and potentially involved in criminal activity. In initial experiments [13] we had found that the use of MI was a promising solution to this problem. In this paper we perform a comprehensive evaluation of MI in this problem domain and also modify the MI formulation to incorporate domain heuristics. Domain experts (CBP agents, police detectives and analysts) and our previous study [14] suggest that groups of criminal vehicles may cross at certain times during the day or cross at different ports of entry to try and evade inspection. It is difficult to identify these heuristics with border crossing information alone since it does not contain clear indications of criminal history or possible intent. We use law enforcement information from border-area jurisdictions to identify times and ports that criminal vehicles prefer and incorporate this knowledge in the MI formulation. The new formulations are likely to help CBP agents identify better quality target vehicles more efficiently.

This study attempts to answer the following questions:

• Can law enforcement information from border-area jurisdictions be used to identify suspect vehicles at the border?

• How can domain heuristics be incorporated to enhance the performance of mutual information?

• Which domain heuristics are important in identifying target vehicles at the border?

In the next section we discuss background information and previous studies using mutual information. Section 3 presents the research testbed and explains the research design. Experimental results are shown and discussed in Section 4. Section 5 concludes and presents future directions.

## 2. Related work

In this section we review previous studies that have used association mining and mutual information in various domains.

## 2.1. Association rule mining

Inferring associations between items in a database was motivated by decision support problems faced by retail organizations [23]. Retail stores needed information on which items their customers were likely to buy together. The problem spawned a method in data mining known as association rule mining. An association rule is a relationship of the form $A \longrightarrow B ,$ where A is the antecedent item-set and B is the consequent item-set. The antecedent and consequent item-sets can contain multiple items. A → B holds in a transaction set T with confidence ‘c’ if c% of transactions in T that contain A, also contain B. A → B holds with support $\cdot _ { s } ,$ if $s \%$ of transactions in T contain both A and B. To find associations between two item-sets, the association mining procedures identify all relationships (rules) that have support and confidence greater than user-specified thresholds.

Association rule mining has been applied in many domains including ‘market basket’ data [2,1], web log analysis (to identify online user behavior) [19], network intrusion detection [15], gene regulatory network extraction (to identify cause–effect relationships between genes) [4], recommender systems (for predicting future purchases) [16] and law enforcement [5]. Some previous studies [10,12] have also included domain heuristics in association rule mining. Hilderman et al. [10] suggested new item-set measures to replace the commonly used support measure. They contend that the new measures were more practical and useful for market basket analysis. Huang et al. [12] modified association rule mining to extract large scale gene regulatory networks.

## 2.2. Mutual information

Mutual information is an information theoretic measure that can be used to identify interesting cooccurrences of objects. It can be considered a subset of association rule mining with 1-item antecedent and 1-item consequent item-sets. There are other more general forms of MI that include multiple item antecedent and consequent item-sets, however in this study we employ the more commonly used classical MI formulation. The earliest definitions of MI were given by Claude and Weaver [7] and Fano [8]. It was defined as the amount of information provided by the occurrence of an event ( y) about the occurrence of another event (x). They formulated it as:

$$
I (x; y) = \log_ {2} {\frac {P (x , y)}{P (x) P (y)}}
$$

Intuitively, this concept measures if the co-occurrence of x and $y ~ ( P ( x , y ) )$ is more likely than their independent occurrences $( P ( x ) . P ( y ) )$ . This formula is referred to as the classical mutual information in the rest of the paper.

The MI measure has been applied to problems in many domains. It works well for phrase extraction from text documents. This is because text documents can be considered as a set of events (words), and the probability of the occurrence of a word can be calculated over the entire document. Previous studies in this area have used MI to study association between words in English texts and identify commonly occurring phrases [6,11]. It has also been used for key phrase extraction from Chinese texts [21].

Pantel et al. [22] did a novel study where they used MI to match database columns containing similar information. They found that their SIfT model which was based on MI performed well in identifying schema correspondences across comparable datasets. In the bioinformatics domain, MI has been used to extract protein motif patterns from sequences [24] and identify building blocks of proteins from biomedical abstracts [25]. Mutual information scores have also been used for feature selection. Battiti [3] used MI to select features in supervised neural network learning.

Work on extending or modifying the classical MI measure to add domain heuristics includes studies in natural language processing: Magerman and Marcus [17] modified the MI measure (bi-gram) to include n-grams, bioinformatics: Wren [26] extended the measure to calculate transitive MI scores for biological associations, and feature selection: Fleuret [9] used conditional MI to identify important features for image classification.

Border crossing records can be considered as a stream of text (license plates) ordered by the time of crossing. So, MI can be used to identify frequent cooccurrence between a pair of vehicle crossings. If one vehicle in the pair has a criminal record, some inferences may be made about the second vehicle if they cross together frequently. In a previous study [13] we found that the time and port of crossing may be important heuristics for improving the performance of MI in this problem domain. We propose to use conditional probability to include these domain heuristics in the MI formulation (Section 3.2.5).

## 3. Research testbed and design

## 3.1. Testbed

The testbed for this study includes datasets obtained from various law enforcement agencies in the Tucson, AZ metropolitan region. These agencies include the Tucson Police Department (TPD), Pima County Sheriff's Department (PCSD), and many other smaller police agencies in the area. Data from these agencies is referred to as police data through this paper. In addition, the study also uses data from the Tucson Customs and Border Protection (CBP). These datasets were provided to us through the BorderSafe project funded by the Department of Homeland Security. The TPD and PCSD datasets include information on police incidents over 16 years (1990–2005). The incidents include information on individuals and vehicles that are involved in illegal activity in southern Arizona. Some key statistics of these datasets is shown in Table 1.

CBP data includes information on vehicles crossing the border between Arizona and Mexico at six ports of entry. This data includes the license plate, state, date, port, and time for non-commercial vehicle crossings from March 2004 to October 2005. Details of this dataset are shown in Table 2.

## 3.2. Research design

Prior to presenting the research design we first define the terms criminal vehicle and police contact. A criminal vehicle is a vehicle that has been suspected, arrested, impounded, or has a warrant (with its occupant) for crimes that include narcotics (sale, possession, etc.), violence (homicide, aggravated assault, armed robbery, etc.), larceny and theft (property, vehicles, etc.), and other serious crimes in the Tucson metropolitan region. Police detectives and analysts consider these crimes and roles (suspect, arrestee) as strong indications of involvement in criminal activity. A vehicle with a police contact is one that is recorded in the law enforcement databases; this may be for serious crimes (as listed above) or for other activities that may include forgery and counterfeiting, suspicious activity, and others. Vehicles with police contacts are also referred to as potentially criminal vehicles in this paper. These definitions are used in the description of the design and the evaluation process.

Key statistics of data from agencies in the Tucson metropolitan region

<table><tr><td></td><td>TPD</td><td>PCSD</td><td>Others</td></tr><tr><td>Date range</td><td>1990–2005</td><td>1990–2005</td><td>1990–2005</td></tr><tr><td>Vehicles</td><td>629,039</td><td>614,455</td><td>456,832</td></tr></table>

Table 2  
Key statistics of CBP border crossing data

<table><tr><td>Date range</td><td>2004–2005</td></tr><tr><td>Recorded crossings</td><td>11 million</td></tr><tr><td>Number of vehicles</td><td>2 million</td></tr></table>

Motivation for heuristic selection - CBP agents check all vehicles entering the U.S. at various ports of entry. Majority of the vehicles are subjected to ‘primary checking’ which includes verifying the admissibility of the occupants and some checks for obvious presence of contraband. Primary checking usually takes between 1– 2 min. In addition to primary checking, some vehicles with alerts on them are assigned to ‘secondary checking which includes a thorough check of the vehicle and an interview of the passengers that may take 10 min or longer. The vehicles that are selected for secondary checking are referred to as target vehicles in this study. The target vehicles are selected based on various criteria. These include vehicle alerts from federal systems like FBI's NCIC (National Crime Information Center), random selection, and prior knowledge and intuition of CBP agents. As mentioned before, CBP agents believe that vehicles involved in cross border crime operate in groups. These vehicles look out for each other and cross frequently within a small time frame.

To identify interesting pairs of vehicles that cross the border together we use the time of crossing and the port of crossing as heuristics to enhance mutual information. The time of crossing heuristic suggests that vehicle pairs that cross during certain times of the day or night are more interesting than others. Domain experts and our previous study [13] suggest that criminal vehicles regularly cross at odd times during the night to exploit the cover of darkness. The port of crossing heuristic suggests that vehicle pairs that cross at certain ports of entry are more interesting than others. This is because criminal vehicles tend to use ports that are in areas that are desolated, near areas where contraband can be easily disposed of, or areas that are not under the radar of border patrol and CBP agents. It can be seen that both these heuristics are fluid in nature, i.e., criminal vehicles may change their time and port of crossing according to the current situation in enforcement. The mutual information measure modified to include the time heuristic is referred to as ‘MIT’ (Eq. (2), shown in Section 3.2.5), port heuristic is referred to as $^ { \circ } M I P ^ { \prime }$ (Eq. (3), shown in Section 3.2.5) and classical mutual information (without heuristics) is referred to as $\mathbf { \nabla } ^ { 6 } M I C ^ { \mathbf { \xi } }$ (Eq. (1), shown in Section 3.2.4).

Research design and process - Fig. 1 shows the research design and the process of utilizing information from multiple sources, heuristic calculation, and identification of potential target vehicles at the border. Different parts of the figure are explained in the following sub-sections.

## 3.2.1. Training dataset and heuristic calculation

The TPD, PCSD, and other police agency datasets were consolidated by transforming them to a single schema [18]. This was done to simplify access to multiple sources of information. The common schema contained information on all vehicles that had police contacts along with information on the incidents that they were involved in. To evaluate the performance of MIT, MIP, and MIC, the CBP border crossing records were divided into training and testing datasets. This was done using a 2/3–1/3 hold out procedure. The training dataset contained 7.4 million (≈2/3 of total) crossing records from March 2004 to November 2004.

![](/api/attachments/J3H7ETNH/fulltext/images/e31e64420b5c2a8971236258600d085c2dfedd05f8eff2bddc352aa0e4b5047e.jpg)  
Fig. 1. Research design and process.

To calculate the time heuristic the day was divided into six time periods corresponding to office travel (5 am–10 am), travel for lunch (10 am–2 am), night time (8 pm–12 pm, 12 pm–5 am), and others. These time periods were defined with the help of domain experts. For each of these time periods the ratio of vehicles with police contacts to the total number of crossings was calculated. This value was used to inform the mutual information score between vehicles in a given time period (as shown in Section 3.2.5).

The port heuristic was calculated in a similar fashion. For each of the six ports the ratio of vehicles with police contacts to the total number of crossings was calculated. This value was used to inform the mutual information score between vehicles crossing at a given port (as shown in Section 3.2.5).

## 3.2.2. Testing dataset

The testing data contained 3.6 million (≈1/3 of total) crossings from November 2004 to October 2005. Police data and the border crossings in the testing dataset were used to identify two sets of vehicles:

Set A 251 criminal vehicles that had been arrested or suspected for narcotics sale in the Tucson metropolitan region since January 2003.

Set B All the border crossing vehicles crossing within 1 h of each vehicle in Set A at the same port and in the same direction (i.e., both vehicles are either entering the U.S. or exiting it).

MIT, MIP, and MIC were calculated between paired vehicles in Set A and Set B. The vehicle pairs with high scores were considered potential target vehicles.

## 3.2.3. Evaluation procedure

The potential target vehicles identified were evaluated by measuring their overlap with police datasets. This was done by measuring the number of vehicles with police contacts that were contained in the set of potential target vehicles. The overlap with three different datasets was measured: TPD dataset, PCSD dataset, and the entire Tucson metropolitan region (that includes TPD and PCSD) dataset. This was done since each of these datasets cover different geographical areas and record different levels of crimes. It also gives us a greater insight into the criminal operations of border crossing vehicles. The number of potentially criminal vehicles (vehicles with police contacts) identified by MIT, MIP, and MIC were compared to each other to ascertain the performance of the modified measures. Since the aim of CBP is to target potentially criminal vehicles, a greater number of such vehicles in the target vehicle set indicate a higher quality result. In addition to statistical tests, selected cases judged by domain experts were also used in the comparison. The illustrative cases included a detailed evaluation of the criminal links of target vehicle pairs identified by the three measures.

## 3.2.4. Classical mutual information (MIC) formulation

The classical mutual information score between any two vehicles is defined as:

$$
\operatorname{MIC} (A, B) = \log_ {2} \frac {P (A , B)}{P (A) P (B)}\tag{1}
$$

Here A is a vehicle in Set A, and B is a vehicle in Set B. $P ( A )$ and $P ( B )$ are the probabilities of the vehicles A and B crossing the border, these are calculated from the border crossing datasets. $P ( A , B )$ is the probability of B crossing within 1 h of A, this is calculated based on the number of times A and B are seen crossing together.

## 3.2.5. Modified mutual information with time heuristics (MIT) and port heuristics (MIP)

In the MIT and MIP formulation, we use conditional probability to modify the definition of $P ( A ) , P ( B )$ , and $P ( A , B )$ .

$P ^ { \prime } ( A )$ Probability that vehicle A crosses the border and has a police contact.

$P ^ { \prime } ( B )$ Probability that vehicle B crosses the border and has a police contact.

$P ^ { \prime } ( A , B )$ Probability that vehicles A and B cross the border together and have police contacts.

Thus, a high $\mathrm { M I ^ { \prime } } ( A , B )$ (based on Eq. (1)) indicates that the vehicles are likely to cross the border and potentially commit crimes together.

Given this, we can now modify the classical MI formulation to include the time heuristic: Let $P _ { \mathrm { c } } ( a )$ be the probability that vehicle $\cdot _ { a } ,$ has contact with the police, and $P _ { \mathrm { b } } ( a )$ be the probability that $\cdot _ { a } ,$ crosses the border. The probability of vehicles with police contacts crossing during the six time periods is calculated using historical information in the police databases. So, we can obtain $P _ { \mathrm { c } } ( V | t )$ , which is the probability that any vehicle V in time period $t \left( 1 \leq t \leq 6 \right)$ will have a contact with the police.

Now, by definition of $P ^ { \prime } ( A )$ ,

$$
P ^ {\prime} (A) = \sum_ {t = 1} ^ {6} P [ (A _ {\mathrm{b}} \text {   and   } A _ {\mathrm{c}}) | t ]
$$

In the above equation $A _ { \mathrm { b } }$ refers to vehicle A crossing the border, and $A _ { \mathrm { c } }$ refers to vehicle A having contact with the police. This is summed over all six time periods to obtain $P ^ { \prime } ( A )$ . The equation reduces to

$$
P ^ {\prime} (A) = \sum_ {t = 1} ^ {6} P _ {\mathrm{b}} (A | t) P _ {\mathrm{c}} (V | t)
$$

since the probability of a vehicle crossing the border and having police contact are independent (so they are multiplied to obtain $P ^ { \prime } ( A ) )$ . In addition, A is replaced by V in the second term since the probability that a vehicle in time period t has a police contact is the same for all vehicles in that time period. So basically the above process utilizes historical information (about crime) in the police datasets as a weight to modify $P ^ { \prime } ( A )$ . Similar derivations can be used to obtain $P ^ { \prime } ( B ) , \ P ^ { \prime } ( A , B )$ , and thus MIT(A,B) as shown in the following equations:

$$
P ^ {\prime} (B) = \sum_ {t = 1} ^ {6} P [ (B _ {\mathrm{b}} \text {   and   } B _ {\mathrm{c}}) | t ] = \sum_ {t = 1} ^ {6} P _ {\mathrm{b}} (B | t) P _ {\mathrm{c}} (V | t)
$$

$$
\begin{array}{r l} P ^ {\prime} (A, B) & = \sum_ {t = 1} ^ {6} P [ ((A B) _ {\mathrm{b}} \text {   and   } (A B) _ {\mathrm{c}}) | t ] \\ & = \sum_ {t = 1} ^ {6} P _ {\mathrm{b}} ((A B) | t) P _ {\mathrm{c}} (V | t) P _ {\mathrm{c}} (V | t) \end{array}
$$

$$
\operatorname{MIT} (A, B) = \log_ {2} \frac {P ^ {\prime} (A , B)}{P ^ {\prime} (A) P ^ {\prime} (B)}\tag{2}
$$

A similar derivation can be used to obtain MIP as follows:

$$
\begin{array}{l} P ^ {\prime} (A) = \sum_ {p = 1} ^ {6} P _ {\mathrm{b}} (A | p) P _ {\mathrm{c}} (V | p) \\ P ^ {\prime} (B) = \sum_ {p = 1} ^ {6} P _ {\mathrm{b}} (B | p) P _ {\mathrm{c}} (V | p) \\ P ^ {\prime} (A, B) = \sum_ {p = 1} ^ {6} P _ {\mathrm{b}} ((A B) | p) P _ {\mathrm{c}} (V | p) P _ {\mathrm{c}} (V | p) \end{array}
$$

$$
\operatorname{MIP} (A, B) = \log_ {2} \frac {P ^ {\prime} (A , B)}{P ^ {\prime} (A) P ^ {\prime} (B)}\tag{3}
$$

In the above equations $p \left( 1 \leq p \leq 6 \right)$ represents the six ports of entry.

As mentioned before, the time and port heuristics are fluid in nature. An advantage of using conditional probability to include these heuristics is that the weight assigned to times and ports adjust to the changing nature of data. So, if criminals start moving operations from one port to another, the heuristics will automatically adjust to reflect the situation.

## 3.2.6. Hypotheses

The following hypotheses were tested in this study:

H1. Mutual information modified to include the time heuristic will perform significantly better than classical mutual information in identifying potentially criminal vehicles.

H2. Mutual information modified to include the port heuristic will perform significantly better than classical mutual information in identifying potentially criminal vehicles.

No hypothesis on the comparative performance of MIT and MIP was proposed since prior to this study we had no evidence on any one of them performing better.

## 4. Experimental results

To ascertain whether law enforcement information can be used to identify potential criminal vehicles, we first measured the overlap between border crossing vehicles and police records in border-area jurisdictions. There were 66,185 border crossing vehicles that had police incident records in Tucson metropolitan area datasets. The number suggests that many vehicles crossing the border have incidents recorded in local law enforcement databases. This is a positive sign since it allows us to identify target vehicles at the border by exploring their criminal links. The existence of an overlap is also important for the calculation of heuristics based on law enforcement information.

4.1. Temporal patterns and port distribution of border crossings

Studying the temporal patterns and port distributions of border crossings helps better understand the crossing activity. Fig. 2(a) shows the time distribution of border crossings for all vehicles entering and leaving the country over six time periods. Each slice of the pie shows the percentage of all the border crossings (11 million) that take place in the respective time period. It can be seen that a majority (about 65%) of border crossings occur due to work and lunch/dinner related traffic during working hours (approximately 6 am–8 pm). Domain experts suggest that these are the busiest periods for land borders in the southwest with Mexican citizens and students entering the U.S. and returning to Mexico for lunch. The chart also shows that about 37% of all crossings take place during the night or after dark (approximately 7 pm–6 am).

![](/api/attachments/J3H7ETNH/fulltext/images/55cfbf90ecdbbc88f7f8f6c2ce744dff9d1decdd59fb560536ae88a754662aec.jpg)

![](/api/attachments/J3H7ETNH/fulltext/images/8086a17d48ba95c4a8197f5bda3e1813097da9d7ddca88bf6ab0dad73c192dfe.jpg)  
Fig. 2. Temporal distribution of crossings — (a) percentage of total crossings (b) percentage of crossings with police contacts.

Fig. 2(b) shows the time distribution of border crossings by vehicles with police contacts. Each slice of the pie shows the percentage of all crossings by such vehicles that took place in that respective time-period. For instance, 27% of all the border crossings by police contact vehicles took place between 8 pm and midnight. The chart suggests that a large percentage (about 48%) of crossings by these vehicles take place after dark. This is probably because there is less enforcement at ports at nighttime (many vehicle lanes are closed) and it is also easier to rendezvous with other criminal elements at both sides of border under the cover of darkness. This heuristic is used to inform the mutual information algorithm. MIT incorporates this information to assign more weight to time periods with high percentage of crossings by vehicles with police contacts. The weights also discount work travel related periods since they have a lower percentage of such crossings. Such information can also be used by CBP to increase or decrease enforcement in certain time periods.

Fig. 3(a) shows the number of crossings that take place at each of the six ports over a 12 month period. It can be seen that Port D and Port F (we hide the actual names for security reasons) are the biggest ports in Arizona. Port E is the smallest port with the lowest number of crossings. Port E was also found to have limited operating hours. Fig. 3(b) shows the percentage of crossings at each port which involved vehicles that had police contacts. For instance, 2.61% of the 1.47 million crossings at Port A were by vehicles that had police contacts. It can be seen that even though Port E is by far the smallest port (with 0.003% of total crossings),

9.9% of the crossings at that port have had previous contact with the police (this is significantly larger than any other port). This fact confirms suspicions of domain experts that this port might be a focus of criminal activity due to its proximity to certain remote areas in Mexico and the U.S. Thus, in identifying target vehicles for inspection at the border, it would be probably beneficial to target more vehicles at Port E. These important heuristics are incorporated into the MIP formulation described in Section 3.2.5.

## 4.2. Comparative evaluation of MIT, MIP, and MIC

Mutual information scores (MIT, MIP, and MIC) were calculated for 410,079 pairs of vehicles (the first vehicle from Set A and the second from Set B). To statistically compare the three measures, the number of police contact vehicles in Set B identified by each was counted.

![](/api/attachments/J3H7ETNH/fulltext/images/f73c535534f7beb43b74404a0eeabb874d01eee9b0e6e267966ea1a25fd49555.jpg)

![](/api/attachments/J3H7ETNH/fulltext/images/32e3d0cb1b332003edebc62db4da718520b123355d960f37c43ece7c932ac825.jpg)  
Fig. 3. Port distribution of crossings — (a) total crossings (b) percentage of crossings with police contacts.

This was done for all three police datasets as discussed in Section 3.2.3. The results are shown in Fig. 4.

On the X-axis are top-n pairs (n ranging from 10– 2500) of vehicles ordered by their MIT, MIP, and MIC scores. On the Y-axis is the number of vehicles with police contacts identified by the three measures. For instance, in Fig. 4(c), fourteen vehicles of the top-100 vehicles identified by MIP had previous police contacts. As can be seen in all three graphs, both MIT and MIP consistently identified more potentially criminal vehicles (vehicles with prior police contacts) than MIC. MIP also identified more potentially criminal vehicles than MIT. It is also evident that the illegal activity of border crossing vehicles was higher in the Pima County region as compared to the city of Tucson. In the biggest dataset (Tucson metropolitan region) MIP identified 206 vehicles among the top 2500 pairs that had prior police contacts, i.e., 8.2% of the vehicles identified had police contacts. The average number of border crossing vehicles that have police contacts in the Tucson metropolitan region is 3.3%. Thus, the performance of MIP is better than a random selection of target vehicles from the set of border crossing vehicles. For hypothesis testing, thirty data points (ranging from top 5 to 3500 pairs) were taken for each of the measures and a t-test was done for the differences in the mean number of potentially criminal vehicles identified. Since all the samples had unequal variances, the Smith-Satterthwaite t-test procedure was used. The p-values of the tests are listed in Table 3. It was found that MIT performed significantly better (at 95% level) than MIC in all but one dataset. Thus, the first hypothesis (H1) is partially supported. MIP also performed significantly better than MIC (at 99% level) in identifying potentially criminal vehicles in all datasets. This supports the second hypothesis (H2).

![](/api/attachments/J3H7ETNH/fulltext/images/8bd587c9055a3307946925c5d59e808fab60948d45503f51e260fd45a663e585.jpg)

![](/api/attachments/J3H7ETNH/fulltext/images/573c3d0d690ca0069a617dea8b55a38787cb782ce8ab2866c7f5c31058c92ff1.jpg)

![](/api/attachments/J3H7ETNH/fulltext/images/1a7494272b0bd4072c5ed201b58e7100720419d869298a7eab571e7c06d25ca7.jpg)  
Fig. 4. Number of vehicles with police contacts identified using — (a) TPD dataset (b) PCSD dataset (c) Tucson metropolitan area dataset. On the X axis are the top ‘n’ pairs ordered by mutual information scores.

Table 3  
p values for two sample t-test

<table><tr><td></td><td>MIT-MIC</td><td>MIP-MIC</td></tr><tr><td>PCSD dataset</td><td>0.036</td><td>0.001</td></tr><tr><td>TPD dataset</td><td>0.050</td><td>&lt;0.000</td></tr><tr><td>Tucson met. dataset</td><td>0.106</td><td>0.001</td></tr></table>

Bold values are significant at a 95% or higher level.

Even though the top-n pairs contained many potentially criminal vehicles, they also included many other vehicles that had no past criminal records. This might not look promising in other domains, but has positive connotations in this one. It suggests that many of the vehicles postulated to be potentially criminal by the algorithms were not known to have police records before. So the new measures can be used to identify new potentially criminal vehicles that can be targeted for further inspection at the border. The low number of police contacts might also be a result of properties of the datasets. Most of the border crossing vehicles in our datasets may be headed for Phoenix, AZ and surrounding areas and thus their activity (if any) will be recorded in those police datasets. A more accurate test of the algorithms is possible if those datasets were available.

## 4.3. Selected case studies

The illustrative cases shown here were reviewed and evaluated by domain experts. These and other cases were found to be good candidates for further investigation at the border. Fig. 5 shows the temporal crossing patterns of the vehicle pair (Vehicles A and B) that had the highest MIC score. On the X-axis are the dates when the vehicles were seen crossing together. On the Y-axis are the times of crossing (0–2400).

Vehicle A and its occupant were arrested for a narcotics possession crime in Tucson in 2003. Vehicle A crossed the border within 1 h of Vehicle B fourteen out of a total of thirty times. This activity is considered suspicious by domain experts since both vehicles may be involved in smuggling narcotics across the border. However, on closer examination it can be seen that the times of crossings of both vehicles correspond to a standard morning work schedule. This crossing pattern can be discounted since it is possible that both vehicles may be going for work at almost regular intervals. Since the MIT formulation is informed of these heuristics, it produced better examples.

Fig. 6(a) shows the temporal crossing patterns of a vehicle pair (Vehicles C and D) that received a high MIT score. Vehicle C crossed 51 times in a 7 month period, out of which it crossed 22 times with Vehicle D. As can be seen in the figure, this vehicle pair crossed together frequently, but in addition all the crossings were after dark and did not follow a standard work schedule. This example and other like it show that MIT identifies cases that are more likely to be considered suspicious by domain experts. Since, Vehicles C and D are interesting with respect to the frequency and times of crossing together; we explored their police contacts further. Fig. 6(b) shows the criminal links of Vehicle C and Vehicle D. Vehicle C was found to have strong connections to a narcotics network in the Tucson metropolitan area. It had links to other people and vehicles that had been arrested suspected for narcotics sales and possession in the region. These connections suggested that the vehicle might be an active member of a narcotics sale and smuggling ring. Domain experts also suggested that viewing the vehicles border crossing activity in this context made them a candidate for further investigation. MIT identified many other such examples.

![](/api/attachments/J3H7ETNH/fulltext/images/5e2d459543205c8b7d4d91c57123489816d07b861ca37addd34ab65b820653f2.jpg)  
Fig. 5. A vehicle pair identified by classical mutual information.

![](/api/attachments/J3H7ETNH/fulltext/images/f25f19bcc0fd37598162a4872db79f7fc7275dbb29be37074cd3eb1eaf290970.jpg)

![](/api/attachments/J3H7ETNH/fulltext/images/6ba7a3d62e206f511fa492830768a5419bbdbde111e3f80b205afe6d5b2e4f75.jpg)  
Fig. 6. (a) A vehicle pair identified by mutual information with time heuristics (b) The activity of the vehicles as recorded in Tucson met. area police databases.

Fig. 7(a) shows an example vehicle pair (Vehicles E and F) that received a high MIP score. In a period of 1 month Vehicle E crossed 39 times and Vehicle F crossed 10 times. It can be seen that they did not follow any particular schedule and crossed at all times during the day. They were assigned a high MIP score because they crossed at ports with a high level of criminal activity. A deeper examination into their activity (Fig. 7(b)) shows that they had criminal links recorded in police databases. An experienced police detective classified the links described in the figure as strong criminal links. MIP identified many more such suspicious examples. The above cases show that both MIT and MIP identified more suspicious activity as compared to those identified by MIC.

## 5. Conclusions and future directions

Exploring the criminal links of border crossing vehicles in local law enforcement databases can be used to enhance border security. In this study we used mutual information to identify pairs of border crossing vehicles that may be involved in criminal activity. We found that mutual information can be used to identify high quality potential suspect vehicles that may warrant more inspection at the border. In addition, we concluded that the mutual information measure modified to include domain heuristics like time and port of crossing performs significantly better than classical mutual information in the identification of potentially criminal vehicles. The method can be used to assist Customs and Border Protection agents to perform their functions both effectively and efficiently.

![](/api/attachments/J3H7ETNH/fulltext/images/2089c8703c0bc86edda2726dcd941915460ce304c4fe061e4e402446a2c8740a.jpg)

![](/api/attachments/J3H7ETNH/fulltext/images/8abdd87e648151102e0d71fd74525326eeb7a6d46eac0f5217409c1dd47bb5bb.jpg)  
Fig. 7. (a) A vehicle pair identified by mutual information with port heuristics. The vehicles do not cross with a fixed schedule and cross at all times during the day (b) The activity of the vehicles as recorded in police databases.

In the future, we plan to incorporate other domain heuristics in the mutual information formulation. In addition we plan to modify the formulation to include both the time and port heuristics to enhance the results. We also plan to have domain experts from Customs and Border Protection validate our results and use them in their operations. If validated in the field, then the methodology can be used in other border states and help in enhancing national and international security. Since the methodology is based on information sharing, the results may also encourage law makers to formulate policies to increase cooperation among agencies.

## Acknowledgements

This research was supported in part by the NSF Digital Government (DG) program: “COPLINK Center: Information and Knowledge Management for Law Enforcement” #9983304, NSF Knowledge Discovery and Dissemination (KDD) program: “COPLINK Border Safe Research and Testbed” #9983304, NSF Information Technology Research (ITR) program: “COPLINK Center for Intelligence and Security Informatics Research - A Crime Data Mining Approach to Developing Border Safe Research” #0326348, and Department of Homeland Security (DHS) through the “BorderSafe” initiative #2030002.

We thank our BorderSafe project partners: Tucson Police Department, Pima County Sheriff's Department, Tucson Customs and Border Protection, ARJIS (Automated Regional Justice Information Systems), San Diego Super Computer Center (SDSC), SPAWAR, Department of Homeland Security, and Corporation for National Research Initiatives (CNRI). We also thank Homa Atabakhsh and Hemanth Gowda of the AI Lab at the University of Arizona, Tim Petersen and Chuck Violette of the Tucson Police Department, and Ron Friend of Tucson Customs and Border Protection for their contributions to this research.

## References

[1] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Presented at 20th Int. Conf. Very Large Data Bases, VLDB, 1994.

[2] R. Agrawal, T. Imielinski, A. Swami, Mining association rules between sets of items in large databases, Presented at ACM SIGMOD Conference on Management of Data, New York, 1993.

[3] R. Battiti, Using mutual information for selecting features in supervised neural net learning, IEEE Transactions on Neural Networks 5 (4) (1994).

[4] D. Berrar, W. Dubitzky, M. Granzow, R. Eils, Analysis of gene expression and drug activity data by knowledge-based association mining, Presented at Critical Assessment of Microarray Data Analysis Techniques (CAMDA '01), Berlin, 2001.

[5] D.E. Brown, S. Hagen, Data association methods with applications to law enforcement, Decision Support Systems 34 (4) (2003).

[6] K.W. Chruch, P. Hanks, Word association norms, mutual information, and lexicography, Computational Linguistics 16 (1) (1990).

[7] S. Claude, E. Weaver, The Mathematical Theory of Communi cation, University of Illinois Press, Chicago, 1949.

[8] R.M. Fano, Transmission of Information, MIT Press, Cambridge, MA, 1961.

[9] F. Fleuret, Fast binary feature selection with conditional mutual information, Journal of Machine Learning Research 5 (2004).

[10] R.J. Hilderman, C.L. Carter, H.J. Hamilton, N. Cercone, Mining association rules from market basket data using share measures and characterized itemsets, Presented at Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD 1998), 1998.

[11] D. Hindle, Noun classification from predicate-argument structures, Presented at 28th Conference on Association for Computational Linguistics, 1990.

[12] Z. Huang, J. Li, H. Su, G.S. Watts, H. Chen, Large-scale Regulatory Network Analysis from Microarray Data: Modified Bayesian Network Learning and Association Rule Mining, Decision Support Systems (2006).

[13] S. Kaza, T. Wang, H. Gowda, H. Chen, Target vehicle identification for border safety using mutual information, Presented at 8th International IEEE Conference on Intelligent Transportation Systems, New York, 2005.

[14] S. Kaza, Y. Wang, H. Chen, Target vehicle identification for border safety with modified mutual information, Presented at IEEE International Conference on Intelligence and Security Informatics (ISI), San Diego, CA, 2006.

[15] W. Lee, S.J. Stolfo, Data mining approaches for intrusion detection, Presented at 7th USENIX Security Symposium, 1998.

[16] W. Lin, S.A. Alvarez, C. Ruiz, Efficient adaptive-support association rule mining for recommender systems data, Mining Knowledge Discovery 6 (1) (2002).

[17] D.M. Magerman, M.P. Marcus, Parsing a natural language using mutual information statistics, Presented at Eight National Conference on Artificial Intelligence, Menlo Park, CA, 1990.

[18] B. Marshall, S. Kaza, J. Xu, H. Atabakhsh, T. Petersen, C. Violette, H. Chen, Cross-jurisdictional criminal activity networks to support border and transportation security, Presented at 7th Internationa IEEE Conference on Intelligent Transportation Systems, New York, 2004.

[19] B. Mobasher, N. Jain, E.H. Han, J. Srivastava, Web mining: pattern discovery from world wide web transactions, Technical Report, Department of Computer Science, University of Minnesota, Minneapolis, 1996.

[20] National Strategy for Homeland Security, Office of Homeland Security, 2002.

[21] T. Ong, H. Chen, Updateable PAT-Tree approach to Chinese key phrase extraction using mutual information: a linguistic foundation for knowledge management, Presented at 2nd Asian Digita Library Conference, Taipei, Taiwan, 1999.

[22] P. Pantel, A. Philpot, E. Hovy, Aligning database columns using mutual information, Presented at The 6th National Conference on Digital Government Research (dg.o), Los Angeles, 2005.

[23] M. Stonebraker, R. Agrawal, U. Dayal, E. Neuhold, A. Reuter, The DBMS research at crossroads, Presented at The VLDB Conference, San Francisco, 1993.

[24] T. Tao, C.X. Zhai, X. Lu, H. Fang, A study of statistical methods for function prediction of protein motifs, Applied Bioinformatics 3 (2–3) (2004).

[25] D. Weisser, J. Klein-Seetharaman, Identification of fundamental building blocks in protein sequences using statistical association measures, Presented at ACM Symposium on Applied Computing, Nicosia, Cyprus, 2004.

[26] J.D. Wren, Extending the mutual information measure to rank inferred literature relationships, BMC Bioinformatics 5 (2004).

![](/api/attachments/J3H7ETNH/fulltext/images/148ab661b02a62a61987a196524b82681005ae3b3d31189ea5cd4437578248a6.jpg)

Siddharth Kaza is a doctoral student and research associate of the Artificial Intelligence Lab in the Department of Management Information Systems at the University of Arizona. He earned his M.S. in Computer Science from Central Michigan University and his B.Sc. in Mathematical Sciences from University of Delhi. His research interests include data mining, information integration and social network analysis.

![](/api/attachments/J3H7ETNH/fulltext/images/0e4b3bf39e453f6942586cb5fd99b0dcc62e9c9c6883de2af9405d6523e5168b.jpg)

Yuan Wang is a doctoral student in the Department of Economics at the University of Arizona. He received his B.E. from Harbin Institute of Technology in 2001 and M.S. from Beijing Institute of Technology in 2004. He worked as an intern in Microsoft Research Asia in Summer 2004. His research interests include financial economics, pattern recognition and data mining.

![](/api/attachments/J3H7ETNH/fulltext/images/93ed45156221164241ee2ac4f62bd028c2184214d99f65d61114173e2260eb8b.jpg)

Hsinchun Chen is McClelland Professor of Management Information Systems at the University of Arizona and Andersen Consulting Professor of the Year (1999). He received his BS degree from the National Chiao-Tung University in Taiwan, MBA from the SUNY Buffalo, and PhD degree in Information Systems from New York University. He authored six books and more than 100 SCI journal articles covering intelligence analysis, data/text/web mining, digital library, knowl-

edge management, medical informatics, and Web computing. He is a member of the editorial board of the Journal of the American Society for Information Science and Technology, ACM Transactions on Information Systems, IEEE Transactions on Systems, Man, and Cybernetics, IEEE Transactions on Intelligent Transportation Systems, and Decision Support Systems. Dr. Chen has served as an advisor to the National Science Foundation (NSF), Department of Justice (DOJ), Department of Homeland Security (DHS), NLM, and other international research programs in digital library, digital government, medical informatics, and national security. Dr. Chen is the founding director of the UA Artificial Intelligence Laboratory and Hoffman Ecommerce Laboratory.
