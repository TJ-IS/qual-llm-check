---
otero_id: 13856
otero_key: "8AGURRUZ"
title: "Friendships in Online Peer-To-Peer Lending: Pipes, Prisms, and Relational Herding1"
authors: "De Liu; Daniel J. Brass; Yong Lu; Dongyu Chen"
year: "2015"
journal: "MIS Quarterly"
doi: "10.25300/misq/2015/39.3.11"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# FRIENDSHIPS IN ONLINE PEER-TO-PEER LENDING:PIPES, PRISMS, AND RELATIONAL HERDING<sup>1</sup>

De Liu Department of Information and Decision Sciences, Carlson School of Management, University of Minnesota, Minneapolis, MN 55455 U.S.A. {deliu@umn.edu}

Daniel J. Brass LINKS Center for Social Network Analysis, Gatton College of Business and Economics, University of Kentucky, Lexington, KY 40506 U.S.A. {dbrass@uky.edu}

Yong Lu Institute of Internet Finance & Institute of Chinese Financial Studies, Southwestern University of Finance and Economics, CHINA, and Information Science & Technology, The Pennsylvania State University, 76 University Drive, Hazelton, PA 18202 U.S.A. {ericlu@psu.edu}

Dongyu Chen Dongwu Business School, Soochow University, No. 50, Donghuan Road, Suzhou City, Jiangsu Province, PEOPLE’S REPUBLIC OF CHINA {chendongyu@suda.edu.cn}

This paper investigates how friendship relationships act as pipes, prisms, and herding signals in a large online, peer-to-peer (P2P) lending site. By analyzing decisions of lenders, we find that friends of the borrower, especially close offline friends, act as financial pipes by lending money to the borrower. On the other hand, the prism effect of friends’ endorsements via bidding on a loan negatively affects subsequent bids by third parties. However, when offline friends of a potential lender, especially close friends, place a bid, a relational herding effect occurs as potential lenders are likely to follow their offline friends with a bid.

Keywords: Peer-to-peer lending, friendship relationships, social networks, prism effect, herding

… man’s economy, as a rule, is submerged in his social relationships. (Polanyi 1944, p. 46)

## Introduction

The idea that economic transactions are embedded in social relationships is not new (Granovetter 1985; Uzzi 1999). However, social networking sites such as Facebook and Linkedin have changed the landscape of social embeddedness by greatly facilitating the creation and maintenance of many social relations and making them highly visible (Kane et al. 2014; Oestreicher-Singer and Sundararajan 2012). More and more online platforms are seeking to leverage these social relations for economic activities such as lending (Prosper), car sharing (Getaround), and rentals (AirBnB). As individuals connected by powerful social networking tools transact with each other, it is inevitable that economic decisions are embedded in social relations. Such is the case with online peer-to-peer (P2P) lending where individual lenders collectively bid on loan requests by individual borrowers in an online platform supported by social networking tools.

There are several online peer-to-peer lending platforms worldwide, such as Prosper, Lending Club, Zopa, Funding Circle, and PPDai. It is expected that loans originated by P2P lenders in the United States alone will reach \$20 billion yearly by 2016 (http://goo.gl/A7KlAO). Online P2P lending is part of a larger crowd funding movement that uses the Internet to rally the crowd for collective funding (Burtch et al. 2013; Zvilichovsky et al. 2013). As with other crowd funding platforms, P2P lending leverages the “wisdom of the crowd” (Freedman and Jin 2008; Yum et al. 2012) by allowing multiple lenders to collectively fund a loan. P2P lending also provides online social networking functions so that lenders and borrowers can declare friendships with one another (Yum et al. 2012). These friendships include both existing offline social relations and newly formed online friends. P2P lending platforms provide tools for members to formally recognize these social relations, together with benefits such as the ability to broadcast loan requests to friends, and to receive notifications of friends’ borrowing and lending activities. The ability to leverage friendship networks in borrowing/lending activities is a key difference between online P2P lending and traditional lenders such as banks. Recent research on online P2P lending takes a borrower’s perspective to study how friendships affect the overall funding outcomes and subsequent loan performance. Freedman and Jin (2008) found that borrowers’ friendship networks were consistently significant predictors of lending outcomes. Lin et al. (2013) found that the number of friends that a borrower has and the number of friends that actually bid on a loan increase the probability of successful funding of a loan and reduce interest rates and ex post default rates. However, overall funding outcomes are a result of many decisions made by potential lenders over time and the route from friendship to funding success may be more complicated than it appears when only considering aggregate outcomes. For example, the aggregate measures of funding success may suggest a positive effect of a bid by a friend of the borrower on subsequent potential lenders, but our investigation of lending decisions finds the opposite effect. Our focus on individual lending decisions allows us to better distinguish different ways friendship relations may affect lending decisions.

We add to the previous research by focusing on lending decisions to obtain a clearer, more detailed picture of the effects of social relationships on economic transactions. We study how the decision of whether or not to offer a loan is affected by the friendship between the potential lender and the borrower (the pipe effect), by a bid from the borrower’s friend (the prism effect), and by a bid from the potential lender’s friend (the relational herding effect). Aggregate economic outcomes, such as funding success, may be attributed to some or all of these effects and it is important to understand the effect of each. We further investigate the nuances of friendship effects by distinguishing between offline and online friends. The proliferation of online social networks raises questions regarding the comparability of online and offline friendships, but little empirical evidence exists on these questions (Bapna et al. 2011; Bond et al. 2012; Kane et al. 2014). Overall, we attempt to expand the previous research by providing a more nuanced, detailed understanding of the way social relations impact economic decisions in online platforms such as P2P lending.

## Theoretical Development

## Pipes

Economic transactions are embedded in social relationships, and friendship surely plays a key role. According to Granovetter’s (1985) theory of embeddedness, there is “widespread preference for transacting with individuals of known reputation” (p. 490), and there is no better basis for trust than our own past dealings with people. Trust is particularly important when markets are inefficient, such as in the case of P2P lending sites which suffer from information asymmetry and adverse selection problems (Akerlof 1970; Spence 2002). As Granovetter (2005) notes, when assessment of product quality or seller credibility is difficult, one-quarter to one half of all U.S. purchases of goods are made through personal networks. Thus, we expect that people will be more likely to lend money to friends whom they feel they know and trust. That trust is likely well-placed as there is motivation to repay the loan so as not to disrupt the friendship. Indeed, results on P2P lending using Prosper data show a negative relationship between friendship and default on loans (Freedman and Jin 2008; Lin et al. 2013).

While previous research has shown that the number of friends bidding on a loan is positively related to successful funding and low defaults (Lin et al. 2013), our data allows us to investigate the probability of a friend bidding on a listing prior to and regardless of the overall funding success, and to distinguish between different types of friendship relationships.

Following the terminology used by P2P lending platforms and other social media, we use the term friends to refer to a broad range of digitized social relations of both online and offline origins. Within this broad categorization of friends, we distinguish between online friends (who only communicate online) and offline friends (who communicate offline and possibly online). We further distinguish between types of offline friends using the frequently used social network classification of strong ties (close friends and relatives) and weak ties (colleagues and acquaintances). In sum, we have three mutually exclusive “friendship” categories: offline strong-tie friends, offline weak-tie friends, and online friends. While we expect friends to be more likely to offer bids than strangers, our data permit a more detailed analysis of these relationships. We anticipate that the strong social obligation to support one’s strong-tie friends will override any negative economic considerations, and offline strong-tie friends will be more likely to offer loans than offline weak-tie friends. Further, we expect that even offline weak-tie friends will be more likely to bid on loans than online friends. The proliferation of online social networks raises questions regarding the qualities of online friendships compared with offline friendships and it is popularly believed that online friends are not the same. Kane and colleagues (2014) note two basic differences: online relationships are easier to form, and online relationships are more visible to others. Initial empirical evidence suggests that online friendships are less influential (Bond et al. 2012), less holistic (restricted to nonpersonal topics rather than everyday activities), shorter in duration (fewer shared events in the history of the relationship), and have less opportunity to develop mutual trust and reciprocity than offline friendships (Cummings et al. 2002; Mesch and Talmud 2006). In addition, members of P2P lending sites may forge online utilitarian friendships with others that they don’t know off-line but that appear useful for attaining economic goals (e.g., history of funding success or a large number of friends). The following hypotheses reflect the direct pipe between the borrower and the potential lender.

H1: An offline strong-tie friend of the borrower is more likely to bid on a listing than an offline weak-tie friend of the borrower.

H2: An offline weak-tie friend of the borrower is more likely to bid on a listing than an online friend of the borrower.

## Prisms

While the information and resource advantages of social relations as pipes are well documented in the network literature (Brass 2012; Brass et al. 2004), very little is known about the prism effects of friendship. Prism is a metaphorical label coined by Podolny (2001) to describe how an actor’s social relations can affect third parties’ perceptions of the actor’s goods and services. Podolny (2001) argued that actors exchange relations with high status others can act as status endorsements and provide signals of credibility and reliability to third parties. The social network research on prism effects has focused on high-status endorsements, showing that mere perceptions of social relationships with high-status others can induce positive reputation evaluations even when such relations do not exist (Kilduff and Krackhardt 1994). Rather than status, we focus our research on the prism effects of exchange relations with friends, or friend endorsements. While little is known about how friend endorsements are perceived by others, we note that friend endorsements (e.g., “liking”) are much more prevalent than high status endorsements in online social networks.

Do friend endorsements produce the same positive prism effects as endorsements by high status others? While both high-status and friend endorsements can provide informational cues to third-party observers, they are quite different in nature. High-status endorsers have a reputable public image and are motivated to maintain such a public image. Friend endorsers are not. Friends have an emotional or social obligation to each other, not to the public.

We argue that a third-party potential lender may interpret a friend endorsement, in the form of a bid by a friend of the borrower, differently from a stranger’s bid. On the one hand, potential lenders may view an endorsement by a borrower’s friend as a positive signal of quality. Potential lenders may infer that friends of the borrower know more about the borrower, therefore their bids reveal their private information about the borrower (Donath and Boyd 2004; Freedman and Jin 2008; Lin et al. 2013). Friends can also closely monitor the borrower after the loan is initiated, thus mitigating the moral hazard problem (Arnott and Stiglitz 1991). Finally, friends may impose social sanctions on the borrower in the event of default (Besley and Coate 1995). Borrowers are not likely to default on a loan funded by their friends. Based on these arguments, a bid by a friend of the borrower signals low defaulting probability and may have a positive effect on subsequent lending probability.

On the other hand, friends may be emotionally biased or feel strong social obligations toward the borrower. Friendships have an affective foundation as opposed to an economic foundation. Such relationships are governed by mutual, reciprocated affect rather than reciprocated economic exchange. As Argyle and Henderson (1984) note, in friendship relationships “receiving benefits does not incur a specific debt to return a comparable benefit, and does not alter the general obligation to aid the other in need” (p. 213). Calculated selfinterest is the antithesis of friendship and consciously monitoring economic exchange undermines the trust and mutual support inherent in friendship (Silver 1990). Thus, potential lenders will likely view bids from friends of the borrower as signaling emotional attachment and social obligation to the borrower rather than economic value. In addition, potential lenders may view a friend endorsement as a result of collusion: Friends have a better chance than does a stranger to recoup their investments using their social leverage, or borrowers may provide side payments in return for bids.

For a friend endorsement to be a credible signal of quality, some form of sanction is required (e.g., friends’ reputation concerns). Friend monitoring typically works in a group of individuals who are tightly connected to each other (Arnott and Stiglitz 1991). However, on P2P lending platforms, most potential lenders are strangers to the borrower and his/her friends and thus have no way of holding friend endorsers accountable. Moreover, third-party lenders cannot observe or verify the type of friendship between the borrower and the endorser; they observe only a friend bid. In such a circumstance, a friend endorsement is more likely viewed as a signal of social obligation, affective bias, or collusion, than a signal of quality. Therefore, while acknowledging the countervailing arguments, we hypothesize that endorsements by friends of the borrower will negatively affect future bids by others.

H3: A potential lender is less likely to bid on a listing if a prior bid on the listing is by a friend of the borrower than by a stranger to the borrower.

## Relational Herding

When individuals face uncertainties in making economic decisions, they may follow the actions of others, a phenomenon known as “herding” (Bikhchandani et al. 1992; Bikhchandani and Sharma 2000).<sup>2</sup> Banerjee (1992), Bikhchandani et al. (1992), and Welch (1992) describe herding as the result of informational cascading when people optimally ignore their private information and follow the behavior of agents who are believed to hold valuable private information. Herding may also be a result of individuals blindly following others without calculated analysis (Devenow and Welch 1996). Different from social influence theories (Cialdini 1993; Friedkin and Johnsen 2011),<sup>3</sup> theories of herding require only the observation of others’ actions.

Because the Internet has vastly improved the observability of others’ actions, herding is a prevalent phenomenon in online platforms, as illustrated by software downloading behavior (Duan et al. 2009) and eBay auctions (Simonsohn and Ariely 2008). In P2P lending markets, Herzenstein et al. (2011) and Lee and Lee (2012) show that the more existing funding a loan obtains, the more future funding of the same loan. Zhang and Liu (2012) further show that lenders on Prosper not only use existing bidding amounts as herding signals, but also view such signals as more informative when the underlying loan has unfavorable characteristics. As with previous research, we expect herding to exist in our setting:

H4: A potential lender is more likely to bid on a listing as the number of prior bids on the listing increases.

The extant herding research assumes prior behaviors are anonymous and does not take into account social relations between prior and subsequent decision makers. This is not the case with online social platforms, where individuals are connected via social networking technology and can easily track friends’ activities. For example, potential lenders are notified when a friend has made a bid on a listing, and this may serve as a filter for only considering loans that have been previously bid on by a friend. We expect that herding behavior in the P2P context will be more nuanced and sensitive to the types of social relations between individual decision makers. We refer to herding between socially connected decision markers as relational herding to differentiate it from the classic anonymous herding.

We expect potential lenders to more likely follow bids from their friends than bids from strangers. Multiple theories may explain relational herding behaviors. The theory of network transitivity (Heider 1958; Newcomb 1961) predicts that if I trust my friend and my friend trusts the borrower (offers a bid), then I should also trust the borrower and offer a bid. Similarly, cognitive balance theory (Festinger 1962; Heider 1958; Newcomb 1961) posits that if my friend trusts A by offering a bid but I do not, a stressful psychological inconsistency occurs: a drive for cognitive balance will cause me to also bid on A. In addition, P2P lending platforms provide shortcuts to listings invested by friends. Such listings may simply be more salient to the potential lender due to the notification of a friend’s bid. Thus, a potential lender is more likely to bid on a listing after observing a bid from his or her friend than a bid from a stranger. Moreover, potential lenders have knowledge of whether the bid is from an offline strong tie, offline weak tie, or online friend. We expect potential lenders to make differential decisions as a result. Based on the previously noted differences between offline and online friends and Granovetter’s (1973) distinction between offline strong and weak ties, we expect the trust and tendency toward balance to be greatest among offline strong-tie friends, followed by offline weak-tie friends, and least among online friends.

H5: A potential lender is more likely to bid on a listing if a prior bid on the listing is by an offline strong-tie friend of the lender rather than by an offline weak-tie friend of the lender.

H6: A potential lender is more likely to bid on a listing if a prior bid on the listing is by an offline weak-tie friend of the lender rather than by an online friend of the lender.

## Data

We obtained our data from PPDai, one of the largest peer-topeer lending platforms in China. PPDai has over 1 million members and has provided 100 million RMB in funded loans as of August, 2011, since its official launch in 2007. On PPDai, borrowers can post loan requests, called listings, with a title, description, loan amount, interest rate (or borrowing rate), number of monthly repayments, etc. (Figure 1). Borrowers can also provide additional information about themselves such as age, gender, education, location, income, marriage status, photo, and so on. PPDai provides identity verification services using national identification cards, photo, cell phone, and video. The platform calculates a credit score for each borrower based on borrowing/lending history and the number of verified information.<sup>4</sup>

A listing is typically open for several days. At the entry page for lenders, dozens of active listings are shown with borrower’s user ID, photo, loan title, borrowing amount, asking rate, credit rating, percent completed, and time left. Lenders can search, filter, and sort listings by percent completed, credit rating, time left, and time since posting. By clicking on a particular listing, a potential lender can observe additional information about the listing/borrower (Figure 1), such as loan description, borrower’s age, gender, education, authentication, a link to the borrower’s profile page, and the entire bidding history (Figure 2). To bid on a listing, a lender must submit the bid amount and interest rate (which is usually the borrowing rate). The minimum bid amount is 50 RMB and lenders are encouraged to bid in small amounts as a way of diversifying risks. As a result, a listing typically requires dozens of bids to become fully funded.

Over 98 percent of lending auctions at PPDai are “closed” auctions, that is, auctions are set to terminate immediately after reaching 100 percent funding status and the interest rate is fixed at the borrowing rate.<sup>5</sup> A listing that reaches 100 percent funding status is a “successful” listing; otherwise, the borrower receives zero funding.

All successfully funded listings are forwarded to PPDai staff for further review. PPDai does not disclose the details of the review. Anecdotal evidence suggests that PPDai routinely rejects borrowers who fail to obtain adequate identity verification or have overdue loans. About 70 percent of successful listings pass PPDai review and become loans. Once a listing passes review, funds are transferred from lenders to the borrower, minus a 2 to 4 percent service fee. The service fee rate varies depending on the loan duration. In subsequent months, borrowers are obligated to repay the principal and interest in monthly installments. The repayments are proportionally distributed to the lenders of the loan. If a repayment is overdue, PPDai makes several attempts to recover the loan, including e-mailing, text messaging, calling the borrower, and, in extreme cases, exposing the borrower’s identity online as a way of pressuring the borrower (Lu et al. 2012).

Like other P2P lending platforms, PPDai allows members to declare friendships with one another. Any member can send a friend request to another member. The initiating party must choose a friendship type from two online friendship types (PPDai friends and other online friends, such as Taobao friends) and six offline friend types (close friends, ordinary friends, colleagues, classmates, relatives, and acquaintances). After the friend request is confirmed by the recipient, the friendship will be displayed on both members’ profile pages without distinguishing the type of friendship. By becoming friends, a member will receive notifications when friends bid on a listing. PPDai also displays a “friend bid” symbol next to the bids submitted by borrower’s friends (see Figure 2 for an illustration). Unlike some other P2P lending platforms,<sup>6</sup>

![](/api/attachments/8AGURRUZ/fulltext/images/fc21ce5eaf217aa57918656aa61ecdef137967178122f612dcb838e4ae8c21d7.jpg)

## Borrower information

PPDai audit

PPDai statistics

Borrower Objective: Gender: Male Age: 26

Marital status: Single

Level of education: college

financial position of the (self-administered, unaudited ):

Income items Expenditure items

Other certification programs (third party certification ):

![](/api/attachments/8AGURRUZ/fulltext/images/bf474b199407813f5d83c48d1aadef05ed11b1a52fe2d8059228db0be79bc65d.jpg)

The screenshots were translated from Chinese using GoogleTranslate with minor corrections.

Figure 1. A PPDai Listing  
![](/api/attachments/8AGURRUZ/fulltext/images/b8fd6442f7327fa011890cb7d6a2c655755840a8c522826a625cbad3cad082bc.jpg)  
Figure 2. Bidding History

<table><tr><td>Variables</td><td>Value</td></tr><tr><td># of lenders</td><td>2166</td></tr><tr><td># of borrowers</td><td>7812</td></tr><tr><td># of listings</td><td>12514</td></tr><tr><td># of fully funded listings</td><td>2074</td></tr><tr><td># of approved loans</td><td>1353</td></tr><tr><td># of fully repaid loans</td><td>1257</td></tr><tr><td>Average bids per listing (SD)</td><td>6.47 (15.06)</td></tr><tr><td colspan="2">Offline strong ties</td></tr><tr><td>Close friend</td><td>1,518</td></tr><tr><td>Relative</td><td>632</td></tr><tr><td colspan="2">Offline weak ties</td></tr><tr><td>Colleague</td><td>710</td></tr><tr><td>Ordinary friend</td><td>14766</td></tr><tr><td>Classmate</td><td>524</td></tr><tr><td>Acquaintance</td><td>390</td></tr><tr><td colspan="2">Online friends</td></tr><tr><td>PPDai friend</td><td>87873</td></tr><tr><td>Other online friend</td><td>1,143</td></tr></table>

here are very few groups with restricted members on PPDai and these groups are essentially forums where members can post questions and share experiences.

We obtained a proprietary dataset from PPDai that contains all member and friendship information as of August, 2011, and records of listings, biddings, and repayments from inception to August, 2011. We used an 18-month period from January 1, 2009, to June 30, 2010, for this study. The earlier and later data were discarded to avoid the initial launch period and truncation on loan repayments respectively. Table 1 summarizes the data for the study period.

We constructed a sample that consists of lender–listing pairs. A lender–listing pair is included in our sample if the lender is active during the duration of a listing, with active defined as having bid at least once (on any listing) during the observation window. This approach minimizes the risk of including inactive lenders who no longer visit the site. However, it may leave out lenders who visited the site but did not bid on any listing. The risk of the latter is low because the observation window, which equals the duration of a listing, is reasonably long for observing any bidding activity. As a precaution, we also estimated the probability of a lender being active and used it to correct possible selection bias (details described in the section “Heckman Correction of Selection Bias”).

We constructed a dependent variable (bidyes<sub>ij</sub>) to indicate whether lender i bids on listing j. If lender i bids at least once on listing j, we recorded a value of 1 for $b i d y e s _ { i j } .$ Otherwise, we recorded a value of 0. Each lending decision is accompanied by a decision time t. For a positive decision (bidyes = 1), we used the bidding time as the decision time. If a lender submits multiple bids, which rarely occurred, we randomly chose one as the decision time. For a negative decision $( b i d y e s _ { i j } = 0 )$ , we used the time of bidding on a different listing as the decision time (recall that an active bidder must have at least one bid). In case of multiple bids on other listings, we randomly chose one as the decision time (we also tested other decision times in Appendix C). Because lenders can use filters, search tools, and direct links to bypass listings without explicitly evaluating them, we interpret $b i d y e s _ { i j } = 0$ as either an explicit decision in which the lender evaluated the listing and decided not to bid on it, or an implicit one in which the lender bypassed the listing without an explicit evaluation. Our construction resulted in a total of 2,546,799 lending decisions, 2.6 percent of which are positive decisions. To speed up the analysis, we randomly selected 50 percent of the dataset for model estimations.

## Empirical Model and Results

## Lending Probability

We estimated a conditional logit model for lending decisions. Consider a lender who faces a choice of whether to bid on a listing. Her utility from lending to the listing is

$$
U _ {i j} ^ {*} = X _ {i j} \alpha + Y _ {i} \beta + Z _ {j} \gamma + \varepsilon_ {i j}\tag{1}
$$

where $X _ { i j }$ is a set of lender–listing variables that may include social relationships between the lender and the borrower and time-variant listing characteristics such as number of prior bids. $Y _ { i }$ denotes a set of lender characteristics such as lender's past bids. $Z _ { j }$ denotes a set of listing/borrower characteristics that remain constant for all lenders. $\mathcal { E } _ { i j }$ denotes a random component in her utility. The utility $\check { U } _ { i j } ^ { * }$ is not observed. Instead, we only observe lending decisions $b i d y e s _ { i j }$ which, by the convention of latent class models (Greene 2002), takes a value of 1 if $U _ { i j } ^ { * } > 0$ and 0 otherwise.

A conditional logit model is akin to a fixed-effect logit model because both models compare decisions within the same group and interpret differences as a result of within-group variations. A conditional logit model grouped by listings estimates the probability of a lender bidding on a listing conditional on the total number of bids the listing gets. When the error term $\mathcal { E } _ { i j }$ in (1) satisfies an i.i.d. type-I extreme value distribution, this conditional probability is not a function of time-invariant listing characteristics $( Z _ { j } )$ so that estimations are not biased by unobserved listing heterogeneities (see Appendix A for details). This is especially important in our context because individual lenders often make decisions based on “soft” information (Lin et al. 2013) such as profile photos and loan descriptions, which are notoriously difficult to account for.

Based on our theoretical development, we further specify the latent utility model (1) as:

$$
\begin{array}{c} U _ {i j} ^ {*} = \alpha_ {1} P i p e _ {i j} + \alpha_ {2} P r i s m _ {i j} + \alpha_ {3} R e l a t i o n a l H e r d _ {i j} + \\ \alpha_ {5} C o n t r o l s _ {i j} + \beta L e n d e r A t t r i b u t e s _ {i} + Z _ {f} \gamma + \varepsilon_ {i j} \end{array}
$$

$P i p e _ { i j } ,$ a binary variable indicating whether the potential lender is a friend of the borrower, captures the pipe effect. $P r i s m _ { i j }$ and $R e l a t i o n a l H e r d _ { i j } ,$ calculated as the number of prior bids by friends of the borrower and by the friends of the lender respectively, capture the prism and relational herding effects, respectively. For $P i p e _ { i j }$ and $R e l a t i o n a l H e r d _ { i j } ,$ we further distinguish three mutually exclusive friendship categories: offline strong ties (close friends and relatives), offline weak ties (ordinary friends, classmates, colleagues, and acquaintances), and online friends (PPDai and other online friends). We count a friendship relation only if it was confirmed before the listing.

As control variables, we calculated the number of prior bids, the number of large bids, and the number of bids from elite lenders. We considered a bid to be large if it exceeds 2,000 RMB, which is approximately one standard deviation above the average bid size. To calculate elite bids, we followed PPDai’s formula by first calculated lending scores of each lender at each decision time as 2 × successful bids + 2 × full monthly payments received – 10 × overdue monthly payments (by 30 days or more). We then defined an elite lender as one whose lending score exceeded 1000, which is approximately one standard deviation above the average lending score.

We included several lender attributes as controls: age, gender, education, past bids, and days since last bid. The last two lender attributes are time-specific and calculated for each specific decision time. Three time-variant listing characteristics were used as controls: number of days since listing, percentage of funding completed, and whether the listing has reached 100 percent funding status. Because the tendency to bid may vary throughout the week, we included day-of-week dummies. We included a variable “same city” to capture a potential “home bias” (Lin and Viswanathan 2013). Finally, we controlled for the potential interaction between prism and relational herding effects by including the number of prior bids by friends of both lender and borrower. A list of variables and their descriptive statistics are provided in Table 2. A correlation table is provided in Appendix D.

## Heckman Correction of Selection Bias

Selection biases may arise if active lenders are systematically different from inactive ones in their lending decisions. A commonly used approach for correcting such selection bias is a two-step Heckman correction procedure. To do so, we constructed a sample that includes both the sample of active lenders and an equal number of lender–listing pairs randomly selected from the remaining inactive lenders. We followed the Heckman correction procedure by first running a Probit model estimating the probability of a lender–listing pair to be active. Weighting factors were included in the Probit model to account for differences in sampling ratios. A lender may be inactive either because the lender was not present or because the lender was present but chose not to bid on any of the available listings. To account for the first effect, we included explanatory variables that may affect lenders availability, such as marriage status, past bids, days since last bid, number of children, and membership length. To account for the second effect, we included explanatory variables that characterize the choice set, including the number of listings and the number of low-risk listings (credit grade D or above). Variables such as marriage status, number of children, and number of listings are not in the main regression, thus satisfying the exclusion restriction. From the first-period Probit model, we calculated the inverse Mills ratio, which can be interpreted as nonparticipation hazard, and included it in the main model.

<table><tr><td colspan="4">Table 2. Bidding Level Descriptive Statistics (N = 1,250,426)</td></tr><tr><td>Name</td><td>Description</td><td>Mean</td><td>SD</td></tr><tr><td>bidyes</td><td>The lender has bid on the listing</td><td>0.02</td><td>0.15</td></tr><tr><td>daysPassed</td><td># of days passed since listing</td><td>4.12</td><td>3.54</td></tr><tr><td>pctCompleted</td><td>The listing has reached 100% funding</td><td>0.09</td><td>0.33</td></tr><tr><td>pct100</td><td>The percentage of funding completed</td><td>0.04</td><td>0.19</td></tr><tr><td>ldrAge</td><td>Age of the lender</td><td>31.31</td><td>6.28</td></tr><tr><td>ldrFemale</td><td>Gender of the lender (1 = Female)</td><td>0.17</td><td>0.38</td></tr><tr><td>ldrEdu</td><td>Education level of the lender (1 = middle/high school, 2 = 3-year college, 3 = 4-year college, 4 = graduate school)</td><td>2.41</td><td>1.08</td></tr><tr><td>ldrPastBids</td><td># of past bids by the lender</td><td>26.89</td><td>55.79</td></tr><tr><td>ldrBidSince</td><td># of days since the lender&#x27;s last bid</td><td>13.73</td><td>46.16</td></tr><tr><td>sameCity</td><td>The lender and the borrower are from the same city</td><td>0.02</td><td>0.15</td></tr><tr><td>Bids</td><td># of prior bids</td><td>2.7</td><td>8.23</td></tr><tr><td>bidsElite</td><td># of prior bids from elite lenders</td><td>0.31</td><td>0.98</td></tr><tr><td>bidsLarge</td><td># of prior large bids (≥ 1000 RMB)</td><td>0.05</td><td>0.39</td></tr><tr><td>isBF</td><td>Lender is a friend of the borrower</td><td>0.0034</td><td>0.06</td></tr><tr><td>isBFoffstrong</td><td>Lender is an offline strong tie of the borrower</td><td>0.00008</td><td>0.009</td></tr><tr><td>isBFoffweak</td><td>Lender is an offline weak tie of the borrower</td><td>0.0002</td><td>0.016</td></tr><tr><td>isBFonline</td><td>Lender is an online friend of the borrower</td><td>0.003</td><td>0.055</td></tr><tr><td>bidsBF</td><td># of prior bids from the borrower&#x27;s friends</td><td>0.16</td><td>1.22</td></tr><tr><td>bidsLF</td><td># of prior bids from the lender&#x27;s friends</td><td>0.08</td><td>0.54</td></tr><tr><td>bidsLFoffstrong</td><td># of prior bids from offline strong ties of the lender</td><td>0.004</td><td>0.08</td></tr><tr><td>bidsLFoffweak</td><td># of prior bids from offline weak ties of the lender</td><td>0.012</td><td>0.16</td></tr><tr><td>bidsLFonline</td><td># of prior bids from online friends of the lender</td><td>0.065</td><td>0.48</td></tr><tr><td>priorTrans</td><td># of prior transactions between lender and borrower</td><td>0.05</td><td>2.68</td></tr><tr><td>bidsCobidders</td><td># of prior bids by lenders who co-bid with the focal lender</td><td>1.47</td><td>4.45</td></tr><tr><td>bidsFriendsBoth</td><td># of prior bids by lenders who are friends of both</td><td>0.01</td><td>0.19</td></tr></table>

## Results

Before estimating our main model, we conducted an analysis of collinearity. The variance inflation factors (VIFs) associated with all variables were below 5, indicating no issue of multicollinearity. The first step results of the Heckman correction are reported in Appendix B<sup>.</sup> We also conducted analyses of overall funding success (available upon request) which indicates a positive correlation with number of friends, consistent with previous findings reported for Prosper (Lin et al. 2013).

We ran five variations of the equation (1). Model 1 includes only the control variables. Model 2 includes the inverse Mills ratio calculated from the Probit model. Model 3 includes our three main explanatory variables for the pipe, prism, and relational herding effects. Model 4 breaks down the pipe and relational herding effects by three mutually exclusive friendship types: offline strong ties, offline weak ties, and online ties. Model 5 tests the robustness of our findings by controlling for prior interactions between the borrower and the lender and co-bids between the lender and prior lenders.

The results of the conditional logit regression are illustrated in Table 3. Among 1,250,426 lending decisions, 849,621 from 8,260 listings were automatically dropped because these listings did not receive any bid. For ease of interpretation, all estimated coefficients are presented in the form of odds ratios. As shown in Table 3, the lending probability increases with the number of days passed, the percentage funded, the number of prior bids, and co-location of the borrower and the lender in the same city. The lending probability decreases with 100 percent funding status, gender (female), education, and the number of friends the lender has. The coefficient of inverse Mills ratio is negative and significant, suggesting a significant selection bias. The negative sign suggests that unobserved factors that increase nonparticipation hazard are negatively correlated with the lending probability.

Table 3. Conditional Logit Regression on the Probability of Lending

<table><tr><td>Variables</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5</td></tr><tr><td># of days passed since listing</td><td>1.088***(0.008)</td><td>1.088***(0.008)</td><td>1.082***(0.008)</td><td>1.082***(0.008)</td><td>1.082***(0.008)</td></tr><tr><td>The percentage of funding completed</td><td>2.119***(0.343)</td><td>2.121***(0.347)</td><td>1.995***(0.320)</td><td>2.000***(0.321)</td><td>2.023***(0.324)</td></tr><tr><td>The listing has reached 100% funding</td><td>0.054***(0.007)</td><td>0.052***(0.007)</td><td>0.052***(0.007)</td><td>0.051***(0.007)</td><td>0.051***(0.006)</td></tr><tr><td>Age of the lender</td><td>1.012***(0.001)</td><td>1.000(0.001)</td><td>1.000(0.001)</td><td>1.000(0.001)</td><td>1.000(0.001)</td></tr><tr><td>Gender of the lender (1 = Female)</td><td>0.678***(0.016)</td><td>0.722***(0.018)</td><td>0.723***(0.018)</td><td>0.722***(0.018)</td><td>0.723***(0.018)</td></tr><tr><td>Education level of the lender</td><td>1.082***(0.008)</td><td>0.978**(0.007)</td><td>0.981**(0.007)</td><td>0.981**(0.007)</td><td>0.981**(0.007)</td></tr><tr><td># of past bids by the lender</td><td>1.006***(0.000)</td><td>1.004***(0.000)</td><td>1.004***(0.000)</td><td>1.004***(0.000)</td><td>1.004***(0.000)</td></tr><tr><td># of days since the lender&#x27;s last bid</td><td>0.991***(0.001)</td><td>1.006***(0.000)</td><td>1.006***(0.000)</td><td>1.006***(0.000)</td><td>1.006***(0.000)</td></tr><tr><td># of friends the lender has</td><td>0.998***(0.000)</td><td>0.996***(0.000)</td><td>0.995***(0.000)</td><td>0.995***(0.000)</td><td>0.995***(0.000)</td></tr><tr><td>Lender and borrower are from the same city</td><td>1.560***(0.060)</td><td>1.570***(0.062)</td><td>1.531***(0.061)</td><td>1.500***(0.060)</td><td>1.506***(0.060)</td></tr><tr><td># of prior bids</td><td>1.014**(0.004)</td><td>1.016***(0.004)</td><td>1.021***(0.005)</td><td>1.022***(0.005)</td><td>1.016**(0.005)</td></tr><tr><td># of prior bids from elite lenders</td><td>0.995(0.019)</td><td>0.986(0.018)</td><td>1.012(0.018)</td><td>1.012(0.018)</td><td>1.001(0.017)</td></tr><tr><td># of prior large bids (≥ 1000 RMB)</td><td>0.866***(0.036)</td><td>0.865***(0.036)</td><td>0.883**(0.037)</td><td>0.882**(0.037)</td><td>0.889**(0.036)</td></tr><tr><td>Day of week dummies</td><td>included</td><td>included</td><td>included</td><td>included</td><td>included</td></tr><tr><td>Inverse Mills ratio</td><td></td><td>0.313***(0.008)</td><td>0.314***(0.008)</td><td>0.312***(0.008)</td><td>0.330***(0.009)</td></tr><tr><td>The lender is a friend of the borrower</td><td></td><td></td><td>3.512***(0.183)</td><td></td><td></td></tr><tr><td>- Lender is an offline strong-tie of the borrower</td><td></td><td></td><td></td><td>18.336***(7.753)</td><td>18.147***(7.622)</td></tr><tr><td>- Lender is an offline weak-tie of the borrower</td><td></td><td></td><td></td><td>5.272***(0.914)</td><td>5.248***(0.911)</td></tr><tr><td>- Lender is an online friend of the borrower</td><td></td><td></td><td></td><td>3.245***(0.176)</td><td>3.239***(0.177)</td></tr><tr><td># of prior bids from friends of the borrower</td><td></td><td></td><td>0.945***(0.010)</td><td>0.946***(0.010)</td><td>0.947***(0.011)</td></tr><tr><td># of prior bids from friends of the lender</td><td></td><td></td><td>0.997(0.009)</td><td></td><td></td></tr><tr><td>- # of prior bids from offline strong ties of the lender</td><td></td><td></td><td></td><td>1.157***(0.046)</td><td>1.151***(0.046)</td></tr><tr><td>- # of prior bids from offline weak ties of the lender</td><td></td><td></td><td></td><td>1.106***(0.022)</td><td>1.101***(0.022)</td></tr><tr><td>- # of prior bids from online friends of the lender</td><td></td><td></td><td></td><td>0.975**(0.009)</td><td>0.967***(0.009)</td></tr><tr><td># of bids from friends of both</td><td></td><td></td><td>1.010(0.018)</td><td>1.017(0.019)</td><td>1.025(0.020)</td></tr><tr><td># of prior transactions between lender and borrower</td><td></td><td></td><td></td><td></td><td>0.999**(0.001)</td></tr><tr><td># of prior bids by lenders who co-bid with the lender</td><td></td><td></td><td></td><td></td><td>1.012***(0.003)</td></tr><tr><td>Log-likelihood</td><td>-67879.7</td><td>-65642.8</td><td>-65190.3</td><td>-65131.3</td><td>-65101.8</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.105</td><td>0.134</td><td>0.140</td><td>0.141</td><td>0.141</td></tr><tr><td>N</td><td>400805</td><td>400805</td><td>400805</td><td>400805</td><td>400805</td></tr></table>

\*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001. All reported coefficients are in odds ratios.

The number of bids by elite lenders does not have a significant impact on subsequent lending probabilities. This is likely because the platform is still new and the elite lender has not achieved the true elite status as those in the offline world. The number of large bids has a significant negative effect on subsequent lending probabilities. While large bids may signal strong confidence in a listing, they may also signal a lack of experience and idiosyncrasy.

## The Pipe Effect

Consistent with our expectation, being a friend of a borrower is associated with higher probability of lending. However, the pipe effect differs dramatically by friendship types: an offline strong tie, an offline weak tie, and an online friend are 17.3 times, 4.3 times, and 2.2 times more likely to offer a bid than a stranger, respectively. Wald tests show that an offline strong tie indeed has a stronger effect than an offline weak-tie (p = 0.006, χ² = 7.66, H1 is supported) and an offline weak-tie has a stronger effect than an online friend (p = 0.007, χ² = 7.26, H2 is supported). Each prior bid increases the likelihood of lending by 2.1 percent (Model 3), suggesting an anonymous herding effect among potential lenders (H4 is supported).

## The Prism Effect

A bid by a friend of the borrower has a significant marginal effect of -5.5 percent (Model 3). This suggests that a friend bid has a negative effect relative to an anonymous bid (H3 is supported). Noting a baseline effect of 2.1 percent by any prior bid (Model 3), we conclude that a bid by a friend of the borrower has an overall negative effect of -3.4 percent on each subsequent potential lender.

## The Relational Herding Effect

The coefficient for the number of prior bids by a lender’s friends is insignificant, suggesting that, on average, a lender is no more likely to follow a friend than a stranger. However, a breakdown by friendship types suggests a different story (Model 4): A prior bid by an offline strong tie of the lender has a positive effect of 15.7 percent and that by an offline weak tie has a positive effect of 10.6 percent. However, a prior bid by an online friend has a negative effect of -2.5 percent. The difference between offline strong ties and offline weak ties is not significant $( \mathfrak { p } = 0 . 3 , \chi ^ { 2 } = 1 . 0 7$ , H5 is not supported), but the difference between offline weak ties and online friends is significant $( { \mathrm { p } } < 0 . 0 0 1 , \chi ^ { 2 } = 3 3 . 6 ,$ , H6 is supported). These results provide evidence of relational herding: lenders are more likely to follow their offline friends than online friends and strangers. Our finding adds to the emerging body of evidence that online friends are less influential than offline friends (Bond et al. 2012).

We defer all robustness checks, including the discussion of Model 5 findings, to Appendix C.

## Concluding Remarks

The proliferation of social media technologies has led to many online social-economical platforms such as peer-to-peer lending, crowd funding, social commerce, and social networking sites. These platforms facilitate economic exchanges between friends and collective decision making by connected individuals through the pipe, prism, and relational herding effects. Several platforms are proactively pursuing these effects. For example, Linkedin actively seeks endorsements of its members from their friends. Facebook recently introduced social advertising, which highlighted friend endorsements in the ad campaign messages. These trends emphasize the importance of understanding the nuances of friendship relations in economic transactions.

Overall, our results confirm that friendships affect economic decisions—as pipes, prisms, and relational herding signals. As pipes, friends of borrowers are more likely to offer loans than strangers. However, as prisms, endorsements by friends of the borrower have a negative effect on subsequent lenders. We extend the theory and research on herding (Banerjee 1992; Bikhchandani et al. 1992; Lee and Lee 2012) by offering the concept of relational herding: people are more likely to follow the “wisdom of crowds” when those crowds include friends rather than strangers. In particular, lenders have a stronger tendency to follow their offline friends than online friends or strangers.

Our results add to the nascent empirical research on P2P lending and crowd funding. Our research complements the more borrower-focused research of Freedman and Jin (2008)

and Lin et al. (2013) who report associations between friendship and aggregate outcomes such as funding success and defaults. Although a boundary condition of our study is the Chinese context and possible cultural differences (see Cialdini et al. 1999), we find similar aggregate-level results across cultures, reinforcing the earlier findings that friendships are associated with aggregate successful funding. On the other hand, our lender-level analyses provide more nuanced findings.

Our results pose an interesting dilemma for borrowers. On the one hand, by making more friends, they get more friend bids. On the other hand, these friend bids turn away other potential lenders who are strangers, including those with many offline friends. This suggests alternative strategies for borrowers: A borrower may either rely on friend bids at the peril of alienating total strangers, or rely on the “kindness of strangers.” Furthermore, we learn of differential effects for offline strong-tie friends, offline weak-tie friends, and online friends, consistent with the popular notion that offline relationships are stronger and more trustworthy. These findings suggest that it is necessary to conceptualize and measure friendship ties at the more granular level in online social network studies. Thus, our study’s findings provide additional insights that modify previously suggested interpretations based on aggregate outcomes while reinforcing the overall positive effect of friendships in P2P lending.

Our finding of the negative prism effect suggests a distrust of friend bid by third parties. A P2P lending platform may increase the number of bids by removing friend bid labeling. Additionally, our findings on relational herding effects suggest that the platform can increase bidding activities by making it easy for lenders to follow their offline friends. Our findings of differential effects by friendship types suggest that P2P lending platforms may prioritize loan and friend-bid notifications by friendship types (e.g., by highlighting loans and bids from off-line friends). We caution that the above recommendations are based on their effects on lenders and tests of their impact on loan default rates and long-term health of the platform are strongly recommended.

While previous network studies (Kilduff and Krackhardt 1994; Podolny 2001; Stuart et al. 1999) have focused on the prism effects of associating with high status others, ours is the first network study to explore the prism effects of friendship. We add to the literature on cognitive social networks by noting that the perception of friendship ties may have an adverse effect. Although we have no direct measures of cognitive assessments, our findings support the view that friends of borrowers feel a social obligation to endorse or support their friends. Likewise, our findings support the view that potential lenders consider bids by borrower’s friends as a signal of social obligation, coupled with an emotional bias, such that potential lenders are less likely to offer a bid. However, potential lenders view bids by their own friends as a positive signal of economic value. My own friends can be trusted to make sound economic decisions, but friends of borrowers cannot.

Our results may also have broader implications for such diverse topics as word-of-mouth marketing (Godes and Mayzlin 2009) and political campaigns (Bond et al. 2012). Marketing and political campaigns designed to seed and diffuse favorable information among peers are well-advised to consider how endorsements by perceived friends of the marketer or candidate affect subsequent behavior. While endorsements by friends are easier to acquire, such endorsements may be perceived as resulting from emotional bias and social obligation and create negative prism effects among third parties. On the other hand, endorsements by strangers with many friends may fuel the spread of positive reactions from others.

## Limitations

We rely on self-reported friendship types. Although such friendships require acceptance by the other party, we cannot rule out the possibility that some members of P2P lending networks may strategically forge friendship relations with strangers for economic or social benefits (e.g., funding success or a large number of friends). Thus, further research is required regarding the exact nature of these relationships. While we find an overall negative prism effect, it is possible that potential lenders weigh both positive and negative signals when considering the prism effects of bids from friends of the borrower. Finally, our findings on the pipe, prism, and relational herding effects are based on the existing platform design. They may not be immune to changes in the details of the platform design. Future research should test how different ways of supporting friendship relations may affect these effects.

## Acknowledgments

The authors wish to thank seminar participants at University of Texas at Dallas, University of Kentucky, Indiana University, University of Minnesota, George Washington University, Rensselaer Polytechnic Institute, Soochow University, Tsinghua University, China Summer Workshop on Information Management (CSWIM), Statistical Challenges in Electronic Commerce Research (SCECR), and Symposium on Financial Intelligence and Risk Management and

International Workshop of Electronic Commerce (FIRM-EPECC) for their valuable feedback. This research is supported by the China Social Science Foundation (Grant No. 11AZD077), National Natural Science Foundation of China (Grant No. 71302008, 71371076), and the Laboratory for Financial Intelligence and Financial Engineering at the Southwestern University of Finance and Economics.

## References

Akerlof, G. A. 1970. “The Market for ‘Lemons’: Quality Uncertainty and the Market Mechanism,” Quarterly Journal of Economics (84:3), pp. 488-500.

Argyle, M., and Henderson, M. 1984. “The Rules of Friendship,” Journal of Social and Personal Relationships (1:2), pp. 211-237.

Arnott, R., and Stiglitz, J. 1991. “Moral Hazard and Nonmarket Institutions: Dysfunctional Crowding Out of Peer Monitoring?,” The American Economic Review (81:1), pp. 179-190.

Banerjee, A. V. 1992. “A Simple Model of Herd Behavior,” The Quarterly Journal of Economics (107:3), pp. 797-817.

Bapna, R., Gupta, A., Rice, S., and Sundararajan, A. 2011. “Trust, Reciprocity and the Strength of Social Ties: An Online Social Network based Field Experiment,” in Proceedings of Conference on Information Systems and Technology, Charlotte, NC.

Besley, T., and Coate, S. 1995. “Group Lending, Repayment Incentives and Social Collateral,” Journal of Development Economics (46:1), pp. 1-18.

Bikhchandani, S., Hirshleifer, D., and Welch, I. 1992. “A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades,” Journal of Political Economy (100:5), pp. 992-1026.

Bikhchandani, S., and Sharma, S. 2000. “Herd Behavior in Financial Markets,” IMF Staff Papers (47:3), pp. 279-310.

Bond, R. M., Fariss, C. J., Jones, J. J., Kramer, A. D. I., Marlow, C., Settle, J. E., and Fowler, J. H. 2012./ “A 61-Million-Person Experiment in Social Influence and Political Mobilization,” Nature (489:7415), pp. 295-298.

Brass, D. J. 2012. “A Social Network Perspective on Organizational Psychology,” in The Oxford Handbook of Organizational Psychology, S. W. J. Kozlowski (ed.), New York: Oxford University Press.

Brass, D. J., Galaskiewicz, J., Greve, H. R., and Tsai, W. P. 2004. “Taking Stock of Networks and Organizations: A Multilevel Perspective,” Academy of Management Journal (47:6), pp. 795-817.

Burtch, G., Ghose, A., and Wattal, S. 2013. “An Empirical Examination of the Antecedents and Consequences of Contribution Patterns in Crowd-Funded Markets,” Information Systems Research (24:3), pp. 499-519.

Cai, H., Chen, Y., and Fang, H. 2009. “Observational Learning: Evidence from a Randomized Natural Field Experiment,” American Economic Review (99:3), pp. 864-882.

Cialdini, R. B. 1993. Influence: The Psychology of Persuasion, New York: HarperCollins, 1993.

Cialdini, R. B., Wosinska, W., Barrett, D. W., Butner, J., and Gornik-Durose, M. 1999. “Compliance with a Request in Two Cultures: The Differential Influence of Social Proof and

Commitment/Consistency on Collectivists and Individualists,” Personality and Social Psychology Bulletin (25:10), pp. 1242-1253.

Cummings, J. N., Butler, B., and Kraut, R. 2002. “The Quality of Online Social Relationships,” Communications of the ACM (45:7), pp. 103-108.

Devenow, A., and Welch, I. 1996. “Rational Herding in Financial Economics,” European Economic Review (40:3-5), pp. 603-615.

Donath, J., and Boyd, D. 2004. “Public Displays of Connection,” BT Technology Journal (22:4), pp. 71-82.

Duan, W., Gu, B., and Whinston, A. B. 2009. “Informational Cascades and Software Adoption on the Internet: An Empirical Investigation,” MIS Quarterly (33:1), pp. 23-48.

Everett, C. R. 2010. “Group Membership, Relationship Banking and Loan Default Risk: The Case of Online Social Lending, Purdue University Working Paper.

Festinger, L. 1962. A Theory of Cognitive Dissonance, Stanford, CA: Stanford University Press.

Freedman, S., and Jin, G. Z. 2008. “Do Social Networks Solve Information Problems for Peer-to-Peer Lending? Evidence from Prosper.com,” NET Institute Working Paper.

Friedkin, N. E., and Johnsen, E. C. 2011. Social Influence Network Theory: A Sociological Examination of Small Group, New York: Cambridge University Press.

Godes, D., and Mayzlin, D. 2009. “Firm-Created Word-of-Mouth Communication: Evidence from a Field Test,” Marketing Science (28:4), pp. 721-739.

Granovetter, M. S. 1973. “The Strength of Weak Ties,” American Journal of Sociology (78:6), pp. 1360-1380.

Granovetter, M. S. 1985. “Economic Action and Social Structure: The Problem of Embeddedness,” American Journal of Sociology (91:3), pp. 481-510.

Granovetter, M. S. 2005. “The Impact of Social Structure on Economic Outcomes,” Journal of Economic Perspectives (19:1), pp. 33-50.

Greene, W. H. 2002. Econometric Analysis, Upper Saddle River, NJ: Prentice Hall.

Heider, F. 1958. The Psychology of Interpersonal Relations, New York: Wiley.

Herzenstein, M., Dholakia, U. M., and Andrews, R. L. 2011. “Strategic Herding Behavior in Peer-to-Peer Loan Auctions,” Journal of Interactive Marketing (25:1), pp. 27-36.

Kane, G. C., Alavi, M., Labianca, G., and Borgatti, S. P. 2014. “What’s Different about Social Media Networks? A Framework and Research Agenda,” MIS Quarterly (38:1), pp. 275-304.

Kilduff, M., and Krackhardt, D. 1994. “Bringing the Individual Back In: A Structural Analysis of the Internal Market for Reputation in Organizations,” Academy of Management Journal (37:1), pp. 87-108.

Krumme, K. A., and Herrero, S. 2009. “Lending Behavior and Community Structure in an Online Peer-to-Peer Economic Network,” in Proceedings of the International Conference on Computational Science and Engineering, Los Alamitos, CA: IEEE Computer Society, pp. 613-618.

Kumar, S. 2007. “Bank of One: Empirical Analysis of Peer-to-Peer Financial Marketplaces,” in Proceedings of the $I 3 ^ { t h }$ Americas Conference on Information Systems, Keystone, CO.

Lee, E., and Lee, B. 2012. “Herding Behavior in Online P2P Lending: An Empirical Investigation,” Electronic Commerce Research and Applications (11:4), pp. 485-503.

Lin, M., Prabhala, N. R., and Viswanathan, S. 2013. “Judging Borrowers by the Company They Keep: Friendship Networks and Information Asymmetry in Online Peer-to-Peer Lending,” Management Science (59:1), pp. 17-35.

Lin, M., and Viswanathan, S. 2013. “Home Bias in Online Investments: An Empirical Study of an Online Crowd Funding Market,” Management Science, Forthcoming.

Lu, Y., Gu, B., Ye, Q., and Sheng, Z. 2012. “Social Influence and Defaults Peer-to-Peer Lending Networks,” in Proceedings of the 33<sup>rd</sup> International Conference on Information Systems, Orlando.

Mesch, G., and Talmud, I. 2006. “The Quality of Online and Offline Relationships: The Role of Multiplexity and Duration of Social Relationships,” Information Society (22:3), pp. 137-148.

Newcomb, T. M. 1961. The Acquaintance Process, New York: Holt, Reinhart & Winston.

Oestreicher-Singer, G., and Sundararajan, A. 2012. “The Visible Hand? Demand Effects of Recommendation Networks in Electronic Markets,” Management Science (58:11), pp. 1963-1981.

Podolny, J. M. 2001. “Networks as the Pipes and Prisms of the Market,” American Journal of Sociology (107:1), pp. 33-60.

Polanyi, K. 1944. The Great Transformation: The Political and Economic Origins of Our Time, Boston: Beacon Press.

Silver, A. 1990. “Friendship in Commercial Society: Eighteenth Century Social Theory and Modern Sociology,” American Journal of Sociology (95:6), pp. 1474-1504.

Simonsohn, U., and Ariely, D. 2008. “When Rational Sellers Face Non-Rational Buyers: Evidence from Herding on eBay,” Management Science (54:9), pp. 1624-1637.

Spence, M. 2002. “Signaling in Retrospect and the Informational Structure of Markets,” American Economic Review (92:3), pp. 434-459.

Stuart, T. E., Hoang, H., and Hybels, R. C. 1999. “Interorganizational Endorsements and the Performance of Entrepreneurial Ventures,” Administrative Science Quarterly (44:2), pp. 315-349.

Uzzi, B. 1999. “Embeddedness in the Making of Financial Capital: How Social Relations and Networks Benefit Firms Seeking Financing,” American Sociological Review (64:4), pp. 481-505.

Valente, T. W. 1999. Network Models of the Diffusion of Innovations, Cresskill, NJ: Hampton Press.

Welch, I. 1992. “Sequential Sales, Learning, and Cascades,” Journal of Finance (47:2), pp. 695-732.

Yum, H., Lee, B., and Chae, M. 2012. “From the Wisdom of Crowds to My Own Judgment in Microfinance through Online Peer-to-Peer Lending Platforms,” Electronic Commerce Research and Applications (11:5), pp. 469-483.

Zhang, J., and Liu, P. 2012. “Rational Herding in Microloan Markets,” Management Science (58:5), pp. 892-912.

Zvilichovsky, D., Inbar, Y., and Barzilay, O. 2013. “Playing Both Sides of the Market: Success and Reciprocity on Crowdfunding Platforms,” Working Paper, Recanati Business School, Tel Aviv University.

## About the Authors

De Liu is an associate professor of Information and Decision Sciences at the Carlson School of Management, University of Minnesota, and a member of LINKS Center for Social Network Analysis (http://linkscenter.org). He received his Ph.D. in Management Science and Information Systems from University of Texas at Austin. His research interests include analysis and design of Internet-based auctions, contests, social systems, and gamification. His research has appeared in journals such as MIS Quarterly, Information Systems Research, Journal of Marketing, and Journal of Market Research.

Daniel J. Brass is J. Henning Hilliard Professor of Innovation Management and director of the LINKS Center for Social Network Analysis (http://linkscenter.org) at the Gatton College of Business and Economics, University of Kentucky. He received his Ph.D. in Business Administration from University of Illinois. He has published articles in such journals as Science, Administrative Science Quarterly, Academy of Management Journal, Academy of Management Review, Journal of Applied Psychology, Organization Science, and Information Systems Research, as well as numerous book chapters. His research focuses on the antecedents and consequences of social networks in organizations.

Yong Lu is an associate professor of information sciences and technology at the Pennsylvania State University. His research interests include Internet finance, complex adaptive systems, social media, and information security. His research articles have appeared in MIS Quarterly, Decision Support Systems, Journal of the American Society for Information Science and Technology, Computers and Education, Journal of Computer Information Systems, and E-Markets, among others.

Dongyu Chen is an associate professor at the Dongwu Business School, Soochow University. His research interests include the implementation of IS innovations and the adoption of information systems. He has published papers in Journal of Global Information Technology Management as well as the proceedings of the Pacific Asia Conference on Information Systems.

# FRIENDSHIPS IN ONLINE PEER-TO-PEER LENDING:PIPES, PRISMS, AND RELATIONAL HERDING

De Liu Department of Information and Decision Sciences, Carlson School of Management, University of Minnesota, Minneapolis, MN 55455 U.S.A. {liux3269@umn.edu}

Daniel J. Brass LINKS Center for Social Network Analysis, Gatton College of Business and Economics, University of Kentucky, Lexington, KY 40506 U.S.A. {dbrass@uky.edu}

Yong Lu Institute of Internet Finance & Institute of Chinese Financial Studies, Southwestern University of Finance and Economics, CHINA, and Information Science & Technology, The Pennsylvania State University, 76 University Drive, Hazelton, PA 18202 U.S.A. {ericlu@psu.edu}

Dongyu Chen Dongwu Business School, Soochow University, No. 50, Donghuan Road, Suzhou City, Jiangsu Province, PEOPLE’S REPUBLIC OF CHINA {chendongyu@suda.edu.cn}

## Appendix A

## The Conditional Logit Model

Let $L _ { i j }$ be shorthand for bidyes<sub>ij</sub> and $L _ { j } = \left( L _ { 1 j } , L _ { 2 j } , . . . , L _ { T _ { j } j } \right)$ denote the observed $T L _ { j }$ decisions throughout the lifespan of listing j. Suppose $k _ { j }$ of these decisions are positive decisions. Let $d _ { j } = \left( d _ { 1 j } , d _ { 2 j } , \ldots , d _ { T _ { j } j } \right)$ be a vector of decisions subject to $\textstyle \sum _ { i = 1 } ^ { T _ { j } } d _ { i j } = k _ { j }$ and S<sub>j</sub> be a set of all such vectors. If we assume the error term $\varepsilon _ { i j }$ follows an i.i.d. type I extreme value distribution, then the conditional probability is

$$
\operatorname * {P r} \left(L _ {j} \mid \sum_ {i = 1} ^ {T _ {j}} L _ {i j} = k _ {j}\right) = \frac {\sum_ {e} \sum_ {i = 1} ^ {T _ {j}} L _ {i j} \left(x _ {i j} \alpha + Y _ {i} \beta + z _ {j \gamma}\right)}{\sum_ {d _ {j} \in S _ {j}} e \sum_ {i = 1} ^ {T _ {j}} d _ {i j} \left(x _ {i j} \alpha + Y _ {i} \beta + z _ {j \gamma}\right)} = \frac {\sum_ {e} \sum_ {i = 1} ^ {T _ {j}} L _ {i j} \left(x _ {i j} \alpha + Y _ {i} \beta\right)}{\sum_ {d _ {j} \in S _ {j}} e \sum_ {i = 1} ^ {T _ {j}} d _ {i j} \left(x _ {i j} \alpha + Y _ {i} \beta\right)}\tag{2}
$$

Notice that the listing specific effects $Z _ { j \gamma }$ cancel out in the conditional probability. This suggests that we can recover the rest of model parameters without knowing $Z _ { j } .$ . A conditional logit model estimates the model parameters and by maximizing the likelihood function

$$
\ln L = \sum_ {j = 1} ^ {n} \operatorname * {P r} \left(L _ {j} \mid \sum_ {i = 1} ^ {T _ {j}} L _ {i j} = k _ {j}\right)\tag{3}
$$

where n is the number of listings.

## Appendix B

## Heckman Correction’s First Step

<table><tr><td colspan="2">Table B1. Probit Regression on the Probability of Being Active</td></tr><tr><td>Variables</td><td>Coefficients (se)</td></tr><tr><td rowspan="2">Log # of past bids by the lender</td><td>0.219***</td></tr><tr><td>(0.011)</td></tr><tr><td rowspan="2">The lender has past bids</td><td>-0.835***</td></tr><tr><td>(0.028)</td></tr><tr><td rowspan="2">Log days since the last bid by the lender</td><td>-0.537***</td></tr><tr><td>(0.006)</td></tr><tr><td rowspan="2">Age of the lender</td><td>0.009***</td></tr><tr><td>(0.001)</td></tr><tr><td rowspan="2">Gender of the lender (1 = Female)</td><td>0.020</td></tr><tr><td>(0.021)</td></tr><tr><td rowspan="2">Education level of the lender</td><td>0.088***</td></tr><tr><td>(0.009)</td></tr><tr><td rowspan="2">The lender is married</td><td>0.055*</td></tr><tr><td>(0.022)</td></tr><tr><td rowspan="2">The lender&#x27;s marriage information is missing</td><td>0.197***</td></tr><tr><td>(0.034)</td></tr><tr><td rowspan="2"># of children of the lender</td><td>-0.032*</td></tr><tr><td>(0.015)</td></tr><tr><td rowspan="2"># of day since the lender joined the platform</td><td>-0.000**</td></tr><tr><td>(0.000)</td></tr><tr><td rowspan="2"># of friends the lender has</td><td>-0.001</td></tr><tr><td>(0.001)</td></tr><tr><td rowspan="2"># of concurrent listings</td><td>0.001***</td></tr><tr><td>(0.000)</td></tr><tr><td rowspan="2"># of low-risk concurrent listings</td><td>0.005***</td></tr><tr><td>(0.000)</td></tr><tr><td rowspan="2">Constant</td><td>-0.826***</td></tr><tr><td>(0.056)</td></tr><tr><td>Log-likelihood</td><td>-2491965</td></tr><tr><td>Pseudo R2</td><td>0.643</td></tr><tr><td>N</td><td>2694688</td></tr></table>

\*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001. Month dummies were also included.  
Estimated coefficients and standard errors adjusted by sampling weights.

## Appendix C

## Robustness Checks

To address concerns related to random sampling, we ran the same analysis using two months and five months of data and the results did not change. We also drew different random samples of the data and obtained consistent results across samples.

To make sure parameter estimates are not biased by potential interaction between the pipe and the other two effects, we ran analysis using only potential lenders who are not friends of the borrower and the results did not change.

To address the concern that friendships merely reflect the history of past interactions and have no independent effect, we controlled for past transactions between the borrower and the lender and between the lender and prior lenders in Model 5. Our main results hold after introducing these additional controls.

As an alternative specification, we also ran robust logit regressions with two dimensional clustering by listings and lenders (Table C1, Model 6). This model accounts for correlations among decisions by the same lender but is subject to omitted-variable bias. Besides the controls fo conditional logit models, we included several listing/borrower characteristics as controls, such as borrower credit grade, loan purpose, borrowing amount, interest rate, borrower age, gender, education, borrowing history, and authentication. The results are similar to existing ones, although the robust logit reported greater pipe (314.6%), prism (-7.5%), anonymous herding (9.1%), and relational herding (5.0%) effects, which may reflect the omitted-variable bias.

<table><tr><td colspan="4">Table C1. Additional Robustness Checks</td></tr><tr><td></td><td>Model 6Robust logit</td><td>Model 7WeightedConditional Logit</td><td>Model 8Conditional Logit on listings with &gt;25 clicks</td></tr><tr><td># of prior bids</td><td>1.091***(0.004)</td><td>1.045***(0.007)</td><td>1.061***(0.006)</td></tr><tr><td>Lender is an offline strong-tie of the borrower</td><td>16.680***(6.290)</td><td>94.650***(93.806)</td><td>38.509***(41.866)</td></tr><tr><td>Lender is an offline weak-tie of the borrower</td><td>7.565***(1.591)</td><td>4.271***(1.298)</td><td>5.529***(1.436)</td></tr><tr><td>Lender is an online friend of the borrower</td><td>3.807***(0.238)</td><td>3.434***(0.315)</td><td>3.692***(0.287)</td></tr><tr><td># of prior bids from the borrower&#x27;s friends</td><td>0.925***(0.012)</td><td>0.879***(0.021)</td><td>0.881***(0.017)</td></tr><tr><td># of prior bids from offline strong-ties of the lender</td><td>1.564***(0.080)</td><td>1.151(0.089)</td><td>0.870*(0.057)</td></tr><tr><td># of prior bids from offline weak-ties of the lender</td><td>1.143***(0.032)</td><td>1.154***(0.035)</td><td>1.203***(0.040)</td></tr><tr><td># of prior bids from online friends of the lender</td><td>1.022(0.013)</td><td>0.954**(0.018)</td><td>0.938***(0.017)</td></tr><tr><td>Log-likelihood</td><td>-91339.30</td><td>-6317171.4</td><td>-21086.6</td></tr><tr><td>Adjust R-squared</td><td>0.302</td><td>0.130</td><td>0.156</td></tr><tr><td>N</td><td>1250426</td><td>239444</td><td>136745</td></tr></table>

$^ { \star } \mathsf { p } < 0 . 0 5 , ^ { \star \star } \mathsf { p } < 0 . 0 1 , ^ { \star \star \star } \mathsf { p } < 0 . 0 0 1$ . All control variables are omitted for brevity. Full results available upon request. Model 6 clusters error by listings and lenders and controls for listing/borrower characteristics including credit grades, loan purposes, interest rate, borrowing amount, listing duration, number of repayments, borrower age, gender, education, past listings, past loans, other loans, identity authentication (via mobile or video), diploma authentication, borrower’s number of friends, region dummies.

The lack of a bid from an active lender may be because the lender made an implicit negative decision. As an implicit negative decision does not require a listing’s details, including such a case may bias our estimations. The Heckman selection may mitigate such a bias to some extent because the propensity of being active may be correlated with the propensity to evaluate a listing. To further address this potential bias, we ran two additional robustness tests. First, we used the number of clicks on a listing as an “importance” factor for a weighted conditional logit model. The rationale is that a negative decision on a listing with many clicks is more likely an explicit negative decision, thus it should weigh more. Similarly, we also ran analyses on listings with at least 25 clicks (i.e., the mean number of clicks). The two robustness checks yield qualitatively similar results as our main findings (Table C15, Models 7 and 8)

To address the concern that our choice of bid timing may be a source of bias, we constructed a sample using the “last-sight” rule under the assumption that non-bidders repeatedly checked a listing and waited until the last sight to decide not to bid on the list. This alternative data construction depressed some of the coefficients for control variables (e.g., for percentage completed and number of days since listing) but our main findings remained qualitatively the same (results available upon request). Finally, to rule out the possibility that lenders increase their lending probability but decrease lending amount, we ran a fixed-effect model on lending amount while taking into account left-censoring. Our results suggest a positive pipe effect on lending amounts but no significant prism or relational herding effect. Thus our qualitative results do not change after taking lending amount into account.

## Appendix D

## Correlation Table

<table><tr><td></td><td>Variable</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td></tr><tr><td>1</td><td>The lender has bid on the listing</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td># of days passed since listing</td><td>-.03</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>The percentage of funding completed</td><td>.21</td><td>.12</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>The listing has reached 100% funding</td><td>.05</td><td>.13</td><td>.78</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>Age of the lender</td><td>.02</td><td>-.01</td><td>.00</td><td>.00</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>Gender of the lender (1=Female)</td><td>-.03</td><td>.03</td><td>-.01</td><td>.00</td><td>-.08</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>Education level of the lender</td><td>.02</td><td>-.02</td><td>.00</td><td>.00</td><td>.03</td><td>-.08</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td># of past bids by the lender</td><td>.15</td><td>-.10</td><td>.03</td><td>-.01</td><td>.12</td><td>-.12</td><td>.12</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9</td><td># of days since the lender&#x27;s last bid</td><td>-.03</td><td>.04</td><td>.01</td><td>.01</td><td>-.05</td><td>.04</td><td>-.05</td><td>-.11</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>Lender and borrower are from the same city</td><td>.03</td><td>-.01</td><td>.02</td><td>.01</td><td>.00</td><td>-.01</td><td>.02</td><td>.02</td><td>-.01</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11</td><td># of prior bids</td><td>.27</td><td>.12</td><td>.82</td><td>.63</td><td>.00</td><td>-.01</td><td>.00</td><td>.05</td><td>.01</td><td>.02</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12</td><td># of prior bids from elite lenders</td><td>.17</td><td>-.07</td><td>.26</td><td>.09</td><td>.02</td><td>-.04</td><td>.01</td><td>.17</td><td>.02</td><td>.02</td><td>.45</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13</td><td># of prior large bids (&gt;=1000 RMB)</td><td>.12</td><td>.06</td><td>.53</td><td>.41</td><td>.00</td><td>.00</td><td>.00</td><td>-.01</td><td>.00</td><td>.01</td><td>.55</td><td>.08</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>14</td><td>Lender is an offline strong-tie of the borrower</td><td>.03</td><td>.00</td><td>.01</td><td>.00</td><td>.00</td><td>.00</td><td>.00</td><td>.01</td><td>.00</td><td>.02</td><td>.01</td><td>.00</td><td>.00</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>Lender is an offline weak-tie of the borrower</td><td>.04</td><td>-.01</td><td>.01</td><td>.01</td><td>.00</td><td>.00</td><td>.00</td><td>.02</td><td>.00</td><td>.02</td><td>.02</td><td>.02</td><td>.01</td><td>.00</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>16</td><td>Lender is an online friend of the borrower</td><td>.12</td><td>-.03</td><td>.04</td><td>.01</td><td>.01</td><td>-.02</td><td>.01</td><td>.06</td><td>-.01</td><td>.01</td><td>.07</td><td>.09</td><td>.03</td><td>.00</td><td>.00</td><td>1</td><td></td><td></td><td></td></tr><tr><td>17</td><td># of prior bids from friends of the borrower</td><td>.14</td><td>-.01</td><td>.30</td><td>.17</td><td>.00</td><td>-.01</td><td>.00</td><td>.04</td><td>.00</td><td>.02</td><td>.50</td><td>.39</td><td>.36</td><td>.01</td><td>.05</td><td>.11</td><td>1</td><td></td><td></td></tr><tr><td>18</td><td># of prior bids from offline strong ties of the lender</td><td>.07</td><td>-.01</td><td>.05</td><td>.03</td><td>.01</td><td>-.02</td><td>.02</td><td>.14</td><td>-.01</td><td>.02</td><td>.07</td><td>.07</td><td>.03</td><td>.01</td><td>.02</td><td>.03</td><td>.04</td><td>1</td><td></td></tr><tr><td>19</td><td># of prior bids from offline weak ties of the lender</td><td>.08</td><td>.00</td><td>.09</td><td>.05</td><td>.01</td><td>-.01</td><td>.03</td><td>.11</td><td>-.01</td><td>.02</td><td>.12</td><td>.13</td><td>.06</td><td>.01</td><td>.02</td><td>.04</td><td>.09</td><td>.06</td><td>1</td></tr><tr><td>20</td><td># of prior bids from online friends of the lender</td><td>.17</td><td>-.01</td><td>.22</td><td>.13</td><td>.03</td><td>-.03</td><td>.03</td><td>.21</td><td>-.03</td><td>.03</td><td>.31</td><td>.30</td><td>.14</td><td>.01</td><td>.05</td><td>.14</td><td>.23</td><td>.08</td><td>.14</td></tr></table>

\*Significant numbers (p < .05) are in bold.
