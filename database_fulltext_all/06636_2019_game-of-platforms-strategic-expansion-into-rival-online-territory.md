---
otero_id: 6636
otero_key: "XGZCJEV7"
title: "\"Game of Platforms: Strategic Expansion into Rival (Online) Territory\""
authors: "Sagit Bar-Gill1"
year: "2019"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00575"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Game of Platforms: Strategic Expansion into Rival (Online) Territory

Sagit Bar-Gill<sup>1</sup>

<sup>1</sup>Tel Aviv University, sagitb@tau.ac.il

## Abstract

Online platforms, such as Google, Facebook, and Amazon, are constantly expanding their activities while increasing the overlap in their service offerings. This paper asks: Is expansion into rival platforms’ services profit-maximizing when users’ platform choices endogenously change with expansion? We model an expansion game between two online platforms, both incumbents in distinct service markets, that provide their services free of charge to users and earn ad-based revenues. Platforms decide whether or not to expand by adding the service already offered by their rival. Expansion is costly and impacts users’ platform choice—namely, their choice of single- vs. multihoming, which, in turn, affects platform prices and profits derived from the advertisers’ side of the market. We demonstrate that, in equilibrium, platforms may choose not to expand. Strategic “no expansion” decisions are due to the quantity and price effects of changes in the user partition resulting from expansion. We further analyze the effects of expansion-driven changes in interplatform compatibility, expansion costs, probability of users’ ad engagement, switching costs, and intraplatform service complementarity and quality on the optimal expansion strategy. We then incorporate these considerations to derive an optimal expansion rule that can be used to guide managerial decision-making regarding expansion into a rival’s “territory.”

Keywords: Media Economics, Entry, Expansion Game, Online Platforms, Two-Sided Markets.

Kenny Cheng was the accepting senior editor. This research article was submitted on November 30, 2016 and underwent two revisions.

## 1 Introduction

Google Plus, Google’s social networking service, was introduced in 2011, in the wake of Buzz, Google's previous and quite unsuccessful attempt to expand into social networking. With 25 million users in one month, industry analysts initially dubbed Google Plus the “Facebook Killer,” expecting Google Plus to be the next Facebook or Twitter. This narrative was quick to change. Most Google Plus users were not active, and in 2012 analysts and bloggers largely referred to Google Plus as a “ghost town,” compared to its very active and lively counterpart, Facebook. Today, Google Plus is defined as a “social layer” on top of Google. Its active users are predominantly from the tech community and use it mainly for aggregating, sharing and discussing news items related to their common interests. Nevertheless, while Google Plus has 28 million unique monthly visitors<sup>1</sup> spending an average of around seven minutes on the site, Facebook boasts 142 million unique users, spending an average of almost seven hours on the site. In the online world, where traffic and time spent equal money, Google Plus is hardly a success story.<sup>,2</sup>

Google Plus is just one example of expansion by an online platform into a territory already occupied by a rival platform. Google, Facebook, Amazon, and Apple—the “big four” of the tech industry—are constantly expanding their activities and increasing their overlap. Google now competes with incumbent Facebook in social networking; conversely, with the recent introduction of Facebook Graph Search, Facebook also competes with incumbent Google in search services. Apple and Amazon compete in selling digital media and devices, and additional overlap among all these platforms is found in cloud services, operating systems, smartphones, e-commerce, etc. With new services and products added each month, the overlap in the activities of these giants will only increase as each strives to provide a one-stop shop for their users.<sup>3</sup>

And to what end? A major driver of the expansion of these platforms is the cultivation of exclusive and intimate relationships with users, which they anticipate will translate into large advertising revenues<sup>4,5</sup> (e.g., through improved ad targeting; see Kang, 2012). Indeed, both Facebook and Google’s revenue comes predominantly from advertising, and in 2013 Amazon launched its ad exchange, allowing for the retargeting of shoppers after they leave Amazon.com (Edwards, 2012; Griffith, 2012; Taube, 2013).

For this paper we examined optimal expansion strategies of online ad-financed platforms, focusing on expansion into services already offered by rival platforms, a practice that has become pervasive in today’s tech landscape. This paper presents a modeling framework that helps formulate answers to the following questions: Should ad-financed platforms always strive to expand their service offerings by adding rivals’ existing services? Under what circumstances is platform imperialism a profitmaximizing strategy? What are the effects of expansion costs on users’ response to advertising, service quality, intraplatform complementarity, and interplatform compatibility on the optimal expansion strategies?

Through an analysis of a platform expansion game, we thus provide a timely addition to the growing literature on various strategic behaviors in platform markets.<sup>6</sup> Recent work has examined platform strategies such as openness and developer property rights (Boudreau, 2010; Eisenmann, Parker, & Van Alstyne, 2008; Parker & Van Alstyne, 2018), compatibility with rival platforms (Adner, Chen, & Zhu, 2015; Casadesus-Masanell & Ruiz-Aliseda, 2009), the choice of exclusive contracts versus multihoming (Hagiu & Lee, 2011), tying (Amelio & Jullien 2012; Choi, 2010), exclusion of some user types (Hagiu, 2011), and strategic preannouncement (Chellapa & Mukherjee 2015), to name but a few.<sup>7</sup>

Within this literature, a few works have examined platform expansion or entry; papers by Eisenmann, Parker, & Van Alstyne (2011) and Zhu & Iansiti (2012) are most closely related to our work. These papers study one-sided decisions by an entrant or “attacker” platform, deriving conditions for successful attacks on an incumbent’s market. Specifically, Eisenmann et al. (2011) focus on the impact of complementarity levels between the attacker and target platforms, whereas Zhu and Iansiti (2012) focus on the impact of platform quality, indirect network effects, and consumer expectations on the entrant’s success.

Our contribution to the existing literature is thus threefold: (1) We analyze a strategic expansion game between two platforms that are incumbents in their respective markets and that are both considering expansion into the rival platform’s market. As such, expansion is not a one-sided activity but rather a strategic interaction between platforms because their expansion decisions interact with and affect each other. Highlighting strategic interaction provides a more realistic representation of platform expansion decisions, as current digital platform markets are largely dominated by a small number of competing firms responding to each other’s actions.<sup>8</sup> (2) Within this strategic interaction framework, we study the resulting expansion equilibrium and identify the conditions that lead to expansion by both platforms, one platform, or none of the platforms. (3) We study the effect of various factors on platforms’ optimal expansion strategies, such as interplatform compatibility, intraplatform service complementarity, expansion costs, service quality, switching costs, and user response rates to ads. This paper thus provides a comprehensive view of expansion drivers and inhibitors through the medium of our strategic game, which will serve as a useful guide for practitioner decision-making.

We model a market with two platforms through which advertisers may reach potential buyers (platform users). The platforms provide free services to users, generating revenue by selling users’ ad engagement (or ad-related actions) <sup>9</sup> to advertisers, <sup>10</sup> where ad engagement represents a positive cross-side network effect of potential buyers on the advertisers’ side of the market (e.g., Eisenman et al., 2006). At the outset, each platform offers one service type, and buyers optimally choose which platform(s) to use, inducing the initial buyer partition.

Platforms engage in an expansion game, in which each platform strategically chooses whether or not to expand by adding the type of service already offered by its rival. We specifically consider expansion that may affect the overlap in platforms’ user bases, or the degree of multihoming. This potential impact of expansion is the main driver of the strategic interaction studied in the model.

The game proceeds in two stages. In the first stage, platforms make their expansion decisions, which affect buyers’ platform choice and thus determine the final buyer partition. In the second stage, platforms set prices per user action charged to advertisers, given the buyer partition. Advertisers then observe platform prices and the buyer partition and choose where to place their ads, which, in turn, determines platforms’ expected profits.

Endogeneity of the buyer partition is an important feature in our setting, resulting from changes in the level of compatibility between the platforms brought on by expansion. We consider both increases and decreases in compatibility following expansion, capturing two possible scenarios: (1) expansion is aimed at creating a one-stop shop for users, therefore compatibility with the rival platform is decreased; (2) expansion that adds the rival’s core service requires intraplatform service compatibility that may increase interplatform compatibility as a side effect (since the new service is the same as the rival’s core offering). Such changes in platform compatibility affect users’ single- and multihoming behaviors, and thus the buyer partition and resulting cross-side network effect for different pairs of expansion decisions.

The basic motivation for expansion in our setting is increasing users’ probability of ad engagement, as a result of ad exposure occurring on an additional service. This implies that if the buyer partition were exogenous, then expansion would always increase expected profits, due to the increase in the expected quantity of ad-engagement events sold to advertisers. Endogeneity of the buyer partition in our setting implies that this benefit of expansion must be weighed against the effects of changes in the user partition.

We distinguish between two effects associated with the endogeneity of the partition of buyers: a quantity effect and a price effect. The former is a direct effect resulting from the change in user partition that may either increase or decrease the total number of potential buyers reached through the platform <sup>11</sup> following expansion, thereby affecting expected profits. The latter is an indirect effect, as equilibrium prices per user action decrease according to the degree of multihoming. This is because, in equilibrium, prices are set such that advertisers place ads on both platforms but do not pay double for reaching multihomers twice.

Considering the above effects of expansion, as well as platforms’ expansion costs, users’ switching costs, and various benefits to users from expansion, we derive conditions for optimal expansion and no-expansion. We find that expansion is a dominant strategy when it decreases multihoming, increases exclusivity, and when its cost is relatively low, while no-expansion may be optimal when the cost of expansion is higher or when users’ multihoming increases with expansion. This allows us to characterize expansion equilibria for different parameter spaces. We show that different types of equilibria may arise depending on the magnitude of the effects discussed. Notably, asymmetric expansion may be an equilibrium even for symmetric platforms, and symmetric no-expansion may also be optimal when the benefits of expansion are lower than its cost.

We further analyze the effects of our model parameters on optimal expansion strategies. Increases in the expansion cost, users’ switching cost, and core service quality, may lead to equilibrium no-expansion. Similarly, decreases in the probability of ad engagement, in the quality of the added service, and in the complementarity between same-platform services may also impact optimal expansion strategies, as will changes in interplatform compatibility levels. These factors are all represented in the optimal expansion rule (OER) derived in this paper, which may be used to structure debates surrounding platform expansion decisions.

We thus offer the following contributions for managers and researchers of digital platforms: (1) We provide a structured framework for consideration of platform expansion, which incorporates various factors, including expansion cost, expansion effects on same-platform service complementarity, users’ switching costs, platform compatibility, users’ adengagement rates, and more. (2) Our analysis cautions against the prevalent practice of “platform imperialism,” by deriving market conditions for optimal expansion and, importantly, optimal noexpansion. (3) We show that a Prisoner’s Dilemma may arise, highlighting the circumstances when expansion is individually rational, but yields lower profits than coordinated no-expansion. These contributions are unique to our game-theoretic framework and are particularly relevant for today’s largely oligopolistic digital platform markets.

In the following, Section 2 reviews the related literature; the model is then set up in Section 3 and analyzed in section 4. We offer concluding remarks and a discussion of managerial implications in Section 5.

## 2 Related Literature

Studying advertising-financed platforms, we relate to the literature on media platforms. This literature has examined equilibrium ad prices, levels of advertising, content differentiation, and platform entry (e.g., Ambrus et al, 2013; Anderson & Coate 2005; Anderson, Foros, & Kind, 2011; Anderson et al., 2012; Crampes, Haritchabalet, & Jullien, 2009; Reisinger, 2012). Compared to these papers, we simplify by assuming that advertisers are homogeneous, and by focusing on the positive crossside network effect exerted by potential consumers on advertisers, <sup>12</sup> in order to allow for tractability in solving the two-stage expansion game.

Still, the main assumptions of our model are consistent with previous work in the media platforms literature. Advertisers in our model may multihome, as is common in the literature (an exception is Reisinger 2012). We further allow for user multihoming, as in Ambrus et al. (2013), Anderson et al. (2011), Anderson et al. (2012), and Athey, Calvano, and Gans (2013).

User multihoming creates some redundancy for multihoming advertisers in our model, and thus gives rise to pricing which follows the “principle of incremental pricing” defined in Anderson et al. (2011). Namely, prices are determined according to the incremental benefit of placing ads on an additional platform, thereby internalizing the redundancy for multihoming advertisers. A similar notion of redundancy in advertising arises in Athey et al. (2013) as a result of consumer switching.<sup>13,14</sup>

Note that in our model there is only partial redundancy from reaching multihoming users twice, as users’ probability of an ad-related action increases with ad exposure on an additional service. As a result, the degree of user multihoming exerts a negative effect on prices. This is in contrast to Anderson et al. (2011), where the redundancy is full and the degree of multihoming does not directly affect ad pricing. On the other hand, and quite naturally, user exclusivity has a positive effect on prices in both papers.<sup>15</sup>

Related to our paper, Eisenmann et al. (2011) and Zhu and Iansiti (2012) have studied entry or expansion by one platform into another platform’s market. Eisenmann et al. (2011) dub this practice an “envelopment attack,” and build a typology of attacks based on the level of complementarity between the attacker and target platforms, deriving conditions for successful attacks. Zhu and Iansiti (2012) develop a theoretical model to examine the relative importance of platform quality, indirect network effects, and consumer expectations on the entrant’s success. We, on the other hand, model a strategic expansion game between two platforms; we do not label one platform an “attacker” or “entrant,” both platforms may or may not expand and conditions for different types of expansion equilibria are derived.

## 3 The Model

We model a market with two platforms offering online services to buyers or platform users, in order to attract advertisers who would like users to engage with their ads. Platforms thus connect advertisers with potential buyers, facilitating a cross-side network effect of the buyer side on the advertiser side of the market. Platforms are ad financed, and advertising revenues are collected based on users’ ad-related actions (this constitutes the common pay-per-performance model).<sup>16</sup>

The focus of the model is platforms’ strategic expansion behavior when the buyer partition is endogenous, and thus changes with expansion decisions. We analyze an entry or expansion game between the two platforms, in which each platform may or may not expand by adding the service initially offered by the rival platform. Following expansion decisions, platforms set prices per user action charged to advertisers. Advertisers observe the partition of buyers resulting from platforms’ expansion decisions as well as platform prices and choose their advertising strategy: placing ads on both platforms, placing an ad on one of the platforms, or not advertising at all.

## 3.1 Platforms: Basic Assumptions and Notation

There are two platforms in the market; let $i \in \{ 1 , 2 \}$ denote the platform index. At the outset, each platform provides one service, its core service, that is different from the one provided by its rival. Platform services are provided to users free of charge. A strategy for platform ?? is a couple $( e _ { i } , p _ { i } )$ , where $e _ { i } \in \{ E , \bar { E } \}$ represents the platform‘s expansion decision—either “expansion” (denoted ??) or “no-expansion” (denoted ??<sup>̅</sup>), and $p _ { i } \in [ 0 , \infty )$ is the price per user action charged to advertisers on the platform. Let $( e _ { 1 } , e _ { 2 } )$ denote a pair of expansion decisions, and $n \in \{ 0 , 1 , 2 \}$ the number of expanded platforms. We assume that platforms expand only by adding the service already offered by their rival.

The quality of platforms’ core services is denoted $q ,$ and expansion implies adding a second service of quality $\Delta q \in ( 0 , \bar { q } ) . ^ { 1 7 }$ Platforms’ initial or core services are thus assumed to be of higher quality than newly added services, as a baseline case. We allow for complementarity between platform services or, equivalently, a quality enhancement for the newly added service. This complementarity (or quality) benefit is denoted as $\mu _ { b } \sim U [ 0 , \overline { { \mu } } ]$ , where subscript ?? represents a buyer-specific realization, such that $\mu _ { b }$ is the subjective enjoyment of buyer ?? from the incremental benefits, uniformly distributed across the buyer population. The total quality offered by platform ?? is denoted $q _ { i } ,$ such that $q _ { i } = q$ for $e _ { i } = { \bar { E } }$ , and $q _ { i } =$ $q + \Delta q + \mu _ { b }$ for $e _ { i } = E$

Expansion entails a fixed cost for platforms, represented by the constant $c \geq 0$ . Generally, we denote total cost for ?? as $C ^ { e _ { i } }$ , such that $C ^ { \overline { { E } } } = 0$ and $C ^ { E } = c .$

Platforms are assumed to be symmetric, offering the same quality of core and added services, the same distribution for service complementarity (or quality enhancement) benefits, $\mu _ { b }$ , and incurring the same fixed cost for expansion. Clearly, this may not be the case in most real-world situations. But rather than restrict our analysis, this will demonstrate that platform asymmetry is not required to obtain nontrivial equilibrium outcomes (including equilibria with asymmetric expansion).

Platform revenues are derived from user ad actions sold to advertisers, where these ad actions represent a positive indirect network effect of the buyer side on the advertiser side of the market. We thus turn to introduce assumptions regarding buyers and advertisers in the market.

## 3.2 Buyers

There is a unit mass of buyers in the market. Buyers choose which platform(s) they subscribe to, and this yields the buyer partition—a partition of the buyer population into three groups comprising exclusive users of Platforms 1 and 2 and multihomers.

We define multihoming users as those who subscribe to each platform’s core service, i.e., its original, preexpansion, offering. Postexpansion, the same definition of multihoming continues to hold. While, in reality, users may subscribe to the same type of service from both platforms postexpansion, we assume that they primarily use only one service of a certain type, as same-type services are substitutes.

The buyer partition is a function of platforms expansion decisions $( e _ { 1 } , e _ { 2 } )$ denoted $B ^ { e _ { 1 } e _ { 2 } } \equiv$ $\left\{ b _ { 1 } ^ { \bar { e } _ { 1 } e _ { 2 } } , b _ { 2 } ^ { e _ { 1 } e _ { 2 } } , b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } } \right\}$ , where $b _ { i } ^ { e _ { 1 } e _ { 2 } }$ is the group of platform ??’s exclusive subscribers and its mass, and $b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } }$ is the group of multihomers and its mass, for $( e _ { 1 } , e _ { 2 } )$ . We assume that the market is covered for any $( e _ { 1 } , e _ { 2 } )$ , such that, $b _ { 1 } ^ { e _ { 1 } e _ { 2 } } + b _ { 2 } ^ { e _ { 1 } e _ { 2 } } + b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } } = 1 . ^ { 1 8 }$

We will consider both the initial and final buyer partition, as buyers choose platforms twice. Their initial choice is made before platforms decide on expansion and without anticipating possible expansion. This results in the initial buyer partition $B ^ { \bar { E } \bar { E } }$ . Following expansion decisions, buyers may switch away from their initial subscription choices, which results in the final buyer partition $B ^ { e _ { 1 } e _ { 2 } }$ where $e _ { 1 } , e _ { 2 } \in \{ \overline { { E } } , E \}$ The buyer partition is determined in equilibrium as a result of buyers’ utility maximization, defined as follows.

## 3.2.1 Buyer Utility

Buyer utility is linear in the total quality of platform services. For exclusive platform ?? users, this total quality is $q _ { i }$ (defined above), and for multihomers total quality is $2 q$ (the sum of the two core services’ quality).

Multihomers incur heterogeneous and endogenously determined compatibility costs (or multihoming costs). We specifically consider users who draw a baseline compatibility cost once at the outset from ??[0,1], and then experience an increase or decrease in this cost, as a result of platforms’ expansion decisions. The change in multihoming cost is the same across users, such that each user maintains the same relative cost compared to his or her peers.

Expansion-induced changes in compatibility costs represent changes in platform compatibility resulting from the addition of the rival’s core service. We explore both the case of (weakly) increasing and decreasing compatibility costs, <sup>19</sup> motivated by the following possible scenarios:

Increasing (or weakly increasing) compatibility costs: Expansion aims to create a one-stop shop, and thus decreases the expanding platform’s compatibility with the rival, making multihoming costlier. Returning to the Google-Facebook example, Google Plus was intended to create a rival social networking service to fulfill yet one more need for Google users. Since Google Plus allows users already signed into their Google accounts to participate in social networking that is integrated with other Google services, it thereby (weakly) increases the relative cost of multihoming, i.e., using Facebook for social networking. This same “one-stop shop” argument could be applied to Facebook’s introduction of search, which reduces the need to leave Facebook to conduct certain types of search queries, and thus increases (at least weakly) the cost of multihoming. <sup>20</sup> Of course, more successful one-stop shops were created by Google and Apple in their competition in the markets for devices, gadgets and compatible apps, <sup>21</sup> where expansion into overlapping apps and services was accompanied by decreased compatibility, leading users to identify with only one ecosystem over time.<sup>22</sup>

Decreasing compatibility costs—two scenarios: In the first scenario of decreasing compatibility costs, the newly added service is designed to be compatible with the core service, whereas the latter may be further tweaked to increase compatibility. Since the newly added service is the same as the rival’s core service, a possible side-effect is increased compatibility between the two core services, which decreases multihoming costs. A case in point is the ongoing competition between Snapchat and Instagram. Instagram, which set out as a photo-sharing app, and Snapchat, a multimedia messaging app, have both expanded their services and have become very similar over time. Specifically, in 2016, Instagram launched its “Stories” feature, which essentially copies Snapchat’s Stories functionality.<sup>23</sup> While this expansion into the Snapchat realm was intended to steal users away from the rival, for many users this increased similarity facilitated multihoming, evidenced by the number of users cross-posting the same content on both platforms.<sup>24</sup>

In the second scenario of decreasing compatibility costs, expansion leads to exclusive users learning about the new service offering, which may lead to increased awareness of the rival’s similar offering (its core service), thus leading to lower multihoming costs as a result of expansion. Expansions into the e-retail space are a prime example of this scenario. Consider Google’s attempts to establish an e-commerce service (with Google Shopping, Google Express and, recently, Google Shopping $\mathrm { \bar { A } c t i o n s } ^ { 2 5 } )$ . In the course of these attempts, Google has noted that many product searches initiated on Google conclude with purchases on Amazon. <sup>26</sup> This is because, for many users, information on product offerings, availability, and prices on Google, reduces search time on Amazon, and thus increases interplatform compatibility and decreases multihoming costs.

The above scenarios are represented in the model by endogenous compatibility costs. Formally, we denote user $b ^ { \prime } \mathbf { s }$ baseline compatibility cost by $m _ { b } { \sim } U [ 0 , 1 ]$ and the change in this cost following expansion by $\Delta m ^ { n }$ (recall that $n \in \{ 0 , 1 , 2 \}$ is the number of expanded platforms), where $\Delta m ^ { 0 } = 0$ and $\Delta m ^ { 1 } , \Delta m ^ { 2 }$ are either (weakly) positive or negative constants (we allow $\Delta m ^ { 1 } \neq \Delta \dot { m } ^ { 2 } )$ . User $b ^ { \prime } \mathbf { s }$ compatibility cost is thus $m _ { b } ^ { e _ { 1 } e _ { 2 } } \equiv m _ { b } + \Delta m ^ { n }$ . This specification, chosen for its simplicity and realism, will allow for a tractable analysis.

## We further assume that:

1. $| \Delta m ^ { 1 } | , | \Delta m ^ { 2 } | < q \quad :$ Changes in users’ compatibility costs following expansion do not exceed the utility derived from the core service’s quality.

2. $\overline { { \mu } } < q \colon$ : The upper bound for users’ utility from same-platform service complementarity does not exceed the utility derived from the core service’s quality.

These assumptions limit the number of cases we consider, allowing us to focus on more plausible parameter values.

Utility for user $b \in B$ is written as:

$$
\begin{array}{c} {u _ {i} ^ {b} = q _ {i}} \\ {u _ {1 2} ^ {b} = 2 q - m _ {b} ^ {e _ {1} e _ {2}}} \end{array}\tag{1}
$$

Where $u _ { i } ^ { b }$ is $b ^ { \prime } \mathbf { s }$ utility from subscription to a single platform ?? (i.e., singlehoming on ?? ) and $u _ { 1 2 } ^ { b }$ is $b ^ { \prime } \mathbf { s }$ utility from multihoming.<sup>27</sup>

Since users do not anticipate platform expansion, they are therefore likely to choose platforms twice. They make an initial subscription choice before expansion decisions are made and may then switch to another choice following platform expansion. Switching to a new choice is costly, such that the utility for a switching user $b \in B$ from a new choice $i _ { n e w } \in$ {1,2,12} is $u _ { i _ { n e w } } ^ { b } - s$ , where $u _ { i _ { n e w } } ^ { b }$ is defined in Eq. (1) and $s \geq 0$ is the switching cost incurred. To summarize, a user’s initial platform choice is made given his or her individual realization of $m _ { b } .$ , and the final platform choice (following expansion decisions) is made given $m _ { b } ^ { e _ { 1 } e _ { 2 } }$ , with a switching cost of ??.

Users’ platform choices for each pair $( e _ { 1 } , e _ { 2 } )$ maximize utility. We make two tie-breaking assumptions. First, we assume that indifference between the two platforms is resolved by a fair coin flip, i.e., users indifferent between Platform 1 and 2 will choose each platform with a probability of 0.5. This represents an idiosyncratic platform preference when platforms offer exactly the same total quality level. Second, we assume that indifference between multihoming and the choice of a single platform is resolved in favor of multihoming.

## 3.2.2 Buyer Equilibrium

Definition 1: Buyer equilibrium is a choice of platform(s) for each buyer $b \in B$ given $( e _ { 1 } , e _ { 2 } )$ such that each buyer’s choice is utility maximizing, given $m _ { b } ^ { e _ { 1 } ^ { - } e _ { 2 } }$ and ??.

A partition $B ^ { e _ { 1 } e _ { 2 } }$ thus constitutes buyer equilibrium given $( e _ { 1 } , e _ { 2 } )$ . Endogeneity of $B ^ { e _ { 1 } e _ { 2 } }$ is the result of expansion-induced changes in compatibility costs, which, in turn, represent endogenous interplatform compatibility levels.

## 3.2.3 Buyers’ Probability of Ad Engagement

Advertising on the platforms is aimed at generating user engagement with the ad or the advertiser. The adengagement event can take different forms, where the ad action for which advertisers pay is usually campaign specific. Examples of ad actions include a sale, click, registration, form submission, or any type of engagement solicited by the advertisement.

The expected number of ad-related actions, or engagement events, generated by each group of buyers depends on its mass and response rate. The response rate is the probability that a user engages with an ad, where ad exposure occurs via platform services. Let $\rho \in ( 0 , 1 )$ denote users’ ad-action probability, for ad exposure on one service. We assume that ad actions are independent across services, such that a user exposed to an ad on two services will engage with the ad exactly once with probability $2 \rho ( 1 - \rho )$ , twice with probability $\rho ^ { 2 }$ , and will not engage at all with probability $( 1 - \rho ) ^ { 2 }$ . This represents the basic motivation for platform expansion—improving users’ overall ad-engagement probability by increasing the number of contact points with the platform’s user base.

## 3.3 Advertisers

There is a unit mass of homogeneous advertisers in the market who aim to reach potential buyers by placing ads on the platforms. Platform users’ ad engagement generates a positive cross-side network effect of the buyer side on the advertiser side of the market, and thus drives advertisers’ participation in the platform market. Advertisers’ strategy is a choice of platform or platforms on which to place ads, denoted $\alpha \in A \equiv$ {{1}, {2}, {1,2}, ∅}.

The expected benefit of ??. Advertisers benefit from unique user ad actions, i.e., a second action by the same user is considered redundant. This is represented by a constant value for a user’s first engagement event, normalized to 1, whereas the value of a user’s second engagement event is $\operatorname { z e r o . } ^ { 2 8 }$ We introduce the notation $\tilde { \rho } \equiv 2 \rho - \rho ^ { 2 }$ , which is the probability of at least one user action, when reaching the same user on two services. $\tilde { \rho }$ is thus the relevant engagement probability when considering the benefit of ad exposure on two services (i.e., for an expanded platform).

The expected benefit of ?? is the cross-side network effect of buyers on advertisers, defined as the product of the relevant engagement probability and the mass of users reached. Notably, the mass of users reached via platform ?? includes both its exclusive subscribers and its multihoming users, who subscribe to one service from each platform. When advertising on a single platform, $\alpha = \{ i \}$ , the expected benefit is simply $\rho _ { i } b _ { i } ^ { e _ { 1 } e _ { 2 } } + \rho b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } }$ where $\rho _ { i } \equiv \rho _ { i } ( e _ { i } )$ represents the probability of a unique engagement event and depends on the platform’s expansion decision, such that $\rho _ { i } ( \bar { E } ) = \rho$ and $\rho _ { i } ( E ) = \tilde { \rho }$ . When advertising on both platforms, $\alpha = \{ 1 , 2 \}$ , the expected benefit is $\rho _ { 1 } b _ { 1 } ^ { e _ { 1 } e _ { 2 } } + \rho _ { 2 } b _ { 2 } ^ { e _ { 1 } e _ { 2 } } + \tilde { \rho } b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } }$ , since multihomers are now reached through two services and $\tilde { \rho }$ is their relevant engagement probability.

The expected cost of $\pmb { \alpha } .$ . The expected cost is the amount charged by the platforms in the advertiser’s choice set, $\alpha ,$ which is, for each $i \in \alpha ,$ the product of the price per action and the expected number of ad actions provided. Considering the expected number of actions provided by ??, we assume that the platform perfectly tracks its exclusive users, and thus charges advertisers only for unique actions by these users, $\rho _ { i } b _ { i } ^ { e _ { 1 } e _ { 2 } }$ . On the other hand, multihomers subscribe to only one of the platform’s services and are not tracked outside of the platform. Each platform thus provides $\rho b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } }$ expected actions by these users. 29 Summarizing, each platform $i \in \alpha$ charges its advertisers a sum of $p _ { i } \bar { [ } \rho _ { i } b _ { i } ^ { e _ { 1 } e _ { 2 } } + \rho b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } } ]$

The expected value of choice ?? is defined as the difference between the expected benefit and the cost of ?? , and is denoted as $V ^ { \alpha } \equiv$ $V \big ( \boldsymbol { \alpha } | ( e _ { i } , p _ { i } ) _ { i = 1 , 2 } , B ^ { e _ { 1 } e _ { 2 } } \big )$ :

$$
= \left\{ \begin{array}{l l} (1 - p _ {i}) \big [ \rho_ {i} b _ {i} ^ {e _ {1} e _ {2}} + \rho b _ {1 2} ^ {e _ {1} e _ {2}} \big ] & \text {for} \alpha = \{i \} \\ \big [ \rho_ {1} b _ {1} ^ {e _ {1} e _ {2}} + \rho_ {2} b _ {2} ^ {e _ {1} e _ {2}} + \tilde {\rho} b _ {1 2} ^ {e _ {1} e _ {2}} \big ] \\ - p _ {1} \big [ \rho_ {1} b _ {1} ^ {e _ {1} e _ {2}} + \rho b _ {1 2} ^ {e _ {1} e _ {2}} \big ] \\ - p _ {2} \big [ \rho_ {2} b _ {2} ^ {e _ {1} e _ {2}} + \rho b _ {1 2} ^ {e _ {1} e _ {2}} \big ] & \text {for} \alpha = \{1, 2 \} \\ 0 & \text {for} \alpha = \emptyset \end{array} \right.\tag{2}
$$

The important feature of $V ^ { \alpha }$ is that advertiser multihoming, or $\alpha = \{ 1 , 2 \}$ , entails some redundancy, as multihoming users are reached twice and advertisers pay both platforms for their ad actions. Specifically, when $\alpha = \{ 1 , 2 \}$ , access to multihoming users provides an expected benefit of $\tilde { \rho } b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } }$ , at an expected cost of $( p _ { 1 } + p _ { 2 } ) \rho b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } }$ , where $\rho < \tilde { \rho } < 2 \rho$ Therefore, $V ^ { 1 2 } < V ^ { 1 } + V ^ { 2 }$

We assume that advertiser indifference between $\alpha =$ {1,2} and $\alpha = \{ i \}$ is resolved in favor of $\alpha = \{ 1 , 2 \}$

## 3.4 Platforms: Profits

Each pair of platform expansion decisions $( e _ { 1 } , e _ { 2 } )$ defines an expansion subgame and determines $B ^ { e _ { 1 } e _ { 2 } }$ in the subgame. Platform $i \ ' _ { \mathrm { { s } } }$ expected profit in an expansion subgame $( e _ { 1 } , e _ { 2 } )$ for price $p _ { i }$ , given the rival’s price $p _ { j }$ , and cost $C ^ { e _ { i } }$ is denoted as $\pi _ { i } ^ { e _ { 1 } e _ { 2 } } ( p _ { i } | p _ { j } )$ . Platform profit is the product of its price per action $p _ { i }$ and the number of ad actions provided, minus the cost $C ^ { e _ { i } }$ . The number of actions provided is positive if the platform is chosen by advertisers $( i \in \alpha )$ and zero otherwise. Therefore:

$$
\begin{array}{r l} & {\pi_ {i} ^ {e _ {1} e _ {2}} \big (p _ {i} | p _ {j} \big)} \\ & {= \left\{ \begin{array}{l l} p _ {i} \big [ \rho_ {i} b _ {i} ^ {e _ {1} e _ {2}} + \rho b _ {1 2} ^ {e _ {1} e _ {2}} \big ] - C ^ {e _ {i}} & i \in \alpha \\ - C ^ {e _ {i}} & i \notin \alpha \end{array} \right.} \end{array}\tag{3}
$$

Where the expected number of actions, $\left[ \rho _ { i } b _ { i } ^ { e _ { 1 } e _ { 2 } } + \right.$ $\rho b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } } \big ]$ , is comprised of $\rho _ { i } b _ { i } ^ { e _ { 1 } e _ { 2 } }$ ad actions by exclusive subscribers, and $\rho b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } }$ actions by multihomers, who use only the platform’s core service, regardless of $e _ { i }$ .

## 3.5 Timeline

Summarizing, the timeline of the model is as follows:

1. Platforms make expansion decisions $e _ { 1 }$ and $\boldsymbol { e } _ { 2 } .$

2. The final buyer partition $B ^ { e _ { 1 } e _ { 2 } }$ is determined $( B ^ { e _ { 1 } e _ { 2 } }$ is the buyer equilibrium).

3. Platforms set prices per user action $p _ { 1 }$ and $p _ { 2 } .$ .

4. Advertisers choose the platform(s) on which they place their ads, ??, and this determines platform profits.

## 3.6 Market Equilibrium

We define market equilibrium for the simultaneous move expansion game, which represents an environment where platforms’ development efforts are kept secret until new services are launched.

Definition 2: Market equilibrium is a couple $\left. \alpha ^ { \ast } , ( e _ { i } ^ { \ast } , p _ { i } ^ { \ast } ) _ { i = 1 , 2 } \right.$ , such that:

1. Advertisers’ platform choice is optimal, given platforms’ expansion and pricing decisions, and the resulting $B ^ { e _ { 1 } e _ { 2 } } \colon \alpha ^ { * } =$ $a r g m a x _ { \alpha \in A } \big \{ V \big ( \alpha | ( e _ { i } , p _ { i } ) _ { i = 1 , 2 } , B ^ { e _ { 1 } e _ { 2 } } \big ) \big \}$

2. Platform pricing is Nash equilibrium, given their expansion decisions, $B ^ { e _ { 1 } e _ { 2 } }$ , and $\alpha ^ { * } { : } p _ { i } ^ { * } =$ ?????????????? $\boldsymbol { \cdot } _ { i } ^ { e _ { 1 } e _ { 2 } } \big ( p _ { i } | p _ { j } ^ { * } \big )$ . Subgame equilibrium profits: $\Pi _ { i } ( e _ { 1 } , e _ { 2 } ) \equiv \pi _ { i } ^ { e _ { 1 } e _ { 2 } } \big ( p _ { i } ^ { * } | p _ { j } ^ { * } \big )$

3. Platforms’ expansion decisions are Nash equilibrium in the expansion game: $e _ { i } ^ { * } =$ ????????????Π ${ \bf \nabla } _ { i } \left( e _ { i } , e _ { j } ^ { \ast } \right)$

The sequential move version of the platform expansion game is also considered, as it represents a market where platforms’ development efforts are known. The sequential version is further used as a means of equilibrium selection, whenever multiple equilibria arise in the simultaneous move game.

The definition of market equilibrium for the sequential game will be similar, differing only in the equilibrium concept for optimal expansion decisions (Item 3 of Definition 2), which will be subgame perfect equilibrium.

## 4 Analysis

The expansion game is solved by backward induction. For each pair of expansion decisions (Timeline Step 1), the buyer partition is derived (Step 2), and platform pricing and profits follow, as platforms set profit maximizing prices (Step 3) based on their expected impact on advertisers’ choice and the resulting profits (Step 4). Comparing profits in each subgame $( e _ { 1 } , e _ { 2 } )$ platforms’ optimal expansion decisions are then determined. We begin by deriving platform pricing and profits for a given expansion subgame and its buyer equilibrium $\bar { B } ^ { e _ { 1 } e _ { 2 } }$

## 4.1 Pricing Equilibrium

In this subsection, we show that equilibrium prices and profits are constrained by the degree of user multihoming in the final partition. The intuition for this result is as follows. First, the profit-maximizing price per action induces multihoming by advertisers $( \mathrm { i . e . }$ , placing ads on both platforms). Multihoming advertisers suffer partial redundancy from reaching multihoming users through both platforms (as $V ^ { 1 2 } <$ $V ^ { 1 } + V ^ { 2 } )$ . In equilibrium, platforms internalize this redundancy by setting prices according to the incremental benefit of advertising on an additional platform.<sup>30</sup> Since this redundancy is a function of the mass of multihoming users, $b _ { 1 2 } ^ { e _ { 1 } \check { e } _ { 2 } }$ , equilibrium prices decrease in $b _ { 1 2 } ^ { e _ { 1 } e _ { 2 } }$ , and increase in the mass of exclusive users, $b _ { i } ^ { e _ { 1 } e _ { 2 } }$

Market power in the model thus stems from the degree of exclusivity and decreases in the degree of multihoming.

The following Proposition 1 provides a characterization of the pricing equilibrium and the resulting platform profits in a given subgame.

Proposition 1: Given $( e _ { 1 } , e _ { 2 } )$ and the resulting $B ^ { e _ { 1 } e _ { 2 } }$ platform ?? sets its price at $p _ { i } ^ { * }$ , where:

$$
p _ {i} ^ {*} = 1 - \frac {\rho^ {2} b _ {1 2} ^ {e _ {1} e _ {2}}}{\rho_ {i} b _ {i} ^ {e _ {1} e _ {2}} + \rho b _ {1 2} ^ {e _ {1} e _ {2}}}\tag{4}
$$

And its profits are given by:

$$
\pi_ {i} ^ {e _ {1} e _ {2}} = \rho_ {i} b _ {i} ^ {e _ {1} e _ {2}} + \rho (1 - \rho) b _ {1 2} ^ {e _ {1} e _ {2}} - C ^ {e _ {i}}\tag{5}
$$

Equilibrium prices decrease in the degree of multihoming, $\bar { b } _ { 1 2 } ^ { e _ { 1 } e _ { 2 } }$ , and increase in their degree of exclusivity, $b _ { i } ^ { e _ { 1 } \bar { e } _ { 2 } ^ { - } }$

## Proof: See Appendix A.

As noted, for a given pair of expansion decisions and resulting buyer subscription choices, Proposition 1 provides the profit maximizing price and subgame profits. This interim result will play an important role in developing intuition for platform expansion decisions, which will also incorporate changes in buyers’ platform choices following expansion.

## 4.2 Optimal Expansion Rule and Intuitions

Equilibrium profits increase in both exclusivity and multihoming, <sup>31</sup> yet expansion may have opposing effects on the masses of these groups. We thus proceed to derive an optimal expansion rule based on the expected profits in each subgame (given by Eq. (5)), which we then use in the derivation of expansion equilibria, for different parameter spaces.

We first introduce notation for expansion effects on the buyer partition that will be useful down the road. Let $\Delta b _ { k } ^ { e _ { i } } \vert _ { e _ { j } } \equiv b _ { k } ^ { E e _ { j } } - b _ { k } ^ { \bar { E } e _ { j } }$ , for $k \in \{ i , j , 1 2 \}$ , denote the change in the mass of group ??, resulting from $i \ ' \mathbf { s }$ expansion, given the opponent’s strategy $e _ { j } \in \{ \bar { E } , E \}$ Our symmetry assumption implies that $\Delta b _ { k } ^ { e _ { i } } | _ { \bar { E } } =$ $\Delta b _ { k } ^ { e _ { j } } | _ { \bar { E } }$ and $\Delta b _ { k } ^ { e _ { i } } | _ { E } = \Delta b _ { k } ^ { e _ { j } } | _ { E }$

The optimal expansion rule (henceforth, OER) for platform ?? , given $e _ { j }$ , is derived by solving $\pi _ { i } { } ^ { E e _ { j } } \geq$ $\pi _ { i } ^ { \bar { E } e _ { j } }$ (using Eq. (5)), and employing the above notation for expansion effects. This yields the following condition:

$$
\begin{array}{r l} & {O E R \colon e _ {i} | _ {e _ {j}} = E \Leftrightarrow \rho (1 - \rho) b _ {i} ^ {\bar {E} e _ {j}} + \rho (2 -} \\ & {\rho) \Delta b _ {i} ^ {e _ {i}} | _ {e _ {j}} + \rho (1 - \rho) \Delta b _ {1 2} ^ {e _ {i}} | _ {e _ {j}} - c \geq 0} \end{array}\tag{6}
$$

The OER represents the three effects of expansion: the ad-engagement effect and the quantity and price effects associated with changes in the user partition. Platform expansion decisions are thus based on weighing these effects against each other, and against the fixed cost of expansion, ??. Further discussion and insight into these effects is given as follows:

The ad-engagement effect. The ad-engagement effect refers to the increase in exclusive users engagement (or ad action) probability, brought on by expansion. Specifically, expansion increases these users’ engagement probability from $\rho$ to $( 2 \rho - \rho ^ { 2 } )$ an increase of $\rho ( 1 - \rho )$ in engagement probability for the mass of $b _ { i } ^ { \bar { E } e _ { j } }$ of preexpansion exclusive users. The ad-engagement effect is thus represented by the first term in the OER and is a positive effect aiming toward platform expansion. It follows that when the user partition does not change as a result of expansion, platforms will expand whenever the fixed cost ?? does not exceed the ad-engagement effect and the equilibrium is $( E , E )$ . Finally, note that the adengagement effect is non-monotonic in $\rho ,$ increasing in magnitude as $\rho$ increases for $\rho < 0 . 5$ , then decreasing in $\rho$ for $\rho > 0 . 5$

The quantity and price effects. The quantity effect is the direct effect of platform expansion—the change in user partition, which is endogenous in our setting. As expansion changes the mass of exclusive and multihoming users, it changes the expected number of ad actions sold by the platform. The price effect of expansion is the indirect effect of the change in user partition, as changes in multihoming and exclusivity affect prices (see Proposition 1). The quantity and price effects are jointly represented in the second and third term in the OER.

It is important to note that changes in the mass of multihomers exert opposing quantity and price effects. Namely, an increase (decrease) in multihoming entails a positive (negative) quantity effect, as the platform provides access to more (less) multihomers. At the same time, increased (decreased) multihoming leads to lower (higher) prices, implying a negative (positive) price effect.

Furthermore, our covered market assumption implies that changes in one group’s mass will always be accompanied by corresponding changes to one or both of the other two user groups. Therefore, the overall quantity and price effects of expansion will take changes in both exclusivity and multihoming into account.

## 4.3 Deriving Optimal Expansion Strategies

We now compare subgame profits to derive platform expansion strategies using the OER. This will require consideration of different parameter spaces and the resulting buyer partitions for each subgame.

We solve for expansion strategies separately for the case of $c = 0$ and for $c > 0$ . In reality, investment costs related to expansion are clearly positive and affect expansion decisions. Yet, the case of $c = 0$ is instructive, as it will allow us to highlight the effects on platform expansion strategies of user partition endogeneity, intraplatform service quality and complementarity, and users’ switching costs and response rates to ads.

Optimal expansion strategies will be summarized in Lemmas 1-2. Without loss of generality, assume that when $n = 1$ , Platform 1 expands, and the subgame is $( E , { \bar { E } } )$ (the subgame $( { \bar { E } } , E )$ is symmetric). For brevity, subscripts and superscripts are omitted whenever this does not create any ambiguity.

## Baseline: Buyer partition with no expansion, $\mathbf { \nabla } \mathbf { \mathbf { n } } = \mathbf { 0 } .$

$B ^ { \bar { E } \bar { E } }$ is both the initial partition, as well as a possible final partition. To derive $B ^ { \bar { E } \bar { E } }$ , we note that user ?? will multihome if $u _ { 1 2 } \geq u _ { i }$ , and thus whenever $m \leq q$ Since $m { \sim } U [ 0 , 1 ]$ , group masses in the initial user partition are given by $b _ { 1 2 } ^ { \bar { E } \bar { E } } = q$ and $b _ { 1 } ^ { \bar { E } \bar { E } } = b _ { 2 } ^ { \bar { E } \bar { E } } =$ $0 . 5 ( 1 - q )$ (as platforms are assumed to be symmetric), and profits are $\pi _ { i } ^ { \bar { E } \bar { E } } = 0 . 5 \rho ( 1 - q )$ + $\rho ( 1 - \rho ) q = 0 . 5 \rho + q [ 0 . 5 \rho - \rho ^ { 2 } ]$ . For the remainder of the analysis, we assume that $q < 1$ , such that all groups have positive mass in the initial partition.

## 4.3.1 Expansion Strategy When Rival Does Not Expand, $e _ { i } | _ { \overline { { E } } } .$

To derive platform ??’s expansion strategy, we find its impact on the buyer partition. Without loss of generality, let $e _ { 1 } = E , e _ { 2 } = \overline { { E } }$ . We consider both (weak) increases and decreases in the compatibility costs $\Delta m ^ { 1 } \geq 0$ and $\Delta m ^ { 1 } < 0 . { ^ { 3 2 } }$ Also recall that user switching away from the initial platform choice entails a switching costs of $s \geq 0$

The discussion in this and the following subsection will provide intuitions on user switching in each subgame, and its impact on expansion strategies. Detailed analysis, with full mathematical derivations of users’ decision lines and switching conditions is relegated to Appendix B.

## (a) Compatibility costs increase (weakly), $\Delta \mathbf { m } ^ { 1 } \geq \mathbf { 0 } .$

When Platform 1 expands and compatibility costs increase (weakly), $\Delta m ^ { 1 } \geq 0$ , the utility from choosing Platform 1 increases, while the utility from multihoming decreases (weakly). This implies that initial multihomers and Platform 2 users may switch to Platform 1. Those who multihome in the initial partition (for whom $m \leq q )$ will switch when the utility from choosing the expanded Platform 1 is higher than that of multihoming, i.e., $u _ { 1 } > u _ { 1 2 } \Leftrightarrow \mu > ( q -$ $\Delta q - \Delta m ^ { 1 } + s ) - m$ . We refer to $\mu = ( q - \Delta q -$ $\Delta m ^ { 1 } + s ) - m$ as multihomers’ decision line, denoted by $D L _ { M H }$ in Figure 1 below.

![](/api/attachments/XGZCJEV7/fulltext/images/aed8dfa31860f737cea487a98c38958478a2fe6e91ea17e250a752cdc5682ff7.jpg)  
Figure 1. User switching when only one platform expands, and compatibility costs increase (weakly) with expansion, i.e., for $( E , { \overline { { E } } } )$ and $\Delta m ^ { 1 } \geq 0 .$ . The case of intermediate switching costs, $s \in ( \Delta q , \overline { { \mu } } + \Delta q )$ , is depicted (such that both decision lines are in effect).

Platform 2 users in the initial partition (for whom $m >$ ??) will switch when $u _ { 1 } > u _ { 2 } \Leftrightarrow \mu > s - \Delta q$ . We refer to $\mu = s - \Delta q$ as the singlehomers’ decision line, denoted by $D L _ { 2 }$ in Figure 1 below. Figure 1 summarizes users’ switching for $( E , { \bar { E } } )$ and $\Delta m ^ { 1 } \geq 0$ Note that the decision lines’ locations, and whether or not they are binding, depend on parameter values. Figure 1 depicts the case with positive switching by both multi- and singlehomers, with some users from both groups remaining at their initial subscription choice. This is the case for intermediate levels of users’ switching cost, namely $s \in ( \Delta q , \bar { \mu } + \Delta q )$ See Appendix C for a full characterization of parameter ranges for decision lines’ possible locations (for Figure 1, and similarly for the subsequent Figures 2-4).

Figure 1 demonstrates that when compatibility costs (weakly) increase with expansion, there is nonnegative switching to Platform 1, depicted by the areas above both decision lines. This switching comes from both initial multihomers and subscribers of the rival platform. For all parameter values,<sup>33</sup> subscription to the expanded platform will (weakly) increase, whereas multihoming and singlehoming with the nonexpanded platform will weakly decrease.

As a result, expansion is a dominant strategy when expansion costs are sufficiently low, and the OER allows us to derive conditions on parameter ranges that support expansion (see Appendix B). The effect of expansion costs is analyzed in the Appendix, where we find lower and upper bounds $c _ { L }$ and $c _ { H } ,$ , such that for $c \leq c _ { L }$ expansion is always a dominant strategy and for $c > c _ { H }$ it is never a dominant strategy. When costs are midrange, expansion will depend on the relative magnitudes of $( c , s , \rho , q , \Delta q , \Delta m ^ { 1 } , \bar { \mu } )$ , that shift the LHS of the OER.<sup>34</sup>

## (b) Compatibility costs decrease, $\pmb { \Delta } \mathbf { m } ^ { 1 } < \mathbf { 0 } .$

When Platform 1’s expansion decreases compatibility costs, $\Delta m ^ { 1 } < 0$ , both the utility from Platform 1 as well as the utility from multihoming increase. Users may thus switch to either multihoming or to the expanded Platform 1.

Users who multihome in the initial partition (for whom $m \leq q )$ will switch to Platform 1 when this choice provides higher utility, $u _ { 1 } > u _ { 1 2 }$ . This defines multihomers’ decision line, $\mu = ( q - \Delta q + | \Delta m ^ { 1 } | +$ $s ) - m$ , denoted by $D L _ { M H }$ in Figure 2 below, where users above the line switch to the expanded platform.<sup>35</sup>

Platform 2 users (for whom $m > q )$ may switch to either Platform 1 or multihoming. Their switching decisions are derived by comparing utilities from each choice, yielding decision lines $D L _ { 2 a } , D L _ { 2 b }$ and $D L _ { 2 c } \mathrm { . }$ $\mu = s - \Delta q , m = q + | \Delta m ^ { 1 } | - s ,$ , and $\mu = ( q - \Delta q +$ $| \Delta m ^ { 1 } | ) - m \mid$ , respectively. These are graphed in Figure 2, which summarizes switching for $( E , { \bar { E } } )$ and $\Delta m ^ { 1 } < 0$ . Again, the decision lines’ location depends on parameter values and we depict the case where all decision lines are in effect, namely $s \in ( \Delta q , \bar { \mu } + \Delta q -$ $| \Delta m ^ { 1 } | ) \cap ( | \Delta m ^ { 1 } | - ( 1 - q ) , | \Delta m ^ { \bar { 1 } } | )$ and $| \Delta m ^ { 1 } | > \Delta q$ (see Appendix C for a characterization of other cases).

![](/api/attachments/XGZCJEV7/fulltext/images/1f21eea0814c77f4d7e66dec7ec1e87962d18afd7149b56049e8eaaede50f6b0.jpg)  
Figure 2. User switching when only one platform expands, and compatibility costs decrease with expansion, i.e., for $( E , { \overline { { E } } } )$ and $\Delta m ^ { 1 } < 0$ . The case of $s \in ( \Delta q , \overline { { \mu } } + \Delta q - | \Delta m ^ { 1 } | ) \cap ( | \Delta m ^ { 1 } | - ( 1 - q ) , | \Delta m ^ { 1 } | )$ and $| \Delta m ^ { 1 } | > \Delta q$ , is depicted (such that all decision lines are in effect).

As in scenario (a) above, there is nonnegative switching to Platform 1, which is depicted by the areas above the decision lines in Figure 2. Since users may only switch away from the nonexpanded platform, the mass of its subscribers will (weakly) decrease, whereas the mass of multihomers may either increase or decrease, depending on the relative magnitudes of the area above $D L _ { M H }$ and the area below $D L _ { 2 c }$ . Intuitively, increases in multihoming are only due to users who were initially singlehomers with the nonexpanded platform, and expansion is thus the optimal strategy for both increases and decreases in multihoming.

Formally, the OER inequality holds for $c = 0$ , and expansion is a dominant strategy when its cost is sufficiently low. See Appendix B for a detailed analysis, which includes the impact of expansion costs on the optimal expansion strategy. Lemma 1 summarizes the conditions for optimal expansion when the rival has not expanded.

Lemma 1: Expansion strategy given $e _ { j } = { \overline { { E } } } .$ When $e _ { j } = { \bar { E } } _ { }$ , and for $c _ { L } = c _ { L } | _ { \bar { E } }$ and $c _ { H } = c _ { H } | _ { \bar { E } }$

1. When $c \leq c _ { L }$ , expansion is a dominant strategy for all parameter values: $e _ { 1 } | _ { \bar { E } } \equiv E$

2. When $c > c _ { H } ,$ , expansion is a dominated strategy for all parameter values: $e _ { 1 } | _ { \bar { E } } \equiv \bar { E }$

3. When $c \in ( c _ { L } , c _ { H } ]$ : both $e _ { 1 } | _ { \bar { E } } = E$ and $e _ { 1 } | _ { \bar { E } } =$ ??<sup>̅</sup> are possible, and depend on the relative magnitudes of all parameters (?? $; s , \rho , q , \Delta q , | \Delta m ^ { 1 } | , \bar { \mu } )$

Proof: Follows from the above analysis of scenarios (a) and (b) and further derivations given in Appendix B).

## 4.3.2 Expansion Strategy When Rival Expands, ??<sub>??</sub>|<sub>??</sub>.

We continue to derive ?? ’s expansion strategy by studying its impact on the buyer partition, considering both (weak) increases and decreases in the compatibility costs as a result of expansion. As before, detailed derivations and analysis of the impact of positive expansion costs are relegated to Appendix B.

## (a) Compatibility costs increase (weakly), $\Delta \mathbf { m } ^ { 2 } \geq \mathbf { 0 } .$

Given that Platform 2 has expanded, expansion by Platform 1 that (weakly) increases compatibility costs $( \Delta m ^ { 2 } \ge 0 )$ , will (weakly) decrease the utility from multihoming, while increasing the utility from a choice of Platform 1 to the same level of utility derived from its expanded rival.

As a result, some initial multihomers will become exclusive users of either Platform 1 or 2, with equal probability (due to symmetry). Comparing utilities from single- and multihoming yields multihomers decision line, $\mu = ( q - \Delta q + s - \Delta m ^ { 2 } ) - m$ , denoted by $D L _ { M H }$ in Figure 3 below. There is no decision line for exclusive subscribers of Platforms 1 and 2, as they will optimally refrain from any switching in this subgame.

Switching decisions are summarized in Figure 3, which depicts the case where the decision line is in effect, i.e., $s \in ( \Delta m ^ { 2 } - ( q - \Delta q ) , \bar { \mu } + \Delta q + \Delta m ^ { 2 } )$ (see Appendix C for a characterization of other cases). As seen in Figure 3, there is nonnegative switching by multihomers to the expanded platforms (depicted by the area above multihomers’ decision line). As a result, expansion is a dominant strategy when expansion costs are sufficiently low (see Appendix B for an analysis of the impact of expansion costs).

![](/api/attachments/XGZCJEV7/fulltext/images/b25a7efdf11c220cfb6bd60a9825b94d556493102b274fac0ebe81f812e15744.jpg)  
Figure 3. : User switching when both platforms expand and compatibility costs weakly increase with expansion, i.e., for (??, ??) and $\Delta m ^ { 2 } \geq 0 .$ . The case of $s \in ( \Delta m ^ { 2 } - ( q - \Delta q ) , \overline { { \mu } } + \Delta q + \Delta m ^ { 2 } )$ is depicted (decision line is in effect).

## (b) Compatibility costs decrease, $\Delta \mathbf { m } ^ { 2 } < \mathbf { 0 } .$

Given that Platform 2 has expanded, expansion by Platform 1 that decreases compatibility costs $( \Delta m ^ { 2 } <$ 0) will increase the utility from multihoming while also increasing the utility from a choice of Platform 1 to the same level of utility derived from its expanded rival. In this case, multihomers will switch to Platform 1 or 2 (with equal probability) when the utility from singlehoming is higher, which defines multihomers’ decision line, $D L _ { M H }$ , given by $\mu = ( q - \Delta q +$ $| \Delta m ^ { 2 } | + s ) - m$ , and graphed in Figure 4 below.

At the same time, some exclusive users of Platforms 1 and 2 may switch to multihoming. Switching to multihoming is utility maximizing for $( m , \mu )$ combinations below the $D L _ { 1 , 2 }$ decision line $( \mu =$ $\left( q - \Delta q + | \Delta m ^ { 2 } | - s \right) - m )$ in Figure 4. Figure 4 summarizes users’ switching, depicting the case where both decision lines are in effect, i.e., $s < \mathrm { m i n } \{ \bar { \mu } -$ $( | \Delta m ^ { 2 } | - \Delta q ) , | \Delta m ^ { 2 } | - \Delta q \}$ (see Appendix C for a characterization of other cases).

The optimal expansion strategy will now depend on the relative switching to multihoming and to the expanded platforms, represented by the areas of the triangles in Figure 4. These, in turn, depend on the relative magnitudes of the changes in compatibility costs, incremental quality of the newly added service, intraplatform service complementarity, and switching costs. We distinguish between two cases (b1) and (b2), based on the relative magnitudes of these parameters, namely $| \Delta m ^ { 2 } | , \Delta q , \bar { \mu }$ and ??.

Case (b1): When the utility increase from multihoming is smaller than the average utility increase from singlehoming $\begin{array} { r } { ( \mathrm { i . e . , } \ | \Delta m ^ { 2 } | \leq \Delta q + } \end{array}$ $0 . 5 \bar { \mu } )$ , more multihomers switch to the expanded platforms than vice versa, and expansion is a dominant strategy when its cost is low.

Case (b2): When the utility increase from multihoming is higher than the average utility increase from singlehoming $( \mathrm { i . e . , ~ } | \Delta m ^ { 2 } | > \bar { \Delta q } + 0 . \bar { 5 } \bar { \mu } )$ , more singlehomers switch to multihoming than vice versa. Now, expansion is no longer a dominant strategy, and no-expansion may be optimal, even when expansion is costless (see Appendix B for detailed derivations of subcases (b1) and (b2), and the impact of expansion costs). Lemma 2 summarizes the conditions for optimal expansion given that the rival has expanded.

## Lemma 2: Expansion strategy given $e _ { j } = E$ . When $e _ { j } = E { \big . }$ , there are two scenarios:

1. For $\Delta m ^ { 2 } > 0$ and for $( \Delta m ^ { 2 } < 0$ ?????? $| \Delta m ^ { 2 } | \leq$ $\Delta q + 0 . 5 \bar { \mu } )$ there exist $c _ { L } = c _ { L } | _ { E }$ and $c _ { H } \in$ $\left\{ c _ { H } \big \vert _ { E , \Delta m ^ { 2 } > 0 } , c _ { H } \big \vert _ { E , \Delta m ^ { 2 } < 0 , ( b 1 ) } \right\}$ such that

a. When $c \leq c _ { L }$ , expansion is a dominant strategy for all parameter values: $e _ { i } | _ { E } \equiv E$

b. When $c > c _ { H } .$ , expansion is a dominated strategy for all parameter values: $e _ { i } | _ { E } \equiv \bar { E }$

c. When $c \in ( c _ { L } , c _ { H } ] ;$ : both $e _ { i } | _ { E } = E$ and $e _ { i } | _ { E } = \bar { E }$ are possible, and depend on the relative magnitudes of all parameters $( c , s , \rho , q , \Delta q , \Delta m ^ { 2 } , \bar { \mu } )$

![](/api/attachments/XGZCJEV7/fulltext/images/76230a9c26a09c03af58d466f9d1e53f6901379c0891ce5cb7460da8b9b521f1.jpg)  
Figure 4. User switching when both platforms expand and compatibility costs weakly increase with expansion, i.e., for (??, ??) and $\Delta m ^ { 2 } \geq 0 .$ . The case of $s \in ( \Delta m ^ { 2 } - ( q - \Delta q ) , \overline { { \mu } } + \Delta q + \Delta m ^ { 2 } )$ is depicted (decision line is in effect).

2. For $( \Delta m ^ { 2 } < 0$ ?????? $| \Delta m ^ { 2 } | > \Delta q + 0 . 5 \bar { \mu } )$ expansion is never a dominant strategy. There exists $c _ { H } = { c _ { H } } | _ { E , \Delta m ^ { 2 } < 0 , ( b 2 ) }$ , such that:

a. When $c \leq c _ { H } , e _ { i } | _ { E } = E$ if and only if $c +$ $\rho ^ { 2 } \big | \Delta b _ { i } ^ { e _ { i } } \big | _ { E } \big | \le \rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E }$

b. When $c > c _ { H } .$ , expansion is a dominated strategy for all parameter values: $\boldsymbol { e } _ { i } | _ { E } \equiv \boldsymbol { \bar { E } }$

Proof: Follows from the above analysis and from derivations in Appendix B.

## 4.4 Expansion Equilibrium and Comparative Statics

The results of Lemmas 1 and 2 are summarized in the following Corollary 1.

## Corollary 1: Optimal expansion strategies.

1. When expansion weakly increases the mass of exclusive subscribers of the expanding platform, there exist $c _ { H } \geq c _ { L } \geq 0$ , such that expansion is a dominant strategy for $c \leq c _ { L }$ , a dominated strategy for $c > c _ { H } .$ , and a possible optimal strategy for $c \in ( c _ { L } , c _ { H } ]$ , where the latter depends on the relative magnitudes of $( c , s , \rho , q , { \varDelta q } , { \varDelta m ^ { 1 } } , { \varDelta m ^ { 2 } } , { \bar { \mu } } )$

2. When expansion decreases the mass of exclusive subscribers of the expanding platform, there exist $c _ { H } > 0$ , such that expansion is a dominated strategy for $c > c _ { H }$ and a possible optimal strategy for $c \leq c _ { H }$ Specifically, for $c \leq c _ { H }$ , when $\varDelta m ^ { 2 } < 0$ $| \Delta m ^ { 2 } | > \Delta q + 0 . 5 \bar { \mu } , \ : e _ { i } | _ { E } = E$ if and only if $c + ~ \rho ^ { 2 } \big | \Delta b _ { i } ^ { e _ { i } } \big | _ { E } \big | \leq \rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E }$

The main effects discussed in Section 4.2 drive the result in Corollary 1, for the case of costless expansion or low expansion costs. When the cost of expansion is sufficiently low, expansion is a dominant strategy whenever it increases exclusivity and decreases multihoming—that is, when the price effect is positive, and expansion increases market power. On the other hand, when expansion decreases exclusivity and the price effect is negative, expansion is no longer a dominant strategy; rather, it depends on the relative magnitudes of the price, quantity and ad-engagement effects.

When the cost of expansion increases, it becomes a major force in the model, preventing expansion when it is high. For intermediate values of the expansion cost, the optimal expansion strategy will depend on the relative magnitudes of the expansion cost and the quantity, price and ad-engagement effects. As seen above, the quantity effect is created by users’ switching decisions, which depend on the relative benefits of intraplatform service quality and complementarity, and the costs of compatibility and switching.

The resulting expansion equilibrium is stated in Proposition 2, which considers the equilibrium for low, high, and intermediate expansion costs.

## Proposition 2: Expansion equilibrium.

1. Low expansion cost. There exists $c _ { L }$ such that for $c \leq c _ { L } \mathrm { : }$

a. For $\Delta m ^ { 2 } \geq 0$ and for $( \Delta m ^ { 2 } <$ 0 ?????? $| \Delta m ^ { 2 } | \leq 0 . 5 \bar { \mu } + \Delta q )$ , the expansion equilibrium is (??, ??).

b. For $\Delta m ^ { 2 } < 0$ ?????? $| \Delta m ^ { 2 } | > 0 . 5 \bar { \mu } + \Delta q$ , the expansion equilibrium is asymmetric, i.e., both $( E , { \bar { E } } )$ and $( \bar { E } , E )$ are equilibria, if $\rho ^ { 2 }$ $\left| \Delta b _ { i } ^ { e _ { i } } | _ { E } \right| + c > \rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E }$ , and otherwise the equilibrium is (??, ??).

2. High expansion cost. There exists $c _ { H }$ such that for $c > c _ { H }$ the equilibrium is (??<sup>̅</sup>, ??<sup>̅</sup>).

3. Intermediate expansion cost. There exist $c _ { L } , c _ { H } .$ such that for $c \in ( c _ { L } , c _ { H } )$ , all equilibrium types are possible (symmetric expansion, noexpansion, and asymmetric expansion) and the expansion equilibrium will depend on the parameters’ relative magnitudes.

## Proof:

1. Follows from Lemmas 1 and 2

for $c _ { L } = \operatorname* { m i n } \{ c _ { L } | _ { \bar { E } } , c _ { L } | _ { E } \} .$

2. Follows from Lemmas 1 and 2 for $c _ { H } = \mathrm { m a x }$

$$
\left\{c _ {H} \big | _ {\bar {E}}, c _ {H} \big | _ {E, \Delta m ^ {2} > 0}, c _ {H} \big | _ {E, \Delta m ^ {2} <   0, (b 1)}, c _ {H} \big | _ {E, \Delta m ^ {2} <   0, (b 2)} \right\}
$$

3. Follows from Lemmas 1 and 2

$$
\mathrm{for} c _ {L} = \max \left\{c _ {L} | _ {\bar {E}}, c _ {L} | _ {E} \right\} \mathrm{and} c _ {H} = \min
$$

$$
\left\{c _ {H} \big | _ {\bar {E}}, c _ {H} \big | _ {E, \Delta m ^ {2} > 0}, c _ {H} \big | _ {E, \Delta m ^ {2} <   0, (b 1)}, c _ {H} \big | _ {E, \Delta m ^ {2} <   0, (b 2)} \right\}
$$

The equilibrium is derived for specific parameter values by applying the OER.

Note that whenever the equilibrium in the simultaneous expansion game is asymmetric (i.e., both (??, ??<sup>̅</sup>) and (??<sup>̅</sup>, ??) are equilibria), then in the sequential-move game, the first mover will expand and the follower will not. Clearly, the expanded platform enjoys higher profits than its nonexpanded rival, and the sequential expansion game is thus characterized by a first mover advantage.

Proposition 2 (Parts 1-3) does not cover all possible ranges of ?? , as we do not explicitly write the equilibrium for:

$$
\begin{array}{l} c _ {L} \in (\min \{c _ {L} | _ {\bar {E}}, c _ {L} | _ {E} \}, \max \{c _ {L} | _ {\bar {E}}, c _ {L} | _ {E} \}) \quad \text {and} \quad c _ {H} \in \\ (\min \bigl \{c _ {H} | _ {\bar {E}}, c _ {H} | _ {E, \Delta m ^ {2} > 0}, c _ {H} | _ {E, \Delta m ^ {2} <   0, (b 1)}, c _ {H} | _ {E, \Delta m ^ {2} <   0, (b 2)} \bigr \}, \\ \max \bigl \{c _ {H} | _ {\bar {E}}, c _ {H} | _ {E, \Delta m ^ {2} > 0}, c _ {H} | _ {E, \Delta m ^ {2} <   0, (b 1)}, c _ {H} | _ {E, \Delta m ^ {2} <   0, (b 2)} \bigr \}). \end{array}
$$

This is to avoid repetition, as the derivation proceeds similarly, following from Lemmas 1 and 2.

The main take-away from the derivations presented is that even when expansion costs are low, expansion may not necessarily be an optimal strategy, as changes in the buyer partition resulting from expansion affect the pricing equilibrium and thus platforms’ expansion strategy. Interestingly, the equilibrium may be asymmetric even for symmetric platforms. Clearly, as the expansion cost increases, so does its impact on the equilibrium strategies.

Generally, for any combination of parameter values, the OER is used to derive the optimal expansion strategies and resulting equilibrium. We thus consider how the OER changes with each of the parameters. These comparative statics highlight the different forces at work in our model, all of which should be considered by platforms as they decide whether or not to expand into a service offered by a rival platform. The effects of changes in each parameter, while all others are held constant, are analyzed in Proposition 3 below.

Proposition 3: Comparative statics. For ?? that does not exceed the upper bounds derived, the optimal expansion strategy may change from expansion to noexpansion as a result of the following changes in parameters:

1. Increases in $c .$

2. Increases in ?? and ??, when expansion increases exclusivity.

3. Decreases in $\rho ,$ when $\rho < 0 . 5$

4. Decreases in $\Delta q$ and ${ \bar { \mu } } .$ .

5. Decreases in $\Delta m ^ { 1 } , \Delta m ^ { 2 }$ , when $\Delta m ^ { 1 } , \Delta m ^ { 2 } > 0$ and increases in $| \Delta m ^ { 1 } | , | \Delta m ^ { 2 } |$ when $\Delta m ^ { 1 } , \Delta m ^ { 2 } < 0 .$

Proof: We consider the effect of each parameter, holding all others constant.

The effect of ??: Increases in ?? shift the OER downward and may change the optimal strategy from ?? to ??<sup>̅</sup>.

The effect of $\rho \colon$ The ad-engagement effect, i.e., the additional ad actions derived from existing users following expansion is $\rho ( 1 - \rho ) b _ { i } ^ { \bar { E } e _ { j } }$ , which increases in $\rho$ for $\rho < 0 . 5$ and decreases in $\rho$ for $\rho > 0 . 5$ Increases in $\rho ,$ thus, shift the OER upward when $\rho <$ 0.5 and otherwise the effect on the OER will depend on the remaining parameters’ values.

The effect of ??: Increases in ?? reduce switching. When expansion increases exclusivity, increases in ?? decrease beneficial switching and will reduce the incentive to expand. Conversely, if expansion lowers exclusivity and increases multihoming, increases in ?? make expansion more beneficial, and may thus change the optimal expansion strategy from ??<sup>̅</sup> to ??.

The effect of $\pmb q \colon$ Increases in ?? imply a larger $u _ { 1 2 } -$ $u _ { i }$ , and thus lower the incentive to expand when expansion increases exclusivity. However, when expansion decreases exclusivity, expansion can counter the impact of increases in $q$ . Therefore, for $\Delta m ^ { 2 } < 0$ ?????? $| \Delta m ^ { 2 } | - \Delta q > 0 . 5 \bar { \mu }$ , increases in ?? may result in a switch from optimal no-expansion to expansion, and otherwise the reverse is possible.

The effect of $\Delta \mathbf { { q } } , \bar { \pmb { \mu } } ;$ Increases in $\Delta q , \bar { \mu }$ lead to a higher utility from singlehoming on an expanded platform and increase the benefit of expansion. Furthermore, increases in these parameters reduce the domain in which expansion decreases exclusivity (for $\Delta m ^ { 2 } <$ 0 ?????? $| \Delta m ^ { 2 } | - \Delta q > 0 . 5 \bar { \mu } )$ . Therefore, increases in $\Delta q$ and $\bar { \mu }$ will make expansion more likely, and decreases in $\Delta q$ and $\bar { \mu }$ may result in a switch from optimal expansion to no-expansion.

The effect of $\Delta { m } ^ { 1 } , \Delta { m } ^ { 2 } : \quad \mathrm { F o r } \quad \Delta { m } ^ { 1 } , \Delta { m } ^ { 2 } >$ 0, increases in these parameters reduce the utility from multihoming and increase singlehoming and the benefits of expansion. For $\Delta m ^ { 1 } , \bar { \Delta } m ^ { 2 } < 0$ , decreases in $| \Delta m ^ { 1 } | , | \Delta m ^ { \frac { 1 } { 2 } } |$ reduce the utility from multihoming and increase the benefits of expansion. Moreover, for $\Delta m ^ { 2 } < 0$ ?????? $| \Delta m ^ { 2 } | - \Delta q > 0 . 5 \bar { \mu }$ , decreases in $| \Delta m ^ { 2 } |$ reduce the domain in which expansion decreases exclusivity. This implies that increases in $\Delta m ^ { 1 } , \Delta m ^ { 2 }$ lead to more expansion when $\Delta m ^ { 1 } , \Delta m ^ { 2 } >$ 0 and decreases in $| \bar { \Delta m ^ { 1 } } | , | \Delta m ^ { 2 } |$ lead to more expansion when $\Delta m ^ { 1 } , \Delta m ^ { 2 } < 0$

## 4.5 A Potential Prisoner’s Dilemma

In this section, we highlight a noteworthy equilibrium outcome—a Prisoner’s Dilemma. This is an equilibrium where both platforms optimally choose to expand but would have enjoyed higher profits by coordinating a “no-expansion” equilibrium. With “platform imperialism” prevalent in many digital markets, it is important to investigate the potential for a Prisoner’s Dilemma in our model and develop intuitions for this interesting scenario.

Thus far, our model has shown that expansion is not necessarily an optimal strategy for platforms, and that its benefits must be weighed against its costs and a potentially negative price effect resulting from more direct competition with the rival platform (represented by increased multihoming). Now we consider the case where expansion is individually rational, yielding a symmetric expansion equilibrium, (??, ??), with profits that are lower than the no-expansion profits, $\pi ^ { { \bar { E } } { \bar { E } } } >$ $\pi ^ { E E }$ . When would this be the case?

Intuitively, when the effect of intensified competition is not too strong and expansion costs are not prohibitively high, platforms will expand to increase the probability of an ad-related action by their exclusive subscribers while still benefiting from the baseline level of ad-actions by multihomers (who subscribe to core services). Taken together, these imply higher profits from the advertisers’ side of the market for the expanded platform, given the rival’s strategy. This intuition holds even when multihoming increases and exclusivity decreases following expansion (as long as the price effect is not too strong), and this is precisely the case where a Prisoner’s Dilemma may arise. Specifically, when multihoming increases and exclusivity decreases with expansion, it is possible to identify a range of expansion costs for which coordinated no-expansion would have resulted in higher profits. In this cost range, higher profits under no-expansion are due to higher exclusivity with reduced price competition, while platforms do not incur any expansion costs.

This outcome is a subcase of the one shown in Case (b2) of Figure 4 (in 4.3.2 above). Recall that in this Case (b2), expansion results in a utility increase from multihoming that is higher than the average utility increase from singlehoming (i.e., $| \Delta m ^ { 2 } | > \Delta q { \mathrm { ~ + ~ } }$ $0 . 5 \bar { \mu } )$ . This implies more switching to multihoming than to singlehoming when both platforms expands. Thus, platforms will expand only when the cost of expansion is sufficiently low, namely when $c \leq$ $\rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E } - \rho ^ { 2 } \big | \Delta b _ { i } ^ { e _ { i } } \big | _ { E } \big |$ . Within the cost range that ensures a symmetric expansion equilibrium when the expansion cost is sufficiently high, the (??, ??) equilibrium constitutes a Prisoner’s Dilemma. This result is formally stated in the following proposition.

## Proposition 4: A Prisoner’s Dilemma. The equilibrium is a Prisoner’s Dilemma when $\Delta m ^ { 2 } <$

0 ?????? $| \Delta m ^ { 2 } | > 0 . 5 \bar { \mu } + \Delta q$ , and the expansion cost is in the following range $c \in ( \rho ( 1 - 2 \rho ) b _ { 1 } ^ { \bar { E } \bar { E } } +$ $\rho ^ { 2 } b _ { 1 } ^ { E E } , \rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E } - \rho ^ { 2 } \big | \Delta b _ { i } ^ { e _ { i } } \big | _ { E } \big | \big ] .$

## Proof: See Appendix A.

The above analysis demonstrates the possibility of individually rational expansion even when it implies lower profits for both platforms. While common in strategic interactions, this type of outcome is interesting and noteworthy for platforms.

## 5 Discussion and Managerial Implications

## 5.1 Managerial Implications

We have presented a game-theoretic framework for the analysis of online platforms’ expansion decisions when the buyer partition is endogenous. Our analysis demonstrates that expansion may not be optimal when it intensifies competition between the platforms; that is, when it decreases the degree of user singlehoming and increases multihoming, thus lowering equilibrium prices charged to advertisers.

The model provides an optimal expansion rule that takes into account the relative impacts of various parameters affecting the costs and benefits of expansion, such as expansion cost, same-platform service complementarity, users’ switching costs, platform compatibility, users’ ad-engagement rates, and more. This optimal expansion rule may be used by practitioners to help structure decision-making regarding expansion into a service already offered by a rival platform.

Deriving conditions for different types of expansion equilibria, our analysis demonstrates that the expansion equilibrium may be asymmetric, even when platforms are symmetric, and that both symmetric expansion and no-expansion are possible outcomes. The key takeaway for managers is that platforms should not always expand into services offered by their rivals, and that careful consideration of different market characteristics is required when devising expansion strategies.

Moreover, the model highlights the possibility of a Prisoner’s Dilemma, a notable subcase of a symmetric expansion equilibrium, which is individually rational, yet characterized by lower profits compared to coordinated no-expansion. Managers should, therefore, seek to understand the circumstances that may give rise to such an inevitably “bad equilibrium,” especially when coordination is not possible (e.g., due to antitrust laws).

## 5.2 Discussion and Extensions

The possibility of intensified competition following platform expansion drives many of our model’s results. In our model, such intensified competition is due to expansion effects on interplatform compatibility that impact the degree of user multihoming and exclusivity. Alternatively, one may consider other mechanisms driving expansion effects on the user partition (and hence, affecting the level of competition in the market). Possible examples are choice set effects, or changes in users’ perceptions of platform identity and service differentiation as a result of expansion, where each of these may impact buyers’ decision-making processes and subsequent platform choice.

The model may also be extended to consider subscription to services of the same type from both platforms, in lieu of the simplifying assumption that users subscribe to one service of each type. In such a general setting, the level of substitution or complementarity between same-type services will affect the partition of users and their multihoming behavior postexpansion. The model may further inform expansion decisions when the market is not covered and platforms expand to redefine market boundaries and reach untapped user segments. In such a variant of the model, new buyers’ platform choices will continue to depend on platforms’ expansion decisions and multihoming will increase with expansion when compatibility costs decrease. <sup>36</sup> The covered market assumption may thus be relaxed, and our main results will qualitatively hold.<sup>37</sup>

Finally, note that in our framework, utility does not depend on users’ expectations regarding the number of subscribers on each platform, i.e., we abstract from modeling the same-side network effect. Leaving buyer expectations outside the scope of our model is a choice made for two related reasons. First, when utility is a function of expectations of other users’ subscription decisions, the result is often a winner-take-all equilibrium, where all users congregate on the same platform (e.g., Calliaud & Jullien, 2003; Zhu & Iansiti, 2012). Second, due to the potential for obtaining such knife-edge equilibria, expectations have already been the focus of several papers in the platforms literature (e.g., Hagiu & Halaburda, 2011; Halaburda, Jullien, & Yehezkel, 2016; Katz & Shapiro, 1985). We have thus abstracted away from modeling expectations, in order to focus on the other effects of expansion discussed above. Future work may consider endogenous user expectations and the implied same-side network effect within a strategic expansion game.

## 5.3 Concluding Remarks

Our general framework is amenable to different market settings and may be applied by managers even without fully specifying assumptions on buyers’ decisionmaking—as the OER may be used based on forecasts on the partition of users following expansion. Whenever multihoming may increase, caution is advised, as expansion may decrease, rather than increase, profits. Moreover, in real-world situations, the cost of developing new services must be carefully weighed against the benefits of new service introduction, which may be low with an incumbent service already in place.

Returning to the example of Google Plus: Does the model imply that Google should not have expanded into social networking? Google Plus did not succeed in stealing away (most) Facebook users and it seems that any effects on the user partition were minor at best. The main benefit of this expansion was generating more ad engagement from Google’s existing user base with the addition of valuable social network data. Given the limited use of Google Plus (compared to Facebook), this benefit should be weighed against the cost of expansion.

Expansion effects on the user partition may play a more prominent role for the many platforms expanding into content streaming services. Video streaming services are likely to complement each other and create an “increased appetite” for streamed content. Therefore, expansion into content streaming may increase users’ multihoming with competitors. For example, Amazon users who start using Amazon Instant Video may also increase their consumption of Netflix, Hulu, and other competitors. Expansion into content streaming should therefore take such strategic effects into account.

## References

Adner, R., Chen J., & Zhu, F. (2015). Frenemies in platform markets: The case of Apple’s iPad vs. Amazon’s Kindle (Harvard Business School Working Paper No. 15-087).

Ambrus, A., Calvano, E., & Reisinger, M. (2013). Either or both competition: a “two-sided” theory of advertising with overlapping viewerships (Economic Research Initiatives at Duke Working Paper No. 170).

Amelio, A., & Jullien, B. (2012). Tying and freebies in two-sided markets. International Journal of Industrial Organization, 30(5), 436-446.

Anderson, S. P., & Coate, S. (2005). Market provision of broadcasting: a welfare analysis. The Review of Economic Studies, 72(4), 947-972.

Anderson, S. P., Foros, O., & Kind, H. J. (2011). Competition for advertisers in media markets (Working paper). Retrieved from https://economics.virginia.edu/sites/econo mics.virginia.edu/files/anderson/AFK-Comp4AdsAnd4Vwrs.pdf

Anderson, S. P., Foros, O., Kind, H. J., & Peitz, M. (2012). Media market concentration, advertising levels, and ad prices. International Journal of Industrial Organization, 30(3), 321- 325.

Armstrong, M. (2006). Competition in two-sided markets. RAND Journal of Economics, 37(3), 668-691.

Athey, S., Calvano, E., & Gans, J. S. (2013). The impact of the internet on advertising markets for news media (Rotman School of Management Working Paper No. 2180851).

Boudreau, K. J. (2010). Open platform strategies and innovation: Granting access vs. devolving control. Management Science, 56(10), 1849- 1872.

Boudreau, K. J., & Hagiu, A. (2008). Platform rules: Multi-sided platforms as regulators (Harvard Business School Working Paper No. 09-061).

Cabral, L. (2011). Dynamic price competition with network effects. Review of Economic Studies, 78(1), 83-111.

Caillaud, B., & Jullien, B. (2001). Competing cybermediaries. European Economic Review, 45(4), 797-808.

Caillaud, B., & Jullien, B. (2003). Chicken & egg: Competition among intermediation service

providers. The RAND Journal of Economics, 34(2), 309-328.

Casadesus-Masanell, R., & Ruiz-Aliseda, F. (2009). Platform competition, compatibility, and social efficiency (Harvard Business School Working Paper No. 09-058).

Chellappa, R. K., & Mukherjee, R. (2015). Platform preannouncement strategies: a duopoly of twosided markets (Working paper). Retrieved from http://www.teisworkshop.org/papers/2016/ TEIS\_2016\_5\_Mukherjee.pdf

Chen, J., Dou, Y., & Wu, D. J. (2012). Platform pricing with strategic buyers. Proceedings of the 45th Hawaii International Conference on System Sciences (pp. 4535-4544).

Choi, J. P. (2010). Tying in two-sided markets with multi-homing. The Journal of Industrial Economics, 58(3), 607-626.

Crampes, C., Haritchabalet, C., & Jullien, B. (2009). Advertising, competition and entry in media industries. The Journal of Industrial Economics, 57(1), 7-31.

The Economist (2012). Another game of thrones. Retrieved from https://www.economist.com/ briefing/2012/12/01/another-game-of-thrones

Edwards, J. (2012). Amazon launches an ad exchange to rival Facebook and Google. Business Insider. Retrieved from https://www.businessinsider .com/amazon-launches-an-ad-exchange-torival-facebook-and-google-2012-12

Edwards, J. (2013). Google is now bigger than both the magazine and newspaper industries. Business Insider. Retrieved from https://www. businessinsider.com/google-is-bigger-than-allmagazines-and-newspapers-combined-2013- 11

Eisenmann, T. R., Parker, G., & Van Alstyne, M. (2006). Strategies for two-sided markets. Harvard Business Review. Retrieved from https://hbr.org/2006/10/strategies-for-twosided-markets

Eisenmann, T. R., Parker, G., & Van Alstyne, M. (2008). Opening platforms: How, when and why? Harvard Business School Working Paper Summaries (Harvard Business School Working Paper No. 09-030). Retrieved from https://hbswk.hbs.edu/item/opening-platformshow-when-and-why

Eisenmann, T., Parker, G., & Van-Alstyne, M. (2011). Platform envelopment. Strategic Management Journal, 32(12), 1270-1285.

Evans, D. S. (2009). The online advertising industry: Economics, evolution, and privacy. The Journal of Economic Perspectives, 23(3), 37- 60.

Evans, J. (2013). Google Plus is like Frankenstein’s monster. Retrieved from https://techcrunch. com/2013/07/06/google-plus-is-likefrankensteins-monster

Griffith, E. (2012). Watch out, Google, Facebook, Apple: Amazon is coming for your advertisers. Retrieved from https://pando.com/2012/12/17/ watch-out-google-facebook-apple-amazon-iscoming-for-your-advertisers/

Hagiu, A. (2006). Pricing and commitment by twosided platforms. The RAND Journal of Economics, 37(3), 720-737.

Hagiu, A. (2009a). Multi-sided platforms: From microfoundations to design and expansion strategies (Harvard Business School Strategy Unit Working Paper No. 09-115).

Hagiu, A. (2009b). Two-sided platforms: Product variety and pricing structures. Journal of Economics & Management Strategy, 18(4), 1011-1043.

Hagiu, A. (2011). Quantity vs. quality and exclusion by two-sided platforms (Harvard Business School Strategy Unit Working Paper No. 11-125).

Hagiu, A., & Halaburda, H. (2011). Expectations, network effects and platform pricing (Harvard Business School Strategy Unit Working Paper No. 12-045).

Hagiu, A., & Lee, R. S. (2011). Exclusivity and control. Journal of Economics & Management Strategy, 20(3), 679-708.

Halaburda, H., & Yehezkel, Y. (2013). Platform competition under asymmetric information. American Economic Journal: Microeconomics, 5, 22-68.

Halaburda, H., & Yehezkel, Y. (2016). The role of coordination bias in platform competition. The Journal of Economics and Management Strategy, 25(2), 274-312.

Halaburda, H., Jullien, B., & Yehezkel, Y. (2016). Dynamic competition with network externalities: Why history matters (CESifo Working Paper Series No. 5847).

Jullien, B. (2008). Price skewness and competition in multi-sided markets (IDEI Working Papers No. 504).

Kang, C. (2012). Google announces privacy changes across products; Users can’t opt out. Washington Post. Retrieved from

https://archive.org/post/409299/googleannounces-privacy-changes-across-productsusers-cannot-opt-out

Katz, M. L., & Shapiro, C. (1985). Network externalities, competition, and compatibility. The American Economic Review, 75(3), 424- 440.

Parker, G., & Van Alstyne, M. (2005). Two-sided network effects: A theory of information product design. Management Science, 51(10), 1494-1504.

Parker, G., & Van Alstyne, M. (2018). Innovation, openness, and platform control. Management Science, 64(7), 3015-3032.

Rasch, A., & Wenzel, T. (2014). Content provision and compatibility in a platform market. Economic Letters, 124(3), 478-481.

Reisinger, M. (2012). Platform competition for advertisers and users in media markets. International Journal of Industrial Organization, 30(2), 243-252.

Rochet, J.-C., & Tirole, J. (2002). Cooperation among competitors: some economics of payment card associations. The RAND Journal of Economics, 33(4), 549-570.

Rochet, J.-C., Tirole, J. (2003). Platform competition in two-sided markets. Journal of the European Economic Association, 1(4), 990-1029.

Rochet, J.-C., & Tirole, J. (2006). Two-sided markets: a progress report. Rand Journal of Economics, 37(3), 645-667.

Tassy, P. (2011). A eulogy for Google Plus. Forbes. Retrieved from https://www.forbes.com/sites/ insertcoin/2011/08/15/a-eulogy-for-googleplus/#7786e2351f93

Taube, A. (2013). Here’s a glimpse inside Amazon’s secretive 800-million-dollar ad business. Business Insider. Retrieved from https://www. businessinsider.com/heres-a-glimpse-insideamazons-secretive-800-million-ad-business-2013-10

Veiga A., & Weyl, E. G. (2016). Product design in selection markets. The Quarterly Journal of Economics, 131(2), 1007-1056.

Weyl, E. G. (2010). A price theory of multi-sided platforms. The American Economic Review 100(4), 1642-1672.

Zhu, F., & Iansiti, M. (2012). Entry into platformbased markets. Strategic Management Journal, 33(1), 88-106.

## Appendix A. Proof of Propositions

## Proof of Proposition 138

Given $( e _ { 1 } , e _ { 2 } )$ and ??, advertisers place ads on both platforms whenever $V ^ { 1 2 } \ge V ^ { 1 } , V ^ { 2 } , 0$ , and choose a single platform ?? whenever $V ^ { i } > V ^ { 1 2 } , V ^ { j } , 0 ^ { 3 9 }$ . Solving $V ^ { 1 2 } \ge V ^ { j }$ we find that $\alpha ^ { * } = \{ 1 , 2 \}$ whenever $p _ { i } \leq p _ { i } ^ { * }$ . Furthermore, note that $V ^ { i } \geq V ^ { j }$ if and only if $p _ { i } \leq \tilde { p } _ { i } ( p _ { j } )$ , where $\begin{array} { r } { \tilde { p } _ { i } \big ( p _ { j } \big ) \equiv \frac { \left[ \rho _ { i } b _ { i } - \rho _ { j } b _ { j } \right] + p _ { j } \left[ \rho _ { j } b _ { j } + \rho b _ { 1 2 } \right] } { \rho _ { i } b _ { i } + \rho b _ { 1 2 } } } \end{array}$ . It is easily verified that $p _ { i } ^ { * } = \tilde { p } _ { i } \bigl ( p _ { j } ^ { * } \bigr )$ , thus $V ^ { 1 } = \ V ^ { 2 } = V ^ { 1 2 } = \rho ^ { 2 } b _ { 1 2 } \ \mathrm { f o r } \ p _ { i } = p _ { i } ^ { * } , i = 1 , 2$

We show that pricing at $p _ { i } ^ { * }$ is profit maximizing. First note that $i \in \alpha ^ { * }$ for all $p _ { i } \leq p _ { i } ^ { * }$ , and the profit maximizing price in this region is clearly $p _ { i } = p _ { i } ^ { * }$ . We now consider $p _ { i } > p _ { i } ^ { * }$ . Pricing at $p _ { i } > 1$ leads to $i \not \in \alpha ^ { * }$ and zero revenue with $\pi _ { i } = - C ^ { e _ { i } } \leq 0$ , and is not profit maximizing. Therefore assume $p _ { i } \in ( p _ { i } ^ { * } , 1 ) \colon \mathrm { i f } p _ { j } \in \left( p _ { j } ^ { * } , 1 \right)$ and that only one platform is chosen by advertisers—assume that ?? is chosen, i.e., $V ^ { i } \geq V ^ { j }$ . This implies $\pi _ { i } = - C ^ { e _ { j } } \leq 0$ , and a profitable deviation to $\boldsymbol { p } _ { j } ^ { * }$ . Alternatively, if $p _ { i } \in ( p _ { i } ^ { * } , 1 )$ and $p _ { j } = p _ { j } ^ { * }$ then $V ^ { j } > V ^ { i }$ , thus $i \not \in \alpha ^ { * }$ and ?? has a profitable deviation to $p _ { i } = p _ { i } ^ { * }$ . We have thus shown that for any price $p _ { i } \neq p _ { i } ^ { * }$ there exists a profitable deviation to $p _ { i } = p _ { i } ^ { * }$ . Nash equilibrium prices in a given subgame are thus $p _ { i } = p _ { i } ^ { * }$ for $i = 1 , 2$ . Substituting for $p _ { i } ^ { * }$ in Eq. (3) yields the expression in Eq. (5) for platforms’ profits in subgame $( e _ { 1 } , e _ { 2 } )$

To see that $p _ { i } ^ { * }$ decreases in $b _ { 1 2 }$ and increases in $b _ { i }$ we examine the following first order derivatives:

$$
\begin{array}{r} (1) \frac {\partial p _ {i} ^ {*}}{\partial b _ {1 2}} = - \frac {\rho^ {2} \rho_ {i} b _ {i}}{(\rho_ {i} b _ {i} + \rho b _ {1 2}) ^ {2}} <   0 \\ (2) \frac {\partial p _ {i} ^ {*}}{\partial b _ {i}} = \frac {\rho^ {2} \rho_ {i} b _ {1 2}}{(\rho_ {i} b _ {i} + \rho b _ {1 2}) ^ {2}} > 0 \end{array}
$$

## Proof of Proposition 4

A Prisoner’s Dilemma (PD) would arise when expansion increases multihoming, and therefore $b _ { 1 } ^ { \bar { E } \bar { E } } \geq b _ { 1 } ^ { E E } \geq b _ { 1 } ^ { \bar { E } E }$ . This is depicted in Figure 4, Case (b2), where the utility increase from multihoming is higher than the average utility increase from singlehoming $( \mathrm { i . e . , } | \Delta m ^ { 2 } | > \Delta q + 0 . 5 \bar { \mu } )$ , and thus more singlehomers switch to multihoming than vice versa. In this case, i.e., for $\Delta m ^ { 2 } < 0$ ?????? $| \Delta m ^ { 2 } | > 0 . 5 \bar { \mu } + \Delta q$ : the equilibrium is $( E , E ) \Leftrightarrow c \leq \rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E } - \rho ^ { 2 } \big | \Delta b _ { i } ^ { e _ { i } } \big | _ { E } \big |$ (as stated in Proposition 2).

We now derive the condition for a PD, namely $\pi _ { 1 } ^ { E E } < \pi _ { 1 } ^ { \bar { E } \bar { E } }$ . Using (5), this profit inequality becomes-

$$
\rho b _ {1} ^ {\bar {E} \bar {E}} + \rho (1 - \rho) b _ {1 2} ^ {\bar {E} \bar {E}} > \rho (2 - \rho) b _ {1} ^ {E E} + \rho (1 - \rho) b _ {1 2} ^ {E E} - c
$$

Symmetry implies $b _ { 1 2 } = 1 - 2 b _ { 1 }$ for both (??, ??) and $( { \bar { E } } , { \bar { E } } )$ , and thus the PD inequality is equivalent to

$$
c > \rho (1 - 2 \rho) b _ {1} ^ {\bar {E} \bar {E}} + \rho^ {2} b _ {1} ^ {E E}
$$

Combining the conditions for $( E , E )$ and PD, and arranging, we find the range of expansion costs for which a PD will arise. Namely, a PD expansion equilibrium is the outcome for

$$
c \in \left(\rho (1 - 2 \rho) b _ {1} ^ {\bar {E} \bar {E}} + \rho^ {2} b _ {1} ^ {E E}, \rho (1 - \rho) b _ {1} ^ {\bar {E} E} - \rho^ {2} \big | \Delta b _ {i} ^ {e _ {i}} | _ {E} \big | \right]
$$

This domain is nonempty whenever $\rho ( 1 - 2 \rho ) b _ { 1 } ^ { \bar { E } \bar { E } } + \rho ^ { 2 } b _ { 1 } ^ { E E } < \rho b _ { 1 } ^ { \bar { E } E } - \rho ^ { 2 } b _ { 1 } ^ { E E }$ , i.e., when the probability of an ad action is sufficiently large: $\begin{array} { r } { \rho > \frac { b _ { 1 } ^ { \overline { { E } } \overline { { E } } } - b _ { 1 } ^ { \overline { { E } } E } } { 2 \left( b _ { 1 } ^ { \overline { { E } } \overline { { E } } } - b _ { 1 } ^ { E E } \right) } } \end{array}$

## Appendix B. Optimal Expansion Strategies: Full Derivations for Section 4.3

Expansion Strategy When Rival Does Not Expand, $e _ { i } | _ { \overline { { E } } } .$

(a) Compatibility costs increase $( w e a k l y ) , \ : \Delta m ^ { 1 } \geq 0 .$

Deriving $D L _ { M H }$ in Figure 1:

$u _ { 1 } > u _ { 1 2 } \Leftrightarrow q + \Delta q + \mu - s > 2 q - ( m + \Delta m ^ { 1 } )$ . This implies $\mu > ( q - \Delta q - \Delta m ^ { 1 } + s ) - m$ . Therefore, $D L _ { M H }$ is given by $\mu = ( q - \Delta q - \Delta m ^ { 1 } + s ) - m .$

Deriving $D L _ { 2 } ;$ :

$u _ { 1 } > u _ { 2 } \Leftrightarrow q + \Delta q + \mu - s > q$ . This implies $\mu > s - \Delta q$ . Therefore, $D L _ { 2 }$ is given by $\mu = s - \Delta q$

## Deriving Expansion Strategies:

For all parameter values, $\Delta b _ { 1 2 } \leq 0 , \Delta b _ { 1 } \geq 0 , \Delta b _ { 2 } \leq 0$ and $\Delta b _ { 1 } = | \Delta b _ { 1 2 } | + | \Delta b _ { 2 } |$ . Substituting into the OER we have $\begin{array} { r } { e _ { 1 } | _ { \bar { E } } = E \Leftrightarrow \rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } \bar { E } } + \rho ( 2 - \rho ) [ | \Delta b _ { 1 2 } | + | \Delta b _ { 2 } | ] - \rho ( 1 - \rho ) | \Delta b _ { 1 2 } | - c \geq 0 . } \end{array}$

Simplifying, the inequality becomes $\rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } \bar { E } } + \rho ( 2 - \rho ) | \Delta b _ { 2 } | + \rho | \Delta b _ { 1 2 } | - c \geq 0$ , which always holds when $c = 0$

To analyze the effect of $c > 0 .$ , we find lower and upper bounds $c _ { L }$ and $c _ { H }$ such that for $c \leq c _ { L }$ expansion is always a dominant strategy and for $c > c _ { H }$ it is never a dominant strategy. These bounds will vary by subgame and by the effect of expansion on the compatibility cost, and we thus use the full notation $c _ { L } | _ { e _ { j } , \Delta m ^ { n } } , c _ { H } | _ { e _ { j } , \Delta m ^ { n } }$ to summarize and compare different cases. The lower bound, $c _ { L } ,$ , supports expansion when the incremental profits are minimal, i.e., only the adengagement effect drives expansion: $\Delta b _ { 1 } = \Delta b _ { 2 } = \Delta b _ { 1 2 } = 0$ . Employing the OER yields $e _ { 1 } | _ { \bar { E } } = E \Leftrightarrow \rho ( 1 -$ $\rho ) b _ { 1 } ^ { \bar { E } \bar { E } } - c \geq 0 \Rightarrow c _ { L } | _ { \bar { E } , \Delta m ^ { 1 } > 0 } = 0 . 5 \rho ( 1 - \rho ) ( 1 - q )$

The upper bound $c _ { H }$ represents prohibitive costs such that expansion is never optimal, even when the increase in exclusivity and decrease in multihoming are maximal, i.e., $b _ { 1 } ^ { E \bar { E } } = 1 , b _ { 2 } ^ { E \bar { E } } = 0$ and $b _ { 1 2 } ^ { E \bar { E } } = 0$ . Solving $\pi _ { 1 } ^ { E \bar { E } } < \pi _ { 1 } ^ { \bar { E } \bar { E } }$ ⇔ $\rho ( 2 - \rho ) \cdot 1 - c < 0 . 5 \rho + q [ 0 . 5 \rho - \rho ^ { 2 } ]$ we find $c _ { H } | _ { \bar { E } , \Delta m ^ { 1 } > 0 } = \rho ( 0 . 5 - \rho ) ( 1 - q ) + \rho .$

When costs are midrange, $c \in \left( c _ { L } | _ { \bar { E } , \Delta m ^ { 1 } > 0 } , c _ { H } | _ { \bar { E } , \Delta m ^ { 1 } > 0 } \right]$ , expansion will depend on the relative magnitudes of $( c , s , \rho , q , \Delta q , \Delta m ^ { 1 } , \bar { \mu } )$ that shift the LHS of the OER. A discussion of comparative statics for all parameters is provided in section 4.4.

(b) Compatibility costs decrease, $\varDelta m ^ { 1 } < 0$

Deriving $D L _ { M H }$ in Figure 2:

$u _ { 1 } > u _ { 1 2 } \Leftrightarrow q + \Delta q + \mu - s > 2 q - ( m + \Delta m ^ { 1 } )$ . This implies $\mu > ( q - \Delta q + | \Delta m ^ { 1 } | + s ) - m$ . Therefore, $D L _ { M H }$ is given by $\mu = ( q - \Delta q + | \Delta m ^ { 1 } | + s ) - m .$

Deriving $D L _ { 2 a }$ and $D L _ { 2 b }$ in Figure 2:

A user will not switch to Platform 1 whenever $u _ { 1 } \leq u _ { 2 } \Leftrightarrow \mu \leq s - \Delta q$ . Therefore, $D L _ { 2 a }$ is given by $\mu = s - \Delta q$

A user will not switch to multihoming whenever $u _ { 1 2 } < u _ { 2 } \Leftrightarrow m > q + | \Delta m ^ { 1 } | - s$ . Therefore, $D L _ { 2 b }$ is given by $m =$ $q + | \Delta m ^ { 1 } | - s$

Deriving $D L _ { 2 c }$ in Figure 2:

Platform 2 subscribers will switch to multihoming when $\mu \leq s - \Delta q$ and $m \leq q + | \Delta m ^ { 1 } | - s$ and to Platform 1 when $\mu > s - \Delta q$ and $m > q + | \Delta m ^ { 1 } | - s .$

If both $\mu > s - \Delta q$ and $m \leq q + | \Delta m ^ { 1 } | - s$ hold, then users will switch to the alternative that provides higher utility, choosing Platform 1 when $u _ { 1 } > u _ { 1 2 } \Leftrightarrow \mu > ( q - \Delta q + | \Delta m ^ { 1 } | ) - m$ and multihoming when $u _ { 1 } \leq u _ { 1 2 } \Leftrightarrow \mu \leq$ $( q - \Delta q + | \Delta m ^ { 1 } | ) - m$ . Therefore, $D L _ { 2 c }$ is given by $\mu = ( q - \Delta q + | \Delta m ^ { 1 } | ) - m$

Deriving Expansion Strategies:

For $\Delta m ^ { 1 } < 0$ (all parameter values), $\Delta b _ { 1 } \geq 0$ and $\Delta b _ { 2 } \leq 0$ (as in (a)), while both $\Delta b _ { 1 2 } \leq 0$ and $\Delta b _ { 1 2 } \geq 0$ are possible. If $\Delta b _ { 1 2 } \leq 0$ , then the analysis is the same as the case of $\Delta m ^ { 1 } > 0$ , and expansion is a dominant strategy for $c = 0 . { \mathrm { I f } }$ , on the other hand, $\Delta b _ { 1 2 } \geq 0$ , then all non-cost components in the LHS of the OER are positive, and the inequality trivially holds for $c = 0$ . Summarizing, $e _ { 1 } | _ { \bar { E } } \equiv E { \mathrm { ~ f o r ~ } } \Delta m ^ { 1 } > 0$ , when $c = 0$

As before, we find $c _ { L }$ and $c _ { H }$ to derive the impact of ?? on the optimal expansion strategy. For $c _ { L } ^ { \phantom { } } ,$ , we find the lowest $\pi _ { 1 } ^ { E \bar { E } }$ . Again, min $\pi _ { 1 } ^ { E \bar { E } }$ is obtained for $\Delta b _ { 1 } = \Delta b _ { 2 } = \Delta b _ { 1 2 } = 0$ (when only the ad-engagement effect drives expansion). The analysis is the same as for $\Delta m ^ { 1 } > 0$ and $c _ { L } | _ { \bar { E } , \Delta m ^ { 1 } < 0 } = c _ { L } | _ { \bar { E } , \Delta m ^ { 1 } > 0 }$ . Derivation of $c _ { H }$ is also the same as in $( a ) .$ , and $c _ { H } | _ { \bar { E } , \Delta m ^ { 1 } < 0 } = c _ { H } | _ { \bar { E } , \Delta m ^ { 1 } > 0 }$ and we denote these bounds as $c _ { L } | _ { \bar { E } } , c _ { H } | _ { \bar { E } } .$

## Expansion Strategy When Rival Expands, $e _ { i } | _ { E } .$

(a) Compatibility costs (weakly) increase, $\varDelta m ^ { 2 } \geq 0$

Deriving $D L _ { M H }$ in Figure 3:

$u _ { 1 } \geq u _ { 1 2 } \Leftrightarrow \ q + \Delta q + \mu - s > 2 q - ( m + \Delta m ^ { 2 } )$ . This implies $\mu > ( q - \Delta q + s - \Delta m ^ { 2 } ) - m$ . Therefore, $D L _ { M H }$ is given by $\mu = ( q - \Delta q + s - \Delta m ^ { 2 } ) - m .$

## Deriving Expansion Strategies:

For all parameter values, $\Delta b _ { 1 } = \Delta b _ { 2 } \geq 0$ and $\Delta b _ { 1 2 } = - 0 . 5 \Delta b _ { 1 } \leq 0$ . Substituting into the OER, $e _ { 1 } | _ { E } = E \iff$ $\rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E } + \rho ( 2 - \rho ) \Delta b _ { 1 } - 0 . 5 \rho ( 1 - \rho ) \Delta b _ { 1 } - c \geq 0$ . Simplifying, the inequality becomes $\rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E } +$ $\rho ( 1 . 5 - 0 . 5 \rho ) \Delta b _ { 1 } - c \geq 0 \quad$ , and always holds for $c = 0$

We proceed to derive $c _ { L }$ and $c _ { H } . \mathrm { A g a i n } , c _ { L }$ is obtained for the case of no switching $\Delta b _ { 1 } = \Delta b _ { 2 } = \Delta b _ { 1 2 } = 0$ , which implies $c _ { L } \big | _ { E , \Delta m ^ { 2 } > 0 } = \rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E }$ , where $b _ { 1 } ^ { \bar { E } E } \leq 0 . 5 ( 1 - q )$ (such that $ { c _ { L } } \big | _ { E , \Delta m ^ { 2 } > 0 }$ depends on the parameters $c , s , \rho , \Delta q , \Delta m ^ { 1 } , \bar { \mu }$ and $c _ { L } | _ { E , \Delta m ^ { 2 } > 0 } \leq c _ { L } | _ { \bar { E } }$

Similarly, $c _ { H }$ is obtained for maximal switching, i.e., the case when all multihomers switch, for $s < \Delta m ^ { 2 } - ( q - \Delta q )$ Note that this condition implies $s < \Delta q$ (since $\Delta m ^ { 2 } < q )$ and thus $b _ { 1 } ^ { \bar { E } E } = 0$ . Expansion is never optimal when $\pi _ { 1 } ^ { E E } <$ $\pi _ { 1 } ^ { \bar { E } E }$ , which implies $c _ { H } | _ { E , \Delta m ^ { 2 } > 0 } = 0 . 5 \rho ( 2 - \rho ) - \rho ( 1 - \rho ) b _ { 1 2 } ^ { \bar { E } E } \geq 0 . 5 \rho ( 2 - \rho ) . ^ { 4 0 }$

## (b) Compatibility costs decrease, $\varDelta m ^ { 2 } < 0$

Deriving $D L _ { M H }$ in Figure 4:

$u _ { 1 } \geq u _ { 1 2 } \Leftrightarrow q + \Delta q + \mu - s > 2 q - ( m + \Delta m ^ { 2 } )$ . This implies $\mu > ( q - \Delta q + | \Delta m ^ { 2 } | + s ) - m$ . Therefore, $D L _ { M H }$ is given by $\mu = ( q - \Delta q + | \Delta m ^ { 2 } | + s ) - m$

Deriving $D L _ { 1 , 2 }$ in Figure 4:

$u _ { 1 } \leq u _ { 1 2 } \Leftrightarrow q + \Delta q + \mu \leq 2 q - ( m + \Delta m ^ { 2 } ) - s$ . This implies $\mu \leq ( q - \Delta q + | \Delta m ^ { 2 } | - s ) - m$ . Therefore, $D L _ { 1 , 2 }$ is given by $\mu = ( q - \Delta q + | \Delta m ^ { 2 } | - s ) - m$

## Deriving Expansion Strategies:

Case (b1): When $| \Delta m ^ { 2 } | \leq \Delta q + 0 . 5 \bar { \mu } .$ , a larger mass of multihomers switch to the expanded platforms than vice versa. To see this, first note that $| \Delta m ^ { 2 } | \leq \Delta q + 0 . 5 \bar { \mu }$ ̅ implies $| \Delta m ^ { 2 } | - \Delta q < \bar { \mu } - ( | \Delta m ^ { 2 } | - \Delta q )$ . When $s > \bar { \mu } - ( | \Delta m ^ { 2 } | -$ $\Delta q )$ there is no switching, and when $s \in \big ( | \Delta m ^ { 2 } | - \Delta q < \bar { \mu } - ( | \Delta m ^ { 2 } | - \Delta q ) \big )$ only $D L _ { M H }$ is binding and $\Delta b _ { 1 } = \Delta b _ { 2 } >$ $0 , \Delta b _ { 1 2 } < 0$ . Finally, when $s < | \Delta m ^ { 2 } | - \Delta q$ , both decision lines are in effect, and $| \Delta m ^ { 2 } | \leq \Delta q + 0 . 5 \bar { \mu }$ ensures that $\Delta b _ { 1 } = \Delta b _ { 2 } > 0 , \Delta b _ { 1 2 } < 0$ continue to hold.<sup>41</sup> Overall, for $| \Delta m ^ { 2 } | \leq \Delta q + 0 . 5 \bar { \mu }$ , we have $\Delta b _ { 1 } = \Delta b _ { 2 } \geq 0 , \Delta b _ { 1 2 } \leq 0$ Deriving $c _ { L }$ and $c _ { H }$ for $| \Delta m ^ { 2 } | \leq \Delta q + 0 . 5 \bar { \mu } : c _ { L }$ is obtained, as before, for the case of no switching $\Delta b _ { 1 } = \Delta b _ { 2 } =$ $\Delta b _ { 1 2 } = 0$ which implies $c _ { L } | _ { E , \Delta m ^ { 2 } < 0 , ( b 1 ) } = \rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E }$ (recall that $b _ { 1 } ^ { \bar { E } E } \leq 0 . 5 ( 1 - q )$ and depends on $c , s , \rho , \Delta q , \Delta m ^ { 1 } , \bar { \mu } )$ . Since $c _ { L } | _ { E , \Delta m ^ { 2 } < 0 , ( b 1 ) } = c _ { L } | _ { E , \Delta m ^ { 2 } > 0 }$ denote both as $c _ { L } | _ { E }$

To find $c _ { H }$ we note that $\Delta b _ { 1 } = \Delta b _ { 2 } = - 0 . 5 \Delta b _ { 1 2 }$ are maximal when $s = 0$ , and $c _ { H }$ follows from the OER. Expansion is, therefore, a dominated strategy when $c > c _ { H } \vert _ { E , \Delta m ^ { 2 } < 0 , ( b 1 ) } = \rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E } + \rho ^ { 2 } \Delta b _ { 1 }$ , where $\Delta b _ { 1 } = 0 . 2 5 \bar { \mu } [ \bar { \mu } -$ $2 ( | \Delta m ^ { 2 } | - \Delta q ) ]$ ] and $b _ { 1 } ^ { \bar { E } E } \leq 0 . 5 ( 1 - q )$ (further depending on the parameters).

Case (b2): When $| \Delta m ^ { 2 } | > \Delta q + 0 . 5 \bar { \mu } ,$ , a larger mass of singlehomers switch to multihoming than vice versa. To see this, first note that $| \Delta m ^ { 2 } | > \Delta q + 0 . 5 \bar { \mu }$ implies $| \Delta m ^ { 2 } | - \Delta \bar { q } > \bar { \mu } - ( | \Delta m ^ { 2 } | - \Delta q )$ . When $s > | \Delta m ^ { 2 } | - \Delta q$ there is no switching, and when $s \in ( \bar { \mu } - ( | \Delta m ^ { 2 } | - \Delta q ) , | \Delta m ^ { 2 } | - \Delta q )$ only $D L _ { 1 , 2 }$ is in effect and $\Delta b _ { 1 } = \Delta b _ { 2 } < 0 , \Delta b _ { 1 2 } > 0$ Lastly, when $s < \bar { \mu } - ( | \Delta m ^ { 2 } | - \Delta q )$ , then both decision lines are in effect, and $| \Delta m ^ { 2 } | > \Delta q + 0 . 5 \bar { \mu }$ ensures that $\Delta b _ { 1 } = \Delta b _ { 2 } < 0 , \Delta b _ { 1 2 } > 0$ continue to hold. <sup>42</sup> Overall, for $| \Delta m ^ { 2 } | > \Delta q + 0 . 5 \bar { \mu }$ , we have $\Delta b _ { 1 } = \Delta b _ { 2 } \leq 0 , \Delta b _ { 1 2 } =$ $2 \Delta b _ { 1 } \geq 0$ . Now, expansion is no longer a dominant strategy, and no-expansion may be optimal even when expansion is costless. This follows from the OER, which becomes $e _ { 1 } | _ { E } = E ~ \Leftrightarrow ~ \rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E } + \rho ^ { 2 } \varDelta b _ { 1 } - c \geq 0$ . For $c = 0$ $e _ { 1 } | _ { E } = E$ when $\begin{array} { r } { | \varDelta b _ { 1 } | \leq \frac { 1 - \rho } { \rho } b _ { 1 } ^ { \bar { E } E } } \end{array}$ , and otherwise $e _ { 1 } | _ { E } = \bar { E }$ . Since expansion is no longer a dominant strategy for $c = 0$ there is no lower bound for the expansion cost. The expansion cost that will preclude expansion when switching to the expanded platform is maximal, $c _ { H } ,$ is derived from the OER with $\Delta b _ { 1 } = \Delta b _ { 2 } = \Delta b _ { 1 2 } = 0$ , and thus $c _ { H } | _ { E , \Delta m ^ { 2 } < 0 , ( b 2 ) } =$ $\rho ( 1 - \rho ) b _ { 1 } ^ { \bar { E } E }$

## Appendix C. Deriving Possible Domains for Decision Lines in Figures 1-4:

$D L _ { M H }$ is given by $\mu = ( q - \Delta q + s - \Delta m ^ { 1 } ) - m$ . No multihomers switch when $\mu ( m = q ) > \bar { \mu } \Leftrightarrow s > \bar { \mu } + \Delta q +$ $\Delta m ^ { 1 }$

$D L _ { 2 }$ is given by $\mu = s - \Delta q$ . No singlehomers switch when $s > \bar { \mu } + \Delta q$

Figure C1 summarizes the decision lines’ domains and the resulting changes in ?? in each domain.

![](/api/attachments/XGZCJEV7/fulltext/images/a9163fe8b670c48c4be515f483b6d8b0525a3d36cf35fd8cc108758ca027b527.jpg)  
Figure C1. Domains for $D L _ { M H } , D L _ { 2 }$ and the Resulting Changes in ?? in Each Domain

## Figure 2 Domains:

$D L _ { M H }$ is given by $\mu = ( q - \Delta q + s + | \Delta m ^ { 1 } | ) - m$ . No multihomers switch when $\mu ( m = q ) > \bar { \mu } \Leftrightarrow s > \bar { \mu } + \Delta q -$ |Δ??<sup>1</sup>|.

$D L _ { 2 a } , D L _ { 2 b }$ and $D L _ { 2 c }$ are given by $\mu = s - \Delta q , m = q + | \Delta m ^ { 1 } | - s$ and $\mu = ( q - \Delta q + | \Delta m ^ { 1 } | ) - m$ . There is no switching from $b _ { 2 }$ to $b _ { 1 }$ when $s > \bar { \mu } + \Delta q$ . There is no switching from $b _ { 2 }$ to $b _ { 1 2 }$ when $s > | \Delta m ^ { 1 } |$ . The third decision line $D L _ { 2 c }$ is in effect when $s \leq \operatorname* { m i n } \{ | \Delta m ^ { 1 } | , \bar { \mu } + \Delta q \}$ , and when this holds, users in $b _ { 2 }$ will switch to both $b _ { 1 }$ and $b _ { 1 2 }$ We consider the following three domains for $D L _ { M H } , D L _ { 2 a } , D L _ { 2 b } \colon ( \mathbf { A } ) | \Delta m ^ { 1 } | \leq \bar { \mu } + \Delta q - | \Delta m ^ { 1 } | ; \mathrm { ( B ) } | \Delta m ^ { 1 } | \in ( \bar { \mu } + \Delta m ^ { 1 } ) .$ $\Delta q - | \Delta m ^ { 1 } | , \bar { \mu } + \Delta q ) ; ( \mathbf { C } ) | \Delta m ^ { 1 } | > \bar { \mu } + \Delta q$ . Figure C2 summarizes the decision lines’ domains and the resulting changes in ?? in each domain

<table><tr><td rowspan="3">Direction of changes in B:</td><td>Δb1&gt;0</td><td>Δb1&gt;0</td><td>Δb1&gt;0</td><td>Δb1=0</td></tr><tr><td>Δb2&lt;0</td><td>Δb2&lt;0</td><td>Δb2&lt;0</td><td>Δb2=0</td></tr><tr><td>Δb12≤0</td><td>Δb12&lt;0</td><td>Δb12=0</td><td>Δb12=0</td></tr><tr><td rowspan="16">Domains for DLMH, DL2a, DL2b:</td><td rowspan="16" colspan="2">b2: don&#x27;t switch to b12</td><td rowspan="16">b12: none switch</td><td rowspan="16">b2: don&#x27;t switch to b1</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr></table>

(A)  
(C)

<table><tr><td>Direction of changes in B:</td><td> $\Delta b_{1} > 0$  $\Delta b_{2} < 0$  $\Delta b_{12} \leqslant 0$ </td><td> $\Delta b_{1} > 0$  $\Delta b_{2} < 0$  $\Delta b_{12} > 0$ </td><td> $\Delta b_{1} = 0$  $\Delta b_{2} < 0$  $\Delta b_{12} > 0$ </td><td> $\Delta b_{1} = 0$  $\Delta b_{2} = 0$  $\Delta b_{12} = 0$ </td></tr><tr><td rowspan="2">Domains for  $DL_{MH}$ ,  $DL_{2a}$ ,  $DL_{2b}$ :</td><td> $b_{12}$ : none switch</td><td> $b_{2}$ : don&#x27;t switch to  $b_{1}$ </td><td colspan="2"> $b_{2}$ : don&#x27;t switch to  $b_{12}$ </td></tr><tr><td> $\bar{\mu} + \Delta q - |\Delta m^{1}|$ </td><td> $\bar{\mu} + \Delta q$ </td><td> $|\Delta m^{1}|$ </td><td>s</td></tr></table>

Figure C2. Domains for $D L _ { M H } , D L _ { 2 a } , D L _ { 2 b }$ and the Resulting Changes in ?? in Each Domain: $\left( \mathbf { A } \right) \left| \Delta \pmb { m } ^ { 1 } \right| \leq$ $\overline { { \mu } } + \Delta q - | \Delta m ^ { 1 } | ; \mathrm { ( B ) } | \Delta m ^ { 1 } | \in ( \overline { { \mu } } + \Delta q - | \Delta m ^ { 1 } | , \overline { { \mu } } + \Delta q ) ; \mathrm { ( C ) } | \Delta m ^ { 1 } | > \overline { { \mu } } + \Delta q .$

## Figure 3 Domains:

$D L _ { M H }$ is given by $\mu = ( q - \Delta q + s - \Delta m ^ { 2 } ) - m$ . No multihomers switch when $\mu ( m = q ) > \bar { \mu } \Leftrightarrow s > \bar { \mu } + \Delta q +$ $\Delta m ^ { 2 }$

Figure C3 summarizes the decision line’s domains and the resulting changes in ?? in each domain.

<table><tr><td>Direction of changes in B:</td><td>Δb1&gt;0
Δb2&gt;0
Δb12&lt;0</td><td>Δb1=0
Δb2=0
Δb12=0</td></tr><tr><td rowspan="2">Domains for DLMH:</td><td>b12: all switch</td><td>b12: none switch</td></tr><tr><td>0 Δm2+Δq−q</td><td>μ̄+Δm2+Δq</td></tr></table>

Figure C3. Domains for $D L _ { M H }$ and the Resulting Changes in ?? in Each Domain.

## Figure 4 Domains:

$D L _ { M H }$ is given by $\mu = ( q - \Delta q + s + | \Delta m ^ { 2 } | ) - m$ . No multihomers switch when $\mu ( m = q ) > \bar { \mu } \Leftrightarrow s > \bar { \mu } -$ $( | \Delta m ^ { 2 } | - \Delta q )$ $D L _ { 1 , 2 }$ is given by $\mu = ( q - \Delta q - s + | \Delta m ^ { 2 } | ) - m$ . No singlehomers switch when $\mu ( m = q ) < 0 \Leftrightarrow s > ( | \Delta m ^ { 2 } | -$ $\Delta q )$ We thus consider the following two domains for $D L _ { M H } , D L _ { 1 , 2 } \colon ( \mathrm { A } ) \ ( | \Delta m ^ { 2 } | - \Delta q ) \leq 0 . 5 \bar { \mu } ; ( \mathrm { B } ) \ ( | \Delta m ^ { 2 } | - \Delta q ) > 0 . 5 \bar { \mu }$ Figure C4 summarizes the decision lines’ domains and the resulting changes in ?? in each domain.

<table><tr><td rowspan="3">Direction of changes in B:</td><td>Δb1&gt;0</td><td>Δb1&gt;0</td><td>Δb1=0</td></tr><tr><td>Δb2&gt;0</td><td>Δb2&gt;0</td><td>Δb2=0</td></tr><tr><td>Δb12&lt;0</td><td>Δb12&lt;0</td><td>Δb12=0</td></tr><tr><td rowspan="2">Domains for DLMH, DL1,2:</td><td></td><td>b1,b2:none switch</td><td>b12:none switch</td></tr><tr><td>0</td><td>|Δm2|-Δq</td><td>μ-(|Δm2|-Δq)</td></tr></table>

(B)

$$
\begin{array}{c c c c} \text {Direction of changes in B:} & \Delta b _ {1} <   0 & \Delta b _ {1} <   0 & \Delta b _ {1} = 0 \\ & \Delta b _ {2} <   0 & \Delta b _ {2} <   0 & \Delta b _ {2} = 0 \\ & \Delta b _ {1 2} > 0 & \Delta b _ {1 2} > 0 & \Delta b _ {1 2} = 0 \\ \hline \text {Domains for DL} _ {M H}, D L _ {1, 2}: & & \xrightarrow [ \text {switch} ]{b _ {1 2} : \text {none}} & \xrightarrow [ \text {switch} ]{b _ {1}, b _ {2} : \text {none}} \\ 0 & \bar {\mu} - (| \Delta m ^ {2} | - \Delta q) & | \Delta m ^ {2} | - \Delta q & s \end{array}
$$

Figure C4. Domains for $D L _ { M H } , D L _ { 1 , 2 }$ and the Resulting Changes in ?? in Each Domain: (A) $( | \Delta m ^ { 2 } | - \Delta q ) \leq 0 .$ . ????̅ ; (B) $( | \Delta m ^ { 2 } | - \Delta q ) > 0 . 5 \overline { { \mu } } .$

## About the Author

Sagit Bar-Gill. Sagit Bar-Gill is an assistant professor of technology management and information systems at Tel Aviv University. Prior to joining TAU, Sagit was a postdoctoral associate at MIT’s Sloan School of Management and the Initiative on the Digital Economy, where she remains a Digital Fellow. Sagit holds a PhD and MA in economics, and a BSc in mathematics from Tel Aviv University.

Copyright © 2019 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
