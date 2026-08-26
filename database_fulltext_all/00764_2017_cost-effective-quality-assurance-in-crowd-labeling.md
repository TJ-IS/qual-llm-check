---
otero_id: 764
otero_key: "MYWW5GR9"
title: "Cost-Effective Quality Assurance in Crowd Labeling"
authors: "Jing Wang; Panagiotis G. Ipeirotis; Foster Provost"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0661"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [134.148.10.12] On: 23 February 2017, At: 08:13 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## HSR

## Information Systems Research

![](/api/attachments/MYWW5GR9/fulltext/images/601c7885f7b78de48b3c2d4484f32cbc1f1ef8f43aa17445de55917a0b8364be.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Cost-Effective Quality Assurance in Crowd Labeling

Jing Wang, Panagiotis G. Ipeirotis, Foster Provost

To cite this article:

Jing Wang, Panagiotis G. Ipeirotis, Foster Provost (2017) Cost-Effective Quality Assurance in Crowd Labeling. Information Systems Research

Published online in Articles in Advance 09 Feb 2017

http://dx.doi.org/10.1287/isre.2016.0661

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/MYWW5GR9/fulltext/images/8ff59b842b980be3e00ec7a804b393e75cb0d3a013e52c79032d8325a1a38974.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Cost-Efective Quality Assurance in Crowd Labeling

Jing Wang,<sup>a</sup> Panagiotis G. Ipeirotis,<sup>b</sup> Foster Provost <sup>b</sup>

<sup>a</sup> School of Business and Management, Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong; <sup>b</sup> Leonard Stern School of Business, New York University, New York, New York 10012

Contact: jwang@ust.hk (JW); panos@stern.nyu.edu (PGI); fprovost@stern.nyu.edu (FP)

Received: August 14, 2014 Revised: Accepted: June 2, 2016 Published Online in Articles in Advance: February 9, 2017

https://doi.org/10.1287/isre.2016.0661

Copyright: © 2017 INFORMS

Abstract. The emergence of online paid micro-crowdsourcing platforms, such as Amazon Mechanical Turk, allows on-demand and at-scale distribution of tasks to human workers around the world. In such settings, online workers come and complete small tasks posted by employers, working for as long or as little as they wish, a process that eliminates the overhead of hiring (and dismissal). This flexibility introduces a diferent set of ineficiencies: verifying the quality of every submitted piece of work is an expensive operation that often requires the same level of efort as performing the task itself. A number of research challenges arise in such settings. How can we ensure that the submitted work is accurate? What allocation strategies can be employed to make the best use of the available labor force? How can we appropriately assess the performance of individual workers? In this paper, we consider labeling tasks and develop a comprehensive scheme for managing the quality of crowd labeling: First, we present several algorithms for inferring the true classes of objects and the quality of participating workers, assuming the labels are collected all at once before the inference. Next, we allow employers to adaptively decide which object to assign to the next arriving worker and propose several heuristic-based dynamic label allocation strategies to achieve the desired data quality with significantly fewer labels. Experimental results on both simulated and real data confirm the superior performance of the proposed allocation strategies over other existing policies. Finally, we introduce two novel metrics that can be used to objectively rank the performance of crowdsourced workers after fixing correctable worker errors and taking into account the costs of diferent classification errors. In particular, the worker value metric directly measures the monetary value contributed by each label of a worker toward meeting the quality requirements and provides a basis for the design of fair and eficient compensation schemes.

History: Gediminas Adomavicius, Senior Editor; Gautam Pant, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2016.0661.

Keywords: crowd labeling • quality assurance • dynamic label allocation • worker performance metrics

## 1. Introduction

Crowdsourcing has emerged over the last few years as an important new labor pool for a variety of tasks (Malone et al. 2009), ranging from microtasks posted on platforms like Amazon Mechanical Turk<sup>1</sup> (AMT) to big innovation contests conducted by Netflix<sup>2</sup> and Innocentive.<sup>3</sup> Today, AMT, in particular, dominates the market for crowdsourcing microtasks, which are easy for humans to accomplish but remain challenging for computers (Ipeirotis 2010). The employers on AMT can post a variety of small tasks, such as image tagging, sentiment judgment, language translation, and text annotation. Workers complete these tasks and get compensated in the form of micropayments, typically in the range of 5 to 20 cents per task. The immediate and elastic supply of cheap labor in microcrowdsourcing systems makes it possible to complete tasks at low cost and with high throughput.

Firms, ranging from Fortune 500 companies to small start-ups, are increasingly attracted to microcrowdsourcing to meet their business needs. Amazon has been using micro-crowdsourcing for more than 10 years to deduplicate products in catalogs uploaded to its platform by merchants. Microsoft has built the Universal Human Relevance System (UHRS) to evaluate and improve the performance of its search engine—Bing. Facebook has been relying on microcrowdsourcing for content moderation, and Twitter is using AMT to improve its real-time event detection accuracy. Many other companies employ microcrowdsourcing either directly or through an intermediary (e.g., AMT, CrowdFlower, CrowdSource).

Micro-crowdsourcing platforms are also increasingly used by information systems (IS) researchers for a wide variety of data labeling and annotation tasks. To study the impact of review text on product sales, Archak et al. (2011) recruited workers from AMT to extract product features and opinions about these features from the text of product reviews. Moreno and Terwiesch (2014) used AMT workers to code the sentiment of comments left by previous service buyers as either positive or negative and constructed a reputation measure for service providers based on this information. Wang et al. (2012) also relied on the AMT platform to obtain a reliable measure of the perceived helpfulness of user-generated reviews.

Despite the promise, significant challenges remain. Workers in microtask crowdsourcing markets usually have diferent levels of expertise and dedication and thus exhibit heterogeneous quality in task execution. Unfortunately, verifying the quality of every submitted answer is an expensive operation and negates many advantages of micro-crowdsourcing: the cost and time for verifying the correctness of each submitted answer (e.g., checking the answers for a question such as “Do you see any recognizable human face in the picture?”) are typically comparable to the cost and time for performing the task itself. The dificulty of verification makes micro-crowdsourcing systems prone to errors, which harms the reliability, scalability, and robustness of such markets (Wais et al. 2010).

Our main research objective is to develop a comprehensive scheme for assuring the quality of microtask crowdsourcing in a cost-efective manner. In this paper, we focus on the quality control of binary labeling tasks (e.g., “Does this photograph violate the terms of service? Yes or No.”). While this might seem limiting, we show in Online Appendix A that many complex tasks can be broken down into a set of simpler operations for which a binary choice task serves as a key building block for quality assurance. Hence, our proposed scheme naturally fits into such workflows and provides a fundamental quality control mechanism for other more complicated operations. Such synergies lead to workflows that can accomplish complex tasks with guarantees of high-quality output, even when the underlying workforce has uncertain, varying, or even moderate-to-low quality.

In the crowd labeling settings, one common approach used by employers to ensure reliability is to introduce redundancy: ask multiple workers to work on the same task and infer the correct answer using some aggregation method such as majority voting. In this paper, we are interested in the following optimization problem: Suppose an employer wishes to achieve a certain level of data labeling quality, what strategies can she use to minimize the expense of acquiring labels from crowdsourced workers?

The decision system in our framework consists of two phases: a label allocation phase and an inference phase. In the label allocation phase, the unlabeled or partially labeled objects are assigned to crowdsourced workers for labeling. In the inference phase, an algorithm is used to infer the true classes of objects. The system is called static if the inference phase begins after the full completion of the allocation phase. In a static system, labels are allocated all at once before the inference process starts. Most of the previous studies assume one-time allocation of labels and devote the research efort to improving the inference accuracy (e.g., Whitehill et al. 2009, Raykar et al. 2010, Welinder et al. 2010, Karger et al. 2011). The system is called dynamic if the two phases are interleaved. A dynamic system iterates over these two phases until the desired data quality is achieved or the available resources are exhausted, allowing the employer to adaptively decide which object to assign to the next arriving worker based on the stream of collected labels so far. Figure 1 illustrates these two decision systems.

![](/api/attachments/MYWW5GR9/fulltext/images/7e887a3bb6c214849698fef821094decb000575ce3eb3fb941ad5afe7a58c817.jpg)

The characteristics of microtask crowdsourcing platforms make them well suited for the implementation of a dynamic decision system. Workers arrive in the market over time, and once they agree to work on tasks, they label the objects one after another. The decision about which object to assign to the worker next can be postponed until she finishes labeling the current object. Since the allocation decision can be made within a very short period of time, the worker will not feel any latency in waiting for the next labeling task. As will be shown later, the possibility of making label assignments on the spot instead of beforehand allows the employer to make eficient use of available information at each step and reduce the total expense incurred during the labeling process.

In this paper, we consider a typical labeling scenario in which the easiness of the objects and the quality of the workers are both heterogeneous. We focus on a dynamic environment where workers arrive over time while the employer is running the task so that incoming workers can be assigned to individual objects dynamically. To harness the potential of this dynamic decision system, we propose several heuristic-based label allocation strategies that adaptively choose which object to label next, based on the algorithmic estimates of object and worker quality from all of the labels obtained so far. Using experiments on both synthetic and real-world data sets, we demonstrate that our proposed dynamic label allocation methods can achieve significant savings in labeling expenses and completion time.

Another contribution of this paper is to use a decision-theoretic approach to generate two performance metrics for each worker, both of which allow the employer to separate correctable errors from uncorrectable errors that workers make and take into account the costs of diferent classification errors. In particular, the worker value metric directly measures the monetary contribution of each label provided by a worker toward meeting the quality requirements of the employer and provides a basis for the employer to grant monetary bonuses to high-quality workers who contribute more than they earn and block inferior workers whose contributed value is not worth the payment.

Our paper responds to the call for more research on design science in the IS field (e.g., Hevner et al. 2004, March and Storey 2008, Kuechler and Vaishnavi 2012, Gregor and Hevner 2013, Goes 2014). As mentioned earlier, companies today invest substantial amounts of money in gathering information and knowledge from crowdsourced workers. Therefore, the problem of cost reduction in information acquisition is of tremendous importance to business organizations. By formulating a decision problem in the dynamic crowd labeling environment, developing techniques that can manage quality assurance cost efectively, and demonstrating the eficacy of the proposed methods via rigorous experimentation, this work will help companies to dramatically reduce data acquisition costs and engage in faster and more eficient decision making in their business processes.

The remainder of the paper is organized as follows. Section 2 reviews the related literature. Section 3 outlines the modeling assumptions and formalizes the problem. Section 4 describes the inference algorithms for estimating the true classes of objects and the quality of workers. Section 5 proposes several heuristic-based dynamic label allocation strategies that aim to reduce labeling expenses while maintaining the required level of data quality. Sections 6 and 7 evaluate the performance of inference and allocation algorithms using simulated and real-world data sets, respectively. Section 8 introduces two scalar metrics for evaluating the performance of heterogeneous workers and discusses the potential of worker value metric for compensation scheme design. Section 9 concludes by presenting practical implications, limitations, and directions for future research.

## 2. Literature Review

In this section, we survey the relevant literature in three streams of research: quality estimation and control, worker performance metrics, and active information acquisition.

## 2.1. Quality Estimation and Control

A simple approach to measure the quality of submitted answers is to use gold data: insert a small percentage of tasks for which the correct answers are known and measure the performance on these tasks. The testing of worker quality using gold labels is related to, but distinct from, two lines of research: test theory in psychometrics and education (Crocker and Algina 2006, DeMars 2010), and acceptance sampling in operation management (Wetherill and Chiu 1975, Berger 1982, Schilling 1982). Existing test theory models do not consider the additional costs incurred in labeling gold data, which is analogous to the inspection cost in the manufacturing process. In acceptance sampling, a production lot of items will get rejected if the number of defective items in a sample exceeds a threshold, whereas in crowd labeling markets that deal with information goods, low-quality work can be combined to provide high-quality outcomes.

Another method for ensuring quality is to ask multiple workers to complete the same task and use majority voting (MV) to identify the correct answer. In reality, most employers check labels provided by workers with MV and dismiss workers systematically in disagreement with the majority. This approach has two undesirable properties: First, it does not account for heterogeneity in the exhibited quality of workers; second, it causes sufering for diligent and informative workers whose answers are wrong but correctable.

Several more advanced aggregation methods have been developed in the past years. Dawid and Skene (1979) present an expectation maximization (EM) algorithm to simultaneously estimate the true responses for patients and the error rates of observers. The algorithm iterates until convergence, following two steps: (1) it estimates the true response for each patient, using records given by all observers, accounting for the error rates of each observer; and (2) it estimates the error rates of each observer by comparing the submitted records with estimated true responses. Variations of the algorithm were recently proposed by Carpenter (2008) and by Raykar et al. (2010). Welinder et al. (2010) develop a generative Bayesian model in which each annotator is a multidimensional entity with variables representing competence, expertise, and bias. Inspired by the standard belief propagation algorithm, Karger et al. (2011) introduce a novel message-passing technique to jointly infer the correct answers of the tasks and the reliability of workers. Whitehill et al. (2009) incorporate task dificulty into the labeling process and present a probabilistic model that simultaneously infers the expertise of each worker, and the label and the dificulty of each task. The decision systems in these papers are all static and involve no adaptive allocation of labels.

## 2.2. Worker Performance Metrics

All of the above inference algorithms generate some indicators of worker performance in scalar, vector, or matrix form. For example, MV measures the accuracy rate of each worker by the proportion of the labels submitted by the worker in agreement with the majority labels. The EM algorithm proposed by Dawid and Skene (1979) returns a confusion matrix, which lists the probabilities of diferent classification errors made by each worker. Welinder et al. (2010) measure worker ability in a multidimensional space, with each element modeling the worker’s individual weight on each of the major components of the annotation task. Karger et al. (2011) use a set of task-specific worker messages to represent the belief of how reliable a worker is in labeling each specific task. Whitehill et al. (2009) employ a scalar value to model the expertise of each worker.

However, none of these metrics can efectively quantify the contributed value of each label provided by an individual worker in meeting the quality assurance needs of the employer. First, they cannot separate correctable errors from uncorrectable errors that workers make. For example, a malicious worker may always submit wrong labels, but these labels are informative, as they can be reversed to uncover the truth. In such cases, the naïve measurement of accuracy rate results in an underestimate of the value of workers who consistently give predictably incorrect answers. Second, they fail to take into account the relative costs of diferent types of classification errors. Understandably, some types of misclassification errors incur significantly higher costs than others. For example, allowing a porn image to pass a moderation filter is often more costly than blocking a legitimate image incorrectly. Third, a number of workers often need to work in tandem to generate labels of acceptable quality; therefore, it is more appropriate to evaluate the performance of each worker in a multiple-label setting than treating them as isolated. In our work, we propose a value-based performance metric that directly measures the monetary contribution of each worker in a multiple-label setting, after fixing correctable worker errors and accounting for heterogeneity in misclassification costs across diferent types of classification errors.

## 2.3. Active Information Acquisition

Active information acquisition, which focuses on gathering various types of information incrementally so as to achieve diferent objectives cost efectively, has been an important topic in the machine learning and management literature. Moore and Whinston (1986, 1987) develop a theoretical decision-making framework in which the decision maker gathers costly information optimally and sequentially to reduce the uncertainty associated with the final decisions. There have been a large number of papers devoted to active learning (e.g., Cohn et al. 1994, Lewis and Gale 1994, Roy and McCallum 2001, Saar-Tsechansky and Provost 2004), which aim to economize resources on training instances that are more likely to be informative for building classifiers. Another stream of papers (Lizotte et al. 2003, Zheng and Padmanabhan 2006, Saar-Tsechansky and Provost 2007, Saar-Tsechansky et al. 2009) study the active feature-value acquisition problem in scenarios where the feature values of the training data are costly to acquire.

In the context of dynamic label allocation using multiple noisy workers, Sheng et al. (2008) and Ipeirotis et al. (2014) develop several selective repeated-labeling strategies and show that selective allocation of labeling resources can improve the overall labeling quality and model prediction accuracy. However, both papers assume that all workers have an equal level of quality when labeling the same instance and the costs incurred by diferent classification errors are identical, which rarely hold in real-life scenarios.

Another emerging set of research papers takes an additional step by allowing employers to selectively target workers when requesting labels. The underlying assumption is that employers can arbitrarily exploit high-quality workers by asking them to label as many objects as possible. For instance, Welinder and Perona (2010) propose a dynamic allocation approach in which the employer can prioritize expert workers by asking them to label more in the annotation process. Chen et al. (2015) formulate a budget allocation problem where the employer can simultaneously choose which instance to label next and which worker to assign the task to. These studies have limited applicability in platforms where workers’ arrivals are exogenous and not under the control of employers. For example, workers on AMT arrive in real time and may work for as long or as little as they wish, depending on their own interests and time constraints. In this paper, we work under the assumption that workers’ arrival and participation are not controlled by the employer, and focus on the dynamic task allocation problem that aims to reduce labeling expenses by adaptively selecting which object to assign to a worker conditional on her agreement to continue providing labels.

## 3. Modeling Framework

In this section, we describe our modeling assumptions and formalize the problem. Table 1 summarizes the notations used in this paper.

## 3.1. Scenario

We consider a typical scenario in crowd labeling. An employer has a set of unlabeled objects and wants them to be labeled with the correct classes (e.g., judging whether a Facebook post contains hate speech). The employer may incur diferent costs in making different types of classification errors. For instance, it is more costly for Facebook to classify a hate speech post as OK than to classify a legitimate post as hate speech. We assume that the employer’s misclassification costs can be represented by a matrix c: The cost $c _ { i j }$ is incurred when an object with true class i is categorized into class $j . ^ { 4 }$ The average misclassification cost is used to quantify the quality of labeling. The goal of the employer is to guarantee that the average misclassification cost will not exceed a threshold $\tau _ { c } .$ We further assume that the employer can derive a value of V from each labeled object with average misclassification cost not exceeding $\tau _ { c }$

Table 1. Notations

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $t^{(o)}$ </td><td>True class of object (o)</td></tr><tr><td> $\mathbf{c}$ </td><td>Misclassification cost matrix</td></tr><tr><td> $c_{ij}$ </td><td>Cost incurred when an object with true class i is classified into class j</td></tr><tr><td> $\tau_c$ </td><td>Threshold for the average misclassification cost</td></tr><tr><td>V</td><td>Value of each object with average misclassification cost below  $\tau_c$ </td></tr><tr><td> $l^{(k)}_{(o)}$ </td><td>Label that worker (k) assigns to object (o)</td></tr><tr><td>L</td><td>Set of observed labels  $\{l^{(k)}_{(o)}\}$ </td></tr><tr><td> $\boldsymbol{\alpha}^{(k)}$ </td><td>Quality vector of worker (k)</td></tr><tr><td> $\alpha_i^{(k)}$ </td><td>Quality of worker (k) on labeling objects in class i</td></tr><tr><td> $\beta^{(o)}$ </td><td>Easiness of object (o)</td></tr><tr><td> $\hat{t}^{(o)}$ </td><td>Estimated true class of object (o)</td></tr><tr><td> $K^{(o)}$ </td><td>Set of workers who assign labels to object (o)</td></tr><tr><td> $O^{(k)}$ </td><td>Set of objects labeled by worker (k)</td></tr><tr><td>I(·)</td><td>Indicator function for an event</td></tr><tr><td>|·|</td><td>Cardinality of a set</td></tr><tr><td> $\mathbf{p}^{(o)}$ </td><td>Vector with probability estimates for the true class of object (o)</td></tr><tr><td> $p_i^{(o)}$ </td><td>Estimated probability that the true class of object (o) is i</td></tr><tr><td> $q^{(k)}$ </td><td>Accuracy rate of worker (k) (for MV)</td></tr><tr><td> $\pi$ </td><td>Vector with prior probabilities of all classes</td></tr><tr><td> $\pi_i$ </td><td>Prior probability of class i</td></tr><tr><td> $\mathbf{e}^{(k)}$ </td><td>Confusion matrix for worker (k) (for EM)</td></tr><tr><td> $e_{ij}^{(k)}$ </td><td>Probability that worker (k) labels an object of class i into class j (for EM)</td></tr><tr><td> $L^{(o)}$ </td><td>Set of observed labels on object (o)</td></tr><tr><td> $\hat{\pi}_j^{(k)}$ </td><td>Estimated prior probability that worker (k) assigns label j</td></tr></table>

The employer posts the task on a micro-crowdsourcing platform (e.g., AMT, CrowdFlower, Crowd-Source). Workers arrive at the platform over time and search for tasks they are interested in. When a worker agrees to perform the task, the employer presents the to-be-labeled objects to the worker one after another, until she stops working or the employer achieves the quality requirements.

## 3.2. The Labeling Model

In the labeling task, each object <sup>(</sup>o<sup>)</sup> is associated with a latent true class $t ^ { ( o ) }$ , picked from one of two possible classes, 0 or 1 $( \mathrm { e . g . }$ , positive/negative, useful/not useful). The true class $\bar { t } ^ { ( o ) }$ is unknown, and the task is to infer the true class for each object <sup>(</sup>o<sup>)</sup>. The objects to be labeled may vary in their level of easiness. For example, a hate speech that directly attacks people based on their ethnicity is easier to identify than a hate speech that demeans people in a subtle way.

To incorporate the efect of object easiness, we adapt the labeling model from Whitehill et al. (2009), but allow workers’ quality to vary across the two classes. The observed label $l _ { ( o ) } ^ { ( k ) }$ provided by worker <sup>(</sup>k<sup>)</sup> on object <sup>(</sup>o<sup>)</sup> is jointly determined by three factors: (1) the quality of worker <sup>(</sup>k<sup>)</sup>; (2) the easiness of object <sup>(</sup>o<sup>)</sup>; and (3) the true class of object <sup>(</sup>o<sup>)</sup>.

We model the quality of each worker <sup>(</sup>k<sup>)</sup> using a two-dimensional vector $\pmb { \alpha } ^ { ( k ) } = ( \alpha _ { 0 } ^ { ( k ) } , \alpha _ { 1 } ^ { ( k ) } ) .$ , where $\alpha _ { i } ^ { ( \widetilde { k } ) } \in$ <sup>(+∞</sup>, <sup>−∞)</sup> represents worker $( k ) ^ { \prime } \mathbf { s }$ quality on labeling objects belonging to class i. Here, $\alpha _ { i } ^ { ( k ) } \stackrel { \cdot } { = } + \infty$ means worker <sup>(</sup>k<sup>)</sup> always labels objects in class i correctly; and ${ \alpha } _ { i } ^ { ( k ) } = - \infty$ means worker <sup>(</sup>k<sup>)</sup> always labels objects in class i incorrectly. Note that unlike Whitehill et al. (2009), we do not impose the constraint that $\alpha _ { 0 } ^ { ( k ) } = \alpha _ { 1 } ^ { ( k ) }$ and allow the quality of each worker to vary by classes. For example, if worker <sup>(</sup>k<sup>)</sup> labels all objects into class $i ,$ then $\alpha _ { i } ^ { ( k ) } = + \infty$ and $\alpha _ { 1 - i } ^ { ( k ) } = - \infty$

The easiness of each object <sup>(</sup>o<sup>)</sup> is modeled by $\beta ^ { ( o ) } .$ where $\beta ^ { ( o ) } \in [ 0 , + \infty )$ is constrained to be positive. Here, $\beta ^ { ( o ) } = 0$ means object <sup>(</sup>o<sup>)</sup> is very dificult to label, and even a high-quality worker only has a 50% probability of labeling it correctly; and $\beta ^ { ( o ) } = + \infty$ means object <sup>(</sup>o<sup>)</sup> is very easy to label, and even a low-quality worker can label it correctly with 100% probability.

Under the labeling model, the log adds of the obtained label being correct is a bilinear function of the quality of worker <sup>(</sup>k<sup>)</sup> on class $t ^ { ( o ) }$ and the easiness of the object <sup>(</sup>o<sup>)</sup>, i.e.,

$$
\log \frac {p (l _ {(o)} ^ {(k)} = t ^ {(o)} \mid \alpha_ {t ^ {(o)}} ^ {(k)} , \beta^ {(o)})}{1 - p (l _ {(o)} ^ {(k)} = t ^ {(o)} \mid \alpha_ {t ^ {(o)}} ^ {(k)} , \beta^ {(o)})} = \alpha_ {t ^ {(o)}} ^ {(k)} \beta^ {(o)}.
$$

Thus, the label $l _ { ( o ) } ^ { ( k ) }$ given by worker <sup>(</sup>k<sup>)</sup> to object <sup>(</sup>o<sup>)</sup> is generated as follows:

$$
p (l _ {(o)} ^ {(k)} = t ^ {(o)} \mid \alpha_ {t ^ {(o)}} ^ {(k)}, \beta^ {(o)}) = \frac {1}{1 + e ^ {- \alpha_ {t ^ {(o)}} ^ {(k)} \beta^ {(o)}}}\tag{1}
$$

and

$$
p \left(l _ {(o)} ^ {(k)} = 1 - t ^ {(o)} \mid \alpha_ {t ^ {(o)}} ^ {(k)}, \beta^ {(o)}\right) = 1 - \frac {1}{1 + e ^ {- \alpha_ {t ^ {(o)}} ^ {(k)} \beta^ {(o)}}} = \frac {1}{1 + e ^ {\alpha_ {t ^ {(o)}} ^ {(k)} \beta^ {(o)}}}. \tag {2}\tag{2}
$$

Understandably, the probability that worker <sup>(</sup>k<sup>)</sup> labels object <sup>(</sup>o<sup>)</sup> correctly increases with her labeling quality on class $t ^ { ( o ) }$ and the easiness of the object <sup>(</sup>o<sup>)</sup>.

## 4. Inference

In this section, we describe several algorithms for inferring the true classes of objects and the quality of workers.

## 4.1. Majority Voting

The simplest method to estimate the true class of an object is MV, which simply ignores any heterogeneity in worker quality and takes the majority label provided by multiple workers. The performance of each worker is measured by accuracy rate (i.e., how frequently the worker agrees with the majority label). Algorithm 1 presents a sketch of the MV algorithm. Because of its simplicity, MV is commonly used by employers who lack competence in data processing.

Algorithm 1 (Majority voting (MV) inference algorithm)

Input: The set of observed labels ${ \cal L } = \{ l _ { ( o ) } ^ { ( k ) } \}$

Output: Estimated true class $\hat { t } ^ { ( o ) }$ for each object <sup>(</sup>o<sup>)</sup>, accuracy rate ${ q ^ { ( k ) } }$ for each worker <sup>(</sup>k<sup>)</sup>

1 Estimate the class probability estimates for each

object <sup>(</sup>o<sup>)</sup>: $p _ { i } ^ { ( o ) } = \frac { \sum _ { ( k ) \in K ^ { ( o ) } } I ( l _ { ( o ) } ^ { ( k ) } = i ) } { | K ^ { ( o ) } | } ;$

2 Estimate the true class using the majority label for object $( o ) \colon { \hat { t } } ^ { ( o ) } = \arg \operatorname* { m a x } _ { i \in \{ 0 , 1 \} } p _ { i } ^ { ( o ) } ;$

3 Estimate the accuracy rate of each worker <sup>(</sup>k<sup>)</sup>:

$$
q ^ {(k)} = \frac {\sum_ {(o) \in O ^ {(k)}} I (l _ {(o)} ^ {(k)} = \hat {t} ^ {(o)})}{| O ^ {(k)} |}.
$$

## 4.2. Message Passing

Inspired by the standard belief propagation algorithm, Karger et al. (2011) introduce a message passing (MP) algorithm that jointly infers the true classes of objects and the reliability of workers. The algorithm iteratively operates on a set of object messages and worker messages: at each object update, it gives more weight to labels that come from more trustworthy workers; and at each worker update, it adds more confidence in that worker if the labels she gives on other objects agree with the current estimates of object labels. The details of the MP algorithm are given in Algorithm 2.<sup>5</sup>

Another advanced inference technique is EM, first proposed by Dawid and Skene (1979) in the context of medical diagnosis. The algorithm iterates until convergence, following two steps: (1) it estimates the true class for each object using the labels provided by a set of workers, accounting for the error rates of each worker; and (2) it estimates the error rates of each worker by comparing the submitted labels with estimated true class for each object. The performance of each worker <sup>(</sup>k<sup>)</sup> is represented by a confusion matrix $\mathbf { e } ^ { ( k ) }$ , where $e _ { i j } ^ { ( k ) }$ gives the probability that worker <sup>(</sup>k<sup>)</sup> classifies an object of class i into class j.

## 4.3. Expectation Maximization

To incorporate priors on worker quality, we move from maximum likelihood estimates to Bayesian ones. If the true class of an object is $i ,$ we model the error rates of the worker <sup>(</sup>k<sup>)</sup> as a beta distribution with parameter vector ${ \Theta } _ { i } ^ { ( k ) }$ . The value of $\theta _ { i j } ^ { ( k ) }$ is given by $\theta _ { i j } ^ { ( k ) } =$ $\lambda _ { i j } ^ { ( k ) } + n _ { i j } ^ { ( k ) }$ , where $n _ { i j } ^ { ( k ) }$ represents the number of times that the worker classifies objects of class i into class j and $\lambda _ { i j } ^ { ( k ) }$ captures the prior belief. Using this strategy, the error rates of a worker can be fully captured by two beta distributions. Algorithm 3 presents a sketch of the process, where $\theta ^ { ( k ) }$ parameterizes the error rate distributions of worker <sup>(</sup>k<sup>)</sup> and $\mathbf { e } ^ { ( k ) }$ is defined by the expected values.

Algorithm 2 (Message passing (MP) inference algorithm)

## 4.4. Generative Model of Labels, Abilities,

## and Dificulties

All of the previous inference algorithms ignore the possible heterogeneity of object easiness and simply attribute the generation of noisy labels to imperfect worker quality. However, as illustrated in Section 3.2, the observed labels provided by workers on a particular object may also depend on the easiness of the object.

Following Whitehill et al. (2009), we propose a generative model of labels, abilities, and dificulties (GLAD) and use an EM approach to obtain the maximum likelihood estimates of the $\alpha ^ { ( k ) } , \beta ^ { ( o ) } .$ , and $t ^ { ( o ) }$ for each worker <sup>(</sup>k<sup>)</sup> and each object <sup>(</sup>o<sup>)</sup>.

Input: The set of observed labels ${ \cal L } = \{ l _ { ( o ) } ^ { ( k ) } \}$

Output: Estimated true class $\hat { t } ^ { ( o ) }$ for each object <sup>(</sup>o<sup>)</sup>, object message $\{ x _ { ( o ) \to ( k ) } \}$ , and worker message

$\{ y _ { ( k ) \to ( o ) } \}$ for each object <sup>(</sup>o<sup>)</sup> and worker <sup>(</sup>k<sup>)</sup> with $l _ { ( o ) } ^ { ( k ) } \in { \cal L }$

1 Initialize each worker message: draw $y _ { ( k ) \to ( o ) }$ from a Gaussian distribution N<sup>(</sup>1, 1<sup>)</sup>;

2 while not converged do

3 Update each object message: $\begin{array} { r } { x _ { ( o )  ( k ) } = \sum _ { ( k ^ { \prime } ) \in K ^ { ( o ) } \backslash ( k ) } ( 2 l _ { ( o ) } ^ { ( k ) } - 1 ) y _ { ( k ^ { \prime } )  ( o ) } ; } \end{array}$

Update each worker message: $\begin{array} { r } { y _ { ( k )  ( o ) } = \sum _ { ( o ^ { \prime } ) \in O ^ { ( k ) } \backslash ( o ) } ( 2 l _ { ( o ) } ^ { ( k ) } - 1 ) x _ { ( o ^ { \prime } )  ( k ) } ; } \end{array}$

5 end

6 Calculate the estimated true class for each object <sup>(</sup>o<sup>)</sup>: $\begin{array} { r } { \hat { t } ^ { ( o ) } = \frac { 1 } { 2 } ( 1 + \mathrm { s i g n } ( \sum _ { ( k ) \in K ^ { ( o ) } } ( 2 l _ { ( o ) } ^ { ( k ) } - 1 ) y _ { ( k )  ( o ) } ) ) . } \end{array}$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
2 while not converged do
3    Estimate the  $\boldsymbol{\theta}^{(k)}\colon\theta_{ij}^{(k)}=\lambda_{ij}^{(k)}+n_{ij}^{(k)}=\lambda_{ij}^{(k)}+\sum_{(o)\in O^{(k)}}p_{i}^{(o)}I(l_{(o)}^{(k)}=j);$ 
4    Estimate the confusion matrix  $\mathbf{e}^{(k)}\colon e_{ij}^{(k)}=\frac{\theta_{ij}^{(k)}}{\sum_{q}\theta_{iq}^{(k)}};$ 
5    Estimate the class priors:  $\hat{\pi}_{i}=\frac{\sum_{(o)}p_{i}^{(o)}}{|O|};$ 
6    Compute the class probability estimates for each object (o):  $p_{i}^{(o)}=\frac{\hat{\pi}_{i}\prod_{(k)\in K^{(o)}}\prod_{m}(e_{im}^{(k)})^{I(l_{(o)}^{(k)}=m)}}{\sum_{q}\hat{\pi}_{q}\prod_{(k)\in K^{(o)}}\prod_{m}(e_{qm}^{(k)})^{I(l_{(o)}^{(k)}=m)}};$ 
7 end
</div>

Algorithm 3 (Bayesian expectation maximization (EM) inference algorithm)

Input: The set of observed labels $L = \{ l _ { ( o ) } ^ { ( k ) } \} , \mathrm { p r i o r s } \lambda ^ { ( k ) }$ Output: Class probability estimates $\boldsymbol { \mathsf { p } } ^ { ( o ) }$ for each object <sup>(</sup>o<sup>)</sup>, confusion matrix $\mathbf { e } ^ { ( k ) }$ for each worker <sup>(</sup>k<sup>)</sup>, class prior estimates πˆ

1 Initialize class probability estimates for each object $( o ) \colon p _ { i } ^ { ( o ) } = \frac { \sum _ { ( k ) \in K ^ { ( o ) } } I ( l _ { ( o ) } ^ { ( k ) } = i ) } { | K ^ { ( o ) } | }$

E-step. The posterior probability of $t ^ { ( o ) }$ given $\{ \alpha ^ { ( k ) } \}$ and $\{ \beta ^ { ( o ) } \}$ is characterized by

$$
\begin{array}{l} p \left(t ^ {(o)} \mid L, \{\boldsymbol {\alpha} ^ {(k)} \}, \{\beta^ {(o)} \}\right) \\ = p \left(t ^ {(o)} \mid L ^ {(o)}, \{\boldsymbol {\alpha} ^ {(k)} \mid (k) \in K ^ {(o)} \}, \beta^ {(o)}\right) \\ \propto p \left(t ^ {(o)} \mid \{\boldsymbol {\alpha} ^ {(k)} \mid (k) \in K ^ {(o)} \}, \beta^ {(o)}\right) \\ \cdot p \left(L ^ {(o)} \mid t ^ {(o)}, \{\boldsymbol {\alpha} ^ {(k)} \mid (k) \in K ^ {(o)} \}, \beta^ {(o)}\right) \\ \text { since } l _ {(o)} ^ {(k)}, \text { s are conditionally independent } \\ \text { given } t ^ {(o)}, \{\boldsymbol {\alpha} ^ {(k)} \} \text { and } \beta^ {(o)} \\ \propto p \left(t ^ {(o)}\right) \prod_ {(k) \in K ^ {(o)}} p \left(l _ {(o)} ^ {(k)} \mid t ^ {(o)}, \alpha_ {t ^ {(o)}} ^ {(k)}, \beta^ {(o)}\right) \\ \propto p \left(t ^ {(o)}\right) \prod_ {(k) \in K ^ {(o)}} \left(\frac {1}{1 + e ^ {- \alpha_ {t ^ {(o)}} ^ {(k)} \beta^ {(o)}}}\right) ^ {I \left(l _ {(o)} ^ {(k)} = t ^ {(o)}\right)} \\ \cdot \left(\frac {1}{1 + e ^ {\alpha_ {t ^ {(o)}} ^ {(k)} \beta^ {(o)}}}\right) ^ {I \left(l _ {(o)} ^ {(k)} = 1 - t ^ {(o)}\right)}. \end{array} \tag {3}
$$

Following Equation (3), we can calculate the posterior probability of $t ^ { ( o ) }$ using the prior probability of $t ^ { ( o ) }$ , the values of $\{ \alpha ^ { ( k ) } | ( k ) \in \check { K } ^ { ( o ) } \} _ { . }$ , and the value of $\beta ^ { ( o ) }$ estimated from the previous M-step.

M-step. We maximize the auxiliary function $Q ,$ which is defined as the expectation of the joint log-likelihood of the observed and hidden variables $( L , \stackrel { \smile } { \left\{ \right\} t ^ { ( o ) } } )$ given the parameters $\big ( \{ \alpha ^ { ( k ) } \} , \{ \beta ^ { ( o ) } \} \big )$ <sup>)</sup>, where the values of hidden variables $\{ t ^ { ( o ) } \}$ are computed during the previous E-step. We can also impose a prior on each parameter. The prior probabilities of $\alpha _ { 0 } ^ { ( k ) } , \alpha _ { 1 } ^ { ( k ) }$ , and $\beta ^ { ( o ) }$ are denoted as $p \big ( \alpha _ { 0 } ^ { ( k ) } \big ) , \dot { p } ( \alpha _ { 1 } ^ { ( k ) } )$ , and $p ( { \boldsymbol { \beta } } ^ { ( o ) } )$ <sup>)</sup>, respectively

$$
\begin{array}{l} Q (\{\boldsymbol {\alpha} ^ {(k)} \}, \{\beta^ {(o)} \}) \\ = \mathbb {E} [ \ln (p (L, \{t ^ {(o)} \} \mid \{\boldsymbol {\alpha} ^ {(k)} \}, \{\beta^ {(o)} \}) p (\{\boldsymbol {\alpha} ^ {(k)} \}, \{\beta^ {(o)} \})) ] \\ = \mathbb {E} \bigg [ \ln \prod_ {(o)} (p (t ^ {(o)}) \prod_ {(k) \in K ^ {(o)}} p (l _ {(o)} ^ {(k)} \mid t ^ {(o)}, \alpha_ {t ^ {(o)}} ^ {(k)}, \beta^ {(o)})) \bigg ] \end{array}
$$

$$
\begin{array}{l} + \ln \prod_ {(k)} \prod_ {i = 0} ^ {1} p (\alpha_ {i} ^ {(k)}) + \ln \prod_ {(o)} p (\beta^ {(o)}) \\ = \sum_ {(o)} \mathbb {E} [ \ln p (t ^ {(o)}) ] + \sum_ {(o)} \sum_ {(k) \in K ^ {(o)}} \mathbb {E} [ \ln p (l _ {(o)} ^ {(k)} | t ^ {(o)}, \alpha_ {t ^ {(o)}} ^ {(k)}, \beta^ {(o)}) ] \\ + \sum_ {(k)} \sum_ {i = 0} ^ {1} \ln p (\alpha_ {i} ^ {(k)}) + \sum_ {(o)} \ln p (\beta^ {(o)}), \end{array} \tag {4}
$$

where the expectation is taken over $\{ t ^ { ( o ) } \}$ estimated during the previous E-step. The values of $\{ \alpha ^ { ( k ) } \}$ and $\{ \beta ^ { ( o ) } \}$ are obtained by maximizing the auxiliary function Q. This is not directly solvable, therefore we apply a gradient ascent approach to find parameter values that locally maximize Q. (The details of the gradient ascent approach are provided in Online Appendix B.)

We present a sketch of the inference process in Algorithm 4. Note that when we assume that all of the objects are equally dificult (i.e., ${ \beta ^ { ( o ) } = \beta }$ where $\beta$ is a constant), GLAD degenerates to EM with the following relationship: $e _ { i i } ^ { ( k ) } = 1 / ( 1 + e ^ { - \alpha _ { i } ^ { ( k ) } \beta } )$ and $e _ { i , 1 - i } ^ { ( k ) } =$ $1 / ( 1 + e ^ { \alpha _ { i } ^ { ( k ) } \beta } )$

4.5. Estimated and Actual Misclassification Cost In the four inference algorithms presented above, MV and MP return the estimated true class <sup>ˆ</sup>t<sup>(o)</sup> for each object <sup>(</sup>o<sup>)</sup>, while EM and GLAD return the class probability estimates $\boldsymbol { \mathsf { p } } ^ { ( o ) }$ for each object <sup>(</sup>o<sup>)</sup>. If the class probability estimates of the object are available, we can calculate the estimated misclassification cost as follows:

Proposition 1. Given the misclassification cost matrix c and the class probability estimates $\boldsymbol { \mathsf { p } } ^ { ( o ) }$ for object <sup>(</sup>o<sup>)</sup>, the estimated misclassification cost of object <sup>(</sup>o<sup>)</sup> is $\begin{array} { r } { E s t C o s t ( \mathbf { p } ^ { ( o ) } ) = \operatorname* { m i n } _ { j \in \{ 0 , 1 \} } \sum _ { i = 0 } ^ { 1 } p _ { i } ^ { ( o ) } c _ { i j } . } \end{array}$

The estimated misclassification cost if we report $j$ as the true class is equal to the posterior probability of the object <sup>(</sup>o<sup>)</sup> belonging to class i (namely, $p _ { i } ^ { ( o ) } )$ multiplied by the associated cost of classifying an object of class i into class j (namely, $c _ { i j } )$ , aggregated over all possible i’s. Clearly, the best decision is to report the class that incurs the minimum cost. Therefore, the reported class label for EM and GLAD is given by $\hat { t } ^ { ( o ) } =$ arg min $\begin{array} { r } { \operatorname { \varepsilon } _ { j \in \{ 0 , 1 \} } \sum _ { i = 0 } ^ { 1 } p _ { i } ^ { ( o ) } c _ { i j } } \end{array}$ . Note that unlike MV and MP, the object class label reported by EM and GLAD might vary depending on the misclassification cost matrix.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 4 (GLAD expectation maximization inference algorithm)

Input: The set of observed labels  $L = \{l_{(o)}^{(k)}\}$ , priors  $p(\alpha_{0}^{(k)})$ ,  $p(\alpha_{1}^{(k)})$ , and  $p(\beta^{(o)})$ 

Output: Class probability estimates  $\mathbf{p}^{(o)}$  for each object (o), easiness  $\hat{\beta}^{(o)}$  of each object (o), quality vector  $\hat{\alpha}^{(k)}$  for each worker (k), class prior estimates  $\hat{\pi}$ 

1 Initialize the easiness estimate for each object (o):  $\hat{\beta}^{(o)} = 1$ ;

2 Initialize class probability estimates for each object (o):  $p_{i}^{(o)} = \frac{\sum_{(k) \in K^{(o)}} I(l_{(o)}^{(k)} = i)}{|K^{(o)}|}$ ;

3 Estimate the class priors:  $\hat{\pi}_{i} = \frac{\sum_{(o)} p_{i}^{(o)}}{|O|}$ ;

4 while not converged do

5 Obtain the estimated quality vector  $\hat{\alpha}^{(k)}$  for each worker (k) and the estimated easiness  $\hat{\beta}^{(o)}$  of each object (o) by maximizing the auxiliary function  $Q(\{\alpha^{(k)}\}, \{\beta^{(o)}\})$  in Equation (4) using gradient ascent approach;

6 Compute the class probability estimates for each object (o):

7  $p_{i}^{(o)} = \frac{\hat{\pi}_{i} \prod_{(k) \in K^{(o)}} (1/(1 + e^{-\hat{\alpha}_{i}^{(k)}}\hat{\beta}^{(o)}))^{I(l_{(o)}^{(k)}=i)} (1/(1 + e^{\hat{\alpha}_{i}^{(k)}}\hat{\beta}^{(o)}))^{I(l_{(o)}^{(k)}=1-i)}}{\sum_{q} \hat{\pi}_{q} \prod_{(k) \in K^{(o)}} (1/(1 + e^{-\hat{\alpha}_{q}^{(k)}}\hat{\beta}^{(o)}))^{I(l_{(o)}^{(k)}=q)} (1/(1 + e^{\hat{\alpha}_{q}^{(k)}}\hat{\beta}^{(o)}))^{I(l_{(o)}^{(k)}=1-q)}}$ ;

8 Estimate the class priors:  $\hat{\pi}_{i} = \frac{\sum_{(o)} p_{i}^{(o)}}{|O|}$ ;

9 end
</div>

If the true class of the object is known, we can also calculate the actual misclassification cost:

Proposition 2. Given the misclassification cost matrix $\mathbf { c } ,$ the true class label $t ^ { ( o ) }$ and the estimated class label <sup>ˆ</sup>t<sup>(o)</sup> for object <sup>(</sup>o<sup>)</sup>, the actual misclassification cost of object <sup>(</sup>o<sup>)</sup> is $A c t u a l C o s t ( \hat { t } ^ { ( o ) } ) = c _ { t ^ { ( o ) } \hat { t } ^ { ( o ) } }$

## 5. Dynamic Label Allocation

In the previous section, we focus on a static setting: given all of the labels provided by workers, we use several diferent approaches to infer object class and worker quality. In real crowdsourcing marketplaces, labels are often obtained incrementally and dynamically, therefore the <sup>(</sup>n <sup>+</sup> 1<sup>)</sup>th label allocation decision can be made based on the n labels collected so far. Intuitively, it is preferable for the employer to prioritize labels to objects that are more likely to achieve a greater reduction in misclassification cost. The challenge facing the employer is to devise a label allocation strategy that minimizes the number of labels required to achieve a certain level of data quality (measured by average misclassification cost), or equivalently, minimizes the average misclassification cost with a given number of labels.

To find the optimal allocation strategy, the employer needs to solve the following optimization problem:

$$
\underset {z} {\text { minimize }} \mathbb {E} _ {z} \left[ \sum_ {(o)} A c t u a l C o s t (\hat {t} ^ {(o)} | _ {N}) \right],\tag{5}
$$

where $\big | _ { N }$ denotes the estimates at the final step $N , \mathbb { E } _ { z }$ represents the expectation taken over the sample paths $\{ ( \bar { o } _ { 1 } ) , ( o _ { 2 } ) , \dots , ( o _ { N } ) \}$ generated by an allocation strategy z.

The optimization problem in (5) is a finite horizon multiarmed bandit (MAB) problem, where each object corresponds to an arm, while pulling an arm is equivalent to assigning the next label to a particular object. However, our problem is more challenging because the rewards can only be realized at the final step, when the average misclassification cost does not exceed a threshold, and so the intermediate rewards at each step are not deducible or distinguishable. This problem is computationally intractable, therefore, we resort to heuristic approaches to find approximate solutions.

Below, we propose several heuristic-based dynamic label allocation strategies with the aim of reducing the label resources required to achieve the desired data quality.

## 5.1. Message Passing-Reliability (MP-Reliab)

The first strategy is motivated by the MP algorithm in Section 4.2, which estimates the label for each object based on the sign of a weighted sum of the answers provided by workers. While the predicted label is binary (i.e., 0 or 1), the weighted sum is a real value. The further away the sum is from zero, the more reliable the prediction is. Therefore, it makes sense to allocate more labels to objects whose weighted sums, based on the existing labels, are closer to the decision threshold of zero.

To formalize this idea, we define the following heuristic function:

$$
h _ {M P - R e l i a b} ^ {(o)} = - \bigg | \sum_ {(k) \in K ^ {(o)}} (2 l _ {(o)} ^ {(k)} - 1) y _ {(k) \to (o)}) \bigg |.
$$

Here, all of the notations are from Section 4.2. The negative sign is introduced to get a larger function value when the deviation from zero is smaller.

## 5.2. Expectation Maximization-Cost (EM-Cost) and GLAD-Cost

One drawback of the MP-Reliab strategy is that it cannot incorporate the heterogeneous costs of diferent classification errors into the allocation decision. Fortunately, the EM and GLAD inference algorithms presented in Sections 4.3 and 4.4 are able to generate class probability estimates for all of the objects, which can then be utilized to help the employer make a more informed decision.

The estimated misclassification cost of the object is important to inform the allocation decision on which object to assign the next label to. Based on Proposition 1, the highest cost is incurred when two diferent label predictions yield the same misclassification cost $( \mathrm { i . e . , \ : \ : } \ : \dot { p _ { 0 } ^ { ( o ) } } c _ { 0 0 } + p _ { 1 } ^ { ( o ) } \dot { c } _ { 1 0 } = p _ { 0 } ^ { ( o ) } c _ { 0 1 } + p _ { 1 } ^ { ( o ) } c _ { 1 1 } )$ . When the estimated cost is high (i.e., the costs of two label predictions are similar), a small variation in class probability estimates can lead to totally diferent label predictions. On the other hand, when the estimated cost is low, the same variation might not cause any change in label prediction. Therefore, the average misclassification cost is more likely to be reduced when the additional labels are allocated to objects with higher estimated costs.

The heuristic functions based on this idea are

$$
\begin{array}{r} h _ {E M - C o s t} ^ {(o)} = E s t C o s t (\mathbf {p} _ {E M} ^ {(o)}) \mathrm{and} \\ h _ {G L A D - C o s t} ^ {(o)} = E s t C o s t (\mathbf {p} _ {G L A D} ^ {(o)}), \end{array}
$$

where $\mathbf { p } _ { E M } ^ { ( o ) }$ represents the class probability estimates for object <sup>(</sup>o<sup>)</sup> using the EM inference algorithm and $\mathfrak { p } _ { G L A D } ^ { ( o ) }$ are the class probability estimates for object <sup>(</sup>o<sup>)</sup> returned by the GLAD algorithm.

## 5.3. GLAD-Cost-Variation (GLAD-CostV)

One criticism of the two cost-based approaches is that labeling the object with the highest estimated misclassification cost does not necessarily lead to the greatest cost reduction. For example, a dificult object is more likely to have a high estimated cost; however, the cost reduction induced by an additional label may be marginal, as even a high-quality worker has a considerable chance of providing an incorrect label.

To remedy this deficiency, we want to incorporate the expected reduction in estimated misclassification cost induced by one additional label into the heuristic function. However, as shown in Proposition 3, the estimated misclassification cost of an object is very likely to stay the same in expectation.

Proposition 3. Assume that the easiness of an object <sup>(</sup>o<sup>)</sup> is $\beta ^ { ( o ) }$ and its class probability estimate is $\left. \mathbf { p } ^ { ( o ) } \right. _ { m }$ after querying m workers, and now there arrives a worker <sup>(</sup>k<sup>)</sup> with quality vector $\alpha ^ { ( k ) }$ . The estimated misclassification cost will stay the same in expectation if the predicted label does not change with the adding of the <sup>(</sup>m <sup>+</sup> 1<sup>)</sup>th label by worker <sup>(</sup>k<sup>)</sup>, i.e., $E s t C o s t ^ { ( o ) } | _ { m } = \breve { \mathbb { E } } ( \bar { E s t } C o s t ^ { ( o ) } | _ { ( m + 1 ) } )$

## Proof. See Online Appendix C.1.

In practice, the same predicted label condition in Proposition 3 can be easily met. When the predicted label of object <sup>(</sup>o<sup>)</sup> at step m is in agreement with the new label provided by worker <sup>(</sup>k<sup>)</sup>, the model predicts the same label at step <sup>(</sup>m <sup>+</sup> 1<sup>)</sup>; when the two labels conflict with each other, the predicted label at step $( m + 1 )$ still does not change as long as the model has more confidence in the collective label of the first m workers than in the label of the <sup>(</sup>m <sup>+</sup> 1<sup>)</sup>th worker. Therefore, we cannot use the expected reduction in estimated misclassification cost $\bar { E } s t C o s t ^ { ( o ) } | _ { m } - \mathbb { E } ( E s t C o s t ^ { ( o ) } | _ { ( m + 1 ) } )$ as the heuristic function to solve the optimization problem.

As an alternative, we propose a new approach that selects the next object to label based on the expected variation in estimated misclassification cost. The underlying intuition is that the addition of one more label leads to a higher cost variation for more uncertain objects. If the model is confident about the true class of a particular object, an additional label would result in little cost reduction when it agrees with the previous label prediction and little cost increment when it disagrees with the previous prediction. The heuristic function is

$$
\begin{array}{r l} & h _ {G L A D - C o s t V} ^ {(o)} = \mathbb {E} (| E s t C o s t ^ {(o)} | _ {m} - E s t C o s t ^ {(o)} | _ {(m + 1)} |) \\ & \quad = p (l _ {(o)} ^ {(k)} = 0) | E s t C o s t ^ {(o)} | _ {m} - E s t C o s t ^ {(o)} | _ {(m + 1)} ^ {0} | \\ & \qquad + p (l _ {(o)} ^ {(k)} = 1) | E s t C o s t ^ {(o)} | _ {m} - E s t C o s t ^ {(o)} | _ {(m + 1)} ^ {1} |, \end{array}
$$

where $E s t C o s t ^ { ( o ) } | _ { ( m + 1 ) } ^ { 0 }$ represents the estimated misclassification cost of the object when the additional label provided by the worker equals 0, and $E s t C o s t ^ { ( o ) } | _ { ( m + 1 ) } ^ { 1 }$ represents the estimated misclassification cost of the object with the additional label being 1.

Note that this cost variation approach cannot help when the inference algorithm employed is EM, which is due to the basic assumption of the EM model that the same worker has equal likelihood of making errors on all objects, regardless of the dificulty of each object.

Proposition 4. The expected variation in estimated misclassification cost of an object <sup>(</sup>o<sup>)</sup> under EM algorithm only depends on the class probability estimate $\bar { \boldsymbol { \mathsf { P } } } ^ { ( o ) } | _ { m } ^ { - } ,$ the confusion matrix $\mathbf { e } ^ { ( k ) }$ of the worker <sup>(</sup>k<sup>)</sup> who provides the next label, and the cost matrix c.

Proof. See Online Appendix C.2.

Based on Proposition $^ { 4 , }$ we can claim that under the EM algorithm, if two objects have the same class probability estimates (and thus the same estimated misclassification cost), assigning the next label to either of them will produce the same expected variation in estimated misclassification cost.

All four strategies proposed above prioritize labels based on diferent heuristics. We present a general framework for dynamic label allocation in Algorithm 5. Note that the inference algorithms used for deriving the values of heuristic functions can be diferent from the inference algorithms used for estimating misclassification cost. For instance, we may use MP-Reliab (which relies on MP to infer $h _ { M P - R e l i a b } ^ { ( o ) } )$ for allocating labels and use EM for estimating misclassification cost.

## 5.4. Batch Processing

Two minor points limit the applicability of the dynamic allocation strategies described above in real-world large data environments. First, at each time point, we need to compute the values of the heuristic functions for all of the objects and choose the one with the highest value, which is computationally expensive. Second, we tend to assign workers to objects of which we are less certain first; however, an accurate estimation of worker quality relies on good estimates of the labels for the objects that the worker has already worked on. This poses a disadvantage for the early coming workers since they need to wait a long time to get their quality correctly estimated. To alleviate the computational complexity and the latency in worker quality updates, we can divide the full set of objects into a number of subsets $N = \{ N _ { 1 } , N _ { 2 } , \dots , N _ { n } \}$ , where each $N _ { i }$ contains a relatively small number of objects.<sup>6</sup> We will start with the first subset $N _ { 1 }$ and move to $N _ { \gamma }$ when the average estimated misclassification cost of $N _ { 1 }$ is below the threshold $\tau _ { c } ,$ and so on. Note that as new labels arrive and the worker quality and object class probability estimates get updated, the estimated cost of previous batches might fail to meet the quality requirement. To overcome this problem, we allow labels to be allocated to previous batches when working on the current batch.

## 6. Simulation Experiments

To test the performance of the inference and label allocation strategies, we run a set of simulation experiments using synthetic data generated by the labeling model described in Section 3.2. Simulation experiments are a powerful tool for modeling complicated market environments and conducting analyses under various parameter values $( \mathrm { e . g . }$ , Chiang and Mookerjee 2004, Adomavicius et al. 2009, Ketter et al. 2012). We describe below the setting for the simulations.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 5 (A general framework for dynamic label allocation)

Input: The set of objects $O = \{(o)\}$ to be labeled, misclassification cost matrix $\mathbf{c}$, cost threshold $\tau_c$, heuristic function $h^{(o)} \in \{h_{MP\text{-Reliab}}^{(o)}, h_{EM\text{-Cost}}^{(o)}, h_{GLAD\text{-Cost}}^{(o)}, h_{GLAD\text{-CostV}}^{(o)}\}$, inference and cost estimation algorithm $\eta \in \{EM, GLAD\}$

Output: Predicted class label $\hat{t}^{(o)}$ for each object ($o$)

1 Initialize $L = \emptyset$, $O^{(k)} = \emptyset$ for each worker ($k$), $avg\_cost = \infty$;

2 while $avg\_cost &gt; \tau_c$ do

3 When a worker ($k$) is ready to accept the next task,

4 Select the next object to label according to ($o$) = $\arg \max_{(o') \in O \setminus O^{(k)}} h^{(o')}$;

5 Once worker ($k$) finishes the task,

6 Add the acquired label $l_{(o)}^{(k)}$ to the label set: $L = L \cup \{l_{(o)}^{(k)}\}$;

7 Add object ($o$) to the set of objects labeled by worker ($k$): $O^{(k)} = O^{(k)} \cup \{(o)\}$;

8 Using algorithm $\eta$, estimate the class probability estimates $\mathbf{p}^{(o)}$ for each object ($o$);

9 sum_cost = 0;

10 for ($o$) ∈ $O$ do

11 Calculate the predicted label $\hat{t}^{(o)}$ and the estimated misclassification cost $EstCost^{(o)}$:

12 $\hat{t}^{(o)} = \arg \min_{j \in \{0,1\}} \sum_{i=0}^{1} p_i^{(o)} c_{ij}$;

13 $EstCost^{(o)} = \min_{j \in \{0,1\}} \sum_{i=0}^{1} p_i^{(o)} c_{ij}$;

14 sum_cost = sum_cost + EstCost$^{(o)}$;

15 end

16 $avg\_cost = \frac{sum\_cost}{|O|}$

17 end
</div>

The simulation setup is as follows: We have 1,000 objects evenly assigned to two classes. The easiness of each object $\beta ^ { ( o ) }$ is obtained by exponentiating a draw from a normal distribution ${ \dot { \mathcal { N } } } ( 0 , 1 { \dot { ) } } .$ . There are 200 workers whose quality parameters $\{ \grave { \alpha } _ { 0 } ^ { ( k ) } \}$ and $\{ \alpha _ { 1 } ^ { ( k ) } \}$ are drawn from a normal distribution $\mathcal { N } ( 1 , 1 ) . ^ { 7 }$ The assigned labels $\{ l _ { ( o ) } ^ { ( k ) } \}$ are generated according to Equations (1) and (2). To test the performance of the algorithms under diferent cost settings, we employ two cost matrices: a symmetric cost matrix $\mathbf { c } ^ { ( a ) } = ( \hat { 0 } 1 ; 1 0 )$ and an asymmetric cost matrix $\mathbf { c } ^ { ( b ) } = ( 0 \ 1 \ ; \ 5 \ 0 ) . ^ { 8 }$ To smooth out variability between trials, the simulation is repeated 20 times and the results are averaged over all experimental runs.

## 6.1. Inference Algorithms in a Static System

We first look at a static system in which there is no adaptive decision making with respect to label allocation. Since there is no ex ante information, we generate an equal number of labels for all objects. Based on the collected labels, the estimated class label (for MV and MP) or class probability estimates (for EM and GLAD) of each object, and the quality measure of each worker are obtained using diferent inference algorithms presented in Section 4. We evaluate the performance of these algorithms from two aspects: object actual misclassification cost and worker quality estimation accuracy. Since inference algorithms are not the main focus of this paper, for the sake of space, we present and discuss the results in Online Appendix D. The comparisons yield the following conclusions: (1) EM and GLAD outperform MV and MP by a large margin in both object actual misclassification cost and worker quality estimation accuracy; (2) GLAD results in a lower object actual misclassification cost than EM when the cost matrix is asymmetric; and (3) GLAD achieves a higher worker quality estimation accuracy than EM when the object assignment to each worker is not uniform with respect to easiness. Therefore, we use GLAD as the inference algorithm when testing the efectiveness of diferent label allocation strategies.

## 6.2. Label Allocation Strategies in a Dynamic System

We now proceed to a dynamic system, which allows the employer to allocate labels adaptively based on the data obtained so far. To mimic the dynamic process of the crowdsourcing marketplace, we assume that<sup>9</sup> (1) assigning a label to an object requires one unit of time; (2) every 10 time units, a new worker comes to work on the available tasks; and (3) each worker stops working once she contributes 50 labels.

As a baseline comparison, we implement a generalized round-robin (GRR) strategy that always assigns the next label to the object with the fewest number of labels so that on average, each object would receive an equal number of labels. We also include the current state-of-the-art adaptive allocation strategy called new label uncertainty (NLU), presented by Ipeirotis et al. (2014), which assigns the next label to the object with the highest label uncertainty score, defined based on the posterior probability estimates of object class after obtaining a certain number of positive and negative labels. We test the performance of the four adaptive label allocation strategies (i.e., MP-Reliab, EM-Cost, GLAD-Cost, and GLAD-CostV) proposed in Section 5 against GRR and NLU. To ensure a fair comparison, we use GLAD as the inference algorithm for all of the above-mentioned label allocation strategies.

Figure 2(a) reports the efectiveness of diferent allocation strategies under symmetric cost matrix $\mathbf { c } ^ { ( a ) }$ , measured by the average actual misclassification cost of the objects. All four strategies proposed in this paper show superior performance over GRR and NLU, with an improvement rate of 15%–35% when the average number of labels allocated per object is 10. Among the four proposed strategies, EM-Cost achieves the best results overall; MP-Reliab performs poorly initially but catches up as more labels are collected; and GLAD-CostV beats GLAD-Cost by a small margin. The simulation results under asymmetric cost matrix $\mathbf { c } ^ { ( b ) }$ are shown in Figure 2(b). NLU performs the worst, followed by GRR, MP-Reliab, and GLAD-Cost, which produce similar results; GLAD-CostV has a clear advantage over GLAD-Cost; EM-Cost outperforms all of the other strategies by a significant margin (25%–45%).

The fact that EM-Cost outperforms GLAD-CostV is somewhat surprising, as we expect that allocating labels based on the expected variation of estimated cost will help to make better use of labeling resources. To explore the underlying mechanism driving these results, we check the performance of GLAD-Cost-β<sup>∗</sup> and GLAD-CostV-β<sup>∗</sup>, which are basically the same as GLAD-Cost and GLAD-CostV, but assuming that the true easiness $\beta ^ { ( o ) }$ of each object <sup>(</sup>o<sup>)</sup> is known. The following is clear from Figures 2(a) and 2(b): (1) GLAD-Cost-β performs very poorly, especially when the average number of labels allocated per object is large. This is probably because of the fact that GLAD-Cost-β<sup>∗</sup> tends to allocate excessive labels to a small number of dificult objects that are more likely to have very high estimated misclassification costs. (2) GLAD-CostV-β performs much better than GLAD-Cost-β , confirming our intuition that cost variation is a good metric to use. However, GLAD-CostV-β only provides a marginal performance improvement over EM-Cost.

To see how labels are allocated among diferent objects, we introduce the Gini coeficient, which measures

Figure 2. (Color online) Average Actual Misclassification Cost as a Function of the Average Number of Labels Acquired per Object for Diferent Allocation Algorithms in a Dynamic System

![](/api/attachments/MYWW5GR9/fulltext/images/203d8737185b0f3aaf04b7b15ff43016c3f750c1e68cffd00a5d42770b17ba5b.jpg)

![](/api/attachments/MYWW5GR9/fulltext/images/8b401f85d98340996f0d640029ea2ba24034ec9ca60940dc814001a8b6a449ad.jpg)

<table><tr><td>GRR</td><td>GLAD-Cost</td></tr><tr><td>NLU</td><td>GLAD-CostV</td></tr><tr><td>MP-Reliab</td><td>GLAD-Cost- $\beta^{*}$ </td></tr><tr><td>EM-Cost</td><td>GLAD-CostV- $\beta^{*}$ </td></tr></table>

the inequality of number of labels’ distribution among objects. The Gini coeficient ranges from a minimum value of zero, when all objects receive an equal number of labels, to a maximum value of one, when one object gets all of the labels. The higher the Gini coeficient, the greater the degree of inequality in the distribution of labels across objects. We plot the Gini coeficients for diferent allocation strategies in Figures 3(a) and 3(b). As expected, GRR has a near-zero Gini coeficient since it aims to equalize the number of labels assigned to each object. The Gini coeficient for GLAD-Cost-β is very high, approaching 0.7 when the average number of labels allocated per object is 10. By taking into consideration the magnitude of cost variation, GLAD-CostV-β<sup>∗</sup> is able to achieve a lower degree of inequality in label distribution. The Gini coeficients of GLAD-Cost and GLAD-CostV lie between the coeficients of GLAD-Cost-β and GLAD-CostV-β because of the imprecise estimates of object easiness. Notably, EM-Cost is associated with a moderate degree of inequality, which also stabilizes as the average number of labels allocated per object increases.

Figure 3. (Color online) Gini Coeficient for Number of Labels’ Distribution Among Objects as a Function of the Average Number of Labels Acquired per Object for Diferent Allocation Algorithms in a Dynamic System  
(a) Symmetric cost matrix c<sup>(a)</sup>  
![](/api/attachments/MYWW5GR9/fulltext/images/cc014971f2d4299eb92840475ec908b0d40b8d6dcbe04260497f33de368a9e24.jpg)

(b) Asymmetric cost matrix c<sup>(b)</sup>  
![](/api/attachments/MYWW5GR9/fulltext/images/bf1c6b63f9e299009597a13232c40eea3f010e9b25a2c217bc46259cef28ca0d.jpg)

<table><tr><td>GRR</td><td>GLAD-Cost</td></tr><tr><td>NLU</td><td>GLAD-CostV</td></tr><tr><td>MP-Reliab</td><td>GLAD-Cost- $\beta^{*}$ </td></tr><tr><td>EM-Cost</td><td>GLAD-CostV- $\beta^{*}$ </td></tr></table>

Why does EM-Cost not sufer the same problem as GLAD-Cost and GLAD-Cost-β ? We turn to the basic assumption underlying the EM algorithm, that is, workers’ error rates do not change when labeling objects of varying degrees of easiness. The consequence is that EM is likely to produce overconfident (or extreme) class probability estimates for dificult objects (see Online Appendix E for an explanation). Therefore, the estimated misclassification cost of a dificult object under EM is likely to be lower than what is obtained using GLAD. As an object accrues many labels, its estimated misclassification cost under EM becomes very low, so the chance of this object being allocated with the next label is greatly reduced. The overconfident estimates act like a penalty function to prevent EM-Cost from overinvesting labels in a few dificult objects and make it a pragmatic and efective strategy for allocating limited labels in a dynamic system.

## 7. Experiments on Real-World Crowdsourced Data Sets

One drawback of using simulation is that the underlying label generation model is artificial, which is unlikely to hold in real-world settings. For example, the generation of labels may not follow a specific model; the errors workers make might be correlated. For further evaluation, we test the performance of the proposed approaches on three publicly available data sets obtained using AMT. The first bluebird data set is collected by Welinder et al. (2010), in which workers are asked whether the presented image contains Indigo Bunting or Blue Grosbeak. The second rte data set and the third temp data set are both natural language processing data sets collected by Snow et al. (2008): rte represents the recognizing textual entailment task, where workers are presented with two sentences and given a binary choice of whether the second hypothesis sentence can be inferred from the first; temp represents the event temporal annotation task, where workers are presented with a dialogue and a pair of verb events from the dialogue, and asked whether the event described by the first verb occurs before or after the second. Table 2 summarizes these three data sets.

All three data sets in Table 2 are collected in a static way, regardless of the labels acquired at each intermediate step. At the end of the data collection, all of the objects receive the same number of labels. To simulate the dynamic label acquisition, we acquire labels in the following way:<sup>10</sup> At each step, we first pick a worker from the set of workers who still have labels, with the probability of being picked proportional to the number of available labels per worker; then, we choose the next object to label based on the dynamic allocation strategies proposed in Section 5, with the constraint that the object must have been labeled by the chosen worker; next, we put the assigned label to the observed label set, and remove it from the label pool available for drawing. We consider two cost settings $\mathbf { c } ^ { ( a ) }$ and $\mathbf { c } ^ { ( b ) }$ and average the results over 20 experimental runs.

Table 2. Description of the Three Real-World Data Sets

<table><tr><td>Data set</td><td>No. of objects(positive/negative)</td><td>No. ofworkers</td><td>No. of labelsper object</td><td>Mean/Medianno. of labelsper worker</td></tr><tr><td>bluebird</td><td>108 (60/48)</td><td>39</td><td>39</td><td>108/108</td></tr><tr><td>rte</td><td>800 (400/400)</td><td>164</td><td>10</td><td>49/20</td></tr><tr><td>temp</td><td>462 (259/203)</td><td>76</td><td>10</td><td>61/16</td></tr></table>

## 7.1. Inference Algorithms

We first evaluate the performance of diferent inference algorithms in a scenario where all objects receive an equal number of labels. The experimental results are shown in Figure F1 in the online appendix, which confirm the superior performance of EM and GLAD. MP performs the worst on all three data sets and shows little to no improvement as more labels are allocated to each object. This is probably because of the fact that the regular graph assumption<sup>11</sup> of MP is violated in real-world settings where there exists both productive workers who tend to submit a large number of labels and unproductive workers who provide only a few labels. GLAD achieves similar results as EM does when the cost matrix is symmetric and slightly outperforms EM when the cost matrix is asymmetric. Therefore, we stick to GLAD as the inference algorithm for testing diferent allocation strategies.

## 7.2. Dynamic Label Allocation Strategies

Figure 4 reports the performance of diferent allocation strategies on real-world data sets, using GLAD as the inference algorithm. Clearly, EM-Cost, GLAD-Cost, and GLAD-CostV perform consistently better than GRR, NLU, and MP-Reliab across all six combinations of data sets and cost settings. Diferent from what is observed on synthetic data, MP-Reliab does not even approach the performance of GRR on two of the data sets (i.e., rte and temp). This is because for both data sets, the number of objects labeled by each worker varies significantly: For rte, the number of labels contributed by each worker ranges from 20 to 800; and for temp, the range is between 10 and 462. In these scenarios, MP tends to excessively weigh the labels from productive workers and thus yield biased estimates for object classes. EM-Cost, GLAD-Cost, and GLAD-CostV achieve similar performance in all cases except in Figure 4(b), where EM-Cost outperforms the other two strategies by a significant margin.

Note that the performance of the allocation strategies difers at first but converges as more labels are allocated to objects. This is because no matter what

Figure 4. (Color online) Average Actual Misclassification Cost for Diferent Allocation Algorithms on Real-World Data Sets

(a) bluebird data set, symmetric cost $\pmb { \mathfrak { c } } ^ { ( a ) }$  
![](/api/attachments/MYWW5GR9/fulltext/images/57a3790da12ddaf9906970df09163be6cba9c6ff8d3be8b1e1e7b19e490c1c58.jpg)

(b) bluebird data set, asymmetric cost $\pmb { \mathsf { c } } ^ { ( b ) }$  
![](/api/attachments/MYWW5GR9/fulltext/images/ffcd2111854fc96d14d2760ab4f952156f7d4287601d68ab3d251f423ab426ed.jpg)

(c) rte data set, symmetric cost $\pmb { c } ^ { ( a ) }$  
![](/api/attachments/MYWW5GR9/fulltext/images/310521cdb910e29d284cde6c08c5284e0275415ac34e8855a24bbadc47b88f08.jpg)

(d) rte data set, asymmetric cost $\pmb { \mathsf { c } } ^ { ( b ) }$  
![](/api/attachments/MYWW5GR9/fulltext/images/aaa10fc94b59c4a82f55b9615d59aa44530be212483fa3316dccd04c5d110294.jpg)

(e) temp data set, symmetric cost $\pmb { \mathfrak { c } } ^ { ( a ) }$  
![](/api/attachments/MYWW5GR9/fulltext/images/f37da2cec97f4d49fe13c05ae23382042afa53aa1fc7d1efef6bfac6c6711396.jpg)

allocation strategy is employed, the labels are drawn from the same pool. At the beginning, each strategy has considerable freedom of choice in allocating labels to objects; however, as more labels are allocated, some objects are running out of labels quickly, and the next label has to be allocated to others; and at the end of the process, all of the strategies get the same set of labels. Here, we report the performance improvement when the average number of labels allocated to each object is about one-third of the total labels available to mitigate the interference of limited labels on evaluation. On the bluebird data set, EM-Cost outperforms the baseline

(f) temp data set, asymmetric cost $\pmb { \mathsf { c } } ^ { ( b ) }$  
![](/api/attachments/MYWW5GR9/fulltext/images/c15dc6391e7d8b6128dc8aac5ff47afa9fd42699b271d279fbdf9b3dabdcc459.jpg)  
Average no. of labels allocated per object

GRR by 15% and NLU by 38% under $\mathbf { c } ^ { ( a ) } ,$ , and the improvement rates are 23% and 50% under $\mathbf { c } ^ { ( b ) }$ . On the rte data set, EM-Cost outperforms GRR by 25% and NLU by 23% under $\mathbf { c } ^ { ( a ) }$ , and the rates are 21% and 15% under $\mathbf { \check { c } } ^ { ( b ) }$ . On the temp data set, EM-Cost outperforms GRR by 27% and NLU by 31% under $\mathbf { c } ^ { ( a ) }$ , and the rates are 29% and 28% under $\dot { \mathbf { c } } ^ { ( b ) }$ . We conclude that on these real-world data sets, our proposed allocation strategy EM-Cost can bring down the labeling cost by 15%–50%, which can be directly translated into huge economic savings when the number of objects to be classified is large.

## 8. Generating Reliable Worker Performance Metrics

In Online Appendix D.2, we leverage the advantage of simulated data to check the accuracy of worker quality estimation by calculating the Spearman coeficient between workers’ true quality values and the estimated quality values using diferent inference algorithms. 12 The results show that both EM and GLAD achieve a fairly high level of accuracy and can be used as efective tools for evaluating worker quality. Unfortunately, neither the confusion matrix $\mathbf { e } ^ { ( k ) ^ { \ J } }$ returned by EM nor the quality vector $\hat { \alpha } ^ { ( k ) }$ returned by GLAD is a scalar, and therefore cannot be directly used to rank worker performance. Here, we introduce two scalar metrics of worker performance: one is based on the estimated misclassification cost of a worker’s label in single labeling (Section 8.2), and the other is based on the contributed value of a worker’s label in multiple labeling (Section 8.3).

## 8.1. EM-Equivalent Confusion Matrix for GLAD

The confusion matrix $\mathbf { e } ^ { ( k ) }$ produced by EM can fully reflect workers’ errors in classifying objects of diferent classes. GLAD is more complicated in the sense that workers’ errors not only depend on the quality vector $\hat { \alpha } ^ { ( k ) }$ but also on the easiness of the object being classified. Therefore, the first step we take is to convert the quality vector into a measure that is able to capture the worker’s overall classification errors independent of the specific object being labeled.

Based on Equation (1), the confusion matrix of a worker <sup>(</sup>k<sup>)</sup> on labeling a particular object <sup>(</sup>o<sup>)</sup> is $\hat { \boldsymbol { \xi } } ^ { ( \bar { k } , o ) } ,$ where

$$
\hat {\xi} _ {i i} ^ {(k, o)} = \frac {1}{1 + e ^ {- \hat {\alpha} _ {i} ^ {(k)} \hat {\beta} ^ {(o)}}} \quad \mathrm{and} \quad \hat {\xi} _ {i, 1 - i} ^ {(k, o)} = 1 - \hat {\xi} _ {i i} ^ {(k, o)}.
$$

The values in confusion matrix $\hat { \boldsymbol { \xi } } ^ { ( k , o ) }$ vary widely depending on the easiness of the object ${ \hat { \beta } } ^ { ( o ) }$ . If we simply take the average of $\bar { \boldsymbol { \xi } } ^ { ( k , \bar { o } ) }$ over all of the objects that worker <sup>(</sup>k<sup>)</sup> labels, we will overvalue a worker who labels disproportionately more easy objects and undervalue a worker who labels disproportionately more dificult objects. For a fair evaluation, we propose a measure $\bar { \boldsymbol { \xi } } ^ { ( k ) }$ , where

$$
\bar {\xi} _ {i i} ^ {(k)} = \frac {1}{1 + e ^ {- \hat {\alpha} _ {i} ^ {(k)} \bar {\beta}}} \quad \mathrm{and} \quad \bar {\xi} _ {i, 1 - i} ^ {(k)} = 1 - \bar {\xi} _ {i i} ^ {(k)}.
$$

Here, $\hat { \beta }$ represents the average easiness of the objects, which is defined as $\bar { \beta } = 1 / | O | \sum _ { ( o ) \in O } \hat { \beta } ^ { ( o ) }$ . The element values of confusion matrix $\bar { \boldsymbol { \xi } } ^ { ( k ) }$ do not depend on the specific objects assigned to worker <sup>(</sup>k<sup>)</sup> and thus can objectively evaluate worker performance. For ease of presentation, we use $\mathbf { e } ^ { ( k ) }$ to denote both $\mathbf { e } ^ { ( k ) }$ produced by EM and $\bar { \boldsymbol { \xi } } ^ { ( k ) }$ produced by GLAD.

## 8.2. Estimated Cost of a Worker in the Single-Label Case

A straightforward method for evaluating worker performance is to calculate the accuracy rate $( \mathrm { i . e . , }$ how often the worker submits a correct label) for each worker based on $\mathbf { e } ^ { ( k ) }$ . However, this approach may mistakenly reject workers whose labels are wrong but informative. Consider the following example:

Example 1. Two workers are working on the task of classifying websites into two groups: porn and notporn. Worker A is always incorrect, labeling all porn websites as notporn, and vice versa. Worker B is lazy and classifies all websites as porn. A simple analysis indicates that the accuracy rate of worker A is $0 \% ,$ while the accuracy rate of worker B is only 50%.<sup>13</sup> However, it is not dificult to see that worker $\boldsymbol { \dot { A ^ { \prime } } \mathrm { s } }$ errors are easily reversible, while worker B’s errors are irreversible.

Another drawback of using accuracy rate is that all types of classification errors are treated indiscriminately. However, in reality, some errors can be more costly than others. For the classification task in Example 1, labeling a porn website as notporn can lead to serious consequences, while labeling a notporn website as porn is less harmful.

Naturally, a question arises: Given the estimates of confusion matrix $\mathbf { e } ^ { ( k ) }$ for each worker <sup>(</sup>k<sup>)</sup>, how can we generate a reliable worker performance metric that can separate correctable errors from uncorrectable errors workers make and weigh diferent types of errors based on their cost magnitudes?

Each worker assigns a hard label to each object. Using the confusion matrix of this worker, we can transform this assigned label into a soft label $( \mathrm { i . e . , }$ , posterior estimate), which is the best possible probability estimate we have for the true class of the object. If the worker <sup>(</sup>k<sup>)</sup> assigns l as the label to an object, we can transform this hard assigned label into a posterior soft label vector $( \hat { \pi } _ { 0 } e _ { 0 l } ^ { ( k ) } , \hat { \pi } _ { 1 } e _ { 1 l } ^ { ( k ) } )$ , where $\hat { \pi } _ { 0 }$ and $\hat { \pi } _ { 1 }$ are the estimated class priors. Of course, the quantities above need to be normalized by dividing them with $\begin{array} { r } { \hat { \pi } _ { l } ^ { ( k ) } = \sum _ { i = 0 } ^ { 1 } \hat { \pi } _ { i } e _ { i l } ^ { ( k ) } } \end{array}$ , which denotes the estimated prior probability that worker <sup>(</sup>k<sup>)</sup> assigns a label l. The misclassification cost of this soft label can be estimated based on Proposition 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 6 (Calculating the estimated cost of each worker)

Input: Confusion matrix  $\mathbf{e}^{(k)}$ , misclassification cost matrix c, estimated class prior vector  $\hat{\pi}$ 

Output: Estimated cost  $EstCost^{(k)}$  of each worker (k)

1 foreach worker (k) do

2    $EstCost^{(k)} = 0$ ;

3    foreach hard label l do

4    Estimate the prior probability that worker (k) assigns label l:  $\hat{\pi}_{l}^{(k)} = \sum_{i=0}^{1} \hat{\pi}_{i} e_{il}^{(k)}$ ;

5    Compute the posterior soft label vector corresponding to hard label l:

6    $soft^{(k)}(l) = \left(\frac{\hat{\pi}_{0} e_{0l}^{(k)}}{\hat{\pi}_{l}^{(k)}}, \frac{\hat{\pi}_{1} e_{1l}^{(k)}}{\hat{\pi}_{l}^{(k)}}\right)$ ;

7    Using Proposition 1, compute  $EstCost(\text{soft}^{(k)}(l))$  for the soft label;

8    $EstCost^{(k)} + =EstCost(\text{soft}^{(k)}(l)) \cdot \hat{\pi}_{l}^{(k)}$ ;

9    end

10 end
</div>

Knowing how to compute the estimated prior probability that worker <sup>(</sup>k<sup>)</sup> assigns each hard label, and the estimated cost of the posterior soft label vector corresponding to the hard label, we can easily calculate the estimated cost of worker <sup>(</sup>k<sup>)</sup>. Algorithm 6 illustrates this process.

Example 2. Consider the estimated costs of worker A and worker B from the previous example. Assuming equal priors across classes, and $c _ { i j } = 1 { \mathrm { i f } } { \bar { i } } \neq j$ and $c _ { i j } = 0$ ${ \mathrm { i f ~ } } i = j .$ , we have the following: The cost of worker A is 0, as the soft labels are <sup>(</sup>0.0, 1.0<sup>)</sup> and <sup>(</sup>1.0, 0.0<sup>)</sup> when the hard labels provided by A are 0 and 1. For worker $B ,$ the cost is 0.5 (the maximum possible) as the soft label generated by B is always <sup>(</sup>0.5, 0.5<sup>)</sup>.

It turns out that workers with confusion matrices that generate posterior labels with probability mass concentrated into a single class (i.e., confident posterior labels) tend to have a low estimated cost. On the contrary, workers that generate posterior labels with probabilities widely spread across classes $( \mathrm { i . e . } $ , uncertain posterior labels) tend to have high misclassification costs. This performance metric based on estimated misclassification cost resolves quite a few issues of prior approaches that rely on agreement, which generate a significant number of rejections for workers whose labels are wrong but informative and workers whose errors do not incur a high cost. However, it only works in the single label case, where each object only receives one label. We next discuss how to evaluate the performance of a worker in a multiple-label setting.

## 8.3. Contributed Value of a Worker in the Multiple-Label Case

As mentioned in Section 3.1, the ultimate objective of the employer is to get all objects labeled with average misclassification cost not exceeding the threshold $\tau _ { c } .$ For ease of exposition, we define a worker as a qualified worker if her estimated cost is below $\tau _ { c } ;$ otherwise, the worker is considered an unqualified worker. Since the data quality requirement is usually high, many workers in crowdsourcing markets fall into the category of unqualified workers. In fact, there might be cases where no worker satisfies the desired quality. Simply considering these workers as having no value and disregarding their labels is shortsighted and renders the problem intractable. Although each individual worker does not necessarily submit high-quality labels, a group of them as a whole may be able to achieve the requirements. A substantial number of papers in the literature (e.g., Sheng et al. 2008, Snow et al. 2008, Welinder et al. 2010, Raykar et al. 2010, Ipeirotis et al. 2010, Bachrach et al. 2012) have shown that multiple low-quality workers can work in tandem to generate results of high quality. The focus of this section is to derive the value of such unqualified workers, according to the level of redundancy required to reach the required quality standards.

Example 3. Suppose an employer has a binary classification problem with equal class priors, misclassification cost set to 1, and a quality requirement that the average misclassification cost is below 0.1. The employer gains \$1 value for each classified object meeting the required quality level. If we have workers with a confusion matrix of

$$
\mathbf {e} = \left( \begin{array}{c c} q & 1 - q \\ 1 - q & q \end{array} \right),
$$

how many workers do we need to assign to each object to achieve the quality objective? Figure 5 shows the relationship between the number of workers and the integrated estimated cost with the value of $q$ ranging from 0.60 to 0.90 at an interval of 0.05. The black dashed line indicates the required cost level. We can see the following:

Figure 5. (Color online) The Relationship Between the Number of Workers and Integrated Estimated Cost  
![](/api/attachments/MYWW5GR9/fulltext/images/6ba6f23dedef2af31285822dfb4a16d8f7e782c781368e20a6b2dde809ad7baa.jpg)

1. A worker with $q = 0 . 9 0$ is a qualified worker and is worth \$1 to the employer.

2. A worker with $q = 0 . 8 0$ is unqualified. However, a set of three workers with $q = 0 . 8 0$ generate labeling of required quality. Therefore, a worker with $q = 0 . 8 0$ is worth \$0.33.

3. A worker with $q = 0 . 7 0$ is unqualified. We need nine workers with $q = 0 . 7 0$ to reach the required quality, therefore, a worker with $q = 0 . 7 0$ is worth \$0.11.

Therefore, the contributed value of a worker is inversely proportional to the number of workers with the same confusion matrix required to achieve the acceptable quality level. Next, we show the process for estimating the value of a worker with an arbitrary confusion matrix e.

Definition 1. The value v<sup>(</sup>e<sup>)</sup> of a worker with confusion matrix e is $v ( \mathbf { e } ) = V / d ( \mathbf { e } )$ , where $d ( \mathbf { e } )$ is the number of workers with confusion matrix e required to reach the target average misclassification cost $\tau _ { c } ,$ and V is the value that the employer can gain from a unit of object with an acceptable cost level. For qualified workers $d ( \mathbf { e } ) = 1$ , while for unqualified workers $d ( \mathbf { e } ) > 1$

Now the key challenge is to estimate the value d<sup>(</sup>e<sup>)</sup> for an arbitrary confusion matrix e. For this, we need to estimate the number of workers with identical confusion matrix e required to generate labeling of acceptable quality. Assume that we have m workers with identical confusion matrix e who assign labels to an object. This generates a label assignment l $= \{ l _ { 1 } , \ldots , l _ { m } \} _ { }$ where $l _ { i }$ denotes the label assigned by the ith worker. Because of the exchangeability of the labels, it can be represented as a count of all class labels $\mathbf { n } = \{ n _ { 0 } , m -$ $n _ { 0 } \}$ . When the true class label is i (which occurs with probability $\textstyle { \hat { \pi } } _ { i } ) $ , this label assignment happens with probability $\begin{array} { r } { f ( n _ { 0 } ; m , e _ { i 0 } ) = \binom { m } { n \circ } ( \check { e _ { i 0 } } ) ^ { n _ { 0 } } ( 1 - e _ { i 0 } ) ^ { \hat { m } - n _ { 0 } } } \end{array}$ , which is the probability mass function (pmf) of the binomial distribution with parameters m (number of trials) and $e _ { i 0 }$ (success probability in each trial). Integrating this over both classes, the overall probability of seeing n is

$$
p (\mathbf {n}) = \sum_ {i = 0} ^ {1} \hat {\pi} _ {i} f (n _ {0}; m, e _ {i 0}) = \binom {m} {n _ {0}} \hat {\pi} _ {i} (e _ {i 0}) ^ {n _ {0}} (1 - e _ {i 0}) ^ {m - n _ {0}}.\tag{6}
$$

For each label assignment $\boldsymbol { \mathbf { n } } = \{ n _ { 0 } , m - n _ { 0 } \}$ , the soft label is given by

$$
\left(\frac {\hat {\pi} _ {0} \left(e _ {0 0}\right) ^ {n _ {0}} \left(1 - e _ {0 0}\right) ^ {m - n _ {0}}}{\sum_ {i = 0} ^ {1} \hat {\pi} _ {i} \left(e _ {i 0}\right) ^ {n _ {0}} \left(1 - e _ {i 0}\right) ^ {m - n _ {0}}}, \frac {\hat {\pi} _ {1} \left(e _ {1 0}\right) ^ {n _ {0}} \left(1 - e _ {1 0}\right) ^ {m - n _ {0}}}{\sum_ {i = 0} ^ {1} \hat {\pi} _ {i} \left(e _ {i 0}\right) ^ {n _ {0}} \left(1 - e _ {i 0}\right) ^ {m - n _ {0}}}\right).\tag{7}
$$

The estimated misclassification cost associated with the label assignment n is then calculated using Proposition 1. By repeating the process across all possible label assignments and weighing the cost of each one by its occurrence probability, we get the average misclassification cost of using m workers with confusion matrix e. Knowing how to compute the integrated estimated cost, the value derivation becomes quite easy. Given a worker with specific confusion matrix e, we simply find the minimum number of workers $d ( \mathbf { e } )$ needed to achieve the required cost level.

Unfortunately, except for very simple cases, there is no closed form solution to this problem, and the computational complexity increases exponentially with the value of $d ( \mathbf { e } )$ . In addition, the $d ( \mathbf { e } )$ generated above is likely to be an overestimate, as we force each label assignment to have an equal number of labels. As illustrated in Sections 6 and $^ { 7 , }$ selective label acquisition can potentially reduce the amount of labels required to achieve the target quality level. Therefore, we resort to a Monte Carlo approach for estimating $d ( \mathbf { e } )$ , where labels are drawn incrementally and prioritized to objects with high estimated misclassification costs, allowing some types of label assignments to have more labels than others. Algorithm 7 illustrates the overall process.<sup>14</sup> Note that the worker values v<sup>(</sup>e<sup>)</sup> can be computed beforehand and stored in a twodimensional matrix.<sup>15</sup> The number of elements in the matrix determines the degree of accuracy. For example, if we round $e _ { 0 0 }$ and $e _ { 1 1 }$ to one decimal place, the number of elements is $1 1 \times 1 1 = 1 2 1$ ; if we round $e _ { 0 0 }$ and $e _ { 1 1 }$ to two decimal places, the number of elements is $1 0 1 \times 1 0 1 = 1 0 , 2 0 1$

To see how the contributed value metric difers from the naïve accuracy rate metric, we present workers’ performance based on accuracy rate (x-axis) and contributed value (y-axis) in Figure $^ { 6 , }$ estimated from the three real-world data sets in Section 7. Each blue dot

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 7 (Estimating the value $v(\mathbf{e})$ of a worker with confusion matrix $\mathbf{e}$)
Input: Confusion matrix $\mathbf{e}$, misclassification cost matrix $\mathbf{c}$, estimated class prior vector $\hat{\pi}$, unit price for qualified objects $V$, sample size $N$, maximum number of workers $D$
Output: Value $v(\mathbf{e})$
1 for $x = 1$ to $N$ do
2 Generate object $x$ with the true class drawn from prior vector $\hat{\pi}$;
3 Using Proposition 1, compute EstCost(x) based on prior probability vector $\hat{\pi}$;
4 end
5 cnt = 0;
6 while cnt ≤ D · N do
7 Pick the object $y$ with the highest estimated cost (i.e., EstCost(y) ≥ EstCost(x), ∀x);
8 Draw one label for object $y$, following confusion matrix $\mathbf{e}$;
9 cnt = cnt + 1;
10 Using Equation (7), compute the posterior probability vector $\mathbf{p}(y)$ for object $y$;
11 Using Proposition 1, compute EstCost(y) for the posterior probability vector $\mathbf{p}(y)$;
12 sum_cost = 0;
13 for $x = 1$ to $N$ do
14 sum_cost = sum_cost + EstCost(x);
15 end
16 avg_cost = $\frac{\text{sum\_cost}}{N}$;
17 if avg_cost ≤ τc then
18 break;
19 end
20 end
21 if cnt ≤ D · N then
22 d(e) = $\frac{cnt}{N}$; v(e) = $\frac{V}{d(\mathbf{e})}$;
23 else
24 v(e) = 0;
25 end
</div>

represents a worker. For easier comparison, we normalize both measures by the sum of values of all workers so that the two measures are on the same scale. We also draw a red diagonal line with x and y having the same value. As shown in the figure, there is a notable discrepancy between the accuracy rate measure and the contributed value measure. Overall, using accuracy rate as a performance measure tends to overestimate the contribution of low-quality workers and underestimate the contribution of high-quality workers.

As a leading player in micro-crowdsourcing markets, AMT has implemented operations such as Grant-Bonus<sup>16</sup> and BlockWorker<sup>17</sup> to supplement its piece rate compensation system. We believe that the contributed value measure developed in this paper, which represents the monetary value that the employer can derive from each label of a worker, can be used as a basis for employers to grant bonuses to good workers and block low-value workers from further participation. For example, a simple way to utilize this measure is to ofer a base payment for all workers and block those workers whose contributed value is below the base payment. A more advanced usage is to pay a bonus on top of the piece rate based on the performance of workers.<sup>18</sup> Figure F2 in the online appendix illustrates what the bonus payment interface looks like to workers. Workers are shown their current bonus levels throughout their participation, and they can move the cursor around to know the bonus amounts associated with other performance levels. The granularity of the performance measure can be adjusted to suit workers’ comprehension level.

Figure 6. (Color online) Scatter Plots of Worker’s Accuracy Rate (Normalized by Sum) vs. Worker’s Contributed Value (Normalized by Sum) on Real-World Data Sets  
![](/api/attachments/MYWW5GR9/fulltext/images/d8822a27d2b1945a27fc465ac99f6ee213e4d1fd5a020904e89946d5c2399edc.jpg)

![](/api/attachments/MYWW5GR9/fulltext/images/14b8c84ee3119aa903c81bba3dc8d204c4d2f20acd478d293a6a3752f3a35ed4.jpg)

![](/api/attachments/MYWW5GR9/fulltext/images/c82d33ced33578ce0cb0719f485fc849422cc91f36bd316ea5f45b39c0712e3e.jpg)

To get a preliminary idea of how a quality-sensitive payment scheme works, we conducted the following experiment in a live production system, where workers were asked to take a look at online discussion forums, and decide whether the question discussed in the forum can be used as an assessment question in an exam.<sup>19</sup> The workers were automatically hired using an API from the oDesk labor platform. In the control condition, all workers were paid the same, but when a worker’s performance dropped below a particular threshold (which is set to 80%), her contract would be terminated. In the experimental treatment, workers were paid under quality-based pricing (QBP) and received compensation proportional to the value they were adding to the system.<sup>20</sup> A total of 120 workers participated in the experiment and were randomly assigned to either the treatment or control condition.

The results indicated a significant improvement of QBP, not only in terms of cost reduction but also in terms of worker retention. The cost for completing the tasks at the same level of quality was 50% to 70% lower in the QBP condition compared to the control. Furthermore, the lifetime of the workers in the QBP condition was 1.5 to 3 times longer when measured by the number of completed tasks; in other words, the churn rate in the control condition was significantly higher. The high churn is undesirable both from a human management perspective and from a data gathering and statistics perspective: for many workers in the control condition, the collected data were insuficient to allow for accurate inferences about their quality, which in turn led to the need to collect more data to compensate for this uncertainty. We believe that the results of this experiment highlight the potential for QBP, not only as a cost-saving scheme but also as a means to improve worker retention.

Although the results are encouraging, we acknowledge that determining the optimal amount of bonus to ofer to each worker is a complex problem that may depend on a number of factors, including reservation wages and risk preferences of workers, the type of microtasks (skill- or efort-based), the demand-supply balance of crowdsourced workers, the motivation component of workers (intrinsic or extrinsic), etc. Nevertheless, our proposed contributed value metric can tell the employer approximately how much monetary value she can derive from the labels provided by workers and make a step further toward the development of more fair and eficient compensation systems.

## 9. Conclusions and Discussion

Crowd labeling has rapidly become a commonly used tool for companies and researchers to acquire a huge number of cheap labels. However, such nonexpert labels are often noisy and unreliable, and employers need to rely on redundancy to achieve a desired level of quality, which significantly increases the total labeling expense. Therefore, devising cost-efective label acquisition strategies and establishing reliable worker performance metrics are of substantial interest to decision makers.

The contribution of this paper is twofold: First, we formulate a dynamic decision system in which label allocation and inference occur simultaneously, and propose several adaptive label allocation strategies that prioritize labels on objects that are more likely to yield higher rewards for employers. We demonstrate the superior performance of the proposed strategies over alternative approaches via extensive experiments on both simulated and real-world data sets. Second, we introduce two novel metrics that can be used to objectively rank the performance of crowdsourced workers, both allowing employers to separate workers’ correctable errors from uncorrectable errors and incorporate unequal costs of diferent types of classification errors. In particular, the contributed value metric directly measures worker’s individual contribution in quality assurance through redundancy and provides a basis for employers to develop more fair and eficient compensation schemes. As illustrated further in Online Appendix A, our work may serve as a fundamental quality control block for a variety of tasks, ensuring that the outcome of crowdsourced production reaches the quality levels desired by employers.

Although we focus on binary labeling tasks in this paper, most of our adaptive label allocation strategies can be generalized to multiclass settings.<sup>21</sup> The EM-Cost strategy can be directly applied to multiclass settings by (1) representing the performance of each worker by a multidimensional confusion matrix; (2) obtaining the class probability estimates for each object using the EM inference algorithm; and (3) estimating the misclassification cost based on the class probability estimates and a multidimensional cost matrix specified by the employer. To generalize GLAD-Cost and GLAD-CostV to multiclass scenarios, we can use a multidimensional vector to represent worker quality and a numeric value to represent object easiness. In the GLAD inference algorithm, the logistic function that jointly incorporates the class-dependent quality of the worker and the easiness of the object only gives the probability of obtaining the correct label. We need to make some simplification (e.g., assuming labeling errors are equally distributed across classes other than the correct one) to obtain the probability distribution over incorrect classes,<sup>22</sup> and then calculate the misclassification cost and the cost variation. Furthermore, the two worker performance metrics—estimated cost metric and contributed value metric—introduced in this paper can be readily used in multiclass settings by following the same procedure as described in Algorithms 6 and 7.

## 9.1. Practical Implications

Despite the wide adoption of micro-crowdsourcing by various companies, quality assurance at minimal cost remains an issue yet to be explored. Many of today’s firms still operate on a static system in which a fixed number of labels are collected for each object first, and some aggregation method is then employed to infer the true classes of objects. However, the real-world crowd labeling system is inherently dynamic, which provides an opportunity for companies to allocate labels adaptively and eficiently so that the target data quality can be achieved at considerably less expense. As illustrated in previous experiments, compared with the nonadaptive scheme, our proposed label allocation strategies can reduce the labeling expense by 15%–50%. For big companies (e.g., Facebook, Twitter) that require tons of human labels on an everyday basis, the implementation of such adaptive schemes can help save millions of dollars in data acquisition costs.

Crowdsourcing also lowers the barrier-to-entry for workers and provides a great way to help unemployed and underemployed people. Since there is no interview stage and workers can join the workforce at will, employers often face a pool of heterogeneous workers. Our proposed worker performance metrics can reliably assess the performance of each worker and distinguish informative workers from those of little use. The approach of evaluating workers based on their contributed value toward a desired level of data quality can facilitate the implementation of a bonus-based compensation scheme to motivate crowdsourced workers to submit more high-quality work and foster the creation of a healthy, well-operating crowdsourcing marketplace.

## 9.2. Limitations and Future Work

This study has several limitations and opens up opportunities for further research. First, in our study, we assume that worker quality does not change over time.

However, for many types of tasks in practice, there might be either learning efects or tiredness efects, which may lead to possible fluctuations in the exhibited quality of workers. To account for this, we can apply a particle filtering method to track the changes in worker quality (Crisan and Doucet 2002, Donmez et al. 2010) and choose the size of window for aggregation appropriately (Aperjis and Johari 2010).

Second, in reality, sometimes the employer has access to past performance of workers on the same or similar tasks. Kokkodis and Ipeirotis (2015) show that worker reputation is transferable across categories and predictive of future performance. Knowledge of prior, intracategory or intercategory reputation of workers could potentially improve the estimation accuracy of worker quality, especially when the worker only submits very few labels. As demonstrated in Sections 4.3 and 4.4, EM and GLAD algorithms can either work independently or in tandem with the existence of a reputation system.

Third, the focus of this paper is to guarantee a certain level of labeling quality at as low a cost as possible. With the aid of advanced supervised learning techniques, companies can use a small set of labeled objects to build classification models to make predictions on the set of unlabeled objects. In this case, the optimization problem becomes how to achieve a desirable level of model predictive performance at minimum label acquisition cost. To solve this problem, we can adjust the dynamic label allocation strategies by taking into consideration the prediction uncertainty of objects and prioritize labels to objects that are likely to induce greater improvement in both data and model quality.

Fourth, we discuss the potential of our worker value metric in guiding the design of more efective compensation schemes and present some preliminary realworld experimental results to illustrate the benefits of quality-based pricing in reducing labeling cost and improving worker retention. However, since there are many factors at play, coming up with a specific compensation contract that can be used immediately by all employers to achieve optimal profits is extraordinarily dificult. For example, Ho et al. (2015) show that bonus payments only work when tasks are efort responsive. A comprehensive examination of how workers respond to diferent incentives requires extensive experimentation across a wide range of task settings and is thus beyond the scope of this paper.

Despite these limitations, we believe that our current work provides a solid foundation on which future work can build. The proposed dynamic label allocation strategies substantially reduce the labeling expenses incurred by employers and thus contribute to better and eficient utilization of crowd intelligence. Our value-based worker performance metric gives a fairly reasonable estimate of the contribution of individual workers in monetary terms and provides a reference for employers to ofer performance-contingent bonuses to motivate crowdsourced workers. Furthermore, our work can be used immediately by interested parties, allowing easier management of crowdsourced workers and therefore the development of more interesting applications, enabled by micro-crowdsourcing.

## Acknowledgments

The authors thank the senior editor, associate editor, and anonymous reviewers for their helpful comments and constructive suggestions.

## Endnotes

<sup>1</sup>https://www.mturk.com/.

<sup>2</sup>http://www.netflixprize.com/.

<sup>3</sup>http://www.innocentive.com/.

<sup>4</sup>By definition, $c _ { i j } = 0$ when i <sup></sup> j.

<sup>5</sup> The algorithm presented here is slightly diferent from the original one presented in Karger et al. (2011) since the possible label set is now <sup>{</sup>0, 1<sup>}</sup> instead of <sup>{−</sup>1, 1<sup>}</sup>.

<sup>6</sup> The number of objects within each batch is decided by the employer. Smaller batches save computation time at the cost of suboptimal label resource allocation.

<sup>7</sup> The specific parameter values are chosen to produce a similar level of label noise as in real-life scenarios. Our simulated data sets have an overall accuracy rate of 0.700, while the rates for the three realworld data sets bluebird, rte, and temp in Section 7 are 0.636, 0.729, and 0.734, respectively.

<sup>8</sup> We choose an asymmetric cost matrix $\mathbf { c } ^ { ( b ) } = ( 0 \ 1 \ ; \ 5 \ 0 )$ to allow for a considerable, but not extreme, cost variation in diferent types of classification errors.

<sup>9</sup> Our results are robust to diferent specifications of worker arrival rate and lifetime.

<sup>10</sup> Such experiments based on real-world data sets possess two desirable properties: (1) The label generation process is real and does not assume any specific labeling model, which addresses the concerns of using artificial data. (2) All of the diferent allocation strategies are using the same set of collected labels, allowing for a randomized controlled experiment that eliminates the influence of confounding factors across experimental runs. Chen et al. (2015) use a similar approach in their paper for studying budget allocation.

<sup>11</sup> In a regular graph, each worker contributes an equal number of labels, and each object receives an equal number of labels.

<sup>12</sup> The same procedure cannot be applied on real-world data sets since in practice, workers’ true quality values are always unknown.

<sup>13</sup> Assume, for simplicity, equal priors for the two classes.

<sup>14</sup> We use EM-Cost because of its outstanding performance on both simulated and real-world data sets. To save computation cost without sacrificing too much accuracy, we set D <sup></sup> 30 and N <sup></sup> 1,000 in the actual implementation.

<sup>15</sup> Since $e _ { 0 0 }$ and $e _ { 1 1 }$ fully determine e, we can use them as row- and column-index and put v<sup>(</sup>e<sup>)</sup> into the corresponding matrix element.

<sup>16</sup>http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ ApiReference\_GrantBonusOperation.html.

<sup>17</sup>http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ ApiReference\_BlockWorkerOperation.html.

<sup>18</sup> See Ho et al. (2015) for an example of using bonus payments to induce high-quality work.

<sup>19</sup> For more details about the system, please see Christoforaki and Ipeirotis (2014).

<sup>20</sup> For example, a worker who was 80% accurate, was paid one-third of the price ofered to a worker who was 90% accurate, as we need three workers with 80% accuracy to simulate a worker with 90% accuracy.

<sup>21</sup> The only exception is MP-Reliab strategy, which relies on an inherently binary inference algorithm MP to derive the value of the corresponding heuristic function.

<sup>22</sup> Such a simplification might sacrifice the accuracy, but the GLAD specification allows us to incorporate the heterogeneity of object easiness while still capturing workers’ diferential qualities in each class.

## References

Adomavicius G, Gupta A, Zhdanov D (2009) Designing intelligent software agents for auctions with limited information feedback. Inform. Systems Res. 20(4):507–526.

Aperjis C, Johari R (2010) Optimal windows for aggregating ratings in electronic marketplaces. Management Sci. 56(5):864–880.

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Bachrach Y, Graepel T, Minka T, Guiver J (2012) How to grade a test without knowing the answers—A Bayesian graphical model for adaptive crowdsourcing and aptitude testing. Proc. 29th Internat. Conf. Machine Learning (Omnipress, Madison, WI), 1183–1190.

Berger RL (1982) Multiparameter hypothesis testing and acceptance sampling. Technometrics 24(4):295–300.

Carpenter B (2008) Multilevel Bayesian models of categorical data annotation. https://lingpipe.files.wordpress.com/2008/ 11/carp-bayesian-multilevel-annotation.pdf.

Chen X, Lin Q, Zhou D (2015) Statistical decision making for optimal budget allocation in crowd labeling. J. Machine Learning Res. 16:1–46.

Chiang IR, Mookerjee VS (2004) A fault threshold policy to manage software development projects. Inform. Systems Res. 15(1):3–21.

Christoforaki M, Ipeirotis P (2014) STEP: A scalable testing and evaluation platform. Second AAAI Conf. Human Comput. Crowdsourcing (AAAI Press, Palo Alto, CA), 41–49.

Cohn D, Atlas L, Ladner R (1994) Improving generalization with active learning. Machine Learning 15(2):201–221.

Crisan D, Doucet A (2002) A survey of convergence results on particle filtering methods for practitioners. IEEE Trans. Signal Processing 50(3):736–746

Crocker L, Algina J (2006) Introduction to Classical and Modern Test Theory (Wadsworth, Belmont, CA).

Dawid AP, Skene AM (1979) Maximum likelihood estimation of observer error-rates using the EM algorithm. Appl. Statist. 28(1): 20–28.

DeMars C (2010) Item Response Theory (Oxford University Press, Oxford, UK).

Donmez P, Carbonell J, Schneider J (2010) A probabilistic framework to learn from multiple annotators with time-varying accuracy. Proc. 10th SIAM Internat. Conf. Data Mining (SDM) (SIAM, Philadelphia), 826–837.

Goes PB (2014) Editor’s comments: Design science research in top information systems journals. MIS Quart. 38(1):iii–viii.

Gregor S, Hevner AR (2013) Positioning and presenting design science research for maximum impact. MIS Quart. 37(2):337–356.

Hevner AR, March ST, Park J, Ram S (2004) Design science in information systems research. MIS Quart. 28(1):75–105.

Ho CJ, Slivkins A, Suri S, Vaughan JW (2015) Incentivizing high quality crowdwork. Proc. 24th Internat. Conf. World Wide Web (ACM, New York), 419–429.

Ipeirotis PG (2010) Analyzing the Amazon Mechanical Turk marketplace. XRDS: Crossroads, ACM Magazine Students 17(2):16–21.

Ipeirotis PG, Provost F, Wang J (2010) Quality management on Amazon Mechanical Turk. Proc. ACM SIGKDD Workshop on Human Comput. (ACM, New York), 64–67.

Ipeirotis PG, Provost F, Sheng VS, Wang J (2014) Repeated labeling using multiple noisy labelers. Data Mining Knowledge Discovery 28(2):402–441.

Karger DR, Oh S, Shah D (2011) Iterative learning for reliable crowdsourcing systems. Proc. 24th Internat. Neural Inform. Processing Systems (Curran Associates, Red Hook, NY), 1953–1961.

Ketter W, Collins J, Gini M, Gupta A, Schrater P (2012) Realtime tactical and strategic sales management for intelligent agents guided by economic regimes. Inform. Systems Res. 23(4): 1263–1283.

Kokkodis M, Ipeirotis PG (2015) Reputation transferability in online labor markets. Management Sci. 62(6):1687–1706.

Kuechler W, Vaishnavi V (2012) A framework for theory development in design science research: Multiple perspectives. J. Assoc. Inform. Systems 13(6):395–423.

Lewis DD, Gale WA (1994) A sequential algorithm for training text classifiers. Proc. 17th Annual Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (Springer, New York), 3–12.

Lizotte DJ, Madani O, Greiner R (2003) Budgeted learning of naive-Bayes classifiers. Proc. 19th Conf. Uncertainty Artificial Intelligence (Morgan Kaufmann, San Francisco), 378–385.

Malone TW, Laubacher R, Dellarocas C (2009) Harnessing crowds: Mapping the genome of collective intelligence. Working paper, Massachusetts Institute of Technology, Cambridge, http://ssrn .com/abstract=1381502.

March ST, Storey VC (2008) Design science in the information systems discipline: An introduction to the special issue on design science research. MIS Quart. 32(4):725–730.

Moore JC, Whinston AB (1986) A model of decision-making with sequential information-acquisition (part 1). Decision Support Systems 2(4):285–307.

Moore JC, Whinston AB (1987) A model of decision-making with sequential information-acquisition (part 2). Decision Support Systems 3(1):47–72.

Moreno A, Terwiesch C (2014) Doing business with strangers: Reputation in online service marketplaces. Inform. Systems Res. 25(4): 865–886.

Raykar VC, Yu S, Zhao LH, Valadez GH, Florin C, Bogoni L, Moy L (2010) Learning from crowds. J. Machine Learning Res. 11(April): 1297–1322.

Roy N, McCallum A (2001) Toward optimal active learning through sampling estimation of error reduction. Proc. 18th Internat. Conf. Machine Learning (Morgan Kaufmann, San Francisco), 441–448.

Saar-Tsechansky M, Provost F (2004) Active sampling for class probability estimation and ranking. Machine Learning 54(2):153–178.

Saar-Tsechansky M, Provost F (2007) Decision-centric active learning of binary-outcome models. Inform. Systems Res. 18(1):4–22.

Saar-Tsechansky M, Melville P, Provost F (2009) Active feature-value acquisition. Management Sci. 55(4):664–684.

Schilling EG (1982) Acceptance Sampling in Quality Control (CRC Press, Boca Raton, FL).

Sheng VS, Provost F, Ipeirotis PG (2008) Get another label? Improving data quality and data mining using multiple, noisy labelers. Proc. 14th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 614–622.

Snow R, O’Connor B, Jurafsky D, Ng AY (2008) Cheap and fast— But is it good? Evaluating non-expert annotations for natural language tasks. Proc. Conf. Empirical Methods Natural Language Processing (Association for Computational Linguistics, Stroudsburg, PA), 254–263.

Wais P, Lingamneni S, Cook D, Fennell J, Goldenberg B, Lubarov D, Marin D, Simons H (2010) Towards building a high-quality workforce with Mechanical Turk. Proc. NIPS Workshop Comput. Soc. Sci. Wisdom Crowds (Curran Associates, Red Hook, NY), 1–5.

Wang J, Ghose A, Ipeirotis P (2012) Bonus, disclosure, and choice: What motivates the creation of high-quality paid reviews? Proc. 33rd Internat. Conf. Inform. Systems (AIS, Atlanta).

Welinder P, Perona P (2010) Online crowdsourcing: Rating annotators and obtaining cost-efective labels. 2010 IEEE Comput. Soc. Conf. Comput. Vision Pattern Recognition-Workshops (IEEE, New York), 25–32.

Welinder P, Branson S, Belongie S, Perona P (2010) The multidimensional wisdom of crowds. Proc. 23rd Internat. Conf. Neural Inform. Processing Systems (Curran Associates, Red Hook, NY), 2424–2432.

Wetherill GB, Chiu WK (1975) A review of acceptance sampling schemes with emphasis on the economic aspect. Internat. Statist. Rev. 43(2):191–210.

Whitehill J, Ruvolo P, Wu T, Bergsma J, Movellan J (2009) Whose vote should count more: Optimal integration of labels from labelers of unknown expertise. Proc. 22nd Internat. Conf. Adv. Neural Inform. Processing Systems (Curran Associates, Red Hook, NY), 2035–2043.

Zheng Z, Padmanabhan B (2006) Selectively acquiring customer information: A new data acquisition problem and an active learning-based solution. Management Sci. 52(5):697–712.
