---
otero_id: 2094
otero_key: "PTYP6DF3"
title: "Syndicating Web Services: A QoS and user-driven approach"
authors: "Yi Sun; Shaoyi He; Jack Y. Leu"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.09.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Syndicating Web Services: A QoS and user-driven approach

Yi Sun <sup>⁎</sup>, Shaoyi He, Jack Y. Leu

High-Technology Management Department, College of Business Administration, California State University San Marcos, San Marcos, CA 92096-0001, United States

Received 23 April 2005; received in revised form 30 June 2006; accepted 12 September 2006 Available online 1 November 2006

## Abstract

Web Services that provide a real-time e-business solution via online binding of software components must have a mechanism to win users' confidence in the quality of service (QoS) to establish a solid foot holding in the market. Inspired by the trust third-party approach in the public key system, we explored the idea of expanding the role of registrars to include (1) assessing quality of Web Services and (2) syndicating Web Services. The Analytic Hierarchy Process (AHP) and the Brown–Gibson (BG) methods were adapted to facilitate quality assessment. An optimization model was proposed for Web Service syndication. A heuristic algorithm was developed to solve the NP-hard problem, and an experiment was conducted, with two sensitivity analyses involving adjusting parameters, to compare its performance and the optimal solutions. © 2006 Elsevier B.V. All rights reserved.

Keywords: Web Services; Web Services registry; Web Services syndication; Quality of Service (QoS); AHP method; Brown–Gibson method

## 1. Introduction

Web Services have emerged as a viable e-business platform, providing a business software solution via realtime binding of software components over the Internet or corporate networks. This technology is facilitated by a set of standard protocols that allow: (1) a service provider to publish software components, (2) a registrar to serve as the repository of available services, and (3) a user to discover services suitable for the business.

To fully realize the potential, the Web Services infrastructure must have a mechanism to bestow users confidence in the quality of the published software components. The issue is similar to the public key infrastructure, whose success hinges on the key authentication. Therefore, we propose that the role of the Web Services registrar be expanded to include Quality of Service (QoS) assessment and Web Services syndication. By syndication, we mean that a registrar with the capability of identifying a user's QoS preferences could make recommendations and/or provide a package of Web Services to the user. Such a process could turn a passive registrar into an active player. Some might suspect the impartiality of a registrar. We believe that the market self-selection process will keep the registrar in check, much the same as it does to firms providing and registering public keys.

However, QoS encompasses so many different dimensions including integrity of solution, speed, security and cost. It is difficult, if not impossible, to derive an absolute QoS measurement. This is compounded by the fact that the value of QoS is in the eyes of the beholder. Any QoS assessment effort would be to no avail if a user's QoS preferences were not taken into consideration.

In this study, we first adopt Saaty's Analytic Hierarchy Process (AHP) approach [27] for assessing quality of Web Services published to a registrar. The outcome of the AHP approach is a set of Eigenvalues representing the relative merits of available services. The AHP approach, however, involves time-consuming pair-wise comparisons. To alleviate the problem, we adapted the Brown–Gibson method (BG) [7] to further divide the QoS criteria into two categories: subjective and objective. While the subject criteria reflect a user's personal opinions or attitudes, the objective criteria are those can be measured in the monetary term. The BG approach provides an efficient way to derive the relative merits of services in terms of objective criteria. For the subjective criteria, we recommend using the AHP approach to obtain the relative merits so that evaluation biases can be avoided [31]. The BG approach also provides a way to synthesize the subjective and the objective evaluations into a composite index. We then incorporate the composite indices into a mathematical model, capturing the syndication efforts of a registrar. The resulting mathematical model is an NP-hard problem. A heuristic algorithm is developed, and an experiment is conducted to compare its performance to the optimal solutions. Optimal solutions are obtained through CPLEX because it is one of the industry leading software, and the heuristic algorithm is coded in C++ to take advantage of its object-oriented features. The experiment is also done with two sensitivity analyses that involve adjusting two parameters: variations in QoS and increases in the number of service providers.

This paper is organized in the following fashion. A brief literature review is provided in the next section, followed by the discussions of the AHP and the BG approaches. The mathematical model and the heuristic algorithm are then presented, along with the experiment and its results. Finally, the benefits and the limitations are discussed.

## 2. Literature review

Web Services have recently become a viable Internetbased distributed e-commerce platform to establish and maintain business relationships and product development. They support self-describing and modular software applications with open interface standards and communication protocols. They exceed previous distributed component technologies by offering a high level of interoperation between programs that are written in different languages and running on different operating systems [17]. Web Services, reinforcing the principles of modularization, reuse, and information hiding, offer an unparalleled level of customization to support business processes. Software systems based on Web Services are able to quickly adapt to dynamic business environments through fast assembly and disassembly of its Web Services components [26].

Due to the perceived cost benefit, Web Services are increasingly adopted by businesses for their principle activities [3,13]. Research activities on Web Services are also flourishing including studies on Web Services dynamic discovery [20], composition [37], application integration [1], adoption [36], and location [33].

Facing a market full of competitive Web Services of various qualities, a consumer may have to spend a large amount of time to find the right products and even more to keep its services in accord with the offerings in the market [20]. A consumer's request may require assemblies of multiple Web Services from a large collection of services offered in the market. When business environments change, the consumer may need to change business rules and models accordingly and therefore need to dynamically change his Web Services portfolio. This requires the development of automated systems for Web Services discovery. Efforts have been made to combine the UDDI and the WSDL protocols to automate service discovery and usage [11,20]. However, it is still difficult to dynamically identify Web Services for specific business applications.

As the Web Service market matures, a service may be offered by a number of providers with different qualities. While many Web Services quality dimensions have been identified [5,37], consumers may have limited controls over these qualities due to the distributed nature of Web Services. At the same time, consumers may also have different quality preferences when choosing a service as one of the building blocks of their applications. Tian et al. [34] proposed an architecture for QoS-aware service discovery and selection of Web Services. Cardoso et al. [8] developed a model to analyze and estimate the overall QoS for new functionality in the context of Web processes. Other approaches have also been proposed to globally optimize the overall QoS during the execution of composing a composite service [5,37].

For the Web Service to be successful as envisioned, it must prove to have the ability to support the needs of businesses. In facing stiffer global competitions, more and more companies are focusing on their core competency while outsourcing other applications over the Internet [32]. Incorporating QoS measurements into the Web Service infrastructure allows an organization to effectively select and integrate heterogeneous services across organizational boundaries [16,30]. QoS-based Web Service infrastructure, therefore, helps an organization translate its vision into business processes more efficiently [8]. An organization also needs to adapt to the everchanging environment. QoS-based infrastructure makes it possible for an organization to monitor QoS metrics and trigger the adaptation strategies when threshold values are reached [8]. Conversely, lacking QoS measurements would severely limit the potential of Web Services. Thus, there is an effort to address how to incorporate QoS measurements into Web Service infrastructure [19].

Another issue in the Web Services that has not been fully addressed is syndication. The importance of Web Service syndication is twofold. When no single service can satisfy the functionality of a user's request, the infrastructure should allow the possibility of combining services to fulfill the request [23,32]. In addition, related services could be offered by many independent providers, giving rise to an inherent need for composing these complementary services to meet the user's requirements [23]. The syndication capability is of particular importance to a B2B service, which provides a conglomeration of services working in tandem to achieve a user's overall business objectives [25]. Recent efforts in Web Service syndication include the work by Akkiraju et al. [2], who suggested a conceptual framework for Web Services syndication that allowed business applications to be built by aggregating existing Web Services. In their framework, the Web Services registry system played a central role in constructing dynamically configurable systems.

The AHP is a multi-criteria decision-making methodology particularly suitable for the situation where due regard for individual beliefs is critical. The methodology uses pair-wise comparisons and Eigenvector to prioritize alternatives. Its theory and the underlining axioms was introduced by Saaty [29] and further developed by many other scholars [4,15]. Since its introduction, the AHP has found its way to solving a wide spectrum of real-world problems. Shim [30] and Vargas [35] provided a comprehensive collection of industry and public sector applications. One of the AHP's criticisms is its pair-wise comparisons, which are labor intensive and could be unreliable under some circumstances. Therefore, there is an interest in incorporating other methodologies into the AHP to address the potential problems. For example, Punniyamoorthy and Vijaya Ragavan [24] applied the Brown–Gibson model and the AHP to select automatic storage/retrieval systems. Instead of using pair-wise comparisons, the Brown– Gibson model uses the actual costs to derive the relative merits of alternatives along the criteria that can be measured objectively. It only relies on human judgments for intangible criteria. Other examples of the Brown– Gibson model applications can be found in Refs. [6,22].

In this study, we propose a QoS and user-driven approach to Web Services syndication. We believe that a full-fledged Web Services registry system can be developed so that a registrar not only serves as a clearinghouse in which a Web Service provider publishes its services, but also syndicates the services. However, syndication must mean much more than merely repackaging available services. A syndicator must have a mechanism to assess the quality of Web Services, understand the needs of its user, and identify the best collection of services that match a user's preferences.

![](/api/attachments/PTYP6DF3/fulltext/images/a9b341333e7bc9a378f43b5fac2e5fc19eceb7da6d58bbbf30074ca590a40131.jpg)  
Fig. 1. A Web Services syndication model adapted from Ref. [14].

Fig. 1 shows a revised Web Services model in which the registrar also plays the role of syndication. There are several distinct features in this proposed model. The registrar develops a set of quality attributes for evaluating available services. Based on the evaluations of a group of experts, the AHP/BG method is used to derive the quality index of each service. The quality indices along with the experts' evaluation are stored in a database on the syndicator's server. When a service is needed, a user sends the registrar a request along with his/her QoS preferences. The registrar then employs a search mechanism to identify the services that best match the user's preferences. The user is notified of the selected services with the quality indices and the experts' evaluations. Upon confirming the subscription, the registrar “binds” the service on behalf of the user. Finally, the registrar will solicit user's ratings along with the quality attributes after the service is deployed. The feedback ratings will then be used to validate and update experts' evaluations. The following sections detail our approach to implementing the augmented registrar functions.

## 3. Models and solutions

## 3.1. User driven Web Service syndication

We first assume that there are M providers collectively offering N services. An M by N incidence matrix, $G ,$ is used to represent services available from each

Table 1

provider in that $g _ { m n } = 1$ if provider m offers service $n ;$ otherwise, $g _ { m n } = 0$ . We then assume that the QoS of a provider is measured along r quality dimensions including security, speed, information integrity, cost, and so on. To facilitate syndication, the registrar, using the AHP approach, assesses QoS of providers and stores the evaluation results in a matrix whose entries are denoted as $q _ { m n r }$ where $0 \leq q _ { m n r } \leq 1$ with 1 being the highest evaluation and $\begin{array} { r } { \sum _ { m } q _ { m n r } = 1 , } \end{array}$ n and $\forall r .$ We further assume that a service request is also accompanied by a set of QoS preferences, expressed as $w _ { r } ,$ where $0 \leq w _ { r } \leq 1$ with 1 being the best preference and $\textstyle \sum w _ { r } = 1$ . Therefore, the objective of the registrar is to identify a provider, who can provide the best QoS, taking into consideration of user's preferences, for a particular service, say service ñ. This can be formulated as the following:

$$
\text { Maximize }: \sum_ {m} x _ {m \tilde {n}} g _ {m \tilde {n}} \sum_ {r} w _ {r} q _ {m \tilde {n} r}
$$

$$
\text { Subject   to }: \sum_ {m} x _ {m \tilde {n}} = 1;
$$

where $x _ { m \tilde { n } }$ are 0–1 integer decision variables.

The objective function is to maximize the dot product of a user's preferences and a provider's QoS rating. Provider m is chosen, i.e. $x _ { m \tilde { n } } = 1$ , when it provides the service, i.e., $g _ { m \tilde { n } } { = } 1$ and the sum of the dot product is the highest. The formulation, however, offers no guarantee in matching all of the preferences of the user, while the goal is to search for the best overall fit and use the objective value as an indicator of the goodness of the fit. This problem is rather straightforward. However, the derivation of $q _ { m n r }$ is a non-trivial task. In the following section, we adopt the AHP approach to evaluate QoS services.

## 3.1.1. Building providers' QoS indices

The AHP approach has been used in many arenas for evaluating the relative merit of alternatives. It is not only built on a solid mathematical foundation, but also provides a way to remove rating biases stemming from lack of equal reference bases that have plagued many evaluation schemes. For example, when evaluating candidates in a hiring process, a recruiting committee could evaluate candidates by assigning a score, say 1–10, to each evaluation criterion. However, a score of 5 given by a committee member could be drastically different from the same score by another committee member because they do not necessarily share the same reference base. The AHP approach uses pair-wise comparisons to alleviate this problem. Following the previous example, the recruiting committee members would rate how much more attractive Candidate A is in comparison to Candidate B in terms of a criterion, say teaching. A rating of “Candidate A is 3 times better than Candidate B in teaching” by two different committee members is commensurable because different reference bases become immaterial when the rating is expressed as a ratio.

Saaty suggests a 1–9 ratio scheme for pair-wise comparisons. More specifically, a score of 1 means equally preferred; 3 moderately preferred; 5 strongly preferred; 7 very strongly preferred; and 9 extremely preferred. In-between scores are possible, and reciprocal scores are used for reverse comparisons. For example, if Candidate A is rated as 3 times more attractive than Candidate B (moderately preferred in Saaty's terminology), Candidate B is rated as 1/3 as attractive as Candidate A. For each evaluation criterion, a matrix is used to represent the pair-wise comparisons among all candidates or alternatives under consideration. Saaty shows mathematically that the values of the Eigenvector of this comparison matrix, normalized to between 0 and 1, represent the relative merits of alternatives in terms of an evaluation criterion. Saaty also provides an index for gauging inconsistencies resulted from the pair-wise comparisons. We use an example to illustrate this.

A loan company relies on multiple Web Services to make decisions on loan approval. Assume that four providers offer a total of five Web Services: credit score inquiry, criminal history check, current interest rates quote, employment verification, and residency proof. For each of these services, four quality criteria including security, cost, information integrity/accuracy, and speed are of particular concern. Table 1 is the incidence matrix showing the services available from each provider. For example, Provider 1 offers Services 1, 3, and 4. Similarly, Service 3 is available from Providers 1, 2, and 3. We will use Service 3 to demonstrate the AHP evaluation process.

Table 2 is the comparison matrix, which shows the result of pair-wise comparisons of the three providers offering Service 3 in terms of security. The diagonal elements are 1s because they represent self-comparisons and, by default, their score should be 1. In this hypothetical case, Provider 1 with a score of 3 is rated as moderately preferred to Provider 2 and a score of 9 as extremely preferred to Provider 3 in terms of security. By using reciprocal ratings, Provider 2 and Provider 3 are 1/3 and 1/9 as preferred as Provider 1, respectively.

Service-provider incidence matrix

<table><tr><td rowspan="2">Providers</td><td colspan="5">Web Services</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>2</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>4</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr></table>

Table 2  
The comparisons of service providers in terms of security

<table><tr><td rowspan="2">Providers</td><td colspan="3">Providers</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>1</td><td>1</td><td>3</td><td>9</td></tr><tr><td>2</td><td>1/3</td><td>1</td><td>6</td></tr><tr><td>3</td><td>1/9</td><td>1/6</td><td>1</td></tr></table>

Several software packages are available to derive the Eigenvalues. We use Expert Choice 11 [10] because it is easy to use and readily available through the Internet. The Eigenvector for Table 2 is [.663, .278, .058] with an inconsistency coefficient of .05. These three Eigenvalues indicate the relative attractiveness of the three providers from the view point of security. In this case, Provider 1 is far more attractive than the other two counterparts. The inconsistency coefficient reveals some minor discrepancies in the pair-wise comparisons. Recall that Provider 1 is “3 and 9 times” as attractive as Providers 2 and 3 respectively; however, Provider 2 is rated “6 times” as attractive as Provider 3. The transitive relation does not hold, thus giving rise to the inconsistency. Saaty [9,21] suggests that the inconsistency coefficient, which, in essence, is measured by the average deviation of expected transitive relations, be less than .1. Otherwise, the pair-wise comparisons should be scrutinized.

We use the above procedure to evaluate the relative merits of the three providers in terms of cost, information integrity/accuracy, and speed. Table 3 provides the overall result of this hypothetical case. Provider 1 is the most attractive in terms of security, and Provider 3 is the most meritorious in terms of cost. The same interpretation can be applied to the other two quality criteria. The pair-wise comparison approach is regarded as an effective way to derive the relative merits of alternatives [28]. However, the approach does not work well in the situation where the relative merits of alternatives are highly skewed; i.e. all alternatives under consideration are either very good or very bad. In this extreme situation, human judgments are unlikely to discern the subtle differences among alternatives. In other words, the pair-wise comparisons would result in scores of all 1s. On the contrary, the averaged user ratings, especially when the number of users is large, exhibit a better discriminating power. Therefore, we suggest that the ratio of the averaged user ratings be used in lieu of Saaty's scaling system in this case. We also suggest that the user's ratings, when available, be considered in conjunction with the experts' evaluations.

Table 3  
Relative QoS attractiveness

<table><tr><td rowspan="2">Quality criteria</td><td colspan="3">Providers’ QoS attractiveness</td><td rowspan="2">Inconsistency coefficients</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Security</td><td>.663</td><td>.278</td><td>.058</td><td>.05</td></tr><tr><td>Cost</td><td>.258</td><td>.105</td><td>.637</td><td>.04</td></tr><tr><td>Information integrity/accuracy</td><td>.125</td><td>.750</td><td>.125</td><td>.00</td></tr><tr><td>Speed</td><td>.625</td><td>.238</td><td>.136</td><td>.02</td></tr></table>

## 3.1.2. Matching customer's preferences

When a user submits a service request in the discovery phase, quality preferences can be transmitted at the same time. In other words, a user provides his/her preferences or weights on a set of corresponding quality criteria to indicate their relative importance. The AHP approach can be applied to derive these weights. With the user's preferences, the registrar can calculate the dot products of the user's preferences and the QoS ratings of each provider who offers the service capable of fulfilling the request. To continue with the above example, a numerical example is shown in Table 4 in which the user preferences' column shows the user's relative preferences along the four quality criteria. The sum row shows the dot product of a provider's quality ratings and the user preferences. Since Provider 1 has the highest dotproduct score (.48), it is deemed as the best provider for this request.

## 3.2. Subjective and objective measurements of QoS

In addition to the difficulty in dealing with the situation where quality distribution is extremely skewed as alluded to earlier, the AHP approach has several other disadvantages. First, rank reversal could occasionally occur when similar alternatives are introduced. For example, in an initial vehicle purchasing evaluation, the AHP methodology ranks a white BMW better than a black Mercedes. However, when a red BMW is added to the alternative list, the white BMW could rank lower than the black Mercedes. While algorithms have been developed to overcome this shortcoming, a client needs to remain cautious about this potential consequence [31]. Second, the AHP approach requires $\frac { 1 } { 2 } r \dot { n } ( n - 2 )$ comparisons, where r is the number of evaluation criteria and n is the number of alternatives. It is evident that the pair-wise comparisons could quickly become laborious and less reliable as the number of alternatives and/or criteria increases. Third, in a more dynamic situation, these comparisons must be reevaluated frequently. Consider the previous example in which providers are assessed against four quality criteria. One can argue that the characteristics of security, information integrity/accuracy, and speed are closely related to capital investment; therefore, they do not change frequently since capital investment is likely to be fixed for a longer period of time. On the contrary, cost does not share the same stable characteristics; it is likely to become a key competitive strategy exploited by the price leaders and followers alike as the industry matures. In this situation, constantly conducting pair-wise comparisons over a large number of alternatives would become a drudgery task if possible at all. In addition, cost can be measured in a more precise term than the AHP's notion of degree of preferences. Therefore, we integrate the AHP approach with the Brown–Gibson method (BG) so that it, in our opinion, works better in a volatile environment and provides an improved evaluation for cost-related criteria.

Table 4  
Matching user's preferences

<table><tr><td rowspan="2">Quality criteria</td><td rowspan="2">User preferences</td><td colspan="3">Providers’ QoS attractiveness</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Security</td><td>0.30</td><td>.663</td><td>.278</td><td>.058</td></tr><tr><td>Cost</td><td>0.25</td><td>.258</td><td>.105</td><td>.637</td></tr><tr><td>Information integrity/accuracy</td><td>0.13</td><td>.125</td><td>.750</td><td>.125</td></tr><tr><td>Speed</td><td>0.32</td><td>.625</td><td>.238</td><td>.136</td></tr><tr><td>Sum</td><td></td><td>0.480</td><td>0.283</td><td>0.236</td></tr></table>

The BG method classifies evaluation criteria into two categories: objective and subjective factors, depending on whether or not they can be measured by the monetary term. By considering objective factors separately, a client can elaborate on cost components such as transmission cost, hardware cost, and so on. The BG method then provides the following elegant approach to developing an objective index for each alternative under consideration. Let $c _ { i }$ represent the total cost of Alternative i. The objective index, $O _ { i } , \enspace 0 \leq O _ { i } \leq 1$ , for Alternative i is defined as:

$$
O _ {i} = \frac {1}{c _ {i} \sum 1 / c _ {j}}, \forall c _ {j} \neq 0\tag{1}
$$

For example, we assume that the total costs per request for the three providers are ¢30, ¢50, and ¢15, respectively. Their respective objective indices, which represent their relative merits, would be 5/18, 3/18, and 10/18.

For the subjective factors, the BG method suggests using a scale of 1–10 to rate each alternative. These scores are then converted to ratings between 0 and 1. The subjective index for alternative $i , S _ { i } , 0 { \leq } S _ { i } { \leq } 1$ , is the sum of the dot product of its subjective ratings and the weights of user preferences on these factors. The BGs' approach to evaluating subjective factors has two serious shortcomings. Multi-criteria evaluations require that alternatives be evaluated against independent criteria. The BG approach lacks the ability to address the correlation issue. On the contrary, the AHP approach ensures criteria independence by structuring criteria in a hierarchical fashion [29]. In addition, the rating approach used in the BG method entails that all evaluators have an equal reference basis. The AHP approach uses pair-wise comparisons to avoid problems stemming from unequal reference bases. Therefore, we recommend that it be substituted with the AHP approach.

The BG method combines subjective and objective evaluations into a composite index, which is expressed as the linear combination of both indices and is defined as: $\begin{array} { r } { L _ { i } { = } \alpha O _ { i } { + } ( 1 - \alpha ) S _ { i } } \end{array}$ , where α, $0 \leq \alpha \leq 1$ , represents the relative emphasis on the objective evaluations [18]. $L _ { i } \mathbf { s } ,$ thus, are line segments between 0 and 1, and a decision frontier can be constructed based on these line segments. Furthermore, if the decision frontier consists of more than one line segment, each intersection of two line segments can serve as a yard stick for determining the relative emphasis between the subjective and objective factors. We will continue to use the example discussed in the previous section to illustrate this.

Refer to Table 5. Security, information integrity/ accuracy, and speed are classified as subjective quality criteria. The derivation of provider's ratings follows the AHP approach. The subjective index for each provider is its individual ratings on these quality criteria weighted by user preferences. In this case, the subjective indices are .555, .341, and .103 for Providers 1, 2, and 3, respectively. On the other hand, the transmission cost and the hardware cost are classified as objective quality criteria. The total costs of these two objective quality criteria are used to calculate the objective indices as given in Eq. (1), which are .278, .167, and .555 for the three providers, respectively.

Table 5  
A Brown–Gibson example

<table><tr><td rowspan="2">Subjective quality criteria</td><td rowspan="2">User preferences</td><td colspan="3">Providers</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Security</td><td>0.40</td><td>.663</td><td>.278</td><td>.058</td></tr><tr><td>Information integrity/accuracy</td><td>0.17</td><td>.125</td><td>.750</td><td>.125</td></tr><tr><td>Speed</td><td>0.43</td><td>.625</td><td>.238</td><td>.136</td></tr><tr><td>Subjective Index ( $S_i$ )</td><td></td><td>.555</td><td>.341</td><td>.103</td></tr></table>

<table><tr><td rowspan="2">Objective quality criteria</td><td colspan="3">Providers</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Transmission cost</td><td> $\phi 10$ </td><td> $\phi 45$ </td><td> $\phi 10$ </td></tr><tr><td>Hardware cost</td><td> $\phi 20$ </td><td> $\phi 5$ </td><td> $\phi 5$ </td></tr><tr><td>Total cost</td><td> $\phi 30$ </td><td> $\phi 50$ </td><td> $\phi 15$ </td></tr><tr><td>Objective index ( $O_i$ )</td><td>.278</td><td>.167</td><td>.555</td></tr></table>

Fig. 2 shows the construction of the decision frontier based on the composite indices, each of which is a linear combination of a provider's objective index and subjective index. As shown in the figure, $L _ { 1 }$ and $L _ { 3 }$ make up the decision frontier and these two line segments intersect at $\alpha _ { * } = . 6 2$ . This implies that if a client gives a weight of $. 6 2$ or more to the objective factors, Provider 3's service will be the choice. Otherwise, Provider 1 will be the favorite. Provider 2 will never be considered because it is inferior to Providers 1 and 3 in all circumstances.

## 3.3. Syndication with a user budget constraint

The combination of AHP and the BG methods provides a methodology for a registrar to syndicate services and play the role of a quality assessor. In terms of optimization, however, the methodology is myopic and greedy in nature. It merely considers the best solution on a per usage basis, not the entire solution space in a planning horizon. Furthermore, it does not consider the budget implication for repetitive service requests. For example, an e-business may rely on Web Services such as credit checking, delivery tracking, and zip-code verification for every transaction. In such an environment, demand, budget and other constraints may become critical. However, the AHP and the BG methods cannot accommodate any of these constraints. Therefore, we propose the following model that takes into account volume requests with a budget constraint.

![](/api/attachments/PTYP6DF3/fulltext/images/c577524c69f26c8b73d92b07e002de47cb22d7d84d33bfc30d883e3a93651ec8.jpg)  
Fig. 2. The decision frontier.

Let $d _ { n }$ denote a user's total amount of requests for Service n during a planning horizon, $c _ { m n }$ the cost of using Service n offered by Provider $m , \lambda$ an arbitrarily large number, and C the total budget. Furthermore, let $u _ { m n }$ be integer decision variables determining the amount of requests for Service n that is fulfilled by Provider m. Other notations are the same as those in the previous sections. The problem can be formulated as the following:

$$
\text { Maximize }: \sum_ {r} w _ {r} \left(\sum_ {m} \sum_ {n} u _ {m n} q _ {m n r}\right)
$$

$$
\text { Subject   to }: \sum_ {m} u _ {m n} = d _ {n}, \forall n\tag{2}
$$

$$
\sum_ {m} \sum_ {n} u _ {m n} c _ {m n} \leq C\tag{3}
$$

$$
u _ {m n} <   \lambda g _ {m n}, \forall n, m\tag{4}
$$

The objective function is to maximize the overall quality level with the consideration of a user's preferences. Constraint (2) is to ensure that all service requests are met; Constraint (3) is to uphold the budget requirement; and Constraint (4) is to make sure that requests are only fulfilled by providers offering the services.

The formulation is a constrained multi-dimensional knapsack problem and is strongly NP-hard [12]. In other words, optimal solutions can be obtained within a reasonable amount of time only for small-sized problems. However, problems of large size need heuristics that take advantage of the structures of the problem. We developed a heuristic algorithm so that decisions for real-time service binding are possible. The algorithm involves the following steps:

1. Obtain an initial solution by selecting services from low to high cost to meet demand, $d _ { n } .$ . If the budget constraint is violated, there are no feasible solutions.

2. Arrange all unselected services in the descending sequence of $\begin{array} { r } { \varphi _ { m n } = \sum _ { r } w _ { r } q _ { m n r } / c _ { m n } \cdot \varphi _ { m n } } \end{array}$ , termed the QC ratio, is the dot product of the QoS indices and a user's preferences over the cost of a service.

3. Arrange the services in the incumbent solution in the ascending sequence of the QC ratios.

4. Replace, as much as the budget allows, the incumbent service with the lowest QC ratio by the available service with the highest QC ratio. The feasible solution is still guaranteed as the replacement process does not upset the budget and the demand constraints.

5. Repeat Step 4 until no improvement can be found.

In Step 1, the selection process involves a scanning of the M by N services; therefore, the complexity is O (mn). Steps 2 and 3 entail the sorting of at most M by N elements. We employed the quicksort algorithm, which has an average complexity of O(mn log(mn)). Steps 4 and 5 are the most time-consuming components of the algorithm. Since the list of available services contains at most M by N services and the number of search iterations for replacing inferior solution is at most N, the length of the incumbent solution, these two steps have a complexity of $O ( m n ^ { 2 } )$ . Therefore, the proposed algorithm has a computational complexity of $\bar { O ( m n ^ { 2 } ) }$ .

## 3.3.1. The experiment

The proposed mathematical model is a known NPhard problem and renders it unsuitable for large-sized problems. While the proposed heuristic algorithm has a polynomial computational complexity, it requires a sacrifice in solution quality. Therefore, the trade-off warrants a closer scrutiny. We used CPLEX version 9 and C++ to implement the proposed mathematical program and the heuristic algorithm. Both are run on a laptop with a 1.6 GHz Pentium 4 processor and 512 MB

RAM. The test cases were generated based on three factors as follows:

I. The number of Web Services (N) and the number of providers in the market (M).

More specifically, N and M are set at three levels: a. Small-sized problems: $N { = } 1 0 0$ and M=50;

b. Medium-sized problems: N = 500 and M = 100;

c. Large-sized problems: N =1500 and M= 500.

II. Percentage of providers (P) who provide a particular service.

We set P at three levels: low (25%), medium (50%), and high (75%).

III. Budget constraints (B).

We set the budget constraints at two levels: loose and tight, which were determined as follows. We first set the budget of a test case at an arbitrarily high level so that the budget was not a binding constraint. We then ran a study to determine the cost of the optimal solution and randomly set the tight budget constraint at 15% to 25% below that level.

The demand $( d _ { n } ) ,$ , the cost $( c _ { m n } )$ , and the quality index or Eigenvalue $( q _ { m n r } )$ were all randomly generated for each test case. We assumed that the demand was uniformly distributed between 1 and 15. Since service providers were not capacitated in this study, we did not believe that the distribution and the range of demands would significantly affect the behavior of the heuristic algorithm and the optimization procedure. We also assumed that the cost per service request would follow a uniform distribution between 1 and 5. In addition, we assumed that there were 10 QoS criteria. $\sum _ { r } w _ { r } q _ { m n r }$ was calculated in advance to facilitate the generation of the objective functions using CPLEX.

Table 6  
ANOVA for performance gap

<table><tr><td>Source</td><td>Type III sum of squares</td><td>df</td><td>Mean square</td><td>F</td><td>Sig.</td></tr><tr><td>Corrected model</td><td>1102.129(a)</td><td>17</td><td>64.831</td><td>498.161</td><td>.000</td></tr><tr><td>Intercept</td><td>1966.390</td><td>1</td><td>1966.390</td><td>15109.684</td><td>.000</td></tr><tr><td>FACTOR_1</td><td>178.174</td><td>2</td><td>89.087</td><td>684.544</td><td>.000</td></tr><tr><td>FACTOR_2</td><td>69.250</td><td>2</td><td>34.625</td><td>266.057</td><td>.000</td></tr><tr><td>FACTOR_3</td><td>750.358</td><td>1</td><td>750.358</td><td>5765.730</td><td>.000</td></tr><tr><td>FACTOR_1*FACTOR_2</td><td>43.471</td><td>4</td><td>10.868</td><td>83.507</td><td>.000</td></tr><tr><td>FACTOR_1*FACTOR_3</td><td>40.197</td><td>2</td><td>20.098</td><td>154.436</td><td>.000</td></tr><tr><td>FACTOR_2*FACTOR_3</td><td>12.444</td><td>2</td><td>6.222</td><td>47.811</td><td>.000</td></tr><tr><td>FACTOR_1*FACTOR_2*FACTOR_3</td><td>8.235</td><td>4</td><td>2.059</td><td>15.819</td><td>.000</td></tr><tr><td>Error</td><td>114.784</td><td>882</td><td>.130</td><td></td><td></td></tr><tr><td>Total</td><td>3183.304</td><td>900</td><td></td><td></td><td></td></tr><tr><td>Corrected total</td><td>1216.914</td><td>899</td><td></td><td></td><td></td></tr></table>

Key: FACTOR\_1: problem size.  
FACTOR\_2: percentage of providers.  
FACTOR\_3: budget constraint.

![](/api/attachments/PTYP6DF3/fulltext/images/a6a38b19ea7e63c99ea8a1f73381492de556ba9448f51cf4cefa65f21d015eb9.jpg)  
Fig. 3. Performance gap: heuristic vs. optimal solution.

This experiment represented a 3 X 3 X 2 factorial design. Each experiment combination was replicated 50 times for a total 900 test cases. The performance of the heuristic algorithm was measured by the performance gap, the percent deviation from the optimal objective value, and the difference in CPU time. An ANOVA for each performance measurement was run to identify significant main factors and interaction effects.

## 3.3.2. The experiment result

Table 6 shows the ANOVA results for the performance gap. All three main factors and multiple-way interaction effects were significant. Among these significant main and interaction effects, the budget constraint had the most explanatory power, accounting for more than 80% of the performance difference between the two solution approaches (750.36 of the 913.32 sum of square errors; an F-value of 5765.73). The number of Web Services and providers also had a good explanatory power, accounting for about 10% of the sum of square errors. The three main and interaction effects were further explored in Fig. 3, in which each line represented the performance gap due to a combination of the percent of service providers (Factor 2) and the budget constraints (Factor 3). Based on the graph, we had the following observations:

1. The heuristic algorithm appeared to be a viable alternative as the heuristic solutions were no more than 5% worse than their optimal counterparts.

2. The quality of the heuristic solutions only deteriorated slightly, on the average of 2%, as the budget became a tight constraint.

3. The general direction of these lines suggested that the performance gap decreased as the problem size increased. However, this was largely due to the increase in the objective value—the denominator in calculating the performance gap.

4. The experiment shows that the difference in performance gap between tight and loose budget constraints decreased from 2.38% to 1.35% while the problem size increased from N = 100/M = 50 to N =1500/M=500. This indicates that the proposed heuristics is less effective when the problem size is small and budget constraint is tight.

5. The heuristic solutions improved only marginally as the percent of service providers increased. Our intuitive interpretation was that more service providers for a service afforded the heuristic algorithm a better chance to improve its solution.

Table 7 shows the analysis of variances for the difference in CPU time. The analysis suggests that problem size (or the number of service services/ providers) was the only significant main factor, accounting for more than 98.8% of the difference in CPU time. The interaction effect between the problem size and percent of service providers was also significant. These were further explored in Fig. 4, in which the two lines represented the average CPU time required for the two approaches with respect to problem sizes. For small-sized problems, the heuristic algorithm required an average of .006 s compared to the average of .055 s needed for the CPLEX. For mid-sized problems, the heuristic required an average of .072 s, and the CPLEX required .646 s. For large-sized problems, the heuristic required an average of 10.69 s while the CPLEX needed an average 88.147 s. This clearly shows the advantage of the heuristic algorithm when the problem size increases.

ANOVA for difference in computational times

<table><tr><td>Source</td><td>Type III sum of squares</td><td>df</td><td>Mean square</td><td>F</td><td>Sig.</td></tr><tr><td>Corrected model</td><td>1,209,096.811(a)</td><td>17</td><td>71,123.342</td><td>144.134</td><td>.000</td></tr><tr><td>Intercept</td><td>609,650.837</td><td>1</td><td>609,650.837</td><td>1235.478</td><td>.000</td></tr><tr><td>FACTOR_1</td><td>1,190,372.292</td><td>2</td><td>595,186.146</td><td>1206.165</td><td>.000</td></tr><tr><td>FACTOR_2</td><td>4887.166</td><td>2</td><td>2443.583</td><td>4.952</td><td>.007</td></tr><tr><td>FACTOR_3</td><td>150.344</td><td>1</td><td>150.344</td><td>.305</td><td>.581</td></tr><tr><td>FACTOR_1*FACTOR_2</td><td>9749.897</td><td>4</td><td>2437.474</td><td>4.940</td><td>.001</td></tr><tr><td>FACTOR_1*FACTOR_3</td><td>461.243</td><td>2</td><td>230.621</td><td>.467</td><td>.627</td></tr><tr><td>FACTOR_2*FACTOR_3</td><td>1162.967</td><td>2</td><td>581.483</td><td>1.178</td><td>.308</td></tr><tr><td>FACTOR_1*FACTOR_2*FACTOR_3</td><td>2312.902</td><td>4</td><td>578.226</td><td>1.172</td><td>.322</td></tr><tr><td>Error</td><td>435,225.971</td><td>882</td><td>493.453</td><td></td><td></td></tr><tr><td>Total</td><td>2,253,973.619</td><td>900</td><td></td><td></td><td></td></tr><tr><td>Corrected Total</td><td>1,644,322.782</td><td>899</td><td></td><td></td><td></td></tr></table>

Key: FACTOR\_1: problem size.  
FACTOR\_2: percentage of providers.  
FACTOR\_3: budget constraint.

![](/api/attachments/PTYP6DF3/fulltext/images/185ffb65bd27c07a2d47159404a838cc69ae4c2532d4b085c71f4fc311f6bb64.jpg)  
Fig. 4. CPU time: heuristic vs. CPLEX.

In all, the experiment suggested that the proposed heuristic algorithm was a viable approach to syndicating Web Services. Its solutions were less than 5% away from the optimum values for all experiment combinations, and its computational time was more than eight folds faster than that of the CPLEX counterparts.

![](/api/attachments/PTYP6DF3/fulltext/images/5065ae47235a08483fd885e0a1d9609b7791f37db8f900a862d8c3b8a58d7d79.jpg)  
Fig. 5. Performance gaps of the QoS sensitivity study.

![](/api/attachments/PTYP6DF3/fulltext/images/081feb4ba4b8a637d9c2d551522475223ae971b8898dd068223cd966170800ac.jpg)  
Fig. 6. Performance gaps of the competitive market study.

## 3.3.3. Sensitivity analyses

As the Web Service market matures and the barrier of entry is reduced, more and more providers are expected to compete in the market. The quality of service of these providers, however, might begin to vary as a result of using quality as a strategic weapon by some providers. In this study, we conducted two sensitivity analyses by changing the parameters in the previous experiment to examine the effectiveness of the proposed algorithm in an environment with an increased competitiveness.

In the first sensitivity study, four groups of test cases were generated to represent a various degree of quality differences among the providers. In the first test group, the QoS of providers was rather uniform, with the quality being within 10% of each other. Then, the quality of these providers began to diverge. The QoS differences were set at 50%, 100%, and 200% for the remaining three test groups. Fifty test cases were replicated for each group. Other parameters were the same as the previous experiment, and the experiment factors were set at the second level.

![](/api/attachments/PTYP6DF3/fulltext/images/358dd2c667798783851454296fabe3dd03f0039d4a286a13885634e02f54ceb0.jpg)  
Fig. 7. Number of services providers selected.

The result was shown in Fig. 5, which depicted an upward trend in the performance gaps between the heuristic and the optimal solutions. The averaged gaps ranged from 1.37% to 2.02%. The Tukey HSD multiple comparison test indicated that, at the 95% confidence interval, there was no statistical difference between the 10% and the 50% test groups. This sensitivity study suggested that the heuristic algorithm performed better in a homogenous quality environment. Although the heuristic still performed well, its quality of solution declined noticeably as the QoS diverged.

In the second sensitivity study, four groups of tests cases were generated to represent the increases in competitiveness in terms of the number of providers in the market. In the first test group, the market was less competitive with only 50 providers offering 500 services. Then, the barrier of entry was gradually lowered with 100, 200, and 400 providers offering the same services for the remaining three test groups. Each test group was also replicated 50 times. Other test conditions were the same as the previous experiment with the experiment factors being set at the second level.

The result of the second sensitivity study was shown in Fig. 6, which depicted a downward trend in performance gaps as the number of providers increased. The Tukey HSD multiple comparison test indicated that, at the 95% confidence interval, there was no statistical difference between 200 and 400 service providers. The performance differences ranged from 1.62% to 3.10%. We then examined the difference in the number of providers selected in both solutions. In a less competitive environment, the number of providers selected in the heuristic solution, as shown in Fig. 7, was of no statistical difference from that in the optimal solution. On the contrary, the number of providers selected began to differ significantly as the competition intensified. In other words, the heuristic algorithm was better at matching the profile of the selected providers in a less competitive environment and was only able to maintain a small performance gap, not necessarily the profile, in a more competitive environment.

## 4. Conclusions

Quality of Web Services has become a prominent issue when more and more services are offered by an ever-increasing number of service providers. Selecting and combining services require intimate knowledge about the offerings in the market and the expertise of evaluating the qualities of these offerings. A Web Service registrar is in the best position to provide such valuable services to its users. In this paper, we explored ways for a QoS and user-driven syndication of Web Services. The application of the AHP and the BG methods made it possible to evaluate the QoA of Web Services and match a customer's quality preferences. In addition, we developed an efficient heuristic method for solving the Web Services syndication problems. Within the parameters tested, the heuristics provided near optimal solutions with significant savings in computing time.

Since this is a preliminary study of the selecting of Web Services based on quality criteria, there is still much to be done for further development and refinement of the modeling and solution methodologies. While being a mathematically proven methodology, AHP entails a time-consuming evaluation process, and the whole evaluation process must take place again whenever new services and service providers are added. Furthermore, the AHP and the GB methodologies cannot accommodate the situation where quality criteria are correlated. Therefore, other multi-criteria decision-making methodologies should be explored to make QoS assessments less labor intensive and more effective. In this study, all data were generated randomly. The study can certainly benefit from using real-life data to validate the model. We also assumed that all data were deterministic, including consumer demands and qualities of the services. In future research, this assumption may be relaxed and revisited.

## References

[1] M. Agrawal, K. Chari, S. Seshadri, A Methodology for Business Process Integration of Legacy Systems using Web Services, The Third Workshop on e-Business, Washington, DC, 2004.

[2] R. Akkiraju, D. Flaxer, H. Chang, T. Chao, L.-J. Zhang, F. Wu, J.-J. Jeng, A Framework for Facilitating Dynamic e-Business Via Web Services, Proceedings of the Workshop on Object-Oriented Web Services, Tampa, FL, 2001.

[3] W. Andrews, Predicts 2004: Web Services, 2003, Gartner Research, 2003.

[4] A. Arbel, S.S. Oren, Generating search directions in multiobjective linear programming using the hierarchy process, Socioeconomic Planning Sciences 20 (1986) 369–373.

[5] Y. Babich, Composition of Web Services and QoS Aspects, http://www-i4.informatik.rwth-aachen.de/content/teaching seminars/sub/2003\_2004\_ws\_docs/WebServices.pdf, 2004.

[6] P.A Brown, D.F. Gibson, A quantified model for facility site selection—application to multiplant location problem, AIIE Transactions 4 (1) (1972) 1–10.

[7] J. Canada, W. Sullivan, Economic and Multiattribute Evaluation of Advanced Manufacturing Systems, Prentice Hall, 1989

[8] J. Cardoso, A. Sheth, J. Millerb, J. Arnoldc, K. Kochutb, Quality of service for workflows and web service processes, Journal of Web Semantics: Science, Services and Agents on the World Wide Web 1 (2004) 281–308.

[9] J.S. Dyer, Remarks on the analytic hierarchy process, Management Science 36 (1990) 249–258.

[10] Expert Choice, http://www.expertchoice.com, 2004.

[11] X. Gao, J. Yang, M.P. Papazoglou, The Capability Matching of Web Services, Proceedings of IEEE 4th International Symposium on Multimedia Software Engineering, Newport Beach, CA, 2002.

[12] M.R. Garey, D.S. Johnson, Computers and Intractability: A Guide to the Theory of NP—Completeness, W. H. Freeman and Company, New York, NY, 1979.

[13] M. Gilpin, Who Has How Many Web Services? Forrester Research, 2004.

[14] K. Gottschalk, S. Graham, H. Kreger, J. Snell, Introduction to Web Services Architecture, IBM Systems Journal 41 (2) (2002) 170–177.

[15] P.T. Harker, I. Miller, Global effective questioning in the analytic hierarchy process, European Journal of Operational Research 48 (1990) 88–97.

[16] S. Kalepu, S. Krishnaswamy, S.W. Loke, Verity: A QoS Metric for Selecting Web Services and Providers, Proceedings of the First Web Services Quality Workshop, Rome, Italy, 2003.

[17] C. Lau, A. Ryman, Developing XML Web Services with WebSphere Studio Application Developer, IBM Systems Journal 41 (2) (2002) 178–197.

[18] M.A. Maurino, J.T. Luxhøj, Analysis of a Group Decision Support System (GDSS) for Aviation Safety Risk Evaluation, Rutgers University, New Brunswick, NJ, 2002.

[19] T. Niko, K. Shanika, Automatic Measurement of a QoS Metric for Web Service Recommendation, Proceedings of Australian Software Engineering Conference, Brisbane, Australia, 2005.

[20] M. Paolucci, T. Kawamura, T. Payne, K. Sycara, Semantic Matching of Web Services Capabilities, Proceedings of International Semantic Web Conference, Sardinia, Italy, 2002.

[21] J. Perez, Some comments on Saaty's AHP, Management Science 41 (1995) 1091–1995.

[22] D.A. Petee, P.J. Componation, Development of a Systems Engineering Training Plan at the U.S. Navy's Coastal Systems Station, Systems Engineering 5 (2) (2002) 156–163.

[23] S.R. Ponnekanti, A.S. Fox, A Developer Toolkit for Web Service Composition, Proceedings of the Eleventh World Wide Web Conference, Honolulu, HI, USA, 2002.

[24] M. Punniyamoorthy, P. Vijaya Ragavan, Justification of Automatic Storage and Retrieval System (AS/RS) in a heavy engineering industry, The International Journal of Advanced Manufacturing Technology 26 (5) (2005) 653–658.

[25] H. Rachid, B. Boualem, A Petri Net based Model for Web Service Composition, Proceedings of the Fourteenth Australasian Database Conference on Database Technologies, Adelaide, Australia, 2003.

[26] V.S.R. Ramakrishnan, Web Services: OR's newest ally? OR/MS Today 28 (6) (2001) 37–39.

[27] T.L. Saaty, The Analytic Hierarchy Process, McGrawHill, New York, NY, 1980.

[28] T.L. Saaty, Axiomatic Foundation of the Analytic Hierarchy Process, Management Science 32 (1986) 841–855.

[29] T.L. Saaty, L.G. Vargas, The Logic of Priorities, Kluwer Nijhoff Publishing, Massachusetts, 1982.

[30] J.P. Shim, Bibliographical research on the analytic hierarchy process, Socio-economic Planning Sciences 23 (1989) 161–167.

[31] A. Stam, A.P.D. Silva, Stochastic judgments in the AHP: the measurement of rank reversal probabilities, Decision Sciences 28 (1997) 655–688.

[32] X. Su, J. Rao, A Survey of Automated Web Service Composition Methods, Proceedings of First International Workshop on Semantic Web Services and Web Process Composition, San Diego, CA, USA, 2004.

[33] Y. Sun, G. Koehler, A location model for a web service intermediary, Decision Support Systems 42 (2006) 221–236.

[34] M. Tian, A. Gramm, T. Naumowicz, H. Ritter, J. Schiller, A Concept for QoS Integration in Web Services, Proceedings of IEEE Computer Society 1st Web Services Quality Workshop, Rome, Italy, 2003.

[35] L.G. Vargas, An overview of the analytic hierarchy process, European Journal of Operational Research 48 (1990) 2–8.

[36] H. Xu, Understanding Web Services Adoption: An Exploratory Study, The Third Workshop on E-Business, Washington, DC, 2004.

[37] L. Zeng, B. Benatallah, M. Dumas, J. Kalagnanam, Q.Z. Sheng, Quality Driven Web Services Composition, Proceedings of The Twelfth International World Wide Web Conference, Budapest, Hungary, 2003.

![](/api/attachments/PTYP6DF3/fulltext/images/edf8d94c7e126a2a2305f4d803b3b87a19c6a35cbd024881064f7ad453b947cb.jpg)  
<sup>Dr. Yi Sun</sup> is an Assistant Professor of Information Systems at the School of Business, California State University San Marcos. His degrees include BA degree from Foreign Affairs College in Beijing, China and PhD (Management Information Systems) from University of Florida. He has research interests in telecommunications, data mining and artificial intelligence, electronic commerce, and applied operations research.

![](/api/attachments/PTYP6DF3/fulltext/images/b04721d57215a0590f8b77ce8fb32681d1f09b790560e932b4235d127a17dd25.jpg)

<sup>Dr. Shaoyi He</sup> is currently an Associate Professor of Information Systems in the School of Business Administration at California State University San Marcos in the United States. He received his PhD from the University of North Carolina at Chapel Hill in 1998. Since then, he has worked as a faculty member in Long Island University, Pennsylvania State University, and California State University San Bernardino. His current research interests include interplay of technology, culture and language in global e-

business, multilingual information access and retrieval on the Web, multilingual issues in e-commerce website glocalization, and language barriers in marketing across cultures. He has published papers in such academic journals as Journal of the American Society for Information Science, Information Processing and Management, Journal of Information Communication and Library Science, Electronic Library, and Journal of China Society for Scientific and Technical Information.

![](/api/attachments/PTYP6DF3/fulltext/images/ca17e5ef4382adc79e3cb31255e06c88e603b2365e761849f8c1db61b446bde2.jpg)

<sup>Dr.</sup> <sup>Jack</sup> <sup>Leu</sup> is a Professor of Operations and Information Systems at California State University San Marcos. He has served as the department chair and the graduate program director. His teaching interests include Database, Networking, Programming, and Operations Management. His current research focuses on Web Services and Internet Gaming Strategy. He has published articles in journals such as Decision Sciences, IIE Transac-

tions, International Journal of Production Research, and Annals of Operations Research.
