---
otero_id: 12158
otero_key: "CR8UYHGX"
title: "Price competition with service level guarantee in web services"
authors: "Zhongju Zhang; Yong Tan; Debabrata Dey"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.01.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Price competition with service level guarantee in web services<sup>☆</sup>

Zhongju Zhang <sup>a,</sup>⁎, Yong Tan <sup>b</sup>, Debabrata Dey <sup>b</sup>

<sup>a</sup> School of Business, University of Connecticut, Storrs, CT 06269–1041, United States

<sup>b</sup> Michael G. Foster School of Business, University of Washington, Box 353200, Seattle, WA 98195–3200, United States

## a r t i c l e i n f o

Article history: Received 25 April 2008 Received in revised form 13 January 2009 Accepted 26 January 2009 Available online 3 February 2009

Keywords: Price competition Service differentiation Quality of service guarantee Capacity constraint

## a b s t r a c t

Web services have become quite popular over the last few years as they allow easier development and integration of business applications. Unlike traditional software systems, web services are self-contained modular software components that are delivered over a network (such as the Internet) and executed on a remote system hosting the requested services. However, the network and processing overhead associated with web services have also presented a signi<sup>fi</sup>cant challenge to its performance. As a result, a web service provider often announces a service-level agreement when launching a service. The service-level agreement provides a guarantee to the consumers that they can get the service they pay for at an assured level of quality. In this paper, we study the competition between two such providers offering functionally the same web services. Each provider needs to decide a service level (standard or premium) she would offer and a corresponding price for the selected service level to meet the QoS guarantee (in terms of an average response time of the service). We <sup>fi</sup>rst analyze the case where the providers choose service levels and prices simultaneously, and then extend it to a sequential-move situation. Finally, we examine strategic choices of providers when the processing capacity is endogenized into the model.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

In recent years, web services have gained popularity as a useful and ef<sup>fi</sup>cient technology for developing and integrating web applications [51]. Unlike traditional software systems, web services are modular software components that are delivered to the user over a network (such as the Internet) and executed on a remote system hosting the requested services. The software components encapsulate certain business functionality, and are usually self-contained, loosely coupled, and programmatically accessible using standard Internet protocols that permit different types of systems to share information without human intervention [16,36]. This can also form the basis of interorganizational collaboration and distributed process management [17,38,52].

Web services provide an inexpensive and rapid solution for system development and integration. Typically, service providers create and publish components with speci<sup>fi</sup>c functionalities. A service consumer who needs certain functionality can resort to various web service discovery mechanisms to locate and invoke the service using standard protocols by paying a fee [4,16]. For example, Google's AdWords web service (see http://www.google.com/apis/adwords/) allows consumers to design computer programs to interact directly with its AdWords platform. After registering for AdWords to obtain a developer token and an application token, advertisers can invoke the service by paying US\$0.25 (per 1000 service requests) to ef<sup>fi</sup>ciently manage their complex AdWords accounts and campaigns (such as generating automatic custom reports and integrating AdWords data with the inventory system). Another major player in the competitive pay-per-click advertising market is Yahoo! Search Marketing (see http://searchmarketing.yahoo.com). They offer similar web services that consumers can use to write and manage ads delivered by Yahoo! Search Marketing. This new model of system development has several bene<sup>fi</sup>ts. In addition to the universal availability and interoperability of components, consumers get lower up-front costs and more frequent software updates. Service providers not only procure the service implementations, but also offer technical support and execute services on demand [34,35].

Despite its great promise, there are serious concerns about the performance of a web service because of the network bandwidth and processing overhead associated with transferring the large and complex XML-based messages over the network. In some instances, a service provider may not be able to handle the throughput, resulting in a serious performance degradation. As a result, when launching a service, a service provider often announces a web service-level agreement (WSLA) along with the capability and interfaces of the service (see Fig. 1). The service capability and interfaces de<sup>fi</sup>ne the conceptual purpose as well as the input/output of the web service. The WSLA, on the other hand, de<sup>fi</sup>nes agreed performance metrics and ways to evaluate and measure them [22,34]. The WSLA thus serves as a formal contract (guaranteeing quanti<sup>fi</sup>able performance metrics at pre-speci<sup>fi</sup>ed levels) between a service provider and a consumer. It assures consumers that they can get the quality of service (QoS) they pay for and obligates the service provider to deliver on the promises.

![](/api/attachments/CR8UYHGX/fulltext/images/cd0cf1c3bcf67fdf4730bb36047a0a54b855d060cb5f4418a022d9b92ec88b9f.jpg)  
Fig. 1. Role of web service level agreement (Source: [22]).

A service-level agreement for a web service could include several quality metrics, such as response time or latency, availability, accessibility, reliability, and versioning [1,22,25,32,43,48]. Among the various quality dimensions, the response time is often considered to be the most critical dimension and the most dif<sup>fi</sup>cult one to manage [27,39,49,50], and hence is the focus of the paper. The response time refers to how long it takes for a web service to respond and is typically measured as the average time over a speci<sup>fi</sup>ed time horizon. Web service portals, such as StrikeIron (see http://www.strikeiron.com), now post both the average response time and the corresponding cost for web services.

Irrespective of the robustness or the functionalities of a web service, in order to maintain a WSLA, especially with respect to the response time, it is necessary for the web service provider to design and implement a proper pricing scheme. A pricing scheme works as an ef<sup>fi</sup>cient access control mechanism by providing suf<sup>fi</sup>cient incentives to users so that they choose appropriate service levels. Although there is a rich body of prior research on pricing products and services, these traditional pricing schemes do not usually work well for web services: First, the marginal cost of providing the service to an additional user is negligible, thereby reducing the traditional price to zero. Second, a very important aspect here is the social cost of congestion; traditional pricing models do not capture this negative externality. On the other hand, non-pricing approaches to access control for reducing the congestion cost are either <sup>fl</sup>awed or, more generally, have undesirable side effects [23]. Pricing, on the other hand, has an advantage because it permits users to express the value they place on obtaining a service. Users can trade off their bene<sup>fi</sup>ts from the service against its price (plus the delay cost) to make informed decisions. The number of low-value and frivolous users is thereby likely to decrease, which could provide a better quality of service (QoS) for high-value users [23].

The main contribution of this research is development of a framework for competitive pricing of web services. We combine modeling constructs from game theory and queueing theory to propose a rigorous model that can provide useful insights to service providers about pricing, capacity planning, and general competitive strategies. More speci<sup>fi</sup>cally, we study duopoly competition between two providers offering web services with the same functionality. Facing a continuum of users who value the bene<sup>fi</sup>ts from the service against its price (plus the delay cost), a provider needs to decide a service level (standard or premium) she would offer, and a corresponding price for the selected service level to meet the QoS guarantee (in terms of the average response time of the service). We <sup>fi</sup>rst analyze the case where the providers choose service levels and prices simultaneously, and then extend it to a sequential-move situation. Finally, we examine strategic choices of providers when the overall service capacity is endogenized into the model.

Our analyses show that the equilibrium choices depend on the traf<sup>fi</sup>c intensity. When the traf<sup>fi</sup>c intensity is low (or the processing capacity is relatively large), the principle of differentiation observed in traditional markets still holds, i.e., one provider chooses to provide the standard service while the other premium service. As traf<sup>fi</sup>c increases, however, providers may end up choosing exactly the same service level, thus competing head to head. We also <sup>fi</sup>nd that providing the premium service may not always enjoy a higher pro<sup>fi</sup>t, especially under a heavy traf<sup>fi</sup>c because of the high cost of congestion. In the long-run situation involving capacity planning, on the other hand, head-to-head competition is not observed. In that case, the providers are actually better off if they differentiate from each other. Practically, this research provides useful insights for web service providers on how to position themselves in a competitive market. Conventional wisdom emphasizes the importance of differentiation by a provider so that it can increase its margins and improve pro<sup>fi</sup>tability. This research demonstrates that a provider's optimal product position depends on the situation and may or may not be different from the competitor.

Our work relates to the pricing of a service that is subject to queueing delays. In a classical article, Mendelson [28] shows that the optimal price for a pro<sup>fi</sup>t-maximizing <sup>fi</sup>rm is equal to the expected marginal delay cost. A number of studies, such as [9,26,30], have followed, all with an aim to improve the overall ef<sup>fi</sup>ciency of a single network (or service facility). In the context of data network pricing, various pricing schemes (for example, [14,15,24,41,49], to name a few)

have been proposed. In recent years, these pricing schemes have also been applied to web services. For example, Lin et al. [21] conduct a pilot study to demonstrate the use of dynamic pricing scheme to manage web service resources. Tang and Cheng [44] study the pricing and location strategy of a web service intermediary that provides time-sensitive integrated services from two complementary service providers. Consumers have the choice of buying the composite web service from either the intermediary or buying the complementary services directly from the two providers and integrating them.

Research on the duopoly competition in the presence of a delay cost dates back at least to [19], when they noted that there always exists a symmetric equilibrium if the market is covered. Similar studies [8,20] have been subsequently conducted under different assumptions. These models were also extended to other areas such as data networks or service industries (e.g., [2,3,6,10,13,42,50]). These studies demonstrated a common <sup>fi</sup>nding, i.e., the existence of symmetric equilibrium for identical <sup>fi</sup>rms in the presence of service guarantees.

This paper also relates to the vertical differentiation model. Some of the representative work include [12] and [40], who show that competing <sup>fi</sup>rms typically choose to locate at the extreme ends of quality spectrum to reduce price competition. Moorthy [31] extends the basic model by incorporating variable production costs and demonstrate that, in equilibrium, <sup>fi</sup>rms choose products that are differentiated. Many economists [5,7,11,33,46,47] have subsequently studied this game under various settings. Most of the vertical differentiation models however do not explicitly model capacity constraints (or service guarantees). A general <sup>fi</sup>nding from those models is that <sup>fi</sup>rms differentiate along the quality dimension at equilibrium.

The remainder of the paper is organized as follows. In Section $^ { 2 , }$ we describe the basic modeling framework. Section 3 analyzes the equilibrium pricing strategy when two providers choose service levels and prices simultaneously, while Section 4 discusses the equilibrium strategy in the sequential-move game. In Section 5, we endogenize the processing capacity and study the long-term competition. Finally, Section 6 provides concluding remarks and offers future research directions.

## 2. The model

Assume that there are two identical providers, indexed 1 and 2, offering web services (or software components) with the same functionalities. The processing capacity of each provider is <sup>fi</sup>xed; in Section $5 ,$ we relax this assumption and consider the long-run situation where capacity is also a decision variable. The service can be delivered in one of two discrete QoS levels (for example, standard vs. premium service); each level is characterized by an expected total response time of the service.<sup>1</sup> Let $d _ { L }$ be the response time guarantee for the standard service and $d _ { H }$ for the premium service, where $d _ { L } > d _ { H } .$ . We assume that $d _ { L }$ and $d _ { H }$ are exogenous and fixed.<sup>2</sup> A provider $i \ ( i = 1 , 2 )$ can choose either premium or standard service $d _ { j } ^ { \left( i \right) } \left( j = L \mathrm { o r } H \right)$ and charges a corresponding price $p _ { j } ^ { ( i ) }$ for it. Each provider guarantees that the actual expected response time for her service will be at most $d _ { j } ^ { ( i ) }$ time units. Since the marginal cost of providing a web service is negligible, we set it to zero. The costs of developing web services are assumed sunk.

There is a continuum of users, who look to use web services from one of the two providers. The users differ by two parameters: the value parameter v and the delay-sensitivity parameter h. The value parameter v of a user denotes the value the user assigns to the immediate provision of service. The delay-sensitivity parameter h of a user denotes the disutility (cost) incurred by the user when the provision of service is delayed by one time unit. The disutility is assumed to be linear in h—if the delay-sensitivity is h, then the disutility is hγ per time unit of delay, where γ is a constant. We assume that both v and h are uniformly distributed and are normalized between [0,1]. In order to simplify our analysis, we further assume that v and h are linearly related: $h = \alpha \nu + \beta .$ This is a reasonable assumption since a high value of v usually means that the user is also more delay-sensitive (i.e., a high value of h) in obtaining the service, and vice versa. Extending our analysis to a more general relationship is conceptually straightforward. We now observe that $\beta$ should be zero. This is because users with zero valuation of the service $( \nu = 0 )$ would not be sensitive to delay at all $( h = 0 )$ . Given this, without any loss of generality, we can set α=1, i.e., h=v.

At the time of requesting a service, a user knows the service level and the price charged by each provider. The user, however, does not know in advance the true service level (i.e., the actual response time of the service), which would be known only after the true demand is realized. Hence, the user makes his decision to request a service based on the announced service level. In other words, the net utility of a user with (v,h), who chooses to obtain the service from provider i is $\nu - p _ { j } ^ { ( i ) } - h \gamma d _ { j } ^ { ( i ) }$ . The user chooses the service from a provider in a manner that maximizes his net utility. Of course, the user also has the option of not using any service (with net utility of zero). Assume that the total arrival of users looking for web services follows a Poisson process with a base rate o $\mathrm { \dot {  } } \lambda _ { 0 } ,$ i.e., $. \lambda _ { 0 }$ is the total arrival rate of users when the response time of the service is zero and the service is free. The effective arrival of users accessing service from provider i will only be a random fraction of the original arrival stream. Hence, it also follows a Poisson process, but with a rate $\lambda _ { j } ^ { ( i ) }$ proportional to $\lambda _ { 0 } [ 3 7 ]$ . The user requests are served on a round-robin processor-sharing discipline. The service time of each request follows an arbitrary distribution with a mean service time of b second; in other words, the processing rate of each provider is $\scriptstyle { \frac { 1 } { b } } .$ The above system can be modeled using an $\mathsf { M } / \mathsf { G } / 1$ processor-sharing queue, and the expected total response time $\boldsymbol { W } _ { j } ^ { ( i ) }$ from provider i is given by [18]:

$$
W _ {j} ^ {(i)} = \frac {b}{1 - \rho \frac {\lambda_ {j} ^ {(i)}}{\lambda_ {0}}},
$$

where $\rho { \equiv } \lambda _ { 0 } b { > } 0$ represents the normalized total traf<sup>fi</sup>c intensity. Provider i $( i = 1 , 2 )$ satis<sup>fi</sup>es the WSLA by ensuring that $W _ { j } ^ { ( i ) }$ is no greater than the posted service level $d _ { j } ^ { ( i ) } \left( j = L , H \right)$ ). Therefore, we can formulate provider i's optimization problem as:

$$
\max _ {j, p _ {j} ^ {(i)}} \Pi^ {(i)} = \lambda_ {j} ^ {(i)} p _ {j} ^ {(i)}, s. t. W _ {j} ^ {(i)} \leq d _ {j} ^ {(i)}.\tag{1}
$$

Note that the provider's objective function in this case is simply the total revenue. This makes sense for the short-run problem being studied here, since the capacity is <sup>fi</sup>xed and the marginal cost of providing an additional service is negligible. Subsequently, in Section $5 ,$ we extend our model to the long-run problem where capacity planning is part of the decision model and the marginal cost is not zero.

## 3. Price competition with simultaneous choices

In this section, we consider the situation where service providers choose their service levels (in terms of a premium or standard service) and price decisions simultaneously and non-cooperatively. In other words, when making her own decisions, a provider cannot observe the choices made by the other.

## 3.1. Non-differentiated service

Since both providers choose the same service level d $\left( j = L , H \right)$ , we temporarily drop the superscript denoting the provider. Consumers buy from the provider who charges the lowest price. If they both charge the same price, each provider would face a demand equal to the half of the market demand at that price. Because of the capacity constraint and the service-level agreement, however, a provider may not be able to reduce her price to the marginal cost. We now investigate the range of prices a service provider is allowed to charge.

Let $\overline { { p } } _ { j }$ be the price charged by only one provider (with the other out of the market) such that the response-time constraint due to the service level agreement is binding. Since v is uniformly distributed in [0, 1], only that portion of users with $\nu - \overline { { p } } _ { j } - \nu \gamma d _ { j } { \geq } 0$ will choose service from the provider. In other words, the effective arrival rate for the provider is $\begin{array} { r } { \lambda _ { j } = \lambda _ { 0 } \left( \frac { 1 - \overline { { p } } _ { j } } { 1 - \gamma d _ { j } } \right) } \end{array}$ . Hence, $\overline { { p } } _ { j }$ solves the following equation:

$$
\frac {b}{1 - \rho \left(\frac {1 - \overline {{p}} _ {j}}{1 - \gamma d j}\right)} = d _ {j}.
$$

Further, let p be the common price charged by each provider when they split the market equally and keep the response-time constraint binding. In this case, the effective arrival rate for each provider can be obtained as $\begin{array} { r } { \lambda _ { j } = \frac { 1 } { 2 } \lambda _ { 0 } \Bigl ( 1 - \frac { \underline { { p } } _ { j } } { 1 - \gamma d _ { j } } \Bigr ) } \end{array}$ . Hence ${ \underline { { p } } } _ { j }$ solves the following equation:

$$
\frac {b}{1 - \frac {\rho}{2} \left(1 - \frac {\underline {{p}} _ {j}}{1 - \gamma d _ {j}}\right)} = d _ {j}.
$$

Solving the above two equations, we get:

$$
\overline {{p}} _ {j} = \left(1 - \gamma d _ {j}\right) \left(1 - \frac {u _ {j}}{\rho}\right) \text {   and   } \underline {{p}} _ {j} = \left(1 - \gamma d _ {j}\right) \left(1 - \frac {2 u _ {j}}{\rho}\right),
$$

where $\begin{array} { r } { u _ { j } = 1 - \frac { b } { d _ { i } } } \end{array}$ . It can be easily veri<sup>fi</sup>ed that both $\overline { { p } } _ { j }$ and ${ \underline { { p } } } _ { j } ,$ as de<sup>fi</sup>ned above, can be negative if the total traf<sup>fi</sup>c intensity $( \rho )$ is very low. This is because, when $\rho$ is small, the delay constraint could become slack—arti<sup>fi</sup>cially forcing the delay constraint to be binding would lead to negative prices. Of course, prices cannot be negative in reality, so we re-de<sup>fi</sup>ne:

$$
\overline {{p}} _ {j} = \max \left\{0, (1 - \gamma d _ {j}) \left(1 - \frac {u _ {j}}{\rho}\right) \right\} \text {   and   } \underline {{p}} _ {j} = \max \left\{0, (1 - \gamma d _ {j}) \left(1 - \frac {2 u _ {j}}{\rho}\right) \right\}.
$$

Lemma 3.1. In a non-differentiated market, (i) the equilibrium price $p _ { j } ^ { ( i ) }$ must satisfy $\underline { { p } } _ { j } \leq p _ { j } ^ { ( i ) } \leq \overline { { p } } _ { j } ,$ , and (ii) every symmetric price choice $\mathring { p _ { j } ^ { ( 1 ) } } = p _ { j } ^ { ( 2 ) } = p _ { j } \in \overline { { [ \overline { { p } } _ { j } , \underline { { p _ { j } } } ] } }$ is an equilibrium.

The proof of this lemma and those of subsequent lemmas and propositions are all provided in an appendix.

Of all the possible symmetric Nash equilibria, we consider only the Pareto-dominant one—an equilibrium that maximizes the pro<sup>fi</sup>t when two providers split market equally. Let p be the common price charged by both the providers if they both choose service level $d _ { j } .$ Then, the effective demand to each provider is $\textstyle { \frac { 1 } { 2 } } \lambda _ { 0 } \left( 1 - { \frac { p _ { j } } { 1 - { \gamma d _ { i } } } } \right)$ . Hence, the optimization problem of each provider can be written as:

$$
\begin{array}{l l} \max _ {j, p _ {j}} & \Pi = \frac {1}{2} \lambda_ {0} p _ {j} \left(1 - \frac {p _ {j}}{1 - \gamma d _ {j}}\right), \\ s. t. & \frac {b}{1 - \frac {\rho}{2} \left(1 - \frac {p _ {j}}{1 - \gamma d _ {j}}\right)} \leq d _ {j}, \\ & \underline {{p}} _ {j} \leq p _ {j} \leq \overline {{p}} _ {j}. \end{array}
$$

We can solve the above to obtain the equilibrium price; this is summarized in Lemma 3.2.

Lemma 3.2. When both the providers choose the same service level, the Pareto optimal price is given by:

$$
p _ {j} = \left(1 - \gamma d _ {j}\right) \times \left\{ \begin{array}{l l} 0, & \text { if } \rho <   u _ {j}, \\ 1 - \frac {u _ {j}}{\rho}, & \text { if } u _ {j} \leq \rho <   2 u _ {j}, \\ \frac {1}{2}, & \text { if } 2 u _ {j} \leq \rho <   4 u _ {j}, \\ 1 - \frac {2 u _ {j}}{\rho}, & \text { otherwise }. \end{array} \right.\tag{2}
$$

Here, as before, $\begin{array} { r } { u _ { j } = 1 - \frac { b } { d _ { i } } . } \end{array}$

Lemma 3.2 implies that, without service differentiation, competitive providers would price at the marginal cost (zero, in this case) if the processing capacity is much greater than what is required to serve the overall traf<sup>fi</sup>c intensity $\scriptstyle ( \rho < u _ { j } )$ . This means that, when the processing capacity is not a concern, our result reduces to that of standard Bertrand price competition [45]. However, as the traf<sup>fi</sup>c intensity increases, providers must increase the market price in order to provide the promised service-level agreement. Consequently, the optimal price is greater than zero, and providers make positive pro<sup>fi</sup>ts.

It is also interesting to note that, when $u _ { j } \le \rho < 2 u _ { j } ,$ a provider can increase the price only to $\overline { { p } } _ { j } { < } \frac { 1 - \gamma d _ { j } } { 2 }$ because this is the price a single provider could charge to maintain the service agreement. When the traf<sup>fi</sup>c intensity is within a range $( 2 u _ { j } \le \rho < 4 u _ { j } )$ , the competitive price $\frac { 1 - \gamma d _ { j } } { 2 }$ is exactly the same as that would be charged by a monopoly provider in the absence of a service-level agreement. Finally, when the traf<sup>fi</sup>c intensity is very high $\scriptstyle ( \rho > 4 u _ { j } )$ , a provider charges the lowest feasible price $\underline { { \dot { p } } } _ { i } > \frac { 1 - \gamma d _ { j } } { 2 }$ . At this price, the market demand for each provider is exactly equal to the maximum she can meet, given her capacity level $\textstyle { \frac { 1 } { b } }$ and service-level agreement $d _ { j } .$ . The reason is as follows: In the non-differentiated market with service-level agreement, two factors determine the price equilibrium—a competitive factor that compels the <sup>fi</sup>rms to reduce prices, and a service-warranty factor that requires the <sup>fi</sup>rms to increase prices in order to meet the service-level agreement. Of course, the most pro<sup>fi</sup>table price for each <sup>fi</sup>rm is the “monopoly” price. When this price is not feasible, the <sup>fi</sup>rms would choose a price closest to it because of the Pareto dominance.

Substituting the prices into the pro<sup>fi</sup>t functions, we can obtain the pro<sup>fi</sup>t of each provider for choosing service level j as:

$$
\Pi_ {j} = \Big (1 - \gamma d _ {j} \Big) \times \left\{ \begin{array}{l l} 0, & \text { if   } \rho <   u _ {j}, \\ \frac {u _ {j}}{2 b} \bigg (1 - \frac {u _ {j}}{\rho} \bigg), & \text { if   } u _ {j} \leq \rho <   2 u _ {j}, \\ \frac {\rho}{8 b}, & \text { if   } 2 u _ {j} \leq \rho <   4 u _ {j}, \\ \frac {u _ {j}}{b} \bigg (1 - \frac {2 u _ {j}}{\rho} \bigg), & \text { otherwise }. \end{array} \right.\tag{3}
$$

## 3.2. Differentiated services

Without loss of generality, assume that provider 1 chooses premium-service level $d _ { H }$ while provider 2 chooses standard-service level $d _ { L }$ . This, of course, means that provider 1 must charge a price $p _ { H } ^ { ( 1 ) }$ higher than $p _ { L } ^ { ( 2 ) }$ charged by provider 2.

In order to <sup>fi</sup>nd the equilibrium prices, we need to estimate the expected demand for each provider. Let V be the v-value of the marginal user who is indifferent between the two providers. This implies that $V - p _ { H } ^ { ( 1 ) } - V \gamma d _ { H } = \mathsf { V } - p _ { L } ^ { ( 2 ) } - V \gamma d _ { L } ,$ , or $\begin{array} { r } { V = \frac { { \dot { p _ { H } ^ { ( 1 ) } } - p _ { L } ^ { ( 2 ) } } } { \gamma ( d _ { L } \mathrm { ~ } - \mathrm { ~ } d _ { H } ) } . } \end{array}$ user with v should prefer the premium service if $\nu \in [ V , 1 ] ,$ <sup>ð Þ</sup> or the standard service i $\mathrm { f } \nu \in [ 0 , V ] ;$ this is the incentive-compatibility constraint $( \mathrm { I C C } )$ Even though one level of service may dominate the other, it would be chosen only if the user obtains a non-negative net utility from it. This implies that $\nu - p _ { j } ^ { ( i ) } - \nu \gamma d _ { j } { \geq } 0 ,$ , or $\nu \ge \frac { p _ { j } ^ { ( i ) } } { 1 - \gamma d _ { j } } ;$ this is the individual rationality constraint (IRC). Let $\begin{array} { r } { V _ { H } = \frac { p _ { H } ^ { ( 1 ) } } { 1 - \gamma d _ { H } } } \end{array}$ and $\begin{array} { r } { V _ { L } = \frac { p _ { L } ^ { ( 2 ) } } { 1 - \gamma d _ { L } } } \end{array}$ . Then combining ICC and IRC, we can express the effective arrival rates for the two providers as:

![](/api/attachments/CR8UYHGX/fulltext/images/fc454e95ef306eadeb7e4cab9586250dedc52edc13a36563f15861dee058075c.jpg)  
Fig. 2. Equilibrium prices as functions of ρ.

$$
\lambda_ {H} ^ {(1)} = \lambda_ {0} [ 1 - \max \{V, V _ {H} \} ] \quad \text { and } \quad \lambda_ {L} ^ {(2)} = \lambda_ {0} [ \max \{V, V _ {L} \} - V _ {L} ].\tag{4}
$$

Lemma 3.3. At equilibrium, $V _ { H }$ and $V _ { L }$ are both less than V.

Lemma 3.3 and Eq. (4) imply that $\lambda _ { H } ^ { ( 1 ) } = \lambda _ { 0 } ( 1 - V )$ and $\lambda _ { L } ^ { ( 2 ) } = \lambda _ { 0 } ( V -$ $V _ { L } ) _ { \ L }$ , where $\lambda _ { 0 }$ is the total arrival rate of users, as de<sup>fi</sup>ned earlier. We can then formulate each provider's optimization problem by substituting $\lambda _ { H } ^ { ( 1 ) }$ and ${ \lambda } _ { L } ^ { ( 2 ) }$ into (1); solving for optimal prices, we get Lemma 3.4.

Lemma 3.4. In a differentiated market, the optimal prices are given by:

$$
p _ {H} ^ {(1)} = (1 - \gamma d _ {H}) \times \left\{ \begin{array}{l l} 2 x _ {1}, & \text { if } \rho <   v _ {1}, \\ 2 x _ {2} \bigg (1 - \frac {u _ {H}}{\rho} \bigg), & \text { if } v _ {1} \leq \rho <   v _ {2}, \\ 1 - \frac {u _ {H} + x _ {3} u _ {L}}{\rho}, & \text { otherwise }; \end{array} \right.\tag{5}
$$

and

$$
p _ {L} ^ {(2)} = (1 - \gamma d _ {L}) \times \left\{ \begin{array}{l l} x _ {1}, & \text { if } \rho <   v _ {1}, \\ x _ {2} \bigg (1 - \frac {u _ {H}}{\rho} \bigg), & \text { if } v _ {1} \leq \rho <   v _ {2}, \\ 1 - \frac {u _ {H} + u _ {L}}{\rho}, & \text { otherwise }; \end{array} \right.\tag{6}
$$

where

$$
x _ {1} = \frac {\gamma (d _ {L} - d _ {H})}{3 + \gamma d _ {L} - 4 \gamma d _ {H}}, x _ {2} = \frac {\gamma (d _ {L} - d _ {H})}{1 + \gamma d _ {L} - 2 \gamma d _ {H}}, x _ {3} = \frac {1 - \gamma d _ {L}}{1 - \gamma d _ {H}},\tag{7}
$$

and

$$
v _ {1} = u _ {H} + \frac {u _ {H}}{2 (1 - x _ {2})}, v _ {2} = u _ {H} + \frac {u _ {L}}{1 - x _ {2}}.
$$

It can be seen from the above lemma that in a differentiated market, providers never charge their marginal costs (zero). Choosing differentiated services allows two providers to be unique in the QoS dimension. Hence both providers can command a price greater than the marginal cost. In that context, one might think that providers would always obtain a higher pro<sup>fi</sup>t by strategically choosing differentiated services. However, we will demonstrate in the next section that, at equilibrium, two providers may end up choosing the same service and competing directly against each other.

As before, the pro<sup>fi</sup>ts for the two providers under differentiated services can be obtained as:

$$
\Pi_ {H} ^ {(1)} = (1 - \gamma d _ {H}) \times \left\{ \begin{array}{l l} \frac {4 \rho}{b} x _ {1} ^ {2} \frac {1 - \gamma d _ {H}}{\gamma (d _ {L} - d _ {H})}, & \text { if } \rho <   v _ {1}, \\ \frac {2 u _ {H}}{b} x _ {2} \bigg (1 - \frac {u _ {H}}{\rho} \bigg), & \text { if } v _ {1} \leq \rho <   v _ {2}, \\ \frac {u _ {H}}{b} \bigg (1 - \frac {u _ {H} + x _ {3} u _ {L}}{\rho} \bigg), & \text { otherwise }; \end{array} \right.\tag{8}
$$

and

$$
\Pi_ {L} ^ {(2)} = (1 - \gamma d _ {L}) \times \left\{ \begin{array}{l l} \frac {\rho}{b} x _ {1} ^ {2} \frac {1 - \gamma d _ {H}}{\gamma (d _ {L} - d _ {H})}, & \text { if } \rho <   v _ {1}, \\ \frac {\rho}{b} x _ {2} ^ {2} \frac {1 - \gamma d _ {H}}{\gamma (d _ {L} - d _ {H})} \bigg (1 - \frac {u _ {H}}{\rho} \bigg) ^ {2}, & \text { if } v _ {1} \leq \rho <   v _ {2}, \\ \frac {u _ {L}}{b} \bigg (1 - \frac {u _ {H} + u _ {L}}{\rho} \bigg), & \text { otherwise }. \end{array} \right.\tag{9}
$$

Because of symmetry, it is clear that $I I _ { L } ^ { ( 1 ) } { = } I I _ { L } ^ { ( 2 ) }$ and $I I _ { H } ^ { ( 2 ) } { = } I I _ { H } ^ { ( 1 ) }$

## 3.3. Equilibrium strategies

Before we can decide the equilibrium strategies, we assume that $u _ { L } x _ { 3 } > 2 u _ { H }$ . This assumption is reasonable and generally implies that: (i) $d _ { L }$ and d are well separated, and (ii) the server capacity is limited.<sup>3</sup>

The payoff to a provider depends not only on her own choice, but also on the choice by the competitor. If both providers chose the same service level, they both have the same payoff given in Eq. (3). If provider i chooses the premium service, and provider j chooses the standard service, the payoffs are $\varPi _ { H } ^ { ( i ) }$ and $\boldsymbol { \Pi } _ { L } ^ { ( j ) }$ to providers i and j, respectively; Eqs. (8) and (9) provide these payoffs. Since the functional forms of these pro<sup>fi</sup>ts vary with overall traf<sup>fi</sup>c intensity ρ, several types of equilibrium strategies, as summarized in Proposition 3.1, could exist.

Proposition 3.1. There exists $\rho _ { 1 } , \rho _ { 2 } ,$ and $\rho _ { 3 }$ (with $\rho _ { 1 } { < } \rho _ { 2 } , \rho _ { 3 } )$ , such that: (i) when $\rho { \le } \rho _ { 1 }$ or $\rho _ { 2 } \le \rho \le \rho _ { 3 } ,$ providers choose differentiated service; (ii) when $\rho _ { 1 } { < } \rho { < } \rho _ { 2 } ,$ , both providers choose the premium service; (iii) when $\rho { > } \rho _ { 3 } ,$ both providers choose the standard service.

Proposition 3.1 has important managerial implications for service providers who need to establish service-level agreements with their customers. When the traf<sup>fi</sup>c intensity is low $\scriptstyle ( \rho < \rho _ { 1 } )$ , the capacity constraint is not relevant, and the service-level agreement does not have an impact on the providers' decision. Analogous to the traditional setting (e.g., [31], both the providers bene<sup>fi</sup>t by locating far away from each other in the service dimension, since the competition in that position is the weakest. Consequently the providers charge different prices for differentiated services. This phenomenon can be clearly seen from Fig. 2, in which equilibrium prices were plotted against $\rho$ when $b = 0 . 2 7 5 \ s ,$ $d _ { L } = 0 . 6 ~ s , d _ { H } = 0 . 3 ~ s$ , and $\gamma = 1$

![](/api/attachments/CR8UYHGX/fulltext/images/8316a20a17bf689e650d8f95f1f2df4dfd6e0a99d8819b07f97f553435c22d70.jpg)  
Fig. 3. Equilibrium demands as functions of ρ.

Fig. 2 also shows that, as the traf<sup>fi</sup>c intensity increases above $\rho _ { 1 } ,$ the standard-service provider becomes interested in the more lucrative premium-service market. In response, however, the premium-service provider chooses not to move. Hence, both providers end up in the same market, charging the same price and splitting the demand equally. Even though price competition intensi<sup>fi</sup>es in this case, the standard-service provider still enjoys a higher pro<sup>fi</sup>t by switching because of the higher price she can charge (see Fig. 2 between $\rho _ { 1 }$ and $\rho _ { 2 } )$ . The symmetric equilibrium may appear a bit surprising at <sup>fi</sup>rst, but it is actually not. With <sup>fi</sup>xed processing capacity (in the short term) and service guarantee, two premium-service providers could only reduce their prices to ${ \overline { { p } } } _ { j } ,$ at which the service agreement kicks in and forces a provider not to lower prices any further.

As ρ increases above $\rho _ { 2 } ,$ one of the premium-service providers now switches to the standard-service position, which yields a higher pro<sup>fi</sup>t than if she sticks with the premium service. This is because the demand for providing standard service becomes much higher; see $\mathrm { F i g } . 3$ in the range of $\rho \in [ \rho _ { 2 } , \rho _ { 3 } ]$

When $\rho$ is beyond $\rho _ { 3 } ,$ the premium-service position is no longer attractive because the high price charged by the premium-service provider is not enough to offset the loss of market share (see Fig. 3). As a result, the premium-service provider switches and both now offer the standard service.

Fig. 4 shows how the equilibrium pro<sup>fi</sup>t changes withρ; the parameter values are the same as the ones used in Figs. 2 and 3. It can be seen that, under differentiated services, providing premium service is more pro<sup>fi</sup>table only when the traf<sup>fi</sup>c is light. As the system becomes more congested $( \rho \in [ \rho _ { 2 } , \rho _ { 3 } ] )$ , premium-service provider makes less pro<sup>fi</sup>t because fewer customers subscribe to premium service due to the high price.

## 4. Price competition with sequential choices

In this section, we analyze the Stackelberg game in which one service provider (the leader) moves <sup>fi</sup>rst, and decides upon her service level $d _ { i } ^ { ( \mathrm { i e a d e r } ) }$ and price $p _ { j } ^ { ( \mathrm { l e a d e r } ) } \left( j = L \operatorname { o r } H \right)$ . The other provider (the follower), observing the choice of the leader, then chooses her service level $d _ { k } ^ { ( \mathrm { f o l l o w e r } ) }$ and the corresponding price $p _ { k } ^ { ( \mathrm { f o l l o w e r } ) } \left( k = L \operatorname { o r } H \right)$ . If the follower chooses the same service level as the leader, there can be only one unique equilibrium, at which the market is split and each provider's pro<sup>fi</sup>t is maximized (see Section 3.1). The unique equilibrium is given by (2).

![](/api/attachments/CR8UYHGX/fulltext/images/d3df35d69815cef5f20c77a50eeb89e309b1c201c61025301e112d053d59d465.jpg)  
Fig. 4. Equilibrium pro<sup>fi</sup>ts as functions of ρ.

If the follower chooses a different service level than the leader, she would react to the leader's choice in a way that maximizes her own pro<sup>fi</sup>t.

Lemma 4.1. If the leader chooses $d _ { L }$ and the follower $d _ { H } ,$ the follower would react (for a given $p _ { L } ^ { ( \mathrm { l e a d e r } ) } )$ by choosing a price:

$$
p _ {H} ^ {\text {(follower)}} = \max \left\{\frac {p _ {L} ^ {\text {(leader)}} + \gamma (d _ {L} - d _ {H})}{2}. p _ {L} ^ {\text {(leader)}} + \gamma (d _ {L} - d _ {H}) \left(1 - \frac {u _ {H}}{\rho}\right) \right\}.
$$

The leader anticipates the reaction of the follower, and chooses a price $p _ { L } ^ { ( \mathrm { l e a d e r } ) }$ to maximize her pro<sup>fi</sup>t, from which we can determine the optimal prices.

Lemma 4.2. If the leader chooses $d _ { L }$ and the follower $d _ { H } ,$ the optimal prices are given by:

$$
p _ {L} ^ {\text {(leader)}} = (1 - \gamma d _ {L}) \times \left\{ \begin{array}{l l} \frac {x _ {2}}{2}, & \text { if } \rho <   v _ {3}, \\ \frac {1}{2} \bigg (1 - \frac {u _ {H}}{\rho} \bigg), & \text { if } v _ {3} \leq \rho <   v _ {4}, \\ 1 - \frac {u _ {H} + u _ {L}}{\rho}, & \text { otherwise }; \end{array} \right.\tag{10}
$$

and

$$
p _ {H} ^ {\text {(follower)}} = (1 - \gamma d _ {H}) \times \left\{ \begin{array}{l l} \frac {3}{4} \frac {x _ {2}}{1 - x _ {1}}, & \text { if } \rho <   v _ {3}, \\ \frac {1}{2 (1 - x _ {2})} \bigg (1 - \frac {u _ {H}}{\rho} \bigg), & \text { if } v _ {3} \leq \rho <   v _ {4}, \\ 1 - \frac {u _ {H} + x _ {3} u _ {L}}{\rho}, & \text { otherwise }; \end{array} \right.\tag{11}
$$

where $\nu _ { 3 } = u _ { H } ( 2 - x _ { 3 } ) , \nu _ { 4 } = u _ { H } + 2 u _ { L } , x _ { 1 } , x _ { 2 } ,$ , and $x _ { 3 }$ are given in (7).

The pro<sup>fi</sup>ts can be obtained as:

$$
\Pi_ {L} ^ {(\text { leader })} = (1 - \gamma d _ {L}) \times \left\{ \begin{array}{l l} \frac {\rho}{8 b} x _ {2}, & \text { if   } \rho <   v _ {3}, \\ \frac {\rho}{4 b} \bigg (1 - \frac {u _ {H}}{\rho} \bigg) ^ {2}, & \text { if   } v _ {3} \leq \rho <   v _ {4}, \\ \frac {u _ {L}}{b} \bigg (1 - \frac {u _ {H} + u _ {L}}{\rho} \bigg), & \text { otherwise }; \end{array} \right.
$$

and

$$
\Pi_ {H} ^ {\text {(follower)}} = (1 - \gamma d _ {H}) \times \left\{ \begin{array}{l l} \frac {3 \rho}{1 6 b} \frac {x _ {2} ^ {2}}{x _ {1} (1 - x _ {1})}, & \text { if } \rho <   v _ {3}, \\ \frac {u _ {H}}{2 b} \frac {1}{1 - x _ {2}} \bigg (1 - \frac {u _ {H}}{\rho} \bigg), & \text { if } v _ {3} \leq \rho <   v _ {4}, \\ \frac {u _ {H}}{b} \bigg (1 - \frac {u _ {H} + x _ {3} u _ {L}}{\rho} \bigg), & \text { otherwise }. \end{array} \right.
$$

Comparing Eqs. (10) and (11) with Eqs. (5) and (6), we observe that:

Lemma 4.3. With service differentiation, the Stackelberg prices are no less than the prices in the simultaneous-move game.

Under high traf<sup>fi</sup>c (for example $\rho { > } V _ { 4 } )$ , the two providers would simply serve consumers equal to their maximum capacities for a given service level d . Hence, two providers would charge exactly the same prices. Under low traf<sup>fi</sup>c, it is intuitive that the leader (offering standard service), in a favorable position of being the <sup>fi</sup>rst mover, can charge a higher price. In the context of service-level agreement, the follower can also charge a higher price. The rationale is as follows. An increase in price for the standard service would make it less attractive to consumers. Hence, more consumers would obtain service from the premium-service provider (the follower), who can then charge a higher price to obtain a higher pro<sup>fi</sup>t.

Lemma 4.4. If the leader chooses $d _ { _ H }$ and the follower $d _ { \mathbf { \Gamma } _ { L } } ,$ , the follower would react to the leader's price choice p(leader) by choosing:

$$
p _ {L} ^ {\text {(follower)}} = \max \left\{\frac {x _ {3}}{2} p _ {H} ^ {\text {(leader)}}, x _ {3} p _ {H} ^ {\text {(leader)}} - \frac {\gamma (d _ {L} - d _ {H}) u _ {L} x _ {3}}{\rho} \right\},
$$

where $x _ { _ 3 }$ is as given in (7).

Lemma 4.5. If the leader chooses $d _ { H }$ and the follower $d _ { L } ,$ the optimal prices are given by:

$$
p _ {L} ^ {\text {(follower)}} = (1 - \gamma d _ {L}) \times \left\{ \begin{array}{l l} \frac {x _ {2}}{2}, & \text { if } \rho <   v _ {5}, \\ x _ {2} \Big (1 - \frac {u _ {H}}{\rho} \Big), & \text { if } v _ {5} \leq \rho <   v _ {2}, \\ 1 - \frac {u _ {H} + u _ {L}}{\rho}, & \text { otherwise }; \end{array} \right.\tag{12}
$$

and

$$
p _ {H} ^ {\text {(leader)}} = (1 - \gamma d _ {H}) \times \left\{ \begin{array}{l l} x _ {2}, & \text { if } \rho <   v _ {5}, \\ 2 x _ {2} \Big (1 - \frac {u _ {H}}{\rho} \Big), & \text { if } v _ {5} \leq \rho <   v _ {2}, \\ 1 - \frac {u _ {H} + x _ {3} u _ {L}}{\rho}, & \text { otherwise }; \end{array} \right.\tag{13}
$$

where $v _ { 5 } = 2 u _ { H }$

The pro<sup>fi</sup>ts are given by:

$$
\Pi_ {H} ^ {(\text { leader })} = (1 - \gamma d _ {H}) \times \left\{ \begin{array}{l l} \frac {\rho x _ {2}}{b   2}, & \text { if } \rho <   v _ {5}, \\ \frac {2 u _ {H}}{b} \bigg (1 - \frac {u _ {H}}{\rho} \bigg) x _ {2}, & \text { if } v _ {5} \leq \rho <   v _ {2}, \\ \frac {u _ {H}}{b} \bigg (1 - \frac {u _ {H} + x _ {3} u _ {L}}{\rho} \bigg), & \text { otherwise }; \end{array} \right.
$$

and

$$
\Pi_ {L} ^ {\text {(follower)}} = (1 - \gamma d _ {L}) \times \left\{ \begin{array}{l l} \frac {\rho}{4 b} x _ {2} ^ {2} \frac {1 - \gamma d _ {H}}{\gamma (d _ {L} - d _ {H})}, & \text { if } \rho <   v _ {5}, \\ \frac {\rho}{b} x _ {2} (1 - x _ {2}) \bigg (1 - \frac {u _ {H}}{\rho} \bigg) ^ {2}, & \text { if } v _ {5} \leq \rho <   v _ {2}, \\ \frac {u _ {L}}{b} \bigg (1 - \frac {u _ {H} + u _ {L}}{\rho} \bigg), & \text { otherwise }; \end{array} \right.
$$

As before, one can easily verify that the Stackelberg prices are at least as high as the simultaneous ones.

Proposition 4.1. There exists $\rho _ { 4 } , \rho _ { 5 } ,$ , and $\rho _ { 6 }$ (with $\rho _ { 4 } { < } \rho _ { 5 } , \rho _ { 6 } )$ , such that: $( i ) i f \rho { \leq } \rho _ { 4 }$ , the leader chooses premium service and the follower chooses standard service; $i f \rho _ { 5 } { \le } \rho \le \rho _ { 6 } ,$ the leader chooses standard service and the follower chooses premium service; (ii) if $\rho _ { 4 } { < } \rho { < } \rho _ { 5 }$ , both providers choose premium service and charge high price; (iii) if $\rho { > } \rho _ { 6 } ,$ both providers choose standard service and charge low price.

The qualitative trends of the sequential equilibria are, therefore, quite similar to those of the simultaneous ones. Under low traf<sup>fi</sup>c $\scriptstyle ( \rho < \rho _ { 4 } )$ , two providers choose differentiated services. Further, the leader chooses the premium service and the follower, the standard service. As traf<sup>fi</sup>c increases beyond $\rho _ { 4 } ,$ the follower switches from the standard service to the premium service and competes directly with the leader. When $\rho$ further increases beyond $\rho _ { 5 } ,$ , the leader provides the standard service because it results in a higher pro<sup>fi</sup>t. Beyond $\rho _ { 6 } ,$ both providers prefer standard service. When providers choose the same level of service, the sequential equilibrium is exactly the same as the simultaneous one. Unlike traditional quality differentiation models, in the context of servicelevel agreements, offering the premium service is not always the enviable position for the leader. When the traf<sup>fi</sup>c intensity is above a certain threshold $( \rho _ { 5 } )$ , the leader would choose standard service (and charge a low price) because the overall pro<sup>fi</sup>t is higher in this case—the reduction in marginal price is more than compensated by the higher demand, which can be met easily with the standard service-level agreement. Interestingly, when the traf<sup>fi</sup>c is above $\rho _ { 6 } ,$ , both providers end up offering only the standard service; in that case, the leader does not enjoy a <sup>fi</sup>rstmover advantage at all.

It is instructive to compare the sequential-move with the simultaneous-move equilibria under differentiated services. When providers move sequentially, both providers charge higher prices (since $x _ { 2 } { > } 2 x _ { 1 } )$ than those in the simultaneous-move game. Fig. 5 illustrates the simultaneous-move and sequential-move equilibria where $\rho { = } 0 . 0 5 ,$ $\gamma = 1 , b = 0 . 2 7 \ s , d _ { L } = 0 . 6 \ s , \mathrm { a n d } d _ { H } = 0 . 3 \ s .$ The dashed lines in this <sup>fi</sup>gure represent the isopro<sup>fi</sup>t curves—thicker lines for the sequential game and thinner lines for the simultaneous game—while the solid lines represent the reaction curves. Using standard notations, we denote S and N as the equilibrium outcomes in the sequential and simultaneous games, respectively. It can be seen from the <sup>fi</sup>gure that the price choices of the two providers are strategic complements; i.e. an increase in $p _ { H }$ induces an increase in p . The temporal asymmetry allows the leader to charge a higher price than it would have done in a simultaneous equilibrium. Consequently, demand for the follower increases, thereby creating an incentive for this provider to increase the price as well. These phenomena are consistent with the existing literature (Tirole,1989) [45].

## 5. Capacity planning and long-term competition

We now consider the duopoly competition when the capacity is a variable. We assume that the cost of capacity is linear, i.e., the cost of capacity <sup>1</sup> is ${ \frac { c } { b } } ,$ where the constant c represents the marginal capacity cost [28,29]. Initially, provider $( i = 1 , 2 )$ invests in a capacity o $\begin{array} { r } { \dot { \cdot } \frac { 1 } { b _ { i } ^ { ( i ) } } ( j = H } \end{array}$ or L) and chooses appropriate QoS level $d _ { j } ^ { ( i ) }$ and price $\hat { p _ { j } ^ { ( i ) } }$ <sup>)</sup>. Once invested, the capacity cost is sunk. In the face of changing demand, however, a provider may solve the short-run problem and adjust by changing the QoS guarantee and/or the price. The long-term pricing problem for provider i can be written as:

$$
\begin{array}{l l} \max _ {j, p _ {j} ^ {(i)}, b _ {j} ^ {(i)}} & \Pi_ {j} ^ {(i)} = \lambda_ {j} ^ {(i)} p _ {j} ^ {(i)} - \frac {c}{b _ {j} ^ {(i)}}, \\ s. t. & \frac {b _ {j} ^ {(i)}}{1 - \lambda_ {j} ^ {(i)} b _ {j} ^ {(i)}} \leq d _ {j} ^ {(i)}. \end{array}
$$

When both capacity and price are decision variables, each provider would invest in a capacity that is exactly equal to the market demand she can serve for a chosen service level $d _ { j _ { \mathbf { \alpha } _ { j _ { \cdot } \mathbf { \hat { n } } } } } ^ { ( i ) } .$ In other words, the optimal solution is obtained only when $\begin{array} { r } { \frac { b _ { j } ^ { ( i ) } } { 1 - \lambda _ { i } ^ { ( i ) } b _ { i } ^ { ( i ) } } = d _ { j } ^ { ( i ) } } \end{array}$ . To see this point, temporarily assume that $( p _ { j } ^ { ( i ) } , b _ { j } ^ { ( i ) } )$ is the optimal solution, but $\frac { b _ { j } ^ { ( i ) } } { 1 - \lambda _ { i } ^ { ( i ) } b _ { i } ^ { ( i ) } } < d _ { j } ^ { ( i ) }$ . Then, without changing $p _ { j } ^ { ( i ) } ,$ , the provider could increase her pro<sup>fi</sup>t by simply increasing $b _ { j } ^ { ( i ) }$ until $\frac { b _ { j } ^ { ( i ) } } { 1 - \lambda _ { i } ^ { ( i ) } b _ { i } ^ { ( i ) } } = d _ { j } ^ { ( i ) }$ . This is because $\frac { b _ { j } ^ { ( i ) } } { 1 - \lambda _ { i } ^ { ( i ) } b _ { i } ^ { ( i ) } }$ increases if $b _ { j } ^ { ( i ) }$ increases, but the effective demand $\lambda _ { j } ^ { ( i ) }$ depends only on her own price $p _ { j } ^ { ( i ) }$ as well as the competitor's price. Hence, we can simplify the capacity constraint to obtain $\begin{array} { r } { b _ { j } ^ { ( i ) } = \frac { d _ { j } ^ { \ast \prime } } { 1 + \lambda _ { i } ^ { ( i ) } d _ { i } ^ { ( i ) } } . } \end{array}$ Substituting $b _ { j } ^ { ( i ) }$ into the pro<sup>fi</sup>t functions and simplifying, we get:

![](/api/attachments/CR8UYHGX/fulltext/images/52394cd62d7b71fea5881abbb60f479b5241ec81f4c3d5e8bfe67bccd1d3456b.jpg)  
Fig. 5. Sequential and simultaneous equilibria.

$$
\max _ {p _ {j} ^ {(i)}} \Pi_ {j} ^ {(i)} = \lambda_ {j} ^ {(i)} \left(p _ {j} ^ {(i)} - c\right) - \frac {c}{d _ {j} ^ {(i)}}.
$$

Furthermore, the two providers would also like to choose differentiated service in stage 1. Otherwise, if they choose the same service level, they would engage in Bertrand price competition in stage $^ { 2 , }$ and both providers would charge prices such that they each make zero pro<sup>fi</sup>t. Without loss of generality, we assume that provider 1 chooses the premium service and provider 2 the standard service. The long-term decision problems of the two providers can then be written as:

$$
\max _ {p _ {H} ^ {(1)}} \Pi_ {H} ^ {(1)} = \lambda_ {H} ^ {(1)} \left(p _ {H} ^ {(1)} - c\right) - \frac {c}{d _ {H}},
$$

and

$$
\max _ {p _ {L} ^ {(2)}} \Pi_ {L} ^ {(2)} = \lambda_ {L} ^ {(2)} \left(p _ {L} ^ {(2)} - c\right) - \frac {c}{d _ {L}},
$$

where, as before, $\begin{array} { r } { \lambda _ { H } ^ { ( 1 ) } = \lambda _ { 0 } ( 1 { - } V ) , \lambda _ { L } ^ { ( 2 ) } = \lambda _ { 0 } ( V { - } V _ { L } ) , V = \frac { p _ { H } ^ { ( 1 ) } - p _ { L } ^ { ( 2 ) } } { \gamma ( d _ { L } - d _ { H } ) } , } \end{array}$ and $\begin{array} { r } { V _ { L } = \frac { p _ { L } ^ { ( 2 ) } } { 1 - \gamma d _ { L } } . } \end{array}$

Proposition 5.1. Let $\begin{array} { r } { \overline { { c } } = \frac { 1 - \gamma d _ { L } } { 2 } } \end{array}$ and

$$
\overline {{\lambda}} _ {0} = \frac {c (3 + \gamma d _ {L} - 4 \gamma d _ {H}) ^ {2}}{\gamma (d _ {L} - d _ {H})} \max \biggl \{\frac {1}{d _ {H} (c - 2 + 2 \gamma d _ {H}) ^ {2}}, \frac {1 - \gamma d _ {L}}{d _ {L} (1 - \gamma d _ {H}) (2 c - 1 + \gamma d _ {L}) ^ {2}} \biggr \}.
$$

$I f c { < } \overline { { c } }$ and $\lambda _ { 0 } > \overline { { \lambda } } _ { 0 } ,$ the long-term equilibrium prices are given by:

$$
p _ {H} ^ {(1)} = \frac {(1 - \gamma d _ {H}) [ 3 c + 2 \gamma (d _ {L} - d _ {H}) ]}{3 + \gamma d _ {L} - 4 \gamma d _ {H}},
$$

and

$$
p _ {L} ^ {(2)} = \frac {c (3 - 2 \gamma d _ {H} - \gamma d _ {L}) + \gamma (d _ {L} - d _ {H}) (1 - \gamma d _ {L})}{3 + \gamma d _ {L} - 4 \gamma d _ {H}}.
$$

The capacities are given by:

$$
b _ {H} ^ {(1)} = \frac {d _ {H} (3 + \gamma d _ {L} - 4 \gamma d _ {H})}{3 + \gamma d _ {L} - 4 \gamma d _ {H} - \lambda_ {0} d _ {H} (c - 2 + 2 \gamma d _ {H})},
$$

and

$$
b _ {L} ^ {(2)} = \frac {d _ {L} (1 - \gamma d _ {L}) (3 + \gamma d _ {L} - 4 \gamma d _ {H})}{(3 + \gamma d _ {L} - 4 \gamma d _ {H}) (1 - \gamma d _ {L}) + \lambda_ {0} d _ {L} (1 - \gamma d _ {H}) (1 - \gamma d _ {L} - 2 c)}.
$$

If c ≥¯¯c or $\lambda _ { 0 } < \overline { { \lambda } } _ { 0 } ,$ providers would not provide any service.

Proposition 5.1 has several implications. When the traf<sup>fi</sup>c intensity is low or the capacity cost is high, both providers exit the market and they make zero pro<sup>fi</sup>t. This is in contrast to the shortterm (where the processing capacity is <sup>fi</sup>xed) equilibrium, where, under low traf<sup>fi</sup>c, providers choose to differentiate from each other. This is because, with low demand, the revenue obtained from providing the service is low and cannot justify the investment cost in the capacity.

![](/api/attachments/CR8UYHGX/fulltext/images/6727b05e9c77aa5ee49fd4a9ffcdee7ecaba75ebc00f7e4be28447d117233333.jpg)  
Fig. 6. Long-term capacity and price as functions of c.

Service differentiation happens only when the market size is “big” enough $\left( \lambda _ { 0 } > \overline { { \lambda } } _ { 0 } \right)$ and the capacity cost is suf<sup>fi</sup>ciently small $( c < \overline { { c } } )$ Moreover, under service differentiation, providers would choose capacity so as to accommodate the demand, and the equilibrium prices are largely independent of the total demand (represented by the overall traf<sup>fi</sup>c intensity $\lambda _ { 0 } )$ . Fig. 6 shows how the equilibrium capacity and the price change with the capacity cost when $\lambda _ { 0 } =$ 60 arrivals/s, $\gamma = 1 , d _ { L } = 0 . 6 \ s ,$ and $d _ { H } = 0 . 3$ s. It can be seen from the <sup>fi</sup>gure that, as the cost of the capacity increases, the optimal capacity investment decreases. Also, to offset the high capacity investment costs, providers also have to raise prices. The marginal impact of the capacity cost on the price of the standard-service provider is smaller than that of the premium-service provider.

## 6. Conclusion

Pricing has been used as an incentive mechanism to control traf<sup>fi</sup>c in many areas. As web services become popular, consumers are asking for service level agreements that guarantee the QoS they pay for. In this context, it is particularly important that service providers design an ef<sup>fi</sup>cient pricing mechanism to enforce service-level agreements. In this paper, we develop a model to study the duopoly competition where service providers can provide either standard or premium service. We found that, in the long run, with reasonable market size and capacity costs, the principle of differentiation always holds. However, in the short run, service providers might choose to compete head to head by providing the same service level. When the traf<sup>fi</sup>c intensity is very high, providing the standard service level is bene<sup>fi</sup>cial. This is because, under a heavy traf<sup>fi</sup>c, the high negative externality imposed by the premium service requires a provider to drastically increase prices (thus resulting in signi<sup>fi</sup>cantly low demand and pro<sup>fi</sup>t).

There are several directions for future research. We have assumed that a provider offers only one level of service. A natural extension is to study the duopoly competition if a provider is allowed to provide multiple priority-based service levels. In that case, the queueing model would be more complicated and providers would have more choices. It would be interesting to see how that affects the pricing strategy. Furthermore, in this paper, we have focused our attention to only one aspect of quality of service, namely the response time. As mentioned earlier, in practice, several aspects of quality are important with respect to web services. We are currently examining how this framework can be extended to multiple dimensions of quality of service. Another possible extension is to explore an oligopolistic setting. Such a model would be analytically intractable, but one could always resort to numerical analysis to gain useful insights.

## Appendix A

Proof of Lemma 3.1.

(i) Assume that provider 1 charges a price $p _ { j } ^ { ( 1 ) } { > } \overline { { p } } _ { j } ,$ , provider 2 can simply set $p _ { j } ^ { ( 2 ) } { = } \overline { { p } } _ { j }$ and get the entire market while meeting the service-level agreement. Hence provider 1 would be better off by reducing her price to ${ \overline { { p } } } _ { j } .$ On the other hand, provider 1 would not charge a price $p _ { j } ^ { ( 1 ) } { < } p _ { j } .$ This is because if she does, provider 2 would charge a price $\mathsf { \chi } _ { p _ { j } } ^ { ( 2 ) } { > } p _ { j } ^ { ( 1 ) }$ in order to commit to her service level guarantee. All the consumers would then choose service from provider 1, resulting in violation of her service level guarantee. By symmetry $p _ { j } ^ { ( \breve { 2 } ) } \in [ \underline { { p } } _ { j } , \overline { { p } } _ { j } ]$

(ii) Suppose provider 1 offers a price $p _ { j } ^ { ( 1 ) } \in [ p _ { j } , \overline { { p } } _ { j } ]$ . If provider 2 chooses $p _ { j } ^ { \dot { ( 2 ) } } { > } p _ { j } ^ { ( 1 ) }$ , all consumers would prefer the service from 2, leading to the violation of provider 2's service level guarantee. Provider 2 also would not choose $p _ { j } ^ { ( 2 ) } { > } p _ { j } ^ { ( 1 ) }$ either, because in that case all consumers would choose the service from 1, resulting in zero pro<sup>fi</sup>t for 2. Hence, the only choice for provider 2 is to charge $p _ { j } ^ { ( 2 ^ { \bullet } ) } { > } p _ { j } ^ { ( 1 ) } . \mathsf { S i n c e } p _ { j } ^ { ( 1 ) }$ is arbitrarily chosen in [p̲ <sub>j</sub>,p¯¯<sub>j</sub>], any price choice $p _ { j } ^ { ( 1 ) } { = } p _ { j } ^ { ( 2 ) } { = } p _ { j }$ is a Nash equilibrium. □

Proof of Lemma 3.2. The formulation is a simple quadratic optimization problem with one decision variable $p _ { j } .$ It is clear that the optimal solution is obtained at either $( \mathsf { a } ) \underline { { p } } _ { j } , ( \mathsf { b } ) \overline { { p } } _ { j } ^ { \cdot } , \mathsf { o r } ( \mathsf { c } )$ if none of the above constraints is binding, then at the price $p _ { j } = { \frac { 1 - \gamma d _ { j } } { 2 } }$ <sup>j</sup> where the objective function is maximized.

Proof of Lemma 3.3. First, we note that $V _ { L } \not \geq V .$ Otherwise, we know from Eq. (10) that $\lambda _ { L } ^ { ( 2 ) } = 0$ , and hence $\Pi _ { L } ^ { ( \tilde { 2 } ) } = 0$ . Provider 2 can then increase her pro<sup>fi</sup>t by decreasing $p _ { L } ^ { ( 2 ) }$ till V drops to a value just below V. This is because, in that case, $\lambda _ { L } ^ { ( 2 ) } { > } 0$ and provider 2 enjoys a positive pro<sup>fi</sup>t while satisfying the service-level agreement. Now, $V _ { L } { < } V$ implies:

$$
\frac {p _ {L} ^ {(2)}}{1 - \gamma d _ {L}} <   \frac {p _ {H} ^ {(1)} - p _ {L} ^ {(2)}}{\gamma (d _ {L} - d _ {H})} \Rightarrow \frac {p _ {H} ^ {(1)} - p _ {L} ^ {(2)}}{p _ {L} ^ {(2)}} > \frac {\gamma (d _ {L} - d _ {H})}{1 - \gamma d _ {L}} \Rightarrow \frac {p _ {H} ^ {(1)}}{p _ {L} ^ {(2)}} > \frac {\gamma (d _ {L} - d _ {H})}{1 - \gamma d _ {L}} + 1 = \frac {1 - \gamma d _ {H}}{1 - \gamma d _ {L}}.
$$

This means

$$
\frac {p _ {L} ^ {(2)}}{p _ {H} ^ {(1)}} <   \frac {1 - \gamma d _ {L}}{1 - \gamma d _ {H}} \Rightarrow 1 - \frac {p _ {L} ^ {(2)}}{p _ {H} ^ {(1)}} > 1 - \frac {1 - \gamma d _ {L}}{1 - \gamma d _ {H}} \Rightarrow \frac {p _ {H} ^ {(1)} - p _ {L} ^ {(2)}}{p _ {H} ^ {(1)}} > \frac {\gamma (d _ {L} - d _ {H})}{1 - \gamma d _ {H}}.
$$

Hence

$$
V _ {H} = \frac {p _ {H} ^ {(1)}}{1 - \gamma d _ {H}} <   \frac {p _ {H} ^ {(1)} - p _ {L} ^ {(2)}}{\gamma (d _ {L} - d _ {H})} = V.
$$

This completes the proof.

Proof of Lemma 3.4. When one provider chooses premium service and the other standard service, the providers' optimization problems can be written as:

$$
\max _ {p _ {H} ^ {(1)}} \Pi_ {H} ^ {(1)} \equiv \lambda_ {0} p _ {H} ^ {(1)} (1 - V),
$$

$$
s. t. \quad \frac {b}{1 - \rho (1 - V)} \leq d _ {H},
$$

and

$$
\max _ {p _ {L} ^ {(2)}} \Pi_ {L} ^ {(2)} \equiv \lambda_ {0} p _ {L} ^ {(2)} (V - V _ {L}),
$$

$$
s. t. \quad \frac {b}{1 - \rho (V - V _ {L})} \leq d _ {L}.
$$

Each one is a non-linear constrained optimization problem with one decision variable and one constraint (due to service-level agreement). If both of the constraints are slack, we can obtain the best response functions from the <sup>fi</sup>rst order conditions as: $p _ { H } ^ { ( 1 ) } =$ $\frac { \gamma ( d _ { L } - d _ { H } ) } { 2 } + \frac { p _ { L } ^ { ( 2 ) } } { 2 }$ and $\begin{array} { r } { p _ { L } ^ { ( 2 ) } = \frac { ( 1 - \gamma d _ { L } ) } { 2 ( 1 - \gamma d _ { H } ) } p _ { H } ^ { ( 1 ) } } \end{array}$ , which then yield:

$$
p _ {L} ^ {(2)} = (1 - \gamma d _ {L}) x _ {1} \mathrm{and} p _ {H} ^ {(1)} = 2 (1 - \gamma d _ {H}) x _ {1}.
$$

Because of our assumption that the QoS guarantees are well separated, if only one of the constraints is binding, it must be the one for the premium service; that for the standard service must be slack. In that case, the best response functions are given by: $\begin{array} { r } { p _ { L } ^ { ( 2 ) } = \frac { ( 1 - \gamma d _ { L } ) } { 2 ( 1 - \gamma d _ { H } ) } p _ { H } ^ { ( 1 ) } } \end{array}$ and $\begin{array} { r } { p _ { H } ^ { ( 1 ) } = \gamma ( d _ { L } - d _ { H } ) \Big ( 1 - \frac { u _ { H } } { \rho } \Big ) + p _ { L } ^ { ( 2 ) } } \end{array}$ . Solving <sup>ð Þ</sup>the two equations simultaneously, we get:

$$
p _ {L} ^ {(2)} = \bigg (1 - \frac {u _ {H}}{\rho} \bigg) (1 - \gamma d _ {L}) x _ {2} \text { and } p _ {H} ^ {(1)} = 2 (1 - \gamma d _ {H}) \bigg (1 - \frac {u _ {H}}{\rho} \bigg) x _ {2}.
$$

Finally, if both the constraints are binding, the optimal prices can be obtained directly from the constraints as:

$$
p _ {L} ^ {(2)} = (1 - \gamma d _ {L}) \left[ 1 - \frac {u _ {H} + u _ {L}}{\rho} \right] \text {   and   } p _ {H} ^ {(1)} = (1 - \gamma d _ {H}) \left[ 1 - \frac {u _ {H} + x _ {3} u _ {L}}{\rho} \right].
$$

In order to complete the proof, the thresholds of ρ can be found by comparing the optimal prices. □

Proof of Proposition 3.1. To prove the existence of $\rho _ { 1 } , \rho _ { 2 } , \rho _ { 3 }$ and the various equilibrium strategies, we need to <sup>fi</sup>nd out where the pro<sup>fi</sup>t functions $\dot { \boldsymbol { \pi } } _ { L } ^ { ( 2 ) }$ and $I I _ { H } , \tilde { H _ { H } ^ { ( 1 ) } }$ and $\Pi _ { L }$ intersect. First, it can be easily veri<sup>fi</sup>ed from Eqs. $( 3 ) , ( 8 )$ , and (9) that these pro<sup>fi</sup>t functions are nondecreasing with $\rho$ because $\begin{array} { r } { \frac { \partial \varPi } { \partial \varDelta o } \geq 0 } \end{array}$ . For simplicity, we assume $4 u _ { H } < \nu _ { 2 } .$ Also note that when $u _ { L } x _ { 3 } > 2 u _ { H } , u _ { H } < \nu _ { 1 } < 2 u _ { H } < u _ { L } < \nu _ { 2 } < 2 u _ { L }$

Let us now look at where $\Pi _ { L } ^ { ( 2 ) }$ and $\Pi _ { H }$ intersect. It is clear that $\varPi _ { L } ^ { ( 2 ) }$ $\vert \rho = u _ { \scriptscriptstyle H } > T _ { \cal H } \vert _ { \rho = u _ { \scriptscriptstyle H } } = 0$ . One can also show that $\Pi _ { L } ^ { ( 2 ) } | _ { \rho = \nu _ { i } } { < } I I _ { H } | _ { \rho = \nu _ { i } } .$ Hence $\Pi _ { L } ^ { ( 2 ) }$ and $\Pi _ { H }$ <sup>fi</sup>rst intersects at $\rho _ { 1 } \in [ u _ { H } , v _ { 1 } ] ,$ , which solves:

$$
\frac {2 x _ {1} ^ {2} (1 - \gamma d _ {L}) \rho_ {1}}{\gamma u _ {H} (d _ {L} - d _ {H})} + \frac {u _ {H}}{\rho_ {1}} = 1.
$$

Solving the above quadratic equation and ignoring the invalid root, we obtain:

$$
\rho_ {1} = \frac {u _ {H} (1 - x _ {3})}{4 x _ {1} ^ {2} x _ {3}} \left[ 1 - \sqrt {1 - \frac {8 x _ {1} ^ {2} x _ {3}}{1 - x _ {3}}} \right].
$$

Since ${ \cal I } { \cal I } _ { H } | _ { \rho = \infty } < { \cal I } { \cal I } _ { L } ^ { ( 2 ) } | _ { \rho = \infty } , { \cal I } { \cal I } _ { L } ^ { ( 2 ) }$ and $\Pi _ { H }$ intersect again. It can be shown that $\Pi _ { H } \vert _ { \rho = 4 u _ { H } } > \Pi _ { L } ^ { ( 2 ) } \vert _ { \rho = 4 u _ { H } } , \boldsymbol { \mathrm S 0 }$ , the second intersection of $\varPi _ { L } ^ { ( 2 ) }$ and $\Pi _ { H }$ occurs at $\rho _ { 2 } { > } 4 u _ { H } .$ . If $\rho _ { 2 } \leq \nu _ { 2 } ,$ , then $\rho _ { 2 }$ solves:

$$
u _ {H} \left(1 - \frac {2 u _ {H}}{\rho_ {2}}\right) = \rho_ {2} x _ {2} ^ {2} \frac {1 - \gamma d _ {L}}{\gamma (d _ {L} - d _ {H})} \left(1 - \frac {u _ {H}}{\rho_ {2}}\right) ^ {2}.
$$

The above equation can be solved; since one of the roots is invalid, we obtain:

$$
\rho_ {2} = u _ {H} + \frac {u _ {H} (1 - x _ {3})}{2 x _ {2} ^ {2} x _ {3}} \left[ 1 + \sqrt {1 - \frac {4 x _ {2} ^ {2} x _ {3}}{1 - x _ {3}}} \right].
$$

I $\mathrm { f } \rho _ { 2 } > \nu _ { 2 } ,$ then $\rho _ { 2 }$ solves:

$$
u _ {H} (1 - \gamma d _ {H}) \bigg (1 - \frac {2 u _ {H}}{\rho_ {2}} \bigg) = u _ {L} (1 - \gamma d _ {L}) \bigg (1 - \frac {u _ {H} + u _ {L}}{\rho_ {2}} \bigg).
$$

From which we can obtain:

$$
\rho_ {2} = \frac {u _ {L} ^ {2} x _ {3} + u _ {L} u _ {H} x _ {3} - 2 u _ {H} ^ {2}}{u _ {L} x _ {3} - u _ {H}}.
$$

To <sup>fi</sup>nd out the intersection of ${ \varPi } _ { H } ^ { ( 1 ) }$ and $\Pi _ { L } .$ . We note that $\Pi _ { H } ^ { ( 1 ) } \big | _ { \rho = u _ { L } } >$ $\Pi _ { L } | _ { \rho , = u _ { L } } = 0$ and $\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad$ . So the only intersection between $I I _ { H } ^ { ( 1 ) }$ and $\boldsymbol { \Pi } _ { L }$ occurs at $\rho _ { 3 } { > } u _ { L } { > } \rho _ { 1 } . \mathrm { I f } \rho _ { 3 } \in [ u _ { L } , \nu _ { 2 } ] ,$ , it solves:

$$
(1 - \gamma d _ {L}) \frac {u _ {L}}{2} \left(1 - \frac {u _ {L}}{\rho_ {3}}\right) = 2 u _ {H} x _ {2} (1 - \gamma d _ {H}) \left(1 - \frac {u _ {H}}{\rho_ {3}}\right).
$$

The above equation yields:

$$
\rho_ {3} = \frac {u _ {L} ^ {2} x _ {3} - 4 u _ {H} ^ {2} x _ {2}}{u _ {L} x _ {3} - 4 u _ {H} x _ {2}}.
$$

$\mathrm { I f } \rho _ { 3 } \in [ \nu _ { 2 } , 2 u _ { L } ] ,$ , it solves:

$$
(1 - \gamma d _ {L}) \frac {u _ {L}}{2} \left(1 - \frac {u _ {L}}{\rho_ {3}}\right) = u _ {H} (1 - \gamma d _ {H}) \left(1 - \frac {u _ {H} + u _ {L} x _ {3}}{\rho_ {3}}\right).
$$

In this case, $\begin{array} { r } { \rho _ { 3 } = \frac { u _ { L } ^ { 2 } x _ { 3 } - 2 u _ { H } ( u _ { H } + u _ { L } x _ { 3 } ) } { u _ { L } x _ { 3 } - 2 u _ { H } } . \operatorname { I f } \rho _ { 3 } \in [ 2 u _ { L } , 4 u _ { L } ] , } \end{array}$ , it solves:

$$
(1 - \gamma d _ {L}) \frac {\rho_ {3}}{8} = u _ {H} (1 - \gamma d _ {H}) \left(1 - \frac {u _ {H} + u _ {L} x _ {3}}{\rho_ {3}}\right).
$$

One of the roots of the above equation is less than $2 u _ { L }$ and hence invalid. Therefore:

$$
\rho_ {3} = \frac {4 u _ {H} + 2 \sqrt {2 u _ {H} [ x _ {3} (u _ {H} - u _ {L} x _ {3}) + 2 u _ {H} (1 - x _ {3}) ]}}{x _ {3}}.
$$

If $\rho _ { 3 } > 4 u _ { L }$ , it solves:

$$
u _ {L} (1 - \gamma d _ {L}) \bigg (1 - \frac {2 u _ {L}}{\rho_ {3}} \bigg) = u _ {H} (1 - \gamma d _ {H}) \bigg (1 - \frac {u _ {H} + u _ {L} x _ {3}}{\rho_ {3}} \bigg).
$$

In this case, we get:

$$
\rho_ {3} = \frac {2 u _ {L} ^ {2} x _ {3} - u _ {H} (u _ {H} + u _ {L} x _ {3})}{u _ {L} x _ {3} - u _ {H}}.
$$

Finally, the equilibrium strategies can be obtained by comparing the pro<sup>fi</sup>ts for the two <sup>fi</sup>rms under different regions. Speci<sup>fi</sup>cally, if $\rho { < } \rho _ { 1 } \ 0 \Gamma \rho _ { 2 } { < } \rho { < } \rho _ { 3 }$ , then $\Pi _ { L } ^ { ( 2 ) } { > } \Pi _ { H }$ and $\Pi _ { H } ^ { ( 1 ) } { > } \Pi _ { l }$ and providers would choose differentiated service. If $\rho _ { 1 } { < } \rho { < } \rho _ { 2 } ,$ then $\Pi _ { L } ^ { ( \bar { 2 } ) } { < } \Pi _ { H }$ and both providers would choose the premium service. $\mathrm { I f } \rho { > } \rho _ { 3 } ,$ then $\Pi _ { H } ^ { ( 1 ) } { < } \Pi _ { L }$ and both providers would choose the standard service.

Proof of Lemma 4.1. The follower's optimization problem can be written as:

$$
\begin{array}{l l} \underset {p _ {H} ^ {\text {(follower)}}} {\max} & \Pi_ {H} ^ {\text {(follower)}} \equiv \lambda_ {0} p _ {H} ^ {\text {(follower)}} \left[ 1 - \frac {p _ {H} ^ {\text {(follower)}} - p _ {L} ^ {\text {(leader)}}}{\gamma (d _ {L} - d _ {H})} \right], \\ \text {s.t.} & \frac {b}{1 - \rho \left[ 1 - \frac {p _ {H} ^ {\text {(follower)}} - p _ {L} ^ {\text {(leader)}}}{\gamma (d _ {L} - d _ {H})} \right]} \leq d _ {H}, \end{array}
$$

If the capacity constraint for the follower is slack, the best response can be obtained from the <sup>fi</sup>rst order condition as: $p _ { H } ^ { ( \mathrm { f o l l o w e r } ) } =$ $\begin{array} { r } { \underline { { \hat { p } _ { L } ^ { ( \mathrm { l e a d e r } ) } + \gamma ( d _ { L } - d _ { H } ) } } . } \end{array}$ otherwise, the best response for the follower can be directly obtained from the capacity constraint as: $p _ { H } ^ { ( \mathrm { f o l l o w e r } ) } =$ $\begin{array} { r } { p _ { L } ^ { ( \mathrm { l e a d e r } ) } + \smile \gamma ( d _ { L } - d _ { H } ) \Bigl ( 1 - \frac { u _ { H } } { \rho } \Bigr ) } \end{array}$ □

Proof of Lemma 4.2. The optimal prices can be obtained using backward induction. If $p _ { H } ^ { ( \mathrm { f o l l } ^ { \bullet } ) } = \frac { \dot { p } _ { L } ^ { ( \mathrm { l e a d e r } ) } + \gamma ( d _ { L } - d _ { H } ) } { 2 }$ , the leader's optimization problem can be written as: 2

$$
\begin{array}{l l} \max _ {p _ {L} ^ {(\text { leader })}} & \Pi_ {L} ^ {(\text { leader })} \equiv \lambda_ {0} p _ {L} ^ {(\text { leader })} \left(\frac {1}{2} - \frac {p _ {L} ^ {(\text { leader })}}{2 \gamma (d _ {L} - d _ {H})} - \frac {p _ {L} ^ {(\text { leader })}}{1 - \gamma d _ {L}}\right), \\ s. t. & \frac {1}{2} - \frac {p _ {L} ^ {(\text { leader })}}{2 \gamma (d _ {L} - d _ {H})} - \frac {p _ {L} ^ {(\text { leader })}}{1 - \gamma d _ {L}} \leq \frac {u _ {L}}{\rho}. \end{array}
$$

The constraint of the standard-service provider (the leader) will be slack, and the optimal price can be solved from the <sup>fi</sup>rst order condition as: $p _ { L } ^ { ( \mathrm { l e a d e r } ) } = ( \dot { 1 } - \gamma d _ { L } ) \frac { x _ { 2 } } { 2 }$

I $\begin{array} { r } { \mathsf { f } p _ { H } ^ { ( \mathsf { f } _ { 0 } \mathrm { l l o w e r } ) ^ { s } } = p _ { L } ^ { ( \mathrm { l e a d e r } ) } + \gamma ( \mathsf { \ddot { d } } _ { L } - \mathsf { d } _ { H } ) \Big ( 1 - \frac { u _ { H } } { \rho } \Big ) } \end{array}$ , the leader's optimization problem simpli<sup>fi</sup>es to:

$$
\begin{array}{l l} \max _ {p _ {L} ^ {\text {(leader)}}} & \Pi_ {L} ^ {\text {(leader)}} \equiv \lambda_ {0} p _ {L} ^ {\text {(leader)}} \left(1 - \frac {u _ {H}}{\rho} - \frac {p _ {L} ^ {\text {leader}}}{1 - \gamma d _ {L}}\right), \\ s. t. & 1 - \frac {u _ {H}}{\rho} - \frac {p _ {L} ^ {\text {(leader)}}}{1 - \gamma d _ {L}} \leq \frac {u _ {L}}{\rho}. \end{array}
$$

The optimal price can be obtained as:

$$
p _ {L} ^ {\text {(leader)}} = (1 - \gamma d _ {L}) \max \left\{\frac {1}{2} - \frac {u _ {H}}{2 \rho}, 1 - \frac {u _ {L} + u _ {H}}{\rho} \right\}.
$$

The follower's optimal price $p _ { H } ^ { ( \mathrm { f o l l o w e r } ) }$ can be obtained by substituting $p _ { L } ^ { ( \mathrm { l e a d e r } ) }$ □

Proof of Lemma 4.3. It is clear from Eqs. (10) and (11) and (5) and (6) that under high traf<sup>fi</sup>c, the Stackelberg prices are exactly the same prices as the simultaneous ones. We can also show that $\frac { 1 } { 2 } > x _ { 2 } > 2 x _ { 1 }$ since $1 - \gamma d _ { L } > 0 .$ . Therefore $p _ { L } ^ { ( \mathrm { l e a d e r } ) } \ge p _ { L } ^ { ( 2 ) }$

In addition, $\frac { 1 } { 2 } > x _ { 2 }$ implies that $\frac { 1 } { 2 ( 1 - x _ { 2 } ) } > 2 x _ { 2 }$ . Finally,

$$
(3 + \gamma d _ {L} - 4 \gamma d _ {H}) ^ {2} = [ 1 + \gamma d _ {L} - 2 \gamma d _ {H} + 2 (1 - \gamma d _ {H}) ] ^ {2} > 8 (1 + \gamma d _ {L} - 2 \gamma d _ {H}) (1 - \frac {\Pi_ {L}}{\gamma d _ {H}}) | _ {\rho = u _ {L}}
$$

Hence

$$
\frac {3 + \gamma d _ {L} - 4 \gamma d _ {H}}{4 (1 + \gamma d _ {L} - 2 \gamma d _ {H}) (1 - \gamma d _ {H})} > \frac {2}{3 + \gamma d _ {L} - 4 \gamma d _ {H}} \Rightarrow \frac {3 x _ {2}}{4 (1 - x _ {1})} > 2 x _ {1}.
$$

This means $p _ { H } ^ { ( \mathrm { f o l l o w e r } ) } \geq p _ { H } ^ { ( 1 ) } .$

Proof of Lemma 4.4. In this case, the follower's optimization problem is given by:

$$
\begin{array}{l l} \max _ {p _ {L} ^ {\text {(follower)}}} & \Pi_ {L} ^ {\text {(follower)}} \equiv \lambda_ {0} p _ {L} ^ {\text {(follower)}} \left[ \frac {p _ {H} ^ {\text {(leader)}} - p _ {L} ^ {\text {(follower)}}}{\gamma (d _ {L} - d _ {H})} - \frac {p _ {L} ^ {\text {(follower)}}}{1 - \gamma d _ {L}} \right], \\ s. t. & \frac {b}{1 - \rho \left[ \frac {p _ {H} ^ {\text {(leader)}} - p _ {L} ^ {\text {(follower)}}}{\gamma (d _ {L} - d _ {H})} - \frac {p _ {L} ^ {\text {(follower)}}}{1 - \gamma d _ {L}} \right]} \leq d _ {L}. \end{array}
$$

Depending on whether the capacity constraint is binding, the follower's best response can be derived as: $p _ { L } ^ { ( \mathrm { f o l l o w e r } ) } = \mathrm { m a x } \Big \{ \frac { x _ { 3 } } { 2 } p _ { H } ^ { ( \mathrm { l e a d e r } ) }$ ， $x _ { 3 } p _ { H } ^ { ( \mathrm { l e a d e r } ) } - { \frac { \gamma ( d _ { L } - \mathrm { \hat { d } } _ { H } ) u _ { L } x _ { 3 } } { \rho } } \}$ □

Proof of Lemma 4.5. If $\begin{array} { r } { p _ { L } ^ { ( \mathrm { f o l l o w e r } ) } = \frac { p _ { H } ^ { ( \mathrm { l e a d e r } ) } ( 1 - \gamma d _ { L } ) } { 2 ( 1 - \gamma d _ { H } ) } } \end{array}$ , the leader's opti mization problem becomes:

$$
\begin{array}{l l} \max _ {p _ {H} ^ {(\text { leader })}} & \Pi_ {H} ^ {(\text { leader })} \equiv \lambda_ {0} p _ {H} ^ {(\text { leader })} \left[ 1 - \frac {1}{2 (1 - \gamma d _ {H}) x _ {2}} p _ {H} ^ {(\text { leader })} \right], \\ s. t. & 1 - \frac {1}{2 (1 - \gamma d _ {H}) x _ {2}} p _ {H} ^ {(\text { leader })} \leq \frac {u _ {H}}{\rho}. \end{array}
$$

The optimal price is given by:

$$
p _ {H} ^ {\text {(leader)}} = (1 - \gamma d _ {H}) x _ {2} \max \left\{1, 2 \left(1 - \frac {u _ {H}}{\rho}\right) \right\}.
$$

If $p _ { L } ^ { ( \mathrm { f o l l o w e r } ) } = x _ { 3 } \left\lceil p _ { H } ^ { ( \mathrm { l e a d e r } ) } - \frac { \gamma ( d _ { L } - d _ { H } ) u _ { L } } { \rho } \right\rceil$ , the leader's optimization problem becomes:

$$
\begin{array}{l l} \max _ {p _ {H} ^ {\text {(leader)}}} & \varPi_ {H} ^ {\text {(leader)}} \equiv \lambda_ {0} p _ {H} ^ {\text {(leader)}} \left(1 - \frac {p _ {H} ^ {\text {(leader)}}}{1 - \gamma d _ {H}} - \frac {x _ {3} u _ {L}}{\rho}\right), \\ s. t. & 1 - \frac {p _ {H} ^ {\text {(leader)}}}{1 - \gamma d _ {H}} - \frac {x _ {3} u _ {L}}{\rho} \leq \frac {u _ {H}}{\rho}. \end{array}
$$

Here, the constraint of the premium service will be binding, and the optimal price is solved from the constraint as:

$$
p _ {H} ^ {\text {(leader)}} = (1 - \gamma d _ {H}) \left(1 - \frac {u _ {H} + x _ {3} u _ {L}}{\rho}\right).
$$

Proof of Proposition 4.1. The proof of the sequential equilibria is similar to Proposition 3.1. The computation of the thresholds $\rho _ { 4 } , \rho _ { 5 }$ and $\rho _ { 6 } ,$ however, is mathematically cumbersome. We note that when $I I _ { L } ^ { ( \mathrm { f o i l o w e r } ) } { > } I I _ { H }$ and $\Pi _ { H } ^ { ( \mathrm { l e a d e r } ) } { > } \mathrm { m a x } \{ \Pi _ { L } ^ { ( \mathrm { l e a d e r } ) } , ~ \Pi _ { L } \}$ , the leader would choose premium service while the follower the standard service. This means $\rho _ { 4 } \in [ \rho _ { H } , 2 u _ { H } ]$ . Its existence is assured because $\begin{array} { r } { { \cal I } _ { L } ^ { ( \mathrm { f o l l o w e r } ) } | _ { \rho = } - } \end{array}$ $\begin{array} { r } { u ^ { H } { > } \Pi _ { H } \big | _ { \rho = u _ { H } } } \end{array}$ and $\Pi _ { L } ^ { ( \mathrm { f o l l o w e r } ) } | _ { \rho = \nu _ { 5 } } < \Pi _ { H } | _ { \rho = \nu _ { 5 } }$

When $I I _ { H } { > } I I _ { L } ^ { ( \mathrm { f o l l o w e r } ) }$ and $\Pi _ { H } { > } \mathrm { m a x } \{ I I _ { L } ^ { \mathrm { ( l e a d e r ) } } , ~ \Pi _ { L } \}$ , both providers would choose premium service. These set of conditions ensure the existence o $\mathrm { \Delta } \rho _ { 5 } { > } 2 u _ { H } { > } \rho _ { 4 }$ because $\Pi _ { L } ^ { ( \mathrm { l e a d e r } ) } | _ { \rho = 2 u _ { H } } { < } \Pi _ { H } | _ { \rho = 2 u _ { H } }$ and $\quad I I _ { L } ^ { ( \mathrm { l e a d e r } ) } | _ { \rho = \infty ^ { - } }$ $\Pi ^ { H } \big | _ { \rho = \infty }$

$\begin{array} { r } { \stackrel { \mathrm { \tiny ~ \wedge p - ~ \infty ~ } } { \mathrm { W h e n } } \ : \boldsymbol { \Pi } _ { H } ^ { \mathrm { ( f o l l o w e r ) } } > \boldsymbol { \Pi } _ { L } \mathrm { ~ a n d ~ } \boldsymbol { \Pi } _ { L } ^ { \mathrm { ( l e a d e r ) } } > \mathrm { m a x } \{ \boldsymbol { \Pi } _ { H } ^ { \mathrm { ( l e a d e r ) } } , \boldsymbol { \Pi } _ { H } \} } \end{array}$ , the leader would choose standard service while the follower the premium service. We can then obtain $\rho _ { 6 } { > } u _ { L } { > } 2 u _ { H } { > } \rho _ { 4 }$ because $\begin{array} { r } { \Pi _ { H } ^ { \mathrm { ( f o l l o w e r ) } } \vert _ { \rho = u _ { L } } > } \end{array}$ Π<sub>L</sub>|<sub>ρ= u</sub> and $\Pi _ { H } ^ { ( \mathrm { f o l l o w e r } ) } \vert _ { \rho = \infty } \dot { < } \bar { I } I _ { L } \vert _ { \rho = \infty } ^ { - }$ Þ<sup>H</sup> <sup>: L</sup> Finally when γd Finallywhen $\rho { > } \rho _ { 6 } , \Pi _ { L } { > } \Pi _ { H } ^ { \mathrm { ( f o l l o w e r ) } }$ and and $\Pi _ { L } { > } \mathrm { m a x } \{ I I _ { H } ^ { \mathrm { ( l e a d e r ) } } , ~ \Pi _ { H } \}$ hence both providers bene<sup>fi</sup>t by choosing standard service. □

Proof of Proposition 5.1. When providers choose differentiated service, we can re-write, after substituting the demand, the optimization problems as:

$$
\max _ {p _ {H} ^ {(1)}} \Pi_ {H} ^ {(1)} = \lambda_ {0} \left[ 1 - \frac {p _ {H} ^ {(1)} - p _ {L} ^ {(2)}}{\gamma (d _ {L} - d _ {H})} \right] \left(p _ {H} ^ {(1)} - c\right) - \frac {c}{d _ {H}},
$$

and

$$
\max _ {p _ {L} ^ {(2)}} \Pi_ {L} ^ {(2)} = \lambda_ {0} \left[ \frac {p _ {H} ^ {(1)} - p _ {L} ^ {(2)}}{\gamma (d _ {L} - d _ {H})} - \frac {p _ {L} ^ {(2)}}{1 - \gamma d _ {L}} \right] \left(p _ {L} ^ {(2)} - c\right) - \frac {c}{d _ {L}}.
$$

Simplifying the <sup>fi</sup>rst order conditions and solving for $p _ { H } ^ { ( 1 ) }$ and $p _ { L } ^ { ( 2 ) }$ , we get

$$
p _ {H} ^ {(1)} = \frac {(1 - \gamma d _ {H}) [ 3 c + 2 \gamma (d _ {L} - d _ {H}) ]}{3 + \gamma d _ {L} - 4 \gamma d _ {H}}
$$

and

$$
p _ {L} ^ {(2)} = \frac {c (3 - 2 \gamma d _ {H} - \gamma d _ {L}) + \gamma (d _ {L} - d _ {H}) (1 - \gamma d _ {L})}{3 + \gamma d _ {L} - 4 \gamma d _ {H}}.
$$

The optimal capacity can be found by substitution of the above prices. Finally the proof can be completed by <sup>fi</sup>nding the upper limit ¯¯c and $\bar { \lambda } _ { 0 } .$ This can be achieved by setting $b _ { j } ^ { ( i ) } > 0$ and $\overline { { I I _ { j } ^ { ( i ) } } } > \dot { 0 }$ □

## References

[1] P. Ahluwalia, U. Varshney, Composite quality of service and decision making perspectives in wireless networks, Decision Support Systems 46 (2) (2009) 542–551.

[2] G. Allon, A. Federgruen, Competition in service industries, Operations Research 55 (1) (2007) 37–55.

[3] M. Armony, M. Haviv, Price and delay competition between two service providers, European Journal of Operational Research 147 (1) (2003) 32–50.

[4] D. Bachlechner, K. Siorpaes, D. Fensel, I. Toma, Web service discovery—a reality check. Digital Enterprise Research Institute, Technical Report, 2006.

[5] G. Biglaiser, C. Ma, Price and quality competition under adverse selection: market organization and ef<sup>fi</sup>ciency, Rand Journal of Economics 34 (2) (2003) 266–286.

[6] P.C. Cachon, P.T. Harker, Competition and outsourcing with scale economies, Management Science 48 (10) (2002) 1314–1333.

[7] C.J. Choi, H.S. Shin, A comment on a model of vertical product differentiation, The Journal of Industrial Economics 40 (2) (1992) 229–231.

[8] A. de Palma, L. Leruth, Congestion and game in capacity: a duopoly analysis in the presence of network externalities, Annales d'Economie et de Statistique 0 (15–16) (1989) 389–407.

[9] S. Dewan, H. Mendelson, User delay costs and internal pricing for a service facility, Management Science 36 (12) (1990) 1502–1517.

[10] S. Essegaier, S. Gupta, Z. Zhang, Pricing access service, Marketing Science 21 (2) (2002) 139–159.

[11] N. Economides, Quality variations and maximal variety differentiation, Regional Science and Urban Economics 19 (1) (1989) 21–29.

[12] J. Gabszewicz, J.-F. Thisse, Price competition, quality and income disparities, Journal of Economic Theory 20 (1979) 340–359.

[13] R. Gibbens, R. Mason, R. Steinberg, Internet service classes under competition, IEEE Journal on Selected Areas in Communications 18 (12) (2000) 2490–2498.

[14] A. Gupta, D.O. Stahl, A.B. Whinston, A stochastic equilibrium model of internet pricing, Journal of Economic Dynamics and Control 21 (1997) 697–722.

[15] N.J. Keon, G. Anandalingam, Optimal pricing for multiple services in telecommunications networks offering quality of service guarantees, IEEE/ACM Transactions on Networking 11 (2003) 66–80

[16] J. Kerstetter, So, What the heck are web services, Business Week, 2005, URL: www. businessweek.com/technology/content/feb2005/tc2005028\_8000\_tc203.htm.

[17] J.B. Kim, A. Segev, A web services-enabled marketplace architecture for negotiation process management, Decision Support Systems 40 (1) (2005) 81–87.

[18] L. Kleinrock, Queueing systems, Computer Applications, vol. II, John Wiley & Sons, New York, NY, 1976.

[19] D. Levhari, I. Luski, Duopoly pricing and waiting lines, European Economic Review 11 (1) (1978) 17–35.

[20] L. Li, Y.S. Lee, Pricing and delivery-time performance in a competitive environment, Management Science 40 (5) (1994) 633–646.

[21] Z. Lin, S. Ramanathan, H. Zhao, Usage-based dynamic pricing of web services for optimizing resource allocation, Journal of Information Systems and E-Business 3 (2005) 221–242

[22] H. Ludwig, A. Keller, A. Dan, R.P. King, R. Franck, Web Service Level Agreement Language Speci<sup>fi</sup>cation, IBM T.J. Watson Research Center, 2003.

[23] J.K. MacKie-Mason, H.R. Varian, Economic FAQs about the internet, The Journal of Economic Perspectives 8 (3) (1994) 75–96.

[24] J.K. MacKie-Mason, H.R. Varian, Pricing the internet, in: B. Kahin, J. Keller (Eds.), Public Access to the Internet, MIT Press, Cambridge, MA, 1995.

[25] A. Mani, A. Nagarajan, Understating quality of service for web services, 2002 URL: http://www-128.ibm.com/developerworks/webservices/library/ws-quality.html.

[26] Y. Masuda, S. Whang, Dynamic pricing for network service: equilibrium and stability, Management Science 45 (6) (1999) 857–869.

[27] D.A. Menascé, Response-time analysis of composite web services, IEEE Internet Computing 8 (1) (2004) 90–92.

[28] H. Mendelson, Pricing computer services: queueing effects, Communications of the ACM 28 (3) (1985) 312–321.

[29] H. Mendelson, Economies of scale in computing: Grosch's law revisited, Communications of the ACM 30 (12) (1987) 1066–1072

[30] H. Mendelson, S.J. Whang, Optimal incentive-compatible priority pricing for the M/M/1 queue, Operations Research 38 (5) (1990) 870–883.

[31] K.S. Moorthy, Product and price competition in a duopoly, Marketing Science 7 (2) (1988) 141–168.

[32] J. Myerson, Use SLA in a web services context, IBM DeveloperWorks, 2004, URL: http://www-128.ibm.com/developerworks/library/ws-sla/.

[33] D. Neven, J.F. Thisse, On quality and variety competition, in: J.J. Gabszewicz, J.-F. Richard, L.A. Wolsey (Eds.), Economic Decision Making: Games, Econometrics and Optimization, Amsterdam, North-Holland, 1990.

[34] M.P. Papazoglou, D. Georgakopoulos, Service oriented computing, Communications of the ACM 46 (10) (2003) 24–28.

[35] A. Paschke, M. Bichler, Knowledge representation concepts for automated SLA management, Decision Support Systems 46 (1) (2008) 187–205.

[36] T. Pilioura, S. Hadjiefthymiades, A. Tsalgatidou, M. Spanoudakis, Using web services for supporting the users of wireless devices, Decision Support Systems 43 (1) (2007) 77–94.

[37] S. Ross, Introduction to Probability Models, Academic Press, Boston, MA, 1993.

[38] J.Y. Sayah, L.-J. Zhang, On demand business collaboration enablement with web services, Decision Support Systems 40 (1) (2005) 107–127.

[39] M. Scharf, On the response time of large-scale composite web services, Proceedings of the 19th International Teletraf<sup>fi</sup>c Congress, Beijing, China, 2005.

[40] A. Shaked, J. Sutton, Relaxing price competition through product differentiation, Review of Economic Studies 49 (1982) 3–13.

[41] R. Simon, W.S. Chang, B. Jukic, Network path pricing: a QoS-based model, Proceedings of 8th International Symposium on Modeling, Analysis, and Simulation of Computer and Telecommunication Systems, 2000, pp. 457–465, San Francisco, CA.

[42] K. So, Price and time competition for service delivery, Manufacturing Service and Operations Management 2 (4) (2000) 392–409.

[43] Y. Sun, S. He, J.Y. Leu, Syndicating web services: a QoS and user-driven approach, Decision Support Systems 43 (1) (2007) 243–255.

[44] Q. Tang, H.K. Cheng, Optimal location and pricing of web services intermediary, Decision Support Systems 40 (1) (2005) 129–141.

[45] J. Tirole, The Theory of Industrial Organization, MIT Press, Cambridge, MA, 1989

[46] M.B. Vandenbosch, C.B. Weinberg, Product and price competition in a twodimensional vertical differentiation model, Marketing Science 14 (2) (1995) 224-249.

[47] X. Wauthy, Quality choice in models of vertical differentiation, Journal of Industrial Economics 44 (3) (1996) 345–353.

[48] T. Yu, K. Lin, The design of QoS broker algorithms for QoS-capable web services, International Journal of Web Services Research 1 (4) (2004) 33–50.

[49] Z. Zhang, D. Dey, Y. Tan, Pricing communication services with delay guarantee, Informs Journal on Computing 19 (2) (2007) 248–260.

[50] Z. Zhang, D. Dey, Y. Tan, Pricing and QoS competition in communication services, European Journal of Operational Research 186 (2) (2008) 681–693.

[51] J.L. Zhao, H.K. Cheng, Web services and process management: a union of convenience or a new area of research? Decision Support Systems 40 (1) (2005) 1–8.

[52] M. zur Muehlen, J.V. Nickerson, K.D. Swenson, Developing web services choreography standards—the case of REST vs, SOAP. Decision Support Systems 40 (1) (2005) 9–29.
