---
otero_id: 15650
otero_key: "JKNDFKQW"
title: "An effective customization procedure with configurable standard models"
authors: "Hyun Jung Lee; Jae Kyu Lee"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.06.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 41 (2005) 262 – 278

www.elsevier.com/locate/dsw

# An effective customization procedure with configurable standard models

Hyun Jung Lee<sup>\*</sup>, Jae Kyu Lee

Graduate School of Management, Korea Advanced Institute of Science and Technology, 207-43, Cheongryang, Seoul 130-012, Korea

Received 12 June 2003; received in revised form 24 June 2004; accepted 24 June 2004 Available online 14 August 2004

## Abstract

In electronic catalogs, commodities such as computers and electronic equipment are specified as standard models although a variety of possible alternative specifications can exist as a combination of selected options; therefore, customized configurations are essential to support various customers with individual needs. Thus, the problem here is the selection of a standard model and reconfiguration with this selected model. An issue is that requirements may be fulfilled by more than one standard model. To develop an algorithm that can find the near minimum price without causing unacceptable computation effort, we devised the Standard Model Selection and Modification (SMSM) Algorithm. To establish the SMSM Algorithm, we propose the Concurrent Local Propagation procedure complemented with pruning capability owing to the nature of standard models. The effective strategies for selection of seed variables and stopping rules are devised through comparative experiments.

For the experiment, we use Dell’s personal computer (PC) products consisting of 42 standard models with 25 specification variables. The SMSM Algorithm is tested with 75 experimental cases, and we found that the most similar standard models could discover the minimum price only in 24 out of 75 cases and that the SMSM procedure could reduce the price by 6.04% from the one offered by the most similar standard models. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Configuration; Customization; Case-based reasoning; Comparison shopping; Constraint satisfaction problem

## 1. Introduction

There is an abundance of products in online shopping malls and comparison sites on the Internet. Products such as books and CDs on the Internet have fixed features without optional changes. However, many products such as computers, electronic equipment, and automobiles are customizable by customers to some extent. Hence, customer-driven customization is becoming more popular [8,42]. Since generative configuration is not easy for customers, manufacturers build a series of standard models to make the selection process simpler. With the standard models, customers select an appropriate one first and customize it by adding optional features. For instance, when a customer selects a notebook, s/he selects a favorite standard model first and probably enhances the CPU Speed. Under this circumstance, a concern is whether the same target specifications could have been achieved by another standard model possibly at a lower price.

Although the customer’s ultimate concern is configured specifications, most sites, nevertheless, merely display the standard models and options without appropriate support for reconfiguration with the standard models. For the effective display of comparable models [11], similarity-based ordering that is used in Case-Based Reasoning (CBR) is widely adopted [21]. Tabular comparisons [32] of particularly interesting models are complementarily provided to support detail comparisons. Some systems support the selection of optional features; however, compatibility check among selected features is rarely supported in the real world, although there are many studies done for this purpose [6,28,37,45]. Without appropriate assistance in checking compatibility during the reconfiguration of a standard model, there is no guarantee that the customized specifications are feasible. Although more than one standard model may be able to satisfy the customer’s requirements, customers do not know about it in advance, let alone which standard model provides the best price.

In this research, we develop an efficient algorithm to solve the Standard Model Selection and Modification (SMSM) problem. The SMSM Algorithm seeks the standard model and its modification, which can minimize its price while satisfying the customer’s requirements. For the selection of the standard model, a similarity measure can be used. For modification, the Constraint Satisfaction Problem (CSP) can be adopted. To solve the CSP effectively while resolving the conflicting goals, the Concurrent Local Propagation approach is proposed in this research. The approach needs to set an effective strategy of selecting seed variables which partition the CSP into multiple sub-CSPs. The algorithm also needs to prune the unnecessary propagation whose compatibility is assured by the nature of the standard model. Along with these features, the SMSM Algorithm needs to establish an effective stopping rule for iterative comparisons of standard models. By putting these ideas into a procedure, we devised the SMSM Algorithm. The procedure is demonstrated with the Personal Computer (PC) selection and reconfiguration problem at the Dell web site, and the performance is evaluated to discover best policies in establishing the algorithm.

To fulfill this aim, this paper is organized as follows. Section 2 reviews related literature and systems on customization and configuration. Section 3 specifies the product structure and customer’s requirements with the PC example. Section 4 describes the SMSM Algorithm formally, and Section 5 illustrates the algorithm with 42 standard models at the Dell site. Section 6 conducts a series of experiments to validate the performance of the SMSM Algorithm. Limitations and future research potentials are discussed in Section 7.

## 2. Review of customization and configuration

In this section, let us review the relevant literature on customization and configuration and identify the goal of this research more specifically.

## 2.1. Mass customization and configuration

In the late 1980s, the notion of mass customization was introduced to support customized products or services in high volumes at reasonably low costs [41]. Many business managers and researchers expected that generation of standardization would shift to generation of customization [24,40]. Typical strategies for customization are pure aggregation, personalization, and modification of standard models. To assist the modification with standard models, we need a configuration process, and this process is called reconfiguration. In finding the most preferred specifications and price, there are several approaches. First, if the functional requirements are given in advance, the aim of configuration is finding the specifications that meet the requirements at the lowest price. Second, the problem may be viewed from a different direction— find the model that maximizes the consumer surplus within a fixed budget. The implicit purpose of these two approaches is basically the same. However, since measuring the customer’s implicit surplus is very difficult, we adopt the first model in this research.

## 2.2. Generative configuration and reconfiguration with standard models

There are two types of configuration: Generative Configuration and Reconfiguration. Since the generative configuration requires heavy computation [7], it may be applied to the purchase of expensive industrial equipment in the B2B settings. For products in the B2C environment, standard models usually exist, which may be reconfigured [46].

Generative configuration starts from scratch searching for all possible solutions that satisfy the constraints among variables. The Constraint Satisfaction Problem (CSP) is the most popular approach for generative configuration. iLOG is a well-known package that solves the CSP’s search for the products closest to the customer’s requirements. It also suggests alternative solutions to customers while iteratively seeking optimization according to the customer’s decision criteria [16]. The generative constraint satisfaction is successfully applied to the configuration of the digital switching system [40]. However, the complexity of solving the CSP increases exponentially as the number of variables increases. For instance, even for the configuration of PCs with 25 variables, each of which has two values, we need to search for 2<sup>25</sup> combinations which become an NP-hard problem [7].

The rule-based approach can reduce the search space, but a huge rule base and heavy update are required. For example, the rule-based system XCON contained 30,000 components, 40% of which were updated each year [38]. AT&T DECS IV-2000 is another example of a rule-based configuration system for maintenance of telecommunication equipment [33].

To reduce the complexity of configuration, the introduction of standard models with flexible options is introduced [24]. Thus, this research aims to assist the standard model selection and reconfiguration for optional modification. Since the standard models are analogous to cases, the similarity-based retrieval approach in CBR can be used for the selection of the model closest to the customer’s requirements. Then, the CSP can be adopted for reconfiguration. The primary concern of CSP is the assurance of meeting compatibility constraints. For instance, <sup>d</sup>1.0 GHz<sup>T</sup> of CPU Speed is required to support the <sup>d</sup>20 GB<sup>T</sup> of Hard Disk Size (see the constraint C3 in Fig. 1).

## 2.3. Configuration systems

The configuration systems are developed using the general solvers of CBR and/or CSP, or Configuration Specific Tools. Typical configuration systems by the CBR approach are CLAVIER that designs autoclave loading [13], WPS which recommends wines [2], and READEE which assists in electrical engineering design [36]. Finding a similar case is not a difficult task in CBR, but automatic adaptation is usually very difficult. Four well-known adaptation approaches are substitution (CHEF [10], JUDGE [1] and MEDIA-TOR [22]), transformation (CASEY [23] and JULIA [14]), derivation (ARIES [3] and PRODIGY/ANAL-OGY [4]) [37] and composition (CADSYN [31] and DEJAVU [43]) [47].

iLOG is equipped with the generic solver for CSP and object oriented representation of variables. Using this facility, the iLOG configurator is devised as a model-based configuration system which represents parts of products in the objects with attributes such as the dimensions, price and constraints [17]. iLOG configurator searches for the first best model from the model base [16] and the iLOG solver configures the selected model. SAP’s Sales Configuration Engine supports the constraint-based product configuration [9], and Schenner and Fleischanderl [40] have developed a configuration tool named COCOS (2003). When users are not familiar with the configuration knowledge, the Salesman Expert System is necessary as a preprocessor of identifying the required specifications to map the customer’s requirements to the product specifications [26].

To check consistency during the reconfiguration process, the CSP approach can be adopted. Typical configuration systems that adopt the combination of the CBR and CSP approaches are COMPOSER which assists in the engineering design [37], CADRE in the architectural design [28], CBAR in the tour reservation [15], FASTrak-APT in the project planning of apartment construction [27] and WEBSELL in online sales [6,45].

## 2.4. Online customization sites with standard models

There are numerous online customization sites with standard models. Typical ones include Active-BuyersGuide (http://www.activebuyersguide.com), Dell (http://www.dell.com), PCOrder (http:// www.PCorder.com), ZDnet (http://www.zdnet.com/ computershopper), SalesBuilder (http://www. contractorssoftwaregroup.com/SalesBuilderPlus.htm), Transtec (transtec.de), Vobis (http://www.vobis.de), and Cisco (http://www.cisco.com). For instance, ActiveBuyersGuide computes the similarity of candidate products and sorts them by the level of similarity, ZDnet compares the interesting alternatives in tables, and Dell supports modification with options. However, these systems do not support compatibility checks although the methods are already well established in the literature [44].

http://www.Personalogic.com, a site that no longer exists, assisted in finding the full features of the configuration process including the high level expression of customer’s requirements [20,30,34], it considered the customer’s preference by receiving the weights of factors, it ordered the standard models by the preference satisfaction levels, and it offered a detailed comparison of the selected models in tabular contrast. We do not know the precise reason why this site vanished, but we guess that the site was not widely used although the technology was very sophisticated. This implies that studying the customer’s behavior in using configuration technology is critical for successful development.

## 2.5. Concurrent local propagation and tradeoff between conflicting goals

Since propagating all constraints in a CSP requires heavy computation [5], the concept of local propagation by local interchangeability is proposed in Freuder [19,44]. This concept is effective for reconfiguration of standard products. The neighborhood interchangeability [35] and neighborhood partial interchangeability [5] approaches could obtain the solutions in polynomial time.

Although there are powerful packages such as iLOG [16] that solves the CSP problems by obtaining one or all feasible solutions (in some literature, it is called consistent solutions [29,41]), it is not easy to pinpoint the most preferred configuration among all the feasible ones. One reason is that the preference revelation is difficult and time consuming as most Multiple Criteria Decision Making problems show [18]. iLOG iteratively seeks a better solution, but there is no guarantee in finding the optimal solution. The other reason is that the tradeoffs between conflicting goals are not effectively handled by most CSP algorithms. Thus, dealing with the tradeoff between one goal and another is very important to reduce the necessity of a priori revelation of customer’s preference.

To support the tradeoffs, we adopt the Concurrent Propagation approach which the author has proposed in an earlier study [26]. Concurrent Propagation means that multiple seed variables concurrently start to propagate the constraints with the goal values that the decision maker has given. In the configuration problem, the functional requirements correspond to the goal values. Each seed variable establishes a sub-CSP problem as propagation processes. If the value of a non-seed variable is propagated from more than one constraint, we need to check whether the variable has a value(s) that commonly meets both propagations. If the compatible value from one propagation is also compatible with the other, two (or more) concurrent sub-CSPs can be merged via the common value that satisfies both sub-CSPs. This implies that both goals set in the seed variables can be satisfied. However, if no common value for the two propagations exists, the decision maker has to decide which goal to choose to resolve the conflict. The beauty of this framework is that the system can compute the impact of choosing one goal over the other by reversely propagating from the winning goal to the yielding goal.

## 2.6. Research purpose revised

To find a specification from a set of reconfigurable standard models, we need to establish a procedure, named the SMSM Algorithm, considering the following issues:

(1) Selecting qualified standard models and sequencing the order of pairwise comparison. Establishing a reasonable stopping rule.

(2) Formulating the reconfiguration problem of standard models using the CSP model, and

Illustrative product structure with PCs

Monitor Size (in.) 15, 17, 19, 21 Refresh rate 54, 70, 85, 107 Resolution 1024 ( 768, 1600 ( 1200 Type Monitor, FD Trinitron, Digital Flat Panel Display

Video Card Size 16 MB, 32 MB, 64 MB Speed 2X, 4X Type Intel<sup>\_</sup>3D<sup>\_</sup>AGP 16 MB<sup>\_</sup>ATI\_Rage<sup>\_</sup>128<sup>\_</sup>pro 32 MB<sup>\_</sup>NVIDIA<sup>\_</sup>GeGorce2 32 MB<sup>\_</sup>NVIDIA<sup>\_</sup>TNT2<sup>\_</sup>M64 32 MB<sup>\_</sup>DDR<sup>\_</sup>ATI<sup>\_</sup>Radeon New<sup>\_</sup>32 MB<sup>\_</sup>DDR<sup>\_</sup>ATI<sup>\_</sup>Radeon 32 MB<sup>\_</sup>DDR<sup>\_</sup>NVIDIA<sup>\_</sup> Geforce2<sup>\_</sup>GTS 64 MB<sup>\_</sup>DDR<sup>\_</sup>NVIDIA<sup>\_</sup> Geforce2<sup>\_</sup>GTS 64 MB<sup>\_</sup>DDR<sup>\_</sup>NVIDIA<sup>\_</sup> Geforce2<sup>\_</sup>ULTRA

CD/DVD Speed 12X, 16X, 20X, 32X, 40X, 48X,ROM Drive 50X

Type CD-Rom Drive, Max Variable CD-ROM Drive, CD-RW Drive, DVD ROM Drive

Sound Card Sound Card Soundblaster 64 V PCI with Music Match Software SB Live! Value Digital with Music Match Software Turtle Beach Santa Cruz DSP Sound Card

Modem Modem V.90/56 K PCI DataFax Modem for Windows V.90/56 K Telephony Modem for Windows V.90/56 K Telephony Modem for Windows ME-Sound Option US Robotics v.90/56 K PCI Telephony Modem-Sound Option establishing the concurrent reasoning algorithm which propagates from multiple seed variables. Making the algorithm more efficient by pruning the propagation that is assured by the specifications of standard models.

Table 1  
Table 1 (continued )

<table><tr><td>Factors</td><td>Variables</td><td>Possible values</td></tr><tr><td>Network Card</td><td>Network Card</td><td>3COM®10/100 Fast Ethernet PC Card3Com HomeConnect 10 MB Phoneline PCI NIC Dell TrueMobile 1150 Wireless Networking</td></tr><tr><td>Limited warranty and support</td><td>Limited warranty and support</td><td>1 Year Parts and Onsite Labor (Next Business Day)+1 Year Phone Tech Support1 Year Parts and Onsite Labor_Years 2–3 Parts Delivery (Next Business Day)1 Year Next Business Day On-Site Parts and Labor_Years 2 and 3 Parts3 Years Parts Delivery and 1 Year Labor (Next Business Day)3 Years Parts_1 Year Onsite Labor (Next Business Day)+Lifetime Phone Tech Support3 Years Next Business Day On-Site Parts and Labor</td></tr></table>

(3) Testing the performance of the procedure with the example of PC configuration.

## 3. Specifications of product structure and requirements

Before we formalize the SMSM procedure, this section describes the specifications of product structure, constraints and CSP formulation, and the customer’s requirements with the example of PCs.

## 3.1. Product structure in variables and values

To demonstrate the configuration process, the products are specified by a set of variables, each of which has candidate values. Some variables may be grouped into a factor to categorize them. For instance, a PC has 25 variables categorized in 14 factors as depicted in Table 1. In the factor CPU, there are two variables: CPU Processor and CPU Speed. The variable CPU Processor has three possible symbolic values: Celeron, Pentium III, and Pentium IV; and the variable CPU Speed has seven numeric values that express the level of speed: 700 MHz, 866 MHz, 933 MHz, 1 GHz, 1.3 GHz, 1.4 GHz, and 1.5 GHz.

## 3.2. Constraints and CSP for configuration

In the illustrative CSP for the configuration of a PC, there are 12 compatibility constraints (denoted as Ci, i=1, . . ., 12) on the values of paired variables as depicted in Fig. 1. For instance, the constraint C1 restricts the compatibility between CPU Speed and Hard Disk RPM. The constraint expression ((700 MHz) (5400)) means CPU Speed of 700 MHz is required to use the Hard Disk of 5400 RPM.

The CSP is also graphically depicted in Fig. 2. The CSP graph consists of variables (bubbles) and undirected constraints (solid lines). Special types of variables are Must variables (double bubbles) and seed variables (rectangles) where the constraint propagations may start [15]. The Must variables are nonnegotiable, while others are negotiable. To solve the SMSM problem, we need to establish the rules that decide the seed variables, variable ordering, and value ordering [39].

## 3.3. Customer requirements as values and weights

A customer expresses his/her requirements by selecting a value (or values) for each variable as demonstrated on the screen in Fig. 3. The requirements correspond to the goals in CSP. The customer also assigns the weight of each variable by selecting a level in the rightmost column: Must, Very High, High, Low, Very Low. The weight level has a corresponding numeric value between 0 and 1: Must=1, Very High=0.8, High=0.6, Low=0.4, and Very Low=0.2. The variables in the Must level are nonnegotiable as mentioned earlier, while others are negotiable. When conflicts exist between goals, the DSS may suggest the impact of meeting one goal over the other so that decision maker can select the preferred tradeoff. However, to experiment with many cases with the automatic tradeoffs, we may assume that a goal with a lower weight yields to the one with a higher weight.

## 4. The standard model selection and modification algorithm

In this section, we propose the principles and procedure of the Standard Model Selection and Modification (SMSM) Algorithm.

## 4.1. Principles of the SMSM Algorithm

To solve the SMSM problem, our concern is how to support the customer in finding the optimal standard model and reconfigurating according to the customer’s requirements. To fulfill these purposes, we design the SMSM Algorithm with the following principles:

(1) Using the similarity measure for the selection of candidate standard models.

(2) Using the CSP algorithm, for adaptation with options (in other words, reconfiguration).

(3) In order to solve the CSP algorithm for reconfiguration efficient, we propose the concurrent reasoning approach which assists the tradeoffs between conflicting goals.

(4) Pruning constraint propagation when compatibility is assured by the feature of standard models.

(5) Developing a search procedure for finding an approximately optimal standard model by establishing a reasonable stopping rule.

Based on the above principles, the standard model selection process retrieves a set of qualified standard models similar to the customer’s requirements which is represented as the value and weight of each variable. Using the qualified standard models, the CSP model is formulated to find modified specifications. Let us call this model CSP for Modification of the Standard Model (CSP-MSM). The CSP-MSM model needs to be iteratively solved for each standard model to find the model which minimizes the cost of specifications while satisfying the requirements. Since the global optimal solution requires iteration with all candidate standard models, we need to establish a reasonable stopping rule. The iteration may stop at the most similar model, at the first local optimum, or after a certain number of iterations. To evaluate the achieved functional performance and required computational effort by each strategy, we conduct an experiment with the PC cases to compare the performance by the strategies as described in Section 6. Based on the experiment, we adopt the local optimum as the reasonable stopping rule.

![](/api/attachments/JKNDFKQW/fulltext/images/05e151abe2ea328c9d5a8925270fcc000a54b694ad3dc20edb67eabde89befeb.jpg)  
Fig. 1. Constraints for the compatibility among PC components.

![](/api/attachments/JKNDFKQW/fulltext/images/21374ddb4090f19c3f6dff7bcc9bb860e033dab694f52b28337b4722e6352404.jpg)  
Fig. 2. An illustrative CSP graph.

<table><tr><td>Factors</td><td>Variables</td><td>Values</td><td colspan="2">Preference(Weight)Must High ... Low</td></tr><tr><td rowspan="2">CPU</td><td>Processor</td><td>Pentium4</td><td></td><td></td></tr><tr><td>Speed</td><td>1Ghz</td><td></td><td></td></tr><tr><td rowspan="3">Memory</td><td>Size</td><td>256MB</td><td></td><td></td></tr><tr><td>Speed</td><td>133Mhz</td><td></td><td></td></tr><tr><td>Type</td><td>SDRAM</td><td></td><td></td></tr><tr><td rowspan="3">Hard Drive</td><td>Size</td><td>40GB</td><td></td><td></td></tr><tr><td>RPM</td><td>7200</td><td></td><td></td></tr><tr><td>Interface Method</td><td>ATA</td><td></td><td></td></tr><tr><td rowspan="4">Monitor</td><td>Size</td><td>17&quot;</td><td></td><td></td></tr><tr><td>R/R</td><td>70</td><td></td><td></td></tr><tr><td>Resolution</td><td>1024X768</td><td></td><td></td></tr><tr><td>Type</td><td>Monitor</td><td></td><td></td></tr><tr><td rowspan="3">Video Card Drive</td><td>Size</td><td>32MB</td><td></td><td></td></tr><tr><td>Speed</td><td>4X</td><td></td><td></td></tr><tr><td>Type</td><td>NVIDIA TNT2 M64</td><td></td><td></td></tr><tr><td rowspan="2">CD/DVD ROM Drive</td><td>Speed</td><td>48X</td><td></td><td></td></tr><tr><td>Type</td><td>Max Variable CD-ROM Drive</td><td></td><td></td></tr><tr><td colspan="2">Sound Card</td><td>SB Live! Value Digital with Music Match Software</td><td></td><td></td></tr><tr><td colspan="2">Speakers</td><td>PC Speakers</td><td></td><td></td></tr><tr><td colspan="2">Modem</td><td>US Robotics v.90/56K PCI Telephony Modem-Sound Option</td><td></td><td></td></tr><tr><td colspan="2">Network Card</td><td>3COM 10/100 Fast Ethernet PC Card</td><td></td><td></td></tr><tr><td colspan="2">Keyboard</td><td>Quiet Key Keyboard</td><td></td><td></td></tr><tr><td colspan="2">Mouse</td><td>MS IntelliMouse®</td><td></td><td></td></tr><tr><td colspan="2">Bundled Software</td><td>New Microsoft TM Works Suite 2001 with Money 2001</td><td></td><td></td></tr><tr><td colspan="2">Limited Warranty and Support</td><td>1Yr Parts &amp; Onsite Labor (Next Business Day)+1Yr Phone Tech Support</td><td></td><td></td></tr></table>

Fig. 3. An illustrative customer requirements.

Thus, the overall procedure of SMSM Algorithm can be summarized as follows:

(1) Filter out disqualified models according to the customer’s preemptive criteria denoted as must conditions.

(2) Compute the similarity of qualified standard models with the customer’s requirements.

(3) Select the most similar model as the first candidate model.

(4) If the current model satisfies the customer’s requirements, go to Steps 6. Otherwise, establish a CSP-MSM model with the current model.

(5) Propagate the constraints concurrently from multiple seed variables, while pruning whenever possible.

(6) Check the local optimal condition. Stop if the local optimality is reached or all candidate models are exhausted. Otherwise, go to Step 7.

(7) Reset the current model with the next similar model, and repeat Steps 4 Steps 5 Steps 6.

To formally describe the SMSM Algorithm, we define the notation as follows.

i: An index of the product model.

j: An index of the attribute variable in the product model specifications.

R: Customer’s requirements (noted as required goals) with $q$ variables. $R { = } [ r _ { 1 } , ~ r _ { 2 } , ~ . ~ . ~ . , ~ r _ { j } , ~ . ~ . ~ . , ~ r _ { q } ]$ where $r _ { j }$ implies the requirement of the jth variable. A variable with a required goal is called a goal variable, while a variable without such a restriction is known as a non-goal variable.

$S { = } [ S _ { 1 } , ~ S _ { 2 } , ~ . ~ . ~ . , ~ S _ { i } , ~ . ~ . ~ . , ~ S _ { p } ] \colon$ The universe of $p$ standard models. $s _ { i } { : } ~ \mathrm { A }$ standard (product) model i. ${ \cal S } _ { i } \mathrm { = } [ s _ { i 1 } , s _ { i 2 } , \ldots , s _ { i j } , \ldots , s _ { i q } ] \mathrm { : }$ Standard model i with $q$ variables, where $s _ { i j }$ implies the jth variable of the model $\pmb { S } _ { i }$

${ \cal M } _ { i } { = } [ m _ { i 1 } , m _ { i 2 } , . . . , m _ { i j } , . . . , m _ { i q } ] ; .$ A modified model of $s _ { i } ,$ , where $m _ { i j }$ implies the jth variable of the model $M _ { i } .$

$\scriptstyle { \pmb { d } } ( x , y ) = x - y \colon$ The distance of x from $y ;$ To make $0 { \leq } d ( x , y ) { \leq } 1$ , the original measures of x and $y$ are normalized to [0,1] scale. In the PC example, R, S, M are normalized accordingly. With the normalized scales, the bigger figure implies higher performance.

$D ( X , Y ) = [ d ( x _ { 1 } , y _ { 1 } ) , d ( x _ { 2 } , y _ { 2 } ) , . . . , d ( x _ { q } , y _ { q } ) ] \}$ : The distance vector from $X { = } [ x _ { 1 } , ~ . ~ . ~ . , ~ x _ { q } ]$ to $Y = [ y _ { 1 } , \ldots ,$ $y _ { q } ]$ . For instance, $D ( S _ { i } , R ) { = } [ d ( s _ { i 1 } , r _ { 1 } ) , ~ d ( s _ { i 2 } , r _ { 2 } ) ,$ $\pmb { d } ( s _ { i q } , r _ { q } ) ] .$ : The distance vector of the standard model $\pmb { S } _ { i }$ from the customer’s requirements $R ;$ and $D ( M _ { i } , R ) = [ d ( m _ { i 1 } , r _ { 1 } ) , ~ d ( m _ { i 2 } , r _ { 2 } ) , ~ . ~ . ~ . , ~ d ( m _ { i q } , r _ { q } ) ]$ : The distance vector of the modified model $M _ { i }$ from the customer’s requirements R.

W: Customer’s preference weights of variables. $W \mathrm { = } [ w _ { 1 } , \ w _ { 2 } , \ \dots , \ w _ { j } , \ \dots , \ w _ { q } ]$ where $w _ { j }$ implies the weight on the variable j. We restrict the value of $w _ { j }$ to $0 { \leq } w _ { j } { \leq } 1 , \ j { = } 1 , \ . \ . . , \ q .$ The goals with $0 { \le } w _ { j } { < } 1$ are negotiable with each other. However, we assume that the variable with $w _ { j } { = } 1$ must be satisfied and is thus nonnegotiable.

$\operatorname { S I M } ( \pmb { S } _ { i } , \pmb { R } ) ;$ : Similarity Score is the reverse of distance and can be measured by one of the nearestneighbor algorithms [12]:

$$
\operatorname{SIM} (\boldsymbol {S} _ {i}, \boldsymbol {R}) = \sum_ {j = 1} ^ {q} w _ {j} (1 - d (s _ {i j}, r _ {j})) / \sum_ {j = 1} ^ {q} w _ {j}
$$

$$
\text { for } i = 1, \dots , p\tag{1}
$$

$$
0 \leq \operatorname{SIM} (\boldsymbol {S} _ {i}, \boldsymbol {R}) \leq 1 \quad \text {   for   } i = 1,.., p\tag{2}
$$

Price(X): The price of model X. For instance. ${ \mathrm { P r i c e } } ( S _ { i } ) { \mathrm { : } }$ The price of the standard model $s _ { i } .$ $\mathrm { P r i c e } ( M _ { i } ) ;$ : The price of the modified model $M _ { i } .$ $\operatorname { P r i c e } ( M _ { i } - { \pmb S } _ { i } ) ;$ : The price change for the modification from $\pmb { S } _ { i }$ to $M _ { i }$

Thus, ${ \mathrm { P r i c e } } ( M _ { i } ) = { \mathrm { P r i c e } } ( S _ { i } ) + { \mathrm { P r i c e } } ( M _ { i } - S _ { i } )$

Using the above notations, the standard model selection and modification procedure are described in the following subsections.

## 4.2. Standard model selection procedure

In this stage, we need to select a similar model among p standard models under consideration. The procedure consists of four steps: filtering out disqualified models, computing the similarity, sorting the models by the order of similarity and selecting the most similar one as the first candidate model. To compute the distance, we prepared a thesaurus that provides the measures of values. All original measures are transformed to the [0,1] scale, and the bigger figure represents higher performance. For instance, memory size in Table 1 has the original measure of MB. The minimum is 64 MB, while the maximum 1024 MB. Hence, the normalized scale of the memory size of 512 MB is (51264)/(102464)=0.47. Since all scales stay [0,1], the distance between two scale values thus also stays [0,1]. For the non-numeric measures, the relative performance order is regarded as the measure, which is also transformed to the scale [0,1]. With the normalized scales, the heterogeneous measures can be aggregated.

## Step 1. Filter out disqualified models.

Let a customer input his/her requirements R and preference weights W for the q variables. Compute the distances $\pmb { d } ( s _ { i j } , r _ { j } )$ of the Must variables with $w _ { j } { = } 1$ for all models. If any j of the Must variables is not satisfied, the model is disqualified. Filter out the disqualified models, and make a list of the qualified models.

Step 2. Compute the similarity score of qualified standard models by the Eq. (1).

The similarity score can be regarded as the satisfaction level of the product model. Sort the standard models in the descending order of similarity scores.

Step 3. Select the qualified standard model with the maximum similarity as the current standard model.

4.3. Concurrent Local Propagation Algorithm for CSP-MSM problems

Formulate the CSP-MSM model by assigning the values of the current standard model. To solve the CSP-MSM effectively, we devised the Concurrent Local Propagation Algorithm using the following three policies.

Policy 1. Set the unsatisfied goal variables as seed variables.

The specifications of the current model are assigned as initial values to the CSP. If a value does not satisfy the required goal, such a variable needs modification. Thus, it is reasonable to appoint the unsatisfied variables as seed variables where the constraint propagations begin [15]. Another popular strategy of selecting the seed variables is the strategy by Variable Importance and/or Tightness [25]. In this study, the weight of a variable can be regarded as important. Hence, the Must variables may become the seed variables. In Section 5, we compare the performance of two strategies, and found the strategy by Unsatisfied Goal Variable more effective in the SMSM problem.

Policy 2. Propagate with multiple seed variables concurrently, and resolve goal conflicts.

Concurrent propagation with multiple seed variables is an effective architecture to support negotiation between the conflicting goals. When a non-goal variable receives more than one conflicting propagation, the impact of adopting one goal over the other is useful information to support the tradeoff between the two goals. The difference between realized value and desired goal is the impact that we have to sacrifice to fulfill the winning goal. In the decision supporting system setting, the decision maker may interactively select the winning goal. However, to experiment with many cases, we need to automate the tradeoffs. Thus, in this experimental setting, we assume the goal with the higher weight will win.

Policy 3. Prune unnecessary propagations that are assured by the specifications of standard models.

If the value of a variable is not changed even after a constraint is propagated, the variable does not have to propagate further if the compatibilities with the remaining variables are already assured by the specifications of the standard model. This approach can eliminate unnecessary propagations.

Based on the above principles, the Concurrent Local Propagation Algorithm to solve the CSP-MSM is organized as Steps 4-5.

Step 4. Formulate the CSP-MSM model with the current model.

Step 4.1. Identify the distance between the requirements R and current model $\pmb { S } _ { \mathrm { i } }$

If the current $\pmb { S } _ { i }$ completely satisfies R, that is $D ( S _ { i } , R ) { \geq } 0 $ , a satisfactory model is found with the current model. Go to Step 6 to check the necessity of repeating the process with the next most similar standard model. If there exists j that is ${ \pmb d } ( s _ { i j } , r _ { j } ) { < } 0$ , the current model needs modification. Go to Step 4.2.

Step 4.2. Assign the specifications of the current model $\pmb { S } _ { i }$ as the values of the CSP model.

## Step 4.3. Derive an initial modified model.

Detect the unsatisfied values by the condition ${ \pmb d } ( s _ { i j } , r _ { j } ) { < } 0$ . For the unsatisfied goals, modify the specifications of the current model according to the customer’s requirements as follows:

$$
m _ {i j} = \left\{ \begin{array}{l l} s _ {i j} & \text { if } d (s _ {i j, r _ {j}}) \geq 0 \\ r _ {j} & \text { if } d (s _ {i j}, r _ {j}) <   0. \end{array} \right.\tag{3}
$$

The Eq. (3) implies that the values of overqualified variables offered by the standard models are adopted assuming that there is no extra cost for the overqualification. Sometimes, degrading the overqualified factors of the standard models may not be even physically possible.

## Step 4.4. Select seed variables.

Unsatisfied variables associated with constraints are selected as seeds with which to propagate because these variables are the origin that requires negotiation.

Step 5. Propagate the constraints concurrently from multiple seed variables.

Propagations start with each seed variable concurrently. To decide the order of propagation, we need to make the rules for variable ordering and value ordering:

– Variable Ordering Rule: Propagate the constraint first that is associated with the variable with the largest number of constraints.

– Value Ordering Rule: Among the values of a negotiating variable, select a value that has minimum distance from the customer’s requirements. If more than one value exist at the minimum distance, select the one with the lowest price.

For the repeated iterations after the first round with the most similar model, we should make sure that the assigned values are at least as good as the ones assigned in the first iteration to prevent functional degradation. The unnecessary propagations are pruned whenever the compatibility is assured by the specifications of standard models.

4.4. Check the optimality and iterate with the next similar model

Step 6. Check the local optimal condition.

If a previous model exists, compare the price of the current modified model with that of the last model. If the current model has a higher price, conclude that the last model is local optimal and stop the iteration. If there are no more models left, stop the iteration and conclude that the current model is local optimal. Otherwise, go to Step 7.

## Step 7. Replace the candidate model.

Replace the current model with the next most similar standard model and repeat Steps 4-6.

## 5. Illustrative customization of personal computers

This section illustrates the SMSM Algorithm with an example of PCs. A PC has 25 variables (in 14 factors) as depicted in Fig. 3. To conduct the experiment, we use 42 standard models at the Dell’s PC section as of January 20, 2001, which are denoted as $S { = } [ S _ { 1 } , . . . , S _ { 4 2 } ]$ . As mentioned in Section 4.2, the functions in numeric and non-numeric measures and price are transformed to the scale [0,1] based on expert opinion and the authors’ knowledge. In this manner, all measures have become commensurable. Distance 0 means the two values are functionally equal. For instance, Mouseman Wheel and Mouseman USB Wheel are functionally equal. Note the illustrative customer’s requirements depicted in Fig. 3.

The weights of variables are marked in the right most column.

## 5.1. Standard model selection with the PC case

## Step 1. Filter out disqualified models.

Since the mission critical factors adopted as Must are Memory Size, Monitor Size and Resolution, CD/DVD ROM Drive Size and Type, and Sound Card, filter out the models that do not satisfy these six variables. We obtain five qualified models: $S _ { 9 } , S _ { 2 7 } , S _ { 1 1 } , S _ { 4 } , S _ { 8 }$ as listed in Table 2. Table 2 contrasts the customer’s requirements with five qualified standard models.

Step 2. Compute the similarities of qualified standard models.

The similarities of the models $S _ { 9 } , S _ { 2 7 } , S _ { 1 1 } , S _ { 4 } , S _ { 8 }$ to R are 0.82, 0.79, 0.77, 0.76, 0.73, respectively.

Step 3. Select the model $S _ { 9 }$ as the first candidate because it has the maximum similarity score.

5.2. Concurrent Local Propagation Algorithm for the CSP-MSM problem

This stage modifies the current standard model to fit to the requirements considering the 12 constraints in Fig. 1. Eleven variables associated with the constraints are graphically depicted in Fig. 2.

## Step 4. Formulate the CSP-MSM model.

By computing the normalized distance between R and $s _ { 9 } ,$ we can identify that four variables in three factors are unsatisfied with $S _ { 9 } .$ . Among them, only two variables (CPU<sup>\_</sup>Processor and Video<sup>\_</sup>Card<sup>\_</sup>Speed) are associated with constraints and thus are selected as seed variables as marked in a rectangle in Fig. 2.

Substitute the unsatisfied values in $S _ { 9 }$ with those of requirements R and derive $M _ { 9 }$ with a similarity score of 1.00: Other values of $M _ { 9 }$ are the same as those of $S _ { 9 }$

Step 5. Propagate the constraints concurrently from multiple seed variables.

The Concurrent Local Propagation starts with two seeds: CPU<sup>\_</sup>Processor and Video<sup>\_</sup>Card<sup>\_</sup>Speed. The

CPU<sup>\_</sup>Processor (the first seed) is associated with the CPU<sup>\_</sup>Speed by the constraint C8 and the Video<sup>\_</sup> Card<sup>\_</sup>Speed (the second seed) is associated with Video<sup>\_</sup>Card<sup>\_</sup>Type by the constraint C11.

Detect the conflicting goals and resolve them by the priority of variables.

After the propagation of C8 starting with the first seed, the Pentium IV of CPU<sup>\_</sup>Speed has three compatible values (1.3, 1.4 and 1.5 GHz). Hence, the current value <sup>d</sup>1.0 GHz<sup>T</sup> of CPU<sup>\_</sup>Speed should be replaced by <sup>d</sup>1.3 GHz<sup>T</sup>, which is closest to the current value. The second seed Video<sup>\_</sup>Card<sup>\_</sup>Speed with the value <sup>d</sup>4X<sup>T</sup> propagates with the constraint C11 and finds the compatible value <sup>d</sup>NVIDIA<sup>\_</sup>TNT2<sup>\_</sup>M64<sup>T</sup> of the Video<sup>\_</sup>Card<sup>\_</sup>Type.

In this manner, each seed continues propagation concurrently. In the first seed, the CPU<sup>\_</sup>Speed continues to propagate Video<sup>\_</sup>Card<sup>\_</sup>Type. In the Video<sup>\_</sup>Card<sup>\_</sup>Type, conflict occurs from two propagations. The decision maker has to decide which propagation (in other words, which seed variable) has higher priority. In this example, the CPU<sup>\_</sup>Processor has the weight 0.8, while the Video<sup>\_</sup>Card<sup>\_</sup> Speed 0.6. Thus, the propagation from the first seed is assumed to win. Fortunately, the suggested value of Video<sup>\_</sup>Card<sup>\_</sup>Type by the first seed is also compatible with the required Video<sup>\_</sup>Card<sup>\_</sup>Speed; thus, there is no impact on the goal in the second seed.

Now, the two sub-CSPs are merged. However, the cost of replacing the CPU<sup>\_</sup>Speed and Video<sup>\_</sup>Card<sup>\_</sup> Type should be additionally paid. The propagation continues to other constraints, and finds other variables have compatible values. However, the propagation stops at Memory<sup>\_</sup>Type, because its value was not changed. The further propagation to C9 and C10 can be pruned.

Modifying the CPU<sup>\_</sup>Speed from <sup>d</sup>1.0 GHz<sup>T</sup> to <sup>d</sup>1.3 GHz<sup>T</sup> to meet the constraint C8 costs \$50.00. Likewise, modifying the Video<sup>\_</sup>Card<sup>\_</sup>Type from <sup>d</sup>NVIDIA<sup>\_</sup>TNT2<sup>\_</sup>M64<sup>T</sup> to <sup>d</sup>DDR<sup>\_</sup>ATI<sup>\_</sup>Radeon<sup>T</sup> to meet the constraint C4 costs \$30.00. The costs to upgrade the other two variables (Modem and Network<sup>\_</sup>Card) not associated with the constraints are (\$30.00, \$117.00) respectively. Since the price of the standard model $S _ { 9 }$ is \$1,299.00, the price $M _ { 9 }$ is: $\operatorname* { P r i c e } ( M _ { 9 } ) = \operatorname* { P r i c e } ( S _ { 9 } ) + \operatorname* { P r i c e } ( M _ { 9 } - S _ { 9 } ) = \ S 1 , 2 9 9 . 0 0 +$ $( \ S 5 0 . 0 0 + \ S 3 0 . 0 0 + \ S 3 0 . 0 0 + \ S 1 1 7 . 0 0 ) { = } \ S 1 , 5 2 6 . 0 0$

T<sub>a</sub>bl<sub>e</sub> 2 V<sub>ar</sub>i<sub>a</sub>bl<sub>es requ</sub>i<sub>remen</sub>t<sub>s we</sub>i<sub>g</sub>ht<sub>s an</sub>d <sub>qua</sub>lifi<sub>e</sub>d <sub>s</sub>t<sub>an</sub>d<sub>ar</sub>d <sub>mo</sub>d<sub>e</sub>l<sub>s</sub>

<table><tr><td rowspan="2">Factors</td><td rowspan="2">Variables</td><td rowspan="2">Requirements (R)</td><td rowspan="2">Weights</td><td colspan="5">Qualified standard models</td></tr><tr><td> $S_9$ </td><td> $S_{27}$ </td><td> $S_{11}$ </td><td> $S_4$ </td><td> $S_8$ </td></tr><tr><td rowspan="2">CPU</td><td>Processor</td><td>PentiumIV</td><td>0.8</td><td>PentiumIII</td><td>PentiumIII</td><td>PentiumIII</td><td>PentiumIII</td><td>PentiumIII</td></tr><tr><td>Speed</td><td>1.0 GHz</td><td>0.8</td><td>933 MHz</td><td>1 GHz</td><td>1 GHz</td><td>866 MHz</td><td>933 MHz</td></tr><tr><td rowspan="3">Memory</td><td>Size</td><td>256 MB</td><td>1.0</td><td>256 MB</td><td>256 MB</td><td>256 MB</td><td>256 MB</td><td>256 MB</td></tr><tr><td>Speed</td><td>600 MHz</td><td>0.8</td><td>600 MHz</td><td>600 MHz</td><td>133 MHz</td><td>133 MHz</td><td>133 MHz</td></tr><tr><td>Type</td><td>SDRAM</td><td>0.8</td><td>RDRAM</td><td>RDRAM</td><td>SDRAM</td><td>SDRAM</td><td>SDRAM</td></tr><tr><td rowspan="3">Hard Drive</td><td>Size</td><td>20 GB</td><td>0.6</td><td>40 GB</td><td>40 GB</td><td>20 GB</td><td>10 GB</td><td>40 GB</td></tr><tr><td>RPM</td><td>7200</td><td>0.6</td><td>7200</td><td>7200</td><td>7200</td><td>-</td><td>7200</td></tr><tr><td>Interface method</td><td>ATA</td><td>0.6</td><td>ATA</td><td>ATA-100</td><td>ATA</td><td>ATA</td><td>ATA</td></tr><tr><td rowspan="4">Monitor</td><td>Size (in.)</td><td>17</td><td>1.0</td><td>17</td><td>17</td><td>17</td><td>17</td><td>17</td></tr><tr><td>Refresh rate</td><td>70</td><td>0.8</td><td>70</td><td>85</td><td>107</td><td>70</td><td>70</td></tr><tr><td>Resolution</td><td>1024×768</td><td>1.0</td><td>1024×768</td><td>1024×768</td><td>1024×768</td><td>1024×768</td><td>1024×768</td></tr><tr><td>Type</td><td>Monitor</td><td>0.6</td><td>Monitor</td><td>Monitor</td><td>Monitor</td><td>Monitor</td><td>Monitor</td></tr><tr><td rowspan="3">Video Card</td><td>Size</td><td>32 MB</td><td>0.8</td><td>16 MB</td><td>32 MB</td><td>32 MB</td><td>-</td><td>-</td></tr><tr><td>Speed</td><td>4X</td><td>0.8</td><td>2X</td><td>4X</td><td>4X</td><td>-</td><td>-</td></tr><tr><td>Type</td><td>NVIDIA_TNT2_M64</td><td>0.6</td><td>NVIDIA_TNT2_M64</td><td>NVIDIA_Geforce2_MX</td><td>DDR ATI Radeon</td><td>Intel 3D AGP Graphics</td><td>Intel 3D AGP Graphics</td></tr><tr><td>CD/DVD</td><td>Speed</td><td>48X</td><td>1.0</td><td>48X</td><td>48X</td><td>48X</td><td>48X</td><td>48X</td></tr><tr><td>ROM Drive</td><td>Type</td><td>Max Variable CD-ROM Drive</td><td>1.0</td><td>Max Variable CD-ROM Drive</td><td>Max Variable CD-ROM Drive</td><td>Max Variable CD-ROM Drive</td><td>Max Variable CD-ROM Drive</td><td>Max Variable CD-ROM Drive</td></tr><tr><td>Sound Card</td><td>Sound Card</td><td>SB Live! Value Digital with Music Match Software</td><td>1.0</td><td>SB Live! Value Digital with Music Match Software</td><td>SB Live! Value Digital with Music Match Software</td><td>SB Live! Value Digital with Music Match Software</td><td>SB Live! Value Digital with Music Match Software</td><td>SB Live! Value Digital with Music Match Software</td></tr><tr><td>Modem</td><td>Modem</td><td>US Robotics v.90/56 K PCI Telephony Modem-Sound Option</td><td>0.6</td><td>V.90/56 K PCI DataFax Modem for Windows</td><td>-</td><td>V.90/56 K Telephony Modem for Windows ME-Sound Option</td><td>V.90/56 K PCI DataFax Modem for Windows</td><td>V.90/56 K PCI DataFax Modem for Windows</td></tr><tr><td>Network Card</td><td>Network Card</td><td>3COM 10/100 Fast Ethernet PC Card</td><td>0.8</td><td>-</td><td>3COM 10/100 Fast Ethernet PC Card</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Limited warranty and support</td><td>Limited warranty and support</td><td>1 Year Parts and Onsite Labor (Next Business Day)+1 Year Phone Tech Support</td><td>0.2</td><td>1 Year Next Business Day On-Site Parts and Labor_Years 2 and 3 Parts</td><td>3 Years Parts Delivery and 1 Year Labor (Next Business Day)</td><td>1 Year Next Business Day On-Site Parts and Labor_Years 2 and 3 Parts</td><td>1 Year Next Business Day On-Site Parts and Labor_Years 2 and 3 Parts</td><td>1 Year Next Business Day On-Site Parts and Labor_Years 2 and 3 Parts</td></tr><tr><td>Price</td><td></td><td></td><td></td><td>$1,299.00</td><td>$1,399.00</td><td>$1,599.00</td><td>$1,089.00</td><td>$1,299.00</td></tr><tr><td>Similarity score of requirements</td><td></td><td></td><td></td><td>0.82</td><td>0.79</td><td>0.77</td><td>0.76</td><td>0.73</td></tr></table>

Steps 6–7. Check the local optimal condition and replace the candidate model.

Reset the currency to $\pmb { S } _ { 2 7 }$ and repeat Steps 4 and 6. The price of $M _ { 2 7 }$ turns out to be \$1,509.00, which is less than that of $M _ { 9 } .$ Repeat Steps 4 and 6 again with the next most similar model $\pmb { S } _ { 1 1 }$ . The price of $M _ { 1 1 }$ is \$1,716.00, which is higher than that of $M _ { 2 7 }$ . Thus, the previous model $\pmb { S } _ { 2 7 }$ turns out as the local optimal solution. In this example, the customer finds the reconfigured model $M _ { 2 7 }$ is cheaper than $M _ { 9 }$ by \$17.

## 6. Performance evaluation of the SMSM Algorithm

This section explains the experiment on the performance of the SMSM Algorithm with 93 randomly generated cases of PC selections. The 93 cases are generated by randomly modifying the requirements based on the standard models, but 18 generically infeasible cases are discarded from the experiment. This experiment is designed to test the following issues:

(1) Does the most similar standard model provide the optimal specifications? The answer can derive a conclusion on whether the price obtained with the most similar model is significantly higher than the one obtained with the global optimum.

(2) What is the contribution of the SMSM Algorithm in obtaining feasible specifications?

(3) What is the performance achieved by the first local optimal model in comparison with the global optimal model?

(4) What is the computational efficiency of the Concurrent Local Propagation Algorithm in comparison with the conventional constraint propagation algorithm with a single seed variable?

Let us investigate each issue one by one.

(1) Performance of the most similar standard model in providing the optimal specifications.

According to the experiment, 56 out of 75 cases found the local optimal specifications with a model other than the most similar standard model. This result implies that the most similar model does not guarantee the discovery of the optimal specifications. Based on this statistic, we tested the following hypothesis: <sup>d</sup>The price obtained with the most similar model is equal to the price obtained by the first local minimum.

A paired t-test with 75 pairs was conducted to verify if the prices obtained from the local optimal models are significantly lower. We found that $t { = } 1 4 8 . 3 9 { > } t _ { 7 5 , 0 . 0 1 } { = } 2 . 3 7 4$ . Thus, the test rejects the null hypothesis, which means the average price of the first local optimal model is significantly $( p { < } 0 . 0 1 )$ lower than that of the most similar standard model. The average price difference between the two is 6.04 %. The price error percentages for the iterations are summarized in Table 3. The average price difference after the second iteration (the third iteration) is 0.32% (0.00%) (see Table 3). Thus, we conclude that the most similar model does not guarantee local optimality, and it is worth searching for one or two more similar models to discover the approximately optimal model. This conclusion can also show that the price obtained with the most similar model is significantly higher than the one obtained with the global optimum.

(2) Contribution of the SMSM Algorithm in obtaining feasible specifications.

The similar standard model without modification approach could satisfy the requirements in only 5 out of 75 cases (93.33% error rate). The modification with the most similar model without the compatibility check could satisfy 31 out of 75 cases (58.67% error rate). However, the SMSM Algorithm could discover the feasible specifications without any error even in the first iteration as summarized in the second column of Table 4.

The effect of iterations in the SMSM Algorithm is summarized in the third and fourth columns of Table 4.

Price error percentage of the SMSM Algorithm

<table><tr><td>Phase</td><td></td><td>Price error (%) in finding the first local optimum with the satisfied model</td><td>Price error (%) in finding global optimum with the satisfied model</td></tr><tr><td rowspan="3">Number of iterations by the Order of Similarity</td><td>1</td><td>6.04</td><td>6.36</td></tr><tr><td>2</td><td>0.32</td><td>0.81</td></tr><tr><td>3</td><td>0.00</td><td>0.42</td></tr></table>

Table 4  
Effectiveness of the SMSM Algorithm (total number of cases=75)

<table><tr><td colspan="3">Phase</td><td>Number of cases finding satisfied model (% error)</td><td>Number of cases finding the first local optimum with the satisfied model (% error)</td><td>Number of cases finding global optimum with the satisfied model (% error)</td></tr><tr><td colspan="3">Most similar standard model without modification</td><td>5 (93.33%)</td><td>5 (82.42%)</td><td>5 (82.42%)</td></tr><tr><td colspan="3">modification of the most similar model without compatibility checks</td><td>31 (58.67%)</td><td>19 (74.67%)</td><td>19 (74.67%)</td></tr><tr><td rowspan="5">Modification of the similar models with compatibility checks (SMSM Algorithm)</td><td rowspan="5">Number of iterations by the order of similarity</td><td>1</td><td>75 (0.00%)</td><td>24 (68.00%)</td><td>24 (68.00%)</td></tr><tr><td>2</td><td>-</td><td>71 (5.33%)</td><td>68 (9.33%)</td></tr><tr><td>3</td><td>-</td><td>75 (0.00%)</td><td>71 (5.33%)</td></tr><tr><td>6</td><td>-</td><td>-</td><td>74 (1.33%)</td></tr><tr><td>14</td><td>-</td><td>-</td><td>75 (0.00%)</td></tr></table>

Twenty four cases could find the local optimality after the first iteration, 71 after the second iteration, and 75 (all cases) after the third iteration. The average number of iterations for finding the local optimum is 1.69, but the actual number of iterations necessary to confirm the local optimality is 2.36 because we need to check the next model to confirm the convexity condition of the local optimum. The SMSM Algorithm with three iterations can find the 71 global optimal models with a success rate of 94.67%.

(3) Performance achieved by the local optimal model in comparison with the global optimal model.

For 4 out of 75 (94.67% accuracy rate) cases, the local optimal model is not the same as the global optimal model, and the price error by the local optimum is 0.42%. One outlier found the global optimum at the 14th iteration. According to the results of this experiment, the local optimum rule is reliable enough to discover the global optimum with an accuracy of 94.67 %, while reducing the average computational effort from 4.15 iterative to 2.36.

Table 5  
Performance of Concurrent Local Propagation

<table><tr><td rowspan="2">Seed</td><td colspan="3">Seed selection strategies</td></tr><tr><td>Unsatisfied variables</td><td>Must variables and unsatisfied variables</td><td>A single must variable</td></tr><tr><td>Average number of seeds</td><td>2.28</td><td>5.41</td><td>1.00</td></tr><tr><td>Average number of consistency checks</td><td>4.92</td><td>8.72</td><td>12.28</td></tr></table>

(4) Computational efficiency of the Concurrent Local Propagation Algorithm.

The conventional constraint propagation algorithm with a single seed variable required 12.28 consistency checks [22], while the concurrent reasoning by the unsatisfied variable strategy took only 4.92 checks (see Table 5). Note that adding the Must variables to seeds was not helpful.

According to this experiment, we conclude that the SMSM Algorithm with the following three strategies is effective in finding an approximately optimal reconfigured standard model:

– The concurrent sub-CSPs are propagated from the multiple seed variables.

– Unsatisfied variables are adopted as seed variables.

– The first local optimum is adopted as the stopping rule.

## 7. Conclusion and discussion

We developed the Standard Model Selection and Modification (SMSM) Algorithm that can find the first local optimal configuration by iterating with the next few similar standard models. According to our experiment with real world PC selection at Dell’s site, we discovered that in 51 out of 75 cases the first local optimal configuration with a model other than the most similar standard model has found. The local optimal solution could cut costs by 6.04%. Since all the local optimal configurations could be discovered within three iterations (on the average by 2.36 iterations), it is recommended that the three most similar models are tried in PC selection to find the local optimal model, which is the same as the global optimal 94.67% of the time.

One limitation of the current experiment is that the cases are randomly generated; hence, the requirements generated for this experiment may not precisely coincide with a real customer’s behavior. For this purpose, we need to collect the data from the real world, and this was not possible without Dell’s cooperation.

By deploying the SMSM on the online comparison sites for standardized products with options, customers can select their favorite specifications at a lower cost with a relatively easy search. This capability will attract customers to the site. Since the benefit of the SMSM Algorithm will be increased as the constraints become more complex, it will be interesting to apply the algorithm in the B2B setting for the selection of industrial products such as servers, machine tools, and integrated software components.

## References

[1] W.M. Bain, Case-based reasoning: a computer model of subjective assessment, PhD thesis, Yale University, 1989.

[2] R. Burke, The Wasabi personal shopper: a case-based recommender system, Proc. AAAI-99, AAAI (American Association of Artificial Intelligence), Orlando, Florida United States, 1999, pp. 844 – 849.

[3] J.G. Carbonell, M.M. Veloso, Proc. Workshop on Case Based Reasoning (DARPA), Morgan Kaufmann Publishers, Clearwater, FL, 1988.

[4] J.G. Carbonell, R.S. Michalski, T.M. Mitchell, Machine Learning: An Artificial Intelligence Approach, Morgan Kaufmann Publishers, Los Altos, CA, 1986.

[5] B.Y. Choueiry, G. Noubir, On the computation of local interchangeability in discrete constraint satisfaction problems, Proc. AAAI-98, AAAI, Madison, Wisconsin, 1998, pp. 326 – 333.

[6] P. Cunningham, R. Bergmann, S. Schmitt, R. Traph<sup>f</sup>ner, S. Breen, B. Smyth, WEBSELL: intelligent sales assistants for the world wide web, KI - Zeitschrift f<sup>q</sup>r K<sup>q</sup>nstliche Intelligenz, Special Issue: Electronic Commerce Issue 1 (1) (2001) 28 – 32.

[7] E.C. Freuder, The role of configuration knowledge in the business process, IEEE Intelligent Systems 13 (4) (1998 (July/ August)) 29– 31.

[8] J.H. Gilmore, B.J. Pine, The four faces of mass customization, Harvard Business Review (1997) 91– 101.

[9] A. Haag, Sales configuration in business processes, IEEE Intelligent Systems (1998) 78 – 85.

[10] K. Hammond, CHEF: a model of case-based planning, Proc. AAAI-86, AAAI, Philadelphia, PA, 1986, pp. 267 – 271, Cambridge, MA.

[11] G. H<sup>7</sup>ubl, V. Trifts, Consumer decision making in online shopping environments: the effects of interactive decision aids, Marketing Science 19 (1) (2000) 4 –21.

[12] M. Heinrich, E. Jungst, A resource-based paradigm for the configuring of technical systems from modular components, Proc. Conference on Artificial Intelligence Applications, IEEE Computer Society Press, Miami Beach, Florida, USA, 1991, pp. 257– 264.

[13] D.H. Hennessy, D. Hinkle, Applying case-based reasoning to atuoclave loading, IEEE Expert 7 (5) (1992) 21–26.

[14] T.R. Hinrichs, Problem Solving in Open Worlds: A Case Study in Design, Lawrence Erlbaum Publishers, Atlanta, GA, USA, 1992.

[15] Y. Huang, R. Miles, Combining case based and constraint based techniques in travel reservation systems, Proc. Conference on Artificial Intelligence for Applications (Los Angeles, CA, 1995), IEEE, Los Angeles, CA, 1995.

[16] iLog, iLog Configurator White Paper, ILOG Gentilly France, 2000.

[17] iLog, iLog Optimization Suit delivering a Competitive Advantage White Paper, iLOG France, May 2001.

[18] S. Jacobs, S. Kethers, Improving communication and decision making within quality function deployment, in: Proc. Conference on Concurrent Engineering, Research and Applications, CE94, Pittsburgh, Pennsylvania, vol. 8, CERA, Pittsburgh, PA, 1994.

[19] N. Jussien, O. Lhomme, Local search with constraint propagation and conflict-based heuristics, Artificial Intelligence 139 (1) (2002 (July)) 21– 45.

[20] N. Karacapilidis, P. Mora<sup>R</sup>tis, Building an agent-mediated electronic commerce system with decision analysis feature, Decision Support Systems 32 (1) (2001 (November)) 53– 69.

[21] J.L. Kolodner, Case-Based Reasoning, Morgan Kaufman Publishers, San Francisco, CA, 1993.

[22] J.L. Kolodner, R.L. Simpson, The mediator: analysis of an early case-based problem solver, Cognitive Science 13 (1989) 507 – 549.

[23] P. Koton, Reasoning about evidence in causal explanation, Proc. AAAI-88, AAAI, Cambridge, MA, 1988, pp. 256 – 263, Cambridge, MA.

[24] J. Lampel, H. Mintzberg, Customizing customization, Sloan Management Review (1996 (Fall)) 21 – 30.

[25] J.K. Lee, S.B. Kwon, ES\*: an expert systems development planner using a constraint and rule-based approach, Expert Systems with Applications 9 (2) (1995) 3 – 14.

[26] S.K. Lee, J.K. Lee, K.J. Lee, Salesman expert system for customized purchasing support: UNIK-SES, Expert Systems with Applications 11 (4) (1996) 431– 441.

[27] K.J. Lee, H.W. Kim, J.K. Lee, T.H. Kim, C.G. Kim, M.K. Yoon, E.J.V. Hwang, H.J. Park, Case and constraint-based apartment construction project planning system: FASTrak-APT, Proc. AAAI-97 (1997) 861– 866.

[28] C. Lottaz, I. Smith, B. Faltings, Spatial composition using cases: IDIOM, Proc. ICCBR’95, Springer Verlag, Berlin, Heidelberg, 1995, pp. 88 – 97.

[29] G.F. Luger, W.A. Stubblefield, Artificial Intelligence, The Benjamin/Cummings Publishing, Redwood City, CA, 1993.

[30] P. Maes, R.H. Guttman, A.G. Moukas, Agents that buy and sell: transforming commerce as we know it, Communications of the ACM (1999 (March)) 81– 91.

[31] M.L. Maher, CASECAD and CADSYN: implementing case retrieval and case adaptation, in: M.L. Maher, P. Pu (Eds.), Issues and Applications of Case-Based Reasoning in Design, Lawrence Erlbaum Publishers, Atlanta, GA, USA, 1997.

[32] M. McCandless, Let’s go shopping, IEEE Intelligent Systems 14 (1) (1999 (January/February)) 2 – 4.

[33] D.L. McGuiness, J.R. Wright, An industrial-strength description logic-based configurator platform, IEEE Intelligent Systems (1998 (July/August)) 69–77.

[34] F. Menczer, W. Nick Street, A.E. Monge, Adaptive assistants for customized E-shopping, IEEE Intelligent Systems (2002 (November/December)) 12 – 19.

[35] N. Neagu, B. Faltings, Exploiting interchangeabilities for case adaptation, Proc. ICCBR’01, Springer Verlag, Vancouver, CA, 2001.

[36] P. Oehler, I. Vollrath, P. Conradi, R. Bergmann, T. Wahlmann, READEE-decision support for ip selection using a knowledgebased approach, IP98 Europe Proc., Miller Freeman, San Francisco, CA, 1998.

[37] L. Purvis, P. Pu, COMPOSER: a case-based reasoning system for engineering design, Robotica 16 (3) (1998 (May)) 285 – 295.

[38] D. Sabin, R. Weigel, Product configuration frameworks—a survey, IEEE Intelligent Systems (1998 (July/August)) 42 – 50.

[39] N.M. Sadeh, M.S. Fox, Variable and value ordering heuristics for the job shop scheduling constraint satisfaction problem, Artificial Intelligence 86 (1996) 1 – 41.

[40] G. Schenner, G. Fleischanderl, Modifying configurations with model finding, Proc. IJCAI 2003, Morgan Kaufmann, Acapulco, Mexico, 2003.

[41] S. Schmitt, R. Bergmann, Product customization in an electronic commerce environment using adaptation operators, Proc. GWCBR’99, Wu¨ rzburg, Germany, Springer Verlag, Wu¨ rzburg, 1999 (March).

[42] G.D. Silveira, D. Borenstein, F.S. Fogliatto, Mass customization: literature review and research directions, International Journal of Production Economics 72 (2001) 1 – 13.

[43] B. Smyth, M.T. Keane, Experiments on adaptation-guided retrieval in case-based design, in domains by using goal dependencies, in: M. Veloso, A. Aamodt (Eds.), Proc. ICCBR’95, LNAI series, Springer Verlag, Sesimbra, Portugal, 1995, Springer.

[44] M.H. Sqalli, E.C. Freuder, CBR support for CSP modeling of interoperability testing, Proc. AAAI-98, Workshop on Case-Based Reasoning Integrations, Madison, Wisconsin, AAAI, Madison, Wisconsin, 1998 (July).

[45] I. Vollrath, W. Wilke, R. Bergmann, Case-based reasoning support for online catalog sales, IEEE Internet Computing 2 (4) (1998) 47–54.

[46] R. Weigel, B. Faltings, M. Torrens, Interchangeability for case adaptation in configuration problems, in: Proc. AAAI-98,

Workshop on Case-Based Reasoning Integrations, Madison, Wisconsin, USA, Technical Report WS-98-15, July 1998, pp. 166–171.

[47] W. Wilke, B. Smyth, P. Cunningham, in: M. Lenz, B. Bartsch-Sp<sup>f</sup>rl, H.-D. Burkhard, S. Wess (Eds.), Using Configuration Techniques for Adaptation, Case Based Reasoning Technology, Springer-Verlag, New York, 1999, pp. 139 – 168.

![](/api/attachments/JKNDFKQW/fulltext/images/628395ab7c7bd9d6e36479182549c6913a0e639d38eef60a4ccd3573fcf6397e.jpg)

Hyun Jung Lee has taken a PhD degree in Management Engineering from the Graduate School of Management at Korea Advanced Institute of Science and Technology (KAIST). She has work experiences as an Engineer at Hyundai Information Technology and a Principal Researcher at the International Center for Electronic Commerce (ICEC). She received BS in Physics and MS in Computer Science degrees from Ewha Womans University.

She has taken a UK technology scholarship programme, especially in technology transfer and the commercialization of innovation, combining technology and business training with specific commercialization projects in London Business School, Imperial College and Cambridge University. She has developed Management Information Systems and Electronic Commerce Applications with various industrial partners. Current research interests are in the fields of Electronic Commerce, Knowledge Management Systems and Intelligent Information Systems.

![](/api/attachments/JKNDFKQW/fulltext/images/0ba7ee05dfba35e7c47368fa3babcc1fc028c281eccf475635ba4547504c23dc.jpg)

Jae Kyu Lee is a Professor of Management Information Systems at Korea Advanced Institute of Science and Technology and a Director of the International Center for Electronic Commerce. He received a PhD degree from the Wharton School, University of Pennsylvania. He was Chair of the International Conference on Electronic Commerce (ICEC 1998 and ICEC 2000) and the 3rd World Congress on Expert Systems (1996). He

has authored several books on electronic commerce and expert systems and published numerous papers in the following journals: Management Science, CACM, DSS, Expert Systems with Applications, International Journal of Electronic Commerce, Decision Science, etc. Currently, he is the Editor in Chief of the Journal Electronic Commerce Research and Applications, and an Editorial Member of various international journals such as Decision Support Systems, Expert Systems with Applications, International Journal of Electronic Commerce, etc. His main research interests are in the fields of electronic commerce and intelligent information systems.
