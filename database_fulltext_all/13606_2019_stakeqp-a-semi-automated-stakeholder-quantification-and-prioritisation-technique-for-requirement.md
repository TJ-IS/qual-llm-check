---
otero_id: 13606
otero_key: "27XXRAWR"
title: "StakeQP: A semi-automated stakeholder quantification and prioritisation technique for requirement selection in software system projects"
authors: "Fadhl Hujainah; Rohani Binti Abu Bakar; Mansoor Abdullateef Abdulgabber"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.04.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# StakeQP: A semi-automated stakeholder quantification and prioritisation technique for requirement selection in software system projects

![](/api/attachments/27XXRAWR/fulltext/images/5d2fc54be348f30f5bd552f26d1a46d001e912f769abbf5d5885a0d82cac1411.jpg)

Fadhl Hujainah<sup>a,⁎</sup>, Rohani Binti Abu Bakar<sup>b</sup>, Mansoor Abdullateef Abdulgabber<sup>c</sup>

<sup>a</sup> Software Engineering Research Group, Faculty of Computer Systems and Software Engineering, Universiti Malaysia Pahang, Kuantan 26300, Malaysia <sup>b</sup> Soft Computing and Intelligent System Research Group, Faculty of Computer Systems and Software Engineering, Universiti Malaysia Pahang, Kuantan 26300, Malaysia Faculty of Computer and Cyber Science, Software Engineering, University Prince Mugrin, Al-Madinah 41499, Saudi Arabia

## A R T I C L E I N F O

Keywords: Stakeholder analysis Stakeholder prioritisation Stakeholder quantification Multi-attribute decision-making TOPSIS Software system project

## A B S T R A C T

Stakeholder quantification and prioritisation (SQP) is performed on the basis of the stakeholder's influence. The involvement of adequate stakeholders plays a crucial role in identifying and selecting the most essential requirements to produce a successful system. However, the current SQP techniques still face serious limitations, such as having insuficient low-level implementation details, being time-consuming, lacking an automation level, heavily relying on professional expertise and having no attribute measurement criteria (AMC) for stakeholder evaluation. These key issues serve as the motivation of the present study. Hence, this study is aimed at proposing a new semi-automated technique called StakeQP to address the reported key limitations. StakeQP introduces new low-level implementation details to perform SQP automatically on the basis of the newly proposed AMC using the multi-attribute decision-making method, namely, the technique of order preference similarity to the ideal solution (TOPSIS), to achieve an eficient StakeQP. The efectiveness of StakeQP is evaluated using a benchmark dataset of the actual software project. The findings show that StakeQP can produce more accurate results with less time consumption and is more efective in addressing the defined key limitations compared with other alternative techniques.

## 1. Introduction

Requirement engineering is a crucial phase in system development which involves eliciting, documenting and maintaining system requirements [1–3]. This process is conducted on the basis of stakeholder preferences [1,4]. Hence, selecting appropriate key stakeholders is essential to identifying and capturing the complete requirements that are relevant to the system, resulting in a good-quality system [5–7]. As reported in [8,9], the system project success rates were 29%, 27%, 32%, 28% and 29% from 2011 to 2015. This outcome indicates that many projects failed to produce a successful system. The participation of stakeholders, who lack power, knowledge, interest and influence, re sulting in a low-quality system, is a major cause of failure in many system projects [4,5,10–12].

System development projects are usually performed with limited time, cost, materials and staf. Consequently, it is dificult to implement and develop all stakeholder requirements with these limited resources [3,13]. Thus, identifying and prioritising requirements are essential to capturing the core requirements based on the stakeholders' preferences. Selecting the most essential and complete requirements can only be achieved with the involvement of appropriate and core stakeholders [4,5,14,15]. However, stakeholders have diferent influences on the success of system development proiects [10.11.16]. These differences can be influenced by their knowledge, interest, power and role on the system projects [5,10,16,17]. Furthermore, the number of diferent types of participating stakeholders can be immense, with each one construing their requirements diferently. This diference will create complications in deciding which stakeholders have more influence on the project than others [4,11,18]. Thus, the stakeholder quantification and prioritisation (SQP) process is conducted to identify the influence (priority) value of each stakeholder (SPV) and prioritises them on the basis of the identified influence values [6,11,18], where the stakeholders are quantified and prioritised on the basis of certain attributes, such as power, influence and role [5,6].

Additionally, detecting the stakeholders' influences and prioritising their importance accordingly can assist the project manager in pro viding a clear view about the expectations, roles and needs of the stakeholders who have a potential influence on a certain activity of the project development process, which assists managers in factoring in the planning project in order to win support from the most influential stakeholders [6,17,19–21]. Obtaining such support will bring more potential resources to the project development, which will induce an increase in the possibility of producing a successful project [6,17,19].

The majority of existing studies related to stakeholder analyses are mainly focused on the stakeholder identification process and do not precisely emphasise the quantification and prioritisation process of the stakeholder [4,18], while few techniques in the stakeholder analysis are concerned with the SQP process, such as Babar et al. (StakeMeter) [18]. At a glance, these techniques have usefully emphasised the process of quantifying and prioritising the stakeholders. Nonetheless, a close look reveals that these techniques still sufer from certain challenges with respect to being time-consuming, lacking an automation level, and having insuficient low-process level details of SQP, in addition to the non-existence of a standard measurement criterion for evaluating the stakeholders' influence based on the SQP attributes and a heavy reliance on the involvement of experts in performing SQP; these chal lenges can promote issues of expert unavailability and natural human biases [4,5,11,18]. Possible biases can occur when experts evaluate the stakeholders with a given input of the priority value of each stake holder. These biased inputs or evaluations can significantly impact the quality of the technique in terms of identifying the accurate priority values of the stakeholder, which will negatively impact the reliability of the prioritised list of these stakeholders and the identification quality of the core stakeholder to be considered in the development process [4,11,18]. Concerning the issue of the unavailability of experts, heavy reliance on highly professional human judgement is not preferred due to threats that are related to the validity of the technique in case there is a shortage of expertise in the SQP domain. In such a case, the execution of the technique (which requires good expertise in the stakeholder analysis) without the participation of good expertise can lead to difi culty in absorbing and interpreting the requirements needed in executing or initiating the technique, along with the issue of increasing the possibility of implementing the technique in a non-proper and professional way that will directly influence the quality of the result produced [4,11,18].

The incapability of the technique in providing low-level details of implementation for the SQP process, along with the absences of attribute measurements criteria, induce low accuracy results since the ambiguity in the existing techniques can lead to a threat of executing the process in contrary to or beneath the standards expected in a specific profession [4,18]. Regarding the issues of the deficiency of the automation level and not being cost-efective with respect to time utilisa tion, conducting the SQP process without employing the automation influences the eficiency of the technique with respect to it being more complex when quantifying and prioritising the stakeholders due to the manual process that will be required to execute the computational calculation to obtain the relative priority value of each stakeholder [4,11,18]. This manual computational complexity requires more efort in terms of time and increases the likelihood of human errors, indicating that the technique is impractical in a real scenario of being adopted in quantifying and prioritising stakeholders [4,18].

To address these SQP challenges, this study proposes a new SQP technique, namely, StakeQP. The proposed technique can perform SQP and produce a prioritised list of stakeholders automatically, removing the manual process with less time consumption as well as providing clear and low-level implementation details to be easily applied in academics and industries. Moreover, StakeQP includes the attribute mea surement criteria (AMC), which are proposed for use in evaluating each stakeholder's influence on the basis of SQP attributes to minimise the need for expert involvement during the SQP, thereby reducing the expert biases, as well as solving the issue of expert unavailability. Furthermore, the automation tool is developed and presented to automate the StakeQP process. The benchmark dataset of the RALIC industrial project documented in [22,23] is used to implement and evaluate the performance of the StakeQP and compare it with that of other existing SQP techniques.

The remainder of this paper is structured into seven main sections, as follows. Section 2 describes the related works on SQP. Section 3 il lustrates the proposed StakeQP technique in detail with respect to its proposed phases. Section 4 elaborates on the developed automation implementation tool (AIT) of the proposed StakeQP. Section 5 presents the evaluation of the proposed StakeQP technique. Section 6 discusses the performance analysis and evaluation of the results. Section 7 enumerates the threats of the validity, and Section 8 concludes this study.

## 2. Related works

Stakeholder theory was established by Freeman in recognition of the significance of the stakeholder management in securing the success in the development of the firm's projects [24]. This theory was then grown to include a variety of fields, such as organisational management [25], business society and ethics [20,26], as it is evident that organi sations' projects generally have an extensive variety of stakeholders, and these compete for available resources, leading to dificulty in making a decision of specifying the core stakeholders [4,6,21,25]. Thus, identifying the strategies for managing stakeholders is an important task for managers, leading them to a better understanding of the stakeholders' project networks and the possible impacts of the stakeholders. This will induce the decision makers of the organisation to make more efective and realistic strategic decisions on the development process of the organisation's project [20,25,27]. Additionally, the perspective of the stakeholder analysis can assist the managers in identifying the most influential stakeholders that the firm seeks support from and directs the managers to incorporate those stakeholders' concerns into the strategic plans, leading them to win more support and carry on the development of the project by increasing the chances of developing a successful project [6,17].

While stakeholder analysis techniques have been extensively presented in various contexts, few studies concentrate specifically on the SQP process [4,18]. Razali and Anwar [28] proposed a conceptual framework that presented high-level details of the selection process in quantifying and prioritising the stakeholders based on the stakeholder's role, education, experience, job scope, interest inventory, and personality test [18,28]. Likewise, the technique of McManus [29] involves performing the SQP process by categorising the stakeholders into primary, secondary and external stakeholders based on expert judgement, in which the positional power attribute (PPA), interest attribute (IA) and role influence attribute (RIA) are considered [4,30]. Furthermore, the analytic hierarchy process (AHP) has been used to quantify and prioritise the stakeholders based on the influence attribute with a lack of low implementation details, requiring the need for expert participation to perform the pairwise comparisons [31,32]. Bendjenna et al. [33] introduced a technique to prioritise stakeholders using a multi-criteria analysis on the basis of urgency, power and legitimacy attributes, whereas the fuzzy Choquet integral was used as an integration operator for these attributes. The authors reported that the results of the proposed technique are not widely accepted due to the use of rapid elicitation [33].

In addition, the Ballejos and Montagna technique was documented in [34] with the aim of performing the SQP of information systems based on the role, influence, power and interest attributes. Even though this technique provides the ability of handling the competency problem among the considered attributes. it is not cost effective with respect to time consumption [18]. Similarly, the Lim et al. StakeNet technique quantifies and prioritises stakeholders and their roles with respect to the RIA on the basis of stakeholders' recommendations and the applying social network measures with the non-existence of the AMC [22]. This technique is one of the first techniques that has been tested with an actual industrial project, and the results show an accuracy of 75% [22]. However, the results of the prioritised list of the stakeholders using this technique is directly afected by the stakeholders' recommendations, so human expertise is exceedingly desirable in order to initiate and exe cute the technique [4,18,22].

Furthermore, Babar et al. [35] proposed a technique for a value-based software system called Star Triangle that presented high-level details of quantifying and prioritising the stakeholders based on a knowledge and experience attributes [35]. To further improve the eficiency performance of the Star Triangle, Babar et al. [30] presented a bi-metric technique by employing the fuzzy c-means to present the overall SPV [30]. Thereafter, Babar et al. [18] extended the previous two techniques (Star Triangle and bi-metric) by proposing the StakeMeter technique, which presented a manual SQP process with more low-level implementation guidelines, at tributes, metrics and application procedures compared to other techni ques. However, these techniques presented by Babar et al. require a deep knowledge and good expertise to be employed in order to interpret and execute the process and the measurement criteria for each attribute used in measuring the SPV were not provided [18,30].

On the other hand, a recent theoretical approach has been docu mented that aims to quantify and prioritise the stakeholders' influences on the discipline of housing energy, in which the influences of the stakeholders are manually measured based on the experts' judgements with respect to the attributes of the power, proximity, and interest [6]. In addition, Mascena et al. [17] conducted an investigation study that highlights a detailed description of the SQP in the industry sector and provides a theoretical contribution that is associated with the analysis of the industry factor with respect to the prioritisation of the stakeholders on the basis of their interest. Two other recent studies, [4,5], respectively provided a systematic literature review and a systematic mapping on SQP domain. The detailed analysis of the existing SQP techniques in terms of the limitation was conducted. The results of these two studies, along with others [18,30,33,34,36,37], indicated that the existing techniques face key issues, such as being time-consuming, having insuficient low-level implementation details of the SQP process, having a heavy reliance on expert participation to perform the process, lacking the measurement criteria of the SQP attributes, lacking automation, and having dificulty in producing accurate and accepted results and a final prioritised list of the stakeholders.

Therefore, on the basis of the reported limitations of the existing SQP techniques, the current work presents a new SQP technique, namely, StakeQP, which can produce a ranked list. This list is the result of the SQP with an automation level and low-level details of the SQP implementation with minimal expert involvement in performing the process given the standard measurement criteria for each attribute considered in determining the SPV. The following section presents a detailed explanation of the proposed StakeQP technique.

## 3. Proposed StakeQP technique

Fig. 1 shows the process of the proposed StakeQP technique. This technique is aimed at quantifying and prioritising stakeholders. The StakeQP process consists of three main phases, as follows:

i. Phase 1: Establishment phase

a. Finalise the StakeQP attributes

b. Propose the AMC.

c. Formulate the attribute weight values and the AMC values.

ii. Phase 2: Stakeholders' profile collection.

iii. Phase 3: Formulate the SPV by calculating the stakeholder's attribute value (SAV) and employing the technique of order preference similarity to the ideal solution (TOPSIS) method.

## 3.1. Establishment phase

The establishment phase is constructed initially in the StakeQP technique to present the low-level details of the StakeQP attributes along with their proposed AMC and to specify the weights of each StakeQP attribute with its AMC on the basis of the experts' inputs. These specified weight values of the attributes and the AMC are used to measure and assess the importance of the stakeholders for each StakeQP attribute. Then these attributes are used in specifying the final SPV while minimising the need for direct expert involvement in assigning the SPV to the stakeholder. Therefore, this phase is considered to be the basis for performing the full process of the proposed StakeQP technique. This phase consists of three sub-phases, and the explanation of these phases is illustrated precisely in following sub-sections.

## 3.1.1. Finalising the StakeQP attributes of the SQP

The first step of the proposed technique is to finalise the attributes that will be used to perform the SQP in the StakeQP. Fig. 2 presents the attributes selected for use in the SQP of the proposed technique.

Four main attributes and two subdivided attributes are selected. These attributes include the role influence (RIA), the positional power attribute (PPA), interest (IA), and knowledge (KA), which is further subdivided into two attributes: experience (EA) and educational background (EBA). These attributes are referred to as StakeQP attributes in this study. Table 1 presents the definition of the StakeQP attributes. These attributes are retrieved from the literature review of the SQP studies [7,16,20,25,43–45]. These attributes are considered to be the most important SQP attributes in the SQP domain. This importance is due to the fact that the high impact of these attributes in the common practices of evaluating the stakeholders' salience with respect to their power, knowledge, experience, and role responsibility can be imposed on the project development and when measuring the stakeholders' interest towards the success of the project.

## 3.1.2. Proposed AMC

In this section, the measurement criteria of each listed StakeQP attribute are proposed and discussed in detail. The proposed measurement criteria are used to calculate the SAV for each StakeQP attribute, which assists in identifying the final SPV. The AMC is a measurement used to assess the stakeholders' influence on each attribute. The SAV refers to the value of the stakeholder for each StakeQP attribute. This value is measured on the basis of the proposed AMC. Hence, each listed StakeQP attribute will have diferent measurement criteria, as follows.

a. RIA Measurement Criteria (RIA-MC): The important degree of influence of the stakeholders' role is related to the role responsibility (job scope) of the stakeholders in a project [34]. Hence, the role responsibility and job scope are used to measure the degree of influence of the stakeholders' role. System stakeholders can have various roles on system development projects, such as suppliers, support staf and developers. These roles can be classified into different groups based on the stakeholder roles and concerns. To capture all the roles of the system's stakeholders in our proposed technique, we adopt the standard group of stakeholder roles in the system development projects [38–40]. Merging the roles of groups from the three standard resources is essential because it suficiently covers the role of groups that can exist in system development projects. However, the role of experts and specialists are added to the list of the merged roles of groups to solve issues that cannot be solved by the participating stakeholders [41]. Table 2 in Appendix A presents the list of stakeholder role groups along with the description of each group used as a measurement criterion for the RIA.

b. PPA Measurement Criteria (PPA-MC): The influence level of the stakeholders' degree of power can be measured on the basis of the authority level of the stakeholders in organisations. This authority level indicates the position power (management level) type of the stakeholders [42,43]. Therefore, this attribute can be measured using the standard position levels of stakeholders in organisations [42–45]. These four levels include the top, middle, supervisory and worker levels. The first three levels (namely, top, middle and supervisory) are stated in [43–45]. The stakeholder has the managerial position power. In [42], the worker level was introduced as the fourth level to represent individual workers who do not hold any managerial position. Table 2 in Appendix A presents the explanation of the four levels.

![](/api/attachments/27XXRAWR/fulltext/images/76ca51a71ea07b7480c09ae53e08d164c07c9063d6476aacc687b2afc27afb79.jpg)  
Fig. 1. Process of the StakeQP technique.

![](/api/attachments/27XXRAWR/fulltext/images/c1baa05e8da4e73e75bd58a4a4e6955164fa4a58dc486693602e5808ebe02861.jpg)  
Fig. 2. StakeQP attributes.

Table 1  
Definitions of the StakeQP attributes.

<table><tr><td>Attributes</td><td>Description</td><td>Usage</td></tr><tr><td>RIA</td><td>The influence of the stakeholder&#x27;s role responsibility</td><td>To measure the degree of influence of the stakeholders&#x27; role</td></tr><tr><td>PPA</td><td>The level of the stakeholders&#x27; authority based on their positional power that can be imposed on the project&#x27;s development or objectives</td><td>To measure the authority level of the stakeholders over a project</td></tr><tr><td>IA</td><td>The level of concern of the stakeholders towards achieving the defined goals of the system project</td><td>To measure the concern or willingness level of the stakeholders to allow the system project to satisfy its specified objectives or goals</td></tr><tr><td>KA</td><td>The knowledge level of the stakeholders about a related domain.</td><td>To measure the influence level of stakeholders&#x27; knowledge based on their years of experience and educational background level</td></tr><tr><td>EA</td><td>Previous experience of the stakeholders in the related domain</td><td>To measure the stakeholders&#x27; influence in terms of their previous experience</td></tr><tr><td>EBA</td><td>The level of stakeholders&#x27; educational background</td><td>To measure the influence level of the stakeholders&#x27; educational background</td></tr></table>

c. IA Measurement Criteria (A-MC): This attribute is deduced from the level of the stakeholders' concern with the project success (stakeholders' desire to achieve the project's goals or purpose). Three possible classes of stakeholders are defined in [46,47] on the basis of the stakeholders' interest in any project. The three classes are as follows.

1 Primary stakeholders: This includes beneficiaries who are directly afected by the project and stand to obtain money, services and skills.

2 Secondary stakeholders: This includes stakeholders who are in charge of obtaining the targets of the eforts or beneficiaries. Their jobs or lives might be afected by the results or by obtaining the goals of the project.

3 Key stakeholders: This includes stakeholders who oversee the law, legal and standard regulations and policy that may either conflict with or fulfil the goals of the project.

Four stakeholder interest levels are proposed on the basis of these defined classifications. A new level, namely, the sponsor and project manager level, is introduced to the defined primary stakeholder class in [46,47] because it has a higher interest level than the other stakeholder of the primary stakeholder class [48–50]. Therefore, the four stakeholders' interest levels are structured in this study as follows: a very high stakeholder interest level, a high stakeholder interest level, a medium stakeholder interest level and a low stakeholder interest level. The detailed description of these stakeholder interest levels are as follows.

Table 3  
Demographic analysis of participating experts.

<table><tr><td>Year of experience</td><td>Latest job title</td></tr><tr><td>19 years</td><td>IS Executive Manager</td></tr><tr><td>14 years</td><td>Data and Infrastructure Business Owner</td></tr><tr><td>11 years</td><td>IT Solutions Operation Manager</td></tr><tr><td>12 years</td><td>Information Management Technical Consultant</td></tr><tr><td>26 years</td><td>Information Solutions and Project Manager</td></tr><tr><td>12 years</td><td>Senior System Engineer</td></tr><tr><td>11 years</td><td>Requirements Engineer</td></tr><tr><td>19 years</td><td>Senior System Analyst</td></tr><tr><td>18 years</td><td>Chief Technology Officer</td></tr><tr><td>13 years</td><td>Technical Project Manager</td></tr></table>

1 Very high stakeholder interest level: This level includes only certain beneficiary stakeholders from the primary stakeholders' class. These stakeholders are the sponsors and project managers. They have higher levels of interest in the system project success because their main aim is to ensure that the project is successful in gaining revenue, which can be obtained when the project goals have been achieved [48–50].

2 High stakeholder interest level: This level includes other bene ficiaries of primary stakeholders who aim to obtain services, functions and skills. These stakeholders are users in the role of system development projects [40]. These users are considered functional beneficiaries who define and ultimately use the system's function ality.

3 Medium stakeholder interest level: This level includes the stakeholders of the system development project, excluding the project managers. These stakeholders can include communicators, developers, maintainers, suppliers, support staf and system administrators [40].

4 Low stakeholder interest level: This level includes the key stakeholders who study, protect and prepare the policy and standard regulations that may conflict with or fulfil the projects' goals. These stakeholders are the assessors of the system development projects who oversee the conformance of the system to the legal and stan dard regulations [40].

d. KA Measurement Criteria (KA-MC): The attribute of knowledge is used to measure the impact level of stakeholders' knowledge on the system development process via two attributes, namely, EA and EBA. EA is used to measure the stakeholders' influence with respect to their prior experience. The influence of the stakeholders' years of experience can be measured using the categories introduced in [51] as a consistent worldwide basis to distinguish the various job levels. The categories are as follows:

Category A: 0–1 year of experience

• Category B: 1–3 years of experience

• Category C: 3–5 years of experience

• Category D: 5–8 years of experience

Category E: 8–10 years of experience

• Category F: > 10 years of experience

EBA is the second attribute used to assess the knowledge of stakeholders in terms of their educational level. This assessment is performed on the basis of the International Standard Classification of Education (ISCED 2011) [52], which consists of nine levels (starting from level 0: early childhood education to level 8: doctoral or equivalent). However, only the last five levels of ISCED 2011 (level 5: short-cycle tertiary education, level 6: bachelor or equivalent, level 7: master or equivalent and level 8: doctoral or equivalent) are selected in evaluating the EBA of system stakeholders because levels zero to four are unrelated to this work. A full explanation on the five selected levels of the ISCED is presented in [52].

## 3.1.3. Formulating the StakeQP attribute weight values and measurement criterion values

In the proposed technique, the stakeholders' selection is based on the StakeQP attributes. Hence, calculating the weight value of each proposed attribute and its proposed measurement criteria is essential to identifying the overall SAV. This phase is aimed at gaining the inputs from the industrial experts to formulate the attribute weight values (AWV) for each StakeQP attribute, as well as the measurement criteria value (MCV) for each AMC to measure the SAV. Obtaining the inputs of the values in this phase will assist in reducing the need for direct participation of the experts in SQP in assigning the SPV.

A survey with experts is conducted to obtain the importance values for each defined StakeQP attribute and the proposed measurement criteria. These values will be used in formulating the AWV of each defined StakeQP attribute and the MCV of each proposed measurement criteria for the specified StakeQP attributes, except for the measurement criteria for the EBA and IA. The standard sequence level number of the measurement criteria will be used as the importance values. The policy of expert judgement suggests that the number of experts to be targeted should be at least six in order to obtain quality and robust results [53,54]. In this survey, the participants were comprised of 10 industrial experts. All participating experts have > 10 years of relevant experience in the software development process and software project practices. Table 3 presents the years of experience and the latest job title of each included participating expert.

The survey is structured into two parts and follows the guidelines of the survey construction based on [55]. The first part is conducted to obtain the importance values of each specified StakeQP attribute. The second part is constructed to obtain the importance values of each proposed measurement criteria of the defined StakeQP attributes. The hard copy of the survey is sent to two participants, and the soft copy via email is used to obtain the responses of another eight participants. Each participant is requested to rate the importance weight value using the seven importance levels of the Likert scale.

The description and values of the Likert scale are structured based on [55,56]. A detailed explanation of the steps for formulating the AWV and MCV of the proposed AMC are enumerated as follows.

Fig. 3 shows the process of formulating the AWV of each specified attribute. The process begins by obtaining the importance values of each defined attribute from the conducted survey, where each participating expert assigns an importance value for the seven importance points of the Likert scale to each proposed attribute. Then Eq. (1) is used to find the AWV of each proposed attribute by calculating the mean of the assigned values from the participating experts to each proposed attribute. The AWV values will be in the range of $1 \leq \mathrm { A W V } \leq 7 .$ .where

AWV is a set of the weight values for the selected StakeQP attributes, $A W V = \{ A W V _ { i } \mid i = \mathrm { R I A } , \mathrm { P P A } , \mathrm { I A } , \mathrm { K A } ,$ EDA};

![](/api/attachments/27XXRAWR/fulltext/images/825d8fd3455f94c74c4d1878db44f58e0c0166dcdc861a71e00820ad05605525.jpg)

(1)

Table 4  
AWV of each proposed attribute.

<table><tr><td>Attribute</td><td></td><td>Attributes Weight Value (AWV)</td></tr><tr><td>RIA</td><td></td><td>6.02</td></tr><tr><td>PPA</td><td></td><td>6.09</td></tr><tr><td>IA</td><td></td><td>6.23</td></tr><tr><td rowspan="2">KA</td><td>EA</td><td>5.46</td></tr><tr><td>EBA</td><td>5.39</td></tr></table>

$A W V _ { i }$ is the importance value associated with the $i ^ { \mathrm { { t h } } }$ attribute; $V _ { i , j }$ is the entered value of the $i ^ { \mathrm { { t h } } }$ attribute provided by expert j, where $j = 1 , . . . , \boldsymbol { \mathrm { n ; } }$ and

n is the total number of participating experts.

The result of Eq. (1) is presented in Table 4, which shows the AWV for each attribute that will be used to quantify and prioritise the stakeholder in our proposed technique. A higher attribute weight value indicates a greater influence on SQP. As shown in Table 4, the AWV of IA has the highest weight value (6.23) compared to the other attributes, thereby reflecting its considerable influence on the SQP. This attribute is followed by PPA with an AWV of 6.09, RIA with 6.02, and the subdivided attributes, EA and EBA of the KA, with 5.46 and 5.39, respectively.

Fig. 4 presents the manner in which the MCV is formulated for each proposed AMC. In this study this method is called the MCV calculation method. This calculation process consists of three steps: obtaining the importance values of each measurement criteria, calculating the mean value of the obtained importance values of each measurement criterion and finding the MCV for each AMC. Obtaining the importance value of each measurement criterion is the first step in calculating the MCV of the proposed AMC. The importance value of each measurement criterion of PPA, RIA and KA in terms of EA is obtained by conducting the second part of the survey, in which the participating experts rate the importance value of each measurement criteria for each StakeOP at tribute. The importance value is obtained on the basis of the same seven importance points of the Likert scale that are used in determining the AWV of each proposed attribute.

The standard level numbers of the selected ISCED 2011 levels are used as the importance values for the measurement criteria of KA in terms of EBA, whereas the importance values for the IA's measurement criteria are obtained on the basis of the proposed levels of interest. First, the importance values of each willingness level are obtained by ranking the number of each level. The very high interest level is given the highest ranking number of 4; 3 is given to the high interest level, 2 is assigned as the importance value of the middle interest level, and the low interest level is given the lowest ranking number of 1. Second, the mean value of the obtained importance values for each measurement criterion is calculated using Eq. (2). The next step is to determine the MCV of each AMC using Eq. (3), where the obtained mean value of each attribute's AMC is divided by 7 (the maximum rating scale value) and then multiplied by the AWV of the attribute. This step is essential because it identifies the accurate MCV of the given attribute over the AWV.

$$
M _ {i, k} = \frac {\left(\sum_ {j = 1} ^ {n} P _ {i , k , j}\right)}{n}\tag{2}
$$

where

M is a set of the mean of the considered AMC, $M = \{ M _ { i } \mid i = \mathrm { R I A } \cdot$

MC, PPA-MC, IA-MC, KA-MC};

$M _ { i , k }$ is a set of the importance values associated with the $k ^ { \mathrm { { t h } } }$ measurement criteria of the $i ^ { \mathbf { \hat { t h } } }$ attribute;

$P _ { i , k , j }$ represents the entered value associated with the $k ^ { \mathrm { t h } }$ measurement criteria of the $i ^ { \mathrm { { t h } } }$ attribute provided by expert j, where $j = 1 , . . . ,$ n; and

n is the total number of participating experts.

$$
M C V _ {i, k} = \left(\frac {M _ {i , k}}{7}\right) * A W V _ {i}\tag{3}
$$

where

MCV is a set of measurement criterion values of each considered AMC;

$M C V _ { i , k }$ is the measurement value of the $i ^ { \mathrm { { t h } } }$ attribute for the $k ^ { \mathrm { { t h } } }$ measurement criteria, where $K = 1 , 2 , 3 , . . . , \mathrm { L } .$ K represents the number of measurement criteria associated with the $i ^ { \mathrm { { t h } } }$ attribute;

$M _ { i , k }$ is the mean value of the $k ^ { \mathrm { { t h } } }$ measurement criteria associated with the $i ^ { \mathrm { { t h } } }$ attribute obtained from $\operatorname { E q . }$ (2); and

$A W V _ { i }$ is the importance value associated with the $i ^ { \mathrm { { t h } } }$ attribute in Table 4.

Table 5 presents the results of formulating the measurement criterion value of the StakeQP attributes. The table shows each AMC associated with its obtained MCV. The MCV value refers to the influence value of each AMC that is associated with the stakeholder in calculating the SAV value for the stakeholders. Thus, a high MCV value represents a great influence of the AMC.

The formulated AWV of each StakeQP attribute and the MCV of each AMC are considered to be constant values for this proposed StakeQP technique. The process of formulating the AWV and MCV will not be repeated during the execution of the StakeQP technique for quantifying and prioritising the stakeholders. Additionally, all of the process work of the establishment phase is only performed on the research scope of the proposed StakeQP technique, but not on the implementation scope of the StakeQP in conducting the SQP process. With the proposed AMC and the formulated AWV and MCV, the need for expert participation in evaluating the stakeholder (based on the proposed AMC of each defined StakeQP attribute) will be minimised. The detailed description of utilising the specified StakeQP attributes and their AMC, AWV and MCV in evaluating the stakeholders will be elaborated in Section 3.3.

## 3.2. Stakeholder profile collection

Stakeholders' profiles are an essential input element in the SQP of StakeQP. Thus, the profile of each system stakeholder must be collected. The profile of each stakeholder should be collected finalized attributes and their proposed AMC. Each profile should contain the details of each stakeholder in terms of the stakeholder's educational level, role, position, educational background and years of experience. The collected stakeholders' profiles are used as inputs for quantification and prioritisation. The stakeholders' profiles, the AWV of each proposed attribute, and the MCV of each AMC and stakeholders' profiles are used in the next step of calculating the SPV, which will be critically discussed in the next section (Section 3.3).

## 3.3. Formulating the SPV

This step is conducted to identify the SPV of each stakeholder. SPV presents the priority value of the stakeholders (representing the importance value of a stakeholder), which will be used to prioritise the stakeholders according to their identified SPV. The SPV of each stakeholder is formulated using two main processes: calculating the SAV for each proposed attribute and employing the multi-attribute decision method, namely, TOPSIS. The following sub-sections will provide a full explanation of the execution of these processes.

![](/api/attachments/27XXRAWR/fulltext/images/c3ec3711605087a99698b3f8dc2a6e34aa1aae13d09b07235bd93540dc84919f.jpg)  
Fig. 4. MCV Calculation Method.

Table 5  
MCV of the attribute measurement criteria.

<table><tr><td rowspan="13">RIA-MC</td><td>Stakeholders&#x27; role groups</td><td>MCV</td></tr><tr><td>Acquirers</td><td>5.24</td></tr><tr><td>Assessors</td><td>5.24</td></tr><tr><td>Communicators</td><td>4.70</td></tr><tr><td>Developers</td><td>4.82</td></tr><tr><td>Maintainers</td><td>4.88</td></tr><tr><td>Suppliers</td><td>4.70</td></tr><tr><td>Support staff</td><td>4.76</td></tr><tr><td>System administrators</td><td>4.21</td></tr><tr><td>Testers</td><td>4.64</td></tr><tr><td>Users</td><td>5.36</td></tr><tr><td>Consultant</td><td>4.45</td></tr><tr><td>Expert</td><td>5.30</td></tr><tr><td rowspan="5">PPA-MC</td><td>Position level</td><td>MCV</td></tr><tr><td>Top level</td><td>5.48</td></tr><tr><td>Middle level</td><td>5.72</td></tr><tr><td>Supervisory level</td><td>5.54</td></tr><tr><td>Worker level</td><td>5.30</td></tr><tr><td rowspan="5">IA-MC</td><td>Interest level</td><td>MCV</td></tr><tr><td>Very high interest level</td><td>6.23</td></tr><tr><td>High interest level</td><td>4.67</td></tr><tr><td>Medium interest level</td><td>3.12</td></tr><tr><td>Low interest level</td><td>1.56</td></tr><tr><td rowspan="7">KA in terms of EA-MC</td><td>Standard categories of years of experience</td><td>MCV</td></tr><tr><td>Category A: 0–1 year of experience</td><td>2.46</td></tr><tr><td>Category B: 1–3 years of experience</td><td>3.11</td></tr><tr><td>Category C: 3–5 years of experience</td><td>3.66</td></tr><tr><td>Category D: 5–8 years of experience</td><td>4.15</td></tr><tr><td>Category E: 8–10 years of experience</td><td>4.48</td></tr><tr><td>Category F: &gt;10 years of experience</td><td>4.64</td></tr><tr><td rowspan="5">KA in terms of EBA-MC</td><td>Standard educational level</td><td>MCV</td></tr><tr><td>Short-cycle tertiary education</td><td>3.37</td></tr><tr><td>Bachelor or equivalent</td><td>4.04</td></tr><tr><td>Master or equivalent</td><td>4.72</td></tr><tr><td>Doctoral or equivalent</td><td>5.39</td></tr></table>

## 3.3.1. Calculating the SAV

SAV refers to the degree value of a given stakeholder for each proposed attribute. The SAV of each StakeQP attribute is calculated based on two input elements, namely, the MCV of each AMC and the stakeholders' profiles (formulating the MCV and collecting the stake holders' profiles). The manner in which the SAV is calculated for each stakeholder on the basis of the specified StakeQP attributes with their specified measurement criteria is discussed as follows.

SAV of RIA: Role responsibility is used as a measurement criterion for RIA. Hence, the SAV of this attribute is identified on the basis of the MCV of the role responsibility of stakeholders (s) from the collected stakeholder profile, as shown in Eq. (4).

$$
S A V (R I A) _ {s} = M C V \text {(Stakeholder role responsibility type)} _ {s}\tag{4}
$$

SAV of PPA: The standard position levels are used as measurement criteria for RIA. The SAV of PPA for each stakeholder is calculated on the basis of the MCV of the position level that is associated with each stakeholder (s) from his/her profile. Eq. (5) is used to calculate the SAV of this attribute.

$$
S A V (P P A) _ {s} = M C V \text {(Stakeholder position level)} _ {s}\tag{5}
$$

SAV of IA: Three willingness levels are used as measurement criteria for IA. As a result, the SAV of IA is calculated on the basis of the MCV of each interest level that is associated with stakeholders (s), as shown in Eq. (6).

$$
S A V (I A) _ {s} = M C V \text {(Stakeholder interest level)} _ {s}\tag{6}
$$

SAV of KA: This attribute has two subdivided attributes: EA and EBA. Therefore, the SAV of this attribute is identified on the basis of the SAV of these two attributes, as shown in Eq. (7).

$$
S A V (K A) _ {s} = S A V (E A) _ {s} + S A V (E B A) _ {s}\tag{7}
$$

The EA is measured using standard categories of years of experience. Thus, the MCVs of each standard category of the years of experience that are associated with a stakeholder from his/her profile are used to calculate SAV of EA for stakeholders. Eq. (8) calculates the SAV of this attribute for each stakeholder.

$$
S A V (E A) _ {s} = M C V \text {(Stakeholder category of years of experience)} _ {s}\tag{8}
$$

The MCV of the standard educational levels is used to find the SAV of EBA because the standard educational level is applied as measurement criteria for educational background. Hence, Eq. (9) is used to find the SAV of the educational background of each stakeholder (s). The SAV of the educational background is the MCV associated with the educational background level of the stakeholder (s) retrieved from his profile.

$$
S A V (E B A) _ {s} = M C V \text {(Stakeholder educational level)} _ {s}\tag{9}
$$

3.3.2. Applying the multi-attribute decision-making (MADM) method: TOPSIS

MADM refers to the process of evaluating and ranking the number of alternatives on the basis of multiple defined attributes or criteria [57–60]. Several existing methods have been proposed to conduct the process of MADM [57,58]. One of these existing methods is TOPSIS [59,61,62], which was initially introduced by Hwang and Yoon in 1981 [59]. It is a useful and practical technique that can be used in decision making for selecting and ranking a specified number of alternatives over listed criteria or attributes [59,63].

TOPSIS has the features of simplicity and speed, where the best alternatives can be revealed in a shorter time with a simple computation process compared with other techniques, such as AHP [63,64]. Its output is simple and can be easily understood. Moreover, TOPSIS is executed with certain number of steps, which remain the same regardless of the alternative size and number of attributes [62,63].

With respect to the number of required inputs from the decision makers, TOPSIS does not require as many inputs as the other methods [60,62,65]. The only required input is related to the weight value for each defined attribute to initiate the process [60,62,65]. Therefore, TOPSIS is used to evaluate and rank the stakeholders (represented as alternatives) on the basis of the defined proposed StakeQP attributes. The dificult issue of inputting and estimating the required input of the weights is controlled because the weight value of each StakeQP attribute is provided based on the identified AWV of each StakeQP attribute (Table 4). The fundamental principle of TOPSIS is to determine the best alternative that is closest to the ideal solution and the farthest from the negative ideal solution (NIS) [59,60]. The TOPSIS technique is performed using seven steps, which are explained in detail, as follows.

Step 1: Construct the Decision Matrix: Constructing the decision matrix $D [ x _ { i j } ] _ { m x n } ,$ which is comprised of m alternatives (stakeholders) linked with n attributes (defined SOP attributes) and filled up by the performance ratings of the alternatives of each attribute. Table 6 presents the constructed decision matrix $D [ x _ { i j } ] _ { m x n }$ the information of which is described as follows:

S is a set of alternatives, $S = \{ S _ { i } \mid i = 1 , . . . , m \}$ . This set of alternatives is the set of stakeholders who must be quantified and prioritised.

A is a set of attributes, $A = \{ A _ { j } | j = 1 , . . . , n \}$ . This set of attributes is the set of the specified StakeQP attributes, namely, RIA, IA, PPA, EA of KN and EBA of KN.

X is the set of performance ratings of S, $X = \{ x _ { i j } \mid i = 1 , . . . , \mathrm { m } ; j = 1$ …, $n \}$ , where $x _ { i j }$ is the evaluation of stakeholder $S _ { i }$ with respect to the specified StakeQP attribute $A _ { j }$ . The SAV of each stakeholder is the given value for $x _ { i j } ,$ where each SAV presents the worth of stakeholders on each listed StakeQP attribute.

Table 7  
Table 6 Decision matrix.

<table><tr><td rowspan="3">Alternatives</td><td colspan="5">Attributes (StakeQP attributes)</td></tr><tr><td> $A_j$ </td><td> $A_j$ </td><td> $A_j$ </td><td> $A_j$ </td><td> $A_j$ </td></tr><tr><td> $w_j$ </td><td> $w_j$ </td><td> $w_j$ </td><td> $w_j$ </td><td> $w_j$ </td></tr><tr><td> $S_i$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td></tr><tr><td> $S_i$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td></tr><tr><td> $S_i$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td><td> $x_{ij}$ </td></tr></table>

W is a set of attribute weights, $w = \{ w _ { j } | j = 1 , . . . , n \}$ and is the set of specified StakeQP attribute weights. AWV is calculated on the basis of the importance value of each proposed attribute. Thus, the weight of each StakeQP attribute is provided based on the value of AWV of each proposed attribute shown in Table 4. Therefore, the AWV of each proposed attribute is its weight value $( 1 \leq \mathrm { A W V } \leq 7 )$ .

Step 2: Construct the Normalised Decision Matrix: The decision matrix is then constructed by normalising the obtained decision matrix from Step 1. This step is performed to transform the various attribute dimensions into non-dimensional attributes to allow for a comparison across the specified StakeQP attributes. The decision matrix is normalised using Eq. (10). Table 7 presents the constructed normalised decision matrix.

$$
r _ {i j} = \frac {x _ {i j}}{\sqrt {\sum_ {j = 1} ^ {n} x _ {i j} ^ {2}}}, i = 1, \dots , m. a n d. j = 1, \dots , n\tag{10}
$$

where

$r _ { i j }$ is the normalised score of a stakeholder; and

$x _ { i j }$ is the original score performance rating of the stakeholder in the previous decision matrix in Table 6.

Step 3: Construct the Weighted Normalised Decision Matrix: The weighted normalised decision matrix is obtained by multiplying each r normalised score with its corresponding attribute weight, as shown in Eq. (11). Table 8 presents the constructed weighted normalised decision matrix.

$$
v _ {i j} = r _ {i j} * w _ {j}\tag{11}
$$

where

w is the weight of the specified StakeQP attribute;

$\nu _ { i j }$ is the obtained weighted normalised score of the stakeholders; and

$r _ { i j }$ is the normalised score of the stakeholders obtained from Step 2. Step 4: Identify the Positive Ideal Solution (PIS) and the NIS: The PIS is identified as a composite of the best weighted normalised scores exhibited by any stakeholder (in the weighted normalised decision matrix) for each StakeQP attribute, as shown in Eq. (12). Meanwhile, a composite of the worst weighted normalised scores of any stakeholder for each attribute is identified as the NIS, as shown in Eq. (13).

Normalised decision matrix.

<table><tr><td rowspan="3">Alternatives</td><td colspan="5">Attributes (StakeQP attributes)</td></tr><tr><td> $A_j$ </td><td> $A_j$ </td><td> $A_j$ </td><td> $A_j$ </td><td> $A_j$ </td></tr><tr><td> $w_j$ </td><td> $w_j$ </td><td> $w_j$ </td><td> $w_j$ </td><td> $w_j$ </td></tr><tr><td> $S_i$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td></tr><tr><td> $S_i$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td></tr><tr><td> $S_i$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td><td> $r_{ij}$ </td></tr></table>

Table 8  
Weighted normalised decision matrix.

<table><tr><td rowspan="3">Alternatives</td><td colspan="5">Attributes (StakeQP Attributes)</td></tr><tr><td> $A_j$ </td><td> $A_j$ </td><td> $A_j$ </td><td> $A_j$ </td><td> $A_j$ </td></tr><tr><td> $w_j$ </td><td> $w_j$ </td><td> $w_j$ </td><td> $w_j$ </td><td> $w_j$ </td></tr><tr><td> $S_i$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td></tr><tr><td> $S_i$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td></tr><tr><td> $S_i$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td><td> $v_{ij}$ </td></tr></table>

$$
P I S = \{v _ {1} ^ {*}, v _ {2} ^ {*},..., v _ {n} ^ {*} \}, w h e r e v ^ {*} = \{(m a x _ {i} (v _ {i j}) i f j \in J) \}
$$

$$
N I S = \{v _ {1} ^ {\prime}, v _ {2} ^ {\prime},..., v _ {n} ^ {\prime} \}, w h e r e v ^ {\prime} = \{(m i n _ {i} (v _ {i j}) i f j \in J) \}\tag{12}
$$

(13)

Step 5: Calculate the Separation Measure for Each Alternative (Stakeholder): This step is aimed at calculating the individual separation measures of each stakeholder from the PIS and NIS. The separation measures are calculated using the Euclidean distance. Eqs. (14) and (15) are executed to determine the separation measures of each stakeholder (alternative) from the PIS and NIS, respectively. S<sup>⁎</sup> and $s ^ { \prime }$ are donated for the obtained separation value of each stakeholder from the PIS and NIS, respectively.

$$
S _ {i} ^ {*} = \left[ \sum_ {j = 1} ^ {n} (v _ {i j} - v _ {i} ^ {*}) ^ {2} \right] ^ {1 / 2}, i = 1, \dots , m\tag{14}
$$

$$
S _ {i} ^ {\prime} = \left[ \sum_ {j = 1} ^ {n} (v _ {i j} - v _ {i} ^ {\prime}) ^ {2} \right] ^ {1 / 2}, i = 1, \dots , m
$$

where

(15)

S<sup>⁎</sup> and S′ represent the obtained separation values of each stake holder from the PIS and NIS, respectively.

Step 6: Find the Ideal Stakeholders by Calculating the Relative Closeness Coeficient (RC ) and the Relative Closeness to the PIS: The relative closeness of the $i ^ { \mathrm { { t h } } }$ stakeholder to the PIS is defined in Eq. (16).

$$
R C _ {i} = \frac {S _ {i} ^ {\prime}}{(S _ {i} ^ {*} + S _ {i} ^ {\prime})} 0 \leq R C _ {i} \leq 1\tag{16}
$$

where

$R C _ { i }$ is the relative closeness value (SPV) of the $i ^ { \mathrm { { t h } } }$ stakeholder to the IPS, which is between 0 and 1.

Step 7: Rank the Stakeholders: Finally, the set of stakeholders is ranked according to the descending order of their relative closeness $R C _ { i }$ (SPV ). The highest $S P V _ { i }$ value indicates that more important stakeholders such as $S _ { i }$ are to be considered in the system development process.

## 4. StakeQP-AIT

The StakeQP-AIT is constructed with a .NET environment using HTML for the graphical user interface (GUI), a Microsoft SQL Server database for efective data management and execution and the C# programming language to execute the proposed StakeQP. The AWV of each StakeQP attribute and the MCV of each proposed AMC are stored in the constructed database. The proposed attributes and their measurement criteria, AWV and MCV, are identified and formulated in the establishment phase of this StakeQP technique. Fig. 5 presents the phases of implementing the StakeQP technique using the StakeQP-AIT, which consists of two main components: the GUI and automation en gine. The two components include two phases, namely, the pre-requisite phase and the quantifying and prioritising phase. The pre-requisite input is essential for the other phases. Thus, it must be conducted prior to the implementation of other phases of the StakeQP AIT. The quantifying and prioritising phase includes sub-steps and the presentation of the results. These phases are detailed as follows.

![](/api/attachments/27XXRAWR/fulltext/images/25aa297be58ad479ab1397bc5f25ebfbf09ab1074c1854408617d7dc0ad7fb08.jpg)  
Fig. 5. StakeQP-AIT implementation structure

1. Phase 1: Pre-requisite Input. Collecting and storing the stakeholders' profiles. The stakeholder profiles must be collected on the basis of the proposed measurement criteria of each SQP attribute of this technique. Each stakeholder profile contains the details of each stakeholder, such as positional power, interest, years of experience, educational level and role influence. The identification process of these details is conducted based on the defined measurement cri teria of each StakeQP attribute (Section 3.1.2). Then, these col lected stakeholder profiles must be stored in the database by in putting or uploading via the developed GUI of the StakeQP-AIT tool. These stakeholder profiles are then used as an input to quantify and prioritise the stakeholders in the next phase of the implementation guidelines.

2. Phase 2: Quantifying and Prioritising Processes. This phase includes the steps of quantifying and prioritising the stakeholders of the StakeQP. The StakeQP-AIT tool is used by calculating the SPV of each stakeholder and displaying the result using three automated steps, as follows.

2.1 Automated Calculation of SAV. The SAV of each stakeholder is calculated using the automated tools of the technique. The stakeholder profiles and the specified MCV of each attribute are retrieved from the database and used as inputs to calculate the SAV of each stakeholder. The details of this calculation process have been

described in Section 3.3.1.

2.2 Automated Execution of TOPSIS. The obtained SAV of each stakeholder from the previous step and the AWV of each attribute are used as inputs for the TOPSIS algorithm, which is executed automatically via the developed automation tools to identify the SPV of each stakeholder. The prioritised list of stakeholders is produced on the basis of the identified SPV.

2.3 Presentation of the Result. The prioritised list of stakeholders and their identified SPV are displayed on the GUI of the StakeQP-AIT.

With these clear implementation steps of the semi-automated StakeQP-AIT, the implementer can perform SQP with minimal expert participation in order to initiate, absorb and implement the process. The implementer only needs to input the stakeholder profiles, such as their power position level, educational background, years of experience and their role in the system development project. Then the SPV is ob tained through automated implementation based on the two sub-automated processes, namely, the automated calculation of SAV for each stakeholder and applying the automated TOPSIS method that will produce the final order list of the SPV for each system stakeholder.

## 5. Experimental study

This section presents the evaluation of the proposed StakeQP performance. The StakeQP technique is proposed to quantify and prioritise the stakeholders with the capability of addressing the key issues of the SQP domain in terms of time consumption, lack of automation level and low-level implementation details, the need for expert participation in executing the SQP process and the absence of the measurement criteria for assessing the stakeholders' influence. Evaluating the StakeQP by implementing and testing its performance with an actual industrial project is essential to confirm its capability of solving the specified issues. The empirical experiment is selected as an evaluation method for the StakeQP technique, and the RALIC benchmark dataset is used to evaluate its performance. To the best of our knowledge, the dataset of RALIC is the only available and complete dataset in the SQP domain. In comparison with other case studies, the RALIC dataset includes detailed information of the stakeholder profiles and the actual results for the priority ranks of the RALIC stakeholders. Thus, this dataset is used in evaluating the SQP techniques, such as in [22,23]. Hence, this project can be used in the evaluation, and the results can be compared with those of existing techniques. Moreover, RALIC is a large-scale software project used as replacement access, library and ID card project [22,23]. It was developed to improve the existing access control system by combining the photo ID card, access card and library card at University College London. A total of 85 relevant stakeholders from the RALIC documentation reports must be quantified and prioritised [22,23].

Table 9  
Sample of the RALIC stakeholder profiles.

<table><tr><td>Stakeholder ID</td><td>Stakeholder role group</td><td>Education level</td><td>Category of years of experience</td><td>Stakeholder positional level</td><td>Stakeholder interest level</td></tr><tr><td>SID0234</td><td>Developers</td><td>6: Bachelor or Equivalent</td><td>C</td><td>Middle</td><td>Medium Interest</td></tr><tr><td>SID3010</td><td>Users</td><td>5: Short-cycle Tertiary Education</td><td>B</td><td>Worker</td><td>High Interest</td></tr><tr><td>SID7234</td><td>System administrators</td><td>6: Bachelor or Equivalent</td><td>C</td><td>Supervisory</td><td>Medium Interest</td></tr></table>

Table 9 presents a sample of the RALIC stakeholders' profiles based on the defined measurement criteria of each StakeQP attribute. The documentation reports of the selected RALIC project are provided in the RALIC dataset and the thesis of Lim [22,23]. The experiment is con ducted with 85 stakeholders of the RALIC benchmark dataset.

The experimental implementation of the proposed StakeQP tech nique is performed on the basis of the specified steps of StakeQP-AIT presented in Section 4. A desktop computer with 3.60 GHz, 16 GB RAM and the Microsoft Visual Studio 2010 full-package programme installed is used to run the experiment using the developed StakeQP-AIT tool. Table 10 shows the experimental results and presents the list of the prioritised and quantified stakeholders. The results show the list of stakeholders, including the stakeholder rank, stakeholder ID and the obtained SPV for each stakeholder. The SPV of each stakeholder is in the range of 0 to 1 (0 ≤ SPV ≤ 1) after normalising the steps of TOPSIS. However, the evaluation and the performance analysis will be discussed and highlighted in detail in the next section.

## 6. Performance analysis and result evaluation

StakeQP is proposed in order to provide the prioritised list of stakeholders and solve certain issues of the existing SQP techniques. Thus, the evaluation performance of the StakeQP is based on these parameters. The accuracy of StakeQP is also measured for a comparison with existing techniques. Time consumption is measured by the time consumed when executing the SQP process to produce the prioritised list of stakeholders on the basis of the generated SPV of stakeholders. The lack of an automation level is concerned with the capability of StakeQP to provide an automated SQP process, whereas the insuficient low-level implementation details are concerned with providing in suficient low-level implementation details for SQP. The need for highly professional human intervention is concerned with the capability of the StakeQP to generate results with minimal expert involvement. In ad dition, nine existing techniques are selected for comparison with the performance of the proposed StakeQP based on the defined evaluation parameters. These existing techniques are derived from the study in [4], where they have been identified as available techniques that focused on the SQP process compared with other stakeholder analysis techniques. These techniques include the works of Razali and Anwar [28], Bendjenna et al. [33], Babar et al. (Star Triangle [35], bi-metric [30] and StakeMeter [18]), the AHP method [31–33], Ballejos and Montagna [34], Lim et al.-StakeNet [22], and McManus [29].

Table 10  
Sample of the StakeQP experimental results.

<table><tr><td>Rank</td><td>Stakeholder ID</td><td>SPV</td></tr><tr><td>1</td><td>SID3007</td><td>0.9142</td></tr><tr><td>2</td><td>SID9024</td><td>0.8987</td></tr><tr><td>3</td><td>SID3002</td><td>0.8564</td></tr></table>

The eficiency of StakeQP is measured with respect to the time consumed in SQP. The StakeQP took 6.25 s to produce the prioritised list of 85 stakeholders from the RALIC dataset with their SPV. This response time is better that the other existing techniques that take 23–58 h to quantify and prioritise 63 stakeholders [18]. Table 11 shows the comparative analysis of StakeQP with four SQP techniques based on the time consumption for the total number of stakeholders and the usage process type of the technique in terms of the automation level in conducting the SQP process. These four techniques are evaluated in terms of the time consumption and compared with other listed SQP techniques and one of these five techniques. Lim et al. introduced StakeNet [22] using the same dataset (RALIC) as the present study in the evaluation process.

The performance evaluation of the methods of Ballejos and Montagna and Babar et al. (bi-metric and StakeMeter) in terms of time consumption is reported based on the recent study of Babar et al. in [18], where these three techniques are implemented with diferent numbers of stakeholders. The Babar et al.-StakeMeter took 7, 23 and 47 h to prioritise 23, 63 and 47 stakeholders, respectively, and the efficiency of this technique is higher than the other two techniques. The time consumption performance of the Lim et al.-StakeNet technique by Lim et al. is reported in [22]. The Lim et al.-StakeNet [22] technique took 17 h to quantify and prioritise 85 RALIC stakeholders. Evidently, the StakeQP consumes less time compared with the other existing techniques at 6.25 s for 85 stakeholders. Fig. 6 shows the improvement percentage in terms of the time consumption of the proposed StakeQP with respect to each of the selected existing techniques. The improvement percentage is measured on the basis of the lowest time consumption by each technique in Table 11. The lowest time consumption of the techniques of Ballejos and Montagna, Babar et al. (bi-metric and StakeMeter) and Lim et al. (StakeNet) is 28, 11, 7 and 17 h for prioritising 15, 8, 13 and 85 stakeholders, respectively. The time consumption of StakeQP in prioritising 85 stakeholders is 6.25 s. Eq. (17) is

## Table 11

Comparative analysis of StakeQP with existing techniques based on time consumption.

<table><tr><td>No.</td><td>Technique</td><td>Stakeholders</td><td>Time consumption</td><td>Techniques&#x27; process types</td></tr><tr><td rowspan="3">1.</td><td rowspan="3">Ballejos and Montagna [34] [18]</td><td>15</td><td>28 h</td><td rowspan="3">Manual</td></tr><tr><td>46</td><td>58 h</td></tr><tr><td>53</td><td>108 h</td></tr><tr><td rowspan="3">2.</td><td rowspan="3">Babar et al.-bi-metric [30] [18]</td><td>8</td><td>11 h</td><td rowspan="3">Manual</td></tr><tr><td>22</td><td>31 h</td></tr><tr><td>13</td><td>65 h</td></tr><tr><td rowspan="3">3.</td><td rowspan="3">Babar et al.-StakeMeter [18]</td><td>13</td><td>7 h</td><td rowspan="3">Manual</td></tr><tr><td>32</td><td>23 h</td></tr><tr><td>21</td><td>47 h</td></tr><tr><td>4.</td><td>Lim et al.-StakeNet [22]</td><td>85</td><td>17 h</td><td>Manual</td></tr><tr><td>5.</td><td>Proposed StakeQP</td><td>85</td><td>6.25 s</td><td>Semi-automated</td></tr></table>

![](/api/attachments/27XXRAWR/fulltext/images/01d03cfcc11f4db844f7de4928b90f07df4d12a6121b49167231b375d76ea3e9.jpg)  
Fig. 6. Performance analysis of StakeQP with respect to time consumption.

used to calculate the improvement percentage. It is a basic and well known equation for finding the improvement percentage of the performance testing for a technique or firm [66–70].

$$
P I M _ {i} = \frac {T S - T E _ {i}}{T E _ {i}} \times 1 0 0\tag{17}
$$

where

PIM is the percentage improvement of the StakeQP technique against the $i ^ { \mathrm { { t h } } }$ existing technique;

TE<sub>i</sub> is the lowest time consumption of the $i ^ { \mathrm { { t h } } }$ existing technique; TS is the time consumption of the proposed StakeQP technique.

Fig. 6 also shows that the time consumption eficiency of StakeQP is 99.94%, 99.84%, 99.75% and 99.90% better than that of Ballejos and Montagna, Babar et al. (bi-metric and StakeMeter) and Lim et al.-StakeNet, respectively. Moreover, the average performance of the StakeQP against all selected techniques indicates that its performance is better than the existing techniques in terms of the time consumption at a percentage of 99.86%, although the number of stakeholders prioritised in StakeQP (85 stakeholders) is larger than that in other existing techniques.

The StakeQP can automate SQP with less time consumption while producing the prioritised list of stakeholders with minimal expert participation by using clear implementation details with the proposed AMC, TOPSIS and the developed StakeQP-AIT tool. However, the selected existing techniques consume a large amount of time, given that these techniques executed their processes manually with expert involvement, thereby providing highly abstract information of the implementation details and not presenting any standard AMC for identifying the stakeholder priority. Moreover, the StakeQP technique proposed the AMC and the MCV of each proposed measurement criteria in its initial step. Thus, the proposed technique can solve the issue related to the absence of AMC in the existing techniques. Most of the existing techniques proposed only the attributes without providing their measurement criteria, depending on expert involvement. Hence, the stakeholders are evaluated by providing their weight value without defining the standard measurement criteria. The defined AMC and their identified MCV are combined to measure the SAV of each stakeholder, which is then used with the listed StakeQP attributes with their specified AWV, employing the TOPSIS algorithm to calculate the SPV and produce the ranked list of stakeholders. The StakeQP-AIT tool is used to solve the major issue of the existing techniques that require the involvement of professionals to quantify and prioritise the stakeholders. Thus, the result is generated in the experimental implementation by conducting all of the StakeQP steps automatically without expert participation.

Additionally, the accuracy of the StakeQP is measured by comparing the produced stakeholders' prioritised list against that of the ground truth, which is derived from the project documentation and given in [22,23]. Hence, accuracy is the intersection between the stakeholders priority rank in the StakeQP list and their actual priority rank in the ground truth list [22,23]. The statistical measure of the Pearson correlation coeficient is used to find the degree of correlation (intersection) between the two lists. It is the best method of measuring the association between two variables because it is based on the covariance method [71]. The correlation coeficient value (r) ranges from +1 to $^ { - 1 , }$ , where +1, −1 and 0 indicate a perfect positive correlation, perfect negative correlation and no correlation, respectively. The interpretation of the correlation coeficient value is (r), where each range of the correlation coeficient with its associated degree of correlation is provided in [71,72]. To calculate the correlation coeficient value (r) between the two lists, the Pearson correlation coeficient formula is used, as shown in Eq. (18). The obtained result is 0.8969 (89.69%), which is a positive correlation with a very strong positive degree of correlation (based on the interpretation of the correlation coeficients in [71,72]). Thus, the high X stakeholder rank in StakeQP indicates a high Y stakeholder rank in the ground truth, and vice versa.

$$
r = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) (y _ {i} - \overline {{y}})}{\sqrt {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} \sum_ {i = 1} ^ {n} (y _ {i} - \overline {{y}}) ^ {2}}}\tag{18}
$$

where

r is the correlation coeficient value;

n is the number of samples, which are the stakeholders in each list (both lists consist of 85 stakeholders);

$X _ { i }$ is the rank of the $i ^ { t h }$ stakeholder in the StakeQP list; and

$Y _ { i }$ is the rank of the $i ^ { t h }$ stakeholder in the ground truth.

Fig. 7 presents the percentage of the accuracy performance of the proposed StakeQP compared with the Lim et al.-StakeNet technique by Lim et al. [22]. Lim et al.-StakeNet [22] is the only technique that has been evaluated in terms of accuracy, which is measured on the basis of the final ranking of each stakeholder using the same dataset (RALIC). Although the performance evaluation of the accuracy for the Ballejos and Montagna and Babar et al. (bi-metric and StakeMeter) techniques was conducted and reported by Babar et al. in [18], these techniques are not selected for comparison because their reported accuracies were measured based on the selection of critical stakeholders rather than the stakeholder ranking values. Thus, they cannot be directly compared with the proposed StakeQP accuracy performance. Fig. 7 evidently shows that the eficiency of StakeQP is higher than that of the Lim et al.- StakeNet. The accuracy result of StakeQP is 89.69%, whereas that of Lim et al.-StakeNet is 78.00%.

Furthermore, Table 12 presents a comparative analysis of the proposed StakeQP technique with all existing techniques based on the other defined evaluation parameters as follows: low-level implementation details (guidelines), reduced expert involvement, automation tools for SQP and the existence of the AMC for measuring the priority degree of the stakeholders and the clearly defined stakeholder priorities by producing a ranked list of the stakeholders. The results of the comparative analysis reveal that the proposed technique (StakeQP) can handle the key SQP issues, whereas most existing techniques cannot suficiently provide support to various considered key parameters. Lim et al.-StakeNet and Babar et al.-StakeMeter are better techniques that can support fewer key parameters compared to other existing techniques because they focus on providing support to two key issues, namely, guidelines and defining the stakeholder priorities. However, these techniques overlook handling the key issues of automation tools, AMC, and heavily rely on expert participation given that these techniques perform their processes manually without providing the AMC of the attribute, thereby heavily relying on the participation of experts in conducting the SQP. Moreover, the StakeQP-AIT was developed and used by practitioners of software in actual industries. The evaluation parameters of the performance analysis indicate that StakeQP is better than the existing techniques and can be beneficial in actual SQP prac tice.

![](/api/attachments/27XXRAWR/fulltext/images/53ea35049c84f301d671ca08a4a9496df09c0685cfad1a88453c923433568dca.jpg)  
Fig. 7. Accuracy performance of StakeQP.

Table 12  
Comparative analysis of StakeQP with diferent existing techniques.

<table><tr><td>Technique</td><td>AMC</td><td>Guidelines</td><td>Automation tools</td><td>Not requiring the involvement of professional expertise</td><td>Defined stakeholders&#x27; priority list</td></tr><tr><td>Proposed StakeQP</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Razali and Anwar [18,28]</td><td>✗</td><td>Partial</td><td>✗</td><td>✗</td><td>✗</td></tr><tr><td>Bendjenna et al. [18,33]</td><td>✗</td><td>Partial</td><td>✗</td><td>✗</td><td>Partial</td></tr><tr><td>Babar et al.&#x27;s-Star Triangle [18,35]</td><td>✗</td><td>Partial</td><td>✗</td><td>✗</td><td>Partial</td></tr><tr><td>AHP method [31-33]</td><td>✗</td><td>Partial</td><td>✗</td><td>✗</td><td>Partial</td></tr><tr><td>Babar et al.-Bi-metric [30]</td><td>✗</td><td>Partial</td><td>✗</td><td>✗</td><td>✓</td></tr><tr><td>Ballejos and Montagna [18,34]</td><td>✗</td><td>✓</td><td>✗</td><td>✗</td><td>Partial</td></tr><tr><td>Lim et al.-StakeNet [18,22]</td><td>✗</td><td>✓</td><td>✗</td><td>✗</td><td>✓</td></tr><tr><td>Babar et al.- StakeMeter [18]</td><td>✗</td><td>✓</td><td>✗</td><td>✗</td><td>✓</td></tr><tr><td>McManus [18,29]</td><td>✗</td><td>Partial</td><td>✗</td><td>✗</td><td>✗</td></tr></table>

## 7. StakeQP managerial contributions

With respect to the managerial side, StakeQP has a various number of contributions. As revealed from the literature, the existing SQP techniques fall short of providing the AMC for each attribute used for measuring the stakeholder impacts. Thus, new AMC are proposed in this research for each attribute used in quantifying and prioritising the stakeholders. The description and implementation of these proposed AMC are also provided. The proposed AMC is one of the first measurement criteria that can be used by the project manager to assess the stakeholder impact according to the SOP attributes in the SOP domain. Another contribution of the StakeQP to the SQP managerial side is related to the formulation of AWV for each finalized StakeQP attribute and the MCV for each AMC. With the usage of the formulated AWV and MCV along with the automation process of the StakeQP in identifying the SPV of each stakeholder, the project manager can assess the stakeholders' impacts by measuring the degree value of a given stakeholder for each StakeQP attribute and prioritising them without being heavily reliant on expert involvement. As a result, StakeQP can also assist the projects managers in achieving the cost-savings benefits by saving the cost resources of the project that are usually located fo hiring the experts to participate in conducting the SQP process.

Additionally, with the automation, fast speed and low implementation details features of StakeQP, the project managers can perform SQP in a proper and eficient way in the industrial and academic sectors without requiring considerable amount of efort (such as a tedious manual process, the necessity of the experts' participation, possible human errors in the manual process, time and efort workloads). Furthermore, the ability of StakeQP in producing better accu racy results than alternative techniques in identifying the core stakeholders with their SPV value can enable the project managers to reveal stakeholders with high levels of impact on the project outcomes and give high priority to these stakeholders at the outset of the project development process. This will consequently lead the project managers to establishing an efective planning strategy for maximising the benefits of the organisations based on the most influential stakeholders, which induce winning support from most of the specified stakeholders, bringing more potential resources during the project development and increasing the possibility of producing a successful project. Utilising this technique and its automation tools, the organisation can obtain a direction towards the core stakeholders and assist decision makers in shaping up the project direction and anticipating reactions from the stakeholders concerning the development of the project. Eventually, with the existence of such a StakeQP technique, the software system project will have a lower possibility of failure due to the participation of the inadequate stakeholder, an omission of the core requirements, biased prioritisation results and a time constraint.

## 8. Threats to validity

An empirical study can face various threats to validity [73]. In the context of this study, we identify a few threats that may be associated with our experiment, and substantial eforts are undertaken to decrease such threats.

The selection of a benchmark dataset represents the first essential threat due to the lack of available benchmark datasets in the SQP domain (this can include detailed information of the stakeholders' profile as essential inputs in the proposed StakeOP). given that SOP is the forthcoming research direction in stakeholder analysis. To address this threat, we select a benchmark dataset of an actual software project (RALIC), which is a well-known benchmark dataset in the domain of SQP and RP. RALIC is the only available and complete benchmark dataset in terms of providing detailed information on the stakeholder profiles for the proposed StakeQP. However, this dataset initially lacks details on the educational level and years of experience of the stakeholders. These missing details are necessary to cover the educational background and years of experience. The missing details are then obtained from the owner of the dataset by providing the range of the educational level and the years of experience of the stakeholders. Although the RALIC benchmark dataset is derived from the documentation of the RALIC software project, we cannot guarantee that this benchmark dataset represents the actual stakeholder details.

In addition, the performance comparison with other existing techniques poses a threat. Few techniques have been proposed for SQP [4,18]. However, not all techniques have been implemented and eval uated due to the ambiguity and complexity associated with the SQP and because of the unavailability of experts [4,18]. Thus, we cannot compare the proposed StakeQP technique with all available techniques. To eliminate this threat, we select recently published studies [18,22] that present the most recent and the best results for the related SQP techniques and measure the defined evaluation parameters in this study. Another essential threat is related to the time consumption of each selected technique. To compare the time consumption fairly, implementing and using all the techniques in the same environment is essential. However, this is dificult because the existing techniques are performed manually. To minimise this threat, we conduct a perfor mance comparison of the time consumption of four existing techniques that can be implemented in actual scenarios with less time consumption [18,22]. These techniques (Babar et al.'s bi-metric and StakeMeter, Ballejos and Montagna's and Lim et al.'s StakeNet) perform their SQP processes manually, as reported in their published works. Thus, we cannot implement them with automated tools compared to the proposed StakeQP, which provides a semi-automated SQP process.

Another threat is related to the automation process issues. The au tomation process, although timesaving and with minimal to no human intervention, may elicit an issue of producing an unpredictable processing error or a low quality result where the implementer has not uploaded the stakeholder's profile based on the StakeQP attributes and their AMC. The reason is that the automated machine cannot execute a flexible variety of tasks, as it is restricted to execute the task based on what it has been programmed to do. Similarly, the StakeQP automation process is executed in the full process of evaluating the stakeholders based on the finalized attributes and their proposed AMC with inability of completing the process if the stakeholder profile has been uploaded based on diferent attributes or measurements. To minimise this issue, we precisely explained the full process of the StakeQP attributes and the AMC in order to assist the implementer in specifying the profiles of the stakeholders based on the attributes and their AMC. Hence, we strongly recommended that the implementer carefully read the provided explanation. However, there is one threat here that is associated with the unknown costs that will be required to the keep the processes of the StakeQP-AIT updated because the cost disbursed in updating with a new procedure will demand high operational costs with respect to the research and development requirements to be performed.

## 9. Conclusion and future work

Stakeholder selection plays a key role in eliciting and identifying the core requirements that need to be developed to satisfy the stakeholders requirements. Thus, various techniques have been proposed for SQP. In this study, a new semi-automated SQP technique called StakeQP and a new AMC were proposed to address the limitations of the existing SQP, such as its excessive reliance on expert intervention, its time con sumption caused by a lack of automation and unclear guidelines of the existing techniques, its ambiguity in terms of performing the SQP process and a lack of standard measurement criteria for the attributes used to identify the SPV. The proposed StakeQP technique provides low-level implementation details of the SQP process using the TOPSIS method based on the StakeQP attributes and their measurement criteria, which are identified and proposed for SQP. To evaluate the per formance of the StakeQP technique, an actual software project called RALIC was used by applying StakeQP, and a comparative analysis with other techniques was performed based on the defined evaluation criteria. The findings demonstrate that StakeQP can generate more accurate results with less time utilisation and is more efective in handling the defined SQP limitations compared with the other alternative techniques.

Even though StakeQP has proven itself in achieving a good performance in the evaluation part, the study still has some limitations that lead to a strong need to extend this work. In this research, the proposed StakeQP has been applied to a large real software project (RALIC benchmark dataset). However, with limited resources and other constraints in accessing other benchmark datasets that can be used in the SQP domain, we could not apply the proposed technique with other projects datasets. Thus, we call for further research to extend the implication of the proposed StakeQP with diferent project datasets. Additionally, so far the StakeQP is implicated in performing the SQP with 85 stakeholders. However, the StakeQP technique is suggested for implementation with larger projects that contain hundreds or thousands of stakeholders. Its application in larger projects can assist in better assessments of the StakeQP with respect to the scalability issue, which is related to its capability in handling a large number of stakeholders. There is also the need to implement the StakeQP in global software projects practices for better applicability.

Additionally, future research can dig deeper in improving the StakeQP performance with respect to catering the stakeholder classifications and is considered to be an important aspect in the process of the stakeholder analysis [6,19]. The final output of the StakeQP process is a ranked list of stakeholders based on the defined SPV values without classifying the ranked stakeholders in diferent categories, such as the “most important stakeholders”, “medially important stakeholders” and “less important stakeholders”. Hence, the next phase is to enhance the robustness of the StakeQP in terms of classifying the stakeholders. This improvement can be achieved by employing the classification algorithms of supervised or unsupervised learning, which will make StakeQP be an intelligent support decision solution in quantifying and prioritising the stakeholders with the ability of categorising these stakeholders on the basis of their defined SPV values.

## Acknowledgment

The authors appreciate the efforts of the Ministry of Educatior Malaysia, University Malaysia Pahang (UMP) and Ministry of Higher Education Yemen for supporting this research. This work is supported in part by the Fundamental Research Grant: A New Model for Automated Stakeholder Quantification and Prioritization Based on User Needs for Software System Development from the Ministry of Education Malaysia under Grant RDU190164 and the PGRS170393 Grant from UMP. The authors also give special thanks to Professor Soo Ling Lim for her kind support in providing the benchmark dataset for this work.

## Appendix A. Details of measurement criteria

Table 2  
Detailed description of RIA-MC, and PPA-MC.

<table><tr><td colspan="2">RIA-MC</td></tr><tr><td>Stakeholders&#x27; role group</td><td>Description</td></tr><tr><td>Acquirers</td><td>Oversee the system&#x27;s procurement in the development process of system project; acquirers frequently represent the business sponsors, senior executives from the technology groups, marketing and sales. When the system project requires funding from the external investment, the investors can also act as acquirers.</td></tr><tr><td>Assessors</td><td>Oversee the conformance of the system to legal and standard regulation.</td></tr><tr><td>Communicators</td><td>Describe the system to other stakeholders using training materials and documentation.</td></tr><tr><td>Developers</td><td>Perform the system contraction and deployment from its specification (or lead the teams, which perform this construction and development process).</td></tr><tr><td>Maintainers</td><td>Handle the system evaluation once it is in use or ready to be used.</td></tr><tr><td>Suppliers</td><td>Supply and/or construct the software, hardware or infrastructure, where the system will function.</td></tr></table>

(continued on next page)

Table 2 (continued)

<table><tr><td colspan="2">RIA-MC</td></tr><tr><td>Stakeholders&#x27; role group</td><td>Description</td></tr><tr><td>Support Staff</td><td>Related to staff who provides support to users of the product or system.</td></tr><tr><td>System Administrators</td><td>Execute the system once deployed.</td></tr><tr><td>Testers</td><td>Test the developed system to ensure that the system is convenient to be used.</td></tr><tr><td>Users (Functional Beneficiary)</td><td>Specify the functionality of the system and ultimately make use of it.</td></tr><tr><td>Consultant</td><td>Consultant acts more within mission, where standard solutions fit the forecasted project.</td></tr><tr><td>Expert</td><td>Intervenes mainly in unusual situations and operates a relatively new panel of knowledge.</td></tr><tr><td colspan="2">PPA-MC</td></tr><tr><td>Position level</td><td>Description</td></tr><tr><td>Top Level</td><td>This level includes decisive people for directing and leading other people&#x27;s efforts towards achieving success. It comprises chairman, vice president, president, board of directors, general manager, managing director, chief financial officer, chief operating officer and chief executive officer. The managers (people) of this group have the maximum level of authority.</td></tr><tr><td>Middle Level</td><td>This level comprises departmental heads, such as purchasing department head, sales department head, marketing manager, finance manager, plant superintendent and executive officer. People in this level are in charge of implementing the policies and plans structured by the top level. They also practice the roles of the top level for their associated department as they structure policies and plans for their department. They collect and organise the resources based on the defined policies and plans of the top level.</td></tr><tr><td>Supervisory Level</td><td>This level comprises superintendent, supervisors, sub-department executives, foreman and clerk. Managers of this level have limited authority; they work to execute the defined activities of the plan constructed by the previous two levels (top- and middle-position levels). They pass on the instruction to the workers and report to the middle level management. They are in charge of preserving discipline between the workers.</td></tr><tr><td>Worker Level</td><td>Those who do not hold any managerial position</td></tr></table>

## References

[1] F. Gomariz-Castillo, I. Garrigós, J.-A. Aguilar, J. Zubcof, S. Casteleyn, J.-N. Mazón, Evaluating diferent i\*-based approaches for selecting functional requirements while balancing and optimizing non-functional requirements: a controlled experiment, Information and Software Technology 106 (2019) 68–84, https://doi.org/10. 1016/i,infsof,2018.09.004.

[2] L. Alawneh. Requirements prioritization using hierarchical dependencies. Inf. Technol. - New Gener, 2018, pp. 459–464, , https://doi.org/10.1007/978-3-319- 54978-1.

[3] N. Misaghian, H. Motameni, An approach for requirements prioritization based on tensor decomposition, Requirements Engineering 23 (2018) 169–188, https://doi. org/10.1007/s00766-016-0262-6.

[4] F. Hujainah, R.B. Abu Bakar, B. Al-haimi, M.A. Abdulgabber, Stakeholder quantification and prioritisation research: a systematic literature review, Information and Software Technology 102 (2018) 85–99, https://doi.org/10.1016/j.infsof.2018.05. 008.

[5] Y. Zhao, A Systematic Stakeholder Selection Model in Requirements Elicitation fo Software Projects: A Systematic Mapping Study, Blekinge Institute of Technology, SE-371 79 Karlskrona, Sweden, 2018.

[6] S. Zedan, W. Miller, Quantifying stakeholders' influence on energy eficiency of housing: development and application of a four-step methodology, Construction Management and Economics 36 (2018) 375–393. https://doi,org/10.1080 01446193.2017.1411599.

[7] M. Sadiq, A fuzzy set-based approach for the prioritization of stakeholders on the basis of the importance of software requirements. IETE Journal of Research 63 (2017) 616–629, https://doi.org/10.1080/03772063.2017.1313140.

[8] Standish Group, CHAOS Report 2015, (2015).

[9] Standish Group, Modern Resolution of All Software Project From 2011–2015, (2015).

[10] M.I. Babar, M. Ghazali, D.N.A. Jawawi, Risk based decision support system for stakeholder quantification for value based, Journal of Theoretical and Applied Information Technology 76 (2015) 373–385.

[11] F. Hujainah, R.B.A. Bakar, B. Al-Haimi, M.A. Abdulgabber, Investigation of stake holder analysis in requirement prioritization techniques, Advanced Science Letters 24 (2018) 7227–7231

[12] J. Colazo, Performance implications of stage-wise lead user participation in software development problem solving, Decision Support Systems 67 (2014) 100–108, https://doi.org/10.1016/j.dss.2014.08.007.

[13] F. Huiainah, R.B.A. Bakar, M.A. Abdulgabber, K.Z, Zamli, Software requirements prioritisation: a systematic literature review on significance, stakeholders, techniques and challenges, IEEE Access 6 (2018) 71497–71523, https://doi.org/10.1109 ACCESS.2018.2881755.

[14] F. Hujainah, R.B. Abu Bakar, B. Al-Haimi, A.B. Nasser, Analyzing requirement prioritization techniques based on the used aspects, Research Journal of Applied Sciences. 11 (2016) 327–332, https://doi.org/10.3923/riasci.2016.327.332.

[15] R.A. Ribeiro, A.M. Moreira, P. Van Den Broek, A. Pimentel, Hybrid assessment method for software engineering decisions, Decision Support Systems 51 (2011) 208–219. https://doi org/10.1016/i dss 2010.12.009

[16] A. Elsaid, R. Salem, H.A.- Kader, A dynamic stakeholder classification and prioritization based on hybrid rough-fuzzy method, J. Softw. Eng. 11 (2017) 143–159,

https://doi.org/10.3923/jse.2017.143.159.

[17] K. Mascena, A. Fischmann, J. Boaventura, Stakeholder prioritization in Brazilian companies disclosing GRI reports, Brazilian Bus. Rev. 15 (2018) 17–32, https://doi org/10.15728/bbr.2018.15.1.2.

[18] M.I. Babar, M. Ghazali, D.N.A. Jawawi, K. Bin Zaheer, StakeMeter: value-based stakeholder identification and quantification framework for value-based software systems, PLoS One 10 (2015) 1–33, https://doi.org/10.1371/journal.pone. 0121344

[19] J. Lehtinen, K. Aaltonen, R. Rajala, Stakeholder management in complex product systems: practices and rationales for engagement and disengagement, Industrial Marketing Management (2018) 1–13, https://doi.org/10.1016/j.indmarman.2018. 08.011.

[20] A.B. Carroll, J.A. Brown, A.K. Buchholtz, Business & Society: Ethics, Sustainability, and Stakeholder Management, 10th ed., Cengage Learning, Boston, MA, 2018 United States

[21] Y. Li, J. O'Donnell, R. García-Castro, S. Vega-Sánchez, Identifying stakeholders and key performance indicators for district and building energy performance analysis, Energy and Buildings 155 (2017) 1–15. https://doi,org/10.1016/i,enbuild.2017. 09.003.

[22] S.L. Lim, D. Quercia, A. Finkelstein, StakeNet: using social networks to analyse the stakeholders of large-scale software proiects. Proc. 32nd ACM/IEEE Int. Conf. Softw. Eng, - ICSE '10. 2010. p. 295. . https://doi,org/10.1145/1806799.1806844

[23] S. Lim, Social Networks and Collaborative Filtering for Large-scale Requirements Elicitation, University of New South Wales, Sydney, Austrailia, 2010http:/ discovery.ucl.ac.uk/1329883/

[24] R.E. Freeman, Strategic Management: A Stakeholder Approach, Pitman, Boston, 1984.

[25] T. Donaldson, L.E.E.E. Preston, The stakeholder theory of the corporation: concepts, evidence, and implications, Academy of Management 20 (1995) 65–91, https://doi. org/10.1007/sll205-006-9069-z

[26] A.A.A. Majoch. A.G.F. Hoepner, T. Hebb, Sources of stakeholder salience in the responsible investment movement : why do investors sign the principles for responsible investment? Journal of Business Ethics 140 (2017) 723–741. https://doi org/10.1007/s10551-016-3057-2.

[27] R.E. Freeman, Strategic Management: A Stakeholder Approach, Cambridge university press. 2010

[28] R. Razali, F. Anwar, Selecting the right stakeholders for requirements elicitation: a systematic approach, Journal of Theoretical and Applied Information Technology 33 (2011) 250–257.

[29] J. McManus, A stakeholder perspective within software engineering projects, Eng. Manag. Conf. 2004. Proceedings. 2004 IEEE Int, 2004, pp. 880–884, , https://doi. org/10.1109/IEMC.2004.1407508.

[30] M.I. Babar, M. Ghazali, D.N.A. Jawawi, A bi-metric and fuzzy c-means based intelligent stakeholder quantification system for value-based software, Front. Artif. Intell. Appl, 2014, pp. 295–309, , https://doi.org/10.3233/978-1-61499-434-3- 295.

[31] I. Brito, A. Moreira, Towards a composition process for aspect-oriented require ments, Early Asp. Work. AOSD Conf., Boston, MA, USA, 2003, pp. 1–6 http://www. cs.bilkent.edutr/AOSD-EarlvAspects/Papers/BritoMoreira.pdf

[32] P. Voola, A.V. Babu, Requirements uncertainty prioritization approach: a novel approach for requirements prioritization, Softw. Eng. Int. J. 2 (2012) 37–49.

[33] H. Bendjenna, P. Charre, N. Eddine Zarour, Using multi-criteria analysis to prioritize stakeholders, Journal of Systems and Information Technology 14 (2012) 264–280.https://doi.org/10.1108/13287261211255365

[34] L.C. Ballejos, J.M. Montagna, Modeling stakeholders for information systems design processes, Requirements Engineering 16 (2011) 281–296, https://doi.org/10.1007/ s00766-011-0123-2.

[35] M.I. Babar, M. Ghazali, D.N.A. Jawawi, Software quality enhancement for value based systems through stakeholders quantification, Journal of Theoretical and Applied Information Technology 55 (2013) 359–371 http://www.scopus.com/ inward/record.url?eid=2-s2.0-84884830773&partnerID=40&md5= 588ef36ee435d2a197513afb21d13370.

[36] L.C. Ballejos, S.M. Gonnet, J.M. Montagna, A stakeholder model for interorganizational information systems, Requir. Eng. Found. Softw. Qual. 4542 (2007) 247–261, https://doi.org/10.1007/978-3-540-73031-6.

[37] M.I. Babar, M. Ghazali, D.N. a Jawawi, A. Elsa, Stakeholder management in value based software development: systematic review, IET Software 8 (2014) 219–231, https://doi.org/10.1049/iet-sen.2013.0216.

[38] ISO, IEC, IEEE, International Standard ISO/IEC/IEEE Systems and Software Engineering — Engineering, 2011 (2011) (doi:IEEESTD.2011.6129467).

[39] IEEE-SA Standards Board, IEEE Recommended Practice for Architectural Description of Software-intensive Systems, 1471–2000 IEEE Std, 2000, pp. 1–23, https://doi.org/10.1109/IEEESTD.2000.91944.

[40] N. Rozanski, E. Woods, Software Systems Architecture: Working With Stakeholder Using Viewpoints and Perspectives, second, Addison-Wesley Professional, 2012, https://doi.org/10.1017/CB09781107415324.004

[41] F. Creplet, O. Dupouet, F. Kern, B. Mehmanpazir, F. Munier, Consultants and experts in management consulting firms. Research Policy 30 (2001) 1517–1535. https://doi.org/10.1016/S0048-7333(01)00165-2.

[42] A.J. DuBrin, Essentials of Management, Cengage Learning, https://books.google. com.my/books?id=dNThzoekGQcC, (2008).

[43] K.C. Laudon, J.P. Laudon, Management Information Systems: Managing the Digital Firm, Pearson Education, 2017, https://books.google.com.my/books?id= oBISDgAAQBAJ.

[44] M.J. Austin, K. Hopkins, Supervision as Collaboration in the Human Services: Building a Learning Culture, SAGE Publications, 2004, https://books.google.com. my/books?id=s2fZiivwKoIC.

[45] B. Chatteriee, Human Resource Management - A Contemporary Text: Economics. Commerce & Management, Sterling Publishers Pvt. Ltd, n.d. https://books.google com.my/books?id=g4weAgAAQBAJ.

[46] P. Rabinowitz, Section 8. Identifying and Analyzing Stakeholders and Their Interests. (2015)

[47] P.K. Sengupta, Industrial Water Resource Management, Challenges and Opportunities for Eficient Water Stewardship, Wiley-Blackwell, 2017.

[48] A. Mendelow, Stakeholder mapping, in: Proc. 2nd Int. Conf. Inf. Syst. (Cambridge, MA (Cited Sch., 1991)).

[49] S.T. Demir, D.J. Bryde, D.J. Fearon, E.G. Ochieng, Three dimensional stakeholder analysis - 3dSA: adding the risk dimension for stakeholder analysis, Int. J. Proj. Organ. Manag. 7 (2015) 15–30, https://doi.org/10.1504/IJPOM.2015.068002.

[50] W. Support, Y. Projects, Stakeholder Management, (2015).

[51] W.W. Worldwide, Level Guides, Position Descriptions and Global Grades, (2017).

[52] UNESCO, International Standard Classification of Education, http://uis.unesco.org/ sites/default/files/documents/international-standard-classification-of-educationisced-2011-en,pdf. (2012).

[53] M. Almaliki. F. Fanivi. R. Bahsoon. K. Phalp. R. Ali, Requirements-driven socia adaptation: expert survey, in: C. Salinesi, I. van de Weerd (Eds.), Requir. Eng. Found. Softw. Qual. Springer International Publishing, Switzerland, 2014, pp. 72–87.

[54] R. Cooke, K.N. Probst, Highlights of the expert judgment policy symposium and technical workshop. Resour. Futur. DC. (2006) 31 http://rff,org/Documents Conference-Summary.pdf.

[55] J. Lin, S.M. Sulaman, R.M. de Mello. H. Martin, Guidelines for Conducting Surveys in Software Engineering v. 1.1. (2015)

[56] W.M. Vagias, Likert-type scale response anchors, Clemson Int. Inst. Tour. Res. Dev. Dep. Park. Recreat. Tour. Manag. Clemson Univ. (2006), https://scholar.google. com/scholar?hl=en&as\_sdt=0%2C5&q=W.M.+Vagias%2C+Likert-type+scale +response+anchors%2C+Clemson+Int.+Inst.+Tour.+Res.+Dev.+Dep. + Park + Recreat + Tour + Manag + Clemson + Univ + 2006 &btnG =

[57] A. Mattiussi, M. Rosano, P. Simeoni, A decision support system for sustainable energy supply combining multi-objective and multi-attribute analysis: an Australian case study, Decision Support Systems 57 (2014) 150–159, https://doi.org/10.1016 i dss 2013.08 013

[58] A.A. Zaidan, B.B. Zaidan, M. Hussain, A.M. Al-Haiqi, M.L. Mat Kiah, M. Abdulnabi, Multi-criteria analysis for OS-EMR software selection problem: a comparative study, Decision Support Systems 78 (2015) 15–27, https://doi.org/10.1016/j.dss.2015.07. 002.

[59] G.-H. Tzeng, J.-J. Huang, Multiple Attribute Decision Making Methods and Applications, Chapman and Hall/CRC, 2011.

[60] A. Ishizaka, P. Nemery, Multi-criteria Decision Analysis Methods, Wiley, 2013

[61] M. Behzadian, S. Khanmohammadi Otaghsara, M. Yazdani, J. Ignatius, A state-of the-art survey of TOPSIS applications, Expert Systems with Applications 39 (2012) 13051–13069, https://doi.org/10.1016/j.eswa.2012.05.056.

[62] M. Velasquez, P.T. Hester, An analysis of multi-criteria decision making methods,

Int. J. Oper. Res. 10 (2013) 56–66.

[63] H.S. Shih, H.J. Shyur, E.S. Lee, An extension of TOPSIS for group decision making, Mathematical and Computer Modelling 45 (2007) 801–813, https://doi.org/10. 1016/i.mcm.2006.03.023

[64] C. Parkan, M.L. Wu, On the equivalence of operational performance measurement and multiple attribute decision making, International Journal of Production Research 35 (1997) 2963–2988, https://doi.org/10.1080/002075497194246.

[65] D.L. Olson, Comparison of weights in TOPSIS models, Mathematical and Compute Modelling 40 (2004) 721–727, https://doi.org/10.1016/j.mcm.2004.10.003.

[66] D. De Angelis, Y. Grinstein, Relative performance evaluation in CEO compensation: evidence from the 2006 disclosure rules, Johnson Sch. Res. Pap. Ser. (2011) 39–2010, https://doi.org/10.2139/ssrn.1710386.

[67] M.I. Babar, Framework for Stakeholder Quantification and Requirements Prioritization for Value-based Software Development, PhD's Thesis Fac. Comput., Universiti Teknol. Malavsia. Malaysia. 2015

[68] M.I. Babar, M. Ghazali, D.N.A. Jawawi, S.M. Shamsuddin, N. Ibrahim, PHandler: an expert system for a scalable software requirements prioritization process, Knowledge-Based Syst. 84 (2015) 179–202, https://doi.org/10.1016/j.knosys. 2015.04.010.

[69] F.M. Tice, Explicit Relative Performance Evaluation and Managerial Decision making: Evidence From Firm Performance and Investments, https://papers.ssrn com/abstract= 2645956. (2017)

[70] G. Gong, L.Y. Li, J.Y. Shin, Relative performance evaluation and related peer groups in executive compensation contracts relative performance evaluation and related peer groups in executive compensation contracts, The Accounting Review (2010) https://doi.org/10.2308/accr.00000042 forthcoming.

[711 J.D. Evans. Straightforward Statistics for the Behavioral Sciences. Brooks/Cole Pub Co, 1996 August 2, 1995.

[72] A.K. Chowdhury, A. Debsarkar, S. Chakrabarty, Novel methods for assessing urban air quality: combined air and noise pollution approach, J. Atmos. Pollut. 3 (2015) 1–8, https://doi.org/10.12691/jap-3-1-1.

[73] C. Wohlin, P. Runeson, M. Höst, M.C. Ohlsson, B. Regnell, A. Wesslén, Experimentation in Software Engineering, Springer-Verlag, Berlin Heidelberg, 2012.

![](/api/attachments/27XXRAWR/fulltext/images/536897d9718b6bbdcfbedad271a699fecd361f69c3e75684deac0e5ca7468b3a.jpg)  
Fadhl Hujainah received the B.Sc. degree (Hons.) in computer science and software engineering and the M.Sc. degree (Hons.) in information technology from the Universiti Teknologi Malaysia, Johor Bahru. Malaysia, in 2012 and 2013, respectively. He is currently pursuing the Ph.D. degree with the Faculty of Computer Systems and Software Engineering, University Malaysia Pahang, Kuantan Malaysia His research interests include software engineering with particular interest in requirements prior itization and stakeholder analysis.

![](/api/attachments/27XXRAWR/fulltext/images/8d800f298121a34326e47ca981271369998cf166d5b6a437cf32d2dbf58f0aff.jpg)

Rohani Binti Abu Bakar received the B.Sc. degree in computer science from Universiti Teknologi Malaysia, Johor Bahru, Malaysia; the M.Sc. degree in computer science from Universiti Malaya, Kuala Lumpur, Malaysia; and the Dr. Eng. degree in DNA computing and its applications from Waseda University, Kitakyushu, Japan. She is currently an Associate Professor with the Faculty of Computer Systems and Software Engineering, University Malaysia Pahang. Kuantan. Malaysia. Her research interests include software engineering, and soft computing.

![](/api/attachments/27XXRAWR/fulltext/images/74c62cd15bf47a2da53d26442e20752a88cb1f883f72afde3e8931651f64a191.jpg)

Mansoor Abdullateef Abdulgabber received the B.C.A degree (First Division) from Osmania University, Hyderabad, India, the M.Sc. degree in real-time software engineering from the Universiti Teknologi Malaysia, Kuala Lumpur, Malaysia, and the Ph.D. degree in software testing and semantic technology from the Universiti Malava, Kuala Lumpur. Malaysia. He is a specialist in the area of software engineering and a certified Project Manager, as well as a fellow with the American Academy of Project Management. He has been in the industry for over 10 vears, He is currently an Assistant Professor with the University of Prince Mugrin. Madinah. Saudi Arabia. He is highly professional, passionate, and fo cused in what he does and wishes to accomplish. His research interests include software engineering
