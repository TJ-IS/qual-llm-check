---
otero_id: 8516
otero_key: "ZVXN26GJ"
title: "Can “Gold Medal” Online Sellers Earn Gold? The Impact of Reputation Badges on Sales"
authors: "Hsing Kenneth Cheng; Weiguo Fan; Peipei Guo; Hailiang Huang; Liangfei Qiu"
year: "2020"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2020.1831776"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Check for updates

# Can “Gold Medal” Online Sellers Earn Gold? The Impact of Reputation Badges on Sales

Hsing Kenneth Cheng<sup>a</sup>, Weiguo Fan<sup>b</sup>, Peipei Guo<sup>c</sup>, Hailiang Huang<sup>c</sup>, and Liangfei Qiu<sup>a</sup>

<sup>a</sup>Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, Gainesville, Florida, USA; <sup>b</sup>Tippie College of Business, University of Iowa, Iowa City, Iowa, USA; <sup>c</sup>School of Information Management and Engineering, AI Lab, Shanghai University of Finance and Economics, Shanghai, China

## ABSTRACT

Reputation systems have been an important component for improvement of online markets’ eficiency by reducing uncertainty about the quality of the sellers. Most, if not all, reputation systems examined in the extant literature reflect the sellers’ long-term accumulative reputation, which has several drawbacks that impede accomplishing the intended goals of the reputation systems. Taobao.com, the largest consumer-to-consumer online market in China, implemented the Gold Medal Seller (GMS) program as a concurrent reputation mechanism to enhance its existing long-term accumulative reputation system. The GMS program presents a backdrop that allows us to address several intriguing research issues not empirically examined in prior literature. By adopting multiple causal identification strategies, we find that earning a reputation badge has a positive impact on sales, and losing a reputation badge has a negative impact on sales. More importantly, the signaling value of obtaining/losing a reputation badge is asymmetric: The magnitude of the efect of losing a reputation badge is four times larger than that of earning a badge. Moreover, consecutively keeping a reputation badge or earning it multiple times is a stronger signal for seller quality and has a larger positive impact on sales, which suggests that the marginal value of reputation badges increases. Our findings ofer a new and deeper understanding of the reputation system mechanism design.

## KEYWORDS

Reputation system; online markets; signaling; countersignaling; reputations badges

“Give a man a reputation as an early riser and he can sleep ‘til noon.” ― Mark Twain

“A good reputation is more valuable than fine perfume.” ― Ecclesiastes 7:1

## Introduction

Online markets have become an important part of modern life by allowing buyers and sellers to overcome temporal and geographical barriers to buy and sell products anytime and anywhere. Compared to ofline markets, online markets can provide more product selections with lower prices and higher eficiency [20, 27]. However, online retailers have yet to fully reap the benefits of online markets because of the existence of information asymmetry, which can lead to moral hazard, adverse selection, market ineficiency, or even market failure [1]. There are two sources of information asymmetry in online markets: the product uncertainty and the seller uncertainty. The uncertainty about the product and the seller prevents buyers from making the appropriate choice among sellers and products. High-quality products and sellers may be forced to leave the market since they could not be properly rewarded with fair prices due to their true quality not being correctly signaled, potentially creating a market of “lemons” [1] and reducing transaction activities below the socially optimal level. Therefore, reducing product and seller uncertainty is crucial to further promote the success of online marketplaces.

Product uncertainty, originally proposed in [5] as the uncertainty pertaining to the quality of the product in the medical care industry, has been found to be a major impediment to the eficiency of online markets [21, 25, 32]. Dimoka et al. [21, p. 401] define the product uncertainty as the “consumer’s dificulty in assessing the product’s characteristics and predicting how the product will perform in the future,” and identify description uncertainty and performance uncertainty as two major facets of the product uncertainty in online markets. They show that diagnostic product descriptions and third-party product assurances help reduce the product uncertainty using used cars online auctions data from eBay Motors. Hong and Pavlou [32] propose fit uncertainty as the third dimension of product uncertainty where fit uncertainty is defined as the degree to which a consumer cannot assess whether a product’s attributes match the consumer’s preference.

The reputation system is the most commonly used mechanism by online markets (e.g., Amazon, eBay, and Taobao) to address the seller uncertainty—the uncertainty about the quality of the sellers. Consequently, reputation system is one of the most active research topics online market literature focuses on. The predominant majority of the literature relating to seller reputation is studying the impact of sellers’ long-term accumulative reputation, the reputation garnered from the date when sellers first enrolled in the online markets. However, the long-term accumulative reputation has several disadvantages in alleviating the seller uncertainty. First, the efect of long-term accumulative reputation is assumed to be constant with respect to the change of time, while [6] find that the reputation efect was strongest in the short term but decayed thereafter. Second, the long-term accumulative reputation is usually a simple scalar quantity representing only one dimension but not the totality of the seller’s performance in transactions. This makes the long-term accumulative reputation susceptible to manipulation. For example, Nosko and Tadelis [53] argue that seller long-term accumulative reputation measures are coarse or biased. Dellarocas and Wood [19] also reveal the problem of skewed long-term accumulative reputation. Finally, the simple method of computing the long-term accumulative reputation, which increases by one for each good transaction and decreases by one for each bad transaction, allows the long-term accumulative reputation to keep growing indefinitely even if a seller cheats one buyer out of every four. It makes the longterm accumulative reputation incomparable among diferent sellers because if the seller sells frequently, he or she could have a higher reputation than someone who trades perfectly but has less than three quarters the number of sales [54].

The foregoing discussions show that current reputation systems based on sellers’ longterm accumulative reputation are one dimensional and susceptible to manipulation biases and that the reputation efect is strongest in the short term and then decays thereafter. An ideal reputation system should thus provide a measure that aggregates multiple dimensions of sellers’ short-term performance and has the property of an efective reputation system of “capture and distribution of feedback about current interactions” [61, p. 47]. Naturally, an intriguing research question arises. If such a short term comprehensive reputation exists, what is its efect on product sales? This question has not been examined empirically in the literature yet, which is most likely due to the lack of data.

Fortunately, Taobao.com, the largest online marketplace in China, announced the program of Gold Medal Seller (GMS) on July 1 2014, in which Taobao.com gives the GMS award (a reputation badge) to sellers based on their past short-term performance. The main criteria of the GMS program are based on the sellers’ comprehensive performance during a fifteen-day period, including transaction volume, percentage of positive feedback, detailed seller ratings, dispute rates, etc. The GMS badge is valid for only fifteen days after it is awarded, which has the same duration as the evaluation period. These features of the GMS program conform to those of a desirable short-term comprehensive reputation system that hasn’t been seen before the implementation of Taobao.com’s GMS.

Using a six-month panel data set (July 1<sup>st</sup> – December 31<sup>st</sup>, 2015) from Taobao.com, we aim at addressing the following research questions.

● Does the short-term reputation badge have any influence on product sales?

● What is the efect of losing or keeping a reputation badge compared with earning a badge?

● What is the moderating efect of earning reputation badges multiple times?

Regarding the first research question, our study finds that the short-term reputation badge indeed has a significant positive impact on product sales. It may be obvious that earning a reputation badge may diferentiate high-quality sellers from low-quality sellers. However, an empirical challenge lies in establishing the causal efect of reputation badges on product sales. The sellers that earn reputation badges might be systematically diferent from sellers who do not. Using several causal identification strategies, we provide a comprehensive understanding of the impact of reputation badges on product sales.

Prior research has not directly addressed our second research question on the efect of losing or keeping a reputation badge. We empirically find that losing a reputation badge has a negative impact on product sales. More interestingly, the signaling value of obtaining/losing a reputation badge is asymmetric: The magnitude of the efect of losing a reputation badge is larger than that of earning a badge. In addition, consecutively keeping a reputation badge is a stronger signal for seller quality and has a larger positive impact on product sales than earning a reputation badge.

Conventional wisdom would lead one to expect that the marginal value of earning an additional reputation badge decreases: Earning a reputation badge first time is important, and earning it second time is less important. However, the answer to the third research question suggests that the marginal value of earning reputation badges actually increases, which is consistent with the signaling theory. We find that as a seller earns more reputation badges, earning or keeping a reputation badge has a larger positive impact on product sales, and losing a badge has a smaller negative impact on product sales. The reason is that if a seller earns reputation badges multiple times, we are more likely to observe a separating equilibrium in which low-quality sellers are dificult to imitate high-quality sellers [64].

This study makes several important contributions to the literature and the industry practice. First, our research is among the first to empirically examine the efect of earning/ losing/keeping short-term reputation badge on product sales. Second, our research highlights the importance of introducing the possibility of losing badges in reputation system design. When losing reputation badge is possible, keeping a reputation badge or earning it multiple times has a larger signaling value for seller quality. Third, our results ofer useful insights to sellers on how they should manage their reputation efectively. In particular, our research shows that earning a reputation badge might be a double-edged sword for sellers: If a seller earns a badge and then loses it immediately in the next time period, consumers interpret it as a more negative signal than not earning a badge at all.

The remainder of this paper is structured as follows. We first review the relevant literature. For the sake of completeness, we provide a critical review of literature on both the product uncertainty and seller uncertainty. We note that our paper focuses on examining the role of short-term reputation badges in reducing seller uncertainty, not product uncertainty. We next describe the research setting, Taobao.com’s GMS program, in detail. We then formulate a set of research hypotheses on the efect of reputation badges. Following the research hypotheses, we present the research model and report major findings and robustness checks. Finally, we conclude with discussions on the implications of our findings, limitations, and suggestions for future research.

## Literature Review

## Product Uncertainty

Understanding the efect of product uncertainty has been an active research area in the literature of online markets. In the context of used car auctions on eBay Motors, Dimoka et al. [21] conceptualize product uncertainty into description uncertainty and performance uncertainty dimensions and identify the most influential information signals, such as diagnostic product descriptions and third-party product assurances, to reduce product uncertainty. Hong and Pavlou [32] identify product fit uncertainty and quality uncertainty as two distinct dimensions of product uncertainty. They show that product fit uncertainty has a significantly stronger efect on product returns than product quality uncertainty. By calibrating product-level uncertainty using product intangibility level, Kim and Krishnan [40] identify the interaction efect of product uncertainty and product price on online consumers’ purchase decision and show that online merchants can take advantage of their reputation in the physical world and the use of digitized video commercials to overcome product-level uncertainty efectively.

Word-of-mouth (WOM) in the form of product reviews has been shown in the literature as a means of mitigating the impact of produce uncertainty on product sales [47, 41, 43, 63]. For example, Hu et al. [35] test the efect of online reviews on sales and demonstrate that reviews written by reviewers with better reputation and higher exposure have a more favorable impact on the sales. Chevalier and Mayzlin [14] collect public data on book characteristics and user review from Amazon.com and barnesandnoble.com and show that reviews are overwhelmingly positive at both sites. However, an improvement in a book’s reviews leads to an increase in relative sales at that site. Clemons et al. [15] demonstrate that which new products grow the fastest in the online marketplace is significantly influenced by the variance of ratings and the strength of the most positive quartile of reviews. Using a panel of sales and WOM data for 148 digital cameras from Amazon.com and three external WOM websites (Cnet, DpReview, and Epinions), Gu et al. [30] suggest that a retailer’s external WOM sources, rather than the internal WOM, have a significant impact on the retailer’s sales of high-involvement products. Recently, social media is playing an increasingly important role in WOM and social learning [34, 45, 58, 59, 68].

## Seller Uncertainty

Seller uncertainty is defined as “the buyer’s perceived estimate of the variance in seller quality based on subjective probabilities about the seller’s characteristics and whether the seller will act opportunistically” [21]. Seller uncertainty can arise from risks involved in the transaction, such as intentionally misrepresenting the product, an error in shipping the right product, or failure to deliver on time [26, 56]. Since seller uncertainty prevents buyers from fully evaluating seller quality and has been identified as a major impediment of eficiency in online markets [56], a large body of literature aims at understanding various mechanisms implemented to reduce seller uncertainty, including third-party institutional structures [55, 57], buyer protection [23], trust-assuring arguments [7, 39], warranties [50, 62], feedback text comments [56].

Among the many mechanisms to reduce seller uncertainty, reputation system is the oldest and most prevalent one used by major online markets (e.g. Amazon, eBay, and Taobao.com,). Reputation system is thus one of the most active research areas the literature on seller uncertainty focuses on. For example, Melnik and Alm [51]’s empirical results indicate that a seller’s overall reputation has a positive impact on a buyer’s willingness to pay. Similarly, Lucking-Reiley et al. [49] find that bidders give reward to sellers who have better reputations as a seller’s feedback ratings reported by other eBay users have a measurable efect on the auction prices. Zhang [69] separates the reputation into selling reputation and buying reputation, and indicates that selling reputation significantly afects the closing prices but buying reputation does not. Houser and Wooders [33] also illustrate that seller’s, but not bidder’s, reputation has an economically and statistically significant efect on the auction price. Fan et al. [23] find a substantial return to reputation, but only for established sellers.

Prior literature examining seller reputation is mostly based on sellers’ long-term accumulative reputation, with only a few analytical studies looking at simple short-term reputation [17, 18, 48]. For example, Dellarocas [17] propose three immunization mechanisms (controlled anonymity, median filtering, and frequency filtering) for a robust reputation system in the presence of unfair and deceitful raters. He shows that when sellers’ service quality varies over time, it is most economically eficient to estimate sellers’ reputation by giving a higher weight on the most recent ratings with older ratings discounted heavily. In online markets with limited records (e.g., the online labor market Elance.com displays users feedback on contractors for only the past twelve months), Liu and Skrzypacz [48] find equilibria of “reputation bubbles” that do not happen in existing reputation literature where an increasing amount of trust is granted to the opportunistic long-run player even though his true type is perfectly observed. However, extant literature studying short-term reputation is mostly analytical in nature and the lack of empirical data on sellers’ short-term comprehensive reputation hampers the understanding of the efect of sellers’ short-term comprehensive reputation in online markets.

With abundant literature on reputation systems addressing product uncertainty and seller uncertainty, only a few studies [22, 36] investigate the efect of short-term reputation badge. Both [22] and [36] identify the positive signaling efect of eBay Top Rated Seller (eTRS) badges. Hui et al. [36] takes one step further by showing the impact of eBay Buyer Protection program, another asymmetric information mitigation mechanism, and its interaction with eTRS. Our study ofers new and deeper understanding on the reputation system mechanism design by examining the efect of earning/losing/keeping reputation badge on product sales and the moderating efect of earning reputation badges multiple times.

## Research Background

Taobao.com was founded by the Alibaba Group, Inc. in 2003, and has become China’s largest e-commerce platform. The general merchandise sales on the Taobao Marketplace from Aril 1, 2019 to March 31, 2020 is 3,387 billion Chinese yuan (479 billion U.S. dollars).<sup>1</sup> By March 2020, the Taobao marketplace had over 300 million daily active users, 846 million mobile monthly active users, and 726 million annual active users. To monitor seller quality and help buyers identify good sellers, Taobao.com maintains a reputation system almost identical to that adopted by eBay. Through this reputation system, a buyer can rate a seller by leaving a positive (+1), neutral (0), or negative (-1) score after each transaction. A seller’s reputation score is the cumulative sum of these feedback scores from the first day of presence in Taobao.com, which is the seller’s longterm accumulative reputation. Then Taobao.com categorizes the long-term accumulative reputation into grades, and the reputation grades are represented by heart, diamond, crown, or golden crown, which are displayed on a seller’s homepage and the product detail page to help buyers make purchase decisions.

As discussed in the Introduction section, this seller’s long-term reputation grade has several drawbacks that weaken the reputation system in helping buyers make purchase decisions. To improve the efectiveness of the reputation system, Taobao.com introduced the Gold Medal Seller (GMS) program that was announced in March 2014 and became efective in July 2014. The GMS badge is awarded on the 1<sup>st</sup> and the $1 6 ^ { \mathrm { t h } }$ of each month to sellers who have met the requirement. The GMS requirement has two parts. The first part applies to all product categories and establishes a minimum threshold for the sellers to be further considered for the GMS award. The common minimum threshold includes such criteria as

● The seller’s active time must be no less than 183 days,

● The seller’s cumulative feedback scores must be no less than 251,

● The seller must take part in Taobao.com’s “consumer protection program,”

● The “buyers’ like degree” (an aggregate score summarizing the return percentage of the buyers, repeat purchase ratio, recommendation percentage of the buyers, etc.) of the seller must be no less than 80 (out of 100).

The majority of the sellers can meet the common minimum threshold requirement. The second part requirement of GMS includes individual criteria that are diferent from product category to product category. The category-specific individual criteria are typically comprised of transaction volume, percentage of positive feedback, dispute rates, and Detailed Seller Ratings (DSR). The DSR ratings have three dimensions, including item description DSR, service DSR, and shipping DSR given by buyers using a 5-point Likert scale. The individual criteria in the second-part requirement of GMS are used to evaluate sellers’ performance every half month. Therefore, the gold medal program on Taobao is not a reputation badge only. The GMS badge is awarded a month later on the $1 ^ { \mathsf { s t } }$ or the $1 6 ^ { \mathrm { { ^ { - } } t h } }$ day of each month and is valid for only fifteen days. For example, if a seller meets both the minimum common threshold and the category-specific individual criteria for the period of March 1 to March 15, the seller is awarded the GMS whose efective period will be April 1 to April 15. For the digital product category, a seller awarded the GMS valid for April 1 to April 15 has to meet the following individual criteria:

● 98.742 percent or higher positive feedback from March 1 to March 15,

● 4.817 or higher item description DSR from March 1 to March 15,

● 4.884 or higher service DSR from March 1 to March 15,

● 4.817 or higher shipping DSR from March 1 to March 15,

● selling 17,000RMB (roughly US\$2,500) from March 1 to March 15,

● 0.003 percent or lower dispute rates from March 1 to March 15.

Once the sellers are awarded a GMS badge, they are entitled to show the GMS badge on the sellers’ home page and on each product detail page next to the product title, which helps GMS sellers signal their quality (see Figure 1). If a seller consecutively wins the badge, consumers know this information from the product page. In Figure 1, we can see that the seller has won a gold medal six times consecutively. Many consumers on Taobao are experienced customers. They tend to check Taobao product pages regularly (for example, multiple times during a month) to see whether there is a price promotion. If they see a seller had a gold medal in the previous period, but does not have it in the current period, then they know that this seller has lost the gold medal. When buyers view the product search results, the GMS badge is also displayed under or next to the seller information (see Figure 2), which allows the buyer to distinguish between listings sold by the GMS sellers and those by non-GMS sellers before deciding to view the product detail page and make purchase decisions.

There is no application fee for the gold medal program.<sup>2</sup> According to Taobao, the application process is straightforward. Once a seller applies, the systems automatically check the transaction history of the seller. If the conditions are satisfied, a gold medal is awarded (in the selection process, no human is involved).<sup>3</sup> Given the apparent benefit and no substantial additional cost, most of the high-quality sellers are willing to apply.

The GMS program implemented by Taobao.com afords us an opportunity to empirically examine several issues not addressed in the prior literature such as the impact of reputation badges on product sales. We thus formulate research hypotheses in the next section.

![](/api/attachments/ZVXN26GJ/fulltext/images/fc39f7153b41209a9d8d12070abf39958849dde157a884ad8ab4ac52b625c862.jpg)  
Figure 1. The GMS badge prominently displayed on seller’s home page and the product detail page.

## Hypotheses Development

There is a general lack of literature on the impact of sellers’ reputation badges on product sales with only a few analytical papers examining the efect of short-term reputation [17, 18, 48]. Dellarocas [18] explores the reputation mechanism design in a trading environment with moral hazard and shows that a simple binary feedback mechanism publishing the most recent rating is just as eficient as those that publish a seller’s detailed feedback history. The same findings can be extended from a simple binary feedback mechanism to multivalued reputation mechanisms. Liu and Skrzypacz [48] indicate that limited records generate a reputation efect that cannot be guaranteed with complete records. Theoretically, a gold medal is a short-term reputation badge, which summarizes the previous trustworthy behavior of a seller. For example, Hui et al. [36, p. 3604] call eBay Top Rated Seller program a reputation badge: “Reputation badges take the form of the eBay Top Rated Seller (eTRS) program.” eTRS program is similar to gold medal program on Taobao, which requires specific conditions: (i) 98 percent or higher positive feedback; (ii) 4.6/5.0 Detailed Seller Ratings (DSR); (iii) No more than 1 percent low DSR; (iv) Selling 100 items and \$3,000 in the past 12 months; (v) Selling 100 items or \$1,000 monthly for the past three consecutive months; and (vi) Low dispute rates. Actually, most if not all of the reputation badge programs require certain conditions. If a reputation badge cannot diferentiate high-quality sellers from low-quality sellers, then it loses the signaling value.

![](/api/attachments/ZVXN26GJ/fulltext/images/892e47f109e1583135853af76e71f30f340f429276a12ad9d7c91356a7583df3.jpg)  
Figure 2. Product search result with the GMS badges shown under those who earn the badge.

The key role of short-term reputation badges is to extend the trust between a seller and its existing customers to new customers. The trust between a seller and its existing customers can be established through repeated interaction. However, new customers do not have prior experience with the seller. A short-term reputation badge reflects the previous trustworthy behavior of the seller and is a way of building a reputation for being trustworthy. Our study highlights how sellers can build a reputation for being trustworthy through consecutively winning short-term reputation badges.

The relationship between a seller and its existing customers on the Taobao platform can be treated as a repeated game: Buyers and sellers interact on the marketplace repeatedly. According to the repeated game theory, people’s current actions largely depend on the economic and social value of future interactions [7]. The role of future interactions on current decisions has been widely discussed in the contexts of the folk theorem in economics (e.g., [12]). Axelrod [2] calls the prospect of future interaction the “shadow of the future” (p. 126): People tend to become more “cooperative” and benefit the other player in repeated interactions when the economic and social value of future interactions is larger. In our context, if buyers and sellers interact repeatedly, sellers tend to stay in the “cooperative” equilibrium and show trusting behavior.

However, for a new customer who has no prior transaction with a seller, she cannot identify a seller’s reputation through repeated interaction. A short-term reputation badge, such as a gold medal, contains the information about a seller’s trustworthy behavior in the past (to other buyers), and is a way of building a reputation for being trustworthy.

## Positive Signaling Value of Earning a Reputation Badge

We develop a unified theoretical framework of signaling and countersignaling [24, 64] to formulate our hypotheses. The main feature of consumer-to-consumer online markets (e.g., Taobao.com) is the existence of a large number of small sellers. A consumer-toconsumer online market is inherently flawed because of asymmetric information [36]. For a small seller, earning a reputation badge is a signal for the seller quality. This strategy is consistent with the signaling literature in game theory [64]: One party can credibly convey some information about itself to another party by sending signals. In our context, a good seller can credibly convey the seller quality information by earning a reputation badge. The signaling framework has been widely applied in business contexts. For example, a stream of literature [3, 29, 52] develops game-theoretic models in which high-quality sellers are incentivized to spend more on advertising to signal, but low-quality sellers do not find it profitable to imitate.

There are two preconditions for the application of signaling theory. (i) Information asymmetry between a signaler and receiver. In our context, sellers know more than consumers. (ii) The potential for divergence or conflict of interest between the signaler and receiver. In our context, sellers may not serve the best interest of consumers and benefit from information asymmetry. Without either of these two conditions, there is no need for signals as the problem is merely one of communication. When these two conditions are satisfied simultaneously, signals have to be used by signalers to prove to receivers their underlying hidden types where the hidden type in our context is the quality of sellers. We expect that the GMS badge signals sellers’ quality and efectively reduces seller uncertainty. We thus hypothesize a positive efect of GMS on product sales as follows:

Hypothesis 1 (H1): Earning a reputation badge has a positive impact on product sales.

## Negative Signaling Value of Losing a Reputation Badge

In the signaling framework, if earning a badge is a positive signal, then losing a badge should be a negative signal. However, is losing a badge worse than not earning a badge at all? In the classical signaling model, high-quality sellers typically send signals that can separate them from lower-quality senders. However, based on the signaling framework, Feltovich et al. [24] develop a theory of countersignaling: They show that sellers of the best quality may use nondisclosure as a countersignal to distinguish themselves from eager-todisclose medium-quality sellers. High-quality sellers not only save costs by relying on the additional information to separate them from low-quality sellers, countersignaling itself is a signal of confidence that separates high-quality sellers from medium-quality sellers. Recent studies provide empirical evidence for the countersignaling theory (e.g., [9]).

According to the countersignaling theory, some best-quality sellers may choose not to earn a reputation badge (countersignaling) to distinguish themselves from mediumquality sellers. Earning a badge and then losing it immediately reveals that these sellers are not countersignaling sellers (best-quality sellers), and consumers make downward adjustments on the quality of these sellers. In contrast, if some sellers have not earned reputation badges at all, they still might be countersignaling sellers (best-quality sellers).

Therefore, we expect that the signaling value of obtaining/losing a reputation badge is asymmetric: The magnitude of the efect of losing a reputation badge is larger than that of earning a badge. In other words, if a seller earns a badge and then loses it immediately in the next time period, consumers interpret it as a more negative signal than not earning a badge at all.

Moreover, the literature on behavioral economics (the theory of reference-dependent preference) demonstrates that humans rarely look at things in absolute terms: They focus on the changes relative to contextual reference points and judge things in a relative way [66]. Moreover, the theory of reference-dependent preference postulates a kink about a contextual reference point, where losses relative to this point are weighted more heavily than gains [66]. In our context, losing a badge is interpreted as losses in consumers perceived seller quality, and earning a badge is interpreted as gains in consumers perceived seller quality. Since losses are weighted more heavily than gains, the magnitude of the efect of losing a reputation badge is larger than that of earning a badge. Hence, we hypothesize:

Hypothesis 2 (H2): Losing a reputation badge has a negative impact on product sales. The magnitude of the efect of losing a reputation badge is larger than that of earning a badge.

## Positive Signaling Value of Keeping a Reputation Badge

In the signaling theory [64], the informational value of a signal comes from the fact that the receiver believes that the signal is positively correlated with having greater ability or quality and is dificult for low-ability signalers to obtain. Therefore, the signal enables the receiver to reliably distinguish high-ability signalers from low-ability ones. In our context, earning a badge is dificult for low-quality sellers.

There are two key equilibrium concepts in signaling games: A separating equilibrium vs. a pooling equilibrium [64]. In a separating equilibrium, high and low-ability signalers choose diferent signals. In a pooling equilibrium, low-ability signalers try to mimic highability ones and send the same signals. A stronger signal means that it is more dificult for low-ability signaler to imitate, and hence is more likely to lead to a separating equilibrium. In our context, keeping a reputation badge is a stronger signal for quality because it may be not that dificult for a low-quality seller to earn one badge, but it is very dificult for him/her to earn badges consecutively. Therefore, keeping a reputation badge has a larger signaling (informational) value than earning one badge.

In practice, the GMS program records and displays the number of consecutive attainments of earning the badge. For instance, if the seller gains the GMS badge in two consecutive periods, then “two consecutive periods” will be displayed on the GMS badge. However, once the seller loses the GMS badge, the number of consecutive period will be reset to zero and starts from one when the seller gains the GMS badge again. The display of consecutive attainments of the GMS badge informs buyers of the consistency of the seller’s achieving high quality. As the higher the number of consecutive periods of earning the GMS badge, the more consistent the seller’s performance is. Therefore, we hypothesize:

Hypothesis 3 (H3): Keeping a reputation badge has a larger positive impact on product sales than earning a reputation badge.

## Moderating Role of Earning Reputation Badges Multiple Times

In line with our explanations for larger signaling value of keeping a reputation badge, if a seller earns reputation badges multiple times, we are more likely to observe a separating equilibrium in which low-quality sellers are dificult to imitate high-quality sellers. The reason is that a stronger signal is more likely to lead to a separating equilibrium [64]. In contrast, if a signal is noisier, we are less likely to observe a separating equilibrium [16]. In other words, if lower-quality sellers pay higher cost for signaling, high-quality sellers are easier to separate themselves from lower-quality sellers. In our context, earning reputation badges multiple times increases the cost for signaling.

On the one hand, if a seller has previously earned a reputation badge multiple times, we expect that the signaling value of earning or keeping a badge in the current period is larger. On the other hand, if a seller has previously earned a badge multiple times, then losing a badge in the current time period is a less negative signal. Thus, we hypothesize a positive moderating role of earning the reputation badge multiple times:

Hypothesis 4 (H4): As a seller earns more reputation badges, earning or keeping a reputation badge has a larger positive impact on product sales, and losing a badge has a smaller negative impact on product sales.

## Data Description

We collected a six-month panel data set that contains a wide variety of new search products sold through posted prices on Taobao.com from July 1, 2015 to December 31, 2015. Since the GMS badge is evaluated every half-month, the sales variable aggregates the total sales in each half-month period. Our time period (halfmonth) matches the period of the GMS program, which enables us to better capture whether a seller obtains or loses a gold medal. Our data period is comparable with prior empirical research on Taobao and eBay. For example, Fan et al. [23] examine the online feedback systems on Taobao and use a month as a time period. Cabral and Hortacsu [13] investigate the importance of eBay’s reputation mechanism, and their time period is at a monthly level.

A snapshot of the information about the products and sellers at the midpoint of each period is reported in our data as customary in the literature [23]. Since the focus of our research is the impact of sellers’ short-term reputation on product sales, we chose those product categories (router, monitor, and refrigerator) commonly carried by many diferent sellers on Taobao.com that are new search products with little product uncertainty. The sample set within each product category consists of homogenous goods.

We selected the top ten routers, the top ten monitors, and the top ten refrigerators in terms of monthly sales from Taobao.com, and collected the information of all the sellers who sell these products and whose monthly sales of this product was not zero. The collected information includes seller information and product information displayed on the product detail page on Taobao.com, where buyers will browse before they make their purchase decisions. As for the seller information, it contains long-term accumulative reputation, whether the seller has attained GMS, and seller’s first date of operations on Taobao.com. The product information is comprised of sales, price, product WOM (including review volume and negative review percentage), product description information, the number of product page reviews, whether the product participates in the “charity plan,” and so on.

Excluding the products that were taken of the shelves during the sample period and the products whose information was incomplete, our final data set has 944 seller-product pairs in total, including 468 seller-router pairs, 258 seller-monitor pairs, and 218 seller-refrigerator pairs in twelve half-month periods. The average number of product sales in each period is 31.63. Throughout the sample period, 30.9 percent of sellers gained GMS. The average number of continuous periods of earning the GMS badge is 0.95, and the max number of continuous periods is 32. Note that at the beginning of our sample period, some sellers have already been gold medal sellers for a long time. This explains why the maximum number of continuous periods is longer than six-month. The average reputation grade is 9.69 out of 20 possible levels. The average volume of product reviews is 44.75, with an average of 1.1 percent of negative reviews. With regard to the product description, 36.2 percent of the products had a customized description. A total of 46.2 percent of the sellers’ age of operations was more than four years. The average product price is 606.70 RMB (roughly 93.92 USD at the time of research sample), with the minimum of 30RMB (roughly 4.64USD) and the maximum of 3,588RMB (roughly 555.42 USD). The average number of product page views is 7,107.08, 11.4 percent of products participated in the charity plan, and 54.8 percent of the products can be paid by credit card. Table 1 presents the descriptive statistics of our research sample.

## Empirical Model and Results

## Impact of Reputation Badges on Product Sales

In this section, we examine the impact of reputation badges on product sales. In particular, we estimate the following two fixed efects models:

$$
\log (S a l e s) _ {i j t} = a _ {i} + c _ {j} + \nu_ {t} + \beta_ {0} + \beta_ {1} G M _ {i t} + c o n t r o l s + \varepsilon_ {i j t}\tag{1a}
$$

$$
\log \left(S a l e s\right) _ {i j t} = a _ {i} + c _ {j} + v _ {t} + \beta_ {0} + \beta_ {1} W i n G M _ {i t} + \beta_ {2} K e e p G M _ {i t} + \beta_ {3} L o s e G M _ {i t} g _ {i} t\tag{1b}
$$

Table 1. Descriptive statistics.

<table><tr><td>Variables</td><td>Mean</td><td>Min</td><td>Max</td><td>Std.</td></tr><tr><td>Product sales transactions</td><td>31.630</td><td>0</td><td>11,251.00</td><td>213.770</td></tr><tr><td>GMS</td><td>0.309</td><td>0</td><td>1.00</td><td>0.462</td></tr><tr><td>The continuous periods of GMS</td><td>0.950</td><td>0</td><td>32.00</td><td>2.080</td></tr><tr><td>Log(SellerReputation)</td><td>3.740</td><td>0.60</td><td>5.83</td><td>0.800</td></tr><tr><td>Customized description percentage</td><td>36.200</td><td>0</td><td>100.00</td><td>48.100</td></tr><tr><td>Price (in RMB)</td><td>606.700</td><td>30.00</td><td>3,588.00</td><td>634.270</td></tr><tr><td>Age of operations (≥4)</td><td>0.460</td><td>0</td><td>1.00</td><td>0.500</td></tr><tr><td>Number of page views</td><td>7,107.080</td><td>12.00</td><td>283,403.00</td><td>20377.990</td></tr></table>

Note: N = 11,328.

where the dependent variable is the log sales of product j of seller i in time period t (half month is a time period), $a _ { i }$ is the seller fixed efect, $c _ { j }$ is the product fixed efect, $\nu _ { t }$ represents time dummies, $G M _ { i t }$ is a dummy variable indicating whether seller i earns a reputation badge in time period t (Yes: 1; No: 0), $W i n G M _ { i t }$ is a dummy variable indicating that seller i does not have a reputation badge in time period $t \mathrm { ~ - ~ } 1$ , but earns one in time period t (Yes: 1; No: 0), $K e e p G M _ { i t }$ is a dummy variable indicating that seller i has a reputation badge in time period $t \textrm { - } 1$ , and keeps it in time period $t \left( \mathrm { Y e s } ; 1 ; \mathrm { N o } ; 0 \right)$ and $L o s e G M _ { i t }$ is a dummy variable indicating that seller i has a reputation badge in time period $t \textrm { - } 1$ , but loses it in time period t (Yes: 1; No: 0). Our control variables include the log number of seller reputation scores (log $( S e l l e r s R e p u t a t i o n ) _ { i t } )$ , the number of ratings by consumers $( T o t a l R a t i n g N u m b e r _ { i t } )$ , the number of times a seller is favorited by consumers $( S e l l e r F a \nu o r i a t e _ { i t } )$ , the rating of shipping by consumers $( S h i p p i n g R a t i n g _ { i t } )$ , the price of the product, the number of years a seller have been selling products on the platform $( A g e _ { i t } )$ the number of product page views $( P a g e V i e w _ { i t } )$ , whether the product is participating in the “charity plan,” and whether buyers can use a credit card to pay the product. A plausible confounding factor is that GMS sellers have the privilege to appear in the recommended positions on the search page, which may increase sales through increased product page views. In other words, the underlying mechanism is that gold medal sellers prominent position on the search page leads more consumers to visit the product pages. Then, an increased number of product page views can increase sales. This mechanism is blocked if we control for the number of product page views. Therefore, we can alleviate the concern of this confounding factor by controlling for the number of product page views.

The fixed efects model allows us to control for product level and seller level fixed efects, which address the endogeneity concern from the unobserved time-invariant product and seller quality. If we use a random efect model, the unobserved product level and seller level fixed efects will not be canceled out in the estimation (they are still left in the error term), and our main efects can be confounded by these time-invariant product and seller factors.

The estimation results of regression equation (1a) are shown in columns 1 and 2 of Table 2. In column 1, we find that the coeficient on $G M _ { i t }$ is positive and statistically significant. In general, a reputation badge leads to a 6.75 percent increase in sales, supporting hypothesis H1. To alleviate concerns about the failure to meet standard regression assumptions (such as clustering and heteroscedasticity), we compute the robust statistics in column 2 and the results are similar.

We present the estimation results of regression Equation (1b) in columns 3 and 4 of Table 2. The coeficients on $W i n G M _ { i t }$ and $K e e p G M _ { i t }$ are significantly positive, and the coeficient on $L o s e G M _ { i t }$ is significantly negative. These results suggest that earning a reputation badge leads to a 4.43 percent increase in sales; keeping a badge leads to a 9.28 percent increase in sales; and losing a reputation badge leads to a 7.97 percent decrease in sales. In other words, our empirical results support H2 and H3: (i) losing a reputation badge has a negative impact on product sales, (ii) the magnitude of the efect of losing a reputation badge is larger than that of earning a badge, and (iii) keeping a reputation badge has a larger positive impact on product sales than earning a reputation badge.

Table 2. The impact of GMS badge on sales.

<table><tr><td rowspan="2">VARIABLES</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>t-statistics</td><td>Robust t-statistics</td><td>t-statistics</td><td>Robust t-statistics</td><td>HLM</td></tr><tr><td>GM</td><td>0.0675***[5.325]</td><td>0.0675***[4.628]</td><td></td><td></td><td></td></tr><tr><td>WinGM</td><td></td><td></td><td>0.0443***[3.075]</td><td>0.0443***[3.146]</td><td>0.0287***[2.943]</td></tr><tr><td>KeepGM</td><td></td><td></td><td>0.0928***[4.126]</td><td>0.0928***[4.484]</td><td>0.0731***[2.831]</td></tr><tr><td>LoseGM</td><td></td><td></td><td>-0.0797***[-3.819]</td><td>-0.0797***[-3.813]</td><td>-0.0554***[-3.204]</td></tr><tr><td>Log(SellerReputation)</td><td>0.0112**[2.195]</td><td>0.0112**[2.243]</td><td>0.0287**[2.282]</td><td>0.0287**[2.092]</td><td>0.0184**[2.113]</td></tr><tr><td>TotalRatingNumber</td><td>2.94e-05***[7.105]</td><td>2.94e-05***[4.063]</td><td>3.23e-05***[4.865]</td><td>3.23e-05***[8.243]</td><td>2.04e-05***[6.332]</td></tr><tr><td>SellerFavorite</td><td>-2.28e-06[-1.448]</td><td>-2.28e-06[-1.280]</td><td>-1.35e-06[-1.283]</td><td>-1.35e-06[-1.513]</td><td>-1.04e-06[-1.231]</td></tr><tr><td>ShippingRating</td><td>0.0886*[1.680]</td><td>0.0886[1.199]</td><td>0.104[1.406]</td><td>0.104[1.523]</td><td>0.156[1.774]</td></tr><tr><td>Price</td><td>-0.000430***[-16.49]</td><td>-0.000430***[-14.73]</td><td>-0.000208*[-1.788]</td><td>-0.000208*[-1.898]</td><td>-0.000128[-1.251]</td></tr><tr><td>Age</td><td>-0.0337***[-5.354]</td><td>-0.0337***[-4.165]</td><td>-0.0278***[-3.672]</td><td>-0.0278***[-4.734]</td><td>-0.0172***[-3.218]</td></tr><tr><td>PageView</td><td>5.76e-06***[7.173]</td><td>5.76e-06***[5.395]</td><td>4.47e-06***[4.487]</td><td>4.47e-06***[6.011]</td><td>2.35e-06***[4.221]</td></tr><tr><td>CharitableGoods</td><td>-0.0308[-1.039]</td><td>-0.0308[-0.954]</td><td>-0.0133[-0.414]</td><td>-0.0133[-0.461]</td><td>-0.0104[-0.226]</td></tr><tr><td>Creditcard</td><td>-0.0379[-1.253]</td><td>-0.0379[-1.297]</td><td>-0.0320[-1.124]</td><td>-0.0320*[-1.932]</td><td>-0.0165[-1.032]</td></tr><tr><td>Product Dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time Dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>11,328</td><td>11,328</td><td>11,328</td><td>11,328</td><td>11,328</td></tr></table>

Notes: t-statistics or robust t-statistics in brackets. $\star ^  \star \star \} \mathsf { p } < 0 . 0 1 . \ ^ { \star \star } \mathsf { p } < 0 . 0 5 . \ ^ { \star } \mathsf { p } < 0 . 1 .$

Because of the multi-level structure (seller-product pairs) of our data sets, we also estimate a hierarchical linear model (HLM):

$$
\begin{array}{c} \log (S a l e s) _ {i j t} = u _ {i} + u _ {i j} + v _ {t} + \beta_ {0} + \beta_ {1} W i n G M _ {i t} + \beta_ {2} K e e p G M _ {i t} + \beta_ {3} L o s e G M _ {i t} \\ + c o n t r o l s + \varepsilon_ {i j t} \end{array}\tag{2}
$$

where $u _ { i } { \sim } N ( 0 , \gamma ^ { 2 } ) , u _ { i j } { \sim } N ( 0 , \tau ^ { 2 } )$ , and $\scriptstyle \varepsilon _ { i j t } \sim N ( 0 , \sigma ^ { 2 } )$ . The estimation results are robust and are presented in Column 5 of Table 2. We use an HLM mainly because of multiple products within each seller. In this setting, we want to adjust for the variations at both the seller-level and at the product-level. A hierarchical linear model is used to handle this hierarchical data structure [65].

## Moderating Efect of Earning Reputation Badges Multiple Times

In the analysis of the moderating efect, we focus on how the main efect is moderated by the number of times winning the badge previously. In particular, we estimate the following model:

$$
\begin{array}{l} \log (S a l e s) _ {i j t} = a _ {i} + c _ {j} + v _ {t} + \beta_ {0} + \beta_ {1} W i n G M _ {i t} + \beta_ {2} K e e p G M _ {i t} + \beta_ {3} L o s e G M _ {i t} \\ \qquad + \beta_ {4} N u m G M _ {i t} + \beta_ {5} (W i n G M _ {i t} * N u m G M _ {i t}) \\ \qquad + \beta_ {6} (K e e p G M _ {i t} * N u m G M _ {i t}) + \beta_ {7} (L o s e G M _ {i t} * N u m G M _ {i t}) \\ \qquad + c o n t r o l s + \varepsilon_ {i j t} \end{array}\tag{3}
$$

where $N u m G M _ { i t }$ is the number of times seller i has earned the reputation badge up until time period t - 1. We are interested in the coeficients on the interaction terms.

The estimation results are shown in Table 3. We find that the coeficients on the interaction terms are significantly positive, which suggests that the moderating role of $N u m G M _ { i t }$ is positive. This empirical finding supports H4. On the one hand, if a seller has previously earned the badge multiple times, then the signaling value of winning or keeping the badge in the current period is larger (the coeficients on $W i n G M _ { i t } * N u m G M _ { i t }$ and $K e e p G M _ { i t } * N u m G M _ { i t }$ are positive). On the other hand, if a seller has previously earned the badge multiple times, then losing a badge in the current time period is a less negative signal. Our results on H3 and H4 indicate that the marginal value of earning reputation badges increases, which is consistent with the signaling theory: If a seller earns reputation badges multiple times, we are more likely to observe a separating equilibrium in which low-quality sellers are dificult to imitate high-quality sellers.

Table 3. The impact of GMS badge on sales: Moderating efects.

<table><tr><td rowspan="2">VARIABLES</td><td>(1)</td><td>(2)</td></tr><tr><td>t-statistics</td><td>Robust t-statistics</td></tr><tr><td>WinGM</td><td>0.0202**[2.231]</td><td>0.0202**[2.144]</td></tr><tr><td>KeepGM</td><td>0.0513***[3.324]</td><td>0.0513***[3.571]</td></tr><tr><td>LoseGM</td><td>-0.0914***[-4.336]</td><td>-0.0914***[-4.257]</td></tr><tr><td>NumGM</td><td>0.00942**[2.246]</td><td>0.00942**[2.317]</td></tr><tr><td>WinGM*NumGM</td><td>0.0113***[2.942]</td><td>0.0113***[2.885]</td></tr><tr><td>KeepGM*NumGM</td><td>0.0141***[3.146]</td><td>0.0141***[3.023]</td></tr><tr><td>LoseGM*NumGM</td><td>0.0106***[4.237]</td><td>0.0106***[4.152]</td></tr><tr><td>Log(SellerReputation)</td><td>0.0297**[2.135]</td><td>0.0297**[2.043]</td></tr><tr><td>TotalRatingNumber</td><td>3.28e-05***[4.912]</td><td>3.28e-05***[3.325]</td></tr><tr><td>SellerFavorite</td><td>-1.36e-06[-1.293]</td><td>-1.36e-06[-1.104]</td></tr><tr><td>ShippingRating</td><td>0.105[1.419]</td><td>0.105[1.213]</td></tr><tr><td>Price</td><td>-0.000212*[-1.814]</td><td>-0.000212*[-1.883]</td></tr><tr><td>Age</td><td>-0.0281***[-3.717]</td><td>-0.0281***[-3.214]</td></tr><tr><td>PageView</td><td>4.46e-06***[4.472]</td><td>4.46e-06***[4.546]</td></tr><tr><td>CharitableGoods</td><td>-0.0128[-0.398]</td><td>-0.0128[-0.216]</td></tr><tr><td>Creditcard</td><td>-0.0323[-1.137]</td><td>-0.0323[-1.327]</td></tr><tr><td>Product Dummies</td><td>Yes</td><td>Yes</td></tr><tr><td>Time Dummies</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>11,328</td><td>11,328</td></tr></table>

Notes: t-statistics or robust t-statistics in brackets. $\texttt { * * } \texttt { p < 0 . 0 1 . } ^ { \star \star } \texttt { p < 0 . 0 5 . } ^ { \star } \texttt { p < 0 . 1 }$

## Endogeneity Concerns and Robustness Checks

To address diferent endogeneity mechanisms, we use various causal identification strategies and robustness checks. If the underlying selection process is known, we adopt the Heckman-type model to explicitly account for the selection process. If the selection process is unknown and the selection process is driven by observable characteristics (observable to researchers), we use a fixed efects model combined with propensity score matching (PSM) to address the endogeneity issue. If the selection process is unknown and the selection process is driven by unobserved time-variant factors, PSM could not fully address this endogeneity concern. In this case, we use three strategies to further confirm our causal identifications. First, we use Rosenbaum bounds [60] to examine if PSM is sensitive to hidden bias. Second, we control for seller-specific time trends in a correlated random trend model. Third, we conduct a placebo test to examine if our results could be driven entirely by some unobserved time-varying factors. All of these additional causal identification strategies and robustness checks suggest that the positive efect of reputation badge is unlikely driven by confounding factors.

## Heckman-Type Model

We consider a Heckman-type model [11] to directly specify the selection process. Our main model is regression Equation (1a). We directly model whether a seller is more likely to earn a reputation badge by looking at a Probit model. A possible selection bias is that if some types of sellers are less likely to apply for the program, they will be less likely to earn a reputation badge. The selection equation is given as follows:

$$
\begin{array}{r l} w _ {i t} ^ {*} = & \gamma_ {0} + \gamma_ {1} \text {BrandExclusive} _ {i} + \gamma_ {2} \text {PhysicalStore} _ {i} + \gamma_ {3} \log (\text {SellersReputation}) _ {i t} \\ & + \gamma_ {4} \text {TotalRatingNumber} _ {i t} + \gamma_ {5} \text {SellerFavoriate} _ {i t} + \gamma_ {6} \text {ShippingRating} _ {i t} \\ & + \gamma_ {7} A g e _ {i t} + \gamma_ {8} P a g e V i e w _ {i t} + e _ {i t} \end{array}\tag{4}
$$

where $w _ { i t } ^ { * }$ is a latent variable, BrandExclusive<sub>i</sub> is a binary variable indicating whether the seller is a brand exclusive store, and PhysicalStore<sub>i</sub> is a binary variable indicating whether the seller has a physical store. Assume that the errors $\varepsilon _ { i j t }$ and $e _ { i t }$ follow a bivariate

normal with mean zero and covariance matrix $\left[ \begin{array} { l l } { \sigma _ { \varepsilon } ^ { 2 } } & { \rho } \\ { \rho } & { 1 } \end{array} \right]$

In the selection equation, we consider the following covariates. (i) Seller reputation covariates: the log number of seller reputation scores, the number of times a seller is favorited by consumers, and the rating of shipping by consumers. We expect that sellers with a high level of reputation are more likely to apply for the program because they are more likely to earn a gold medal. (ii) Seller experience covariate: the number of years a seller has been selling products on the platform. We expect more experienced sellers have a better understanding of the benefit of GMS, and hence they are more motivated to apply for the program and earn the badges. (iii) Seller popularity: the number of ratings by consumers and the number of product page views. More popular sellers are more likely to apply for the program because they are more likely to earn a gold medal. (iv) Other seller characteristics: whether the seller is a brand exclusive store and whether the seller has a physical store. Sellers that are brand exclusive stores or have physical stores are more likely to be large sellers, and obtaining reputation badges brings more benefits for these large sellers. Therefore, these larger sellers are more motivated to apply for the program and earn the badges.

The indicator $G M _ { i t } = 1$ if $w _ { i t } ^ { * } \geq 0 ; G M _ { i t } = 0$ otherwise. Taking this selection process into account, we estimate Equations (1a) and (4) jointly, and the selection issue in our fixed efects model is less of a concern. The estimation results of the Heckman-type model are consistent with our main results, and are presented in column 1 of Table 4.

## Fixed Efects Model Combined with PSM

Following [8, 28, 38, 42, 46], we first create a “proper” control group for treated sellers by using PSM. We ensure that the control and treated groups are comparable in terms of observable characteristics. Then, we run the fixed efects model in Equation (1a) based on the new matched sample.

In the matching process, the treated sellers are the ones that earn reputation badges. Using PSM, we match each treated seller to the most “similar” control seller (closest propensity score) in terms of the following observable characteristics at the beginning of the sample period: the log number of seller reputation scores, the number of ratings by consumers, the number of times a seller is favorited by consumers, the rating of shipping by consumers, the price of the product, the number of years a seller have been selling products on the platform, the number of product page views, whether the seller is a brand exclusive store, and whether the seller has a physical store.

Table 4. The impact of GMS badge on sales: Robustness checks.

<table><tr><td rowspan="2">VARIABLES</td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>Heckman Model</td><td>Fixed Effects + PSM</td><td>Correlated Random Trend</td></tr><tr><td>GM</td><td>0.0642***[5.173]</td><td>0.0663***[5.842]</td><td>0.0587***[4.854]</td></tr><tr><td>Log(SellerReputation)</td><td>0.0148**[2.221]</td><td>0.0132**[2.034]</td><td>0.0126**[2.132]</td></tr><tr><td>TotalRatingNumber</td><td>2.12e-05***[4.632]</td><td>1.43e-05***[3.527]</td><td>2.35e-05***[4.724]</td></tr><tr><td>SellerFavorite</td><td>-2.03e-06[-1.542]</td><td>-2.68e-06[-1.321]</td><td>-2.26e-06[-1.652]</td></tr><tr><td>ShippingRating</td><td>0.0632*[1.723]</td><td>0.0554[1.531]</td><td>0.0716*[1.784]</td></tr><tr><td>Price</td><td>-0.000254***[-4.222]</td><td>-0.000213***[-4.254]</td><td>-0.000232***[-4.021]</td></tr><tr><td>Age</td><td>-0.0126***[-4.183]</td><td>-0.0132***[-4.358]</td><td>-0.0119***[-4.026]</td></tr><tr><td>PageView</td><td>3.21e-06***[4.532]</td><td>2.16e-06***[3.336]</td><td>3.47e-06***[4.632]</td></tr><tr><td>CharitableGoods</td><td>-0.0128[-1.225]</td><td>-0.0153[-1.436]</td><td>-0.0114[-1.107]</td></tr><tr><td>Creditcard</td><td>-0.0211[-1.214]</td><td>-0.0187[-1.154]</td><td>-0.0194[-1.203]</td></tr><tr><td>Product Dummies</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time Dummies</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>11,328</td><td>11,328</td><td>11,328</td></tr></table>

Notes: t-statistics or robust t-statistics in brackets. \*\*\*p < 0.01. \*\*p < 0.05. \*p < 0.1.

Note that we conduct PSM based on several categories of matching attributes: (i) seller reputation: the log number of seller reputation scores, the number of times a seller is favorited by consumers, and the rating of shipping by consumers; (ii) seller experience: the number of years a seller have been selling products on the platform; (iii) seller popularity: the number of ratings by consumers and the number of product page views; (iv) other seller characteristics: whether the seller is a brand exclusive store and whether the seller has a physical store; (v) product characteristics: the price of the product. The purpose of matching on these attributes is to construct a more balanced control sample. More specifically, categories (i) through (iv) are seller characteristics, and (v) is a product characteristic. In our context, gold medal (treated) sellers could be systematically diferent from sellers without a gold medal (control) in terms of these seller and product characteristics, which are potential confounding factors. To obtain a more balanced sample, we choose these matching attributes.

It is worth noting that the traditional PSM takes care of only observable characteristics and may be biased in the case of selection-on-unobservables. However, in the implementation of the fixed efects approach combined with PSM, our specification can eliminate the bias resulting from the unobserved time-invariant factors.

We first sort all sellers in a random order to make sure that the ordering does not afect the subsequent matching. Then, we run a logit regression based on the variables mentioned earlier and obtain the predicted propensity scores. We use the nearest neighbor matching algorithm in which each treated seller is matched with the control seller with the closest propensity score. In order to assess the quality of matching, we perform t-tests of equality of means before and after the matching to check whether our PSM adequately balances characteristics between the treatment and the control group units. The results are presented in Table 5. In this table, there is a clear evidence of covariate imbalance between groups. After matching, the diferences of mean are significantly reduced, suggesting that matching helps reduce the bias associated with the observable characteristics. From Table 5, we can see that among the nine matching attributes, diferences in mean between control and treatment groups after matching become insignificant (p-value > 0.05) for five matching attributes. For the rest four matching attributes, although the diferences in mean are still significant, the percentage bias between control and treatment groups reduces substantially after matching. In addition, we alleviate the concern of significant diferences in mean for some matching attributes by running a fixed efects regression based on the matched sample because we control for these matching attributes in the regression.

Table 5. Diferences in Mean Before and After Matching.

<table><tr><td rowspan="2">Variables</td><td colspan="5">Before Matching</td><td colspan="5">After Matching</td></tr><tr><td>Mean Treated</td><td>Mean Control</td><td>% bias</td><td>t-statistics</td><td>p-value</td><td>Mean Treated</td><td>Mean Control</td><td>% bias</td><td>t-statistics</td><td>p-value</td></tr><tr><td>log_sellers_reputation</td><td>4.01</td><td>3.61</td><td>52.1</td><td>25.06***</td><td>0.00</td><td>4.01</td><td>4.01</td><td>0.4</td><td>0.18</td><td>0.86</td></tr><tr><td>total_rating_number</td><td>2,770.50</td><td>1,161.30</td><td>37.9</td><td>20.99***</td><td>0.00</td><td>2752.3</td><td>1863.3</td><td>20.9</td><td>8.01***</td><td>0.00</td></tr><tr><td>seller_favorite</td><td>9,563.00</td><td>4,619.40</td><td>26.6</td><td>13.87***</td><td>0.00</td><td>9517.7</td><td>7663.3</td><td>10.0</td><td>3.81***</td><td>0.00</td></tr><tr><td>shipping_rating</td><td>4.88</td><td>4.86</td><td>26.4</td><td>12.19***</td><td>0.00</td><td>4.88</td><td>4.88</td><td>-2.2</td><td>-1.15</td><td>0.25</td></tr><tr><td>price</td><td>752.86</td><td>541.18</td><td>32.6</td><td>16.62***</td><td>0.00</td><td>751.88</td><td>722.03</td><td>4.6</td><td>1.79*</td><td>0.07</td></tr><tr><td>age</td><td>4.48</td><td>4.20</td><td>11.9</td><td>5.72***</td><td>0.00</td><td>4.48</td><td>4.53</td><td>-2.7</td><td>-1.16</td><td>0.24</td></tr><tr><td>page_view</td><td>10,843.00</td><td>5,432.70</td><td>23.7</td><td>13.16***</td><td>0.00</td><td>10,793.00</td><td>7612.3</td><td>13.9</td><td>5.39***</td><td>0.962</td></tr><tr><td>physical_store</td><td>0.70</td><td>0.67</td><td>1.2</td><td>0.59</td><td>0.56</td><td>0.70</td><td>0.72</td><td>-1.1</td><td>-0.46</td><td>0.64</td></tr><tr><td>brand_exclusive_stores</td><td>0.80</td><td>0.38</td><td>17.8</td><td>9.35***</td><td>0.00</td><td>0.80</td><td>0.65</td><td>6.1</td><td>2.30**</td><td>0.02</td></tr></table>

Note: \*\*\*p < 0.01. \*\*p < 0.05. \*p < 0.1.

![](/api/attachments/ZVXN26GJ/fulltext/images/c2d7df539e826f358cb769d18d471ef4ac8d4d8dc8efe6b59c8b86d0f709e553.jpg)  
Figure 3. Standardized percentage bias for each covariate before and after matching.

Figure 3 displays a graphical summary of covariate imbalance showing the standardized percentage bias for each covariate. It clearly shows that the covariate imbalance has been greatly reduced after matching.

Common support or overlap condition is a critical assumption in matching. The prior matching literature [38] suggests that checking the overlap or region of common support between treatment and control groups can be done through a visual inspection of the propensity score distributions for both the treatment and control groups. Figure 4 graphs the propensity score histogram by treatment status, and it reveals a clear overlapping of the distributions between treatment and control groups. Next, we re-estimate our fixed efects model (1a) using the new matched sample created by PSM, and the results are presented in column 2 of Table 4. The basic findings are consistent with those in our fixed efects model and Heckman-type model.

## Rosenbaum Bounds

PSM could not fully address the endogeneity concern caused by unobserved time-varying factors. If there are unobserved time-varying variables that simultaneously afect assignment into treatment and the outcome variable, PSM may not be robust against this hidden bias. We thus use the approach of Rosenbaum bounds [60] to address the concern of hidden bias that may be caused by unobserved time-varying factors. The basic idea of

![](/api/attachments/ZVXN26GJ/fulltext/images/c06c90114981a13fe2e696d4fa78bb496809e7f078b4488e26dfb7bf07ef4e89.jpg)  
Figure 4. Propensity score histogram by treatment status.

Rosenbaum bounds is to examine if PSM is sensitive to hidden bias: We can manipulate the estimated odds of receiving a treatment to see how much the estimated treatment efects may vary. In other words, we want to determine how strongly an unmeasured variable must influence the selection process to undermine the inference of the matching analysis.

In order to estimate the extent to which such “selection on unobservables” may bias our estimation and inference, we present the results of Rosenbaum bounds sensitivity using Wilcoxon’s signed rank test [60] in Table 6. Table 6 reports p-values from Wilcoxon signed rank tests for the averaged treatment efect while setting the level of hidden bias to a certain value Γ. In Table 6, Γ is the odds ratio of treatment assignment, which is a measure of the degree of departure from a study that is free of hidden bias. Our sensitivity analysis considers several possible values of Γ and shows how the inferences might change. When $\Gamma = 1$ , it implies that we assume the absence of unobserved selection bias. In this case, both the upper and lower bounds of $\boldsymbol { p }$ values are zero $( \mathrm { s i g } + = 0 , \mathrm { s i g } - = 0 )$ in Table $^ { 6 , }$ indicating that the efect of receiving a reputation badge is significant when there is no hidden bias. We interpret the $\boldsymbol { p }$ values under diferent values of Γ in Table 6 as follows: PSM is sensitive to hidden bias if values of Γ close to 1 could lead to inferences that are very diferent from those obtained assuming the study is free of hidden bias (Γ ¼ 1). PSM is insensitive if extreme values of Γ are required to alter the inference.

Table 6. Rosenbaum bounds for PSM: Range of significant levels for the signed rank statistic.

<table><tr><td>Γ</td><td>Sign+</td><td>Sign-</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>2</td><td>3.2e-10</td><td>0</td></tr><tr><td>3</td><td>6.3e-08</td><td>0</td></tr><tr><td>4</td><td>1.7e-05</td><td>0</td></tr><tr><td>5</td><td>0.0112</td><td>0</td></tr><tr><td>6</td><td>0.0243</td><td>0</td></tr><tr><td>7</td><td>0.146</td><td>0</td></tr></table>

Notes: Γ, odds of diferential assignment due to unobserved factors. Sign+, upper bound significance level; Sign-, lower bound significance level.

The critical level of Γ at which we would have to question the significance of our PSM is between 6 and $7$ (when $\Gamma = 7 .$ , the upper bound of $\dot { \boldsymbol { p } }$ value is greater than 5 percent): For the impact of reputation badges to disappear, the unobserved confounder has to cause the odds ratio of treatment assignment to difer between treatment and control groups by a factor of about $7 . ^ { 5 }$ Note that a Γ value of 6 is very large [37, 31] and it is well above the threshold values used in the prior studies for robust PSM [37, 67]. It is also worth noting that the Rosenbaum bounds are “worst-case” scenarios. An insignificant upper bound $\boldsymbol { p }$ value for Γ = 7 does not mean that there is no true positive efect of reputation badges on sales when $\Gamma = 7$ . This result means that the confidence interval for the efect of reputation badges would include zero if an unobserved variable causes the odds ratio of treatment assignment to difer between treatment and control groups by 7. As a summary, the results in Table 6 show that our PSM is robust to a plausible range of unobserved selection bias (hidden bias).

## Correlated Trend Model

A potential concern in the fixed efects model is whether there is heterogeneity in the pretreatment trends between control and treatment groups [4]. If there is a significant heterogeneity in the pretreatment trends, it suggests that the pretreatments may disproportionately afect treated sellers, as opposed to control sellers, and the parallel trend assumption is less likely to be satisfied. In our study, we conduct the correlated random trend model to address this concern and rule out the impact of pretreatments as an alternative explanation for our results. Specifically, we control for seller-specific time trends in the model. We follow [4] and estimate the following correlated random trend model:

$$
\log (S a l e s) _ {i j t} = a _ {i} + c _ {j} + \nu_ {t} + \beta_ {0} + g _ {i} t + \beta_ {1} G M _ {i t} + c o n t r o l s + \varepsilon_ {i j t}\tag{5}
$$

where $g _ { i }$ is a seller-specific time trend for seller i. This specification allows sellers to follow diferent time trends in a limited but potentially revealing way. It is worth noting that, in the correlated random trend model, g t can be correlated with $G M _ { i t }$ because in the estimation process, $g _ { i } t$ will be cancelled out by first diferencing equation (5) twice, and our estimation will be unbiased. Therefore, the fixed efects model with correlated random trends is likely to be more robust and convincing. We estimate equation (5) and the estimation results of the correlated random trend model are presented in column 3 of Table 4. We find that there is a minimal amount of change of the estimated efects of interest by the inclusion of these trends, which rules out individual specific time trends as an alternative explanation for our results.

## Placebo Test

We also conduct a placebo test to examine if our results could be driven entirely by some unobserved time-varying factors. The idea of the placebo test proposed here is akin to the framework in [10]: We estimate pseudo-causal efects that are known to be equal to zero based on a priori knowledge. More specifically, following [10], we randomly generate placebo reputation badges, where gold medal winners are chosen at random in each time period. Because these gold medal winners are fictitious, a significant “efect” of receiving reputation badges at the 5 percent level (5 percent significance level) should be found roughly 5 percent of the time. On the one hand, if in the placebo test, a significant “efect” at the 5 percent level is found at a value much larger than 5 percent of the time, then our interpretation is that our analysis could be driven by the placebo efect and does not provide significant evidence of a positive efect of reputation badges. On the other hand, if a significant “efect” at the 5 percent level is found at a value of about 5 percent, then our interpretation is that our analysis provides evidence that the positive efect of reputation badges is not driven by the placebo efect.

Following Bertrand et al. [10], we randomly assign reputation badges to sellers in diferent time periods using a pseudo random number generator. The values of our dependent variable do not change. We then re-estimate regression Equation (1a) using these placebo badges. The estimation generates an estimate of the “efect” of reputation badges and a standard error for this estimate. We repeat this exercise 1,000 times. Since these reputation badges are fictitious, we expect to reject the null hypothesis of no efect roughly 5 percent of the time (50 times). From our results for the 1,000 runs, we find that the fraction of simulations in which the null hypothesis is rejected is 4.2 percent (42 times), indicating that our results are unlikely to be driven by the placebo efect.

## Discussion and Conclusions

Reputation systems have been implemented by all major online markets as an important component of improving their operation eficiency by reducing uncertainty about the quality of the sellers. Studying the efect of reputation systems has been a long-standing active research area of online market literature. However, virtually all reputation systems examined in the extant literature reflect the sellers’ long-term accumulative reputation, which has several drawbacks that impede accomplishing the intended goals of the reputation systems. For example, long-term accumulative reputation, usually a simple scalar quantity, is susceptible to manipulations and does not consider the totality of sellers’ performance in transactions. Taobao.com, the largest consumer-to-consumer online market in China with 12 million active users each day, implemented the Gold Medal Seller (GMS) program in July 2014 as a concurrent second reputation mechanism to complement its existing long-term accumulative reputation system.

Our findings have useful managerial implications for both the online markets and sellers. We provide practical insights for reputation badge design and highlight the importance of introducing the possibility of losing reputation badges. Our results on gold medal sellers also apply to short-term reputation badges on other platforms, such as Top Rated Seller badges on eBay. Online markets should consider implementing a reputation system similar to Taobao.com’s GMS program as an additional mechanism to assess their sellers’ short-term comprehensive performance in parallel to their existing systems that track sellers’ long-term accumulative reputation since the GMS program is an efective means of mitigating the seller uncertainty and enhancing the eficiency of the market. One main drawback of the traditional reputation systems is the lack of the possibility of losing reputation badges. Our results provide a deeper understanding of the practical reputation badge design and show the critical signaling value of losing and keeping reputation badges. When losing a reputation badge is possible, keeping a reputation badge has a larger positive impact on product sales than earning a reputation badge.

For sellers, the GMS program is especially beneficial for those new entrants to the market. Earning reputation badges multiple times can help them compete with the established incumbent sellers as earning a badge has a significant and positive impact on the product sales, and earning badges multiple times is a much stronger signal for high-quality sellers to diferentiate themselves from low-quality sellers without relying on long-term reputation scores. Our research also highlights that earning a reputation badge might be a double-edged sword for sellers: If a seller earns a badge, and then loses it immediately in the next time period, consumers interpret it as a more negative signal than not earning a badge at all.

Our study is not without limitations. First, we collected six-month panel data from July 1 to December 31, 2015. Although the sample period is suficiently long, it would be ideal to have more data collected beyond the six-month period. Unfortunately, it is impossible to do so since Taobao.com no longer publishes daily sales data efective January 1, 2016. A second limitation of our research is that we focus on new search goods; therefore, our results should be interpreted as such with a grain of salt. An interesting avenue of future research is to replicate our study in the context of experienced goods. Third, the positive impact of reputation badge could come from short-term reputation or the endorsement efect of the platform. In our present study, we do not diferentiate between these two underlying mechanisms. A future research direction is to further separate the efect of short-term reputation from the endorsement efect of the platform using an experimental approach. Fourth, Taobao provides additional benefits to gold medal sellers. For example, the platform organizes sales promotion activities for GMS only. These confounding factors are dificult to tease out by nature because they are additional benefits brought by gold medals. Fifth, due to the limitation of our data collection, we are not able to aggregate the dataset into a daily level (some key variables were not collected at the daily level). Sixth, mobile devices are popular for online shopping, but the small screen size reduces the overall amount of information that consumers can access. In our context, a user interface on small mobile screens makes it dificult for consumers to locate detailed information [44]. It would be interesting to dig deep into the behavior diferences of mobile users in the future. Finally, it would be of interest for future research to further delineate the efect of reputation badges on the heterogeneity of buyers by understanding which type of buyers is most influenced by the reputation badge.

Using the GMS program as the backdrop of our study, our study addresses several intriguing research issues that have not been empirically examined in prior literature. We address the endogeneity concerns by adopting multiple causal identification strategies and establishing a robust quantitative relationship between earning a reputation badge and product sales. Our study fills an important gap in the literature by deriving several significant and useful findings on reputation badge design. First, earning a GMS badge indeed has a positive impact on product sales. Second, losing a reputation badge has a negative impact on product sales. More importantly, the magnitude of the efect of losing a reputation badge is larger than that of earning a badge. Third, keeping a reputation badge has a larger positive impact on product sales than earning a reputation badge. Finally, we find a positive moderating role of earning reputation badge multiple times: As a seller earns more reputation badges, earning or keeping a reputation badge has a larger positive impact on product sales, and losing a badge has a smaller negative impact on product sales.

## Notes

1. See https://www.alibabagroup.com/en/news/press\_pdf/p200522.pdf (last accessed: July 1, 2020).

2. See http://jinpai.taobao.com/seller/ (last accessed: July 2, 2020).

3. See http://jinpai.taobao.com/seller/ (last accessed: July 2, 2020).

4. The “charity plan” is a Taobao.com program where the participating sellers will donate 0.06 RMB on average to a charity of their choice for each completed transaction.

5. Intuitively, it means that for the impact of reputation badges to disappear, the unobserved confounder has to cause a seller to be seven times as likely as another seller to receive treatment (assuming the two sellers have the same observable characteristics).

## Acknowledgements

The authors are listed in the alphabetical order.

## Funding

The generous support for professional development from the John B. Higdon endowment is gratefully acknowledged. This research was partly supported by the Social Science Foundation of Ministry of Education of China (No. 17YJA630029), National Natural Science Foundation of China (No. 71601106 & No. 71531013), Shanghai Science and Technology Innovation Projects (No. 18511103703) and Pudong Science and Technology Development Fund (No. PKX2019-R01).

## References

1. Akerlof, G.A. The market for “lemons”: Quality uncertainty and the market mechanism. The Quarterly Journal of Economics, 84, 3 (1970), 488–500.

2. Axelrod, R. The Evolution of Cooperation. New York: Harper Collins, 1984.

3. Anderson, S.P.; and Renault, R. Advertising content. American Economic Review, 96, 1 (2006), 93–113.

4. Angrist, J.D.; and Pischke, J. S. Mostly Harmless Econometrics: An Empiricist’s Companion. Princeton: Princeton University Press, 2008.

5. Arrow, K.J. Uncertainty and the welfare economics of medical care. American Economic Review, 53, 5 (1963), 941–973.

6. Baker, W.E.; and Bulkley, N. Paying it forward vs. rewarding reputation: Mechanisms of generalized reciprocity. Organization Science, 25, 5 (2014), 1493–1510.

7. Bapna, R.; Qiu, L.; and Rice, S. Repeated interactions versus social ties: Quantifying the economic value of trust, forgiveness, and reputation using a field experiment. MIS Quarterly, 41, 3 (2017), 841–866.

8. Bapna, S.; Benner, M.J.; and Qiu, L. Nurturing online communities: An empirical investigation. MIS Quarterly, 43, 2, (2019) 425–452.

9. Bederson, B.B.; Jin, G.Z.; Leslie, P.; Quinn, A.J.; and Zou, B. Incomplete disclosure: Evidence of signaling and countersignaling. American Economic Journal: Microeconomics, 10, 1 (2018), 41–66.

10. Bertrand, M.; Duflo, E.; and Mullainathan, S. How much should we trust diferences-indiferences estimates? Quarterly Journal of Economics, 119, 1 (2004), 249–275.

11. Brown, G.K.; and Mergoupis, T. Treatment interactions with non-experimental data in Stata. Stata Journal, 11, 4 (2010), 545–555.

12. Cabral, L.; Ozbay, E.Y.; and Schotter, A. Intrinsic and instrumental reciprocity: An experimental study. Games and Economic Behavior, 87, C (2014) 100–121.

13. Cabral, L.; and Hortacsu, A. The dynamics of seller reputation: Evidence from eBay. The Journal of Industrial Economics, 58, 1 (2010) 54–78.

14. Chevalier, J.A.; and Mayzlin, D. The efect of word of mouth on sales: Online book reviews. Journal of Marketing Research, 43, 3 (2006), 345–354.

15. Clemons, E.K.; Gao, G.G.; and Hitt, L.M. When online reviews meet hyperdiferentiation: A study of the craft beer industry. Journal of Management Information Systems, 23, 2 (2006), 149–171.

16. de Haan, T.; Oferman, T.; and Sloof, R. Noisy signaling: theory and experiment. Games and Economic Behavior, 73, 2 (2011), 402–428.

17. Dellarocas, C. Building trust online: The design of robust reputation reporting mechanisms for online trading communities. In G.I. Doukidis, N. Mylonopoulos, and N. Pouloudi (eds.). Social and Economic Transformation in the Digital Era. IGI Global, Hershey, PA, 2004.

18. Dellarocas, C. Reputation mechanism design in online trading environments with pure moral hazard. Information Systems Research, 16, 2 (2005), 209–230.

19. Dellarocas, C.; and Wood, C.A. The sound of silence in online feedback: Estimating trading risks in the presence of reporting bias. Management Science, 54, 3 (2008), 460–476.

20. Dennis, A.R.; Yuan, L.; Feng, X.; Webb, E.; and Hsieh, C.J. Digital nudging: Numeric and semantic priming in e-commerce. Journal of Management Information Systems, 37, 1, (2020) 39–65.

21. Dimoka, A.; Hong, Y.; and Pavlou, P.A. On product uncertainty in online markets: Theory and evidence. MIS Quarterly, 36, 2, (2012) 395–426.

22. Elfenbein, D.W.; Fisman, R.; and McManus, B. Market structure, reputation, and the value of quality certification. American Economic Journal: Microeconomics, 7, 4 (2015) 83–108.

23. Fan, Y.; Ju, J.; and Xiao, M. Reputation premium and reputation management: Evidence from the largest e-commerce platform in China. International Journal of Industrial Organization, 46, (2016) 63–76.

24. Feltovich, N.; Harbaugh, R.; and To, T. Too cool for school? Signalling and countersignalling. RAND Journal of Economics, 33, 4, (2002) 630–649.

25. Ghose, A. Internet exchanges for used goods: An empirical analysis of trade patterns and adverse selection. MIS Quarterly, 33, 2 (2009) 263–291.

26. Ghose, A.; Ipeirotis, P.G.; and Sundararajan, A. Opinion mining using econometrics: A case study on reputation systems. In Proceedings of the 45th Annual Meeting of the Association of Computational Linguistics, 7, (2007) 416–423, Prague, Czech Republic. Stroudsburg, PA: The Association for Computational Linguistics.

27. Ghose, A.; Smith, M.D.; and Telang, R. Internet exchanges for used books: An empirical analysis of product cannibalization and welfare impact. Information Systems Research, 17, 1, (2006) 3–19.

28. Goh, K.Y.; Heng, C.S.; and Lin, Z. Social media brand community and consumer behavior: Quantifying the relative impact of user-and marketer-generated content. Information Systems Research, 24, 1, (2013) 88–107.

29. Grossman, G.M.; and Shapiro, C. Informative advertising with diferentiated products. Review of Economic Studies, 51, 1, (1984) 63–81.

30. Gu, B.; Park, J.; and Konana, P. Research note—the impact of external word-of-mouth sources on retailer sales of high-involvement products. Information Systems Research, 23, 1, (2012) 182–196.

31. Guo, S.; and Fraser, M. Propensity Score Analysis: Statistical Methods and Applications. Los Angeles: Sage Publications, 2010.

32. Hong, Y.; and Pavlou, PA. Product fit uncertainty in online markets: Nature, efects, and antecedents. Information Systems Research, 25, 2, 2014 328–344.

33. Houser, D.; and Wooders, J. Reputation in auctions: Theory, and evidence from eBay. Journal of Economics & Management Strategy, 15, 2 (2006), 353–369.

34. Hu, Y.; Xu, A.; Hong, Y.; Gal, D.; Sinha, V.; and Akkiraju, R. Generating business intelligence through social media analytics: measuring brand personality with consumer-, employee-, and firm-generated content. Journal of Management Information Systems, 36, 3 (2019), 893–930.

35. Hu, N.; Liu, L.; and Zhang, J.J. Do online reviews afect product sales? The role of reviewer characteristics and temporal efects. Information Technology and Management, 9, 3 (2008), 201–214.

36. Hui, X.; Saeedi, M.; Shen, Z.; and Sundaresan, N. Reputation and regulations: evidence from eBay. Management Science, 62, 12 (2016), 3604–3616.

37. Keele, L. An overview of rbounds: An R package for Rosenbaum bounds sensitivity analysis with matched data. Working Paper, 2010. Acessed on 10 June, 2017: http://www.personal.psu. edu/ljk20/rbounds%20vignette.pdf.

38. Khurana, S.; Qiu, L.; and Kumar, S. When a doctor knows, it shows: An empirical analysis of doctors’ responses in a Q&A forum of an online healthcare portal. Information Systems Research, 30, 3 (2019), 872–891.

39. Kim, D.; and Benbasat, I. The efects of trust-assuring arguments on consumer trust in internet stores: Application of Toulmin’s model of argumentation. Information Systems Research, 17, 3 (2006) 286–300.

40. Kim, Y.; and Krishnan, R. On product-level uncertainty and online purchase behavior: An empirical analysis. Management Science, 61, 10 (2015), 2449–2467.

41. Kumar, N.; Venugopal, D.; Qiu, L.; and Kumar, S. Detecting review manipulation on online platforms with hierarchical supervised learning. Journal of Management Information Systems, 35, 1 (2018), 350–380.

42. Kumar, N.; Qiu, L.; and Kumar, S. Exit, voice, and response on digital platforms: An empirical investigation of online management response strategies. Information Systems Research, 29, 4 (2018), 849–870.

43. Kumar, N.; Venugopal, D.; Qiu, L.; and Kumar, S. Detecting anomalous online reviewers: An unsupervised approach using mixture models, Journal of Management Information Systems, 36, 4 (2019), 1313–1346.

44. Kwark, Y.; Lee, G.M.; Pavlou, P.A.; and Qiu, L. On the spillover efects of online product reviews on purchases: Evidence from clickstream data, working paper, 2019. Accessed on 03 December, 2019: https://ssrn.com/abstract=2838410.

45. Lee, G.M.; Qiu, L.; and Whinston, A.B. A friend like me: modeling network formation in a location-based social network. Journal of Management Information Systems, 33, 4 (2016), 1008–1033.

46. Li, X. Could deal promotion improve merchants’ online reputations? The moderating role of prior reviews. Journal of Management Information Systems, 33, 1 (2016), 171–201.

47. Lin, Z.; and Heng, C.S. The paradoxes of word of mouth in electronic commerce. Journal of Management Information Systems, 32, 4 (2015), 246–284.

48. Liu, Q.; and Skrzypacz, A. Limited records and reputation bubbles. Journal of Economic Theory, 151, (2014) 2–29.

49. Lucking-Reiley, D.; Bryan, D.; Prasad, N.; and Reeves, D. Pennies from eBay: The determinants of price in online auctions. The Journal of Industrial Economics, 55, 2 (2007), 223–233.

50. Lwin, M.O.; and Williams, J.D. Promises, promises: How consumers respond to warranties in internet retailing. Journal of Consumer Afairs, 40, 2 (2006), 236–260.

51. Melnik, M.I.; and Alm, J. Seller reputation, information signals, and prices for heterogeneous coins on eBay. Southern Economic Journal, 72, 2 (2005), 305–328.

52. Milgrom, P.; and Roberts, J. Price and advertising signals of product quality. Journal of Political Economy, 94, 4 (1986), 796–821.

53. Nosko, C.; and Tadelis, S. The Limits of reputation in platform markets: An empirical analysis and field experiment, The National Bureau of Economic Research, 2015, Paper No. 20830.

54. Oram, A. Peer-to-Peer: Harnessing the Power of Disruptive Technologies. Cambridge, MA: O’Reilly Media, Inc., 2001.

55. Özpolat, K.; Gao, G.; Jank, W.; and Viswanathan, S. Research note—The value of third-party assurance seals in online retailing: An empirical investigation. Information Systems Research, 24, 4 (2013), 1100–1111.

56. Pavlou, P.A.; and Dimoka, A. The nature and role of feedback text comments in online marketplaces: Implications for trust building, price premiums, and seller diferentiation. Information Systems Research, 17, 4 (2006), 392–414.

57. Pavlou, P.A.; and Gefen, D. Building efective online marketplaces with institution-based trust. Information Systems Research, 15, 1 (2004), 37–59.

58. Pu, J.; Chen, Y.; Qiu, L.; and Cheng, H.K. Does identity disclosure help or hurt user content generation? Social presence, inhibition, and displacement efects. Information Systems Research, 31, 2 (2020), 297–322.

59. Qiu, L.; Tang, Q.; and Whinston, A.B. Two formulas for success in social media: Learning and network efects. Journal of Management Information Systems, 32, 4 (2015), 78–108.

60. Rosenbaum, P.R. Observational Studies. 2nd ed. New York: Springer, 2002.

61. Resnick, P.; Kuwabara, K.; Zeckhauser, R.; and Friedman, E. Reputation systems. Communications of the ACM, 43, 12 (2000), 45–48.

62. Roberts, J.W. Can warranties substitute for reputations? American Economic Journal: Microeconomics, 3, 3 (2011), 69–85.

63. Siering, M.; and Janze, C. Information processing on online review platforms. Journal of Management Information Systems, 36, 4 (2019), 1347–1377.

64. Spence, M. Job market signaling. Quarterly Journal of Economics, 87, 3 (1973), 355–374.

65. Sullivan, L.M.; Dukes, K.A.; and Losina, E. An introduction to hierarchical linear modelling. Statistics in Medicine, 18, 7 (1999), 855–888.

66. Tversky, A.; and Kahneman, D. Loss aversion in riskless choice: A reference-dependent model. Quarterly Journal of Economics, 106, 4 (1991), 1039–1061.

67. Wei, Z.; and Lin, M. Market mechanisms in online peer-to-peer lending. Management Science, 63, 12 (2017), 4236–4257.

68. Yoo, E.; Gu, B.; and Rabinovich, E. Difusion on social media platforms: A point process model for interaction among similar content. Journal of Management Information Systems, 36, 4 (2019), 1105–1141.

69. Zhang, J. The roles of players and reputation: Evidence from eBay online auctions. Decision Support Systems, 42, 3 (2006), 1800–1818.

## About the Authors

Hsing Kenneth Cheng (hkcheng@ufl.edu) is the John B. Higdon Eminent Scholar and Department Chair in the Department of Information Systems and Operations Management, Warrington College of Business, University of Florida. He received his Ph.D. from the University of Rochester. His research interests focus on analyzing the impact of Internet technology on software development and marketing, and information systems policy issues. Dr. Cheng’s research has appeared in premier academic journals, such as Information Systems Research, Journal of Management Information Systems, MIS Quarterly, and Production and Operations Management.

Weiguo Fan (weiguo-fan@uiowa.edu) is a Henry B. Tippie Chair Professor in Business Analytics at the Tippie College of Business, University of Iowa. He received his Ph.D. from the Ross School of Business, University of Michigan. His research interests focus on the design and development of novel information technologies—information retrieval, data mining, text analytics, social media analytics, business intelligence techniques—to support better business information management and decision making. Dr. Fan has published more than 250 refereed journal and conference papers. His research has appeared in many premier journals such as Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Productions and Operations Management, IEEE Transactions on Knowledge and Data Engineering, and others.

Peipei Guo (guopeip0413@163.com) is a data scientist at Cardinal Operation Co. Ltd. She received her Ph.D. degree from Shanghai University of Finance and Economics. Her research interests focus on data analytics and machine learning to support better business decision making.

Hailiang Huang (hlhuang@shufe.edu.cn; corresponding author) is a chair professor with the School of Information Management & Engineering, Shanghai University of Finance and Economics, China. He received his Ph.D. degree from Xi’an Jiaotong University, China. His research interests include e-commerce, Fintech and artificial intelligence applications in business. Dr. Huang’s research has appeared in IEEE Transactions on Dependable and Secure Computing, Decision Support Systems, Knowledge Based Systems, and other venues.

Liangfei Qiu (liangfei.qiu@warrington.ufl.edu) is an Associate Professor and Hough Faculty Fellow in the Department of Information Systems and Operations Management, Warrington College of Business, University of Florida. He received his Ph.D. from the University of Texas at Austin. Dr. Qiu’s research focuses on prediction markets, social networks and social media platforms, telecommunications networks, and economics of information systems. His work has appeared in premier academic journals, such as Information Systems Research, Journal of Management Information Systems, MIS Quarterly, and Production and Operations Management.
