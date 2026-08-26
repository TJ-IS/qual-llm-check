---
otero_id: 24461
otero_key: "BWDEM2NZ"
title: "Security of Statistical Databases with an Output Perturbation Technique"
authors: "Nabil R. Adam; Douglas H. Jones"
year: "1989"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1989.11517851"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Security of Statistical Databases with an Output Perturbation Technique

Nabil R. Adam & Douglas H. Jones

To cite this article: Nabil R. Adam & Douglas H. Jones (1989) Security of Statistical Databases with an Output Perturbation Technique, Journal of Management Information Systems, 6:1, 101-110, DOI: 10.1080/07421222.1989.11517851

To link to this article: http://dx.doi.org/10.1080/07421222.1989.11517851

![](/api/attachments/BWDEM2NZ/fulltext/images/cbbec57346ebf473461fb4c6f61b26bfeab3a65cc98c25f7f36201b3804db82e.jpg)

Published online: 22 Dec 2015.

![](/api/attachments/BWDEM2NZ/fulltext/images/b4f7908ab5d7218ceb93517768b6ce7e25c7657f56aee40761bd8e273c1be01b.jpg)

Submit your article to this journal ↗

![](/api/attachments/BWDEM2NZ/fulltext/images/9e0c5ae225632d840eaa08c9004a48cbbee9f2a10d831bf55ec4cc811977fcc7.jpg)

View related articles ↗

# Security of Statistical Databases with an Output Perturbation Technique

NABIL R. ADAM and DOUGLAS H. JONES

NABIL R. ADAM is Associate Professor at the Graduate School of Management of Rutgers University. He received his M.S., M.Phil., and Ph.D. from Columbia University. He has contributed to ACM Computing Surveys, European Journal of Operational Research, Management Science, and IEEE Transactions. He has edited a special issue on Database Management for JMIS, on Computer Simulation for Communications of the ACM, and has co-edited a special issue on Simulation for Operations Research. His research interests include database security, concurrency control in distributed database systems, computer simulation and scheduling. He has served as a consultant in the area of Database Management to several major organizations.

DOUGLAS H. JONES is Associate Professor of Quantitative Studies at the Graduate School of Management of Rutgers University. He received his M.S. and Ph.D. from Florida State University, and his B.S. from Florida Atlantic University–Boca Raton. His specialties include Mathematical and Applied Statistics, Mental Measurement, and Data Analysis. He has published in the Annals of Statistics, Journal of the American Statistical Association, and Psychometrika.

ABSTRACT: A statistical database aims at providing users with statistics about the population while not compromising the confidentiality of the individuals whose data are included in the database. Threats to the database security range from issuing cleverly designed sequences of queries to using such sophisticated methods as regression analysis. In order to overcome this security problem, several solution methods have been suggested in the literature. These methods can be classified under four general approaches: conceptual modeling; query restriction; data perturbation; and output perturbation. These methods, however, can be easily compromised, or require excessive CPU and memory, or result in biased response to users.

The purpose of this paper is to propose a new type of output perturbation method that may be very difficult to compromise and provides unbiased response. The method is based on recoding of the data, the jackknifing concept, and an extension of the random sample queries method suggested by Denning [5]. A comparison of the proposed method and the modified random sample queries method (which is considered a viable alternative for security of statistical databases) is presented.

KEY WORDS AND PHRASES: Database management, statistical databases, and database security.

## 1. Introduction

A DATABASE OF A GIVEN ENTERPRISE COMPRISES a description of, and relationships among, some distinguishable elements of that enterprise. Those elements are referred to as entities. For example, faculty member Joe Smith with social security number 111-22-3456 is an entity in a university environment. An entity may be either concrete, such as a faculty member, or it may be abstract, such as a class schedule. An entity is represented by a set of attributes. In a university environment, social security number, name, and rank are examples of attributes of the faculty entity.

A statistical database system (SDB) is a special type of database system that aims at providing users with only aggregate statistics (e.g., sample mean and count) of confidential information such as income, credit ratings, type of disease, and test scores of individual entities in the database.

An SDB also aims at guarding against the user's ability to infer any confidential information related to a specific individual whose data are included in the database. Thus, the system does not respond to a query whose response involves one entity, or in general a few entities. For the purpose of illustration, consider a faculty database with the attributes: salary, academic rank, sex, age, department, and highest degree. Suppose that a malicious user (snooper) of that system, who is authorized to use the database only for the purpose of studying the characteristics of the faculty as a whole, is attempting to infer the salary of the only 42-year-old female computer science associate professor. Such a malicious user would get no response for the following query:

COMPUTE average salary (rank=associate professor AND sex=female AND age=42 AND department=computer science AND highest degree=Ph.D.)

This user can, however, compromise the database by obtaining responses to the following set of queries:

Q1: COUNT (rank=associate professor AND sex=male AND department=computer science AND highest degree=Ph.D.)

Q2: COMPUTE average salary (rank=associate professor AND sex=male AND department=computer science AND highest degree=Ph.D.)

Q3: COUNT (rank=associate professor AND department=computer science AND highest degree=Ph.D. AND (sex=male OR (sex=female AND age=42)))

Q4: COMPUTE average salary (rank=associate professor AND department=computer science AND highest degree=Ph.D. AND (sex=male OR (sex=female AND age=42)))

Suppose that $n_{1}, \overline{x}_{1}, n_{2}, \overline{x}_{2}$ are, respectively, the responses to the above queries. If $n_{2} = n_{1} + 1$ the snooper's target is uniquely identified by the characteristics “age=42 and sex=female” and the snooper is then able to infer the target's salary, which is given by $n_{2} \overline{x}_{2} - n_{1} \overline{x}_{1}$ .

As seen by the above example, an authorized user may cleverly design other complex sequences of queries that would result in compromising the database.

Such a user who is making improper use of the aggregate data, normally available to him/her is referred to as a “snooper.” In addition, threats to the database security include sophisticated methods such as regression analysis. For example, Palley [9] and Palley and Simonoff [10] discuss the use of regression analysis to compromise statistical databases.

In order to overcome this security problem, several solution methods have been suggested in the literature. These methods can be classified under four general approaches: conceptual modeling, query restriction, data perturbation, and output perturbation. A brief overview of these approaches is presented below. A detailed review of the methods based on these approaches is presented in, e.g., [4, 6, 2].

The conceptual modeling approach develops a framework that deals with the security problem at the conceptual data modeling level. Although this framework has helped in broadening the scope of research in security of statistical databases, it is an ambitious endeavor and to date has not been realized as a completely working software system.

Security control methods that are based on the query restriction approach provide protection through one of the following measures: (1) Restricting the query set size, i.e., permitting a statistic to be released only if the query set (the number of entities included in the response to the query) exceeds a certain value set by the database administrator; (2) Restricting the number of overlapping entities among successive queries of a given user; (3) Auditing, i.e., keeping up-to-date logs of all queries made by each user and constantly checking for possible compromise whenever a new query is issued; (4) Partitioning, where individual entities are clustered in a number of mutually exclusive subsets whose statistical properties constitute the raw materials available to the database users; and (5) Cell suppression, which is typically used by census bureaus for data published in tabular form.

The data perturbation approach introduces noise in the data. In this case, the original database is transformed into a modified (perturbed) SDB, which is then used to satisfy user queries. For example, the faculty database discussed above would be replaced by a modified one where a random noise is added to the salary of each faculty in the database.

The output perturbation approach perturbs the answer to user queries while leaving the data unchanged. For example, the response to query Q2, mentioned above, would be based on a random sample taken from those records that satisfy the conditions: rank=associate professor AND sex=male and department=computer science AND highest degree=Ph.D.

Security control methods based on the first two approaches either can be easily compromised or their time and storage requirements render these methods impractical to real world applications (see for example [2]).

Data perturbation based methods suffer from a bias problem [8], are not suitable for dynamic SDBs, or are limited to one confidential attribute [2].

Although output perturbation methods do not suffer from the bias problem, they suffer, however, from the possibility of having a null query set, thus providing valuable information to a snooper. Compromised methods such as regression based ones could take advantage of the null query set situation. Among the output perturbation methods, the random sample queries method developed by Denning [5] is considered a viable alternative for SDBs where several dependent attributes are involved (e.g., [2]).

It is the purpose of this paper to propose a new type of data perturbation that may defeat most snoopers. The key element of our perturbation method is the recoding of the data. The recoding makes use of a fully saturated linear model, which we will explain shortly. The following example illustrates a simple case.

The general form of a statistic requested in the query is:

$$
E (y \mid \mathbf {x})
$$

where y is the confidential attribute whose sample mean is requested, and where $\mathbf{x} = (x_{0}, \ldots, x_{p})^{T}$ is a column vector of indicator variables (a type of boolean variable) coding the attributes included in the query. The expected value is defined as the average over the individual records in the database that have a common coding x.

In the above example, suppose a query is issued concerning degree and gender, then p is equal to 7 (as shown below), y is income, $x_{1}-x_{3}$ represent highest degree earned, e.g.:

<table><tr><td>highest degree</td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td></tr><tr><td>High School (HS) or less</td><td>1</td><td>1</td><td>1</td></tr><tr><td>B.S. or B.A.</td><td>0</td><td>1</td><td>0</td></tr><tr><td>M.S. or M.A.</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Ph.D.</td><td>0</td><td>0</td><td>0</td></tr></table>

and $x_{4}$ represents the gender, e.g.:

<table><tr><td>gender</td><td> $x_{4}$ </td></tr><tr><td>female</td><td>1</td></tr><tr><td>male</td><td>0</td></tr></table>

Furthermore, $x_0$ is a constant 1; and the rest of the vector $\mathbf{x}$ is defined as:

$$
x _ {5} = x _ {1} \cdot x _ {4} \quad x _ {6} = x _ {2} \cdot x _ {4} \quad x _ {7} = x _ {3} \cdot x _ {4}
$$

The attributes $y$ and $x$ are assumed to be related according to the following regression equation:

$$
E (y \mid \mathbf {x}) = \mathbf {x} ^ {T} \boldsymbol {\beta}
$$

where $\beta$ is a column vector of dimension 8. The least squares estimate (LSE) of $\beta$ provides the response to user queries involving degree and gender as the following example shows:

compute the average salary of female persons whose highest degree is M.S.

x-VECTOR CORRESPONDING TO QUERY:

$$
[ \mathbf {x} = (1, 0, 0, 1, 1, 0, 0, 1) ]
$$

$$
\text {   COMPUTED   RESPONSE:   }
$$

$$
\mathrm{average} y = \beta_ {0} + \beta_ {3} + \beta_ {5} + \beta_ {7}
$$

The above regression model is an example of a fully saturated model. In fully saturated models, when the predictor variables are indicator variables, the model is overspecified and prediction values would be identical to the average of the outcome variable over all the records that have the same code x. In other words, the model does not differ from the data in its ability to provide averages over query sets, and thus, it is an effective recoding of the data for database query.

In brief, our perturbation method consists of using a resampling plan to replace (without bias over resamples) the least squares estimate (LSE) of the $\beta$ vector and in turn to provide perturbed values for query responses. Our method is a member of the output perturbation approach. Methods based on this approach could provide unbiased, although slightly inefficient, estimators of the query responses while preserving confidentiality of the database. Specifically, we limit our attention to the random sample queries method suggested by Denning [5].

Our perturbation method could use any resampling plan as long as the corresponding estimate of LSE( $\beta$ ) is unbiased and enjoys high efficiency. The jackknife and the bootstrap are well-known members of this class of resampling plans [7]. Our method incorporates Wu's recent extension of the jackknife and the bootstrap to unbiased estimation of the general linear model [12]. An advantage of Wu's extension is that his method provides superior estimates of the variability of the least-squares estimator (LSE) that are robust against heteroscedastic variance among query sets.

In this paper we explore the feasibility of the jackknife form of resampling. In addition we recast the Denning output perturbation method as a resampling plan and discuss its feasibility for our perturbation method. We refer the reader to another paper for discussion and experimental results on the use of bootstrap resampling plan $[1]$ .

The remainder of the paper is organized as follows. Sections 2 and 3 include a discussion on the data coding scheme and the database model, respectively. The proposed method is discussed in section 4, followed by a discussion of the extended random sample queries method [5]. Section 5 compares the two methods, and the conclusion is presented in section 6.

## 2. The Database Model

CONSIDER A DATABASE THAT CONSISTS of a total of N records with each record having K attributes. Let $x_{ij}$ be the jth attribute of the ith record. Suppose a query is issued in order to obtain an estimate of a confidential attribute y. A subset of those records whose data are included in the computation of the response to the query is referred to as the “query set.” Statistics are calculated for subsets of records having common attribute values (e.g., highest degree earned=Ph.D., academic rank=Professor, . . .). Such a subset can be specified by a characteristic formula, C, which is a logical formula over the values of the attributes, using the boolean operators: AND(&), OR(+), NOT(-). For example:

$$
C = (\text { Highest   Degree } = \text { Ph.D. }) \& (\text { Sex } = \text { Female }) \& (\text { Rank } = \text { Professor })
$$

is a characteristic formula that specifies the subset of female professors with Ph.D. degrees. Let n be the size of the query set (number of records that make up the set), and k be the number of attributes included in the set. Now consider the fully saturated linear model consisting of all first and higher order effects

$$
y _ {i} = \mathbf {x} _ {i} ^ {T} \beta + e _ {i}\tag{1}
$$

where $\mathbf{x}_{i}=(x_{i1},x_{i2},\ldots,x_{ip})^{T}$ is a vector of indicator variables for the k attributes and their product terms, for $i=1,2,\ldots,N$ , $e_{i}=y_{i}-x_{i}$ are the deviations between individual database values and their group mean, and $\beta=(\beta_{1},\beta_{2},\ldots,\beta_{p})^{T}$ is a known vector of parameters determined by the database.

Let $\mathbf{X} = (x_1, x_2, \ldots, x_n)^T$ , $\mathbf{y} = (y_1, y_2, \ldots, y_n)^T$ and $\mathbf{e} = (e_1, e_2, \ldots, e_n)^T$ . Then the above regression model may be rewritten in matrix notation as

$$
\mathbf {y} = \mathbf {X} \beta + \mathbf {e}\tag{2}
$$

The LSE is formulated as

$$
\beta = (\mathbf {X} ^ {T} \mathbf {X}) ^ {- 1} \mathbf {X} ^ {T} \mathbf {y}\tag{3}
$$

where a standard reduction of X has been taken in order for $(\mathbf{X}^{T}\mathbf{X})^{-1}$ to exist, e.g., eliminating the redundant columns of X and the corresponding components of $\beta$ . Throughout the rest of the paper we will refer to the LSE obtained directly from the query set without applying any security control method as the unperturbed LSE or ULSE.

## 3. An Output Perturbation Approach Based on Jackknifing

## 3.1 Jackknifing

The term “jackknife” was originally coined by Tukey [11] to denote the estimators that are obtained from subsets of the original sample. Originally jackknife was used to refer to the point estimator of a function, g, of a location parameter, $\theta$ , $g(\theta)$ that would have less bias than the usual estimator based on the sample mean, thus providing a generally useful statistical procedure. Today the term simply refers to the partitioning of the original sample into all subsets of size r.

Let $r \geq k$ and $s = (i_1, i_2, \ldots, i_r)$ denote a subset of the integers $1, 2, \ldots, N$ . For the subset $s$ , denote the regression matrix by $X_s$ and the dependent vector by $y_s$ , and the LSE by $\beta_s$ . Let $r$ denote summation over all subsets of size $r$ .

Theorem 1:

For any $r \geq p$ ,

$$
\begin{array}{r l} & {\beta = \Sigma_ {r} | \mathbf {X} _ {s} ^ {T} \mathbf {X} _ {s} | \beta_ {s} / \Sigma | \mathbf {X} _ {s} ^ {T} \mathbf {X} _ {s} |} \\ & {\quad = \Sigma_ {r} | \mathbf {X} _ {s} ^ {T} \mathbf {X} _ {s} | \beta_ {s} / _ {n - r} C _ {r - p} | \mathbf {X} ^ {T} \mathbf {X} |} \end{array}
$$

where $|X_{s}^{T}X_{s}|\beta_{s}$ is defined as zero for singular $X_{s}^{T}X_{s}$ . This is a well-known theorem; for proof and further elaboration see [12].

Theorem 1 suggests that one can consistently and without bias estimate the ULSE $\beta$ obtained from subsets $s_{1}, s_{2}, \ldots, s_{J}$ of the database; each is of size r drawn randomly without replacement. The estimate of $\beta$ is the weighted average,

$$
b _ {J} = \Sigma_ {j} w _ {s (j)} \beta_ {s (j)}\tag{4}
$$

$w_{s}$ is proportional to $|\mathbf{X}_s^T\mathbf{X}_s|$

$$
\Sigma_ {j} w _ {s (j)} = 1
$$

$$
\text { for } j = 1, 2, \dots , J
$$

Since each jackknifed sample is drawn randomly from all subsets of size r with equal probability, the expected value of $\beta_{s(j)}$ is $\beta$ , thus the expected value of $\beta_{J}$ is also $\beta$ . It follows from Slutsky's Lemma [3] that $\beta_{J}$ converges with probability one to $\beta$ as J converges to $_{n}C_{r}$ . We call this estimator the sampled-general weighted jackknife.

The number of subsets, J, required to come within an acceptable error of the estimator ULSE $\beta$ , which is based on the database, depends on how widely variable the $\beta_{s(j)}$ 's are over sampled subsets of size r. This information could be gathered incrementally by the database administrator as the number of sampled subsets is increased and used in the usual manner for estimating the number of jackknifed samples for achieving a certain level of accuracy. However it would be difficult for a snooper to achieve a greater accuracy than intended by the database manager through repeated queries, since as shown in (4), determining the value of $\beta_{J}$ requires the exact value of the weights $w_{s}$ 's and these are not available to the snooper.

## 3.2. Implementation

Given a database of size N, two important implementation considerations are: the appropriate subsets size, r; and the appropriate number of these subsets, J, that should be used to satisfy the query. According to Wu [12], a recommended value for r is given by

$$
r = \frac {(N + a - 1)}{2}\tag{5}
$$

where a is the rank of X in the regression model. A value of r around 0.72N possesses a desirable second-order asymptotic property [12].

The detailed implementation of the proposed method is as follows.

1. Determine the query set that satisfies the characteristic formula, C. Let N be the size of the database (or a subset containing the query set) and determine r accordingly.

2. Select randomly $J$ subsets $s_1, s_2, \ldots, s_J$ of size $r$ each from the entire database. For each subset $s_j$ compute the corresponding LSE $\beta_{s(j)}$ using $\mathbf{y}_{s(j)}$ and $\mathbf{X}_{s(j)}$ .

3. Compute the weighted average LSE $\beta_{J}$ using (4) and an estimate of the corresponding variance,

$$
\mathbf {V} _ {J r} (\beta) = \binom{n - a}{r - a + 1} ^ {- 1} | \mathbf {X} ^ {T} \mathbf {X} | ^ {- 1} \Sigma_ {j} w _ {s (j)} \left(\beta_ {s (j)} - \beta\right) \left(\beta_ {s (j)}\right) ^ {- 1}\tag{6}
$$

4. Deliver $\beta_{J}$ and $\mathbf{V}_{Jr}$ .

## 4. An Output Perturbation Approach Based on the Random Sample Queries Method

## 4.1. Extending the Random Sample Queries Method

Denning's original method [5] consists of randomly sampling, without replacement, records from the query set. Then the sample mean and variance of $y$ in the sample is reported to the user. The random sampling is implemented by sequentially selecting a record for the sample with probability $p$ .

To incorporate Denning's perturbation plan into our coding scheme, we would randomly sample, without replacement, from the entire database or a subset containing the query set. The subset should be chosen to be large. Then sampling would be repeated $D$ times to obtain $D$ independent samples. Then we would proceed to encode the sample with a model conforming to equation (2). We note that Denning explicitly recommended the random sample query over sampling the entire database in order to reduce the cost of implementation. However, when the query set is small the random sample queries method has a higher chance of being compromised, because $p$ must be taken large to ensure an acceptably small error of the reported statistic. Moreover, by sampling the entire database, the random sample queries method is more fairly compared to our jackknife method. We will call our modification of Denning's method the modified random sampling queries method.

## 4.2. Implementation

Given a database of size N, the important implementation consideration is the choice of p that should be used to satisfy the query. According to Denning [5], a recommended value for p when the sampled set is large can be as large as 0.9375 and avoid compromise by trackers, provided that the database size is at least 20,000 records. However, should the query set be small, a p of 0.9375 may be too large.

The detailed implementation of the proposed method is as follows.

1. Determine the query set that satisfies the characteristic formula, C. Let N be the size of the database (or a subset containing the query set) and determine p accordingly.

2. Select randomly records with probability $p$ from the entire database. Repeat this $D$ times to form $D$ independent samples $(s_1, \ldots, s_D)$ . The expected number of records in each sample will be $Np$ . For each sample $s_j$ compute the corresponding LSE $\beta_{s(j)}$ using $\mathbf{y}_{s(j)}$ and $\mathbf{X}_{s(j)}$ .

3. Compute the average LSE $\beta_{D}$ using (4) with weights $w_{s(j)}$ determined from the above $\mathbf{X}_{s(j)}$ .

4. Compute an estimate of the corresponding variance,

$$
\mathbf {V} _ {D p} (\beta) = \Sigma_ {j} w _ {s (j)} (\beta_ {s (j)} - \beta) (\beta s _ {(j)} - \beta) ^ {- 1} \tag {7}
$$

5. Deliver $\beta_{D}$ and $\mathbf{V}_{Dp}$ .

## 5. Comparison between the Two Schemes

LISTED BELOW ARE A FEW COMMENTS ABOUT both output perturbation methods considered in this article. We refer the reader to our simulation results for a rigorous comparison between these and other resampling plans [1]. Most of our comments here point out some advantages and disadvantages of the two methods.

1. When $D = 1$ , our extension almost corresponds to the original random sample queries method.

2. The modified random sample queries method with D = 1 could be compromised by a tracker using averages over queries that could produce independent responses (i.e., estimates) of the same attribute average.

3. A theoretical lower bound to the confidence interval a tracker could obtain with repeated queries of the Denning extension can be controlled by the database manager through the choice of D (greater than one). (We mentioned this possibility with the jackknife as well.)

4. The modified random sample queries method may be easier to implement than the jackknife, since the process of randomly selecting jackknifed samples is cumbersome.

5. Both methods will produce unbiased query responses, but the jackknife may produce a better estimate of standard error for equal sample sizes.

6. None of these methods requires assumptions or tests for our models to fit, since our models are “over-fitted” and serve only to recode the data and act as a vehicle for Theorem 1.

## 6. Conclusion

WE HAVE PRESENTED A NEW SECURITY CONTROL METHOD that is based on a recoding of the data and the jackknifing concept. We also presented a modification to the random sample queries method. One of the advantages of these methods is that they provide the legitimate user with extremely good estimates while at the same time severely limiting the success of a snooper in any attempt to compromise the database.

## ACKNOWLEDGEMENTS

The research of Douglas H. Jones was partially supported by the Cognitive Science Program, Office of Naval Research; the Faculty Academic Study Program, Rutgers University; and the Research Council, Graduate School of Management, Rutgers University.

## REFERENCES

1. Adam, N. R., and Jones, D. H. Statistical databases: Perturbation using bootstrap resampling plan. Tech. Report, Grad. Sch. Mngmt., Rutgers U., Newark, NJ (1989).

2. Adam, N. R., and Wortmann, J. C. Secure dynamic statistical database: comparison of methods. ACM Computing Surveys (September 1989).

3. Chung, K. L. A Course in Probability Theory. New York: Academic Press (1974).

4. Denning, D. E. Cryptography and Data Security. Reading, MA: Addison-Wesley, 1982.

5. Denning, D. E. Secure statistical database with random sample queries. ACM Trans.

6. Denning, D. E., and Schlörer, J. Inference control for statistical databases. Computer Journal, 16, 7 (July 1983), 79–82.

7. Efron, B. The Jackknife, the Bootstrap and Other Resampling Plans. Philadelphia: SIAM, 1982.

8. Matloff, N. E. Another look at the use of noise addition for database security. Proceedings of IEEE Symposium on Security and Privacy (1986), 173–180.

9. Palley, M. A. Security of Statistical Databases Compromise through Attribute Correlational Modeling. Proceedings of IEEE Conference on Data Engineering (1986), 67–74.

10. Palley, M. A., and Simonoff, J. S. The use of regression methodology for compromise of confidential information in statistical databases. ACM Trans. Database Sys., 12, 4 (December 1987), 593–608.

11. Tukey, J. Bias and confidence in not quite large samples (abstract). Annual Math. Statist. (1958), 29.

12. Wu, C. F. J. Resampling inference in regression. The Annals of Statistics, 14, 4 (1986), 1261–1350.
