---
otero_id: 19934
otero_key: "AUWXVA2C"
title: "A project prioritization approach considering uncertainty, reliability, criteria prioritization, and robustness"
authors: "Hamed Jafarzadeh; Jalil Heidary-Dahooie; Pouria Akbari; Alireza Qorbani"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113731"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A project prioritization approach considering uncertainty, reliability, criteria prioritization, and robustness

![](/api/attachments/AUWXVA2C/fulltext/images/641d00f1871b5b0efe289e9e49cb124cfee2f902ae742a0f59e94818643f8fa7.jpg)

Hamed Jafarzadeh <sup>a,\*</sup>, Jalil Heidary-Dahooie <sup>b</sup>, Pouria Akbari <sup>c</sup>, Alireza Qorbani <sup>c</sup>

<sup>a</sup> School of Management, Massey Business School, Massey University, New Zealand

<sup>b</sup> Department of Industrial Management, Faculty of Management, University of Tehran, Iran

<sup>c</sup> Department of Information Technology Management, Faculty of Management, University of Tehran, Iran

## A R T I C L E I N F O

Keywords: Project selection Project portfolio Z-numbers ZQFD Z-ARAS Z-CODAS ZCOPRAS Z-MABAC

## A B S T R A C T

Given the limitation of resources in organizations (time, money, staff, material, etc.), deciding which projects should be given priority – among many competing projects – is a constant and continuous challenge for decision makers. As a result, a proliferation of methods and solutions for project prioritization has been developed, each with its own strengths and limitations. In this paper, we propose a hybrid approach for prioritizing projects taking into consideration four pervasive challenges in decision making: 1) uncertainty (imprecision and vagueness) of human decisions, 2) reliability (extent of sureness) of decision makers, 3) systematic identification of selection criteria, and 4) robustness of decision making (reasonable tolerance against insignificant changes to decision makers’ evaluations during the process). In doing so, we propose integrating Z-numbers theory with Quality Function Development (ZQFD), four Multi-Criteria Decision-Making (Z-MCDM) methods, ensemble ranking aggregation, and sensitivity analysis. The proposed method is then applied in a real-world organization with twenty IT projects to illustrate how our approach might be used in practice. Furthermore, we elaborate on the trustworthiness of the proposed method in light of 16 criteria available in the literature of structured decision making.

## 1. Introduction

Usually in every organization, more candidate projects exist than can be undertaken given the physical, financial, and logistical limitations of the enterprise [1]. An important and challenging task for the managers and executives, therefore, is to prioritize the projects [2,3]. This calls for a thoughtful selection of the most suitable projects – among the pool of available projects – taking into consideration numerous competing, and in many cases contradictory, selection criteria [4,5].

Given the importance of project prioritization for the organizations, researchers have proposed a proliferation of theoretical and practical methods to tackle this challenge, ranging from simpler approaches using a single technique [6–12] to more sophisticated approaches combining several methods [1,13–15]. However, given that project prioritization in the real world is an overly complex, multifaceted, and to a large extent unstructured decision [16,17], researchers typically have to consider simplifying, compromising, or ignoring some aspects of project priori tization in practice to be able to model the decision making process.

Table 1 presents an illustrative list of relevant studies in this domain and the aspects of decision making they have (and have not) taken into consideration. The table implies that there are still opportunities for proposing decision making models that simultaneously take into consideration four pervasive challenges of decision making in project prioritization: (1) uncertainty (imprecision or vagueness) in decision making (i.e., not being able to provide exact numerical judgment for the importance or weight of factors involved in the decision), (2) the reli ability of decision making (i.e., the extent of sureness of decision makers about their judgments, e.g., very sure, not sure, or rather sure), (3) determining the selection criteria systematically and rigorously (especially when a multitude of selection criteria are involved in the project pri oritization task, which is common in practice), and (4) robustness of the decision to small changes in criteria weights/importance. Motivated by this opportunity, the present paper aims to contribute to the current body of knowledge in project prioritization by proposing an approach for decision making that takes imprecision and vagueness into consider ation, accommodates reliability, can systematically determine the selection criteria, and addresses robustness – which are all ubiquitous in today’s decision making when it comes to prioritizing the projects in organizations.

Table 1  
A (non-inclusive) list of project selection papers and the aspects covered.

<table><tr><td rowspan="2">Publication and brief description</td><td colspan="4">Accounted for ...?</td></tr><tr><td>Uncertainty</td><td>Reliability</td><td>Systematic identification of selection criteria</td><td>Robustness</td></tr><tr><td rowspan="16">Lin and Chen [27] ranked projects in the food sector combining integer linear programming and fuzzy logicEilat et al. [6] proposed a solution for selecting research &amp; development projects using balance scorecard &amp; DEAHuang et al. [7] ranked R&amp;D projects by fuzzy AHPTiryaki and Ahlatcioglu [8] selected and ranked stock via fuzzy AHPChen and Cheng [28] offered a fuzzy MCDM for Information System projectsGhapanchi et al. [9] used a fuzzy DEA solution for choosing projects to maximize portfolio value in the Information Technology sectorTavana et al. [14], combined fuzzy DEA, linear programming, and TOPSIS for ranking potential projectsJiménez et al. [12] proposed a method for incompatible fuzzy goal programming for portfolio optimizationKarsak and Dursun [29] combined DEA and QFD with imprecise data to develop an approach for supplier selectionWang et al. [30] combined Fuzzy with QFD to propose a model to support decision making for selection of patent licensorsKhademi-Zare et al. [31] used two methods of fuzzy QFD to sort strategic decisions in the context of mobile-based communicationTayali and Timor [32] used an analytic hierarchy process along with a statistical variance procedure to rank projectsJafarzadeh et al. [1], combined QFD with DEA to establish the best portfolio of projects in the IT sectorAkbari et al. [15] combined ARAS with QFD and fuzzy logic to prioritize projects in the IT sectorHeidary et al. [23] combinad fuzzy QFD and five MCDM methods in deterministic conditionMohtashami and Ghiasvand [33] merged fuzzy DEA with z-number theory to evaluate efficiency and effectiveness in the financial industryAboutorab et al. [34] integrated BWM and z-number (ZBWM) and supplier developmentDurbach et al. [2] developed and examined some fast and frugal heuristics approaches to select an approximately optimal portfolioLin and Hsieh [5] proposed a hybrid model based on fuzzy logic for best portfolio managementHujainah et al. [35] presented a new partially-automated technique named StakeQP to select appropriate key stakeholdersLourenco et al. [3] developed a Portfolio Robustness Evaluation approach and depicted the respective Pareto frontierArratia et al. [36] offered a mathematical solution to establish R&amp;D project portfoliosMohagheghi et al. [17] offered a novel multi-objective approach for evaluation of high tech project portfoliosTavana et al. [16] proposed combination of two-stage hybrid MCDM and linear programming (integer) to choose projects under uncertainty with interdependencies</td><td rowspan="16">✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓</td><td rowspan="16">-</td><td rowspan="16">-</td><td rowspan="16">-</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr></table>

To achieve the above objective, we propose to integrate z-numbers theory (which can measure both imprecision/vagueness and reliability) with Quality Function Development<sup>1</sup> (ZQFD) which allows a systematic and rigorous identification of the selection criteria before feeding them into the decision-making algorithms. We next combine z-numbers with four MCDM methods (Z-MCDM) and then aggregate the individual outputs with the Ensemble Ranking Method. Sensitivity analysis is then used to examine the robustness of the decision to changes in the criteria weights. Next, we implement the proposed approach in an IT organization with twenty projects to illustrate how our proposed approach might be used in practice. In addition, the trustworthiness of the proposed method is discussed and evaluated in light of 16 criteria available in the literature

of structured decision making.

Our proposed approach in this paper largely draws upon MCDM methods, which are ‘decision aids’ to support decision makers (DMs) in complex decision problems when a multitude of criteria, objectives and stakeholders are involved [18]. These methods “assist people in making decisions using their own preferences in cases where more than one conflicting criterion exists” [19 ,p.810] (which is the case in our study), and are said “to be a way of dealing with complex problems by breaking them into smaller [manageable] pieces” [19 ,p.810]. While MCDM methods typically cannot guarantee an absolute optimal decision<sup>2</sup> [19] and also demand more time and effort from the DMs (compared to fast decisions solely based on DMs’ intuition or experience), the systematic approach undertaken in MCDM would help the DMs “to feel that all important criteria have been properly accounted for, which should help to reduce the possibility of post-decision regret” [19 ,p.810]. The more careful understanding of the decision problem and the more systematic identification and evaluation of the decision criteria during the MCDM process ideally help the DMs to avoid making important decisions only out of habit [19,20] which, in essence, could justify the extra effort needed for MCDM-driven decision making. [21]

## 2. Background

This section provides a brief background about decision making models for project prioritization as well as the methods used in the paper including z-numbers theory, ZQFD and Z-MCDM.

## 2.1. Decision making models for project prioritization

Decision making models for project prioritization have been an area of interest in the academic community for decades, leading to the emergence of a vast range of proposed models and approaches, each with its own focus, limitations, assumptions, and characteristics (see Table 1 for a sample list). For example, many studies in this domain account for imprecision and vagueness in decision making by incorpo rating fuzzy logic [22] into their proposed model. Some tend to focus on prioritizing the projects simply based on a known, and usually small, set of selection criteria (e.g., [2,9,14,16]). An example is Ghapanchi, et al. [9] who propose a solution based on Fuzzy Data Envelopment Analysi (DEA) to identify and rank the most valuable projects but. as acknowl. edged in the paper itself (p.798), they do not offer any suggestion fo determining the decision factors (the feed to the DEA process) and simply rely on the organization to name a few selection factors with no systematic or rigorous analysis. Tavana et al. [14] is another example which introduces a combined model (DEA, Technique of Order Prefer ence Similarity to the Ideal Solution [TOPSIS] and integer program ming) to prioritize information technology projects but they do not provide any guideline for determining the selection factors. Anothe group of studies pay special attention to systematic and rigorous iden tification of selection criteria. Examples, among others, are Jafarzadeh et al. [1], Akbari et al. [15], and Heidary et al. [23] who considered careful and systematic identification of criteria. Some studies have taken into consideration the reliability (extent of sureness) of decision makers judgment during the decision making process (however, they are not in the context of proiect selection). In some other studies, robustness of decisions has been the primary point of interest, which is typically addressed by incorporating several ranking models in the process of decision making, given that there is a general consensus in the literature that reliance on one single technique is prone to robustness risk [24.25], especially when the differences between the alternatives/criteria are inherently small or the number of alternatives/criteria is large [26]. All things considered. one can see that there are still opportunities for putting forward hybrid solutions with the ability to take into consider ation four aspects of real-world decision making at the same time: un: certainty (imprecision and vagueness) in human decision making when prioritizing projects, reliability of judgment by the decision makers, systematic identification of multiple selection criteria, and robustness of decision making. The present paper seeks to address this goal.

## 2.2. Z-numbers theory

Z-numbers theory, introduced by Zadeh [37], is an extension to fuzzy logic [22] and brings in a new whole dimension to the notion of modeling human judgment. Fuzzy logic, as the origin of z-numbers, is an approach to support decision making in conditions where a decision is made under uncertainty and with imprecise and vague data [38]. Instead of using rigid numbers, in fuzzy logic people express their evaluation of a phenomenon (e.g., importance of a factor) in terms of linguistic variables (such as: “very low, low, high, very high”) which is more aligned with the natural cognitive system of the human brain

![](/api/attachments/AUWXVA2C/fulltext/images/61e1a2fcfb9d6aeaab166a1804c9d8fee60f1613c61dd4a02239884fce0d5ffa.jpg)  
Fig. 1. A simple Z-number adapted from [41].

[36,37,39].

While fuzzy logic is very strong in dealing with uncertainty in deci sion making, it does not address the notion of reliability – another important aspect of human judgment. Reliability refers to the extent to which one is sure or confident about his/her judgment. A z-number is a pair of two ordered fuzzy components, $Z = ( A , B )$ , in which A is an evaluation of the value of a parameter (X) in an uncertain situation, and B is a measure of the reliability $( \mathrm { i . e . }$ , extent of sureness or confidence) of A (Fig. 1). Both A and B are described in the form of uncertain natural language fuzzy labels, for example, about 45 min, not very sure) for evaluating the distance between two cities, (very high, absolutely) for evaluating the honesty of a witness in a court [37], (high, potential) to evaluate trust of a supplier, and (low, very confident) to estimate demand for a product [40]. According to Zadeh, if we consider calculation by exact numbers as level 1 and calculation by uncertain fuzzy numbers as level 2, then z-numbers stand at level 3 where we can compute through numbers that are not fully reliable (hence, one level closer to real-world human decision making) [33]. The definitions and procedure or calcu lation of z-numbers are outlined in the following.

Definition 1. Assume that $Z = ( \widetilde { A } , \widetilde { R } )$ is a z-number. $\widetilde { A } =$ $\{ ( x , \mu _ { _ A } ( x ) )$ |xϵX} and $\widetilde { R } = \{ ( x , \mu _ { _ R } ( x ) { \mathrm { ) } } | x \epsilon X \}$ } are triangular membership functions. $\widetilde { A }$ and $\widetilde { R }$ can be converted to a definite number using Eq. 1 [41].

$$
\alpha = \frac {\int x \mu_ {R} ^ {\sim} (x) d x}{\int \mu_ {R} ^ {\sim} (x) d x}\tag{1}
$$

where α represents the weight of second part $( { \widetilde { R } } )$ and $\mu _ { { \widetilde R } } \alpha \left( x \right)$ repre sents the degree of dependence of $x \in X$ in ${ \widetilde { R } } .$ Following that, α can be added to the first part (A<sup>̃</sup>) by using Eq. 2 [41]:

$$
\widetilde {Z} ^ {\alpha} = \left\{(x, \mu_ {\underset {A} {\sim^ {\alpha}}}) | \mu_ {\underset {A} {\sim^ {\alpha}}} (x) = \alpha \mu_ {\underset {A} {\sim}} (x), x \in [ 0, 1 ] \right\},\tag{2}
$$

where $\mu _ { \widetilde { A } } \alpha \left( x \right)$ represents the degree of dependence of $x \in X \mathrm { i n } \widetilde { A } ^ { \alpha }$ . As a result, by combining the linguistic variables for assessing the criteria and alternatives and the rules for transforming reliability linguistic vari ables, the rules for converting z-number linguistic variables to triangular fuzzy numbers (TFN) are obtained [41].

Definition 2. Assuming that $\widetilde { \mathbf { A } } = ( \mathbf { l } _ { 1 } , \mathbf { m } _ { 1 } , \mathbf { u } _ { 1 } )$ and $\widetilde { \mathbf { B } } = ( \mathrm { l } _ { 2 } , \mathrm { m } _ { 2 } , \mathrm { u } _ { 2 } )$ are two fuzzy numbers; then, the main algebraic operations between A<sup>̃</sup>, B<sup>̃</sup> and crisp value k are [42]:

$$
\widetilde {A} \oplus \widetilde {B} = (l _ {1} + l _ {2}, m _ {1} + m _ {2}, u _ {1} + u _ {2}),\tag{3}
$$

$$
\widetilde {A} \ominus \widetilde {B} = (l _ {1} - u _ {2}, m _ {1} - m _ {2}, u _ {1} - l _ {2}),\tag{4}
$$

$$
\widetilde {A} \otimes \widetilde {B} = (l _ {1} \times l _ {2}, m _ {1} \times m _ {2}, u _ {1} \times u _ {2}),\tag{5}
$$

$$
\widetilde {A} \oslash \widetilde {B} = (l _ {1} \div u _ {2}, m _ {1} \div m _ {2}, u _ {1} \div l _ {2}),\tag{6}
$$

$$
k \times \widetilde {A} = (k \times l _ {1}, k \times m _ {1}, k \times u _ {1}),\tag{7}
$$

$$
(\widetilde {A}) ^ {- 1} = \left(\frac {1}{u _ {1}}, \frac {1}{m _ {1}}, \frac {1}{l _ {1}}\right),\tag{8}
$$

$$
(\widetilde {A}) ^ {\widetilde {B}} = \left(l _ {1} ^ {u _ {2}}, m _ {1} ^ {m _ {2}}, u _ {1} ^ {l _ {2}}\right).\tag{9}
$$

Definition 3. Assuming that $\widetilde { \mathbf { A } } = ( \mathbf { l } _ { 1 } , \mathbf { m } _ { 1 } , \mathbf { u } _ { 1 } )$ and $\widetilde { \mathbf { B } } = ( \mathrm { l } _ { 2 } , \mathrm { m } _ { 2 } , \mathrm { u } _ { 2 } )$ are two fuzzy numbers. Then, the distance between A <sup>̃</sup> and B <sup>̃</sup> is calculated by the Eq. 10 [16]:

$$
d (\widetilde {A}. \widetilde {B}) = \sqrt {\frac {1}{3} \left[ (l _ {1} - l _ {2}) ^ {2} + (m _ {1} - m _ {2}) ^ {2} + (u _ {1} - u _ {2}) ^ {2} \right]}.\tag{10}
$$

Definition 4. Let $\widetilde { \mathbf { A } } = \left( \mathrm { l } _ { 1 } , \mathrm { m } _ { 1 } , \mathrm { u } _ { 1 } \right)$ is a fuzzy number; then, based on the graded mean integration representation method (GMIR), the graded mean integration representation value $\mathbf { G } ( \widetilde { \mathbf { A } } )$ is calculated by Eq. 11 [34]:

$$
G (\widetilde {A}) = \left[ l _ {1} + 4 m _ {1} + u _ {1} \right] / 6.\tag{11}
$$

## 2.3. ZQFD

The concept of Quality Function Deployment (QFD) was first intro duced in Japan in the 1960s and 70s for systematic translation of customer needs into characteristics of new services and products [43]. Since then. the method has been used widely as an effective method for quality management. In QFD, customers’ requirements (also known as the voice of customers) are transformed into a group of detailed quan titative and qualitative specifications that help to design and engineer the characteristics and features of a new product or service [1]. In general, QFD can be used in any context when the goal is to prioritize and weight a list of objectives or benefits (HOWs) based on a given set of requirements or criteria (WHATs), for instance for project selection [1,15] or for supplier selection [44,45].

QFD analysis is facilitated through a semantic visualization known as House of Quality (HOQ) which guides the process of converting customer needs (WHATs) to design specifications (HOWs) (Fig. 2) [1,45]. To start the QFD process, domain experts (QFD team) first identify the customer requirements (CR) (or WHATs) (section A in Fig. 2) and evaluate the relevant importance weight of each requirement (sec tion B) through listening to, and considering, the voice of customers. Drawing on their knowledge, experience, and expertise, the QFD team then translate the customer requirements into a set of design specifica tion (DS) (or HOWs) (section C). Next, the QFD team examines which DS (HOW) affects which CR (WHAT) and to what extent (section D). In addition, they identify the correlations between design specifications (HOWs) (section E). Using the data seated in sections A to E, the impor tance scores of the design specifications are calculated (section $F ) ,$ , which is the ultimate aim of the HOQ process. These weights will then inform the design and development of the new product or service by demon strating which DSs should receive more attention (e.g., receive more resources) to make sure that the associated most important customer requirement(s) are best met [1,45].

In the classical form of the QFD process, scores and weights are evaluated with crisp and deterministic values [46], but given that de cision making in real-world applications commonly takes place under uncertainty, vagueness, and imprecision, prior research has incorpo rated fuzzy logic into the QFD process to allow decision makers to state their judgments in the form of natural linguistic labels, rather than picking a single numeric value [1,15,45,47]. However, as discussed previously in the introduction section of the paper, while fuzzy logic is successful in considering the intrinsic fuzziness and uncertainty in human decision making, it does not account for the extent to which decision makers are sure or have confidence in their decisions (i.e., the reliability of the decision) [33,37,40]. In the present research, we therefore propose to combine QFD with z-numbers theory to accom modate both uncertainty and reliability of evaluations and assessments by decision makers during the process of project selection. This is a new contribution to the broad literature in general and of project selection in particular given that integration of z-numbers into the QFD approach is currently very scarce in the literature (limited to a couple of recent papers in the context of logistics [48] and health [49]).

## 2.4. Z-MCDM

Multi-criteria decision making (known commonly as MCDM) is a branch of operations research that aims to choose between a set of al ternatives based on multiple competing selection criteria [50]. The outcome is a list of sorted or ranked alternatives. Each MCDM method has its own characteristics, strengths, limitations, assumptions, and logic; therefore, they typically produce different, and in many cases inconsistent, results, even when the input to the models is the same [51]. Comparing the results of different models is a controversial challenge in the MCDM domain given that none of the methods is inherently superior to the others [51]. As a solution, it is commonly suggested in the liter ature to employ multiple MCDM methods at the same time and then aggregate the results to increase the robustness of the analysis [25,50]. While some studies use a simple statistic, such as averaging [52] or ranked means [53] to aggregate the individual results, other attempts to reconcile the differences and work out a compromise [51,54,55] using techniques such as Borda [56,57], Borda-Kendall [58,59], Copeland [26], utility range [50] and ensemble ranking [51].

![](/api/attachments/AUWXVA2C/fulltext/images/382785d005c39184a482f47b3a2bf37cb0be119f4574fc8f3914a4f86926cefa.jpg)  
Fig. 2. House of quality (adapted from [1]).

![](/api/attachments/AUWXVA2C/fulltext/images/df61feb1d04846e1e289acf02aff11e2779e5213c67dc2b982395ba7ff7f9b5d.jpg)  
Fig. 3. Proposed hybrid method

To address the robustness issue, and following suggestions in the literature (e.g., [60]), in the present research we employ four Z-MCDM techniques to prioritize and rank the projects based on the criteria carefully identified through the ZQFD process.<sup>3</sup> We also combine the four MCDM methods with z-number theory to simultaneously address uncertainty and reliability of the decision by domain experts. The four methods employed in our model are Additive Ratio Assessment (ARAS) [61], combinative distance-based assessment (CODAS) [62], Complex Proportional Assessment of alternatives (COPRAS) [63], and Multi-Attributive Border Approximation area Comparison (MABAC) [64]. As these methods are merged with z-numbers in the present study, we abbreviate them to Z-ARAS, Z-CODAS, Z-COPRAS, and Z-MABAC. For aggregation, we use the ensemble ranking method [51] as a novel method in this field which is based on half-quadratic theory and is able to provide consensus of aggregation of results. In the ensemble ranking method, the weight of each MCDM method is obtained with no need for human intervention. The logic and algorithm for ensemble ranking is presented in the proposed model section of this paper. Sensitivity analysis eventually determines which ranking method (i.e., the four MCDM methods and ensemble) is the most robust solution.

## 3. Proposed method

The hybrid model proposed in this study combines z-numbers, QFD, four Z-MCDM techniques, ensemble ranking, and sensitivity analysis to provide a seamless and integrated solution that simultaneously caters for four prevalent challenges of project selection decision making in real-world situations: 1) uncertainty (imprecision and vagueness) of human decisions, 2) reliability (extent of sureness) of decision makers, 3) handling a large number of carefully identified selection criteria in decision making, and 4) robustness of decision by taking a multiplemethod approach for decision making. The method consists of three phases and a number of steps (see Fig. 3) which are explained in the following.

## 3.1. Phase 1. Formulating the problem

The first phase of our approach, which is an initial phase to formulate the problem, is largely adopted from Jafarzadeh et al. [1] and consists of two steps:

## 3.1.1. Step 1a. Establishing the team for decision making

The process starts with identifying the team of domain experts, or the decision makers (DMs), responsible for prioritizing the projects to maximize the benefit of the organization. DMs are chosen based on their local expertise in the organization and their deep knowledge about the projects and criteria for selecting and prioritizing the projects in that organization. Furthermore, a senior manager is required to evaluate the DMs as part of the decision-making process (required for Step 2a).

## 3.1.2. Step 1b. Determining WHATs and HOWs for the decision-making problem

In the context of project selection, the QFD WHATs refer to the criteria influencing the selection of the projects, and the HOWs refer to the benefits expected from implementing those projects. Many lists of project selection factors and project benefits (with lots of similarities and overlaps) are available in the literature which can be used in the decision-making process. However, given that the situation and the needs of every organization are unique, the factors (WHATs) and ben efits (HOWs) in the literature should be tailored for each organization. It is therefore required to refine and confirm the list of WHATs and HOWs with the DMs to ensure fitness of the factors for the particular situation of the organization under examination [1]. DMs may exclude some factors or introduce new ones according to the condition of their orga nization and the decision-making problem.

## 3.2. Phase 2. Prioritizing selection criteria using ZBWM and ZQFD

The selection criteria and the benefits identified in the previous phase are then used in phase 2 to build the House of Quality in the QFD process. This will result in systematic evaluation and calculation of the relevant importance score (or weight) of selection factors and project benefits according the judgments of the DMs. In our proposed model, we combine z-numbers with the QFD process to address both the uncer tainty and the reliability (extent of sureness) involved in real-world decision making.

## 3.2.1. Step 2a. Determining the importance of WHATs using group ZBWM

While the simplest way to determine the weights of the benefits (WHATs) is to ask the DMs to directly give a score to each criterion, it has been consistently demonstrated in the literature that more advanced computational methods return better outcomes [65]. In our proposed method, therefore, we adopt the best-worst method (BWM) [66] as one of the most recent developments in the domain of multi-criteria decision making based on pairwise comparison. BWM has demonstrated a number of advantages over its older counterparts (e.g., Analytic Hier archy Process – AHP) such as less computational complexity and higher compatibility [66] which has resulted in significant uptake by the research community since its introduction in 2015 [67,68]. To account for uncertainty and reliability concerns in human judgment (which are among the objectives of our study), we integrate BWM with z-numbers [34]. The embedded application of z-numbers and BWM (aka ZBWM) in the literature so far considers only one decision maker [69,70] but in our method we have several decision makers. $\mathrm { W e , }$ therefore, extend current ZBWM to group ZBWM which is able to consolidate the individual de cisions into one group decision. In doing so, we employ an approach proposed by Pedrycz et al. [71] which appoints an external qualified person (e.g., a senior manager) to assign a credit weight to the individual DMs based on their knowledge and experience. Our proposed procedure for group ZBWM analysis and calculation is as follows (see Table 2 for nomenclature).

Table 2  
Sets, parameters, and variables of group ZBWM.

<table><tr><td colspan="2">Sets</td><td colspan="2">Variables</td></tr><tr><td>“J</td><td>Set of criterion</td><td> $\widetilde{\lambda}_{B}$ </td><td>Fuzzy weight of the best expert by senior manager</td></tr><tr><td rowspan="2">K</td><td rowspan="2">Set of experts</td><td> $\widetilde{\lambda}_{W}$ </td><td>Fuzzy weight of the worst expert by senior manager</td></tr><tr><td> $\widetilde{\lambda}_{k}$ </td><td>Fuzzy weight of  $k^{th}$  expert by senior manager</td></tr><tr><td colspan="2">Index</td><td> $\widetilde{a}_{Bk}^{\lambda}$ </td><td>Fuzzy preference of best expert over the expert k by senior manager</td></tr><tr><td>j</td><td>Criteria (1,...,n)</td><td> $\widetilde{a}_{kW}^{\lambda}$ </td><td>Fuzzy preference of expert k over the worst expert by senior manager</td></tr><tr><td>k</td><td>Decision makers (1,...,p)</td><td> $\widetilde{w}_{B}^{k}$ </td><td>Fuzzy weight of the best criterion by  $k^{th}$  expert</td></tr><tr><td>B</td><td>Best criterion</td><td> $\widetilde{w}_{W}^{k}$ </td><td>Fuzzy weight of the worst criterion by  $k^{th}$  expert</td></tr><tr><td>W</td><td>Worst criterion</td><td> $\widetilde{w}_{j}^{k}$ </td><td>Fuzzy weight of criterion j by  $k^{th}$  expert</td></tr><tr><td rowspan="6">λ</td><td rowspan="6">Expert weights</td><td> $\widetilde{a}_{Bj}^{k}$ </td><td>Fuzzy preference of the best criterion over the criterion j by  $k^{th}$  expert</td></tr><tr><td> $\widetilde{a}_{jW}^{k}$ </td><td>Fuzzy preference of criterion j over the worst criterion by  $k^{th}$  expert</td></tr><tr><td> $\widetilde{w}_{j}$ </td><td>Final fuzzy weight of each criterion</td></tr><tr><td>G</td><td>Graded mean integration representation for representing generalized fuzzy number</td></tr><tr><td> $\widetilde{\xi}_{\lambda}$ </td><td>Optimal objective value of model for weight of expert</td></tr><tr><td> $\widetilde{\xi}_{k}$ </td><td>Optimal objective value of model for weight of main criteria”</td></tr></table>

To undertake group ZBWM, first, using z-number linguistic variables listed in Table 4 $( \boldsymbol { \mathrm { b } } , \boldsymbol { \mathrm { c } } ) ,$ , the senior manager identifies the best $\left( E _ { B } \right)$ and the worst $( E _ { W } )$ experts $( \mathrm { i . e . }$ , DMs) based on their abilities and experiences. Then they compare $E _ { B }$ to other experts and other experts to $E _ { W } .$ . As mentioned, the evaluations are converted to TFNs using Eqs. 1 and 2 and then expressed as follows:

$$
\widetilde {A} _ {B} ^ {\lambda} = \big (\widetilde {a} _ {B 1} ^ {\lambda}, \widetilde {a} _ {B 2} ^ {\lambda}, \dots , \widetilde {a} _ {B k} ^ {\lambda} \big),\tag{12}
$$

$$
\widetilde {A} _ {W} ^ {\lambda} = \bigl (\widetilde {a} _ {1 W} ^ {\lambda}, \widetilde {a} _ {2 W} ^ {\lambda}, \dots , \widetilde {a} _ {k W} ^ {\lambda} \bigr).\tag{13}
$$

In order to perform pairwise comparisons of the criteria, $C = \{ c _ { 1 } , c _ { 2 } ,$ $\ldots , c _ { n } \}$ , each expert chooses the best $( C _ { B } )$ and the worst $( C _ { W } )$ criterion using linguistic variables based on z-numbers listed in Table 4 (b, c). Next, they undertake pairwise comparisons between the best criterion and other criteria, as well as between the others and the worst criterion. By using Eqs. 1 and 2, the obtained results based on TFNs are expressed as:

$$
\widetilde {A} _ {B} ^ {k} = \left(\widetilde {a} _ {B 1} ^ {k}, \widetilde {a} _ {B 1} ^ {k}, \dots , \widetilde {a} _ {B j} ^ {k}\right),\tag{14}
$$

$$
\widetilde {A} _ {W} ^ {k} = \left(\widetilde {a} _ {1 W} ^ {k}, \widetilde {a} _ {2 W} ^ {k}, \dots , \widetilde {a} _ {j W} ^ {k}\right).\tag{15}
$$

Eventually, we calculate the optimal importance of experts $\widetilde { \lambda } _ { k } ^ { * } =$ $( \widetilde { \lambda } _ { 1 } ^ { * } , \widetilde { \lambda } _ { 2 } ^ { * } , . . . , \widetilde { \lambda } _ { k } ^ { * } )$ and the optimal weight of the criteria $\widetilde { \pmb { w } } _ { j } ^ { \ast } = \left( \widetilde { \pmb { w } } _ { 1 } ^ { \ast } , \widetilde { \pmb { w } } _ { 2 } ^ { \ast } , \dots \right.$ $, \widetilde { w } _ { j } ^ { * } \big )$ using the following optimization problem (Eq. 16).

All z-number evaluations for group ZBWM (either by the senior manager to evaluate the experts or by the experts to evaluate the criteria) are in the form of $Z = ( \widetilde { A } , \widetilde { R } )$ in which A <sup>̃</sup> is a linguistic label representing the importance (weight) of the object under decision and R<sup>̃</sup> is the extent to which the decision maker is sure (or unsure) about their evaluation. The linguistic variables applied in this study are presented in Table 3. In addition, Table 3 shows the fuzzy triangular membership function used in the study. Once the linguistic labels are determined by the individuals using z-numbers, then the definitions and procedure outlined previously in Section 2.1 are employed to convert the linguistic terms into numerical quantified values.

min $\widetilde { \xi } _ { \lambda } + \sum _ { k = 1 } ^ { p } \widetilde { \xi } _ { k }$

$$
\left\{ \begin{array}{l} \left| \frac {\widetilde {\lambda} _ {B}}{\widetilde {\lambda} _ {k}} - \widetilde {a} _ {B k} ^ {\lambda} \right| \leq \widetilde {\xi} _ {\lambda}; \forall k, \\ \left| \frac {\widetilde {\lambda} _ {k}}{\widetilde {\lambda} _ {W}} - \widetilde {a} _ {k W} ^ {\lambda} \right| \leq \widetilde {\xi} _ {\lambda}; \forall k, \\ \left| \frac {\widetilde {w} _ {B} ^ {k}}{\widetilde {w} _ {j} ^ {k}} - \widetilde {a} _ {B j} ^ {k} \right| \leq \widetilde {\xi} _ {k}; \forall j, k, \\ \left| \frac {\widetilde {w} _ {j} ^ {k}}{\widetilde {w} _ {W} ^ {k}} - \widetilde {a} _ {j W} ^ {k} \right| \leq \widetilde {\xi} _ {k}; \forall j, k, \\ \widetilde {w} _ {j} = \sum_ {k = 1} ^ {p} \sum_ {j = 1} ^ {n} \widetilde {w} _ {j} ^ {k} \widetilde {\lambda} _ {k}; \forall j, k, \\ \sum_ {k = 1} ^ {p} G (\widetilde {\lambda} _ {k}) = 1, \\ \sum_ {k = 1} ^ {p} \sum_ {j = 1} ^ {n} G (\widetilde {w} _ {j} ^ {k}) = 1, \\ l _ {j} ^ {w} \leq m _ {j} ^ {w} \leq u _ {j} ^ {w}, \\ l _ {j} ^ {w} \geq 0, \\ l _ {k} ^ {\lambda} \leq m _ {k} ^ {\lambda} \leq u _ {k} ^ {\lambda}, \\ l _ {k} ^ {\lambda} \geq 0. \end{array} \right.\tag{16}
$$

## 3.2.2. Step2b. Prioritizing HOWs as per ZQFD algorithm

Next, the ZQFD process is employed to prioritize the benefits of projects (HOWs). In doing so, we construct the House of Quality (HOQ) as per Fig. 2. So far, project benefits $( \mathsf { W H A T s } = C R _ { 1 } , C R _ { 2 } , . . . , C R _ { m } )$ and project selection criteria $( \mathrm { H O W s } \ : = \ : D S _ { 1 } , \ : \ : D S \ : _ { 2 } , . . . , \ : D S \ : _ { m } )$ have been identified in Phase 1 of our proposed method. Moreover, the importance of WHATs $( \widetilde { W } _ { C R } )$ has been determined (Step 2a) using group ZBWM. Now, each DM $( k = 1 , . . . , p )$ identifies the relationship between WHATs and HOWs using the z-numbers (Eq. 17).

Table 3  
Linguistics variables for weighting criteria and ranking alternatives.

<table><tr><td colspan="2">a) Linguistic variables for ranking alternatives (i.e., projects) ( $\widetilde{A}$ ) [72]</td><td colspan="2">(b) Linguistic variables for pairwise comparison of criteria and experts (also  $\widetilde{A}$ ) [73]</td><td colspan="2">(c) Linguistic variables for reliability (extent of sureness) ( $\widetilde{R}$ ) [42]</td></tr><tr><td>Linguistic Terms</td><td>Membership Function</td><td>Linguistic Variables</td><td>Membership Function</td><td>Linguistic Terms</td><td>Membership Function</td></tr><tr><td>Very High (VH)</td><td>(7, 9, 9)</td><td>Equally important (EI)</td><td>(1,1,1)</td><td>Very sure (VS)</td><td>(0.7, 1, 1)</td></tr><tr><td>High (H)</td><td>(5, 7, 9)</td><td>Weakly important (WI)</td><td>(0.67, 1, 1.5)</td><td>Sure (S)</td><td>(0.5, 0.7, 0.9)</td></tr><tr><td>Medium (M)</td><td>(3, 5, 7)</td><td>Fairly Important (FI)</td><td>(1.5, 2, 2.5)</td><td>Neutral (N)</td><td>(0.3, 0.5, 0.7)</td></tr><tr><td>Low (L)</td><td>(1, 3, 5)</td><td>Very important (VI)</td><td>(2.5, 3, 3.5)</td><td>Relatively unsure (RS)</td><td>(0.1, 0.3, 0.5)</td></tr><tr><td>Very Low (VL)</td><td>(1,1,3)</td><td>Absolutely important (AI)</td><td>(3.5, 4, 4.5)</td><td>Not sure at all (NSA)</td><td>(0, 0, 0.3)</td></tr></table>

$$
\widetilde {Y} _ {k} = \left[ \widetilde {y} _ {i j} ^ {k} \right] _ {n \times m},\tag{17}
$$

$$
\text { where } \widetilde {y} _ {i j} ^ {k} = \widetilde {Z} _ {i j} ^ {k} (\widetilde {A}, \widetilde {R}); i = 1, \dots , m; j = 1, 2, \dots , n; k = 1, 2, \dots , p.
$$

The z-numbers are then converted to TFNs according to Eq. 18.

$$
\widetilde {X} _ {k} = \left[ \widetilde {x} _ {i j} ^ {k} \right] _ {n \times m},\tag{18}
$$

$$
\text { where } \widetilde {x} _ {i j} ^ {k} = \left(l _ {i j} ^ {k}, m _ {i j} ^ {k}, u _ {i j} ^ {k}\right); i = 1,..., m; j = 1, 2,..., n; k = 1, 2,..., p.
$$

Let $\widetilde { x } _ { i j } ^ { k }$ be the judgment of ${ K } ^ { t h } { \bf D } { \bf M } ,$ indicating the relationship between ith benefit $( i = 1 , 2 , . . . ,$ m) and jth indicator $( j = 1 , 2 , . . . , i$ n); then, the aggregation of the opinions of DMs is calculated based on Eq. 19 and 20.

$$
\widetilde {S} _ {i j} = \left\{\left(l _ {i j}, m _ {i j}, u _ {i j}\right) | i = 1, \dots , m; j = 1, 2, \dots , n \right\},\tag{19}
$$

$$
\text { where } l _ {i j} = \frac {1}{p} \sum_ {k = 1} ^ {p} l _ {i j} ^ {k}, m _ {i j} = \frac {1}{p} \sum_ {k = 1} ^ {p} m _ {i j} ^ {k}, u _ {i j} = \frac {1}{p} \sum_ {k = 1} ^ {p} u _ {i j} ^ {k}.
$$

$$
\widetilde {S} = \left[ \widetilde {S} _ {i j} \right] _ {n \times m},\tag{20}
$$

where $\widetilde { S } _ { i j }$ represents the average opinions of $k ^ { t h }$ decision maker.

The final weight (importance degree) of the $j ^ { t h }$ selection criteria (HOWs) is calculated using Eq. 21.

$$
\begin{array}{c} \widetilde {\omega} _ {H O W} ^ {*} = [ \widetilde {w} _ {C R 1} \quad \dots \quad \widetilde {w} _ {C R i} \quad \dots \quad \widetilde {w} _ {C R m} ] \otimes [ \widetilde {S} _ {i j} ] _ {n \times m} \\ = [ \widetilde {\omega} _ {H O W 1} ^ {*} \quad \dots \quad \widetilde {\omega} _ {H O W j} ^ {*} \quad \dots \quad \widetilde {\omega} _ {H O W n} ^ {*} ] \end{array}\tag{21}
$$

## 3.3. Phase 3. Z-MCDM analysis and aggregation, to rank the project

This phase consists of three steps as described in the following.

## 3.3.1. Step3a. Individual Z-MCDM analysis to prioritize the projects

In this paper, we propose to use ARAS, CODAS, COPRAS, and MABAC in combination with z-number logic to account for uncertainty as well as reliability involved in human decision making by the DMs (i. e., Z-ARAS, Z-CODAS, Z-COPRAS, and Z-MABAC).

To form the decision matrix, each DM $( k = 1 , . . . , p )$ is asked to evaluate the selection criteria for each project using z-numbers $( \widetilde { \nu } _ { i j } ^ { k } )$ which results in forming the decision matrix as shown in Eq. 22.

$$
\widetilde {V} _ {k} = \left[ \widetilde {v} _ {i j} ^ {k} \right] _ {n \times m},\tag{22}
$$

where $\widetilde { \nu } _ { i j } ^ { k } = \widetilde { Z } _ { i j } ^ { k } ( \widetilde { A } , \widetilde { R } ) ; i = 1 , . . . , m ; j = 1 , 2 , . . . , n ; k = 1 , 2 , . . . , p .$

Eq. 1 and Eq. 2 are then used to convert z-numbers to triangular numbers. The aggregated decision matrix $( \tilde { T } )$ is established based on Eq. 23.

$$
\widetilde {T} = \left[ \widetilde {t _ {i j}} \right] _ {n \times m}; i = 1, \dots , m; j = 1, 2, \dots , n.\tag{23}
$$

This decision-making matrix and final weight (HOWs) obtained from the ZQFD process $( \widetilde { \omega } _ { i } ^ { * } )$ are then fed to the Z-ARAS, Z-CODAS, Z-COPRAS, and Z-MABAC to individually rank the projects in accordance with their underlying logic and algorithm.

## 3.3.2. Step3b. Aggregating Z-MCDM analyses and determining the combined rank

In our proposed model, we use the ensemble ranking method [51] which is a novel development for aggregating the output of individual Z-MCDMs. Ensemble ranking is objective and obtains the weight of each Z-MCDM method with no need for human intervention, via Algorithm 1.

Algorithm 1. Ensemble ranking

$$
\begin{array}{l} \text {‘Input: Ranking P^{m}, m = 1,2,\ldots,M} \\ \text {While NotConverged do} \\ \alpha_ {m} = \delta (\| P ^ {m} - P ^ {*} \| _ {2}), m = 1, 2, \ldots , M \\ w _ {m} = \alpha_ {m} / \sum_ {j} \alpha_ {j}, m = 1, 2, \ldots , M \\ P ^ {*} = \sum_ {m} w _ {m} P ^ {m} \\ \text {end while} \\ \text {Output Final Ranking P^{*}, \alpha^{\prime\prime}} \end{array}
$$

Where $P ^ { * }$ represents the final aggregated ranking for project $i , P ^ { m }$ indicates the ranking of the $m ^ { t h }$ Z-MCDM method, $\alpha _ { m }$ shows the mini mizer function based on half-quadratic function, and $w _ { m }$ is the weight of each Z-MCDM method obtained by half-quadratic function [51].

## 3.3.3. Step 3c. Determining the most robust ranking using sensitivity analysis

Sensitivity analysis is a method used to evaluate the robustness of MCDM techniques by examining the extent to which the outcome of the decision-making model changes when the weightings of the selection criteria change [60,74,75]. A more robust approach is expected to demonstrate a higher level of tolerance to the fluctuations in the weightings of the criteria before the outcome of the MCDM model $( \mathrm { i . e . , }$ the ranking of the alternatives) is affected and changed [74,76]. In our method, we therefore propose to employ sensitivity analysis to assess which of the individual or aggregated methods used in the previous steps exhibit a higher level of robustness.

The sensitivity coefficient $( S C _ { i j } )$ of the $i ^ { t h }$ method is calculated as the average value of changes in alternative rankings by each method when the criterion j weight is modified (Eq. 25) [60].

$$
S C _ {i j} = \frac {\sum_ {w = 1} ^ {W} D _ {i j} ^ {w}}{F}; \forall i, j, w \in \{0, 0. 0 1, 0. 1, 0. 5, \dots , 1. 0 1, 1. 0 5, \dots , 4, 5 \},\tag{25}
$$

where $S C _ { i j }$ indicates the sensitivity coefficient of method i to criterion j, $D _ { i j } { } ^ { w }$ shows the number of changes that occurred in the alternative ranking result by method i in defined variation in the criterion weight $( j ) ,$ and F represents the frequency of changes in the criteria weights. Eventually, the total average sensitivity of each method (SC \*) is calculated via Eq. 26 where j denotes the number of criteria.

$$
S C _ {i} ^ {*} = \frac {\sum_ {j = 1} ^ {J} S C _ {i j}}{J}; \forall i, j.\tag{26}
$$

## 4. Applying the proposed method in a real-world case

Unlike optimization or simulation-based studies where independent verification and validation (V&V) of a new solution is typically feasible based on a set of objective measures (e.g., runtime, accuracy, and variability) or in comparison to baseline models, in many MCDM-based studies, opportunities for objective validation of proposed solutions are limited (and in many cases not relevant). The reason is that each MCDM method comes with its own characteristics and normally there is no baseline model to compare to. In other words, in many MCDM studies (including ours), the aim is more about illustrating how the proposed solution might be used (rather than validation or verification) which is typically undertaken through applying the solution in an illustrative case study or in a numerical example. This approach for assessing the applicability of MCDM-based models is extensively used in the litera ture. Recent examples are Asadabadi and Zwikael [4] (where the au thors proposed a solution for ranking ambiguous project proposals and then demonstrated the applicability of the method via applying it in an illustrative real-world case study with three projects), Kilic et al. [77] (where the authors proposed a decision-making methodology for personnel selection and then demonstrated the applicability of the method via applying it in a case study of personnel selection in a manufacturing company), and Hsu et al. [49] (where the authors pro posed a model to prioritize healthcare strategies and then demonstrated the applicability of the model via implementing it in an illustrative healthcare case study in Taiwan).

Hence, consistent with most similar studies in the domain of project selection (e.g., [1,4,9,16]), we apply our proposed method in a realworld case study to illustrate how it might be used in practice. The company is a large organization that provides telecommunication ser vices to more than sixty million active customers. In collaboration with the Project Management Office (PMO) of the organization, and with the intention to maximize the project benefits of the organization, twenty competing IT projects were analyzed and prioritized using our proposed hybrid method.

## 4.1. Phase 1. Formulating the problem

Two steps are undertaken in this phase, as follows.

## 4.1.1. Step 1a and 1b. Establishing the team for decision making and determining WHATs and HOWs

In consultation with the PMO of the organization, four expert deci sion makers (DMs) were selected who had a deep knowledge of the digital strategy of the company and were fully familiar with the 20 projects (all in managerial positions with a minimum of 5 years’ work experience in the organization). In addition, a senior manager was appointed by the PMO for evaluating the DMs as part of the process.

To identify the “project selection criteria (HOWs) and the project benefits (WHATs)” we referred to the literature which offers a long list of project selection factors and project benefits with many similarities and overlaps. For our case study, we adopt a list proposed by Jafarzadeh et al. [1] which they collated through review and aggregation of liter ature, as presented in Table 4. After reviewing the list with the experts (DMs and the senior manager), they confirmed the appropriateness of the factors for prioritizing projects in their organization and did not recommend any modifications.

## 4.2. Phase 2. Prioritizing selection criteria using group ZBWM and ZQFD

Phase 2 in the case study consists of two steps.

Table 4  
Criteria involved in the selection of IT projects (WHATs), and the expected benefits (HOWs) [1].

<table><tr><td></td><td colspan="2">HOWs</td><td>WHATs</td></tr><tr><td>B1</td><td>“Alignment with strategic objectives”</td><td>C1</td><td>“Contribution to corporate strategic goals”</td></tr><tr><td>B2</td><td>“Risk of project”</td><td>C2</td><td>“Maximize the value of the portfolio”</td></tr><tr><td>B3</td><td>“Acceptance and support of senior management”</td><td>C3</td><td>“Acceptance by users”</td></tr><tr><td>B4</td><td>“Technology requirements”</td><td>C4</td><td>“Minimize the risk”</td></tr><tr><td>B5</td><td>“Complexity of the project”</td><td>C5</td><td>“Balance in the portfolio of projects”</td></tr><tr><td>B6</td><td>“Dependency to other projects”</td><td>C6</td><td>“Organizational performance”</td></tr><tr><td>B7</td><td>“Alignment between team skills and project needs”</td><td>C7</td><td>“Proper stakeholders management”</td></tr><tr><td>B8</td><td>“ROI of project”</td><td></td><td></td></tr><tr><td>B9</td><td>“Project transparency requirements”</td><td></td><td></td></tr><tr><td>B10</td><td>“Innovation required”</td><td></td><td></td></tr><tr><td>B11</td><td>“Flexibility in time and project activities”</td><td></td><td></td></tr><tr><td>B12</td><td>“Implementation cost”</td><td></td><td></td></tr><tr><td>B13</td><td>“Alignment of project manager skills to the project”</td><td></td><td></td></tr><tr><td>B14</td><td>“Net present value of earnings”</td><td></td><td></td></tr></table>

The next step was to determine the relevant importance of each WHAT using group ZBWM as described in Section 3.2.1 The senior manager was first asked to determine the best $\left( E _ { B } \right)$ and the worst $( E _ { W } )$ DMs and evaluate others against them. Then, a questionnaire was given to each DM in which they were asked to identify the best $( C _ { B } )$ and the worst $( C _ { W } )$ criteria and then undertake pairwise comparisons between the best/worst criteria and the others. All evaluations at this step (by the senior manager and the DMs) were via z-numbers in which the linguistic terms in Table 3(b) were used for pairwise comparisons and the terms in Table 3(c) for extent of sureness (reliability). The evaluations by the senior manager and the DMs are presented in Tables 5 and $^ { 6 , }$ respectively. Conversion of the labels to associated fuzzy z-numbers, as per Eqs. 1 and $^ { 2 , }$ are also reported in Tables 5 and 6.

Lastly, the importance of WHATs was calculated based on group ZBWM logic outlined in Eq. 16. The result is depicted in Table 7.

## 4.2.2. Step 2b. Prioritizing HOWs as per fuzzy ZQFD algorithm

This step began with evaluating the relationship between the HOWs and the WHATs. In doing so, the decision makers were requested to express their opinion in relation to the impact of each HOW on each WHAT using z-numbers and based on the linguistic variables presented in Table 3(a) for the weights (‘very high’ to ‘very low’ in five intervals) and Table 3(c) for the reliability (‘not sure at all’ to ‘very sure’). Eq. 17, 18 and 19 were then used to calculate the correlations between WHATs and HOWs $( \widetilde { s } _ { i j }$ in Table 8). Finally, the ultimate weight of HOWs was obtained via Eq. 21, which is reported in Table 9.

## 4.3. Phase 3. Z-MCDM analysis and aggregation to prioritize the project

The weighted list of HOWs identified at the end of Phase 2 (Table 9) creates a solid foundation for Phase 3 in which the four Z-MCDM methods (Z-ARAS, Z-CODAS, Z-COPRAS, and Z-MABAC) are applied and aggregated to inform the best selection of the project that can bring in the maximum value for the company (according to the weighted benefits and selection factors).

## 4.3.1. Step 3a. Individual Z-MCDM analysis to prioritize the projects

The four expert DMs were asked to complete a questionnaire and score the twenty IT projects (P1 to P20) against the 14 criteria. Again, znumbers were used to allow DMs to express their judgments and the level of sureness about their judgments (same linguistic variables as in Table 3). The DMs’ evaluations (i.e., decision matrix) are shown in Table 10. The linguistic z-number evaluations by DMs were then con verted to triangular numbers. The result is demonstrated in Table 11.

Table 5  
Linguistic pairwise evaluation of DMs by the senior manager.

<table><tr><td></td><td></td><td>Linguistic evaluation</td><td>Translating to z-number</td><td></td><td></td><td>Linguistic evaluation</td><td>Translating to z-number</td></tr><tr><td rowspan="2">Best</td><td></td><td>#2</td><td></td><td>Worst</td><td></td><td>#4</td><td></td></tr><tr><td>#1</td><td>(FI, S)</td><td>(1.26, 1.68, 2.1)</td><td></td><td>#1</td><td>(VI, S)</td><td>(2.1, 2.52, 2.94)</td></tr><tr><td rowspan="3">Best-to-others</td><td>#2</td><td>(EI, VS)</td><td>(1, 1, 1)</td><td rowspan="3">Worst-to-others</td><td>#2</td><td>(AI, S)</td><td>(2.94, 3.36, 3.78)</td></tr><tr><td>#3</td><td>(VI, S)</td><td>(2.1, 2.52, 2.94)</td><td>#3</td><td>(FI, S)</td><td>(1.26, 1.68, 2.1)</td></tr><tr><td>#4</td><td>(AI, S)</td><td>(2.94, 3.36, 3.78)</td><td>#4</td><td>(EI, VS)</td><td>(1, 1, 1)</td></tr></table>

Table 6  
Pairwise comparisons of criteria (WHATs) based on DMs’ (experts’) opinions.

<table><tr><td colspan="2"></td><td colspan="4">Linguistic evaluation</td><td colspan="6">Linguistic evaluation</td></tr><tr><td>DM</td><td></td><td>#1</td><td>#2</td><td>#3</td><td>#4</td><td></td><td></td><td>#1</td><td>#2</td><td>#3</td><td>#4</td></tr><tr><td>Best</td><td></td><td>C1</td><td>C6</td><td>C1</td><td>C1</td><td>Worst</td><td></td><td>C5</td><td>C5</td><td>C5</td><td>C4</td></tr><tr><td rowspan="7">Best-to-others</td><td>C1</td><td>(EI, VS)</td><td>(WI, N)</td><td>(EI, VS)</td><td>(EI, VS)</td><td rowspan="7">Worst-to-others</td><td>C1</td><td>(VI, S)</td><td>(VI, S)</td><td>(AI, VS)</td><td>(VI, VS)</td></tr><tr><td>C2</td><td>(VI, S)</td><td>(WI, S)</td><td>(VI, RS)</td><td>(FI, S)</td><td>C2</td><td>(FI, S)</td><td>(AI, VS)</td><td>(WI, RS)</td><td>(VI, S)</td></tr><tr><td>C3</td><td>(WI, VS)</td><td>(WI, VS)</td><td>(FI, N)</td><td>(WI, NSA)</td><td>C3</td><td>(VI, N)</td><td>(VI, S)</td><td>(VI, N)</td><td>(AI, S)</td></tr><tr><td>C4</td><td>(FI, S)</td><td>(FI, N)</td><td>(VI, S)</td><td>(VI, VS)</td><td>C4</td><td>(FI, N)</td><td>(VI, S)</td><td>(FI, S)</td><td>(EI, VS)</td></tr><tr><td>C5</td><td>(VI, S)</td><td>(AI, VS)</td><td>(AI, VS)</td><td>(FI, S)</td><td>C5</td><td>(EI, VS)</td><td>(EI, VS)</td><td>(EI, VS)</td><td>(FI, S)</td></tr><tr><td>C6</td><td>(FI, S)</td><td>(EI, VS)</td><td>(FI, S)</td><td>(FI, S)</td><td>C6</td><td>(VI, N)</td><td>(AI, VS)</td><td>(VI, S)</td><td>(AI, VS)</td></tr><tr><td>C7</td><td>(EI, VS)</td><td>(WI, S)</td><td>(VI, N)</td><td>(VI, NSA)</td><td>C7</td><td>(FI, VS)</td><td>(FI, N)</td><td>(FI, N)</td><td>(AI, VS)</td></tr></table>

Table 7  
Final importance weights of WHATs (as per ZBWM).

<table><tr><td>DMs</td><td>#1</td><td>#2</td><td>#3</td><td>#4</td><td>Final weights</td></tr><tr><td>C1</td><td>(0.198, 0.225, 0.225)</td><td>(0.164, 0.164, 0.164)</td><td>(0.25, 0.254, 0.27)</td><td>(0.173, 0.173, 0.177)</td><td>(0.173, 0.195, 0.235)</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C7</td><td>(0.162, 0.162, 0.187)</td><td>(0.103, 0.122, 0.134)</td><td>(0.102, 0.102, 0.102)</td><td>(0.129, 0.129, 0.129)</td><td>(0.121, 0.136, 0.17)</td></tr></table>

According to the requirements of each Z-MCDM method and using the weights already obtained from ZQFD analysis, we calculated the priority score for each project and ranked them accordingly. The result is presented in Table 12.

4.3.2. Step 3b. Aggregating Z-MCDM analyses and determining the combined rank

The results were then combined with the aid of the ensemble ranking method to prioritize the projects as reported in Table 12 (last column). The results are also visualized in Fig. 4 (in situations where a project receives the same rank by different methods, one method is shown by a dot and others by abbreviations).

## 4.3.3. Step 3c. Determining the most robust ranking using sensitivity analysis

To programmatically assess the robustness of the model, we imple ment sensitivity analysis. Fig. 5 shows how the ranking of the four MCDM methods and the aggregated ensemble ranking changed as the result of manipulating the weighting of each criteria [60]. Dark green depicts no sensitivity (no changes) to the ranking, light green demonstrates one single change, grey means two changes, and white denotes three or more changes. In doing the analysis, criteria were changed one at a time [60] and normalization was applied to ensure the total criteria weights have a unit sum to one [78].

Table 8  
Linguistic assessment of relationships between HOWs and WHATs and aggregated results $( \widetilde { S } _ { i j } ) .$

<table><tr><td colspan="2"></td><td colspan="6">DMs</td><td colspan="6">DMs</td></tr><tr><td rowspan="2">WHATs</td><td>HOWs</td><td>#1</td><td>#2</td><td>#3</td><td>#4</td><td> $s_{ij}$ </td><td>HOWs</td><td>#1</td><td>#2</td><td>#3</td><td>#4</td><td> $s_{ij}$ </td><td></td></tr><tr><td>B1</td><td>(H, S)</td><td>(VH, S)</td><td>(H, VS)</td><td>(VH, S)</td><td>(0.89, 1.35, 1.83)</td><td>B8</td><td>(H,N)</td><td>(M, S)</td><td>(H, S)</td><td>(M, N)</td><td>(0.53, 0.91, 1.45)</td><td></td></tr><tr><td rowspan="2">C1</td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B7</td><td>(M, N)</td><td>(H, N)</td><td>(L, S)</td><td>(M, N)</td><td>(0.38, 0.71, 1.2)</td><td>B14</td><td>(H, RS)</td><td>(H, N)</td><td>(L,N)</td><td>(H, S)</td><td>(0.48, 0.82, 1.32)</td><td></td></tr><tr><td rowspan="2">...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B1</td><td>(M, N)</td><td>(M, N)</td><td>(L, N)</td><td>(VH, S)</td><td>(0.33, 0.57, 0.89)</td><td>B8</td><td>(L, N)</td><td>(M, N)</td><td>(L, S)</td><td>(H, S)</td><td>(0.24, 0.48, 0.86)</td><td></td></tr><tr><td rowspan="2">C7</td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B7</td><td>(M, RS)</td><td>(L, N)</td><td>(L, S)</td><td>(VH, S)</td><td>(0.28, 0.51, 0.81)</td><td>B14</td><td>(L, RS)</td><td>(M, N)</td><td>(L, S)</td><td>(H, S)</td><td>(0.23, 0.46, 0.83)</td><td></td></tr></table>

Final weight of each HOWs.

<table><tr><td>HOWs</td><td> $\widetilde{\omega}_{HOW}^{*}$ </td><td>Defuzzified values</td><td>Normalized</td><td>Rank</td><td>HOWs</td><td> $\widetilde{\omega}_{HOW}^{*}$ </td><td>Defuzzified values</td><td>Normalized</td><td>Rank</td></tr><tr><td>B1</td><td>(0.416, 0.686, 1.039)</td><td>0.767</td><td>0.081</td><td>2</td><td>B8</td><td>(0.318, 0.578, 0.94)</td><td>0.659</td><td>0.07</td><td>9</td></tr><tr><td>B2</td><td>(0.395, 0.665, 1.025)</td><td>0.734</td><td>0.078</td><td>4</td><td>B9</td><td>(0.422, 0.706, 1.095)</td><td>0.803</td><td>0.085</td><td>1</td></tr><tr><td>B3</td><td>(0.373, 0.645, 1.004)</td><td>0.722</td><td>0.076</td><td>5</td><td>B10</td><td>(0.257, 0.495, 0.838)</td><td>0.551</td><td>0.058</td><td>13</td></tr><tr><td>B4</td><td>(0.312, 0.58, 0.934)</td><td>0.682</td><td>0.072</td><td>7</td><td>B11</td><td>(0.293, 0.538, 0.904)</td><td>0.595</td><td>0.063</td><td>12</td></tr><tr><td>B5</td><td>(0.24, 0.485, 0.834)</td><td>0.543</td><td>0.057</td><td>14</td><td>B12</td><td>(0.395, 0.674, 1.059)</td><td>0.761</td><td>0.08</td><td>3</td></tr><tr><td>B6</td><td>(0.312, 0.58, 0.934)</td><td>0.682</td><td>0.072</td><td>7</td><td>B13</td><td>(0.348, 0.616, 0.994)</td><td>0.709</td><td>0.075</td><td>6</td></tr><tr><td>B7</td><td>(0.303, 0.559, 0.882)</td><td>0.627</td><td>0.066</td><td>11</td><td>B14</td><td>(0.306, 0.548, 0.895)</td><td>0.639</td><td>0.067</td><td>10</td></tr></table>

Table 10  
Decision matrix of DMs’ opinions (V<sup>̃</sup>).

<table><tr><td colspan="2"></td><td colspan="7">Projects</td><td colspan="5">Projects</td></tr><tr><td rowspan="5">B1</td><td>DM</td><td>P1</td><td>P2</td><td>...</td><td>P20</td><td></td><td rowspan="5"></td><td rowspan="5">B14</td><td>DM</td><td>P1</td><td>P2</td><td>...</td><td>P20</td></tr><tr><td>#1</td><td>(VL, S)</td><td>(L, S)</td><td>...</td><td>(VH, S)</td><td>...</td><td>#1</td><td>(L, S)</td><td>(VL, RS)</td><td>...</td><td>(H, RS)</td></tr><tr><td>#2</td><td>(VL, N)</td><td>(L, S)</td><td>...</td><td>(VH, S)</td><td></td><td>#2</td><td>(L, S)</td><td>(VL, RS)</td><td>...</td><td>(M, N)</td></tr><tr><td>#3</td><td>(M, S)</td><td>(VH, N)</td><td>...</td><td>(VL, N)</td><td></td><td>#3</td><td>(L, S)</td><td>(VL, N)</td><td>...</td><td>(L, RS)</td></tr><tr><td>#4</td><td>(VH, S)</td><td>(VH, S)</td><td>...</td><td>(L, S)</td><td></td><td>#4</td><td>(VL, S)</td><td>(L, N)</td><td>...</td><td>(M, S)</td></tr></table>

Table 11  
Aggregated decision matrix (T<sup>̃</sup>).

<table><tr><td></td><td>B1 (+)</td><td>B2 (−)</td><td>B3 (+)</td><td>B4 (+)</td><td>B5 (−)</td><td>B6 (−)</td><td>B7 (+)</td></tr><tr><td>P1</td><td>(2.48, 3.32, 4.51)</td><td>(2.16, 3.41, 4.67)</td><td>(1.84, 3.38, 4.57)</td><td>(2.12, 2.96, 4.69)</td><td>(4.6, 6.28, 7.11)</td><td>(3.42, 4.75, 5.38)</td><td>(0.84, 2.09, 3.76)</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P20</td><td>(3.32, 4.57, 5.34)</td><td>(2.7, 4.31, 5.57)</td><td>(2.67, 4.22, 5.76)</td><td>(5.63, 7.24, 7.24)</td><td>(1.73, 2.57, 4.35)</td><td>(3.91, 5.63, 6.95)</td><td>(1.98, 3.3, 4.62)</td></tr><tr><td></td><td>B8 (−)</td><td>B9 (+)</td><td>B10 (−)</td><td>B11 (−)</td><td>B12 (−)</td><td>B13(+)</td><td>B14 (+)</td></tr><tr><td>P1</td><td>(1.61, 2.59, 3.84)</td><td>(1.88, 3.14, 4.39)</td><td>(4.51, 6.12, 6.89)</td><td>(1.92, 3.26, 4.59)</td><td>(3.02, 4.19, 4.74)</td><td>(1.73, 2.79, 4.12)</td><td>(0.84, 2.09, 3.76)</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P20</td><td>(0.81, 2, 3.6)</td><td>(1.23, 1.64, 3.25)</td><td>(1.73, 2.57, 4.35)</td><td>(1.26, 1.68, 3.35)</td><td>(3.54, 5.15, 6.4)</td><td>(0.81, 2, 3.6)</td><td>(1.98, 3.3, 4.62)</td></tr></table>

Table 12  
Priority score and rank of each project across four methods, and final rank.

<table><tr><td rowspan="2">Projects</td><td colspan="2">Z-ARAS</td><td colspan="2">Z-CODAS</td><td colspan="2">Z-COPRAS</td><td colspan="2">Z-MABAC</td><td colspan="2">Ensemble Ranking</td></tr><tr><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td><td>Score</td><td>Rank</td><td>P*</td><td>Final Rank</td></tr><tr><td>P19</td><td>0.668</td><td>1</td><td>4.021</td><td>1</td><td>100.00</td><td>1</td><td>0.156</td><td>1</td><td>1.00</td><td>1</td></tr><tr><td>P15</td><td>0.666</td><td>2</td><td>3.502</td><td>2</td><td>97.552</td><td>2</td><td>0.144</td><td>3</td><td>2.29</td><td>2</td></tr><tr><td>P18</td><td>0.646</td><td>3</td><td>2.973</td><td>3</td><td>95.753</td><td>4</td><td>0.147</td><td>2</td><td>2.79</td><td>3</td></tr><tr><td>P10</td><td>0.613</td><td>4</td><td>1.412</td><td>4</td><td>96.685</td><td>3</td><td>0.072</td><td>4</td><td>3.92</td><td>4</td></tr><tr><td>P11</td><td>0.590</td><td>5</td><td>1.062</td><td>5</td><td>95.431</td><td>6</td><td>0.038</td><td>7</td><td>5.66</td><td>5</td></tr><tr><td>P6</td><td>0.582</td><td>6</td><td>0.761</td><td>8</td><td>90.730</td><td>9</td><td>0.040</td><td>6</td><td>6.86</td><td>6</td></tr><tr><td>P3</td><td>0.567</td><td>8</td><td>1.062</td><td>6</td><td>83.672</td><td>15</td><td>0.047</td><td>5</td><td>7.05</td><td>7</td></tr><tr><td>P20</td><td>0.570</td><td>7</td><td>0.783</td><td>7</td><td>87.775</td><td>10</td><td>0.022</td><td>8</td><td>7.53</td><td>8</td></tr><tr><td>P4</td><td>0.561</td><td>9</td><td>0.532</td><td>9</td><td>84.112</td><td>14</td><td>0.020</td><td>9</td><td>9.39</td><td>9</td></tr><tr><td>P14</td><td>0.550</td><td>11</td><td>-0.113</td><td>10</td><td>84.545</td><td>13</td><td>-0.020</td><td>10</td><td>10.55</td><td>10</td></tr><tr><td>P8</td><td>0.550</td><td>10</td><td>-0.216</td><td>11</td><td>92.910</td><td>7</td><td>-0.042</td><td>13</td><td>10.96</td><td>11</td></tr><tr><td>P17</td><td>0.532</td><td>12</td><td>-0.304</td><td>12</td><td>84.613</td><td>12</td><td>-0.041</td><td>12</td><td>12.00</td><td>12</td></tr><tr><td>P16</td><td>0.527</td><td>13</td><td>-0.382</td><td>13</td><td>82.124</td><td>16</td><td>-0.020</td><td>11</td><td>12.65</td><td>13</td></tr><tr><td>P12</td><td>0.525</td><td>14</td><td>-1.062</td><td>14</td><td>95.650</td><td>5</td><td>-0.059</td><td>15</td><td>13.58</td><td>14</td></tr><tr><td>P13</td><td>0.509</td><td>15</td><td>-1.645</td><td>16</td><td>91.886</td><td>8</td><td>-0.090</td><td>16</td><td>15.06</td><td>15</td></tr><tr><td>P5</td><td>0.506</td><td>16</td><td>-1.123</td><td>15</td><td>80.182</td><td>19</td><td>-0.058</td><td>14</td><td>15.34</td><td>16</td></tr><tr><td>P2</td><td>0.495</td><td>17</td><td>-1.874</td><td>17</td><td>85.011</td><td>11</td><td>-0.092</td><td>17</td><td>16.53</td><td>17</td></tr><tr><td>P7</td><td>0.472</td><td>18</td><td>-2.412</td><td>18</td><td>81.123</td><td>17</td><td>-0.125</td><td>18</td><td>17.92</td><td>18</td></tr><tr><td>P1</td><td>0.443</td><td>19</td><td>-3.323</td><td>19</td><td>80.684</td><td>18</td><td>-0.169</td><td>19</td><td>18.92</td><td>19</td></tr><tr><td>P9</td><td>0.438</td><td>20</td><td>-3.555</td><td>20</td><td>76.145</td><td>20</td><td>-0.191</td><td>20</td><td>20.01</td><td>20</td></tr></table>

![](/api/attachments/AUWXVA2C/fulltext/images/9cc89c28d5810d7e2d7406d66f439711225899013fbad11214795f07f6b72784.jpg)  
Fig. 4. Priority rank of the project for individual Z-MCDMs and aggregated with ensemble ranking.

![](/api/attachments/AUWXVA2C/fulltext/images/4e20de6c33c1a0c271b842de03377a76e5c315663a846b60a3bb68b25f39ab5f.jpg)

Fig. 5. The sensitivity analysis by change of criterion weight (\*: for each criterion, the 5 rows of colored cells shown the sensitivity change for, from top, Z-ARAS, Z-CODAS, ZCOPRAS, Z-MABAC, and ensemble, respectively).  
![](/api/attachments/AUWXVA2C/fulltext/images/3f2c1dd556b5a4703c6c98b9830efba02bb2f522cc949f81b7bd7f7da5b73f1f.jpg)  
Fig. 6. Sensitivity coefficient (SC ) for individual factors and overall for the model (SC \*).

We used Eq. 26 and 27 to calculate the overall sensitivity for each MCDM method per criterion (Fig. 6, light grey bars) and then as a whole for each method (Fig. 6. dark bars). With the lowest sensitivity coefficient (which means higher robustness [76]) calculated for ensemble ranking in Fig. 6 (overall = 3.543), it is evident that, for our case study, aggregated ensemble ranking is the most successful method in terms of robustness of the decision making. However, it should be noted that this result is specific to the case study. In Section 5.2, we undertake further analysis on the robustness through a scenario analysis.

## 5. Further examination of the proposed method

Further to applying our proposed hybrid method in a real-world case (as discussed in Section 4), in this section we undertake further analysis on our case data to assess our proposed model in terms of reliability and robustness. We first assess to what extent incorporating reliability into the decision-making model changes the outcome of the decision (and whether it is significant) (via Spearman coefficient analysis) (Section 5.1). Then, we examine the extent to which the result of our proposed solution is sensitive to the changes in decision makers’ opinions (via scenario analysis) and which MCDM method demonstrates higher robustness to artificial noises (via sensitivity analysis) (Section 5.2).

## 5.1. Examining the impact of reliability

To examine the magnitude of the impact of reliability/sureness on changing the final outcome of decision making, we analyzed our nu merical case once more but this time without considering DMs’ level of sureness.<sup>4</sup> The result is reported in Table 13. Fifteen out of the twenty projects (75%) had a shift in their position, some of which were very significant. For example, P2 shifted eight steps down (from 17 to 9) when the level of sureness expressed by the DMs was ignored. In the opposite direction, P11 climbed in the ranking by 11 steps (from 5 to 16). Just from the look of Table 5, the difference in the ranks is noticeable. To make this assessment more objective, we applied Spearman correlation coefficient (r ) [76,79] which demonstrates the statistical importance of the difference between the two rankings (with and without the reliability component in our case) through calculating pairwise correlations as per Eq. 27 [79].

Table 13  
Comparison of rankings with and without the reliability aspect.

<table><tr><td>Project</td><td>Ranking of projects excluding reliability</td><td>Shift in the rank without reliability</td><td>Project</td><td>Ranking of projects excluding reliability</td><td>Shift in the rank without reliability</td></tr><tr><td>P1</td><td>19</td><td>No change</td><td>P11</td><td>16</td><td>11</td></tr><tr><td>p2</td><td>9</td><td>-8</td><td>P12</td><td>17</td><td>3</td></tr><tr><td>P3</td><td>7</td><td>No change</td><td>P13</td><td>15</td><td>No change</td></tr><tr><td>P4</td><td>8</td><td>-1</td><td>P14</td><td>6</td><td>-4</td></tr><tr><td>P5</td><td>12</td><td>-4</td><td>P15</td><td>1</td><td>-1</td></tr><tr><td>P6</td><td>5</td><td>-1</td><td>P16</td><td>10</td><td>-3</td></tr><tr><td>P7</td><td>18</td><td>No change</td><td>P17</td><td>14</td><td>2</td></tr><tr><td>P8</td><td>13</td><td>2</td><td>P18</td><td>4</td><td>1</td></tr><tr><td>P9</td><td>20</td><td>No change</td><td>P19</td><td>3</td><td>2</td></tr><tr><td>P10</td><td>11</td><td>7</td><td>P20</td><td>2</td><td>-6</td></tr></table>

$$
r _ {s} = 1 - \frac {6 \sum_ {i = 1} ^ {n} d _ {i} ^ {2}}{n (n ^ {2} - 1)},\tag{27}
$$

where $d _ { i }$ and n are the rank difference at position i and the number of ranks, respectively.

The Spearman coefficient calculated for the two rankings (with and without reliability) was 0.747. According to Keshavarz-Ghorabaee et al. [62], this is considered a noticeable difference between the two rankings (as the coefficient is below the threshold of 0.8). This clearly emphasizes the importance of accounting for the sureness level in decision-making models. Undoubtedly, variance in level of sureness exists in human de cision making in real-world scenarios and our case study provides evi dence that ignoring the level of sureness can change the ultimate ranking considerably. It is, however, worthwhile to note that the Spearman analysis is not meant to demonstrate that one ranking is better, or more accurate, than the other. Here, in the Spearman analysis, there is no notion of comparison between the rankings as no basis exists for such a conclusion. Rather, Spearman analysis provides objective support for the importance of capturing the level of sureness when modeling real-world decision-making problems (as we did in the present paper).

Furthermore, without revealing which ranking considered reliability and which one did not, we presented the two rankings to the four DMs as well as the senior manager and asked them to choose which ranking seems more meaningful to them in general. Overall, they all chose the ranking which considered the level of sureness. While not an objective quantified assessment, this comparison broadly implies the better per formance of the decision model where the level of sureness is taken into consideration in our particular case study.

## 5.2. Examining robustness: Scenario analysis

In our case study, as explained in Section 4.3.3, ensemble ranking exhibited the highest level of tolerance to artificial changes applied to the criteria weights. This result, however, was specific to the situation of our case and the specific weights assigned to the criteria by the expert DMs. One case study on its own cannot demonstrate whether ensemble ranking is necessarily the most robust solution in all situations. We, therefore, delved further into the robustness issue by conducting scenario analysis following the procedure proposed by Sun et al. [80]. Scenario analysis is similar to sensitivity analysis in nature but allows changing weights simultaneously across several criteria (whereas sensitivity analysis varies weights one at a time). Five scenarios were designed. For scenario $^ { 1 , }$ equal weights were given to each criterion. For scenarios 2 to $^ { 5 , }$ in consultation with the senior manager, the criteria were broadly grouped into financial (B8, B12, B14), stakeholders (B1, B3), project (B2, B5, B6, B9, B11), and learning/growth (B4, B7, B10, B13). For each of scenarios 2 to 5, the criteria in one of the groups received the highest weight via giving 50% of the total weight to the criteria in that group. The remaining 50% was split between the rest of the criteria equally. For example, for the stakeholder scenario, B1 and B3 received 50% of the weight (0.25 each) and the remaining 12 criteria received 0.042 each (total of 50%). We then followed the same process for sensitivity analysis as described in Section 4.3.3 (Eq. 25 and 26). The outcome is presented in Table 14. The asterisk in each column depicts the smallest value (i.e., sensitivity), hence, the most robust ranking method for each scenario. Z-ARAS and Z-CODAS performed best in two of the scenarios each, whereas MABAC outperformed others in one scenario. Z-COPRAS had no success and ensemble performed better than the others in the original case data (where actual weights were assigned by the DMs).

The scenario analysis evidently demonstrates that no method is the best method in terms of robustness. The level of robustness of each method varies from one scenario to another, urging that careful and thorough investigation of robustness is essential in each case should the organizations seek to make the most robust decision that is less sensitive to small changes in the weights of criteria (which, in essence, is desirable in practical real-world applications) [33,34,49]. Overall, the outcome of the scenario analysis supports the last step in our proposed hybrid model where we suggest that sensitivity analysis is required to determine which method is better able to establish the most robust project ranking in each particular case of project ranking in organizations.

## 6. Discussion

In the real world, prioritizing projects is an overly complex task for organizations. Consequently (and conceivably) researchers have to apply simplifications when they propose academic models and solutions for such decision making. Our paper is no exception but it attempts to make the application of decision-making models one step closer to the reality by addressing four common challenges of real-world decision making simultaneously in one proposed hybrid solution, and then applying the approach in a case study to illustrate how it might be used in practice. In summary, the main contribution of our paper to the decision-making arena is proposing a hybrid solution for the important problem of project prioritization in organizations when the decision has to be made 1) under uncertainty and impreciseness, 2) the decision makers are not fully confident about the reliability (or sureness) of their evaluations and judgments during the decision-making process, 3) there is a large number of selection criteria to be carefully and systematically identified and incorporated into the decision-making process, and 4) the organization is keen to make a decision robust to the small changes to criteria weights. The main generalizable take-away for the readers is a proposed solution for decision making which takes into consideration the four above-mentioned prevalent challenges in decision making when it comes to prioritizing the competing projects in an organization.

Table 14  
Result of sensitivity analysis for different scenarios.

<table><tr><td rowspan="2"></td><td colspan="6">Scenarios</td></tr><tr><td>Original case data</td><td>Equal weights</td><td>Financial</td><td>Stakeholders</td><td>Project</td><td>Learning</td></tr><tr><td>Z-ARAS</td><td>3.639</td><td>3.954</td><td>2.957*</td><td>3.257</td><td>3.664*</td><td>3.043</td></tr><tr><td>Z-CODAS</td><td>3.739</td><td>3.411*</td><td>3.550</td><td>2.832*</td><td>4.064</td><td>2.746</td></tr><tr><td>Z-COPRAS</td><td>3.950</td><td>4.661</td><td>3.379</td><td>3.236</td><td>3.796</td><td>3.604</td></tr><tr><td>Z-MABAC</td><td>4.175</td><td>3.454</td><td>2.875</td><td>3.336</td><td>3.807</td><td>2.643*</td></tr><tr><td>Ensemble</td><td>3.543*</td><td>3.757</td><td>3.757</td><td>3.004</td><td>3.671</td><td>2.693</td></tr></table>

Our proposed approach is largely MCDM-driven. While MCDM methods, by nature, cannot necessarily guarantee an absolute optimal decision [19–21], and also, in many cases, a full objective validation of the outcome is not feasible/relevant (due to absence of a baseline model) [4,49,77], they are still helpful in supporting decision makers to arrive at more informed decisions. We also acknowledge the higher level of effort required for decision making based on MCDM approaches compared to faster decision making based on DMs’ intuition, skills, or experience (with no systematic approach). Nevertheless, the more sys tematic and careful structuring and examination of the decision problem via MCDM models can potentially support the DMs in the process of decision making, help them to avoid making decisions based on habit only, increase the trust in the decision, and eventually reduce the pos sibility of post-decision regret [19,20]. These may justify the cost of extra effort required for MCDM-driven decision making. Further, to address the effort concern, we were mindful of the balance between effort and effectiveness when we designed our proposed hybrid model by making sure that human involvement is as minimal as possible. The last step in our process for which human involvement is required is when decision makers are asked to compare the criteria for the projects (which is an inevitable task in any MCDM analysis) (in the beginning of step 3.3.1). All steps after that are fully automatic and programmatic with no human involvement required. The decision makers do not need to do anything during the time when the four MCDM analyses, ensemble ag gregation, and sensitivity analysis are being conducted (one of the rea sons that we selected ensemble ranking – over some alternative aggregation methods – was that ensemble ranking works with no human engagement). That being said, we believe that the balance between effort and effectiveness is reasonable in our proposed method and is not over and above similar methods available in the literature (e.g., [1,4,49,77]).

One of the additions of our proposed model to the literature is incorporating z-numbers theory into the decision-making process in the context of project prioritization, which not only allows the domain ex perts to make decisions under uncertainty and ambiguity, but also captures the reliability of their decisions by giving them the opportunity to express their confidence and level of sureness in all evaluations throughout the process. This, to the best of our knowledge, so far has been absent in the literature of project prioritization since prior studies $\left( \mathbf { e } . \mathbf { g } . , \ \left. [ 1 , 9 , 1 4 - 1 6 , 2 3 \right] \right)$ mostly use fuzzy logic which is capable of capturing uncertainty, but not reliability [37]. Considering the level of sureness of the experts during the decision making process is important given that reliability or sureness is a natural part of human decision making and should be factored in when developing decision-making models for project selection.

Incorporating ZQFD into our proposed models enabled us to identify and prioritize the selection criteria in a systematic manner. However, it should be noted that other alternative approaches for problem struc turing do exist in the literature such as Strategic Options Development and Analysis (SODA) or Soft Systems Methodology (SSM) (sometimes broadly categorized under the umbrella term of soft operation research or soft OR) [81]. The intention of our research was not to compare QFD with other counterparts, but rather to propose and illustrate how sys tematic approaches for problem structuring could be combined with other initiatives (e.g., z-number theory, MCDM methods, sensitivity analysis, etc.) during the decision making process to assist and support the DMs in the challenging task of project prioritization (focusing on the four challenges that we addressed in our study).

In our proposed approach, we addressed the issue of decision robustness by considering several ranking methods (instead of only one) and then assessed robustness through sensitivity analysis. What our approach offers is evaluating robustness to changes in criteria weight (in situations where DMs may change their opinion slightly) and assesses robustness to the four decision making methods employed in the approach, but not to decision making methods in general. Conceivably, the boundary of robustness evaluation in our paper is limited to the changes in the weights from among the four methods used in the paper, and does not (and cannot) assess robustness to other methods. None theless, our approach offers insights on how robustness to other methods can be evaluated in the same way.

## 6.1. An elaboration on the trustworthiness of the proposed method

Since 1970, MCDM research has developed extensively due to its capability in responding to complex practical decision problems involving multiple and conflicting criteria and objectives [82]. Numerous MCDM-based solutions have been proposed in the past few decades across various contexts and settings, each claiming that their approach is the one to use. This concerns some users who ask how well does a MCDM solution perform and how valid is its ranking and order? In responding to this question, many MCDM scholars argue “that it is all a subjective matter (the judgments, the numbers used to represent them), why bother validating any method?” [82 ,p.2]. However, others still emphasize that some elements of evaluation are essential when a MCDM-based solution is proposed to address a practical problem. This is particularly relevant when the decision is complex and in addition in volves Benefits, Opportunities, Costs, and Risks (BOCR) [82]. To address this, Thomas Saaty, one of the highly recognized names in decision making science and the inventor, architect, and primary theoretician of AHP, introduced 16 criteria that may be used to evaluate trustworthi ness of MCDM-based solutions. He defines trustworthiness as “the quality of a method and its findings that make it noteworthy to decision makers” [82, p12]. In Table 15, our proposed method comes under scrutiny in light of these sixteen criteria.

Given that our proposed solution is rated ‘high’ in a large majority of criteria in Saaty and Ergu’s framework, it can be considered as a trust worthy and valid solution for prioritizing projects when uncertainty, reliability or sureness, handling a large set of prioritized selection criteria, and robustness are four concerns to be addressed simultaneously.

## 7. Conclusion and future research

This study proposed a hybrid approach to simultaneously conside some aspects, or challenges, of decision making in real-world scenarios for prioritizing projects: 1) uncertainty and fuzziness in decision mak ing, 2) reliability (extent of sureness) of decision makers in their judg ments, 3) accounting for a large number of selection criteria and identifying them systematically, and 4) the robustness of decision making to slight changes in experts’ opinions. The first and second as pects were achieved by incorporating the concept of z-numbers into our proposed model (for the first time in the literature of project selection) which is able to account for both uncertainty and reliability. The third aspect was met by using ZQFD which enables systematic and rigorous analysis and identification of selection criteria. The last aspect – robustness to changes in the weights – was addressed by employing several MCDM techniques and then aggregating them using the ensemble ranking method. Sensitivity analysis subsequently determines the most robust ranking. By implementing the proposed method in a real-world organization with twenty IT projects, we illustrated how our approach might be used in practice to assist managers and practitioners in prioritizing competing projects given the restrictions and re quirements of real-world problems.

We note three limitations of our study that open opportunities for future research. First, while we accounted for uncertainty and level of sureness in our proposed model by adopting z-numbers theory, the prevalent notion of hesitation in decision making, where a decision maker is unable to select among alternatives and thus wants to give a score to both alternatives [84], was not addressed. We call for future research to use emerging developments in fuzzy logic literature, such as

Table 15  
An elaboration on the trustworthiness of the proposed method based on the Saaty and Ergu framework [82].

<table><tr><td>Evaluation criteria introduced by Saaty and Ergu (2015) [82]</td><td>Evaluation of our proposed method</td><td>Justification/discussion</td></tr><tr><td>“1) Simplicity of execution:Low: logic is complicated and can only be used by professional decision makers or experts.Medium: one needs to put much efforts to learn the method.High: the method can be easily understood and implemented by most users in practice.”</td><td>High</td><td>While any structured systematic decision (including our MCDM-driven approach) requires more execution effort than intuitive decision making, our approach can be easily understood and executed any lay DMs in organizations with no need to have specific expertise in decision science and theory.Furthermore, the computations of our method are supported by an automated computerized system to minimize the users&#x27; execution effort.To obtain external opinion on this criterion, we asked the four DMs and the senior manager to rate their experience with our method in terms of ease of use (1: super easy, 10: super difficult). On average, they rated the model 3.2/10 which can be considered as reasonably easy.</td></tr><tr><td>“2) Comprehensive structure - breadth and depth:Low: Method contains only a few criteria without decomposition with necessary detail.Medium: Structure is neither broad nor deep.High: structure is not only broad (contains a number of distinct criteria) but also deep (criteria can be broken down to sub-criteria).”</td><td>High (breadth), Medium (depth)</td><td>Our proposed method is strong in terms of breadth of analyses as it can handle as many project selection criteria as an organization may need (since we have not used techniques that have limited ability to handle large numbers of criteria such as DEA – as used by [1,9]). In terms of depth (hierarchical decomposition), while we did not explicitly talk about criteria decomposition in our proposed solution, BWM is inherently capable of covering decomposition by making adjustments to the formulae in section 3.2.1 (see [83]). Hence, we rank it as &#x27;medium&#x27;.</td></tr><tr><td>“3) Comprehensive structure consisting of merit substructures:NA: Method does not involve BOCR analysis.Low: Method only considers one to two of the BOCR.Medium: if it involves three parts of BOCR.High: if it considers all the BOCR merits.”</td><td>Low</td><td>The ZQFD part of our proposed method explicitly considers two sets of criteria from BOCR: benefits and costs. While the other two group of BOCR (opportunities and risks) may be captured implicitly under benefits and costs, we evaluate our method as being &#x27;low&#x27; in this feature since only two BOCR categories are explicitly included.</td></tr><tr><td>4) Logical, mathematical procedure:Low: Method involves only a simple mathematical logical procedure (e.g., arithmetic value utility).Medium: Method uses references sequence or relative difference to rank alternatives.High: Method uses a pairwise comparison technique to determine the dominance of one criterion over another.”</td><td>High</td><td>Our method uses pairwise comparison of the decision making factors (using ZQFD and ZBWM) so the method is considered to be &#x27;high&#x27; in this feature.</td></tr><tr><td>“5) Justification of the approach-justifiable axiomsLow: Method involves no mathematics with axioms to justify its use.Medium: Method involves axioms only in part.High: Method involves complete and logical axioms.”</td><td>High</td><td>A method is justifiable if it has a theory based on meaningful axioms [82]. As we use a combination of recognized MCDM methods and tools, the mathematics behind the method is highly justifiable and logical. For example, the use of QFD for analyzing the decision making factors or using a range of MCDM method for ranking and aggregation are well supported in the literature. Hence, the axioms of the model are complete and logical.</td></tr><tr><td>“6) Scales of measurement:Low: Method uses nominal or ordinal scale.Medium: Method uses interval or ratio scales.High: Method uses absolute scales.”</td><td>High</td><td>The evaluations by the DMs are in form of fuzzy linguistic variables which can cover any type of scales (ordinal, interval, absolute, etc) using relevant and appropriate fuzzy membership number according to the needs of the users. Thus, this feature can be ranked as &#x27;high&#x27;.</td></tr><tr><td>“7) Synthesis of judgments with merging functions:Low: Method is synthesized by averaging weights.Medium: a simple weighted method is used.High: a rigorous merging function with reasonable weights is used.”</td><td>High</td><td>Our proposed model takes into consideration the aggregation of judgments and evaluations by individual DMs to achieve a group decision. In this regard, we expand BWM to group ZBWM (one of the side contributions of our paper). This is a rigorous merging function beyond simple averaging or conventional weighted aggregation.</td></tr><tr><td>“8) Ranking of tangibles:NA: Method does not involve some kind of ranking of the alternatives.Low: Method uses a nominal scale.Medium: Method uses an ordinal scale, High: Method uses a cardinal scale to rank alternatives.”</td><td>High</td><td>According to Saaty and Ergu [82], a good decision making solution ranks the alternatives according to evaluation of certain criteria and produces the total preorder of alternatives by balancing the preferences on all the criteria (rather than simply comparing alternatives directly against one another). Our proposed approach does so precisely and uses cardinal scales (after defuzzification).</td></tr><tr><td>“9) Generalization to ranking of intangiblesLow: Method simply quantifies intangibles by assigning arbitrary ordinal numbers.Medium: transforms intangibles into cardinal numbers by using an interval, ratio, or absolute scale.High: assesses intangibles by using pairwise comparison technique to consider their relative importance.”</td><td>High</td><td>Many of the selection criteria in the context of project prioritization are intangible (see Table 4). Our proposed model uses fuzzy linguistic variables which allow assessing intangibles by pairwise comparison of their relative importance, as well as assessing the level of sureness of DMs (another intangible). Thus, the method is ranked &#x27;high&#x27; according to this feature of evaluation in Saaty and Ergu&#x27;s framework.</td></tr><tr><td>“10) Rank preservation and reversal:Low: Method simply assumes rank preservation.Medium: Method basically deals with both rank preservation and rank reversal.High: Method is capable of interpreting the reasons for rank preservation and rank reversal and implements the idea in its procedures.”</td><td>Low</td><td>Rank preservation means that the order previously determined among the alternatives remains unchanged when a new alternative is added (or deleted) [82]. Otherwise, rank reversal exists. We did not undertake this analysis in our method, so this feature is ranked as &#x27;low&#x27;.</td></tr><tr><td>“11) Sensitivity analysis:Low: Method involves only a single parameter.Medium: Method works on two to three parametersHigh: Method is capable of assessing more than three parameters.”</td><td>High</td><td>Sensitivity analysis is an integrated part of our proposed solution. The mechanism we used for sensitivity analysis evaluates changes to parameters one at a time but eventually combines them together. In addition, we used scenario analysis which allows changing weights simultaneously across several criteria. Thus, all in all, we evaluate our method as &#x27;high&#x27; in this feature since it assesses sensitivity to all criteria (more than three).</td></tr></table>

(continued on next page)

Table 15 (continued )

<table><tr><td>Evaluation criteria introduced by Saaty and Ergu (2015) [82]</td><td>Evaluation of our proposed method</td><td>Justification/discussion</td></tr><tr><td>“12) Validation of decision problems:Low: Method does not involve justifiable validation of some kind.Medium: Method only uses examples with tangibles to validate its procedures.High: Method uses real-world examples with intangibles to validate its effectiveness.”</td><td></td><td>An ideal way to validate a scientific solution is to show that the outcomes match known results. However, in many MCDM-based decision making solutions, even in mainstream ones such as AHP itself, it is not pragmatically possible to do so since there is no real-world outcome (i.e., a guaranteed optimal best ranking), or even a baseline model, to compare to. Alternatively, and similar to many prior studies, we applied our proposed model in a real-world case study to demonstrate that the approach works and can assist decision makers to come to a collective group decision for a complex problem of project prioritization under the pressure of four challenges of real-world decision making (uncertainty, reliability or sureness, handling a large set of prioritized selection criteria, and robustness). While this is not a fully objective validation (as we may see in other fields), it shows the applicability and usability of the approach.In addition, to further examine the performance of our hybrid model, we presented the ultimate ranking of the project (obtained via executing our full model i.e., last column of Table 12) along with the ranking of the projects without the reliability (sureness) element (i.e., column 2 in Table 13) as well as a group ranking obtained from simple averaging of individual rankings by the DMs. The titles of the rankings were not revealed to the DMs. We asked them to choose the ranking that they deem more suitable to them based on what they know about the organization and projects. Three out of the four DMs (75%) chose the ranking produced by our model (and one selected simple averaging). While we acknowledge that this outcome is subjective to the opinion of the DMs in our case, to some extent it depicts that the ranking (or the group decision) produced via our model (which takes several aspects of human decision making into consideration at the same time, including the sureness of people with their judgments during the process) produces better results than simple averaging or the ranking that exclude reliability (as evident by our case study). Given the above, it seems ‘medium’ is a reasonable evaluation for our model in this feature of Saaty and Ergu’s framework (noting that the model is evaluated by an example, i.e., a case study).</td></tr><tr><td>“13) Prediction of the outcome of decisions with intangibles (the capability to predict preferences):Low: Method just plays with numbers by pretending what it does is correct and can be taken for granted.Medium: Method does a credible job without the need for much explanation or argument.High: if it directly involves prediction of a decision (the predicted results match the outcome of that decision).”</td><td>Medium</td><td>The notion of prediction is not applicable in our study since there is no actual practical data with which to check the accuracy of the prediction.Nevertheless, the applicability and usability of the model to assist the decision makers in addressing a complex issue was demonstrated via a case study. Thus, ‘medium’ seems a reasonable level for this feature, noting that the model does the job as illustrated by the case study.</td></tr><tr><td>“14) Generalizability to dependence and feedback:NA: Method does not involve feedback in the process of making a decision.Low: either dependence or feedback is used indirectly.Medium: both partially influence the results of decision making; High: they are regarded as parts of the inputs of the decision itself that can affect the results of that decision.”</td><td>NA</td><td>Our proposed method does not involve feedback in the process of making the decision.</td></tr><tr><td>“15) Applicability to conflict resolution:Low: the method uses a simple mathematical compensation technique to make tradeoffs in a conflict.Medium: Method uses an analytical method for dealing with conflict resolution.High: Method can provide the best solution for a group conflict that is understandable, acceptable, practical, and flexible.”</td><td>High</td><td>Our proposed approach responds to the conflicting opinions among the DMs by using a systematic approach to aggregate the results and reach a collective group agreement. In particular, a senior manager is involved in the model to rate the credibility of the expert which means the opinion of the more credible expert will have a stronger impact on the final output in case of conflicts. This is done as part of group ZBWM (an expansion of conventional BWM in our paper).</td></tr><tr><td>“16) Trustworthiness of the approach:Low: Method uses cardinal measurement model with a simple structure.Medium: Method uses cardinal measurement model but does not provide rigorous mathematical axioms.High: Method uses a cardinal measurement model with a mathematical logical procedure and mathematical axioms.”</td><td>High</td><td>Trustworthiness has been defined as “that quality of a method and its findings that make it noteworthy to decision makers” [82, p12]. Our proposed method deals with cardinal measurements following rigorous mathematical axioms and is based upon well established and proven theories and techniques in scientific and systematic decision making (from QFD to z-numbers theory, BWM, sensitivity analysis, etc.). Therefore, this feature is rated ‘high’.”</td></tr></table>

hesitant fuzzy numbers (HFN) [84] to synthesize solutions for hesitant decision making in the use case of identifying and prioritizing profitable projects.

Second, while in our study we accounted for the robustness of the MCDM and the aggregation method used in the paper (via sensitivity analysis and scenario analysis), there is still a need for a separate and focused standalone study on the robustness of MCDM methods (when they are coupled with z-numbers theory). Currently, the notion of robustness in fuzzy MCDM is well explored in the literature (e.g., [60]) but the concept is largely left un-researched for z-number MCDM. We therefore call for future research on the robustness of Z-MCDM covering a comprehensive range of MCDM methods including the four methods explored in the present study together with other techniques such as TOPSIS, Grey Relational Analysis (GRA), Multiple Multi-Objective Optimization based on a Ratio Analysis (MULTIMOORA), Weighted Aggregated Sum Product Assessment (WASPAS), etc.

Third, as Fig. 4 depicts, the ranking of some projects fluctuates more than the others across different MCDM techniques (e.g., P3, 12, 13). This is likely to be attributable to the formation of the weights when it comes to the algorithm behind each MCDM method. Careful assessment of this matter, however, is beyond the scope of the present study. A separate future work with appropriate objectives and research design is required for scrutiny into this finding.

## References

[2] I.N. Durbach, S. Algorta, D.K. Kantu, K.V. Katsikopoulos, O. <sup>¨</sup> S¸ ims¸ek, Fast and frugal heuristics for portfolio decisions with positive project interactions, Decis. Support. Syst. 138 (2020), 113399.

[3] J.C. Lourenco, A. Morton, C. A. B. eCosta, PROBE—a multicriteria decision support system for portfolio robustness evaluation, Decis. Support. Syst. 54 (1) (2012) 534–550.

[4] M.R. Asadabadi, O. Zwikael, The ambiguous proposal evaluation problem, Decis. Support. Syst. 136 (2020), 113359.

[5] C. Lin, P.-J. Hsieh, A fuzzy decision support system for strategic portfolio management, Decis. Support. Syst. 38 (3) (2004) 383–398.

[6] H. Eilat, B. Golany, A. Shtub, Constructing and evaluating balanced portfolios of R&D projects with interactions: a DEA based methodology, Eur. J. Oper. Res. 172 (3) (2006) 1018–1039.

[7] C.-C. Huang, P.-Y. Chu, Y.-H. Chiang, A fuzzy AHP application in government sponsored R&D project selection, Omega 36 (6) (2008) 1038–1052.

[8] F. Tiryaki, B. Ahlatcioglu, Fuzzy portfolio selection using fuzzy analytic hierarchy process, Inf. Sci. 179 (1) (2009) 53–69.

[9] A.H. Ghapanchi, M. Tavana, M.H. Khakbaz, G. Low, A methodology for selecting portfolios of projects with interactions and under uncertainty, Int. J. Proj. Manag. 30 (7) (2012) 791–803.

[11] F. Kucukbay, C. Araz, Portfolio selection problem: a comparison of fuzzy goa programming and linear physical programming, Int. J. Optimiz. Control: Theories Appl. (IJOCTA) 6 (2) (2016) 121–128

[12] M. Jim´enez, A. Bilbao-Terol, M. Arenas-Parra, A model for solving incompatible fuzzy goal programming: an application to portfolio selection, Int. Trans. Oper. Res. 25 (3) (2017) 887–912.

[13] S. Sivzattian, B. Nuseibeh, Linking the selection of requirements to market value: A portfolio-based approach, in: Proceedings of 7th International Workshop on Requirements Engineering: Foundation for Software Quality (REFSQ 2001), 2001.

[14] M. Tavana, M. Keramatpour, F.J. Santos-Arteaga, E. Ghorbaniane, A fuzzy hybrid project portfolio selection method using data envelopment analysis, TOPSIS and integer programming, Expert Syst. Appl. 42 (22) (2015) 8432–8444.

[15] P. Akbari, H. Jafarzadeh, J.H. Dahooie, Prioritising IT projects: combination of fuzzy QFD and ARAS to address criteria multiplicity challenge, in: Pacific Asia Conference on Information Systems (PACIS), 2019.

[16] M. Tavana, G. Khosrojerdi, H. Mina, A. Rahman, A new dynamic two-stage mathematical programming model under uncertainty for project evaluation and selection, Comput. Ind. Eng. 149 (2020), 106795.

[17] V. Mohagheghi, S.M. Mousavi, M. Mojtahedi, S. Newton, Evaluating large, hightechnology project portfolios using a novel interval-valued Pythagorean fuzzy set framework: an automated crane project case study, Expert Syst. Appl. 162 (2020), 113007.

[18] S.H. Zanakis, A. Solomon, N. Wishart, S. Dublish, Multi-attribute decision making: a simulation comparison of select methods, Eur. J. Oper. Res. 107 (3) (1998) 507–529.

[19] M.B. Barfod, An MCDA approach for the selection of bike projects based on structuring and appraising activities, Eur. J. Oper. Res. 218 (3) (2012) 810–818.

[20] V. Belton, T. Stewart, Multiple Criteria Decision Analysis: An Integrated Approach, Springer Science & Business Media. 2002.

[21] E. Løken, Use of multicriteria decision analysis methods for energy planning problems, Renew. Sust. Energ. Rev. 11 (7) (2007) 1584–1595.

[22] LA. Zadeh. Fuzzy sets, Inf, Control. 8 (3) (1965) 338–353.

[23] J. Heidary, H. Jafarzadeh, P. Akbari, Prioritising IT projects: A multi-method approach, in: presented at the Pacific Asia Conference on Information Systems (PACIS). 2020

[24] J. Antucheviciene, A. Zakarevicius, E.K. Zavadskas, Measuring congruence of ranking results applving particular MCDM methods, Informatica 22 (3) (2011) 319-338.

[25] P. Akhavan, S. Barak, H. Maghsoudlou, J. Antuchevičienė, FOSPM-SWOT for strategic alliance planning and partner selection: case study in a holding car manufacturer company, Technol. Econ. Dev. Econ. 21 (2) (2015) 165–185.

[26] M. Varmazyar, M. Dehghanbaghi, M. Afkhami. A novel hybrid MCDM model for performance evaluation of research and technology organizations based on BSC approach, Eval. Progr. Plann. 58 (2016) 125–140.

[27] C.-W.R. Lin, H.-Y.S. Chen, A fuzzy strategic alliance selection framework for supply chain partnering under limited evaluation resources, Comput. Ind. 55 (2) (2004) 159-179.

[28] C.-T. Chen, H.-L. Cheng, A comprehensive model for selecting information system project under fuzzy environment, Int. J. Proj. Manag. 27 (4) (2009) 389–399.

[29] E.E. Karsak, M. Dursun, An integrated supplier selection methodology incorporating QFD and DEA with imprecise data, Expert Syst. Appl. 41 (16) (2014) 6995–7004.

[30] L. Wang, Y.-K. Juan, J. Wang, K.-M. Li, C. Ong, Fuzzy-QFD approach based decision

[31] H. Khademi-Zare, M. Zarei, A. Sadeghieh, M.S. Owlia, Ranking the strategic actions of Iran mobile cellular telecommunication using two models of fuzzy QFD, Telecommun, Policy 34 (11) (2010) 747–759.

[32] H.A. Tayali, M. Timor, Ranking with Statistical Variance Procedure Based Analytic Hierarchy Process, 2017.

[33] A. Mohtashami, B.M. Ghiasvand, Z-ERM DEA integrated approach for evaluation of banks & financial institutes in stock exchange, Expert Syst. Appl. 147 (2020), 113218.

[34] H. Aboutorab, M. Saberi, M.R. Asadabadi, O. Hussain, E. Chang, ZBWM: the Z number extension of best worst method and its application for supplier development, Expert Syst. Appl. 107 (2018) 115–125.

[35] F. Hujainah, R.B.A. Bakar, M.A. Abdulgabber, StakeQP: a semi-automated stakeholder quantification and prioritisation technique for requirement selection in software system projects, Decis. Support. Syst. 121 (2019) 94–108.

[36] N.M. Arratia, F. Lόpez, S. Schaeffer, L. Cruz-Reyes, Static R&D project portfolio selection in public organizations, Decis. Support. Syst. 84 (2016) 53–63.

[37] L.A. Zadeh, A note on Z-numbers, Inf. Sci. 181 (14) (2011) 2923–2932.

[38] L.A. Zadeh, Fuzzy sets as a basis for a theory of possibility, Fuzzy Sets Syst. 1 (1978) 3–28.

[39] H. Dincer, U. Hacioglu. E. Tatoglu, D. Delen, A fuzzy-hybrid analytic model to assess investors' perceptions for industry selection, Decis. Support. Syst. 86 (2016) 24–34.

[40] A. Azadeh, R. Kokabi, Z-number DEA: a new possibilistic DEA in the context of Z numbers, Adv. Eng. Inform. 30 (3) (2016) 604–617.

[41] B. Kang, D. Wei, Y. Li, Y. Deng, A method of converting Z-number to classical fuzzy number, J. Inform. Comput. Sci. 9 (2012) 703–709.

[42] S. Hendiani, M. Bagherpour, A. Mahmoudi, H. Liao, Z-number based earned value management (ZEVM): a novel pragmatic contribution towards a possibilistic costduration assessment, Comput. Ind. Eng. 143 (2020), 106430.

[43] Y. Akao, G.H. Mazur, The leading edge in QFD: past, present and future, Int. J. Qual. Reliab. Manag. 20 (1) (2003) 20–35.

[44] F.R. Lima-Junior, L.C.R. Carpinetti, A multicriteria approach based on fuzzy QFD for choosing criteria for supplier selection, Comput. Ind. Eng. 101 (2016) 269–285.

[45] L.-H. Chen, W.-C. Ko, F.-T. Yeh, Approach based on fuzzy goal programing and quality function deployment for new product planning, Eur. J. Oper. Res. 259 (2) (2017) 654–663.

[46] L.-K. Chan, M.-L. Wu, A systematic approach to quality function deployment with a full illustrative example, Omega 33 (2) (2005) 119–139.

[47] M.P. Amiri, Project selection for oil-fields development by using the AHP and fuzzy TOPSIS methods, Expert Syst. Appl. 37 (9) (2010) 6218–6224.

[48] C. Song, J.-Q. Wang, J.-B. Li, New framework for quality function deployment using linguistic Z-numbers, Mathematics 8 (2) (2020) 224.

[49] W.-C.J. Hsu, J.J. Liou, H.-W. Lo, A group decision-making approach for exploring trends in the development of the healthcare industry in Taiwan, Decis. Support. Syst, 141 (2021). 113447.

[5o] S. Barak, J.H. Dahooei. A novel hybrid fuzzy DEA-fuzzy MADM method for airlines safety evaluation, J. Air Transp. Manag. 73 (2018) 134–149.

[51] M. Mohammadi, J. Rezaei, Ensemble ranking: aggregation of rankings produced by different multi-criteria decision-making methods, Omega (United Kingdom) 96 (2020), 102254.

[52] Y. Peng, G. Wang, H. Wang, User preferences based software defect detection algorithms selection using MCDM, Inf. Sci. 191 (2012) 3–13.

[53] M.E. Banihabib, F. Hashemi, M.H. Shabestari, A framework for sustainable strategic planning of water demand and supply in arid regions, Sustain. Dev. 25 (2017) 254–266.

[54] G. Kou, Y. Lu, Y. Peng, Y. Shi, Evaluation of classification algorithms using MCDM and rank correlation. Int. J. Inf. Technol, Decis, Mak, 11 (2012) 197–225

[55] Y. Peng, G. Kou, G. Wang, Y. Shi, FAMCDM: a fusion approach of MCDM methods to rank multiclass classification algorithms, Omega 39 (6) (2011) 677–689.

[56] A. Jahan, M.Y. Ismail, S. Shuib, D. Norfazidah, K.L. Edwards, An aggregation technique for optimal decision-making in materials selection, Mater. Des. 32 (2011) 4918–4924.

[57] I. Contreras, Emphasizing the rank positions in a distance-based aggregation procedure, Decis. Support. Syst. 51 (2011) 240–245.

[58] Y.M. Wang, J.B. Yang, D.L. Xu, A preference aggregation method through the estimation of utility intervals, Comput. Oper. Res. 32 (2005) 2027–2049.

[59] A. Tayal, A. Gunasekaran, S.P. Singh, R. Dubey, T. Papadopoulos, Formulating and solving sustainable stochastic dynamic facility layout problem: a key to sustainable operations, Ann. Oper. Res. 253 (2017) 621–655.

[60] S. Barak, S. Javanmard, Outsourcing modelling using a novel interval-valued fuzzy quantitative strategic planning matrix (QSPM) and multiple criteria decisionmaking (MCDMs). Int, J. Prod, Econ, 222 (2020). 107494.

[61] E.K. Zavadskas. Z. Turskis. A new additive ratio assessment (ARAS) method in multicriteria decision-making. Technol. Econ, Dev. Econ. 16 (2) (2010) 159–172

[62] M. Keshavarz-Ghorabaee, E.K. Zavadskas, Z. Turskis, J. Antucheviciene, A new combinative distance-based assessment (CODAS) method for multi-criteria decision-making, Econ. Comput. Econ. Cybernet. Stud. Res. 50 (2016) 25–44.

[63] E. Zavadskas. A. Kaklauskas. Determination of an efficient contractor by using the new method of multicriteria assessment, in International Symposium for “The Organization and Management of Construction”, Shap. Theory Pract. 2 (1996) 94–104.

[64] D. Bozanic. D. Tešić. A. Milić. Multicriteria decision making model with Z-numbers (2) (2020) 19–36.

[65] Q. Cao, M.O. Esangbedo, S. Bai, C.O. Esangbedo, Grey SWARA-FUCOM weighting method for contractor selection MCDM problem: A case study of floating solar panel energy system installation. Energies 12 (2019).

[66] J. Rezaei, Best-worst multi-criteria decision-making method, Omega (United Kingdom) 53 (2015) 49–57

[67] X. Mi, M. Tang, H. Liao, W. Shen, B. Lev, The state-of-the-art survey on integrations and applications of the best worst method in decision making: why, what, what for and what’s next? Omega (United Kingdom) 87 (2019) 205–225.

[68] M.A. Alsalem, et al., Systematic review of an automated multiclass detection and classification system for acute Leukaemia in terms of evaluation and benchmarking, open challenges, issues and methodological aspects, J. Med. Syst. 42 (2018) ed.

[69] A.K. Yazdi, P.F. Wanke, T. Hanne, E. Bottani, A decision-support approach under uncertainty for evaluating reverse logistics capabilities of healthcare providers in Iran, J. Enterp. Inf. Manag. 33 (5) (2020) 991–1022.

[70] N.G. Mokhtarzadeh, H.A. Mahdiraji, V. Jafari-Sadeghi, A. Soltani, A.A. Kamardi, A product-technology portfolio alignment approach for food industry: a multicriteria decision making with z-numbers, Br. Food J. 122 (12) (2020) 3947–3967.

[71] W. Pedrycz, P. Ekel, R. Parreiras, Fuzzy Multicriteria Decision-Making: Models, Methods and Applications, John Wiley & Sons, 2011.

[72] A. Mahpour, Prioritizing barriers to adopt circular economy in construction and demolition waste management, Resour. Consery. Recycl. 134 (2018) 216–227.

[73] S. Guo, H. Zhao, Fuzzy best-worst multi-criteria decision-making method and its applications, Knowl.-Based Syst. 121 (2017) 23–31.

[74] V. Maliene, R. Dixon-Gough, N. Malys, Dispersion of relative importance values contributes to the ranking uncertainty: sensitivity analysis of multiple criteria decision-making methods, Appl. Soft Comput. 67 (2018) 286–298.

[75] J. Heidary Dahooie, A.S. Vanaki, H.R. Firoozfar, E.K. Zavadskas, A. Cere<sup>ˇ</sup> ˇska, An extension of the failure mode and effect analysis with hesitant fuzzy sets to assess the occupational hazards in the construction industry, Int. J. Environ. Res. Public Health 17 (4) (2020) 1442.

[76] K. Chatterjee, E.K. Zavadskas, J. Tamoˇsaitiene, ˙ K. Adhikary, S. Kar, A hybrid MCDM technique for risk management in construction projects, Symmetry 10 (2) (2018) 46.

[77] H.S. Kilic, A.E. Demirci, D. Delen, An integrated decision analysis methodology based on IF-DEMATEL and IF-ELECTRE for personnel selection, Decis. Support. Syst. 137 (2020), 113360.

[78] E. Mulliner, N. Malys, V. Maliene, Comparative analysis of MCDM methods for the assessment of sustainable housing affordability, Omega (United Kingdom) 59 (2016)146–156.

[79] N. Chitsaz, M.E. Banihabib, Comparison of different multi criteria decision-making models in prioritizing flood management alternatives, Water Resour. Manag. 29 (8) (2015) 2503–2525.

[80] R. Sun, Z. Gong, G. Gao, A.A. Shah, Comparative analysis of multi-criteria decisionmaking methods for flood disaster risk in the Yangtze River Delta, Int. J. Disaster Risk Reduct. 51 (2020), 101768.

[81] T. Seagriff, S. Lord, Soft operational research techniques: current and future uses, in: YoungOR 17 Conference. 2011. Citeseer.

[82] T.L. Saaty, D. Ergu, When is a decision-making method trustworthy? Criteria for evaluating multi-criteria decision-making methods. Int. J. Inf. Technol. Decis. Mak 14 (06) (2015).1171–1187

[83] J.H. Dahooie, A.R. Qorbani, T. Daim, Providing a framework for selecting the appropriate method of technology acquisition considering uncertainty in hierarchical group decision-making: case study: interactive television technology, Technol. Forecast. Soc. Chang. 168 (2021), 120760.

[84] M. Ranjbar, S.M. Miri, S. Effati, Hesitant fuzzy numbers with (α, k)-cuts in compact intervals and applications, Expert Syst. Appl. 151 (2020), 113363.

Hamed Jafarzadeh is a senior lecturer in Business Analytics and Information Systems at the School of Management, Massey University, New Zealand. He holds a PhD in Infor mation Systems from the University of New South Wales (UNSW), Australia. Prior to Massey University, he was an assistant professor of Information Systems at the University of Tehran, Iran, and an IT Project Manager and BPM Project Manager at the University of Oueensland, Australia. His main research interests include business analytics and big data analysis, decision making in IT context, IT project management with focus on agile ap proaches, business process management (BPM), and the role of behavioral traits in IT/IS use, e.g., IT mindfulness. He has published in high quality journals including Experts Systems with applications, Journal of Retailing and Consumer Services, Information Sys tems Management, Transportation Research Part F, Journal of Organizational Computing and Electronic Commerce, as well as leading IS conferences including, ICIS, ECIS, PACIS, HICSS and ACIS.

Jalil Heidary-Dahooie is Associate Professor at the Department of Industrial Manage ment, University of Tehran, Tehran, Iran. He has received BSc degree in Industrial Engi neering from the Sharif University of Technology and MSc and PhD degrees from th Department of Industrial Engineering of Amirkabir University of Technology. His research and teaching interests include areas such as Technology and knowledge Management, Multi Criteria Decision Making, Data Mining, and Business Process Management. He has published articles in various indexed journals including: Journal of Knowledge Manage ment, Expert Systems with Applications, Neural Computing & Applications, International Journal of Fuzzy Systems.

Pouria Akbari is a practitioner and researcher in the School of Management at the Uni versity of Tehran. He has received a BSc degree in Industrial Engineering from the Bu-Ali Sina University, Hamedan, Iran, and an MSc degree in Information Systems from the University of Tehran. His current research interests are Information System project man agement, Responsible Data Science, fuzzy mathematics, and decision science. He has published papers in high-quality journals (e.g., Expert Systems with Applications) and prestigious conferences in Information Systems, including Pacific Asia Conferences on Information System (PACIS).

Alireza Qorbani is a MSc graduate in the field of IT management from the University of Tehran and holds a BSc in industrial management from the International University of Imam Khomeini. He is currently working as a researcher in the field of Technology Management, Technology Assessment, Multi Criteria Decision Making, Fuzzy logic, and Text mining at the University of Tehran.
