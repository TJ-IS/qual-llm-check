---
otero_id: 10578
otero_key: "3ERT5YFT"
title: "Real option valuation on grid computing"
authors: "Juheng Zhang; Subhajyoti Bandyopadhyay; Selwyn Piramuthu"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.07.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Real option valuation on grid computing ☆

Juheng Zhang, Subhajyoti Bandyopadhyay, Selwyn Piramuthu ⁎

Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, Gainesville, FL 32611-7169, USA

## a r t i c l e i n f o

Article history: Received 6 August 2007 Received in revised form 19 June 2008 Accepted 3 July 2008 Available online 16 July 2008

Keywords: Grid computing Real option valuation

## a b s t r a c t

Grid computing essentially involves transparent access to distributed computing where computing resources are pooled and shared both within and among organizations. Grid computing is increasingly becoming a viable option for businesses looking for high-end computing requirements for relatively short periods of time. We analyze some economic decision criteria for a grid computing provider wishing to provide such a service to businesses. Given the large amount of uncertainty in prices and demand (which is demonstrated through Monte Carlo simulations) for such a service, a real options valuation technique is particularly suitable for such an exercise. We study the dynamics of grid computing from an economic perspective. Speci<sup>fi</sup>cally, we consider a monopolist scenario providing two kinds of service, one of which might preempt the other.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

The idea behind grid computing originated in the early 1990s as a means to share computational resources over a network similar to utilities such as gas, water, and electricity [15]. It is based on the principle of electrical power grids where resources are shared among members in a grid in a seamless fashion to provide consistent and transparent access to power regardless of source or destination location. The Internet is utilized to garner distributed computing resources that lay unused from the general population (e.g., SETI@home project for detecting intelligent life outside Earth, [22]) and use it to solve massive computing problems. Grid computing speci<sup>fi</sup>cally refers to a conceptual framework of a virtual organization where uncommonly deployed computational resources (e.g., CPU cycles, disk storage, data, software, peripherals) that are expensive and outside of a local administrative domain are made available [9,27]. Karl

Czajkowski, Ian Foster (sometimes called the “father of grid computing”), and Carl Kesselman developed the Globus Toolkit, which remains the de facto standard for building and maintaining grid solutions [14].

Although grid computing has been used mainly in the areas of scienti<sup>fi</sup>c computing, it is gradually <sup>fi</sup>nding use in the arena of business computing [19,20]. Bort [8] gives a typical example of when businesses might revert to using grid computing rather than have a traditional computing infrastructure — the human resources outsourcing company Hewitt Associates used to host a pension-calculating application on a mainframe for its 5.5 million customers. The application would see sudden spikes of activity whenever rumors of mergers and acquisitions circulated in any of Hewitt's client companies, as the potentially affected employees wanted to calculate their pension earnings. The application, which was otherwise separate from Hewitt's other computing operations, was an ideal candidate for grid computing – it was compute-intensive, had high variability in demand during very limited timeframes, and was scalable – and it was successfully transferred to a grid computing infrastructure by IBM using generic hardware from Intel running the Linux operating system.

Typical users of grid computing are developers, researchers, scientists, and businesses who require on-demand computing resources without massive investment in IT infrastructure. Grid computing involves both commercial as well as non-commercial (e.g., SETI@home) settings where the grid providers could be a single organization (e.g., Sun Grid) or a distributed set of organizations including the general public with shareable available resources. Sun Grid is an on-demand grid computing service operated by Sun Microsystems that provides access to computing resource over the Internet for an all-inclusive price of US\$1 per CPU-hour. The commercial offerings from a single provider have the advantage of complete control over its resources and their availability. These providers are thus able to provide quality of service (QoS) guarantees, which are hard to achieve in a non-commercial setting with computational resources from the general public.

A majority of grid computing applications involve largescale computational problems that necessitate use of multiple resources that are typically not found in a single physical organization. Brunett et al. describe an example of simulation where 13 parallel supercomputers comprising more than 1300 processors were utilized [9].

Although the concept of effectively utilizing resources is very attractive, its operationalization is complicated because of the presence of heterogeneous resources including operating systems, platforms, available memory, available processing power, data security and privacy issues, etc. in an architecture that is physically distributed in different locations, belonging to different administrative domains, and accessed over the network. Unlike power grids, where it is relatively easy to guarantee quality of service since loads at any part of the grid at any point in time can be estimated with reasonable accuracy, computing grids experience more uncertainty with respect to both demand and supply primarily due to the lack of structure inherent in such networks (interested readers might want to peruse [25] who considers the use of real options in demand-side electricity contracts). Grid computing relies on the simultaneous availability of multiple resources that are distributed across a network and fast reliable network connections among them.

A signi<sup>fi</sup>cant amount of the extant literature on grid computing is concerned with the problem of resource allocation on the grid [2,10,12,17,18,24,30]. Although resource allocation over a network has been extensively studied in other contexts, the presence of disparate resources that are required to work in concert within a grid computing framework increases the complexity of the problem. Jobs are assigned either through scavenging, where idle machines are identi<sup>fi</sup>ed and put to work, or through reservation in which jobs are matched and pre-assigned with the most appropriate systems in the grid for ef<sup>fi</sup>cient work<sup>fl</sup>ow.

Yet another set of literature on grid computing assumes resource allocation as a given and deal with economic issues, including pricing mechanisms (e.g., [1,28]). Characteristics de<sup>fi</sup>ning grid computing from an economic perspective include uncertain demand for resources, uncertainty in the quality of service associated with such demands and pricing issues across time periods. The set of characteristics, replete with uncertainties, naturally lends itself to consideration through real options analysis.

The term “real options” was coined by Professor Stewart Myers of the MIT Sloan School of Management, and it refers to the right (as opposed to an obligation) to make a business decision, which is typically an investment decision. Unlike a <sup>fi</sup>nancial option, a real option (e.g. the option to expand capacity of production in a factory) is not tradable. Real options enable decision makers to place a value on uncertainty that is inherent in a high-risk environment that is not adequately captured in traditional techniques like Net Present Value (NPV) or Return on Investment (ROI) [13]. Use of real options in information technology-related investment decisions makes inherent sense given the dynamic nature of prices of information technology.

Joch [20] is among the earliest literature to consider the use of real options for justifying investment in information technology. [4] also justi<sup>fi</sup>ed the use of real options to evaluate information technology projects, and the same authors used real options to make a case for expanding electronic banking networks in [5]. Other related literature using real options in information technology include [21] and [3]. The interested reader is urged to peruse a rich discussion on the use of real options in information technology projects in [29].

Given the unique nature of computing projects that are suitable for grid computing (limited timeframes of use, bursty demand, etc.), organizations that want to use grid computing might not want to manage the infrastructure in-house [7]. In response to that demand, we now have several hardware providers like IBM, Sun Microsystems and Hewlett-Packard who maintain dedicated infrastructures that are rented out to organizations. The arrangement is mutually bene<sup>fi</sup>cial – the customers get to use the high-end infrastructure for limited times without the associated problems of managing the infrastructure, and the providers can recoup the investment in the infrastructure through effective “time-sharing”. In this paper, we consider the pricing and investment decisions for a grid computing provider who wants to provide its services to different classes of customers who differ in the priority of jobs that they wish to assign to the grid computing provider. We analyze a two-period model where the provider has the option to either buy or rent the necessary equipment at the beginning of either period. We develop an intuitive rule of thumb for the provider that assists him in making the rent versus buy decision.

The remainder of the paper is organized as follows: We provide a brief review of related literature in the next section. This is followed by the proposed model. We then conclude the paper in the following section with a brief discussion.

## 2. Related literature

There is a paucity of reported research on economics of grid computing. Most work in this area tends to be based on simulation. We provide a brief overview of a selected few among these.

Tycoon [24] is a distributed market-based grid resource allocation system. It is based on a decentralized auction-based model where each host (called auctioneer) allocates local resources to users who achieve the most value from any given allocation. The users have limited budget, and they bid on resources that they deem to provide the most utility. For each resource, the bids basically signify the amount the user is willing to pay per unit time of resource use. An auctioneer collects the bids and allocates resources in proportion to the bids. Since it is a decentralized mechanism, the auctioneers do not share information with one another. Therefore, a user requiring resources from a few different hosts is required to independently bid for those resources. However, it is not clear from their results whether the cumulative effect of locally ef<sup>fi</sup>cient resource allocation translates to ef<sup>fi</sup>cient resource allocation in the entire grid. Tycoon has several components: service location server (SLS), bank, auctioneer, and agent, where the <sup>fi</sup>rst two components are centralized and the latter two are decentralized. Messages among these components are encrypted. Since not all bids are successful, an appreciable amount of resources including communication and computing are spent on handling the auction mechanism.

Gomoluch and M. Schroeder propose a market-based mechanism for resource allocation, and consider three cases: continuous double auction protocol, proportional share protocol, and round-robin [13]. They study the load factor, number of resources, heterogeneity among resources, and communication delays to compare the three cases. In continuous double auction protocol, the best match satisfying the task's constraints is selected for a given price bid. If the best match is unavailable, the task waits in queue for next availability. In proportional share protocol, several tasks are simultaneously allowed to share a resource according to the proportion of their price bids. The round-robin approach allocates resources as and when available without regard to price. Clearly the continuous double auction protocol and proportional share protocol perform better than round-robin under the four performance criteria studied.

Stuer et al. use a commodity-based model where the value of a grid resource is determined based on supply and demand information [28]. They also consider grid resources to be substitutable by two types: high-end and low-end. Customers are provided with a limited budget, and they express their preferences for resources on the grid. Providers allocate a given resource to a customer if the average past price of that resource is less than the current asking price. They characterize market equilibrium by the point at which supply equals demand, and determine the price at this point.

Abramson et al. use the prototype Nimrod-G resource broker to study the economic aspects of grid computing [1]. They use real-world examples to illustrate their framework. Wolski et al. consider both auctions and commodity markets to allocate resources in a grid, and conclude that commodity markets are preferable to auctions for this purpose [30].<sup>1</sup> They use simulation experiments to study the dynamics associated with auctions and commodity markets in a grid computing context.

In contrast to the extant literature which has largely looked at the problem of ef<sup>fi</sup>ciently allocating resources that are already present within the computing grid, this article considers the grid computing provider's perspective from an investment standpoint — the promise of grid computing is widely acknowledged, but the actual demand for it is still subject to wide variability. From a provider's perspective, he has to make a large investment in the hardware, but even more crucially, he has to invest in developing highly specialized middleware that can effectively harness the resources of a wide array of generic hardware so that they can scale effectively with highly specialized software that have traditionally used supercomputing platforms — in other words, an infrastructure that does not lend itself to be used in a wide variety of computing needs. Thus, the provider has to make an informed decision in a highly volatile environment. Our research suggests that using a real options valuation model in this environment might be of interest to a provider in this setup.

We are not aware of any existing literature on real options that speci<sup>fi</sup>cally considers investment decisions related to grid computing. We believe that this research is a <sup>fi</sup>rst step in that direction.

## 3. The model

Our objective in this research is to develop an implementable tool for managers that will help in the process of pricing and making investment decisions on grid computing infrastructure. We assume that there is a monopoly provider for the grid computing service, who caters to multiple customers. The monopoly assumption is justi<sup>fi</sup>able, since the grid computing environment is highly specialized — even though the hardware platform is very generic in nature, in order to effectively utilize the raw computing power of this generic hardware, the middleware that harnesses this computing power is very specialized in nature. It requires a thorough knowledge of the hardware, operating systems and networking, and such knowledge is in very limited supply (as opposed to programmers developing, say, a commercial database application with a wide portfolio of use). It is therefore not surprising that there are consequently very few service providers in the area of grid computing, thus justifying our assumption.<sup>2</sup>

Summary of all notations

<table><tr><td>a</td><td>Growth factor</td></tr><tr><td> $u_{j}$  (j=H,L)</td><td>The proportional up movement of high/low-end service</td></tr><tr><td> $d_{j}$  (j=H,L)</td><td>The proportional down movement of high/low-end service</td></tr><tr><td> $\Delta t$ </td><td>The time interval</td></tr><tr><td>r</td><td>The risk-free rate of return</td></tr><tr><td>I</td><td>The initial investment (sunk cost)</td></tr><tr><td> $\alpha$ </td><td>Fraction of high-end customers</td></tr><tr><td> $\mu$ </td><td>Provider&#x27;s job processing rate</td></tr><tr><td> $\lambda$ </td><td>Total job arrival rate</td></tr><tr><td> $P_{j}^{*}$ </td><td>The lowest price that the provider would charge for high/low-end service</td></tr><tr><td> $P_{j}'$ </td><td>The highest price that customers will pay for high/low-end service</td></tr><tr><td> $\sigma_{j}$  (j=H, L)</td><td>Risk (follows Brownian motion)</td></tr><tr><td> $P_{ij}$  (i={1, 2, ...,n}; j={H, L} \)</td><td>The price of service level j at the stage i</td></tr><tr><td> $\Omega_{i}$  (i=1,2)</td><td>The investment value at stage i</td></tr><tr><td> $\Omega_{2}'$ </td><td>The discounted value of investing at the stage two</td></tr><tr><td> $P_{j}$  (j=H, L)</td><td>The price for the high/low-end service</td></tr><tr><td> $V_{j}$  (λ) (j=H, L)</td><td>The customer&#x27;s gross utility of the high/low-end service</td></tr><tr><td> $C_{j}$  (j=H, L)</td><td>The provider&#x27;s cost of the high/low-end service</td></tr><tr><td> $C_{D}$ </td><td>Cost of development of specialized middleware</td></tr><tr><td> $d_{j}$  (j=H, L)</td><td>Customers&#x27; disutility of waiting in queue for service</td></tr><tr><td> $q_{j}$  (j=H, L)</td><td>Probability of the high/low-end service price increases</td></tr></table>

The monopolist provider sets the price so as to maximize its pro<sup>fi</sup>ts. The customers, however, can choose to buy the service from the provider, have the infrastructure in-house or forgo it altogether, implying that the customer has a gross utility for the service that helps set the maximum price that he would be willing to pay. We summarize the notations we employ for the various parameters in (Table 1).

## 3.1. Setting the customers' prices

To complete the computing task at hand, the customers of the grid service have two choices — buying the grid computing service from a service provider at either the higher or the lower levels of service. Since the likely customers of grid computing service are large corporations, we assume that network bandwidth for accessing the service is not a limitation. Further, as is customary for such economic agents, we assume that the customers are risk neutral.

We assume that the provider provides two types of services, a high-end service and low-end service. A highend service has high-priority and a customer requesting such a service is expecting the job to be handled using necessary resources as quickly as possible, and therefore are assumed to be willing to pay a relatively high price for that service. These jobs probably require real-time handling, and the provider might need to reschedule the existing jobs and put more time and computer resources on such jobs. An example of such a job would be the pension-calculating application of Hewitt Associates that we mentioned earlier. On the other hand, a low-end service request need only be handled anytime before its due date. An example of such a project is the SETI@home project that ran on idle computing time on millions of personal computers all over the world. These due dates are set such that the service can be delivered on time even with low priority. With such characteristics in place, we assume that $V _ { \mathrm { H } } ( \lambda ) \gg V _ { \mathrm { L } } ( \lambda )$ . It follows that for a high-end service, the provider can charge a premium, and the “per-unit” price he charges for a high-end service request, $P _ { \mathrm { H } } ,$ is higher than the per-unit price for a low-end service request, $P _ { \mathrm { L } }$ . It is also conceivable that the average marginal cost for catering to a high-end service request is higher than the average marginal cost for catering to a low-end service request $( C _ { \mathrm { H } } { > } C _ { \mathrm { L } } ) .$ Finally, we assume that the cost of developing the specialized middleware $C _ { \mathrm { D } }$ is prohibitively high.

We apply an M/M/1 queuing system to describe the service system where the customers are characterized by a Poisson arrival rate of requests (jobs) per unit of time $\lambda ,$ and a fraction α of these jobs are high-priority jobs. The service provider has the capacity to process µ jobs per unit time.

The producer then tries to maximize his pro<sup>fi</sup>ts subject to the customer's participation and incentive compatibility constraints:

$$
\text { Max } \pi = \alpha (P _ {\mathrm{H}} - P _ {\mathrm{L}}) + (1 - \alpha) (P _ {\mathrm{L}} - C _ {\mathrm{L}})
$$

subject to

$$
V _ {\mathrm{L}} (\lambda) - \frac {\mu d _ {\mathrm{L}}}{(\mu - \alpha \lambda) (\mu - \lambda)} - P _ {\mathrm{L}} \geq 0\tag{1}
$$

$$
V _ {\mathrm{H}} (\lambda) - \frac {d _ {\mathrm{H}}}{(\mu - \alpha \lambda)} - P _ {\mathrm{H}} \geq 0\tag{2}
$$

$$
\left[ V _ {\mathrm{L}} (\lambda) - \frac {\mu d _ {\mathrm{L}}}{(\mu - \alpha \lambda) (\mu - \lambda)} - P _ {\mathrm{L}} \right] - \left[ V _ {\mathrm{L}} (\lambda) - \frac {d _ {\mathrm{L}}}{(\mu - \lambda)} - P _ {\mathrm{H}} \right] \geq 0\tag{3}
$$

$$
\left[ V _ {\mathrm{H}} (\lambda) - \frac {d _ {\mathrm{H}}}{(\mu - \alpha \lambda)} - P _ {\mathrm{H}} \right] - \left[ V _ {\mathrm{H}} (\lambda) - \frac {d _ {\mathrm{H}}}{(\mu - \lambda)} - P _ {\mathrm{L}} \right] \geq 0\tag{4}
$$

$$
\frac {1 + R}{R} (C _ {\mathrm{H}} + C _ {\mathrm{D}}) - P _ {\mathrm{H}} \geq 0\tag{5}
$$

$$
\frac {1 + R}{R} (C _ {\mathrm{L}} + C _ {\mathrm{D}}) - P _ {\mathrm{L}} \geq 0.\tag{6}
$$

The two inequalities (1) and (2) refer to the participation constraints of the low-type and high-type customers respectively, while Eqs. (3) and (4) are their respective incentive compatibility constraints. The inequalities re<sup>fl</sup>ect the fact that the high-type customer jobs can preempt the low-type customer jobs. The inequalities (5) and (6) re<sup>fl</sup>ect the fact that the prices that the service provider charges its customers is not that high that the customers prefer to buy the hardware and develop the software themselves. Notice that the cost of developing the software is a long-term sunk cost, and therefore does not <sup>fi</sup>gure in the short-run pro<sup>fi</sup>t term.

Constraints (3) and (4) can be combined together to express a relationship between the prices charged for the high-end and the low-end customers:

$$
d _ {\mathrm{L}} \left(\frac {\mu}{(\mu - \alpha \lambda) (\mu - \lambda)} - \frac {1}{(\mu - \lambda)}\right) \leq P _ {\mathrm{H}} - P _ {\mathrm{L}} \leq d _ {\mathrm{H}} \left(\frac {1}{(\mu - \lambda)} - \frac {1}{(\mu - \alpha \lambda)}\right)\tag{7}
$$

Since constraint (7) holds and $V _ { \mathrm { H } } ( \lambda ) \gg V _ { L } ( \lambda ) ,$ , it is easy to verify that while the monopolist service provider can make constraint (1) binding (in other words, extract all surplus from the low-type customers), constraint (2) is not (the high-type customers retain some surplus), and in fact, the highest that the service provider can charge for the high-type customers is given by the right-hand side of constraint (7) (As we assume that the cost of developing the specialized middleware software is prohibitively high, constraints (5) and (6) can never be binding and are there for completeness sake). In other words, we can conclude that

$$
P _ {\mathrm{L}} ^ {\prime} = V _ {\mathrm{L}} (\lambda) - \frac {\mu d _ {\mathrm{L}}}{(\mu - \alpha \lambda) (\mu - \lambda)}\tag{8}
$$

and

$$
P _ {\mathrm{H}} ^ {\prime} = P _ {\mathrm{L}} ^ {\prime} + d _ {\mathrm{H}} \left(\frac {1}{(\mu - \lambda)} - \frac {1}{(\mu - \alpha \lambda)}\right).\tag{9}
$$

The above prices are the highest prices that customers will pay for the high/low-end service. In the next section, the lowest prices that service provider can charge for providing service will be derived.

![](/api/attachments/3ERT5YFT/fulltext/images/a88b812f6d1613a308a8b09ec6fd36a65a050dfdf53e42eda0689978075576ab.jpg)  
Fig. 1. Monte Carlo simulations of P<sub>L</sub>.

## 3.2. The provider's options

With this knowledge of what the customers are willing to pay for his services, the provider can make a decision on how to fund his grid computing infrastructure. As stated earlier, the provider has the option to buy the equipment at two (higher or lower) levels. This decision is based on the future market price, the quantum of demand, the obsolescence cost, and other variables that are stochastic in nature. We use Real Option Valuation to address the provider's problem, primarily because Real Options analyses enable capturing strategic value that is oftentimes overlooked in traditional analysis. Real options analysis has strategic value when

1. There is uncertainty in the project.

2. This uncertainty itself drives the project value.

3. The decision-maker has <sup>fl</sup>exibility in his decision-making.

4. The <sup>fl</sup>exibility in the strategies is credible and can be acted upon.

5. The decision-maker is rational in executing the strategies.

To demonstrate the utility of real options in this particular environment, we carried out Monte Carlo simulations of the prices and pro<sup>fi</sup>ts of the service provider by changing the different variables. For the purposes of this exercise, we kept, somewhat arbitrarily, $V _ { \mathrm { H } } V _ { H } = 1 0 ,$ , with the ratio $V _ { \mathrm { H } } / V _ { \mathrm { L } }$ varying normally around a mean of 5 and standard deviation of 0.83 (so that the ratio varies between 2.5 and 7.5 within 3 standard deviations around the mean. Similarly, we kept $d _ { \mathrm { L } } = 1$ , and varied the ratio $d _ { \mathrm { H } } / d _ { \mathrm { L } }$ normally around a mean of 5. The service capacity µ was <sup>fi</sup>xed at 10 units, and the arrival rate of jobs was again varied normally around a mean of 2 units. Finally, the fraction of high-type customers α was varied around a mean of 0.3.

![](/api/attachments/3ERT5YFT/fulltext/images/e5765ff69d60e1055cba1e288ca39fb5709cfb76c5b41a27317e7faa43e29d44.jpg)  
Fig. 2. Monte Carlo simulations of P .

![](/api/attachments/3ERT5YFT/fulltext/images/dc92683fd3f3f6ad9c809cbb6b54e5c0be3aac9f9c81d8aaa46bc011e7eb2f25.jpg)  
Fig. 3. Monte Carlo simulations of pro<sup>fi</sup>t from low-end customers.

The results of the Monte Carlo simulations are shown in Figs. 1–6.

With the above set of parameter values, it can be seen that the service provider's pro<sup>fi</sup>t can vary widely, and moreover, the contribution from the low-end is signi<sup>fi</sup>cant — there is nearly 50% probability that 80% or more of the provider's total pro<sup>fi</sup>t is provided by the low-end customers.

This brings into focus the need for having an option to expand capacity to serve high-end customers only if the circumstances warrant. In deciding to invest on the grid computing infrastructure, the provider of the grid computing service faces uncertainty on several fronts — the demand for the service and the price of the information technology equipment being its primary sources. However, he has the <sup>fl</sup>exibility to defer the decision of buying the equipment at a later time period (if at all), as the uncertainties get resolved over time. The setup, therefore, is a natural <sup>fi</sup>t for using the

Real Option Valuation technique for analysis. We assume that the provider has to decide to buy a determined proportion of the two types of machines — low-end machines or high-end machines. We build the model under the assumption that the demand is for one unit and assume that the variation of prices captures the variation in demand.

Based on these considerations, we use the binomial tree methodology to value investment decisions in a sequence of stages by incorporating the variation of price per demand in our model. The decision tree based on price is generated by working forward from valuation date to expiration. At each node in the decision tree, we assume that the price moves either up or down by pre-speci<sup>fi</sup>ed factors u or d respectively. We also incorporate standard assumptions that are made in the Real Options literature (see for example [19]), such as the price P of the service following a geometric Brownian motion with volatility σ. By de<sup>fi</sup>nition, if $P _ { \mathrm { H } }$ is the current price of high level service, in the next period the price will either be $P _ { \mathrm { u p } } { = } P _ { \mathrm { H } } \left( 1 { + } u \right)$ or $P _ { \mathrm { d o w n } } = P _ { \mathrm { H } } ( 1 - d )$ . The up and down factors are calculated using the underlying volatility $\begin{array} { r } { \sigma _ { \mathrm { H } } = f \Big ( \lambda , \alpha , \frac { V _ { \mathrm { H } } } { V _ { \mathrm { L } } } , \frac { d _ { \mathrm { H } } } { d _ { \mathrm { L } } } , C _ { \mathrm { H } } , C _ { \mathrm { D } } \Big ) } \end{array}$ . Similarly, the current price of low level service $\mathrm { P _ { L } }$ will increase or decrease in the next period and the movement is calculated using the volatility $\begin{array} { r } { \sigma _ { \mathrm { L } } = f \Big ( \lambda , \alpha , \frac { V _ { \mathrm { H } } } { V _ { \mathrm { L } } } , \frac { d _ { \mathrm { H } } } { d _ { \mathrm { L } } } , C _ { \mathrm { L } } \Big ) } \end{array}$ . The time duration of a step t is normally measured in years but can be adjusted to <sup>fi</sup>t the needs of the problem of interest. If the service provider evaluates grid computing investment decisions every year then t is in years. If investing projects are assessed every month then the time duration of a step t represents the number of months in the period. Here we use the commonly accepted assumption and let the duration be the number of years. Since the variance of the log of the price is $\sigma ^ { 2 } t ,$ we denote the variation of high level service prices in the different stages in the following schematic (Fig. 7).

![](/api/attachments/3ERT5YFT/fulltext/images/15ab928b07c348828b25a2310f8012eff2e8b5c9a2caf0ff9af7186aa18fb0b0.jpg)  
Fig. 4. Monte Carlo simulations of pro<sup>fi</sup>t from high-end customers.

![](/api/attachments/3ERT5YFT/fulltext/images/f702a01701b27d9ebae440c72ad637a0828bb15c158ac927bd474869d2ee8145.jpg)  
Fig. 5. Monte Carlo simulations of total pro<sup>fi</sup>t π.

Assuming uncertainties are cleared up at stage 2, prices in the later stages stay the same. This one-stage model captures characteristics of Real Options method and can be repeated n times when solving n stage problem. At stage 1, although the future price of each unit of grid computing is unknown, the provider can predict the up and down movements of the prices and calculate the value of investment $\begin{array} { r } { V _ { 1 } = \frac { \alpha P _ { \mathrm { H 1 } } ( 2 + q _ { \mathrm { H } } * ( \overline { { u } } _ { \mathrm { H } } + d _ { \mathrm { H } } ) - d _ { \mathrm { H } } ) + ( 1 - \alpha ) P _ { \mathrm { L 1 } } ( 2 + q _ { \mathrm { L } } * ( u _ { \mathrm { L } } + d _ { \mathrm { L } } ) - d _ { \mathrm { L } } ) } { r } } \end{array}$ . In order to maintain the <sup>fl</sup>ow of the paper without unnecessary clutter, we have included the derivation of results in Appendix $\mathsf { A } , \mathsf { I f } V _ { 1 }$ is greater than the initial payout I, the service provider will invest in the grid services project. Otherwise, there is no incentive for the provider to invest. Let $\Omega _ { 1 } = \operatorname { M a x } ( V _ { 1 } - 1 , 0 )$ be the investment value at stage 1. The provider will invest only if $\Omega _ { 1 } > 0 .$ . The provider will not invest i $\mathrm { f } \Omega _ { 1 } { < } 0 ,$ , while being indifferent when $\Omega _ { 1 } = 0 .$ . We assume that for our purposes, the uncertainty resolves in Period 2. While we could have allowed for more variability in the later periods, the usefulness of the real options valuation technique can be demonstrated from this simple exercise.

![](/api/attachments/3ERT5YFT/fulltext/images/21cf94ee12b70f54e9ff50c252414565a87071490421abba456158dfec916b3c.jpg)  
Fig. 6. Monte Carlo simulations of pro<sup>fi</sup>t contribution of low-end customers

![](/api/attachments/3ERT5YFT/fulltext/images/28cc63606cce95ece436cd6d51f485f9384cd0e29787c0f02879352460d2cb72.jpg)  
Fig. 7. Schematic of different stages.

Real Options allows for deferring investment decision till a later point in time. Assuming the price for the service is known and other uncertainties are cleared up at stage 2, the provider defers the investment decision until stage 2. The investment value at stage 2 is given by $\begin{array} { r } { V _ { 2 } = \frac { [ \alpha P _ { \mathrm { H } 2 } + ( 1 - \alpha ) P _ { \mathrm { L } 2 } ] } { r } } \end{array}$ Depending on whether the price of the service is known as well as other uncertainties at stage 2, the provider has the choice to make investment decision following similar arguments and logic. If $\Omega _ { 2 } = \mathrm { M a x } ( V _ { 2 } - 1 , 0 ) { > } 0$ , the provider will invest on buying equipment to provide grid service either at the high or low level. If $\Omega _ { 2 } < 0 ,$ , the provider will not invest. Discounting the investment value to stage 1, we get $\begin{array} { r } { \Omega ^ { \prime } = \frac { 1 } { 1 + r } } \end{array}$ q4Max <sup>½</sup> <sup>-</sup> <sup>αPH1þð</sup> <sup>Þ</sup> <sup>1−α</sup> <sup>PL1</sup> <sup>ð</sup> <sup>Þ</sup> <sup>1þu</sup> −I; 0<sup></sup> <sup></sup> 1−q Max <sup>½</sup> <sup>-</sup> <sup>αPH1þð</sup> <sup>Þ</sup> <sup>1−α</sup> <sup>PL1</sup> <sup>ð</sup> <sup>Þ</sup> <sup>1−d</sup> −I; 0<sup>h</sup> <sup>i</sup> <sup></sup> <sup></sup> ; where $q = \alpha \dot { q } _ { \mathrm { H } } + ( 1 - \alpha ) q _ { \mathrm { L } }$ . The provider will not invest in buying, but would rather prefer to wait at stage 1 if $\Omega ^ { \prime } { } _ { 1 } > \Omega _ { 1 }$ If $\Omega ^ { \prime } { } _ { 1 } > \Omega _ { 1 } ,$ the provider will invest and buy equipment for providing grid services at the stage 1. The investment values depend primarily on the price that the service provider can charge the customer. Depending on the service level (i.e., high or low) there exists a price $P _ { j } ^ { * } ( j { = } \mathrm { H } , \mathrm { L } )$ , such that when $P _ { j 1 } { > } P _ { j } ^ { * }$ the provider invests in the respective (high or low) infrastructure and when $P _ { j 1 } { < } \mathrm { P } _ { j } ^ { * }$ , the provider defers the investment option to next stage. This process can be repeated iteratively as long as there are unresolved uncertainties. Positive investment decision takes place only when the provider is reasonably certain of the outcome, and this materializes when reduction in uncertainties occur as more information about the dynamics of the market is gathered over time.

## 3.3. The decision rules

The above analysis derives the highest prices of high/lowend services $( P _ { \mathrm { ~ H ~ } } ^ { \prime }$ and $P _ { \mathrm { ~ L ~ } } ^ { \prime }$ that customers will pay and the lowest prices $\left( P _ { \mathrm { H } } { } ^ { * } \right.$ and $P _ { \mathrm { L } } { } ^ { * } )$ that the grid computing service provider can charge for the services provided that the project is pro<sup>fi</sup>table. Our work points to the basic set of investment decision rules for the grid computing provider. Under different sets of realized prices, the provider will make different decision, but the basic rules are as follows (Figs. 8–13).

## 3.3.1. Investing in high-end and low-end infrastructure

In this case, the price and service quality combination that the high- and low-end service customers would be willing to pay for are respectively higher than the prices that the provider has to charge to make his investment pro<sup>fi</sup>table. The provider will invest in buying both high-end and low-end infrastructure. This is an agreeable scenario for both provider and customer, and both high- and low-end services will be provided.

## 3.3.2. Investing in both high- and low-end infrastructure

This case will lead the provider to invest in both high- and low-end infrastructure, but primarily in low-end infrastructure. The rationale here is that the price set by the provider for high- and low-end services are lower than customer's reservation prices for the same. The provider can safely charge higher and make the investment more pro<sup>fi</sup>table. This case is different from the previous case in that the customers are willing to get low-end service by paying more than the price charged for high-end service by the provider. With no prior knowledge of the costs and the technology infrastructure that is involved, the customers are willing to pay a higher price.

![](/api/attachments/3ERT5YFT/fulltext/images/82abc27fc8d023772ef46a02d2bec0298a6c9ee325449441acb6916b32de219d.jpg)  
Fig. 8. Decision rule 1.  
Fig. 9. Decision rule 2.

![](/api/attachments/3ERT5YFT/fulltext/images/c633b90ad88e51e72aa7861b8cc478d350e8277d45a84d0fed46e3fa6c730e1b.jpg)  
Fig. 10. Decision rule 3.  
Fig. 13. Decision rule 6.

Another interesting observation in this case is that the provider can make the project more pro<sup>fi</sup>table by investing more in low-end infrastructure. But the provider still needs to invest minimally in high-end infrastructure for two reasons. Firstly, considering the prospective increase in demand for high-end infrastructure, the provider can reduce layout cost without completely replacing the equipment during every period. While high-end infrastructure can be used in later periods as low-end, it does not work the other way around. Most of the low-end infrastructure is replaced in the following period. Secondly, the provider might be interested in meeting the demand for high-end service from some customers in order to get another slice of the market pie.

## 3.3.3. Investing only in high-end infrastructure

In this scenario, it is pro<sup>fi</sup>table for the provider to invest in high-end infrastructure, and not the low-end infrastructure. Customers would like to use high-end service but not low-end service. This follows from the observation of the price difference between high-end and low-end infrastructure. If the low-end infrastructure is cheap, customers would rather buy their own equipment instead of renting them from the provider. The decreasing cost of computing equipment renders this a viable alternative in some cases. For high-end infrastructure, because of the cost involved, it is more reasonable from the customer's perspective to rent from the provider than buy given the fact that the reservation price of customers is higher than the price charged by the provider. This scenario is readily observable in reality. Following Moore's law, customers perceive the price of low-end infrastructure to be reasonable and that it is good to buy, but they would rather wait for the price on high-end infrastructure to get lower, so they resort to renting the highend service <sup>fi</sup>rst. This scenario happens in transparent markets where information is symmetric.

![](/api/attachments/3ERT5YFT/fulltext/images/2b635094e2d727f97b8dbaed1c16ed83af7f57c4cf04731912f69254a57e9e63.jpg)  
Fig. 11. Decision rule 4.

![](/api/attachments/3ERT5YFT/fulltext/images/ec6d45574448f0d58a3b34c6a4efb766a108dfb5d09b23fc9fa1442926e58bea.jpg)  
Fig. 12. Decision rule 5.

## 3.3.4. Investing in low-end infrastructure

This case describes that the situation that investing only on low-end infrastructure makes the investment pro<sup>fi</sup>table. The price for low-end service that the customers would like to pay is higher than the price that the provider would like to charge. However, this is reversed for high-end service and the customer would not be interested in such a price-service combination.

## 3.3.5. No major investment, but could enter the market

In this scenario, current investments in grid computing infrastructure do not result in any short-term pro<sup>fi</sup>t, regardless of the level of high- or low-end investment. In such a scenario, the provider can enter the market <sup>fi</sup>rst by charging low-end price for high-end service with the aim of attracting customers in the <sup>fi</sup>rst stage. If the project turns out to be pro<sup>fi</sup>table, the provider can expand the investment in the following periods. The advantage of this early-entrant strategy is to capture the market share earlier when competition is lower or non-existent. This strategy is important for long-term market development.

## 3.3.6. No investment

The price that customers would like to pay for high-end and low-end services are lower than price charged by the provider for high-end and low-end service respectively. The provider does not have any incentive to invest in either of the services.

To summarize, the provider's investment decisions in high end or low-end service depend on the maturity of the market, the degree of information asymmetry, and the cost of infrastructure, among other factors.

## 4. Conclusion

Grid computing is becoming a viable option for businesses looking for high-end computing requirements for relatively short periods of time without investing in expensive infrastructure. We analyze the dynamics of some economic decision criteria for a grid computing provider wishing to provide such a service to businesses. Monte Carlo simulations of the analytical results illustrate the large amount of variability in the outcome. Given the large amount of uncertainty in price and demand for such a service, a Real Options valuation technique is particularly suitable for such an exercise.

Extensions of this exercise include considering competition among providers to cater to a grid computing service requirement. The advantage of assuming a monopolist service provider is of course the tractability of the analytical results. While the analytical exercise becomes rather complicated even with competition between two <sup>fi</sup>rms, several observations can be made. Competition between the service providers can be modeled in two ways — horizontal differentiation (where the customers have a preference for one of the service providers) or vertical differentiation (where the two <sup>fi</sup>rms are supposed to differ in quality that is unambiguously recognized by potential customers). In a nascent industry like grid computing, where the service offerings are not yet mature, what we have seen so far has mostly been undifferentiated service offerings based on price. If we assume that the “quantity” (or rather, the number of jobs that can be serviced per unit of time) offered by a <sup>fi</sup>rm is limited, we can conjecture that the quantity restriction will not be as extreme as a Bertrand outcome [6], and the equilibrium will be some form of a Cournot outcome [11], as established by [23] in a more traditional setting. A more probable result however is that given a duopoly setting and the high costs of entry, the two service providers might resort to “cooperation” in the in<sup>fi</sup>nitely repeated game, whereby both of them decide to charge the same prices until one provider “defects” (this result is an offshoot of the “folk theorems” of repeated games which “assert that if the players are suf<sup>fi</sup>ciently patient then any feasible, individually rational payoff can be enforced by an equilibrium” [16].

As the industry matures and more competitors enter the market, we should witness providers coalescing around different core competencies, and different types of computing requirements will be catered to by different service providers. Given the relative uniqueness of the service, we do not expect there to be any meaningful competitors within the different market segments.

In our current exercise, we did not consider the effect of technological advancements that are unique to information technology investments, popularly known as Moore's Law [26]. Thus, an extension of the current research can incorporate scenarios in which a service provider can initially buy a limited number of computers for his grid (and thereby forego some revenue from the high-end customers), and have the option to expand later when the price of the technology falls.

## Appendix A

Stage one: the investment value

$$
\begin{array}{l} V _ {\mathrm{H1}} = P _ {\mathrm{H1}} + [ q _ {\mathrm{H}} * P _ {\mathrm{H1}} (1 + u _ {\mathrm{H}}) + (1 - q _ {\mathrm{H}}) * P _ {\mathrm{H1}} (1 - d _ {\mathrm{H}}) ] \\ \times \left(\frac {1}{(1 + r)} + \frac {1}{(1 + r) ^ {2}} + \frac {1}{(1 + r) ^ {3}} + \dots\right) \\ = P _ {\mathrm{H1}} [ 1 + (1 + u _ {\mathrm{H}}) q _ {\mathrm{H}} + (1 - d _ {\mathrm{H}}) (1 - q _ {\mathrm{H}}) ] \left(\frac {\frac {1}{1 + r}}{1 - \frac {1}{1 + r}}\right) \\ = \frac {P _ {\mathrm{H1}} (2 + q _ {\mathrm{H}} * (u _ {\mathrm{H}} + d _ {\mathrm{H}}) - d _ {\mathrm{H}})}{r} \end{array}
$$

$$
\begin{array}{r l} & \text {   Similarly,   } V _ {\mathrm{L1}} = \frac {P _ {\mathrm{L1}} (2 + q _ {\mathrm{L}} * (u _ {\mathrm{L}} + d _ {\mathrm{L}}) - d _ {\mathrm{L}})}{r}. \\ & V _ {1} = \alpha V _ {\mathrm{H1}} + (1 - \alpha) V _ {\mathrm{L1}} \\ & = \frac {\alpha P _ {\mathrm{H1}} (2 + q _ {\mathrm{H}} * (u _ {\mathrm{H}} + d _ {\mathrm{H}}) - d _ {\mathrm{H}}) + (1 - \alpha) P _ {\mathrm{L1}} (2 + q _ {\mathrm{L}} * (u _ {\mathrm{L}} + d _ {\mathrm{L}}) - d _ {\mathrm{L}})}{r} \end{array}
$$

Let $\Omega _ { 1 } = \operatorname { M a x } ( V _ { 1 } - I , 0 )$

▪ I $\mathrm { ~ f ~ } \Omega _ { 1 } > 0 ,$ , then the provider invest at the stage one.

▪ If $\varOmega _ { 1 } = 0$ , then no investment at the stage one.

Stage two: the investment value

$$
\begin{array}{l} V _ {2} = P _ {2} \left(\frac {1}{(1 + r)} + \frac {1}{(1 + r) ^ {2}} + \frac {1}{(1 + r) ^ {3}} + \dots\right) = \frac {P _ {2}}{r} \\ = \frac {\alpha P _ {\mathrm{H2}} + (1 - \alpha) P _ {\mathrm{L2}}}{r} \\ \text {   Let   } \Omega_ {2} = \operatorname{Max} (V _ {2} - 1. 0) \end{array}
$$

▪ If $\overline { { \Omega } } _ { 2 } > 0 ,$ , then the provider invest at the stage two.

▪ If $\begin{array} { r } { { \bf \nabla } \cdot \Omega _ { 2 } = { \bf 0 } , } \end{array}$ , then no investment at the stage two.

Let $\boldsymbol { \Omega ^ { \prime } } _ { 2 }$ be the discounted value of $\Omega _ { 2 }$ at stage 1, $P _ { 1 } { ^ { * } } ( 1 { + } u )$ be the price up move, and $P _ { 1 } { ^ * } ( 1 - d )$ be the price down move.

$$
\begin{array}{l} \Omega_ {2} ^ {\prime} = \frac {1}{1 + r} E V (\Omega_ {2}) \\ = \frac {1}{1 + r} \left[ q ^ {*} \operatorname{Max} \left(\frac {[ \alpha P _ {H 1} + (1 - \alpha) P _ {L 1} ] (1 + u)}{r} - I, 0\right) \right. \\ \left. + (1 - q) \operatorname{Max} \left(\frac {[ \alpha P _ {H 1} + (1 - \alpha) P _ {L 1} ] (1 - d)}{r} - I, 0\right) \right] \end{array}
$$

where $P _ { i } { = } \alpha P _ { \mathrm { H i } } { + } ( 1 { - } \alpha ) P _ { \mathrm { L } i }$ and $q { = } \alpha q _ { \mathrm { H } } { + } ( 1 { - } \alpha ) q _ { \mathrm { I } }$

Investment decision-making at the stage 1:

$$
\text { Let } \pi = \operatorname{Max} (\Omega_ {1}, \Omega_ {2} ^ {\prime}),
$$

▪ If $\scriptstyle { \pi = \Omega _ { 1 } }$ , then the provider will make an investment and buy machines at the <sup>fi</sup>rst stage.

▪ If $\pi = \Omega ^ { \prime } _ { 2 } ,$ , the provider will not invest at the <sup>fi</sup>rst stage but will invest at the second stage, so he rent machines at the <sup>fi</sup>rst stage but buy at the second stage.

$\mathrm { I f } \pi { = } 0 ,$ , the provider neither invest at stage one nor at stage two. He rent machines both at the <sup>fi</sup>rst stage and second stage.

## References

[1] D. Abramson, R. Buyya, J. Giddy, A computational economy of grid computing and its implementation in the nimrod-g resource broker, Future Generation Computer Systems 18 (2002) 1061–1074

[2] J. Altmann, A model for resource sharing for Internet data center providers within the grid, 1st IEEE International Workshop on Grid Economics and Business Models, 2004, pp. 113–120.

[3] M. Benaroch, Managing information technology investment risk: a rea options perspective, Journal of Management Information Systems 19 (2) (2002) 43–84.

[4] M. Benaroch, R.J. Kauffman, A case for using real options pricing analysis to evaluate information technology project investments, Information Systems Research 10 (1) (1999) 70–86.

[5] M. Benaroch, R.J. Kauffman, Justifying electronic banking network expansion using real options analysis, MIS Quarterly 24 (2) (2000) 197-225

[6] J. Bertrand, Theorie mathematique de la richesse sociale, Journal des Savants 67 (1883) 499–508.

[7] H.K. Bhargava, S. Sundaresan, Computing as utility: managing availability, commitment, and pricing through contingent bid auctions Journal of Management Information Systems 21 (2) (2004) 201–227.

[8] J. Bort, Grid on the job, in: Network World, 2004

[9] R. Buyya, S. Venugopal, A gentle introduction to grid computing and technologies, Computer Society of India Communications (2005) 9–19.

[11] A. Cournot, Recherches sur les principes mathématiques de la théorie des richesses, (English ed.)Macmillan, New York, 1897.

[12] K. Czajkowski, I. Foster, C. Kesselman, Resource co-allocation in computational grids,, The Eighth IEEE International Symposium on High Performance Distributed Computing, 1999, p. 37.

[13] A.K. Dixit, R.S. Pindyck, Investment under uncertainty, Princeton University Press, Princeton, NJ, 1994.

[14] I. Foster, C. Kesselman, Globus: a metacomputing infrastructure toolkit, International Journal of Supercomputer Applications 11 (2) (1997) 115–128.

[15] I. Foster, C. Kesselman, S. Tuecke, The anatomy of the grid: enabling scalable virtual organizations, International Journal of Supercomputer Applications 15 (3) (2001).

[16] D. Fudenberg, J. Tirole, Repeated games, in: Game theory, The MIT Press, Cambridge, Massachusetts, 1991, p. 150

[17] J. Gomoluch, M. Schroeder, Market-based resource allocation for grid computing: a model and simulation, Middleware Workshop, 2003, pp. 211–218.

[18] J. Gomoluch, M. Schroeder, Performance evaluation of market-based resource allocation for grid computing, Concurrency and Computation: Practice and Application (2004) 1–6.

[19] S. Hamm, Getting a grip on grid computing, in: BusinessWeek, 2004.

[20] A. Joch, Grid gets down to business, in: Network World, 2004.

[21] Y.J. Kim, G.L. Sanders, Strategic actions in information technology investment based on real option theory, Decision Support Systems 33 (1) (2002) 1–11.

[22] E. Korpela, D. Werthimer, D. Anderson, J. Cobb, M. Lebofsky, Seti@home — massively distributed computing for seti, Computing in Science & Engineering (January 2001) 78–83.

[23] D.M. Kreps, J. Scheinkman, Quantity precommitment and Bertrand competition yields Cournot outcomes, Bell Journal of Economics 14 (1983) 326–337.

[24] K. Lai, L. Rasmusson, E. Adar, L. Zhang, B.A. Huberman, Tycoon: an implementation of a distributed, market-based resource allocation system, Multiagent and Grid Systems 1 (3) (2005) 169–182.

[25] S.S. Oren, Integrating real and <sup>fi</sup>nancial options in demand-side electricity contracts, Decision Support Systems 30 (3) (2001) 279–288.

[26] R.R. Schaller, Moore's law: past, present and future, IEEE Spectrum 34 (6) (1997) 52–59.

[27] H. Stockinger, De<sup>fi</sup>ning the grid: a snapshot on the current view, Journal of Supercomputing (March 2007).

[28] G. Stuer, K. Vanmechelen, J. Broeckhove, A commodity market algorithm for pricing substitutable grid resources, Future Generation Computing Systems 23 (5) (2007) 688–701.

[29] P.P. Tallon, R.J. Kauffman, H.C. Lucas, A.B. Whinston, K. Zhu, Using real options analysis for evaluating uncertain investments in information technology: insights from the ICIS 2001 debate, Communications of the Association for Information Systems, vol. 9, 2002, pp. 136–167, 9 (2002).

[30] R. Wolski, J.S. Plank, J. Brevik, T. Bryan, Analyzing market-based resource allocation strategies for the computational gridThe International Journal of High Performance, Computing Applications 15 (3) (Fall 2001) 258–281.

Juheng Zhang is a Ph.D. student in the Department of Information Systems and Operations Management in the Warrington School of Business at the University of Florida. Her interests are in quantum computing and quantum games, economics of information systems, and real options.

Subhajyoti Bandyopadhyay is currently an Assistant Professor in the department of Information Systems and Operations Management in the University of Florida, Gainesville. He received his Ph.D. in Management Information Systems from Purdue University in 2002. His work has been published in Information Systems Research, Journal of Operations Management, European Journal of Operational Research, Decision Sciences Journal, Decision Support Systems, Communications of the ACM, International Journal of Electronic Commerce, Journal of Electronic Commerce Research, Journal of Organizational Computing and Electronic Commerce, Lecture Notes in Computer Science and the Database for Advances in Information Systems. His current research interests include economics of information systems, electronic commerce strategies, and information systems policy issues, especially in the area of Net Neutrality. He is a member of the INFORMS and the AEA.

Selwyn Piramuthu is Associate Professor in the Information Systems and Operations Management department at the University of Florida. His research interests include RFID, pattern recognition and its application in supply chain management, computer-aided manufacturing, and <sup>fi</sup>nancial credit-risk analysis.
