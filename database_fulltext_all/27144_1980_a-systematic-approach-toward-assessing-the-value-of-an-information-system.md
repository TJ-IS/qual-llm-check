---
otero_id: 27144
otero_key: "6WCR4CYY"
title: "A Systematic Approach Toward Assessing the Value of an Information System*"
authors: "Niv Ahituv"
year: "1980"
journal: "MIS Quarterly"
doi: "10.2307/248961"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A Systematic Approach toward Assessing the Value of an Information System Author(s): Niv Ahituv

Source: MIS Quarterly, Vol. 4, No. 4 (Dec., 1980), pp. 61-75

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/248961

Accessed: 22-10-2015 06:27 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# A Systematic Approach Toward Assessing the Value of an Information System\*

By: Niv Ahituv

## Abstract

A multiattribute utility approach is adopted to assess the value of an information system. Various economic analyses of the value of information are reviewed and the conceptual problems regarding the definition of this value and some measurement difficulties are discussed. A list of possible utility attributes is proposed for a reporting system value assessment, and for each attribute a measure and a utility function is suggested. Some techniques which constitute a joint utility function are presented, accompanied by two examples. A real case of minicomputer selection is given in order to illustrate the structured approach.

Keywords: Information evaluation, system selection, information economics
ACM Categories: 2.44, 2.49

## Introduction

The various approaches toward information system evaluation can be roughly classified into two different categories.

1. Pragmatic assessment such as cost/benefit analysis. A review of this approach was published recently by King and Schrems [25].

2. Theoretical evaluation based on Decision Theory. The general foundations were developed among others by Ackoff [1], Marschak [30], and McGuire and Radner [33]. Some of them have been applied in accounting research (Feltham, [15]; Mock, [36]; Feltham, [16]; Demski, [11]; Butterworth, [8]).

A third approach can be placed in between the above two. This approach attempts to formulate a utility function for certain information problems and then to find the system which gives an optimal solution for the function. Grochow [19] and Dexter [12] proposed such an approach toward timesharing systems evaluation. Grochow's work is a rare case where empirical data as well as a theoretical model were used. Ahituv [2] uses a similar approach to evaluate data entry and validation systems.

This article should be classified in the third category. It will attempt to list possible attributes of the user utility function associated with reporting systems. It will also attempt to assess the nature of the utility gained by the user from each individual attribute, and then to outline how those fragments of the utility function can be combined. The next section discusses conceptual problems with regard to the definition of the value of information. The third section discusses some measurement problems. The fourth section lists possible attributes of user utility gained by using reporting systems. The fifth section outlines some techniques of assessing and optimizing user's utility function, or at least reaching a satisficing $^{1}$ solution. Some concluding remarks are indicated in the last section.

## Conceptual Problems

Any fundamental discussion with regard to the value of information raises at least three major questions.

1. Whose value are we talking about? Is it an individual, a team, an organization, or any group of individuals?

2. What type of value are we talking about? Is it the value perceived by the user; is it the marginal improvement of the user performance revealed after receiving the information; or is it the normative value analytically computed?

3. Who is performing the evaluation and when? Is it the decision maker or user served by the system who evaluates it either continuously or ex-post; or is it an external or objective evaluator who recognizes all the parameters and performs an ex-ante analysis?

With regard to the first question, usually there are no severe theoretical obstacles as long as the utility of an individual is considered (see for example Radner [39]). When an information system should serve a group of individuals, we have to face the “Impossibility Theorem” [4] before allowing any further discussion. According to the theorem, it is not possible to assign a common set of preferences to a group of individuals, unless the assignment is “imposed or dictatorial” [4, p.59]. Usually, the problems evolving from this theorem are overcome by assuming that common preferences can be assigned to the group, as done in Team Theory [31, 40]. Similarly, this article will assume that a common set of preferences exists, e.g., a utility function will be developed for the user of an information system, where the notion “user” does not necessarily imply an individual.

With regard to the second question, three different definitions of the value of information are found in the literature. The following example illustrates them.

Suppose a gambler in a horse race is able to purchase information about the results of a future race prior to its commencement. Suppose the gambler believes that the proposed information is true, complete and private, i.e., it will not be disclosed to the public, and is probably willing to pay for that information. The amount the gambler is willing to pay reflects the subjective evaluation of the worth of the information, namely the perceived value of the information. Suppose later, after the information had been acquired, some income was gained from gambling. The difference between that income and the income that could have been gained without the information is the virtual betterment of the gambler's performance, namely the revealed (realistic) value of the information. By using some simple tools of Probability Theory, we can also compute the expected payoff of what should have been gained if the gambler used the information optimally—assuming the gambler wished to maximize the expected payoff. The difference between this payoff and the expected payoff when the gambler has no prior information is the normative value of the information.

Thus, there are three different values of information; see related discussion in Mock [36]. The perceived value is usually discussed in papers based on empirical research. Gallagher [17], and Munro and Davis [37] measured this value by using a semantic differential scale. A similar approach was taken by King and Rodriguez [27]. Neumann and Segev [38] investigated the perceived value of a banking information system among branch managers. Ronen and Falk [41] measured the “monetary equivalent” of the perceived value by “selling” information to the participants of their experiment; see also Zmud [51].

The revealed value of information has been measured in some experimental research. A series of such experiments were carried out at the University of Minnesota [13]. Hedberg [21] and Edstrom [14] investigated the additional value gained by using an online reporting system in comparison to a batch processing system. Mock [35] compared the revealed value to the normative value and found them to be different. In a way, his results conform with Simon's ideas about decision makers being satisficers rather than optimizers [44].

The normative value is intensively discussed in Information Economics. Feltham [16], Tapiero [50], and Stohr [48] calculated this value for inventory control information systems. Butterworth [8] presented its application to accounting systems.

There is not an ultimate answer to the question of which value should be considered. The perceived value is available only if experiments and interviews are undertaken, and it is useful for economic considerations only if it is expressed in monetary figures, which is not frequently done. The revealed value probably best reflects the realistic impact of the information. However, when information for middle or top level decision making is investigated, it is very difficult to estimate that value. This is because decisions in these levels are unstructured, their implications are likely intangible and range over a long time, and therefore the revealed value of particular information is hard to isolate. Both the perceived and revealed values require some post hoc analysis. The normative value might be easier to handle from an analytic point of view, but it is applicable only in structured or semistructured decision problems $[45]$ . Even then it can serve only as an upper bound for the value of information $[35]$ .

This article adopts an approach based upon the Multiattribute Utility Theory $[24]$ . In a way it is a combination of the above “values.” The determination of the utility attributes and the characterization of the user preferences $[51]$ can be based on the perceived or revealed value. Further analysis can be done by a normative method.

Referring to the third question of the above, the identity of the evaluator has some implications on the approach to the evaluation itself [16]. If the evaluator is an operator within the system (i.e., the decision maker according to Churchman [9]), he or she is not supposed to have a comprehensive knowledge about all the states and the components. The evaluation is performed on a day to day basis, resulting in gradual improvements to the existing system. If the evaluator is external to the system, some sort of a “know-all” system designer [9], the evaluation gets the overall perspective required for designing a new system.

This article takes the point of view of the outsider, the objective designer who wishes to better the utility of the user. Consequently, the approach would be to devise tools for pre-implementation, or ex-ante, rather than post implementation, or ex-post, valuation. However, since we would like to incorporate user's views and expectations into the analysis, we have to obtain some data which are normally available only after implementation. This type of data is obtained through experiments [13, 35], questionnaires [37], and interviews in empirical research related to perceived and realistic values. These methods may be useful for the approach discussed here. With those remarks in mind, we can proceed now to discuss some technical problems.

## Measurement Problems

It is almost generally agreed that the utility gained by using information is not a unidimensional function $[26, 46, 51]$ . McGuire expresses it bluntly by saying that “any search for a one-dimensional measure of ‘informativeness’ is a vain one” $[32, p. 109]$ . Thus, a multiattribute utility function should always be selected for information system evaluation. This approach involves some technical problems.

First, what are the relevant attributes? Terms such as timeliness, accuracy, reliability, etc., tend to play an important role in the evaluation process [23, pp. 82-83]. However, it is not certain that all of them are always relevant. In other words, it is likely that the dimensionality can be reduced by assigning only the relevant attributes to each case investigated. For example, Neumann and Segev [38] found a spill over effect of the content attribute over several other attributes, i.e., the evaluation of content causes evaluations of other characteristics to be similar.

Second, how would each attribute be defined and measured? The answer is relatively simple when timeliness is considered, but it might be nontrivial with regard to some other attributes.

Third, how would the effect of each attribute on the utility function $^{2}$ be assessed? For example, it is relatively easy to declare that users prefer short response times to long ones, but is it a linear or a threshold function?

Finally, what is the joint utility function constituted from all the relevant attributes? In order to formulate the joint utility function one has to assess the tradeoffs among the various attributes, and those are not so easily detected. Moreover, sometimes only an ordinal, or value, function is feasible, and sometimes even achieving that is too ambitious.

The next section develops a list of possible utility attributes. Each attribute will be developed through the following steps:

1. definition of the concept behind the attribute,

2. definition of a possible measure for the attribute, and

3. characterizing the nature of the [marginal] utility function related to that attribute.

Before proceeding it is important to note that this article presents an approach toward information systems evaluation. It does not pretend to propose an ultimate method, nor to provide the readers with an exhaustive list of attributes. It only claims that a similar approach can be adopted in many cases of information evaluation.

## Possible Utility Attributes for a Reporting System

In order to simplify the presentation, we confine ourselves only to a reporting system. We assume that at a given point of time, $t_{0}$ , there exists a database $^{3}$ containing data already validated and updated. The only feasible operations on that database are selective retrieval, manipulation (aggregation, sort, computation, etc.), and displaying. We exclude any reference to the preparation of the data, namely, the capturing, validating, and updating of the data files, i.e., we assume that the user cannot affect the creation of the database.

First, three major categories of attributes are proposed $^{4}$ :

1. timeliness,

2. contents, and

3. format.

The cost attribute is not introduced here; however, it is discussed in the subsequent sections. For each of the three categories, we will try now to determine various attributes.

## Timeliness

One has to differentiate between online and batch processing reporting systems before evaluating the time factor. Online systems are usually designed to provide fast answers to queries. Therefore, in such cases, the response time should be considered. Batch processing systems are usually designed to provide information in a fixed frequency thus, in addition to response time, the frequency should be considered. Two attributes, therefore, emerge.

## Response Time

This is defined as the difference between the time the information is received and the time it was requested (i.e., $t-t_{0}$ ). Assume $t_{0}=0$ and get t as a measure.

Assumption. The utility function is a nonincreasing function of t [43, 49]. The nature of the function might be continuous, or discrete (threshold), etc. $^{5}$

## Frequency

It is important to provide data within the framework of a given frequency in cases of periodical reporting systems. For example, the share prices in the stock exchange are highly valuable as long as the trade continues. The usefulness of the information decreases after the end of the business hours, and then starts to increase again before the beginning of the new business day, and so on.

In periodical systems, the variable remains the same as above (i.e., t), yet the utility function is different.

Assumption. The utility function is a decreasing cyclic function of t (such as $u_{t}(t) = |\sin(a_{1}t)/(t + b_{1})|$ where $a_{1}$ and $b_{1}$ are positive constants).

The last function can be exemplified by taking $a_{1}=\pi/2$ and $b_{1}=1$ . Some typical results are exhibited in Table 1.

Table 1. An Example of a Cyclic Decreasing Function

<table><tr><td>t</td><td> $u_t(t)$ </td></tr><tr><td>0</td><td>0</td></tr><tr><td>1</td><td>0.50</td></tr><tr><td>2</td><td>0</td></tr><tr><td>3</td><td>0.25</td></tr><tr><td>4</td><td>0</td></tr><tr><td>5</td><td>0.20</td></tr></table>

It can be noticed that the figures reflect periodical changes in the utility as well as a decay over time. Of course, this is only an example and in a real case one has to assess and calibrate a representative function.

There may be some other time related attributes. For example, Keen and Scott Morton mention the currency of data as one of them [23, p.84]. However, due to the initial assumption that the user does not affect data generation timeliness attributes are not discussed any further here.

## Contents

The content characteristics of a report are somewhat vague [38]. They may include various aspects such as accuracy, relevance, fineness (aggregation level), or order of magnitude (units, thousands, millions), etc. This article proposes two attributes which are content related—the similarity and aggregation level.

## Similarity

The notion of similarity [2], which will be explained later, is introduced in order to represent the relevance and the accuracy of the reported data. We will introduce it from an abstract point of view and then discuss its applicability.

Let D be a finite set of data actually received by the decision maker. Suppose that after a decision has been made, and the real state of the world is already known, the decision maker can determine what should have been the optimal set of data, ex-post. In other words, the decision maker, restricted to the data available in the database, designates a subset of the database that, if had been displayed, would have led to the best (subjective) decision. Denote this subset by D\*.

Let $m(A)$ be an operator which provides the number of members in a set, and assume that each data item in $D^{*}$ has the same importance with regard to the decision problem.

## Denote.

a. $m_{1} = m(D \cap D^{*})$ , the number of members that are common in D and $D^{*}$ ,

b. $m_{2} = m(D^{*} - D \cap D^{*})$ , the number of members of $D^{*}$ that were not provided to the user, and

c. $m_{3} = m(D - D \cap D^{*})$ , the number of members that were provided but not desired.

A comparison between $m_{i}$ , i=1,2,3, and some common notions of statistics will be presented later. Figure 1 helps to picture $m_{1}$ , $m_{2}$ , and $m_{3}$ .

Now define s as follows $^{6}$ :

Equation (1)

$$
s = m _ {1} / (m _ {1} + m _ {2}) - m _ {3} / (m _ {1} + m _ {3})
$$

Let us examine some properties of s:

a. If $D^{\star} = D$ , i.e., the data provided are exactly the data desired, then $m_2 = m_3 = 0$ hence $s = m_1 / m_1 = 1$ .

b. If $D^* \cap D = 0$ , i.e., the report does not provide any desired datum, then $m_1 = 0$ hence $s = -m_3 / m_3 = -1$ .

c. If $D \subset D^*$ , i.e., the data provided are desired but still there are missing data, then $m_3 = 0$ , hence $s = m_1 / (m_1 + m_2)$ , namely $0 < s < 1$ .

d. If $D \supset D^{*}$ , i.e., the data desired are provided but there are also undesired data, then $m_{2}=0$ , hence $s=1-m_{3}/(m_{1}+m_{3})$ , namely 0>s>1.

Generally speaking, s is minimal, equals -1, when there is no similarity at all between the desired and the provided data. s is maximal, equals 1, when the data are prefect. s increases when the similarity increases. Thus, s is suggested as a theoretical measure of similarity whenever each datum carries the same value for the user. If various subsets of the data are associated with different values for the user, each subset j can be corresponded to its own $s_{j}$ and then a “weighted average” of the $s_{j}$ 's can be computed.

![](/api/attachments/6WCR4CYY/fulltext/images/0efeb2f4a41d32477c4de161344b6cc7a2badff1e487c9d43ba9f14acc5d2131.jpg)  
Figure 1. Components of Similarity

Now the assessment of s should be discussed. Referring to statistical errors of the first and second type, one can interpret the formula for s (1) as follows:

a. “An error of the first type” would be the probability $p_{1}$ that a datum is desired, i.e., should belong to $D^{*}$ , but it has been omitted from the report. $^{7}$

$$
\begin{array}{l} p _ {1} = 1 - m (D \cap D ^ {*}) / m (D ^ {*}) = \\ 1 - m _ {1} / (m _ {1} + m _ {2}) = m _ {2} / (m _ {1} + m _ {2}) \end{array}
$$

b. “An error of the second type” would be the probability $p_{2}$ that a datum is not desired $^{8}$ , i.e., should not belong to D, but it has been provided.

$$
\begin{array}{r l} p _ {2} = & m (D - D \cap D ^ {*}) / m (D) = \\ & m _ {3} / (m _ {1} + m _ {3}) \end{array}
$$

Equation (1) can be presented as $s = 1 - p_{1} - p_{2}$ , namely, a function decreasing when the probabilities of error increase.

These probabilities can be forecasted by using some past data and/or some similar cases. Mace, Crowe, and Jones [29], while discussing data validation systems, suggest that either moving average or exponential smoothing seem appropriate techniques to assess such probabilities. Cushing [10] and Bodnar [7] also discuss some implementation aspects of reliability assessment, i.e., probabilities of errors, with regard to accounting control systems. There is no unique method of assessment, but all these articles regard it as feasible.

Whenever such probabilities are not available or cannot be estimated, a surrogate variable may be considered. For example, one may find it useful to examine the adaptability of the report to the requirements of the user as stated in the initial design of the system. That might help to estimate the relevance factor. The correctness of the data can be estimated by samples $[29]$ . Once the similarity measure, s, is determined, its utility function should be assessed.

Assumption. The utility function is a non decreasing function of s. The use of the similarity measure is exemplified in the fifth section.

## Aggregation Level

The degree to which data should be aggregated is a frequent issue in Accounting, MIS, and Econometrics. Ijiri [22, appendix B] gave a mathematical interpretation for the aggregation process. Lev suggested to adopt the entropy function for aggregation measurement [28]. Generally, it is agreed that some amount of information is lost by its aggregation. Whether this loss has any qualitative significance is still a debatable issue [18, 20, 41].

A decision maker faced with many figures, potentially has a better opportunity to “know” what is going on. On the other hand, the human perception is limited $[34]$ so one might overlook some important facts due to information overload. Sometimes the domain of possible actions or decisions to be taken does not require a full detailed report, namely, aggregated data will lead to the same decisions as more detailed data $[16, p.31]$ .

The usefulness of the entropy function $[28]$ for measuring the value of aggregation was found to be limited only to cases where the user utility function is of a logarithmic nature $[5, 41]$ . Nevertheless, this function can still serve as a measure for the quantity, rather than quality, of aggregation, as will be proposed here.

Let us limit our concern only to numerical non-negative numbers. Assume that a list of data, $D_{0}$ , contains all the raw data that can be displayed to the user. Denote $D_{0} = \{d_{1}, \ldots, d_{n}\}$ and normalize the list by computing

$$
d _ {i} ^ {\prime} = d _ {i} / \sum_ {i = 1} ^ {n} d _ {i}.
$$

The entropy of the raw data would be:

$$
h _ {0} = - \sum_ {i = 1} ^ {n} d _ {i} ^ {\prime} \log d _ {i} ^ {\prime}
$$

Suppose the members of $D_{0}$ are aggregated into a new list, D, whose entropy is h. The absolute loss of entropy, $h_{0}-h$ , does not have a high significance since it is highly dependent upon the number of items in $D_{0}$ and D. A relative measure would serve us better.

Following the same line of thought as with the similarity measure, suppose post hoc, the user can determine the optimal report required for his decision making process. Denote the entropy of this report by $h^{*}$ .

Assumption. A possible utility function for the aggregation attribute has a single peak at $h^{*}$ .

For example:

$$
\begin{array}{l} U _ {h} (h) = - a _ {3} [ (h - h ^ {\star}) / (h _ {0} - h ^ {\star}) ] ^ {2} \\ \text {(assume h_{0} \neq h^{\star} , a_{3} > 0)} \end{array}
$$

(The coefficient $a_{3}$ serves for calibration purposes). Denote $H=(h-h^{*})/(h_{0}-h^{*})$ and note that $0<H\leq1$ whenever the aggregation level is less than desired; H=0 when the aggregation level is optimal; H<0 whenever aggregation is overdone.

The proposed measure ignores the meaning of the figures, the title of the items, which is a common disadvantage of all the attempts to deal with entropy. However, if the aggregation is initially restricted only to “reasonable” aggregations from an accounting point of view, that disadvantage may partly be overcome. $^{9}$

The problem remaining is the assessment of the "optimal entropy," h\*. Actually, it is a problem of an ex-ante assessment of a value which can be investigated ex-post. Ex-ante, it should be estimated by using questionnaires, interviews [24], and experiments [13, 41]. For example, the designer can prepare some alternative pilot reports, each of which varies in aggregation level; users will be requested to opine on each alternative. In fact, if the decisions involved are fairly structured, users' preferences can be experimentally measured [41].

Entropy is not the ultimate measure for data aggregation. Many articles inquire into aggregation problems without the use of entropy (see $[6, 47]$ ). The following example illustrates an aggregation problem in which entropy has not been applied. Although the example is simplistic, we believe that it may clarify the idea of this attribute.

Example. Suppose a top manager supervising several departments is periodically informed by receiving N figures (for example, there are r departments and each has z budgetary items hence N = rz). The manager makes judgments and decisions by scanning the figures and carrying out comparisons between various figures appearing in the output. It is assumed that the importance of each department and each figure is the same.

Let N be sufficiently large to make it quite difficult to analyze all the figures and come to definite conclusions in a reasonable time. The maximum number of possible comparisons between every pair of figures is proportional to $N^{2}$ , $(N(N-1))$ , and it is too large to be handled by the manager. On the other hand, providing the manager with only one figure which is the total of the entire list of N figures is meaningless. Thus, the first characteristic of the manager's utility is determined by the bounded capacity to perceive and analyze data [34, 44].

The manager would like to detect exceptions in the departmental activities. If two figures are aggregated together and there has been at least one exception regarding one of the original figures, it is not certain that the manager will detect the exception because two counter direction exceptions might compensate each other. Even if it is discovered, the manager will not be able to promptly determine its location. Therefore, the second characteristic of the utility is the ability of control.

The above verbal description is formulated in a quantitative manner.

Denote. N - the number of the original raw data,

n – the number of figures in the report provided to the manager, $1 \leq n \leq N$ , and

$$
k = N - n.
$$

This problem can be examined from two points of view—pessimistic and optimistic. The pessimistic view assumes that the loss of information is maximized. For example, if $d_{1}$ , $d_{2}$ , $d_{3}$ , and $d_{4}$ are the original data, then in a report containing two figures they will appear in the form of $(d_{1} + d_{2})$ and $(d_{3} + d_{4})$ , or similarly, so that no original figure is available. The optimistic view assumes that the loss of information is minimal; e.g., a two figure report produced from $d_{1}$ , $d_{2}$ , $d_{3}$ , and $d_{4}$ will exhibit one original figure, say $d_{1}$ and aggregate the rest. Certainly, in reality the manager knows which numbers have been combined and which remained separate. However, since it is assumed here that the figures do not differ in importance, and aggregation is a must, the upper and lower bounds are set for the evaluation.

From the pessimistic point of view, Table 2 describes the maximum number of items for which the control is lost (denote $\overline{\mathsf{M}}(\mathsf{k})$ ) if n figures are presented to the manager.

Table 2. Pessimistic Estimate of the Number of Data Items Garbled in Aggregation

<table><tr><td>n</td><td> $\overline{M}(k)$ </td></tr><tr><td>N</td><td>0</td></tr><tr><td>N-1</td><td>2</td></tr><tr><td>N-2</td><td>4</td></tr><tr><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td></tr><tr><td>N-k</td><td>2k</td></tr></table>

The preceding table is valid as long as $k \leq N/2$ . When k > N/2, all the items are not controlled from the pessimistic point of view.

It is obvious here that $\overline{M}(k) = 2k = 2(N - n)$ , $k \leq N/2$ . Suppose the probability that an exception occurs is the same for each item, then the conditional probability to detect it, given it has occurred, is:

$$
\begin{array}{l} q _ {1} = 1 - \overline {{M}} (k) / N = 2 n / N - 1, n \geq N / 2 \\ \text { Obviously, } q _ {1} = 1 \text { when } n = N, \text { and } \\ q _ {1} = 0 \text { when } n = N / 2, \text { or   less. } \end{array}
$$

$q_{1}$ would be a measure for the quality of control in a pessimistic evaluation.

From an optimistic point of view, the minimum number of items that are not controlled if n figures are presented to the manager should be determined from an optimistic point of view. Denote this number by $\underline{\mathsf{M}}(\mathsf{k})$ . Table 3 describes its nature.

For $1 \leq k \leq N - 1$ we get

$$
\underline {{M}} (k) = k + 1 = N - n + 1.
$$

Table 3. Optimistic Estimate of the Number of Data Items Garbled in Aggregation

<table><tr><td>n</td><td> $\underline{M}(k)$ </td></tr><tr><td>N</td><td>0</td></tr><tr><td>N-1</td><td>2</td></tr><tr><td>N-2</td><td>3</td></tr><tr><td>N-3</td><td>4</td></tr><tr><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td></tr><tr><td>N-k</td><td>k+1</td></tr></table>

Taking the above assumptions regarding the probability of exception the conditional probability of detection is derived:

$$
\begin{array}{r l} q _ {2} = 1 - \underline {{M}} (k) / N & = (n - 1) / N, \\ 1 \leq n \leq N - 1. \end{array}
$$

For example, if n = 2, then $q_{2} = 1/N$ , meaning that N - 1 figures have been aggregated and only one original figure remained unchanged.

Regarding the detection probability as a representative of the quality we may conclude that the quality is limited between 2n/N-1 and (n-1)/N, where N/2≤n≤N-1. The quality is limited between zero and (n-1)/N where 1≥n>N/2.

Since the pessimistic and optimistic boundaries of the quality function are both linear in n, we may say that the quality function, $q(n)$ , is a linear function of n, and write it as $q(n) = a_{1}n + a_{2}$ , where $a_{1}$ and $a_{2}$ can be estimated as shown above.

Regarding the human capacity to perceive and analyze data [34], it seems that any utility function representing that characteristic should have a single maximum value in the range between n = 1 and n = N. Recall that the number of possible comparisons is proportional to $n^{2}$ . A quadratic function might serve though not necessarily, for that purpose: $w(n) = -b_{1}n^{2} + b_{2}n + b_{3}$ . If $n_{0}$ is known to be the optimal number of n from cognitive psychology viewpoint, then the ratio, $b_{2}/2b_{1} = n_{0}$ may serve as a constraint for the equation of $w(n)$ .

Finally, in order to constitute a joint utility function, one has to calibrate $q(n)$ and $w(n)$ in order to obtain monetary values and to inquire about the tradeoffs among them. The cost of producing and reporting n items out of N has to be assessed as a function of n. We may assume that the cost is linear to n, since the data are more aggregated, less space is required for their storage, fewer retrieval operations are performed, yet more calculations are executed, and hence, arrive at a quadratic single attribute utility function of n with few constraints, whose solution should lead to an optimal n.

The preceding example is certainly simplistic, yet it exhibits an approach to handle aggregation. We return now to the general discussion on the attributes of content.

The content attributes that have been presented do not pretend to be exhaustive, nor mutually independent. Their tradeoffs and overlapping domains should be investigated while the joint utility function is assessed, as discussed in the next major section. They were brought in order to demonstrate an approach toward content evaluation.

## Format

Many possible attributes exist with regard to the format of a report. Among others, one may consider the following:

Medium—the medium by which the report is provided, such as a printed report, visual display, plotter or graphs, or microfilm, etc. [13, 51].

Ordering—the way the data is arranged in the report, such as the order of the columns or horizontal ordering, or the sequencing of details and totals, or vertical ordering, etc.

Graphic Design—the graphic setting of the report, such as colors, letter sets and font, etc. [13].

The main problem regarding the evaluation of the format related attributes is that quantitative variables cannot be obtained, hence the use of an analytical approach is almost impossible. Two methods can be used for the assessment of the value as perceived by the user. First, since in reality the number of alternatives here is very small, the user may be asked to rank order preference explicitly. Second, one may use some of those attributes, which are no more than technological characteristics, to set constraints for the other categories of attributes. For example, the usage of a line printer sets a constraint on response time. The vertical order of the printed lines might set constraints on feasible aggregations, if sorting is not desired and the files are sequential.

The above discussion presents a somewhat arbitrary list of attributes related to the assessment of the value of a reporting system. Its main purpose is to demonstrate an approach, rather than to set an ultimate attribute list.

## The Joint Utility Function

The ideal situation, from the evaluator point of view, would be when every relevant attribute is known and measurable; the utility function related to each individual attribute is clearly defined; and the tradeoffs among the various attributes are available and provide a clear mathematical formulation of the joint utility function, which also includes the cost function. In this case, an adequate optimization technique will lead to an optimal solution for a reporting system. An ideal situation like that is illustrated in the following example.

Example [2]. Suppose a user wishes to install a semiheuristic inquiry system. The system should provide information about individual customers, but the identification of the customer is not always unique. Sometimes only the name of the customer is available and sometimes the name is not even correctly spelled. There are various software packages performing such types of retrieval. The packages differ in their reliability or similarity measure, response time, and cost.

Assume the user utility function regarding the similarity measure, s, is found to be $U_{s}(s) = -a_{2} \exp(-b_{2}s)$ , where $a_{2}, b_{2} > 0$ and $a_{2}$ serves as a calibration coefficient which transforms the value of $U_{s}$ into monetary figures. s itself is based on the probabilities of errors of the first and second type described above, e.g., $s = 1 - p_{1} - p_{2}$ where $p_{1}$ is the probability that an existing desired record is not retrieved, and $p_{2}$ is the probability that the record retrieved is not the one desired.

The user utility function regarding the response time t is $U_{t}(t)=a_{1}\exp(-b_{1}t)$ , where $a_{1}, b_{1}>0$ , and $a_{1}$ calibrates the function to provide monetary values.

Now suppose the cost is increasing linearly with regard to the increasing of s and the decreasing of t, namely:

$$
c = - a _ {3} t + b _ {3} s + \text { constant } (a _ {3}, b _ {3} > 0)
$$

If the joint utility function is found to be additive with regard to $U_{t}$ , $U_{s}$ , and c, and if some coefficients can be calibrated, a utility function of the type is achieved:

Equation (2)

$$
\begin{array}{r l} \mathsf {u} & = a _ {1} \exp (- b _ {1} t) - a _ {2} \exp (- b _ {2} s) - \\ & (- a _ {3} t + b _ {3} s) + c o n s t a n t \end{array}
$$

The solution to this function under some constraints for t and s, at least t > 0 and $-1 \leq s \leq 1$ , might give some insight to the optimal system for the organization involved. After the theoretical equation (2) has been solved, one may look into the actual values of t and s characterizing each of the proposed systems, and select a system whose attributes are the closest to the values obtained in the optimal solution.

The prospects of facing an ideal case in reality are poor. More often “quick and dirty” approaches are needed which would be less sophisticated but sufficiently convincing, and above all, make sense. The following discusses and demonstrates such methods.

Suppose that constructing a joint utility function is not feasible. Moreover, even the marginal utility function for each individual attribute is not available. The user can only rank order the possible values of attributes, assuming that they are measurable, according to individual preferences. In that case, one of the following evaluation methods is recommended.

## Lexicographical ordering

This approach is useful if the value attributes can be rank ordered according to their importance, and tradeoffs are not accepted among them, i.e., the user is not willing to trade a possible decrease of a certain attribute for an increase in another [24, pp. 77-79]. For example, suppose the response time, t, is the most important attribute. Hence, if $t_{1} > t_{2}$ then system 2 is selected regardless of the value of any other attribute, assuming that the user prefers a shorter response time. If $t_{1} = t_{2}$ then the next attribute is examined and so on. This method should be used if there is a clear dominance of importance among the various attributes. It can be refined by bounding attributes to be between some given constraints. However, cases in which such dominance exists are quite rare.

## The efficient frontier

Definition. System j dominates a system k if at least one of its attribute's value is better than the corresponding value of system k and the other attribute's values of j are not worse than the corresponding values of k [24, pp. 69-77]. The set of all the systems that are not dominated by any other system, cost is considered as well, will be called the "efficient frontier." Each proposed system which does not belong to the efficient frontier can be eliminated. However, the problem remaining is how to select a system out of all members of the efficient frontier. Keeney and Raiffa [24] suggest some heuristic ways such as setting constraints to all the attributes less one, and selecting the best system with regard to the remaining attribute, as long as the constraints are satisfied.

A further refinement suggested by them would be to weight each attribute and select the system with the best “weighted average.” Virtually, this is the well known method of weighting [43] which assumes the existence of a linear utility function and linear tradeoffs; it is therefore often criticized.

Some of the above ideas have been used in order to select a minicomputer for a small business. As happens very often when theoretical concepts are applied to a real case, the evaluator has to tolerate some compromises. For example, in this case the price of the equipment considered ranged around \$40,000, hence the selection process could not be too costly in comparison to the above figure. This prohibited the use of sophisticated analysis of a utility function, rather than linear weighting. The analysis also had to comply with a certain degree of understanding mastered by the business management. Still, the case shows that the aforementioned ideas are applicable and can be used to solve real problems.

Case [3]. A regional distributor, or franchise, of an international company that produces cameras, films, x-ray machines, developing chemicals, etc., had some severe problems in managing and controlling the developing laboratory. Too many customer orders were lost, delayed, mishandled, or mistakenly mailed. Sudden shortages in developing chemicals caused delays in lab operations. The management had a vague feeling that computerized data processing would improve its operations and its planning. A feasibility study was completed, recommending the installation of a minicomputer to handle the lab data processing and the bookkeeping of the entire firm.

The feasibility report, with a cover letter, was sent to various manufacturers of minicomputers. A mandatory requirement was that a turnkey system should be proposed, including: hardware, software, operating procedures, and assistance in implementation. The possibility of smooth future upgrading was highly stressed. Six proposals were received, and they were analyzed and compared as shown in Table 4.

It is important to note that there was not any attempt to assign absolute “grades” to the proposals’ attributes. The entire evaluation was based on relative comparisons among the various proposals.

In the next step, the number of appearances of "S," "A," and "I" were counted for each proposal, resulting in the following as shown in Table 5.

The “linearity” approach was then used to rank order the various proposals, by associating three points for “S,” two points for “A,” and one point for “I.” Another rank ordering was performed for the purchase price. Both orderings are presented in Figure 2.

In other words, the price ordering from the bottom up was D, F, E, B, A, and C. The quality ordering from the bottom up was F, D and E, C, A, and B.

The evaluation rule was applied and proposals D and B were found to dominate all others; all other proposals are inferior either to B or to D. Thus, it was recommended that proposals D and B be investigated further. At this point some members of management and user departments, i.e., lab and bookkeeping, were taken to live demonstrations of systems B and D and began negotiations with manufacturers B and D. The price difference between B and D was around \$20,000, \$25,000 versus \$45,000, and what was actually being investigated was whether system B was worth the difference. Eventually, proposal B was accepted. The system is now implemented and the user is quite satisfied, mainly because management understood and was involved in the selection process, though its knowledge in DP was limited.

Table 4. Relative Ranking of Proposals' Attributes\*

<table><tr><td colspan="7">Proposal</td></tr><tr><td>Attribute</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td></tr><tr><td>hardware</td><td>S</td><td>S</td><td>A</td><td>A</td><td>A</td><td>I</td></tr><tr><td>upgrading ceiling</td><td>S</td><td>S</td><td>A</td><td>A</td><td>S</td><td>I</td></tr><tr><td>modularity of upgrading</td><td>S</td><td>S</td><td>I</td><td>A</td><td>A</td><td>I</td></tr><tr><td>software</td><td>A</td><td>S</td><td>S</td><td>A</td><td>I</td><td>I</td></tr><tr><td>similar experience of manufacturer</td><td>A</td><td>S</td><td>S</td><td>S</td><td>I</td><td>I</td></tr><tr><td>backup</td><td>I</td><td>I</td><td>A</td><td>I</td><td>S</td><td>S</td></tr></table>

\*S - superior; A - average; I - inferior

Table 5. Totals of Relative Grades

<table><tr><td>Manufacturer</td><td>Number of “S”</td><td>Number of “A”</td><td>Number of “I”</td></tr><tr><td>A</td><td>3</td><td>2</td><td>1</td></tr><tr><td>B</td><td>5</td><td>0</td><td>1</td></tr><tr><td>C</td><td>2</td><td>3</td><td>1</td></tr><tr><td>D</td><td>1</td><td>4</td><td>1</td></tr><tr><td>E</td><td>2</td><td>2</td><td>2</td></tr><tr><td>F</td><td>1</td><td>0</td><td>5</td></tr></table>

![](/api/attachments/6WCR4CYY/fulltext/images/9b606b6a5adaa3c80bc0d09b98290ec26cd6275c392d28560eccf81672e8be57.jpg)  
Figure 2. Efficient Frontier

## Conclusions

The issue of information systems evaluation suffers from scarce and scattered theoretical background as well as severe technical problems of measurement. However, it seems that if the measurement problems are at least partly overcome, there are sufficient methods of evaluation.

This article attempts to contribute to the solution of both problems. It condenses and classifies some theoretical background for information systems evaluation. It also suggests a systematic approach toward applying this theory. Some examples were given to demonstrate that approach.

The discussion here could not be exhaustive. Hopefully, it will lead to further research in that area.

## References

[1] Ackoff, R.L. “Towards a Behavioral Theory of Communication,” Management Science, Volume 4, Number 8, April 1958, pp. 218-234.

[2] Ahituv, N. “A Cost/Benefit Analysis of Data Entry and Validation System,” W.P.-14-79, Faculty of Management, The University of Calgary, Calgary, Canada, March 1979.

[3] Ahituv, N. "Techniques of Selecting Computers for Small Business," Proceedings of the 24th Annual Conference of the Interna-

tional Council for Small Business, Quebec City, Canada, June 1979.

[4] Arrow, K.J. Social Choice and Individual Values, 2nd ed., Yale University Press, New Haven, Connecticut, 1963.

[5] Arrow, K.J. “The Value of and Demand for Information,” in Decision and Organization, C.B. McGuire and R. Radner, eds., North Holland Publishing Co., Amsterdam, Holland, 1972.

[6] Barnea, A. and Lakonishok, J. "An Analysis of the Usefulness of Disaggregated Accounting Data for Forecasts of Corporate Performance," Decision Sciences, Volume 11, Number 1, January 1980, pp. 17-26.

[7] Bodnar, G. "Reliability Modeling of Internal Control Systems," The Accounting Review, Volume 50, Number 4, October 1975, pp. 747-757.

[8] Butterworth, J.E. “The Accounting System as an Information Function,” Journal of Accounting Research, Volume 10, Number 1, Spring 1972, pp. 1-27.

[9] Churchman, C.W. The Design of Inquiring Systems: Basic Concepts of Systems and Organizations, Basic Book Inc., New York, New York, 1971.

[10] Cushing, B.E. “A Mathematic Approach to the Analysis and Design of Internal Control Systems,” The Accounting Review, Volume 49, Number 1, January 1974, pp. 24-41.

[11] Demski, J.S. Information Analysis, Addison-Wesley Publishing Co., Reading, Massachusetts, 1972.

[12] Dexter, A.S. “Evaluating a Time-Share Information Systems: A Step Towards Optimization,” Proceedings of AIDS Western Regional Meeting, San Francisco, California, March 1974.

[13] Dickson, G.W., Senn, J.A. and Chervany, N.L. "Research in Management Information Systems: The Minnesota Experiments," Management Science, Volume 23, Number 9, May 1977, pp. 913-923.

[14] Edstrom, O. Man-Computer Decision Making, Gothenburg Studies in Business Administration, Goteborg, Sweden, 1973.

[15] Feltham, G.A. "The Value of Information," The Accounting Review, Volume 43, Number 4, October 1968, pp. 684-696.

[16] Feltham, G.A. Information Evaluation,

American Accounting Association, Sarasota, Florida, 1972.

[17] Gallagher, C.A. "Perceptions of the Value of Management Information System," Academy of Management Journal, Volume 17, Number 1, March 1974, pp. 46-55.

[18] Gould, J.P. “Risk, Stochastic Preference, and the Value of Information,” Journal of Economic Theory, Volume 8, Number 1, May 1974, pp. 64-84.

[19] Grochow, J.M. "A Utility Theoretic Approach to Evaluation of a Time-Sharing System," Statistical Computer Performance Evaluation, in Freiberger, W., ed., Academic Press, New York, New York, 1972.

[20] Grunfeld, Y. and Griliches, Z. "Is Aggregation Necessarily Bad?," The Review of Economics and Statistics, Volume 42, February 1960, pp. 1-13.

[21] Hedberg, B. On Man-Computer Interaction in Organizational Decision-Making: A Behavioral Approach, 2nd ed., Business Administration Studies in Gothenburg, Sweden, 1973.

[22] Ijiri, Y. The Foundation of Accounting Measurement, Prentice-Hall, Englewood Cliffs, New Jersey, 1967.

[23] Keen, P.G.W. and Scott Morton, M.S. Decision Support Systems, Addison Wesley, Reading Massachusetts, 1978.

[24] Keeney, R.L. and Raiffa, H. Decisions with Multiple Objectives: Preferences and Value Tradeoffs, John Wiley and Sons, New York, New York, 1976.

[25] King, J.L. and Schrems, E.L. "Cost-Benefit Analysis in Information Systems Development and Operation," ACM Computing Surveys, Volume 10, Number 1, March 1978, pp. 19-34.

[26] King, W.R. and Epstein, B.J. “Assessing the Value of Information,” Management Datamatics, Volume 5, Number 4, 1976, pp. 171-180.

[27] King, W.R. and Rodriguez, J.I. “Evaluating Management Information Systems,” MIS Quarterly, Volume 2, Number 3, September 1978, pp. 43-51.

[28] Lev, B. Accounting and Information Theory, American Accounting Association, Sarasota, Florida, 1971.

[29] Mace, D.R., Crowe, T. and Jones, J.H. "The Econometrics of Data Validation,"

Management Datamatics, Volume 5, 1976, pp. 65-72.

[30] Marschak, J. “Economics of Information Systems,” Journal of the American Statistical Association, Volume 66, Number 333, March 1971, pp. 192-219.

[31] Marschak, J. and Radner, R. Economic Theory of Teams, Yale University Press, New Haven, Connecticut, 1972.

[32] McGuire, C.B. “Comparison of Information Structures,” in Decision and Organization, C.B. McGuire and R. Radner, eds., North Holland Publishing Co., Amsterdam, Holland, 1972.

[33] McGuire, C.B. and Radner, R., eds. Decision and Organization, North Holland Publishing Co., Amsterdam, Holland, 1972.

[34] Miller, G.A. “The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information,” Psychological Review, Volume 63, Number 2, March 1956, pp. 81-97.

[35] Mock, T.J. The Evaluation of Alternative Information Structures, Unpublished Ph.D. Dissertation, University of California, Berkeley, California, 1969.

[36] Mock, T.J. "Concepts of Information Value and Accounting," The Accounting Review, Volume 46, Number 4, October 1971, pp. 765-778.

[37] Munro, M.C. and Davis, G.B. “Determining Management Information Needs: A Comparison of Methods,” MIS Quarterly, Volume 1, Number 2, June 1977, pp. 55-67.

[38] Neumann, S. and Segev, E. "A Case Study of User Evaluation of Information Characteristics for System Improvement," Information and Management, Number 4, forthcoming.

[39] Radner, R. “Normative Theory of Individual Decision: An Introduction,” in Decision and Organization, in C.B. McGuire and R. Radner, eds., North Holland Publishing Co., Amsterdam, Holland, 1972.

[40] Radner, R. “Teams,” in Decision and Organization, C.B. McGuire and R. Radner, eds., North Holland Publishing Co., Amsterdam, Holland, 1972.

[41] Ronen, J. and Falk, G. “Accounting Aggregation and the Entropy Measure: An Experimental Approach,” The Accounting

Review, Volume 28, Number 4, October 1973, pp. 696-717.

[42] Shannon, C.E. and Weaver, W. The Mathematical Theory of Communication, University of Illinois Press, Urbana, Illinois, 1949.

[43] Sharpe, W.E. The Economics of Computers, Columbia University Press, New York, New York, 1969.

[44] Simon, H.A. Models of Man, John Wiley and Sons Inc., New York, New York, 1957.

[45] Simon, H.A. The New Science of Management Decisions, Harper and Row Publishers, Inc., New York, New York, 1960.

[46] Snavely, H.J. “Accounting Information Criteria,” The Accounting Review, Volume 42, Number 2, April 1967, pp. 223-232.

[47] Snowball, D. and Brown, C. “Decision Making Involving Sequential Events: Some Effects of Disaggregated Data and Dispositions Toward Risk,” Decision Sciences, Volume 10, Number 4, October 1979, pp. 527-546.

[48] Stohr, E.A. “Information Systems for Observing Inventory Levels,” Operations Research, Volume 27, Number 2, March/April 1979, pp. 242-259.

[49] Streeter, D.N. "Cost-Benefit Evaluation of Scientific Computing Services," IBM

System Journal, Volume 11, Number 3, pp. 219-233.

[50] Tapiero, C.S. "Optimization of Information Measurement with Inventory Applications," Infor, Volume 15, Number 1, February 1977, pp. 50-61.

[51] Zmud, R.W. “An Empirical Investigation of the Dimensionality of the Concept of Information,” Decision Sciences, Volume 9, Number 2, February 1978, pp. 187-195.

## About the Author

Niv Ahituv is an Assistant Professor at the Faculty of Commerce and Business Administration, at The University of British Columbia. He formerly lectured at The University of Calgary and at Tel-Aviv University, and managed the Data Processing department at the Bank of Israel. He holds a B.Sc. in Mathematics, an M.B.A., and M.Sc., and a Ph.D. in Information Systems. His articles have appeared in Computers and Operation Research, The Computer Journal, Information and Management, and others. His main areas of interest are Economics of Computers, Information Economics, and Information Systems Management and Development.
