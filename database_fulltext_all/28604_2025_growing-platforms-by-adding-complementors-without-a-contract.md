---
otero_id: 28604
otero_key: "EEGYEBDP"
title: "Growing Platforms by Adding Complementors Without a Contract"
authors: "Raveesh Mayya; Zhuoxin Li"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0237"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Growing Platforms by Adding Complementors Without a Contract

Raveesh Mayya,<sup>a,</sup>\* Zhuoxin Li<sup>b</sup>

<sup>a</sup> Leonard N. Stern School of Business, New York University, New York, New York 10012; <sup>b</sup> Wisconsin School of Business, University of Wisconsin–Madison, Madison, Wisconsin 53706

\*Corresponding author

Contact: raveesh@stern.nyu.edu, https://orcid.org/0000-0003-1248-712X (RM); allen.li@wisc.edu, https://orcid.org/0000-0002-4687-4913 (ZL)

Received: April 21, 2023 Revised: May 24, 2024; July 26, 2024 Accepted: August 24, 2024 Published Online in Articles in Advance: February 20, 2025

https://doi.org/10.1287/isre.2023.0237

Copyright: © 2025 The Author(s)

Abstract. Multisided platforms often pursue growth strategies of expanding participants on one side (e.g., suppliers) and leveraging the cross-side network effect to attract participants on other sides (e.g., consumers). Whereas formal contractual agreements have traditionally been the norm for onboarding suppliers, an emerging trend involves platforms enabling consumers to interact with noncontracted suppliers via third-party enablers with both sharing profits from providing complementary services. This study examines this strategy of increasing market thickness in the context of food delivery platforms, focusing on the platforms’ inclusion of restaurants as “nonpartnered” restaurants. Nonpartnered restaurants do not pay commission fees for being listed on the platforms and do not control their menu or item prices. The platforms collect and transfer consumer orders to the thirdparty deliverers who place the order, pick it up, and deliver the food to consumers. The strategy has drawn regulatory scrutiny regarding its potential harm to nonpartnered restaurants and consumers. This research empirically investigates the impact of this noncontracted partnership on restaurants, leveraging two natural experiments: (1) a number of nonpartnered restaurants were listed on the platform, and (2) the restaurants were later delisted because of a governmental regulation. Our findings show that being added as a nonpartnered restaurant increases these restaurants’ revenue from takeout orders by about \$1,410 per month. Adding nonpartnered restaurants also has a positive spillover effect on the revenue of partnered restaurants already on the platform. Finally, the delisting of nonpartnered restaurants leads to a drop in their takeout orders as well as a negative spillover on the revenue of partnered restaurants. In essence, a nonpartnered contract benefits most restaurants, especially independent restaurants. These insights can inform the design of platform and regulatory policies related to noncontracted growth strategies.

History: Hsing Kenneth Cheng, Senior Editor; Gordon Burtch, Associate Editor.

Open Access Statement: This work is licensed under a Creative Commons Attribution 4.0 Internationa License. You are free to copy, distribute, transmit and adapt this work, but you must attribute this work as “Information Systems Research. Copyright © 2025 The Author(s). https://doi.org/10.1287/ isre.2023.0237, used under a Creative Commons Attribution License: https://creativecommons.org/ licenses/by/4.0/.”

Funding: Authors acknowledge the financial support of NET Institute [Grant 21-14]. Z. Li is grateful to the National Science Foundation Division of Social and Economic Sciences for support provided through the CAREER award [Grant 2243736].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.0237.

Keywords: multisided platform • market thickness • on-demand delivery • network effects • regulation • seeding • platform policy

## 1. Introduction

The rise of online intermediaries and digital marketplaces across almost every industry has raised questions about the sustainability of platform business models. Many platforms now face the challenges of continuing to expand their networks through the traditional, organic approach. Given the strong network effects and the tendency for digital markets to exhibit a winnertake-all dynamic (McAfee and Brynjolfsson 2008), exploring alternative growth strategies becomes crucial for the platforms to succeed.

To address slow organic growth, platforms have embarked on novel strategies, by which they enable third parties to insert themselves and facilitate trade with noncontracted businesses. These third parties leverage their reputation to provide complementary services, generating revenue in the process. This initiative reflects a burgeoning trend by which intermediaries on platforms facilitate transactions without formal agreements with supply-side entities. For example, hyperlocal courier services, such as Swiggy in India, enable deliverers to pick up items from any retail store regardless of whether the store has partnered with the platform.<sup>1</sup> Similarly, services such as TaskRabbit and PostMates in the United States empower taskers to complete tasks by picking up items from establishments without formal partnerships. In the hospitality sector, Airbnb Experiences connects travelers with local experience providers (e.g., tour guides), who might patronize restaurants or attractions not officially affiliated with Airbnb. Additionally, YouTubers might review products without direct partnerships with manufacturers, further exemplifying this trend of leveraging noncontracted businesses for content and revenue generation.

Noncontracted partnerships can offer strategic advantages in certain industries, particularly when the costs or efforts of establishing formal partnerships are not negligible, whereas the benefits are not immediately clear. In these settings, consumers may value the variety of selection, creating opportunities for the third-party enablers under the platform’s direct oversight to profitably facilitate transactions with suppliers without formal contracts. This model seems particularly appealing in sectors such as food delivery, in which platforms can leverage this strategy to cater to consumers’ diverse culinary preferences without formal partnerships with every restaurant.

On-demand food delivery platforms, such as Door-Dash, Grubhub, and UberEats, connect independent drivers with restaurants to fulfill food delivery orders placed by consumers through the platforms (Li and Wang 2024b). Maintaining visibility on these food delivery platforms by signing contractual agreements comes with both costs and benefits. Whereas some restaurants credit their survival to delivery platforms,<sup>2</sup> others are ambivalent about whether the benefits outweigh the commission fees charged by the platforms (McCart 2019)<sup>3</sup>; nonetheless, they recognize the potential downsides of being absent on these platforms (Ahuja et al. 2021).

A recent attempt by food delivery platforms to provide more restaurant selection for consumers has been to list nonpartnered restaurants<sup>4</sup> on their platforms. Grubhub, for instance, added 150,000 nonpartnered restaurants in the last quarter of 2019.<sup>5</sup> Proponents of this strategy argue that this benefits all parties involved: consumers benefit from a wider selection of restaurants, and nonpartnered restaurants benefit from increased visibility and a new channel to serve consumers.<sup>6</sup> Despite its potential benefits, this strategy has faced criticism from some restaurants because of outdated menu prices, incorrect order handling, and poor resultant ratings, thereby attracting regulatory scrutiny. For instance, California has prohibited delivery platforms from adding nonpartnered restaurants and has forced the platforms to delist the already listed ones.

The listing and delisting of nonpartnered restaurants provide a unique empirical setting to explore not only the economics of noncontracted partnerships, but also the interplay between platform strategies, externalities, and regulatory responses in the swiftly evolving food delivery industry. Extant literature does not offer a clear prediction on the impact of noncontracted relationships on restaurants. Studies on growth strategies in twosided networks (e.g., Rochet and Tirole 2003, Parker and Van Alstyne 2005, Economides and Viard 2006, Boudreau 2010, Zhu and Iansiti 2012) highlight the impor tance of using levers, such as price, quality, platform openness, and entry decisions, to expand the platform.

However, the strategy of including noncontracted passive participants on the platform, which already has active contracted partners, has not been empirically investigated (Feldman et al. 2023). To understand how an exogenous increase in the supply of restaurants alters platform competition and externalities, this research aims to address the following two questions: (1) How does adding restaurants to delivery platforms without a formal contract affect these restaurants? (2) How does adding nonpartnered restaurants impact partnered restaurants already on the platforms?

We answer these research questions using a comprehensive restaurant data set spanning three neighboring states—California, Oregon, and Washington—that share similar economic profiles, regulatory environments, and consumer behaviors in the gig economy.<sup>7</sup> Our empirical strategy exploits two exogenous shocks to restaurants: (1) Grubhub’s unilateral addition of nonpartnered restaurants to its platform in late 2019, and (2) California’s subsequent ban on this practice in late 2020. We investigate the changes in consumer demand and revenue for nonpartnered restaurants following their inclusion on the platform, examine the spillover effects on existing partnered restaurants, and evaluate the consequences of delisting nonpartnered restaurants in Cali fornia following the regulatory intervention.

Our empirical analysis shows that, when restaurants were added to the Grubhub platform without a formal partnership, takeout visits to these restaurants increased by 41.02 per month, translating to about \$1,409.96 monthly revenue at an average order size of \$34.37 (Circuit 2022). This increase in takeout orders was particularly significant for independent restaurants, suggesting that noncontracted partnerships can help these restaurants reach new customers without incurring platform commission fees, particularly those with limited advertising budgets and resources. Mechanism analysis suggests that the impact of nonpartnered relationships on restaurant revenue varied based on their takeout readiness prior to being listed. Restaurants with a high existing takeout volume had already invested in infrastructure to accommodate increased demand but had opted out of platform partnerships because of the prohibitive commission fees. For such restaurants, a noncontracted relationship led to an average monthly revenue increase of \$6,238.97. We also find positive spillover effects on partnered restaurants on the platform, resulting in a revenue increase of \$2,430. However, these benefits for both nonpartnered and partnered restaurants were partially reversed following Californian regulation that led to the delisting of nonpartnered restaurants. Overall, these findings imply that noncontracted partnerships positively impact most restaurants; however, regulatory interventions may have the unintended consequences of curtailing restaurants’ choice of staying on the platform as nonpartners.

This research makes several contributions to the understanding and strategic analysis of noncontracted partnerships, a novel phenomenon in the gig economy. We provide empirical evidence on the benefits of such partnerships for both nonpartnered and partnered restaurants on the platform. Given that network effects are heterogeneous and context-specific (Zhu and Iansit 2019), we demonstrate that the positive cross-side network effects of including nonpartnered restaurants outweigh the negative competition effects. This result challenges traditional platform strategies that focus solely on boosting the number of active suppliers. Next, our findings show that independent restaurants are the main beneficiaries of flexible noncontracted partnerships. The finding aligns with prior studies across sectors such as restaurants, gyms, and stores, highlighting the differential effects of platform policies on chain versus independent businesses and the unique strategic considerations for independent establishments facing digital transformation and regulatory changes (De Vaan et al. 2021, Le Bot et al. 2023). We also further the knowledge on the interplay between private platform policies and public regulatory policies by illustrating how digital marketplaces navigate recent regulatory efforts. Our analysis reveals how a regulatory attempt that aim to protect businesses may inadvertently harm them as noted by De Vaan et al. (2021) and Li and Wang (2024b). By aligning our study with lessons across industries, our paper offers new insights into the challenges and opportunities presented by digital platforms to thirdparty stakeholders, focusing on the resilience and adaptive strategies of independent entities in contrast to their chain counterparts.

## 2. Related Literature

This research builds on and contributes to the literature on delivery platforms’ impact on restaurants (e.g.,

Zhang et al. 2019; Raj et al. 2020; Li and Wang 2024a, b) as well as the literature on multisided platforms, specifi cally concerning intraplatform competition and platform governance in the presence of network effects (e.g., Rochet and Tirole 2003, Parker and Van Alstyne 2005, Boudreau and Hagiu 2009, Zhu and Iansiti 2012, Cohen and Sundararajan 2015, Cusumano et al. 2021). To place our contributions in perspective, this section reviews the relevant literature, identifies gaps, and motivates our research questions.

## 2.1. Delivery Platforms and Restaurant Partnership

Joining delivery platforms may affect a restaurant’s sales, profits, and survival. For instance, Li and Wang (2024a) find that a formal partnership with a delivery platform can improve outcomes for restaurants, espe cially for chain restaurants. Others note the long-term benefits of joining platforms, such as increasing online and off-line sales, enhancing the survival chances of small restaurants, and retaining existing customers and acquiring new ones in a competitive environment (Zhang et al. 2019, Raj et al. 2020). However, the literature also highlights the costs associated with partnering with delivery platforms. For instance, being listed on these platforms alongside other restaurants can facilitate price comparisons and intensify the competition (Li and Wang 2024a). Similar observations are documented by practitioners and industry analysts about the asymmet ric relationship: being on the platform does not guarantee benefits for the restaurants, but their absence from such platforms can unequivocally put them at a competitive disadvantage (McCart 2019, Ahuja et al. 2021).

Whereas extant research focuses on formal contracted partnerships between platforms and restaurants, recent theoretical papers suggest that nonpartnered relationships may also be viable arrangements (Feldman et al. 2023). Nonpartnered relationships enabled by indepen dent third-party enablers (such as deliverers) seem particularly relevant in competitive environments in which speed and consumer choice drive market dynamics. These arrangements afford platforms the agility to expand offerings and capture market trends without the time-intensive process of securing formal agreements. They exploit market niches quickly, responding to consumer demands for diverse and immediate options, illustrating how such strategies can flourish in specific sectors despite their operational challenges. However, there could be inefficiencies in such relationships because of operational issues, such as incorrect menu prices, improper handling of food (e.g., Saxena 2019, Christians 2020), or a reduction of platform profit in the absence of commission fees (Chen et al. 2022). This research adds to the literature by empirically investigating the impact of platforms listing restaurants without a formal contracted partnership.

## 2.2. Platform Strategy in Multisided Markets

The multisided networks literature investigates various strategies that platform owners can use to grow the network and ensure efficient governance. Extant research demonstrates that platform owners can manage their platforms by controlling various operational levers, such as price, quality, entry decisions, and platform openness (Rochet and Tirole 2003, Parker and Van Alstyne 2005, Boudreau 2010, Zhu and Iansiti 2012), in order to attract participants from both the demand and supply sides, thereby creating same-side and cross-side network effects. Consequently, the focus has been on studying how these levers help organically grow the network on both sides.

Platforms may also grow their network inorganically through strategies such as seeding (Dou and Wu 2021), mergers (Farronato et al. 2023), or envelopment (Eisenmann et al. 2011). Most studies use theoretical modeling to understand the impact of such strategies on network growth and their implications for value creation and capture on the platform. However, few papers empirically investigate how these strategies manifest in the context of food delivery platforms. In particular, there is a lack of empirical evidence on how cross-side and same-side network effects are affected when a platform expands the supply side (e.g., Reshef 2023) without formal contracts. Such relationships are feasible in settings in which the third side of the platform can leverage its reputation to profitably unlock commerce. Unlike partnered restaurants, nonpartnered restaurants are passive suppliers; they do not contribute efforts toward advertising or innovation on the platform. This research adds to the literature by shedding light on how the inclusion of passive suppliers affects platform dynamics.

## 2.3. Platform Actions, Externalities, and Regulations

Multisided platforms often generate externalities— positive or negative—that can impact a wide range of stakeholders within and outside the platforms (Boudreau and Hagiu 2009). Given the extensive influence platforms exert, a key issue has arisen regarding the mode of oversight that best promotes fair competition and mitigates negative externalities without stifling innovation (e.g., Cohen and Sundararajan 2015, Frieden 2017, Mayya and Viswanathan 2024). Some studies highlight the effectiveness of market competition in encouraging platforms to self-regulate via private platform policies without the need for external interventions (e.g., Boudreau and Hagiu 2009). However, other studies emphasize that platforms may lack the discretion or motivation to self-regulate because of their ubiquity and often monopolistic market position. Most recent discussions focus on how the credible threat of regulation can motivate platforms to self-regulate (e.g., Cusumano et al. 2021, Gawer and Srnicek 2021). Whereas it is generally accepted that the threat of regulation can improve platform governance practices, much is unknown about the effectiveness of implementing retrospective regulations. We add to this literature by providing insights into the impact of retrospective regulations that intend to check externalities related to platform expansion strategies. We provide empirical evidence on its efficacy in promoting better market outcomes.

## 2.4. Literature Gap

The literature on the impact of delivery platforms on restaurant businesses (e.g., Zhang et al. 2019; Raj et al. 2020; Li and Wang 2024a, b, among others) predominantly examines the formal partnerships between res taurants and delivery platforms. Formal partnerships present a trade-off: offering benefits such as menu and pricing control (Saxena 2019, Christians 2020) and access to consumer data and reach (McCarthy 2024, Peek 2024), they also impose additional costs, such as commission fees and the need for a dedicated workforce. However, much is unknown about the platform dynamics when nonpartnered restaurants are added on both those restaurants as well as the partnered restaurants already on the platform. Whereas partnered restaurants actively participate in promotions and respond to competitive pressures on the platform, nonpartnered restaurants do neither. Hence, it is unclear whether the negative competition effect dominates the positive cross-side network effects. This important difference allows us to provide new insights into how platforms can expand inorganically to include passive partners as well as measure the resultant effects on both partnered and nonpartnered suppliers. Furthermore, it is unclear whether external regulations to delist nonpartnered restaurants lead to desirable outcomes. Recent papers on commission cap regulations suggest that such regulations may lead to unintended consequences that harm restaurants (e.g., Li and Wang 2024b). Therefore, it is important to empirically investigate the impact of such regulations on various stakeholders to inform evidencebased policymaking. Our study fills these gaps in the literature.

## 3. Empirical Context, Data, and Models

We answer the research questions by analyzing Grubhub, one of the three largest food delivery platforms fo restaurants in the United States.<sup>8</sup> Founded in 2004, the platform quickly gained prominence, aggressively acquiring competitors such as Seamless and Eat24 and becoming the dominant player in on-demand food delivery. At its core, Grubhub is a marketplace connecting three sides of the food ordering and delivery process: consumers, restaurants, and delivery personnel (deliverers).

## 3.1. Partnered vs. Nonpartnered Restaurants

How do partnered and nonpartnered restaurants differ in their relationships with online delivery platforms? Partnered restaurants enter into formal agreements with the platform, typically involving fee structures and cooperative marketing efforts, creating a mutually beneficial relationship. Partnered restaurants also decide the menu items and prices. When a consumer places an order through the platform, the platform collects the payment, releases the order to the restaurant electronically, and dispatches a deliverer to pick up and deliver the order. Conversely, nonpartnered restaurants are listed without an explicit contract or direct consent, often unbeknownst to them until orders commence. These restaurants do not pay fees to the platform and do not control their menu pricing as listed on the platform. A typical order flow for nonpartnered restaurants, fulfilled by deliverers, is shown in Figure 1. When a platform user places an order with a nonpartnered restaurant, the platform collects the payment and dispatches a deliverer to place the order on the consumer’s behalf through the restaurant’s existing channels. The deliverer then picks up the order, pays for the food using a payment method provided by the platform, and delivers it.

The inclusion of nonpartnered restaurants largely stems from the platforms’ decision to rapidly expand their restaurant offerings, thereby enhancing their appeal to users and simultaneously demonstrating the benefits of being on their platform to restaurants. When the platform decided to add nonpartnered restaurants, the selection of restaurants primarily depended on the availability of an online menu from platforms such as Yelp or restaurants’ own websites, reflecting a tactic aimed at scaling platform options through mass inclusion. The partnership status of restaurants was often obscured from consumers with subtle pricing disclaimers at the order stage that, at best, vaguely hinted at possible cost variations.

## 3.2. Context

In the last quarter of 2019, Grubhub adopted an aggressive expansion strategy that aimed at encompassing as many restaurants as possible on its platform, primarily guided by the availability of online menus. This strategy saw Grubhub’s restaurant listings swell from an overall restaurant count of 105,000 in 2018 to adding more than 150,000 restaurants<sup>9</sup> in just the last quarter of 2019. Online Figure A1 illustrates the similarity in footfall patterns across different restaurant categories— nonpartnered, partnered, and those not on the platform—highlighting Grubhub’s lack of specific selection criteria.<sup>10</sup> Although delivery platforms argued that listing nonpartnered restaurants on the platforms was beneficial to nonpartnered restaurants because of increased visibility, some restaurants did not appreciate this practice and sought legal and regulatory remedies.<sup>11</sup> Consequently, in response to complaints from restaurants about being listed on Grubhub without their consent, the state of California passed the Fair Food Delivery Act prohibiting this practice.<sup>12</sup> Prior to the regulation, approximately 40% of the restaurants on the platform in California were nonpartnered. Online Figure A2 captures the timelines of the two exogenous events.

Our research context has two distinct aspects that facilitate empirical identification. First, unlike other contexts in which joining a platform is a voluntary decision made by the participants, our context involves an involuntary addition to the platform. This allows us to assess the outcomes of platform participation without significant self-selection concerns. Second, our context offers a rare opportunity to measure the impact of a platform strategy, followed by the impact of external regulation that reversed this platform strategy. The addition of nonpartnered restaurants by Grubhub and California’s regulatory intervention occurred within a year of each other, enabling us to study the impact of both the platform policy and the regulation.

Figure 1. (Color online) Comparison of Partnered and Nonpartnered Restaurants  
![](/api/attachments/EEGYEBDP/fulltext/images/1326cecab5b5e48c73d321e1f33a190bdbdb239c2eabfa77ae02e31fe2dceb18.jpg)

## 3.3. Data

We compiled a comprehensive panel data set by triangulating across multiple sources. The raw data set comprises all restaurants<sup>13</sup> located in the states of California, Oregon, and Washington.

3.3.1. Restaurant Foot Traffic. The foot traffic data are provided by SafeGraph, Inc., a data company that collects anonymized location data from approximately 35 million unique devices across the United States. The data has been used by researchers across fields, including public health and economic activity analysis (e.g., Chiou and Tucker 2020). To preserve anonymity, Safe-Graph aggregates visiting data weekly and provides visit duration categories: 0–5 minutes, 5–10 minutes, etc. This granularity allows us to analyze the impact of platform listings on restaurants’ takeout orders.

3.3.2. Restaurant–Platform Partnership. Restaurant partnership data are provided by Grubhub. The longitudinal data captures which restaurants are listed on the platform each month, which are nonpartnered, and the exact dates when they were added to the platform. Our data set also captures when nonpartnered restaurants in California were removed per the state’s regulation.

3.3.3. Transaction Data Set. We utilize a comprehensive data set of anonymized, aggregate debit/credit card transactions provided by Visa. Compiled in collaboration with more than a thousand financial institutions, this data set captures the monthly sales figures in terms of both transactions and total expenditure in U.S. dollars from diverse restaurant channels, including deliveries and direct sales from dine-in or takeout services. The data set categorizes transactions by restaurant type using merchant category codes, offering a granular view of spending through both delivery platforms and direct restaurant sales. We aggregate the transactions at a restaurant–month level.

3.3.4. Variables and Measurement. The main variables and their summary statistics are presented in Tables 1 and 2, respectively. The primary variable of interest relates to consumers’ visits to restaurants. We specifically investigate the frequency of takeout visits to restaurants, as defined in Table 1, because food delivery platforms directly impact only takeout orders.

3.3.4.1. Takeout Visits (Visits Lasting Less Than 10 Minutes). Consumers (or deliverers) typically wait less than 10 minutes upon arriving at a restaurant before their orders are ready for takeout, drive-through, or pickup.<sup>15</sup> Takeout visits include instances in which consumers pick up orders themselves or deliverers fulfill platform orders. Following the literature (e.g., Huntington-Klein 2020), we normalize the SafeGraph data by multiplying the SafeGraph footfall by the ratio of the census population of a census region to the Safe-Graph panel population of that region in a given month. The RawTakeout visits refer to the unnormalized Safe-Graph visit counts.

3.3.4.2. Nonpartnered Restaurants. This binary variable carries the value of one for any restaurant that was added to the platform without a formal contract. We retain only those restaurants for which this binary value remains consistent throughout the panel.<sup>16</sup>

3.3.4.3. Chain Restaurants. This binary variable carries the value of one if any restaurant is part of a chain restaurant business, including both franchises and company-owned locations.

3.3.4.4. Nonpartnered Restaurants Nearby. NonPartner-ListingNearby is a binary variable that equals one if at least one nonpartnered restaurant is located in the same zip code as the focal restaurant at the time. Similarly, NonPartnerListingNearbyCount quantifies the number of nonpartnered restaurants in the same zip code as the focal restaurant. Both variables are used exclusively in the analysis of same-side network effects. For additional analysis, we also created two separate binary variables: one indicating the presence of a nonpartnered chain restaurant and the other indicating the presence of a non partnered independent restaurant.

## 3.4. Empirical Strategy

In order to study the effects of delivery platforms on restaurants, we follow a two-pronged empirical strategy. The first empirical strategy involves exploiting the shock caused by Grubhub when it added nonpartnered restaurants to its platform without a formal contract. We also model the impact of this growth strategy on partnered restaurants to measure the competition effect from the exogenous increase in the suppliers on the platform. The second empirical strategy capitalizes on the regulation in California that mandated platforms to remove nonpartnered restaurants from their platform. We also model the impact of this regulatory delisting on partnered restaurants, which were never removed from the platform but experienced a sudden decrease in the competition on the platform. These policy variations allow us to utilize a quasi-experimental design and adopt a difference-in-differences (DiD) method, contrasting the outcomes of restaurants on the platform with those of similar restaurants that were never on the platform. We use two variants of DiD estimators in the aforementioned two empirical strategies: the staggered DiD estimation technique for the first strategy and the standard panel DiD estimation for the second.

Table 1. Variable Explanation

<table><tr><td>Variable</td><td>Description</td></tr><tr><td colspan="2">Dependent variables</td></tr><tr><td>Takeout $_{it}$ </td><td>Number of visitors that spent less than 10 minutes in a restaurant i in month t,normalized by the population of the neighborhood</td></tr><tr><td>RawTakeout $_{it}$ </td><td>Number of visitors that spent less than 10 minutes in a restaurant i in month t</td></tr><tr><td>Revenue $_{it}$ </td><td>Monthly revenue for a restaurant i in month t</td></tr><tr><td colspan="2">Explanatory variables</td></tr><tr><td>NonPartnerListing $_{i}$ </td><td>Whether a restaurant i that is on Grubhub has a formal partnership with it</td></tr><tr><td>ChainRestaurant $_{i}$ </td><td>Whether a restaurant i is a chain restaurant</td></tr><tr><td>PlatformStrategyEnacted $_{it}$ </td><td>Whether the platform growth policy was implemented on restaurant i in month t</td></tr><tr><td>RegulatoryPolicyEnacted $_{t}$ </td><td>Whether the California regulation barring platforms from adding nonpartnered restaurants was enacted in month t</td></tr><tr><td>NonPartnerListingNearby $_{it}$ </td><td>Whether there is at least one nonpartnered restaurant within the zip code of partnered restaurant i in month t</td></tr><tr><td>NonPartnerListingNearbyCount $_{it}$ </td><td>Number of nonpartnered restaurants within the zip code of partnered restaurant i in month t</td></tr></table>

Note. Nonpartnered restaurants were added to the platform at different months.

3.4.1. Staggered DiD Estimation of the Impact of Listing. In our first empirical investigation, we analyze the differential trajectory of visits to restaurants following their inclusion on the platform, employing a staggered treatment approach because each restaurant is added at different times. Following the literature, we first preprocess the data set using matching and then apply the classical two-way fixed effect (TWFE) model. Additionally, as a robustness check, we employ the matrix completion (MC) method (Athey et al. 2021).

3.4.1.1. Traditional Matching. We adopted the classic TWFE model as our main analytical framework, consistent with prior studies (Gao and Zhang 2017, Mayya et al. 2021). There are known estimation problems when DiD is used in a quasi-experimental setting without preprocessing the data. One such problem is that the treatment is not randomly assigned. These issues have been addressed by preprocessing the data using established matching techniques such as the propensity score matching (PSM) technique. PSM, in conjunction with DiD, has been used for causal inferences across disciplines (Smith and Todd 2005, Liu and Lynch 2011, Mayya and Viswanathan 2024). The procedure requires predicting the propensity of a restaurant to be listed on the platform using various timevariant covariates (e.g., total visits, takeout visits, median distance from consumers’ home) and timeinvariant covariates (e.g., zip code, restaurant subcategory). We employed a dynamic matching approach in which, each month, newly treated restaurants were matched to control restaurants using the time-variant covariates based on their mean value from the pretreatment period with additional constraints ensuring that the treated–control restaurant pair were from the same zip code and the same restaurant category. Finally, we performed a one-to-one match without replacement of the matched control restaurants. This matching procedure resulted in 7,000 treated restaurants and an equal number of dynamically matched control restaurants.

Table 2. Summary Statistics

<table><tr><td>Variable</td><td>Observations</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td>Takeoutit</td><td>660,923</td><td>1,279</td><td>1,574</td><td>0</td><td>92,256</td></tr><tr><td>RawTakeoutit</td><td>660,923</td><td>56.1</td><td>72.3</td><td>0</td><td>3,135</td></tr><tr><td>Revenueit</td><td>660,923</td><td>1,084</td><td>1,186</td><td>0</td><td>90,970</td></tr><tr><td>NonPartnerListingi</td><td>660,923</td><td>0.268</td><td>0.443</td><td>0</td><td>1</td></tr><tr><td>ChainRestauranti</td><td>660,923</td><td>0.242</td><td>0.428</td><td>0</td><td>1</td></tr><tr><td>PlatformStrategyEnactedit</td><td>660,923</td><td>0.33</td><td>0.47</td><td>0</td><td>1</td></tr><tr><td>RegulatoryPolicyEnactedt</td><td>660,923</td><td>0.333</td><td>0.471</td><td>0</td><td>1</td></tr><tr><td>NonPartnerListingNearbyit</td><td>660,923</td><td>0.701</td><td>0.458</td><td>0</td><td>1</td></tr><tr><td>NonPartnerListingNearbyCountit</td><td>660,923</td><td>17</td><td>20.6</td><td>0</td><td>105</td></tr></table>

Notes. The summary statistics table includes monthly observations from September 2019 to March 2021 for 36,776 restaurants that show up in at least one of the analyses. Some urban coffee shops experience daily footfall in the thousands.

For the first question, we specify the empirical model as follows:

$$
\begin{array}{r l} & Y _ {i t} = \alpha + \beta N o n P a r t n e r L i s t i n g _ {i} \\ & \qquad \times P l a t f o r m S t r a t e g y E n a c t e d _ {i t} + \mathbf {X} _ {i t} \theta + \mu_ {i} + v _ {t} + \varepsilon_ {i t}, \end{array}\tag{1}
$$

where i and t index a restaurant and month, respectively, and $\mu _ { i }$ and $\upsilon _ { t }$ represent the fixed effect for restaurant i and the fixed effect for absolute month $t ,$ respectively. The outcome variables of interest, $Y _ { i t } ,$ are Takeout<sub>it</sub>, Revenue<sub>it</sub>, or RawTakeou $\ ! t _ { i t }$ as defined in Table 1.<sup>17</sup> The variable PlatformStrategyEnacted<sub>it</sub> becomes one for both restaurant i and its matched pair after month t. The DiD coefficient $\beta$ captures the causal effect of the platform strategy.

3.4.1.2. Matrix Completion Method. The alternative model estimation is the MC method, which uses a datadriven approach to estimate the counterfactual outcomes.<sup>18</sup> The MC method works by creating a low-rank approximation of the outcome matrix, which balances capturing systematic patterns (both across units and over time), handles heterogeneous treatment effects, and allows for differential trends among treated and control units (Athey et al. 2021). In the context of staggered policy adoption, the MC method can handle varying treatment times by predicting unobserved outcomes as though the policy were adopted at the same time for all units, thus aligning the data for comparison.

We specify the model as recommended by Athey et al. (2021), which accounts for individual restaurant characteristics and time-specific effects (e.g., seasonality or economic fluctuations). By specifying the model this way, the MC method estimates the outcome by contrasting the observed restaurant performance with the predicted performance if the restaurant did not have a nonpartner listing, enabling us to accurately isolate the specific effects of these listings and platform strategies.

3.4.1.3. Minimum Distance Matching. The second research question measures the impact of listing nonpartnered restaurants on the performance of existing partnered restaurants on the platform. The model is similar to Equation (1) except, in this case, the event refers to the addition of the first nonpartnered restaurant within the same zip code as the treated–control restaurant pair. The formal model is as follows:

$$
\begin{array}{r l} Y _ {i t} = & \alpha + Y \text {PartnerListing} _ {i} \times \text {NonPartnerListingNearby} _ {i t} \\ & + \mathbf {X} _ {i t} \theta + \mu_ {i} + v _ {t} + \varepsilon_ {i t}, \end{array} \tag {2}
$$

where i and t index a restaurant and an absolute month, respectively. As described in Table 1, the variable Non-PartnerListingNearby is a binary variable that takes the value of one if the restaurant i has at least one nonpartnered restaurant in the zip code where i is located. Once this value turns to one, it stays one for the duration of the panel. For robustness, we also use NonPartnerListingNearbyCount , which represents the count of nonpartnered restaurants.

Because the demand for partnered and nonpartnered restaurants can potentially interfere in the presence of network effects, we follow extant literature $( \mathrm { e . g . }$ , Ho et al. 2020) and enforce a minimum distance between the treated and control restaurants within the same zip code.<sup>19</sup> On average, zip codes in the United States cover more than 50 square miles although those in more densely populated cities can span just a few square miles (e.g., Mack and Grubesic 2009). Given the wide geographical variation of zip code sizes, we use Uber’s H3 grid system<sup>20</sup> to develop a better cutoff for minimum distance matching. Uber’s H3 grid indexes all areas of the Earth into uniform-sized hexagonal cells across different resolutions from 0 to 10. We go with a level 7 resolution, which approximates a one-mile radius around each restaurant to construct a competitive perimeter that is conservative yet adequate for discerning the effects of nonpartnered restaurants on those partnered with delivery platforms. We continue to retain the exact zip code matching along with the one-mile minimum distance requirement to ensure that the matched restaurants are within the same regulatory space.

3.4.2. Traditional DiD Estimation for the Impact of Delisting. Here, we model the differential trajectory of takeout visits after nonpartnered restaurants were delisted from the platform as a one-shot policy implementation. On September 24, 2020, the California governor signed a bill banning platforms from listing restaurants without a formal contract. We designate the month of law implementation as t � 0 and organize the preimplementation and postimplementation periods accordingly. We perform a subsample analysis on California restaurants by matching the nonpartnered restaurants with the control group of similar restaurants that were never listed on the platform.

We formally state our model as follows:

$$
\begin{array}{r l} & Y _ {i t} = \alpha + \delta N o n P a r t n e r L i s t i n g _ {i} \\ & \qquad \times R e g u l a t o r y P o l i c y E n a c t e d _ {t} + \mathbf {X} _ {i t} \theta + \mu_ {i} + \nu_ {t} + \varepsilon_ {i t}, \end{array}\tag{3}
$$

where i and t index a restaurant and an absolute month, respectively. The coefficient δ measures the impact of regulation enactment in California, which required delivery platforms to delist nonpartnered restaurants.

Finally, we modify Equation (3) by replacing the treated units with partnered restaurants and match them with “never on platform” restaurants to study the spillover impact of delisting nonpartnered restaurants on partnered restaurants on Grubhub in California.

## 4. Empirical Analysis and Results 4.1. Impact of Being Added Without a Contract on Nonpartnered Restaurants

The first analysis is to understand how the inclusion of nonpartnered restaurants on the platform affects their takeout orders. For this analysis, we use the matched data set, in which the nonpartnered restaurants serve as the treated group and restaurants that were never on the platform serve as the control group. Figure 2 presents the graphical representation of the classic TWFE model and the matrix completion models. The results of model 1 are presented in Table 3. As shown in column (1) of panel A of Table 3, nonpartnered restaurants experienced a 41.023 increase in the normalized Takeout visits $( \beta = 4 1 . 0 2 3 )$ . This increase of 41.023 translates to an additional \$1,409.96 in revenue each month based on an average order size of \$34.37 (Circuit 2022). Panel B of Table 3 shows the outcome for the raw takeouts based on the raw data obtained from SafeGraph. These results are consistent with those in panel A. Finally, we reestimate the model using Revenue<sub>it</sub> as the dependent variable with the results presented in panel C of Table 3. Consistent with panels A and B, the overall revenue increased significantly.<sup>21</sup>

4.1.1. Heterogeneous Effects. Platform policies and regulations pertaining to delivery platforms may impact independent and chain restaurants differently because of the differences in their operational models, marketing strategies, and consumer awareness. Independent restaurants also differ from chain establishments in their resilience to technological advancements because of their limited resources for navigating challenges posed by rapidly changing technologies. To explore these heterogeneous effects, we perform a subsample analysis based on whether a nonpartnered restaurant is a chain or an independent restaurant. The empirical results are presented in columns (2) and (3) of panels $\mathrm { A } { \ - } C$ of Table 3 for $T a k e o u t _ { i t } ,$ RawTakeout , and $R e v e n u e _ { i t } ,$ respectively. We find that the increase in takeout orders is numerically larger and statistically significant for independent restaurants (column (3)) compared with chain restaurants (column (2)).

4.1.2. Alternative Estimators. As noted in Section 3.2, Grubhub followed an aggressive expansion strategy to add as many restaurants as it could to the platform, con ditional on the availability of an online menu. As shown in Online Figure A1, concerns about selection bias are largely absent. Yet, because of the staggered nature of adding nonpartnered restaurants, we test the robustness of our findings using modern estimators such as Callaway and Sant’Anna (2021), Butts and Gardner (2022), Roth and Sant’Anna (2023), and Sun and Abra ham (2021), which are well-suited to handle the stag gered policy enactment scenario. We present the results in Online Figure A3. The findings are consistent with those obtained using TWFE and MC methods.

Next, we perform the Goodman-Bacon decomposition, detailed in Goodman-Bacon (2021). The procedure disaggregates the TWFE estimates into individually interpretable components that facilitate clearer causal inference in staggered adoption settings. Following current literature recommendation, we applied this method in our analysis, presenting the results in Online Figure A4 and Online Table A3; our findings align closely with previous results, reinforcing the robustness of our conclusions.

Figure 2. Event Study and Matrix Completion Graphs: Impact on Nonpartnered Restaurants  
(a)  
![](/api/attachments/EEGYEBDP/fulltext/images/d95b7ff4aa2b54fa799fd2b2034883ee57b0d2bb2145c955d5635377e66dc9ad.jpg)

(b)  
![](/api/attachments/EEGYEBDP/fulltext/images/1cb59dce228f5a398025a1b19bcda60be4847acadca972b3557c8059fd06a0ef.jpg)  
Notes. Y-axis is RawTakeou $t _ { i t } ,$ the data obtained from SafeGraph. (a) Impact on non-partnered-event study and (b) impact on non-partnered matrix completion.

Table 3. Effects of Being Added to the Platform Without a Contract on Restaurant Demand

<table><tr><td colspan="4">Panel A: Takeout as the dependent variable</td></tr><tr><td>Dependent variables</td><td>(1)Takeout0–10 minutes</td><td>(2)Takeout0–10 minutes</td><td>(3)Takeout0–10 minutes</td></tr><tr><td>Sample</td><td>FullSample</td><td>SubsampleChain</td><td>SubsampleIndependent</td></tr><tr><td>NonPartnerListing × PlatformStrategyEnacted</td><td>41.023***(7.606)</td><td>50.333(32.684)</td><td>54.577***(6.804)</td></tr><tr><td>Observations</td><td>167,786</td><td>26,965</td><td>140,821</td></tr><tr><td> $R^2$ </td><td>0.915</td><td>0.930</td><td>0.865</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Panel B: RawTakeout as the dependent variable

<table><tr><td>Dependent variables</td><td>(1) RawTakeout 0–10 minutes</td><td>(2) RawTakeout 0–10 minutes</td><td>(3) RawTakeout 0–10 minutes</td></tr><tr><td>Sample</td><td>Full Sample</td><td>Subsample Chain</td><td>Subsample Independent</td></tr><tr><td>NonPartnerListing × PlatformStrategyEnacted</td><td>1.767*** (0.359)</td><td>0.308 (1.553)</td><td>2.314*** (0.317)</td></tr><tr><td>Observations</td><td>167,786</td><td>26,965</td><td>140,821</td></tr><tr><td> $R^2$ </td><td>0.903</td><td>0.918</td><td>0.856</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Panel C: Revenue as the dependent variable

<table><tr><td>Dependent variables</td><td>(1) Revenue</td><td>(2) Revenue</td><td>(3) Revenue</td></tr><tr><td>Sample</td><td>Full Sample</td><td>Subsample Chain</td><td>Subsample Independent</td></tr><tr><td>NonPartnerListing × PlatformStrategyEnacted</td><td>49.495***(7.752)</td><td>23.369(17.972)</td><td>66.005**(8.520)</td></tr><tr><td>Observations</td><td>167,786</td><td>26,965</td><td>140,821</td></tr><tr><td> $R^2$ </td><td>0.863</td><td>0.920</td><td>0.852</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes. Standard errors clustered around restaurants in parentheses. A total of 7,000 restaurants each in treated and control postmatching. \*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

4.1.3. Robustness Checks. We assess the robustness of our findings by redefining RawTakeout with varying time windows for qualifying visits: 0–20 minutes and 0–5 minutes. The results are presented in panels A and B of Online Table A1, respectively. Across both variations, the main results remain consistent. Next, to ensure the stability of the subsample analysis, we included a three-way interaction in the main model, involving DiD terms and a dummy variable for chain restaurants. The results, presented in column (1) of Online Table A10, remain consistent.

We also evaluate the sensitivity of our findings to different model specifications. We employ a Poisson count model to account for the count nature of the footfall data. Panel A of Online Table A2 shows the results from this specification. Next, following prior literature (Smith and Todd 2005, Austin and Small 2014), we bootstrap the standard errors with 100 replications. The results from this approach are presented in panel B of Online Table A2. Our results are robust across both alternative specifications. Additionally, we use the log transformation of RawTakeout as the outcome variable and present the corresponding results in panel C of Online Table A2. These results indicate that the average takeout increases by 3.98% (β � 0.039 in column (1); $( \mathrm { e } ^ { 0 . 0 3 9 } \mathrm { - } 1 ) \times 1 0 0 =$ 3.98%) after being listed as a nonpartnered restaurant on the platform.

Finally, we perform the in-space placebo test, also referred to as the random implementation (shuffle) test, in line with those by Burtch et al. (2018). The test utilizes fictitious treatment units, selected randomly from either the control or an unaffected pool, to assess the likelihood of placebo effects surpassing or equating the estimated treatment effect. We replicated this procedure

Figure 3. (Color online) In-Space Placebo Test: Nonpartnered Restaurants  
![](/api/attachments/EEGYEBDP/fulltext/images/6a662a7b80698f5e0e919f6caf0fddac5aea21b4f1954981140789f3962d737a.jpg)

500 times, randomly assigning a treatment indicator to various units by treating some restaurants that were never on platforms as nonpartnered restaurants and estimating the effect. Subsequently, we plot the DiD outcomes of these various draws and compare them against the actual effect size (indicated by the solid vertical line to the right). As seen in Figure 3, the placebo test results are distributed around zero, confirming the absence of spurious effects and supporting the internal validity of our main model.

4.1.4. Possible Mechanisms. Section 4.1 demonstrates that nonpartnered restaurants benefit from being listed on the platform. One possible explanation for the positive effect is increased visibility as observed by recent work such as those by Li and Wang (2024b) in the restaurant delivery setting and by Teng et al. (2023) in the grocery delivery setting. Our finding that independent restaurants enjoy a marked increase in takeout orders postlisting further supports the visibility mechanism. Unlike their chain counterparts, many of the independent establishments previously lacked significant exposure; hence, they benefit disproportionately from the enhanced visibility provided by the delivery platform.

However, to capitalize on the increased visibility effectively, restaurants must be well-equipped and prepared to handle takeout orders. Otherwise, they may not be able to convert potential demand into actual sales. To test this hypothesis, we classified nonpartnered restaurants into four quartiles based on their Takeout orders in August 2019, which was the month before Grubhub began listing nonpartnered restaurants on its platform. We then estimated the interaction effects of these group dummies with the DiD terms and report the results in Table 4. The results show that the restaurants in the top quartile of Takeout orders prior to the platform strategy experienced the largest revenue increase. Column (1) shows that the coefficient of 114.133 translates to about \$3,922.75 per month over and above the improvements for restaurants in the lowest quartile based on an average order size of \$34.37 (Circuit 2022). For independent restaurants, the gains are about \$6,239 per month as seen in column (3). These restaurants likely had existing systems deployed for phone or web orders, potentially with their own delivery services. However, they likely opted not to partner with the platform because of high commission fees.<sup>22</sup> Because they already had a takeout channel with a publicly accessible takeout menu, being listed as a nonpartnered restaurant on the platform gave them an added advantage of free advertising on the platform.

We further evaluate this mechanism by splitting restaurants into two groups based on their takeout readiness. We coded the restaurant as “takeout-ready” if the restaurant’s Yelp page indicated that it offered either pickup or delivery service. We reestimated Model 1 on these two subsamples. The results, presented in Online Table A4, confirm the mechanism: only takeout-ready restaurants benefited from being listed as a nonpartnered restaurants on Yelp.

Table 4. Mechanism Analysis: Outcomes Based on Restaurant’s Takeout Readiness

<table><tr><td>Dependent variables</td><td rowspan="2">(1)TakeoutFullSample</td><td rowspan="2">(2)TakeoutSubsampleChain</td><td rowspan="2">(3)TakeoutSubsampleIndependent</td><td rowspan="2">(4)RawTakeoutFullSample</td><td rowspan="2">(5)RawTakeoutSubsampleChain</td><td rowspan="2">(6)RawTakeoutSubsampleIndependent</td></tr><tr><td>Sample</td></tr><tr><td>NonPartnerListing × PlatStratEnacted</td><td>8.960*(4.307)</td><td>-50.663(38.424)</td><td>12.059**(3.990)</td><td>0.360(0.184)</td><td>-1.970(1.582)</td><td>0.483**(0.172)</td></tr><tr><td>NonPartnerListing × PlatStratEnacted × QuartileTwo</td><td>-1.764(8.975)</td><td>34.955(46.387)</td><td>-1.056(9.218)</td><td>0.056(0.384)</td><td>1.151(1.909)</td><td>0.103(0.396)</td></tr><tr><td>NonPartnerListing × PlatStratEnacted × QuartileThree</td><td>33.520**(11.612)</td><td>78.992(49.524)</td><td>42.698***(12.142)</td><td>1.369**(0.497)</td><td>2.705(2.094)</td><td>1.847***(0.517)</td></tr><tr><td>NonPartnerListing × PlatStratEnacted × QuartileFour</td><td>114.133***(26.897)</td><td>129.212*(64.587)</td><td>181.524***(29.329)</td><td>5.030***(1.223)</td><td>4.508(2.905)</td><td>8.199***(1.302)</td></tr><tr><td>Observations</td><td>167,786</td><td>26,965</td><td>140,821</td><td>167,786</td><td>26,965</td><td>140,821</td></tr><tr><td> $R^2$ </td><td>0.924</td><td>0.935</td><td>0.879</td><td>0.925</td><td>0.930</td><td>0.890</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Note. Standard errors clustered around restaurants in parentheses.  
\*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

Another potential mechanism could be the inherent quality of the restaurant; more precisely, higher quality establishments might benefit more from inclusion on the platform.<sup>23</sup> For this exploration, we obtained and integrated the Yelp restaurant data set. Yelp ratings are considered a reliable indicator of a restaurant’s off-line quality as they are rigorously assessed, a point underscored by recent studies (Beck et al. 2023). We classified restaurants into quartiles based on their Yelp ratings rather than their volume of takeout orders. The results, presented in Online Table A5, reveal no significant differences in performance across the quartiles, suggesting that the inherent restaurant quality does not explain the findings. 24

## 4.2. Impact of Adding Nonpartnered Restaurants on Partnered Restaurants

Much is unknown in the literature on whether a delivery platform’s expansion strategy would have any impact on the restaurants that are already on the platform. Exogenously adding more restaurants could lead to increased competition among restaurants. Rapid supply-side expansion may decrease sales for partnered restaurants because of heightened competition. However, these new players on the supply side are passive participants with no involvement in the menu curation or promotional activities. Hence, it is unclear whether competition effects dominate network effects. Specifically, the interplay between network effects and competition effects stemming from passive participants may be different from those studied in the literature (Reshef 2023). To empirically investigate this question, we follow a similar empirical strategy as outlined in Section 3.4, in which we match partnered restaurants with those that are never on the platform. As noted in that section, we enforce a minimum distance matching of one mile and estimate Equation (2). The graphical presentations of the classical TWFE and matrix completion models are as shown in Figure 4.

Parameter estimates of Model 2 are shown in Table 5. We find evidence that the addition of nonpartnered restaurants improves outcomes for partnered restaurants already on the platform. Column (1) of panel A in Table 5 shows that partnered restaurants experienced an increase of 70.71 in normalized Takeout visits, which translates to \$2,430 in additional monthly revenue for these partnered restaurants based on an average order size of \$34.37 (Circuit 2022). We find consistent results with RawTakeout visits (panel B) and with the measure of revenue (panel C). In essence, the positive network effect outweighs the negative competition effect. Even when the supply side grows because of the exogenous addition of passive restaurants, the platform becomes more attractive to consumers, potentially drawing a larger user base as well as increasing overall platform transactions for existing users.

In columns (2) and (3) of panels A–C of Table 5, we present the respective heterogeneous effects on chain and independent restaurants. We find no impact on partnered chain restaurants (column (2)), whereas partnered independent restaurants saw a significant boost in Takeout orders (column (3)). We further examine the heterogeneity by splitting NonPartnerListingNearby into two binary variables, NonPartnerListingNearby–Chain

Figure 4. Event Study and Matrix Completion Graphs: Impact on Partnered Restaurants  
![](/api/attachments/EEGYEBDP/fulltext/images/f90255d6b23fbe64dc5811c9da1dacf1b1e9fe19ba8501ab793ccb5a16a38a96.jpg)

(b)  
![](/api/attachments/EEGYEBDP/fulltext/images/efd08c544dbc10418d7203900f46bbb4eba8ac424711c88c90be3d0189866ff7.jpg)  
Notes. Y-axis is RawTakeou $t _ { i t } ,$ the data obtained from SafeGraph. (a) Impact on partnered-event study. (b) Impact on partnered-matrix completion.

Table 5. Impact of Adding Nonpartnered Restaurants on Partnered Restaurants

<table><tr><td colspan="4">Panel A: Takeout as the dependent variable</td></tr><tr><td>Dependent variables</td><td>(1)Takeout0–10 minutes</td><td>(2)Takeout0–10 minutes</td><td>(3)Takeout0–10 minutes</td></tr><tr><td>Sample</td><td>FullSample</td><td>SubsampleChain</td><td>SubsampleIndependent</td></tr><tr><td>PartnerListing × NonPartnerListingNearby</td><td>70.707***(12.082)</td><td>33.141(23.314)</td><td>82.201***(11.815)</td></tr><tr><td>Observations</td><td>138,055</td><td>57,981</td><td>80,074</td></tr><tr><td> $R^2$ </td><td>0.906</td><td>0.909</td><td>0.819</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Panel B: RawTakeout as the dependent variable

<table><tr><td>Dependent variables</td><td>(1) RawTakeout0–10 minutes</td><td>(2) RawTakeout0–10 minutes</td><td>(3) RawTakeout0–10 minutes</td></tr><tr><td>Sample</td><td>Full Sample</td><td>Subsample Chain</td><td>Subsample Independent</td></tr><tr><td>PartnerListing × NonPartnerListingNearby</td><td>2.309***(0.557)</td><td>1.473(1.060)</td><td>3.895***(0.583)</td></tr><tr><td>Observations</td><td>138,055</td><td>57,981</td><td>80,074</td></tr><tr><td> $R^2$ </td><td>0.898</td><td>0.903</td><td>0.803</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Panel C: Revenue as the dependent variable

<table><tr><td>Dependent variables</td><td>(1) Revenue</td><td>(2) Revenue</td><td>(3) Revenue</td></tr><tr><td>Sample</td><td>Full Sample</td><td>Subsample Chain</td><td>Subsample Independent</td></tr><tr><td>PartnerListing × NonPartnerListingNearby</td><td>104.623***(10.911)</td><td>15.004(12.549)</td><td>100.471***(15.589)</td></tr><tr><td>Observations</td><td>138,055</td><td>57,981</td><td>80,074</td></tr><tr><td> $R^2$ </td><td>0.829</td><td>0.901</td><td>0.796</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes. Standard errors clustered around restaurants in parentheses. A total of 5,762 restaurants each in treated and control postmatching. \*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

and NonPartnerListingNearby–Independent, and present the results in Online Table A9. Both types of nonpartnered restaurants boost the outcomes of partnered independent restaurants but not those of partnered chain restaurants. The finding aligns with industry reports indicating that diners are more likely to try out independent restaurants that they encounter.<sup>25</sup> To state it differently, when new customers join a platform because their favorite restaurant is listed, they are more likely to explore diverse culinary experiences from other independent restaurants, thereby fostering a positive spillover effect.

4.2.1. Robustness Checks. Given our minimum distance matching criteria, the treated partnered restaurants and the control restaurants may be less comparable despite being in the same zip code and having a similar trend prior to the treatment. To address the variability, we estimate the model using the generalized synthetic control method (Xu 2017). This method builds on the synthetic control approach (Abadie et al. 2010) by adding interactive fixed effects models, enhancing its ability to estimate causal effects in diverse settings with multiple treated units and varying treatment durations. We present the results in Online Figure A5. The results are consistent.

Next, instead of defining the treatment variable as a binary variable for the presence or absence of nonpartnered restaurants, we redefine it as the number of nonpartnered restaurants within the specified radius. This adjustment allows for a more nuanced capture of heterogeneous competition effects. We reestimate Model 2 using this modified treatment variable and present the results in Online Table A6. We find the results to be consistent with our main findings.<sup>26</sup> To further confirm the stability of the subsample analysis in the main table, we add a three-way interaction in the main model involving the DiD terms and a dummy variable set to one for chain restaurants. The results, shown in column (2) of Online Table A10, are consistent.

Next, as in Section 4.1.3, we test the robustness of our findings by changing the operationalization of our dependent variables. In panel A of Online Table A7, we present the results after changing the model specifications to the Poisson count model. In panel B of Online Table A7, we present results after bootstrapping the standard errors for the estimations in Table 5 using 100 replications. In panel C of Online Table A7, we present the outcome after log-transforming the dependent variable. The results remain consistent and robust across al analyses, adding confidence to our findings.

Next, similar to Section 4.1.3, we test the robustness of our findings using modern estimators such as Callaway and Sant’Anna (2021), Butts and Gardner (2022), Roth and Sant’Anna (2023), and Sun and Abraham (2021) and present the results in Online Figure A6. The findings are consistent with our results using the TWFE and MC methods. Furthermore, we perform the Goodman-Bacon decomposition, detailed in Goodman-Bacon (2021), and present the results in Online Figure A7 and Online Table A8. The findings align with the main analysis and support our belief that potential biases with TWFE models under staggered policy adoption do not affect the direction or significance of our findings.

Finally, to ensure that the platform strategy change did not affect partnered restaurants without any nonpartnered restaurants nearby, we perform an in-space placebo test that involves partnered restaurants that did not see nonpartnered restaurants in their zip code, presumably unaffected by the platform strategy change. The procedure randomly assigns fake treatments to unaffected partnered restaurants that are spatially isolated from the strategy because of the absence of nearby nonpartnered restaurants. As shown in Online Figure A8, the placebo effects are statistically insignificant from zero and differ from the actual treatment effect. This gives us confidence that the observed actual DiD estimate can be attributed solely to the platform strategy change.

Synthesizing the results from Sections 4.1 and 4.2, our findings indicate that the introduction of nonpartnered restaurants to the platform elevates their order volumes, simultaneously boosting sales for existing partnered establishments. This dual impact embellishes the understanding of network effects within platform economics, revealing that the presence of passive suppliers that are activated by third-party enablers can also enhance overall market dynamics in ways previously unexplored. The analysis further shows a differentiated impact based on restaurant type; the positive spillover from nonpartnered to partnered entities is observable primarily among independent restaurants with almost no gains for chain establishments.

## 4.3. Evidence from the Exogenous Delisting of Nonpartnered Restaurants

Grubhub’s strategy of listing nonpartnered restaurants on its platform faced legal challenges from some restaurants (Saxena 2020, Dowty 2021). Resultant media cov erage prompted legislative action with California becoming the first state to pass a law banning this platform strategy. We leverage this regulatory enactment to provide additional evidence for the effectiveness of noncontracted partnerships. Specifically, we employ Model 3 to analyze the effects of delisting nonpartnered restaurants on both nonpartnered and partnered establishments. Figure 5 provides the event study plot as well as the matrix completion plot of the estimation for the two models.

The results analyzing the impact of delisting on nonpartnered restaurants are presented in Table 6. column (1) of panel A shows that nonpartnered restaurants in California experience a decrease of 14.318 normalized Takeout visits. This translates to a \$492.11 monthly revenue drop for nonpartnered restaurants based on an average order size of \$34.37 (Circuit 2022). We observe a similar decline in RawTakeout value in panel (B) of Table 6 and a similar revenue drop in panel A of Online Table A11. In essence, restaurants in California that were delisted from the platform lose the benefit of being on the platform. The results analyzing the impact of regulatory delisting on partnered restaurants are presented in Table 7. Column (1) of both panels A and B shows negative but statistically insignificant results. We find similar but statistically significant results with revenue as the dependent variable detailed in panel B of Online Table A11.

4.3.1. Heterogeneous Effects. In line with Section 4.1, we examine whether being delisted from the platform affects chain and independent restaurants differently through subsample analysis. We estimate Model 3 on two distinct subsamples, one comprising chain restaurants and the other comprising independent restaurants. The results for nonpartnered restaurants are presented in columns (2) and (3) of Table 6. The results indicate that delisting the restaurants did not have a statistically significant impact on chain restaurants (column (2)), whereas it had a detrimental effect on independent restaurants (column (3)). The coefficient δ in column (3) of panel B suggests that regulatory delisting leads to a monthly drop of 16.010 Takeout visits for independent restaurants. The analysis for partnered restaurants is presented in columns (2) and (3) of Table 7. In this case, chain partnered restaurants, which did not benefit from the listings of nonpartnered restaurants, did not experience a loss in customers. Conversely, independent partnered restaurants witnessed a negative effect of removing nonpartnered restaurants. In panels (A) and (B) of Online Table A11, we find similar insights by using Revenue as the dependent variable.

Figure 5. Event Study and Matrix Completion Graphs: Impact of Regulatory Delisting  
(a)  
![](/api/attachments/EEGYEBDP/fulltext/images/71b0ae5baeb92e0351d5e7c7ab351d987669bef2c4ecf0beab97dead55520e51.jpg)

(b)  
![](/api/attachments/EEGYEBDP/fulltext/images/8c335a1d9da0551395bb0d81ad20d2ad8ced5c949e9456f55502e597da800ec1.jpg)  
(d)

(c)  
![](/api/attachments/EEGYEBDP/fulltext/images/f384a8f33160f54ecb8e0176e2818f0935d06ccdf86ab5e04a8ad70001403e4b.jpg)

![](/api/attachments/EEGYEBDP/fulltext/images/13f0523ae830a23ccf13b4d92d95ffa87ee87a362eb64aff75348d92aec0e4e0.jpg)  
Notes. Y-axis is RawTakeout , the data obtained from SafeGraph. (a) Delisting impact on non-partnered-event study. (b) Delisting impact on non partnered-MC. (c) Delisting impact on partnered-event study. (d) Delisting impact on partnered-MC.

Synthesizing the outcomes of our entire investigation, we find that the inclusion of nonpartnered restaurants on the food delivery platform created positive network effects by increasing overall user engagement and demand, benefiting both partnered and nonpartnered restaurants. Conversely, delisting nonpartnered restaurants led to negative network effects, characterized by decreased platform attractiveness and a reduction in consumer engagement, which particularly affected independent restaurants. These dynamics demonstrate how platform decisions on passive restaurant listings can significantly sway overall market behavior and user interaction within the food delivery ecosystem. Similarly, regulatory efforts to shield restaurants from such strategies may backfire.<sup>27</sup>

4.3.2. Robustness Checks. We conduct several additional analyses to ensure the results are robust. First, the dependent variable, Takeout, might be better modeled as a count variable. Therefore, we estimate Model 3 as a Poisson count model and present the results in panel A of Online Tables A12 and A13 for nonpartnered and partnered analysis, respectively. Next, we use an alternative approach to compute robustness standard errors. Specifically, we bootstrapped the standard errors for Model 3 with 100 replications and present the results in panel B of Online Tables A12 and A13. Finally, we reestimate Model 3 by taking the log transformation of RawTakeout and present the results in panel C of Online Tables A12 and A13. All results align with our main specification, thereby reinforcing the robustness of our findings.

Table 6. Impact of Delisting on Nonpartnered Restaurants

<table><tr><td colspan="4">Panel A: Takeout as the dependent variable</td></tr><tr><td>Dependent variables</td><td>(1)Takeout0–10 minutes</td><td>(2)Takeout0–10 minutes</td><td>(3)Takeout0–10 minutes</td></tr><tr><td>Sample</td><td>FullSample</td><td>SubsampleChain</td><td>SubsampleIndependent</td></tr><tr><td>NonPartnerListing × RegulatoryPolicyEnacted</td><td>-14.318*(6.412)</td><td>7.784(30.986)</td><td>-16.010*(6.472)</td></tr><tr><td>Observations</td><td>106,303</td><td>7,746</td><td>98,557</td></tr><tr><td> $R^2$ </td><td>0.803</td><td>0.918</td><td>0.722</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Panel B: RawTakeout as the dependent variable

<table><tr><td>Dependent variables</td><td>(1) RawTakeout 0–10 minutes</td><td>(2) RawTakeout 0–10 minutes</td><td>(3) RawTakeout 0–10 minutes</td></tr><tr><td>Sample</td><td>Full Sample</td><td>Subsample Chain</td><td>Subsample Independent</td></tr><tr><td>NonPartnerListing × RegulatoryPolicyEnacted</td><td>-0.631** (0.243)</td><td>0.321 (1.323)</td><td>-0.703** (0.241)</td></tr><tr><td>Observations</td><td>106,303</td><td>7,746</td><td>98,557</td></tr><tr><td> $R^2$ </td><td>0.835</td><td>0.923</td><td>0.749</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes. Standard errors clustered around restaurants in parentheses. A total of 4,838 restaurants each in treated and control postmatching. \*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

Table 7. Impact of Delisting Nonpartnered Restaurants on Partnered Restaurants

<table><tr><td>Dependent variables</td><td>(1)Takeout0–10 minutes</td><td>(2)Takeout0–10 minutes</td><td>(3)Takeout0–10 minutes</td></tr><tr><td>Sample</td><td>FullSample</td><td>SubsampleChain</td><td>SubsampleIndependent</td></tr><tr><td>PartnerListing × RegulatoryPolicyEnacted</td><td>-5.656(6.305)</td><td>20.601(20.318)</td><td>-13.125*(5.659)</td></tr><tr><td>Observations</td><td>145,859</td><td>32,409</td><td>113,450</td></tr><tr><td> $R^2$ </td><td>0.892</td><td>0.933</td><td>0.759</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Panel B: RawTakeout as the dependent variable

<table><tr><td>Dependent variables</td><td>(1) RawTakeout 0–10 minutes</td><td>(2) RawTakeout 0–10 minutes</td><td>(3) RawTakeout 0–10 minutes</td></tr><tr><td>Sample</td><td>Full Sample</td><td>Subsample Chain</td><td>Subsample Independent</td></tr><tr><td>PartnerListing × RegulatoryPolicyEnacted</td><td>-0.319 (0.247)</td><td>0.877 (0.85)</td><td>-0.658** (0.204)</td></tr><tr><td>Observations</td><td>145,859</td><td>32,409</td><td>113,450</td></tr><tr><td> $R^2$ </td><td>0.905</td><td>0.934</td><td>0.788</td></tr><tr><td>Restaurant fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Notes. Standard errors clustered around restaurants in parentheses. A total of 6,641 restaurants each in treated and control postmatching. \*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

## 5. Discussion and Conclusion

The literature on platform growth strategies in twosided networks (Rochet and Tirole 2003, Parker and Van Alstyne 2005, Economides and Viard 2006, Boudreau 2010, Zhu and Iansiti 2012) has demonstrated the importance of proactive platform growth strategies using various levers, such as price, quality, entry decisions, and platform openness. However, little is known about the impact of growth strategies that involve adding participants to the platform without a contract. The inclusion of nonpartnered suppliers, who are passive and enabled by a third party (such as deliverers in our case), adds a layer of complexity to platform dynamics. This issue becomes particularly complex in multisided networks such as delivery platforms, on which coordination must occur between multiple parties: the platform itself, restaurants, deliverers, and diners. Despite the increasingly critical role these platforms play in the restaurant industry, empirical studies on these policies remain limited.

Contracted partnerships are essential in high-stakes environments such as Airbnb Stays or Amazon.com eCommerce, in which substantial mutual investments and strict operational and regulatory compliance are necessary. However, in the fiercely competitive food delivery sector, major platforms are increasingly exploring the noncontracted arrangements, recognizing their viability and value as an alternative strategy to broaden their network. This study explores the impact of food delivery platforms’ practice of enlisting restaurants without formal contracts on both new and existing restaurants on the platforms, probing the broader ramifications of this contentious strategy aimed at expanding their supply base inorganically.

The empirical findings suggest that, when restaurants are added to the platform without a contract, their takeout orders rise by \$1,430, bringing in additional revenues without having to pay the commission fees. This finding is in line with recent theoretical papers, which suggest that noncontracted partnerships are viable arrangements that are incentive-compatible to all parties involved (Feldman et al. 2023). The mechanism analysis suggests that restaurants equipped with a robust takeout infrastructure benefit the most. Establishments that are well-prepared for takeout prior to their nonpartnered inclusion on Grubhub experienced the most substantial gains.

Another salient finding in our paper is that the platform’s strategy of adding nonpartnered restaurants enhances the same-side network effects for partnered restaurants. We estimate that partnered restaurants receive more than \$2,430 in additional revenue after the platform adds nonpartnered restaurants in their area. This implies that positive network effects dominate negative competitive effects (Katz and Shapiro 1994). This revenue boost likely results from both new customers attracted to the platform’s expanded offerings and increased engagement from existing customers who find greater value in its enhanced selection. The benefits of being listed on delivery platforms may extend beyond immediate revenue from online orders to increased physical store visits (Xu et al. 2017, Chen et al. 2019, Li and Wang 2024b). Whereas our findings focus only on online orders, it could be extended to reflect broader industry dynamics in which digital engagement influences off-line behaviors. Luca (2016) further illustrates that even restaurants not directly accepting orders through digital platforms experience an increase in demand as a collateral benefit of the increased visibil ity that these platforms create, possibly enhancing overall business performance.

Heterogeneity analysis indicates that only indepen dent restaurants benefit from being added to the platform without a formal contract. This finding aligns with prior research that suggests food delivery platforms affect independent and chain restaurants differently (Li and Wang 2024b) and generalizes to independent ver sus chain businesses (De Vaan et al. 2021, Le Bot et al. 2023). Chain restaurants have more technological and financial resources as well as brand recognition, which may help them better withstand external shocks. Conversely, independent restaurants rely more on flexibility and creativity to adapt to changing market conditions. Hence, compared with chain restaurants, independent restaurants gain more from the flexible noncontracted partnership. Interestingly, nonpartnered restaurants experienced a larger increase in takeout orders by 41.02 after their addition but a smaller decrease of 14.31 upon delisting. Established customer relationships and loy alty may mitigate the negative impact of delisting, maintaining a certain level of demand via alternative takeout channels despite no platform visibility. Additionally, the similar asymmetric effects for partnered restaurants are justifiable because network expansion increases value for all, and the enhanced user activity would sus tain even if some restaurants are delisted. Finally, because chain restaurants invest heavily in customer relationships and loyalty programs at a brand level, both partnered and nonpartnered chain restaurants are shielded from the impact of delisting.

In the mechanism analysis section, we demonstrate that the visibility mechanism may be driving the outcome as seen by a larger impact on restaurants with high takeout abilities. However, our observations extend beyond mere visibility benefits. Following our findings on independent partnered establishments, the increase in the outcome may be driven by a composite effect of increased visibility, stronger cross-side network effects, and the consumer’s variety-seeking nature. This understanding highlights the multifaceted nature of platform dynamics and their differentiated impact on participants in a multichannel environment.

Finally, we reveal unintended consequences of a regulatory policy enactment that removes nonpartnered restaurants from the platform. The negative impact of delisting on takeout orders is more pronounced for independent restaurants. Chain restaurants do not experience significant effects either following the platform strategy change or after the retrospective regulation enactment.

Overall, our findings challenge the popular media narrative that untested policies, such as listing nonpartnered restaurants, are harmful for all platform participants despite limited empirical evidence. Our research shows that enabling passive involvement alters the competitive landscape and contributes to network effects in ways not yet documented in the literature. Our findings reveal that the inclusion of passive suppliers not only affects their own business through increased order volume but also positively influences the performance of partnered restaurants. In the process, we add to the discussion on alternative contract arrangements between the platform owner and other participants (Feldman et al. 2023). Our paper also adds to the ongoing discussion on the role of platforms in actively intervening to influence users’ intentions to participate on the platform by employing tactics such as knowledge seeding (Huang et al. 2018, Nagaraj 2021). Customer adoption increases for all suppliers when the platform activates passive suppliers using third-party deliverers.

## 5.1. Practical and Public Policy Implications

It is not uncommon for policymakers to respond to concerns raised by businesses and the media. The primary argument for forcing a delivery platform to delist nonpartnered restaurants from its platform is that such a regulatory policy would protect restaurants and consumers. However, our findings suggest that being listed as a nonpartnered restaurant on the platform does not necessarily harm the establishment. In fact, independent restaurants may benefit from being listed as nonpartnered. Furthermore, adding nonpartnered restaurants may also indirectly benefit partnered independent restaurants on the platform. Forcing the platform to delist nonpartnered restaurants may end up harming these restaurants.

We interpret this finding through the lens of policies impact on enhancing choices for platform participants (e.g., Mayya et al. 2021, Mayya and Viswanathan 2024). Banning nonpartnered restaurants on delivery platforms inadvertently reduced the choice available to these restaurants, some of which may have preferred to be on the platform as a nonpartnered restaurant as this provided them the opportunities to reach new consumers without having to invest in their in-house delivery capabilities or having to pay the commission fees as a partnered restaurant. In this regard, our paper adds to extant research in highlighting that retrospective policy enforcement may have unintended consequences (e.g., Li and Wang 2024b).

In addressing the complex interplay between food delivery platforms and restaurants, we offer multiple policy recommendations based on our findings. First, policymakers should allow noncontracted partnerships but develop guidelines that carefully delineate the liabilities between platforms and restaurants in scenarios involving noncontracted partnerships to ensure that consumer protection mechanisms are in place.<sup>28</sup> Together with existing platform-specific quality feedback systems for deliverers, these liability measures will help safeguard restaurants reputations. Second, improving transparency around extra fees charged to consumers for orders from nonpartnered establishments can help consumers make more informed purchasing decisions. Third, allowing restaurants to opt in or out of being listed on platforms addresses the need for greater control by restaurants over how their services are made available to customers. Regulators should empower restaurants by requiring platforms to give them ample notice before adding them. These evidence-based policy recommendations to regulators aim to enhance choices for both restaurants and consumers.

## 5.2. Future Research

We suggest several directions for future research based on our findings. First, it would be valuable to examine whether our findings apply to other multisided networks that involve external facilitators (e.g., deliverers) besides buyers and sellers. The restaurant industry is characterized by variety-seeking consumers, and hence, some of our results may be driven by this characteristic. It would be interesting to explore whether the results differ in other contexts, such as intracity courier services. Second, in our setting, the platform added nonpartnered restaurants without their consent. Future research should investigate how noncontracted partnerships affect complementors when they have a choice to opt in or out to better understand the impact of noncontract partnerships. Third, we use two exogenous shocks to measure the impact of being listed on and late delisted from the platform as a nonpartnered restaurant. Although we use matching and DiD methods, a quasiexperimental setting cannot completely eliminate selection issues. Researchers could collaborate with a multisided platform to randomly assign treatment to complementors, including the option to opt out. Such a research design can help understand who opts out and measure the outcomes. Next, a small proportion of the nonpartnered restaurants transitioned to partnered status. Future research should explore the reasons and impacts of using noncontracted partnerships to induce partnerships. Finally, this research focuses on takeout sales as they are the first order effects directly related to the impact of being listed on the platform. In practice, for some restaurants, having too many takeout orders might not always be optimal as they may interfere with dine-in service. Future research may use other data sources (e.g., survey of restaurant owners) to better understand each restaurant’s capacity constraints. This would allow a holistic evaluation of the heterogeneous effects of being listed on the platform, reflecting the broader industry dynamics in which digital engagement influences off-line behavior.

## Acknowledgments

R. Mayya sincerely thanks Yuxin Geng for his valuable help. The authors sincerely thank the senior editor, the associate editor, and three anonymous reviewers for their constructive engagement during the review process.

## Endnotes

<sup>1</sup> See Swiggy Genie—Anything you need, delivered! https://www. swiggy.com/swiggy-genie, accessed January 22, 2025.

<sup>2</sup> This is noted by some restaurants in Seattle Times and Chicago Tribune articles.

<sup>3</sup> Partnered restaurants may pay as high as 30% as the platform commission fee; see TribecaCitizen, Ranjan Roy, accessed January 22, 2025.

<sup>4</sup> Unlike partnered restaurants that pay commission fees and can control the menu, price, and promotions, nonpartnered restaurants do not pay commission fees and might not be aware of their listing on the platform.

<sup>5</sup> See “Grubhub Accused of Adding 150,000 Restaurants to App Without Permission,” CBS News, accessed January 22, 2025.

<sup>6</sup> Please see Section 3.1 for details on how the order is fulfilled when a consumer orders from a nonpartnered restaurant.

<sup>7</sup> In unreported tests, we expanded our coverage to include other states and territories with similar economic profiles: New York, Pennsylvania, New Jersey, Connecticut, Maryland, Virginia, and Texas as well as Washington, DC. The results are consistent.

<sup>8</sup> Grubhub is the third largest in the US as of 2024 - see Statista https://www.statista.com/statistics/1235724/market-share-us-fooddelivery-companies/, accessed January 22, 2025.

<sup>9</sup> See “Grubhub Adds 150K Non-partnered Restaurants as Controversy Grows,” Restaurant Dive, accessed January 22, 2025.

<sup>10</sup> Online Figure A1 also illustrates similarity in footfall across nonpartnered restaurants added at different time periods, underscoring the nondiscriminatory nature of Grubhub’s expansion in terms of restaurant selection.

<sup>11</sup> See “Grubhub Hit with Lawsuit for Listing Restaurants Without Permission,” Eater, accessed January 22, 2025.

<sup>12</sup> See “New California Law Requires Delivery Platforms to Have Direct Partnerships with Restaurants,” ABC News, accessed Janu ary 22, 2025.

<sup>13</sup> Out of 115,889 restaurants, 36,749 were partnered, 27,966 were nonpartnered, and 51,174 were not on the platform.

<sup>14</sup> Expanding the data set to include New York, Pennsylvania, New Jersey, Connecticut, Maryland, Virginia, and Texas as well as Wash ington, DC, did not change the results (unreported).

<sup>15</sup> As robustness checks, we also define takeout visits as those with a duration of (a) less than 20 minutes and (b) less than five minutes and present the results in Online Table A1.

<sup>16</sup> We drop 1.8% of restaurants in our sample that were added as nonpartnered restaurants but that signed formal partnership agreements during the duration of our panel.

<sup>17</sup> During robustness checks in Section 4.1.3, we use alternative measures, such as the natural log of RawTakeout or testing the sensitivity of the visit range between 0 and 5 minutes and 0 and 20 minutes.

<sup>18</sup> We thank the anonymous reviewer for suggesting this method.

<sup>19</sup> We thank the associate editor and anonymous reviewer for this suggestion.

<sup>20</sup> See Uber’s H3 geospatial indexing system, https://h3geo.org, accessed January 22, 2025.

<sup>21</sup> Please note that our revenue data set captures a subsample of all transactions, hence, the smaller absolute value.

<sup>22</sup> See “Delivery Platforms Need to Give Restaurants a Break,” Food & Wine, accessed January 22, 2025.

<sup>23</sup> We thank the anonymous reviewer for pointing us to an alternative mechanism.

<sup>24</sup> In an unreported table, we estimated Table 4 by including Yelp rating as a control variable; the results are consistent.

<sup>25</sup> See “The 2022 Restaurant Digital Divide: Turning First-Time Diners Into Loyal Customers.” PYMNTS, https://www.pymnts. com/wp-content/uploads/2022/11/PYMNTS-Restaurant-Digital Divide-November-2022.pdf, accessed January 22, 2025.

<sup>26</sup> We thank the anonymous reviewer for this recommendation.

<sup>27</sup> It is worth noting the asymmetric impact of listing and nonlisting: the positive effects of listing dominate the negative effect of delisting. This is discussed in detail in Section 5.

<sup>28</sup> For instance, what to do if a consumer faces health issues after consuming food from nonpartnered restaurants?

## References

Abadie A, Diamond A, Hainmueller J (2010) Synthetic control methods for comparative case studies: Estimating the effect of California’s tobacco control program. J. Amer. Statist. Assoc. 105(490): 493–505.

Ahuja K, Chandra V, Lord V, Peens C (2021) Ordering in: The rapid evolution of food delivery. McKinsey & Company. 22:1–13.

Athey S, Bayati M, Doudchenko N, Imbens G, Khosravi K (2021) Matrix completion methods for causal panel data models. J. Amer. Statist. Assoc. 116(536):1716–1730.

Austin PC, Small DS (2014) The use of bootstrapping when using propensity-score matching without replacement: A simulation study. Statist. Medicine 33(24):4306–4319.

Beck BB, Wuyts S, Jap S (2023) Guardians of trust: How review platforms can fight fakery and build consumer trust. J. Marketing Res. 61(4):682–699.

Boudreau K (2010) Open platform strategies and innovation: Granting access vs. devolving control. Management Sci. 56(10): 1849-1872.

Boudreau KJ, Hagiu A (2009) Platform rules: Multi-sided platforms as regulators. Gawer A, ed. Platforms, Markets and Innovation (Edward Elgar Publishing Limited, Cheltenham, UK), 163–191.

Burtch G, Carnahan S, Greenwood BN (2018) Can you gig it? An empirical examination of the gig economy and entrepreneurial activity. Management Sci. 64(12):5497–5520.

Butts K, Gardner J (2022) did2s: Two-stage difference-in-differences. R J. 14(3):162–173.

Callaway B, Sant’Anna PH (2021) Difference-in-differences with multiple time periods. J. Econometrics 225(2):200–230

Chen H, Hu YJ, Smith MD (2019) The impact of e-book distribution on print sales: Analysis of a natural experiment. Management Sci. 65(1):19–31.

Chen M, Hu M, Wang J (2022) Food delivery service and restaurant: Friend or foe? Management Sci. 68(9):6539–6551.

Chiou L, Tucker C (2020) Social distancing, internet access and inequal ity. Preprint, submitted April 13, https://ssrn.com/abstract=3574446.

Christians L (2020) Grubhub hubbub: Restaurants fire back at delivery companies that post menus without consent. The Cap Times (February 20), https://captimes.com/entertainment/dining/grubhubhubbub-restaurants-fire-back-at-delivery-companies-thatpost-menus-without-consent/article\_45c1a4a0-d4e5-56d8-b93e-208f5e1e5c3b.html.

Circuit (2022) Average spend per order on selected online food delivery services in the United States in 2022. Accessed January 22, 2025, https://www.statista.com/statistics/1358873/ average-food-delivery-spend-per-order-us/.

Cohen M, Sundararajan A (2015) Self-regulation and innovation in the peer-to-peer sharing economy. Univ. Chicago Law Rev. 82(1):116–133.

Cusumano MA, Gawer A, Yoffie DB (2021) Can self-regulation save digital platforms? Indust. Corporate Change 30(5):1259–1285.

De Vaan M, Mumtaz S, Nagaraj A, Srivastava SB (2021) Social learning in the covid-19 pandemic: Community establishments’ closure decisions follow those of nearby chain establishments. Management Sci. 67(7):4446–4454.

Dou Y, Wu D (2021) Platform competition under network effects: Piggybacking and optimal subsidization. Inform. Systems Res. 32(3):820–835.

Dowty D (2021) CNY restaurant fights back against Grubhub’s unauthorized deliveries: They’re illegal, owners charge. Accessed January 22, 2025, https://www.syracuse.com/food 2021/06/cny-restaurant-fights-back-against-grubhubs-unauthorizeddeliveries-theyre-illegal-owners-charge.html.

Economides N, Viard VB (2006) Pricing of complementary goods and network effects. Preprint, submitted August 15, https:// ssrn.com/abstract=2118273.

Eisenmann T, Parker G, Van Alstyne M (2011) Platform envelopment. Strategic Management J. 32(12):1270–1285.

Farronato C, Fong J, Fradkin A (2023) Dog eat dog: Measuring net work effects using a digital platform merger. Management Sci. 70(1):464–483.

Feldman P, Frazelle AE, Swinney R (2023) Managing relationships between restaurants and food delivery platforms: Conflict, con tracts, and coordination. Management Sci. 69(2):812–823.

Frieden R (2017) The internet of platforms and two-sided markets: Legal and regulatory implications for competition and consu mers. Preprint, submitted October 13, https://dx.doi.org/10. 2139/ssrn.3051766

Gao H, Zhang W (2017) Employment nondiscrimination acts and corporate innovation. Management Sci. 63(9):2982–2999.

Gawer A, Srnicek N (2021) Online platforms: Economic and societal effects. Accessed January 22, 2025, https://www.europarl.europa. eu/RegData/etudes/STUD/2021/656336/EPRS\_STU(2021)656336\_ EN.pdf.

Goodman-Bacon A (2021) Difference-in-differences with variation in treatment timing. J. Econometrics 225(2):254–277.

Ho YJ, Dewan S, Ho YC (2020) Distance and local competition in mobile geofencing. Inform. Systems Res. 31(4):1421–1442.

Huang P, Tafti A, Mithas S (2018) Platform sponsor investments and user contributions in knowledge communities: The role of knowledge seeding. MIS Quart. 42(1):213–240.

Huntington-Klein N (2020) Calculating absolute visit counts in safegraph data. Unpublished, submitted October 11, https://nickch-k. github.io/SafeGraphAbsoluteNumbers/Absolute\_Numbers\_ Report.html.

Katz ML, Shapiro C (1994) Systems competition and network effects. J. Econom. Perspect. 8(2):93–115.

Le Bot C, Perrigot R, Cliquet G (2023) Franchise vs. independent retail and service stores: Customer perceptions. Hendrikse GWJ, Cliquet G, Hajdini I, Raha A, Windsperger J, eds. Networks in International Business: Managing Cooperatives, Franchise and Alliances (Springer, Cham, Switzerland), 171–200.

Li Z, Wang G (2024a) On-demand delivery platforms and restaurant sales. Management Sci., ePub ahead of print October 16, https:// doi.org/10.1287/mnsc.2021.01010.

Li Z, Wang G (2024b) Regulating powerful platforms: Evidence from commission fee caps. Inform. Systems Res., ePub ahead of print February 28, https://doi.org/10.1287/isre.2022.0191.

Liu X, Lynch L (2011) Do agricultural land preservation programs reduce farmland loss? Evidence from a propensity score matching estimator. Land Econom. 87(2):183–201.

Luca M (2016) Reviews, reputation, and revenue: The case of yelp. com. Preprint, submitted 16 Mar, http://dx.doi.org/10.2139/ ssrn.1928601.

Mack EA, Grubesic TH (2009) Broadband provision and firm location in Ohio: An exploratory spatial analysis. J. Econom. Human Geography 100(3):298–315.

Mayya R, Viswanathan S (2024) Delaying informed consent: An empirical investigation of mobile apps’ upgrade decisions. Management Sci., ePub ahead of print December 2, https://doi org/10.1287/mnsc.2022.00334.

Mayya R, Ye S, Viswanathan S, Agarwal R (2021) Who forgoes screening in online markets and why? Evidence from Airbnb MIS Quart. 45(4):1745–1776.

McAfee A, Brynjolfsson E (2008) Investing in the IT that makes a competitive difference. Harvard Bus. Rev. 86(7/8):98–107.

McCart M (2019) Wary of third-party delivery, some restaurateurs say, “it’s a parasitic relationship.” Accessed January 22, 2025, https:// www.post-gazette.com/life/dining/2019/03/11/food-delivery pittsburgh-grubhub-uber-eats-doordash/stories/201903040106.

McCarthy (2024) How to partner with DoorDash: Your complete guide to third party delivery. Accessed January 22, 2025, https://merchants.doordash.com/en-us/blog/how-to-partnerwith-a-third-party-delivery-service.

Nagaraj A (2021) Information seeding and knowledge production in online communities: Evidence from OpenStreetMap. Manage ment Sci. 67(8):4908–4934.

Parker GG, Van Alstyne MW (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10): 1494–1504.

Peek S (2024) Should your restaurant be on grubhub? Accessed January 22, 2025, https://www.business.com/articles/is-grubhub good-for-restaurants/.

Raj M, Sundararajan A, You C (2020) Covid-19 and digital resilience: Evidence from Uber Eats. Preprint, submitted June 16, https:// dx.doi.org/10.2139/ssrn.3625638

Reshef O (2023) Smaller slices of a growing pie: The effects of entry in plat form markets. Amer. Econom. J. Microeconomics 15(4):183–207.

Rochet JC, Tirole J (2003) Platform competition in two-sided markets. J. Eur. Econom. Assoc. 1(4):990–1029.

Roth J, Sant’Anna PH (2023) Efficient estimation for staggered rollout designs. J. Political Econom. Microeconomics 1(4):669–709.

Saxena J (2019) Grubhub’s new strategy is to be an even worse partner to restaurants. Accessed January 22, 2025, https://www.eater. com/2019/10/30/20940107/grubhub-to-add-restaurants-withoutpermission-like-postmates/.

Saxena J (2020) Grubhub hit with lawsuit for listing restaurants without permission. Accessed January 22, 2025, https://www.eater. com/21537215/restaurants-sue-third-party-delivery-service grubhub-for-listing-businesses-without-permission.

Smith JA, Todd PE (2005) Does matching overcome LaLonde’s critique of nonexperimental estimators? J. Econometrics 125(1–2):305–353.

Sun L, Abraham S (2021) Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. J. Economet rics 225(2):175–199.

Teng H, Xia Q, Shou J, Zhao J (2023) Positive or negative spillover? The influence of online channel satisfaction on offline channe adoption. J. Bus. Res. 154:113332.

Xu Y (2017) Generalized synthetic control method: Causal inference with interactive fixed effects models. Political Anal. 25(1):57–76.

Xu K, Chan J, Ghose A, Han SP (2017) Battle of the channels: The impact of tablets on digital commerce. Management Sci. 63(5): 1469–1492.

Zhang S, Pauwels K, Peng C (2019) The impact of adding online-to offline service platform channels on firms’ offline and total sales and profits. J. Interactive Marketing 47:115–128.

Zhu F, Iansiti M (2012) Entry into platform-based markets. Strategi Management J. 33(1):88–106.

Zhu F, Iansiti M (2019) Why some platforms thrive and other don’t. Harvard Bus. Rev. 97(1):118–125.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
