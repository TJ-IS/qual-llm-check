---
otero_id: 4532
otero_key: "QNMXD9AN"
title: "Mobile coupons delivery problem: Postponable online multi-constraint knapsack"
authors: "Keumseok Kang; Kemal Altinkemer; Inkyoung Hur"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.10.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Mobile coupons delivery problem: Postponable online multiconstraint knapsack

![](/api/attachments/QNMXD9AN/fulltext/images/98143d6d0b794ae30f0c833ad89bab2d508016104afbfb063381b447b0defedb.jpg)

Keumseok Kang, Kemal Altinkemer, Inkyoung Hur

<table><tr><td>PII:</td><td>S0167-9236(18)30161-1</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.10.004</td></tr><tr><td>Reference:</td><td>DECSUP 12996</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>9 March 2018</td></tr><tr><td>Revised date:</td><td>8 September 2018</td></tr><tr><td>Accepted date:</td><td>9 October 2018</td></tr></table>

Please cite this article as: Keumseok Kang, Kemal Altinkemer, Inkyoung Hur , Mobile coupons delivery problem: Postponable online multi-constraint knapsack. Decsup (2018), doi:10.1016/j.dss.2018.10.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Mobile Coupons Delivery Problem: Postponable Online Multi-Constraint Knapsack

Keumseok Kang College of Business, Florida International University, Miami, Florida 33199 kskang@fiu.edu

Kemal Altinkemer Krannert School of Management, Purdue University, West Lafayette, Indiana 47907 kemal@purdue.edu

Inkyoung Hur College of Engineering and Computing, Nova Southeastern University, Fort Lauderdale, Florida 33314 ihur@nova.edu

## Abstract

We study the mobile coupons delivery problem (MCDP) in a push-based location based advertisement where an advertiser proactively sends mobile coupons to prospective customers on behalf of stores based on the customers’ location and preferences. MCDP provides a new capability called postponable selection that enables an advertiser to better capitalize on the plethora of customer information provided by mobile phone users through network service providers. Postponable selection allows a customer to be reconsidered for selection for coupon delivery (i.e. postponed) as more information becomes available. We formulate MCDP as a new problem category referred to as the postponable online multi-constraint knapsack. We propose a single threshold-type algorithm with different design options and conduct extensive computational experiments to discuss the effectiveness of our algorithm as well as the benefit of postponable selection. Our experimental results show that the proposed algorithm outperforms the First-Come-First-Serve heuristic by 46% and postponable selection additionally improves performance by 4% on average.

Keywords: mobile coupons delivery problem, online multi-constraint knapsack problem, online algorithm, postponable selection, computational experiment

# ACCEPTED MANUSCRIPT

## Mobile Coupons Delivery Problem: Postponable Online Multidimensional Knapsack

## 1. Introduction

As the number of mobile phone users worldwide is expected to reach 5.07 B in 2019 (a 26% increase since 2013) [1], businesses and advertisers continually seek new ways to take advantage of this rapidly expanding market sector. Along with the pervasive growth of the mobile phone market, recent advances in mobile technologies have created valuable new location information about cell phone users. Location information provides the real-time coordinates of entities, such as parcels, vehicles, and people. Location Based Advertisement (LBA) is a contextual marketing technique that has emerged as a promising next generation advertising method that uses this new data set [2-4]. Whereas first generation contextual marketing tools—such as personalized web sites, recommendation systems, search engine advertisements, and email campaigns—do not capture the coordinates of target customers, LBA provides advertisers with this additional dimension of information to more effectively attract their target customers [2-4] when sending relevant advertisements through personal mobile devices. The advertisements usually contain favorable offers such as discounts or traditional coupons [2, 5, 6] called “mobile coupons” [7, 8]. In LBA, an advertiser wants to maximize its profit by providing potential customers with targeted mobile coupons at the optimal time and place, capitalizing on the location, and possibly individual preferences, of customers. We refer to the identification and optimization of these variables as the mobile coupons delivery problem (MCDP).

To study MCDP in digital advertisement, the knapsack problem, a well-known combinatorial optimization problem [9], has been applied [10, 11]. A knapsack problem with multiple constraints is referred to as the multi-constraint knapsack problem (MKP) [12-15]. If decisions on how to pack the knapsack are made simultaneously, the problem is called the offline MKP, while if the decisions are not made at once but sequentially, the problem is called the online MKP. The offline MKP has been used to study the deterministic version of MCDP [5, 6].

In contrast, we study the dynamic version of MCDP in push-based LBA, a specific type of LBA in which an advertiser proactively pushes mobile coupons to customers’ cell phones. This problem has a unique characteristic, referred to as postponable selection, which allows the delivery of a coupon to be postponed. The traditional online MKP cannot represent this postponable selection. Therefore, we propose a new problem category, referred to as postponable online MKP.

The purpose of this study is to formulate the dynamic version of MCDP in push-based LBA using the concept of postponable online MKP, propose a basic algorithm, and provide insights on how the algorithm is influenced by key problem parameters by conducting extensive computational experiments.

The remainder of the paper is organized as follows. In §2, we provide background information about LBA and MCDP. In §3, we review the related literature and discuss how this study differs from the existing literature. In §4, we formulate the problem as a postponable online MKP. In §5, we propose a single threshold-type algorithm with 10 different combinations of design options. In §6, we conduct extensive computational experiments and discuss the effectiveness of the proposed algorithm. We show that postponable selection improves the performance of our algorithm, ultimately improving the delivery of mobile coupons in push-based LBA. In §7, we discuss contributions, limitations, and future research.

## 2. Background context

## 2.1. Pull- versus push-based LBA

Depending on who initiates the process of sending mobile coupons, an advertiser could implement LBA in two different ways: pull-based LBA and push-based LBA [3, 4, 16]. Pull-based LBAs are similar to search engine advertisements. Customers initiate receiving mobile coupons by actively searching for mobile coupons (or information) about nearby stores by entering keywords. Then, an advertiser sends mobile coupons based on the integration of the keywords entered and the location of customers. In pushbased LBAs, the advertiser initiates the process of sending mobile coupons. Here, an advertiser can proactively send mobile coupons to potential customers via mobile devices based on their location, product or store preferences, and demographics—even if the customer is not searching for anything. In push-based LBAs, for privacy reasons, an advertiser is generally required to get explicit consent from customers before using their geographic and demographic information to send them mobile coupons [17]. Conceptually, push-based LBAs are more attractive to advertisers and stores because they are more apt to trigger impulse buying [1]. However, push-based LBAs are generally much more complex than pullbased LBA’s, and are consequently more difficult to manage and operate. Hence, we are focusing on the push based LBA in this paper.

## 2.2. General settings of a push-based LBA

Still early in its evolution, push-based LBA is a new marketing tool that could provide potentially transformative opportunities for stores, customers, and advertisers. Currently, there are a number of pushbased LBA variations using different approaches, constraints, and technologies. For the purpose of this study, we define push-based LBA using the elements and constraints essential to every variation [2, 5, 6, 18]. This includes four different parties—customers, stores, an advertiser, and network service providers—and two environmental entities—a target area and regions

A target area is where an advertiser and stores are interested in sending mobile coupons [5, 6]. For instance, it could be a mall like in the case of De Reyck and Degraeve [6], or it could be a downtown area. A target area will then be subdivided into multiple regions [5]. A region is a physical segment of the target area. However, regions do not have to be physically adjacent to each other and may each have different shapes or sizes.

Prospective customers who have consented to receiving mobile coupons from the advertiser may visit the target area. In LBA, regions within the target area are mutually exclusive, meaning a customer between regions at any time. A probable scenario is as follows: a customer arrives at one region in the target area, stays for a while at the region, moves to another region and stays there for a while, repeats moving and staying, and finally leaves the target area. Stores are physically located in a region. They aim to attract potential customers by sending mobile coupons to mobile phone users while they are in select regions.

Network service providers provide technical infrastructure that enables an advertiser detect the locations of customers and send mobile coupons to customers [5, 6, 18]. The locations of customers can be detected by a number of technologies such as global positioning system, wireless internet, cellular network, and indoor sensors like beacons. Also, mobile coupons can be sent via various ways, such as text messages, multimedia messages, and app notifications. Examples of network service providers include cellular phone carriers (e.g., Verizon), bulk message providers (e.g., Twilio), mobile app platform providers (e.g., Apple), indoor map service providers (e.g., Google), and so on.

Due to technical limitations and privacy issues, stores generally do not send mobile coupons directly to customers. Therefore, an intermediary works between the three LBA parties (customers, stores, and network service providers) to send mobile coupons to potential customers on behalf of stores [5, 18, 19]. Customers allow this intermediary entity to use their location information. And, in some cases customers also allow access to additional information such as their product preferences, purchase history, and demographic information. We refer to this intermediate entity as an advertiser.

## 2.3. General settings of MCDP in push-based LBA

A coupon may be sent to a customer using a text or multimedia message that contains a link to retrieve a coupon or sent as a push notification to an app installed in the phones. Each mobile coupon is owned by one store and related to one or more products or services that the store provides. A store may have one or multiple mobile coupons and these are often customized for different customers (e.g., different discount rates, products, etc.). Critical to LBA, the same mobile coupon may have different effects based on customer, region, and time [2, 5, 18].

In a push-based LBA, when a mobile coupon is sent to a customer (or is converted into actual sales), the corresponding store pays the price of the mobile coupon to the advertiser. And, since network service providers possess the technical infrastructure that enables an advertiser to identify the location of customers and send them mobile coupons, the advertiser pays the network service provider the cost of sending the mobile coupon [5, 6, 18]. The prices and costs are determined between the advertiser, stores, and network service providers in several different ways [2]. They may have a fixed structure with predetermined costs or prices negotiated between the parties using historical data [6, 18], or a dynamic structure, with costs or prices dynamically determined by generalized second-price auctions [20]. The approach presented in this study is applicable to any price or cost structure.

# ACCEPTED MANUSCRIPT

In either structure, the price is determined between the advertiser and stores using an incentive compatible mechanism in such a way that when the advertiser maximizes its own objective function (net profit), each store maximizes its own objective function. For example, if a customer has a preference for a certain store (which might be obtained from the customer’s purchase history or demographic information), sending the store’s mobile coupon to the customer should benefit both the store and advertiser. The price should be set (e.g., high price) to motivate the advertiser to send the coupon to the customer.

Like any conventional advertising campaign [10, 11], mobile coupons are generally limited by financial budgets [2]. In LBA, each individual store sets the budget for its mobile coupon campaign, meaning the advertiser cannot send a mobile coupon to a target customer if no budget remains. In addition to budgetary constraints, to be effective, mobile coupon deliveries need to be restricted by what we identify as the “annoyance factor.” Sending what the customer perceives to be too many advertisements will annoy that customer, which will create a negative association and hurt the sales of related products or services [21-24].

Ultimately, the advertiser sends mobile coupons based on the locations and preferences of customers under budget and annoyance constraints. With that, the MCDP is defined as an ideal situation for an advertiser to send mobile coupons by optimally integrating all data sets and constraints. The advertiser’s net profit is determined by the combination of all decisions made during the decision horizon, which allows the MCDP to maximize the net profit of the advertiser.

While the MCDP can be defined as a selection problem, it has unique characteristics when compared to traditional selection problems such as the knapsack, secretary, admission control, search engine auction, and pull-based LBA problems. In these conventional selection problems, a customer explicitly asks for selection by the decision maker (or system). The customer then intentionally waits or abandons the process, and learns whether or not they are selected. However, in a push-based LBA, a customer does not explicitly ask for selection, instead they unintentionally become available to be selected by the decision maker. The customer does not even know that they are being considered for

# ACCEPTED MANUSCRIPT

mobile coupon selection and may unknowingly abandon or leave the system without realizing that selection decisions are being made by the decision maker. Therefore, in the push-based scenario the advertiser leads the process. This could allow the decision maker to postpone the selection decision for a customer and/or reconsider selecting the customer (herein referred to as “postponable selection”), which is not an option in pull-based LBA. For example, suppose a customer who is shopping at a mall needs to have lunch. In a pull-based LBA, the customer asks the advertiser to send available offers from nearby restaurants, and then the advertiser selects and sends the most appropriate coupon to the customer. On the other hand, in a push-based system, the advertiser identifies that the customer may need to have lunch and sends the most appropriate coupon based on the customer’s preference and current location. In this case, the advertiser could have sent a restaurant coupon to the customer when he/she enters the mall, but it may also postpone the delivery until lunch time or he/she moves to a certain area (e.g., food court) to maximize the effectiveness of the coupon. Thus, by postponing selection decisions, the decision maker could have more acute control over their target customer, which may increase the selection effectiveness and impact of the LBA. To enable advertisers to leverage this opportunity, this study addresses the unique challenges associated with postponed decisions in mobile coupons through a new problem category we define as the postponable online MKP.

## 3. Related literature

## 3.1. LBA challenges

Although LBA is a promising contextual marketing tool, there exist challenges and problems to overcome [25], as shown in Fig. 1. These challenges can be divided into two categories: 1) operational problems and 2) behavioral/technical problems. Research on operational problems generally require mathematical modeling with the aim of improving operational performance [3, 6, 18]. The MCDP is a representative problem in this category [3, 6, 18]. MCDP exists in both push-based [5, 6, 18] and pull-based LBAs [3, 4], but differs in many aspects, including who initiates delivery, decisions, constraints, math models, and solution approaches. Unlike MCDP in pull-based LBA where the advertiser sends coupons based on the requests from customers, in MCDP in push-based LBA the advertiser initiates the process of delivering

mobile coupons, which creates a new strategy of postponing the delivery of a coupon. This leads to a special variant of online MKP, postponable online MKP.

<table><tr><td rowspan="2" colspan="3"></td><td colspan="2">Location-Based Advertisement (LBA)</td></tr><tr><td>Push-based LBA</td><td>Pull-based LBA</td></tr><tr><td rowspan="8">Operational Problems</td><td colspan="2">Main research methods</td><td>Math modeling</td><td>Math modeling</td></tr><tr><td rowspan="7">Main issue: MCDP</td><td>Who initiates delivery</td><td>Advertiser</td><td>Customers</td></tr><tr><td>Decisions</td><td>Whom, when, where, and which coupons to send</td><td>Which coupons in which order to send for a request</td></tr><tr><td>Main constraints</td><td>Annoyance, Budget</td><td>Budget</td></tr><tr><td>Target customers</td><td>Any (opt-in) customers</td><td>Customers who request</td></tr><tr><td>Objective</td><td>Maximize the profit of advertiser</td><td>Maximize the profit of advertiser</td></tr><tr><td>Main math models</td><td>Deterministic: Offline MKPDynamic, stochastic: Stochastic dynamic program,Postponable online MKP</td><td>Deterministic: Offline MKPDynamic, stochastic: Stochastic dynamic program,Online MKP</td></tr><tr><td>Solution approach</td><td>Deterministic: Optimal algorithm, heuristicDynamic, stochastic: Optimal policy, online heuristic algorithm allowing postponable selections</td><td>Deterministic: Optimal algorithm, heuristicDynamic, stochastic: Optimal policy, online heuristic algorithm</td></tr><tr><td rowspan="2">Behavioral/technical problems</td><td colspan="2">Main research methods</td><td>Empirical analysis using lab/field experiments,surveys, or archival data orDesign science</td><td>Empirical analysis using lab/field experiments,surveys, or archival data orDesign science</td></tr><tr><td colspan="2">Main issues</td><td>Privacy, annoyance, personalization, coupon types,customer targeting, customer&#x27;s need prediction,location detection and trajectory prediction,customer perception and response</td><td>Coupon types, personalization, location detection,customer perception and response</td></tr></table>

Fig. 1. Framework of LBA problems

For behavioral or technical problems, the main focus is understanding the behavioral phenomena emerging in LBA or designing technical solutions to implement LBA. Research in this category requires qualitative/empirical analyses [26] or design science approaches [27] and provides contextual knowledge (e.g., model parameters) to operational problems. The main issues in this problem category may vary by the type of LBA. Some of the issues, such as types of coupons [28] and location detection [4], are common to both types of LBA. However, push-based LBA seems to have more complicated issues. For example, in push-based LBA, privacy [24, 29] and annoyance [17] become more critical as compared to pull-based LBA. Also, location detection technologies used in pull-based LBA [4] need to be enhanced so that location trajectories can be predicted in push-based LBA [30]. In addition, how customers perceive and respond to LBA is a key question to understanding how to leverage LBA and has been a main research topics [31].

We study MCDP in push-based LBA. Therefore, in the subsequent sections, we will mainly review prior studies on MCDP and related behavioral/technical issues in push-based LBA.

# ACCEPTED MANUSCRIPT

## 3.2. Behavioral and technical problems of push-based LBA

While personalization usually helps to increase profits of the firm, customers’ privacy is one of the main inhibiting factors in the prevalence of push-based LBA [29]. With LBA you can personalize however at the expense of privacy [24]. Another inhibitor is annoyance. Seventy-nine percent of customers think that advertising messages sent through their mobile phones are annoying [19]. Acknowledging that customers who receive push-based LBA have already consented, and are therefore open to some amount of mobile coupons, it is imperative to identify their coupon threshold, or their “annoyance number.” While this is important, it is also extremely subjective and, consequently, very difficult. Therefore, some researchers recommend that the customers set their own annoyance numbers in LBA as part of the consent process [17]. Beyond this, some empirical research investigates the implications behind the types of message sent to customers. For example, multimedia messages are found to be more effective but at the same time more annoying than text messages [28]. Targeting customers and predicting the needs of customers is a challenging but critical task in push-based LBA. Provost et al. [27] propose a concept of geosimilarity network, which uses location-visitation data to find customers with similar tastes. Nevertheless, mobility makes targeting customers more difficult. In an ideal push-based LBA, an advertiser could predict the location trajectory of a customer and send a coupon relevant to the trajectory. Therefore, location trajectory has become an important topic among researchers [30, 32] due to the increased attention to push-based LBA in practice.

## 3.3. MCDP in push-based LBA

Despite increasing attention on push-based LBA, few studies have dealt with the challenge of MCDP in push-based LBA. De Reyck and Degraeve [6]’s work represents the first paper addressing MCDP in push-based LBA. They formulate the problem using deterministic integer programming and propose heuristics to solve the problem using a relaxation and decomposition technique. Tripathi and Nair [5] extend the work of De Reyck and Degraeve [6], showing that if some constraints are relaxed, the original problem can be solved more effectively without altering the original assumptions. Although both papers provide a significant contribution to the literature by introducing the challenges of implementing pushbased LBA, their models have limited application because they are offline models that assume the advertiser knows the future location trajectories of potential customers in advance, which allows the advertiser to make all mobile coupons delivery decisions at once.

Tripathi and Nair [18] go on to address a dynamic version of MCDP in push-based LBA, which assumes that the advertiser only knows the current and past locations of potential customers causing the advertiser to make delivery decisions dynamically as new location information becomes available over time. They also assume that customers’ movements have a Markov property and formulate the problem using a Markov decision process, which is a useful tool to solve stochastic and dynamic decision-making problems but quickly becomes intractable as the problem size increases [33]. Therefore, Tripathi and Nair [18] work cannot sufficiently address the scope of push-based LBA. Although their research provides significant theoretical insights, in practice an effective LBA program needs to manage, evaluate, and integrate a large number of customers with vast amounts of mobile coupons and multiple regions and periods. Therefore, it is imperative to design simple algorithms that can effectively translate the staggering amounts of consumer data into successful push-based LBAs. Therefore, this study provides an alternative way to analyze and solve the dynamic version of MCDP in push-based LBA by developing an algorithm that overcomes the tractability issue of Tripathi and Nair [18]’s approach.

## 3.4. Multi-constraint knapsack problem (MKP)

## 3.4.1. Offline MKP

A knapsack problem with multiple constraints is generally referred to as the MKP [12-15]. The MKP belongs to the NP-hard class [14]. Although effective and efficient approaches have been proposed by pioneering researchers [34-37], the MKP does not have a fully polynomial approximation scheme [9]. And, even finding a fully polynomial approximation algorithm for a problem with more than two constraints belongs to the NP-hard class of problems [15]. For those who are interested in the intricacies of MKP, we recommend Freville [14] and Kellerer et al. [9] as useful references.

## 3.4.2. Online MKP and postponable online MKP

In contrast to offline MKP, in online MKP items are not available a priori. Instead, they become available sequentially over time requiring the decision maker to decide whether or not to select the item to pack into a knapsack whenever an item becomes available [9]. For the category of knapsack problems, the term item generally refers to the target of selection. However, in the specific context of this research, it refers to the pair of customer and coupon. The online knapsack problem is well studied in the literature; however, most studies only consider the single constraint online knapsack [10, 38-40]. There are very few studies that address the online MKP due to its intractability. Pak and Dekker [41] attempt by defining the air cargo revenue problem as a two-dimensional (weight and volume) online knapsack problem and propose an algorithm using bid prices. Each bid price plays the role of a threshold value for each constraint of the MKP. Bid prices were originally used to solve offline MKPs; however, they do not provide optimal solutions [42]. Also, finding good bid prices in an online setting where future incoming items are unknown is difficult. Moreover, it is challenging to analyze the effects of bid prices on the performance of an algorithm because of the multidimensional nature of bid prices. For these reasons, we propose a different approach that uses a single-value threshold to design algorithms for online MKPs that is comparatively easy to implement and evaluate.

Typical online knapsack problems, including online MKPs, assume that items to fill the knapsack are given one at a time, as opposed to by batch. Then, whenever an item becomes available, a decision maker should immediately decide whether or not to select the item to fill the knapsack before the next item becomes available. Importantly, once a decision is made for an item, it cannot be revoked— unselected items cannot be reconsidered for selection, even if the knapsack has room. Because push-based LBA’s could greatly benefit from the ability to delay and reconsider a selection decision as more information is available, these assumptions are not realistic in the dynamic version of MCDP in pushbased LBA that we study in this paper.

Therefore, we define a new variant of online MKP, referred to as the postponable online MKP, and use it to formulate the dynamic version of MCDP in push-based LBA. The postponable online MKP

# ACCEPTED MANUSCRIPT

has the following characteristics: First, any unselected item that has been considered but rejected, may be reconsidered for being selected as long as it is available. Second, because selection decisions do not have to be made immediately but may be postponed, selection decisions for multiple items may be made at the same time. This implies that the model allows a batch arrival. However, when selection decisions are made for multiple items, each item has its own individual decision.

## 3.4.3. Performance measures for online algorithms

The performance of an online algorithm is generally measured by its competitive ratio, which is defined as the ratio of the online algorithm’s output to the optimal output obtained by the corresponding offline algorithm [43]. In a maximization problem, the competitive ratio is less than or equal to one. An online algorithm is k-competitive if the algorithm’s competitive ratio is greater than k on any problem instance [43]. Currently, there is no k-competitive algorithm for the general online MKP [13, 44], which means that there is no known algorithm for which the worst-case performance is bounded. Studies have established algorithms with bounds for single constraint online knapsack problems in some special cases [10, 38], but their results are difficult to extend to the online MKP due to its multiple constraints. Agrawal et al. [45] study the theoretical bounds of algorithms for online linear programs. Although online linear programs and MKP share some common characteristics, their results cannot be directly applied to the online MKP, including its extension, the postponable online MKP.

## 4. Problem formulation

For simplicity we will use MCDP to specifically refer to the dynamic version of MCDP in push-based LBA which is the focus of this study. Customers may arrive or move to a region in the target area at any discussed earlier, in MCDP, mobile coupons do not have to be delivered to customers right after customers arrive or move—their delivery may be delayed. For this reason, as well as for simplicity, we assume that the decision horizon of MCDP is broken down into a finite set of small time periods, and mobile coupons are sent to customers only at the end of each period. Although each period does not need to have the same time interval, without loss of generality, we further assume fixed time periods. Period t

# ACCEPTED MANUSCRIPT

is defined as time interval (t – 1, t], and only at the end of every period (i.e., at every time t) does the advertiser send mobile coupons to customers. We assume that time periods are made narrow enough so that most customers do not take more than one action during a period. Depending on the application context, the time interval of periods could be hours (within a mall) or even minutes (within a store). The following are the definitions of the variables and subscripts used to define MCDP.

## Subscripts:

$i \in I = \{ 1 , \ldots , C \}$ : Customers who visit the target area.

$j \in J = \{ 1 , \dots , A \}$ Mobile coupons.

$t \in T = \left\{ 1 , \ldots , P \right\}$ : Time periods. The decision horizon consists of P time periods.

A customer cannot be located in multiple regions at the same time. So, we define the function l(i,t) in order to reduce the number of decision variables.

$l ( i , t ) \in L = \{ 1 , \ldots , R \}$ : Region where customer i is located at time t.

## Decision variable:

$x _ { i j t l ( i , t ) } .$ If mobile coupon j is decided to be sent to customer i who is at region l at time t, $x _ { i j t l ( i , t ) } = 1$ ; otherwise, $x _ { i j t l ( i , t ) } = 0$

## Parameters:

$p _ { i j t l ( i , t ) } \dot { . }$ Price that a store pays the advertiser when the advertiser sends mobile coupon j to customer i at region l at time t.

$c _ { i j t l ( i , t ) } .$ Cost that the advertiser pays a network service provider when the advertiser sends mobile coupon j to customer i at region l at time t.

$a _ { i t } .$ Remaining annoyance number of customer i at time t

$b _ { j t } \mathrm { : }$ Remaining budget of mobile coupon j at time t.

NI(t) represents the set of new customers who have arrived (or moved) to a region during period t, while EI(t) represents the set of existing customers who arrived (or moved) to a region before period t and stayed in the same region till the end of period t. Customers in both NI(t) and EI(t) are targeted to send mobile coupons. Sending coupons to customers in EI(t) represents postponed selections. Location information of customers becomes available at time t. Prices $p _ { i j t l ( i , t ) } ,$ costs $c _ { i j t l ( i , t ) } ,$ remaining budgets $b _ { j t }$ and remaining annoyance numbers $a _ { i t }$ are also revealed at time t. The advertiser solves the following problem at every t.

The Basic Model:

$$
M a x \sum_ {i \in E I (t) \cup N I (t), j \in J} \bigl (p _ {i j t l (i, t)} - c _ {i j t l (i, t)} \bigr) x _ {i j t l (i, t)}\tag{BM-1}
$$

s.t.

$$
\sum_ {j \in J, t \in T} x _ {i j t l (i, t)} \leq a _ {i t} \forall i \in E I (t) \cup N I (t)\tag{BM-2}
$$

$$
\sum_ {i \in E I (t) \cup N I (t), t \in T} p _ {i j t l (i, t)} x _ {i j t l (i, t)} \leq b _ {j t} \forall j \in J\tag{BM-3}
$$

$$
x _ {i j t l (i, t)} \in \{0, 1 \} \forall i \in E I (t) \cup N I (t), \forall j \in J\tag{BM-4}
$$

The above MCDP does not belong to any traditional online MKPs. We refer to this new problem category as the postponable online MKP.

Given that LBA is still evolving, with different versions of LBAs in practice and development [2], we follow prior related studies and use flexible assumptions rather than restrictive ones in order to maximize the generalizability of the proposed model [5, 6, 18]. However, our model and solution approach proposed in §5 can also apply to LBAs with various different assumptions. For example, the vary by customer, coupon, region, and time. In some LBAs, this assumption may not be necessary. A coupon may have the same price for a group of similar customers (i.e., customer segments) and/or a network service provider may charge the same cost to send a coupon regardless of time, region, coupon, and/or customer. Also, there are different price structures used in current LBA. The most representative ones include pay-per-impression (PPM, or called cost-perimpression), pay-per-click (PPC, or called cost-per-click), and pay-per-action (PPA, or called cost-peraction)[46]. We propose a general model which can be applicable to any price structure following prior related similar studies in LBA [5, 6, 18]. Also, in some LBAs, the prices may be influenced by the outcomes of prior mobile coupons delivery decisions. Stores (or the advertiser) may change the coupon prices dynamically based on ongoing advertisement performance. Our model and solution approach are also applicable to this endogenous/dynamic price case. In fact, the proposed model and solution approach do not assume any specific functional forms for the parameters.

# ACCEPTED MANUSCRIPT

## 5. Algorithm design for MCDP

We discuss three mechanisms to design the single threshold-type algorithm for MCDP. They are selection (§5.1.1), weight (§5.1.2), and the sequence of decision (§5.1.3). 10 different combinations of design options (§5.2) are proposed.

## 5.1. Design mechanisms

## 5.1.1. Selection mechanism

For this mechanism, we first consider an option that implements postponable selection. In this option, a customer, who was considered to send a mobile coupon but not selected before, may be reconsidered to send the coupon again. We call this selection option semi-online. In the literature, semi-online is used to refer to any variant online model which has some additional information compared to pure online models [47]. In order to evaluate the performance of postponable selection, we consider a pure online selection option which only sends mobile coupons to customers who newly arrive or move to a region during the focal period, following the convention of traditional online algorithm literature [10, 43]. At time t, the semi-online option sends mobile coupons to customer , while the online option sends coupons to customer $i \in N I ( t )$

## 5.1.2. Weight mechanism

In single constraint online knapsack problems, one of the most widely used criteria to determine whether an item should be selected and packed into a knapsack is the item’s efficiency [10, 38]. Consider the following single constraint online knapsack problem: $\begin{array} { r } { \sum _ { m } v _ { m t } x _ { m t } \ s . t . \sum _ { m } k _ { m t } x _ { m t } \leq d ( t ) } \end{array}$ , where $x _ { m t }$ represents decision variables. The efficiency of item m at time t is defined as $e _ { m t } = v _ { m t } / k _ { m t }$ . This represents the marginal increase of the objective value that can be earned by spending one unit of resource (related to the single constraint) for item m. The most common way to solve a single constraint online knapsack problem is to use a threshold type online algorithm: if $e _ { m t } \geq \mathrm { a }$ threshold value, item m is selected; otherwise, item m is rejected [10, 38, 40, 48]. When it comes to online MKPs, the efficiency computation becomes more complicated due to multiple constraints. Consider the following online MKP: Max $\begin{array} { r } { \sum _ { m } v _ { m t } x _ { m t } s . t . \sum _ { j } k _ { n m t } x _ { m t } \le d ( t ) _ { n } } \end{array}$ for all n. Now the efficiency of item m is not a single value

Note: We use the notations of the following online MKP: $\begin{array} { r } { \sum _ { m } v _ { m t } x _ { m t } \ s . t . \sum _ { j } k _ { n m t } x _ { m t } \leq d ( t ) _ { m } } \end{array}$ for all n.

but a vector consisting of multiple ratios, $v _ { m t } / k _ { n m t }$ for all n. Each ratio represents the marginal increase of the objective value that can be earned by spending one unit of resource related to each constraint for a given item. Adopting ideas from prior studies on offline MKPs [12, 49], we use weights to address the multiple efficiency ratios for an item: the efficiency of item m at time t is defined as a single, weighted value $\begin{array} { r } { e _ { m t } = \sum _ { n } \omega _ { n t } v _ { m t } / k _ { n m t } } \end{array}$ , where $\omega _ { n t }$ is the weight for $v _ { m t } / k _ { n m t }$ at time t. Then, the same style of single threshold-type algorithm can be used for the online MKP, including the postponable MKP. We refer to how to define the weights as the weight mechanism.

Table 1. Weight options

<table><tr><td>Option</td><td>Description</td></tr><tr><td>EW (Equal Weight)</td><td>All constraints have the same weight:  $w_{nt} = 1/N$ , where N is the number of constraints.</td></tr><tr><td>WC(Weight by Remaining Capacity)</td><td>The weights of constraints are determined according to the relative sizes of remaining capacities:  $w_{nt} = d(t)_n / \sum_n d(t)_n$ , where  $d(t)_n$  is the remaining capacity of constraint n at time t.</td></tr><tr><td>WCT(Weight by Remaining Capacity within Type)</td><td>The weights of constraints are determined according to the relative sizes of remaining capacities within the same type:  $w_{nt} = d(t)_n / (Z \times \sum_{n \in N(z)} d(t)_n)$ , where Z is the number of constraint types, z ∈ {1,2,...,Z} represents a type, and N(z) represents the set of constraints that belong to type z.</td></tr><tr><td>RWC(Reverse WC)</td><td>The weights of constraints are determined according to the relative sizes of the reverse of remaining capacities:  $w_{nt} = (1/d(t)_n) / \sum_n (1/d(t)_n)$ .</td></tr><tr><td>RWCT(Reverse WCT)</td><td>The weights of constraints are determined according to the relative sizes of the reverse of remaining capacities within the same type: $w_{nt} = (1/d(t)_n) / (Z \times \sum_{n \in N(z)} (1/d(t)_n))$ .</td></tr></table>

Although there could be other ways to define the options for the weight mechanism, we propose the five basic options represented in Table 1. Each option varies depending on how it utilizes the information about the type of constraint and the remaining capacity of resource. Equal Weight (EW) option does not differentiate the type of constraint or the remaining capacity of resource. The intuition behind EW is that every resource (represented by each constraint of MKP) should be assumed to have the same level of importance given that future incoming items are unknown. Weight by Remaining Capacity (WC) and Reverse WC (RWC) options take the remaining capacities of resources into consideration. WC puts more weight on a resource with greater remaining capacity, while RWC puts more weight on a resource with smaller remaining capacity. The motivation of WC is to increase the chance to fill the

# ACCEPTED MANUSCRIPT

knapsack as much as possible by preventing certain resources from being consumed too quickly. On the other hand, the incentive behind RWC is to maximize the marginal returns of scarce resources by putting more value on their efficiencies. Although they look contradictory, both WC and RWC are reasonable strategies to maximize the objective value of MKP. The basic model of MCDP has two types of constraints: budget and annoyance. Different types of constraints usually have different structures and may differentially affect the solution of MKP. Weight by Remaining Capacity within Type (WCT) and Reverse WCT (RWCT) options are based on WC and RWC, respectively, but also consider the differences among the types of constraints. Weights are based on the remaining capacities but only among constraints of the same type. Given that there is no predefined way to judge the relative importance among different constraint types, we assume the sums of weights within each type to be the same across various types and the sum of all weights should always be 1 in all weight options. Since t e basic model of MCDP has two types of constraints, the sum of weights within each type is ½ in WCT and RWCT.

## 5.1.3. Sequence of decisions mechanism

In MCDP, the decision maker (i.e., advertiser) may make selection decisions for multiple items at the same time. Since the remaining capacities of resources are changed by selecting an item, the sequence of items affects the solution of the online MKP. The sequence of selection mechanism defines an order in which items are considered for selection One of the most reasonable ways is to use the efficiency of items defined in §5.1.2: The advertiser makes a binary selection decision for an item (i.e., send or not the mobile coupon to the customer) of which efficiency is larger than that of any other items of which selection decisions need to be made at the same time. The advertiser repeats this binary decision until there are no remaining items to consider. If there are ties in efficiency among multiple items, we use simple tie-breaking rules, which randomly determines a sequence among them.

Another important mechanism for threshold-type online algorithms is how to determine a good threshold value. We discuss the impact of different threshold values on the effectiveness of algorithms by conducting extensive experiments. The results are explained in §6.3.1.

# ACCEPTED MANUSCRIPT

## 5.2. Proposed algorithm

We test five options (EW, WC, WCT, RWC, and RWCT) for the weight mechanism and two options (online and semi-online) for the selection mechanism. We use one option (efficiency) for the sequence of decisions. Therefore, we have 10 unique versions of the single threshold-type algorithm for MCDP. Each version is represented by the option names in the two mechanisms, Weight-Selection: EW-online, WConline, WCT-online, RWC-online, RWCT-online, EW-semi, WC-semi, WCT-semi, RWC-semi, and RWCTsemi. For example, EW-online represents the version of algorithm that uses online as the selection mechanism and EW as the weight mechanism. From this point, we will simply refer to each version of the single threshold-type algorithm as an algorithm.

A formal description of the proposed single threshold-type algorithm is presented below. First is information for notation: An item available to be selected at time t is denoted by $( i , j , l ( i , t ) )$ , where i represents a customer, j represents a mobile coupon, $l ( i , t )$ represents a region where customer i is located at time t. Selecting item $( i , j , l ( i , t ) )$ means sending mobile coupon j to customer i at region l at time t. M represents the set of all available items to be considered for selection. Q represents a priority queue which stores items in a descending order of item’s efficiency. At every time t, single threshold-type algorithm Weight-Selection (z, t) is called to make selection decisions (i.e., mobile coupons delivery decisions). A threshold value, denoted by z, is given to the algorithm.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Single threshold-type algorithm Weight-Selection (z, t)

Step 0. (initialization) If Selection is “online”, set  $I(t) = NI(t)$ ; otherwise, set  $I(t) = EI(t) \cup NI(t)$ .

Set  $M = \left\{(i,j,l(i,t)) | i \in I(t), j \in J\right\}$ .

Step 1. Empty priority queue Q. For every item  $(i,j,l(i,t)) \in M$ , compute the efficiency according to Weight and store the item in Q.

Step 2. If Q is empty, exit; otherwise, retrieve an item  $(i,j,l(i,t))$  from Q and remove the item from M.

Step 3. If the retrieved item  $(i,j,l(i,t))$  is feasible and its efficiency  $\geq z$ , select the item and go to Step 2; else if the retrieved item  $(i,j,l(i,t))$  is not feasible but its efficiency  $\geq z$ , do not select item and go to Step 2; else, exit.
</div>

Complexity analysis: It is known to take O(log n) time to add or delete an item in a priority queue, where n is the number of items [50]. The proposed algorithm adds and deletes items in a priority queue in Step 1 and Step 2, respectively, and performs a comparison operation in Step 3. Hence, the

algorithm has O(n log n) computational complexity, where n=CA, C is the number of customers in the target area, and A is the number of mobile coupons. The computational resources required for the proposed algorithm are not hugely affected by the problem size. This implies that the algorithm scales well to be practically useful.

## 6. Computational experiments

## 6.1. Problem parameter settings

Table 2 shows the problem parameters and their values used in our experiments. We use a total of 4,424 problem instances for the experiments.

Table 2. Problem parameters

<table><tr><td>Parameter name</td><td>Number of values</td><td>Values</td></tr><tr><td>Number of customers (C)</td><td>3 values</td><td>50; 100; 200</td></tr><tr><td>Number of regions (R)</td><td>2 values</td><td>1; 5</td></tr><tr><td>Number of periods (P)</td><td>3 values</td><td>2; 4; 9</td></tr><tr><td>Max price</td><td>3 values</td><td>5; 30; 100</td></tr><tr><td>Max annoyance</td><td>3 values</td><td>1; 2; 6</td></tr><tr><td>Number of mobile coupons (A)</td><td>3 values</td><td>1; 10; 20</td></tr></table>

The customer actions (i.e., arrive, move, and leave) and customer locations are randomly generated according to Exponential and uniform discrete distributions. Prices vary by customer, mobile coupon, region, and period. They are randomly generated from a uniform distribution, U[2, max price]. Costs also vary by customer, mobile coupon, region, and period. They are randomly generated from a uniform distribution, U[1,corresponding price] so that a cost is always smaller than the corresponding price. Annoyance numbers vary by customer. They are randomly generated from a uniform distribution, U[1, max annoyance]. In order to avoid trivial solutions, we let the capacity of budget constraints be randomly generated satisfying the following rules [10, 14]: 1) every cost of sending a mobile coupon is smaller than the half of the initial budget capacity of the mobile coupon (i.e., $p _ { i j t l ( i , t ) } \leq b _ { j 1 } / 2$ , ∀i ∈ ) and 2) the total cost to send a given mobile coupon in all possible cases is greater than the initial budget of the mobile coupon (i.e., $\sum _ { i \in I , t \in T } p _ { i j t l ( i , t ) } > b _ { j 1 } , \forall j \in J )$

## 6.2. Performance of the algorithms

The competitive ratio has been widely used to evaluate the performance of online algorithms [43]. We follow this convention to evaluate the performance of our proposed algorithms. The competitive ratio of an algorithm is defined as the ratio of the algorithm’s objective value to the corresponding offline model’s optimal objective value.

In order to compute the competitive ratio, we optimally solve the offline version of problem instances and get the objective values. The offline optimal objective value represents the profit the advertiser can produce if and only if the advertiser knows how all customers would move in advance. The offline optimal objective value is an unrealistic but theoretical upper bound for MCDP because it is hardly obtainable in a real online MCDP setting. Next, we solve each of the problem instances using each of the 10 algorithm options by using each algorithm with 200 different threshold values, each time computing the competitive ratio.

Table 3. Average competitive ratio of the algorithms

<table><tr><td>FCFS</td><td>Weight options</td><td>Online</td><td>Gap: Online - FCFS</td><td>Semi</td><td>Gap: Semi - Online</td></tr><tr><td rowspan="6">32.30%</td><td>EW</td><td>81.15%</td><td>48.85%</td><td>85.52%</td><td>4.38%</td></tr><tr><td>WC</td><td>83.18%</td><td>50.88%</td><td>87.08%</td><td>3.83%</td></tr><tr><td>WCT</td><td>82.94%</td><td>50.64%</td><td>87.37%</td><td>4.47%</td></tr><tr><td>RWC</td><td>65.97%</td><td>33.67%</td><td>69.58%</td><td>3.62%</td></tr><tr><td>RWCT</td><td>78.21%</td><td>45.91%</td><td>83.82%</td><td>5.61%</td></tr><tr><td>Average</td><td>78.29%</td><td>45.99%</td><td>82.67%</td><td>4.38%</td></tr></table>

Note: Competitive ratio = performance of online algorithm / performance of optimal offline algorithm. For example, the Online (or Semi) column represents the ratios of the objective values of online (or semi-online) algorithms to the optimal offline objective values. A larger value, close to 100%, means a better performance.

Since the competitive ratio may be influenced by the intrinsic difference between online and offline settings, we also compare our proposed algorithms with a potential alternative online algorithm: the First-Come-First-Serve (FCFS) algorithm. We choose the FCFS algorithm because it is widely used in practice due to its simplicity and there exists no well-known algorithm for online MKP in the literature. In our context, the FCFS algorithm works as follows: When a customer (or a group of customers) enters the target area or moves to a region, the FCFS algorithm sends mobile coupons to customers in a descending order of the profit (= price – cost) as long as it is feasible. We solve every problem instance using this FCFS algorithm and compute the competitive ratio. This average ratio is shown in the first column (FCFS) in Table 3.

# ACCEPTED MANUSCRIPT

In order to evaluate the performances of the proposed algorithms, we first analyzed the best competitive ratio among those obtained using 200 different threshold values for each pair of problem instance and algorithm. Then we averaged them across the problem instances for each algorithm, which is shown in the third (Online) and fifth (Semi) columns in Table 3. The fourth (Gap: Online – FCFS) and sixth (GAP: Semi – Online) columns show gaps between the FCFS algorithm and the algorithms using the online selection option (hereafter online algorithms) and the gap between the algorithms using the online selection option and those using the semi-online selection option (hereafter semi-online algorithms).

The results show that the proposed algorithms perform relatively well. The best average competitive ratio of the online algorithms is 78.29% (third column), and that of the semi-online algorithms—which implement the postponable selection—is 82.67% (fifth column). Our online algorithms are found to be much more effective than the FCFS algorithm. The average competitive ratio of the FCFS algorithm is 32.30% (first column). Our online algorithms improve the competitive ratio by 45.99% over the FCFS algorithm (fourth column) on average.

The results also show that the semi-online algorithms perform better than the online algorithms. Within the same weight option, the semi-online algorithms always perform better than the online algorithms, on average (pairwise t-test: EW-online vs. EW-semi: t=50.53, p<0.0001; WC-online vs. WCsemi: t=45.83, p<0.0001; WCT-online vs. WCT-semi: t=49.89, p<0.0001; RWC-online vs. RWC-semi: t=43.49, p<0.0001; RWCT-online vs. RWCT-semi: t=60.85, p<0.0001) Overall, the semi-online algorithms improve the competitive ratio by 4.38% over the online algorithms (sixth column). This result implies that postponable selection brings greater benefits to the advertiser and that the semi-online algorithms are more appropriate to solve MCDP than the pure online algorithms.

Among the five different weight options, WCT (85.16%) and WC (85.13%) options perform better than the other options on average. After these, EW (83.34%) is better than RWCT (81.02%), and RWCT is better than RWC (67.78%) (WCT vs. WC: t=0.48, p=ns; WC vs. EW: t=10.80, p<0.0001; EW vs. RWCT: t=12.19, p<0.0001; RWCT vs. RWC: t=60.84, p<0.0001).

# ACCEPTED MANUSCRIPT

WC and WCT put more weight on the efficiency ratio of a resource with greater remaining capacity, while RWC and RWCT put more weight on the efficiency ratio of a resource with smaller remaining capacity. Hence, our experimental results imply that putting more weight on a resource with greater remaining capacity produces better performance on average. This provides a managerial insight that the advertiser needs to prevent certain resources (i.e., budget, annoyance numbers) from being s related to relatively sufficient resources (e.g., coupons with more remaining budget, customers with more remaining annoyance limit). Both RWC and RWCT attempt to maximize the marginal returns of scarce resources by putting more value on their efficiencies. Our results indicate it is not a good strategy, possibly because if a resource is quickly consumed (e.g., a coupon budget is used up prematurely), the advertiser loses all potential opportunities related to the resource that could be available in the future (e.g., cannot send a coupon even if there are customers likely to use them), which may restrict the set of overall feasible choices and deteriorate delivery performance.

The semi-online option, which allows postponable selection, and the WCT option are found to be better than the other options in each design mechanism. The combination of these two options produces the best performance. Among the 10 proposed algorithms, WCT-semi (87.37%) performs better than any other algorithms, including the second-best one, WC-semi (87.08%) (WCT-semi vs. WC-semi: t=4.91, p<0.0001). The performance reported in Table 3 represents the average comparative ratios with a good threshold. Later, we show how threshold values impact the effectiveness of the proposed algorithms.

## 6.3. Sensitivity analyses

## 6.3.1. Threshold values

Because we use normalized weights to compute the efficiency of items, the possible threshold values that can be used for a given problem instance are bounded. In our experiments, we use [1/max price, max price/10] based on the results of our pilot tests. Then, we divide this range into 200 equal intervals and solve the same problem instance 200 times, using these 200 different threshold values with each algorithm.

![](/api/attachments/QNMXD9AN/fulltext/images/303533aeb29d62ce4dea4cec8ccab30f8544b4c7779615ba7ab0cc67cc7b4a2e.jpg)  
Fig. 2. Performance by threshold value (one problem instance)

Fig. 2 shows the objective values of one problem instance computed by two algorithms, EWonline and WC-semi, with the x-axis as the ordinal threshold values from 1 to 200. In the example of Fig. 2, the range of the actual threshold values is [1/30, 3], and the constant interval is (3-1/30) /200=0.033. As Fig. 2 shows, the best objective value and the corresponding threshold value that produce the best objective value are different between the two algorithms (EW-online: obj=2.946, threshold value=16; WC-semi: obj=2,845, threshold value=42). Also, the shapes of the wo graphs differ. EW-online has a steeper slope than WC-semi. This means that when we use EW-online, if we mistakenly choose a threshold value far from the best threshold value, then we will get a much worse objective value compared to when we use WC-semi. In other words, EW-online is more sensitive to the threshold value than WC-semi. Although EW-online has a greater best objective value (2,946) than WC-semi (2.845), which can be earned if the best threshold value is known, the average performance (which is represented by the area under the graph over 200 threshold values) of WC-semi is greater than that of EW-online. This implies that if the advertiser implements a randomized threshold algorithm that randomly selects a threshold value from the range between 1 and 200, WC-semi would perform better than EW-online on average.

![](/api/attachments/QNMXD9AN/fulltext/images/29ecdcf25e905f6cb078174bcc73690d8fbdfebfae17d24e7ead9fa9ef4a2f95.jpg)

(a) EW-semi and EW-online  
![](/api/attachments/QNMXD9AN/fulltext/images/8b3bea67b1d098bd69e2eafae654081cf50cb15badd68e70b90e0125f7acc26a.jpg)

(b) WCT-semi and WCT-online  
![](/api/attachments/QNMXD9AN/fulltext/images/509388022333e79c600a6d444a3e3d2823cdfe8c920b342499f95a2692c68b97.jpg)  
(c) semi-online algorithms  
Fig. 3. Performance by threshold value

Fig. 3 shows the impact of threshold values on the performance of the algorithms on average. The range of threshold values varies by the problem parameters, especially the max price. In order to compare different problem instances that have different ranges of threshold values, we need to normalize the range of threshold value. Similarly, the magnitude of objective value differs by the problem parameters, too, and the best objective value computed by a given algorithm also varies by problem instance. In order to compare the impact of threshold value on the objective values of algorithms, we use the following normalized performance: The normalized performance of an algorithm with a given threshold value for a given problem instance is defined as the ratio of the objective value computed by the algorithm on the problem instance using the threshold value to the best objective value among the objective values

computed by the same algorithm on the same problem instance using 200 different threshold values. The y-axis in Fig. 3 represents this normalized performance. Each graph represents the normalized performance of an algorithm, averaged across all problem instances, along with ordinal threshold values.

Fig. 3(a) shows the graphs of EW-semi and EW-online, with both graphs maximized at approximately the same threshold. After the maximum normalized performance, both have steep downward slopes and almost identical curvatures. Fig. 3(b) shows the graphs of WCT-semi and WCTonline. Similar to the case of EW-semi and EW-online, both graphs are maximized at approximately the same threshold and have similar curvatures after that point. These results provide some interesting findings. In both Fig. 3(a) and 3(b), the semi-online algorithms show smoother upward curvatures and have higher normalized performances than the online algorithms up to the threshold value where both have the maximized performance. Also, it is shown that the performance of semi-online algorithms is better than, or at least the same as, the online algorithms at almost every threshold value. Although we do not show them due to limited space, the online and semi-online algorithms using other weight options show the same patterns. These findings imply that given a weight option, the semi-online algorithm is likely to perform better than the online algorithm at any given threshold on average. The results also indicate that the semi-online algorithm is less sensitive to the threshold value than the online algorithm. In other words, if a wrong threshold value is mistakenly chosen, the semi-online algorithm is less negatively affected than the online algorithm, particularly when the chosen value is much smaller than what it needs to be. Lastly, we observe that the area under the graph of the semi-online algorithm is greater than that of the online algorithm. This implies that when a randomized threshold algorithm is implemented, the semionline algorithm performs better than the online algorithm.

This could be due to the fact that the feasible set of items (i.e., sending a coupon to a customer) a semi-online algorithm can select always includes the feasible set of items a corresponding online algorithm can select. Therefore, it seems intuitive that a semi-online algorithm performs better than or at least as the same as a corresponding online algorithm, on average. Postponable selection allows an item that was not selected before because its efficiency was below a chosen threshold, to be selected once its efficiency becomes above the threshold. Hence, if a chosen threshold is smaller than the ideal threshold value that produces the optimal profit, the semi-online algorithm may select items with efficiencies that are greater and closer to the ideal threshold than the online algorithm. On the other hand, if a chosen threshold is bigger than the ideal threshold value, the semi-online algorithm may select items with efficiencies that are greater but further from the ideal threshold value, which may diminish the overall benefit of postponable selection. This may explain why the performance difference between the semionline and the online algorithms becomes more apparent when the chosen threshold value is smaller than the ideal threshold value.

The impact of threshold value varies by weight option, too. It is easy to notice that the graphs in Fig. 3(a) and 3(b) do not look like each other. The graphs of WCT-semi and WCT-online in Fig. 3(b) have smoother upward and downward slopes than the graphs of EW-semi and EW-online in Fig. 3(a). Fig. 3(c) shows the graphs of the semi-online algorithms using different weight options. Since the online and semionline algorithms using the same weight option produce similar graphs and the semi-online algorithms outperform the online algorithms, we only display the graphs of the semi-online algorithms in Fig. 3(c) where all five curvatures are different. Among the five weight options, WC and WCT options have smoother slopes than the others. If there is not sufficient information on what value should be used as a threshold, WC and WCT options would be better than the others because they are least sensitive to the threshold value. In other words, WC and WCT options are less negatively affected than the other options by a mistakenly chosen threshold. Among the five weight options, WC and WCT options have larger areas under graphs than the others. This implies that in a randomized algorithm setting, WC and WCT options would perform better than any other option on average. In fact, these two options always dominate the others in any sub-range (e.g., from 10 to 100 or 50 to 150), which means they would outperform the others (on average) in any randomized threshold algorithm settings using any sub-range.

The reduced sensitivity of WC and WCT to the chosen threshold as compared to the other options seems attributable to how these two weight options balance the remaining capacity of resources. Both options try to prevent any resources from being consumed too quickly and becoming unavailable. Once a resource becomes unavailable (e.g., the budget of a coupons is consumed), any future item related to the resource (e.g., new customer who is willing to use the coupon) becomes infeasible to select, which restricts the overall feasible set of decisions, which in turn negatively affects performance. WC and WCT seem to avoid this problem relatively well by keeping all resources available longer than the other options, even when the chosen threshold value is far from the ideal value.

As shown in Fig. 3(c), there is no single ordinal threshold value that performs best in every algorithm. In addition, the best threshold value varies by the parameters. Fig. 4 shows how the best threshold value is affected by key problem parameters.

![](/api/attachments/QNMXD9AN/fulltext/images/3b2aa0248dda504b63ec451787bc20f4fca927c3393847f00e926609955abda2.jpg)  
(a) customer

![](/api/attachments/QNMXD9AN/fulltext/images/058e0dd1833ae4b684e4ed2540b82099c501c143b9c378db9eff9ea9d5d5f437.jpg)  
(b) max price

![](/api/attachments/QNMXD9AN/fulltext/images/cfd110b27482696648f4aea5fbc7b423312013ecb49925f0842b3df6cc8e0e88.jpg)  
(c) max annoyance

![](/api/attachments/QNMXD9AN/fulltext/images/fb922453d771eb8e10099e479ac09930dbd4cced0cbded955c68d980d4416dc2.jpg)  
(d) period  
Fig. 4. Best threshold value by problem parameter

The y-axis of Fig. 4(a)-(d) represents the best ordinal threshold value. Consistent with the findings reported in Fig. 3, different algorithms have different best threshold values, while the online and

# ACCEPTED MANUSCRIPT

semi-online algorithms using the same weight option have similar best threshold values. Fig. 4(a) shows that the best threshold value for EW and RWCT algorithms decrease as the number of customers increases, i.e. the advertiser would need to decrease the threshold value as the customer size increases when using these algorithms. WC and WCT algorithms do not change significantly, which implies that a good threshold value for WC and WCT algorithms does not need to be adjusted due to a change in the number of customers. Fig. 4(b) and 4(c) show that the best threshold value of every algorithm decreases as the max price and max annoyance increase. This indicates that as the budget or annoyance decreases, the threshold value of an algorithm needs to be increased so that selection criteria become stricter. This is intuitive because decreasing budget and annoyance means the resources of the knapsack are becoming scarcer. Fig. 4(d) shows the impact of periods on the best threshold value, illustrating that the best threshold value of each algorithm increases with respect to the number of periods, implying the threshold value needs to be decreased as the number of remaining periods decreases. This is also intuitive since selection criteria need to become more generous to fill the remaining space of the knapsack as the end of the decision horizon comes closer.

The sensitivity analysis on the best threshold value provides important insights into the design of an adaptive-threshold algorithm that automatically adjusts the threshold value as the problem state changes. For instance, the algorithm should increase the threshold as the campaign budget is gradually used up, while the algorithm should decrease the threshold as the decision horizon is closer to the end.

## 6.3.2. Problem instances

To understand the impact of problem instances, we evaluate the performance of the proposed algorithms on different problem instances randomly generated with the same problem parameters. For simplicity, we omit the results of RWC-online and RWC-semi because their performances are relatively low (67.78%) compared to the others.

Fig. 5 shows the performance of the six algorithms (WCT-semi, WCT-online, EW-online, EWsemi, WC-semi, and WC-online) for the 10 randomly generated problem instances with the same problem parameters. As being consistent with our overall results, WCT-semi is the best algorithm for these 10

problem instances in terms of average performance (81.45%). However, as Fig. 5 shows, WCT-semi does not outperform the others in every instance. While WCT-semi most frequently performs best $( 3 ^ { \mathrm { r d } } , 4 ^ { \mathrm { t h } } , 8 ^ { \mathrm { t h } }$ and $9 ^ { \mathrm { t h } }$ instances), in the $1 ^ { \mathrm { s t } }$ and $2 ^ { \mathrm { n d } }$ instances, EW-semi performs best and WC-semi outperforms in the $1 0 ^ { \mathrm { t h } }$ instance. Also aligned with our overall results, the average performance of the three semi-online algorithms (80.67%) is greater than that of the three online algorithms (78.94%); however, in the $6 ^ { \mathrm { t h } }$ instance the online algorithm, WCT-online, performs better than any semi-online algorithm. These results imply that although some algorithms perform better than others in terms of average, there is no superior algorithm that always outperforms the others in every case because they are all heuristics which do not guarantee the optimality and their performances are affected by problem instance.

![](/api/attachments/QNMXD9AN/fulltext/images/e08d67eb77c5518ca223a7ce9f35437976b141d5b0960f5541694fe03aacc4f2.jpg)  
Note: 10 problem instances with customer=50, mobile coupon=10, region=5, period=3, max price=30, and max annoyance=2  
Fig. 5. Performances of the algorithms by problem instance

The results of our computational experiments provide rich insights into designing algorithms for MCDP. To summarize: 1) Between the semi-online and online options, the semi-online algorithms perform better than the online algorithms on average. 2) Among the five weight options, WCT and WC are better than the others on average. 3) WCT-semi and WC-semi, the combinations of the best selection and the best weight options, perform better than the other algorithms on average. 4) However, there is no single algorithm that always outperforms the other algorithms in every problem instance. Algorithms may be implemented in a deterministic algorithm setting where a good threshold is known or a randomized algorithm setting where each time a threshold is randomly chosen from a distribution. Our findings provide useful guidelines for both settings.

# ACCEPTED MANUSCRIPT

## 7. Concluding remarks

We define MCDP as when mobile coupons delivery decisions are made sequentially as customers’ location information becomes gradually revealed over time. MCDP provides unique requirements, particularly postponable selection, which has not been considered in traditional online MKPs. Therefore, we formulate MCDP as a new problem category, referred to as the postponable online MKP where mobile coupons delivery decisions may be postponed and revisited. We propose several algorithms to solve MCDP and analyze their performances through extensive computational experiments and sensitivity analyses. The proposed algorithms perform relatively well in a wide range of problem parameters (78% of the offline optimal performance on the average). The semi-online algorithms that implement postponable selection generally perform better than the pure online algorithms (by 4% on the average). Among the five different options for the weight mechanism to compute the efficiency of items, WCT and WC perform better than the other options.

As a major contribution of this study, the postponable online MKP has significant potential uses in other online decision-making problems. The proposed algorithms and computational results provide insights into the solution approach not only for MCDP but also for the postponable online MKP. This study also gives practical implications to LBA practitioners.

This study may be improved in a few dimensions. First, we solve the problem of a single advertiser. The assumption of a single advertiser is not uncommon in the literature on related areas, including search engine advertisement [51]. However, in reality it may be possible to have more than one advertiser competing for the same customer in the same target area. Considering multiple advertisers and their competition is an interesting research topic and a potential extension of this study, but it would need different analytical angles. Second, it is accepted to be a challenge to theoretically analyze the performance of an algorithm for online MKP. An alternative method is computational experiments, which we rely on in this study. Although our experimental results provide rich insights, an analytical model to support our results would increase the generalizability of our findings. Third, this study proposes simple, easily implementable algorithms using a constant threshold. Developing an algorithm using a non-

constant, adoptive, self-learning threshold is a potential extension of this study. Similarly, we propose a simple, fundamental model of MCDP to emphasize its unique setting, postponable selection. Extending our model with sophisticated elements, such as predicting customer location trajectories and integrating automatic, real-time feedback of customer responses or actions on the delivered coupons, is another area for future research. Finally, this study uses simulated data to test the performances of our algorithms. A field test using real data may provide additional practical insights.

## References

[1] Statista, Number of mobile phone users worldwide from 2015 to 2020 (in billions), Available at https://www.statista.com/statistics/274774/forecast-of-mobile-phone-users-worldwide, 2018.

[2] A. Ghose, Tap: Unlocking the Mobile Economy, MIT Press, Cambridge, MA, 2017.

[3] K. Li, T.C. Du, Building a targeted mobile advertising system for location-based services, Decision Support Systems, 54 (2012) 1-8.

[4] D.-Y. Choi, Personalized local internet in the location-based mobile web search, Decision Support Systems, 43 (2007) 31-45.

[5] A.K. Tripathi, S.K. Nair, Narrowcasting of wireless advertising in malls, European Journal of Operational Research, 182 (2007) 1023-1038.

[6] B. De Reyck, Z. Degraeve, Broadcast scheduling for mobile advertising, Operations Research, 51 (2003) 509-517.

[7] N.M.-J. Achadinha, L. Jama, P. Nel, The drivers of consumers’ intention to redeem a push mobile coupon, Behaviour & Information Technology, 33 (2014) 1306-1316.

[8] A. Dickinger, M. Kleijnen, Coupons going wireless: Determinants of consumer intentions to redeem mobile coupons, Journal of interactive marketing, 22 (2008) 23-39.

[9] H. Kellerer, U. Pferschy, D. Pisinger, Knapsack Problems, Springer, Berlin, 2004.

[10] D. Chakrabarty, Y. Zhou, R. Lukose, Budget Constrained Bidding in Keyword Auctions and Online Knapsack Problems, WWW, Banff, Canada, 2007.

[11] Y. Zhou, D. Chakrabarty, R. Lukose, Budget constrained bidding in keyword auctions and online knapsack problems, International Workshop on Internet and Network Economics, Springer, 2008, pp. 566-576.

[12] Y. Akçay, H. Li, S.H. Xu, Greedy algorithm for the general multidimensional knapsack problem, Annals of Operations Research, 150 (2007) 17-29.

[13] M.E. Dyer, A.M. Frieze, Probabilistic analysis of the multidimensional knapsack-problem, Mathematics of Operations Research, 14 (1989) 162-176.

[14] A. Freville, The multidimensional 0-1 knapsack problem: An overview, European Journal of Operational Research, 155 (2004) 1-21.

[15] M.J. Magazine, M.-S. Chern, A note on approximation schemes for multidimensional knapsack problems, Mathematics of Operations Research, 9 (1984) 244-247.

[16] R. Unni, R. Harmon, Perceived effectiveness of push vs. pull mobile location based advertising,

[17] E. Gratton, M-commerce: The notion of consumer consent in receiving location-based advertising, Canadian Journal of Law and Technology, 1 (2002) 59-77.

[18] A.K. Tripathi, S.K. Nair, Mobile advertising in capacitated wireless networks, IEEE Transactions on Knowledge and Data Engineering, 18 (2006) 1284-1296.

[19] Forrester Research, Telcos Should Look To Location-Based Services For Growth, Forrester Research, 2007.

[20] D. Grewal, Y. Bart, M. Spann, P.P. Zubcsek, Mobile advertising: a framework and research agenda, Journal of Interactive Marketing, 34 (2016) 3-14.

[21] P. Haghirian, M. Madlberger, A. Tanuskova, Increasing advertising value of mobile marketing – An empirical study of antecedents, 38th Hawaii International Conference on System Sciences, Hawaii, 2005.

[22] S.Y. Ho, S.H. Kwok, The attraction of personalized service for users in mobile commerce: an empirical study, ACM SIGecom Exchanges, 3 (2002) 10-18.

[23] R.H. Ducoffe, Advertising value and advertising on the web, Journal of Advertising Research, 36 (1996) 21-35.

[24] H. Xu, X.R. Luo, J.M. Carroll, M.B. Rosson, The personalization privacy paradox: An exploratory study of decision making process for location-aware marketing, Decision Support Systems, 51 (2011) 42-

[25] S. Dhar, U. Varshney, Challenges and business models for mobile location-based services and advertising, Communications of the ACM, 54 (2011) 121-128.

[26] C. Kumar, J.B. Norris, Y. Sun, Location and time do matter: A long tail study of website requests, Decision Support Systems, 47 (2009) 500-507.

[27] F. Provost, D. Martens, A. Murray, Finding similar mobile consumers with a privacy-friendly geosocial design, Information Systems Research, 26 (2015) 243-265.

[28] H. Xu, L.-B. Oh, H.-H. Teo, Perceived effectiveness of text vs. multimedia location-based advertising messaging, International Journal of Mobile Communications, 7 (2009) 154-177.

[29] H. Xu, H.-H. Teo, B.C. Tan, R. Agarwal, The role of push-pull technology in privacy calculus: the case of location-based services, Journal of Management Information Systems, 26 (2009) 135-174.

[30] T. Peng, Q. Liu, D. Meng, G. Wang, Collaborative trajectory privacy preserving scheme in locationbased services, Information Sciences, 387 (2017) 165-179.

[31] G.C. Bruner, A. Kumar, Attitude toward location-based advertising, Journal of Interactive Advertising, 7 (2007) 3-15.

[32] A. Ghose, B. Li, S. Liu, Mobile Targeting Using Customer Trajectory Patterns, Available at SSRN: https://ssrn.com/abstract=2962044 or http://dx.doi.org/10.2139/ssrn.2962044, 2018.

[33] W.B. Powell, Approximate Dynamic Programming: Solving the Curses of Dimensionality, Wiley-Interscience, Hoboken, NJ, 2007.

[34] B. Gavish, H. Pirkul, Efficient algorithms for solving multiconstraint zero-one knapsack problems to optimality, Mathematical Programming, 31 (1985) 78-105.

[35] H.M. Weingartner, D.N. Ness, Methods for the solution of the multidimensional 0/1 knapsack problem, Operations Research, 15 (1967) 83-103.

[36] J. Puchinger, G.R. Raidl, U. Pferschy, The multidimensional knapsack problem: Structure and algorithms, INFORMS Journal on Computing, 22 (2010) 250-265.

[37] R. Mansini, M.G. Speranza, Coral: An exact algorithm for the multidimensional knapsack problem, INFORMS Journal on Computing, 24 (2012) 399-415.

[38] M. Babaioff, J.D. Hartline, R.D. Kleinberg, Selling banner ads: online algorithms with buyback, Workshop on Ad Auctions, Chicago, Illinois USA, 2008.

[39] K. Iwama, G. Zhang, Optimal resource augmentations for online knapsack, Approximation, Randomization, and Combinatorial Optimization: Algorithms and Techniques, 4627 (2007) 180-188.

[40] A. Marchettispaccamela, C. Vercellis, Stochastic online knapsack-problems, Mathematical Programming, 68 (1995) 73-104.

[41] K. Pak, R. Dekker, Cargo revenue management: Bid-prices for a 0-1 multi knapsack problem, ERIM Report Series Research in Management, DOI (2004).

[42] K. Talluri, G. Van Ryzin, An analysis of bid-price controls for network revenue management, Management Science, 44 (1998) 1577-1593.

[43] A. Borodin, R. El-Yaniv, Online Computation and Competitive Analysis, Cambridge University Press, Cambridge, UK, 2005.

[44] M. Meanti, A. Kan, L. Stougie, C. Vercellis, A probabilistic analysis of the multiknapsack value function, Mathematical Programming, 46 (1990) 237-247.

[45] S. Agrawal, Z. Wang, Y. Ye, A dynamic near-optimal algorithm for online linear programming, Operations Research, 62 (2014) 876-890.

[46] M. Mahdian, K. Tomak, Pay-per-action model for on-line advertising, International Journal of Electronic Commerce, 13 (2008) 113-128.

[47] H. Kellerer, V. Kotov, M.C. Speranza, Z. Tuza, Semi on-line algorithms for the partition problem, Operations Research Letters, 21 (1997) 235-242.

[48] G.S. Lueker, Average-case analysis of off-line and on-line Knapsack problems, Journal of Algorithms, 29 (1998) 277-305.

[49] A. Rinnooy Kan, L. Stougie, C. Vercellis, A class of generalized greedy algorithms for the multiknapsack problem, Discrete Applied Mathematics, 42 (1993) 279-290.

[50] D.W. Jones, An empirical comparison of priority-queue and event-set implementations, Communications of the ACM, 29 (1986) 300-311.

[51] J. Feng, Z.J.M. Shen, R.L. Zhan, Ranked items auctions and online advertisement, Production and Operations Management, 16 (2007) 510-522.

## Appendix: Acronyms and notations

A-Table 1. Acronyms

<table><tr><td>Acronym</td><td>Full description</td></tr><tr><td>LBA</td><td>Location Based Advertisement</td></tr><tr><td>MCDP</td><td>Mobile Coupons Delivery Problem.</td></tr><tr><td>MKP</td><td>Multi-constraint Knapsack Problem</td></tr><tr><td>FCFS</td><td>First-Come-First-Serve</td></tr><tr><td>EW</td><td>Equal Weight</td></tr><tr><td>WC</td><td>Weight by remaining Capacity</td></tr><tr><td>WCT</td><td>Weight by remaining Capacity within Type</td></tr><tr><td>RWC</td><td>Reverse WC</td></tr><tr><td>RWCT</td><td>Reverse WCT</td></tr></table>

A-Table 2. Main notations

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $i \in I = \{1, ..., C\}$ </td><td>Customer.</td></tr><tr><td> $j \in J = \{1, ..., A\}$ </td><td>Mobile coupon.</td></tr><tr><td> $t \in T = \{1, ..., P\}$ </td><td>Time period. The decision horizon consists of  $P$  time periods.</td></tr><tr><td> $l(i, t) \in L = \{1, ..., R\}$ </td><td>Region where customer  $i$  is located at time  $t$ .</td></tr><tr><td> $x_{ijtl(i,t)}$ </td><td>Decision variable. If mobile coupon  $j$  is decided to be sent to customer  $i$  who is at region  $l$  at time  $t$ ,  $x_{ijtl(i,t)} = 1$ ; otherwise,  $x_{ijtl(i,t)} = 0$ .</td></tr><tr><td> $p_{ijtl(i,t)}$ </td><td>Price that a store pays the advertiser when the advertiser sends mobile coupon  $j$  to customer  $i$  at region  $l$  at time  $t$ .</td></tr><tr><td> $c_{ijtl(i,t)}$ </td><td>Cost that the advertiser pays a network service provider when the advertiser sends mobile coupon  $j$  to customer  $i$  at region  $l$  at time  $t$ .</td></tr><tr><td> $a_{it}$ </td><td>Remaining annoyance numbers for customer  $i$  at time  $t$ .</td></tr><tr><td> $b_{jt}$ </td><td>Remaining budget for mobile coupon  $j$  at time  $t$ .</td></tr><tr><td> $NI(t)$ </td><td>New customers who has arrived (or moved) to a region during period  $t$ .</td></tr><tr><td> $EI(t)$ </td><td>Existing customers who had arrived (or moved) to a region before period  $t$  and stayed in the same region till the end of period  $t$ .</td></tr></table>

Keumseok Kang is an assistant professor at the College of Business, Florida International University. He received his Ph.D. in management from Purdue University. His research interests include organizational learning in software development, location-based advertisement, and service operations management. His research has appeared in Manufacturing & Service Operations Management and Information Systems Research.

Kemal Altinkemer is a Professor in MIS area at the Krannert Graduate School of Management at Purdue University. He has been a Guest Editor in Telecommunication Systems, Information Technology and Management and ECRA. He is an Associate Editor in five journals. His research interests are in computer networks, infrastructure development, distribution of priorities by using pricing as a tool, infrastructure for E-commerce and pricing of information goods, bidding with intelligent software agents, strategy from Brickandmortar to Clickandmortar business model. He has more than 50 publications in journals such as Operations Research, Operations Research Letters, Management Science, INFORMS Journal on Computing, MSOM, Transportation Science, EJOR, Computers and OR, Annals of Operations Research, and more than 50 articles in various conference proceedings.

Inkyoung Hur is an assistant professor in the Department of Information Systems and Cybersecurity at Nova Southeastern University. Her research focuses on patient-centered care, social media technology, patient engagement, knowledge sharing, data visualization, and business analytics in healthcare domain. Her research has appeared in Journal of Economic Behavior & Organization, International Journal of Human–Computer Interaction, and Human Factors and Ergonomics in Manufacturing and Service Industries.

## Research Highlights: Mobile Coupons Delivery Problem: Postponable Online Multidimensional Knapsack

 We study the mobile coupons delivery problem (MCDP) in a push-based location based advertisement where an advertiser proactively sends mobile coupons to prospective customers on behalf of stores based on the customers’ location and preferences.

 MCDP provides a new capability called postponable selection that enables an advertiser to better capitalize on the plethora of customer information provided by mobile phone users through network service providers.

As a major contribution of this study, the postponable online MKP has significant potential uses in other online decision-making problems. The proposed algorithms and computational results provide insights into the solution approach not only for MCDP but also for the postponable online MKP. This study also gives practical implications to LBA practitioners.

Our experimental results show that the proposed algorithm outperforms the First-Come-First-Serve heuristic by 46% and postponable selection additionally improves performance by 4% on average.
