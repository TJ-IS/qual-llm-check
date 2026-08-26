---
otero_id: 1336
otero_key: "Z77M45NR"
title: "Pricing Models for Online Advertising: CPM vs. CPC"
authors: "Kursad Asdemir; Nanda Kumar; Varghese S. Jacob"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1110.0391"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/Z77M45NR/fulltext/images/7cba52970dfff24b11554ee72576355270d10d8a894a60b83c7f6563ba440bcd.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Pricing Models for Online Advertising: CPM vs. CPC

Kursad Asdemir, Nanda Kumar, Varghese S. Jacob,

## To cite this article:

Kursad Asdemir, Nanda Kumar, Varghese S. Jacob, (2012) Pricing Models for Online Advertising: CPM vs. CPC. Information Systems Research 23(3-part-1):804-822. http://dx.doi.org/10.1287/isre.1110.0391

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/Z77M45NR/fulltext/images/88cf89bd51ebaafd91540ba7e78f342298096ca1e3ae77c877aa59dd64aa613a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Pricing Models for Online Advertising: CPM vs. CPC

Kursad Asdemir

Faculty of Business and Economics, United Arab Emirates University, Al Ain, United Arab Emirates, kursad.a@uaeu.ac.ae

Nanda Kumar, Varghese S. Jacob

School of Management, University of Texas at Dallas, Richardson, Texas 75083 {nkumar@utdallas.edu, vjacob@utdallas.edu}

nline advertising has transformed the advertising industry with its measurability and accountability. Online software and services supported by online advertising is becoming a reality as evidenced by the success of Google and its initiatives. Therefore, the choice of a pricing model for advertising becomes a critical issue for these firms. We present a formal model of pricing models in online advertising using the principal–agent framework to study the two most popular pricing models: input-based cost per thousand impressions (CPM) and performance-based cost per click-through (CPC). We identify four important factors that affect the preference of CPM to the CPC model, and vice versa. In particular, we highlight the interplay between uncertainty in the decision environment, value of advertising, cost of mistargeting advertisements, and alignment of incentives. These factors shed light on the preferred online-advertising pricing model for publishers and advertisers under different market conditions.

Key words: online advertising; cost per impression (CPM); cost per click (CPC); pricing models; asymmetric information; delegation; principal–agent model

History: Paulo Goes, Senior Editor; Giri Kumar Tayi, Associate Editor. This paper was received on October 10, 2007, and was with the authors 17 months for 4 revisions. Published online in Articles in Advance December 7, 2011.

## 1. Introduction

Worldwide online advertising spending is projected to reach \$98 billion annually by 2012. In an effort to capture a piece of this action, Microsoft launched an unsuccessful \$47.5 billion hostile takeover bid against Yahoo! on May 3, 2008 (eMarketer 2008b, New York Times 2009). This move by the world’s largest software maker underlines a fundamental shift in information technology from the desktop platform to online software and services. Online advertising is an indispensable part of the business models of firms that will provide advertising-supported online services. A basic understanding of the economics of online advertising will be a critical success factor for these companies. In this paper we develop a game-theoretic model that sheds light on the fundamental economic incentives and trade-offs that online advertisers and publishers face in choosing the right pricing model.

There has been intense debate on the most appropriate pricing model for Internet advertising: cost per thousand impressions (CPM) or cost per click-through (CPC). In the CPM model, an advertiser pays for impressions. In other words, the advertiser pays the publisher when a visitor has been given an opportunity to see an advertisement, i.e., an impression. This approach is closer to the traditional magazine advertising, wherein magazine publishers are compensated on the circulation of their magazines. In the CPC model, the publisher pays only for clickthroughs (click hereafter)—when a visitor clicks on an advertisement (ad hereafter).

The impact of advertising on sales is hard to measure. John Wanamaker’s famous phrase, “Half my advertising is wasted, I just don’t know which half,” highlights this fact (Ad Age 2008). Online advertising distinguishes itself from traditional media advertising by its measurability and accountability. By measurability, we mean that the performance of a campaign can be tracked in real time using metrics such as clicks. By accountability, we mean that the websites can be compensated based on these metrics. In its early days, these features of online advertising were thought to be its major competitive advantage over other media. The following excerpt from Wired magazine reflects the beliefs in that period: “The Net is accountable 0 0 0 0 It is the highway leading marketers to their Holy Grail: single-sourcing technology that can definitively tie the information consumers perceive to the purchases they make” (Rothenberg 1998).

In fact, in April 1996, Yahoo! agreed with Procter & Gamble to be compensated on the basis of clicks (Novak and Hoffman 1997). As a result, the metric of accountability became the number of clicks. However, after initial successes, click rates started dropping steadily from levels of 5% to 0.2%, raising issues about the effectiveness of the Internet as an advertising medium (Gaffney 2001). This trend forced publishers to move away from click as a performance measure. On July, 2001, CBS MarketWatch.com announced that it would not report the number of clicks to its advertisers unless specifically requested (I-Advertising 2001). Publishers retreated from the total-accountability ideal and despised click as a success measure. Not surprisingly, advertisers do not share the same views with publishers. The following quote from Business Week illustrates this position:

Michael Sands is tired of hearing how much the Internet is like television. But the marketing head of online travel company Orbitz … says … “There’s a notion that accountability is not the direction to go in,” scoffs Sands, who adds: “That’s frightening. Worse, it’s a capitulation.” (Black 2001)

Despite these troubles, the CPC model regained its prevalence by the tremendous success of search engine advertising. Search engines invented innovative ways to sell advertising using the CPC model to thousands of advertisers. However, recent industry statistics show that the CPM model still generates a large portion of online advertising revenue (IAB 2008). This makes CPM an attractive model even to one of the most successful search engines, Google. Google, which discontinued its CPM-based Premium Sponsorship program in 2003, recently reintroduced another CPM-based program (Lee 2005a).

Thus, reviews in the trade press and the practices in the industry highlight a lack of any consensus between advertisers and publishers on an appropriate pricing model for Internet advertising. At the heart of this tension lies the fact that advertisers want their ads to be seen by their target consumers. Accordingly, they would like their ads to be placed on Web pages whose visitors share the characteristics of their target consumers. With the websites changing their content (and organization) on a continuous basis, information pertaining to the characteristics of visitors to different pages in a publisher’s website can be prohibitively expensive to acquire for an advertiser. However, the publisher can gather such information with relative ease and use it to enhance the effectiveness of the advertiser’s campaign. Although advertisers would like the publishers to perform this service, publishers appear to have no incentive to use or acquire such information to enhance the effectiveness of advertising campaigns.

Consequently, one would expect advertisers to prefer a performance-based pricing model (CPC) to one that does not hold the publishers accountable (CPM).

Table 1 Pricing Model Choice on Google.com for the Search Phrase “Computer” on November 13, 2002

<table><tr><td>Advertiser</td><td>Pricing model</td></tr><tr><td>SonyStyle.com</td><td>CPM</td></tr><tr><td>Gateway.com</td><td>CPM</td></tr><tr><td>eBay.com</td><td>CPM</td></tr><tr><td>Computers-coupon-gateway.com</td><td>CPC</td></tr><tr><td>Shopper.cnet.com</td><td>CPC</td></tr></table>

However, as illustrated in Table 1, not all advertisers prefer the CPC model to the CPM model.

The choice of pricing models made by different advertisers is quite puzzling. One observes that for the same search phrase, “computer,” on the same publisher, Google.com, some advertisers prefer the CPM model to the CPC model and others prefer the CPC model to the CPM model. This behavior can be explained if there is a corporate policy in place that forces the advertiser to adopt one pricing model regardless of the market forces at work. However, there are instances in which an advertiser uses the CPM model for some search phrases and the CPC model for other search phrases. For example, eBay.com uses the CPM model for the search phrases “Dell” and “Hewlett-Packard” but the CPC model for the search phrases “Vaio” and “Pentium.”<sup>1</sup> This practice suggests that at least some of the variation in advertisers’ choice of one pricing model over the other may be influenced by market factors. Shedding light on some of the strategic forces that may influence advertisers’ and publishers’ choice of the pricing model is the main goal of this study.

We develop an economic model of targeting and volume decisions in an online advertising campaign. We use a principal–agent model to capture the institutional context in which CPM and CPC decisions are made. In our model the principal (advertiser) hires an agent (publisher) to deliver advertising.<sup>2</sup> Agency theory models focus on situations where the agent’s effort is unobservable and so the principal is uncertain about the agent’s effort level. The challenge then is to devise compensation contracts that offer the right incentives and insurance to the agent to engage in the desired level of effort recognizing the stochastic relationship between the agent’s effort and the output. This methodology has been extensively used in various domains to analyze and explain behavior of economic agents. For example, Austin (2001) considers a system development problem in which a project manager (principal) tries to balance incentives given to an individual software developer (agent) for staying on schedule versus producing high-quality software. More recently, Iyer et al. (2005) model a supply chain management context in which a buyer (principal) faces the problem of delegating product specification and/or production decisions to a supplier (agent).

In our setting, the advertiser seeking to advertise to her target segment is uncertain about the pages that these consumers visit at the publisher’s website. The advertiser can induce the publisher to acquire information regarding pages visited by her target market by engaging in a performance-based (CPC) contract. For the advertiser, a performance-based contract entails delegating campaign decisions to the publisher and, as in the traditional agency model, tying compensation to the value generated from advertising. Consequently, the advertiser faces the following tradeoff: she can control campaign decisions by choosing on which pages and how much to advertise with the CPM model, or she can opt for the CPC model where the publisher has control over decisions but also has better information. We are interested in understanding the role market conditions play in influencing the preference for the CPC or the CPM model.

The model provides insight on several issues related to the choice of pricing models. Specifically, we address the effects of the advertiser’s targetmarket characteristics, competition for advertising space, and control over the advertising campaign decisions on the choice of the appropriate pricing model for online advertising. We identify four important factors that affect the preference of the CPM model to the CPC model, and vice versa. Specifically, we highlight the interplay between uncertainty in the decision environment, value of advertising, cost of mistargeting ads, and alignment of incentives on the choice of the pricing model. We discuss the implications of these effects from the perspectives of advertisers and publishers.

The rest of the paper is organized as follows. In the next section, we review the relevant literature. In §3, we introduce our models and their assumptions. We compare the CPC model with the CPM model in §4. Section 5 presents alternative specifications of the models and the insights obtained. Section 6 discusses the managerial implications for advertisers and publishers. Finally, we conclude the paper with a discussion and future directions in §7.

## 2. Literature Review

Academic research on online advertising has been conducted on three fronts: developing measurement standards, understanding advertising response on the Internet, and developing models of operational advertising decisions such as targeting and scheduling banner ads or determining the level of advertising.

Because there were no established standards in Internet advertising, some of the early work dealt with exploring possible standards for the industry. Hoffman and Novak (2000) and Novak and Hoffman (1997) propose standard measurement constructs and point out potential problems in Internet advertising pricing models. However, they do not identify the market conditions that dictate the use of a particular pricing model. We extend this literature by investigating the economic incentives influencing the choice of a pricing model.

Marketing researchers have been interested in identifying factors influencing a visitor’s response to Internet advertising. Using “click” as a response measure, Chatterjee et al. (2003) consider the effects of exposure to repeated banner advertising and competing ads. Manchanda et al. (2006) find evidence that there is temporal separation between exposure to advertising and action. This problem has been recognized by the industry, and a new metric “viewthrough,” which measures the number of people who visited an advertiser’s website after exposure to advertising without clicking on the ad, has been introduced. We incorporate this feature in our model by associating value with exposure to advertising rather than the number of clicks. This implies that the value can be generated either through clicks or viewthroughs.

Substantial work has been done to improve operational Internet advertising decisions. Dewan et al. (2002) build an optimal control theory model to balance advertising and content on a website. Kumar et al. (2006) consider scheduling banner ads on a Web page. Karuga et al. (2001) develop the AdPalette algorithm, which dynamically changes ad copies based on click response. Langheinrich et al. (1999) develop a linear programming model for nonintrusive targeting to increase click rates. Tomlin (2000) highlights potential problems with the linear programming approach and proposes a solution using traffic theory. Kohda and Endo (1996) propose an advertising agent, which selects ads based on consumers’ indicated preferences. Baudisch and Leopold (1997) also propose userconfigurable ads where the user indicates her interests. Gallagher and Parsons (1997) propose a framework where demographics of each individual are matched against a defined demographic target. Even though our focus is on strategic issues, our study has implications on ad copy (text, banner, video, etc.), design, and targeting choice under uncertainty.

The delegation issue in a general context has attracted considerable interest in the literature. The delegation literatures in accounting and economics have mainly focused on decision-making rights within organizations (e.g., Aghion and Tirole 1997, Melumad and Reichelstein 1987). In information systems, outsourcing can be considered as a delegation mechanism (Wang et al. 1997). Delegation issue also arises in supply chains and distribution channels (e.g., Iyer et al. 2005). In marketing literature, delegation of pricing decisions to the sales force has been studied (e.g., Lal 1986). Lal (1986) shows that a necessary condition for delegation to be preferred by the principal is that the agent is better informed than the principal. In this case where the agent cannot communicate his private information, the principal is always weakly better off by delegating decisions to the agent. We contribute to this literature by showing that the benefits of delegation may be outweighed by costs incurred because of the loss of control in the online advertising context. Therefore, delegation may not always be preferred by a principal even though the agent is better informed. We see our work contributing to the literature on Internet advertising, delegation, and agency theory. Next, we present the notation and the description of our model and motivate its assumptions.

## 3. Model Description

A risk-neutral advertiser faces the problem of choosing where to advertise (targeting) and how much to advertise (volume). It is well known that advertisers often classify the consumer population into a target market segment and a nontarget market segment depending on how likely they are to purchase their product (Assael and Cannon 1979). Consequently, advertising to consumers in the target segment yields a higher return relative to advertising to consumers in the nontarget segment. We assume that the value of reaching the target segment (exposure value) is a per impression,<sup>3</sup> and the exposure value in the nontarget segment is b $( b < a )$ per impression. This ensures that the advertiser would prefer targeted ads. However, in our model the advertiser does not know with certainty which pages attract target market consumers. For instance, in an actual media plan for Samsonite luggage, the target market segment is composed of (1) adults 25–54, household income \$25,000+, business travelers; (2) men 25–54, household income \$40,000+, business travelers; (3) adults 25–54, household income \$25,000+, long trips 4+ (Barban et al. 1993). If Samsonite plans to advertise on Yahoo!, Samsonite may choose to advertise on Yahoo! Travel (travelers) or Yahoo! Finance (high-income segment) but may not exactly know whether these consumers share the characteristics of its target segment. Yahoo!, on the other hand, may acquire this information with relative ease using consumers’ transaction history, Web server log files, data collected using cookies, and market research.

![](/api/attachments/Z77M45NR/fulltext/images/39cb604fa2d7c4d0faef4cd4c769bee35dc2800c5043015e79052e175b592d03.jpg)

To model targeting and volume decisions together in this setting, we develop the following model. Namely, target and nontarget segments on a website lie on a targeting line between zero and one (Figure 1). The idea we seek to capture here is that the advertiser’s target consumers may visit certain pages on the publisher’s site more often than the nontarget consumers do. For simplicity we assume that pages visited by the target consumers are not visited by the nontarget consumers, and vice versa. The targeting line (between zero and one) in Figure 1 may be interpreted as the content continuum on the publisher’s website. It is possible to arrange the pages so that pages in the interval [01 T ] on the targeting line are visited by the target segment whereas those in the interval [T 1 1] on the targeting line are visited by the nontarget consumers. The boundary page, located at T , between target and nontarget segments is assumed to be unknown to the advertiser but may be acquired by the publisher at a negligible cost. We assume that the boundary is a random variable T that can be anywhere between $c \ ( 0 = c = 1 )$ and d 4c = d = 15. We assume T has a uniform distribution F 4T 5 (see Figure 1).<sup>4</sup> The advertiser’s targeting decision is to choose a spread level s 40 = s = 15, which indicates that the ads will be shown in the interval [01 s].

For example, Dell Computers advertises on Google.com. Choosing s = 1 means that Dell Computers advertises on all result pages generated by Google.com searches. Clearly, there will be result pages in the (d1 1] region such as “Edmonton weather,” “Sears Canada,” and others that may not be visited by the target segment of Dell. In contrast, there will be pages in the [01 c5 region such as “Dell computer,” “Dell Inspiron,” and “Dell Inspiron 6400,” that are very likely to be visited by a potential Dell customer. Choosing a small s would correspond to a very targeted advertising campaign using result pages like “buy Dell Inspiron 6400,” yet there are also result pages that would be in the [c1 d] region such as “Computer” that may or may not be visited by potential customers. Volume decisions are made by setting the intensity of the campaign x, which is the number of impressions at each point on the targeting line. The advertiser thus faces the following revenue function when the realization of T is :

$$
\Pi^ {A} (x, s \mid \tau) = \left\{ \begin{array}{l l} a s x & \text { if } s \leq \tau , \\ (a \tau + b (s - \tau)) x & \text { otherwise }. \end{array} \right.\tag{1}
$$

It is costly to provide content, create infrastructure, and attract unique visitors for a website publisher (MarketWatch 2002). We assume that the risk-neutral publisher’s cost of generating impressions $( \mathrm { i . e . , }$ reaching unique visitors) depends on x and the cost of delivering the campaign depends on the total number of impressions xs. Two natural characteristics of the publisher’s cost function are (a) for the same number of total impressions, cost should increase with better targeting; and (b) for a fixed targeting level, additional cost of attracting another visitor should increase as the number of impressions increase.<sup>5</sup> Appendix A in the online supplement<sup>6</sup> provides an example derivation of these qualitative characteristics that follows from Butters (1977) and Grossman and Shapiro (1984) in the economic analysis of advertising literature. The quadratic form has been used by Tirole (1987, §7.3.2.1) and Bagwell (2007). A cost function for generating impressions and delivering an advertising campaign that captures these features is $C ( x , s ) = x ^ { 2 } + k x s$ , where $a > k > b . ^ { 7 }$ We call k the ad serving cost; k captures the cost of serving ads and tracking and reporting impressions and clicks. Because $k > b ,$ , the advertiser loses money in the nontarget segment. This, in turn, makes targeting important. We assume that k is a realization of a random variable $\tilde { k } \sim \mathrm { U } [ \underline { { k } } , \bar { k } ]$ . Furthermore, only the publisher knows this value. The advertiser does not know the realization of the ad serving cost k; however, she knows the distribution of ad serving costs. To focus on regions in which targeting is important, we assume $b < \underline { { k } }$

In the next three sections, we discuss our models of the two most popular compensation contracts in the online advertising industry. These models are principal–agent type models where a principal (advertiser) hires an agent (publisher) to deliver advertising. Of particular interest is whether a compensation contract can induce the publisher to acquire the target segment boundary information. We assume that for the advertiser it is too costly to acquire this information; however, the publisher can attain this information with minimal costs.

## 3.1. The CPM Model

We begin with the CPM model where targeting and volume decisions are made by the advertiser. Hence, CPM is a pricing model where decisions are centralized. In this model, both of the decisions are observable and the publisher delivers as promised. In Figure 2, the game unfolds according to the following timeline of events.

In stage 1, the CPM contract, which specifies the campaign decisions $( x , s )$ and the price per impression 4p5, is agreed upon, and the advertiser pays for the total number of impressions (pxs). The assumption that price is set by the advertiser approximates markets in which prices are negotiable. For instance, there is evidence in the trade press that although many publishers have rate cards, often the price paid by the advertiser is significantly lower than the quoted price (Meskauskas 2006). More recently, Google, among others, allows advertisers to bid a CPM/CPC price that it may reject if it has better offers. Furthermore, it appears to be standard industry practice wherein in the CPM model the advertiser specifies where and how much to advertise, whereas in the CPC model the publisher determines where to place the ad copy and with what intensity. The assumptions regarding the decisions made in the first stage attempt to capture this institutional reality.<sup>8</sup> In the second stage, the uncertainty in the target-segment boundary is resolved ( is realized). Regardless of this realization, the publisher delivers the promised intensity and spread in stage 3. In stage 4, the advertiser obtains the value generated from the campaign. Then, the advertiser’s decision problem can mathematically be expressed as

Figure 2 Timeline of Events in the CPM Model  
![](/api/attachments/Z77M45NR/fulltext/images/0f3583b72a7521e4f428c8ee15be204614f4736fa1347ef150c8c3ad147a13a5.jpg)

$$
\begin{array}{l l} \mathrm {P_ {CPM}} \colon & \max _ {p,   x,   s} \left\{\mathrm{E} \big [ \Pi^ {A} (x,   s,   \mathrm{T}) \big ] - p x s \right\} \\ & \text { subject   to } \quad p - \frac {\bar {C} (x ,   s)}{x s} \geq u, \end{array}\tag{IR-1}
$$

where $\bar { C } ( x , s ) = x ^ { 2 } + \bar { k } x s .$

In $\mathrm { P _ { C P M } , }$ the advertiser’s decision variables are price per impression 4p5, the campaign intensity 4x5, and the campaign spread level 4s5; the publisher decides whether to accept or reject the offer. But the individual rationality constraint (IR-1) in $\mathrm { P _ { C P M } }$ guarantees that for every impression, the publisher makes at least his reservation utility per impression, u. As noted earlier, the advertiser’s bid may be rejected if it is not at least as good as a competitive bid. In practice, the advertiser may not be fully informed about the outside options of the publisher and/or the ad serving costs. For simplicity, we assume that the reservation utility, u, is known to the advertiser but the ad serving costs are not. Because the advertiser does not know the realization of the ad serving cost k, in (IR-1) the advertiser guarantees that the publisher accepts the contract by using the upper limit of the ad serving cost distribution, <sup>¯</sup>k. If the advertiser offers a contract based on the average cost, the publisher may reject such an offer when k is higher than the average ad serving cost.

By endowing the publisher with an outside option per impression, we capture the effect of competition for advertising space on the pricing model choice. When competition for advertising space is high (low) the publisher’s outside options, and hence u, will be high (low). Therefore, u tends to increase as the competition for advertising space and/or the leverage of the publisher increases. Because the advertiser prefers paying the minimum amount possible that will make the publisher content with the offer, she can adjust the per impression price (p5 so that in equilibrium (IR-1) binds in $\mathrm { P _ { C P M } } .$ . The emerging ad exchange model that became widely known after Yahoo!’s acquisition of Right Media Inc., which is worth more than \$680 million, is a good example of how our CPM model can be implemented in the real world:

With ad exchanges, member advertisers specify the price they’re willing to pay for a certain type of ad spot, such as a banner ad that will be viewed by a female in Boston. When a woman in Boston pulls up a Web page of an exchange member with a banner slot available, software assesses the exchange’s offer. If the price offered is better than the site’s minimum rate for that page and higher than what it can get from other sources, such as ads sold by its sales staff, the site will usually accept the exchange-brokered offer. The exchange’s computers can then deliver the winning ad to be displayed as the Web page loads on the consumer’s PC. The exchange immediately notifies the site if it doesn’t have a buyer for the ad space, and the site can then put in a nonpaying house ad or try other means to unload it on the fly.

(Guth and Delaney 2007, B1)

Although the ad exchange model implements the model at a per impression basis, CPM campaigns traditionally span many months or years and have multimillion dollar budgets. Fortune Magazine reports that companies such as Chrysler and Pepsi-Cola run such advertising campaigns on Yahoo! (Vogelstein 2005). Typically an ad agency’s creative department designs the ad copies (banners or rich media), and the media buying/planning department, which has long-term relationships with publishers, makes the campaign buys. In this sense, our model is a reasonable abstraction of the online media buying process in which media buyers can have knowledge of a publisher’s minimum acceptable rate.

## 3.2. The CPC Model

In the CPC model, the publisher’s compensation is based on the number of clicks; the campaign decisions are thus delegated to the publisher who in turn decides on targeting 4s5 and intensity 4x5. To keep the analysis simple, we assume that the publisher incurs a fixed cost to acquire the target boundary information; we normalize this fixed cost to zero without any loss of generality. In the CPC model, the advertiser delegates the targeting and volume decisions to the publisher and ties the compensation to an output measure: the number of clicks generated, $\operatorname { N } ( x , s \mid \tau )$ As in Equation (1), we define $\mathrm { N } ( x , s \mid \tau )$ for a particular realization of $T , \tau$ as

$$
\mathrm{N} (x, s \mid \tau) = \left\{ \begin{array}{l l} \alpha s x & \text {if} s \leq \tau , \\ (\alpha \tau + \beta (s - \tau)) x & \text {otherwise}. \end{array} \right.\tag{2}
$$

In (2), the propensity of consumers in the target segment and nontarget segment to click on the ad copy is assumed to be  and $\beta ,$ respectively. We note that both the number of clicks and the advertiser’s revenue depend on the number of impressions. In Figure 3, the game unfolds in the following timeline of events.

In the first stage, the CPC contract, which specifies the price per click (), is agreed upon. In stage 2, the target market uncertainty is realized. The publisher learns this realization and then decides on the intensity x() and the spread $s ( \tau )$ and delivers the campaign in stage 3. In stage 4, the advertiser pays price per click times the total number of clicks generated after the campaign. Finally in stage 5, the advertiser obtains the value generated from the campaign. We can write the advertiser’s optimization problem in the CPC model as

$$
\mathrm{P} _ {\text { CPC }}: \max _ {\rho} \mathrm{E} \left[ \Pi^ {A} (x (\mathrm{T}), s (\mathrm{T}) \mid \mathrm{T}) - \rho \mathrm{N} (x (\mathrm{T}), s (\mathrm{T}) \mid \mathrm{T}) \right]
$$

subject to

$$
\frac {\operatorname{E} [ \rho \mathrm{N} (x (\mathrm{T}) , s (\mathrm{T}) \mid \mathrm{T}) - \bar {C} (x (\mathrm{T}) , s (\mathrm{T})) ]}{\operatorname{E} [ x (\mathrm{T}) s (\mathrm{T}) ]} \geq u,\tag{IR-2}
$$

$$
x (\mathrm{T}), s (\mathrm{T}) \in \underset {\hat {x} (\mathrm{T}), \hat {s} (\mathrm{T})} {\arg \max} \left\{\rho \mathrm{N} \bigl (\hat {x} (\mathrm{T}), \hat {s} (\mathrm{T}) \mid \mathrm{T} \bigr) - \mathrm{C} (\hat {x} (\mathrm{T}), \hat {s} (\mathrm{T})) \right\},\tag{IC-1}
$$

$$
\rho \beta \leq \underline {{k}}, \quad \bar {k} \leq \rho \alpha .\tag{IC-2}
$$

In $\Gamma _ { \mathrm { C P C } } ,$ the advertiser’s decision variable is price per click $( \rho ) ;$ the publisher’s decision variables are the campaign intensity 4x5 and the campaign spread level 4s5. The advertiser’s objective function is the expectation of the revenue function defined in (1) minus the price per click times the expected number of clicks defined in (2). (IR-2) is the individual rationality constraint that ensures that even the publisher with the highest cost $( k = \bar { k } )$ is guaranteed his reservation utility per impression u.

Note that the reservation utility per impression in (IR-2) is the same as that in the CPM model because u represents the reservation utility of displaying an advertiser’s ad copy on the website. The issue of how the publisher is compensated is different from what is displayed. In both the CPM and the CPC models, the same ad copy is displayed. As noted above, the parameter u represents the opportunity cost to the publisher of doing so. In the CPM model the publisher gets compensated for merely exposing the ad copy to a visitor, and in the CPC model compensation results only if the visitor clicks on the ad copy. However, it is possible that the competition for ad copy/advertising space may depend on the pricing model that is adopted. In this case, the difference in the reservation utilities across the two models will also affect the choice of the appropriate pricing model. We demonstrate this formally in an extension where the reservation utility per impression is different across the two pricing models.<sup>9</sup>

The second constraint (IC-1) requires that the publisher with cost parameter, k, chooses the intensity x and s to maximize his payoff with the knowledge of the true realization of $T = \tau$ . Recall that because k is not known to the advertiser the price per click is set given the recognition that a publisher with cost parameter k will set the campaign decisions to maximize his profits.

The last set of constraints (IC-2) corresponds to the information selection constraints, which induce the publisher to use the available boundary information $\left( \mathrm { e . g . } , s = \tau \right)$ . There are two cases in which the publisher may not make informed decisions: if the advertiser pays on average more than <sup>¯</sup>k per impression $( \rho \beta > \bar { k } )$ in the nontarget segment, the publisher will not use the boundary information and will instead display ads on the whole website $( s = 1 )$ . Therefore, (IC-2) guarantees that for any realization of ${ \tilde { k } } ,$ the publisher loses money in the nontarget segment $( \rho \beta \leq k )$ . Likewise, if the advertiser pays on average less than $\bar { k } \ \mathrm { p e r }$ impression $( \rho \alpha < \bar { k } )$ in the target segment, then the publisher will not use the information by declining the contract $( s = 0 )$ . As expected, this implies that the propensity to click in the nontarget segment has to be less than the one in the target market $( \beta < \alpha )$ for the publisher to engage in targeting. This condition reflects the belief that consumers’ propensity to click tends to be higher in the target segment than the nontarget segment. This constraint has implications on ad copy design. The advertiser has to design ads that appeal to the target segment. This is well known in the industry: “If I have a message that says ‘Free \$1 Million’ if you click here, I may get lots of clicks but so what? What matters is who these people are 0 0 0 0 Not all clicks are equal” (Sheiner 2001). With these assumptions in place, we are now ready to characterize the equilibrium decisions in the CPM and CPC models.

## 4. Results and Comparison of the Models

## 4.1. Analysis of the CPM Model

We first turn our attention to the solution of $\mathrm { P _ { C P M } }$ We characterize this solution for a general distribution F of the target segment boundary T , and then we present the solution when F is a uniform distribution. As noted earlier, the participation constraint (IR-1) is binding. We can solve for the total payment pxs using (IR-1) and calculate the advertiser’s payoff function by subtracting the total payment from the revenue function (1). Let $\Omega ( x , s \mid \tau )$ be the advertiser’s payoff function; then

Figure 3 Timeline of Events in the CPC Model  
![](/api/attachments/Z77M45NR/fulltext/images/ab52aa5747390f0517abf948ea97517e913966cc894b4c839473dd1c00212fd4.jpg)

$$
\begin{array}{l} \Omega (x, s \mid \tau) \\ = \left\{ \begin{array}{l l} \Omega^ {+} (x, s \mid \tau) = ((a - u - \bar {k}) \tau \\ \quad + (b - u - \bar {k}) (s - \tau)) x - x ^ {2} & \text {if s > \tau ,} \\ \Omega^ {-} (x, s \mid \tau) = (a - u - \bar {k}) s x - x ^ {2} & \text {if s\leq\tau .} \end{array} \right. \end{array}\tag{3}
$$

Using (3), we can write the advertiser’s objective function in $\mathrm { P _ { C P M } }$ as

$$
\begin{array}{c} \max _ {s, x} \Omega (x, s) = \operatorname{E} [ \Omega (x, s \mid \mathrm{T}) ] \\ = \int_ {c} ^ {s} \Omega^ {+} d F + \int_ {s} ^ {d} \Omega^ {-} d F. \end{array}\tag{4}
$$

Proposition 1 presents the solution to $\mathrm { P _ { C P M } }$ with the assumption that F ∼ Uniform $( c , d )$ . Following Proposition 1, the spread of the campaign is increasing in the exposure value in either segment (a or b) but decreasing in the outside options of the publisher (u) and delivery costs (<sup>¯</sup>k5.

Proposition 1. <sub>If</sub> $u \leq a - \bar { k }$ and the target segment boundary has a uniform distribution $F \sim$ Uniform(c1 d5, the solution to $P _ { \mathrm { C P M } }$ is given by

$$
\begin{array}{c} {s ^ {*} = c + \frac {(a - u - \bar {k}) (d - c)}{a - b},} \\ {x ^ {*} = \frac {(a - u - \bar {k}) (s ^ {*} + c)}{4}, \quad a n d \quad p ^ {*} = u + \bar {k} + \frac {x ^ {*}}{s ^ {*}}.} \end{array}\tag{5}
$$

The expected payoff of the advertiser is

$$
\Omega^ {A} (\mathrm{CPM}) = (x ^ {*}) ^ {2}.\tag{6}
$$

The expected payoff of the publisher is

$$
\Omega^ {P} (\mathrm{CPM}) = \left(\frac {\bar {k} - \underline {{k}}}{2} + u\right) x ^ {*} s ^ {*}.\tag{7}
$$

<sup>Proof.</sup> See Appendix A in the online supplement. <sup></sup>

Analysis of the equilibrium strategies and their sensitivity to market parameters offer insights on the interplay between the choice of campaign decisions and uncertainty in the target segment boundary. In Corollary 1, we identify the effect of increasing the target segment uncertainty on the payoffs.

<sup>Corollary</sup> <sup>1.</sup> As the target segment uncertainty $( \sim d - c )$ increases while preserving the mean, in the CPM model both the advertiser and the publisher are worse off if $a + b < 2 ( u + \bar { k } )$

<sup>Proof.</sup> See Appendix A in the online supplement. <sup></sup>

The negative impact of higher uncertainty on the advertiser and the publisher in the CPM model is not surprising. This result is driven by the advertiser’s decision problem. If the advertiser displays impressions on the nontarget segment pages by choosing a high spread level, $s ,$ she displays ads on pages where the returns are not as high as that from displaying impressions on the target segment pages. In contrast, if the advertiser chooses a small $s ,$ then she may miss a portion of the target segment. The advertiser’s choice of the spread level and the advertising intensity depends on the relative magnitude of these costs. As target segment uncertainty increases and the mean remains the same $( c \to c - { \bar { \delta } }$ and $d $ $d + \delta )$ , these costs increase. When the exposure value of advertisements to the target segment (a) is not too large, the benefit of advertising to the target segment is not large enough to offset the costs of advertising to the nontarget segment. Consequently, the advertiser reduces both the spread and advertising intensity. Because the publisher’s payoff is also dependent on the advertiser’s volume and targeting decisions, this reduction makes both the advertiser and the publisher worse off.

Therefore, we show that when the advertiser’s information quality deteriorates, this will make her cautious by not advertising to a broad audience with high volume. This, in turn, makes both parties worse off. Next, we analyze the solution of the CPC model.

## 4.2. Analysis of the CPC Model

Recall that in the CPC model the advertiser sets the price per click and delegates the decisions of the campaign decisions to the publisher. We analyze $\mathrm { P _ { C P C } }$ by first solving the publisher’s problem for any given price per click $\rho$ and then solving the advertiser’s problem taking into account the publisher’s optimal response. The publisher’s decision problem after the contract is signed and  is realized is

$$
\begin{array}{l} \max _ {x, s} \left\{\rho \mathrm{N} (x, s \mid \tau) - \mathrm{C} (x, s) \right\} \\ = \left\{ \begin{array}{l l} ((\rho \alpha - k) \tau + (\rho \beta - k) (s - \tau)) x - x ^ {2} & \text { if } s > \tau , \\ (\rho \alpha - k) s x - x ^ {2} & \text { if } s \leq \tau . \end{array} \right. \end{array}\tag{8}
$$

The information selection constraints (IC-2) together with (8) imply that the publisher’s optimal choice of spread $s _ { P } ^ { * } = \tau$ . Then, the solution to (8) is

$$
s _ {P} ^ {*} = \tau \quad \text { and } \quad x _ {P} ^ {*} = \frac {(\rho \alpha - k) \tau}{2}.\tag{9}
$$

Substituting $s _ { P } ^ { * } ( = T )$ and $x _ { P } ^ { * } ,$ , and then multiplying (IR-2) with $\mathrm { E } [ u x _ { P } ^ { * } \mathrm { T } ]$ and rearranging, the advertiser’s problem $\mathrm { P _ { C P C } }$ becomes

$$
\max _ {\rho} \mathrm{E} \left[ \Pi^ {A} (x _ {P} ^ {*}, \mathrm{T} \mid \mathrm{T}) - \rho \mathrm{N} (x _ {P} ^ {*}, \mathrm{T} \mid \mathrm{T}) \right]\tag{10}
$$

subject to

$$
\mathrm{E} \big [ \rho \mathrm{N} (x _ {P} ^ {*}, \mathrm{T} | \mathrm{T}) - \bar {\mathrm{C}} (x _ {P} ^ {*}, \mathrm{T}) - u x _ {P} ^ {*} \mathrm{T} \big ] \geq 0.\tag{IR-2}
$$

We present the solution to $\mathrm { P _ { C P C } }$ in Proposition 2.

<sup>Proposition</sup> <sup>2.</sup> We provide the solution to $\mathrm { P _ { C P C } }$ in two cases depending on whether the publisher’s individual rationality constraint (IR-2) binds in equilibrium.

(a) If $a > 2 ( u + \bar { k } + \sqrt { u ^ { 2 } + ( \bar { k } - \underline { { { k } } } ) ( 3 u + \bar { k } - \underline { { { k } } } ) / 3 } ) \ - $ $( \bar { k } + \underline { { k } } ) / 2$ so that (IR-2) does not bind in equilibrium, then the advertiser sets $\rho ^ { * } = ( 2 a + \bar { k } + \underline { { k } } ) / 4 \alpha .$ . And, the publisher’s choice of campaign decisions is $s _ { P } ^ { * } = \tau$ or $x _ { P } ^ { * } = ( a +$ $( \bar { k } + \underline { { k } } ) / 2 - 2 k ) \tau / 4$ . The resulting expected payoffs are

$$
\Omega^ {A} (\mathrm{CPC}) = \frac {1}{2 4} (d ^ {2} + d c + c ^ {2}) (a - (\bar {k} + \underline {{k}}) / 2) ^ {2} a n d
$$

$$
\begin{array}{l} \Omega^ {P} (\mathrm{CPC}) = \frac {1}{4 8} (d ^ {2} + d c + c ^ {2}) \\ \cdot \left(a ^ {2} - a (\bar {k} + \underline {{k}}) + \frac {1 . 7 5 (\bar {k} + \underline {{k}}) ^ {2} - 4 \bar {k} \underline {{k}}}{3}\right). \end{array}\tag{11}
$$

(b) If $u + \bar { k } + \sqrt { u ^ { 2 } + ( \bar { k } - \underline { { k } } ) ( 3 u + \bar { k } - \underline { { k } } ) / 3 } \le a \le 2 ( u + \bar { k }$ $+ \sqrt { u ^ { 2 } + ( \bar { k } - \underline { { k } } ) ( 3 u + \bar { k } - \underline { { k } } ) / 3 ) - ( \bar { k } + \underline { { k } } ) / 2 }$ so that the advertiser participates in the contract and (IR-2) binds in equilibrium, then the advertiser sets $\rho ^ { u * } = ( u + \bar { k } +$ $\sqrt { u ^ { 2 } + ( \bar { k } - \underline { { k } } ) ( 3 u + \bar { k } - \underline { { k } } ) } / 3 ) / \alpha$ . The publisher’s choice of campaign decisions is $s _ { P } ^ { u ^ { * } } = \tau , x _ { P } ^ { u ^ { * } } = ( ( \rho ^ { u ^ { * } } \alpha - k ) \tau ) / 2$ . The resulting expected payoffs are

$$
\begin{array}{l} \Omega^ {A} (\mathrm{CPC} ^ {u}) = \frac {1}{6} (d ^ {2} + d c + c ^ {2}) (a - \rho^ {u ^ {*}} \alpha) (\rho^ {u ^ {*}} \alpha - (\bar {k} + \underline {{k}}) / 2) \\ a n d \end{array}
$$

$$
\begin{array}{l} \Omega^ {P} (\mathrm{CPC} ^ {u}) = \frac {1}{1 2} (d ^ {2} + d c + c ^ {2}) \\ \qquad \cdot \big [ (\rho^ {u ^ {*}} \alpha) ^ {2} - \rho^ {u ^ {*}} \alpha (\bar {k} + \underline {{k}}) + (\bar {k} ^ {2} + \bar {k} \underline {{k}} + \underline {{k}} ^ {2}) / 3 \big ]. \end{array}\tag{12}
$$

<sup>Proof.</sup> See Appendix A in the online supplement. <sup></sup>

A careful examination of Proposition 2, part (a), reveals interesting insights into the performancebased model. In the CPC model, the advertiser delegates campaign decisions to the publisher. The publisher, in turn, makes decisions with perfect information. However, the publisher chooses the advertising intensity x to maximize his payoff (8). Therefore, there is an incentive conflict between the publisher and the advertiser on the choice of x. The advertiser’s choice of the price per click $\rho ^ { * }$ in Proposition $^ { 2 , }$ part (a), tries to alleviate this conflict.

On the other hand, in Proposition 2, part (b), the price is determined by the market conditions (the publisher’s outside option), (IR-2), and so the incentive alignment role of the price per click $\rho ^ { u ^ { * } }$ is different. Whereas the publisher’s choice of campaign intensity increases with $u ,$ the advertiser would reduce intensity as u gets larger, if she has control. The rationale for this conflict is that the price per click $\rho ^ { u ^ { * } }$ is increasing in u. Because the publisher already advertises to all consumers in the target segment, the only way to increase his payoff is by increasing advertising intensity. The intuition for why the advertiser would prefer to reduce the advertising intensity is simply a cost argument; as the clicks get more expensive, the advertiser would want to lower intensity. Therefore the degree of misalignment between the advertiser and the publisher in the CPC model increases with u. We will highlight this phenomenon when we compare the pricing models.

In Proposition 2, the advertiser factors in the consumers’ propensity to click in setting the price per click. Note that whereas both $\rho ^ { * }$ and $\rho ^ { u ^ { * } }$ depend on the propensity to click $\alpha , \rho ^ { * } \alpha$ and $\rho ^ { u ^ { * } }$  do not. Said differently, the price per click is set so that the effective CPM (propensity to click times price per click) is independent of . To see this, suppose $a = 1 . 5$ and $\bar { k } + \underline { { k } } = \bar { 1 }$ . Consider two cases: if $\alpha = 0 . 2 5 ,$ then $\rho ^ { * } = 4 ;$ and if $\alpha = 0 . 5 ,$ , then $\rho ^ { * } = 2$ . But in each case, the effective CPM remains the same: $\rho ^ { * } \alpha = 1$ . This implies that the advertiser should determine price offers based on effective CPM just as the publisher should decide whether to accept or reject campaigns based on reservation utility per impression. A prominent industry expert, Kevin Lee, has been a strong advocate of this finding: “To succeed with Google, marketers must run their campaigns using CPM-like strategies 0 0 0 ” (Lee 2002).

Because the publisher acquires target segment information, uncertainty plays a different role in $\mathrm { P _ { C P C } }$ We study the impact of increasing uncertainty on the advertiser and the publisher in Corollary 2.

<sup>Corollary</sup> <sup>2.</sup> As the target segment uncertainty $( \sim d - c )$ increases while preserving the mean, both the advertiser and the publisher are better off using the CPC model.

<sup>Proof.</sup> See Appendix A in the online supplement. <sup></sup>

Recall that the target segment boundary T is a random variable with support [c1 d]. As (d − c5 increases the range of values that T can take (i.e., the variance of T) increases. In Corollary 1, we noted that as $( d - c )$ increases the advertiser lowers both the spread and intensity in the CPM model resulting in reduced profits for both the advertiser and the publisher. Under the CPC model the publisher acquires the target segment information and makes both the spread and intensity decisions with perfect information.<sup>10</sup> Now consider the value of making decisions with perfect information vis-à-vis the CPM model. If target segment uncertainty is low, i.e., $( d - c )$ is small, then the possibility of over or under targeting in the CPM model is low. However, as target segment uncertainty increases, the possibility of over- or undertargeting increases in the CPM model. In contrast, regardless of the level of uncertainty, the publisher in the CPC model makes decisions with information of the realized value of the target segment boundary, T . Hence, information is more valuable when uncertainty (d −c5 is higher, and the benefits to the advertiser and the publisher for a given mean increase with uncertainty. Thus, when all else remains the same, both the advertiser and the publisher are more likely to prefer the CPC model to the CPM model under higher uncertainty because the value of suitably adjusting the campaign decisions is greater when the range of $( d - c )$ or uncertainty is higher.

## 4.3. Comparison of the Models

Recall that in the CPM model the advertiser does not delegate campaign decisions to the publisher. Instead she sets the CPM rate, the advertising intensity $x ,$ and the spread s while remaining uncertain about the true realization of the target segment boundary T . The advertiser’s profits would be higher if the realization of T were known with certainty. In contrast, in the CPC model the advertiser simply sets the CPC rate  and delegates the campaign decisions to the publisher. The publisher in turn acquires the information on the target segment boundary before making the campaign decisions. In this case, even though the publisher uses better information, the advertiser’s payoff need not be as high as her payoff if the pricing model was CPM because the publisher makes decisions to maximize his payoff not the advertiser’s payoff. Consequently, the choice of the pricing model for the advertiser boils down to the trade-off between benefits of delegating and having the publisher make better informed decisions versus the cost of losing control over the campaign decisions.

This trade-off is consistent with observations in the trade press. As noted earlier, Yahoo! has moved to a search engine advertising model where the position of the ads will be determined by Yahoo! This change resulted in less control by advertisers and better targeting provided by the Yahoo! algorithm. From the advertisers’ perspective delegating the campaign decisions to the publisher, for instance the position of the banners on the publisher’s site (s in our model) can result in better targeting. The following quote attests to this finding: “Position control and the ability to predict position for a given search is moving from difficult to impossible. With loss in position [control], searchers are getting more relevance” (Lee 2005b). Because position of an ad copy is an important decision variable that determines number of impressions and clicks, this move by Yahoo! underscores the institutional feature of CPC that the publisher should make campaign decisions with better information.

To understand the determinants of pricing model preferences, we identify market conditions under which the advertiser and the publisher prefer the CPM model to the CPC model, or vice versa. We use the difference between expected payoffs in different models for the corresponding ranges in Propositions 2(a) and 2(b). Figure 4 illustrates the possible combinations of preferences for specific values of the parameters (u = 3, b = −5, <sup>¯</sup>k = 1, k = 0081, c = 0049−, $d = 0 . 5 1 + \sigma )$ . The y axis is a measure of variance of the target segment boundary $T ;$ we vary the range of T with  so that $T \sim \mathrm { U } [ 0 . 4 \dot { 9 } - \sigma , 0 . 5 1 + \dot { \sigma } ]$ . The graph shows the value of  on the y axis and the exposure value in the target segment a per impression on the x axis. For $a > 1 3 . 3$ , Propositions 1 and 2(a) are used for comparison, and for $7 . 1 \leq a \leq 1 3 . 3 ,$ , Propositions 1 and 2(b) are used for comparison. In Figure 4, Regions I and II denote market conditions in which the publisher prefers $\mathrm { P _ { C P M } }$ to $\mathrm { P _ { C P C } }$ (III and IV are the publisher’s $\mathrm { P _ { C P C } }$ preference regions); Regions II and III denote market conditions in which the advertiser prefers $\mathrm { P _ { C P M } }$ to $\mathrm { P _ { C P C } }$ (I and IV are the advertiser’s $\mathrm { P _ { C P C } }$ preference regions). The respective boundaries in the figure represent the curve along which the publisher (or the advertiser) is indifferent between the two pricing models. Notice that in Region I, the advertiser prefers $\mathrm { P _ { C P C } }$ to $\mathrm { P _ { C P M } }$ and the publisher prefers $\mathrm { P _ { C P M } }$ to $\mathrm { P _ { C P C } } .$ . This is consistent with the tension that is often discussed in the trade press.

Figure 4 The Boundary Between the CPM and the CPC Models for the Advertiser and the Publisher  
![](/api/attachments/Z77M45NR/fulltext/images/d5d9dd5bdbcbac56489d62ea894d4311039d863890836f26e9792875d53b3990.jpg)

<table><tr><td>Region I (expected tension)</td><td></td><td>Advertiser prefers CPC and publisher prefers CPM</td></tr><tr><td>Region II (consensus with CPM)</td><td></td><td>Advertiser prefers CPM and publisher prefers CPM</td></tr><tr><td>Region III (unexpected tension)</td><td></td><td>Advertiser prefers CPM and publisher prefers CPC</td></tr><tr><td>Region IV (consensus with CPC)</td><td></td><td>Advertiser prefers CPC and publisher prefers CPC</td></tr></table>

Interestingly, there is a (rather large) region in the parameter space (Region III) where the advertiser prefers $\mathrm { P _ { C P M } }$ and the publisher prefers $\mathrm { P _ { C P C } }$ . This finding is counter to the prevailing wisdom; i.e., the principal prefers an input-based contract and the agent prefers to be held accountable with a performancebased contract. Further, contrary to the academic literature that shows delegation is preferred by a principal when the agent is better informed (Lal 1986, Melumad and Reichelstein 1987), we show that this may not always be true; i.e., advertiser’s profits in $\mathrm { P _ { C P C } }$ do not always dominate her profits from $\mathrm { P _ { C P M } } .$ . In our context, benefits of using better information in making decisions may be less than the value lost because of delegating decisions to the publisher. Moreover, prior literature has not focused on the agent’s (publisher’s) preference over a pricing model. To help explain the intuition behind our findings, we identify four factors that impact the pricing model preference of the advertiser and the publisher: (a) uncertainty over the target segment boundaries (uncertainty effect), (b) the value of advertising to the target segment (exposure-value effect), (c) the cost of mistargeting ads to consumers in the nontarget segment (mistargeting effect), and (d) the difference in the alignment of incentives of the advertiser and the publisher (alignment effect). These factors are interrelated. The interplay of the factors may make an effect inconsequential in one region and dominant in another. For example, a strong exposure-value or alignment effect may diminish the impact of the uncertainty effect on preferences. We discuss the impact of these effects in turn below.

4.3.1. Uncertainty Effect. Corollaries 1 and 2 characterize the effect of uncertainty over the target segment boundaries in the CPM and CPC models.

Corollary 1 states that uncertainty over the realization of the target segment boundaries has a negative effect on both the advertiser’s and publisher’s payoffs in $\mathrm { P _ { C P M } }$ . Because decisions are made with better knowledge of the target segment boundary in $\Gamma _ { \mathrm { C P C } } ,$ advertising volume can be decreased or increased depending on the level of uncertainty. As a result, losses will be limited and gains will be higher. Uncertainty, thus, has a positive effect on payoffs in Corollary 2. In other words, the model predicts that, ceteris paribus, both advertisers and publishers are more likely to prefer the CPC model under high uncertainty. Therefore, uncertainty effect favors the CPC model for both the advertiser and the publisher. Figure 4 clearly illustrates this finding. Note that, as the variance ( 5 increases, both parties prefer the CPC model: Region IV in Figure 4.

4.3.2. Exposure-Value Effect. This effect moderates the uncertainty effect for the advertiser. Although the uncertainty effect unambiguously favors the use of the CPC model for both parties, its strength depends on the exposure value in the target segment (a5. Inspection of the optimal spread choice in CPM s<sup>∗</sup> in (5) reveals the direction of this effect. As exposure value goes to infinity, $s ^ { * }$ goes to the upper limit of the target segment boundary distribution d $( s ^ { * } \to d { \mathrm { a s } } a \to \infty )$ . This implies that the value of delegating decisions to the publisher—so that he can make better informed decisions—diminishes as exposure value increases. In this case, control of campaign decisions is more critical than value of information for the advertiser. In contrast, the publisher’s desire to control campaign decisions increases with the exposure value because, as the exposure value increases, the advertiser would choose increasingly higher campaign intensities (x) than the level the publisher would prefer. Therefore, exposure-value effect favors the CPM model for the advertiser and the CPC model for the publisher.

Figure 5 The Boundary Between the CPM and CPC Models for the Advertiser and the Publisher When b Is Increased from b = −5 to $b = 0 . 8$  
![](/api/attachments/Z77M45NR/fulltext/images/824e9f47e0394e0eeeba390415121bb611fc6efbfa0de9d1069f96439a2583c7.jpg)

4.3.3. Mistargeting Effect. This effect also moderates the uncertainty effect for both the advertiser and the publisher. Note that the price per impression and effective CPM in CPC are bounded and cannot be less than the maximum ad-serving cost (<sup>¯</sup>k5 plus the publisher’s outside option u. When the value of advertising to consumers in the nontarget segment b is significantly lower than $\bar { k } \ \mathrm { o r } \ u ,$ then advertising in this segment is simply dissipative. Although we use negative values for b in some of our simulations, as illustrated in the right panel in Figure 5, our findings hold for positive values as well. The sign of b is not critical. The mistargeting effect depends on how low b is relative to <sup>¯</sup>k. Said differently, when mistargeting ads to consumers in the nontarget segment is sufficiently costly, then the advertiser would like to ensure that the campaign decisions are set such that mistargeting is minimized. Under these conditions the value of information on the target segment boundaries is high so that the advertiser would prefer to delegate the campaign decisions to the publisher. Note that in the CPM model $s ^ { * } \to c \mathrm { \ a s \ } \bar { k } - \bar { b } \to$ $\infty ,$ which essentially means that when the value of advertising to consumers in the nontarget segment is very low compared to the ad-serving cost (<sup>¯</sup>k5. The advertiser, therefore, chooses a spread so that only the consumers in the target segment see the banners $( s ^ { * } \to c )$ . This very conservative decision affects both the advertiser and the publisher’s profits adversely in the CPM model. Under the CPC model the publisher makes decisions with complete information on the target segment boundaries, which result in higher payoffs to both vis-à-vis the CPM model. A similar reasoning applies to $\bar { k }$ and u because $s ^ { * } \to c \mathrm { ~ a s ~ } \bar { k } +$ $u  a ,$ , making CPC the preferred pricing model as <sup>¯</sup>k increases. Figure 5 shows the expansion of CPM regions as the mistargeting effect is decreased (b is increased from −5 to 0.8). The mistargeting effect essentially increases the value of information and favors the CPC model for both the advertiser and the publisher.

![](/api/attachments/Z77M45NR/fulltext/images/be0f192783da8f130e027f367784c9e6a30fbf05f6135284533c1bd0eddc1b5c.jpg)

4.3.4. Alignment Effect. Note that in the CPC model the equilibrium solution depends upon market conditions. Proposition 2(a) characterizes the solution when the exposure value a is sufficiently high. In this case, the participation constraint of the publisher (IR-2) is slack. In contrast, when the exposure value is not too large, the solution is characterized as in Proposition 2(b), and in this case the participation constraint (IR-2) binds in equilibrium. Recall that in the CPC model the advertiser delegates decisions to the publisher who sets the intensity and spread to maximize his payoff, not the advertiser’s payoff. Consequently, the campaign decisions will never be perfectly aligned with what the advertiser may desire. This misalignment of incentives helps explain the unexpected tension in Region III in Figures 4 and 5.

We use a numerical illustration to highlight the role of this effect. For the parameter values used to plot Figure 4 $( u = 3 , b = - \bar { 5 } , \bar { k } = 1 , \underline { { k } } = 0 . 8 1$ , and $\sigma =$ $\bar { 0 } . 0 5 , c \bar { = } 0 . 4 4 , d = 0 . 5 6 )$ , the condition in Proposition 2(a) is satisfied for exposure value $a > 1 3 . 3$ , and the condition in Proposition 2(b) is satisfied for $7 . 1 < a <$ 1303. In Table 2, we vary the exposure value a. When the exposure value is sufficiently small, $a = 8 ,$ the publisher’s participation constraint determines the price per click. The publisher’s CPC choice of intensity is distorted upward vis-à-vis that which would be set by the advertiser in the CPM model (compare $x =$ 0.92 in CPM with E[x7 = 1055 in CPC). The reason is, although the exposure value is low, the advertiser has to pay a high enough price per click to guarantee publisher participation (compare 5.92 in CPM with effective CPM () 7.10 in CPC), resulting in an expected advertiser CPM payoff of 0.84 and publisher CPM payoff of 1.35. The respective payoffs in the CPC model are 0.70 (advertiser is worse off) and 2.41 (publisher is better off). This explains Region III when exposure value is sufficiently small.

Table 2 Numerical Illustration of the Alignment Effect

<table><tr><td>Exposure value</td><td>Model</td><td>x for CPM E[x] for CPC</td><td>p for CPM  $\rho\alpha$  for CPC</td><td>Advertiser profit  $\Omega^A$ </td><td>Publisher profit  $\Omega^P$ </td></tr><tr><td rowspan="2">a=8</td><td>CPM</td><td>0.92</td><td>5.92</td><td>0.84</td><td>1.35</td></tr><tr><td>CPC</td><td>1.55</td><td>7.10</td><td>0.70</td><td>2.41</td></tr><tr><td rowspan="2">a=40</td><td>CPM</td><td>8.78</td><td>20.39</td><td>77.2</td><td>14.57</td></tr><tr><td>CPC</td><td>4.89</td><td>20.45</td><td>47.99</td><td>24.0</td></tr></table>

Figure 6 The Boundary Between the CPM and the CPC Models for the Advertiser and the Publisher When U Is Increased from u = 3 to $u = 5$  
![](/api/attachments/Z77M45NR/fulltext/images/90359e4f0865d0c59796bbde1829d34dcc872e5a420d1ea579df036e6469fa19.jpg)

![](/api/attachments/Z77M45NR/fulltext/images/5fb7d5928c62eff0c179d12cd0320eeb8e772c7a342f2111374d570e6480a039.jpg)

When exposure value is large, say, $a = 4 0$ , the participation constraint of the publisher is slack. The distortion in the publisher’s CPC choice of intensity is now in the opposite direction. Given the high exposure value, the advertiser would prefer high intensity. Thus, the effective CPM in CPC (20.45) exceeds the CPM price (20.39) because the advertiser ties compensation to exposure value in CPC to induce higher advertising intensity. As a result, the publisher earns 50% of what the advertiser earns (24 versus 47.99) and 65% more than his would-be CPM payoff (14.57). Yet the publisher’s expected CPC choice of intensity $( \operatorname { E } [ x ] = 4 . 8 9 )$ still falls short of what the advertiser would like $( x = 8 . 7 8 )$ . Consequently, the advertiser earns 38% less than her would-be CPM payoff (77.16). Therefore, we obtain the following result. The alignment effect becomes a dominant factor when the publisher’s outside option (u) is sufficiently higher or smaller than the exposure value (a). If the difference between u and a is sufficiently large (negative or positive), the alignment effect favors the CPM model for the advertiser and the CPC model for the publisher.

4.3.5. Regions I (Expected Tension) and II (Consensus with CPM). In Figures 4 and 5, when uncertainty over the target segment boundaries is low, both the advertiser and the publisher prefer the CPM model to the CPC model (CPM provides consensus in Region II). The intuition for this follows directly from Corollaries 1 and 2. For exposure values in the neighborhood of 10, the uncertainty effect is the dominant effect for the advertiser, and as a increases, the uncertainty effect is moderated by the exposurevalue effect. In other words, for higher values of $a ,$ uncertainty has to be higher for the advertiser to prefer the CPC model to the CPM model. The region where the advertiser prefers the CPC model and the publisher prefers the CPM model (Region I) depends upon the net result of the uncertainty, exposure-value, and the alignment effects. Because the alignment and exposure-value effects are dominated by the uncertainty effect for the advertiser, she prefers the CPC model in Region I.

The alignment effect explains why the publisher prefers the CPM model to the CPC model in Regions I and II. Because CPM and effective CPM (in CPC) prices are similar in these regions, the campaign decisions become critical for the publisher’s preference. The advertiser’s campaign decisions in the CPM model are more beneficial to the publisher than the decisions the publisher would make in the CPC model. The rationale is, although the advertiser would choose x and s based on exposure value a, the publisher in the CPC model would base them only on a fraction of the exposure value because of the optimal effective CPM $\bar { ( \rho ^ { * } \alpha = ( a + ( \bar { k } + \underline { { k } } ) / 2 ) / 2 ) }$ . That is, the publisher would not fully internalize the exposure value in making her decisions. Figure 6 shows that a higher outside-option u enlarges the publisher’s CPM regions, because CPM price always depends on u but effective CPM does not.

## 5. Alternative Specifications of the CPM and CPC Models

## 5.1. Pricing Model Choice with Price Menus 5.1. Pricing Model Choice with Price Menus

In our base model, we analyze the setting where the prices in both the CPM and the CPC models are determined with a contract offered by the advertiser who recognizes that the publisher has outside options. It is worth noting that the base setup approximates oneon-one negotiations in which each party is informed about the value to the other of entering into the agreement. Specifically, the advertiser recognizes the publisher’s outside options, and the publisher recognizes the value of advertising. Consequently, the equilibrium characterized in the base model depends upon the characteristics of the participating agents making the CPM and CPC prices specific to the target market characteristics of the advertiser and the publisher. In many cases, however, the publisher may have a standard rate card, with CPM and CPC rates that are independent of the specific advertiser’s characteristics. Instead, the rates may only depend on the intensity (x) and spread of the advertising campaign (s).

In this extension, we develop a model in which the publisher charges a price that depends only on the spread and intensity of the campaign. Specifically, the price menu assumes the following functional form:

$$
\text { CPM   price: } \quad p (x, s) = \lambda \frac {x}{s} + \mu ;\tag{13}
$$

$$
\mathrm{CPCprice:} \quad \rho (x, s) = \frac {\gamma}{\alpha} p (x, s).
$$

Figure 7

We maintain the rest of the assumptions of the base model in §§3.1 and 3.2. The parameters $\lambda , \ \mu ,$ and  are exogenous. This pricing function has an intuitive form: when the spread (s5 is high (targeting is less precise), the price is lower. In addition, when the number of unique impressions (x5 is high, the price is higher. The parameter $\gamma / \alpha$ captures the relative strength of CPC over CPM prices. Recall that  is the rate at which consumers in the target segment click on the ad copy. The functional form of the price per click has the desirable feature that when propensity to click is lower, the effective CPM does not change. Given the exogenous prices, the advertiser decides on spread (s) and intensity (x) in the CPM model, and the publisher makes these decisions in the CPC model. This setup allows us to examine the robustness of our findings by allowing the publisher to determine the price.<sup>11</sup> The details of this setup are in Appendix B in the online supplement. As in the base model we compare the profits of the advertiser and the publisher to identify market conditions in which they would prefer the CPM model to the CPC model, and vice versa. These findings are depicted in Figure 7.

Figure 7 shows the preference regions and the parameter values used in addition to the parameter values in Figure 4. Notably, comparison of Figures 7(a) and 7(b) with Figures 4 and 5 reveal that the two main results qualitatively hold: the four preference regions exist and CPC is more likely when there is high target market uncertainty (uncertainty effect). Moreover, low mistargeting effect (higher b) makes targeting less critical and thus expands the CPM consensus Region II (Figure 7). A slight difference is that CPM provides consensus when the target market exposure value a is high. In contrast, in Figure 4 the

The Boundary Between the CPM and the CPC Models with Price Menus for $b = - 5$ and $b = 0 . 8$  
![](/api/attachments/Z77M45NR/fulltext/images/cb49263dc2f802a658aa1adff6a8b497d054a44aea6f58362c8158ae87a698d7.jpg)

![](/api/attachments/Z77M45NR/fulltext/images/9098623675f9102cc0bfd7d2ec9c4141cd72916cd8ce358e69034a121c55bfa4.jpg)  
publisher prefers CPC for high levels of a (Regions III and IV). This difference arises because unlike in the base model, the prices in this extension do not explicitly depend on the individual advertiser’s parameters. In particular, price per click is not tied to exposure value.

## 5.2. Partial Delegation in the CPC Model

In our base model the advertiser delegates both the spread and intensity decisions to the publisher. As noted earlier, although our assumptions in the base model regarding the decision variables of the advertiser and the publisher are consistent with institutional practice, in this extension we consider the case in which the advertiser delegates the targeting decision to the publisher but retains control of the intensity decision in the CPC model. In this setting, the advertiser can induce the publisher to acquire the target segment boundary information and also control the intensity decision. Appendix C in the online supplement presents the analysis of this alternative model, $\mathrm { P _ { C P C - A } } ^ { \mathrm { } }$ . Corollary 3 summarizes the fundamental insights.<sup>12</sup>

<sup>Corollary</sup> <sup>3.</sup> The advertiser always prefers $P _ { \mathrm { C P C - A } }$ to $P _ { \mathrm { C P M } } .$ . Moreover, the advertiser may or may not prefer

Figure 8 The Boundary Between the CPM with a Strategic Publisher and the CPC Models for the Advertiser and the Publisher  
![](/api/attachments/Z77M45NR/fulltext/images/d399df3c6c998315740ece9f12268590ce43b79d2f8d0c3c4c9ef5e8c6c5aaf1.jpg)

$P _ { \mathrm { C P C - A } }$ to $P _ { \mathrm { C P C } }$ . In addition, the publisher may or may not prefer $P _ { \mathrm { C P C - A } }$ to either $P _ { \mathrm { C P M } }$ or $P _ { \mathrm { C P C } }$

<sup>Proof.</sup> See Appendix C in the online supplement. <sup></sup>

In this setup, not surprisingly the advertiser prefers the CPC model with partial delegation to the CPM model because she retains the control of the intensity decision and also obtains the benefits of better information. However, compared to our base CPC model, the CPC model with partial delegation does not utilize the target segment information in choosing campaign intensity. Therefore, there is still a region where the advertiser may delegate the intensity decision to the publisher. Similarly, the publisher may opt for the CPM model over the CPC model with partial delegation because the advertiser may choose a higher spread and intensity in the CPM model to reduce the possibility of overtargeting. In general, we expect that the publisher would prefer making all the campaign decisions. Surprisingly, there is a region where the publisher would prefer the CPC model with partial delegation to the CPC model. In the base CPC model, the publisher is hurt as a result of the advertiser’s strategic reaction to the publisher’s choice of intensity. However, partial delegation reduces this strategic burden by having the advertiser set the intensity. Thus, in some regions, the publisher is better off with partial delegation.

## 5.3. The CPM Model with the Publisher Choosing Intensity and Spread

In this alternative specification, we investigate the CPM model where certain decisions are made by the publisher. This specification will shed light on whether the results of our base model are applicable to situations where the publisher has more control over the campaign decisions in the CPM model. In this model, the advertiser sets the price per impression p and the total number of impressions $M = x s ,$ leaving the publisher to decide on the campaign decisions x and s.

![](/api/attachments/Z77M45NR/fulltext/images/aa8e74b0c432f35e8d9c2abce00375cf61a24f8d6bf2b07958bfc3835957f3d2.jpg)

We provide the analysis of this model in Appendix D in the online supplement. In this setup, the publisher will choose x and s to maximize his payoff; in equilibrium $s ^ { * } = 1$ . In other words, the publisher will not target the ads. Figure 8 depicts the preference regions for this model. As is evident in Figure 8, the main results of the base models hold under this alternative specification. In Figure $^ { 8 , }$ we have $b = - 2 . 5$ in contrast to $b = - 5$ in Figure 4. The reason is, the publisher never prefers the current CPM model to the CPC model for $b = - 5 ,$ . Mistargeting effect becomes a dominant factor (low b), because the publisher does not make the optimal trade-offs in choosing the spread in the current model $( s ^ { * } = 1 )$ . The CPM model of this section, thus, performs quite poorly for both the advertiser and the publisher under high mistargeting effect. On the other hand, for low mistargeting effect $( b = 0 . 8 )$ in Figure 8, the publisher’s CPM and the advertiser’s CPC preference regions are larger compared to the same case in Figure 5. Therefore, under low mistargeting effect, the publisher is better off controlling some campaign decisions and the advertiser is worse off by not controlling all the decisions in the CPM model.

## 5.4. The CPC Model with Costly Endogenous Information Acquisition

In this alternative CPC model, we relax the assumption of perfect information acquisition at no cost. The publisher can now reduce the level of initial uncertainty $( d - c )$ by an amount  at a fixed cost of information acquisition $( A / 2 ) ( d - c - \delta ) ^ { 2 } \nonumber$ , where $A \geq 0$ This cost function is highest when perfect information is acquired $( \delta = 0 )$ and lowest when no information is acquired $( \delta = d - c )$ . Furthermore, the choice of  is endogenous and made by the publisher. We provide the details of the statement and analysis of this model in Appendix E in the online supplement. Although all the qualitative results of our base models hold with this extension, not surprisingly, introducing costly information acquisition makes the CPC model less desirable compared to the CPM model (see Figure 9).

Figure 9 The Boundary Between the CPM Model and the CPC Model with Costly Information Acquisition  
![](/api/attachments/Z77M45NR/fulltext/images/0d4674e9ec8175a07a6672f2d83c123b1042719f81f03a039c99294690103fd5.jpg)

## 6. Managerial Implications

## 6.1. Implications for Advertisers

An advertising campaign usually employs different pricing models and runs on a number of websites. The campaign may include text, display, and video ads. The advertiser’s problem is to choose a portfolio of websites and ad networks that employ different pricing models. As the following quote emphasizes, one of the fundamental issues is to manage downside risk due to the uncertainty effect exacerbated by the mistargeting effect:

CPA [or CPC] offers guaranteed results, while CPM carries the risk that nobody will click through and your investment vanishes into the ether. (Limbach 2002)

The source of uncertainty may stem from the advertiser’s business model. Advertisers with niche products and small target markets in the consumer population face higher uncertainty. For a small advertiser, it is difficult to predict whether a website’s audience belongs to its narrowly defined target market. For example, for a pure online retailer without a physical presence, target market is constrained, among other things to be consumers who are willing to shop online. On the other hand, for a national brand, target market can be defined in terms of age category and gender. Table 3, which shows the pricing model choice on the same website, supports this prediction. CPM advertisers are national brands, and they attract significantly more traffic than CPC advertisers. For example, whereas Classmates.com has a traffic ranking of 804, TCAfutures.com has a ranking of 428,877.

When the uncertainty effect’s impact is slight, then CPM pricing, which provides more control over targeting and volume (intensity) decisions, becomes more desirable, as suggested by the following excerpt from an industry publication:

Many marketers are wedded to CPA pricing, when they could generate stronger performance by purchasing on a CPM basis. Since the expected value of CPM inventory is already known to a network, by agreeing to CPM pricing on highly targeted inventory, marketers can better manage volume of their targeted campaigns and potentially pocket a significant ROI improvement. In CPA pricing, the network will apply “black box” targeting to maximize its own yield. In CPM pricing, the advertiser may be able to employ its own targeting schemes to procure highly relevant impressions at a lower effective cost. (Howe 2005)

Table 3 Pricing Model Choice at NYTimes.com’s Business Section in July 2008

<table><tr><td>Advertiser</td><td>Log $_{10}$ (Traffic rank)</td><td>Pricing model</td></tr><tr><td>Classmates.com</td><td>2.9</td><td>CPM</td></tr><tr><td>Chevrolet.com</td><td>3.7</td><td>CPM</td></tr><tr><td>CDW.com</td><td>4.1</td><td>CPM</td></tr><tr><td>Spanishschool.uninter.edu.mx</td><td>5.6</td><td>CPC</td></tr><tr><td>TCAfutures.com</td><td>6.6</td><td>CPC</td></tr><tr><td>Mandus-Forex.com</td><td>7.4</td><td>CPC</td></tr></table>

Note. See Appendix A in the online supplement regarding the data collection procedure for this table.

Our model can also explain the popularity of CPM or branding campaigns on large portals among large advertisers (eMarketer 2008a). National brands have very large target markets with broad interests. Therefore, uncertainty effect is small for national brands. Moreover, attracting people with broad interests is cheaper per impression than attracting a targeted audience. This, in turn, implies that the price per impression would be lower for large campaigns. Because the probability of covering the target segment is high and the cost is low, CPM emerges as the most suitable pricing model for large portals and large advertisers.

Exposure value and alignment effects also play critical roles in the advertiser’s preference for a pricing model, especially when exposure value is high. Because CPC prices are value based, CPC is more expensive for these advertisers (see Table 2 with a = 40). Recent discussions in the trade press further buttress the importance and validity of this finding:

It may be asked why an advertiser would purchase inventory based on a CPM price structure when inventory might be available based on a pay-for-performance price structure. The reason is that sometimes, depending on performance, CPM-based buys can actually yield lower costs per action than CPC buys.

With a CPC (cost per click) or CPA (cost per acquisition) buy, an advertiser is locked to a cost per response regardless of whether or not response rates rise or fall. By fixing this variable, one manages the downside risk of possible poor performance (e.g., weak creative or poorly targeted placements). But if response is good or improves, the advertiser is still beholden to that cost per response. (Meskauskas 2005)

It is worth noting that the alignment effect is also important in Table 3, as it may not be feasible for tcafutures.com to pay NYTimes.com’s CPM rates.

## 6.2. Implications for Publishers

Publishers ultimately decide what offers to accept from advertisers. A publisher faces advertising demand from advertisers with different characteristics and preferences. For this reason, the online advertising medium evolved such that several publishers offer different pricing models that use separate parts of a Web page and different formats (e.g., CPC for text ads, CPM for display ads). This strategy reflects a need to satisfy advertisers’ needs. For example, publishers with websites associated with high uncertainty effect—without past performance history or with volatile results—are more likely to offer performance-based deals. These publishers cannot attract advertising demand, because CPM advertisers would reduce their business volume due to high uncertainty and mistargeting effects. The publisher, thus, may have to accept CPC deals to attract advertisers, as the following quotation recommends:

CPM based fee elements are more suitable for websites which are successful in terms of track records of brand awareness, responses, or other advertiser’s target, 0 0 0 0 [CPC]-based fee elements are more suitable where the online property cannot demonstrate that track record, or where there’s an element of uncertainty 0 0 0 0 All ads are experiments, some more certain than others. (Baugh 2001)

On the flip side, exposure-value effect would encourage publishers to opt for CPC deals even though the advertisers are willing to offer CPM deals. For example, search engines successfully adopted and popularized CPC pricing. Google switched from offering both models to only the CPC-based Google AdWords program (see New York Times 2009). Interestingly, in 2005, Google reintroduced the CPM model in its AdWords auction system for placement-targeted ads, where it displays ads on its network of partner websites. The stated reason for offering CPM is “[a]dvertisers have told us that CPM pricing is a tool they like to have available for their AdWords campaigns 0 0 0 0 As a result, AdWords has made CPM pricing available to those who prefer it” (Google 2006).

However, not all publishers can be successful with CPC pricing. As traditional agency theory predicts, performance-based compensation will attract agents with higher abilities (Prendergast 1999). As a result, publishers with good targeting capabilities and ability to produce good results would prefer CPC:

0 0 0 industry rates average about 0.25% from what I hear and read. On smartly targeted sites 0 0 0 you can beat that rate. We regularly clear CTR [click-through] rates of 3% to 14%, mainly because we keep our advertisers within a narrowly defined brand-compatibility 0 0 0 0

(Frankel 2001)

What matters most is targeting the right market.

(Hopkins 2001, emphasis added)

In summary, online publishers face a trade-off between pleasing their advertisers and using their capabilities to maximize their own profits. Naturally, this will segment the advertising market on the demand side with respect to the different advertiser preferences. To meet the needs of these different segments, publishers should offer a portfolio of different pricing models, as the NYTimes.com example illustrates in Table 3.

## 7. Conclusion

Online advertising will increasingly become an indispensable element of information technology companies’ business models. We developed a model of advertising on a website and explained the role of the two most popular pricing models for online advertising using a game-theoretic framework. We identified several factors that influence the choice of a pricing model: uncertainty effect, exposure-value effect, mistargeting effect, and alignment effect. These factors may lead to conflicts between publishers and advertisers, and we highlighted the role of market characteristics on these factors.

One possible direction for future research is investigating the impact of advertiser competition on the pricing model choices. We conjecture that competition is a control dimension. A reasonable assumption can be made such that a publisher wants to increase the level of advertiser competition, and advertisers want to reduce direct competition. Because CPC is characterized by the publisher making decisions with better information, the publisher may act to intensify competition. Considering this incentive on the publisher side, the advertisers may opt for CPM pricing, where they retain the control of targeting. This paper identifies market conditions in which the advertiser and publisher’s preference for CPM or CPC coincide (diverge). It would be interesting, particularly when the two parties prefer different pricing policies, to develop a mechanism to resolve the conflict. This could be another promising avenue for future work.<sup>13</sup>

## Electronic Companion

An electronic companion to this paper is available as part of the online version at http://dx.doi.org/10.1287/ isre.1110.0391.

## Appendix. Notation Table

Model Parameters

a: exposure value in the target segment.

b: exposure value in the nontarget segment.

u: publisher’s outside option.

: the propensity to click in the target segment.

: the propensity to click in the nontarget segment.

$T \sim \mathrm { U } [ c , d ] ;$ : unknown location of the target segment boundary with realization  for $0 \leq c \leq d \leq 1$

$\tilde { k } \sim \mathrm { U } [ \underline { { k } } , \bar { k } ] \colon$ random variable for the ad serving cost with realization k.

## Decision Variables

s: campaign spread level corresponds to advertising in 601 s].

x: campaign intensity, the number of impressions at each point on the targeting line.

p: price per impression in the CPM model.

: price per click in the CPC model.

M = xs: total number of impressions.

## Functions

$\Pi ^ { A } ( x , s \mid \tau ) ;$ advertiser’s revenue function given $T = \tau .$

$\Omega ( x , s \mid \tau )$ : advertiser’s payoff function given $T = \tau$ $\mathrm { N } ( x , s \mid \tau ) ;$ the number of clicks given $T = \tau$

$\Omega ^ { A } ( \mathrm { C P M } ) , \Omega ^ { A } ( \mathrm { C P C } )$ : advertiser’s equilibrium CPM and $\mathrm { C P C \ p a y o f f s . }$

$\Omega ^ { P } ( { \bf C P \bar { M } } ) , \Omega ^ { P } ( { \bf C P C } )$ : publisher’s equilibrium CPM and CPC payoffs.

## References

Ad Age. 2008. The advertising century: John Wanamaker. Accessed August 2008, http://adage.com/century/people006.html.

Aghion, P., J. Tirole. 1997. Formal and real authority in organizations. J. Political Econom. 105(1) 1–29.

Assael, H., H. M. Cannon. 1979. Do demographics help in media selection. J. Advertising Res. 19(6) 7–11.

Austin, R. D. 2001. The effects of time pressure on quality in software development: An agency model. Inform. Systems Res. 12(2) 195–207.

Bagwell, K. 2007. The economic analysis of advertising. M. Armstrong, R. Porter, eds. Handbook of Industrial Organization, Vol. 3. North-Holland, Amsterdam, 1701–1844.

Barban, A. M., C. M. Steven, F. J. Kopec. 1993. Essentials of Media Planning. NTC Business Books, Chicago.

Baudisch, P., D. Leopold. 1997. User-configurable advertising profile applied to Web page banners. Proc. First Berlin Economics Workshop, Berlin. http://patrickbaudisch.com/publications/ 1997-Baudisch-Berlin-UserConfigurableAdvertisingProfiles.pdf.

Baugh, R. 2001. Re: What is fair? Clicks or conversions. Online Advertising discussion list (October 30) http://www.o-a.com/ archive/0110/4897.html#start.

Black, J. 2001. Performance anxiety hits online ads. Business-Week (August 15) http://www.businessweek.com/bwdaily/ dnflash/aug2001/nf20010815\_806.htm.

Butters, G. 1977. Equilibrium distributions of sales and advertising prices. Rev. Econom. Stud. 44(3) 465–491.

Chatterjee P., D. L. Hoffman, T. P. Novak. 2003. Modeling the clickstream: Implications for Web-based advertising efforts. Management Sci. 22(4) 520–541.

Dewan, R., M. Freimer, J. Zhang. 2002. Management and valuation of advertisement-supported websites. J. Management Inform. Systems 19 (3) 87–98.

eMarketer. 2008a. Why online display ads still matter. (February 8) http://www.emarketer.com/Article.aspx?id=1005912.

eMarketer. 2008b. Worldwide online ad spending. (July 3) http:// www.emarketer.com/Article.aspx?R=1006403.

Frankel, R. 2001. Re: Affiliate junk-revisited briefly. Online Advertising discussion list (October 25) http://www.o-a.com/ archive/0110/4887.html#start.

Gaffney, J. 2001. The battle over Internet ads. Business 2.0 (July 25) http://web.archive.org/web/20020601124847/http://www .business2.com/articles/web/0,1653,16546,00.html.

Gallagher, K., J. Parsons. 1997. A framework for targeting banner advertising on the Internet. Proc. 13th Annual Hawaii International Conference on System Sciences (HICSS), IEEE Computer Society Press, Washington, DC.

Google. 2006. CPM pricing for site-targeted campaigns. Accessed December 22, 2008, http//docs.justia.com/cases/federal/ district-courts/california/candce/5:2005cv03649/34465/81/14.pdf.

Grossman, G. M., C. Shapiro. 1984. Informative advertising with differentiated products. Rev. Econom. Stud. 51(1) 63–81.

Guth, R. A., K. J. Delaney. 2007. Selling Web advertising space like pork bellies: Exchanges that pair buyers, sellers for available ad slots attract Internet giants. Wall Street Journal (May 29) B1.

Hoffman, D. L., T. P. Novak. 2000. Advertising pricing models for the World Wide Web. D. Hurley, B. Kahin, H. Varian, eds. Internet Publishing and Beyond: The Economics of Digital Information and Intellectual Property. MIT Press, Cambridge, MA, 45–61.

Hopkins, M. 2001. Keep it targeted, stupid - [Was: Affiliate junk]. Online Advertising discussion list (November 1) http://www.oa.com/archive/0111/4910.html#start.

Howe, S. 2005. How to beat the system. iMedia Connection (October 10) http://www. imediaconnection.com/content/6915.asp.

IAB. 2008. IAB Internet Advertising Revenue Report: 2007-Full Year Results. Accessed July 15, 2008, http://www.iab.net/media/ file/IAB\_PwC\_2007\_full\_year.pdf.

I-Advertising. 2001. I-Advertising interviews: Scot McLernon, Executive VP Sales, CBS MarketWatch.com. Accessed October 9, 2007, http://web.archive.org/web/20010718173722/http://www.i -advertising.com/news/int071601.shtml.

Iyer, A. V., L. B. Shwarz, A. Z. Stefanos. 2005. A principal-agent model for product specification and production. Management Sci. 51(1) 106–119.

Karuga, G. G., A. M. Khraban, S. K. Nair, D. Rice. 2001. AdPalette: An algorithm for customizing online advertisements on the fly. Decision Support Systems 32(2) 85–106.

Kohda, Y., S. Endo. 1996. Ubiquitous advertising on the World Wide Web: Merging advertisement on the browser. Computer Networks ISDN Systems 28(7–11) 1493–1500.

Kumar, S., V. Jacob, C. Sriskandarajah. 2006. Scheduling advertisements on a Web page to maximize space utilization. Eur. J. Oper. Res. 173(3) 1067–1089.

Lal, R. 1986. Delegating pricing responsibility to the salesforce. Marketing Sci. 5(2) 159–168.

Langheinrich, M., A. Nakamura, N. Abe, T. Kamba, Y. Koseki. 1999. Unintrusive customization techniques for Web advertising. Proc. 8th Internat. World Wide Web Conf., Toronto. http://www.ra.ethz.ch/CDstore/www8/data/2159/ html/index.htm.

Lee, K. 2002. Google and Overture: CPM in disguise? ClickZ (September 4) http://www/clickz.com/clickz/column/1705617/ google-overture-cpm-disguise.

Lee, K. 2005a. Tapping the power of Google’s AdSense bidding. ClickZ (December 9) http://web.archive.org/web/ 200601126230056/http://www.clickz.com/experts/search/strat/ article.php/3569251.

Lee, K. 2005b. SEM in the age of uncertainty. ClickZ (December 16) http://web.archive.org/web/20060101124136/ http://clickz.com/experts/search/strat/article.php/3571011.

Limbach, D. 2002. Re: CPM pricing models. Online Advertising discussion list (January 18) http://www.o-a.com/archive/0201/ 5344.html#start.

Manchanda, P., J. Dube, K. Y. Goh, P. K. Chintagunta. 2006. The effects of banner advertising on Internet purchasing. J. Marketing Res. 43(1) 98–108.

Marketwatch. 2002. SEC Filling Form 10-K for the Fiscal Year 2001. Accessed August 8, 2008, http://www.sec.gov/Archives/ edgar/data/1068969/000106896902000004/body10k.htm.

Melumad, N., S. Reichelstein. 1987. Centralization versus delegation and the value of communication. J. Accounting Res. 25(1) 1–18.

Meskauskas, J. 2005. Taking the promo online. iMedia Connection (September 30) http://www.imediaconnection.com/ content/6866.asp.

Meskauskas, J. 2006. A second look at media auctions. iMedia Connection (February 21) http://www.imediaconnection.com/ content/8333.asp.

New York Times. 2009. Yahoo-Microsoft deal. (July 30) http:// topics.nytimes.com/top/news/business/companies/yahoo \_inc/yahoo-microsoft-deal/index.html.

Novak, T. P., D. L. Hoffman. 1997. New metrics for new media: Toward the development of Web measurement standards. World Wide Web J. 2(1) 213–246.

Prendergast, C. 1999. The provision of incentives in firms. J. Econom. Literature 37(1) 7–63.

Rothenberg, R. 1998. Bye-bye. Wired (6.01) http://www.wired.com/ wired/archive/6.01/rothenberg\_pr.html.

Sheiner, L. 2001. Internet advertising bubble. E-mail to post@i -advertising.com (August 15).

Tirole, J. 1987. The Theory of Industrial Organization. MIT Press Cambridge, MA.

Tomlin, J. A. 2000. An entropy approach to unintrusive targeted advertising on the Web. Proc. 9th Internat. World Wide Web Conf., http:// www9.org/w9-papers/EC-Security/214.pdf.

Vogelstein, F. 2005. Yahoo’s brilliant solution. Fortune Magazine. Accessed October 9, 2007, http://money.cnn.com/magazines/ fortune/fortune\_archive/2005/08/08/8267671/index.htm.

Wang, E. T. C., T. Barron, A. Seidmann. 1997. Contracting structures for custom software development: the impacts of informational rents and uncertainty on internal development and outsourcing. Management Sci. 43(12) 1726–1744.
