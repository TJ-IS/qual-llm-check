---
otero_id: 20066
otero_key: "XZ9SPN9V"
title: "Analyzing the online word of mouth dynamics: A novel approach"
authors: "Xian Cao; Timothy B. Folta; Hongfei Li; Ruoqing Zhu"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2024.114306"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analyzing the online word of mouth dynamics: A novel approach

![](/api/attachments/XZ9SPN9V/fulltext/images/d7ea11dda1d34b0b9675af9c4c2e1e023632c2938a620613ceaf125bcc13825c.jpg)

Xian Cao <sup>a,1</sup>, Timothy B. Folta <sup>b,1</sup>, Hongfei Li <sup>c,\*,1</sup>, Ruoqing Zhu <sup>d,1</sup>

<sup>a</sup> Department of Management, College of Business, Illinois State University, 410 S University St., Normal, IL 61761, United States of America

<sup>b</sup> Management & Entrepreneurship Department, School of Business, University of Connecticut, 2011 Hillside Road, Storrs, CT 06268, United States of America

<sup>c</sup> Department of Decisions, Operations and Technology, CUHK Business School, The Chinese University of Hong Kong, 12 Chak Cheung Street, Shatin, N.T., Hong Kong

<sup>d</sup> Department of Statistics, University of Illinois Urbana-Champaign, 605 E. Springfield Ave, Champaign, IL 61820, United States of America

## A R T I C L E I N F O

Keywords: Multi-view sequential canonical covariance analysis Canonical correlation analysis Online word-of-mouth dynamics Dimension reduction Social media

## A B S T R A C T

In today’s digital economy, virtually everything from products and services to political debates and cultural phenomena can spark WOM on social media. Analyzing online WOM poses at least three challenges. First, online WOM typically consists of unstructured data that can transform into myriad variables, necessitating effective dimension reduction. Second, online WOM is often continuous and dynamic. with the potential for rapid, timevarying changes. Third, significant events may trigger symmetric or asymmetric responses across various entities, resulting in “bursty” and intense WOM from multiple sources. To address these challenges, we introduce a new computationally efficient method—multi-view sequential canonical covariance analysis. This method is designed to solve the myriad online WOM conversational dimensions, detect online WOM dynamic trends, and examine the shared online WOM across different entities. This approach not only enhances the capability to swiftly interpret and respond to online WOM data but also shows potential to significantly improve decision-making processes across various contexts. We illustrate the method’s benefits through two empirical examples, demonstrating its potential to provide profound insights into online WOM dynamics and its extensive applicability in both academic research and practical scenarios.

## 1. Introduction

Word of mouth (WOM) is one of the most important forms of communication through which individuals share information about their experiences with products, services, or broader topics [24]. This communication, whether positive or negative, significantly influences others’ emotional and behavioral responses, highlighting the undeniable importance of WOM [18,32,56]. While traditional WOM is generally limited by individuals’ time, location, or social contact boundaries, online WOM is more visible and able to reach a vast number of people in a short period, leading to unprecedented volume and greater awareness [17,20,25]. In today’s digital economy, virtually all entities, ranging from products to public figures, generate WOM on the internet. However, analyzing online WOM presents at least three challenges that may complicate understanding and decision-making processes related to this crucial form of communication.

First, the information conveyed through online WOM is unstructured, including various communication forms such as texts, images, or videos [41]. For instance, a post on platforms like Twitter and Instagram about a new tech gadget may include hashtags, emotive texts, images of the product, and video reviews. To extract meaningful information from such diverse data, researchers often employ machine learning techniques like natural language processing. However, these techniques usually generate a plethora of variables, increasing the need for dimension reduction [55,60]. Second, online WOM is often continuou and dynamic, with the potential for rapid and time-varying changes, unrestricted by time, location, or social interaction [68]. An example of continuous and dynamic online WOM could be the discussion on Reddit about Adobe Photoshop, where users share various tips and solutions daily. As such, understanding these time-varying trends is crucial for appropriate responses. Third, significant events may trigger symmetric or asymmetric reactions across various entities, generating “bursty” and intense WOM from multiple sources [63]. This requires an understanding of shared WOM across different entities such as competing brands, diverse opinions, and various market segments. For instance, during the release of the Samsung Galaxy Note 7, reports of devices catching fire went viral, not only damaging Samsung’s reputation but also prompting scrutiny of the safety features of other smartphone brands. Marketing and management researchers have long recognized that positive or negative WOM can spill over from a focal firm to its competitors $[ 1 0 , 1 3 , 1 6 ]$ , and the internet has dramatically enlarged these possibilities. Such incidents highlight the critical need to monitor online WOM to understand both direct impacts on a single entity and broader effects across multiple entities, demonstrating the extensive reach and influence of online WOM in the modern digital landscape.

This paper presents a methodology that overcomes the challenges mentioned above. In particular, we introduce a novel approach—multi view sequential canonical covariance analysis (MultiSeqCCoA), which is an extension of canonical correlation analysis (CCA) [23,53] and multi-view canonical correlation analysis (Multi-view CCA) [33,57,65,66]. In statistics, a “view” represents a set of variables from a plane or a single design matrix. Intuitively, “views” represent various entities, such as rival firms, competing brands, platforms, or market segments.

MultiSeqCCoA offers substantial advancements over existing tech niques in analyzing online WOM dynamics, tailored to meet specific analytical challenges mentioned above. First, this method excels at reducing the dimensionality of diverse and unstructured data typical of online WOM, including texts, images, and videos. This reduction simplifies data analysis and enhances interpretability, making it easier to handle the vast quantities of information generated daily. Second, MultiSeqCCoA is adept at identifying and tracking both continuous and dynamic trends in online discussions by accurately computing the covariance structure. This capability provides detailed insights into both persistent dialogues and rapid shifts in sentiments, essential for understanding the dynamic nature of online discussions. Third, the method extends its capabilities to detect shared WOM across multiple entities, a crucial function in today’s interconnected digital marketplace. This functionality becomes particularly crucial when a viral event, such as a new product release, quickly generates “bursty” and intense WOM from multiple sources. Although existing techniques (e.g., principal component analysis, Multi-view CCA, etc.) may partially handle the afore mentioned methodological challenges, none of them can simultaneously solve all the problems. Furthermore, MultiSeqCCoA goes beyond existing techniques by using novel manifold optimization algorithms [35] that provide greater computational efficiency. This improvement is vital for the real-time monitoring and analysis of online WOM, allowing stakeholders to monitor the real-time online WOM and make timely decisions. Integrating these capabilities, MultiSegCCoA has the potential to facilitate a more nuanced understanding of online WOM and enhance the decision-making process by providing timely, actionable insights.

We illustrate the features of MultiSeqCCoA using two empirical examples. One examines the online shared WOM about United Express Flight 3411 across United Airlines and its rivals. The other examines the partisan differences in the online shared WOM during the Covid-19 pandemic. These examples showcase how MultiSeqCCoA addresses the full spectrum of methodological challenges encountered in analyzing online WOM, highlighting the method’s versatility from multiple perspectives. An additional empirical analysis applicable to a different context is also presented.

In addition to its methodological innovations, MultiSeqCCoA offer potential for theoretical and practical applications across various disciplines such as management and marketing, public policy, and causal inference. For example, this method could facilitate researchers to investigate the dynamics of online WOM across industries, offering new insights into the effects of managerial decisions and market trends. Managers could leverage this method to strategically monitor and respond to relevant online WOM, effectively managing stakeholder relationships. Additionally, the method’s capabilities may also support policymakers in analyzing public responses to legislative changes, potentially enhancing the efficacy of policy adjustments. The broad applicability of MultiSeqCCoA suggests it could significantly enhance decision-making processes across diverse disciplines. The full scope of its theoretical and managerial implications will be further elaborated in the

discussion section.

## 2. Literature review

## 2.1. Online WOM dynamics

Myriad conversational dimensions, trajectory dynamics, and concurrent effects across multiple entities pose challenges to the analysis of online WOM. Previous studies discuss the methodological challenges in analyzing online WOM $[ 1 3 , 1 6 , 3 0 , 5 0 ]$ . Still, they do not provide a unifying solution to the three challenges we identify.

For example, Pfeffer et al. [50] observe “online firestorms” and derive generalized factors to understand the online WOM dynamics. They define “online firestorms” as “the sudden discharge of large quantities of messages containing negative WOM and complaint behavior against a person, firm, or group in social media networks.” They acknowledge the speed and volume of WOM spread with time and space. As they mention, Facebook users post a new comment to ING-Diba’s Facebook homepage every five seconds. They also acknowledge that information flows unrestrained among internet users, and the vast majority of individuals are likely to be influenced by others’ opinions. Consequently, Pfeffer et al. [50] recommend using social network analysis to understand users’ network structures better, but they do not provide a solution to the aforementioned methodological challenges.

Chae et al. [16] investigate how seeded marketing campaigns affect WOM spillover effects at the brand and category levels. They find that product seeding increases WOM about the product but decreases WOM about other products of the same brand. It also reduces WOM about competitors’ products in the same category as the focal product. Although Chae et al. [16] provide important implications about WOM spillover effects, their study does not examine the valence of WOM. Thus, it does not examine the underlying WOM trends nor discuss dimension reduction for online WOM.

Borah and Tellis [13] mainly examine the existence of the negative WOM spillover effect, and they call it a “perverse halo effect”. Using a dataset of online chatter for forty-eight nameplates across four car brands, they find that negative WOM about product recall of a focal brand can spillover to its rival brands. They specifically use the generalized impulse response function from the vector autoregressive model to calculate negative WOM spillover effects. However, although their model detects online WOM trends, it assumes fixed time points (e.g., months) while the time-frequency of online WOM is much more intense (e.g., minutes, seconds, etc.). Therefore, analyzing online WOM requires higher computational efficiency, which is not solved in their study. In addition, their parameters of interest are invariant over time.

Gelper et al. [30] investigate the sudden increase of WOM toward the release date of new products, and they call it sudden “spikes.” This study contributes to the WOM dynamic literature by proposing “spikes” as a standalone WOM dimension in addition to volume and valence. They argue that these “spikes” emerge because of spontaneous synchronization of consumer activity, yet their study does not empirically test it.

Table 1 summarizes the findings of the above-selected studies. It is also worth pointing out that another stream of methods for modeling online WOM dynamics includes topic models (e.g., [12]), which are mainly based on Bayesian frameworks. However, these methods cannot simultaneously address problems raised by multiple views and temporal dependency. Furthermore, topic models usually rely on Markov Chain Monte-Carlo, which is computationally expensive. Their underlying model assumption does not necessarily represent the true data gener ating process, which could bias the conclusion. To conclude, the three methodological challenges of analyzing online WOM dynamics have remained unresolved.

## 2.2. Multi-view canonical correlation analysis

We design MultiSeqCCoA based on conventional dimensionality reduced (low-rank) multi-view models [22]. Previous studies also refer to these models as multi-blocks or multi-groups $[ 3 4 , 5 7 , 6 5 , 6 6 ] .$ . “Views” represent a set of data matrices collected simultaneously from different data sources. They may not share the same variables (i.e., columns), but the same row from each data matrix corresponds to the data collected simultaneously. The essential ideas of these models can be traced back to CCA [35,58,59], which seeks to maximize the correlation between the linear combination of two sets of variables. However, CCA focuses on only two sets of variables from two views. Subsequent research extends the context to multiple views [14,39,65], i.e., Multi-view CCA. Researchers have used Multi-view CCA to develop nonlinear approaches $[ 3 , 4 0 ]$ and deep learning algorithms [6]. Its application has spanned various scientific fields, including bioinformatics, chemometrics, operational research, psychometrics, text mining, impact processing, and more.

Table 1  
Selected Studies of Online WOM Dynamics.

<table><tr><td>Study</td><td>Research Question</td><td>Methodological Challenges Raised</td><td>Empirical Solutions Suggested</td><td>Dimension Reduction</td><td>Dynamic WOM</td><td>Concurrent</td></tr><tr><td>Pfeffer et al. [50]</td><td>The new possibilities and challenges presented by online feedback mechanisms</td><td>The speed, volume, and unrestraint of WOM spread</td><td>Social network analysis to understand network structures of users</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Chae et al. [16]</td><td>How seeded marketing campaigns affect WOM spillover effects at the brand and category levels</td><td>WOM spillover effects</td><td>Investigate WOM spillover effect using the number of relevant posts about the focal product, brand, or competitors&#x27; product</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Borah and Tellis [13]</td><td>The existence of negative WOM spillovers</td><td>WOM spillover effects</td><td>Vector autoregressive model</td><td>X</td><td>√</td><td>X</td></tr><tr><td>Gelper et al. [30]</td><td>The WOM &quot;spikes&quot; before new products launching</td><td>“Spikes” as a standalone dimension</td><td>Comprehensive descriptive analysis</td><td>X</td><td>X</td><td>X</td></tr></table>

While Multi-view CCA can detect the correlation across different views, it does not account for the time dimension. A naïve method to involve the time dimension into Multi-view CCA is to select multiple subsets of the whole periods $( \mathrm { i . e . } ,$ , successive time buckets) and analyze the correlation within each subset. Prior literature has used this idea in Multi-view CCA to solve multiple directions successively by removing the effects of previous directions and repeatedly applying the algorithm over all time points [34,57,66]. However, this idea ignores that successive time points are likely to share related information $( \mathrm { i . e . , }$ , the dependency between two successive time buckets), leading to an unsmoothed outcome. Since this idea fails to leverage the information shared between successive time points, it also has low computational efficiency. In short, most existing studies $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } _ { }$ , [22,28,42]) can only be applied to two views and do not address temporal dependency [66]. None of the existing dimensionality-reduced (low-rank) multi-view models can simultaneously handle all these methodological challenges noted above in analyzing online WOM, or doing so would dramatically decrease the efficiency of such efforts.

To address the challenges mentioned above, we first introduce the time dimension into Multi-view CCA. We further impose an all-pairwise orthogonality criterion of the loading vectors to search jointly for multiple shared canonical covariance directions over time. The problem then can be viewed as an optimization request on the Stiefel manifold [2]. To this end, we utilize a computationally efficient algorithm that preserves the orthogonality exactly over time. In particular, we use covariance instead of correlation, following a series of covariance-based criteria, originated from Tucker [58] and extended by Westerhuis et al. [65], Hanafi and Kiers [33], and many others. Van de Geer [61]’s MAXDIFF stationary criteria can be viewed as a special case of our MultiSeqCCoA when there are no time-varying effects and only two views. This new method can also automatically solve the standard ca nonical correlation analysis through simple algebra. Table 2 compares the features of existing techniques with MultiSeqCCoA.

Table 2  
Comparison among Different Techniques on Analyzing WOM.

<table><tr><td>Techniques</td><td>Dimension Reduction</td><td>Correlation Analysis</td><td>Dynamic Analysis</td><td>Multiple Views</td></tr><tr><td>Multiple Regression Principal</td><td>X</td><td>√</td><td>X</td><td>X</td></tr><tr><td>Component Analysis (PCA)</td><td>√</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Principal Component Regression (PCR)</td><td>√</td><td>√</td><td>X</td><td>X</td></tr><tr><td>Time Series Analysis</td><td>X</td><td>√</td><td>√</td><td>X</td></tr><tr><td>CCA</td><td>√</td><td>√</td><td>X</td><td>X</td></tr><tr><td>Multi-viewCCA</td><td>√</td><td>√</td><td>X</td><td>√</td></tr><tr><td>MultiSeqCCoA</td><td>√</td><td>√</td><td>√</td><td>√</td></tr></table>

## 3. Methodology

We start with notations of a standard CCA. Consider two matrices $\mathbf { X } _ { 1 } \in \mathbb { R } ^ { n \times p _ { 1 } }$ and $\mathbf { X } _ { 2 } \in \mathbb { R } ^ { n \times p _ { 2 } }$ , that represent the information collected from two views, such as two rival firms or products, respectively. The standard CCA searches for two vectors $\mathbf { w } _ { 1 } \in \mathbb { R } ^ { p _ { 1 } }$ and $\mathbf { w } _ { 2 } \in \mathbb { R } ^ { p _ { 2 } }$ by maximizing the correlation between ${ \bf X } _ { 1 } \mathbf { w } _ { 1 }$ and ${ \bf X } _ { 2 } { \bf w } _ { 2 } .$ . This formulation is equivalent to solving the following constrained optimization problem:

maximize $\big ( \mathbf { X } _ { 1 } \mathbf { w } _ { 1 } \big ) ^ { \prime } \mathbf { X } _ { 2 } \mathbf { w } _ { 2 }$

subject to $\left\| \mathbf { X } _ { j } \mathbf { w } _ { j } \right\| = 1 , \operatorname { f o r } j = 1 , 2$

(1)

where $\| \bullet \|$ is the $\ell _ { 2 }$ norm. In the above equation, $\mathbf { w } _ { 1 }$ and $\mathbf { w } _ { 2 }$ are vectors that only contain information from one direction $( K = 1$ , denote the number of directions as K). When we are interested in finding multiple $( K > 1 )$ directions, we jointly search for loading matrices ${ \bf W } _ { 1 } \in  \qquad $ $\mathbb { R } ^ { p _ { 1 } \times K }$ and $\mathbf { W } _ { 2 } \in \mathbb { R } ^ { p _ { 2 } \times K }$ such that the correlation between the corresponding columns in $\mathbf { X } _ { 1 } \mathbf { W } _ { 1 }$ and ${ \bf X } _ { 2 } { \bf W } _ { 2 }$ is maximized. One of the many equivalent formulations $[ 2 4 , 4 3 , 6 6 ]$ of this problem is:

maximize $\mathbf { T r } [ ( \mathbf { X } _ { 1 } \mathbf { W } _ { 1 } ) ^ { ' } \mathbf { X } _ { 2 } \mathbf { W } _ { 2 } ]$

subject to $\left( \mathbf { X } _ { j } \mathbf { W } _ { j } \right) ^ { \prime } \mathbf { X } _ { j } \mathbf { W } _ { j } = \mathbf { I } _ { K } , \operatorname { f o r } j = 1 , 2$

(2)

where $\mathbf { I } _ { \mathrm { K } }$ is a $K \times K$ identity matrix and $\mathbf { T r } ( \cdot )$ is the trace.

Researchers generalize this problem from two views to multiple views. It should be noted that a unique solution might not exist in such settings. However, it still provides a useful summary of joint signals from multiple views. To be specific, let n be the number of unique time points at which the data are collected for each view. Without loss of generality, we assume that each data matrix X is ordered row-wise based on the increasing order of time. In this case, we may be interested in the following question: are the CCA directions during the first h $( h \leq n )$ time points the same as the second h time points? In analyzing online WOM, a related question can be – does the online shared WOM trend across rivals remain the same from the first month to the second? If not, are we able to detect the changes? To this end, we propose a covariance-based criterion and solve the joint optimization problem successively for all time points.

To demonstrate this idea in the case where the number of views $D =$ $^ { 2 , }$ for all t ranging from 1 to $T ,$ where $T = n - h + 1$ , let $\mathbf { X _ { j } ^ { [ t ] } }$ be ${ \tt a } h \times p$ sub-matrix of $\mathbf { X _ { j } }$ , for $j = 1 , 2$ . When the rows of $\mathbf { X _ { j } }$ are meaningfully sorted, $\mathbf { X _ { j } ^ { [ t ] } }$ is essentially the $t ^ { t h }$ row to $( t + h - 1 ) ^ { t h }$ of $\mathbf { X _ { j } }$ . Hence, h is a bandwidth that imposes a restricted time interval and serves the purpose of smoothness for any local estimators [54] and we may choose to center $\mathbf { X } _ { j } ^ { [ t ] }$ if needed. However, different methods will lead to different interpretations. In our analysis, we choose not to center $\mathbf { X } _ { j } ^ { [ t ] }$ that leads to a type of gram matrix instead of a covariance matrix between two views. Now, we solve for the loading matrices $\mathbf { W } _ { 1 } ^ { ( t ) }$ and $\mathbf { W } _ { 2 } ^ { ( t ) }$ through

maximize $\mathbf { T r } \Big [ \left( \mathbf { X } _ { 1 } ^ { [ t ] } \mathbf { W } _ { 1 } ^ { ( t ) } \right) ^ { \prime } \mathbf { X } _ { 2 } ^ { [ t ] } \mathbf { W } _ { 2 } ^ { ( t ) } \Big ]$

subject to $\mathbf { W } _ { j } ^ { ( t ) ^ { \prime } } \mathbf { W } _ { j } ^ { ( t ) } = \mathbf { I } _ { \mathrm { K } } , \mathbf { f o r } \mathbf { j } = 1 , 2$

(3)

Fig. 1 shows an example of the concrete computing process of our proposed method. In this example, we collect data from 10 time periods $( n = 1 0 )$ . We execute MultiSeqCCoA every $4 ( h = 4 )$ time periods. We totally need to compute $n - h + 1 = 7$ times, denoted by $T ,$ and the submatrices we use for each computation are respectively denoted by, $\mathbf { X } _ { j } ^ { [ t ] } , t = 1 , . . . , T ,$ where j denotes the $j ^ { t h }$ view.

Although we switch the constraint. the above formulation can still be used to solve the traditional canonical correlation problem. We can execute this solution by simply multiplying the root of the covariance matrix $\boldsymbol { \Sigma _ { j } ^ { t } } = \mathbf { X } _ { j } ^ { [ t ] ^ { \prime } } \mathbf { X } _ { j } ^ { [ t ] }$ to its corresponding loading matrix $\mathbf { W } _ { j } ^ { ( t ) }$ and solve for an equivalent problem. A detailed explanation is provided in Appendix A.1. However, the time-varying scale change of $\Sigma _ { \mathrm { j } } ^ { \mathrm { t } }$ may affect the solution, making the result less stable. Hence, we choose to use the covariance formulation instead of the correlation formulation.

In sum, our formulation has several unique advantages for addressing online WOM dynamics. First, there is a significant overlap between $\mathbf { X } _ { j } ^ { [ t ] }$ and $\mathbf { X } _ { j } ^ { [ t + 1 ] }$ ; they contain just one different row by construction. Hence, we would expect a certain smoothness of $\mathbf { W } _ { 1 } ^ { ( t ) }$ over $t ,$ making the solution more interpretable. Second, by observing the overtime (argument t) drift of the loading matrices $\mathbf { W } _ { 1 } ^ { ( t ) }$ and $\mathbf { W } _ { 2 } ^ { ( t ) }$ , we can detect the time-varying online WOM trends and relate these trends with specific critical incidents. Third, the covariance criterion, instead of correlation, allows the loading matrices to be less sensitive to the scale change of $\mathbf { X } _ { j } ^ { [ t ] }$ overtime. Note that such a time-varying scale change of the data matrix is inevitable in practice. Fourth, dissimilar to existing methods that can only solve for one column of $\mathbf { W } _ { j } ^ { ( t ) }$ at a time, our proposed optimization approach can efficiently solve $\mathbf { W } _ { j } ^ { ( t ) } { \bf \bar { s } }$ on the Stiefel manifold. Moreover, we can take advantage of the sequential nature and use a warm start for optimization.

![](/api/attachments/XZ9SPN9V/fulltext/images/90184dc6213ef5ff81c9e8e63fd0eb4d5fae7c18830d75dc0619524f1fdde6e7.jpg)  
Fig. 1. An Example Showing the Computing Process.  
Notes: Fig. 1 describes an example of the computing process. In this example, the total periods $n = 1 0 ;$ the bandwidth $h = 4 ;$ the total computation times $T =$ $n - h + 1 = 7 ;$ j denotes $j ^ { t h }$ view. The structure (n, h, T) of all the views should be the same to guarantee the execution of MultiSeqCCoA.

Finally, we incorporate the multi-view nature that requires us to consider more than two data matrices. The joint problem takes care of all pair-wise covariance structure among D views. Hence, we solve the following problem sequentially for all $t = 1 , . . . , T \colon$

$$
\text { maximize } \sum_ {j <   k} ^ {D} \mathbf {T r} \left[ \left(\mathbf {X} _ {j} ^ {[ t ]} \mathbf {W} _ {j} ^ {(t)}\right) ^ {\prime} \mathbf {X} _ {k} ^ {[ t ]} \mathbf {W} _ {k} ^ {(t)} \right]
$$

subject to $\mathbf { W } _ { j } ^ { ( t ) ^ { \prime } } \mathbf { W } _ { j } ^ { ( t ) } = \mathbf { I } _ { K } , \mathbf { f o r } j = 1 , . . . , D$

(4)

Throughout the rest of the paper, we refer to the above problem over the entire domain of t as MultiSeqCCoA. For ease of interpretation and to illustrate the evolution from Multi-view CCA to MultiSeqCCoA, we have visualized the structure of their results in Appendix A.2. We present the technical details for solving the optimization problem defined in (4) in the Appendix A.3. Table 3 summarizes all the notations and quantities we need throughout this paper.

## 4. Adoption of MultiSeqCCoA in practice

The use of MultiSeqCCoA involves the input data structure, several important tuning parameters (i.e., K and $h ) ,$ , and outputs $( \mathrm { i . e . , } \mathbf { W } _ { j } ^ { ( t ) }$ and $\mathbf { T r } ^ { ( t ) } )$ . This section will provide general guidelines for choosing the input data structure and tuning parameters and will discuss the implications of outputs. We then provide quantitative evidence on how MultiSeqCCoA dominates other traditional methods using simulations.

Table 3  
Notations throughout this Paper.

<table><tr><td colspan="2">Notations</td><td>Description</td><td>Details</td></tr><tr><td>K</td><td></td><td>Number of directions</td><td>The objective dimensions we achieve by MultiSeqCCoA. This can be viewed as an analog of the number of directions in the PCA.</td></tr><tr><td>h</td><td></td><td>Bandwidth</td><td>In our method, we solve the direction within a restricted time interval. This parameter specifies the width of this time interval. If h = n, then this reduces to a Multi-view CCA.</td></tr><tr><td>n</td><td>Number of observations of each view</td><td colspan="2">The data is collected on the same grid of n time points.</td></tr><tr><td rowspan="2">T</td><td>Number of time points on which</td><td rowspan="2" colspan="2"> $T = n - h + 1$ , where h is bandwidth.</td></tr><tr><td>MultiSeqCCoA is solved</td></tr><tr><td>D</td><td>Number of views</td><td colspan="2">The number of design matrices, such as the number of rival firms, platforms, or products.</td></tr><tr><td> $p_j$ </td><td>Dimension of a specific view</td><td colspan="2">For simplicity, we assume  $p_j = p, \forall j = 1, ..., D$ .</td></tr><tr><td> $X_j$ </td><td>Design Matrix of  $j^{th}$  view</td><td colspan="2">The dimension of  $X_j$  is n by  $p_j$ </td></tr><tr><td> $X_j^{[t]}$ </td><td>A submatrix of  $X_j$  from the  $t^{th}$  row to $(t + h - 1)^{th}$  row</td><td colspan="2">t is the index of time that runs through 1 to T.</td></tr><tr><td> $W_j^{(t)}$ </td><td>Loading Matrix at time t</td><td colspan="2">At each time point t, we solve for the loading directions that maximize the trace of the covariance/g matrix.</td></tr><tr><td> $\mathbf{Tr}^{(t)}$ </td><td></td><td>Trace</td><td>The summation of the diagonal elements of a matrix at time t.In our context, Trace represents the concordance of variables from different views.</td></tr></table>

## 4.1. Inputs of MultiSeqCCoA

The input structure for MultiSeqCCoA requires a meticulously organized set of time series matrices. Each matrix in this set represents a view $( \boldsymbol { \mathrm { e } } . \boldsymbol { \mathrm { g } } . ,$ firm) and adheres to a uniform dimension of $n \times p ,$ where n denotes the number of time periods and $p$ signifies the number of variables under examination, as explained in Table 3. Within each matrix, rows correspond to sequential time points, while columns represent the various attributes or variables being measured. The cell values in these matrices contain the quantitative measurements of each variable at the respective time points. To facilitate the analysis of shared trends across multiple views, researchers must compile these matrices into a comprehensive list, ensuring that all matrices maintain consistent dimensions and variable definitions. This standardized input format enables MultiSeqCCoA to effectively identify and analyze shared patterns and components across the temporal sequences of multiple views simultaneously.

## 4.2. Tuning parameters of MultiSeqCCoA

There are two user-defined parameters in MultiSeqCCoA. One is $K ,$ which is defined as the number of directions. K is similar to the number of principal components used in traditional dimension reduction methods. In practice, it is recommended to set $K = 1 \mathrm { o r } K = 2$ since the first several directions have already explained most variations in the original data. And this is common for data visualization purposes in dimension reduction, such as PCA. Another user-defined parameter is bandwidth $h ,$ which describes the range of the neighborhood for a particular time point t where we are searching for the shared signal $( \boldsymbol { \mathrm { e } } . \boldsymbol { \mathrm { g } } . ,$ online shared WOM). A small bandwidth h presents a more sensitive analysis and can be used when the shared signal may change dramatically in a short amount of time. A large bandwidth h, on the other hand, is more stable and less sensitive. The difference between a short and long bandwidth h can be considered as reflecting the bias-variance tradeoff [29], which are inevitable in statistical analysis. We recommend band width h such that it is much larger than $p _ { j }$ for all $j ;$ that means the number of rows in the local data matrix $\mathbf { X } _ { j } ^ { [ t ] }$ is much larger than the number of columns. For example, when analyzing an hourly dataset spanning a year, a one to three-day bandwidth may be suitable for identifying minor, recurring weekly trends. However, to detect more pronounced signals that persist over several months, employing a twoweek to one-month bandwidth could yield superior results. In essence, there is no universally optimal bandwidth. The choice is predominantly dictated by the specific analytical goals of the user.

## 4.3. Outputs of MultiSeqCCoA

First. the loading matrix $\mathbf { W } _ { j } ^ { ( t ) }$ can be viewed as an analog of the loadings when constructing a CCA or PCA at a given time point t. It represents the weight of each variable contributing to the association between each pair of views. In analyzing online WOM, it shows the contribution of a particular sentiment or an emotion to the overall WOM trends across multiple entities. In addition, the loading matrix $\mathbf { W } _ { j } ^ { ( t ) }$ allows us to calculate the corresponding projected scores as linear combinations of original variables and the loading matrix $( \mathrm { i . e . , } \mathbf { X } _ { j } ^ { [ t ] } \mathbf { W } _ { j } ^ { ( t ) } )$ for each view j at each time point t. In analyzing online WOM, it rep resents composite sentiment or emotion scores derived from each entity.

Second, the trace $\mathbf { T r } ^ { ( \mathbf { t } ) }$ represents the overall shared signal among different views at a time point t. It is the sum of shared signal among D directions $( \mathrm { i . e . , \sum _ { j < k } ^ { D } { \bf T r } } \Big [ \left( { \bf X } _ { j } ^ { [ t ] } { \bf W } _ { j } ^ { ( t ) } \right) ^ { \prime } { \bf X } _ { k } ^ { [ t ] } { \bf W } _ { k } ^ { ( t ) } \Big ] )$ ) that can be interpreted as the total variation explained by the top D principal components in the traditional dimension reduction methods. This summation changes over time and indicates the concurrent association among all views. Thus, it allows us to analyze the online shared WOM dynamics.

## 4.4. Testing MultiSeqCCoA using synthetic data

We manually generated synthetic data to test the performance of MultiSeqCCoA. As mentioned above, one novelty of our method is to introduce time dependency into multiple-view dimension reduction methods. Time dependency is particularly interesting in the online WOM context, in which the dynamic trends of WOM are crucial for managers. In addition, our method is computationally efficient for learning multiple dimension reduction directions using the Stiefel manifold optimization approach. We first tested whether our method could accurately estimate loading matrices from observed synthetic data. We then compared the running time of our method with a naïve approach to illustrate the improved computation efficiency. For the first task, we generated synthetic data under known loading matrices. Then we used MultiSeqCCoA to estimate the loading matrices from the synthetic data and compared our estimation with the true loading matrices. For the second task, we compared the running time of MultiSeqCCoA and other naïve methods. We show the details of this session in Appendix B. The results of this simulation study confirm that Multi-SeqCCoA can indeed “recover” the true loading matrices with less time, indicating the accuracy and efficiency of our novel approach.

## 5. Empirical examples

In the following, we provide two empirical examples to illustrate the features of MultiSeqCCoA. The first example examines the online WOM dynamics about an incident on United Express Flight 3411 (hereafter, the Incident). The second example discusses the partisan differences in online WOM during the Covid-19 pandemic. These two examples contain all the aforementioned methodological challenges in analyzing online WOM and have different features that illustrate the use of MultiSeqCCoA from different angles. First, the Incident example features one significant event that allows us to analyze the online WOM dynamics before., during, and after the event. It also allows us to observe the possible WOM spillover effects from United Airlines to its rivals due to the Incident. In the Covid-19 example, we do not have clear preacknowledged events. Instead, we visualized the online WOM dynamics first and then identified the events retrospectively. In this sense, we used MultiSeqCCoA as an event detector in addition to understanding online WOM dynamics. Second, the volume of online WOM in the Covid-19 example is massive and continuous, while the volume of online WOM in the Incident example is relatively smaller and “bursty.” The different data features allow us to illustrate the use of different band widths h.

## 5.1. Study 1: The united express flight 3411 incident

On April 9, 2017, passenger David Dao was forcibly removed from the flight after Dao refused to leave the aircraft voluntarily. A video showing Dao screaming as officers pulled him out of his seat and dragged him down the aisle by his arm had spread quickly and widely on social media, sparking outrage across the internet.<sup>2</sup> In addition, people started to pay greater attention to airline service and how other airlines treated customers relative to the Incident. Since WOM resulting from a reputational crisis can spread to other firms offering similar products or services [10], we wonder (1) whether the online WOM regarding the Incident might spillover from United Airlines to its rivals; and (2) whether the spillover effect was more dramatic for United Airline's direct competitors than for its indirect competitors.

## 5.1.1. Data

Our sample includes Facebook posts and user comments of eleven U. S. major airlines in competition $( \mathrm { i . e . , }$ United Airlines, American Airlines, Delta, Spirit Airlines, Flyfrontier, Southwest, Allegiant, Alaska Airlines, JetBlue, Virgin America, and Hawaiian Airlines). We specifically observe the online WOM between January and October 2017. The data collected via the Facebook Graph API in November 2017 includes 2832 airlines’ Facebook posts and 301,936 user comments. Appendix C.1 presents the detailed number of posts and comments.

We employed the Linguistic Inquiry and Word Count (LIWC) [47] to parse the information conveyed by user comments. The LIWC has been widely used in the psychology literature and also introduced to business domains, such as management information systems and marketing (e.g., [60]). It functions by matching the percentage of words in a text to predefined keyword dictionaries to calculate the prevalence of different categories of words [48]. Using the LIWC, we parsed each user’s com ments into 93 variables, including various dimensions such as social words (e.g., “family,” “friends”), biological processes (e.g., “body,” “sexuality”), and psychological processes $( \boldsymbol { \mathrm { e . g . } }$ , “affective processes,” “cognitive processes”). Appendix C.2 shows the detailed descriptions of variables parsed by the LIWC. Since online user comments are not evenly distributed over time, there might be some time points showing no user comments. To reduce the prevalence of such cases, we aggregated user comments per hour for each airline.<sup>3</sup> After this aggregation, if there were any time points with no user comments, we used linear interpolation to fill the missing values. We standardized the data matrix by centering and dividing it by the standard deviation column-wise. Please note that both the demean and non-demean versions (at each time point t) are implemented in our R package. We then used the period weighting by multiplying the log of the summation of the number of comments and likes since some Facebook comments might attract more attention than others. This approach considers social media features of Facebook, and is consistent with other online WOM analyses (e.g., [21]). Our final data contains n = 7403, with each row representing the aggregated sentiment per hour.

In analyzing the spillover effect from United Airlines following the incident. we categorized its competitors based on the number of pre. incident consumer complaints as reported in the November 2016 Air Travel Consumer Report by the U.S. Department of Transportation. This method is grounded in consumer behavior theories suggesting that complaints significantly reflect customer dissatisfaction and perceived service quality $[ 2 6 , 3 6 ]$ . Airlines with similar complaint volumes are likely perceived by consumers as having comparable service quality, positioning them as more direct competitors. Unlike previous studies that used operational metrics like flight route overlaps [51] or airline alliances [38], this approach captures consumer perceptions more effectively, which are vital for understanding online WOM dynamics. As noted by Gr´egoire et al. [27], consumer complaints directly reflect the negative perceptions that significantly influence online discussions, brand loyalty, and purchasing decisions. By using consumer complaint to define competition, we provide a metric that mirrors consumer perspectives on service quality among airlines. With United Airlines receiving the second-highest complaints in November 2016, we identified airlines with more complaints as direct competitors and those with fewer as indirect competitors. This classification offers insights into the competitive landscape from the consumer’s viewpoint, emphasizing factors that directly impact their perceptions and decisions. Table 4

Table 4  
Pre-Incident Number of Complaints.

<table><tr><td>Airlines</td><td>Number of Complaints</td><td>Airlines</td><td>Number of Complaints</td></tr><tr><td>United Airlines</td><td>116</td><td></td><td></td></tr><tr><td>Direct competitors</td><td></td><td>Indirect competitors</td><td></td></tr><tr><td>American Airlines</td><td>183</td><td>Allegiant</td><td>26</td></tr><tr><td>Delta</td><td>65</td><td>Alaska Airlines</td><td>14</td></tr><tr><td>Spirit Airlines</td><td>54</td><td>JetBlue</td><td>12</td></tr><tr><td>Flyfrontier</td><td>40</td><td>Virgin America</td><td>10</td></tr><tr><td>Southwest</td><td>33</td><td>Hawaiian Airlines</td><td>5</td></tr></table>

presents the details.

## 5.1.2. MultiSeqCCoA results

5.1.2.1. The online shared WOM dynamics of direct vs. indirect competitors. We conducted two MultiSeqCCoA analyses, with one analysis on United Airlines’ direct competitors $( \mathrm { i . e . , }$ , the number of views, $D = 6 )$ and the other analysis on its indirect competitors $( \mathrm { i . e . }$ , the number of views, $D = 6 )$ . We set bandwidth $h = 6 7 2$ time points, which span four weeks of signal, to enable enough smoothness. The number of data points $( \mathrm { i } . \mathrm { e } . , 6 7 2 )$ is much larger than the number of variables (i.e., 93), consistent with our recommendation above of choosing a bandwidth h. We also conducted several supplementary analyses using different bandwidths $h ,$ and the results are consistent. The detailed analysis of the different bandwidths can be found in Appendix C.3. We set $K = 1$ to extract one dimension from the original LIWC variables, and the findings of K = 2 are provided in Appendix C.4.

Fig. 2 presents the online shared WOM trends. The red line shows the online shared WOM about United Airlines and its direct competitors (i. e., American Airlines, Delta, Spirit Airlines, Flyfrontier, and Southwest). The green line shows the online shared WOM about United Airlines and its indirect competitors (i.e., Allegiant, Alaska Airlines, JetBlue, Virgin America, and Hawaiian Airlines). As shown, the indirect competitors group had much higher online shared WOM with United Airlines than the direct competitors’ group before the Incident. During the Incident, although the online shared WOM about United Airlines and these two groups all increased, the magnitude of online shared WOM changes was more dramatic for the direct competitors’ group. Around one month after the Incident, the online shared WOM about United Airlines and these two groups all declined. But opposite to the situation before the Incident, the online shared WOM about United Airlines and its direct competitors remained higher.

5.1.2.2. The impact of the incident on the online shared WOM. To study whether the WOM about the Incident spillovered from United Airlines to its rivals, we conducted another MultiSeqCCoA analysis on all airlines (i. e., the number of views $D = 1 1$ and $K = 1 )$ . Then, we calculated the projected scores $\mathbf { X } _ { j } ^ { [ t ] } \mathbf { W } _ { j } ^ { ( t ) }$ . As discussed above, this is an analog to the principal components in PCA. Fig. 3 shows the project scores of United Airlines, which represents a composite online WOM from United Airlines that has the strongest shared signal with all other airlines. As shown, the strongest signal appeared during the Incident and declined after that. In addition, there were several spikes in September and October, possibly due to Hurricane Harvey.

Since the project scores represent one view’s comprehensive shared WOM with others, we can use it as the dependent variable to compare the shared WOM changes across different airlines. Since it is hypothetical that reputational crisis is more likely to spillover to a focal firm’s direct competitor than its indirect competitor [10], we considered the United Airline as the treatment group, its direct competitors as the spillover group, and the indirect competitors as the control group. We then used a DID analysis with two-way fixed effects on airlines and time (i.e., Eq. 5) to identify whether the Incident has any treatment effects on United Airlines and spillover effects on its direct competitors.

Table 5  
![](/api/attachments/XZ9SPN9V/fulltext/images/78a71fcb621afa400853a1021dc22c55ae16a167a25fe4f799a08121867bb071.jpg)  
Fig. 2. United Airline’s Online Shared WOM with its Direct and Indirect Competitors.

![](/api/attachments/XZ9SPN9V/fulltext/images/5de8258203ce12d079b2ed0da5d81028437db51c553103e13d4e92454b0b0948.jpg)  
Fig. 3. Projected Scores of United Airline from January 2017 to October 2017.

$$
P C _ {i t} = \beta_ {0} + \beta_ {1} \text { Treatment } _ {i} \times \text { After } _ {t} + \beta_ {2} \text { Spillover } _ {i} \times \text { After } _ {t} + \lambda_ {i} + \delta_ {t} + \varepsilon_ {i t}\tag{5}
$$

Here $P C _ { i t }$ represents the projected scores of an airline i in at time t, indicating the shared WOM of airline i at time t. Treatment represents whether airline i is in the treatment group (i.e., whether airline i is United Airline) while Spillover indicates whether airline i belongs to the spillover group (i.e., direct competitors). After denotes whether time t i after the Incident. $\lambda _ { i }$ represents the firm-level fixed effects, capturing the effects of time-invariant characteristics of airline i. δ is the time-level fixed effects, which account for any potential temporal shocks at time $t , \varepsilon _ { i t }$ is the random error.

Table 5 shows the results of DID analysis. In Model 1, we used the data aggregated at one hour. In Model 2, we further aggregated the data at one week since a shorter time interval might be associated with some unexpected shocks, which leads to a potential non-parallel trend. As shown, the coefficients of Treatment × After in both models are signifi cantly positive, indicating that the Incident increased the online shared WOM between United Airlines and other airlines. The coefficients of Spillover × After in both models are also significantly positive, indicating a positive spillover of WOM from United Airlines to its direct competitors compared to its indirect competitors. Although both treatment and spillover effects are significant, their magnitudes are quite different. For example, the impact of the Incident on United Airlines WOM (i.e., 2.148) is around four times as much as its direct competitors WOM (i.e., 0.537) in Model (1), indicating that the Incident affected United Airlines most. We conduct the parallel trend tests [1] of the treatment and spillover effects, respectively. The results show that the parallel trend assumption holds for both effects and we show the details in Online Appendix C.5.

DID Analysis of the Treatment and Spillover Effect of United Incident.

<table><tr><td></td><td>(1)</td><td>(2)</td></tr><tr><td>After × Spillover</td><td>0.537**(0.135)</td><td>0.478**(0.150)</td></tr><tr><td>After × Treatment</td><td>2.148***(0.112)</td><td>2.485***(0.059)</td></tr><tr><td>Firm Fixed Effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Time Fixed Effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Number of Companies</td><td>11</td><td>11</td></tr><tr><td>R-squared</td><td>0.016</td><td>0.188</td></tr><tr><td>Observations</td><td>16,368</td><td>99</td></tr></table>

Notes: Robust standard errors clustered by companies in parentheses. $^ { * * * } p <$ $0 . 0 0 1 , ^ { * * } p < 0 . 0 1 , ^ { * } p < 0 . 0 5 , + p < 0 . 1$

In conclusion, the above findings show that the online shared WOM about United Airlines and other airlines significantly increased during the Incident, indicating the online WOM about the Incident spillovered from United Airlines to its rivals. Our analysis also shows that the spillover effect was more dramatic for the direct competitors than for indirect competitors.

## 5.2. Study 2: Partisan differences in online WOM dynamics during Covid 19

Partisan differences significantly influence various societal aspects, including government policy, education, healthcare, and economic stability. The COVID-19 pandemic in the United States, notably characterized as a partisan issue [4], exemplifies this impact. Evidence suggests that individuals from different political spectrums exhibited varying attitudes toward social distancing, perceptions of personal risk from COVID-19, and expectations about the pandemic’s future severity.

Given this context, it is crucial to explore whether these partisan dif ferences extend to the online shared WOM trends during the pandemic. Additionally, we also investigate how these partisan differences in online WOM dynamics might correlate with broader economic uncertainty [5] and use MultiSeqCCoA as an event detector to detect potential events.

## 5.2.1. Data

We used a publicly available Covid-19 Twitter dataset collected by Chen et al. [19] since January 2020. This dataset used the Twitter API to track Covid-19 related keywords such as “Coronavirus,” “Covid-19,” “Pandemic,” etc., in real-time and recorded over 87 million tweets from 13 million Twitter users. For detailed information, please refer to Chen et al. [19]. For each tweet, in addition to tweet information such as tweet text and created date, user metadata, including users’ screen names and self-reported locations at the time of the data collection, is also available.

To study the partisan differences, we followed prior studies and selected Tweets from 20 major U.S. cities according to their party af filiations in the 2016 U.S. presidential election [31]. The top 10 most liberal cities include Baltimore, Washington D.C., Boston, San Francisco, New Orleans, New York City, Seattle, Pittsburgh, Philadelphia, and Austin. The top 10 most conservative cities include Phoenix, Arlington, Oklahoma City, Wichita, Nashville, Omaha, Lexington, Colorado Springs, Virginia Beach, and Jacksonville. Since users’ self-reported profile location is not mandatory information, tweets from users who chose not to disclose their locations were deleted. As with the practice in the Incident example, we standardized the data matrix by centering and dividing it by the standard deviation column-wise. We then used the period weighting by multiplying the log of the summation of the number of retweets and favorites, to take the features of social media into consideration. The final sample includes 2,603,224 tweets from 438,080 unique users between January and July 2020. We used the LIWC to parse each tweet into 93 variables. We then aggregated each variable per hour and filled the missing values using linear interpolation.

## 5.2.2. MultiSeqCCoA results

5.2.2.1. Partisan difference of online shared WOM. We conducted two MultiSeqCCoA analyses, with one analysis on the liberal cities (i.e., the number of views D = 10) and the other analysis on the conservative cities (i.e., the number of views D = 10). We set bandwidth h = 336 time points, equal to two weeks. We selected a smaller bandwidth h in the Covid-19 example because, unlike the Incident example, the WOM in the

Covid-19 example is massive and continuous. A smaller bandwidth h would help us increase the analysis sensitivity and improve signal detections. Similar to Study 1, we also conducted robustness checks using different bandwidths ℎ and the results are consistent. We show the robustness tests of different bandwidths in Appendix D.1. We set K = 1 to extract one dimension from the original LIWC variables, and the findings of K = 2 are provided in Appendix D.2.

Fig. 4 shows the partisan differences in online shared WOM during the Covid-19 pandemic. The red line represents the online shared WOM across ten conservative cities, and the blue line represents the online shared WOM across ten liberal cities. As shown, the online shared WOM of both conservative and liberal cities significantly increased since March and declined toward mid-April. The online shared WOM of both conservative and liberal cities increased again since June, then slightly reduced, increased once again, and fluctuated after that. Even though conservative and liberal cities exhibited similar online shared WOM trends, the magnitude of online shared WOM changes was more dramatic in liberal cities than in conservative cities. We calculated the descriptive statistics of the common trend of conservative and liberal WOM, which are presented in Table 6. We observed that the average of the shared trend of liberal WOM (mean = 298,726.4) is much higher than that of conservative WOM (mean = 140,773.5). To provide more evidence from a statistical inference standpoint, we conducted t-tests to determine whether there is a significant difference between the average of the shared trend of liberal WOM and that of conservative WOM. We performed both a Welch Two Sample t-test and a paired t-test, with the results shown in Table 7.

Both t-test results indicate a significant difference in the means of WOM consistency between these two groups. Specifically, the mean WOM consistency for liberal cities was substantially higher than that for conservative cities, with a 95% confidence interval of [− 165,579.8, − 150,325.9]. This suggests that liberal cities are more likely to achieve alignment in their WOM during the pandemic. These findings align with existing literature on the role of political orientation in social network structures and communication patterns [8,9]. To further elucidate the specific implications of the shared WOM, we also investigate its potential correlation with economic uncertainty using the Cboe Volatility Index (VIX). The detailed analysis is provided in Online Appendix D.3.

Descriptive Statistics of the Common Trend of Conservative and Liberal WOM.

<table><tr><td></td><td>Mean</td><td>SD</td><td>Min</td><td>Median</td><td>Max</td></tr><tr><td>Shared Trend of Conservative WOM</td><td>140,773.5</td><td>86,803.5</td><td>41,041.3</td><td>114,798.5</td><td>389,102.5</td></tr><tr><td>Shared Trend of Liberal WOM</td><td>298,726.4</td><td>236,752.5</td><td>69,583.7</td><td>230,509.4</td><td>990,597.0</td></tr></table>

![](/api/attachments/XZ9SPN9V/fulltext/images/4b413552d3cc173107eeb3c0f5c3c856d264b961fef4305ebd071c7af9b26175.jpg)  
Fig. 4. The Partisan Differences in Online WOM Dynamics.

Table 7  
t-test Results of the Common Trend of Conservative and Liberal WOM.

<table><tr><td colspan="2">Panel 1: Welch Two Sample t-test</td><td colspan="2">Panel 2: Paired t-test</td></tr><tr><td>Statistic</td><td>Value</td><td>Statistic</td><td>Value</td></tr><tr><td>t-value</td><td>-40.6</td><td>t-value</td><td>-67.4</td></tr><tr><td>df</td><td>5309.1</td><td>df</td><td>4200</td></tr><tr><td>p-value</td><td>&lt; 0.001</td><td>p-value</td><td>&lt; 0.001</td></tr><tr><td>95% CI</td><td>[-165,579.8,-150,325.9]</td><td>95% CI</td><td>[-162,550.6,-153,355.1]</td></tr><tr><td>Mean of Conservative</td><td>140,773.5</td><td>Mean of Conservative</td><td>140,773.5</td></tr><tr><td>Mean of Liberal</td><td>298,726.4</td><td>Mean of Liberal</td><td>298,726.4</td></tr></table>

5.2.2.2. Event detection. As mentioned above, there are no preacknowledged events in the Covid-19 example. MultiSeqCCoA might be able to serve as an event detector that helps identify events. In a traditional offline setting, one could use business research services, such as LexisNexis, to search relevant news in the observation window. In the online setting, this information can be conveniently obtained from MultiSeqCCoA outputs. The event detection function can be used to control confounding events, which is the necessary step for any event studies.

Intuitively, when the shared WOM changed (i.e., turning points in Tr), there might be some significant events causing that. To determine the concrete time of an event, we can apply an appropriate change point detection technique [62]. We employed “segmented” [43,44] to detect the dates associated with these changing points in the trace from January 22 to July 31, 2020. “Segmented” is a widely used changepoint analysis method, and its idea is to cut the time series data into pieces and regress the time variable (i.e., dates) on the dependent variable (i.e., trace or online shared WOM). This approach is especially appropriate in our example because the online shared WOM may suddenly go up or down due to events, leading to a piecewise-like trace curve. The key point of this method is to identify the locations where the splits work the best. By doing that, we can then retrospectively detect events that might cause the online shared WOM dynamics. Table 8 shows the results of event detection. Possible events that are associated with the online shared WOM are provided.

To summarize, MultiSeqCCoA can serve as an event detector, which presents unique advantages over conventional event detection methods (e.g., using LexisNexis) since different entities might have completely different reactions to an event. An event may significantly increase the shared WOM in some entities, while leaving the shared WOM in others unaffected. In our Covid-19 example, liberal cities reacted more dramatically to all five events, while conservative cities’ reactions were not significant. MultiSeqCCoA can be used to detect events that might particularly interest some views and can be considered a more precise

Table 8  
Results of Changepoint Detection using Segmented Method.

<table><tr><td>Change Point</td><td>Time</td><td>Possible Events</td></tr><tr><td>1</td><td>2020-02-27 04:56:25 (3.48 h)</td><td>Outbreak of COVID-19</td></tr><tr><td>2</td><td>2020-03-28 21:15:55 (2.70 h)</td><td>Peak of the outbreak</td></tr><tr><td>3</td><td>2020-04-22 00:48:17 (5.65 h)</td><td>Slow-down of the outbreak</td></tr><tr><td>4</td><td>2020-05-29 18:47:23 (3.77 h)</td><td>Outbreak of George Floyd protests</td></tr><tr><td>5</td><td>2020-06-03 10:22:33 (3.69 h)</td><td>Peak of George Floyd protests</td></tr></table>

Notes: Standard errors of estimated changepoints are in parentheses.

view-specific event detector.

While the above two case studies focus on online WOM analysis, MultiSeqCCoA extends beyond this scope. To demonstrate the versatility of our novel approach and provide more instructions to practitioners, we conducted an additional study—“Competitive Analysis of China’s Ecommerce Market.” This study investigates user activity trends and competitive dynamics among major e-commerce platforms in China from 2018 to 2023. Utilizing the MultiSeqCCoA methodology, the study identifies synchronicity and shared trends in user engagement, revealing a trend toward increased market integration, despite disruptions caused by the COVID-19 pandemic. The analysis shows that two of the platforms exhibit the closest competitive relationship, indicated by their highly similar user activity patterns. These insights offer a detailed view of the evolving competitive landscape and user behavior within China’s e-commerce sector. We have included this study in Appendix E.

## 6. Discussion

In today’s digital economy, virtually everything from products and services to political debates and cultural phenomena can spark WOM on social media [57]. In the complex landscape of online WOM, data analysis faces significant challenges including managing the high dimensionality of varied and unstructured data, tracking ongoing and episodic WOM trends, and deciphering the interconnected impacts across diverse entities. Our advanced analytical tool, MultiSeqCCoA, is tailored to overcome these hurdles. It efficiently simplifies complex data from texts, images, and videos, making large information streams both manageable and interpretable. MultiSeqCCoA also adeptly identifies and follows the dynamic trends of WOM, providing real-time insights into both persistent conversations and abrupt changes in the public sentiment. Moreover, its ability to detect and assess WOM across various entities demonstrates its critical role in a connected digital marketplace, offering the comprehensive insights necessary for informed decisionmaking.

MultiSeqCCoA was demonstrated in two distinct scenarios. The first scenario involves the Incident, which provides an ideal context to showcase the method’s ability to manage “bursty” data. The Incident, marked by a sudden surge in online activity following a highly publi cized event, allows MultiSeqCCoA to analyze rapid shifts in public sentiment and interactions not only related to United Airlines but also across its competitors. This example illustrates MultiSeqCCoA’s strength in dimension reduction and detecting nuanced shifts in WOM dynamics, offering clear advantages over traditional methods like PCA that may struggle with the transient nature of such data. The second example examines partisan differences in online WOM during the COVID-19 pandemic, a scenario characterized by continuous and complex data flows. MultiSeqCCoA is instrumental in parsing out the influence of varied political views on the discourse surrounding the pandemic, demonstrating its robustness in handling continuous data and its adeptness at identifying underlying patterns in a vast dataset without clear temporal boundaries. This example showcased the method’s utility in tracking ongoing discussions and its superior performance in handling multidimensional datasets compared to methods like CCA, which may not efficiently capture the dynamics of such extensive data.

## 6.1. Theoretical and managerial implications

MultiSeqCCoA demonstrates its potential to significantly enhance our understanding of online WOM dynamics, providing novel insight that are crucial for academic research and informed decision-making across various fields. In the following discussion, we illustrate its applicability to marketing and management, public policy, and causal inference.

In marketing and management, MultiSeqCCoA could be instrumental in exploring a wide range of critical topics, such as firm reputation and the integrity of online feedback mechanisms. Firm reputation, a strategic asset, markedly influences a firm’s competitive landscape by distinguishing it from competitors [49] and restricting rival’s mobility [15]. By facilitating the empirical examination of reputation’s influences on a firm's competitive landscape, MultiSeqCCoA could enrich theories related to competitive advantage [11], stakeholder theory [46], and dynamic capabilities [67]. This would contribute to a deeper understanding of the mechanisms by which reputations impact firm performance over time. Additionally, this analytical tool could provide actionable data that managers can use to make informed decisions about strategic positioning and reputation management. For instance, during reputational crises, MultiSeqCCoA could enable real-time analysis of WOM dynamics, allowing managers to quickly gauge the impact of negative sentiments and strategically manage their spillover across brands, thus enhancing the firm’s ability to maintain its market position and stakeholder trust.

Furthermore, MultiSeqCCoA could enhance the integrity of online feedback systems, crucial for capturing authentic customer insights. Aligned with current research on information asymmetry (e.g., [52]) and signaling theory (e.g., [64]), this tool could address challenges posed by the quality of WOM and risk of dishonest feedback that may compromise the reliability of these systems [7,37]. MultiSeqCCoA could parse and analyze detailed customer opinions to detect anomalies indicating manipulative activities, such as “phantom” transactions intended to inflate positive feedback or the underlying reasons for polarized feedback. This capability could assist researchers and managers in designing more effective online feedback mechanisms, thus improving strategic decision-making based on a trustworthy source of customer insights.

Turning to public policy, MultiSeqCCoA could facilitate decisionmaking by providing critical tools to analyze public sentiment in response to legislative or regulatory proposals, potentially enhancing policy effectiveness through better alignment with public needs and expectations. For instance, using MultiSeqCCoA to monitor reactions to environmental legislation or healthcare reform could give policymakers detailed feedback on public acceptance and resistance, possibly guiding them to adjust policies in ways that enhance their legitimacy and effectiveness. This tool could contribute to the literature on public opinion and policy responsiveness (e.g., [45]), offering empirical data that may test and refine theories regarding the impact of public senti ment on policy formulation and adjustment.

Our method can also serve as a complementary technique for busi ness causal inference. Investigating cause and effect is a major task in most scientific studies, including the business field. While Multi-SeqCCoA is not specifically designed to infer causality, it can be utilized to enhance causal investigations. Here, we present two potential appli cations of our method in this context. First, one of the outputs of Mul tiSeqCCoA is the trace, which represents a shared trend among multiple entities, such as competing firms’ shared WOM, public’s shared opinions, or the similar development trajectories of various apps or products. This shared trend is a comprehensive variable that consolidates multiple factors into a single measure. This measure can then be employed as either an independent or dependent variable, providing numerous opportunities to explore causality. For instance, our DID analysis in the example of the Incident demonstrates how the generated trace can be used as a dependent variable for causal inference. Second, since the output of MultiSeqCCoA is a time series variable, significant changes in this series may indicate potential shocks or events. This is exemplified by our change point detection results in the analysis of Partisan Differences in the Online WOM Dynamics. Such dynamic analyses can be combined with causal inference methods to determine the causal effects of policy changes or exogenous shocks, akin to the regression discontinuity in time (RDiT) approach. In summary, MultiSeqCCoA is an auxiliary method that enhances researchers’ ability to apply causal inference in specific scenarios. By providing a robust framework for identifying shared trends and detecting significant changes over time, it opens up new avenues for causal exploration and strengthens the analytical toolkit available to researchers and practitioners.

## 6.2. Limitations and future directions

While our study introduces a novel method for analyzing online word-of-mouth dynamics, it is not without limitations. These limitations provide opportunities for future research to further refine and extend the MultiSeqCCoA approach, and they may impact various disciplines differently.

First, our reliance on the LIWC for sentiment analysis presents a potential limitation. While LIWC is a widely used tool in social science research, it has inherent constraints in capturing the full nuance of human communication, particularly in the context of social media. This limitation could particularly affect marketing and management research, where nuanced understanding of consumer sentiment is crucial. For instance, in studies of brand perception or customer satisfaction, the inability to capture subtle emotional cues could lead to incomplete insights. Future research could explore the integration of more advanced natural language processing techniques, such as deep learning-based sentiment analysis or contextual embeddings, to potentially yield more nuanced and accurate representations of online sentiment. This could enhance the method’s ability to capture subtle shifts in word-of-mouth dynamics and provide richer insights into consumer sentiment across various business contexts.

Second, the interpretation of MultiSeqCCoA outputs may pose challenges for non-technical managers or researchers who lack expertise in advanced data analysis. The multidimensional nature of the results, while comprehensive, can be complex to translate into actionable in sights without significant analytical expertise. This limitation could impact the practical application of the method in organizational research and public policy, where decision-makers may struggle to derive actionable strategies from complex analytical outputs. Future work could focus on developing more intuitive visualization techniques or simplified interpretative frameworks that make the outputs more accessible to a broader range of practitioners. Additionally, research into how to effectively communicate these complex analytical results to various stakeholders could greatly enhance the practical utility of the method, particularly in fields like entrepreneurship and public policy where clear communication of insights is crucial.

Lastly, the current implementation of MultiSeqCCoA has specific requirements for the input data structure, namely a list of time-series matrices with identical dimensions. This constraint may limit the method’s applicability in scenarios where data sources have varying dimensions or time periods. In genetics research, for example, this could pose challenges when dealing with datasets of varying sizes or time scales. Future research could explore extensions to the method that accommodate more diverse input structures, such as matrices with different dimensions or varying time periods. This could significantly enhance the versatility of the approach, making it applicable to a wider range of real-world scenarios across disciplines. Furthermore, the method's reliance on a relatively large time window for sufficient in formation may be problematic when dealing with limited time periods, which could impact its use in fast-moving fields like social media analytics or real-time market analysis. Addressing this limitation could involve developing techniques to achieve reliable outputs even with constrained temporal data, potentially through the integration of advanced statistical methods for small sample inference or the incorporation of external data sources to augment limited time series.

## CRediT authorship contribution statement

Xian Cao: Conceptualization, Writing – original draft, Writing – review & editing. Timothy B. Folta: Conceptualization, Resources, Supervision. Hongfei Li: Formal analysis, Validation, Visualization, Writing – original draft, Writing – review & editing. Ruoqing Zhu: Data curation, Formal analysis, Methodology, Supervision, Visualization.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgements

The authors thank the editor and two anonymous reviewers for their constructive comments throughout the review process.

## Appendix A. Supplementary data

The supplementary material to this article can be found online at htt ps://doi.org/10.1016/j.dss.2024.114306.

## References

[11 A. Abadie. Semiparametric difference-in-differences estimators. Rey. Econ. Stud 72 (1) (2005) 1–19.

[2] P.A. Absil, R. Mahony, R. Sepulchre, Optimization Algorithms on Matrix Manifolds Princeton University Press, 2009.

[3] S. Akaho, A Kernel Method for Canonical Correlation Analysis, arXiv Preprint Cs 0609071, 2006.

[4] H. Allcott, L. Boxell, J. Conway, M. Gentzkow, M. Thaler, D. Yang, Polarization and public health: partisan differences in social distancing during the coronavirus pandemic, J. Public Econ. 191 (2020).

[5] D. Altig, S. Baker, J.M. Barrero, et al., Economic uncertainty before and during the COVID-19 pandemic, J. Public Econ. 191 (2020).

[6] G. Andrew, R. Arora, J. Bilmes, K. Livescu, Deep canonical correlation analysis, Proc Int, Conf Machine Learn (2013) 1247-1255

[7] N.F. Awad, A. Ragowsky, Establishing trust in electronic commerce through online word of mouth: an examination across genders, J. Manag. Inf. Syst. 24 (4) (2008) 101–121.

[8] C.A. Bail, L.P. Argyle, T.W. Brown, J.P. Bumpus, H. Chen, M.F. Hunzaker, A. Volfovsky, Exposure to opposing views on social media can increase politica polarization, Proc. Natl. Acad. Sci. 115 (37) (2018) 9216–9221.

[9] P. Barbera,´ J.T. Jost, J. Nagler, J.A. Tucker, R. Bonneau, Tweeting from left to right: is online political communication more than an echo chamber? Psychol. Sci. 26 (10) (2015) 1531–1542.

[10] M.L. Barnett, A.A. King, Good fences make good neighbors: a longitudinal analysis of an industry. Acad. Manag, J. 51 (2008) 1-23.

[11] J.B. Barney, E.J. Zajac, Competitive organizational behavior: toward an

organizationally-based theory of competitive advantage, Strateg. Manag. J. 15 (S1) (1994) 5–9.

[12] D.M. Blei, J.D. Lafferty. Dynamic topic models. in: ACM International Conference Proceeding Series. 2006, pp. 113–120.

[13] A. Borah, G.J. Tellis, Halo (spillover) effects in social media: do product recalls of

[14] J.D. Carroll, Generalization of canonical correlation analysis to three or more sets of variables. in: Proceedings of the 76th annual convention of the Americar Psychological Association. 1968, pp. 227–228.

[15] R.E. Caves, M.E. Porter. From entry barriers to mobility barriers: coniectural decisions and contrived deterrence to new competition. O. J. Econ. 91 (2) (1977) 241.

[16] I. Chae, A.T. Stephen, Y. Bart, D. Yao, Spillover effects in seeded word-of-mouth marketing campaigns, Mark, Sci, 36 (1) (2016) 89–104.

[17] C.C. Chern, C.P. Wei, E.Y. Shen, Y.N. Fan. A sales forecasting model for consumer products based on the influence of online word-of-mouth, IseB 13 (2015) 445–473.

[18] C.M. Cheung, M.K. Lee, What drives consumers to spread electronic word of mouth in online consumer-opinion platforms, Decis. Support, Syst. 53 (1) (2012) 218-225.

[19] E. Chen, K. Lerman, E. Ferrara, Tracking social media discourse about the COVID-19 pandemic: development of a public coronavirus twitter data set, JMIR Public Health Surveill. 6 (2) (2020).

[20] C.M. Cheung, D.R. Thadani, The impact of electronic word-of-mouth communication: a literature analysis and integrative model. Decis. Support, Syst. 54 (1) (2012) 461–470

[21] S. Dewan, Y.J. Ho, J. Ramaprasad, Popularity or proximity: characterizing the nature of social influence in an online music community, Inf. Syst. Res. 28 (1) (2017).117-136

[22] P. Dhillon, D. Foster, L. Ungar, Multi-view learning of word embeddings via CCA, in: Advances in Neural Information Processing Systems (NIPS 2011), 2011, pp. 1–10.

[23] T.K. Dijkstra, J. Henseler, Consistent partial least squares path modeling, MIS Q. 39 (2) (2015) 297–316.

[24] J.A. Dodson Jr., E. Muller, Models of new product diffusion through advertising and word-of-mouth, Manag. Sci. 24 (15) (1978) 1568–1578.

[25] W. Duan, B. Gu, A.B. Whinston, The dynamics of online word-of-mouth and product sales—an empirical investigation of the movie industry, J. Retail. 84 (2) (2008) 233–242.

[26] K. Gelbrich. H. Roschk. A meta-analysis of organizational complaint handling and customer responses, J. Sery. Res, 14 (1) (2011) 24–43.

[27] Y. Gr´egoire, A. Salle, T.M. Tripp, Managing social media crises with you customers: the good, the bad, and the ugly, Bus. Horiz, 58 (2) (2015) 173–18

[28] D.P. Foster, S.M. Kakade, T. Zhang, Multi-View Dimensionality Reduction via Canonical Random Correlation Analysis, 2008.

[29] J. Friedman, T. Hastie, T. Robert, The Elements of Statistical Learning vol. 1, No. 10, Springer, New York, 2001. Series in Statistics.

[30] S. Gelper, R. Peres, J. Eliashberg, Talk bursts: the role of spikes in prerelease wordof-mouth dynamics, J. Mark. Res. 55 (6) (2018) 801–817.

[31] A. Ghose, B. Li, M. Macha, C. Sun, N.Z. Foutz, Trading privacy for the greater social good: How did America react during COVID-19? arXiv preprint arXiv:2006.05859 (2020).

[32] D. Godes, D. Mayzlin, Firm-created word-of-mouth communication: evidence from a field test, Mark. Sci. 28 (4) (2009) 721–739.

[33] M. Hanafi, H.A.L. Kiers, Analysis of K sets of data, with differential emphasis on agreement between and within sets, Comp. Stat. Data Anal. 51 (3) (2006) 1491–1508.

[34] M. Hanafi, A. Kohler, E.M. Qannari, Shedding new light on hierarchical principal component analysis, J. Chemom. 24 (11–12) (2010) 703–709.

[35] H. Hotelling, Relations between two sets of variates, Biometrika 28 (3/4) (1936) 321.

[36] C. Homburg, A. Fürst, How organizational complaint handling drives custome lovalty: an analysis of the mechanistic and the organic approach, J. Mark. 69 (3 (2005) 95–114.

[37] N. Hu, I. Bose, N.S. Koh, L. Liu, Manipulation of online reviews: an analysis of ratings, readability, and sentiments, Decis. Support. Syst. 52 (3) (2012) 674–684.

[38] X. Hu, R. Caldentey, G. Vulcano, Revenue sharing in airline alliances, Manag. Sci. 59 (5) (2013) 1177–1195.

[39] J.R. Kettenring, Biometrika trust canonical analysis of several sets of variables, Biometrika 58 (3) (1971) 433–451.

[40] P.L. Lai, C. Fyfe, Kernel and nonlinear canonical correlation analysis, Int. J. Neural Syst. 10 (05) (2000) 365–377.

[41] D. Lee, K. Hosanagar, H.S. Nair, Advertising content and consumer engagement on social media: Evidence from Facebook, Manag, Sci, 64 (11) (2018) 5105–5131.

[43] V.M.R. Muggeo, Segmented: an R package to fit regression models with broken-line relationships, R News. 8 (1) (2008) 20–25.

[44] V.M.R. Muggeo, Estimating regression models with unknown break-points, Stat. Med, 22 (19) (2003) 3055–3071.

[45] D.C. Mutz, J. Soss, Reading public opinion: the influence of news coverage on perceptions of public sentiment, Public Opin. Q. (1997) 431–451.

[47] J.W. Pennebaker, R.L. Boyd, K. Jordan, K. Blackburn, The Development and Psychometric Properties of LIWC2015. 2015.

[48] J.W. Pennebaker, M.E. Francis, R.J. Booth, Linguistic Inquiry and Word Count LIWC 2007, 2007.

[49] M.A. Peteraf, The cornerstones of competitive advantage: a resource-based view,

[50] J. Pfeffer, T. Zorbach, K.M. Carley, Understanding online firestorms: negative word-of-mouth dynamics in social media networks. J. Mark. Commun. 20 (1-2) (2014) 117–128.

[51] J. Prince, D. Simon, Multimarket contact and service quality: evidence from on time performance in the U.S. airline industry, Acad. Manag. J. 52 (2) (2009) 336–354.

[52] T. Reimer, M. Benkenstein, When good WOM hurts and bad WOM gains: the effect of untrustworthy online reviews, J. Bus. Res. 69 (12) (2016) 5993–6001.

[53] R. Sarathy, K. Muralidhar, The security of confidential numerical data in databases, Inf, Syst. Res, 13 (4) (2002) 389–403

[54] B.W. Silverman. Density Estimation: For Statistics and Data Analysis. 2018

[55] O. Sun. R. Zhu. T. Wang. D. Zeng. Counting process-based dimension reductior methods for censored outcomes. Biometrika 106 (1) (2019) 181–186

[56] A. Susarla, J.H. Oh, Y. Tan, Influentials, imitables, or susceptibles? Virality and word-of-mouth conversations in online social networks, J. Manag. Inf. Syst. 33 (1) (2016) 139–170.

[57] A. Tenenhaus, M. Tenenhaus, Regularized generalized canonical correlation

[58] LR. Tucker, An inter-battery method of factor analysis, Psychometrika 23 (2

[59] LR. Tucker. Determination of parameters of a functional relation by factor analysis. Psychometrika 23 (1) (1958) 19–23

[60] J.W. van Dam, M. Van De Velden, Online profiling and clustering of Facebook

[61] P. Van de Geer, J. Linear relations among K sets of variables, Psychometrika 49 (1) (1984) 79–94.

[62] G.J.J. van den Burg, C.K.I. Williams, An evaluation of change point detection algorithms, arXiv preprint. arXiv:2003.06222, 2020.

[63] X. Wang, L. Kou, V. Sugumaran, X. Luo, H. Zhang, Emotion correlation mining through deep learning models on natural language text, IEEE Trans. Cybernet. 51 (9) (2020) 4400–4413.

[64] Y. Wang, M. Zhang, S. Li, F. McLeay, S. Gupta, Corporate responses to the coronavirus crisis and their impact on electronic-word-of-mouth and trust recovery: evidence from social media, Br. J. Manag. 32 (4) (2021) 1184–1202.

[65] J.A. Westerhuis, T. Kourti, J.F. Macgregor, Analysis of multiblock and hierarchical PCA and PLS models, J. Chemomet, J. Chemomet. Soc. 12 (5) (1998) 301–321

[66] D.M. Witten, R. Tibshirani, T. Hastie, A penalized matrix decomposition, with applications to sparse principal components and canonical correlation analysis, Biostatistics 10 (3) (2009) 515–534.

[67] S.G. Winter, Understanding dynamic capabilities, Strateg. Manag. J. 24 (10) (2003) 991–995.

[68] T. Zhang, G.A. Wang, Z. He, A. Mukherjee, Service failure monitoring via multivariate multiple linear regression profile schemes with dimensionalit reduction, Decis. Support. Syst. 178 (2024) 114–122.

Xian Cao obtained her Ph.D. from the University of Connecticut and now is an Assistant Professor in the Department of Management at Illinois State University. Her current research interests include social media and research methods, female entrepreneurs, and the motivation of entrepreneurship.

Timothy Bernarr Folta (Ph.D. Purdue University) is Professor; Thomas John and Bette Wolff Family Chair of Strategic Entrepreneurship at the University of Connecticut; Faculty Director of the Connecticut Center for Entrepreneurship and Innovation; Past Chair of th Strategic Management Division (6000 members) of the Academy of Management; and Visiting Research Professor at Instituto de Empresa. His research and teaching examine both entrepreneurship and corporate strategy, analyzing decisions around entry, exit, and diversification.

Hongfei Li is an Assistant Professor in the Department of Decisions, Operations and Technology (DOT) at The Chinese University of Hong Kong (CUHK) Business School. Before joining CUHK, he received his Ph.D. from the School of Business at the University of Connecticut and his BS and MS from Renmin University of China in Beijing. His current research focuses on three main streams: (i) business analytics in emerging online plat forms; (ii) applications of artificial intelligence and machine learning; and (iii) statistical methodology.

Ruoqing Zhu obtained his Ph.D. in Biostatistics from the University of North Carolina at Chapel Hill in 2013 and completed his Postdoc training at Yale University in 2015. He is now an Associate Professor of Statistics in the Department of Statistics at the University of Illinois Urbana Champaign. His research focuses on personalized medicine, machin learning, dimension reduction, survival analysis, and their applications to biomedica studies.
