---
otero_id: 21607
otero_key: "9AX5MPUM"
title: "A decision support system for partial drug testing: DSS-DT"
authors: "Kaushal Chari; Joanna R. Baker; Pamela K. Lattimore"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00047-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for partial drug testing: DSS-DT

Kaushal Chari <sup>a,)</sup>, Joanna R. Baker <sup>b</sup>, Pamela K. Lattimore <sup>c,1</sup>

<sup>a</sup> Information Systems and Decision Sciences, College of Business Administration, UniÕersity of South Florida, 4202 E. Fowler AÕenue, CIS 1040, Tampa, FL 33620-7800, USA

<sup>b</sup> Information and Operations Management, Belk College of Business Administration, UniÕersity of North Carolina at Charlotte, Charlotte, NC 28223-0001, USA

<sup>c</sup> National Institute of Justice, 633 Indiana AÕe., NW, Washington, DC 20531 USA

Accepted 29 July 1998

## Abstract

This paper presents a Decision Support System DSS for the application of partial drug testing to a population ofŽ . individuals with a history of drug abuse. The need for such a system arose in response to a 40% reduction in drug testing funds allocated to probation offices in the State of Illinois’ Intensive Drug Supervision Programs IDSP in 1995. RecentŽ . work in adapting single-attribute Bayesian acceptance sampling to the problem of drug testing in ‘at risk’ populations has shown that the total cost of sampling can be reduced without adversely affecting the proportion of users in the population. The DSS for Drug Testing DSS-DT allows users the opportunity to: 1 readily access information about the prior Ž . Ž . distribution of drug use by population and drug type; 2 generate optimal sampling plans based on current population Ž . inputs; 3 generate near-optimal sampling plans using a heuristic; and 4 evaluate the sensitivity of the solution to changesŽ . Ž . in various input parameters for the drug testing model. Use of DSS-DT expedites the dissemination of the partial drug testing results while offering information and budget planning support to planners charged with implementing a random drug testing procedure. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: DSS application; Acceptance sampling DSS; Criminal justice system support; Drug testing

## 1. Introduction

Drug testing has become an important tool in monitoring the usage of illegal drugs in populations of individuals in various sectors, including the criminal justice system and the transportation industry

ŽBaker et al., 2,3 ; Lattimore et al., 18 . Drug <sup>w</sup> <sup>x</sup> <sup>w x</sup>. testing methodologies are generally applied on an ad hoc basis by individuals responsible for drug testing. These individuals are typically familiar with drug use<sup>r</sup>abuse but are not necessarily familiar with the techniques of random drug testing and systematic approaches to planning, delivering, and monitoring such a program. This paper presents a DSS for Drug Testing DSS-DT that provides the decision maker Ž . Žsuch as a probation officer or a prison warden in the criminal justice system, or a supervisor in a trucking or mass transit office<sup>r</sup>depot the ability to apply . sophisticated quality control techniques to the problem of random, partial drug testing. The need for such a tool is particularly important given that the ability to use 100% testing as a tool for monitoring or controlling illegal drug use is increasingly difficult in the face of declining budgets. Although DSS-DT is applicable in various sectors, in this paper, DSS-DT is presented in the context of the criminal justice system.

The focus of drug testing within the criminal justice system has centered on the who, what and when of drug testing. As the funding for testing has declined, local and state municipalities can no longer rely on methodologies for drug testing that require testing, ‘ . . . all of the people, all of the time.’ In response to the infeasible alternative of testing everyone, every time, efforts have focused on how drug testing dollars can be stretched most effectively while not compromising the traditional functions of drug testing to monitor, control and deter illegal drug use. To the dimensions of whom, what and when to test, is added how? How refers to the proportion of the population to test and the information needed to make that decision—the focus of DSS-DT.

This research develops a DSS that allows decision makers in the criminal justice system the opportunity to use a drug testing cost model for testing drug use which: 1 reduces from 100%, the amount of testingŽ . which must be done to monitor the population; and Ž . 2 provides a decision rule for probation officers involved in drug testing that specifies under what sampling outcome the entire population must be tested. The modeling approach used by DSS-DT is based on single-attribute Bayesian acceptance sampling, a statistical quality control technique that has been applied extensively for monitoring quality of manufactured parts or products. As part of the DSS-DT development effort, a heuristic is developed for generating ‘near-optimal’ sampling plans described Ž in Section 3.2 for large population sizes. This . heuristic, which is interactive, utilizes data stored in a relational database table for generating sampling plans.

Earlier research by Baker et al. 2 developed the <sup>w</sup> <sup>x</sup> theoretical model for application of this methodology to the problem of drug testing. A recent study by Lattimore et al. 18 , applied this methodology to <sup>w</sup> <sup>x</sup> partial drug testing in a population of probationers enrolled in an Intensive Drug Supervision Program Ž . IDSP in six counties in Illinois. This latest study <sup>w</sup> <sup>x</sup> 18 showed that single attribute Bayesian acceptance sampling, when applied to the problem of monitoring drug use among probationers, reduced the total cost of drug testing by up to 56% over 100% testing theŽ status quo.. Partial drug testing, when implemented in these counties, did not result in an increase in the proportion of positive drug users in the population of probationers. The results of this experiment provide the framework for the development and structure of DSS-DT. The purpose of DSS-DT is to provide the probation officer with a decision making and planning tool that minimizes the technical requirements of the user and maximizes the ability of the user to develop an effective partial drug testing strategy.

DSS-DT falls in the category of systems that support optimization models 1 . A notable feature of DSS-DT is the use of indexes stored in relational database tables by a heuristic to speed-up the search for a ‘near-optimal’ sampling plan in the solution space. DSS-DT also facilitates interactions between users and the computer to enable users override default heuristic settings at certain points in the heuristic execution. Users therefore have the ability to influence the search for a sampling plan. Since the model input parameters in the drug testing domain are often imprecise, DSS-DT provides graphical objects such as sliders and dialog boxes to facilitate sensitivity analysis of model solutions to changes in model input parameters. DSS-DT also supports visualization to demonstrate changes in the values of certain input parameters.

DSS-DT fills the need to provide decision support in the drug testing domain. Although a large number of DSS are available in the literature that support planning and analysis 4,12–14,21,24 , the authors<sup>w</sup> <sup>x</sup> are not aware of any specific DSS that has been used in the domain of partial drug testing or of any DSS that has integrated acceptance sampling in the context of drug testing.

This paper is organized into five sections. Section 2 describes the partial drug testing domain. A description of DSS-DT is presented in Section 3. The efficiency and flexibility of DSS-DT is increased through the development and implementation of a solution heuristic for generating near-optimal sampling plans. The heuristic and computation results are also presented in Section 3; the details of the heuristic solution procedure used to obtain an estimate of the sample size are presented in the Appendices. Section 4 describes the cost savings resulting from the use of DSS-DT and Section 5 summarizes the contribution of DSS-DT prototype to improved decision making in an environment where partial drug testing is required.

## 2. Nature of partial drug testing

Testing for the use of illegal drugs has evolved as a routine part of supervision for individuals who are under the control of the criminal justice system. Drug testing programs are applied to detect and monitor the use of illegal drugs as well as to deter drug use through the threat or application of sanctions for positive results e.g., see Wish and Gropper,Ž <sup>w</sup> <sup>x</sup> 26 . As noted in Wish and Gropper 26 , p. 330 ,. <sup>w</sup> <sup>x</sup> . ‘‘Monitoring programs may also deter persons not being tested for using drugs. This is the primary rationale for random testing in the workplace.’’ Several researchers have found that urine testing reduces drug use in criminal justice populations e.g., CarverŽ <sup>w x</sup> <sup>w x</sup> <sup>w x</sup> 10 ; Collins 11 ; and Latessa 19 . However, recog-. nition of the effectiveness of testing does not answer either the question of how much to test or the question of whether it is necessary to test all collected urine specimens. Kennedy 16 conducted an<sup>w</sup> <sup>x</sup> experiment in which only one-third of the tests of collected urine specimens were reported back to probation officers. His results showed no increase in the percent positive specimens, leading him to conclude in part that agencies could reallocate testing dollars to other purposes or could collect more specimens e.g., more frequently or from other popula-Ž tions . The results of the study reported in Lattimore . et al. 18 supported the findings of Kennedy 16<sup>w x</sup> <sup>w x</sup> noting specifically that the benefits of an acceptance sampling approach to partial drug testing include the potential for reduced costs.

The need to develop more efficient testing methodologies in environments where it is not possible or practical to test all of the population is self evident in the face of declining resources. Typically, in probation or other community-based criminal justice populations, the cost associated with 100% testing is prohibitive. In addition, probationers typically learn ways to ‘beat the test’ if non-random sampling is performed or if they are expecting to be tested—for example, by not appearing for a test if they have been using drugs. Because deterrence depends on the threat of testing and also on the threat of being caught, frequent testing is required for most populations in which drug use is high. Random, partial drug testing provides one approach to reduce or at least control drug use while remaining within budget. Providing partial drug testing based minimum cost sampling plans and a decision rule for population testing are the main goals of DSS-DT.

## 3. DSS design

The architecture of DSS-DT is shown in Fig. 1. This architecture supports various objectives of DSS-DT that are as follows: 1 to provide the necessary Ž . support to select parameter values for the drug testing model; 2 to determine the optimal or nearŽ . Ž optimal policies for drug testing; 3 to generate. Ž . sampling plans; and 4 to provide support for ‘Ž . what $i f '$ analyses.

DSS-DT has been developed using models and data on drug use generated as a result of the Illinois experiment on partial drug testing of probationers reported in Lattimore et al. 18 . Model results have<sup>w</sup> <sup>x</sup> been tested and validated against known populations. DSS-DT is implemented for Windows 95 using Borland C<sup>qq</sup> Version 5.0 6 which includes Object<sup>w</sup> <sup>x</sup> Ž Windows Library OWL 7 and Borland DatabaseŽ . <sup>w</sup> <sup>x</sup> Engine BDE 5 and IMSL C Numeric LibraryŽ . <sup>w</sup> <sup>x</sup>. <sup>w</sup> <sup>x</sup> 25 . Various DSS subsystems are described below.

## 3.1. Solution module: acceptance sampling model for optimal solutions

The partial drug testing model, which is solved by the solution module of DSS-DT, is based on a single-sample, single-attribute Bayesian acceptance sampling model for examples and references, see Ž Refs. 2,15,20,23 . Briefly, acceptance sampling en- <sup>w</sup> <sup>x</sup>. tails the random selection of a sample of items from a lot or population ofŽ . N items and inspection of the sampled items on the basis of the selected attribute s . When an economic or expected total costŽ . model is used to identify the acceptance sampling plan, the goal is to select the sample size n and the acceptance number a that jointly minimizes expected total cost. These decision variables are referred to as the sampling plan Ž . n, a . A lot is accepted if there are a or fewer ‘defective’ items in the sample; otherwise, the lot is rejected. Rejected lots may be scrapped or subjected to 100% inspection for a Ž more complete description see Tang et al. 23 or<sup>w</sup> <sup>x</sup> Moskowitz et al. 20 .<sup>w</sup> <sup>x</sup>.

![](/api/attachments/9AX5MPUM/fulltext/images/9827072144c7c708687e51fefdb3f037e10aa1caad9e3a2d268bf08dc86e93be.jpg)  
Fig. 1. Architecture of DSS-DT.

A cost-minimizing acceptance-sampling plan for a population of probationers with a history of drug abuse was developed. For purposes of developing the expected total cost model: 1 a urine specimen isŽ . considered defective or non-conforming if it tests positive for one or more of a finite set of illicit drugs; and 2 a ‘lot’ consists ofŽ . N urine specimens collected from a homogeneous population during a short period of time. For example, in the criminal justice system case, a ‘lot’ can be defined as the specimens produced by a probation population during a one-week period. The following terms are defined for a single period:

N<sup>s</sup>population size;

D<sup>s</sup>number of drug users in the population;

<sup>s</sup>population proportion of drug users, D<sup>r</sup>N;

n<sup>s</sup>number of people tested in the population;

d<sup>s</sup>number of drug users in the sample; and

a<sup>s</sup>the acceptance number. <sup>2</sup>

The objective is to derive a sampling plan Ž . n,a for a single period that minimizes the expected total cost of administering the plan. The plan is implemented by selecting n people at random. If more than a specimens test positive, the remaining Ž . N <sup>y</sup> n people are also tested. An abbreviated description of the model using the notation and assumptions described is provided next; the complete derivation of the model is shown in 2 .<sup>w</sup> <sup>x</sup>

The expected total cost of acceptance sampling is:

$$
\mathrm{ETC} = \mathrm{IC} + \mathrm{ERC} + \mathrm{EAC}.\tag{1}
$$

The total inspection costs IC is given by the fol- Ž . lowing:

$$
\mathrm{IC} = \left(c _ {\mathrm{c}} + c _ {\mathrm{t}}\right) n\tag{2}
$$

Where: $c _ { \mathrm { c } } =$ the cost of collecting a urine specimen; and $c _ { \mathrm { t } } =$ the cost of performing a drug test. <sup>3</sup>

The second component cost considered is the cost of treatment or sanction for a probationer testingŽ . positive for drug use. In order to determine this cost it is necessary to determine the probability that a urine specimen will be accepted. The population is assumed to be at an ‘appropriate’ level of usage if no more than a people test positive. The probability of ‘accepting the population,’ PA, is:

$$
\mathrm{PA} = \sum_ {D = 0} ^ {N} \sum_ {d = 0} ^ {a} h (d | D) \cdot g (D),\tag{3}
$$

where, h d D( <sup><</sup> )<sup>s</sup>the hypergeometric probability of finding d users in a sample of n people when there are D users in the population; and $g ( D ) = { \mathrm { t h } } \epsilon$ prior distribution of users in the population. Here we consider a positive result to be one in which a probationer tests positive for an illegal drug. This expected rejection cost ERC is as follows:Ž .

$$
\begin{array}{r l} \mathrm{ERC} & = \left[ \left(c _ {\mathrm{c}} + c _ {\mathrm{t}}\right) \cdot (N - n) + c _ {\mathrm{s}} \sum_ {D = 0} ^ {N} D \cdot g (D) \right] \\ & \cdot (1 - \mathrm{PA}) \end{array}\tag{4}
$$

Where, $c _ { \mathrm { s } } =$ the cost per incident of a treatment or sanction; and all other terms are previously defined.

The last component cost to be elicited is the most subjective, the penalty associated with failing to detect a positive drug use, or the acceptance cost.

The expected cost of acceptance or the penalty Ž associated with failing to detect a positive user is:.

$$
\begin{array}{r l} \mathrm{EAC} & = \sum_ {D = 0} ^ {N} \sum_ {d = 0} ^ {a} \left[ c _ {\mathrm{A}} \cdot (D - d) + c _ {\mathrm{s}} \cdot d \right] \\ & \quad \cdot h (d | D) \cdot g (D). \end{array}\tag{5}
$$

Where, $c _ { \mathrm { A } } =$ the cost of failing to detect a user or the acceptance cost; and all other terms are previously defined. The likelihood that an individual who is positive for drugs will be involved in a property or violent offense is very small. However, the cost associated with such an event is extremely high from the standpoint of society. Because it is difficult to objectively ‘cost out’ the penalty of a single occasion’s drug use, we asked probation officers what this cost would be relatiÕe to the rejection cost. All probation officers responded that the acceptance cost Ž . or penalty was probably greater than, but not significantly greater than the rejection cost. 4

When all members of a lot are tested, we are screening the lot rather than performing acceptance sampling. The expected total cost of screening is:

$$
\mathrm{ETC} _ {n * = N} = \left(c _ {\mathrm{c}} + c _ {\mathrm{t}}\right) \cdot N + c _ {\mathrm{s}} \cdot E (D),\tag{6}
$$

where $E ( D )$ is the expected number of drug users in the population. When no testing is done, then the expected total cost is:

$$
\mathrm{ETC} _ {n * = 0} = c _ {\mathrm{A}} \cdot E (D),\tag{7}
$$

The optimal sampling plan is obtained by minimizing ETC.

## 3.2. Solution module: heuristic for generating ‘near-optimal’ sampling plans

The expression for ETC is non-convex; therefore many local minima can exist. Earlier empirical work has shown that these local minima are typically ‘close’ to the global minimum 17,18 . Although <sup>w</sup> <sup>x</sup> exhaustive enumeration has been used in Ref. <sup>w</sup> <sup>x</sup> 2,3,17,18 to obtain optimal sampling plans, it is not computationally feasible for medium to large population sizes. <sup>5</sup> Therefore, in order to apply the partial drug testing methodology to large populations, a heuristic has been developed and incorporated into the solution module of DSS-DT. This heuristic provides optimal or near-optimal solutions.

The heuristic primarily does a local search in the solution space to obtain low-cost sampling plans. The starting point for the local search is determined using data stored in an index file, which contains optimal grid points for a population size of 100. For population sizes over 100, the heuristic first finds a local minima solution for the initial population size of 100. The solution obtained for a population of size 100 is then scaled up in stages. At each stage, a local search is performed using the last scaled solution as the starting point. The heuristic terminates when a local minima is reached for the actual population size. For population sizes of 100 or less, the index file is again consulted to obtain the starting point for the local search. However, the estimate obtained from the index file is scaled down in proportion to the actual population in one step, before a local search is performed.

In order to reduce the computation time, the ‘near-optimal’ cost for any given sample size is computed by enumerating only a small range of likely acceptance numbers instead of all possible acceptance numbers. DSS-DT allows system-generated default values for the range of likely acceptance numbers, the starting point and the step size for the local search to be overwritten by the user at the beginning of certain heuristic iterations. Further details of the heuristic can be found in the Appendices.

Table 1 Ž Computational results N<sup>s</sup>100,  <sup>s</sup>0.15, and $\sigma ^ { 2 } = 0 . 0 0 5 )$

<table><tr><td rowspan="2"> $c_A$ </td><td colspan="3"> $c_S$ </td></tr><tr><td>650</td><td>1300</td><td>2600</td></tr><tr><td rowspan="4">650</td><td>Z = 9750.00</td><td>Z = 9750.00</td><td>Z = 9750.00</td></tr><tr><td>n = 0</td><td>N = 0</td><td>n = 0</td></tr><tr><td>a = 0</td><td>A = 0</td><td>a = 0</td></tr><tr><td>gap% = 0</td><td>gap% = 0</td><td>gap% = 0</td></tr><tr><td rowspan="4">1300</td><td>Z = 12421.31</td><td>Z = 18699.80</td><td>Z = 19500.00</td></tr><tr><td>n = 74</td><td>N = 24</td><td>n = 0</td></tr><tr><td>a = 9</td><td>A = 4</td><td>a = 0</td></tr><tr><td>gap% = 0</td><td>gap% = 0</td><td>gap% = 0</td></tr><tr><td rowspan="4">2600</td><td>Z = 13175.80</td><td>Z = 21426.64</td><td>Z = 35238.93</td></tr><tr><td>n = 88</td><td>N = 78</td><td>n = 46</td></tr><tr><td>a = 8</td><td>A = 9</td><td>a = 7</td></tr><tr><td>gap% = 0</td><td>gap% = 0</td><td>gap% = 0</td></tr></table>

Computational results $( N = 2 0 0 ,$ $\varPi = 0 . 1 5 ,$ and $\sigma ^ { 2 } = 0 . 0 0 5 )$

<table><tr><td rowspan="2"> $c_A$ </td><td colspan="3"> $c_S$ </td></tr><tr><td>650</td><td>1300</td><td>2600</td></tr><tr><td rowspan="4">650</td><td>Z = 19500.00</td><td>Z = 19500.00</td><td>Z = 19500.00</td></tr><tr><td>n = 0</td><td>n = 0</td><td>n = 0</td></tr><tr><td>a = 0</td><td>a = 0</td><td>a = 0</td></tr><tr><td>gap% = 0</td><td>gap% = 0</td><td>gap% = 0</td></tr><tr><td rowspan="4">1300</td><td>Z = 24227.46</td><td>Z = 36739.88</td><td>Z = 39000.00</td></tr><tr><td>n = 161</td><td>n = 47</td><td>n = 0</td></tr><tr><td>a = 21</td><td>a = 8</td><td>a = 0</td></tr><tr><td>gap% = 0</td><td>gap% = 0.021</td><td>gap% = 0</td></tr><tr><td rowspan="4">2600</td><td>Z = 25569.76</td><td>Z = 41537.81</td><td>Z = 69455.64</td></tr><tr><td>n = 180</td><td>n = 168</td><td>n = 78</td></tr><tr><td>a = 20</td><td>a = 22</td><td>a = 12</td></tr><tr><td>gap% = 0</td><td>gap% = 0</td><td>gap% = 0</td></tr></table>

Computational results $( N = 1 0 0 ,$ $\Pi = 0 . 3 5 ,$ and $\sigma ^ { 2 } = 0 . 0 1 )$

<table><tr><td rowspan="2"> $c_A$ </td><td colspan="3"> $c_S$ </td></tr><tr><td>650</td><td>1300</td><td>2600</td></tr><tr><td rowspan="4">650</td><td>Z = 22663.12</td><td>Z = 22750.00</td><td>Z = 22750.00</td></tr><tr><td>n = 17</td><td>n = 0</td><td>n = 0</td></tr><tr><td>a = 7</td><td>a = 0</td><td>a = 0</td></tr><tr><td>gap% = 0.013</td><td>gap% = 0</td><td>gap% = 0</td></tr><tr><td rowspan="4">1300</td><td>Z = 24784.03</td><td>Z = 43442.03</td><td>Z = 45500.00</td></tr><tr><td>n = 91</td><td>n = 42</td><td>n = 0</td></tr><tr><td>a = 29</td><td>a = 15</td><td>a = 0</td></tr><tr><td>gap% = 0</td><td>gap% = 0.002</td><td>gap% = 0</td></tr><tr><td rowspan="4">2600</td><td>Z = 25623.00</td><td>Z = 45948.30</td><td>Z = 84146.70</td></tr><tr><td>n = 95</td><td>n = 92</td><td>n = 72</td></tr><tr><td>a = 27</td><td>a = 29</td><td>a = 25</td></tr><tr><td>gap% = 0</td><td>gap% = 0</td><td>gap% = 0.010</td></tr></table>

Table 4 Ž Computational results N<sup>s</sup>200,  <sup>s</sup>0.35, and $\sigma ^ { 2 } = 0 . 0 1 )$

<table><tr><td rowspan="2"> $c_A$ </td><td colspan="3"> $c_S$ </td></tr><tr><td>650</td><td>1300</td><td>2600</td></tr><tr><td rowspan="4">650</td><td>Z = 44836.46</td><td>Z = 45500.00</td><td>Z = 45500.00</td></tr><tr><td>n = 29</td><td>n = 0</td><td>n = 0</td></tr><tr><td>a = 12</td><td>a = 0</td><td>a = 0</td></tr><tr><td>gap% = 0</td><td>gap% = 0</td><td>gap% = 0</td></tr><tr><td rowspan="4">1300</td><td>Z = 48884.37</td><td>Z = 86190.50</td><td>Z = 91000.00</td></tr><tr><td>n = 188</td><td>n = 57</td><td>n = 0</td></tr><tr><td>a = 62</td><td>a = 21</td><td>a = 0</td></tr><tr><td>gap% = 0</td><td>gap% = 0</td><td>gap% = 0</td></tr><tr><td rowspan="4">2600</td><td>Z = 50197.51</td><td>Z = 90457.62</td><td>Z = 167601.62</td></tr><tr><td>n = 193</td><td>n = 189</td><td>n = 99</td></tr><tr><td>a = 60</td><td>a = 62</td><td>a = 35</td></tr><tr><td>gap% = 0</td><td>gap% = 0</td><td>gap% = 0.0004</td></tr></table>

## 3.2.1. EÕaluation of the heuristic

The heuristic incorporated in DSS-DT has been tested on a Pentium 166 MHz machine. Two population sizes of 100 Tables 1 and 3 and 200 Tables 2Ž . Ž and 4 were used in the computational tests. The. sensitivity of the heuristic solution to changes in the prior distribution of population is also reported. The prior distribution of the population is generated by making a discrete approximation of the beta distribution. A prior population distribution with mean<sup>s</sup> 0.15 and variance<sup>s</sup>0.005 is used in Tables 1 and 2; mean<sup>s</sup>0.35 and variance<sup>s</sup>0.01 is used in Tables 3 and 4. In all the computational experiments, $c _ { \mathrm { c } } = \mathrm { U } \mathrm { S }$ \$12.50 and $c _ { \mathrm { t } } = \mathrm { U S }$ \$25.00.

In Tables 1–4, the gap% represents the quantity $( Z - Z ^ { * } ) * 1 0 0 / Z ^ { * }$ , where $Z ^ { * }$ is cost of the optimal sampling plan that is obtained via exhaustive enumeration. The results in Tables 1–4 indicate that the heuristic solution Ž . Z is optimal in 31 out of 36 cases. When the heuristic fails to provide an optimal solution, the maximum gap% based on computa- Ž tional results reported is 0.021%. The computational.

![](/api/attachments/9AX5MPUM/fulltext/images/a8987ae976c27127597016f92b94971ece36696df6951e7f58c3c3cd96aa8421.jpg)  
Fig. 2. GUI of the DSS showing the File pop-up menu.

results point to the high quality of the heuristic solutions. In the case of a population of size 100, the typical time taken by the heuristic is 1 min, whereas the time taken to generate an optimal solution is around 10 min. In the case of a population of size 200, the typical time taken by the heuristic is 2 min, whereas the time taken to generate an optimal solution is around 217 min.

## 3.3. Graphical user interface GUI ( )

The graphical user interface consists of graphical objects such as pop-up menus, sliders, dialog boxes and message boxes. These objects facilitate userfriendly interface. Users can interact with the various subsystems as well as access or update data stored in the data structure located in the primary memory Ž . via this interface. The GUI is implemented using

Borland’s Object Windows Library. Fig. 2 displays the graphical user interface of DSS-DT. Users, using the graphical user interface objects can retrieve population and drug information stored in Paradox databases 8 , and then generate a sampling plan. The<sup>w</sup> <sup>x</sup> New Plan option in the File pop-up menu Fig. 2Ž . can be selected to start a New Plan. Subsequent to selecting an option from the File menu, one of several dialog boxes will appear. For example, when new plan is selected, a dialog box appears which contains two list boxes that display the populations and drugs that exist in the Paradox database tables. The user can then select the population and the drug. Following this, the default cost and population parameters are retrieved from Paradox tables. The slider settings for the mean and variance of the prior distribution are then reset according to the population parameter values retrieved. Accordingly, the

![](/api/attachments/9AX5MPUM/fulltext/images/9933ceaa4d6e3e332d20da870748b2c677b2ade7a3dd91e75eb6d39cc3e902d0.jpg)  
Fig. 3. Population\_Drug Specifications dialog box.

![](/api/attachments/9AX5MPUM/fulltext/images/a5737e0f743b9c9f2c8a400d0473c3037a1b8426b3589b79653fd96c973cd68b.jpg)  
Fig. 4. SolÕe pop-up menu.

graph of the prior distribution is displayed on the screen Fig. 3 . The user has the option of changing Ž . the cost parameters by selecting the Set Parameter option under Parameters pop-up menu. The parameter specifications dialog box is then displayed. <sup>6</sup> This dialog box displays default values, stored in Paradox database tables that are associated with the population and the drug selected. Other than Plan-ID, Population Name and Population Size, the user can change any cost parameters. The user can also change the mean and variance of the prior distribution by moving the two sliders to the desired positions. The prior distribution is automatically redrawn on the screen on a dynamic basis as the sliders move. This allows users to get a feel for the shape of the prior distribution as parameters change.

Having specified the inputs to the DSS, the user can then select the O ptimal Solution, Approximate Solution or Smallest Size Solution option under the SolÕe pop-up menu to generate a sampling plan seeŽ Fig. 4 . Solution modules are responsible for deter-. mining the sampling policy, i.e., the sample size and acceptance number. There are separate modules for optimal solution, approximate solution and smallest sample size solution. These modules take the data stored in the data structure for generating the appropriate sampling policy. The results generated from these modules are then stored back in the data structure for use by the sample generator module. The GUI interfaces with these modules at the frontend. The prior distribution probabilities used in the computation of sampling costs are generated using IMSL C Numeric Library functions. The Optimal solution option uses exhaustive enumeration and is therefore not practical for large population sizes. The Approximate Solution option uses the heuristic de-Ž scribed in Section 3.2 and Appendices A and B to. generate optimal or near-optimal solutions in reasonable times. The Smallest Size solution generates the smallest sample size solution that is within x percent of the optimal, where x is specified by the user.

The Approximate Solution option, that uses the heuristic described in Appendices A and B, displays a dialog box at various heuristic iterations. This dialog box contains default values generated from previous iterations. The user can intervene in the solution process by overriding default values. After the completion of the heuristic procedure, the results of the heuristic procedure i.e., cost, sample size and Ž the acceptance number are displayed in a message . box as illustrated in Fig. 5. The user can then generate a random sample from the test population using the Generate Sample option in the Data pop-up menu. This sample is generated using a random number generator. Based on the random numbers, a list of names belonging to the population stored in Paradox database table is generated. The Sample generator generates a list of persons selected randomly from the population. The size of the list is determined by the solution module used and is stored in the data structure. This is then retrieved from the data structure by the sample generator. The sample generator interfaces with the appropriate Paradox database table to retrieve persons from the population using Borland Database Engine calls. This list can be displayed using the Display Sample option in the Data pop-up menu.

## 3.4. Data management modules

DSS-DT supports several data management functions. This includes adding and deleting population,

![](/api/attachments/9AX5MPUM/fulltext/images/9ad9f854fca5d78d37ca574bcca6e852cb2fd7edc0bb0af4650ea20f7b9e5c6c.jpg)  
Fig. 5. Sampling Plan message box.

Table 6  
Table 5  
Cost benefits of using DSS-DT

<table><tr><td>Population characteristics $( \Pi ,\sigma ^{2})$ </td><td>Cost of screening</td><td>Sampling plan $(n,a)$  using the heuristic</td><td>Heuristic solution cost</td><td>Savings</td></tr><tr><td>(0.01, 0.001)</td><td>US$30,000.00</td><td>(0,0)</td><td>US$10,000.00</td><td>US$20,000.00</td></tr><tr><td>(0.035, 0.001)</td><td>US$55,000.00</td><td>(74,4)</td><td>US$32,040.88</td><td>US$22,959.12</td></tr><tr><td>(0.05, 0.001)</td><td>US$70,000.00</td><td>(98,7)</td><td>US$47,178.35</td><td>US$22,821.65</td></tr></table>

drug, person, and sampling plan information to and from the Paradox tables. In order to add a population record, the user chooses the Add record option in the Data pop-up menu, and then selects Population in the Add record pop-up menu. A population specifications dialog box appears and the user can then specify the population information to be added. DSS-DT also supports external links to Paradox database <sup>w x</sup> <sup>w x</sup> 8 and Quattro 9 spreadsheet environments. This permits querying and analysis of data stored in Paradox tables. For instance, the user can select the Paradox option from the External links pop-up menu. The external linkage module links the DSS-DT to the Paradox database and Quattro spreadsheet environments. This allows data stored in Paradox database tables to be queried, analyzed, graphed or updated. The linkage is implemented using Windows’ Application Program Interface API calls.Ž . The user can override the default path for Paradox if necessary and then select the database file that is opened in the Paradox environment. The selected database file can then be opened in the Paradox environment. All the tools available in the Paradox environment can then be used to query, analyze and update the database table.

Data management modules retrieve and store data on drugs, population, persons and sampling plans. These modules interface with the GUI at the front-end and with the Paradox tables at the back-end. The interface with Paradox tables is implemented using Borland Database Engine calls.

## 4. Benefits of DSS-DT

The probation environment represents one type of environment where DSS-DT can be used. A DSS

<table><tr><td colspan="2">Notation used in the heuristic</td></tr><tr><td>n</td><td>Sample size</td></tr><tr><td>a</td><td>Acceptance number</td></tr><tr><td>N</td><td>Actual population size</td></tr><tr><td>curr_N</td><td>Population size used in the current heuristic iteration</td></tr><tr><td>(a1,a2)</td><td>Lower and upper limits for the range of acceptance numbers</td></tr><tr><td>step</td><td>Step size for local search</td></tr><tr><td>direction</td><td>Search direction. If direction = +, the current sample size is increased by step; else if direction = -, the current sample size is decreased by step; else if direction = 0, nothing is done.</td></tr><tr><td>Cost(n,a)</td><td>In the general case, the cost of sampling plan with a sample size of n and acceptance number a based on Eq. (1) is returned. If n = 0, the no-testing cost based on Eq. (7) is returned. If n = N, the screening cost based on Eq. (6) is returned.</td></tr><tr><td>Costna*</td><td>The minimum value of cost (n,a) for any given sample size n, obtained by selecting the optimal acceptance number a * in some specified range.</td></tr><tr><td>curr_cost</td><td>Current cost</td></tr><tr><td>prev_cost</td><td>Previous cost</td></tr><tr><td>no_test_cost</td><td>Cost obtained by evaluating Eq. (7)</td></tr><tr><td>screen_cost</td><td>Cost of screening obtained by evaluating Eq. (6)</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Initialization
1. Get an initial estimate of n assuming a population size of 100 from the user OR use an index to obtain the estimate.
2. Get an estimate for (a1, a2) from the user OR use default values.
3. Get the value of step for the local search from the user OR use a default value.
4. IF N &lt; 100,
    THEN
    scale down n obtained in step 1 as follows:  $n = \text{int}(n*N/100)$ ,
    set curr_N = N;
    ELSE set curr_N = 100.
5. Determine the direction for the local search by evaluating costs for sample sizes n, min(n+step, curr_N) and max(n-step, 0):
(a)  $cost_{na*} = \min_{a \in \max(a1,0), \ldots, \min(a2,n)} cost(n,a)$ ,
(b)  $cost_{\min(n+step, curr_N)a*} = \min_{a \in \max(a1,0), \ldots, \min(a2,\min(n+step, curr_N))} cost(\min(n+step, curr_N), a)$ ,
(c)  $cost_{\max(n-step, 0)a*} = \min_{a \in \max(a1,0), \ldots, \min(a2,\max(n-step, 0))} cost(\max(n-step, 0), a)$ .
Set direction = 0;
IF  $cost_{\min(n+step, curr_N)a*} &lt; cost_{na*}$  THEN direction = +;
ELSE IF  $cost_{\max(n-step, 0)a*} &lt; cost_{na*}$  THEN direction = -.
6. Set curr_cost =  $cost_{na*}$ ;
 $a = a^{*}$ .
Fig. 6. Initialization phase of the heuristic.
</div>

based on accepted sampling reduces from 100%, the amount of testing which must be performed in a population in order to monitor the use of illegal drugs. In addition, a decision rule is provided via a sampling plan that specifies under what outcomes the entire population must be tested. Thus, as shown in the study by Lattimore et al. 18 , by using <sup>w</sup> <sup>x</sup> acceptance sampling the number of tests can be reduced without increasing drug use. This is very useful to probation office planners who have limited budget.

To demonstrate further the flexibility of the model for a variety of parameter ranges and population sizes, DSS-DT has been applied to the problem of drug testing in a prison. As a first step to developing and implementing a prototype model for the US

Bureau of Prisons, data is obtained for use in DSS-DT. <sup>7</sup> The Bureau of Prison has jurisdiction over all Federal Prisons in the US and mandates a rigorous random testing protocol for prison inmates. Given that there are over 100,000 prisoners in the federal prison system, there is considerable interest in reducing the cost of drug testing throughout the system.

A typical prison inmate population size of 1000 is used. The proportion of drug users is typically 3.5%. The following cost parameter values are used: the cost of collecting and testing the sample $( c _ { \mathrm { c } } + c _ { \mathrm { t } } ) =$

US \$20; Sanction cost $\begin{array} { r } { ( c _ { \mathrm { s } } ) = \mathbf { U } \mathbf { S } \ \mathfrak { H } 1 0 0 0 ; } \end{array}$ Acceptance cost $( c _ { \mathrm { A } } ) \mathrm { = U S } \ \ S 1 0 0 0$ . Table 5 shows the cost of screening the entire population computed using Eq. Ž

Ž .. 6 as well as the cost of acceptance sampling determined by the heuristic. Savings in Table 5 represents the cost savings due to acceptance sam-

```txt
Local Search
7. Set prev_cost = curr_cost;
    prev_n = n; prev_a = a.
8. IF direction = + THEN
    Set n = min(n+step, curr_N);
    Compute cost_na* ; set curr_cost = cost_na* ; a = a* .
    ELSE IF direction = - THEN
    set n = max(n-step, 0) ;
    compute cost_na* ; set curr_cost = cost_na* ; a = a* .
    IF (curr_cost < prev_cost) Goto step 7.
9. Set n = prev_n; a = prev_a; curr_cost = prev_cost.
10. IF screen_cost < curr_cost THEN
    set curr_cost = screen_cost; n = N; a = 0.
11. IF no_test_cost < curr_cost THEN
    set curr_cost = no_sample_cost; n = 0; a = 0.
12. IF (step/2 ≥ 1) THEN
    set al = max(0, a - max(5, 5*stepsize/20))); a2 = min(n, a + max(5, 5*stepsize/20)));
    step = int(step/2).
    Goto step 13.
    ELSE IF (step = 1) AND (curr_N < N) THEN
    scale as follows:
    n = int(min(N/curr_N, 2)*n) ; a = int(min(N/curr_N, 2)*a);
    curr_N = min(N, curr_N*2); set step = int(0.1*curr_N)
    al = max(0, a - max(5, 5*stepsize/20))); a2 = min(n, a + max(5, 5*stepsize/20)).
    Goto step 13.
    ELSE IF (step = 1) AND (curr_N = N) AND (prev_cost = curr_cost) THEN
    stop; solution found.
13. Get n from the user OR use the current value of n.
    Get an estimate for (a1, a2) from the user OR use current values of a1, a2.
    Get the value of step from the user OR use current value of step.
    Goto step 7.
```  
Fig. 7. Local search phase of the heuristic.

![](/api/attachments/9AX5MPUM/fulltext/images/c8e8cd393233fa262c8ab4e87dc6a746580ada68f055d1bc6cfbbdb453ea330b.jpg)  
Fig. 8. Using index when two problem parameters $( \pi , \sigma ^ { 2 } )$ do not match.

pling over screening the entire population. It can be seen from Table 5 that the use of DSS-DT can provide huge savings in the drug testing effort.

## 5. Conclusions and summary

This paper presents DSS-DT, a DSS that can be used by practitioners for partial drug testing. The results from studies on populations of probationers in Illinois 17,18 suggest that partial drug testing can <sup>w</sup> <sup>x</sup> provide a cost-effective way to reduce the cost of drug testing. The results of these studies also indicate the need for a decision support system that provided probation officers the local decision-maker with theŽ . necessary tools to develop an effective drug testing program for their populations.

DSS-DT is specifically suited to the needs of practitioners who are typically familiar with drug use<sup>r</sup>abuse but are not necessarily familiar with the techniques of random drug testing and systematic approaches to planning, delivering, and monitoring such a program. DSS-DT provides a way in which to address budget reductions without abandoning drug testing as a potential tool for monitoring or deterring drug use. Application of such a systematic approach reduces the need to rely on ad hoc approaches that have no long-term benefit. The heuristic presented in this paper to generate sampling plans has been successfully tested for many practical situations. The incorporation of this heuristic in the DSS makes the DSS applicable to situations where the population sizes are much larger, such as in the transportation industry, and various federal and state agencies.

![](/api/attachments/9AX5MPUM/fulltext/images/abc22fd71c6b11eece4e2df08b807b8bbdf8261084ff7ea11bb0abd5048b4c4a.jpg)  
Fig. 9. Using index when none of the parameter values match the index keys.

## Acknowledgements

The authors would like to thank the two anonymous referees for their valued comments. This work was done while the first author was at James Madison University, VA.

## Appendix A. Heuristic solution procedure

The notation used in the heuristic is defined in Table $\begin{array} { r } { 6 ; { } } \end{array}$ the Initialization Phase and the Local Search Phase are given in Figs. 6 and 7, respectively. The index used by the heuristic to obtain the initial estimate of n is based on known optimal solutions obtained for different problem parameters when population size is 100. The expression for the approximate value of the sample $( n _ { \mathrm { e s t } } )$ can be generalized for the case when none of the problem parameters match with the corresponding entries in the index. This generalization is given in Appendix B.

A row in the index is a 5-nary tuple of the form $- ( r , \hat { c } _ { \mathrm { A } } , \varPi , \sigma ^ { 2 } , n )$ —where the following definitions apply.

$\hat { c } _ { \mathrm { A } } =$ the normalized acceptance cost given by the expression $\hat { c } _ { \mathrm { A } } = c _ { \mathrm { A } } / c _ { \mathrm { t } }$ and $\hat { c } _ { \mathrm { t } } = 1 . 0 ;$

$r = \operatorname* { m a x } ( 0 , ( \hat { c } _ { \mathrm { A } } - \hat { c } _ { \mathrm { S } } ) / \hat { c } _ { \mathrm { A } } )$ , where $\hat { c } _ { \mathrm { S } } = \hat { c } _ { \mathrm { S } } / c _ { \mathrm { t } } ;$

$\varPi , \sigma ^ { 2 } =$ the mean and variance of the prior distribution of users, respectively;

n<sup>s</sup>the sample size associated with an index row; $n _ { \mathrm { e s t } } =$ the estimate of sample size for local search. The index values are in the sorted order of r Žprimary .key , $\hat { c } _ { \mathrm { \scriptscriptstyle A } }$ Ž . Ž . secondary key ,  3-nary key , $\sigma ^ { 2 }$ Ž4-nary key . These key values belong to the following sets:.

R<sup>s</sup>set of r values used in the index;

C <sup>s</sup> set of $\hat { c } _ { \mathrm { \scriptscriptstyle A } }$ values used in the index;

M<sup>s</sup>set of values used in the index; and

V<sup>s</sup>set of $\sigma ^ { 2 }$ values used in the index.

The total number of rows in the index is given by $| R | \times | C | \times | M | \times | V | ,$ . The cardinality of sets R, $C ,$ M and V are typically small in order to keep the size of the index within reasonable limits.

The index is maintained in the secondary storage and is retrieved as needed. If the problem parameters match all the key values of the $\bar { i } ^ { \mathrm { { t h } } }$ index row—i.e., $( r _ { i } , \hat { c } _ { \mathrm { A } _ { i } } , \varPi _ { i } , \sigma _ { i } ^ { 2 } )$ —then $n _ { i } ,$ , associated with the $i ^ { \mathrm { { t h } } }$ row is the starting point for the local search. If, on the other hand, the problem parameters do not match one or more key values, then interpolation of index values is performed to obtain a value for $n _ { \mathrm { e s t } } .$

For example, consider the case for parameters $( r , \hat { c } _ { \mathrm { A } } , \varPi , \sigma ^ { 2 } )$ . If $\sigma _ { i } ^ { 2 } < \sigma ^ { 2 } < \sigma _ { i + 1 } ^ { 2 }$ Ži.e., the variance of prior distribution is between the $i ^ { \mathrm { { t h } } }$ and the i<sup>q</sup>1th .variance values in the index , $I I = I I _ { \mathrm { } } = \Omega _ { \mathrm { } m } \mathrm { \Omega } \left( m ^ { \mathrm { t h } } \right.$ mean .value in the index , $\hat { c } _ { \mathrm { A } } = \hat { c } _ { \mathrm { A } k } \ : \left( k ^ { \mathrm { t h } } \ : \ : \hat { c } _ { A } \right.$ value in the .index , and $r = r _ { l } \ ( l ^ { \mathrm { t h } }$ r value in index ; then,.

<table><tr><td colspan="2">Estimate of n for the case in Fig. 9 using an index</td></tr><tr><td>n17 =</td><td>n1 for  $\sigma^{2} = \sigma_{j}^{2}$ </td></tr><tr><td></td><td> $n1 + (n2 - n1)(\sigma^{2} - \sigma_{j}^{2}) / (\sigma_{j+1}^{2} - \sigma_{j}^{2})$ , otherwise</td></tr><tr><td>n18 =</td><td>n3 for  $\sigma^{2} = \sigma_{j}^{2}$ </td></tr><tr><td></td><td> $n3 + (n4 - n3)(\sigma^{2} - \sigma_{j}^{2}) / (\sigma_{j+1}^{2} - \sigma_{j}^{2})$ , otherwise</td></tr><tr><td>n25 =</td><td>n17 for  $\Pi = \Pi_{i}$ </td></tr><tr><td></td><td> $n17 + (n18 - n17)(\Pi - \Pi_{i}) / (\Pi_{i+1} - \Pi_{i})$ , otherwise</td></tr><tr><td>n19 =</td><td>n5 for  $\sigma^{2} = \sigma_{j}^{2}$ </td></tr><tr><td></td><td> $n5 + (n6 - n5)(\sigma^{2} - \sigma_{j}^{2}) / (\sigma_{j+1}^{2} - \sigma_{j}^{2})$ , otherwise</td></tr><tr><td>n20 =</td><td>n7 for  $\sigma^{2} = \sigma_{j}^{2}$ </td></tr><tr><td></td><td> $n7 + (n8 - n7)(\sigma^{2} - \sigma_{j}^{2}) / (\sigma_{j+1}^{2} - \sigma_{j}^{2})$ , otherwise</td></tr><tr><td>n26 =</td><td>n19 for  $\Pi = \Pi_{i}$ </td></tr><tr><td></td><td> $n19 + (n20 - n19)(\Pi - \Pi_{i}) / (\Pi_{i+1} - \Pi_{i})$ , otherwise</td></tr><tr><td>n29 =</td><td>n25 for  $\hat{c}_{\text{A}} = \hat{c}_{\text{A}_{k}}$ </td></tr><tr><td></td><td> $n25 + (n26 - n25)(\hat{c}_{\text{A}} - \hat{c}_{\text{A}_{k}}) / (\hat{c}_{\text{A}_{k+1}} - \hat{c}_{\text{A}_{k}})$ , otherwise</td></tr><tr><td>n21 =</td><td>n9 for  $\sigma^{2} = \sigma_{j}^{2}$ </td></tr><tr><td></td><td> $n9 + (n10 - n9)(\sigma^{2} - \sigma_{j}^{2}) / (\sigma_{j+1}^{2} - \sigma_{j}^{2})$ , otherwise</td></tr><tr><td>n22 =</td><td>n11 for  $\sigma^{2} = \sigma_{j}^{2}$ </td></tr><tr><td></td><td> $n11 + (n12 - n11)(\sigma^{2} - \sigma_{j}^{2}) / (\sigma_{j+1}^{2} - \sigma_{j}^{2})$ , otherwise</td></tr><tr><td>n27 =</td><td>n21 for  $\Pi = \Pi_{i}$ </td></tr><tr><td></td><td> $n21 + (n22 - n21)(\Pi - \Pi_{i}) / (\Pi_{i+1} - \Pi_{i})$ , otherwise</td></tr><tr><td>n23 =</td><td>n13 for  $\sigma^{2} = \sigma_{j}^{2}$ </td></tr><tr><td></td><td> $n13 + (n14 - n13)(\sigma^{2} - \sigma_{j}^{2}) / (\sigma_{j+1}^{2} - \sigma_{j}^{2})$ , otherwise</td></tr><tr><td>n24 =</td><td>n15 for  $\sigma^{2} = \sigma_{j}^{2}$ </td></tr><tr><td></td><td> $n15 + (n16 - n15)(\sigma^{2} - \sigma_{j}^{2}) / (\sigma_{j+1}^{2} - \sigma_{j}^{2})$ , otherwise</td></tr><tr><td>n28 =</td><td>n23 for  $\Pi = \Pi_{i}$ </td></tr><tr><td></td><td> $n23 + (n24 - n23)(\Pi - \Pi_{i}) / (\Pi_{i+1} - \Pi_{i})$ , otherwise</td></tr><tr><td>n30 =</td><td>n27 for  $\hat{c}_{\text{A}} = \hat{c}_{\text{A}_{k}}$ </td></tr><tr><td></td><td> $n27 + (n28 - n27)(\hat{c}_{\text{A}} - \hat{c}_{\text{A}_{k}}) / (\hat{c}_{\text{A}_{k+1}} - \hat{c}_{\text{A}_{k}})$ , otherwise</td></tr><tr><td>n31 =</td><td>n29 for  $r = r_{l}$ </td></tr><tr><td></td><td> $n29 + (n30 - n29)(r - r_{l}) / (r_{l+1} - r_{l})$ , otherwise</td></tr><tr><td colspan="2"> $n_{\text{est}_{100}} = n31$ </td></tr></table>

$$
n _ {\text { est }} = n _ {i} + \left(n _ {i + 1} - n _ {i}\right) \left(\sigma^ {2} - \sigma_ {i} ^ {2}\right) / \left(\sigma_ {i + 1} ^ {2} - \sigma_ {i} ^ {2}\right).
$$

Fig. 8 illustrates the case when two of the problem parameters $( \pi , \sigma ^ { 2 } )$ do not match the corresponding parameter values in the index. If

$$
\Pi_ {i} <   \Pi <   \Pi_ {i + 1}, \sigma_ {j} ^ {2} <   \sigma^ {2} <   \sigma_ {j + 1} ^ {2}, r = r _ {l}, \hat {c} _ {\mathrm{A}} = \hat {c} _ {\mathrm{A} _ {k}}
$$

then in Fig. 8

$$
n 5 = n 1 + (n 2 - n 1) \left(\sigma^ {2} - \sigma_ {j} ^ {2}\right) / \left(\sigma_ {j + 1} ^ {2} - \sigma_ {j} ^ {2}\right)
$$

$$
n 6 = n 3 + (n 4 - n 3) \left(\sigma^ {2} - \sigma_ {j} ^ {2}\right) / \left(\sigma_ {j + 1} ^ {2} - \sigma_ {j} ^ {2}\right)
$$

$$
n _ {\text { est }} = n 5 + (n 6 - n 5) (\Pi - \Pi_ {i}) / (\Pi_ {i + 1} - \Pi_ {i})
$$

The formula for $n _ { \mathrm { e s t } }$ can be generalized for the case when none of the problem parameters match with the corresponding entries in the index. This generalization is given in Appendix B.

## Appendix B. Estimating using an index

Fig. 9 illustrates the general case when none of the problem parameter values match the corresponding entries in the index. The problem parameters— $( r , \hat { c } _ { \mathsf { A } } , \varPi , \sigma ^ { 2 } )$ are in the following ranges:

$r _ { \mathrm { l } } < r < r _ { \mathrm { l + 1 } }$ where r is the $l ^ { \mathrm { t h } } \ r$ value in the index;

$\hat { c } _ { \mathrm { A } _ { k } } < \hat { c } _ { \mathrm { A } } < \hat { c } _ { \mathrm { A } _ { k + } }$ where $\hat { c } _ { { \bf A } _ { k } }$ is the $k ^ { \mathrm { t h } } \hat { c } _ { \mathrm { A } }$ value in the index;

$\varPi _ { i } < \varPi < \varPi _ { i + 1 }$ where $\textstyle { \boldsymbol { \pi } } _ { i }$ is the $i ^ { \mathrm { t h } } \ \pi$ value in the index; and

$\sigma _ { j } ^ { 2 } < \sigma ^ { 2 } < \sigma _ { j + } ^ { 2 }$ where <sub>1</sub> ${ \sigma _ { j } } ^ { 2 }$ is the $j ^ { \mathrm { t h } } \sigma ^ { 2 }$ value in the index.

The expressions for n associated with the various nodes in Fig. 9 are presented in Table 7.

## References

<sup>w</sup> <sup>x</sup> 1 S. Alter, A Taxonomy of Decision Support Systems, Sloan Management Review, Fall, 1973, pp. 33–41.

<sup>w</sup> <sup>x</sup> 2 J.R. Baker, P.K. Lattimore, L.A. Matheson, Constructing optimal drug-testing plans using a Bayesian acceptance sampling model, Mathematical and Computer Modeling 17 2Ž . Ž .1996 77–88.

<sup>w</sup> <sup>x</sup> 3 J.R. Baker, P.K. Lattimore, L.A. Matheson, Cost-effective drug testing in the transportation industry, IIE Transactions 28 1996 735–744.Ž .

<sup>w</sup> <sup>x</sup> 4 C. Basnet, L. Foulds, M. Igbaria, FleetManager: a microcomputer-based decision support system for vehicle routing, Decision Support Systems 16 1996 195–207.Ž .

<sup>w</sup> <sup>x</sup> 5 Borland International, Borland Database Engine, Scotts Valley, CA 95067-0001, 1996.

<sup>w</sup> <sup>x</sup> 6 Borland International, C<sup>qq</sup> User’s Guide, Version 5.0, Scotts Valley, CA, 95067-0001, 1996.

<sup>w</sup> <sup>x</sup> 7 Borland International, Object Windows for C<sup>qq</sup>, Scotts Valley, CA 95067-0001, 1996.

<sup>w</sup> <sup>x</sup> 8 Borland International, Paradox for Windows, Version 4.5, Scotts Valley, CA, 95067-0001.

<sup>w</sup> <sup>x</sup> 9 Borland International, Quattro for Windows, Version 5.0, Scotts Valley, CA, 95067-0001.

<sup>w</sup> <sup>x</sup> 10 J.A. Carver, Drugs and Crime: Controlling Use and Reducing Risk through Testing. Washington, DC: National Institute of Justice, 1986.

<sup>w</sup> <sup>x</sup>11 J.J. Collins, Policy choices in urine testing of probationers and parolees, Presentation to the American Society of Criminology, Reno, NV, 1989.

<sup>w</sup> <sup>x</sup> 12 J. Couillard, A decision support system for vehicle fleet planning, Decision Support Systems 9 2 1993 149–159.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 M. Gopalakrishnan, S. Gopalakrishnan, D.M. Miller, A decision support system for scheduling personnel in a newspaper publishing environment, Interfaces 23 4 1993 104–115.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 G. Guariso, M. Hitz, H. Werthner, An integrated simulation and optimization modeling environment for decision support, Decision Support Systems 16 1996 103–117.Ž .

<sup>w</sup> <sup>x</sup> 15 A. Hald, The determination of single-sampling plans based on prior distribution and costs, Technometrics 2 1960 275– Ž . 340.

<sup>w</sup> <sup>x</sup> 16 E. Kennedy, The Effects of Partial Drug Testing on Drug-Use Behavior and Self-Disclosure Validity, Chicago, IL Criminal Justice Information Authority, 1993.

<sup>w</sup> <sup>x</sup> 17 P.K. Lattimore, J.R. Baker, E. Kennedy, L.A. Matheson, Effectiveness of partial drug testing: evaluation of an acceptance sampling approach, Working Paper Number 95-01, National Institute of Justice, Washington, DC, 1995.

<sup>w</sup> <sup>x</sup> 18 P.K. Lattimore, J.R. Baker, L.A. Matheson, Effectiveness of partial drug testing: the Illinois experiment, Operations Research 44 2 1996 274–286.Ž . Ž .

<sup>w</sup> <sup>x</sup> 19 E.J. Latessa, The effects of random drug testing on probationers, Presentation to the Academy of Criminal Justice Sciences, Nashville, TN, 1991.

<sup>w</sup> <sup>x</sup>20 H. Moskowitz, R. Plants, K. Tang, Multistage multiattribute acceptance sampling in serial production systems, IIE Transactions 16 1986 130–137.Ž .

<sup>w</sup> <sup>x</sup> 21 R. Ravichandran, A decision support system for stochastic cost-volume-profit analysis, Decision Support Systems 10 4Ž . Ž .1993 379–399.

<sup>w</sup> <sup>x</sup> 22 C.P. Rydell, S.S. Everingham, Controlling cocaine: supply versus demand programs, RAND, Drug Policy Research Center, Santa Monica, CA, 1994.

<sup>w</sup> <sup>x</sup> 23 K. Tang, R. Plante, H. Moskowitz, Multiattribute Bayesian

acceptance sampling plans under nondestructive inspection, Management Science 32 1986 739–750.Ž .

24 E. Turban, Decision Support and Expert Systems, 2nd edn., Macmillan Publishing, New York, 1990.

<sup>w</sup> <sup>x</sup> 25 Visual Numerics, IMSL C Numerical Libraries, Houston, TX 77042.

<sup>w</sup> <sup>x</sup> 26 E.D. Wish, B.A. Gropper, Drug testing by the criminal justice system: methods, research, and applications. In: Crime and Justice, Vol. 13, Drugs and Crime, The University of Chicago, Chicago, 1990, 321–391.

Kaushal Chari currently teaches in the Information Systems Area at the University of South Florida. He obtained a B. Tech. in Mechanical Engineering from the Indian Institute of Technology Kanpur, followed by an M.B.A. and Ph.D. from the University of Iowa. His research has been published in journals such as IN-FORMS Journal on Computing, Telecommunication Systems, Decision Support Systems, European Journal of Operational Research, Computers and Operations Research and Omega. His research interests include telecommunications network design, model management systems, software agents and intelligent systems.

Joanna Baker is the Director of the School of Information Tech nology and Professor of Information and Operations Management. Joanna Baker is the former Chairperson of the Information and operations Management department at UNC Charlotte. She specializes in applied research mathematical programming and decision support system in the public sector. Prior to joining UNC Charlotte she held positions as Professor and Head of the Information and Decision Sciences Department at James Madison University 1993–1996 and Professor of Management Science at Vir-Ž . ginia Tech 1985–1993 . She holds a Ph.D. in Engineering Man-Ž . agement with a minor in Systems Engineering from Clemson University 1983 . Her teaching interests lie in the areas of appliedŽ . artificial intelligence, decision support systems, and management science. Her research interests are in the application of operations research<sup>r</sup>management science techniques to the solution of large-scale system public sector applications including health care planning, transportation systems, and criminal justice operations. She has published in such journals as the Annals of Operational Research, Benchmarking for Quality and ProductiÕity, Decision Sciences, European Journal of Operations Research, IIE Transactions, International Journal of Production Research, Journal of Mathematical Modelling, Journal of the Operational Research Society, Journal of QuantitatiÕe Criminology, NaÕal Research Logistics, Operations Research, Socio-Economic Planning Sciences, and others. She is active in National and Southeastern regions of the Decision Sciences Institute DSI , having served asŽ . Program Chair and President of the Southeastern Region and Associate Program Chair of National. She served as Vice President at Large and a member of the Board of Directors of National DSI. She is also active in National INFORMS and is a member of the Board of Southeast INFORMS, having served as Program Chair and President of the Southeastern Chapter.

Pamela K. Lattimore is Director of the Criminal Justice and Criminal Behavior Division, Office of Research and Evaluation, the National Institute of Justice in Washington, DC. She directs the Institute’s extramural research and evaluation programs in the areas of corrections, courts, sentencing, criminal behaviour and victimization, as well as coordinates the intramural research activities in those areas and policing. She conducts research in criminal behavior and criminal justice operations, including recent research focusing on factors associated with city-level homicide trends, the development of methods for classifying probation populations for risk, and improving the cost-effectiveness of drug testing programs. She has also worked for a number of years on models of criminal recidivism, focusing primarily on hazard models and, more recently, count models. Her most recent research appears in Operations Research, Socio-Economic Planning Sciences, the Journal of Research in Crime and Delinquency, Criminology, Journal of Quantitative Criminology, Mathematical and Computer Modelling, and the Journal of Economic Behavior and Organization, among others. She received the Ph.D. in economics from the University of North Carolina at Chapel Hill in 1987.
