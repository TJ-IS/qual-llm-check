---
otero_id: 21934
otero_key: "PRGB3QG4"
title: "Early project estimation in the formal communication protocol development"
authors: "Sun-Jen Huang"
year: "2001"
journal: "Information & Management"
doi: "10.1016/s0378-7206(00)00081-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Early project estimation in the formal communication protocol development

Sun-Jen Huang<sup>\*</sup>

Department of Information Management, National Taiwan University of Science and Technology, 43, Sec. 4, Keelung Rd., Taipei, Taiwan

Received 1 December 1999; accepted 9 November 2000

## Abstract

To help industrialize the use of formal description techniques in the software development of communication protocols, improving the software project management is as equally important as improving the software development techniques. An early software project estimation is a prerequisite for the quantitative software project management to be started early in the development life cycle. However, relatively little work has been done on such an issue in the formal communication protocol development environment. This paper proposes a two-stage software sizing process and product decomposition technique for establishing Estelle specification and implementation size models tailored to the formal communication protocol development environment. Based on the size estimates obtained from the size models above, this paper also presents the practical application in conducting a software cost model COCOMO II to estimate the development cost and project schedule of the ISO ROSE protocol development. <sup>#</sup> 2001 Elsevier Science B.V. All rights reserved.

Keywords: Software project estimation; Software sizing; Software cost estimate; COCOMO II; Formal description techniques

## 1. Introduction

Communication protocols play a vital role in distributed computing systems and computer networks. As most of the communication protocols are enormously complex, the use of informal techniques in such complex communication systems often produces systems with errors and undesirable behaviors [1,2]. Most of the problems are due to the fact that the specifications of communication protocols written in natural languages are inherently and unavoidably ambiguous, inconsistent and incomplete [3]. Therefore, such informal specifications cannot be analyzed for correctness before they are implemented. For producing the formal specifications of communication protocols, International Organization for Standardization (ISO) has developed specification languages called formal description techniques (FDTs) [4], which are based on a mathematical or graphical language.

Most of the past research work on FDTs in the software development of communication protocols has been mainly devoted to technical issues related to protocol specification, validation and verification, testing and implementation [5,6]. However, industrial acceptance of FDTs is still not very common. To help industrialize the use of FDTs, improving the way the communication protocol development projects are managed is as equally important as improving the software development technology. To date, however, relatively little research work has been done on the software project management issues using FDTs in the communication protocol development [7].

To produce high-quality software on time and within budget, software measurement [8,9] is one of the key factors that lead to effective software project management. Software measurement enables developers to measure and further assess the capability maturity of the software process, the quality of the products being produced and the productivity of the resource inputted, and thereby assist the management activities, like planning, tracking and controlling, in the software development. Especially, an early software cost and project schedule estimation is a prerequisite for the quantitative project management to be started early in the software development life cycle. The earlier we can estimate the development cost and project schedule, the sooner a software project development can be under control.

This paper proposes a two-stage software sizing process and product decomposition technique for establishing Estelle specification and implementation size models tailored to the formal communication protocol development environment. Based on the size estimates obtained from the size models above, this paper also presents the practical application in conducting a software cost model COCOMO II to estimate the development cost and project schedule of the ISO ROSE protocol development.

The rest of this paper is organized as follows. Section 2 introduces the formal communication protocol development environment where the Estelle language and the formal communication protocol development process are discussed. The establishment of the Estelle specification and implementation size estimation models is given in Section 3. The practical application of conducting COCOMO II to estimate the development cost and project schedule of the ISO ROSE protocol development is given in Section 4. Finally, Section 5 gives a conclusion of this paper.

## 2. The formal communication protocol development

## 2.1. Estelle

FDTs [4] have been recognized as being very beneficial in facilitating the development of unambiguous and complete protocol specifications, and in forming the basis for verification, validation, implementation and testing of communication protocols. Defined by ISO TC97/SC16/WG1 group formed in 1981 under the chairmanship of Professor Richard Tenney, Estelle [12] is one of the internationally standardized FDTs. Estelle makes use of ISO Pascal level 0 and enhances the finite state machine (FSM) by adding the facilities of control structures and data types which enable Estelle to specify distributed and concurrent information processing systems, in particular communication services and protocols at all seven layers of the ISO–OSI (OSI, open systems interconnection) architectures.

Within an Estelle specification, a communication protocol is specified as a hierarchical structure of communicating non-deterministic state automata, each of which is expressed in an Estelle module. Each module is characterized by its external communication interface and internal behavior and structure. The external interface of a module describes its communication with the environment by exchanging messages (interactions) through bi-directional bindings (channels) connecting its communication ports (interaction points, IPs) and by sharing, in a restricted way, some variables (exported variables). The internal behavior and structure of a module are specified by the set of actions (transitions) of an EFSM, and by the definition of sub-modules (children modules) of the module together with their interconnections, thus leading to a hierarchical tree structure of module definitions. A more detailed description of Estelle can be found in [12,13].

## 2.2. The formal communication protocol development process

The left part of Fig. 1 depicts the general formal communication protocol development process using FDTs. During the formal development life cycle, the initial task is the definition of system requirements. The desired communication services and the required behaviors of protocol entities are usually expressed in informal requirement descriptions using a natural language augmented with graphic- and tabular-based notations.

The next task is the formalization of system requirements. The functional protocol specification written in a chosen FDT is first obtained by hands with the aid of editor tools from the requirement descriptions of system requirements, and then further refined into the detailed protocol specification. The formal specifications written in a chosen FDT are then fed into the associated compilers for checking language syntax and static semantics and, if no errors occur, generating high level language source code for the purpose of implementation.

![](/api/attachments/PRGB3QG4/fulltext/images/8feac155d828c441509520634d25963166a5f5ec9dcfb3bb3a70efefa26b4c17.jpg)  
Fig. 1. The formal communication protocol development process.

## 3. Size estimation models

## 3.1. A two-stage software sizing process

Considering the formal protocol development process presented in Section 2, a two-stage software sizing process, shown in the right part of Fig. 1, is conducted for estimating the size of an Estelle specification and its generated implementation of a communication protocol. Stage 1 estimates the size of an Estelle specification of a communication protocol from its informal or semi-formal specification. Stage 2 estimates the size of an implementation generated automatically by the Estelle development toolset (EDT) tool [14], from the estimated size of an Estelle specification obtained at Stage 1, and then obtains the size estimate of the hand-coded implementation.

An Estelle specification is composed of a set of individual parts, each of which has different purposes and characteristics; thus, the size drivers for each part are apparently different. Therefore, the construction of the model is based on two approaches. A top-down product decomposition approach partitions the Estelle specification of a communication protocol into four parts based on its textual layout. A bottom-up construction approach first estimates the size for each part of an Estelle specification, and then obtains an equation for the size of an Estelle specification by adding the sizes of its four parts.

Least squares regression analysis [15] is used to develop the Estelle specification and implementation size estimation models. The process of building the regression model performed in this work involves three phases: (i) data collection and preparation, (ii) model refinement and selection, and (iii) model validation. The regression data set includes 14 communication protocols shown in Table 1, where the actual size of each Estelle specification and implementation is given. The established size models are validated using both the regression data set and a test data set. The test data set comprises two communication protocols which are shown in Table 1. Two criteria, mean magnitude of relative error (MMRE) and prediction at level L (Pred(L)), the most commonly used in existing software project estimation models, are applied for validating the model established. The introduction to MMRE and Pred(L) can be found in most literature work [20] or textbooks [8,9].

## 3.2. The Estelle specification size model

After the regression analysis, the derived size drivers and their definition for the four Estelle parts are summarized in Table 2. The final regression size estimation equations and their validation results for the four Estelle parts are presented in Table 3. The detailed description of how the size drivers and the regression equation for each Estelle part are derived can be found in [7].

By summing the four equations in Table 3, the size estimation equation for an Estelle specification is as follows:

$$
\begin{array}{r l} S _ {\text { spec }} & = - 9. 4 3 + 1. 4 2 \text { NCEP } + 3. 6 \text { NEV } \\ & + 3. 7 6 \text { NPF } + 2. 1 8 \text { NSP } + 2 \text { NPEFP } \\ & + 9. 9 6 \text { NFUN } + 1. 8 1 \text { NCA } + 2. 3 6 \text { NMI } \\ & + 6. 5 3 \text { NAV } + 5. 9 4 \text { STSI } \\ & + 0. 0 0 5 4 (\text { NAV } \times \text { STSI }) \end{array}\tag{1}
$$

The validation results of the Estelle specification size model using both the regression and test data sets are presented in Table 4. The results of two validation criteria, MMRE and Pred(0.25), are equal to 0.108 and 0.929 based on the regression data, and 0.076 and 1.0 based on the test data set. The results meet the required accuracy that the values of MMRE < 0:25

Table 1 The regression and test data sets

<table><tr><td>Protocols</td><td>Size in LOC of Estelle specification</td><td>Size in LOC of the implementation</td></tr><tr><td colspan="3">(a) The regression data set</td></tr><tr><td>Association control element (ACSE) protocol</td><td>729</td><td>3257</td></tr><tr><td>ROSE protocol</td><td>1575</td><td>7121</td></tr><tr><td>Virtual terminal protocol (VTP)</td><td>1047</td><td>4474</td></tr><tr><td>OSI transaction processing protocol (OSI TP)</td><td>8738</td><td>37531</td></tr><tr><td>OSI session protocol</td><td>1272</td><td>4540</td></tr><tr><td>OSI transport protocol</td><td>543</td><td>3126</td></tr><tr><td>Abracadabra protocol</td><td>314</td><td>1899</td></tr><tr><td>Express transfer protocol (XTP)</td><td>3182</td><td>22264</td></tr><tr><td>Sliding windows protocol (SWP)</td><td>225</td><td>1930</td></tr><tr><td>Alternative bit protocol (ABP)</td><td>248</td><td>2066</td></tr><tr><td>Metropolitan area network service (DQDB)</td><td>529</td><td>3662</td></tr><tr><td>ISDN link access protocol for D-channel (LAPD)</td><td>5488</td><td>25561</td></tr><tr><td>Connection less network protocol (CLNP)</td><td>439</td><td>3816</td></tr><tr><td>Network time protocol (NTP)</td><td>567</td><td>3379</td></tr><tr><td colspan="3">(b) The test data set</td></tr><tr><td>Reliable transfer service elements (RTSE) protocol</td><td>1087</td><td>4465</td></tr><tr><td>Logical link control type-3 (LLC3) protocol</td><td>539</td><td>3103</td></tr></table>

Table 2  
Size drivers and their definition

<table><tr><td></td><td>Size drivers</td><td>Definition</td></tr><tr><td rowspan="2">Header</td><td>NCEV</td><td>Number of connection end points</td></tr><tr><td>NEV</td><td>Number of exported variables</td></tr><tr><td rowspan="6">Declaration</td><td>NSP</td><td>Number of service primitive</td></tr><tr><td>NPF</td><td>Number of SPs parameters and PDUs fields</td></tr><tr><td>NCS</td><td>Number of control states</td></tr><tr><td>NMI</td><td>Number of module instances</td></tr><tr><td>NFUN</td><td>Number of predefined functions and procedures</td></tr><tr><td>NPEFP</td><td>Number of external and primitive functions and procedures</td></tr><tr><td rowspan="3">Initialization</td><td>NEV</td><td>Number of exported variables</td></tr><tr><td>NMI</td><td>Number of module instances</td></tr><tr><td>NCA</td><td>Number of connections and attachments</td></tr><tr><td rowspan="2">Transition</td><td>STSI</td><td>State table size index</td></tr><tr><td>NAV</td><td>Number of all variables</td></tr></table>

Table 3  
Four Estelle size estimation equations and their validation results

<table><tr><td>Specification part</td><td>Size estimation equation</td><td>Adj- $R^{2}$ </td><td>MMRE</td><td>Pred(0.25)</td></tr><tr><td>Header</td><td> $4.97 + 1.42 \times NCEP + 1.52 \times NEV$ </td><td>0.995</td><td>0.102</td><td>1.000</td></tr><tr><td>Declaration</td><td> $4.26 + 3.76 \times NPF + 2.18 \times NSP + 2 \times NPEFP + 9.96 \times NFUN$ </td><td>0.980</td><td>0.140</td><td>0.857</td></tr><tr><td>Initialization</td><td> $5.3 + 1.81 \times NCA + 2.08 \times NEV + 2.36 \times NMI$ </td><td>0.985</td><td>0.196</td><td>0.786</td></tr><tr><td>Transition</td><td> $-23.96 + 6.53 \times NAV + 5.94 \times STSI + 0.0054 \times (NAV \times STSI)$ </td><td>0.999</td><td>0.202</td><td>0.786</td></tr></table>

Table 4  
Validation of the Estelle specification size model

<table><tr><td>Protocol</td><td>Estimated</td><td>Actual</td><td>Residual</td><td>MRE</td></tr><tr><td colspan="5">(a) Based on the regression data set</td></tr><tr><td>ACSE</td><td>619</td><td>729</td><td>110</td><td>0.151</td></tr><tr><td>ROSE</td><td>1577</td><td>1575</td><td>-2</td><td>0.001</td></tr><tr><td>VTP</td><td>941</td><td>1047</td><td>106</td><td>0.101</td></tr><tr><td>OSI TP</td><td>8722</td><td>8738</td><td>16</td><td>0.002</td></tr><tr><td>Session</td><td>1212</td><td>1272</td><td>60</td><td>0.047</td></tr><tr><td>Transport</td><td>637</td><td>543</td><td>-94</td><td>0.173</td></tr><tr><td>Abracadabra</td><td>342</td><td>314</td><td>-28</td><td>0.089</td></tr><tr><td>XTP</td><td>3150</td><td>3182</td><td>32</td><td>0.010</td></tr><tr><td>SWP</td><td>220</td><td>225</td><td>5</td><td>0.022</td></tr><tr><td>ABP</td><td>371</td><td>248</td><td>-123</td><td>0.496</td></tr><tr><td>DQDB</td><td>596</td><td>529</td><td>-67</td><td>0.127</td></tr><tr><td>LAPD</td><td>5549</td><td>5488</td><td>-61</td><td>0.011</td></tr><tr><td>CNLP</td><td>456</td><td>439</td><td>-17</td><td>0.039</td></tr><tr><td>NTP</td><td>427</td><td>567</td><td>140</td><td>0.247</td></tr><tr><td colspan="5">MMRE = 0.108; Pred(0.25) = 0.929</td></tr><tr><td colspan="5">(b) Based on the test data set</td></tr><tr><td>RTSE</td><td>1014</td><td>1087</td><td>73</td><td>0.067</td></tr><tr><td>LLC3</td><td>585</td><td>539</td><td>-46</td><td>0.085</td></tr><tr><td colspan="5">MMRE = 0.076; Pred(0.25) = 1.0</td></tr></table>

and Pred $( 0 . 2 5 ) > 0 . 7 5$ are considered desirable for software project estimation models [8,9].

## 3.3. The implementation size model

After generating an implementation by using the EDT C code generator with the option $^ { 6 6 } - 1 ^ { 5 9 }$ , the semantic relationship between an Estelle specification and its generated C code is first analyzed. Based on the analysis, an implementation C code is partitioned into six parts: header, declaration, initialization, transition, Hdesc and Chead. A size metric, the number of nonblank and non-commentary source lines, is used to measure the size of the generated C code. The method of least squares regression analysis is used to develop the fitted equation for estimating the size of each of the four parts of the generated C code, and the size estimation equation for a communication protocol implementation is obtained by adding these size equations.

The size estimation equations for the implementations of the four parts of an Estelle specification are summarized in Table 5, where the validation results using the regression data set are also presented. Based on the analysis, the size of the Hdesc part of the generated implementation code linearly depends on the number of module bodies (including the specification module) of a source Estelle specification. Its size is equal to the number of module bodies (NOMB) multiplied by 31. By summing the size of all C header files required to be included in the generated C code, the size of the Chead part is a constant value 627.

Table 5  
Implementation size estimation equations and their validation results

<table><tr><td>Implementation part</td><td>Size estimation equation</td><td>Adj- $R^{2}$ </td><td>MMRE</td><td>Pred(0.25)</td></tr><tr><td>Header</td><td> $18.98 + 1.16 \times S_{header}$ </td><td>0.991</td><td>0.079</td><td>1.000</td></tr><tr><td>Declaration</td><td> $108.12 + 2.831 \times S_{decl}$ </td><td>0.952</td><td>0.128</td><td>0.786</td></tr><tr><td>Initialization</td><td> $9.66 + 7.78 \times S_{initi} - 0.0157 \times S_{initi}^{2}$ </td><td>0.968</td><td>0.127</td><td>0.786</td></tr><tr><td>Transition</td><td> $129.7 + 4.386 \times S_{trans}$ </td><td>0.998</td><td>0.143</td><td>0.769</td></tr></table>

By adding the four equations in Table 5 and the size of the Hdesc and Chead parts together, the size estimation equation for an implementation is as follows:

$$
\begin{array}{r l} S _ {\text { impl }} & = 8 9 3. 4 6 + 1. 1 6 S _ {\text { header }} + 2. 8 3 1 S _ {\text { decla }} \\ & \quad + 7. 7 8 S _ {\text { init }} - 0. 0 1 5 7 S _ {\text { init }} ^ {2} + 4. 3 8 6 S _ {\text { trans }} \\ & \quad + 3 1 \text { NOMB } \end{array}\tag{2}
$$

The validation results of the implementation size model using both the regression and test data sets are presented in Table 6. The results of two validation criteria, MMRE and Pred(0.25), are equal to 0.106 and 0.857 based on the regression data, and 0.079 and 1.0 based on the test data set. The results are considered as acceptable for a software project estimation model [8,9].

## 3.4. The computation of the total hand-coded size

Existing size-based software cost estimation models consider the hand-coded size in thousands of lines of code (KLOC) to be the primary factor. Thus, the size of codes by hand during the formal communication protocol development must be computed before employing the software cost models.

It was reported that during the formal protocol development, the code for the machine-independent part of the specification, which can be automatically generated, constitutes around 50–70% of a complete protocol implementation [19]. The machine-dependent parts of the specification have to be hand-coded. Much of these hand-coded routines, however, may be reused for different protocols running on the same machine.

Based on the analysis above, the size of codes by hand $( S _ { \mathrm { h a n d e d } } )$ , including the Estelle specification and those machine-dependant codes which are not reused, can be computed as follows:

$$
S _ {\mathrm{handed}} = S _ {\mathrm{spec}} + S _ {\mathrm{impl}} \frac {1 - \alpha}{\alpha} (1 - \beta),\tag{3}
$$

where $S _ { \mathrm { s p e c } }$ is the estimated size of an Estelle specification computed by Eq. $( 1 ) , S _ { \mathrm { i m p l } }$ the estimated size of an implementation computed by Eq. (2), a the abstraction ratio computed as the proportion of the size of the generated code out of the complete implementation code, and b the reuse rate computed as the proportion of the reused lines out of the total number of the machine-dependent lines.

Validation of the implementation size model

<table><tr><td>Protocol</td><td>Estimated</td><td>Actual</td><td>Residual</td><td>MRE</td></tr><tr><td colspan="5">(a) Based on the regression data set</td></tr><tr><td>ACSE</td><td>3699</td><td>3257</td><td>-442</td><td>0.136</td></tr><tr><td>ROSE</td><td>7246</td><td>7121</td><td>-125</td><td>0.018</td></tr><tr><td>VTP</td><td>5257</td><td>4474</td><td>-783</td><td>0.175</td></tr><tr><td>OSI TP</td><td>37386</td><td>37531</td><td>145</td><td>0.004</td></tr><tr><td>Session</td><td>5844</td><td>4540</td><td>-1304</td><td>0.287</td></tr><tr><td>Transport</td><td>3240</td><td>3126</td><td>-114</td><td>0.036</td></tr><tr><td>Abracadabra</td><td>2314</td><td>1899</td><td>-415</td><td>0.218</td></tr><tr><td>XTP</td><td>6111</td><td>6035</td><td>-76</td><td>0.012</td></tr><tr><td>SWP</td><td>2013</td><td>1930</td><td>-83</td><td>0.043</td></tr><tr><td>ABP</td><td>1978</td><td>2066</td><td>88</td><td>0.043</td></tr><tr><td>DQDB</td><td>3402</td><td>3662</td><td>260</td><td>0.071</td></tr><tr><td>LAPD</td><td>24949</td><td>25561</td><td>612</td><td>0.024</td></tr><tr><td>CNLP</td><td>2524</td><td>3816</td><td>1292</td><td>0.338</td></tr><tr><td>NTP</td><td>3092</td><td>3379</td><td>287</td><td>0.085</td></tr><tr><td colspan="5">MMRE = 0.106; Pred(0.25) = 0.857</td></tr></table>

<table><tr><td colspan="5">(b) Based on the test data set</td></tr><tr><td>RTSE</td><td>4837</td><td>4465</td><td>372</td><td>0.083</td></tr><tr><td>LLC3</td><td>3336</td><td>3103</td><td>-233</td><td>0.075</td></tr><tr><td colspan="5">MMRE = 0.079; Pred(0.25) = 1.0</td></tr></table>

## 4. Cost and schedule estimation

## 4.1. ISO ROSE, COCOCO II and COSTAR

The ISO ROSE (ROSE, remote operations service element ) protocol [16] is used as an example to illustrate our approach to estimating its development cost and project schedule. The ROSE protocol is an application service element (ASE) and drives the general purpose protocol for invoking and reporting the returns of arbitrary operations. The static system architecture of the ROSE protocol and parts of its Estelle specification can be found in [6].

Over the years a great variety of modeling techniques [17,18] for establishing software cost models have been proposed. A more detailed description for most existing software cost estimation models can be found in [8,9]. Among these models, COCOMO II (Constructive Cost Model II) [17], successor of the original COCOMO and Ada COCOMO models, is a well-known and widely employed cost estimation model. The COCOMO II model is developed with the aim of tailoring to new forms of software development in the 1990s and 2000s, like application composition capabilities, rapid development approaches and distributed middleware capabilities.

Developed by Softstar Systems, the software tool COSTAR automates the process of producing the development cost and schedule estimates based on the COCOMO family models including COCOMO II. Readers can get a free demo of COSTAR from URL: http://www.softstarsystems.com/index.htm. With the tailoring of the COCOMO II model, the software tool COSTAR is employed for conducting the procedure of estimating the development cost and project schedule of the ROSE protocol development.

## 4.2. Specification and implementation size measures of the ROSE protocol

The values of all size drivers of the ISO ROSE protocol are summarized in Table 7. By using the Estelle specification and implementation size estimation equations established in Section 3, the actual and estimated sizes of all parts of the ROSE Estelle specification and the generated implementation are summarized in Table 7.

The comparison of the actual and estimated sizes of the Estelle specification and implementation of the ROSE protocol is presented in Table 7. The size estimate of the ROSE Estelle specification is 1577 LOC which is very close to the actual size 1575 LOC. The size estimate of the ROSE implementation is 7246 LOC and the actual size is 7121 LOC; the magnitude of relative error (MRE) value is 1.7% ðj7121  7247j=7121Þ, which is considered as acceptable under the criterion MRE  0:25 for software project estimation models.

Comparison of the actual and estimated sizes of the ISO ROSE protocol<sup>a</sup>

<table><tr><td rowspan="2">Parts</td><td colspan="2">Specification</td><td colspan="2">Implementation</td></tr><tr><td>Actual</td><td>Estimated</td><td>Actual</td><td>Estimated</td></tr><tr><td>Size of the header part</td><td>36</td><td>37</td><td>61</td><td>61</td></tr><tr><td>Size of the declaration part</td><td>522</td><td>502</td><td>1421</td><td>1586</td></tr><tr><td>Size of the initialization part</td><td>47</td><td>53</td><td>268</td><td>341</td></tr><tr><td>Size of the transition part</td><td>970</td><td>985</td><td>4493</td><td>4384</td></tr><tr><td>Size of the Hdesc part</td><td>Nil</td><td>Nil</td><td>251</td><td>248</td></tr><tr><td>Size of the Chead part</td><td>Nil</td><td>Nil</td><td>627</td><td>627</td></tr><tr><td>Total</td><td>1575</td><td>1577</td><td>7121</td><td>7246</td></tr><tr><td>Residual</td><td></td><td>2</td><td></td><td>125</td></tr><tr><td>MRE (%)</td><td></td><td>0.1</td><td></td><td>1.7</td></tr></table>

<sup>a</sup> Size driver: NSEP (17), NEV (5), NSP (56), NPF (102), NCS (29), NMI (8), NFUN (0), NPEFP (0), NCA (10), STSI (110), NAV (50), NOMB (8).

Table 8  
The detailed report of the ROSE protocol development

<table><tr><td>Phase</td><td>Effort (staff-months)</td><td>Cost ($K)</td><td>Duration (months)</td><td>Staffing</td></tr><tr><td>RQ</td><td>0.6</td><td>1.5</td><td>0.9</td><td>0.6</td></tr><tr><td>PD</td><td>1.4</td><td>3.5</td><td>1.4</td><td>1.0</td></tr><tr><td>DD</td><td>2.2</td><td>5.5</td><td>1.3</td><td>1.6</td></tr><tr><td>CT</td><td>3.0</td><td>7.5</td><td>1.8</td><td>1.7</td></tr><tr><td>IT</td><td>1.6</td><td>4.0</td><td>1.2</td><td>1.4</td></tr><tr><td>Development Phase (PD + DD + CT + IT)</td><td>8.2</td><td>20.4</td><td>5.7</td><td></td></tr><tr><td>Totals (RQ + PD + DD + CT + IT)</td><td>8.7</td><td>21.9</td><td>6.6</td><td></td></tr></table>

<sup>a</sup> Estimate name: ISO ROSE; Estimate ID: 2011; Module name: COCOMO II 97; Module ID: 1997; Process Model: COCOMO II; Component size: 3440 SLOC; Level: 1.

## 4.3. The size estimate of the total code by hand of the ROSE protocol

Based on the level of abstractness of the ROSE Estelle specification, the abstraction rate (a) is estimated as 70% and the reuse rate (b) at our working environment is estimated as 40%. By using Eq. (3), the size estimate of the total code by hand of the ROSE protocol is computed as follows:

$$
\begin{aligned} S_{\text{handed}} & = S_{\text{spec}} + S_{\text{impl}} \frac{1 - \alpha}{\alpha}(1 - \beta) \\ & = 1577 + 7246 \frac{1 - 70\%}{70\%}(1 - 40\%) \\ & = 3440(\text{LOC}) \end{aligned}
$$

## 4.4. Cost and schedule estimates of the ROSE protocol development

The COCOMO II early design model (1997) with seven cost drivers is employed as the project estimation model and SEI CMM Level 1 is assigned as the process capability maturity for the ROSE protocol development. The size estimate of the total code by hand is 3440 LOC. Seven cost drivers for calculating the effort adjustment factor (EAF) are personnel capability, personnel experience, platform difficulty, product reliability and complexity, required reusability, facility, and development schedule. Based on the university statistics at La Trobe University, Australia, the value 152 is assigned as hours per staff-month and the value AU\$2500 is assigned as the cost per staffmonth for all development phases. The three reports, detail, schedule and activity reports generated by COSTAR, of the ROSE protocol development are shown in Tables 8–10, respectively.

Table 9  
The schedule report of the ROSE protocol development<sup>a</sup>

<table><tr><td rowspan="2">Month</td><td colspan="6">Effort this month (staff-month)</td><td rowspan="2">Cumulative effort</td><td rowspan="2">Cost this month</td><td rowspan="2">Cumulative cost ($K)</td></tr><tr><td>RQ</td><td>PD</td><td>DD</td><td>CT</td><td>IT</td><td>Total</td></tr><tr><td>1</td><td>0.6</td><td>0.1</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.7</td><td>0.7</td><td>1.7</td><td>1.7</td></tr><tr><td>2</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>1.7</td><td>2.5</td><td>4.2</td></tr><tr><td>3</td><td>0.0</td><td>0.3</td><td>1.2</td><td>0.0</td><td>0.0</td><td>1.5</td><td>3.1</td><td>3.6</td><td>7.8</td></tr><tr><td>4</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.6</td><td>0.0</td><td>1.6</td><td>4.8</td><td>4.1</td><td>12.0</td></tr><tr><td>5</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.7</td><td>0.0</td><td>1.7</td><td>6.4</td><td>4.2</td><td>16.1</td></tr><tr><td>6</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.7</td><td>0.8</td><td>1.5</td><td>7.9</td><td>3.7</td><td>19.9</td></tr><tr><td>7</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.8</td><td>0.8</td><td>8.7</td><td>2.0</td><td>21.9</td></tr></table>

<sup>a</sup> Estimate name: ISO ROSE; Estimated ID: 2011; Module name: COCOMO II 97; Module ID: 1997; Process model: COCOMO II.

Table 10  
The activity report of the ROSE protocol development

<table><tr><td rowspan="2">Activity</td><td colspan="5">Effort (person-month)</td><td rowspan="2">Total RQ to IT</td></tr><tr><td>RQ</td><td>PD</td><td>DD</td><td>CT</td><td>IT</td></tr><tr><td>RQ</td><td>0.3</td><td>0.2</td><td>0.1</td><td>0.1</td><td>0.0</td><td>0.7</td></tr><tr><td>PD</td><td>0.1</td><td>0.6</td><td>0.2</td><td>0.2</td><td>0.1</td><td>1.2</td></tr><tr><td>Programming</td><td>0.0</td><td>0.2</td><td>1.2</td><td>1.7</td><td>0.5</td><td>3.6</td></tr><tr><td>Test plans</td><td>0.0</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.0</td><td>0.3</td></tr><tr><td>V and V</td><td>0.0</td><td>0.1</td><td>0.2</td><td>0.2</td><td>0.5</td><td>1.0</td></tr><tr><td>Project office</td><td>0.1</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.1</td><td>0.8</td></tr><tr><td>CM/QA</td><td>0.0</td><td>0.0</td><td>0.2</td><td>0.2</td><td>0.1</td><td>0.6</td></tr><tr><td>Manuals</td><td>0.0</td><td>0.1</td><td>0.1</td><td>0.2</td><td>0.1</td><td>0.6</td></tr><tr><td>Totals</td><td>0.6</td><td>1.4</td><td>2.2</td><td>3.0</td><td>1.6</td><td>8.7</td></tr></table>

<sup>a</sup> Module name: COCOMO II 97; Module ID: 1997; Process Model: COCOMO II.

The detailed report of the ISO ROSE protocol development, shown in Table 8, depicts that the effort of the development phases including requirements (RQ), product design (PD), detailed design (DD), code and unit test (CT) and integrate and test (IT) is 8.7 staff-months, total cost is \$AD 21.9 K, the development duration is 6.6 months, and the project staffing is among 0.6 at the requirement phase to 1.7 at CT phases. The average staffing during 6.6 months of the ISO ROSE protocol development is 1.32 staffs (8.7/6.6).

The schedule report of the ISO ROSE protocol development, shown in Table 9, depicts the monthly schedule planning during the development period of 7 months. It shows the effort in staff-month and cost in dollars for all development phases from requirement to IT phases. The phases from PD through IT are named as the development phase. Table 9 shows that the project spends 0.6 staff-month in the first month on its RQ analysis phase, and 0.8 staff-month in the sixth month and 0.8 staff-month in the seventh month on its IT phase. The cumulative effort and cost during the development period can also be found in Table 9. For example, the effort of 6.4 staff-months is committed in the fifth month and the total cost of AU \$16.1.1 K are spent at the end of the fifth month in the ROSE protocol development project.

The activity report of the ISO ROSE protocol development, shown in Table 10, depicts the effort spent in development activities within the five development phases. For example, the project in the RQ phase spends 0.3 staff-month on RQ analysis activity,

0.1 staff-month on PD activity and 0.1 staff-month on project office activity.

## 5. Conclusions

Over the years, researchers and practitioners have proposed many software size and cost estimation models conducted with an intention of producing a generic model which was assumed to be applicable in a great number of applications [10]. As each application has its own specific features affecting the software size and development cost, a software project estimation model cannot work well if it is applied outside the application domain upon which it was based. On the other hand, without the aid of the software project estimation models, subjective software project estimation techniques relying on expert judgment cannot provide project estimates with required accuracy [11].

This paper has presented two software size models tailored for estimating the sizes of the Estelle specification and implementation of a communication protocol and the procedure of further estimating the software cost and project schedule in the formal communication protocol development environment. With early availability of the software development cost and schedule estimates, project managers are able to effectively allocate limited organization resource, accurately price the communication protocol system to be developed; thus, this paper can help project managers in managing the communication software development project better at the early stage.

## Acknowledgements

This research was supported in part by the National Science Council (NSC) of Taiwan under the grant of a three-year fellowship. The author wishes to thank the chief editor, Dr E.H. Sibley and anonymous reviewers for their constructive comments.

## References

[1] J.M. Schneider, L.F. Mackert, G. Zorntlein, R.J. Velthuys, U. Bar, An integrated environment for developing communication protocol, Computer Networks and ISDN Systems 25 (1), 1992, pp. 43–61.

[2] D. Sidhu, A. Chung, Experience with Formal Methods in Protocol Management, Formal Description Techniques, Elsevier, Amsterdam, 1990, pp. 437–453.

[3] R. Lai, A. Jirachiefpattana, Communication Protocol Specification and Verification, Kluwer Academic Publishers, Dordrecht, 1998.

[4] ISO/TC97/SC21/N1534, Information Processing Systems — Open Systems Interconnection, Guidelines for the Application of FDTs to OSI, Geneva, 1986.

[5] S.J. Huang, R. Lai, On measuring the complexity of an Estelle specification, The Journal of Systems and Software 40 (2), 1998, pp. 161–181.

[6] S.J. Huang, R. Lai, Deriving complexity information from a formal communication protocol specification, Software Practice and Experience 28 (14), 1998, pp. 1465–1491.

[7] S.J. Huang, R. Lai, Estimating the size of an Estelle specification for a communication protocol, in: Proceedings of the 21st Annual International Computer Software and Application Conference, Washington, DC, 1997, pp. 565–568.

[8] N.E. Fenton, S.L. Pfleeger, Software Metrics: A Rigorous and Practical Approach, 2nd Edition, PWS Publishing Company, 1997.

[9] S.D. Conte, H.E. Dunsmore, V.Y. Shen, Software Engineering Metrics and Models, Benjamin/Cummings, Menlo Park, CA, 1986.

[10] B.A. Kitchenham, Empirical studies of assumptions that underlie software cost estimation models, Information and Software Technology 34 (4), 1992, pp. 211–218.

[11] L.A. Laranjeira, Software size estimating of object-oriented systems, IEEE Transaction on Software Engineering 16 (5), 1990, pp. 510–522.

[12] ISO IS 9074, Estelle — A Formal Description Technique Based on Extended State Transition Model, 1989.

[13] S. Budkokski, P. Dembinski, An introduction to Estelle: a specification language for distributed systems, Computer Networks and ISDN Systems 14, 1987, pp. 3–23.

[14] S. Budkokski, Estelle development toolset (EDT), Computer Networks and ISDN Systems 25 (1), 1992, pp. 63–82.

[15] J. Neter, W. Wasserman, M.H. Kutner, Applied Linear Statistical Models: Regression, Analysis and Experimental Designs, 3rd Edition, IRWIN, Homewood, IL, 1990.

[16] ISO/IEC 9072, Information Processing Systems — Open System Interconnection — Remote Operations, Part 1: OSI Realisation — Remote Operations Service Element (ROSE) Service Definition, Part 2: ROSE Protocol Specification, 1992.

[17] B. Boehm, B. Clark, E. Horowitz, C. Wadachy, R. Selby, Cost models for future software life cycle processes: COCOMO II, in: Proceedings of Annuals of Software Engineering, Special Volume on Software Process and Product Management, 1995.

[18] A. Lee, C.H. Cheng, J. Balakrishnan, Software development cost estimation: integrating neural network with cluster analysis, Information and Management 34 (1), 1998, pp. 1–9.

[19] D.P. Sidhu, T.P. Blumer, Semi-automatic implementation of OSI protocol, Computer Networks and ISDN Systems 18, 1989/90, pp. 221–238.

[20] J. Verner, G. Tate, A software size model, IEEE Transaction on Software Engineering 18 (4), 1992, pp. 265–278.

![](/api/attachments/PRGB3QG4/fulltext/images/d206af8d06fea1215b46cedd9bf7fe80400eed5638be514b87432dfa4fb45bdc.jpg)

Sun-Jen Huang received his BA in Industrial Management in 1988, and his MS in Engineering and Technology in 1991, both from National Taiwan Institute of Technology, Taipei, Taiwan. He received a three-year scholarship from the National Science Council, Taiwan in 1995, and commenced his PhD study in the School of Computer Science and Computer Engineering, La Trobe University, Melbourne, Australia,

and obtained his PhD in 1999. He is currently an Assistant Professor at the Department of Information Management, National Taiwan University of Science and Technology, Taipei, Taiwan, and also a member of Software Quality Promotion Committee at Chinese Society for Quality (CSQ). His research interests include Software Engineering Measurement, Software Project Management and Software Quality Engineering. Dr Huang has published papers in journals including Information and Management, Software Practice and Experience, Journal of Systems and Software.
