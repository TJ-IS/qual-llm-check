---
otero_id: 16050
otero_key: "KUYEM2V9"
title: "An efficiency-driven approach for setting revenue target"
authors: "Hung-Tso Lin"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.03.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An ef<sup>fi</sup>ciency-driven approach for setting revenue target

Hung-Tso Lin ⁎

Department of Distribution Management, National Chin-Yi University of Technology, Taichung County, Taiwan, Republic of China

a r t i c l e i n f o

Article history: Received 9 July 2009 Received in revised form 25 January 2010 Accepted 28 March 2010 Available online 2 April 2010

Keywords: Ef<sup>fi</sup>ciency Data envelopment analysis (DEA) Strong ordinal data

## a b s t r a c t

This paper addresses the ef<sup>fi</sup>ciency measurement and revenue setting problems drawn from a home improvement company with 22 chain stores in Taiwan. The top management attaches great importance to ef<sup>fi</sup>ciency analysis of their stores. Furthermore, when the proposal to establish a new store is under development, the regional manager must determine what ef<sup>fi</sup>ciency level the new store should achieve and what amount of business revenue it should earn. An approach by using the imprecise DEA (IDEA) and inverse IDEA models as core techniques is proposed to deal with such problems. A simulated application illustrates the implementation of the proposed approach.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

In popular management theory, goal-setting and ef<sup>fi</sup>ciency measurement play a pivotal role, expressed in phrases such as “what gets measured, gets done” [22]. From the viewpoint of management practice, questions related to what level of ef<sup>fi</sup>ciency an organization needs to achieve and how it should set appropriate ef<sup>fi</sup>ciency target are some of the main issues for managing organizational ef<sup>fi</sup>ciency [12,21].

In this paper, the issue for measuring ef<sup>fi</sup>ciencies of existing stores and decision-making problem for setting business revenue target of a new store are addressed. These problems are drawn from a home improvement company in Taiwan. The company has established 22 chain stores to sell do-it-yourself products including more than thirty thousand items and to provide professional design and consultation for home improvement. In order to enhance the service competence to cope with intense competition within the same business sector and to meet the diverse demands of customers, the top management attaches great importance to ef<sup>fi</sup>ciency analysis. Thus, to obtain an objective ef<sup>fi</sup>ciency measurement in last period the regional managers must evaluate not only the business revenue earned by the stores in their respective regions, but also the performance of resource utilization in earning that revenue. Furthermore, important considerations have arisen due to the development of a new store establishment proposal. In addition to allotting the input resources for a new store, a regional manager must determine what ef<sup>fi</sup>ciency level the new store should achieve and how much business revenue it should earn. Under the target of business revenue, the store manager and the subsidiary workers will devote themselves to develop effective marketing and service plans for delivering the target. Since the company plans to establish new stores each year in different regions, such considerations have become important issues for corporate administration, and so this is thus a problem worthy of investigation.

Each store consumes some resources in implementing the tasks to obtain some concerned results. Conceptually, the relative ef<sup>fi</sup>ciency of a store is calculated as the ratio of weighted sum of outputs to weighted sum of inputs. Data envelopment analysis (DEA) has been shown to be a powerful tool for measuring the relative ef<sup>fi</sup>ciencies of the homogenous decision-making units (DMUs). In this study, the chain stores are referred to as homogenous DMUs. DEA and the relevant techniques are employed to deal with the problems under consideration. The rest of this paper is organized as follows. The next section presents the fundamentals of DEA models and the relevant techniques. Section 3 describes the proposed approach consisting of <sup>fi</sup>ve stages. Section 4 illustrates the implementation of the proposed approach via a simulated application. Finally, conclusions are given in Section 5.

## 2. DEA models and relevant techniques

DEA is a nonparametric method that can be applied to assess the relative ef<sup>fi</sup>ciency of each DMU without predetermined weights for the input and output factors and without knowing information on the production function. The CCR model [3] and BCC model [1] are commonly used to evaluate relative aggregate ef<sup>fi</sup>ciency and technical ef<sup>fi</sup>ciency, respectively, of each DMU that consumes multiple inputs to produce multiple outputs. For convenience, the momentous notations used in the following description are listed in Table 1. The CCR (Charnes–Cooper–Rhodes) model was developed to establish an ef<sup>fi</sup>ciency frontier based on the Pareto optimum concept. The aggregate ef<sup>fi</sup>ciency of the DMU under evaluation, say DMU k, can be calculated by the following output-oriented DEA-CCR model:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 1
Notations.

Index and input parameters
 $X_{i}$  input factor i, i=1,2,...,m.
 $Y_{r}$  output factor r, r=1,2,...,s.
 $x_{ij}$  input amount of  $X_{i}$  of DMU j, j=1,2,...,n.
 $y_{rj}$  output amount of  $Y_{r}$  of DMU j, j=1,2,...,n.
 $\varepsilon$  a non-Archimedean small number.
 $n_{\ell j}$  number of workers in rank  $\ell$  of DMU j.
 $BP_{\ell}$  basic payment of salary and bonus of a worker in rank  $\ell$ .
 $EE_{\ell}$  extra expenditures of a worker in rank  $\ell$ .
 $\delta(\ell)$  total amount of resources consumed by a worker in rank  $\ell$ ,
where  $\delta(\ell)=BP_{\ell}+EE_{\ell},\delta(\ell)&lt;\delta(\ell+1)$  and  $\delta(1)\geq\gamma=BP_{1}$ .
 $\pi_{\ell}$  a value to reflect the degree of worker level intensity between ranks  $\ell$  and  $\ell+1$ .
 $p_{r}$  unit value of  $Y_{r}$ .
 $x_{ij}'$  adjusted or revised amount of  $x_{ij}$ .
 $n_{\ell j}'$  adjusted or revised number of  $n_{\ell j}$ .

Decision variables
 $E_{k}^{A}$  aggregate efficiency of DMU k.
 $E_{k}^{T}$  technical efficiency of DMU k.
 $E_{k}^{S}$  scale efficiency of DMU k.
 $v_{i}$  weight attached to  $X_{i}$ .
 $u_{r}$  weight attached to  $Y_{r}$ .
 $w_{1\ell}$  weight attached to  $n_{\ell j}$ , where  $w_{1\ell}=v_{1}\delta(\ell)$ .
 $v_{0}$  a variable used to discriminate the status of returns-to-scale of the DMU under evaluation.
 $y_{rj}'$  amount target for adjusting or revising  $y_{rj}$ .
</div>

$$
E _ {k} ^ {A} = \text { Min } \sum_ {i = 1} ^ {m} v _ {i} x _ {i k}\tag{1.0}
$$

$$
\mathrm{s.t.} \sum_ {i = 1} ^ {m} v _ {i} x _ {i j} - \sum_ {r = 1} ^ {s} u _ {r} y _ {r j} \geq 0, j = 1, \dots , n,\tag{1.1}
$$

$$
\sum_ {r = 1} ^ {s} u _ {r} y _ {r k} = 1,   v i, u _ {r} \geq \varepsilon .\tag{1.2}
$$

By the restriction of the above constraints, the ef<sup>fi</sup>ciencies of all DMUs have a lower bound of 1. DMU k is aggregate ef<sup>fi</sup>cient when $E _ { k } ^ { A }$ is equal to 1 and aggregate inef<sup>fi</sup>cient if $E _ { k } ^ { A }$ is greater than 1. The value of E<sup>A</sup> equals 1 indicating that DMU k lies on the ef<sup>fi</sup>ciency frontier and is thus regarded as relatively ef<sup>fi</sup>cient. Alternatively, DMU k does not lie on the ef<sup>fi</sup>ciency frontier and is regarded as relatively inef<sup>fi</sup>cient. Regarding the determination of weights $\nu _ { i }$ and $u _ { r } ,$ each DMU is allowed to select the most favorable weights in measuring its relative ef<sup>fi</sup>ciency provided that all DMUs with the same weights will not be resulted in ef<sup>fi</sup>ciency score of less than 1. However, to prevent unfavorable factors from being ignored in the evaluation by setting a weight of zero to them, all weights should be greater than a non-Archimedean small number ε.

In model (1), when the objective function (Eq. (1.0)) is set as $E _ { k } ^ { A } = \operatorname { M a x } \sum _ { r = 1 } ^ { S } \ u _ { r } y _ { r k }$ and the 2nd constraint (Eq. (1.2)) as $\sum _ { i = 1 } ^ { m } \nu _ { i } x _ { i k } = 1$ , then the model is known as input-oriented DEA-CCR model and the ef<sup>fi</sup>ciencies of all DMUs have a upper bound of 1.

The main advantage of CCR model is that it can be used to measure the aggregate ef<sup>fi</sup>ciency of each DMU for evaluating its performance of resource utilization. However, the limitation of CCR model is that it is based on the assumption of constant returns-to-scale. In order to establish a variable returns-to-scale ef<sup>fi</sup>ciency frontier for measuring the technical ef<sup>fi</sup>ciency, the BCC (Banker–Charnes–Cooper) model was developed by introducing a variable, $\nu _ { 0 } ,$ to reveal the status of returns-to-scale at speci<sup>fi</sup>c points on the ef<sup>fi</sup>ciency frontier. By employing the treatment of $\boldsymbol { v } _ { 0 }$ in the BCC model [16,18], the output-oriented DEA-BCC model for measuring the technical ef<sup>fi</sup>ciency of DMU k can be represented as follows:

$$
\begin{array}{l} E _ {k} ^ {T} = \text { Min } \sum_ {i = 1} ^ {m} v _ {i} x _ {i k} + v _ {0} \\ \text { s.t. } \sum_ {i = 1} ^ {m} v _ {i} x _ {i j} + v _ {0} - \sum_ {r = 1} ^ {s} u _ {r} y _ {r j} \geq 0, j = 1,..., n, \\ \sum_ {r = 1} ^ {s} u _ {r} y _ {r k} = 1, \\ _ {v i}, u _ {r} \geq \varepsilon , v _ {0} \text { unrestricted   in   sign. } \end{array}\tag{2}
$$

DMU k is technical ef<sup>fi</sup>cient when $E _ { k } ^ { T } { = } 1$ and technical inef<sup>fi</sup>cient if $E _ { k } ^ { T } > 1$ . The value of $\boldsymbol { v } _ { 0 }$ can be positive, zero or negative indicating that DMU k presents DRS (decreasing returns-to-scale), CRS (constant returns-to-scale) or IRS (increasing returns-to-scale), respectively. When $\boldsymbol { v } _ { 0 }$ is set as zero in model (2), the model is known as CCR.

The aggregate ef<sup>fi</sup>ciency is used to explore the performance of resource utilization, while the technical ef<sup>fi</sup>ciency is used to explore the performance of operation. By using the technical ef<sup>fi</sup>ciency, the reasons causing aggregate inef<sup>fi</sup>ciency (i.e., inef<sup>fi</sup>ciency in resource utilization) can be speci<sup>fi</sup>ed. Since the aggregate ef<sup>fi</sup>ciency can be decomposed into the technical ef<sup>fi</sup>ciency and the scale ef<sup>fi</sup>ciency [1], the scale ef<sup>fi</sup>ciency can be obtained by calculating the ratio of aggregate ef<sup>fi</sup>ciency to technical ef<sup>fi</sup>ciency and then used to assess the adequacy of the scale. A DMU is aggregate ef<sup>fi</sup>cient if and only if it is both technical ef<sup>fi</sup>cient and scale ef<sup>fi</sup>cient. If a DMU is aggregate inef<sup>fi</sup>cient, then the technical ef<sup>fi</sup>ciency and scale ef<sup>fi</sup>ciency scores can be used to detect the sources of aggregate inef<sup>fi</sup>ciency, viz., whether it is caused by technical inef<sup>fi</sup>ciency, by scale inef<sup>fi</sup>ciency or by both [23].

In the conventional DEA, the input and output data can be expressed exactly. This type of model has been extensively applied in real-world cases [e.g., 2,11,16,24,25]. In practice, uncertain information, which is expressed such as bounded data, ordinal data or ratiobounded data, occurs because of uncertainty. The mixture of uncertain information is referred to as imprecise data, and the associated method as imprecise DEA (IDEA). There have been many studies discussing the treatment of imprecise data and the application of the IDEA model [e.g., 6,8,9,15,19,26,28]. These IDEA models were developed to treat the case of mixtures of interval and ordinal data together with crisp number, or the case of incorporating fuzzy data into interval and ordinal data. With respect to the solution to IDEA model, it can either be solved using the standard linear DEA model by converting imprecise data into exact data [e.g., 30–32] or converted into a linear program by scale transformations and variable alternations [e.g., 7]. Chen [4] showed alternative ways to convert the ordinal data into bounded data and further into a set of exact data, and then investigated the work mechanisms of multiplier IDEA and primal IDEA.

Previous studies of DEA and IDEA were applied to measure the relative ef<sup>fi</sup>ciency scores of the DMUs under given amounts of inputs and outputs. In recent years, a few studies have discussed the inverse DEA problem. Jahanshahloo et al. [14] reviewed these studies and classi<sup>fi</sup>ed the addressed problems into two types. The <sup>fi</sup>rst type is related to how much the amounts of input and output should be adjusted so that the ef<sup>fi</sup>ciency level of the DMU concerned remains unchanged or at least maintains its current ef<sup>fi</sup>ciency status. Some methods were proposed to deal with this problem [27,29]. The second type is concerned with the problem that: if certain amounts of inputs are increased to a particular DMU, and assuming that the DMU improves its current ef<sup>fi</sup>ciency level with respect to other DMUs, then how much should the output of the DMU be increased? Jahanshahloo et al. [13] developed a method to solve this problem.

## 3. Proposed approach

DEA and inverse DEA methods are employed in this study since they are powerful tools that have been extensively applied in management problems. Due to the characteristics of the ordinal data considered in the current real-world case, suitable IDEA and inverse IDEA models are developed as core techniques of the proposed approach to deal with the problems of ef<sup>fi</sup>ciency measurement of existing stores and setting revenue target of a new store. The conceptual <sup>fl</sup>ow of the proposed approach is depicted in Fig. 1. The approach is according to the following procedure:

## Stage 1. Ef<sup>fi</sup>ciency measurement of existing stores

A suitable IDEA-CCR model is proposed to measure the aggregate ef<sup>fi</sup>ciency scores of existing stores which contain strong ordinal input data in last period. The period for ef<sup>fi</sup>ciency measurement is usually a <sup>fi</sup>scal year. The IDEA-BCC model is also employed to measure the technical ef<sup>fi</sup>ciency scores and obtain the values of $\boldsymbol { v } _ { 0 }$ of existing stores for classifying them into the types of IRS, CRS or DRS.

Stage 2. Adjusting inputs and outputs of existing stores and calculating the expected aggregate ef<sup>fi</sup>ciency scores for next period

The status of returns-to-scale of a store is used as a guide for adjusting its input resources and output target. The expected amounts of input and output are increased in next period for existing stores classi<sup>fi</sup>ed as IRS or CRS, while the expected amounts of input are decreased and amount of output will remain the same for a store classi<sup>fi</sup>ed into the DRS type. Then, the expected aggregate ef<sup>fi</sup>ciency scores in the next period are calculated.

Stage 3. Setting expected aggregate ef<sup>fi</sup>ciency score and <sup>fi</sup>ctitious inputs and output for a new store

Among the group of existing stores, the expected aggregate ef<sup>fi</sup>ciency score ranked in cth percentile is selected as the expected level of the new store. The input and output data of this reference store are used as the <sup>fi</sup>ctitious data for the new store such that the aggregate ef<sup>fi</sup>ciency score of new store is kept at the expected level.

Stage 4. Revising <sup>fi</sup>ctitious input data of new store

The <sup>fi</sup>ctitious input data of the new store are revised according to allotted data of the establishment proposal.

Stage 5. Using the inverse IDEA-CCR model to set the target of output (business revenue) for a new store

In order to remain the expected aggregate ef<sup>fi</sup>ciency level of the new store unchanged, a suitable inverse IDEA-CCR model is developed to obtain the target of output for the new store with its revised input data.

## 4. Simulated application

Since the regional manager in the region of southern Taiwan, where 11 chain stores have been established, is now planning to establish a new store in his region, this case is used to illustrate the implementation of the proposed approach.

## 4.1. Stage 1

4.1.1. Inputs and outputs

The relative ef<sup>fi</sup>ciency of each store is calculated via its weighted sum of outputs and weighted sum of inputs. Some factors which are capable of representing the attainment of output and the input resources that the stores have consumed should be selected adequately. According to the managerial judgments, earning money via selling products and providing relevant services for customers is the major task of the stores. Hence, monetary amount of business revenue (in 1000 New Taiwan Dollars; NTD) is served as output factor (Y ). Regarding the input factors, the regional manager concerns the internal resources related to service manpower, space and expenditures. In the study of Wu et al. [28], population density is contained in the input factors to represent the environmental variable, and then the ef<sup>fi</sup>ciencies of banks from different regions were assessed and compared. From the outlook on relative ef<sup>fi</sup>ciency, the more the population (i.e., input), the more the revenue (i.e., output) of a store should be. Therefore, the population density in the trade area is also adopted as input factor to represent the external resource in this study. Thus, the input factors consist of manpower $\left( X _ { 1 } \right)$ , store <sup>fl</sup>oor area $( X _ { 2 } ,$ , in 36 square feet), operating expense $( X _ { 3 } ,$ in 1000 NTD) and number of households in the trade area $( X _ { 4 } )$ . Since the number of stores is somewhat low, and in addition, the number of input factors is from three to four and the number of output factors is from one to three in the reference studies [e.g., 2,8,10,11,15,16,20,24,31], hence the numbers of input and output factors used in this study are appropriate. Table 2 shows the input and output measures of the 11 existing stores in last <sup>fi</sup>scal year. The correlation coef<sup>fi</sup>cients between $X _ { i } , i = 1 , 2 , 3 ,$ 4, and $Y _ { 1 }$ are calculated as 0.97, 0.83, 0.88 and 0.78, respectively, where $X _ { 1 }$ adopts the total number. The high positive correlations between the four input factors and the output factor show that the isotonic property is preserved for them. Thus, the validity of the inputs and output is justi<sup>fi</sup>ed.

![](/api/attachments/KUYEM2V9/fulltext/images/8c82a0d6a64194e9270779e768a74f189282622f64b2444d22e0fe43cad1fff1.jpg)  
Fig. 1. Conceptual <sup>fl</sup>ow of the <sup>fi</sup>ve-stage approach.

Regarding the input manpower $\left( X _ { 1 } \right)$ , there is a characteristic of multiple workers in different ranks. Each store employs workers in these categories to provide the sales service and home improvement consultation for customers. The workers are classi<sup>fi</sup>ed into <sup>fi</sup>ve ranks, abbreviated as ranks 1 to 5, according to knowledge, expertise and experience, with rank 5 being the highest. For example, the total number of workers employed by store 1 is 77, with 12 in rank 1 and three in rank 5. These three workers in rank 5 include one store manager and two division managers. The company provides different remuneration, welfare and related support (such as salary, bonus, traveling perquisite, learning and training expenditure, private room and others) for each of the <sup>fi</sup>ve ranks. According to the payments structure, the total amount of resources consumed by a worker in rank $\ell , ~ \delta ( \ell ) , ~ \ell = 1 , . . . , 5 ,$ can be divided into two parts: basic payment of salary and bonus, BP<sub>ℓ</sub>, and extra expenditures, EE<sub>ℓ</sub>. That $\mathrm { i } s , \delta ( \ell )$ can be expressed as $\delta ( \angle ) = \tt B P _ { \ell } + E E _ { \ell }$ . The higher the rank $\ell ,$ the more the amount of BP . With respect to EE , although the amount of EE is dif<sup>fi</sup>cult to calculate exactly, the regional manager argues that a worker in the higher ranks consumes much more extra expenditures, viz., $\mathrm { E E } _ { \ell + 1 }$ is much more than $\mathrm { E E } _ { \ell } .$ . Thus, obviously a worker in rank 5 consumes the most resources, while one in rank 1 consumes the least. Besides, the amounts of $\mathbf { \delta } _ { \mathbf { \delta } } \delta ( \mathbf { \mathcal { L } } )$ may be different for the workers in rank ℓ but employed by different stores. In order to quantify the characteristics that workers in different ranks are employed by the stores and different ranks consume different amounts of resources, after consultation with the regional manager, the input values of the <sup>fi</sup>ve ranks are treated as a strong ordinal relation. The total amount of resources consumed by the workers in different ranks are expressed as $\delta ( \ell ) { < } \delta ( \ell + 1 ) , \ \ell { = } 1 , . . . , 4 .$ . This relation reveals that a worker in rank ℓ consumes less resources than one in rank $\ell + 1$

By treating $X _ { 1 }$ as a compound manpower which consists of multiple workers in <sup>fi</sup>ve ranks with a strong ordinal relation, then the input amount of $X _ { 1 }$ of store $j , x _ { 1 j } ,$ can be measured as the sum of products between the number of workers in rank $\mathbf { \Xi } _ { \mathbf { z } } ^ { \mathcal { I } } , \ n _ { \mathcal { I } { \mathbf { j } } } ,$ , and the corresponding input amount, $\delta ( \ell )$ . That is, $x _ { 1 j } = \sum _ { \ell = \ l _ { 1 } } ^ { \ l } n _ { \ell j } \delta ( \ell )$ . For example, the numbers of workers in ranks 1 to 5 of store 1 are 12, 46, 10, 6 and 3, respectively. Then $n _ { 1 1 } = 1 2 , n _ { 2 1 } = 4 6 , n _ { 3 1 } = 1 0 , n _ { 4 1 } = 6$ and $n _ { 5 1 } = 3$ . The compound manpower of store $1 , x _ { 1 1 } ,$ is calculated as $x _ { 1 1 } = 1 2 \delta ( 1 ) + 4 6 \delta ( 2 ) + 1 0 \delta ( 3 ) + 6 \delta ( 4 ) + 3 \delta ( 5 )$ . Thus, for store 1, the resources consumed by all workers in the <sup>fi</sup>ve ranks are included in the input manpower via $\delta ( \ell )$ and $n _ { \ell 1 }$

Table 2  
Input and output measures of the 11 existing stores.

<table><tr><td rowspan="2">Store (j)</td><td colspan="6"> $X_1$ </td><td rowspan="2"> $X_2$ </td><td rowspan="2"> $X_3$ </td><td rowspan="2"> $X_4$ </td><td rowspan="2"> $Y_1$ </td></tr><tr><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>Total</td></tr><tr><td>1</td><td>3</td><td>6</td><td>10</td><td>46</td><td>12</td><td>77</td><td>1105</td><td>20,432</td><td>242,766</td><td>421,276</td></tr><tr><td>2</td><td>3</td><td>5</td><td>10</td><td>46</td><td>20</td><td>84</td><td>1480</td><td>16,702</td><td>192,812</td><td>501,549</td></tr><tr><td>3</td><td>3</td><td>4</td><td>6</td><td>33</td><td>11</td><td>57</td><td>725</td><td>13,250</td><td>112,663</td><td>308,853</td></tr><tr><td>4</td><td>3</td><td>5</td><td>10</td><td>38</td><td>15</td><td>71</td><td>1159</td><td>16,310</td><td>149,268</td><td>331,495</td></tr><tr><td>5</td><td>2</td><td>4</td><td>5</td><td>23</td><td>12</td><td>46</td><td>1089</td><td>14,850</td><td>103,735</td><td>222,646</td></tr><tr><td>6</td><td>4</td><td>5</td><td>10</td><td>50</td><td>27</td><td>96</td><td>1615</td><td>29,728</td><td>218,924</td><td>642,073</td></tr><tr><td>7</td><td>2</td><td>3</td><td>7</td><td>17</td><td>12</td><td>41</td><td>753</td><td>12,558</td><td>55,072</td><td>167,886</td></tr><tr><td>8</td><td>3</td><td>5</td><td>7</td><td>42</td><td>13</td><td>70</td><td>1354</td><td>20,229</td><td>253,009</td><td>350,590</td></tr><tr><td>9</td><td>3</td><td>6</td><td>13</td><td>48</td><td>14</td><td>84</td><td>1790</td><td>24,979</td><td>224,362</td><td>460,869</td></tr><tr><td>10</td><td>2</td><td>3</td><td>3</td><td>17</td><td>10</td><td>35</td><td>696</td><td>10,268</td><td>108,672</td><td>139,515</td></tr><tr><td>11</td><td>3</td><td>6</td><td>7</td><td>49</td><td>20</td><td>85</td><td>1645</td><td>20,273</td><td>214,626</td><td>454,549</td></tr></table>

The operating expense (X ) is the expenditures for maintenance of facilities, cleaning, telephone, postage, water, electric power, rent, depreciation and others. The advertising, remuneration, welfare and related support of personnel are not included.

## 4.1.2. Proposed IDEA model

Since the inputs contain strong ordinal data, the suitable outputoriented IDEA-CCR and IDEA-BCC models are developed for measuring the relevant ef<sup>fi</sup>ciency scores and classifying the returns-to-scale of existing stores into the types of IRS, CRS or DRS. The reason for adopting the output-oriented model is that this orientation is suitable for developing the inverse model, where the objective value shows the target of business revenue (see $y ^ { \prime } { } _ { 1 , 1 2 }$ in model (5) later).

In this study, $x _ { 1 j }$ is expressed as $x _ { 1 j } = \sum _ { \ell = 1 } ^ { 5 } n _ { \ell j } \delta ( \ell )$ , where $\delta ( \ell )$ follows the strong ordinal relation of $\delta ( \diagup ) { < } \delta ( \diagup + 1 )$ . Model (2) is rewritten in the following IDEA-BCC form:

$$
E _ {k} ^ {T} = \mathrm{Min} v _ {1} \sum_ {\ell = 1} ^ {5} n _ {\ell k} \delta (\ell) + \sum_ {i = 2} ^ {4} v _ {i} x _ {i k} + v _ {0}\tag{3.0}
$$

$$
\text { s.t. } \quad v _ {1} \sum_ {\ell = 1} ^ {5} n _ {\ell j} \delta (\ell) + \sum_ {i = 2} ^ {4} v _ {i} x _ {i j} + v _ {0} - u _ {1} y _ {1 j} \geq 0, j = 1,..., 1 1,
$$

$$
u _ {1} y _ {1 k} = 1,\tag{3.1}
$$

$$
\delta (5) > \delta (4) > \delta (3) > \delta (2) > \delta (1) \geq \gamma > 0,\tag{3.2}
$$

<sub>ð</sub>3:3<sub>Þ</sub>

v ; v ; v ; v ; u ≥ ε; v unrestricted in sign:

In model (3), the 3rd constraint (Eq. (3.3)) restricts that the permissible input amounts must satisfy the strong ordinal relation in which a worker in rank ℓ consumes less resources than one in rank $\ell + 1$ , and the value of δ(1) is greater than or equal to the value of $\gamma .$ The strong ordinal relation of $\delta ( \angle + 1 ) { > } \delta ( \angle )$ equates the form of $\delta ( \angle + 1 ) - \delta ( \angle ) \geq \pi$ with $\pi { > } 0$ . Since Zhu [31] showed that the strong ordinal relation with this form is unable to discriminate ef<sup>fi</sup>ciencies with a strong ordinal relation from those with a weak ordinal relation. Hence, the improved form, $\delta ( \ell + 1 ) \geq \pi \delta ( \ell ) , \pi { > } 1$ , was suggested by Zhu to replace it. In this study, the parameter π is introduced to re<sup>fl</sup>ect the degree of worker level intensity between ranks $\ell$ and $\ell + 1$ . The strong ordinal relation of $\delta ( \angle + 1 ) { > } \delta ( \angle )$ in Eq. (3.3) is replaced by the improved form of $\delta ( \ell + 1 ) \geq \pi _ { \ell } \delta ( \ell ) , \pi _ { \ell } > 1$

The determination of π is now elaborated in detail. The proportion of $\delta ( \ell + 1 )$ to $\delta ( \ell )$ can be expressed as $\delta ( \diagup ^ { } + 1 ) / \delta ( \ell ) =$ $\left( \mathsf { B P } _ { \ell + 1 } + \mathsf { E E } _ { \ell + 1 } \right) / \left( \mathsf { B P } _ { \ell } + \mathsf { E E } _ { \ell } \right)$ . Since the regional manager argues that $\mathrm { E E } _ { \ell _ { + } } { } _ { 1 }$ is much more than $\mathrm { E E } _ { \ell } ,$ hence he considers that $\delta \left( \ell + 1 \right) / \delta \left( \ell \right) \geq \mathrm { B P } _ { \ell \textrm { + } 1 } / \mathrm { B P } _ { \ell } , \mathrm { o r } \delta \left( \ell + 1 \right) \geq \left( \mathrm { B P } _ { \ell \textrm { + } 1 } / \mathrm { B P } _ { \ell } \right) \delta \left( \ell \right)$ Thus, π is determined as $\pi _ { \ell } = \mathsf { B P } _ { \ell } + \mathsf { \Omega } _ { 1 } / \mathsf { B P } _ { \ell } > 1$ . By using the average of BP for the workers of 11 stores in last <sup>fi</sup>scal year, the amounts of BP (in NTD), $\ell = 1 , . . . , 5 ,$ , are determined as $\mathsf { B P } _ { 1 } = 2 5 0 , 8 9 5 ,$ $\mathsf { B P } _ { 2 } = 3 0 9 , 4 0 7$ , BP =569,435, $\mathsf { B P } _ { 4 } = 8 0 8 , 2 9 5$ and $\mathsf { B P } _ { 5 } = 1 , 6 8 0 , 7 3 0$ By using these amounts of $\mathsf { B P } _ { \ell } , \pi _ { 1 } , \pi _ { 2 } , \pi _ { 3 }$ and $\pi _ { 4 }$ are determined as 1.2332, 1.8404, 1.4194 and 2.0793, respectively. The value of γ is set as $\mathsf { B P } _ { 1 } ~ ( = 2 5 0 , 8 9 5 )$

By substituting $\delta ( \ell + 1 ) \geq \pi _ { \ell } \delta ( \ell )$ for $\delta ( \angle + 1 ) { > } \delta ( \angle )$ and making the change of variable $w _ { 1 / } = \nu _ { 1 } \delta ( \ell )$ , model (3) now has a linear programming problem format:

$$
E _ {k} ^ {T} = \mathrm{Min} \sum_ {\ell = 1} ^ {5} n _ {\ell k} w _ {1 \ell} + \sum_ {i = 2} ^ {4} v _ {i} x _ {i k} + v _ {0}\tag{4.0}
$$

$$
\mathrm{s.t.} \sum_ {\ell = 1} ^ {5} n _ {\ell j} w _ {1 \ell} + \sum_ {i = 2} ^ {4} v _ {i} x _ {i j} + v _ {0} - u _ {1} y _ {1 j} \geq 0, j = 1, \dots , 1 1,\tag{4.1}
$$

$$
u _ {1} y _ {1 k} = 1,\tag{4.2}
$$

$$
w _ {1, \ell + 1} \geq \pi_ {\ell} w _ {1 \ell}, \ell = 1, 2, 3, 4,\tag{4.3}
$$

$$
w _ {1 1} \geq v _ {1} \gamma > 0,\tag{4.4}
$$

v ; v ; v ; v ; u ≥ε; v unrestricted in sign:

Thus, $w _ { 1 \ell }$ is the most favorable weight attached to $n _ { \angle k }$ in calculating the best relative ef<sup>fi</sup>ciency of store k. Regarding the value of ε, Chien et al. [5] pointed out that ε is generally set as 10<sup>−9</sup>, while Kao et al. [17] considered that $1 0 ^ { - 6 }$ is commonly used in practice. In this study, the value of ε is set as $1 0 ^ { - 8 }$ . When $\boldsymbol { v } _ { 0 }$ is set as zero in model (4), the IDEA-BCC model becomes IDEA-CCR form.

By using model (4), the technical ef<sup>fi</sup>ciency score along with the maximum weight and minimum weight are shown in columns 2–4 of Table 3. The status of returns-to-scale is classi<sup>fi</sup>ed by value of v and shown in column 5 of Table 3. None of the stores is classi<sup>fi</sup>ed into DRS type. By using IDEA-CCR model, the aggregate ef<sup>fi</sup>ciency score along with the maximum weight and minimum weight are obtained and shown in columns 7–9 of Table 3. For the weight determination in calculating the best relative ef<sup>fi</sup>ciency of each store, all 11 stores put the maximum weight on $w _ { 1 5 } .$ The minimum weight is put on $\nu _ { 2 } , \nu _ { 3 }$ or $\nu _ { 4 } .$ According to the descending order of $E _ { j } ^ { A } ,$ , the existing stores are ranked as store 10–5–8–4–9–11–1–7–3–2–6, where store 11 is ranked as the 50th percentile in the group of existing stores. This ranking shows that stores 2 (with $E _ { 2 } ^ { A } = 1 )$ and 6 (with E<sup>A</sup>=1) are the best ones in performance of resource utilization, while store 10 (with $E _ { 1 0 } ^ { A } = 1 . 7 4 6 )$ has the worst performance. This is because stores 2 and 6 produce relatively more outputs and store 10 produces relatively fewer outputs. Note that the output of store $7 \left( y _ { 1 7 } = 1 6 7 , 8 8 6 \right)$ is fewer than that of store $5 \left( y _ { 1 5 } = 2 2 2 , 6 4 6 \right)$ , whereas the aggregate ef<sup>fi</sup>ciency score of store 7 $( E _ { 7 } ^ { A } = 1 . 0 4 5 )$ is better than that of store $5 ( E _ { 5 } ^ { A } = 1 . 3 7 9 )$ It may be seen somewhat of a surprise, but the reason is due to the evaluation is based on the resources utilization, and store 7 consumes relatively fewer resources in performing its service tasks.

The scale ef<sup>fi</sup>ciency score of store j can be calculated as $E _ { j } ^ { S } { = } E _ { j } ^ { A } / E _ { j } ^ { T }$ and is shown in column 6 of Table 3. It can be seen from $E _ { j } ^ { A } , E _ { j } ^ { T }$ and $E _ { j } ^ { S }$ that nine stores are aggregate inef<sup>fi</sup>cient. Among these nine stores, <sup>fi</sup>ve stores (stores 1, 3, 5, 7, and 10) are caused by scale inef<sup>fi</sup>ciency, while four stores (stores 4, 8, 9, and 11) are caused by both scale inef<sup>fi</sup>ciency and technical inef<sup>fi</sup>ciency.

Table 3  
Ef<sup>fi</sup>ciency measurement results.

<table><tr><td rowspan="2">Store (j)</td><td colspan="4">BCC model</td><td rowspan="2"> $E_j^S$ </td><td colspan="3">CCR model</td></tr><tr><td> $E_j^T$ </td><td>Max. weight</td><td>Min. weight</td><td>Status of returns-to-scale</td><td> $E_j^A$ </td><td>Max. weight</td><td>Min. weight</td></tr><tr><td>1</td><td>1</td><td> $w_{15}$ </td><td> $v_3,v_4$ </td><td>IRS</td><td>1.107</td><td>1.107</td><td> $w_{15}$ </td><td> $v_3,v_4$ </td></tr><tr><td>2</td><td>1</td><td> $w_{15}$ </td><td> $v_2$ </td><td>IRS</td><td>1</td><td>1</td><td> $w_{15}$ </td><td> $v_2$ </td></tr><tr><td>3</td><td>1</td><td> $w_{15}$ </td><td> $v_3$ </td><td>IRS</td><td>1.004</td><td>1.004</td><td> $w_{15}$ </td><td> $v_4$ </td></tr><tr><td>4</td><td>1.233</td><td> $w_{15}$ </td><td> $v_2$ </td><td>IRS</td><td>1.037</td><td>1.279</td><td> $w_{15}$ </td><td> $v_2$ </td></tr><tr><td>5</td><td>1</td><td> $w_{15}$ </td><td> $v_2$ </td><td>IRS</td><td>1.379</td><td>1.379</td><td> $w_{15}$ </td><td> $v_3$ </td></tr><tr><td>6</td><td>1</td><td> $w_{15}$ </td><td> $v_2,v_3$ </td><td>CRS</td><td>1</td><td>1</td><td> $w_{15}$ </td><td> $v_2,v_3$ </td></tr><tr><td>7</td><td>1</td><td> $w_{15}$ </td><td> $v_3$ </td><td>IRS</td><td>1.045</td><td>1.045</td><td> $w_{15}$ </td><td> $v_3$ </td></tr><tr><td>8</td><td>1.229</td><td> $w_{15}$ </td><td> $v_2,v_4$ </td><td>IRS</td><td>1.094</td><td>1.345</td><td> $w_{15}$ </td><td> $v_2,v_4$ </td></tr><tr><td>9</td><td>1.105</td><td> $w_{15}$ </td><td> $v_3,v_4$ </td><td>IRS</td><td>1.006</td><td>1.112</td><td> $w_{15}$ </td><td> $v_3,v_4$ </td></tr><tr><td>10</td><td>1</td><td> $w_{15}$ </td><td> $v_3$ </td><td>IRS</td><td>1.746</td><td>1.746</td><td> $w_{15}$ </td><td> $v_4$ </td></tr><tr><td>11</td><td>1.053</td><td> $w_{15}$ </td><td> $v_2,v_3$ </td><td>IRS</td><td>1.052</td><td>1.108</td><td> $w_{15}$ </td><td> $v_2,v_4$ </td></tr></table>

## 4.2. Stage 2

Since the returns-to-scale of existing stores are classi<sup>fi</sup>ed as either IRS or CRS, the expected input amounts and output targets will be increased in the next period. According to the suggestion of the regional manager, an increment of 2% for $Y _ { 1 }$ is set for all 11 stores. Regarding the inputs, the adjustment of $X _ { 3 }$ is based on the performance of resource utilization, meaning that with better aggregate ef<sup>fi</sup>ciency, the increment of $X _ { 3 }$ is higher. The other inputs will not be changed in the short-term consideration. As results, the adjusted amounts of $X _ { 3 }$ and $Y _ { 1 } ,$ , along with the expected aggregate ef<sup>fi</sup>ciency scores, for the 11 existing stores in next period are shown in columns 8, 10 and 11 of Table 4.

## 4.3. Stage 3

To set a challenging but attainable goal, the regional manager selects the aggregate ef<sup>fi</sup>ciency score ranked as the $5 0 ^ { \mathrm { { t h } } }$ percentile in the group of existing stores as the target for the new store $( \mathrm { i . e . }$ , store 12). This expected ef<sup>fi</sup>ciency is 1.108 and the reference store is store 11. The input and output data of store 11 are used as the <sup>fi</sup>ctitious data of store 12 so that the aggregate ef<sup>fi</sup>ciency score of store 12 is kept at the expected level. These <sup>fi</sup>ctitious data are listed in the last row of Table 4, which show $n _ { 1 , 1 2 } = 2 0 , n _ { 2 , 1 2 } = 4 9 , n _ { 3 , 1 2 } = 7 , n _ { 4 , 1 2 } = 6 ,$ $n _ { 5 , 1 2 } = 3$ , x<sub>2,12</sub> = 1645, $x _ { 3 , 1 2 } = 2 0 , 5 7 7$ $x _ { 4 , 1 2 } = 2 1 4 , 6 2 6$ and $y _ { 1 , 1 2 } = 4 6 3 , 6 4 0 .$

## 4.4. Stage 4

The previous <sup>fi</sup>ctitious inputs of store 12 are revised according to the company's establishment proposal and then used to determine its output target so that its expected ef<sup>fi</sup>ciency level remains unchanged. The revisions of <sup>fi</sup>ctitious input data of store 12 in the establishment proposal are elaborated as follows. By quoting from the marketing department's investigation, the number of households in the trade area $( X _ { 4 } )$ of store 12 is provided as 201,530. Hence, the <sup>fi</sup>ctitious data $x _ { 4 , 1 2 } = 2 1 4 , 6 2 6$ is revised as ${ x ^ { \prime } } _ { 4 , 1 2 } = 2 0 1 , 5 3 0$ . The regional manager assumes that there are relationships between $X _ { 4 }$ and $X _ { 2 } ,$ between $X _ { 2 }$ and $X _ { 3 }$ and between $X _ { 2 }$ and $X _ { 1 } .$ . Hence, the regression model is used to determine the amounts of input factors $X _ { 1 } , X _ { 2 }$ and $X _ { 3 }$ for store 12. Regarding the allotment of $X _ { 2 } ,$ the regression model used is $\begin{array} { r } { \hat { \mathrm { X } } _ { 2 } = \hat { \mathrm { \beta } } _ { 0 } + \hat { \mathrm { \beta } } _ { 4 } \mathrm { ~ \bar { X } } _ { 4 } . } \end{array}$ From the data shown in Table 4, the correlation coef<sup>fi</sup>cient of 0.772 and the p-value of 0.005 for the test $H _ { 1 } { : } \beta _ { 4 } { \neq } 0$ indicate that this regression model is proper for use under two-sided test at the 0.05 level of signi<sup>fi</sup>cance. Thus, the value o $X _ { 2 }$ for store 12 is allotted to be 1358 by this regression model. The <sup>fi</sup>ctitious data $x _ { 2 , 1 2 } = 1 6 4 5$ is revised as $x ^ { \prime } { } _ { 2 , 1 2 } = 1 3 5 8$ . For the budget of $X _ { 3 } ,$ the correlation coef<sup>fi</sup>cient of 0.837 and the p-value of 0.001 for the test $H _ { 1 } { : } \beta _ { 2 } { \neq } 0$ similarly indicate that $\hat { \mathrm { X } } _ { 3 } = \bar { \hat { \beta } } _ { 0 } + \hat { \beta } _ { 2 } X _ { 2 }$ is proper for use. Thereby, the amount of $X _ { 3 }$ for store 12 is budgeted as 19,524. The <sup>fi</sup>ctitious data $x _ { 3 , 1 2 } = 2 0$ ,577 is revised as $x ^ { \prime } { } _ { 3 , 1 2 } = 1 9 , 5 2 4$ . With respect to the disposition of $X _ { 1 } ,$ the regression model $\hat { \Chi } _ { 1 } = \hat { \beta } _ { 0 } + \hat { \beta } _ { 2 } \bar { X _ { 2 } }$ is respectively used for proposing the numbers of workers in the <sup>fi</sup>ve ranks. The correlation coef<sup>fi</sup>cients of 0.699, 0.844, 0.692, 0.810 and 0.645 and the p-values of 0.016, 0.001, 0.018, 0.002 and 0.032 for ranks 1 to $5 ,$ respectively, support the use of the regression model. The numbers of workers in ranks 1 to 5 are allotted as 16, 41, 9, 5 and 3, respectively. The <sup>fi</sup>ctitious data $n _ { 1 , 1 2 } = 2 0 , ~ n _ { 2 , 1 2 } = 4 9 , ~ n _ { 3 , 1 2 } = 7$ $n _ { 4 , 1 2 } = 6$ and $n _ { 5 , 1 2 } = 3$ are revised as $n ^ { \prime } { } _ { 1 , 1 2 } = 1 6 , n ^ { \prime } { } _ { 2 , 1 2 } = 4 1 , n ^ { \prime } { } _ { 3 , 1 2 } = 9$ $n ^ { \prime } { } _ { 4 , 1 2 } = 5$ and $n ^ { \prime } { } _ { 5 , 1 2 } = 3$

Table 4  
Adjusted data and expected aggregate ef<sup>fi</sup>ciency in the next period.

<table><tr><td rowspan="2">Store (j)</td><td colspan="5"> $X_1$ </td><td rowspan="2"> $X_2$ </td><td rowspan="2"> $X_3$ </td><td rowspan="2"> $X_4$ </td><td rowspan="2"> $Y_1$ </td><td rowspan="2">Expected  $E_j^A$ </td></tr><tr><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td></tr><tr><td>1</td><td>3</td><td>6</td><td>10</td><td>46</td><td>12</td><td>1105</td><td>20,738</td><td>242,766</td><td>429,702</td><td>1.107</td></tr><tr><td>2</td><td>3</td><td>5</td><td>10</td><td>46</td><td>20</td><td>1480</td><td>17,036</td><td>192,812</td><td>511,580</td><td>1</td></tr><tr><td>3</td><td>3</td><td>4</td><td>6</td><td>33</td><td>11</td><td>725</td><td>13,449</td><td>112,663</td><td>315,030</td><td>1.002</td></tr><tr><td>4</td><td>3</td><td>5</td><td>10</td><td>38</td><td>15</td><td>1159</td><td>16,555</td><td>149,268</td><td>338,125</td><td>1.278</td></tr><tr><td>5</td><td>2</td><td>4</td><td>5</td><td>23</td><td>12</td><td>1089</td><td>14,999</td><td>103,735</td><td>227,099</td><td>1.379</td></tr><tr><td>6</td><td>4</td><td>5</td><td>10</td><td>50</td><td>27</td><td>1615</td><td>30,323</td><td>218,924</td><td>654,914</td><td>1</td></tr><tr><td>7</td><td>2</td><td>3</td><td>7</td><td>17</td><td>12</td><td>753</td><td>12,746</td><td>55,072</td><td>171,244</td><td>1.045</td></tr><tr><td>8</td><td>3</td><td>5</td><td>7</td><td>42</td><td>13</td><td>1354</td><td>20,431</td><td>253,009</td><td>357,602</td><td>1.341</td></tr><tr><td>9</td><td>3</td><td>6</td><td>13</td><td>48</td><td>14</td><td>1790</td><td>25,354</td><td>224,362</td><td>470,086</td><td>1.112</td></tr><tr><td>10</td><td>2</td><td>3</td><td>3</td><td>17</td><td>10</td><td>696</td><td>10,371</td><td>108,672</td><td>142,305</td><td>1.741</td></tr><tr><td>11</td><td>3</td><td>6</td><td>7</td><td>49</td><td>20</td><td>1645</td><td>20,577</td><td>214,626</td><td>463,640</td><td>1.108</td></tr><tr><td>12</td><td>3</td><td>6</td><td>7</td><td>49</td><td>20</td><td>1645</td><td>20,577</td><td>214,626</td><td>463,640</td><td>1.108</td></tr></table>

## 4.5. Stage 5

Under the input and output data of all 12 stores depicted in Table 4, the relative aggregate ef<sup>fi</sup>ciency of store 12 is calculated as $E _ { 1 2 } ^ { A } = 1 . 1 0 8$ . Consider the situation that the input amounts of store 12 are changed from the <sup>fi</sup>ctitious input amounts (i.e., $n _ { 1 , 1 2 } = 2 0$ $n _ { 2 , 1 2 } = 4 9 , n _ { 3 , 1 2 } = 7 , n _ { 4 , 1 2 } = 6 , n _ { 5 , 1 2 } = 3 , x _ { 2 , 1 2 } = 1 6 4 5 , x _ { 3 , 1 2 } = 2 0 , 5 7 7$ and $x _ { 4 , 1 2 } = 2 1 4 , 6 2 6 )$ ) to the proposal input amounts $( \mathrm { i } . \mathbf { e } . , n ^ { \prime } _ { 1 , 1 2 } = 1 6 ,$ $n _ { { } ^ { 2 } , 1 2 } ^ { \prime } = 4 1 , \ n _ { { } ^ { 3 } , 1 2 } ^ { \prime } = 9 , \ n _ { { } ^ { \prime } 4 , 1 2 } ^ { \prime } = 5 , \ n _ { { } ^ { \prime } 5 , 1 2 } ^ { \prime } = 3 , \ x _ { { } ^ { \prime } 2 , 1 2 } ^ { \prime } = 1 3 5 8 , \ x _ { { } ^ { 3 } , 1 2 } ^ { \prime } =$ 19,524 and $\boldsymbol { x ^ { \prime } } _ { 4 , 1 2 } = 2 0 1 , 5 3 0 )$ . Then, what is the output target of store $1 2 \ \mathrm { ( i . e . , } \ y ^ { \prime } _ { 1 , 1 2 } \mathrm { ) }$ to keep its expected aggregate ef<sup>fi</sup>ciency score, $E _ { 1 2 } ^ { A } ,$ unchanged? That is, what amount of $Y _ { 1 }$ should store 12 earn to keep $E _ { 1 2 } ^ { A }$ at the level of 1.108? This problem belongs to the inverse DEA [27,29]. Since $E _ { 1 2 } ^ { A } = 1 . 1 0 8 > 1$ , the inverse DEA-CCR model $( \hat { P } )$ [27] is employed to develop an inverse IDEA-CCR model for obtaining the output target of store 12, $y ^ { \prime } { } _ { 1 , 1 2 } ,$ in this case. The proper inverse IDEA-CCR model is proposed as follows (see the development in Appendix):

$$
\begin{array}{l} y _ {1, 1 2} ^ {'} = \text {Min} \sum_ {\ell = 1} ^ {5} n _ {\ell , 1 2} ^ {'} w _ {1 \ell} + \sum_ {i = 2} ^ {4} v _ {i} x _ {i, 1 2} ^ {'} \\ \text {s.t.} \sum_ {\ell = 1} ^ {5} n _ {\ell j} w _ {1 \ell} + \sum_ {i = 2} ^ {4} v _ {i} x _ {i j} - u _ {1} y _ {1 j} \geq 0, j = 1,..., 1 2, \\ u _ {1} E _ {1 2} ^ {A} \geq 1, \\ w _ {1, \ell + 1} \geq \pi_ {\ell} w _ {1 \ell}, \ell = 1, 2, 3, 4, \\ w _ {1 1} \geq v _ {1} \gamma > 0, \\ v _ {1}, v _ {2}, v _ {3}, v _ {4}, u _ {1} \geq \varepsilon . \end{array}\tag{5}
$$

The value of $y _ { 1 , 1 2 } ^ { \prime }$ obtained by model (5) is 443,849, which is the target value of business revenue for store 12 in next period. For determining this value of $y _ { 1 , 1 2 } ^ { \prime }$ in model (5), the maximum weight is $w _ { 1 5 }$ while the minimum weight is $\nu _ { 4 } .$ The store manager and the subsidiary workers of store 12 should devote themselves to develop effective marketing and service plans for delivering this target. Under the expected input and output data of stores 1 to 11 depicted in Table 4 as well as the proposal input data of store 12, if the business revenue delivered by store 12 in next period is the same as $y _ { 1 , 1 2 } ^ { \prime } ,$ , then the aggregate ef<sup>fi</sup>ciency score of store 12 will remain unchanged, viz., stay at the level of 1.108. Of course the aggregate ef<sup>fi</sup>ciency score of store 12 will be better than 1.108 if the business revenue delivered is greater than $y _ { 1 , 1 2 } ^ { \prime } .$ Thus, the output target (i.e., $y _ { 1 , 1 2 } ^ { \prime } { = } 4 4 3 , 8 4 9 )$ is viewed as the minimal amount of business revenue which store 12 should deliver in next period so that its aggregate ef<sup>fi</sup>ciency score can at least maintain the expected level.

## 5. Conclusions

It is seen in the literature that goal-setting and ef<sup>fi</sup>ciency measurement play a pivotal role in current management theory and practice. In order to manage organizational ef<sup>fi</sup>ciency, the questions related to what level of ef<sup>fi</sup>ciency an organization needs to achieve and how it should set appropriate ef<sup>fi</sup>ciency target for the organization need to be resolved.

The issue for measuring ef<sup>fi</sup>ciencies of existing stores and decision-making problem for setting business revenue target of a new store are addressed in this study. The problems are drawn from a home improvement company with 22 chain stores in Taiwan. In order to enhance the service competence to cope with intense competition within the same business sector and to meet the diverse demands of customers, the top management attaches great importance to ef<sup>fi</sup>ciency management. To obtain an objective ef<sup>fi</sup>ciency measurement, the regional managers should not only evaluate the monetary amount of business revenue earned by the stores in their respective regions, but also quantify the performance of resource utilization in earning that revenue. Furthermore, some important considerations arise when developing a proposal to establish a new store. In addition to allotting the input resources for the new store, a regional manager must determine what ef<sup>fi</sup>ciency level the new store should achieve and how much business revenue it should earn. As the company plans to establish new stores each year in different regions, such affairs have become important issues for administration practices, and is thus a problem worthy of investigation. A <sup>fi</sup>vestage approach is developed to deal with the problems under consideration. Since the problems contain strong ordinal data, the suitable IDEA and inverse IDEA models are developed as core techniques of the proposed approach. A simulated application considering the 11 chain stores established in the region of southern Taiwan is presented to illustrate the implementation of the proposed approach.

For ef<sup>fi</sup>ciency measurement, four inputs (manpower, store <sup>fl</sup>oor area, operating expense and number of households in the trade area) and one output (monetary amount of business revenue) are adopted to suit the managerial requirements. Regarding the input manpower, the workers in different ranks are transformed into compound manpower that includes all workers. An IDEA-CCR model is developed to obtain the aggregate ef<sup>fi</sup>ciency for detecting the performance of resource utilization of existing stores, while the BCC model is employed to obtain the value of $\boldsymbol { v } _ { 0 }$ for detecting the status of returns-to-scale. The input and output amounts of existing stores are then adjusted according to the status of returnsto-scale.

In the process of establishing a new store, the regional manager must set a challenging but attainable ef<sup>fi</sup>ciency level for the new store and allot the amounts of input resources for it. Then, the target of business revenue should be properly set for the new store. This target is viewed as the minimal amount of business revenue which the new store should deliver in next period so that its aggregate ef<sup>fi</sup>ciency score can at least maintain the expected level. Under the ef<sup>fi</sup>ciency-driven thinking of the regional manager, an inverse IDEA-CCR model is proposed to set the target of business revenue for the new store.

The regional manager agrees that the proposed approach is an effective technique to solve the problems encountered. It will be implemented as a decision support tool in the near future.

## Appendix A

The inverse DEA-CCR model $ { \left( \hat { \mathsf { P } } \right) } [ 2 7 ]$ can be rewritten as follows:

Max $\sum _ { r = 1 } ^ { s } { p _ { r } y _ { r k } ^ { \prime } }$

$$
\text { s.t. } \sum_ {j = 1} ^ {n} \lambda_ {j} x _ {i j} \leq x _ {i k} ^ {\prime}, i = 1,..., m,
$$

$$
\sum_ {j = 1} ^ {n} \lambda_ {j} y _ {r j} \geq E _ {k} ^ {A} y _ {r k} ^ {\prime}, r = 1, \dots , s,
$$

$$
y _ {r k} ^ {\prime} \geq y _ {r k}, \quad r = 1, \dots , s,
$$

where $x _ { i k } ^ { \prime } = x _ { i k } + \Delta x _ { i k } \ge x _ { i k }$ and $y _ { r k } ^ { \prime } { = } y _ { r k } { + } \Delta y _ { r k } { \ge } y _ { r k }$

The dual of model (P̂) is as follows with removing the conditions of $x _ { i k } ^ { \prime } { \ge } x _ { i k }$ and $y _ { r k } ^ { \prime } { \ge } y _ { r k } { \mathrm { : } }$

Min $\sum _ { i = 1 } ^ { m } \nu _ { i } x _ { i k } ^ { \prime }$

$$
\mathrm{s.t.} \sum_ {i = 1} ^ {m} v _ {i} x _ {i j} - \sum_ {r = 1} ^ {s} u _ {r} y _ {r j} \geq 0, j = 1, \dots , n,
$$

$$
u _ {r} E _ {k} ^ {A} \geq p _ {r}, r = 1, \dots , s,
$$

$$
v _ {i}, u _ {r} \geq \varepsilon .
$$

In this study, since the sole output, $Y _ { 1 } ,$ stands for monetary amount of business revenue, hence its unit value can be set as one, $\begin{array} { r } { \mathrm { { V i z } } . , p _ { 1 } = 1 } \end{array}$ By letting the target store k as store 12, changing the product $\nu _ { 1 } x _ { 1 \ k } ^ { \prime }$ as $\nu _ { 1 } x _ { 1 k } ^ { \prime } = \nu _ { 1 } x _ { 1 , 1 2 } ^ { \prime } = \nu _ { 1 } \sum _ { \ell = 1 } ^ { 5 } n _ { \ell , 1 2 } ^ { \prime } \delta ( \ell ) = \sum _ { \ell = 1 } ^ { 5 } n _ { \ell , 1 2 } ^ { \prime } w _ { 1 \ell }$ , changing the product $\nu _ { 1 } x _ { 1 j }$ as $\nu _ { 1 } x _ { 1 j } = \nu _ { 1 } \sum _ { \ell = 1 } ^ { \mathrm { { } ^ { > } } } n _ { \ell j } \delta ( \ell ) = \sum _ { \ell = 1 } ^ { \mathrm { { } ^ { > } } } n _ { \ell j } w _ { 1 \ell }$ and adding the constraints (shown in Eqs. (4.3) and $\left( 4 . 4 \right) )$ to satisfy the strong ordinal relation for input manpower in this case, model (5) is proposed.

## References

[1] R.D. Banker, A. Charnes, W.W. Cooper, Some models for estimating technical and scale ef<sup>fi</sup>ciencies in data envelopment analysis, Management Science 30 (1984) 1078–1092.

[2] L. Botti, W. Briec, G. Cliquet, Plural forms versus franchise and company-owned systems: a DEA approach of hotel chain performance, Omega 37 (2009) 566–578.

[3] A. Charnes, W.W. Cooper, E. Rhodes, Measuring ef<sup>fi</sup>ciency of decision making units, European Journal of Operational Research 2 (1978) 429–444.

[4] Y. Chen, Imprecise DEA — envelopment and multiplier model approaches, Asia-Paci<sup>fi</sup>c Journal of Operational Research 24 (2007) 279–291.

[5] C.F. Chien, F.Y. Lo, J.T. Lin, Using DEA to measure the relative ef<sup>fi</sup>ciency of the service center and improve operation ef<sup>fi</sup>ciency through reorganization, IEEE Transactions on Power Systems 18 (2003) 366–373.

[6] W.D. Cook, J. Zhu, Rank order data in DEA: a general framework, European Journal of Operational Research 174 (2006) 1021–1038.

[7] W.W. Cooper, K.S. Park, G. Yu, IDEA and AR-IDEA models for dealing with imprecise data in DEA, Management Science 45 (1999) 597–607.

[8] W.W. Cooper, K.S. Park, G. Yu, An illustrative application of IDEA (imprecise data envelopment analysis) to a Korean mobile telecommunication company, Operations Research 49 (2001) 807–820

[9] D.K. Despotis, Y.G. Smirlis, Data envelopment analysis with imprecise data, European Journal of Operational Research 140 (2002) 24–36.

[10] N. Donthu, E.K. Hershberger, T. Osmonbekov, Benchmarking marketing productivity using data envelopment analysis, Journal of Business Research 58 (2005) 1474–1482.

[11] N. Donthu, B. Yoo, Retail productivity assessment using data envelopment analysis, Journal of Retailing 74 (1998) 89–105.

[12] L. Fitzgerald, P. Moon, Performance Measurement in Service Industries: Making It Work, CIMA, 1996.

[13] G.R. Jahanshahloo, F.H. Lot<sup>fi</sup>, N. Shoja, G. Tohidi, S. Razavyan, The outputs estimation of a DMU according to improvement of its ef<sup>fi</sup>ciency, Applied Mathematics and Computation 147 (2004) 409–413.

[14] G.R. Jahanshahloo, F.H. Lot<sup>fi</sup>, N. Shoja, G. Tohidi, S. Razavyan, Input estimation and identi<sup>fi</sup>cation of extra inputs in inverse DEA models, Applied Mathematics and Computation 156 (2004) 427–437.

[15] C. Kao, Interval ef<sup>fi</sup>ciency measures in data envelopment analysis with imprecise data, European Journal of Operational Research 174 (2006) 1087–1099.

[16] C. Kao, H.T. Hung, Ef<sup>fi</sup>ciency analysis of university departments: an empirical study, Omega 36 (2008) 653–664.

[17] C. Kao, S.N. Hwang, T. Sueyoshi, Management performance evaluation: data envelopment analysis, Hwatai Publishing Co., Taipei, 2003 (in Chinese), 18.

[18] C. Kao, S.T. Liu, Fuzzy ef<sup>fi</sup>ciency measures in data envelopment analysis, Fuzzy Sets and Systems 113 (2000) 427–437.

[19] S. Lertworasirikul, S.C. Fang, J.A. Joines, H.L.W. Nuttle, Fuzzy data envelopment analysis (DEA): a possibility approach, Fuzzy Sets and Systems 139 (2003) 379–394.

[20] X. Luo, N. Donthu, Assessing advertising media spending inef<sup>fi</sup>ciencies in generating sales, Journal of Business Research 58 (2005) 28–36.

[21] D.T. Otley, Accounting Control and Organizational Behaviour, CIMA, 1987.

[22] D. Otley, Performance management: a framework for management control systems research, Management Accounting Research 10 (1999) 363–382.

[23] K. Sarica, I. Or, Ef<sup>fi</sup>ciency assessment of Turkish power plants using data envelopment analysis, Energy 32 (2007) 1484–1499.

[24] C. Serrano-Cinca, Y. Fuertes-Callen, C. Mar-Molinero, Measuring DEA ef<sup>fi</sup>ciency in Internet companies, Decision Support Systems 38 (2005) 557–573.

[25] S. Sun, Assessing joint maintenance shops in the Taiwanese Army using data envelopment analysis, Journal of Operations Management 22 (2004) 233–245.

[26] Y.M. Wang, R. Greatbanks, J.B. Yang, Interval ef<sup>fi</sup>ciency assessment using data envelopment analysis, Fuzzy Sets and Systems 153 (2005) 347–370.

[27] Q. Wei, J. Zhang, X. Zhang, An inverse DEA model for inputs/outputs estimate, European Journal of Operational Research 121 (2000) 151–163.

[28] D. Wu, Z. Yang, L. Liang, Ef<sup>fi</sup>ciency analysis of cross-region bank branches using fuzzy data envelopment analysis, Applied Mathematics and Computation 181 (2006) 271–281.

[29] H. Yan, Q. Wei, G. Hao, DEA models for resource reallocation and production input/output estimation, European Journal of Operational Research 136 (2002) 19–31.

[30] J. Zhu, Imprecise data envelopment analysis (IDEA): a review and improvement with an application, European Journal of Operational Research 144 (2003) 513–529.

[31] J. Zhu, Ef<sup>fi</sup>ciency evaluation with strong ordinal input and output measures, European Journal of Operational Research 146 (2003) 477-485.

[32] J. Zhu, Imprecise DEA via standard linear DEA models with a revisit to a Korean mobile telecommunication company, Operations Research 52 (2004) 323–329.

Hung-Tso Lin is an associate professor at the Department of Distribution Management, National Chin-Yi University of Technology, Taiwan. Republic of China. He received the Ph.D. degree from National Taiwan University of Science and Technology. His research interest is applying operations research in the management in industries, with articles published in International Journal of Production Research, International Journal of Production Economics, European Journal of Operational Research, International Journal of Manpower and Expert Systems with Applications.
