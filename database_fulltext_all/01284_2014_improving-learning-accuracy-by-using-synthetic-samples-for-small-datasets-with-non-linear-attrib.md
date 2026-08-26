---
otero_id: 1284
otero_key: "5FTTNAZM"
title: "Improving learning accuracy by using synthetic samples for small datasets with non-linear attribute dependency"
authors: "Der-Chiang Li; Liang-Sian Lin; Li-Jhong Peng"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.12.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving learning accuracy by using synthetic samples for small datasets with non-linear attribute dependency

Der-Chiang Li ⁎, Liang-Sian Lin, Li-Jhong Peng

Department of Industrial and Information Management, National Cheng Kung University, University Road, Tainan 70101, Taiwan, ROC

## a r t i c l e i n f o

Article history: Received 22 July 2012 Received in revised form 13 September 2013 Accepted 26 December 2013 Available online 5 January 2014

Keywords: Small dataset Attribute dependency Related virtual samples Gene expression programming Mega trend diffusion

## a b s t r a c t

Small-data problems are commonly encountered in the early stages of a new manufacturing procedure, presenting challenges to both academics and practitioners, as good performance is dif<sup>fi</sup>cult to achieve with learning models when there is a lack of suf<sup>fi</sup>cient data. Virtual sample generation (VSG) has been shown to be an effective method to overcome this issue in a wide range of studies in various <sup>fi</sup>elds. Such works usually assume that the relations among attributes are independent of each other, and produce synthetic data by using sample distributions of these. However, the VSG technique may be ineffective if the real data has interrelated attributes. Therefore, this research provides a novel procedure to generate related virtual samples with non-linear attribute dependency. To construct a relational model between the independent and dependent attributes, we employ gene expression programming (GEP) to <sup>fi</sup>nd the most suitable mathematical model. One practical dataset and three real UCI datasets are presented in this paper to verify the effectiveness of the proposed method, and the results show that the proposed approach has better learning accuracy with regard to a back-propagation neura (BPN) network than that of the well-known mega-trend-diffusion (MTD) and the multi regression analysis (MRA) approaches.

© 2014 Elsevier B.V. All rights reserved

## 1. Introduction

Many enterprises operating in a very competitive global market would produce products with shorter life cycles for more demanding customers. In the electronics industry, in particular, which is generally very capital intensive, a critical strategy is to reduce pilot runs before mass production in order to maintain a high equipment running rate. Consequently, obtaining meaningful information from a small number of observations in the early stages of a production plan remains very important and a challenging issue.

The problem addressed in this work is de<sup>fi</sup>ned here as small dataset learning, in which the number of observations is usually less than 30, and thus gaps among data exist making it dif<sup>fi</sup>cult for traditional statistical methods to reach robust conclusions. An effective approach in this kind of small dataset learning is to <sup>fi</sup>ll the information gaps by systematically generating virtual samples. Li et al. [11] proposed the use of a functional virtual population as a way to solve small dataset scheduling learning problems in the early stages of manufacturing. Huang and Moraga [5] suggested the use of diffusion-neural-network (DNN), which utilizes information diffusion and Fuzzy Theory to derive new samples for arti<sup>fi</sup>cial neural networks. Li et al. [14] combined data growth trend estimation with a mega-fuzzi<sup>fi</sup>cation approach to estimate the domain bounds considering the data distribution. In addition, a mega-trend-diffusion (MTD) technique, proposed by Li et al. [15], was developed based on the DNN to make the domain bounds estimates more precise. MTD is one of the most widely applied VSG approaches, and its effectiveness has been demonstrated in several real cases [9,10,13,17].

However, since the correlations among attributes are not considered in MTD, when the arti<sup>fi</sup>cial samples are produced, the estimated behavior pattern of small datasets may become disordered. As illustrated in Fig. 1, where (a) shows a non-linearly related behavior pattern between variables X and Y, and (b) indicates that the behavior becomes less correlated.

To date, researchers have not yet developed a VSG technique for the generation of dependent virtual samples. Consequently, based on the consideration of non-linear attribute dependency, this research aims to systematically generate interrelated virtual samples to improve the accuracy of small data learning. We propose a novel procedure which differs from existing VSG techniques to produce both independent and dependent virtual samples to better <sup>fi</sup>t the pattern of real data. Based on the relations among attributes, we identify and group the independent and dependent attributes, and employ the maximal information compression index (MICI) to construct a relational diagram of attributes. To further explore the relations among the independent and dependent attributes, we use gene expression programming (GEP) proposed by Ferreira [2] to construct a non-linear mathematical model, in which the expression tree can represent the non-linear relationships among variables. When obtaining an evaluated model from GEP, we can produce dependent virtual samples by inputting the virtual samples with independent attributes into the model. In addition, we develop a process to produce independent virtual samples by modifying the generated values of the membership function in the MTD method.

![](/api/attachments/5FTTNAZM/fulltext/images/d8959eb91e9582007868f3534d17fe0036e04fea558a712a64e4446ed160620e.jpg)  
(a)

![](/api/attachments/5FTTNAZM/fulltext/images/8e719279978bfa8e7b478da505a773984a7a36e50d043b337e99fcf21e87fd3d.jpg)  
(b)  
Fig. 1. The scatter plot (a) shows a non-linear pattern, and (b) indicates disorder with added virtual samples.

In order to demonstrate the effectiveness of the proposed method, we use one practical process dataset from a Thin Film Transistor-Liquid Crystal Display (TFT-LCD) factory in Taiwan and three real datasets, downloaded from the UCI Machine Learning Repository database [1], namely the Concrete Compressive Strength Data Set (CCS), the Istanbul Stock Exchange Data Set (ISE), and the Yacht Hydrodynamics Data Set (YH), to implement the small dataset analysis. With regard to the selection of the learning tool, a back-propagation neural (BPN) network is used as the basis to carry out the small dataset prediction. In addition, we use the Mean Absolute Percentage Error (MAPE) and Root Mean Square Error (RMSE) to assess the prediction accuracy. Finally, the results of t-tests show that the proposed method is statistically and signi<sup>fi</sup>cantly better than the MTD and MRA (multi regression analysis) approaches.

The remainder of this research is organized as follows: Section 2 brie<sup>fl</sup>y introduces the concept gene expression programming, while

Section 3 presents the proposed procedure and explains the production of interrelated arti<sup>fi</sup>cial samples in detail. Section 4 offers one practical example and three real datasets to validate the effectiveness of the proposed method, and Section 5 discusses the conclusions derived from this paper, and presents some suggestions for further research.

## 2. Gene expression programming (GEP)

In 1975, Holland developed genetic algorithms (GAs) in the <sup>fi</sup>eld of arti<sup>fi</sup>cial intelligence, based on concepts drawn from organic evolution [6], and it have subsequently been applied in many <sup>fi</sup>elds, such as computational science, engineering, and manufacturing. A GA is basically a search heuristic algorithm, which generates solutions and then searches for the optimal one by the operations of mutation, crossover, and inversion, as shown in Fig. 2. The initial population is generated by individuals, and the best-<sup>fi</sup>tting chromosomes of these are then chosen to the reproduction, thus creating the next generation with the aid of the processes of crossover, mutation and inversion processes, and new populations are continuously produced until the preset termination conditions are satis<sup>fi</sup>ed.

Koza [7] developed the genetic programming (GP), a machine learning technology that is a speci<sup>fi</sup>c application of GAs, and the genetic operators of GP act directly on the non-linear structures of problems to <sup>fi</sup>nd an optimal solution. Ferreira [2] then proposed the gene expression programming (GEP) technique, which is a genome/phenome genetic algorithm for linear and non-linear problems based on GAs and GP. In the evolutionary process, GEP incorporates linear chromosomes of <sup>fi</sup>xed length and nonlinear parse trees with different sizes and shapes in order to improve the ef<sup>fi</sup>ciency of the related calculations. Logically, GEP is a tree type algorithm similar to a Boolean string. The concept of evolution is used in GEP to obtain an optimal solution by building the model tree of a cause-effect dataset by using the <sup>fi</sup>tness function, transposition, and mutation of a huge number of generations.

![](/api/attachments/5FTTNAZM/fulltext/images/c032d4dc32bf2136b69786db4fb56d0b5bf000019f19052aa95e800710442ad5.jpg)  
Fig. 2. The diagram of GA procedure.

## 2.1. Expression tree (ET)

GEP solutions are expressed as a tree frame called an expression tree (ET), which is formed with functional (inner) and terminal (leaf) nodes. The functional nodes consist of mathematical functions, operator symbols, and Boolean operators. The terminal nodes include all variables and constants. For instance, the ET of the algebraic expression ${ \sqrt { ( a + b ) \times ( a - b ) } }$ can be represented as shown in Fig. 3.

<sup>Þþ - ð Þ</sup>The leaf and inner nodes of ET include variables {a,b} and operator symbols $\{ 0 , * , + , - \}$ , respectively, where 'Q' means the square root function. The diagram representation is the phenotype of GEP individuals, while the other kind of representation is the genotype which is inferred from the phenotype, as follows:

$$
\begin{array}{l} 0 1 2 3 4 5 6 7 \\ \text { Q } * + - a b a b. \end{array}\tag{1}
$$

This is the direct reading of ET from top to bottom and from left to right. Eq. (1) is an open reading frame (ORF), where the <sup>fi</sup>rst row of numbers means the positions, such that the start is 'Q' (position 0) and the terminal is 'b' (position 7). The ORF is known as the K-expression, based on the KARVA language.

## 2.2. GEP genes and chromosomes

The GEP genes consist of heads (h) and tails (t), where a head includes both operator (function) and variable (terminal) symbols, and a tail includes only variable (terminal) symbols. The length of a gene is the sum of the head and tail length. For a problem, the length of a head is h, and the length of a tail is t, where t is computed by $\operatorname { E q } . \left( 2 \right)$ composed of h and n as the number of arguments of the function.

$$
t = h \cdot (n - 1) + 1\tag{2}
$$

Given a gene composed of the operator set $\{ + , - , * , / , Q \}$ , variable $\mathsf { s e t } = \{ a , b \}$ , and $n = 2$ , if h = 8 and t = 9, then the length of the gene is $8 + 9 = 1 7$ , based on Eq. (2), and the gene is shown below with the tail shown in bold:

01234567890123456 Q –=b baaabbbaaa

![](/api/attachments/5FTTNAZM/fulltext/images/ffe290a90e8ebd94d08cf956ffc5ef0d5a5ecbfdef9bacd47789422c4474d61f.jpg)  
Fig. 3. An ET of GEP.

![](/api/attachments/5FTTNAZM/fulltext/images/143b3b50527bf189e36fbfb95e54d41fca338b63030650db55c4a7cc44726a22.jpg)  
Fig. 4. The sub-ETs codi<sup>fi</sup>ed by the respective genes

In general, more than one gene with an equal length can construct a GEP chromosome. For instance, a GEP chromosome with the length of 27 consists of three genes with a length of 9, which has three ORFs and codes for the three sub-ETs, as shown in Fig. 4, where the start of each gene is marked at position zero and the end of each ORF is observed in the individual sub-ET.

The ET of multi-genic chromosomes is the result of posttranslational linking with addition (+) or other operators. For instance linking with addition (+), the mathematical equation of multi-genic chromosomes is expressed as:

$$
[ a + (a * b) ] + \left[ \sqrt {a + b} \right] + \left[ a - \frac {a}{b} \right].
$$

![](/api/attachments/5FTTNAZM/fulltext/images/f565a166631c980b885556b7683a073471d5a1e41bcf5cc1d190e77bd51192f1.jpg)  
Fig. 5. Diagram of the proposed procedure.

## 2.3. Selection, replication, mutation, transposition, and recombination

The GEP algorithm is based on the mechanism of organic evolution, with natural selection and survival of the <sup>fi</sup>ttest. There is an elimination mechanism in the evolutionary procedure, which is the <sup>fi</sup>tness function that generates the <sup>fi</sup>tness value to determine the degree of improvement in the next generations.

There are three common methods that can be used to select the individuals that will be used to produce the next generations in GEP: Roulette Wheel Selection [3], Tournament [4], and Ranking [18]. Ferreira [2] used Roulette Wheel Selection to obtain a percentage representing the probability that an individual i will be selected, calculated as:

$$
\frac {f (X _ {i})}{\sum_ {i = 1} ^ {n} f (X _ {i})}\tag{3}
$$

where $f ( X _ { i } )$ is the <sup>fi</sup>tness value of an individual i, and $\Sigma _ { i } ^ { n } { = } 1 f ( X _ { i } )$ is the sum of all the <sup>fi</sup>tness values of all the individuals. As in organic evolution, when an individual has a high <sup>fi</sup>tness value, the probability that it will be selected increases.

The selected individuals will be replicated in the next generation, while the unselected ones will be directly eliminated. In this way we can then obtain the optimal solution through mutation, transposition, and recombination.

Mutations may occur anywhere in the chromosome, although its structural organization must stay intact. If mutations occur in a head, any symbol (operator or variable) can change into any other; on the other hand, if mutations occur in a tail, variables can only change into variables. Typically, a mutation rate is set in GEP to present the probability of encoding mutations of chromosomes.

The GEP improves the variance of a gene by building the transposition rule of gene elements; the fragments of a genome can be moved to another place in the chromosome to enhance the evolutionary ability. The parent generation produces the next generation through recombination, of which there are three kinds: 1-point, 2-point, and gene recombination.

## 3. The proposed procedure

The proposed procedure, as shown in Fig. 5, is described as follows: First, utilize the maximal information compression index (MICI) [16] to identify the relations between the independent and dependent attributes, and group the attributes into several subsets. Second, employ GEP to construct a mathematical model tree to describe the nonlinear relations between attributes. Third, produce the virtual samples of independent attributes by MTD, and obtain the corresponding values of dependent attributes by the expression trees. Finally, we add the resulting related virtual dataset into the original dataset to be as a new training dataset of a predictive BPN model.

## 3.1. Identify and group the attributes

In manufacturing processes, the relations among attributes are usually not independent of each other. Therefore, to explore these, we use the MICI to identify and group these attributes into two subsets, and then use the subsets to construct the relational diagram by the following steps. We assume that a dataset X has N samples and f variables, denoted as $X = \left\{ \widetilde { X } _ { 1 } , \widetilde { X } _ { 2 } , . . . , \widetilde { X } _ { f } \right\}$

The de<sup>fi</sup>nitions and operation types of the symbols in GEP.

<table><tr><td>Symbols</td><td>Definition</td><td>Operation type</td><td>Arity</td></tr><tr><td>+</td><td>Addition</td><td>A+B</td><td>2</td></tr><tr><td>-</td><td>Subtraction</td><td>A-B</td><td>2</td></tr><tr><td>*</td><td>Multiplication</td><td>A*B</td><td>2</td></tr><tr><td>/</td><td>Division</td><td>A/B</td><td>2</td></tr><tr><td>Q</td><td>Rooting number</td><td> $\sqrt{A}$ </td><td>1</td></tr></table>

![](/api/attachments/5FTTNAZM/fulltext/images/c4d0c6cdd1579412f3edc756291a86074079b3586df200d2955ba4c7b7f8af32.jpg)  
Fig. 6. MTD fuzzy membership function.

<sup>¼</sup>p 1. Normalize each attribute $\widetilde { X } _ { j } = \{ x _ { 1 } , x _ { 2 } , . . . , x _ { N } \} , j = 1 , 2 , . . . , f$ in the dataset, as:

$$
\frac {x _ {i} - x _ {\mathrm{max}}}{x _ {\mathrm{max}} - x _ {\mathrm{min}}}
$$

where $x _ { \mathrm { m a x } }$ and $x _ { \mathrm { m i n } }$ are the maximum and minimum in the set $\{ x _ { 1 } , x _ { 2 } , . . . , x _ { N } \} ,$ , respectively.

Step 2. Calculate the values of MICI between the attributes, as:

$$
\begin{array}{l} \lambda \left(\widetilde {X} _ {i}, \widetilde {X} _ {j}\right) \\ = \frac {\operatorname{var} \left(\widetilde {X} _ {i}\right) + \operatorname{var} \left(\widetilde {X} _ {j}\right) - \sqrt {\left(\operatorname{var} \left(\widetilde {X} _ {i}\right) + \operatorname{var} \left(\widetilde {X} _ {j}\right)\right) ^ {2} - 4 \operatorname{var} \left(\widetilde {X} _ {i}\right) \cdot \operatorname{var} \left(\widetilde {X} _ {j}\right) \cdot \left(1 - \rho \left(\widetilde {X} _ {i} , \widetilde {X} _ {j}\right) ^ {2}\right)}}{2} \end{array}\tag{4}
$$

for all $i , j = 1 , 2 , . . . . f$ and $i \neq j ,$ where the $\ " \boldsymbol { \nabla } \ b { \mathrm { d } } \boldsymbol { \Gamma } ^ { \prime \prime }$ means the variance of samples, and the symbol ρ is the coef<sup>fi</sup>cient of correlation between variables. The value of λ means the degree of relation between $\widetilde { X } _ { i }$ and ${ \widetilde { X } } _ { j } ,$ and when the value of λ is large, the degree of relation is considered weak, which indicates that the variables are independent. In addition, $\lambda = 0$ means that the attributes are linearly dependent.

Step 3. Compute the average of MICI by $\textstyle \overline { { \lambda } } = \sum _ { i , j = 1 } ^ { f } \lambda \left( \widetilde { X } _ { i } , \widetilde { X } _ { j } \right) / ( i - 1 ) , i \neq j$ <sup>¼</sup>as a criterion to select the highly related attribute pairs whose values of MICI are smaller than λ. This means that the similarity between the two attributes is high, and the similar attributes will be linked together to form a relational diagram.

Step 4. Use the following principles to determine the independent and the dependent attributes.

(1) The attributes that are not included in the relational diagram are considered to be the independent ones, because no other attributes can be used to construct them.

(2) In the relational diagram, the attributes that do not connect with each other are also considered independent.

(3) The remaining attributes are considered dependent.

![](/api/attachments/5FTTNAZM/fulltext/images/5f9e607a8d8b44bdeb92caf601321ea401b11b8bc5dafdcf4b92335c2b889017.jpg)  
Fig. 7. Calculating the MF value of tv.

![](/api/attachments/5FTTNAZM/fulltext/images/a6f43ac44a3cd643fbc0d72980d3ea0dcdf5b8c3356b0d848b9c12266ace8fb7.jpg)  
Fig. 8. The structure of the f → k → 1 BPN.

## 3.2. Build GEP model trees of dependent attributes

The dependent attributes that connect with the independent ones are considered as having high dependence on the independent attributes. In order to build the relational function between the dependent and independent attributes, we input the independent attributes into the GEP to construct model trees of the dependent ones.

## 3.2.1. Define the GEP nodes

The functional and terminal nodes of the Expression Tree (ET) are set by using GEP to construct the mathematical model. For example, the genetic operators set $\{ + , - , * , / , \mathbb { Q } \}$ means selecting plus, minus, times, divide, and rooting to be the functional nodes, as listed in Table 1.

The objective of GEP is to <sup>fi</sup>nd the mathematical relations among attributes for the generation of synthetic attribute values. We thus select arithmetical units for the quantitative data in this study, and use the key units to increase operational ef<sup>fi</sup>ciency.

## 3.2.2. Determine the adaptation function

The adaptation function plays the key role of correcting the direction of the evolution of all the attributes in GEP. We employ the Root Mean Square Error (RMSE) as the adaptation function in this paper, which is expressed as:

$$
f _ {i} = \sqrt {\frac {1}{T} \sum_ {j = 1} ^ {T} \left(y _ {i j} - y _ {j} ^ {*}\right)}\tag{5}
$$

where $f _ { i }$ is the value of the adaptation function of the i-th chromosome, y is the calculated value of the j-th sample in the i-th chromosome, and $y _ { j } ^ { * }$ is the observed value of the j-th sample in the non-selected attributes.

The relational matrix of attributes.

<table><tr><td></td><td> $\tilde{X}_{1}$ </td><td> $\tilde{X}_{2}$ </td><td> $\tilde{X}_{3}$ </td><td> $\tilde{X}_{4}$ </td><td> $\tilde{X}_{5}$ </td><td> $\tilde{X}_{6}$ </td></tr><tr><td> $\tilde{X}_{1}$ </td><td></td><td>0.245</td><td>0.360</td><td>0.108</td><td>0.193</td><td>0.167</td></tr><tr><td> $\tilde{X}_{2}$ </td><td>0.245</td><td></td><td>0.245</td><td>0.285</td><td>0.203</td><td>0.171</td></tr><tr><td> $\tilde{X}_{3}$ </td><td>0.360</td><td>0.245</td><td></td><td>0.258</td><td>0.201</td><td>0.226</td></tr><tr><td> $\tilde{X}_{4}$ </td><td>0.108</td><td>0.285</td><td>0.258</td><td></td><td>0.118</td><td>0.139</td></tr><tr><td> $\tilde{X}_{5}$ </td><td>0.193</td><td>0.203</td><td>0.201</td><td>0.118</td><td></td><td>0.281</td></tr><tr><td> $\tilde{X}_{6}$ </td><td>0.167</td><td>0.171</td><td>0.226</td><td>0.139</td><td>0.281</td><td></td></tr></table>

![](/api/attachments/5FTTNAZM/fulltext/images/ca9fe28e546fe581e732c421a3de74debf751998a39ec3b14079c0ec2ff06959.jpg)  
Fig. 9. The relational diagram of attributes.

## 3.2.3. Iteration termination and a random numerical item

In order to obtain the most suitable population, we set the R-square threshold as a termination condition with the updating evolution process. The R-square means the proportion of explained variability of the input variables for the estimated GEP model trees, and is calculated as:

$$
R _ {i} = \frac {n \sum_ {j = 1} ^ {n} T _ {j} P _ {i , j} - \left(\sum_ {j = 1} ^ {n} T _ {j}\right) \left(\sum_ {j = 1} ^ {n} P _ {i , j}\right)}{\sqrt {\left[ n \sum_ {j = 1} ^ {n} T _ {j} ^ {2} - \left(\sum_ {j = 1} ^ {n} T _ {j}\right) ^ {2} \right] \left[ n \sum_ {j = 1} ^ {n} P _ {i , j} ^ {2} - \left(\sum_ {j = 1} ^ {n} P _ {i , j}\right) ^ {2} \right]}}\tag{6}
$$

where $P _ { i , j }$ is the predicted value from the individual model i, and $T _ { j }$ is the actual value with the j-th iteration. In this work, we set the range of the R-square threshold $R _ { i }$ from 0.8 to 0.9 to avoid too many runs for the generation of updated populations.

When the input variables and genetic operators of the model trees are selected, numerical constants are usually needed to handle the mathematical building blocks in the GEP technique. The constant variable is set as a random numerical item, and it is a set C to be added into the terminal set $\{ + , - , * , / , \mathrm { Q } \}$ for each gene, where the values in the set C can be assigned in the GEP expression tree.

## 3.3. The proposed production procedure of virtual samples

MTD is a useful technique for extending small datasets, and is used for data with independent attributes. MTD basically applies Fuzzy Theory to create a membership function to represent the independent attribute samples with one peak population, as shown in Fig. 6. It utilizes the fuzzy membership function to predict the lower and upper bounds of the population and produces virtual samples within the bounds based on a uniform distribution with the relative value of the membership function (MF).

![](/api/attachments/5FTTNAZM/fulltext/images/9a27544d31a3940f205f85dab58d4c59790012d02a1cb06489bd36a30175e439.jpg)  
Fig. 10. All the relations of the attribute $\widetilde { X } _ { 6 } .$

No. Independent attributes Dependent attributes Predicted output  
![](/api/attachments/5FTTNAZM/fulltext/images/b2fe74ef749a3a2e508ac0b23c96eef27912bc7f125ed6ad2e82a78c4cda1efe.jpg)  
Fig. 11. Production procedure of related virtual data.

The evaluated lower and upper extremes (L and U) of the observation group are calculated as:

$$
L = \left\{ \begin{array}{l l} \frac {\min + \max}{2} - \frac {N _ {L}}{N _ {L} + N _ {U}} \times \sqrt {- 2 \times \hat {s} _ {x} ^ {2} / N _ {L} \times \ln \left(1 0 ^ {- 2 0}\right)} & , L \leq \min, \\ \min & , L > \min, \end{array} \right.\tag{7}
$$

$$
U = \left\{ \begin{array}{l l} \frac {\min + \max}{2} + \frac {N _ {U}}{N _ {L} + N _ {U}} \times \sqrt {- 2 \times \hat {s} _ {x} ^ {2} / N _ {U} \times \ln \left(1 0 ^ {- 2 0}\right)} & , U \geq \max, \\ \max & , U <   \max, \end{array} \right.\tag{8}
$$

where $u _ { s e t } = ( \mathrm { m a x } + \mathrm { m i n } ) / 2$ , max and min mean the maximum and the minimum values of the training samples, $N _ { L }$ and $N _ { U }$ indicate the number of samples which are smaller and bigger than $u _ { s e t } ,$ respectively. $N _ { L } / ( N _ { L } + N _ { U } )$ and $N _ { U } / ( N _ { L } + N _ { U } )$ stand for the skewness of the triangular membership function. In addition $\hat { s } _ { x } ^ { 2 } = \sum _ { i = 1 } ^ { n } { ( x _ { i } - \overline { { x } } ) } ^ { 2 } / { ( n - 1 ) }$ means the <sup>¼</sup>variance of the sample set, n means the sample size, and $\ln ( 1 0 ^ { - 2 0 } )$ means the diffusion coef<sup>fi</sup>cient.

![](/api/attachments/5FTTNAZM/fulltext/images/f730e224f3679102e60ca196486f685a5da241d1eae8464210de11f6ca4188b6.jpg)  
Fig. 12. Three main steps in the TFT-LCD process.

We propose a reasonable process of virtual value <sup>fi</sup>lling, as described in detail in the following steps:

Step 1. Calculate the possible lower (L) and upper (U) bounds of the independent attributes.

Step 2. Randomly generate samples within the corresponding estimated lower and upper bounds and evaluate the MF value of the sample by the following equation:

$$
\mathrm{MF} = \left\{ \begin{array}{l l} 1 & , t v = u _ {s e t} \\ \frac {t v - L}{u _ {s e t} - L} & , t v <   u _ {s e t} \\ \frac {U - t v}{U - u _ {s e t}} & , t v > u _ {s e t} \end{array} \right.\tag{9}
$$

where tv is a random sample from the interval [L,U].

Step 3. Randomly generate a stochastic chaotic number within the interval [0,1] to be a seed value which is then compared with the MF value of $t \nu ,$ if the MF value of tv is bigger than this seed value, tv is kept as the synthetic sample, otherwise tv is abandoned.

![](/api/attachments/5FTTNAZM/fulltext/images/7af08d30985aa25cc1e3a089d1481e657980516d6f5616b6932867a161e62c65.jpg)  
Fig. 13. The six guide-lines on one glass for LCD panel assembly.

Table 3  
The 19 records obtained from the Department of Quality Certi<sup>fi</sup>cates.

<table><tr><td>No.</td><td>V1</td><td>V2</td><td>H1</td><td>H2</td><td>D1</td><td>D2</td><td>Y</td></tr><tr><td>1</td><td>0.995</td><td>1.123</td><td>1.465</td><td>2.387</td><td>0.683</td><td>1.6452</td><td>1.1087</td></tr><tr><td>2</td><td>0.088</td><td>-0.678</td><td>-0.6555</td><td>-0.1265</td><td>-0.8885</td><td>0.4444</td><td>1.599</td></tr><tr><td>3</td><td>0.3785</td><td>-0.174</td><td>-0.5715</td><td>-0.0625</td><td>-0.26</td><td>0.0994</td><td>1.1971</td></tr><tr><td>4</td><td>0.537</td><td>0.634</td><td>1.725</td><td>2.316</td><td>1.094</td><td>1.0937</td><td>1.3663</td></tr><tr><td>5</td><td>1.07</td><td>1.281</td><td>0.315</td><td>1.023</td><td>1.059</td><td>0.4035</td><td>1.2692</td></tr><tr><td>6</td><td>1.1705</td><td>-0.063</td><td>0.132</td><td>0.414</td><td>0.941</td><td>-0.0083</td><td>1.8788</td></tr><tr><td>7</td><td>1.987</td><td>1.395</td><td>1.419</td><td>2.896</td><td>1.381</td><td>1.9795</td><td>1.1183</td></tr><tr><td>8</td><td>2.015</td><td>1.441</td><td>0.701</td><td>1.85</td><td>1.739</td><td>1.0101</td><td>1.0731</td></tr><tr><td>9</td><td>2.3</td><td>1.074</td><td>0.446</td><td>1.602</td><td>1.455</td><td>0.479</td><td>1.0913</td></tr><tr><td>10</td><td>-0.256</td><td>-1.857</td><td>-0.246</td><td>-1.1275</td><td>-0.5855</td><td>0.4568</td><td>1.5067</td></tr><tr><td>11</td><td>0.778</td><td>-0.979</td><td>0.418</td><td>0.951</td><td>0.337</td><td>-0.4092</td><td>0.9798</td></tr><tr><td>12</td><td>1.847</td><td>0.963</td><td>1.651</td><td>2.16</td><td>2.162</td><td>1.5899</td><td>1.2962</td></tr><tr><td>13</td><td>1.596</td><td>0.945</td><td>1.405</td><td>1.993</td><td>2.03</td><td>1.3277</td><td>0.9471</td></tr><tr><td>14</td><td>0.017</td><td>0.1815</td><td>-0.208</td><td>-0.3185</td><td>0.5185</td><td>-0.0378</td><td>1.9577</td></tr><tr><td>15</td><td>1.409</td><td>-0.034</td><td>0.649</td><td>0.74</td><td>1.515</td><td>-0.0221</td><td>1.4135</td></tr><tr><td>16</td><td>0.8025</td><td>-1.749</td><td>-0.472</td><td>-0.5025</td><td>-0.2805</td><td>0.8255</td><td>1.2865</td></tr><tr><td>17</td><td>0.4945</td><td>-0.1145</td><td>-0.5975</td><td>0.441</td><td>-0.5775</td><td>0.0684</td><td>1.1923</td></tr><tr><td>18</td><td>1.747</td><td>0.945</td><td>1.32</td><td>2.481</td><td>1.45</td><td>1.2474</td><td>1.6904</td></tr><tr><td>19</td><td>1.833</td><td>1.401</td><td>1.11</td><td>2.34</td><td>1.177</td><td>1.5551</td><td>1.0894</td></tr></table>

Table 4  
UCI dataset description.

<table><tr><td>Datasets</td><td>No. instances</td><td>No. attributes</td><td>Attribute characteristics</td></tr><tr><td>CCS</td><td>1030</td><td>9</td><td>Real</td></tr><tr><td>ISE</td><td>536</td><td>7</td><td>Real</td></tr><tr><td>YH</td><td>308</td><td>6</td><td>Real</td></tr></table>

Step 4. Repeat steps 2 and 3 until suf<sup>fi</sup>cient virtual samples are obtained.

When the MF value of tv is bigger, the probability of tv being the synthetic sample increases, and the value <sup>fi</sup>lling process makes the distribution of the virtual samples close to the membership function, as shown in Fig. 7, which is generally more reasonable than the results that are obtained directly with a random process.

When completing the proposed procedure, we can generate virtual samples with attribute independency, and input these data into the GEP mathematical model trees to produce related virtual samples based on the estimated functions of dependent attributes. Finally, we merge the virtual samples of independent attributes and the related virtual samples to be a new virtual dataset with non-linear attribute dependency.

## 3.4. Build the BPN model

The <sup>fi</sup>rst arti<sup>fi</sup>cial neural network (ANN) was proposed by Rosenblatt in 1957. With regard to network structures, there are three types: forward, feed forward, and feedback. Each network is composed of many interconnected arti<sup>fi</sup>cial neurons, and the neuron can perform functional calculations or logistical determinations. When obtaining computational results from neurons, the results are inputted to each other with weight adaptation learning to minimize the errors between the actual target and the output value of the network. Kumar [8] divided ANN models into four categories: supervised, unsupervised, associative memory, and optimization application learning networks, based on the learning algorithm used. The back-propagation neural (BPN) networks, one kind of supervised learning feedback network, is the most popular ANN model for data analyses. The structure of a typical BPN network is separated into three layers, as shown in Fig. 8.

The input layer expresses the f input variables, where the number of process units f is determined by the problem. The hidden layer expresses the interaction of the input variables, and the number of nodes k is determined by the test method. The output layer has one output variable. In this paper, we employ the BPN network to be the predictive model.

In order to explain the process of the BPN network, we assume that a training dataset has N samples and f attributes denoted as $T = \{ ( X _ { 1 } ,$ $y _ { 1 } ) , ( X _ { 2 } , y _ { 2 } ) , . . . , ( X _ { N } , y _ { N } ) \}$ , where each sample $X _ { i } , i = 1 , . . . , N$ has f attributes (means tha $X _ { i } = \{ x _ { i 1 } , x _ { i 2 } , . . . , x _ { i f } \}$ and x are the values of j attributes in X ), y is the target value of $\dot { X } _ { i } ,$ , and the q-th forward training operations of neuron j are propagated to each s-th layer as follows:

$$
v _ {j} (q) = \sum_ {i = 1} ^ {N _ {s - 1}} x _ {i} (q) \times w _ {i j} (q) + \theta_ {j} (q) \quad \text { and } \quad y _ {j} (q) = f \Big (v _ {j} (q) \Big), j = 1,..., N _ {s}\tag{10}
$$

where $N _ { s \mathrm { ~ - ~ } 1 }$ is the node size in the s-th layer, $w _ { i j }$ is the synaptic weight connecting the i-th to the j-th neurons, $\theta _ { j }$ is the bias at the j-th neuron, and f(x) is the sigmoid activation function for neurons in the s-th layer, as:

$$
f (x) = \frac {1}{1 + e ^ {- \lambda x}}.\tag{11}
$$

In the backward pass, we consider an error function $E ( w ) = 0 . 5 \times$ $\sum _ { j = 1 } ^ { N _ { s } } \left( y _ { j } ( q ) - \hat { y } _ { j } ( q ) \right) ^ { 2 }$ to differentiate the continuous weight vector to solve the unconstrained optimization problem of minimizing the error function, where $\hat { y } _ { j }$ is the output value of the network and y<sub>j</sub> is the actual target.

## 3.5. An example for production of virtual samples

In this section, we present a dataset with six attributes $X =$ $\left\{ \widetilde { X } _ { 1 } , \widetilde { X } _ { 2 } , \widetilde { X } _ { 3 } , \widetilde { X } _ { 4 } , \widetilde { X } _ { 5 } , \widetilde { X } _ { 6 } \right\}$ and one output variable Y to explain the proposed procedure in detail using the following steps:

Step 1. Use the MICI calculated from Eq. (4) to set up the relational matrix of attributes, where we can obtain the λ 0:213, as <sup>¼</sup>shown in Table 2, the values in bold are all smaller than 0.213.

The MAPE of predictions for the case data.

<table><tr><td> $N_V$ </td><td colspan="2">10</td><td colspan="2">20</td><td colspan="2">30</td><td colspan="2">40</td><td colspan="2">50</td><td>-</td></tr><tr><td>No.</td><td>PM</td><td>MTD</td><td>PM</td><td>MTD</td><td>PM</td><td>MTD</td><td>PM</td><td>MTD</td><td>PM</td><td>MTD</td><td>BPN</td></tr><tr><td>1</td><td>32.48</td><td>40.40</td><td>33.37</td><td>26.42</td><td>19.04</td><td>27.99</td><td>30.78</td><td>29.79</td><td>29.63</td><td>32.88</td><td>39.19</td></tr><tr><td>2</td><td>26.27</td><td>33.85</td><td>37.82</td><td>32.07</td><td>28.20</td><td>31.13</td><td>22.05</td><td>33.57</td><td>20.89</td><td>29.47</td><td>40.96</td></tr><tr><td>3</td><td>31.97</td><td>37.91</td><td>24.28</td><td>25.34</td><td>22.14</td><td>29.77</td><td>23.40</td><td>22.30</td><td>24.69</td><td>24.86</td><td>38.81</td></tr><tr><td>4</td><td>26.35</td><td>25.15</td><td>21.10</td><td>25.57</td><td>18.22</td><td>30.21</td><td>17.93</td><td>33.86</td><td>22.34</td><td>23.87</td><td>23.96</td></tr><tr><td>5</td><td>27.75</td><td>27.50</td><td>23.39</td><td>28.69</td><td>25.82</td><td>29.79</td><td>24.14</td><td>34.41</td><td>20.61</td><td>25.84</td><td>25.84</td></tr><tr><td>6</td><td>33.11</td><td>26.67</td><td>27.50</td><td>37.48</td><td>23.29</td><td>27.11</td><td>17.25</td><td>37.57</td><td>22.27</td><td>28.27</td><td>31.40</td></tr><tr><td>7</td><td>28.28</td><td>31.71</td><td>23.24</td><td>30.40</td><td>29.62</td><td>30.55</td><td>26.52</td><td>33.07</td><td>26.52</td><td>28.56</td><td>30.15</td></tr><tr><td>8</td><td>24.10</td><td>32.45</td><td>23.31</td><td>39.56</td><td>30.81</td><td>34.74</td><td>20.06</td><td>33.10</td><td>21.99</td><td>31.09</td><td>29.39</td></tr><tr><td>9</td><td>28.06</td><td>31.78</td><td>26.08</td><td>32.93</td><td>29.57</td><td>39.00</td><td>28.36</td><td>31.09</td><td>23.23</td><td>25.94</td><td>36.32</td></tr><tr><td>10</td><td>33.18</td><td>28.38</td><td>30.73</td><td>32.91</td><td>26.90</td><td>28.78</td><td>19.84</td><td>35.22</td><td>17.98</td><td>20.39</td><td>31.08</td></tr></table>

The RMSE of predictions for the case data.

<table><tr><td rowspan="2"> $N_V$ No.</td><td colspan="2">10</td><td colspan="2">20</td><td colspan="2">30</td><td colspan="2">40</td><td colspan="2">50</td><td>-</td></tr><tr><td>PM</td><td>MTD</td><td>PM</td><td>MTD</td><td>PM</td><td>MTD</td><td>PM</td><td>MTD</td><td>PM</td><td>MTD</td><td>BPN</td></tr><tr><td>1</td><td>0.42</td><td>0.54</td><td>0.43</td><td>0.33</td><td>0.25</td><td>0.38</td><td>0.41</td><td>0.39</td><td>0.36</td><td>0.42</td><td>0.51</td></tr><tr><td>2</td><td>0.34</td><td>0.43</td><td>0.49</td><td>0.41</td><td>0.37</td><td>0.41</td><td>0.28</td><td>0.42</td><td>0.27</td><td>0.38</td><td>0.52</td></tr><tr><td>3</td><td>0.39</td><td>0.47</td><td>0.31</td><td>0.32</td><td>0.30</td><td>0.38</td><td>0.30</td><td>0.28</td><td>0.31</td><td>0.31</td><td>0.50</td></tr><tr><td>4</td><td>0.34</td><td>0.30</td><td>0.29</td><td>0.33</td><td>0.23</td><td>0.36</td><td>0.25</td><td>0.44</td><td>0.28</td><td>0.31</td><td>0.29</td></tr><tr><td>5</td><td>0.34</td><td>0.33</td><td>0.30</td><td>0.36</td><td>0.33</td><td>0.38</td><td>0.30</td><td>0.43</td><td>0.27</td><td>0.33</td><td>0.33</td></tr><tr><td>6</td><td>0.43</td><td>0.33</td><td>0.36</td><td>0.47</td><td>0.30</td><td>0.34</td><td>0.22</td><td>0.49</td><td>0.27</td><td>0.37</td><td>0.41</td></tr><tr><td>7</td><td>0.36</td><td>0.39</td><td>0.29</td><td>0.40</td><td>0.36</td><td>0.40</td><td>0.34</td><td>0.41</td><td>0.34</td><td>0.37</td><td>0.39</td></tr><tr><td>8</td><td>0.33</td><td>0.43</td><td>0.31</td><td>0.51</td><td>0.40</td><td>0.43</td><td>0.28</td><td>0.42</td><td>0.28</td><td>0.38</td><td>0.36</td></tr><tr><td>9</td><td>0.36</td><td>0.39</td><td>0.33</td><td>0.44</td><td>0.39</td><td>0.48</td><td>0.37</td><td>0.39</td><td>0.29</td><td>0.34</td><td>0.46</td></tr><tr><td>10</td><td>0.42</td><td>0.36</td><td>0.38</td><td>0.42</td><td>0.34</td><td>0.37</td><td>0.25</td><td>0.43</td><td>0.24</td><td>0.25</td><td>0.40</td></tr></table>

Step 2. Construct the relational diagram. In the diagram, we consider the variables $\widetilde { X } _ { 1 } , \widetilde { X } _ { 2 }$ and ${ \widetilde { X } } _ { 3 }$ to be independent attributes, and $\widetilde { X } _ { 4 } , \widetilde { X } _ { 5 }$ and ${ \widetilde { X } } _ { 6 }$ to be dependent ones, as shown in Fig. 9.

Step 3. Use the independent attributes $\left\{ \widetilde { X } _ { 1 } , \widetilde { X } _ { 2 } , \widetilde { X } _ { 3 } \right\}$ to build the GEP model trees for the dependent attributes $\left\{ \widetilde { X } _ { 4 } , \widetilde { X } _ { 5 } , \widetilde { X } _ { 6 } \right\}$ . In this paper, with regard to setting the parameters of GEP, we set the head size h at 8, the number of arguments of the function n at 2, the mutation rate at 0.00206, the R-square threshold at 0.85, the numerical error item $C \in [ - 1 0 , 1 0 ] ,$ , and the terminal nodes are $\left\{ \widetilde { X } _ { 1 } , \widetilde { X } _ { 2 } , \widetilde { X } _ { 3 } , C \right\}$ . Here, we use the ${ \widetilde { X } } _ { 6 }$ attribute as an example to show the process, as shown in Fig. 10.

Step 4. Generate 50 virtual samples in the independent attributes set $\left\{ \widetilde { X } _ { 1 } , \widetilde { X } _ { 2 } , \widetilde { X } _ { 3 } \right\}$ by using the MTD technique, and then input these into the evaluated model trees to produce related virtual samples of dependent attributes $\left\{ \widetilde { X } _ { 4 } , \widetilde { X } _ { 5 } , \widetilde { X } _ { 6 } \right\}$ . Then combine $\left\{ \widetilde { X } _ { 1 } , \widetilde { X } _ { 2 } , \widetilde { X } _ { 3 } \right\}$ and $\left\{ \widetilde { X } _ { 4 } , \widetilde { X } _ { 5 } , \widetilde { X } _ { 6 } \right\}$ to predict output Y, as shown in Fig. 11.

## 4. Experiments

In this section we provide a practical case and three UCI datasets to illustrate the proposed method (PM). GeneXpro Tools (4.0.954 Enterprise Edition) is applied to the GEP method, and the freeware WEKA (http://www.cs.waikato.ac.nz/ml/WEKA/) is used to construct the BPN's predictive model.

## 4.1. Practical case and UCI datasets

The experiment data is the process data of a TFT-LCD factory in Taiwan. There are three main steps in the LCD process, as shown in Fig. 12. Step 1: assemble the Thin Film Transistor (TFT) glass and Color Filter (CF) glass. Step 2: cut the assembled glass to be the LCD panel.

t-Test results for the case data from PM and MTD.

<table><tr><td rowspan="2"> $N_V$ </td><td rowspan="2">Method</td><td colspan="3">MAPE</td><td colspan="3">RMSE</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>p-Value</td><td>Mean</td><td>Standard deviation</td><td>p-Value</td></tr><tr><td rowspan="2">10</td><td>PM</td><td>29.15</td><td>3.27</td><td>0.28</td><td>0.37</td><td>0.04</td><td>0.39</td></tr><tr><td>MTD</td><td>31.58</td><td>4.90</td><td></td><td>0.40</td><td>0.07</td><td></td></tr><tr><td rowspan="2">20</td><td>PM</td><td>27.08</td><td>5.33</td><td>0.09</td><td>0.35</td><td>0.07</td><td>0.09</td></tr><tr><td>MTD</td><td>31.14</td><td>4.85</td><td></td><td>0.40</td><td>0.06</td><td></td></tr><tr><td rowspan="2">30</td><td>PM</td><td>25.36</td><td>4.50</td><td>0.01*</td><td>0.33</td><td>0.06</td><td>0.02*</td></tr><tr><td>MTD</td><td>30.91</td><td>3.51</td><td></td><td>0.39</td><td>0.04</td><td></td></tr><tr><td rowspan="2">40</td><td>PM</td><td>23.03</td><td>4.49</td><td>0.00*</td><td>0.30</td><td>0.06</td><td>0.00*</td></tr><tr><td>MTD</td><td>32.40</td><td>4.13</td><td></td><td>0.41</td><td>0.05</td><td></td></tr><tr><td rowspan="2">50</td><td>PM</td><td>23.02</td><td>3.28</td><td>0.02*</td><td>0.29</td><td>0.04</td><td>0.03*</td></tr><tr><td>MTD</td><td>27.12</td><td>3.68</td><td></td><td>0.35</td><td>0.05</td><td></td></tr></table>

![](/api/attachments/5FTTNAZM/fulltext/images/3df6d740b38ee90d50d18f6bd7ed836761df343b242c672b2512249ad1dde554.jpg)  
Fig. 14. The trend chart of MAPE means of PM, MTD, and BPN.

Step 3. Measure the assembly shift (y) of the LCD panel. The assembly shift (y) is due to the differences among the six guide-lines for LCD panel assembly, as shown in Fig. 13. In order to construct the predictive model, we detect the difference between the real data and the speci<sup>fi</sup>cation of the six guide-lines to be the input variables (V1, V2, H1, H2, D1, D2), and assign the assembly shift (y) to be the output variable. In this case, the small dataset learning problem is solved with the 19 pilot run records in the early stage of a manufacturing system, as shown in Table 3.

Furthermore, the employed three datasets are the Concrete Compressive Strength Data Set (CCS), the Istanbul Stock Exchange Data Set (ISE), and the Yacht Hydrodynamics Data Set (YH), all downloaded from the UCI Machine Learning Repository database [1], to demonstrate the performance of the proposed method. The details of the three datasets are summarized in Table 4.

## 4.2. Implementation of experiment

The case data has a small sample size, and since this dataset is not suitable for separating, we adopt the leave one out method, which has the advantage of keeping most original samples. With regard to the UCI datasets, to design the experiment for small dataset analysis, we randomly sample data to generate small sets from the original data, and use the rest as the testing data. This paper sets the training data size $N _ { T }$ forward in order as 20, 40, 60, 80, 100, 125, and 150 in the UCI datasets. The determination of virtual sample size is based on Li et al. [12], which stated that too many virtual samples would decrease the learning accuracy. In order to verify the improved predictive accuracy achieved with small dataset learning in this work, the related experiment is carried out by the following three steps:

Step 1: Divide the data into training and testing samples and produce virtual samples at $N _ { V } = \{ 1 0 , 2 0 , 3 0 , 4 0 , 5 0 \}$ for the case data and $N _ { V } = \{ 5 0 , 1 0 0 \}$ for the three UCI datasets.

![](/api/attachments/5FTTNAZM/fulltext/images/c2e4d3814766898e20736ca3e91021396a76667ca11fd90adbcf087c4101895b.jpg)  
Fig. 15. The trend chart of RMSE means of PM, MTD, and BPN

<table><tr><td rowspan="2">Dataset</td><td rowspan="2"> $N_T$ </td><td colspan="2"> $N_V = 50$ </td><td colspan="2"> $N_V = 100$ </td></tr><tr><td>MAPE</td><td>RMSE</td><td>MAPE</td><td>RMSE</td></tr><tr><td rowspan="7">CCS</td><td>20</td><td>0.000*</td><td>0.020*</td><td>0.000*</td><td>0.058</td></tr><tr><td>40</td><td>0.000*</td><td>0.002*</td><td>0.000*</td><td>0.000*</td></tr><tr><td>60</td><td>0.000*</td><td>0.103</td><td>0.012*</td><td>0.009*</td></tr><tr><td>80</td><td>0.418</td><td>0.184</td><td>0.189</td><td>0.011*</td></tr><tr><td>100</td><td>0.110</td><td>0.701</td><td>0.003*</td><td>0.168</td></tr><tr><td>125</td><td>0.001*</td><td>0.095</td><td>0.001*</td><td>0.004*</td></tr><tr><td>150</td><td>0.000*</td><td>0.12</td><td>0.000*</td><td>0.111</td></tr><tr><td>Dataset</td><td> $N_T$ </td><td>MAPE</td><td>RMSE</td><td>MAPE</td><td>RMSE</td></tr><tr><td rowspan="7">ISE</td><td>20</td><td>0.038*</td><td>0.001*</td><td>0.250</td><td>0.113*</td></tr><tr><td>40</td><td>0.404</td><td>0.000*</td><td>0.951</td><td>0.000*</td></tr><tr><td>60</td><td>0.206</td><td>0.000*</td><td>0.661</td><td>0.000*</td></tr><tr><td>80</td><td>0.031*</td><td>0.000*</td><td>0.136</td><td>0.000*</td></tr><tr><td>100</td><td>0.631</td><td>0.000*</td><td>0.915</td><td>0.000*</td></tr><tr><td>125</td><td>0.890</td><td>0.000*</td><td>0.753</td><td>0.000*</td></tr><tr><td>150</td><td>0.819</td><td>0.000*</td><td>0.080</td><td>0.000*</td></tr><tr><td rowspan="7">YH</td><td>20</td><td>0.002*</td><td>0.025*</td><td>0.007*</td><td>0.296</td></tr><tr><td>40</td><td>0.000*</td><td>0.001*</td><td>0.000*</td><td>0.002*</td></tr><tr><td>60</td><td>0.000*</td><td>0.000*</td><td>0.000*</td><td>0.000*</td></tr><tr><td>80</td><td>0.000*</td><td>0.000*</td><td>0.000*</td><td>0.000*</td></tr><tr><td>100</td><td>0.000*</td><td>0.000*</td><td>0.000*</td><td>0.000*</td></tr><tr><td>125</td><td>0.000*</td><td>0.000*</td><td>0.000*</td><td>0.000*</td></tr><tr><td>150</td><td>0.000*</td><td>0.000*</td><td>0.000*</td><td>0.000*</td></tr></table>

Table 9

Step 2: Input the virtual samples and original training data to the BPN to construct the predictive model, then put the test data to the model and repeat 10 times (the validation process is repeated 19 times) for the case data and 30 times for UCI datasets to obtain the mean prediction error using Eqs. (12) and (13).

Step 3: Adopt t-tests to analyze the differences in predictive performances among the different methods, including PM, MTD, and MRA.

In this paper, the MAPE and RMSE are used to be the prediction error indicators, de<sup>fi</sup>ned as:

$$
\mathrm{MAPE} = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {\left| y _ {i} - \hat {y} _ {i} \right|}{y _ {i}} \times 100 \%\tag{12}
$$

$$
\mathrm{RMSE} = \sqrt {\frac {\sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) ^ {2}}{n}}\tag{13}
$$

where n is the number of observations, y is the observed value, and y^ is the predicted value.

## 4.3. The results and statistical tests

The prediction errors of the experiments using different numbers of virtual samples for different methods are presented here, with both the case data and UCI datasets.

## 4.3.1. Results of the case data

With different numbers of virtual samples, $N _ { V } = \{ 1 0 , 2 0 , 3 0 , 4 0 , 5 0 \}$ the values of MAPE and RMSE from 10 experiments are listed in Tables 5 and 6.

Table 7 shows the means, standard deviations, and p-values of MAPE and RMSE, where the p-values are the results of t-tests between PM and MTD. Note that ‘\*’ indicates that the MAPE and RMSE have statistically signi<sup>fi</sup>cant differences (p-value b 0.05). As shown in Tables 5 to 7, the experimental results with regard to MAPE and RMSE indicate that the predictive performance of PM is statistically superior to that of other methods.

Table 8  
The MAPE of predictions for the UCI data.

<table><tr><td rowspan="2">Dataset</td><td> $N_V$ </td><td colspan="3">50</td><td colspan="3">100</td></tr><tr><td> $N_T$ </td><td>PM</td><td>MTD</td><td>MRA</td><td>PM</td><td>MTD</td><td>MRA</td></tr><tr><td rowspan="7">CCS</td><td>20</td><td>38.09</td><td>55.95</td><td>83.22</td><td>37.24</td><td>57.32</td><td>73.95</td></tr><tr><td>40</td><td>34.87</td><td>48.91</td><td>73.95</td><td>35.24</td><td>47.69</td><td>69.61</td></tr><tr><td>60</td><td>32.43</td><td>38.36</td><td>59.84</td><td>33.19</td><td>38.99</td><td>65.38</td></tr><tr><td>80</td><td>32.23</td><td>33.42</td><td>63.31</td><td>32.38</td><td>35.26</td><td>64.32</td></tr><tr><td>100</td><td>30.49</td><td>31.31</td><td>63.55</td><td>29.20</td><td>32.47</td><td>61.12</td></tr><tr><td>125</td><td>28.04</td><td>31.84</td><td>61.21</td><td>27.76</td><td>32.16</td><td>56.99</td></tr><tr><td>150</td><td>27.07</td><td>32.27</td><td>60.65</td><td>26.13</td><td>31.91</td><td>63.66</td></tr><tr><td>Dataset</td><td> $N_T$ </td><td>PM</td><td>MTD</td><td>MRA</td><td>PM</td><td>MTD</td><td>MRA</td></tr><tr><td rowspan="7">ISE</td><td>20</td><td>390.66</td><td>498.25</td><td>481.47</td><td>461.53</td><td>535.12</td><td>490.26</td></tr><tr><td>40</td><td>321.76</td><td>344.46</td><td>515.23</td><td>352.97</td><td>354.72</td><td>476.79</td></tr><tr><td>60</td><td>325.03</td><td>349.21</td><td>441.02</td><td>310.15</td><td>317.74</td><td>330.47</td></tr><tr><td>80</td><td>314.19</td><td>372.82</td><td>560.85</td><td>319.09</td><td>343.41</td><td>364.23</td></tr><tr><td>100</td><td>332.36</td><td>342.10</td><td>429.93</td><td>322.91</td><td>324.69</td><td>415.84</td></tr><tr><td>125</td><td>305.06</td><td>307.84</td><td>467.70</td><td>322.33</td><td>327.24</td><td>568.60</td></tr><tr><td>150</td><td>304.74</td><td>308.25</td><td>443.52</td><td>290.43</td><td>320.76</td><td>333.46</td></tr><tr><td rowspan="7">YH</td><td>20</td><td>64.84</td><td>73.73</td><td>85.46</td><td>59.73</td><td>76.26</td><td>88.08</td></tr><tr><td>40</td><td>59.62</td><td>69.20</td><td>84.22</td><td>48.79</td><td>68.73</td><td>83.35</td></tr><tr><td>60</td><td>38.99</td><td>65.04</td><td>81.32</td><td>28.60</td><td>55.81</td><td>83.84</td></tr><tr><td>80</td><td>23.81</td><td>57.36</td><td>74.13</td><td>26.25</td><td>48.80</td><td>75.97</td></tr><tr><td>100</td><td>29.08</td><td>48.33</td><td>70.80</td><td>25.26</td><td>47.78</td><td>71.19</td></tr><tr><td>125</td><td>14.68</td><td>39.98</td><td>65.97</td><td>14.64</td><td>34.86</td><td>68.12</td></tr><tr><td>150</td><td>16.23</td><td>33.11</td><td>62.09</td><td>12.31</td><td>32.89</td><td>65.60</td></tr></table>

Table 10  
p-Values of t-test based on MAPE and RMSE.

The RMSE of predictions for the UCI data.

<table><tr><td rowspan="2">Dataset</td><td> $N_V$ </td><td colspan="3">50</td><td colspan="3">100</td></tr><tr><td> $N_T$ </td><td>PM</td><td>MTD</td><td>MRA</td><td>PM</td><td>MTD</td><td>MRA</td></tr><tr><td rowspan="7">CCS</td><td>20</td><td>15.53</td><td>18.77</td><td>24.39</td><td>15.47</td><td>18.92</td><td>21.11</td></tr><tr><td>40</td><td>13.34</td><td>16.70</td><td>21.37</td><td>12.30</td><td>16.39</td><td>20.18</td></tr><tr><td>60</td><td>11.65</td><td>15.64</td><td>18.65</td><td>11.70</td><td>13.80</td><td>18.40</td></tr><tr><td>80</td><td>11.57</td><td>12.26</td><td>18.57</td><td>11.15</td><td>12.32</td><td>17.87</td></tr><tr><td>100</td><td>11.13</td><td>11.29</td><td>18.06</td><td>10.83</td><td>11.54</td><td>17.49</td></tr><tr><td>125</td><td>10.31</td><td>10.86</td><td>18.00</td><td>10.03</td><td>11.02</td><td>16.59</td></tr><tr><td>150</td><td>10.12</td><td>10.85</td><td>17.03</td><td>10.10</td><td>10.78</td><td>17.15</td></tr><tr><td>Dataset</td><td> $N_T$ </td><td>PM</td><td>MTD</td><td>MRA</td><td>PM</td><td>MTD</td><td>MRA</td></tr><tr><td rowspan="7">ISE</td><td>20</td><td>0.018</td><td>0.021</td><td>0.024</td><td>0.019</td><td>0.021</td><td>0.023</td></tr><tr><td>40</td><td>0.015</td><td>0.019</td><td>0.023</td><td>0.016</td><td>0.018</td><td>0.022</td></tr><tr><td>60</td><td>0.015</td><td>0.018</td><td>0.021</td><td>0.015</td><td>0.018</td><td>0.020</td></tr><tr><td>80</td><td>0.015</td><td>0.017</td><td>0.022</td><td>0.015</td><td>0.018</td><td>0.020</td></tr><tr><td>100</td><td>0.014</td><td>0.017</td><td>0.020</td><td>0.014</td><td>0.017</td><td>0.021</td></tr><tr><td>125</td><td>0.014</td><td>0.016</td><td>0.019</td><td>0.014</td><td>0.017</td><td>0.022</td></tr><tr><td>150</td><td>0.014</td><td>0.016</td><td>0.018</td><td>0.014</td><td>0.017</td><td>0.018</td></tr><tr><td rowspan="7">YH</td><td>20</td><td>0.71</td><td>0.87</td><td>1.38</td><td>0.72</td><td>0.79</td><td>1.24</td></tr><tr><td>40</td><td>0.36</td><td>0.63</td><td>1.23</td><td>0.38</td><td>0.64</td><td>1.26</td></tr><tr><td>60</td><td>0.24</td><td>0.62</td><td>1.17</td><td>0.18</td><td>0.63</td><td>1.22</td></tr><tr><td>80</td><td>0.17</td><td>0.61</td><td>1.18</td><td>0.17</td><td>0.61</td><td>1.21</td></tr><tr><td>100</td><td>0.21</td><td>0.59</td><td>1.25</td><td>0.16</td><td>0.61</td><td>1.19</td></tr><tr><td>125</td><td>0.08</td><td>0.34</td><td>1.16</td><td>0.08</td><td>0.61</td><td>1.24</td></tr><tr><td>150</td><td>0.10</td><td>0.40</td><td>1.52</td><td>0.08</td><td>0.60</td><td>1.22</td></tr></table>

In addition, the trend charts of the MAPE and RMSE means of PM, MTD, and BPN versus the virtual sample sizes are shown in Figs. 14 and 15, where the BPN prediction uses only the original data. These trend charts show the differences of MAPE and RMSE means among PM, MTD, and BPN when increasing the virtual sample size.

## 4.3.2. Results of the UCI data

We experiment 30 times using the CCS, ISE, and YH datasets by setting the two virtual sample sizes at 50 and 100 with different training data sizes $N _ { T } = \{ 2 0 , 4 0 , 6 0 , 8 0 , 1 0 0 , 1 2 5 , 1 5 0 \}$ . The values in Tables 8 and

9 are the means of MAPE and RMSE from PM, MTD, and MRA (multi regression analysis). In order to compare the predictive performance among the three methods, we use t-tests to examine the experiment results, as shown in Table 10.

## 4.4. Summary

Based on these results, as shown in Tables 5 to 10, we can summarize the proposed method as follows: <sup>fi</sup>rst, the PM including the processes of GEP and MTD has signi<sup>fi</sup>cant improvements in prediction accuracy when using small datasets compared to MTD and MRA. Second, when the number of virtual samples becomes larger, there are more signi<sup>fi</sup>cant differences between PM and MTD based on the MAPE and RMSE. Third, with regard to the ISE dataset, the MAPE values are not suitable to assess the predictive performance, as the output values are very small.

## 5. Conclusions and suggestions for future research

Research has shown that the VSG technique, which produces virtual samples of independent attributes, can effectively enhance learning performance for small datasets. However, because real datasets usually have non-linear attribute dependency, one problem with the VSG approach is its inability to generate related virtual samples. Therefore, in this work we combine the GEP with MTD to create a non-linear relational model among interrelated attributes, and use the estimated model to produce related virtual samples to expand small datasets. With the case data and UCI datasets, the results show that the proposed method can signi<sup>fi</sup>cantly improve the analytical performance for small dataset learning in the comparison with the MTD and MRA methods.

In future research, one can explore other real cases to further verify the effectiveness of the proposed method. Another direction is to undertake veri<sup>fi</sup>cation using k-fold or other models to decide the optimal number of virtual samples.

## References

[1] A. Asuncion, D.J. Newman, UCI Machine Learning Repository, [http://www.ics. uci.edu/mlearn/MLRepository.html] University of California, School of Information and Computer Science, Irvine, CA, 2007.

[2] C. Ferreira, Gene expression programming: a new adaptive algorithm for solving problems, Complex Systems 13 (2) (2001) 87–129.

[3] D.E. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning, Addison-Wesley Longman, Boston, MA, 1989.

[4] D.E. Goldberg, Genetic algorithms, tournament selection, and the effects of noise, Complex Systems 9 (3) (1995) 193–212.

[5] C.F. Huang, C. Moraga, A diffusion-neural-network for learning from small samples, International Journal of Approximate Reasoning 35 (2) (2004) 137–161.

[6] H. John Holland, Adaptation in Natural and Arti<sup>fi</sup>cial Systems, MIT Press, Cambridge, MA, 1992.

[7] J.R. Koza, Genetic Programming: Vol. 1, On the Programming of Computers by Means of Natural Selection, MIT Press, 1992

[8] S. Kumar, Neural Networks: A Classroom Approach, Tata McGraw-Hill Education, 2004.

[9] D.C. Li, C.C. Chang, C.W. Liu, Using structure-based data transformation method to improve prediction accuracies for small data sets, Decision Support Systems 52 (3) (2012) 748–756

[10] D.C. Li, C.C. Chen, C.J. Chang, W.C. Chen, Employing box-and-whisker plots for learning more knowledge in TFT-LCD pilot runs, International Journal of Production Research 50 (6) (2012) 1539–1553.

[11] D.C. Li, L.S. Chen, Y.S. Lin, Using functional virtual population as assistance to learn scheduling knowledge in dynamic manufacturing environments, International Journal of Production Research 41 (17) (2003) 4011–4024.

[12] D.C. Li, Y.H. Fang, Y.M. Fang, The data complexity index to construct an ef<sup>fi</sup>cient cross-validation method, Decision Support Systems 50 (1) (2010) 93–102.

[13] D.C. Li, C.W. Liu, Extending attribute information for small data set classi<sup>fi</sup>cation, IEEE Transactions on Knowledge and Data Engineering 24 (3) (2012) 452–464.

[14] D.C. Li, C.S. Wu, T.I. Tsai, F.M.M. Chang, Using mega-fuzzi<sup>fi</sup>cation and data trend estimation in small data set learning for early FMS scheduling knowledge, Computers & Operations Research 33 (6) (2006) 1857–1869.

[15] D.C. Li, C.S. Wu, T.I. Tsai, Y.S. Lin, Using mega-trend-diffusion and arti<sup>fi</sup>cial samples in small data set learning for early <sup>fl</sup>exible manufacturing system scheduling knowledge, Computers & Operations Research 34 (4) (2007) 966–982.

[16] P. Mitra, C.A. Murthy, S.K. Pal, Unsupervised feature selection using feature similarity, IEEE Transactions on Pattern Analysis and Machine Intelligence 24 (3) (2002) 301–312.

[17] M.M. Papari, F. Youse<sup>fi</sup>, J. Moghadasi, H. Karimi, A. Campo, Modeling thermal conductivity augmentation of nano<sup>fl</sup>uids using diffusion neural networks, International Journal of Thermal Sciences 50 (1) (2011) 44–52.

[18] D. Whitley, The genitor algorithm and selection pressure: why rank-based allocation of reproductive trials is best, Proceeding of the Third International Conference on Genetic Algorithms, Morgan Kaufmann, 1989, pp. 116–121

![](/api/attachments/5FTTNAZM/fulltext/images/c63687d9046f7464d214e10ff1111f3166c2e1f37434a9d5935a3f25cf6c6ff1.jpg)

Der-Chiang Li is a Distinguished Professor at the Department of Industrial and Information Management, the National Cheng Kung University, Taiwan. He received his PhD degree at the Department of Industrial Engineering at Lamar University Beaumont, Texas, USA, in 1985. As a research professor, his current interest concentrates on machine learning with small datasets. His articles have appeared in OMEGA, The International Journal of Management Science, IEEE Transactions on Knowledge and Data Engineering, Decision Support Systems, Information Sciences, European Journal of Operational Research, Computers & Operations Research, International Journal of Production Research, and other publications.

![](/api/attachments/5FTTNAZM/fulltext/images/8965b3862bf3e5f8ce23fb183dd19d1aee7455d9fdbbd9ebd15ddafdf089d03a.jpg)

Liang-Sian Lin is a doctoral candidate researcher at the Department of Industrial and Information Management, the National Cheng Kung University, Taiwan. He is also working at the laboratory for small sample learning. As a research professor, his current interests concentrate on small datasets. His article has appeared in European Journal of Operational Research.

![](/api/attachments/5FTTNAZM/fulltext/images/92f0608eb7581d91b84c566019913886748148db02f31afb3eec4c7aac9ee80a.jpg)

Li-Jhong Peng is a master at the Department of Industrial and Information Management, National Cheng Kung University, Taiwan. His recent research interests include production forecasting and machine learning.
