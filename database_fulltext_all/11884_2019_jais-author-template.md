---
otero_id: 11884
otero_key: "EP2762R9"
title: "JAIS Author Template"
authors: ""
year: "2019"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1.jais.00536"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
ISSN 1536-9323

# An Economic Analysis of Consumer Learning on Entertainment Shopping Websites

Jin Li<sup>1</sup>, Zhiling Guo<sup>2</sup>, Geoffrey Tso<sup>3</sup> <sup>1</sup>Xidian University, Xi’an, China, jinli@xidian.edu.cn <sup>2</sup>Singapore Management University, Singapore, zhilingguo@smu.edu.sg <sup>3</sup>City University of Hong Kong, China, msgtso@cityu.edu.hk

## Abstract

Online entertainment shopping, normally supported by the pay-to-bid auction mechanism, represents an innovative business model in e-commerce. Because the unique selling mechanism combines features of shopping and online auction, consumers expect both monetary return and entertainment value from their participation. We propose a dynamic structural model to analyze consumer behaviors on entertainment shopping websites. The model captures the consumer learning process, based both on individual participation experiences and also on observational learning of historical auction information. We estimate the model using a large data set from an online entertainment shopping website. Results show that consumers’ initial participation incentives mainly come from a significant overestimation of the entertainment value and an obvious underestimation of the auction competition. Both types of learning contribute to a general decreasing participation trend among consumers over time. Our model provides both a theoretical explanation and empirical evidence of the consumer churn issue. It further identifies two groups of consumers with different risk characteristics: One group is risk-averse and quits using the website before effective learning takes place, while the other group exhibits risk-seeking behavior and overly commits to the auction games. Based on the estimated parameters of the model, we perform counterfactual analyses to evaluate the effects of policy changes on consumers’ participation behaviors. We discuss several important design implications and recommend strategies for building a sustainable business model in the entertainment shopping industry.

Keywords: Dynamic Structural Model, Consumer Learning, Pay-to-Bid Auction, Bayesian Statistics, Maximum Likelihood Estimation

Kenny Cheng was the accepting senior editor. This research article was submitted on February 9, 2017, and went through two revisions.

## 1 Introduction

The proliferation of e-commerce has inspired the development of many new forms of online retail mechanisms, among which “entertainment shopping” represents one recent innovation. As the name implies, entertainment shopping combines “entertainment” with “online shopping.” It sells products using a type of pay-to-bid auction (also known as bidding-fee auction or penny auction) to engage players in online shopping tasks. The auction design leverages people’s natural desires for socializing, competition, achievement, status, and self-expression. It provides an interactive shopping environment to effectively integrate into retail shopping consumers’ utilitarian and hedonic motivations.

According to Alexa’s web traffic rankings, pennyauctionwatch.com currently tracks the top 50 active entertainment shopping websites worldwide. DealDash.com, the US-based e-commerce company that operates the longest-running bidding-fee auction website, allows bidders to bid on brand new products, including electronics, household items, gift cards, and more. Beezid.com is a Canada-based entertainment auction site that features auctions for designer handbags, Apple products, and other desirable consumer products and electronics. MadBid.com is a UK-based e-commerce and online auction site. This fast-growing shopping site has attracted more than one million users from across Europe and around the world.

The pay-to-bid auction is different from other traditional online auction models such as eBay auctions. As the US entertainment shopping site QuiBids.com claims, the new auction format is “a unique, exciting way to rejuvenate a century-old traditional auction in the digital era.” A typical auction on entertainment shopping websites works as follows. Every auction starts at \$0.00, and each bid normally costs the bidder \$0.50-\$1.00 and raises the auction price by only \$0.01, thus the name “penny auction.” The auction adopts a soft ending rule. Every bid restarts the auction countdown clock from a maximum of 10-20 seconds (the timing is not uniform from auction to auction).<sup>1</sup> If no new bids are placed before the clock runs out, the last bidder wins the auction. The winner has the right to buy the item for the final price—typically 60-90% off the retail price. Further details about the auction design and comparison across different websites are provided in Appendix B.

Although the auction design elements, such as the cost of bidding, the incremental price increase, and the countdown clock time, can vary from one website to another, all websites share a common feature—they collect revenue from the bidding fees paid by all participants. The auction turns shopping into a competitive bidding game, so that the business model combines the features of both auctions and entertainment. The winning bidders obtain the merchandise at huge savings, and all losing bidders experience the excitement of potential “winning,” which they deem worthy of the bidding fees they pay in auctions.

However, because most consumers pay the rather large bidding fee and still lose the auction, some analysts have criticized this model as a type of gambling, similar to lotteries (Platt, Price, & Tappen, 2013). Also, Wang & Xu (2016) find evidence that the majority of the participants quickly quit using the entertainment shopping websites after losing money, suggesting significant consumer churn issues. Decreasing consumer confidence has curtailed the overall growth of the industry, casting doubts as to whether the pay-to-bid auction-based entertainment shopping represents a sustainable business model. In fact, many of the early movers in this space, such as Swoopo.com and BigDeal.com, failed after a short period of operation.

Motivated by this paradox that a seemingly attractive business model cannot profit in a long run because of the unusual consumer churns, we develop a model to analyze entertainment shopping from the perspective of participating consumers. We aim to answer the following research questions: What are the main driving factors that motivate consumers to participate in the entertainment shopping website? Why would consumers churn on these websites? Do consumers learn from their repeated participation? If so, what types of learning are possible and what effects does learning have on consumers’ decisions to participate in auctions? From the website design perspective, what policy changes would be effective to better engage consumers and create a sustainable business model?

We believe consumers are attracted to the websites not only because they expect monetary payoff, but also because they perceive considerable entertainment value. Consumers that repeatedly participate in online auctions for different products are able to learn through their own experiences and update beliefs about the perceived entertainment value. They can also learn by observing the historical auction information and by becoming more informed about auction competition. We thus propose a utility-based structural model of consumer learning to gain insights into consumers’ dynamic participation and churn behaviors on the entertainment shopping websites.

We estimate our model using data collected from a leading entertainment auction website, on which we tracked the bidding behaviors of users for more than three months. We found that the consumers’ initial participation incentives mainly come from an overestimation of the entertainment value and an underestimation of the auction competition. Both selflearning and observational learning are effective and help consumers discover the true value of entertainment, form correct expectations about auction competition, and contribute to a general decreasing participation trend among consumers over time. Our model provides both a theoretical explanation and empirical evidence of the consumer churn issue.

Interestingly, our model identifies two groups of consumers with different risk characteristics. The first group of consumers are risk-averse—they are enticed by the fun shopping opportunities but quit the website quickly, even before they learn the true entertainment value for themselves. The second group of consumers, in contrast, are more persistent in their participation and exhibit risk-seeking preferences. This finding is consistent with theories related to wars of attrition and escalation of commitment, thus confirming that entertainment shopping does induce some sort of gambling behavior. Through policy simulations, we offer several recommendations for managing consumer churn on websites and discuss plausible mechanisms for building a sustainable business model.

The rest of this paper is organized as follows. Section 2 briefly reviews the related literature. Section 3 describes our data and presents some initial evidence. Section 4 proposes a structural model of consumer decision-making. Section 5 describes the model estimation method. Section 6 presents the empirical results, robustness checks, and additional tests of the model. Section 7 conducts policy simulations and discusses their implications. Section 8 concludes the study with future research directions.

## 2 Related Literature

In this section, we first review literature in the general context of Internet auctions. We then focus on pay-to-bid auction-based entertainment shopping as an emerging ebusiness model. Finally, we review consumer learning models in various e-commerce applications.

Internet auctions are an important selling mechanism used by many retailers who sell products online (Sun, 2010; Bockstedt & Goh, 2012). Many studies have focused on eBay, the leading auction marketplace selling a broad variety of goods and services (Bapna, Jank, & Shmueli, 2008; Hong & Pavlou, 2014). Because the online auction imposes social competition on bidders, it elicits a more exciting shopping experience than fixed-price purchases. For example, consumers might respond emotionally to environmental stimuli during the auction process, such as excitement, arousal (Teubner, Adam, & Riordan, 2015), impulse buying (Adam, Krämer, & Weinhardt, 2012), escalation of commitment (Staw, 1976; Malmendier & Lee, 2011; McGee, 2013) and winner’s curse (Easley, Wood, & Barkataki, 2011), the reference price effect (Popkowski Leszczyc, Qiu, & He, 2009), and strategic exit using the buy-now option (Angst, Agarwal, & Kuruzovich, 2008; Reiner, Natter, & Skiera, 2014), etc. Specifically, Ku, Malhotra, and Murnighan (2005) identify the “auction fever” phenomenon, in which bidders engage in a fierce battle to win the item in an auction because of competitive arousal. Adam, Krämer, and Müller (2015) further show that social competition drives the auction fever phenomenon, and that bidders’ arousal increases in auctions characterized by high time pressure. In addition, Goes, Karuga, and Tripathi (2010) find that bidders form and update their willingness-to-pay by learning from the participation experience in sequential online auctions.

A new form of Internet auction is the pay-to-bid auction currently adopted by many entertainment shopping websites (Augenblick, 2016), which represents a recent business innovation in e-commerce. Hinnosaar (2016) shows that a high variance of outcomes is common for pay-to-bid auctions. Byers, Mitzenmacher, and Zervas (2010) show that the information asymmetries across participants increase auction duration and produce excess profits. Platt et al. (2013) incorporate risk-loving preferences of users to explain excess revenue in such auctions. Augenblick (2016) incorporates bidders’ regret over past bidding costs into the classic risk-neutral auction models to improve prediction accuracy. In addition, Wang and Xu (2016) find evidence that entertainment shopping websites might lose money to sophisticated participants, but find that the gain from the least experienced bidders far exceeds the loss. Their finding suggests that players learn from their repeated participation experiences. Nevertheless, how learning affects consumers’ choices in different types of bidding games and how the learning effectiveness affects their website participation remain challenging research questions.

Consumer behavior modeling has gained increasing attention in marketing and information systems disciplines. Prior research has shown that consumer learning occurs naturally in various complex decisionmaking environments. Erdem and Keane (1996) treat the use experience of consumers and advertisement as two noisy signals in consumers’ process of learning the attributes of a new product. Erdem, Keane, and Sun (2008) further incorporate product price and advertisement frequency to enrich the consumer learning model. Narayanan and Manchanda (2009) apply a Bayesian learning model to account for the heterogeneous learning rates of individual physicians for new prescription medicines. In addition to new products, learning models have been developed in other application contexts, such as service quality learning and usage learning in the service industry (Iyengar, Ansari, & Gupta, 2007), user content generation and consumption behavior in the mobile context (Ghose & Han, 2014), online reviews (Zhao, Yang, Narayan, & Zhao, 2013), and crowdsourcing (Huang, Singh, & Srinivasan, 2014). These researches contribute to better understanding consumer behaviors under various uncertain environments. Following this stream of research, we propose two learning mechanisms in our model—self-experienced entertainment value learning and observational learning based on historical prices. In addition, we take into account consumers’ risk attribute in their decisionmaking. We develop a dynamic structural model using Bayesian learning to analyze the participation behavior of consumers in entertainment shopping.

Various studies in consumer research have confirmed that shopping experiences produce both utilitarian and hedonic values (Holbrook & Hirschman, 1982), especially in online auctions (Angst et al., 2008; Adam et al., 2012). Hedonic value refers to the enjoyment derived by users from engaging, while utilitarian values are directly related to the shopping outcome (Babin, Darden, & Griffin, 1994). Van der Heijden (2004) argue that perceived enjoyment is extremely important in web systems, games, and systems for home and leisure purposes. Ariely & Simonson (2003) also show that the hedonic value derived from fun and excitement is an important factor leading to the success of Internet auctions. In the entertainment shopping context, we simultaneously consider both the utilitarian and hedonic values consumers derive from their repeated participation in pay-to-bid auctions. We examine how learning occurs over time, how learning dynamics affect consumers’ choice of participation in different types of product auctions, and how their risk preferences influence their changing interests in the online entertainment shopping environment.

## 3 Data and Initial Evidence

## 3.1 Data Description

We collected data from one of the earliest leading entertainment auction websites in China, 5Pai.com. The website sells a large number of consumer electronics and other popular products typically found in online retail stores. Figure B-1 in Appendix B shows a screen shot for 5Pai to illustrate its selling mechanism. Figure B-2 compares other similar websites in China and the United States. Since these websites have adopted identical selling mechanisms, insights gained from this study are directly applicable to other pay-to-bid auctionbased entertainment shopping environments.

We tracked live auctions on the website from October 19, 2011 to January 21, 2012 to collect information about auction-level dynamics and bidder-level details.<sup>2</sup> During each day of this period, the website provided a relatively stable number of auctions and attracted a steady stream of newly registered users. We present detailed descriptive statistics for different product auctions and the corresponding auctioneer revenue in Appendix C. There are 21,463 auctions covering 586 unique products in the data set. The large number of different products and the low repetition for most auctioned products limit us to analyze consumers’ decision-making toward a specific product. We thus choose to focus on consumers’ participation behaviors at the product-category level.

According to the website navigation, we classify the product auctions into three paid auction categories: virtual products (e.g., top-up cards and bid packs), general merchandise (e.g., home daily supplies and electronic appliances), and digital products (e.g., tablets and mobile phones). We separated virtual products from physical products because they have distinct features that might lead to different consumer behaviors. For example, the auction for virtual products (e.g., top-up telephone cards) usually only last for minutes and can be immediately cashed out upon winning. The immediate gratification of virtual products might excite and motivate users. For physical products, we further separated digital products from general merchandise because digital products are some of the most popular auctions, and the same digital product auction is more frequently offered on websites than are other physical products. Furthermore, digital product auctions often take longer—auctions for iPhones, for example, might take hours or even a day to complete, thereby incurring high time and cognitive costs for users. We also believe the consumer learning rates in the three product categories differ. This classification resulted in a relatively balanced sample of 5,000 to 7,000 auctions in each category.

In addition, the website offers free auctions in various product categories (e.g., CNY10 face value top-up card) to attract and engage users. The website distinguishes free auctions from other product auctions using a “free” label, which means that users can use free auction bids to participate in such auctions.<sup>3</sup> We view free auctions as the fourth type of auction because they require bidders to use free, rather than paid, bids. During the three-month period of our data collection, about one out of six auctions were free auctions. Table 1 provides the descriptive statistics for the three types of paid auctions and the free auction.

We observed that digital products have higher retail prices, higher auction closing prices, longer duration, and higher website profits than the other categories. This category has apparently attracted a significant number of bidders who contribute substantially to website revenues. The high average auction closing price of digital products indicates intense competition in the auctions, and the longer auction duration implies higher cognitive and time costs for bidders. closing prices and the accurate inference of the expected payoff from the auctions difficult for users.

Table 1. Summary Statistics for Auctions

<table><tr><td>Product categories</td><td>Virtual products</td><td>General merchandise</td><td>Digital products</td><td>Free auctions</td></tr><tr><td>Average number of auctions per day</td><td>59(14.8)</td><td>55(18.9)</td><td>78(19.9)</td><td>38(13.4)</td></tr><tr><td>Average number of profitable auctions per day</td><td>43(7.96)</td><td>17(6.97)</td><td>26(7.08)</td><td>0(0)</td></tr><tr><td>Average daily website profit (CNY)</td><td>10690.81(3567.34)</td><td>-369.22(2541.42)</td><td>26529.66(25126.33)</td><td>-1184.61(927.18)</td></tr><tr><td>Average retail price per auction (CNY)</td><td>50.45(26.42)</td><td>220.49(134.84)</td><td>442.03(710.70)</td><td>31.18(40.00)</td></tr><tr><td>Average closing price per auction (CNY)</td><td>2.29(3.26)</td><td>2.12(3.32)</td><td>7.73(29.65)</td><td>5.16(7.30)</td></tr><tr><td>Average duration per auction (minutes)</td><td>33.35(128.61)</td><td>28.31(109.38)</td><td>69.35(227.96)</td><td>7.30(21.36)</td></tr></table>

Note: Numbers in parentheses are standard deviations.

In addition, the large variance suggests that auction outcomes are highly uncertain, making the estimation of auction. Note that, although the auction closing prices and the auction duration of the virtual products are similar to those of the general merchandise, the average retail price of the virtual products is much lower than that of the general merchandise. Therefore, the website profit for virtual products is higher than it is for general merchandise.

## 3.2 Sample Auctions and Users

During our observation period, the website had 32,070 active users.<sup>4</sup> Our data show that most registered users were only active for a short period of time. To eliminate the concern that users who registered early might have obtained more information than those who registered late, we randomly selected a sample of users who registered on a typical weekday in October 2011, so that these users had the same prior information set. In Section 6.3 we show that our model estimation and insights are robust against other user samples.

Figure 1 shows the logarithm (log) of the number of auctions and the log of the number of bids placed by all users and the selected sample users, respectively. We observed a power law distribution, in which a few users participated in many auctions and placed a large number of bids, while the majority of users participated in only a handful of auctions and placed few bids. Our sample of users exhibited similar participation patterns as the general population, thereby confirming that our selected sample reasonably represents the population.

Table 2 shows the descriptive statistics of the registered users and the sample users (in parentheses), respectively. On average, each registered user on the website has participated in 5.89 auctions, of which only 0.5 were winning auctions; these numbers indicate high competition and a low probability of winning. We further define the active bidding window as the number of days between the first and last participation of a registered user. The mean active bidding window per user was 4.53 days, indicating that users stayed active for only a few days, thus reflecting limited participation on the website. The mean and variance of the users participating in free auctions were relatively smaller than the mean and variance of the users in paid auctions because the number of free auction bids awarded to or earned by each user is limited. The significant variations in the number of paid auctions indicate strong heterogeneity across users.

![](/api/attachments/EP2762R9/fulltext/images/76ce4f29edc97d0d02d2f93b83c362bbbe2dc5360fe81c8cd836fdfb5aeda350.jpg)

![](/api/attachments/EP2762R9/fulltext/images/d7c907d34c3a63fbcc3073d2153f98ef440ae9f5f03cb82c764ac07f2b92bab8.jpg)

![](/api/attachments/EP2762R9/fulltext/images/c2f73843d9281e637e30a6b49ce2772ab189320c81ab68d1d229129a4c6e2aaf.jpg)

![](/api/attachments/EP2762R9/fulltext/images/6d4cefab186067cc9f3758d3088c54b52eac32bbb17f5015b436851a1fcf8dcf.jpg)  
Figure 1. Histogram of Log Numbers of Auctions and Bids

Table 2. Summary Statistics for All (Sample) Registered Users

<table><tr><td>Variables</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td></tr><tr><td>Total number of auctions per user</td><td>5.89(5.21)</td><td>18.66(10.79)</td><td>1(1)</td><td>822(77)</td></tr><tr><td>Total number of paid auctions per user</td><td>4.12(3.36)</td><td>16.23(8.43)</td><td>0(0)</td><td>749(66)</td></tr><tr><td>Total number of free auctions per user</td><td>1.78(1.85)</td><td>3.53(5.50)</td><td>0(0)</td><td>150(76)</td></tr><tr><td>Total number of winning auctions per user</td><td>0.50(0.33)</td><td>2.82(1.39)</td><td>0(0)</td><td>61(11)</td></tr><tr><td>Active bidding window per user</td><td>4.53(7.66)</td><td>12.14(18.12)</td><td>0(0)</td><td>91(85)</td></tr></table>

Note: Numbers outside the parentheses are for all 32,070 registered users in our data set. Numbers inside the parentheses are for the selected 241 users who registered on a typical weekday.

## 3.3 Initial Evidence of Consumer Participation

What participation patterns do we observe for registered users? Because only paid auctions affect the website revenue, we focus on paid auction participation. Figure 2 presents the number of paid sample users per day and the sample users’ dynamic participation patterns for the three types of paid auctions, respectively. We see that both the number of paid users and the number of paid auctions in which they participated were significantly higher on the registration day. The level of participation decayed over time and stabilized around zero after a month.

Do users learn from their past experiences to improve their bidding skills? To measure a user’s skill in the auction, we define profit per bid as the total net profit the user has gained until day t divided by the number of bids the user has placed up to day t. We conducted regression analysis on the profit per bid using the number of auctions in which a user has participated and using the log number of auctions provided on the website, controlling for the auction type and the individual fixed effects. Table D-1 in Appendix D shows the regression results. We find that the number of auction participations and of observed auctions by a user did not significantly affect the average profit per bid of the user. Users thus seem not to gain effective bidding skills over time.

![](/api/attachments/EP2762R9/fulltext/images/d3a47ecb27499f7a8fb964893adfe4e09b4e40c21572002003d88fa2f172ea37.jpg)

![](/api/attachments/EP2762R9/fulltext/images/82a87d915e50bf7acd3e1d9a799f2843e68b53f6fc8944b101b0cffd3888d02e.jpg)  
Figure 2. Daily Number of Paid Sample Users and Participation in Paid Auctions

Consequently, we ask two questions: What aspects of learning are possible? How do users learn from their experience and observation? We developed a structural model to explain the dynamic participation behaviors of users, which enables us to better understand the users’ decision-making processes regarding their participation on entertainment shopping websites.

## 4 The Model

Deci, Betley, Kahle, Abrams, & Porac (1981) assert that people can gain extrinsic rewards (e.g., monetary awards and prizes) when they participate in competitive events. They also can gain a more intrinsic, personal, and emotional reward from competitively derived pleasure. On entertainment shopping websites, consumers derive a positive utilitarian value by winning an auction and obtaining a desired product at a huge discount. The direct monetary return from winning (i.e., the savings) and the bidding fees paid in the participated auctions represent the tangible utility gain/loss.

In addition to the tangible values, consumers derive intangible rewards, which are more subjective and personal and result more from fun and excitement in the process than from simply completing a shopping task. According to Adam et al. (2012), Consumers might be interested more in having such experiences than in merely acquiring products. We term such intangible rewards from the auction participation the “entertainment value.”

Because a bidder needs to make a bidding decision within a very short countdown clock window (usually within 10 seconds), the high time pressure will impose a high cognitive cost for the consumer. In addition, some popular auctions typically take hours to complete; thus consumers must invest significant time and effort in continuously monitoring the auction process. We term this intangible cost the “cognitive cost.”

In this study, we assume that consumers derive utility from both the tangible monetary return and the intangible nonmonetary entertainment value and cognitive cost. We also consider the risk attitude of consumers in the structural model.

## 4.1 User Utility

We consider a number of users indexed by <sub>??</sub> <sub>=</sub> <sub>1,2, … , ??</sub> who choose to participate in paid auctions with category $j = 1 , 2 , 3$ over the time period <sub>?? =</sub> $1 , 2 , \dots , T .$ . At the beginning of each day <sub>??</sub>, users decide whether to participate in a specific type of auction based on their expected utility.

First, a user’s utility can be affected by his or her current financial status and past participation experience. We use $S _ { i t } = [ M _ { i t } ^ { c } , M _ { i t } ^ { l } , L _ { i t } ]$ to depict a vector of the user- and time-specific covariates, including a user’s cumulative wealth up to day <sub>??</sub> $( M _ { i t } ^ { c } )$ earnings from the previous day $( M _ { i t } ^ { l } )$ , and a loss indicator $( L _ { i t } )$ capturing the user’s continuous failures in the auctions. Both $M _ { i t } ^ { c }$ and $M _ { i t } ^ { l }$ are affected by the bidding fees sunk cost and the auction outcomes from the user’s past auction participation. The loss indicator $L _ { i t }$ is used to measure whether frequent past failures would cause competitive arousal which might increase the bidder’s likelihood to participate in future auctions.

Second, regardless of the auction outcome, participating in the auction is seen as an adventure and has a potential entertainment and emotional worth. Thus, the entertainment effect is considered a key design feature of hedonic information systems (Van der Heijden, 2004). We assume each user has a perceived website entertainment value $E _ { i t } ^ { e }$ at time <sub>??</sub> , which reflects the user’s overall evaluation of the entertainment shopping environment. A number of factors, including fair auction rules, large number and variety of products, rich functionalities, friendly user interface, automatic bidding tools, easy account management, active online community, and other aspects of web design might positively affect the website entertainment value. The overall website entertainment value can be reflected by the steady state of user participation.

Third, various types of auctions might bring different participation experiences to individual users and require different levels of cognitive effort (Camerer, Ho, & Chong, 2004). For example, due to the soft ending rule of the auction, digital products such as iPhones might take hours or even a day to complete, thereby incurring high time and cognitive cost for users. In contrast, the auction for virtual products such as top-up telephone cards can be completed within minutes. We thus introduce a category-specific cognitive cost parameter, $\beta _ { j }$ , to reflect the nonmonetary, psychological participation cost including the average time and effort invested in different types of auctions. This set of parameters can be identified relatively to each other based on users’ heterogeneous participation patterns in the different categories of product auctions.

In addition, each user might infer the level of auction competition from the observed historical auction closing prices. Because we are interested in users’ decision-making at the category level, we aggregate auction closing prices $P _ { i j t }$ in each category. The mean and variance of the auction closing price, which can be identified through the historical auction closing price series, represent the expected competition and the uncertainty involved in the specific auction category.

Let $U _ { i j t }$ be the utility that user <sub>??</sub> obtained from participating in category <sub>??</sub> auction on day <sub>??</sub> . We specify the utility function as follows:

$$
\begin{array}{r} U _ {i j t} = E _ {i t} ^ {e} + \beta_ {j} + \alpha_ {g} P _ {i j t} + \alpha_ {g} r _ {g} P _ {i j t} ^ {2} + \\ \lambda_ {g} ^ {\prime} S _ {i t} + \varepsilon_ {i j t} (1) \end{array}
$$

The first two terms capture the individual and category level expected intangible values that we infer from our data. The third term captures the user’s perceived price effect of auction competition from observable historical price information. The fourth (squared) term measures the risk preferences of the user in response to auction competition. <sup>5</sup> The fifth term is a vector of covariates that capture the tangible monetary gains and losses from the user’s own past auction participation experiences. Finally, the error term $\varepsilon _ { i j t }$ captures the user choice-specific random shock at time . These errors can be any promotional activities or reminder emails that are unknown to the researchers but that can influence the choice users make about the types of auctions in which they would like to participate.

Our model allows for user heterogeneity by assuming different latent segments (Desarbo, Kamakura, & Wedel, 2006; Erdem et al., 2008; Ghose & Han, 2014). For each latent segment $^ { g , }$ parameter $\alpha _ { g }$ measures the effect of the auction competition, and $r _ { g }$ captures the risk preference of users toward uncertainty in the auction outcome. The perceived auction competition and risk level would affect a user’s expected monetary payoff. In addition, parameter vector $\lambda _ { g }$ measures how the past monetary returns and auction outcomes (expressed in the vector covariates) affect the user’s perceived utility for the <sub>??</sub>th latent segment.

At the beginning of each day, users decide whether to participate in any type of auction based on their expected utility. Each user has a prior belief about the perceived entertainment value and the auction competition. Users are initially uncertain about these values when they first registered on the website. As time goes by, they learn through both direct participation experiences and indirect observations on the website. Figure 3 illustrates the belief update framework.

Two types of learning occur simultaneously. First, consumers learn through their own participation in auctions. These personal experiences provide the consumers with signals to update their belief about the entertainment value of the site. Their utilitarian payoffs such as monetary gains and losses from auction participation are also updated. Second, consumers can actively track newly completed auctions on the website. The observed closing price signals help the users update their beliefs and infer the level of auction competition.

in the expected utility functional expression (see Equation 4 in Section 4.5).

![](/api/attachments/EP2762R9/fulltext/images/75bded9e044afaf5bd353ba3428ef7d39b15f6a38d3d65bb0296b40361a201ce.jpg)  
Figure 3. User Learning Through Direct Experiences and Indirect Observations

As seen in Figure 3, both the monetary and experiencerelated terms and the beliefs about entertainment value and perceived auction competition affect a user’s expected utility. In the following, we discuss our measures and implement the learning process using a Bayesian learning model.

## 4.2 Monetary Gain and Continuous Loss

Two monetary terms enter a user’s utility function. The user’s cumulative wealth up to day <sub>??</sub> , $M _ { i t } ^ { c }$ , is the user’s account balance at the beginning of day <sub>??</sub>. The user’s earning in the previous day, $M _ { i t } ^ { l } .$ , is calculated as the total revenue (retail prices minus auction closing prices for winners and zero for losers) minus the sunk cost during the previous day. We take the log transformation of the cumulative balance, revenue, and sunk cost plus 1 to rescale the measure and to avoid infinitely negative values.

We also include a consecutive loss factor. The escalation of commitment (Staw, 1976; Malmendier & Lee, 2011; McGee, 2013) and the sunk cost fallacy (Augenblick, 2016; French & McCormick, 1984) together have been used to justify people’s increased investment of money and time in a decision. It refers to the phenomenon that, based on the cumulative prior investment, and despite new evidence suggesting that the cost of continuing the decision outweighs the expected benefit, the decision maker still “throws good money after bad.” Because each time a bidder loses an auction, he or she incurs some sunk costs (i.e., nonnegligible biddings fees), we want to evaluate whether bidders make poor decisions by using their past failures to justify their continued involvement. Thus, we use a loss indicator $L _ { i t }$ to indicate whether the user has lost a fixed number of auctions consecutively. In our main model estimation, the indicator is 1 if a user loses 15 consecutive auctions; otherwise, it is 0. The escalation of commitment could be confirmed with a significant and positive estimate of the coefficient for $L _ { i t } .$ . The values for $M _ { i 1 } ^ { c } , M _ { i 1 } ^ { l }$ , and $L _ { i 1 }$ at the beginning of day 1 are all zero.

## 4.3 User Learning About Entertainment Value

We assume users have a heterogeneous prior belief $E _ { i 0 }$ about the entertainment value when they first register on the website. This prior belief is normally distributed with mean $E _ { 0 }$ and variance $\sigma _ { E _ { 0 } } ^ { 2 }$ , so $E _ { i 0 } { \sim } N \left( E _ { 0 } , \sigma _ { E _ { 0 } } ^ { 2 } \right)$ 1

After registration, users can participate in both free and paid auctions on the website. By experiencing both types of auctions, users obtain different signals about the website entertainment value. The free auction experience signal is considered more precise than the paid auction signal because the bidding in the former generally does not involve real money, allowing users to discover quickly the true entertainment value. <sup>6</sup>

from a distribution. Users are initially uncertain about the match value of content. They gradually learn the true value

We define user $i \ ' \mathbf { s }$ direct experience through the $s ^ { t h }$ paid auction and $m ^ { t h }$ free auction on day <sub>??</sub> as $E _ { i t s } ^ { p } { \sim } N ( \mu , \sigma _ { \delta } ^ { 2 } )$ , and $E _ { i t m } ^ { f } { \sim } N \left( \mu , \sigma _ { \eta } ^ { 2 } \right)$ , where $\mu$ is the true website entertainment value and $\sigma _ { \delta } ^ { 2 }$ and $\sigma _ { \eta } ^ { 2 }$ are the bidding experience variances that measure the precision of signals. Note that user <sub>??</sub> receives the experience signals only when she bids in an auction.

Assume user <sub>??</sub> participates in a total of $n _ { i t }$ paid auctions and $f _ { i t }$ free auctions on day <sub>??</sub>. The aggregated signals follow normal distributions $E _ { i t } ^ { p } =$ $\frac { \sum _ { s } E _ { i t s } ^ { p } } { n _ { i t } } { \sim } N \left( \mu , \frac { \sigma _ { \delta } ^ { 2 } } { n _ { i t } } \right)$ and $\begin{array} { r } { E _ { i t } ^ { f } = \frac { \sum _ { m } E _ { i t m } ^ { f } } { f _ { i t } } { \sim } N \left( \mu , \frac { \sigma _ { \eta } ^ { 2 } } { f _ { i t } } \right) \quad , } \end{array}$ respectively. Consequently, the bidders update their posterior entertainment belief according to Bayes’ theorem (DeGroot, 1970) following the normal distribution, $N \left( E _ { i t } , \sigma _ { E _ { i t } } ^ { 2 } \right)$ , where $\begin{array} { r } { E _ { i t } = \frac { \sigma _ { E _ { i t } } ^ { 2 } } { \sigma _ { E _ { i , t - 1 } } ^ { 2 } } E _ { i , t - 1 } - } \end{array}$ $\begin{array} { r } { n _ { i t } \frac { \sigma _ { E _ { i t } } ^ { 2 } } { \sigma _ { \delta } ^ { 2 } } E _ { i t } ^ { p } + f _ { i t } \frac { \sigma _ { E _ { i t } } ^ { 2 } } { \sigma _ { \eta } ^ { 2 } } E _ { i t } ^ { f } \qquad , } \end{array}$ and $\sigma _ { E _ { i t } } ^ { 2 } =$ $\scriptstyle \frac { 1 } { 1 / \sigma _ { E _ { i , t - 1 } } ^ { 2 } + n _ { i t } / \sigma _ { \delta } ^ { 2 } + f _ { i t } / \sigma _ { \eta } ^ { 2 } } .$ Here, $E _ { i , t - 1 }$ and $\sigma _ { E _ { i , t - 1 } } ^ { 2 }$ are the mean and variance of the entertainment belief at the beginning of day <sub>??</sub>, which are the same as the posterior beliefs at the end of day $t - 1$ . Accordingly, bidders place a relatively higher weight on more precise signals (the signals with a lower variance).

## 4.4 User Learning About Auction Closing Prices

Because each new bid will raise the auction price by a positive price increment, a higher auction closing price directly reflects a higher level of auction competition. Consumers can observe the historical auction closing prices and use them to form expectations about future auction outcomes.

We assume that users have prior beliefs about the closing price distribution for a specific auction category <sub>??</sub> when they join the website. Thus, $P _ { i j 0 } { \sim } N \left( P _ { j 0 } , \sigma _ { P _ { 0 } } ^ { 2 } \right)$ , where $P _ { j 0 }$ and $\sigma _ { P _ { 0 } } ^ { 2 }$ are the prior mean and variance of the closing price distribution, respectively. Users update their beliefs about type <sub>??</sub> auction closing prices on a daily basis. Thus, $P _ { i j t } { \sim } N \left( P _ { j } , \sigma _ { \zeta _ { j } } ^ { 2 } \right)$ , where $P _ { j }$ reflects the true auction competition and $\sigma _ { \zeta _ { j } } ^ { 2 }$ is the closing price variance for type <sub>??</sub> auctions.

The users update their posterior closing price belief based on the daily closing price signals they observe following the normal distribution $N \left( P _ { j t } , \sigma _ { P _ { j t } } ^ { 2 } \right)$ , where $\begin{array} { r } { P _ { j t } = \frac { \sigma _ { P _ { j t } } ^ { 2 } } { \sigma _ { P _ { j , t - 1 } } ^ { 2 } } P _ { j , t - 1 } + \frac { \sigma _ { P _ { j t } } ^ { 2 } } { \sigma _ { \zeta _ { j } } ^ { 2 } } P _ { i j t } } \end{array}$ and $\begin{array} { r } { \sigma _ { P _ { j t } } ^ { 2 } = \frac { 1 } { 1 / \sigma _ { P _ { j , t - 1 } } ^ { 2 } + 1 / \sigma _ { \zeta _ { j } } ^ { 2 } } . } \end{array}$

Here, $P _ { j , t - 1 }$ and $\sigma _ { P _ { j , t - 1 } } ^ { 2 }$ are the mean and variance of the prior closing price belief for type <sub>??</sub> auctions at the beginning of day $t ,$ which are the same as the posterior belief at the end of day $t - 1$

## 4.5 Expected Utility and Likelihood

Users make participation decisions based on their expected utilities. Denote $I _ { i t }$ as user $i \ ' _ { \mathbf { S } }$ information set, which contains all auction-related signals received up to day <sub>??</sub>. Conditional on the information set, and based on Equation (1), the expected utility of user <sub>??</sub> from participating in type <sub>??</sub> auctions at time <sub>??</sub> is:

$$
E \big [ U _ {i j t} \big | I _ {i t} \big ] = \widetilde {U} _ {i j t} + \varepsilon_ {i j t}, (2)
$$

where

$$
\begin{array}{r} \widetilde {U} _ {i j t} = E [ E _ {i t} ^ {e} | I _ {i t} ] + \beta_ {j} + \alpha_ {g} E [ P _ {i j t} | I _ {i t} ] + \\ \alpha_ {g} r _ {g} E [ P _ {i j t} ^ {2} | I _ {i t} ] + \lambda_ {g} ^ {\prime} E [ S _ {i t} | I _ {i t} ]. \end{array} (3)
$$

Expanding the conditional expected utility in Equation (3) and substituting into Equation (2) we have Equation (4). Detailed derivation of the expression is provided in Appendix E.

$$
\begin{array}{r l} & E \big [ U _ {i j t} \big | I _ {i t} \big ] = E _ {i, t - 1} + \beta_ {j} + \alpha_ {g} P _ {j, t - 1} + \alpha_ {g} r _ {g} P _ {j, t - 1} ^ {2} + \\ & \alpha_ {g} r _ {g} E \big [ (P _ {j} - P _ {j, t - 1}) ^ {2} \big | I _ {i t} \big ] + \alpha_ {g} r _ {g} \sigma_ {\zeta_ {j}} ^ {2} + \lambda_ {g 1} M _ {i t} ^ {l} + \\ & \lambda_ {g 2} M _ {i t} ^ {c} + \lambda_ {g 3} L _ {i t} + \varepsilon_ {i j t}. \end{array} \tag {4}
$$

Note that two sources of expected variability are associated with the observed type <sub>??</sub> closing prices at the beginning of day <sub>??</sub>. One source is the observed variance, $\sigma _ { \zeta _ { j } } ^ { 2 }$ , of historical closing prices, and the other is $E \big [ ( P _ { j } - \tilde { P } _ { j , t - 1 } ) ^ { 2 } \big | I _ { i t } \big ]$ , which is the difference between the true closing price and the expected closing price of category <sub>??</sub>. If a user has little information about the true closing price, her estimation of auction competition would be inaccurate, which amplifies the risk involved in her decision-making.

As previously mentioned, users might participate in a specific type of auction based on their expected utility. Let $A _ { i j t }$ denote user <sub>??</sub>’s participation variable, which is equal to 1 if user <sub>??</sub> participates in type <sub>??</sub> auctions at time <sub>??</sub> and is 0 otherwise. The participation decision of users for each type of auction is assumed to be independent. $\varepsilon _ { i j t }$ is assumed to follow a Type I extreme value distribution. The probability of observing the user’s participation decision can be specified as

$$
\begin{array}{c} {P r \big (A _ {i j t} \big) =} \\ {\big (\frac {e x p (\widetilde {U} _ {i j t})}{1 + e x p (\widetilde {U} _ {i j t})} \big) ^ {A _ {i j t}} \big (\frac {1}{1 + e x p (\widetilde {U} _ {i j t})} \big) ^ {(1 - A _ {i j t})},} \end{array}\tag{5}
$$

The joint likelihood that the sample users participate in the full bidding series can be expressed as:

$$
\begin{array}{l} \text { Likelihood } (A) = \prod_ {i = 1} ^ {N} \prod_ {j = 1} ^ {J} \prod_ {t = 1} ^ {T} P r \big (A _ {i j t} \big), \\ (6) \end{array}
$$

where <sub>??</sub> is the participation decision matrix for the bidding action of all <sub>??</sub> users for <sub>??</sub> types of auctions over the entire observation period .

## 5 Model Estimation

## 5.1 Simulated Maximum Likelihood

The likelihood function in Equation (6) is jointly determined by the perceived entertainment effect and the anticipated auction closing prices, means and variances, and user- and time-specific covariates in each period. Note that the closing price signals can be observed, whereas the entertainment signals through bidding cannot. Because the high dimensional integration for the likelihood function is not feasible in closed form, we adopt a simulated maximum likelihood method (McFadden, 1989) to compute the likelihood function.<sup>7</sup>

## 5.2 Identifications

The nonmonetary payoff in the expected utility function consists of two terms. The first term, $E _ { i , t - 1 }$ , is the overall entertainment belief of user at the beginning of day <sub>??</sub> . The other term is the auction category-specific parameter, $\beta _ { j } { \mathrm { : } }$ , which represents the perceived average cognitive cost for users participating in different types of auction on the website. $\beta _ { 2 }$ was set as -5 for model identification purposes.<sup>8</sup>

The prior belief about the website entertainment value, $E _ { 0 } ,$ is the same for all users in our sample since they registered on the same date. Because the entertainment beliefs of active participating users are updated after they participate in more auctions and the entertainment beliefs of those who had no actions on the registration day stay unchanged, $E _ { 0 }$ can be identified through the observations before the first participation.

The true website entertainment mean value <sub>??</sub> was identified according to the steady state of users’ participation behavior. When users learn based on their own repeated participation, their entertainment beliefs,

$E _ { i t } ,$ , converge to their true mean. If the learning period is long enough, users learn the true value after a sufficient number of participations in the auctions.

The experience signal variances for paid auctions $( \sigma _ { \delta } ^ { 2 } )$ and free auctions $( \sigma _ { \eta } ^ { 2 } )$ ) were identified through the users’ participation patterns in the sample. For users who participated in one or more auctions during a day, the change in their probability of participation before and after the day helps infer the learning rate and identify the signal variance parameters, $\sigma _ { \delta } ^ { 2 }$ and $\sigma _ { \eta } ^ { 2 }$ . A smaller signal variance implies that users can obtain a more precise signal by participating in auctions. Thus, the knowledge acquisition of users about the website entertainment effect converges to the true value at a relatively faster learning rate.

The prior belief about the auction closing prices, $P _ { j 0 } { \mathrm { : } }$ can be identified using the frequency of participation in different types of auctions during the first day of registration. Each observed auction closing price was considered to be a realization of a random variable following a normal distribution with true mean $P _ { j }$ and variance $\sigma _ { \zeta _ { j } } ^ { 2 }$ . Because the auction closing prices are observable, the population mean and variance are directly estimated from the complete data set.

The variations in users’ participation in different types of auctions help to identify the coefficient $\alpha _ { g }$ Parameter $r _ { g }$ reflects the average risk preference of users. Given that $\alpha _ { g }$ is negative, the users are riskseeking if $r _ { g }$ is negative and are risk-averse if $r _ { g }$ is positive. Users face uncertainty in the auction competition. They update their expected auction closing price dynamically, thereby affecting the likelihood of their participation in different types of auctions. Accordingly, the risk preference of users can be identified through this learning process. Finally, the sensitivity parameter vector, $\lambda _ { g }$ , of bidders can be identified using the changes in users’ dynamic participation behavior when the covariates change.

## 6 Empirical Results

## 6.1 Model Fit and Model Selection

Incorporating learning effects into the model results in the need to estimate more parameters. We compare the performance of the full model defined in Section 5 with

three alternative models to test how learning improves the model fit. Model 1 does not consider the learning effects at all. In this case, we assume users know the true entertainment value, as well as the true mean auction closing prices, for different types of auctions. Model 2 assume the users are certain about the website entertainment effect and includes only the auction closing price learning component. Model 3 assumes that users are uncertain about the auction closing prices and incorporates only the entertainment learning effect.

Table 3 reports the log likelihood, the Akaike information criteria (AIC), and the Bayesian information criteria (BIC) values, as well as the log likelihood for out-of-sample tests for each model. The model with the lower AIC and BIC values is preferred.

Table 3. Model Fit and Comparison

<table><tr><td rowspan="2">Model</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td colspan="3">Full model</td></tr><tr><td>No learning</td><td>Price learning</td><td>Entertainment learning</td><td colspan="3">Both price and entertainment learnings</td></tr><tr><td>Latent classes</td><td>One</td><td>One</td><td>One</td><td>One</td><td>Two</td><td>Three</td></tr><tr><td colspan="7">In-sample (241 users registered on the same day)</td></tr><tr><td>Log likelihood</td><td>-2902.05</td><td>-2083.13</td><td>-1964.66</td><td>-1789.85</td><td>-1741.73</td><td>-1717.59</td></tr><tr><td># of Parameters</td><td>8</td><td>11</td><td>11</td><td>14</td><td>20</td><td>26</td></tr><tr><td>Sample size</td><td>65793</td><td>65793</td><td>65793</td><td>65793</td><td>65793</td><td>65793</td></tr><tr><td>AIC</td><td>5064.85</td><td>4188.27</td><td>3951.31</td><td>3607.69</td><td>3523.46</td><td>3487.18</td></tr><tr><td>BIC</td><td>5136.85</td><td>4288.30</td><td>4051.35</td><td>3735.01</td><td>3705.34</td><td>3723.63</td></tr><tr><td colspan="7">Out-of-sample (325 users registered on a different day)</td></tr><tr><td>Log likelihood</td><td>-3239.72</td><td>-2396.93</td><td>-2421.04</td><td>-2026.63</td><td>-2013.19</td><td>-2022.69</td></tr></table>

Comparing Model 1 (the model without learning) with Model 2 and Model 3 (models that have only one learning component), we see that the two types of learning independently contribute to improving the model fit. It suggests that the two learning mechanisms are substitutable to each other. Moreover, entertainment learning has a larger effect on improving the model fit than the auction closing prices learning.

The log likelihood, AIC and BIC values suggest that the full model performs the best among the alternative models. It indicates that these two types of learning mechanisms complement each other. Both the learning of the entertainment value and the learning of auction closing prices are important to explain the observed data variations.

In addition, the full model allows for user heterogeneity in terms of auction competition $( \alpha _ { g } )$ risk preference $( r _ { g } )$ , monetary payoffs, and loss status $( \lambda _ { g } )$ . We estimate the number of latent segments <sub>??</sub> using 1, 2, and 3 latent segments, respectively. As shown in Table 3, if we increase <sub>??</sub> from 1 to 2, AIC and BIC, as well as the log likelihood values, for insample and out-of-sample tests all are improved. Meanwhile, if we increase the <sub>??</sub> value from 2 to 3, the BIC and log likelihood for the out-of-sample test deteriorate, but the AIC and log likelihood for the insample test slightly improve. Hence, we select two latent segments for further parameter estimates.

## 6.2 Parameter Estimation

Table 4 summarizes the parameter estimation results. Let us first look at the homogenous parameter estimates. Since we fixed $\beta _ { 2 }$ at -5 in our model estimation, $\beta _ { 1 }$ and $\beta _ { 3 }$ are estimated with negative values, reflecting the average cognitive cost for users participating in the other two types of paid auctions. The absolute values for Type 1 auctions (virtual products, 4.900) and Type 2 auctions (general merchandise, fixed at 5) are smaller than the absolute values for Type 3 auctions (digital products, 6.340).

Table 4. Structural Model Parameter Estimation

<table><tr><td rowspan="2" colspan="2">Heterogeneous parameters</td><td colspan="2">Segment 1</td><td colspan="2">Segment 2</td></tr><tr><td>Estimates</td><td>Std. error</td><td>Estimates</td><td>Std. error</td></tr><tr><td> $\alpha_g$ </td><td>Sensitivity to auction competition</td><td>-2.824</td><td>0.000***</td><td>-4.159</td><td>0.348***</td></tr><tr><td> $r_g$ </td><td>Risk preference</td><td>3.223</td><td>0.000***</td><td>-0.071</td><td>0.002***</td></tr><tr><td> $\lambda_{g1}$ </td><td>Past monetary gain</td><td>4.124</td><td>0.000***</td><td>-0.435</td><td>0.053***</td></tr><tr><td> $\lambda_{g2}$ </td><td>Cumulative monetary gain</td><td>-5.239</td><td>0.000***</td><td>0.487</td><td>0.066***</td></tr><tr><td> $\lambda_{g3}$ </td><td>Consecutive bidding loss</td><td>0.117</td><td>0.000***</td><td>0.990</td><td>0.344**</td></tr><tr><td> $\pi_g$ </td><td>Segment membership probability</td><td>0.413</td><td>0.036***</td><td>0.587</td><td>--</td></tr><tr><td colspan="4">Homogenous parameters</td><td>Estimates</td><td>Std. error</td></tr><tr><td> $\beta_1$ </td><td colspan="3">Type 1 (virtual products) cognitive cost</td><td>-4.900</td><td>0.157***</td></tr><tr><td> $\beta_2$ </td><td colspan="3">Type 2 (general merchandise) cognitive cost</td><td>-5</td><td>-Fixed</td></tr><tr><td> $\beta_3$ </td><td colspan="3">Type 3 (digital products) cognitive cost</td><td>-6.340</td><td>0.622***</td></tr><tr><td> $\mu$ </td><td colspan="3">Mean website entertainment value</td><td>6.017</td><td>0.573***</td></tr><tr><td> $E_0$ </td><td colspan="3">Prior belief about website entertainment value</td><td>7.297</td><td>0.512***</td></tr><tr><td> $\sigma_{E_0}^2$ </td><td colspan="3">Variance of prior belief about website entertainment value</td><td>10</td><td>-Fixed</td></tr><tr><td> $ln\sigma_\delta^2$ </td><td colspan="3">Log variance of paid auction participation signal</td><td>4.281</td><td>0.271***</td></tr><tr><td> $ln\sigma_\eta^2$ </td><td colspan="3">Log variance of free auction participation signal</td><td>2.086</td><td>0.254***</td></tr><tr><td> $P_{10}$ </td><td colspan="3">Prior belief for Type 1 auction closing price</td><td>1.737</td><td>0.107***</td></tr><tr><td> $P_{20}$ </td><td colspan="3">Prior belief for Type 2 auction closing price</td><td>1.752</td><td>0.113***</td></tr><tr><td> $P_{30}$ </td><td colspan="3">Prior belief for Type 3 auction closing price</td><td>5.310</td><td>0.373***</td></tr><tr><td> $\sigma_{P_0}^2$ </td><td colspan="3">Variance of prior belief about auction closing price</td><td>10</td><td>-Fixed</td></tr><tr><td> $P_1$ </td><td colspan="3">Mean closing price for Type 1 auction</td><td>2.346</td><td>0.070***</td></tr><tr><td> $P_2$ </td><td colspan="3">Mean closing price for Type 2 auction</td><td>2.195</td><td>0.061***</td></tr><tr><td> $P_3$ </td><td colspan="3">Mean closing price for Type 3 auction</td><td>8.441</td><td>0.556***</td></tr><tr><td> $ln\sigma_{\zeta_1}^2$ </td><td colspan="3">Log variance of Type 1 auction closing price signal</td><td>-0.799</td><td>0.147***</td></tr><tr><td> $ln\sigma_{\zeta_2}^2$ </td><td colspan="3">Log variance of Type 2 auction closing price signal</td><td>-1.064</td><td>0.147***</td></tr><tr><td> $ln\sigma_{\zeta_3}^2$ </td><td colspan="3">Log variance of Type 3 auction closing price signal</td><td>3.371</td><td>0.147***</td></tr><tr><td colspan="6">Note: *** denotes significant at 0.001; ** denotes significant at 0.01.</td></tr></table>

This finding is considered reasonable because the average duration for Type 1 and Type 2 auctions is relatively short, and auctions usually end quickly, lasting from a few minutes to a few hours. In contrast, Type 3 products generally have higher retail prices, and users who participate in this type of auction might persist for a long time. For example, the auctions for popular Apple product auctions can last for more than one day, pausing at 00:00 a.m. and restarting at 9:00 a.m. The time and cognitive costs associated with this type of auction are higher than those related to the other types of auctions.

The website entertainment value measures the average overall effect of the entertainment auction environment on the utility of users—for example, the average level of enjoyment provided by the online auction games and the overall quality of services on the website. The prior entertainment belief, $E _ { 0 }$ (7.297), is significantly higher than the estimated true mean entertainment value <sub>??</sub> (6.017). This result indicates that users overestimate the entertainment benefit they can obtain when they initially join the website. Recall that users participate in both paid and free auctions. The estimated natural logarithm variance for free auctions (2.086) is smaller than that for paid auctions (4.281). Thus, the signal from free auctions is more precise. This is mainly because users do not have a monetary sunk cost for free auctions, which enables them to obtain a more accurate entertainment valuation by participating in the free auctions.

The estimated initial auction type-specific closing price beliefs are 1.737, 1.752, and 5.310, which are smaller than the true means of 2.346, 2.195, and 8.441, respectively. This result indicates that users underestimate the auction closing prices for all three types of auction. The overestimation of the entertainment value and underestimation of auction competition together confirm the observation that many users actively participate in auctions when they initially register on the website, but their level of participation decreases over time. In terms of signal precision, Type 1 and Type 2 auctions show more precise signals than Type 3 auctions. The natural logarithm of variances are -0.799, -1.064, and 3.371, respectively, for the three types of auction. These figures suggest that learning in the digital products category is more difficult to achieve than learning in the first two types of auction.

Next, we turn to heterogeneous model parameter estimates. Because parameter $\alpha _ { g }$ for the expected auction closing price is estimated as -2.824 for the first latent segment and -4.159 for the second latent segment, it appears that users in Segment 2 are more sensitive about auction competition than users in Segment 1. The risk preference parameters, $r _ { g } ,$ , are positive for users in Segment 1 (3.223) and negative for users in Segment 2 (-0.071). Together with the negative estimation of $\alpha _ { g }$ , the result indicates that users in Segment 1 show risk-averse preferences, while users in Segment 2 show risk-seeking preferences. Hence, a relatively large percentage (58.9%) of the users in our data exhibits risk-seeking behavior and the rest is risk-averse.

The parameter for the recent past monetary gain, $\lambda _ { g 1 }$ is positive for users in Segment 1 (4.124) and negative (-0.435) for users in Segment 2. Because users in Segment 1 are risk-averse, a gain in the recent past increases their participation interest in the following period, while a loss in the recent past reduces their participation interest in the following period. Because Segment 2 users are risk-seeking, the loss increases their participation interest in the following period.

In contrast, the cumulative balance, $\lambda _ { g 2 }$ , negatively affects the utility for Segment 1 users (-5.239) and positively affects the utility for Segment 2 users (0.487). When a risk-averse user loses a significant amount of money cumulatively on the entertainment auction website, that user’s utility is negatively affected. Such users might quit the website without bidding anymore. The opposite is true for the riskseeking users, whose utility is positively affected. The risk-seeking users might become addicted and stay on the website, continuing to participate in auctions even though they have incurred significant losses in the past.

Finally, the coefficients for the consecutive loss indicator, $\lambda _ { g 3 }$ , are positive for both segments (0.117 and 0.990, respectively). The positive coefficient indicates that users become more addicted to the game after losing many auctions. The higher coefficient of Segment 2 users also suggests that they might be more likely to overly commit to the auction games than Segment 1 users. This result reflects the gambling effect inherent in the pay-to-bid auction mechanism and the entertainment shopping environment, and the finding is consistent with the prior literature on the escalation of commitment (Staw, 1976; Malmendier & Lee, 2011; McGee, 2013) that has been widely discussed in the context of lotteries and gambling.

## 6.3 Robustness Checks

The results obtained in this study are robust and not sensitive to particular assumptions underlying the data analysis. Table 5 demonstrates the robustness of the model by using different data sets and by varying some criteria in the model estimation.

In the main model, a sample of users who registered on the same day was used to represent the population of users. This approach effectively controlled the confounding effects of consumer learning. An alternative sample was then selected to estimate the model and test its robustness.

Table 5. Parameter Estimation and Robustness Checks

<table><tr><td rowspan="2"></td><td colspan="2">Sample (325 Users)</td><td colspan="2">Base value ( $\beta_2 = -1$ )</td><td colspan="2">No. of losses (18)</td></tr><tr><td>Segment 1</td><td>Segment 2</td><td>Segment 1</td><td>Segment 2</td><td>Segment 1</td><td>Segment 2</td></tr><tr><td> $\alpha_g$ </td><td>-4.034***(0.000)</td><td>-7.088***(0.178)</td><td>-1.723***(0.000)</td><td>-3.882***(0.439)</td><td>-3.649***(0.000)</td><td>-4.084***(0.550)</td></tr><tr><td> $r_g$ </td><td>7.055***(0.000)</td><td>-0.072***(0.001)</td><td>0.490***(0.000)</td><td>-0.070***(0.002)</td><td>2.398***(0.000)</td><td>-0.071***(0.002)</td></tr><tr><td> $\lambda_{g1}$ </td><td>0.036***(0.000)</td><td>-0.330***(0.051)</td><td>2.549***(0.000)</td><td>-0.443***(0.052)</td><td>2.148***(0.000)</td><td>-0.445***(0.051)</td></tr><tr><td> $\lambda_{g2}$ </td><td>-1.838***(0.000)</td><td>0.531***(0.065)</td><td>-3.797***(0.000)</td><td>0.615***(0.082)</td><td>-7.523***(0.000)</td><td>0.513***(0.066)</td></tr><tr><td> $\lambda_{g3}$ </td><td>1.235***(0.000)</td><td>2.020***(0.352)</td><td>0.561***(0.000)</td><td>1.130***(0.408)</td><td>0.453***(0.000)</td><td>0.154 (0.507)</td></tr><tr><td> $\pi_g$ </td><td>0.347***(0.030)</td><td>0.653 (--)</td><td>0.464***(0.003)</td><td>0.536 (--)</td><td>0.414 (--)</td><td>0.586***(0.036)</td></tr><tr><td> $\beta_1$ </td><td colspan="2">-4.857(0.168) ***</td><td colspan="2">-0.871(0.159) ***</td><td colspan="2">-4.900(0.163) ***</td></tr><tr><td> $\beta_2$ </td><td colspan="2">-5(-Fixed)</td><td colspan="2">-1(-Fixed)</td><td colspan="2">-5(-Fixed)</td></tr><tr><td> $\beta_3$ </td><td colspan="2">-6.991(0.792) ***</td><td colspan="2">-2.092(0.621) ***</td><td colspan="2">-6.373(0.645) ***</td></tr><tr><td> $\mu$ </td><td colspan="2">9.186(0.369) ***</td><td colspan="2">2.263(0.741) **</td><td colspan="2">5.823(0.933) ***</td></tr><tr><td> $E_0$ </td><td colspan="2">10.974(0.176) ***</td><td colspan="2">3.091(0.634) ***</td><td colspan="2">7.187(0.792) ***</td></tr><tr><td> $\sigma_{E_0}^2$ </td><td colspan="2">10(-Fixed)</td><td colspan="2">10(-Fixed)</td><td colspan="2">10(-Fixed)</td></tr><tr><td> $ln\sigma_\delta^2$ </td><td colspan="2">3.716(0.203) ***</td><td colspan="2">3.247(0.241) ***</td><td colspan="2">4.317(0.270) ***</td></tr><tr><td> $ln\sigma_\eta^2$ </td><td colspan="2">3.466(0.319) ***</td><td colspan="2">2.695(0.250) ***</td><td colspan="2">2.313(0.273) ***</td></tr><tr><td> $P_{10}$ </td><td colspan="2">2.038(0.049) ***</td><td colspan="2">1.693(0.128) ***</td><td colspan="2">1.722(0.136) ***</td></tr><tr><td> $P_{20}$ </td><td colspan="2">1.976(0.049) ***</td><td colspan="2">1.703(0.138) ***</td><td colspan="2">1.738(0.149) ***</td></tr><tr><td> $P_{30}$ </td><td colspan="2">6.164(0.313) ***</td><td colspan="2">5.209(0.414) ***</td><td colspan="2">5.242(0.550) ***</td></tr><tr><td> $\sigma_{P_0}^2$ </td><td colspan="2">10(-Fixed)</td><td colspan="2">10(-Fixed)</td><td colspan="2">10(-Fixed)</td></tr><tr><td colspan="7">Note: Numbers in the parentheses are standard deviations for estimates.*** denotes significant at 0.001; ** denotes significant at 0.01; * denotes significant at 0.05.The mean and variance for three closing price distributions are the same as in Table 4.</td></tr></table>

The new sample was a group of 325 users who registered on a different day and who were observed long enough for their learning process to become stable. The estimation results are presented in the first column in Table 5. We observe the same signs and similar numerical values as the main model. The qualitative insights are robust against the different samples of users.

In the previous model estimation, $\beta _ { 2 }$ , which represents the average cognitive cost users incur from a Type 2 product auction on the website, was set at -5 for model identification purpose. We use $\beta _ { 2 } = - 1$ here for robustness check. The estimation results are presented in the second column in Table 5. All estimated parameters have the same sign as those reported in Table 4. Since the base value for identification is changed, the estimated numerical values also vary. However, the new values present similar relative relationships in magnitude. Hence, the estimation results are robust against the choice of base values.

In the base model, we use a loss indicator $L _ { i t }$ to indicate whether the user has consecutively lost a fixed number of auctions. We have chosen 15 consecutive auction losses as the threshold value. In the robustness test, we change the threshold value to 18. As seen from the third column in Table 5, the parameter estimates are all significant and are not significantly affected when the cumulative loss threshold value is changed.

## 6.4 Alternative Explanation

In the main model, we find there is an overestimation of the entertainment value in initial participation. As consumers gain more experiences, their entertainment belief converges to a lower value. We wonder whether we could alternatively interpret the “overestimation” effect as a natural decline of the perceived entertainment value due to tenure and participation experience.<sup>9</sup> We address this concern in this section.

Instead of using the Bayesian framework for entertainment belief updating in the main model, we assume a user’s perceived entertainment value is affected by her tenure and participation experience. The first model specifies that $E _ { i t } ^ { e } = E _ { 0 } + a *$ ?? ?? + ?? ∗ ???? ?? \_ $\dot { } d _ { i t } + c *$ ???? ?? $f r e e _ { i t }$ (Model A), where the constant is the perceived entertainment value at the beginning of the registration day. The second model specification takes the log transformation of tenure, so that $E _ { i t } ^ { e } =$ $E _ { 0 } + a * l o g ( t e n u r e _ { i t } ) + b * e x p e r i e n c e _ { - } p a i d _ { i t } +$ <sub>∗</sub> <sub>????</sub> <sub>??</sub> <sub>\_??</sub> (Model B). The third model assumes the perceived entertainment value takes an exponential decay functional form, converging to the true mean at the end of the observation period. The entertainment belief equation becomes $E _ { i t } ^ { e } = \mu +$ $e x p ( a * t e n u r e _ { i t } + b * e x p e r i e n c e _ { - } p a i d _ { i t } + c *$ ???? ?? $f r e e _ { i t } )$ (Model C). Keeping all the other variables the same as in the main model, Table 6 presents the estimated parameters in the entertainment belief equations from the three model specifications. For the purpose of comparison, we also present the full model parameter estimates in the fourth column.

Table 6. Effects of Tenure and Participation Experience on Entertainment Value

<table><tr><td>Parameters</td><td>Model A</td><td>Model B</td><td>Model C</td><td>Full model</td></tr><tr><td> $E_0$ </td><td>2.432 (0.166) ***</td><td>3.363 (0.179) ***</td><td>/</td><td>7.297 (0.512) ***</td></tr><tr><td>a</td><td>-0.067 (0.005) ***</td><td>-1.339 (0.104) ***</td><td>-1.071 (0.763)</td><td>/</td></tr><tr><td>b</td><td>0.093 (0.006) ***</td><td>0.092 (0.005) ***</td><td>-0.002 (0.196)</td><td>/</td></tr><tr><td>c</td><td>0.012 (0.028)</td><td>0.011 (0.020)</td><td>0.883 (0.160) ***</td><td>/</td></tr><tr><td>μ</td><td>/</td><td>/</td><td>5.070 (0.580) ***</td><td>6.017 (0.573) ***</td></tr><tr><td> $ln\sigma_{\delta}^{2}$ </td><td>/</td><td>/</td><td>/</td><td>4.281 (0.271) ***</td></tr><tr><td> $ln\sigma_{\eta}^{2}$ </td><td>/</td><td>/</td><td>/</td><td>2.086 (0.254) ***</td></tr><tr><td>Log likelihood</td><td>-1802.27</td><td>-1785.58</td><td>-1835.20</td><td>-1741.73</td></tr><tr><td>AIC</td><td>3644.54</td><td>3611.16</td><td>3710.40</td><td>3523.46</td></tr><tr><td>BIC</td><td>3826.43</td><td>3793.05</td><td>3892.29</td><td>3705.34</td></tr><tr><td>Plots for mean entertainment beliefs</td><td>Mean Entertainment Beler Day</td><td>Mean Entertainment Beler Day</td><td>Mean Entertainment Beler Day</td><td>Mean Entertainment Beler Day</td></tr></table>

![](/api/attachments/EP2762R9/fulltext/images/fab1c5154272aaf3a335079f18216c159b96bd0a82fec576fdd4018e18446286.jpg)

![](/api/attachments/EP2762R9/fulltext/images/528fb506074f0897e2f2fc0c75d6bd08229d93b137823c14b577d163b3b60578.jpg)

![](/api/attachments/EP2762R9/fulltext/images/d937236d714866a733d72915b138b1358b5a0d97a52f35c2cbdde272fb51c2c1.jpg)

![](/api/attachments/EP2762R9/fulltext/images/ff14db88373feae16dd6bf616059d1503a459e9551fec9962d1c709d2303567b.jpg)

In Model A and Model B, the negative coefficients for tenure indicate that users perceive high entertainment value at the beginning, and that the perceived entertainment value declines over time. However, this natural decline explanation suggests the users’ experienced entertainment values would keep decreasing. If the user stayed on the website long enough, their entertainment value would decrease to zero or even negative values (see the plots in the first two columns), which is not reasonable. In addition, the estimated coefficient c for free auction participation is insignificant, indicating that participating in free auctions has no significant impact on perceived entertainment value. This is inconsistent with our data. As shown in Figure C1 in the Appendix, the free top-up cards auctions generated the lowest revenue over retail value (measured at 0.51CNY) among all the auction categories. The website loses money by offering these auctions as an effort to increase the website’s entertainment value to attract and retain users.

Model C produces a quick decline of entertainment belief, which stabilizes at value 5.07. In comparison, our full model shows that users overestimate the entertainment value (7.297) at the beginning and the entertainment belief converges to the true value of 6.017. Compared with Model A and Model B, although Model C produces entertainment belief curves closer to our own, the log likelihood, AIC, and BIC values indicate Model C has the poorest data fit.

Clearly, our model outperforms these alternative models. We believe the main reason is that our model can account for heterogeneity of user behaviors while Models A-C fail to do so. By assuming different latent classes, our model takes heterogeneity in user learning into account in the following ways. First, our model allows users to have heterogeneous beliefs. Second, since entertainment values are unobservable, we randomly generated the paid and free entertainment signals from a normal distribution based on each user’s daily participation experience. Both the values of signals and the frequency of the user’s participation per day were taken into consideration in the entertainment belief updating. The signal generation process and the Bayesian belief update framework take a wide range of user experiences and behavioral patterns into account.

In summary, a learning model based on Bayesian belief updating provides more explanatory power than models using some independent variables to directly reflect the change of entertainment belief. Similar to Ghose & Han (2014) who assume there is a true “content match value” on the mobile Internet, we assume there is a true entertainment value on the entertainment shopping website. Learning models have been frequently used in new products and in introductions to services. Thus, learning naturally occurs when new users first register on the website. As the users interact more with the website, the learning process reveals the true website entertainment value and converges with its underlying true measure.

## 6.5 Moderating Effects of Observable Characteristics on Learning

We further examine heterogeneity of learning to identify whether users’ observable characteristics moderate their learning effectiveness. We characterize users with two indicators: $I _ { - } W i n = 1$ for users who have winning experience and <sub>??\_?? =</sub>1 for users who are classified into the persistent group (we use the cutoff value of 5 auctions, since 20% of users in the sample participate in more than five auctions).

In the main model, we assume that all users have the same level of precision (the same variance from a normal distribution) in generating their entertainment signals and auction closing price signals, respectively. Taking into account the learning heterogeneity, we modify the variances for entertainment signals and closing price signals as $v a r _ { e n t } + d * I n d i c a t o r *$ $v a r _ { e n t } .$ , and $v a r _ { p r i c e } + e * I n d i c a t o r * v a r _ { p r i c e }$ . For the indicator variable, we use in Model D and in Model E.

Table 7 presents the empirical results. Both and <sub>??\_??</sub> have shown a positive moderation effect ( =1.548 in Model D and =2.717 in Model E) on entertainment signal variance. It suggests that learning of the true entertainment value from users who have winning experience is less effective than learning from those who do not have winning experience.

Table 7. Moderating Effects of Observable Characteristics on Learning Mechanism

<table><tr><td>Parameters</td><td>Model D</td><td>Model E</td></tr><tr><td>d</td><td>1.548 (0.281) ***</td><td>2.717 (0.724) ***</td></tr><tr><td>e</td><td>0.008 (0.043)</td><td>0.087 (0.037) *</td></tr><tr><td colspan="3">Note: Standard errors are in parentheses.*** denotes significant at 0.001; * denotes significant at 0.05.</td></tr></table>

One possible explanation is the joy of winning. Bidders who have previously won auction games obtained higher entertainment signals and perceived higher entertainment value than those who had no winning experience. Inaccurate signals with larger variance tend to delay users’ discovery of the true entertainment value.

In comparison, the moderating effect of both past winning and persistent participation on the price learning mechanism is not as significant as entertainment learning. The positive effect is either nonsignificant ( =0.008, p-value=0.043) or only marginally significant at the 0.05 level ( =0.087, p-value=0.037).

## 7 Policy Simulations

Our empirical model analysis helps us gain a better understanding of users’ participation behaviors on entertainment auction websites. Since structural models allow for counterfactual analyses, we perform a set of policy experiments in this section. Our objective is to recommend some plausible policy changes to help the website designer address the consumer churn problem, which is a pain point in the current entertainment shopping industry.

Because the number of daily active users reflects the operating performance of web-based shopping platforms (Astonkar & Buchade, 2015), we use the percentage of active users per day as our performance measure. For each policy design, we simulate 2,000 iterations with estimated parameters and use the average performance measure to assess the effects of the policy changes. Based on three key learning model components, Table 8 summarizes our policy questions and the corresponding policy simulation designs.

Table 8. Policy Simulations Design

<table><tr><td>Model components</td><td>Policy questions</td><td>Simulation designs</td></tr><tr><td>Paid auction learning</td><td>Should the website disclose historical auction closing prices?</td><td>Increase the auction closing price signal variance,  $\sigma_{\zeta_j}^2$ , by 20% and 50%.</td></tr><tr><td>Free auction learning</td><td>Should the website offer new users free auction bids?</td><td>Remove all free auctions by setting  $f_{it}$  for all users at zero.</td></tr><tr><td>Auction competition learning</td><td>Should the website limit the auction competition?</td><td>Reduce the true mean closing prices,  $P_j$ , by 20% and 50%.</td></tr></table>

## 7.1 Should the Website Disclose Historical Auction Closing Prices?

Because users update their perceptions about auction competition based on observed auction closing price signals, the website can strategically influence users’ observational learning. Because less information leads to higher uncertainty, the website can increase the auction closing price variances in a specific product category by disclosing partial historical auction information instead of full historical auction data.

To examine the effect of auction closing price signals on consumer learning, we increase the auction closing price signal variances by 20% and 50%, respectively. Figure 4 shows that these changes did not yield discernable effects on virtual product (Type 1) or general merchandise (Type 2) auctions. However, the percentage of daily active users for digital products (Type 3) auctions significantly increased. Two plausible reasons explain this observation. First, large closing price variances make consumer observational learning less effective, leading to continued underestimation of auction competition, because higher expected auction payoff attracts consumers. Second, higher uncertainty in auction competition stimulates risk-seeking consumers’ persistent interest in participation. Both factors potentially contribute to the increased number of daily active users on the website.

A key feature of the entertainment shopping website design is the uncertainty involved in the auction outcomes. By strategically disclosing less historical information, the website purposely makes observational learning less effective. As such, the website would benefit from this policy change. This finding is supported by current industry practice. For example, Quibids.com has already adopted this strategy. It displays only the nine most recent completed auctions for each auctioned product.

![](/api/attachments/EP2762R9/fulltext/images/125f0e934e7b230fd95aacd8c163cd9322187f251350a9e8e515ef1e6ca22c6d.jpg)

![](/api/attachments/EP2762R9/fulltext/images/9145c81b0ae2fa90a58f89807e14c0ba56a673758e3acf18607d41852b30ca5b.jpg)

![](/api/attachments/EP2762R9/fulltext/images/54204065f2e027a3aba573efc4ab3eb2724c317d76ea8e4a1818e7c834dd7f41.jpg)  
Figure 4. Percentages of Active Users After Varying Auction Closing Price Signals

## 7.2 Should the Website Offer New Users Free Auction Bids?

Our base model estimation shows that free auctions provide a more precise signal than paid auctions and that new users overestimate the entertainment value of the website at the beginning of their participation. Therefore, offering new users free auction bids enables them to participate in more free auctions, helping them to quickly discover the true entertainment value. The free auction bids thus might have the adverse effect of inducing some users to quit using the website early on rather than engaging them.

![](/api/attachments/EP2762R9/fulltext/images/6f00958a90bbdf27ec34653ff32065ec78498fcb60d860d1d855e20657132a47.jpg)

![](/api/attachments/EP2762R9/fulltext/images/9be0a09efdedc39ea40ad34270e4811d06d508a278f5a82fa023bf315cd9ec2f.jpg)

In this policy experiment, we eliminate all free auctions and set parameter $f _ { i t }$ for all users during the observation period at zero. Figure 5 shows that removing free auctions helps increase the expected percentage of active users on the website, even though the effect is not significant.

![](/api/attachments/EP2762R9/fulltext/images/6819764f16bc46e0f966c68b60413c450c8f319f3a5d8a4421de659fd5445374.jpg)  
Figure 5. Percentages of Active Users without Free Auctions

Although providing free auction bids at the time of registration helps attract new users, it has the negative effect of allowing consumers who have quickly learned the true entertainment values to quit after a few trials on the free auctions. If the website aims to engage users, it should provide free auctions to users who have stayed on the website for a relatively long time. These users, if they are still active after having participated in many auctions, have already learned the true entertainment value. Free auction bids can be offered to these persistent users to better engage them in the entertainment auction environment. For example, it would be an effective strategy to award free auction bids to winners who upload pictures of their winning products or who frequently share their winning experiences.

## 7.3 Should the Website Limit the Auction Competition?

To create a fair auction environment and to avoid jump bidding (i.e., bidders enter an auction after others have placed a considerable number of bids), some websites have introduced locked auctions. For example, QuiBids.com has imposed a time limit: After a certain point, auctions become locked, and only bidders who have been participating are able to continue placing bids, while all other bidders are “locked out.” Compared with the free entry rule, setting a time limit helps restrict the total number of participants in an auction after the auction has already been running for some time, thereby protecting the bidders who have already sunk bidding fees into the early stages of the game. This policy has the potential effect of reducing auction closing prices, since our data shows that auction closing price is positively correlated with the total number of bidders in an auction (see Table D2 in Appendix D). Consequently, it directly affects the expected revenue of the auction.

Because average auction competition is reflected by mean closing prices, this policy simulation limits average auction competition through controlling closing prices. We reduce the true mean values of auction closing price for each type of auction, $P _ { j } ,$ by 20% and 50% but keep other parameters the same as the estimated values. Figure 6 presents the percentage of active users under different policies.

![](/api/attachments/EP2762R9/fulltext/images/8c561267cf9007ba6f60f01f025540be9c57817c5c9b426dd71b1570c7090b6b.jpg)

![](/api/attachments/EP2762R9/fulltext/images/399bb5a5b7ec33b81c23fe690438f59b1cfa93189530e790536ce83907d2fcc1.jpg)

![](/api/attachments/EP2762R9/fulltext/images/50f3fbfd08516c628d10cfbb0f308fd8e695b0babc321eea1e7deba0c2eefde0.jpg)  
Figure 6. Percentage of Active Users After Reducing Auction Closing Prices

The results indicate that the virtual product category has the highest percentage increase in active users, whereas the digital product category has the lowest percentage increase. This observation suggests that introducing policies such as “locked auction” to limit auction competition is more effective in the virtual product category than in other categories. Although controlling the auction competition in the highly demanded digital product category is helpful, it does not help retain users as much as it does in the other product categories.

## 8 Discussion and Conclusion

The unique selling mechanism of pay-to-bid auctions has attracted both consumers and businesses, resulting in the proliferation of numerous entertainment shopping websites worldwide in recent years. Despite their huge revenue potential, many of these websites have ceased operations after only a short period of time, throwing doubts on the entertainment shopping concept and the sustainability of the business model.

This study proposes a dynamic structural model of consumer learning to understand consumer participation and churn behaviors in different categories of product auctions. We also conducted policy simulations to evaluate the potential effects of policy changes on consumer participation to address the observed consumer churn issues.

Our model captures consumer learning on the basis of both the consumers’ own participation experience and observational learning on the website. Both types of learning are important in influencing the participation behavior of consumers. In particular, new consumers tend to significantly overestimate the entertainment value but underestimate the level of competition during the beginning stages of their participation. This finding helps explain the overall decreasing participation and increasing churn rate observed over time. Moreover, our model estimation segments consumers into two groups based on their participation behavior: one group of risk-averse users quits the website quickly, even before they learn its true entertainment value; the other group of risk-seeking users can fully discover the entertainment benefit, is likely to be addicted to the auction games, and persists on the website for a longer period of time.

Our empirical findings offer several website design implications for consumer churn management. Since the cognitive cost negatively impacts consumer utility, we suggest automatic bidding tools to reduce consumers’ cognitive costs of participation. The website can also provide more auctions in the virtual product category because this category incurs the lowest nonmonetary participation cost. Since the entertainment value positively affects consumer utility, we suggest more game design features to increase the potential entertainment value on the website. All these efforts undoubtedly enhance user experience.

Our policy simulation further shows the effectiveness of disclosing less historical information on customer retention. This is achieved by weakening the effect of consumers’ observational learning. In addition, we find that offering free auction bids to new users has an adverse effect on their participation. More participation in free auctions would allow new users to more quickly learn of the entertainment value and may induce them to quit early. Instead, the website should offer free auction bids to users who have been active for a while to better engage them in the entertainment shopping environment. Finally, we find that locked auctions are actually beneficial in retaining active users, especially in the virtual product category.

The insights gained in this research could be generalized to other similar selling mechanisms that combine the elements of auction and lottery. For example, Raviv and Virag (2009) analyzed a different selling mechanism in which the auction charges each bidder an entry fee, the bidders submit sealed bids, and the winning bid is the highest unique bid among all bids received. More generally, the method of modeling consumers’ risk attitude together with consumer learning based on both latent and observable variables is relevant in other consumer decision-making contexts, such as crowdsourcing contests. Not only does our model provide insights relevant to industries experiencing frequent consumer churns, but it is also relevant to other industries involving information disclosure and firms that strategically interact with consumers. For example, film studios sometimes purposely withhold movies from critics before their release because moviegoers often overestimate the quality of unreviewed movies. Firms may examine what level of information disclosure is optimal to profitably exploit consumer bias.

The current model has several limitations. First, because the research focus is on consumers’ learning across different categories of product auctions, consumers’ in-game experience is not explicitly incorporated into the model. Although some recent research in penny auctions has attempted to model consumers’ bidding strategies in each stage of the auction bidding game (Byers et al., 2010; Platt et al., 2013; Augenblick, 2016), these models use equilibrium types of analysis without capturing the behavior aspects of consumer decision-making. A possible future avenue would be to build a micro level behavior model to study consumers’ bidding strategies in unique entertainment auctions.

Second, consumers are heterogeneous in nature and may have different educational backgrounds, income, and budget constraints, risk attitudes, and shopping interests. Because we do not have access to data that includes these consumer characteristics, our model cannot capture such heterogeneity. Thus, future research might use surveys and lab experiments to collect the behavior data of individual consumers. An enriched model would offer more valuable insights that are not available from this study.

Finally, we consider the consumer’s participation decision as a myopic decision problem based on the consumer’s current information set, beliefs about the entertainment value, and perceptions about auction competition. Future research might build a dynamic optimization model to study consumers’ forwardlooking behavior in managing a portfolio of auction participation, subject to consumers’ personal total budget constraints, to improve their overall experiences on entertainment shopping websites.

## Acknowledgments

This research was supported by the Natural Science Basic Research Plan in the Shaanxi Province of China (2017JQ7012), Chinese Fundamental Research Funds for Central Universities (JB180602), the National Natural Science Foundation of China (71602153), and the Research Grants Council of the Hong Kong Special Administrative Region, China (Project No. 11507817).

## References

Adam, M. T. P., Krämer, J., & Müller, M. B. (2015). Auction fever! How time pressure and social competition affect bidders’ arousal and bids in retail auctions. Journal of Retailing, 91(3), 468- 485.

Adam, M. T. P., Krämer, J., & Weinhardt, C. (2012). Excitement up! Price down! Measuring emotions in Dutch auctions. International Journal of Electronic Commerce, 17(2), 7-40.

Angst, C. M., Agarwal, R., & Kuruzovich, J. (2008). Bid or buy? Individual shopping traits as predictors of strategic exit in on-line auctions. International Journal of Electronic Commerce, 13(1), 59-84.

Ariely, D., & Simonson, I. (2003). Buying, bidding, playing, or competing? Value assessment and decision dynamics in online auctions. Journal of Consumer Psychology, 13(1-2), 113-123.

Astonkar, M. R., & Buchade, A. (2015). Analytics: Building mobile game-users insights using parameter. International Journal of Computer Science and Mobile Computing, 4(6), 844-853.

Augenblick, N. (2016). The sunk-cost fallacy in penny auctions. Review of Economic Studies, 83(1), 58-86.

Babin, B. J., Darden, W. R., & Griffin, M. (1994). Work and/or fun: Measuring hedonic and utilitarian shopping value. Journal of Consumer Research, 20(4), 644-656.

Bapna, R., Jank, W., & Shmueli, G. (2008). Consumer surplus in online auctions. Information Systems Research, 19(4), 400-416.

Bockstedt, J., & Goh, K. H. (2012). Seller strategies for differentiation in highly competitive online auction markets. Journal of Management Information Systems, 28(3), 235-268.

Byers, J. W., Mitzenmacher, M., & Zervas, G. (2010). Information asymmetries in pay-per-bid Auctions: How Swoopo makes bank. In Proceedings of the 11th ACM Conference on Electronic Commerce.

Camerer, C. F., Ho, T., & Chong, J. (2004). A cognitive hierarchy model of games. Quarterly Journal of Economics, 119(3), 861-898.

Deci, E. L., Betley, G., Kahle, J., Abrams, L., & Porac, J. (1981). When trying to win: Competition and intrinsic motivation. Personality and Social Psychology Bulletin, 7(1), 79-83.

Desarbo, W. S., Kamakura, W. A., & Wedel, M. (2006). Latent structure regression. In R.

Grover & M. Vriens. The handbook of marketing research: Uses, misuses, and future (pp. 394-417). New York, NY: SAGE.

DeGroot, M. H. (1970). Optimal statistical decisions. New York, NY: McGraw-Hill.

Easley, R. F., Wood, C. A., & Barkataki, S. (2011). Bidding patterns, experience, and avoiding the winner’s curse in online auctions. Journal of Management Information Systems, 27(3), 241- 268.

Erdem, T., & Keane, M. P. (1996). Decision-making under uncertainty: Capturing dynamic brand choice processes in turbulent consumer goods markets. Marketing Science, 15(1), 1-20.

Erdem, T., Keane, M. P., & Sun, B. (2008). A dynamic model of brand choice when price and advertising signal product quality. Marketing Science, 27(6), 1111-1125.

French, K. R., & McCormick, R. E. (1984). Sealed bids, sunk costs, and the process of competition. The Journal of Business, 57(4), 417-441.

Ghose, A., & Han, S. P. (2014). A dynamic structural model of user learning on the mobile Internet (NET Institute working paper, no. 09-24).

Goes, P. B., Karuga, G. G., & Tripathi, A. K. (2010). Understanding willingness-to-pay formation of repeat bidders in sequential online auctions. Information Systems Research, 21(4), 907-924.

Hinnosaar, T. (2016). Penny auctions. International Journal of Industrial Organization, 48, 59-87.

Holbrook, M. B., & Hirschman, C. (1982). The experiential aspects of consumption: Consumer fantasies, feelings, and fun. Journal of Consumer Research, 9(2), 132-140.

Hong, Y., & Pavlou, P. A. (2014). Product fit uncertainty in online markets: Nature, effects, and antecedents. Information Systems Research, 25(2), 328-344.

Huang, Y., Singh, P. V., & Srinivasan, K. (2014). Crowdsourcing new product ideas under consumer learning. Management Science, 60(9), 2138-2159.

Iyengar, R., Ansari, A., & Gupta, S. (2007). A model of consumer learning for service quality and usage. Journal of Marketing Research, 44(4), 529-544.

Ku, G., Malhotra, D., & Murnighan, J. K. (2005). Towards a competitive arousal model of decision-making: A study of auction fever in live and Internet auctions. Organizational Behavior & Human Decision Processes, 96(2), 89-103.

Malmendier, U., & Lee, Y. H. (2011). The bidder’s curse. American Economic Review, 101(2), 749-787.

McFadden, D. (1989). A method of simulated moments for estimation of discrete response models without numerical integration. Econometrica, 57(5), 995-1026.

McGee, P. (2013). Bidding in private-value auctions with uncertain values. Games and Economic Behavior, 82, 312-326.

Narayanan, S., & Manchanda, P. (2009). Heterogeneous learning and the targeting of marketing communication for new products. Marketing Science, 28(3), 424-441.

Platt, B. C., Price, J., & Tappen, H. (2013). The role of risk preferences in pay-to-bid auctions. Management Science, 59(9), 2117-2134.

Popkowski Leszczyc, P. T. L., Qiu, C., & He, Y. (2009). Empirical testing of the reference-price effect of buy-now prices in Internet auctions. Journal of Retailing, 85(2), 211-221.

Raviv, Y., & Virag, G. (2009). Gambling by auctions. International Journal of Industrial Organization, 27(3), 369-378.

Reiner, J., Natter, M., & Skiera, B. (2014). The impact of buy-now features in pay-per-bid auctions.

Journal of Management Information Systems, 31(2), 77-104.

Staw, B. M. (1976). Knee-deep in the big muddy: A study of escalating commitment to a chosen course of action. Organizational Behavior and Human Performance, 16(1), 27-44.

Sun, H. (2010). Sellers’ trust and continued use of online marketplaces. Journal of the Association for Information Systems, 11(4), 182-211.

Teubner, T., Adam, M., & Riordan, R. (2015). The impact of computerized agents on immediate emotions, overall arousal and bidding behavior in electronic auctions. Journal of the Association for Information Systems, 16(10), 838-879.

Van der Heijden, H. (2004). User acceptance of hedonic information systems. MIS Quarterly, 28(4), 695-704.

Wang, Z., & Xu, M. (2016). Selling a dollar for more than a dollar? Evidence from online penny auctions. Information Economics and Police, 36, 53-68.

Zhao, Y., Yang, S., Narayan, V., & Zhao, Y. (2013). Modeling consumer learning from online product reviews. Marketing Science, 32(1), 153-169.

## Appendix A: Notation Table

Table A1: Notation Table

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $\alpha_g$ </td><td>Sensitivity to auction competition for  $g^{th}$  latent segment</td></tr><tr><td> $\beta_j$ </td><td>Auction category-specific (or type-specific) cognitive cost</td></tr><tr><td> $r_g$ </td><td>Users&#x27; risk preference toward variation in closing price for  $g^{th}$  latent segment</td></tr><tr><td> $\varepsilon_{ijt}$ </td><td>Error term</td></tr><tr><td> $\lambda_g$ </td><td>Vector of covariates contained in  $S_{it}$  for  $g^{th}$  latent segment</td></tr><tr><td> $\mu$ </td><td>The true mean of website entertainment value</td></tr><tr><td> $\pi_g$ </td><td>Segment membership probability for  $g^{th}$  latent segment</td></tr><tr><td> $\sigma_\delta^2$ </td><td>Variance of the experience signal for paid auctions</td></tr><tr><td> $\sigma_\zeta_j^2$ </td><td>Variance of the observed type  $j$  auctions&#x27; closing price signals</td></tr><tr><td> $\sigma_\eta^2$ </td><td>Variance of the experience signal for free auctions</td></tr><tr><td> $\sigma_{E0}^2$ </td><td>Variance of users&#x27; prior belief about the website entertainment value</td></tr><tr><td> $\sigma_{E_{it}}^2$ </td><td>User  $i$ &#x27;s posterior variance of the entertainment value at the end of day  $t$ </td></tr><tr><td> $\sigma_{P_0}^2$ </td><td>Variance of users&#x27; prior belief about the auction closing price</td></tr><tr><td> $\sigma_{P_{jt}}^2$ </td><td>Users&#x27; posterior variance of type  $j$  auction closing price at the end of day  $t$ </td></tr><tr><td> $A_{ijt}$ </td><td>User  $i$ &#x27;s participation decision for type  $j$  auction on day  $t$ </td></tr><tr><td> $A$ </td><td>Action matrix for  $N$  users toward  $J$  types of auctions over the period  $T$ </td></tr><tr><td> $E_{i0}$ </td><td>User  $i$ &#x27;s prior belief about the website entertainment value</td></tr><tr><td> $E_0$ </td><td>The mean of users&#x27; prior belief about the website entertainment value</td></tr><tr><td> $E_{its}^p$ </td><td>User  $i$ &#x27;s  $s^{th}$  paid auction experience signal on day  $t$ , following  $N(\mu, \sigma_\delta^2)$ </td></tr><tr><td> $E_{itm}^f$ </td><td>User  $i$ &#x27;s  $m^{th}$  free auction experience signal on day  $t$ , following  $N(\mu, \sigma_\eta^2)$ </td></tr><tr><td> $E_{it}^p$ </td><td>User  $i$ &#x27;s aggregated paid auction signals on day  $t$ , following  $N(\mu, \sigma_\delta^2 / n_{it})$ </td></tr><tr><td> $E_{it}^f$ </td><td>User  $i$ &#x27;s aggregated free auction signals on day  $t$ , following  $N(\mu, \sigma_\eta^2 / f_{it})$ </td></tr><tr><td> $E_{it}$ </td><td>User  $i$ &#x27;s posterior mean of the entertainment value at the end of day  $t$ </td></tr><tr><td> $E_{it}^e$ </td><td>Website entertainment value user  $i$  perceives on day  $t$ </td></tr><tr><td> $f_{it}$ </td><td>Number of free auctions in which user  $i$  participated on day  $t$ </td></tr><tr><td> $g$ </td><td>Latent class membership</td></tr><tr><td> $I_{it}$ </td><td>User  $i$ &#x27;s information set at the beginning of day  $t$ </td></tr></table>

Table A1: Notation Table

<table><tr><td> $L_{it}$ </td><td>A loss indicator for whether a user has lost a number of auctions consecutively</td></tr><tr><td> $M_{it}^{c}$ </td><td>User i&#x27;s cumulative wealth up to day t</td></tr><tr><td> $M_{it}^{l}$ </td><td>User i&#x27;s earning during the previous day t-1 (at the beginning of day t)</td></tr><tr><td> $n_{it}$ </td><td>Number of paid auctions in which user i participated on day t</td></tr><tr><td> $P_{ij0}$ </td><td>User i&#x27;s prior belief about category j auction closing price</td></tr><tr><td> $P_{j0}$ </td><td>The mean of users&#x27; prior belief about type j auction closing price</td></tr><tr><td> $P_{ijt}$ </td><td>User i&#x27;s observed closing price signal for category j auction on day t</td></tr><tr><td> $P_{jt}$ </td><td>Users&#x27; posterior mean of type j auction closing price at the end of day t</td></tr><tr><td> $P_{j}$ </td><td>The true mean closing price of type j auctions</td></tr><tr><td> $S_{it}$ </td><td>Vector of user- and time-specific covariates</td></tr><tr><td> $U_{ijt}$ </td><td>User i&#x27;s utility from participating in a category j auction on day t</td></tr><tr><td> $\tilde{U}_{ijt}$ </td><td>User i&#x27;s expected utility from participating in a category j auction on day t</td></tr></table>

Appendix B: Screen Shots for Entertainment Auction Websites  
![](/api/attachments/EP2762R9/fulltext/images/9418de54f8890f8a39b2e006facc2a51ab0926237b6927fd77eec4a7674e37fc.jpg)

① Product Description: It includes the product name, feature, photo and the market retail price (CNY 2099).

② Ongoing Auction Status: It presents the current price (CNY 41.44) and current winner / leader (username: weinanzhiye) in this ongoing auction.

③ Countdown Clock: Every bid restarts the countdown clock to a maximum of 10 seconds.

④ Bidding Rule: It indicates a fixed number of bidding tokens required for every new bid.

⑤ Bid Now Button: Registered users can click to place a bid. It costs 2 bidding tokens, as indicated by ④. The current price in ② increases by CNY 0.02, and the current winner changes to this new username. The countdown clock in ③ restarts to 10 seconds.

Figure B1. Screen Shot for 5Pai.com

![](/api/attachments/EP2762R9/fulltext/images/36cb620c987cc6058d09ffb2d3965c46181285122ba3f6daae6793a03dd4c360.jpg)  
Note:  
1) 9Pai.net is an entertainment auction site in China that employs a website design and selling mechanism that are very similar to those of 5Pai.com.  
2) Quibids.com is the largest entertainment auction site in the United States.  
Figure B2. Screen Shots for 9Pai.net and Quibids.com

## Appendix C: Descriptive Statistics

Table C1 summarizes the statistics in terms of the total number of auctions, total revenue, and total value of products sold on the website (which is based on the listed retail prices of the products).

Table C1. Auctions and Auctioneer Revenue by Products<sup>a</sup>

<table><tr><td>Products</td><td>No. of Auctions</td><td>Total revenue (CNY)</td><td>Total value (CNY)</td></tr><tr><td>Bid packs</td><td>2,967</td><td>824,376</td><td>131,270</td></tr><tr><td>Gift &amp; top-up cards</td><td>5,344</td><td>450,691</td><td>190,549</td></tr><tr><td>Fashion, health &amp; beauty</td><td>1,710</td><td>382,859</td><td>401,349</td></tr><tr><td>Hobbies &amp; outdoors</td><td>1,050</td><td>141,235</td><td>168,666</td></tr><tr><td>Home, garden &amp; tools</td><td>1,641</td><td>304,959</td><td>347,314</td></tr><tr><td>Kitchen &amp; dining</td><td>1,226</td><td>288,117</td><td>272,216</td></tr><tr><td>Computers &amp; laptops</td><td>225</td><td>839,148</td><td>432,818</td></tr><tr><td>Portable electronics</td><td>2,413</td><td>4,130,030</td><td>1,997,878</td></tr><tr><td>Digital accessories</td><td>4,887</td><td>709,996</td><td>802,862</td></tr><tr><td>Total</td><td>21,463</td><td>8,071,410</td><td>4,744,922</td></tr></table>

<sup>a</sup> We used the retail prices listed on the website, which might not be the same as the real retail prices in other online or physical stores.

![](/api/attachments/EP2762R9/fulltext/images/38d07fc981fb7f631344dbfba9e33a8c4bbf2b6909242461084b5f950524607c.jpg)  
Figure C1. Revenue over Retail Value (CNY) by Product Category

To measure the average profitability of the auctions under different product categories, we define the revenue over retail value in CNY as the ratio of the average revenue from the auctions to the average listed retail prices in a product category. Figure C1 shows the average profitability.

We see that the most profitable auction category on the website is the bid pack category, the average revenue of which is 6.28 times its value. It is calculated as follows: A bid pack of 10 bids has a value of CNY10. On average, the auction collects bidding fees of CNY62.8, so the revenue over retail value in CNY for the bid pack is 6.28.

The second most profitable product category is Apple products (the average revenue over retail value, in CNY, is 3.22). The third most profitable product category is top-up cards of different face values (2.76). In contrast, the website loses money in categories with revenue over retail value (CNY) of less than 1. However, these auctions represent more than 58% of all the auctions conducted on the website. We believe that the website offers these nonprofitable auctions to attract and retain active users because a healthy number of active users is the most important determinant for the website’s sustainability.

## Appendix D: Additional Empirical Tests

## D1. Users’ Bidding Skills

The regression results in Table D1 indicate that the number of participations and observed auctions by a user did not significantly affect the average profit per bid of the user.

Table D1. Regression Tests for Users’ Bidding Skill

<table><tr><td colspan="3">Dependent variable: profit per bid</td></tr><tr><td>Independent variables</td><td colspan="2">Coefficients</td></tr><tr><td># of participated auctions</td><td>-0.0008(0.0003)</td><td>-0.0062(0.0030) *</td></tr><tr><td>Log # of provided auctions</td><td>0.0003(0.0005)</td><td>0.0008(0.0008)</td></tr><tr><td>Auction-type fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Individual fixed effects</td><td>No</td><td>Yes</td></tr><tr><td>R-square</td><td>0.0164</td><td>0.1627</td></tr><tr><td colspan="3">Note: Standard errors are in parentheses. * denotes significant at 0.05.</td></tr></table>

## D2. Auction Competition

In the main model, the auction closing price is used as a proxy for auction competition. Using the 17,930 paid auction observations, the regression results show that the number of participants in the auction has a significant positive effect on the auction closing price.

Table D2. Regression Tests for Auction Competition

<table><tr><td colspan="3">Dependent variable: auction closing price</td></tr><tr><td>Independent variables</td><td colspan="2">Coefficients</td></tr><tr><td># of participants in the auction</td><td>1.103(0.010) ***</td><td>1.130(0.010) ***</td></tr><tr><td>Retail price stated by auctioneer</td><td>0.016(0.000) ***</td><td>-0.010(0.004) *</td></tr><tr><td>Auction-type fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Product-type fixed effects</td><td>No</td><td>Yes</td></tr><tr><td>R-square</td><td>0.6882</td><td>0.7738</td></tr><tr><td colspan="3">Note: Standard errors are in parentheses.*** denotes significant at 0.001; * denotes significant at 0.05.</td></tr></table>

## Appendix E: The Conditional Expected Utility

The conditional expected utility is expressed as:

$$
E \big [ U _ {i j t} \big | I _ {i t} \big ] = E [ E _ {i t} ^ {e} | I _ {i t} ] + \beta_ {j} + \alpha_ {g} E \big [ P _ {i j t} \big | I _ {i t} \big ] + \alpha_ {g} r _ {g} E \big [ P _ {i j t} ^ {2} \big | I _ {i t} \big ] + \lambda_ {g} ^ {\prime} E [ S _ {i t} | I _ {i t} ] + \varepsilon_ {i j t}.
$$

For linear terms in the utility function, we simply have $E [ E _ { i t } ^ { e } | I _ { i t } ] = E _ { i , t - 1 }$ and $E \big [ P _ { i j t } \big | I _ { i t } \big ] = P _ { j , t - 1 }$ through the Bayesian belief update. The conditional expectation of the covariates contained in $S _ { i t }$ is $\lambda _ { g } ^ { \prime } E [ S _ { i t } | I _ { i t } ] = \lambda _ { g 1 } M _ { i t } ^ { l } +$ $\lambda _ { g 2 } M _ { i t } ^ { c } + \lambda _ { g 3 } L _ { i t }$

For the nonlinear term in the utility function, note that $P _ { i j t } { \sim } N \left( P _ { j } , \sigma _ { \zeta _ { j } } ^ { 2 } \right)$ . We write $P _ { i j t } = P _ { j , t - 1 } + \left( P _ { j } - P _ { j , t - 1 } \right) + \zeta _ { i j t }$ Since $E \big [ P _ { i j t } \big | I _ { i t } \big ] = E \big [ P _ { j } \big | I _ { i t } \big ] = P _ { j , t - 1 }$ and $V a r [ X ] = E [ X ^ { 2 } ] - E [ X ] ^ { 2 }$ , the expectation for the closing price conditioned on the information set can be expressed as:

$$
\begin{array}{r l} & E \big [ P _ {i j t} ^ {2} \big | I _ {i t} \big ] \\ & = E \left[ \big (P _ {j, t - 1} + \big (P _ {j} - P _ {j, t - 1} \big) + \zeta_ {i j t} \big) ^ {2} \Big | I _ {i t} \right] \\ & = E \left[ P _ {j, t - 1} ^ {2} + \big (P _ {j} - P _ {j, t - 1} \big) ^ {2} + \zeta_ {i j t} ^ {2} + 2 P _ {j, t - 1} \big (P _ {j} - P _ {j, t - 1} \big) + 2 P _ {j, t - 1} \zeta_ {i j t} + 2 \big (P _ {j} - P _ {j, t - 1} \big) \zeta_ {i j t} \Big | I _ {i t} \right] \\ & = P _ {j, t - 1} ^ {2} + E \left[ \big (P _ {j} - P _ {j, t - 1} \big) ^ {2} \Big | I _ {i t} \right] + E \big [ \zeta_ {i j t} ^ {2} \big | I _ {i t} \big ] + 2 E \big [ P _ {j, t - 1} P _ {j} - P _ {j, t - 1} ^ {2} \big | I _ {i t} \big ] \\ & = P _ {j, t - 1} ^ {2} + E \left[ \big (P _ {j} - P _ {j, t - 1} \big) ^ {2} \Big | I _ {i t} \right] + V a r \big (\zeta_ {i j t} | I _ {i t} \big) + \big (E \big [ \zeta_ {i j t} | I _ {i t} \big ] \big) ^ {2} + 2 P _ {j, t - 1} ^ {2} - 2 P _ {j, t - 1} ^ {2} \\ & = P _ {j, t - 1} ^ {2} + E \big [ (P _ {j} - P _ {j, t - 1}) ^ {2} \big | I _ {i t} \big ] + \sigma_ {\zeta_ {j}} ^ {2}. \end{array}
$$

Therefore, the conditional expected utility of user <sub>??</sub> is expressed as:

$$
\begin{array}{r l} & E \big [ U _ {i j t} \big | I _ {i t} \big ] = E [ E _ {i t} ^ {e} | I _ {i t} ] + \beta_ {j} + \alpha_ {g} E \big [ P _ {i j t} \big | I _ {i t} \big ] + \alpha_ {g} r _ {g} E \big [ P _ {i j t} ^ {2} \big | I _ {i t} \big ] + \lambda_ {g} ^ {\prime} E [ S _ {i t} | I _ {i t} ] + \varepsilon_ {i j t} \\ & = E _ {i, t - 1} + \beta_ {j} + \alpha_ {g} P _ {j, t - 1} + \alpha_ {g} r _ {g} P _ {j, t - 1} ^ {2} + \alpha_ {g} r _ {g} E \left[ (P _ {j} - P _ {j, t - 1}) ^ {2} \Big | I _ {i t} \right] + \alpha_ {g} r _ {g} \sigma_ {\zeta_ {j}} ^ {2} + \lambda_ {g 1} M _ {i t} ^ {l} + \lambda_ {g 2} M _ {i t} ^ {c} + \lambda_ {g 3} L _ {i t} + \varepsilon_ {i j t}. \end{array}
$$

## About the Authors

Jin Li is an assistant professor in the School of Economics and Management at Xidian University. He received his PhD in management science from City University of Hong Kong. His recent research interests include resource allocation and management in cloud computing, and consumer behaviors in electronic commerce. He has published papers in INFORMS Journal on Computing, Electronic Markets, Electronic Commerce Research, Electronic Commerce Research and Applications, and others.

Zhiling Guo is an associate professor of information systems at Singapore Management University. She received her PhD from The University of Texas at Austin. Her recent research focuses on innovative business models for digital payments, resource allocation and management in cloud computing, and data analytics to understand consumer decision-making. She has published papers in leading business and management journals, including Management Science, MIS Quarterly, Information Systems Research, INFORMS Journal on Computing, Journal of Management Information Systems, Production and Operations Management, among others.

Geoffrey Tso is an associate professor in the Department of Management Sciences and the director of the Statistical Consulting Unit at the City University of Hong Kong. He completed his PhD in biostatistics at the University of Toronto. His research interests include market research, economic indexes, energy research, and business intelligence. His research has appeared in Computational Statistics & Data Analysis, Energy, Social Indicators Research, Journal of the Association for Information Systems, Electronic Markets, Communications in Statistics: Simulation and Computation, and others. He has also conducted over 200 market research projects for organizations operating in Hong Kong.
