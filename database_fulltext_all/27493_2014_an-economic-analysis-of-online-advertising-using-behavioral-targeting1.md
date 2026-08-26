---
otero_id: 27493
otero_key: "3KZFDJGW"
title: "An Economic Analysis of Online Advertising Using Behavioral Targeting1"
authors: "Jianqing Chen; Jan Stallaert"
year: "2014"
journal: "MIS Quarterly"
doi: "10.25300/misq/2014/38.2.05"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# AN ECONOMIC ANALYSIS OF ONLINE ADVERTISING USING BEHAVIORAL TARGETING<sup>1</sup>

Jianqing Chen

Jindal School of Management, The University of Texas at Dallas, 800 West Campbell Road, Richardson, TX 75080 U.S.A. {chenjq@utdallas.edu}

Jan Stallaert

School of Business, University of Connecticut, 2100 Hillside Road, Storrs, CT 06269 U.S.A. {jan.stallaert@business.uconn.edu}

Online publishers and advertisers have recently shown increasing interest in using targeted advertising online. Such targeting allows them to present users with advertisements that are a better match, based on their past browsing and search behavior and other available information (e.g., hobbies registered on a web site). This technique, known as behavioral targeting, has been hailed as the new “Holy Grail” in online advertising because of its potential effectiveness. In this paper, we study the economic implications when an online publisher engages in behavioral targeting. The publisher auctions off an advertising slot and is paid on a cost-perclick basis. Using a horizontal differentiation model to capture the fit between a user and an advertisement being displayed, we identify the factors that affect the publisher’s revenue, the advertisers’ payoffs, and social welfare. We show that revenue for the online publisher in some circumstances can double when behavioral targeting is used. However, increased revenue for the publisher is not guaranteed: in some cases, the prices of advertising and hence the publisher’s revenue can be lower, depending on the degree of competition and the advertisers’ valuations. We identify two effects associated with behavioral targeting: a competitive effect and a propensity effect. The relative strength of the two effects determines whether the publisher’s revenue is positively or negatively affected. We also demonstrate that, although social welfare is increased and small advertisers are better off under behavioral targeting, the dominant advertiser might be worse off and reluctant to switch from traditional advertising.

Keywords: Behavioral targeting, targeted advertising, online advertising, pricing, competition, auctions, analytical modeling, economic modeling

## Introduction

Advances in information technology have radically changed online advertising, most notably in the ability to measure advertising outcomes and target advertisements. Information technology now can easily monitor clicks on a specific advertisement—which to some degree is regarded as the measure of effectiveness of advertising—and, as a result, using costper-click has become the new standard pricing practice for online advertising. Meanwhile, technology also enables the delivery of more targeted advertisements to consumers, for example, based on the keyword that a consumer enters in a search engine or the location of the consumer inferred from the computer’s IP address. One radical and recent innovation in targeted advertising is behavioral targeting—a technology aimed at increasing the effectiveness of advertising by online publishers. Behavioral targeting uses information collected from an individual’s web-browsing behavior (e.g., the pages that they have visited or the searches they have conducted) to select advertisements to display. This paper aims to analyze how behavioral targeting affects a publisher’s and advertisers’ payoffs, as well as social welfare.

“Cookies” (a small text file installed on a computer by web sites) have traditionally been used to track user behavior on the Web, such as a user’s web visiting history. Recent tracking technology is much more sophisticated and able to capture detailed data about a user’s actions and online behavior.<sup>2</sup> To illustrate, a recent study by The Wall Street Journal (Angwin 2010) found that the nation’s top 50 websites install, on average, 64 pieces of tracking technology, usually without any notification to users.

Behavioral targeting has been used for different advertising formats on the Internet. For example, any banner advertisement associated with a text web page (e.g., from Dictionary. com or MSN) can be chosen in a way to reflect a user’s interest. Similarly, the “pre-roll” (i.e., a video advertisement that appears before a requested video starts) or “overlay ad” (i.e., an advertisement that appears near the bottom of a video window) with online videos (e.g., from YouTube or ESPN3) can also be tailored based on a user’s interest. Therefore, under behavioral targeting, if a user is known to have recently visited a number of automotive shopping and comparison sites based on the data recorded by cookies stored on the user’s computer, the user can then be served automotiverelated advertisements when he visits Dictionary.com or YouTube, even if the word he searches on Dictionary.com or the video on YouTube he watches is not related to automobiles (Angwin 2010; Bazilian 2011). In June 2011, Google announced that it would allow “interest-based advertising” (Google’s term for behavioral targeting) for all advertisers on Google’s Display Network (Bazilian 2011). Interest-based advertisements are auctioned off on the basis of click-through rates, and user’s interests are derived from their online browsing behavior.

Advertising using behavioral targeting is becoming a sizable industry: eMarketer estimated that online advertisers spent more than \$1.3 billion in targeted advertising in 2011, and the figure is expected to rise to more than \$2.6 billion in 2014 (Hallerman 2010). Different studies also show the promise of behavioral targeting from different perspectives. Based on user survey responses from countries in the European Union (subject to the EU Privacy and Electronic Communications Directive, which prevents the collection and use of user data for behavioral targeting purposes) and non-EU countries, Goldfarb and Tucker (2011) find that, on average, users in EU countries were as much as 65 percent less likely to purchase a product advertised, compared to users in non-EU countries. In other words, users are much less likely to purchase after viewing advertisements that were not behaviorally targeted. When it comes to users’ intent to click on an advertisement, the results are even more staggering: experiments have shown that click-through rates can be increased by as much as 670 percent using behavioral targeting (Yan et al. 2009).

Despite such dramatic potential improvements for advertisers and online publishers, some users and user advocacy groups have expressed concerns over the privacy issues raised by behavioral targeting (Clifford 2009). To date, the Federal Trade Commission (FTC) has tried to let advertisers and publishers self-regulate: it has established a set of principles that Internet service providers (ISPs) and other collectors of user behavioral data should heed (FTC 2009). One such principle is that the data collector should receive “affirmative express consent [from the user] to the Use of Sensitive Data.” Some online publishers (e.g., Google) require the user to explicitly opt in before they collect any sensitive data, and they allow the user to select and specify what information can be gathered and what it can be used for. In this paper, we do not model the effects of behavioral targeting on the end-users. Rather, we are interested in finding out whether an online publisher and online advertisers would benefit from offering behaviorally targeted advertisements. If the answer is negative, user privacy concerns become irrelevant because the adoption of behavioral targeting would be unlikely. In general, this paper aims to understand how behavioral targeting affects publishers’ revenues (or the prices charged to the advertisers), advertisers’ payoffs, and social welfare.

In this paper, we consider a publisher who has one advertising slot for sale. This slot is used either for behavioral targeting, in which different advertisements are displayed for different users based on the fit between advertisements and users, or for traditional advertising, in which the same chosen advertisement is displayed for all users. Users (or potential customers) have different preferences for the advertisements, which translates into a different likelihood of clicking the advertisement. We assume that there is no universal ranking of the preferences over the user population, and user preferences are modeled to be horizontally differentiated. As in traditional horizontal differentiation models, the taste (or fit) of users is measured by their distance from the advertiser:

practical behavioral targeting algorithms (e.g., Liu and Lin 2007) compute this number as the fit between a user and an advertisement. The advertising slot is sold by weighted unitprice auctions, in which advertisers place cost-per-click bids and the winner is selected based on both the fit to a user and their cost-per-click bids. The winning advertiser pays according to the rule of second weighted unit price, which currently is the most commonly used payment scheme in online advertising auctions.

The main questions we try to answer are these: Do online publishers and advertisers benefit from behavioral targeting as compared to traditional advertising? How does behavioral targeting affect publishers’ and advertisers’ payoffs? Because of the increased effectiveness of behaviorally targeted advertisements, conventional wisdom would suggest that the answers to these questions are easily predicted, as summed up in an article in The Economist (2008) about behavioral targeting:

Advertisers will be prepared to pay more to place ads, since they are more likely to be clicked on. That in turn means that websites will be able to charge more for their advertising slots.

However, our research shows that this expected relationship between charges and clicks does not necessarily emerge when the advertising slot is auctioned off. Instead, using targeted advertisements turns out to have a similar effect as product differentiation: it causes relaxed competition among the advertisers, and hence it is possible that advertisers need not pay as much for the advertising slot as they do under traditional advertising. By focusing on a specific user segment, an advertiser’s advertisement may be selected with a relatively low price under behavioral targeting. That is, because fewer advertisers focus on a targeted user, it is more likely that the subset of advertisers focusing on the specific user have low value and/or low probabilities of click-through for this user, which enables the winning advertiser to pay less for the advertising slot. We call this phenomenon the competitive effect of behavioral targeting, and it can depress the online publisher’s income by lowering the revenue per click-through.

On the other hand, we find that the negative effect of relaxed competition for online publishers might be offset by a positive propensity effect under behavioral targeting: the increase in the probability of a click-through stemming from targeting advertisements. The propensity effect results in a higher expected volume of click-throughs, which positively contributes to the publisher’s revenue. Whether the publisher can benefit from behavioral targeting depends on the trade-off between the competitive effect and the propensity effect.

Behavioral targeting outperforms traditional advertising only if the competitive effect is dominated by the propensity effect. In particular, we show that when the advertisers competing for the advertising space are comparable and the number of advertisers is large, behavioral targeting generates more revenue for the publisher. This gain under behavioral targeting is increasing in user heterogeneity and the number of advertisers, and the expected revenue for the publisher can double compared to traditional advertising.

In addition, we find that the effect of behavioral targeting on different advertisers’ payoffs is asymmetric. While small advertisers are generally better off under behavioral targeting by winning their targeted users, the dominant advertiser may or may not be better off. The dominant advertiser is worse off under behavioral targeting when he has a significant competitive advantage over his competitors because, under traditional advertising, the advertiser would otherwise grab a larger group of users and still realize a decent payoff. The real benefit brought by the increased effectiveness of behavioral targeting is realized in the higher joint payoff of the publisher and the advertisers, as well as in social welfare under some assumptions about the users. We show that the joint payoff of the publisher and the advertisers is maximized under behavioral targeting. When users are given the choice to opt out of behavioral targeting and under some other mild assumptions, we can demonstrate that the social welfare for publishers, advertisers, and users is higher under behavioral targeting than under traditional advertising.

To the best of our knowledge, this study is one of the earliest theoretical studies on the effects of behavioral targeting. This work makes a substantive contribution to the understanding of the emerging behavioral targeting technology by providing a theoretical explanation of how behavioral targeting affects publishers, advertisers, and social welfare. This study also makes a theoretical contribution to the online advertising literature by developing an integrated three-layer framework (i.e., users, advertisers, and a publisher), in which a horizontal differentiation model is suggested as the means to measure the fit between users and advertisers, and on that basis advertisers compete for the advertising space provided by the publisher via auctions to display their advertisements to users.

The rest of the paper is organized as follows. In the next section, we discuss the related literature. We then set forth our model and provide an equilibrium analysis. We study the effect of behavioral targeting on the publisher, on the advertisers, and on the joint payoff of the publisher and the advertisers before discussing some extensions. Finally, we present our conclusions.

## Literature Review

Behavioral targeting of online advertisements is a relatively new phenomenon, and only limited studies have been devoted to this topic. Beales (2010) uses data collected from online advertising networks and finds that prices and conversion rates (i.e., the likelihood of a click eventually leading to a sale) for behaviorally targeted advertisements are more than twice as high as those for traditional advertising. We complement these empirical findings on the effect of targeting on the prices that advertisers pay by analytically studying the effect of behavioral targeting on advertisers’ payoffs, as well as on publishers’ revenues.

The studies on traditional targeted advertising can be traced back some decades, but the issues addressed are, although related, dissimilar to the ones that we discuss in this paper. We focus on prices of advertisements under behavioral targeting, while the traditional literature has mainly studied targeting either to price discriminate in the product market or to customize advertisements to different customer segments (Gal-Or et al. 2006; Ghose and Huang 2009).

Iyer et al. (2005) compare the strategies of targeted advertising and targeted pricing in a duopoly setting. They conclude that targeted advertising increases a firm’s profits, whereas targeted pricing might not. The optimal strategy for targeted advertising consists of advertising with probability 1 to loyal customers, and advertising less frequently to comparison shoppers. Gal-Or et al. (2006) study how an advertiser should allocate resources to increase the quality of the targeting. They measure the quality of targeting in two dimensions, accuracy and recognition, and consider a duopoly in which consumer tastes for the two products differ. Gal-Or et al. show that improving recognition in this case reduces profitability, and they derive the allocation of resources to achieve the optimal levels of accuracy and recognition. The model of Esteban and Hernandez (2007) is similar to that of Gal-Or et al., but assumes that the two firms sell vertically differentiated products. In such a model, Esteban and Hernandez show that the market may become permanently fragmented into local monopolies. This result contrasts with the earlier findings in the model of Iyer et al., who found that equilibrium pricing is only possible in mixed strategies, giving rise to markets that are fragmented from time to time, rather than being permanently fragmented.

Most of the papers in this rich body of literature concentrate on the effect of targeting on the profitability of the advertisers and do not address the effect of targeted advertising on the prices charged for the advertising itself. One exception is the paper by Gal-Or and Gal-Or (2005), in which two firms use a common media distributor as the channel for (targeted) advertising. Somewhat related to our model, in the horizontal differentiation model used by these authors, the probability that consumers become familiar with a brand is a linear decay function of their distance (taste) to the two brands. Conditions of optimality are derived for the distributor’s optimal payment schedule, but no explicit revenue comparisons are made between an environment with and without targeted advertising. In this paper, we also adopt a model of horizontal differentiation with a linear decay function but, for a general oligopoly. We compare behavioral targeting and traditional advertising in terms of various players’ payoffs, and reveal a competitive effect and a propensity effect associated with the difference in the two advertising technologies.

In our study, the publisher uses auctions to sell the advertising slot. The study of auctions in economics goes back many years. McAfee and McMillan (1987) and Klemperer (1999) provide comprehensive surveys of the large volume of early literature. Since online auctions gained popularity on the Internet, researchers in the information systems field have presented many interesting findings regarding the new features of this selling mechanism (e.g., Bapna et al. 2003; Bapna et al. 2004; Pinker et al. 2003). More recently, search engines have had great success in using auctions to sell their keyword-advertising/sponsored-search space, which has attracted significant attention from academia (e.g., Chen et al. 2009; Liu et al. 2010; Zhang and Feng 2011). Unlike most of the studies in this stream that focus on providing a better understanding or better design of auctions, in this paper we take the auction mechanism as given and focus on how the emergent behavioral targeting technology affects the players involved.

Our research is also loosely related to the literature on bundling (e.g., Geng et al. 2006; Ghosh et al. 2007; Palfrey 1983), if we view each user visit as an individual product sold by the publisher. Traditional advertising allocates all users to one winner and thus can be viewed as the publisher’s selling a bundled product. Behavioral targeting assesses each user and may allocate different users to different advertisers, which can be viewed as selling individual products. Geng et al. (2006) summarize a number of studies on using bundling for price discrimination or as a competition tool under a postedprice mechanism. Ghosh et al. (2007) consider the bundling strategy in auctioning different contexts for sponsored searches, and find cases in which it is better for online publishers to bundle in order to maximize their revenue. The comparison of traditional advertising and behavioral targeting discussed in this paper departs from the discussion of bundling or unbundling in that the pricing of advertising space under behavioral targeting differs from pricing of discrete goods under a traditional unbundled setting. In allocating traditional unbundled goods, the same bidder can propose different prices for different goods; in contrast, under behavioral targeting, each advertiser proposes one (unit) price for the advertising space, and the same price is used by the publisher in allocating different users. Our research also contributes to this stream of literature by integrating auctions within a horizontal differentiation model, which essentially introduces valuation dependence and continuous goods/users (in contrast to discrete goods as in Palfrey and Ghosh et al.).

## Baseline Model

We consider n advertisers competing for one advertising slot offered by a publisher in a specific context. A group of online users with a measure of one unit may view the advertising slot. The advertisers fit each user’s interest or need to different degrees, and the users have different preferences across the advertisers and different probabilities of clicking on their advertisements. In particular, we use a circular city model (Salop,1979) to represent users’ preferences or probabilities of clicking on advertisements from different advertisers.

We assume that the advertisers, indexed by $i = 1 , . . . , n ,$ are symmetrically distributed along a circle, clockwise in the order of $1 , 2 , . . . ,$ and n. The perimeter of the circle is 1, and thus the shortest distance between any two adjacent advertisers along the circle is 1/n. Unless otherwise indicated, we use the term distance to refer to the shortest distance along the circle. Each user is represented by a point on the circle, and users are uniformly distributed along the circle. The distance between a user and an advertiser reflects the degree of matching or misfit between the user and the advertiser: the longer the distance is, the lower the degree of the matching. Therefore, the most targeted user for an advertiser is the user that is located at the same spot as the advertiser. For advertiser $i ,$ we denote $p _ { i }$ as the probability that the most targeted user clicks on the advertisement when it is displayed. The probabilities attached to other users’ clicking on the advertisement decay to different degrees, depending on their distances from the advertiser. If the distance between advertiser i and user j is $x _ { i j } ,$ , we model the decay $q _ { i j } \operatorname { a s } q _ { i j } = 1 - \gamma x _ { i j }$ such that the probability that user j clicks on advertiser i is $p _ { i } q _ { i j } ,$ where $x _ { i j } \in [ 0 , 1 / 2 ]$ and γ is the decay factor $( 0 < \gamma \leq 2 )$ . The linear decay assumption simplifies the mathematical expressions and has been widely used in existing literature (e.g., in Gal-Or and Gal-Or (2005), discussing targeted advertising). The insights derived from our analysis stay the same when using other decreasing functions to model decay. Notice that γ also measures the heterogeneity of users’ preferences, and a high γ means that users have very different probabilities of clicking on an advertisement. We also call the probability $p _ { i } q _ { i j }$ user j’s expected click-through rate on advertiser i.

Figure 1 illustrates the basic elements of the model, with each small circle representing an advertiser (e.g., advertiser i) and any point on the big circle representing a user (e.g., user j).

The publisher knows the advertisers’ types, characterized by the locations on the circle. The publisher can learn a user’s preference (e.g., by monitoring her browsing history and the registered information) if the user opts in to the behavioral targeting; in this case, the publisher is able to determine the location of each user on the circle. In the baseline model, we assume that all users opt in. In reality, some users might be concerned about privacy and choose to opt out of behavioral targeting. In this case, the publisher does not know these users’ preferences. In the extension, we discuss this general case and show that the main results continue to hold. In addition, the publisher knows the probability that advertiser $i ^ { \circ } \mathrm { s }$ most targeted user clicks on his advertisement (p ) and the overall user heterogeneity with respect to the advertisements shown $( \gamma )$ . Different algorithms are available to obtain these parameters in practice, such as Liu and Lin (2007). All we assume about an advertiser is that he knows the value of a user’s clicking on his advertisement. Other information, such as the locations of other advertisers and their valuations for clicks, is irrelevant.

Following common practice in online advertising, we assume that the publisher uses second weighted unit-price auctions to sell the advertising slot. Advertisers bid on a per-click unit price, or cost-per-click, $b ,$ for the slot, and the winner is chosen based on the product of their cost-per-click bids and their expected click-through rates. Under behavioral targeting, for user j, the publisher knows her preference/expected click-through rates on different advertisers $p _ { i } q _ { i j } ,$ , and chooses the advertiser with the highest $b _ { i } \cdot p _ { i } q _ { i j }$ to be displayed to the user. Because the users differ in their preferences/expected click-through rates, different advertisements may be presented to different users. Under traditional advertising, the publisher does not learn or does not use users’ preference information, and one auction is used for the whole group of users. The winner is chosen based on his bid and the overall expected click-through rate across all users E $[ p _ { i } q _ { i j } ]$ . The advertiser with the highest $b _ { i } \cdot \mathrm { E } [ p _ { i } q _ { i j } ]$ wins the auction, and the same advertisement is displayed to all users. Notice that the cost-perclick bid times the expected click-through rate $( \mathrm { i . e . , } b _ { i } \cdot p _ { i } q _ { i j }$ under behavioral targeting or $b _ { i } \cdot \mathrm { E } [ p _ { i } q _ { i j } ]$ under traditional advertising) is the expected payment that an advertiser proposes. Therefore, the winner of an auction is essentially determined by advertisers’ expected payments for the user(s).

![](/api/attachments/3KZFDJGW/fulltext/images/c0d88d03e2059b294dc47d0006eceac3f371bdb033b717e009fd7fd09ed3cab1.jpg)  
Figure 1. Circular Model of Preferences

The advertiser with the highest proposed expected payment wins the auction and pays the unit price that makes his total payment (the unit price times his expected click-through rate) match the second highest proposed expected payment (i.e., second-score rule in Liu et al. (2010), similar to second-price auctions). Under this payment rule, the winner pays what is equivalent to the second highest proposed expected payment for the user(s).

We denote the unit value that advertiser i derives from each click by $\nu _ { i } ,$ and thus the expected value of user j to advertiser i is $\nu _ { i } p _ { i } q _ { i j } .$ We let $z _ { i } \equiv \nu _ { i } p _ { i }$ and call parameter $z _ { i }$ advertiser $i ^ { \circ } \mathrm { s }$ reference value, which is the expected value that advertiser i derives from his most targeted user. The value of user $\dot { \boldsymbol { \jmath } }$ to advertiser i can be viewed as advertiser i’s reference value $z _ { i }$ discounted by the decay ${ q _ { i j } } ^ { 3 }$ When ranking the $z _ { i }$ in nonincreasing order, we denote the $i ^ { \mathrm { { t h } } }$ highest value as $z _ { ( i ) } .$ We call the advertiser with the highest reference value $z _ { ( 1 ) }$ the dominant advertiser. For ease of exposition, we here make a comparable value assumption:

$$
z _ {(n)} > z _ {(1)} \left(1 - \frac {\gamma}{n}\right)\tag{1}
$$

That is, even if the advertiser with the lowest reference value happens to be adjacent to the dominant advertiser, the lowestvalue advertiser derives more value from his most targeted user than the dominant advertiser derives from the same user. In other words, the comparable value assumption ensures that, from an advertiser’s most targeted user, the advertiser derives higher value than other advertisers, which implies that no advertiser is dominated in terms of their valuation. We discuss the extension without the comparable value assumption in a later subsection.

## Equilibrium Analysis

In this section, we provide a general analysis of the equilibrium bidding outcome and the publisher’s and advertisers’ equilibrium payoffs under traditional advertising and behavioral targeting.

## Equilibrium Payoff under Traditional Advertising

Under traditional advertising, the publisher does not track users’ behavior and does not learn their preferences. The winner determination and payment are based on advertisers’ overall expected click-through rates. The expected decay across all users for any advertiser is

$$
\mathrm{E} [ q ] = 2 \int_ {0} ^ {1 / 2} (1 - \gamma x) d x = 1 - \frac {\gamma}{4}\tag{2}
$$

and hence the overall expected click-through rate for advertiser i is $p _ { i } ( 1 - \gamma / 4 )$ . Similar to the argument for the equilibrium bidding under standard second-price auctions (Klemperer 1999), we have the following lemma:

Lemma 1 Under traditional advertising, bidding the true per-click unit value is advertisers’ (weakly) dominant strategy when the advertising slot is auctioned off using the rule of second weighted unit price.

Proof. All proofs are in the appendix unless indicated otherwise.

The intuition behind this result is that if advertisers bid lower than their true unit value, they might lose some auctions that they could have won by bidding the true unit value. If advertisers bid higher than their true unit value, they risk earning negative payoffs by winning auctions that have a price higher than the true value to them. Therefore, bidding the true unit value is the best action and the equilibrium strategy for advertisers.

As a result, in equilibrium, the advertiser with the highest proposed expected payment who wins the advertising slot is the one with the highest expected value $( \nu _ { i } p _ { i } \mathrm { E } [ q ] )$ ). In other words, the advertiser with the highest reference value wins the advertising slot (by noting $z _ { i } = \nu _ { i } p _ { i } )$ . The winner’s payment, which is also the publisher’s revenue, is the second highest proposed expected payment in the auction and is thus the second highest expected value:

$$
\pi_ {T} = \left[ b _ {i} p _ {i} \left(1 - \frac {\gamma}{4}\right) \right] _ {(2)} = \left[ v _ {i} p _ {i} \left(1 - \frac {\gamma}{4}\right) \right] _ {(2)} = z _ {(2)} \left(1 - \frac {\gamma}{4}\right)\tag{3}
$$

where $[ \cdot ] _ { ( 2 ) }$ is the operator for the second highest value in the bracket among all $i ^ { \gamma } \mathsf { s } .$ . The winner’s payoff is thus

$$
\left(z _ {(1)} - z _ {(2)}\right) \left(1 - \frac {\gamma}{4}\right)\tag{4}
$$

## Equilibrium Payoff under Behavioral Targeting

Under behavioral targeting, we assume that the publisher has collected data about a user’s behavior and knows a user’s preference. The publisher allocates the advertising slot based on advertisers’ bids and how well an advertiser fits the user’s preference. Specifically, the advertiser with the highest expected payment for user $j ~ ( \mathrm { i . e . , }$ the highest $b _ { i } p _ { i } q _ { i j } )$ is presented in the advertising slot for the user. Different advertisers can win the advertising slot for different users because users generally differ in their preferences, represented by $q _ { i j }$ . We first derive which advertiser wins user j, which is commonly referred to as the winner determination problem. Then we determine the price being paid by the advertiser, which is known as the price determination problem. Based on the prices that advertisers pay for their users, we formulate the publisher’s revenue.

## Winner Determination

Following a similar argument as the one under traditional advertising, we can show that bidding the true per-click value is the equilibrium strategy for advertisers when the publisher charges according to the rule of second weighted unit price (see the proof of Lemma 1).

Provided that advertisers follow their dominant strategy and bid their true unit value $( b _ { i } = \nu _ { i } )$ in equilibrium, an advertiser’s proposed expected payment for a user is equal to his expected value when winning the user. In auctioning the advertising slot for user $j ,$ the publisher assigns the slot to the advertiser with the highest weighted unit price, which is the advertiser with the highest expected value $\nu _ { i } p _ { i } q _ { i j } ( = z _ { i } q _ { i j } )$ . We next show that all users are assigned to one of their two closest advertisers. To simplify the notation, we let $z _ { 0 } \equiv z _ { n }$ and $z _ { n + 1 } \equiv z _ { 1 }$

Lemma 2 Under the comparable value assumption, any user j located between advertisers i and i + 1 must be assigned to either advertiser i or advertiser i + 1 in equilibrium.

The intuition for this result is as follows. For any advertiser k different from advertisers i and $i + 1 .$ , we suppose the shortest path from user j to advertiser k passes advertiser i. If advertiser i has a higher reference value than advertiser k does (i.e., if $z _ { i } \geq z _ { k } )$ , advertiser i derives higher expected value from user j because user j has less decay for advertiser $i ( \mathrm { i . e . }$ $q _ { i j } > q _ { k j }$ because $x _ { i j } < x _ { k j } )$ . Otherwise $( \mathrm { i . e . , i f } z _ { i } < z _ { k } )$ , we notice that, according to the comparable value assumption, for advertiser $i ^ { \circ } \mathrm { s }$ most targeted user $j ^ { * }$ (with $x _ { i j ^ { * } } = 0 )$ , advertiser i derives a higher value than advertiser $k \ ( { \mathrm { i . e . , } } \ z _ { i } \ \geq \ z _ { k } q _ { k j ^ { * } } )$ Relative to user $j ^ { * } { } _ { ; }$ , user j has the same additional decay to both advertisers, but the decay has a greater negative effect on advertiser $k \mathrm { { s } }$ value because advertiser k has a higher reference value. Therefore, advertiser i derives a higher value from user j than advertiser k does. As a result, for any user j located between advertisers i and i + 1, either advertiser i or advertiser $i + 1$ derives the highest value, and thus the user must be assigned to one of them in equilibrium.

Next, we determine how many users are won by advertiser i. Within the user segment between advertisers i and $i + 1$ , or user segment $i \mid ( i + 1 )$ ), the users who have a strong preference for advertiser i are assigned to advertiser $i ,$ and the others are assigned to advertiser i + 1. A unique marginal user for allocation exists who has the same value to both advertisers; this marginal user is determined by

![](/api/attachments/3KZFDJGW/fulltext/images/4ecb544f49c41877d34fab11e96e142c3da4237f5c2250ebfb96d0819b865a59.jpg)  
(a) When $z _ { i - 1 } < z _ { i + 1 }$  
Figure 2. Marginal User Between Advertisers i and i + 1

$$
(1 - \gamma x _ {i}) z _ {i} = \left[ 1 - \gamma \left(\frac {1}{n} - x _ {i}\right) \right] z _ {i + 1}\tag{5}
$$

where $x _ { i }$ is the marginal user’s distance from advertiser i, as illustrated in Figure 2. Simply rearranging terms leads to

$$
x _ {i} = \frac {\left(z _ {i} - z _ {i + 1}\right) + \frac {1}{n} \gamma z _ {i + 1}}{\gamma \left(z _ {i} + z _ {i + 1}\right)}\tag{6}
$$

It is worth noting that the comparable value assumption ensures that $x _ { i } \in [ 0 , 1 / n )$ , such that each advertiser has some market coverage.

From Lemma 2 and Equation (6), we find that the users won by advertiser i in user segment $i \left| \left( i + 1 \right) \right.$ start with advertiser $i ^ { \circ } \mathrm { s }$ most targeted user, up to the user within distance $x _ { i \cdot }$ By the same argument, advertiser i also wins the users within distance $( 1 / n - x _ { i - 1 } )$ in user segment (i – 1) | i.

## Price Determination

Now we examine advertiser i’s payment for any user j within distance x in user segment $i \mid ( i + 1 )$ . Advertiser i pays the second highest proposed expected payment for user j, which is the highest value of user j to the remaining advertisers. The highest value to the remaining advertisers must be from either advertiser i + 1 or advertiser i – 1, by the same argument to that for Lemma 2. Determining which one among the remaining advertisers derives the highest value from user j is also equivalent to rerunning the auction with advertiser i removed, and in that case Lemma 2 establishes that user j can only be assigned either to advertiser $i - 1$ or to advertiser i + 1. So, either advertiser $( i - 1 ) ^ { \circ } \mathrm { s }$ or advertiser $( i + 1 ) \mathrm { { ^ { \circ } s } }$ value determines advertiser $i ^ { \circ } \mathrm { s }$ payment for use $: j .$ We next distinguish two cases, $z _ { i + 1 } \geq z _ { i - 1 }$ and $z _ { i + 1 } < z _ { i - 1 }$ , and examine the expected payment in each case.

![](/api/attachments/3KZFDJGW/fulltext/images/8a8d385cfd1cb92a93b885ddde25b4b21f6b1c14b0b6631c4ab73c4cda3582c0.jpg)  
(b) When $z _ { i - 1 } > z _ { i + 1 }$

When $z _ { i + 1 } \geq z _ { i - 1 }$ , advertiser (i + 1)’s valuation of any user that advertiser i wins in segment $i | ( i + 1 )$ is higher than advertiser $( i - 1 ) ^ { \circ } \mathrm { s }$ (see Figure 2a). Therefore, the expected payment from advertiser i for the users that the advertiser wins within this segment is

$$
z _ {i + 1} \int_ {0} ^ {x _ {i}} \left[ 1 - \gamma \left(\frac {1}{n} - x\right) \right] d x = z _ {i + 1} x _ {i} \left(1 - \frac {1}{n} \gamma + \frac {x _ {i}}{2} \gamma\right)\tag{7}
$$

which is the size of the light gray area in Figure 2a.

When $z _ { i + 1 } < z _ { i - 1 } ,$ for some users (close to advertiser i) within segment $i \mid ( i + 1 )$ , advertiser $( i - 1 ) \mathrm { { ' s } }$ value is higher than advertiser (i + 1)’s (see Figure 2b). In this case, the price for these users is determined by the value of advertiser i – 1 (which is the second highest value among all advertisers). For one user in segment i | (i + 1), located at distance y from advertiser i, advertisers i – 1 and i +1 derive the same value. We call this user the marginal user for payment, and the location of the marginal user for payment (i.e., the value of y ) is determined by the equality:

$$
\left[ 1 - \gamma \left(\frac {1}{n} + y _ {i}\right) \right] z _ {i - 1} = \left[ 1 - \gamma \left(\frac {1}{n} - y _ {i}\right) \right] z _ {i + 1}
$$

Hence, the distance from the marginal user for payment to advertiser i in this case is given by

$$
y _ {i} = \frac {\left(1 - \frac {\gamma}{n}\right) \left(z _ {i - 1} - z _ {i + 1}\right)}{\gamma \left(z _ {i - 1} + z _ {i + 1}\right)}\tag{8}
$$

The price that advertiser i pays for the users located within distance $y _ { i }$ is advertiser $( i - 1 ) \mathrm { { s } }$ valuation of these users, and the price that advertiser i pays for the rest of the users is advertiser $( i + 1 ) ^ { \dag }$ s valuation. Thus, when $z _ { i + 1 } < z _ { i - 1 }$ , the expected payment for all users in segment $i | ( i + 1 )$ allocated to advertiser i is

$$
\begin{array}{l} z _ {i - 1} \int_ {0} ^ {y _ {i}} \left[ 1 - \gamma \left(\frac {1}{n} + x\right) \right] d x + z _ {i + 1} \int_ {y _ {i}} ^ {x _ {i}} \left[ 1 - \gamma \left(\frac {1}{n} - x\right) \right] d x = \\ z _ {i + 1} x _ {i} \left(1 - \frac {1}{n} \gamma + \frac {x _ {i}}{2} \gamma\right) + \left(z _ {i - 1} - z _ {i + 1}\right) \left(1 - \frac {\gamma}{n}\right) \frac {y _ {i}}{2} \end{array}\tag{9}
$$

which is the size of the light gray and dark gray areas in Figure 2b.

The difference in the expected payments in (7) and (9) lies in that the latter has an extra term $\begin{array} { r l } { \big ( z _ { i - 1 } - z _ { i + 1 } \big ) \big ( 1 - \frac { \gamma } { n } \big ) \frac { y _ { i } } { 2 } } & { { } } \end{array}$ , which is the size of the dark gray area in Figure 2b. The extra term, which represents the additional expected payment/revenue to the publisher, arises because advertiser i’s payments in both segments are affected by his neighbor with the higher reference value: the neighbor with the higher reference value not only raises the payments for advertiser i in the segment between them (i.e., segment (i –1) | i in Figure 2b), but also raises the price for some users in the segment on the other side of advertiser i (i.e., the users within distance $y _ { i }$ to advertiser i in segment i | (i + 1) in Figure 2b). We call this extra term the cross-border effect. We call the term in (7), or the first term in (9), the base payment.

The expected payment from advertiser i for his users within user segment $( i - 1 ) \mid$ i can be derived similarly. Depending on the relative competitiveness betweem advertisers i – 1 and i + 1, advertiser i pays the cross-border effect either in one segment or in the other. Only in the special case where both neighbors’ reference values are identical does the crossborder effect vanish. Either way, the cross-border effect, denoted as $\Delta _ { i } ,$ takes the same form (by substituting (8) into the second term of (9)):

$$
\Delta_ {i} = \frac {\left(1 - \frac {\gamma}{n}\right) ^ {2} \left(z _ {i - 1} - z _ {i + 1}\right) ^ {2}}{2 \gamma \left(z _ {i - 1} + z _ {i + 1}\right)}\tag{10}
$$

Therefore, advertiser i’s expected payment $H _ { i }$ for the users that he wins (i.e., the users within distance $x _ { i }$ in segment i | (i + 1) and the users within distance $\begin{array} { r } { \left( \frac { 1 } { n } - x _ { i - 1 } \right) } \end{array}$ in segment (i – 1) | i) can be formulated as

$$
\begin{array}{r l} H _ {i} & = z _ {i + 1} x _ {i} \left(1 - \frac {1}{n} \gamma + \frac {\gamma x _ {i}}{2}\right) + \\ & \quad z _ {i - 1} \left(\frac {1}{n} - x _ {i - 1}\right) \left[ 1 - \frac {1}{n} \gamma + \frac {\gamma}{2} \left(\frac {1}{n} - x _ {i - 1}\right) \right] + \Delta_ {i} \end{array}\tag{11}
$$

The advertiser’s payoff $A _ { i }$ is the expected value of the users that he wins net the expected payment. The payoff from segment i | (i + 1) is illustrated by the dotted area of each subfigure in Figure 2. The advertiser’s payoff comes from both segments (i – 1) | i and $i \mid ( i + 1 )$ and can be formulated as

$$
\begin{array}{r l} A _ {i} & = \frac {1}{2} x _ {i} \left[ z _ {i} - z _ {i + 1} \left(1 - \frac {\gamma}{n}\right) \right] + \\ & \quad \frac {1}{2} \left(\frac {1}{n} - x _ {i - 1}\right) \left[ z _ {i} - z _ {i - 1} \left(1 - \frac {\gamma}{n}\right) \right] - \Delta_ {i} \end{array}\tag{12}
$$

where the first term is the size of the dotted triangle in Figure 2a, and the second has a similar interpretation. (The rigorous derivation of the payoff function can be found in the proof of Proposition 4.)

The publisher’s revenue consists of the expected payment from all n advertisers:

$$
\pi_ {B} = \sum_ {i = 1} ^ {n} H _ {i}\tag{13}
$$

where $H _ { i }$ is defined as in Equation (11).

## Comparison of Advertising Technologies

In this section, we study the conditions under which the publisher prefers behavioral targeting over traditional advertising and the conditions under which some advertisers are better off under behavioral targeting. We also examine the joint payoff of the publisher and the advertisers under the two advertising technologies.

## Publisher’s Revenue

Facing the decision between two advertising technologies, the publisher will choose the one that generates higher revenue by comparing $\pi _ { T }$ and $\pi _ { B } .$ . We notice that, given user preference heterogeneity (γ), the publisher’s revenue under traditional advertising $( \pi _ { T }$ in Equation (3)) is solely determined by the second-highest reference value $( z _ { ( 2 ) } )$ , whereas the revenue under behavioral targeting $( \pi _ { B }$ in Equation (13)) depends on many other factors as well, such as the number of advertisers (n), as well as the advertisers’ reference values (z ) and their relative location. In general, either technology can lead to a higher revenue than the other, depending on these factors. In order to establish a baseline for comparison, we first fix $z _ { ( 2 ) }$ (such that $\pi _ { T }$ is fixed) and examine the publisher’s maximum and minimum possible revenues when the other reference values and their locations, henceforth called the value structure, are varied under behavioral targeting.

## Maximum and Minimum Revenue under Behavioral Targeting

We first examine how the revenue under behavioral targeting changes with each advertiser’s reference value. According to the auction rule, the expected revenue generated from each user is the second highest proposed expected payment for the user, or the second highest value of the user to the advertisers. When an advertiser’s reference value is increased, the value derived from the user is also increased, and the second highest value of the user to the advertisers is (weakly) increased. In addition, under the comparable value assumption, the advertiser has some market coverage under his original reference value and captures some additional users from his neighbor when increasing his reference value. For these additional users, the second highest value of each user after the increase is the highest value of each user before the increase. Therefore, the expected revenue from these users is strictly increasing, as is the total expected revenue.

Lemma 3 The revenue under behavioral targeting is increasing in $z _ { i } , i = 1 , 2 , . . . , n .$

The revenue under behavioral targeting not only depends on the values of the advertisers but also might depend on how those values are located along the circle (e.g., whether the dominant advertiser is adjacent to the one with the second highest reference value). The following proposition concludes the maximum and minimum revenues among all value structures under behavioral targeting, $\mathrm { g i v e n } z _ { ( 2 ) }$

Proposition 1 Under behavioral advertising, for a fixed value $o f z _ { ( 2 ) } .$

(a) the value structure with $z _ { ( 1 ) } = z _ { ( 2 ) } / ( 1 - { \scriptstyle \frac { \gamma } { n } } ) a n d z _ { ( 3 ) } = z _ { ( 4 ) } = \dots$ $= z _ { ( n ) } = z _ { ( 2 ) }$ generates the highest revenue for the publisher among all possible value structures;

(b) the value structure with $z _ { ( 1 ) } = z _ { ( 2 ) } , z _ { ( 3 ) } = z _ { ( 4 ) } = \ldots = z _ { ( n ) } =$ $\begin{array} { r l } { ( 1 - \frac { \gamma } { n } ) z _ { ( 2 ) } , } \end{array}$ and the two highest-value advertisers being $\textstyle { \frac { 2 } { n } }$ distant from each other (if possible) generates the lowest revenue for the publisher among all possible value structures.

Based on the monotonicity between the revenue and the advertisers’ reference value in Lemma 3, part (a) is intuitive. Given the second highest reference value, the revenue is increasing in these lower reference values. The maximum can be reached only if these lower values reach as high as the second highest value (within the order constraint). The revenue is also increasing in the highest reference value, which is constrained at the value specified in the proposition because of the comparable value assumption.

The argument for part (b) is in the same spirit as the argument for part (a). Given the second highest value, all the other values should be as low as possible, and thus, for instance, the highest value is equal to the second highest. One additional issue beyond part (a) is the relative position of the two advertisers with the highest reference value. The intuition for the result regarding the relative position is as follows.

First, the revenue from the base payment is lower when the two highest-value advertisers are not adjacent than when they are. The reason is that, when the two highest-value advertisers are adjacent to each other, each of them faces a competitor who is very similar to himself, and the resulting faceto-face competition between them significantly raises the prices for the users for whom they compete. In contrast, when the two highest-value advertisers are not adjacent, each of them directly competes with a low-value advertiser and pays a low price for the users he wins.

Second, the number of cross-border effects is at a minimum when the two highest-value advertisers ar $; { \frac { 2 } { n } }$ distant from each other. The cross-border effect arises in an advertiser’s payment when the advertiser’s two neighbors have different reference values. When there are four advertisers and the two highest-value advertisers are $\textstyle { \frac { 2 } { n } }$ distant away, no cross-border effect occurs because each advertiser’s two neighbors have the same value. When there are more than four advertisers and the two highest-value advertisers are $\textstyle { \frac { 2 } { n } }$ distant away, the cross-border effect occurs in the payments of the two lowvalue advertisers who have one low-value neighbor and one highest-value neighbor, and thus the number of cross-border effects is two. Meanwhile, under any value structure, at least two advertisers have as neighbors one highest-value advertiser and one low-value advertiser, and thus the number of cross-border effects is at least two. Therefore, the number of cross-border effects is at the minimum when the two highestvalue advertisers are $\textstyle { \frac { 2 } { n } }$ distant from each other. Because the total revenue is composed of the base payments and the crossborder effects, we conclude that the revenue is the lowest when the two highest-value advertisers are $; { \frac { 2 } { n } }$ distant from each other.

## Publisher’s Revenue Comparison

In Proposition 1, given the number of advertisers under behavioral targeting, we have identified the upper bound and the lower bound of the publisher’s revenue among all possible value structures—that is, the ones that yield the highest revenue or lowest revenue for the publisher. Then, if the lowest revenue under behavioral targeting is higher than the revenue under traditional advertising, we can conclude that the revenue under behavioral targeting is higher than that under traditional advertising. Similarly, if the highest revenue under behavioral targeting is lower than the revenue under traditional advertising, the revenue under behavioral targeting is lower than that under traditional advertising. Using such reasoning based on the upper and lower bounds of the publisher’s revenue, in the following proposition we derive how the number of advertisers affects the comparison between advertising technologies, independent of valuation structure.

## Proposition 2

(a) If and only if the number of advertisers is small $( n = 2 )$ , the publisher is (weakly) better off by using traditional advertising, regardless of the advertisers’ value structure or the heterogeneity of users’ preference;

(b) When the number of advertisers is intermediate $( 2 < n <$ 6), which advertising technology yields the higher revenue depends on the value structure and the heterogeneity of users’ preference;

(c) If and only if the number of advertisers is large enough $( n \geq 6 ) _ { : }$ , the publisher is better off by using behavioral targeting, regardless of the advertisers’ value structure or the heterogeneity of users’ preference.

The intuition for part (a) is as follows: When only two advertisers compete for the advertising slot, we assume that advertiser 1 has a higher reference value than advertiser 2 without loss of generality. Under traditional advertising, advertiser 1 wins the auction and pays advertiser 2’s expected value of the users. The gray area in Figure 3a illustrates the expected payment for one user segment. The other user segment is symmetric. Under behavioral targeting, advertiser 1 wins users within distance $x _ { 1 }$ and pays advertiser 2’s expected value of that user group, and advertiser 2 wins the rest and pays advertiser 1’s expected value of those users. The gray area in Figure 3b illustrates the expected payment. The main difference in the expected payments under the two advertising technologies lies in the expected payment for the users located at $[ x _ { 1 } ,$ 1/2] from advertiser 1. We can see that the expected payment for those users under traditional advertising is greater than that under behavioral targeting. Therefore, the revenue under traditional advertising is higher than that under behavioral targeting if both advertisers have some positive market share. When one advertiser 1 has no market share $( \mathrm { i } . \mathsf { e } . , x _ { 1 } = 1 / 2 )$ , the revenue under the two advertising strategies is the same. Notice that under traditional advertising, all users are auctioned off together as one package or bundle. “Bundling” users together can reduce the advertisers’ valuation heterogeneity and increase the competition, which, consistent with the bundling literature (Geng et al. 2006), is the reason that traditional advertising may generate more revenue for the publisher.

When the number of advertisers is greater than 2, the dominant advertiser continues to win the auction under traditional advertising and pays their expected value of the advertiser with the second highest reference value for all users. For the users who are far from the second-highest-value advertiser, their expected value to the second-highest advertiser can be significantly lower than their expected value to multiple other advertisers who fit these users better (i.e., who are closer to such users on the circle) because of the decay. Under traditional advertising, the expected payment is the expected value of these users to the second-highest advertiser. Under behavioral targeting, the expected payment is the second highest expected value of these users to all of the advertisers, and the expected payment for these users under behavioral targeting therefore could be higher. As a result, we cannot extend the argument for the case with two advertisers to the case with more advertisers. At the same time, we can easily find cases in which the revenue under behavioral targeting is greater than that under traditional advertising when more than two advertisers are involved (e.g., the special case discussed in Corollary 2).

Under behavioral targeting, each advertiser has his own targeted user, and thus, compared to traditional advertising, the competition among advertisers is less fierce (in a sense similar to relaxed competition in the product differentiation setting). This competitive effect has a negative effect on the publisher’s revenue. On the other hand, each individual user is checked case by case and assigned to an advertiser with the highest proposed payment for the user, which improves the advertising resource allocation. In contrast, misallocation is inherent in the allocation under traditional advertising. When the advertiser with the highest reference value wins the auction under traditional advertising, he wins all the users and pays the second-highest advertiser’s expected value of the users. However, when there are multiple advertisers, assigning these users who are distant from the winner or who have a low probability of clicking on the winner’s advertisement might not be desirable because other advertisers might value those users more and be willing to pay more. We call this the propensity effect, and it positively affects the publisher’s revenue under behavioral targeting. Under the comparable value assumption, when the number of advertisers becomes considerably large, the propensity effect becomes intense because a large number of advertisers have a much better fit for some users and propose higher expected payments than the winner under traditional advertising does. As a result, the propensity effect dominates the competitive effect, and the publisher is better off using behavioral targeting.

![](/api/attachments/3KZFDJGW/fulltext/images/4f9f626ebd2d9b1f15c82b4c8f9719dcb392211bb7c99d78eda1c4716dc1bc2a.jpg)  
(a) Under Traditional Advertising  
Figure 3. Revenue Comparison When n = 2

The implication of Proposition 2 is both easy to understand and actionable. In general, big publishers with considerable demand for their advertising resources can improve revenue by switching from traditional advertising to behavioral targeting. Small publishers with low demand might be better off staying with traditional advertising. In addition, the advertising resources from the same publisher might generate different levels of demand. For example, different YouTube video clips have different contexts and attract different numbers of advertisers. So publishers might even choose to tailor their selling policies across their advertising resources, using behavioral targeting for selling popular advertising resources and using traditional advertising for selling resources that have less mass appeal.

It is worth pointing out that the strong results depending only on the number of advertisers in Proposition 2 can only be obtained under the assumptions of the comparable value relationship and the symmetric location of the advertisers along the circle. With these assumptions, the number of advertisers is a good measure of competition and thus is reflected in the results; otherwise, the condition on the number of advertisers should be replaced by a more general condition. The later subsection regarding the case without comparable value relaxes these assumptions and depicts the general condition, by which we show that the intuition revealed in the baseline model remains the same: when enough “comparable” advertisers compete for each user under behavioral targeting, behavioral targeting generates higher revenue than traditional advertising, and when little competition exists among advertisers, traditional advertising is better for the online publisher.

![](/api/attachments/3KZFDJGW/fulltext/images/0d14749a1260b930ddeb735a2ce1917af1bcbe688ff80025c3d4688373005c1e.jpg)  
(b) Under Behavioral Targeting

Part (b) of Proposition 2 identifies an area where the number of advertisers alone is not sufficient to demonstrate superiority of one advertising technology over the other. When the number of advertisers is intermediate, either advertising technology could generate higher revenue than the other, depending on the advertiser’s value structure and the heterogeneity of users’ preference. If we have additional information about the value structure, we can compare the revenues in this area. Next, we consider two special cases:

1. The symmetric case in which all advertisers have the same reference value. Without loss of generality, we assume $z _ { i } = 1$

2. The all-but-one symmetric case in which one advertiser (the dominant advertiser) has a value advantage over the others while the others have the same reference value. In particular, we let $z _ { 1 } > z _ { 2 } = z _ { 3 } = . . . = z _ { n } = 1$

Corollary 1 In the symmetric case (in which $z _ { 1 } = z _ { 1 } = \dots =$ $z _ { n } ) ,$ when there are three advertisers, the publisher is indifferent between traditional advertising and behavioral targeting. When the number of advertisers is greater than three, the publisher is better off using behavioral targeting.

In this situation, under behavioral targeting, for a user located between advertisers i and i + 1, advertiser i wins the advertising slot for the user if the user is more likely to click on the advertisement from advertiser i than on the advertisement from advertiser i + 1. When advertiser i wins these users, the expected price that the advertiser pays for each user (i.e., the average of the highest price and the lowest price that the advertiser pays) is

$$
\frac {1}{2} \left[ \left(1 - \frac {1}{2 n} \gamma\right) + \left(1 - \frac {1}{n} \gamma\right) \right] = 1 - \frac {3}{4 n} \gamma
$$

Because the expected price for each user is the same across advertisers, this expression is also the total revenue for the publisher. The expected revenue under traditional advertising is $\pi _ { T } = ( 1 - \frac { \chi } { 4 } )$ by Equation (3), and the result in Corollary 1 follows.

The intuition is again the balance between the competitive effect and the propensity effect. When the number of advertisers is low, the auction under traditional advertising can leverage the competitive effect (by letting the advertisers compete for one single bundled user group), but it does so at the cost of efficiency because of the lower propensity of users to click on the advertisement.

In the all-but-one symmetric case, the revenue under traditional advertising is the same as in the case with symmetric advertisers because both cases have the same second highest reference value. When there are more than two advertisers, the revenue under behavioral targeting $\pi _ { B }$ can be formulated as

$$
\begin{array}{l} \pi_ {B} = 2 x _ {1} \left(1 - \frac {1}{n} \gamma + \frac {x _ {1}}{2} \gamma\right) + 2 z _ {1} \left(\frac {1}{n} - x _ {1}\right) \left[ 1 - \frac {1}{n} \gamma + \frac {1}{2} \left(\frac {1}{n} - x _ {1}\right) \gamma \right] \\ + \frac {n - 2}{n} \left(1 - \frac {3}{4 n} \gamma\right) + \frac {\left(1 - \frac {\gamma}{n}\right) ^ {2} \left(z _ {1} - 1\right) ^ {2}}{\gamma \left(z _ {1} + 1\right) ^ {2}} \end{array} \tag {1}\tag{14}
$$

where the first two terms are the payment from the two segments containing the dominant advertiser, the third term is the base payment from (n – 2) segments between the advertisers with the low reference value, and the fourth term is from the cross-border effects. The marginal type $x _ { 1 }$ is defined by Equation (6); that is,

$$
x _ {1} = \frac {\left(z _ {1} - 1\right) + \frac {1}{n} \gamma}{\gamma \left(z _ {1} + 1\right)}
$$

According to Lemma 3, the above revenue under behavioral advertising in this special case is greater than in the symmetric case (because advertiser 1’s reference value is higher in the former than in the latter, while the other reference values are the same). Therefore, based on Corollary 1, we can conclude that the comparison of revenue is as follows:

Corollary 2 In the all-but-one symmetric case (in which $z _ { 1 } >$ $z _ { 2 } = z _ { 3 } = \ldots = z _ { n } ) ,$ , when the number of advertisers is greater than 2, the publisher is better off using behavioral targeting.

Notice that this class of all-but-one symmetric case contains the value structure that results in the highest revenue for the publisher under behavioral targeting, as discussed in Proposition 1. Next, we derive how much the online publisher can benefit from using behavioral targeting. We use $( \pi _ { B } - \pi _ { T } ) / \pi _ { T }$ as the measure of the gain from behavioral targeting, and explore the maximum gain that the publisher can obtain by switching from traditional advertising to behavioral targeting. Notice that if all $z _ { i } ^ { \mathrm { ~ \tiny ~ s ~ } }$ are scaled to the same degree (e.g., to $\tau { z _ { i } } ^ { \mathrm { ~ \tiny ~ s ~ } }$ where τ is a constant), the gain is not affected. Therefore, as in the discussion for Proposition 1, we can let $z _ { ( 2 ) }$ be fixed without loss of generality, and the maximum gain can be obtained by solving the following optimization problem:

$$
\max _ {z _ {(1)}, z _ {(3)}, \dots , z _ {(n)}} \frac {\pi_ {B} - \pi_ {T}}{\pi_ {T}}
$$

which is equivalent to maximizing $\pi _ { B }$ because $\pi _ { T }$ is solely determined by $z _ { ( 2 ) } .$ . From Proposition 1, we showed that for the value structure generating the highest revenue under behavioral targeting, we must have $z _ { ( 2 ) } = z _ { ( 3 ) } = \ l _ { \cdot \cdot } = z _ { ( n ) }$ and $z _ { ( 1 ) }$ must be as big as possible.

## Proposition 3

(a) When the number of bidders is two, the publisher’s maximum gain from behavioral targeting is zero. When the number of bidders is greater than two, the maximum gain under the comparable value assumption is

$$
\frac {\gamma}{4 - \gamma} \left[ \frac {(n - 2) (n - 1)}{n ^ {2}} + \left(\frac {2 (n - \gamma)}{n (2 n - \gamma)}\right) ^ {2} \right]
$$

(b) The publisher’s maximum gain from behavioral targeting is increasing in the number of advertisers n and user heterogeneity γ.

It is worth pointing out that the gain from behavioral targeting can be very significant. For example, if the degree of heterogeneity among user preferences is high $( \mathrm { i } . \mathrm { e } . , \gamma  2 )$ , then the gain can be 100 percent when the number of advertisers becomes large $( { \mathrm { i . e . , ~ } } \frac { ( n - 2 ) ( n - 1 ) } { { n } ^ { 2 } } {  } 1 \mathrm { a n d ~ } \frac { 2 ( n - \gamma ) } { { n } ( 2 n - \gamma ) } {  } 0$ when $n  \infty )$ . In other words, the publisher’s revenue can be doubled by switching to behavioral targeting.

## Advertisers’ Payoffs

Next, we examine advertisers’ payoffs under different advertising technologies. Under traditional advertising, all advertisers except the dominant advertiser (i.e., the one with the highest reference value) earn zero payoff because they have zero market share. Under behavioral targeting, in contrast, all advertisers might have positive payoffs, unless an advertiser is totally dominated by his competitors such that the advertiser has negligible market share. Therefore, all advertisers except the dominant advertiser are always (weakly) better off under behavioral advertising.

For the dominant advertiser, the payoff under traditional advertising is $( z _ { ( 1 ) } - z _ { ( 2 ) } ) ( 1 - \gamma / 4 )$ by Equation (4). Under behavioral targeting, each advertiser’s payoff has been derived in Equation (12), and the payoff of the dominant advertiser can be formulated accordingly. In general, whether the dominant advertiser can be better off depends on the parameters, such as the values of his neighbors and the number of advertisers. We start by giving a general result, independent of the specific value structure of the advertisers. Without loss of generality, we assume that the dominant advertiser is advertiser 1.

## Proposition 4

(a) All advertisers other than the dominant advertiser are always (weakly) better off under behavioral targeting.

(b) The dominant advertiser (advertiser 1) could be better off or worse off, depending on the competitive situation $( e . g .$ the second highest reference value, direct neighbors’ reference values, the number of advertisers, and γ). Specifically, (b.1) the dominant advertiser is (weakly) better off under behavioral advertising when there are only two advertisers, regardless of his per-click value or γ; (b.2) when $n > 2 .$ , the dominant advertiser is better off only if

$$
\begin{array}{r l} (z _ {1} - z _ {(2)}) \left(1 - \frac {\gamma}{4}\right) & <   \frac {1}{2} \left[ z _ {1} - z _ {2} \left(1 - \frac {\gamma}{n}\right) \right] x _ {1} + \\ & \frac {1}{2} \left[ z _ {1} - z _ {n} \left(1 - \frac {\gamma}{n}\right) \right] \left(\frac {1}{n} - x _ {n}\right) - \Delta_ {1} \end{array}
$$

where $x _ { 1 }$ and $x _ { n }$ are defined as in Equation (6) and $\Delta _ { 1 }$ is defined as in Equation (10).

The result in the case with two advertisers can be seen in Figure 3. The payoff under traditional advertising is the size of A minus the size of B in Figure 3a, whereas the payoff under behavioral targeting is the size of A in Figure 3b. So the dominant advertiser is better off under behavioral targeting as long as the other advertiser has some market share. When the other advertiser has no market share under behavioral targeting, the dominant advertiser’s payoff is the same under both advertising technologies.

When there are more than two advertisers, for the symmetric case, because the competition is intensely fierce under traditional advertising, the winner barely earns a profit; that is, the winner under traditional advertising earns zero payoff because $z _ { ( 1 ) } = z _ { ( 2 ) } .$ . In contrast, under behavioral advertising, advertisers are differentiated from each other because of users’ heterogeneous preferences, and all of them earn some positive payoff.

Corollary 3 In the symmetric case (in which $z _ { 1 } = z _ { 2 } = \dots =$ $z _ { n } ) ,$ , all advertisers are better off under behavioral advertising.

In general, whether the dominant advertiser is better off under behavioral targeting involves many factors and is complicated to derive. For example, the dominant advertiser’s neighbors directly affect the competition the advertiser faces under behavioral targeting and thus affect the advertiser’s payoff. The higher the neighbors’ values are, the less payoff the highest-value advertiser can obtain under behavioral targeting (which is reflected in Figure 2, as the dotted areas shrink when the lines ending at $z _ { i + 1 }$ move upward). Therefore, when neither neighbor is the one with the second highest value (so the payoff under traditional advertising remains the same), the dominant advertiser is more likely to be better off under traditional advertising. When one neighbor is the advertiser with the second highest value, the neighbor’s value also affects the dominant advertiser’s payoff under traditional advertising, and the effect is two-edged.

Next, we consider a case in which the dominant advertiser’s two neighbors have the same reference value, and this value is the second highest. Without loss of generality, we assume that advertiser 1 is the dominant advertiser and his neighbors reference values are 1 $( \mathrm { i } . { \bf e } . , \ z _ { 1 } = z _ { ( 1 ) }$ and $z _ { 2 } = z _ { n } = z _ { ( 2 ) } = 1 )$ Notice that the all-but-one symmetric case is a special instance of this case. We next use this case to demonstrate how the number of advertisers and the relative competitiveness of the dominant advertiser to the second-highest-value advertiser affects the dominant advertiser’s payoff. From Equation (12), the dominant advertiser’s payoff under behavioral targeting is

$$
\left[ z _ {1} - \left(1 - \frac {\gamma}{n}\right) \right] x _ {1} = \frac {\left[ z _ {1} - \left(1 - \frac {\gamma}{n}\right) \right] ^ {2}}{\gamma (z _ {1} + 1)}
$$

because the advertiser’s neighbors have the same reference value, and thus the last term in (12) is zero.

Corollary 4 In the case when the dominant advertiser’s (advertiser 1’s) neighboring advertisers have the same reference value and the value is the second highest (normalized to 1), when n > 2, if

$$
z _ {1} \leq \frac {\left(1 - \frac {\gamma}{n}\right) - \sqrt {\gamma \left(1 - \frac {\gamma}{4}\right) \left[ \left(1 - \frac {\gamma}{n}\right) ^ {2} - \left(1 - \frac {\gamma}{2}\right) ^ {2} \right]}}{\left(1 - \frac {\gamma}{2}\right) ^ {2}}
$$

the dominant advertiser is better off under behavioral targeting; otherwise, the dominant advertiser is worse off under behavioral targeting.

The intuition is as follows. When the dominant advertiser has a low valuation (close to that of the other advertisers), the competition under traditional advertising leaves the dominant advertiser little profit margin. In contrast, under behavioral targeting, with the relaxed competition, the dominant advertiser can reap benefits from his targeted users. Therefore, the dominant advertiser is better off under behavioral targeting. With a high valuation, the dominant advertiser can grab the whole group of users under traditional advertising while maintaining a considerable profit margin. Under behavioral targeting, the dominant advertiser wins significantly fewer users because other advertisers have advantage with their targeted users. Therefore, the dominant advertiser is worse off under behavioral targeting.

Notice that the number of advertisers plays an important role in mediating the aforementioned tradeoff. When the number increases, the dominant advertiser’s payoff remains the same under traditional advertising, while his payoff decreases under behavioral targeting because more advertisers split the users. As a result, everything else being equal, the dominant advertiser is more likely to be better off under behavioral targeting when the number of advertisers is low. In the case with two advertisers, as indicated in Proposition 4, the dominant advertiser is always (weakly) better off under behavioral targeting.

## Joint Payoff of Publisher and Advertisers

We next compare the joint payoff of the publisher and the advertisers under the two different advertising technologies. The joint payoff is defined as the sum of the publisher’s payoff and the advertisers’ payoffs, or the value created by users through advertising. In a sense, the joint payoff concerns the total “pie” created from the advertising slot, which would be an important consideration for the publisher in the long term and/or when facing competition for advertisers.

Recall that in equilibrium advertisers bid their true value and that under behavioral targeting each user is allocated to the advertiser with the highest value. The realized highest value of each user is the joint payoff for the advertiser and the publisher created from each user. Therefore, the equilibrium allocation under behavioral targeting creates the maximum joint payoff. In contrast, the equilibrium allocation under traditional advertising cannot generate the maximum joint payoff. To illustrate, note, for example, the users located at [x , 1/2] from advertiser 1 in Figure 3. These users are assigned to advertiser 1 under traditional advertising, although advertiser 2 values them more. Thus, the joint payoff created under behavioral targeting is higher than that created under traditional advertising.

Proposition 5 The allocation under behavioral targeting generates a higher joint payoff for the publisher and the advertisers than the allocation under traditional advertising.

Notice that the joint payoff created by displaying the advertisement(s) to the users is shared by the publisher and advertiser(s) via the auction. Behavioral targeting creates a larger pie than traditional advertising, and thus engenders the possibility that both the publisher and the advertisers are better off (i.e., a possible “win–win” result). This win–win result under behavioral targeting indeed occurs in many cases. For example, all advertisers are better off under behavioral targeting in many cases such as in the symmetric case (by Corollary 3), and the publisher is also better off under behavioral targeting when the number of advertisers is large. Therefore, in the case with both conditions satisfied, behavioral targeting leads to a win–win equilibrium.

## Extensions with Opt-Out Choice and Without Comparable Value Assumption

In this section we extend our model by relaxing some of the assumptions made previously. First, it is worthy to note that although we adopt a linear decay function, our results hold qualitatively and the insights derived stay the same for nonlinear forms of the decay function. In particular, if we use a nonlinear delay function, Proposition 2(a) regarding the threshold number “2” about the publisher continues to hold, because the intuition provided applies to the other decay functions as well. The threshold $ { { } ^ { \circ } } 6 { } ^ { \circ }$ in Propositions 2(b) and 2(c) is different, and the threshold value depends on the form of the decay function, but the tradeoff between the competitive effect and propensity effect remains. Propositions 4(a) and 4(b.1) about the advertisers stay the same. The condition in Proposition 4(b.2) is different but can be similarly formulated. Proposition 5 about the joint payoff stays unaffected.

Second, in the baseline model, we assume that all users opt in to behavioral targeting. The FTC’s principles for online behavioral advertising (FTC 2009) explicitly require that users can opt not to have their online data and behavior collected. We here extend our model by allowing users to opt out from behavioral targeting. The comparable value assumption on the value structure (which implies that no advertiser is dominated) allows for the derivation of closed-form formulas and bounds for the online publisher’s revenue in the baseline model. We now relax this assumption as well and show that, qualitatively, the same results hold.

## Some Users Who Opt Out

In the baseline model, we assume that the publisher can learn all users’ preferences under behavioral targeting. However, because privacy advocates have expressed concerns over user privacy, in the absence of legal regulations, many selfregulated publishers now allow users to opt out of behavioral targeting in practice. Before a user decides to opt into behavioral targeting, the publisher reveals to the user (1) what kind of data can be collected; (2) what this data will be used for; and (3) with whom it will be shared. Hence, a user who opts into behavioral targeting is fully aware of the consequences and has decided that the benefits from behavioral targeting are higher than the cost of giving up some personal privacy. The publisher learns nothing about the preferences of users who opt out, and must use the overall expected clickthrough rates to determine the advertisement to be displayed for these users. Therefore, these users are always treated as under traditional advertising, even if the publisher uses behavioral targeting to auction off the advertising slot. We assume that the proportion of users who opt in is λ and the proportion of users who opt out is 1 – λ. We also assume that users’ opt-in/opt-out decisions are independent of their degrees of matching. We show that the results from the baseline model carry over.

If some users opt out, the auction under behavioral targeting becomes a hybrid of the traditional advertising and behavioral targeting ones in the baseline model. For users who opt out, the winning advertiser is chosen using traditional advertising, while for users who opt in, advertisers are chosen via behavioral targeting. The publisher’s revenue under this hybrid scheme, denoted as $\pi _ { B } ^ { ' } ,$ now consists of the payments for the users who opt in and the payments for the users who opt out. The revenue from each user who opts in is $\pi _ { B }$ as in the baseline model, and the revenue from each user who opts out is $\pi _ { T } .$ Therefore, the total revenue under behavioral targeting is

$$
\pi_ {B} ^ {\prime} = (1 - \lambda) \pi_ {T} + \lambda \pi_ {B}\tag{15}
$$

where $\pi _ { B }$ and $\pi _ { T }$ are defined in Equations (3) and (13), respectively.

The above revenue under behavioral targeting when some users opt out is the weighted average of the revenue under traditional advertising and the revenue under behavioral targeting in the baseline model. Therefore, the comparison between the revenue under behavioral targeting when some users opt out $( \pi _ { B } ^ { ' } )$ and the revenue under traditional advertising $( \pi _ { T } )$ is essentially the same as that between $\pi _ { B }$ and $\pi _ { T } .$ Hence, all results regarding the publisher’s revenue comparison under the two advertising technologies continue to hold. The only adjustment required is the expression of the maximum gain in Proposition 3. The gain under behavioral targeting now comes from the users who opt in, and the maximum gain is thus λ times the maximum gain in the baseline model. Clearly, the maximum gain in this case is increasing in the proportion of users who opt in to behavioral targeting. Advertisers’ payoffs can be similarly analyzed, and the same results hold as long as some users opt in to behavioral targeting.

As in Proposition 5, the joint payoff for the publisher and the advertisers can be shown to be higher under behavioral targeting than under traditional advertising, because, similar to that in Equation (15), the joint payoff under this hybrid scheme is a weighted average of the joint payoff under traditional advertising and that under behavioral targeting in the baseline model (and, similarly, the weights are (1 – λ) and $\lambda ,$ respectively).

If we include users’ utility in addition to the joint payoff of the publisher and the advertisers in Proposition 5, we can compute the social welfare of all three parties involved: the publisher, the advertisers, and the users. However, the opinions in the literature so far are mixed on whether behavioral targeting increases or decreases the users’ utility. For example, Picker (2009) argues that targeted advertising reduces search costs and hence increases consumer utility. On the other hand, McDonald and Cranor (2010a, 2010b), through user interviews, find that consumers believe targeted advertising to be intrusive to their privacy and that users are willing to pay to avoid them, which implies that behavioral targeting decreases consumer utility. Settling this controversy is outside the scope of this paper; different perspectives can lead to different consumer utility measures, which in turn can lead to different conclusions regarding consumer utility. When all users are subject to behavioral targeting, the effect on users’ utility can only be assessed from a specific chosen perspective, and then a broad social welfare measure that includes users’ utility can be evaluated accordingly. However, when users are allowed to opt out of behavioral targeting and assuming that users act rationally and have perfect knowledge of how behavioral targeting affects their utility, the analysis becomes easier. In this case, the users who expect a negative effect on their utility from behavioral targeting opt out, and the others opt in. In such a situation, the social welfare for the publisher, advertisers, and users is always higher under behavioral targeting than under traditional advertising. The reasoning is as follows: The users who opt out (i.e., the (1 – λ) users) are treated the same as under traditional advertising and thus derive the same utility as under traditional advertising. The users voluntarily choosing behavioral targeting (i.e., the λ users) must have a higher utility under this advertising technology than under traditional advertising. Altogether, in the presence of an optout choice, all users are (weakly) better off under behavioral targeting. Therefore, the social welfare in the broad measure is also higher under behavioral targeting (with the opt-out option).

Corollary 5 When users are given the choice to opt out of behavioral targeting, the social welfare for the publisher, advertisers, and users is higher under behavioral targeting than under traditional advertising.

As discussed earlier, under the increased joint payoff for the publisher and the advertisers, both parties can benefit from behavioral targeting at the same time in many scenarios. In addition to this, now users are (weakly) better off when given the choice of opting out or opting in. As a result, under this hybrid scheme, behavioral targeting can result in a “win–win– win” outcome for the publisher, advertisers, and users.

## The Case Without Comparable Value Assumption

In the baseline model, we imposed the comparable value assumption, $z _ { ( n ) } { \ge } z _ { ( 1 ) } ( 1 { - } \gamma / n )$ , which implies that no advertiser is strictly dominated—that is, every advertiser has at least one user group (however small) for which his advertisement would be displayed. In this section, we show that the main insights remain the same if we relax this assumption.

The results under traditional advertising are the same as in the baseline model, because the analysis of traditional advertising does not involve the comparable value assumption. Under behavioral targeting, we can verify that advertisers continue to bid their true per-click unit value. The result of Lemma 3 remains: the revenue continues to be (weakly) increasing in advertisers’ reference value. We can similarly characterize the value structures that lead to the maximum and minimum revenues as in Proposition 1. In the structure that generates the highest revenue, given $z _ { ( 2 ) } { \mathrm { . } }$ , we must have $z _ { ( 3 ) } = z _ { ( 4 ) } = \dots z _ { ( n ) }$ $\begin{array} { r } { { \bf \Pi } = { \bf \Pi } _ { Z _ { ( 2 ) } , } } \end{array}$ as in Proposition 1, because of the monotonicity between revenue and the advertisers’ reference value. Regarding the value of the dominant advertiser with the highest reference value $z _ { ( 1 ) } ,$ the revenue, on the one hand, is (weakly) increasing in $z _ { ( 1 ) } .$ . On the other hand, when the value is large enough such that the advertiser wins all users, any further increase in the advertiser’s value does not change the payment for each user and thus the revenue is not affected. Therefore, the value structure that results in the highest revenue is the one in which $z _ { ( 3 ) } = z _ { ( 4 ) } = \ldots = z _ { ( n ) } = z _ { ( 2 ) }$ and in which the dominant advertiser’s value of his least targeted user (i.e., the user who is 1/2 distant from the dominant advertiser) is higher than the value of that user to other advertisers (such that the dominant advertiser wins all users). In the structure that generates the lowest revenue, we must have $z _ { ( 1 ) } = z _ { ( 2 ) }$ and $z _ { ( 3 ) } = z _ { ( 4 ) } = \dots = z _ { ( n ) } = 0$

For a comparison of the publisher’s revenues under the two advertising technologies, as in Proposition 2, when there are only two advertisers, the publisher is always (weakly) better off using traditional advertising. However, unlike in the baseline model under the comparable value assumption, even if the number of advertisers is large, the publisher can still be better off using traditional advertising. In other words, if the comparable value assumption is not satisfied, the publisher might prefer traditional advertising, even given a large number of advertisers. The reason is that, in this case, the number of advertisers is not a sufficient measure for competition: even if there are a considerable number of advertisers, the competition among advertisers could be low because the very low-value advertisers (e.g., the zero-value advertisers in the extreme) will be strictly dominated and their presence does not affect the competition. For example, suppose 2m advertisers are competing for the advertising slot, advertiser 1 and advertiser m + 1 have a reference value z, and other advertisers have very low reference values (e.g., close to zero). In this case, the competition structure is very similar to the case with just two advertisers of reference value z. As a result, traditional advertising results in higher revenue than behavioral targeting, even if the number of advertisers is high. In fact, the insight revealed by Proposition 2 is about balancing the competitive effect and the propensity effect, which remains in effect in this general case. The seeming difference in the revenue comparisons in the baseline case and in this general case occurs because the competitive effect cannot be properly reflected by the mere number of advertisers in the latter case.

For illustrative purposes, we next introduce the concept of active (or non-dominated) advertisers and use the associated properties to measure competition. We say an advertiser is active if there exists at least one user for which the advertiser has the highest (or one of the highest) value(s) among all advertisers. In other words, an advertiser is not active if the advertiser is strictly dominated by others for every user. We denote the maximum distance between any two adjacent active advertisers as s (notice that active advertisers might not be symmetrically distributed) and the minimum reference value of any active advertiser as $z _ { m i n } .$ The combination of maximum distance and minimum reference value is an appropriate measure of competition in this general case. Intuitively, the former reflects the market share that an advertiser might grab, and the latter reflects the price that an advertiser has to pay. Under s and $z _ { m i n } ,$ the minimum average price that any advertiser has to pay is

$$
\frac {1}{2} \left[ z _ {\min} (1 - \gamma s) + z _ {\min} \left(1 - \frac {1}{2} \gamma s\right) \right] = z _ {\min} \left(1 - \frac {3}{4} \gamma s\right)
$$

which occurs when two active advertisers with $z _ { m i n }$ are adjacent with distance s. Therefore, according to (3), when

$$
z _ {m i n} \left(1 - \frac {3}{4} \gamma s\right) > z _ {(2)} \left(1 - \frac {\gamma}{4}\right)
$$

or when $z _ { m i n }$ is large and s is small such that the competition under behavioral targeting is high enough, behavioral targeting generates higher revenue than traditional advertising. This condition reiterates the insight revealed earlier: when the loss from reduced competition under behavioral targeting can be compensated for by the gain from the propensity effect, behavioral targeting is superior to traditional advertising.

As in Proposition 4, all advertisers except the dominant advertiser continue to be (weakly) better off because they might have a positive market share under behavioral targeting (compared to the zero market share under traditional advertising). The dominant advertiser is (weakly) better off under behavioral advertising when there are only two advertisers. When there are more than two advertisers, we can similarly derive the condition under which the dominant advertiser is better off. As in Proposition 5, behavioral targeting results in a higher joint payoff for the publisher and the advertisers than traditional advertising. The only adjustment we need to make is the expression of the maximum gain in Proposition 3. The maximum gain in this general case is $\frac { \gamma } { 4 - \gamma } \frac { ( n - 2 ) ( n + 1 ) } { n ^ { 2 } }$ , which is again increasing in the number of advertisers and user heterogeneity (see Appendix for the proof). But, the maximum gain is higher in the general case than in the baseline case because the value of the dominant advertiser (and hence his payments) can be larger without the comparable value assumption.

In sum, the main results from the baseline model continue to hold qualitatively without the comparable value assumption. The main difference is that, without the assumption, the number of advertisers alone is not a sufficient measure of the competition among advertisers in the tradeoff for the publisher between the competitive effect and the propensity effect.

## Conclusion

In this paper, we analyze the economic implications of behavioral targeting for the main players involved: advertisers and online publishers. Contrary to conventional wisdom, our study reveals that, for an online publisher, behaviorally targeted advertisements that are auctioned off under the rule of second weighted unit price might result in lower revenue than traditional advertising. We identify two effects associated with behavioral targeting—the competitive effect and the propensity effect—that affect the online publisher’s revenue in opposite directions. The relative strength of the two effects determines whether the publisher’s revenue is positively or negatively affected. Advertisers’ payoffs are affected asymmetrically. While small advertisers are generally better off under behavioral targeting by winning their targeted users, the dominant advertiser might or might not be better off. The dominant advertiser is worse off under behavioral targeting when he has a significant competitive advantage over his competitors because under traditional advertising, he would otherwise grab a larger group of users and still realize a decent payoff.

In examining the benefit for the publisher from behavioral targeting, our paper reveals the trade-off between the competitive effect and the propensity effect. The competitive effect refers to the relaxed competition resulting from the differentiation under behavioral targeting, which is similar to that in horizontal product differentiation models (e.g., Salop 1979; Tirole 1988). In the latter models, firms directly compete with each other for customers, whereas in our model firms (advertisers) compete for customers (users) via the publisher’s advertising slot. Our focus is on the publisher’s advertising technology choice (i.e., traditional advertising versus behavioral targeting) and on how this technology choice affects the publisher’s and advertisers’ payoffs and social welfare. Our research thus contributes to this stream of literature by introducing the publisher as a third layer on top of a horizontal product differentiation setup and integrating auctions within the framework. Because it gives advertisers their favorable users, behavioral targeting can also be viewed as product customization by the publisher, if we view advertisers as the publisher’s customers and users as the publisher’s products. Departing from earlier studies on product customization (e.g., Dewan et al. 2003), the critical feature of our setting is that customers (advertisers) compete for the publisher’s resource, which brings in new insights beyond the existing literature.

So far, behavioral targeting mainly takes place on the Internet. Ultimately, such targeted advertisements could be sent to televisions using a technology called “addressable television.” This much-touted technology, by which different advertisements can be sent to different television sets, was until recently thought to be “vaporware” rather than a practical reality. However, new advances have been made in the technology, as evidenced by Google’s recent investment in Invidi in May 2010 (Kafka 2010). Addressable television, together with the increasing use of unicast advertising for online video and other content, brings new possibilities for advertisers and publishers, and also underscores the importance of understanding the implications of such technologies.

## Managerial Implications

As we show in the paper, when advertisers are roughly similar in valuations and click-throughs, the online publisher’s revenue increases under behavioral targeting if, and only if, the number of advertisers is sufficiently high. When the advertisers’ valuations and click-throughs significantly differ from each other, the number of advertisers is not a sufficient measure in choosing the advertising technologies. The rule of thumb is that behavioral targeting may generate higher revenue only if the resulting competition is not seriously reduced.

The implications for online publishers are two-fold. On the one hand, behavioral targeting is not necessarily better in terms of generating revenue. For small publishers that face low demand for their advertising space, staying with traditional advertising might be best, even without considering the cost for switching to behavioral targeting. The cost of running behavioral targeting includes the one-time cost of acquiring an accurate behavioral targeting algorithm, as well as the ongoing costs of collecting, storing, and updating users’ profile data. Incorporating such costs, which we do not consider in this paper, tips the balance even further in favor of traditional advertising.

On the other hand, we show that when sufficient competition exists among similar advertisers, the behavioral targeting revenue for the online publisher can approach double the income from traditional advertising. Thus, the decision by online publishers to adopt behavioral targeting should be driven by the particular set of advertiser characteristics they face. Publishers that face considerable demand for their advertising resources can improve revenue by switching to behavioral targeting. For big publishers with multiple advertising resources (e.g., YouTube with different video clips), the advertising technology chosen can be tailored based on the popularity of the advertising resource: popular ones by behavioral targeting and unpopular ones by traditional advertising.

Our study also implies that advertisers’ incentives for switching to behavioral targeting are not totally aligned. All advertisers except for the advertiser with the greatest competitive advantage (i.e., the dominant advertiser in our model) have a higher payoff under behavioral targeting, indicating that they would voluntarily adopt behavioral targeting. Except for special cases, whether the most competitive advertiser benefits from behavioral targeting hinges on a combination of factors, such as the number of advertisers and the valuations of the competitors who share a similar user preference. The most competitive advertiser benefits from and is willing to switch to behavioral targeting only if the strength in his competitive advantage is low. In other words, a really dominant and competitive advertiser might object to the transition to behavioral targeting, despite the temptation of exposing the advertisement only to users of high relevance. In this case, special contract terms might be considered for those advertisers if necessary.

This research also has implications for social planners, such as the Federal Trade Commission. With the commonly used second weighted unit-price auctions, the allocation of advertising resources under behavioral targeting is a way to maximize the total welfare of the publisher and the advertisers. Therefore, behavioral targeting should be encouraged, given the premise that the users’ privacy concerns with behavioral targeting are properly addressed and thus that their utilities are not compromised. Users benefit as well if online publishers allow them to opt out of behavioral targeting. Users need to be aware of this option so that they can choose to stay with traditional advertising (e.g., if they are uncomfortable with their private data being collected). The current practice of self-regulation proposed by the FTC is generally in line with the suggestion prescribed in this study. If selfregulation practices are limited or ineffective, stricter regulations should be established and enforced to protect users and to reap the gain for publishers, advertisers, and users as an interdependent system. Again, another concern with behavioral targeting is the cost of implementation. In calibrating the net benefit from behavioral targeting, such costs should be taken into account. When the cost becomes negligible compared to the benefit realized as the technology advances, behavioral targeting should be widely promoted, and the FTC may even consider subsidizing or facilitating the switch to behavioral targeting by, for example, offering standard tracking software.

## Limitations and Future Research

This paper has several limitations that suggest the direction for future research. First of all, we take the second weighted unit-price auctions that are widely used in online advertising practice as given, and do not offer the results under different auction formats. Under a standard auction setting, one wellknown result is the “revenue equivalence” theorem (Klemperer 1999; McAfee and McMillan 1987). Given that our setting departs from the standard setting in many dimensions, such as the valuation dependence associated with the horizontal differentiation model, we do not expect that the revenue equivalence theorem continues to hold. Therefore, despite the popularity of the second weighted unit-price auctions, one natural theoretical question for future research is whether other types of auctions, such as first weighted unitprice auctions (in which bidders pay the unit prices they bid), can outperform the one commonly used in practice. Furthermore, the optimal auction design for the setting studied in this paper—in which the auctioneer (i.e., the publisher) has nonidentical continuous objects (i.e., users) to auction off and their value to bidders (i.e., advertisers) are dependent— remains far from clear.

Second, we do not explicitly model the privacy sensitivity of consumers. Another interesting future direction would be to introduce some utility function incorporating consumer privacy and study consumers’ decision making and the implications to social welfare.

In addition, under the second weighted unit-price payment scheme, the prices for users are discriminatory (i.e., an advertiser would need to pay more for a click-through from a less preferred user). To facilitate the implementation of our auction mechanism and eliminate these discriminatory payments, the publisher might be able to compute a uniform payment per click-through. Many questions arise, including whether a payment exists such that all other conditions (e.g., truthful bidding by advertisers) and results remain satisfied. Also interesting to study would be the optimal user segmentation in the setting introduced in this paper.

## Acknowledgments

We thank the review team for their detailed and constructive comments. We thank R. Preston McAfee from Yahoo! for his insights on the practice of behavioral targeting. We also thank participants at the Workshop on Information Systems and Economics (2010), INFORMS Annual Meeting (2010, 2011), The Fifth China Summer Workshop on Information Management (2011), INFORMS Conference on Information Systems and Technology (2011), and 2012 Winter Conference on Business Intelligence, as well as seminar participants at Emory University, Georgia Institute of Technology, the University of Arizona, the University of Texas at Dallas, Shanghai Jiao Tong University, and the University of Connecticut for their helpful feedback.

## References

Angwin, J. 2010. “The Web’s New Gold Mine: Your Secrets,” Wall Street Journal, July 30.

Bapna, R., Goes, P., and Gupta, A. 2003. “Analysis and Design of Business-to-Consumer Online Auctions,” Management Science (49:1), pp. 85-101.

Bapna, R., Goes, P., Gupta, A., and Jin, Y. 2004. “User Heterogeneity and its Impact on Electronic Auction Market Design: An Empirical Exploration,” MIS Quarterly (28:1), pp. 21-43.

Bazilian, E. 2011. “Google Completes Rollout of Interest-Based Advertising: Adwords Will Be Able to Target Customers Based on Web Behavior,” technical report, AdWeek, June 28.

Beales, H. 2010. “The Value of Behavioral Targeting,” Network Advertising Initiative (http://www.networkadvertising.org/pdfs/ Beales\_NAI\_Study.pdf).

Chen, J., Liu, D., and Whinston, A. B. 2009. “Auctioning Keywords in Online Research,” Journal of Marketing (73:4), pp. 125-141.

Clifford, S. 2009. “Many See Privacy on Web as Big Issue, Survey Says,” New York Times, March 15.

Dewan, R., Jing, B., and Seidmann, A. 2003. “Product Customization and Price Competition on the Internet,” Management Science (49:8), pp. 1055-1070.

Economist. 2008. “Watching While You Surf,” The Economist, June 5.

Esteban, L., and Hernandez, J. M. 2007. “Strategic Targeted Advertising and Market Fragmentation,” Economics Bulletin (12:10), pp. 1-12.

FTC. 2009. “Self-Regulatory Principles for Online Behavioral Advertising,” technical report, Federal Trade Commission.

Gal-Or, E., and Gal-Or, M. 2005. “Customized Advertising Via a Common Media Distributor,” Marketing Science (24:2), pp. 241-253.

Gal-Or, E., Gal-Or, M., May, J. H., and Spangler, W. H. 2006. “Targeted Advertising Strategies on Television,” Management Science (52:5), pp. 713-725.

Geng, X., Stinchcombe, M. B., and Whinston, A. B. 2006. “Product Bundling,” in Handbooks in Information Systems, T. Hendershott (ed.), Amsterdam: Elsevier, pp. 499-525.

Ghose, A., and Huang, K-W. 2009. “Personalized Pricing and Quality Customization,” Journal of Economics and Management Strategy (18:4), pp. 1095-1135.

Ghosh, A., Nazerzadeh, H., and Sundararajan, M. 2007. “Computing Optimal Bundles for Sponsored Search,” in Proceedings of the 3<sup>rd</sup> International Conference on Internet and Network Economics, Lecture Notes in Computer Science (4858), pp. 576-583.

Gilbert, F. 2008. “Beacons, Bugs and Pixel Tags: Do You Comply with the FTC Behavioral Marketing Principles and Foreign Law Requirements?,” Journal of Internet Law, pp. 3-10.

Goldfarb, A., and Tucker, C. E. 2011. “Privacy Regulation and Online Advertising,” Management Science (57:1), pp. 57-71.

Hallerman, D. 2010. “Audience Ad Targeting: Data and Privacy Issues,” technical report, eMarketer Report.

Iyer, G., Soberman, D., and Villas-Boas, J. M. 2005. “The Targeting of Advertising,” Marketing Science (24:3), pp. 461-476.

Kafka, P. 2010. “Google Ups its TV Bet, Invests in Invidi,” CNET News, May 5.

Klemperer, P. 1999. “Auction Theory: A Guide to the Literature.,” Journal of Economic Surveys (13:3), pp. 227-286.

Liu, D., Chen, J., and Whinston, A. B. 2010. “Ex Ante Information and Design of Keyword Auctions,” Information Systems Research (21:1), pp. 133-153.

Liu, H., and Lin, L-J. 2007. “Method and Apparatus for Selecting Advertisements to Serve Using User Profiles, Performance Scores, and Advertisements Revenue Information,” United States Patent Application Publication US 2007/0239534 A1.

McAfee, R. P., and McMillan, J. 1987. “Auctions and Bidding,” Journal of Economic Literature (25:2), pp. 699-738.

McDonald, A. M., and Cranor, L. F. 2010a. “Americans’ Attitudes About Internet Behavioral Advertising Practices,” in Proceedings of the 9<sup>th</sup> Workshop on Privacy in the Electronic Society, New York: ACM Press.

McDonald, A. M., and Cranor, L. F. 2010b. “Beliefs and Behaviors: Internet Users’ Understanding of Behavioral Advertising,” in Proceedings of 38<sup>th</sup> Research Conference on Communication, Information and Internet Policy, October 1-3, Arlington, VA.

Palfrey, T. R. 1983. “Bundling Decisions by a Multiproduct Monopolist with Incomplete Information,” Econometrica (51:2), pp. 463-483.

Picker, R. C. 2009. “Online Advertising, Identity and Privacy,” Working Paper, The Law School, University of Chicago.

Pinker, E. J., Seidmann, A., and Vakrat, Y. 2003. “Managing Online Auctions: Current Business and Research Issues,” Management Science (49:11), pp. 1457-1484.

Salop, S. C. 1979. “Monopolistic Competition with Outside Goods,” The Bell Journal of Economics (10:1), pp. 141-156.

Tirole, J. 1988. The Theory of Industrial Organization, Cambridge, MA: MIT Press.

Yan, J., Liu, N., Wang, G., Zhang, W., Jiang, Y., and Chen, Z. 2009. “How Much Can Behavioral Targeting Improve Online Advertising?,” in Proceedings of the 18<sup>th</sup> International Conference on World Wide Web, Madrid, Spain, pp. 261-270.

Zhang, X. M., and Feng, J. 2011. “Cyclical Bid Adjustments in Search-Engine Advertising,” Management Science (57:9), pp. 1703-1719.

## About the Authors

Jianqing Chen is an assistant professor in information systems at the Naveen Jindal School of Management at the University of Texas at Dallas and was previously an assistant professor at the Haskayne School of Business at the University of Calgary. He received his Ph.D. from McCombs School of Business at the University of Texas at Austin in 2008. His general research interests are in electronic commerce, economics of information systems, and supply chain management. His papers have been published in academic journals, including Decision Analysis, Decision Support Systems, Economics Letters, Information Systems Research, Journal of Management Information Systems, Journal of Marketing, Journal of Marketing Research, and Production and Operations Management. He was the co-recipient of the Best Paper award for the 15<sup>th</sup> Conference on Information Systems and Technology in 2010.

Jan Stallaert is a professor in operations and information management at the University of Connecticut. His research interests are in electronic commerce, competition in electronic retailing, auction mechanisms for resource allocation, and group decision making. His papers have been published in Management Science, Information Systems Research, Journal of Management Information Systems, Production and Operations Management, INFORMS Journal on Computing, Discrete Applied Mathematics, and others. He was the co-recipient of the Best Publication in an Information Systems Journal award from the Association for Information Systems in 2011.

# AN ECONOMIC ANALYSIS OF ONLINE ADVERTISING USING BEHAVIORAL TARGETING

Jianqing Chen

Jindal School of Management, The University of Texas at Dallas, 800 West Campbell Road, Richardson, TX 75080 U.S.A. {chenjq@utdallas.edu}

Jan Stallaert

School of Business, University of Connecticut, 2100 Hillside Road, Storrs, CT 06269 U.S.A. {jan.stallaert@business.uconn.edu}

## Appendix

## A.1 Summary of Notations

<table><tr><td>Notation</td><td>Definition and Comments</td></tr><tr><td>i</td><td>Index for advertisers</td></tr><tr><td>j</td><td>Index for users</td></tr><tr><td>n</td><td>Number of advertisers</td></tr><tr><td>pi</td><td>Probability that advertiser i&#x27;s most targeted user clicks on his advertisement</td></tr><tr><td>xij</td><td>Distance between advertiser i and user j along the circle</td></tr><tr><td>γ</td><td>Decay factor, which also measures the heterogeneity of users&#x27; preferences</td></tr><tr><td>qij</td><td>Decay in the probability that user j clicks on advertiser i</td></tr><tr><td>vi</td><td>Unit value that advertiser i derives from each click</td></tr><tr><td>zi</td><td>Advertiser i&#x27;s reference value, defined as zi = vi pi</td></tr><tr><td>z(i)</td><td>The ith highest value among all zi</td></tr><tr><td>πT</td><td>The publisher&#x27;s revenue under traditional advertising</td></tr><tr><td>πB</td><td>The publisher&#x27;s revenue under behavioral targeting</td></tr><tr><td>xi</td><td>Marginal user for allocation under behavioral targeting who has the same value to advertisers i and i + 1</td></tr><tr><td>yi</td><td>Marginal user for payment under behavioral targeting who has the same value to advertisers i - 1 and i + 1</td></tr><tr><td>Δi</td><td>Cross-border effect under behavioral targeting</td></tr><tr><td>Hi</td><td>Advertiser i&#x27;s expected payment for the users won under behavioral targeting</td></tr><tr><td>Ai</td><td>Advertiser i&#x27;s payoff under behavioral targeting</td></tr></table>

## A.2 Proof of Lemma 1

Proof. We consider any advertiser i’s bidding strategy $b _ { i }$ . We suppose that among the rest of advertisers, advertiser l has the highest proposed expected payment $b _ { l } \cdot p _ { l } \mathrm { E } [ q ] . \mathrm { I f } \ : b _ { i } \cdot p _ { i } \mathrm { E } [ q ] > b _ { l } \cdot p _ { l } \mathrm { E } [ q ]$ , advertiser i wins the auction with total expected payment $b _ { l } p _ { l } \mathrm { E } [ q ]$ , and his payoff is

$$
v _ {i} p _ {i} \mathrm{E} [ q ] - b _ {l} p _ {l} \mathrm{E} [ q ]\tag{16}
$$

Otherwise, the advertiser loses the auction and his payoff is zero.

We first consider bidding $b _ { i } < \nu _ { i } . \mathrm { ~ I f ~ } b _ { i } \cdot p _ { i } \mathrm { E } [ q ] > b _ { l } \cdot p _ { l } \mathrm { E } [ q ]$ , the advertiser wins the auction and derives the payoff in Equation (16), just as if bidding v<sub>i</sub>. $\mathrm { I f } b _ { l } \cdot p _ { l } \mathrm { E } [ q ] > \nu _ { i } \cdot p _ { i } \mathrm { E } [ q ]$ , the advertiser loses the auction and derives zero payoff, just as if bidding $\nu _ { i \cdot } \ \mathrm { I f } \ b _ { i } \cdot p _ { i } \mathrm { E } [ q ] < b _ { l } \cdot p _ { l } \mathrm { E } [ q ] $ $< \nu _ { i } \cdot p _ { i } \operatorname { E } [ q ]$ , bidding $b _ { i }$ causes the advertiser to lose the auction and receive zero payoff, whereas if he had bid $\nu _ { i } ,$ the advertiser would have won the auction and derived positive payoff as in Equation (16). Therefore, bidding $b _ { i } < \nu _ { i }$ is (weakly) dominated by bidding $\nu _ { i } .$

We then consider bidding $b _ { i } > \nu _ { i } . \mathrm { I f } \nu _ { i } \cdot p _ { i } \mathrm { E } [ q ] > b _ { l } \cdot p _ { l } \mathrm { E } [ q ]$ , the advertiser wins the auction and derives the payoff in Equation (16), just as if bidding $\nu _ { i } . \mathrm { \ I f } \ : b _ { l } \cdot p _ { l } \mathrm { E } [ q ] > b _ { i } \cdot p _ { i } \mathrm { E } [ q ] $ , the advertiser loses the auction and derives zero payoff, just as if bidding $\nu _ { i } . \mathrm { ~ } \mathrm { I f } \nu _ { i } \cdot p _ { i } \mathrm { E } [ q ] < b _ { l } \cdot p _ { l } \mathrm { E } [ q ] $ $< b _ { i } \cdot p _ { i } \operatorname { E } [ q ]$ , bidding b causes the advertiser to win the auction with negative payoff, whereas bidding v leads to zero payoff. Therefore, bidding $b _ { i } > \nu _ { i }$ is (weakly) dominated by bidding $\nu _ { i } .$ All together, bidding true value $\nu _ { i }$ is advertiser $i ^ { \prime } \mathrm { s } \left( \mathrm { w e a k l y } \right)$ dominant strategy.

Under behavioral targeting, the same argument applies, simply replacing $p _ { i } \operatorname { E } [ q ]$ with $p _ { i } q _ { i j }$ for user j.

## A.3 Proof of Lemma 2

Proof. For any advertiser k different from advertisers i and i + 1, we first consider the case where the shortest path from user j (located between advertiser i and i + 1) to advertiser k passes advertiser i. $\operatorname { I f } z _ { i } \geq z _ { k }$ then $z _ { k } ( 1 - \gamma x _ { k j } ) < z _ { i } ( 1 - \gamma x _ { i j } )$ because $x _ { i j } < x _ { k j } . \mathrm { \scriptsize ~ I f } \ z _ { i } < z _ { k } ,$ we have (assuming $k < i )$

$$
z _ {k} \left(1 - \gamma x _ {k j}\right) = z _ {k} \left[ 1 - \gamma \left(\frac {i - k}{n} + x _ {i j}\right) \right] <   z _ {i} - z _ {k} \gamma x _ {i j} <   z _ {i} \left(1 - \gamma x _ {i j}\right)
$$

where the first inequality follows from the comparable value assumption and the second inequality is because $z _ { i } < z _ { k } .$ Therefore, in this case, advertiser i derives higher value than advertiser k from user j. Similarly, when the shortest path from user j to advertiser k passes advertiser $i + 1$ , advertiser i + 1 derives higher value than advertiser k from user j. All together, either advertiser i or advertiser i + 1 derives higher value than any other advertiser k from user j, and thus user j must be assigned to either advertiser i or advertiser i + 1 in equilibrium.

## A.4 Proof of Lemma 3

Proof. We denote $V _ { i j } \equiv z _ { i } q _ { i j } ,$ the value that the advertiser i derives from user j, and denote $V _ { ( 1 ) }$ and $V _ { ( 2 ) j }$ as the highest and second highest values among all $i ^ { \gamma } { \bf s } .$ . When z is increased to $z _ { i } ^ { ' } ( { \mathrm { i . e . , } } z _ { i } ^ { ' } { > } z _ { i } ) , V _ { i j } ^ { ' } { > } V _ { i j }$ and thus $V _ { ( 2 ) j } \geq V _ { ( 2 ) j } .$ . In addition, for the additional users that advertiser i wins under $\boldsymbol { z } _ { i } ^ { \mathrm { i } } ,$ the highest values under $z _ { i }$ become the second highest ones under $\dot { z _ { i } } ,$ and thus $V _ { ( 2 ) j } ^ { ' } = V _ { ( 1 ) j } > V _ { ( 2 ) j } .$ Because the publisher’s revenue is the sum of the second highest value from each user, $\pi _ { B } ^ { ' } > \pi _ { B }$

## A.5 Proof of Proposition 1

Proof. (a) By Lemma $3 , \partial \pi _ { B } / \partial z _ { i } > 0$ . Given $z _ { ( 2 ) }$ and the order constraint $z _ { ( i ) } \ge z _ { ( i + 1 ) , } ,$ to maximize $\pi _ { B } , z _ { ( 3 ) } = z _ { ( 4 ) } = \ldots = z _ { ( n ) } = z _ { ( 2 ) }$ . For $z _ { ( 1 ) } ,$ we have $\partial \pi _ { B } / \partial z _ { ( 1 ) } > 0$ 0 subject to $z _ { ( n ) } \geq z _ { ( 1 ) } \biggl ( 1 - \frac { \gamma } { n } \biggr )$ (i.e., the comparable value assumption). Noticing $z _ { ( n ) } { = } z _ { ( 2 ) } $ we conclude the $z _ { ( 1 ) }$ that maximize $\pi _ { B } \mathrm { i s } \ : z _ { ( 1 ) } = z _ { ( 2 ) } \Biggl / \Biggl ( 1 - \frac { \gamma } { n } \Biggr )$ (when the condition binds).

(b) Similarly, because $\partial \pi _ { B } / \partial z _ { i } > 0 .$ , to minimize $\pi _ { B }$ subject to $z _ { ( 2 ) }$ and $z _ { ( i ) } \geq z _ { ( i + 1 ) } ,$ we have $z _ { ( 1 ) } = z _ { ( 2 ) }$ and $z _ { ( 3 ) } = z _ { ( 4 ) } = \ldots = z _ { ( n ) }$ . Because of the comparable value assumption $z _ { ( n ) } \geq z _ { ( 1 ) } \biggl ( 1 - \frac { \gamma } { n } \biggr )$ , the $z _ { ( n ) }$ that minimizes $\pi _ { B }$ is $z _ { ( n ) } = \left( 1 - \frac { \gamma } { n } \right) z _ { ( 1 ) } = \left( 1 - \frac { \gamma } { n } \right) z _ { ( 2 ) }$

We next determine how the relative location of the two advertisers with $z _ { ( 2 ) }$ affects the revenue. When $n = 2 \mathrm { ~ o r ~ } 3$ , there is a unique relative distribution of these advertisers’ values. We next focus on the case with $n \geq 4$

We first examine the possible revenue for a user segment $i | ( i + 1 )$ . For a user segment with $z _ { i } = z _ { ( 2 ) }$ and $z _ { i + 1 } = z _ { ( 2 ) } ,$ or for user segment $z _ { ( 2 ) } | z _ { ( 2 ) } ,$ the revenue is from a base payment (in Table A1) by Equation (7) with $x _ { i } = { \frac { 1 } { 2 n } }$ . For user segmen $z _ { ( 2 ) } \mid z _ { ( n ) } , \mathrm { i f } z _ { ( 2 ) } { } ^ { , } \mathrm { s }$ other neighbor is of $\cdot _ { z _ { ( n ) } , }$ the revenue is from a base payment (in Table A1) by Equation (7) with $x _ { i } = 1 / n ; \mathrm { i f } z _ { ( 2 ) } \mathrm { ^ { , } s }$ other neighbor is ${ \mathrm { o f } } z _ { ( 2 ) } ,$ the revenue is the base payment plus the cross-border effect. By Equation (10), the cross-border effect is

$$
\frac {\left(1 - \frac {\gamma}{n}\right) ^ {2} \left(z _ {(2)} - z _ {(n)}\right) ^ {2}}{2 \gamma \left(z _ {(2)} + z _ {(n)}\right)} = \frac {\left(1 - \frac {\gamma}{n}\right) ^ {2} \left(\frac {\gamma}{n}\right) ^ {2}}{2 \gamma \left(2 - \frac {\gamma}{n}\right)} z _ {(2)} = \frac {\gamma (n - \gamma) ^ {2}}{2 n ^ {3} (2 n - \gamma)} z _ {(2)}\tag{17}
$$

For user segment $z _ { ( n ) } \mid z _ { ( n ) } ,$ if the neighbors are ${ \mathrm { o f } } z _ { ( n ) } ,$ the revenue is from a base payment (in Table A1) by Equation (7) with $x _ { i } = 1 / ( 2 n ) ;$ ; if one neighbor is of $z _ { ( 2 ) }$ and the other is of $z _ { ( n ) } ,$ the revenue is the base payment plus one piece of the cross-border effect defined in (17). If both neighbors are of $z _ { ( 2 ) } ,$ the revenue is the base payment plus two pieces of the cross-border effect (with one piece at each border).

<table><tr><td colspan="4">Table A1. The Base Payments for Possible User Segments</td></tr><tr><td>User Segment</td><td> $z_{(2)} \mid z_{(2)}$ </td><td> $z_{(2)} \mid z_{(n)}$ </td><td> $z_{(n)} \mid z_{(n)}$ </td></tr><tr><td>Base Payment</td><td> $\frac{1}{n}\left(1 - \frac{3\gamma}{4n}\right)z_{(2)}$ </td><td> $\frac{1}{n}\left(1 - \frac{\gamma}{n}\right)\left(1 - \frac{\gamma}{2n}\right)z_{(2)}$ </td><td> $\frac{1}{n}\left(1 - \frac{\gamma}{n}\right)\left(1 - \frac{3\gamma}{4n}\right)z_{(2)}$ </td></tr></table>

Notice the base payment from each user segment $i | ( i + 1 )$ is solely determined by the values z and $z _ { i + 1 }$ (while the cross-border effect depends on the neighbors’ values). Therefore, the revenue from base payments (excluding the cross-border effect) can differ only when the two highestvalue advertisers are adjacent and when they are not. In the former, the revenue consists revenue from one $z _ { ( 2 ) } \left| z _ { ( 2 ) } \right.$ segment, from two $z _ { ( 2 ) } \left| z _ { ( n ) } \right.$ segments, and from $\left( n - 3 \right) z _ { ( n ) } \mid z _ { ( n ) }$ segments; in the latter (the non-adjacent case), the revenue consists of revenue from four $z _ { ( 2 ) } \left| z _ { ( n ) } \right.$ segments and from $\left( n - 4 \right) z _ { \scriptscriptstyle ( n ) } \mid z _ { \scriptscriptstyle ( n ) }$ segments. The difference in these revenues is the revenue from one $z _ { ( 2 ) } \left| z _ { ( 2 ) } \right.$ and from one $z _ { ( n ) } \mid z _ { ( n ) }$ minus the revenue from two $z _ { ( 2 ) } \mid z _ { ( n ) } ;$ that is,

$$
\frac {1}{n} \left(1 - \frac {3 \gamma}{4 n}\right) z _ {(2)} + \frac {1}{n} \left(1 - \frac {\gamma}{n}\right) \left(1 - \frac {3 \gamma}{4 n}\right) z _ {(2)} - \frac {2}{n} \left(1 - \frac {\gamma}{n}\right) \left(1 - \frac {\gamma}{2 n}\right) z _ {(2)} = \frac {1}{n} \left(1 - \frac {3 \gamma}{4 n}\right) z _ {(2)} - \frac {1}{n} \left(1 - \frac {\gamma}{n}\right) \left(1 - \frac {\gamma}{4 n}\right) z _ {(2)} = \frac {1}{n} \frac {\gamma}{2 n} \left(1 - \frac {\gamma}{2 n}\right) z _ {(2)} > 0
$$

which indicates that the revenue from base payments is greater when the highest-value advertisers are adjacent.

If the two highest-value advertisers are adjacent, the total revenue includes four pieces of cross-border effects, in addition to the revenue from the base payment. When $n = 4$ , the four pieces consist of two from the two $z _ { ( 2 ) } | z _ { ( n ) }$ segments (because in each segment $z _ { ( 2 ) }$ neighbors the other $z _ { ( 2 ) } )$ and two from the $z _ { ( n ) } \mid z _ { ( n ) }$ segment (because both $z _ { ( n ) } ^ { \phantom { \dagger } } \mathbf { s }$ neighbor $z _ { ( 2 ) } )$ . When $n \geq 5 ,$ the four pieces consist of two from the two $z _ { ( 2 ) } \mid z _ { ( n ) }$ segments and two from the two $z _ { ( n ) } \mid z _ { ( n ) }$ segments with one $z _ { ( n ) }$ in each segment neighbored by $z _ { ( 2 ) }$

If the two highest-value advertisers are not adjacent, the total revenue contains no cross-border effect when $n = 4$ . Therefore, the total revenue (including the revenue from the base payment and the cross-border effect) is lower when the two highest-value advertisers are not adjacent than when they are. When $n \geq 5 ,$ if the two highest-value advertisers are 2/n distant to each other (i.e., there is one lowest-value advertiser in between), the total revenue contains two pieces of cross-border effect: either from the two $z _ { ( n ) } \mid z _ { ( n ) }$ segments with one $z _ { ( n ) }$ neighbored by $z _ { ( 2 ) }$ $( \operatorname { i f } n > 5 )$ or from the $z _ { ( n ) } \mid z _ { ( n ) }$ segment with both ${ \boldsymbol { z } _ { ( n ) } } ^ { \prime } { \mathbf { s } }$ neighbored by $z _ { ( 2 ) } \left( \mathrm { i f } n = 5 \right)$ . If at least two lowest-value advertisers are located between the two highest-value advertisers, the total revenue contains four pieces of cross-border effect. The reason is that, around each arc connecting the two ${ z _ { ( 2 ) } } ^ { \mathrm { { ' } } } \mathrm { { S } } ,$ , we should have either two $z _ { ( n ) } \mid z _ { ( n ) }$ segments with one $z _ { ( n ) }$ neighbored by $z _ { ( 2 ) }$ in each segment or one $z _ { ( n ) } \mid z _ { ( n ) }$ segment with both ${ \boldsymbol { z } _ { ( n ) } } ^ { \prime } { \mathbf { s } }$ neighbored by $z _ { ( 2 ) } .$ . Either case leads to two pieces of cross-border effect with one arc, and we have two different arcs. Therefore, when $n \geq 5 ,$ , the structure with the two highest-value advertisers being 2/n distant from each other generates the least total revenue (with the lowest revenue from the base payment and the least number of cross-border effects).

## A.6 Proof of Proposition 2

Proof. (a) When $n = 2 ,$ , by Proposition 1, given $z _ { ( 2 ) } ,$ the structure with $z _ { \scriptscriptstyle ( 1 ) } = z _ { \scriptscriptstyle ( 2 ) } / ( 1 - \gamma / 2 )$ generates the highest $\pi _ { B } ,$ in which the dominant advertiser wins all users (except the other advertiser’s most targeted user, from which both advertisers derive the same value). In this case, by Equation (7) with $x _ { i } = 1 / 2 , \pi _ { B } = \left( 1 - \frac { \gamma } { 4 } \right) z _ { ( 2 ) }$ , which is the same as $\pi _ { I }$ by Equation (3). Therefore, $\pi _ { B } \leq \pi _ { T }$ and the equality occurs only $\mathrm { i f } z _ { ( 1 ) }$ $= z _ { ( 2 ) } / ( 1 - \gamma / 2 )$

When n $\iota \geq 3 , \ \pi _ { B } > \pi _ { I }$ is always possible. For example, when $z _ { ( 1 ) } = z _ { ( 2 ) } = \dots z _ { ( n ) } , \pi _ { B }$ consists of the base payments from the $n \ z _ { ( 2 ) } \mid z _ { ( 2 ) }$ segments. According to Table A1, $\pi _ { B } = \left( 1 - \frac { 3 \gamma } { 4 n } \right) z _ { ( 2 ) }$ . Noticing $\pi _ { { \scriptscriptstyle T } } = \left( 1 - \frac { \gamma } { 4 } \right) z _ { { \scriptscriptstyle ( 2 ) } }$ , we can conclude $\pi _ { B } \geq \pi _ { I }$ when $n \geq 3$ . Furthermore, a value structure with $z _ { ( 1 ) } > z _ { ( 2 ) }$ results in a higher revenue under behavioral targeting (by Lemma 3) and in the same revenue under traditional advertising, which leads to $\pi _ { B } > \pi _ { T }$

(b) For $2 < n < 6 ,$ , traditional advertising might generate higher revenue than behavioral targeting as well. For $n = 5 ,$ , see the proof in part (c). When $n = 4 _ { : }$ , the least revenue under behavioral advertising is $\left( 1 - \frac { \gamma } { 4 } \right) \left( 1 - \frac { \gamma } { 8 } \right) z _ { ( 2 ) }$ (from four $z _ { ( 2 ) } \mid z _ { ( n ) }$ segments), which is less than $\pi _ { { \scriptscriptstyle T } } = \left( 1 - \frac { \gamma } { 4 } \right) z _ { { \scriptscriptstyle ( 2 ) } }$ regardless of γ. When $n = 3 { \mathrm { . } }$ , the least revenue consists of the base payment (from two $z _ { ( 2 ) } \mid z _ { ( n ) }$ segments and one $z _ { ( 2 ) } \mid z _ { ( 2 ) }$ segment) and two pieces of cross-border effect:

$$
\frac {1}{3} \left(1 - \frac {\gamma}{4}\right) z _ {(2)} + \frac {2}{3} \left(1 - \frac {\gamma}{3}\right) \left(1 - \frac {\gamma}{6}\right) z _ {(2)} + \frac {\gamma (3 - \gamma) ^ {2}}{2 7 (6 - \gamma)} z _ {(2)} = \left(1 - \frac {\gamma}{4}\right) z _ {(2)} + \left[ - \frac {1}{6} + \frac {\gamma}{2 7} + \frac {(1 - \gamma / 3) ^ {2}}{3 (6 - \gamma)} \right] \gamma z _ {(2)}
$$

which is less than $\pi _ { T }$ regardless of $\dot { \gamma }$ because the term in the square bracket is negative.

(c) When $n \geq 5 ,$ according to the proof of Proposition 1, the least revenue consists of the base payment (from fou $\cdot z _ { ( 2 ) } | z _ { ( n ) }$ segments and $( n - 4 )$ $z _ { ( n ) } \mid z _ { ( n ) }$ segments) and two pieces of cross-border effect:

$$
\pi_ {B} = \frac {4}{n} \left(1 - \frac {\gamma}{n}\right) \left(1 - \frac {\gamma}{2 n}\right) z _ {(2)} + \frac {n - 4}{n} \left(1 - \frac {\gamma}{n}\right) \left(1 - \frac {3 \gamma}{4 n}\right) z _ {(2)} + \frac {\gamma (n - \gamma) ^ {2}}{n ^ {3} (2 n - \gamma)} z _ {(2)}
$$

The difference between this $\pi _ { B }$ and $\pi _ { T }$ in Equation (3) is

$$
\left[ \left(1 - \frac {\gamma}{n}\right) \left(1 - \frac {3 n - 4}{4 n ^ {2}} \gamma\right) + \frac {\gamma (n - \gamma) ^ {2}}{n ^ {3} (2 n - \gamma)} - \left(1 - \frac {\gamma}{4}\right) \right] z _ {(2)} = \left[ n ^ {2} (n - 4) - (3 n - 4) (n - \gamma) + \frac {4 (n - \gamma) ^ {2}}{2 n - \gamma} \right] \frac {\gamma z _ {(2)}}{4 n ^ {3}}
$$

The term in the second square bracket is increasing in γ by noticing the first-order derivative

$$
3 n - 4 - \frac {8 (n - \gamma)}{2 n - \gamma} + \frac {4 (n - \gamma) ^ {2}}{(2 n - \gamma) ^ {2}} > 3 n - 4 - \frac {8 (n - \gamma)}{2 n - \gamma} = 3 n - 8 + \frac {4 \gamma}{2 n - \gamma} > 0
$$

and thus is greater than its value at zero $n ^ { 2 } ( n - 4 ) - ( 3 n - 4 ) n + 2 n = n ( n - 6 ) ( n - 1 )$ (which is nonnegative $\mathrm { i f } n \geq 6 )$ . Therefore, the difference is positive, and behavioral advertising generates higher revenue if $n \geq 6 . \ \mathrm { H } n = 5 .$ , the difference is negative for any γ by noting that the value of the term in the square bracket at $\gamma = 2 ~ \mathrm { i s } - 3 . 5$ . All together, we can conclude that if $\begin{array} { r } { n < 6 _ { \ddagger } } \end{array}$ , the revenue under behavioral targeting may be less than the revenue under traditional advertising. $\mathrm { I f } n \ge 6$ , the least amount of revenue under behavioral targeting is still greater than the revenue under traditional advertising. Therefore, if and only i $\mathrm { f } n \geq 6 ,$ , the publisher is better off using behavioral targeting.

## A.7 Proof of Corollary 1

Proof. Under behavioral targeting, $x _ { i } = { \frac { 1 } { 2 n } } \mathrm { { b y } \ E q u a t i o n } \left( 6 \right)$ . According to Equation (13), $\pi _ { \scriptscriptstyle B } = \left( 1 - \frac { 3 \gamma } { 4 n } \right)$ by substituting in x<sub>i</sub> and noting $\Delta _ { \mathrm { i } } = 0$ According to Equation (3), $\pi _ { { } _ { T } } = \left( 1 - \frac { \gamma } { 4 } \right)$ . Therefore, when $n = 3 , \pi _ { B } = \pi _ { T } .$ and when $n > 3 , \pi _ { B } > \pi _ { T }$

## A.8 Proof of Proposition 3

Proof. (a) When $n = 2 .$ , according to Proposition 2, the publisher is (weakly) better off under traditional advertising. Meanwhile, when the lower-value advertiser gets no market share under behavioral targeting, two advertising strategies could lead to the same revenue for the publisher. Therefore, if $n = 2 .$ , the maximum gain is zero.

When $n > 2$ , without loss of generality, we let $z _ { 1 } = z _ { ( 1 ) }$ and normalize $z _ { ( 2 ) } = 1 . ~ \pi _ { B }$ is maximized when $z _ { ( 2 ) } = z _ { ( 3 ) } = \ldots = z _ { ( n ) } = 1$ and $z _ { ( 1 ) } = 1 \bigg / \bigg ( 1 - \frac { \gamma } { n } \bigg )$ by Proposition 1. By substituting $z _ { ( 1 ) }$ and $x _ { 1 } = \mathrm { \cdot }$ 1/n into (14), we can obtain the maximum $\pi _ { B }$ and thus calculate the maximum gain as

$$
\frac {\pi_ {B}}{\pi_ {T}} - 1 = \frac {\frac {n - 2}{n} \left(1 - \frac {3 \gamma}{4 n}\right) + \frac {2}{n} \left(1 - \frac {\gamma}{2 n}\right) + \left(\frac {n - \gamma}{(2 n - \gamma) n}\right) ^ {2} \gamma}{1 - \frac {\gamma}{4}} - 1 = \frac {\frac {\gamma}{4} - \frac {\gamma}{n} \left(\frac {n - 2}{n} \frac {3}{4} + \frac {1}{n}\right) + \left(\frac {n - \gamma}{(2 n - \gamma) n}\right) ^ {2} \gamma}{1 - \frac {\gamma}{4}}\tag{18}
$$

$$
= \frac {\left(1 - \frac {3 n - 2}{n ^ {2}}\right) \gamma + \left(\frac {2 (n - \gamma)}{n (2 n - \gamma)}\right) ^ {2} \gamma}{4 - \gamma} = \frac {\gamma}{4 - \gamma} \left[ \frac {(n - 2) (n - 1)}{n ^ {2}} + \left(\frac {2 (n - \gamma)}{n (2 n - \gamma)}\right) ^ {2} \right]
$$

(b) We notice the first-order derivative of the term in the square bracket on the right-hand side of (18) with respect to $n ,$

$$
\frac {3 n - 4}{n ^ {3}} - 2 \frac {2 (n - \gamma)}{n (2 n - \gamma)} \frac {2 \left(2 n ^ {2} - 4 n \gamma + \gamma^ {2}\right)}{(2 n - \gamma) ^ {2} n ^ {2}} > \frac {3 n - 4}{n ^ {3}} - \frac {2 \left(2 n ^ {2} - 4 n \gamma + \gamma^ {2}\right)}{(2 n - \gamma) ^ {2} n ^ {2}} = \frac {(2 n - 4) (2 n - \gamma) ^ {2} + (4 n ^ {2} \gamma - n \gamma^ {2})}{(2 n - \gamma) ^ {2} n ^ {3}} > 0
$$

which indicates the maximum gain is increasing in n.

We notice the first-order derivative of the right-hand side of (18) with respect to γ,

$$
\frac {4}{(4 - \gamma) ^ {2}} \left[ \frac {(n - 2) (n - 1)}{n ^ {2}} + \left(\frac {2 (n - \gamma)}{n (2 n - \gamma)}\right) ^ {2} \right] - \frac {2 \gamma}{(4 - \gamma)} \frac {2 (n - \gamma)}{(2 n - \gamma) n} \frac {2}{(2 n - \gamma) ^ {2}} = \frac {8 (n - \gamma)}{(4 - \gamma) ^ {2} (2 n - \gamma) ^ {3} n ^ {2}} \left[ \frac {(n - 2) (n - 1) (2 n - \gamma) ^ {3}}{2 (n - \gamma)} + 2 (n - \gamma) (2 n - \gamma) - (4 - \gamma) n \gamma \right]
$$

Note that the term in the above square bracket is greater than $( 2 n - \gamma ) ^ { 2 } + 2 ( n - \gamma ) ( 2 n - \gamma ) - ( 4 - \gamma ) n \gamma = 8 n ^ { 2 } - 1 4 n \gamma + 3 \gamma ^ { 2 } + n \gamma ^ { 2 }$ , which is positive. Therefore, the above first-order derivative is positive, and the maximum gain is increasing in γ.

## A.9 Proof of Proposition 4

Proof. Part (a) can be found to be true from the discussion in the body.

(b) We first derive advertiser i’s payoff under behavioral targeting:

$$
\int_ {0} ^ {x _ {i}} \left[ z _ {i} (1 - \gamma x) - z _ {i + 1} \left(1 - \frac {\gamma}{n} + \gamma x\right) \right] d x + \int_ {0} ^ {\frac {1}{n} - x _ {i - 1}} \left[ z _ {i} (1 - \gamma x) - z _ {i - 1} \left(1 - \frac {\gamma}{n} + \gamma x\right) \right] d x - \Delta_ {i}
$$

$$
= \left[ z _ {i} - z _ {i + 1} \left(1 - \frac {\gamma}{n}\right) \right] x _ {i} - \frac {\gamma}{2} \left(z _ {i} + z _ {i + 1}\right) x _ {i} ^ {2} + \left[ z _ {i} - z _ {i - 1} \left(1 - \frac {\gamma}{n}\right) \right] \left(\frac {1}{n} - x _ {i - 1}\right) - \frac {\gamma}{2} \left(z _ {i} + z _ {i - 1}\right) \left(\frac {1}{n} - x _ {i - 1}\right) ^ {2} - \Delta_ {i}\tag{19}
$$

$$
= \frac {1}{2} x _ {i} \left[ z _ {i} - z _ {i + 1} \left(1 - \frac {\gamma}{n}\right) \right] + \frac {1}{2} \left(\frac {1}{n} - x _ {i - 1}\right) \left[ z _ {i} - z _ {i - 1} \left(1 - \frac {\gamma}{n}\right) \right] - \Delta_ {i}
$$

where the first integral is the expected value net the base payment for the users in segment i | (i + 1), the second integral is the expected value net the base payment for the users in segment $\left( i - 1 \right) \mid i , \Delta _ { i }$ is the cross-border effect, and the last equality is because

$$
\gamma (z _ {i} + z _ {i + 1}) x _ {i} = z _ {i} - z _ {i + 1} \left(1 - \frac {\gamma}{n}\right)
$$

$$
\gamma (z _ {i} + z _ {i - 1}) \left(\frac {1}{n} - x _ {i - 1}\right) = z _ {i} - z _ {i - 1} \left(1 - \frac {\gamma}{n}\right)
$$

from Equation (6).

(b.1) When $n = 2 .$ , the difference in the payoff under behavioral targeting and under traditional advertising is

$$
\frac {\left[ z _ {1} - z _ {2} \left(1 - \frac {\gamma}{2}\right) \right] ^ {2}}{\gamma \left(z _ {1} + z _ {2}\right)} - \left(z _ {1} - z _ {2}\right) \left(1 - \frac {\gamma}{4}\right) = \frac {1}{\gamma \left(z _ {1} + z _ {2}\right)} \left[ \left(1 - \frac {\gamma}{2}\right) ^ {2} z _ {1} ^ {2} - 2 \left(1 - \frac {\gamma}{2}\right) z _ {1} z _ {2} + z _ {2} ^ {2} \right] = \frac {1}{\gamma \left(z _ {1} + z _ {2}\right)} \left[ \left(1 - \frac {\gamma}{2}\right) z _ {1} - z _ {2} \right] ^ {2} \geq 0
$$

where the first term (the advertiser’s payoff under behavioral targeting) is from Equation (19) (noticing $\Delta _ { \mathrm { 1 } } = 0 )$

(b.2) Advertiser 1’s payoff under behavioral targeting can be formulated by letting i = 1 in Equation (19), and the payoff under traditional advertising is $( z _ { 1 } - z _ { ( 2 ) } ) \bigg ( 1 - \frac { \gamma } { 4 } \bigg )$ by Equation (4). The condition for advertiser 1 to be better off under behavioral targeting specified in the proposition then follows.

## A.10 Proof of Corollary 4

Proof. The difference in the payoff under behavioral targeting and under traditional advertising is

$$
\Delta \left(z _ {1}\right) = \frac {\left[ z _ {1} - \left(1 - \frac {\gamma}{n}\right) \right] ^ {2}}{\gamma \left(z _ {1} + 1\right)} - \left(z _ {1} - 1\right) \left(1 - \frac {\gamma}{4}\right) = \frac {1}{\gamma \left(z _ {1} + 1\right)} \left[ \left(1 - \frac {\gamma}{2}\right) ^ {2} z _ {1} ^ {2} - 2 \left(1 - \frac {\gamma}{n}\right) z _ {1} + \left(1 - \frac {\gamma}{n}\right) ^ {2} + \gamma \left(1 - \frac {\gamma}{4}\right) \right]
$$

$\Delta ( z _ { 1 } ) = 0$ has two roots:

$$
z _ {1} ^ {\prime} = \frac {\left(1 - \frac {\gamma}{n}\right) - \sqrt {\gamma \left(1 - \frac {\gamma}{4}\right) \left[ \left(1 - \frac {\gamma}{n}\right) ^ {2} - \left(1 - \frac {\gamma}{2}\right) ^ {2} \right]}}{\left(1 - \frac {\gamma}{2}\right) ^ {2}} \text {and} z _ {1} ^ {"} = \frac {\left(1 - \frac {\gamma}{n}\right) + \sqrt {\gamma \left(1 - \frac {\gamma}{4}\right) \left[ \left(1 - \frac {\gamma}{n}\right) ^ {2} - \left(1 - \frac {\gamma}{2}\right) ^ {2} \right]}}{\left(1 - \frac {\gamma}{2}\right) ^ {2}}
$$

with $z _ { 1 } ^ { ' } < z _ { 1 } ^ { ' } .$ . Notice that $\Delta ( 1 ) > 0$ because when $z _ { \mathrm { 1 } } = 1$ the advertiser’s payoff under behavioral targeting is positive and his payoff under traditional advertising is zero. Furthermore, because $z _ { 1 } ^ { ' } + z _ { 1 } ^ { " } = 2 \biggl ( 1 - \frac { \gamma } { n } \biggr ) \Biggl / \biggl ( 1 - \frac { \gamma } { 2 } \biggr ) ^ { 2 } > 2$ , we have $z _ { 1 } ^ { ' } { > } 1$ . Under the comparable value assumption, $z _ { 1 } \leq 1 { \bigg / } { \bigg ( } 1 - { \frac { \gamma } { n } } { \bigg ) }$ . Because $1 \bigg / \bigg ( 1 - \frac { \gamma } { n } \bigg ) < \bigg ( 1 - \frac { \gamma } { n } \bigg ) \bigg / \bigg ( 1 - \frac { \gamma } { 2 } \bigg ) ^ { 2 } < z _ { 1 } ^ { * }$ , it follows that $z _ { 1 } < z _ { 1 } ^ { ' } .$ . Therefore, if $z _ { 1 } < z _ { 1 } ^ { ' } , \Delta ( z _ { 1 } ) > 0$ and thus the advertiser is better off under behavioral targeting; otherwise, it is worse off. Notice that $z _ { 1 } \in \left[ 1 , 1 \middle / \left( 1 - \frac { \gamma } { n } \right) \right] . ~ z _ { 1 } < z _ { 1 } ^ { ' }$ can occur because $z _ { 1 } ^ { ' } > 1 . \ z _ { 1 } > z _ { 1 } ^ { ' }$ can occur because

$$
\frac {1}{1 - \frac {\gamma}{n}} - z _ {1} ^ {\prime} = \frac {1}{\left(1 - \frac {\gamma}{n}\right) \left(1 - \frac {\gamma}{2}\right) ^ {2}} \left[ \left(1 - \frac {\gamma}{2}\right) ^ {2} - \left(1 - \frac {\gamma}{n}\right) ^ {2} + \left(1 - \frac {\gamma}{n}\right) \sqrt {\gamma \left(1 - \frac {\gamma}{4}\right) \left[ \left(1 - \frac {\gamma}{n}\right) ^ {2} - \left(1 - \frac {\gamma}{2}\right) ^ {2} \right]} \right]
$$

$$
= \frac {\sqrt {\left(1 - \frac {\gamma}{n}\right) ^ {2} - \left(1 - \frac {\gamma}{2}\right) ^ {2}}}{\left(1 - \frac {\gamma}{n}\right) \left(1 - \frac {\gamma}{2}\right) ^ {2}} \left[ \left(1 - \frac {\gamma}{n}\right) \sqrt {\gamma \left(1 - \frac {\gamma}{4}\right)} - \sqrt {\left(1 - \frac {\gamma}{n}\right) ^ {2} - \left(1 - \frac {\gamma}{2}\right) ^ {2}} \right] = \frac {\sqrt {\left(1 - \frac {\gamma}{n}\right) ^ {2} - \left(1 - \frac {\gamma}{2}\right) ^ {2}}}{\left(1 - \frac {\gamma}{n}\right) \left(1 - \frac {\gamma}{2}\right) ^ {2}} \frac {\left(1 - \frac {\gamma}{2}\right) ^ {2} \left[ 1 - \left(1 - \frac {\gamma}{n}\right) ^ {2} \right]}{\left(1 - \frac {\gamma}{n}\right) \sqrt {\gamma \left(1 - \frac {\gamma}{4}\right)} + \sqrt {\left(1 - \frac {\gamma}{n}\right) ^ {2} - \left(1 - \frac {\gamma}{2}\right) ^ {2}}} > 0
$$

## A.11 Proof of Proposition 5

Proof. We assume that advertiser 1 is the dominant advertiser. The joint payoff of the publisher and the advertisers under traditional advertising can be formulated as $2 z _ { 1 } \int _ { 0 } ^ { \frac { 1 } { 2 } } ( 1 - \varkappa ) d x$ . The joint payoff under behavioral targeting is $\begin{array} { r } { \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { x _ { i } } z _ { i } ( 1 - \varkappa ) d x + \int _ { 0 } ^ { \frac { 1 } { n } - x _ { i - 1 } } z _ { i } ( 1 - \varkappa ) d x } \end{array}$ For any user j in segment $i \mid ( i + 1 ) , { \mathrm { i f } } x _ { i j } \in [ 0 , x _ { i } ]$ , by Lemma 2 and the definition of $\cdot _ { x _ { i } , }$ advertiser i wins the user and derives the highest value among all advertisers, which implies

$$
z _ {i} \left(1 - \gamma x _ {i j}\right) > z _ {1} \left(1 - \gamma x _ {1 j}\right)
$$

The left-hand side of the inequality is also use $\mathrm { ~  ~ \cdot ~ } j ^ { \mathrm { ~ \tiny ~ s ~ } }$ contribution to the joint payoff under behavioral targeting, and the right-hand side is her contribution to the joint payoff under traditional advertising. Therefore, the joint payoff derived from user j is higher under behavioral targeting than under traditional advertising. The same argument applies if $x _ { i j } \in [ x _ { i } , 1 / n ]$ (such that advertiser i + 1 wins the user and derives the highest value). Because the joint payoff is the sum of the joint payoff from each user, the joint payoff under behavioral targeting is greater than the joint payoff under traditional advertising

## A.12 Maximum Gain in the General Case

Proof. Without loss of generality, we let $z _ { 1 } = z _ { ( 1 ) }$ and normalize $z _ { ( 2 ) } = 1$ . By Lemma $3 , \pi _ { B }$ is maximized when $z _ { ( 2 ) } = z _ { ( 3 ) } = \ l _ { \cdot \cdot } = z _ { ( n ) }$ and when $z _ { ( 1 ) }$ is large enough to win all of the users. For each of the two segments with one end at $z _ { ( 1 ) } ~ ( \mathrm { i . e . }$ , segments $n \mid 1$ and $1 \mid 2 )$ , the expected revenue is the lower-value advertiser’s expected value of all the users in the segment, which is ${ \frac { 1 } { n } } { \left( 1 - { \frac { \gamma } { 2 n } } \right) }$ . For each of the other $n - 2$ segments (e.g., $i | i + 1 )$ , the expected revenue is advertiser $i ^ { \circ } \mathrm { s }$ expected value of the half of the users who are closer to him than to advertiser $i + 1$ and advertiser $i + 1 \gamma _ { \mathrm { s } }$ expected value of the other half, which is ${ \frac { 1 } { n } } { \left( 1 - { \frac { \gamma } { 4 n } } \right) }$ . We can thus obtain the maximum and calculate the maximum $\pi _ { B }$ gain as

$$
\frac {\pi_ {B}}{\pi_ {T}} - 1 = \frac {\frac {n - 2}{n} \left(1 - \frac {\gamma}{4 n}\right) + \frac {2}{n} \left(1 - \frac {\gamma}{2 n}\right)}{1 - \frac {\gamma}{4}} - 1 = \frac {\frac {\gamma}{4} - \frac {\gamma}{n} \left(\frac {n - 2}{n} \frac {1}{4} + \frac {1}{n}\right)}{1 - \frac {\gamma}{4}} = \frac {\gamma \left(1 - \frac {n + 2}{n ^ {2}}\right)}{4 - \gamma} = \frac {\gamma}{4 - \gamma} \frac {(n - 2) (n + 1)}{n ^ {2}}
$$

The maximum gain is clearly increasing in γ. The gain is also increasing in n because its first-order derivative with respect to n is positive; that is, ${ \frac { \gamma } { 4 - \gamma } } \left( { \frac { 1 } { n ^ { 2 } } } + { \frac { 4 } { n ^ { 3 } } } \right) > 0$
