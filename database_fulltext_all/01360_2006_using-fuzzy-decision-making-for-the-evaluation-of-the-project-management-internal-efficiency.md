---
otero_id: 1360
otero_key: "RSUSNRAQ"
title: "Using fuzzy decision making for the evaluation of the project management internal efficiency"
authors: "F.T. Dweiri; M.M. Kablan"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.04.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using fuzzy decision making for the evaluation of the project management internal efficiency

F.T. Dweiri <sup>a</sup>, M.M. Kablan <sup>b,\*</sup>

<sup>a</sup>Industrial Engineering Department, Jordan University of Science and Technology, Irbid, Jordan <sup>b</sup>Engineering College, Mutah University, P. O. Box 7, Mutah, Alkarak, Jordan

Available online 23 May 2005

## Abstract

Specific applications of fuzzy logic in project management are relatively few in comparison to other application areas. The criteria of project cost, project time, and project quality may be considered as project management internal measures of efficiency. The objective of this research is to present an approach that employs fuzzy decision making (FDM) to combine these three measures into one measure namely the project management internal efficiency (PMIE) which should represent an overall estimate of how well the project was managed and executed. The proposed approach for the evaluation of PMIE is illustrated on a case study. A fuzzy decision making system is designed and implemented using the MATLAB software for the evaluation of the PMIE. The methodology and procedure proposed in this research may be easily implemented by project management organizations. The evaluation of PMIE can serve for project managers and for project organizations as an indicator for the level of achievement of the project management internal objectives. PMIE may help in the evaluation of the performance of project teams. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Cost; Time; Quality; Project management internal measures of efficiency; Fuzzy decision making system; Fuzzy sets

## 1. Introduction

Effective management of projects is crucial for the development and survival of any economy because development is about growth and growth is about a series of successfully managed projects [4]. A project may be viewed as <sup>b</sup>the entire process required to produce a new product, new plant, new system, or other specific results<sup>Q</sup> [1]. In this fiercely competitive world, project organizations are forced to look for scientific tools that assist them in the evaluation of their projects. The project management team is responsible for producing the project output and hence the project management team must be constantly aware of the project goal, project purpose, and the project management internal measures of efficiency. Project effectiveness, which is a synonym of project success, is measured or assessed in terms of the degree of achievement of project objectives [2,3]. The concept of project success is a controversial concept. The Project Management Institute devoted its Annual Seminars and Symposium in 1986 to this topic. Many authors tried to study project success factors and attempted to measure the project success [2,5,8,14,17,21–23]. Lin and Walker, [14], point out that the concept of project success remains ambiguously defined. Many studies considered that the factors of project time, project cost, and project quality are the essential factors for project success. Wideman, [23], emphasizes that customer satisfaction should be considered as a major factor of project success. Baccarini, [2], makes a fine distinction between the following three important concepts related to project success:

<sup>!</sup> Project management success: This deals with the project process from its start to its handover to the client. The focus here is on short-term criteria concentrating on meeting time, budget and quality objectives, and the satisfaction of the project process stakeholders who are in this case the client, and the project team.

<sup>!</sup> Product success: This deals with the effects of the project’s final product at the post-project stage. However, the focus here is on the long-term criteria concentrating on meeting the project owner’s strategic organizational objectives (profitability, market share, and technology advancement) and the satisfaction of the needs of the product-user, i.e., fitness for use. The stakeholders at this stage are the users of the product and the project owner.

<sup>!</sup> Project success: This is a combination of project management success and the product success. It should be pointed out here that some projects can meet the project management success criteria of cost, time, and quality and still they are product failures. Conversely, some projects don’t meet the project management success criteria but they are product success.

Project management success can contribute positively toward product success but it doesn’t guarantee it. In general it should be strived to achieve the project management success and the product success.

The criteria of project cost (PC), project time (PT), and project quality (PQ) are viewed by Shenhar et al. [21] and Baccarini [2] as project management internal measures of efficiency. It may be useful to combine these measures into one measure to get an overall judgement about how well the project was managed and executed. However, the problem is that the three measures are of different dimensions. This problem can be overcome by measuring PC in terms of cost overrun underrun as a percentage of the planned budget, measuring PT as a percentage of the planned duration, and measuring PQ as percentage conforming to functional and technical specifications. However, questions like the following may arise: When does a project have low, medium, or high cost overrun/underrun? When does a project have low, medium, or high schedule overrun/ underrun? This is a vague problem, and we may adhere in this case to expert’s subjective value judgement. Fuzzy logic is a problem solving technique that was introduced by Zadeh [28] to deal with vague or imprecise problems. Fuzzy decision making system (FDMS) in general uses a collection of fuzzy membership functions and decision rules that are solicited from experts in the field to reason about data.

The objective of this research is to present an approach that utilizes a fuzzy decision making system (FDMS) to quantify the Project Management Internal Efficiency (PMIE). The evaluation of PMIE can serve for project managers and for project organizations as an indicator for the level of achievement of the project management internal objectives. PMIE may help in the evaluation of the performance of project teams.

## 2. An overview of the proposed approach

As mentioned above, the objective of this research is to combine the measures of project cost (PC), project time (PT), and project quality (PQ) into a single measure that may be called the project management internal efficiency (PMIE). These three measures have different priorities with respect to the management of the project organization. Hence, for the evaluation of the PMIE we must take in consideration an additional set of variables, namely: Project cost weighting factor (PCWF), Project time weighting factor (PTWF), and Project quality weighting factor (PQWF), and we require that:

$$
\mathrm{PCWF} + \mathrm{PTWF} + \mathrm{PQWF} = 1\tag{1}
$$

Now it is reasonable to assume that the value of PMIE can be determined from the aggregation of the following three impacts:

1) The combined impact of PC and its weighting factor PCWF on PMIE.

![](/api/attachments/RSUSNRAQ/fulltext/images/ec93293e030bfe081683d4ddca5d466aa68b864d0f1c31f5cbf27bdcded0d4a8.jpg)  
Fig. 1. Membership functions of monthly income (MI).

2) The combined impact of PT and its weighting factor PTWF on PMIE.

3) The combined impact of PQ and its weighting factor PQWF on PMIE.

In addition, we should make sure that PC, PT, and PQ are dimensionless. When the project is completed, project cost for example might be measured in terms of cost overrun or cost underrun as a percentage of the planned budget, and PCWF can be assigned a value between 0 and 1 according to the preference of the management of the project organization. Hence, the combined impact of PC and PCWF on PMIE might be evaluated, for example, according to a fuzzy decision rule like the following:

If PC is Very Low (VL) and PCWF is High (H) then PMIE is Very High (VH).

However, the boundaries of Very High, High, Medium, and Low of any decision variable are determined by experts of the project organization. The other two combined impacts can be evaluated in a similar fashion. A fuzzy decision making system is a scientific tool that can be used to handle such a problem. This suggests that, it may be useful for a project organization to integrate experts’ knowledge and experience in a FDMS that can be used for the evaluation of PMIE. The development of such a fuzzy decision making system is easily implemented using the MATLAB software. MATLAB is a menudriven software that allows the implementation of fuzzy constructs like membership functions and a database of decision rules. The software is easy to use and it is user friendly. The management of the project organization can then access the FDMS at the completion of any project and enter values for PC,

PT, PQ, PCWF, PTWF, and PQWF and get as an output a value for the project management internal efficiency (PMIE). The details of the implementation of the proposed approach will be explained in the following sections.

The next section of the paper presents an introduction to fuzzy logic and fuzzy set theory (FST). Section 4 provides a discussion of the fuzzy decision making system (FDMS). Section 5 provides an outline of how fuzzy decision making (FDM) can be used for the evaluation of PMIE. In Section 6, the application of fuzzy decision making for the assessment of PMIE is illustrated via a case study and the design and implementation of a FDMS using the MATLAB software is outlined. Finally, summery and conclusions of the paper are presented in the last Section.

## 3. Introduction to fuzzy logic and fuzzy set theory

Fuzzy logic is a problem solving methodology that provides a simple way of definite conclusions

![](/api/attachments/RSUSNRAQ/fulltext/images/c86c4582934b995a213a173f9aa406fd8d1e25fa97408be099199592f2e34697.jpg)  
Fig. 2. A framework that represents the interrelationships among the components comprising a fuzzy decision making system (FDMS).

![](/api/attachments/RSUSNRAQ/fulltext/images/ee705920438b6eee885079d33e612ac82dd42c27a52f780f6ac6bb44b48c14f7.jpg)  
Fig. 3. A hierarchy structure for the prioritization of the factors: project cost, project time, and project quality.

from vague and imprecise information. Fuzzy set theory was first introduced by Zadeh in 1965. He was motivated by observing that human reasoning can utilize concepts and knowledge that don’t have well-defined boundaries [25]. Fuzzy set theory (FST) is a generalization of the ordinary set theory.

A fuzzy set is a set whose elements belong to the set with some degree of membership l. Consider for example the fuzzification of the variable monthly income (MI) that is illustrated in Fig. 1. The variable is fuzzified into two fuzzy subsets namely Low and High. An income value of \$2500, for example, belongs to the fuzzy subset Low with the membership value of 0.25, and it belongs to the fuzzy subset High with the membership value of 0.75. Using the Max rule, i.e., the fuzzy union operator, then MI = 2500 belongs to the fuzzy subset High with the membership value of 0.75. The fuzzy subsets Low and High are also called labels or linguistic values of the linguistic variable MI in the universe of discourse U = [0, 4000]. The variable MI is called a linguistic variable because its possible values are only Low or High which are words in natural language, while numerical variables use numbers as values [6,26].

In general, a fuzzy set F in a universe of discourse U is characterized by a membership function $\mu _ { \mathrm { F } }$ that takes values in the interval [0,1], i.e., $\mu _ { \mathrm { { F } } } \colon U \longrightarrow [ 0 , 1 ]$ . Hence, the fuzzy set F in U can be represented as a set of ordered pairs of a generic element u and its degree of membership function as the following [13,20]:

![](/api/attachments/RSUSNRAQ/fulltext/images/9842acf3fba14925eb36490e826b2313f786e5683790145ce8ff1ceafc4264be.jpg)  
Fig. 4. Expert choice output for the priorities of the alternatives.

![](/api/attachments/RSUSNRAQ/fulltext/images/2723102060c652cddd04a15ee187d1f3504fecb9e81818c3d927be34e439881b.jpg)  
Fig. 5. The intended fuzzy decision making system (FDMS).

$$
F = \{(u, \mu_ {F} (u)), u \in U \}\tag{2}
$$

The probability that u belongs to F is the membership function $\mu _ { F } ( u )$

If A and B are two fuzzy subsets of U and if $\mu _ { A } ( x )$ is the degree of membership of x in A and $\mu _ { B } ( x )$ the degree of membership of x in B then the fuzzy union set and the fuzzy intersection set are defined according to the following [20]:

Table 1  
If–then rules of PC and its weighting factor (PCWF)

<table><tr><td rowspan="2">PMIE</td><td rowspan="2"></td><td colspan="5">PC</td></tr><tr><td>VL</td><td>L</td><td>M</td><td>H</td><td>VH</td></tr><tr><td rowspan="3">PCWF</td><td>L</td><td>H</td><td>M</td><td>M</td><td>L</td><td>L</td></tr><tr><td>M</td><td>VH</td><td>H</td><td>M</td><td>L</td><td>VL</td></tr><tr><td>H</td><td>VH</td><td>VH</td><td>H</td><td>VL</td><td>VL</td></tr></table>

$A \cup B = \{ x , \operatorname* { m a x } ( \mu _ { A } ( x ) , \mu _ { B } ( x ) ) | x$ gis an element of U

ð3Þ

$$
A \cap B = \{x, \min (\mu_ {A} (x), \mu_ {B} (x)) | x \text {   is   an   element   of   } U \}\tag{4}
$$

For more detailed discussion of the mathematics of FST, the reader is referred to [13,20,28]. Although fuzzy logic covers a wide range of theories and techniques, it is mainly based on four concepts: fuzzy sets, linguistic variables, possibility distributions (membership functions), and fuzzy if–then rules [25]. The values of a linguistic variable are both quantitatively and qualitatively described by a fuzzy set. Possibility distributions or membership functions are constraints on the value of a linguistic variable imposed by assigning it a fuzzy set. Fuzzy if–then rules is a knowledge representation scheme for describing a functional mapping between antecedents and consequences. Fuzzy if–then rules is important for most industrial applications of fuzzy logic including many fuzzy logic control systems.

Table 2  
If–then rules of PT and its weighting factor (PTWF)

<table><tr><td rowspan="2">PMIE</td><td rowspan="2"></td><td colspan="5">PT</td></tr><tr><td>VL</td><td>L</td><td>M</td><td>H</td><td>VH</td></tr><tr><td rowspan="3">PTWF</td><td>L</td><td>H</td><td>M</td><td>M</td><td>L</td><td>L</td></tr><tr><td>M</td><td>VH</td><td>H</td><td>M</td><td>L</td><td>VL</td></tr><tr><td>H</td><td>VH</td><td>VH</td><td>H</td><td>VL</td><td>VL</td></tr></table>

If–then rules of PQ and its weighting factor (PQWF)

<table><tr><td rowspan="2">PMIE</td><td rowspan="2"></td><td colspan="5">PQ</td></tr><tr><td>VL</td><td>L</td><td>M</td><td>H</td><td>VH</td></tr><tr><td rowspan="3">PQWF</td><td>L</td><td>VL</td><td>VL</td><td>L</td><td>L</td><td>L</td></tr><tr><td>M</td><td>M</td><td>M</td><td>M</td><td>H</td><td>H</td></tr><tr><td>H</td><td>H</td><td>H</td><td>VH</td><td>VH</td><td>VH</td></tr></table>

Fuzzy control was first used by Mamadani [15]. Fuzzy controllers are among the important applications of fuzzy set theory. Expert knowledge in terms of linguistic variables and fuzzy if–then rules is used to describe the system. A fuzzy rule usually has a form similar to the following:

If a is Low and b is Medium then c is High. Where Low, Medium, and High are linguistic values of the linguistic variables a, b, and c in the universe of discourse U, V, and W, respectively.

Fuzzy set theory has been applied in many areas of engineering and management [6,12,18,24]. The focus of this paper is on the use of fuzzy decision making system on the assessment of the management internal efficiency of a project.

## 4. Fuzzy decision making system

A fuzzy decision making system (FDMS) is comprised of four main components: a fuzzification interface, a knowledge base, decision making logic, and a defuzzification interface [6,13]. In essence, a FDMS is a fuzzy expert system (FES). Fuzzy expert systems are oriented towards numerical processing where conventional expert systems are mainly symbolic reasoning engines [11,24,27]. Fig. 2 provides a framework for the interrelationships between the components that constitute a fuzzy decision making system (FDMS).The four components are explained as in the following:

![](/api/attachments/RSUSNRAQ/fulltext/images/915ab049feb1a91086d02da5464030d316dc7290e98af2c6ad28c26f506a84f0.jpg)  
Fig. 6. Membership functions of project cost (PC).

1. The fuzzification interface: It measures the values of the input variables on their membership functions to determine the degree of truth for each rule premise.

2. The knowledge base: It comprises experts’ knowledge of the application domain and the decision rules that govern the relationships between inputs and outputs. The membership functions of inputs and outputs are designed by experts based on their knowledge of the system and experience.

3. The decision making logic (DML): It is similar to simulating human decision making in inferring fuzzy control actions based on the rules of inference in fuzzy logic. The evaluation of a rule is based on computing the truth value of its premise part and applying it to its conclusion part. This results in assigning one fuzzy subset to each output variable of the rule. In Min Inferencing the entire strength of the rule is considered as the minimum membership value of the input variables’ membership values [16].

$$
\mu_ {\text { Output }} = \min \left\{\mu_ {\text { Input1 }}, \mu_ {\text { Input2 }}, \dots , \mu_ {\text { InputN }} \right\}\tag{5}
$$

A rule is said to <sup>b</sup>fire<sup>Q</sup>, if the degree of truth of the premise part of the rule is not zero.

4. The defuzzification interface: It converts a fuzzy control action ( a fuzzy output) into a nonfuzzy control action (a crisp output). The most common used method in defuzzification is the center of area method (COA). The COA method computes the crisp value as the weighted average of a fuzzy set. The result of applying the COA defuzzification method to a fuzzy conclusion <sup>b</sup>u is $F ^ { \ast }$ can be expressed according to the following formula [25]:

![](/api/attachments/RSUSNRAQ/fulltext/images/6defb4bab3705fc2ac0136347db05f3f1859d0be5d603149d1e8417688d3eab2.jpg)  
Fig. 7. Membership functions of project time (PT).

$$
u _ {0} = \frac {\sum_ {i} \mu_ {F} (u _ {i}) \times u _ {i}}{\sum_ {i} \mu_ {F} (u _ {i})}\tag{6}
$$

where $u _ { i }$ is the representative value of the fuzzy subset member i of the output, and $\mu _ { F } ( u _ { i } )$ is the confidence in that member (membership value) and $u _ { 0 }$ is the crisp value of the output. In this research, we use FDM to evaluate PMIE in a similar fashion to the applications of FDM in the facilities layout problem given in Ref. [6], and in the part-machine grouping problem given in Ref. [10].

## 5. Fuzzy decision making for the evaluation of PMIE

PMIE is a vague or uncertain quantity. Fuzzy logic is initially introduced to deal with fuzzy or ill-defined problems. To use fuzzy decision making for the evaluation of the project management internal efficiency the following procedure is proposed:

<sup>!</sup> Find all factors that affect the PMIE. According to our approach we have the following factors that affect the evaluation of PMIE: PC, PT, and PQ and their corresponding priorities PCWF, PTWF, and PQWF.

<sup>!</sup> Develop fuzzy subsets and membership functions for each of the input variables and for the output variable PMIE using expert’s knowledge and experience.

<sup>!</sup> Determine decision rules: Expert’s knowledge and experience is used here for the development of IF– THEN rules that govern the relationships between inputs and the output.

<sup>!</sup> Relate input values to their fuzzy sets and apply the decision rules.

<sup>!</sup> Compose the fuzzy results for the output and use some defuzzification method like the COA method to get a crisp value for the output variable.

![](/api/attachments/RSUSNRAQ/fulltext/images/5acae76c06bf23e17e91dab589acb99344fe886da5d7e2e7a1af6074fddb527f.jpg)  
Fig. 8. Membership functions of project quality (PQ).

Luckily, all these steps can be implemented using the FUZZY-Module of the MATLAB software. Using MATLAB we can, for example, fuzzify the input and output variables by constructing the membership functions of inputs and outputs. In addition, using the software we can build a knowledge base of if– then rules, perform inferences using the built in fuzzy decision making logic, and finally defuzzify the output to get a crisp (non-fuzzy) value. This means that, we can use the MATLAB software to build any fuzzy decision making system.

It must be mentioned at this point that the management of the project organization can determine weights for the factors PC, PT, and PQ by consent or by using the Analytic Hierarchy Process (AHP). AHP is a prioritization technique that can deal with unstructured and multi-attribute decisions [19]. AHP starts by dividing the decision problem into a hierarchy of goal, criteria, and alternatives. Using the AHP approach, the decision maker attempts to analyze the impacts of the alternatives at the lowest level of the hierarchy on the overall objective or the focus of the hierarchy. The AHP approach is mainly based on pairwise comparison of elements which has the advantage of greatly reducing the complexity of the decision problem. In addition, the AHP approach applies a consistency test that can screen out inconsistent judgements. Expert Choice (EC) is a microcomputer generic implementation of AHP. It is an interactive software that makes the application of AHP easy and fast [7].The details of AHP as a prioritization tool is beyond the scope of this paper. The reader is referred to [9,19].

## 6. Case study

It might be convenient at this point to illustrate the use of fuzzy decision making for the evaluation of PMIE via a case study. Let us assume that the project organization XYZ completed a project and it is found that the project is 105% overbudget, 135% behind schedule, and 85% conforming to technical and functional specifications. The management of

![](/api/attachments/RSUSNRAQ/fulltext/images/83db692879271a4149b1383b65d661fc479d9825c271f7050fb82f020f1243b7.jpg)  
Fig. 9. Membership functions of project cost weighting factor (PCWF).

XYZ is interested in building a FDMS that evaluates the PMIE.

To be able to evaluate the PMIE for the project, the management of XYZ has to provide its priorities for the factors PC, PT, and PQ. For this purpose, assume that a management team used the software Expert Choice and they constructed a hierarchy of criteria and subcriteria as shown in Fig. 3. The team decided that profitability, market share, and customer satisfaction are the main criteria that should be considered in making the prioritization. According to the standard procedure of EC, the software prompts the user to compare each node in the hierarchy against each of its peers with respect to its parent node. These evaluations are called pairwise comparisons. Then the software synthesizes these judgments according to the mathematically proved approach of AHP. Without going in to the details of AHP and EC, the EC final output of priorities of the alternatives is given in Fig. 4, namely: PCWF=35%, PTWF=18%, and PQWF=47%.

## 6.1. Fuzzy decision making system implementation

Having all necessary inputs for the determination of the PMIE of the project, we can at this point build a FDMS for the evaluation of PMIE according to the following steps.

6.1.1. Step 1: Access the fuzzy-module of MATLAB and enter the names of input variables and the output variables

Fig. 5 illustrates the intended FDMS, where we have six inputs (PC, PT, PQ, PCWF, PTWF, and PQWF), and only one output namely PMIE. In general, the value of PMIE according to our proposed approach is determined from the aggregation of the following three components:

1) The combined impact of PC and PCWF on PMIE: This combined impact can be evaluated using a set of fuzzy if–then rules as shown in Table 1. These rules should be usually based on expert’s knowledge and experience in the project organization. Some examples of these if–then rules are:

![](/api/attachments/RSUSNRAQ/fulltext/images/deb4edfbe7b96458e9cacaddfc937b5c53f3e90bbb2c1cd2e5e345c7d2a93eaf.jpg)  
Fig. 10. Membership functions of project time weighting factor (PTWF).

If PC is Low (L) and PCWF is Medium (M) then PMIE is High (H).

If PC is Low (L) and PCWF is High (H) then PMIE is Very High (VH).

It is to notice that: The lower the project cost is and the higher the PCWF is, the higher is the PMIE.

2) The combined impact of PT and PTWF on PMIE: Similarly, this combined impact can be evaluated according to a set of fuzzy if–then rules as shown in Table 2. We notice that the lower the project time is and the higher the PTWF is, the higher is the PMIE.

3) The combined impact of PQ and PQWF on PMIE: The evaluation of this impact is based on the fuzzy decision rules given in Table 3. In this case: The higher the project quality is and the higher the PQWF is, the higher is the PMIE.

6.1.2. Step 2: Fuzzify the input variables and the output variable PMIE based on expert’s knowledge and experience

The fuzzification of the input variables PC, PT, PQ, PCWF, PTWF, PQWF is presented in Figs. 6–11, respectively. The fuzzification of the output variable PMIE is presented in Fig. 12.

Fig. 6, for example, illustrates the fuzzy subsets and membership functions of the input variable PC. Membership functions in general are developed using expert’s knowledge and experience. The boundaries and the shape of each subset are usually suggested by experts. We selected to use the following fuzzy subsets to fuzzify the input variable project cost: VL (Very Low), L (Low), M (Medium), H (High), and VH (Very High). In addition, we selected to use triangular membership functions.

Similarly, the other input variables PT, PQ, PCWF, PTWF, PQWF and the output variable PMIE are fuzzified.

![](/api/attachments/RSUSNRAQ/fulltext/images/b76ac3d10bda55b68e217568f2612a839050ded2b21735f8bf62f2d3f9904f79.jpg)  
Fig. 11. Membership functions of project quality weighting factor (PQWF).

![](/api/attachments/RSUSNRAQ/fulltext/images/01ff40d2ffe6fb6287e4fb0a96c18a85143f466183862af10e1ffd06b9cc7281.jpg)  
Fig. 12. Membership functions of the project management internal efficiency (PMIE).

6.1.3. Step 3: Enter if–then decision rules into the software

The used if–then rules in our case study are assumed to be based on heuristic knowledge and experience of the experts. They are conveniently tabulated in the form of look-up tables as shown in Tables 1–3. The total number of rules included in the three tables are 45 rules. These rules are entered in to the software and they will be accessed and their truth-ness evaluated during the inferencing process.

An example of a fuzzy rule that is taken from Table 1 is:

If PC is Very High (VH) and PCWF is High (H) then PMIE is Very Low (VL).

The rule above is interpreted as in the following: If the project cost is within the subset Very High as in Fig. 6 and the management priority of project cost is within the fuzzy subset High as shown in Fig. 9 then the combined impact of these two factors on PMIE results in assigning the fuzzy subset Very Low to the output variable PMIE. At this point, the construction of the FDMS is complete because inferencing and defuzzification are built in functions in the software.

## 6.2. Application of the FDMS for PMIE evaluation

At this point the FDMS is ready to accept input values. If we feed the system with the input values [105 135 85 0.35 0.18 0.47], as shown on the bottom of Fig. 13, then the input values are related to their fuzzy sets, the decision rules are applied, and the fuzzy results of the output variable PMIE are composed and defuzzified using the COA method. It must be mentioned that all these steps are implemented by the software based on fuzzy logic rules and operations as it was outlined in Sections 3 and 4 of the paper. The final output is given in Fig. 13.

The output in Fig. 13 can be interpreted as on the following: We have a project that is 105% overbudget, 135% behind schedule, and 85% conforming to technical and functional specifications.

![](/api/attachments/RSUSNRAQ/fulltext/images/070a96ca5acdcd03ddc819a678818a6001ba92105e836b99c273b0e5afd4c69e.jpg)  
Fig. 13. Rules output (final results).

The management has the following priorities: 35%, 18%, and 47% for project cost, project time, and project quality, respectively. The computed value of the PMIE is 52.4% as shown on the rightist top corner of Fig. 13. The PMIE value is relatively low as expected because project quality (85% conforming) is not very high and its weight is relatively very high (47%). Moreover, the project cost is slightly overbudget (105%) but its weight is relatively high (35%). In addition, the project is very much behind schedule (135%) and PTWF is relatively medium (18%). The value of PMIE must be always a number between 0 and 1. The system can be used now for the evaluation of PMIE for any set of inputs.

## 7. Summary and conclusions

This research presented an approach that employs fuzzy decision making (FDM) for the evaluation of the project management internal efficiency (PMIE) which should represent an overall estimate of how well the project was managed and executed. According to the proposed approach, the value of PMIE is determined from the aggregation of the following three impacts: the combined impact of PC and its weighting factor PCWF on PMIE, the combined impact of PT and its weighting factor PTWF on PMIE, and the combined impact of PQ and its weighting factor PQWF on PMIE.

The proposed approach for the evaluation of PMIE is illustrated via a case study. A fuzzy decision making system is designed and implemented using the MATLAB software for the evaluation of the PMIE. In addition, the Analytic Hierarchy Process (AHP), and Expert Choice (EC) were employed for the evaluation of the priorities of PC, PT, and PQ. Expert Choice is the microcomputer generic implementation of AHP. This research also provided a reasonably short but sufficient introduction to the concepts of fuzzy logic and fuzzy decision making. The introduction is of great benefit to readers who don’t have good familiarity with fuzzy logic.

The evaluation of PMIE can serve for project managers and for project organizations as an indicator for the level of achievement of the project management internal objectives. PMIE might be also considered as an indicator for the performance of the project team. The development of a fuzzy decision making system for the evaluation of PMIE is easily implemented using the MATLAB software. MATLAB is a menu-driven software that allows the implementation of fuzzy constructs like membership functions and the creation of a database of decision rules. In addition, fuzzy inferencing and defuzzification are built in functions in MATLAB. The software is easy to use and it is user friendly.

The implemented FDMS relied heavily on expert’s knowledge and experience. Expert’s Knowledge and experience was needed in the determination of fuzzy subsets and membership functions for each input and output variable, and in the determination of if–then rules that govern the relationships between inputs and the output. Hence, the implemented FDMS might be considered as a Fuzzy Decision Making Expert System (FDMES). The proposed FDMS like any other expert system can help preserve the knowledge of experts in the project organization, i.e., it builds up the corporate memory of the firm.

## References

[1] R.D. Archibald, Managing High-Technology Programs and Projects, John Wiley, New York, 1976.

[2] D. Baccarini, The logical framework method for defining project success, Project Management Journal 30 (4) (1999).

[3] A. Belout, Effects of human resource management on project effectiveness and success, toward a new conceptual framework, International Journal of Project Management 16 (1) (1998).

[4] S. Choudhury, Project Management, McGraw-Hill Publishing Company, 2000.

[5] De-Wit, Measurement of project success, International Journal of Project Management 6 (3) (1988).

[6] F. Dweiri, Fuzzy development of crisp activity relationship

charts for facilities layout, Computers and Industrial Engineering 36 (1999) 1 – 16.

[7] E. Forman, T. Saaty, Expert Choice, Decision Support Software company, Mclean, VA, 1983.

[8] M. Freeman, P. Beale, Measuring project success, Project Management Journal 23 (1) (1992) 8 – 17.

[9] B.L. Golden, E.A. Wasil, P.T. Harker, The Analytic Hierarchy Process, Springer Verlag, Berlin, 1989.

[10] Z. Gu¨ ngo¨ r, F. Arikan, Application of fuzzy decision making in part-machine grouping, International Journal of Production Economics 63 (2000) 181 – 193.

[11] A. Kandel, Fuzzy Expert Systems, CRC PRESS, Boca Raton, FL, 1992.

[12] K.C. Lam, A.P. So, T. Hu, T. Ng, R.K. Yuen, S.M. Lo, et al., An integration of the fuzzy reasoning technique and the fuzzy optimization method in construction project management decision-making, Construction Management and Economics 19 (2002) 63– 76.

[13] C. Lee, Fuzzy logic in control systems: fuzzy logic parts I, II, IEEE Transactions on Systems, Man, and Cybernetics 20 (1990) 404.

[14] A.N. Lin, A. Walker, Evaluation of project outcomes, Construction Management and Economics 16 (1998) 209– 219.

[15] E.H. Mamadani, Applications of fuzzy algorithm for simple dynamic plant, IEE Proceedings 121 (1974) 1585– 1588.

[16] E.H. Mamadani, S. Assilian, An experiment in linguistic synthesis with a fuzzy logic controller, International Journal of Man–Machine Studies 7 (1975) 1 –13.

[17] A.K. Munns, B.F. Bjeirmi, The role of project management in achieving project success, International Journal of Project Management 14 (2) (1996) 81– 87.

[18] G. Noci, G. Toletti, A decision support system of qualitybased programs in small firms, Management Decision 36 (7) (1998) 473– 486.

[19] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[20] K.J. Schmucker, Fuzzy Sets, Natural Language Computations and Risks Analysis, Computer Science Press, Rockville, Maryland, 1984.

[21] A.J. Shenhar, O. Levy, D. Dvir, Mapping the dimensions of project success, Project Management Journal 28 (2) (1997).

[22] J. Wateridge, How can IT/IS project be measured for success? International Journal of Project Management 16 (1) (1998) 59– 63.

[23] R.M. Wideman, How to motivate stakeholders to work together, Field Guide to Project Management, Van Nostrand Reinhold, New York, 1998.

[24] H. Yang, C.J. Anumba, J. Kamara, P. Carrillo, A fuzzy-based analytic approach to collaborative decision making for construction teams, Logistics Information Management 14 (5/6) (2001) 344– 354.

[25] J. Yen, R. Langari, Fuzzy Logic Intelligence, Control, and Information, Prentice Hall Publishing Company, 1999.

[26] L.A. Zadeh, The concept of linguistic variable and its application to approximate reasoning, Information Sciences 8 (1975) 199– 249.

[27] L.A. Zadeh, The role of fuzzy logic in the management of uncertainty in expert systems, Fuzzy Sets and System 11 (1983).

[28] L.A. Zadeh, Fuzzy sets, Information and Control 8 (1998) 338–353.

Dr. F. Dweiri is an assistant professor of Industrial Engineering at Jordan University of Science and Technology (JUST). Dr. Dweir received Ph.D., M.Sc. and B.S. in Industrial and Systems Engineer ing from the University of Texas at Arlington, Texas, USA. He also has a B.S. in Electrical Engineering from Lamar University, Beau mont, Texas, USA. He served for two years as the chairman of the Industrial Engineering Department and for 8 years as a faculty of the Mechanical Engineering Department at JUST. Dr. Dweiri research interests include quality improvement, benchmarking, facilities lay out, inventory control, project management, fuzzy logic, production process, and ergonomics.

Dr. M. Kablan is a professor of Mechanical Engineering at Mutah University in Jordan. He received a D.Sc. in Engineering Management from George Washington University, U.S.A., M.Sc. in Mechanical Engineering from Akron University, U.S.A., and a Diplom Ingenieur from Stuttgart University, Germany. He has been a faculty member of the Mechanical Engineering Department since 1991. He served as a chairman of the Mechanical Engineering Department and as an assistant dean at Mutah University for several times. Prof. Kablan’s research interest includes operations research applications, quality improvement, benchmarking, project management, energy management, fuzzy logic, and multicriteria decision-making. Prof. Kablan has written widely in the field, and taught several courses at George Washington University, Mutah University, and Jordan University of Science and Technology.
