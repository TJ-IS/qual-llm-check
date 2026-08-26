---
otero_id: 14326
otero_key: "CUBVGY63"
title: "Design and Analysis of Contracts for Software Outsourcing"
authors: "Debabrata Dey; Ming Fan; Conglei Zhang"
year: "2010"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0223"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.122.253.212] On: 23 May 2015, At: 02:59 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## 6SR

## Information Systems Research

![](/api/attachments/CUBVGY63/fulltext/images/221355c1a979a5deff9bd4604bdf5cedf0306f4709dc3eeded53ffbd7d17719c.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Design and Analysis of Contracts for Software Outsourcing

Debabrata Dey, Ming Fan, Conglei Zhang,

## To cite this article:

Debabrata Dey, Ming Fan, Conglei Zhang, (2010) Design and Analysis of Contracts for Software Outsourcing. Information Systems Research 21(1):93-114. http://dx.doi.org/10.1287/isre.1080.0223

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2010, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/CUBVGY63/fulltext/images/ba47d8e577a4fac427d351f28e77e49aeed39f18106055a37cf8c9e1522e0b31.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Design and Analysis of Contracts for Software Outsourcing

Debabrata Dey, Ming Fan, Conglei Zhang

Department of Information Systems and Operations Management, Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195 {ddey@u.washington.edu, mfan@u.washington.edu, conglei@u.washington.edu}

utsourcing of software development allows a business to focus on its core competency and take advantage of vendors’ technical expertise, economies of scale and scope, and their ability to smooth labor demand fluctuations across several clients. However, contracting a software project to an outside developer is often quite challenging because of information asymmetry and incentive divergence. A typical software developmen contract must deal with a variety of interrelated issues such as the quality of the developed system, the timeliness of delivery, the effort and cost associated with the project, the contract payment, and the postdelivery software support. This paper presents a contract-theoretic model that incorporates these factors to analyze how software outsourcing contracts can be designed. We find that despite their relative inefficiency, fixed-price contracts are often appropriate for simple software projects that require short development time. Time-and-materials contracts work well for more complex projects when the auditing process is efficient and effective. We also examine a type of performance-based contract called quality-level agreement and find that the first-best solution can be reached with such a contract. Finally, we consider profit-sharing contracts that are useful in situations where the developer has more bargaining power.

Key words: contract design; software engineering; software outsourcing; performance-based contracts History: Paulo Goes, Senior Editor; Ram Gopal, Associate Editor. This paper was received on October 20, 2006, and was with the authors 9 <sup>1</sup> months for 3 revisions. Published online in Articles in Advance May 12, 2009.

## 1. Introduction

Outsourcing of software development projects has become a popular practice over the last two decades. Outsourcing allows a business to focus on its core competency and take advantage of a vendor’s technical expertise and economies of scale and scope (Lichtenstein 2004). Furthermore, by outsourcing the development of software, the client can avoid hiring a large development staff, most of whom will have little value after the system is developed, tested, and deployed. A software vendor, on the other hand, usually works for several clients and can easily smoothen such labor demand fluctuations.

Contracting a software project to an outside developer, however, can be quite challenging because of the presence of information asymmetry and incentive divergence (Gopal et al. 2003). A typical software development contract must deal with a variety of closely related issues such as the quality of the developed system, the timeliness of delivery, the effort and cost associated with the project, and the support agreement. The objective of this research is to develop a contract-theoretic model that incorporates these factors and analyzes the performance of different software outsourcing contracts. We first examine the two most common contract forms used in practice, namely fixed-price and time-and-materials contracts (Bajari and Tadelis 2001, Lichtenstein 2004). In a fixed-price contract, a predetermined price is paid to a developer for a specific software system. On the other hand, a time-and-materials contract, also known as a cost plus contract, requires the client to pay the vendor the development cost plus a profit. Subsequently, we analyze performance-based contracts (Phillips 2006, Reddy 2003). In these contracts, the payoff to the developer is tied to the overall quality and performance of the software, which can provide more incentives to the developers. Finally, we examine contracts negotiated using a bargaining game; these contracts are useful in situations where the outsourcing market is not competitive because, for example, the developer possesses a patented technology or a rare expertise.

Our model draws insights from software outsourcing practices and extends prior contracting literature. We model a software outsourcing project with the following characteristics: First, we follow software engineering literature and software development economics to model software project value, quality, and cost (Boehm 1981, Pressman 2005). In modeling the value and cost of software projects, we can categorize software projects into different types, which provide insights in analyzing the corresponding contract performance. Second, we look at software outsourcing as a problem that not only has asymmetric information coupled with moral hazard (Laffont and Tirole 1993) but also involves a great deal of uncertainty. A developer usually has information about the development effort that the client lacks and may not have the right incentive to invest optimal effort for the project. Moreover, software projects usually involve large uncertainties in system requirements as well as the development process. We evaluate the performance of different contracts and develop mechanisms to lower risks and mitigate information asymmetry and moral hazard problems. We find that, despite their relative inefficiency, fixed-price contracts are quite appropriate for software projects that are simple and require short development time. Time-and-materials contracts can help alleviate the problems of information asymmetry and moral hazard but require monitoring of project progress and effort. Our result suggests that this type of contract works well for more complex projects when the auditing process is efficient and effective. Third, we recognize that software quality is often difficult to evaluate at the time of release (Kalnins and Mayer 2004) and usually takes some time for the client to learn while the system is being used. We examine a type of performance-based contract called a qualitylevel agreement that ties the client payoff to the eventual quality of the software. We find that this contract form can achieve the first-best quality level. Finally, we consider contracts negotiated under a bargaining game. We find that this contract form can also achieve the first-best solution.

The rest of the paper is organized as follows. We review literature and draw insights from realworld software outsourcing contracts in §2. We set up the basic model and analyze fixed-price and time-and-materials contracts in §3. Section 4 analyzes performance-based contracts. Contracts negotiated using a bargaining game are discussed in §5. Section 6 discusses the results and implications of this study. Concluding remarks and future research directions are offered in §7. Proofs of all propositions, corollaries, and lemmas are provided in Appendix A. Appendix B furnishes the details of the real-world contracts examined by us.

## 2. Prior Literature and Industrial Practices

There has been a growing research interest on software and information technology (IT) outsourcing in the information systems literature. Whang (1992) formulates a viable software contract for external software development that can achieve the same results as in-house development. There, the software development is composed of multiple phases and the uncertainties about the costs are progressively resolved as the project advances. The project could be abandoned at the end of each stage based on a costbenefit analysis at that stage. Wang et al. (1997) find that high uncertainty about the development costs makes outsourcing less attractive. Choudhury and Sabherwal (2003) examine the dynamics of different control mechanisms and find that more complex control mechanisms are used when performance problems begin to occur. Gopal et al. (2003) conduct an empirical study on offshore software outsourcing and find that the contract choice significantly determines the project profit. Koh et al. (2004) study obligations from both customers’ and suppliers’ perspective in IT outsourcing. Lee et al. (2004) find that IT outsourcing strategies strongly affect outsourcing success.

In economics, contract theory has been an active research area (e.g., Laffont and Tirole 1993, Laffont and Martimort 2002). Theoretical contract literature has examined risk allocation (Cheung 1969), moral hazard (Grossman and Hart 1983), and measurement and enforcement costs (Allen and Lueck 1993). Bajari and Tadelis (2001) study contract choices in the construction industry and find that a time-and-materials contract is preferred to a fixed-price contract when the project is more complex. Kalnins and Mayer (2004) empirically study contracts in the IT services industry; they find that a time-and-materials contract is preferred when the cost of measuring quality ex post is high.

Despite the vast literature in contracting, the issues related to contract choice and performance for software projects remain largely unclear. Because of the high complexity in software engineering processes, software outsourcing contracts pose many unique challenges that are usually not seen in contracts in other industries. Incomplete requirement specification and difficulty in quality assessment are only two of these challenges. These problems could make a fixedprice contract difficult to manage by often incurring significant cost overruns from change requests. However, there is little research that provides clear understanding and guidance on the choice and performance of outsourcing contracts.

We aim to study this problem at a project level by modeling the characteristics of a software project based on established theories and practices in software engineering. To ensure that our model captures the unique aspects of software contracts, we have collected and carefully studied a set of 15 real-world software outsourcing contracts. Our examination of these contracts suggests that the following factors are important in the outsourcing process.

## Project Type

• Project type, especially the complexity of the project, is a major factor affecting the contractual relationship. A project that is mission critical to a client company usually requires higher effort from the developer, and clients often prefer to include detailed project specifications and requirements in the contract.

## Project Uncertainties

• There are different types of uncertainties in software outsourcing. For example, project requirement and scope may not be clear at the contract initiation stage. Project uncertainties may increase with the overall complexity of the project.

## Project Delivery Time and Milestones

• A complex system usually requires longer time to complete; a shorter delivery time often indicates a simpler project. The timeline of a project can affect payment terms. Also, a contract may specify project deliverables in terms of milestones. Sometimes the client may tie payment terms with project milestones.

## Software Support

• Most of the contracts require some warranty and support after the software is delivered. Usually, a developer is required to correct the defects for a prenegotiated duration after deployment.

## Client Knowledge

• Clients with greater knowledge and sophistication in IT and software development are likely to specify the contracts in more detailed terms.

## Measurability of Project Quality

• This refers to performance standard and metrics to measure project success. If companies can clearly define various quality measures, they are likely to write detailed contracts with those measures.

Furthermore, we observe that in addition to the traditional fixed-price and time-and-materials contracts, companies do use performance-based contracts. In a performance-based contract, a developer’s compensation is tied to the quality of the software. We also observe that companies sometimes use profit-sharing contracts, where the payment to the developer is tied to the revenue the software generates. Both of these contract forms have received little attention in software contracting literature. In this research, we incorporate into our analytical model the insights derived from examining real-world contract documents and analyze the performance of various types of contracts.

## 3. Analysis of Traditional Contracts

In this section, we analyze the two most common types of contracts, namely fixed-price and time-andmaterials contracts. We introduce the basic notation and model setup, derive the first-best solution, and use it as a benchmark to compare the two types of contracts. Following prior literature (Gopal et al. 2003), we use contract profit or surplus to measure the performance or the efficiency of a contract.

## 3.1. Model Setup

The events and their timing associated with an outsourcing contract can be summarized as follows: After the contract is negotiated and signed, the project is launched. The developer or the client, depending on the particular contract form, determines the release time t for the project. The developer then chooses the appropriate effort level e. After the project is completed, the quality of the software q is realized and the software is released to the client. A monetary payment P is transferred from the client to the developer who absorbs the actual development and subsequent support costs; see Figure 1.

Figure 1 Timing of the Model  
![](/api/attachments/CUBVGY63/fulltext/images/0af9d8d058115aabaaad220fc07a7224bc2489beb55207b0f68f273cb27fa32f.jpg)

We model software quality q as a function of effort e and time t. We assume that it follows a Cobb-Douglas functional form:

$$
q = e ^ {\alpha} t ^ {\beta} + \varepsilon ,
$$

where $\alpha + \beta < 1$ and  is the uncertainty associated with software quality. The restriction $\alpha + \beta < 1$ signifies a decreasing return to scale and is motivated by the observation that it becomes increasingly more difficult to improve the quality of the software product. We model  as a random variable with $\operatorname { E } ( \varepsilon ) = 0$ We assume that the effort e and quality q are private information of the developer and are not directly observable by the client.

The utility of the software product to the client increases with the quality of the software and decreases as the project release is delayed. We assume that the client, as well as the developer is risk neutral. Thus, the total expected utility of the client can be expressed as

$$
U = \operatorname{E} [ u _ {1} q - u _ {2} t ] = u _ {1} e ^ {\alpha} t ^ {\beta} - u _ {2} t,
$$

where $u _ { 1 }$ and $u _ { 2 }$ are the client’s sensitivity to quality and project release time, respectively. The first parameter $u _ { 1 }$ represents the client’s valuation of the software product and is closely related to the features and complexity of the product. The second parameter $u _ { 2 }$ represents the opportunity cost of delayed release.

The total cost for the developer has the following three parts: the direct development cost $( C _ { 1 } ) _ { \cdot }$ the support cost $( C _ { 2 } ) _ { \cdot }$ , and the cost related to the project duration $( C _ { 3 } )$ . The direct development cost incurred by the developer includes mainly wages and is proportional to the total effort: $C _ { 1 } = c _ { 1 } e$ . The total support cost incurred by the developer is modeled as $C _ { 2 } = c _ { 2 } ( q _ { 0 } - q ) , \ q \leq q _ { 0 } ,$ , where $q _ { 0 }$ is a constant and $c _ { 2 }$ is the developer’s cost sensitivity to product quality. The support cost captures the fact that lower quality software will incur a higher support cost.

The third component represents the cost associated with the duration of the project. Expediting a project to a date earlier than its normal completion date is also referred to as project crashing in the project management parlance (Gray and Larson 2007). We model the cost associated with releasing the product at time t as $C _ { 3 } = c _ { 3 } ( g - t )$ , where $g$ is the normal completion time. This is consistent with software project management practices that crashing a project $( t < g )$ places a heavy demand on tight resources and should increase the cost. On the other hand, if the release is postponed beyond the normal completion date $( t > g )$ then the developer gains flexibility afforded by lesser demand on the resources (Pressman 2005). We assume that the benefit to the developer from this flexibility is less than the disutility to the client from delaying the release, i.e., $c _ { 3 } < u _ { 2 } ;$ otherwise, the social optimum would degenerate to the trivial case, where the release of the software is postponed indefinitely.

We now turn our attention to the normal completion time of a project. In software engineering, this normal completion time is estimated as a function of the overall effort (Boehm 1981): $g = 2 . 5 e ^ { \mu }$ , where  varies from 0.32 to 0.38 depending on the project type. A closer examination of this relationship reveals that as long as the project size is not very small, the relationship is close to a linear one and can be approximated quite well by a piecewise linear function. For the sake of simplicity, in this work, we model the normal completion time g as a linear function of effort: $g = a + h e$

Now, the overall expected cost to the developer can be expressed as a total of these various costs as

$$
\begin{array}{r l} & C = \operatorname{E} [ c _ {1} e + c _ {3} (a + h e - t) + c _ {2} (q _ {0} - q) ] \\ & \quad = (c _ {1} + c _ {3} h) e - c _ {2} e ^ {\alpha} t ^ {\beta} - c _ {3} t + (c _ {2} q _ {0} + c _ {3} a). \end{array}\tag{1}
$$

Two points need further elaboration. First, we simply add the three different costs without discounting them even though they are typically incurred at different time points. This is because we assume that the cost parameters $( c _ { 1 } , \ c _ { 2 } ,$ and $c _ { 3 } )$ in the model already account for the necessary discounting. Second, note that the term $( c _ { 2 } q _ { 0 } + c _ { 3 } a )$ in Equation (1) is a constant that simply increases the cost, thereby decreasing the expected profit by a constant amount. Therefore, it does not change the solution, and hereafter we exclude it from the model without any loss of generality. As a result, the expected profit for the developer can be expressed as

$$
\pi_ {D} = P - C = P - (c _ {1} + c _ {3} h) e + c _ {2} e ^ {\alpha} t ^ {\beta} + c _ {3} t,
$$

where $P$ is the contract payment for the developer. The client’s expected profit is given by

$$
\pi_ {C} = U - P = u _ {1} e ^ {\alpha} t ^ {\beta} - u _ {2} t - P.
$$

We now model the first-best problem (FBP) by maximizing the total expected profit:

$$
\begin{array}{r} \max _ {e, t} \Pi = \pi_ {C} + \pi_ {D} = (u _ {1} + c _ {2}) e ^ {\alpha} t ^ {\beta} \\ - (u _ {2} - c _ {3}) t - (c _ {1} + c _ {3} h) e. \end{array}\tag{2}
$$

Proposition 1. The optimal effort and release time for the FBP in Equation (2) are

$$
e _ {b} = \left[ (u _ {1} + c _ {2}) \left(\frac {\beta}{u _ {2} - c _ {3}}\right) ^ {\beta} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {1 - \beta} \right] ^ {1 / (1 - \alpha - \beta)},\tag{3}
$$

and

$$
t _ {b} = \left[ \left(u _ {1} + c _ {2}\right) \left(\frac {\beta}{u _ {2} - c _ {3}}\right) ^ {1 - \alpha} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {\alpha} \right] ^ {1 / (1 - \alpha - \beta)}.\tag{4}
$$

The proofs of this and all the subsequent propositions, corollaries, and lemmas are provided in Appendix A.

The comparative statics of the optimal effort and release time are summarized in Table 1. We find that if the client places a higher value on the software quality, i.e., $u _ { 1 }$ is higher, the finished software product requires more effort and time and hence would be of a higher quality. If the software is required soon, as represented by a higher $u _ { 2 } ,$ it would be of a lower quality, requiring less effort and time. If the software is costly to develop, i.e., $c _ { 1 }$ is high, then less effort would be allocated to this project and it would have a shorter release time. If, on the other hand, the software is less costly to develop, $\mathrm { i . e . , } \ c _ { 1 }$ is low, more effort would be expended on the project, because the marginal cost of effort is low. With a higher $c _ { 2 } ,$ which indicates a higher support cost, the software project would take more effort and longer time to develop, and eventually the product would be of higher quality. Under the optimal effort and release time, we can find the expected first-best quality level $q _ { b } = e _ { b } ^ { \alpha } t _ { b } ^ { \beta }$ . Substituting Equations (3) and (4) into Equation (2), we have the following total surplus or social welfare for the FBP:

Table 1 Comparative Statics of the First-Best Solution

<table><tr><td>Parameters</td><td> $e_b$ </td><td> $t_b$ </td></tr><tr><td> $u_1$ </td><td>+</td><td>+</td></tr><tr><td> $u_2$ </td><td>-</td><td>-</td></tr><tr><td> $c_1$ </td><td>-</td><td>-</td></tr><tr><td> $c_2$ </td><td>+</td><td>+</td></tr><tr><td> $c_3$ </td><td>+, if  $\beta c_1 - h[(1-\beta)u_2 - c_3] > 0,$  $-, otherwise$ </td><td>+, if  $(1-\alpha)c_1 - h(\alpha u_2 - c_3) > 0,$  $-, otherwise$ </td></tr></table>

$$
\Pi_ {b} = (1 - \alpha - \beta) \left[ \left(u _ {1} + c _ {2}\right) \left(\frac {\beta}{u _ {2} - c _ {3}}\right) ^ {\beta} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {\alpha} \right] ^ {1 / (1 - \alpha - \beta)}.
$$

We use $\Pi _ { b }$ as a benchmark in the rest of the paper.

## 3.2. Fixed-Price Contract

We now examine the performance of a fixed-price contract in which the payment from the client to the developer is $P = F - p t ,$ where F is the fixed payment and $p$ is the delay penalty per unit time (Bajari and Tadelis 2001). The sequence of events follows the structure of a Stackelberg game, where the client as the Stackelberg leader chooses F and $p ,$ and the developer follows by choosing the effort level e and the release time t. The developer’s problem is

$$
\max _ {e, t} \pi_ {D} = F - p t - (c _ {1} + c _ {3} h) e + c _ {2} e ^ {\alpha} t ^ {\beta} + c _ {3} t.\tag{5}
$$

Now, we examine the client’s problem. Let $v ^ { \prime }$ be the actual reservation value of the developer, and let $v = v ^ { \prime } + ( c _ { 2 } q _ { 0 } + c _ { 3 } a )$ be the adjusted reservation price.<sup>1</sup> Now, because the contract must satisfy the individual rationality condition for the developer, the optimal contract for the client can be obtained by solving

$$
\begin{array}{l l} \max _ {F, p} & \pi_ {C} = - F + p t + u _ {1} e ^ {\alpha} t ^ {\beta} - u _ {2} t \\ \text {s.t.} & \pi_ {D} (e, t) \geq v. \end{array}\tag{6}
$$

We denote the equilibrium contract solution as $( F _ { f } , p _ { f } )$ and developer’s best response as $( e _ { f } , t _ { f } )$ . The equilibrium fixed-price contract and developer’s strategy are derived as follows:

Proposition 2. The contract $P _ { f } = ( F _ { f } , p _ { f } )$ and developer’s choice of effort and release time $( e _ { f } , t _ { f } )$ constitute a

Nash equilibrium, where $F _ { f } , p _ { f } , e _ { f } ,$ , and $t _ { f }$ are given by

$$
\begin{array}{c} F _ {f} = p _ {f} t _ {f} - c _ {2} e _ {f} ^ {\alpha} t _ {f} ^ {\beta} - c _ {3} t _ {f} + (c _ {1} + c _ {3} h) e _ {f} + v, \\ p _ {f} = c _ {3} + \frac {c _ {2} (1 - \alpha) (u _ {2} - c _ {3})}{c _ {2} (1 - \alpha) + u _ {1}}, \\ e _ {f} = \left[ c _ {2} \left[ \left(1 + \frac {u _ {1}}{c _ {2} (1 - \alpha)}\right) \frac {\beta}{u _ {2} - c _ {3}} \right] ^ {\beta} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {1 - \beta} \right] ^ {1 / (1 - \alpha - \beta)}, \\ a n d \\ t _ {f} = \left[ c _ {2} \left[ \left(1 + \frac {u _ {1}}{c _ {2} (1 - \alpha)}\right) \frac {\beta}{u _ {2} - c _ {3}} \right] ^ {1 - \alpha} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {\alpha} \right] ^ {1 / (1 - \alpha - \beta)}. \end{array}
$$

Now, consider the situation where the client (instead of the developer) determines and insists on a release time t. The payment from the client to the developer is $P = F$ . The developer chooses effort level e. We have the following result:

Corollary 1. The performance of the fixed-price contract, in which the client determines the release time t, is equivalent to that of the fixed-price contract with the release time determined by the developer.

Corollary 1 suggests that under a fixed-price contract, the equilibrium is not affected by whether the client or the developer determines the release time. When the developer determines the release time, the client simply finds the right delay penalty for the developer to choose a specific release time.

The total social welfare under the fixed-price contract can be calculated as

$$
\begin{array}{c} \Pi_ {f} = (1 - \alpha - \beta) \bigg [ c _ {2} \bigg (\frac {1 - \alpha + u _ {1} / c _ {2}}{1 - \alpha} \bigg) ^ {1 - \alpha} \\ \cdot \bigg (\frac {\beta}{u _ {2} - c _ {3}} \bigg) ^ {\beta} \bigg (\frac {\alpha}{c _ {1} + c _ {3} h} \bigg) ^ {\alpha} \bigg ] ^ {1 / (1 - \alpha - \beta)}. \end{array}
$$

Therefore, the total social welfare under the fixedprice contract is strictly lower than that under the first-best solution, $\Pi _ { b } ,$ , with the gap being

$$
\begin{array}{l} \Delta \Pi = \Pi_ {b} - \Pi_ {f} \\ = (1 - \alpha - \beta) \left[ \left(u _ {1} + c _ {2}\right) ^ {1 / (1 - \alpha - \beta)} - \left[ c _ {2} \left(1 + \frac {u _ {1}}{c _ {2} (1 - \alpha)}\right) ^ {1 - \alpha} \right] ^ {1 / (1 - \alpha - \beta)} \right] \\ \cdot \left[ \left(\frac {\beta}{u _ {2} - c _ {3}}\right) ^ {\beta} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {\alpha} \right] ^ {1 / (1 - \alpha - \beta)}. \end{array} \tag {7}
$$

It is easy to see that $\Delta \Pi > 0 .$ . Comparing the results of the fixed-price contract with those of the FBP, we have the following result:

Proposition 3. (i) Under a fixed-price contract, the developer would invest lower effort and less time compared to the first-best solution, resulting in a lower expected software quality. (ii) The performance gap between a fixedprice contract and the first-best solution increases in $u _ { 1 }$ and decreases in $u _ { 2 }$

Proposition 3 suggests that under a fixed-price contract, the developer does not have an incentive to provide development effort and time at an optimal level. This is the underlying reason why a fixedprice contract performs less efficiently. Furthermore, the performance gap between a fixed-price contract and the first-best solution increases in $u _ { 1 }$ . This suggests that these contracts are not appropriate for complex projects that usually have a high quality requirement. For simpler projects, however, the performance gap narrows and a fixed-price contract may be appropriate.

We illustrate the result in Proposition 3 with the help of Figure 2, which plots effort and release time as functions of $u _ { 1 }$ and $u _ { 2 }$ We use the following parameter values for this illustration: $\alpha = 0 . 4 , \beta = 0 . 4 ,$ $c _ { 1 } = 3 , \ c _ { 2 } = 2 , \ c _ { 3 } = 0 . 5 ,$ and $h = 0 . 0 4$ . In Figures 2(a) and 2(b), $u _ { 2 } = 2 ,$ , and in Figures 2(c) and 2(d), $u _ { 1 } = 4$ First, as indicated in Proposition 3, both effort and release time under fixed-price contracts are below the first-best levels. As the demand for software quality increases or the software becomes more complex $( \mathrm { i . e . , }$ $u _ { 1 }$ increases), the effort and release time gaps between FBP and fixed-price contracts increase. The effort-level difference between the two cases is large because a fixed-price contract provides only weak incentives to the developer. We can also see from Figure 2 that for projects with a stricter release time, effort level decreases and projects are released earlier. When the client prefers a faster release $\left( \mathrm { i . e . , ~ } u _ { 2 } \right.$ is higher), the effort and release time gaps between FBP and fixedprice contracts become smaller.

## 3.3. Time-and-Materials Contract

We now analyze time-and-materials contracts in which the client is charged based on the time and effort incurred by the developer. Let e be the effort

## Figure 2 Effort and Release Time as Functions of $u _ { 1 }$ and $u _ { 2 }$

(a) Effort vs. u<sub>1</sub>  
![](/api/attachments/CUBVGY63/fulltext/images/1cdc8e934ad4c146a7d4c776c9ac96ef2baea08a612c833630bd576c5a0d9ce3.jpg)

(c) Effort vs. $u _ { 2 }$  
![](/api/attachments/CUBVGY63/fulltext/images/b0e7e8d049acc109411b95dca8d649bd76b08a2d35e8f204526f71e9fe960510.jpg)  
reported by the developer. We consider a contract form where the payment from the client to the developer is expressed as $\boldsymbol { P } = \boldsymbol { F } + p _ { 1 } \boldsymbol { \hat { e } } - p _ { 2 } \boldsymbol { t } ,$ where $F$ is the fixed part of the payment. The developer chooses the real effort level $e ,$ the release time $t ,$ and the reported effort level ${ \hat { e } } .$ Although t is directly observable, the real effort level $e$ is not. Therefore, the client usually resorts to auditing the developer to verify the reported effort level. The auditing process, of course, is imperfect in the sense that the real effort $e$ can never be fully verified against the reported level ${ \hat { e } } .$ Instead, the client could collect evidence of inflation in the reported effort. As the inflation level $d = \hat { e } - e$ increases, the probability that the client could detect this inflation also increases. To model the detection probability, we introduce two

(b) Release time vs. u<sub>1</sub>  
![](/api/attachments/CUBVGY63/fulltext/images/686a9e53683bd88a15eb34e88b247a4c2a5490fba436305fb6eb8dadbf9a6e63.jpg)

(d) Release time vs. $u _ { 2 }$  
![](/api/attachments/CUBVGY63/fulltext/images/0a3ee943ba45515d1687b5dd5055cd8f33d5b62998bc4b4cf46f6c7430bb95bd.jpg)  
parameters: an auditing policy parameter $\phi$ and an auditing effectiveness parameter \$. The policy parameter $\phi \in [ 0 , 1 ]$ simply indicates the level of auditing effort; a higher value of $\phi$ means that the client would audit a larger number of documents or monitor a larger number of process, thereby increasing the detection probability. The auditing cost to the client is expressed as a linear function of the auditing policy $C _ { a } ( \phi ) = w \phi$ , where w is a constant. The effectiveness parameter $\theta \in \left[ 0 , 1 \right]$ , on the other hand, measures the ability of the client to unearth irregularities when they exist; it depends on the ability and experience of the personnel doing the auditing. The higher the value of $\theta ,$ the higher the effectiveness of the client’s audit team and, hence, the higher the detection probability.

Assuming that a developer would never underreport the effort level $( \mathrm { i . e . , } d \geq 0 )$ , the detection probability is modeled as

$$
\rho (d) = \left\{ \begin{array}{l l} \theta \phi d, & \text { if } 0 \leq d <   1 / (\theta \phi), \\ 1, & \text { if } d \geq 1 / (\theta \phi). \end{array} \right.
$$

When $d > 1 / ( \theta \phi )$ , the client can surely tell that the developer has inflated his effort level and would, therefore, impose a fine. Thus, it is in the developer’s interest not to report an effort level exceeding e by more than $1 / ( \theta \phi )$ . The expected payment to the developer, therefore, is $\boldsymbol { P } = \boldsymbol { F } + p _ { 1 } \boldsymbol { \hat { e } } - p _ { 2 } \boldsymbol { t } - \theta \phi d s ,$ , where s is the penalty for cheating.<sup>2</sup>

The game proceeds as follows: The client first decides the auditing policy # and the contract payment terms $\mathrm { - } F , p _ { 1 } ,$ and $p _ { 2 }$ . The developer then decides the effort $e ,$ reported effort $\hat { e } ,$ and release time t. Hence, the developer’s problem is

$$
\begin{array}{r} \max _ {e, \hat {e}, t} \pi_ {D} = F + p _ {1} (e + d) - p _ {2} t - \theta \phi d s \\ - (c _ {1} + c _ {3} h) e + c _ {2} e ^ {\alpha} t ^ {\beta} + c _ {3} t. \end{array}\tag{8}
$$

Now, the incentive-compatible condition for the developer not to cheat is simply (Myerson 1979)

$$
\frac {\partial \pi_ {D}}{\partial d} = p _ {1} - \theta \phi s \leq 0.
$$

If this condition is violated, the developer would inflate the reported effort; otherwise, he would be truthful. Because the client prefers to deter the developer from cheating, he would like to satisfy this incentive compatible condition: $p _ { 1 } \leq \theta \phi s$ or $\phi \ge p _ { 1 } / ( \theta s )$ . The client’s problem can then be stated as

$$
\begin{array}{l} \max _ {F, p _ {1}, p _ {2}, \phi} \pi_ {C} = - F - p _ {1} e + p _ {2} t + u _ {1} e ^ {\alpha} t ^ {\beta} - u _ {2} t - w \phi \\ \text {s.t.} \pi_ {D} \geq v \quad \text {and} \quad \phi \geq p _ {1} / (\theta s). \end{array}
$$

The client’s profit is not necessarily concave in $p _ { 1 }$ and $_ { p _ { 2 } , }$ and a general closed-form solution does not exist. However, we can still find the performance bound for the time-and-materials contract analytically in terms of the effectiveness and efficiency of the auditing procedure. We first define a combined index of effectiveness and efficiency as $\eta = \theta s / w ;$ ) measures the effectiveness of the client’s auditing procedure per unit cost of auditing. We expect that the adoption of the time-and-materials contract would depend on this index $\eta .$ Clearly, ) decreases with the auditing cost parameter w, thereby decreasing the likeliness of adoption of a time-and-materials contract. This is intuitive. As the cost for auditing goes up, the client is less likely to adopt this type of contract. On the other hand, ) increases with the penalty s. A higher penalty reduces the propensity of the developer to cheat and enhances the likeliness of the client to adopt this contract.

Proposition 4. The client will choose a time-andmaterials contract over a fixed-price contract if and only if $\eta > \underline { { \eta } } .$ , where

$$
\begin{array}{c} \underline {{\eta}} = \frac {1 - \alpha}{u _ {1}} \bigg [ \bigg (\frac {1}{c _ {2}} \bigg) ^ {\alpha} \bigg (\frac {c _ {1} + c _ {3} h}{\alpha} \bigg) ^ {1 - \beta} \\ \cdot \bigg (\frac {(1 - \alpha) (u _ {2} - c _ {3})}{\beta (c _ {2} (1 - \alpha) + u _ {1})} \bigg) ^ {\beta} \bigg ] ^ {1 / (1 - \alpha - \beta)}. \end{array}
$$

It can be shown analytically that ) is a decreasing function of $u _ { 1 }$ and an increasing function of $u _ { 2 }$ This is also intuitive. When $u _ { 1 }$ increases, the software becomes more complex and provides better utility to the client. Therefore, the client is more likely to choose a contract form that provides higher incentives to the developer. On the other hand, when $u _ { 2 }$ increases, i.e., when there is a high opportunity cost of time, the gap between fixed-price and time-andmaterials contracts reduces, thereby making auditing a less attractive option. Overall, our result indicates that a time-and-materials contract is more appropriate when the auditing process is effective and efficient and the quality requirement is high. When the auditing process is either ineffective or inefficient and the quality requirement is not critical, a fixed-priced contract performs reasonably well when compared to a time-and-materials contract. To illustrate these trends, we plot in Figure 3 how ) changes with $u _ { 1 }$ and $u _ { 2 } ;$ all the parameters in these plots are the same as the ones used in Figure 2.

## 4. Performance-Based Contract: Quality-Level Agreement

In this section, we analyze a type of performancebased contract called quality-level agreement that has

## Figure 3 The Threshold  as Functions of $u _ { 1 }$ and $u _ { 2 }$

![](/api/attachments/CUBVGY63/fulltext/images/238e1635e6a0e6a7db7b3da6f81fbff45dc78898914baa6cfc221033145db244.jpg)

![](/api/attachments/CUBVGY63/fulltext/images/136b930ffe671a9e24736b7facf9982f019fb628b29bebb3365f84228a73282d.jpg)

become quite common in recent times. A qualitylevel agreement contract is similar to service level agreements that have been used in services sectors (Trienekens et al. 2004). This contract form makes a client’s payment contingent on the quality of the product. Under a quality-level agreement, the developer commits to fix all the bugs discovered within a prespecified time frame after the deployment of the product and agrees to pay a penalty when the software fault level exceeds the level specified in the contract. We first consider the situation where the contract is signed for a single period without any prototyping.

## 4.1. Single-Period Quality-Level Agreement

The timing of the events is similar to our original settings as shown in Figure 1. At time t, the software product is delivered to the client. Then, the client deploys the product and observes its quality for a prespecified period of time. The payment is made at the end of this period and is dependent on the observed quality. Software quality mainly includes functionality, usability, and reliability (Khoshgoftaar and Allen 2001). Because usability tests are relatively simple to conduct, we concentrate only on software functionality and reliability. We consider the common case where the quality of the software is indicated by major bugs and functional faults (Kan 2002). The client imposes a penalty based on the accumulated faults during the period of observation. The release time is the client’s decision.

Following prior literature (e.g., Jones 2000, Kan 2002), we treat software quality and number of faults or defects as linearly related: $N = A - B q .$ , where A and B are constants, and $q = e ^ { \alpha } t ^ { \beta } + \epsilon$ as before, with $E ( \epsilon ) = 0 .$ . We further assume that - follows a uniform distribution: $\epsilon \sim \mathrm { U n i f o r m } [ - \delta , \delta ]$ . The qualitylevel agreement contract can be written as $P = F -$ $r ( N - N _ { 0 } ) ^ { + }$ , where F is the fixed payment, r the penalty per fault, $N _ { 0 } = A - B q _ { k }$ the expected number of faults under the first-best quality level, and $( N -$ $N _ { 0 } ) ^ { + } = \mathrm { m a x } \{ 0 , N - N _ { 0 } \}$ . In other words, under this contract there is no penalty unless the number of faults is greater than $N _ { 0 }$ . The developer’s expected profit is

$$
\pi_ {D} = F - r \mathrm{E} (N - N _ {0}) ^ {+} - (c _ {1} + c _ {3} h) e + c _ {2} e ^ {\alpha} t ^ {\beta} + c _ {3} t.\tag{9}
$$

The client first chooses the contract parameters $F ,$ $r ,$ and t. The developer then maximizes the profit in Equation (9) and decides the effort level. To find the equilibrium, we use backward induction. First, we derive the upper bound for the effort exerted by the developer.

Lemma 1. The developer would choose an effort level no greater than $\bar { e } = ( ( q _ { b } + \delta ) / t ^ { \beta } ) ^ { 1 / \alpha }$ , where $q _ { b }$ is the first-best software quality.

From Lemma 1, we know that there is no need to consider the situation $q _ { b } - e ^ { \alpha } t ^ { \beta } < - \delta$ . We define $\psi =$ min $\{ q _ { b } - e ^ { \alpha } t ^ { \beta } , \delta \}$ . Then

$$
\begin{array}{l} \mathrm{E} (N - N _ {0}) ^ {+} = B \mathrm{E} (q _ {b} - e ^ {\alpha} t ^ {\beta} - \epsilon) ^ {+} \\ \qquad = B \int_ {- \delta} ^ {\psi} (q _ {b} - e ^ {\alpha} t ^ {\beta} - \epsilon) \frac {1}{2 \delta}   d \epsilon \\ \qquad = \frac {B (\psi + \delta) (2 q _ {b} - 2 e ^ {\alpha} t ^ {\beta} - \psi + \delta)}{4 \delta}. \end{array}
$$

Substituting the value of $\psi ,$ we get

$$
\begin{array}{l} \mathrm{E} (N - N _ {0}) ^ {+} \\ = \left\{ \begin{array}{l l} \frac {B (q _ {b} - e ^ {\alpha} t ^ {\beta} + \delta) ^ {2}}{4 \delta}, & \text { if } - \delta \leq q _ {b} - e ^ {\alpha} t ^ {\beta} <   \delta , \\ B (q _ {b} - e ^ {\alpha} t ^ {\beta}), & \text { if } q _ {b} - e ^ {\alpha} t ^ {\beta} \geq \delta . \end{array} \right. \end{array}
$$

It should be noted here that when $q _ { b } - e ^ { \alpha } t ^ { \beta } = \delta ,$ , the two expressions are exactly the same. Therefore, $\pi _ { D }$ is continuous at that point. We now try to characterize the developer’s response to the penalty rate set by the client.

Lemma 2. (i) The developer’s optimal effort level increases in the penalty rate r. (ii) The developer’s optimal profit decreases in the penalty rate r.

Finally, the client’s problem can be written as

$$
\max _ {F, r, t} \pi_ {C} = - F + r \mathrm{E} (N - N _ {0}) ^ {+} + u _ {1} e ^ {\alpha} t ^ {\beta} - u _ {2} t
$$

$$
\mathrm{s.t.} \pi_ {D} (e) \geq v.
$$

By anticipating the developer’s optimal response to the penalty rate and the fixed payment, the client could design the optimal contract. The equilibrium contract is given as follows.

Proposition 5. For the quality-level agreement contract $P = F - r ( N - N _ { 0 } ) ^ { + }$ , the equilibrium release time $t _ { q } ,$ contract payment $( F _ { q } , r _ { q } )$ , and the developer’s effort $e _ { q }$ are given by

$$
\begin{array}{c} {e _ {q} = e _ {b}, \quad t _ {q} = t _ {b}, \quad r _ {q} = 2 u _ {1} / B, \quad a n d} \\ {F _ {q} = (c _ {1} + c _ {3} h) e _ {b} - c _ {2} q _ {b} - c _ {3} t _ {b} + v + \delta u _ {1} / 2.} \end{array}
$$

From Proposition 5, we can see that the equilibrium fixed payment increases in $\delta ,$ the parameter representing uncertainty in software quality. With higher uncertainty, the client compensates the developer with a higher fixed payment to maintain the incentive compatibility of the developer with the optimal penalty rate $r _ { q } .$ . Proposition 5 also suggests that the penalty rate depends only on $u _ { 1 }$ and B. When the client requires a higher software quality, i.e., $u _ { 1 }$ is higher, he would naturally set a higher penalty rate. On the other hand, when there is a lower error rate, i.e., B is lower, the expected number of faults decreases, resulting in a lower incentive for the developer. The client responds to this by increasing the penalty rate to induce the developer to provide the optimal effort level. Because the developer’s equilibrium effort and release time equal the respective firstbest levels, the contract attains the first-best quality.

## 4.2. Two-Period Quality-Level Agreement with Prototyping

In this section, we extend quality-level agreements into a two-period framework. In practice, software outsourcing often involves multiple stages of project development and milestones. Software development is usually quite complex and has large uncertainties. External factors as well as internal business changes can alter the requirements and, therefore, the specification of a software system. There can be two approaches toward writing an outsourcing contract.

The first approach is to write a complete contract at the beginning based on the best available information at that time. If the requirements change over time, change requests are appended to the contract when necessary. The second approach is to use a two-stage adaptive contract (Bennedsen and Schultz 2005). The first stage is used to build a prototype and understand the requirements better, and this information is used to build the appropriate software in the second stage. The contract itself allocates a fixed payment for the prototyping in the first stage<sup>3</sup> and ties the qualitylevel agreement in the second stage to the outcome of the first stage. The benefit of the second approach is that the client has the ability to write the contract in the second stage with new information obtained from the first stage.

We specifically model the uncertainties in project requirements and specifications. As discussed earlier, the parameter $u _ { 1 }$ represents the client’s valuation of the utility from the software. Therefore, $u _ { 1 }$ indicates the client’s requirements for functionalities and thus the overall complexity of the software project. A higher $u _ { 1 }$ is, therefore, likely to be associated with a more complex project with higher requirements. However, software requirements are difficult to specify up-front and may change as the project progresses. To account for this uncertainty in requirements, one could adopt prototyping, which is a commonly used approach to better learn the software requirements before starting the actual development activities (Boehm 1981).

We complete the two-period model setup by assuming that at the end of the prototyping stage, the realized value of $u _ { 1 }$ is either $u _ { 1 H }$ with probability 5 or $u _ { 1 L }$ with probability 1 − 5; $u _ { 1 H } > u _ { 1 L } > 0$ . Because $u _ { 1 } =$ $\gamma u _ { 1 H } + ( 1 - \gamma ) u _ { 1 L } ,$ , we get

$$
\gamma = \frac {u _ {1} - u _ {1 L}}{u _ {1 H} - u _ {1 L}}.
$$

The client must choose between a single-stage contract or an adaptive two-stage contract. If a singlestage contract is chosen, the actual realization of $u _ { 1 }$ is not observable and the contract is specified based on the available information at that time. With an adaptive contract, the client can find out the quality requirement through project prototyping in the first period. The uncertainty is removed because the actual realization of $u _ { 1 }$ can be observed and the contract can be written based on this actual realization. However, the client would incur an additional fixed cost for prototyping; let us denote this cost as $c _ { p } .$ The client clearly faces a trade-off in the contract choice. Committing to a single-stage contract saves the prototyping cost, but there will be uncertainties in the requirements and additional costs for change requests. On the other hand, though an adaptive contract can help reduce project requirement uncertainty, it will involve an extra, up-front prototyping cost.

Because the first-best solution can be achieved in the quality-level agreement, we can just compare the total surplus for both cases. First, from Equations (3) and (4) we can get effort and release time $( e _ { b } , t _ { b } )$ for a single-period contract, $( e _ { b H } , t _ { b H } )$ for an adaptive contract with $u _ { 1 } = u _ { 1 H } ,$ , and $( e _ { b L } , t _ { b L } )$ for an adaptive contract with $u _ { 1 } = u _ { 1 L } \colon$

$$
e _ {b} = \left[ (u _ {1} + c _ {2}) \left(\frac {\beta}{u _ {2} - c _ {3}}\right) ^ {\beta} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {1 - \beta} \right] ^ {1 / (1 - \alpha - \beta)},
$$

$$
t _ {b} = \left[ (u _ {1} + c _ {2}) \left(\frac {\beta}{u _ {2} - c _ {3}}\right) ^ {1 - \alpha} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {\alpha} \right] ^ {1 / (1 - \alpha - \beta)},
$$

$$
e _ {b H} = \left[ (u _ {1 H} + c _ {2}) \left(\frac {\beta}{u _ {2} - c _ {3}}\right) ^ {\beta} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {1 - \beta} \right] ^ {1 / (1 - \alpha - \beta)},
$$

$$
t _ {b H} = \left[ (u _ {1 H} + c _ {2}) \left(\frac {\beta}{u _ {2} - c _ {3}}\right) ^ {1 - \alpha} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {\alpha} \right] ^ {1 / (1 - \alpha - \beta)},
$$

$$
e _ {b L} = \left[ (u _ {1 L} + c _ {2}) \left(\frac {\beta}{u _ {2} - c _ {3}}\right) ^ {\beta} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {1 - \beta} \right] ^ {1 / (1 - \alpha - \beta)},
$$

and

$$
t _ {b L} = \left[ (u _ {1 L} + c _ {2}) \left(\frac {\beta}{u _ {2} - c _ {3}}\right) ^ {1 - \alpha} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {\alpha} \right] ^ {1 / (1 - \alpha - \beta)}.
$$

Next, we can find the total surplus in each of the cases. For a single-period contract, the expected total surplus is

$$
\gamma \Pi (u _ {1 H}, e _ {b}, t _ {b}) + (1 - \gamma) \Pi (u _ {1 L}, e _ {b}, t _ {b}).
$$

On the other hand, the expected total surplus under an adaptive contract is

$$
\gamma \Pi (u _ {1 H}, e _ {b H}, t _ {b H}) + (1 - \gamma) \Pi (u _ {1 L}, e _ {b L}, t _ {b L}) - c _ {p}.
$$

We can prove the following result by simply comparing the total surpluses for the above two contracts:<sup>4</sup>

Proposition 6. The client would prefer an adaptive two-period contract if and only if $c _ { p } < \bar { c } _ { p } ,$ , where

$$
\begin{array}{r l} & {\bar {c} _ {p} = (1 - \alpha - \beta) \bigg (\frac {\beta}{u _ {2} - c _ {3}} \bigg) ^ {\beta / (1 - \alpha - \beta)} \bigg (\frac {\alpha}{c _ {1} + c _ {3} h} \bigg) ^ {\alpha / (1 - \alpha - \beta)}} \\ & {\quad \cdot [ \gamma (u _ {1 H} + c _ {2}) ^ {1 / (1 - \alpha - \beta)} + (1 - \gamma) (u _ {1 L} + c _ {2}) ^ {1 / (1 - \alpha - \beta)}} \\ & {\qquad - (u _ {1} + c _ {2}) ^ {1 / (1 - \alpha - \beta)} ].} \end{array}
$$

Clearly, $\bar { c } _ { p }$ represents the benefit of prototyping whereas $c _ { p }$ represents the cost. Proposition $^ { 6 , }$ therefore, indicates that the client would use an adaptive contract if the benefit $( \bar { c } _ { p } )$ outweighs the cost $( c _ { p } )$ of prototyping. It is easy to see that the benefit increases with the uncertainty level of $u _ { 1 } . \mathrm { A s } u _ { 1 H }$ and $u _ { 1 L }$ get further and further apart, thereby increasing the uncertainty about $u _ { 1 } ,$ the benefit increases. On the other hand, as $u _ { 1 H }$ and $u _ { 1 L }$ approach each other, the benefit decreases. In the extreme, when $u _ { 1 H } = u _ { 1 L } = u _ { 1 . }$ the benefit reduces to zero, implying that prototyping is not an attractive option. To illustrate this, in Figure 4 we plot $\bar { c } _ { p }$ as a function of the uncertainty in $u _ { 1 } ,$ where this uncertainty is represented by the coefficient of variation $\mathrm { C V } ( u _ { 1 } ) ;$ ; as expected, $\bar { c } _ { p }$ increases with $\mathrm { C V } ( u _ { 1 } )$

We conclude this discussion with the observation that adaptive contracts can also be viewed as hybrid contracts, where the two (or more) stages use different contract types. The two most common contract types for the prototyping stage are fixed price and timeand-materials. In this section, we model the prototyping stage as one with a fixed-price contract. However, because our results in §3.3 are applicable to a prototype developed under a time-and-materials contract, it is conceptually straightforward to extend the insights in this section to hybrid contracts that use a time-andmaterials contract for the first stage.

## 5. Profit-Sharing Contract

We finally turn our attention to contracts negotiated using a bargaining game. The contracts analyzed thus far in the paper follow a typical principal-agent model setup, where the reservation value of the developer is assumed to be known to the client. This is indeed a reasonable assumption when the market for developers is competitive. In a competitive market for agents, the principal needs to pay just the market value for the agent (Mas-Colell et al. 1995, p. 480). The principal-agent model has been widely applied in areas such as labor contracts, government procurement, and construction projects, where a single principal can choose agents in a competitive market. The above assumption has been common in those situations (Bajari and Tadelis 2001).

Figure 4 The Threshold $\bar { c } _ { p }$ as a Function of $\complement \lor ( u _ { 1 } )$  
![](/api/attachments/CUBVGY63/fulltext/images/a5070267fdc2525c586e80b5a76133cf8cf9f848ab8dbe48290d41210de20223.jpg)

Our analysis of software outsourcing contracts makes an implicit assumption that the outsourcing market is competitive. Over the last decade, outsourcing of IT services, especially software development, has seen a tremendous growth (McFarlan and Delacey 2004, Palvia 2007). The emergence of standardized tools, platforms, and metrics have made the development process more mature (Davenport 2005) and has reduced the barriers to entry into this market (Rai 2007). As a result, currently software outsourcing has a large global provider market with many established firms competing fiercely for software development contracts (McFarlan and Delacey 2004). Therefore, it is not unreasonable to assume that this market is competitive (Pettey 2008).

However, we do recognize that the competitive market assumption may not hold in a few situations. For example, when a developer has a patented technology or is licensing a rare expertise to a client, the developer can expect higher returns and may want to share the profit with the client (Shapiro 1985). In these situations, the sequence of the game will be different from a principal-agent model. First, the client and the developer will negotiate on the payment $P ,$ which should typically include some profit-sharing provision. Second, based on the negotiated contract, the developer will decide the time and effort for the project. A Nash bargaining game (Nash 1950) is an approach that has been widely used in two-party bargaining situations (Riddell 1981). We model the negotiation between the client and the developer as an asymmetric Nash bargaining game (Roth 1979) in which the payment P is derived by maximizing $\Pi _ { s } =$ <sup>7</sup><sub>D</sub> $\pi _ { C } ^ { 1 - \kappa }$ . The parameter $\kappa \in ( 0 , 1 )$ is a part of the negotiation and represents the developer’s relative bargaining power over the client. Because $\pi _ { D } = P - C$ and $\pi _ { C } = U - P , $ where $C = ( c _ { 1 } + c _ { 3 } h ) e - c _ { 2 } e ^ { \alpha } t ^ { \beta } - c _ { 3 } t$ and $U = u _ { 1 } e ^ { \alpha } t ^ { \beta } - u _ { 2 } t ,$ the optimal contract should, therefore, involve a payment P that solves<sup>5</sup>

$$
\begin{array}{l} \max _ {P} \Pi_ {s} = (P - C) ^ {\kappa} (U - P) ^ {1 - \kappa} \\ \text {s.t.} P \geq C \quad \text {and} \quad U \geq P. \end{array}
$$

Lemma 3. The Nash bargaining game results in a payment $P = \kappa U + ( 1 - \kappa ) C$ such that the expected net profit to each party is proportional to his or her bargaining power, i.e.,

$$
\frac {\pi_ {D}}{\pi_ {C}} = \frac {P - (c _ {1} + c _ {3} h) e + c _ {2} e ^ {\alpha} t ^ {\beta} + c _ {3} t}{u _ {1} e ^ {\alpha} t ^ {\beta} - u _ {2} t - P} = \frac {\kappa}{1 - \kappa}.
$$

We are now ready to characterize the equilibrium outcome of the Nash bargaining game. We first consider the situation where the developer’s effort can be verified costlessly. In that case, the expected profits for the client and the developer reduce to

$$
\pi_ {C} = (1 - \kappa) (U - C) \quad \mathrm{and} \quad \pi_ {D} = \kappa (U - C).
$$

Because 7 is a constant, both the client and the developer maximize U − C. This has two implications. First, the client would reveal his true $u _ { 1 }$ and $u _ { 2 }$ to the developer. This is because truth revelation is the only way the client can induce the developer to solve the same problem as his own. Second, because the developer maximizes the first-best objective function $( U - C )$ , the first-best solution can be reached in this case. Therefore, we have the following proposition:

Proposition 7. Under a contract negotiated through a Nash bargaining game, when the developer’s effort is observable, the developer’s effort and release time $e _ { s }$ and $t _ { s } ,$ respectively, will be at the first-best levels, i.e., $e _ { s } = e _ { b }$ and $t _ { s } = t _ { b }$

The above result is simple and intuitive but more effort is required before it can be implemented in practice. This is because the developer’s effort is usually not verifiable. Therefore, after the software is developed, the developer has an incentive to inflate the effort expended for the project. Naturally, the client cannot assume that the developer will report the effort level truthfully and must audit the developer to keep her from cheating. We model the audit process in exactly the same manner as described in §3.3: We assume that the actual effort is $e ,$ the reported effort is ${ \hat { e } } = e + d ,$ and the expected penalty is \$#ds, where as before \$ represents the auditing effectiveness, $\phi$ represents the level of auditing effort, and s represents the penalty for cheating. Let $\widehat { C } = ( c _ { 1 } +$ $c _ { 3 } h ) \hat { e } - c _ { 2 } \hat { e } ^ { \alpha } t ^ { \beta } - c _ { 3 } t$ and $\widehat { U } = u _ { 1 } \hat { e } ^ { \alpha } t ^ { \beta } - u _ { 2 } t$ . The expected profit for the developer can then be written as

$$
\pi_ {D} = \kappa \widehat {U} + (1 - \kappa) \widehat {C} - C - \theta \phi d s.
$$

As before, the incentive compatible condition for the developer not to cheat is (Myerson 1979)

$$
\frac {\partial \pi_ {D}}{\partial d} \leq 0.
$$

Clearly, the client would ensure $\partial \pi _ { D } / \partial d \leq 0 ,$ , which would keep the developer from cheating. This, in turn, ensures that the first-best can be reached in this situation, as well.

Proposition 8. Under a contract negotiated through a Nash bargaining game, when the developer’s effort is not directly observable, the client would implement an auditing

policy denoted by

$$
\phi_ {s} = \frac {(c _ {1} + c _ {3} h) (u _ {1} + 2 (1 - \kappa) c _ {2})}{\theta s (u _ {1} + c _ {2})}.
$$

The developer would choose effort and release time at the first-best levels, i.e., $e _ { s } = e _ { b }$ and $t _ { s } = t _ { b }$

A contract negotiated under a bargaining game can also be viewed as a profit-sharing contract, where the overall profit $( U - C )$ is shared according to the relative bargaining power of the two parties. It should be noted, however, that such a bargaining game may reach a disagreement point (Roth 1979)—and a contract not be reached—if one of the parties has a very high bargaining power. To see this, consider the case where 7 is very small; in that case, the expected profit for the developer may be smaller than her reservation value. Alternatively, if 7 is close to one, the client’s expected profit net of the auditing cost may be negative. Also, note that when the bargaining powers of the two parties are equal (i.e., 7 = 05), this reduces to a traditional symmetric Nash solution (Roth 1979), where the profit is shared equally by the two parties.

## 6. Discussions

## 6.1. Practical Relevance

To understand the relevant aspects of real-world software outsourcing contracts, we studied 15 contracts written during the period of December 2002 to January 2007. These contracts were filed by the individual companies as a part of their financial statements with the U.S. Securities and Exchange Commission (SEC). A more detailed description of these contracts is provided in Appendix B. Table 2 summarizes the data gleaned from these contracts and categorizes them along five key dimensions.

These dimensions have been incorporated into our modeling framework based on contract theory and software engineering economics. Our analytical results are largely consistent with the broad observations from these contracts. We find that 5 out of the 15 contracts were fixed price despite the fact that, under these contracts, developers have high incentives to reduce their costs and underprovide quality. However, our analytical results indicate that a fixed-price contract may indeed perform better than a time-and-materials contract if the client lacks an efficient and effective auditing process. Furthermore, the performance gap between fixed-price contracts and the first-best solution narrows for relatively simple projects with somewhat less stringent quality requirement. Interestingly, the five fixed-price contracts were all for projects that were relatively small and less complicated.

Table 2 Summary of Real-World Software Outsourcing Contracts

<table><tr><td>Dimension</td><td>Fixed price</td><td>Time and materials</td><td>Performance based</td><td>Profit sharing</td></tr><tr><td>Project complexity</td><td>Low</td><td>Medium/high</td><td>High</td><td>Medium/high</td></tr><tr><td>Product support</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Control mechanism</td><td>Project specification</td><td>Auditing</td><td>Measuring outcome</td><td>Auditing</td></tr><tr><td>Administration cost</td><td>Low</td><td>Medium</td><td>High</td><td>Medium</td></tr><tr><td>Incentive for quality</td><td>Low</td><td>Medium</td><td>High</td><td>High</td></tr></table>

The four time-and-materials contracts in our data set were for larger and more complex projects with medium to high quality requirements. The clients for these projects were usually knowledgeable about the software projects. This is in line with our finding that for a time-and-materials contract to be effective, the client’s auditing process ought to have some traction, which often depends on the monitoring and control mechanisms used by the client. Clearly, a client’s knowledge of the project is important in implementing these mechanisms.

There were three performance-based contracts; the associated projects were large and complex with high quality requirement. The knowledge level of the clients for these projects was high as was the outcome measurability. Once again, this is consistent with the results from our model. Our result indicates that when companies can clearly tie contract payment to software quality, performance-based contracts are better in providing incentives to the developers and increasing accountability. However, it is often quite challenging to properly write and administer a performance-based contract. Companies need to have extensive knowledge on the software project and must define clear and measurable goals and metrics.

Only two of the contracts specified profit-sharing clauses between the client and the developer. In one case, the developer provides a digital download and management software system to the client, who uses the system to sell digital contents to its customers. In the second case, the client company integrates the system provided by the developer and sells the combined commercial software system in the market. In each of these two cases, the revenue generated by the outsourced software system can be measured directly. Furthermore, in both cases, the developers have proprietary technologies that are critical to the clients businesses. The developers, therefore, were in a position to bargain for profit sharing with the clients.

We found that two of the companies used staged development for software outsourcing. The companies that used such staged development approaches are operate in the energy and food services sectors. Though no details were available about the level of uncertainty in requirements specifications in these cases, perhaps the two companies lack specific knowledge and face high uncertainties for their projects. Staged development and prototyping can definitely help them learn more during the initial phase, thereby reducing the overall uncertainty.

## 6.2. Prerelease Monitoring vs. Postrelease Evaluation

Our results suggest that incorporating incentive mechanisms into an outsourcing contract helps motivate the developer. Those incentive mechanisms include monitoring and auditing development efforts and evaluating project and product qualities. Depending on the timing of the outsourcing process (see Figure 1), we can categorize those mechanisms as prerelease monitoring and postrelease evaluation.

In a fixed-price contract, a client usually needs to make sure that the delivered product follows the specifications in the contract. In a time-and-materials contract with auditing, issues about developer effort should be resolved before client accepts the system. Naturally, these two types of contracts belong to the prerelease control mechanism. The actual performance of a fixed-price contract depends on the level of details at which the client can specify the requirements. For a time-and-materials contract, it depends on the efficiency and the effectiveness of the auditing mechanism.

Because software quality is hard to verify on release, companies can use postrelease evaluation to verify the quality. Our results suggest that a quality-level agreement can achieve first-best results. However, postrelease evaluation is not without its problems. Although a quality-level agreement can achieve a high level of efficiency, there are operational risks associated with this type of contracts. When software faults happen, clients face system downtime and delay, which could hurt their businesses severely. For example, in late 2005, Salesforce.com, a well-known customer relationship management provider, experienced several service outages, which prevented its customers from using the system for planned marketing activities (Vara 2006). Companies have to consider these risks carefully before adopting postrelease evaluation. If the risk of system downtime is too high, a company should try to negotiate a performance-based contract that ties the penalty to the system downtime. If this is not possible, it is better to use prerelease monitoring and resolve quality issues as much as possible before the system is released.

## 6.3. Incentives in Contracts

Our study shows that fixed-price contracts do not achieve a high level of efficiency, especially for complex projects with stringent requirements on software quality. The main reason is that developers have incentives to reduce their costs and underprovide quality under fixed-price contracts. For a time-andmaterials contract, even if the client has an efficient and effective auditing mechanism to verify developer effort, there is no guarantee that the developer would supply effort at an optimal level simply because the developer’s incentive is unlikely to be aligned perfectly with that of the client.

We find that a properly executed performancebased contract can align a developer’s incentive with the client and help achieve a higher level of efficiency. We observe such contracts in software outsourcing practices. Industrial reports also suggest that performance-based contracts are on the rise (Reddy 2003, Phillips 2006). Our results suggest that performance-based contracts work quite differently from traditional fixed-price and time-andmaterials contracts, and successful management of performance-based contracts relies on a few critical elements. First, a client company should be clear on the overall goal of the software system and on how the software product links to the business strategy and operations. This is crucial in helping the company define success measures in the next step. Second, the client is required to establish metrics to measure the product performance. The client should decide the performance standards from a business perspective and develop the metrics by considering both business needs and industrial standards. For example, if the software is mission critical, then the metrics should include measures such as number of software faults and system downtime. It is important that the performance metrics measure operational results and are not about mere compliance with software specifications (Phillips 2006). Furthermore, the right incentives including reward and penalty need to be built into the contract. In managing a performance-based contract, it may be difficult for a company to establish the right metrics and incentives at the beginning. In those situations, a client may adopt approaches such as phased development, prototyping, and adaptive contracts. With initial prototyping and testing, companies can learn from the experience and refine their metrics for the software system.

Profit-sharing contracts also provide strong incentives to a developer. When the economic value such as the sales or revenue related to the software product can be quantified, these profit-sharing contracts can be quite effective in motivating the developers. It should be noted, however, that even though profitsharing contracts align the incentives of the client and the developer well, the client still has to invest in an auditing mechanism to ensure that the developer does not inflate her reported effort on the project.

We find that contracts that provide high incentives can achieve the first-best results. In practice, designing high-incentive contracts can be quite complex. The basic principle behind these contracts is to achieve goal congruence, which means that an appropriately designed reward and penalty system encourages a self-interested agent to behave closely to what a principal desires. This usually requires a contract to provide an optimal balance of incentive and risk sharing.

## 7. Conclusions

This paper examines the performance of various software outsourcing contracts. In a typical principalagent model, it is assumed that the agent effort or the contract outcome is observable. For software projects, however, developer effort may be hard to monitor and product quality cannot be verified immediately after the software is delivered. We apply software engineering economics and a principal-agent model to analyze different types of software outsourcing contracts. We find that under fixed-price contracts, developers would invest lower effort and less time than those in first-best scenarios. We examine how improvements on outsourcing process and control mechanisms could improve contract performance. We find that, if a client has an effective and efficient process of monitoring and auditing, a timeand-materials contract may perform better than a fixed-price contract.

We also consider a type of performance-based contract, called quality-level agreements, where developer payoff is associated with the performance of the software for a specified period of time after deployment. Such an agreement is shown to achieve the first-best performance ex ante. To address challenges associated with projects involving high requirements uncertainty, we extend these contracts to multiple stages. Finally, we examine profit-sharing contracts, where the costs and benefits associated with the software are allocated to the two parties according to their relative bargaining power. These contracts are also shown to achieve the first-best performance.

Our results provide useful insights on contract design and process improvement for software outsourcing. First, without active processes and mechanisms to monitor developer effort and collect project information, a more complicated contract form does not automatically guarantee higher performance. Second, incentive divergence is one of the main reasons of welfare loss. Performance-based contracts could improve contract performance. However, these contracts involve additional downtime risks and may incur a fixed prototyping cost. Managers should carefully consider this cost and operational risks when choosing a contract form.

This paper makes a few assumptions. First, for the sake of tractability, we ignore the iterative nature of software development. Almost all real-world contracts contain contingency clauses and provisions for change requests. It would be interesting to see how these provisions may affect the performance of different contract types. Second, we assume that once the specification is finalized and the contract is negotiated, the developer works in isolation. Many firms are realizing that a collaborative process that engages both the client and the developer in software development is often quite beneficial. Future studies could study the impact of collaborative processes in contract design. Third, different types of monitoring and control mechanisms could be incorporated into a contract and their impact could be studied. It will be interesting, for example, to see whether continuous monitoring and testing would lead to a higher software quality. Finally, we do not perform robust empirical validation of the results derived in this paper; our analysis of real-world contracts is largely qualitative. Future research could collect real-world contract data and perform rigorous empirical analysis to estimate the propositions derived in this paper. We are currently working on some of these issues to develop a more complete picture of the topic and to shed more light on the related managerial implications.

## Acknowledgments

An earlier version of this paper was presented at the Workshop on Information Technologies and Systems (WITS-05), Las Vegas, NV, in 2005; the authors thank the participants of that workshop for encouraging remarks and useful insights. The authors also thank the senior editor (Paulo Goes), the associate editor (Ram Gopal), and three anonymous reviewers of Information Systems Research for comments and suggestions they made in the two rounds of review; this paper greatly benefited from their efforts.

## Appendix A. Proofs

<sup>Proof of Proposition 1.</sup> The first-order conditions for the FBP are

$$
\frac {\partial \Pi}{\partial e} = \alpha (u _ {1} + c _ {2}) e ^ {\alpha - 1} t ^ {\beta} - (c _ {1} + c _ {3} h) = 0, \quad \mathrm{and}\tag{A1}
$$

$$
\frac {\partial \Pi}{\partial t} = \beta (u _ {1} + c _ {2}) e ^ {\alpha} t ^ {\beta - 1} - (u _ {2} - c _ {3}) = 0.\tag{A2}
$$

From Equation (A1), we get

$$
e = \left[ \frac {\alpha (u _ {1} + c _ {2}) t ^ {\beta}}{c _ {1} + c _ {3} h} \right] ^ {1 / (1 - \alpha)},\tag{A3}
$$

which can be substituted into Equation (A2) to get

$$
\beta \left[ \left(u _ {1} + c _ {2}\right) \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {\alpha} t ^ {\alpha + \beta - 1} \right] ^ {1 / (1 - \alpha)} - \left(u _ {2} - c _ {3}\right) = 0.\tag{A4}
$$

Equation (A4) can be simplified to obtain ${ t } _ { b } ,$ which in turn can be substituted into Equation (A3) to obtain $\boldsymbol { e } _ { b } .$ . Finally, the Hessian matrix is given by

$$
\mathbf {H} = \left[ \begin{array}{c c} \frac {\partial^ {2} \Pi}{\partial e ^ {2}} & \frac {\partial^ {2} \Pi}{\partial e \partial t} \\ \frac {\partial^ {2} \Pi}{\partial t \partial e} & \frac {\partial^ {2} \Pi}{\partial t ^ {2}} \end{array} \right].
$$

It is easy to seen that H is negative semidefinite for any value of e and t. This is because

$$
\frac {\partial^ {2} \Pi}{\partial e ^ {2}} = \alpha (\alpha - 1) (u _ {1} + c _ {2}) e ^ {\alpha - 2} t ^ {\beta} \leq 0, \quad \mathrm{and}
$$

$$
\begin{array}{c} \frac {\partial^ {2} \Pi}{\partial e ^ {2}} \cdot \frac {\partial^ {2} \Pi}{\partial t ^ {2}} - \frac {\partial^ {2} \Pi}{\partial e \partial t} \cdot \frac {\partial^ {2} \Pi}{\partial t \partial e} \\ = \alpha \beta (1 - \alpha - \beta) (u _ {1} + c _ {2}) ^ {2} e ^ {2 (\alpha - 1)} t ^ {2 (\beta - 1)} \geq 0. \end{array}
$$

Therefore, the objective function is concave in $( e , t )$ , and $( e _ { b } , t _ { b } )$ in Equations (3) and (4) is the optimal solution. <sup></sup> <sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>2.</sup> Using standard backward induction, we first examine the developer’s problem in Equation (5). The first-order conditions for the problem are

$$
\frac {\partial \pi_ {D}}{\partial e} = \alpha c _ {2} e ^ {\alpha - 1} t ^ {\beta} - (c _ {1} + c _ {3} h) = 0, \quad \mathrm{and}\tag{A5}
$$

$$
\frac {\partial \pi_ {D}}{\partial t} = - p + \beta c _ {2} e ^ {\alpha} t ^ {\beta - 1} + c _ {3} = 0.\tag{A6}
$$

From Equation (A5), we get

$$
e = \left[ \frac {\alpha c _ {2} t ^ {\beta}}{c _ {1} + c _ {3} h} \right] ^ {1 / (1 - \alpha)},\tag{A7}
$$

which is substituted into Equation (A6) to obtain

$$
- p + \beta \biggl [ c _ {2} \biggl (\frac {\alpha}{c _ {1} + c _ {3} h} \biggr) ^ {\alpha} t ^ {\alpha + \beta - 1} \biggr ] ^ {1 / (1 - \alpha)} + c _ {3} = 0.
$$

Simplifying, we get

$$
t _ {f} = \left[ c _ {2} \bigg (\frac {\beta}{p - c _ {3}} \bigg) ^ {1 - \alpha} \bigg (\frac {\alpha}{c _ {1} + c _ {3} h} \bigg) ^ {\alpha} \right] ^ {1 / (1 - \alpha - \beta)},\tag{A8}
$$

which can be substituted into Equation (A7) to obtain

$$
e _ {f} = \left[ c _ {2} \left(\frac {\beta}{p - c _ {3}}\right) ^ {\beta} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {1 - \beta} \right] ^ {1 / (1 - \alpha - \beta)}.\tag{A9}
$$

Now, we look at the Hessian matrix, which is given by

$$
\mathbf {H} = \left[ \begin{array}{c c} \frac {\partial^ {2} \Pi_ {D}}{\partial e ^ {2}} & \frac {\partial^ {2} \Pi_ {D}}{\partial e \partial t} \\ \frac {\partial^ {2} \Pi_ {D}}{\partial t \partial e} & \frac {\partial^ {2} \Pi_ {D}}{\partial t ^ {2}} \end{array} \right].
$$

It can be easily seen that

$$
\begin{array}{c} \frac {\partial^ {2} \Pi_ {D}}{\partial e ^ {2}} = \alpha (\alpha - 1) c _ {2} e ^ {\alpha - 2} t ^ {\beta} \leq 0, \quad \text { and } \\ \frac {\partial^ {2} \Pi_ {D}}{\partial e ^ {2}} \cdot \frac {\partial^ {2} \Pi_ {D}}{\partial t ^ {2}} - \frac {\partial^ {2} \Pi_ {D}}{\partial e \partial t} \cdot \frac {\partial^ {2} \Pi_ {D}}{\partial t \partial e} = \alpha \beta (1 - \alpha - \beta) c _ {2} ^ {2} e ^ {2 (\alpha - 1)} t ^ {2 (\beta - 1)} \geq 0. \end{array}
$$

Therefore, H is negative semidefinite, the objective function in Equation (5) is concave, and $( e _ { f } , t _ { f } )$ is the optimal strategy of the developer given the contract.

Next, we examine the client firm’s problem in Equation (6). Clearly, the individual rationality condition for the developer must be binding because the client firm can choose the lowest possible fixed-price payment to maximize $\pi _ { C } .$ Thus,

$$
F = p t - c _ {2} e ^ {\alpha} t ^ {\beta} - c _ {3} t + (c _ {1} + c _ {3} h) e + v,
$$

which, after substitution, simplifies the client’s problem to

$$
\max _ {p} \pi_ {C} = (c _ {2} + u _ {1}) e ^ {\alpha} t ^ {\beta} - (u _ {2} - c _ {3}) t - (c _ {1} + c _ {3} h) e - v.
$$

Because the client can anticipate the developer’s strategy in designing the optimal contract, we substitute $( e _ { f } , t _ { f } )$ from Equations (A8) and (A9) into the client’s problem and derive the first-order derivative as

$$
\begin{array}{c} \frac {d \pi_ {C}}{d p} = - K _ {1} \frac {\beta}{1 - \alpha - \beta} (p - c _ {3}) ^ {- (1 - \alpha) / (1 - \alpha - \beta)} \\ + K _ {2} (u _ {2} - c _ {3}) \frac {1 - \alpha}{1 - \alpha - \beta} (p - c _ {3}) ^ {- (2 - 2 \alpha - \beta) / (1 - \alpha - \beta)}, \end{array}
$$

where

$$
\begin{array}{c} K _ {1} = K _ {2} ^ {\beta} K _ {3} ^ {\alpha} (c _ {2} + u _ {1}) - K _ {3} (c _ {1} + c _ {3} h), \\ K _ {2} = \left[ c _ {2} \beta^ {1 - \alpha} \bigg (\frac {\alpha}{c _ {1} + c _ {3} h} \bigg) ^ {\alpha} \right] ^ {1 / (1 - \alpha - \beta)}, \quad \text { and } \\ K _ {3} = \left[ c _ {2} \beta^ {\beta} \bigg (\frac {\alpha}{c _ {1} + c _ {3} h} \bigg) ^ {1 - \beta} \right] ^ {1 / (1 - \alpha - \beta)}. \end{array}
$$

Solving $d \pi _ { C } / d p = 0 .$ , we get the following solution for the delay penalty:

$$
p _ {f} = c _ {3} + \frac {c _ {2} (1 - \alpha) (u _ {2} - c _ {3})}{c _ {2} (1 - \alpha) + u _ {1}}.\tag{A10}
$$

Finally, to complete the proof, we need to show that $p _ { f }$ in Equation (A10) is the unique optimal solution for the client. The second derivative of the client’s objective function is:

$$
\begin{array}{c} \frac {d ^ {2} \pi_ {\mathrm{C}}}{d p ^ {2}} = \frac {1 - \alpha}{(1 - \alpha - \beta) ^ {2}} (p - c _ {3}) ^ {(- 2 + 2 \alpha + \beta) / (1 - \alpha - \beta)} \\ \cdot \bigg [ K _ {3} \beta - \frac {K _ {2} (u _ {2} - c _ {3}) (2 - 2 \alpha - \beta)}{p - c _ {3}} \bigg ]. \end{array}
$$

Examining the second-order derivatives, we observe that:

$$
\frac {d ^ {2} \pi_ {C}}{d p ^ {2}} \left\{ \begin{array}{l l} <   0, & \mathrm{if} p <   p _ {0}, \\ = 0, & \mathrm{if} p = p _ {0}, \\ > 0, & \mathrm{if} p > p _ {0}, \end{array} \right.
$$

where $p _ { 0 } ~ = ~ c _ { 3 } ~ + ~ c _ { 2 } ( 2 - 2 \alpha - \beta ) ( u _ { 2 } - c _ { 3 } ) / ( ( c _ { 2 } 1 - \alpha ) + u _ { 1 } ) .$ Clearly, $p _ { f } ~ < ~ p _ { 0 } ,$ , and $p _ { f }$ is the only maximum in the interval $( - \infty , p _ { 0 } )$ ). We now consider the interval $[ p _ { 0 } , \infty )$ We note that $( d \pi _ { C } / d p ) | _ { p = p _ { 0 } } < 0 , ( d ^ { 2 } \pi _ { C } / d p ^ { 2 } ) | _ { p > p _ { 0 } } > 0 ,$ and lim $\mathfrak { l } _ { p \to \infty } ( d \pi _ { C } / d p ) = 0 .$ This is only possible if $( d { \dot { \pi } } _ { C } / d p ) | _ { p > p _ { 0 } } < 0$ and $\pi _ { C }$ is decreasing in $p$ beyond $p _ { 0 } .$ Clearly, $p _ { f }$ must be the global maximum. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Corollary</sup> <sup>1.</sup> In this case, the developer’s problem is

$$
\max _ {e} \pi_ {D} = F + c _ {2} e ^ {\alpha} t ^ {\beta} + c _ {3} t - (c _ {1} + c _ {3} h) e.
$$

The first-order condition for the problem is

$$
\frac {d \pi_ {D}}{d e} = \alpha c _ {2} e ^ {\alpha - 1} t ^ {\beta} - (c _ {1} + c _ {3} h) = 0.
$$

Because the second-order condition

$$
\frac {d ^ {2} \pi_ {D}}{d e ^ {2}} = \alpha (\alpha - 1) c _ {2} e ^ {\alpha - 2} t ^ {\beta} \leq 0
$$

is satisfied, we get the optimal effort from the first-order condition: 1/(1 -α

$$
e _ {f} = \left[ \frac {\alpha c _ {2} t ^ {\beta}}{c _ {1} + c _ {3} h} \right] ^ {1 / (1 - \alpha)}.\tag{A11}
$$

Next, we examine the client firm’s problem:

$$
\max _ {F, t} \pi_ {C} = - F + u _ {1} e ^ {\alpha} t ^ {\beta} - u _ {2} t
$$

$$
\begin{array}{l l} \text {s.t.} & \pi_ {D} (e, t) \geq v. \end{array}
$$

The individual rationality condition for the developer is binding, from which we get

$$
F = - c _ {2} e ^ {\alpha} t ^ {\beta} - c _ {3} t + (c _ {1} + c _ {3} h) e + v.
$$

The client’s problem now simplifies to

$$
\begin{array}{c} \max _ {t} \pi_ {C} = [ u _ {1} + (1 - \alpha) c _ {2} ] \bigg [ \frac {\alpha c _ {2}}{c _ {1} + c _ {3} h} \bigg ] ^ {\alpha / (1 - \alpha)} t ^ {\beta / (1 - \alpha)} \\ - (u _ {2} - c _ {3}) t - v. \end{array}
$$

The first-order condition is

$$
\begin{array}{c} \frac {d \pi_ {C}}{d t} = \frac {\beta}{1 - \alpha} [ u _ {1} + (1 - \alpha) c _ {2} ] \bigg [ \frac {\alpha c _ {2}}{c _ {1} + c _ {3} h} \bigg ] ^ {\alpha / (1 - \alpha)} t ^ {(- 1 + \alpha + \beta) / (1 - \alpha)} \\ - (u _ {2} - c _ {3}) = 0. \end{array}
$$

The second-order condition

$$
\begin{array}{l} \frac {d ^ {2} \pi_ {C}}{d t ^ {2}} = - \frac {\beta (1 - \alpha - \beta)}{(1 - \alpha) ^ {2}} \\ \cdot [ u _ {1} + (1 - \alpha) c _ {2} ] \left[ \frac {\alpha c _ {2}}{c _ {1} + c _ {3} h} \right] ^ {\alpha / (1 - \alpha)} t ^ {(- 2 + 2 \alpha + \beta) / (1 - \alpha)} \leq 0 \end{array}
$$

is satisfied. Therefore, from the first-order condition, we can derive the optimal release time for the client. When this is substituted into Equation (A11), we can get the optimal effort level of the developer. With some effort, it can be shown that the release time and effort level thus obtained are exactly the same as the ones in Proposition 2. <sup></sup>

Proof of Proposition 3.

(i) We define a function:

$$
f (x) = (1 + x) ^ {1 / (1 - \alpha)} - \left(1 + \frac {x}{1 - \alpha}\right).
$$

Of course,

$$
f ^ {\prime} (x) = \frac {1}{1 - \alpha} (1 + x) ^ {\alpha / (1 - \alpha)} - \frac {1}{1 - \alpha} > 0, \quad \text { for   all } x > 0.
$$

We see that $f ( 0 ) = 0 , \mathrm { { s o } } f ( x ) > 0$ for all $x > 0 .$ . Because $u _ { 1 } > 0 ,$ we conclude that $f ( u _ { 1 } / c _ { 2 } ) > 0 .$ , which implies:

$$
1 + \frac {u _ {1}}{c _ {2} (1 - \alpha)} <   \left(1 + \frac {u _ {1}}{c _ {2}}\right) ^ {1 / (1 - \alpha)}.
$$

This, of course, is equivalent to:

$$
c _ {2} \left(1 + \frac {u _ {1}}{c _ {2} (1 - \alpha)}\right) ^ {1 - \alpha} <   u _ {1} + c _ {2}.
$$

Because $\beta < 1 - \alpha$ and

$$
\left(1 + \frac {u _ {1}}{c _ {2} (1 - \alpha)}\right) ^ {\beta} <   \left(1 + \frac {u _ {1}}{c _ {2} (1 - \alpha)}\right) ^ {1 - \alpha},
$$

we have:

$$
c _ {2} \left(1 + \frac {u _ {1}}{c _ {2} (1 - \alpha)}\right) ^ {\beta} <   u _ {1} + c _ {2}.
$$

It is thus clear that $e _ { f } < e _ { b } , t _ { f } < t _ { b } ,$ and the expected quality under a fixed-price contract is lower when compared to the expected first-best quality.

(ii) From Equation $( 7 ) ,$ we can easily prove that $\partial \Delta \Pi / \partial u _ { 1 } > 0$ and $\partial \Delta \Pi / \partial u _ { 2 } < 0 .$ 

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>4.</sup> Assume that the client offers an incentive compatible contract with $\phi \ge p _ { 1 } / ( \theta s )$ . Then, $d = 0$ and the first-order conditions for the developer’s problem in Equation (8) are

$$
\begin{array}{c} \frac {\partial \pi_ {D}}{\partial e} = p _ {1} + \alpha c _ {2} e ^ {\alpha - 1} t ^ {\beta} - (c _ {1} + c _ {3} h) = 0, \quad \text { and } \\ \frac {\partial \pi_ {D}}{\partial t} = - p _ {2} + c _ {3} + \beta c _ {2} e ^ {\alpha} t ^ {\beta - 1} = 0. \end{array}
$$

With some algebraic manipulations, we can solve the above to obtain

$$
e = \left[ c _ {2} \left(\frac {\alpha}{c _ {1} + c _ {3} h - p _ {1}}\right) ^ {1 - \beta} \left(\frac {\beta}{p _ {2} - c _ {3}}\right) ^ {\beta} \right] ^ {1 / (1 - \alpha - \beta)}, \quad \text { and }\tag{A12}
$$

$$
t = \left[ c _ {2} \left(\frac {\alpha}{c _ {1} + c _ {3} h - p _ {1}}\right) ^ {\alpha} \left(\frac {\beta}{p _ {2} - c _ {3}}\right) ^ {1 - \alpha} \right] ^ {1 / (1 - \alpha - \beta)}.\tag{A13}
$$

Now, we look at the Hessian matrix, which is given by

$$
\mathbf {H} = \left[ \begin{array}{c c} \frac {\partial^ {2} \Pi_ {D}}{\partial e ^ {2}} & \frac {\partial^ {2} \Pi_ {D}}{\partial e \partial t} \\ \frac {\partial^ {2} \Pi_ {D}}{\partial t \partial e} & \frac {\partial^ {2} \Pi_ {D}}{\partial t ^ {2}} \end{array} \right].
$$

It can be easily seen that

$$
\frac {\partial^ {2} \Pi_ {D}}{\partial e ^ {2}} = \alpha (\alpha - 1) c _ {2} e ^ {\alpha - 2} t ^ {\beta} \leq 0, \quad \mathrm{and}
$$

$$
\frac {\partial^ {2} \Pi_ {D}}{\partial e ^ {2}} \cdot \frac {\partial^ {2} \Pi_ {D}}{\partial t ^ {2}} - \frac {\partial^ {2} \Pi_ {D}}{\partial e \partial t} \cdot \frac {\partial^ {2} \Pi_ {D}}{\partial t \partial e} = \alpha \beta (1 - \alpha - \beta) c _ {2} ^ {2} e ^ {2 (\alpha - 1)} t ^ {2 (\beta - 1)} \geq 0.
$$

Therefore, H is negative semidefinite, and Equations (A12) and (A13) denote the optimal strategy of the developer given the contract.

We now turn our attention to the client’s problem:

$$
\begin{array}{l l} \max _ {F, p _ {1}, p _ {2}, \phi} & \pi_ {C} = - F - p _ {1} e + p _ {2} t + u _ {1} e ^ {\alpha} t ^ {\beta} - u _ {2} t - w \phi \\ \text {s.t.} & \pi_ {D} \geq v, \quad \text {and} \quad \phi \geq p _ {1} / (\theta s). \end{array}
$$

First, we prove by contradiction that the condition $\phi ~ \ge ~ p _ { 1 } / ( \theta s )$ is binding. Suppose this is not true. Then, let the optimal solution be $( F ^ { * } , p _ { 1 } ^ { * } , p _ { 2 } ^ { * } , \phi ^ { * } )$ where $\phi ^ { * } = \phi ^ { \prime } + \xi , { \bf \bar { \phi } } \phi ^ { \prime } = p _ { 1 } / ( \theta s )$ and $\xi > 0 . \mathrm { O f }$ course, $\pi _ { D } ( F ^ { * } , p _ { 1 } ^ { * } , p _ { 2 } ^ { * } , \phi ^ { * } ) > v .$ . Now, consider the solution $( F ^ { * } , p _ { 1 } ^ { * } .$ $p _ { 2 } ^ { * } , \phi ^ { \prime } )$ . It is clear that this new solution is also feasible because $\pi _ { D } ( F ^ { * } , p _ { 1 } ^ { * } , p _ { 2 } ^ { * } , \phi ^ { \prime } ) = \pi _ { D } ( F ^ { * } , p _ { 1 } ^ { * } , p _ { 2 } ^ { * } , \phi ^ { * } ) + \theta d s \xi > v$ Furthermore, $\pi _ { C } ( F ^ { * } , p _ { 1 } ^ { * } , p _ { 2 } ^ { * } , \phi ^ { \prime } ) - \pi _ { C } ( F ^ { * } , p _ { 1 } ^ { * } , p _ { 2 } ^ { * } , \phi ^ { * } ) = w \xi > 0 .$ In other words, we have a feasible solution where the objective function value is strictly greater than the optimal value, which is a contradiction to the assumption that $( F ^ { * } , p _ { 1 } ^ { * } , p _ { 2 } ^ { * } , \phi ^ { * } )$ is the optimal solution. Therefore, $\phi = p _ { 1 } / ( \theta s )$ and

$$
F = - p _ {1} e + p _ {2} t - c _ {2} e ^ {\alpha} t ^ {\beta} + (c _ {1} + c _ {3} h) e - c _ {3} t + v.
$$

The client’s problem can be simplified to

$$
\max _ {p _ {1}, p _ {2}} \pi_ {C} = (u _ {1} + c _ {2}) e ^ {\alpha} t ^ {\beta} - (u _ {2} - c _ {3}) t - (c _ {1} + c _ {3} h) e - v - \frac {w p _ {1}}{\theta s}.
$$

Now, $( p _ { 1 } , p _ { 2 } ) = ( 0 , p _ { f } )$ is a feasible solution to the above problem. If $( p _ { 1 } , p _ { 2 } ) \stackrel { \cdot } { = } ( 0 , p _ { f } )$ , by substituting we get $F = F _ { f } ,$ $e = e _ { f } ,$ and $t = t _ { f }$ . Thus, if the client chooses this solution, the client gets exactly the same payoff as a fixed-price contract. Of course, the client can do better than the fixed-price contract by increasing $p _ { 1 }$ if and only if $( \partial \pi _ { C } / \partial p _ { 1 } ) | _ { p _ { 1 } = 0 } = 0 ;$ after some algebra, we can show that this is equivalent to

$$
\frac {u _ {1}}{1 - \alpha} \left[ c _ {2} ^ {\alpha} \left(\frac {\alpha}{c _ {1} + c _ {3} h}\right) ^ {1 - \beta} \left(\frac {\beta (c _ {2} (1 - \alpha) + u _ {1})}{(1 - \alpha) (u _ {2} - c _ {3})}\right) ^ {\beta} \right] ^ {1 / (1 - \alpha - \beta)} - \frac {w}{\theta s} > 0.
$$

This leads to the desired result. <sup></sup>

Proof of Lemma 1. <sub>It is easy to see</sub> $\bar { e } \geq e _ { b }$ and the developer has no incentive to choose an effort level greater than e¯ if the expected penalty from faults is zero, $\mathrm { i . e . , }$ if $N \leq N _ { 0 } .$ However, e is the solution to $N = N _ { 0 }$ or to $e ^ { \alpha } t ^ { \beta } - q _ { b } - \delta = 0 .$ Therefore, beyond an effort level of ${ \bar { e } } ,$ there is no extra benefit to the developer. <sup></sup>

Proof of Lemma 2.

Case $1 \colon - \delta \leq q _ { b } - e ^ { \alpha } t ^ { \beta } < \delta$

The first-order condition is given by

$$
\begin{array}{c} \frac {d \pi_ {D}}{d e} = \alpha e ^ {\alpha - 1} t ^ {\beta} \bigg [ \frac {r B}{2 \delta} (q _ {b} - e ^ {\alpha} t ^ {\beta} + \delta) + c _ {2} \bigg ] \\ - (c _ {1} + c _ {3} h) = 0. \end{array}\tag{A14}
$$

The second-order condition, given by

$$
\begin{array}{c} \frac {d ^ {2} \pi_ {D}}{d e ^ {2}} = \alpha (\alpha - 1) e ^ {\alpha - 2} t ^ {\beta} \bigg [ \frac {r B}{2 \delta} (q _ {b} - e ^ {\alpha} t ^ {\beta} + \delta) + c _ {2} \bigg ] \\ - \frac {r B}{2 \delta} \alpha^ {2} e ^ {2 (\alpha - 1)} t ^ {2 \beta} <   0 \end{array}
$$

is also satisfied, so the first-order condition maximizes the developer's objective function. We now take the derivative of both sides of Equation (A14), w.r.t. $r ,$ and rearrange the terms to obtain

$$
\begin{array}{l} \left[ \alpha (\alpha - 1) e ^ {\alpha - 2} t ^ {\beta} \left(\frac {r B}{2 \delta} (q _ {b} - e ^ {\alpha} t ^ {\beta} + \delta) + c _ {2}\right) - \frac {r B}{2 \delta} \alpha^ {2} e ^ {2 (\alpha - 1)} t ^ {2 \beta} \right] \frac {d e}{d r} \\ = - \alpha e ^ {\alpha - 1} t ^ {\beta} \left[ \frac {B}{2 \delta} (q _ {b} - e ^ {\alpha} t ^ {\beta} + \delta) \right]. \end{array}
$$

The right-hand side of the above expression is negative and so is the term within square brackets in the left-hand side. Clearly, it follows that $d e / d r > 0$

To prove that the developer’s optimal profit decreases with $r ,$ we note that

$$
\frac {d \pi_ {D}}{d r} = \frac {\partial \pi_ {D}}{\partial e} \frac {\partial e}{\partial r} + \frac {\partial \pi_ {D}}{\partial r}.
$$

However, at the optimal profit, $\partial \pi _ { D } / \partial e = 0$ . Therefore,

$$
\frac {d \pi_ {D}}{d r} = \frac {\partial \pi_ {D}}{\partial r} = - \frac {B}{4 \delta} [ q _ {b} - e ^ {\alpha} t ^ {\beta} + \delta ] ^ {2} <   0.
$$

Case 2: $q _ { b } - e ^ { \alpha } t ^ { \beta } \geq \delta$

The first-order condition is given by

$$
\frac {d \pi_ {D}}{d e} = \alpha e ^ {\alpha - 1} t ^ {\beta} (r B + c _ {2}) - (c _ {1} + c _ {3} h) = 0.\tag{A15}
$$

The second-order condition, given by

$$
\frac {d ^ {2} \pi_ {D}}{d e ^ {2}} = \alpha (\alpha - 1) e ^ {\alpha - 2} t ^ {\beta} (r B + c _ {2}) <   0
$$

is satisfied and the first-order condition maximizes the developer’s objective function. We now take the derivative of both sides of Equation (A15), w.r.t. $r ,$ and rearrange the terms to obtain

$$
[ \alpha (\alpha - 1) e ^ {\alpha - 2} t ^ {\beta} (r B + c _ {2}) ] \frac {d e}{d r} = - \alpha e ^ {\alpha - 1} t ^ {\beta} B.
$$

Once again, the right-hand side of the above expression is negative along with the term within square brackets in the left-hand side, so $d e / d r > 0$

Finally, as before, we can prove that the developer’s optimal profit decreases with r:

$$
\frac {d \pi_ {D}}{d r} = \frac {\partial \pi_ {D}}{\partial e} \frac {\partial e}{\partial r} + \frac {\partial \pi_ {D}}{\partial r} = \frac {\partial \pi_ {D}}{\partial r} = - B (q _ {b} - e ^ {\alpha} t ^ {\beta}) <   0,
$$

because $\partial \pi _ { D } / \partial e = 0$ at the optimal profit. <sup></sup>

Proof of Proposition $5 .$ In the proof of Lemma $^ { 2 , }$ we derived two first-order conditions in Equations (A14) and (A15). However, in the end only one of them would be valid because the optimal effort can satisfy only one of the two conditions for the two cases discussed there. Let us denote

$$
\bar {e} = \left(\frac {q _ {b} + \delta}{t ^ {\beta}}\right) ^ {1 / \alpha} \quad \text { and } \quad \underline {{e}} = \left(\frac {q _ {b} - \delta}{t ^ {\beta}}\right) ^ {1 / \alpha}.
$$

It then follows that under Case 1 (when $- \delta \leq q _ { b } - e ^ { \alpha } t ^ { \beta } < \delta ) ,$ $\underline { { { e } } } < e \leq \bar { e } ;$ on the other hand, under Case 2 (when $q _ { b } - e ^ { \alpha } t ^ { \beta } \geq$ $\delta ) , e \leq \underline { { e } } .$ Which of these two cases would eventually be satisfied would depend on the optimal penalty rate r chosen by the client. Therefore, we now examine the client’s problem. First, we consider Case 1:

$$
\begin{array}{l l} \max _ {F, r, t} & \pi_ {C} = - F + \frac {r B (q _ {b} - e ^ {\alpha} t ^ {\beta} + \delta) ^ {2}}{4 \delta} + u _ {1} e ^ {\alpha} t ^ {\beta} - u _ {2} t \\ \text {s.t.} & \pi_ {D} \geq v. \end{array}
$$

The client would choose F and r is such a way that makes the constraint binding. Therefore, we get

$$
F = \frac {r B (q _ {b} - e ^ {\alpha} t ^ {\beta} + \delta) ^ {2}}{4 \delta} - c _ {2} e ^ {\alpha} t ^ {\beta} + (c _ {1} + c _ {3} h) e - c _ {3} t + v.\tag{A16}
$$

This can be substituted into the client’s objective function to obtain

$$
\max _ {r, t} \pi_ {C} = (u _ {1} + c _ {2}) e ^ {\alpha} t ^ {\beta} - (u _ {2} - c _ {3}) t - (c _ {1} + c _ {3} h) e - v.
$$

The first-order conditions are

$$
\begin{array}{c} \frac {\partial \pi_ {C}}{\partial r} = \frac {\partial \pi_ {C}}{\partial e} \frac {d e}{d r} = (\alpha (u _ {1} + c _ {2}) e ^ {\alpha - 1} t ^ {\beta} - (c _ {1} + c _ {3} h)) \frac {d e}{d r} = 0, \\ \frac {\partial \pi_ {C}}{\partial t} = \beta (u _ {1} + c _ {2}) e ^ {\alpha} t ^ {\beta - 1} - (u _ {2} - c _ {3}) = 0. \end{array}
$$

Because we know from Lemma 2 that $d e / d r > 0 ,$ , the above conditions are exactly the same as the first-order conditions for the first-best problem; see Equations (A1) and (A2). Therefore, the optimal solution would be $e _ { q } = e _ { b }$ and $t _ { q } = t _ { b } .$ Furthermore, because $\underline { { e } } < e _ { b } \le \bar { e } ,$ the condition for Case 1 is satisfied and there is no need to consider Case 2 any further. Comparing Equation (A14) with Equation (A1) and noting that the first-best quality level is given by $q _ { b } = e _ { b } ^ { \alpha } t _ { b } ^ { \beta }$ , we can derive that $r _ { q } = 2 u _ { 1 } / B .$ . Finally, the value of $F _ { q }$ is determined from Equation (A16). <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>6.</sup> By comparing the total surplus of the two-period contract with that of the single-period contract, we can easily see that a two-stage contract would be preferable if and only if

$$
\begin{array}{r} c _ {p} <   \gamma [ \Pi (u _ {1 H}, e _ {b H}, t _ {b H}) - \Pi (u _ {1 H}, e _ {b}, t _ {b}) ] \\ + (1 - \gamma) [ \Pi (u _ {1 L}, e _ {b L}, t _ {b L}) - \Pi (u _ {1 L}, e _ {b}, t _ {b}) ]. \end{array}
$$

Substituting the expressions for different effort levels and release times and simplifying the right-hand side, we can prove the result stated in the proposition. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>3.</sup> We need to solve the following optimization problem:

$$
\begin{array}{l} \max _ {P} \Pi_ {s} = (P - C) ^ {\kappa} (U - P) ^ {1 - \kappa} \\ \text {s.t.} P \geq C \quad \text {and} U \geq P. \end{array}
$$

We first note that the optimal objective function value is always nonnegative because $P = \dot { C }$ and $P = U$ are both feasible solutions. It follows that at optimality there are only two possibilities: $U \geq P \geq C$ or $U \leq { \overline { { P } } } \leq C .$ . The second possibility can be ignored because it leads to a net negative expected surplus $( U - C )$ ; clearly, such a software project would never be undertaken in the first place. The first possibility implies that the two constraints are always satisfied by the solution of the unconstrained problem and can hence be dropped.

We now consider the first-order condition:

$$
\frac {\partial \Pi_ {s}}{\partial P} = k (P - C) ^ {k - 1} (U - P) ^ {1 - k} - (1 - k) (P - C) ^ {k} (U - P) ^ {- k} = 0,
$$

which can be simplified to obtain the desired result:

$$
\frac {P - C}{U - P} = \frac {\kappa}{1 - \kappa}, \quad \mathrm{and} \quad P = \kappa U + (1 - \kappa) C.
$$

We also note that

$$
\frac {\partial^ {2} \Pi_ {s}}{\partial P ^ {2}} = - k (1 - k) (P - C) ^ {k - 2} (U - P) ^ {- k - 1} (U - C) ^ {2} <   0.
$$

Therefore, the second-order condition is satisfied. <sup></sup>

Proof of Proposition 7. because the developer solves an optimization problem that is equivalent to the FBP. <sup></sup>

Proof of Proposition 8. <sub>If</sub> $\partial \pi _ { D } / \partial d \leq 0 .$ , the $d = 0 ;$ after some algebraic manipulations, we get

$$
\phi \geq \frac {1}{\theta s} [ (1 - \kappa) (c _ {1} + c _ {3} h) + \alpha (\kappa u _ {1} + (1 - \kappa) c _ {2}) e ^ {\alpha - 1} t ^ {\beta} ].
$$

As before, because the client’s profit decreases in $\phi ,$ we know that the condition will be binding in the client’s optimization problem. Therefore, we obtain

$$
\phi = \frac {1}{\theta s} [ (1 - \kappa) (c _ {1} + c _ {3} h) + \alpha (\kappa u _ {1} + (1 - \kappa) c _ {2}) e ^ {\alpha - 1} t ^ {\beta} ].\tag{A17}
$$

This will prohibit the developer from inflating her reported effort and reduce her expected profit to $\pi _ { D } ^ { - } = \kappa ( { \bar { U } } - C ) .$ which is aligned with the first-best case. Because the developer solves the FBP, condition (A1) still applies to the outcome; we rearrange the terms in condition (A1) to get

$$
e ^ {\alpha - 1} t ^ {\beta} = \frac {c _ {1} + c _ {3} h}{\alpha (u _ {1} + c _ {2})}.\tag{A18}
$$

We substitute Equation (A18) into Equation (A17) and after some algebra, we obtain

$$
\phi_ {s} = \frac {(c _ {1} + c _ {3} h) (u _ {1} + 2 (1 - \kappa) c _ {2})}{\theta s (u _ {1} + c _ {2})}.
$$

We already know that the developer solves the FBP, so to complete the proof, we only need to show that the client’s objective is also aligned with the first-best. This is easy. The client’s expected profit is given by

$$
\pi_ {C} = (1 - \kappa) (U - C) - w \phi_ {s}.
$$

However, because both w and $\phi _ { s }$ are independent of $e$ and t, the client’s objective reduces to the maximization of U − C as well. Therefore, the client would reveal his private knowledge of $u _ { 1 }$ and $u _ { 2 }$ truthfully and the first-best would be achieved. <sup></sup>

## Appendix B. Details of Real-World Contracts

We have obtained a set of 15 software outsourcing contracts from a database maintained by Practice Technologies, a company that specializes in legal information retrieval. These are the only software development contracts (stored in this database) that were written during the period of December 2002 to January 2007 and filed by companies as part of their financial statements to the U.S. Securities and Exchange Commission (SEC). A typical contract is about 10 pages long. Summaries of these contracts are provided in Tables B.1, B.2, and B.3.

Table B.1 Details of the Contracts Examined in This Study (Contracts 1–5)

<table><tr><td>Contract details</td><td>Contract 1</td><td>Contract 2</td><td>Contract 3</td><td>Contract 4</td><td>Contract 5</td></tr><tr><td>Client</td><td>mPhase Technologies</td><td>New Motion</td><td>True Digital Entertainment</td><td>Network Communications</td><td>Lawson Software</td></tr><tr><td>Developer</td><td>Magpie Telecom Insiders</td><td>Visionaire</td><td>NS8</td><td>EX Squared Solutions</td><td>Xansa</td></tr><tr><td>Developer location</td><td>United States</td><td>United States</td><td>United States</td><td>United States</td><td>India</td></tr><tr><td>Time contract written</td><td>2004</td><td>2005</td><td>2006</td><td>2006</td><td>2004</td></tr><tr><td>Contract duration</td><td>3 years</td><td>1 year</td><td>3 years</td><td>1 year</td><td>&gt;1 year</td></tr><tr><td>Nature of the project</td><td>Customized telecommuni-cation system</td><td>General development and service</td><td>Digital content manager</td><td>Database application</td><td>Enterprise system</td></tr><tr><td>Contract type</td><td>Performance based</td><td>Time and materials</td><td>Profit sharing</td><td>Time and materials</td><td>Hybrid</td></tr><tr><td>Quality requirement</td><td>High</td><td>Medium</td><td>High</td><td>High</td><td>High</td></tr><tr><td>Software support</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Client knowledge on the project</td><td>High</td><td>High</td><td>High</td><td>High</td><td>High</td></tr><tr><td>Outcome measurability</td><td>High</td><td>Medium</td><td>High</td><td>Medium</td><td>High</td></tr></table>

Table B.2 Details of the Contracts Examined in This Study (Contracts 6–10)

<table><tr><td>Contract details</td><td>Contract 6</td><td>Contract 7</td><td>Contract 8</td><td>Contract 9</td><td>Contract 10</td></tr><tr><td>Client</td><td>EPMed</td><td>Verizon</td><td>Energy Control Systems</td><td>Evove</td><td>Spectre Gaming</td></tr><tr><td>Developer</td><td>Biosense Webster</td><td>Intellisync</td><td>Bulldog Technologies</td><td>Xten Network</td><td>MET Games</td></tr><tr><td>Developer location</td><td>United States</td><td>United States</td><td>Canada</td><td>Canada</td><td>United States</td></tr><tr><td>Time contract written</td><td>2005</td><td>2004</td><td>2004</td><td>2002</td><td>2004</td></tr><tr><td>Contract duration</td><td>2 years</td><td>2 years</td><td>&lt;1 year</td><td>&lt;1 year</td><td>&gt;1 year</td></tr><tr><td>Nature of the project</td><td>Medical diagnostic system</td><td>Customized telecommunication system</td><td>Wireless software and system</td><td>Client-server communication software</td><td>Gaming software and application</td></tr><tr><td>Contract type</td><td>Profit sharing</td><td>Performance based</td><td>Fixed price</td><td>Time and materials</td><td>Performance based</td></tr><tr><td>Quality requirement</td><td>High</td><td>High</td><td>Medium</td><td>Medium</td><td>High</td></tr><tr><td>Software support</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Client knowledge on the project</td><td>High</td><td>High</td><td>Medium</td><td>Medium</td><td>High</td></tr><tr><td>Outcome measurability</td><td>High</td><td>High</td><td>High</td><td>Low</td><td>High</td></tr></table>

Table B.3 Details of the Contracts Examined in This Study (Contracts 11–15)

<table><tr><td>Contract details</td><td>Contract 11</td><td>Contract 12</td><td>Contract 13</td><td>Contract 14</td><td>Contract 15</td></tr><tr><td>Client</td><td>Hillwood Enterprises</td><td>Meridian</td><td>Essentially Yours Industries</td><td>Brooklyn Cheesecake and Desserts</td><td>Digital Youth Network</td></tr><tr><td>Developer</td><td>Perot Systems</td><td>Carla Leone</td><td>Colossal Head</td><td>Burbro Capital</td><td>Beacon Media</td></tr><tr><td>Developer location</td><td>United States</td><td>Canada</td><td>Canada</td><td>United States</td><td>Canada</td></tr><tr><td>Time contract written</td><td>2007</td><td>2004</td><td>2007</td><td>2005</td><td>2006</td></tr><tr><td>Contract duration</td><td>Long term</td><td>11 month</td><td>&gt;1 year</td><td>&lt;1 year</td><td>&lt;1 year</td></tr><tr><td>Nature of the project</td><td>Software and information service</td><td>Website development</td><td>e-commerce application</td><td>e-commerce application</td><td>Website design</td></tr><tr><td>Contract type</td><td>Time and materials</td><td>Fixed price</td><td>Fixed price</td><td>Fixed price</td><td>Fixed price</td></tr><tr><td>Quality requirement</td><td>Medium</td><td>Low</td><td>Medium</td><td>High</td><td>Low</td></tr><tr><td>Software support</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Client knowledge on the project</td><td>Low</td><td>High</td><td>High</td><td>High</td><td>High</td></tr><tr><td>Outcome measurability</td><td>Medium</td><td>Medium</td><td>High</td><td>Medium</td><td>Low</td></tr></table>

## References

Allen, D., D. Lueck. 1993. Transaction costs and the design of cropshare contracts. RAND J. Econom. 24(1) 78–100.

Bajari, P., S. Tadelis. 2001. Incentives versus transaction costs: A theory of procurement contracts. RAND J. Econom. 32(3) 387–407.

Bennedsen, M., C. Schultz. 2005. Adaptive contracting: The trialand-error approach to outsourcing. Econom. Theory 25(1) 35–50.

Boehm, B. W. 1981. Software Engineering Economics. Prentice-Hall, Upper Saddle River, NJ.

Cheung, S. 1969. Transaction costs, risk aversion, and the choice of contractual arrangements. J. Law Econom. 12(1) 23–42.

Choudhury, V., R. Sabherwal. 2003. Portfolios of control in outsourced software development projects. Inform. Systems Res. 14(3) 291–314.

Davenport, T. 2005. The coming commoditization of processes. Har vard Bus. Rev. 83(6) 100–108.

Gopal, A., K. Sivaramakrishnan, M. S. Krishnan, T. Mukhopadhyay. 2003. Contracts in offshore software development: An empirical analysis. Management Sci. 49(12) 1671–1683.

Gray, C. F., E. W. Larson. 2007. Project Management: The Managerial Process, 4th ed. McGraw-Hill, New York.

Grossman, S. J., O. D. Hart. 1983. An analysis of the principal-agent problem. Econometrica 51(1) 7–45.

Jones, C. 2000. Software Assessments, Benchmarks, and Best Practices. Addison-Wesley, Boston.

Kalnins, A., K. Mayer. 2004. Relationship and hybrid contracts: An analysis of contract choice in information technology. J. Law Econom. Organ. 20(1) 207–229.

Kan, S. H. 2002. Metrics and Models in Software Quality Engineering. Addison-Wesley, Boston.

Khoshgoftaar, T. M., E. B. Allen. 2001. Empirical assessment of a software metric: The information content of operators. Software Quality J. 9(2) 99–112.

Koh, C., S. Ang, D. W. Straub. 2004. IT outsourcing success: A psychological contract perspective. Inform. Systems Res. 15(4) 356–373.

Laffont, J.-J., D. Martimort. 2002. The Theory of Incentives. Princeton University Press, Princeton, NJ.

Laffont, J.-J., J. Tirole. 1993. A Theory of Incentives in Procurement and Regulation. MIT Press, Cambridge, MA.

Lee, J., M. Shaila, Y. Kim. 2004. IT outsourcing strategies: Universal istic, contingency, and configurational explanations of success. Inform. Systems Res. 15(2) 110–131.

Lichtenstein, Y. 2004. Puzzles in software development contracting. Comm. ACM 47(2) 61–65.

Mas-Colell, A., M. Whinston, J. Green. 1995. Microeconomic Theory.Oxford University Press, Oxford, UK.

McFarlan, F. W., B. J. Delacey. 2004. Outsourcing IT: The global landscape in 2004. Case Study 9-304-104, Harvard Business School, Boston.

Myerson, R. 1979. Incentive compatibility and the bargaining problem. Econometrica 47(1) 61–73.

Nash, J. 1950. The bargaining problem. Econometrica 18(2) 155–162.

Palvia, S. 2007. Global market for outsourcing IT and IT enabled services. J. Global Inform. Tech. Management 10(2) 1–6.

Pettey, C. 2008. Gartner says worldwide outsourcing market to grow 8.1 percent in 2008. Gartner Report, January 8, http:// www.gartner.com/it/page.jsp?id=578307.

Phillips, Z. 2006. Buying tech performance. Government Executive (May 24), http://www.govexec.com/dailyfed/0506/ 052406mm.htm.

Pressman, R. 2005. Software Engineering: A Practitioner’s Approach. McGraw-Hill, Boston.

Rai, S. 2007. India urged to adapt to stay outsource king. Internat. Herald Tribune (February 9) 16.

Reddy, A. 2003. Law aims to change acquisitions. Washington Post (November 24) E07.

Riddell, W. 1981. Bargaining under uncertainty. Amer. Econom. Rev. 71(4) 579–590.

Roth, A. 1979. Axiomatic Models of Bargaining. Springer-Verlag, Berlin.

Shapiro, C. 1985. Patent licensing and R&D rivalry. Amer. Econom. Rev. 75(2) 25–30.

Trienekens, J., J. Bouman, M. Van Der Zwan. 2004. Specification of service level agreements: Problems, principles and practices. Software Quality J. 12 43–57.

Wall Street J. 2006. Web services face reliability challenges. (February 23) B3.

Wang, E. T. G., T. Barron, A. Seidmann. 1997. Contracting structures for custom software development: The impacts of informational rents and uncertainty on internal development and outsourcing. Management Sci. 43(12) 1726–1744.

Whang, S. 1992. Contracting for software development. Management Sci. 38(3) 307–324.
