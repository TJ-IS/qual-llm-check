---
otero_id: 9082
otero_key: "6YP6MAU7"
title: "Harnessing the Power of the Cloud: Revenue, Fairness, and Cloud Neutrality"
authors: "Carlee Joe-Wong; Soumya Sen"
year: "2018"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2018.1481639"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Harnessing the Power of the Cloud: Revenue, Fairness, and Cloud Neutrality

Carlee Joe-Wong & Soumya Sen

To cite this article: Carlee Joe-Wong & Soumya Sen (2018) Harnessing the Power of the Cloud: Revenue, Fairness, and Cloud Neutrality, Journal of Management Information Systems, 35:3, 813-836, DOI: 10.1080/07421222.2018.1481639

To link to this article: https://doi.org/10.1080/07421222.2018.1481639

![](/api/attachments/6YP6MAU7/fulltext/images/1c48b6394f06c8fcd5374acbb678f47704e460508b5f1aee1c6811ff282163eb.jpg)

View supplementary material

![](/api/attachments/6YP6MAU7/fulltext/images/74b0b7910bc5779320d781667b6549baa73bccf2528cfd6a71143076ef58d997.jpg)

Published online: 26 Oct 2018.

![](/api/attachments/6YP6MAU7/fulltext/images/30e0e2cf7bc0f2dfc4a53040da3ced2db56365297daeda42d4904d8836b5b928.jpg)

Submit your article to this journal

![](/api/attachments/6YP6MAU7/fulltext/images/b2026cb8a71b5cd360ad0b886af7409393edfda9bf48de6d09b0e3fc38ce4248.jpg)

View Crossmark data

# Harnessing the Power of the Cloud: Revenue, Fairness, and Cloud Neutrality

CARLEE JOE-WONG AND SOUMYA SEN

CARLEE JOE-WONG (cjoewong@andrew.cmu.edu) is an assistant professor in Electrical and Computer Engineering at Carnegie Mellon University. She received her Ph.D. degree in applied and computational mathematics from Princeton University. Dr. Joe-Wong is broadly interested in optimizing networked systems, including applications of machine learning and pricing in wireless, energy, and transportation networks. She was previously Director of Advanced Research at DataMi, a startup she co-founded based on her research on mobile data pricing. She received the INFORMS ISS Design Science Award in 2014 and the Best Paper Award at IEEE INFOCOM 2012.

SOUMYA SEN (ssen@umn.edu; corresponding author) is an assistant professor of Information & Decision Sciences at the Carlson School of Management of the University of Minnesota. He received his PhD in Electrical & Systems Engineering from the University of Pennsylvania and did his postdoctoral research at the Princeton University. His research interests are in design and economics of information systems and user behavior, with applications in network pricing, resource allocation, and information security. He has published in several IEEE, ACM, and INFORMS journals and conferences, and won the IEEE INFOCOM Best Paper Award in 2012, INFORMS ISS Design Science Award in 2014, and a UMN Grant-in-Aid Award in 2014. Dr. Sen received several patents on his research. He edited a book “Smart Data Pricing” for J. Wiley & Sons. He also co-founded a startup, DataMi, which provides pricing solutions for several major telecom providers around the world.

ABSTRACT: Cloud computing is a transformational technology that reduces upfront infrastructure costs, democratizes access to computing and storage capacity, and helps businesses innovate and compete in the digital economy. However, the distribution of these significant social and economic benefits among the various stakeholders in the cloud ecosystem will critically depend on pricing and resource allocation decisions made by cloud providers. These decisions impact not only the provider revenue, but also the fairness of resources allocated among cloud users and the overall social welfare. Several unique features of cloud computing (e.g., the presence of multiple, nonfungible resources and heterogeneous users) make the interplay between these competing objectives hard to understand. To truly harness the power of cloud computing and to establish regulatory benchmarks, there is a need for frameworks that quantify how resource allocation and pricing choices affect different objectives. In this work, we introduce an analytical model that incorporates user utility, endogenous pricing, fairness among heterogeneous users, social welfare, and cloud provider revenue. We identify conditions under which there is a tradeoff between fairness and revenue, and quantify the extent of this tradeoff by formulating an optimization problem in which a cloud provider maximizes its revenue, subject to constraints on the desired level of fairness. Our work provides an initial step toward developing regulatory policies for cloud neutrality to ensure an equitable distribution of the transformative benefits of the cloud.

KEY WORDS AND PHRASES: Cloud computing, fairness, revenue distribution, social welfare, resource allocation, cloud neutrality, IT regulation.

## Introduction

Cloud computing provides a transformative way for businesses to access servers, store data, deploy new services, and scale up their resources on-demand. New network technologies like virtualization increasingly allow for better control and sharing of computational resources across multiple clients, resulting in a distinct trend toward the creation of large centralized datacenters that lies at the heart of cloud computing. Recent studies have found that businesses can realize an average of 22 percent savings due to cloud computing, with benefits of up to 48 percent in areas like innovation [12]; as many as 95 percent of digital businesses have taken advantage of these benefits and begun using public cloud computing facilities [50]. By reducing up-front provisioning costs and democratizing access to shared computing and storage facilities, cloud computing can significantly improve productivity in businesses and organizations, resulting in greater value for societies and economies.

Although cloud computing offers substantial benefits, the distribution of these benefits among the various stakeholders in the cloud ecosystem depends crucially on various operational decisions of cloud providers and, in particular, on how they price and allocate their available resources among their (likely heterogeneous) clients or users. This resource allocation decision may incorporate several possible considerations, such as: how can providers maximize their revenue? How can they ensure “fairness” in the benefits that the different clients receive? Allocating resources with such objectives is also complicated by the fact that clients can configure the resources of their virtual machines based on their jobs’ requirements, and the provider’s control over the resource allocation stems primarily from the prices that it charges per job<sup>1</sup> [2, 24]. This leads to another question: can a cloud provider use pricing to achieve fairness while maximizing its revenue?

Answering these questions in the cloud computing context is particularly nontrivial for four main reasons. First, the cloud is a multi-resource setting in which clients are heterogeneous in the ratios of different resources that they need to derive utility from completed jobs (e.g., some jobs may be compute-intensive, while others may be memory-intensive). Second, the resources required per job (e.g., CPU cycles, memory,

I/O bandwidth) are nonfungible, that is, a provider cannot flexibly compensate for a client’s deficit of one resource by providing more of another. Third, the resources that each job needs for completion must be consumed in bundles, that is, an a-la-carte combination of individual resources from different cloud vendors is typically infeasible (e.g., a computational job running on a provider’s virtual machine will use both CPU cycles and memory from that provider’s datacenter). Fourth, the notion of fairness is quite nebulous in multiresource contexts, and it is unclear how to incorporate it in resource allocation decisions. Clients’ requests for bundles of nonsubstitutable resources mean that “fairness” must account for the amount of each resource received by each client, as well as whether the allocated resources match each client’s requested bundle. These features are somewhat unique to the cloud in that they are rarely present simultaneously in flexible manufacturing settings. Additionally, a user is more likely to discover whether the resource provider is being fair or not with online performance measurement software than in traditional flexible manufacturing processes. In this work, we therefore aim to provide information systems (IS) researchers and practitioners with an analytical framework for structured explorations of revenue and fairness in cloud computing contexts.

This work primarily approaches the resource allocation problem from a cloud provider’s perspective based on two real-world motivations. First, evaluating the tradeoff between revenue and fairness is a natural consideration for many cloud providers. Although revenue maximization is usually thought of as providers’ primary objective, there is a business impetus for a cloud provider to be fair in how it allocates its resources among its clients (users) so as to prevent them from experiencing resource starvation. Such starvation can potentially have long-term consequences for the reputation and loss in business of the cloud provider. In our surveys with members of the technical staff at three large U.S. based cloud operators (enterprise, public, and government cloud operators), all of them identified fairness as an important metric to consider in cloud resource allocation. In the public IS sector, cloud providers may also need to account for regulatory interests in addition to their own [13].

Second, cloud providers are beginning to face calls for ensuring cloud neutrality [29, 34], mirroring the net neutrality debate around Internet resource allocation [9, 10, 21]. Cloud neutrality refers to the practice of ensuring free, robust competition among cloud providers, which, like the net neutrality debate, requires addressing various facets of possible discriminatory and unfair practices. These include ensuring that providers do not favor any single user [9, 14], clients are not locked into a specific provider through use of proprietary application programming interfaces (APIs) [15, 45] and that discretionary resources are allocated fairly among tenants in the same service level agreement (SLA) class [29]. Allowing clients this autonomy can lead to more innovation [38]. Just as no cloud provider should gain an unfair advantage by deploying proprietary APIs, no provider should be able to gain an advantage by favoring the jobs from some of its users while starving others. In our context, such neutrality can be realized in the form of regulatory policies that require a provider to also satisfy a constraint on the minimum level of utility for all clients, or some similar fairness criteria. These fairness policies can also lead to greater cloud adoption, as transitioning to cloud systems involves transition costs [17]. We take this perspective in setting up an optimization framework for the cloud provider in this work.

Incorporating “fairness” considerations presents its own challenges, namely that it is not obvious which fairness criterion should be used. Hence, we first survey the fairness literature by introducing some basic concepts related to resource allocation from the domain of welfare economics. At a fundamental level, any resource allocation problem is one in which a central decision-maker (e.g., a cloud operations manager or a regulator) decides on an assignment of utilities to different users from the set of feasible utilities.<sup>3</sup> When this assignment is done so as to maximize the sum of the utilities across all the users, it is known as a utilitarian or Benthamite<sup>4</sup> allocation. Mathematically, the utilitarian criterion tries to find a feasible allocation that maximizes $\sum _ { i } u _ { i } ,$ , where $u _ { i }$ is the utility derived by the i-th user. This is the commonly used notion of social welfare $\begin{array} { r } { ( W = \ \sum _ { i } u _ { i } ) } \end{array}$ in the economics literature. However, social welfare, as defined here from the perspective of utilitarianism, is often criticized for resulting in inequitable resource allocations [36, 41]: it is possible that a socially efficient outcome is achieved by giving most of the resources to a select few, while denying resources to others and causing them to suffer significantly. Additionally, a pricing or compensation mechanism may not exist to deal with the resulting inequity; for example, when a cloud provider allocates any discretionary resources (i.e., leftover resources after tenant SLAs have been met) [29].

To address inequity in resource allocation, welfare economists have introduced a family of social welfare functions, given by $\sum { _ i } \frac { u _ { i } ^ { 1 - \alpha } } { 1 - \alpha }$ , which is parameterized by a single <sup>-</sup>scalar α that captures the decision-maker’s aversion to inequity. This is also referred to as the α-fairness scheme [3]. Most well-known fairness measures can be generated from this family of functions by varying the value of $\alpha .$ For instance, when $\alpha = 0 ,$ the social welfare function becomes the previously discussed utilitarian objective $\textstyle { \bigl ( } \sum _ { i } u _ { i } { \bigr ) }$ , which lacks equity considerations [6, 20]. For $\alpha = 1$ , the α-fairness scheme corresponds to proportional fairness [8], in which the objective function becomes $\textstyle \sum _ { i } \log ( u _ { i } )$ Maximizing the proportional fairness is equivalent to maximizing the objective $\prod _ { i } u _ { i }$ in a Nash bargaining setting. Similarly, when $a \longrightarrow \infty ,$ , the scheme converges to Maximin fairness, that is, min<sub>i</sub> $u _ { i }$ is the measure of fairness [27, 35]. Maximin (max-min) fairness follows from Rawls’ theory<sup>5</sup> of justice [36], which advocates the allocation of resources in a way that maximizes the utility of the least well-off. Thus, a higher value of α in the α-fairness scheme will lead to a fairer overall allocation [26, 30, 43]. These functions thus parameterize the tradeoff between fairness and social welfare: by increasing α from 0 to $^ { \infty , }$ one can put more emphasis on fairness and less on social welfare.

Applying these fairness measures to a cloud setting is nontrivial. First, fairness can be measured on various metrics [26], for example, user utilities realized, number of jobs completed, share of the dominant resource, and so forth. In this work, we follow the traditional approach in welfare economics, as previously described, to consider fairness on user utilities;<sup>6</sup> although our framework can be easily extended to consider alternative metrics. Second, the notions of fairness and equity are necessarily subjective, and hence no allocation scheme can objectively claim to be the “best” or the most fair. In this work, we focus on maximin fairness because it is often viewed as the “most fair” allocation [1, 7], as previously discussed. This minimum utility requirement is also easier to enforce in practice by a regulator. We, therefore, adopt this fairness measure in our main model and explore the cloud provider’s revenue optimization problem under a maximin fairness constraint. Numerical evaluations are then used to demonstrate the robustness of the main results for other fairness criteria.

This paper makes four key contributions to the literature: first, we introduce a framework that endogenizes provider prices into resource allocation decisions and, thus, can be used to reason about revenue and fairness in a cloud context. Second, we use this framework to quantify the exact combinations of user resource requirements under which a tradeoff between fairness and revenue exists. We find that the existence of the tradeoff depends on the degree of symmetry or asymmetry in users resource requirements. Third, we provide an optimization formulation to quantify this fairness-revenue tradeoff for varying degrees of similarity in resource requirements of users. Lastly, this work provides initial insights into when regulatory intervention may be needed and how it can be implemented to ensure neutrality in the cloud.

This work is organized as follows: The second section provides an overview of the related research works and outlines our contributions to them. We then develop and analyze our model in the third section along with numerical evaluations of the model. We discuss our findings and conclude in the final section. Proofs of all results are in the Appendix.

## Literature Review

Our work draws upon several streams of research in welfare economics, computer science, and information systems, which we discuss next.

## Welfare Economics

Much of the literature in welfare economics uses microeconomic theory to evaluate how a central decision maker should allocate resources among different users, given a constraint set of achievable utility allocations known as the utility possibility set [38, 40]. A typical methodology to address the allocation problem involves the use of social welfare functions to rank feasible allocations of resources in terms of the social welfare they entail. Such functions typically include measures of both economic efficiency and equity. For example, a widely used class of social welfare functions is the α-fairness scheme, given by $\sum { i } \frac { u _ { i } ^ { 1 - \widetilde { \alpha } } } { 1 - \alpha }$ , which is parameterized by a <sup>-</sup>single parameter α that captures the decision maker’s aversion to inequity. Different values of α produce the most well-known realizations of social welfare functions, namely utilitarian α 0 , proportional (α 1), and maximin fairness α .

We draw upon these definitions of fairness in our model, and our analysis uses the maximin fairness criterion [1, 7]. The maximin criterion imposes a minimum utility guarantee for all users and will likely be easier to enforce in practice.

## Cloud Computing

Much of the research on cloud computing in the Computer Science and Information Systems literature has focused on the cloud architecture, service models [4], and their associated pricing challenges [33, 48]. In particular, researchers have studied two main models for the pricing of cloud services: Infrastructure-as-a-service (IaaS) [42, 47], in which raw resources such as central processing unit (CPU) or memory storage are sold to end users; and Software-as-a-Service (SaaS) [31], which provides a more integrated platform that includes the use of software systems (e.g., data management applications). This study focuses solely on IaaS scenarios, as offered by third-party public cloud providers such as Amazon’s EC2 [2] and Google’s Compute Engine [21].

Most works on IaaS pricing have focused on designing pricing strategies for a single resource scenario. For instance, [32] considers dynamic pricing of a single computing resource, subject to different customer budgets and service requirements (e.g., amount of computing time), while [54] considers a dynamic auction in which customers bid on resources in real time in order to complete their jobs, a format similar to Amazon’s spot pricing [2]. Reviews of various pricing schemes are reported in the literature [34, 39]. Other works (e.g., [16, 51]) have incorporated stochastic job arrivals and departures in their models of revenue-maximizing cloud providers. Wang et al. [49] consider pricing based on job completion times and also account for electricity costs in the provider’s optimization problem. All of these works largely deal with the operational aspects of cloud computing from the viewpoint of either a revenue-maximizing cloud provider or a utility-maximizing bidding agent. Additionally, their focus is often on job scheduling and demand management as a means to improve the cloud’s operational efficiency, as measured in terms of leftover capacity; thus, they take only the utilitarian perspective and have largely eschewed fairness considerations. In contrast, we account for the social welfare function to explore the impact of a cloud provider’s operational decisions (e.g., multiresource allocation) on the resulting fairness and revenue outcomes.

The notion of fairness has been primarily studied in the Internet and cloud computing literature in the context of single resource allocation [30]. For example, some research [5, 28, 43] considers the problem of “efficient” allocation of available link bandwidth to network flows to maximize throughput without attention to equitability of each individual flow. Even multiresource allocation problems, such as scheduling jobs in a datacenter, have been treated as a single resource problem (e.g., the Hadoop and Dryad schedulers [53]). Only recently has the Computer Science community started to systematically examine the unique challenges of defining and enforcing fairness in the cloud’s multiresource setting. For instance, some research [18, 19] generalized the max-min fairness measure to multiple resource settings by introducing the notion of dominant resource fairness, while another paper [26] introduced the notion of fairness on jobs. However, these works only model the supply-side of providers’ allocation decisions and focus on quantifying the fairness of a realized allocation under the capacity constraints for different types of resources. They do not model user utility and do not endogenize the cloud provider’s pricing decision. In contrast, our framework incorporates a demand-side model and also incorporates the traditional economic perspective of computing fairness on the user utilities.

Lastly, our work also contributes to the emerging literature on “cloud neutrality” [29, 37, 52]. Kesidis et al. [29, p. 1] advocate, “with the public cloud providers poised to become indispensable utility providers, neutrality-related mandates will likely emerge to ensure a level playing field among their customers (tenants).” These recent works have highlighted the need for enforcing fairness between affiliates of the cloud provider and its tenants (e.g., in how Amazon’s AWS resources are allocated between services such as Netflix and Amazon Prime, which both run on Amazon EC2). Similarly, cloud neutrality would require guarantees on how the cloud allocates any discretionary resources among tenants of the same SLA class. The framework we present in this work helps identify the conditions under which a tradeoff between fairness and revenue exists (as a function of the (a)symmetry in the ratios of resources required by the different clients) and, hence, can inform future policy decisions on when and how a regulator may need to intervene to ensure fairness in the cloud. This work thus complements and extends the recent research in the IS community on net neutrality issues [9, 22] to the cloud computing context.

## Tradeoff Analysis

As discussed earlier, the utilitarian objective maximizes efficiency but is neutral to fairness. A few recent works [6, 7, 26] have therefore undertaken worst-case analyses by comparing the value of the utilitarian objective achieved under some fair allocation to the value achieved by an allocation that maximizes the utilitarian objective (i.e., price of fairness). In a follow up work, Bertsimas et al. [7] quantify the tradeoff between efficiency and fairness when different users have different utility functions. Joe-Wong et al. [26] studied a similar tradeoff between fairness and efficiency, where the efficiency metric is quantified in terms of the leftover (unused) resource capacity after a fair allocation. Our model differs from these studies in three key ways. First, we incorporate a demand-side formulation and endogenize the provider’s pricing decision, which affects the achieved fairness. Second, we show that even if the users have the same utility function, but differ in the ratios of the different resources they need to derive utilities from completed jobs, a tradeoff between fairness and revenue can arise, even with endogenous pricing. Third, we derive conditions under which a tradeoff between fairness and revenue exists and solve for the cloud provider’s profit maximization objective under a fairness constraint. Thus, this work takes an initial step towards developing a holistic model to evaluate the outcomes in the cloud’s multi-resource allocation setting. In doing so, we also address the calls by Clemons et al. [11] and Tilson et al. [44] to put the study of digital infrastructures and their relationships to public policy at the core of the IS research agenda.

## Analysis

Proofs of all propositions and corollaries may be found in the Appendix. Proofs of the lemmas are given in our online technical report [25].

## Cloud Computing: A Multiresource Allocation Problem

Before introducing a formal analytical model, we first present a motivating toy example to evaluate the most basic question: Is there a tradeoff between revenue maximization and fairness in multiresource allocation?

Consider an example in which two users have jobs to run in the cloud. Each user $i = \{ 1 , 2 \}$ has a standard concave utility function, say $U _ { i } ( x _ { i } ) = \left( b x _ { i } - x _ { i } ^ { 2 } \right) - p _ { i } x _ { i } ,$ which captures user i’s utility from running $x _ { i }$ number of $\mathrm { j o b s } ^ { 8 }$ , where b is a fixed constant and $p _ { i }$ is the price per $\mathrm { j o b } ^ { 9 }$ for user i. Then, the user’s demand function that optimizes his/her utility will be $x _ { i } ^ { * } ( p _ { i } ) = ( b - { \ p } _ { i } ) / 2$ . We can thus find the revenue $p _ { 1 } x _ { 1 } ^ { * } + p _ { 2 } x _ { 2 } ^ { * }$ and maximin fairness<sup>10</sup> min $\left\{ U _ { 1 } \left( x _ { 1 } ^ { * } ( p _ { 1 } ) \right) \right.$ ; $U _ { 2 } \left( x _ { 2 } ^ { * } ( p _ { 2 } ) \right) \big \}$ achieved by the cloud provider for a given set of prices.

The cloud provider chooses these prices to satisfy the constraints on the capacity of resources available in the cloud. For numerical evaluation of the aforementioned setup, let us assume some real values for the parameters. First consider the case in which user 1 needs equal amounts of two resources, CPU cycles and memory, to complete each job, for example, (0.5, 0.5) units, and user 2 needs (0.9, 0.1) units of CPU and memory respectively to complete each (computationally intensive) job. Assume that all users configure their virtual machines (VMs) to consume the exact bundle of resources specified by their per-job resource requirements. Our CPU and memory resource constraints are then $0 . 5 ( b - p _ { 1 } ) / 2 + 0 . 9 ( b - p _ { 2 } ) / 2 \leq 1 , 0 . 5 ( b - p _ { 1 } ) / 2$ $+ 0 . 1 ( b - p _ { 2 } ) / 2 \le 1$ . For $b = 4 _ { : }$ , the revenue-maximizing prices are $( p _ { 1 } , p _ { 2 } ) = ( 2 . 3 7 7 4$ 2.6792), yielding a revenue of $p _ { 1 } x _ { 1 } ^ { * } + p _ { 2 } x _ { 2 } ^ { * } = 3 . 7$ and fairness of $m i n \big \{ U _ { 1 } \big ( x _ { 1 } ^ { * } ( p _ { 1 } ) \big )$ ; $U _ { 2 } \big ( x _ { 2 } ^ { * } ( p _ { 2 } ) \big ) \big \} = 0 . 4 3 6 1$ . Now consider if the provider had instead chosen a different set of prices, say $( p _ { 1 } , p _ { 2 } ) = ( 2 . 5 7 1 4 , 2 . 5 7 1 4 )$ ; in this case, the resulting revenue would drop only slightly to 3.67, but the fairness would increase to 0.5102, a 17 percent increase. Thus, the example demonstrates that there is a tradeoff between the achieved fairness and revenue that varies with the decisions taken by the cloud operator, and navigating this tradeoff carefully can help achieve greater fairness without significantly sacrificing revenue.

In the remainder of this section, we examine this fairness-revenue tradeoff in a general analytical framework. We first investigate the resource requirements under which a tradeoff arises (On Existence of the Fairness-Revenue Tradeoff section)

and then present a principled method for a cloud provider to navigate this tradeoff (Quantifying the Fairness-Revenue Tradeoff section).

## On Existence of the Fairness-Revenue Tradeoff

To find the exact conditions under which a tradeoff between fairness and revenue exists, we model two users<sup>11</sup> who wish to process jobs at a cloud provider. We develop a demand-side model in which users’ resource requirements for jobs are denoted by $( r _ { 1 1 } , \ r _ { 1 2 } )$ and $( r _ { 2 1 } , \ r _ { 2 2 } )$ , where $r _ { i j }$ is user i’s per-job requirement for resource j and $r _ { 1 1 } , r _ { 1 2 } , r _ { 2 1 } , r _ { 2 2 } > 0$ (i.e., each user needs some amount of each resource to complete a job). These resources are non-substitutable (e.g., CPU cycles and IO bandwidth) and users are heterogeneous in the ratios of the resources needed to complete their jobs (e.g., one type of job is CPU-intensive and another type can be IO-intensive). For example, MapReduce jobs that read large volumes of data from disk or from the network (e.g., sorting, indexing, grouping, data importing and exporting, data transformation) are IO-intensive. On the other hand, jobs that process data (e.g., clustering, complex text mining, natural-language processing, feature extraction, video encoding) are CPU-intensive. The price per job offered to the user i by the cloud provider is denoted by $p _ { i } .$ The utility $( V _ { i } )$ that user i receives depends on the number of jobs processed (x<sub>i</sub>), given the price per job $( p _ { i } )$ . We denote this utility with a generic isoelastic utility function<sup>12</sup> $\begin{array} { r } { V _ { i } = ~ \frac { c x _ { i } ^ { 1 - \gamma } } { 1 - \gamma } } \end{array}$ , where the parameter γ parameterizes the concavity of utility function (i.e., quantifying the degree of diminishing marginal utility) and $c > 0$ is a positive constant that scales the utility level relative to the cost. We assume that users are homogeneous in the shape (i.e., have the same $\gamma )$ of their utility functions.<sup>13</sup> Users choose the number of jobs that they process so as to maximize their surplus or net user utility, which is given by:

$$
U _ {i} = V _ {i} - p _ {i} x _ {i} = \frac {c x _ {i} ^ {1 - \gamma}}{1 - \gamma} - p _ {i} x _ {i}\tag{1}
$$

Users can be charged different prices because of their needs for different resource combinations to complete a job. We assume that users configure their virtual machines to consume bundles of resources that match their jobs’ resource requirements; users thus consume, and are charged based on, the number of jobs. They choose the number of jobs to process, $x _ { i } ,$ to maximize their utility functions (1), yielding the demand functions:

$$
x _ {i} = x ^ {*} (p _ {i}) = c ^ {\frac {1}{\gamma}} p _ {i} ^ {\frac {- 1}{\gamma}}, U ^ {*} (r _ {i}) = \frac {\gamma}{1 - \gamma} c ^ {\frac {1}{\gamma}} p _ {i} ^ {1 - \frac {1}{\gamma}}\tag{2}
$$

Without loss of generality, we normalize the units of each resource such that the provider has a capacity of 1, yielding the resource constraints:

$$
r _ {1 1} x ^ {*} (p _ {1}) + r _ {2 1} x ^ {*} (p _ {2}) \leq 1, r _ {1 2} x ^ {*} (p _ {1}) + r _ {2 2} x ^ {*} (p _ {2}) \leq 1\tag{3}
$$

We now consider how the prices $p _ { I } , \ p _ { 2 }$ are chosen. As previously discussed, a cloud provider and a regulator would likely have different objectives in choosing the prices: the provider would likely choose prices to maximize its revenue,<sup>14</sup> while a regulator would be more concerned with fairness. We denote the revenue and (maximin) fairness<sup>15</sup> measures as:

$$
R (p _ {1}, p _ {2}) = p _ {1} x ^ {*} (p _ {1}) + p _ {2} x ^ {*} (p _ {2}), F (p _ {1}, p _ {2}) = \min \{U ^ {*} (p _ {1}), U ^ {*} (p _ {2}) \}\tag{4}
$$

respectively, where $x ^ { * }$ and $U ^ { * }$ are given by Equation (2).

As an alternative to maximin fairness, we can also use the utilitarian criteria, that is, measuring the total benefits that the cloud provider and users jointly realize from a given set of resource prices. In this case, the social welfare<sup>16</sup> is given by:

$$
W (p _ {1}, p _ {2}) = U _ {1} ^ {*} (p _ {1}) + U _ {2} ^ {*} (p _ {2}) + R (p _ {1}, p _ {2}) = \frac {c ^ {\frac {1}{\gamma}}}{1 - \gamma} \left(p _ {1} ^ {1 - \frac {1}{\gamma}} + p _ {2} ^ {1 - \frac {1}{\gamma}}\right)\tag{5}
$$

Substituting the optimal demands $x ^ { * }$ from Equation (2) into the expressions for $W$ and R, we see that social welfare is a scalar multiple of cloud provider revenue, leading to the following lemma:

Lemma 1: For general isoelastic user utility functions defined in (1), $W ( p _ { 1 } , p _ { 2 } ) = R$ $( p _ { 1 } , p _ { 2 } ) / ( I - \alpha )$ . Thus, the prices $\left( p _ { 1 } ^ { * } , \ p _ { 2 } ^ { * } \right)$ at which the cloud provider can maximize its revenue R subject to the resource constraints (3) also maximize the (utilitarian) social welfare W subject to the same constraints.

Lemma 1 implies that there is no tradeoff between revenue and social welfare in this setting.<sup>17</sup> However, we may have a tradeoff between fairness and revenue; thus, the provider’s and the regulator’s objectives may not be aligned if the regulator uses fairness as a performance benchmark. We examine the circumstances of this fairness-revenue tradeoff in the discussion below.

We first identify conditions under which there is no tradeoff between maximizing revenue and maximin fairness, that is, there exists a set of prices $\left( p _ { I } , \ p _ { 2 } \right)$ that maximizes the provider’s revenue and the minimum utility across users. Without loss of generality, we assume the two resources are indexed (labeled) such that $r _ { I I } +$ $r _ { 2 I } \ge r _ { I 2 } + r _ { 2 2 }$ throughout this section. We then find conditions under which fairness is maximized:

Lemma 2: The prices $p _ { 1 } = p _ { 2 } = c ( r _ { 1 1 } + r _ { 2 1 } ) ^ { \alpha }$ are the unique maximizers of the fairness function F = min $\{ U ^ { * } ~ ( p _ { 1 } ) , ~ U ^ { * } ~ ( p _ { 2 } ) \}$ in (4), subject to the resource constraints (3).

Thus, at the fair solution, users are charged equal prices and can process equal numbers of jobs, resulting in equal utilities. Next, we find the necessary conditions for the cloud provider to maximize its revenue.

Lemma 3: Suppose that $p _ { 1 } , p _ { 2 }$ maximize the cloud provider’s revenue. Then,

$$
p _ {1} = \frac {\mu r _ {1 1} + v r _ {1 2}}{2}, p _ {2} = \frac {\mu r _ {2 1} + v r _ {2 2}}{2}\tag{6}
$$

for some $\mu , \nu \geq 0$ such that

$$
\left(r _ {1 1} x ^ {*} \left(\frac {\mu r _ {1 1} + v r _ {1 2}}{2}\right) + r _ {2 1} x ^ {*} \left(\frac {\mu r _ {2 1} + v r _ {2 2}}{2}\right)\right) = 1
$$

$$
\left(r _ {1 2} x ^ {*} \left(\frac {\mu r _ {1 1} + v r _ {1 2}}{2}\right) + r _ {2 2} x ^ {*} \left(\frac {\mu r _ {2 1} + v r _ {2 2}}{2}\right)\right) = 1\tag{7}
$$

We can now quantify when the fairness-revenue tradeoff arises by identifying conditions under which the fairness-maximizing prices of Lemma 2 do not satisfy the revenue- maximizing conditions of Lemma 3:

Proposition 1: There is a fairness-revenue tradeoff if $r _ { 1 1 } r _ { 2 2 } \neq r _ { 1 2 } r _ { 2 1 } , \ r _ { 1 1 } \neq r _ { 2 1 }$ ， and $r _ { 1 1 } + r _ { 2 1 } \neq r _ { 1 2 } + r _ { 2 2 }$ ; i.e., the revenue maximizing prices do not maximize fairness.

In general, for most combinations (ratios) of resource requirements, these conditions are likely to be satisfied; hence, there is usually a fairness-revenue tradeoff that needs to be considered. However, if the resource requirements of the users are sufficiently aligned such that any one of the conditions in Proposition 1 is not met, then this tradeoff will not arise. We therefore need to formally characterize this “alignment” of resource requirements for which a tradeoff does not exist. Proposition 1 shows that there are at least three different cases of this alignment to consider, namely $( r _ { 1 1 } r _ { 2 2 } = r _ { 1 2 } r _ { 2 1 } , r _ { 1 1 } = r _ { 2 1 }$ , and $r _ { 1 1 } + r _ { 2 1 } = r _ { 1 2 } + r _ { 2 2 } )$

Proposition 2: Suppose without loss of generality that $r _ { 1 1 } \geq r _ { 1 2 }$ (we can re-index the users to ensure that this constraint is satisfied). There is no fairness-revenue tradeoff if and only $i f r _ { 1 1 } = r _ { 2 1 } o r r _ { 1 1 } + r _ { 2 1 } = r _ { 1 2 } + r _ { 2 2 }$ and either $r _ { 1 1 } \ge r _ { 2 2 } \ge r _ { 1 2 }$ or $r _ { 2 2 } \ge r _ { 1 1 } \ge r _ { 1 2 }$

These conditions are usually satisfied in only a few specific cases, as $r _ { 1 1 } = r _ { 2 1 }$ and $r _ { I I } +$ $r _ { 2 I } = r _ { I 2 } + r _ { 2 2 }$ each eliminate one degree of freedom in choosing the four resource requirements. We can broadly categorize these two conditions as ensuring sufficient “symmetry” or “asymmetry” in the users’ resource requirements respectively, either of which can ensure that charging users equal prices (i.e., maximizing fairness) also maximizes provider revenue, thus eliminating the tradeoff. Formally, we define “perfectly symmetric” resource requirements as the case when both users have identical resource needs<sup>18</sup> $( \mathrm { i . e . , } \ r _ { 1 1 } = r _ { 2 1 } \ge r _ { 1 2 } = r _ { 2 2 } )$ , and “perfectly asymmetric” resource requirements as the case when user 1’s requirement for resource 1 equals user 2’s requirement for resource 2, and user 1’s requirement for resource 2 equals user 2’s requirements for resource 1 $( \mathrm { i . e . , } r _ { 1 1 } = r _ { 2 2 } > r _ { 1 2 } = r _ { 2 1 } \mathrm { o r } r _ { 1 1 } = r _ { 2 2 } < r _ { 1 2 } = r _ { 2 1 } )$

Proposition 2 shows that perfect symmetry and perfect asymmetry are sufficient, but not necessary, conditions for there to be no tradeoff between fairness and revenue. We can easily check that the conditions for perfect symmetry satisfy Proposition 2. However, if $r _ { 1 1 } = r _ { 2 1 } \ge r _ { 2 2 } > r _ { 1 2 }$ , i.e., both users have the same requirements for resource 1, which exceed their (unequal) requirements for resource 2, then there would still be no tradeoff between fairness and revenue. In this case, the users’ resource requirements are not perfectly symmetric, but are symmetric “enough” for there to be no fairness-revenue tradeoff.

Similarly, users with sufficiently asymmetric resource requirements would not experience any tradeoff between fairness and revenue. Perfectly asymmetric users, whose requirements can be written as $r _ { 1 1 } = r _ { 2 2 } = r , r _ { 1 2 } = r _ { 2 1 } = \beta r$ for some scalar $\beta$ $\geq 0 ,$ , satisfy the conditions $r _ { 1 1 } + r _ { 2 1 } = r _ { 1 2 } + r _ { 2 2 }$ and $r _ { 1 1 } \ge r _ { 2 2 } \ge r _ { 1 2 }$ in Proposition $2 ;$ thus, they do not have a tradeoff. However, Proposition 2 requires only the weaker condition that $r _ { 1 1 } + r _ { 2 1 } = r _ { 1 2 } + r _ { 2 2 }$ and $r _ { 1 1 } \ge r _ { 2 2 } \ge r _ { 1 2 }$ or $r _ { 2 2 } \ge r _ { 1 1 } \ge r _ { 1 2 }$ in order for there to be no tradeoff. These conditions ensure that user 1’s requirement for resource 1 dominates its requirement for resource 2, and vice versa for user 2, but are weaker than perfect asymmetry. For instance, we might assume $r _ { 1 1 } = 0 . 5$ $r _ { 2 2 } = 0 . 4 $ ; then $r _ { 1 2 } = 0 . 1$ and $r _ { 2 1 } = 0 . 2$ ensures that the resource requirements are sufficiently, though not perfectly, asymmetric for there to be no fairness-revenue tradeoff.

The aforementioned analysis shows that a fairness-revenue tradeoff usually does not arise when the ratios of the resource requirements of users are sufficiently symmetric or asymmetric (see exact conditions in Proposition 2). In such cases, there is little reason for regulatory intervention because the cloud provider’s profit maximization also maximizes the (maximin) fairness criteria. It is scenarios with other combination of resource requirements that may need a regulator to step in to require minimum fairness guarantees for all users.

## Quantifying the Fairness-Revenue Tradeoff

Given the scenarios under which a fairness-revenue tradeoff exists, we now examine the extent of this tradeoff. Such results are of particular interest to cloud regulators who might wish to ensure a certain level of fairness without unduly impacting the cloud provider’s revenue. For instance, the regulator may mandate that the achieved fairness exceed a given threshold $\phi ;$ cloud providers would then price their resources so as to maximize their revenue while satisfying this constraint. We can thus model the outcome of the cloud provider’s resource allocation as a solution to the optimization problem:

$$
\max _ {p _ {1}, p _ {2}} p _ {1} x ^ {*} (p _ {1}) + p _ {2} x ^ {*} (p _ {2})\tag{8}
$$

$$
s. t. \min \left\{U _ {1} ^ {*} (p _ {1}), U _ {2} ^ {*} (p _ {2}) \right\} \geq \phi
$$

$$
r _ {1 1} x _ {1} ^ {*} (p _ {1}) + r _ {2 1} x _ {2} ^ {*} (p _ {2}) \leq 1, r _ {1 2} x _ {1} ^ {*} (p _ {1}) + r _ {2 2} x _ {2} ^ {*} (p _ {2}) \leq 1
$$

The last two constraints represent the resource constraints, while the first constraint is the fairness constraint imposed by the regulator. The regulator then faces a question of how to choose the threshold $\phi .$ While a larger threshold will enforce a more fair allocation, choosing $\phi$ to be too large may significantly lower the cloud provider’s revenue; the regulator would likely wish to achieve a balance between these two quantities. In the following discussion, we quantify the dependence of the provider’s achieved revenue on the fairness threshold $\phi .$

In light of our findings that tradeoffs do not exist when users’ resource requirements are sufficiently symmetric or asymmetric, we consider an intermediate scenario in which user 1 has similar resource requirement $^ { 1 9 } \left( r _ { 1 1 } = r _ { 1 2 } = r / 2 \right)$ and user 2 has dissimilar requirements ${ } ^ { 2 0 } ( r _ { 2 1 } = \sigma r ; r _ { 2 2 } = ( I - \sigma ) r )$ . In this setting, the users’ resource requirements can never be perfectly asymmetric for $\theta < \sigma < I$ and can be symmetric only at $\sigma = 1 / 2$ . In other words, for all values of $\sigma \neq { \frac { 1 } { 2 } }$ , there will likely be a fairness-revenue tradeoff that our optimization approach can quantify. Without loss of generality, we suppose that $\sigma < 1 / 2$ . We first consider the threshold $\phi$ values for which the fairness constraint imposed by the regulator is tight at optimality (i.e., imposing the constraint affects the prices chosen by the cloud provider):

Lemma 4: The fairness constraint in (8) is not tight at optimality if

$$
\phi <   \frac {2 ^ {\frac {- (1 - \gamma) ^ {2}}{\gamma}} c \gamma}{(1 - \gamma) r ^ {1 - \gamma} \left((1 - \sigma) ^ {\frac {1}{\gamma}} + (1 - \sigma) 2 ^ {1 - \frac {1}{\gamma}}\right) ^ {1 - \gamma}}\tag{9}
$$

under which the optimal prices satisfying (8) are given by

$$
p _ {1} ^ {\frac {- 1}{\gamma}} = \frac {2 (1 - \sigma) ^ {\frac {1}{\gamma}}}{r c ^ {\frac {1}{\gamma}} \left((1 - \sigma) ^ {\frac {1}{\gamma}} + (1 - \sigma) 2 ^ {1 - \frac {1}{\gamma}}\right)}, p _ {2} ^ {\frac {- 1}{\gamma}} = \frac {2 ^ {1 - \frac {1}{\gamma}}}{r c ^ {\frac {1}{\gamma}} \left((1 - \sigma) ^ {\frac {1}{\gamma}} + (1 - \sigma) 2 ^ {1 - \frac {1}{\gamma}}\right)}\tag{10}
$$

Moreover, (8) is infeasible if

$$
\phi \geq \frac {2 ^ {1 - \gamma} c \gamma}{(1 - \gamma) r ^ {1 - \gamma} (3 - 2 \sigma) ^ {1 - \gamma}}\tag{11}
$$

Thus, the regulator would only choose thresholds $\phi$ between the bounds in Equations (9) and (11). Within these bounds, we can now find the achieved revenue as a function of $\dot { \varphi }$ by first observing that at the optimal prices that solve Equation (8), resource 1’s capacity constraint is tight: either resource 1’s or resource 2’s capacity constraint must be tight at optimality, and since we assume $\sigma \leq 1 / 2$ , resource ${ 2 \mathrm { { \dot { s } } } }$ constraint is always satisfied if resource 1’s capacity constraint is satisfied. We can thus write:

$$
x ^ {*} (p _ {1}) = \frac {2}{r} - 2 (1 - \sigma) x ^ {*} (p _ {2})\tag{12}
$$

due to resource 1’s capacity constraint being tight at optimality. This observation allows us to solve for the optimal prices:

Proposition 3: The optimal prices that solve (8) are given by

$$
p _ {1} ^ {\frac {- 1}{\gamma}} = \frac {2}{r c ^ {\frac {1}{\gamma}}} - 2 (1 - \sigma) \left(\frac {\phi (1 - \gamma)}{\gamma c ^ {\frac {1}{\gamma}}}\right) ^ {\frac {1}{1 - \gamma}}, p _ {2} ^ {\frac {- 1}{\gamma}} = \left(\frac {\phi (1 - \gamma)}{\gamma c ^ {\frac {1}{\gamma}}}\right) ^ {\frac {1}{1 - \gamma}}\tag{13}
$$

for ϕ satisfying the upper and lower bounds in Equations $( 9 )$ and (11). Moreover, at these optimal prices $p _ { 1 } \geq p _ { 2 }$ . At these prices, the cloud provider’s achieved revenue is given by:

$$
\frac {\phi (1 - \gamma)}{\gamma} + 2 ^ {1 - \gamma} c \left(\frac {1}{r} - c ^ {\frac {- 1}{1 - \gamma}} (1 - \sigma) \left(\frac {\phi (1 - \gamma)}{\gamma}\right) ^ {\frac {1}{1 - \gamma}}\right) ^ {1 - \gamma}\tag{14}
$$

We can see from Equation (13) that as $\phi$ increases $\mathfrak { p } _ { 2 } ^ { \frac { - 1 } { \gamma } }$ also increases, that is, the two prices have more similar values, as we would expect at a stricter fairness threshold. Moreover, the achieved revenue attains its maximum value at $\sigma = 1 / 2$ , that is, symmetric users: in this case, both users’ resource requirements align with the resource requirements, allowing users to process more jobs while still satisfying the resource constraints, and thus allowing the cloud provider to extract more revenue. We can further characterize the achieved optimal revenue as $\phi$ varies:

Corollary 1: The optimal revenue (Equation 14) decreases as $\phi$ increases. Moreover, the rate of decrease becomes more negative as $\phi$ increases $( i . e .$ (Equation 14) is a concave function of $\dot { } \phi \dot { } < \phi < \frac { } { }$ .

Thus, initially increasing $\phi$ from its minimum value has comparatively little effect on the achieved revenue. However, as $\phi$ increases, the consequent decrease in revenue becomes steeper. A regulator might then wish to limit the threshold $\phi$ so as to limit the effect on the cloud provider’s revenue: there is an especially large risk of unduly harming the provider’s revenue when $\phi$ is close to its maximum value, that is, a strict fairness threshold.

We finally consider the limits of this tradeoff, for which the fairness threshold $\phi$ takes its maximum and minimum values from Equation (9) and Equation (11). At these threshold values, the cloud provider would either maximize its revenue (for the minimum threshold $\phi )$ or maximize its fairness (for the maximum threshold $\phi )$ . We can then find the achieved fairness and revenue respectively at these two extremes:

Proposition 4: Let $( p _ { 1 } ^ { r } , ~ p _ { 2 } ^ { r } )$ denote the revenue-maximizing prices, and $( p _ { 1 } ^ { f } , p _ { 2 } ^ { f } )$ the fairness-maximizing prices. Then the ratios of the achieved fairness and revenue compared to their maximum values are respectively

$$
L _ {f} = \frac {\min \left\{U ^ {*} \left(p _ {1} ^ {r}\right) , U ^ {*} \left(p _ {2} ^ {r}\right) \right\}}{\min \left\{U ^ {*} \left(p _ {1} ^ {f}\right) , U ^ {*} \left(p _ {2} ^ {f}\right) \right\}} = \left(\frac {3 - 2 \sigma}{2 ^ {\frac {1}{\gamma}} (1 - \sigma) ^ {\frac {1}{\gamma}} + 2 - 2 \sigma}\right) ^ {1 - \gamma}\tag{15}
$$

$$
L _ {r} = \frac {p _ {1} ^ {f} x ^ {*} \left(p _ {1} ^ {f}\right) + p _ {2} ^ {f} x ^ {*} \left(p _ {2} ^ {f}\right)}{p _ {1} ^ {r} x ^ {*} \left(p _ {1} ^ {r}\right) + p _ {2} ^ {r} x ^ {*} \left(p _ {2} ^ {r}\right)} = 2 (3 - 2 \sigma) ^ {\gamma - 1} \left(1 + 2 ^ {1 - \frac {1}{\gamma}} (1 - \sigma) ^ {1 - \frac {1}{\gamma}}\right) ^ {- \gamma}\tag{16}
$$

Moreover, there is a larger reduction in fairness compared to revenue: $L _ { f } \leq L _ { r }$

By imposing the constraint that min $\{ U ^ { * } ( p _ { 1 } ) , ~ U ^ { * } ( p _ { 2 } ) \} \ge \phi$ on the cloud provider’s prices, the regulator can ensure that the ratio of achieved to maximum fairness is greater than $L _ { f } ,$ thus mitigating the loss in fairness due to the cloud provider’s attempt to maximize its revenue.

## Numerical Evaluations

In this section, we numerically illustrate the results from the previous sections regarding the fairness-revenue tradeoff for different configurations of resource requirements among users. Furthermore, we demonstrate the robustness of these results by showing that they remain qualitatively valid for a wide range of scenarios, such as resource allocation decisions with more than two users, choice of different fairness measures (e.g., proportional fairness), different values for the concavity parameter in the users’ isoelastic utility functions, and nonisoelastic utility functions (e.g., exponential utility).

We begin our evaluation with Proposition 2, which provides the conditions for the existence of a fairness-revenue tradeoff. In particular, it implies that when the resource requirements for the two users are either sufficiently “symmetric” or perfectly “asymmetric” (as defined in the section On Existence of the Fairness-Revenue Tradeoff), a significant tradeoff does not arise. But how does this tradeoff change as the resource requirements of the users deviate from the symmetric or asymmetric configurations? To study how the tradeoff evolves numerically, we choose two baseline resource configurations (symmetric in Figure 1(a) and asymmetric in Figure 1(b)) for which the tradeoff does not exist, and then perturb these resource requirements $r _ { i j }$ by adding independently drawn random noises from uniform distributions with different upper bounds. The resulting fairness-tradeoff plots for four different upper bounds (5 percent, 10 percent, 20 percent, and 30 percent over the baseline resource requirement values) are shown in Figure 1. As the percentage of the added noise increases, we observe larger deviations from the initial symmetric or asymmetric resource configuration. For all the numerical plots, we assume that the available capacities of the two resources are normalized to 1 and that the isoelasticity parameter in the users’ utility function is $\gamma = 0 . 3 3$ . The two axes in the plots are normalized with respect to the maximum achievable fairness and revenue values, given the realized resource requirements. When there is no noise (i.e., the configuration is perfectly symmetric or asymmetric), then the cloud provider will be able to maximize both fairness and revenue, that is, (1, 1) in the figure. As the noise level increases and the resource requirements deviate from the notradeoff conditions of Proposition 2, the fairness-revenue tradeoff curves move inwards, that is, the tradeoff grows more severe.

![](/api/attachments/6YP6MAU7/fulltext/images/89dc1741d08b08a811056800b22ac76f5916fed905bcb4aa35c6b7b0a6e947a8.jpg)  
(a) Symmetric requirements

![](/api/attachments/6YP6MAU7/fulltext/images/3b8973d76fd7fe35d5e9970534285eba4da00b572ede7f7ca806096cb4036d02.jpg)  
(b) Asymmetric requirements  
Figure 1. Emergence of (maximin) fairness-revenue tradeoffs when the user’s resource requirements deviate from the conditions of Proposition 2. We consider (a) a symmetric resource case with $r _ { 1 1 } = r _ { 1 2 } = r _ { 2 1 } = 0 . 5 , r _ { 2 2 } = 0 . 3 3$ and (b) an asymmetric case with $r _ { 1 1 } = 5 / 6 , r _ { 1 2 } = 1 / 3 , r _ { 2 1 } = 1 / 2 .$ $r _ { 2 2 } = 1$

Next, we extend the scenario in Figure 1 to study whether these tradeoffs also arise when there are more than two users. In Figure 2a, we consider perturbations from a scenario in which four users all have symmetric requirements for resource 1, which dominate their requirements for resource 2. As before, there is no fairness-revenue tradeoff with the symmetric requirements, but the tradeoff emerges as we increase the perturbations in resource requirements, thereby decreasing the symmetry in the resource requirements among the four users. We also observe that the tradeoff is more severe for revenue: the loss in fairness when revenue is maximized, $1 - L _ { f }$ exceeds the loss in revenue when fairness is maximized, $1 - L _ { r }$ . We also observe this in Figure 2b, which shows the fairness-revenue tradeoff with a baseline of asymmetric resource requirements. Since we have four instead of two users, the notion of perfect resource asymmetry does not easily extend, and so there is a small fairness-revenue tradeoff even without the perturbations. But as the perturbations increase, inducing greater variation in the ratios of the resource requirements among users, the tradeoff becomes more severe, as in the previous case. These results imply that there is a case to be made for a regulatory intervention to ensure that the social objective of fairness, not just the provider’s revenue, is accounted for in multiresource, multi-user settings.

![](/api/attachments/6YP6MAU7/fulltext/images/1b92b853bb283b2049bed0b8898b54fd1b3cb2aa5adf015d6f81ae6d8204a922.jpg)  
(a) Symmetric requirements

![](/api/attachments/6YP6MAU7/fulltext/images/9b63ade0e78815ad1cde6b96357c2d8f3f3fe8d83ddcbd292f7b592837567762.jpg)  
(b) Asymmetric requirements  
Figure 2. Fairness-revenue tradeoffs for 4 users and 2 resources when the user’s resource requirements deviate from symmetric and asymmetric resource requirements. We consider a symmetric resource case with $r _ { 1 1 } = r _ { 1 2 } = r _ { 2 1 } = r _ { 3 1 } = r _ { 4 1 } = 0 . 5 , r _ { 2 2 } = r _ { 3 2 } = r _ { 4 2 } = 0 . 3 3$ and (b) an asymmetric case with $r _ { 1 1 } = 5 / 6 , r _ { 1 2 } = 1 / 6 , r _ { 2 1 } = 1 / 2 , r _ { 2 2 } = 1 / 2 , r _ { 3 1 } = 2 / 3 , r _ { 3 2 } = 1 / 3 , r _ { 4 1 } = 1 / 3 . 0$ $r _ { 4 2 } = 1$

Next, we investigate the fairness-revenue tradeoffs arising from the optimization formulation of the section on Quantifying the Fairness-Revenue Tradeoff for two users and two resource cases under three different configurations of the resource requirements: two of them are of the form $( r _ { 1 1 } , r _ { 1 2 } , r _ { 2 1 } , r _ { 2 2 } ) = ( 0 . 5 , 0 . 5 , \sigma , 1 - \sigma )$ for $\sigma = 0 . 2$ and $\sigma = 0 . 4$ , and the third one is derived from the real workload trace of a Google datacenter [23]. For the datacenter trace data, we cluster the jobs according to their CPU and memory requirements and take the resource requirements for each cluster to lie at the cluster centroids to get: $r _ { 1 1 } = 0 . 6 8 , r _ { 1 2 } = 0 . 1 4 , r _ { 2 1 } = 0 . 3 2 , r _ { 2 2 } =$ 0.86. As expected from Proposition 3, we see in Figure 3a that the achieved revenue decreases as a higher fairness threshold is chosen to increase fairness. Moreover, as σ increases (indicating more symmetry in the two users’ resource requirements), the revenue-fairness tradeoff becomes less severe. We also validate the results in Proposition 4, showing that maximizing revenue leads to a greater reduction in fairness (up to 41% when $\sigma = 0 . 2 )$ than the reduction in revenue due to maximizing fairness $( < 6 \% )$ . We also note that the requirements from the Google trace lead to a less extreme decrease in fairness when revenue is maximized, but a larger decrease in revenue as the fairness constraint grows tighter. Both of our analytical results, however, still hold: the achieved revenue decreases for a high fairness threshold, and the reduction in fairness from maximizing revenue (15%) is larger than the reduction in revenue from maximizing fairness (9%).

To demonstrate the robustness of these results, we next consider proportional fairness instead of maximin fairness in the optimization model. Figure 3b shows that these results are qualitatively similar when a proportional fairness criterion is used to specify the fairness constraint. The normalized proportional fairness values are negative due to negative values generated by the logarithmic form of the proportional fairness metric. As before, we see that a revenue-fairness tradeoff exists and that it is less severe for larger values of $\sigma .$

![](/api/attachments/6YP6MAU7/fulltext/images/4ca680f1a8f406432aada70c70bd1f076fafb381e5964a2fbe8f24884cdf20a3.jpg)  
(a)Max-min fairness

![](/api/attachments/6YP6MAU7/fulltext/images/f5252fe0952e51c2a1ff1c108a9c2bf179a55d4e8d073cf6ed423aed36f578f6.jpg)  
(b) Proportional fairness  
Figure 3. Achieved provider revenue for different fairness thresholds in (8) and different sets of resource requirements. The three sets of resource requirements correspond to $r _ { 1 1 } = r _ { 1 2 } = 0 . 5 , r _ { 2 1 } = \sigma ,$ $r _ { 2 2 } = 1 - \sigma$ for $\sigma = 0 . 2 , 0 . 4 ;$ and $r _ { 1 1 } = 0 . 6 8 , r _ { 1 2 } = 0 . 3 2 , r _ { 2 1 } = 0 . 1 4 , r _ { 2 2 } = 0 . 8 6$ . The last set of resource requirements was derived from the Google datacenter trace. There is no revenue-fairness tradeoff for the Google resource requirements when we use a proportional fairness constraint, and thus the curve is not visible.

We now explore the robustness of the results for different value of the parameter γ in the users’ isoelastic utility functions. Figure 4 shows the achieved revenue for different resource requirements (i.e., different values of $\sigma )$ under the revenue-maximizing prices, fairness-maximizing prices, and revenue-maximizing prices subject to a fairness constraint in which the threshold $\phi$ is set to the midpoint of the maximum and minimum achievable fairness. We see that the achieved revenue always increases with $\sigma$ for all three types of prices, suggesting that the provider can extract more revenue whenever users’ requirements are closer to being symmetric. This finding holds for both the utility function parameters $\gamma = 0 . 3 4$ and $\gamma =$ 0.68. In both cases, the revenue does not vary too much for the three different sets of prices, which is consistent with Figure 3: a stricter fairness constraint impacts the achieved revenue less than maximizing revenue impacts the achieved fairness.

Lastly, we evaluate the tradeoffs between (maximin) fairness, revenue, and social welfare (i.e., utilitarian fairness) when the users’ utility functions are exponential (i.e., specified as $V ( x ) = 1 - \exp ( - \lambda x )$ for a given parameter λ) rather than isoelastic. Once again, we use the optimization model in Equation (8) to compute the prices that maximize revenue subject to a constraint on the fairness value. Figure 5 shows our results. We observe that while there is a similar fairness-revenue tradeoff as found in the isoelastic case, there is also a tradeoff between revenue and social welfare (utilitarian fairness). For isoelastic utility functions, maximizing revenue is equivalent to maximizing the utilitarian social welfare (Lemma 1); but in the exponential utility case, the overall social welfare decreases as revenue increases. However, social welfare increases with the fairness threshold, which means that when users’ utility functions are exponential, the maximin fairness constraint imposed by a regulator on the provider’s revenue maximization problem (Equation 8) will also protect (utilitarian) social welfare.

![](/api/attachments/6YP6MAU7/fulltext/images/5aa454750acbeef8df2ad320f93aca002a0fefc1549b946b1c802ff3e53db9d4.jpg)  
(a) $\alpha = 0 . 3 4$

![](/api/attachments/6YP6MAU7/fulltext/images/a9277b1ff7dee6bd29732ec23d11816c7748dca1567cd2bf68d01112a095b653.jpg)  
(b) $\alpha = 0 . 6 8$  
Figure 4. Achieved provider revenue for different values of α as the resource requirements change. We suppose, as considered in the Quantifying the Fairness-Revenue Tradeoff section, that users’ resource requirements are given by $( r _ { 1 1 } = r _ { 1 2 } = r / 2 )$ and user 2 has dissimilar requirements $( r _ { 2 1 } = \sigma r , r _ { 2 2 } = ( 1 - \sigma ) r )$ . The achieved revenue then depends on the fairness threshold $\phi ;$ we show the achieved revenue when $\phi$ attains its maximum and minimum values, as well as the midpoint of the two (“median fairness constraint”). The area between the top and bottom curves can be interpreted as the region of achieved revenue for different threshold values.

![](/api/attachments/6YP6MAU7/fulltext/images/73bde49ef4d0d059ee833568f87eac0fc80f7b04e385a3780fd08ac9c68bfa0d.jpg)  
(a) As fairness varies

![](/api/attachments/6YP6MAU7/fulltext/images/c0c9be8885d49800768483829d8ad35c0ef48dc3b1b96dbdea2184937b8656aa.jpg)  
(b) As social welfare varies  
Figure 5. Plots of tradeoffs between provider revenue, social welfare, and maximin fairness on user utilities when users have exponential utility functions. Each point shown represents the achieved revenue, social welfare, and max-min fairness when the provider chooses the prices so as to maximize its revenue, subject to a fairness threshold constraint. We observe a similar revenue-fairness tradeoff as with the isoelastic utility functions. Additionally, the achieved social welfare increases as the fairness threshold increases; thus, imposing a fairness constraint also leads to higher (utilitarian) social welfare.

## Discussion and Conclusion

In this work, we develop a model for multiresource allocation in cloud computing and investigate the tradeoffs that different allocations create between fairness and revenue. While revenue is an important objective for cloud providers, ensuring fairness across different clients is also of critical interest, as observed in our own survey of cloud operators and from the growing interest in fairness in the cloud [18, 26, 29]. In contrast to the existing works on this topic, which have mostly analyzed the operational tradeoffs between fairness and capacity utilization without regard to pricing, we introduce an analytical framework that incorporates an endogenous model of user demand and the cloud providers’ pricing and allocation decisions in the multiresource setting. We discuss the different notions of fairness from welfare economics and then use them in our study to quantify how different configurations of users’ resource requirements create a tradeoff between the fairness and revenue objectives. We show that this tradeoff exists unless users’ resource requirements are sufficiently symmetric or sufficiently asymmetric. When a tradeoff exists, a cloud provider’s use of revenue-maximizing prices, without consideration of fairness, can lead to a significant reduction in fairness compared to the maximum achievable fairness value. Understanding if and when these tradeoffs arise is required to inform policy decisions, such as whether there is a need for regulatory intervention to achieve cloud neutrality from the perspective of resource allocation.

The notion of fairness primarily used in the main model is that of maximin fairness, which is useful for a regulator to consider in scenarios where the utility of the least well-off cloud client must be accounted for (e.g., in resource allocation across critical facilities like hospitals and non-profits). Alternatively, the regulator may consider a utilitarian fairness metric in scenarios where equity considerations are less important and some clients’ jobs are more tolerant of resource starvation (e.g., noncritical, delay-tolerant applications). Proportional fairness may be more relevant to a regulator in scenarios where the overall success of a mission depends on the completion of each clients’s jobs in proportion to their priorities (e.g., a set of mission-oriented, prioritized military applications [46]). Our numerical investigations demonstrate the robustness of the main results to these alternative fairness specifications.

Our model provides a principled approach for cloud providers to optimize for revenue while requiring a desired level of fairness across its clients to ensure that the transformative benefits of the cloud are available to all. To summarize, in this work (i) the inclusion of social welfare and equity considerations helps motivate a community-level discussion of what is fairness, (ii) the identification of the tradeoffs across a wide range of scenarios motivates why there is a need for designing new monitoring tools and regulatory policies, (iii) the quantification of resource requirement scenarios that lead to such tradeoffs informs when such policy intervention may become necessary, and (iv) the optimization formulation for the cloud provider helps answer how such allocations should be made to trade off between fairness and revenue goals.

Our work represents an initial foray into developing an analytical framework for considering both social and operational objectives in cloud computing. While we have characterized the case of two users and two resources, deriving analytical results for more general settings is difficult. Our numerical evaluations, however, show that the findings generally hold for a much wider range of scenarios. Future work can use our framework to investigate, e.g., conditions on multiple users’ requirements for which a fairness-revenue tradeoff does or does not hold. We can also consider incorporating other provider or user objectives (e.g., max-min fairness on the number of jobs submitted by each user instead of user utilities or the amount of utilized resource capacities instead of provider revenue). Another aspect to further investigate is the role of alternative pricing models, such as pay-per-resource, although we believe that tradeoffs will continue to arise, at least for scenarios where the providers cannot use higherorder price-discrimination across users on each resource. Thus, our framework can be extended for further exploration into a rich set of social and operational tradeoffs in cloud computing. In conclusion, this work can help the IS community to make important policy contributions in the emerging debate on cloud neutrality.

## NOTES

1. For virtual machines, the commonly used hourly pay-per-machine price can be easily translated to a price per job by dividing it by the number of jobs that the virtual machines (VM) can process per unit time, given its resource configuration.

2. Our survey respondents reported that fairness across clients is always an important factor in their resource allocation decisions. One respondent stated, “Enforcing fairness among multiple cloud instances is one of the most important problems in [our] internal cloud computing platform.” Another respondent further opined, “Guaranteeing fairness is always the most important task. In the cloud industry, efficiency and revenue maximization is always the second-tier goal. That is the reason why most of the public clouds are having a very low hardware utilization rate.” Additionally, all of them agreed that internal policies enforcing fair resource allocations would likely help them avoid the same kind of regulatory scrutiny that broadband providers have faced in the net neutrality debate. These comments highlight that fairness is a desirable property even for profit-seeking cloud providers.

3. The net utility realized by an individual user depend on the user’s valuation, allocation, and price, among others.

4. Jeremy Bentham was an English philosopher who is regarded as the founder of modern utilitarianism.

5. John Rawls was an American political philosopher who developed a theory of the Good as Justice and Justice conceived as Fairness.

6. It bears mention that from an auditing standpoint, it is arguably easier to measure the realized user utilities as a function of the number of jobs completed for each user than it is to precisely measure the internal allocation of resources among users in a highly virtualized datacenter. For example, Netflix and Amazon Prime both run on EC2. Netflix relies on the hypervisor underlying its Amazon EC2 instances to report on the “stolen time” (a measure of competition for CPU) to help identify incidents when its procured instances do not get enough CPU capacity. But if the cloud provider’s hypervisor does not report this metric truthfully, it will be very hard to audit and account for such neutrality violations at the individual resource level.

7. While the focus of the net neutrality literature has been on a single-resource allocation (e.g., bandwidth), packet prioritization, tiering, and openness of service provider platforms that serve a two-sided market, the initial focus of cloud neutrality has primarily been on multiresource allocation, with little consideration of prioritization or tiering. Additionally, a typical cloud provider is not a two-sided platform. But many of the issues raised in the net neutrality debate, such as openness and fair competition, may become relevant even in the cloud context.

8. We assume that users can derive utility from fractional numbers of jobs, for example, if the jobs are divided into many individual tasks, as in MapReduce scenarios often considered in the computer science literature [18].

9. These jobs are processed in VM that are configured with ratios of CPU and memory capacity as needed by the type of job. The users pays at a unit rate per VM (e.g., in Google’s Compute Engine), which can be directly translated to a per job price. It also bears mention that unlike resource pricing, differential pricing per job need not depend on the user’s per-job resource requirements in any systematic way, and therefore represents the maximum flexibility for a provider to use pricing as a lever to overcome inequity.

10. As mentioned earlier, in this work we primarily consider maximin fairness as the benchmark in our analysis as it is often considered to be the fairest allocation [7].

11. The model can also be extended to consider two types of users who have different resource requirements (i.e., two types of jobs). For example, one type of users is those with computation-intensive jobs and the other with memory-intensive jobs.

12. Isoelastic utility functions represent a large class of utility functions, parameterized by γ, that are most commonly used in the economics literature (e.g., γ = 0 corresponds to a linear utility model and γ → 1 leads to a logarithmic utility model). Moreover, because such a constant elasticity function is concave and increasing, it captures diminishing marginal utility. It bears mention that the individual-level isoelastic utility functions are not to be confused with the α-fairness social welfare function

13. This is arguably a more conservative setting for demonstrating any tradeoff between revenue and fairness perspectives. This is because any heterogeneity in the user utility functional forms is more likely to create these tradeoffs, but we show that such a tradeoff can exist even with homogeneous users who have the same utility functional form (but only differ in the ratios of different multiple resources that they need to complete their jobs).

14. Cloud providers could instead maximize their profits by including a cost term in their objectives. We suppose that the majority of the provider’s cost lies in the fixed cost of provisioning cloud infrastructure capacity instead of processing jobs, allowing us to abstract away from operational costs like electricity, scheduling, and partial server shutdowns to instead constrain the amount of each available resource

15. For the remainder of the paper, we will simply use the term “fairness” to refer to maximin fairness unless otherwise noted.

16. This is same as the notion of total welfare, realized as the sum of user and provider utilities, from a utilitarian fairness perspective.

17. In the Numerical Evaluators section, we provide additional numerical evaluation of this tradeoff with non-isoelastic user utility functions

18. Thus, if the users are homogeneous, the fairness-revenue tradeoff is avoidable by choosing the right prices. This shows that the cloud context, which features heterogeneous user requirements in the ratios of the resources, is itself the driver for this tradeoff. That is why such a tradeoff is not usually noticed in single-resource pricing and allocation settings (for users with same utility functional form).

19. In cloud parlance, this is a balanced job, which uses CPU or IO bandwidth in equal proportion.

20. These jobs are either CPU-intensive or IO-intensive.

## REFERENCES

1. Altman, E.; Avrachenkov, K.; and Garnaev, A. Generalized α-fair resource allocation in wireless networks. In Proceedings of the Institute of Electrical and Electronics Engineers Conference on Decision and Control, Cancun, Mexico: IEEE, 2008, pp. 2414–2419.

2. Amazon. EC2 pricing. http://aws.amazon.com/ec2/pricing/(accessed September 16, 2016).

3. Atkinson, A. B. On the measurement of inequality. Journal of Economic Theory, 2, 3 (1970), 244–263.

4. Battleson, D.A.; West, B.C.; Kim, J.; Ramesh, B.; and Robinson, P.S. Achieving dynamic capabilities with cloud computing: An empirical investigation. European Journal of Information Systems, 25, 3 (2016), 209—230.

5. Bertsekas, D.P.; and El Baz, D. Distributed asynchronous relaxation methods for convex network flow problems. SIAM Journal on Control and Optimization, 25, 1 (1987), 74–85.

6. Bertsimas, D.; Farias, V.F.; and Trichakis, N. The price of fairness. Operations Research, 59, 1 (2011), 17–31.

7. Bertsimas, D.; Farias, V.F.; and Trichakis, N. On the efficiency-fairness trade-off. Management Science, 58, 12 (2012), 2234–2250.

8. Binmore, K.; Rubinstein, A.; and Wolinsky, A. The Nash bargaining solution in economic modeling. The RAND Journal of Economics, 17, 2 (1986), 176–188.

9. Cheng, H.K.; Bandyopadhyay, S.; and H. Guo. The debate on net neutrality: A policy perspective. Information Systems Research, 22, 1 (2011), 60–82.

10. Cho, S.; Qiu, L.; and Bandyopadhyay, S. Should online content providers be allowed to subsidize content? An economic analysis. Information Systems Research, 27, 3 (2016), 580– 595.

11. Clemons, E.K.; Dewan, R.M.; Kauffman, R.J.; and Weber, T.A. Understanding the information-based transformation of strategy and society. Journal of Management Information Systems, 32, 2 (2017), 425—456.

12. Columbus, L. Making cloud computing pay. In Forbes. Retrieved January 1<sup>st</sup>, 2018 from http://tinyurl.com/csqa9wq.

13. Dawson, G.F.; Denford, J.S.; Williams, C.K.; Preston, D.; and Desouza, K.C. An examination of effective IT governance in the public sector using the legal view of agency theory. Journal of Management Information Systems, 33, 4 (2016), 1180–1208.

14. Dean, K. Cloud and carrier-neutrality in a colocation data centre. In Interxion. http://bit. ly/2IkgYo6 (accessed January 1, 2018).

15. Donnelly, C. Lock-in: Using cloud-neutral technology to avoid it. In Computer Weekly. http://www.computerweekly.com/blog/Ahead-in-the-Clouds/Lock-in-Using-cloud-neutral-tech nology-avoid-it (accessed January 1, 2018).

16. Feng, G.; Garg, S.; Buyya, R.; and Li, W. Revenue maximization using adaptive resource provisioning in cloud computing environments. In Proceedings of the ACM/IEEE Conference on Grid Computing, Beijing: IEEE, 2012, pp. 192–200.

17. Furneaux, B. and Wade, M. Impediments to information systems replacement: A calculus of discontinuance. Journal of Management Information Systems, 34, 3 (2017), 902–932.

18. Ghodsi, A.; Zaharia, M.; Hindman, B.; Konwinski, A.; Shenker, S.; and Stoica, I. Dominant resource fairness: Fair allocation of multiple resource types. In Proceedings of the USENIX Symposium on Networked Systems Design and Implementation, Boston: ACM, 2011, pp. 24–37.

19. Ghodsi, A.; Zaharia, M.; Shenker, S.; and Stoica, I. Choosy: Max-min fair sharing for datacenter jobs with constraints. In Proceedings of the 8th ACM European Conference on Computer Systems, Prague: ACM, 2013, pp. 365–378.

20. Giacomini, M.; Hurley, J.; and DeJean, D. Fair reckoning: A qualitative investigation of responses to an economic health resource allocation survey. Health Expectations, 17, 2 (2014), 174–185.

21. Google Cloud Platform. Compute Engine Pricing. http://bit.ly/2rxGuSi (accessed September 16, 2016).

22. Guo, H.; Bandyopadhyay, S.; Lim, A.; Yang, Y.-C.; and Cheng, H. K. Effects of competition among Internet service providers and content providers on the net neutrality debate. Management Information Systems Quarterly, 41, 2 (2017), 353–370.

23. Hellerstein, J. L. Google cluster data. In Google Research Blog. http://bit.ly/2rnec8A (accessed December 1, 2016).

24. IBM. IBM Smart cloud workload automation, IBM Data Sheet. http://bit.ly/2sr6TQF (accessed January 1, 2018).

25. Joe-Wong, C.; and Sen. S. Harnessing the power of the cloud: Revenue, fairness, and cloud neutrality. Technical Report, 2018. http://www.andrew.cmu.edu/user/cjoewong/JMIS\_ CloudNeutrality.pdf (accessed March 1, 2018).

26. Joe-Wong, C.; Sen, S.; Lan, T.; and Chiang, M. Multiresource allocation: Fairnessefficiency tradeoffs in a unifying framework. IEEE/ACM Transactions on Networking, 21, 6 (2013), 1785–1798.

27. Kalai, E.; and Smorodinsky, M. Other solutions to Nash’s bargaining problem. Econometrica: Journal of the Econometric Society, 43, 3 (1975), 513–518.

28. Kelly, F.P.; Maulloo, A.K.; and Tan, D.K.H. Rate control for communication networks: Shadow prices, proportional fairness and stability. The Journal of the Operational Research Society, 49, 3 (1998), 237–252.

29. Kesidis, G.; Urgaonkar, B.; Nasiriani, N.; and Wang, C. Neutrality in future public clouds: Implications and challenges. In Proceedings of the 8th USENIX Workshop on Hot Topics in Cloud Computing, Denver: USENIX, 2016, pp. 1–6.

30. Lan, T.; Kao, D.; Chiang, M.; and Sabharwal, A. An axiomatic theory of fairness in network resource allocation. In Proceedings of the IEEE International Conference on Computer Communications, San Diego: IEEE, 2010, pp. 1–9.

31. Lehmann, S.; Draisbach, T.; Buxmann, P.; and Dörsam, P. Pricing of software as a service – An empirical study in view of the economics of information theory. In Proceedings of the International Conference on Software Business, Cambridge, Massachusetts: Springer, 2012, pp. 1–14.

32. Li, H.; Liu, J.; and Tang, G. A pricing algorithm for cloud computing resources. In Proceedings of the IEEE International Conference on Network Computing and Information Security, Guilin, China: IEEE, 2011, pp. 69–73.

33. Lin, W.-Y.; Lin, G.-Y.; and Wei, H.-Y. Dynamic auction mechanism for cloud resource allocation. In Proceedings of the IEEE/ACM International Conference on Cluster, Cloud, and Grid Computing, Melbourne: IEEE, 2010, pp. 591–592.

34. Marston, S.; Li, Z.; Bandyopadhyay, S.; Zhang, J.; and Ghalsasi, A. Cloud computing: The business perspective. Decision Support Systems, 51, 1 (2011), 176–189.

35. Mas-Colell, A.; Whinston, M.D.; and Green, J.R. Microeconomic Theory. New York: Oxford University Press, 1995.

36. Rawls, J., and Kelly, E. Justice as Fairness: A Restatement. Boston: Harvard University Press, 2001.

37. Renda, A. Competition, neutrality and diversity in the cloud. Communications and Strategies, 85, 1 (2012), 23–44.

38. Roberts, N.; Campbell, D.E.; and Vijayasarathy, L.R. Using information systems to sense opportunities for innovation: Integrating postadoptive use behaviors with the dynamic managerial capability perspective. Journal of Management Information Systems, 33, 1 (2016), 45–69.

39. Samimi, P.; and Patel, A. Review of pricing models for grid & cloud computing. In Proceedings of the IEEE Symposium on Computers and Information, Kuala Lumpur: IEEE, 2011, pp. 634–639.

40. Samuelson, P.A. Some implications of “linearity.” The Review of Economic Studies, 15, 2 (1947), 88–90.

41. Sen, A. Utilitarianism and welfarism. Journal of Philosophy, 76, 9 (1979), 463–489.

In Proceedings of the $2 { \cal O } ^ { t h }$ European Conference on Information Systems, Barcelona: AIS, 2012, pp. 161.

43. Tang, A.; Wei, D.; and Low, S.H. Heterogeneous congestion control: Efficiency, fairness and design. In Proceedings of the IEEE International Conference on Network Protocols, Santa Barbara, California: IEEE, 2006, pp. 127–136.

44. Tilson, D.; Lyytinen, K.; and Sorensen, C. Digital infrastructures: The missing IS research agenda. Information Systems Research, 21, 4 (2010), 748–759.

45. Vizard, M. The march toward cloud neutrality. In Barracuda MSP Industry and Tech Blog. https://blog.barracudamsp.com/the-march-toward-cloud-neutrality (accessed January 1, 2018).

46. Wagner, S.; van den Berg, E.; Giacopelli, J.; Ghetie, A.; Burns, J.; Tauil, M.; Sen, S.; Wang, M.; Chiang, M.; Lan, T.; Laddaga, R.; Robertson, P.; and Manghwani, P. Autonomous, collaborative control for resilient cyber defense (ACCORD). In Proceedings of the Workshop on Adaptive Host and Network Security, Lyon, France: IEEE, 2012, pp. 39–46.

47. Wang, H.; Jing, Q.; Chen, R.; He, B.; Qian, Z.; and Zhou, L. Distributed systems meet economics: Pricing in the cloud. In Proceedings of the USENIX Workshop on Hot Topics in Cloud Computing, Boston: USENIX, 2010, pp. 1–7.

48. Wang, N.; Liang, H.; Jia, Y.; Ge, S.; Xue, Y.; and Wang, Z. Cloud computing research in the IS discipline: A citation/co-citation analysis. Decision Support Systems, 86 (2016), 35–47.

49. Wang, W.; Zhang, P.; Lan, T.; and Aggarwal, V. Datacenter net profit optimization with deadline dependent pricing. In Proceedings of the Conference on Information Sciences and Systems, Princeton: IEEE, 2012, pp. 1–6.

50. Weins, K. Cloud computing trends: 2016 state of the cloud survey. In Cloud Management Blog. http://bit.ly/1TTf92A (accessed January 1, 2018).

51. Xu, H.; and Li, B. Maximizing revenue with dynamic cloud pricing: The infinite horizon case. In Proceedings of the IEEE International Conference on Communications Next-Generation Networking Symposium, Ottawa: IEEE, 2012, pp. 2929–2933.

52. Yoo, C.S.; and Blanchette, J.F. Regulating the Cloud: Policy for Computing Infrastructure. Boston: The MIT Press, 2015.

53. Zaharia, M.; Borthakur, D.; Sen Sarma, J.; Elmeleegy, K.; Shenker, S.; and Stoica, I. Delay scheduling: A simple technique for achieving locality and fairness in cluster scheduling. In Proceedings of the 5<sup>th</sup> European Conference on Computer Systems, Paris: ACM, 2010, pp. 265–278.

54. Zheng, L.; Joe-Wong, C.; Tan, C. W.; Chiang, M.; and Wang, X. How to bid the cloud. ACM Special Interest Group (SIGCOMM) Computer Communication Review, 45, 4 (2015), 71–84.
