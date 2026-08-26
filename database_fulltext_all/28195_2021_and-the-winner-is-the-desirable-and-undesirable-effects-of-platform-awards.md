---
otero_id: 28195
otero_key: "8FG8FDDW"
title: "And the Winner Is …? The Desirable and Undesirable Effects of Platform Awards"
authors: "Jens Foerderer; Nele Lueker; Armin Heinzl"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1019"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# And the Winner Is … ? The Desirable and Undesirable Effects of Platform Awards

Jens Foerderer,<sup>a</sup> Nele Lueker,<sup>b</sup> Armin Heinzl<sup>b</sup>

<sup>a</sup> TUM School of Management, Technical University of Munich, 74076 Heilbronn, Germany; <sup>b</sup> Business School, University of Mannheim, 68131 Mannheim, Germany

Contact: jens.foerderer@tum.de, https://orcid.org/0000-0002-3090-4559 (JF); lueker@uni-mannheim.de https://orcid.org/0000-0002-1792-7967 (NL); heinzl@uni-mannheim.de, https://orcid.org/0000-0001-9886-9596 (AH)

Received: May 2, 2019 Revised: March 22, 2020; November 3, 2020; February 4, 2021 Accepted: February 14, 2021 Published Online in Articles in Advance: July 9, 2021

https://doi.org/10.1287/isre.2021.1019

Copyright: © 2021 INFORMS

Abstract. We study platform <sup>fi</sup>rms’ decision to recognize innovation by complementors ex post through awards. Despite being purely symbolic, awards might set incentives for complementors’ product strategies that can eventually lead to both desirable and undesirable outcomes for the platform <sup>fi</sup>rm. We depart from signaling theory and derive hypotheses on the effects of awards on complementors’ product strategies. To test them, we implement a quasiexperiment in the context of the Google Android mobile platform and the prestigious Google Play Award. We infer the effect of the award by estimating the difference-in-differences between award winners and runners-up, before and after the conferral. The main sample encompasses 125 award nominees and their 793 apps between 2016 and 2018. We report three <sup>fi</sup>ndings. First, the award encourages recipients to focus on releasing complement improvements rather than new complements. Second, the award increases recipients’ likelihood of multihoming. Finally, the award increases new complement releases in the recipients’ market niche by attracting other complementors. We contribute to the platform governance literature by informing about the effects of awards. Additionally, our <sup>fi</sup>ndings have theoretical implications for understanding “soft” platform governance mechanisms.

History: Ola Henfridsson, Senior Editor; Yili (Kevin) Hong, Associate Editor. Supplemental Material: The online appendix is available at https://orcid.org/10.1287/isre.2021.1019.

Keywords: platform ecosystems awards platform governance multihoming signaling software updates mobile apps multisided markets innovation complement signaling

## 1. Introduction

A key challenge for <sup>fi</sup>rms in charge of digital platform ecosystems is innovation in software complements (e.g., Tiwana et al. 2010, Parker et al. 2017, Constantinides et al. 2018). As noted by Parker and Van Alstyne (2018, p. 3015), a platform <sup>fi</sup>rm can “coax but it cannot coerce” complementors into innovating.

Cognizant of this challenge, platform <sup>fi</sup>rms have increasingly been seeking to recognize and honor complementary innovation ex post with awards. Awards are a symbolic, non-monetary means of publicly conveying recognition and honor (Gallus and Frey 2016). Google bestows the Google Play Award annually to a handful of app developers on its Android mobile platform. Similarly, Apple curates the Apple Design Award, Microsoft grants the Partner of the Year Award, and SAP confers the Pinnacle Award.

In this paper, we seek to understand how winning an award affects complementors’ choices between different product development strategies. We investigate this question from the perspective of the platform owner in order to inform about the effects and design of award programs. Although the practice of bestowing awards has become business as usual for platform <sup>fi</sup>rms, little systematic evidence exists regarding its potential effects. Given that awards are non-monetary and symbolic one may argue that they have little or no effect on complementor behavior. Thus, award programs may do little to encourage innovation. More problematic, however, is Gallus and Frey’s (2016) conclusion made after reviewing extant empirical studies of award programs across various contexts: awards may incentivize behaviors that eventually turn out to be detrimental for the award giver. This raises the question of whether awards may lead to undesirable outcomes for the platform <sup>fi</sup>rm.

Extant research is relatively silent on this issue. Work on platform governance has investigated various mechanisms, including boundary resources (e.g., Ghazawneh and Henfridsson 2013), competition (e.g., Foerderer et al. 2018), and control (e.g., Parker and Van Alstyne 2018). However, these studies primarily assess “hard” governance mechanisms that seek to direct complementor behavior through providing resources or exerting control. By contrast, “soft” governance mechanisms such as awards remain less understood.

Our hypothesis development departs from signaling theory (Spence 1973). One may argue that an award represents a public, veri<sup>fi</sup>able signal of complement quality. Therefore, three effects are plausible. First, award winners should be more likely to release complement updates and less likely to release new complements. This is because recipients can use the award as a quality signal to prospective customers, therefore having a market incentive to capitalize on their existing complements. Second, award winners should be more likely to multihome because of reduced costs of visibility and lower risk of failure. Furthermore, an award reveals information about complement quality to rival platform owners, who are likely to poach recipients. Finally, we argue that other complementors are likely to follow award winners and release new complements in the award winners’ market niche because the award signals the quality of the market niche.

We test the hypotheses in the context of the Google Android mobile app platform and the annual Google Play Award. The Google Play Award recognizes “developers that continue to set the bar for quality apps and games [ … ], with an emphasis on overall quality, strong design, technical performance, and innovation” (Google 2019). This context is suitable for two reasons. First, we can observe the behavior of complementors (i.e., app developers) before and after they receive an award. Second, the context provides a unique opportunity to identify the effects of the award in a quasi-experimental research design. Google publishes the full short list of award nominees. This allows us to compare the behavior of award winners with that of a relatively homogenous control group, namely, runners-up. Econometrically, we infer the effects of winning the award in a difference-in-differences (DID) setup.

We observe evidence consistent with the hypotheses. Additional robustness checks corroborate the model assumptions and conclusions. We demonstrate that the results hold for alternative control groups constructed via coarsened exact matching (CEM) and propensity score matching (PSM) (Rosenbaum and Rubin 1983, Iacus et al. 2012). Further tests corroborate the assumption of parallel trends, including preaward checks and a relative-time model.

Our study offers three theoretical contributions. The <sup>fi</sup>rst and principal one is toward research on platform governance (Constantinides et al. 2018, Parker and Van Alstyne 2018). The present work extends our understanding of one key governance mechanism, namely, awards. Second, our study adds to the growing research on the consequences of awards, particularly by linking awards to <sup>fi</sup>rms’ product strategies (Gallus and Frey 2016, Robinson et al. 2021). Finally, this study adds to the literature on the antecedents of complementors’ product strategies (Bhargava et al. 2013, Tiwana 2015).

## 2. Theoretical Foundations and Hypotheses

## 2.1. Conceptualization and Related Literature

2.1.1. Governance of Platform Ecosystems. One strategy by which <sup>fi</sup>rms can pro<sup>fi</sup>t from innovation capabilities outside their boundaries is the establishment of digital platform ecosystems (e.g., Tiwana et al. 2010, Parker et al. 2017). When a <sup>fi</sup>rm follows a platform strategy, it allows other <sup>fi</sup>rms to develop and commercialize products complementary to its platform. The term digital platform thereby refers to a software system that becomes more attractive to users, as the availability and quality of its complements increase (Parker and Van Alstyne 2005, Tiwana et al. 2010). Based on Brandenburger and Nalebuff (1996), we use complement to refer to any other product that makes the platform more valuable for its users. The term complementor refers to <sup>fi</sup>rms that develop and offer complements.

Our study relates to research on platform governance (Tiwana et al. 2010, Wareham et al. 2014, Parker and Van Alstyne 2018). This stream of research is based on the notion that platform owners’ activities go beyond development and marketing. Instead, the platform <sup>fi</sup>rm is in charge of a microeconomy, and therefore needs to design mechanisms that encourage desirable behaviors and outcomes.

Previous studies have researched various governance decisions, including pricing (Hagiu 2006), resourcing (Ghazawneh and Henfridsson 2013, Foerderer et al. 2019), restricting the number of complements (Boudreau 2012), matching (Bhargava et al. 2020), seeding (Huang et al. 2018), rule setting (Claussen et al. 2013), intellectual property rights (Ceccagnoli et al. 2012), performance investments (Anderson et al. 2014), inter<sup>fi</sup>rm exchange (Foerderer 2020), social norms (Burtch et al. 2018), and value capture (Foerderer et al. 2018). All these studies investigate mechanisms that require substantial <sup>fi</sup>nancial commitment or the exertion of control in terms of a hard governance mechanism. By contrast, we study awards which represent a comparatively soft governance mechanism, in terms of being non-monetary and non-control.

Research has started to investigate soft governance mechanisms only recently. Jullien and Pavan (2019) and Hukal et al. (2020) investigate the communication behavior of platform owners. For example, Hukal et al. (2020) observe that platform owners can direct complementor contributions to certain areas of the ecosystem by communicating their intention and interest in advancing these areas. Liang et al. (2019) investigate spillover effects from endorsements. Adding to these studies, we focus on understanding the consequences of awards on complementors’ product strategies.

2.1.2. Awards. Awards are a special form of non-<sup>fi</sup>nancial, symbolic recognition that is conferred to a recipient (Gubler et al. 2016, Frey and Gallus 2017). Two broad types of awards can be distinguished: prospective and retrospective (Frey and Gallus 2017, Robinson et al. 2021). Prospective awards are based on clear, prespeci-<sup>fi</sup>ed criteria (e.g., sales targets) and are automatically conferred if these are ful<sup>fi</sup>lled by aspirants. Prospective awards are like tournaments in that they seek to stimulate competition through the prospect of a reward. By contrast, retrospective awards highlight outstanding behavior ex post and often come as surprise to the recipient. They allow an effort to be recognized more broadly without the need to quantify expected behaviors beforehand (e.g., an Oscar or a Best Paper award). In this paper, we study retrospective awards.

The work on retrospective awards is, as Frey and Gallus (2017) conclude in their survey of extant work, still in its early stages. The primary difference between our work and extant studies of awards is that we investigate awards that are conferred on <sup>fi</sup>rms, and not on individuals. Most previous studies have investigated awards for individuals and studied outcomes such as employee motivation (Kosfeld and Neckermann 2011), student attendance (Robinson et al. 2021), and community contributions (e.g., Gallus 2016, Burtch et al. 2021, Chen et al. 2010). Comparably few works have investigated awards for products or <sup>fi</sup>rms (e.g., Hendricks and Singhal 1996, Anand and Watson 2004, Kovacs and Sharkey´ 2014).

Nevertheless, the current studies center around a shared debate, namely, whether retrospective awards (hereafter, “awards”) have any effect on recipients’ behavior. This question is not trivial given that awards are symbolic, uncostly to arrange, and hold no monetary value for the recipient. The results mostly indicate positive effects, but some studies also indicate no effects or even negative effects (e.g., Gubler et al. 2016).

2.1.3. Complementors’ Product Strategies. We use the term product strategy to refer to a <sup>fi</sup>rm’s general set of choices regarding its allocation of scarce resources among different software product development and portfolio decisions (Sorenson 2000).

Building on prior literature, we distinguish between three main strategies: new complement development, complement improvements (i.e., updates or enhancements), and multihoming (e.g., Bhargava et al. 2013, Cennamo et al. 2018). New complement development is the release of products that have not previously been released by the complementor to the market, in terms of being new to the complementor. Furthermore, new complements may be aimed at new markets or at customer groups not previously addressed by the complementor (Bhargava et al. 2013). New complement development is costly and risky because it requires market research, the generating of new ideas, prototyping, development, testing, and market launch (Brown and Eisenhardt 1995).

Complement improvements are incremental enhancements of an existing complement. In the software context, they are usually synonymous with updates. Updates add new capabilities or attributes to products (Nowlis and Simonson 1996), keep them operational (Banker et al. 1998, Cavusoglu et al. 2008), or patch errors and security issues. Updates are not stand-alone products but are integrated into an existing product (Krishnan and Ramachandran 2011). Complement updates are less costly and less risky than new complement developments because they leverage a <sup>fi</sup>rm’s existing capabilities, infrastructures, and products. Updates also allow <sup>fi</sup>rms to exploit existing demands and build on a known and familiar market.

Multihoming refers to the decision to operate a complement on other platforms (Caillaud and Jullien 2003, Tanriverdi and Lee 2008, Landsman and Stremersch 2011). Multihoming contrasts with singlehoming, which is operating a complement only on the focal platform. Multihoming has the bene<sup>fi</sup>t of allowing a complementor to reach a new customer base with an existing product strategy but may carry signi<sup>fi</sup>cant costs. These costs pertain to the need to adjust a complement to new technological speci<sup>fi</sup>cations and new interfaces, and sometimes even the need to code the complement from scratch (Cennamo et al. 2018, Kang et al. 2019).

The different strategies employed by complementors also have consequences for the platform <sup>fi</sup>rm (Bhargava et al. 2013, Foerderer et al. 2018). Arguably, new complement development is vital for platform <sup>fi</sup>rms because it can bring about innovation. Complement improvements are also important because they increase the quality of the complements and ensure that complementors address the needs of an existing user base. By contrast, multihoming is an undesirable outcome because it reduces platform <sup>fi</sup>rms’ differentiation from their rivals (Landsman and Stremersch 2011, Kang et al. 2019).

There is growing research that takes the complementors’ perspective (Tanriverdi and Lee 2008, Bhargava et al. 2013, Cennamo et al. 2018). Some studies have investigated multihoming and updating (Cennamo et al. 2018, Kang et al. 2019). Cennamo et al. (2018), for example, found that the characteristics of the platform technology determine complementors’ tendency to multihome. Tiwana (2015) reports that increased rates of updating are related to platform control and the modularity of the complement. These contributions notwithstanding, little work so far has considered the relationship between awards and complementors’ product strategies.

## 2.2. Theoretical Framework and Hypotheses

2.2.1. Awards as Signals. To understand the consequences of awards, we draw on the theoretical concept of signaling (Spence 1973, Connelly et al. 2011). This departs from the notion that exchanges between market actors are characterized by information asymmetries (e.g., Jensen and Meckling 1976). To overcome information asymmetries, actors can employ signaling, that is, credibly conveying information that reduces other actors’ uncertainty and eventually in<sup>fl</sup>uences their behavior.

Following Stiglitz (2000), we focus on asymmetries arising from the uncertainty regarding the qualities of an actor. Quality uncertainty refers to the “underlying, unobservable ability [ … ] to ful<sup>fi</sup>ll the needs or demands” (Connelly et al. 2011, p. 43). A detailed discussion of signaling theory and an excellent overview of the literature appears in Connelly et al. (2011).

Awards ful<sup>fi</sup>ll the two primary conditions for being a signal, namely, information content and observability. First, awards convey quality-related information. Awards reward behavior that is considered desirable, is worthy of respect, and exceeds expectations (Gallus and Frey 2017). The award signals to users that the winner has engaged in outstanding behaviors. Users can view awards as signals of desirable, unobservable complementor characteristics. An award is presumably a reliable signal because other complementors were not able to withstand the rigors of the selection procedure and because it has been conferred by the platform owner. Second, awards are observed by other parties, including platform users, complementors, and other platform owners. Awards are typically conferred as part of a public ceremony. In addition, the press reports award recipients. Award winners also frequently announce their distinctions, displaying the award on their websites or using it in their advertising.

2.2.2. Hypotheses. Awards are likely to exert crucial in<sup>fl</sup>uence on the relationship between complementors and potential users of their complements. The primary reason for this lies in the uncertainty that users face before committing to a purchase. Part of this uncertainty derives from the large numbers of complements available on many platforms. Even in a relatively narrow product category, there can be many complements available (e.g., Boudreau 2012). To evaluate complements, users have to spend search costs in the form of their time and attention (Ghose et al. 2012). Uncertainty about quality is another distinct issue for platform users (Boudreau and Hagiu 2009, Dimoka et al. 2012). Complements are experience goods, whose quality is dif<sup>fi</sup>cult to assess before usage. Users may hesitate to choose complements, especially when it is costly to obtain information about their true quality, or when it is costly to obtain or return them (Halaburda et al. 2018, Jullien and Pavan 2019). Also, the existence of copycats—a common issue in platform ecosystems—may further increase user uncertainty (Wang et al. 2018, Xue et al. 2019).

As a result of this uncertainty, users’ decisions tend to rely on the judgment of others, as manifested in reviews, awards, or rankings (e.g., Dimoka et al. 2012, Li et al. 2020). Lacking full information, a user might decide to buy a complementor’s product if others have evaluated it favorably. Of the various potential signals of quality available (e.g., reviews, ratings), awards provide a strong signal because they are conferred by the platform owner. In addition, given the prevalence of fake reviews, users are likely to resort to stronger signals of quality (Luca and Zervas 2016). Award winners may be better able to credibly convey quality and trust.

There is some evidence that users prefer awardwinning products or <sup>fi</sup>rms. Products tend to experience an uptick in sales after receiving an award (e.g., Anand and Watson 2004, Kovacs and Sharkey´ 2014). For example, Kovacs and Sharkey (´ 2014) observed that books attract more readers after winning an award. Hendricks and Singhal (1996) <sup>fi</sup>nd that after receiving an award, <sup>fi</sup>rms experience an increase in market valuation and, among investors, a decreased perception of systematic risk faced by the <sup>fi</sup>rm.

Given the increased demand for their complements and their improved signaling, award winners have a market incentive to capitalize on their existing complements instead of developing new ones. Updates allow complementors to exploit existing demands and build on a known customer base (Nowlis and Simonson 1996). Updates expand the lifespan of a product (Krishnan and Ramachandran 2011, Ho-Dac et al. 2020). They are also less costly and less risky than new complement developments because they leverage existing capabilities, infrastructures, and products (Krishnan and Ramachandran 2011). Improving existing products is less likely to place the relationship with existing users at risk because it involves tried and tested activities (Voss et al. 2008). By contrast, new complement development becomes the less favored option because it requires carrying out multiple activities, including market research, generating new product ideas, prototyping, development, testing, and market launch (Brown and Eisenhardt 1995). Taking these factors together, tweaking and enhancing their existing products with updates becomes the low-risk option.

There is some indirect evidence supporting these arguments. Various studies in product development literature document that <sup>fi</sup>rms focus their product development efforts on incremental improvements after initial product success (e.g., Brown and Eisenhardt 1997, Rothaermel and Deeds 2004). In addition, Voss et al. (2008) <sup>fi</sup>nd that <sup>fi</sup>rms are more likely to focus on re<sup>fi</sup>ning and improving their product portfolio when they have garnered trust and reputation in a market. Hence, we argue the following:

Hypothesis 1. Awards increase recipients’ likelihood of releasing complement updates and reduce their likelihood of releasing new complements.

We also expect that award winners have greater incentives to multihome. These incentives derive partly from reduced costs and partly from reduced risks associated with multihoming. In general, complementors multihome to address different user bases, create economies of scale, distribute <sup>fi</sup>xed costs, or become less dependent from one platform—yet this is conditional on the costs of multihoming (Corts and Lederman 2009, Landsman and Stremersch 2011).

Multihoming costs accrue in part from technological dif<sup>fi</sup>culties in porting a complement to another platform technology (Cennamo et al. 2018, Kang et al. 2019). In addition, signi<sup>fi</sup>cant costs might be incurred in creating visibility. Regarding development costs, each platform carries unique infrastructure costs due to technological differences (Anderson et al. 2014, Cennamo et al. 2018). Complements are required to implement platform-speci<sup>fi</sup>c technology standards and interface requirements. This may even require assembling specialized human capital (Venkataraman et al. 2018). Regarding visibility, creating an initial user base on a rival platform is costly for complementors, especially given the crowdedness of many platforms (e.g., Boudreau 2012). Without advertising and communication, the probability of being discovered can be low (Garg and Telang 2013, Liang et al. 2019). Expanding to rival platforms may also require complementors to incur further costs by making their complement available at lower prices, such as in a freemium version, to create an installed base (Liu et al. 2014). For all these reasons, multihoming is a risky and costly endeavor.

An award can be an important asset in cutting multihoming expenditures and mitigating risk. In particular, we expect that for award winners, multihoming becomes feasible. An award may not only serve as a quality signal to users of the awarding platform but also to users of rival platforms. Award winners may also stand out among the competition and have generally higher visibility. Therefore, award winners may need to spend less on advertisement and user acquisition. In addition, award winners may be much better positioned to monetize their complement earlier, because the award serves as a signal of trust. Taking these factors together, award winners have an incentive to multihome.

There is some empirical evidence supporting this line of reasoning. Cennamo et al. (2018) <sup>fi</sup>nd that complementors tend to release their complements on different platforms sequentially, potentially because of the costs linked to simultaneous launches.

Another reason for greater multihoming incentives lies in the competitive dynamics between platform <sup>fi</sup>rms. Winning decent complementors is important for platform <sup>fi</sup>rms because users tend to choose the platform with the most appealing set of complements (Caillaud and Jullien 2003). Thus, the success of platform <sup>fi</sup>rms is closely linked to contracting or poaching marquee complementors (Hagiu and Spulber 2013, Li and Zhu 2020).

For these reasons, platform <sup>fi</sup>rms have to continuously look out for promising or successful complementors on rival platforms and seek to poach them. Poaching allows platform <sup>fi</sup>rms to reduce the exclusivity of rival platforms, thereby making the indirect network effects less effective (e.g., Bakos and Halaburda 2020). In addition, poaching can reduce the rival platform’s sales (Landsman and Stremersch 2011), dominance (Corts and Lederman 2009), and barriers (Lee 2013).

Given that an award is publicly bestowed, it is likely that rival platforms will take notice of it. Just as the award acts as a quality signal to platform users, rival platforms will likely interpret the award as a quality signal as well. We therefore expect that rival platforms are likely to poach award winners, providing a second strong incentive for award winners to multihome.

There is some indirect evidence that supports this line of reasoning. Rietveld et al. (2019) <sup>fi</sup>nd that, to differentiate their platforms, owners of video console platforms are more likely to endorse exclusive rather than multihomed games. Li and Zhu (2020) observe that after Groupon restricted public information about its online daily deals, its rival LivingSocial copied fewer Groupon deals and sought instead to source more new deals. We argue the following:

Hypothesis 2. Awards increase recipients’ likelihood of multihoming.

We expect that an award also in<sup>fl</sup>uences the product development strategies of other complementors in the ecosystem. Given the dynamic nature of platforms, complementors continuously evaluate their product portfolios (Tiwana 2015). Complementors who intend to develop new complements face a complex choice regarding which market niche to enter. Ex ante, demand for these niches is uncertain and unknown. Part of this uncertainty derives from markets being crowded, product success being highly stochastic, and information collection being costly (e.g., Clements and Ohashi 2005, Rietveld and Eggers 2018).

The bestowal of an award resolves some of this uncertainty. First, an award may signal a promising market niche. Extant studies of platforms have already supported that complementors watch one another’s activities closely and follow each other in and out of markets (Wang et al. 2018, Xue et al. 2019). Besides, other complementors may try to follow to avoid being late to a new market. For example, Chen et al. (2020) <sup>fi</sup>nd that <sup>fi</sup>rms whose competitors receive an award are more likely to show “catch-up” behaviors by expanding into their competitors’ product markets. In addition, an award can be a signal of a platform owner’s interest in a market niche (Hukal et al. 2020).

Second, potential entrants may expect to bene<sup>fi</sup>t from demand spillovers caused by the award. Following an award, there may be an overall increase in the number of users interested in complements from the niche, from which potential entrants may stand to bene<sup>fi</sup>t. Several extant empirical studies have documented such demand spillovers (e.g., Foerderer et al. 2018, Liang et al. 2019, Song et al. 2020). For example, Foerderer et al. (2018) observe that Google’s entry into the niche for photography apps on its Android platform attracted more new app releases to that market niche, because complementors expected to bene<sup>fi</sup>t from demand and attention spillovers. Liang et al. 2019 report that competitors of an endorsed complement bene<sup>fi</sup>tted from demand spillovers. The expectation of such spillover may attract entrants.

In light of these arguments, we expect that complementors will release new complements in award winners’ market niches. Hence, we argue the following:

Hypothesis 3. Awards encourage other complementors to release new complements in recipients’ market niches.

## 3. Method

## 3.1. Empirical Context: The Google Play Awards 2016–2018

We conducted a quasi-experimental study in the context of the Google Android platform and the annual Google Play Awards. The Google Android platform is a mobile operating system. Complementor <sup>fi</sup>rms (“app developers”) provide ancillary mobile apps via the Google Play Store. The Google Play Award seeks to “recognize top app and game developers from around the world who lead the way in delighting users with incredible experiences on Android” (Google 2016). Its speci<sup>fi</sup>c focus is to honor an outstanding app by an app developer <sup>fi</sup>rm. Online Appendix Table A1 provides further details on the Google Play Award.

Google does not publish criteria for nomination or winning, but states that nominees are selected by a “panel of experts on the Google Play team based on criteria emphasizing app quality, innovation, and having a launch or major update in the last 12 months” (Google 2016). The award is conferred at Google’s annual developer conference in May. The award is purely symbolic and grants no prize money, but is considered highly prestigious.

This context is appealing for reasons of data availability. Compared with other contexts, the Google Play Award provides us with a setting in which we can observe complementor behavior over time. Other platforms nominate only a handful of <sup>fi</sup>rms per year and do not provide enough data for statistical analysis. Of particular value is the fact that Google publishes the entire short list of nominees for the award. This permits the construction of a quasi-experimental design, which we describe in the following section. Online Appendix Table A2 compares the suitability of different contexts.

## 3.2. Research Design

The main empirical challenge is to isolate the effects of the award from pre-existing heterogeneity. Simple comparisons between award winners and other complementors would be misleading because they might capture not only changes due to winning the award but also pre-existing differences that correlate with the propensity to win an award in the <sup>fi</sup>rst place.

Figure 1 illustrates our identi<sup>fi</sup>cation strategy. The context of the Google Play Award offers the opportunity for a quasi-experimental research design that may mitigate the above concerns. Less than one month before the award is presented, Google publishes a short list of the app developers nominated for the award. We expect a great degree of homogeneity among app developers on the short list because Google has selected them and it is not known which candidate will win the award. Only some of the nominees will be “lucky” and receive the award, whereas others will not receive it. It is precisely those runners-up who may provide a close-comparison benchmark.

In our quasi-experimental design, therefore, the treatment group consists of those app developers who ended up winning the award, whereas the control group consists of the runners-up. Econometrically, we infer the effects of award winning by estimating a DID design. By these means any bias caused by variables (observed or unobserved) common to award winners and runners-up is accounted for (Angrist and Pischke 2009).

## 3.3. Data Collection

Our dataset is a time-series panel on the app-month level. We conduct the analysis on the app-level because this allows accounting for app-level factors that in<sup>fl</sup>uence product strategies, and it is in line with prior research on awards (Kovacs and Sharkey´ 2014). We considered the Google Play Award in the years 2016, 2017, and 2018. We identi<sup>fi</sup>ed all apps nominated for the award in these years from the of<sup>fi</sup>cial Android

Figure 1. Difference-in-Differences Research Design  
![](/api/attachments/8FG8FDDW/fulltext/images/f58c30aaba108d134db985899c0ae02ad3effa07f4ea071ab16b17f51ae365d5.jpg)  
Notes. The <sup>fi</sup>gure illustrates the research design. We construct a quasi-experiment wherein the treatment group encompasses app developers (and their apps) that ended up winning the award (award winners) and the control group contains developers (and their apps) that were also nominated for the award but did not win (non-winners). We construct two alternative control groups via matching. We estimate the effect of the award in a difference-in-differences framework.

Developers Blog run by Google. We removed apps from the sample that were nominated in consecutive years (see Online Appendix C). We obtained monthly data (e.g., on app ratings, updates, and new app releases) from AppBrain, App Annie, and the Internet Archive.

In the dataset, the pre-award period begins in January of each year and ends in March. Nominations are announced in April, which is why we exclude this month from the analysis. Across the years studied, the dates for nomination and award conferral fall into the same month of the year. The post-award period begins in May and ends in March of the following year so that it does not overlap with next year’s award period. The length of the post-award period involves trading off variance in the dependent variables— which gets larger as we extend the post-award period—with capturing the immediate effects. Because we removed app developers who were nominated in subsequent years, little bias is to be expected, but we additionally restrict the post-award period to end in March to avoid any potential effect (see Online Appendix Figure A2).

The <sup>fi</sup>nal sample size differs depending on the control group. In the base setup (i.e., runners-up as the control group), the sample comprises 125 developers (30 winners and 95 runners-up) and their 793 apps, resulting in an unbalanced panel of 5,131 app-months. In the matched sample setup based on coarsened exact matching, given the employed procedures outlined below, the sample comprises 8,414 appmonths. In the matched sample setup based on propensity score matching, the sample comprises 8,126 app-months. We allow apps to drop out of the sample (e.g., due to being removed or due to missing data) and to enter the dataset (i.e., due to being released).

We conducted interviews with three award winners. All interviewees were founders and executives of the <sup>fi</sup>rms. We conducted semistructured interviews to validate the assumptions of the research design. We also asked the award winners questions about the impact of the award on their businesses.

## 3.4. Variables

The four dependent variables are UPDATE, NEWAPP, MULTIHOMED, and CAT\_NUMAPPS. The term UP-DATE is an indicator that takes a value of one if app i was updated in month t. To identify updates, we obtained the version number of app i in month t. If the version number changed between two consecutive periods, we coded UPDATE as one (e.g., change from 1.1 to 1.2). We created a second variable, UPD\_MINOR, coded as one if a so-called minor update was performed. To distinguish minor updates from other updates, we followed Boudreau (2010) and categorized changes in an app’s version number. An informal but not enforced convention on the version number on Android’s platform is <major>.<minor>, wherein minor updates are represented by decimal increases (Android Developers 2020).

The term NEWAPP is an indicator coded as one if developer j of app i released a new app in month t. New app releases may include not only apps new to the complementor, but also versioned releases of existing apps (e.g., Call Blocker Free versus Call Blocker Premium). We therefore scanned the names of new apps and removed instances of apps whose name hinted at versioning or a sequel.

To measure multihoming, we tracked whether app i was published on a rival platform to Google Android. At the time of the study, the mobile platform economy is characterized by two dominant platforms, Android and Apple iOS. Data obtained from one of the app analytics providers was readily coded such that multihomed apps could be directly identi<sup>fi</sup>ed. The variable MULTI-HOMED is an indicator coded as one if app i was available on Apple iOS in month t. For each app, the variable is coded as zero until an app is multihomed, and then is coded as one for the remaining periods. There is variation in the variable across apps, within developers, and over time.

Variable CAT\_NUMAPPS holds the total count of apps available in app i’s market category in month t. Google Play distinguishes more than 30 market categories, including photography, sports, tools, and several subcategories for games. These categories re<sup>fl</sup>ect customer segments and clusters of product functionality (Lee and Raghu 2014).

Regarding the independent variables, our empirical framework required two main indicators. AWARD, coded as one for apps of award winners, and AFTER, coded as one if month t is after the ceremony.

Choosing control variables is not trivial because of the risk of including “bad controls.”<sup>2</sup> We nevertheless deem it necessary to control for two variables. First, we control for pricing. Product strategies are likely to be in<sup>fl</sup>uenced by app pricing. The term PRICE holds app i’s purchase price in USD in month t. We (log 1)-transformed the variable to account for skewed distribution. We use alternative price variables in the robustness section to account for potential concerns over the empirical distribution of PRICE. Second, we control for app quality. Complement strategies may be in-<sup>fl</sup>uenced by consumer perceptions of an app. In particular, developers may be more inclined to update higher-rated apps. To capture these differences, we control for RATING, which holds the average consumer rating for app i in month t.

We rely on two further variables in additional analyses. The term NUMRATINGS is the total number of ratings submitted for app i as of month $t ,$ and EMPLOY-EES is a proxy of <sup>fi</sup>rm size in terms of the number of employees of the developer. We infer the number of employees from the number of LinkedIn members that state they worked for each <sup>fi</sup>rm. We obtain these data from each <sup>fi</sup>rm’s LinkedIn page. The term INAPP is coded as one if app i offers in-app purchases in month t. The term APP AGE is the age of app i in t in months.

Table 1 describes the sample.

## 3.5. Matching

In addition to using runners-up as a control group, we constructed two alternative control groups based on matching. Matching is based on the idea that units—in our case developers—are selected and placed into an arti<sup>fi</sup>cial control group based on their observational similarity. We selected developers based on their similarity before the award.

We conduct the matching using CEM, and document that the results hold for propensity score matching (PSM). We match on the developer level to address developer-level heterogeneity.<sup>3</sup> To create a pool of developers for matching, we obtain developers with apps in the top 300 of the Google Play Store rankings as of January 1 in the respective award year. We use the top 300 as a starting point to reduce heterogeneity to award winners. We match on the variables UPDATE and NUMRAT-INGS. Regarding the cut-off points, we followed the methodological literature, which recommends choosing coarsening values “in a customized way based on substantive knowledge of the measurement scale of each variable” (Iacus et al. 2012, p. 9). Online Appendix D provides further details.

Table 2 reports a balance check. Although we matched on only two variables, the procedure achieved balance across various developer characteristics.

## 3.6. Econometric Framework

We test the hypotheses in a <sup>fi</sup>xed-effects DID framework (Angrist and Pischke 2009):

$$
\begin{array}{r l} \Upsilon_ {i, j, t} = & \beta_ {0} + \beta_ {1} A F T E R _ {t} \times A W A R D _ {i, j} + \kappa_ {i} + \phi_ {t} \\ + & \psi_ {i, j, t} + \epsilon_ {i, j, t}. \end{array}\tag{1}
$$

$Y _ { i , j , t }$ is the dependent variable of interest in month t for complementor $j ^ { \prime } \mathbf { s }$ app i, AFTER equals one if month t is after the award, $A W A R D _ { i , j }$ is an indicator variable for whether complementor $j ^ { \prime } \mathbf { s }$ app i received an award, $\kappa _ { i }$ are app <sup>fi</sup>xed effects, and $\phi _ { t }$ are month <sup>fi</sup>xed effects. The coef<sup>fi</sup>cient of interest is $\beta _ { 1 }$ . When comparing winners to runners-up, $\beta _ { 1 }$ is the relative change in Y due to award winning, whereas nomination effects are differenced out. When comparing winners to the matched developers, $\beta _ { 1 }$ captures both the effects of the nomination and of award winning. The vector $\psi _ { \mathrm { i , j , t } }$ contains time-variant controls outlined above. We omit the regressor AFTER from the model because award time is homogenous and would be collinear to time <sup>fi</sup>xed effects. The main term $A W A R D _ { i , j }$ is not included because it is collinear to the app <sup>fi</sup>xed effects. To estimate the binary dependent variables, we use a conditional logit estimator. We cluster standard errors around app developers to adjust for the developer-app structure.

To remain consistent, we also use this app-level framework to test Hypothesis 3 but without app-level <sup>fi</sup>xed effects. We estimate CAT\_NUMAPPS with a Poisson estimator to account for its count structure. One may argue that restricting the control group to apps that are not in the same categories as award winners’ apps would avoid comparing <sup>fi</sup>rms from the same niche that have received similar increases in new app releases. The robustness section con<sup>fi</sup>rms that the results hold for this alternative setup.

Table 1. Descriptive Statistics

<table><tr><td colspan="3"></td><td>Mean</td><td>S.D.</td><td>Min.</td><td>Median</td><td>Max.</td></tr><tr><td>1.</td><td>UPDATE</td><td>Indicator that is one if app i was updated in month t</td><td>0.32</td><td>0.47</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>2.</td><td>NEWAPP</td><td>Indicator that is one if complementor j of app i released a new app in month t</td><td>0.03</td><td>0.17</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>3.</td><td>MULTIHOMED</td><td>Indicator that is one if app i was available on Apple iOS in month t</td><td>0.54</td><td>0.50</td><td>0.00</td><td>1.00</td><td>1.00</td></tr><tr><td>4.</td><td>CAT_NUMAPPS</td><td>Count of apps (in thousands) available in category of app i in month t</td><td>60.91</td><td>59.01</td><td>2.92</td><td>38.91</td><td>307.96</td></tr><tr><td>5.</td><td>PRICE</td><td>Price of app i in month t in USD</td><td>1.70</td><td>5.50</td><td>0.00</td><td>0.00</td><td>82.99</td></tr><tr><td>6.</td><td>INAPP</td><td>Indicator that is one if app i offered in-app purchases in month t</td><td>0.45</td><td>0.50</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>7.</td><td>RATING</td><td>Average rating for app i in month t</td><td>4.24</td><td>0.36</td><td>2.30</td><td>4.30</td><td>5.00</td></tr><tr><td>8.</td><td>NUMRATINGS</td><td>Count of consumer ratings (in thousands) for app i in month t</td><td>468.99</td><td>1,944.57</td><td>0.00</td><td>20.50</td><td>35,660.92</td></tr><tr><td>9.</td><td>APP AGE</td><td>Age of app i in t (in months)</td><td>27.10</td><td>21.02</td><td>0.00</td><td>23.00</td><td>95.00</td></tr><tr><td>10</td><td>EMPLOYEES</td><td>Number of employees of complementor j as inferred from LinkedIn</td><td>4,802.27</td><td>12,208.99</td><td>1.00</td><td>224.00</td><td>123,466.00</td></tr><tr><td colspan="8">11. Google Play Store category (%)</td></tr><tr><td></td><td>Art and Design</td><td>0.21</td><td>News and Magazines</td><td>3.08</td><td>Games—Card</td><td>1.57</td><td></td></tr><tr><td></td><td>Books and Reference</td><td>1.28</td><td>Personalization</td><td>0.03</td><td>Games—Casino</td><td>0.86</td><td></td></tr><tr><td></td><td>Business</td><td>0.05</td><td>Photography</td><td>0.44</td><td>Games—Casual</td><td>5.67</td><td></td></tr><tr><td></td><td>Communication</td><td>0.57</td><td>Productivity</td><td>0.78</td><td>Games—Educational</td><td>0.92</td><td></td></tr><tr><td></td><td>Education</td><td>5.20</td><td>Shopping</td><td>0.91</td><td>Games—Music</td><td>0.21</td><td></td></tr><tr><td></td><td>Entertainment</td><td>4.06</td><td>Social</td><td>0.37</td><td>Games—Puzzle</td><td>6.22</td><td></td></tr><tr><td></td><td>Events</td><td>0.08</td><td>Sports</td><td>0.84</td><td>Games—Racing</td><td>3.04</td><td></td></tr><tr><td></td><td>Finance</td><td>1.21</td><td>Tools</td><td>0.28</td><td>Games—Role Playing</td><td>10.30</td><td></td></tr><tr><td></td><td>Food and Drink</td><td>0.18</td><td>Travel and Local</td><td>1.02</td><td>Games—Simulation</td><td>2.91</td><td></td></tr><tr><td></td><td>Health and Fitness</td><td>4.40</td><td>Video Players</td><td>0.83</td><td>Games—Sports</td><td>4.24</td><td></td></tr><tr><td></td><td>Lifestyle</td><td>1.59</td><td>Games—Action</td><td>10.90</td><td>Games—Strategy</td><td>10.12</td><td></td></tr><tr><td></td><td>Maps and Navigation</td><td>0.58</td><td>Games—Adventure</td><td>6.54</td><td>Games—Trivia</td><td>0.06</td><td></td></tr><tr><td></td><td>Medical</td><td>0.28</td><td>Games—Arcade</td><td>5.73</td><td>Games—Word</td><td>0.53</td><td></td></tr><tr><td></td><td>Music and Audio</td><td>1.44</td><td>Games—Board</td><td>0.47</td><td></td><td></td><td></td></tr></table>

Notes. Statistics are reported for the primary sample. S.D., Standard deviation.

## 4. Results

## 4.1. Hypothesis Tests

Tables 3 and 4 report the results of the hypothesis tests. We <sup>fi</sup>nd support for Hypothesis 1. In Table 3, columns (1) to (3) report the estimates for Equation (1) with UP-DATE as the dependent variable. The coef<sup>fi</sup>cients are reported in log-odds notation. Column (1) shows that winning an award has a positive effect on the likelihood of an app update, with runners-up as a control benchmark. The odds of an app update are $\mathbf { e } ^ { 0 . 4 7 2 } = 1 . 6 0$ times higher for app developers who won the award. Column (2) uses CEM matches as a control group, supporting the positive effects $( \mathrm { e } ^ { 0 . 6 0 9 } = 1 . 8 4 )$ . Column (3) uses PSM matches as a control group and documents odds comparable to the baseline $( \mathrm { e } ^ { 0 . \dot { 6 } 4 1 } = 1 . 9 0 )$ . Columns (4) to (6)

estimate the effect of the award on NEWAPP. Column (4) indicates a signi<sup>fi</sup>cantly negative effect. For recipients, the odds of releasing a new app are $\mathrm { e } ^ { - 2 . 8 3 7 } = 0 . 0 6$ times that of runners-up. Column (5) uses CEM matches as the benchmark and suggests effects similar to the baseline $( \mathrm { e } ^ { - 3 . 2 2 6 } = 0 . 0 4 )$ . Column (6) uses PSM matches as the benchmark, and the coef<sup>fi</sup>cient differs only marginally from the baseline $( \mathrm { e } ^ { - 3 . 4 6 1 } = 0 . 0 3 )$ ). Taken together, these data support Hypothesis 1.

We can also observe evidence in line with Hypothesis 2. Table 4 reports the estimates. Column (1) is the baseline, predicting MULTIHOMED and using runners-up as a benchmark. For award recipients, the odds of multihoming an app are $\mathrm { e } ^ { 1 . 0 5 2 } = 2 $ .86 times that of runnersup. Column (2) uses CEM matches as the control benchmark, further corroborating the positive effects $( \mathrm { e } ^ { 1 . 0 1 2 } = 2 . 7 \dot { 5 } )$ . Column (3) uses PSM matches as the control group, also corroborating the baseline in magnitude and signi<sup>fi</sup>cance $( \mathrm { e } ^ { 1 . 0 5 5 } = 2 . 8 7 )$ . Taken together, these data provide evidence in line with Hypothesis 2.

Table 2. Pre-award Balance

<table><tr><td rowspan="2"></td><td colspan="3">Difference in means</td></tr><tr><td>Winners vs. runners-up</td><td>Winners vs. CEM</td><td>Winners vs. PSM</td></tr><tr><td>UPDATE</td><td>0.03 (ns)</td><td>0.09 (ns)</td><td>0.08 (ns)</td></tr><tr><td>NEWAPP</td><td>-0.05 (ns)</td><td>0.02 (ns)</td><td>0.02 (ns)</td></tr><tr><td>MULTIHOMED</td><td>0.13 (ns)</td><td>0.03 (ns)</td><td>0.01 (ns)</td></tr><tr><td>Log(CAT_NUMAPPS)</td><td>-0.26 (ns)</td><td>0.16 (ns)</td><td>0.08 (ns)</td></tr><tr><td>Log(PRICE)</td><td>0.00 (ns)</td><td>0.24 (ns)</td><td>0.30 (ns)</td></tr><tr><td>Log(RATING)</td><td>-0.03 (ns)</td><td>-0.02 (ns)</td><td>-0.02 (ns)</td></tr><tr><td>Log(NUMRATINGS)</td><td>-0.35 (ns)</td><td>1.78 (ns)</td><td>1.88 (ns)</td></tr><tr><td>Log(EMPLOYEES)</td><td>-0.46 (ns)</td><td>-0.58 (ns)</td><td>-0.84 (ns)</td></tr><tr><td>Log(NUMAPPS)</td><td>0.57 (ns)</td><td>0.55 (ns)</td><td>0.59 (ns)</td></tr><tr><td>Log(APP AGE)</td><td>-0.01 (ns)</td><td>-0.08 (ns)</td><td>-0.07 (ns)</td></tr></table>

Notes. Table summarizes t-tests for differences in means between the groups. ns, Not signi<sup>fi</sup>cant at the 5% level.

Finally, we <sup>fi</sup>nd support for Hypothesis 3. Column (4) of Table 4 is the baseline, predicting CAT\_NUMAPPS. The DID estimate suggests that award recipients’ market categories experience an increase in app releases. Column (5) con<sup>fi</sup>rms the positive effect when using CEM matches as the control group. Column (6) also con-<sup>fi</sup>rms the positive effect when using the PSM control group. Online Appendix Table A5 reports that the estimate differs only marginally when restricting the control group to apps that are not in the same categories as award winners’ apps. Therefore, the composition of the categories within the groups seems to exert little in<sup>fl</sup>uence on the results. Together, these analyses indicate support for Hypothesis 3.

## 4.2. Robustness and Further Analyses

In this section, we report several tests for the model assumptions, rival explanations, and sensitivity, as well as additional analyses. Table 5 summarizes them.

4.2.1. Assumption of “Parallel” Trends. The DID framework assumes that award winners and control developers are balanced on pre-award characteristics, and, more importantly, on “parallel” trends (Bertrand et al. 2004). To assess parallel trends, we adopted several tests recommended in the methodological literature (e.g., Bertrand et al. 2004).

First, we estimate regressions in which AWARD is interacted with a continuous time trend variable and data being restricted to the pre-award period. A signi<sup>fi</sup>cant interaction term would indicate a violation of the parallel-trends assumption. Table 6 reports the results. None of the interaction terms are signi<sup>fi</sup>cant, which corroborates the assumption of parallel trends. In Online Appendix Table A3, panel A reports tests for various further developer and app characteristics. Panel B summarizes the test recommended in Angrist and Pischke (2009, p. 238, equation 5.2.7), which is based on adding a developer-speci<sup>fi</sup>c time trend to Equation (1). The results are consistent.

Second, we estimate a relative time model (e.g., Greenwood and Wattal 2017). We interact dummies for each pre-award month with AWARD to allow for separate award effect magnitudes in each pre-award month:

$$
Y _ {i, j, t} = p ^ {\prime} [ A W A R D _ {i} \times T _ {\mathrm{t}} ] + \kappa_ {i} + \phi_ {\mathrm{t}} + \epsilon_ {i, j, t}.\tag{2}
$$

T is a dummy that re<sup>fl</sup>ects each observation’s distance from the award-conferral time. We omit the month immediately prior to an election and use it as the reference period. The coef<sup>fi</sup>cient of interest is $p ^ { \prime } ,$ which can be interpreted as the difference between award winners and the corresponding control group in each relative period.

Table 7 reports the estimates.<sup>5</sup> To ease interpretation, Online Appendix Figure A4 plots the coef<sup>fi</sup>cients of the interaction term. The pre-entry time dummies are insigni<sup>fi</sup>cant. Thus, there is no evidence that the award effects originate in the pre-award period. Two further observations corroborate the hypothesis tests. First, the effect on MULTIHOMED becomes positive and signi<sup>fi</sup>cant only toward the end of the observation period (and is even negative in t 4). One explanation could be that multihoming is a costly endeavor that takes time to be realized. Second, the effect on CAT NUMAPPS is not signi<sup>fi</sup>cant until period t 3, which is in line with our theorizing that new complement development takes time.

Table 3. Hypothesis Tests: Hypothesis 1

<table><tr><td rowspan="2"></td><td colspan="3">UPDATE</td><td colspan="3">NEWAPP</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>AFTER × AWARD</td><td>0.472**(0.180)</td><td>0.609**(0.206)</td><td>0.641**(0.202)</td><td>-2.837*(1.320)</td><td>-3.226***(0.793)</td><td>-3.461***(0.774)</td></tr><tr><td>Controls</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Log(PRICE)</td><td>0.209(0.290)</td><td>-0.311(0.317)</td><td>-0.268(0.270)</td><td>0.110(0.470)</td><td>0.399(0.774)</td><td>-0.535(0.619)</td></tr><tr><td>Log(RATING)</td><td>2.136(2.208)</td><td>0.789(2.422)</td><td>0.544(2.141)</td><td>4.561(18.595)</td><td>-6.578(4.376)</td><td>-6.744(4.850)</td></tr><tr><td>Control group</td><td>Runners-up</td><td>CEM</td><td>PSM</td><td>Runners-up</td><td>CEM</td><td>PSM</td></tr><tr><td>Estimator</td><td>Logit</td><td>Logit</td><td>Logit</td><td>Logit</td><td>Logit</td><td>Logit</td></tr><tr><td>Observations</td><td>5,131</td><td>8,414</td><td>8,126</td><td>5,131</td><td>8,414</td><td>8,126</td></tr></table>

Notes. Standard errors are given in parentheses. Observations are app-months. \*, \*\*, and \*\*\* indicate signi<sup>fi</sup>- cance at the 5%, 1%, and 0.1% levels, respectively.

Table 4. Hypothesis Tests: Hypotheses 2 and 3

<table><tr><td rowspan="2"></td><td colspan="3">MULTIHOMED</td><td colspan="3">CAT_NUMAPPS</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td rowspan="2">AFTER × AWARD</td><td>1.052*</td><td>1.012***</td><td>1.055***</td><td>0.062***</td><td>0.040***</td><td>0.057***</td></tr><tr><td>(0.486)</td><td>(0.274)</td><td>(0.277)</td><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td></tr><tr><td colspan="7">Controls</td></tr><tr><td rowspan="2">Log(PRICE)</td><td>0.489*</td><td>-0.238***</td><td>-0.103</td><td>-0.122***</td><td>0.177***</td><td>0.121***</td></tr><tr><td>(0.245)</td><td>(0.063)</td><td>(0.061)</td><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td></tr><tr><td rowspan="2">Log(RATING)</td><td>-4.444**</td><td>-0.500</td><td>0.074</td><td>0.131***</td><td>0.197***</td><td>0.113***</td></tr><tr><td>(1.725)</td><td>(0.380)</td><td>(0.441)</td><td>(0.001)</td><td>(0.000)</td><td>(0.000)</td></tr><tr><td>Control group</td><td>Runners-up</td><td>CEM</td><td>PSM</td><td>Runners-up</td><td>CEM</td><td>PSM</td></tr><tr><td>Estimator</td><td>Logit</td><td>Logit</td><td>Logit</td><td>Poisson</td><td>Poisson</td><td>Poisson</td></tr><tr><td>Observations</td><td>5,131</td><td>8,414</td><td>8,126</td><td>5,131</td><td>8,414</td><td>8,126</td></tr></table>

Notes. Standard errors are given in parentheses. Observations are app-months.  
\*, \*\*, and \*\*\* indicate signi<sup>fi</sup>cance at the 5%, 1%, and 0.1% levels, respectively.

4.2.2. Interview Evidence. To further investigate the model assumptions and tests, we report anecdotal evidence from the interviews with award winners. The interviews con<sup>fi</sup>rm that there is some unexpectedness in award-winning. For example, one interviewee stated that winning “was a surprise. [ … ] They certainly did not give us any indication that we would win anything.” Another interviewee said, “We had no idea we’d win it. [ … ] When the winner was announced we could hardly believe it.” Interviewed winners also stated that even after receiving the award, they were not sure of the exact criteria for award winning or nomination.

The interviews also provide support for Hypotheses 1 and 2. Asked about the business impact of the award, one interviewee said, “this major recognition helped us feel that we were on the right track, and it greatly boosted our con<sup>fi</sup>dence and productivity. [ … ] It was essential to stay aligned with [ … ] the overall trend.”

Table 5. Summary of Robustness Checks

<table><tr><td>Test</td><td>Result</td></tr><tr><td colspan="2">Assumption of parallel trends</td></tr><tr><td>Time trends</td><td>No significant difference between groups regarding time trends in the dependent variables</td></tr><tr><td>Relative time model</td><td>No evidence of significant pre-award differencesResults consistent with the hypotheses</td></tr><tr><td>Developer-specific time trend</td><td>Consistent results when including a developer-specific time trend</td></tr><tr><td>Interview evidence</td><td>Opaque selection process, “randomness” in award winningAwards are important for firm outcomes</td></tr><tr><td colspan="2">Sensitivity</td></tr><tr><td>Models without controls</td><td>Consistent results, larger effects for NEWAPP</td></tr><tr><td>Alternative estimator</td><td>Consistent results, effect for NEWAPP drops below the significance level</td></tr><tr><td>Alternative price controls</td><td>Consistent results</td></tr><tr><td colspan="2">Rival explanations</td></tr><tr><td>Nomination effects</td><td>No statistical evidence of a nomination effect on the dependent variables</td></tr><tr><td>H1—Alternative measure</td><td>Results consistent for minor updates</td></tr><tr><td>H1—Panel vector autoregression</td><td>On average, updates tend to reflect improvements: updates in t - 1 associated with improved app ratings in t</td></tr><tr><td>H3—Alternative measure</td><td>Results for H3 are consistent when using the cumulative number of apps</td></tr><tr><td>H3—Alternative control group</td><td>Consistent results</td></tr><tr><td>Placebo treatment</td><td>No indirect evidence of a false positive</td></tr><tr><td>Heterogeneity</td><td>Update-inducing effects of the award are weaker for larger firmsOlder apps are more likely to be multihomedApps by larger firms are more likely to be multihomed and updated</td></tr></table>

Notes. The table summarizes the robustness checks reported in the paper and in the online appendix along with their results. H1, Hypothesis 1; H3, Hypothesis 3.

Table 6. Tests for Parallel Trends

<table><tr><td></td><td>UPDATE(1)</td><td>NEWAPP(2)</td><td>CAT_NUMAPPS(3)</td><td>MULTIHOMED(4)</td><td>Log(PRICE)(5)</td><td>Log(RATING)(6)</td><td>Log(NUMRATINGS)(7)</td></tr><tr><td colspan="8">Panel A: Winners vs. runners-ups</td></tr><tr><td>Trend</td><td>0.022(0.155)</td><td>0.371(0.683)</td><td>0.013(0.055)</td><td>0.010(0.059)</td><td>-0.051(0.066)</td><td>0.002(0.004)</td><td>-0.069(0.247)</td></tr><tr><td>AWARD × Trend</td><td>0.030(0.312)</td><td>0.105(1.155)</td><td>-0.001(0.101)</td><td>0.019(0.123)</td><td>0.037(0.106)</td><td>-0.007(0.009)</td><td>-0.162(0.478)</td></tr><tr><td colspan="8">Panel B: Winners vs. CEM</td></tr><tr><td>Trend</td><td>0.528**(0.201)</td><td>-0.213(0.294)</td><td>0.024(0.040)</td><td>0.024(0.065)</td><td>0.015(0.062)</td><td>0.000(0.003)</td><td>0.035(0.205)</td></tr><tr><td>AWARD × Trend</td><td>-0.385(0.346)</td><td>0.548(0.735)</td><td>-0.013(0.096)</td><td>0.003(0.133)</td><td>-0.032(0.108)</td><td>-0.007(0.007)</td><td>-0.307(0.477)</td></tr><tr><td colspan="8">Panel C: Winners vs. PSM</td></tr><tr><td>Trend</td><td>0.646***(0.187)</td><td>0.077(0.269)</td><td>0.022(0.039)</td><td>0.023(0.064)</td><td>0.013(0.060)</td><td>0.000(0.003)</td><td>0.025(0.227)</td></tr><tr><td>AWARD × Trend</td><td>-0.503(0.338)</td><td>0.258(0.726)</td><td>-0.012(0.096)</td><td>0.005(0.132)</td><td>-0.030(0.107)</td><td>-0.006(0.007)</td><td>-0.297(0.487)</td></tr></table>

Notes. Binary dependent variables estimated with a conditional logit estimator. Observations are developer-months. Panel A is based on 336 obser vations, panel B is based on 354 observations, and panel C is based on 360 observations. The numbers of observations differ because the sample i restricted to pre-award period and on the developer level. Standard errors are in parentheses  
\*\* and \*\*\* indicate signi<sup>fi</sup>cance at the 1% and 0.1% levels, respectively.

4.2.3. Sensitivity. Online Appendix Table A4 reports tests for sensitivity. First, we estimate the plain models without controls. The results are consistent (panel A). Second, we estimate the models using ordinary least squares (OLS), and the hypotheses remain con<sup>fi</sup>rmed (panel B). The coef<sup>fi</sup>cient on NEWAPP drops below the signi<sup>fi</sup>cance level $( p = 0 . 0 5 6 )$ . Finally, we estimate the models using a different set of controls for app prices. In particular, we include a binary for whether an app offers in-app purchases (INAPP) or whether it charges an upfront price (HAS PRICE). The results are similar (panel C).

4.2.4. Rival Explanations. Table 8 reports tests for several rival explanations. First, we investigate whether the nomination itself invoked changes in product strategies. We therefore exclude winners from the sample and compare outcomes of runners-up to the matched control groups. In Table 8, columns (1) to (4) report the estimates. We do not observe signi<sup>fi</sup>cant effects of nomination.

Second, to address the concern that UPDATE only partially captures the improvements to an app, we estimate Equation (1) with UPD\_MINOR as the dependent variable. In Table 8, column (5) reports the results. We observe evidence in line with Hypothesis 1:

the odds of a minor app update are higher for recipients, yet the p-value is below conventional levels of signi<sup>fi</sup>cance (p 0.065).

Third, one of the assumptions of our theorizing is that updates are improvements. However, from a pure measurement perspective, updates capture changes but not whether users perceived those changes as an improvement. To further investigate whether updates are linked to improvements in app ratings, we implement a panel vector autoregression model (PVAR).<sup>6</sup> PVARs are a collection of models that capture dynamic effects between variables in time-series data. PVAR models are increasingly adopted in information systems (e.g., Chen et al. 2015). The intention of this analysis is not to reassess the effects of award winning, but to explore the relationship between updates and app ratings. Online Appendix B provides the technical details and results. An update in t 1 is associated with an increase in the average rating in t by 0.1%. This suggests that apps that received an update show a higher rating in the subsequent period. This corroborates the assumption that updates are product improvements.

Finally, we follow Bertrand et al. (2004) to assess the plausibility of false positives. We restrict the sample to the control group and then randomly assign a placebo AWARD variable to developers. Estimating Equation (1) with a randomly assigned placebo variable should not indicate any signi<sup>fi</sup>cant effect. In Table 8, columns (6) to (9) report the results. The effects are insigni<sup>fi</sup>cant, as expected.

Table 7. Relative-Time Estimation

<table><tr><td></td><td>UPDATE(1)</td><td>NEWAPP(2)</td><td>MULTIHOMED(3)</td><td>Log(CAT_NUMAPPS)(4)</td></tr><tr><td>Award [t-2]</td><td>0.058(0.083)</td><td>-0.050(0.030)</td><td>0.077(0.041)</td><td>0.008(0.016)</td></tr><tr><td>Award [t-1]</td><td>0.174(0.092)</td><td>0.006(0.030)</td><td>-0.016(0.045)</td><td>0.008(0.016)</td></tr><tr><td>Award t</td><td>Omitted</td><td>Omitted</td><td>Omitted</td><td>Omitted</td></tr><tr><td>Award [t+1]</td><td>-0.051(0.091)</td><td>-0.042(0.030)</td><td>-0.000(0.045)</td><td>0.020(0.015)</td></tr><tr><td>Award [t+2]</td><td>0.047(0.092)</td><td>-0.072*(0.030)</td><td>-0.067(0.045)</td><td>0.022(0.016)</td></tr><tr><td>Award [t+3]</td><td>0.228*(0.092)</td><td>-0.071*(0.030)</td><td>-0.080(0.045)</td><td>0.024(0.016)</td></tr><tr><td>Award [t+4]</td><td>0.191*(0.092)</td><td>-0.076*(0.030)</td><td>-0.091*(0.045)</td><td>0.023(0.015)</td></tr><tr><td>Award [t+5]</td><td>0.099(0.093)</td><td>-0.048(0.030)</td><td>-0.083(0.045)</td><td>0.029(0.016)</td></tr><tr><td>Award [t+6]</td><td>0.042(0.091)</td><td>-0.000(0.030)</td><td>0.043(0.045)</td><td>0.037*(0.015)</td></tr><tr><td>Award [t+7]</td><td>0.166(0.091)</td><td>-0.074*(0.030)</td><td>0.049(0.045)</td><td>0.052***(0.015)</td></tr><tr><td>Award [t+8]</td><td>0.148(0.094)</td><td>-0.039(0.031)</td><td>0.148**(0.046)</td><td>0.047**(0.016)</td></tr><tr><td>Control group Estimator</td><td>Runners-upOLS</td><td>Runners-upOLS</td><td>Runners-upOLS</td><td>Runners-upOLS</td></tr></table>

Notes. There are 5,131 app-month observations. Standard errors are given in parentheses.  
\*, \*\*, and \*\*\* indicate signi<sup>fi</sup>cance at the 5%, 1%, and 0.1% levels, respectively.

4.2.5. Sample Size and Statistical Power. Although our sample size is comparable to those of prior studies of awards (e.g., Kovacs and Sharkey´ 2014), it still represents a small sample. To help interpret the data, we conduct an ex post power simulation for our own sample size and compare it with other sample sizes, as applied, for instance, in Gubler et al. (2018). More speci<sup>fi</sup>cally, we randomly generate datasets, each with a structure identical to our panel and using the same ratio between treatment and control units. As minimum detectable effects, we take OLS estimates of Equation (1).

Online Appendix Figure A3 plots the power for different sample sizes and a signi<sup>fi</sup>cance level of 5%. The statistical power associated with our sample is above the conventional threshold of 0.8 for Hypothesis 2 (i.e., MUL-TIHOMED) and Hypothesis 3 (i.e., CAT\_NUMAPPS). For UPDATE, the power is 0.56, and a sample size of approximately 233 developers would be required to make a judgment of con<sup>fi</sup>dence above the conventional power threshold. For NEWAPP, the power is 0.67, and a sample of approximately 170 developers would be required for a judgment above the conventional power threshold. Nevertheless, it is important to consider the power for Hypothesis 1 in light of the fact that it was corroborated across different model speci<sup>fi</sup>cations, an alternative variable, and in interviews.

Table 8. Tests for Robustness and Rival Explanations

<table><tr><td rowspan="2"></td><td colspan="4">Nomination effects</td><td>Alternative measure</td><td colspan="4">Placebo test</td></tr><tr><td>UPDATE(1)</td><td>NEWAPP(2)</td><td>MULTI HOMED(3)</td><td>CAT_NUMAPPS(4)</td><td>UPD_MINOR(5)</td><td>UPDATE(6)</td><td>NEWAPP(7)</td><td>MULTIHOMED(8)</td><td>CAT_NUMAPPS(9)</td></tr><tr><td>AFTER × Nomination</td><td>-0.875(1.010)</td><td>1.306(0.940)</td><td>0.758(0.490)</td><td>0.029(0.073)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AFTER × AWARD</td><td></td><td></td><td></td><td></td><td>2.037(1.104)</td><td>0.668(0.369)</td><td>-0.001(0.610)</td><td>0.163(0.556)</td><td>-0.109(0.081)</td></tr><tr><td>Control groupEstimator</td><td>CEMLogit</td><td>CEMLogit</td><td>CEMLogit</td><td>CEMPoisson</td><td>Runners-upLogit</td><td>Logit</td><td>Logit</td><td>Logit</td><td>Poisson</td></tr></table>

Notes. Logit coef<sup>fi</sup>cients reported as log-odds. Standard errors are given in parentheses. Results are based on 5,131 app-month observations \*, \*\*, and \*\*\* indicate signi<sup>fi</sup>cance at the 5%, 1%, and 0.1% levels, respectively.

4.2.6. Heterogeneity: Influence of Firm Size and App Age. We conduct further exploratory analyses to investigate the in<sup>fl</sup>uence of <sup>fi</sup>rm size and app age. The effects are not straightforward to predict. On the one hand, small <sup>fi</sup>rms may have no hierarchies or procedures to follow. Therefore, they might be more agile and quicker to release updates. On the other hand, small <sup>fi</sup>rms might face resource constraints that may hamper a reallocation of product development efforts. Following a related line of arguments, one may expect heterogeneous effects regarding app age.

Online Appendix Table A6, panel A, explores the award effects conditional on <sup>fi</sup>rm size. The only signi<sup>fi</sup>- cant interaction we observe is the one concerning UP-DATE, meaning that the update-inducing effects of the award are weaker for larger <sup>fi</sup>rms. Panel B of Table A6 proceeds with the award effects conditional on app age. We do not observe heterogeneous effects along app age. Nevertheless, assessing heterogeneous effects comes at the expense of statistical power. Panel C of Table A6 estimates Equation (1) for UPDATE and MULTIHOMED without <sup>fi</sup>xed effects but with controls for <sup>fi</sup>rm size and app age.<sup>7</sup> The coef<sup>fi</sup>cient on the DID term remains positive and signi<sup>fi</sup>cant, which is consistent with our main estimation. Finally, Online Appendix Table A7 reports that the positive effects on UPDATE and MULTI-HOMED hold when the sample is restricted to young apps (i.e., below median app age) or apps of small <sup>fi</sup>rms (i.e., fewer than 50 employees), respectively.

## 5. Discussion

## 5.1. Main Findings

This study investigates the decision of platform <sup>fi</sup>rms to honor complementary innovation ex post with awards. In an empirical study of Google’s Android platform and the Google Play Award, we report three <sup>fi</sup>ndings. First, awards increase recipients’ likelihood of releasing complement improvements and decrease their likelihood of releasing new complements. Second, awards increase recipients’ likelihood of multihoming. Finally, awards encourage other complementors to release new complements in recipients’ market niches.

## 5.2. Theoretical Contributions

This study offers three theoretical contributions. First, this study contributes to research on platform governance by advancing our understanding of the mechanisms that in<sup>fl</sup>uence complementor behavior (Parker and Van Alstyne 2005, Parker et al. 2017). In particular, we add that a non-<sup>fi</sup>nancial mechanism which is relatively simple to implement—awards—may in<sup>fl</sup>uence complementors’ product development strategies. We observe three desirable and undesirable consequences for platform <sup>fi</sup>rms, further enriching our understanding of the mechanisms of platform governance and the complex decisions faced by platform <sup>fi</sup>rms. More generally, our <sup>fi</sup>ndings help in understanding the effectiveness of soft governance mechanisms.

Second, this study contributes to the growing literature on awards (Kovacs and Sharkey´ 2014, Gallus and Frey 2016, Frey and Gallus 2017), particularly the literature that has studied awards in online communities (e.g., Gallus 2016, Chen et al. 2010, Burtch et al. 2021). We add to the understanding of the consequences of awards, especially how a <sup>fi</sup>rm’s receipt of an award is linked to its choice of different product strategies. More importantly, our <sup>fi</sup>ndings provide evidence that awards honoring outstanding product developments can disincentivize new product development and incentivize the release of product improvements and multihoming.

Finally, this study adds to the extant body of knowledge studying complementors’ product strategies (Tiwana 2015, Cennamo et al. 2018). We contribute by observing that complementors’ product strategies may be driven by the receipt of an award. More broadly, our <sup>fi</sup>ndings suggest that complementors’ ability to signal product quality may be linked to a greater focus on updating. In addition, our study integrates three different software product strategies, namely, complement improvements, new complement releases, and multihoming.

## 5.3. Research Implications and Future Work

Our <sup>fi</sup>ndings offer several theoretical implications. For research on platform governance, the puzzling question that emerges from our work is whether award recipients’ focus on updates provides value to the platform owner. Recipients’ shift toward releasing improvements might have direct positive impacts on the platform owner by promoting improvement without requiring coordination or resources (e.g., Wareham et al. 2014, Huber et al. 2017). The shift toward updates might have even more direct impacts on value if the platform owner can participate the recipient’s success (e.g., via transaction fees or in-app sales) and if this value exceeds that obtained from a more even demand distribution.

The <sup>fi</sup>nding that awarded complementors are more likely to multihome is novel when considered in the light of recent empirical studies which observed that platform participants are more loyal the higher their past success and activity on a platform (Koh and Fichman 2014). These differences may be related to the type of platform exchange studied, for which our data do not permit further investigation.

The observation that more new complements were released in the recipients’ market is novel in the light of the literature on entry deterrence by established <sup>fi</sup>rms (e.g., Goolsbee and Syverson 2008) and recent empirical studies on platforms. One may argue that award winners may obtain a competitive advantage that deters entry by rival complementors. One explanation that may reconcile these different arguments is that complementors still expect greater opportunities from entering (e.g., Liang et al. 2019). If so, our <sup>fi</sup>ndings indicate the strength of the signal emitted by an award.

## 5.4. Managerial Implications

Firms can directly bene<sup>fi</sup>t from the analyses presented in this study. First, this study has implications for platform <sup>fi</sup>rms that are interested in utilizing awards as a governance mechanism on their platforms. This study’s results suggest that awards do have signi<sup>fi</sup>- cant effects on complementors’ behavior despite representing only symbolic and non-<sup>fi</sup>nancial mechanisms. Managers should consider the <sup>fl</sup>exibility of awards as a particular strength of the mechanism. The precise information conveyed through the award is at the discretion of the platform owner. The platform owner has full freedom in signaling ex post whatever outcome is most valuable. An award can, for instance, be given to “the most innovative complement” with no need to de<sup>fi</sup>ne the criteria exactly. Thus, awards re-<sup>fl</sup>ect an instrument for platform owners to in<sup>fl</sup>uence the behavior of the recipient and the ecosystem, especially in cases where owners are unable or unwilling to specify desired outcomes. This represents an important capability of digital business strategy (e.g., Park and Mithas 2020).

Nevertheless, managers should be aware that awards are complex mechanisms and therefore require a careful evaluation of whether their effects are desirable. On the one hand, awards may be an instrument to incentivize improvement in a particular complement. Moreover, awards boost the development of new complements in the niche market targeted by the award. Therefore, platform <sup>fi</sup>rms may use awards as a strategic instrument to guide complementors’ attention toward a certain market niche. On the other hand, awards can encourage multihoming, potentially by providing additional resources through demand increases, but also by increasing competing platform <sup>fi</sup>rms’ awareness of promising potential complementors. After all, awards may increase the transparency of complementor performance beyond the boundaries of the platform. Which of these effects prevail is a question that our study cannot address, and one that likely depends on the particular platform. Thus, one recommendation for platform <sup>fi</sup>rms is to employ additional mechanisms to increase recipients’ loyalty to the platform, for example, through contractual exclusivity arrangements.

Second, this study has managerial implications for complementors. These <sup>fi</sup>rms typically “swim with sharks,” facing high competitive pressure both from other complementors and from appropriation or “Sherlocking” by platform owners (e.g., The Economist 2012). The <sup>fi</sup>ndings of our study suggest that awards may represent both an opportunity and a challenge for the complementors who receive them. On the one hand, awards provide these <sup>fi</sup>rms with elevated status, which helps them gain visibility among their consumers, reduce transaction costs, and diversify on competing platforms. This may help complementors recoup their investments into costly complement development and enable improvement strategies.

On the other hand, recipients should be careful not to overstate the potential advantages of an award. As our study indicates, awards may attract the entry of other complementors. Eventually, recipients may face increased competition through having more “sharks” in the tank. In addition, other complementors, or the platform owner, may feel encouraged to challenge award winners and engage in competitive attacks. Therefore, multihoming could be caused by a desire to escape niche competition. It may be crucial for award recipients to leverage their signaling advantages on a rival platform to mitigate the increased competitive risks. Award recipients may demand exclusivity fees from the focal platform owner to not multihome, giving them even greater advantages over rivals.

## 5.5. Limitations

We cannot fully rule out confounding effects or omitted variables. Although the analyses did not support pre-existing differences, winners and runners-up may differ in characteristics that we were unable to observe. Also, Google may have selected award winners because they expected exactly those <sup>fi</sup>rms to focus on complement improvements. Our research may not account for this possibility. We also acknowledge that our research design is constrained by its sample size. Our power analysis provides a starting point for the design of future studies of awards.

## 6. Conclusion

We investigated the effects of platform <sup>fi</sup>rms’ choices when conferring retrospective awards on complementors. In an empirical study of Google’s Android platform, we found both desirable and undesirable outcomes for platform <sup>fi</sup>rms. The award increased recipients’ release of complement improvements as well as the overall number of apps released in the recipients’ market niche. However, the award also increased recipients’ likelihood of multihoming.

## Acknowledgments

The authors thank Senior Editor Ola Henfridsson, Associate Editor Yili (Kevin) Hong, and the anonymous reviewers, as well as participants at the 2018 International Conference on Information Systems, at the 2018 ZEW Conference on Information and Communication Technologies, and in seminars at the University of Hohenheim, University of Mannheim, University of Minnesota, University of Arkansas, and Technical University of Munich. They especially thank Marshall van Alstyne and Chris Forman for helpful comments. They are grateful to Okan Aydingul for his outstanding assistance with data collec-¨ tion. An early version appeared in the 2018 proceedings of the International Conference on Information Systems as “App Superstars: Are High-Status Complementors a Sustained Source of Innovation in Platform Ecosystems?”

## Endnotes

<sup>1</sup>Anecdotal evidence bears out this claim. Winners announce the award on their website or display it in the Google Play Store (see Online Appendix Figure A1). News media report the awards. The conferral of the award during the developer conference makes winners highly visible. Only a tiny fraction of the hundreds of thousands of mobile app developers receive the award. Interviewees described the award as a “validator to be recognized by your peers” and reported that “the breakthrough ... came with [the app] receiving the Google Play Award.”

<sup>2</sup>We use the term bad controls to refer to variables that “might just as well be dependent variables too” (Angrist and Pischke 2009, p. 64). In our case, CAT\_NUMAPPS might be a bad control because, as suggested in Hypothesis 1, award winning is likely to reduce complementors’ focus on new complement development. In addition, the number of ratings is likely to be a bad control because awards increase the overall attention to an app.

<sup>3</sup>We thank an anonymous reviewer for this suggestion.

<sup>4</sup>We thank an anonymous reviewer for suggesting this approach.

<sup>5</sup>For fixed-effects logit models, Monte Carlo studies (e.g., Greene 2003, p. 690) have shown that bias due to the incidental parameters problem is large when the number of observations per group is small. Greene’s (2003) conclusions were based on simulations with a panel length of 2 to 20 periods, which is similar to ours. Given that a logit estimation can be problematic in the presence of many interaction terms and fixed effects as caused by the additional trends, we follow the recommendations and use OLS (i.e., a linear probability model) for estimation.

<sup>6</sup>We thank the review panel for the idea to use a PVAR.

<sup>7</sup>We make further observations. Older apps are more likely to be multihomed, potentially because they have proved to be successful. Apps by larger firms are more likely to be multihomed and updated, potentially because of the greater resources available. We thank an anonymous reviewer for this suggestion.

## References

Anand N, Watson MR (2004) Tournament rituals in the evolution of <sup>fi</sup>elds: The case of the Grammy Awards. Acad. Management J. 47(1):59–80.

Anderson EG, Parker GG, Tan B (2014) Platform performance investment in the presence of network externalities. Inform. Systems Res. 25(1):152–172.

Android Developers (2020) Android versioning. Retrieved January 1, 2020, https://developerandroid.com/studio/publish/versioning.

Angrist JD, Pischke JS (2009) Mostly Harmless Econometrics: An Empiricist’s Companion (Princeton University Press, Princeton, NJ).

Bakos Y, Halaburda H (2020) Platform competition with multi-homing on both sides: Subsidize or not? Management Sci. 66(12):5599–5607.

Banker RD, Davis GB, Slaughter SA (1998) Software development practices, software complexity, and software maintenance performance: A <sup>fi</sup>eld study. Management Sci. 44(4):433–450.

Bertrand M, Du<sup>fl</sup>o E, Mullainathan S (2004) How much should we trust differences-in-differences estimates? Quart. J. Econom. 119(1):249–275.

Bhargava HK, Kim BC, Sun D (2013) Commercialization of platform technologies: Launch timing and versioning strategy. Production Oper. Management 22(6):1374–1388.

Bhargava HK, Csapo G, M´ uller R (2020) On optimal auctions for¨ mixing exclusive and shared matching in platforms. Management Sci. 66(6):2653–2676.

Boudreau KJ, Hagiu A (2009) Platform rules: Multi-sided platforms as regulators. Gawer A, ed. Platforms, Markets and Innovation (Edward Elgar Publishing, Cheltenham, UK), 163–191.

Boudreau K (2010) Open platform strategies and innovation: Granting access vs. devolving control. Management Sci. 56(10):1849–1872.

Boudreau K (2012) Let a thousand <sup>fl</sup>owers bloom? An early look at large numbers of software app developers and patterns of innovation. Organ. Sci. 23(5):1409–1427.

Brandenburger AM, Nalebuff BJ (1996) Co-Opetition (Doubleday, New York).

Brown SL, Eisenhardt KM (1995) Product development: Past research, present <sup>fi</sup>ndings, and future directions. Acad. Management Rev. 20(2):343–378.

Brown SL, Eisenhardt KM (1997) The art of continuous change: Linking complexity theory and time-paced evolution in relentlessly shifting organizations. Admin. Sci. Quart. 42(1):1–34.

Burtch G, Hong Y, Bapna R, Griskevicius V (2018) Stimulating online reviews by combining <sup>fi</sup>nancial incentives and social norms. Management Sci. 64(5):2065–2082.

Burtch G, He Q, Hong Y, Lee D (2021) How do peer awards motivate creative content? Experimental evidence from Reddit. Management Sci. Forthcoming.

Caillaud B, Jullien B (2003) Chicken & egg: Competition among intermediation service providers. RAND J. Econom. 34(2):309–328.

Cavusoglu H, Cavusoglu H, Zhang J (2008) Security patch management: Share the burden or share the damage? Management Sci. 54(4):657–670.

Ceccagnoli M, Forman C, Huang P, Wu DJ (2012) Cocreation of value in a platform ecosystem: The case of enterprise software. MIS Quart. 36(1):263–290.

Cennamo C, Ozalp H, Kretschmer T (2018) Platform architecture, multihoming and complement quality: Evidence from the U.S. video game industry. Inform. Systems Res. 29(2):461–478.

Chen H, De P, Hu YJ (2015) IT-enabled broadcasting in social media: An empirical study of artists’ activities and music sales. Inform. Systems Res. 26(3):513–531.

Chen IJ, Hsu PH, Of<sup>fi</sup>cer MS, Wang Y (2020) The Oscar goes to … : High-tech <sup>fi</sup>rms’ acquisitions in response to rivals’ technology breakthroughs. Res. Policy 49(7)104078.

Chen L, Zhan MS, Raghu TS (2019) The Spillover of Spotlight: Platform recommendation in the mobile app market. Inform. Systems Res. 30(4):1296–1318.

Chen Y, Harper FM, Konstan J, Xin Li SX (2010) Social comparisons and contributions to online communities: A feld experiment on MovieLens. Amer. Econom. Rev. 100(4):1658–1698.

Claussen J, Kretschmer T, Mayrhofer P (2013) The effects of rewarding user engagement: The case of facebook apps. Inform. Systems Res. 24(1):186–200.

Clements MT, Ohashi H (2005) Indirect network effects and the product cycle: Video games in the US, 1994–2002. J. Indust. Econom. 53(4):515–542.

Connelly BL, Certo ST, Ireland RD, Reutzel CR (2011) Signaling theory: A review and assessment. J. Management 37(1):39–67.

Constantinides P, Henfridsson O, Parker GG (2018) Introduction— Platforms and infrastructures in the digital age. Inform. Systems Res. 29(2):381–400.

Corts KS, Lederman M (2009) Software exclusivity and the scope of indirect network effects in the US home video game market. Internat. J. Indust. Organ. 27(2):121–136.

Dimoka A, Hong Y, Pavlou PA (2012) On product uncertainty in online markets: Theory and evidence. MIS Quart. 36(2):395–426.

Economist, The (2012) You’ve been sherlocked. The Economist (July 13) https://www.economist.com/babbage/2012/07/13/ youve-been-sherlocked.

Farrell J, Shapiro C (1988) Dynamic competition with switching costs. RAND J. Econom. 19(1):123–137.

Foerderer J (2020) Inter<sup>fi</sup>rm exchange and innovation in platform ecosystems: Evidence from Apple’s worldwide developers conference. Management Sci. 66(10):4772–4787.

Foerderer J, Kude T, Schuetz SW, Heinzl A (2019) Knowledge boundaries in enterprise software platform development: Antecedents and consequences for platform governance. Inform. Systems J. 29(1):119–144.

Foerderer J, Mithas S, Kude T, Heinzl A (2018) Does platform owner’s entry crowd out innovation? Evidence from Google photos. Inform. Systems Res. 29(2):444–460.

Frey BS, Gallus J (2017) Towards an economics of awards. J. Econom. Survey 31(1):190–200.

Gallus J (2016) Fostering public good contributions with symbolic awards: A large-scale natural <sup>fi</sup>eld experiment at Wikipedia. Management Sci. 63(12):3999–4015.

Gallus J, Frey BS (2016) Awards: A strategic management perspective. Strategic Management J. 37(8):1699–1714.

Gallus J, Frey BS (2017) Honours versus money: The economics of awards. J. Econom. Surveys (Oxford University Press, Oxford).

Garg R, Telang R (2013) Inferring app demand from publicly available data. MIS Quart. 37(4):1253–1264.

Ghazawneh A, Henfridsson O (2013) Balancing platform control and external contribution in third-party development: The boundary resources model. Inform. Systems J. 23(2):173–192.

Ghose A, Ipeirotis PG, Li B (2012) Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content. Marketing Sci. 31(3):493–520.

Google (2016) The Google Play Awards coming to Google I/O. Accessed January 1, 2020, https://android-developers.googleblog. com/2016/04/the-google-play-awards-coming-to-google.html.

Google (2019) And the 2019 Google Play Award nominees are … .” Retrieved January 1, 2020, https://android-developers.googleblog. com/2019/04/and-2019-google-play-award-nominees-are.html.

Goolsbee A, Syverson C (2008) How do incumbents respond to the threat of entry? Evidence from the major airlines. Quart. J. Econom. 123(4):1611–1633.

Greene WH (2003) Econometric Analysis (Prentice Hall, Upper Saddle River, NJ).

Greenwood BN, Wattal S (2017) Show me the way to go home: An empirical investigation of ride-sharing and alcohol related motor vehicle fatalities. MIS Quart. 41(1):163–187.

Gubler T, Larkin I, Pierce L (2016) Motivational spillovers from awards: Crowding out in a multitasking environment. Organ. Sci. 27(2):286–303.

Gubler T, Larkin I, Pierce L (2018) Doing well by making well: The impact of corporate wellness programs on employee productivity. Management Sci. 64(11):4967–4987.

Hagiu A (2006) Pricing and commitment in two-sided platforms. RAND J. Econom. 37(3):720–737.

Hagiu A, Spulber D (2013) First-party content and coordination in two-sided markets. Management Sci. 59(4):933–949.

Halaburda H, Jan Piskorski M, Yıldırım P (2018) Competing by restricting choice: The case of matching platforms. Management Sci. 64(8):3574–3594.

Hendricks KB, Singhal VR (1996) Quality awards and the market value of the <sup>fi</sup>rm: An empirical investigation. Management Sci. 42(3):415–436.

Ho-Dac NN, Kumar M, Slotegraaf RJ (2020) Using product development information to spur the adoption of continuous improvement products. J. Acad. Marketing Sci. 48(6):1156–1173.

Huang P, Mithas S, Tafti A (2018) Platform sponsor’s investments and user contributions in knowledge communities: The role of knowledge seeding. MIS Quart. 42(1):213–240.

Huber T, Kude T, Dibbern J (2017) Governance practices in platform ecosystems: Navigating tensions between co-created value and governance costs. Inform. Systems Res. 28(3):563–584.

Hukal P, Henfridsson O, Shaikh M, Parker G (2020) Platform signaling for generating platform content. MIS Quart. 44(3): 1177–1205.

Iacus SM, King G, Porro G, Katz JN (2012) Causal inference without balance checking: Coarsened exact matching. Political Anal. 20(1):1–24.

Jensen MC, Meckling WH (1976) Theory of the <sup>fi</sup>rm: Managerial behavior, agency costs and ownership structure. J. Financial Econom. 3(4):305–360.

Jullien B, Pavan A (2019) Information management and pricing in platform markets. Rev. Econom. Stud. 86(4):1666–1703.

Kang C, Aaltonen A, Henfridsson O (2019) The impact of platform entry strategies on the quality of complements in multihoming. Proc. 40th Internat. Conf. Inform. Systems (ICIS, Munich, Germary).

Koh TK, Fichman M (2014) Multihoming users’ preferences for twosided exchange networks. MIS Quart. 38(4):977–996.

Kosfeld M, Neckermann S (2011) Getting more work for nothing? Symbolic awards and worker performance. Amer. Econom. J. Microeconom. 3(3):86–99.

Kovacs B, Sharkey AJ (2014) The paradox of publicity: How awards´ can negatively affect the evaluation of quality. Admin. Sci. Quart. 59(1):1–33.

Krishnan V, Ramachandran K (2011) Integrated product architecture and pricing for managing sequential innovation. Management Sci. 57(11):2040–2053.

Landsman V, Stremersch S (2011) Multihoming in two-sided markets: An empirical inquiry in the video game console industry. J. Marketing 75(6):39–54.

Lee RS (2013) Vertical integration and exclusivity in platform and two-sided markets. Amer. Econom. Rev. 103(7):2960–3000.

Lee G, Raghu TS (2014) Determinants of mobile apps’ success: Evidence from the app store market. J. Management Inform. Systems 31(2):133–170.

Li H, Zhu F (2020) Information transparency, multi-homing, and platform competition: A natural experiment in the daily deals market. Management Sci., ePub ahead of print October 7, https://doi.org/10.1287/mnsc.2020.3718.

Li J, Shi W, Connelly B, Yi X, Qin X (2020) CEO awards and <sup>fi</sup>nancial misconduct. J. Management, ePub ahead of print, https:// doi.org/10.1177/0149206320921438.

Luca M, Zervas G (2016) Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Sci. 62(12):3412–3427.

Nowlis SM, Simonson I (1996) The effect of new product features on brand choice. J. Marketing Res. 33(1):36–46.

Park Y, Mithas S (2020) Organized complexity of digital business strategy: A con<sup>fi</sup>gurational perspective. MIS Quart. 44(1):85–127.

Parker G, Van Alstyne MW (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10):1494–1504.

Parker G, Van Alstyne MW (2018) Innovation, openness, and platform control. Management Sci. 64(7):3015–3032.

Parker G, Van Alstyne MW, Jiang X (2017) Platform ecosystems: How developers invert the <sup>fi</sup>rm. MIS Quart. 41(1):255–266.

Rietveld J, Eggers JP (2018) Demand heterogeneity in platform markets: Implications for complementors. Organ. Sci. 29(2):304–322.

Rietveld J, Schilling MA, Bellavitis C (2019) Platform strategy: Managing ecosystem value through selective promotion of comple ments. Organ. Sci. 30(6):1232–1251.

Robinson CD, Gallus J, Lee MG, Rogers T (2021) The demotivating effect (and unintended message) of awards. Organ. Behav. Hu man Decision Processes. 32(1):iii–vi.

Rosenbaum PR, Rubin DB (1983) The central role of the propensity score in observational studies for causal effects. Biometrika 70(1):41–55.

Rothaermel FT, Deeds DL (2004) Exploration and exploitation alliances in biotechnology: A system of new product development. Strategic Management J. 25(3):201–221.

Song W, Chen J, Li W (2020) Spillover effect of consumer awareness on third parties’ selling strategies and retailers’ platform openness. Inform. Systems Res. 32(1):iii–vi.

Sorenson O (2000) Letting the market work for you: An evolutionary perspective on product strategy. Strategic Management J. 21(5):577–592.

Spence M (1973) Job market signaling. Quart. J. Econom. 87(3):355–374.

Stiglitz JE (2000) The contributions of the economics of information to twentieth century economics. Quart. J. Econom. 115(4):1441–1478.

Tanriverdi Hn, Lee CH (2008) Within-industry diversi<sup>fi</sup>cation and <sup>fi</sup>rm performance in the presence of network externalities: Evidence from the software industry. Acad. Management J. 51(2):381–397.

Tiwana A (2015) Evolutionary competition in platform ecosystems. Inform. Systems Res. 26(2):266–281.

Tiwana A, Konsynski B, Bush AA (2010) Platform evolution: Coevolution of platform architecture, governance, and environmental dynamics. Inform. Systems Res. 21(4):675–687.

Venkataraman V, Ceccagnoli M, Forman C (2018) Multihoming within platform ecosystems: The strategic role of human capital. Research Paper No. 18-8, Scheller College of Business, Georgia Institute of Technology, Atlanta.

Voss GB, Sirdeshmukh D, Voss ZG (2008) The effects of slack resources and environmental threat on product exploration and exploitation. Acad. Management J. 51(1):147–164.

Wang Q, Li B, Singh PV (2018) Copycats vs. original mobile apps: A machine learning copycat-detection method and empirical analysis. Inform. Systems Res. 29(2):273–291.

Wareham J, Fox PB, Cano Giner JL (2014) Technology ecosystem governance. Organ. Sci. 25(4):1195–1215.

Xue L, Song P, Rai A, Zhang C, Zhao X (2019) Implications of application programming interfaces for third-party new app development and copycatting. Production Oper. Management 28(8): 1887–1902.

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
