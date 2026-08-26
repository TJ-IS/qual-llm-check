---
otero_id: 15130
otero_key: "T9WQP86F"
title: "Matching intermediaries for information goods in the presence of direct search: an examination of switching costs and obsolescence of information"
authors: "Manish Agrawal; Govind Hariharan; Rajiv Kishore; H.R. Rao"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.05.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Matching intermediaries for information goods in the presence of direct search: an examination of switching costs and obsolescence of information

Manish Agrawal<sup>a,\*</sup>, Govind Hariharan<sup>b</sup>, Rajiv Kishore<sup>c</sup>, H.R. Rao<sup>c</sup>

<sup>a</sup>Department of Information Systems and Decision Sciences, College of Business Administration, University of South Florida 4202, E. Fowler Avenue, CIS 1040, Tampa, FL 33620, United States <sup>b</sup>Kennesaw State University, Kennesaw, GA 30144, United States <sup>c</sup>University at Buffalo, Amherst, NY 14260, United States

Received 6 June 2003; received in revised form 7 May 2004; accepted 8 May 2004 Available online 17 June 2004

## Abstract

This paper investigates patterns of revenues earned by an intermediary that matches buyers and sellers in the presence of direct search markets. We develop a theoretical structure and a computer simulation model of such a marketplace where vendors are horizontally differentiated, and an intermediary matches clients to the optimal vendor for a fee. The model is applicable to information services such as application service providers (ASPs). The contribution of this paper is the identification of scenarios under which intermediaries that match clients and vendors are likely to be profitable considering switching costs and obsolescence of information.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Electronic intermediary; Information economics; Simulation; Search

## 1. Introduction

Intermediaries are entities (computational, human or organizational) that can be utilized as a bridge on an information stream between separate (perhaps distinct or even incompatible) entities to tailor, customize, personalize, or otherwise extend functions as the information flows along the stream [3]. Electronic intermediaries and exchanges are a relatively recent business service model aimed at leveraging the benefits of the Internet by bringing together large numbers of buyers and sellers and facilitating transactions between them [1,12]. Their promise has led to the creation of many intermediaries in the recent past, though few have survived. The failure of such a large number of public exchanges in spite of the promise of the business model suggests that research is needed to identify scenarios where intermediaries may profitably add value for buyers and sellers [33]. This research is a step in that direction. We examine intermediation scenarios where the goods and services traded may be classified as information goods to identify cases where intermediaries may be profitable.

A distinguishing feature of information services is that the marginal cost of production, differentiation and transportation and of serving additional customers is very low and often close to 0 [30]. These properties considerably simplify our analysis and help us focus exclusively on the matching properties of intermediation, while still considering a very realistic scenario [23]. Examples of information service providers are as diverse as Application Service Providers (ASPs), travel systems like SABRE and financial services. In each of these cases, there are many providers offering essentially similar services [10,34]. Though the existence of numerous providers is generally beneficial to users and indicates a competitive market, their existence implies that in choosing a service provider, clients have to evaluate a large number of providers, making search an important and potentially expensive issue [13,15,22].

The aim of this paper is to investigate potential revenue patterns for intermediaries that provide matching services for buyers and sellers of information services. We consider an information services marketplace with one intermediary that has perfect knowledge about the characteristics of vendors and clients and provides matching services. The intermediary exists alongside a direct search market. All clients have the same willingness to pay for services while vendors are horizontally differentiated. This implies that each client may have its own preference for the ideal vendor. Vendors participate in both the mediated and direct markets but each client maximizes its utility from trade by choosing either the intermediary or direct search. The intermediary earns revenues through the fees it receives from its clients. We use a computer simulation test bed to introduce clients, vendors, and the intermediary into the marketplace and compute the resulting intermediary revenues. We also examine the consequences of consumption of services by clients during search on intermediary revenues. To model the fact that clients may start with some prior knowledge of the market, we examine the impact of client experience from repeated search on intermediary revenues. For each case, we consider different sizes of the vendor population and examine the intermediary’s revenue maximizing fee.

The contributions of the paper are as follows. In the context of information services, the paper identifies the impact of direct search markets and changing fees on the profitability of matching intermediaries. We also consider the impact of clients’ knowledge of the marketplace on the intermediary’s profits. Finally, we look at the influence of the industry in which the intermediary operates, specifically the rate at which the information gathered by clients in earlier searches loses fidelity in representing the distribution of vendors in the marketplace.

The paper is organized as follows. Section 2 reviews the research on intermediaries and search. Section 3 describes our basic research model and the research context of information services. In Section 4, we describe the simulations and consider changes in the pricing policy of the intermediary under different conditions of direct search. Specifically, we consider random search, search with and without consumption and the impact of search experience. Finally, Section 5 concludes the paper with a discussion of the results and ideas to extend this research.

## 2. Prior research

This research develops a model to compare the utility received by clients from matching services provided by an intermediary when the alternative is direct search. This section summarizes results from prior research on intermediaries and search models that are used in building our model.

## 2.1. Intermediaries

Intermediaries can play many roles in a marketplace. A familiar scenario is a market maker that increases the likelihood of completing transactions [24]. Rubinstein and Wolinsky [27] examined intermediaries as market makers when both buyers and sellers had the option of transacting directly with each other or through the intermediary. The intermediary bought products from sellers and sold them to buyers, choosing a buy price and sell price that maximized its profits. Its competitive advantage was based on the greater likelihood of a customer meeting an intermediary than a seller. In this formulation, the intermediary’s profits were explained by the time-consuming nature of direct trade, which allowed the intermediary to extract some surplus for providing immediacy in matching demand.

The distinction between market makers and match makers was first clarified by Yavas [37]. Market makers correspond to the traditional definition of intermediaries such as retailers who set buy and sell prices to trade on their own account. This creates the bid–ask spread in financial markets and inventory markup in retailing [8]. Their primary service is immediacy [9,37]. This service becomes particularly important when there is some uncertainty in levels of demand and supply and market makers use their pricing policies to maintain inventories [8,31]. Match makers on the other hand do not buy or sell but simply match two parties. Examples of market makers include used-car dealers and examples of match makers include real-estate brokers. It has been shown that market making is more profitable than match making when the valuations of buyers and sellers are common knowledge. However, when the valuations are private information, match making is more profitable and yields higher welfare when search is relatively inefficient and costly. It has also been shown that the presence of an intermediary reduces the equilibrium search intensities of both sellers and buyers [37].

Bakos [2] examined the implications of a reduction in search costs by the use of electronic marketplaces and suggested that commodity markets could move closer to Walrasian markets which assume that buyers are costlessly and fully informed about sellers. Assuming that buyers start with the knowledge of distribution of seller prices, he found that by reducing search costs, electronic markets could prevent market failures in differentiated markets. Also, by emphasizing product information over price information using such intermediaries, sellers could maintain profits.

The role of an intermediary considered in this research is that of a match maker that facilitates search. This is appropriate because buyers have private values for a number of information services. To decide which market to participate in, consumers compare the utility of an intermediary’s match making services with the expected utility from direct search. In the initial model, clients start with no prior knowledge of the distribution of vendor offerings. In later models, we extend our model to examine the influence of client’s prior information.

## 2.2. Search

The theory of consumer search was introduced by Stigler [32] to explain the observed dispersion of prices in markets. Kohn and Shavell [14] summarized some of the early results regarding search rules. Search is generally seen as sequential sampling from a population where the samples could be prices, product features, etc. Consumers engaged in search are generally assumed to have a probability distribution for samples over the population, which could be known with certainty or could be uncertain and subject to revision in light of new information [36]. In general, the expected utility maximizing decision rule takes the form of a switch point utility level s. Search ends if the best available utility exceeds s and continues otherwise. When the distribution is uncertain, s could change as new samples are drawn. When current costs become relatively more important than future benefits, for example when risk aversion or discount rate increases, the switch point level falls, resulting in reduced search. The switch point also falls as search costs increase, again reducing the level of search [14].

When clients do not start with prior information about the distribution of vendors in the marketplace, the switch point in the search rule can in general only be characterized in terms of a functional equation that is impossible to solve explicitly [14]. Rothschild [26] showed that dynamic programming can be used to describe the optimal search rule in terms of the searcher’s current beliefs even from unknown distributions. Essentially, search stops when the sampled value is superior to the best-expected utility at the time of sampling after considering search costs. This rule also generally satisfies the switch point feature described by Kohn and Shavell [14]. Rothschild’s search rule is the basis of the direct search model in this paper.

Though search rules in the literature are generally based on sequential sampling [20], another possible search mechanism is based on obtaining all samples at once. This is called the fixed-sample-size (FSS) search strategy. FSS search and sequential search may be considered special cases of a general search strategy in which the searcher obtains more than one sample at a time and then has to decide how many more times to sample [17]. FSS and sequential searches each have their advantages and disadvantages. FSS search allows information to be gathered quickly, though it may lead to overinvestment in information-gathering. Sequential search avoids unnecessary information-gathering costs but is slow in gathering the information [21]. It is therefore suggested that optimal search should combine the speed of information-gathering provided by FSS search with the flexibility provided by sequential search to avoid unnecessary costs. The important result for our research is that optimal search reduces to sequential search under certain conditions. Specifically, optimal search reduces to sequential search if the search problem has no decision horizon; the searcher enjoys full recall and has no rate of time preference [21]. In the real world, the decision horizon cannot be indefinite. However, as long as the search is based on careful evaluation, we consider the decision horizon to be long enough to make sequential search appropriate to our analysis. We have therefore used sequential search in our model.

Sequential search has also been used extensively in other related applications in the IS literature on gathering information in order to make decisions [19]. For example, distributed problem solving has been modeled as sequential information-gathering and communication, followed by the final decision [7]. The task of designing inductive expert systems to classify objects based on their description has also been viewed as a problem of developing an optimal sequential information acquisition strategy [18].

## 3. Basic model

Commercial transactions involve a search by clients for services and vendors, followed by negotiations and final delivery of services over the contract period (for example, in <sup>b</sup>The Sourcing Life-Cycle<sup>Q</sup>, 6/ 26/2000, The Gartner group calls it the sourcing life cycle in the context of Information Services) [11].

Since the matching role of intermediaries is related to search, we focus our attention on search and develop progressively complete models of direct search in an information services marketplace and examine intermediary revenues for the different cases considered. We utilize the result from prior research that under full recall, no time preference and long decision horizons, optimal search reduces to sequential search.

As already described, this paper examines the role of matching intermediaries in the specific context of information services. Information services have minimal marginal costs of serving additional customers [30]: they also have low to negligible marginal costs of production, differentiation and transportation. We use these properties to simplify our model and focus on the matching properties of intermediation.

Matching is trivial if clients and vendors are identical. However, goods and services in any marketplace are generally differentiated along characteristics such as features, price, availability, information, support, etc. This differentiation could be either horizontal or vertical [35]. Horizontal differentiation applies to cases where the optimal product choice at equal prices depends upon the particular consumer. There are no good or bad services. Instead, whereas consumer A may prefer service X over service Y, consumer B may prefer service Y over service X. Vertical differentiation applies to cases where all consumers agree over the most preferred set of characteristics and over the preference ordering among services. An example of vertical differentiation is quality. Though a consumer may choose to buy a service of inferior quality based on budget constraints, most consumers agree that higher quality is preferable to lower quality.

We consider horizontal differentiation to be the appropriate choice for information services, as clients may prefer vendors on many criteria including geographical location, references and service features. We therefore examine a market where a population of clients is interested in identifying an optimal provider from a horizontally differentiated population of vendors.

There are two models commonly used to study horizontal differentiation [35]. In the linear model, vendors are assumed to be located at different points on a straight line. In the circular model, vendors are located around a circular city. The straight line model is convenient to use while considering a market with two vendors. However, when considering a large number of vendors in a market, the circular model is more tractable. Since our model can have a potentially large number of vendors, we used the circular model using Salop’s circle where the product space is the circumference of a unit-circle [28].

The circular model of product differentiation was introduced to study the location of services by vendors. Consumers are assumed to be located uniformly on a circle with perimeter 1. Consumers buy one unit of a product or service and face constant transport costs in using the service. Following the general horizontal differentiation model, every vendor is assumed to be located at exactly one point on the circle, which defines its product specifications, and to charge the same price for its services. Vendors are selected based on the <sup>b</sup>match<sup>Q</sup> between their service specifications and the optimal specifications of each client. Transport costs may also be considered as the costs associated with the mismatch between desired and received service specifications for clients. In Fig. 1, we show six vendors located around the circle. Since we consider a horizontally differentiated marketplace, all clients are characterized by a type $u ,$ which is the price they are willing to pay for the service, and an ideal service specification $l _ { i } ^ { * } .$ , where i is the label for clients. The horizontally differentiated vendors charge $P _ { \mathrm { { V } } }$ for each unit of their service and are characterized by the specifications $l _ { j }$ of their service, where $j$ is the label for vendors. The distribution of clients and vendors in this product space makes the services imperfect substitutes. This eliminates price competition where each client selects vendors based exclusively on price.

A population of clients seeking services, vendors providing these services and one intermediary enter the market at a certain time, labeled as 0 in Fig. 2. Each client buys one unit of a service from a vendor that maximizes its expected utility net of costs. The client chooses either direct search or mediated search to maximize its expected utility. In mediated search, the client is guaranteed the best possible match for a fee. In direct search, the client avoids the fee but incurs search costs. Clients enter the market with no prior knowledge of the distribution of vendor service characteristics. In direct search, clients have to develop their beliefs about the market through sequential sampling.

![](/api/attachments/T9WQP86F/fulltext/images/304759a3a8e938aa6bda54a31c25ff1436b7e7843c9de00c838bff6a3a7bba40.jpg)  
Fig. 1. Salop’s circle.

The information available to clients in our model is the following: a rule to evaluate the utility of each vendor, awareness of the existence of the intermediary which provides matching services and of a forum where vendors advertise their services that enables clients to draw their samples for evaluation. At the start of a search, the intermediary informs each client of the utility it can attain by contracting with the vendor identified by it and the intermediary’s fee $P _ { \mathrm { i n t } }$ to disclose the identity of the vendor. As observed in prior research, utility functions are useful when comparisons involve uncertain values as in this paper where clients compare their expectations from direct search and mediated search. Modeling the marketplace as being horizontally differentiated over a circle implies that clients are also aware of the minimum expected utility from a service.

Providers who list with the intermediary generally pay a listing fee. However, it was shown by Bhargava and Chaudhary [4] that an intermediary would prefer to include as many vendors as possible and it could achieve this by reducing vendor participation fees. We consider the limiting case where the intermediary charges no listing fees to participating vendors, as a result of which all vendors in the market choose to participate in the mediated marketplace. This is in line with what we observe in many online marketplaces where the value of the intermediary’s service increases with the number of participating vendors. The only revenues to the intermediary in our model are participation fees from clients that choose to use it to identify the best available vendor for the client. When clients use the services of the intermediary, in return for the intermediary’s fees, they can complete their search in one single time period and obtain services from the best matching provider in subsequent time periods. Clients that choose direct search use sequential search to identify a suitable vendor and use a termination rule to stop search when future searches are not expected to improve utility [21]. If the players enter the market at $\scriptstyle t = 0$ and we consider a total of T time periods for search and consumption, Fig. 2 shows that mediated search terminates at $t { = } 1$ whereas direct search can last for $t _ { \mathrm { D } }$ time periods.

In our model, we assume that only complete information may be gathered from the intermediary. A client may either pay the intermediary a fee $P _ { \mathrm { i n t } }$ to identify the optimal vendor or pay nothing to the intermediary and choose to search for a vendor on its own. This assumption was described by Salop and Stiglitz [29] as follows. There exists a newspaper that publishes full information and a client can either pay a fee $P _ { \mathrm { i n t } }$ to purchase and process all this information or choose not to purchase the newspaper. This is the basic tradeoff in our model. Clients choose to use the services of an intermediary when an intermediary provides utility net of fees which exceeds that from direct search.

Most search models assume that clients know the prior distribution of prices or service specifications in the marketplace, though they do not know who offers what. In our model, we start by assuming that clients have no knowledge of the distribution of service offerings in the product space. This would be particularly true when they are new services or services which are constantly evolving. While performing direct search, clients draw inferences about the parameters of the marketplace through the sampling process. The advantage of this approach is that it helps us identify the changes in intermediary revenues as clients develop greater knowledge about the marketplace.

Starting with no prior knowledge of the market is useful in at least two ways in the context of intermediaries. One, it creates the most favorable conditions for an intermediary because the profitability of the intermediary in our model is dependent on the utility of the information it provides to clients. Also, in many markets, particularly those for information services where technologies and business models are rapidly changing, clients are not likely to start with much knowledge of the distribution of offerings in the market.

Net utility for client i from mediated search has three components: (1) expected utility from consumption $U _ { i \mathrm { I } } ( l _ { i } ^ { * } , l _ { \mathrm { i n t } , i } )$ based on clients’ preferences in the product space where $l _ { \mathrm { i n t } , i }$ represents the specifications of the vendor identified by the intermediary and $U _ { i \mathrm { I } }$ denotes client i’s utility from using the intermediary; (2) vendor fee $P _ { \mathrm { { V } } }$ and (3) intermediary fees $P _ { \mathrm { i n t } }$ . Utility from direct search has two components: (1) expected utility from consumption $U _ { i \mathrm { D } } ( l _ { i } ^ { * } , l _ { \mathrm { d i r } , i } )$ where $l _ { \mathrm { d i r } , i }$ represents the specifications of the vendor identified in search, $U _ { i \mathrm { D } }$ the utility obtained by client i by using direct search, and (2) vendor fee $P _ { \mathrm { { V } } }$ As described earlier, $l _ { \mathrm { i n t } , i }$ and $l _ { \mathrm { d i r } , i }$ may be different because $l _ { \mathrm { i n t } , i }$ is the best available vendor identified by the intermediary but direct search may stop after identifying $l _ { \mathrm { d i r } , i }$ before the optimal vendor is identified. The clients’ selection rule states that it should select mediated search when mediation yields greater expected utility than direct search and vice versa. If we consider a total of T time periods, the search rule may be written as:

Select Intermediary when

$$
\begin{array}{l} \left[ \sum_ {T} U _ {i \mathrm{I}} \left(l _ {i} ^ {*}, l _ {\text { int }, i}\right) - P _ {\mathrm{V}} \right] \\ - P _ {\text { int }} > \left[ \sum_ {T} U _ {i \mathrm{D}} \left(l _ {i} ^ {*}, l _ {\text { dir }, i}\right) - P _ {\mathrm{V}} \right] \end{array}\tag{1}
$$

Choose direct search otherwise.

Here the LHS represents utility from mediation and the RHS represents utility from direct search. Vendors whose service specifications differ from the ideal specification have a lower utility for a client, as specified by the clients’ preferences in product space. These preferences are modeled using a constant mismatch costs model so that $U ( l _ { 1 } ^ { \ast } , l _ { j } ) { = } u { - } c | l _ { i } ^ { \ast } { - } l _ { j } |$ where the distance $| l _ { i } ^ { * } - l _ { j } |$ refers to the shortest arc around the unit circle between $l _ { i } ^ { * }$ and $l _ { j } \ [ 2 8 ]$ . c is the cost of mismatch of specifications. Given the decision rule of clients (Eq. (1)), the intermediary attempts to set the fee $P _ { \mathrm { i n t } }$ that maximizes its profits. Following the model of horizontal differentiation, we set the clients’ willingness to pay, u to a constant value for all models which keeps utilities from all vendors in the circular product-space to be non-negative.

![](/api/attachments/T9WQP86F/fulltext/images/9c60a20a22c02db8d097de2a128c63a3e3787fdb245dc5d0cfbfec9b569508ba.jpg)  
Fig. 2. Intermediated and direct search.

Using the constant mismatch model, over the duration of the arrangement, which lasts for T time periods, client i’s utility $U _ { i \mathrm { I } }$ in Eq. (1) is given by:

$$
U _ {i 1} = \left[ \sum_ {t = 1} ^ {T} \left(u - c | l _ {i} ^ {*} - l _ {\text { int }, i} | - P _ {\mathrm{V}}\right) \right] - P _ {\text { int }}\tag{2}
$$

## 3.1. Direct transactions without the intermediary

When clients perform direct search, they examine vendors in the market sequentially until their searchtermination rule indicates that further search is unlikely to improve utility. The search algorithm used in the research is based on Rothschild [26]. The client’s utility from direct search may be split into two components: one during search and the other after search is completed. Adding the two, client $i \ ' \mathrm { s }$ net utility is given by:

$$
\begin{array}{l} U _ {i \mathrm{D}} = \sum_ {t = 1} ^ {t _ {\mathrm{D}} - 1} \left(u - c | l _ {i} ^ {*} - l _ {j} ^ {t} | - P _ {\mathrm{V}} - s c\right) \\ + \sum_ {t = t _ {\mathrm{D}}} ^ {T} \left(u - c | l _ {i} ^ {*} - l _ {j} ^ {\mathrm{D}} | - P _ {\mathrm{V}}\right) \end{array}\tag{3}
$$

where $l _ { j } ^ { t }$ are service specifications of the vendor being sampled at time $t , \ : l _ { j } ^ { \mathrm { D } }$ is the vendor identified from direct search, sc is the evaluation cost per time period. As described earlier, direct search may not identify the optimal vendor when the termination rule suggests that search be stopped. The cost of direct search therefore has three components: a fixed cost sc to evaluate a vendor, opportunity costs associated with loss of utility during search and loss of utility from identifying a sub-optimal provider at the end of the search. Increasing search cost sc decreases the client’s utility from direct search and expensive evaluation costs could make intermediation preferable over direct search to the client. However, since sc has a constant monotonic effect on $U _ { i \mathrm { D } } ,$ we set $s c$ to 0 for the simulations in this paper. Further evaluation of the influence of sc on the intermediary’s revenues will be done in future research.<sup>1</sup>

As pointed out earlier, the switch point for the search rule in our model can only be characterized in terms of a functional equation that cannot be solved explicitly. Therefore, a closed-form solution to identify the clients that will use the intermediary is, in general, not possible. In situations where it is not easy to obtain closed-form solutions from a model, simulations have become a commonly used technique in management research and extensive models have been developed for specific business applications. Simulations also help to isolate the impact of specific constructs under study for detailed examination. For example, Rivkin [25] used simulations to study the impact of the complexity of strategies on their duplication by competitors. Simulations have also been used to examine team processes [6]. We used a simulation model to study the selection process and identify the utilities for each participant in the marketplace as described in the setup below.

## 4. Simulation results

## 4.1. Setup

In the simulations, for each client, we compare the utility from direct and mediated search to identify the market the client will prefer. When the client selects the intermediary, it pays the intermediary fee and uses the intermediary to facilitate search. Intermediary revenues are calculated by summing client fees for those clients that prefer to use intermediary services. When direct search completes, clients use Eq. (3) to evaluate their utility $U _ { i \mathrm { D } }$ from direct search. Clients compare this to the utility $U _ { i \mathrm { I } }$ they would derive from using the intermediary. This information is provided to clients by the intermediary using Eq. (2) at the beginning of the search (though the identity of the vendor is not revealed). If $U _ { i \mathrm { I } }$ exceeds $U _ { i \mathrm { D } }$ net of fees, the client pays the intermediary fee and contributes to intermediary revenues. Intermediary revenues R are calculated by summing the fees from clients that choose the intermediary as in Eq. (4).

$$
R = \sum_ {i} P _ {\mathrm{int}}\tag{4}
$$

To examine the effect of intermediary fees, we calculated R for intermediary fees $P _ { \mathrm { i n t } }$ ranging from 0 to u, the maximum price clients was willing to pay for the service. The revenue-maximizing fee and revenues are identified from the resulting revenues as shown in Section 4 for the different configurations. We ran many different search configurations to examine the revenues and revenue-maximizing fees of matching intermediaries.

In the simulations, we introduced 1000 clients and recorded the mean values per client of the various parameters such as intermediary revenues over these 1000 clients. The simulations were then repeated 100 times to gather observations over 100,000 independ ent client observations. The mean values over these 100,000 observations have been reported here to ensure the robustness of the results [16]. A separate simulation was run for each size of the population of vendors in the marketplace. The service specifications of each vendor and client were generated randomly from a uniform distribution around the circle. When consumption was allowed, clients used the services provided by the best-known vendor found in earlier searches. Since we consider horizontal differentiation, all clients had the same reservation value (willingness to pay). The cost of mismatch c, and the client reservation value were such that when the client and vendor were on opposite sides of the diameter on the circle, the client obtained no utility from the service offered by the client.

We started with a random search model. This provides a benchmark for the profitability of an intermediary because it examines the impact of the most rudimentary direct search strategy on intermediary revenues. We then introduce deliberate search and examine the impact of consumption during search on the profitability of the intermediary. Finally, we compare the case where clients repeatedly enter the market to search for services. In the simulations, service specifications of vendors were uniformly distributed around the circumference of the circle though this information was not available to the clients.

## 4.2. Random search

We start with a basic comparison of mediated and direct search. Consider the case where there are two time periods (T=2), the first of which is spent in search and evaluating a vendor and the second is spent in using services from the vendor identified in the first time period. Since only one vendor is evaluated at a time in sequential direct search, this case may be considered a zero intelligence search where the optimal vendor (identified by the intermediary) is compared to the first random provider identified by direct search. In Figs. 3 and 4, we plot the intermediary’s revenues as a function of mediation fees $P _ { \mathrm { i n t } }$ charged per client for different sizes of the vendor population. Fig. 3 shows intermediary revenues when random search is possible and Fig. 4 shows intermediary revenues when the only option to clients is mediated search.

These figures indicate that there are distinct differences in the intermediary’s business performance when the simplest form of direct search is considered in the analysis versus when it is not. Direct search has two main effects on the intermediary’s revenues. The first is that when direct search is considered, there is an optimal fee that an intermediary may charge clients for matching services. In the absence of direct search, the intermediary is able to charge a fee that is very close to the clients’ reservation value and extract virtually all the surplus of the client from the use of the service offered by the provider. In smaller markets (10 vendors in Fig. 4), the intermediary’s optimal fee is less than the reservation value simply because even the best vendor for a client still does not generally provide the ideal selection of services for the client. In the presence of direct search, the optimal fee is close to one-third the value of the fee in the absence of direct search. The second is that the intermediary’s revenues/client fall sharply when direct search is allowed. On our scale, revenues fell from almost 180 units to about 25 units at the point where the profits are maximized when direct search is considered (at a mediation fee close to 60).

Intermediary revenue with direct search  
![](/api/attachments/T9WQP86F/fulltext/images/48861ff2db09217eba293ee8b589181261effff647bf08bb22200c06789dfee3.jpg)  
Fig. 3. Intermediary revenues in the presence of random search.

When direct search is allowed, it is seen that the intermediary’s revenues are low for very low and very high unit fees and are highest for intermediate fees. This is explained by the fact that when the unit fees are low, net utility for a large majority of the clients is higher after paying intermediary fees and availing matching services than after direct search. It may be noted that this direct search is not intelligent in the sense that clients only compare a random provider with the most preferred supplier in the population. Low mediation fees imply that the benefits of matching are not diminished greatly by the matching fees. As a result, most clients avail themselves of the intermediary’s matching service but the intermediary earns very little from each client. On the other hand, when the intermediary charges very high fees, much of the value of matching is eroded by the <sup>b</sup>matching tax<sup>Q</sup> levied by the intermediary. Under these conditions, the only clients that still find it efficient to use the intermediary are those whose luck of the draw was rather unfavorable and the service specifications of the selected provider yielded very little utility for the clients. As the fees were increased, there were fewer and fewer of these clients and consequently, though each such client is highly profitable to the intermediary, the overall effect is a decrease in the overall profitability of the intermediary. When the fees are almost equal to the clients’ reservation prices, there are no more clients for the matching service and the intermediary’s revenues reduce to zero. There is therefore an optimal intermediate price at which the intermediary achieves the highest profitability.

On the other hand, when direct search is not explicitly considered, the intermediary’s revenues are monotonically increasing in fees for all but the smallest populations of vendors. This is explained by the fact that clients prefer to use the intermediary as long as the utility derived from the preferred vendor net of matching fees is positive. When the population of vendors is small, the utility from the most preferred vendor could be significantly less than the reservation price and, depending upon the specific configuration of the vendor service specifications, many clients may not derive positive utility after accounting for matching fees. This indicates that when direct search is not an option, the optimal policy for an intermediary depends upon the size of the vendor population. For smaller populations, there is an optimal matching fee that maximizes intermediary revenues. For larger vendor populations, the optimal pricing policy is to charge a fee close to the clients’ reservation price and extract maximum revenues from the intermediary’s knowledge of the supplier population.

Intermediary revenues with no direct search  
![](/api/attachments/T9WQP86F/fulltext/images/568689d8fac862a1d6dad2880837489804854f8843ed8abf26692dd59124dfc6.jpg)  
Fig. 4. Intermediary revenues when direct search is not considered.

It must be remembered that the model here is very favorable to the intermediary. Direct search is nothing more than a random draw from the vendor population. Yet, the change has significant effects both on the overall revenues of the intermediary and the pricing policies of the intermediary.

## 4.3. Consumption during search

We now consider the case where clients use a search rule to terminate sequential direct search. The search rule used in this research is based on Rothschild [26]. In such a case, it is necessary to distinguish between services with low and high switching costs. When switching costs are low, clients are likely to consume services from providers even while searching. On the other hand, when switching costs are high, clients are likely to forego consumption of services until search terminates. In such cases, utility from consumption during search could be reduced significantly by switching costs so that it is efficient to wait for search to complete before consumption.

To simulate low and high switching costs, we expanded the time horizons in Eqs. (2) and (3) to 16 time periods (T=16). We consider two limiting cases: where there is no switching cost for the client and where there are prohibitively high switching costs. The first time period is used exclusively for search, but in the case of services with low switching costs, starting with the second time period, clients begin to utilize the services of the best available vendor, switching providers as superior providers are identified until search terminates. Upon termination of search, clients start using the services of the best available vendor in both cases of search with and without consumption. Intermediary revenues are calculated as before by summing the revenues gained from the clients that select mediation. Fig. 5 shows the intermediary’s revenues per client for both cases under different sizes of the vendor population. The labels for each curve indicate the size of the vendor population and whether consumption was possible or not. For example the label n<sup>\_</sup>cm10 indicates no consumption and 10 vendors and cons100 indicates 100 vendors and consumption during search. To enable comparison between cases, all fees and revenues have been normalized on a per-time-period basis.

Cons and 10 vendorsCons and 100 vendorsCons and 1000 vendors  
Impact of consumption during search on intermediary revenues  
![](/api/attachments/T9WQP86F/fulltext/images/7bf068e3dd28afa7420b03f31faaf87577c3f33ec43ff12580dfc3396c5370a9.jpg)  
— No cons and 10 vendors No cons and 100 vendors No cons and 1000 vendors  
Fig. 5. Consumption versus non-consumption during search.

It is again seen that the profits for the intermediary are highest for some intermediate values of client fees. Profits are low for very low and very high fees. It is also seen that profits are higher when consumption is not done during search compared to cases where consumption is done during search. The difference between the two cases lies in the fact that when consumption was allowed during search, clients were deriving some positive level of utility of service even while searching. These results indicate that a matching intermediary is likely to be most profitable in cases where switching costs are high and consumption is not viable during search.

## 4.4. Search experience

Thus far, we have only considered the case of clients who enter the market for the first time. However, as clients perform direct searches, they gather information about the marketplace and are able to make more informed decisions in subsequent searches. In particular, clients can form beliefs about the minimum utility that may be expected from direct search and can reject vendors whose service specifications are such that the utility from using their services is below the belief level. This reflects the client’s updated knowledge about the distribution of vendors in the market. The interesting feature of this model is that it allows us to consider the influence of the obsolescence of information gathered in past searches on current search.

Information gathered from earlier searches eventually becomes obsolete due to a number of factors.

Belief = 1

Demand and supply conditions change over time and further search is required just to ascertain the new vendor characteristics and prices. In dynamic industries, where technologies change rapidly, product and service features change over time. Finally, every market has a component of randomness created by the changing identity of buyers and sellers. The initial ignorance of new buyers and sellers makes the information of even the most experienced participants obsolete [32].

The obsolescence of information gathered from prior search is modeled by specifying the rate at which client’s expectations regarding the utility from direct search decays with time. Clients lower their expected utility from direct search in proportion to the rate of decay of information. Thus if client utility per time period achieved from direct search in iteration 4 in a certain search for a certain client is 150 and the rate of decay is 0.8, the client will lower its expectation from direct search to 120 and will reject all vendors in iteration 5 which yield utility per time period less than 120. To examine the influence of repeated searches and belief levels, we extend the simulations to perform 15 iterations of direct search. In each iteration, while performing direct search, clients rejected providers who yielded utility lower than the expected utility. The viability of intermediation under different conditions of information decay becomes clearer when we examine intermediary revenues/client/time period for different belief levels under consumption and non-consumption. Intermediary revenues are calculated using Eq. (4). Fig. 6 below shows intermediary revenues/ client/time period after 15 iterations of search. To facilitate comparison, only the case of search without consumption is shown in the paper, the results for the case with consumption are similar.

![](/api/attachments/T9WQP86F/fulltext/images/c04dd837eefde87ae2c624cb8959fc922f0ec483ecd4d419ffa9026b484a66d5.jpg)

The graphs show intermediary revenues when clients are assumed to search without consumption for belief levels of 1.0 and 0.8. Comparing the two graphs, we see that as expected, intermediary revenues are greater when the rate of obsolescence of information gathered during search increases. It is also seen that intermediary revenues increase when the size of the vendor population increases, though at a decreasing rate. The increase in intermediary revenues when the vendor population changes from 10 to 100 is much greater than the change in revenues when the vendor population increases from 100 to 1000.

Since the intermediary’s revenues in our model are obtained exclusively from fees paid by clients, we tried to understand the underlying phenomena that were driving intermediary revenues by calculating the utilities of clients under direct and mediated search as they gained experience from the search process. As the clients completed search iterations, we computed the cumulative utility of clients from all prior searches. A plot of these cumulative client utilities for the different configurations studied in this paper are presented in Fig. 7 below.

![](/api/attachments/T9WQP86F/fulltext/images/ae9d6fd5bc09c642c7b01db08c6b3e8e437f8ec0dd35b951647ffbbb570b95fd.jpg)  
Fig. 6. Intermediary revenues for repeated search.

The two sets of graphs show the average cumulative utility for a set of 1000 clients from mediated search and direct search over 15 iterations for two belief levels. The upper graphs are for the no-consumption cases and the lower graphs are for the cases where consumption of services is allowed. The LHS graphs represent belief levels of 1 and the RHS graphs represent belief levels of 0.8 (degradation of information). The labels for each curve indicate the number of vendors, intermediary fee and if the search was direct or mediated. For example, v10<sup>\_</sup> fee24D indicates that there were 10 vendors, intermediary fee was 24 units and search was direct. The figure shows that when belief is 1.0, i.e. clients reject all vendors who are less satisfactory than the best vendors found so far, utility from direct search rapidly surpasses that from mediated search both when consumption is allowed and when it is not. However, the graph on the top-right shows (v200<sup>\_</sup> fee24D and v200<sup>\_</sup> fee24I) that when the beliefs are lower than 1.0, vendor fees are low and the marketplace includes a large number of vendors, mediated search is generally superior to direct search.

Belief levels of 1.0 indicate that the market is fairly static and clients can be confident of evaluating vendors based on their knowledge of the marketplace gathered in previous searches. In such cases, it is seen that it is very efficient for clients to invest in gathering knowledge about the marketplace through direct search and avoid paying mediation fees. Though client utilities are low in initial searches and the use of mediation might appear efficient at that stage, the knowledge gathered about the market pays back very rapidly and in as few as seven or eight iterations, utility from direct search exceeds that from mediated search, even when the intermediary charges a very low fee. Therefore, we conclude that when the markets are relatively static and clients can use the experience they gather from previous searches in future searches, it is efficient for them to avoid the use of matching services altogether. However, when the marketplace is dynamic with client needs or vendor offerings change rapidly with time, clients cannot be confident of the value of the knowledge they gather from earlier searches and are forced to consider more vendors than their counterparts in static markets. This may happen when vendors are constantly upgrading features of their services or when client needs are changing rapidly. A matching intermediary can offer significant benefits in such dynamic markets, by matching clients to vendors.

Client utilities by iteration (without consumption and belief = 1)  
![](/api/attachments/T9WQP86F/fulltext/images/bf0d3d04001476837934d6d8598f1ec0c73b32fff7076a875f7b38a622585ee9.jpg)

Client utilities by iteration (without consumption and belief = 0.8)  
![](/api/attachments/T9WQP86F/fulltext/images/bf7b81f74b16d196053621182d85b285badd4a1d0e48549f87119f95fff22811.jpg)

Client utilities by iteration (with consumption and belief = 1)  
![](/api/attachments/T9WQP86F/fulltext/images/6fc9e65d50bf57cbcbabc360d1975d011090aa2156643496f3e1fdfb5762e8f8.jpg)

Client utilities by iteration (with consumption and belief = 0.8)  
![](/api/attachments/T9WQP86F/fulltext/images/529d36134c74fb3ff8288c16671708c109bb1a6ecedf03f7efa420a0f0106eb6.jpg)  
Fig. 7. Cumulative client utilities after repeated searches.

Finally, we summarize the results found in this paper in Table 1, which shows the optimal fees of the intermediary and its corresponding revenues for the four configurations examined in this paper.

Table 1(a) shows that the intermediary’s profits are highest when no direct search is allowed. At the optimal fees, its profits are higher when consumption is not allowed during search. Also, the intermediary’s profits increase as the vendor population increases in all columns. When clients consider search horizons that extend to future searches, the intermediary’s profitability decreases sharply as seen in Table 1(b), though increasing rate of obsolescence of information helps improve the intermediary’s revenues profits.

An interesting observation may be made regarding the superiority of mediation in dynamic markets in which the characteristics of vendor services change frequently and clients are unable to extrapolate their expectations from prior searches to future searches. In many cases, such dynamic markets have been created by the creative use of information using the vast amount of computing power now available in many companies. For example, in the market for airline tickets, prices change very rapidly and different price combinations are created in real time by the information systems of these companies. As a result, customers cannot hope to repeatedly get comparable prices for the same trip specifications. On the other hand, online intermediaries can easily integrate and process this information, keeping information-acquisition costs under check. The divergence between client utilities for mediated search and direct search over iterations in the presence of information obsolescence in Fig. 7 suggests that matching intermediaries such as those for airline tickets could be viable in the long run.

(b) Repeated search  
Table 1  
Intermediary’s optimal fees and profits  
(a) Random search versus mediated search

<table><tr><td rowspan="2">Vendor population</td><td colspan="6">Two time periods, one iteration</td></tr><tr><td>10</td><td></td><td>100</td><td></td><td>1000</td><td></td></tr><tr><td>Direct search allowed?</td><td>yes</td><td>no</td><td>yes</td><td>no</td><td>yes</td><td>no</td></tr><tr><td>Intermediary&#x27;s optimal fees/time period</td><td>54</td><td>138</td><td>60</td><td>174</td><td>60</td><td>174</td></tr><tr><td>Intermediary&#x27;s optimal revenues per time period</td><td>19.31</td><td>130</td><td>26.2</td><td>168</td><td>26.7</td><td>174</td></tr></table>

<table><tr><td rowspan="2">Vendor population</td><td colspan="6">T=16; 15 iterations; belief=1.0</td><td colspan="6">T=16; 15 iterations; belief=0.8</td></tr><tr><td>10</td><td></td><td>100</td><td></td><td>1000</td><td></td><td>10</td><td></td><td>100</td><td></td><td>1000</td><td></td></tr><tr><td>Consumption allowed?</td><td>yes</td><td>no</td><td>yes</td><td>no</td><td>yes</td><td>no</td><td>yes</td><td>no</td><td>yes</td><td>no</td><td>yes</td><td>no</td></tr><tr><td>Intermediary&#x27;s optimal fees/time period</td><td>36</td><td>30</td><td>24</td><td>36</td><td>24</td><td>12</td><td>12</td><td>6</td><td>12</td><td>24</td><td>12</td><td>24</td></tr><tr><td>Intermediary&#x27;s optimal revenues per time period</td><td>0.3</td><td>1.3</td><td>0.9</td><td>2.14</td><td>0.93</td><td>2.58</td><td>0.53</td><td>4.85</td><td>3.45</td><td>13.44</td><td>4.06</td><td>15.21</td></tr></table>

## 5. Conclusions and discussions

The research found that the introduction of direct search significantly reduces the revenues earned by the intermediary, even when clients have no prior information of the distribution of vendor features. When direct search is allowed, there is an optimal fee which the intermediary can charge to maximize intermediary revenues. The intermediary revenues fall when clients are allowed to consume services while searching compared to the case where consumption is not allowed during search. When client information atrophies rapidly between searches, it becomes more efficient for clients to use the intermediary and therefore, intermediary revenues increase. These results are also intuitively reasonable because the intermediary’s revenues depend upon the surplus that may be extracted from the expected mismatch between clients’ optimal service specifications and the service specifications of the selected vendor in direct search. The intermediary’s revenues are found to increase as the expected mismatch increases. The research can be used to generate many testable hypotheses. For example, it is expected that (1) intermediaries should be more profitable in markets characterized by information obsolescence, (2) intermediaries should be more profitable in markets where switching costs for services are high.

The results indicate that matching intermediaries can offer the greatest benefits in markets where the value of information gathered in search atrophies rapidly. In such cases, intermediary profits may be protected if knowledge of prices and services offered in prior searches is inadequate for clients to filter out vendors. The viability of intermediaries in such markets must however be tempered by at least two concerns. The first is that the profitability of an intermediary in such markets would depend upon the efficiency with which it can gather all the required information about all vendors in the first place. If information-gathering costs for the intermediary exceed the differential utility of the matching service to clients whose willingness to pay for the matching information will be constrained by the utility they can gather from direct search, intermediaries would not be profitable even in the markets most favorable to them. The other concern would be the role of competition among intermediaries. This research has examined the revenues of a monopoly intermediary and the introduction of competition will constrain the profitability of the intermediary further.

This last observation points to an important direction for future research. Intermediaries are likely to achieve significant economies of scale in providing matching services, thereby achieving profitability. However, to protect their profits from being eroded by defecting clients and competition, intermediaries may also attempt to provide other value-added services that may not necessarily offer economies of scale. One such possibility is the monitoring of quality [5].

One limitation of this research is that the simulation is based on a combination of an optimal search design for each individual search and a mechanism design for repeated search. Though the search algorithm used in direct search is based on Rothschild [26], who proved the optimality of the algorithm, the repeated searches are based on a mechanism design of transfer of expected utilities from previous searches adjusted for the likelihood of changes in market conditions. It is possible that a superior mechanism design for repeated search can further reduce the utility of mediated matching.

## Acknowledgements

The paper is based on the PhD dissertation of the first author. The feedback from participants at the AMCIS 2001 meetings in Boston, MA is gratefully acknowledged. The paper has benefited significantly from the comments of two anonymous reviewers. An earlier version of this paper was selected for a best paper award at the AMCIS 2001 conference. We thank Prof. V. Sambamurthy and Prof. R. Garud for helpful comments during the AOM 2000 meeting in Toronto. This research has been funded by the National Science Foundation under grant 9907325. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

## References

[1] M. Agrawal, R. Kishore, H.R. Rao, S. Upadhyaya, Towards a testbed for modelling application service providers (ASPs), Vision 5 (1) (2001) 13–23.

[2] J.Y. Bakos, Reducing buyer search costs: implications for electronic markets, Management Science 43 (12) (1997) 1676– 1692.

[3] R. Barrett, P.P. Maglio, Intermediaries: an approach to manipulating information streams, IBM Systems Journal 38 (4) (1999) 13.

[4] H.K. Bhargava, V. Chaudhary, Economics of an electronic intermediary with aggregation benefits (under review) (2001) 31.

[5] G. Biglaiser, Middlemen as experts, Rand Journal of Economics 24 (2) (1993) 212–223.

[6] A. Chaudhury, K. Nam, H.R. Rao, Management of information systems outsourcing: a bidding perspective, Journal of Management Information Systems 12 (2) (1995) 131– 159.

[7] P. De, V.S. Jacob, R. Pakath, A formal approach for designing distributed expert problem-solving systems, Information Systems Research 4 (2) (1993) 141 – 165.

[8] H. Demsetz, The cost of transacting, Quarterly Journal of Economics 82 (1) (1968 Feb.) 33– 53.

[9] T. Gehrig, Intermediation in search markets, Journal of Economics and Management Strategy 2 (1) (1993) 97 – 120.

[10] J. Goo, R. Kishore, H.R. Rao, A content-analytic longitudinal study of the drivers for information technology and systems outsourcing, Proceedings of the Twenty-First International Conference on Information Systems, Brisbane, Australia, 2000, pp. 601– 611.

[11] A. Kambil, E.v. Heck, Reengineering the Dutch flower auctions: a framework for analyzing exchange organizations, Information Systems Research 9 (1) (1998) 1 – 19.

[12] S. Kaplan, M. Sawhney, E-hubs: the new B2B marketplaces, Harvard Business Review 78 (3) (2000) 97–100.

[13] R. Kishore, H.R. Rao, K. Nam, S. Rajagopalan, A. Chaudhury, A relationship perspective on IT outsourcing: insights from a longitudinal study, Communications of the ACM 46 (12) (2003) 86 – 92.

[14] M.G. Kohn, S. Shavell, The theory of search, Journal of Economic Theory 9 (1974) 93 – 123.

[15] K.R. Lang, A.B. Whinston, A design of a DSS intermediary for electronic markets, Decision Support Systems 25 (3) (1999) 181 – 197.

[16] A.M. Law, W.D. Kelton, Simulation modeling and analysis, McGraw-Hill Series in Industrial Engineering and Management Science, 2nd ed., McGraw-Hill, New York, NY, 1991, pp. 113 – 114.

[17] R. Manning, P.B. Morgan, Search and consumer theory, Review of Economic Studies 49 (2) (1982) 203 – 216.

[18] V.S. Mookerjee, B.L. DosSantos, Inductive expert system design: maximizing system value, Information Systems Research 4 (2) (1993) 111– 140.

[19] J.C. Moore, H.R. Rao, A.B. Whinston, K. Nam, T.S. Raghu, An analysis of information gathering strategies for multi-agent

discrete resource allocation, Information Systems Research 8 (2) (1997) 151–171.

[20] S. Moorthy, B.T. Ratchford, D. Talukdar, Consumer information search revisited: theory and empirical analysis, Journal of Consumer Research 23 (4) (1997) 263– 277.

[21] P. Morgan, R. Manning, Optimal search, Econometrica 53 (4) (1985) 923– 944.

[22] K. Nam, S. Rajagopalan, H.R. Rao, A. Chaudhury, A twolevel investigation of information systems outsourcing, Communications of the ACM 39 (7) (1996) 36– 44.

[23] D.E. O’Leary, Internet-based information and retrieval systems, Decision Support Systems 27 (3) (1999) 319 – 327.

[24] M. Pingle, The effect of decision costs on the formation of market-making intermediaries: a pilot experiment, Journal of Economic Behavior and Organization 41 (1) (2000) 3– 26.

[25] J.W. Rivkin, Imitation of complex strategies, Management Science 46 (6) (2000) 824 – 844.

[26] M. Rothschild, Searching for the lowest price when the distribution of prices is unknown, Journal of Political Economy 82 (4) (1974) 689 – 711.

[27] A. Rubinstein, A. Wolinsky, Quarterly Journal of Economics 102 (1987 August) 581 – 593.

[28] S.C. Salop, Monopolistic competition with outside goods, The Bell Journal of Economics 10 (1) (1979) 141–156.

[29] S. Salop, J.E. Stiglitz, Bargains and ripoffs: a model of monopolistically competitive price dispersion, Review of Economic Studies 44 (3) (1977 October) 493–510.

[30] C. Shapiro, H. Varian, Information Rules: A Strategic Guide to the Network Economy, Harvard Business School Press, Boston, MA, 1998.

[31] D.F. Spulber, Market microstructure and intermediation, Journal of Economic Perspectives 10 (3) (1996) 135 – 152.

[32] G. Stigler, The economics of information, Journal of Political Economy 49 (3) (1961) 213 – 225.

[33] T.J. Strader, M.J. Shaw, Characteristics of electronic markets, Decision Support Systems 21 (3) (1997) 185 – 198.

[34] G. Tewari, J. Youll, P. Maes, Personalized location-based brokering using an agent-based intermediary architecture, Decision Support Systems 34 (2) (2003) 127–137.

[35] J. Tirole, The Theory of Industrial Organization, M.I.T. Press, Cambridge, MA, 1988.

[36] J.C. Westland, Transaction risk in electronic commerce, Decision Support Systems 33 (1) (2002) 87 – 103.

[37] A. Yavas, Marketmakers versus matchmakers, Journal of Financial Intermediation 2 (1) (1992) 33 – 58.

Manish Agrawal is an Assistant Professor in the department of Information Systems and Decision Sciences at the University of South Florida in Tampa. He completed his PhD at SUNY Buffalo. His research interests include Information Systems outsourcing, electronic commerce and electronic intermediaries. His articles have appeared or have been accepted for publication in Decision Support Systems, the Journal of Organizational Computing and Electronic Commerce, Communications of the ACM and his work has received the best paper award at the proceedings of the Americas Conference on Information Systems, 2001.

Govind Hariharan is an Associate Professor at the Coles College of Business of the Kennesaw State University. He specializes in the Economics of Regulations, Health Economics and Information Economics. Dr. Hariharan has taught business economics courses primarily for the executive MBA programs in Buffalo, Beijing and Singapore and Health Care Systems and Health Economics courses in the Health Care Administration program. He has received numerous awards for his teaching. He has assisted many technology start-ups get off the ground and has consulting experience in the banking, health care and grocery industries and has also served on numerous health-related task forces.

Rajiv Kishore is an assistant professor in the School of Management at the State University of New York at Buffalo. His research is focused on contemporary techno-organizational innovations geared towards improving an organization’s IT services delivery capabilities, and has been published or accepted for publication in Information Systems Frontiers, Communications of the ACM, and Journal of Healthcare Information Management. Rajiv has consulted in some of these and related areas with a number of large companies, some of which include BellSouth, Blue Cross Blue Shield of Minnesota, IBM, and Pioneer Standard Electronics. He is also the recipient of a multi-year National Science Foundation research grant as a co-principal investigator for conducting research in the area of IT outsourcing.

H.R. Rao is a Professor in the Department of Management Science and Systems at SUNY Buffalo and Adjunct Professor in CSE. His interests are in the areas of management information systems, ebusiness and outsourcing. He has authored or co-authored more than 90 technical papers, of which more than 60 are published in archival journals including Management Science, Information Systems Research and MIS Quarterly. His work has also received the best paper runner-up award at ICIS 2003. Dr. Rao has received funding for his research from the National Science Foundation, and he received the prestigious Teaching Fellowship at SUNY Buffalo. He is a co-editor of a special issue of The Annals of Operations Research, the Communications of ACM, Decision Support Systems and co Editor-in-Chief of Information Systems Frontiers and Associate Editor of ISR, IEEE SMC and DSS.
