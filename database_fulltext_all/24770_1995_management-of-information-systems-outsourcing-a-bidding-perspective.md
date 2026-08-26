---
otero_id: 24770
otero_key: "4SSY3R7Z"
title: "Management of Information Systems Outsourcing: A Bidding Perspective"
authors: "A. Chaudhury; Kichan Nam; H. Raghav Rao"
year: "1995"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1995.11518084"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Management of Information Systems Outsourcing: A Bidding Perspective

A. Chaudhury, Kichan Nam & H. Raghav Rao

To cite this article: A. Chaudhury, Kichan Nam & H. Raghav Rao (1995) Management of Information Systems Outsourcing: A Bidding Perspective, Journal of Management Information Systems, 12:2, 131-159, DOI: 10.1080/07421222.1995.11518084

To link to this article: http://dx.doi.org/10.1080/07421222.1995.11518084

![](/api/attachments/4SSY3R7Z/fulltext/images/79aa2c31a1af0f50a6e35d5314a4fe866204594bcac694e46dd3012f7cdba205.jpg)

Published online: 11 Dec 2015.

![](/api/attachments/4SSY3R7Z/fulltext/images/cb0f8ca7bbb9933a0acb48b601a28a50a66e57d6ceef480275896f006920f302.jpg)

Submit your article to this journal ↗

![](/api/attachments/4SSY3R7Z/fulltext/images/7407048d637ca950c071bc04b121c466a9645f5bf39db6a5b2ae1b372d27a425.jpg)

View related articles ↗

![](/api/attachments/4SSY3R7Z/fulltext/images/c2b9610a08e212a9705341a1f6eabacaafd30288fad1e8e04403a73d3a967736.jpg)

Citing articles: 2 View citing articles ↗

# Management of Information Systems Outsourcing: A Bidding Perspective

A. CHAUDHURY, KICHAN NAM, AND H. RAGHAV RAO

A. CHAUDHURY is Assistant Professor of MIS at the University of Massachusetts at Boston. He graduated from the Krannert Graduate School of Management, Purdue University, in 1989. His publications have appeared in varied journals such as IEEE Transactions on Systems, Man and Cybernetics, IEEE Transactions on Data and Knowledge Engineering, Information Systems Research, International Journal of Production Research, and others.

KICHAN NAM is a faculty member in the Department of Information Systems at Queensland University of Technology, Australia. He holds a Ph.D from the State University of New York at Buffalo. Outsourcing is one of his major research topics. Another major research interest is telecommunications. He has published papers in the European Journal of Operational Research, International Conference on Information System (ICIS) Proceedings, and other major international conference proceedings.

H. RAGHAV RAO is an Associate Professor of Management Systems at the State University of New York at Buffalo. He graduated from the Krannert Graduate School of Management, Purdue University, in December 1987. Since then he has published over thirty archival journal articles in journals such as Communications of the ACM, Discrete Applied Mathematics, Decision Support Systems, IEEE Transactions on Systems, Man and Cybernetics, MIS Quarterly, and others. He is currently editor of the special issue of the Annals of Operations Research on the Information Systems and Operations Research interface.

ABSTRACT: Outsourcing is the contracting of various information systems' sub-functions by user firms to outside information systems vendors. A critical factor in the outsourcing process is the bidding and vendor selection mechanism. This paper describes the process of outsourcing and identifies the various stages involved. Subsequently, considering that cost reduction is a driving force of outsourcing for user-firms, this paper proposes a bidding mechanism to reduce expected outsourcing

Acknowledgments: The authors thank Mr. S. Vatsa of M&T Bank, for sharing his extensive outsourcing experience with us. We thank Mr. John Kanicki of the IBM Information Systems Solution Center for his presentation, Professors I. Gill and S. Rajagopalan (for their insightful comments, and Dr. Lawrence Loh for comments on an earlier paper. We also thank Professor L. Schrage of the University of Chicago for insights into LINDO and for taking the time out to run our mixed integer programming code. We would like to express our thanks to the Editor-in-Chief and also our appreciation of the critical comments of the three anonymous referees, particularly anonymous referee 1 and anonymous referee 2, that have greatly increased the lucidity of the paper. This research was supported in part by National Science Foundation under Grant Number IRI-9001424. Authors are listed in alphabetical order.

costs in the final bidding and vendor selection process. The paper studies outsourcing contracts of routine and repetitive activities such as maintenance and operation of telecommunication networks. A realistic scenario is studied, wherein multiple vendors bid for such contracts and where one vendor has cost and expertise advantages over other vendors and as a result tends to inflate bids. A mixed integer programming model is formulated for a multiple vendor scenario. In general, the results suggest a prescription that calls for the use of “carrot and stick” policies by the user firm. Subsidies (the carrot) need to be used as incentives for bidders to announce their most competitive bids. In addition, penalties (the stick) have to be levied in order to pressure bidders not to bid high.

KEY WORDS PHRASES: bidding mechanisms, information systems management, mixed integer programming, outsourcing of information systems.

OUTSOURCING IS THE CONTRACTING OF VARIOUS SYSTEMS SUBFUNCTIONS, such as data entry, programming, facilities management, systems integration, support operations of maintenance, service and disaster recovery, managing of data centers, and telecommunications by user firms to vendors [1]. This trend toward outsourcing has currently become a major information systems phenomenon. A number of major contracts have been reported by Gantz [10] and by Loh and Venkatraman [21]: IBM and MCI running Merrill Lynch's network, McDonnel Douglas and Genix running American Standard's data and network operations, the \$3 billion partnership between Computer Sciences Co. and General Dynamics for the entire information system [41], and recently an \$800 million, ten-year contract between EDS and Blue Cross and Blue Shield of Massachusetts. The most well known outsourcing example is that of Kodak. In 1989, Kodak outsourced operations, support, and ownership of its large systems and computer networks to IBM, and its telecommunications equipment and networks to Digital Equipment Corp [12, 39].

According to the Yankee Group [10], the estimated worldwide market size of outsourcing for U.S. vendors (covering facility management, contract programming, systems integration, and others) was \$29 billion in 1990 and will be \$49.5 billion in 1994, and even if less than 20 percent of the Fortune 500 companies ultimately opt for outsourcing, 100 percent will evaluate it [10]. Of the market for outsourcing, routine and standardized activities constitute a significant portion of activities that are outsourced. In a recent survey, PC maintenance and routine maintenance were “the main targets of respondents who said they would outsource next year” [13, p. 8].

An important factor in outsourcing is the governance of the contractual agreement and the bidding procedures that are involved in the contract. In this paper, we focus on bidding situations that involve routine, standard, and repetitive outsourcing activities—for example, maintenance and management of telecommunications networks—where the vendors have different levels of expertise and cost structures for the job being tendered by a user firm. For the purposes of this paper, the vendor who has the cost and expertise advantages over other competing vendors is termed the incumbent vendor. $^{1}$ This asymmetry in the cost structure arises for various reasons. For instance, a company's equipment may be mostly obtained from the incumbent vendor; the incumbent usually has economies of scale that are not available to other vendors. This is known to the incumbent vendor who usually exploits such asymmetry in expertise by bidding a value that is only marginally lower than what it expects other vendors would bid. This leads to the user firm ending up with higher outsourcing costs.

Our study focuses on the precontract bidding process in an environment that incorporates asymmetric costs, individual rationality, and incentive compatibility. The following questions are investigated: (1) Is it possible for the user firm to reduce or minimize the cost of outsourcing by designing a bidding process that can induce the incumbent to submit its most competitive bid, and (2) if so, what kind of mechanism for submission and evaluation of bids will make that possible?

There are two aspects that drive the vendors: (1) to be selected as a contractor and (2) to make as much profit as possible. To investigate the problem, we formulate a model to minimize the expected cost to the user firm, subject to participation, truth-telling, and integer constraints. Participation constraints indicate that the vendor must realize that he or she has at least as much (and perhaps more) to gain by participating in the bidding process, than by not participating. Truth-telling constraints denote that for each vendor, the expected profits resulting from not inflating bids must be at least as much as (and perhaps greater than) the expected profit from inflating bids. The integer constraints signal that only a single vendor can be chosen as a contractor. In line with some of the current research in information systems $[3]$ , in this exercise we focus on optimization over a single period bidding situation.

The contributions of this paper are twofold. First this paper is among the earliest attempts to employ the tools of economic theory, specifically mechanism design (based on Kreps [18, pp. 661–715], $^{2}$ and extending a preliminary model suggested in [28, 29]), (a) to formulate a model for the management of precontractual bidding aspects of the information systems outsourcing process, and (b) to actualize the potential of this formulation by utilizing tools of management science, specifically mixed integer programming, to generate prescriptions for the problem of cost-effective outsourcing. This approach allows us to propose a bidding mechanism for minimizing outsourcing costs. Second, while the approach is mathematical and is based on sound theoretical arguments, the conclusions have natural and realistic interpretations that can allow the manager to adopt the resulting qualitative guidelines. In general, the results of the model suggest a prescription that calls for the use of a “carrot and stick” policy to be followed by the user firm. The carrot corresponds to subsidies that need to be used as incentives for vendors to bid low. The stick corresponds to instituting penalties in order to pressure the incumbent vendor not to bid high. Most managers involved in contract negotiation would immediately recognize these prescriptions. These include preferential treatment for challengers to the value of bids submitted, which parallel bidding arrangements that are observed in the real world.

The paper is organized as follows. The next section presents related research along with an overview of the outsourcing vendor selection process. We describe the process of outsourcing and identify the stage where the mixed integer modeling can be introduced by the user firm. In the third section, we introduce the fundamental concepts of mechanism design. We then employ mixed integer programming to model a three-vendor/single user firm outsourcing problem. Examples show the application of the model. The results then are discussed, with findings and implications of the model. We describe scenarios where the solutions of the model are easily implementable and scenarios where they are not. The final section summarizes and concludes the paper. (Throughout this paper, we refer to the user firm in the neuter gender, the incumbent firm is feminine, and the competing firms are masculine. We also use the terms bidder and vendor interchangeably.)

## Related Research and Outsourcing Process

## Related Research

THE USE OF ECONOMIC TOOLS IN THE AREA OF SYSTEMS MANAGEMENT has been proposed recently by Bakos and Kemerer [2] and by Gurbaxani and Kemerer [11], who suggest and argue for the use of agency theory and transaction cost economics in the study of information systems. Another recent study, by Pick and Whinston [31], investigates effective techniques for allocation of computer resources based on economic tools. Based on the economic literature of incentive structures, they use the Clarke-Groves charging mechanism to develop an approach for the internal computer pricing problem.

In the specific area of outsourcing, although many discussions have appeared in trade literature in the past few years, research is limited. Some exceptions that we know of are the recent published work on outsourcing $[5, 19, 21, 22, 33, 34]$ . Lacity and Hirschheim $[19]$ study outsourcing phenomena using case studies of thirteen companies. Richmond and Seidmann $[33]$ compare a stage-by-stage software outsourcing contract with a two-stage software outsourcing contract and suggest that the two-stage method is a beneficial way of contracting. Richmond et al. $[34]$ employ an incomplete contracting framework to characterize two agents, the user and the developer; they formulate a quantitative model to obtain closed form solutions for investigating the decision whether to outsource or use internal development. However, since the “closed-form analytic solutions . . . provided no insights,” they use a series of numerical simulations to derive insights by examining the effects of different parameter values $[34, p. 467]$ .

Loh and Venkatraman [21] investigated the impact of the IBM–Kodak outsourcing contract on the IS industry; they also empirically develop and test determinants of information technology outsourcing [22]. They point out that companies can search out experienced low-cost providers through the bid process and subsequent contract negotiations. As part of future research, Loh and Venkatraman [22] suggest the investigation of the economic and informational aspects of the outsourcing phenomenon through the use of economic tools.

Few previous studies have focused on the bidding process of outsourcing contracts, even though it is one of the important aspects of outsourcing. In accordance with Loh and Venkatraman's suggestion, this paper studies the precontract bidding stage of outsourcing of routine IS activities where the bid is usually the driving element of competition in the contracting process. In this paper we extend earlier research [5] that studied the outsourcing bidding situation under certain restrictive assumptions. Here we consider the case of multiple agents (specifically one user firm and three vendors) and scenarios with different types of cost asymmetry.

## The Process of Outsourcing

Since outsourcing is a relatively new phenomenon in the IS industry, it is worthwhile not only to discuss the effective outsourcing vendor selection process but also to specify the point in the process where this study focuses. This vendor selection process is shown in figure 1.

First, the user firm has to decide if it will outsource or not. In order to do so, the user firm has to carry out a technical assessment of the existing operations, review management tools, databases, and problem resolution processes $[15]$ . If existing information technology capabilities are limited, and economies of scale may accrue, then outsourcing makes sense $[7]$ .

Second, if it decides to outsource, the optimal degree of outsourcing must be decided. That is, will outsourcing include all information services such as software development, systems integration, and network management, or will selective and segmented outsourcing be carried out by including just a few of the services?

Third, the user firm prepares a list of possible vendors. It usually considers several vendors as candidates for outsourcing, a key candidate usually being the incumbent vendor.

The vendors should be able to handle every aspect of the operations at a reasonable cost. However, if some vendor has significant knowledge and accumulated knowhow about systems in the user firm, this bidder (incumbent vendor) will have a strong advantage over other bidders. This is because the incumbent can make use of her specialized experience and scale size to offer lower bids while delivering superior services. It has often been observed that vendors with proven track records, and with whom the user firm has worked previously, are at an advantage when it comes to vendor selection $[14]$ . For example, IBM is well known as a formidable force in outsourcing bids, especially in the securities industry, largely because its equipment is so pervasive $[35]$ .

Fourth, the user firm analyzes the major dimensions in order to evaluate vendors, compares the different philosophies of the vendors, and creates a further short list of prospective vendors [17]. At issue here are both technical competence in terms of quality and service and “soft” criteria such as whether the vendors in question have a feel for the user firm’s business and are known to exhibit appropriate consulting and people skills [7]. The process of deciding on the final short list would be iterative, involving repeated refinement of the short lists.

Fifth, in the final round, after preparing and issuing documents known as Requests for Proposals (RFP), the user firm receives bids. Here it is necessary for the user firm to have an understanding of the vendor's pricing and how it compares with internal costs [7]. With an existing IS department within the organization, changing control through outsourcing requires an in-depth analysis of business objectives, technological requirements, strengths, and weaknesses. From the user firm point of view, the precontract bidding stage is very important. The RFP must be carefully thought out: it can be a formal document requiring detailed and comprehensive answers or a short wish list describing the functionalities that are needed. It is at this stage, that the user firm can benefit from the competition among the vendors to obtain an advantageous contractual deal. According to Johnston-Turner [16], at the same time it is important not to be too tough in negotiations, since vendors who are squeezed out of reasonable profits are trapped, $^{3}$ and thereafter inflate costs or degrade the quality of service in the subsequent periods to compensate for losses after the contract is signed.

![](/api/attachments/4SSY3R7Z/fulltext/images/45153e395834c969c0738abaa904bff20a83ad9db74b272f5180445d9ee6f226.jpg)  
Figure 1. Processing of Outsourcing

Johnston-Turner [16] recommends that the number of competing vendors be kept to no more than five for the final round. A case in point is National Car Rental Co., which decided on an outsourcing agreement of \$500 million after an eighteen-month bidding process. The maximum number of vendors at any time was thirteen and after four months there were only two in the final round, IBM and EDS [6]. Another example is Navistar International Transportation Corp., which evaluated bids from IBM, EDS, and the in-house operations department for a billion-dollar outsourcing contract [41].

Sixth, from the final short list, one contractor is selected and the user firm develops policies and contracts to manage subsequent organizational and temporal issues.

The model developed in later sections concentrates on the bid as the only factor of interest, and focuses on the final round scenario. To keep the model realistic and tractable, we investigate a situation where there is a user firm and three vendors (with one incumbent vendor and two competitors). The categories of outsourcing where the model developed here can be most readily used include the outsourcing of routine and standardized activities such as PC maintenance and running of telecommunications services $[13]$ . In such contracts involving routine tasks, quality is usually measurable and can be enforced through penalty provisions in the contract. During the tendering stage, once a short list of qualified providers is chosen and invited to submit bids, the bid is usually the driving element of competition. We investigate different scenarios involving how the underlying cost structures of the vendors relate to each other. For each of these scenarios we discuss the prescriptions that emerge.

## An Introduction to Incentive Schemes

AN APPROACH TO THE DESIGN OF BIDDING MECHANISMS is to use incentive theory. According to incentive theory [20, 40], instead of letting the vendors inflate their bids, the user firm can achieve low costs by giving some rewards as incentives for submitting competitive low bids. Examples of the use of incentive mechanisms are mechanisms for allotting airport time slots [32] and an incentive mechanism used by Citibank for auctioning commercial paper [38]. The fundamental concept behind incentive theory is that if an incentive mechanism to induce the vendors to submit their most competitive low bids can be formulated, for situations where the vendor's private information and actions are difficult to monitor, it will be of benefit to the user firm.

## An Example with Two Bidders

To illustrate the concepts of mechanism design, we first describe a simple two-vendor problem. Later we will extend the concepts illustrated here to a three-vendor scenario.

Suppose a user firm has to deal with two vendors: the incumbent vendor A and her rival B. While one can generally say which vendor has a cost advantage, one cannot be perfectly sure of it. This lack of perfect information is modeled by having different discrete probabilities (to illustrate the information asymmetry) associated with the cost structure of the two vendors. We assume that the incumbent vendor, A, has a cost advantage. (Here the term cost includes the cost of the contract as well as the opportunity cost or profit [margin] available in the market for such services.)

Let us have two possible bids of \$90 or \$110. Now each vendor can bid at a value of either \$90 or \$110 with probabilities of two-thirds and one-third, respectively, for vendor A, and one-third and two-thirds, respectively, for B. Neither the user firm nor the other vendor knows the true cost of the rival. We also assume that when the user firm proposes a contract, each firm responds on a “take-it-or-leave-it” basis.

If the user firm knows the true costs of the two vendors, it will choose a vendor who bids lower. Therefore, in only two-ninths of cases will it face a situation where both bids have a high value. In such a case it will pay \$110. In the other seven-ninths of the cases it will pay \$90 to whoever bids the low value \$90 (see Table 1). This results in an optimal expected cost of \$94.44 (2/9 × 110 + 7/9 × 90 = 94.44) to the user firm.

It is unlikely, however, that the user firm and the rivals will know the true cost. In this situation of information asymmetry (i.e., only the vendor knows its true cost but not the user firm or the rival), what prediction can be made? If vendors are restricted to bid \$90 or \$110, they will bid \$110 regardless of their cost. This can be shown as follows.

Let us consider two situations as faced by A. Her cost is either \$90 or \$110: (1) If her cost is \$110, she will always bid \$110, since she will lose by bidding \$90. (2) If her cost is \$90, by bidding \$90 she will not gain over or above what she can in the market at large (because cost includes the opportunity margin or markup). By bidding \$110, however, there is also a two-thirds chance that B will bid \$110 and so A will have an equal chance of getting the contract. Therefore, her expected gain by bidding \$110 is $(2/3) \times (1/2) \times 20 = 6.67$ over and above what she can make by bidding \$90.

Therefore, for A, bidding \$110 is the best possible strategy. A similar analysis will reveal that bidding \$110 is also the best possible strategy for B. Hence, both will bid \$110 and the user firm will be faced with the high contract value of \$110.

## Incentive Design

We now propose a mechanism design that can be used to discourage the incumbent vendor from bidding high, or alternately encourage her to bid low. This would then result in the user firm having significantly lower costs. The scheme that follows refers to Table 1. Suppose that $X (\geq \$90)$ will be paid by the user firm if both vendors submit bids of \$90. Suppose $Y (\geq \$90)$ will be paid if one (say vendor A) calls \$90 and the other (say vendor B) calls \$110, but the order goes to the vendor who announces a bid of \$90. If both vendors announce \$110, the bid is given to one of them with equal probability of being chosen, and the user firm pays \$110. If A's costs are \$90, and B's costs are \$110, A can announce \$110, and have profits of \$13.33 with a probability of 1/2. (Note: $(2/3) \times (110 - 90) = \$13.33$ since vendor B calls \$110 with a probability of 2/3.) Otherwise, she can announce \$90. If B's costs are \$90 also, A will get a profit of $(1/3) \times (X - 90)$ with a probability of 1/2, and if B's costs are \$110, she gets a profit of $(2/3) \times (Y - 90)$ .

Table 1

<table><tr><td>Bid(A, B)</td><td>Probability(A, B)</td><td>Joint prob.</td></tr><tr><td>(90, 90)</td><td>(2/3, 1/3)</td><td>2/9</td></tr><tr><td>(90, 110)</td><td>(2/3, 2/3)</td><td>4/9</td></tr><tr><td>(110, 90)</td><td>(1/3, 1/3)</td><td>1/9</td></tr><tr><td>(110, 110)</td><td>(1/3, 2/3)</td><td>2/9</td></tr></table>

The above discussion leads to the following two truth-revealing conditions: vendor A will bid a value of \$90 only if she can have profits of:

[Constraint a]

$$
(1 / 2) \times (1 / 3) \times (X - 9 0) + (2 / 3) \times (Y - 9 0) \geq (1 / 2) \times 1 3. 3 3.
$$

Likewise, vendor B will bid \$90 (assuming that expected profits are maximized) if

[Constraint b]

$$
(1 / 2) \times (2 / 3) \times (X - 9 0) + (1 / 3) \times (Y - 9 0) \geq (1 / 2) \times 6. 6 7.
$$

However, the user firm will try to minimize the expected cost of

[Objective function]

$$
(2 / 9) \times X + (5 / 9) \times Y + (2 / 9) \times 1 1 0,
$$

That is, with probability 2/9 it pays $X$ ; with probability 5/9 it pays $Y$ , and with probability 2/9 it pays \$110 (see Table 1). Any solution of $X$ and $Y$ that satisfies the user firm's objective function in conjunction with the bidders' two truth-revealing conditions will give the minimum expected cost of \$100. By solving the above objective function with constraints a and b, the optimal expected cost of the user firm that successfully induces the vendors to bid low is \$100 with $X$ = \$90 and $Y$ = \$100.

If the user firm has some prior information, it will naturally try to reduce the expected cost from \$100, to the expected cost of \$94.44 (when the user firm knows the vendor's costs as shown in the preceding section). Or if it does not have any information, it will try to give some incentives to the bidders to bid low even if the minimum expected cost of the user firm should be a little above \$100. On the other hand, the vendors, possibly by bidding high, will find ways to increase the expected cost above \$100 to make more profits while at the same time winning the contract. It is important to note the following with regard to above analysis:

1. It is assumed that bidders are rational—that is, that they have rational expectations about the outcome of their behavior. For example, low cost bidders do not bid high once they realize that they will not be awarded the contract if they bid high.

2. There may be more than one solution that results in the same optimal value, in which case making a reasonable prediction of behavior would become more complex. However, the mixed integer program model that is used to solve the problem in this paper is an easily implementable technique for finding an optimal solution.

3. Irrespective of what the true costs of vendors are, they will try to maximize their payoff. Thus, there are obvious benefits in inflating one's bids in some situations.

The above analysis shows that implementation of the incentive design mechanism will imply a lower cost to the user firm than not implementing the mechanism. This line of reasoning is pursued in the next section, and is extended to a situation with three vendors and varying scenarios.

## A Model of the Outsourcing Problem

## Mechanism Design

A NUMBER OF ASSUMPTIONS ARE USED IN THE MODEL THAT WE DEVELOP BELOW. Each of these assumptions follows from the literature in bidding and in mechanism design [23, 29]. $^{4}$

First, vendors are not allowed to collude or to communicate to exchange information among themselves before the contract is signed. Second, all bidders behave rationally on the basis of the information available. Third, the bid is the basis for the final choice of one contractor. Fourth, each bidder will not bid below a value that includes the opportunity cost of using resources for other contracts. Therefore, though the incumbent will bid lower than her competitors, she will not bid at values below what she can otherwise make in the market at large.

Each vendor has different cost structures because of asymmetries due to differences in information, location, experience, and economies of scale. Each bidder's true cost is private information. However, we assume that each bidder's different cost structure is independent of every other bidder, and can be estimated by each party. In the absence of a mechanism design as is explained here, the nonsymmetric cost structure among bidders allows the incumbent bidder to earn more by bidding higher, thereby causing the user firm to spend more money. The incumbent bidder has no incentive to bid low and finds it advantageous to bid higher than what she would have done if her competitor's cost structures were similar to her's.

When several bidders participate in the bidding process, they can be classified into two categories: the incumbent vendor (which we call vendor A), which has an inherent advantage over other bidders; and the rival or challenging vendors (which we call vendor B and vendor C). Vendors B and C have a greater possibility of having higher costs than vendor A.

![](/api/attachments/4SSY3R7Z/fulltext/images/6ea9bb519e1e328c49af9ccd0e17e2cb4e8a1850c087ddeeb478f87a44519ee0.jpg)

![](/api/attachments/4SSY3R7Z/fulltext/images/91e24a07f6639023d4ffdbe2424016060d7231879fdac5deffd74344fb8b3f48.jpg)

Firm C
(Second Challenger)  
![](/api/attachments/4SSY3R7Z/fulltext/images/e70888cb68d499793d91bdd1bbd4554b8fa4633d14ddcca8c96bb58485b5494d.jpg)  
Figure 2A. Skewness of Continuous Probability Distributions

In a bidding situation, the kind of information that a user firm or the bidders have about each other's cost structure and the probable bids is marked by uncertainty. This uncertainty is represented in the model by probability distributions. Since the incumbent vendor has cost advantages over other bidders, the incumbent vendor is assumed to have a cost probability distribution that is skewed toward low values (positive skewness). The cost structure for the rival bidders can be represented by cost distribution curves that are skewed toward higher values (either zero skewness or negative skewness). (We later show that the model's conclusions are quite robust with regard to the actual distributions used.) In order to simplify the problem, we approximate the continuous probability distributions by discrete probability distributions with discrete cost structures, as shown in figures 2A and 2B.

![](/api/attachments/4SSY3R7Z/fulltext/images/03a3c5431a2b86b195456d5635e5543f7b111d7c4990a9427e48a3d961344558.jpg)

![](/api/attachments/4SSY3R7Z/fulltext/images/51e801d939ce8edbba570d76bfb5e95e80fdd5b3fb05b0d7b0c35f28f0e557c7.jpg)

Firm C
(Second Challenger)  
![](/api/attachments/4SSY3R7Z/fulltext/images/bb29f3260b84cba4a19241d7ad3c9619cb60f606689ec0da004c91ae318cbd16.jpg)  
Figure 2B. Skewness of Discrete Probability Distributions

The outsourcing model is based on two fundamental rationales: the vendors wish to be selected as outsourcing contractors, and they wish to make as much profit as possible. In developing the model, we closely follow Kreps [18, pp. 661–715]. $^{5}$

The objective function is formulated to represent minimization of the expected cost to the user firm, subject to participation, truth-telling, and integer constraints. Participation constraints indicate that each bidder participates only if a nonnegative profit is given by the user firm. Truth-telling constraints denote that for each bidder the expected profit resulting from not inflating its bid must be at least as much as (perhaps greater than) the expected profit from inflating its bid. The integer constraints signal that only a single vendor can be chosen as a contractor. This then results in a mixed integer model. The discrete probability distributions of the possible bids are input to the model. As explained in figure 2A, the major difference between the incumbent and other challengers in our problem-solving method is that the incumbent vendor has a probability distribution skewed toward low costs while other challengers are more skewed toward high costs. The model returns the optimal expected value of the objective function. In addition, the output shows (1) the vendor to whom the contract should be awarded, and (2) the value of the contract for the user firm, given the bids by the incumbent and the two challenger vendors. Details of the input and output parameters are presented in the next subsection.

## The Mixed Integer Outsourcing Model with Multiple Vendors

The treatment below is general to the multiagent scenario. In this paper, we focus on three vendors. Let k be vendor A's bid announcement parameter, i be vendor B's bid parameter, and j be vendor C's bid parameter. Then the decision variables of the model are:

1. $R_{kij}^{f}$ : payment to be made by the user firm to vendor $f$ ; and

2. $X_{kij}^{f}$ : an integer that has the value of 1 if any vendor f is awarded the outsourcing contract, otherwise 0.

The parameters of the model are:

(i) $f$ , where $f = 1$ for the incumbent bidder, vendor A, $f = 2$ for the first rival bidder, vendor B, and $f = 3$ for the second rival bidder, vendor C;

(ii) $C^k$ constitutes the possible values of vendor A's true cost in dollars ( $k = 1, \ldots, l$ ), $C^i$ are possible values of vendor B's true cost in dollars ( $i = 1, \ldots, n$ ), $C^j$ are the possible values of vendor C's true cost in dollars ( $j = 1, \ldots, m$ ); The distribution of all these values is common knowledge.

(iii) $v_{kij}$ is the joint probability of $C^k, C^i$ , and $C^j$ .

(iv) $w_{k}$ is the common knowledge probability that vendor A's cost is $C^{k}$ , $w_{i}$ is the probability that vendor B's cost is $C^{i}$ , $w_{j}$ is the probability that vendor C's cost is $C^{j}$ .

(v) $w_{ki}$ is the joint probability of $C^k$ and $C^i$ , $w_{kj}$ is the joint probability of $C^k$ and $C^j$ , and $w_{ij}$ is the joint probability of $C^i$ and $C^j$ .

(vi) U and L are the upper and lower bounds of all the bids respectively.

Then we have the following system of equations:

$$
\text { Minimize } \sum_ {k = 1} ^ {l} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} v _ {k i j} \left[ R _ {k i j} ^ {1} + R _ {k i j} ^ {2} + R _ {k i j} ^ {3} \right].
$$

subject to the following constraints:

(1)

$$
\sum_ {i} ^ {n} \sum_ {j} ^ {m} w _ {i j} \left[ R _ {k i j} ^ {1} - C _ {k} X _ {k i j} ^ {1} \right] \geq 0 \quad (k = 1, \dots , 1)\tag{2}
$$

$$
\sum_ {k} ^ {i} \sum_ {j} ^ {m} w _ {k j} \left[ R _ {k i j} ^ {2} - C _ {t} X _ {k i j} ^ {2} \right] \geq 0 \quad (i = 1, \dots , n)\tag{3}
$$

$$
\sum_ {k} ^ {l} \sum_ {i} ^ {n} w _ {k i} \left[ R _ {k i j} ^ {3} - C _ {j} X _ {k i j} ^ {3} \right] \geq 0 \quad (j = 1, \dots , m)
$$

Constraints (1), (2), and (3) are the participation constraints for vendor A, vendor B, and vendor C. These induce firms to participate only if they can make a nonnegative expected profit.

$$
\sum_ {i} ^ {n} \sum_ {j} ^ {m} w _ {i j} \left[ R _ {k i j} ^ {1} - C _ {k} X _ {k i j} ^ {1} \right] \geq \sum_ {i} ^ {n} \sum_ {j} ^ {m} w _ {u j} \left[ R _ {k ^ {\prime} i j} ^ {1} - C _ {k} X _ {k ^ {\prime} i j} ^ {1} \right] \begin{array}{l} (k = 1, \dots , 1) \\ (k ^ {\prime} = 1, \dots , k - 1, k +, \dots , 1) \end{array}
$$

$$
\sum_ {k} \sum_ {j} ^ {m} w _ {k j} \left[ R _ {k i j} ^ {2} - C _ {i} X _ {k i j} ^ {2} \right] \geq \sum_ {k} ^ {l} \sum_ {j} ^ {m} w _ {k j} \left[ R _ {k i ^ {\prime} j} ^ {2} - C _ {i} X _ {k i ^ {\prime} j} ^ {2} \right] \begin{array}{l} (i = 1, \dots , n) \\ (i ^ {\prime} = 1, \dots , i - 1, i + 1, \dots , n) \end{array} \tag {5}
$$

$$
\sum_ {k} \sum_ {i} ^ {n} w _ {k i} \left[ R _ {k i j} ^ {3} - C _ {f} X _ {k i j} ^ {3} \right] \geq \sum_ {k} ^ {i} \sum_ {i} ^ {n} w _ {k i} \left[ R _ {k i j ^ {\prime}} ^ {3} - C _ {f} X _ {k i j ^ {\prime}} ^ {3} \right] \begin{array}{l} (j = 1, \dots , n) \\ (j ^ {\prime} = 1, \dots , j - 1, j + 1, \dots , m) \end{array}
$$

Constraints (4), (5), and (6) are the truth-telling constraints, indicating that each bidder will prefer to tell the truth only if this leads to a nonnegative profit.

$$
X _ {k i j} ^ {1} + X _ {k i j} ^ {2} + X _ {k i j} ^ {3} = 1 \quad \begin{array}{l l} & (k = 1, \dots , 1) \\ & (i = 1, \dots , n) \\ & (j = 1, \dots , m) \end{array}\tag{7}
$$

Equation (7) is the integer constraint implying that only one bidder will be successful and can be chosen as the outsourcing vendor.

$$
L   X _ {k i j} ^ {f} \leq R _ {k i j} ^ {f} \leq U X _ {k i j} ^ {f} \quad \begin{array}{l l} & (k = 1, \ldots , 1) \\ & i = 1, \ldots , n) \\ & (j = 1, \ldots , m) \\ & (f = 1, 2, 3) \end{array}\tag{8}
$$

Equation (8) depicts the lower and upper bound constraints. The lower bound L is equal to the lowest value for each vendor's $C^{k}$ , $C^{i}$ , and $C^{j}$ . It is provided in order to guarantee the coverage of cost for each bidding price of the vendor. The upper bound is equal to $\text{Max}(C^{k})$ for vendor A, $\text{Max}(C^{i})$ for vendor B, and $\text{Max}(C^{j})$ for vendor C, and represents the fact that the user firm does not want to pay out more than the highest cost to be announced regardless of the truth.

As shown, the model is a mixed integer problem. The decision variable $X_{kij}^{f}$ takes on a 0 or 1 integer value and $R_{kij}^{f}$ takes on positive real numbers only when $X_{kij}^{f}$ takes on a value of 1. This restriction reflects a situation in which only one bidder is chosen and makes a profit.

## An Illustrative Scenario

To test different cases of asymmetric information structure, we include nine representative examples (see Table 2). To solve the mixed integer programs, we use the well-known LINDO software which has built-in functions for handling integer problems.

It is important to point out here that there are multiple possible outcomes to the problem. In fact the number of possible outcomes is huge. This is a problem that is well known in game theory literature $[18, 19]$ and has recently been documented in the popular literature as well. In an article on the 1994 Economics Nobel Prize winners $[23]$ , Michael J. Mandel writes, “the phenomenon of many stable outcomes—or “multiple equilibria”—has proven disturbing and embarrassing to economists hoping to use game theory to make predictions. Certainly it has been worrisome to Harsanyi and Selten, who have devoted the second half of their careers to unsuccessfully trying to eliminate multiple equilibria.” Also, LINDO has the limitation that if the LP relaxation is naturally integer, then the commercial LINDO package will do no branching, even though there may be alternate integer optimal solutions $[36]$ . If an analysis of alternate optimal solutions is desired, new subroutines have to be written for more branching. This, however, does not lessen the value of the formulation or the solution process, because our objective here is to find a solution that has a natural interpretation, to see how this interpretation can help the user firm find a better method of handling bidding among different vendor firms, and to point out how the user firm may implement this method.

We assume that the three vendors' announcements are \$50, \$100, or \$150. Since an incumbent vendor (vendor A) is assumed to have a lower cost structure and a challenger (vendors B and C) to have a higher cost structure, we assign a higher probability of lower cost to vendor A and a higher probability of the higher costs for vendors B and C. The results are summarized in Table 2.

For explanation purposes, we focus on row 5 in Table 2. In row 5, for each of the bids, \$50, \$100, and \$150, vendor A is assumed to have an associated probability distribution of 2/3, 1/6, and 1/6, respectively; vendor B has a probability distribution of 1/6, 2/3, and 1/6; and vendor C has a probability distribution of 1/6, 1/6, and 2/3. If vendor A bids \$50, B bids \$50, and C bids \$50, vendor A is selected at a value of \$50. If vendor A bids \$50, B bids \$50, and C bids \$100, vendor A is selected at a value of \$50. All other values are interpreted in the same manner. If we assume that the user firm does not follow the proposed mechanism design, the best strategy for any vendor is to inflate the bid to exploit the cost differential that is in the vendor's favor. It can be shown that the expected cost to the user firm in such a (no-revelation-

Table 2 Bid Awards Using the Mixed Integer Model for Three Vendors

<table><tr><td rowspan="4"></td><td colspan="3">Bid values and associated probability structure</td><td rowspan="4">Optimal expected cost</td><td rowspan="4">Bids by</td><td colspan="16"></td></tr><tr><td rowspan="3" colspan="3">(50, 100, 150)</td><td>A:</td><td>50</td><td>50</td><td>50</td><td>50</td><td>50</td><td>50</td><td>50</td><td>50</td><td>50</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td>B:</td><td>50</td><td>50</td><td>50</td><td>100</td><td>100</td><td>100</td><td>150</td><td>150</td><td>150</td><td>50</td><td>50</td><td>50</td><td>100</td><td>100</td><td>100</td></tr><tr><td>C:</td><td>50</td><td>100</td><td>150</td><td>50</td><td>100</td><td>150</td><td>50</td><td>100</td><td>150</td><td>50</td><td>100</td><td>150</td><td>50</td><td>100</td><td>150</td></tr><tr><td rowspan="3">1</td><td colspan="3">A: (1/2, 1/4, 1/4)</td><td>0.2325</td><td>75.00</td><td>A:</td><td>—</td><td>—</td><td> $150^{***}$ </td><td>50</td><td>50</td><td>50</td><td>—</td><td>50</td><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td colspan="3">B: (1/4, 1/2, 1/4)</td><td></td><td></td><td>B:</td><td>—</td><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>50</td><td> $150^{***}$ </td><td>—</td><td>100</td><td>100</td></tr><tr><td colspan="3">C: (1/4, 1/2, 1/4)</td><td></td><td></td><td>C:</td><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td></tr><tr><td rowspan="3">2</td><td colspan="3">A: (1/2, 1/4, 1/4)</td><td>0.4028</td><td>76.56</td><td>A:</td><td>—</td><td>50</td><td>—</td><td>—</td><td>50</td><td>50</td><td>—</td><td> $150^{***}$ </td><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td colspan="3">B: (1/2, 1/4, 1/2)</td><td></td><td></td><td>B:</td><td>—</td><td>—</td><td> $75^*$ </td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td> $150^{***}$ </td><td>50</td><td>—</td><td>100</td><td>100</td></tr><tr><td colspan="3">C: (1/4, 1/4, 1/2)</td><td></td><td></td><td>C:</td><td>50</td><td>—</td><td>—</td><td> $87.5^*$ </td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td></tr><tr><td rowspan="3">3</td><td colspan="3">A: (1/2, 1/4, 1/4)</td><td>0.4651</td><td>84.375</td><td>A:</td><td>—</td><td>50</td><td>—</td><td>—</td><td>50</td><td>50</td><td>—</td><td> $150^{***}$ </td><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td colspan="3">B: (1/4, 1/4, 1/2)</td><td></td><td></td><td>B:</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td> $150^{***}$ </td><td> $150^{***}$ </td><td> $75^{**}$ </td><td>—</td><td>—</td><td>100</td></tr><tr><td colspan="3">C: (1/4, 1/4, 1/2)</td><td></td><td></td><td>C:</td><td>50</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td> $137.5^{***}$ </td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>50</td><td>100</td><td>—</td></tr><tr><td rowspan="3">4</td><td colspan="3">A: (2/3, 1/6, 1/6)</td><td>0.529</td><td>66.67</td><td>A:</td><td>50</td><td>—</td><td>50</td><td>—</td><td>50</td><td>50</td><td>50</td><td>50</td><td> $100^{**}$ </td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td colspan="3">B: (1/6, 2/3, 1/6)</td><td></td><td></td><td>B:</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>50</td><td>50</td><td>50</td><td>—</td><td>100</td><td>100</td></tr><tr><td colspan="3">C: (1/6, 2/3, 1/6)</td><td></td><td></td><td>C:</td><td>—</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td></tr><tr><td rowspan="3">5</td><td colspan="3">A: (2/3, 1/6, 1/6)</td><td>0.9163</td><td>67.13</td><td>A:</td><td>50</td><td>50</td><td>—</td><td>—</td><td>50</td><td>50</td><td>50</td><td>50</td><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td colspan="3">B: (1/6, 2/3, 1/6)</td><td></td><td></td><td>B:</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>50</td><td>50</td><td>—</td><td>100</td><td>100</td></tr><tr><td colspan="3">C: (1/6, 1/6, 2/3)</td><td></td><td></td><td>C:</td><td>—</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td> $150^{***}$ </td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td></tr><tr><td rowspan="3">6</td><td colspan="3">A: (2/3, 1/6, 1/6)</td><td>1.058</td><td>76.85</td><td>A:</td><td>—</td><td>50</td><td>—</td><td>50</td><td>50</td><td>50</td><td>—</td><td>50</td><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td colspan="3">B: (1/6, 1/6, 2/3)</td><td></td><td></td><td>B:</td><td>—</td><td>—</td><td> $93.75^*$ </td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>50</td><td>50</td><td>—</td><td> $150^{**}$ </td><td> $125^*$ </td></tr><tr><td colspan="3">C: (1/6, 1/6, 2/3)</td><td></td><td></td><td>C:</td><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td> $68.75^*$ </td><td>—</td><td>—</td><td> $150^{***}$ </td><td>—</td><td>—</td><td> $150^{***}$ </td><td>—</td><td>—</td></tr></table>

<table><tr><td>7</td><td>A: (4/5, 1/10, 1/10)B: (1/10, 4/5, 1/10)C: (1/10, 1/10, 4/5)</td><td>0.905</td><td>60.00</td><td>A:B:C:</td><td>—50—</td><td>—60*—</td><td>50—51.56*</td><td>—</td><td>50—</td><td>50—</td><td>50—</td><td>50—</td><td>62.50*</td><td>50—</td><td>—60</td><td>—60</td><td>—150***</td><td>—</td><td>—100</td><td>—100</td></tr><tr><td>8</td><td>A: (4/5, 1/10, 1/10)B: (1/10, 4/5, 1/10)C: (1/10, 1/10, 4/5)</td><td>1.567</td><td>60.10</td><td>A:B:C:</td><td>50—</td><td>50—</td><td>—65*—</td><td>—</td><td>50—</td><td>50—</td><td>50—</td><td>50—</td><td>50—</td><td>50—</td><td>—</td><td>—50</td><td>—50</td><td>—</td><td>—100</td><td>—100</td></tr><tr><td>9</td><td>A: (4/5, 1/10, 1/10)B: (1/10, 1/10, 4/5)C: (1/10, 1/10, 4/5)</td><td>1.810</td><td>67.80</td><td>A:B:C:</td><td>50—</td><td>50—</td><td>—70.31*—</td><td>50—</td><td>50—</td><td>50—</td><td>—68.75*—</td><td>50—</td><td>50—</td><td>50—</td><td>—</td><td>—50</td><td>—50</td><td>—</td><td>—100</td><td>—100</td></tr><tr><td rowspan="2" colspan="2"></td><td rowspan="2" colspan="2">Bid values and associated probability structure</td><td colspan="17">Bids by</td></tr><tr><td>Optimal ex-pected cost</td><td>A:B:C:</td><td>10015050</td><td>100150100</td><td>100150150</td><td>1505050</td><td>1505010</td><td>15050150</td><td>15010050</td><td>150100100</td><td>150100150</td><td>150100150</td><td>15010050</td><td>150150100</td><td>150150100</td><td>150150150</td><td>150150150</td></tr><tr><td>1</td><td>A: (1/2, 1/4, 1/4)B: (1/4, 1/2, 1/4)C: (1/4, 1/2, 1/4)</td><td>0.2325</td><td>75.00</td><td>A:B:C:</td><td>—50</td><td>—</td><td>—150**</td><td>—</td><td>—50</td><td>—150***</td><td>—50</td><td>—</td><td>—50</td><td>—</td><td>—100</td><td>—100</td><td>—150***</td><td>—100</td><td>—</td><td>—</td></tr><tr><td>2</td><td>A: (1/2, 1/4, 1/4)B: (1/2, 1/4, 1/2)C: (1/4, 1/4, 1/2)</td><td>0.4028</td><td>76.56</td><td>A:B:C:</td><td>—50</td><td>—</td><td>—100</td><td>—</td><td>—50</td><td>—150</td><td>—50</td><td>—</td><td>—50</td><td>—</td><td>—100</td><td>—100</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>3</td><td>A: (1/2, 1/4, 1/4)B: (1/4, 1/4, 1/2)C: (1/4, 1/4, 1/2)</td><td>0.4651</td><td>84.375</td><td>A:B:C:</td><td>—50</td><td>—</td><td>—100</td><td>—</td><td>—50</td><td>—50</td><td>—50</td><td>—</td><td>—50</td><td>—</td><td>—100</td><td>—100</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>4</td><td>A: (2/3, 1/6, 1/6)B: (1/6, 2/3, 1/6)C: (1/6, 2/3, 1/6)</td><td>0.529</td><td>66.67</td><td>A:B:C:</td><td>—150***</td><td>—</td><td>—100</td><td>—</td><td>—50</td><td>—50</td><td>—50</td><td>—</td><td>—50</td><td>—</td><td>—112.5*</td><td>—100</td><td>—</td><td>—</td><td>—</td><td>—</td></tr></table>

<table><tr><td rowspan="3">5</td><td rowspan="3">A: (2/3, 1/6, 1/6)B: (1/6, 2/3, 1/6)C: (1/6, 1/6, 2/3)</td><td rowspan="3">0.9163 67.13</td><td>A: — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>B: —</td><td>—</td><td>—</td><td>—</td><td>50</td><td>50</td><td>50</td><td>—</td><td>100</td><td>100</td><td>—</td><td>—</td><td>—</td></tr><tr><td>C: 150***</td><td>150**</td><td>150#</td><td>—</td><td>—</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td>50</td><td>150</td><td>150</td></tr><tr><td rowspan="3">6</td><td rowspan="3">A: (2/3, 1/6, 1/6)B: (1/6, 1/6, 2/3)C: (1/6, 1/6, 2/3)</td><td rowspan="3">1.058 76.85</td><td>A: —</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>B: —</td><td>—</td><td>—</td><td>—</td><td>50</td><td>50</td><td>50</td><td>—</td><td>150**</td><td>100</td><td>—</td><td>—</td><td>150</td></tr><tr><td>C: 50</td><td>150**</td><td>150#</td><td>—</td><td>—</td><td>—</td><td>—</td><td>150***</td><td>—</td><td>—</td><td>50</td><td>100</td><td>—</td></tr><tr><td rowspan="3">7</td><td rowspan="3">A: (4/5, 1/10, 1/10)B: (1/10, 4/5, 1/10)C: (1/10, 1/10, 4/5)</td><td rowspan="3">0.905 60.00</td><td>A: —</td><td>—</td><td>—</td><td>150**</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>150</td></tr><tr><td>B: —</td><td>—</td><td>—</td><td>—</td><td>—</td><td>50</td><td>50</td><td>—</td><td>100</td><td>100</td><td>—</td><td>—</td><td>—</td></tr><tr><td>C: 50</td><td>100</td><td>—</td><td>50</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td>50</td><td>100</td><td>—</td><td></td></tr><tr><td rowspan="3">8</td><td rowspan="3">A: (4/5, 1/10, 1/10)B: (1/10, 4/5, 1/10)C: (1/10, 1/10, 4/5)</td><td rowspan="3">1.567 60.10</td><td>A: —</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>B: —</td><td>—</td><td>—</td><td>—</td><td>—</td><td>50</td><td>50</td><td>—</td><td>100</td><td>100</td><td>—</td><td>—</td><td>—</td></tr><tr><td>C: 50</td><td>150**</td><td>150#</td><td>50</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td>50</td><td>150**</td><td>150</td><td></td></tr><tr><td rowspan="3">9</td><td rowspan="3">A: (4/5, 1/10, 1/10)B: (1/10, 1/10, 4/5)C: (1/10, 1/10, 4/5)</td><td rowspan="3">1.810 67.80</td><td>A: —</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>B: —</td><td>—</td><td>—</td><td>150#</td><td>50</td><td>50</td><td>50</td><td>—</td><td>100</td><td>150**</td><td>—</td><td>—</td><td>—</td></tr><tr><td>C: 50</td><td>150**</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>50</td><td>—</td><td>—</td><td>50</td><td>100</td><td>150</td></tr></table>

Table 2 Continued

\* Incentives less than 50; \*\* incentives equal 50; \*\*\* incentives more than 50; # lowest bidder is not selected; σ (skewedness) = measure of the dispersion among the vendors for each probability scenario.
Note: A dash (—) denotes vendors A, B, or C that are not getting the contract.
There are nine representative examples, shown in rows 1 to 9. Each row has different probability distributions for vendors A, B, and C. The columns represent all possible combination of bids from the three vendors. For example, the first row explains that if vendors A, B, and C's probability distributions are (1/2, 1/4, 1/4), (1/4, 1/2, 1/4), and (1/4, 1/2, 1/4) respectively for the possible bid value of (50, 100, 150), the expected optimal cost to the user firm is \$75. Also, the second column after the optimal expected cost column in the first row explains that if all vendors bid at \$50, vendor C is awarded the contract at \$50. All other cells are interpreted in the same way for all possible combinations of bids.

mechanism $^{6}$ case is \$117.54 (by following the analysis presented earlier).

If the user firm knows how much the three noncolluding vendors value the current job, and then makes a contract with a vendor who offers the least bid, the expected value of this contract is 62.5. $^{7}$ This is the least possible expected cost to the user firm when perfect information is available. However, in the worst case, the user firm has to pay out 150 if all three vendors bid 150. The optimal minimum expected cost is expected to lie somewhere within this range. Unless a vendor's value for a job of the size being bid is 150, it is not advantageous to the vendor to bid 150 because of a low possibility of being awarded the contract. Without knowing a vendor's true value structure, it is also difficult for the user firm to lower its expected minimum cost to 62.5. However, by following the mechanism design described here, the user firm can lower the optimal cost to 67.13 (see Table 2). This value is significantly lower than the expected value of the no-revelation-mechanism strategy, 117.54. The no-revelation-mechanism strategy allows vendors to obtain the highest expected surplus. However, when mechanism design (as shown here) is used by the user firm, inflating bids is not at all advantageous to the vendors because of the low possibility that they will win the contract. The minimum expected cost to the user firm obtained by following mechanism design is undominated (lower than or equal to the expected cost) by any other mechanism, according to the revelation principle.

## Discussion and Model Results

LET US CONSIDER TABLE 2. FOR EACH DISCRETE BID of \$50, \$100, and \$150, there is an associated probability distribution for the incumbent vendor A. Distributions of vendor A are: (1/2, 1/4, 1/4) from rows 1 to 3, (2/3, 1/6, 1/6) from rows 4 to 6, and (4/5, 1/10, 1/10) from rows 7 to 9. These distributions are left skewed because the incumbent has competitive advantage over the other two challenging vendors B and C, while vendor B and C have probability distributions that are skewed more to the right than the incumbent's probability distributions in every row from 1 to 9.

Consider the optimal expected cost from rows 1, 4, and 7, or rows 2, 5, and 8, or rows 3, 6, and 9. We find that the use of the bidding mechanism results in a steady decrease in the expected optimal cost for all three cases. For example, for rows 1, 4, and 7, the optimal expected cost to the user firm decreases from \$75.00 to \$60.00. This can be explained as follows: the more competitive the incumbent vendor is (i.e., the more left-skewed the distribution), the better the mechanism is able to counter the tendency to inflate bids on the part of the bidders. The mechanism delivers in terms of more competitive bids more often and hence the lower expected cost to the user firm.

However, within each set of probability distributions—that is, rows 1–3, or rows 4–6, or rows 7–9—the expected optimal cost to the user firm increases. This implication is that as the competing vendors B and C get to be less and less competitive with respect to the incumbent vendor A (i.e., their distribution becomes more right-skewed), there is greater opportunity for A to inflate bids. The system reacts by providing greater subsidies/incentives to vendors to bid low and thus increases the

expected cost to the user firm.

In Table 2, one can observe the following from the optimal results of the mixed integer model:

1. In a large number of cases, though not all, a challenger is favored over the incumbent whenever their bids are equal. The exceptions occur in the column of (100, 150, 150) wherever the # sign is positioned (rows 5, 6, 8, and 9). For these (#) cells, there are two common features: the probability structures among bidders are more asymmetric than those of other rows, and the low-cost bidders (A and B) inflate costs. On the basis of these two common features, it is possible to interpret that the low-cost bidder is not necessarily awarded the contract when the low-cost bidder is believed to inflate cost. This implies a “weak stick” policy against the incumbent vendor.

2. In most cases, the user firm awards the contract at a higher value than the lowest bid, when the bids received are toward the lower end. This constitutes an inducement or “carrot,” to vendors to bid their most competitive value. Vendors bidding low have a “safety net” with this policy.

In addition, the types of probability distribution associated with the vendors play an important role in the final outcome of the expected cost and the nature of the prescriptions to be followed. For this reason we investigate three diverse scenarios (see figures 3, 4, and 5).

## Three Scenarios

Let L represent a positively skewed probability structure, M represent a structure skewed toward medium value, and H represent a negatively skewed probability structure.

1. Scenario type LMM (figure 3): The first letter, L, stands for the probability structure of vendor A, the second letter, M, stands for the probability structure of vendor B, and the third letter, M, stands for the probability structure of vendor C. Here both the challenging vendors have a medium distribution (type M), while the incumbent has a positively skewed distribution (type L). Examples are rows 1, 4, and 7 in Table 2.

2. Scenario type LMH (figure 4): Here one of the challengers has a structure that has a skewness of zero (type M), and the other is negatively skewed (type H). Examples are rows 2, 5, and 8 in Table 2.

3. Scenario type LHH (figure 5): Here the incumbent's distribution is positively skewed as usual (type $L$ ), the other two vendors have a distribution that is highly negatively skewed (type $H$ ). Examples are rows 3, 6, and 9 in Table 2.

In each figure, we compare two strategies. One is the optimal strategy that results from the mixed integer programming model. The second, a more easily implementable version, is a stronger version of the “weak stick” strategy against the incumbent vendor

Probability Structures

Downloaded by [University of Pennsylvania] at 09:50 07 May 2016  
![](/api/attachments/4SSY3R7Z/fulltext/images/69929d5fa311660bd5b8397fb52f873e19c637214054ef776974c6dec8085948.jpg)  
Figure 3. Expected Values for LMM Scenario

![](/api/attachments/4SSY3R7Z/fulltext/images/716dc9f48396beaf47779728bed9e338d558cafce7b054865e6744deb398e72a.jpg)  
Probability Structures  
Figure 4. Expected Values for LMH Scenario

Downloaded by [University of Pennsylvania] at 09:50 07 May 2016  
![](/api/attachments/4SSY3R7Z/fulltext/images/f664785ec3ce48319cd782c904adc5dc2ce7ac4cecbf593364a748038c6f4abf.jpg)  
Probability Structures  
Figure 5. Expected Values for LHH Scenario

observed above and is what we call the “challenger preferred” strategy (see Table 3). The idea here is to pressure the incumbent vendor by minimizing her chances of getting the contract whenever she bids the same as or more than the challengers. The following constraints are added to the mixed integer outsourcing model to represent the challenger preferred strategy.

For all $k, i$ , and $j$ ,

If $C^k > C^i \geq C^j$ , or $C^k > C^j \geq C^i$ , then $X A_{kij} = 0$ ,

If $C^i > C^k \geq C^j$ , or $C^i > C^j \geq C^k$ , then $XB_{kij} = 0$ ,

If $C^j > C^k \geq C^i$ , or $C^j > C^i \geq C^k$ , then $XC_{kij} = 0$ ,

If $C^i > C^k$ and $C^j > C^k$ , then $X A_{kij} = 1$ ,

If $C^j > C^i$ and $C^k > C^i$ , then $XB_{kij} = 1$ , and

If $C^k > C^j$ and $C^i > C^j$ , then $XC_{kij} = 1$ .

Following these constraints, the incumbent knows that if she were to inflate her bid to be the same as the challenger's bid she would be taking a risk of always being rejected for the outsourcing job.

For the LMM scenario (see figure 3), the model was run at eight different probability values. For all the different probability distributions, the “challenger-preferred” strategy gave exactly the same result as the optimal strategy. This shows that whenever the LMM scenario is true, adhering to the “challenger-preferred” strategy has several advantages:

1. The “challenger-preferred” strategy is insensitive to the actual probability values used. From this point of view the model is extremely robust.

2. The “challenger-preferred” strategy is easy to describe, understand, and implement for bid evaluation on the part of the user firm.

3. Such a policy of bid evaluation has a certain similarity to bid advantages provided to “minority” vendors in government contracting, and in private contracting when user firms attempt to broaden the supplier base by preferring newer vendors even if their bids are marginally higher.

4. When the user firm declares that this is the strategy to be adhered to, the vendors can easily derive what the consequences of their behavior would be. This results in getting the incumbent vendor to behave as the model predicts, as a “rational” player leading to a “real-world” cost in line with the model’s optimal cost to the user firm.

The situation is very similar though not always exactly equal to the optimal mixed integer solution when the scenario is LMH for most of the probability distributions considered (see figure 4). In view of the advantages of “simple” interpretations, for practical purposes it may be wise to adopt the “challenger-preferred” strategy even in the LMH scenario. The model is by and large robust to the actual probability values input to the model.

For the LHH scenario there is no obvious and easy interpretation available for the evaluation strategy as prescribed by the optimal bidding model. “Challenger-preferred” strategy is no longer optimal or near-optimal in most cases (see figure 5).

However, for the probability distributions' edge represented by point 6 (A's distribution is [1/2, 1/4, 1/4] and the challengers' distribution is [1/4, 1/4, 1/2]) and point 8 where there is no difference between the vendors' probability distributions, the optimal strategy provides the same optimal value as the "challenger-preferred" strategy. This suggests that a more complex strategy be followed for probability distributions that are quite divergent (high standard deviation of skewness), the LHH case. For example, the "weak stick" strategy may be more useful than the "strong stick" policy, i.e., when the bids by the challengers are the same as the incumbent, instead of awarding the bids all the time to the challengers, they may sometimes be awarded to the incumbent.

To summarize the result of three scenarios, the challenger-preferred strategy is easy to implement and recommended if bidders are similar in terms of cost structures. In scenarios when the market is matured, firms have similar cost structures, which in turn results in high competition among vendors. This is the case where the challenger-preferred strategy can be used most effectively. In contrast, if bidders' cost structures are largely asymmetrical, the user firm should use the challenger-preferred strategy with caution because it might increase the costs. High-cost asymmetry among vendors refers to a situation where there are dominant vendors. If one vendor dominates the market with low costs, it is obviously hard to pressure that vendor.

In general, the different scenarios suggest that subsidies need to be given to induce the bidders to bid low. However, instead of promising a blanket subsidy to all vendors, the following general advice is revealed by the analysis: (1) A large subsidy is given to the vendor who quotes a lower bid if there is a large difference between the two bids, and (2) a small subsidy is given, if any, if both vendors bid low. The intuitive explanation is that a subsidy should be given when bids are at the lower end in order to promote low bids by the bidders.

Our results reveal that low bids are not always chosen. This may sound odd; however, this result is explained by the theory of discriminatory auctions in the case of asymmetric bidders $[24, 26]$ . Moreover, user firms do not always achieve the low bid since they provide some amount of subsidies. These two results should be carefully scrutinized by IS managers because our study results are consistent with reality and can provide guidelines for managers who face these types of problems.

There are other reasons why low bids are not necessarily awarded the contract $^{8}$ : First, it has been often observed that the winning bidder faces the phenomenon of winner's curse. A low bidder often bids so low that it is forced to request additional costs or to deliver poor service. Second, reputation is another driving force that results in extra costs. Reputation is usually associated with some real capabilities, including technical expertise or high-quality service. When companies do not have the ability to fully evaluate a vendor's quality, they tend to rely on reputation. Third, if a vendor offers flexible or favorable terms that minimize the side effects of outsourcing, this vendor is sometimes awarded the contract instead of lower bidders. For example, if the vendor promises to retain displaced employees, it can help to reduce the real costs for the firm and avoid severe impacts on employee morale.

In view of the above, there are several features of our approach that make it appropriate for use in outsourcing tendering situations. First, implementation of stick and carrot policies (preferential strategies and subsides) are believed to be feasible and allow explicit guidelines to handle the above realities effectively. For instance, private firms have considerable flexibility in how they evaluate submitted bids in order to serve their interests best. In government bidding also, RFPs normally make clear that the lowest bidder will not necessarily be awarded the bid. Second, the number of bidders in the final short list usually corresponds to the number of bidders considered in this model. Third, the model is robust—that is, irrespective of the actual numerical values used in the input, the final prescriptions that can be drawn from the model output are consistent. As long as the judgment regarding the scenario to be used is right, the prescriptions from the models can be used to guide bid evaluation. Fourth, cost and/or expertise asymmetry is commonly observed. Finally, the underlying assumptions of the model such as self-serving, competitive, and noncolluding behavior are likely to be satisfied in most real-world situations.

## Conclusion

BOTH PRACTITIONERS AND RESEARCHERS ARE CONCERNED THAT IS investments of a trillion dollars in the 1990s may not yield commensurate gains. Any tool that allows the reduction of IS operations costs and is theoretically sound should be of interest to IS researchers and practitioners. Outsourcing is one such information management tool and has been addressed often in IS trade literature [7, 8, 10, 12, 13]. This literature has frequently discussed bidding processes that select one outsourcing vendor [17]. Selection of a low-cost vendor is one of the major success factors for routine IS operations and cost has been predominantly cited as the “dominant” motivation for outsourcing [8].

Current research in outsourcing is predominantly descriptive and empirical $[19, 21]$ . In contrast, the research in this paper is of the prescriptive kind. It demonstrates how economic theory techniques can be operationalized using management science tools. The objective is to build tools that can be utilized to prescribe actions for IS managers to reduce costs, that is, to generate prescriptions for the problem of cost-effective outsourcing. While the method described here is mathematical, the conclusions that flow from this mathematical exposition have natural and qualitative interpretations that can allow managers in the field to adopt the qualitative guidelines.

This paper has investigated two primary questions. The first question concerns the likelihood of a user firm's ability to reduce or minimize costs by designing mechanisms that induce incumbent vendors to submit low bids in environments that involve routine and repetitive activities like network maintenance. The second question concerns the prescriptive and implementation issues involved in the design of such mechanisms.

The paper has developed a structured description of the outsourcing process. In addition, the model developed herein has allowed the development of practitioner guidelines about how to structure a bidding process whereby the user firm can obtain the most competitive bid. Interestingly, it is not necessary for the user firm to estimate the precise cost profiles of the vendors in order to adhere to our suggested policy guidelines: the carrot and stick policies. First, if vendors bid the same, the challenger is awarded the bid in most of the scenarios covered in this paper. Second, if the incumbent vendor is believed to inflate her bid, she is penalized, since the user firm would then award the contract to the challenger. Third, subsidies are awarded to compensate and encourage vendors to bid low. So when a vendor bids low, chances of winning improve and at the same time there is a some limited protection against incurring a loss during execution of the contract.

These procedures have interesting interpretations that most practicing managers would immediately recognize as negotiation approaches which they themselves may have followed on occasions. The procedures not only enhance the user firm managers' negotiation abilities, they also increase their repertoire of negotiation or bidding strategies. Also, preferential treatment in favor of challengers is a well-known practice by user firms that is used to increase competition and to escape from the clutches of single suppliers. This preferential treatment makes the bidding situation more attractive to challengers and it not only induces more challengers to participate but also to bid aggressively. However, instead of providing a blanket subsidy or preferential treatment, which is the common method of practicing preference, the proposed model provides very detailed guidelines for the user firm managers. In addition, the model allows the user firm to devise a policy regarding how much to subsidize or how much preferential treatment to give under what conditions. It also parallels some bidding behavior practices observed in the real world. This research has implications for both the practitioner and the researcher. Practitioners can be guided in setting up a bidding mechanism that can lead to more competitive bids under certain circumstances. Researchers can evaluate the implications of utilizing mechanism design in the practical context of an outsourcing tendering situation.

In summary, to our knowledge, this paper is one of the earliest attempts to explore the limits of the utility of economic theory and management science optimization in studying cost asymmetry, individual rationality, and incentive compatibility in outsourcing, a line of research suggested by Loh and Venkatraman $[21]$ . Of course, because of the complexities of reality, it is not possible to map all aspects of the real world into the modeling environment. Therefore, we have, in the spirit of Simon $[37]$ attempted “to capture in our models a simplified picture of reality, which nevertheless allow us to make inferences that are important to our goals.” In retrospect, we consider this research a qualified success. We have been able to describe scenarios where the solutions suggested by the model are easily implementable and scenarios where they are not.

The model developed here obviously cannot entirely reflect all of the outsourcing bidding process. We have made some restrictive assumptions as is common in studies based on economic theory. By relaxing some assumptions, researchers can develop more realistic models that will enhance the quality of the bidding selection process. However, our model handles certain important issues such as selection of a low-cost vendor for routine IS operations, while incorporating the tendency for misrepresentation among vendors.

## NOTES

1. Here we subscribe to the commonly held notion that an incumbent would generally have a lower cost structure than other vendors. This is not, however, necessarily always the case, and the model developed here is valid for any low-cost structure vendor.

2. Readers interested in exploring the theory behind Kreps's model may see Myerson's seminal papers on auction design [25, 26, 27], and McAfee and McMillan's comprehensive paper on auctions and bidding [24].

3. This phenomenon is called winner's curse [24]. Here the winner of a bidding exercise loses because of aggressive bidding.

4. There are other types of mechanisms such as the Clarke-Groves mechanisms [31], and AGVArrow mechanisms [9], which study efficient allocation in auctions. The Clarke-Groves charge is a very powerful tool. However, “implementation faces a number of practical and theoretical obstacles .... the Clarke-Groves charge is complex and difficult (for users) to understand” [31, p. 99]. Readers interested in a game-theoretic analysis of mechanism design may see Fudenberg and Tirole [9].

5. For the origin of Kreps's model, readers are referred to the revelation principle [25, 26, 27].

6. Hereafter, for convenience, we call this the “no-revelation-mechanism.”

7. $\sum_{k}\sum_{i}\sum_{j}\left\{v_{kj}*\text{MIN}\left\{C^{k},C^{i},C^{j},\right\}\right\} = 62.5$

8. We are grateful to an anonymous referee who pointed these out to us.

## REFERENCES

1. Apte, U. and Winniford, M. Global outsourcing of information systems functions: opportunities and challenges. In M. Khosrowpour (ed.), Managing Information Technology in a Global Society. Harrisburg, PA: Idea Group Publishing, 1991, pp. 58–59.

2. Bakos, J.Y., and Kemerer, C.F. Recent applications of economic theory in information technology research. Decision Support Systems, 8, 5, (September 1992), 365–386.

3. Banker, R.D., and Kemerer, C.F. Performance evaluation metrics for information systems development: a principal-agent model. CISR WP NO 243, MIT (July 1992).

4. Bets, M. Real IS payoff lies in business benefits. Computerworld (January 3, 1994), 10, 56.

5. Chaudhury, A.; Rao, H.R.; and Nam, K. Mixed integer programming for outsourcing bidding. Research-in-Progress Paper, Proceedings of the 14th International Conference on Information Systems, Dallas, 1992, p. 263.

6. Chester, J.S. National goes with EDS-IBM beat out for major outsourcing. Communications Week (January 21, 1991), 42.

7. Clermont, P. Outsourcing without guilt. Computerworld (September 9, 1991), 67.

8. Eckerson, W. Outsourcing: a tough call for net execs. Network World (July 9, 1990), 1, 52.

9. Fudenberg, D., and Tirole, J. Game Theory. Cambridge, MA: MIT Press, 1992.

10. Gantz, J. Outsourcing: threat or salvation? Networking Management (October 1990), 25–40.

11. Gurbaxani, V., and Kemerer, C.F. An agent-theoretic perspective on the management of information systems. Proceedings of the 22nd Hawaii International Conference on System Sciences, January 1989, pp. 141–150.

12. Halper, M. IBM pilot reduces outsourcing costs. Computerworld (October 26, 1992), 1, 16.

13. Halper, M. Smarts prevail in the area of doubtsourcing. Computerworld (January 4, 1993), 8–10.

14. Jacobs, P. Some assembly required: even with industry-standard components, it takes some work to put together a heterogeneous environment. DG Review, 12, 9 (March 1992), 25.

15. Johnston-Turner, M. The new players: common carriers. Network World (February 17, 1992), 34.

16. Johnston-Turner, M. The first step to outsourcing. Data Communications, 21, 1 (January 1992), 23.

17. Johnston-Turner, M., and Juneau, L. Crafting a net outsourcing strategy. Network World (February 17, 1992), 34.

18. Kreps, D. A Course in Microeconomic Theory. Princeton, NJ: Princeton University Press, 1990.

19. Lacity, M.C., and Hirschheim, R. Information Systems Outsourcing: Myths, Metaphors, and Realities. New York: John Wiley, 1993.

20. Ledyard, J. Incentive compatibility. In J. Eatwell, M. Milgate, and P. Newman (eds.), Allocation, Information and Markets. New York: Norton, 1989, pp. 141–151.

21. Loh, L., and Venkatraman, N. Diffusion of information technology outsourcing: influence sources and the Kodak effect. Information System Research, 3, 4 (December 1992), 334–358.

22. Loh, L., and Venkatraman, N. Determinants of information technology outsourcing. Journal of Management Information Systems, 9, 1 (Summer 1992), 7–24.

23. Mandel. M.J. How game theory rewrote all the rules. Business Week (October 24, 1994), 44.

24. McAfee, R.P., and McMillan, J. Auctions and bidding. Journal of Economic Literature, 25 (June 1987), 699–738.

25. Milgrom, P. Auction and bidding: a primer. Journal of Economic Perspectives, 3, 3 (Summer 1989), 3–22.

26. Myerson, R.B. Mechanism design. In J. Eatwell, M. Milgate, and P. Newman (eds.), Allocation, Information and Markets. New York: Norton, 1989, pp. 191–206.

27. Myerson, R.B. Optimal auction design. Mathematics of Operations Research, 6, 1 (February 1981), 58–73.

28. Myerson, R.B. Incentive compatibility and the bargaining problem. Econometrica, 47, 1 (January, 1979), 61–73.

29. Nam, K. Three essays on information systems outsourcing. Ph.D. dissertation, SUNY Buffalo, 1995.

30. Nam, K.; Chaudhury, A.; and Rao, H.R. A mixed integer model of bidding strategies in outsourcing. European Journal of Operational Research (1995), forthcoming.

31. Philips, L. The Economics of Incomplete Information. Cambridge: Cambridge University Press, 1988.

32. Pick, R.A., and Whinston, A.B. A computer charging mechanism for revealing user preferences within a large organization. Journal of Management Information Systems, 6, 1 (Summer 1989), 87–100.

33. Rassenti, S.; Smith, V.L.; and Bulfin, R.L. A combinatorial auction mechanism for airport time slot allocation. Bell Journal of Economics, 13, 2 (Autumn 1982), 402–417.

34. Richmond, W.B., and Seidmann, A. Software development outsourcing contract struc-

34. Richmond, W.B., and Seidmann, A. Software development outsourcing contract structure and business value. Journal of Management Information Systems, 10, 1 (Summer 1993), 57–72.

35. Richmond, W.B.; Seidmann, A.; and Whinston, A.B. Incomplete contracting issues in information systems development outsourcing. Decision Support Systems, 8, 5 (September 1992), 459–477.

36. Schmerken, I. Outsourcing holds the line on technology costs. Wall Street Computer Review, 8, 4 (January 1991), 12.

37. Schrage, L. Personal communication, October 29, 1994.

38. Simon, H.A. Prediction and prescription in systems modeling. Operations Research, 38, 1 (January–February 1990), 7–14.

39. Smith, V. Auctions. In J. Eatwell, M. Milgate, and P. Newman (eds.), Allocation, Information and Markets. New York: Norton, 1987, pp. 39–53.

40. Socolovsky, A. Computer service evolves into outsourcing. Electronic Business (September 3, 1990), 23.

41. Waller, W.S., and Bishop, R.A. An experimental study of incentive pay schemes, communication, and intrafirm resource allocation. The Accounting Review, 65, 4 (October 1990), 812–836.

42. Wilder, C. Giant firms join outsourcing parade. Computerworld, 35, 39 (September 30, 1991), 1, 91.
