---
otero_id: 16246
otero_key: "7AAJH8MD"
title: "Joint Product Improvement by Client and Customer Support Center: The Role of Gain-Share Contracts in Coordination"
authors: "Shantanu Bhattacharya; Alok Gupta; Sameer Hasija"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2013.0504"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/7AAJH8MD/fulltext/images/dbacfc15594724617e8eb883d8eea1c367db93139cf3dd86cf20986a927bffa3.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Joint Product Improvement by Client and Customer Support Center: The Role of Gain-Share Contracts in Coordination

Shantanu Bhattacharya, Alok Gupta, Sameer Hasija

## To cite this article:

Shantanu Bhattacharya, Alok Gupta, Sameer Hasija (2014) Joint Product Improvement by Client and Customer Support Center: The Role of Gain-Share Contracts in Coordination. Information Systems Research 25(1):137-151. http://dx.doi.org/10.1287/ isre.2013.0504

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/7AAJH8MD/fulltext/images/c552086900d9d25c2889f682357975b990796d10bb09e6d9154b80e95b0a3c2d.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Joint Product Improvement by Client and Customer Support Center: The Role of Gain-Share Contracts in Coordination

Shantanu Bhattacharya INSEAD, Singapore 138676, shantanu.bhattacharya@insead.edu

Alok Gupta University of Minnesota, Minneapolis, Minnesota 55455, gupta037@umn.edu

Sameer Hasija INSEAD, Singapore 138676, sameer.hasija@insead.edu

W e study the role of different contract types in coordinating the joint product improvement effort of a client and a customer support center. The customer support center’s costly efforts at joint product improvement include transcribing and analyzing customer feedback, analyzing market trends, and investing in product design. Yet this cooperative role must be adequately incentivized by the client, since it could lead to fewer service requests and hence lower revenues for the customer support center. We model this problem as a sequential game with double-sided moral hazard in a principal-agent framework (in which the client is the principal). We follow the contracting literature in modeling the effort of the customer support center, which is the first mover, as either unobservable or observable; in either case, the efforts are unverifiable and so cannot be contracted on directly. We show that it is optimal for the client to offer the customer support center a linear gain-share contract when efforts are unobservable, even though it can yield only the second-best solution for the client. We also show that the cost-plus contracts widely used in practice do not obtain the optimal solution. However, we demonstrate that if efforts are observable then a gain-share and cost-plus options- based contract is optimal and will also yield the first-best solution. Our research provides a systematic theoretical framework that accounts for the prevalence of gain-share contracts in the IT industry’s joint improvement efforts, and it provides guiding principles for understanding the increased role for customer support centers in product improvement.

Keywords: IT outsourcing; gain-share contract; cost-plus contract; joint product improvement; double-sided moral hazard

History: Anitesh Barua, Senior Editor; Karthik Kannan, Associate Editor. This paper was received on October 25, 2011, and was with the authors 5 months for 2 revisions. Published online in Articles in Advance November 27, 2013.

## 1. Introduction

The importance of incorporating customer feedback into the product improvement process has long been recognized. A number of studies have demonstrated the value of incorporating customer feedback into the product improvement process (von Hippel and Katz 2002) and in new services development (Carbonell et al. 2009). However, the avenues of obtaining customer feedback in product design have been increasingly focused on the third parties responsible for customer support on previous versions of products and services. Customer support centers operated by third parties are a primary customer-facing channel for firms in many industries (Aksin et al. 2007). Nambisan and Baron (2009) also report that firms increasingly seek to establish “virtual” customer environments in association with customer support centers. In the traditional model of customer interaction, firms could directly obtain customer feedback on product design and then focus on improvements using the feedback they had gathered. But when support centers are operated by third parties, customer feedback on product design must be incorporated into products jointly with the customer support center partners.

There are important advantages to partnering with customer support centers in the product improvement process. Mehrotra and Grossman (2009) describe how, by using information captured during customer interactions, analysts from the customer support center and the client quantified the impact of specific issues on customer satisfaction and call volumes and then worked with the product engineering, marketing, and documentation groups to eliminate specific problems from future software releases. These improvements resulted in increased customer satisfaction as well as fewer service calls by customers. Thus, although the joint product improvement effort significantly increases the client’s revenues, it also results in fewer service requests to the customer support center and hence lower revenues for the support center.

An illustration of the agency issues arising in a typical joint product improvement effort is given by the partnership between WNX, a service outsourcing firm that provides customer support services, and Travelcountry, an online travel agency.<sup>1</sup> In accordance with standard industry practice (see Hasija et al. 2008), WNX had been compensated historically by Travelcountry on a payment-per service request basis. Revenues for WNX were therefore based on the number of problems that customers encountered when using Travelcountry’s products and services. WNX frequently received requests from customers to help them access their itinerary as they could not access them smoothly because of the design of the website interface. Yet if WNX were to help Travelcountry with the design of their website to improve the accessibility of customer itineraries, then WNX stood to lose a significant stream of revenues because the number of service requests associated with this problem would decrease markedly. At the same time, solving the problem would improve Travelcountry’s product and thus allow it to earn higher revenues. Travelcountry worked closely with WNX to redesign their website (including the itinerary accessing problem) and then compensated WNX by means of a gain-share contract—wherein the gains made because of lower service request volumes are shared with WNX. This case study highlights the agency issues embedded in the cooperation between the customer support center and the client in product improvement. If the customer support center partners with the client on product improvement, the client then profits more from a product that has fewer bugs and thus serves customer needs better, however, unless appropriately compensated by the client, the revenues of the customer support center then stand to decrease because they are contingent on the volume of service requests.

Another example of successfully applying gainshare contracts is provided by Martinez-Jerez et al. (2007), who describe the outsourcing of IT services by Bharti Airtel to IBM in 2004. In this case, IBM provided Bharti Airtel with comprehensive end-toend services for the management of all hardware and software requirements for the IT architecture needed by Bharti and all of the applications needed to operate it. Bharti Airtel was responsible for designing and managing all telecom-specific structures and networks. The contract used to govern this joint product improvement effort was a gain-share contract based on revenues. This joint improvement effort was very successful, and both firms renewed their contract in 2009; the contract grew in value from \$750 million in 2004 to \$2.5 billion in 2009 (Vadlamani 2009).

Gain-sharing contracts are increasingly used in the governance of IT outsourcing relationships between clients and customer support centers (Kapadia 2010), and they feature several managerial advantages: fewer resources required by the client, higher levels of motivation in the customer support center, and the use of targets as milestones (Koelsch 2004). The E-Government Act of 2002 authorized federal agencies in the United States to enter gain-sharing contracts as “sharein-savings initiatives” (Bierce & Kenerson, P.C. 2009). Gain-sharing contracts have also been successfully used by the U.S. Department of Defense (Gartner 2003), and gives both parties an incentive to cooperate and improve the product or service, hence, they are useful tools in joint effort applications. In addition to applications of coordinating the efforts of parties in corporate and governmental applications, gain-share contracts are also widely used for sharing cost savings with employees (Gomez-Mejia and Balkin 2007). In this context, there are three major types of gain sharing: (i) the Scanlon plan, that derives incentives for employees as a function of the ratio of labor costs to sales value of production; (ii) the Rucker plan, that derives incentives based on the ratio of the value of production required for each dollar of the total wage bill; and (iii) the Improshare plan, that derives a standard for the expected hours of production, and any savings between this standard and actual hours of production are shared with the employees (Gomez-Mejia and Balkin 2007).

In the IT context, the use of gain-share contracts is usually applied to projects with prespecified service level agreements (SLAs) for the ongoing management of IT services (Gartner 2003). In the context of our paper, customer support centers (e.g., WNX, IBM) that can effectively take part in the product improvement process of a client are typically information technology enabled service (ITES) providers. These providers are either call centers that remotely provide customer support via Voice over Internet Protocol , or they provide email/Internet chat support. Note that customer support in some settings is provided by field-service engineers, but because of the geographical dispersed nature of field-service support, such service providers do not have the scale required to be able to credibly participate in the client product improvement process. Therefore, customer service that is IT enabled and hence geographically aggregated (BPO firms), is the best setting for our paper. Client firms that use such customer support service providers are often the ones that sell digital goods to their customers. Such goods have a high volume of customer service requests that can be handled remotely. Examples of such client firms are online travel agents such as Travelocountry, online tax service providers such as Intuit, software providers such as Symantec, computer manufacturers such as Dell, e-commerce firms such as Amazon, and mobile telecommunications firms such as Bharti Airtel.

An important element of both the examples above (WNX and IBM) is that both joint improvement efforts were governed by gain-share contracts. Although gain-share contracts are widely used in practice and have been well documented in the practitioner literature, a number of studies caution that gain-share contracts have to be structured well to be effective. In a practitioner blog, Goolsby (2011) points out that revisions or renegotiations of gain-share contracts occur frequently, and these renegotiated contracts have worked well in practice. Wilensky et al. (2007) make a similar point, and posit that the structure of gain-share contracts is an important element in their overall efficiency.

As stated above, in practice, gain-share contracts are structured in terms of the verifiable performance output of the joint effort, and a prespecified target performance output or standard. In this paper, gainshare contracts are structured based on the difference between the verifiable output of the product or service in the market after the improved product is launched, and a prespecified target performance output. Specifically, in this paper, the improved product yields two sets of outputs: more revenues for the client (which is usually not verifiable in the IT context), and fewer potential service requests attended to by the customer support center. The revenues from the improved product may or may not be verifiable by both parties, but the realized volume of service requests handled for the improved product is definitely verifiable by both the client and the customer support center. Our industry observations indicate that the client and the customer support center share data on call volumes or emails answered in real time and also on the cumulative number of calls and emails, so we model gain-share contracts based on service request volumes handled for the improved product with reference to a prespecified target level. Apart from gain-share contracts, cost-plus contracts are also used in IT outsourcing (Gopal and Sivaramakrishnan 2008). We investigate the efficacy of these two prevalent contract types (gain share, cost plus) in the IT industry and compare contractual efficiencies from the perspective of the principal (i.e., the client).

We develop a model of the joint product improvement effort of a client and its customer support center, where the support center’s costly efforts include transcribing and analyzing customer feedback, analyzing market trends, and investing in product design.

The problem is modeled as a sequential-move game in which the customer service center is the first mover in a principal–agent framework. The client is modeled as the principal because it is the client that hires the support center to serve its customers, and hence needs to design appropriate incentive contracts. The successful conclusion of such outsourcing partnerships entails optimal efforts of both parties in the joint improvement effort, but this sequential-move game is complicated by agency issues because of the decentralized decision making of self-interested firms. Although such bilateral efforts may be observable to both parties, they are not verifiable in a court of law and so are not directly contractible, which creates a double-sided moral hazard problem. When efforts are unobservable, the sequential-move game mirrors a simultaneous-move game; hence the double-sided moral hazard problem may lead to inefficiency stemming from the free-rider problem (Holmstrom 1982, Bhattacharyya and Lafontaine 1995, Roels et al. 2010). When efforts are observable but not verifiable, the double-sided moral hazard may lead to suboptimal effort by the support center because of the classic holdup problem (Demski and Sappington 1991, Noldeke and Schmidt 1998, Edlin and Hermalin 2000). Therefore, the design of optimal contracts in the presence of such agency issues is critical for the effective governance of these joint product improvement partnerships.

Our objective is to find if the first-best solution can be achieved where the first-best solution is characterized by (i) both parties making system-optimal efforts, and (ii) the principal attains the maximum profits possible. Specifically, we ask the following questions: (i) What is the optimal contractual structure to be offered by the client if efforts are unobservable? (ii) Can the optimal contract implement the firstbest solution for the client for unobservable efforts? (iii) How do different contracts observed in practice (gain share, cost plus) perform in the case of unobservable efforts? (iv) What is the optimal contractual structure to be offered by the client if efforts are observable but not verifiable, and does it attain the first-best solution?

Our findings are as follows. We show that if efforts are unobservable then the client should offer the customer support center a linear gain-share contract, as it can achieve the optimal solution. However, the optimal solution achieved by the gain-share contract only yields the second-best solution. We also show that cost-plus contracts do not obtain the optimal solution and perform worse than gain-share contracts. Finally, if efforts are observable we show that the optimal contract to be offered by the client is an options-based contract, where the client offers to compensate the customer support center by either a gain-share contract or a cost-plus contract at a later date. Finally, we show that such a gain-share/cost-plus options contract can attain the first-best solution for the client.

The contribution of our results to the literature are as follows. First, in double-sided moral hazard settings the existing literature has assumed that the total output, in the form of revenue, of the joint efforts is contractible (Bhattacharyya and Lafontaine 1995). In our setting such an assumption poses severe restrictions, as it is unlikely that a customer support center or a third party can isolate the impact of product improvement efforts on the increase in revenues for the client from the joint improvement project. In general, the client’s overall revenues from all activities across all projects are verifiable, but the revenues from individual projects are not verifiable in reality, this is an important distinction in our paper from the literature. Instead, we use an objectively verifiable measure, customer service requests, as the contractible metric and show that gain-share contracts based on this metric are an important element of the optimal contract. In our observation from the industry, the call volume of the support center is always verifiable and a part of the contractual agreement. Second, no paper, to the best of our knowledge, has shown that an options-based contract that includes gain-share and cost-plus terms can be designed to attain the first-best outcome when efforts are observable. We note that both these types of contracts are observed widely in practice, and our results present a novel combination of these contract types to attain the first-best outcome. Finally, the holdup problem has been studied empirically in the IS literature. Using an analytical model, we show that the option-based contract can alleviate inefficiency in the system because of holdup by providing sufficient incentives for both parties to invest optimally. We now position our paper with respect to individual articles.

## 1.1. Literature Review

The use of performance-based contracts, including gain-share contracts for governing outsourcing relationships, has been well documented in the IT literature. In this paper, we examine the role of contract design (using contracts that have been widely used in the IT literature) to coordinate the efforts of two parties when they both make efforts toward a common objective (joint improvement of the product). A second feature of this paper is that the efforts of the two parties are sequentially exerted, with the agent (customer support center) making its effort first, followed by the principal (client). The third feature of this paper is that efforts of the support center may or may not be observable. Hence, this paper is aimed at the gap in the IT literature on contract design in environments with double-sided moral hazard and sequential moves by parties with or without observable efforts.

For governing outsourced relationships, the contract design problem has been studied in the IT context of several different applications. In the extant literature on contract design in information systems, a number of studies investigate contract structures from the client’s perspective in the outsourcing of software development and IT services, and the monitoring and control of outsourced activities.

In the study of governance contracts for managing outsourced software development, studies have investigated contractual design (Lee et al. 2013, Dey et al. 2010) as well as the effect of outcome verifiability on contract design (Fitoussi and Gurbaxani 2011). Lee et al. (2013) consider one MSSP (managed security service provider) making an effort in the development of a security system interacting with multiple client firms who exert efforts simultaneously for their specific product (hence, double-sided moral hazard for each party, as the MSSP and each client exert efforts for the client’s security system), and focus on contracts attaining first-best efforts only (and not the highest profits for any one party). They show that multilateral contracts consisting of a fixed ex ante payment to the MSSP and contingent payments ex post that depend on the security status realization of all client firms induce the first-best efforts from all parties. In their paper, Lee et al. (2013) show that multilateral contracting is important to resolve inefficiency due to double-sided moral hazard in their setting. In contrast, the context studied in this paper is different, and our focus is on bilateral contracting between the client and the customer support center. Here, we solve for the principal’s (client) contract design problem with an objective of maximizing its profit, i.e., either attaining the first-best profit or the second best if the first best cannot be attained. Hence, in our paper both the optimal contract structure and the outcome are different (the optimal contract structure is a linear gain-share contract when efforts are unobservable, similar to simultaneous moves, and only the second-best efforts are attained). If efforts are observable, then in our paper, the client can attain the first-best solution by using an options contract that has gain-share and cost-plus terms. Dey et al. (2010) consider the contracting of software projects to an outside developer; they find that fixed-price contracts are appropriate for simple projects with a short development time whereas cost-plus contracts are appropriate for complex projects with a low cost of monitoring. They also study contingent performancebased contracts (with quality as the criterion) and find that such contracts attain the first-best solution. Profit-sharing contracts perform well when the client does not have the power to offer a take-it-or-leaveit contract. Our results show that in double-sided moral hazard environments with sequential moves, (i) performance-based contracts in the form of gainshare contracts are indeed optimal when efforts are unobservable, but performance-based contracts only attain the second-best solution. (ii) Cost-plus contracts are dominated by gain-share contracts in this environment. (iii) When efforts are observable, an options contract using performance-based elements as one option (in the form of a gain-share contract) and cost-plus elements as another option achieve the first-best solution and eliminate the effects of doublesided moral hazard and the holdup problem. Fitoussi and Gurbaxani (2011) find that contract efficiency is strongly influenced by the specific types of performance metrics used, and they offer insights into the design of contracts based on the verifiability of those metrics. Our study adds to this literature by showing that verifiable outputs that only partially capture the impact of the joint effort (support center call volumes) may be sufficient as a contract metric in attaining the first-best solution when the joint output measures like project revenues are not verifiable.

In the context of joint efforts, performance-based contracts in the form of gain sharing have been studied using case-based means in the literature. Wong (2006) provides an application of a gain-share contract based on target costs and actual costs with a software-based decision support system monitoring the progress of the project with respect to the target cost. Agrawal et al. (2005) provide a methodology for the measurement of savings to be shared using gainshare contracts in an information technology environment. Finally, Jiang et al. (2010) show that gain-share contracts perform the useful role of breaking the winner’s curse in outsourcing relationships by mitigating buyer regret. Our study contributes to this stream of literature by providing an analytical justification of the use of gain-share contracts in mitigating the effects of double-sided moral hazard when the efforts are not observable, and in eliminating the effects of double-sided moral hazard and the holdup problem when used in conjunction with cost-plus contracts in an options framework.

In the study of contractual structures for governing IT service outsourcing, Bapna et al. (2010) give prescriptive guidelines for contract design when sourcing from multiple vendors who are competitors but cooperate in a particular project for a common client. The environment described in their study has n-sided moral hazard, and our study provides potential contract designs that could mitigate the effect of moral hazard from the efforts of multiple partners. In addition, monitoring processes are costly but increase the observability of efforts; in this stream of research,

Banker et al. (2006) study the impact of lower monitoring and coordination costs (due to information technology) on the number of suppliers; they find that higher contract completeness may lead to a higher cost per supplier—despite lower coordination and monitoring costs and consequently to a lower number of suppliers. Aron et al. (2008) investigate the role of real-time monitoring enabled by advances in IT and telecommunications. They show that the client can ensure a minimum level of performance by vendors if it commits to a certain level of monitoring. We provide a basis for quantifying the benefits of monitoring information technology projects; these benefits can be estimated in our paper as the difference between the profits from the case when efforts are observable (hence, the client attains the first-best solution) and the case when the efforts are unobservable (the client can only attain the second-best solution).

An important element of contract design in environments with double-sided moral hazard and sequential moves is the mitigation of the holdup problem, which describes the propensity of the client to renegotiate the contract after the agent (as the first mover) has exerted its effort. A recent study of the holdup issue (Susarla et al. 2010) examines the role of contractual provisions and options (to increase the project’s duration) in reducing holdup and find that both provisioning and the extendability of duration have a mitigating effect on the holdup problem. We contribute to this literature by showing that the holdup problem can be eliminated if the parties move sequentially and efforts are observable by creating options-based contracts using gain-share and costplus elements.

Whereas our paper is focused on the impact of contract design on the profitability and the ability to attain the best outcome for the client, a related stream of literature focuses on the impact of contract design on the profitability and survival of vendors. Gopal and Sivaramakrishnan (2008) find that the vendor’s ability to leverage adverse selection results in vendors preferring fixed-price contracts, although timeand-materials contracts are preferred when the risk of employee attrition is high. We contribute to the literature on cost-plus contracts by showing that they do not perform well in environments with double-sided moral hazard and sequential moves when efforts are unobservable, but perform well when used in conjunction with gain-share contracts when efforts are observable. Susarla and Barua (2011) find that the probability of vendor survival is strongly influenced by contractual efficiency, and this influence is stronger when there are adjustment costs associated with shifting to aligned contracts. Gopal et al. (2003) analyze contractual structures for offshore software development contracts as well as the impact of these structures on vendor profits.

Finally, our paper relates to studies in contract theory that consider bilateral investments. Bhattacharyya and Lafontaine (1995) show that a revenue-sharing contract is the optimal solution to the bilateral investment problem with double-sided moral hazard if both parties move simultaneously. We add to this literature by showing that if the revenue is not verifiable, but another metric (support center call volumes) that partially reflects the joint effort is verifiable, then the optimal solution can be attained by a linear gainshare contract with other forms of uncertainty than an exogenous, additive shock. Kim and Wang (1998) show that if the agent (customer support center) is risk-averse, then in a double-sided moral hazard problem with simultaneous moves, the optimal contract is usually nonlinear. In our paper, since the agent is risk neutral, we show that a linear gain-share contract is optimal and replicates any optimal nonlinear contract; further nonlinear static contracts cannot attain the first-best solution for the client when efforts are observable. Also, in contrast to Kim and Wang (1998), we show that options contracts using gain-share and cost-plus elements attain the first-best solution in this case. Roels et al. (2010) show that if the cost to monitor and verify the effort of the other party is incurred, the first-best solution can be achieved by cost-sharing and revenue-sharing contracts; yet the parties make less than their first-best profits because of the monitoring cost, which thereby introduces contractual inefficiency.

In a repair outsourcing setting, Jain et al. (2013) show that tiered penalties can overcome agency issues due to double-sided moral hazard when the agent solves a profit maximization problem subject to a financial distress constraint. However, in their setting, realized downtime, which is a stochastic signal of only the agent’s effort, is contractible. Demski and Sappington (1991), Noldeke and Schmidt (1998), and Edlin and Hermalin (2000) show that if bilateral investments are made sequentially, the first-best solution can be achieved by buyout option contracts under different sets of conditions. Bhattacharya et al. (2013) show that if the agent is risk averse and if the bilateral investments are made sequentially, then the existence of an intermediate verifiable signal can help the principal attain the first-best solution. Our paper contributes to this stream of literature by studying gain-share contracts and cost-plus contracts that are based on the verifiable output of customer service requests, and not on revenues or buyout options.

A summary of the findings of our paper, positioned against the closest papers in the literature, is provided in Table 1.

The rest of the paper is organized as follows. In §2, we describe the model and state our assumptions formally. Section 3 contains the formulation, analysis, and results of the model as well as the main contributions of the paper. Section 4 concludes with a discussion of our findings.

Table 1 Summary of the Most Relevant Literature

<table><tr><td>Papers</td><td>Setting for analysis</td><td>Main findings</td></tr><tr><td>Dey et al. (2010)</td><td>Single-sided moral hazardProfits associated with effort-based quality and time of development</td><td>Fixed-price contracts for simple projectsTime and materials for complex projects with low monitoring costsPerformance-based contracts yield first best</td></tr><tr><td>Lee et al. (2013)</td><td>Double-sided moral hazard with multiple clientsSimultaneous effortsSystem profit maximization</td><td>Multilateral contracts required to attain the first bestInitial fixed payment to provider, with contingent payments on ex post security realization status of all players in the network</td></tr><tr><td>Gopal and Sivaramakrishnan (2008)</td><td>Empirical study on preferences of vendors for contract types</td><td>Vendors prefer fixed-price contracts to leverage private information on capability to maximize information rentVendors prefer time-and-material contracts when risk of employee attrition is high</td></tr><tr><td>Bhattacharyya and Lafontaine (1995)</td><td>Double-sided moral hazardSimultaneous effortsClient revenues are contractibleRisk-neutral agent</td><td>Static revenue sharing contracts are optimal</td></tr><tr><td>Kim and Wang (1998)</td><td>Double-sided moral hazardSimultaneous effortsClient revenues are contractibleRisk-averse agent</td><td>Optimal contracts are nonlinear in realized revenues, but static</td></tr><tr><td>This paper</td><td>Double-sided moral hazardSequential effortsRisk-neutral agentClient revenues are not contractibleCustomer service request volumes are contractible</td><td>When efforts are unobservable, linear gain-share contracts based on customer service requests are optimal but second bestWhen efforts are observable, options-based (nonstatic) contracts, with gain-share and cost-plus terms, are optimal and first best</td></tr></table>

Table 2 Notation and Definitions

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $f(\cdot)$ </td><td>Form of contract</td></tr><tr><td> $s$ </td><td>Support center&#x27;s effort</td></tr><tr><td> $\theta$ </td><td>Client&#x27;s effort</td></tr><tr><td> $I(s)$ </td><td>Support center&#x27;s investment corresponding to effort</td></tr><tr><td> $I_{m}(\theta)$ </td><td>Client&#x27;s investment corresponding to effort</td></tr><tr><td> $m(\theta, s)$ </td><td>Revenue earned by client (stochastic)</td></tr><tr><td> $p(\theta, s)$ </td><td>Probability of service requests</td></tr><tr><td> $u(\theta, s)$ </td><td>Service request volume (stochastic)</td></tr><tr><td> $c$ </td><td>Cost per customer service request</td></tr><tr><td> $V$ </td><td>Market size</td></tr></table>

## 2. Model Description and Assumptions

In this section we describe the formal mathematical model in detail and state our assumptions. The problem is modeled as a sequential game, between the client and the customer support center, in four stages. The sequence of events in our model is described as follows (Figure 1). In the initial stage $( t = 0 )$ , the client proposes a contract $f ( \cdot )$ to the customer support center, where f is based on verifiable outcomes. Next, the customer support center exerts an effort in the first stage (t = 1) of product improvement. Following this, the client makes its effort to improve the product $( t = 2 )$ . Finally, the outcomes of the product improvement efforts are realized $( t = 3 ) ;$ in this case, the expected results are higher revenues for the client and reduced service requests for the customer support center. Table 2 summaries the notation in the paper.

After the contract is offered, the customer support center exerts an effort s in product improvement and incurs an investment of $\bar { I ( s ) }$ . This is followed at t = 2 by the client making an effort  toward product improvement that requires an investment of $\bar { I } _ { m } ( \theta )$ Finally, at $t = 3 ,$ , the outcomes of the product improvement effort by the two parties are realized. Given the efforts  and s, the client earns a revenue of $E [ m ( \theta , s ) ]$ and the probability of service requests at the customer support center is $\overset { \cdot } { p } ( \theta , s )$ . The support center incurs a cost of c per customer service request. The following table summarizes the notation used in the paper.

We make the following assumptions about the model parameters.

<sup>Assumption</sup> <sup>1.</sup> The realized revenue m is a random variable with a pdf parameterized by  and s. We assume

$E [ m ( 0 , s ) ] = m _ { 0 } \forall s \in [ 0 , \infty ] ; \ \partial E [ m ( \theta , s ) ] / \partial \theta \geq 0 \forall \theta \in$ $[ 0 , \infty ] \forall s ; \partial ^ { 2 } E [ m ( \theta , s ) ] / \partial \theta ^ { 2 } \leq 0 \forall \theta , s ; \partial E [ m ( \theta , s ) ] / \partial s \geq 0$ $\forall s \in [ 0 , \infty ] , \forall \theta \in ( 0 , \infty ] ; \partial ^ { 2 } E [ m ( \theta , s ) ] / \partial s ^ { 2 } \leq 0 \forall \theta , s .$

These conditions imply that the client’s revenue is increasing and concave in efforts of both parties and that there is no improvement without the client’s minimal effort. The realized revenues are not verifiable.

<sup>Assumption</sup> <sup>2.</sup> Service support requests follow the binomial distribution parameterized by the market size V and $p ( \theta , s )$ . We also assume that $p ( 0 , s ) = p _ { 0 } \leq 1 \ \forall s \in$ $[ 0 , \dot { \infty } ] ; \partial p ( \theta , s ) / \partial \theta = 0$ as $\theta \to \infty , \ \forall s ; \ \partial p ( \theta , s ) / \partial \theta < 0$ $\forall \theta \in [ 0 , \infty )$ ∀ s; $\partial ^ { 2 } p ( \theta , s ) / \partial \theta ^ { 2 } \geq 0 \ \forall \theta , s ; \ \partial p ( \theta , s ) / \partial s = 0$ as s →  $\forall \theta ; \partial p ( \theta , s ) / \partial s < 0 \forall s \in [ 0 , \infty ) \forall \theta \in ( 0 , \infty ) ;$ $\partial ^ { 2 } p ( \theta , s ) / \partial s ^ { 2 } \geq \dot { 0 } \ \forall \theta , s$ . These conditions imply that the expected number of service requests is decreasing and convex in both parties’ effort and that there is no improvement without the client’s minimal effort.

<sup>Assumption</sup> <sup>3.</sup> We assume that I 4s5 is strictly convex and increasing; $I ( 0 ) = 0 ; I ^ { \prime } ( 0 ) = 0 ; I ^ { \prime } ( \infty ) = \infty ; I _ { m } ( \theta )$ is strictly convex and increasing; ${ \cal I } _ { m } ( 0 ) = 0 ; { \cal I } _ { m } ^ { \prime } ( 0 ) = 0 ;$ $I _ { m } ^ { \prime } ( \infty ) = \infty$

<sup>Assumption</sup> <sup>4.</sup> To rule out the unrealistic case of  as efforts that are optimal we assume that $E [ m ( \infty , s ) ] -$ $c V p ( \infty , s ) - I _ { m } ( \infty ) - I ( s ) < 0 \ \forall s \geq 0$ and $E [ m ( \theta , \infty ) ] \stackrel { - } { - }$ $c V p ( \theta , \infty ) - I _ { m } ( \theta ) - I ( \infty ) < 0 \forall \theta \geq 0 .$

<sup>Assumption</sup> <sup>5.</sup> We assume that the functions $I ( s ) _ { \ast }$ $I _ { m } ( \theta ) , E [ m ( \theta , s ) ]$ , and $p ( \theta , s )$ are continuous, and differentiable in their respective arguments.

Assumptions A1–A4 ensure that the optimal efforts to be exerted by the client () and the customer support center (s) in the joint improvement effort are interior points. The verifiable outcome of the joint efforts of the client and the customer support center at $t = 3$ will be the number of service requests $u ( \theta , s )$ . Observe that this outcome is inseparable in the two efforts, creating a double-sided moral hazard, and that $E [ u ( \theta , s ) ] = V \bar { p } ( \theta , s )$

## 3. Model Formulation and Analysis

In this section, we analyze the contractual structures that could potentially yield optimal outcomes for the client in two scenarios: (i) when efforts exerted by both parties are unobservable, and (ii) when efforts exerted by both parties are observable.

Figure 1 Timeline and Sequence of Events in the Model  
![](/api/attachments/7AAJH8MD/fulltext/images/385606b6956dda31711259e30d5bfd777aaf4027e4a96ee62d8d9b9374feaf63.jpg)

We begin with the sequential game in which the two parties coordinate their efforts to maximize joint profits. Since the efforts by the two parties are exerted sequentially, we determine the optimal efforts using backward induction as follows:

$$
\theta^ {*} (s) = \underset {\theta \geq 0} {\arg \max} \{E [ m (\theta , s) ] - c V p (\theta , s) - I _ {m} (\theta) \},\tag{1}
$$

$$
\begin{array}{c} s ^ {*} = \underset {s \geq 0} {\arg \max} \bigl \{E [ m (\theta^ {*} (s), s) ] - c V p (\theta^ {*} (s), s) \\ - I _ {m} (\theta^ {*} (s)) - I (s) \bigr \}. \end{array}\tag{2}
$$

Equations (1) and (2) determine the first-best efforts $\left( \theta ^ { * } ( s ) , s ^ { * } \right)$ in the coordinated problem of the two parties to maximize their joint profits from the product improvement effort. We now present the results for our two scenarios (based on the observability of efforts), starting with the case where efforts are unobservable.

## 3.1. Unobservable Efforts

If the client offers the customer support center a contract $f$ based on the verifiable outcome $u ( \theta , s )$ , then the client’s problem can be stated as follows:

$$
\max _ {f (\cdot)} \{E [ m (\tilde {\theta}, \tilde {s}) ] - I _ {m} (\tilde {\theta}) - E [ f (u (\tilde {\theta}, \tilde {s})) ] \}\tag{3}
$$

$$
\text { s.t. } \quad \tilde {\theta} = \underset {\theta} {\arg \max} \{E [ m (\theta , \tilde {s}) ] - I _ {m} (\theta) - E [ f (u (\theta , \tilde {s})) ] \},\tag{4}
$$

$$
\tilde {s} = \underset {s} {\arg \max} \{E [ f (u (\tilde {\theta}, s)) ] - c V p (\tilde {\theta}, s) - I (s) \},\tag{5}
$$

$$
E [ f (u (\tilde {\theta}, \tilde {s})) ] - c V p (\tilde {\theta}, \tilde {s}) - I (\tilde {s}) \geq v.\tag{6}
$$

Equation (6) represents the participation constraint for the customer support center (with a reservation value $v \geq 0 )$ , Equation (5) represents the support center’s problem of determining its effort, Equation (4) represents the equivalent problem for the client’s effort, and Equation (3) represents the contract design problem for the client.

Although the decisions made by the two parties are sequential, if efforts are unobservable then (4) and (5) are solved simultaneously by the two parties, because each will base its best response on the reaction functions of the other. Given that efforts are unobservable, the client’s effort will be contingent upon its expectation of the effort to be made by the customer support center. Similarly, the customer support center (as a rational player) will assume that the client will make an effort that is based on the best response to its own effort.

<sup>Proposition</sup> <sup>1.</sup> With unobservable efforts in product improvement, linear gain-share contracts are optimal.

The client, as principal, prefers gain-share contracts with unobservable efforts because they incentivize the customer support center to invest optimally in the product improvement effort. In addition to being compensated for its loss of revenue due to fewer customer service requests, the customer support center has some upside potential from the gain-share contract. Gain-share contracts are increasingly being used in the industry (Kapadia 2010) for the very reason that they induce optimal efforts from both parties even when efforts are unobservable, also they are easy to implement since the cost of monitoring the verifiable outcome is zero. That is, in almost all cases that we have observed in practice, data on customer service requests are already available to the client and are readily available for verification by legal authorities. Kapadia (2010) notes that gain-share contracts need to be structured carefully to be effective. In this regard, Proposition 1 provides guidelines on the optimal structure for such contracts.

There have been other examples of performancebased contracts leading to the optimal outcome. For instance, Dey et al. (2010) show that in the context of outsourced software development projects, performance-based contracts that incorporate quality level agreements achieve the optimal solution. We add to this stream of literature by showing that, when customer support centers perform the role of service providers and participate in product improvement, a gain-share contract (which is a type of a performance-based contract) achieves the optimal solution for the client. We next analyze whether the optimal solution is also the first-best solution from the client’s perspective.

<sup>Lemma</sup> <sup>1.</sup> With unobservable efforts, the optimal gainshare contract attains the second-best solution.

Although the linear gain-share contract is optimal for the client, it cannot completely resolve the freerider problem that stems from double-sided moral hazard. This is consistent with the literature on double-sided moral hazard, as performance-based contracts with simultaneous moves do not attain the first-best outcome for the client (Bhattacharyya and Lafontaine 1995). Lee et al. (2013) show that first-best efforts can be induced by multilateral contracting, whereby two parties pay a penalty to a third contingent on an outcome that is specific to the relationship between the first two parties. In essence, a third party acts as a “budget breaker” for the relationship between two other parties. Since gain-share contracts can attain the optimal solution with unobservable efforts, but they only attain the second-best solution, no contract can attain the first-best solution for the client. In the literature on outsourcing contracts with single moral hazard, performance-based contracts can resolve the single moral hazard issue (Dey et al. 2010). However, an important result of our paper is that in the presence of double-sided moral hazard and unobservable efforts, no contract can attain the firstbest solution for the client. The reason is that the client can only offer outcome-based contracts to the customer support center, and there is no intermediate update of information on the effort exerted by the customer support center. This precludes attaining the first-best solution because the double-sided moral hazard cannot be resolved by performancebased contracts alone. We now investigate whether an alternative, cost-plus contractual structure can replicate the optimal solution. A cost-plus contract is one that compensates the support center for the variable cost of service, cu41 s5, and pays the support center an additional fixed fee, T , such that $E [ \hat { f } ( u ( \theta , s ) ) ] =$ $c V p ( \theta , s ) + T$

<sup>Lemma</sup> <sup>2.</sup> With unobservable efforts in product improvement, a cost-plus contract is not optimal.

Cost-plus contracts are widely used for governing outsourced IT projects, and they have been shown to be efficient in governing outsourced software development contracts in some special cases, as when auditing effort is efficient and effective and so the cost of monitoring is low (Dey et al. 2010). Gopal and Sivaramakrishnan (2008) find that time-and-materials contracts (a type of cost-plus contract) perform well when there is a high risk of project team member attrition. Cost-plus contracts do not perform optimally in the case of bilateral efforts with double-sided moral hazard and no observability for reasons that are similar to the case of single sided moral hazard (Dey et al. 2010). Cost-plus contracts must be monitored in the case of single moral hazard as vendors have the incentive to inflate costs. In the context of this paper, the support center’s effort cannot be directly contracted on because efforts are not verifiable. In addition, the fixed fee with the cost in cost-plus contracts does not adequately incentivize the service provider to invest in the joint product improvement effort, because it is not linked to the improvement achieved—unlike gain-share contracts, in which the service provider’s incentive for product improvement is linked to the effort invested. Hence cost-plus contracts are less efficient than gain-share contracts in coordinating the efforts of the two parties. Similarly, fixed-fee only contracts do not provide the support center an incentive to exert sufficient effort toward the client’s product improvement initiative. The reason for this is that, under a fixed-fee contract the marginal gain for the support center from product improvement is solely from the reduction in the transaction cost associated with serving customers, whereas the optimal gainshare contract provides incentives for the support center via a financial reward, in addition to the transaction cost savings, associated with the reduction in customer service requests.

We next analyze the joint product improvement problem when efforts made by both parties are observable.

## 3.2. Observable Efforts

When the efforts made by both parties are observable, the problem faced by the client is described formally as follows:

$$
\max _ {f (\cdot)} \{E [ m (\tilde {\theta} (\tilde {s}), \tilde {s}) ] - I _ {m} (\tilde {\theta} (\tilde {s})) - E [ f (u (\tilde {\theta} (\tilde {s}), \tilde {s})) ] \}\tag{7}
$$

$$
\begin{array}{r l} \text {s.t.} & \tilde {\theta} (s) = \underset {\theta} {\arg \max} \bigl \{E [ m (\theta , s) ] - I _ {m} (\theta) \\ & \qquad - E [ f (u (\theta , s)) ] \bigr \}, \end{array}\tag{8}
$$

$$
\begin{array}{c} \tilde {s} = \underset {s} {\arg \max} \bigl \{E [ f (u (\tilde {\theta} (s), s)) ] \\ - c V p (\tilde {\theta} (s), s) - I (s) \bigr \}, \end{array}
$$

$$
E [ f (u (\tilde {\theta} (\tilde {s}), \tilde {s})) ] - c V p (\tilde {\theta} (\tilde {s}), \tilde {s}) - I (\tilde {s}) \geq v.\tag{9}
$$

(10)

As before, Equation (10) represents the participation constraint for the customer support center; Equation (9) represents the support center’s problem of determining its effort. Note that the support center will now exert its effort while taking the client’s bestresponse function into account. Equation (8) represents the equivalent problem for the client’s effort, which is a function of the customer support center’s observable effort s, and Equation (7) represents the contract design problem for the client. We investigate the efficiency of different contractual structures, starting with static contracts (noncontingent contracts that are not options based and cannot be renegotiated), in obtaining the first-best solution.

<sup>Proposition</sup> <sup>2.</sup> With observable efforts, no static contract can yield the first-best outcome.

The result that static contracts do not attain the firstbest solution, even if efforts are observable, is based on the conditions for obtaining the first-best outcome under double-sided moral hazard. In the centralized problem, the first-best effort by the client is obtained via Equation (1), which gives the expected revenues from the joint improvement effort to the client minus the cost of servicing customer requests and the cost of effort exerted by the client. A contract will not elicit the client’s first-best efforts unless all the upside (from the joint improvement project) accrues to the client; yet by retaining all the upside, the client leaves no incentive for the customer support center to invest in the product improvement effort. No static contract will be able to incentivize both firms adequately to invest their first-best efforts, so static contracts do not obtain the first-best solution. This is an important insight for the analysis of optimal contracts for coordinating joint product improvement efforts. We now consider options-based contracts to see whether they can yield the client’s first-best solution to the joint product improvement problem.

<sup>Proposition</sup> <sup>3.</sup> With observable efforts, a gain share/ cost-plus option contract is optimal and attains the firstbest solution. Here the client can use one of two options below to compensate the support center, and the exercise date of the option is set at $t \in ( 2 , 3 )$ , i.e., when both parties have made their respective efforts in product improvement.

Option 1: Pay the support center using a gain-share contract.

Option 2: Pay the support center using a cost-plus contract.

The intuition behind Proposition 3 is as follows. The client offers the customer support center two different contractual structures and retains the option of eventually compensating the support center using either structure. Option 1 is a gain-share contract, and option 2 is a cost-plus contract. As we show in the proof, the support center will exert an effort $s ^ { * }$ and the client will subsequently exert an effort $\theta ^ { * }$ and choose to compensate the support center using the cost-plus contract. The intuition of the outcome of the option contract is straightforward. If the support center chooses to exert an effort $s < s ^ { * }$ then the cost-plus contract will leave a surplus for the support center; hence the client will prefer to exert an effort $\theta < \theta ^ { * }$ and choose the gain-share contract (see Figure $2$ to see the client’s preference for the gain-share option for $s < s ^ { * } )$ . In this case the outcome of the joint product improvement effort will be suboptimal and the contract will lead to lower payments to the support center than its required reservation value. To prevent this from occurring the support center will exert the system-optimal effort, to induce the client to choose the cost-plus option (see Figure 2), and thereby incentivize the client to exert its own system-optimal effort and to choose the cost-plus contract (under the costplus contract, the client has an incentive to invest the system-optimal effort). The client sets the contract parameters in such a way that, at $s ^ { * }$ , the support center earns a profit equal to its reservation value under the cost-plus contract and hence the client attains the first-best profit. Notice that the support center will not choose an effort greater than the system-optimal level, since doing so would lead to a lower profit for the support center than its reservation value (because then the client would choose the cost-plus contract).

An interesting insight from Proposition 3 is that these options-based contracts are robust to renegotiation. In general sequential move games, renegotiation is caused because of the holdup problem, wherein the second mover may be in a position to lower the transfer payment to the first mover after the first mover’s effort has been sunk. Moreover, Gartner (2005) points out that outsourcing contracts frequently get renegotiated in practice, and over 55 % of existing outsourcing contracts (in a survey of 200 executives of midsize and large companies) have already been renegotiated in practice. The options-based contracts presented in Proposition 3 are robust to renegotiation, due to the fact that the exercise date of the options contract is after the second mover has also exerted its effort. The exercise time of the options contract is important as it precludes the second mover (client) from holding up the first mover, as any such threat is not credible. This is because, given that one of the options is a costplus option and that the support center has exerted its first-best effort, the client is better off exerting its firstbest effort and choosing the cost-plus option (thereby earning first-best profits). Our result that gain-share contracts used in conjunction with cost-plus contracts in an options framework attain the first-best solution provides an important guide to firms about the structuring of gain-share contracts with sequential moves (as renegotiation happens only in sequential move games).

The mechanics of this options contract are illustrated in Figure 2, where we have taken the functional forms of ${ \overset { \smile } { m } } ( \theta , s ) = 5 \theta ( 1 + s ^ { 0 . 5 } ) , \ p ( \theta , s ) = e ^ { - 0 . 0 1 \theta ( 1 + s ) } ,$ $I _ { m } ( \theta ) = \theta ^ { 2 } / 2 , \ I ( s ) = s ^ { 2 } / 2 ,$ and $V = 1 0 0$ . The support cente ${ \bf \chi } ^ { \prime } { \bf s }$ reservation value of profits is taken as $v = 0 .$

Figure 2 shows that the support center prefers to be compensated by the cost-plus option for all levels of effort it exerts in product improvement. However the client prefers the gain-share option to compensate the support center, unless the support center exerts the system-optimal effort. Hence, the support center finds it optimal to exert the system-optimal effort $( s ^ { * } = 1 6 )$ because doing so maximizes its total profit. This gives the support center a total expected profit equal to its reservation value, so the client finds it optimal to exert the system-optimal effort level $\theta ^ { * } ,$ thus this contract mechanism yields the first-best outcome for the client.

Studies in economics have shown that buyout options implement the first-best solution in bilateral investment games with double-sided moral hazard (Demski and Sappington 1991, Noldeke and Schmidt 1998, Edlin and Hermalin 2000). However, buyout options are impractical to implement in the context of joint product improvement effort. Buyout contracts rely on the assumption that the agent can buy the entire firm of the principal. But given that customer support centers are usually small, buyout option contracts are impractical in the cases that we study. Finally, in our context, revenue-sharing options contracts are also difficult to implement as most clients that cooperate with customer support centers are large and have multiple products in their portfolios; hence the revenues that they publicly declared consist of revenues from multiple streams, so it may not be possible to verify which revenues have been generated by the cooperative effort on any particular product. Second, few privately owned companies declare their revenues publicly, in which case there may be adverse selection effects on the revenues declared by the client from the joint product improvement. Therefore, in cases where revenues from the product improvement initiative are not objectively verifiable, it is not easy to implement contractual agreements that are contingent on such revenues.

Figure 2 Mechanics of Gain-Share/Cost-Plus Options Contract  
![](/api/attachments/7AAJH8MD/fulltext/images/af91bc0c3e2f5820ee5f376c2331dfb85a750ce181834d40eed15d27205ff90b.jpg)

In contrast, gain-share and cost-plus contracts studied in this paper are both widely used in practice, and our analysis in the previous section showed that, while gain-share contracts are indeed optimal when efforts are unobservable, cost-plus contracts do not perform as well. The advantage of the gain-share contract studied in this paper is that it relies on gains achieved via reduction in customer service request volumes, an objectively verifiable metric. When efforts are observable, we show that gain-share and cost-plus contracts can be used effectively in combination (through the use of options to choose either one of the two) to attain the first-best solution. The literature has most often studied single-sided moral hazard that arises when an agent implements an unverifiable action for the principal (Gopal and Sivaramakrishnan 2008, Dey et al. 2010, Fitoussi and Gurbaxani 2011) and has found that these contracts perform well under different conditions. We show in a normative model that—in the context of double-sided moral hazard, where both parties invest in efforts toward joint product improvement and those efforts are observable—a combination of these widely used contracts achieves the first-best solution and also performs better than either contract individually. Implementing such an options contract should not be difficult in practice as the individual contract types are already widely used in practice. Furthermore, different types of embedded options are often provisioned in customer support outsourcing contracts in practice.<sup>2</sup>

## 4. Conclusions and Future Research

In this paper we study the cooperative product improvement effort of a client and a customer support center, where the client must incentivize the support center to make its first-best effort, and must also compensate the support center for its revenue loss caused by the potential fewer service requests following the joint product improvement effort. We model the problem as a sequential bilateral game between the two parties with double-sided moral hazard. Our findings can be summarized as follows. When efforts are unobservable: (i) the client should offer the customer support center a linear gain-share contract as it yields the optimal solution; (ii) the optimal solution achieved by the gain-share contract attains only the secondbest solution; (iii) cost-plus contracts do not yield the optimal solution and, moreover perform worse than the gain-share contracts. Our results contribute to the literature in a number of ways. First, in doublesided moral hazard settings the existing literature has assumed that the total output of the joint efforts is contractible. In IT settings with joint efforts at improvement, it is unlikely that a customer support center or a third party can isolate the impact of product improvement efforts on the increase in revenues for the client from the joint improvement project. In general, the client’s overall revenues from all activities across all projects are verifiable, but the revenues from individual projects are not verifiable in reality, this is an important distinction in our paper from the literature. Instead, we use an objectively verifiable measure, customer service requests, as the contractible metric and show that gain-share contracts based on this metric are an important element of the optimal contract. Second, cost-plus contracts have been shown to perform well in the literature in single-sided moral hazard in certain settings (Dey et al. 2010, Gopal and Sivaramakrishnan 2008), we show that if efforts are unobservable, costplus contracts never attain the second-best outcome. Finally, Lee et al. (2013) show that in such settings, the first-best efforts can be attained, but that requires multilateral contracting. We show that under bilateral contracting, linear gain-share contracts are optimal, but attain only the second-best outcome, and hence, the first-best outcome cannot be attained by any contractual form.

When efforts are observable, (i) static contracts (including gain-share and cost-plus contracts) do not yield the first-best solution because they cannot adequately incentivize both parties to invest their firstbest efforts; (ii) the optimal contract to be offered by the client is an options-based contract, where the client offers to compensate the customer support center either by a gain-share or a cost-plus contract, and the option will be exercised by the client after both parties have sunk their efforts. Finally, we show that such a gain-share/cost-plus option contract can attain the first-best solution for the client.

Our results have a number of implications. First, we provide theoretical support for the use of gainshare and cost-plus contracts in combination in joint product improvement effort with double-sided moral hazard when efforts are observable. The observability of efforts is a function of the degree of cooperation between the client and the customer support center. If the two parties work closely together, as we observed in the example cases of WNX and Travelcountry and of Bharti Airtel and IBM, then the observability of efforts is a valid assumption because the client can closely monitor the effort of the customer support center. However, if the two parties work in an arm’s-length relationship then the unobservability of efforts would be the more valid assumption. In this case we show that gain-share contracts are optimal and perform better than cost-plus contracts, though no individual contract can achieve the first-best solution for the client.

Our results contribute to the extant literature in a number of ways. First, performance-based contract design has been studied in the single moral hazard case in terms of the number of performance metrics used (Fitoussi and Gurbaxani 2011), the effect of task complexity on agency issues (Susarla et al. 2010), the kind of contracts to be used under different scenarios (Dey et al. 2010), and the vendor’s preferred contractual designs (Gopal and Sivaramakrishnan 2008). We add to this literature by considering the issues of double-sided moral hazard and holdup, and we show that options-based combinations of gain-share and cost-plus contracts perform best when efforts are observable, whereas specific performance-based contracts (gain share) perform best when efforts are unobservable. We also add to the economic literature by showing that options-based contracts that are not based on buyout but rather on contract types that are widely used in practice can coordinate the two parties’ efforts to yield the first-best solution.

As the research in this area is in the nascent stage, there are a number of avenues that should be addressed by future research. First, if both the customer support center and the client make additional efforts in other tasks (e.g., efforts in improving the quality of service), then it would be interesting to look at the changes in the structure of the optimal contracts under multitasking double-sided moral hazard settings. Second, it would be interesting also to investigate the impact of risk aversion on the part of the customer support center on the nature of optimal contracts. The analysis presented in the paper has some limitations that we believe should be of interest for future studies. For example, we limit our analysis to a single period setting, whereas the setting studied in this paper may also be applicable to many multiperiod settings, where the parties undertake a product improvement effort in each period. We have also ignored the effects of competition, both in the product market faced by the client and in the service market faced by the support center. It will be interesting to study the effects of competition on the joint product improvement efforts of the client and the customer support center. Our work assumes symmetric information between the client and the support center. It is possible that in some settings the client and the support center may have access to private information, which would significantly increase the economic tension in the model. Finally, in this paper we use customer service requests as the contractible metric for the client’s product improvement initiative. In many situations there may be other metrics associated with product development and improvement, such as approval by a regulatory authority for new products, including which may provide the possibility of studying a wider range of contractual mechanisms. We believe that the role of the customer support center in the client’s product improvement effort is a rich setting with many opportunities for future research that can address some of the issues not addressed in this paper.

This paper looks at the practice of joint product improvement efforts and models the impact of double-sided moral hazard on the contracts described in the literature and observed in practice between clients and customer support centers. Our findings indicate that clients could make better decisions when designing contracts for customer support centers, and the framework proposed in this paper can serve as a guide in this regard.

## Appendix

Proof of Proposition 1. <sub>Assume</sub> <sub>that</sub> $f ( \cdot ) = f _ { o } ( \cdot )$ is the optimal contract for the client and also assume that, for the optimal contract, <sup>˜</sup>, s˜ are interior points. We will show later that our assumptions ensuring that $\theta ^ { * } , s ^ { * }$ are interior points are sufficient to ensure that $\tilde { \theta } , \tilde { s }$ are interior points. Therefore,

$$
\left. \frac {\partial E [ m (\theta , \tilde {s}) ]}{\partial \theta} \right| _ {\theta = \tilde {\theta}} - \left. \frac {\partial I _ {m} (\theta)}{\partial \theta} \right| _ {\theta = \tilde {\theta}} - \left. \frac {\partial E [ f _ {o} (u (\theta , \tilde {s})) ]}{\partial \theta} \right| _ {\theta = \tilde {\theta}} = 0,\tag{11}
$$

$$
\left. \frac {\partial E [ f _ {o} (u (\tilde {\theta} , s)) ]}{\partial s} \right| _ {s = \tilde {s}} - c V \left. \frac {\partial p (\tilde {\theta} , s)}{\partial s} \right| _ {s = \tilde {s}} - \left. \frac {\partial I (s)}{\partial s} \right| _ {s = \tilde {s}} = 0.\tag{12}
$$

Suppose we have a linear gain-share contract $E [ f ( u ( \theta , s ) ) ] =$ $a \bar { V [ p _ { 0 } - p ( \theta , s ) ] } + b$ . Set the value of a such that,

$$
a = \frac {1}{V} \left[ \sum_ {x = 0} ^ {V} \binom {V} {x} f _ {o} (x) p (\tilde {\theta}, \tilde {s}) ^ {x - 1} (1 - p (\tilde {\theta}, \tilde {s})) ^ {V - x - 1} (- x + V p (\tilde {\theta}, \tilde {s})) \right]
$$

and the value of b such that

$$
b = v - a V [ p _ {0} - p (\tilde {\theta}, \tilde {s}) ] + c V p (\tilde {\theta}, \tilde {s}) + I (\tilde {s}).
$$

Our claim is that such a linear gain-share contract will replicate the optimal contract $f _ { o } ( \cdot )$ . For the linear gain share contract, the first-order conditions are

$$
\begin{array}{l} \frac {\partial E [ m (\theta , s) ]}{\partial \theta} - \frac {\partial I _ {m} (\theta)}{\partial \theta} + a V \frac {\partial p (\theta , s)}{\partial \theta} = 0, \\ - a V \frac {\partial p (\theta , s)}{\partial s} - c V \frac {\partial p (\theta , s)}{\partial s} - \frac {\partial I (s)}{\partial s} = 0. \end{array}
$$

Substituting the values of a yields

$$
\begin{array}{l} \frac {\partial E [ m (\theta , s) ]}{\partial \theta} - \frac {\partial I _ {m} (\theta)}{\partial \theta} - \left[ \sum_ {x = 0} ^ {V} \binom {V} {x} f _ {o} (x) p (\tilde {\theta}, \tilde {s}) ^ {x - 1} q (\tilde {\theta}, \tilde {s}) ^ {V - x - 1} \right. \\ \cdot (- x + V p (\tilde {\theta}, \tilde {s})) \Bigg ] \frac {\partial p (\theta , s)}{\partial \theta} = 0, \end{array}\tag{13}
$$

$$
\begin{array}{l} \left[ \sum_ {x = 0} ^ {V} \binom {V} {x} f _ {o} (x) p (\tilde {\theta}, \tilde {s}) ^ {x - 1} q (\tilde {\theta}, \tilde {s}) ^ {V - x - 1} (x - V p (\tilde {\theta}, \tilde {s})) \right] \frac {\partial p (\theta , s)}{\partial s} \\ - c V \frac {\partial p (\theta , s)}{\partial s} - \frac {\partial I (s)}{\partial s} = 0, \end{array} \tag {14}
$$

where $q ( \theta , s ) = 1 - p ( \theta , s )$ . It is easy to see that (13) and (14) are satisfied at $\{ { \widetilde { \theta } } , { \widetilde { s } } \}$ . It is also easy to check that the second-order conditions are satisfied, and hence $\{ \tilde { \theta } , \tilde { s } \}$ are the outcome of the linear gain-share contract. Furthermore, the constant term of the linear gain-share contract is set such that no additional surplus is paid to the customer support center; hence the linear gain-share contract can replicate the optimal contract. Next we show that, given our assumptions on the relevant functions, $\tilde { \theta } , \tilde { s }$ are interior points. Our assumptions on the cost functions $I _ { m } ( \theta )$ and $I ( s )$ rule out $\infty ,$ so we need only show that $\widetilde { \theta } , \widetilde { s } \neq 0$ . First let us assume that $\tilde { \theta } = 0 .$ . This implies that $\widetilde s = 0 ,$ as when the client exert no effort, the support center’s effort yields no improvement in the product and the client’s profit is $m _ { 0 } -$ $f _ { o } ( V p _ { 0 } )$ . Now let us consider a different contract $f ( u ( \theta , s ) ) =$ $c u ( \theta , s ) + T$ . Under this contract the support center’s optimal effort is $s = 0$ . However, we note that $\partial E [ m ( \theta , 0 ) ] / \bar { \partial \theta } -$ $\partial I _ { m } ( \theta ) / \partial \theta - c V ( \partial p ( \theta , 0 ) / \partial \theta ) > 0 \mathrm { ~ a t ~ } \theta = 0 .$ . Hence under this contract the client’s optimal effort is $\theta > 0$ . Set T such that $T = f _ { o } ( V p _ { 0 } ) - c V \overline { { p _ { 0 } } }$ . Then the client’s expected profit under this contract is $\begin{array} { r } { E [ m ( { \theta } , 0 ) ] - I _ { m } ( \theta ) - c V p ( \theta , 0 ) - T > } \end{array}$ $V m _ { 0 } - f _ { o } ( V p _ { 0 } ) ;$ which yields a contradiction. Now let us assume that $\tilde { s } = 0$ and $\tilde { \theta } > 0 .$ . The client’s expected profit is then, $E [ m ( \tilde { \theta } , 0 ) ] - I _ { m } ( \tilde { \theta } ) - E [ f _ { 0 } ( u ( \tilde { \theta } , 0 ) ) ]$ , and this implies that $\partial E [ f _ { o } ( u ( \tilde { \theta } , s ) ) ] / \partial s - c V ( \partial p ( \tilde { \theta } , s ) / \partial s ) - \partial I ( s ) / \partial s \leq 0 \ \forall \hat { s } \geq 0$ Let us consider a different contract $f ( u ( \theta , s ) ) = T$ . Under this contract, $\partial E [ m ( \theta , s ) ] / \partial \theta - \partial I _ { m } ( \theta ) / \partial \theta > 0$ at $\theta = 0 ~ \forall s$ Hence under this contract the client’s optimal effort is $\theta > 0 ,$ which implies that $- c V ( \partial p ( \theta , s ) / \partial s ) - \bar { \partial } I ( s ) / \partial s > 0 \mathrm { a t } s = 0 .$ In this case, the optimal effort of the support center is $s > 0 .$ Now set $T$ such that $T = E [ f _ { o } ( u ( \tilde { \theta } , 0 ) \bar { ) } ]$ . Then the client’s expected profit under this contract is $E [ m ( \theta , s ) ] - I _ { m } ( \theta ) - T \geq$ $\begin{array} { r } { E [ \tilde { m } ( \tilde { \theta } , s ) ] - I _ { m } ( \tilde { \theta } ) - T > E [ m ( \tilde { \theta } , 0 ) ] - \bar { I } _ { m } ( \tilde { \theta } ) - E [ f _ { o } ( u ( \tilde { \theta } , 0 ) ) ] . } \end{array}$ which also yields a contradiction. Therefore, a contract that induces zero effort from either party cannot be optimal, and there exists at least one contract that leads to interior solutions for the efforts. This completes the proof.

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>1.</sup> By Proposition 1, we know that the linear gain-share contract is optimal. So to prove Lemma 1 it is sufficient to show that no linear gain-share contract will attain the first-best outcome. Let us assume that this is not true and ∃ a linear gain-share contract $\{ a _ { o } , b _ { o } \}$ that does attains the first-best outcome. This would imply that

$$
\left. \frac {\partial E [ m (\theta , s ^ {*}) ]}{\partial \theta} \right| _ {\theta = \theta^ {*}} - \left. \frac {\partial I _ {m} (\theta)}{\partial \theta} \right| _ {\theta = \theta^ {*}} + a V \frac {\partial p (\theta , s ^ {*})}{\partial \theta} \bigg | _ {\theta = \theta^ {*}} = 0,\tag{15}
$$

$$
- a V \frac {\partial p (\theta^ {*} , s)}{\partial s} \bigg | _ {s = s ^ {*}} - c V \frac {\partial p (\theta^ {*} , s)}{\partial s} \bigg | _ {s = s ^ {*}} - \frac {\partial I (s)}{\partial s} \bigg | _ {s = s ^ {*}} = 0.\tag{16}
$$

From the definition of $\{ \theta ^ { * } , s ^ { * } \}$ we know that

$$
\left. \frac {\partial E [ m (\theta , s ^ {*}) ]}{\partial \theta} \right| _ {\theta = \theta^ {*}} - \left. \frac {\partial I _ {m} (\theta)}{\partial \theta} \right| _ {\theta = \theta^ {*}} - c V \frac {\partial p (\theta , s ^ {*})}{\partial \theta} \bigg | _ {\theta = \theta^ {*}} = 0,\tag{17}
$$

$$
\left. \frac {\partial E [ m (\theta^ {*} , s) ]}{\partial s} \right| _ {s = s ^ {*}} - c V \left. \frac {\partial p (\theta^ {*} , s)}{\partial s} \right| _ {s = s ^ {*}} - \left. \frac {\partial I (s)}{\partial s} \right| _ {s = s ^ {*}} = 0.\tag{18}
$$

Comparing (15) and (17) yields that $a = - c$ . However, if $a = - c$ then (16) cannot be true because $s ^ { * }$ is an interior point. This contradiction completes our proof.

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>2.</sup> Let the outcome of the effort game between the client and the support center be $\left\{ \theta _ { C } , s _ { C } \right\}$ under the cost-plus contract $( E [ f ( u ( \bar { \theta , } s ) ) ] = c V p ( \theta , s ) + T )$ , where the first-order conditions for the client’s and support center’s effort game are (respectively)

$$
V \frac {\partial E [ m (\theta , s _ {C}) ]}{\partial \theta} \bigg | _ {\theta = \theta_ {C}} - \frac {\partial I _ {m} (\theta)}{\partial \theta} \bigg | _ {\theta = \theta_ {C}} - c V \frac {\partial p (\theta , s _ {C})}{\partial \theta} \bigg | _ {\theta = \theta_ {C}} = 0,\tag{19}
$$

$$
- \frac {\partial I (s)}{\partial s} \bigg | _ {s = s _ {C}} = 0.\tag{20}
$$

By $( 2 0 ) , s _ { C } = 0 .$ . From the proof of Proposition 1, we know that the optimal second-best efforts, <sup>˜</sup> and s˜, are interior points. Therefore, the cost-plus contract cannot attain the optimal second-best.

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>2.</sup> Assume that a static contract $f _ { o } ( \cdot )$ is the optimal static contract. Since the client observes the support center’s effort, the client’s effort is given by

$$
\tilde {\theta} (s) = \underset {\theta} {\arg \max} \{E [ m (\theta , s) ] - I _ {m} (\theta) - E [ f (u (\theta , s)) ] \}.\tag{21}
$$

The support center’s optimal effort is

$$
\tilde {s} = \underset {s} {\arg \max} \{E [ f (u (\tilde {\theta} (s), s)) ] - c V p (\tilde {\theta} (s), s) - I (s) \}.\tag{22}
$$

To complete our proof, it is sufficient to show that either $\tilde { \theta } ( s ^ { * } ) \neq \bar { \theta } ^ { * } \ \mathrm { o r } \ \tilde { s } \neq \bar { s ^ { * } }$ . For this it is enough to show that the first-order conditions under the static contract do not align with the first-order conditions for coordination. The firstorder condition for the client under contract $f _ { o } ( \cdot )$ is

$$
\left. \frac {\partial E [ m (\theta , \tilde {s}) ]}{\partial \theta} \right| _ {\theta = \tilde {\theta}} - \left. \frac {\partial I _ {m} (\theta)}{\partial \theta} \right| _ {\theta = \tilde {\theta}} - \left. \frac {\partial E [ f _ {o} (u (\theta , \tilde {s})) ]}{\partial \theta} \right| _ {\theta = \tilde {\theta}} = 0.\tag{23}
$$

For $\tilde { \theta } ( s ^ { * } ) = \theta ^ { * }$ we need that

$$
\left. \frac {\partial E [ f _ {o} (u (\theta , s ^ {*})) ]}{\partial \theta} \right| _ {\theta = \theta^ {*}} = c V \left. \frac {\partial p (\theta , s ^ {*})}{\partial \theta} \right| _ {\theta = \theta^ {*}}.\tag{24}
$$

We can rewrite Equation (24) as

$$
c = \frac {1}{V} \left[ \sum_ {x = 0} ^ {V} \binom {V} {x} f _ {o} (x) p (\theta^ {*}, s ^ {*}) ^ {x - 1} (1 - p (\theta^ {*}, s ^ {*})) ^ {V - x - 1} \right.
$$

$$
\left. \cdot (x - V p (\theta^ {*}, s ^ {*})) \right].\tag{25}
$$

The first-order condition for the support center under contract $f _ { o } ( \cdot )$ is

$$
\begin{array}{c} \left[ \left(\frac {\partial E [ f _ {o} (u (\theta , \tilde {s})) ]}{\partial \theta} - c V \frac {\partial p (\theta , \tilde {s})}{\partial \theta}\right) \Big | _ {\theta = \tilde {\theta}} \frac {\partial \tilde {\theta} (s)}{\partial s} + \frac {\partial E [ f _ {o} (u (\tilde {\theta} , s)) ]}{\partial s} \right. \\ \left. - c V \frac {\partial p (\tilde {\theta} , s)}{\partial s} - \frac {\partial I (s)}{\partial s} \right] \Big | _ {s = \tilde {s}} = 0. \end{array}
$$

For $\widetilde { \boldsymbol { s } } = \boldsymbol { s } ^ { * }$ and $\tilde { \theta } ( s ^ { * } ) = \theta ^ { * }$ we need that

$$
\begin{array}{l} \left[ \left(\frac {\partial E [ f _ {o} (u (\theta , s ^ {*})) ]}{\partial \theta} - c V \frac {\partial p (\theta , s ^ {*})}{\partial \theta}\right) \Big | _ {\theta = \theta^ {*}} \frac {\partial \tilde {\theta} (s)}{\partial s} \right. \\ \left. + \frac {\partial E [ f _ {o} (u (\theta^ {*} , s)) ]}{\partial s} - c V \frac {\partial p (\theta^ {*} , s)}{\partial s} - \frac {\partial I (s)}{\partial s} \right] \Big | _ {s = s ^ {*}} = 0. \end{array}
$$

Replacing (24) and (25) yields

$$
- \left. \frac {\partial I (s)}{\partial s} \right| _ {s = s ^ {*}} = 0.\tag{26}
$$

Because $s ^ { * }$ is an interior point, (26) implies that the conditions for $\tilde { s } = s ^ { * }$ and $\tilde { \theta } ( s ^ { * } ) \stackrel { = } { = } \theta ^ { * }$ are not satisfied. Therefore, an optimal static contract cannot attain the first-best solution.

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>3.</sup> Under the gain-share option (Option 1) the support center’s expected profit function is $\mathrm { \hat { H } } _ { s } ( \theta , s ) = a V ( p _ { 0 } \dot { - } p ( \theta , s ) ) + b - \hat { I ( s ) } - c \hat { V p ( \theta , s ) } ;$ and the client’s expected profit is $\Pi _ { m } ( \theta , s ) = { \cal E } [ m ( \theta , s ) ] - { \cal I } _ { m } ( \theta ) -$ $a V ( p _ { 0 } - p ( { \bar { \theta } } , s ) ) - \mathbf { \bar { \theta } }$ . Similarly under the cost-plus option (option 2) the expected profits are $\Pi _ { s } ( \theta , s ) = c V p ( \theta , s ) +$ $F - I ( s ) - c V p ( \theta , s ) ;$ and $\Pi _ { m } ( \theta , s ) = { \cal E } [ m ( \theta , s ) ] - { \cal I } _ { m } ( \theta ) -$ $c V p ( \theta , s ) - F$ . We will show that a gain-share/cost-plus option contract based on the contracts described above will yield the first-best outcome for the client. Set a such that the client’s best response under option 1 for any $s \in [ 0 , s ^ { * } ]$ is $\theta = 0 .$ . First we will show that a finite a will achieve this. We want

$$
\frac {\partial E [ m (\theta , s) ]}{\partial \theta} + a V \frac {\partial p (\theta , s)}{\partial \theta} - \frac {\partial I _ {m} (\theta)}{\partial \theta} \leq 0 \quad \forall \theta , \forall s \in [ 0, s ^ {*} ].\tag{27}
$$

Observe that, for $a > 0 , ( 2 7 )$ holds $\forall \theta \geq { \tilde { \theta } } ( s )$ , where

$$
\tilde {\theta} (s) = \underset {\theta} {\arg \left\{\frac {\partial E [ m (\theta , s) ]}{\partial \theta} - \frac {\partial I _ {m} (\theta)}{\partial \theta} \right\}} = 0.\tag{28}
$$

It can be shown via the implicit function theorem that $\partial { \tilde { \theta } } ( s ) / \partial s \geq 0 .$ . Furthermore by our assumptions on relevant functions we know that $s ^ { * } < \infty$ and $\tilde { \theta } ( s ^ { * } ) < \infty$ . Hence the relevant domain to show on which the inequality (27) is  $^ { \prime } \in [ 0 , \tilde { \theta } ( s ^ { * } ) ] , s \in [ 0 , s ^ { * } ]$ . Therefore, (27) is satisfied if we set

$$
a = \max _ {\theta \in [ 0, \tilde {\theta} (s ^ {*}) ], s \in [ 0, s ^ {*} ]} \frac {- \partial E [ m (\theta , s) ] / \partial \theta + \partial I _ {m} (\theta) / \partial \theta}{V (\partial p (\theta , s) / \partial \theta)}.\tag{29}
$$

It is easy to check that $0 < a < \infty$ . This implies that the best response of the client under option 1 is $\theta = 0$ for any action $s \in [ 0 , s ^ { * } ]$ by the support center. Set $F = I ( s ^ { * } ) + v$ . Then we can rewrite the profit functions as follows:

$$
\Pi_ {s} = - c V p _ {0} - I (s) + b \quad \text { Option   1 }\tag{30}
$$

$$
= I (s ^ {*}) + v - I (s) \quad \text { Option   2 }\tag{31}
$$

$$
\Pi_ {m} = m _ {0} - b \quad \mathrm{Option1}\tag{32}
$$

$$
= E [ m (\theta , s) ] - I _ {m} (\theta) - c V p (\theta , s) - I (s ^ {*}) - v
$$

$$
\text { Option   2 }\tag{33}
$$

Now set b such that,

$$
m _ {0} - b + \epsilon = E [ m (\theta^ {*}, s ^ {*}) ] - I _ {m} (\theta^ {*}) - c V p (\theta^ {*}, s ^ {*}) - I (s ^ {*}) - v,\tag{34}
$$

where $\epsilon  0 ^ { + }$ . In this case the client will use option 2 iff the support center’s action $s = s ^ { * }$ . Note that the support center will not choose $s > s ^ { * } ,$ since that would not satisfy the support center’s reservation value. The reason is that here the client’s profit $\Pi _ { m } \geq E [ m ( \theta ^ { \ast } ( s ) , s ) ] - I _ { m } ( \theta ^ { \ast } ( s ) ) -$ $c V p ( \theta ^ { * } ( s ) , s ) - I ( s ^ { * } ) - \bar { v } > E [ m ( \theta ^ { * } , s ^ { * } ) ] - I _ { m } ( \theta ^ { * } ) - c V p ( \theta ^ { * } , s ^ { * } ) -$ $I ( s ^ { * } ) - v ,$ and the support center’s profit is therefore $\Pi _ { s } =$ $\Pi _ { c } - \Pi _ { m } < \Pi _ { c } ^ { * } - \Pi _ { m } < v ,$ where $\Pi _ { c }$ is the joint profit of the two parties. If the support center chooses $s = s ^ { * }$ , then the client will use option 2 and choose $\theta = \theta ^ { * } ;$ ; under this condition, the support center will earn v and the client’s profit is maximized. If the support center instead chooses $s < s ^ { * } ,$ then the client will use option 1 and choose $\theta = 0$ . This option is clearly not incentive compatible for the support center, since $\dot { \Pi _ { s } } = - c \dot { V } p _ { 0 } - I ( s ) + b = - c \dot { V } p _ { 0 } - I ( s ) + { m _ { 0 } } \dot { + } \epsilon -$ $E [ m ( \theta ^ { * } , s ^ { * } ) ] + I _ { m } ( \theta ^ { * } ) + c V p ( \theta ^ { * } , s ^ { * } ) + I ( s ^ { * } ) + v < v .$ The support center will therefore choose $\boldsymbol { s } = \boldsymbol { s } ^ { * } ,$ , inducing the client to use the option 2 contract and choose $\theta = \theta ^ { * }$ . Note that once the support center has exerted an effort $s ^ { * }$ , the client may hold up the support center and not choose the existing cost-plus option and renegotiate it to a lower fixed fee. However, since the exercise date of the options contract follows the investment made by the client, the client cannot credibly hold up the support center. After the client exerts an effort , the support center is guaranteed a profit of $a V ( p _ { 0 } - p ( \theta , s ^ { * } ) ) - I ( s ^ { * } ) - c V p ( \theta , s ^ { * } )$ + b under the gainshare option. Thus the maximum profit that the client can earn by not choosing the cost-plus option and offering the support center a renegotiated contract is $E [ m ( \theta , s ^ { * } ) ] - I _ { m } ( \theta )$ $- \bar { a } \bar { V } ( p _ { 0 } - p ( \theta , s ^ { * } ) ) - \bar { b }$ . We know from Equation (29) that $\begin{array} { r } { E [ m ( \theta , s ^ { * } ) ] - I _ { m } ( \theta ) - a V ( p _ { 0 } - p ( \theta , s ^ { * } ) ) - b \leq \bar { m } _ { 0 } - b . } \end{array}$ . Therefore any renegotiation due to holdup will not be profitable for the client. Hence the options contract described in Proposition 3 is robust to renegotiation.

## References

Agrawal S, Guerreiro R, Pereira CA (2005) How to measure gain-sharing in an outsourcing relationship: A case study in information technology management. Revista Contabilidade and Financas 16(38):1–12.

Aksin Z, Armony M, Mehrotra V (2007) The modern call center: A multi-disciplinary perspective on operations management research. Production Oper. Management 16:665–688.

Aron R, Bandopadyay S, Jayanty S, Pathak PS (2008) Monitoring process quality in offshore outsourcing: A model and findings from multi-country survey. J. Oper. Management 26(2):303–321.

Banker RD, Kalvenes J, Patterson RA (2006) Information technology, contract completeness, and buyer-supplier relationships. Inform. Systems Res. 17(2):180–193.

Bapna R, Barua A, Mani D, Mehra A (2010) Cooperation, coordination and governance in multisourcing: An agenda for analytical and empirical research. Inform. Systems Res. 21(4):785–795.

Bhattacharya S, Gaba V, Hasija S (2013) A comparison of milestonebased and buyout options contracts for coordinating R&D partnerships. INSEAD Working paper, 2013/TOM/OB.

Bhattacharyya S, Lafontaine F (1995) Double-sided moral hazard and the nature of share contracts. RAND J. Econom. 26:761–781.

Bierce & Kenerson, P.C. (2009) Legislation in outsourcing: Gainsharing under the E-Government Act of 2002. White Paper (October 16). Outsourcing Law Bus. J.

Carbonell P, Rodriguez-Escudero AI, Pujari D (2009) Customer involvement in new service development: An examination of antecedents and outcomes. J. Product Innovation Management 26:536–550.

Demski JS, Sappington DEM (1991) Resolving double moral hazard problems with buyout agreements. RAND J. Econom. 22: 232–240.

Dey D, Fan M, Zhang C (2010) Design and analysis of contracts for software outsourcing. Inform. Systems Res. 21(1):93–114.

Edlin A, Hermalin BE (2000) Contract renegotiation and options in agency problems. J. Law, Econom. Organ. 16(2):395–423.

Fitoussi D, Gurbaxani V (2011) IT outsourcing contracts and performance measurement. Inform. Systems Res. 22:1–17.

Gartner (2003) ERP Implementations and gain sharing. White paper, Under Secretary of Defense, Logistics Systems Management, https://acc.dau.mil/adl/en-US/180762/file/ 31714/erp\_impl\_gain\_share\_gartner.ppt.

Gartner (2005) Gartner Says Vendors Must Be Prepared to Renegotiate Outsourcing Contracts. White Paper, http:// www.gartner.com/newsroom/id/492133.

Gomez-Mejia LR, Balkin DB (2007) Managing Human Resources, 5th ed. (Pearson Prentice Hall, Upper Saddle River, NJ).

Goolsby K (2011) The truth about gain-sharing in outsourcing. Outsourcing Success, March 23. http://www.outsourcing-buzz-blog .com/2011/03/the-truth-about-gain-sharing-in-out-sourcing .html.

Gopal A, Sivaramakrishnan K (2008) On vendor preferences for contract types in offshore software projects: The case of fixed price vs. time and materials contracts. Inform. Systems Res. 19(2):202–220.

Gopal A, Sivaramakrishnan K, Krishnan MS, Mukhopadhyay T (2003) Contracts in offshore software development: An empirical analysis. Management Sci. 49(12):1671–1683.

Hasija S, Pinker EJ, Shumsky RA (2008) Call center outsourcing contracts under information asymmetry. Management Sci. 54(4):793–807.

Holmstrom B (1982) Moral hazard in teams. Bell J. Econom. 13: 324–340.

Jain N, Hasija S, Popescu DG (2013) Optimal contracts for outsourcing of repair and restoration services. Oper. Res. Forthcoming.

Jiang B, Talluri S, Yao T, Moon Y (2010) Breaking the winner’s curse in outsourcing. Decision Sci. 41(3):573–594.

Kapadia M (2010) 7 practices to making gain-share contracts work. Outsourcing Observer, White paper.

Kim SK, Wang S (1998) Linear contracts and the double moral hazard. J. Econom. Theory 82(2):342–378.

Koelsch JR (2004) Gain sharing motivates vendors to boost your bottom line. Automation World, http://www.automationworld .com/feature-990.

Lee CH, Geng X, Raghunathan S (2013) Contracting information security in the presence of double moral hazard. Inform. Systems Res. 24(2):295–311.

Martinez-Jerez FA, Narayanan VG, Jurgens M (2007) Strategic outsourcing at Bharti Airtel ltd. Harvard Bus. School Case 9:107-1003.

Mehrotra V, Grossman T (2009) OR process skills transform an out-of-control call center into a strategic asset. Interfaces 39(4): 346–352.

Nambisan S, Baron RA (2009) Virtual customer environments: Testing a model of voluntary participation in co-creation activities. J. Product Innovation Management 26:388–406.

Noldeke G, Schmidt KM (1998) Sequential investments and options to own. RAND J. Econom. 29:633–653.

Roels G, Karmarkar US, Carr S (2010) Contracting for collaborative services. Management Sci. 56(5):849–863.

Susarla A, Barua A (2011) Contracting efficiency and new firm survival in markets enabled by information technology. Inform. Systems Res. 22(2):306–324.

Susarla A, Subramanyam R, Karhade P (2010) Contractual provisions to mitigate holdup evidence from information technology outsourcing. Inform. Systems Res. 21(1):37–55.

Vadlamani S (2009) How IBM is helping Airtel? asiancorrespondent .com, April 12, http://asiancorrespondent.com/516/how-ibm -is-helping-airtel/.

von Hippel E, Katz R (2002) Shifting innovation to users via toolkits. Management Sci. 48(7):821–833.

Wilensky GR, Wolter N, Fischer MM (2007) Gain sharing: A good concept getting a bad name? Health Affairs 26(1):58–67.

Wong AKD (2006) The application of a computerized financial control system for the decision support of target cost contracts. J. Inform. Tech. Construction 11:257–268.
