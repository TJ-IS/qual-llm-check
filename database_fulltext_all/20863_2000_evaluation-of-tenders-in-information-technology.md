---
otero_id: 20863
otero_key: "NU65E29E"
title: "Evaluation of tenders in information technology"
authors: "T Rapcsák; Z Sági; T Tóth; L Kétszeri"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00078-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evaluation of tenders in information technology

T. Rapcsak <sup>a,)</sup>, Z. Sagi <sup>a</sup>, T. Toth <sup>a</sup>, L. Ketszeri <sup>b</sup> ´ ´ ´ ´

<sup>a</sup> Department of Operations Research and Decision Systems, Computer and Automation Institute, Hungarian Academy of Sciences, PO Box 63, Budapest H-1513, Hungary

<sup>b</sup> Directorate for Public Procurement and Economic Management, Prime Minister’s Office 1055 Budapest, Kossuth ter 2-4 Hungary ´ Accepted 8 May 2000

## Abstract

Two case studies are described for evaluating tenders in information technology IT in public procurement process basedŽ . on multiattribute group decision models and the software WINGDSS. The given decision methodology is further developed by discussing a method to aggregate scores measured on a scale and price.

In 1997, 17 parallel tenders were handled together, 468 offers were evaluated by eight decision-makers, in two rounds, with respect to 18 and 5–8 criteria, respectively, in 5 days. In 1998, the same problem resulted in 168 offers, which were evaluated in one round by nine decision-makers with respect to 100–150 criteria, in 3 days.

Since 1997, goods worth of 4–5 billion HUF approximately 200–300 million US\$ per year have been purchased withinŽ . the frame of the contracts yielded by the tenders. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Multiattribute group decision problems; Group decision support systems; Tender evaluations

## 1. Introduction

The Parliament of the Republic of Hungary passed a bill in order to rationalize the expenses of public institutions and ensure the equitable, market-based distribution of the governmental orders. The Public Procurement Law No. XL, 1995 came into force onŽ . November 1, 1995.

Following the new regulations, for any order exceeding a certain, fixed sum, threshold tenders Ž . must be invited §2 . Naturally, the winner of aŽ . tender is the one who makes the best offer, or, in case the best offer is withdrawn or the contract negotiations are not successful, the second best one Ž .§50 .The ranking of the offers may be based on

1. the prices and<sup>r</sup>or

2. a multitude of criteria.

The bids should contain the evaluation process that will be followed, and in the case of 2 , the criteriaŽ . are also given, along with the order of their importance §34 .Ž .

In the case of 1 , it is necessary to determine the Ž . total price consisting of different parts and to exclude the unacceptable tenders. The preclassification process for filtering out the prospective bidders and offers not fulfilling some conditions §42 may re-Ž . quire decision support tools as well.

In the case of 2 , a multiattribute decision prob-Ž . lem is given. Moreover, the law orders that a committee of at least three members has to be set up to help the decision-maker to exclude unbalanced decisions §31 . Sometimes their contribution is limitedŽ . to assembling an expert report, but it is often a group decision-making. Based on the above, it can be stated that for evaluating tenders, a multiattribute group decision problem has to be solved for applying the stipulations of the Public Procurement Law. Problems like this can be solved, e.g., by AHP, PROMETHEE and WINGDSS methodologies and the corresponding EXPERT CHOICE, GDSS PROMETHEE or WINGDSS softwares see Refs. 1,2,4–6,8 .Ž <sup>w</sup> <sup>x</sup>.

In order to coordinate the developments in information technology IT in the governmental sphere,Ž . public offices and all types of educational institutions, at the Prime Minister’s Office, the Directorate for Public Procurement and Economic Management was entrusted with arranging 17 parallel tenders for the acquisition of computer technology-related goods. The areas of the tender invitations were as follows: general purpose PC workstations, high-performance PC workstations, network servers, notebooks, matrix printers of nine pins, matrix printers of 24 pins, ink-jet printers, laser printers, matrix printers for network, operational system softwares, word processor softwares, spreadsheet softwares, floppy disks, configuration and installation, service and maintenance, software selection and planning, and other computer technological services. The winner of each tender would supply practically the entire governmental sector with the goods and<sup>r</sup>or services in question.

The paper discusses two case studies on the evaluation of the above 17 parallel tenders in IT. The first series of tenders was invited in 1997. The Department of Operations Research and Decision Systems, Computer and Automation Institute, Hungarian Academy of Sciences participated in the whole procedure as an advising consultant, and the implied data processing and computations were our responsibility as well. On behalf of the Directorate for Public Procurement and Economic Management, L. Ketszeri´ was in charge of the whole tendering process. In Section 2, an overview is given on the model building phase; in Section 3, the multiattribute group decision models are studied; in Section 4, special attention is paid to the price adjustment method; in Section 5, the computational experience and the results are summarized, and finally, some concluding remarks are enumerated. During 1998, in the course of the second tendering process, the alteration of models built for the first series were used for tender evaluations, thus, our assistance was needed in data processing only. Therefore, in the latter tendering process, notes can be found on computational experience, in Section 5.

Besides the fact that the models designed for the earlier series have been reused for the latter series, the success of the tender evaluations is proved by the volume of the public procurement. Since 1997, goods worth of 4–5 billion HUF approximately 2–300 Ž million US\$ per year have been purchased within. the frame of the contracts yielded by the tenders.

## 2. Building the decision model

The Directorate for Public Procurement set up an interdepartmental committee, consisting of one member from each of the ministries involved. As there had not been such a complex tender since the Public Procurement Law came into force, and as the Law does not stipulate the tendering process precisely, the Directorate for Public Procurement requested a group of our department to participate in the whole tendering process. Our role was to provide assistance with the following steps: compilation of the decision model, IT processing, and evaluation of the incoming offers.

During the 2-month preparatory period, the committee of decision-makers completed with a member of our group, convened weekly to discuss the tendering process in details. A panel on building the decision model, led by the representative of our department, was involved in every weekly meeting among Ž three to four other panels on varying topics . In the. modelling panel of the first sessions, alternative evaluation techniques were introduced, their fundamentals were described, so that the decision-makers could choose the proper one for each phase of the tender evaluation. After decision models had been assigned to the evaluation steps, model parameters and components were focused on. Each meeting panel dealt with a class of model parameters; their role was explained, followed by a demonstration on the effect of different parameter settings, then the members of the committee specified the parameter values to be used in the tender evaluation process. The demonstrations were of a great help in showing the decision-makers how to translate their intrinsic preferences into model parameters that could be handled in this group decision situation.

In the preparatory period, the general course of the procedure was agreed upon. Considering the probably large number of competing firms, the committee, in accordance with the law, decided that the tendering process would consist of two rounds. The first round was the prequalification process, followed by the final ranking as the second round. In the first round, each firm was encouraged to compete, but only the top performers were invited to participate in the second round.

The goal of the first round was to check the competitors’ compliance with the pre-set legal and financial conditions and to select the ones with the best technical competence. Note that no offer was made on the part of the competitors at this stage, only information on each company were submitted, regarding the firm’s history, references, capital, employees, etc. Accordingly, the first round was further divided into pre-classification and ranking processes. During the pre-classification process, the competitors not fulfilling the financial and legal requirements were filtered out, afterwards, in the ranking process, those who passed were qualified, based on their technical competence. In each tender, the best onethird of the competing firms was invited to participate in the second round.

In the second round, in each tender, each of the invited firms was requested to submit an offer. No auction-type elements were involved in the process: only one offer could be proposed by each of the invited firms, and the offer was considered as a decision binding on the tenderer. The offers were ranked with respect to the criteria of the firm’s technical competence, the product quality and the price.

The filtering conditions were determined so that every competing firm should fulfill financial conditions, legal conditions formal requirements on theŽ application included , and a technical condition, .

namely, the product offered should bear the notion of ISO 9000-based quality assurance.

The committee adopted our recommendation that the technical competence of the competing firms should be evaluated by the methodology of multiattribute group decision model of tree type. The detailed description of this model can be found in Ref. <sup>w</sup> <sup>x</sup> 7 , in Chapter 3.1, a short summary is given.

The committee decided that the multiattribute group decision model of tree type should be used for evaluating the competitors during the second round, under the main criteria of technical competence and product quality. The technical competence was measured by the score achieved during the first round, while the product quality was further divided to subcriteria.

The score — provided by the group decision model, later referred to as gross score — and the offer price determined the choice of the winner. Inspired by the example of the World Bank, the committee decided that the final ranking should be accomplished by the price adjustment method, discussed in Chapter 4.

As the discussion of the evaluation methodology to be used in the second round commenced, a problem emerged: how to evaluate the prices? Normally, the market of IT commodities is transparent, so experts, based on their experience, can decide whether a given price is low, reasonable or actually high. Moreover, they can determine the exact utility value, i.e., one can construct a utility function. In this situation, however, as governmental orders were in question, it was clear that the competitors would cut their prices so as to win the contract. The hope for an increase in prestige and growth in market share, yielded by being a supplier of the government, might have made them cutting their prices so considerably that the bargain would not be worthy for them. Naturally, the price-cuts of the several companies were absolutely unpredictable, resulting in a AmarketB of offers that no one had experienced. Having no experience implied the impossibility of determining the utility value of the offers; moreover, no expert volunteered to forecast the price level that would rank low, medium or high amongst the reduced prices, not even tried anyone to predict the offer price range. This meant that a utility function could not be constructed in the classical manner.

Recall that by the force of the Public Procurement Law, the way of offer evaluation must be determined and made public in advance.

The choice of the price adjustment method did not completely solve, in itself, the problem of price evaluation, but resulted in other questions that called for a new solution methodology, discussed in Chapter 4.

## 3. Multiattribute group decision models

## 3.1. Decision model for the prequalification process

Narrowing down to its essentials, the model consists of a criterion tree, a weight system for each decision-maker and a voting power vector at each node of the tree.

The criterion tree consists of the criteria taken into account: on the first level, one finds the main criteria that are usually too complex and, therefore, are divided into subcriteria, which form the second level of the tree. If a subcriterion is still too complex, it is further divided into sub-subcriteria, which are placed on the third level, and so on. The criteria that are not divided into subcriteria are called leaf criteria. For practical reasons, a ‘goal’ criterion is taken, and the main criteria are considered the subcriteria of ‘goal.’

The weight systems are used to express the relative importance of the criteria. If a criterion and its subcriteria are considered, the weights assigned to the subcriteria show their importance relative to each other, i.e., the extent the subcriteria are taken into account in the evaluation with respect to the criterion.

The voting powers express the extent according to which the decision-makers’ opinion with respect toŽ the various tenders’ scores and importance — i.e., weights — of the criteria is taken into account..

The leaf criteria with respect to which the decision-makers give a consensus evaluation, rather than evaluating individually, are called objective criteria. They usually represent the numerically measurable properties of the competitors such as the density ofŽ their service network, the time required for meeting an order, etc. , and the evaluation with respect to. them is often carried out via utility functions. We refer to the other leaf criteria as subjective criteria, as each decision-maker evaluates the competitors independently. We note, however, that a numerically measurable criterion can also play the role of a subjective criterion if the decision-makers do not agree on a utility function, but evaluate the numbers individually, and vice versa, a numerically not measurable criterion can be objective if the decisionmakers evaluate by consensus rather than individually.

Through collective work and consulting, the criterion tree to be used in the evaluation of the firms’ technical competence has been compiled, as can be seen in Fig. 1. The criteria ‘Employees’ and ‘Information and training’ were set to subjective criteria, the other one’s objective, therefore, a construction of utility functions was required for the latter ones. The usage of a scale of 0–100 was accepted the com-Ž petitors would be scored by numbers between 0 and 100, under each criterion ..

All the objective criteria represented numerically measurable properties. The decision-makers were asked to name the number that expressed the minimal, just acceptable quality to them, and the number that meant maximum satisfaction, i.e., the level beyond which they did not acknowledge further im-

References (17) Delivery record (67) Length of relationship to the manufacturer (33) Services (42) Network (25) Commerce (27) Maintenance (73) Guarantee (24) Information, training (14) Maintenance (26) Capital (46) Provinces (54) Consumer support (11) Manufacturing (24) Delivery capacity (42) Quality assurance (58) Employees (17)

Fig. 1. Criterion tree for the prequalification process.

provement as quality increase. The utility function sought for have to return 0 and 100, respectively, if the former value and latter value are substituted. If, e.g., a decision-maker thought that a retailer should have had at least 2 years of business contact with the manufacturer in order to be considered a serious partner, but he judged 5 years of partnership just as good as 6, 7 or more, then $f ( x ) = 0$ for each $x \leq 2$ and $f ( x ) = 1 0 0$ for each $x \ge 5$ should hold for the utility function $f .$ In Fig. 2, a form used by the decision-makers in the utility function constructing process can be seen.

The decision-makers were asked, furthermore, to give the numbers corresponding to certain satisfaction levels they can identify e.g., to 50% satisfaction Ž level . We had previously wanted to apply interpola-. tion methods to construct the functions, but it turned out that the members of the committee had linear or Ž piecewise linear utility preferences. After recogniz- . ing this fact, a simple vote on the above two numbers and in the case of some criteria, on the break-Ž point sufficed to compile the utility functions. .

Weighting the criteria, i.e., determining their importance, is a very significant part of building a decision model. However, the decision-makers carried out this task with a relatively little effort, the reason of which became clear when the model for the second round was constructed.

The question of the voting powers was easily solved. As the members of the decision-making committee represented different ministries, equal voting powers were assigned to them, for the duration of the whole evaluation process thus, including the secondŽ round as well . Naturally, our representative had no . voting power, since he did not take part in the evaluation process either. In Fig. 1, the computed group weights can also be seen.

The structure of the model was documented, signed by each member of the committee, and deposited in a safe of the Directorate for Public Procurement, so it can be referred to in case of any legal dispute.

## 3.2. Decision model for the second round

As it was stated earlier, during the second round, the main criteria were as follows: technical competence, product quality and price. Thus, more expensive products of higher quality of more competent firms could compete with the cheaper products of relatively lower quality of relatively less competent firms. An adequate tradeoff had to be found so that the offers in the former and latter category be competitive with each other.

The decision-makers agreed that the technical competence would be evaluated with the score achieved in the prequalification process. They also identified the subcriteria of the criterion ‘product quality,’ some objective criteria and some subjective ones. The subjective criteria served for measuring the conformity of the offer to the governmental IT strategy. This time the multiattribute group decision model was the same as used in the first round, but the criterion trees for the various tenders were different.

Please fill in, at least, cells '0 %' and '100 %', and 1 or 2 other fields

<table><tr><td>Score (satisfaction level)</td><td>Number of sales points</td></tr><tr><td>0 %</td><td>0</td></tr><tr><td>10 %</td><td></td></tr><tr><td>20 %</td><td></td></tr><tr><td>30 %</td><td></td></tr><tr><td>40 %</td><td></td></tr><tr><td>50 %</td><td>5</td></tr><tr><td>60 %</td><td></td></tr><tr><td>70 %</td><td></td></tr><tr><td>80 %</td><td></td></tr><tr><td>90 %</td><td></td></tr><tr><td>100 %</td><td>11 or more</td></tr></table>

Fig. 2. Form for the specification of utility functions.

In the case of this model, the committee of decision-makers agreed on using a consensus weight system rather than the weight system of each individual i.e., the group weight system is simply a Ž weight system determined by consensus, during a meeting . Assigning weights to the subcriteria and . sub-subcriteria of ‘product quality’ and constructing the utility functions proved to be routine work.

The whole model building panel of two sessions was devoted to weighting the three main criteria. The decision-makers requested a complete lecture on the weighting, and demanded more and more demonstrative examples, although they already had successfully weighted a criterion tree and a part of another one. The explanation is as follows: the price concern was high, as usual, or even higher, as the subsequent purchases would induce public expenses, which is always a sensitive issue. On the other hand, reliability and proper quality is a must, especially in the governmental sector. This meant that the decisionmakers had an incredibly narrow scope for weighting and thus, the sharp determination of the tradeoff between the main criteria was a crucial point in the decision. The other weights and the utility functions were important as well, but we arrived at a central question right now.

To help the decision-makers we provided an entire tender evaluation example with various weight systems. To ensure that the decision-makers’ preferences were exactly transformed to weights the weighting was accomplished by two methods, directly and by the help of verbal pairwise comparison with the EXPERT CHOICE software.

In the tenders of PC workstations, servers, notebooks, software products and floppy disks, the final weight system was as follows:

price 50; product quality 30; technical competence 20.

In the tenders of printers and services, the weights were:

price 60; product quality 20; technical competence 20.

## 3.3. Methodology for solution

The main steps of the evaluation by this model are as follows a more detailed study is found in Ref.Ž <sup>w</sup> <sup>x</sup> 7 :.

First step: each decision-maker evaluates the firms with respect to the subjective leaf criteria.

Second step: each decision-maker assigns weights to the criteria.

These are the steps that require the direct participation of the decision-makers. During the remaining steps, calculations are performed, and no further input data occur. Thus, the following steps are executed automatically by our software.

Third step: the group scores are determined at the leaf criteria, based on the scores given by the decision-makers and the voting powers assigned to them Ž . with respect to the criterion in question . At an objective criterion, the group score is equal to the consensus score at that criterion or, if a utilityŽ function is used, to the value given by the utility function ..

Fourth step: determination of the group weights. The decision-makers’ weight system is normalized so that if a non-leaf criterion is taken, the sum of the weights assigned to its subcriteria is equal to 1. After the normalization, the group weight is calculated from the individual weights and the voting powers assigned to the decision-makers at the parent criterion of the criterion in question.

Fifth step: the evaluation is done on the tree recursively: a firm’s group score at a non-leaf criterion is computed from the firm’s group score at the subcriteria of this criterion and the group weights of the subcriteria. The total score of the firm is the firm’s score at the criteria ‘goal.

In this case, the evaluation with respect to the leaf criteria was scale-based, and an additive aggregation method, the weighted arithmetic average based onŽ Bridgman’s principle, see Ref. 3 , was used. <sup>w</sup> <sup>x</sup>.

## 4. The price adjustment method

Our first task was to work out a correct price adjustment method equivalent to a multiattribute decision model of tree type with the criteria weights determined earlier with great effort.

The solution we recommended, and accepted by the decision-makers, was the use of the formula

$$
C ^ {*} = C + (1 - p) N,
$$

in the case of tenders where the weight of criterion ‘price’ was 50, and

$$
C ^ {*} = C + \frac {2}{3} (1 - p) N,
$$

where this weight was 60. Here, $C ^ { * }$ denotes the adjusted price, C the original offer price, p the fraction value corresponding to the gross score inŽ our case, it was the one hundredth of the gross score , and. N a benchmark price, the determination of which will be discussed later.

These formulae are equivalent to the determination of the adjusted price by the tree-type model with two criteria: price and an artificial cost factor re-Ž lated to the difference from the perfect quality ,. where the weighted arithmetic average is used, and the weights of the price and cost criteria are set to 50–50 or 60–40, respectively. In the second for- Ž mula, the coefficient of the term C, 1, is 60% of $5 / 3 ,$ , the sum of the coefficients, whilst the coefficient $2 / 3$ of term $( 1 - p ) N$ represents 40% of the sum..

The suggested method is correct in the sense that it treats the differences in product quality and technical competence i.e., the difference in the gross Ž score equally regardless of the offer price. Note that. the original price adjustment method, defined by the formula

$$
C _ {1} ^ {*} = C - p C,
$$

would result in a situation in which the same extra quality or plus service is regarded unequal in the case of offers with different prices, a situation unacceptable in this tender due to the expected unpredictable price cuts on behalf of the competitors.

Finally, our suggestion is really a price-adjusted method, as it is equivalent to the use of formulae

$$
C ^ {*} = C - p N,
$$

and

$$
C ^ {*} = C - \frac {2}{3} p N,
$$

respectively the addition of a constant to the right-Ž hand side implies no change in the outcome of the evaluation process, as the addition of the same constant to the adjusted price of each of the offers does not affect their order ..

Recall from Chapter 2 that the competitors’ unpredictable price cuts made it impossible to construct a utility function for price evaluation. By the choice of the price-adjustment method, we had a device for completing the tender evaluation, determining only a benchmark price N rather than a utility function.

Needless to say, the benchmark price N cannot be given in advance. A method could be constructed, however, to compute its value based on the offer prices.

The method we suggested and was accepted by Ž the committee is as follows. The offers were sorted. by the offer prices: first, the harmonic and quadratic means of the prices were calculated, then the offers with a price lower than the harmonic mean were put into the first group, offers with price exceeding the quadratic mean were put into the second group. The values $p _ { 1 }$ and $C _ { 1 }$ were calculated afterwards as the geometric means of the gross score values and the offer prices of the offers in the first group, respectively, and analogously, $p _ { 2 }$ and $C _ { 2 }$ were the geometric averages of those in the second group. Finally, the benchmark price was expressed as

$$
N = \frac {C _ {2} - C _ {1}}{p _ {2} - p _ {1}}.
$$

Note that the above classification of the offers into groups served no other purpose beyond the determination of N.

The reason for applying the described method is as follows. In the price adjustment formulae 1 andŽ . Ž . 2 , N obtains an economic interpretation: it expresses the market value of the perfect product quality and technical competence corresponding to Ž $p = 1$ or a gross score of 100 . Thus, when the offer prices . are known, a realistic value of N can be determined as the typical offer price increase per one point extra gross score, among the offers.

## 5. Computational experience

## 5.1. Tendering process, 1997

Considering that 18 criteria were used in the first multiattribute group decision model and the expected number of the competing firms was large, the tenderers were obliged to attach files to their written tender offers which contained inŽ . EXCEL format the data needed for the prequalification process. In order to make automated data processing possible, the EXCEL files were created in advance and provided for the competitors as part of the tender documentation , so Ž . they only had to fill in the appropriate cells.

The evaluation in the prequalification process was scheduled as follows. As the first step, one dBase database was to be created for each tender, then the data of the offers were to be parsed from the EXCEL files and collected in the database of the corresponding tender. According to the second step of the schedule, the filtering process was to be performed by sorting the records of the dBase files, thus the offers not meeting all the legal and financial conditions were to be removed from the databases and moved into a ‘drop’ database the contents of thisŽ database would be used to compile a document on the inappropriate offers and the reasons of exclusion from further competition . With respect to the offers. that passed, the utility functions were to be evalu ated, and the data entered into the WINGDSS 4.1 software package. Note that the software uses dBase compatible files, so any dBase data could be directly written into the WINGDSS’s inner data tables, supposing that the decision model was built previously.

It was scheduled that the members of the committee eight decision-makers should meanwhile score Ž . the offers with respect to the subjective criteria, based on the written part of the applications. When they were ready, the scores would be entered into the WINGDSS software as well. At this point, the software should have all the data required to provide the ranking of the offers with respect to technical competence.

Considering the 17 tenders, altogether 468 offers were handed in by 34 firms. The processing of the 468 offers meant such a big task that was not possible to be completed by traditional, not computer-based evaluation methods within the 5-day deadline prescribed in this case. On the other hand, by the above data processing schedule, the accomplishment would have taken some hours only. However, our program terminated with an error message during the very first step. Investigation soon revealed the reason: some of the firms re-edited the EXCEL files, e.g., inserted rows, or wrote text in cells where a numeric expression was expected e.g., price , orŽ . answered to a yes<sup>r</sup>no question in three lines, etc. Thus, all the EXCEL files had to be checked and repaired manually. Despite the fact that correction of the files took 3 days, the evaluation was completed in time.

During the second round, the quantity of new input data was considerably lower: only about onethird of the competitors were invited to participate, and the number of criteria in a tender varied between five and eight. The subjective scores were provided by the decision-makers in EXCEL files, and the objective values were disposed in dBase format. After applying the utility functions on the objective values, the arising objective scores were entered into the WINGDSS software, along with the subjective scores. The total group scores were exported in dBase format, and the reference price N was determined based on the offer prices and total group scores for each tender, as described in subsection 4. Finally, the adjusted prices were determined.

## 5.2. Tendering process, 1998

In 1998, 17 parallel tenders were considered, 168 offers were evaluated in one round by nine decision-makers with respect to 100–150 criteria. As it was stated earlier, the evaluation of the tenders in 1998 was accomplished by similar models built for those in 1997. However, some of the elements were changed.

The evaluation consisted of one round thus, thereŽ was no prequalification process . Filtering conditions. were set up not only for legal or economic and financial attributes, but for other properties of the firms e.g., number of employees , for technical Ž . parameters of the offered product e.g., speed of a Ž printer and evidence of compliance with certain. standards proven by certifications supplied.

The main criteria were as in 1997: offer price, technical competence and product quality, but the criterion tree constructed for the purpose of evaluating ‘product quality’ and ‘technical competence was larger: 100 to 150 subcriteria were used in the various tenders. Almost all of the criteria were objective, scored by nearly 1500 utility functions. With respect to the subjective criteria, the 168 offers of the firms were scored by nine decision-makers, but by consensus rather than individually from our point ofŽ view, this meant that these criteria acted as objective ones as well . The evaluation was concluded with the. price adjustment, with the method discussed in Chapter 4.

Gaining experience from the tendering process in 1997, the offer data were requested in written form only, and professional operators were hired to type those in ACCESS databases. As the utility functions could be sorted in some classes e.g., linear, piece-Ž wise linear, threshold, Boolean , they, too, were . written in an ACCESS database with a specific notation system, and a small interpreter program was developed to carry out the evaluation. With these arrangements, the evaluation of the 168 incoming offers was executed in 3 days.

Regarding the amount of purchase accomplished within the frame of the previous year’s tenders, necessity for security emerged. In order to achieve complete confidentiality in handling the offer data, the names of the competing firms and the decisionmakers were substituted for code words. The names did not appear in any of the databases, only the code words, thus — except the main decision-makers — no one was able to match the data records with the applicants. Some of the participants of the evaluation process including our Department did not know theŽ . list of the competitors either.

A further precious attribute of software-supported decision-making is controllability. Although the evaluation was complex, the participants had only a part of the information, and in 1998, security arrangements were made, yet the main decision-makers could follow the whole process.

It is also worth mentioning that the evaluation having been accomplished by exactly defined mathematical functions in the frame of well-documented models, the decision can be justified, and the computation can be reconstructed in the case of any legal dispute.

We were informed by the main decision-makers that our computation results were accepted and the winners were chosen accordingly, both in 1997 and 1998.

## References

<sup>w</sup> <sup>x</sup> 1 J.P. Brans, C. Macharis, B. Mareschal, The GDSS PROMETHEE Procedure, Vrije Universiteit Brussel, 1977, STOOT W<sup>r</sup>277, March.

<sup>w</sup> <sup>x</sup> 2 J.P. Brans, B. Mareschal, Ph. Vincke, How to select and how to rank projects. The PROMETHEE method, European Journal of Operation Research 24 1986 228–238.Ž .

<sup>w</sup> <sup>x</sup> 3 P.W. Bridgman, Dimensional Analysis, Yale Univ. Press, New Haven, 1931.

<sup>w</sup> <sup>x</sup> 4 P. Csaki, T. Rapcsak, P. Turchanyi, M. Vermes, Research and´ ´ ´ development for group decision aid in Hungary by WINGDSS, a Microsoft Windows based group decision support system, Decision Support Systems 14 1995 205–217.Ž .

<sup>w</sup> <sup>x</sup> 5 P. Csaki, L. Csiszar, F. Folsz, K. Keller, Cs. Meszaros, T.´ ´ ¨ ´ ´ Rapcsak, P. Turchanyi, A flexible framework for group deci-´ ´ sion support: WINGDSS 3.0, Annals of Operations Research 58 Ž . 1995 441–453.

<sup>w</sup> <sup>x</sup> 6 P. Csaki, F. Folsz, K. Keller, G. Lorant, Cs. Meszaros, T.´ ¨ ´ ´ ´ ´ Rapcsak, T. Toth, Visualisation in decision support system´ ´ WINGDSS 4.0, in: T. Hunjak, L. Martic, L. Neralic Eds. ,Ž . Proceedings of KOI’95 5th Conference on Operational Research, Croatian Operational Research Society, 1995, pp. 1–32.

<sup>w</sup> <sup>x</sup> 7 P. Csaki, F. Folsz, T. Rapcsak, Z. Sagi, On tender evaluations,´ ¨ ´ ´ Journal of Decision Systems 7 1998 179–194.Ž .

<sup>w</sup> <sup>x</sup> 8 T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

![](/api/attachments/NU65E29E/fulltext/images/fddaa7f59b15a4d97f81032959b6a6b55181387aef100febc2bc7c716901b367.jpg)

Tamas Rapcsak graduated from the Kos-´ ´ suth Lajos University, Debrecen, Hungary, and received his PhD and DSc from the Hungarian Academy of Sciences in Operations Research. Current posts: Head of Department and Laboratory of Operations Research and Decision Systems at Computer and Automation Institute, Hungarian Academy of Sciences, Professor and Head of Department of Economic Decisions a jointŽ department with Budapest University of

Economic Sciences . His research interests include decision sys-. tems, nonlinear optimization and generalized convexity. He is the President of Hungarian Operational Research Society and the Operational Research Committee of the Hungarian Academy of Sciences. He is also the editor of the Journal of Optimization Theory and Applications, Journal of Global Optimization, Central European Journal of Operations Research and P.U.M.A. He is the author of the book titled ASmooth nonlinear optimization in R<sup>n</sup> B published by Kluwer Academic Publishers in 1997. He received Gyula Farkas Prize in 1978.

![](/api/attachments/NU65E29E/fulltext/images/ca20d02ade2b28cb81f77fc1ad71098e697a1ec83e09bfd8c50daa8be7f9ada2.jpg)

Zoltan Sagi graduated from the Lorand´ ´ ´ Eotvos University, Budapest, Hungary, ¨ ¨ where he presently pursues his PhD studies in operations research, in the field of multiattribute group decisionmaking. He is employed at the Department of Operations Research and Decision Systems, Computer and Automation Institute, Hungarian Academy of Sciences, with responsibilities of research, participation in decision support projects and in the education of univer-

![](/api/attachments/NU65E29E/fulltext/images/f32c63d70c2f26ffb9ae640af1a589a0a8d45f7fe26237ecb187867177543693.jpg)

Laszlo Ketszeri graduated from the´ ´ ´ Technical University of Budapest, Hungary, in 1973, Faculty of Measurement and Control Techniques. Main jobs: 1982–1983 Foreign service in Syria, Aleppo Academy Al Assad, procurement expert for education technological development. 1984–1989 MOD Electronic Directorate<sup>r</sup>foreign service in India, Syria, Libya, Military Adviser, bidding manager major. 1989–1991 TECH-NIKA Foreign Trading, Sales Engineer

sity students. He is a member of the Hungarian Operational Research Society.

![](/api/attachments/NU65E29E/fulltext/images/06a3bfaa37ae45accd6ba52186d28aac04f088e28670ddb843af702a596d7f17.jpg)

Tamas Toth is an undergraduate at the´ ´ Technical University of Budapest, Ž . Hungary , Faculty of Informatics. Since 1998: branch: Department of Control Engineering and Informatics, Intelligent systems, intelligent robots. His interests include decision systems, electronic vision, detecting, image processing, and neural networks. Employments: 1996– 2000, Computer and Automation Institute, Hungarian Academy of Sciences, Department of Operations Research and

Decision Systems. Jobs: software development and assistance in university education, designing and developing environmental monitoring system. From 1998: Stock Exchange software development upon the order of Fornax Rt. Developing option-pricing and real-time data-transmission systems, and further data-base and client-server applications for Windows and UNIX platforms.

<sup>r</sup> Bidding Manager, Head of Department. 1991–1992 DND. TELECOM Marketing Manager. 1992–1993 MOI Technical Department, Procurement expert, Counselor. 1993. MOI Central Office of Procurement. In 1995–1996, he attended a special course for asset evaluation and property business management and got the qualification of a registered expert for asset evaluation and trading. 1997–1998 Prime Minister’s Office, Directorate for Economic and Public Procurement, Deputy Head of Directorate, senior counselor. 1999 Hungarian Post, Directorate for Procurement and Supply, Head of Department for IT and logistical procurement.
