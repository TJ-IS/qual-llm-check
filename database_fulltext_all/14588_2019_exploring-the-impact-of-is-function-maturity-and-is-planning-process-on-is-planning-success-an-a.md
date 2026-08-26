---
otero_id: 14588
otero_key: "3STD2XYZ"
title: "Exploring the impact of IS function maturity and IS planning process on IS planning success: an ACE analysis"
authors: "Tomoaki Shimada; James Ang Soo-Keng; Darren Ee"
year: "2019"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2018.1557373"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exploring the impact of IS function maturity and IS planning process on IS planning success: an ACE analysis

Tomoaki Shimada, James Ang Soo-Keng & Darren Ee

To cite this article: Tomoaki Shimada, James Ang Soo-Keng & Darren Ee (2018): Exploring the impact of IS function maturity and IS planning process on IS planning success: an ACE analysis, European Journal of Information Systems, DOI: 10.1080/0960085X.2018.1557373

To link to this article: https://doi.org/10.1080/0960085X.2018.1557373

![](/api/attachments/3STD2XYZ/fulltext/images/86417ce42ef0259f4b8e025f9d700504d4224eab05c85e14aaa7caa6fd8bfaa4.jpg)

Published online: 20 Dec 2018.

![](/api/attachments/3STD2XYZ/fulltext/images/d3884ad65c0656b9d03af6bc035dce798b19c71181f701bf1a474381551fdc46.jpg)

Submit your article to this journal

![](/api/attachments/3STD2XYZ/fulltext/images/b9d09dc3226e8c4baf7305b3b3a5bbb06bd8fe5a31b710f3f47ca5015fef62d0.jpg)

Article views: 12

![](/api/attachments/3STD2XYZ/fulltext/images/ef51eabbe5efd9644f2e003505443f4f12cde4003c507aa9d9012f1943f9cb80.jpg)

View Crossmark data CrossMark

EMPIRICAL RESEARCH

Check for updates

# Exploring the impact of IS function maturity and IS planning process on IS planning success: an ACE analysis

Tomoaki Shimada <sup>a</sup>, James Ang Soo-Keng<sup>b</sup> and Darren Ee<sup>c</sup>

<sup>a</sup>The NUCB Business School, Nagoya University of Commerce and Business, Aichi, Japan; <sup>b</sup>The Logistics Institute - Asia Paci<sup>fi</sup>c, Nationa University of Singapore, Singapore, Singapore; <sup>c</sup>Department of Analytics and Operations, National University of Singapore, Singapore, Singapore

## ABSTRACT

We examine the impact of information system (IS) function maturity and IS planning process on IS planning success in an exploratory approach. We conducted non-linear regression analysis using the Alternating Conditional Expectations algorithm, and found signi<sup>fi</sup>cant non-linear relationships between the dimensions of IS function maturity/IS planning process and those of IS planning success. We also visualised how various IS planning success measures can evolve with low or high values of determinant variables. We used four dimensions of capabilities, analysis, cooperation, and alignment to evaluate IS planning success. We also employed four dimensions to analyse each of IS function maturity and IS planning process. IS function maturity consists of IT planning mode, IT integration, IT industry practice, and IT perspective. On the other hand, IS planning process is composed of long-range planning, medium-range managerial planning, short-range operational planning, and organisational IT potential.

ARTICLE HISTORY Received 2 September 2015 Revised 10 August 2018 Accepted 4 November 2018

ACCEPTING EDITOR Prof. Frantz Rowe

ASSOCIATE EDITOR Prof. Paul Alpar

KEYWORDS IS function maturity; IS planning process; IS planning success; nonlinear regression analysis; Alternating Conditional Expectations algorithm

## 1. Introduction

Information systems (IS) planning has been pertinent to rapidly evolving business environment. With the acceleration of globalisation and computerisation of business processes over the past three decades, organisations have had to constantly upgrade their processes to keep pace. IS planning has remained at the forefront of this progress and has consistently ranked among the top issues facing IS professionals over the last half-century.

Many aspects of IS planning have been examined. For example, the link between IS planning and business objectives (eg, King, 1978; Lederer & Sethi, 1988; Teo & King, 1997), problems and challenges associated with the IS planning process (eg, Conrath, Ang, & Mattay, 1992; Goodhue, Kirsch, Quillard, & Wybo, 1992; Teo & Ang, 2001), antecedents to IS planning success (eg, Basu, Hartono, Lederer, & Vijay, 2002; Bechor, Neumann, Zviran, & Glezer, 2010), e<sup>f</sup>ectiveness of IS planning (eg, Grover & Segars, 2005; Segars, Grover, & Teng, 1998; Wang & Tai, 2003), IS planning in an uncertain environment (Mirchandani & Lederer, 2012; Newkirk & Lederer, 2006a, 2006b), and methodologies for conducting IS planning (eg, King, 1988; Li & Chen, 2001; Segars & Grover, 1999).

King and Teo (1997) classi<sup>fi</sup>ed the evolution of IS planning into three stages, and Mangalaraj (2014) added two stages as follows: (1) The pre-strategic IS planning era in the early to mid-1970s: The research focus was assessment of future computing needs. (2) The early strategic IS planning era in the late 1970s: Top management involvement with strategic planning was crucial. (3) The modern IS planning era in the late 1980s: E<sup>f</sup>ectiveness consideration and IS planning became part of business planning. (4) The alignment era in the late 1990s: IS planning became part of the process to align business and IS strategy. (5) The uncertainty era in the late 2000s: The research focus was the comprehensiveness of IS planning under uncertain environmental conditions.

Although several new methods are introduced in IS development for the last decade, IS planning is still fundamental to IS development because IS cannot be developed without planning. For example, agile software development methodologies (eg, Dingsoyr & Lassenius, 2016; Nerur, Mahapatra, & Mangalaraj, 2005) including DevOps practices (eg, Bass 2018; Zhu, Bass, & Champlin-Schar<sup>f</sup>, 2016) are the extension of IS planning.

Several methodologies for evaluating IS planning success have also been proposed. Some of these techniques make the assumption that IS planning success translate accordingly into tangible bene<sup>fi</sup>ts (eg, improved <sup>fi</sup>nancial performance) and/or intangible bene<sup>fi</sup>ts (eg, improved communication and cooperation). Although IS planning is recognised as an intricate and complex, most studies have built linear models to analyse the antecedents to IS planning success. In fact, the factors a<sup>f</sup>ecting IS planning success may not always have linear relationships with IS planning success (eg, Newkirk, Lederer, & Cidambi, 2003; Newkirk, Lederer, & Johnson, 2008).

In this study we do not examine IS planning in an uncertain environment, which is research trend for these two decades. Instead we introduce a new research method to the traditional research topic in IS planning. Speci<sup>fi</sup>cally, we explore the non-linear relationship between IS function maturity, IS planning process, and the organisation’s subsequent IS planning success using Alternating Conditional Expectations (ACE) algorithm, as shown in Figure 1. We use four dimensions of capabilities, analysis, cooperation, and alignment to evaluate IS planning success. We also employ four dimensions to analyse each of IS function maturity and IS planning process. IS function maturity consists of IT planning mode, IT integration, IT industry practice, and IT perspective. We use the term “IS function maturity” for “IT maturity” because IT maturity in this study is IS function maturity in substance. On the other hand, IS planning process is composed of long-range planning, medium-range managerial planning, short-range operational planning, and organisational IT potential.

The contributions of this study are twofold. First, using data collected from the self-administrated questionnaire survey, we explore the relationships between the dimensions of IS function maturity and those of IS planning success as well as between the dimensions of IS planning process and those of IS planning success. Second, to investigate the relationships, we apply ACE algorithm in a non-linear regression approach and visualise how various IS planning success measures can evolve with low or high values of determinant variables.

Following the introduction, Section 2 reviews the literatures on IS function maturity, IS planning process, and IS planning success. Sample data, variables, validity and reliability, and ACE algorithm are explained in Section 3. Section 4 illustrates the outputs from the utilisation of ACE and discusses the main results. Section 5 summarises the conclusions and provides the managerial implications of the study.

## 2. Literature review

## 2.1. IS function maturity

The concept of IS function maturity was initially coined in a study by Churchill, Kempster, and Uretsky (1969), to determine how managers used computer-based IS (Karimi, Gupta, & Somers, 1996). Later, Nolan (1973) developed one of the best known stages of growth models in IS, the “Stage Hypothesis”, which describes the assimilation of computer technology in organisations. Nolan (1973) proposed that the growth of computing follows an S-shaped curve which can be divided into four stages: initiation, contagion, control, and integration. Nolan (1979) further included two additional stages into his original model: data administration and maturity, thereby creating a six-stage model.

Many researchers subjected di<sup>f</sup>erent aspects of Nolan’s (1979) stage hypothesis to empirical studies in attempts to verify his <sup>fi</sup>ndings (Benbasat, Dexter, & Mantha, 1980; Farhoomand & Gatehouse, 1988; Grover & Segars, 2005). Benbasat, Dexter, Drury, and Goldstein (1984) utilised Nolan’s (1979) stage hypothesis and developed a nine-item instrument to measure IT maturity. Although this study did not support Nolan’s stage hypothesis, it did support the hypothesis concerning progression towards increasingly formalised management of the IS function. In other studies, it was revealed that the IS function in <sup>fi</sup>rms that possessed a higher level of IT maturity should have evolved from a simple data-processing orientation to a more strategic one (McFarlan, 1984; Sabherwal & King, 1992; Ward, Gri<sup>fi</sup>ths, & Whitmore, 1990).

Karimi et al. (1996) carried out a pre-testing of the nine-item instrument developed by Benbasat et al.

![](/api/attachments/3STD2XYZ/fulltext/images/782525017ecb8eeca55fe5b6d0e1b381604c982d74e8e2bcc6e1389bf63ca84f.jpg)  
Research framework.

(1984). Feedback from the pre-testers (IS managers) revealed that factors a<sup>f</sup>ecting IT maturity were much broader. Karimi et al. (1996) then developed a more comprehensive IT maturity scale based on four criteria (IT planning mode, IT control mode, IT organisation, and IT integration), which are in turn represented by 20 items. They also found that IT maturity variables have more predicting power to forecast <sup>fi</sup>rms’ perceived increase in IT investment than competitive strategy or size.

Poeppelbuss, Niehaves, Simons, and Becker (2011) conducted a literature review on IT maturity models, and found that Capability Maturity Model (CMM) is the most dominant foundation of past IT maturity models from the research perspective. CMM consists of the <sup>fi</sup>ve maturity levels: 1. initial; 2. repeatable; 3. de<sup>fi</sup>ned; 4. capable; and 5. e<sup>fi</sup>cient (Humphrey, 1989). Although we did not use the CMM for the constructs, we use the model to explain the nonlinear relationships as a result of ACE analysis.

## 2.2. IS planning process

McLean and Soden (1977) conceptualised the IS planning process into three stages: long-range strategic planning, medium-range managerial planning, and short-range operational planning. Premkumar and King (1994) de<sup>fi</sup>ned the IS planning process as comprising “a set of activities that transforms the information inputs from business plans, external sources, and IS users into plans that guide the development of the IS function”. These plans include the development strategy, system purpose, system selection priorities, system functions, function goals, function requirements, and documentation (Ein-Dor & Segev, 1978).

Even though the value of IS planning has long been recognised, IS planning issues have changed over time. Early IS planning studies concentrated on application development issues (McFarlan, 1971). Blumenthal (1969) described the IS planning process as one of reviewing proposed systems against predetermined criteria to minimise resource duplication and maximise functionality. Later this operational focus has been replaced by a more strategic slant. Earl (1989) demonstrates this change, proposing that IS strategy focuses on systems or business applications of IT, and the aligning of these with business needs to derive strategic bene<sup>fi</sup>ts. The importance of aligning IS planning with business strategy is well recognised (King, 1978; King & Teo, 1997). Several researchers have since studied the need to link IS planning process with business planning (Henderson & Venkatraman, 1993; King, 1978).

Sabherwal (1999) incorporated the IS planning process into his de<sup>fi</sup>nition of IS sophistication. He de<sup>fi</sup>nes an organisation’s IS planning sophistication as “the extent to which the IS planning process helps create opportunities for information systems to make a strategic contribution in the organization”. While traditionally, there has been an implicit assumption that a sophisticated IS planning process leads to greater IS planning success, his research provides empirical evidence to support the reverse linkage of a high level of IS success being necessary for IS managers to persuade top management to take the necessary actions required to raise the level of IS planning sophistication.

In the late 1990s some IS researchers started to have a critical view towards IS planning due to the in<sup>fl</sup>exibility to dynamically adjust the IS development process according to changing technologies and new demands from users. Then, agile software development methodologies emerged in 2001 to meet the changing requirements of the companies which adapt their structures, strategies, and policies to suit the new environment (Dingsoyr, Nerur, Balijepally, & Moe, 2012). Agile software development methodologies are characterised by social inquiry in which extensive collaboration and communication provide the basis for collective action (Nerur et al., 2005). Among agile software development methodologies, extreme programming and Scrum has been popular in the past decade, while more and more companies recently move towards continuous value delivery such as DevOps and the practice of “continuous integration” (Dingsoyr & Lassenius, 2016).

## 2.3. IS planning success

IS planning encompasses a multitude of managerial, system and technological components over a certain time horizon (McLean & Soden, 1977; Raghunathan & Raghunathan, 1994; Wilkin & Cerpa, 2012). Thus, the di<sup>f</sup>erent stakeholders, namely, IS managers, user managers and top management in the organisation, de<sup>fi</sup>ne IS planning success di<sup>f</sup>erently (Earl, 1993). To overcome this complexity, several researchers have proposed using multi-dimensional terms to measure IS planning success (King, 1988; Venkatraman & Ramanujam, 1987). The use of multiple, interrelated success dimensions, which are in turn captured by multiple indicators, is more e<sup>f</sup>ective than utilising an all-encompassing scale item or <sup>fi</sup>nancial indicators to measure IS planning success (Segars & Grover, 1998).

Four major approaches for assessing IS planning success of an organisation were also uncovered (Segars & Grover, 1998). They are the goal-centred approach, the comparative approach, the normative approach, and the improvement-oriented approach. These four di<sup>f</sup>erent approaches for evaluating IS planning success are based on the work of Cameron and Whetten (1983) in relation to organisation e<sup>f</sup>ectiveness measurement. Although all four have their merits, two speci<sup>fi</sup>c approaches (ie, a combination of the goalcentred approach and the improvement-oriented approach) were selected for use in this study. The comparative and the normative approaches are more relevant for evaluating speci<sup>fi</sup>c planning methodologies such as strategic data planning, which have a narrower focus, a more concise set of outcomes, and a de<sup>fi</sup>ned time horizon (Goodhue et al., 1992).

Segars and Grover (1998) following Venkatraman and Ramanujam (1987) and Raghunathan and Raghunathan (1994), utilised a combination of the goal-centred and improvement-oriented approaches in modelling IS planning success. They identi<sup>fi</sup>ed three broad dimensions of objective ful<sup>fi</sup>lment (alignment, analysis, and cooperation) in the goal-centred approach, and one additional dimension of improvement in capabilities which equated to the improvement-oriented approach. The eventual model developed to measure IS planning success comprised of six measures for alignment, six measures for analysis, seven measures for cooperation, and seven measures for improvement in capabilities.

The DeLone and McLean Model, which were updated a few times due to its complexity, is popularly used to measure IS success (DeLone & McLean, 1992, 2003, 2016). The recent model consists of six dimensions as follows: system quality, information quality, service quality, use, user satisfaction, and net impacts. However, these six variables are interdependent, and some interrelationships are recognised as both positive and negative at an individual level as well as at an organisational level (DeLone & McLean, 2016; Petter, DeLone, & McLean, 2008). We did not employ the DeLone and McLean Model because our study focuses on IS planning success and not compound IS success. Therefore, business value of IS to a company is not explicitly included in the measurement of IS planning success.

## 3. Methodology

## 3.1. Sample and data collection

The researchers and one research assistant spent two weeks telephoning 1500 companies which were randomly chosen from the Singapore Telephone Book (Business Listing). Only companies with a formal IS department quali<sup>fi</sup>ed as participants. The name of the highest ranking IS executive in the companies was requested. This sampling procedure generated a sample base of 500 potential respondents from 500 companies. Each of them were mailed a survey questionnaire, with a cover sheet explaining the objectives of the study. A prepaid, self-addressed envelope was also included to facilitate responses from the participants. One month after the initial mailing, a reminder letter was sent out to participants that had not responded. A follow-up telephone call was subsequently made to try to elicit a higher response rate. Five questionnaires were returned as undeliverable, and a total of 109 companies responded. Of these, 80 practiced strategic IS planning while 29 did not. The response rate of 22.02% for this study.

The questionnaire consists of four sections. The <sup>fi</sup>rst section gathers demographic data of the participants. The other three sections measure the three main constructs. In order to ensure that the questionnaire was properly understood, it was piloted with <sup>fi</sup>ve senior IS practitioners. Minor modi<sup>fi</sup>cations were then made to produce the main study questionnaire. Our <sup>fi</sup>nal questionnaire collected data on: (1) demographic pro<sup>fi</sup>le, (2) IS function maturity, (3) IS planning process, and (4) IS planning success.

Although the questionnaire was speci<sup>fi</sup>cally addressed to the head of the IS departments, there were variations in the job designations of the respondents. Table 1 presents the demographic characteristics of the sampled companies. Eighty-nine respondents held IS-related job titles, while the other 20 organisations had IT/IS departments that were overseen by non-IT/IS heads. For instance, in some companies, the IS department was directly overlooked by the general manager of the company. More signi<sup>fi</sup>cantly, 82% of the organisations that had speci<sup>fi</sup>c IT/IS heads of departments practicing IS planning against 35% for those whose IT/IS departments that were overseen by non-IT/IS heads. Majority adopt a functional or matrix structure. Additionally, <sup>fi</sup>rms with IS planning tend to be larger in size (in terms of the number of employees) than <sup>fi</sup>rms without IS planning.

Demographic characteristics of respondents.

<table><tr><td rowspan="2"></td><td colspan="2">IS Planning</td></tr><tr><td>Yes(%)</td><td>No(%)</td></tr><tr><td colspan="3">IT/IS</td></tr><tr><td>Vice President/CIO</td><td>6.3</td><td>0</td></tr><tr><td>Director/General Manager</td><td>13.8</td><td>3.5</td></tr><tr><td>Manager</td><td>63.8</td><td>31.0</td></tr><tr><td>Senior IT Executive/Systems Analyst</td><td>7.5</td><td>20.7</td></tr><tr><td>Subtotal</td><td>91.3</td><td>55.2</td></tr><tr><td colspan="3">Non-IT/IS</td></tr><tr><td>Director/Deputy Director</td><td>2.5</td><td>6.9</td></tr><tr><td>General Manager/Manager</td><td>3.8</td><td>27.6</td></tr><tr><td>Accounts Manager/Finance Manager</td><td>1.3</td><td>3.5</td></tr><tr><td>Administrative Manager</td><td>1.3</td><td>6.9</td></tr><tr><td>Subtotal</td><td>8.8</td><td>44.8</td></tr><tr><td colspan="3">Company business</td></tr><tr><td>Airline</td><td>0</td><td>0</td></tr><tr><td>Auditing/Management Consulting</td><td>2.5</td><td>10.3</td></tr><tr><td>Banking/Finance/Insurance</td><td>18.8</td><td>6.9</td></tr><tr><td>Computer/Telecommunications</td><td>13.8</td><td>0</td></tr><tr><td>Engineering</td><td>5.0</td><td>3.5</td></tr><tr><td>Entertainment</td><td>1.3</td><td>3.5</td></tr><tr><td>Hotels/Travel</td><td>3.8</td><td>13.8</td></tr><tr><td>Logistics/Freight Forwarders</td><td>6.3</td><td>0</td></tr><tr><td>Manufacturing</td><td>22.5</td><td>20.7</td></tr><tr><td>Petroleum/Chemicals</td><td>2.5</td><td>0</td></tr><tr><td>Real Estate</td><td>3.8</td><td>0</td></tr><tr><td>Retailer/Wholesaler</td><td>2.5</td><td>24.1</td></tr><tr><td>Service</td><td>10.0</td><td>13.8</td></tr><tr><td>Others</td><td>7.5</td><td>3.5</td></tr><tr><td colspan="3">Organisational structure</td></tr><tr><td>Functional (ie, division by production, marketing, accounting, etc.)</td><td>55.0</td><td>37.9</td></tr><tr><td>Product (ie, division by product/service produced)</td><td>16.3</td><td>24.1</td></tr><tr><td>Matrix (mixture of above two, subordinates report to multiple managers)</td><td>28.8</td><td>37.9</td></tr><tr><td colspan="3">Number of employees</td></tr><tr><td>&lt;100</td><td>8.8</td><td>6.9</td></tr><tr><td>100–500</td><td>18.8</td><td>17.2</td></tr><tr><td>500–1000</td><td>0</td><td>0</td></tr><tr><td>1000–5000</td><td>13.8</td><td>31.0</td></tr><tr><td>&gt;5000</td><td>42.5</td><td>24.1</td></tr><tr><td>Missing value</td><td>16.3</td><td>20.7</td></tr></table>

## 3.2. Variables

The two independent variables for this study are the IS function maturity of an organisation and the IS planning process it undertakes, whereas the dependent variable is the eventual IS planning success the organisation attains. The operationalisation of each variable is as follows:

## 3.2.1. IS function maturity

Karimi et al. (1996) developed a 20-item instrument and found that the development of IS function in organisations has the following phases: IT planning mode, IT control mode, IT organisation, and IT integration. We employed Karimi et al.’s (1996) scale for IT maturity to measure IS function maturity. The responses were measured on a Likert scale from 1 to 5, with 5 being “strongly agree” and 1 being “strongly disagree”.

## 3.2.2. IS planning process

McLean and Soden (1977) in their seminal work conceptualised the IS planning process into three stages: long-range strategic planning, medium-range managerial planning, and short-range operational planning. In this study, the IS planning process scale was adapted from the 22-item instrument proposed by McLean and Soden (1977). The responses were measured on a Likert scale from 1 to 5, with 5 being “strong emphasis” and 1 being “weak emphasis”.

## 3.2.3. IS planning success

Segars and Grover (1998) theoretically developed and statistically tested a 26-item instrument of IS planning success. We used Segars and Grover (1998) measurement not only because it had been statistically tested but also because of its broad, multidimensional approach towards IS planning success. The responses were measured on a Likert scale from 1 to 5, with 5 being “entirely ful<sup>fi</sup>lled” and 1 being “entirely unful<sup>fi</sup>lled” for the goal-centred approach questions, and with 5 being “much improvement” and 1 being “much deterioration” for the improvement-oriented approach questions.

## 3.3. Validity and reliability

Factor analysis with promax rotation was used to assess construct validity. To determine the number of factors, we applied Kaiser’s eigenvalue-greater-than-one rule. For IS function maturity, four factors emerged (Table 2(a)). We called them: IT planning mode (ITPlan), IT integration (ITInt), IT industry practice (ITIndPrac), and IT perspective (ITPer). Karimi et al.’s factors were IT planning mode, IT control mode, IT organisation, and IT integration. Comparing the factors in this study to Karimi et al.’s, several di<sup>f</sup>erences are noted. The six variables comprising Karimi et al.’s IT planning mode factored across three factors, two of which (consisting of two items each) are distinct. We named them IT industry practice and IT perspective. The other two variables and those under the IT control mode and IT organisation factored under one factor in this study. We retained Karimi et al.’s IT planning mode for this factor.

Several reasons could account for the variation in factor loadings. First, the original study was conducted some time ago in the U.S. The level of adoption and usage of IT in <sup>fi</sup>rms have evolved rapidly over the years. Second, the level of IS function maturity of the respondents in this study varies from those in the previous study.

For IS planning process, four items, namely, “de<sup>fi</sup>ning the planning process”, “launching the formal planning e<sup>f</sup>ort”, “evaluating internal MIS group improvement needs”, and “evaluating potential projects” were eliminated and four factors emerged (Table 2(b)). We named the four factors: medium-range managerial planning (MRMP), long-range planning (LRP), short-range operational planning (SROP), and organisational IT potential (OrgITPot) (Table 2(b)). This is in line with McLean and Soden’s conceptualisation except that variables relating to medium-range managerial planning factored into two factors. We called them MRMP and OrgITPot. The former involves managerial planning issues, while the latter consists of variables relating to IT potential.

For IS planning success, <sup>fi</sup>ve items were eliminated, and four factors were extracted. We retain Segars and Grover (1998) four factors with some variations. They are Capabilities (an organisation’s versatility), Analysis (level of structural management), Cooperation (organisational collaboration), and Alignment (organisational integration) (Table 2(c)). Except for the Capabilities factor, the other three factors are similar to those of the original study. While the Capabilities factor comprised many of the original study’s planning capabilities factor variables, a few additional variables loaded onto this factor. This probably demonstrates that IT managers’ perception of the ability to improve on planning capabilities has expanded to incorporate more variables than when the original study was conducted.

Factor analysis results.

<table><tr><td>Items</td><td colspan="4">Loadings</td></tr><tr><td colspan="5">A: Factor analysis results on IS function maturity</td></tr><tr><td>F1: IT Planning mode (ITPlan)</td><td>0.7862</td><td></td><td></td><td></td></tr><tr><td>Our IT function is clear about its goals and responsibilities.</td><td></td><td></td><td></td><td></td></tr><tr><td>In our organisation, the responsibility and authority for IT operations are clear.</td><td>0.7576</td><td></td><td></td><td></td></tr><tr><td>In our organisation, the responsibility and authority for IT direction and development are clear.</td><td>0.7444</td><td></td><td></td><td></td></tr><tr><td>The IT specialist-user relations in our firm are constructive.</td><td>0.7382</td><td></td><td></td><td></td></tr><tr><td>We are contented with how our IT project priorities are set.</td><td>0.7339</td><td></td><td></td><td></td></tr><tr><td>We constantly monitor the performance of IT functions.</td><td>0.7200</td><td></td><td></td><td></td></tr><tr><td>The structure of our IT function fits our organisation.</td><td>0.7146</td><td></td><td></td><td></td></tr><tr><td>We are confident that IT project proposals are properly appraised.</td><td>0.7029</td><td></td><td></td><td></td></tr><tr><td>We have an adequate picture of the coverage and quality of our IT systems.</td><td>0.6920</td><td></td><td></td><td></td></tr><tr><td>Our IT function is clear about its performance criteria.</td><td>0.6566</td><td></td><td></td><td></td></tr><tr><td>In our organisation, user ideas are given due attention in IT planning and implementation.</td><td>0.6467</td><td></td><td></td><td></td></tr><tr><td>Our IT specialist understands our business and the firm.</td><td>0.5665</td><td></td><td></td><td></td></tr><tr><td colspan="5">F2: IT Integration (ITInt)</td></tr><tr><td>The introduction of, or experimentation with, new technologies takes place at the business unit level under business unit control.</td><td></td><td>0.8889</td><td></td><td></td></tr><tr><td>Some IT development resource is positioned within the business unit.</td><td></td><td>0.7424</td><td></td><td></td></tr><tr><td>There is a top-down planning process for linking information systems strategy to business needs.</td><td></td><td>0.7073</td><td></td><td></td></tr><tr><td>In my firm, top management perceives that future exploitation of IT is of strategic importance.</td><td></td><td>0.6962</td><td></td><td></td></tr><tr><td colspan="5">F3: IT Industry Practice (ITIndPrac)</td></tr><tr><td>We are adequately informed on the current use of IT by competitive forces (eg, buyers, suppliers, and competitors) in our industry.</td><td></td><td></td><td>0.7923</td><td></td></tr><tr><td>We are adequately informed of the potential use of IT by competitive forces (eg, buyers, suppliers, and competitors) in our industry.</td><td></td><td></td><td>0.7567</td><td></td></tr><tr><td colspan="5">F4: IT Perspective (ITPer)</td></tr><tr><td>We continuously examine the innovative opportunities IT can provide for competitive advantage.</td><td></td><td></td><td></td><td>0.7940</td></tr><tr><td>Our IT projects support the business objectives and strategies of our company.</td><td></td><td></td><td></td><td>0.7324</td></tr><tr><td>Eigenvalues</td><td>9.138</td><td>1.926</td><td>1.467</td><td>1.123</td></tr><tr><td>Percentage of variance</td><td>45.69</td><td>9.63</td><td>7.33</td><td>5.62</td></tr><tr><td>Cronbach's alpha</td><td>0.93</td><td>0.82</td><td>0.87</td><td>0.78</td></tr><tr><td colspan="5">B: Factor analysis results on IS planning process</td></tr><tr><td colspan="5">F1: Medium-Range Managerial Planning (MRMP)</td></tr><tr><td>Selecting most appropriate strategy alternatives.</td><td>0.8823</td><td></td><td></td><td></td></tr><tr><td>Translating selected strategy into action.</td><td>0.8781</td><td></td><td></td><td></td></tr><tr><td>Evaluating strategic alternatives.</td><td>0.8781</td><td></td><td></td><td></td></tr><tr><td>Translating strategy into short-term middle management performance milestones.</td><td>0.8369</td><td></td><td></td><td></td></tr><tr><td>Forecasting resource needs for each strategy.</td><td>0.8115</td><td></td><td></td><td></td></tr><tr><td>Identifying strategy alternatives.</td><td>0.7427</td><td></td><td></td><td></td></tr><tr><td>F2: Long-Range Planning (LRP)</td><td>0.7014</td><td></td><td></td><td></td></tr><tr><td>Defining longer-term MIS system architecture.</td><td></td><td>0.8219</td><td></td><td></td></tr><tr><td>Identifying longer-term structure and management style.</td><td></td><td>0.7717</td><td></td><td></td></tr><tr><td>Agreeing on the MIS group objectives.</td><td></td><td>0.7695</td><td></td><td></td></tr><tr><td>Identifying the potential areas for use of computers.</td><td></td><td>0.6656</td><td></td><td></td></tr><tr><td>Identifying longer-term MIS needs.</td><td></td><td>0.6357</td><td></td><td></td></tr><tr><td colspan="5">F3: Short-Range Operational Planning (SROP)</td></tr><tr><td>Defining criteria for evaluating and ranking potential projects.</td><td></td><td></td><td>0.7246</td><td></td></tr><tr><td>Ranking potential projects.</td><td></td><td></td><td>0.7074</td><td></td></tr><tr><td>Analysing applications in use by competition or by similar organisations.</td><td></td><td></td><td>0.7017</td><td></td></tr><tr><td>Documenting assumptions regarding future trends.</td><td></td><td></td><td>0.6168</td><td></td></tr><tr><td colspan="5">F4: Organisational IT Potential (OrgITPot)</td></tr><tr><td>Identifying potential projects among nonuser groups across the organisation.</td><td></td><td></td><td></td><td>0.8181</td></tr><tr><td>Identifying potential projects among nonuser groups in higher management.</td><td></td><td></td><td></td><td>0.8106</td></tr><tr><td>Identifying potential projects among current user groups.</td><td></td><td></td><td></td><td>0.7641</td></tr><tr><td>Eigenvalues</td><td>9.997</td><td>1.687</td><td>1.634</td><td>1.009</td></tr><tr><td>Percentage of variance</td><td>55.54</td><td>9.37</td><td>9.08</td><td>5.61</td></tr><tr><td>Cronbach's alpha</td><td>0.89</td><td>0.86</td><td>0.84</td><td>0.80</td></tr><tr><td colspan="5">C: Factor analysis results on IS Planning Success</td></tr><tr><td colspan="5">F1: Capabilities</td></tr><tr><td>Flexibility to adapt to unanticipated changes.</td><td>0.7862</td><td></td><td></td><td></td></tr><tr><td>Ability to gain cooperation among user groups for IS plans.</td><td>0.7625</td><td></td><td></td><td></td></tr><tr><td>Adapting the goals/objectives of IS to changing goals/objective of the organisation.</td><td>0.7050</td><td></td><td></td><td></td></tr><tr><td>Ability to anticipate surprise and crises.</td><td>0.6851</td><td></td><td></td><td></td></tr><tr><td>Improved understanding of how the organisation actually operates.</td><td>0.6794</td><td></td><td></td><td></td></tr><tr><td>Ability to understand the business and its information needs.</td><td>0.6361</td><td></td><td></td><td></td></tr><tr><td>Avoiding the overlapping development of major systems.</td><td>0.5888</td><td></td><td></td><td></td></tr><tr><td>Ability to identify key problems areas.</td><td>0.5840</td><td></td><td></td><td></td></tr><tr><td colspan="5">F2: Analysis</td></tr><tr><td>Understanding the dispersion of data, applications, and other technologies throughout the firm.</td><td></td><td>0.8540</td><td></td><td></td></tr><tr><td>Maintaining an understanding of changing organisational processes and procedures.</td><td></td><td>0.7740</td><td></td><td></td></tr><tr><td>Development of a "blueprint" which structures organisational processes.</td><td></td><td>0.7425</td><td></td><td></td></tr><tr><td>Generating new ideas to reengineer business processes through IT.</td><td></td><td>0.7151</td><td></td><td></td></tr><tr><td>Establish a uniform basis for prioritising projects.</td><td></td><td>0.5040</td><td></td><td></td></tr><tr><td colspan="5">F3: Cooperation</td></tr><tr><td>Maintaining open lines of communication with other departments.</td><td></td><td></td><td>0.7508</td><td></td></tr><tr><td>Coordinating the development efforts of various organisational subunits.</td><td></td><td></td><td>0.7475</td><td></td></tr><tr><td>Identifying and resolving potential sources of resistance to IS plans.</td><td></td><td></td><td>0.6759</td><td></td></tr><tr><td>Development clear guideline of managerial responsibility for plan implementation.</td><td></td><td></td><td>0.5537</td><td></td></tr><tr><td>Achieve a general level of agreement regarding the risks/trade-offs among system project.</td><td></td><td></td><td>0.5248</td><td></td></tr><tr><td colspan="5">F4: Alignment</td></tr><tr><td>Ability to identify new business opportunities.</td><td></td><td></td><td></td><td>0.8043</td></tr><tr><td>Ability to align IS strategy with organisational strategy.</td><td></td><td></td><td></td><td>0.7497</td></tr><tr><td>Identifying IT-related opportunities to support the strategic direction of the firm.</td><td></td><td></td><td></td><td>0.5974</td></tr><tr><td>Eigenvalues</td><td>9.330</td><td>1.888</td><td>1.366</td><td>1.146</td></tr><tr><td>Percentage of variance</td><td>44.43</td><td>8.99</td><td>6.50</td><td>5.46</td></tr><tr><td>Cronbach's alpha</td><td>0.89</td><td>0.86</td><td>0.84</td><td>0.80</td></tr></table>

The underlying reasons for the variations in the loadings for IS planning success are similar to that given for the IS function maturity factors. Although Segars and Grover (1998) study is more recent, it was still some time ago. Di<sup>f</sup>erent cultures among the respondents, di<sup>f</sup>erent levels of IT practices, and different IT objectives of local IT managers may also be relevant in explaining the di<sup>f</sup>erences. Therefore, although the IS planning success variables presented in the earlier study remain relevant, some di<sup>f</sup>erences have surfaced as a result of evolving IT practices. Notably, less variation is seen in this scale as compared to Karimi et al.’s (1996) IT maturity scale. This re<sup>fl</sup>ects the speed at which the technology environment (which the IS function maturity scale seeks to capture) has evolved over time. Furthermore, reliability was assessed using Cronbach’s alpha. As shown in Table 2(a–c), all three constructs have alpha values greater than 0.70 indicating acceptable internal consistency (Nunnally, 1978).

## 3.4. ACE algorithm

The ACE algorithm (Breiman & Friedman, 1985) was chosen over the standard regression technique of ordinary least squares (OLS). The ACE algorithm produces the best-<sup>fi</sup>tting additive model by estimating individual optimal smooth (linear and non-linear) transformations for both dependent and independent variables to maximise the correlation between the dependent variable and the variable of the <sup>fi</sup>tted values. Consequently, ACE transformations can be used to identify potential underlying non-linear relationships between the dependent and independent variables.

While variable transformations in other techniques are usually made to satisfy the model assumptions without explicitly improving model <sup>fi</sup>t, ACE transformations are unambiguously de<sup>fi</sup>ned and estimated without the use of heuristics, restrictive distributional assumptions, or restrictions of the transformation to a particular parametric family. As a result, ACE models often possess a superior <sup>fi</sup>t to those generated using standard regression techniques. As long as the number of samples is substantially greater than the number of independent variables, the sample size is not considerably important in ACE models. A detailed discussion of ACE regression, interpretation of its transformation plots, and generation of ACE models are contained in Sum, Yang, Ang, and Quek (1995) and Ang, Shimada, Quek, and Lim (2015). The overview of ACE algorithm is provided in the Appendix.

## 4. Results and discussions

## 4.1. Overall results

The optimal transformations of the dependent and independent variables are illustrated in Figure 2(1–4). These results show signi<sup>fi</sup>cant non-linear relationships between a dimension of IS function maturity and a dimension of IS planning success. Similarly, they indicate signi<sup>fi</sup>cant non-linear relationships between a dimension of IS planning process and a dimension of IS planning success.

The parameter p-values of the ACE transformations are presented in Table 3. Four dependent variables (ie, the four IS planning success factors of Capabilities, Analysis, Cooperation, and Alignment) were run separately against eight independent variables (the four IS function maturity factors of IT Planning Mode (ITPlan), IT Integration (ITInt), IT Industry Practice (ITIndPrac), and IT Perspective (ITPer), and the four IS planning process factors of Medium-Range Managerial Planning (MRMP), Long-Range Planning (LRP), Short-Range Operational Planning (SROP), and Organizational IT Potential (OrgITPot).

The determinants of Capabilities using ACE transformations were ITPlan and MRMP. Positive relationships held for both determinants. The positive determinants of Analysis were ITPlan, ITInt, LRP, and SROP. The negative determinants were MRMP and OrgITPot. The ACE transformations revealed six determinants for Cooperation. Positive relationships held for ITPlan, ITInt, MRMP, and LRP while negative relationships held for SROP and OrgITPot. For Alignment, the following determinants exhibited positive relationships: ITInt, ITIndPrac, MRMP, and LRP. However, the independent variable SROP exhibited a negative relationship with the dependent variable. All determinants mentioned above were signi<sup>fi</sup>cant at the 0.05 level of signi<sup>fi</sup>cance.

![](/api/attachments/3STD2XYZ/fulltext/images/828971ca14ec1d7e6b8e6da1ed116c87b5e0324b7a9de33ec059a6a6e7027afd.jpg)  
a: Capabilities (Dependent Variable)

![](/api/attachments/3STD2XYZ/fulltext/images/82f8e83c1d0894df16a9c951ef8c8dcaf3ad77d5ad9d2db41dcc1db01e04043b.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/58a3f3948fbeee0d865b695bbf98063f3a9ee8795d7825bade2df3b631f74a36.jpg)  
ACE graphical results. (1) ACE graphical results on capabilities. (2) ACE graphical results on analysis. (3) ACE graphica <sup>Figure 2.</sup>results on cooperation. (4) ACE graphical results on alignment.

The <sup>fi</sup>nal ACE models generated were compared with the OLS multiple regression models to demonstrate how much ACE improved the research models. For example, the ACE adjusted $R ^ { 2 }$ for the model on Cooperation excelled the linear model by about 24 per cent points. In all cases, the ACE transformations produced models with far better adjusted $R ^ { 2 }$ values than the corresponding linear models.

As shown in Figure 2(1a), 2(2a), 2(3a), and 2(4a), all the transformations of the four dependent variables are nondecreasing functions. This implies that the transformed values of the dependent variables are positively correlated to their corresponding observed dependent measures. Therefore, we can interpret the transformed value axis (y-axis) of the independent variable in the transformation plots (ie, Figures 2 (1b–c), 2(2b–g), 2(3b–g), and 2(4b–f)) as if it were the corresponding “dependent variable” axis (Sum et al., 1995). For example, Figure 2(1b) can be interpreted as showing the relationship between ITPlan on the x-axis (observed) and Capabilities on the y-axis (transformed). In contrast, Figure 2(1a) presents the overall e<sup>f</sup>ect of the statistically signi<sup>fi</sup>cant determinant variables on Capabilities. Simply put, Figures 2 (2a), 2(3a), and 2(4a) show the overall e<sup>f</sup>ect of the statistically signi<sup>fi</sup>cant determinant variables (Table 3) on each of the dependent variables, respectively. The remaining <sup>fi</sup>gures (ie, Figures 2(1b–c), 2 (2b–g), 2(3b–g), and 2(4b–f)) show the individual e<sup>f</sup>ects of each determinant variable on the corresponding dependent variable.

## 4.2. Interpretations of the main results

## 4.2.1. Patterns of the results

There are some patterns of non-linear curves in the ACE transformations. For example, we can categorise an upward-sloping curve into <sup>fi</sup>ve main patterns: (1) a gradual increase in the former part and a steep increase in the latter part; (2) a steep increase in the former part and a gradual increase in the latter part; (3) an increase in the former part and a <sup>fl</sup>at in the latter part; (4) a <sup>fl</sup>at in the former part and an increase in the latter part; (5) an increase in the former part, a <sup>fl</sup>at in the middle part, and an increase in the latter part. In this study, we obtained all the patterns except the pattern of a steep increase in the former part and a gradual increase in the latter part. Since our focus in this study is the research method rather than the research model or its results, we select four non-linear relationships as examples of each pattern above, and discuss their interpretations.

![](/api/attachments/3STD2XYZ/fulltext/images/dbfba332cd06e3dd7908459ace1c3fb74fcd3eb73aa85013de8ad7280b668a38.jpg)  
a: Analysis (Dependent Variable)

![](/api/attachments/3STD2XYZ/fulltext/images/7bc08be1ee8319ffad0fdbff0e30d55a08266c60b15471c125b36e34f9cc3898.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/b3cabae72bddc0fd732adc116c04c3765b9df9ea9287582228ac77f3aabf7615.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/8d36feb2ec8ebb89b71079fdc54bb19da7a6af302a35d1b1005bc566c5f73459.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/63986a4f343afe69249ccb183f695b8b52ad46a19cf4c9e0870cc8a1b01e13d5.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/93f73a4364a1e9104af391b5b5d801389722dea3346dc225922512efbd85cf88.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/2181a1fba2b38f0c536b293565142ca8e70c86050aafc92d590928be7fce4d2e.jpg)  
(Continued).

## 4.2.2. The e<sup>f</sup>ects of IT planning mode on capabilities

Figure 2(1b) shows a relationship between ITPlan and Capabilities. This is an example of the pattern of a gradual increase in the former part and a steep increase in the latter part. When the IT function is young, its structure is not clearly de<sup>fi</sup>ned. Thus, the ITPlan is limited. When ITPlan is low, the

![](/api/attachments/3STD2XYZ/fulltext/images/cc50656eee8af69ad19c9ae8a24324ab51037dba1f7016d550df3e095858f0da.jpg)  
a: Cooperation (Dependent Variable)

![](/api/attachments/3STD2XYZ/fulltext/images/f4646ffc2521afb1d7531fd6d7cf4ddb5cec0e942457562027947ef658ad10ee.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/d526a5fcee4fcba6fd2d6cedb9016f2c53b690addff0d18600344b1f09a4bab7.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/3d7cc0c49841ea76d7268f6967164250c9d371593e1befde383df4d57849875e.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/3011bb5486347151f6ad726e1fdeac602cbef388e459ae007a83bbdeb1c180c0.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/a8f45d3a855e880dc2b88a43d1e11e98baf00369132dc24ec95e9b0562742cea.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/8e14c9b845f952c947f0b3a6a31221d7b4bb5bfc76133406280ba008b7dc31c7.jpg)  
(Continued).

organisation is less able to respond to unanticipated changes in the organisation. The IT function’s understanding of the business is not strong, and is unable to clearly de<sup>fi</sup>ne goals and objectives to support the business (Lederer & Mendelow, 1987). Cooperation between the IT function and other business functions is low as the IT function is unable to gain support and cooperation to implement its proposals.

![](/api/attachments/3STD2XYZ/fulltext/images/9dbb0542fad6973a2ee000b7c94ae47398231eb8126f1427b5ac1b5b6d14342d.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/8b4e241189c36e98889a584d35588be09c54baf86ec579e606fd37e4898e9a38.jpg)  
b: ITInt

a: Alignment (Dependent Variable)  
![](/api/attachments/3STD2XYZ/fulltext/images/1849593cedb1c872350750405915a14282b18691e62c5ae81bdef352e9c3f0c5.jpg)  
c: ITIndPrac

![](/api/attachments/3STD2XYZ/fulltext/images/b09f5f1cd03e6f11ca01b56953977c87f47358fbc0b8fd7165b2c64b9bb7180a.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/56bb45e279994ef913e854e342ef7113b3c25e5e552118ebd71af96c31225025.jpg)

![](/api/attachments/3STD2XYZ/fulltext/images/67ff65d744956695f0d24ec2bc6ee8cf01a7e482eca3a5b8603d1201a484fe46.jpg)  
f: SROP

(Continued).  
Parameter p-Values from ACE analysis.

<table><tr><td rowspan="2">Independent variables</td><td colspan="4">Dependent variables</td></tr><tr><td>Capabilities</td><td>Analysis</td><td>Cooperation</td><td>Alignment</td></tr><tr><td>ITPlan</td><td>0.0000 (+)</td><td>0.0028 (+)</td><td>0.0001 (+)</td><td></td></tr><tr><td>ITInt</td><td></td><td>0.0051 (+)</td><td>0.0003 (+)</td><td>0.0003 (+)</td></tr><tr><td>ITIndPrac</td><td></td><td></td><td></td><td>0.0072 (+)</td></tr><tr><td>ITPer</td><td></td><td></td><td></td><td></td></tr><tr><td>MRMP</td><td>0.0004 (+)</td><td>0.0101 (-)</td><td>0.0172 (+)</td><td>0.0192 (+)</td></tr><tr><td>LRP</td><td></td><td>0.0001 (+)</td><td>0.0000 (+)</td><td>0.0000 (+)</td></tr><tr><td>SROP</td><td></td><td>0.0000 (+)</td><td>0.0077 (-)</td><td>0.0002 (-)</td></tr><tr><td>OrgITPot</td><td></td><td>0.0002 (-)</td><td>0.0034 (-)</td><td></td></tr><tr><td colspan="5">Model adjusted  $R^{2}$ </td></tr><tr><td>ACE</td><td>0.7247</td><td>0.6225</td><td>0.5991</td><td>0.7437</td></tr><tr><td>OLS</td><td>0.5541</td><td>0.4449</td><td>0.3580</td><td>0.5827</td></tr></table>

Note: p-values are indicated only when they are signi<sup>fi</sup>cant (p ≤ 0.05). (+) means a positive relationship between the independent variable and the dependent variable, and (−) means a negative relationship between them.

As the IT function becomes more established, ITPlan increases. This leads to Capabilities increasing at a faster pace. Understanding the strategic importance of the IT function enables proper goals and objectives to be determined and responsibilities of department members to be clearly de<sup>fi</sup>ned. The IT function is able to anticipate problem areas and react to unexpected changes with greater conviction and con<sup>fi</sup>dence. The IT function progressively becomes part of the strategic arsenal that the organisation can harness upon to compete e<sup>f</sup>ectively in the dynamic business environment.

## 4.2.3. The e<sup>f</sup>ects of IT integration on analysis

The plot in Figure 2(2b) reveals a positive relationship between ITInt and Analysis. However, at mid-- levels, a plateau is recorded before the positive relationship resumes. This is an example of the pattern of an increase in the former part, a <sup>fl</sup>at in the middle part, and an increase in the latter part. When IT integration is low, most of the IT development is undertaken at a business unit level without much regard for integrating systems with the rest of the organisation. The di<sup>f</sup>erent functional areas in the organisation are automated on an application-byapplication basis (Karimi et al., 1996).

Analysis refers to the ability of the IT function to understand IT dispersion throughout the organisation. This factor also encompasses the IT function’s capacity to determine current and future IT requirements of the organisation. Understanding organisational-wide processes and procedures is important as it allows the IT function to better plan and implement new technologies. As the IT function matures, IT integration increases and this brings about a corresponding improvement in Analysis.

Improvements in Analysis continue as the <sup>fi</sup>rm grows and the IT function matures. At a certain critical point these improvements stagnate. This situation typically arises when many of the application systems installed in the company start to become incompatible with newer systems and redundancies begin to cause complications. During that period, the IT function seeks to implement integrated companywide applications systems such as enterprise resource planning systems to improve e<sup>fi</sup>ciencies in the company. The implementation of such systems often requires companies to undergo business process reengineering, and change management is often a complementary exercise that occurs concurrently. It is only after the company successfully emerges from this period of radical change that improvements in Analysis continue. The plot re<sup>fl</sup>ects the resumption of the positive relationship between the two factors.

## 4.2.4. The e<sup>f</sup>ects of IT planning mode on cooperation

Figure 2(3d) shows a positive relationship between ITPlan and Cooperation (or organisational collaboration). This is an example of the pattern of an increase in the former part and a <sup>fl</sup>at in the latter part. The need for the organisation to band together to contribute to the development of a company’s IT systems is highest when the company is de<sup>fi</sup>ning its strategic position, and when the IT function is trying to uncover potential IT projects of strategic value (McLean & Soden, 1977).

The positive relationship hits a plateau. This is a common phenomenon which occurs as other factors counteract the positive e<sup>f</sup>ects of increasing IT organisational e<sup>f</sup>ectiveness. As organisational size increases, organisational structure becomes increasingly complex, thus inhibiting an increase in the quality of organisational collaboration (ie, Cooperation) (Sum et al., 1995; Teo & King, 1997). At this point, organisations may engage consultants (Thong, Yap, & Raman, 1996) to identify further areas where improvements in organisational collaboration can be achieved. These incremental improvements register in the graph as the small upward trend that is registered before the next plateau is soon reached.

## 4.2.5. The e<sup>f</sup>ects of IT industry practice on alignment

The plot in Figure 2(4c) portrays the relationship between ITIndPrac and Alignment. This is an example of the pattern of a <sup>fl</sup>at in the former part and an increase in the latter part. Initially, organisations are more focused on developing IT systems to support the operational needs of their di<sup>f</sup>erent functions. These are often transaction systems. Thus, even as organisations become more aware of the current and potential use of IT by their competitors, this knowledge does not in<sup>fl</sup>uence their IT decision-making process. As long as the IT function is viewed solely as an operational tool, Alignment remains low.

When management recognises the strategic importance of IT, it becomes crucial and critical to factor in the IT industry practices of competitors. The organisation begins to evaluate the strategic direction of its competitors and incorporates that knowledge into determining how to establish a sustainable competitive advantage (Kettinger, Grover, Guha, & Segars, 1994). Consequently, Alignment increases as awareness of IT industry practice increases since this knowledge is exploited in the strategic formulation of future IT and organisational plans.

## 5. Conclusions

## 5.1. Concluding remarks

This exploratory study demonstrates that there is often a complex relationship between IS planning success and its determinants as indicated by various non-linear relationships. The various plots enable us to better visualise how various success measures can evolve with low or high values of determinant variables, thereby providing further avenues for future research to better understand the complex nature of the relationships between IS planning success and its determinants. We understand that the study is exploratory and data-driven, but we provide our best interpretations of the main results in the previous section.

The study shows that the relationships between the dimensions of IS function maturity and those of IS planning success are positive, though they are not linear. Among the four dimensions of IS function maturity, IT planning mode and IT integration have great e<sup>f</sup>ects on IS planning success. However, the IT perspective dimension does not a<sup>f</sup>ect IS planning success at all. These relationships imply that the organisations should concentrate their e<sup>f</sup>orts on improving the levels of IT planning mode and IT integration to increase their chances of achieving IS planning success. For example, The IT function should be clear about its goals and responsibilities, and the introduction of new technologies should take place at the business unit level under business unit control.

On the other hand, the relationships between the dimensions of IS planning process and those of IS planning success are either positive, negative, or mixed with nonlinearity. Among the four dimensions of IT planning process, the long-range planning dimension has positive e<sup>f</sup>ects on IS planning success, while the organisational IT potential dimension has negative e<sup>f</sup>ects. The other two dimensions of IT planning process (ie, medium-range managerial planning and short-range operational planning) have both positive and negative e<sup>f</sup>ects on IT planning success, depending on its dimension. The positive and negative relationships between the independent IS planning process variables and the dependent IS planning success variables demonstrate that IS planning is an intricate process, that is, a process which IT functions must approach with an understanding of all the relevant issues. Understanding all the issues is a preliminary step. The di<sup>fi</sup>cult part is establishing the <sup>fi</sup>ne balance between the di<sup>f</sup>erent aspects even as the IT function matures and organisation-wide business plans evolve.

## 5.2. Managerial implications

From this exploratory study, we can provide two main managerial implications. First, the <sup>fi</sup>rst two levels of CMM (ie, the initial level and the repeatable level) among the <sup>fi</sup>ve levels is a key to IS planning success. Although we adopt Karimi et al.’s model (Karimi et al., 1996) for the constructs of IS function maturity, we can use CMM to discuss the interpretation of the ACE graphical results in the IS function maturity. The upward trend of the curves of IT integration and IT planning mode (ie, two dimensions of IS function maturity) in analysis and cooperation (ie, two dimensions of IS planning success) are steep initially and reach a plateau in the middle, as shown in Figure 2(2,3). This implies that IT planning success increases as the IS function maturity increases in the initial and repeatable levels of CMM. However, the increase in the IS function maturity does not have much in<sup>fl</sup>uence on the increase in IT planning success in the de<sup>fi</sup>ned level of CMM.

Before the process is de<sup>fi</sup>ned or con<sup>fi</sup>rmed as a standard business process, IS function maturity is low and unstable. Therefore, a company has to make IT function clear and link IS strategy to business needs to succeed in IS planning. However, once the process is standardised, IS function maturity is not very important to IS planning success. A company need to invest in IT and human resources su<sup>fi</sup>ciently to reach the threshold level of IS success.

Second, the traditional IS planning process needs to change to achieve success. Surprisingly, medium-range managerial planning and organisational IT potential (ie, two dimensions of IS planning process) have negative e<sup>f</sup>ects on analysis (ie, a dimension of IS planning success). Similarly, short-range operational planning and organisational IT potential (ie, two dimensions of IS planning process) have negative e<sup>f</sup>ects on cooperation (ie, a dimension of IS planning success). In addition, the downward trend of the curves of these variables are steep initially and reach a plateau in the middle, as shown in Figure 2(2,3). However, longrange planning (ie, a dimension of IS planning process) has positive e<sup>f</sup>ects on both analysis and cooperation.

These results imply that the traditional IS planning process does not sometimes reach to IS planning success and may have negative in<sup>fl</sup>uence on the success. Speci<sup>fi</sup>cally, this may happen when IS planning process is at the low level. Due to this problem agile software development methodologies emerged and has been evolving even now. Therefore, we conclude that today’s dynamic business environment forced companies to change IS development process.

## Disclosure statement

No potential con<sup>fl</sup>ict of interest was reported by the authors.

## ORCID

Tomoaki Shimada http://orcid.org/0000-0001-7114- 0586

## References

Ang, J. S. K., Shimada, T., Quek, S. A., & Lim, E. (2015). Manufacturing strategy and competitive performance: An ACE analysis. International Journal of Production Economics, 169, 240–252.

Bass, L. (2018). The software architect and DevOps. IEEE Software, 53(1), 8–10.

Basu, V., Hartono, E., Lederer, A. L., & Vijay, S. (2002). The impact of organizational commitment, senior management involvement, and team involvement on strategic information systems planning. Information and Management, 39(6), 513–524.

Bechor, T., Neumann, S., Zviran, M., & Glezer, C. (2010). A contingency model for estimating success of strategic information systems planning. Information and Management, 47(1), 17–29.

Benbasat, I., Dexter, A. S., Drury, D. H., & Goldstein, R. C. (1984). A critique of the stage hypothesis: Theory and empirical evidence. Communications of the ACM, 27(5), 476–485.

Benbasat, I., Dexter, A. S., & Mantha, R. W. (1980). Impact of organizational maturity on information system skill needs. MIS Quarterly, 4(1), 21–34.

Blumenthal, S. C. (1969). Management information systems: A framework for planning and development. Englewood Cli<sup>f</sup>s: Prentice-Hall.

Breiman, L., & Friedman, J. H. (1985). Estimating optimal transformations for multiple regression and correlation [with discussion]. Journal of American Statistical Association, 80, 580–619.

Cameron, K. S., & Whetten, D. A. (1983). Some conclusions about organizational e<sup>f</sup>ectiveness. In K. S. Cameron & D. A. Whetten (Eds.), Organizational efectiveness: A comparison of multiple methods (pp. 261– 277). New York: Academic Press.

Churchill, N. C., Kempster, J. H., & Uretsky, M. (1969). Computer based information systems for management: A survey. New York: National Association of Accountants.

Conrath, D. W., Ang, J. S. K., & Mattay, S. (1992). Strategic planning for information systems: A survey of Canadian organizations. INFOR, 30(4), 364–378.

DeLone, W. H., & McLean, E. R. (1992). Information systems success: The quest for the dependent variable. Information Systems Research, 3(1), 60–95.

DeLone, W. H., & McLean, E. R. (2003). The DeLone and McLean model of information systems success: A tenyear update. Journal of Management Information Systems, 19(4), 9–30.

DeLone, W. H., & McLean, E. R. (2016). Information systems success measurement. Foundations and Trends in Information Systems, 2(1), 1–116.

Dingsoyr, T., & Lassenius, C. (2016). Emerging themes in agile software development: Introduction to the special section on continuous value delivery. Information and Software Technology, 77, 56–60.

Dingsoyr, T., Nerur, S., Balijepally, V., & Moe, N. B. (2012). A decade of agile methodologies: Towards explaining agile software development. Journal of Systems and Software, 85(6), 1213–1221.

Earl, M. J. (1989). Management strategies for information technology. London: Prentice-Hall.

Earl, M. J. (1993). Experiences in strategic information systems planning. MIS Quarterly, 17(1), 1–24.

Ein-Dor, P., & Segev, E. (1978). Strategic planning for MIS. Management Science, 24(15), 1631–1641.

Farhoomand, F., & Gatehouse, M. (1988). Factors in<sup>fl</sup>uencing the growth of the MIS department: A survey. Journal of Information Systems Management, 5(2), 56– 60.

Goodhue, D. L., Kirsch, L. J., Quillard, J. A., & Wybo, M. D. (1992). Strategic data planning: Lessons from the <sup>fi</sup>eld. MIS Quarterly, 16(1), 11–34.

Grover, V., & Segars, A. H. (2005). An empirical evaluation of stages of strategic information systems planning: Patterns of process design and e<sup>f</sup>ectiveness. Information and Management, 42(5), 761–779.

Henderson, J. C., & Venkatraman, N. (1993). Strategic alignment: Leveraging information technology for tomorrow. IBM Systems Journal, 32(1), 4–16.

Humphrey, W. S. (1989). Managing the software process. Reading, MA: Addison-Wesley.

Karimi, J., Gupta, Y., & Somers, T. (1996). Impact of competitive strategy and information technology maturity on <sup>fi</sup>rm’s strategic response to globalization. Journal of Management Information Systems, 12(4), 55–88.

Kettinger, W. J., Grover, V., Guha, S., & Segars, A. H. (1994). Strategic information systems revisited: A study in sustainability and performance. MIS Quarterly, 18(1), 31–58.

King, W. R. (1978). Strategic planning for management information systems. MIS Quarterly, 2(1), 27–37.

King, W. R. (1988). Evaluating an information systems planning process. Long Range Planning, 21(5), 103–112.

King, W. R., & Teo, T. S. H. (1997). Integration between business planning and information systems planning; validating a stage hypothesis. Decision Sciences, 28(2), 279–308.

Lederer, A. L., & Mendelow, A. L. (1987). Information resource planning: Overcoming di<sup>fi</sup>culties in identifying top management’s objectives. MIS Quarterly, 11(3), 389–399.

Lederer, A. L., & Sethi, V. (1988). The implementation of strategic information systems planning methodologies. MIS Quarterly, 12(3), 445–461.

Li, E., & Chen, H. G. (2001). Output-driven information system planning: A case study. Information and Management, 38(3), 185–199.

Mangalaraj, G. (2014), “Strategic information systems planning: A literature review”. Proceedings of the Ninth Midwest Association for Information Systems Conference, Ames, IA, 17.

McFarlan, F. W. (1971). Problems in planning the information system. Harvard Business Review, 49(2), 75–89.

McFarlan, F. W. (1984). Information technology changes the way you compete. Harvard Business Review, 62(3), 98–103.

McLean, E. R., & Soden, J. V. (1977). Strategic planning for MIS. New York: John Wiley.

Mirchandani, D. A., & Lederer, A. L. (2012). “Less is more:” Information systems planning in an uncertain environment. Information Systems Management, 29(1), 13–25.

Nerur, S., Mahapatra, R., & Mangalaraj, G. (2005). Challenges of migrating to agile methodologies. Communications of the ACM, 48(5), 73–78.

Newkirk, H. E., & Lederer, A. L. (2006a). Incremental and comprehensive strategic information systems planning in an uncertain environment. IEEE Transactions on Engineering Management, 53(3), 380–394.

Newkirk, H. E., & Lederer, A. L. (2006b). The e<sup>f</sup>ectiveness of strategic information systems planning under environmental uncertainty. Information and Management, 43 (4), 481–501.

Newkirk, H. E., Lederer, A. L., & Cidambi, S. (2003). Strategic information systems planning: Too little or too much? Journal of Strategic Information Systems, 12 (3), 201–228.

Newkirk, H. E., Lederer, A. L., & Johnson, A. M. (2008). Rapid business and IT change: Drivers for strategic information systems planning? European Journal of Information Systems, 17(3), 198–218.

Nolan, R. L. (1973). Managing the computer resource: A stage hypothesis. Communications of the ACM, 16(7), 399–405.

Nolan, R. L. (1979). Managing the crises in data processing. Harvard Business Review, 57(2), 115–126.

Nunnally, J. (1978). Psychometric theory ((2nd ed.). New York: McGraw-Hill.

Petter, S., DeLone, W. H., & McLean, E. R. (2008). Measuring information systems success: Models, dimensions, measures, and interrelationships. European Journal of Information Systems, 17(3), 236–263.

Poeppelbuss, J., Niehaves, B., Simons, A., & Becker, J. (2011). Maturity models in information systems research: Literature search and analysis. Communications of the Association for Information Systems, 29(1), 505–532.

Premkumar, G., & King, W. R. (1994). Organizational characteristics and information systems planning: An empirical study. Information Systems Research, 5(2), 75–109.

Raghunathan, B., & Raghunathan, T. S. (1994). Adaptation of a planning system success model to information sys tems planning. Information Systems Research, 5(3), 326– 340.

Sabherwal, R. (1999). The relationship between information system planning sophistication and information system success: An empirical assessment. Decision Sciences, 30(1), 137–167.

Sabherwal, R., & King, W. R. (1992). Decision processes for developing strategic applications of information systems: A contingency approach. Decision Sciences, 23(4), 917–943.

Segars, A. H., & Grover, V. (1998). Strategic information systems planning success: An investigation of the construct and its measurement. MIS Quarterly, 22(2), 139–163.

Segars, A. H., & Grover, V. (1999). Pro<sup>fi</sup>les of strategic information systems planning. Information Systems Research, 10(3), 199–232.

Segars, A. H., Grover, V., & Teng, J. T. C. (1998). Strategic information systems planning: Planning system dimensions, internal coalignment, and implications for planning e<sup>f</sup>ectiveness. Decision Sciences, 29(2), 303–345.

Sum, C. C., Yang, K. K., Ang, J. S. K., & Quek, S. A. (1995). An analysis of materials requirements planning (MRP) bene<sup>fi</sup>ts using Alternating Conditional Expectations (ACE). Journal of Operations Management, 13(1), 35–38.

Teo, T. S. H., & Ang, J. S. K. (2001). An examination of major IS planning problems. International Journal of Information Management, 21(6), 457–470.

Teo, T. S. H., & King, W. R. (1997). Integration between business planning and information systems planning: An evolutionary-contingency perspective. Journal of Management Information Systems, 14(1), 185–214.

Thong, J. Y. L., Yap, C. S., & Raman, K. S. (1996). Top management support, external expertise and information systems implementation in small businesses. Information Systems Research, 7(2), 248–267.

Venkatraman, N., & Ramanujam, V. (1987). Planning system success: A conceptualization and operational model. Management Science, 33(6), 687–705.

Wang, E. T. G., & Tai, J. C. F. (2003). Factors a<sup>f</sup>ecting information systems planning e<sup>f</sup>ectiveness: Organizational contexts and planning systems dimensions. Information and Management, 40(4), 287–303.

Ward, J., Gri<sup>fi</sup>ths, P., & Whitmore, P. (1990). Strategic planning for information systems. New York: Wiley.

Wilkin, C. L., & Cerpa, N. (2012). Strategic information systems planning: An empirical evaluation of its dimensions. Journal of Technology Management and Innovation, 7(2), 52–61.

Zhu, L., Bass, L., & Champlin-Schar<sup>f</sup>, G. (2016). DevOps and its practices. IEEE Software, 33(3), 32–34.

## Appendix: Overview of ACE Algorithm

The ACE algorithm chooses the functions θ and $f _ { 1 } , . . . , f _ { j }$ to maximise the correlation between the predictor $\textstyle \sum _ { j = 1 } ^ { p } f _ { j } ( X _ { j } )$ 十 ε and θ  Y in the following equation.

$$
\theta (Y) = \alpha + \sum_ {j = 1} ^ {p} f _ {j} \left(X _ {j}\right) + \varepsilon .
$$

In order to select the preferred ACE model, an algorithm was implemented in the Dbank software using forwardstepwise inclusion, alternating with backward-stepwise deletion, for a total of, say, m eligible independent variables. While this process is not quite as exhaustive as the prohibitive all-subset procedure (which would require 2<sup>m-1</sup> ACE runs), it was designed to be no worse than both the purely forward-stepwise and the purely backward-stepwise procedures.

The ACE algorithm starts with <sup>fi</sup>nding the best model with only one predictor, and keeps track of the best-found – thus, benchmark – model for a given number (from 1 to m) of predictors. The algorithm is continuously trying to step forward or backward from the current benchmark model for some number (say, $i , 1 \le - i \le m )$ of predictors to a new benchmark model for one more (i + 1) or one less $( i \mathrm { ~ - ~ } 1 )$ predictor.

For instance, suppose the algorithm has so far not evaluated any model with more than k predictors, and the current model is the best one found (sometime back) with k predictors. For a forward step, the additional variable that would yield the smallest resultant (mode F-test) p-value (or greatest resultant adjusted R-squared) is selected to expand the model to $\dot { k } ~ + ~ 1$ predictors. (Note that, to allow meaningful comparison of models, each p-value or adjusted R-squared should be computed in the original (ie, pre-transformed) Y-space by <sup>fi</sup>rst reversing the transformation of Y given by ACE).

Upon <sup>fi</sup>nding a new benchmark, the algorithm tries to search 1-step back for a new benchmark for one less predictor, failing which it tries to search one or more steps forward for a new benchmark for one or more predictors. Speci<sup>fi</sup>cally, the algorithm proceeds according to the following three rules:

(1) Whenever a new best model (of k + 1 predictors in this instance) is found, the algorithm attempts a backward step by deleting the variable that yield the smallest resultant p-value (or greatest resultant adjusted Rsquared) among sub-models with one less predictor – in this case, with k of the original k + 1 predictors. If this new k-predictor model is better than the previous benchmark k-predictor model, the backward step is successfully taken from the best (k + 1)-predictor model to this new best k-predictor model, and then (since a new best model is just found) another backward step is attempted to <sup>fi</sup>nd a new benchmark (k – 1)-predictor model.

(2) Whenever a backward step fails, the algorithm attempts instead a forward step. In this instance, if the backward step fails from the benchmark k-predictor model to a new benchmark (k – 1)-predictor model, the algorithm tries to step forward from the current benchmark k-predictor model to <sup>fi</sup>nd a new benchmark (k + 1)-predictor model.

(3) Whenever a forward step fails, the algorithm attempts a new forward step from the benchmark model with one more predictor than the current benchmark model. In this instance, if the forward step from the current benchmark k-predictor model fails (all resultant models from adding one variable are inferior to the existing benchmark model with k + 1 predictors), the algorithm attempts instead a forward step from the benchmark (k + 1)-predictor model to a new benchmark (k + 2)-predictor model (ie, if it cannot jump 1-step forward, it tries to jump 2-step forward, and so on).

The algorithm stops when it cannot <sup>fi</sup>nd, either in forward or backward stepping, a new benchmark (m – 1)- predictor model, because then the algorithm, while observing either rule 3 or 2, has no (m + 1)-predictor model to step forward into (since there are only m independent variables). A parsimonious model is then selected from among the benchmark models for the di<sup>f</sup>erent numbers of predictors.

When all models under consideration have the same number of observations, experience has shown that using p-value tends to yield parsimonious models when compared to using adjusted R-squared. Whereas when the m predictors do not have the same range of observations – so that the e<sup>f</sup>ective number of observations in a mode depends on the particular collection of predictors – using adjusted R-squared tends to yield more interpretable results.
