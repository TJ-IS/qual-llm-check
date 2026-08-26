---
otero_id: 10138
otero_key: "6PXE2U7C"
title: "Entity matching in heterogeneous databases: A logistic regression approach"
authors: "Debabrata Dey"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.10.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Entity matching in heterogeneous databases: A logistic regression approach

Debabrata Dey

Michael G. Foster School of Business, University of Washington, Seattle, WA 98195-3200, United States

Received 5 October 2006; received in revised form 14 September 2007; accepted 4 October 2007 Available online 18 October 2007

## Abstract

This paper examines a widely-encountered data heterogeneity problems—often faced in real-world decision support situations— called the entity heterogeneity problem, which arises when the same real-world entity type is represented using different identifiers in different applications. Supporting real-world decisions often requires one to identify which entity in one application is the same as another in a second application. Previous research has proposed decision models to resolve this problem. However, the implementation of those models requires either the estimation of probability parameters by manually matching a large sample of the existing data or the estimation of a distance measure based on user-specified weights. This paper proposes an alternative technique based on logistic regression for estimating the matching probabilities to be used in the matching decision model. This approach has been implemented and tested on real-world data. Comparison of the results with those from earlier approaches indicate that the proposed approach performs quite well and is certainly a viable approach in practical situations. © 2007 Elsevier B.V. All rights reserved.

## 1. Introduction

In order to provide efficient and effective support for real-world decisions, it is often necessary to consolidate information contained in several heterogeneous data sources [3,12]. To that end, it is necessary to resolve several types of heterogeneity that may exist across different data sources [9,11].

In the recent years, one such widely-encountered data heterogeneity problem—called the entity heterogeneity problem—has received a lot of attention in the literature [2,4,5,6,7,10,13]. The entity heterogeneity problem arises when the same real-world entity type is represented using different identifiers in different applications. For example, an employee may be uniquely identified using the social security number (SSN) in a payroll application and by an EMP-ID in a project management application. Similarly, different identifiers may be used to identify the same customer by different organizations, or even by different departments within the same organization. To support a decision problem it may often be necessary to ascertain whether an entity instance in one application is the same as an instance in another application. However, in the absence of a common identifier, it is difficult to do so. It is, of course, possible to use the common attributes for this purpose. However, because of the existence of data entry errors, time-related changes, and systematic data transformations, often a perfect match on the common attributes may not be found, even when the underlying entity instances are the same in the real world.

In an earlier work, Dey et al. [5] proposed a decision model where the uncertainty about the matching of two entities was represented using the probability of a match. Implementation of their model requires that the probability parameters are accurately estimated. They use a naïve Bayesian approach for estimating the probability parameters. If manually-matched training data are available, this approach can be implemented in a relatively straightforward manner; in that case, the model is shown to perform quite well. However, in many realworld situations, manually-matched training data are not always available. Generating such manually-matched data is quite time-consuming, especially if one considers a sufficiently large data set to ensure the accuracy of the probability parameters. Furthermore, the information overload associated with the matching process could eventually lead to error in judgment. For example, when asked to manually match just 100 entities each from two databases, an expert must make 100 ×100 =10,000 comparisons—an extremely time-consuming task, with a high amount of information overload.

In order to overcome this problem of the lack of manually-matched data, Dey et al. [6] adopted a distance-based measure to express the similarity between two entity instances and then employed this measure in a decision-theoretic setting. There, distance between two entity instances is expressed as a weighted sum of the distances between their attribute values. The weights in the distance function parameterize the predictive power of the attributes in terms of whether the entity instances indeed match or not, and should be elicited from domain experts. These distances are then used in a simple decision model for matching. Although their experimental results indicate that this is a viable approach, there are several problems with the distancebased approach. First, eliciting the weights (representing the predictive power) of the attributes from users is not an easy task. In fact, Dey et al. [6] resorted to eliciting the ranks of the attributes from users; these ranks were then converted to weights for the attributes. It is not clear if the actual predictive power of an attribute is captured well in its relative rank. Second, the similarity between two entity instances is not necessarily a linear combination of the distances between their attribute values. When this similarity is expressed as the probability of a match and estimated using the naïve Bayesian approach, the non-linearity is easily captured. However, this non-linearity is completely ignored in the linear distance function adopted in [6]. Consequently, the results from the distance-based approach could be quite sensitive to the cost parameters of the model.

This paper presents another approach to solve the entity heterogeneity problem in the absence of training data, by making use of the logistic regression technique [8,10] to obtain the probabilities required in the decision model. The data required to perform the logistic regression can be easily obtained from users or domain experts. This technique has been implemented and tested on real-world data. Comparison of the results obtained this way with those from the earlier approaches clearly indicates the viability of the proposed approach in practice.

The rest of the paper is organized as follows. Section 2 reviews the matching decision model developed in prior research. In Section 3, the logistic regression approach to probability estimation is described. Section 4 discusses the implementation of the model and its testing on real-world data. Section 5 concludes the paper and provides directions for future research.

## 2. The matching model and previous research

This section describes the entity matching decision model developed in [5,6]. First a few notations are necessary.

Let $D _ { 1 }$ and $D _ { 2 }$ be two databases. Further, let $R _ { 1 } \in D _ { 1 }$ and $R _ { 2 } \in D _ { 2 }$ be two relations representing the same realworld entity type, which do not share a common identifier. Let $R _ { 1 } { = } \{ a _ { 1 } , a _ { 2 } { , } . . . , a _ { m } \}$ , and $R _ { 2 } = \{ b _ { 1 } , b _ { 2 } , . . . ,$ $\left. b _ { n } \right\}$ . Consider two records $a _ { i } \in R _ { 1 }$ and $b _ { j } \in R _ { 2 } ;$ in order to verify whether they represent the same real-world entity instance (denoted $a _ { i } = \mathrm { b j } )$ ), consider a set of attributes $Y { = } \left\{ Y _ { 1 } , \ Y _ { 2 } { , } { \ldots } , \ Y _ { K } \right\}$ common to both $R _ { 1 }$ and $R _ { 2 }$ The comparison results between $a _ { i }$ and $b _ { j } ,$ as well as their common attributes, respectively, can be expressed as the following random variables:

$$
M _ {\mathrm{ij}} = \left\{ \begin{array}{l l} 1, & \text { if   } a _ {i} \simeq b _ {j}, \\ 0, & \text { otherwise }, \end{array} \right. \quad \text { and }
$$

$$
U _ {\mathrm{ijk}} = \left\{ \begin{array}{l l} 1, & \text {   if   } a _ {i} \left(Y _ {k}\right), \\ 0, & \text {   otherwise }, \end{array} \right. \quad k \in \{1, 2, \ldots , K \},
$$

where $r ( Y _ { k } )$ denotes the $Y _ { k }$ value of any record $r .$ Note that, although $U _ { \mathrm { i j k } }$ is represented as a binary-valued random variable here, it is straightforward to extend this idea to the case where $U _ { \mathrm { i j k } }$ can assume more than two values. The possible match between $a _ { i }$ and $b _ { j }$ is quantified by a probability $p _ { i j }$ that denotes the conditional probability that $a _ { i }$ and $b _ { j }$ refer to the same realworld entity instance, given the matching pattern of their recorded attribute values:

$$
p _ {\mathrm{ij}} = \operatorname * {P r} \left[ M _ {\mathrm{ij}} = 1 \mid U _ {\mathrm{ij} 1}, U _ {\mathrm{ij} 2}, \dots , U _ {\mathrm{ijK}} \right]
$$

Now consider the case of testing a possible match between $a _ { i }$ and $b _ { j } \mathrm { ~ . ~ I f } a _ { i } { \backsimeq } b _ { j }$ in reality and are matched, or if $a _ { i } \not = b _ { j }$ in reality and are not matched, then there is no error. However, if $a _ { i } { = } b _ { j }$ in reality, and one fails to match them, a type-I error is committed; let $c _ { 1 }$ denote the cost (to the decision maker) for this error. Similarly, a type-II error occurs when $a _ { i } \not = b _ { j }$ in reality, but are matched; let $c _ { 2 }$ denote the associated cost. Based on these notations, Dey et al. [5] defined the following decision variables:

$$
X _ {\mathrm{ij}} = \left\{ \begin{array}{l l} 1, & \text { if } a _ {i} \in R _ {1} \text { is   matched   with } b _ {j} \in R _ {2}, \\ 0, & \text { otherwise }, \end{array} \right.
$$

and developed a decision model based on the minimization of the total error cost:

$$
\begin{array}{l l} (P) & \max _ {X} \qquad \sum_ {t = 1} ^ {m} \sum_ {j = 1} ^ {n} \left(p _ {\mathrm{ij}} - \alpha\right) X _ {\mathrm{ij}} \\ & \text { s.t. } \qquad \sum_ {t = 1} ^ {m} X _ {\mathrm{ij}} \leq 1, \quad \forall j \in \{1, 2, \ldots m \}, \\ & \sum_ {j = 1} ^ {n} X _ {\mathrm{ij}} \leq 1, \quad \forall i \in \{1, 2, \ldots m \}, \\ & X _ {\mathrm{ij}} \not \in \{0, 1 \}, \quad \forall i \in \{1, 2, \ldots , m \}, \\ & \forall j \in \{1, 2, \ldots n \}, \end{array}
$$

where, α is the relative cost of type-II error; i.e., $\scriptstyle { \alpha = c _ { 2 } } /$ $( c _ { 1 } + c _ { 2 } )$

In order to implement this model, it is necessary to estimate the matching probabilities, $p _ { \mathrm { i j } } , i \in \{ 1 , 2 , \dotsc m \}$ $j \in \{ 1 , 2 , . . . , n \}$ . Dey et al. [5] used a naïve Bayesian approach (of conditional independence of the $\mathrm { U _ { i j k } } ^ { \mathbf { \hat { s } } }$ given $M _ { \mathrm { i j } } )$ and expressed the probability term as:

$$
p _ {\mathrm{ij}} = \left(1 + \frac {1 - \pi}{\pi} \prod_ {k = 1} ^ {K} \frac {\operatorname* {P r} | U _ {\mathrm{ijk}} | M _ {\mathrm{ij}} = 0}{\operatorname* {P r} | U _ {\mathrm{ijk}} | M _ {\mathrm{ij}} = 1}\right) ^ {- 1},\tag{1}
$$

where $\pi$ is prior probability of a match between any two records, one from $R _ { 1 }$ and the other from $R _ { 2 } .$ . The parameters needed for this estimation are: π, $\mathrm { P r } [ U _ { \mathrm { i j k } } | M _ { \mathrm { i j } } = 0 ]$ , and Pr $[ U _ { \mathrm { i j k } } | M _ { \mathrm { i j } } = 1 ]$ . These parameters can be easily estimated if manually matched training data are available.

In order to extend this model to situations where the training data are not available, Dey et al. [6] proposed a distance-based measure. They defined $\overline { { d } } _ { \mathrm { i j } }$ as the expected distance between $a _ { i }$ and b on a 0–1 scale based on their recorded attribute values and approximated the probability of a match as $p _ { \operatorname { i j } } \ l _ { 1 } - 1 - { \overline { { d } } } _ { \operatorname { i j } } .$ In order to calculate the expected distance $\boldsymbol { \overline { { d } } } _ { \mathrm { i j } }$ between the entities $a _ { i }$ and $b _ { j } ,$ Dey et al. [6] considered the distance between each of their common attributes. Let $d _ { \mathrm { i j k } } { = } d ( a _ { i } ( Y _ { k } ) , b _ { j } ( Y _ { k } ) )$ denote the distance, normalized on a 0–1 scale, between the observed $Y _ { k ^ { - } }$ values of $\dot { a } _ { i }$ and b . The expected distance between $\mathrm { a } _ { \mathrm { i } }$ and $\mathsf { b } _ { \mathrm { j } }$ was expressed in [6] as a weighted average of the distances between individual attribute values:

$$
\overline {{{d}}} _ {\mathrm{ij}} = \sum_ {k = 1} ^ {K} w _ {k} d _ {\mathrm{ijk}}, \text {   where   } \sum_ {k = 1} ^ {K} w _ {k} = 1\tag{2}
$$

The weight $w _ { k }$ denotes the relative importance or predictive power of $Y _ { k } , k { = } 1 , 2 { , } . . . , K$ . In the absence of training data, Dey et al. [6] resorted to obtaining these weights from users familiar with the application context. Since it is difficult for users to explicitly state the weights for the attributes, in those experiments, the users were asked to rank order the attributes according to their predictive power. These ranks are then consolidated and converted to the weights for these attributes. Their results show that this approach works well, especially when the type-I and type-II costs are similar, i.e., α is close to 0.5.

## 3. The proposed approach

This section proposes the logistic regression approach for estimating the probabilities. These probabilities can then be used in decision model (P) to perform entity matching. In this approach, the logit of the probability (of a match) is expressed as a linear combination of the independent variables $U _ { \mathrm { i j k } } \left[ 8 , 1 0 \right]$

$$
\log \left(\frac {p _ {\mathrm{ij}}}{1 - p _ {i j}}\right) = B _ {0} + \sum_ {k = 1} ^ {K} B _ {k} U _ {\mathrm{ijk}}
$$

where $B _ { k } , k { = } 0 , 1 , 2 { , } { \ldots } , K .$ , are the coefficients of regression. Once these coefficients are estimated, one can easily estimate the probability of a match between two records based on the matching pattern of their common attribute values [8]:

$$
\begin{array}{l} p _ {\mathrm{ij}} = \frac {1}{1 + \exp (- G _ {\mathrm{ij}})}, \text {   where   } \\ G _ {\mathrm{ij}} = B _ {0} + \sum_ {k = 1} ^ {K} B _ {k} U _ {\mathrm{ijk}} \end{array}\tag{3}
$$

Therefore, the challenge in implementing this approach lies in the estimation of the regression coefficients. When manually-matched training data are available, this estimation is quite straight-forward, since complete information is available about the comparison results between records from the matched training portions of the two relations. In other words, one knows $\mathrm { U _ { i j k } }$ and $M _ { \mathrm { i j } } -$ values for all $a _ { i } \in \hat { R } _ { I } , b \in \hat { R } _ { 2 }$ , and $k { = } 1 , 2 { \mathrm { , . . . , } } K$ , where $\hat { R } _ { 1 }$ and $\hat { R } _ { 2 }$ are the training portions of the relations $R _ { 1 }$ and $R _ { 2 } ,$ respectively. Given a value of B, the vector of regression coefficients, one can estimate, for every comparison $( i , j ) ,$ , the probability $p _ { \mathrm { i j } }$ from Eq. (3), and hence the likelihood measure $( \dot { p _ { \mathrm { i j } } } ) ^ { \dot { M _ { \mathrm { i j } } } } ( 1 - p _ { \mathrm { i j } } ) ^ { 1 \dot { - } \dot { M _ { \mathrm { i j } } } }$ . Since the likelihood function is a product of the individual likelihood measures of all the comparisons, the likelihood function can be expressed as:

$$
l (\mathbf {B}) = \prod_ {i = 1} ^ {| \hat {R} _ {1} |} \prod_ {j = 1} ^ {| \hat {R} _ {2} |} \left(p _ {\mathrm{ij}}\right) ^ {M _ {\mathrm{ij}}} \left(1 - p _ {\mathrm{ij}}\right) ^ {1 - M _ {\mathrm{ij}}}.\tag{4}
$$

The maximum likelihood fit can then be obtained by finding a value of B such that l(B) is maximized [8]. The maximization procedure is iterative and is supported by most statistical and data mining software tools.

Of course, the focus of this paper is the situation where manually-matched training data are not available. As a result, the above procedure cannot be implemented directly, and one must rely on input from users knowledgeable about the application context to develop a sense of how matching patterns of attributes correspond to the eventual matching of records. In order to obtain such input from the user, one could consider every possible realization of the matching pattern $U _ { \mathrm { i j } } .$ Since $U _ { \mathrm { i j k } } { } ^ { \prime } s$ are assumed to be binary-valued, there can clearly be $2 ^ { K }$ possible realizations. After presenting each of these $2 ^ { \bar { K } }$ realizations to a user, (s)he can be asked pass a judgment, based on his (her) knowledge of the application context, as to whether each realization leads to a match or not. Once the users' input is coded, we could run it in a standard software package to obtain the regression coefficients in a manner described above.

There are three main problems in implementing this scheme: (i) K could be large, (ii) some of the configurations could be impossible, and (iii) there may be some conflicts across users' judgment about matching entities. Each of these problems are described below along with how they can be remedied in practice.

## 3.1. Large K

It is clear that the number of possible realizations grows exponentially with K. As a result, if K is large, then the users would have to work with a large number of realizations. While this may still be better than the users having to work with matching the training data manually for $| R _ { 1 } | \times | R _ { 2 } |$ possible realizations, it would be preferable to ease the burden on the user. This can be done in several ways. First, the users can be asked to identify common attributes that shed little light on the eventual matching; these non-informative attributes can be eliminated, thereby making K effectively smaller. Furthermore, the users should be encouraged to establish possible matching rules involving some of the predictive attributes. For configurations that abide by these rules, the matching decision can be set automatically using the rules. Only the remaining configurations would then require direct input from the users.

## 3.2. Impossible configurations

Since we start with an exhaustive list of all possible configurations, it is quite likely that many of them are not possible in reality. This is because the attributes are likely to have some dependency on one another and certain combinations could be either impossible or extremely rare. The inclusion of these combinations would not only make it difficult for the user to pass accurate estimates of a match, but could also introduce unnecessary bias into the logistic regression model. In order to address this, the users should be requested to develop rules for impossible configurations, based on their knowledge of these dependencies. Once these rules are identified, they can be used to prune out the impossible configurations, thereby reducing the total number of configurations requiring direct user input, as well. One could also use a data-driven approach to identify and eliminate the impossible configurations. This can be done by examining $U _ { \mathrm { i j } }$ from the actual data and identifying those values that are never realized. Of course, the data driven-approach should be adopted only when the data set is reasonably large, and valid configurations are not eliminated unnecessarily.

## 3.3. Conflicts in user input

It is always better to get the input from several users so that individual bias can be reduced as much as possible. However, when there are several users, it is quite possible that not all of them will treat every configuration the same way. As a result, some configurations may be labeled as a “match” by some users and as a “non-match” by others. In addition, some users may not be able to make a clear decision about some configurations. In order to resolve this type of conflict, one could resort to a vote across users and the majority decision could be implemented.

## 4. Implementation and testing

This section describes the implementation of the model and its testing with real data. It also provides comparison with the earlier approaches.

## 4.1. Description of the data

The testing was performed on the same MIS faculty directory database that was also used in [5,6]. Two versions of the database were used—the 1996 version $( R _ { 9 6 } )$ and the 1992 version $( R _ { 9 2 } )$ . There were 17 common attributes between these two versions; these attributes furnished information on a faculty member's name (2 attributes), affiliation (6 attributes), last degree (4 attributes), and research interests (5 attributes representing the IFIP TC8 Working Groups). Two of these attributes were integers, 5 were logical, and the remaining 10 were character strings, with the size varying from 14 to 70 characters.

Records from each of the two relations, $R _ { 9 2 }$ and $R _ { 9 6 } ,$ were assigned to four sets of records: I, II, III, and IV. The assignment of faculty records to different sets was done in the following manner. For set IV, a few states were randomly selected and all faculty members from those states were included in that set. States included in set III were chosen as a random subset of states in set IV, states in set II as a random subset of states in set III, and states in set I as a random subset of states in set II. The composition of these subsets and the number of true matches (identified through manual matching) for each subset are shown in Table 1.

## 4.2. Elicitation of user input and estimation of coefficients

Although there were 17 common attributes, the 5 users who provided input to the logistic regression models were unanimous that the last 5 attributes (representing the IFIP TC8 Working Groups) provided little information about the eventual matching. After dropping these attributes, we were left with 12 attributes that resulted in $2 ^ { 1 2 } { = } 4 0 9 6$ configurations. The users were then encouraged to develop rules describing “impossible” configurations. The users agreed on only two rules:

Table 1  
Data sets used for entity matching

<table><tr><td rowspan="2">Data set</td><td rowspan="2">States included</td><td colspan="2">No. of records</td><td rowspan="2">No. of true matches</td></tr><tr><td> $R_{92}$ </td><td> $R_{96}$ </td></tr><tr><td>I</td><td>{WA, NJ, OK}</td><td>65</td><td>75</td><td>45</td></tr><tr><td>II</td><td>{WA, NJ, OK, WI, ID, NH}</td><td>127</td><td>135</td><td>84</td></tr><tr><td>III</td><td>{WA, NJ, OK, WI, ID, NH, GA, AL}</td><td>228</td><td>262</td><td>155</td></tr><tr><td>IV</td><td>{WA, NJ, OK, WI, ID, NH, GA, AL,VA, ME, DC, MI, PA, IL}</td><td>543</td><td>598</td><td>365</td></tr></table>

• If there is a match in the EMail Address, then there cannot be a mismatch in both First and Last Names.

• If there is a mismatch in the Institution Name, then there cannot be a match in the Work Phone.

These two rules were applied to prune out a total of 1408 configurations as impossible. The users were then requested to develop possible matching rules. A total of 13 rules were agreed upon by all the users. Examples of matching rules include:

• A match in the EMail Address implies an entity instance match,

• A match in both the First and Last Names implies an entity instance match.

• A mismatch in both the First and Last Names implies an entity instance mismatch.

Application of these 13 rules led to automated decisions in 2368 cases. Therefore, in the end, the users were left with only 320 configurations on which they were asked to make matching decisions from three possible choices:

• 1, if the user felt that the two records represent the same faculty member.

• 0, if the user felt that the two records represent two different faculty members.

• No decision, if the user could not make up his (her) mind about the above two choices.

The users' input were consolidated into a single data set after removing all the rows that were marked as “no decision” by users; any time there was a disagreement among users, the majority decision was chosen to be the actual decision, with ties broken randomly. In the end, there were 2688 rows of comparison data that were used for finding the regression coefficients. In order to assess the goodness of the fit, we used two well-known tests: the likelihood-ratio test and the Hosmer-Lemeshow test [1,8]. For the first test, the likelihood-ratio statistic, which follows a $\chi ^ { 2 }$ distribution with 12−1=11 degrees of freedom, was estimated. It is 1754.36, much bigger than the tabulated value of $\chi _ { 1 1 ; 0 . 0 0 1 } ^ { 2 } = 3 1 . 2 6$ . The fit is, therefore, considered to be excellent. The Hosmer-Lemeshow goodness-of-fit statistic (with 8 groups) was estimated as 2.47 with a p-value of 0.8713, implying an excellent fit, once again.

Table 2  
Number of errors in the logistic regression and distance function approaches

<table><tr><td>Data Set →</td><td colspan="3">Set I (4875 comparisons, 45 true matches)</td><td colspan="3">Set II (17145 comparisons, 84 true matches)</td><td colspan="3">Set III (59736 comparisons, 155 true matches)</td><td colspan="3">Set IV (324714 comparisons, 365 true matches)</td></tr><tr><td>Approach ↓</td><td>α</td><td>Type-I</td><td>Type-II</td><td>α</td><td>Type-I</td><td>Type-II</td><td>α</td><td>Type-I</td><td>Type-II</td><td>α</td><td>Type-I</td><td>Type-II</td></tr><tr><td rowspan="9">Logistic regression</td><td>0.1</td><td>0</td><td>0</td><td>0.1</td><td>0</td><td>0</td><td>0.1</td><td>0</td><td>0</td><td>0.1</td><td>1</td><td>0</td></tr><tr><td>0.2</td><td>0</td><td>0</td><td>0.2</td><td>0</td><td>0</td><td>0.2</td><td>0</td><td>0</td><td>0.2</td><td>1</td><td>0</td></tr><tr><td>0.3</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>0</td><td>0.3</td><td>1</td><td>0</td></tr><tr><td>0.4</td><td>0</td><td>0</td><td>0.4</td><td>0</td><td>0</td><td>0.4</td><td>0</td><td>0</td><td>0.4</td><td>1</td><td>0</td></tr><tr><td>0.5</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0.5</td><td>1</td><td>0</td><td>0.5</td><td>2</td><td>0</td></tr><tr><td>0.6</td><td>0</td><td>0</td><td>0.6</td><td>0</td><td>0</td><td>0.6</td><td>1</td><td>0</td><td>0.6</td><td>2</td><td>0</td></tr><tr><td>0.7</td><td>0</td><td>0</td><td>0.7</td><td>0</td><td>0</td><td>0.7</td><td>1</td><td>0</td><td>0.7</td><td>2</td><td>0</td></tr><tr><td>0.8</td><td>0</td><td>0</td><td>0.8</td><td>0</td><td>0</td><td>0.8</td><td>1</td><td>0</td><td>0.8</td><td>2</td><td>0</td></tr><tr><td>0.9</td><td>0</td><td>0</td><td>0.9</td><td>0</td><td>0</td><td>0.9</td><td>1</td><td>0</td><td>0.9</td><td>2</td><td>0</td></tr><tr><td rowspan="9">Naïve Bayeyesian</td><td>0.1</td><td>0</td><td>20</td><td>0.1</td><td>0</td><td>43</td><td>0.1</td><td>0</td><td>73</td><td>0.1</td><td>0</td><td>178</td></tr><tr><td>0.2</td><td>0</td><td>20</td><td>0.2</td><td>0</td><td>40</td><td>0.2</td><td>0</td><td>73</td><td>0.2</td><td>0</td><td>178</td></tr><tr><td>0.3</td><td>0</td><td>10</td><td>0.3</td><td>0</td><td>22</td><td>0.3</td><td>0</td><td>43</td><td>0.3</td><td>0</td><td>121</td></tr><tr><td>0.4</td><td>0</td><td>2</td><td>0.4</td><td>0</td><td>2</td><td>0.4</td><td>0</td><td>7</td><td>0.4</td><td>0</td><td>18</td></tr><tr><td>0.5</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td>0.6</td><td>0</td><td>0</td><td>0.6</td><td>0</td><td>0</td><td>0.6</td><td>1</td><td>0</td><td>0.6</td><td>2</td><td>0</td></tr><tr><td>0.7</td><td>1</td><td>0</td><td>0.7</td><td>1</td><td>0</td><td>0.7</td><td>3</td><td>0</td><td>0.7</td><td>11</td><td>0</td></tr><tr><td>0.8</td><td>8</td><td>0</td><td>0.8</td><td>8</td><td>0</td><td>0.8</td><td>12</td><td>0</td><td>0.8</td><td>34</td><td>0</td></tr><tr><td>0.9</td><td>23</td><td>0</td><td>0.9</td><td>30</td><td>0</td><td>0.9</td><td>60</td><td>0</td><td>0.9</td><td>157</td><td>0</td></tr></table>

## 4.3. Experimental results and comparison

The regression coefficients were used to obtain the matching probabilities from Eq. (3), for each of the data sets. These probabilities were then used in decision model (P) described in Section 2 to obtain the matching decisions which were compared to the actual matching to obtain the accuracy of the approach. These results are summarized in Table 2. For the sake of comparison, Table 2 also provides the results from the distance function approach [6] with the 12 attributes used in this paper.

Table 3  
Number of errors in the logistic regression and naïve Bayesian approaches

<table><tr><td>Data set →</td><td colspan="3">Set I (4875 comparisons, 45 true matches)</td><td colspan="3">Set II (17145 comparisons, 84 true matches)</td><td colspan="3">Set III (59736 comparisons, 155 true matches)</td><td colspan="3">Set IV (324714 comparisons, 365 true matches)</td></tr><tr><td>Approach ↓</td><td>α</td><td>Type-I</td><td>Type-II</td><td>α</td><td>Type-I</td><td>Type-II</td><td>α</td><td>Type-I</td><td>Type-II</td><td>α</td><td>Type-I</td><td>Type-II</td></tr><tr><td rowspan="9">Logistic regression</td><td>0.1</td><td>0</td><td>0</td><td>0.1</td><td>0</td><td>0</td><td>0.1</td><td>0</td><td>0</td><td>0.1</td><td>1</td><td>0</td></tr><tr><td>0.2</td><td>0</td><td>0</td><td>0.2</td><td>0</td><td>0</td><td>0.2</td><td>0</td><td>0</td><td>0.2</td><td>0</td><td>0</td></tr><tr><td>0.3</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>0</td></tr><tr><td>0.4</td><td>0</td><td>0</td><td>0.4</td><td>0</td><td>0</td><td>0.4</td><td>0</td><td>0</td><td>0.4</td><td>0</td><td>0</td></tr><tr><td>0.5</td><td>0</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0.5</td><td>1</td><td>0</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td>0.6</td><td>0</td><td>0</td><td>0.6</td><td>0</td><td>0</td><td>0.6</td><td>1</td><td>0</td><td>0.6</td><td>0</td><td>0</td></tr><tr><td>0.7</td><td>0</td><td>0</td><td>0.7</td><td>0</td><td>0</td><td>0.7</td><td>1</td><td>0</td><td>0.7</td><td>0</td><td>0</td></tr><tr><td>0.8</td><td>0</td><td>0</td><td>0.8</td><td>0</td><td>0</td><td>0.8</td><td>1</td><td>0</td><td>0.8</td><td>0</td><td>0</td></tr><tr><td>0.9</td><td>0</td><td>0</td><td>0.9</td><td>0</td><td>0</td><td>0.9</td><td>1</td><td>0</td><td>0.9</td><td>0</td><td>0</td></tr><tr><td rowspan="9">Naïve Bayeyesian</td><td>0.1</td><td>3</td><td>6</td><td>0.1</td><td>6</td><td>10</td><td>0.1</td><td>8</td><td>20</td><td>0.1</td><td>6</td><td>28</td></tr><tr><td>0.2</td><td>1</td><td>3</td><td>0.2</td><td>6</td><td>10</td><td>0.2</td><td>8</td><td>17</td><td>0.2</td><td>4</td><td>21</td></tr><tr><td>0.3</td><td>0</td><td>1</td><td>0.3</td><td>6</td><td>10</td><td>0.3</td><td>6</td><td>14</td><td>0.3</td><td>5</td><td>20</td></tr><tr><td>0.4</td><td>0</td><td>1</td><td>0.4</td><td>6</td><td>10</td><td>0.4</td><td>6</td><td>13</td><td>0.4</td><td>5</td><td>20</td></tr><tr><td>0.5</td><td>0</td><td>1</td><td>0.5</td><td>2</td><td>5</td><td>0.5</td><td>3</td><td>10</td><td>0.5</td><td>3</td><td>14</td></tr><tr><td>0.6</td><td>0</td><td>1</td><td>0.6</td><td>4</td><td>7</td><td>0.6</td><td>6</td><td>13</td><td>0.6</td><td>5</td><td>16</td></tr><tr><td>0.7</td><td>0</td><td>1</td><td>0.7</td><td>0</td><td>3</td><td>0.7</td><td>0</td><td>4</td><td>0.7</td><td>0</td><td>7</td></tr><tr><td>0.8</td><td>0</td><td>1</td><td>0.8</td><td>4</td><td>6</td><td>0.8</td><td>6</td><td>10</td><td>0.8</td><td>5</td><td>11</td></tr><tr><td>0.9</td><td>0</td><td>0</td><td>0.9</td><td>0</td><td>2</td><td>0.9</td><td>0</td><td>3</td><td>0.9</td><td>1</td><td>6</td></tr></table>

Clearly, the logistic regression approach performs quite well with the data sets used in the experiments, both in an absolute sense as well as relative to the distance function approach. For example, for data set IV, 324714 (=543×598) comparisons were considered, and at most only two type-I and zero type-II errors were committed, for all values of $\alpha \in [ 0 . 1 , 0 . 9 ]$ , leading to an overall accuracy of 99.9994% or higher. For data sets I and II, no errors were committed, implying a 100% accuracy. These results are quite impressive. When compared to the distance function approach, the main advantage of the logistic regression approach seems to be the robustness of the latter with respect to changes in α. The distance function approach provides reasonably accurate results in the neighborhood of $\alpha = 0 . 5$ . However, as one considers extreme values of a, the number of type-I or type-II errors increases rapidly in the distance function approach. On the other hand, the number of errors in the logistic regression approach seem to remain low even for extreme values of α. This is really useful because, in practice, α can take any value in (0,1)—the higher the asymmetry between the costs of type-I and type-II error, the more extreme is the value of α. Furthermore, it may sometimes be difficult to obtain an accurate estimate of α. The robustness of the logistic regression approach would surely provide the user with a higher level of confidence when using this approach in practice.

## 4.4. Further testing with training data

The distinctly superior performance of the logistic regression approach over the distance function approach with the MIS faculty directory data led to further interest in the former approach. For example, a natural question arose as to how the logistic regression approach would perform if real training data were available and how it would compare with the naïve Bayesian approach used in [5]. In order to satisfy this curiosity, the training data set used in [5] was employed to fit a logistic regression model. Once again, to assess the goodness of the fit, the likelihood-ratio statistic was estimated to be 1023.60, much bigger than the tabulated value of $\chi _ { 1 1 ; 0 . 0 0 1 } ^ { 2 } = 3 1 . 2 6$ Also, the Hosmer-Lemeshow goodness-of-fit statistic (with 6 groups) was estimated as 0 with a p-value of 1. Both the tests clearly indicate an excellent fit.

The estimated regression coefficients were used to obtain the matching probabilities, which were then employed in decision model (P) to obtain the matching decisions. The final results are summarized in Table 3, along with the results from the naïve Bayesian approach [5] with the 12 attributes used in this paper.

The results with the real training data are even more compelling. The logistic regression approach had a perfect prediction for all values of a in all the four data sets. Although the naïve Bayesian approach had a reasonably high accuracy, its overall performance was significantly worse than that of the logistic regression approach.

Given the compelling nature of the results with the logistic regression approach, it is tempting to claim that it would work better than the other two approaches, in general. However, such a claim would be hasty without a more extensive testing of these approaches with different data sets from different application contexts. On the other hand, it is quite reasonable to claim that logistic regression is a viable approach and certainly a possible alternative to the other two approaches. Given a particular situation, one needs to evaluate it along with the other approaches to see which one suits the application the best.

## 5. Conclusions

In modern organizations, the issue of data heterogeneity is rapidly becoming a critical concern. A very common heterogeneity issue is that of entity heterogeneity, which arises from the disparity in representing the same real-world entity using different identifiers in different databases. Previous work [5,6] has developed a probabilitybased matching decision model and has proposed two different approaches for estimating the probabilities. This paper presents a third method of probability estimation based on the logistic regression approach. Based on testing of the approach on real-world data, it appears to be quite efficacious. Given the compelling nature of the results, it is reasonable to claim that this approach is a practical one and can be regarded as a serious alternative to the other two approaches. More extensive testing is desirable before generalized claims about superiority can be made. Such testing is beyond the scope of this paper and will be examined in future research.

## References

[1] A. Agresti, An Introduction to Categorical Data Analysis, 2nd. Ed.John Wiley & Sons, 2002.

[2] J. Bischoff, T. Alexander, Data Warehouse: Practical Advice from the Experts, Prentice-Hall, 1997.

[3] M.W. Bright, A.R. Hurson, S. Pakzad, Automated resolution of semantic heterogeneity in multidatabases, ACM Transactions on Database Systems 19 (2) (June 1994) 212–253.

[4] A.L.P. Chen, P.S.M. Tsai, J.L. Koh, Identifying object isomerism in multidatabase systems, Distributed and Parallel Databases 4 (2) (April 1996) 143–168.

[5] D. Dey, S. Sarkar, P. De, A probabilistic decision model for entity matching in heterogeneous databases, Management Science 44 (10) (1998) 1379–1395.

[6] D. Dey, S. Sarkar, P. De, A distance-based approach to entity reconciliation in heterogeneous databases, IEEE Transactions on Knowledge and Data Engineering 14 (3) (2002) 567–582.

[7] M.A. Hernandez, S.J. Stolfo, The merge/purge problem for large databases, Proceedings of the 1995 ACM SIGMOD Conference, May 1995, pp. 127–138, San Jose.

[8] D.W. Hosmer, S. Lemeshow, Applied Logistic Regression, John Wiley, 2000.

[9] W. Kim, J. Seo, Classifying schematic and data heterogeneity in multidatabase systems, IEEE Computer 24 (12) (December 1991) 12–18.

[10] J.C. Pinheiro, D.X. Sun, Methods for linking and mining massive heterogeneous databases, Proceedings of the Fourth International Conference on Knowledge Discovery and Data Mining (KDD-98), August 1998, pp. 309–313, New York, NY.

[11] A.P. Sheth, J.A. Larson, Federated database systems for managing distributed, heterogeneous, and autonomous data-

bases, ACM Computing Surveys 22 (3) (September 1990) 183–236.

[12] E. Stickel, A. Hunstock, A. Ortmann, J. Ortmann, Data sharing economics and requirements for integration tool design, Informative Sciences 19 (8) (August 1994) 629–642.

[13] Y.R. Wang, S. Madnick, The interdatabase instance identification problem in integrating autonomous systems, Proceedings of the Fifth International Conference on Data Engineering, February 1989, pp. 46–55, Los Angeles, CA.

Debabrata Dey is a Professor of Information Systems at the Michael G. Foster School of Business, University of Washington. His research interests are in studying business issues related to data warehousing, network pricing and performance, data uncertainty, and database design. His other interests include systems development, information security, and technology adoption and diffusion. His research has been published in Management Science, Operations Research, Information Systems Research, ACM Transactions on Database Systems, IEEE Transactions on Knowledge and Data Engineering, INFORMS Journal on Computing, and other journals and conference proceedings. He received his Ph.D. from the University of Rochester in 1994.
