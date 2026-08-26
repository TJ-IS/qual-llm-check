---
otero_id: 2012
otero_key: "68WTEFPJ"
title: "An outlier-based data association method for linking criminal incidents"
authors: "Song Lin; Donald E. Brown"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.06.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# An outlier-based data association method for linking criminal incidents

Song Lin<sup>\*,1</sup>, Donald E. Brown

Department of Systems and Information Engineering, University of Virginia, Charlottesville, VA 22904, USA

Available online 2 October 2004

## Abstract

Serial criminals are a major threat in the modern society. Associating incidents committed by the same offender is of great importance in studying serial criminals. In this paper, we present a new outlier-based approach to resolve this criminal incident association problem. In this approach, criminal incident data are first modeled into a number of cells, and then a measurement function, called outlier score function, is defined over these cells. Incidents in a cell are determined to be associated with each other when the score is significant enough. We applied our approach to a robbery dataset from Richmond, VA. Results show that this method can effectively solve the criminal incident association problem. <sup>D</sup> 2004 Published by Elsevier B.V.

Keywords: Outlier detection; Similarity matching; Entropy; Information measures

## 1. Introduction

Data mining is a collection of techniques that can be used to reveal underlying relationships in a large amount of data. Various data mining approaches have been introduced to the crime analysis field and these have enabled crime analysts to perform some tasks more effectively than ever before.

However, many important problems remain for crime analysts that have not yet been addressed by data mining technologies. Among these is the problem of associating incident reports for crimes perpetrated by the same criminal or criminals. The most compelling examples of this problem involve associating incidents from serial or career criminals. Refs. [5,14] contain a discussion of serial criminals and an example is provided by the recent Washington, DC sniper [30]. For serious part I crimes analysts typically devote as much time as necessary to make the correct associations between incidents. Less serious crimes receive less attention and frequently go without any association at all. The failure to associate these records seriously impedes law enforcement’s ability to recognize criminal patterns and make arrests.

Several different methods have been proposed and developed to resolve this criminal incident association problem. In agencies where incidents are not well indexed, crime analysts make associations by manually comparing the incident records. For major crimes in the jurisdictions of these agencies, analysts will sometimes spread out the paper copies of the incident reports over several tables and stack the ones that seem to associate. Agencies with usable records management systems use a more automated version of this procedure by retrieving records using a series of Structured Query Language (SQL) queries. Instead of stacks on a table, they store and organize results from their queries in folders.

Other more automated approaches have been developed, but not widely used. The Integrated Criminal Apprehension Program (ICAP) [21] enables police officers to match the suspects with the arrested criminals using Modus Operandi (MO) features. In the Armed Robbery Eidetic Suspect Typing (AREST) program [2], an expert system approach is used. A potential offender can be classified into three categories: probable suspect, possible suspect, and non-suspect. The Violent Criminal Apprehension Program (ViCAP) [22] developed by the Federal Bureau of Investigation (FBI) is an incident matching system. MO factors are primarily considered in ViCAP. In the COPLINK project [10] undertaken by the researchers at the University of Arizona, a concept space model is used to link records in the database with given search terms. Brown and Hagen [7] developed similarity based methods for incident association. In testing with crime analysts, they showed that these methods outperformed the commonly used SQL query in terms of both effectiveness and efficiency.

The Brown and Hagen methods present the most formal approach to data association using similarity measures but each of the above methods either implicitly or explicitly uses measure of similarity or dissimilarity. The theoretical basis for <sup>b</sup>similaritybased<sup>Q</sup> approaches derives from results in criminology. According to the rational choice theory [11], criminals make decisions that maximize their expected return. Brantingham and Brantingham [5] claim that the environment in which criminals operate contains signals or cues (physical, spatial, cultural, etc.), and criminals use these cues to evaluate their targets and make their decisions.

According to this theory, a criminal incident is the outcome of a decision process involving a multistaged search in the awareness space of the criminal. During the search phase, the criminal associates cues, clusters of cues, or cue sequences with a <sup>b</sup>good<sup>Q</sup> target. From a crime analyst’s standpoint, these cues form a template of the criminal, and once the template is built, it is self-reinforcing and relatively enduring over the time intervals considered. Due to the cognitive limitations of human beings, a criminal normally does not have many decision templates. Therefore, when we observe criminal incidents with the similar temporal, spatial, and modus operandi features, this suggests the incidents come from the same template of the same criminal. Because of these arguments, linking incidents with similar characteristics or templates together appears to be a natural solution to finding serial criminals.

At some level of detail the template used by each criminal is unique to that criminal. Unfortunately, the data collected by the police department typically does not contain enough detail to uniquely identify a template. Given observed (recorded) attributes, some templates are <sup>b</sup>popular<sup>Q</sup> or <sup>b</sup>common<sup>Q</sup> and one of these common templates may be shared by different criminals. Hence, criminals with common templates are not differentiable. In these cases, linking incidents solely based upon their similarity may lead to erroneous decisions. On the other hand, some templates are <sup>b</sup>unusual<sup>Q</sup>. For <sup>b</sup>unusual<sup>Q</sup> or <sup>b</sup>uncommon<sup>Q</sup> templates, we are more confident in saying that incidents come from the same criminal.

As an example, consider the weapon used in a robbery incident. We may have many incidents with the value <sup>b</sup>gun<sup>Q</sup> for weapon used. However, no crime analysts would say that the same criminal committed all of these robberies because <sup>b</sup>gun<sup>Q</sup> is a common template shared by many criminals. If we observe several robbery incidents with an uncommon template, say a <sup>b</sup>Japanese sword<sup>Q</sup>, we are more confident in asserting that these incidents result from the same criminal. (This <sup>b</sup>Japanese sword<sup>Q</sup> claim was first given in Ref. [7].)

From the above discussions, we see that a good association method should consider not only whether a group of incidents are similar to each other (they result from the same template), but also whether this similarity represents uniqueness or at least distinctiveness. Incidents generated from a distinct template are more likely to be committed by the same criminal. We define an evaluation function, called the outlier score function, which we designed to measure distinctiveness. When the outlier score is large enough, we say that incidents are associated with each other. We call it an outlier score because the distinctiveness measured the outlier score is related to the concept of outliers in statistics. Before presenting the details of our association method, we first review some existing studies concerning outliers.

## 2. Related work on outliers

An outlier is an observation that is <sup>b</sup>so different from other observations as to arouse suspicions that it was generated by a different mechanism<sup>Q</sup> [20]. Traditional studies on outliers can be classified into two major categories: outlier accommodation and outlier identification. In outlier accommodation, the goal is to develop some robust estimates that are insensitive to the existence of outliers. For a univariate dataset, most outlier accommodation studies concentrate on the estimation of measures of central tendency and dispersion that are not effected by outliers. Trimming or winsorizing [3] are two commonly used techniques for estimating the location parameter, and the median absolute deviation (MAD) is suggested for estimating the dispersion parameter [18]. Some of these techniques can be generalized to the multivariate case.

Outlier identification is different from outlier accommodation. In outlier accommodation, outliers are treated as noise and considered harmful to the analysis or estimation process. In outlier identification, researchers treat outliers as meaningful signals rather than noise and this is clearly the perspective in this paper. Other examples of the need for outlier identification are found in many important applications, such as credit card fraud detection [4] and network intrusion detection [26].

Outlier detection in a univariate dataset has been extensively studied in statistics. In a univariate dataset, outliers are normally the largest or the smallest observations at the extremes of an assumed distribution. A number of tests, called discordancy tests, have been developed [3,20]. These tests include the Dixon’s test [12,13], the Rosner’s test [17] and the Grubbs’ test [15].

In these outlier detection approaches, the dataset is required to be univariate, and the dataset is generally assumed to follow some standard probabilistic distributions such as the Gaussian or Poisson distributions. However, in many real-world problems, datasets are multivariate with mixed quantitative and qualitative variables. Under these conditions, it is difficult to make assumptions about the underlying distribution. Several approaches that detect outliers in a multivariate dataset without the a priori assumptions about the distribution have recently been proposed. Knorr and Ng [24,25] introduced the notion of distance-based outliers. They call an object a $\mathrm { D B } ( p , D )$ outlier if at least a fraction of $p$ of the objects in the dataset have a distance greater than distance D. Ramaswamy et al. [29] presented the k-nearest neighbor outlier. The distance from each data point to its kth nearest neighbor is calculated. Then all data points are ranked according to the calculated distances, and the top n data points are selected as outliers. Breunig et al. [6] proposed the concept of <sup>b</sup>local<sup>Q</sup> outliers. They define the notion of the outlier factor, and for each object in the dataset they assign a score to measure the outlier level. Aggarwal et al. [1] claim that for a high-dimensional dataset, the outliers exist only in subspace projections. They use an evolutionary algorithm to find these outliers in subspaces. Unfortunately for our application, most of these approaches were developed for quantitative or numeric variables, while criminal incident databases have mostly categorical or qualitative variables.

In this paper, we extend the concept of outlier detection as part of a new method to solve the criminal incident association problem. Instead of detecting individual outliers, we wish to detect outlier groups, i.e., to associate outliers. Unlike most existing outlier detection methods, our method focuses on categorical variables. In criminal incident association analysis, most attributes, especially MO attributes, are categorical.

## 3. The outlier-based data association method

## 3.1. Definitions

In this section, we formally define the concepts and notations used in the remainder of this paper.

Let $A _ { 1 } , A _ { 2 } , . . . , A _ { m }$ be m attributes that we consider relevant to our study, and let $\smash { D _ { 1 } , D _ { 2 } , . . . , D _ { m } }$ be their domains, respectively. Currently, these attributes are confined to be categorical. Let $\boldsymbol { z } ^ { ( i ) }$ be the ith incident, and $z ^ { ( i ) } A _ { j }$ be the value on the jth attribute of incident $\boldsymbol { i } , \boldsymbol { z } ^ { ( i ) }$ can be represented as $z ^ { ( i ) } { = } ( z _ { 1 } ^ { ( i ) } , z _ { 2 } ^ { ( i ) } , . . . , z _ { m } ^ { ( i ) } )$ , where $z _ { k } ^ { ( i ) } { = } z ^ { ( i ) } A _ { k } { \in } D _ { k } , k { \in } \{ 1 , . . . , m \}$ . Z is the set of all incidents.

Definition 1. (Cell). Cell $c$ is a vector of the values of attributes with dimension $t ,$ where tVm. A cell can be represented as $c { = } c _ { i , } , \ c _ { i , } { , } . . . , \ c _ { i , }$ . In order to standardize the definition of a cell, for each $D _ { i } ,$ we add a <sup>b</sup>wildcard<sup>Q</sup> element <sup>b</sup>\*<sup>Q</sup>. <sup>b</sup>\*<sup>Q</sup> means that we do not <sup>b</sup>care<sup>Q</sup> about the attribute. Now we allow $D _ { i } { = } D _ { i } \cup \{ { * } \}$ . For cell $c { = } c _ { i _ { 1 } } , \ c _ { i _ { 2 } } { , } . \ . \ . , \ c _ { i _ { t } } ,$ we can represent it as $c { = } c _ { i _ { 1 } } , \ c _ { i _ { 2 } } { , } \ . \ . , \ c _ { i _ { m } } ,$ where $c _ { j } \in D _ { j } ^ { \prime } ,$ , and $c _ { j } { = } ^ { * }$ if and only if $j \notin \{ i _ { 1 } ,$ $i _ { 2 } , . . . , i _ { \mathrm { t } } \}$ . C denotes the set of all cells. Since each incident can also be treated as a cell, we define a function Cell: $Z { \longrightarrow } C . \mathrm { C e l l } ( z ) { = } ( z _ { 1 } , \ z _ { 2 } , . . . , \ z _ { m } ) , \ \mathrm { i f } \ z { = } ( z _ { 1 } , \ z _ { 2 } , . . . , \ z _ { m } )$ . Therefore, each cell captures characteristics of a template of one or more criminals.

The concept of cell is borrowed from the online analytical processing (OLAP) field [9]. People familiar with OLAP may find that some other notations in this paper are similar to those used in OLAP studies.

Definition 2. (Contains relation). We say that cel $c { = } ( c _ { 1 } , c _ { 2 } , . . . . , c _ { m } )$ contains incident z if and only ${ \mathrm { i f } } z _ { j } { = } c _ { j } \ { \mathrm { o r } } c _ { j } { = } ^ { * }$ $j { = } 1 , 2 , . . . . , m$ . For two cells, we say that cell $c ^ { \prime } { = } ( c _ { 1 } ^ { \prime } , c _ { 2 } ^ { \prime } { , . . . , c _ { m } ^ { \prime } } )$ contains cell $c ^ { \prime } { = } ( c _ { 1 } , c _ { 2 } , . . . . , c _ { m } )$ if and only if $\scriptstyle { c _ { j } ^ { \prime } = c _ { j } }$ or $c _ { j } ^ { \prime } { = } ^ { * } , j { = } 1 , 2 , . ~ . ~ . , m$

Definition 3. (Count of a cell). Function count is defined on a cell, and count(c) returns the number of incidents that cell c contains.

Definition 4. (Parent cell). Cell $c ^ { \prime } { = } ( c _ { 1 } ^ { \prime } , c _ { 2 } ^ { \prime } { , . . . } . , c _ { m } ^ { \prime } )$ is the parent cell of cell c on the kth attribute when: $\boldsymbol { c ^ { \prime } } _ { k } \mathrm { = } ^ { \ast }$ and $c _ { j } ^ { \prime } { = } c _ { j }$ , for $j { \neq } k .$ . Function parent(c,k) returns parent cell of cell c on the kth attribute.

Definition 5. (Neighborhood). P is called the neighborhood of cell c on the kth attribute when P is a set of cells that take the same values as cell c in all attributes but $k ,$ and does not take the wildcard value \* on the kth attribute, i.e., $P = \{ c ^ { ( 1 ) } , c ^ { ( 2 ) } , . . . , c ^ { ( | P | ) } \}$ where $c _ { l } ^ { ( i ) } { = } c _ { l } ^ { ( j ) }$ for all $l { \neq } k ,$ , and $c _ { k } ^ { ( j ) } { \neq } { ^ { \ast } }$ for all $i { = } 1 , 2 , . . . . , | P |$ . Function neighbor(c,k) returns the neighborhood of cell c on attribute k. (In the OLAP field, the neighbor is also known as <sup>b</sup>siblings<sup>Q</sup>.)

Definition 6. (Relative frequency). We call freq(c,k)=(count(c)/count(parent(c,k))) the relative frequency of cell c with respect to attribute k.

Definition 7. (Uncertainty function). We use function U to measure the uncertainty of a neighborhood. This uncertainty measure is defined on the relative frequencies. If we use $P { = } { \{ c ^ { ( 1 ) } , ~ c ^ { ( \bar { 2 } ) } , . . . , ~ c ^ { ( { | P | } ) } \} }$ to denote the neighborhood of cell c on attribute k, then the uncertainty function is as follows:

$$
U (c, k) = U \left(f r e q \left(c ^ {(1)}, k\right), f r e q \left(c ^ {(2)}, k\right), \dots , f r e q \left(c ^ {(| P |)}, k\right)\right).
$$

Obviously, U should be symmetric for all $\mathrm { f r e q } ( c ^ { ( 1 ) } , k ) , \mathrm { f r e q } ( c ^ { ( 2 ) } , k ) , . . . , \mathrm { f r e q } ( c ^ { ( | P | ) } , k )$ . U takes a smaller value if the uncertainty in the neighborhood is low. (For detailed discussion about the impact of this uncertainty function on the data association problem and why it should be taken into consideration, see Ref. [27].)

In this paper, we choose entropy as the uncertainty function. Entropy function is typically used in information theory.

$$
U (c, k) = H (c, k) = - \sum_ {c ^ {\prime} \in \text { neighbor } (c, k)} f r e q (c ^ {\prime}, k) \log (f r e q (c ^ {\prime}, k))
$$

For the $f r e q = 0 $ , we define $0 \cdot \log ( 0 ) { = } 0$ , as is common in information theory.

## 3.2. Outlier score function

A function $f \colon C { \longrightarrow } R ^ { + }$ is used to measure the distinctiveness of a cell. We call this function the outlier score function. This function is introduced for two purposes. First, it measures the extremeness of a cell. A special or uncommon cell receives a higher score. Second, it provides the accuracy level of asserting that incidents contained in a cell are associated, as the extremeness of a cell implies the distinctiveness of a template used by a specific criminal.

We build the outlier score function from studying requirements that it should satisfy. Since the outlier score function measures the accuracy of the association, the following three properties are desired.

(I) If $c ^ { ( 1 ) }$ and $c ^ { ( 2 ) }$ are two one-dimension cells, and both of them take non-\* value on the same attribute, then $f ( c ^ { ( 1 ) } ) { \ge } f ( c ^ { ( 2 ) } )$ holds if and only if $\mathsf { c o u n t } ( c ^ { ( 1 ) } ) { \ge } \mathsf { c o u n t } ( c ^ { ( 2 ) } )$ .

(II) Assume that $\boldsymbol { c } ^ { ( 1 ) }$ and $c ^ { ( 2 ) }$ are two one-dimension cells, and they take non-\* values on two different attributes, say i and $j ,$ respectively. If $( c ^ { ( 1 ) } , i ) { \geq } \mathrm { f r e q } ( c ^ { ( 2 ) } , j )$ , then $f ( c ^ { ( 1 ) } ) { \ge } \dot { f } ( c ^ { ( 2 ) } )$ holds if and only if $U ( c ^ { ( 1 ) } , i ) { \ge } U ( c ^ { ( 2 ) } , j )$ where $c ^ { ( 1 ) }$ takes non-\* value on the ith, and $c ^ { ( 2 ) }$ takes non-\* value on the $j \mathrm { t h }$ attribute, respectively. If we define the uncertainty function in an entropy format: $U ( c , k ) { = } H ( c , k )$ , then property II can be rewritten as: $f ( c ^ { ( 1 ) } ) { \ge } f ( c ^ { ( 2 ) } )$ if and only if $H ( c ^ { ( 1 ) } , i ) { \le } H ( c ^ { ( \bar { 2 } ) } , j )$

(III) ${ \hat { f } } ( c ^ { ( 1 ) } ) { \ge } { \hat { f } } ( c ^ { ( 2 ) } )$ always holds if $c ^ { ( 2 ) }$ contains $c ^ { ( 1 ) }$

These three properties can be understood as follows. The first property says that an uncommon cell provides more information (more distinctive). The second property means that the distinctiveness level of a cell is reinforced when the uncertainty level is low. The third property implies that we are more confident to associate incidents when they take the same value on <sup>b</sup>more<sup>Q</sup> attributes.

Reasons that these properties are <sup>b</sup>good<sup>Q</sup> desired properties are discussed in details in Ref. [27]. Here we only give some examples for illustration. Consider the following three scenarios.

(I) We have 100 robbery incidents. Five take the value <sup>b</sup>Japanese sword<sup>Q</sup> for the weapon-used attribute, and 95 take the value <sup>b</sup>gun<sup>Q</sup>. Obviously, the 5 <sup>b</sup>Japanese swords<sup>Q</sup> are of more interest (larger score) than the 95 $\mathrm { \ddot { \ g u n s } \vec { \Omega } }$

(II) Now we add another attribute: method-of-escape. For the method-of-escape attribute, we have 20 values: by foot, by car, etc. Each of them has 5 incidents. Although both <sup>b</sup>Japanese sword<sup>Q</sup> and <sup>b</sup>by car<sup>Q</sup> have 5 incidents, they should not be treated equally. The <sup>b</sup>Japanese sword<sup>Q</sup> is more distinctive (larger score) because all other incidents involve the use of <sup>b</sup>guns<sup>Q</sup>, or in other words, the uncertainty level of the weapon-used attribute is smaller.

(III) Now we consider these two attributes, weapon-used and method-of-escape, together. Assume that we have some incidents taking the value <sup>b</sup>Japanese sword<sup>Q</sup> on the former attribute and <sup>b</sup>by $\boldsymbol { \mathrm { c a r } ^ { \circ } }$ on the latter. The combination of <sup>b</sup>Japanese sword<sup>Q</sup> and <sup>b</sup>by $\boldsymbol { \mathrm { c a r } ^ { \circ } }$ is more significant (larger score) than either <sup>b</sup>Japanese sword<sup>Q</sup> and <sup>b</sup>by car<sup>Q</sup> by themselves. The reason is that now we have more evidence of a distinct criminal template.

An outlier score function that satisfies these properties follows:

$$
f (c) = \left\{ \begin{array}{l} \max _ { \begin{array}{l} k \text {   takes   all   non - } ^ {*} \text { dimension   of   } c \\ 0 \quad c = (*, *,.., *) \end{array} } \left(f (\text { parent } (c, k)) + \frac {- \log (\text { freq } (c , k))}{H (c , k)}\right), \end{array} \right.
$$

where c is a cell. When $H ( c , k ) { = } 0$ , we say $( - \log ( \mathrm { f r e q } ( c , k ) ) / H ( c , k ) ) { = } 0$

For details about how this function is derived, see Ref. [27]. It is simple to verify that function f satisfies the three desired properties.

We note that outlier score function has a recursive definition. Given an incident $z ,$ in order to calculate the outlier score for Cell(z), we need to calculate the outlier scores of all parent cells of z. In a similar manner, we need to calculate outlier scores for grand-parents, great-grand-parents, etc. of cell z. Therefore, all cells that contain z will be evaluated. Theoretically, if we do this for all incident-level cells, then we will get outlier scores for all nonempty (containing at least one incident) cells for a given dataset.

## 3.3. Outlier-based data association method

Now that we have a function that measures distinctiveness, we are in a position to develop a process to associate criminal incidents. Using the outlier score function, we provide the following rule to associate criminal incidents.

For a pair of incidents $z _ { 1 }$ and $z _ { 2 } ,$ if there is a cell c that contains both $z _ { 1 }$ and $z _ { 2 } ,$ and the outlier score of cell c exceeds a given threshold s, we say that these two incidents are associated with each other.

Unfortunately, this incident association rule requires checking all cells, which is computationally inefficient. Hence, we adjust the incident association decision rule as follows using some additional properties.

Definition 8. (Union). For a pair of cells $c ^ { ( 1 ) }$ and $c ^ { ( 2 ) } .$ , cell c is called the union of $\cdot _ { c } ^ { ( 1 ) }$ and $c ^ { ( 2 ) }$ when c contains both $c ^ { ( 1 ) }$ and $c ^ { ( 2 ) }$ , and for any other cell $c ^ { \prime }$ that contains $c ^ { ( 1 ) }$ and $c ^ { ( 2 ) } , c ^ { \prime }$ contains $c .$

It is simple to verify that c exists for any pair of incidents. From property III, if there is a cell whose outlier score exceeds $\tau$ then the outlier score of the union cell exceeds s, and vice versa. Hence, the incident association rule becomes:

Associate incident $z ^ { ( 1 ) }$ and $z ^ { ( 2 ) }$ if and only ${ \mathrm { i f } } f ( \mathrm { U n i o n } ( \mathrm { C e l l } ( z ^ { ( 1 ) } ) , \mathrm { C e l l } ( z ^ { ( 2 ) } ) ) > \tau$

## 4. Application

To test our approach to data association, we applied the outlier-based incident association method to a real-world crime dataset. The dataset contains information on robbery incidents that occurred in Richmond, VA in 1998. The dataset consists of two parts: the incident dataset and the suspect dataset. The incident dataset has 1198 records, and the temporal, spatial, and MO information are stored in the incident database. The name (if known), height, and weight information of the suspect are recorded in the suspect database. We applied our method to the incident dataset and used the suspect dataset for verification.

We selected robbery for this study for two reasons: first, compared with violent crimes such as murder or sexual assault, serial robberies occur more frequently; and second, compared with breaking and entering crimes, more robbery incidents are <sup>b</sup>solved<sup>Q</sup> (criminals arrested) or <sup>b</sup>partially solved<sup>Q</sup> (the suspect’s name is known). These two points made the robbery a good choice for the evaluation purpose.

## 4.1. Attribute selection

We used three types of attributes in our analysis. The first set of attributes consisted of 6 MO features. MOs are typically used in criminal incident association studies. The second set of attributes contained demographic features (demographic data was obtained from the census CD held in the library of University of Virginia). Demographic features help to reveal criminals’ preferences. For example, certain criminals prefer to attack <sup>b</sup>high-income<sup>Q</sup> areas. Lastly, we included distance features in our analysis. Distance attributes are distances from the incident location to spatial landmarks, such as a school or a major highway. Distance features are important in the analysis because they may represent the spatial preferences of criminals. Some criminals like to initiate attacks from at specific distance from major highways so that nobody can watch them during the attack and they can leave the crime scene as soon as possible after the attack. Names and descriptions of these attributes are provided in Appendix A. These attributes were also used in a previous study on predicting breaking and entering crimes [8].

We performed an attribute selection process on all numeric attributes (demographic and distance attributes) before using the outlier-based data association method. We did this because some attributes are analytically redundant. This redundancy hinders the association algorithm in terms of both efficiency and accuracy. We used clustering algorithms to pick the attributes. Specifically, we used a correlation coefficient to measure how similar or close two attributes were, and then we clustered the attributes into a number of groups according to this similarity measure. The attributes in the same group were similar to each other, and were quite different from attributes in other groups. For each group or cluster, we picked a representative attribute at the center of the cluster. The final set of all representative attributes was considered to capture the major characteristics of the dataset. A similar methodology was used in Ref. [28].

We employed the k-medoid clustering algorithm in the clustering phase of the attribute selection process. (For more details about clustering algorithms including k-medoid clustering, see Ref. [16].) The reason we picked the k-medoid clustering was because it tends to return spherical groups, and it provides the medoid (the median for high dimension case) for each group. Using these medoids, we can select the representative attributes.

For the dataset in this application, we found three clusters shown in the silhouette plot [23] in Fig. 1.

On the dataset in this application our implementation of the algorithm found the following three medoids: HUNT<sup>\_</sup>DST (housing unit density), ENRL3<sup>\_</sup>DST (public school enrollment density), and TRAN<sup>\_</sup>PC (expenses on transportation: per capita). We made some adjustments. We replaced ENRL3<sup>\_</sup>DST with another attribute POP3<sup>\_</sup>DST (population density: age 12–17). The reason was that POP3<sup>\_</sup>DST was very similar to ENRL3<sup>\_</sup>DST (with a correlation coefficient <sup>N</sup>90%) and is more meaningful in criminology. People in this age range were more likely to be both attackers and victims. For similar reasons, we replaced TRAN<sup>\_</sup>PC with MHINC (median household income).

There were a total of nine attributes used in our analysis: six MO attributes (categorical) and three numeric attributes picked by applying the attributes selection procedure. Since our method was developed on categorical attributes, we converted the numeric attributes to categorical ones by dividing them into 11 equally sized bins. The number was determined by Sturge’s number of bins rule [32,33].

## 4.2. Evaluation criteria

We consider the information in the suspect database as the <sup>b</sup>true result<sup>Q</sup>. There are a total of 170 incidents having identified suspects (<sup>b</sup>identified<sup>Q</sup> means that the name(s) of the suspect(s) is known), and these incidents were used to evaluate our method. We generated all incident pairs. If two incidents in a pair had suspects with the same name and date of birth, the <sup>b</sup>true result<sup>Q</sup> for this pair was called a <sup>b</sup>true association<sup>Q</sup>. Otherwise we called the <sup>b</sup>true result<sup>Q</sup> a <sup>b</sup>non-association<sup>Q</sup>.

![](/api/attachments/68WTEFPJ/fulltext/images/bef4198ca58579330db2c4840c579701960f3c84191a612f240e00dc33727a63.jpg)  
These two components explain 44.25 % of the point variability.  
Fig. 1. Result of the k-medoid clustering.

Two measures were used to evaluate the method. The first measure was the <sup>b</sup>true association detection rate<sup>Q</sup>.

True Association Detection Rate

Number of Detected True Associations

Total Number of True True Associations

A good data association procedure would detect a large portion of <sup>b</sup>true associations<sup>Q</sup>.

We called the second measure the <sup>b</sup>average number of relevant records<sup>Q</sup>. This measure builds on the analogy of search engines. Consider a search engine such as Google. For each search string, it returns a list of documents considered to be <sup>b</sup>relevant<sup>Q</sup> to the search criterion. Similarly, for the crime association problem, if we provide an incident to the association method, then the method will return a list of records that are considered to be associated with the given incident. A shorter list is generally preferred because we only want to be given the incidents that truly associate and nothing else. The average <sup>b</sup>length<sup>Q</sup> of the lists provided by the association method is the average number of relevant records.

The information retrieval area [31] commonly uses two related criteria in evaluating a retrieval system: recall and precision. The former is the ability of a retrieval system to find relevant items, and the latter is the ability to present only the relevant items. Our first measure is a recall-like measure, and our second measure is equivalent to a precision measure. We chose average number of relevant records as a synonym for precision because it is had more meaning to end users (crime analysts). Additionally, when developing a software system, the average number of relevant records can be used to avoid the difficulty of setting the cutoff threshold.

The above two measures, true association detection rate and the average number of relevant records work for more than criminal incident association; they can be used in evaluating any association algorithms. Therefore, we can use these two measures to compare the performance of association methods in different applications.

## 4.3. Result and comparison

To test our method we set different threshold values. Obviously, if we set it to 0, we would expect that the method could detect 100% <sup>b</sup>true associations<sup>Q</sup> but the average number of relevant records was 169 (given 170 incidents for evaluation). If we set the threshold s to infinity, we would expect the method to return 0 for both <sup>b</sup>detected true associations<sup>Q</sup> and <sup>b</sup>average number of relevant records<sup>Q</sup>. As the threshold increases, we expect a decrease in both true association detection rate and average number of relevant records. Table 1 shows the results of applying our method to the robbery dataset.

We compared this outlier-based method with a similarity-based crime association method as described in Ref. [7]. Given a pair of incidents, the similaritybased method first calculates a similarity score for each attribute, and then computes a total similarity score using the weighted average of all individual similarity scores. The total similarity score is used to determine whether the incidents are associated. The full version of the similarity-based method requires the similarity matrix given by experts as input parameters. Here we adopted the binary simplification of the similaritybased association method, as no similar matrices were provided by experts in our study. (According to a previous study [7], the performance of the binary simplification is close to the full version.) Using the same evaluation criteria, the results from the similaritybased method are given in Table 2.

Table 1  
Result of outlier-based method

<table><tr><td>Threshold</td><td>True association detection rate (%)</td><td>Average number of relevant records</td></tr><tr><td>0</td><td>100.0</td><td>169.00</td></tr><tr><td>1</td><td>97.0</td><td>121.04</td></tr><tr><td>2</td><td>90.9</td><td>62.54</td></tr><tr><td>3</td><td>69.7</td><td>28.38</td></tr><tr><td>4</td><td>54.5</td><td>13.96</td></tr><tr><td>5</td><td>48.5</td><td>7.51</td></tr><tr><td>6</td><td>24.2</td><td>4.25</td></tr><tr><td>7</td><td>6.1</td><td>2.29</td></tr><tr><td>∞</td><td>0.0</td><td>0.00</td></tr></table>

Table 2  
Result of the similarity-based method

<table><tr><td>Threshold</td><td>True association detection rate (%)</td><td>Average number of relevant records</td></tr><tr><td>0</td><td>100.0</td><td>169.00</td></tr><tr><td>0.5</td><td>100.0</td><td>112.98</td></tr><tr><td>0.6</td><td>75.7</td><td>80.05</td></tr><tr><td>0.7</td><td>45.5</td><td>45.52</td></tr><tr><td>0.8</td><td>21.2</td><td>19.38</td></tr><tr><td>0.9</td><td>0.0</td><td>3.97</td></tr><tr><td>∞</td><td>0.0</td><td>0.00</td></tr></table>

If we set the average number of relevant records as the X-axis and the true association detection rate as the Y-axis, then the comparisons are illustrated in Fig. 2.

In Fig. 2, the outlier-based method lies above the similarity-based method for most cases. That means given the same <sup>b</sup>accuracy<sup>Q</sup> (true association detection rate) level, the outlier-based method returns fewer relevant records; also if we keep the number of relevant records (average length of the returned list) the same for both methods, the outlier-based method is more powerful (detects more true associations). The curve of the similarity-based method sits slightly above the outlier-based method when the average number of relevant records is above 100. Since the size of the evaluation incident set is 170, no crime analyst would consider exerting further investigation on any set of over 100 incidents. These tables show that the outlierbased method is generally more effective. The graphs shown here are obviously similar to Receiver Operating Characteristic (ROC) curve analysis [19].

## 5. Conclusion and future work

Data association is important to crime analysts as a way to link crimes and help catch the perpetrators. In this paper, we presented an outlier-based method to solve this criminal incident association problem. The method links records through the use of a new outlier score function that measures the distinctiveness of criminal behavior as shown by the values of fields in the records management database. The values of these fields constitute a criminal’s template of behavior. When a group of incidents share the same template and the template is distinct enough so that the outlier score exceeds a certain threshold, then we say that these incidents are associated. To test this approach we applied it to a robbery dataset, and the results show that this method outperforms a similarity-based association method.

The outlier-based method provides a promising solution for the criminal incident association problem, and it could be generalized to other application areas.

![](/api/attachments/68WTEFPJ/fulltext/images/7434bd724a8716d08232b8e5f42446da3878845d5047c17c50290f622005e7f1.jpg)  
Fig. 2. Comparison: outlier-based method vs. similarity-based method.

When applying this method to datasets with more records and more attributes, some adjustments are required to keep this approach efficient and still effective. For example, some powerful commercial OLAP software programs can be introduced to speed up generating the cells. Additionally, some faster attribute selection/reduction methods should be considered. The outlier-based association method itself may also need some adjustments when dealing with large datasets, such as a top-down cell building strategy or some early termination rule. With these improvements the method could have even broader applicability.

## Appendix A. Attributes used in the analysis

<table><tr><td>Attribute name</td><td>Description</td></tr><tr><td colspan="2">(a) MO attributes</td></tr><tr><td>Rsus_Acts</td><td>Actions taken by the suspects</td></tr><tr><td>R_Threats</td><td>Method used by the suspects to threat the victim</td></tr><tr><td>R_Force</td><td>Actions that suspects force the victim to do</td></tr><tr><td>Rvic_Loc</td><td>Location type of the victim when robbery was committed</td></tr><tr><td>Method_Esc</td><td>Method of escape the scene</td></tr><tr><td>Premise</td><td>Premise to commit the crime</td></tr><tr><td colspan="2">(b) Census attributes</td></tr><tr><td colspan="2">General</td></tr><tr><td>POP_DST</td><td>Population density</td></tr><tr><td>HH_DST</td><td>Household density</td></tr><tr><td>FAM_DST</td><td>Family density</td></tr><tr><td>MALE_DST</td><td>Male population density</td></tr><tr><td>FEM_DST</td><td>Female population density</td></tr><tr><td colspan="2">Race</td></tr><tr><td>RACE1_DST</td><td>White population density</td></tr><tr><td>RACE2_DST</td><td>Black population density</td></tr><tr><td>RACE3_DST</td><td>American Indian population density</td></tr><tr><td>RACE4_DST</td><td>Asian population density</td></tr><tr><td>RACE5_DST</td><td>Other population density</td></tr><tr><td>HISP_DST</td><td>Hispanic origin population density</td></tr><tr><td colspan="2">Population age</td></tr><tr><td>POP1_DST</td><td>Population density (0–5 years)</td></tr><tr><td>POP2_DST</td><td>Population density (6–11 years)</td></tr><tr><td>POP3_DST</td><td>Population density (12–17 years)</td></tr><tr><td>POP4_DST</td><td>Population density (18–24 years)</td></tr><tr><td>POP5_DST</td><td>Population density (25–34 years)</td></tr><tr><td>POP6_DST</td><td>Population density (35–44 years)</td></tr><tr><td>POP7_DST</td><td>Population density (45–54 years)</td></tr><tr><td>POP8_DST</td><td>Population density (55–64 years)</td></tr><tr><td>POP9_DST</td><td>Population density (65–74 years)</td></tr><tr><td>POP10_DST</td><td>Population density (over 75 years)</td></tr></table>

Appendix A (continued)

<table><tr><td>Attribute name</td><td>Description</td></tr><tr><td>Householder age</td><td></td></tr><tr><td>AGEH1_DST</td><td>Density: age of householder under 25 years</td></tr><tr><td>AGEH2_DST</td><td>Density: age of householder under 25–34 years</td></tr><tr><td>AGEH3_DST</td><td>Density: age of householder under 35–44 years</td></tr><tr><td>AGEH4_DST</td><td>Density: age of householder under 45–54 years</td></tr><tr><td>AGEH5_DST</td><td>Density: age of householder under 55–64 years</td></tr><tr><td>AGEH6_DST</td><td>Density: age of householder over 65 years</td></tr><tr><td>Household size</td><td></td></tr><tr><td>PPH1_DST</td><td>Density: 1 person households</td></tr><tr><td>PPH2_DST</td><td>Density: 2 person households</td></tr><tr><td>PPH3_DST</td><td>Density: 3–5 person households</td></tr><tr><td>PPH6_DST</td><td>Density: 6 or more person households</td></tr><tr><td>Housing, misc.</td><td></td></tr><tr><td>HUNT_DST</td><td>Housing units density</td></tr><tr><td>OCCHU_DST</td><td>Occupied housing units density</td></tr><tr><td>VACHU_DST</td><td>Vacant housing units density</td></tr><tr><td>MORT1_DST</td><td>Density: owner occupied housing unit with mortgage</td></tr><tr><td>MORT2_DST</td><td>Density: owner occupied housing unit without mortgage</td></tr><tr><td>COND1_DST</td><td>Density: owner occupied condominiums</td></tr><tr><td>OWN_DST</td><td>Density: housing unit occupied by owner</td></tr><tr><td>RENT_DST</td><td>Density: housing unit occupied by renter</td></tr><tr><td>Housing structure</td><td></td></tr><tr><td>HSTR1_DST</td><td>Density: occupied structure with 1 unit detached</td></tr><tr><td>HSTR2_DST</td><td>Density: occupied structure with 1 unit attached</td></tr><tr><td>HSTR3_DST</td><td>Density: occupied structure with 2 unit</td></tr><tr><td>HSTR4_DST</td><td>Density: occupied structure with 3–9 unit</td></tr><tr><td>HSTR6_DST</td><td>Density: occupied structure with 10+ unit</td></tr><tr><td>HSTR9_DST</td><td>Density: occupied structure trailer</td></tr><tr><td>HSTR10_DST</td><td>Density: occupied structure other</td></tr><tr><td>Income</td><td></td></tr><tr><td>PCINC_97</td><td>Per capita income</td></tr><tr><td>MHINC_97</td><td>Median household income</td></tr><tr><td>AHINC_97</td><td>Average household income</td></tr><tr><td>School enrollment</td><td></td></tr><tr><td>ENRL1_DST</td><td>School enrollment density: public preprimary</td></tr><tr><td>ENRL2_DST</td><td>School enrollment density: private preprimary</td></tr><tr><td>ENRL3_DST</td><td>School enrollment density: public school</td></tr><tr><td>ENRL4_DST</td><td>School enrollment density: private school</td></tr><tr><td>ENRL5_DST</td><td>School enrollment density: public college</td></tr><tr><td>ENRL6_DST</td><td>School enrollment density: private college</td></tr><tr><td>ENRL7_DST</td><td>School enrollment density: not enrolled in school</td></tr><tr><td>Work force</td><td></td></tr><tr><td>CLS1_DST</td><td>Density: private for profit wage and salary worker</td></tr><tr><td>CLS2_DST</td><td>Density: private for non-profit wage and salary worker</td></tr><tr><td>CLS3_DST</td><td>Density: local government workers</td></tr><tr><td>CLS4_DST</td><td>Density: state government workers</td></tr><tr><td>CLS5_DST</td><td>Density: federal government workers</td></tr><tr><td>CLS6_DST</td><td>Density: self-employed workers</td></tr><tr><td>CLS7_DST</td><td>Density: unpaid family workers</td></tr><tr><td colspan="2">Consumer expenditures</td></tr><tr><td>ALC_TOB_PH</td><td>Expenses on alcohol and tobacco: per household</td></tr><tr><td>APPAREL_PH</td><td>Expenses on apparel: per household</td></tr><tr><td>EDU_PH</td><td>Expenses on education: per household</td></tr><tr><td>ET_PH</td><td>Expenses on entertainment: per household</td></tr><tr><td>FOOD_PH</td><td>Expenses on food: per household</td></tr><tr><td>MED_PH</td><td>Expenses on medicine and health: per household</td></tr><tr><td>HOUSING_PH</td><td>Expenses on housing: per household</td></tr><tr><td>PCARE_PH</td><td>Expenses on personal care: per household</td></tr><tr><td>REA_PH</td><td>Expenses on reading: per household</td></tr><tr><td>TRANS_PH</td><td>Expenses on transportation: per household</td></tr><tr><td>ALC_TOB_PC</td><td>Expenses on alcohol and tobacco: per capita</td></tr><tr><td>APPAREL_PC</td><td>Expenses on apparel: per capita</td></tr><tr><td>EDU_PC</td><td>Expenses on education: per capita</td></tr><tr><td>ET_PC</td><td>Expenses on entertainment: per capita</td></tr><tr><td>FOOD_PC</td><td>Expenses on food: per capita</td></tr><tr><td>MED_PC</td><td>Expenses on medicine and health: per capita</td></tr><tr><td>HOUSING_PC</td><td>Expenses on housing: per capita</td></tr><tr><td>PCARE_PC</td><td>Expenses on personal care: per capita</td></tr><tr><td>REA_PC</td><td>Expenses on reading: per capita</td></tr><tr><td>TRANS_PC</td><td>Expenses on transportation: per capita</td></tr><tr><td colspan="2">(c) Distance attributes</td></tr><tr><td>D_Church</td><td>Distance to the nearest church</td></tr><tr><td>D_Hospital</td><td>Distance to the nearest hospital</td></tr><tr><td>D_Highway</td><td>Distance to the nearest highway</td></tr><tr><td>D_Park</td><td>Distance to the nearest park</td></tr><tr><td>D_School</td><td>Distance to the nearest school</td></tr></table>

## References

[1] C.C. Aggarwal, P.S. Yu, Outlier detection for high dimensional data, SIGMOD Conference Proceedings, 2001.

[2] A.B. Badiru, J.M. Karasz, B.T. Holloway, AREST: Armed Robbery Eidetic Suspect Typing expert system, Journal of Police Science and Administration 16 (1988) 210– 216.

[3] V. Barnett, T. Lewis, Outliers in Statistical Data, John Wiley, New York, 1994.

[4] R.J. Bolton, D.J. Hand, Unsupervised Profiling Methods for Fraud Detection, Proceedings of Conference on Credit Scoring and Credit Control VII, 2001 (September).

[5] P.J. Brantingham, P.L. Brantingham, Patterns in Crimes, Macmillan, New York, 1984.

[6] M.M. Breunig, H.P. Kriegel, R. Ng, J. Sander, LOF: identifying density-based local outliers, Proc. ACM SIGMOD Int. Conf. on Management of Data, 2000, pp. 93 – 104.

[7] D.E. Brown, S.C. Hagen, Data association methods with applications to law enforcement, Decision Support Systems 34 (2003) 369– 378.

[8] D.E. Brown, H. Liu, Y. Xue, Mining preference from spatial– temporal data, Proc. of the First SIAM International Conference of Data Mining, 2001.

[9] S. Chaudhuri, U. Dayal, An overview of data warehousing and OLAP technology, ACM SIGMOD Record 26 (1) (1997 March) 65–74.

[10] H. Chen, D. Zeng, H. Atabakhsh, W. Wyzga, J. Schroeder, COPLINK managing law enforcement data and knowledge, Communications of the ACM 46 (2003 January) 28– 34.

[11] R.V. Clarke, D.B. Cornish, Modeling offender’s decisions: a framework for research and policy, in: M. Tonry, N. Morris (Eds.), Crime Justice: An Annual Review of Research, vol. 6, University of Chicago Press, Chicago, 1985, pp. 147– 186.

[12] W.J. Dixon, Analysis of extreme values, Annals of Mathematical Statistics 21 (1950) 488 – 506.

[13] W.J. Dixon, Ratios involving extreme values, Annals of Mathematical Statistics 22 (1951) 68 – 78.

[14] S.A. Egger, The Killers among Us: An Examination of Serial Murder and Its Investigation, 2nd edition, Prentice Hall, New Jersey, 2002.

[15] Environmental Protection Agency, Statistical Training Course for Ground-Water Monitoring Data Analysis, EPA/530-R-93- 003, Office of Solid Waste, Washington, DC, 1992.

[16] B. Everitt, Cluster Analysis, John Wiley & Sons, New York, 1993.

[17] R.D. Gibbons, Statistical Methods for Groundwater Monitoring, John Wiley & Sons, New York, 1994.

[18] F.R. Hampel, The influence curve and its role in robust estimation, Journal of American Statistics Association 69 (1974) 383–393.

[19] J.A. Hanley, Receiver operating characteristic (ROC) methodology: the state of the art, Critical Reviews in Diagnostic Imaging 29 (1989) 307 – 335.

[20] D. Hawkins, Identifications of Outliers, Chapman and Hall, London, 1980.

[21] R.O. Heck, Career Criminal Apprehension Program: Annual Report, Office of Criminal Justice Planning, Sacramento, CA, 1991.

[22] D.J. Icove, Automated crime profiling, Law Enforcement Bulletin 55 (1986) 27– 30.

[23] L. Kaufman, P. Rousseeuw, Finding Groups in Data, Wiley, New York, 1990.

[24] E. Knorr, R. Ng, A unified notion of outliers: properties and computation, Proceedings of the International Confer-

ence on Knowledge Discovery and Data Mining (1997) 219– 222.

[25] E. Knorr, R. Ng, Algorithms for Mining Distance-based Outliers in Large Datasets, VLDB Conference Proceedings, 1998, September.

[26] A. Lazarevic, L. Ertoz, V. Kumar, A. Ozgur, J. Srivastava, Comparative Study of Anomaly Detection Schemes in Network Intrusion Detection, Proc. of the 3rd SIAM Conference on Data Mining, 2003.

[27] S. Lin, Outlier-based Method for Data Association, Dissertation in Systems and Information Engineering, University of Virginia (2003).

[28] P. Mitra, C.A. Murthy, S.K. Pal, Unsupervised feature selection using feature similarity, IEEE Transactions on Pattern Analysis and Machine Intelligence 24 (2002) 301– 312.

[29] S. Ramaswamy, R. Rastongi, K. Shim, Efficient Algorithms for Mining Outliers from Large Data Sets, Proc. of the ACM SIGMOD Conference, 2000, pp. 427–438.

[30] M. Ruane, S. Horwitz, Sniper: Inside the Hunt for the Killers Who Terrorized the Nation, 1st edition, Random House, New York, 2003.

[31] G. Salton, M. McGill, Introduction to Modern Information Retrieval, McGraw-Hill Book, New York, 1983.

[32] D. Scott, Multivariate Density Estimation: Theory, Practice and Visualization, Wiley, New York, 1992.

[33] H.A. Sturges, The choice of a class interval, Journal of American Statistician Association 21 (1926) 65 – 66.

![](/api/attachments/68WTEFPJ/fulltext/images/a152aea7499b51f4765ca86696ace04df2033f69ff447b1d9fb4ea1bce3b20ec.jpg)

Dr. Lin received his B.S. degree in Management Information Systems from Tsinghua University (P.R. China), the M.S. degree in Management Science and Engineering from the School of Economics and Management, Tsinghua University (P.R. China) and the Ph.D. degree in Systems and Information Engineering from University of Virginia. His research interest is statistical analysis/data mining.

![](/api/attachments/68WTEFPJ/fulltext/images/24ece74c7147f5fdb94f2df1d3a7515caa7ff9436fc50c11936191dba6a86d0c.jpg)

Dr. Brown is Professor and Chair of the Department of Systems Engineering, University of Virginia and a Fellow of the IEEE. He received his B.S. degree from the United States Military Academy, West Point, the M.S. and M.Eng. Degrees in Operations Research from the University of California, Berkeley and the Ph.D. degree in Industrial and Operations Engineering from the University of Michigan,

Ann Arbor. His research is statistical learning and predictive modeling.
