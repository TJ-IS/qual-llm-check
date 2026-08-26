---
otero_id: 8930
otero_key: "ZD4KEXJQ"
title: "Fuzzy decision support system for risk analysis in e-commerce development"
authors: "E.W.T. Ngai; F.K.T. Wat"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.12.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Fuzzy decision support system for risk analysis in e-commerce development

E.W.T. Ngai\*, F.K.T. Wat

Department of Management and Marketing, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong, People’s Republic of China

Received 1 December 2001; accepted 1 December 2003 Available online 14 March 2004

## Abstract

This paper describes the development of a fuzzy decision support system (FDSS) for the assessment of risk in e-commerce (EC) development. A Web-based prototype FDSS is designed and developed to assist EC project managers in identifying potential EC risk factors and the corresponding project risks. A risk analysis model for EC development using a fuzzy set approach is proposed and incorporated into the FDSS. The results of an evaluation indicate that the prototype performs to expectations.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Electronic commerce; Fuzzy decision support system; Fuzzy set; Risk analysis

## 1. Introduction

E-commerce (EC) is ‘‘a modern business methodology that addresses the needs of organizations, merchants, and consumers to cut costs while improving the quality of goods and services and increasing the speed of service delivery. The term also applies to the use of computer networks to search and retrieve information in support of human and corporate decision making’’ [21]. It has been adopted widely in most enterprises.

Although EC offers various business opportunities, EC development is plagued by various kinds of risk and risk management is necessary to avoid these problems. Indeed, a task that is critical to the proper management of EC development is the assessment of risk. An important step in advancing our knowledge requires that we understand and address these risks. According to Leung et al. [26], most project managers worry about the time involved in risk management when it comes to identifying and assessing risks. However, with the aid of computers and the use of software systems, the time for risk analysis can be significantly reduced. Risk analysis can be conducted by using the theory of probability, which estimates the likelihood and consequences of any given risk. EC development is relatively new to most companies, and only limited information is available on the associated risks. The application of fuzzy set theory (FST) to risk analysis seems appropriate, as such analysis is highly subjective and related to inexact and vague information. There is a need to design and develop a fuzzy decision support system (FDSS) to assist EC practitioners to evaluate the risks associated with EC development.

This paper describes the research and development of a FDSS that can be used to effectively support EC project managers in conducting risk assessment in EC development. The motivation for the present work is the recognized absence and need for such system that help in the evaluation of a company’s risk level and provides an overall risk evaluation of EC development.

## 2. Literature review

## 2.1. Definitions of risks associated with EC development

The concept of ‘‘risk’’ became popular in economics during the 1920s. Since then, it has been successfully used in theories of decision making in economics, finance, and the decision science. The Merriam-Webster [48] dictionary defines risk as the ‘‘possibility of loss or injury’’ or ‘‘someone or something that creates or suggests a hazard’’. At present, there is no agreed upon universal definition of EC risk but information security is a widely recognized aspect of EC risk [44]. Greenstein [17] views risks associated with EC as the possibility of loss of confidential data or the destruction, generation, or use of data or programs that physically, mentally or financially harms another party, as well as the possibility of causing harm to hardware. Mceachern [29] uses the term ‘‘cyber risk’’ to define any risk associated with EC, including, for example, Web site destruction and manipulation, unauthorized access to customer records, Internet fraud, telecommunications theft, copyright infringement and denial of access. On the other hand, Viehlandm [44] focuses on managing business risk in EC. He defines EC risk as the likelihood of a negative impact to organization itself when developing or operating EC strategy. In this paper, risks associated with EC development are the risks of direct or indirect loss to the organization in development an EC project, which refers to any project that involves development stages as planning, analysis, design and implementation of an EC system.

## 2.2. The significance of fuzzy risk analysis for EC development

Through using EC, companies are able to connect with their trading partners for ‘‘just in time production’’ and ‘‘just in time delivery’’, which improves their competitiveness globally. Although EC offers great opportunities, there is no doubt that EC development involves many risks. In this study, we do not intend to present risks to EC only but also risks that EC development shares with traditional systems. Every EC development is linked to a different degree of risk. However, most companies do not identify and assess EC-related risk. EC development has a lot in common with IT project development. Many IT and EC development cannot be completed on-time and on-budget [39]. Proper risk management is an essential element of project success [39] because without appropriate risk management it fails to achieve significant return on investment or defensive/competitive purpose. One of the important phases in risk management is risk analysis, which involves a process of risk identification and risk assessment. Proper risk assessment can enhance the chance of successful project implementation [1]. McDonald [28] and Stoehr [39] point out that companies need to perform a risk analysis before engaging EC development.

## 2.3. Fuzzy risk analysis research

The techniques of risk analysis are powerful tools to help people manage uncertainty. Thorough risk analysis estimation and evaluation can provide valuable support for decision making. There are many risk analysis techniques currently in use that attempt to evaluate and estimate risk. These techniques can be either qualitative or quantitative depending on the information available and the level of detail that is required [4]. Quantitative techniques rely heavily on statistical approaches, which include Monte Carlo Simulation [49], Fault and Event Tree Analysis [4,49], Sensitivity Analysis [49], Annual Loss Expectancy [35], Risk Exposure [5], Failure Mode and Effects Analysis [49], etc. On the other hand, qualitative techniques rely more on judgment than on statistical calculations such as Scenario Analysis [35], FST [35], etc. Quantitative and qualitative techniques have their own advantages and disadvantages. Among these techniques, the application of FST to risk analysis seems appropriate, as such analysis is highly subjective and related to inexact and vague information.

Since FST was introduced by Zadeh [51] to deal with problems in which vagueness was present, linguistic values have been widely used to approximate reasoning. Numerous studies of FST in risk assessment have appeared in different areas, and are summarized in Table 1. FST has been effective in such a variety of areas because it can handle inexact yet useful information.

Table 1  
Fuzzy risk analysis applications

<table><tr><td>Research area</td><td>Description</td><td>References</td></tr><tr><td colspan="3">Information technology</td></tr><tr><td>Database gateway processor</td><td>Applies basic concepts of fuzzy logic modeling to risk analysis in database gateway systems.</td><td>[30]</td></tr><tr><td>Information security</td><td>Presents a methodology for the modeling of the risk analysis process within a computing facility.</td><td>[10]</td></tr><tr><td>Software development</td><td>Applies FST to evaluate the rate of aggregative risk in software development.</td><td>[23]</td></tr><tr><td colspan="3">Environmental</td></tr><tr><td>Natural hazards</td><td>Employs fuzzy methods to calculate the risk of release, exposure to, and consequence of natural urban hazards.</td><td>[19]</td></tr><tr><td>Ground water nitrate risk management</td><td>Presents a nitrate risk-management methodology using fuzzy sets in combination with a multi-criterion decision-making (MCDM) technique to assist decision makers in evaluating, with uncertain information, possible regulatory actions along with the various nitrate risk-management strategies to determine an appropriate strategy.</td><td>[25]</td></tr><tr><td>Hazardous materials</td><td>Provides an application of fuzzy logic to the risk assessment of the transport of hazardous materials by road and pipeline to evaluate the uncertainties that affect both individual and societal risk estimates.</td><td>[7]</td></tr><tr><td colspan="3">Engineering</td></tr><tr><td>System failure</td><td>Presents a fuzzy logic-based technique for prioritizing failures for corrective actions in a Failure Mode, Effects and Criticality Analysis. The method allows the analyst to evaluate the risks associated with item failure modes directly by using the linguistic terms employed in the criticality assessment. Ambiguous, qualitative, or imprecise information, as well as quantitative data, can be used in the assessment.</td><td>[8]</td></tr><tr><td>Construction</td><td>Outlines an approach to the assessment of construction project risk by linguistic analysis using FST.</td><td>[40,50]</td></tr><tr><td>Civil</td><td>Involves fuzzy set representations of structural damage and related safety analyzes in civil engineering.</td><td>[32,36,41]</td></tr><tr><td colspan="3">Others</td></tr><tr><td>Bank</td><td>Develops a fuzzy set approach in planning system for liquidity management in bank industry.</td><td>[15]</td></tr><tr><td>Tourism</td><td>Applies a fuzzy multiple criteria decision-making method to conduct an evaluation of tourist risks.</td><td>[42]</td></tr></table>

## 2.4. Fuzzy weighted average

An operation commonly used in risk and decision analysis is the weighted average operation [20], which takes the following form:

$$
\overline {{W}} = \frac {\sum_ {i = 1} ^ {n} W _ {i} \times R _ {i}}{\sum_ {i = 1} ^ {n} W _ {i}}
$$

where $\bar { W }$ is the weighted average of ratings, $R _ { i }$ is the rating according to criterion i, and $W _ { i }$ is the weight assigned to criterion i. When the terms $R _ { i }$ and $W _ { i }$ are represented by fuzzy sets or fuzzy numbers, the above operation is referred to as a fuzzy weighted average (FWA). Bass and Kwakernaak [3] were amongst the earliest researchers to determine the ranking of multiple alternatives with this weighted average. Later, Schmucker [37] used the FWA to propose an approximate numerical method known as the ‘‘Fuzzy Risk Analyzer’’. Furthermore, many applications such as Refs. [40,50] follow Schmucker’s procedure, and it is widely applied in risk analysis, particularly in relation to construction projects. However, Dong et al. [13] have shown that Schmucker’s discretization method can give quite irregular and incorrect membership functions because information is lost in the process of ensuring its convexity. They introduced the DSW algorithm [13] as an alternative, and dealt with the problem through interval analysis and alpha-cut representations of fuzzy sets. Later, Dong and Wong [12] employed a simple, efficient, and systemic method to develop an FWA algorithm based on the DSW algorithm. The FWA algorithm has been widely adopted in civil engineering, especially in damage assessment such as [32,36,41].

However, as this algorithm requires $O ( 2 ^ { n } )$ comparisons and arithmetic operations, Liou and Wang [27] suggested an improved fuzzy weighted average algorithm (IFWA), whilst Lee and Park [24] proposed an efficient fuzzy weighted average algorithm (EFWA). In the present study, a risk assessment model based on the fuzzy weighted average of FST will be used to calculate the overall risk faced by EC projects. The EFWA algorithm is used because it can reduce the number of comparisons and arithmetic operations to O(n log n) rather than $O ( n ^ { 2 } )$ , as is the case with the IFWA [27].

## 3. System development methodology for the FDSS

The purpose of this study is to design and develop a FDSS to assist EC project managers in identifying potential risk factors and evaluating the corresponding EC development risks. FDSS is constructed following the five-stage system development methodology, which is based on a generic IS development [31], incorporated with the method for fuzzy risk analysis [37,40,41,46]. Although this system development methodology is developed for the FDSS, we believe that other researchers can easily follow as a guideline to design and develop other FDSS for risk analysis in other application areas. The system development process consists of five stages, namely, construction of fuzzy risk analysis model, development of system architecture, analyzing and designing of the system, building of the prototype, and evaluation of the system. An overview of these five stages of system development is shown in Fig. 1. First, a fuzzy risk analysis model was constructed as the kernel of the system. Second, system architecture was developed. Third, system design and analysis were carried out in modularity with defining functionalities of the system components and an understanding of how they interact with one. Fourth, the prototype system was built in order to learn more about the concepts, framework, and design through the system-building process. Finally, the prototype system was evaluated by EC experts and potential users. Detailed descriptions of each phase are presented in the following sections.

![](/api/attachments/ZD4KEXJQ/fulltext/images/431626aa5500cba541c4cb60c22aa7fcb359d8ac4d1ec1ff19a885dbdd0aa5b4.jpg)  
Fig. 1. FDSS development methodology framework.

Table 2  
Potential risks associated with EC development

<table><tr><td>Variables</td><td>Potential risks associated with EC development</td></tr><tr><td>V1</td><td>Hacker gaining unauthorized access</td></tr><tr><td>V2</td><td>Absence of firewall</td></tr><tr><td>V3</td><td>Lack of using cryptography</td></tr><tr><td>V4</td><td>Poor “key” management</td></tr><tr><td>V5</td><td>Malicious code attacks</td></tr><tr><td>V6</td><td>Disclosure of sensitive information</td></tr><tr><td>V7</td><td>Loss of audit trail</td></tr><tr><td>V8</td><td>Natural disaster-caused equipment failure</td></tr><tr><td>V9</td><td>Human factor-caused equipment failure</td></tr><tr><td>V10</td><td>Threat of sabotage in internal network</td></tr><tr><td>V11</td><td>Inadequate backup systems</td></tr><tr><td>V12</td><td>Software or hardware problem-caused system failure</td></tr><tr><td>V13</td><td>Site or network overload and disruption</td></tr><tr><td>V14</td><td>Poor design, code or maintenance procedure</td></tr><tr><td>V15</td><td>Wrong functions and properties development</td></tr><tr><td>V16</td><td>Wrong user interface development</td></tr><tr><td>V17</td><td>Project complexity</td></tr><tr><td>V18</td><td>Wrong project size estimation</td></tr><tr><td>V19</td><td>Technological newness</td></tr><tr><td>V20</td><td>Continuous change of system requirements</td></tr><tr><td>V21</td><td>Wrong schedule estimation</td></tr><tr><td>V22</td><td>Project behind schedule</td></tr><tr><td>V23</td><td>Project over budget</td></tr><tr><td>V24</td><td>Inadequate cash flow</td></tr><tr><td>V25</td><td>Personnel shortfalls</td></tr><tr><td>V26</td><td>Lack of expertise and experience in e-commerce</td></tr><tr><td>V27</td><td>Loss of key person</td></tr><tr><td>V28</td><td>Lack of top management support</td></tr><tr><td>V29</td><td>Poor project planning</td></tr><tr><td>V30</td><td>Unclear project objectives</td></tr><tr><td>V31</td><td>Indefinite project scope</td></tr><tr><td>V32</td><td>Lack of contingency plans</td></tr><tr><td>V33</td><td>Business process redesign</td></tr><tr><td>V34</td><td>Organizational restructuring</td></tr><tr><td>V35</td><td>Lack of trust between your organization and merchant or customer</td></tr><tr><td>V36</td><td>Inappropriate media for the product and service</td></tr><tr><td>V37</td><td>Lack of international legal standards</td></tr><tr><td>V38</td><td>New laws, regulations, and judicial decisions constantly change the online legal landscape</td></tr><tr><td>V39</td><td>Uncertain legal jurisdiction</td></tr><tr><td>V40</td><td>Incompletion of contract terms</td></tr><tr><td>V41</td><td>Difficult to change outsourcing decision/vendor</td></tr><tr><td>V42</td><td>Loss of data control</td></tr><tr><td>V43</td><td>Loss of control over vendor</td></tr><tr><td>V44</td><td>Loss of control over information technology</td></tr><tr><td>V45</td><td>Hidden cost</td></tr><tr><td>V46</td><td>Lack of vendor expertise and experience</td></tr><tr><td>V47</td><td>Lock-in situation</td></tr><tr><td>V48</td><td>Vendor offers outdated technology skill</td></tr><tr><td>V49</td><td>Vendor provides poor quality service</td></tr></table>

Table 2 (continued)

<table><tr><td>Variables</td><td>Potential risks associated with EC development</td></tr><tr><td>V50</td><td>Difference users with different in culture customers, and business styles</td></tr><tr><td>V51</td><td>Language barrier</td></tr></table>

Source: Based on Wat et al. [43].

## 3.1. Phase 1: construct a fuzzy risk analysis model

Most existing risk analysis models are based on quantitative techniques such as Monte Carlo Simulation and Annual Loss Expectancy. However, the information that is related to most uncertainty factors is not numerical. FST provides an approximate model for the evaluation of the risk faced by EC projects through a linguistic approach. The procedure for fuzzy risk analysis is based on the works from Refs. [37,40, 41,46] that consisted of five steps: risk identification, natural language representation, fuzzy assessment aggregation, fuzzy weighted average computation, and linguistic approximation. The details of each stage are described in the following sections.

## 3.1.1. Risk identification

The first step is to conduct risk identification and compile a list of the most significant uncertainty factors and their descriptions. Before conducting fuzzy risk analysis, one must identify the components of risks associated with EC development. However, little empirical research has focused on identifying the potential risk factors that threaten EC development. In the study of Wat et al. [47], a source-based approach to categorizing EC development risks is initially used, with technical, organizational, and environmental risks as three primary source categories. Then the potential risks associated with EC development was identified with 51 risk items (see Table 2) associated with EC development based on a comprehensive literature review and interviewed with EC practitioners.

An empirical study was conducted with 330 valid returns used for the analysis. An exploratory factor analysis (EFA) of the survey data revealed 10 major dimensions of risks associated with EC development, namely: (1) resources risk, (2) requirements risk, (3) vendor quality risk, (4) client – server security risk, (5) legal risk, (6) managerial risk, (7) outsourcing risk, (8) physical security risk, (9) cultural risk, and (10) reengineering risk (see Table 3). As a result of the study [47], the risk classification framework as shown in Fig. 2 helps in the formulation of ways of accessing risks to EC development.

## 3.1.2. Natural language representation

According to Karwowski and Mital [22], traditional approaches to risk assessment obtain their overall risk scores by calculating the product of exposure, likelihood, and the consequences of a possible accident due to the hazard. A simpler approach that is advocated by some risk experts is to multiply the severity of consequences by the likelihood of their occurrence, as the likelihood of occurrence automatically includes exposure [45]. For example, Boehm [5] defined risk impact as the product of the probability of an unsatisfactory outcome (Likelihood) and the loss to the parties affected when the outcome is unsatisfactory (Severity). Consequently, two linguistic variables, ‘‘Likelihood’’ and ‘‘Severity’’, are defined to calculate the overall risk. In FWA, ‘‘Likelihood’’ is the rating factor (R<sub>i</sub>), and ‘‘Severity’’ is the weighting factor (W ) that corresponds to rating factor i. Both linguistic variables have five terms. ‘‘Likelihood’’ is expressed in terms of ‘‘Very Unlikely’’, ‘‘Unlikely’’, ‘‘Medium’’, ‘‘Likely’’, and ‘‘Very Likely’’ (see Fig. 3). ‘‘Severity’’ is expressed as ‘‘Minimal’’, ‘‘Low’’, ‘‘Moderate’’, ‘‘High’’, and ‘‘Critical’’ (see Fig. 4).

In this study, the membership functions of the linguistic terms are characterized by triangular fuzzy numbers, as these are very often used in applications such as fuzzy controllers, and in managerial decision making, business and finance, and the social sciences, etc. [6]. Table 4 shows the membership functions and the triangular fuzzy numbers of each linguistic term.

## 3.1.3. Fuzzy assessment aggregation

In this stage, an aggregate of several evaluators’ fuzzy assessment is performed by using the fuzzy average operation for aggregate method. By allowing more than one evaluator to assess the risks associated with an EC project, a more objective and unbiased result can be obtained. The fuzzy average operation for aggregate method that is known as the ‘‘Triangular Average Formula’’ [6] is used to determine the mean of evaluator opinions. Hence, the fuzzy average of each risk factor question from the risk assessment form can be obtained. The Triangular Average Formula is as follows:

Table 3 Results of EFA

<table><tr><td>Factor</td><td>Variables</td><td>Factor loading</td><td>Eigen value</td><td>Percentage of variance</td><td>Cumulative variance</td></tr><tr><td>Factor 1:</td><td>V21</td><td>0.640</td><td>11.567</td><td>26.900</td><td>26.900</td></tr><tr><td>Resources</td><td>V22</td><td>0.768</td><td></td><td></td><td></td></tr><tr><td>Risk</td><td>V23</td><td>0.758</td><td></td><td></td><td></td></tr><tr><td></td><td>V24</td><td>0.644</td><td></td><td></td><td></td></tr><tr><td></td><td>V25</td><td>0.464</td><td></td><td></td><td></td></tr><tr><td></td><td>V27</td><td>0.416</td><td></td><td></td><td></td></tr><tr><td>Factor 2:</td><td>V14</td><td>0.535</td><td>3.050</td><td>7.094</td><td>33.994</td></tr><tr><td>Requirements</td><td>V15</td><td>0.506</td><td></td><td></td><td></td></tr><tr><td>Risk</td><td>V16</td><td>0.627</td><td></td><td></td><td></td></tr><tr><td></td><td>V17</td><td>0.638</td><td></td><td></td><td></td></tr><tr><td></td><td>V19</td><td>0.699</td><td></td><td></td><td></td></tr><tr><td></td><td>V20</td><td>0.694</td><td></td><td></td><td></td></tr><tr><td>Factor 3:</td><td>V46</td><td>0.679</td><td>2.349</td><td>5.463</td><td>39.457</td></tr><tr><td>Vendor</td><td>V47</td><td>0.712</td><td></td><td></td><td></td></tr><tr><td>Quality</td><td>V48</td><td>0.769</td><td></td><td></td><td></td></tr><tr><td>Risk</td><td>V49</td><td>0.749</td><td></td><td></td><td></td></tr><tr><td>Factor 4:</td><td>V1</td><td>0.630</td><td>2.034</td><td>4.730</td><td>44.187</td></tr><tr><td>Client–</td><td>V2</td><td>0.745</td><td></td><td></td><td></td></tr><tr><td>Server</td><td>V3</td><td>0.750</td><td></td><td></td><td></td></tr><tr><td>Security</td><td>V4</td><td>0.732</td><td></td><td></td><td></td></tr><tr><td>Risk</td><td>V5</td><td>0.445</td><td></td><td></td><td></td></tr><tr><td>Factor 5:</td><td>V37</td><td>0.786</td><td>1.608</td><td>3.739</td><td>47.926</td></tr><tr><td>Legal Risk</td><td>V38</td><td>0.817</td><td></td><td></td><td></td></tr><tr><td></td><td>V39</td><td>0.796</td><td></td><td></td><td></td></tr><tr><td>Factor 6:</td><td>V28</td><td>0.522</td><td>1.451</td><td>3.375</td><td>51.302</td></tr><tr><td>Managerial</td><td>V29</td><td>0.648</td><td></td><td></td><td></td></tr><tr><td>Risk</td><td>V30</td><td>0.728</td><td></td><td></td><td></td></tr><tr><td></td><td>V31</td><td>0.500</td><td></td><td></td><td></td></tr><tr><td></td><td>V32</td><td>0.605</td><td></td><td></td><td></td></tr><tr><td>Factor 7:</td><td>V40</td><td>0.539</td><td>1.343</td><td>3.124</td><td>54.426</td></tr><tr><td>Outsourcing</td><td>V41</td><td>0.641</td><td></td><td></td><td></td></tr><tr><td>Risk</td><td>V42</td><td>0.698</td><td></td><td></td><td></td></tr><tr><td></td><td>V43</td><td>0.751</td><td></td><td></td><td></td></tr><tr><td></td><td>V45</td><td>0.439</td><td></td><td></td><td></td></tr><tr><td>Factor 8:</td><td>V7</td><td>0.519</td><td>1.197</td><td>2.785</td><td>57.210</td></tr><tr><td>Physical</td><td>V8</td><td>0.794</td><td></td><td></td><td></td></tr><tr><td>Security</td><td>V9</td><td>0.821</td><td></td><td></td><td></td></tr><tr><td>Risk</td><td>V10</td><td>0.493</td><td></td><td></td><td></td></tr><tr><td>Factor 9:</td><td>V50</td><td>0.804</td><td>1.112</td><td>2.586</td><td>59.796</td></tr><tr><td>Cultural Risk</td><td>V51</td><td>0.828</td><td></td><td></td><td></td></tr><tr><td>Factor 10:</td><td>V33</td><td>0.606</td><td>1.075</td><td>2.501</td><td>62.297</td></tr><tr><td>Reengineering Risk</td><td>V34</td><td>0.774</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/ZD4KEXJQ/fulltext/images/c36cb32333071b1df0cfd030cd763bdcc204940386b4be001b65bfcec8e7f6cb.jpg)  
Fig. 2. A classification framework for risk management in EC development.

![](/api/attachments/ZD4KEXJQ/fulltext/images/625cbdb4e3a12eecf9a30253491820d0fda79ffe8a8ae74de00119970ee85d2c.jpg)  
Fig. 3. Membership function of likelihood.

Consider n evaluators and let $A _ { i } { = } ( a _ { 1 } ^ { ( i ) } , a _ { M } ^ { ( i ) } , a _ { 2 } ^ { ( i ) } )$ be the fuzzy numbers, $i { = } 1 , \ldots . , n$ . Thus, the triangular average mean:

$$
\begin{array}{l} A _ {\text { average }} = \frac {A _ {1} + \cdots + A _ {n}}{n} \\ = \frac {(a _ {1} ^ {(1)} , a _ {M} ^ {(1)} , a _ {2} ^ {(1)}) + \cdots + (a _ {1} ^ {(n)} , a _ {M} ^ {(n)} , a _ {2} ^ {(n)})}{n} \\ = \frac {\left(\sum_ {i = 1} ^ {n} a _ {1} ^ {(i)} , \sum_ {i = 1} ^ {n} a _ {m 1} ^ {(i)} , \sum_ {i = 1} ^ {n} a _ {2} ^ {(i)}\right)}{n} \end{array}
$$

$$
\begin{array}{l} A _ {\text { average }} = (m _ {1}, m _ {m}, m _ {2}) \\ \qquad = \left(\frac {1}{n} \sum_ {i = 1} ^ {n} a _ {1} ^ {(i)}, \frac {1}{n} \sum_ {i = 1} ^ {n} a _ {M} ^ {(i)}, \frac {1}{n} \sum_ {i = 1} ^ {n} a _ {2} ^ {(i)}\right) \end{array}
$$

## 3.1.4. Fuzzy weighted average computation

Based on the classification framework in Fig. 2, overall EC project risk has three dimensions, which consist of 10 components. The lowest-level node encompasses a list of risks factors that are associated with EC development. Having obtained the fuzzy average with the likelihood and severity of each risk derived from previous step, the EFWA algorithm (see

![](/api/attachments/ZD4KEXJQ/fulltext/images/c54a3f06c344bfaf4260e0e18d619ee88186bc0c992d981fbeb30d60c5a4ae5f.jpg)  
Fig. 4. Membership function of severity.

Fuzzy set representation for each linguistic terms

<table><tr><td>Likelihood</td><td>Severity</td><td></td><td></td><td></td></tr><tr><td>Very unlikely</td><td>minimal</td><td>=1-4x</td><td>(0, 0, 0.25)</td><td>0≤x≤0.25</td></tr><tr><td rowspan="2">Unlikely</td><td rowspan="2">low</td><td>=4x</td><td>(0, 0.25, 0.5)</td><td>0≤x≤0.25</td></tr><tr><td>=2(1-2x)</td><td></td><td>0.25≤x≤0.5</td></tr><tr><td rowspan="2">Medium</td><td rowspan="2">moderate</td><td>=4x-1</td><td>(0.25, 0.5, 0.75)</td><td>0.25≤x≤0.5</td></tr><tr><td>=3-4x</td><td></td><td>0.5≤x≤0.75</td></tr><tr><td rowspan="2">Likely</td><td rowspan="2">high</td><td>=2x-1</td><td>(0.5, 0.75, 1)</td><td>0.5≤x≤0.75</td></tr><tr><td>=4(1-x)</td><td></td><td>0.75≤x≤1</td></tr><tr><td>Very likely</td><td>critical</td><td>=4x-3</td><td>(0.75, 1, 1)</td><td>0.75≤x≤1</td></tr></table>

Appendix A) can be applied. For a better understanding, let us consider an example. Fig. 5 illustrates a simple hierarchical structure that is designed to identify the severity of loss for ‘‘Legal Risk’’. There are three risk factors associated with ‘‘Legal Risk’’, and the fuzzy weighted average for the severity of loss is calculated as follows:

$$
\bar {W} = \frac {W _ {1} \times R _ {1} + W _ {2} \times R _ {2} + W _ {3} \times R _ {3}}{W _ {1} + W _ {2} + W _ {3}}
$$

A numerical illustration of this calculation is shown in Appendix B.

## 3.1.5. Linguistic approximation

As the result of the calculated fuzzy weighted average is a fuzzy number, it is necessary to translate it back into linguistic terms for easy interpretation.

The goal of linguistic approximation is to find the linguistic term with the closest possible meaning to that of a defined fuzzy set. There are three techniques in linguistic approximation: best fit, successive approximation, and piecewise decomposition. The difference between these three techniques was discussed by Schmucker [37]. In the present study, the best fit method is adopted because it is easy to understand and easy to implement on computers [37]. This method is based on the ‘‘Euclidean distance’’ between two fuzzy sets, as proposed by Dubois and Prade [14]. Euclidean distance is defined as:

$$
d (X, A) = \left\{\sum_ {1} [ X (i) - A (i) ] ^ {2} \right\} ^ {1 / 2}
$$

d=Euclidean distance between two fuzzy sets. X=resultant fuzzy set, and A=defined fuzzy set.

However, it is necessary to map the resultant fuzzy interval back to one of the fuzzy numbers that are defined in Fig. 4. Therefore, a modified Euclidean approach was proposed by Ross et al. [36]. The difference measure d is given as follows:

$$
\begin{array}{l} d (X, A) = \left(\sum_ {i} ^ {n} \left[ \left\{X _ {\min} (i) - A _ {\min} (i) \right\} ^ {2} \right. \right. \\ \left. + \left\{X _ {\max} (i) - A _ {\max} (i) \right\} ^ {2} \right] ^ {1 / 2} \end{array}
$$

where i is the a value and n is the number of a-cut.

![](/api/attachments/ZD4KEXJQ/fulltext/images/07d72d8ccab449699629d10830f67356bb7144440ce437f8ec2709cda148168c.jpg)  
Fig. 5. Simple hierarchical structure of legal risk.

Applying the above equation, the Euclidean distance between fuzzy set X and predefined natural language expressions (e.g. low, moderate, and high) is calculated. The model then assigns the appropriate natural language expression to the lowest Euclidian distance associated with fuzzy set X. For example, if fuzzy set X, which represents the total risk faced by an EC project, has a low Euclidian distance with a predefined natural language expression of ‘‘high’’, then the model assumes that fuzzy set X is translated as ‘‘high’’, which indicates that the total risk faced by the project is high. Refer to Appendix B for detailed numerical illustration of the application to the example of ‘‘Legal Risk’’.

## 3.2. Phase 2: develop system architecture

Good system architecture provides a road map for the system building process by placing components into perspective, defining their functionalities, and demonstrating how they will interact with one another [31]. The Web is the center of activity in developing decision support systems (DSS) [38] while client – server architecture has been widely adopted in the integration of Web-based applications [9]. The client – server relationship describes the distribution of tasks between a server and the clients who access that server. The FDSS is a client–server system with a two-tiered architecture. On the client side it is a front-end system that works with Web clients to obtain service requests and present results. On the server side, it is a back-end system that executes a fuzzy risk analysis and access database for data management. Indeed, such a two-tiered architecture is suitable when developing non-critical applications with light transaction loads such as DSS or departmental applications [11]. Since the FDSS is a client–server system, it will be executed on the Web server. Whenever a Web browser (Client) sends a request for a page to the FDSS, the code is processed at that time by the Web server. For the system components contain in the FDSS, it is composed of three interrelated components, which are (1) database, (2) model base subsystem, and (3) user interface. These three components are the basic elements in DSS [33]. Fig. 6 depicts the basic architecture of the FDSS.

## 3.3. Phase 3: analyze and design the system

Analysis and design are important aspects of the system development process. Design involves an understanding of the domain being studied, the application of various alternatives, and the synthesis and evaluation of proposed solutions. Design specifications are used as a blueprint for the implementation of the system [31]. The determination of system components and development platform is made during this phase. The design of DSS can be divided into three interrelated components, which are database, model base subsystem, and user interface [33]. The detailed specifications of these three system components, structure, and features are determined as follows.

## 3.3.1. Database

The database system is responsible for the storage of data and its management. It maintains the necessary information on each EC project. The data is obtained from an external source through manual or automated processes and the results generated by the FDSS. To manipulate databases on the Web, ActiveX Data Object (ADO) is used to interface with relational databases via the Open Database Connectivity (ODBC) protocol [2]. ADO was chosen as the data access mechanism due to its high speed, ease of use, and low memory overheads. The underlying database can be any application that supports the ODBC protocol. The current implementation makes use of Microsoft Access.

## 3.3.2. Model base subsystem (fuzzy risk analysis COM component)

The model base performs activities to provide analytical capabilities for the DSS [43]. Users can write their own models or use standard models at times. Fuzzy risk analysis model described in Section 3.1 is employed as a model base subsystem in FDSS. This model is translated into programming code and is integrated as the Component Object Model (COM). COM defines the binary interface between objects. It is a binary interoperability specification. The two most common reasons for using components are breaking up complex applications into manageable chunks and packaging code for re-use [2]. ASP scripting is mainly used to implement the FDSS. ASP script has the ability to interface with COM compliant software components. If functionality is needed but cannot be provided by scripting, then ASP components can be used. ASP components are COM-based, encapsulate a specific functionality, and are invoked either directly from an ASP page or indirectly via another ASP component [34].

![](/api/attachments/ZD4KEXJQ/fulltext/images/b5ffac950f47bb1097197981cf1a8d2db698942132665f53e98b64c579c9f0db.jpg)  
Fig. 6. System architecture.

Fuzzy risk analysis is implemented as the COM object that is stored in DLL for performing fuzzy risk analysis. When clients invoke the calculation of the overall risk faced by the EC project, the fuzzy risk analysis COM component is called to access necessary information from the database, such as the likelihood and severity of each risk factor, to perform fuzzy averaging, calculate the fuzzy weighted average, and obtain linguistic approximations. Eventually, the overall risk and risk score of each risk dimension are obtained.

## 3.3.3. User interface

The design of the user interface is a key element in DSS functionality. The DSS interface should provide easy communication between the user and the system [43]. Web browser serves as the user interface component of the DSS, which make the technology easy to understand and use [38]. Besides, the FDSS consists mainly of menus and graphics, which are supplemented by natural language. A client invokes the system by connecting to the Web site through the standard HTTP protocol, which causes the interface component to be loaded from the server to the client station. Pull-down menus allow users to specify their needs, such the creation of a new project and the addition of an evaluator record (see Fig. 7).

## 3.4. Phase 4: build the prototype system

The implementation of a system demonstrates the feasibility of the design and the utility of the functionalities that are envisaged [31]. Building a prototype system is one of the processes that allow insight into the problems and the complexity of a system during development research. FDSS is constructed using various commercial software packages and programming techniques. The detail descriptions of construction of the FDSS using these software packages and programming skills are given as below.

The prototype was run on the Windows 2000 Serverk platform. IIS was the Web server which accepted the ASP request forms that were sent from client browsers. Internet Explorer 5.0 was selected as the Web browser in the client computers. Macromedia Dreamweaverk was selected as the HTML editor for Web site and page design, and it was incorporated with Macromedia Fireworksk for the creation and editing of images, and Macromedia Flashk for the creation of animated openings.

The main body of the FDSS was written using ASP script language. VBScript was chosen for the serverside script because it is the default scripting language on the IIS server. To create more functional and interactive Web pages, JavaScript was selected as the client-side script because it is widely supported, and some browsers (e.g. Netscape Communicator 4.5) do not have the capability to interpret VBScript except with the aid of proprietary add-ons from third-party vendors. In the FDSS, JavaScript embedded in ASP code was mainly responsible for HTML form and data validation, and pull-down menus were used in the interface design. Microsoft Visual InterDev (VI) was also used to design dynamic Web applications, as it provides a development environment and collection of useful tools and utilities [9].

Visual Basick was selected for development of the fuzzy risk analysis component. According to Anderson et al. [2], there are several advantages of using Visual Basick to develop COM components. Firstly, it allows the user to write components quickly without having to spend much time learning COM. Secondly, it gives quite respectable performance. Thirdly, it is often seen as the natural progression for ASP developers learning to write components. Power [34] argues that the most common, and the simplest, component to create is Visual Basic, especially using an ActiveX DLL that is an in-process component.

The ODBC protocol was selected to communicate with the Access database because it is compatible with a variety of database systems. ADO was used to provide the database connection, as it is a set of objects that allows programmers to program their data access logic in languages such as Visual Basic, as well as in scripting languages [9].

## 3.5. Phase 5: evaluate the system

Once the system is developed, the testing and evaluation of the prototype can be performed.

![](/api/attachments/ZD4KEXJQ/fulltext/images/5bc867f8d4066446f9e9a14a56f4617c7135821d9e15fd55e17cf0bc2c511c61.jpg)  
Fig. 7. Screen for creating new project.

Through system evaluation, information can be captured on what users like and dislike, and what the system does and does not do to meet their needs. Firstly, testing and evaluation of the system were performed. All of the FDSS modules were tested for accuracy and completeness, and the outputs generated were checked and validated. These tests ensured that the system was performing functions that would meet the requirements of users by assisting them in conducting risk management for EC development. Secondly, once the FDSS was built, outcome evaluation was conducted in two phases. The first phase was domain expert evaluation, and the second phase was potential user (EC practitioner) evaluation.

There are a number of approaches to evaluate DSS. One of the criteria for the evaluation of a DSS is the measurement of the effectiveness of the system. Another evaluation criterion is to measuring user satisfaction. An evaluation form with several sections was designed. The first section measured the effectiveness and usability of the system with five-point Likert scales (1=strongly disagree, 3=undecided, 5=strongly agree). Through measuring the effectiveness of the system, we can see the ability of the system to accomplish its objectives or mission. Items to measure the usability of the system reflect the usefulness and ease of use of the system. We can therefore assess user satisfaction as one of the potential indicators of the system’s success. The second section of the evaluation form included several openended questions that were analogous to an interview in that they gave the respondents an opportunity to express themselves openly, particularly about the problems that they encountered and how the prototype could be improved. The final section collected the evaluators’ personal information.

## 3.5.1. Expert evaluation

Evaluations by domain experts help to determine the accuracy of embedded knowledge [16]. The FDSS system was validated by a group of six participants attending the ‘‘Fuzziness and Soft Computing in the New Millennium’’ session of the 9th International Fuzzy System Association World Congress and the 20th North American Fuzzy Information Processing Society International Conference. The FDSS was demonstrated and an evaluation form was distributed to the experts who presented papers in the fuzzy modeling session of the meeting. All experts were university professors and researchers with average more than 10 years working experience and good knowledge of FST. They were asked to evaluate the prototype from two perspectives: effectiveness and usability of the FDSS. For the effectiveness of the system, most respondents agreed that the prototype system was an effective risk assessment tool, in particular indicating that it can assist in assessing risks associated with EC development. For the usability of the system, most respondents considered the system quite easy to use. User’s interaction with the system was clear and understandable. They were likely to recommend the prototype system to other users.

## 3.5.2. Potential user evaluation

Evaluations by users help to determine the utility of a system according to the following criteria: ease of interaction, the extent of its capabilities, its efficiency and speed, its reliability and whether it produces useful results [16]. The evaluation form was transformed electronically and was integrated in the FDSS for user to conduct online evaluation. A total of 50 e-mails were sent to a randomly selected sample from our mailing list directory of EC practitioners in Hong Kong. Twenty-two responses were collected and stored in the FDSS database for further analysis.

The responses from the potential users are summarized in Table 5. The potential users rated the system highly on ‘‘effectiveness of the system’’ and ‘‘usability’’, with a mean score of at least 3.14 on a five-point scale (1=strongly disagree, 3=undecided, 5=strongly agree). Based on the results of the evaluation, the prototype was seen as a promising system for the management of risk in EC development.

In order to ensure the values of most the mean responses were statistically significantly different from the neutral value of the scale, which is ‘‘3— undecided’’, one-sample t-test using test value ‘‘3’’ was conducted for the 10 items. Results of t-test are presented in Table 5. Overall, the prototype evaluation is satisfactory because items 6 and 8 are not significant from the value ‘‘3’’, which is ‘‘undecided’’. The significant level for other items are smaller than 0.05 and their mean values are larger than 3.00. The viability of the FDSS in supporting risk management in EC development has been ascertained by positive feedback obtained from the evaluation form.

Table 5  
Result of prototype evaluations by potential users

<table><tr><td></td><td>Mean</td><td>S.D.</td><td>t-test</td><td>Significant level</td></tr><tr><td colspan="5">Effectiveness of the systemThe system can</td></tr><tr><td>(1) Assist in assessing risks associated with EC development.</td><td>3.59</td><td>0.96</td><td>2.890</td><td>0.009**</td></tr><tr><td>(2) Provide an effective mean to collect, store and analyze perception on potential risk to EC development.</td><td>3.64</td><td>0.95</td><td>3.130</td><td>0.005**</td></tr><tr><td>(3) Monitor and mitigate risk.</td><td>3.55</td><td>0.86</td><td>2.982</td><td>0.007**</td></tr><tr><td colspan="5">Usability of the system</td></tr><tr><td>(4) Learning to operate the system would be easy for me.</td><td>3.32</td><td>0.72</td><td>2.084</td><td>0.050*</td></tr><tr><td>(5) My interaction with the system would be clear and understandable.</td><td>3.86</td><td>0.77</td><td>5.231</td><td>0.000***</td></tr><tr><td>(6) I find the system to be flexible to interact with.</td><td>3.18</td><td>1.05</td><td>0.810</td><td>0.427</td></tr><tr><td>(7) The system&#x27;s commands are self-explained and easy to understand.</td><td>4.05</td><td>0.72</td><td>6.789</td><td>0.000***</td></tr><tr><td>(8) I find the system easy to use.</td><td>3.14</td><td>1.21</td><td>0.530</td><td>0.602</td></tr><tr><td>(9) The system is user friendly.</td><td>4.09</td><td>0.81</td><td>6.308</td><td>0.000***</td></tr><tr><td>(10) Likely to recommend to other users.</td><td>3.59</td><td>0.67</td><td>4.161</td><td>0.000***</td></tr></table>

## 4. Benefits of using FDSS

FDSS had been implemented and the results of the system evaluation showed that FDSS can be applied effectively for managing risks associated with EC development. The computations involved in the model of fuzzy risk analysis are tedious if performed manually. It is an easy task and the time for risk analysis can be significantly reduced. The Web-based FDSS automates a questionnaire instrument for risk assessment that helps the EC project managers to determine the overall risk of EC development. The benefits of using the system are as follows.

Risks associated with EC development are identified. These risk items serve as a checklist that cover possible risks associated with EC development in technical, organizational, and environmental dimensions. EC project managers or EC practitioners can be informed and be able to recognize the risks associated with EC development.

EC project managers can predict the overall risk of the project before start the implementation. An overall risk index can be used as early indicators of project problems or potential difficulties. Evaluators can keep track to evaluate the current risk level of their EC development.

The system provides an effective, systematic, and more natural way by using the proposed fuzzy risk analysis model. Evaluators can just simply use the risk evaluation checklist and use the linguistic terms to evaluate the EC development risk level.

Prioritization is necessary to provide focus for important risks [18]. A list of ranked risk items associated with EC development will be produced. Therefore, the most serious risk item will be addressed first.

## 5. Conclusions and further enhancements

EC development takes place in a complex and dynamic environment that includes high levels of risk and uncertainty. This study has outlined an approach to the assessment of the risks associated with EC development using FST. A model of fuzzy risk analysis was proposed to assist EC project managers and decision makers in formalizing the types of thinking that are required in assessing the current risk environment of their EC development in a more systematic manner than before.

A Web-based FDSS was designed and developed to incorporate the proposed risk analysis model. System evaluation was performed to ascertain whether the FDSS achieved its designed purpose, and the results were satisfactory. The feedback and comments collected from respondents were used to make necessary adjustments. The results of the evaluation strongly support the viability of the study approach to risk analysis using fuzzy sets, and demonstrated the feasibility of evaluating EC project risk.

The FDSS prototype focused on risk identification, analysis, and prioritization. Less attention was given to the risk management planning, resolution, and monitoring that is associated with EC development. Further research should be conducted into such risk management planning. In addition, risk monitoring should be conducted regularly to track the status of the identified risks. With such insight and improvement, the FDSS could be further enhanced to handle the functionality of risk management.

Moreover, it was assumed that the ‘‘weighting’’ assigned by each evaluator in the risk evaluation was the same, but the relative importance placed on certain factors by individual decision makers and experts could be widely different. Further research is needed to develop different ‘‘weightings’’ for different evaluators.

## 6. Limitations of this study

Although the prototype comes out with many advantages, it still has some limitations. The limitations of the prototype are summarized below.

In spite of the fact that the prototype evaluation shows a satisfactory outcome in the effectiveness and usability of the prototype, but FDSS do not get the chance to test it with real-life EC projects. The validity of the system can be established through in-depth case studies.

The prototype only provides the risk items based on the risk classification framework shown in Fig. 2. The list of risks shown in Table 2 is not exhaustive, but it is comprehensive enough for the purpose of this study.

For simplification, the membership functions were evenly distributed by triangular fuzzy numbers. Various membership functions need to be estimated to be as realistic as possible.

## Acknowledgements

The authors are grateful for the constructive comments of the referees and the Area Editor on an earlier version of this paper. They wish to thank all the people who have participated in the evaluation of the system as well.

## Appendix A. Algorithm procedure of EFWA (source: Ref. [24])

1. Sort a’s in non-decreasing order. Let $( a _ { 1 } , a _ { 2 } , \ldots$ $a _ { n } )$ be the resulting sequence. Let first:=1 and last:=n.

2. Let $\delta { \mathrm { - t h r e s h o l d : } } = \mathsf { l } ( f i r s t + l a s t ) / 2 \mathsf { l } .$ For each i=1,2,. . ., dthreshold, let $\ e _ { i } { : = } d _ { i }$ and for each

i=dthreshold+1,. . ., n, let $e _ { i } . = c _ { i } .$ For an n-tuple $S { = } ( e _ { 1 } , e _ { 2 } , . ~ . ~ . , e _ { n } )$ , evaluate $\delta _ { S _ { \delta - \mathrm { t h r e s h o l d } } }$ and $\delta _ { S _ { ( \delta - \mathrm { t h r e s h o l d } + 1 ) } } .$ 3. If $\delta _ { \mathrm { S } _ { \delta - \mathrm { t h r e s h o l d } } } > 0$ and $\delta _ { S _ { ( \delta - \mathrm { t h r e s h o l d + 1 } ) } } { \leq } 0$ then $\scriptstyle { \cal L } = f _ { L } ( e _ { 1 } ,$ $e _ { 2 } , \ldots , e _ { n } )$ and goto Step 4; otherwise execute the following step.

3.1. If $\delta _ { S _ { \delta - \mathrm { t h r e s h o l d } } } > 0$ then first:=dthreshold+1; otherwise last:=dthreshold, and goto Step 2.

4. Sort b’s in non-decreasing order. Let $( b _ { 1 } , \ b _ { 2 } , \ldots ,$ $b _ { n } )$ be the resulting sequence. Let first:=1 and last:=n.

5. Let $\zeta { - } \mathrm { t h r e s h o l d } . { = } \lfloor ( \mathit { f i r s t } { + } \mathit { l a s t } ) / 2 \rfloor .$ For each i=1, $2 , \ldots , \zeta _ { S _ { \zeta - \mathrm { t h r e s h o l d } + 1 } }$ , let $e _ { i } { \cdot } = c _ { i }$ and for each i=fthreshold+1,. . ., n, let $\scriptstyle e _ { i } : = d _ { i } .$ . For an n-tuple $S { = } ( e _ { 1 } ,$ $e _ { 2 } , . . . , e _ { n } ) ,$ evaluate $\zeta _ { S _ { \zeta - \mathrm { t h r e s h o l d } } }$ and $\zeta _ { S _ { \zeta - \mathrm { t h r e s h o l d } + 1 } } .$

6. $\mathrm { I f ~ } \zeta _ { S _ { \zeta - \mathrm { t h r e s h o l d } } } { > } 0$ and $\zeta _ { S _ { \zeta - \mathrm { t h r e s h o l d + 1 } } } { \leq } 0$ then $U { = } f _ { U } ( e _ { 1 } , e _ { 2 } ,$ $\ldots , e _ { n } )$ and stop; otherwise execute the following step.

6.1. If $\zeta _ { S _ { \zeta - \mathrm { t h r e s h o l d } } } { > } 0 .$ , then $\scriptstyle { \mathit { f i r s t } } : = \zeta - { \mathrm { t h r e s h o l d } } + 1 ;$ otherwise last:=fthreshold, and goto Step 5.

where

$$
\delta_ {S _ {i}} = \frac {(a _ {1} - a _ {i}) e _ {1} + (a _ {2} - a _ {i}) e _ {2} + \cdots + (a _ {n} - a _ {i}) e _ {n}}{e _ {1} + e _ {2} + \cdots + e _ {n}}
$$

$$
\zeta_ {S _ {i}} = \frac {(b _ {1} - b _ {i}) e _ {1} + (b _ {2} - b _ {i}) e _ {2} + \cdots + (b _ {n} - b _ {i}) e _ {n}}{e _ {1} + e _ {2} + \cdots + e _ {n}}
$$

## Appendix B. Illustrative example of fuzzy risk analysis

Based on Fig. 5, an illustrative example is described below. Suppose that two evaluators assess an EC project. Table 6 shows the two different evaluators’ perceptions.

Input values of two evaluators

<table><tr><td rowspan="2">Risk factors</td><td colspan="2">Evaluator A</td><td colspan="2">Evaluator B</td></tr><tr><td>Likelihood</td><td>Severity</td><td>Likelihood</td><td>Severity</td></tr><tr><td>(1) Lack of international legal standard</td><td>likely(0.5, 0.75, 1)</td><td>high(0.5, 0.75, 1)</td><td>medium(0.25, 0.5, 0.75)</td><td>critical(0.75, 1, 1)</td></tr><tr><td>(2) New laws, regulations, and judicial decisions constantly change the online legal landscape</td><td>medium(0.25, 0.5, 0.75)</td><td>high(0.5, 0.75, 1)</td><td>very likely(0.75, 1, 1)</td><td>moderate(0.25, 0.5, 0.75)</td></tr><tr><td>(3) Uncertain legal jurisdiction</td><td>medium(0.25, 0.5, 0.75)</td><td>moderate(0.25, 0.5, 0.75)</td><td>medium(0.25, 0.5, 0.75)</td><td>low(0, 0.25, 0.5)</td></tr></table>

The fuzzy average of the likelihood of risk factor 1 (lack of international legal standard) is:

$$
\begin{array}{l} = \frac {(0 . 2 5 + 0 . 5) , (0 . 5 + 0 . 7 5) , (0 . 7 5 + 1)}{2} \\ = (0. 3 7 5, 0. 6 2 5, 0. 8 7 5) \end{array}
$$

Whilst the fuzzy average of the severity of risk factor 1 is:

$$
\begin{array}{l} = (\text {High + Critical}) / 2 \\ = \frac {(0 . 5 + 0 . 7 5) , (0 . 7 5 + 1) , (1 + 1)}{2} \\ = (0. 6 2 5, 0. 8 7 5, 1) \end{array}
$$

Table 7 shows the fuzzy average of all risk factors. After obtaining the fuzzy average, the FWA can be calculated with the EFWA algorithm. Consider the three-term weighted average from Table 7,

$$
\begin{array}{r l} & y = f (R _ {1}, R _ {2}, R _ {3}, W _ {1}, W _ {2}, W _ {3}) \\ & \quad = \frac {R _ {1} \times W _ {1} + R _ {2} \times W _ {2} + R _ {3} \times W _ {3}}{W _ {1} + W _ {2} + W _ {3}} \end{array}
$$

Two values for $\alpha ,$ viz., 0 and 1, are chosen. For $\scriptstyle { \alpha = 0 }$ , the intervals of $R _ { \mathrm { i } }$ and $W _ { \mathrm { i } }$ are:

$$
\begin{array}{l} \left[ a _ {1} = 0. 3 7 5, b _ {1} = 0. 8 7 5 \right], \left[ a _ {2} = 0. 5, b _ {2} = 0. 8 7 5 \right], \\ \left[ a _ {3} = 0. 2 5, b _ {3} = 0. 7 5 \right], \end{array}
$$

Table 7 Results of fuzzy average

<table><tr><td>Risk factors</td><td>Fuzzy average of likelihood</td><td>Fuzzy average of severity</td></tr><tr><td>(1) Lack of international legal standard</td><td> $R_{1}$  (0.375, 0.625, 0.875)</td><td> $W_{1}$  (0.625, 0.875, 1)</td></tr><tr><td>(2) New laws, regulations, and judicial decisions constantly change the online legal landscape</td><td> $R_{2}$  (0.5, 0.75, 0.875)</td><td> $W_{2}$  (0.375, 0.625, 0.875)</td></tr><tr><td>(3) Uncertain legal jurisdiction</td><td> $R_{3}$  (0.25, 0.5, 0.75)</td><td> $W_{3}$  (0.125, 0.375, 0.625)</td></tr></table>

$$
\begin{array}{l} \left[ c _ {1} = 0. 6 2 5, d _ {1} = 1 \right], \left[ c _ {2} = 0. 3 7 5, d _ {2} = 0. 8 7 5 \right], \\ \left[ c _ {3} = 0. 1 2 5, d _ {3} = 0. 6 2 5 \right] \end{array}
$$

respectively for i=1, 2, 3. The computational procedure is as follows: Step 1 Sort a’s into non-decreasing order, and the resulting sequence is

$$
\begin{array}{l} \left[ a _ {1} = 0. 2 5, b _ {1} = 0. 7 5 \right], \left[ a _ {2} = 0. 3 7 5, b _ {2} = 0. 8 7 5 \right], \\ \left[ a _ {3} = 0. 5, b _ {3} = 0. 8 7 5 \right], \left[ c _ {1} = 0. 1 2 5, d _ {1} = 0. 6 2 5 \right], \\ \left[ c _ {2} = 0. 6 2 5, d _ {2} = 1 \right], \left[ c _ {3} = 0. 3 7 5, d _ {3} = 0. 8 7 5 \right] \\ \left(a _ {1}, a _ {2}, a _ {3}\right) = (0. 2 5, 0. 3 7 5, 0. 5), f i r s t := 1, l a s t := 3 \end{array}
$$

$$
\begin{array}{l} \text {Step 2} \\ \delta - \text {threshold: = l(1 + 3) / 2| = 2 , S = (0.625, 1, 0.375),} \end{array}
$$

$$
\begin{array}{r l} \delta_ {S _ {2}} & = \frac {(0 . 2 5 - 0 . 3 7 5) \times 0 . 6 2 5 + (0 . 5 - 0 . 3 7 5) \times 0 . 3 7 5}{0 . 6 2 5 + 1 + 0 . 3 7 5} \\ & = - 0. 0 1 5 6 \end{array}
$$

$$
\begin{array}{r l} \delta_ {S _ {3}} & = \frac {(0 . 2 5 - 0 . 5) \times 0 . 6 2 5 + (0 . 3 7 5 - 0 . 5) \times 1}{0 . 6 2 5 + 1 + 0 . 3 7 5} \\ & = - 0. 1 4 0 6 \end{array}
$$

$$
\delta_ {S _ {2}} <   0
$$

$$
\delta_ {S _ {3}} <   0,
$$

$$
\begin{array}{r l} \delta_ {S _ {1}} & = \frac {(0 . 3 7 5 - 0 . 2 5) \times 0 . 6 2 5 + (0 . 5 - 0 . 2 5) \times 0 . 3 7 5}{0 . 6 2 5 + 0 . 6 2 5 + 0 . 3 7 5} \\ & = 0. 1 0 5 8 \end{array}
$$

$$
\begin{array}{r l} \delta_ {S _ {2}} & = \frac {(0 . 2 5 - 0 . 3 7 5) \times 0 . 6 2 5 + (0 . 5 - 0 . 3 7 5) \times 0 . 3 7 5}{0 . 6 2 5 + 0 . 6 2 5 + 0 . 3 7 5} \\ & = - 0. 0 1 9 2 \end{array}
$$

![](/api/attachments/ZD4KEXJQ/fulltext/images/f1d4b3a21738f964271dbec4131cf9ea589ed14adcee1e2c7f0342c1810560b9.jpg)  
Fig. 8. Risk assessment form.

Since $\delta _ { S _ { 1 } } { > } 0$ and $\delta _ { S _ { ? } } { < } 0 ,$

$$
\begin{array}{l} \text {Step 5} \\ \delta - \text {threshold} := \lfloor (1 + 3) / 2 \rfloor = 2, S = (0. 1 2 5, 0. 6 2 5, 0. 8 7 5), \end{array}
$$

$$
\begin{array}{r l} L & = f _ {L} (c _ {1}, d _ {2}, d _ {3}) = a _ {1} + \delta_ {S _ {1}} = 0. 2 5 + 0. 1 0 5 8 \\ & = 0. 3 5 5 8 \end{array}
$$

$$
\begin{array}{r l} \delta_ {S _ {2}} & = \frac {(0 . 7 5 - 0 . 8 7 5) \times 0 . 1 2 5 + (0 . 8 7 5 - 0 . 8 7 5) \times 0 . 8 7 5}{0 . 1 2 5 + 0 . 6 2 5 + 0 . 8 7 5} \\ & = - 0. 0 0 9 6 \end{array}
$$

Min $f _ { L }$ is 0.3194 and go to Step 4.

Step 4

Sort b’s into non-decreasing order, and the resulting sequence is

$$
\begin{array}{r l} \delta_ {S _ {3}} & = \frac {(0 . 7 5 - 0 . 8 7 5) \times 0 . 1 2 5 + (0 . 8 7 5 - 0 . 8 7 5) \times 0 . 6 2 5}{0 . 1 2 5 + 0 . 6 2 5 + 0 . 8 7 5} \\ & = - 0. 0 0 9 6 \end{array}
$$

$$
[ a _ {1} = 0. 2 5, b _ {1} = 0. 7 5 ], [ a _ {2} = 0. 3 7 5, b _ {2} = 0. 8 7 5 ],
$$

$$
[ a _ {3} = 0. 5, b _ {3} = 0. 8 7 5 ], [ c _ {1} = 0. 1 2 5, d _ {1} = 0. 6 2 5 ],
$$

$$
[ c _ {2} = 0. 6 2 5, d _ {2} = 1 ], [ c _ {3} = 0. 3 7 5, d _ {3} = 0. 8 7 5 ]
$$

$$
(b _ {1}, b _ {2}, b _ {3}) = (0. 7 5, 0. 8 7 5, 0. 8 7 5), \text { first } := 1, \text { last } := 3
$$

Step 6

As $\delta _ { S _ { 2 } } { < } 0$ and $\delta _ { S _ { 3 } } { < } 0$ , execute the following step. Step 6.1

Let last:=2 and go to Step 5.

$$
\begin{array}{l} \text {Step 5} \\ \delta - \text {threshold: = } (1 + 2) / 2 \text {=} 1, S = (0. 1 2 5, 1, 0. 8 7 5), \\ \delta_ {S _ {1}} = \frac {(0 . 8 7 5 - 0 . 7 5) \times 1 + (0 . 8 7 5 - 0 . 7 5) \times 0 . 8 7 5}{0 . 1 2 5 + 1 + 0 . 8 7 5} \\ = 0. 1 1 7 2 \\ \delta_ {S _ {2}} = \frac {(0 . 7 5 - 0 . 8 7 5) \times 0 . 1 2 5 + (0 . 8 7 5 - 0 . 8 7 5) \times 0 . 8 7 5}{0 . 1 2 5 + 1 + 0 . 8 7 5} \\ = - 0. 0 0 7 8 \\ \text {As} \delta_ {S _ {1}} > 0 \text {and} \delta_ {S _ {2}} <   0, \\ U = f _ {U} (d _ {1}, c _ {2}, c _ {3}) = b _ {1} + \delta_ {S _ {1}} = 0. 7 5 + 0. 1 1 7 2 \\ = 0. 8 6 7 2 \end{array}
$$

Max $f _ { U }$ is 0.8672 and stop.

Accordingly, the interval for a=0 is (0.3558, 0.8672), in which each point corresponds to the end points of the triangle that represent the membership functions. The process is repeated for a=1, and the result obtained is (0.6417, 0.6417), which corresponds to the center of the triangle.

As the results are fuzzy numbers, Euclidean distances are used to map the resultant fuzzy interval back to linguistic terms.

$$
\begin{array}{l} d (X, A) = \left(\sum_ {i} ^ {n} [ \{X _ {\min} (i) - A _ {\min} (i) \} ^ {2} + \{X _ {\max} (i) - A _ {\max} (i) \} ^ {2} ]\right) ^ {1 / 2} \end{array}
$$

where i is the a value and n is the number of a-cut. Based on the results, the Euclidean distances are:

$$
\begin{array}{l l} d (X, \text { Minimal }) = 0. 9 5 8 8; & d (X, \text { Low }) = 0. 6 4 4 1; \\ d (X, \text { Moderate }) = 0. 2 1 2 2; & d (X, \text { High }) = 0. 2 2 4 0; \\ d (X, \text { Critical }) = 0. 5 4 9 0 \end{array}
$$

![](/api/attachments/ZD4KEXJQ/fulltext/images/ce790ffafeb19e3f7618e9ce9933c7d54beafd31191584975ef8e233f113a9c6.jpg)  
Fig. 9. Risk assessment result.

The closest Euclidean distance is 0.2122, which means the legal risk is considered as moderate.

Appendix C. Illustrative example of the use of the FDSS for risk assessment in EC development

In this appendix, examples of a dialogue between a user and the prototype FDSS are shown. Annotations are added to give a deeper insight into the operation of the FDSS.

To conduct a risk analysis for a new project, the evaluator first creates a project evaluation record by clicking on ‘‘New’’ in the ‘‘Project’’ menu (see Fig. 7). The evaluator can then click on the Assessment button to start the fuzzy risk analysis. The risk assessment form is displayed and lists all of the identified risk factors from the database. Based on previous project development experience and their own perception, the evaluator can proceed to define the likelihood and severity of each risk factor in natural language. The first page of the risk evaluation form consists of technical risk factors. The evaluator can click on the radio button for the risk factor, ‘‘Hacker gaining unauthorized access’’, to indicate its likelihood (e.g. ‘‘very unlikely’’) and severity (e.g. ‘‘critical’’). The evaluator can click on the risk factor for further explanation (see Fig. 8). He/she can then go to the next risk assessment form by clicking on the Next button. When all of the risk factors are evaluated, the fuzzy risk analysis COM component is invoked and the overall risk faced by the project is assessed. Fig. 9 shows the results based on inputted information and other evaluator answers for a particular project. The FDSS indicates that the overall risk for the selected project is moderate, and the score for each risk dimension is represented by an image bar.

## References

[1] J. Anderson, R. Narasimhan, Assessing project implementation risk: a methodological approach, Management Science 25 (6) (1979) 512–521.

[2] R. Anderson, A. Homer, S. Robinson, Beginning Components for ASP, Wrox Press, Birmingham, 1999.

[3] S.M. Bass, H. Kwakernaak, Rating and ranking of multipleaspect alternatives using fuzzy sets, Automatica 1 (1) (1977) 47– 58.

[4] J.C. Bennett, G.A. Bohoris, E.M. Aspinwall, R.C. Hall, Risk analysis techniques and their application to software development, European Journal of Operational Research 95 (1996) 467– 475.

[5] B.W. Boehm, Software Risk Management, IEEE Computer, Society Press, Washington, DC, 1989.

[6] G. Bojadziev, M. Bojadziev, Fuzzy Logic for Business, Finance, and Management, World Scientific, Singapore, 1997.

[7] S. Bonvicini, P. Leonelli, G. Spadoni, Risk analysis of hazardous materials transportation: evaluating uncertainty by means of fuzzy logic, Journal of Hazardous Materials 62 (1) (1998) 59– 74.

[8] J.B. Bowles, C. Pelaez, Enrique fuzzy logic prioritization of failures in a system failure mode, effects and criticality analysis, Reliability Engineering and Systems Safety 50 (2) (1995) 203– 213.

[9] D. Buser, J. Kauffman, J.T. Llibre, B. Francis, D. Sussman, C. Ullman, J. Duckett, Beginning Active Server Page 3.0, Wrox Press, Birmingham, 1999.

[10] W.G. de Ru, J.H.P. Eloff, Risk analysis modeling with the use of fuzzy logic, Computer Security 15 (3) (1996) 239 – 248.

[11] A. Dickman, Two-tier versus three-tier apps, Information Week 553 (1995) 74– 77.

[12] W.M. Dong, F.S. Wong, Fuzzy weighted averages and implementation of the extension principle, Fuzzy Sets and Systems 21 (1987) 183– 199.

[13] W.M. Dong, H.C. Shah, F.S. Wong, Fuzzy computations in risk and decision analysis, Civil Engineering Systems 2 (1985) 201–208.

[14] D. Dubois, H. Prade, Fuzzy Sets and Systems, Academic Press, New York, 1980.

[15] F. Gardin, R. Power, E. Martinelli, Liquidity management with fuzzy qualitative constraints, Decision Support Systems 15 (1995) 147– 156.

[16] J. Gasching, P. Klahr, H. Pople, E. Shortliffe, A. Terry, Evaluation of expert systems: issues and case studies, in: F. Hayes-Roth, D.A. Waterman, D.B. Lenat (Eds.), Building Expert Systems, Addison-Wesley, Massachusetts, 1983, pp. 241– 280.

[17] M. Greenstein, Electronic Commerce: Security Risk Management and Control, McGraw-Hill, New York, 2000.

[18] E.M. Hall, Managing Risk: Methods for Software Systems Development, the SEI Series in Software Engineering, Addison Wesley, Massachusetts, 1998.

[19] C. Huang, Fuzzy risk assessment of urban natural hazards, Fuzzy Sets and Systems 83 (2) (1996) 271 – 282.

[20] C.H. Junag, X.H. Huang, D.J. Elton, Fuzzy information processing by the Monte Carlo simulation technique, Civil Engineering Systems 8 (1) (1991) 19 – 25.

[21] R. Kalakota, A.B. Whinston, Frontiers of the Electronic Commerce, Addison-Wesley, Reading, MA, 1996.

[22] W. Karwowski, A. Mital, Potential applications of fuzzy sets in industrial safety engineering, Fuzzy Sets and Systems 19 (1986) 105– 120.

[23] H.M. Lee, Applying fuzzy set theory to evaluate the rate of aggregative risk in software development, Fuzzy Sets and Systems 79 (3) (1996) 323 – 336.

[24] D.H. Lee, D. Park, An efficient algorithm for fuzzy weighted average, Fuzzy Sets and Systems 87 (1997) 39–45.

[25] Y.W. Lee, M.F. Dahab, I. Bogardi, Fuzzy decision making in ground water nitrate risk management, Water Resources Bulletin 30 (1) (1994) 135– 148.

[26] H.M. Leung, K.B. Chuah, V.M.R. Tummala, A knowledgebased system for identifying potential project risks, OMEGA: International Journal of Management Science 26 (5) (1998) 623 – 638.

[27] T.J. Liou, M.J.J. Wang, Fuzzy weighted average: an improved algorithm, Fuzzy Sets and Systems 49 (1992) 307–315.

[28] G. McDonald, http://www.just.how.risky.is.the.internet? Management Accounting 78 (3) (2000) 74– 75.

[29] C. Mceachern, Technology risks: don’t panic. Financial services firms seem to have cyber risk under control, Wall Street+ Technology (April 2001) 38.

[30] D.R. Moscato, Database gateway processor risk analysis using fuzzy logic, Information Management and Computer Security 6 (3) (1998) 138–144.

[31] J.F. Nunamaker, M. Chen, D.M. Purdin, Systems development in information systems research, Journal of Management Information Systems 7 (1990) 89 – 106.

[32] P.C. Pandey, S.V. Barai, Sensitivity-based weighted-average in structural damage assessment, Journal of Performance of Constructed Facilities 8 (4) (1994) 243 – 263.

[33] J.M. Pearson, J.P. Shim, An empirical investigation into DSS structures and environments, Decision Support Systems 13 (1995) 141– 158.

[34] S. Power, Developing ASP Components, O’Reilly, California, 1999.

[35] R.K.J.R. Rainer, C.A. Snyder, H.H. Carr, Risk analysis for information technology, Journal of Management Information Systems 8 (1) (1991) 129 – 147.

[36] T.J. Ross, H.C. Sorensen, S.J. Savage, J.M. Carson, DAPS: expert system for structural damage assessment, Journal of Computing in Civil Engineering 4 (4) (1990) 327 – 348.

[37] K.J. Schmucker, Fuzzy Sets, Natural Language Computations and Risk Analysis, Computer Science Press, Rockville, MD, 1984.

[38] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2002) 111 – 126.

[39] T. Stoehr, Managing e-Business Projects: 99 Key Success Factors, Springer, Hamburg, 2002.

[40] J.H.M. Tah, V. Carr, A proposal for construction project risk assessment using fuzzy logic, Construction Management & Economics 18 (2000) 491–500.

[41] A.B. Tee, M.D. Bowman, Bridge condition assessment using fuzzy weighted averages, Civil Engineering Systems 8 (1) (1991) 49 – 57.

[42] S.H. Tsaur, G.H. Tzeng, K.C. Wang, Evaluating tourist risks from fuzzy perspectives, Annals of Tourism Research 24 (4) (1997) 796– 812.

[43] E. Turban, Decision Support and Expert Systems: Management Support System, 4th ed., Prentice-Hall, New Jersey, 1995.

[44] D.W. Viehlandm, Managing business risk in electronic commerce, Americas Conference on Information Systems.

[45] A. Waring, A.I. Glendon, Managing Risk, International Thomson Business Press, London, 1998.

[46] F.K.T. Wat, E.W.T. Ngai, Risk analysis in electronic commerce development using fuzzy set, Proceedings of the Joint 9th IFSA World Congress and 20th NAFIPS International Conference, IEEE, Piscataway, WJ, vol. 2, 2001, pp. 807–811.

[47] F.K.T. Wat, E.W.T. Ngai, T.C.E. Cheng, Potential risks to ecommerce development using exploratory factor analysis, International Journal of Services Technology and Management, (2004) (in press).

[48] M. Webster, The Merriam-Webster Dictionary, Merriam-Webster, Springfield, MA, 1994.

[49] D. White, Application of systems thinking to risk management: a review of the literature, Management Decision 3 (10) (1995) 35 – 45.

[50] E.N. Wirba, J.H.M. Tah, R. Howes, Risk interdependencies and natural language computations, Engineering Construction and Architectural Management 3 (4) (1996) 251 – 269.

[51] L.A. Zadeh, Fuzzy sets, Information and Control 8 (1965) 338 – 353.

![](/api/attachments/ZD4KEXJQ/fulltext/images/800a7e9c9533aed8301516cc11884340b288d2234b468e061d0d936f5eb33ba0.jpg)

Dr. Eric W.T. Ngai is currently an Associate Professor in the Department of Management and Marketing at The Hong Kong Polytechnic University. His research interests are in the areas of e-commerce, decision support systems, supply chain systems and knowledge management systems. He has published in a number of journals including IEEE Transactions on Systems, Man and Cybernetics, Information and Management, Expert Systems and Applica-

tions, Expert Systems, International Journal of Operations and Production Management, Omega, European Journal of Marketing, European Journal of Operational Research, International Journal of Production Economics, Transportation Review and others. Dr. Ngai serves on the Editorial Board of International Journal of Production Research.

![](/api/attachments/ZD4KEXJQ/fulltext/images/435cd84cf1032f9dd71d50b8c6c184cc6e402a307ec07f6c9f6b74393426ba8c.jpg)

Mr. Francis K.T. Wat is currently a Research Associate in the Department of Management and Marketing at The Hong Kong Polytechnic University. He was awarded the degrees of BSc (Hons) and MPhil from The Hong Kong Polytechnic University. His current research interests are in the areas of e-commerce, management information systems and fuzzy systems. He has published in journal such as Information & Manage-

ment, Omega, International Journal of Services Technology and Management.
