---
otero_id: 27663
otero_key: "T2EMJMJV"
title: "Data Valuation for Vertical Federated Learning: A Model-Free and Privacy-Preserving Method"
authors: "Xiao Han; Leye Wang; Junjie Wu; Xiao Fang"
year: "2026"
journal: "MIS Quarterly"
doi: "10.25300/misq/2025/19161"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DATA VALUATION FOR VERTICAL FEDERATED LEARNING: A MODEL-FREE AND PRIVACY-PRESERVING METHOD<sup>1</sup>

Xiao Han

Key Laboratory of Data Intelligence and Management, Beihang University, Ministry of Industry and Information Technology, and School of Economics and Management, Beihang University, Beijing, CHINA {xh\_bh@buaa.edu.cn}

Leye Wang

Key Lab of High Confidence Software Technologies, Peking University, Ministry of Education, and School of Computer Science, Peking University, Beijing, CHINA {leyewang@pku.edu.cn}

Key Laboratory of Data Intelligence and Management, Beihang University, Ministry of Industry and Information Technology, and School of Economics and Management, Beihang University, Beijing, CHINA {wujj@buaa.edu.cn}

Xiao Fang Lerner College of Business and Economics, University of Delaware, Newark, DE, U.S.A. {xfang@udel.edu}

Vertical federated learning (VFL) is a promising paradigm for predictive analytics, empowering an organization (i.e., task party) to enhance its predictive models through collaborations with multiple data suppliers (i.e., data parties) in a decentralized and privacy-preserving way. Despite the fast-growing interest in VFL, the lack of effective and secure tools for assessing the value of data owned by data parties hinders the application of VFL in business contexts. In response, we propose FedValue, a privacypreserving, task-specific but model-free data valuation method for VFL, which consists of a data valuation metric and a federated computation method. Specifically, we first introduce a novel data valuation metric, namely MShapley-CMI. The metric evaluates a data party’s contribution to a predictive analytics task without the need of executing a machine learning model, making it well-suited for realworld applications of VFL. Next, we develop an innovative federated computation method that calculates the MShapley-CMI value for each data party in a privacy-preserving manner. Extensive experiments conducted on synthetic and realistic datasets validate the efficacy of FedValue for data valuation in the context of VFL. In addition, we illustrate the practical utility of FedValue with case studies involving federated recommendations and financial default prediction.

Keywords: Data valuation, predictive analytics, privacy, vertical federated learning, federated recommendation

## Introduction

Owing to the sheer volume of data accumulated in organizations, predictive analytics has become increasingly vital for businesses across industries (Agarwal & Dhar, 2014; Rai, 2017). It analyzes data with machine learning techniques and makes predictions about future events or unknown facts, which, in turn, effectively supports organizational decisionmaking. As a result, the global market size of predictive analytics had more than doubled from \$4.2 billion in 2017 to \$9.1 billion in 2021,<sup>2</sup> and is expected to continue growing to \$28.1 billion by 2026.<sup>3</sup> Recognizing the value of predictive analytics, information systems (IS) researchers have developed predictive analytics methods to solve a variety of critical business and societal problems, including social network analytics (Fang & Hu, 2018), mobile app recommendations (He et al., 2019), and healthcare analytics (Yu et al., 2024). To maximize the value of predictive analytics, it is important to employ both internal data within an organization and external data outside the organization (Kitchens et al., 2018; Lukyanenko et al., 2019). For example, Lu et al. (2023) conducted a field experiment on a microloan platform and found that combining internal data (e.g., loan amount) on the platform and external data (e.g., loan applicants’ cellphone usage data) off the platform can significantly enhance the accuracy of default predictions, in comparison to using internal data solely. Wang et al. (2021a) developed a predictive analytics method that utilized multisource data collected from within and outside a firm and demonstrated that the method can model financial risks more comprehensively and can remarkably improve the accuracy of financial risk predictions. Although these studies show the great potential for using external data for predictive analytics, they overlook two obstacles that hinder the practical utilization of external data (Kitchens et al., 2018; Liu et al., 2021a). First, owing to significant concerns about data privacy, several data regulations and laws, such as the General Data Protection Regulation<sup>4</sup> in Europe and the Data Security Act<sup>5</sup> in China, have been enacted to prohibit sharing raw data among organizations without proper authorization (Xu & Zhang, 2022). Second, because data is one of the most valuable assets for organizations, data holders may be unwilling to share their data with other organizations without appropriate incentives (e.g., monetary compensation) (Wang et al., 2021b).

Federated learning (FL) is an emerging paradigm towards privacy-preserving collaborative machine learning for predictive analytics (Bi et al., 2023; Yang et al., 2019; Konečnỳ et al., 2016). In general, FL enables its participating organizations to collaboratively train a predictive analytics model without sharing raw data among them. More specifically, each participating organization learns the parameters of a predictive analytics model from its own data locally and only transfers learned parameters to other participating organizations for collaborative model learning, thereby preserving the privacy of raw data. In 2022, the global FL market size reached USD 119.4 million, with the IT & Telecommunications, Finance, and Healthcare industries leading the market. <sup>6</sup> Financial firms, for instance, have explored FL for the use of alternative data for credit scoring (Berg et al., 2020; Zheng & Padmanabhan, 2006). For example, Cignifi, a U.S. start-up, partners with Equifax and Telecom brands like AT&T, Global Telecom and Telefonica to assess credit risk using mobile data.<sup>7</sup> ZestFinance, another U.S. company, works with JD.com and Baidu to generate credit scores for hundreds of millions of prospective borrowers worldwide based on online search and purchase data. <sup>8</sup> Depending on how data are distributed among participating organizations, there are two types of FL: horizontal FL (HFL) and vertical FL (VFL) (Yang et al., 2019). For HFL, local data at different participating organizations have the same features but describe different entities (e.g., customers) (Wang et al., 2020; Wei et al., 2020). Comparatively, for VFL, local data at different participating organizations describe the same set of entities with different features (Wu et al., 2020b; Wang et al., 2019).

Our study focuses on VFL, which is particularly suitable for business applications. Figure 1 illustrates an application of VFL to credit risk prediction. As shown, a financial institution collaborates with a mobile service provider and an online shopping platform to build a credit risk prediction model by analyzing its internal data about credit applicants as well as these applicants’ mobile usage and online shopping data (i.e., external data). In general, if a party (namely, a task party, such as a financial institution) needs to train a predictive analytics model by exploiting additional features about its data samples, it can invite other parties (namely, data parties, such as mobile service providers) who possess these additional features to launch a VFL task.

Although VFL offers a viable solution to overcome the privacy obstacle of integrating internal and external data for predictive analytics, how to select suitable collaborators from many external data suppliers and determine appropriate incentives to encourage high-quality external data suppliers remains underexplored (Kairouz et al., 2021). In response, this study tackles the selection and incentive obstacles by developing a novel data valuation method for VFL. To achieve a successful VFL task, a task party must carefully select the appropriate data parties and offer them proper incentives. Data valuation quantifies the contribution of a data party’s external data to a VFL task. Therefore, an effective data valuation method can help the task party select data parties that contribute most to the VFL task. Moreover, it can assist the task party in determining suitable incentives for the selected data parties and establishing a contribution-based incentive mechanism. This mechanism is crucial for creating a fair and sustainable data marketplace for predictive analytics (Yang et al., 2019).

![](/api/attachments/T2EMJMJV/fulltext/images/ef4435a699d41e847dd861ad5dc0aa0d2be0125ff016a0b64083ff9f866b1555.jpg)  
Note: A financial institution as a task party collaborates with two data parties (an online shopping platform and a mobile service provider) to train a credit risk prediction model using internal data within the financial institution and external data from the data parties.

## Figure 1. An Application of VFL

Designing an effective data valuation method for VFL is nontrivial. First, existing methods are typically either taskindependent or model-dependent, each with its own limitations. Task-independent metrics, such as completeness, precision, uniqueness, and timeliness, evaluate data based on general properties (Wang & Strong, 1996; Batini et al., 2009). However, these methods assign a fixed value to data, ignoring the fact that data contributions can vary across different tasks (Wang & Strong, 1996; Wang et al., 2021b). For example, the value of customer mobile usage data for credit risk prediction may differ from its value for customer retention tasks. To address task-specific needs, some studies propose modeldependent methods based on the Shapley value framework. The exact computation of the Shapley value requires model training with all possible party compositions, leading to a prohibitively high computational cost. Therefore, these studies focus on designing approximation techniques to reduce the need for repeated model training, but this inevitably sacrifices accuracy (Wang et al., 2019; Fan et al., 2024). Moreover, the selection of an appropriate model for valuation poses another challenge: Data parties may be unwilling to invest in complex, resource-heavy training without assurance of returns, whereas simpler models can lead to imprecise value estimates. Thus, efficiently and effectively evaluating a data party’s contribution to a specific task in the VFL context remains a significant challenge.

Second, there might be overlapping or correlated features between the internal data of the task party and the external data from a data party. This phenomenon is known as the “substitution effect,” where these same or correlated features contribute in a comparable manner to a predictive task. Therefore, an effective data valuation method should take the substitution effect between the task and data parties into account and determine appropriate incentives for data parties based on their actual contributions to a VFL task initiated by the task party. Third, a data valuation method must comply with the privacy-preserving requirement. That is, a data valuation method should adhere to data protection regulations and laws, ensuring that no raw data can be leaked from any party involved. However, to assess the contribution of external data, it is essential to have relevant information about the data. For example, we need to know the features of external data to quantify the substitution effect discussed above. As a result, acquiring useful information about external data without violating the privacy-preserving requirement is another challenge for developing an effective data valuation method.

To address these challenges, we propose a privacy-preserving, task-specific but model-free<sup>9</sup> data valuation method for VFL tasks. In particular, premised on cooperative game theory and information theory, we model a VFL task as a master-managed cooperative prediction game and propose a task-specific but model-free data valuation metric that accounts for the substitution effect between the task and data parties. We then develop a federated computation method that assesses the contribution of external data from a data party to a VFL task using the proposed metric. Our data valuation method is privacy preserving in that data are securely stored at their owning data parties. Moreover, it can effectively verify the trustworthiness of results produced by a server in a VFL task, thereby safeguarding against potential malicious attacks by the server intended to manipulate results. We conducted extensive experiments on synthetic and realistic datasets to demonstrate the effectiveness of our method in valuating data for VFL tasks, along with its computational efficiency. We also show the practical value of our method in the context of a federated recommendation task and a federated default prediction task.

## Related Work

Two streams of research are closely related to our study: federated learning (FL) and data valuation. We review each of them and highlight the key novelties of our study.

## Federated Learning

FL enables decentralized collaborative machine learning by utilizing data distributed across multiple parties while ensuring that no party’s data are leaked to any others (Yang et al., 2019). Due to the growing concerns about data privacy, FL has garnered substantial attention from both academia and industry (Yang et al., 2019). An important domain that embraces FL for privacy-preserving predictive analytics is business. In this vein, Tan et al. (2020) deployed a federated recommender system for content recommendations. Liu et al. (2021a) developed an FL framework that enables multiple banks to collaboratively build anti-money laundering models without sharing data among these banks. FL has also been adopted for predictive analytics in the domain of healthcare. For example, Kaissis et al. (2021) developed a framework of federated deep neural networks by exploiting medical image data stored at multiple institutions for privacy-preserving healthcare analytics, such as pediatric chest radiography classification. Warnat-Herresthal et al. (2021) leveraged blood transcriptomes and chest X-ray image data distributed across different medical centers and hospitals to build federated sequential deep neural networks for disease (e.g., COVID-19, tuberculosis, and leukemia) prediction.

The majority of FL studies have designed privacy-preserving and decentralized machine learning algorithms that allow data to be kept locally and only exchange model parameters or intermediate results for collaborative training. FedSGD and FedAvg are two pioneering FL algorithms that have been developed for deep neural networks (McMahan et al., 2017). Specifically, under the framework of FedSGD, each participating party trains its local neural network model using its own data and sends model gradients to a trusted server. The server then aggregates these gradients to create a comprehensive model without accessing the raw data from individual parties, ensuring privacy and confidentiality. Built on FedSGD, FedAvg further improves its computational efficiency and privacy protection. Based on these pioneering algorithms, recent studies have extended FL to other widely used predictive analytics methods, including logistic regression (Hardy et al., 2017; Hu et al., 2019), decision trees (Cheng et al., 2021; Wu et al., 2020b), and matrix factorization (Chai et al., 2020). In addition, some other studies have focused on enhancing FL algorithms by tackling challenges such as non-i.i.d. (non-independent and identically distributed) data among different participating parties and optimizing the communication efficiency among these parties (Sattler et al., 2019; Wu et al., 2020a). Unlike these studies, our paper tackles the data valuation problem, which quantifies the contribution of external data to a predictive analytics task. Data valuation is essential to a successful FL application because it helps the task party select the data parties that contribute the most to the application and facilitates the determination of appropriate incentives offered to them.

To prevent the sharing or leakage of raw data, FL methods typically employ three streams of privacy-preserving methods. The first stream of FL methods transmits intermediate results or parameters of local computations (e.g., model gradients) without encryption. While simple to implement, it risks data leakage, as attackers can infer raw data from transmitted information (Wang et al., 2019; Fan et al., 2024). Differential privacy (DP) methods are sometimes introduced to mitigate this risk but can compromise accuracy (Liu et al., 2024). The second stream employs homomorphic encryption (HE), which encrypts data before transmission and allows computations on encrypted data without decryption (Liu et al., 2024). However, HE often results in significant computational overhead and is limited to FL tasks with simple operations like addition and multiplication. The third stream adopts secure multi-party computation (MPC) techniques, which typically split a task into multiple subtasks and combine their results to produce the outcome without revealing private data (Goldwasser, 1997). MPC is often more efficient and practical for FL, as it can be tailored for specific tasks. However, designing efficient MPC protocols for complex computations is challenging. Considerable research effort has been devoted to designing efficient and secure MPC protocols for various applications, such as addition and multiplication (Goldreich et al., 2019), private set intersection (PSI) (Freedman et al., 2004; Dong et al., 2013), and machine learning (Knott et al., 2021). Among these, PSI is particularly relevant to our work, as our proposed MShapley-CMI can be computed based on several set intersection operations.

One of the earliest PSI protocols was proposed by Meadows (1986), leveraging the Diffie-Hellman (DH) encryption scheme. This approach involves parties exchanging DHencrypted set elements to determine their intersection. The significant computational cost of DH’s exponentiation operations, however, hinders the protocol’s practicality. Later work aimed to improve PSI efficiency, either through optimized DH protocol variations (Huberman et al., 1999; Rosulek & Trieu, 2021) or by adopting alternative cryptographic primitives like oblivious transfer (Freedman et al., 2004; Dong et al., 2013; Kolesnikov et al., 2016; Pinkas et al., 2020). However, most existing PSI protocols are designed for two-party scenarios; extending these to multiple parties typically results in significant computational and transmission overhead, as an ?? -party, PSI generally requires ??(??) instances of two-party PSI. To address this inefficiency in multi-party contexts, server-aided mechanisms have been proposed (Kamara et al., 2014; Abadi et al., 2019). In serveraided PSI, all parties send their encrypted elements to a thirdparty server for intersection computation in a single transmission round, which markedly improves efficiency. Leveraging state-of-the-art encryption schemes, such as AES (Daemen & Rijmen, 1999), server-aided PSI can work for billion-element sets (Kamara et al., 2014). As VFL commonly involves multiple parties, we extend the server-aided PSI method to support MShapley-CMI computation. However, MShapley-CMI computation introduces specific concerns: (1) to prevent the leakage of intersection samples, the server must return only the intersection cardinality, not the intersecting elements, and (2) the protocol needs to defend against a potentially untrustworthy server. To address these issues, we adapted the existing server-aided PSI protocol to achieve efficient and secure MShapley-CMI computation in a federated manner.

## Data Valuation

IS researchers have pioneered data valuation research and proposed numerous data quality metrics from theoretical and operational perspectives (Wang & Strong, 1996; Batini et al., 2009; Wang et al., 2021b). These metrics evaluate the quality of the data based on their intrinsic characteristics, including accuracy, completeness, consistency, and timeliness (Batini et al., 2009). In addition, some studies have considered the contextual nature of data quality and defined systemdependent data quality measurements such as relevancy, accessibility, understandability, traceability, and usage (Wang & Strong, 1996; Wang et al., 2021b). Data quality metrics provide general and high-level evaluations of data value, but they are not tailored for data valuation in the context of predictive analytics.

In response, several data importance metrics have been proposed to assess the contribution of data in a predictive analytics task. Some of these metrics have been developed for particular machine learning models. For example, variable importance (VI) and Gini importance (GI) are data importance measurements developed for predictive analytics with treebased models (Breiman, 2001). In addition, for a predictive analytics task employing a linear model (e.g., logistic regression), the coefficient of a feature indicates its contribution to the task (Fisher et al., 2019). Some other data importance metrics, such as permutation importation (PI) (Fisher et al., 2019), LIME (Ribeiro et al., 2016), and SHAP (Lundberg & Lee, 2017; Jia et al., 2019), can work with different machine learning models, but the evaluation results of these metrics depend on the particular machine learning model used in the evaluation. Specifically, PI assesses the importance of a feature by examining how the performance of a machine learning model varies when different values of the feature are used (Altmann et al., 2010). LIME approximates a complex machine learning model with an interpretable surrogate model (e.g., a linear model) and then uses the surrogate model to evaluate feature importance (Ribeiro et al., 2016). By treating each feature as a game player and the prediction outcome of a predictive analytics task as the payout of the game, SHAP allocates the payout to each feature based on its Shapley value and measures the importance of a feature using its allocated payout. Also built on the Shapley value, Jia et al. (2019) designed an efficient method to measure the contribution of data samples to a predictive analytics task by proposing several approximation techniques to compute Shapley values. Data importance metrics have been developed for centralized predictive analytics tasks, where data are collected and analyzed in a centralized manner. Therefore, they are not suitable for distributed predictive analytics tasks, where data are distributed across various task and data parties, and the privacy of local data at each party must be protected.

To address data valuation challenges in distributed predictive analytics, several studies have developed methods within FL (Yu et al., 2020). These methods typically treat each party as a game player and use the Shapley value to allocate model performance as payouts (Song et al., 2019). The exact computation of the Shapley value requires model training with all possible party compositions, leading to a prohibitively high computational cost of ??(??!) (?? is the number of parties). While some investigations (Ghorbani et al., 2020) have demonstrated that sampling techniques can mitigate this complexity to ??(??) (?? is the number of sampled subsets), the attainment of reliable estimations necessitates a sufficiently large sample size. Nevertheless, training a number of complex machine learning models (e.g., deep neural networks) still poses a considerable computational burden. Therefore, existing studies focus on reducing the computational cost of training models under the Shapley value framework (Wang et al., 2019; Fan et al., 2024; Wang et al., 2020; Wei et al., 2020; Liu et al., 2021b). For VFL, Shapley-SI (Wang et al., 2019) and VerFedSV (Fan et al., 2024) are two leading approaches. Shapley-SI trains a full model with all parties and uses situational importance (SI) to estimate performance changes when parties are removed, avoiding retraining for every coalition. VerFedSV also trains a complete model but leverages intermediate training results to estimate coalition performance. While these methods improve efficiency through approximation, they often significantly compromise accuracy. Moreover, these methods inadequately address the substitution effect between the task and data parties. A task party is unwilling to pay for data it already owns, emphasizing the need to prioritize the task party in value allocation from a business perspective. Current methods based on the Shapley value treat all participants equally and evenly distribute the value of substitutable data, which does not align with practical needs in VFL. Consider a scenario with a task party and two data parties, each owning the same attribute, A, with a contribution of 1 to a predictive task. These methods allocate 1/3 of the value of A to each party. However, since the task party already possesses A, the value of A held by each data party should be 0 to the task party, not 1/3. Therefore, a practical data valuation method should consider the heterogeneity of substitution effects among parties in VFL. A recent study on party selection used mutual information to score parties (Jiang et al., 2022). It computed mutual information for randomly sampled coalitions, distributing the value equally among members. Each party’s value is the average of its allocations across coalitions. However, as it bypasses the Shapley value, this method overlooks fairness among parties.

substitution effects among parties. Table 1 highlights the key differences between our method and existing approaches. Unlike current data valuation methods for VFL, we propose a novel, model-free metric to effectively evaluate parties within the Shapley value framework, eliminating the need for extensive model training. Furthermore, we develop an innovative secure computation method to calculate the proposed metric in a decentralized manner.

## Problem Formulation

We consider a scenario where a task party collaborates with data parties to train a predictive analytics model. In this scenario, the task party seeks to build the model and data parties provide external data with complementary features for model training.

Definition 1 (task party): A task party ?? holds a set of data samples, each of which is identified by its $I D i \in \mathcal I _ { t }$ , where $\mathcal { I } _ { t }$ represents the IDs of all data samples held by the task party. Each data sample ??[??] is characterized by its feature vector $\boldsymbol { x } _ { t [ i ] } \in \mathbb { R } ^ { | F _ { t } | }$ and task label $y _ { t [ i ] } \in \mathbb { R }$ , where $F _ { t }$ denotes the features held by the task party. Accordingly, data held by the task party can be represented as $( X _ { t } , Y _ { t } )$ , where $\pmb { X } _ { t } \in \mathbb { R } ^ { | \mathcal { T } _ { t } | \times | F _ { t } | }$ is the feature matrix, each row of which is $\boldsymbol { x } _ { t [ i ] }$ , and $Y _ { t } \in$ $\mathbb { R } ^ { | \mathcal { I } _ { t } | \times 1 }$ denotes the label vector, each element of which is $y _ { t [ i ] } .$

Recognizing the limitations of existing methods, we introduce a task-specific, model-free, and privacy-preserving data valuation approach that accounts for the heterogeneity of

Definition 2 (data party): A data party ?? possesses a set of data samples, each of which is identified by its $I D i \in \mathcal { I } _ { d } ,$ , where $\mathcal { I } _ { d }$ denotes the IDs of all data samples at the data party. Each data sample ??[??] is described by its feature vector $x _ { d [ i ] } \in$ $\mathbb { R } ^ { | F _ { d } | } ;$ , where $F _ { d }$ represents the features held by the data party. We use feature matrix $\pmb { X } _ { d } \in \mathbb { R } ^ { | \mathcal { I } _ { d } | \times | F _ { d } | }$ to represent data owned by the data party, and each row of the matrix is $x _ { d [ i ] }$

<table><tr><td colspan="5">Table 1. Comparison Between Our Method and Existing Data Valuation Methods</td></tr><tr><td>Method</td><td>Privacy-preserving</td><td>Task-specific</td><td>Model-free</td><td>Substitution effect heterogeneity</td></tr><tr><td>Data quality metrics, e.g., Wang &amp; Strong (1996)</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Data importance metrics, e.g., Ribeiro et al. (2016)</td><td></td><td>√</td><td></td><td></td></tr><tr><td>Data valuation methods for HFL, e.g., Wei et al. (2020)</td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Data valuation methods for VFL, e.g., Wang et al. (2019)</td><td>√</td><td>√</td><td>✕</td><td></td></tr><tr><td>Our method</td><td>√</td><td>√</td><td>√</td><td>√</td></tr></table>

![](/api/attachments/T2EMJMJV/fulltext/images/79c7faccfe02a5f7a1ed7821d3201722c677e834f40c8f6c5f675aac829f7175.jpg)  
Figure 2. An Illustrative Example of Data Held by Task and Data Parties in a VFL Task

Figure 2 illustrates these two definitions. As shown, a task party initiates a vertical FL (VFL) task by inviting selected data parties with suitable incentives. The objective of this task is to train a predictive analytics model by utilizing both internal data held by the task party and external data owned by the selected data parties. A VFL task can be identified by its associated task label ??<sub>??</sub>. For example, the task label of credit risk prediction is whether a customer will default, whereas the task label of customer retention is whether a customer will churn.

This work focuses on assisting the task party in evaluating data parties’ contributions in a VFL task. Our goal is to allocate the total value among the parties effectively, efficiently, and fairly, as in previous VFL data valuation studies (Wang et al., 2019; Fan et al., 2024). To enhance efficiency, we used a model-free metric for evaluation, eliminating the need for extensive model training. We define our data valuation problem for VFL as follows:

Definition 3 (data valuation problem for VFL): Given a VFL task, a task party t and its internal data, a set of data parties ?? ∈ ??, each of which holds its own external data, the objective of the problem is to design a task-specific, model-free, and privacy-preserving method that evaluates the contribution of external data owned by a data party to the VFL task, while taking into account the substitution effect among data held by task and data parties.

Remark: To focus on addressing the data valuation problem, we assume that certain legal prerequisites are satisfied. Specifically, in compliance with privacy regulations (e.g., GDPR and CCPA), it is assumed that the VFL task has obtained consent from all relevant data subjects. This is realistic in scenarios such as loan applicants consenting to a bank and other data providers using their data for credit risk assessment in a VFL task. Also, implementing VFL requires identifying common data samples ℐ among task and data parties in a privacy-preserving manner, where $\mathcal { I } = ( \cap _ { d \in \mathcal { D } } \mathcal { I } _ { d } ) \cap \mathcal { I } _ { t }$ and ?? denotes all data parties. We assume this has been addressed using standard privacy-preserving data alignment methods (Cheng et al., 2021; Liu et al., 2024). Additionally, consistent with prior VFL valuation studies (Wang et al., 2019; Liu et al., 2024; Fan et al., 2024), we assume no collusion among VFL parties and servers.

## Method

In this section, we propose FedValue, a privacy-preserving, task-specific, but model-free method, for data valuation in a VFL task. Concretely, FedValue consists of two components: a data valuation metric and a federated computation method. Premised on cooperative game theory and information theory, we designed a task-specific but model-free data valuation metric that accounts for the substitution effect among data owned by task and data parties. Armed with the data valuation metric, we also developed a federated computation method that assesses the contribution of data owned by a data party to a VFL task in a privacy-preserving manner.

## Data Valuation Metric

In a VFL task, the task party seeks to improve its business model by offering incentives to data parties for a cooperative prediction. Thus, it is natural to model a VFL task as a cooperative game. Along these lines, we began by revisiting the cooperative game and its core solution concept—the Shapley value. We then modeled a VFL task as a master-managed cooperative prediction game and proposed the masterconditioned Shapley value, which considers the substitution effect among data owned by task and data parties. On this basis, we designed an information-theoretic data valuation metric called MShapley-CMI, which is task-specific but model-free. Figure 3 illustrates the metric design process.

![](/api/attachments/T2EMJMJV/fulltext/images/85f3785dc913bd41cd02087ceebd76134c9abc3d14f0d7492a6416389901f249.jpg)  
Figure 3. The Proposed Data Valuation Metric and Its Theoretic Foundations

## Preliminaries: Cooperative Game and Shapley Value

Generally speaking, players participating in a cooperative game form coalitions by making binding agreements so that they can work together to achieve a common goal and receive benefits from the cooperation. A cooperative game is typically modeled as a pair (ℙ, ??), where ℙ denotes the set of players in the game, ?? is the characteristic function, and ??(??) is the real-numbered value generated by coalition $S \subseteq \mathbb { P }$ . The Shapley value, a core solution concept in cooperative game theory, determines how to allocate the value generated by a coalition among its participants (Shapley, 1953). Specifically, the Shapley value of player ?? ∈ ℙ is defined as:

$$
\varphi_ {j} = \sum_ {S \subseteq (\mathbb {P} \setminus \{\mathrm{j} \})} \frac {| S | ! (| \mathbb {P} | - | S | - 1) !}{| P | !} \big (v (S \cup \{\mathrm{j} \}) - v (S) \big)\tag{1}
$$

In this equation, $v ( S \cup \{ \} ) - v ( S )$ computes ?? ’s marginal contribution to the game if the player joins the game right after coalition ??. The first term of the equation, $\vert S \vert ! \left( \vert \mathbb { P } \vert - \vert S \vert - \right.$ $1 ) ! / | P | !$ , gives the probability that player ?? joins the game right after coalition ?? . Thus, Equation (1) calculates the Shapley value of player ?? as the player’s expected marginal contribution to the game.

Being regarded as a fair and justifiable value allocation method, the Shapley value has been widely adopted in various applications, including the task of advertising attribution (Singal et al., 2022), a greenhouse gas emissions game (Gopalakrishnan et al., 2021), and the estimation of feature importance in centralized machine learning (Lundberg & Lee, 2017). The Shapley value has several desirable properties (Shapley, 1953):

 Efficiency: $\begin{array} { r } { \sum _ { j \in \mathbb { P } } \varphi _ { j } = v ( \mathbb { P } ) } \end{array}$

 Symmetry: Consider two players $j , j ^ { \prime } \in \mathbb { P }$ such that for any ?? ⊆ ℙ ∖ {??, ??<sup>′</sup>} , $v ( S \cup \{ j \} ) - v ( S ) = v ( S \cup \{ j ^ { \prime } \} ) - v ( S )$ then $\varphi _ { j } = \varphi _ { j } ,$

 Null-player: If a player ?? ∈ ℙ does not add value to any coalition, i.e., for any $S \subseteq \mathbb { P } \setminus \{ j \} , v ( S \cup \{ j \} ) = v ( S )$ , then $\varphi _ { j } = 0$

## Master-Managed Cooperative Prediction Game for VFL

Prior data valuation methods model a horizontal FL (HFL) task or a vertical FL (VFL) task as a cooperative prediction game denoted by (ℙ, ??) , where ℙ comprises all the parties participating in the task (Wang et al., 2019; Wei et al., 2020; Fan et al., 2024). These methods then adopt the Shapley value defined in Equation (1) to assess the contribution of each party to the task. One limitation of prior data valuation methods is that they treat the task party and each data party indifferently. In reality, the task party initiates a VFL task as a master and recruits data parties with complementary data to improve prediction performance. More severely, prior data valuation methods ignore the substitution effect between internal data owned by the task party and external data held by a data party. Consequently, these methods fail to assess the proper value of a data party to a VFL task. We illustrate this limitation using the following example.

Example 1: Consider a VFL task involving a task party ?? and a data party ??, where the feature matrix $\textstyle { \pmb { X } } _ { d }$ of ?? is identical to the feature matrix $X _ { t } ~ o f ~ t$ . yy applying the Shapley value defined in Equation (1), prior data valuation methods assign the value of ?? as $\begin{array} { r } { \varphi _ { d } = \frac { v ( \{ t , d \} ) } { 2 } = \frac { v ( X _ { d } ) } { 2 } } \end{array}$ . The derivation of $\varphi _ { d }$ is provided in Appendix A. In reality, given ?? already held by task party ?? and $\textstyle { X _ { t } = X _ { d } } ,$ , data party ?? provides no complementary data to the VFL task. As a result, the value of data party ?? should be 0, i.e., $\varphi _ { d } = 0$ . Prior data valuation methods fail to valuate the contribution of data party ?? properly because they overlook the substitution effect between $\pmb { X } _ { t }$ and $\textstyle { \pmb { X } } _ { d }$

To address the limitations of prior data valuation methods, we model a VFL task as a master-managed cooperative prediction game and propose a valuation formula to consider the substitution effects.

Definition 4 (master-managed cooperative prediction game for VFL): A master-managed cooperative prediction game for VFL is defined as a triplet (??, ??, ??) , where ?? represents a master player (i.e., task party), ?? consists of ordinary players $( \mathrm { i . e . , }$ data parties), ?? is the characteristic function of the game, and task and data parties are respectively defined in Definitions 1 and 2. All the players $\mathbb { P } = \{ t \} \cup \mathcal { D }$ work together to accomplish effective predictions on task label $Y _ { t }$ . Characteristic function ??(??) measures the effectiveness of coalition ?? in predicting $Y _ { t } ,$ where ?? is a coalition of task and data parties, i.e., $t \in S \subseteq$ ℙ.

The differentiation of the task party from data parties in the game defined above lays the foundation for our data valuation metric that takes the substitution effect into account. Concretely, the MShapley value (master-conditioned Shapley value) of a party in a master-managed cooperative prediction game for VFL is given by:

$$
\left\{ \begin{array}{l} \varphi_ {t} = v (\{t \}), \\ \varphi_ {d} = \sum_ {D \subseteq (\mathcal {D} \setminus \{d \})} \frac {| D | ! (| \mathcal {D} | - | D | - 1) !}{| \mathcal {D} | !} \big (v (S \cup \{d \}) - v (S) \big), \forall d \in \mathcal {D}, \end{array} \right.\tag{2a}
$$

(2??)

where $\varphi _ { t }$ denotes the MShapley value of task party $t , \varphi _ { d }$ is the MShapley value of data party ?? , and $S = \{ t \} \cup D$ Equation (2) prioritizes task party ?? by fixing it as the first participant in any coalition. As a result, the contribution of ?? to the prediction game does not depend on any other party and $\varphi _ { t } = v ( \{ t \} )$ . Because ?? is the first participant in any coalition, the contribution of data party ?? to the prediction game depends on not only ?? but also other data parties joining the game before $d .$ . Consequently, given that ?? joins the game right after coalition $S = \{ t \} \cup \textit { D } , v ( S \cup \{ d \} ) - v ( S )$ calculates $d \mathrm { \boldsymbol { s } }$ marginal contribution to the game. In other words, data party ?? makes contributions to the prediction game if and only if it provides additional useful data to the prediction, given internal data owned by task party ?? and external data held by other data parties joining the game before ?? . Therefore, Equation (2) considers the substitution effect between internal data owned by the task party and external data held by a data party by fixing ?? as the first participant of coalition. The term $| \dot { D } | ! ( | \mathcal { D } | - \mathbf { \bar { \rho } } | D | - 1 ) ! / | \mathcal { D } | !$ in Equation (2) gives the probability that data party ?? joins the game right after coalition $S = \{ t \} \cup { \cal D }$ . Hence, Equation (2) computes $\varphi _ { d }$ as the expected marginal contribution of data party ?? by averaging over all possible coalition perturbations with ?? always fixed as the first participant.

## MShapley-CMI Metric

Given the MShapley value defined in Equation (2), the remaining task for designing our data valuation metric is to formulate an appropriate characteristic function v that needs to be model-free and task-specific. Recall that coalition ${ \boldsymbol { S } } =$ {??} ∪ ?? consists of the task party ?? , which owns feature matrix $\pmb { X } _ { t }$ and labels of its data samples $Y _ { t } ,$ , and a set of data parties ?? , each of which holds its own feature matrix $\pmb { X } _ { d _ { k ^ { \lambda } } }$ where $d _ { k } \in \mathcal Ḋ D Ḍ$ and $k = 1 , 2 , \dots , | D |$ . Let $\pmb { X } _ { D } = ( \pmb { X } _ { d _ { 1 } } , \cdots$ $, { \pmb X } _ { d _ { k } } \ \cdots , { \pmb X } _ { d _ { | D | } } )$ denote the aggregated feature matrix owned by ?? and $\pmb { X } _ { S } = ( \pmb { X } _ { t } , \pmb { X } _ { D } )$ be the aggregated feature matrix held by ?? . To design a model-free and task-specific data valuation metric, we measure the value of $\pmb { X } _ { S }$ in predicting task label $Y _ { t }$ based on information theory. Our basic idea is to evaluate this value as the reduced uncertainty in predicting $Y _ { t }$ due to $\pmb { X } _ { S }$

We first consider the prediction of task label $Y _ { t }$ based on the prior knowledge about $Y _ { t }$ solely, i.e., the distribution $p ( Y _ { t } )$ derived from labels of data samples $Y _ { t }$ held by the task party. Premised on information theory, the uncertainty of this prediction can be measured by the entropy of $Y _ { t }$ as:

$$
H (Y _ {t}) = - \sum_ {y _ {t} \in \mathcal {Y} _ {t}} p (y _ {t}) \log p (y _ {t}),\tag{3}
$$

where $\mathcal { Y } _ { t }$ represents the set of all possible values of task label $Y _ { t }$ . In this equation, $p ( y _ { t } ) = p ( Y _ { t } = y _ { t } )$ denotes the probability of $y _ { t }$ being observed, which can be learned from $Y _ { t }$ . The uncertainty of predicting $Y _ { t }$ after introducing $\pmb { X } _ { S }$ can then be computed as the conditional entropy of $Y _ { t }$ on $\pmb { X } _ { S }$ which is given by

$$
H (Y _ {t} | \pmb {X} _ {S}) = - \sum_ {\pmb {x} _ {S} \in \mathcal {X} _ {S}} p (\pmb {x} _ {S}) \sum_ {y _ {t} \in \mathcal {Y} _ {t}} p (y _ {t} | \pmb {x} _ {S}) \log p (y _ {t} | \pmb {x} _ {S}),\tag{4}
$$

where $\mathcal { X } _ { S }$ denotes the set of all possible values for the features held by coalition $S , p ( { \pmb x } _ { S } )$ is the probability of feature value $\pmb { x } _ { S }$ being observed in $\pmb { X } _ { S }$ , and $p ( y _ { t } | \pmb { x } _ { S } )$ represents the conditional probability of $y _ { t }$ given $\pmb { x } _ { S }$

Given coalition ?? and its feature matrix $X _ { S }$ , the characteristic function $v ( S )$ in Equation (2b) computes the value of $\pmb { X } _ { S }$ as the reduced uncertainty in predicting $Y _ { t }$ attributed to $X _ { S }$ Accordingly, we have:

$$
v (S) = H (Y _ {t}) - H (Y _ {t} | \pmb {X} _ {S}) = I (\pmb {X} _ {S}; Y _ {t}) = I (\pmb {X} _ {t} \pmb {X} _ {D}; Y _ {t}),\tag{5}
$$

where $I ( \pmb { X } _ { S } ; Y _ { t } )$ is the mutual information between $\pmb { X } _ { S }$ and $Y _ { t }$ (Brown et al., 2012). Consequently, the marginal contribution of data party ?? in Equation (2b) is:

$$
v (S \cup \{d \}) - v (S) = I (\pmb {X} _ {d} \pmb {X} _ {t} \pmb {X} _ {D}; Y _ {t}) - I (\pmb {X} _ {t} \pmb {X} _ {D}; Y _ {t}) = I (\pmb {X} _ {d}; Y _ {t} | \pmb {X} _ {t} \pmb {X} _ {D}),
$$

where $I ( { \pmb X } _ { d } ; Y _ { t } | { \pmb X } _ { t } { \pmb X } _ { D } )$ is the conditional mutual information (i.e., CMI) between $X _ { d }$ and $Y _ { t }$ given $\pmb { X } _ { t } \pmb { X } _ { D }$ (Brown et al., 2012). Substituting the equation above into Equation (2b), we define our information-theoretic data valuation metric, namely MShapley conditional mutual information (i.e., MShapley-CMI), as follows.

Definition 5 (MShapley-CMI): Given a VFL task modeled by a master-managed cooperative prediction game, the MShapley-CMI value of data party ?? , which evaluates the contribution of the data party to the prediction of task label $Y _ { t } ,$ is given by:

$$
\varphi_ {d} = \sum_ {D \subseteq (\mathcal {D} \backslash \{d \})} \frac {| D | ! (| \mathcal {D} | - | D | - 1) !}{| \mathcal {D} | !} I (\boldsymbol {X} _ {d}; Y _ {t} | \boldsymbol {X} _ {t} \boldsymbol {X} _ {D}), \forall d \in \mathcal {D},\tag{6}
$$

The MShapley-CMI metric given in Definition 5 is for evaluating the value of a data party. For the sake of completeness, by considering that the task party is always the first party entering the game, we can define the value of the task party as:

$$
\varphi_ {t} = v (\{\mathfrak {t} \}) = H (Y _ {t}) - H (Y _ {t} | X _ {t}) = I (X _ {t}; Y _ {t}),\tag{7}
$$

where $I ( X _ { t } ; Y _ { t } )$ is the mutual information between $\pmb { X } _ { t }$ and $Y _ { t }$ . Next, we analyze the properties of the proposed MShapley-CMI metric.

Proposition 1: The MShapley-CMI metric has the following properties:

Master-aware efficiency: The sum of the MShapley-CMI values across all data parties is equal to the mutual information between $\pmb { X } _ { \mathcal { D } } \pmb { X } _ { t }$ and $Y _ { t } ,$ , subtracting the MShapley-CMI value of the task party, i.e.,

$$
\sum_ {d \in \mathcal {D}} \varphi_ {d} = I (\pmb {X} _ {\mathcal {D}} \pmb {X} _ {t}; Y _ {t}) - \varphi_ {t}\tag{8}
$$

 Symmetry: If data parties ?? and $d ^ { \prime }$ make the same contributions to the prediction of $\mathrm { \cdot } \mathrm { \cdot } \mathrm { \cdot } \mathrm { \cdot } \mathrm { \cdot } \mathrm { \cdot }$ conditioned on any coalition $S = \{ t \} \cup D$ , then they have the same MShapley-CMI value, i.e.,

$$
\begin{array}{r l} I f & I (\boldsymbol {X} _ {d}; Y _ {t} | \boldsymbol {X} _ {D} \boldsymbol {X} _ {t}) = I (\boldsymbol {X} _ {d ^ {\prime}}; Y _ {t} | \boldsymbol {X} _ {D} \boldsymbol {X} _ {t}), \forall D \subseteq (\mathcal {D} \{d, d ^ {\prime} \}), \\ & t h e n \varphi_ {d} = \varphi_ {d ^ {\prime}} \end{array} \tag {9}
$$

 Null-player: If a data party makes no contribution to the prediction of $Y _ { t }$ , conditioned on any coalition ${ \boldsymbol { S } } =$ {??} ∪ ??, then its MShapley-CMI value equals zero, i.e.,

$$
I f I (\pmb {X} _ {d}; Y _ {t} | \pmb {X} _ {D} \pmb {X} _ {t}) = 0, \forall D \subseteq (\mathcal {D} \{d \}), t h e n \varphi_ {d} = 0\tag{10}
$$

Null-duplication: Let $\pmb { X } _ { d } = ( \pmb { X } _ { d } ^ { 1 } , \pmb { X } _ { d } ^ { 2 } )$ be the feature matrix of data party ?? . Suppose ?? duplicates $\pmb { X } _ { d } ^ { 2 }$ to create a forged feature matrix $\pmb { X } _ { \tilde { d } } = ( \pmb { X } _ { d } ^ { 1 } , \pmb { X } _ { d } ^ { 2 } , \pmb { X } _ { d } ^ { 2 } )$ . Let $\varphi _ { d }$ and $\varphi _ { \tilde { d } }$ denote the MShapley-CMI values calculated using the original feature matrix $X _ { d }$ and the forged matrix $\pmb { X } _ { \tilde { d } } ,$ , respectively. We have

$$
\varphi_ {\tilde {d}} = \varphi_ {d}\tag{11}
$$

The proof is in Appendix B. Proposition 1 shows several desirable properties of the MShapley-CMI metric for data valuation in a VFL task. Specifically, the master-aware efficiency property stipulates that only the contribution of additional features beyond those possessed by the task party will be allocated to data parties, thereby addressing the substitution effect between the task party and data parties. The symmetry property specifies that two data parties receive equal valuation if they make the same contribution to the prediction of $Y _ { t }$ . Thus, two players with identical data will receive the same value, ensuring fairness (Fan et al., 2022). According to the null-player property, MShapley-CMI assigns zero value to a data party that does not offer any useful features for the prediction of $Y _ { t }$ . Finally, the null-duplication property safeguards against the unfair acquisition of added value by a data party through malicious duplication of its features.

In sum, MShapley-CMI is a task-specific and model-free data valuation metric considering substitution effects. It is taskspecific because it evaluates the value of a data party based on the mutual information between the data party’s feature matrix $X _ { d }$ and task label $Y _ { t }$ (Equation 6). The mutual information measure in Equation (6) is independent of any machine learning model. Thus, MShapley-CMI is a model-free metric, unlike previous metrics that rely on the execution of a specific machine learning model for data valuation (Wang et al., 2019; Fan et al., 2024). Finally, MShapley-CMI considers the substitution effect because it evaluates a data party’s marginal contribution to a prediction game, given that the task party always joins the game before the data party. These merits make MShapley-CMI a promising data valuation metric, which is particularly important for fostering legitimate data markets, a trillion-dollar industry in the digital economy era (Chui et al., 2014).

## Federated Computation of MShapley-CMI

We now describe how to compute MShapley-CMI in a federated manner. Our goal is to ensure three levels of privacy and security during data valuation: (1) preventing raw data transmission during valuation, (2) defending against data (features and labels) value inference by servers or parties, and (3) detecting falsified outcomes from malicious servers.

Following the MPC framework, we decompose MShapley-CMI computation into subtasks that preserve data privacy by avoiding raw data transmission and aggregate the results to obtain the final outcome. First, we transform the MShapley-CMI computation into a series of data sample intersection cardinality calculations across all combinations of party data values. Next, we design a private set intersection cardinality (PSIC) protocol to compute these cardinalities securely, preventing data leakage. We then enhance PSIC to a verifiable PSIC (VPSIC) protocol to detect falsified results from malicious servers. Finally, we present a federated MShapley-CMI computation algorithm, integrating PSIC and VPSIC for secure and efficient computation.

## From MShapley-CMI to Intersection Cardinality

According to Definition 5, the challenge of MShapley-CMI computation lies in computing conditional mutual information $I ( \pmb { X } _ { d } ; Y _ { t } | \pmb { X } _ { D } \pmb { X } _ { t } )$ , which involves data distributed in task and data parties. By the definition of conditional mutual information, $I ( { \pmb X } _ { d } ; Y _ { t } | { \pmb X } _ { D } { \pmb X } _ { t } )$ in Equation (6) can be written as:

$$
I (\pmb {X} _ {d}; Y _ {t} | \pmb {X} _ {D} \pmb {X} _ {t}) = \sum_ {\pmb {x} _ {d}, \pmb {x} _ {D}, \pmb {x} _ {t}, y _ {t}} p (\pmb {x} _ {d} \pmb {x} _ {D} \pmb {x} _ {t} y _ {t}) \log \frac {p (\pmb {x} _ {d} y _ {t} | \pmb {x} _ {t} \pmb {x} _ {D})}{p (\pmb {x} _ {d} | \pmb {x} _ {t} \pmb {x} _ {D}) p (y _ {t} | \pmb {x} _ {t} \pmb {x} _ {D})},\tag{12}
$$

where $D \subset \mathcal { D }$ denotes a coalition of data parties, $x _ { d } , x _ { D } ,$ , and $\pmb { x } _ { t }$ respectively represent values of features held by data party $d ,$ coalition of data parties ??, and task party $t , y _ { t }$ is a value of task label $Y _ { t } ,$ and the summation is over all possible values of features held by $d , D _ { \colon }$ , and ??, as well as all possible values of $Y _ { t } .$ . In this equation, $p ( \cdot )$ denotes the probability of observing a combination of values. For example, $p ( { \pmb x } _ { d } { \pmb x } _ { D } { \pmb x } _ { t } y _ { t } )$ is the probability of observing a combination of $\mathbf { \boldsymbol { x } } _ { d } , \mathbf { \boldsymbol { x } } _ { D } , \mathbf { \boldsymbol { x } } _ { t } ,$ and $y _ { t }$

For values of discrete features, ?? , the maximum likelihood estimation of the probability of observing ?? is ${ \hat { p } } ( { \pmb x } ) =$ $N ( { \pmb x } ) / n$ , where $N ( { \pmb x } )$ is the number of data samples containing ?? and ?? is the total number of data samples. Continuous features can be discretized, after which we can proceed with maximum likelihood estimation (Brown et al., 2012). Therefore, the conditional mutual information can be estimated as:

$$
\begin{array}{r l} & {\hat {I} (\pmb {X} _ {d}; Y _ {t} | \pmb {X} _ {t} \pmb {X} _ {D}) = \sum_ {\pmb {x} _ {d}, \pmb {x} _ {D}, \pmb {x} _ {t}, y _ {t}} \hat {p} (\pmb {x} _ {d} \pmb {x} _ {D} \pmb {x} _ {t} y _ {t}) \log \frac {\hat {p} (\pmb {x} _ {d} y _ {t} | \pmb {x} _ {t} \pmb {x} _ {D})}{\hat {p} (\pmb {x} _ {d} | \pmb {x} _ {t} \pmb {x} _ {D}) \hat {p} (y _ {t} | \pmb {x} _ {t} \pmb {x} _ {D})}} \\ & {= \frac {1}{n} \sum_ {\pmb {x} _ {d}, \pmb {x} _ {D}, \pmb {x} _ {t}, y _ {t}} N (\pmb {x} _ {d} \pmb {x} _ {D} \pmb {x} _ {t} y _ {t}) \log \frac {N (\pmb {x} _ {d} \pmb {x} _ {D} \pmb {x} _ {t} y _ {t}) \sum_ {\pmb {x ^ {\prime}} _ {d} \in \mathcal {X} _ {d} , \pmb {y ^ {\prime}} _ {t} \in y _ {t}} N (\pmb {x ^ {\prime}} _ {d} \pmb {x} _ {D} \pmb {x} _ {t} y ^ {\prime} _ {t})}{\sum_ {\pmb {y ^ {\prime}} _ {t} \in y _ {t}} N (\pmb {x} _ {d} \pmb {x} _ {D} \pmb {x} _ {t} y ^ {\prime}) \sum_ {\pmb {x ^ {\prime}} _ {d} \in \mathcal {X} _ {d}} N (\pmb {x ^ {\prime}} _ {d} \pmb {x} _ {D} \pmb {x} _ {t} y _ {t})}} \end{array}\tag{13}
$$

where $N ( \cdot )$ denotes the number of data samples containing given feature values, ?? is the total number of data samples, $\mathcal { Y } _ { t }$ represents the set of all possible values of task label $Y _ { t } ,$ and $\mathcal { X } _ { d }$ denotes the set of all possible values for the features held by data party ??. According to Equation (13), to estimate the conditional mutual information, we need to compute $N ( x _ { d } x _ { D } x _ { t } y _ { t } )$ , and we have

$$
N (\boldsymbol {x} _ {d} \boldsymbol {x} _ {D} \boldsymbol {x} _ {t} y _ {t}) = \left| \bigcap_ {d ^ {\prime} \in D \cup \{d \}} \left\{i | \boldsymbol {x} _ {d ^ {\prime} [ i ]} = \boldsymbol {x} _ {d ^ {\prime}} \right\} \bigcap \left\{j | \langle \boldsymbol {x} _ {t [ j ]}, y _ {t [ j ]} \rangle = \langle \boldsymbol {x} _ {t}, y _ {t} \rangle \right\} \right|,\tag{14}
$$

where $\pmb { x } _ { d ^ { \prime } [ i ] }$ denotes the feature vector of the $i ^ { \mathrm { t h } }$ data sample held by data party $d ^ { \prime } \colon \pmb { x } _ { t [ j ] }$ and $y _ { t [ j ] }$ represent the feature vector and task label value of the $j ^ { \mathrm { t h } }$ data sample owned by task party ?? , respectively. Equation (14) computes $N ( { \pmb x } _ { d } { \pmb x } _ { D } { \pmb x } _ { t } y _ { t } )$ by finding the intersection among data samples owned by data and task parties that satisfy the respective equality condition specified in the equation and then returning the cardinality of the intersection. Therefore, the challenge of computing the MShapley-CMI value becomes how to find the intersection among the data samples, distributed across data and task parties, while preserving the privacy of these data samples.

## Private Set Intersection Cardinality Computation

Among MPC protocols, private set intersection (PSI) is particularly suitable for MShapley-CMI computation, as it computes the intersection of element sets distributed across different parties while allowing each party to keep its data locally (Kamara et al., 2014). Nevertheless, computing the MShapley-CMI value using PSI could violate the privacy of participating parties, which we elaborate next.

Consider a case of computing the number of data samples in the intersection between those held by data party $d ,$ characterized by feature vectors $\pmb { x } _ { d } = \langle 1 , 0 \rangle$ , and those held by task party ?? labeled with $y _ { t } = 1$ . That is, we aim to compute $N ( x _ { d } y _ { t } )$ , a simplified form of Equation (14). To calculate $N ( \pmb { x } _ { d } \ b { y } _ { t } )$ , PSI first requires ?? to encrypt IDs of its data samples, with feature vectors being ⟨1,0⟩, and ?? to encrypt IDs of its data samples, with labels being 1, by using a prior established encryption agreement. Next, a third-party server collects the encrypted IDs from ?? and ??, computes the intersection of the encrypted IDs, and returns the computed intersection to ?? and ??. Finally, using the encryption agreement, ?? and ?? decrypt the encrypted IDs in the intersection. Consequently, party ?? discovers that the labels of data samples with their IDs in the intersection are 1, which is private information owned by task party ?? . Similarly, ?? learns that feature values of data samples with their IDs in the intersection are ⟨1,0⟩; thus, private feature information owned by ?? is disclosed to ??.

One possible fix to the issue discussed above is to let a thirdparty server return the cardinality of the intersection, rather than the intersection, to d and t, called the PSI-cardinality (PSIC) computation. However, directly applying the PSIC method to compute cardinalities for all party feature combinations is inefficient, as sample IDs from one data party often belong to multiple combinations, leading to redundant transmissions. To address this, we propose a “pseudo-category-based PSIC” protocol. With this approach, each party assigns pseudocategories to sample IDs with identical local feature combinations and transmits the encrypted IDs, along with their pseudo-categories, to the server. The server then computes cardinalities for feature category intersections based on the pseudo-categories. This protocol ensures that each local feature combination’s encrypted IDs are transmitted only once, regardless of the total number of features across all parties, significantly reducing redundancy. An illustrative example is shown in Appendix F.

## Verifiable Private Set Intersection Cardinality Computation

While the pseudo-category-based PSIC protocol enhances computational efficiency, it still relies on a trustworthy server to adhere to the protocol. However, the third-party server could be untrustworthy and could falsify results returned to ?? and ??. For instance, if the cardinality of data samples sent by task party ?? to a third-party server is $n _ { t } .$ , the server can easily deceive ?? with any forged intersection cardinality $\hat { n } _ { s }$ that is less than $n _ { t }$ . In practice, a federated machine learning method is required to be sufficiently reliable to discern falsified results from any untrustworthy server (IEEE, 2020). The state-of-theart MPC protocol proposed by Le et al. (2019) can authenticate results provided by a third-party server, determining whether they have been falsified or not. However, this protocol can only work with two parties. The data valuation problem could easily involve more than two parties, e.g., one task party and multiple data parties. Therefore, we need to design a novel protocol that can securely and reliably compute the cardinality of the intersection among data samples distributed across multiple parties.

We thus propose a multi-party verifiable PSIC (VPSIC) protocol, which can verify the veracity of cardinality results returned by a third-party server. Our proposed protocol encrypts IDs of data samples by task and data parties and then sends encrypted IDs to a server to compute the cardinality of the intersection of these IDs. In particular, our protocol has the capability to verify the veracity of the computed cardinality for VFL tasks that involve multiple parties. Such capability is realized through three schemes proposed below.

Definition 6 (ID duplication scheme): The scheme replicates the ID of each data sample owned by a party $q _ { I D }$ times, where $q _ { I D }$ is a random number agreed by all parties. For example, $i f$ $q _ { I D }$ is set to 3, the scheme would generate three IDs, “u011,” “u012,” and “u013,” for a data sample with ID “u01.” The convention for numbering duplicated IDs is also agreed upon by all parties. We note that the value $o f q _ { I D }$ is unknown to thirdparty servers.

Following the scheme, each party (task or data party) duplicates IDs of its data samples $q _ { I D }$ times. It then encrypts these duplicated IDs and sends them to a third-party server to compute cardinality. In principle, a veracious cardinality computed by the server should be divisible by $q _ { I D } .$ , as each data sample is associated with $q _ { I D }$ IDs. Furthermore, since the server is unaware of $q _ { I D }$ , it is difficult for the server to forge a cardinality that can pass the divisibility check.

Definition 7 (redundant computation scheme): Under this scheme, a server is asked to calculate a cardinality multiple times. In each iteration, a party (task or data party) follows the ID duplication scheme to replicate IDs of its data samples $q _ { I D }$ times and then encrypts and sends them to the server for cardinality computation. Since $q _ { I D }$ is a random number generated in each iteration, its value varies from one iteration to another.

As a server is tasked with computing the same cardinality multiple times, the same cardinality result should be received in each iteration. In other words, if inconsistent cardinality results are received across iterations, it implies that the results have been falsified. Note that a server is unaware of $q _ { I D }$ , and the value of $q _ { I D }$ changes from one iteration to another. Consequently, it is hard for an untrustworthy server to pass the consistency check.

There remains a loophole: An untrustworthy server could return zero cardinality in each iteration. Zero cardinality is divisible by $q _ { I D }$ and consistent across iterations, thereby passing both the divisibility and consistency checks. To address this, we enhance our protocol with the following scheme.

Definition 8 (data augmentation scheme): Under this scheme each party produces $n _ { r }$ artificial IDs, where $n _ { r }$ is a random number agreed upon by all parties. The convention for numbering these artificial IDs is also agreed upon by all parties. Each party then encrypts these artificial IDs and sends the encrypted IDs to a server for cardinality computation.

By executing the data augmentation scheme, all parties share a common set of ${ \cdot } n _ { r }$ artificial IDs. Therefore, this set of artificial IDs should be in the intersection, and the cardinality computed by a server should be at least $n _ { r } .$ . In other words, a server’s malicious behavior can easily be detected if its computed cardinality is less than $n _ { r }$

## Federated Computation of MShapley-CM

Built on the proposed pseudo-category-based PSIC and VPSIC protocols, we develop a method to compute the MShapley-CMI value of each data party in a privacy-preserving manner. According to Definition 5 and Equation (13), to calculate the MShapley-CMI value of a data party, we need to compute cardinality $N ( \cdot )$ for each possible combination of $\{ x _ { t } , y _ { t } , \{ x _ { d } | d \in \mathcal { D } \} \}$ . To this end, we developed a secure and verifiable algorithm following the multi-party secure cardinality computation protocol.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: Cardinality Computation and Verification
Input: A task party t, data parties D
Output: Intersection cardinality of every combination of party features;
Each party  $e \in \{t \cup D\}$  labels each sample in J with a pseudo-category in  $P_e$ , generating its data table  $DT_e = \{(id, pc_{id}) | id \in J, pc_{id} \in P_e\}$  (including each ID and the corresponding pseudo-category).
Following the Redundant Computation Scheme (Definition 7), task party t generates a random number  $\tau$  as the number of iterations and synchronizes  $\tau$  with all data parties D;
for  $j \in [1, \tau]$  do
    Task party t generates a random number  $q_{ID}$  as the number of ID duplications;
    Task party t generates artificial IDs  $J^r$  according to the Data Augmentation Scheme (Definition 8);
    Task party t sends  $q_{ID}$  and  $J^r$  to all data parties D;
    for  $e \in \{t \cup D\}$  parallel do
    e applies the ID Duplication Scheme (Definition 6) to replicate each ID for  $q_{ID}$  times: DUP( $J, q_{ID}$ ) →  $J^d$ ;
    for did  $\in J^d$  do
    $pc_{did} = pc_{id}$  where id is the original copy of did;
    end
    Generate the encrypted duplicate data table  $EDT_e^d = \{\langle Enc(did), pc_{did} \rangle | did \in J^d, pc_{did} \in P_e\}$ ;
    for rid  $\in J^r$  do
    $pc_{rid}$  is randomly assigned with a pseudo-category in  $P_e$ ;
    end
    Generate the encrypted artificial data table  $EDT_e^r = \{\langle Enc(rid), pc_{rid} \rangle | rid \in J^r, pc_{rid} \in P_e\}$ ;
    e sends  $EDT_e^r$  to the task party t when e is a data party ( $e \in D$ );
    e sends  $EDT_e^N = EDT_e^d \cup EDT_e^r$  to a third-party server;
    end
    The server computes the cardinality for all combinations of parties' pseudo-categories and sends it to t;
    for each combination of parties' pseudo-categories do
    Suppose the combination is  $\{P_t, P_{d_1}, P_{d_2}, \ldots\}$  where  $\{d_1, d_2, \ldots\}$  are all data parties and  $P_e \in P_e$ ;
    $n_s = cardinality$  of the combination  $\{P_t, P_{d_1}, P_{d_2}, \ldots\}$  returned by the server;
    $n_r = cardinality$  of the combination  $\{P_t, P_{d_1}, P_{d_2}, \ldots\}$  calculated from  $EDT_e^r, e \in \{t \cup D\}$ ;
    Task party t applies non-negativity verification:
    if  $n_s - n_r &lt; 0$  then
    return malicious behavior is detected
    end
    Task party t applies divisibility verification:
    if ( $n_s - n_r$ ) %  $q_{ID}! = 0$  then
    return malicious behavior is detected
    end
    Task party t computes the real cardinality as  $n^* = (n_s - n_r)/q_{ID}$  for the combination  $\{P_t, P_{d_1}, P_{d_2}, \ldots\}$ ;
    Task party t applies consistency verification:
    if j &gt; 1 and the real cardinality for  $\{P_t, P_{d_1}, P_{d_2}, \ldots\}$  in the (j - 1)th iteration is not n* then
    return malicious behavior is detected
    end
    end
End
return n* for every combination of parties' pseudo-categories;
</div>

As illustrated in Algorithm 1 above, each party first assigns a pseudo-category $p c$ to every sample in ℐ . Samples with identical local feature values (plus $y _ { t }$ for the task party) are assigned the same $p c .$ , while those with different feature values are assigned distinct pseudo-categories. Each party then encrypts the sample IDs, encodes them with pseudocategories as an encrypted data table, and sends the table to a third-party server. Then, the server can compute PSI cardinality values for every combination of the parties’ pseudo-categories. In addition, the algorithm employs the ID duplication, redundant computation, and data augmentation schemes to verify the trustworthiness of the computed cardinality values. By invoking Algorithm 1, we can compute cardinality $N ( \cdot )$ for each possible combination of $\{ x _ { t } , y _ { t } , \{ x _ { d } | d \in \mathcal { D } \} \}$ Subsequently, we can estimate conditional mutual information by plugging these computed cardinalities into Equation (13). With estimated conditional mutual information, the MShapley-CMI value of a data party can be computed according to Definition 5.

The proposed method for computing MShapley-CMI has the following security properties:

Preserving the privacy of raw data: As described in Algorithm 1, only encrypted IDs of data samples from task and data parties are sent to a third-party server. The actual data samples remain securely stored with their respective owning parties.

Security against data inference attack: According to Algorithm 1, the task party receives the intersection cardinality values computed by a server rather than the actual sample IDs in the intersection. Consequently, the task party cannot infer any features owned by data parties, thus avoiding the data inference attack elaborated previously.

Security against falsified result attack: Armed with the multi-party secure cardinality computation protocol, Algorithm 1 can effectively verify the trustworthiness of results returned by a server. Proposition 2 gives the upper bound of the probability that a malicious server can successfully deceive the task party during the process of computing an MShapley-CMI value.

Proposition 2: Let $p _ { f }$ be the probability that a malicious server can successfully deceive the task party during the process of computing the MShapley-CMI value of a data party. We thus have:

$$
p _ {f} \leq \min (q _ {I D}) ^ {- \tau \cdot | \mathcal {Y} _ {t} | | \mathcal {X} _ {t} | \cdot \Pi_ {d \in \mathcal {D}} | \mathcal {X} _ {d} |},\tag{15}
$$

where ?? is the number of iterations defined in the redundant computation scheme, ?????? $\left( q _ { I D } \right)$ represents the minimum number of ID duplications across iterations, and $\mathcal { Y } _ { t } , \mathcal { X } _ { t } ,$ , and $\mathcal { X } _ { d } ~ ( \forall d \in \mathcal { D } )$ denote the sets of all possible values $o f Y _ { t } , { \pmb X } _ { t } ,$ and $\scriptstyle { \pmb { X } } _ { d } ,$ respectively.

The proof is in Appendix C. Consider a scenario involving only one data party and one task party. The data party owns two binary features, giving us $| \mathcal { X } _ { d } | = \overset { \cdot } { 2 } { } ^ { 2 } = 4$ . The task party holds a binary task label and a binary feature; thus, we have $| { \mathcal { Y } } _ { t } | =$ $| \mathcal { X } _ { t } | = 2$ . If we set both min(??????) and ?? to be 2, as in Proposition $2 , p _ { f }$ is no larger than $2 ^ { - 2 \cdot 2 \cdot 2 \cdot 4 } = 2 ^ { - 3 2 } \approx 1 0 ^ { - 1 0 }$ . Thus, even under a very simple scenario, the probability that a malicious server will be able to successfully deceive the task party is slim. Real-world scenarios are considerably more complex, involving numerous data parties, each with many more features. Consequently, in the real world, the probability of a malicious server being able to successfully deceive the task party is significantly less than $1 0 ^ { - 1 0 }$ . Proposition 2 demonstrates the strong security of our MShapley-CMI computation method against falsified result attacks by a malicious server. To the best of our knowledge, our study is among the first to design a verifiable federated method for multi-party secure cardinality computation against untrustworthy servers. Although the method was developed for the computation of MShapley-CMI values, it can also be applied to various other tasks involving secure and verifiable multi-party cardinality computation.

Proposition 3: The computation complexity of MShapley-CMI is $O ( \tau ( q _ { I D } | \mathcal { I } | + n _ { r } ) + 2 ^ { | \mathcal { D } | } | \mathcal { X } _ { t } | | \mathcal { Y } _ { t } | \cdot \Pi _ { d \in \mathcal { D } } | \mathcal { X } _ { d } | )$ , which is upper bounded by $O ( ( \tau q _ { I D } + 2 ^ { | \mathcal { D } | } ) | \mathcal { I } | + \tau n _ { r } )$ , where $n _ { r }$ is the number of augmented artificial IDs, $q _ { I D } i s$ the ID duplication times, and ?? is the number of iterations in the redundant computation scheme.

The proof is in Appendix D. This complexity scales linearly with the sample number but exponentially with the party number, as all permutations of data parties must be enumerated in the Shapley process. A method to reduce the exponential complexity is Monte Carlo sampling (Song et al., 2019), which we evaluated in our experiments.

## Experiments

We conducted extensive experiments to evaluate the effectiveness and computational efficiency of FedValue. We first illustrate the experimental setup and then report the results of the effectiveness and efficiency experiments. In general, determining ground truth data contribution values in real-world datasets is challenging due to their unknown intrinsic patterns. Therefore, in this section, we primarily use synthetic datasets with available ground truth contributions for evaluation. In the next section, we evaluate FedValue with realistic datasets by discussing our practical case studies.

## Experimental Setup

We first introduce the datasets and experimental scenarios, followed by a description of the benchmark methods and evaluation metric. Following widely used data simulation strategies in literature (Thrun, 1991; Xu et al., 2017), we created two groups of datasets: LINEAR and MONKLarge.

LINEAR was generated using the logistic regression model, comprising 40 binary features (f<sub>1</sub>- f<sub>40</sub>) and 100,000 samples. To simulate possible substitution effects, f<sub>21</sub>-f<sub>40</sub> are the same as f<sub>1</sub>-f<sub>20</sub>.

MONKLarge was simulated as a larger version of the classic logic rule-based MONK dataset (Thrun, 1991). MONKLarge has 40 binary features and f<sub>21</sub>-f<sub>40</sub> duplicate f<sub>1</sub>-f<sub>20</sub>; the label is set to 1 if exactly 40% of f<sub>1</sub>-f<sub>40</sub> are equal to 1.

We considered three evaluation scenarios for each dataset.

Scenario 0 (S0—no substitution effect): Three data parties hold f<sub>1</sub>-f<sub>5</sub>, f<sub>6</sub>-f<sub>10</sub>, and f<sub>11</sub>-f<sub>20</sub>, respectively. The task party has no features.

Scenario 1 (S1—substitution effects only between the data parties): Four data parties hold f<sub>1</sub>-f<sub>5</sub>, f<sub>6</sub>-f<sub>10</sub>, f<sub>11</sub>-f<sub>20</sub>, and f<sub>21</sub>-f<sub>30</sub>, respectively. The task party has no features.

Scenario 2 (S2—substitution effects between the task and data parties): Data party settings are the same as S1, while the task party holds f<sub>31</sub>-f<sub>40</sub>.

We compared FedValue with model-dependent and modelfree benchmarks discussed in a recent VFL survey (Liu et al., 2024). Model-dependent benchmarks include Shapley-RT (Song et al., 2019), Shapley-SI (Wang et al., 2019), and VerFedSV (Fan et al., 2024). Shapley-RT retrains machine learning models for each Shapley permutation, making it highly time-consuming. Shapley-SI and VerFedSV introduce acceleration techniques to avoid retraining. In particular, Shapley-RT and Shapley-SI can be implemented with any model (Wang et al., 2019); we evaluated them using diverse models of varying architectures and complexities, including logistic regression (LR), deep neural networks (DNN), and XGBoost (XGB). VerFedSV is implemented with LR as per Fan et al. (2024), because it is not easily adaptable to models like XGB. We also considered the model-free method VFPS (Jiang et al., 2022), which was originally designed as a party selection method based on mutual information. VF-PS assigns scores for party rankings, which are used as party values for comparison.

Following the FL valuation literature (Song et al., 2019), we used the Pearson correlation to measure the relationship between benchmark-assessed data party values and ground truths. A correlation close to 1 indicates high accuracy, while a negative correlation suggests a significant discrepancy.

## Effectiveness of FedValue

In this subsection, we mainly evaluate the efficacy of FedValue in gauging the contribution of a data party to a prediction task. We first present the main results (Table 2) across two datasets and three scenarios, followed by additional experiments on robustness to missing/noisy data, fairness, etc.

Main results: Our results demonstrate that FedValue consistently performs well across various datasets and scenarios. Other benchmarks exhibit significant performance drops in scenario S2, where the substitution effects happen between the task and data parties. In some cases, benchmarks even yield negative correlations with ground truth values, i.e., erroneously assigning high contribution values to data parties whose features are already held by the task party. In contrast, FedValue, leveraging the MShapley-CMI metric, can effectively address the substitution effect between task and data parties in S2.

Furthermore, in Scenarios S0 and S1, complex models like DNN often outperform simpler models such as LR for model-dependent benchmarks; however, complex models require significantly more time for training. Notably, FedValue achieves comparable valuation performance to Shapley-RTDNN, while delivering higher computational efficiency.

Additional Results: We evaluated the robustness of FedValue by introducing missing or noisy data into the LINEAR and MONKLarge datasets under various scenarios (Appendix Figure E1). The results indicate that with up to 10% of features missing or noisy, FedValue still maintains a high Pearson correlation (> 0.96) with the ground truth contribution values, demonstrating its practical robustness. We also empirically verified that FedValue can keep the fairness property perfectly, i.e., assigning the exact same contribution values to the parties with the same features (Appendix Tabel E1). In addition, we tested FedValue and benchmarks when there were explicit antagonistic and synergistic feature interactions among data parties; the results also verify that FedValue can consistently keep high Pearson correlations larger than 0.99 (Appendix Table E2).

<table><tr><td colspan="9">Table 2. Pearson Correlation With Ground Truth for Data Valuation Results</td></tr><tr><td rowspan="2"></td><td colspan="3">LINEAR</td><td colspan="3">MONKLarge</td><td rowspan="2">Avg.</td><td rowspan="2">Max. Time</td></tr><tr><td>S0</td><td>S1</td><td>S2</td><td>S0</td><td>S1</td><td>S2</td></tr><tr><td>VF-PS</td><td>0.977</td><td>0.732</td><td>-0.784</td><td>0.968</td><td>0.876</td><td>-0.744</td><td>0.338</td><td>2 sec</td></tr><tr><td>VerFedSV</td><td>0.986</td><td>0.975</td><td>-0.730</td><td>0.956</td><td>0.977</td><td>0.001</td><td>0.528</td><td>39 sec</td></tr><tr><td>Shapley-SI-LR</td><td>0.859</td><td>0.931</td><td>-0.291</td><td>0.920</td><td>0.917</td><td>-0.611</td><td>0.454</td><td>6 sec</td></tr><tr><td>Shapley-SI-XGB</td><td>0.855</td><td>0.857</td><td>0.101</td><td>0.962</td><td>0.816</td><td>0.002</td><td>0.599</td><td>13 sec</td></tr><tr><td>Shapley-SI-DNN</td><td>0.859</td><td>0.937</td><td>-0.307</td><td>0.977</td><td>0.959</td><td>-0.214</td><td>0.535</td><td>29 sec</td></tr><tr><td>Shapley-RT-LR</td><td>1.000</td><td>0.978</td><td>-0.605</td><td>0.865</td><td>0.973</td><td>-0.721</td><td>0.415</td><td>6 sec</td></tr><tr><td>Shapley-RT-XGB</td><td>1.000</td><td>0.976</td><td>-0.613</td><td>1.000</td><td>0.994</td><td>-0.663</td><td>0.449</td><td>16 sec</td></tr><tr><td>Shapley-RT-DNN</td><td>1.000</td><td>0.977</td><td>-0.611</td><td>0.999</td><td>0.997</td><td>-0.642</td><td>0.453</td><td>30 min</td></tr><tr><td>FedValue</td><td>1.000</td><td>0.980</td><td>0.999</td><td>1.000</td><td>0.989</td><td>0.997</td><td>0.994</td><td>6 sec</td></tr></table>

Note: Higher is better; negative values indicate poor performance, such as severely overestimating the value of low-contribution parties.

<table><tr><td colspan="6">Table 3. Default Parameter Setting for Computational Efficiency Evaluation</td></tr><tr><td>Data parties</td><td>Features per party</td><td>Real data samples</td><td>ID duplications</td><td>Redundant tasks</td><td>Artificial IDs</td></tr><tr><td>5</td><td>5</td><td>100,000</td><td>3</td><td>2</td><td>10,000</td></tr></table>

## Computational Efficiency of FedValue

Computational efficiency is critical for the practical implementation of federated methods, as inefficient methods can demand huge computational resources, discourage party participation, and limit privacy protections. Two key classes of parameters influence the efficiency of FedValue. The first class relates to the MShapley-CMI computation, including the number of data parties, features, and data samples. The second involves parameters for verifying the trustworthiness of server results, such as ID duplications, redundant computations, and artificial IDs. We varied these parameters to characterize the efficiencies achieved by FedValue. Table 3 shows the default parameter settings for efficiency experiments. We generated datasets as MONKLarge, while additional features and samples were generated if needed. We varied one parameter at a time while fixing the others at their defaults to assess how each parameter impacted the computation efficiency of FedValue. The experiments were carried out on a workstation with an Intel Core i9 13900KS and 32GB RAM.

Main results: Figure 4 shows the computation time of FedValue concerning the three key parameters related to MShapley-CMI computation. Specifically, Figures 4a and 4b illustrate that the computation time increases linearly with the number of features per party and the number of samples, respectively. Meanwhile, Figure 4c displays an exponential correlation between FedValue’s running time and the number of data parties. Additionally, Figure 5 shows that FedValue exhibits linear scaling regarding the number of ID duplications, redundant computations, and artificial IDs—all three verification parameters.

Addressing exponential complexity in party number: While linear time complexity suggests strong scalability, exponential growth may necessitate acceleration for practical use (Cormen et al., 2022). Experiments showed that FedValue remains efficient with large datasets and features but revealed computational challenges that may arise as the number of data parties increases. This exponential time complexity, common to all Shapley-based methods (Wang et al., 2019; Fan et al., 2024), stems from the ??(??!) permutations for ?? parties. Inspired by prior work on approximating Shapley values (Strumbelj & Kononenko, 2013; Song et al., 2019), we employed Monte Carlo sampling to estimate a data party ??’s value $\hat { \varphi } _ { d }$ by averaging conditional mutual information across sampled permutations.

$$
\hat {\varphi} _ {d} = \frac {1}{| \mathcal {O} |} \sum_ {o \in \mathcal {O}} I (\pmb {X} _ {d}; Y _ {t} | \pmb {X} _ {D _ {o}} \pmb {X} _ {t}),\tag{16}
$$

where ?? is a sampled set of permutations of data parties, ?? is a specific permutation of data parties in ??, and $X _ { D _ { o } }$ is the set of data parties that precede the party ?? in ??.

We tested this strategy using the MONKLarge dataset with 12 data parties. Exhaustively enumerating all permutations would require 12! ≈ 479 million iterations, making it computationally impractical. Figure 6 shows the Pearson correlation between valuation results and ground truth as the number of sampled permutations increases. Notably, after just 1,000 samples (∼0.0002% of total permutations), the correlation exceeds 0.99, with a computation time of only 0.5 hours. This confirms Monte Carlo sampling as an effective method to accelerate FedValue for a large party number.

![](/api/attachments/T2EMJMJV/fulltext/images/22d5868c629c70cd5c86eb0ed78e2bca2b76366e9853a613068f52201b88c000.jpg)  
(a)

![](/api/attachments/T2EMJMJV/fulltext/images/2b6b99977e0e3677e3ac7e61ec50aa7fa33671e161fc6c2b113838ef8c07b2bd.jpg)  
(b)

![](/api/attachments/T2EMJMJV/fulltext/images/928538610575110558f8613442dae847928b10ec4788f0cdc8cee489b2ee7bc5.jpg)  
(c)

Figure 4. Computation Time by MShapley-CMI Parameters  
![](/api/attachments/T2EMJMJV/fulltext/images/cf2470fdea30b1a976bb7b62d8b34f7bfb33e2ac0d2715f0425e9e212e0f48f5.jpg)  
(a)

![](/api/attachments/T2EMJMJV/fulltext/images/0232b2f468b628a98867867279b143c0d217033e8f7f99dd3d3fc8029cc3659d.jpg)  
(b)

![](/api/attachments/T2EMJMJV/fulltext/images/75dfb28a2b13dc9a2616f91d204189b84796e3d04133504f8b792a8a6f2f5fce.jpg)  
(c)

Figure 5. Computation Time by Privacy-Preserving Related Parameters  
![](/api/attachments/T2EMJMJV/fulltext/images/0790fc5f03d8ed5a002c13e77f6896c659422a4bffe912844500df1debf2665e.jpg)  
Figure 6. Pearson Correlation vs. Monte Carlo Sampling Iterations for FedValue (MONKLarge, 12 Data Parties)

## Case Studies of FedValue

We conducted three studies to demonstrate the practical value of FedValue for data party selection in VFL tasks: federated movie recommendation, item recommendation, and financial default prediction. Due to space limitations, the federated item recommendation results are presented in Appendix E.

## Case Study on Federated Movie Recommendation

A movie agency seeks to identify target customers for specific movies from its broader membership base. However, limited access to members’ preference data hampers its ability to accurately identify these customers. At the same time, members movie preference data may be held by other data holders (e.g., YouTube and Netflix); these data holders may be interested in monetizing their data by participating in a federated recommendation task (Yang et al., 2020). Consequently, the agency needs an effective strategy to select data holders that can maximize improvements in federated recommendation performance while adhering to budget constraints. Based on the literature (Shani & Gunawardana, 2011), we define the federated recommendation task as a ranking problem, i.e., generating ranked movie recommendation lists for users.

## Dataset and Party Configuration

We used the MovieLens dataset (Harper & Konstan, 2015), a widely recognized benchmark dataset in federated recommendation research (Li et al., 2021, 2024). Specifically, we leveraged the latest version released in 2024, MovieLens-32M,<sup>10</sup> which contained approximately 32 million ratings for 87,000 movies provided by 200,000 users up to May 2024. The data was partitioned across different parties based on movie genres, following the federated experiment settings in Li et al. (2024).

Task party: The task party sought to develop a highperformance recommendation model that generates ranked lists of movies for users. The user-movie rating data was divided into training and test sets based on temporal order, with the first 70% for training and the latter 30% for testing. Following Li et al. (2021), singular value decomposition (SVD) was applied to the user-item rating matrix to extract features. A user was labeled as positive for a movie recommendation if the rating score was positive (4 or 5) (Zhou et al., 2018). The task party then trained a multi-view federated deep learning model (Li et al., 2021) using local features and the features from other data parties.

Data parties: Data holders who can share historical user-movie ratings were considered candidate data parties. To configure a data party, we assigned a genre of movies and leveraged the corresponding user-movie rating matrix as the party’s data. Each data party also extracted users’ features from the rating matrix by SVD (Li et al., 2021). All data parties and the task party had already aligned an identical set of shared users via privacypreserving entity alignment techniques (Liu et al., 2024).

## Incentive Schemes

We considered two monetary incentive schemes commonly applied in FL tasks.

Fixed incentives (FIX): In this scheme, the task party ?? pays a fixed amount of monetary incentive ?? to every selected data party ??. Despite being simple, FIX is widely used in realistic collaborator recruitment processes, e.g., crowdsourcing platforms like Amazon Mechanical Turk.<sup>11</sup>

Varied incentives (VAR): The VAR scheme allows varying incentives for different data parties. Referring to Zhan et al. (2020), the incentives for data parties are randomly set to ?? or 2??.

We report the results with the FIX scheme in the main text. The results on VAR are in Appendix E.

## Party Selection Strategy and Benchmarks

Following Jiang et al. (2022), we adopted a widely used greedy party selection procedure in FL. In this approach, a data valuation method is first applied to assign each candidate data party a contribution score. Parties are selected in descending order of their scores until the budget is exhausted. For the first step, we employed FedValue, VF-PS (Jiang et al., 2022), VerFedSV (Fan et al., 2024), Shapley-SI (Wang et al., 2019), and Shapley-RT (Song et al., 2019). We also included a common party selection strategy called VOLUME, which prioritizes parties based on data volume.

## Experimental Scenarios and Comparison Metrics

Three experimental scenarios have been developed to address three key questions: (1) Can FedValue help to select suitable data parties for effective federated recommendations, given a certain budget? (2) Can FedValue address the substitution effect appropriately? (3) Can FedValue discern and exclude free-rider parties that lack useful data? First, an ideal scenario is established wherein all data party candidates hold valuable data distinct from that of the task party. Second, to assess FedValue’s ability to handle substitution effects, we developed another scenario involving data overlap either among data parties or between the task and data parties. We set up the third scenario by introducing free-rider parties that attempted to deceive the task party by providing non-valuable data (i.e., fabricated user-movie ratings) (Fraboni et al., 2021; Kairouz et al., 2021). Finally, we executed federated recommendations by employing parties determined by various party selection strategies to compare their efficacy across three scenarios. We repeated each experiment five times by randomly sampling data for party configurations, reporting the average results. Parameter settings are outlined in Table 4.

We assessed the federated recommendation model with ranking-based metrics: nDCG (normalized discounted cumulative gain) and MRR (mean reciprocal rank) (Shani & Gunawardana, 2011). nDCG gives more importance to highly relevant items appearing near the top of the list by discounting the relevance score logarithmically as the rank increases. MRR calculates the reciprocal (1/rank) of the position of the first relevant item for each query and then averages these reciprocals over all queries. Higher nDCG/MRR scores indicate better performance.

## Results

Table 5 reports the performance of federated recommendations without substitution effects. The results indicate that FedValue consistently achieves the highest nDCG and MRR values among all benchmarks. Note that while FedValue may not always achieve statistically significant improvements over Shapley-RT methods, it offers lower computational overhead, especially when compared to complex models like Shapley-RT-DNN.

Table 6 summarizes the federated recommendation performance with substitution effects among parties. <sup>12</sup> Specifically, when substitution effects occur among data parties, FedValue performs slightly better or comparably to Shapley-RT methods with complex models such as DNN, similar to the scenario without substitution effects (Table 5). However, when substitution effects arise between the task and data parties, FedValue significantly outperforms all other benchmarks. These findings are consistent with our earlier experiments, confirming FedValue’s unique advantage in addressing substitution effects between the task and data parties.

Table 7 shows the results when a free rider exists among data parties. Considering all benchmarks, we observe that VF-PS and VerFedSV may fail to differentiate free riders from benign candidates with a free-rider selection probability (FRSP) of greater than zero. FedValue, Shapley-SI, and Shapley-RT all achieved a zero FRSP, demonstrating their effectiveness in identifying and rejecting free riders. Furthermore, FedValue maintained consistently higher nDCG and MRR values compared to other benchmarks, aligning with results from previous scenarios. Appendix E presents results for cold-start users and VAR incentives (Appendix Tables E3 and E4), with FedValue maintaining the best performance.

In summary, the case study verifies that FedValue can significantly enhance federated recommendation systems by effectively selecting appropriate data parties across various practical settings. As reported by Wang et al. (2022), even a 0.1% improvement in recommendation performance would lead to a substantial increase in practical click-through rates for real-world businesses. Therefore, a federated recommendation system integrated with FedValue for party selection could yield significant monetary gains, especially considering annual global film industry revenues (including box office and home entertainment revenue) in excess of \$136 billion (as of 2018).<sup>13</sup>

## Case Study on Financial Default Prediction

We also included a case study on financial default prediction, where a financial institution (task party) holds users’ basic information (e.g., age, occupation), while data parties like digital map services (e.g., Google Maps, Waze) or mobile social services (e.g., Twitter, Foursquare) can provide various types of mobility data. Previous studies have shown that collaborations between financial institutions and mobile data providers can significantly enhance credit scoring quality (Berg et al., 2020).

For the experiment, we leveraged anonymized data collected from a financial institution and its collaborating mobile data providers. To simulate multiple data sources, users’ mobility data was randomly distributed across different parties. For prediction model selection, we evaluated commonly used methods in the literature (Noriega et al., 2023), including LR, DNN, random forest, XGBoost, and SVM. DNN demonstrated superior performance and was chosen as the final prediction model.

<table><tr><td colspan="4">Table 4. Parameter Settings for Federated Movie Recommendation</td></tr><tr><td>variable</td><td>budget</td><td>task party movie genre</td><td>data party movie genres</td></tr><tr><td>value</td><td> $\alpha/2\alpha$ </td><td>Horror</td><td>{Action, Documentary, Romance, Thriller}</td></tr></table>

Table 5. Federated Recommendation Performance Without Substitution Effects

<table><tr><td rowspan="2"></td><td colspan="3">α</td><td colspan="3">2α</td><td rowspan="2">Time</td></tr><tr><td>nDCG@5</td><td>nDCG@10</td><td>MRR</td><td>nDCG@5</td><td>nDCG@10</td><td>MRR</td></tr><tr><td>Volume</td><td>0.0299***</td><td>0.0302***</td><td>0.2899***</td><td>0.0300***</td><td>0.0304***</td><td>0.2940***</td><td>1 sec</td></tr><tr><td>VF-PS</td><td>0.0295**</td><td>0.0297**</td><td>0.2875**</td><td>0.0300**</td><td>0.0305**</td><td>0.2895**</td><td>5 sec</td></tr><tr><td>VerFedSV</td><td>0.0294**</td><td>0.0295**</td><td>0.2879**</td><td>0.0314***</td><td>0.0316***</td><td>0.2992**</td><td>4.5 min</td></tr><tr><td>Shapley-SI-LR</td><td>0.0282***</td><td>0.0281***</td><td>0.2834***</td><td>0.0313*</td><td>0.0315*</td><td>0.2974*</td><td>24 sec</td></tr><tr><td>Shapley-SI-XGB</td><td>0.0300**</td><td>0.0302**</td><td>0.2918**</td><td>0.0309**</td><td>0.0312**</td><td>0.2925**</td><td>37 sec</td></tr><tr><td>Shapley-SI-DNN</td><td>0.0304**</td><td>0.0306**</td><td>0.2895**</td><td>0.0312**</td><td>0.0320**</td><td>0.2938**</td><td>5.1 min</td></tr><tr><td>Shapley-RT-LR</td><td>0.0282***</td><td>0.0281***</td><td>0.2834***</td><td>0.0320</td><td>0.0322</td><td>0.3042</td><td>8.1 min</td></tr><tr><td>Shapley-RT-XGB</td><td>0.0314</td><td>0.0319</td><td>0.2940</td><td>0.0316**</td><td>0.0320*</td><td>0.3053*</td><td>11 min</td></tr><tr><td>Shapley-RT-DNN</td><td>0.0301*</td><td>0.0303*</td><td>0.2950*</td><td>0.0320</td><td>0.0322</td><td>0.3042</td><td>85 min</td></tr><tr><td>FedValue</td><td>0.0321</td><td>0.0324</td><td>0.3092</td><td>0.0330</td><td>0.0333</td><td>0.3102</td><td>1.4 min</td></tr></table>

Note: t-test compares each benchmark with FedValue: ∗ < 0.1, ∗∗ < 0.05, ∗∗∗ < 0.01

<table><tr><td rowspan="2"></td><td colspan="3">Substitution effect between data parties</td><td colspan="3">Substitution effect between task/data parties</td></tr><tr><td>nDCG@5</td><td>nDCG@10</td><td>MRR</td><td>nDCG@5</td><td>nDCG@10</td><td>MRR</td></tr><tr><td>Volume</td><td>0.0299*</td><td>0.0302*</td><td>0.2899*</td><td>0.0299***</td><td>0.0302***</td><td>0.2899***</td></tr><tr><td>VF-PS</td><td>0.0289*</td><td>0.0290*</td><td>0.2846**</td><td>0.0305*</td><td>0.0308*</td><td>0.2962*</td></tr><tr><td>VerFedSV</td><td>0.0297*</td><td>0.0299*</td><td>0.2913*</td><td>0.0277***</td><td>0.0284***</td><td>0.2785***</td></tr><tr><td>Shapley-SI-LR</td><td>0.0295*</td><td>0.0297*</td><td>0.2883*</td><td>0.0249***</td><td>0.0257***</td><td>0.2581***</td></tr><tr><td>Shapley-SI-XGB</td><td>0.0299*</td><td>0.0302*</td><td>0.2899*</td><td>0.0249***</td><td>0.0257***</td><td>0.2581***</td></tr><tr><td>Shapley-SI-DNN</td><td>0.0299*</td><td>0.0302*</td><td>0.2899*</td><td>0.0299***</td><td>0.0302***</td><td>0.2899***</td></tr><tr><td>Shapley-RT-LR</td><td>0.0295*</td><td>0.0297*</td><td>0.2883*</td><td>0.0265***</td><td>0.0271***</td><td>0.2695***</td></tr><tr><td>Shapley-RT-XGB</td><td>0.0305</td><td>0.0307</td><td>0.2947</td><td>0.0249***</td><td>0.0257***</td><td>0.2581***</td></tr><tr><td>Shapley-RT-DNN</td><td>0.0310</td><td>0.0313</td><td>0.2996</td><td>0.0249***</td><td>0.0257***</td><td>0.2581***</td></tr><tr><td>FedValue</td><td>0.0312</td><td>0.0315</td><td>0.3026</td><td>0.0321</td><td>0.0324</td><td>0.3092</td></tr></table>

Note: t-test compares each benchmark with FedValue: ∗ < 0.1, ∗∗ < 0.05, ∗∗∗ < 0.01.

Table 7. Federated Recommendation Performance With One Free Rider

<table><tr><td rowspan="2"></td><td colspan="4">α</td><td colspan="4">2α</td></tr><tr><td>nDCG@5</td><td>nDCG@10</td><td>MRR</td><td>FRSR</td><td>nDCG@5</td><td>nDCG@10</td><td>MRR</td><td>FRSR</td></tr><tr><td>VF-PS</td><td>0.0284**</td><td>0.0286**</td><td>0.2833**</td><td>0.20</td><td>0.0309**</td><td>0.0312*</td><td>0.2936**</td><td>0.20</td></tr><tr><td>VerFedSV</td><td>0.0298*</td><td>0.0302*</td><td>0.2913*</td><td>0.20</td><td>0.0304***</td><td>0.0310**</td><td>0.2870***</td><td>0.20</td></tr><tr><td>Shapley-SI-LR</td><td>0.0296***</td><td>0.0298***</td><td>0.2886***</td><td>0.00</td><td>0.0297*</td><td>0.0301*</td><td>0.2765***</td><td>0.00</td></tr><tr><td>Shapley-SI-XGB</td><td>0.0304**</td><td>0.0306**</td><td>0.2938**</td><td>0.00</td><td>0.0310***</td><td>0.0316**</td><td>0.2884***</td><td>0.00</td></tr><tr><td>Shapley-SI-DNN</td><td>0.0299***</td><td>0.0302***</td><td>0.2899***</td><td>0.00</td><td>0.0312**</td><td>0.0320**</td><td>0.2895**</td><td>0.00</td></tr><tr><td>Shapley-RT-LR</td><td>0.0299***</td><td>0.0302***</td><td>0.2899***</td><td>0.00</td><td>0.0305**</td><td>0.0313**</td><td>0.2862***</td><td>0.00</td></tr><tr><td>Shapley-RT-XGB</td><td>0.0308*</td><td>0.0311*</td><td>0.2976*</td><td>0.00</td><td>0.0312**</td><td>0.0320**</td><td>0.2895**</td><td>0.00</td></tr><tr><td>Shapley-RT-DNN</td><td>0.0302*</td><td>0.0304*</td><td>0.2949*</td><td>0.00</td><td>0.0324</td><td>0.0328</td><td>0.3034</td><td>0.00</td></tr><tr><td>FedValue</td><td>0.0321</td><td>0.0324</td><td>0.3092</td><td>0.00</td><td>0.0330</td><td>0.0333</td><td>0.3102</td><td>0.00</td></tr></table>

Note: FRSP: free rider selection probability—the smaller the better; t-test compares each benchmark with FedValue: ∗ < 0.1, ∗∗ < 0.05, ∗∗∗ < 0.01). This table does not show VOLUME as free riders can always deceive it by generating large volumes of useless data.

<table><tr><td colspan="7">Table 8. AUC of Federated Default Prediction</td></tr><tr><td rowspan="2">budget</td><td colspan="2">No substitution effect</td><td colspan="2">Substitution effect between data parties</td><td colspan="2">Substitution effect task and data parties</td></tr><tr><td>α</td><td>2α</td><td>α</td><td>2α</td><td>α</td><td>2α</td></tr><tr><td>Volume</td><td>0.566***</td><td>0.596***</td><td>0.566***</td><td>0.584***</td><td>0.587***</td><td>0.597***</td></tr><tr><td>VF-PS</td><td>0.563*</td><td>0.598*</td><td>0.563**</td><td>0.594*</td><td>0.597**</td><td>0.605*</td></tr><tr><td>VerFedSV</td><td>0.544***</td><td>0.590***</td><td>0.552**</td><td>0.595*</td><td>0.588***</td><td>0.596**</td></tr><tr><td>Shapley-SI-LR</td><td>0.575</td><td>0.607</td><td>0.572</td><td>0.604</td><td>0.594**</td><td>0.610*</td></tr><tr><td>Shapley-SI-XGB</td><td>0.576</td><td>0.594**</td><td>0.574</td><td>0.603</td><td>0.594**</td><td>0.609**</td></tr><tr><td>Shapley-SI-DNN</td><td>0.576</td><td>0.607</td><td>0.574</td><td>0.604</td><td>0.594**</td><td>0.604**</td></tr><tr><td>Shapley-RT-LR</td><td>0.576</td><td>0.607</td><td>0.572</td><td>0.604</td><td>0.594**</td><td>0.610*</td></tr><tr><td>Shapley-RT-XGB</td><td>0.576</td><td>0.607</td><td>0.574</td><td>0.604</td><td>0.593**</td><td>0.609**</td></tr><tr><td>Shapley-RT-DNN</td><td>0.572*</td><td>0.607</td><td>0.573</td><td>0.603</td><td>0.594**</td><td>0.609**</td></tr><tr><td>FedValue</td><td>0.576</td><td>0.607</td><td>0.574</td><td>0.604</td><td>0.607</td><td>0.616</td></tr></table>

Note: 4 candidate data parties; t-test compares each benchmark with FedValue: ∗ < 0.1, ∗∗ < 0.05, ∗∗∗ < 0.01.

Table 8 presents the results for scenarios where the task party selected one or two data parties. The findings indicate that FedValue and Shapley-based valuation methods (Shapley-SI and Shapley-RT) perform comparably well when there is no substitution effect or substitution effects only exist between data parties. Meanwhile, FedValue significantly outperforms all benchmarks when the substitution effects exist between the task and data parties, demonstrating its practical advantage.

## Conclusion

Federated learning is an emerging privacy-preserving paradigm for collaborative predictive analytics, attracting significant attention from industry and academia. Unlike most studies focused on developing effective learning algorithms, we focus on addressing the pivotal issue of valuating data in the initial stage of VFL tasks from a business perspective. Although this issue holds critical significance for the subsequent party selections and incentive mechanisms design, it remains underinvestigated. We emphasize the difficulty of data valuation in real-life businesses when a task party lacks access to data from other parties, yet needs crucial data value information to select parties before collaboratively training a concrete model with these parties. To tackle this problem, we propose FedValue, a model-free but task-specific data valuation framework for VFL. We demonstrate that FedValue is a useful business decision support tool for a task party to choose appropriate data parties for high-performance VFL.

Our study offers a few theoretical contributions. First, we scrutinize the issue of modeling a VFL task with the conventional cooperative game, which overlooks the substitution effect between candidate data parties and task parties. To address this issue, we propose a master-managed cooperative prediction game (MMCPG) to model a VFL task, considering the master role of a task party in a VFL. MMCPG could establish an effective theoretical foundation for future federated learning studies. Moreover, while the Shapley value allocation framework averages all players’ marginal values across all possible orders in player permutations, it fails to account for the fact that the task party initiates a VFL task and only pays a data party for additional data useful for a predictive task. We extend the Shapley value and propose a valuation framework called MShapley, which is tailored for VFL within MMCPG. MShapley prioritizes the task party in contribution allocation and averages the marginal values of data parties concerning all possible permutations in which they follow the task party. We believe that MMCPG and MShapley can enhance the modeling of broader multi-party cooperative activities. In fact, the MShapley process can be seamlessly integrated into existing Shapley-based data valuation methods, offering improvements particularly when overlapping data exists between the task and data parties. Note that when data parties possess overlapping data, MShapley performs equivalently to the original Shapley value by equally dividing the value of the shared data among its holders. This averaging strategy is standard within existing data valuation methods and is suitable for incentive allocation (Wang et al., 2019); however, it may not always lead to optimal party selection, as party selection is a complex issue related not only to party value but also to other factors such as party pricing or selection mechanisms. Finally, given the crucial role of information/data value within information systems, our work has the potential to enrich the IS literature by analyzing and quantifying the value of data within a privacy-preserving collaborative paradigm for predictive analytics.

Our study also makes some methodological contributions. Primarily, we propose a novel, practical FedValue framework to value data for each party of a VFL task in a privacypreserving manner. In particular, rooted in information theory, we develop MShapley-CMI, a model-free but task-specific metric. We chose CMI over metrics like Pearson or Spearman correlation due to its ability to capture both linear and nonlinear relationships in data and its invariance under invertible transformations (Kullback, 1997). However, we acknowledge that CMI estimation may be challenging in highdimensional contexts, where the curse of dimensionality can hinder the accuracy and reliability of the results (Paninski, 2003). Future work could explore integrating highdimensional mutual information estimation methods with FedValue (Goldfeld & Greenewald, 2021; Gowri et al., 2024). Further, inspired by existing PSI computation protocols, we designed a federated mechanism to compute MShapley-CMI in a privacy-preserving, secure, and verifiable way. This design prevents data leakage and deception during computations, even in the presence of untrustworthy servers or manipulative parties. In Proposition 1, we prove that our method satisfies the null-player and null-duplication properties, ensuring that parties cannot gain credit by submitting useless or redundant data. To address potential result falsification by the malicious server, we incorporated three verification techniques to ensure trustworthiness. Moreover, due to the computationally complex problem of MShapley-CMI, we suggest using Shapley sampling as boosters. FedValue can also adapt to temporal data changes of participants, such as feature additions, updates, or deletions. The server retains encrypted sample IDs, pseudo-feature categories, and the latest intersection cardinality results for each party and coalition. When a party updates its data, it can resend only the modified data, prompting the server to update intersection results for affected coalitions. This ensures that FedValue can efficiently handle dynamic data changes.

We analyzed the practical value of FedValue for real-life businesses. To this end, we conducted case studies of federated recommendations with economic considerations, including budgets, incentive mechanisms, and free riders. The case study showed that a movie agency can use FedValue to identify valuable data parties for building a federated recommendation system. Concretely, FedValue ranks highquality data parties at the top of the list and is capable of excluding free riders, which is particularly important when budgets are tight. Given the report that a 0.1% level of recommendation improvement leads to a substantial rise in the practical click-through rates in real-life businesses (Wang et al., 2022), the monetary gain by FedValue should be significant, given the over \$100 billion in global film market revenues. Our work also sheds light on some general managerial implications for data valuation in VFL tasks. For example, we observed that party selection according to data volume is often ineffective. This highlights the intricate interplay between data value and specific predictive tasks.

The value of our method goes beyond federated recommendation. For example, in the content consumption market where a few super-giants like TouTiao, TikTok, and YouTube occupy the leading positions, a federated recommendation can help companies improve their target marketing abilities in user growth and ad placement by integrating user behavioral data from electronic business companies like JD.com and telecoms like China Mobile. Also, the financial robo-advisor market is still a blue ocean in China, where federated recommendation can help banks identify high-value wealth management customers and assist mutual or private fund companies in promoting new financial products, leveraging auxiliary data from online platforms or telecoms. In such applications, a data valuation mechanism like FedValue will be essential for designing incentives to attract high-quality data providers and optimizing party selection before collaborative model training. We can further expand the application scenario of FedValue to more predictive analytics tasks where vertical federated learning plays an essential role, e.g., systemic risk management across different financial markets and urban intelligent management across different governance sectors, etc. According to Gartner’s hype cycle for privacy,<sup>14</sup> federated learning is still on the rise to the peak and is expected to penetrate privacypreserving predictive analytics in a variety of domains rapidly. Thus, FedValue has the potential to generate considerable business value in the future if practically adopted.

Our study has limitations, and there are research issues that merit future attention and efforts. First, our work does not investigate the important incentive mechanisms issue for a VFL task, although data valuation is the key component in mechanism design. In the near future, we plan to take a step forward to this point based on the FedValue method and study the interactions between data valuation and optimal mechanism design, which in turn can improve FedValue greatly. Second, FedValue currently operates under the assumption of no collusion between the server and participating parties; addressing this limitation represents an intriguing direction for future research. Third, extending the model-free data valuation strategy to horizontal federated learning is another promising research avenue, necessitating the development of a suitable model-free metric to quantify the importance of individual data samples. Fourth, in the case study, we employed a simple greedy strategy for party selection. However, the design of an effective federated learning party selection strategy is an independently significant and challenging research problem that warrants dedicated investigation. Such a strategy would need to account for each party’s contribution, data prices, the task party’s budget constraints, etc. Finally, our work provides simulated case studies for its practical use. It would be much better to have FedValue implemented with the standard of the industry and test it in various real-life VFL applications. The feedback from practices can be used to further improve FedValue.

## Acknowledgments

The authors thank the senior editor, associate editor, and anonymous reviewers for their guidance and constructive comments that have tremendously improved the paper. J. Wu is the corresponding author of the paper. X. Han and J. Wu were supported in part by the National Key R&D Program of China (2023YFC3304700). X. Han is supported in part by the National Natural Science Foundation of China under Grant No. 72071125, 72031001, and 72495151. J. Wu is supported in part by the National Natural Science Foundation of China under Grant No. 72031001, 72242101, 72021001 and the Outstanding Young Scientist Program of Beijing Universities (JWZQ20240201002).

## References

Abadi, A., Terzis, S., Metere, R., & Dong, C. (2019). Efficient delegated private set intersection on outsourced private datasets. IEEE Transactions on Dependable and Secure Computing, 16(4), 608-624. https://doi.org/10.1109/TDSC.2017.2708710

Agarwal, R., & Dhar, V. (2014). Editorial—Big data, data science, and analytics: The opportunity and challenge for IS research. Information Systems Research, 25(3), 443-448. https://pubsonline. informs.org/doi/10.1287/isre.2014.0546

Altmann, A., Toloşi, L., Sander, O., & Lengauer, T. (2010). Permutation importance: A corrected feature importance measure. Bioinformatics, 26(10), 1340-1347. https://doi.org/10.1093/ bioinformatics/btq134

Batini, C., Cappiello, C., Francalanci, C., & Maurino, A. (2009). Methodologies for data quality assessment and improvement. ACM Computing Surveys, 41(3), 1-52. https://doi.org/10.1145 1541880.1541883

Berg, T., Burg, V., Gombović, A., & Puri, M. (2020). On the rise of FinTechs: Credit scoring using digital footprints. The Review of Financial Studies, 33(7), 2845-2897. https://doi.org/10.1093 rfs/hhz099

Bi, X., Gupta, A., & Yang, M. (2023). Understanding partnership formation and repeated contributions in federated learning: An analytical investigation. Management Science, 70(8), 4974-4994. https://doi.org/10.1287/mnsc.2023.00611

Breiman, L. (2001). Random forests. Machine Learning, 45, 5-32. https://doi.org/10.1023/A:1010933404324

Brown, G., Pocock, A., Zhao, M.-J., & Lujan, M. (2012). Conditional likelihood maximisation: A unifying framework for information theoretic feature selection. Journal of Machine Learning Research, 13, 27-66.

Chai, D., Wang, L., Chen, K., & Yang, Q. (2020). Secure federated matrix factorization. IEEE Intelligent Systems, 36(5), 11-20. https://doi.org/10.1109/MIS.2020.3014880

Cheng, G., Qin, Z., Feng, C., Wang, Y., & Li, F. (2011). Conditional mutual information-based feature selection analyzing for synergy and redundancy. Etri Journal, 33(2), 210-218. https://doi.org/ 10.4218/etrij.11.0110.0237

Cheng, K., Fan, T., Jin, Y., Liu, Y., Chen, T., & Yang, Q. (2021). SecureBoost: A lossless federated learning framework. IEEE Intelligent Systems, 36(6), 87-98. https://doi.org/10.1109/MIS. 2021.3082561

Chui, M., Farrell, D., & Jackson, K. (2014). How government can promote open data and help unleash over \$3 trillion in economic value. McKinsey.

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to algorithms. MIT Press.

Daemen, J., & Rijmen, V. (1999). AES proposal: Rijndael. The National Institute of Standards and Technology.

Dong, C., Chen, L., & Wen, Z. (2013). When private set intersection meets big data: An efficient and scalable protocol. In Proceedings of the ACM SIGSAC Conference on Computer & Communications Security (pp. 789-800). https://doi.org/10.1145/2508859.2516701

Fan, Z., Fang, H., Wang, X., Zhou, Z., Pei, J., Friedlander, M., & Zhang, Y. (2024). Fair and efficient contribution valuation for vertical federated learning. In Proceedings of the International Conference on Learning Representations.

Fan, Z., Fang, H., Zhou, Z., Pei, J., Friedlander, M. P., Liu, C., & Zhang, Y. (2022). Improving fairness for data valuation in horizontal federated learning. In Proceedings of the IEEE 38th International Conference on Data Engineering (pp. 2440-2453). https://doi.org/ 10.1109/ICDE53745.2022.00228

Fang, X., & Hu, P. J.-H. (2018). Top persuader prediction for social networks. MIS Quarterly, 42(1), 63-82. https://doi.org/10.25300 MISQ/2018/1321

Fisher, A., Rudin, C., & Dominici, F. (2019). All models are wrong, but many are useful: Learning a variable’s importance by studying an entire class of prediction models simultaneously. Journal of Machine Learning Research, 20(177), 1-81.

Fraboni, Y., Vidal, R., & Lorenzi, M. (2021). Free-rider attacks on model aggregation in federated learning. In Proceedings of the 24th International Conference on Artificial Intelligence and Statistics.

Freedman, M. J., Nissim, K., & Pinkas, B. (2004). Efficient private matching and set intersection. In Proceedings of the International Conference on the Theory and Applications of Cryptographic Techniques. https://doi.org/10.1007/978-3-540-24676-3\_1

Ghorbani, A., Kim, M., & Zou, J. (2020). A distributional framework for data valuation. In Proceedings of the 37th International Conference on Machine Learning.

Goldfeld, Z., & Greenewald, K. (2021). Sliced mutual information: A scalable measure of statistical dependence. In Proceedings of the Conference on Neural Information Processing Systems.

Goldreich, O., Micali, S., & Wigderson, A. (2019). How to play any mental game, or a completeness theorem for protocols with honest majority. In O. Goldreich (Ed.), Providing sound foundations for

cryptography: On the work of Shafi Goldwasser and Silvio Micali (pp. 307-328). ACM Books

Goldwasser, S. (1997). Multi party computations: Past and present. In Proceedings of the 16th Annual ACM Symposium on Principles of distributed computing. https://doi.org/10.1145/259380.259405

Gopalakrishnan, S., Granot, D., Granot, F., Sošić, G., & Cui, H. (2021). Incentives and emission responsibility allocation in supply chains. Management Science, 67(7), 4172-4190. https://doi.org/10.1287/ mnsc.2020.3724

Gowri, G., Lun, X., Klein, A., & Yin, P. (2024). Approximating mutual information of high-dimensional variables using learned representations. In Proceedings of the Conference on Neural Information Processing Systems.

Hardy, S., Henecka, W., Ivey-Law, H., Nock, R., Patrini, G., Smith, G., & Thorne, B. (2017). Private federated learning on vertically partitioned data via entity resolution and additively homomorphic encryption. arXiv. https://doi.org/10.48550/arXiv.1711.10677

Harper, F. M., & Konstan, J. A. (2015). The MovieLens datasets: History and context. ACM Transactions on Interactive Intelligent Systems, 5, Article 19. https://doi.org/10.1145/2827872

He, J., Fang, X., Liu, H., & Li, X. (2019). Mobile app recommendation: An involvement-enhanced approach. MIS Quarterly, 43(3), 827- 850. https://doi.org/10.25300/MISQ/2019/15049

Hu, Y., Niu, D., Yang, J., & Zhou, S. (2019). FDML: A collaborative machine learning framework for distributed features. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (pp. 2232-2240). https://doi.org/10.1145/3292500.3330765

Huberman, B. A., Franklin, M., & Hogg, T. (1999). Enhancing privacy and trust in electronic communities. In Proceedings of the 1st ACM Conference on Electronic Commerce (pp. 78-86). https://doi.org 10.1145/336992.337012

IEEE. (2020). IEEE guide for architectural framework and application of federated machine learning (IEEE Std 3652.1-2020). https://doi.org/10.1109/IEEESTD.2021.9382202

Jia, R., Dao, D., Wang, B., Hubis, F. A., Hynes, N., Gürel, N. M., Li, B., Zhang, C., Song, D., & Spanos, C. J. (2019). Towards efficient data valuation based on the Shapley value. In Proceedings of the 22nd International Conference on Artificial Intelligence and Statistics.

Jiang, J., Burkhalter, L., Fu, F., Ding, B., Du, B., Hithnawi, A., Li, B., & Zhang, C. (2022). VF-PS: How to select important participants in vertical federated learning, efficiently and securely? In Proceedings of the Conference on Neural Information Processing Systems.

Kairouz, P., McMahan, H. B., et al. (2021). Advances and open problems in federated learning. Foundations and Trends in Machine Learning, 14(1-2), 1-210. https://doi.org/10.1561/ 2200000083

Kaissis, G., Ziller, A., Passerat-Palmbach, J., Ryffel, T., Usynin, D., Trask, A., Lima, I., Mancuso, J. V., Jungmann, F., Steinborn, M.- M., Saleh, A., Makowski, M. R., Rueckert, D., & Braren, R. F. (2021). End-to-end privacy preserving deep learning on multiinstitutional medical imaging. Nature Machine Intelligence, 3, 473-484. https://doi.org/10.1038/s42256-021-00337-8

Kamara, S., Mohassel, P., Raykova, M., & Sadeghian, S. S. (2014). Scaling private set intersection to billion-element sets. In Proceedings of the 18th International Conference on Financial Cryptography and Data Security (pp. 195-215). https://doi.org/ 10.1007/978-3-662-45472-5\_13

Kitchens, B., Dobolyi, D. G., Li, J., & Abbasi, A. (2018). Advanced customer analytics: Strategic value through integration of relationship-oriented big data. Journal of Management Information Systems, 35(2), 540-574. https://doi.org/10.1080 07421222.2018.1451957

Knott, B., Venkataraman, S., Hannun, A., Sengupta, S., Ibrahim, M., & van der Maaten, L. (2021). Crypten: Secure multi-party computation meets machine learning. In Proceedings of the Conference on Neural Information Processing Systems.

Kolesnikov, V., Kumaresan, R., Rosulek, M., & Trieu, N. (2016). Efficient batched oblivious PRF with applications to private set intersection. In Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security (pp. 818-829). https://doi.org/10.1145/2976749.2978381

Konečnỳ, J., McMahan, H. B., Yu, F. X., Richtárik, P., Suresh, A. T., & Bacon, D. (2016). Federated learning: Strategies for improving communication efficiency. arXiv. https://doi.org/10.48550/arXiv. 1610.05492

Kullback, S. (1997). Information theory and statistics. Courier Corporation.

Le, P. H., Ranellucci, S., & Gordon, S. (2019). Two-party private set intersection with an untrusted third party. In Proceedings of the ACM SIGSAC Conference on Computer and Communications Security (pp. 2403-2420). https://doi.org/10.1145/3319535.3345661

Li, H., Huang, M., Bai, B., Wang, C., Bai, K., Wang, F., Zhu, X., Zhao, B., Liu, G., & Qi, C. (2021). A federated multi-view deep learning framework for privacy-preserving recommendations. In Proceedings of the International Workshop on Federated and Transfer Learning for Data Sparsity and Confidentiality in Conjunction with IJCAI.

Li, W., Wang, Z., Wang, J., Xia, S.-T., Zhu, J., Chen, M., Fan, J., Cheng, J., & Lei, J. (2024). Refer: Retrieval-enhanced vertical federated recommendation for full set user benefit. In Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval (pp. 1763-1773). https://doi.org/10.1145/3626772.3657763

Liu, Y., Fan, T., Chen, T., Xu, Q., & Yang, Q. (2021a). FATE: An industrial grade platform for collaborative learning with data protection. Journal of Machine Learning Research, 22(1), Article 226.

Liu, Y., Kang, Y., Zou, T., Pu, Y., He, Y., Ye, X., Ouyang, Y., Zhang, Y.-Q., & Yang, Q. (2024). Vertical federated learning: Concepts, advances, and challenges. IEEE Transactions on Knowledge and Data Engineering, 36(7), 3615-3634. https://doi.org/10.1109/ TKDE.2024.3352628

Liu, Z., Chen, Y., Yu, H., Liu, Y., & Cui, L. (2021b). GTG-Shapley: Efficient and accurate participant contribution evaluation in federated learning. ACM Transactions on Intelligent Systems and Technology, 13, 1-21. https://doi.org/10.1145/3501811

Lu, T., Zhang, Y., & Li, B. (2023). Profit vs. equality? The case of financial risk assessment and a new perspective of alternative data. MIS Quarterly, 47(4), 1517-1556. https://doi.org/10.25300/MISQ/ 2023/17330

Lukyanenko, R., Parsons, J., Wiersma, Y. F., & Maddah, M. (2019). Expecting the unexpected: Effects of data collection design choices on the quality of crowdsourced user-generated content. MIS Quarterly, 43(2), 623-648. https://doi.org/10.25300/MISQ/2019/ 14439

Lundberg, S. M., & Lee, S.-i. (2017). A unified approach to interpreting model predictions. In Proceedings of the Conference on Neural Information Processing Systems.

McMahan, B., Moore, E., Ramage, D., Hampson, S., & Agüera y Arcas, B. (2017). Communication-efficient learning of deep networks from decentralized data. In Proceedings of the 20th International Conference on Artificial Intelligence and Statistics.

Meadows, C. (1986). A more efficient cryptographic matchmaking protocol for use in the absence of a continuously available third party. In Proceedings of the IEEE Symposium on Security and Privacy. https://doi.org/10.1109/SP.1986.10022

Noriega, J. P., Rivera, L. A., & Herrera, J. A. (2023). Machine learning for credit risk prediction: A systematic literature review. Data, 8(11), 169. https://doi.org/10.3390/data8110169

Paninski, L. (2003). Estimation of entropy and mutual information. Neural Computation, 15(6), 1191-1253. https://doi.org/10.1162/ 089976603321780272

Pinkas, B., Rosulek, M., Trieu, N., & Yanai, A. (2020). PSI from PaXoS: Fast, malicious private set intersection. In Proceedings of the Annual International Conference on the Theory and Applications of Cryptographic Techniques. https://doi.org 10.1007/978-3-030-45724-2\_25

Rai, A. (2017). Editor’s comments: Diversity of design science research. MIS Quarterly, 41(1), iii-xviii.

Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). “Why should I trust you?” Explaining the predictions of any classifier. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 1135-1144). https://doi.org/10.1145/2939672.2939778

Rosulek, M., & Trieu, N. (2021). Compact and malicious private set intersection for small sets. In Proceedings of the ACM SIGSAC Conference on Computer and Communications Security (pp. 1166- 1181). https://doi.org/10.1145/3460120.3484778

Sattler, F., Wiedemann, S., Müller, K.-R., & Samek, W. (2019). Robust and communication-efficient federated learning from non-i.i.d. data. IEEE Transactions on Neural Networks and Learning Systems, 31(9), 3400-3413. https://doi.org/10.1109/TNNLS.2019.2944481

Shani, G., & Gunawardana, A. (2011). Evaluating recommendation systems. In F. Ricci, L. Rokach, B. Shapira, & P. B. Kantor (Eds.), Recommender systems handbook (pp. 257-297). Springer.

Shapley, L. S. (1953). A value for n-person games. Contributions to the Theory of Games, 2(28), 307-317.

Singal, R., Besbes, O., Desir, A., Goyal, V., & Iyengar, G. (2022). Shapley meets uniform: An axiomatic framework for attribution in online advertising. Management Science, 68(10), 7457-7479. https://doi.org/10.1287/mnsc.2021.4263

Song, T., Tong, Y., & Wei, S. (2019). Profit allocation for federated learning. In Proceedings of the IEEE International Conference on Big Data. https://doi.org/10.1109/BigData47090.2019.9006327

Strumbelj, E., & Kononenko, I. (2013). Explaining prediction models and individual predictions with feature contributions. Knowledge and Information Systems, 41, 647-665. https://doi.org/10.1007/ s10115-013-0679-x

Tan, B., Liu, B., Zheng, V., & Yang, Q. (2020). A federated recommender system for online services. In Proceedings of the 14th ACM Conference on Recommender Systems (pp. 579-581). https://doi.org/10.1145/3383313.3411528

Thrun, S. (1991). The MONK’s problems: A performance comparison of different learning algorithms (Technical report). Carnegie Mellon University.

Wang, G., Chen, G., Zhao, H., Zhang, F., Yang, S., & Lu, T. (2021a). Leveraging multi-source heterogeneous data for financial risk prediction: A novel hybrid-strategy-based self-adaptive method. MIS Quarterly, 45(4), 1949-1998. https://doi.org/10.25300/MISQ/ 2021/16118

Wang, G., Dang, C. X., & Zhou, Z. (2019). Measure contribution of participants in federated learning. In Proceedings of the IEEE International Conference on Big Data. https://doi.org/10.1109 BigData47090.2019.9006179

Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. Journal of Management Information Systems, 12(4), 5-33. https://doi.org/10.1080 07421222.1996.11518099

Wang, T., Rausch, J., Zhang, C., Jia, R., & Song, D. (2020). A principled approach to data valuation for federated learning. In Q. Yang, L. Fan, & H. Yu (Eds.), Federated learning: Privacy and incentive (pp. 153-167). Springer. https://doi.org/10.1007/978-3- 030-63076-8\_11

Wang, Z., Kuang, W., Xie, Y., Yao, L., Li, Y., Ding, B., & Zhou, J. (2022). FederatedScope-GNN: Towards a unified, comprehensive and efficient package for federated graph learning. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (pp. 4110-4120). https://doi.org/10.1145/ 3534678.3539112

Wang, Z., Zheng, Z. E., Jiang, W., & Tang, S. (2021b). Blockchainenabled data sharing in supply chains: Model, operationalization, and tutorial. Production and Operations Management, 30, 1965- 1985. https://doi.org/10.1111/poms.13356

Warnat-Herresthal, S., Schultze, H., Shastry, K. L., Manamohan, S., Mukherjee, S., Garg, V., Sarveswara, R., Händler, K., Pickkers, P., Aziz, N. A., ... Schultze, J. L. (2021). Swarm learning for decentralized and confidential clinical machine learning. Nature, 594(7862), 265-270. https://doi.org/10.1038/s41586-021-03583-3

Wei, S., Tong, Y., Zhou, Z., & Song, T. (2020). Efficient and fair data valuation for horizontal federated learning. In Federated Learning (pp. 139-152). https://doi.org/10.1007/978-3-030-63076-8\_10

Wu, X., Yao, X., & Wang, C.-L. (2020a). FedSCR: Structure-based communication reduction for federated learning. IEEE Transactions on Parallel and Distributed Systems, 32(7), 1565- 1577. https://doi.org/10.1109/TPDS.2020.3046250

Wu, Y., Cai, S., Xiao, X., Chen, G., & Ooi, B. C. (2020b). Privacy preserving vertical federated learning for tree-based models. Proceedings of the VLDB Endowment, 13(12), 2090-2103. https://doi.org/10.14778/3407790.3407811

Xu, E. L., Qian, X., Yu, Q., Zhang, H., & Cui, S. (2017). Feature selection with interactions in logistic regression models using multivariate synergies for a GWAS application. In Proceedings of the 8th ACM International Conference on Bioinformatics, Computational Biology, and Health Informatics (pp. 760-761). https://doi.org/10.1145/3107411.3110406

Xu, H., & Zhang, N. (2022). From contextualizing to context theorizing: Assessing context effects in privacy research. Management Science, 68(10), 7383-7401. https://doi.org/10.1287/mnsc.2021.4249

Yang, L., Tan, B., Zheng, V. W., Chen, K., & Yang, Q. (2020). Federated recommendation systems. In Q. Yang, L. Fan, & H. Yu (Eds.) Federated learning: Privacy and incentive (pp. 225-239). https://doi.org/10.1007/978-3-030-63076-8\_16

Yang, Q., Liu, Y., Chen, T., & Tong, Y. (2019). Federated machine learning: Concept and applications. ACM Transactions on

Intelligent Systems and Technology, 10(2), Article 12. https://doi.org/10.1145/3298981

Yu, H., Liu, Z., Liu, Y., Chen, T., Cong, M., Weng, X., Niyato, D., & Yang, Q. (2020). A fairness-aware incentive scheme for federated learning. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (pp. 393-399). https://doi.org/10.1145/ 3375627.3375840

Yu, S., Chai, Y., Samtani, S., Liu, H., & Chen, H. (2024). Motion sensor-based fall prevention for senior care: A hidden Markov model with generative adversarial network approach. Information Systems Research, 35(1), 1-15. https://doi.org/10.1287/isre. 2023.1203

Zhan, Y., Li, P., Wang, K., Guo, S., & Xia, Y. (2020). Big data analytics by crowdlearning: Architecture and mechanism design. IEEE Network, 34(3), 143-147. https://doi.org/10.1109/MNET. 001.1900286

Zheng, Z., & Padmanabhan, B. (2006). Selectively acquiring customer information: A new data acquisition problem and an active learning-based solution. Management Science, 52(5), 697-712. https://doi.org/10.1287/mnsc.1050.0488

Zhou, G., Zhu, X., Song, C., Fan, Y., Zhu, H., Ma, X., Yan, Y., Jin, J., Li, H., & Gai, K. (2018). Deep interest network for click-through rate prediction. In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (pp. 1059- 1068). https://doi.org/10.1145/3219819.3219823

## About the Authors

Xiao Han is a full professor at the School of Economics and Management, Beihang University. She received a Ph.D. in informatics from the Pierre and Marie Curie University and Institut Mines-TELECOM/TELECOM SudParis in 2015. Her research focuses on data-driven intelligent systems in business and societal contexts, with particular focuses on data security and privacy. Her work has been published in leading journals and top-tier conference proceedings in information systems and computer science, including MIS Quarterly, INFORMS Journal on Computing, IEEE Transactions on Dependable and Secure Computing, IEEE Transactions on Information Forensics and Security, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Software Engineering, The Web Conference, AAAI Conference on Artificial Intelligence, etc.

Leye Wang is a tenured associate professor at Key Lab of High Confidence Software Technologies (Peking University), Ministry of Education, China, and School of Computer Science, Peking University. His research interests include ubiquitous computing and data privacy protection. Wang received a Ph.D. in computer science from the Pierre and Marie Curie University and Institut Mines-TELECOM/TELECOM SudParis, France, in 2016. His research has appeared in journals and conference proceedings such as MIS Quarterly, INFORMS Journal on Computing, IEEE Transactions on Dependable and Secure Computing, IEEE Transactions on Information Forensics and Security, IEEE Transactions on Knowledge and Data Engineering, Artificial Intelligence, The Web Conference, AAAI Conference on Artificial Intelligence, etc.

Junjie Wu is currently a full professor at the School of Economics and Management, Beihang University. He is also the director of the MIIT Key Laboratory of Data Intelligence and Management. He holds a B.E. degree from the School of Civil Engineering and a Ph.D. degree from the School of Economics and Management, Tsinghua University. His research interests include data and decision intelligence, with intense applications to business, finance, cities and industries. He has published prolifically in journals and conference proceedings including MIS Quarterly, Information Systems Research, INFORMS Journal on Computing, IEEE Transactions on Knowledge and Data Engineering, ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Advances in Neural Information Processing Systems, AAAI Conference on Artificial Intelligence, etc.

Xiao Fang is a professor of management information systems and the JPMorgan Chase Senior Fellow at the Lerner College of Business & Economics and the Institute for Financial Services Analytics, University of Delaware. His current research focuses on GenAI, financial technology, and healthcare analytics, with methods and tools drawn from reference disciplines including management science (e.g., optimization) and computer science (e.g., machine learning). He has published in information systems journals, including MIS Quarterly, Information Systems Research, Management Science, and Operations Research, as well as computer science outlets, such as ACM Transactions on Information Systems and IEEE Transactions on Knowledge and Data Engineering.

## Appendix A

## Derivation of $\varphi _ { d }$ in Example 1

Let’s utilize the Shapley value defined in Equation (1) to evaluate a data party d in a cooperative game. We first enumerate the potential coalition S formed before d’s join. In Example 1, there are only two parties (i.e., the data party d and the task party t); then, d would be either the first party $( \mathrm { i . e . , } S = \emptyset )$ or the second party after t $( \mathrm { i } . \mathbf { e } . , S = \{ t \} )$ joining the game. According to the definition of the Shapley value, we compute the value of data party d by its expected marginal contribution to the game as:

$$
\varphi_ {d} = \sum_ {S \subseteq (\mathbb {P} \backslash \{d \})} \frac {| S | ! (| \mathbb {P} | - | S | - 1) !}{| \mathbb {P} | !} \big (v (S \cup \{d \}) - v (S) \big),\tag{17}
$$

$$
= \frac {0 ! (2 - 0 - 1) !}{2 !} \big (v (\{d \}) - v (\phi) \big) + \frac {1 ! (2 - 1 - 1) !}{2 !} \big (v (\{d, t \}) - v (\{t \}) \big),\tag{18}
$$

$$
= \frac {v (\{d \})}{2} + \frac {v (\{d , t \})}{2} - \frac {v (\{t \})}{2},\tag{19}
$$

$$
= \frac {v (\{d , t \})}{2} = \frac {v (\pmb {X} _ {d})}{2} = \frac {v (\pmb {X} _ {t})}{2},\tag{20}
$$

where $\begin{array} { r } { \frac { v ( \{ d \} ) } { 2 } = \frac { v ( \{ t \} ) } { 2 } , } \end{array}$ as it is assumed the data party and the task party exhibit the same feature matrix $( \mathrm { i } . \mathsf { e } . , X _ { d } = X _ { t } )$ in Example 1.

## Appendix B

## Proof of Proposition 1

## Proof of “Master-Aware Efficiency,” “Symmetry,” and “Null Player”

The first three properties can be naturally inferred from the original properties (efficiency, symmetry, and null player) of the Shapley value. Note that the task party’s MShapley-CMI value $\varphi _ { t } \left( = I ( \pmb { X } _ { t } ; Y _ { t } ) \right)$ is only dependent on the task party’s own data set. If we only see data parties ?? as players, then they form a traditional cooperative game with the total value as:

$$
v (\mathcal {D}) = I (\pmb {X} _ {\mathcal {D}}; Y _ {t} | \pmb {X} _ {t}) = I (\pmb {X} _ {\mathcal {D}} \pmb {X} _ {t}; Y t) - I (\pmb {X} _ {t}; Y _ {t}),\tag{21}
$$

Hence, the first three properties can be easily deduced from the Shapley value properties.

## Proof of “Null Duplication”

For proving the fourth property, consider the entropy computation $H ( Y _ { t } | X _ { S } { \pmb X } _ { d } ) ( d \notin S )$ :

$$
H (Y _ {t} | \boldsymbol {X} _ {S} \boldsymbol {X} _ {d}) = - \sum_ {x _ {S} \in \mathcal {X} _ {S}} p (x _ {S} x _ {d}) \sum_ {y _ {t} \in \mathcal {Y} _ {t}} p (y _ {t} | x _ {S} x _ {d}) \log p (y _ {t} | x _ {S} x _ {d}),\tag{22}
$$

By duplicating certain features in d, $\boldsymbol { x } _ { d } = \langle \boldsymbol { x } _ { d } ^ { ( 1 ) } , \boldsymbol { x } _ { d } ^ { ( 2 ) } \rangle$ is changed to $\widetilde { x } _ { d } = \langle x _ { d } ^ { ( 1 ) } , x _ { d } ^ { ( 2 ) } , x _ { d } ^ { ( 2 ) } \rangle$ ⟩. As the duplicated feature is always same as $x _ { d } ^ { ( 2 ) }$ we have:

$$
p (x _ {S} x _ {d}) = p (x _ {S} \tilde {x} _ {d}), p (y _ {t} | x _ {S} x _ {d}) = p (y _ {t} | x _ {S} \tilde {x} _ {d}),\tag{23}
$$

Then,

$$
H (Y _ {t} | \boldsymbol {X} _ {S} \boldsymbol {X} _ {d}) = H \big (Y _ {t} \big | \boldsymbol {X} _ {S} \widetilde {\boldsymbol {X}} _ {d} \big),\tag{24}
$$

Hence, the characteristic function $v _ { y _ { t } } ( S \cup \{ d \} )$ remains unchanged after d duplicates features, leaving MShapley-CMI also unchanged.

## Appendix C

## Proof of Proposition 2

According to Definition 5 and Equation (13), to calculate an MShapley-CMI value, we need to compute cardinality N(·) for each possible combination of $\{ y _ { t } , x _ { t } , \{ x _ { d } | d \in \bar { D } \} \}$ . Let $\mathcal { Y } _ { t } , \mathcal { X } _ { t } .$ , and $\mathcal { X } _ { d } \left( \forall d \in \mathcal { D } \right)$ denote the sets of all possible values of $Y _ { t } , X _ { t }$ , and $X _ { d } .$ , respectively. Therefore, We need to compute cardinality $N ( \cdot )$ for $| \mathcal { Y } _ { t } | | \mathcal { X } _ { t } | \cdot \Pi _ { d \in \mathcal { D } } | \mathcal { X } _ { d } |$ times.

The probability that a falsified N(·) by a malicious server passes the divisibility and non-negativity verifications in one iteration is no larger than min(q<sub>ID</sub>)−1, where min(q<sub>ID</sub>) represents the minimum number of ID duplications across iterations. Considering that there are τ iterations, the probability of a falsified N(·) passing all the verifications in Algorithm 1 regarding one combination of $\{ y _ { t } , x _ { t } , \{ x _ { d } | d \in D \} \}$ is no larger than min(q<sub>ID</sub>)−τ. Given that there are $| \mathcal { Y } _ { t } | | \mathcal { X } _ { t } | \cdot \Pi _ { d \in \mathcal { D } } | \mathcal { X } _ { d } |$ cardinality computations, the probability that a malicious server can successfully deceive the task party during the process of computing an MShapley-CMI value is no larger than min $( q _ { I D } ) ^ { - \tau | \mathcal { Y } _ { t } | | \mathcal { X } _ { t } | \cdot \Pi _ { d \in \mathcal { D } } | \mathcal { X } _ { d } | } . \bigsqcup$

## Appendix D

## Proof of Proposition 3

Computing Shapley-CMI involves two steps: (1) computing PSI cardinality for every combination of party features (Algorithm 1), and (2) using the cardinality results for computing Shapley-CMI (Definition 5).

Step 1: As all the parties send encrypted sample IDs with pseudo-categories to the server, the server can get the cardinality of any party feature combination (i.e., any combination of party pseudo-categories) by iterating all the received IDs one time. As we use ID duplication, redundant computation, and data augmentation schemes for verifiability, the total number of encrypted IDs sent to the server would be $\tau ( q _ { I D } | \mathcal { I } | + n _ { r } )$ , and thus the computation complexity is $O ( \tau ( q _ { I D } | \mathcal { I } | + n _ { r } ) )$ , i.e., linearly proportional to the total number of samples |ℐ|.

Step 2: After the task party receives the PSI cardinality, computing Shapley-CMI needs to compute the mutual information of any subset of parties’ features regarding the task party’s labels. For the set of data parties D, the total number of subsets is 2|D|. For each subset of data parties, we need to calculate the mutual information conditioned on the task parties’ features and labels. As we need to enumerate all the possible value combination of features and labels, the complexity of mutual information computation is $O ( | \mathcal { X } _ { t } | | \mathcal { Y } _ { t } | \cdot \Pi _ { d \in D _ { s } } | \mathcal { X } _ { d } | )$ . However, we notice that the number of total feature and label combinations would not be larger than the total number of samples (as one sample can belong to only one combination), leading to $O ( | \mathcal { X } _ { t } | | \mathcal { Y } _ { t } | \cdot \Pi _ { d \in D _ { s } s } | \mathcal { X } _ { d } | ) < O ( | \mathcal { I } | )$ ). Hence, the total computation complexity for enumerating all party subsets is $O ( 2 ^ { | \mathcal { D } | } \cdot | \mathcal { I } | )$

By combining two steps, the complexity is ${ \cal O } ( ( \tau q _ { I D } + 2 ^ { | \mathcal { D } | } ) | \mathcal { I } | + \tau n _ { r } ) . \big [ $

## Appendix E

## Additional Experiment Results

## Experiments on Missing and Noisy Features

We tested the robustness of FedValue on (1) missing features and (2) noise features.<sup>15</sup> When confronting missing features, FedValue treats missing values as a distinct feature value during CMI computation. Figure E1 shows FedValue’s valuation accuracy through Pearson correlation with ground truth contribution values under missing or noisy features. With up to 10% missing or noisy features, the correlation remains above 0.98/0.96, demonstrating FedValue’s robustness in practice.

![](/api/attachments/T2EMJMJV/fulltext/images/10fb120cbb35a0ef1f4f096e961352a9508325aae7c3281e6c182aac103c30a1.jpg)  
(a) Missing Features

![](/api/attachments/T2EMJMJV/fulltext/images/af656065626e7773d82d63da2a3025f7edbe7ac4aab893234488f82dad39ea86.jpg)  
(b) Noisy features  
Figure E1. Robustness Checks of FedValue

## Experiments on Fairness

We validated FedValue’s ability to ensure fair valuations, i.e., data parties with identical data should receive same valuations (Fan et al., 2022, 2024). Using the LINEAR dataset, we simulated a scenario with four data parties: $d _ { 1 }$ and $d _ { 2 }$ share features $f _ { 1 } { - } f _ { 1 0 } ,$ d<sub>3</sub> holds $f _ { 1 1 } { \mathrm { - } } f _ { 1 5 } ,$ and $d _ { 4 }$ holds f<sub>16</sub>-f<sub>20</sub>; the task party also holds f<sub>11</sub>-f<sub>15</sub>. A fair method should assign equal values to d<sub>1</sub> and d<sub>2</sub>. Table E1 presents the results, including Pearson correlation with ground truth values and the relative difference between d<sub>1</sub> and d<sub>2</sub>’s valuations. Results show that FedValue achieved perfect fairness, with a relative difference of exactly 0 between $d _ { 1 }$ and $d _ { 2 } .$ . While VerFedSV and Shapley-Retrain-LR also exhibited strong fairness, their valuation results deviate significantly from the ground truth (i.e., lower Pearson correlation) compared to FedValue. Thus, FedValue ensures both accurate valuation and fairness.

<table><tr><td colspan="3">Table E1. Fairness Results</td></tr><tr><td rowspan="2"></td><td colspan="2">LINEAR</td></tr><tr><td>Correlation</td><td>Difference</td></tr><tr><td>VF-PS</td><td>0.714</td><td>0.082</td></tr><tr><td>VerFedSV</td><td>0.346</td><td>0.000</td></tr><tr><td>Shapley-SI-LR</td><td>0.566</td><td>0.024</td></tr><tr><td>Shapley-SI-XGB</td><td>0.342</td><td>0.642</td></tr><tr><td>Shapley-SI-DNN</td><td>0.579</td><td>0.070</td></tr><tr><td>Shapley-Retrain-LR</td><td>0.299</td><td>0.000</td></tr><tr><td>Shapley-Retain-XGB</td><td>0.336</td><td>0.006</td></tr><tr><td>Shapley-Retrain-DNN</td><td>0.329</td><td>0.010</td></tr><tr><td>FedValue</td><td>0.998</td><td>0.000</td></tr></table>

Note: “Difference” measures the difference between two data parties with same data: smaller values indicate better fairness.

## Experiments on Antagonistic and Synergistic Feature Interactions

Literature has pointed out that conditional mutual information (CMI) effectively captures both antagonistic and synergistic feature interactions, as it inherently models negative and positive feature interactions (Cheng et al., 2011). Since FedValue leverages CMI to valuate party features, it inherently accounts for such interactions among data parties. Here, we validate this empirically. We adopted the LINEAR dataset for this experiment and conducted the following configurations to simulate antagonistic or synergistic interactions between parties.

Antagonistic: We simulated a task party t and three data parties, $d _ { 1 } , d _ { 2 } ,$ , and $d _ { 3 } .$ Specifically, d<sub>1</sub> holds f<sub>1</sub>-f<sub>5</sub>, d<sub>2</sub> holds f<sub>1</sub> & f<sub>6</sub>-f<sub>10</sub>, d<sub>3</sub> holds $f _ { 1 1 ^ { - } }$ $f _ { 1 5 } ,$ , and the task party t holds f<sub>16</sub>-f<sub>20</sub>. As d<sub>1</sub> and d<sub>2</sub> both hold f<sub>1</sub> (f<sub>1</sub> has a non-zero coefficient), d<sub>1</sub> and d<sub>2</sub> have antagonistic feature interactions.

Synergistic: We generated two new features, $f _ { 1 } ^ { \prime }$ and $f _ { 1 } ^ { \prime \prime }$ . The feature $f _ { 1 } ^ { \prime }$ is randomly set to 0 or 1, while $f _ { 1 } ^ { \prime \prime }$ is determined such that $f _ { 1 }$ is the XOR of $f _ { 1 } ^ { \prime }$ and $f _ { 1 } ^ { \prime \prime } ( f _ { 1 } = f _ { 1 } ^ { \prime } \oplus f _ { 1 } ^ { \prime \prime } )$ . As a result, neither $f _ { 1 } ^ { \prime }$ nor $f _ { 1 } ^ { \prime \prime }$ alone provides any information about the label y. This is because $f _ { 1 } ^ { \prime }$ and $f _ { 1 } ^ { \prime \prime }$ can only influence y through $f _ { 1 , }$ but knowing only $f _ { 1 } ^ { \prime }$ or $f _ { 1 } ^ { \prime \prime }$ does not reveal $. f _ { 1 } ,$ given the intrinsic properties of XOR. Meanwhile, $f _ { 1 } ^ { \prime }$ and $\bar { f _ { 1 } ^ { \prime \prime } }$ are synergistic because their combination uniquely determines $f _ { 1 , }$ thereby impacting $y .$ In this setting, d<sub>1</sub> holds $f _ { 1 } ^ { \prime }$ and f<sub>2</sub>-f<sub>5</sub>, d<sub>2</sub> holds $f _ { 1 } ^ { \prime \prime }$ and f<sub>6</sub>-f<sub>10</sub>, d<sub>2</sub> holds $f _ { 1 1 - } f _ { 1 5 } ,$ and the task party t holds $f _ { 1 6 } \mathrm { - } f _ { 2 0 }$ . Since $d _ { 1 }$ and $d _ { 2 }$ individually hold $f _ { 1 } ^ { \prime }$ and $f _ { 1 } ^ { \prime \prime }$ , respectively, they exhibit synergistic feature interactions.

The results in Table E2 demonstrate that FedValue consistently outperformed benchmarks in both scenarios. Notably, FedValue is the only method capable of maintaining a very high correlation (>0.99) with the ground truth values under synergistic feature interactions.

Table E2. Pearson Correlation With Ground Truth Party Values Under Antagonistic or Synergistic Feature Interactions

<table><tr><td rowspan="2"></td><td colspan="2">LINEAR</td><td></td></tr><tr><td>Antagonistic</td><td>Synergistic</td><td>Average</td></tr><tr><td>VF-PS</td><td>0.918</td><td>0.933</td><td>0.925</td></tr><tr><td>VerFedSV</td><td>0.968</td><td>0.921</td><td>0.945</td></tr><tr><td>Shapley-SI-LR</td><td>0.934</td><td>0.855</td><td>0.895</td></tr><tr><td>Shapley-SI-XGB</td><td>0.991</td><td>0.856</td><td>0.923</td></tr><tr><td>Shapley-SI-DNN</td><td>0.949</td><td>0.858</td><td>0.903</td></tr><tr><td>Shapley-RT-LR</td><td>1.000</td><td>0.883</td><td>0.941</td></tr><tr><td>Shapley-RT-XGB</td><td>1.000</td><td>0.934</td><td>0.967</td></tr><tr><td>Shapley-RT-DNN</td><td>1.000</td><td>0.938</td><td>0.969</td></tr><tr><td>FedValue</td><td>1.000</td><td>0.997</td><td>0.998</td></tr></table>

Note: t-test compares each benchmark with FedValue: ∗ < 0.1, ∗∗ < 0.05, ∗∗∗ < 0.01.

## Additional Results of Case Study: Federated Movie Recommendation

Table E3 presents the performance of federated recommendations for cold-start users without preference data at the task party (but these users can have preference data at data parties). Table E4 highlights the performance under the VAR incentive scheme. Aligning with the main text results, FedValue consistently outperformed benchmarks in these additional experiments.

Table E3. Federated Movie Recommendation Performance Without Substitution Effects for Cold-Start Users When Budget Is α

<table><tr><td></td><td>nDCG@5</td><td>nDCG@10</td><td>MRR</td></tr><tr><td>Volume</td><td>0.0269**</td><td>0.0272**</td><td>0.2642**</td></tr><tr><td>VF-PS</td><td>0.0201*</td><td>0.0204*</td><td>0.2098*</td></tr><tr><td>VerFedSV</td><td>0.0160***</td><td>0.0163***</td><td>0.1754***</td></tr><tr><td>Shapley-SI-LR</td><td>0.0189***</td><td>0.0189***</td><td>0.2013***</td></tr><tr><td>Shapley-SI-XGB</td><td>0.0258*</td><td>0.0261*</td><td>0.2569*</td></tr><tr><td>Shapley-SI-DNN</td><td>0.0274*</td><td>0.0278*</td><td>0.2695*</td></tr><tr><td>Shapley-RT-LR</td><td>0.0189***</td><td>0.0189***</td><td>0.2013***</td></tr><tr><td>Shapley-RT-XGB</td><td>0.0290</td><td>0.0294</td><td>0.2852</td></tr><tr><td>Shapley-RT-DNN</td><td>0.0279*</td><td>0.0283*</td><td>0.2747*</td></tr><tr><td>FedValue</td><td>0.0295</td><td>0.0300</td><td>0.2905</td></tr></table>

Note: t-test compares each benchmark with FedValue: ∗ < 0.1, ∗∗ < 0.05, ∗∗∗ < 0.01.

<table><tr><td colspan="4">Table E4. Federated Movie Recommendation Performance Without Substitution Effects Under the VAR Incentive Scheme When Budget Is 2α</td></tr><tr><td></td><td>nDCG@5</td><td>nDCG@10</td><td>MRR</td></tr><tr><td>Volume</td><td>0.0299***</td><td>0.0302***</td><td>0.2852***</td></tr><tr><td>VF-PS</td><td>0.0303*</td><td>0.0305*</td><td>0.2914*</td></tr><tr><td>VerFedSV</td><td>0.0303**</td><td>0.0305**</td><td>0.2916**</td></tr><tr><td>Shapley-SI-LR</td><td>0.0299*</td><td>0.0300*</td><td>0.2905*</td></tr><tr><td>Shapley-SI-XGB</td><td>0.0304**</td><td>0.0309**</td><td>0.2874**</td></tr><tr><td>Shapley-SI-DNN</td><td>0.0307**</td><td>0.0313**</td><td>0.2885**</td></tr><tr><td>Shapley-RT-LR</td><td>0.0299*</td><td>0.0300*</td><td>0.2905*</td></tr><tr><td>Shapley-RT-XGB</td><td>0.0314</td><td>0.0319</td><td>0.2940</td></tr><tr><td>Shapley-RT-DNN</td><td>0.0317</td><td>0.0319</td><td>0.3035</td></tr><tr><td>FedValue</td><td>0.0325</td><td>0.0329</td><td>0.3059</td></tr></table>

## Case Study: Federated Item Recommendation on Amazon

We also conducted a case study using the Amazon Review ’23 dataset.<sup>16</sup> To simulate a federated recommendation scenario, each party is assigned a specific item category (Li et al., 2024): the task party handles yooks, while data parties hold Kindle\_Store, Electronics, Tools\_and\_Home\_Improvement, and Movies\_and\_TV. Other experimental setups are the same as the federated movie recommendation. Table E5 presents results under the FIX incentive scheme with a budget of α, showing that FedValue performed the best among all methods.

<table><tr><td colspan="4">Table E5. Federated Item Recommendation Performance on Amazon Review &#x27;23</td></tr><tr><td></td><td>nDCG@5</td><td>nDCG@10</td><td>MRR</td></tr><tr><td>Volume</td><td>0.0024***</td><td>0.0028***</td><td>0.0096***</td></tr><tr><td>VF-PS</td><td>0.0028**</td><td>0.0034</td><td>0.0100</td></tr><tr><td>VerFedSV</td><td>0.0027**</td><td>0.0031*</td><td>0.0096</td></tr><tr><td>Shapley-SI-LR</td><td>0.0024***</td><td>0.0028***</td><td>0.0096***</td></tr><tr><td>Shapley-SI-XGB</td><td>0.0022***</td><td>0.0025***</td><td>0.0086***</td></tr><tr><td>Shapley-SI-DNN</td><td>0.0027*</td><td>0.0030*</td><td>0.0093</td></tr><tr><td>Shapley-RT-LR</td><td>0.0024***</td><td>0.0028***</td><td>0.0096***</td></tr><tr><td>Shapley-RT-XGB</td><td>0.0024***</td><td>0.0028***</td><td>0.0096***</td></tr><tr><td>Shapley-RT-DNN</td><td>0.0029</td><td>0.0034</td><td>0.0100</td></tr><tr><td>FedValue</td><td>0.0034</td><td>0.0036</td><td>0.0102</td></tr></table>

## Appendix F

## An Example of Pseudo-Category PSIC Computation

Consider a simple case in Figure F1. Each party encrypts their sample IDs and transmits them alongside assigned pseudo-categories. The server then computes the PSI-Cardinality (PSIC) for all feature combinations (e.g., eight combinations in this example) with a singl transmission of encrypted data. In contrast, a naive PSIC implementation requires repeated ID transmissions for each computation. For instance, in Data Party 1, IDs (e.g., ID1 and ID2) linked to feature category A0 would be transmitted four times due to A0 appearing in four combinations. This redundancy grows exponentially with the number of features, drastically reducing efficiency. Our pseudo-category-based PSIC eliminates this redundancy by transferring IDs only once, significantly enhancing computational efficiency.

![](/api/attachments/T2EMJMJV/fulltext/images/fd3a7a0bce8980f3131abe5c2225f873a34051a932485c5f60ace5d0857c8679.jpg)
