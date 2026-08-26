---
otero_id: 26689
otero_key: "XFUFJ7GT"
title: "Designing Information Systems to Optimize the Accuracy-Timeliness Tradeoff"
authors: "Donald P. Ballou; Harold L. Pazer"
year: "1995"
journal: "Information Systems Research"
doi: "10.1287/isre.6.1.51"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/XFUFJ7GT/fulltext/images/6c1dccf2bb9844a79fba2b394d5c1bb91d36ae8c7390fb0ebeb14f7fc7500b0a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Designing Information Systems to Optimize the Accuracy-Timeliness Tradeoff

Donald P. Ballou, Harold L. Pazer,

To cite this article:

Donald P. Ballou, Harold L. Pazer, (1995) Designing Information Systems to Optimize the Accuracy-Timeliness Tradeoff. Information Systems Research 6(1):51-72. http://dx.doi.org/10.1287/isre.6.1.51

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1995 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/XFUFJ7GT/fulltext/images/bdbcb8bd044fa1a9f5369469181cb9a326b83a830954c6177f07e410062e5afb.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Designing Information Systems to Optimize the Accuracy-timeliness Tradeoff

Donald P. Ballou

School of Business

SUNY-Albany

Albany. New York 12222

Harold L. Pazer

School of Business

SU NY-Albany

.Albanv, New York 12222

It is well known, of course, that the assessment of this month's economic activity will improve with the passage of time. The same situation exists for many of the inputs to managerial and strategic decision processes. Information regarding some situation or activity at a fixed point in time becomes better with the passage of time. However, as a consequence of the dynamic nature of many environments, the information also becomes less relevant over time. This balance between using current but inaccurate information or accurate but outdated information we call the accuracy-timeliness tradeoff. Through analysis of a generic family of environments, procedures are suggested for reducing the negative consequences of this tradeoff. In many of these situations, rather general knowledge concerning relative weights and shapes of functions is sufficient to determine optimizing strategies

data quality—infcrmation qualıty—accuracy-—tımeliness—decision makıng

## 1. Introduction

he importance of information systems designed to support managerial decision making and planning has directed attention toward the need to manage the information resource as effectively as possible. Making correct decisions and developing sound plans are clearly dependent upon the qualitv of the data used and the correctness of the processing procedures that transform the data into the required information. Since in an imperfect world neither data nor processes are perfect, those charged with management of the information resource should identify cost-effective strategies to improve critical data items and processes in the context of required decisions and plans.

Often the information utilized by decision and planning processes becomes better over time. This is illustrated hy economic statistics produced by the federal government such as estimates for GDP, employment growth, savings rate. consumer spending, and so forth. Preliminary estimates are released based on the best available data. With the passage of time the quality of the data improves, which allows for the release of updated. more accurate revisions to the various econoniic statistics.

Although the available information regarding some phenomenon at a fixed point in time may become more accurate with the passage of time, the underlying environment the information is intended to describe is also changing, a consequence of the dynamic nature of most environments. Hence as the information becomes more accurate (relative to the fixed point in time) it also becomes less relevant for decision and planning purposes. Thus some balance needs to be struck between using current but inaccurate information and accurate but outdated information. This balance is referred to throughout this paper as the accuracy-timeliness tradeoff.

This article is directed to two not necessarily distinct audiences. First are those who, on an ongoing basis, confront the accuracy-timeliness tradeoff and must decide whether to act based on preliminary estimates or to defer decisions while waiting for more accurate assessments. Second are those whose responsibility is to analyze and redesign information systems to provide greater responsiveness to the accuracy-timeliness needs of decision makers.

In this context, this work presents concepts and procedures that, for a given situation or environment, can be used to analyze the accuracy-timeliness tradeoff for the information system currently in place and provide information regarding the impact that redesigning the system would have on the tradeoff. Provided resources are made available, it is usually possible to improve both data gathering and data processing activities so as to make better quality information available sooner, which of course would improve the accuracy-timeliness tradeoff. Also decision makers need to know when the accuracy-timeliness tradeoff is optimal. In other words at what point should the decision maker stop waiting for better information and act on the basis of what is available? The goal is to identify that strategy for changing the information system so as to optimize the accuracy-timeliness tradeoff in a way that minimizes cost and identifies that point in time at which the decision maker should act.

Traditionally, accuracy refers to the degree to which the reported value is in conformance with the actual or true value. Thus accuracy is one of the dimensions of data quality. Others include timeliness, consistency, completeness, relevance, reliability, etc. (DeLone and McLean 1992). Some of the dimensions of data quality such as completeness may also improve with the passage of time. Under such circumstances this work applies equally well to the completeness-timeliness tradeoff. For the sake of simplicity and specificity, however, the ideas presented are developed in the context of the accuracy-timeliness tradeoff.

The approach described in this paper is general in that it is applicable to situations other than the one we analyze. There are, of course, other tradeoffs regarding timeli ness, accuracy, and cost. For example, it could be that accuracy is constant over time but there is a tradeoff between the cost of obtaining data and the time required to do so. In essence, are we better off committing resources to obtain data quickly or spending less and taking longer to get the data? The procedure is also potentially applicable to various combinations of data quality attributes. This issue of generality is examined in some detail in the final section.

## Background

Constraints imposed by, and difficulties arising from, accuracy-timeliness tradeoffs appear to be widely recognized by decision makers. For example, the Associated Press quotes a former official of the U.S. Commerce Department as saying:

“Greenspan (chairman of the Federal Reserve Board) wanted to have as much information as he could as early as possıble for the conduct of monetary policy You always face the tradeoff between timeliness and accuracy " (Crutsinger 1989)

Implicit in this statement is the assumption that accuracy improves with time. While this need not always be true, there is a large and important subset for which it is. Our work is in this context.

The scenario that this work is designed to address involves periodic decision making and review by senior officials of an organization. One motivating example would be the periodic meetings of the Open Market Committee of the Federal Reserve Board. Another would be the periodic reviews of a corporation conducted by its senior executives on an annual or some other basis. In both those cases a considerable quantity and diversity of data would be required. Clearly it is desirable that such meetings be held as soon as possible after the data first become available. (A review of the previous year's activities is more valuable in Januarv than in September.) On the other hand it may be better to wait than make wrong decisions based on inaccurate information. The question thus becomes: when should meetings of this sort be scheduled given the improvement over time of the data that serves as the basis for decision making? Another question is: what changes to the information systems that supply the needed data would be beneficial in that better quality data would be made available sooner?

Much of the research related to the accuracy-timeliness tradeoff has been carried out in the discipline of information economics. Some of the theory underlving this field is found in Marschak and Radner (1972). Examples of work in this area include Ijiri and Itami (1973), Stohr (1979) and especially Hilton (1979, 1981). The latter explicitly considers the accuracy-timeliness tradeoff in the context of cost-volumeprofit decisions. The work uses a set of assumptions specific to the application to specialize a general expression for the utility of an information system Although the analysis takes place in this specific context, thé approach is rather general. A paper by Ahituv (1980) examines issues involved with the evaluation of information systems from the perspective of information economics. Various utility attributes are systematically examined and modeled.

Research on information quality and the consequences of inadequate information is also relevant. A recent study by DeLone and McLean (1992) discusses information quality as one of the dimensions of successful information systems. A paper by Goodhue et al. (1988) reports on field research that highlights the diversity of problems arising from poorly managed data. Davis and Olson (1985) discuss a variety of issues related to data quality and its potential impact on organizational effectiveness. Ballou and Pazer (1990) examine the consequences for correct decision making of errors in evaluation and criteria. Analyses of the impact of input errors on various outputs are found in Alonso (1968), Ballou and Pazer (1985) and Ballou et al. (1987).

Related research consists of studies of specific situations. Laudon (1986) systematically identfied and analyzed errors in the criminal justice system. Johnson et al. (1981) determined the error rate for financial and inventory systems for a variety of companies and found the rates on average to be surprisingly high in both cases. Mahmoud and Rice (1988) examined accuracy of data in external databases with emphasis on procedures and controls designed to ensure the integrity of the data.

Nesbit (1985) and Boockholdt (1989) consider data integrity problems in the context of micro-based computer systems.

There has also been some work that addresses the issue of how best to enhance the quality of existing, stored data. Morey (1982) examined data from a military personnel system and developed statistically-based procedures for identifying and correcting errors. Perry (1983) addressed data quality assurance as part of the larger issue of quality of information systems. Ballou and Tayi (1989) developed procedures to allocate limited resources available for data quality enhancement in the context of multiple data sets.

Work that specifically addresses data integrity in data base systems includes Brodie (1980) and Date (1990). The difficulty of identifying existing errors. even sizable ones, is described in Ricketts (1990). Another aspect relates to keeping data errors out of computer-based systems. Various authors and researchers have addressed this, including Martin (1973) and members of the accounting profession, e.g., Cushing (1974) and Hamlen (1980).

The next section presents the theoretical framework which supports analysis of timeliness-accuracy tradeoffs. This general formulation is used as the basis for a class of environments described in §3. The analysis of those environments is found in §4. The final section contains some concluding remarks.

## 2. Theoretical Framework for Analysis of Accuracy-Timeliness Tradeoffs

This section presents a theoretical framework requiring knowledge of certain functional relationships. If these are known or can be determined, then mathematical procedures can be used to provide answers to questions such as those posed above. It may well be, however, that the required functional relationships cannot be readily determined. In this case an alternative approach such as that described in §3 can be followed. That involves using generic families to approximate the required functions. The results provide insights, for example, regarding environments for which early or late decisions are appropriate. A limitation of that approach, however, is that unlike the general theorv presented in this section, it is not possible to determine an overall optimal tradeoff. In any case the material in $\ S 3$ is presented in the context of the framework described below.

## Analvtical Framework

The analysis involves the set V of information whose accuracy improves over time. (All notation introduced in this section is summarized in Table 1.) As indicated, this work assumes a repetitive framework, i.e., the information set $V ^ { \prime } \mathrm { i } s$ generated repeatedly over time and for each cycle the kinds of decisions that utilize V’ can be anticipated. Let $T$ represent time with $T = 0$ marking the point at which V is first made available. For example, the earliest point at which the annual review could be held would be represented by $T = 0$ . Let E represent a measure of the accuracy of the data contained in V’, and let $E = 0$ signify that the data are without error. By this we do not necessarily mean that the data are perfect but rather that the quality of each of the components of $V ^ { ' }$ is as good as can be achieved (relative to the fixed point in time T $\mathbf { \eta } = 0 )$ . Since we assume that over time the quality of each component of V improves or at least does not worsen, the quality of the data is never worse than at $T = 0 .$ . Clearly the quality of each component of V’ will differ from cycle to cycle. For our purposes it is sufficient to consider the average quality of the set V at time 0. This can be obtained, for example, by using a weighted average of the average quality of each of the componerts at $T = 0$ . To provide a standard frame of reference, we assume that this average overall quality measure at $T = 0$ is scaled and represented bv the value $E = 1$ With $E = 0$ signifying data without error, we see that E must satisfy $0 \leq E \leq 1$

<table><tr><td colspan="2">TABLE 1Notation for General Model</td></tr><tr><td>T</td><td>Time, with T = 0 denoting when information first made available</td></tr><tr><td>E</td><td>Error level, with E = 0 representing error free information and E = 1 denoting error level at time T = 0</td></tr><tr><td>U(T,E)</td><td>Utility of information at time T with error level E.</td></tr><tr><td>V</td><td>Set of information upon which decision is based.</td></tr><tr><td>c</td><td>Information system currently in place.</td></tr><tr><td>Tc</td><td>For current information system point in time at which information becomes error free</td></tr><tr><td>Γc</td><td>For current information system path in TL plane representing decrease in error over time.</td></tr><tr><td>g_c(T)</td><td>Analytic representation of Γ_c.</td></tr><tr><td>U_max(c)</td><td>For current information system maximum value for U(T, g_i(T)), 0 ≤ I ≤ T_c, i.e., best achievable utility value for current system.</td></tr><tr><td>S</td><td>Set of strategies for redesigning current information system</td></tr><tr><td>s</td><td>Member of set of strategies S (c is a member of S).</td></tr><tr><td>E_s</td><td>Initial error in I under strategy s (E_s ≤ 1).</td></tr><tr><td>T_s</td><td>Time when information V becomes error free under strategy s (I_s ≤ T_c)</td></tr><tr><td>Γ_s</td><td>Path representing decrease in error over time under strategy s</td></tr><tr><td>g_s(T)</td><td>Analytic representation of Γ_s.</td></tr><tr><td>U_max(s)</td><td>Maximum value of accuracy-timeliness utility function U(I, E) achievable under strategy s.</td></tr><tr><td>Cost(s)</td><td>Cost required for the implementation of strategy s</td></tr><tr><td>ξ</td><td>Strategy that maximizes U_max(s) Cost(s)</td></tr><tr><td>I_0</td><td>Point in the time at which U(I, g(I)) achieves its maximum</td></tr></table>

Presumably the information I’in question has some worth or utility to the decision maker. The utility may well depend on a host of factors. This analysis, however, is concerned with the accuracv-timeliness tradeoff and so to isolate the factors relevant for our purposes, we postulate a utility function $L ^ { \prime } = l ( T , E )$ dependent upon the timeliness and accuracy dimensions. Since the more timelv and/or accurate the information is, the more useful it is to decision makers, the function U has an absolute maximum at (0, 0). One would expect that for a fixed value of time, the utility of the information would decrease as the error level increases. Thus the utility function should be monotone decreasing in E. Similarly it should be monotone decreasing with respect to T. This is consistent with the work of Ahituv (1980) and Hilton (1979).

One would assume that the utility function l' would depend on the values of the components of l’ as well as E and T. For example, at a given point in time with the same error magnitude, information that the demand for a certain product is high would have a different impact regarding production decisions than would a report that the demand is low. The implication is that decisions are made dynamically to adjust to circumstances as information becomes available. Ihis in essence is the framework employed by Hilton (1979) and ljirı and Itamı (1973).

Our framework is different in that it precludes dynamic decision making. An example may help to clarify this issue. As mentioned, fash esumates for GDP are subject to multiple revisions. Suppose the underly ing data gathering and processing systems have been modified so as to reduce the impact of the accuracy-timeliness tradeoff in those cases for which there are large decreases in the flash estimate for GDP compared with the previous quarter. (In such cases monetary policy might need to be modified.) To handle this situation it could be that the supporting information systems were changed to both reduce the initial error and shorten the time until the “correct" information becomes available. However, if the flash GDP estimate is little changed from the previous quarter, both actions probably are unnecessary. Hence the changes made to the supporting information systems would be more valuable in some cycles than in others.

In our case V’ is the value for GDP. We assume that the information systems that support the determination of GDP are in place and cannot be rapidly changed. Often data gathering activities involve multiple parties at dispersed locations who are not under the immediate control of the decision makers, those using the information in question. In such situations only minimal changes can be made during a particular cycle to alter the quality of data collected and made available. Thus the problem is how best to modify data gathering and processing procedures so as to minimize the impact of the accuracy-timeliness tradeoffs over multiple cycles. Once changes have been made, they cannot easily be modified or redone. Thus any changes instituted to improve the accuracy-timeliness tradeoff will be more effective or valuable in some cycles than in others. As indicated, this work provides a framework that yields information on the kinds of changes that should be made.

We adopt the following strategy regarding the accuracy-timeliness tradeoff. A decision is made as to which of the spectrum of past and presumably future environments should be optimized. For the environment chosen the analysis describes how the impact of the accuracy-timeliness tradeoff can be minimized. Information systems are then modified accordingly with the understanding that the resulting systems will be more valuable for the optimized environment than for the others.

The goal of optimizing the accuracy-timeliness tradeoff in a cost-effective manner can be achieved by committing resources in a judicious fashion so as to improve the current situation, notationally represented by c. Let $T _ { c }$ represent the point in time when the information becomes error free. Conceptually there is an error reduction path $\Gamma _ { c }$ in the TE plane from (0, 1) to $( T _ { c } , 0 )$ representing the decrease in error over time. In practice this path would be discontinuous, as reductions in $E$ would not be made continuously, but for modeling purposes we can approximate any discontinuous curve with a continuous one. Thus $\Gamma _ { c }$ can be represented analytically by a continuous error reduction function $g = g _ { c } ( T ) , 0 \leq T \leq T _ { c }$

Currently the decision maker should use the information in V available at time $T _ { 0 } .$ that time which maximizes the quantity $U ( T , g _ { c } ( T ) )$ , with T satisfying $0 \le T \le T _ { c }$ .. Let $U _ { \mathrm { m a x } } ( c )$ represent the maximum utility value currently attainable, $\mathrm { i . e . }$

$$
U _ {\max} (c) = U \left(T _ {0}, g _ {c} \left(T _ {0}\right)\right), \quad 0 \leq T _ {0} \leq 1.
$$

Viewing this situation geometrically, the decision maker should follow $\Gamma _ { c }$ until that time $T _ { 0 }$ at which the surface U above $\Gamma _ { c }$ is at its highest level. This assumes, of course. a static environment, that is, no effort is made to reduce the current initial error or change data gathering and/or processing activities in any way so as to alter $\Gamma _ { c } .$

It may well be that data gathering and data processing activities continue after $T _ { 0 } .$ the time at which the decision maker uses the available estimate for V. For example, even though decisions may be made based on GDP estimates that are not final, the process of refining those values continues. For our purposes what happens in the way of improvement to the information after $T _ { \parallel }$ is irrelevant, as the analvsis that identified the value for $T _ { 0 }$ has already taken that into account.

A more significant problem is to identify the types of changes that should be made to the information system currently in place, (e.g., reduce the initial error. shorten $T _ { c }$ alter $\Gamma _ { c } )$ so as to obtain a utility value larger than $\mathcal { L } _ { \mathrm { m a x } } ( \boldsymbol { c } ^ { \prime } )$ . Clearly a cost would be incurred by such actions, but it may well be that the net utility (value for U once the additional costs have been included) would still be larger than $\chi _ { \mathrm { m a x } } ( \iota )$

Improving the accuracy-tımeliness tradeoff can be formulated analytically as an optimization problem. Let S denote a set of potential strategies, $( \boldsymbol { c } , s _ { 1 } , \boldsymbol { \gamma } _ { 2 } , \boldsymbol { \mu } , \boldsymbol { \gamma } _ { n } )$ . The information systems strategy c represents the optimal tradeoff under the current information system, i.e., a choice of the time $T _ { 0 } \left( 0 < T _ { \mathrm { 1 } } < T _ { c } \right)$ at which the decision making is to take place given the current initial information accuracy $( E = 1 )$ and time $T _ { c }$ when the information accuracy ceases to improve. An information systems redesign strategy s is a collection of actions that result in an initial error $E _ { s } , ( E _ { s } \leq 1 )$ , a time $T _ { s }$ when the information becomes error free. $T , \le I _ { i } , a$ path $\Gamma _ { s } \colon g _ { s } = g _ { s } ( T )$ from $( 0 , E _ { s } )$ to $( T , \allowbreak 0 )$ that captures the reduction of error over time, and value $T _ { 0 }$ at which time optirnal decision making would occur.

Let

$$
U _ {\max} (s) = \max U (T, g _ {s} (T)), \quad 0 \leq T \leq T _ {s}.
$$

The symbol $U _ { \mathrm { m a x } } ( s )$ represents the largest utility value that can be achieved by following $\Gamma _ { s }$ . It also determines $T _ { 0 }$ . Let Cost(s) represent the cost of this strategy, measured in units compatible with U'. Then the goal is to identify that strategy  such that

$$
U _ {\max} (\tilde {s}) - \operatorname{Cost} (\tilde {s}) = \max [ U _ {\max} (s) - \operatorname{Cost} (s) ].
$$

If $U _ { \mathrm { m a x } } ( \tilde { S } ) - \mathrm { C o s t } ( \tilde { s } ) > U _ { \mathrm { m a x } } ( c ^ { . } )$ , then Î should be implemented.

An overview of the general structure of the analysis described above is provided by Figure 1.

As will be demonstrated in the next section, it is not difficult to determine $U _ { \mathrm { m a x } } ( s )$ provided the accuracy-timeliness utility function $\it U ( 1 . 5 ) , \it T . \ . \ E ,$ , and $g _ { * } ( T )$ are known. A potential problem arises from having an unlımited number of possible strategies. In practice, however, there would be a relatively small number of available and feasible alternative strategies. Each could be evaluated to determine the best. The real difficulty lies in determining reasonable analytical expressions for $\ell ( T , E )$ and $g _ { s } ( T )$ . One way of addressing this difficulty is described in the next section.

## 3. Experimental Framework for Exploration of Accuracy-timeliness Tradeoffs

In this section we use the quantitative framework from the previous section to describe an environment that will be used in §4 to generate information regarding accuracy-timeliness tradeoffs. The difficulty of determining the utility function $U ( T .$ E) and paths $g ( T )$ with reasonable precision indicates that insights of a qualitative nature and approximate quantitative information may be all that can be expected in practice.

Nevertheless, the approach described below can lead to a near optimal course of action. To accomplish this, those charged with optimizing the accuracv-timeliness tradeoff in a cost effective manner would identify that environment from the class considered below that most closely corresponds to their own. For each of the environments considered, 27 strategies for handling the accuracv-timeliness tradeoff are analyzed. For each strategy, the time $T _ { 0 }$ is identified at which time the maximum utility $\smash { \dot { \mathcal { U } } _ { \mathrm { m a x } } ( s ) }$ is achieved. For each strategy, ${ \mathcal { L } } _ { \mathrm { m a x } } ^ { \prime } ( s ) - { \mathcal { L } } _ { \mathrm { m a x } } ^ { \prime } ( { \boldsymbol { c } } ^ { \prime } )$ gives the increase in utility. The cost of each of the options has to be estimated. The cost of strategy s is then subtracted from the ${ \cal { L } } _ { \mathrm { \tiny { m a x } } } ^ { \prime } ( s ) \sim - { \cal { L } } _ { \mathrm { \tiny { m a x } } } ^ { \prime } ( c ^ { \prime } )$ values. The largest of the resulting quantities would be correspond to the best of the options analvzed and should be implemented provided that quantity is positive (see Figure 1).

![](/api/attachments/XFUFJ7GT/fulltext/images/88457371e1bae9a535a16384e384b00380928e81c768bfdfcc01a27bc79533a0.jpg)  
Informaton Systems Research 6 · 1

The framework involves determining optimal strategies for subsets of the family of utility surfaces $U ( T , E )$ and paths Γ given below. To facilitate analysıs, the environments are normalized by scaling $T _ { c }$ , the point in time at which the information becomes error free, to 1. Thus the domain for $( T ,  { l i } )$ becomes $t ( \ l ) , \ \{ \ r \} \times \ ( \ l )$ . 1). We consider only moderate and substantial reductions in the initial erroi and $T _ { \epsilon }$ . These are defined to be reductions of one-third and two-thirds respeetively. Thus the starting point possibilities for the I are (0, 0.333), (0, 0 667), and (0, 1.0). Similarly the terminal point possibilities are (0.333, 0), (0.667, 0) and (1.0, 0).

The general form of the utility functions that we examine is given by

$$
U (T, E) = 1 - W E ^ {\alpha} - (1 - W) T ^ {\beta}.\tag{1}
$$

Here $W ^ { \prime }$ is a weight (specified by the user) that gives the relative importance of error magnitude and timeliness $\begin{array} { r l } { ( 0 ) \ \leq \ } & { { } \mathcal { W } ^ { \prime } \leq \ 1 \} } \end{array}$ ). The exponents α and $\beta$ are positive and govern the rate of change of the utility surface with respect to the independent variables. Note that $U ( T , E )$ as defined by (1) possesses the characteristics of a utility function associated with the accuracy-timeliness tradeoff. For example, over the appropriate domain $( T \ge 0 , E \ge 0 ) , \ : { \cal { L } } ^ { \prime } ( T , E ; )$ has an absolute maximum at $T = 0 , E = 0 .$ Furthermore the function (1) is monotone decreasing with respect to each of the independent variables. Equally important for the purposes of analysis. bv varying È, α. and $\beta$ it is possible to generate a wide range of utilitv surfaces.

Clearly there are manv utility functions that are not members of familv (1). This family of functions, chosen partly for illustrative purposes, is consistent nevertheless with the literature in terms of its overall structure and characteristics. (See, for example, Ahituv (1980) and Hilton (1979).) Although there are ways of representing arbitrary utilr.y functions (power series, fourier series, ete.). in practice such approaches would add considerable complexity. In any case the ability to specifv the powers α and $\beta$ allows the user to generate functions that are reasonably good approximations to the majority of potential utility surfaces. Furthermore, famıly (1) probably captures whatever information is available regarding the utility and error reduction functions.

Error reductions over time are captured by another generalized function, that given by Equation (2) for general $E$ and $T ( 0 < E ,  1 . ( ) < T ,  1 )$ ,

$$
\Gamma_ {s} ^ {\prime}: \quad g _ {s} (T) = E _ {s} - (E _ {s} / T _ {s} ^ {\gamma}) T ^ {\gamma}.\tag{2}
$$

The exponent $\gamma$ is positive and determines the rate of change in error over time. The expression (2) has several desirable features. Firstly. $g , ( 0 ) = l ; ,$ , so we can control the

## FiGURF 1 Overvtew of Methodology

initial error level by specifying $E _ { s }$ . Secondly, $g _ { s } ( T )$ is monotone decreasing on $0 \leq T$ $\leq T _ { s }$ , which captures the fact that the error level would decrease with time. Thirdly, $g _ { \mathrm { s } } ( T _ { s } ) = 0$ , so it is possible to specify the time at which the error becomes negligible. The exponent γ allows us to vary the convexity of the path from $( 0 , E _ { s } )$ to $( T _ { s } , 0 )$ with $\gamma = 1$ representing a straight line in $( T , E )$ space.

To gain insight we explore a number of different utility surfaces and error reduction paths. Although it may be difficult for the decision maker to specify the utility function, he or she should be able to make one of the following qualitative evaluations: for a fixed level of error, as T increases the magnitude of the utility (i) decreases slowly at first, more rapidly later; (ii) decreases rapidlv at first, more slowly later or (iii) decreases steadily over time. These cases can be captured by using for β the values 2, 0.5, and 1, respectively. Analogous evaluations can be made regarding varying error magnitudes when time is held fixed; again the values 2, 0.5, and 1 are used for $\alpha .$ (For example, the value $\alpha = 2$ corresponds to the case for which the utility rises sharply for initial error reduction, less rapidly for additional reduction.) The decision maker, by choosing (i), (ii) or (iii) for time and an analogous choice for error magnitude in essence specifies the exponents for a member of the set of equations represented by (1). To complete the parameter specification for $U ( T , E )$ , we let W be one of the values 0.333, 0.5, or 0.667, corresponding respectively to these cases: error magnitude less important than timeliness, equally important, and more important. This approach can generate only a subset of all possible utility surfaces. However, in practice the decision maker would not be able to determine the utility function with any precision. This framework does capture the information the decision maker is most likely to possess regarding the utility surface. Two of the potential utility surfaces are displayed in Figures 2 and 3.

It remains to select a subset of Γ, from the set of functions specified by Equation (2). The options we analyze are $\gamma = 2 .$ , 1, and 0.5. These correspond respectively to the following cases: (a) slow reduction in error initially, more rapid reduction later; (b) steady reduction in error over time; (c) rapid reduction initially, slow reduction later.

The experimental design is summarized in Table 2, and the environments and strategies are described in the next section.

## 4. Analysis of Potential Strategies for Reduction of Accuracy-timeliness Tradeoff for Generic Environments

We now systematically examine the various environments (defined by the specification of the appropriate utility function) and strategies as described in §3. Our goals in doing this are: (1) for a given environment to describe a process for determining the potential for improving the timeliness-accuracy tradeoff; (2) to provide insight regarding behavior of the timeliness-accuracy tradeoff in certain environments that would preclude the need for further analysis.

Altogether we consider 27 environments, each of which is described by a specified utility function (3 values for α crossed with 3 values for β crossed with 3 values for relative weight È'). The squares in Figure 4 represent 9 of those environments where W'is fixed at 0.667. For each environment, we analyze 27 strategies (3 choices for rate of error reduction, i.e., values for γ, crossed with 9 possible $( T _ { s } , E _ { s } )$ pairs). The nine entries in each square in Figure 4 are optimal utility values. $U _ { \mathrm { m a x } }$ , for strategies defined by $( T _ { s } , E _ { s } )$ pairs with $\gamma = 1 . 0$ . The points $( T _ { 0 } , E _ { 0 } )$ at which the optimal values are achieved are suppressed to avoid information overload in this table. They are shown for selected cases in Figure 5. In total 729 environment/strategy combinations were explored. Figure 4 presents 81 of these optimal utility values which for fixed $\alpha ,$ $\beta ,$ W', and $\gamma$ were achieved by following I', from $( 0 , E _ { s } )$ to $( T , \allowbreak , 0 )$

![](/api/attachments/XFUFJ7GT/fulltext/images/85be905728697d4c30f97e6ae778cda310869e062515dc9aae2bd4f0f4497826.jpg)  
FiGuRE 2. α = 2.0, β = 2.0 Sketch of Potental Utihty Surface.

Obtaining the values $U _ { \mathbf { m a x } }$ and pairs $( T _ { 0 } , E _ { 0 } )$ is a straightforward process. Once $\alpha ,$ β and 'have been specified, the expression for U(T, E) involves known exponents and coefficients (see Equation (1)). Identification of a strategy $( \gamma , E , \lambda )$ results in the known functional relationship $E = g _ { s } ( T )$ (see Equation (2)). Replacing E with $g _ { s } ( T )$ in the expression $U ( T , E )$ results in a function of $T$ only, say u( $T ) , 0 \leq T \leq 1$ . Finding the maximum is simply a matter of locating the interior max (if any) and comparing that value with u(0) and $u ( 1 )$ ). The interior maximum is obtained via a numerical procedure based on Newton's Method (Henrici 1964) applied for multiple initial values. The program that generated the values for $\dot { U } _ { \mathbf { m } , \mathrm { i } }$ and $( T _ { 0 } , E _ { 0 } )$ was written in BASIC and was run on an IBM 3081.

Figure 4 is representative of the output produced by the program. (Recall that 1.0 is the maximum possible utility in every case achieved when $T = 0$ and $E \ = \ 0 . )$ The optimal utility values for each square appear in the ovals. One of the striking features of the data shown in Figure 4 is that for almost half the rows the $U _ { \mathbf { m a x } }$ value is independent of the $E _ { s }$ value. In most cases this is because $\chi _ { \mathrm { { \ m a x } } }$ is achieved at $( T _ { s } , 0 )$ regardless of the starting point for $\Gamma _ { s }$ . In such cases the value highlighted as the optimal by the solid oval is the one associated with $E _ { \mathrm { s } } = 1 . 0$ . This is because some cost would be incurred reducing the initial error from 1.0 (the current value) to either 0.667 or 0.333. We refer to this case as economic dominance.

Figure 5 examines in greater detail two of the environments found in Figure 4. The $( T _ { 0 } , E _ { 0 } )$ points have been added, and the net utility gains achievable by moving to adjacent $( T _ { s } , E _ { s } )$ states are displayed on the right. In practice one might well wish to improve the accuracv-timeliness tradeoff by proceeding incrementally. For example. in Figure 5(a) a two-step strategy would consist of moving first from the current state $( T _ { 1 } = 1 , E _ { 1 } = 1 )$ to (0.667, 1) and then to (0.333, 1). Each step is determined by moving to that state resulting in the largest local net utility gain. This approach can, however, result in “misdirects" if one does not have global, as well as local, information. For example in Figure 5(b) an optimal two-stage strategy with global informa-

![](/api/attachments/XFUFJ7GT/fulltext/images/64ad46f765546b88ea6b4a4ebb1bd0067743b0635d5f30472b3e6a636d800e07.jpg)  
FIGURE 3 ${ \mathfrak { c } } = 0 \ 5 , { \mathfrak { \beta } } \ = \ 2 . { \mathfrak { ( ) } }$ Sketch of Potential Utilty Surface

TABLE 2  
Summary of Experimental Design

<table><tr><td>Environmental Parameter</td><td>Symbol</td><td>Values</td></tr><tr><td>Shape of Accuracy Component of Utility</td><td> $\alpha$ </td><td>2.0, 10.05</td></tr><tr><td>Shape of Timeliness Component of Utility</td><td> $\beta$ </td><td>20, 1.0, 05</td></tr><tr><td>Relative Importance of Accuracy and Timeliness</td><td> $\mu$ </td><td>0333, 0.500, 0.667</td></tr><tr><td>Rapidity of Error Reduction Over Time</td><td> $\gamma$ </td><td>20, 1.0, 0.5</td></tr><tr><td>Initial Error</td><td> $E_{s}$ </td><td>0.333, 0.667, 1000</td></tr><tr><td>Time at which Zero Error is Achieved</td><td> $T_{s}$ </td><td>0.333, 0.667, 1000</td></tr></table>

Note For $\alpha , \beta ,$ and $\gamma \colon$ Value of 2.0 yields slow reduction at first, more rapid thereafter. Value of 1.0 yıelds lınear reduction. Value of 0 5 yıelds rapid reduction at first, more slowly thereafter. For I: Vatuc of 0.333 implies accuracy is half as important as timeliness. Value of 0.500 imples equal ımportance. Value of 0.667 imphes accuracy is twice as important as timehness For $E _ { \nu }$ and $T _ { s } .$ Value of 0 333 implies substantial reduction. Value of 0.667 implies moderate reduction. Value of 1.000 is inıtial value.

Designing Information Systems

FiGURE 4. Values for Utility Function and Strategies by Whıch Iheų Are Achieved W hen Error Is More Important (′ = 0.667) and γ = 1 0.

tion is $( 1 . \ 1 )  ( 1 . \ 0 . 6 6 7 )  ( 1 . \ 0 . 3 3 3 )$ yielding $U _ { \mathrm { m a x } } = 0 . 9 2 6$ . Based solely on local information the optimal two-stage strategy would be (1. $1 )  ( 0 . 6 6 7 , \ 1 )  ( 0 . 3 3 3 , \ 1 )$ which results in $U _ { \mathrm { m a x } } ~ \mathrm { ~ \ r ~ { ~ \ r ~ { ~ m ~ } ~ } ~ } ^ { - }$ , significantly less than the 0.926 value. Incidentally, although $U = 0 . 9 2 6$ is not the optimal value for the table, it is very likely that reducing T from 1 1o 0.333 to increase U' from 0.926 to 0.931 is not cost-effective. The issue implicit in this statement will be discussed at greater length below.

The impact of the accuracy-timeliness tradeoff can be reduced in both the short term and long term but by employing rather different approaches. In the short term one should analyze the environment to determine that point in time at which $U _ { \mathrm { m a x } } ( c )$

![](/api/attachments/XFUFJ7GT/fulltext/images/5704161f45fc46132debea20b9613f150cb5cea1116642e1c59abbdb20a2d5ca.jpg)  
FiGuRE 5 Values for Utility Function and Net Utility Gains and Strategies by Whıch They Are Achieved When Error Is More Important (È' – 0.667) for Selected Values of α and $\beta \left( \gamma = 1 . 0 \right)$

is achieved. Doing this would not involve making any changes to the existing information system. Rather the aim is to ensure that the maximum achievable utility which is possible under the current information system is indeed used. One can think of doing this as fine-tuning the existing system. On the other hand it may well be that a strategy to change the data gathering and/or processing procedures is cost-effective There are two broad categories for such strategies. One is a pure strategy that focuses on reducing the current initial error $E _ { c }$ , or the current final time $T _ { c }$ but not both. The second category is a mixed strategy that would involve reducing both.

It is appropriate at this point to clarify the distinction between a pure strategy and the boundary point solution, i.e., (0, 1) or (1, 0). The boundary point solution is in the context of a fixed information system and is indicative of the information being utilized at either the beginning or end of the relevant time frame. The term “pure strategy" is used in the context of redesigning the information system by varying either the timeliness or accuracy dimension but not both

![](/api/attachments/XFUFJ7GT/fulltext/images/fd59c98f497b693b668018d49723f65958bdd617b8e4ac8ad9a90b1606129430.jpg)  
FiGURE 6. Optimal $( T _ { 0 } , E _ { 0 } )$ Values for Three Strategies with γ = 1.0 and Fixed Environment $w = 0 . 6 6 7 .$ ${ \alpha = 2 . 0 , \beta = 1 . 0 }$

These various scenarios are displayed in Figure 6 for the environment $( \alpha = 2 . 0 , \beta$ $= 1 . 0 , \ : W ^ { \prime } = 0 . 6 6 7 )$ . To simplify the discussion we consider only $\gamma = \mathrm { ~ \mathfrak ~ { ~ \mathfrak ~ { ~ \mathfrak ~ { ~ \normalfont ~ { ~ \pi ~ } ~ } } ~ } ~ }$ , which yields strategy paths that are straight lines. The optimal course of action for the current situation is to use the value for V’ available at time $T ^ { \ast } = ( ) . 7 5 0$ , which would leave an error of $E = 0 . 2 5 0$ , and would yield $U _ { \mathrm { m a x } } ( \mathfrak { c } ) = 0 . 7 0 8$ . The line in Figure 6 connecting $E _ { c } = 1 . 0$ to $T _ { c } = 1 . 0$ 0 captures this case. If a decision is made to involve a pure strategy for change, then from Figure 5(b) we see that the optimal strategy is to reduce $E _ { c }$ to 0.333 (and leave $T _ { c }$ at 1.0). In this case $U _ { \mathrm { m a x } } = 0 . 9 2 6$ achieved at $T _ { 0 } = 0$ with, of course, $F _ { 0 } = 0 . 3 3 3$ . In essence this strategy states that procedures should be implemented to reduce the initial error substantially (to $E _ { s } = 0 . 3 3 3 )$ and that the value for V’ used in support of the decision should be the one available at $T = 0$ . This case is captured schematically in Figure 6 by the line connecting $E _ { \varsigma } = 0 . 3 3 3$ and $T _ { c } = 1 . 0 . 1 \mathrm { f } \mathbf { a }$ mixed strategy is emploved, the results shown in Figure 5(b) indicate that $E _ { c }$ should be reduced to $E _ { c } = 0 . 3 3 3$ and that $T _ { c }$ should also be reduced to 0.333. In this event the maxımum utility is achieved at $T _ { 0 } = 0 . 0 8 3$ with a corresponding $E _ { 0 } = 0 . 2 5 0$ , at which time $U _ { \mathrm { m a x } } ~ = ~ 0 . 9 3 \vert$ . The line in Figure 6 connecting $E _ { \mathrm { s } } = 0 . 3 3 3$ and $T _ { s } = 0 . 3 3 3$ represents this strategy.

![](/api/attachments/XFUFJ7GT/fulltext/images/5eb867a9d355f8acf7916775fc9630b887d449f1c7f4a6f9ebd334c436c5e8c1.jpg)  
FiGURE 7 Comparison of Three Strategies for Fixed $T _ { \mathrm { ~ \scriptsize ~ { ~ \scriptsize ~ 1 ~ } ~ } } = \mathrm { ~ 0 ~ } 6 6 7 , \gamma = \mathrm { ~ 1 ~ } 0 , \alpha = \mathrm { ~ 2 ~ } 0 , \beta = \mathrm { ~ 1 ~ . 0 ~ }$

It should be reiterated that our analysis assumes that the decision maker is free to vary Tin such a manner as to maximize utility. If, however, Tis externally specified (e.g., the meeting must be held at the end of the month) the analysis is substantially simplified. Such a situation is presented in Figure 7 for the three strategies we have analyzed above. If, for example, it is specified that $T = 0 . 2 0 0$ , the problem is reduced to one of trading off utility gains vs. system reengineering cost for the indicated points rather than to first optimize each system with respect to time.

It would seem that to analyze the current situation one would have to determine γ, Somewhat surprisingly $U _ { \mathrm { m a x } } ( c )$ can be determined in many cases without knowing γ.

TABI E 3  
Impact of γ on Achievabłe Uuluy Gain for ( uuent Suuatton when $\alpha \right. \alpha \left. ( \ell ) / ( \ell ) / \beta = ?$

<table><tr><td>Achievable Utility Gain</td><td colspan="2"> $\gamma - 0.5$ f</td><td colspan="2"> $\gamma = 1.0$ f</td><td colspan="2"> $\gamma - 2.0$ f</td><td>Σf</td><td>%</td></tr><tr><td>0</td><td>2</td><td> $13.3^{c_{t}}$ </td><td>4</td><td> $26.7^{c_{t}}$ </td><td>12</td><td> $80.0^{c_{t}}$ </td><td>18</td><td> $40.0^{c_{t}}$ </td></tr><tr><td>&gt;0 0 but &lt;0.05</td><td>1</td><td rowspan="2"> $20.0^{c_{t}}$ </td><td>6</td><td rowspan="2"> $40.0^{c_{t}}$ </td><td>2</td><td rowspan="2"> $13.3^{c_{t}}$ </td><td>9</td><td rowspan="2"> $24.4\%$ </td></tr><tr><td>&gt;0 05 but &lt;0.10</td><td>2</td><td>0</td><td>0</td><td>2</td></tr><tr><td>&gt;0.10 but &lt;0.15</td><td>5</td><td rowspan="6"> $66.7^{c_{t}}$ </td><td>4</td><td rowspan="6"> $33.3^{c_{t}}$ </td><td>1</td><td rowspan="6"> $6.7^{c_{t}}$ </td><td>10</td><td rowspan="6"> $35.6^{c_{t}}$ </td></tr><tr><td>&gt;0.15 but &lt;0 20</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td>&gt;0.20 but &lt;0 25</td><td>2</td><td>0</td><td>0</td><td>2</td></tr><tr><td>&gt;0 25 but &lt;0.30</td><td>1</td><td>1</td><td>0</td><td>2</td></tr><tr><td>&gt;0.30 but &lt;0 35</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>&gt;0 35 but &lt;0 40</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td></td><td colspan="2">15</td><td colspan="2">15</td><td colspan="2">15</td><td>45</td><td> $100\%$ </td></tr></table>

This is because for certain environments $\ell _ { \mathrm { m a x } } ^ { \prime } ( c )$ occurs at one of the boundary points, i.e.. (0, 1) or (1, 0). To explore this phenomenon systematically, we define the achievable utility gain for the current situation to be the difference between ${ \dot { L } } _ { \mathrm { m a x } } ( c )$ and the best boundary point solution, i.e., the values for U' at (0, 1) and (1, 0). The utility value for this best boundary point solution will always be $L ^ { \prime } ( 0 , 1 ) = 0 . 6 6 7$ when time is most important. $L ^ { \prime } ( 1 , 0 ) = 0 . 6 6 7$ when error is most important, and U(0, 1) $= U ( { \{ \ : \} } , 0 ) = 0 . 5 0 0$ when they are equally important. (See Equation (1).)

For the cases where the utility shape parameters α and β satisfy ${ \mathfrak { c } } \mathfrak { t } , \ { \mathfrak { \beta } } \leq \mathsf { l } . 0 .$ , the boundary point solution was also the optimal one in 94.4% of the cases (34 of 36). Thus, whenever $\alpha , \beta \le 1 . 0$ holds, it is almost always true that determining the relative importance of timeliness and accuracy also determines the time at which the optimal utilitv is achieved.

As shown in Table 3, however, a very different situation exists when either or both of the exponents are equal to 2. Now in 60% of the cases an optimal solution can be achieved which exceeds the boundary point solution. In over one-third of the cases the achievable utility gain exceeds 0.10. Table 3 also highlights the fact that the achievable utility gain is highly dependent on γ, which determines the rate of change in error over time, with the largest gains attainable when $\gamma ~ = ~ 0 . 5$ . It should be emphasized that these gains are achieved solely by optimizing the current situation without recourse to changing any of the underlying processes.

If optimizing the accuracy-timeliness tradeoff for the current situatton is not sufficient, then data gathering and processing procedures should be changed to increase the value for $\dot { U } _ { \mathrm { m a x } }$ . For each of the squares displayed in Figure 4, the maximum utility value is achieved at $T _ { \surd \nu } = 0 . 3 3 3 , E _ { \surd \nu } = 0 . 3 3 3$ . (There are many ties.) In most cases. however, the utility gain achievable at (0.333, 0.333) is not much. if at all, greater than for the case in which either $T _ { c }$ is not changed ((1.000, 0.3331), or $E _ { c }$ is not changed ((0.333, 1.000)). In the first case the initial error is reduced to one third of its original value but the process after that is not changed. In the second case the initial error is not reduced but processing procedures are changed to reduce the total time to obtain error free estimates to one third of its original value.

Usually reducing only $E _ { c }$ or $T _ { c }$ is simpler than reducing both. If the increase in utility with a pure strategy is nearly as good as what is possible with a mixed strategy, then it probably would not be worth the extra cost of reducing the second dimension. We now explore this issue.

TABLE 4

<table><tr><td colspan="3">TABLE 4</td></tr><tr><td colspan="3">Advantage of Mixed Strategy ( $T_0 = 0\ 333$ ,  $E_0 = 0\ 333$ )Over the Better Pure Strategy ( $T_0 = 0\ 333$ , $E_0 = 1\ 000$ ) or ( $T_0 = 1\ 000$ ,  $E_0 = 0\ 333$ )</td></tr><tr><td>Increase in Utility</td><td>Frequency</td><td>%</td></tr><tr><td>0</td><td>65</td><td>80.2%</td></tr><tr><td>0.001 but &lt;0.010</td><td>8</td><td>9.9</td></tr><tr><td>0.010 but &lt;0.020</td><td>6</td><td>7.4</td></tr><tr><td>0.020 but &lt;0.030</td><td>2</td><td>2.5</td></tr><tr><td>≥0.030</td><td>0</td><td>0.0</td></tr><tr><td></td><td>81</td><td>100%</td></tr></table>

In the case of economic dominance (the left-hand utility value in a row in one of the squares in Figure 4 equals the right-hand utility value in that row; a similar statement holds for columns) the appropriate pure strategy is obviously preferable The same conclusion, however, may hold even when there is not economic dominance. For example, in the middle square, bottom row of Figure 4, the best pure strategy $( T _ { s } = 1 , E _ { s } = 0 . 3 3 3 )$ yields a utility value of 0.926, only 0.005 units less than the utility value for $T _ { s } = 0 . 3 3 3 , E _ { s } = 0 . 3 3 3$ , the optimal $( T _ { s } , E _ { \mathfrak { s } } )$ pair. It is unlikely that the cost of moving from $( T _ { \mathnormal { r } } = 1 , E _ { s } = 0 . 3 3 3 )$ to $( T _ { s } = 0 . 3 3 3 , E _ { \mathfrak { s } } = 0 . 3 3 3 )$ ) is less than 0.005. Thus in this case the decision maker should concentrate on reducing the initial error as much as possible and not spend resources to speed up the process. (The resulting situation should still be optimized, of course, to determine $( T _ { 0 } , E _ { 0 } ) .$ 1

Table 4 provides information on the prevalence of this phenomenon. As shown there, for 65 of the 81 cases examined (27 environments crossed with three possibilities for $g ( T ) )$ , nothing is gained in moving from a pure to a mixed strategy. Furthermore, in another eight cases the achievable utility gain is positive but less than 0.010. From this we can conclude that with a few possible exceptions a pure strategy is either optimal or very satisfactory. Thus in most cases there is no imperative for reducing both $T _ { c }$ and $E _ { c }$

It is not obvious whether one should concentrate on reducing $T _ { c }$ or reducing $E _ { c }$ Clearly that decision is dependent upon the particular environment (values for $\alpha , \beta ,$ and $W )$ and the relative costs. However, in those cases for which timeliness and error are not equally important, it turns out that knowing only which one is more important determines the optimal strategy in approximately two-thirds of the cases, provided the costs of reducing $T _ { c }$ and $E _ { c }$ are roughly comparable. Table 5 contains the relevant information.

A rather surprising insight can be gleaned from Table 5: When error is more important than time, then in most situations reducing the value of $T _ { \mathrm { c } }$ achieves the greatest value for the utility function. When time is the more important factor, then in most situations reducing the value of $E _ { \mathrm { c } }$ vields the greatest utility value

Upon reflection the logic of this result becomes apparent. When error is more important, the optimal solution will usually call for a small error which can be achieved by waiting till near the end of the time period. By reducing $T _ { c }$ , we can reach this low error situation more quickly with greater resulting utility. A similar argument can be made for the case where time is more important. Of the cases where this relationship does not hold, most relate to widely different values for α and $\beta ,$ e.g., α $= 2 , \beta = 0 . 5$ when error is more important and $\alpha = 0 . 5 , \beta = 2$ when time is more important.

TABLE 5  
Strategies Which Achieve the Greatest Value for the Utlity Function

<table><tr><td colspan="3">(a) Error more important ( $W' = 0.667$ )</td></tr><tr><td>Strategy</td><td>f</td><td>%</td></tr><tr><td> $T_s = 1.000, E_s = 0.333$ </td><td>4</td><td>14.8%</td></tr><tr><td> $T_s = 0.333, E_s = 1.000$ </td><td>18</td><td>66.7%</td></tr><tr><td> $T_s = 0.333, E_s = 0.333$ </td><td>5</td><td>18.5%</td></tr><tr><td></td><td>27</td><td>100%</td></tr><tr><td colspan="3">(b) Time more important ( $W' = 0.333$ )</td></tr><tr><td>Strategy</td><td>f</td><td>%</td></tr><tr><td> $T_s = 1.000, E_s = 0.333$ </td><td>17</td><td>63.0%</td></tr><tr><td> $T_s = 0.333, E_s = 1.000$ </td><td>4</td><td>14.8%</td></tr><tr><td> $T_s = 0.333, E_s = 0.333$ </td><td>6</td><td>22.2%</td></tr><tr><td></td><td>27</td><td>100%</td></tr></table>

Various examples illustrate the above insight. Many accounting applications provide instances of situations where error minimization is the major focus. Here the principal contribution of information system technology is to reduce the time required to achieve this target. On the other hand, decision support systems for crisis management require quick response. Here the major contribution of information technology is to provide more accurate information within the time frame mandated by the decision environment.

## 5. Concluding Remarks

This paper has examined the tradeoff between the accuracy and timeliness of data in the context of periodic decision making and review. From the decision maker's perspective this tradeoff may well be unavoidable. That does not mean, however, that one should not attempt to lessen the impact of that tradeoff. At a minimum decision makers should schedule periodic meetings at an optimal time, that is, wait until that time $T _ { 0 }$ at which the utility U(T, E) of the information is largest. In addition it may well be appropriate to initiate changes to the information systems to reduce the initial error and/or shorten the time before the information becomes error free.

The theoretical framework is designed to facilitate analysis of the accuracy-timeliness tradeoff with the goal of determining appropriate changes to the supporting information systems. As one would expect, the accuracy-timeliness utility function U(T, E') figures prominently in the analysis. Realistically, however, it would be next to impossible to determine U(T, E) precisely for all values of T and E. Thus decision makers would have to work with some approximation to $t ( T , E )$ . In $\ S 3$ one approach to identifying a suitable approximation was presented. The essence is that one utility function from a family of generalized utility functions is identified by asking the decision maker to supply information regarding the relative importance of the timelı- ness and accuracy dimensions and to give qualitative descriptions of the rate of change of utility of information with respect to time and error level. This type of information decision makers should be able to supply, and it may well be that it is all the information they can comfortably furnish.

In §4 we showed that knowledge of the environment (values for α, β, and $W )$ is sufficient in many cases to provide guidance on how best to optimize the accuracytimeliness tradeoff. For certain subsets of the family of utility functions considered it is shown that the likelihood is high that an early (or in other cases a late) decision is appropriate. Also it is seen that in about two-thirds of the cases for which either accuracy or timeliness is more important, knowing which one is more important is sufficient to know whether a higher priority should be given to reducing $T _ { c }$ or the initial error. Thus even if the utility function cannot be known precisely, the framework presented nevertheless provides considerable guidance concerning the types of changes that should be made to the supporting information systems.

The analysis described in §4 provides information on the strategy that would yield the largest possible utility. In some cases a reduction in the initial error of either moderate or substantial magnitude would be required. In other cases reduction of the $\vec { \pmb { \mathscr { i } } } _ { c }$ value would be appropriate. In still other situations reductions in both $E _ { c }$ and $T _ { c }$ are called for. Also, information is provided on the appropriate rate of improvement of accuracy with time.

Information such as the above would guide a system designer in how best to redesign an existing system. An information system can be improved in various ways; among these are the upgrading of technology, adding new resources and/or the redistribution of existing resources. For example, in one situation installing a real time system to collect and process key data may be suggested, while in another case, simply adding personnel to eliminate a data input bottleneck may be sufficient.

## Generality of Methodology

This work analyzes in some detail the tradeoff involving two of the dimensions of data quality. namely timeliness and accuracy. For the methodology to be applied to other situations, certain conditions must hold. Firstly one or more of the data quality dimensions must clearly trade off against the other dimensions. Secondly, given values or levels for each of the dimensions analyzed, there should be an associated utility for all points in some region. Thirdly, two or more strategies for dealing with the tradeoff need to be proposed. If two data quality dimensions are involved, then each strategy can be represented by a curve in the plane which captures the improvement in accuracy with time. If three data quality dimensions are to be analyzed simultaneously, then each potential strategy would be modeled by a surface in three space.

In addition to providing general guidelines for the development of both short and long term strategies for improving the accuracy-timeliness tradeoff, the foregoing analysis has also provided a map of an important subset of the decision space confronting system designers. It is likely that, in a number of cases, the results cited in this paper can be used to provide upper and lower bounds to situations which vary within the rather broad range of parameters utilized in this study. Where this cannot be done, the various system options can be evaluated by a custom-tailored version of the described rnodel. In any case, we have seen that for the accuracy-timeliness tradeoff. intuition often may be a poor guide.

Acknowledgment. The authors wish to express their appreciation to the Associate Editor and an anonymous reviewer for their substantial contributions to the refining of the material in this article. We also wish to thank Jeffrey A. Tyler who developed Figures 2 and 3 using the graphics package AXUM by Trimex.

\* Edward A. Stohr, Associate Editor. Γhıs paper was received on July 22. 1992, and has been with the authors 4 months for 3 revisions

## References

Ahituv, N , “A Systematic Approach Ioward Assessing the Value of an Information Systems," AfIS Quatter/r, 4 (1980), 61–75

Alonso, W., “Predicting Best with Impertect Data," Journal of 1meran Insttute of Planner s. 35 (1968), 248-255

Ballou, D. P and H 1.. Pazer, "Modeling Data and Process Qualty in Multi-Input, Multı-Output Information Systems." Management Sctence 31, 2 (1985), 150–162

and , “A Framework for the Analysis of Erroı in ( onjunetıve, Mult-criteria Satisficing Decision Processes," Dectston Sctences. 21, 4 (1990), 752–770

S Belardo, and B Kleın, “Implications of Data Qualıty for Spreadsheet Analysıs." Data Bas(, 18, 3 (1987), 13–19

- and G. K Tayı, "Methodology for Allocatıng Resources for Data Qualıty Enhancement," Commuatons ot the, 1CM. 32, 3 (1989), 320–329

Boockholdt. J. L.. “Implementıng Security and Integrity in Micro-Mainframe Networks," A1IS Quarterhr 13, 2 (1989), 135–144

Brodie, M. I... "Data Qualıty in Infotmation Systems," Information an/ Management, 3 1980), 245–258

Crutsinger, M.. “Economıc Data Errors Skew Outlook, Policy  Associated Press (Schenectady Gazette) Septembei 5. 1989

Cushing, B F . “A Mathematical Approach to the Analysıs and Design of Internal Control Systems," Accountung Revien, 49 1 (1974) 24–41

Date, C J., L1 Introdutton to Data Base S1 stems (5th Ed.), Addison Weslev, Reading. MA. 1990

Davıs, G. and M. Otson, Management Informaton Svstems Conceptual Foundatons, Structure and Development (2nd Ed ). McGra»-Hill, New York 198

DeLone, W and E MeL ean, "Infoımation Systems Success. The Quest for the Dependent Variable," Intormaton Systems Research. 3, 1 (1992), 60–95

Goodhue, D L., J. A. Quıllard, and J F. Rockart, “Managing the Data Resouree A Contngency Perspective." M11S Quarter/v, 12. 3 (1988). 373–392

Hamlen, S S., "A Chance Constrained Mixed Integer Programming Model for Internal Control Design," 4ccounting Review, 55, 4 (1980), 578–593

Henrict, P , Elements of Numerical Inalvsts, John Wiley New Y ork, 1964

Hilton, R. W , “"The Determinants of Cost Information Value An Illustrative Analysis " Joıønal of 1ccountng Research. 17, 2 (1979), 411–435

, "The Determinants of Intormation Value. Synthesizing Some General Results." Management Sctence, 27, 1 (1981), 57–64

Iuri, Y and H Itamı, "Quadratic Cost-Volume Relationship and Tuming of Demand Information," The 1ccounttng Revtew, 48 (1973), 724–737

Johnson, J. R , R. A. Leitch and J. Neter, "Characteristies of Errors in Accounts Receivables and Inventory Audits," 1ccountng Revzeu, 56, 2 (1981), 270–293

Laudon, K. C., “Data Qualıty and Due Process in Large Interorganızational Record Systems." Communı- cations of the ACM, 29, 1 (1986), 4–18

Mahmoud, E. and G. Rice, “Database Accuracy: Results from a Survey of Database Vendors," Informaton and Management, 15 (1988) 243–250.

Marschak, J. and R. Radner, Économıc Theory of Teams, Yale Unıversity Press, New Haven, CT, 1972.

Martin, J. Securitv. Accuraey and Privacv in Computer Systems, Prentice-Hall. Englewood Chiffs, NJ, 1973.

Morey, R. C., “Estimating and Improving the Quality of Information in a MIS," Communicatons of the .4CM, 25, 5 (1982), 337–342.

Nesbit, I. S., “On Thin Ice: Micros and Data Integrıty," Datamation, 31, 21 (Nov. 1985), 80–85

Perry, W., Effecttve Methods of EDP Qualtty Assurance, Prentice-Hall, Englewood Cliffs, NJ, 1983.

Ricketts, J A., “Powers-of-Ten Information Biases." MIS Quarter/y, 14, 1 (1990), 63–77.

Stohr. E. A , “Information Systems for Observıng Inventory Levels," Operattons Researoh. 27, 2 (1979), 242-259.
