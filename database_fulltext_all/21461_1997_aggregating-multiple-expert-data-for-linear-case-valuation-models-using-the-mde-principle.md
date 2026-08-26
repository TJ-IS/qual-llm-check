---
otero_id: 21461
otero_key: "FMPJPJNN"
title: "Aggregating multiple expert data for linear case valuation models using the MDE principle"
authors: "Marvin D. Troutt; Arun Rai; Suresh K. Tadisina"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00018-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Aggregating multiple expert data for linear case valuation models using the MDE principle

Marvin D. Troutt $^{*}$ , Arun Rai $^{1}$ , Suresh K. Tadisina

Southern Illinois University, Carbondale, IL, USA

## Abstract

The Maximum Decisional Efficiency Principle is a recently developed technique for parameter estimation based on actual expert decisions. This paper illustrates how the method may be used to aggregate multiple expert data such as for developing expert system logic for binary classification problems. Previously the method has only been applied to derive a scoring function of Leontief type. In this paper the method is applied to the more important problem of deriving a linear scoring function. Hence the results here are more directly comparable to Linear Discriminant Analysis. Also an example is developed to illustrate the performance of the method when experts disagree on one or more cases to be classified. © 1997 Elsevier Science B.V.

Keywords: MDE principle; Multiple experts; Linear discriminant models

## 1. Introduction

The expert system literature recognizes the knowledge acquisition problems associated with the development of intelligent systems. The term ‘Feigenbaum bottleneck’ has been used for the long lead times and unstructured processes usually associated with eliciting the mental models of experts. As an alternative, it is suggested that the decision-making rules can, in many instances, be induced from underlying observational data. Researchers have spent considerable effort in the last few years on this subject as evidenced by the growing body of literature on machine learning.

As part of the evolving research agenda in machine learning, substantial attention has been paid primarily to three major issues.

(1) Proposing alternative induction techniques. Liang's CRIS [1], Quinlan's ID3 [2] and tree pruning approaches such as the Recursive Partitioning Algorithm (RPA) [3] are examples.

(2) Benchmarking various induction techniques with each other and, in turn, with well-known statistical models such as Linear Discriminant Analysis (LDA). A good example is the study by Cronan et al. [4].

(3) Integrating various learning techniques as illustrated by the studies of Liang et al. [5] and Tessmer et al. [6].

In addition to these issues, Liang [7] suggests that researchers investigate the social and organizational impact of intelligent systems and innovative applications of learning techniques.

The above lines of investigation are clearly important in the disciplinary development of the machine learning field. However, it appears that the present agenda overlooks a major area—the aggregation of expertise. This is important as it is increasingly recognized that complex problems do not have a ‘defined singular’ expert. In such circumstances it becomes attractive to aggregate the individual decisions of multiple experts. Intuitively, use of multiple experts to induce a consensus decision making logic should improve the reliability of resulting systems.

It is often necessary to aggregate individual decisions reached by multiple decision makers. During the decision-making process, information may be shared to facilitate a mutual understanding of differing mental models. During such information exchange sessions, the respective models of the various decision makers are no doubt refined. Eventually, however, organizational action has to be executed given a specific final decision. The problem in such situations comes down to aggregating individual decisions reached by multiple decision makers.

Techniques such as Delphi and Nominal Groups are often used to arrive at a consensus in group decision-making situations. Such processes are suitable for highly unstructured decisions where buy-in by all concerned is deemed desirable prior to the initiation of organizational action, which when initiated, will not lead to damaging consequences due to large scale disagreement. There is a high degree of uncertainty about the final decision at the initiation of those processes. During the course of consensus generation the uncertainty is reduced and a final decision is reached. These techniques are then useful in non-repetitive decision-making environments and the very nature of such decisions are often of strategic consequence for the organization.

Our approach here is not designed to reach consensus through such iterative processes. Rather we limit our attention to decision-making processes which need to be executed regularly in organizations. Several individuals are typically responsible for making such decisions in large organizations. Some examples include decisions made by loan officers in banks, admission decisions made by admissions officers, and vendor selection decisions made by purchasing officers. Decision processes of this latter kind occur with high frequency and involve multiple decision makers. These variations represent uncertainty for both the organization and the external constituents that are influenced by the decision making process.

The costs of variability between decision makers can be high for the organization and, as in the TQM literature, variance reduction may be similarly desirable. A basic tenet of organizational design is to create systems and processes that minimize uncertainty. It would then be useful in our case to understand how variations among decision-makers could be reconciled and aggregate decision models constructed.

It also becomes necessary in such contexts to consider and resolve issues such as conflicting opinions of experts and alternative decision-making models. That is, there is the practical need to model situations in which decisions have been made after review by more than one expert. Such occurrences are common in the review of large or unusual loans (Joe Kessler, President, First National Bank and Trust, Carbondale, IL, personal communication, 1994). Given the difficulties associated with the construction of expert systems using deductive techniques (such as structured interviews), it is reasonable to expect that the problem would be even more complicated when dealing with multiple experts. The application of inductive and statistical techniques holds promise in this context as well. However, there has been no past research reported in any of the leading information systems journals that explore the aggregation of decision-models of multiple experts.

The objective of our paper is to show that the Maximum Decisional Efficiency (MDE) Principle, a recently introduced estimation technique, can be employed to aggregate multiple expert data. We focus on a typical binary classification problem and limit our attention to data that represent decisions of multiple experts made under similar organizational and environmental conditions. The differences in expert decisions can then be attributed to different decision-models used by experts under similar conditions. We emphasize this constraint as the ‘selectivity’ or overall acceptance rate of an expert which in addition to possibly differing decision models, can be influenced by organizational and environmental changes. A loan officer for instance may decide to accept more loan applications when prime rates are favorable.

This paper extends the introductory MDE work $[8]$ as follows. That paper applied the MDE principle to derive a Leontief function for scoring cases to be classified. While of theoretical interest such models have not been widely used in practice. On the other hand, linear scoring functions are familiar from Linear Discriminant Analysis (LDA). According to the recent survey by Rosenberg and Gleit $[9]$ , LDA continues to be the most widely used basis for the commercially important classification systems associated with credit risk selection. Thus the primary purpose of the present article is to derive a linear scoring function from multiple expert data. The results therefore become comparable to those of LDA. Also in this paper we present a complete example which illustrates the method when experts disagree about the classification of one or more cases. Such instances are not easily handled in LDA and stress a unique capability of the MDE approach.

The remainder of the paper is organized as follows. Section 2 introduces the MDE approach for aggregating expert decisions. Section 3 illustrates the approach using the data of Table 1 and derives the consensus linear case valuation model. Section 4 provides a discussion of the results. Section 5 is the conclusion.

Hypothetical credit applicant acceptance-rejection data

<table><tr><td>Loan officer</td><td>Case</td><td>Decision</td><td> $x_1$ </td><td> $x_2$ </td><td> $x_3$ </td></tr><tr><td rowspan="9">1</td><td>1</td><td>Reject</td><td>-0-</td><td>0.78</td><td>0.84</td></tr><tr><td>2</td><td>Accept</td><td>0.68</td><td>1.00</td><td>0.76</td></tr><tr><td>3</td><td>Accept</td><td>0.64</td><td>0.71</td><td>0.74</td></tr><tr><td>4</td><td>Accept</td><td>1.00</td><td>0.70</td><td>0.81</td></tr><tr><td>5</td><td>Reject</td><td>0.57</td><td>0.49</td><td>0.59</td></tr><tr><td>6</td><td>Accept</td><td>0.80</td><td>0.83</td><td>0.75</td></tr><tr><td>7</td><td>Accept</td><td>0.65</td><td>0.70</td><td>0.80</td></tr><tr><td>8</td><td>Accept</td><td>0.74</td><td>0.71</td><td>-0-</td></tr><tr><td>9</td><td>Reject</td><td>0.80</td><td>0.56</td><td>1.00 (9 cases)</td></tr><tr><td rowspan="6">2</td><td>10</td><td>Accept</td><td>0.65</td><td>0.70</td><td>0.80</td></tr><tr><td>11</td><td>Accept</td><td>0.80</td><td>0.56</td><td>1.00</td></tr><tr><td>12</td><td>Accept</td><td>0.98</td><td>0.74</td><td>0.83</td></tr><tr><td>13</td><td>Reject</td><td>0.36</td><td>0.59</td><td>0.64</td></tr><tr><td>14</td><td>Reject</td><td>0.74</td><td>0.71</td><td>-0-</td></tr><tr><td>15</td><td>Reject</td><td>0.57</td><td>0.49</td><td>0.59 (6 cases)</td></tr><tr><td rowspan="7">3</td><td>16</td><td>Accept</td><td>0.74</td><td>0.71</td><td>-0-</td></tr><tr><td>17</td><td>Accept</td><td>0.65</td><td>0.70</td><td>0.80</td></tr><tr><td>18</td><td>Reject</td><td>0.40</td><td>-0-</td><td>0.87</td></tr><tr><td>19</td><td>Accept</td><td>0.79</td><td>0.69</td><td>0.81</td></tr><tr><td>20</td><td>Accept</td><td>0.84</td><td>0.70</td><td>0.80</td></tr><tr><td>21</td><td>Accept</td><td>0.57</td><td>0.49</td><td>0.59</td></tr><tr><td>22</td><td>Accept</td><td>0.80</td><td>0.56</td><td>1.00 (7 cases)</td></tr></table>

## 2. The MDE principle

In Ref. [8], a new general approach for aggregating expert estimates and consensus model identification has been proposed and is briefly reviewed here. This approach starts by considering the problem of identifying the most appropriate value of the parameter p in an optimization model class $f(x,p)$ . Let $x \in X$ and suppose $x^{*}(p)$ optimizes $f(x,p)$ . It is assumed that each of t = 1 to T experts provides an estimate $x'$ of the optimal $x^{\circ} = x^{*}(p^{\circ})$ for the unknown value, $p^{\circ}$ , of p. Then a decisional efficiency, or performance measure, $D(x',p)$ , is indirectly determined for each expert. An aggregator function, a, is next used to determine an aggregate decisional efficiency measure for the whole sample of experts as in:

$$
a _ {t = 1} ^ {T} D \left(x ^ {t}, p\right).\tag{2.1}
$$

In Ref. [8], some results are obtained for the case in which the $D(x^{t}, p)$ are of the ratio form:

$$
D \left(x ^ {t}, p\right) = \frac {f \left(x ^ {t} , p\right)}{f \left(x ^ {*} (p) , p\right)}\tag{2.2}
$$

where $f(x,p)$ is an agreed upon parametric model for the estimates (or actually observed decisions) given by the experts. Note that:

$$
v ^ {t} = D \big (x ^ {t}, p \big)\tag{2.3}
$$

is a measure of the performance of expert t when p is the correct or desired parameter value. It is argued that the density of $v^{t}$ in the population of experts can be expected to be an increasing function on the interval [0,1]. In particular, it was shown there that: (1) if the sum or average aggregator is used as in:

$$
\frac {1}{T} \sum_ {t = 1} ^ {T} D (x ^ {t}, p),\tag{2.4}
$$

then the corresponding MDE estimate is a Maximum Likelihood estimate for all densities in the family:

$$
g (v) = c _ {\alpha} e ^ {\alpha v}, \alpha > 0, v \in [ 0, 1 ],\tag{2.5}
$$

and (2) for the product or geometric mean aggregator:

$$
\left(\sum_ {t = 1} ^ {T} D \left(x ^ {t}, p\right)\right) ^ {1 / T}\tag{2.6}
$$

the resulting MDE estimate is a Maximum Likelihood estimate for all densities of the form:

$$
g (v) = C _ {\alpha} v ^ {\alpha}, \alpha > 0, v \in [ 0, 1 ].\tag{2.7}
$$

Remark: A cognate principle of Minimum Decisional Inefficiency (MDI) was also proposed in Ref. [8] by defining the decisional inefficiency as $D^{-1}$ and considering estimates derived from solving:

$$
\min _ {p} \underset {t = 1} {\overset {T} {a}} \left\{D (x ^ {t}, p) \right\} ^ {- 1}.\tag{2.8}
$$

It is left to the reader to observe that this approach may be regarded as use of the MDE principle with the harmonic mean aggregator. In Ref. [10], it has been shown that using the ‘minimum’ aggregator:

$$
\min _ {t = 1, T} D \left(x ^ {t}, p\right)\tag{2.9}
$$

in the MDE approach also provides a Maximum Likelihood estimation procedure under conditions described further below.

In Section 3, we discuss how the foregoing theory may be used to construct a linear case valuation function for acceptance-rejection of the type shown in Table 1.

## 3. An aggregate linear valuation function

Thus suppose data on credit application cases have been gathered as in Table 1. The reader should carefully note that such data may contain ‘multi-way contradictory’ data. For example, in Table 1, cases 5, 15 and 21 are identical. However the first two loan officers decided rejection, while the third decided acceptance. Other overlap cases are also possible, some of which are reflected in Table 1. For example, see cases 8, 14 and 16, cases 9, 11, and 22, and cases 7, 10, and 17, respectively.

Now consider the problem of finding a linear scoring or valuation function for separating the accepted and rejected cases. Because of the overlapping data cases, the presently known methods are not appropriate. This is because, for example, the data vectors common to cases 7, 10, and 17 can not be unequivocally assigned to either class. However, the MDE principle can still be applied to derive an aggregate linear valuation function and also provide additional information.

In order to apply the MDE approach first note that data have been normalized so that $0 \leq x_{i} \leq 1$ for each measurement. We assume next that there is a case valuation model $w(x)$ which measures the worth of a case to the organization. Presumably such a $w(x)$ function is a surrogate for such measures as probability of non-default, or expected profitability. Also it is assumed that the function, $w(x)$ , is monotonically increasing in each variable. Next if we consider a linear functional form such as:

$$
w (x) = \Sigma a _ {i} x _ {i},\tag{3.1}
$$

then $a_{i} \geq 0$ is required by the monotonicity. Finally, if $\Sigma a_{i} = 1$ is also required then $v(e) = 1$ where $e = (1, 1, 1)$ may be considered the ideal case.

Now in order to proceed with the MDE approach, a measure of expert performance or decisional efficiency is required. Here we propose to use what may be called the average value per case examined. Specifically, let $n_{T}$ be the number of cases which were examined by expert T. Let $J_{T}$ be the set of cases, j, accepted by expert T. Then:

$$
n _ {T} ^ {- 1} \sum_ {j \in J _ {T}} a _ {i} x _ {i j}\tag{3.2}
$$

is a measure of average value contribution to the organization per case examined. The reader may check that this measure lies in the interval $[0,1]$ for all cases.

It may be noted that the decisional efficiency measure proposed here, Eq. (3.2), actually reflects expertise in both acceptance of good cases (avoidance of Type I errors) and in the rejection of bad cases (avoidance of Type II errors). To see this, suppose that c is a cut-off value such that all cases for which $w(x) \geq c$ should in fact be accepted. Then failure to accept a case for which $w(x^{j}) < c$ , a Type

II error, will also lower the average value of cases accepted. Hence the decisional efficiency measure (Eq. (3.2)) will be larger to the extent that both types of error are avoided by the experts. This is a clearly desirable feature for any decisional efficiency measure for a classification problem.

A potential limitation of (Eq. (3.2)) arises when the sets of cases examined by the respective experts differ widely in quality. For example, if one loan officer consistently reviewed only the best cases, then his or her decisional efficiency would tend to be high regardless of actual performance. This does not occur if all cases are examined by all experts. Also if the number of cases examined by each expert is large, then their average quality will tend to be similar by the law of averages. We leave the more general situation as beyond the scope of the present paper.

Now using the “minimum” aggregator, the MDE estimation problem becomes:

$$
\max \min _ {T = 1, 3} n _ {T} ^ {- 1} \sum_ {j \in J _ {T}} a _ {i} x _ {i j}\tag{3.3}
$$

$$
\mathrm{s.t.} \Sigma a _ {i} = 1\tag{3.4}
$$

$$
a _ {i} \geq 0, i = 1, 3.\tag{3.5}
$$

Applying this approach for Table 1, the model Eqs. (3.3), (3.4) and (3.5) may be simplified as follows:

$$
\max \min \left\{\frac {1}{9} \left(a _ {1} \sum_ {j \in J _ {1}} x _ {1 j} + a _ {2} \sum_ {j \in J _ {1}} x _ {2 j} + a _ {3} \sum_ {j \in J _ {1}} x _ {3 j}\right), \right.
$$

$$
\frac {1}{6} \left(a _ {1} \sum_ {j \in J _ {2}} x _ {1 j} + a _ {2} \sum_ {j \in J _ {2}} x _ {2 j} + a _ {3} \sum_ {j \in J _ {2}} x _ {3 j}\right),\tag{3.6}
$$

$$
\frac {1}{7} \left(a _ {1} \sum_ {j \in J _ {3}} x _ {1 j} + a _ {2} \sum_ {j \in J _ {3}} x _ {2 j} + a _ {3} \sum_ {j \in J _ {3}} x _ {3 j}\right), \Bigg \}\tag{3.7}
$$

s.t. $\sum a_{i} = 1, a_{i} \geq 0$

Eqs. (3.6) and (3.7) can be reduced to a linear programming problem (LP) as, for example, in Ref.

[11]. Namely, let m be an auxiliary variable equal to the minimum of the three terms in brackets. We then obtain the LP version as:

max $m$

$$
\text { s   .   t   . } \left(\frac {1}{9} \sum_ {j \in J _ {1}} x _ {1 j}\right) a _ {1} + \left(\frac {1}{9} \sum_ {j \in J _ {1}} x _ {2 j}\right) a _ {2}\tag{3.8}
$$

$$
+ \left(\frac {1}{9} \sum_ {j \in J _ {1}} x _ {3 j}\right) a _ {3} - m \geq 0\tag{3.9}
$$

$$
\left(\frac {1}{6} \sum_ {j \in J _ {2}} x _ {1 j}\right) a _ {1} + \left(\frac {1}{6} \sum_ {j \in J _ {2}} x _ {2 j}\right) a _ {2}
$$

$$
+ \left(\frac {1}{6} \sum_ {j \in J _ {2}} x _ {3 j}\right) a _ {3} - m \geq 0\tag{3.10}
$$

$$
\left(\frac {1}{7} \sum_ {j \in J _ {3}} x _ {1 j}\right) a _ {1} + \left(\frac {1}{7} \sum_ {j \in J _ {3}} x _ {2 j}\right) a _ {2}
$$

$$
+ \left(\frac {1}{7} \sum_ {j \in J _ {3}} x _ {3 j}\right) a _ {3} - m \geq 0\tag{3.11}
$$

$$
a _ {1} + a _ {2} + a _ {3} = 1\tag{3.12}
$$

$$
a _ {i} \geq 0, m \text {   unrestricted }\tag{3.13}
$$

Problem (3.8)-(3.13) was solved using STORM® Personal Version 3.0 [12]. This package uses an implementation of the two phase revised simplex method. The solution obtained was as follows:

$$
m ^ {*} = 0. 4 3 5, a _ {1} ^ {*} = 0. 0 8 9, a _ {2} ^ {*} = 0. 0, a _ {3} ^ {*} = 0. 9 1 1.\tag{3.14}
$$

This solution is unique; that is, no alternative optimal solutions exist.

Loan officer 1 and 2 were both assigned the optimal minimum performance score of 0.435, while loan officer 3 was assigned the score of 0.576. It is necessary, from Ref. [10], to assume that $\alpha > (\ln 3) / (1 - 0.435) = 1.944$ . That is, it is necessary to assume that the three experts here come from a population of experts whose performance scores are distributed according to Eq. (2.5) with $\alpha > 1.944$ . The reader may check that this density is gently sloping upward on the interval [0,1]. Hence we argue that the assumption is a reasonable one, not requiring a dramatically steep expert performance density assumption.

An interesting and important aspect of the present approach is that a value cut-off point remains to be selected. That is, using the estimated value function model:

$$
w (x) = \sum a _ {i} ^ {*} x _ {i j},\tag{3.15}
$$

a value $w_{o}$ may be determined such that future cases are accepted when:

$$
\sum a _ {i} ^ {*} x _ {i j} \geq w ^ {\circ}\tag{3.16}
$$

and rejected otherwise. Thus the MDE approach allows a flexibility not present in previous approaches.

To illustrate this feature, suppose we set the value of $w^{\circ}$ so that the same fraction of cases will be expected to be accepted in future uses. Here 15 cases were accepted out of 22. Hence the observed acceptance rate of the set of experts was 0.682. The cut-off value $w^{\circ}$ which will provide the same acceptance rate is easily seen to be the 31.8 percentile point of the distribution of $w(x)$ scores in the data. For the estimated value function (Eq. (3.15)) the result is $w^{\circ}=0.6731$ .

It is important to emphasize that the acceptance rate need not be determined in this way, but may be considered to be a policy variable for the organization. There are many instances such as new customer promotions or temporary shortages of credit funds, in which a lending institution may wish to increase or decrease its overall acceptance rate for credit cases. Clearly this can be done by adjusting the cut-off value accordingly.

Also distributional assumptions on the value of cases can be accommodated. Having determined $w(x) = \sum a_{i}^{*} x_{ij}$ by the MDE method above, then $w(x)$ becomes a random variable on the population of cases. For instance, a Beta distribution might be fitted to the data if tests of fit indicate that to be an appropriate model.

## 4. Discussion

The performance measure used here is the average value of accepted cases per case examined. This measure, shown in Eq. (3.2) may be expressed as follows where $n_{TA}$ is the number of cases accepted by expert T:

$$
\left(n _ {T A} / n _ {T}\right) \cdot \left(\sum_ {j \in J _ {T}} a _ {i} x _ {i j} / n _ {T A}\right)\tag{4.1}
$$

The first term may be called the selectivity of expert T. In this paper, we assume that no constraints have been imposed on the loan officers. That is, each loan officer is free to accept as many or as few of the cases as judged appropriate. This is in contrast to possible situations in which loan officers are instructed to accept no more than a fixed percentage of cases.

It may be argued that Eq. (4.1) is a reasonable performance measure for comparison of loan officers for two reasons. First, if two such experts accept the same set of cases, the one who did so after examining fewer total cases should be regarded as more efficient. On the other hand, the sample set of cases examined by each expert will be random. Thus, even if both use the same case valuation model, some difference in their acceptable sets will be expected. The selectivity term allows for that difference.

It is interesting to see how the MDE model resolves the contradictory cases for this example. Using the cut-off value $w^{\circ}=0.6731$ we obtain the results shown in Table 2. It will be noted that the MDE consensus model agrees with the ‘majority’ opinion in each case here except that of cases 8, 14, and 16. Here the MDE model overruled the majority. One can argue that this case is very contradictory to acceptance given its low score on $x_{3}$ and the high imputed corresponding weight ( $a_{3}^{*}=0.911$ ) of that variable. It appears likely that the model is influenced in some sense by the whole data set. Human experts, on the other hand, are well known to have limited capacity in being consistent with past decisions.

Table 2  
Resolution of overlap cases

<table><tr><td>Overlapping case sets</td><td>Loan officer 1</td><td>Loan officer 2</td><td>Loan officer 3</td><td>Model</td></tr><tr><td>5, 15, 21</td><td>Reject</td><td>Reject</td><td>Accept</td><td>Reject</td></tr><tr><td>7, 10, 17</td><td>Accept</td><td>Accept</td><td>Accept</td><td>Accept</td></tr><tr><td>8, 14, 16</td><td>Accept</td><td>Reject</td><td>Accept</td><td>Reject</td></tr><tr><td>9, 11, 22</td><td>Reject</td><td>Accept</td><td>Accept</td><td>Accept</td></tr></table>

## 5. Conclusion and future directions

The linear case valuation model derived via the MDE principle provides an alternative to Linear Discriminant Analysis. Its two primary advantages are: first, that multiple, possibly conflicting, expert data can be aggregated and second, the MDE method focuses attention on the policy variable nature of the selectivity rate. This rate can be set independently of the data and perhaps varied during production time use of the model or corresponding expert system.

A problem for future research is to use the model for simultaneous estimation of the optimal selectivity rate. That is, in some settings it may be reasonable to assume that experts not only estimate the correct trade-offs but also the most appropriate overall selectivity rate. Similarly it would be useful to devise a decisional efficiency measure capable of differential weightings of Type I and Type II errors.

The present study limits its attention to contemporary data representing decisions of multiple experts. As one is dealing with multiple data points for each expert, it is important to examine the relative reliability among experts. It is important that an aggregation procedure discount for any inconsistencies in expert decision-making that can be identified in the underlying data. The proposed directions should set the stage for an interesting theory development journey in the area of expert data aggregation.

## References

[1] T.P. Liang, A composite approach to inducing knowledge for expert systems design, Manage. Sci. 28 (1) (1992) 1–17.

[2] J.R. Quinlan, Induction of decision trees, Machine Learning 1 (1) (1986) 81–106.

[3] L. Breiman, J.J. Friedman, R.A. Olshen, C.J. Stone, Classification and Regression Trees, Monterey, CA: Wadsworth, 1984.

[4] T.P. Cronan, L.W. Glorfeld, L.G. Perry, Production system development for expert systems using a recursive partitioning approach: an application to mortgage commercial, and consumer lending, Decision Sciences 22 (4) (1991) 812–845.

[5] T.P. Liang, T.P. Chandler, J.S., I. Han. Integrating statistical and inductive learning methods for knowledge acquisition. Expert Systems with Applications, Vol. 1, No. 4, 1990, pp. 391–401.

[6] A.C. Tessmer, M.J. Shaw, J.A. Gentry, Inductive techniques for international financial analysis: a layered approach, J. Manage. Info. Sys. 9 (4) (1993).

[7] T.P. Liang, Research in integrating learning capabilities into information systems, J. Manage. Info. Sys. 9 (4) (1993) 5–15.

[8] M.D. Troutt, A maximum decisional efficiency estimation principle, Manage. Sci. 41 (1) (1995) 76–82.

[9] E. Rosenberg, A. Gleit, Quantitative methods in credit management: a survey, Oper. Res. 42 (4) (1994).

[10] M.D. Troutt, Derivation of the maximin efficiency ratio model from the maximum decisional efficiency principle, Annals of Operations Research (to appear), accepted by L.M. Seiford, March 1995.

[11] F.S. Hillier, G.T. Lieberman. Introduction to Operations Research, 5th edn., Holden-Day, CA, 1990, pp. 445–446.

[12] H. Emmons, A.D Flowers, C.M. Khot, K. Mathur. STORM --Quantitative Modeling for Decision Support, Personal Version 3.0, Simon and Schuster Publishing, 1992.

![](/api/attachments/FMPJPJNN/fulltext/images/1b9d101ea1e974508857b62e6f9a0e085e72bf47f8e97cb4b0b881bd53c1bf66.jpg)

Marvin D. Troutt is the Rehn Research Professor of Management at Southern Illinois University, Carbondale, IL. His Ph.D. is in Mathematical Statistics from the University of Illinois at Chicago. He has worked as an actuary and also in higher education information systems. He has published articles in several journals including: Operations Research, Management Science, INTERFACES, Journal of Optimization Theory and Applications, Operations Research Letters.

Mathematical Programming, Naval Research Logistics, and European Journal of Operational Research. He is an Associate Editor of Decision Sciences and recently served as the Visiting Fellow in the Applied Mathematics Department at the Hong Kong Polytechnic University.

![](/api/attachments/FMPJPJNN/fulltext/images/363564c505ab238e8f964c6cde43c93cf42d1c5cc6ce1c210700ac26dc7b1476.jpg)

Arun Rai is an Associate Professor in the Department of Decision Sciences at Georgia State University. His research interests include management of systems delivery processes, diffusion of advanced information technologies, strategic alliances in the IT industry, and integration of information systems and management science for decision-making. Dr. Rai has published several articles on these subjects in Journal of Management Information Systems, De

cision Sciences, European Journal of Information Systems, Computers and Operations Research, Omega, Long Range Planning, and others. He is an Associate Editor of MIS Quarterly and Information Resources Management Journal.

![](/api/attachments/FMPJPJNN/fulltext/images/80193baf00381f504d346cb97296b14b463b740253adad4063e97cb474708c37.jpg)

Suresh (Reddy) K. Tadisina is an Associate Professor with the Department of Management, Southern Illinois University, Carbondale. He holds a B. Eng. (Mech) and an M.B.A. from Osmania University in India, and an M.B.A. and Ph.D. in Quantitative Analysis and Operations Management from the University of Cincinnati. He has works published in Computers and Operations Research, IIE Transactions, Journal of Applied Business Research, Journal of

the Operational Research Society, Mathematical and Computer Modeling, OMEGA, Malaysian Journal of Management Science, Project Management Journal among others. His research interests include decision support/expert systems, mathematical programming in statistics, multicriteria decision making, operations strategy, and R&D management.
