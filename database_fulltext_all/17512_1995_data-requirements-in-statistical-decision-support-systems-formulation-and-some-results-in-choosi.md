---
otero_id: 17512
otero_key: "VEDN4ZTQ"
title: "Data requirements in statistical decision support systems: formulation and some results in choosing summaries"
authors: "Terry Barron; A.N. Saharia"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00047-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Data requirements in statistical decision support systems: Formulation and some results in choosing summaries

Terry Barron $^{a,*}$ , A.N. Saharia $^{b}$

$^{a}$ Department of Information Systems and Operations Management, Stranahan Hall 4039, College of Business Administration, University of Toledo, Toledo, OH 43606-3390, USA

$^{b}$ Department of Information and Decision Sciences, College of Business Administration, University of Illinois at Chicago MC 294, Chicago, IL 60680, USA

## Abstract

The problem of determining data requirements in cases where statistical query answers are desired is studied. Specifically, we consider the value of storing aggregate data that can be used to speed up answering such queries, but at the potential costs of incomplete information due to either estimation error or staleness, as well as increased costs of update. We formulate the overall optimization problem for design, and decompose it into several subproblems that can be separately addressed. Two of these subproblems are the choice of update method, and choice of aggregates. Qualitative results are given regarding the selection of update policy, and design heuristics, based on numerical experiments, are given for single-attribute Legendre polynomial aggregates. Multivariate Legendre aggregates are also discussed, and suggestions for future research are given.

Keywords: Statistical databases; Database design; Economics of IS design; Design of decision support systems

## 1. Introduction and related research

The term “statistical decision support system” (SDSS) applies to information systems whose purpose is to answer queries that are requests for statistics about an underlying set of raw data when those answers are going to be used as an input to some decision. The term “statistical database” has a similar but more general meaning that also includes the storage and retrieval of data in scientific settings where the objectives are usually less specific. For example, in [6], three types of users are distinguished: (1) those whose queries are about individuals and thus require detailed (raw) data, (2) those who desire or are restricted to obtaining only statistical answers but require the accuracy that results from using the actual raw data (e.g. the values of population parameters when the raw data is treated as a census), and (3) those who desire statistical results and are willing to incur inaccuracies stemming from storing a representation of the distribution of the data. We are concerned with the type (2) and (3) users who use statistical answers as inputs to reasonably specific decision problems, that is, those who seek a SDSS. (Note that the user need not be human. For example, a DBMS's query optimizer is often a consumer of statistical information about the underlying raw data.)

The spirit of most queries in the business world appears to correspond roughly to the “closed-world assumption”. For example, queries to a personnel database concerning the number of employees in a department, or the average salary of females over 40 years of age, typically treat the current set of employees as a population, so that if the database state is correct, correct answers (as opposed to estimates) can be given. This stands in contrast to most scientific statistical and business forecasting applications where the database data is assumed to be a sample, and so statistics calculated from it are treated as estimators. Thus we use the “closed world” view in this paper.

We study a subset of the data requirements problem when designing a SDSS. There is very little directly related prior work on this topic in the literature. Perhaps the closest is that of [6], who use their categorization of users to motivate the need for statistical data models and a particular method for storing an approximation to the probability distribution of the data; they do not consider the impact of their classification on the data requirements problem.

Rowe [8] proposes answering statistical queries by keeping statistics about a superset (“antisample”) of one or more target samples of interest, allowing the antisample’s costs to be amortized over queries on the various subsets. He notes that updating the antisample will generally be much cheaper than updating the subsets, and certain statistics such as counts and ranges for the subsets can be given absolutely certain bounds since those statistics for the antisample form bounds for the subsets. He does not formally address the design problem, focusing instead on developing methods with desirable properties to calculate a subset’s statistics from an antisample. In the kinds of organizational databases we have in mind, it is likely that the only relevant antisample is the full database itself, and statistical queries will either be about the database as a whole or some welldefined sample of it (e.g. all female employees over 40 years of age.) Thus our work is closely related to the problem of finding low-cost estimates for statistics about subsets of the antisample which is the full database.

Another somewhat related line of work is that of statistical profile estimation, surveyed in [7], where the objective is to maintain statistics about a database for use by a query optimizer. The basic methods for representing distributions of attributes discussed in [7] are (1) parametric approaches where parameter estimates of given functional forms are stored and updated, and (2) nonparametric approaches, which usually amount to one- and two-way histograms represented by tables. These approaches can be included among the feasible alternatives for summaries in the model presented below. Further, they are complementary to the orthogonal polynomial approach we treat in detail since the exact moments can be maintained by orthogonal polynomials, but histograms and counts usually have to be estimated. (Although not studied in this paper, choosing the statistical summaries to store for an optimizer can be formulated as an instance of the design problem we develop here. As discussed in [7], specifying the relevant cost functions for all but the simplest queries is the major roadblock to formally solving the problem.)

## 2. General discussion and examples

There are several costs involved in the SDSS design problem, and as a result there are a number of tradeoffs among them to be considered in the determination of an optimal design. We highlight these informally in this section via several examples.

## 2.1. Incomplete information costs vs. answer construction costs

Consider the query “Find the average salary of employees with age > 40”, and assume the design consists of the single relation Person[Name, Age, Salary]. Two possible answers (among many others) are:

(1) The average salary calculated by using all tuples having Age > 40

(2) The average salary of a sample of tuples of size $N(\geq0)$ having Age >40

Since answer (2) supplies incomplete information (due to the sampling error resulting from excluding some tuples having Age > 40), while answer (1) does not, answer (1) will be preferred when incomplete information costs alone are considered. However, the cost of constructing the answers must also be considered, so it is possible that these costs might be small enough for answer (2) to cause some users to prefer it to answer (1).

## 2.2. Answer construction costs vs. storage and update costs

Next suppose that in addition to the relation Person, the relation Age\_Sal[Age, N\_Age, T\_Salary] is stored, where N\_Age and T\_Salary are the count and total of individual salaries, respectively, corresponding to Age (= 18, 19, etc.) Thus the query can be answered exactly, that is, answer (1) returned, but at a much lower answer construction cost. However, this design increases two other costs, storage and update. Therefore adding this summary data to the design will be worthwhile if the aggregate saving in answer construction outweighs the higher storage and update costs. Thus queries using the relation Age\_Sal must be submitted relatively frequently compared to the update rate in order for such a design to be justified.

## 2.3. Update costs vs. incomplete information costs

When an aggregate such as Age\_Sal is stored, the designer will typically have a choice of update policy as well. The attributes of Age\_Sal are such that they can be correctly updated differentially, that is, the attribute values of added, deleted and updated tuples can be directly added to or subtracted from the current values of T\_Salary to perform the update. (N\_Age can be similarly updated.) Thus three general update policies are possible: (1) continuous - Age\_Sal is updated whenever the raw data is updated, (2) differential - updates to the raw data are buffered for a period before being applied to Age\_Sal, and (3) regeneration - the entire database is scanned (or just the relevant subset of tuples retrieved, depending on the nature of the aggregate) and Age\_Sal is completely recomputed. Note that the continuous policy is a special case of the differential policy; as the period goes to zero in the differential policy, the continuous policy results. Also, the continuous and differential policies are feasible only for those types of aggregates for which there is an “on-line” algorithm to do the update. Regeneration is therefore the most general policy; it can be applied to any type of aggregate.

Costs due to incomplete information are of two types: estimation error and staleness. Estimation error results from an estimated rather than an exact answer being supplied, whereas staleness results from using older than current data to determine either an estimated or exact answer. Under continuous update, staleness cost is clearly zero, whereas the other two policies will lead to some staleness. Therefore, differential update will only be preferred to continuous when its lower update cost outweighs its higher staleness cost. The comparison between the regeneration and continuous policies is similar; however, note that the update cost under regeneration will be independent of the number of raw updates per period if the database size is roughly in equilibrium, while the update costs for the other two are directly related to the arrival rate of the raw updates. Thus there is a fairly complex set of tradeoffs in determining the update policy.

## 2.4. Choosing between types of aggregate storage

Age\_Sal allows exact answers to be constructed to certain classes of queries, namely those that can be answered exactly using total salary and number of people for each age. However, if the query is about the standard deviation of salaries within a given age, for example, then Age\_Sal is not very informative. Thus the degree to which query types are known at design time will be an important factor in selecting the type of aggregate that will be stored. When there is a significant amount of such uncertainty, or when there is a broad range of query types, one design possibility is to store an approximation of the true frequency distribution of the attribute values. If the database were to store an exact frequency distribution of the realized attribute values, all statistical queries concerning those attribute values could be answered exactly. In order to economize on data-related costs, the distribution can be approximated by Legendre polynomials, whose coefficients can be updated online very efficiently. By choosing the number of terms in the representation, any degree of accuracy can be achieved. Since the entire distribution is being represented, it is possible to realize considerable savings in data-related costs while at the same time maintaining relatively low costs of incomplete information for a broad spectrum of queries. There is therefore a clear tradeoff between the number of terms stored and the cost of incomplete information in such a design.

## 3. Formulation

From the preceding discussion, the basic design choices are:

\- Which aggregates are to be stored (if any.) This includes the choice of attributes to be summarized and the nature of the aggregate, e.g. the relation Age\_Sal vs. a Legendre polynomial representation of the joint distribution between Age and Salary.

\- The update policy. The two choices involved are the method: continuous, differential, or regeneration; and in the case of the latter two, the period between updates of the aggregate.

Designs will be denoted by the integer index $\delta \geq 0$ ; update policies will be denoted by $\nu$ (upsilon), and $\nu = (\mu, \tau)$ , where $\mu$ is the method and $\tau$ is the period.

We are interested only in statistical queries here. An information request, $\theta$ , is defined to be a pair (Q, IIC), where Q is the query, e.g. “Find the average salary of employees with age >40”, and IIC is a function that gives the cost imposed on the submitter of $\theta$ by supplying answer a, which may be only an estimate of the true answer, $\alpha$ . (Often it is assumed that $IIC(\theta, a, \alpha) \propto (a - \alpha)^{2}$ .) There are two dimensions of IIC that are relevant here: estimation error and staleness. When either is present, we must have $IIC > 0$ ; for simplicity we assume that $IIC$ is additively separable: $IIC = IIC_s + IIC_e$ , where $IIC_s$ is the staleness cost, and $IIC_e$ is the estimation cost. We assume that the underlying database stores the necessary tuples and attributes to allow the correct answer, $\alpha$ , to be constructed, and it can do so quickly enough so that $IIC_s = 0$ . However, the cost to construct $\alpha$ may be quite high since a complete scan of the database may be required. More generally, for any given design, $\delta$ , there is some cost to construct the answer returned; thus the answer construction cost for $a$ will be denoted by $ACC(\theta, a, \delta)$ . To economize on notation, we will usually suppress $\delta$ when discussing a particular design.

Each information request is assumed to have an expected arrival rate of $\lambda (\theta)$ per period. We define the design $\delta = 0$ to consist only of the raw tuples; no aggregates are stored. Thus we assume that the answer will be constructed directly from a sample of size $N$ of tuples that meet $Q$ 's qualifying condition. Such an answer will be denoted $a(N)$ . Note that $0 \leq N \leq \hat{N} \equiv$ the total number of qualifying tuples in the database, so that this sampling approach includes using the full set of qualifying tuples. Also note that $IIC(\theta, a(\hat{N})) = 0$ , and from previous remarks, $IIC_s(\theta, a(N)) = 0$ , $\forall N$ , so $IIC(\theta, a(N)) = IIC_e(\theta, a(N))$ . Since $ACC$ is increasing in $N$ and $IIC_e$ is decreasing in $N$ , there will be some optimal sample size $N^*(\theta) \equiv argmin ACC(\theta, a(N)) + IIC_e(\theta, a(N))$ (argmin denotes the optimal value of the variable over which the optimization is done.) Thus the optimal expected answer cost, $AC_0^*(\theta) \equiv ACC(\theta, a(N^*(\theta)) + IIC_e(\theta, a(N^*(\theta)))$ , and the total expected answer cost per period for $\delta = 0$ , $\overline{AC_0} \equiv \sum_{\theta} \lambda(\theta) \cdot AC_0^*(\theta)$ .

In a design $\delta\geq1$ that stores aggregates relevant to $\theta$ in addition to the raw tuples, there is more choice in answer construction, but the sampling of raw tuples just described is still possible. Thus $AC_{0}^{*}(\theta)$ represents an upper bound on the optimal expected answer cost here. Using aggregates, the expected answer cost is $AC_{A}^{*}(\theta)=IIC_{e}+IIC_{s}(\tau)+ACC_{A}$ . Note that the staleness cost depends on the period component of the update policy; if it is continuous, then $IIC_{s}=0$ , otherwise it depends on the update period. Similarly, depending on $\theta$ and the nature of the aggregate, $IIC_{e}$ could be either zero or positive. Thus $AC_{\delta}^{*}(\theta)\equiv min(AC_{0}^{*}(\theta),AC_{A}^{*}(\theta))$ is the optimal expected answer cost for $\theta$ in $\delta$ , and the total expected answer cost per period is $\overline{AC_{\delta}}\equiv\Sigma_{\theta}\lambda(\theta)\cdot AC_{\delta}^{*}(\theta)$ (which is also correct for $\delta=0$ .)

For $\delta \geq 1$ , the update costs must be considered (these costs are incremental to $\delta = 0$ .) Let $\phi$ denote the expected arrival rate of (raw tuple) updates relevant to the aggregates. Under continuous update, we will assume the average cost per update to the aggregate is $c$ , so $UC(c) = \phi \cdot c$ per period. Under differential update, the updates are batched. The only motivation for doing so must be to perform the updates at a lower cost (presumably congestion costs) during off-peak time, so we assume $c' < c$ per update applied off-peak. In addition, the updates must be stored prior to application, so let $2\sigma$ denote this cost per update per period. The buffer will gather updates for $\tau_d$ periods, so $\phi \tau_d / 2$ is the mean number of updates stored per period, making the expected storage cost $\sigma \phi \tau_d$ . Thus $UC(d) = \phi \cdot (c' + \sigma \tau_d)$ , so that $c' + \sigma \tau_d < c$ in order for the differential policy to be of interest. Under regeneration, the summary is updated by being completely recalculated, so $\phi$ is irrelevant provided the database size, $\hat{N}$ , is roughly in equilibrium; the total number of (relevant) tuples in the database itself is what matters. We assume that the same off-peak processing cost of $c'$ per tuple applies to the regeneration case as well, and that $\tau_r$ is the time between regenerations. Thus $UC(r) = c' \cdot \hat{N} / \tau_r$ since $\hat{N} / \tau_r$ is the total number of tuples processed per period in doing the updates.

The final major cost component required are those data-related costs, principally incremental (to $\delta = 0$ ) storage, required by a design but which are not accounted for above. These will be denoted by $DC(\delta)$ per period.

Thus for a given design-update policy pair, $(\delta, \nu)$ , the expected cost per period is $\overline{AC_{\delta}(\tau)} + UC(\delta, \nu) + DC(\delta)$ , and as a result, the design problem can be stated as

$$
\min _ {\delta , \nu} \overline {{{{A C}}}} _ {\delta} (\tau) + U C (\delta , \nu) + D C (\delta)\tag{1}
$$

## 4. Identification of subproblems

## 4.1. The problem for $\delta = 0$

From the definition of the costs, for $\delta = 0$ we have $UC = DC = 0$ , so that (1) becomes

$$
A C _ {0} ^ {*} (\theta) = \min _ {N} A C C (\theta , a (N)) + I I C _ {e} (\theta , a (N))\tag{2}
$$

for each $\theta$ . Note that (2) is not a design problem per se, since users can decide at query time how large a sample they want, but is, rather, the designer's model of user behaviour. (It is quite straightforward to use an SQL query to create a random sample; see for example [3, pp. 114-115].) It is relevant to the design problem because for designs $\delta \geq 1$ , $AC_{\delta}^{*}(\theta) \equiv \min(AC_{0}^{*}(\theta), AC_{A}^{*}(\theta))$ , and the total cost for those designs must be compared to $\overline{AC_{0}} \equiv \sum_{\theta} \theta \lambda(\theta) \cdot AC_{0}^{*}(\theta)$ . Certain special cases of (2) are of course well-studied in the statistics literature, particularly where $IIC_{e} = (a - \alpha)^{2}$ and $ACC$ is linear in $N$ , and may be satisfactory for estimating $AC_{0}^{*}(\theta)$ in many, perhaps most, cases. (See, for example, [5, ch. 18].)

4.2. The problem for $\delta > 0$ : the choice of update policy

Program (1) can be decomposed into first finding the optimal query and update policies for a given $\delta$ , and then optimizing over $\delta$ :

$$
\begin{array}{l} A U C ^ {*} (\delta) = \min _ {\nu} \overline {{A C _ {\delta}}} (\tau) + U C (\delta , \nu) \\ \min _ {\delta} A U C ^ {*} (\delta) + D C (\delta) \end{array}\tag{3}
$$

Furthermore, for a given $\delta$ , $IIC_{e}$ and ACC will be constant in v since it is the nature of the aggregates in the design, not the update policy, that determines the estimation error and answer construction costs. Thus only $IIC_{s}$ depends on v, and then only on $\tau$ , so that optimality comes from trading off staleness cost against update cost. As a result, (3) is equivalent to:

$$
\begin{array}{r l} A U C ^ {*} (\delta) & = \overline {{{I I C _ {e}}}} (\delta) + A C C (\delta) + \min _ {\nu} \overline {{{I I C _ {s}}}} (\tau) \\ & + U C (\delta , \nu) \end{array}\tag{4}
$$

where

$$
\overline {{{{I I C _ {s}}}}} (\tau) \equiv \sum_ {\theta} \lambda (\theta) \cdot I I C _ {s} (\theta , \tau)
$$

and

$$
\overline {{{I I C _ {e}}}} (\delta) \equiv \sum_ {\theta} \lambda (\theta) \cdot I I C _ {e} (\theta , \delta)
$$

Define

$$
U S C ^ {*} (\delta) \equiv \min _ {\nu} \overline {{{I I C _ {s}}}} (\tau) + U C (\delta , \nu)
$$

which is the optimal total of staleness and update costs. For each of the three update policies, the determination of $USC^{*}$ in (4) can be specialized further. When continuous update is used, $\overline{IIC}_{s}(\tau)=0$ . When the differential policy is used, we will assume that there is some minimum period $\tau_{d}$ (e.g. 8am–5pm) over which updates must be gathered in order to achieve the (off-peak) lower cost per update than is possible with the continuous policy $^{1}$ . Since there is no saving from delaying beyond $\tau_{d}$ , and there are added staleness and storage costs of doing so, $\tau_{d}$ is optimal. Under regeneration, we will assume that $\tau_{r}\geq\tau_{d}$ , since if it is too costly to run the differential batch during peak time, it will most likely also be too costly to run a regeneration. The update cost per period for regeneration is $UC=c'\cdot\hat{N}/\tau_{r}$ . As a result, the minimization subproblem in (4) becomes:

$$
\min \left(\phi \cdot c, \overline {{I I C}} _ {s} \left(\tau_ {d}\right) + \phi \cdot \left(c ^ {\prime} + \sigma \tau_ {d}\right), \right.
$$

$$
\min _ {\tau_ {i} \geq \tau_ {d}} \overline {{{I I C}}} _ {s} (\tau_ {r}) + c ^ {\prime} \cdot \hat {N} / \tau_ {r})\tag{5}
$$

![](/api/attachments/VEDN4ZTQ/fulltext/images/f57ca9c3d531c7bfa1fcd39127ae1cd3756dac4eb7f7a40514c30d1f7d93f5d7.jpg)  
Fig. 1. Qualitative summary of the conditions under which each update policy is preferred.

where the three costs refer to the continuous, differential and regeneration policies, respectively. It is apparent from (5) that necessary conditions for regeneration to be preferred are: $\phi \cdot (c' + \sigma \tau_d) \geq c' \cdot \hat{N} / \tau_r$ , since regeneration's staleness is at least as large as differential's; and similarly, $\phi \cdot c \geq c' \cdot \hat{N} / \tau_r$ . Qualitatively, (5) can be interpreted graphically as shown in Fig. 1.

4.3. The problem for $\delta > 0$ : the choice of aggregates

Given the cost structure of (4), it is worthwhile to study the behaviour of $\overline{IIC_{e}}$ separately from the other three components since knowledge of $\overline{IIC_{e}}$ for a family of $\delta$ 's can be used across different physical designs and staleness cost functions. There are many possible choices for storing summary information. Since many, perhaps even most, statistical queries involve one or more of the moments of the data, storing corresponding counts and sums is an obvious choice. Thus a relation in the fashion of Age\_Sal used earlier, with perhaps additional attributes to store sums of squares, cubes, etc. could be used. However, storage of the entire distribution function would be even more useful since all statistical queries about that attribute could be answered with zero cost of incomplete information, including the moment queries. If one knew the functional form of the distribution generating the data, then it might make sense to store estimates of its parameters which could be updated as tuples are added, deleted and updated (also see [11].) There are, however, two drawbacks to this direct approach in practice. The first is that the designer may not have good knowledge of the type of distribution generating the data, or even if she does, it may not be well-represented by any of the standard parametrized functional forms. Second, there may be no computationally convenient parameter estimators that are cheap to update as the database is updated. One interesting approach to storing aggregates that addresses both of these problems is to use Legendre polynomials to store an approximation of the distribution of an attribute (also see [2] and [6]). (Joint distributions can be also be represented.) By storing a greater number of terms, M, an approximation of the actual distribution to any degree of accuracy is possible. Thus one interesting family of designs can be specified by varying the number of terms used in the approximation for a given set of attributes. Here we will consider the behaviour of $\overline{IIC_{e}}$ as a function of M for a single attribute, and in the next section we describe how to extend the method to multiple attributes.

## Single-attribute summaries

The most desirable function to approximate is the empirical cumulative distribution function, $F(t) = (\text{number of sample values} \leq t)/(total\text{ number of sample values})$ , which would completely characterize the stored data from the standpoint of statistical queries. As described in Appendix A, a direct Legendre approximation of $F(t)$ can be done, but it has unattractive update properties. However, the estimated density function does have good update behaviour, so integrating its Legendre approximation term by term gives $\hat{F}(t)$ , an approximation of the empirical CDF, $F(t)$ :

$$
F (t) \simeq \hat {F} (t) \equiv \frac {t + 1}{2} + \sum_ {i = 1} ^ {M} c _ {i} \left(p _ {i + 1} (t) - p _ {i - 1} (t)\right)
$$

where the $p_{i}$ are the Legendre polynomials (see e.g. [2] or [6]) and the $c_{i}=1/2N\Sigma_{j=1}^{N}p_{i}(t_{j})$ , where N is the total number of raw tuples stored. The formula for updating the $c_{i}$ when adding or deleting a tuple t is

$$
c _ {i} ^ {\prime} = \frac {N c _ {i} \pm \frac {p _ {i} (t)}{2}}{N \pm 1}
$$

where + is used for adds, - for deletes. Clearly, computing this requires only the single attribute value being added or deleted, together with N, the total number of tuples, and is computationally trivial. Updates are handled as a delete followed by an add.

As long as M < N (which in practice is always true), $\hat{F}$ can only approximate F, although the moments $m_{i}$ can be determined exactly for $0 \leq i \leq M$ (see Appendix A), so that $IIC_{e}(\theta) = 0$ for such moment queries. When i > M, $m_{i}$ will be subject to some error. However, as our numerical experiments indicate, there appears to be rapid improvement in the representation up to about M = 6, after which the amount and rate of improvement drop very rapidly. Since in practice it is the first two moments that have the greatest interest, and queries about moments higher than the fourth are improbable, studying this error behaviour is not very interesting since a good design heuristic is to use at least M = 6 terms.

For non-moment queries the essential design question is how large M needs to be in order to yield a reasonable estimate of $F(t)$ . In order to determine some general design guidelines we employ a surrogate for $\overline{IIC_{e}}$ that abstracts from any particular set of queries, namely the mean square error resulting from comparing the actual empirical CDF, F, to its estimate, $\hat{F}_{M}$ , using M terms:

$$
M S E (M, D) = \frac {1}{N} \sum_ {j = 1} ^ {N} \left(F (t _ {j}) - \hat {F} _ {M} (t _ {j})\right) ^ {2}
$$

where the $t_{j}$ are transformed random draws from an underlying distribution of attribute values, and D is the realized set of untransformed attribute values (i.e. a sample of size N). Calculating the average of $MSE(M, D)$ , call it $MSE(M)$ , over a set of samples that simulate the distribution of D then estimates the behaviour of $\overline{IIC}_{e}$ in () as a function of M.

![](/api/attachments/VEDN4ZTQ/fulltext/images/89d5335fd050ab67e6a9cd1e5fdf01aa28a8a2ad519313f838c4c1409405b603.jpg)  
Fig. 2. Error behaviour of Legendre approximation for a uniformly distributed attribute as a function of the number of terms in the approximation.

Figs. 2, 3 and 4 plot $MSE(M)$ versus M for attribute values following uniform, normal and exponential distributions, respectively $^{2}$ . The experiments were performed as follows:

(1) Generate a random sample, $D$ , of $N$ attribute values from the distribution in question.

(2) Calculate $\hat{F} M$ for the sample for $M = 2, 3, \ldots, 12$ .

(3) Calculate $MSE(M, D)$ for each value of $M$ in 2.

This was done for 100 samples from each of the distributions; what is reported as the vertical axis in the figures is the average of the MSE values, that is, $MSE(M)$ , across the 100 samples for N = 100 and N = 1,000 observations per sample. Clearly, improvement is very rapid in all cases up to M = 6, beyond which improvement is very gradual. Note that the MSE's for the uniform distribution are at least an order of magnitude smaller than for the normal and exponential data. The effects of increasing N are most dramatic for the normal and exponential data. Also note that even for the small sample size, N = 100, the rate of improvement is extremely rapid. It is obvious from the nature of the approximation (see Appendix A) that as N grows, the average MSE for any number of terms will be uniformly smaller than for smaller sample sizes.

![](/api/attachments/VEDN4ZTQ/fulltext/images/f24205f713ca593920d0d6bea54f71a6a4d6e3cfbf8fa359cdbbcf8aa3659410.jpg)  
Fig. 3. Error behaviour of Legendre approximation for a normally distributed attribute as a function of the number of terms in the approximation.

## Representation of joint distributions

The preceding results for a single attribute extend in straightforward ways to representing joint distributions of several attributes. We will present the bivariate distribution case in detail, and then briefly discuss how to extend it to several variables.

By analogy with the single-attribute case, our focus is on the representation of the (unknown)

![](/api/attachments/VEDN4ZTQ/fulltext/images/ccdcbc27a6015686d54516839ac0fe8fad7b62a4abf3d9206618db4d30b1c1d9.jpg)  
Fig. 4. Error behaviour of Legendre approximation for an exponentially distributed attribute as a function of the number of terms in the approximation.

joint density of two attributes, X and Y. The obvious way to proceed is to first write the joint density $g(x, y)$ in its conditional-marginal form, $g(x, y) = g(y|x)g(x)$ . A Legendre representation of $g(x)$ can then be found as before, while for $g(y|x)$ the values of x can be partitioned into a set of subintervals, $X_k$ , k = 1, 2, ..., K (which need not have the same length), and a separate representation of $g(y|Xk)$ can then be constructed for the y values falling in each of the Xk. Choosing a value for K is then a design issue. There is no definitive answer to this choice; the basic guidelines are (1) when coarsely representing the dependency between the two variables yields excessive costs of incomplete information, K should be increased, and (2) the stronger is the dependence between the variables, the larger K should be. In particular, K = 1 implies $g(y|X_1)$ is just the marginal density $g(y)$ , so that one choice is to ignore any dependence between the attributes, and simply treat them as independent. This case then reduces to a pair of unrelated single-attribute representations, of $g(x)$ and $g(y)$ , so the single-attribute methods are sufficient. Thus in the sequel we will assume that $K \geq 2$ .

Unlike the single-attribute case, here many queries are likely to require finding an approximate density $g(y|X_{Q})$ for an interval $X_{Q}$ that does not exactly coincide with the $X_{k}$ intervals. An example of the most general such case is illustrated in Fig. 5. As shown in Appendix B, the needed coefficients can be calculated easily as a weighted average of the coefficients corresponding to the $X_{k}$ that are overlapped by $X_{Q}$ ; see expression (A2-3). These lead to the following two expressions which form the basis for many types of query answers:

$$
\begin{array}{r l} & g \big (y | X _ {Q} \big) \simeq \sum_ {i = 0} ^ {M} (2 i + 1) \cdot \hat {c} _ {i} (Q) \cdot p _ {i} \big (t (y) \big) \\ & P r o b \big (X _ {Q}, J \big) \simeq \frac {(j _ {1} - j _ {0})}{2} + \sum_ {i = 1} ^ {M} \hat {c} _ {i} (Q) \\ & \qquad \cdot \big [ p _ {i + 1} (t) - p _ {i - 1} (t) \big ] | _ {J _ {0}} ^ {j _ {1}} \end{array}
$$

since $\hat{c}_0(Q) = 1 / 2$ , and where $J \equiv [j_0, j_1]$ .

![](/api/attachments/VEDN4ZTQ/fulltext/images/75840eed37dc83e502e682e4dc1cd8dc35a6bb6bdde54a4011274eddbf7155fa.jpg)  
Fig. 5. Example of a bivariate $X_{Q}$ query region that overlaps the $X_{k}$ regions partitioning the data.

The estimated coefficients $\hat{c}_i(Q)$ also allow moment queries to be answered in the same fashion as in Appendix A. Consider for example "Give the average salary for all employees older than $Q$ years of age". Here $X = \text{age}$ , $Y = \text{salary}$ , so in transformed units we have $t(X) \in [t(Q), 1] = X_Q$ . Clearly in this case the right-hand boundary of $X_Q$ coincides with the upper bound of $X_K$ , while in general $t(Q)$ will not coincide with the left-hand boundary of any of the $X_k$ 's. By constructing the $\hat{c}_i(Q)$ we can then apply the formulae from Appendix A to determine any desired moments for $g(y|X_Q)$ , including the answer to the preceding query. Note however that these will not be exact unless the boundaries of $X_Q$ coincide with $X_k$ boundaries $^3$ .

Extension to joint distributions involving arbitrarily many variables is also based on expressing the desired density in conditional-marginal form

$$
\begin{array}{r l} & g \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \\ & = g \left(x _ {n} | x _ {n - 1}, \dots , x _ {1}\right) \dots g \left(x _ {2} | x _ {1}\right) g \left(x _ {1}\right) \end{array}
$$

and then applying the methods for the bivariate case.

## 5. Conclusions and future research

This paper has introduced the SDSS design problem, formulated it, and identified some of its subproblems, which can be studied in detail in order to progress toward a general design method. We have presented some qualitative results regarding the selection of update policy, and design heuristics were presented for single-attribute Legendre polynomial aggregates. Extension of the Legendre method to multivariate aggregates was also discussed.

Future research in a number of directions is desirable. First, update policies should be studied rigorously and in more detail, including consideration of “on-demand” policies. Some work on updating materialized views exists (e.g. [9] and references therein; also [1] on “quasi-copies”) that should be applicable to the SDSS problem. (It should be noted that in general staleness costs in the SDSS environment are less significant than in the materialized view/quasi-copy setting due to law-of-large-numbers effects, especially when the data are draws from a stationary distribution.) Second, designs that contain no raw tuples, only aggregates, can be considered. This introduces another dimension of tradeoffs since there will be large differences in data storage and manipulation costs between the raw data and pure aggregate types of designs. Third, considerable work needs to be done in studying alternative types of aggregates and their performance on various types of queries, and also their update performance. (An approach using parametric revisions for specific distributional forms is presented in [11].) Substantially more work on multivariate Legendre representations also remains to be done. Fourth, we have implicitly assumed in this paper that the statistical queries of interest require only one table. Thus aggregates for multi-table queries need to be studied. Hou and Ozsoyoglu [4] may be used as a starting point for these problems. Finally, we noted that one should be able to formulate the problem of selecting statistical aggregates for a database’s query optimizer within the model given here. Work on this problem remains to be done. Also, using orthogonal polynomials in the query optimizer setting seems not to have been studied to date in the literature. Their good update properties may make them attractive for use with volatile databases.

## Acknowledgements

We thank the editors and the referees for helpful comments that improved the paper, and Prof. Arie Segev for comments on update policies.

## Appendix A

Legendre polynomial method for a single attribute.

Legendre polynomials are orthogonal polynomials defined on the interval $[-1, 1]$ . (An excellent source for background information on orthogonal polynomials in general, as well as more detail on Legendre polynomials in particular, is [2].) They are defined by the following recurrence relations:

$$
\begin{array}{l} p _ {0} (x) \equiv 1 \\ p _ {1} (x) \equiv x \\ p _ {n + 1} (x) = \frac {2 n + 1}{n + 1} x p _ {n} (x) - \frac {n}{n + 1} p _ {n - 1} (x) \end{array}
$$

Linear combinations of these polynomials can be used to approximate any well-behaved function, $h(x)$ , that is,

$$
h (x) \simeq \sum_ {i = 0} ^ {M} (2 i + 1) c _ {i} p _ {i} (x)
$$

for suitably determined constants $c_{i}$ , and where M is the number of terms used in the expansion. The $c_{i}$ are determined by the normal equations:

$$
\begin{array}{l} c _ {i} = \frac {1}{2} \int_ {- 1} ^ {1} h (x) p _ {i} (x) d x (\text { continuous   case }) \\ c _ {i} = \frac {1}{2} \sum_ {j = 1} ^ {M} h (x _ {j}) p _ {i} (x _ {j}) (\text { discrete   case }) \end{array}
$$

where M is the number of points used in the net to estimate the function.

Since Legendre polynomials are defined on $[-1, 1]$ , the transformation $t(x) = (2x - a - b)/(b - a)$ can be used in order to map data on an interval $[a, b]$ onto $[-1, 1]$ , enabling the polynomials to be used with arbitrary data. In the sequel we will assume that the original data lies in an arbitrary interval and will work with the transformed data, denoted by t. We will use x when referring to the raw data.

For the purposes of statistical queries on a single attribute, the most desirable function is the empirical cumulative distribution function, $F(t) = (\text{number of sample values} \leq t)/(total number of sample values)$ , that would completely characterize the stored data from the standpoint of statistical queries. Direct approximation of $F(t)$ can be done, and yields for the $c_{i}$ :

$$
c _ {i} = \frac {1}{2 N} \sum_ {j = 1} ^ {N} p _ {i} (t _ {j}) j
$$

Unfortunately, since j in this expression is the rank (in ascending order) of $t_{j}$ among the current set of attribute values, updating the $c_{i}$ is difficult. For deletions the rank would either have to be stored or determined at update time; for insertions it would have to be determined at update time; and for modifications the ranks of many values might be changed, requiring considerable processing if ranks are stored. Thus this approach is unsatisfactory when updates are expected.

Since the spirit of supplying statistical answers is to handle large amounts of data, one would expect the cdf of the sample data to be well-approximated by the population cdf, $G(t)$ , which in turn is derivable from the population density, $g(t)$ . Writing the i-th normal equation for the coefficients for approximating $g(t)$ by Legendre polynomials gives

$$
c _ {i} = \frac {1}{2} \int_ {- 1} ^ {1} p _ {i} (t) g (t) d t
$$

Since $g(t)$ is unknown, this integral cannot be directly calculated. However, note that the integral is the expected value of $p_{i}(t)$ ; this can be estimated by the sample mean of the $p_{i}(t_{j})$ , $\frac{1}{N}\sum_{j=1}^{N}p_{i}(t_{j})$ , where the $t_{j}$ are the (transformed) values stored by the database for the attribute in question. Clearly, the larger is N the better will be the estimate. Substituting this into the preceding expression yields

$$
c _ {i} \simeq \frac {1}{2 N} \sum_ {j = 1} ^ {N} p _ {i} (t _ {j})\tag{A1-1}
$$

giving

$$
g (t) \simeq \sum_ {i = 0} ^ {M} (2 i + 1) c _ {i} p _ {i} (t)
$$

Expression (A1-1) has the important property that it can be updated very cheaply. Letting $c_{i}^{\prime}$ be the updated coefficient, the formula for updating the ci when adding or deleting t is:

$$
c _ {i} = \frac {N c _ {i} \pm \frac {p _ {i} (t)}{2}}{N \pm 1}
$$

where + is used for adds, - for deletes. Clearly, computing this requires only the single attribute value being added or deleted, together with M, the total number of tuples, and is computationally trivial. Updates are handled as a delete followed by an add. (Note that $c_{0}=(1/2N)\cdot N=1/2$ , so that $c_{0}$ does not need to be calculated from the data, nor does it need to be updated.)

The $c_{i}$ also allow the exact computation of sample moments. In practical terms it is the central moments that are of interest, so we will concentrate on these. Since these will be calculated in terms of moments about the origin, there is no loss of generality. By definition, the n-th central moment of the untransformed data is given by

$$
m _ {n} (x) \equiv \frac {1}{N} \sum_ {j = 1} ^ {N} \left(x _ {j} - \overline {{{x}}}\right) ^ {n}
$$

Solving the transform for $x_{j}=((b-a)t_{j}+(a+b))/2$ and substituting into the expression above gives

$$
m _ {n} (x) = \left[ \frac {b - a}{2} \right] ^ {n} m _ {n} (t)\tag{A1-2}
$$

As a result, it suffices to find central moments of the transformed data. The central moments in turn can be expressed in terms of the mean (first moment about the origin) together with moments about the origin. We will use $M_{i}$ to refer to the i-th moment about the origin. Since simple expressions for the $M_{i}$ can be given in terms of the Legendre coefficients, it is useful to relate the central and origin moments. We supply here formulae for moments up to $m_{4}$ ; a general expression for moments of any degree results from the binomial formula, and can be found in [10], p. 79.

$$
\begin{array}{r l} & m _ {2} (t) = M _ {2} (t) - M _ {1} ^ {2} (t) \\ & m _ {3} (t) = M _ {3} (t) - 3 M _ {2} (t) M _ {1} (t) + 2 M _ {1} ^ {3} (t) \\ & m _ {4} (t) = M _ {4} (t) - 4 M _ {3} (t) M _ {1} (t) + 6 M _ {2} (t) M _ {1} ^ {2} (t) \\ & \quad - 3 M _ {1} ^ {4} (t) \end{array}
$$

Additionally, we have

$$
\begin{array}{r l} \bar {x} & = M _ {1} (x) = \left[ \frac {b - a}{2} \right] \bar {t} + \frac {a + b}{2} \\ & = (b - a) c _ {1} + \frac {a + b}{2} \\ & = (b - a) c _ {1} + (a + b) c _ {0} \end{array}
$$

Evaluating $M_{n}(t)$ is quite straightforward. By definition,

$$
M _ {n} (t) \equiv \frac {1}{N} \sum_ {j = 1} ^ {N} t _ {j} ^ {n}\tag{A1-3}
$$

Since it is a polynomial, the function $t \nmid n$ in (A1-3) can be expressed exactly as a linear combination of Legendre polynomials up to and including degree $n$ , so that for suitable coefficients $ai(n)$ determined from the normal equations, we have

$$
t ^ {n} = \sum_ {i = 0} ^ {n} (2 i + 1) a _ {i} (n) p _ {i} (t)
$$

Substituting this into (A1-3) and reversing the order of the summations gives

$$
M _ {n} (t) = \frac {1}{N} \sum_ {i = 0} ^ {n} a _ {i} (n) \sum_ {j = 1} ^ {N} p _ {i} \left(t _ {j}\right) = 2 \sum_ {i = 0} ^ {n} a _ {i} (n) c _ {i}\tag{A1-4}
$$

Therefore $M_{n}(t)$ can be determined exactly as a linear combination of the $c_{i}$ . Note that the $a_{i}(n)$ do not depend on the database data, so the formulas for the moments can be trivially computed on the basis of the current values of the $c_{i}$ . By carrying out the calculations for the $a_{i}(n)$ 's we have the following results for $M_{0}$ through $M_{4}$ $^{4}$ :

$$
\begin{array}{r l} & M _ {0} (t) = 2 c _ {0} = 1 \\ & M _ {1} (t) = \bar {t} = 2 c _ {1} \\ & M _ {2} (t) = \frac {2}{3} (c _ {0} + 2 c _ {2}) \\ & \Rightarrow m _ {2} (t) = \sigma^ {2} (t) = M _ {2} (t) - M _ {1} ^ {2} (t) \\ & M _ {3} (t) = \frac {2}{5} (3 c _ {1} + 2 c _ {3}) \\ & M _ {4} (t) = \frac {2}{3 5} (7 c _ {0} + 2 0 c _ {2} + 8 c _ {4}) \end{array}
$$

Moments of any order are easily calculated in this fashion from (A1-4) by using the normal equations to find the appropriate $a_{i}(n)$ :

$$
a _ {i} (n) = \frac {1}{2} \int_ {- 1} ^ {1} t ^ {n} p _ {i} (t) d t
$$

## Appendix B

Legendre polynomial method-multiple attributes.

The objective is to determine a Legendre representation for $g(y|X_{Q})$ . Since $g(y|X_{Q})$ is a density on y calculated for those tuples having $x_{t} \in X_{Q}$ , from Appendix A the desired coefficients are given by

$$
c _ {i} (Q) = \frac {1}{2 \cdot N _ {Q}} \cdot \left[ \sum_ {j \in Q} p _ {i} \left(t _ {j}\right) \right]\tag{A2-1}
$$

where $j \in Q$ means all of those $t(y_{j})$ such that the value of the x-attribute of $y_{j}$ 's tuple lies in $X_{Q}$ , and $N_{Q}$ is the number of tuples falling in $X_{Q}$ . Define $I_{1}, I_{2}, \ldots, I_{q}$ to be the $X_{k}$ intervals that $X_{Q}$ overlaps. Thus $I_{2}$ through $I_{q-1}$ will be contained completely within $X_{Q}$ , while in general $I_{1}$ and $I_{q}$ will not lie entirely within $X_{Q}$ (although one or both may as special cases.) Since the coefficients are available for each of $g(y|I_{k})$ , $k=1,\ldots,q$ , we can write (A2-1) as

$$
\begin{array}{r l} c _ {i} (Q) & = \frac {1}{2 \cdot N _ {Q}} \cdot \left[ \sum_ {j \in Q} p _ {i} (t _ {j}) \right] \\ & = \frac {1}{2 \cdot N _ {Q}} \cdot \left[ 2 \sum_ {k = 1} ^ {q} N _ {k} c _ {i} (k) - \sum_ {j \in I _ {1} - X _ {Q}} p _ {i} (t _ {j}) \right. \\ & \left. - \sum_ {j \in I _ {q} - X _ {Q}} p _ {i} (t _ {j}) \right] \end{array} \tag {A2-2}
$$

However, there are two problems with (A2-2). First, $N_{Q}$ cannot be determined exactly. Second, the sets $I_{1}-X_{Q}$ and $I_{q}-X_{Q}$ , and therefore the corresponding $p_{i}(t_{j})=p_{i}(t(y_{j}))$ cannot be determined without going to the raw data. We can however use the following approximations. For $N_{Q}$ we have $N_{Q}\simeq N\cdot G_{X}(X_{Q})$ , where $G_{X}$ is the Legendre approximation of the cumulative (marginal) distribution of X, and N is the total number of tuples. The second problem is resolved by, first, estimating the number of points in $I_{1}-X_{Q}$ and $I_{q}-X_{Q}$ by $N_{1}-N\cdot G_{X}(I_{1}\cap X_{Q})$ and $N_{q}-N\cdot G_{X}(I_{q}\cap X_{Q})$ , and, second, observing that we can estimate an arbitrary $p_{i}(t_{j})$ in each of these two intervals by the average value of $p_{i}(t_{j})$ in the interval, namely $2c_{i}(I_{1})$ and $2c_{i}(I_{q})$ , respectively. Substituting these approximations into (A2-2) gives

$$
\begin{array}{l} c _ {i} (Q) = \frac {1}{2 \cdot N _ {Q}} \cdot \left[ 2 \sum_ {k = 1} ^ {q} N _ {k} \cdot c _ {i} (k) - \sum_ {j \in I _ {1} - X _ {Q}} p _ {i} (t _ {j}) \right. \\ \left. - \sum_ {j \in I _ {q} - X _ {Q}} p _ {i} (t _ {j}) \right] \\ \simeq \frac {1}{2 \cdot N \cdot G _ {X} (X _ {Q})} \cdot \left[ 2 \sum_ {k = 1} ^ {q} N _ {k} c _ {i} (k) \right. \\ \left. - 2 c _ {i} (I _ {1}) \cdot [ N _ {1} - N \cdot G _ {X} (I _ {1} \cap X _ {Q}) ] \right. \\ \left. - 2 c _ {i} (I _ {q}) \cdot [ N _ {q} - N \cdot G _ {X} (I _ {q} \cap X _ {Q}) ] \right] \end{array}
$$

$$
\begin{array}{l} = \frac {1}{G _ {X} (X _ {Q})} \cdot \left[ \sum_ {k = 2} ^ {q - 1} \frac {N _ {k}}{N} \cdot c _ {i} (k) + c _ {i} (I _ {1}) \right. \\ \left. \cdot G _ {X} (I _ {1} \cap X _ {Q}) + c _ {i} (I _ {q}) \cdot G _ {X} (I _ {q} \cap X _ {Q}) \right] \\ \equiv \hat {c} _ {i} (Q) \end{array} \tag {A2-3}
$$

(A2-3) is easily computed. $G_{X}(X_{Q})$ comes from the Legendre representation of $X$ 's marginal CDF, and similarly for the other two $G_{X}$ terms; the $N$ and $N_{k}$ terms are stored as part of the design (alternatively, $N_{k}/N$ could be replaced by $G_{X}(X_{k})$ ); and the remaining terms are $c_{i}$ 's that are stored for the conditional densities corresponding to the $X_{k}$ 's used in the design. It is clear from (A2-3) that the estimate of $c_{i}(Q)$ is a weighted average of the coefficients for the intervals that $X_{Q}$ overlaps since $\frac{1}{G_{X}(X_{Q})} \cdot \left[ \sum_{k=2}^{q-1} \frac{N_{k}}{N} + G_{X}(I_{1} \cap X_{Q}) + G_{X}(I_{q} \cap X_{Q}) \right] = 1$ .

## References

[1] R. Alonso, D. Barbará, and H. Garcia-Molina, Data Caching Issues in an Information Retrieval System, ACM-TODS 15, nr. 3 359–384 (1990).

[2] P. Beckmann, Orthogonal Polynomials for Engineers and Physicists (The Golem Press, Boulder, CO, 1973). [3] G. Diehr, Database Management (Scott, Foresman and Co., Glenview, IL, 1989).

[4] W.C. Hou and G. Ozsoyoglu, Statistical Estimators for Aggregate Relational Algebra Queries, ACM-TODS 16, nr. 4, 600–654 (1991). [5] I. LaValle, An Introduction to Probability, Decision, and Inference (Holt, Rinehart and Winston, New York, 1970).

[6] E. Lefons, A. Silvestri and T. Filippo, An Analytic Approach to Statistical Databases, Proceedings of the Ninth International Conference on Very Large Databases, 260-274 (1983).

[7] M.V. Mannino, P. Chu and T. Sager, Statistical Profile Estimation in Database Systems, ACM Computing Surveys 20, nr. 3, 191–221 (September, 1988).

[8] N. Rowe, Antisampling for Estimation: An Overview, IEEE Transactions on Software Engineering 11, nr. 10, 1081–1091 (October, 1985).

[9] A. Segev and W. Fang, Updating Distributed Materialized Views, Management Science 37, nr. 7, 851–870 (1991).

[10]M. Spiegel, Schaum's Outline of Theory and Problems of

Probability and Statistics, (McGraw-Hill Book Company, New York, 1975).

[11]J.C. Westland, Reporting Strategies for “Events” Accounting, Journal of Information Systems (September, 1993).

Terry Barron is Assistant Professor of Computers and Information Systems at the William E. Simon Graduate School of Business Administration, University of Rochester. His research interests include economics of information, economics of information system management, the impacts of information technology on organizations and markets, and economic aspects of the design of information systems. His research has appeared in Information Systems Research, Decision Support Systems, the Journal of Organizational Computing, Data and Knowledge Engineering, and other journals and conference proceedings.

![](/api/attachments/VEDN4ZTQ/fulltext/images/8e24291cf9600a4f2999f665c48d931c546a186b08b94fc6898efcb640cd0c6d.jpg)

Aditya N. Saharia is Assistant Professor of Management Information Systems at the University of Illinois at Chicago. He received his PhD in Physics from Carnegie-Mellon University and MBA in Computers and Information Systems from the University of Rochester. His research interests include database systems and information resources management. His research has appeared in ACM Transactions on Database Systems,

Information Systems Research, Journal of Management Information Systems, IEEE Transactions on Knowledge and Data Engineering, Decision Support Systems, among others. He is a member of TIMS, ACM, and SIM
