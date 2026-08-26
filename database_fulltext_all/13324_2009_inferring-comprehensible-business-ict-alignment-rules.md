---
otero_id: 13324
otero_key: "K6CUEUCU"
title: "Inferring comprehensible business/ICT alignment rules"
authors: "Bjorn Cumps; David Martens; Manu De Backer; Raf Haesen; Stijn Viaene; Guido Dedene; Bart Baesens; Monique Snoeck"
year: "2009"
journal: "Information & Management"
doi: "10.1016/j.im.2008.05.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Inferring comprehensible business/ICT alignment rules

Bjorn Cumps <sup>a,b,</sup>\*, David Martens <sup>a,f</sup>, Manu De Backer <sup>a,f,g</sup>, Raf Haesen <sup>e,a</sup> Stijn Viaene <sup>a,b</sup>, Guido Dedene <sup>a,c</sup>, Bart Baesens <sup>d,a</sup>, Monique Snoeck <sup>a</sup>

<sup>a</sup> Department of Decision Sciences and Information Management, Katholieke Universiteit Leuven, Belgium

<sup>b</sup> Department of Operations and Technology Management, Vlerick Leuven Gent Management School, Belgium

<sup>c</sup> Department of Economics and Business, University of Amsterdam Business School, The Netherlands

<sup>d</sup> School of Management, University of Southampton, United Kingdom

<sup>e</sup> Department of Economics & Management, Hogeschool-Universiteit Brussel, Belgium

<sup>f</sup> Department of Business Administration and Public Management, Hogeschool Gent, Belgium

<sup>g</sup> Department of Management Information Systems, University of Antwerp, Belgium

## A R T I C L E I N F O

Article history: Received 1 September 2006 Received in revised form 31 July 2007 Accepted 12 May 2008 Available online 7 February 2009

Keywords: Business/ICT alignment Alignment rule set Data mining Artificial ant systems Practical guidelines

## A B S T R A C T

We inferred business rules for business/ICT alignment by applying a novel rule induction algorithm on a data set containing rich alignment information polled from 641 organisations in 7 European countries. The alignment rule set was created using AntMiner+, a rule induction technique with a reputation of inducing accurate, comprehensible, and intuitive predictive models from data. Our data set consisted of 18 alignment practices distilled from an analysis of relevant publications and validated by a Delphi panel of experts. The goal of our study was to describe practical guidelines for managers in obtaining better alignment of ICT investments with business requirements. Our obtained rule set showed the multidisciplinary nature of B/ICT alignment. We discuss implication of the alignment rules for practitioners. - 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Alignment of business (B) and Information and Communication Technology (ICT) strategies in organisations is essential to the organisation and especially to its CIO. Much has been written on B/ ICT alignment, yet few studies have provided actionable results for practitioners. We tried to determine how to achieve alignment using practices suggested in the literature and by collecting quantitative data in a survey designed to test which practices aid in aligning organisational strategies.

## 2. Literature review

We reviewed several articles [2,8,9,17,18] in an attempt to identify the practice of alignment and modelled it as having three major steps: defining, justifying, and achieving alignment.

## 2.1. Defining, justifying and achieving B/ICT alignment

Defining alignment involves assuring the fit, harmony, integration, linkage, bridge or fusion of the strategies. This integration should occur at two levels:

\- Making sure that the information resources support business objectives (aligning planning and objectives).

\- Aligning business and ICT strategies, in conjunction with their infrastructures.

During alignment, formal and social elements must, of course, be considered [10,16]. Also the presence of an informal structure permits an organisation to react rapidly to change and to continue to excel while more formal structures need time to react and potentially be updated.

Of course, B/ICT alignment directly impacts business performance, but there are also indirect effects: alignment can help create sustainable competitive advantage, can lead to better and focussed ICT investment, and result in a better balanced ICT portfolio. However, there may be risks in B/ICT alignment. If it is too tight, it reduces the organisation’s strategic flexibility and may restrict the organisation’s outlook, inhibiting recognition of alternatives and reducing the firm’s ability to recognise and respond to change.

Finally, it is not easy to achieve or obtain B/ICT alignment. Clearly, there is a strong need for insight in the practice of alignment. Examples of enablers and inhibitors have been proposed but the theories and methods have not been tested practically. The goal of our effort was therefore straightforward: to identify how organisations have attempted to improve B/ICT alignment. This involved knowing which processes had been modified, which structures had been installed and how they were managed and thus governed the process of achieving better B/ICT alignment.

## 2.2. Data mining and ant systems

Recently, the volume of available, potentially useful, raw data had increased explosively. But though information is available, it is often hidden. Data mining has become a major process for extracting knowledge from the data.

There are different uses of data mining but the task of interest here is in classification, assigning a data point to a predefined class or group according to its characteristics. We applied this in the B/ ICT alignment context: the result of a classification is the definition of a grouping—producing a model that makes it possible to classify future data points based on the set of specific characteristics in an automated way, as shown in the simplified B/ICT alignment example of Fig. 1.

There are many different techniques that can be used for this classification task, including: logistic regression, linear and quadratic discriminant analysis, k-nearest neighbour, neural networks, and support vector machines. The performance of the classifier is typically measured as its predictive accuracy on an independent test set. Benchmarking studies [1] have shown that the non-linear classifiers generated by neural networks and support vector machines score best on this measure. However, this strength has also been their main weakness: the classifiers are complex mathematical functions which are incomprehensible or opaque. Comprehensibility can be a key requirement: in order to be convinced that the result is of value, the user should understand the reasoning that resulted in the prediction. In some domains, this is a major problem which causes reluctance to use the classifier or may even result in its complete rejection. Obviously, we need to understand why organisations are categorised as either highly or poorly aligned. Thus we realized that we could be either descriptive or prescriptive in our study. Justifiability involves the extent to which the induced model agrees with existing domain knowledge; it also is crucial [13].

We used AntMiner+ [Ant Colony Optimisation (ACO)] to infer rules from our data, with both accuracy and comprehensibility taken into account. AntMiner+ can incorporate domain knowledge, providing intuitive decision support. This system was used to construct a model predicting B/ICT alignment. By using AntMiner+ we were able to classify observations as either highly or poorly aligned as well as understand the classification method and allow us to determine which investments would help the firm become highly aligned.

## 3. Research method

We collected data by administering a survey containing questions that were designed to serve two purposes:

\- to calculate a B/ICT alignment score that gave us an indication of the degree of alignment of the organisations and

\- to determine which alignment interventions (practices) were used in those organisations.

![](/api/attachments/K6CUEUCU/fulltext/images/cb7fa2926af248c6fb42ff74e929cb56597a555374ddf92cc1a20389bd373e60.jpg)  
Fig. 1. B/ICT alignment classification model.

We obtained the set of interventions from a search of the literature. Then, from the data collected, we used AntMiner+ to determine which set of alignment interventions provided higher alignment scores.

## 3.1. Sample selection and characteristics

We used a field survey methodology with a restricted, webbased survey instrument. Invitations to complete the online survey were sent out to 3000 European organisations. A well known and reliable market research institute performed the sampling and execution of the survey. Our population was a quasi-random sample of organisations fulfilling a quota of company size, class, etc. Thus samples were drawn locally by divisions of the market research institute from the following business directories and databases: Dun & Bradstreet, Spectron, and Marktselect. We targeted CIOs as the key informant of each organisation as we decided that he or she was in the best position to respond to our survey questions. However, in order to collect a large data sample, we asked the CIO to redirect the survey to a similar position (ICT director, ICT manager, etc.) if he or she was unwilling or unable to respond; this also was intended to reduce non-response bias and implied that we preferred an answer with slight respondent bias to no reply. Participants were guaranteed confidentiality and a summary of the findings was offered as an incentive for responding.

The themes and questions included in the questionnaire were all subjected to a pre-test. They were elicited via a Delphi panel consisting of four academics with expertise in ICT management and survey design, two ICT management consultants and four ICT managers. This process resulted in a more condensed set of questions and some minor modifications in their wording. The pretesting contributed to a survey that was both theoretically sound and had practical relevance. For most of the questions, organisations had to evaluate themselves on a five-point Likert scale ranging from 1 = strongly agree to 5 = strongly disagree. The respondents were not told the ultimate purpose: that it was intended to determine B/ICT strategy alignment. The survey included questions on infrastructure, applications and systems for other research studies we were making.

From the 790 responses received, we removed responses with missing values, leaving 641 for an overall response rate of 21%. This was low but similar to other studies in the IS field; corporate policy, reluctance to provide information, and time constraints were the major reasons given for non-response. Table 1 gives a breakdown of the sample by country, size, industry, turnover and respondents. The majority of the respondents (67%) had an ICT related function. Around 10% were CEO’s or business managers. More than half of the responding organisations had a workforce of over 500 employees. The spread of countries had an over-respresentation of Belgian organisations and underrepresentation of German organisations. Similarly, the Finance sector was underrepresented and not all respondants were CIO’s or part of an ICT department.

In order to establish the absence of non-response bias, we compared the mean values of 18 variables for the early (week 1) and late (week 6) responders. Differences between the means of the groups were not significant (two-tailed t-tests, p < 0.05), indicating that non-response bias was small.

## 3.2. B/ICT strategy alignment measure

The respondents were not asked to asses the degree of B/ICT alignment. We calculated their score based on their response on the questions reported in Appendix A. To obtain a numerical assessment we first had to construct an alignment score variable which indicated the match between business perception of the role of ICT in the organisation and the ICT portfolio of systems adopted to support it. We considered three value measures: operational excellence, product leadership, and customer focus. These indicated the strategy of the organisation when considering ICT investment. We felt that they were good indicators of the organisation’s strategic direction. However, we decided that we should include two others: enterprise integration and creation of management information. The Delphi panel confirmed the importance of these two.

Profiles of responding organisations.

<table><tr><td>Range</td><td>Frequency</td><td>Percent</td></tr><tr><td colspan="3">(a) Participation by country</td></tr><tr><td>United Kingdom</td><td>142</td><td>22</td></tr><tr><td>Belgium</td><td>140</td><td>22</td></tr><tr><td>France</td><td>95</td><td>15</td></tr><tr><td>Spain</td><td>97</td><td>15</td></tr><tr><td>The Netherlands</td><td>71</td><td>11</td></tr><tr><td>Italy</td><td>57</td><td>9</td></tr><tr><td>Germany</td><td>39</td><td>6</td></tr><tr><td>Total</td><td>641</td><td>100</td></tr><tr><td colspan="3">(b) Total number of employees</td></tr><tr><td>50–99</td><td>90</td><td>14</td></tr><tr><td>100–499</td><td>192</td><td>30</td></tr><tr><td>500–999</td><td>64</td><td>10</td></tr><tr><td>1000–2999</td><td>77</td><td>12</td></tr><tr><td>&gt;3000</td><td>218</td><td>34</td></tr><tr><td colspan="3">(c)  $Participation by industry^a$ </td></tr><tr><td>CIPS</td><td>269</td><td>42</td></tr><tr><td>TICE</td><td>167</td><td>26</td></tr><tr><td>PUBLIC</td><td>134</td><td>21</td></tr><tr><td>FINANCE</td><td>39</td><td>6</td></tr><tr><td>PHARMA</td><td>32</td><td>5</td></tr><tr><td colspan="3">(d) Participation by turnover</td></tr><tr><td>&lt;€10 million</td><td>115</td><td>18</td></tr><tr><td>€10 million–€49 million</td><td>147</td><td>23</td></tr><tr><td>€50 million–€99 million</td><td>71</td><td>11</td></tr><tr><td>€100 million–€499 million</td><td>96</td><td>15</td></tr><tr><td>€500 million–€999 million</td><td>44</td><td>7</td></tr><tr><td>&gt;€1 billion</td><td>154</td><td>24</td></tr><tr><td>Do not know</td><td>14</td><td>2</td></tr><tr><td colspan="3">(e) Participation by position</td></tr><tr><td>CIO</td><td>141</td><td>22</td></tr><tr><td>Head of ICT department</td><td>192</td><td>30</td></tr><tr><td>ICT managers</td><td>96</td><td>15</td></tr><tr><td>Business managers</td><td>38</td><td>6</td></tr><tr><td>CEO</td><td>26</td><td>4</td></tr><tr><td>COO</td><td>7</td><td>1</td></tr><tr><td>Other</td><td>141</td><td>22</td></tr></table>

<sup>a</sup> CIPS = consumer and industrial products and services; TICE = technology, information, communication and entertainment.

Appendix A shows the operationalisation of the alignment capability variable. We used a matching approach to calculate the alignment score (the degree of parallelism between business and ICT). Our approach was similar to that of Chan et al. [3]; e.g., between we rely on formal planning techniques and our IS systems provide planning tools. However, their alignment measure was more elaborate than ours; we opted for matching instead of moderation as we did not use an indicator variable. Alignment varied significantly across organisations. The average alignment score was 13.2 out of 20. About 23% of the organisations scored 16 or above and 6% scored 18 or more. However, 23% of organisations scored 10 or less.

## 3.3. Listing of B/ICT alignment interventions

Based on our archival analysis, we selected 26 practices that organisations used to improve B/ICT policy alignment, categorising each according to Luftman’s [11] categories (the questionnaire is shown as Appendix B). The model shows that we opted for a diverse set of practices able to cover all different categories, though they may not be mutually exclusive. Our initial set of 26 was reduced to 18 by the Delphi panel in order to increase relevance and reduce overlap.

![](/api/attachments/K6CUEUCU/fulltext/images/307e73d3d74082f8305e3eedb2140349b912db3d9734c1383f3be1f66945695b.jpg)  
Fig. 2. Path selection with ants using pheromones.

## Communication

Many authors have stated that communication between business and ICT was key in achieving useful corporate systems. It helped by integrating ICT into business needs. Good communication, a shared vision, and mutual understanding were needed.

## Partnership

Of course, we have known since the concept of a CIO was articulated that his or her participation in business planning was essential to improve performance. Integrated planning, strategising, and executive involvement are determined by answers to questions 4 through 6.

## Architecture

The importance of a link between ICT organisation (centralised vs. decentralised) and strategic alignment has also been stressed for many years. Centralisation consistency, business process support, and architecture impact analysis were reflected in responses to questions 7 through 9.

## Value measurement

The importance of value measurement and management in B/ ICT alignment has also frequently been stressed. Value management has a positive effect on B/ICT alignment and ICT investments generate business value. Both ICT investment prioritisation and benchmarking have to be used as alignment mechanisms. Business value demonstration, prioritisation and benchmarking were measured through questions 10 through 12.

## Governance

ICT governance is a key element in obtaining B/ICT alignment. It encourages desirable behaviour in the use of ICT by effective allocation of decision rights and accountability as well as performance management and budget allocation. Budget allocation and transparency of decision rights and accountability were computed from the answers to questions 13 through 15.

## Human resources

Finally, the importance of a firm’s ability to attract and retain staff is vital to success. Furthermore, ICT staff possessing both business and ICT skills, are more valuable to an organisation than those with only technical skills. ICT acceptance, stakeholder management, and joint development were determined through answers to questions 16 through 18.

## 4. Data analysis

We used AntMiner+ as a system to infer simple, understandable alignment rules for factor classification: this allowed us to derive a series of steps that would produce better B/ICT strategy alignment, resulting in an accurate and comprehensible method that incorporated domain knowledge. As we had a sufficiently large data set and no predefined model, we decided that data mining was the best technique to use. We needed to build a classification model that could distinguish between highly aligned and poorly aligned organisations.

## 4.1. Artificial ant systems

Artificial ant systems were inspired by the behaviour of ant colonies, and represent a relatively new concept in artificial intelligence: swarm intelligence [6]. It is the property of a system whereby the behaviour of unsophisticated agents interacting locally with their environment to result in the emergence of functional global patterns. An ant is a simple insect with limited capabilities, but an ant colony is able to behave in complex manners and construct intelligent solutions to problems such as the transportation of heavy items and finding the shortest path between a food source and the nest. This complex behaviour emerges from self-organisation and indirect communication between the ants. Their communication occurs indirectly through the environment rather than between the individuals: this is termed stigmergy. More specifically, ants communicate through a pheromone, chemical substance that an ant drops on its path. When an ant finds a pheromone trail it is likely to be followed by another ant that encounters it. However, when no ants follow a path, the pheromone trail intensity decreases: this is termed evaporation.

![](/api/attachments/K6CUEUCU/fulltext/images/034709b89883f18be57120f83c10f347f6b8b8b4659ae91fa1f823c3250431ac.jpg)  
Fig. 3. Reduced construction graph for B/ICT alignment data.

These principles are illustrated in Fig. 2, where two ants starting from their nest (left) are looking for the shortest path to a food source (right). Initially no pheromone is present on either trail, so there is thus a 50% chance of an ant choosing either path. Suppose one chooses the lower and the other the upper. The ant that chose the lower (shorter) trail will return faster to the nest, resulting in twice as many pheromones on the lower trail. As a result, the next ant will probably choose the lower, shorter trail, resulting in more pheromone secretion, etc. Thus (almost) all ants will follow the shorter path. These principles have been applied to create multiagent systems, mimicking their biological counterparts and as a viable method for attacking hard combinatorial optimisation problems [4,5], etc.

## 4.2. The AntMiner+ approach to data mining

Recently, we implemented a stigmergy-based approach using artificial ant technology: the AntMiner+ classification technique [7]. Its aim was to extract simple if-then-else rules from data. To use it, an environment for the ants is defined as a directed, acyclic construction graph that allows a clear representation of the problem domain. This graph is defined by having each column (or vertex group) corresponding to a variable and every row corresponding to a value. An ant moving from vertex $\nu _ { i , j }$ to vertex $\nu _ { i + 1 , k }$ adds to its rule the term $\langle V _ { i + 1 } = V a l u e _ { k } \rangle$

To allow for rules when some variables are not involved, an extra dummy vertex is added with a value that is undetermined; i.e., it can take any value available. Although only categorical variables can be used in the implementation, we made a distinction between nominal and ordinal ones. Each nominal variable has one vertex group, but for an ordinal one, we must build two vertex groups to allow for intervals that are to be chosen by the ant. The first vertex group corresponds to the lower bound and should thus be interpreted as $\langle V _ { i + 1 } \geq V a l u e _ { k } \rangle$ , the second determines the upper bound, giving $\langle V _ { i + 2 } \leq V a l u e _ { k } \rangle$ . This allows less, shorter and thus better rules. Fig. 3 provides a reduced construction graph for B/ICT alignment data. Although we showed only two variables (Q1 and Q2), we actually allow 18. An ant that has chosen the path denoted in boldface, implicitly constructing the rule (with SA = strongly agree; A = agree; N = neutral; D = disagree; and SD = strongly disagree):

if Q1  SA and $\mathbf { Q } \mathbf { 1 } \leq \mathbf { N }$ and $\ Q 2 \geq S { \mathsf { A } }$ and $Q 2 \leq { \mathsf { A } }$

then highly aligned

The basic working of this technique follows the procedure:

1. All ants begin in the start vertex and walk to the end, choosing their path in the manner just described, depending on the heuristic and pheromone value.

2. Once the ants arrive at the end, the path of the best ant is updated, i.e. the pheromone increased, while the others have their pheromone lowered by evaporation.

3. After a number of iterations, the pheromone level of one path will be very high, while the value of the other paths will be less.

Thus almost all ants will choose this path and therefore convergence occurs.

4. The described rule is extracted, all data instances that are described by that rule are removed from the data set and a new iteration occurs.

5. The algorithm ends when a sufficient amount of the data has been described by the extracted rule set.

Alternatively this may be represented as

Construct graph

while (insufficient points described by rule set)

initialise heuristics, pheromones and probabilities of edges

while (no convergence)

create ants

let ants walk from start to stop

vaporise the edges

update the path of best ant

kill the ants

end

extract the rule and add to the rule set

remove all data instances covered by the extracted rule

end

evaluate the performance on independent test set

The performance of such a data mining technique is typically measured by its accuracy, when using an independent test set, by calculating the percentage of the data instances that are correctly classified. It was not our goal to compare AntMiner+ with different techniques as it was compared previously [12].

## 4.3. The use of AntMiner+

Rule lists provide insight into decision making, which is a key requirement when we need to understand which B/ICT strategic practices lead to highly aligned organisations. The AntMiner+ technique achieved a significantly higher accuracy and ranked as best for both accuracy and comprehensibility [14].

In order to use AntMiner+ for our analysis, we transformed our B/ICT alignment score variable into a categorical variable: highly or poorly aligned. We did this by labelling the organisations that scored less than average on the B/ICT alignment score variable as poorly aligned and those who scored more than average as highly aligned. We checked the robustness of our categories by performing the analysis also for the 10% best vs. the 10% worst and the 25% best vs. 25% worst scoring organisations. Our results passed this robustness test, as similar rules were inferred.

## 5. Results

The system infered two rules from our data. These provided accurate predictions for 69% of the companies in our data set.

As it was established by means of a survey of several organisations, contradictory data inevitably occured. Because of such idiosyncrasies, or noise, better accuracy will be hard to achieve by any model. Having two rules that provide accurate predictions for almost 70% of the data is a reasonable result.

Rules resulting from our analysis were

1. If Q4  3 and $\mathbf { Q 1 3 } \leq \mathbf { 2 }$ and Q7  3 and Q11  3 and Q6  3 then class = 0

2. If Q13  3 and Q7  2 and Q3  2 and Q11  2 then class = 0 3. else class = 1

where 1 = strongly agree, 2 = agree, 3 = neither agree nor disagree, 4 = disagree, 5 = strongly disagree, while class = 0 means highly aligned and class = 1 means poorly aligned.

The important advantage of using AntMiner+ as our analysis tool was the fact that it generated comprehensible rules that could be represented as simple if-then-else statements.

The If-Then-Else rules inferred by AntMiner+ were The If-Then-Else rules inferred by AntMiner+ were

If Business and ICT planning processes are tightly integrated

And Performance management impacts budget allocation

And Alignment processes at a centralised and

And ICT investments are prioritised against business strategy

And There is a clear business ownership for ICT projects

Then Organisation is highly aligned

Else if Performance management impacts budget allocation

And Alignment processes at a centralised and decentralised level are in line

And The business has a good understanding of the impact of ICT

And ICT investments are prioritised against business strategy

Then Organisation is highly aligned

Else Organisation is poorly aligned

## 6. Discussion

The rules inferred made one result clear: B/ICT strategy alignment is a complex and multidimensional operation. A combination of four or five different practices was needed so that organisations could score high on the alignment score variable. Furthermore, there was no alignment category that dominated the rules. Both were a combination of partnership, communication, governance, architecture, and value measurement categories. This was an important result for practitioners. Investing in only one of these alignment categories would not lead to better B/ICT strategic alignment. Our results clearly indicated that the combination of these different categories made for a high alignment.

Our first rule combined five alignment practices. First, business and ICT planning and management processes should be tightly connected and integrated. This has, of course, been well known and discussed for many years [15]. Second, ICT performance management should impact budget allocation. Again, this result has long been known in practice: organisations need to monitor and measure their performance and use this to steer ICT budget allocation. Third, strategic B/ICT alignment processes at a centralised level have to be in line with decentralised strategic alignment processes. Thus, as stated in many articles since the 1970s, it is important for organisations to ensure that alignment processes are common between headquarters and subsidiaries, etc. Fourth, ICT investment spending should be prioritised against business strategy. This makes sure that organisations only spend money on ICT investments that relate to business requirements and not just technological improvement. This results in an ICT investment portfolio that better supports business. Finally, there should be a clear business ownership for ICT projects. Business and ICT should be partnered in every ICT project. Business ownership makes management responsible for the outcome and fit of technology and business requirements.

The two rules together state that

\- ICT investments should be prioritised according to business strategy needs.

\- Performance management should impact budget allocation.

\- Alignment processes at a centralised and decentralised level should be in synchronism.

We concluded that the combination of the three core alignment practices is the minimal necessary set to obtain high alignment. However, they always have to occur in combination.

The second rule added only one other practice: the business must have a good understanding of the impact of ICT. This understanding has often been discussed also as a way to improve informed business decisions depending on the limitations and possibilities of ICT. Managers who understand both their core business and the impact of ICT on it can use this knowledge to better leverage ICT innovation.

The resulting rule set is thus not surprising. Indeed, we selected the initial set of practices from studies in the literature. Our goal was to generate insight on B/ICT alignment practice by inferring a set of core rules from a set of possible proposed good-practice. Our important contribution was to indicate that previously proposed interventions should not be used in isolation. Our study revealed that techniques only have high discriminative power in combination with the others.

Compared to the work of Luftman and Brier, our study revealed both similarities and differences. In their study the six most important enablers were senior executive support for ICT, ICT involved in strategy development, ICT understanding the business, business/ICT partnership, well-prioritised ICT projects, and ICT demonstrating leadership. Our results were thus in line with some of theirs. We can assume that managers should at least pay attention to these practices.

## 7. Limitations

There are inherent limitations in our study warranting caution in interpreting and applying our findings. First, our measure of alignment was based on a matching score method. There are different ways of measuring alignment effects; they could lead to different results and alignment rule sets.

Next, the results were based on a set of 18 alignment practices. We cannot claim that these are exhaustive. Adding new and different practices could change the rule set. Furthermore, we had to be careful about generalizing our results. Though our sample was quite large, we cannot claim it was representative of a general population in different countries, industries, and company sizes.

Finally, subjective data were collected in our study: scores were based on perceived and self-assessed results. We did not elaborate on the assumed causality between the set of practices and B/ICT alignment, though we believe that an inferred rule set of practices would lead to a highly aligned organisation.

## 8. Conclusion

In summary, our study contributed to understanding B/ICT alignment: first, the literature review gave us a theoretical base on which to frame the study. Second, our data set from 641 European organisations allowed us to use a novel data mining technique to infer simple and understandable B/ICT alignment rules. These provided a guideline for practitioners; they indicated patterns of B/ICT alignment practice in highly aligned organisations. Our goal was to group the important practices and search for the best combination instead of merely focusing on single interventions. Thus our work has contributed to a better understanding of the practice of B/ICT alignment.

## Appendix A. B/ICT alignment measure

A measure of alignment was made by using matching of comparable items, as shown:

5. Innovations in ICT are taken into account when determining the business strategy.

6. Your organisation fosters a clear business ownership for ICT projects.

## Architecture

7. Strategic business/ICT alignment processes at a centralised level are in line with strategic business/ICT alignment processes at a decentralised level.

8. Business processes are adequately supported by ICT.

9. Your organisation systematically determines the impact of new ICT investments on existing business processes, systems and infrastructure.

![](/api/attachments/K6CUEUCU/fulltext/images/1a0d9bba361279e2f2cffe8275fd887da56afc494ecc446e33855009e603be49.jpg)

The pairs compared from the B and ICT sections were

<table><tr><td>Business</td><td>ICT</td></tr><tr><td>ICT plays an important role in meeting customer requirements</td><td>We have a high adoption of CRM systems</td></tr><tr><td>ICT plays an important role in obtaining better management information</td><td>We have a high adoption of business intelligence and knowledge management systems</td></tr><tr><td>ICT plays an important role in cost reduction and efficiency improvement</td><td>We have a high adoption of transactional and ERP systems</td></tr><tr><td>ICT plays an important role in enterprise integration</td><td>We have a high adoption of enterprise application integration systems</td></tr><tr><td>ICT plays an important role in product development</td><td>We have a high adoption of product lifecycle management systems</td></tr></table>

## Appendix B. B/ICT questionnaire on alignment interventions

In your organisation, please rate each question by values ranging from: 1 = strongly disagree to 5 = strongly agree

## Communication

1. Business and ICT speak the same language.

2. Business and ICT management have a shared vision of the role of ICT in enabling business strategies.

3. Business management has a good understanding of the impact of ICT on the business.

## Partnership

4. Business and ICT planning and management processes are tightly connected and integrated.

## Value measurement

10. Your organisation is able to clearly demonstrate the value for its ICT investments.

11. New ICT investment and enhancement spend is prioritised against business strategy.

12. The performance of new ICT investment projects is regularly monitored and benchmarked against strategic objectives.

## Governance

13. ICT performance management impacts budget allocation.

14. There is transparency in the levels of authority and responsibilities for making decisions with respect to ICT projects.

15. There is transparency in the levels of accountability for outcomes for ICT projects.

## Human resource

16. Your organisation is able to minimise the resistance to change that comes with new ICT projects.

17. Your organisation fosters a clear stakeholder management for ICT projects.

18. In your organisation key-users participate in the design and development of new ICT systems.

## References

[1] B. Baesens, T. Van Gestel, S. Viaene, M. Stepanova, J. Suykens, J. Vanthienen, Benchmarking state-of-the-art classification algorithms for credit scoring, Journal of the Operational Research Society 54 (6), 2003, pp. 627–635.

[2] F. Bergeron, L. Raymond, S. Rivard, Ideal patterns of strategic alignment and business performance, Information and Management 41 (8), 2004, pp. 1003– 1020.

[3] Y.E. Chan, S.L. Huff, D.W. Barclay, D.G. Copeland, Business strategy orientation information systems orientation and strategic alignment, Information System Research 8 (2), 1997, pp. 125–150.

[4] G. Di Caro, M. Dorigo, Antnet: distributed stigmergetic control for communications networks, Journal of Artificial Intelligence Research 9, 1998, pp. 317–365.

[5] M. Dorigo, V. Maniezzo, A. Colorni, The ant system: optimization by a colony of cooperating agents, IEEE Transactions on Systems, Man, and Cybernetics Part B: Cybernetics 26 (1), 1996, pp. 29–41.

[6] M. Dorigo, T. Stu¨ tzle, Ant Colony Optimization, Bradford Book, 2004.

[7] M. De Backer, R. Haesen, D. Martens, B. Baesens, A stigmergy based approach to data mining, Lecture Notes in Computer Science, Springer, 2005 pp. 975– 978.

[8] G.S. Kearns, A.L. Lederer, The impact of industry contextual factors on IT focus and the use of IT for competitive advantage, Information & Management 41, 2004, pp. 899–919.

[9] J.N. Luftman, P.R. Lewis, S.H. Oldach, Transforming the enterprise: the alignment of business and information technology strategies, IBM Systems Journal 32 (1), 1993.

[10] J.N. Luftman, T. Brier, Achieving and sustaining business-IT alignment, California Management Review 42 (1), 1999.

[11] J.N. Luftman, Assessing IT/business alignment, Information Systems Management 20 (4), 2003.

[12] D. Martens, M. De Backer, R. Haesen, B. Baesens, T. Holvoet, Ants constructing rule-based classifiers, Swarm Intelligence and Data Mining, Springer, 2006 pp. 21–44 (chapter 2).

[13] D. Martens, M. De Backer, R. Haesen, B. Baesens, C. Mues, J. Vanthienen, Antbased approach to the knowledge fusion problem, in: M. Dorigo, L. Gambardella, M. Birattari, A. Martinoli, R. Poli, T. Stu¨ tzle (Eds.), Ant Colony Optimization and Swarm Intelligence, 5th International Workshop, ANTS 2006, Lecture Notes in Computer Science, 4150, Springer-Verlag, Berlin, Germany, 2006 , pp. 84–95.

[14] D. Martens, M. De Backer, R. Haesen, M. Snoeck, J. Vanthienen, B. Baesens, Classification with ant colony optimization, IEEE Transactions on Evolutionary Computation 9 (5), 2007, pp. 651–665.

[15] D. Peak, S.C. Guynes, V. Kroon, Information technology alignment planning—a case study, Information & Management 42, 2005, pp. 619–633.

[16] B.H. Reich, I. Benbasat, Factors that influence the social dimension of alignment between business and information technology objectives, MIS Quarterly 24 (1), 2000, p. 81.

[17] R. Sabherwal, R. Hirschheim, T. Goles, The dynamics of alignment: insights from a punctuated equilibrium model, Organisation Science 12 (March–April(2)), 2001, pp. 179–197.

[18] P.P. Tallon, K.L. Kraemer, V. Gurbaxani, Executives’ perceptions of the business value of information technology: a process-oriented approach, Journal of MIS 16 (4), 2000, pp. 145–173.

![](/api/attachments/K6CUEUCU/fulltext/images/68862152403d8a19c9e95cc6cfda2c3cb0609638dc65ff458ce7056c26bc0a4e.jpg)

Bjorn Cumps holds a PhD in applied economic sciences from the Katholieke Universiteit Leuven (K.U. Leuven, Belgium). For his research he is connected to both the Department of Decision Sciences and Information Management at the Katholieke Universiteit Leuven and the Operations & Technology Centre of the Vlerick Leuven Gent Management School. His research focuses on Business-ICT alignment ICT management ICT governance and ICT outsourcing. Dr. Cumps is also an internal advisor for KBC Group, a mid-sized European financial institution where he helps implement Business Process Management and Business Architecture as

B-ICT alignment instruments. His findings have been published in international journals (CAIS, IEEE IT professional) and presented at international top conferences (ICIS, ECIS).

![](/api/attachments/K6CUEUCU/fulltext/images/fcb4cad846fc72844471d2852ea98c99b9d2a0b55858b48563c70850a80a95e8.jpg)

David Martens is lecturer at the Department of Business Administration and Public Management at Hogeschool Gent, Belgium, and post-doctoral researcher at the Department of Decision Sciences and Information Management at Katholieke Universiteit Leuven (K.U. Leuven), Belgium. He received the MS degree in civil engineering from the Department of Computer Science, K.U. Leuven, in 2003, and the Master of Business Administration degree from Reims Management School, France, in 2005. In 2008, he received a PhD in Applied Economic Sciences from the Department of Decision Sciences and Information Management of K.U.

Leuven. His research is mainly focused on the development of comprehensible data mining techniques, using Ant Colony Optimisation and Support Vector Machines with main application Basel II-compliant credit scoring systems

![](/api/attachments/K6CUEUCU/fulltext/images/aa733c3f215ce7b60b1e3988d01e5127eeff6463e9840374692a8a634b537493.jpg)

Manu De Backer holds a PhD in Applied Economic Sciences from Katholieke Universiteit Leuven. He is an associate professor in the Department of Management Information Systems of the University of Antwerp and a lecturer at the Hogeschool Gent. He also holds a research position at the K.U. Leuven. His research focuses on the verification of business process models and the consistency and integration of business process models with other conceptual models. Other research interests are data mining with ACO and BPMN.

![](/api/attachments/K6CUEUCU/fulltext/images/ad356b841d81aa9648240b9b4aee43b247f4dc810b2300bbf15963607acbd912.jpg)

Raf Haesen is a PhD student at the KBC-HUBrussel-K.U. Leuven Research Centre. His research interests include object-oriented conceptual modelling, service and component-based architecture, and model-driven development. He received his Civil Engineering degree from the Computer Science Department at K.U. Leuven.

![](/api/attachments/K6CUEUCU/fulltext/images/3fecc93e7cd62747836ce9c4fc98958d61264e1bff5767cc24c757c3f89a47f1.jpg)

Stijn Viaene is an associate professor of Information Systems at K.U. Leuven, Belgium, and at Vlerick Leuven Gent Management School. where he chairs the Competence Center Operations and Technology Management. He received his PhD from the Faculty of Economics and Applied Economics, K.U. Leuven. His research and teaching reflect a wide spectrum of managerial issues in business-ICT alignment and information systems management, with a particular interest in realizing the benefits from Business Intelli gence systems. Dr. Viaene is in charge of the K.U. Leuven Research Chair on Knowledge Discovery in Databases endowed by the Dutch Police Region Amsterdam-Amstelland, and the Vlerick Research Center on Business Intelligence sponsored by SAS Institute. He has published in such journals as IEEE TKDE, ML, IJIS, JORS, ESWA, EJOR, CAIS, and IEEE IT Professional.

![](/api/attachments/K6CUEUCU/fulltext/images/1395d544a86dc59af1f5fc44f65e38dc9b1665b3e31c19620780aa4f6cd28614.jpg)

Guido Dedene has a PhD in Sciences (Mathematics), which he received at the Katholieke Universiteit Leuven (K.U. Leuven, Belgium). He is a full professor in Management Informatics at the K.U. Leuven (Faculty of Economics and Business) and a professor in Development of Information and Communication Systems at the University of Amsterdam Business School. His teaching activities focus on Methods and Techniques of Information & Communication Systems Development, the Economics of Information & Communication Services, and the Management of Information & Communication Technology. His research includes

the Model-driven Development of Information & Communication Systems and Quantitative Management Models for Information & Communication Technology and Systems. He is a board member for several IT-Innovation related organisations and coordinates for more than 10 years the Industry Fellows Programme of the Faculty of Economics and Business at K.U. Leuven.

![](/api/attachments/K6CUEUCU/fulltext/images/dba1dbcb367e0b875287e51914ad96b29c1cbe59e24608f8af9180db9c044fdd.jpg)  
Bart Baesens is an assistant professor at K.U. Leuven (Belgium), and a lecturer at the University of Southampton (United Kingdom). He has done extensive research on predictive analytics, data mining and credit risk management. His findings have been published in well-known international journals and presented at international top conferences. He regularly tutors, advices and provides consulting support to international firms with respect to their data mining, predictive analytics, and credit risk management policy.

![](/api/attachments/K6CUEUCU/fulltext/images/eed7f456175d118386a9ef71536f3a21283e2721c017469fa73b874bdfe4017a.jpg)

Monique Snoeck holds a PhD in computer science from the Katholieke Universiteit Leuven. She is full professor in the department of Decision Sciences and Information Management of the Faculty of Business and Economics of the Katholieke Universiteit Leuven and visiting professor at the Faculte´s Universitaires Notre Dame de la Paix, Namur. Her research focuses on conceptual modeling, requirements engineering, software architecture, model-driven engineering and business process management.
