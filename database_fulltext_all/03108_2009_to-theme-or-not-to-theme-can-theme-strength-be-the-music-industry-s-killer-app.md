---
otero_id: 3108
otero_key: "D6UQB6GN"
title: "To theme or not to theme: Can theme strength be the music industry's “killer app”?"
authors: "Sudip Bhattacharjee; Ram Gopal; James R. Marsden; Ramesh Sankaranarayanan; Rahul Telang"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.07.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# To theme or not to theme: Can theme strength be the music industry's “killer app”?

Sudip Bhattacharjee <sup>a</sup>, Ram Gopal <sup>a,</sup>⁎, James R. Marsden <sup>a</sup>, Ramesh Sankaranarayanan <sup>a</sup>, Rahul Telang <sup>b</sup>

<sup>a</sup> University of Connecticut, United States

<sup>b</sup> Carnegie Mellon University, United States

## a r t i c l e i n f o

Article history: Received 26 September 2008 Received in revised form 29 May 2009 Accepted 7 July 2009 Available online 21 July 2009

Keywords: Digital music Bundling Piracy Sampling

## a b s t r a c t

Music bundling has been the mainstay of the music industry for decades. Record companies and producers have selected bundles of songs and sold them as albums, their most important revenue source. Digitization and piracy of music have threatened this standard business model with consumers increasingly purchasing music a la carte. In this study, we analyze a strategy for designing successful albums through using new concepts of themed bundling. Thematic bundling can lower consumer search costs and dampen the incentive to pirate music, and can potentially be a win–win strategy for both consumers and music companies. Unlike prior work in economics on bundling which typically seeks to determine the optimal price, bundle size and composition, we focus on a restricted bundling problem, since the price of the bundled product (i.e. an album) is generally set over a narrow range as is the number of items (i.e. songs) in the bundle. Our key results and insights are derived using analytic modeling and extended through numerical analysis. In addition, our key <sup>fi</sup>ndings are supported by our empirical analysis of music album chart performance.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

The album is dead! Long live the album! For centuries it was the town crier who <sup>fi</sup>rst announced the death of the king and then proclaimed best wishes for the heir, the new king. In the music world, the album has long been the king, the major industry product. Album sales were the “measure of success” and artists were judged by the market performance of their albums, especially their most recent album.

But then came the rapid emergence of technology that provided the means for a new world of music. Consumers were freed from the shackles of albums, of music compilations forced upon them by the record companies. Individuals could now purchase sets of individual songs that they personally select. In July of 2007, the Wall Street Journal reported (July 5th, 2007) that while the 229.8 million albums sold in the <sup>fi</sup>rst six months of 2007 represented a decrease of 15% over the same period in the previous year, individual digital track sales increased 49% to 417.3 million over the same period. Now surely the king was dead, and the individual song would be the new king! But is it the album that is dying or are different subsets of albums actually doing well and thriving? Is the album dying a slow death or could it be that, like many royal survivors of yore, there are successful forms of the album genre that have already or could quietly morph to assimilate and thrive in the new environment? Here we investigate whether theme strength (as de<sup>fi</sup>ned in detail below) can be the basis for a successful album bundling strategy.

Today's music albums are bundles of digital goods. In the material that follows, we analyze the digital good bundling problem and address the following question: is it possible that major differences between successful album sets and unsuccessful album sets are linked to decision making in the bundling of digital goods? We develop formal models for the special digital good case of music. As we explain below, the bundling problem for digital goods is actually a very different problem from the bundling problem economists have studied extensively. In particular, we focus on a restricted bundling problem, since the price of the bundled product (i.e. an album) is generally set over a narrow range as is the number of items (i.e. songs) in the bundle. In the more general bundling literature, (see especially Geng et al. [10]), the models seek to determine the optimal price, bundle size and composition.

## 1.1. Experience goods and the need for pre-purchase search and sampling

Nelson [14] classi<sup>fi</sup>ed goods into search goods and experience goods. Consumers can evaluate a search good prior to purchase by evaluating observable characteristics of the good together with the price of the good. An experience good, on the other hand, can only be evaluated through consumption or use. To accomplish this prior to purchase, consumers must be able to search and identify contending products and must have a sampling process available to them. Thus, consumers' search and sampling “experience” can both be important components of a consumer's individual estimation of his value for an experience good [17].

For many tangible experience goods, such as a brand of tuna, a consumer may need to sample and experience only once. If there is brand consistency for the product, the consumer can expect the taste from subsequent purchases of the brand to remain consistent. However, for experience goods such as music, movies, video games, software, or <sup>fi</sup>ction books there can be high variability in quality (see Bhattacharjee et al. [2]) even across what might seem to be a “brand”. That is, a speci<sup>fi</sup>c director's <sup>fi</sup>lms often vary greatly as do the video games of a production team or the albums of a musical artist or the books of a <sup>fi</sup>ction mystery writer. Liking one of the products in a product grouping (e.g., <sup>fi</sup>lms by a speci<sup>fi</sup>c director or books by a speci<sup>fi</sup>c author) does not guarantee a favorable view of another product in that product grouping. That is, the elements of speci<sup>fi</sup>c product groupings do not rise to the level of a “brand”. To make good choices, consumers must repeatedly search and sample for new offerings within a product grouping of interest to them. Further, the number of products of potential interest may be very large, presenting an imposing consumer search and sampling problem. Consider, for example, a consumer interested in folk music or mystery novels. How large are the sets that the consumer would need to search and sample in order to realize a high probability of a successful purchase?

Sellers are keenly aware of the bene<sup>fi</sup>t from offering consumers the ability to sample part of an experience good during the purchase decision process. Movie releases have long been preceded by trailers or “coming attraction” promos providing clips (samples) from the <sup>fi</sup>lm. Software vendors often provide restricted edition access or limited 30-day free trials. Brick-and-mortar music retailers have provided various facilities for consumers to sample songs in-store before buying. Online music retailers provide a variety of brief or “partial song” sampling options. The Financial Times (website) now provides free access to the <sup>fi</sup>rst two paragraphs of all news articles, requiring readers to subscribe for access to the rest of the article.

## 1.2. The special case of music

A key characteristic of music purchases is “purchase hazard” since music once purchased cannot be “returned” easily. For many physical experience goods, including clothes, returns are possible. In those cases, consumers have the safety net of getting their money back and thus avoiding loss, though this characteristic may lead to higher prices for such goods. Returns of music have been a bit trickier. Even when music is distributed on CD-ROM or other physical media, most retail stores allow exchanges but not returns of music CDs where the cellophane wrapping has been “breached”. In the case of digitally downloaded songs, the only way for a consumer to “return” a song would be to destroy the copy, which is not very reliable from the seller's viewpoint. Thus, for music, the avoidance of purchase errors is important since consumers cannot rectify such mistakes by returning the goods. Effective search and sampling can provide the means for consumers to make better purchase decisions.

The music recording industry has long played an active, or perhaps better termed a “pro-active” role in music sampling through payola, where payments of undisclosed sums are made to broadcast speci<sup>fi</sup>c songs over radio or television. Coase [8] saw payola as a pricing system, where the service of broadcasting a record by a radio station increased the value of the record. That is, the act of broadcasting attracts a price (payola) which is a means of allocating a scarce resource (broadcast time). Payola can be viewed as a “forced” passive sampling mechanism that focuses sampling on a restricted music set. Though payola was banned by the FCC (Federal Communications Commission) in 1960, the practice continues today [9]. There is some evidence that P2P sharing networks are providing some of the bene<sup>fi</sup>ts of payola by helping customers sample songs before buying [4]. Coase argued that, while the reason for banning payola was to minimize “deception” of consumers, the ban had unintended consequences including less competition among record companies (higher product prices), and additional monitoring expenses by regulators.

For music, the advent of the Internet included the emergence of technologies and channels that facilitated sampling at new levels.

Peer-to-peer <sup>fi</sup>le sharing technologies (Napster, Gnutella, KaZaA, etc.) led to widespread downloaded music <sup>fi</sup>les for either retention (piracy) or sampling (as discussed in [2] and [4]). Online retailers such Amazon.com provide various digital downloadable samples of songs. Websites that have emerged for the purpose of promoting speci<sup>fi</sup>c artists, groups of artists, or a generic class of “lesser-known artists” provide downloadable samples ranging from partial song clips to entire singles.

When digital products are available for downloading, both a substitution effect (retention of downloaded copy in substitution for purchase of the digital good) and a sampling effect (pre-purchase sampling tending to enhance sales of the digital good) can arise (see Gopal et al. [11]). For the case of music, Bhattacharjee et al. [3] <sup>fi</sup>nd: (i) peer-to-peer sharing of music <sup>fi</sup>les results in pre-purchase sampling as well as piracy-related lost sales, and (ii) sharing activity provides a lead indicator to album performance on BillBoard charts. Chellappa and Shivendu [7] suggest that when the quality of a digital good is under-estimated, the sampling effect can actually dominate and help sales.

## 1.3. Bundling in the digital goods marketplace

The emergence of digital goods has opened an expanse of possibilities for bundling. Digital goods can be easily bundled across sellers (e.g., record labels) and good categories. Consider the possible bundling of digital goods for use in an iPhone!

The enormity of the digital goods space and the possibility set for bundling pose daunting problems for those seeking to identify optimal bundling strategies or optimal pricing strategies (the focus of much of economists' research on bundling). But can we identify bundling issues that we can analyze and from which we can gain important insights? In the case of the restricted bundling problem for digital music, we argue that this is indeed the case.

Music has a long history of being sold in bundles or “albums”. Albums do tend to have some linking theme or characteristic – that is, the songs in the album are typically by the same artist, belong to the same genre, and were produced in a given year or time period. But some music albums (such as “compilation albums”<sup>1</sup>) have stronger themes. It is such stronger themes that draw our focus here.

Because they possess a strong theme, we expect greater similarity among the songs in a compilation album than we would see on normal albums. Such similarity, in turn, can impact consumers' sampling behavior. If an individual likes one song in a compilation album, there is an increased likelihood (compared to the same occurrence in a regular album), that the individual will like the other songs in the compilation (See for example the recent study by Borreau et al. [6] which analyzes complementarity issues in the current digital music marketplace). Prior research has emphasized the importance of matching customized information goods to consumers' preferences (e.g. [15]). In our work, we suggest that theme strength can serve as a proxy for consumers' preferences.

While record companies/producers have driven such “compilation albums” (today's most prominent form of themed music bundles), other themed bundles are emerging in today's digital world. In fact, today's music bundles can be vendor-sponsored, independent serviceagent sponsored, or user-driven. There are numerous examples of vendor-sponsored themed bundles in music, including albums of songs recorded at multi-artist events (e.g., “Woodstock: Three Days of Peace & Music”), Christmas albums, or albums featuring a one-time collaboration of two artists (Bruce Hornsby and Ricky Skaggs or Nat King Cole and Natalie Cole), and themed collections of various artists (“Various Artists – Anthony Rother Presents We Are Punks”, “Various Artists – 5 Years of Get Physical”). An interesting example of vendorsponsored, individual sponsored, and service-agent sponsored themed bundles can be found in Apple iTunes' Playlists feature. The iTunes' Playlists are lists of songs that either Apple can compile (vendor-sponsored themed bundles) or users themselves can compile (user-driven themed bundles), which are then published on the Apple iTunes website. A wide variety of service-agent playlists are also available, containing recommendations from celebrities, entertainers, and critics. Any user can purchase some or all songs in a playlist. A user-created playlist (also called an iMix) can contain up to 100 songs, is published on the iTunes website for one year, and is searchable by any user. iMixes can be voted by other users using a <sup>fi</sup>ve-star system.

A recent Gartner report [13] detailed the growing popularity of playlists and other consumer taste-sharing applications in online music purchases. In a different context, Ragno et al. [16] analyzed the similarity of a list of songs played together (in one session) by a radio station. The researchers found various groupings that captured similarity among these songs – e.g. membership in the same genre, similar popularity, or suitability to be played together. The researchers used multiple such lists to build an algorithm that inferred similarity among songs and automatically generated similarity-based playlists. Thus there are two differing approaches, one driven by the record company and another by external entities, which currently determine the ex ante theme of the bundle. Here we have not modeled this ex ante decision making process.

A signi<sup>fi</sup>cant bene<sup>fi</sup>t of aggregating songs by theme is the likelihood of lowered search costs for consumers. Given the large and ever-growing collection of music, the recording industry is grappling with the challenge of helping consumers <sup>fi</sup>nd the songs they like (and that they will buy!) in a quick and effective manner. Themed bundles can be one way to do this. Consumers who sample compilations possessing “high thematic strength” might quickly <sup>fi</sup>nd music that <sup>fi</sup>ts their taste, without actually having to sample every individual song from a vast and ever-growing pool. Themed bundles of songs thus can serve the purpose of most recommender systems – to help “tell consumers about music that they might like”.

We approach the development of our formal model in a way quite different from what most economists have done in the long history of research on bundling. The prior stream of work in economics has tended to focus on identifying optimal pricing strategies for bundled goods (see, especially, discussions in Geng et al. [10]). Historically, music albums have fallen within a fairly tight price range and thus we take price as given (i.e., determined for an album). We focus on the issues of theme strength and sampling.

In Section 2, we offer a formal model of a consumer's music sampling and purchase decision process. The results of a simple analytical modeling exercise suggest that as theme strength increases and sampling costs decrease, consumers are more likely to purchase such an album compared to one with lower theme strength, even when the ex ante valuation is identical for the two albums. To the extent that sampling increases the likelihood of purchase, compilation albums possess both a competitive edge on regular albums and may result in less piracy. We substantiate the <sup>fi</sup>ndings of this simple analytical model with numerical analysis of a more complex model in Section 3. In Section 4, we provide initial validation of the model <sup>fi</sup>ndings using empirical evidence. We conclude in Section 5 with a discussion of key insights and managerial implications.

## 2. A simple analytical model

Consider the decision making process of a consumer who is deciding whether to buy an album of songs. The consumer is ex ante uncertain about the true value of the album but may seek information through sampling. To illustrate the key concepts, we <sup>fi</sup>rst formulate and solve a simple analytical model. Consider an “album” consisting of two songs, each of which can be “good” (denoted by “G”) or “bad” (denoted by $\ " { \bf B } ^ { \prime \prime } )$ . Let G1 and G2 denote the events that the <sup>fi</sup>rst and second songs are “good”. Let B1 and B2 denote the events that the <sup>fi</sup>rst and second songs are “bad”. Denote the value of a “good” song as v, the value of a “bad” song as 0, and the album as a whole as V (note that here V can take on only three values: 2v, v, or 0). Since music albums have historically fallen within a fairly tight price range, we take price as given (i.e. exogenously determined for an album). Since the consumer is uncertain about whether she will like the album, she might wish to sample part of the album. When sampling, in some situations the consumer can't gain repeated access to the sampled song, e.g. when sampling in a retail store. In other situations, the consumer can gain repeated access to the song, e.g. when sampling a song downloaded to a personal computer from a P2P sharing network. In this latter case, the consumer can pirate the song or songs downloaded – i.e., keep and use (consume) the song without buying the rest of the album. We <sup>fi</sup>rst consider situations where the consumer can't gain repeated access to the sampled song, a case where the question of piracy does not arise.

Please note that the relevant parameter range is 2vNpNv. Each consumer is assumed to know the value of v and p, but for a given song, she does not know whether the song's value is v or 0, and so she has to sample. When 2vbp, the price of the album is greater than the value the consumer obtains from it, even if the consumer <sup>fi</sup>nds after sampling that she likes both songs. Therefore, the consumer just avoids sampling this album (because sampling has a cost c), and so this case is not interesting for our purpose. On the other hand, vNp is not a realistic assumption, as this implies that any one song is of higher value than the price of both songs. (In an n-song album of value V, this implies that the price P is less than (1/n)th of V, which is implausible.) Moreover, in our model if a consumer samples a song and <sup>fi</sup>nds it to be good (i.e. of value v), she will buy the album irrespective of the theme strength, because the one song she sampled justi<sup>fi</sup>es the purchase. This will not let us study the role of theme strength. We can study the role of theme strength only in the parameter range where 2vNpNv.

For a particular consumer, who has not yet sampled any song in the album, the <sup>fi</sup>rst song sampled has some probability, r, of being good. Using θ to represent the appropriate probability mass function and the index $" 1 "$ to indicate the <sup>fi</sup>rst song sampled, we have:

$$
\theta (G 1) = r\tag{1}
$$

(Note that r is consumer speci<sup>fi</sup>c, unlike v, and could vary across individuals based upon their preferences for music. Here we model one individual and, for simplicity, use r instead of $r _ { i \cdot } )$ ).

Given that the <sup>fi</sup>rst song is good, the probability that the second song is good is:

$$
\theta (G 2 | G 1) = r + (1 - r) t\tag{2}
$$

where t $( 0 \leq t \leq 1 )$ is the theme strength for the album. If the theme strength is 0, then the second song is good with probability r, that is, there is no interdependence or similarity across the songs. If there is no underlying theme for the album, the consumer liking one song indicates nothing about whether the consumer will or will not like the other song. If theme strength is 1, then the conditional probability that the other song is good is 1, that is, if the consumer likes one song, he/ she is sure to like the second one.

We summarize the relevant probabilities in the following Table 1: If the consumer buys without sampling, the net expected value from the album. $E _ { \mathrm { N S } } ( V )$ , is:

$$
\begin{array}{c} E _ {\mathrm{NS}} (V) = (2 v) [ \theta (G 2, G 1) ] + (v) [ \theta (B 2, G 1) + \theta (G 2, B 1) ] \\ + (0) [ \theta (B 2, B 1) ] - p \end{array}\tag{3}
$$

Table 1 Probabilities of purchase.

<table><tr><td>θ(G1)</td><td>r</td></tr><tr><td>θ(B1)</td><td>1-r</td></tr><tr><td>θ(G2|G1)</td><td>r+(1-r)t</td></tr><tr><td>θ(B2|G1)</td><td>(1-r)(1-t)</td></tr><tr><td>θ(G2|B1)</td><td>r(1-t)</td></tr><tr><td>θ(B2|B1)</td><td>(1-r)+rt</td></tr></table>

where $p$ denotes the price of the album, and $\theta ( G 2 , G 1 )$ denotes the probability that both songs are good. Substituting values from Table 1 and simplifying, we have:

$$
E _ {\mathrm{NS}} (V) = 2 r v - p\tag{4}
$$

Note that the net expected value to a consumer who does not sample is independent of the theme strength t.

Consider the situation where the consumer samples one song before deciding to purchase the album. Denoting the sampling cost by c, the net expected “sample once” value of the album, $E _ { S } ( V )$ , is:

$$
E _ {S} (V) = \theta (G 1) \cdot [ v + [ \theta (G 2 | G 1) (v) + \theta (B 2 | G 1) (0) ] - p ] - c\tag{5}
$$

Eq. (5) simpli<sup>fi</sup>es to<sup>2</sup>:

$$
E _ {S} (V) = r [ v + (r + (1 - r) t) v - p ] - c\tag{6}
$$

Hence, when sampling one song is permitted, the consumer's decision alternatives become “sample a song in the album and then make a purchase/no purchase decision” or “buy the album without sampling”. $E _ { S } ( V )$ captures the expected value to the consumer deciding to sample the album. Comparing this value (Eq. (6)) to the expected value to the consumer from the album with no sampling (Eq. (4)) yields the incremental value from sampling the album.

Now, consider the expected value to a consumer from sampling both songs, which is given by $E _ { S S } ( V )$

$$
E _ {\mathrm{SS}} (V) = \theta (G 1, G 2) (2 v - p) - 2 c\tag{7}
$$

Comparing this value (Eq. (7)) to the expected value to the consumer from sampling just one song (Eq. (6)) yields the incremental value from sampling the second song (details of this analysis are provided in Appendix A, Section (A.1)).

The following result holds:

Result 1. Ceteris paribus, as theme strength increases, consumers <sup>fi</sup>nd it more attractive to sample an album, i.e. $\begin{array} { r } { , \frac { \partial E _ { \mathrm { S } } ( V ) } { \partial t } - \frac { \partial E _ { \mathrm { N S } } ( V ) } { \partial t } > 0 } \end{array}$ . However, they sample a lesser proportion of the album, i.e. $\frac { \partial E _ { \mathrm { S S } } ( V ) } { \partial t } - \frac { \partial E _ { \mathrm { S } } ( V ) } { \partial t } > 0$

## 2.1. Impact of piracy

Suppose the situation is such that the consumer can gain repeated access to the songs sampled opening the possibility of piracy. We <sup>fi</sup>rst examine whether consumers are more or less inclined to pirate an album as theme strength increases. To do so, we introduce the possibility that the consumer, after sampling one song, can pirate it (continue to use or consume that one song without paying for it and without purchasing the album). As previous authors have argued (see Bhattacharjee et al. [2], [1] and Gopal et al. [11]), the pirated music tends to have a “degraded utility” which can be represented using a weight, δ, where 0bδb1. Thus the value of a pirated version of an original song with value v is degraded to a value δv. The consumer who <sup>fi</sup>nds the <sup>fi</sup>rst song to be good now compares the value from buying the album: $\nu + \theta ( G 2 | G 1 ) ( \nu ) - p$ to the value from pirating the <sup>fi</sup>rst song, δv.

Since $\theta ( G 2 | G 1 ) \nu = ( \boldsymbol { \mathrm { r } } + ( 1 - r ) t ) \nu ,$ the consumer buys the album if:

$$
v + (r + (1 - r) t) v - p > \delta v\tag{8}
$$

and pirates otherwise.

Let $\Delta E _ { \mathrm { B P } }$ be the incremental expected value of buying over pirating, after a consumer samples a song. From Eq. (8) above, we have

$$
\Delta E _ {\mathrm{BP}} = v + (r + (1 - r) t) (v) - p - \delta v\tag{9}
$$

where $\begin{array} { r } { \frac { \partial \Delta E _ { \mathrm { B P } } } { \partial t } = \nu ( 1 - r ) > 0 ; a n d \frac { \partial \Delta E _ { \mathrm { B P } } } { \partial v } = ( 1 - \delta ) + [ r + ( 1 - r ) t ] > 0 . } \end{array}$

From the above expressions, we establish our second result:

Result 2. A consumer's expected value of buying over pirating increases with the theme strength (i.e. $\frac { \partial \Delta E _ { \mathrm { B P } } } { \partial t } > 0 )$ and with the value of album $( \mathrm { i . e . } \frac { \partial \Delta E _ { \mathrm { B P } } } { \partial \nu } > 0 )$ .

Further, it can be seen that

$$
\frac {\partial^ {2} (\Delta E _ {\mathrm{BP}})}{\partial v \partial t} = (1 - r) > 0\tag{10}
$$

which leads to the following third result:

Result 3. The effect of theme strength on a consumer's expected value of buying over pirating is accentuated by the album value (i.e. $\frac { \partial ^ { 2 } ( \Delta E _ { \mathrm { B P } } ) } { \partial \nu \partial t } { > } 0 )$

We now consider how piracy affects the extent to which consumers will sample albums of stronger theme strength. Building upon Result 1 above, we derive the incremental expected value to a consumer from sampling both songs over sampling just one song, in the presence of piracy (for brevity in explication, details of the analysis are available in Appendix A, Section (A.2).) The analysis yields our fourth result:

Result 4. Even in the presence of piracy, the proportion of the album sampled is inversely related to the theme strength, $\begin{array} { r } { \mathrm { i . e . , } \frac { \partial E _ { S S } ( V ) } { \partial t } - \frac { \partial E _ { S } ( V ) } { \partial t } > 0 . } \end{array}$

This is a signi<sup>fi</sup>cant and rather counter-intuitive result. Intuitively one would expect that if a consumer can pirate, they will prefer to download more songs in any album. We <sup>fi</sup>nd that this effect is muted by the theme strength of an album, so that albums with stronger themes will witness less downloading. The insight here is that if an album has a strong theme, and if consumers like a few sampled songs in the album, they will prefer to buy the entire album rather than just pirating what they have sampled.

## 3. A more general model

We now formulate a more general model. Given model complexity, we analyze the model implications and results using an exhaustive numerical analysis of the parameter space. In this model, the amount of the album a consumer samples is endogenously determined. For a given album, j, the value is denoted by $V _ { j \ast }$ We assume that the likelihood that a consumer i will like this album is drawn from a beta distribution whose parameters are $\alpha _ { i j }$ an ${ . \beta _ { i j } }$ . We use the beta distribution to describe the likelihood that a consumer will like an album. As the consumer learns more about his true preference (likeability) for an album, the $\alpha _ { i j }$ and $\beta _ { i j }$ can be updated to re<sup>fl</sup>ect this information (that is, the new value distribution for album j for consumer i would incorporate the updated $\alpha _ { i j }$ and $\beta _ { i j } )$ . The resulting distribution would change suitably. The album theme strength t impacts the values of $\alpha _ { i j }$ and $\beta _ { i j } .$ as t increases, both $\alpha _ { i j }$ and $\beta _ { i j }$ decrease. Ceteris paribus, the ex ante probability of a “good” sample outcome, $r _ { i } ,$ also impacts the values of $\alpha _ { i j }$ and $\beta _ { i j } .$ as r increases, $\alpha _ { i j }$ increases but $\beta _ { i j }$ decreases. The relationships can be represented as follows:

$$
\alpha_ {i j} = 2 r _ {i} (1 - t _ {j}) \quad \mathrm{and} \quad \beta_ {i j} = 2 (1 - r _ {i}) (1 - t _ {j})\tag{11}
$$

and thus $\frac { \alpha _ { i j } } { \alpha _ { i j } + \beta _ { i j } } = r _ { i }$

The net expected value of album j for consumer i, ex ante (pre-sampling) is given by:

$$
E _ {\mathrm{NS}} [ V _ {i j} ] = \left(\frac {\alpha_ {i j}}{\alpha_ {i j} + \beta_ {i j}}\right) V _ {j} - p = r _ {i} V _ {j} - p\tag{12}
$$

But for most albums, a consumer is likely to have heard or read at least something about that album – perhaps from friends, radio, TV, magazines, or online. Moreover, the album is likely to have a certain theme strength. Based on this information, the consumer would form a prior distribution of the quality of this album given his personal tastes. The more reliable (in the consumer's view) the source of information, the more compact (lower variance) this prior distribution would be. This “quality” that we refer to is subjective in nature – two different consumers could react to the same song or same information in a completely different manner. As discussed above, we capture this prior distribution of quality through the values of $\alpha _ { i j } = 2 r _ { i } ( 1 - t _ { j } )$ and $\beta _ { i j } { = } 2 ( 1 - r _ { i } ) ( 1 - t _ { j } )$

In general, a consumer may remain uncertain about whether he she likes the album and may wish to sample a fraction k of the album before buying. Of the sampled part, the consumer may like only a fraction, w. Therefore the consumer realizes a value from sampling of $w k V _ { j } .$ . The consumer's updated posterior probability distribution of the value outcomes for the unsampled part of the album is a beta distribution with updated parameter values $\alpha _ { i j } ^ { 1 }$ and β<sub>ij</sub><sup>1</sup> given by:

$$
\alpha_ {i j} ^ {1} = \frac {w k}{(1 - k)} + 2 r _ {i} (1 - t _ {j})\tag{13}
$$

$$
\beta_ {i j} ^ {1} = \frac {(1 - w) k}{(1 - k)} + 2 (1 - r _ {i}) (1 - t _ {j})\tag{14}
$$

Note that $\alpha _ { i j } ^ { 1 }$ increases with w and $\beta _ { i j } ^ { 1 }$ increases with $( 1 - w )$ . As $k \to 1 , \alpha _ { i j } ^ { 1 } \to \infty$ and $\beta _ { i j } ^ { 1 }  \infty .$ As k approaches 1, the consumer samples the entire album, and the quality uncertainty (or variance in the posterior distribution) should approach 0.

## 3.1. The expected value of the album

To summarize, when consumer i samples a fraction k of an album and determines that fraction w of the sample is good:

(i) the utility of the sampled part is wkV ; and, (ii) the expected utility of the remaining (non-sampled) group of songs is:

$$
\frac {\alpha_ {i j} ^ {1}}{\alpha_ {i j} ^ {1} + \beta_ {i j} ^ {1}} (1 - k) V _ {j}\tag{15}
$$

Substituting from above, Eq. (15) can be represented in terms of r and t<sub>j</sub>:

$$
\left(\frac {\frac {w k}{(1 - k)} + 2 r _ {i} (1 - t _ {j})}{\frac {w k}{(1 - k)} + 2 r _ {i} (1 - t _ {j}) + \frac {(1 - w) k}{(1 - k)} + 2 (1 - r _ {i}) (1 - t _ {j})}\right) (1 - k) V _ {j}\tag{16}
$$

Let P be the album price. After sampling fraction k of the album, the net expected utility (net of price paid) from purchasing the album is:

$$
\begin{array}{c} E _ {S} (V _ {i j} | w, k) = w k V _ {j} + \left(\frac {\frac {w k}{(1 - k)} + 2 r _ {i} (1 - t _ {j})}{\frac {w k}{(1 - k)} + 2 r _ {i} (1 - t _ {j}) + \frac {(1 - w) k}{(1 - k)} + 2 (1 - r _ {i}) (1 - t _ {j})}\right) \\ \times (1 - k) V _ {j} - p \end{array}\tag{17}
$$

The consumer purchases only when the observed value of w makes $E _ { S } \left( V _ { i j } | w , k \right)$ positive. Now $E _ { S } \left( V _ { i j } | w , k \right)$ increases in w, which can vary in the interval [0,1] per beta distribution, $f ( w , r , t )$ . If w is observed to be “too low”, the consumer does not purchase the album and realizes a value of zero. At some cutoff value, say $w = w _ { 0 } ,$ the consumer is indifferent between buying and not buying the album. For $w { > } w _ { 0 } ,$ the consumer purchases the album.

But the consumer is likely to incur a cost of sampling. Using a unit cost of sampling, $c ,$ the cost to sample a fraction k is ck and the ex ante overall net expected value of the album with sampling is:

$$
E _ {S} (V _ {i j} | k) = \int_ {w _ {0}} ^ {1} E _ {S} (V _ {i j} | w, k) f (w, r _ {i}, t _ {j}) d w - c k\tag{18}
$$

The beta distribution $f ( w , r , t )$ is given by:

$$
f (w, r _ {i}, t _ {j}) = \frac {w ^ {\eta - 1} (1 - w) ^ {\eta - 1}}{B e t a [ 2 r _ {i} (1 - t _ {j}) , 2 (1 - r _ {i}) (1 - t _ {j}) ]}\tag{19}
$$

Here $B e t a [ 2 r _ { i } ( 1 - t _ { j } ) , 2 ( 1 - r _ { i } ) ( 1 - t _ { j } ) ]$ is the beta function normalization constant that ensures that the beta distribution integrates to unity.

## 3.2. Impact of piracy

In certain sampling settings (e.g. online P2P networks) it may be possible to pirate the sampled songs (that is, save the sampled songs for subsequent consumption, without paying for them). As noted earlier, pirated music tends to have a “degraded quality” which we represent using a weight, δ, where $0 { < } \delta { < } 1$ . Thus, if a fraction, k, of the album is sampled and pirated, of which a fraction, w, is found to be good, then the value of the pirated sample is given by δwkV. To purchase, the user must realize a value $E _ { S } \left( V _ { i j } | w , k \right)$ ) that is at least equal to the value of the pirated version (as opposed to zero earlier). The new cutoff is determined by solving for $w _ { 0 \delta }$ in the following:

$$
\begin{array}{l} w _ {0 \delta} k V _ {j} + \left(\frac {\frac {w _ {0 \delta} k}{(1 - k)} + 2 r _ {i} (1 - t _ {j})}{\frac {w _ {0 \delta} k}{(1 - k)} + 2 r _ {i} (1 - t _ {j}) + \frac {(1 - w _ {0 \delta}) k}{(1 - k)} + 2 (1 - r _ {i}) (1 - t _ {j})}\right) \\ \times (1 - k) V _ {j} - p = \delta w _ {0 \delta} k V _ {j} \end{array}\tag{20}
$$

For values of wN $w _ { 0 \delta } ,$ the consumer prefers buying the album. For values $w { < } w _ { 0 \delta }$ , the consumer prefers to pirate what he/she has sampled. Given a sample of size k, the overall net expected value of the album is now

$$
E _ {S} (V _ {i j} | k) = \int_ {0} ^ {w _ {0 \delta}} (\delta w k V _ {j}) f (w, r _ {i}, t _ {j}) d w + \int_ {w _ {0 \delta}} ^ {1} E _ {S} (V _ {j} | w, k) f (w, r _ {i}, t _ {j}) d w - c k\tag{21}
$$

Here, as for Eq. (15) above, the beta distribution $f ( w , r _ { i } , t _ { j } )$ is given by:

$$
f (w, r _ {i}, t _ {j}) = \frac {w ^ {\eta - 1} (1 - w) ^ {\eta - 1}}{B e t a [ 2 r _ {i} (1 - t _ {j}) , 2 (1 - r _ {i}) (1 - t _ {j}) ]}\tag{22}
$$

Using this formulation, we perform numerical analysis to study the model implications across variations in theme strength and likely sample outcomes.

## 3.3. Results from numerical analysis

We utilized numerical analysis to investigate patterns in the outcomes of interest (album purchase probability and the optimal fraction of album to sample, k⁎) as we varied model parameters including cost of sampling (c) , theme strength (t), quality degradation from piracy (δ), and value of album (V). The results of the numerical analysis show that ceteris paribus, as theme strength increases, a consumer is more likely to buy (rather than pirate), which is re<sup>fl</sup>ected in the higher “purchase probability” with higher $t _ { j } .$ (These results are illustrated and explained for speci<sup>fi</sup>c parameter sets in Appendix A.3.).

## 3.4. Description of numerical analysis

In our numerical analysis, we utilized the following set of values across the full relevant range for each speci<sup>fi</sup>ed parameter:

δ the quality degradation of pirated version – varies from 0.1 to 0.9 in increments of 0.1;

V the maximum valuation – varies from 0.5 to 2.0 in increments of 0.1;

c the cost of sampling – varies from 0.0 to 0.2 in increments of 0.01;, and

α (or) $2 r _ { i } ( 1 - t _ { j } )$ the proportion of “good” songs – varies from 0.1 to 0.9 in increments of 0.1.

For each combination of the above values, we numerically determined the following:

(i) the optimal sample size $k ^ { * } ,$

(ii) the resulting optimal net expected value from sampling $E _ { S } ^ { * } ( V _ { i j } | k ^ { * } )$ and

(iii) the probability of purchase, which translates to the probability that, for the optimal $k ^ { * } ,$ the fraction, w, that is found to be good, is greater than or equal to the cutoff $w _ { 0 \delta } .$ For the beta distribution f(w,r,t), the cumulative distribution function $F ( w _ { 0 \delta } , r _ { i } , t _ { j } )$ indicates the probability that the customer will not purchase the album, so that the purchase probability is given by $[ 1 - F ( w _ { 0 \delta } , r _ { i } , t _ { j } ) ]$

The results of the numerical analysis indicate that, even in the presence of piracy, as theme strength increases, the following results continue to hold:

(i) the optimal sample size $k ^ { * }$ decreases (consistent with Results 1 and $4 ) ;$ and,

(ii) the probability of purchase increases (consistent with Result 2).

(Appendix A (Section A.3) provides various illustrations of how purchase probability and optimal sample size vary with theme strength (t), sample cost (c), album value (v), and quality degradation from piracy (δ).)

## 4. Empirical analysis

The results from the analytical model state that consumers are more willing to buy albums with higher theme strength and higher value, even in the presence of piracy. Here we provide initial empirical evidence of the impact of theme strength and value on the relative performance of albums, using the BillBoard Rankings Charts archival data. This data set consists of weekly rankings of the published BillBoard Top 200 album charts, which are calculated from a national sample of retail store sales in the United States from the previous week and are collected, compiled and provided by Neilsen Soundscan. Hence these rankings directly re<sup>fl</sup>ect actual sales of albums.

Our dataset consists of all albums that appeared on the top 100 rankings of the BillBoard Top 200 album charts in the following time periods: 1997–98, 2001–02, and 2003–04. For each album, we have the debut rank – the rank of the album when it <sup>fi</sup>rst appeared on the chart, and the total number of weeks on the BillBoard charts (weeks on chart). A high debut rank (low numerical rank since a rank of 1 is highest) of an album suggests a high value to potential customers [5]. The total number of weeks on chart is a proxy for aggregate sales for a given album. We then match this album information with that available on allmusic.com, a repository of artist, album, and related music information. This provides us with an indicator variable which equals 1 if the album was a compilation. As discussed earlier, a compilation album would be expected to have greater theme strength than a standard album.

We choose the time period of 1997–98 to study the effects on album survival at a time before the availability of online sampling choices lowered sampling costs for consumers, and before online piracy was prevalent. The period 2001–02 re<sup>fl</sup>ects the time period right after online sampling started to become available through peerto-peer (P2P) networks, online fan clubs, and MP3 players. While these made sampling technically much more convenient and ef<sup>fi</sup>cient, the widespread problem of online piracy led the record labels to <sup>fi</sup>ght these networks, discouraging legal and easy sampling. Further, during this time period, there were few opportunities for consumers to sample and then legitimately buy digital music online. Consumers still incurred the cost and inconvenience of buying CD albums from stores. The period 2003–04 encompasses the time when Apple iTunes and other legitimate online music purchase options started to become widely available. In addition, the introduction of the iPod and other mobile digital music players made the consumption of online purchases ubiquitous. While online piracy was still present in this period, online legal purchase options further decreased total sampling and acquisition costs.

We ran the following linear form regression model and provide the results in Table 2:

$$
\text { weeks   on   chart } = f (\text { debut   rank }, \text { compilation   album })\tag{23}
$$

As shown in Table 2, as expected, the debut rank of an album had a signi<sup>fi</sup>cantly positive effect on aggregate sales in all periods (note – lower values of debut rank are better with debut rank # 1 being “best”). However the compilation characteristic of albums had a signi<sup>fi</sup>cant positive effect on sales only in the period 2003–04 with no signi<sup>fi</sup>cant impact in the previous two periods. This interesting result is explained as follows: when sampling costs are high, as in 1997–98 when consumers had to go to a store physically to sample (or listen to the radio), compilations did not have an advantage over standard albums in terms of total sales. In other words, albums with higher theme strength did not have a signi<sup>fi</sup>cant advantage on sales over lower themed albums. In 2003–04, lower sampling costs (and potentially total acquisition cost) propelled more potential consumers to sample, and, given greater theme strength, to buy the album with the higher theme strength. Hence compilation album and debut rank both have a signi<sup>fi</sup>cant positive effect in 2003–04, which is consistent with Result 2. Further, turning our attention to the interaction effect of debut rank and compilation album, we <sup>fi</sup>nd that albums with greater themes do not automatically do better. Analyzing the interaction effect for 2003–04, we <sup>fi</sup>nd that a compilation album that has a high value to consumers (lower debut rank) has a positive effect on aggregate sales. Hence, even in the presence of piracy, a themed album

Impact of rank and compilation on survival (three time periods).

<table><tr><td>Dependent variable: weeks on chart</td><td>1997–98</td><td>2001–02</td><td>2003–04</td></tr><tr><td>Constant</td><td>39.33** (0.00)</td><td>12.47** (0.00)</td><td>11.35** (0.00)</td></tr><tr><td>Debut rank</td><td>-0.19** (0.00)</td><td>-0.12** (0.00)</td><td>-0.11** (0.00)</td></tr><tr><td>Compilation album</td><td>-2.53 (0.70)</td><td>0.06 (0.98)</td><td>3.92* (0.01)</td></tr><tr><td>Debut rank×compilation album</td><td>-0.12 (0.29)</td><td>0.01 (0.74)</td><td>-0.08* (0.01)</td></tr><tr><td>Number of albums</td><td>866</td><td>846</td><td>936</td></tr><tr><td>Adjusted  $R^{2}$ </td><td>0.06</td><td>0.14</td><td>0.14</td></tr></table>

p-values are indicated in parentheses.

$$
^ {*} p <   0. 0 1.
$$

\*\* $\scriptstyle p < 0 . 0 0 1 .$

which has a high value to consumers continues to have a signi<sup>fi</sup>cantly positive effect on aggregate sales. This is consistent with Result 3.

We contrast this set of results from 2003–04 with those of 2001– 02. In 2001–02, we <sup>fi</sup>nd that neither the compilation album nor the interaction effect is statistically signi<sup>fi</sup>cant. Although sampling costs in 2001–02 were lower than in 1997–98 because of the availability of online sampling mechanisms, the lack of easy and legal opportunities to sample and purchase digital content online may have continued to provide an effective barrier. Hence continuing high sampling and acquisition costs may have hampered sales, leading to no signi<sup>fi</sup>cant effect for compilation album. From this analysis, it appears there are threshold values where sampling cost needs to be suf<sup>fi</sup>ciently low and convenient purchase options available which trigger a signi<sup>fi</sup>cant impact on sampling and purchase behavior. These threshold limits may include both technical and psychological dimensions. Our current research includes designing and developing appropriate controlled human subject experiments to carefully investigate these issues.

## 5. Conclusions and discussion

In the new electronic marketplace for music, massive numbers of music albums are available online to sample and purchase through legal channels. Sampling costs have decreased substantially and the purchase process is straightforward for buying individual songs or albums. Yet, one element has remained constant –– once sampling access is obtained, the consumer still takes the same time to actually sample or listen to a song. Today's consumer doesn't hear any faster than earlier consumers. The time that it takes to listen (sample) has not changed and may be the crucial bottleneck to higher sales. But theme strength is an option that we suggest might serve music companies well. By developing theme strength applications, the music industry might turn its sales <sup>fi</sup>gures around. It may still take as long to sample a song, but with increased theme strength, consumers can sample less (take less total time) and make better inferences (more effective purchase decisions).

We began our investigation by developing a simple analytical model that captured the mechanism of pre-purchase sampling in a restricted bundling scenario (i.e. price and size of bundle varies within a narrow range, and bundled items positively correlated). We showed that consumers derive better utility from sampling a stronger themed album than a weaker themed one. We also showed that stronger themed albums lower the optimal sample size for individual consumers and thus may decrease the “listening time” bottleneck. Albums with stronger themes are more likely to be sampled, and consumers who sample such albums are more likely to purchase them. It is in consumers' as well as sellers' best interests to decrease sampling time and help consumers <sup>fi</sup>nd songs they like in the most ef<sup>fi</sup>cient manner possible. Hence we suggest that appropriately themed bundles of songs serve to reduce consumers' need to sample and promote sales of such albums. In an environment of music piracy, where consumers have a choice to sample and not buy or pirate, our simple model demonstrates that such strong themed albums provide a positive utility for consumers to sample and buy.

We then constructed a more complex model that endogenously determines the amount of an album to be sampled and incorporates a learning mechanism that updates the a priori valuation of the album. We performed an exhaustive numerical enumeration of the parameter space. The results verify our initial results that albums with stronger theme strength are more likely to be sampled and purchased.

Finally, we performed an initial validity test of our model and results through an empirical analysis of data on albums on the Billboard Top 200 ranking charts. This empirical analysis shows that, as sampling and acquisition costs decrease, strongly themed albums are associated with longer chart performance (implying better aggregate sales) compared to weakly themed albums. Further, strongly themed albums that are of high value have a signi<sup>fi</sup>cant positive impact on aggregate sales. These results provide initial empirical support to our analytical <sup>fi</sup>ndings and validate our modeling assumptions.

The sales of CD albums decreased more than 18% in 2007 from the previous year, and even accounting for digital downloads, overall album sales fell almost 10% last year [12]. Overall album sales in US declined 21% to 500 million copies in 2007 from 2003, including CDs and digital downloads. Since CD albums are the major revenue (and pro<sup>fi</sup>t) source for music companies, this rapidly declining trend of album sales has been a signi<sup>fi</sup>cant source of consternation to the industry. Our <sup>fi</sup>ndings have signi<sup>fi</sup>cant implications for the music industry which is striving to navigate the new business environment to pro<sup>fi</sup>tability. Some may argue that singles sales have overtaken album sales and is the new business model. US consumers did download 844 million individual songs from digital download stores in 2007, while they bought only 50 million digital albums [18]. From a business perspective, label executives have suggested that the growth of singles sales on iTunes has been “part of the death knell of the music business”. Several up and coming albums have been taken off iTunes' offerings by artists and managers, who did not want to cannibalize album sales with single sales, which subsequently increased their album sales. Irving Azoff, the manager of the well-known Eagles band, reported that royalties from iTunes sales (chie<sup>fl</sup>y consisting of singles) have been far lower than expected, and “amounted to 39 min on stage in Kansas City”. Lastly, there is evidence that classic rock bands that did not have singles sales on iTunes (the largest online music store) during 2006–08 had the highest full album sales (CD and downloads) [18].

In this research, we have taken a <sup>fi</sup>rst step in analyzing the potential importance of theme strength to the music industry. As noted earlier, we are currently engaged in designing and developing controlled laboratory experiments to carefully analyze behavioral decision making in bundled and unbundled digital good settings with various levels of themed bundling options. As with the work reported in this paper, future analysis will also focus on a restricted bundling problem. For experience goods, sampling time remains a bottleneck, but theme strength may be the “killer app” that opens up the ef<sup>fi</sup>ciency of the sampling process. Staying with the music theme, we end by using the oft-spoken words of the radio DJ, “Please stay tuned!”

## Appendix A

## A.1. Proof of Result 1

The expected value from sampling twice, given by $E _ { S S } ( V )$ , is:

$$
E _ {\mathrm{SS}} (V) = \theta (G 1, G 2) (2 v - p) - 2 c
$$

(Since vbp, the consumer will not buy unless both songs are good.) Simplifying the expression for the incremental gain from sampling two songs over sampling one song: $E _ { S S } ( V ) - E _ { S } ( V ) = ( 1 - r ) ~ r ~ ( 1 - t )$ $\left( p - \nu \right) - c .$

Clearly, the coef<sup>fi</sup>cient of theme strength t is negative, which implies that as theme strength increases, the incremental value from sampling two songs (over the value from sampling one song) decreases. 5

## A.2. Proof of Result 4

When piracy is present:

$$
E _ {S S} (V) = \theta (G 1, G 2) (2 v - p) + [ \theta (G 1, B 2) + \theta (B 1, G 2) ] (\delta v) - 2 c
$$

$$
\text { Therefore } E _ {\mathrm{SS}} (V) - E _ {\mathrm{S}} (V) = (1 - r) r (1 - t) (p - v (1 - 2 \delta)) - c.
$$

The coef<sup>fi</sup>cient of theme strength t is:

$$
- (1 - r) r (p - v (1 - 2 \delta))
$$

Since pNv, this expression is always negative. Hence, sampling two songs is less attractive as theme strength increases. 5

## A.3. Illustrations of numerical results based on specific parameter ranges

The results of the numerical analysis show that for the entire parameter range, ceteris paribus, as theme strength increases (i.e. as α decreases), a customer is more likely to buy (rather than pirate), which is re<sup>fl</sup>ected in the higher Purchase Probability with lower α.

a Lower sampling cost leads to higher optional sample size  
![](/api/attachments/D6UQB6GN/fulltext/images/b088d8294bae4b027dafd4717e7ce81fd4fd2e59b7e176df669c34765efc69b1.jpg)

b High album value V leads to higher optimal sample size  
![](/api/attachments/D6UQB6GN/fulltext/images/102dcf1a1b9574151a2b711ae425f3df4a92696a15508194025f6a77b328e7ab.jpg)  
C Higher quality of pirated version (higher δ) leads to higher optimal sample size

![](/api/attachments/D6UQB6GN/fulltext/images/34e86320f0fe3d8013aa66285453a4d0f10672e398e982992fdb64c5163e1db2.jpg)  
Fig. 1. Shows how increasing α (i.e. decreasing theme strength t) results in lower purchase probability. Also shown are the effects of sampling cost (panel a), album value (panel b) and piracy (panel c).

a Lower sampling cost leads to higher optimal sample size  
![](/api/attachments/D6UQB6GN/fulltext/images/4f62232dac8602a8b8316f96bc1ca5ee380713c6df11d5a6181ed05f87e77efc.jpg)

b Higher album value V leads to higher optimal sample size.  
![](/api/attachments/D6UQB6GN/fulltext/images/12ba7ab00d507fb8ae90455a81ce694953ba030fb3353af3b0311c57ca7c9da2.jpg)  
C Higher quality of pirated version (higher) leads to higher optimal sample size

![](/api/attachments/D6UQB6GN/fulltext/images/8936c55225bd8bd91f95d3c175ee1edd6e9965f80f8b372a379ce438443e53a6.jpg)  
Fig. 2. Shows how increasing α (i.e. decreasing theme strength t) results in higher optimal sample size. Also shown are the effects of sampling cost (panel a), album value (panel b) and piracy (panel c).

This is illustrated for some speci<sup>fi</sup>c parameter values in Fig. 1. The numerical analysis also establishes that for the entire parameter range, ceteris paribus, as theme strength increases (i.e. as α decreases), the optimal sample size $( \boldsymbol { k } ^ { * } )$ decreases, which is re<sup>fl</sup>ected in the higher $k ^ { * }$ with higher α. This is illustrated for some speci<sup>fi</sup>c parameter values in Fig. 2.

## References

[1] S. Bhattacharjee, K. Lertwachara, R.D. Gopal, J.R. Marsden, No more shadow boxing with online music piracy: strategic business models to enhance revenues, Proceedings of the 36th Annual Hawaii International Conference on System Sciences, 2003, 11 pp.

[2] S. Bhattacharjee, R.D. Gopal, K. Lertwachara, J.R. Marsden, Consumer search and retailer strategies in the presence of online music sharing, Journal of Management Information Systems 23 (2006) 129–159.

[3] S. Bhattacharjee, R.D. Gopal, K. Lertwachara, J.R. Marsden, Impact of legal threats on online music sharing activity: an analysis of music industry legal actions, The Journal of Law and Economics 49 (2006) 91–114

[4] S. Bhattacharjee, R. Gopal, K. Lertwachara, J.R. Marsden, Whatever happened to payola? An empirical analysis of online music sharing, Decision Support Systems 42 (2006) 104–120.

[5] S. Bhattacharjee, R.D. Gopal, K. Lertwachara, J.R. Marsden, R. Telang, The effect of digital sharing technologies on music markets: a survival analysis of albums on ranking charts, Management Science 53 (2007) 1359–1374.

[6] M. Bourreau, F. Moreau, M. Gensollen, The digitization of the recorded music industry: impact on business models and scenarios of evolution, SSRN eLibrary. (2008).

[7] R.K. Chellappa, S. Shivendu, Managing piracy: pricing and sampling strategies for digital experience goods in vertically segmented markets, Information System Research 16 (2005) 400–417.

[8] R.H. Coase, Payola in radio and television broadcasting, The Journal of Law and Economics 22 (1979) 269.

[9] R. Desztich, S. McClung, Indie to an extent? Why music gets added to college radio playlists, Journal of Radio Studies 14 (2007) 211.

[10] X. Geng, M.B. Stinchcombe, A.B. Whinston, Bundling information goods of decreasing value, Management Science 51 (2005) 662–667.

[11] R.D. Gopal. S. Bhattachariee, G.I. Sanders, Do artists benefit from online music sharing? The Journal of Business 79 (2006) 1503–1533.

[12] C. Holahan, The Record Labels' Digital Future, Business Week. (2008).

[13] M. McGuire, D. Slater, Consumer taste sharing is driving the online music business and democratizing culture, The Berkman Center for Internet and Society and Gartner Report, Harvard Law School, 2005.

[14] P. Nelson, Information and consumer behavior, The Journal of Political Economy 78 (1970) 311–329.

[15] T.S. Raghu, P.K. Kannan, H.R. Rao, A.B. Whinston, Dynamic pro<sup>fi</sup>ling of consumers for customized offerings over the internet: a model and analysis, Decision Support Systems 32 (2001) 117.

[16] R. Ragno, C.J. Burges, C. Herley, Inferring similarity between music objects with application to playlist generation, Proceedings of the 7th ACM SIGMM International Workshop on Multimedia Information Retrieval, ACM, 2005, pp. 73–80.

[17] C. Shapiro, Optimal pricing of experience goods, The Bell Journal of Economics 14 (1983) 497–507.

[18] E. Smith, N. Wing<sup>fi</sup>eld, More artists steer clear of iTunes; Apple's online music store sells lots of singles, but labels seek higher pro<sup>fi</sup>ts of full album sales. Wall Street Journal. B.1 (2008).

Sudip Bhattacharjee is an Associate Professor and Ackerman Scholar in the Department of Operations and Information Management in the School of Business, University of Connecticut. He also serves as the Executive Director of MBA Programs. Dr. Bhattacharjee's research interests lie in multi-objective optimization, information systems economics and intellectual property rights, operations management, supply chains and distributed computing systems. His research has appeared or is forthcoming in various journals such as Management Science, INFORMS Journal on Computing, Journal of Management Information Systems, Journal of Business, Journal of Law and Economics, Communications of the ACM, IEEE Transactions, Decision Support Systems, and other journals and conference proceedings. His research has been highlighted in various media outlets.

Ram D. Gopal is a GE Capital Endowed Professor of Business and Head of the Department of Operations and Information Management in the School of Business, University of Connecticut. His current research interests are in the areas of information security, privacy and valuation, intellectual property rights, online market design and business impacts of technology. His research has appeared in Management Science, Operations Research, INFORMS Journal on Computing, Information Systems Research, Journal of Business, Journal of Law and Economics, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, Journal of Management Information Systems, Decision Support Systems, and other journals and conference proceedings. He serves on the editorial board of Information Systems Research, Journal of Database Management, Information Systems Frontiers, and Journal of Management Sciences.

Dr. James R. Marsden, is the Treibick Family Endowed Chair in e-Business and Board of Trustees Distinguished Professor, at the Department of Operations and Information Management (OPIM) at the University of Connecticut, He has been at UConn since 1993 as Professor, serving <sup>fi</sup>fteen years (1993–2008) as Head of OPIM. He helped develop both the Connecticut Information Technology Institute and the Treibick Electronic commerce Initiative and currently serves as Executive Director of both. Jim also severs as the UConn Director of edgelab, the unique ongoing research partnership between GE and UConn now in its ninth eighth year of operation (see www.edgelab.com). Dr. Marsden has a lengthy publication record in market innovation and analyses, economics of information, arti<sup>fi</sup>cial intelligence, and production theory. His research work has appeared or is forthcoming in Management Science; Journal of Law and Economics; American Economic Review; Journal of Economic Theory; Journal of Political Economy; IEEE Transactions on Systems, Man, and Cybernetics; Computer Integrated Manufacturing Systems; Decision Support Systems; Journal of Management Information Systems, and numerous other academic journals. He received his A.B. from the University of Illinois and his M.S. and Ph.D. from Purdue University. Also holding a J.D, Jim has been admitted to both the Kentucky and Connecticut Bar.

Ramesh Sankaranarayanan is an Assistant Professor in the Department of Operations and Information Management in the School of Business, University of Connecticut. His current research interests include game theory; innovation, pricing, licensing, and versioning as applicable to durable digital goods such as music, movies, software and video games; and agency theory applied to inter-<sup>fi</sup>rm relationships. His work has appeared or is forthcoming in Information Systems Research, Decision Support Systems, Marketing Science, ACM Transactions, and Communications of the ACM.

Rahul Telang is an Associate Professor of Information Systems at Carnegie Mellon University. Dr Telang’s key research <sup>fi</sup>eld is in economics of Information security and digital media. He has done extensive empirical as well as analytical work on disclosure issues surrounding software vulnerabilities, software vendors’ incentives to provide quality, role of software standards, mechanism designs for optimal security investments and effectiveness of data disclosure policies etc. He received the prestigious National Science Foundation CAREER award for his research in economics of information security. His another area of work is online piracy and digital media research and codirects the digital media research center at CMU. He was recipient of Alfred P Sloan foundation industry study fellowship for his work on Digital Media. He has published numerous articles in leading journals including Management Science, Information Systems Research, Journal of Marketing Research, IEEE transactions of Software Engineering, etc. He is an associate editor at Management Science and Information Systems Research. His work has been reported in The New York Times, Washington Post among other media outlets
