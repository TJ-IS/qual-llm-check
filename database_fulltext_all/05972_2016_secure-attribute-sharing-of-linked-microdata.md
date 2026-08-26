---
otero_id: 5972
otero_key: "HGAZ2XDF"
title: "Secure attribute sharing of linked microdata"
authors: "Krishnamurty Muralidhar; Rathindra Sarathy; Han Li"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.10.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Secure attribute sharing of linked microdata

Krishnamurty Muralidhar <sup>a</sup>, Rathindra Sarathy <sup>b</sup>, Han Li <sup>c</sup>

<sup>a</sup> University of Oklahoma, United States

<sup>b</sup> Oklahoma State University, United States

<sup>c</sup> Minnesota State University Moorhead, United States

## a r t i c l e i n f o

Article history: Received 19 November 2014 Received in revised form 5 October 2015 Accepted 14 October 2015 Available online xxxx

Keywords: Secure attribute sharing Microdata Confidentiality Privacy-preserving data sharing

## a b s t r a c t

Two organizations that have records on the same collection of individuals can benefit from sharing attributes on these individuals. The combined data, with records linked on certain common identifying information, is termed linked microdata. Linked microdata attributes can add considerable value to organizations by enabling them to perform analysis that can provide important information on individual (or record-level) data items. We illustrate practical examples of the need and benefits of sharing linked microdata and identify important privacy issues relating to this context. Based on a conditional distribution approach, we develop a procedure (SASH) for sharing masked attributes in linked microdata that addresses these privacy issues. Our experimental results show that SASH achieves a priori expectations of analytical usefulness, without either party having to provide true values of attribute data. Our results also show that an ad hoc approach such as data swapping, cannot achieve privacy without sacrificing usefulness or vice versa. Our study should provide immediate practical benefits to organizations interested in secure attribute sharing of linked microdata.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Many government agencies such as the Census Bureau gather, store, and disseminate important information. These government agencies release data in many forms — aggregate information about broad demographic groups (median income by state, by race, etc.), contingency tables (frequency counts or aggregate statistics), and individual record level data (microdata). For example, the American Community Survey Public Use Microdata Sample offers record level data on thousands of individuals from across the United States, which consists of over 50 variables (including demographic, economic, housing, and other types of information).<sup>1</sup> This allows the users to perform any type of analysis on the microdata. While microdata offer the greatest analytical flexibility allowing the user to perform any desired analysis on the data, they also pose a greater risk of disclosure than other forms of dissemination. There are two types of disclosure: (1) disclosure of the identity of an individual (identity disclosure), and (2) disclosure of sensitive (confidential) values of an individual (value disclosure). The term privacy is commonly used to refer to both types of disclosure.

Almost invariably, data is gathered with the promise of anonymity and privacy for the subjects. While dissemination of information in any form poses some privacy risks, releasing microdata (individual level data) poses a higher risk of privacy violations compared to releasing tables and summary statistics. To reduce privacy risks, a first step is to deidentify the data (remove all potentially identifying information before the data is released). Unfortunately, de-identification does not always prevent re-identification. For instance, releasing de-identified information that just one individual has an income of over a million dollars in a small town in which all others earned less than (say) \$50,000, would lead to the disclosure of the identity of the individual. Thus, deidentified microdata may need additional protection before dissemination. The techniques designed to prevent the disclosure of identity or other sensitive information are broadly termed as statistical disclosure control (or limitation) (SDC) techniques. SDC techniques have a long history and have received considerable attention in the literature [10,30]. Microdata masking (or “data masking”) procedures are a category of SDC methods. Microdata masking techniques have a dual purpose — to protect privacy and preserve data utility (analytical validity).

Like government agencies, commercial organizations also use the Internet to gather and disseminate data. The volume of data gathered by some Internet companies (such as Google and Facebook) is even greater than the US census Bureau; the data may also be richer. Privacy concerns inhibit the sharing of microdata in commercial organizations since they may be financially liable for privacy breaches and may not possess the expertise required to protect the data adequately. Melville and McQuaid [17] make a compelling case that the requirements of a data masking procedure for sharing data in the business context can be different from those of statistical agencies, warranting the need for procedures suited specifically for secure release of business data. Specifically, they argue that in the context of business organizations, the procedure must be distribution free, automated, fine tunable, low cost, allow flexibility of analysis, and provide high confidentiality protection. They describe one such procedure based on multiple imputation with multi-modal perturbation for releasing de-identified masked microdata. Similar procedures have been proposed by other authors as well. For a comprehensive discussion of the techniques available for microdata masking, please refer to Hundepool et al. [12].

De-identified data has the advantage of preventing obvious privacy violations. But it comes at a price in terms of data utility since it prevents linking data from multiple sources. It is must be emphasized that the utility of microdata arises from the analysis of attribute values belonging to individuals in the microdata. If the data is not de-identified, two parties could link and analyze microdata on the same individuals. This greatly enhances utility, because both parties have access to a greater set of attributes and can benefit from analyzing the combined data. The combined data, with records linked on common identifying information, will be referred to as “linked microdata.”

To underscore the value of linked microdata, consider the following real-world applications:

(1) In an effort to market MegaRed, a premium alternative to fish oils, Facebook combined their own data with data from Datalogix (which gathers information from loyalty cards and other sources) to build a profile based on their past purchases [10]. This offline data is then matched with Facebook's own dossiers on users to help marketers target their advertisements and evaluate the effectiveness of their campaigns.

(2) Shah et al. [27] describe a study in which transaction data from a large retailer was linked to consumer characteristics data from Acxiom. The combined data was used to develop a measure of “habit.”

The above are examples where the ability to combine (or link) identified microdata was critical. Without this ability, these studies would not have been possible. While the above illustrations are good examples of the benefits of linked microdata, they do not represent true data sharing since one of the parties (Facebook and the large retailer) is purchasing consumer data (from Datalogix and Acxiom). Data brokers such as Acxiom are legally required to protect some specific consumer attributes (such as social security number, certain financial and credit information, and health related data). But it is perfectly legal for them to share (or sell) individually identified information about other customer attributes for marketing purposes, as acknowledged by Acxiom in their privacy statement (http://www.acxiom.com/about-acxiom/privacy/usproducts-full-privacy-policy/).

Thus, in the context of data sharing between organizations, we are left with two extremes:

(1) Offering privacy protection by sharing de-identified masked microdata that limits analytical ability (minimizing identity and value disclosure of the shared data) as illustrated by Melville and McQuaid [17], or

(2) Offering no privacy protection by sharing (or purchasing) identified unmasked microdata (complete identity and value disclosure of the shared data) as illustrated by the Facebook scenario [10] and Shah et al. [27].

In this study, we offer a third possibility. In situations where two organizations are permitted to share the identity of common individuals in their database, the organizations can share masked microdata such that neither organization knows the true values of the sensitive attributes of the other organization, but can perform valid analyses on the data at the aggregate level. It is possible to provide protection against value disclosure of sensitive attributes even if the identity of the individuals is known. In other words, the scenario we consider is one where disclosure of identity is not deemed to be a privacy violation, but disclosure of sensitive attribute values is. Privacy policies may permit the organizations to share the identity of common customers [10]. It is important to note that we are not contending that disclosure of identity is not important. We are proposing an enhanced procedure that can be used in the particular scenario described above.

Sharing identified microdata while protecting sensitive attributes has several practical applications

To illustrate these applications, we describe true data sharing versions of the scenarios described earlier:

(1) Consider a scenario where an organization such as a bank or a financial service company, when legally allowed, wishes to combine their own customer microdata with data from a social media firm (such as Facebook). To further protect customer privacy, the bank does not wish to share the original (unprotected) data on their customers' attributes with the social media organization. Similarly, the social media organization does not wish to share the original (unprotected) data with the bank. But the development of improved models based on attributes on the customers (that each possesses) for targeted advertisements will benefit both organizations — better targeted ads improve the hit rate increasing “the bang” for the bank and “the buck” for the social media organization. In this particular case, the sharing may just be one way (the social media organization sharing data with the bank but not the other way).

(2) In the concluding section of their study, Shah et al. [27] state “Further research might observe consumers' behavior across multiple shopping instances at different retail outlets (i.e., across different contexts).” Assume that the home and garden retailer discussed in the Shah et al. [27] study wishes to combine data from common customers with an electronic retailer to analyze the habitual behavior of these customers, without revealing information about individual customers. Such an analysis may be of considerable benefits to both organizations, but sharing actual data may violate legal or policy regulations. The data sharing in this case would be the more general mutual sharing scenario (where the home and garden retailer and the electronics retailer share data with one another).

Practical applications such as these provide the primary motivation for our study. The objective of this study is to develop a masking procedure for linked microdata that allow two organizations to securely share sensitive attributes on common customers (or records with the same identifying information). The procedure permits each organization to perform statistically valid analysis on the masked microdata at the aggregate level. At the individual level, the masking procedure will ensure that value disclosure is maintained at a level acceptable to both organizations.

## 2. Secure identification of common records

The first privacy issue that we identified was that the two sharing organizations should be able to identify only those records that are in common, without either organization obtaining any information about the unmatched records. The solution to this problem is fairly straightforward and is already being practiced. The Wall Street Journal illustrates this process in their coverage of Facebook titled “Facebook sells more access to its members” (see Fig. 1). (http://www.wsj.com/articles/ SB10000872396390443862604578029450918199258).

A more detailed description of this procedure was provided by Telecrunch.com [11]:

Again, it starts with a customer list that a business has already created — for example if I've given my email address to the bookstore on my block so that I can hear about future sales and events. Businesses will be able to upload those lists of email addresses, phone numbers, and user IDs to Facebook, though the data will be hashed first so that Facebook doesn't have access to that information. Meanwhile, Facebook's user data will be similarly hashed, so the company can compare both sets of hashed data, creating a list of users whose contact information matches up with what the advertiser uploaded.

![](/api/attachments/HGAZ2XDF/fulltext/images/1cd177209bd48bf85b289dc4256f62e9c0cf76981bbc440eab4eaa2af1624b09.jpg)  
Fig. 1. Facebook business model (source: Wall Street Journal)

Thus, the matching of the records across two organizations can be performed securely, without either organization being able to identify the unmatched customers of the other organization. For the purposes of this study, we assume that the two organizations have already performed the matching step of the process. In the following section, we describe a two-way sharing procedure that enables the organizations to securely share data about the common customers that have been identified.

The sharing of data between a social media firm and another commercial organization is of considerable interest in practice. Practically every advertiser covets the more comprehensive data on their customers that is available to Facebook and other online social networks for targeted advertising and other promotions. Access to the rich Facebook data on customer attributes can improve the advertiser's targeting decisions, even if the data is masked. However, legal requirements relating to privacy, objections by Facebook users, as well as Facebook's own policies, may prevent true values of customer attributes from being shared with advertisers. It is primarily for this reason that Facebook typically does not “sell” data but provides advertisers the ability to target subscribers. In this particular scenario, once the advertiser has identified the customers it has in common with Facebook, the advertiser could directly contact the customer to gather more information. While we do not preclude the possibility of a survey of the linked customers, data sharing may be both efficient (in terms of cost) and effective (in terms of the richness of the data) compared to surveys. Thus, in addition to two-way sharing of data, secure one-way sharing of data is also of considerable interest. The procedure that we describe in this study can be easily adapted for one-way sharing of data.

## 3. SASH — a masking procedure for secure attribute sharing of linked microdata

For both scenarios (one and two-way sharing), the sharing of masked microdata must preserve the analytical value of the data while preventing disclosure of individual records. Unfortunately, the traditional procedures used to release masked microdata such as the one described by Melville and McQuaid [17] and other similar procedures (see Hundepool et al. [12] for a comprehensive discussion of masking techniques) cannot be used for the purposes of sharing attribute values of linked microdata for one important reason — the primary privacy objective of traditional masking procedures is to prevent the disclosure of the identity of an individual. As Melville and McQuaid note: “Also, the data analyst must be confident that the generated data provide a very high degree of confidentiality, i.e., there is a very low risk of re-identifying individuals …” Our sharing scenario is different. The data is not being released for general access by parties that do not own data on the subjects and therefore re-identification of individuals by third parties is not an issue. In fact, the organizations wish to share data pertaining to identified individuals. When both parties have securely identified common subjects, the confidentiality issue involves protecting the original values of attributes of these common subjects belonging to each party from the other party in the sharing. The masking procedure must reflect this changed confidentiality requirement. Melville and McQuaid [17] procedures are appropriate for the purposes of sharing de-identified microdata. They cannot be used for the purposes of sharing data about a set of individuals whose identity is assumed to be known. Thus, there is a need to develop a new procedure that is capable of performing this task.

In this study, we describe a masking procedure for secure attribute sharing (SASH) of linked microdata. We assume mutually trusting sharing partners who abide by the privacy rules of either party. We assume that the organizations have already identified the set of common records using the hashing algorithm described earlier. Each organization holds a set of variables about these records that they wish to share with the other organization without disclosing the actual values of the individual records. The procedure can be used for all types of attributes. For numerical and ordinal attributes, it can be implemented directly. For categorical attributes, it would be necessary to convert them to binary variables prior to sharing. Fig. 2 provides a pictorial description of the data sharing scenario. The SASH procedure proposed in this paper is highlighted inside the dashed rectangle in Fig. 2, which focuses on the actual sharing of the data. The secure matching of customers (the first step in Fig. 2) has been addressed in prior literature and is beyond the scope of this paper.

Formally, consider two partner organizations A and B with a set of n common records. Let X be a matrix of dimension (n × k) representing the data for k attributes for the records held by A. Let be a matrix of dimension (n × l) representing the data for l attributes for the records held by B. The objective of the SASH procedure is for A (B) to securely share X (V) with B (A). Let Y represent the masked version of X and W the corresponding masked version of V. At the completion of the data sharing, partner organization A possesses the combined data set (X, W) and partner B has (V, Y).

The objective of the data sharing procedure SASH is to preserve statistical utility (by preserving as many statistical properties as possible) while not disclosing X to partner B and V to partner A. These can be stated, in an idealized form, as the following two objectives:

(1) Analytical validity objective: The joint distribution of the masked data f(X, W) and f(V, Y) should, asymptotically, be the same as the joint distribution of the original data f(X, V).

![](/api/attachments/HGAZ2XDF/fulltext/images/1a9b61192b478e5863838faf2c92800851c769c065fc7eb25aa9d3fe93304f3e.jpg)  
Fig. 2. A pictorial description of the data sharing procedure.

(2) Confidentiality objective: Given the masked microdata

a. B should not be able to predict the values of the true confidential attribute X with an accuracy higher than a threshold $\gamma _ { i } ( i = 1 , 2 , . . . , k )$ specified by A, and

b. A should not be able to predict the values of true confidential attribute $V _ { i }$ with an accuracy higher than a threshold $\delta _ { j } ( j = 1 , 2 , . . . , l )$ specified by B.

The general sharing procedure that we have described above can be used in the practical scenarios that we discussed in the introduction between two commercial organizations, two sets of researchers, etc. A simplification of this two-way sharing procedure can be used in a oneway sharing scenario such as when a social media organization shares information with another organization but not vice versa. In this second case, the non-sharing partner does not even have to identify the characteristics of the attributes held. We provide further analysis of this scenario in the discussion section.

The key to being able to successfully achieve the analytical validity and the confidentiality objective when performing data sharing is to be able to model the joint distribution of the complete set of variables held by both parties (X, V) as we now discuss.

## 3.1. Modeling the joint distribution of (X, V)

Masking techniques can be broadly classified into two types, ad hoc approaches and model based approaches. Ad hoc approaches such as noise addition, data swapping, and micro-aggregation (see [12] for a comprehensive discussion of data masking approaches) generate masked data as a function of the original values of the sensitive attribute. The utility and disclosure prevention result directly from the proximity of the masked values to the original values. There is also a direct relationship between analytical validity and disclosure risk. The closer (farther) the proximity between the original and masked values, the greater (lower) the analytical validity and greater (lower) the disclosure risk. Previous studies have established that compared to model based approaches, ad hoc approaches result in lower data utility and higher disclosure risk [8,17,18].

Model based approaches attempt to model the entire data set and then generate a masked version of the data that closely approximates the original data [12]. Typically, this is performed by using the conditional distribution approach. In the two-way sharing example, this implies that for organization B, the masked values Y are generated from the conditional distribution f(X|V) (and for organization A, the masked values W are generated from the conditional distribution f(V|X)). Such an approach requires the modeling of the joint distribution f(X, V). Modeling the multivariate joint distribution of a set of attributes with arbitrary marginal distributions is extremely difficult [14]. Fortunately, it is possible to achieve many desirable analytical validity and disclosure risk properties by approximating the joint distribution f(X, V) (and thereby the conditional f(X|V) and f(V|X)) using statistical models.

Many techniques have been proposed to generate masked values from the approximation of conditional distributions. These include a multivariate normal model [9], log-linear model [8], multiple imputation [17,24,25], copula model [26], the skew-t distribution[15], and odds ratio expression [23]. The SASH procedure employs the copula model for approximating f(X, V) due to the following reasons:

⦁ The log-linear model [8] is intended for categorical data and not numerical data.

⦁ The multivariate normal model [9] can only be used for preserving linear relationships.

⦁ The skew t-distribution [15] and odds ratio expression [23] are computationally difficult.

⦁ Multiple imputation requires “multiple” copies of the data to be shared in order to provide adequate analytical capability which may be difficult in practice.

The key parameter of the copula based approach used in this study is the pairwise rank order correlation between the variables. That is, the copula model ensures that the pairwise rank order correlation between the shared masked attributes Y and W is approximately the same as that between the original attributes X and V. An important consequence of this is that all monotonic (and not just linear) relationships between X and V are maintained in Y and W. The copula model also has the distinct advantage in the data sharing context over the other methods discussed above, namely that it requires only ranks, rather than actual data values. In other words, not only are the original values of sensitive attributes never involved in the sharing process but, as shall be seen later, the risk of any accidental disclosure of sensitive information is considerably reduced.

Copulas offer a simple, effective approach to “join univariate distribution functions to form multivariate distribution functions.”[20]. In recent years, copulas have been applied in decision analysis [1], and in particular, as an effective approach for modeling multivariate marketing data [3]. Copulas have also been used in the context of data masking $[ 2 3 ,$ 26]. Copula models are based on Sklar's theorem [28] which states that if $\pmb { X } = ( X _ { 1 } , X _ { 2 } , . . . , X _ { k } )$ with cumulative distribution functions (CDF) $u _ { i } =$ $F _ { i } ( X _ { i } = x _ { i } ) ( i = 1 , 2 , . . . , k )$ and joint CDF $f ( x _ { 1 } , x _ { 2 } , \ldots x _ { k } )$ , then there exists a function C such that

$$
F (X _ {1} = x _ {1}, X _ {2} = x _ {2}, \dots , X _ {k} = x _ {k}) = C (u _ {1}, u _ {2}, \dots u _ {k}),\tag{1}
$$

where $C ( u _ { 1 } , u _ { 2 } , . . . , u _ { k } )$ is the joint copula CDF with uniform marginal distributions. There are many alternative specifications for the copula function [20]. The selection of the appropriate copula function depends on the analytical validity of the data that we desire to preserve.

We use the Gaussian copula for modeling the data for several reasons. First, it is a general and robust copula and provides the ability to model the entire range of relationships between attributes [3]. Second, it is relatively easy to implement with knowledge of only the rank order correlation between the attributes [1]. Third, monotonic relationships among the masked attributes are preserved to be the same as the original confidential attributes. Fourth, since the copula model can be characterized by the rank order correlation, the parties do not have to share any information regarding the characteristics of the data (other than their rank) until the very last stage, providing an additional layer of protection.

The Gaussian copula parameterized with product moment correlation matrix $\pmb { \rho }$ instead of the rank order correlation, can be written as:

$$
\boldsymbol {C} _ {\rho} (\boldsymbol {u}) = \boldsymbol {\Phi} _ {\rho} ^ {\boldsymbol {k}} \left(\Phi^ {- 1} (u _ {1}), \Phi^ {- 1} (u _ {2}), \dots , \Phi^ {- 1} (u _ {k})\right),\tag{2}
$$

where $\Phi _ { \rho } ^ { k }$ represents the joint CDF of a standard multivariate normal distribution with k attributes and product moment correlation matrix $\rho ,$ and $\phi ^ { - 1 }$ represents the inverse of the CDF of the univariate standard normal function. In addition, the elements $( \rho _ { i j } )$ of the product moment correlation matrix can be computed from the elements $( r _ { i j } )$ of the rank order correlation matrix r as follows

$$
\rho_ {i j} = 2 \sin \left(\frac {\pi r _ {i j}}{6}\right).\tag{3}
$$

Thus, the construction of the Gaussian copula only requires knowledge of the rank order correlation among the attributes of interest and their marginal distributions, but not their true joint or conditional distributions. Alternative specifications for the copula function are possible and may be worthy of further research.

In our context, we modify the traditional copula procedure because the modeling must be performed without either party having access to original data belonging to the other party. Before applying the copula model in Eq. (2), additional procedures are needed to securely compute the rank order correlation between attributes owned by different parties. This is described in greater detail in the next section.

## 3.2. Secure computation of the rank order correlation matrix

The first step of the SASH model is the secure computation of the rank order correlation matrix. At this stage of the process, it is necessary that this computation be performed without either party sharing the actual vectors of X and V. The rank order correlation matrix of the entire data set (containing all attributes belonging to the provider as well as the client) can be partitioned as follows:

$$
\boldsymbol {R} = \left[ \begin{array}{c c} \boldsymbol {r} _ {X X} & \boldsymbol {r} _ {X V} \\ \boldsymbol {r} _ {V X} & \boldsymbol {r} _ {V V} \end{array} \right]
$$

Organization A can compute the rank order correlation matrix $( r _ { X \alpha } )$ of its attributes X and organization B can compute the rank order correlation $( r _ { W } )$ of its attributes V. However, neither party can compute the rank order correlation between the attributes in X and $V ( r _ { x v } )$ without access to each other's data. Hence, it is necessary to consider alternatives for the secure computation of $\pmb { r } _ { X V }$ so that individual record level information is not shared.

Research on computing a common quantity such as correlations between two variables belonging to two different parties, can be found in the secure multi-party computation literature. The computation of the rank order correlation requires the secure computation of the scalar product of two confidential variables owned by two different parties. Du and Atallah [4] proposed two algorithms for the secure computation of the scalar product. In the first, 1-out-n Oblivious Transfer, the confidential variable is hidden among several synthetic data vectors and sent to the other party. The algorithm then computes the exact scalar product through a series of computations that remove the effect of the synthetic vectors. Unfortunately, with this algorithm, the true confidential values suffer from a high risk of exact value disclosure [16]. This algorithm is also not scalable for large data sets since a large number of synthetic vectors are needed to hide the true confidential vector. Du and Atallah [4] also proposed an alternative procedure that takes advantage of the special property of homomorphic encryption whereby product of the encrypted values equal the encrypted value of the product. However, the algorithm is based on public-key encryption which requires extensive processing and hence not very efficient [22]. Therefore, this algorithm is not scalable for practical implementations involving large data sets. A third alternative called the component algorithm was proposed by Vaidya and Clifton [29], which uses a n × n matrix (C) to form coefficients of linear independent equations. Confidential values of both parties are hidden inside equations in such a way that the number of equations is much less than the number of unknown variables. This procedure is also subject to exact disclosure of values [16].

More recently, Karr et al. [13] proposed a procedure for computing secure matrix products. This procedure allows “the database owners to perform analyses that none can perform individually because none has access to all the attributes” to compute the full data covariance matrix [13]. Computing the rank order correlation matrix given ranks is equivalent to computing the full data covariance matrix given data. Compared to the other procedures discussed earlier, this procedure provides the advantage that it offers good security and efficiency as it relies on g orthonormal n-dimension vectors where the value of g is approximately ${ \mathfrak { n } } / 2$ . Hence, for the purposes of this study, we use this procedure for the secure computation of the r .

The process of computing the rank order correlation matrix (X, V) proceeds as follows:

(1) The first organization generates a set of g orthonormal ndimension vectors $( A _ { 1 } , \ A _ { 2 } , \ . . . , \ A _ { g } )$ such that $( X _ { j } ^ { R } ) ^ { T } A _ { i } =$ $0 ( i = 1 , 2 , . . , g ; j = 1 , 2 , . . . , l )$ where $X _ { j } ^ { R }$ is the vector of ranks of $X _ { j } .$ The first organization sends the $( n \times g )$ matrix A to the second organization.

(2) The second organization computes $\pmb { Z } = ( \pmb { I } - \pmb { A } \pmb { A } ^ { T } ) \pmb { V } ^ { R }$ (where I is an identity matrix of dimension $( n \times n )$ and $V ^ { R }$ is a matrix of the ranks of the values in $\pmb { V } )$ and sends Z to the first organization along with $r _ { V V } .$

(3) The first organization computes $( X ^ { R } ) ^ { T } Z = ( X ^ { R } ) ^ { T } ( I - A A ^ { T } ) V ^ { R } =$ $( X ^ { R } ) ^ { T } V ^ { R }$ which is the cross-product of the rank order vectors of (X, V). Using this information, the first organization computes the rank order correlation between X and V $( r _ { X V } )$ , which along with the already constructed $\mathbf { r } _ { x x }$ and $r _ { W }$ (received from B) completes the construction of R. Organization A then shares R with organization B.

The process could be initiated by either party. Note that in the process of constructing R, neither organization has to reveal to the other any information about the individual variables that are being shared or even identity them. Thus, the secure matrix computation ensures that the privacy of the data belongs to both parties. Once R has been constructed and shared, the parties can individually perform disclosure risk assessment.

## 3.3. Disclosure risk assessment

As discussed earlier, it is impossible to share any data without some risk of disclosure [7]. SASH provides the sharing parties the ability to use the shared values of R to assess the level of disclosure likely to take place, prior to actually sharing the data. Traditional disclosure risk assessment for data masking has two aspects, i.e. identity disclosure and value disclosure [5,6]. Identity disclosure provides an assessment of the risk of being able to link the released masked data to the original record. In this context, however, this risk is moot since identified data is being shared and it is the level of value disclosure likely to take place that is relevant. As discussed earlier, in situations where the identity of the individuals cannot be disclosed (for legal or ethical reasons), SASH cannot be used.

Value disclosure is the ability of the user to predict the value of an attribute for a particular record based on the masked microdata [2,9]. It is assessed using the accuracy of regression-based prediction of the values of the confidential attribute using both the masked data and any nonconfidential attributes that may be present [9,21]. This assessment is performed for each attribute by computing the $R ^ { 2 }$ value. High $R ^ { 2 }$ values indicate high risk of disclosure (and $R ^ { 2 }$ of 1 indicating complete value disclosure) since they imply that the user will be able to predict the value of the confidential attributes with a high degree of accuracy. Each of the parties may have different levels of threshold for the variables being shared based on the sensitivity of the variable. Let $( \gamma _ { 1 } , \gamma _ { 2 } , . . . , \gamma _ { k } )$ represent the threshold levels for $\pmb { X } ( = X _ { 1 } , X _ { 2 } , . . . , X _ { k } )$ established by organization A, and let $( \delta _ { 1 } , \delta _ { 2 } , . . . , \delta _ { l } )$ represent the threshold levels for $\pmb { V } ( = V _ { 1 } , V _ { 2 } , . . . , V _ { l } )$ established by organization B. Using the shared rank order correlation matrix R, organization A can assess the risk of value disclosure by computing $R _ { X _ { i } | V } ^ { 2 } ~ ( i = 1 , 2 , . . . , k )$ Similarly, organization B can assess the risk of value disclosure by computing $R _ { V _ { j } | X } ^ { 2 } ~ ( j = 1 , 2 , . . . , l )$ . We assume that the sharing will proceed when $R _ { X _ { i } | V } ^ { 2 } \le \gamma _ { i } ( i = 1 , 2 , . . . , k )$ and $R _ { V _ { j } | X } ^ { 2 } \le \delta _ { j } ( j = 1 , 2 , . . . , l )$ . In cases where this requirement is violated, we assume that the parties renegotiate the sharing agreement (by eliminating the variables that violate the threshold) or, in the worst case scenario, refrain from sharing the data. SASH permits organizations to re-negotiate (or even withdraw) from the sharing agreement based on thresholds assessed using the shared rank order correlation matrix R.

SASH also ensures that external variables that may be available to either party will not impact the disclosure level of the shared data. Research has shown that for ad hoc masking techniques, external (or auxiliary) variables could pose a serious threat to disclosure risk. This phenomenon occurs since the auxiliary variables could be closely related to the shared variable. It may allow the party receiving the data to possibly disclose more than what the providing party intended. SASH, however, is based on the conditional distribution approach. Consequently, once an attribute is approved for sharing by the organization, it is guaranteed that the predictive ability of the receiving party is al ways below the threshold level established by the sharing party.

For the purposes of illustration, assume that, in addition to V, organization B also possesses a set of auxiliary variables S. The conditional distribution approach for generating the masked data ensures that the ability to predict X is dictated exclusively by its relationship with V and is (conditionally) independent of S. In other words, sharing the masked data (Y) in the presence of auxiliary variables (S) will have no impact on the ability to predict X since $f ( X | V , Y ) = f ( X | V ) f ( Y | V , S ) =$ f(Y|V) [19]. The masked data W shared by organization B is similarly protected. Thus, SASH offers both parties the important assurance that some unanticipated auxiliary variable(s) will not result in disclosure of sensitive information.

## 3.4. Sharing the microdata

Once the sharing parties are satisfied with the disclosure thresholds, SASH can employ either perturbation or reverse mapping to generate the masked data. With the perturbation approach, the masked data is simulated from the same distribution as the original data. In practice, this can impose a considerable burden on the two sharing parties especially if the data sharing occurs frequently. In addition, users are also reluctant to analyze simulated data even if they are assured that such analysis would provide the same results as the original data. This reluctance is characterized by Raghunathan et al. [24] as follows: “Could we seriously propose spending time analyzing completely ‘fake’ data?” Reverse mapping is a simple alternative in these situations.

In reverse mapping, a new realization of the attribute to be shared is obtained from the conditional distribution f(X|V) (or f(V|X)). Each value in this realization is then replaced with a value from the original attribute that has the same rank. The resulting (reverse mapped) masked values maintain the same marginal distribution as the original values, but for any given record, the original and masked values are different (see [18] for a comprehensive discussion of reverse mapping). Thus, reverse mapping can alleviate concerns on the part of users to use masked values that are perceived to be artificial.

In order to implement reverse mapping, organization A (B) strips all identifying information from $\pmb { X } ( \pmb { V } ) ,$ , randomly sorts each attribute in X (V), and shares this randomly sorted data with organization B (A). Organization B (A) then generates simulated values $\mathbf { } Y ^ { * } \left( W ^ { * } \right)$ which are then reverse mapped using the randomly sorted values of $X ( V ) .$ The specific details of the procedure are described below for organization A sharing data with organization B. Note that the rank order correlation matrix R has already been shared with both parties.

(1) Organization A strips all identifying attributes, randomly sorts each attribute in X individually (and independent of all other attributes) and shares this randomly sorted data with B. The random sorting of the data removes all linkages between the original record and X, as well as all relationships between the attributes in X.

(2) Organization B reconstructs the masked data Y as follows:

a) Convert the rank order correlation matrix R into the product order correlation matrix using Eq. (3).

b) Use Gaussian copula-based model to generate the simulated masked values: For each record $i = 1 , 2 , . . . , n$ , compute $y _ { i } ^ { * } =$ ρXV ρVV<sup>−1</sup> $\pmb { \nu } _ { i } ^ { * } + \pmb { e } _ { i } ,$ where

$$
\boldsymbol {v} _ {\boldsymbol {i}} ^ {*} = \left(\phi^ {- 1} \left(\frac {t _ {(i) 1} - 0 . 5}{n}\right), \phi^ {- 1} \left(\frac {t _ {(i) 2} - 0 . 5}{n}\right), \dots , \phi^ {- 1} \left(\frac {t _ {(i) l} - 0 . 5}{n}\right)\right),
$$

t<sub>(i)j</sub> is the rank of $\nu _ { i j }$ with respect to j, and $\mathbf { \ } e _ { i } \sim \Phi ( 0 , \rho _ { X X } -$ ρXV $\rho _ { { \pmb v } } ^ { - 1 } \rho _ { { \pmb v } { \pmb x } } ) \ ^ { 2 }$

c) Perform reverse mapping: for each record $i = 1 , 2 , . . . , n ,$ and each attribute $j = 1 , 2 , . . . , k ,$ i. compute $q _ { i j } \doteq R a n k ( y _ { i j } ^ { * } .$ ) with respect to j

ii. set $y _ { i j } = x _ { ( q _ { i j } ) , j }$ where $x _ { ( i ) j }$ is the ordered observations of attribute j. The collection of $y _ { i j }$ i.e., Y, represents the masked values of X.

The process of generating the masked values W by organization A is performed similarly by using the randomly sorted V shared by B, R, and the Gaussian copula model. For the sake of brevity, we do not describe the entire process. In a one-way sharing scenario, the process would terminate at step (c) above.

## 3.5. Summary of the SASH procedure

The entire data sharing process can be summarized as follows:

(1) The organizations securely identify only those customer records that both possess (and not unmatched records) and mutually agree on the attributes for these matched customers that are to be shared (X for organization A and V for organization B).

(2) Using the procedure of Karr et al. [13], the organization computes the rank order correlation R of the attributes to be shared (X, V) and share R.

(3) Using R, each organization performs its own risk assessment to ensure that the release of the masked values would not result in disclosure beyond the established threshold. If the risk of disclosure is higher than the acceptable threshold, we assume that the organizations will return to step (1) and renegotiate the contract.

(4) Organization A

a. Strips all identifying attributes, randomly sorts each attribute in X individually (and independent of all other attributes) and shares this data with organization B.

b. Organization B generates the normalized masked values $y _ { i j } ^ { * }$ and subsequently performs reverse mapping of y<sub>ij</sub><sup>⁎</sup> ← $\mathcal { X } ( i ) j$ to result in Y.

(5) Organization B

a. Strips all identifying attributes, randomly sorts each attribute in V individually (and independent of all other attribute) and shares this data with organization A.

and subsequently performs reverse mapping of $w _ { i j } ^ { * }  \nu _ { ( i ) j }$ to result in W.

The SASH procedure offers high utility and low disclosure risk since the shared masked data possesses the following characteristics: (1) the marginal distribution of any given attribute $\pmb { Y _ { i } } \left( \pmb { W _ { j } } \right)$ is exactly the same as that of $X _ { i } \left( V _ { j } \right)$ for all $i = 1 , 2 , . . . , k ( j = 1 , 2 , . . . , l ) ,$ , but at the individual record level, $y _ { m i } \left( w _ { m j } \right)$ is different from $x _ { m i } \left( \nu _ { m j } \right)$ $( m = 1 , 2 , . . . , n )$ , (2) the rank order correlations of (X, W) and (Y, V) are asymptotically the same as that of (X, V), (3) From the perspective of organization A, it minimizes disclosure risk by ensuring that $f ( \pmb { X } , \pmb { Y } | \pmb { V } ) = f ( \pmb { X } | \pmb { V } ) \times f ( \pmb { Y } | \pmb { V } )$ and $f ( \pmb { Y } | \pmb { V } , \pmb { S } _ { 1 } ) = f ( \pmb { Y } | \pmb { V } )$ (where $\pmb { S } _ { 1 }$ represents a set of auxiliary attributes available to organization B but unknown to organization A). Similarly, from the perspective of organization B, SASH minimizes disclosure risk by ensuring that $f ( V , W | X ) = f ( V | X ) \times f ( W | X )$ and $f ( W | \pmb { X } , \pmb { S } _ { 2 } ) = f ( W | \pmb { X } )$ (where $\pmb { S } _ { 2 }$ represents a set of auxiliary attributes available to organization A but unknown to organization B).

Thus, the masked data preserves the pre-specified statistical characteristics to the same as those of the original data and minimizes the level of disclosure to no more than that resulting from the relationship between (X, V). The last property will be preserved by any model as long as the masked data is generated from the conditional distribution f(XIV) or f(VIX). As we discussed earlier, in this study, we chose the copula model thereby preserving rank order correlation. Hence, analyzing the combined data (X, W) or (V, Y) for all monotonic relationships should yield the same results, asymptotically, as analyzing the original data (X, V). In the following section, we empirically illustrate and evaluate the performance of the SASH procedure.

Table 1  
Correlation matrix of attributes X, Y, and S.

<table><tr><td></td><td>X</td><td>V</td><td>S</td></tr><tr><td>X</td><td>1.0</td><td>0.3</td><td>0.9</td></tr><tr><td>V</td><td></td><td>1.0</td><td>0.0</td></tr><tr><td>S</td><td></td><td></td><td>1.0</td></tr></table>

## 4. Empirical assessment of SASH

## 4.1. Single attribute sharing

In the first experiment, we present a simple case of two organizations sharing a single attribute such as the habitual return behavior of customers common to a garden retailer and an electronic retailer [27]. For comparison purposes, we also provide the results of using a simple data swapping procedure on the same data. In data swapping, the original values of two records within a specified proximity are exchanged with one another. The organizations then exchange the swapped data. Since data swapping is an ad hoc procedure, it should result in lower data utility (attenuation of correlation) and increased disclosure risk compared to model based procedures [18]. We use data swapping simply to illustrate the increased benefits derived from using SASH.

For the purposes of this experiment, we assume that organization A holds variable X whose masked version Y is shared with B, and organization B holds variable V whose masked version W is to be shared with A. In addition, we also consider an auxiliary variable S that is in the possession of organization B. The correlation matrix between these three variables is provided in Table 1. We intentionally specified a very high correlation between (X, S) compared to (X, V) to examine whether organization B possessing an auxiliary attribute S that is highly correlated to X, poses a serious disclosure risk to X, when the masked data Y is shared. In other words, we would like to assess whether organization B could compromise X using S (with which it is highly correlated) and Y. Specifying the correlation between (V, S) to equal 0 provides us with the ability to isolate the predictive power of the individual attributes.

(1) Assessing analytical validity: The correlation between the shared variables (X, W) and (V, Y) should be the same as that between the original variables (X, Y). Thus,

$$
r _ {X, W} = r _ {V, Y} = r _ {X, V} = 0. 3.
$$

Results of single attribute sharing experiment.

<table><tr><td>Performance measure</td><td>n</td><td>SASH</td><td>Swap (10%)</td><td>Swap (25%)</td><td>Swap (50%)</td></tr><tr><td rowspan="3">Analytical validity(1)</td><td>100</td><td>0.295</td><td>0.280</td><td>0.238</td><td>0.154</td></tr><tr><td>1000</td><td>0.300</td><td>0.283</td><td>0.241</td><td>0.157</td></tr><tr><td>5000</td><td>0.300</td><td>0.283</td><td>0.242</td><td>0.157</td></tr><tr><td rowspan="3">Disclosure risk assessment(2 a.)</td><td>100</td><td>0.099</td><td>0.877</td><td>0.651</td><td>0.308</td></tr><tr><td>1000</td><td>0.091</td><td>0.889</td><td>0.662</td><td>0.320</td></tr><tr><td>5000</td><td>0.090</td><td>0.890</td><td>0.662</td><td>0.321</td></tr><tr><td rowspan="3">Disclosure risk assessment(2 b.)</td><td>100</td><td>0.090</td><td>0.798</td><td>0.605</td><td>0.292</td></tr><tr><td>1000</td><td>0.090</td><td>0.809</td><td>0.616</td><td>0.309</td></tr><tr><td>5000</td><td>0.090</td><td>0.810</td><td>0.617</td><td>0.311</td></tr></table>

That is, in Table 2 below, we would like to see the analytical validity value be as close to 0.3 as possible, for different sample sizes.

(2) Assessing disclosure risk:

(a) The sharing of the masked variable should not allow either organization to predict the value of the original variable with a greater degree of accuracy.

$$
R _ {V | X, W} ^ {2} = R _ {V | X} ^ {2} = (r _ {X Y}) ^ {2} = 0. 3 ^ {2} = 0. 0 9 \text { and },
$$

$$
R _ {X | V, Y} ^ {2} = R _ {X | V} ^ {2} = 0. 0 9.
$$

That is, in Table 2 below, we would like to see the disclosure risk 2(a) be as close to 0.09 as possible, for different sample sizes.

(b) The presence of an auxiliary variable should not improve the predictive ability of either organization.

$$
R _ {X | V, S} ^ {2} = R _ {X | V} ^ {2} = 0. 0 9
$$

That is, in Table 2 below, we would like to see the disclosure risk 2(b) be as close to 0.09 as possible, for different sample sizes.

We consider three different sample sizes $( n = 1 0 0 , 5 0 0 , 1 0 0 0 )$ . We also consider three proximity levels (10%, 25%, and 50%) of swapping where the proximity level is expressed as a percentage of n. The experiment consists of generating the data with the correlation matrix shown in Table 1 and assessing the data utility and disclosure risk characteristics of the shared data. The entire experiment was replicated 1000 times. Table 2 provides the average of the 1000 replications of the experiment for the analytical validity and disclosure risk measures above.

The results provided in Table 2 verify the theoretical claims relating to SASH. The correlations using the masked microdata are almost identical to the correlation between the original variables and the proportion of variability explained is close to $( r _ { X Y } ) ^ { 2 } = 0 . 0 9$ . The results are consistent across all sample sizes as well. Data swapping does not perform as well. In terms of analytical validity, all three levels of data swapping result in correlation attenuation (that is, the correlation post masking is weaker than the correlation pre masking). Data swapping also results in increased disclosure risk when the masked data is shared, signifying an increased ability to predict the original variable. The level of disclosure is lower when the swapping distance is set to 50%, but in these cases, the analytical validity is extremely poor. In summary, the results in Table 2 provide empirical verification of the theoretical properties of SASH which ad hoc procedures (such as data swapping) cannot deliver.

Comparison of the rank order correlation between the attributes for the original and SASH masked data.

<table><tr><td>Attributes</td><td> $(X_1, X_2)$ </td><td> $(X_1, V_1)$ </td><td> $(X_1, V_2)$ </td><td> $(X_2, V_1)$ </td><td> $(X_2, V_2)$ </td><td> $(V_1, V_2)$ </td></tr><tr><td>True correlation</td><td>0.000</td><td>0.400</td><td>0.600</td><td>0.200</td><td>0.400</td><td>0.800</td></tr><tr><td colspan="7">Results for organization A</td></tr><tr><td>n</td><td> $(X_1, X_2)$ </td><td> $(X_1, W_1)$ </td><td> $(X_1, W_2)$ </td><td> $(X_2, W_1)$ </td><td> $(X_2, W_2)$ </td><td> $(W_1, W_2)$ </td></tr><tr><td>100</td><td>--</td><td>0.397</td><td>0.597</td><td>0.193</td><td>0.390</td><td>0.792</td></tr><tr><td>1000</td><td>--</td><td>0.402</td><td>0.601</td><td>0.200</td><td>0.399</td><td>0.800</td></tr><tr><td>5000</td><td>--</td><td>0.400</td><td>0.600</td><td>0.201</td><td>0.400</td><td>0.800</td></tr><tr><td colspan="7">Results for organization B</td></tr><tr><td>n</td><td> $(Y_1, Y_2)$ </td><td> $(Y_1, V_1)$ </td><td> $(Y_1, V_2)$ </td><td> $(Y_2, V_1)$ </td><td> $(Y_2, V_2)$ </td><td> $(V_1, V_2)$ </td></tr><tr><td>100</td><td>-0.001</td><td>0.397</td><td>0.596</td><td>0.195</td><td>0.392</td><td>--</td></tr><tr><td>1000</td><td>0.000</td><td>0.400</td><td>0.599</td><td>0.201</td><td>0.400</td><td>--</td></tr><tr><td>5000</td><td>0.000</td><td>0.400</td><td>0.600</td><td>0.200</td><td>0.400</td><td>--</td></tr></table>

## 4.2. Multi attribute sharing

In this section, we describe an experiment to illustrate that SASH performs effectively for multiple attributes by ensuring that the relationships between the shared attributes are maintained effectively for complex relationships and distributional characteristics. The attributes were specifically chosen to have widely varying magnitudes (mean = 75 to 5000), shapes (symmetric, left skewed, right skewed, exponential), and rank order correlations (ranging between 0.0 and 0.8) (Table 3). Our choice was motivated by the fact that when two different types of organization share data, they are likely to have such diverse characteristics. Our objective was to highlight that SASH can be implemented even for such datasets.

We assume that organization A share masked attributes $( Y _ { 1 } , Y _ { 2 } )$ with organization B who, in turn shares masked attributes $( W _ { 1 } , W _ { 2 } )$ with A. In the simulation experiment, the original data was generated using the characteristics specified above, the masked variables were generated using the SASH procedure, and the correlation between the original and masked variables was computed. We used three different sizes for the common set of customers (n = 100, 1000, and 5000). Every experiment was replicated 1000 times. Table 4 provides the average correlation of the masked variables from the 1000 replications. The table is presented as two panels, the top panel representing organization A and the bottom panel representing organization B. Note that from the perspective of organization A, the correlation between variables $( X _ { 1 } , X _ { 2 } )$ are of no consequence since they are not being shared. Hence,

Distributional characteristics of the original experimental attributes

<table><tr><td colspan="2">Organization A</td><td colspan="2">Organization B</td></tr><tr><td>Attribute  $X_1$ </td><td>Attribute  $X_2$ </td><td>Attribute  $V_1$ </td><td>Attribute  $V_2$ </td></tr><tr><td><img src="/api/attachments/HGAZ2XDF/fulltext/images/1250d952a16de3dc06164659e3da6566aaeb53f57eccff25655ff5aa064da3fa.jpg"/></td><td><img src="/api/attachments/HGAZ2XDF/fulltext/images/3e1a7cd217fcaaf8b3c0781575d9519c7c59067411775e283a8b9d353db011c7.jpg"/></td><td>0 10000 20000</td><td>0 50 100</td></tr><tr><td>NormalMean = 1000Standard dev. = 200</td><td>Standard dev. = 15</td><td>GammaMean = 5000Standard dev. = 3160</td><td>ExponentialMean = 25Standard dev. = 25</td></tr></table>

Population rank order correlation matrix

<table><tr><td>Attribute  $X_1$ </td><td>Attribute  $X_2$ </td><td>Attribute  $V_1$ </td><td>Attribute  $V_2$ </td></tr><tr><td rowspan="4">1.0</td><td>0.0</td><td>0.4</td><td>0.6</td></tr><tr><td>1.0</td><td>0.2</td><td>0.4</td></tr><tr><td></td><td>1.0</td><td>0.8</td></tr><tr><td></td><td></td><td>1.0</td></tr></table>

Please cite this article as: K. Muralidhar, et al., Secure attribute sharing of linked microdata, Decision Support Systems (2015), http://dx.doi.org/ 10.1016/j.dss.2015.10.005

![](/api/attachments/HGAZ2XDF/fulltext/images/b1aef1999bf82fd8b4f334e055f60722dbd6f64bc0027f881c6565d8fdf0442f.jpg)  
a. Scatter plot of the original values of $( V _ { 2 } , V _ { 1 } )$

![](/api/attachments/HGAZ2XDF/fulltext/images/f8c0e2ee7fd230ca497a13350c48dadf1266704642a5ed9d592c34fa12679667.jpg)  
b. Scatter plot of the masked values of $( W _ { 2 } , W _ { 1 } )$  
Fig. 3. a. Scatter plot of the original values of $( \pmb { V } _ { 2 } , \pmb { V } _ { 1 } ) .$ . b. Scatter plot of the masked values of $( \pmb { W } _ { 2 } , \pmb { W } _ { 1 } )$

this correlation is represented by “–” in the top panel (as is the correlation between $( V _ { 1 } , V _ { 2 } )$ in the bottom panel).

The results in Table 4 indicate that the correlations between the masked attributes are maintained very well. In almost all cases, the correlation between the masked variables is very close to the correlation between the original variables. This implies that using the masked data in place of the original data for analytical purposes will yield results that are very similar to the analysis using the original data. The results are also consistent — as the sample size increases, the accuracy of the masked estimates approach the true value of the correlation. When $n = 5 0 0 0$ , there is practically no difference in the rank order correlation between the original and shuffled attributes. Combined with the fact that the marginal distribution of the individual shared attributes is unmodified, this ensures the analytical validity of the masked data.

The effectiveness of the SASH based data sharing procedure in preserving asymptotic monotonic non-linear relationships is illustrated in the following figure. Fig. 3a provides a scatter plot of the original values of attributes $( V _ { 2 } , V _ { 1 } )$ . Fig. 3b provides a scatter plot for the same attributes, but with masked values of $( W _ { 2 } , W _ { 1 } )$ in place of the original values. Comparing the two figures, it is easy to see that the masked data very closely approximates the non-linear relationship in the original data. Thus, organization A would be able to perform appropriate analysis with access only the masked values (W , W ).

As an additional illustration, consider a plot of attributes $( X _ { 1 } , V _ { 1 } )$ . Unlike the previous example where both attributes were masked, in this case, one attribute $\left( X _ { 1 } \right)$ is masked, while the other (V ) is left unmasked. Fig. 4a provides the scatter plot using the original data $( X _ { 1 } , V _ { 1 } )$ and Fig. 4b provides the same scatter plot of $( Y _ { 1 } , V _ { 1 } )$ . As in the previous example, the two plots are very similar illustrating the ability of SASH to preserve complex relationships between variables even if only one of them is masked. The plots illustrate the ability of SASH procedure to preserve relationships between one original attribute and the other which is masked, as long as the attributes were included in the model.

![](/api/attachments/HGAZ2XDF/fulltext/images/55234faeeedb14ea71700c2748567950582395dc2019254410fe0cc1772f47e3.jpg)  
a. Scatter plot of the original values of $( X _ { 1 } , V _ { 1 } )$

## 5. Conclusions

In this study, we consider the secure sharing of linked microdata where two organizations are allowed to share the identity of common individuals who reside in their databases, but the values of sensitive attributes about these individuals must be protected. While this may not be the most common scenario, there are many examples of this specific scenario in practice as we have discussed in the introduction. Secure sharing of linked microdata attributes can add considerable value to organizations by enabling them to perform analysis that can provide important information on individual (or record-level) data items. We identified important privacy issues relating to this context, and developed a procedure (SASH) for sharing masked attributes in linked microdata that addresses these privacy issues and retains the usefulness of the shared data.

Our experimental results show that SASH achieves its objective of enabling two parties to share accurate aggregate information about their respective attributes on common customers (analytically valid data sharing), without either party having to provide true values of attribute data (secure sharing). Since data is masked during sharing using a conditional distribution approach, the performance of SASH satisfies a priori expectations of high performance. The simulation was performed to validate the anticipated performance. By contrast, as shown by the simulation results, the performance of ad hoc approaches to data masking, as exemplified by data swapping, depends on chosen masking parameters and exhibits a clear trade-off between analytical validity and security.

![](/api/attachments/HGAZ2XDF/fulltext/images/e209709b4f1dcdf39d821a0dcf24d056749560cc0fb3092778bdc0fea67189d0.jpg)  
b. Scatter plot of the masked values of $( Y _ { 1 } , V _ { 1 } )$  
Fig. 4. a. Scatter plot of the original values of $( { \pmb X } _ { 1 } , { \pmb V } _ { 1 } )$ , b. Scatter plot of the masked values of $( \pmb { Y } _ { 1 } , \pmb { V } _ { 1 } ) .$

The SASH procedure described in this study is but one possible implementation of a general data sharing approach with the following specific characteristics:

(a) Predictable analytical validity and security based on a sound theoretical basis (conditional distribution approach).

(b) Flexibility in determining which (if any) attributes to share based on security considerations

(c) Robustness to distributional assumptions because much of the information exchanged is rank-based and consequently nonparametric.

(d) Better user acceptance because reverse-mapping based on randomly-ordered original data has identical marginal characteristics, alleviating concerns about “artificial data”.

(e) Clear and immediate practical utility as illustrated by the application scenarios. In particular, the shared data can be used for individual customer-level decisions rather than just group-level decisions.

The flexibility in the choice of statistical models, in particular, opens up additional avenues for research. We employed the multivariate normal copula approximation to the conditional distribution. This enabled us to preserve monotonic relationships in the shared version of the attributes. The literature shows other possible approximations. Some of these may be more appropriate for other situations such as for heavytailed distributions, non-monotonic relationships, or specific types of categorical data.

It must be noted a procedure like SASH would simply not have been possible a few years back. Several recent developments including those related to secure identification of common customers, securely sharing inter-attribute correlations belonging to different parties, research on multiple approaches to approximate conditional distributions, and research related to reverse-mapping, all contributed to the feasibility of SASH. SASH brings together these advances, in a theoretically valid fashion, to serve a clear practical purpose.

## References

[1] R.T. Clemen, Correlations and copulas for decision and risk analysis, Management Science 45 (2) (1999).

[2] T. Dalenius, Towards a methodology for statistical disclosure control, Statistisk tidskrift 5 (1977)

[3] P. Danaher, M. Smith, Modeling multivariate distributions using copulas: applications in marketing, Management Science 30 (1) (2011).

[4] W.L. Du, M.J. Atallah, Privacy-preserving Cooperative Statistical Analysis, in 17th An nual Computer Security Applications Conference, New Orleans, Louisiana, 2001

[5] G. Duncan, D. Lambert, Disclosure-limited data dissemination, Journal of the American Statistical Association 81 (393) (1986).

[6] G. Duncan, D. Lambert, The risk of disclosure for microdata, Journal of Business and Economic Statistics 7 (2) (1989).

[7] C. Dwork, A firm foundation for private data analysis, Communications of the ACM 54 (1) (2011).

[8] S. Fienberg, U. Makov, R. Steele, Disclosure limitation using perturbation and related methods for categorical data, Journal of Official Statistics 14 (2) (1998).

[9] W.A. Fuller, Masking procedures for microdata disclosure limitation, Journal of Official Statistics 9 (1993)

[10] V. Goel, How facebook sold you krill oil, The New York Times, vol. 2015, 2014.

[11] A. Ha, Facebook to roll out email-and phone number-based ad targeting next week, (2012), 2014 [(11/18)].

[12] A. Hundepool, J. Domingo-Ferrer, L. Franconi, S. Giessing, E. Nordholt, K. Spicer, P.-P. de Wolf, Statistical Disclosure Control, John Wiley & Sons, West Sussex, United Kingdom, 2012.

[13] A.F. Karr, X. Lin, A.P. Sanil, J.P.P. Reiter, Privacy-preserving analysis of vertically partitioned data using secure matrix products, Journal of Official Statistics 25 (1) (2009).

[14] S. Kotz, N. Balakrishnan, and N. Johnson, Continuous Multivariate Distributions, Eds., (New York, John Wiley & Sons, 2000).

[15] S. Lee, M. Genton, R. Arellano-Valle, Perturbation of numerical confidential data via skew-t distributions, Management Science 56 (2) (2010).

[16] H. Li, K. Muralidhar, R. Sarathy, Secure and Useful Data Sharing — Some Approaches, in INFORMS Fall 2003 Meeting, 2003 (Atlanta, 2003).

[17] N. Melville, M. McQuaid, Generating shareable statistical databases for business value: multiple imputation with multimodel perturbation, Information Systems Research 23 (2) (2012).

[18] K. Muralidhar, R. Sarathy, Data shuffling: a new masking approach for numerical data, Management Science 52 (5) (2006)

[19] K. Muralidhar, R. Sarathy, A theoretical basis for perturbation methods, Statistics and Computing 13 (4) (2003)

[20] R. Nelsen, Copulas, characterization, correlation, and counterexamples, Mathematics Magazine 68 (3) (1995).

[21] M. Palley, J. Simonoff, The use of regression methodology for the compromise of confidential information in statistical databases, ACM Transactions on Database Systems 12 (4) (1987).

[22] R. Panko, Corporate Computer and Network SecurityPrentice Hall, 2003.

[23] Y. Qian, H. Xie, Drive more effective data-based innovations: enhancing the utility of secure databases, Management Science 61 (3) (2015).

[24] T. Raghunathan, J. Reiter, D. Rubin, Multiple imputation for statistical disclosure limitation, Journal of Official Statistics 19 (1) (2003).

[25] D. Rubin, Statistical disclosure limitation, Journal of Official Statistics 9 (2) (1993).

[26] R. Sarathy, K. Muralidhar, R. Parsa, Perturbing nonnormal confidential attributes: the Copula approach, Management Science 48 (12) (2002).

[27] D. Shah, V. Kumar, K.H. Kim, Managing customer profits: the power of habits, Journal of Marketing Research 51 (6) (2014).

[28] A. Sklar, Fonctions de Répartition à n dimensions et Leurs Mages, Publications de l'Institut de Statistique de l'Universite de Paris, 81959.

[29] J. Vaidya, C. Clifton, Privacy preserving association rule mining in vertically partitioned data, Proc. of the 8th ACM SIGKDD Int'l Conference on Knowledge Discovery and Data Mining. (Edmonton. Alterta Canada 2002). 2002

[30] L.T. Willenborg, T.D. Waal, Elements of Statistical Disclosure Control, Springer, New York, 2001.

Krishnamurty Muralidhar is a Professor in the Department of Marketing & Supply Chain Management, Price College of Business at the University of Oklahoma. He received his Ph.D. from Texas A&M University. He has published articles in a variety of journals including Operations Research, Management Science, Information Systems Research, Decision Sci ences, ACM Transactions on Database Systems, International Journal of Production Research International Journal of Operations and Production Management, Journal of Management, Computers and Operations Research, Information and Management, Human Performance, Research on Accounting Ethics Journal of Business Finance and Accounting Simulation OMEGA International Iournal of Management Science, Socio-Economic Planning Sciences. Journal ot Business Ethics, and Journal of Systems Management. His current research interests include privacy and con dentiality, data masking, and data security

Rathindra Sarathy is the Ardmore Chair and Professor of Information Systems in the Spears School of Business at Oklahoma State University. He received his Ph.D. from Texas A&M University. He has published in many journals including ACM Transactions on Database Systems, Decision Sciences, Decision Support Systems, Information Systems Research, Management Science, Information Systems Journal, and Operations Research. His current research interests include privacy and confidentiality, data masking, data and information security, and e-commerce.

Han Li is currently an Associate Professor in Paseka School of Business Administration at Minnesota State University Moorhead. She received her doctorate in Management Information Systems from Oklahoma State University. She has published in Decision Support Systems, Operations Research, European Journal of Information Systems, Information Systems Journal, Journal of Computer Information Systems, Information Management & Computer Security, and Journal of Information Privacy and Security. Her current research interests include Heath IT, privacy and confidentiality, data and information security and the adoption of information technology.
