---
otero_id: 5012
otero_key: "Y7G7VYN9"
title: "A Strategic Group Analysis of Competitor Behavior in Search Advertising"
authors: "Cheng Nie; Zhiqiang (Eric) Zheng; Sumit Sarkar"
year: "2021"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00710"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2021

# A Strategic Gr  oup Analysis of Competit   or Beha  vior in Sear  ch Advertising

Cheng Nie , cheng@chengnie.com

Zhiqiang (Eric) Zheng

, ericz@utdallas.edu

Sumit Sarkar

, sumit@utdallas.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# A Strategic Group Analysis of Competitor Behavior in Search Advertising

Cheng Nie<sup>1</sup>, Zhiqiang (Eric) Zheng<sup>2</sup>, Sumit Sarkar<sup>3</sup>

<sup>1</sup>Iowa State University, USA, cheng@chengnie.com <sup>2</sup>University of Texas at Dallas, USA, ericz@utdallas.edu <sup>3</sup>University of Texas at Dallas, USA, sumit@utdallas.edu

## Abstract

Firms compete intensely in sponsored search. Their bidding strategies hinge on understanding who competes with whom, how they compete, and how consumers react to competing advertisements. In this context, we investigate how firm competition impacts consumers’ click-through behaviors in search advertising from a strategic group perspective. Using search results from Google and consumers clickstream data, we found strong negative externality for competitors within the same strategic group relative to competitors across strategic groups: firms reap fewer click-throughs when an advertisement of another firm from the same strategic group is also displayed in search results, relative to when other displayed advertisers are not from the same group. This indicates that when competitors from the same strategic group are likely to appear in the results of a sponsored search auction, the focal firm would be better off avoiding head-to-head competition in the auction. However, we did not find empirical evidence of such firm behaviors, suggesting myopia or the inability of firms to avoid such competition. We also show that when multiple firms from the same strategic group appear in search results, the closer the focal firm is located to such competing firms, the more click-throughs the firm accrues. This suggests that firms should stay close to their within-group competitors when they compete in the same search auction. Further, our empirical results indicate that firms are indeed doing so. Using another set of data from Google AdWords reports, we show that our findings are also robust to multi-keyword bidding scenarios. These findings represent the first attempt to understand the impact of strategic groups in search advertising and provide interesting implications for advertisers and search engines.

Keywords: Search Advertising, Competition, Click-Through Rate (CTR), Strategic Groups

Giri Kumar Tayi was the accepting senior editor. This research article was submitted on November 13, 2019 and underwent two revisions.

## 1 Introduction

By enabling advertisers to precisely target prospective users based on their search terms, search advertising, has become an indispensable part of the advertising landscape. Spending on search advertising has continued to grow over the last decade, accounting for 44% of the \$124.6 billion digital advertising market in

2019. <sup>1</sup> Advertisements in a sponsored search are typically sold via auctions, and advertisers often pay considerable sums of money when their advertisements are clicked on by users. Consequently, managers of advertising firms need to routinely make several key decisions when participating in sponsored search auctions. These include which keywords to bid on, what the ideal rank (slot) to obtain is, how much to bid, when to activate or pause advertising campaigns, etc. Such decisions dwell on a critical piece of information—who are the firm’s main competitors (in an auction for a keyword) and what are their bidding strategies? Such decisions are faced by every firm that participates in sponsored search auctions.

Not surprisingly, search advertising has attracted a growing interest in the information systems, marketing, and economics literatures. Early research in this area focused on issues such as designing auction and ranking mechanisms while examining payoffs to the parties involved (e.g., Edelman et al., 2007; Feng et al., 2007; Weber & Zheng, 2007). Several researchers have attempted to characterize equilibrium bidding strategies (Edelman & Ostrovsky, 2007; Varian, 2007; Zhang & Feng, 2011). Based on the observation that advertisers typically receive higher click-through rates (CTR) when they appear higher in the search listings, these studies have modeled the net CTR of an advertisement as a function of its position and quality (e.g., the quality of its advertisement or, analogously, the quality of its products and services). However, they seldom examine how the CTR depends on competing advertisements appearing in other positions of the same search results.

A few researchers have considered more nuanced notions of competition, recognizing the negative externality imposed by other firms on the CTR of a focal firm’s advertisement. For example, Jeziorski and Segal (2015) noted that the CTR for an advertisement in a given position depends on which advertisements are shown above or below it, suggesting that the focal advertiser needs to know which advertisers it is competing with. Jerath et al. (2011) highlighted the possibility of a position paradox in a market with vertically differentiated firms, where a superior firm is able to obtain more clicks than an inferior firm when its advertisement appears below the inferior one. Animesh et al. (2009) focused on two attributes to differentiate sponsored search auctions: price and quality. They found that the effects of a firm’s strategy (price- versus quality-differentiation) and of the obtained rank (position) on its advertisement’s CTR are moderated by the firm’s ability to differentiate itself from its immediately adjacent rivals in the ranked listing.

While these studies provide additional insights regarding potential negative externality effects of competitors (i.e., rank externality) on a firm’s advertising strategy, they are restricted to considering differences along two dimensions—quality and price—in a generic manner. Further, they considered only a small set of competitors. Jerath et al. (2011) modeled two advertisers in their analysis, while Animesh et al. (2009) based much of their findings on a “window-of-three” approach where advertisers appearing immediately above and below a focal advertisement are considered to be competitors. An interesting phenomenon in sponsored search auctions is that for many keywords there are a large number of advertisers bidding for slots. Further, the competing advertisers are heterogeneous in multiple ways. Some advertisers may be large retail chains, and some may be much smaller retailers; some may be manufacturers as opposed to retailers. For example, advertisers for the keyword “outdoor furniture covers” include big retailers such as JCPenney, Target, Lowes, and Home Depot, as well as specialized furniture cover makers such as Empire Patio, Patio Plus Outdoor, and Patio Furniture USA. Additionally, as there is virtually no entry barrier to prevent any advertiser to bid on a keyword, the final results of an auction can appear perplexing, with heterogeneous advertisers appearing at different ranks. The competitive strategy that applies to one type of rival may not be equally relevant to another. This motivates us to examine how advertisers react to the complex competitive environment in sponsored search auctions, given rank externality and competitor heterogeneity.

The questions we examine lie at the very heart of a firm’s strategic decisions: Who competes with whom and how do competitors react to each other’s actions? In the context of search advertising, we seek to examine how consumers react to competing advertisements from such heterogeneous firms and the associated bidding strategies by the firms. The sponsored search advertising literature has yet to provide a systematic approach to prescribe the structure of the competitive environment. To this end, we draw on the theory of strategic groups, a central construct in the strategy literature to diagnose the competitive structure in a market (e.g., Cool & Schendel, 1987; Fiegenbaum & Thomas, 1995; Short et al., 2007). Porter (1979) formalizes the notion of a strategic group to be a group of firms that closely compete against each other within an industry, and where firms in the same group are similar to one another along key strategic dimensions (e.g., degree of vertical integration and extent of product diversity). Firms within a strategic group recognize their mutual dependence more markedly than dependence on firms outside the group and select the members of that group as their key competitors (Kotler & Armstrong, 1989). Fiegenbaum and Thomas (1995) note that a strategic group establishes a reference point for group members when they make strategic decisions. Strategic group theory has been widely used in traditional offline markets to theorize performance differences across firms (e.g., Mas‐Ruiz et al., 2014; Mas‐Ruiz & Ruiz‐Moreno, 2011; Short et al., 2007). Yet little is known about how strategic groups influence firms’ decisions to cooperate or compete in online markets like sponsored search. By theorizing on the behaviors of firms in a competitive market, the strategic group literature provides a new lens to delineate the structure of otherwise seemingly unstructured markets in sponsored search.

We examine strategic groups in the context of sponsored search, where advertisers pay to appear for a sponsored position in the results of a search engine. Consumers visit the sites of those advertisers they deem relevant by clicking on links. Search engines serve as an intermediary that connects consumers and firms, providing an ideal test bed to investigate the impact of strategic groups on consumers and to further tie their behaviors to the advertising strategies of competing firms.

Studying the competitive structure in sponsored search is of considerable significance. Spending on digital advertising is growing faster than any other form of advertising and is expected to surge to \$517 Billion worldwide in 2023.<sup>2</sup> Sponsored search advertising has become one of the main venues for firms to compete for consumers. The intensity of competition in sponsored search advertising is substantial and firms are willing to pay dearly for advertising slots because of the ability to target consumers who are actively seeking specific products or services (Animesh et al., 2011; Ghose & Yang, 2009).

Building on strategic group theory, we investigate whether membership in such groups plays a role in influencing the competition outcome in terms of CTR from the consumer side. If it does, then do firms respond strategically to attract more clicks? Does a firm participate in a sponsored search auction where a competitor in the same strategic group is likely to appear? When multiple firms from the same strategic group appear in the search results, does a firm try to position its advertisement to appear close to those of its main competitors (e.g., to signal its quality), or does it position its advertisement away from such competitors (e.g., to better differentiate itself from its rivals)?<sup>3</sup>

We examine the aforementioned questions empirically. To accomplish this, we conducted analyses on two separate sets of data. The first set pertains to the digital camera market. We collected search results data for the keyword “digital camera” from Google during a five-month span from May 2009 to September 2009. Firms that participate in these sponsored search auctions are clustered into strategic groups based on the competitor information obtained from the Hoover’s and LexisNexis databases. We further acquired clickstream data for the same period from a leading marketing firm that measures media and internet audiences,<sup>4</sup> which include consumers’ entire clickstream history after they had searched for the keyword “digital camera” in Google.

The second dataset pertains to the market for leather covers for iPads. The data is from a retailer of leather products<sup>5</sup> and includes Google AdWords reports for advertisement positions and click-through rates for various keywords pertaining to iPad leather covers during April and May 2012. The firm also provided the corresponding Google search results data, including the rank and appearance of competitors for the same period. The data enabled us to examine whether the findings hold under a multi-keyword bidding scenario where a firm competes with potentially varying intensity on a set of related keywords.

We found strong evidence that the appearance of competitors from the same strategic group negatively influences the CTR of a focal firm. Firms do not (or cannot) strategically avoid their within-group competitors, though our results show that avoiding their within-group competitors would be beneficial to the firms. Interestingly, the negative impact on the CTR of an advertisement from a focal firm is mitigated if it is displayed closer to its within-group competitors. Further, we found evidence that firms within the same strategic group compete for similar spots in a search auction listing. Our findings are corroborated for multi-keyword bidding scenarios as well.

To our knowledge, this research represents the first attempt at examining firm competition and consumer reaction of the complex competitive structure of multiple advertisers in a search market from a strategic group perspective. Our findings have important implications for advertisers and search engine platforms. For advertisers, understanding how targeted consumers make choice decisions in the presence of strategic group competitors is crucial in formulating their strategy for sponsored search advertising. For search engine platforms, understanding how consumers click in such situations can help them better project the click-through rates.

We organize this paper as follows. First, we discuss the research hypotheses recognizing the role of strategic groups in sponsored search advertising. We next describe our data and methodology for identifying strategic groups. We then present the results of our analyses for the digital camera keyword, including several robustness checks. Thereafter, we extend our analyses to the multi-keyword bidding scenario. Finally, we discuss the implications of our work for both researchers and practitioners.

## 2 Hypotheses Development

We theorize in this section how consumers respond to ads from competing firms in search auctions and how firms may bid strategically in such auctions. An important characteristic in sponsored search auctions is the heterogeneity of advertisers in an auction, as competing advertisers from various industries with different sizes, foci, and business models often appear in the same auction. How competitor heterogeneity affects an advertiser’s behavior remains largely unanswered, and understanding this heterogeneity is an important step toward explaining the behavior of advertisers in sponsored search auctions. The strategic group theory offers such a lens to examine competitor heterogeneity. The theory asserts that the heterogeneity of competing firms can be largely captured by strategic groups. Further, the formation of competing firms into strategic groups embodies the strategy that individual firms will adopt, which in turn determines the performance of these firms (Leask & Parker, 2007; Mas‐Ruiz & Ruiz‐Moreno, 2011; Porter, 1979). In our analyses, we first consider the effect of heterogeneous competitors on consumer behavior and follow up with implications for the firms themselves.

## 2.1 The Competition Effect

What consumers see in the search results directly impacts a consumer’s choice set. This is often referred to as a consideration set, defined as the set of brands brought to mind on a particular choice occasion (Nedungadi, 1990). The contents and composition of a consumer’s consideration set depend on the consumer’s motives (Chakravarti & Janiszewski, 2003). Consumers often prefer to simplify their choice process by retaining consideration sets of easy-tocompare alternatives. By retaining comparable items in the consideration set, consumers can ease their information-processing efforts during the choice stage since it involves comparing information that is commensurable (Chakravarti & Janiszewski, 2003; Gentner & Markman, 1994; Medin et al., 1995). The need to retain easy-to-compare alternatives may stem from consumers’ need to minimize effort when making choices (Huber & Klein, 1991). This suggests that if two advertisers from the same strategic group show up in search results, consumers would be more likely to consider both since this helps ease the comparison effort, as opposed to the case in which the two advertisers are from different groups. Therefore, it may benefit a focal firm’s CTR if its advertisement is displayed together with that of its within-group competitors.

On the other hand, researchers have identified the negative externality effect exerted by competitors advertisements on the CTR of a focal advertiser (Animesh et al., 2009; Jerath et al., 2011; Jeziorski & Segal, 2015). Further, customers may intentionally prefer to consider firms that are quite different, owing to their desire for variety. By retaining maximally dissimilar items in their consideration set, consumers increase the likelihood of obtaining optimal alternatives (Chakravarti & Janiszewski, 2003). Such variety-seeking behavior is often driven by the inherent satisfaction of “novelty,” “unexpectedness,” “change,” and “complexity” in choice variations (Kahn, 1995; McAlister & Pessemier, 1982). These types of impetuses would be expected to prompt consumers to consider firms from different strategic groups because of the potential “novel” and “unexpected” offerings coming from firms in other strategic groups. Consequently, another factor that may adversely affect the CTR for an advertisement may be the appearance of advertisements from other firms within the same strategic group.

Therefore, when a competing firm from the same strategic group appears in the search results, this could lead to different outcomes about whether a consumer would visit the focal firm or not. On the one hand, consumers’ innate desire to minimize effort would drive them to visit the focal firm because of ease of comparison. On the other hand, consumers’ varietyseeking motives would lead them to be less inclined to visit multiple firms from the same strategic group. Because of these opposing forces, which one dominates becomes an empirical question.

We expect that the presence of competing ads would impose a direct substitution effect for all consumers. While it may also induce a complementarity effect, it only indirectly occurs for those customers who value ease of comparison. Overall, we believe that the substitution effect on the focal firm’s ad is stronger than the possible complementarity effect. Therefore, we postulate the following hypothesis:

H1a: The probability that a consumer visits a focal firm’s site when it appears in sponsored search results is lower if competing firms from the same strategic group also appear, in comparison to the case in which only firms from other strategic groups appear, ceteris paribus.

Next, we examine decisions from an advertising firm’s perspective. Of particular interest is whether an advertiser from a strategic group would choose to coappear with other advertisers from that group (leading to head-to-head competition in the auction) versus strategically avoiding such direct competition. The defining feature of a strategic group prescribes that firms within the same strategic group are more similar to each other, compared to firms from different strategic groups. The strategic group theory further asserts that firms within the same strategic group follow similar strategies and behave similarly in response to market opportunities or threats (e.g., Mas‐Ruiz & Ruiz‐Moreno, 2017; Porter, 1979; Thomas & Venkatraman, 1988). Within the sponsored search context, it means that advertisers within the same strategic group adopt more similar strategies (e.g., what value to place on a user click and whether or not to participate in a search auction) than advertisers from different strategic groups.

A similarity in the behavior of firms within a strategic group is also corroborated by the literature on institutional theory and the herding behavior of firms. According to institutional theory, a firm deviating from the group norm suffers from lower performance (Chen & Hambrick, 1995). This prompts firms within a strategic group to follow the behavior of the pack, leading to herding (e.g., Bikhchandani et al., 1992), where the behaviors of all the strategic group members tend to converge. Cachon et al. (2008) identify similar opposing forces in the context of offline search: a decrease in search cost could result in a competitionintensifying effect that reduces a firm’s chance of attracting customers and a market-expansion effect that attracts more customers for all firms. Through mathematical models, they show that the marketexpansion effect may dominate and suggest that appearing together with competitors would be preferable. Empirically, Murry and Zhou (2019) show that the market expansion effect (called agglomeration effect therein) could indeed dominate the competition effect. Based on these arguments, one would expect advertisers in the same strategic group to exhibit similar auction behaviors. This would be reflected in search results in which firms from the same strategic group tend to show up together.

On the other hand, the literature has documented some evidence that firms within the same strategic group may strategically avoid each other. Dranove et al. (1998) argue that the strategic group concept is important only if there is a relationship between group conduct and firm performance, and the real key to group-level effects is strategic interaction. Even when group members do not collude explicitly, Dranove et al. argue that they may display Cournot behavior, wherein firms act independently but take the actions of their peers into account. Competition in ad auctions can be costly for firms in sponsored search advertising, as firms will have to bid higher to compete for limited available slots (Agarwal et al., 2011). Therefore, avoiding other firms from the same strategic group may be more profitable.

When anticipating the appearance in the search results of advertisements from other within-group competing firms, a focal firm may either avoid bidding in that auction or join the competition by bidding.<sup>6</sup> On the one hand, a firm may benefit from the market-expansion effect when shown together with its within-group competitors. On the other hand, because of costly direct competition, it may benefit the focal firm if it is able to strategically avoid appearing together with its within-group competitors. Because the cost savings from avoiding each other is a direct benefit, while the benefit from competing head-on is indirect (contingent on how consumers actually behave), we expect the benefit from the former to outweigh that of the latter. Therefore, we postulate the following hypothesis from the firm’s perspective:

H1b: Firms are less likely to show up in search results when a within-group firm also appears in the results, ceteris paribus.

H1a and H1b postulate the impact of strategic groups in the search advertising context from the consumers (demand side) and the firms’ (supply side) perspectives, respectively. Assuming firms are strategic, it would be more likely that firms in the same strategic group would attempt to avoid each other in a sponsored search (i.e., H1b would be supported), if their co-appearance leads to lower click-through rates from consumers (i.e., if H1a is supported).

## 2.2 The Co-Location Effect

If an advertiser’s behavior is indeed influenced by its competitors from the same strategic group, the next question is whether its behavior converges or diverges from the group norm. In the sponsored search context, the behavior of interest is the decision an advertiser makes regarding its rank choices, i.e., whether to obtain ranks close to those of its core competitors (those within the same strategic group) on the search engine’s ranked sponsored links or stay away from those advertisers.

There is literature to suggest that the CTR for a focal firm may be lower if its ad is placed close to its competitors from the same strategic group. Das et al. (2008) find that high-quality directly competitive ads that are placed side by side in response to a query (e.g., ads by both Honda and Toyota in response to a search for “Japanese cars”) will reduce the effectiveness of each ad, and each diminishes the appeal of the other. This phenomenon is well known in traditional advertising channels. For example, in television advertising, television networks go to great efforts to satisfy their advertisers by ensuring that competing advertisements do not appear in the same commercial break. Similarly, in online advertising channels, Ghose et al. (2014) show that more alternatives presented to consumers led to lower conversions for all alternatives. This suggests that it may hurt advertisers when more competitors within the same group appear close to each other. In the context of sponsored search auctions, Animesh et al. (2009) find that an advertiser appearing in an immediately adjacent position of its competitor negatively impacts the competitor’s CTR, especially when it appears in the top ranks.

Arguments for firms benefiting from appearing close to their core competitors also exist. As mentioned earlier, Cachon et al. (2008) and Murry and Zhou (2019) show that the market-expansion effect may dominate the competition-intensifying effect, which would indicate that appearing close to its within-group competitors may benefit a focal firm’s CTR. The arguments associated with retaining comparable alternatives in consideration sets that were discussed for H1a also suggest that firms could benefit by staying close to their within-group competitors.

Therefore, by advertising at a spot similar to its withingroup competing firms, a focal firm faces two opposing forces that may drive its CTR: (1) the positive externality because of the reduced search cost and market expansion effect from nearby within-group competing firms, and (2) the negative externality because of the direct substitution effect from nearby within-group competing firms. In the context of sponsored search advertising with trademarked terms, it is found that competitors can “steal” 1-5% of the focal brand’s clicks by staying close to the trademark owner’s ad (Simonov et al., 2018). We similarly expect such spillover traffic to be positive for within-group competitors whose advertisements appear in close proximity, given that competitors have already shown up in the search results and the substitution effect is inevitable. Hence, within our context, we postulate:

H2a: The probability of a consumer visiting a focal firm’s site is higher when the firm shows up closer to its within-group competitors in search results than in the case in which it stays far away from its withingroup competitors, ceteris paribus.

Next, we examine the literature documenting the tension from a firm’s perspective in order to infer what it might do. Previous research on strategic groups has highlighted the fact that managers simplify their competitive space and examine recipes of strategic groups of competitors (instead of examining all the competitors individually) because of bounded rationality and informationprocessing limitations (Hodgkinson & Johnson, 1994). Thus, actions of strategic group members act as prototypes or frames of reference (Fiegenbaum & Thomas, 1995; Short et al., 2007) about which a focal firm’s managers seek information.

Several papers in the strategic group theory literature suggest that firms within the same group follow similar strategies and behave similarly in response to market opportunities or threats (e.g., Thomas & Venkatraman, 1988). Porter (1979) asserts that mutual dependency is recognized more readily for firms within a strategic group than between firms in different groups and thus leads to similar behaviors among firms within the same group. Ebbes et al. (2010) also argue that firms within a strategic group follow the same strategic recipes and compete more intensely with each other than do firms across strategic groups.<sup>7</sup> Several analytical studies on sponsored search auctions suggest that firms with similar strategies and profitability tend to make similar bids (Edelman & Ostrovsky, 2007; Varian, 2007); thus, it may be inferred that their advertisements would appear in close proximity in the search results.

Another argument for advertisers in the same strategic group to appear close to each other in an auction is provided by contrast-assimilation theory proposed in the social communication and advertising literatures (Desai et al., 2014; Hovland et al., 1958). According to this theory, when consumers see two brands simultaneously, they perceive brands that differ substantially in quality to be more different than they actually are and perceive similar brands to be more similar than they actually are. Thus, two advertisers from two different strategic groups (with different quality perceptions associated with the groups) may be harmful for brands with lower reputations. Conversely, similar firms (e.g., those within the same group) would have a higher incentive to appear close to each other because consumers would perceive those brands as belonging to a group with a similar reputation.

In sum, the theories on strategic groups and contrastassimilation suggest that firms within the same group may make similar decisions regarding what rank to target. On the other hand, findings from other studies on consumer behavior and sponsored search auctions suggest the opposite—it may be preferable for advertisers in the same strategic group not to appear close to each other. In a situation where firms within a strategic group are competing with each other, the focal firm is subject to the substitution effect no matter what. We believe that the firm will be better off by positioning itself closer to the competing firm to reap some positive spillover. We therefore expect the net benefit of appearing close to a within-group competitor to outweigh that of appearing far away. Thus, we postulate:

H2b: If a firm appears with its competitors in the same sponsored search results, the firm is more likely to appear closer to its within-group competitors than its across-group competitors, ceteris paribus.

H1b and H2b, taken together, identify strategies that firms may use to bid in sponsored search auctions. A focal firm can choose whether or not to show up together with its within-group competitors; if it does show up with such competitors, it can choose whether or not to bid for similar spots with its within-group competitors.

## 3 Data for the Digital Camera Market

We discuss here the dataset pertaining to the “digital camera” market (the data on iPad covers are discussed in Section 6). The data come from several sources. We first discuss in Section 3.1 the common approaches for strategic group identification. Then in Sections 3.2 and 3.3 we elaborate how strategic groups were obtained based on search results data from Google, and discuss how data on competing firms from the Hoover’s and Lexis-Nexis databases were used in our context. We lastly discuss in Section 3.4 data on consumers’ clickstream data from a third-party data provider, how they were used to identify sessions, and how the sessions were matched to the search results.

## 3.1 Strategic Group Identification Approaches

Previous studies have generally used cluster analysis and related techniques to identify strategic groups. The approaches have been broadly classified into three types based on different categories of measures (Nath & Gruca, 1997). The first type, which uses measures on economic factors constructed from archival data, is a popular way to characterize strategic groups in the literature (e.g., Cool & Schendel, 1987; Mas‐Ruiz & Ruiz‐Moreno, 2017; Short et al., 2007). For example, Cool and Schendel (1987) captured firms’ strategies based on two kinds of economic activities: scope and resource deployments pertaining to a firm’s operations. Scope deployment includes target market segments, the kinds of products offered in each segment, and the associated geographic reach in each segment, while resource deployment includes business-level deployments of cash, human, and materials resources. The second type uses measures constructed from perceptual data, typically elicited from firms’ managers. For example, Nath and Gruca (1997) identified strategic groups among acute-care hospitals by asking executives to rate institutions according to attributes that encompass medical and nursing staff, facilities, administration, etc. The third type uses direct measures where key competitors are identified by asking managers (supply-side) or consumers (demand-side) directly to identify relevant competitors. For example, Gripsrud & Grønhaug (1985) and Porac et al.(1995) directly asked managers about who their most important competitors are, while Hodgkinson et al. (1996) interviewed grocery shoppers to assess the similarities between different super-markets.

We identified strategic groups for the digital camera market using a variant of the third type. Instead of soliciting the list of competitors from managers or consumers, we identified key competitors through objective third-party resources such as the Hoover’s database, an authoritative source for determining competitors (Pant & Sheng, 2015), and the LexisNexis repository.

## 3.2 Extracting Advertisers from Google Search Results

For the main analyses, we first ran Perl scripts to extract the search results on Google.com for the search term “digital camera.” The digital camera market served as an ideal setting for addressing our research questions. First, it’s a market characterized by many heterogeneous firms: some are leading manufacturers like Canon and Nikon while some others are major retailers like Amazon and Best Buy. Second, digital cameras are high-involvement products that require a significant amount of search by consumers before they make purchase decisions. Therefore, it provides rich soil to understand how consumers search and click in search engines. In addition, this keyword has been examined earlier in both sponsored search advertising literature (e.g., Animesh et al., 2009; Jerath et al., 2014; Lu & Zhao, 2014), and management literature (Benner & Tripsas, 2012). All these factors make it challenging and appealing to understand its competitive market structure, rendering it a good candidate for identifying strategic groups and their impact on advertising effectiveness.

We collected the search data from Google approximately once every 1.5 hours during a five-month time window, which yielded data on 2,308 search results.<sup>8</sup> On average, 10.97 advertising firms appeared in sponsored search results. In total, the “digital camera” market resulted in 211 distinct advertisers being displayed.<sup>9</sup> The data exhibit a long tail: only 25% of the firms (i.e., 53 firms) appeared more than 20 times (i.e., in approximately 1% of all the search results we collected). To ensure meaningful analysis, we included the 53 advertisers that appeared in at least 20 sponsored search results.

## 3.3 Two-Step Process for Strategic Group Identification

We used a two-step process to identify the strategic groups among these 53 advertisers. In the first step, we obtained a set of main competitors for each advertiser from the Hoover’s database. It is important to note that using external data such as the Hoover’s database to identify strategic groups is necessary here. Because we needed to use the strategic group memberships to investigate consumers’ website visit behaviors, inferring the strategic group membership directly from consumers’ visit behaviors (as done in Ringel and Skiera (2016) where they visualize the competition network using consumer search data directly) would have led to endogeneity issues.

The Hoover’s database uses industry experts to identify relevant competitors of a firm based on a number of key attributes, including a company’s main business lines, its geographic rivalries, and the specific market segments it belongs to. It is recognized as a reliable source for competitor identification (Ghani et al., 2000; Ma et al., 2011; Pant & Sheng, 2015). We used another database (i.e., the Global Markets Direct database) in the LexisNexis repository as a secondary source to identify additional competitors that were not captured by the Hoover’s database. For each firm, we identified the top competing firms, as indicated by these databases. For example, Amazon, Best Buy, and eBay appear as frequent advertisers in the “digital camera” market, and the Hoover’s database lists eBay and Best Buy among the main competitors for Amazon. For some advertisers, neither Hoover’s nor LexisNexis list any competitors, and furthermore, they are not mentioned as a competitor to other firms in the list of advertisers. We included for further analyses all 29 firms for which we were able to identify at least one competitor from the list of firms (see Table 1).

The competitor list in Table 1 could not be directly used as strategic groups because the competition relationship is not necessarily reciprocal. One firm may be listed as a key competitor to many other firms, but these other firms may not be important competitors to this firm. For example, Walmart is an important competitor to Bonton, but not the other way around.

In the second step, we used a hierarchical clustering technique to identify strategic groups based on the sets of competitors shown in Table 1. In hierarchical clustering, existing clusters (consisting of one or more firms) are combined to form a single cluster in an iterative manner (Everitt et al., 2001; Harrigan, 1985). We derived a distance matrix across firms in the competitor list by first assigning a similarity score to each pair of firms and then normalizing this score into a distance measure between zero and one (a distance matrix is required by hierarchical clustering packages). The similarity score for the pair (i, j) was defined as the number of times firm i appeared in the same competitor set along with firm j. For example, Amazon and Best Buy had a similarity score of five as they appeared together in five competitor sets (the sets for Amazon, Best Buy, and three other firms, Buy, HHGregg, and Radio Shack). Intuitively, if firms i and j co-occur more often in the same competitor sets, the similarity score for cell $( i , j )$ should be higher and the two firms are more likely to belong to the same strategic group. To convert the similarity matrix into a distance matrix, we used the function $d _ { i j } = 1 - s _ { i j } \langle S$ to calculate the distance between two firms i and j where S is the maximum similarity score plus one. Our approach clustered firms in a manner such that each firm in a cluster could be viewed as a key competitor to every other firm in that cluster.

Following Nath and Gruca (1997), we used the Ward’s clustering method to identify the strategic groups; this method has been found to often outperform other hierarchical clustering methods (Jain & Dubes, 1988). The Ward’s clustering method is a bottom-up approach. It starts with isolated singleton clusters (i.e., each consisting of a single firm). Then it calculates the pairwise distance between all clusters and merges the two with the smallest distance into one cluster. The method continues merging the closest two clusters iteratively until only one cluster remains (this cluster will include all firms). The four groups with the members listed in Table 2 provide a reasonable representation of the strategic groups in the digital camera market. Our analyses considered these four strategic groups after eliminating the search engine information portals Bing, Google, and Yahoo. Excluding these search engine sites was necessary since they form the context of this study. Moreover, such information portals are websites that consumers may have visited with or without the need to search for “digital camera”; for example, consumers might set one of them as the homepage or as the default search tool. Based on the nature of firms included in each cluster (after dropping the information portals), we labeled the clusters as online retailers, manufacturers, offline retailers, and others, respectively.

Table 1. Firms and Their Competitors for the “Digital Camera” Market

<table><tr><td>Index</td><td>Firm</td><td>Competitors</td></tr><tr><td>1</td><td>Amazon</td><td>Best Buy, Google, HSN, Office Max, Sears, Staples, Walmart, Yahoo, eBay</td></tr><tr><td>2</td><td>Best Buy</td><td>Amazon, Bing, Dell, Office Max, Radio Shack, Sears, Sony, Staples, Target, Walmart, Yahoo</td></tr><tr><td>3</td><td>Bing</td><td>Google, Sony, Yahoo</td></tr><tr><td>4</td><td>Bonton</td><td>Sears, Target, Walmart</td></tr><tr><td>5</td><td>Buy</td><td>Amazon, Best Buy, eBay</td></tr><tr><td>6</td><td>Canon</td><td>Kodak, Nikon, Olympus, Philips, Samsung, Sony</td></tr><tr><td>7</td><td>Circuit City</td><td>Best Buy</td></tr><tr><td>8</td><td>Dell</td><td>Canon, Sony</td></tr><tr><td>9</td><td>eBay</td><td>Amazon, Bing, Google, HSN, NexTag, Office Max, Sears, Staples, Target, Walmart, Yahoo</td></tr><tr><td>10</td><td>Google</td><td>Bing, Yahoo</td></tr><tr><td>11</td><td>HHGregg</td><td>Amazon, Best Buy, Target</td></tr><tr><td>12</td><td>HSN</td><td>Amazon, eBay</td></tr><tr><td>13</td><td>Kmart</td><td>Best Buy, Staples, Target, Walmart</td></tr><tr><td>14</td><td>Kodak</td><td>Canon, Dell, Nikon, Olympus, Philips, Sony</td></tr><tr><td>15</td><td>NexTag</td><td>Amazon, Buy, Google</td></tr><tr><td>16</td><td>Nikon</td><td>Canon, Kodak, Olympus</td></tr><tr><td>17</td><td>Office Max</td><td>Best Buy, Radio Shack, Staples, Walmart</td></tr><tr><td>18</td><td>Olympus</td><td>Kodak, Philips</td></tr><tr><td>19</td><td>Philips</td><td>Samsung, Sony</td></tr><tr><td>20</td><td>Radio Shack</td><td>Amazon, Best Buy, Dell, Sears, Staples, Target, Walmart</td></tr><tr><td>21</td><td>RCWilley</td><td>Best Buy</td></tr><tr><td>22</td><td>RITZCamera</td><td>Best Buy, Target</td></tr><tr><td>23</td><td>Samsung</td><td>Philips, Sony</td></tr><tr><td>24</td><td>Sears</td><td>Best Buy, Radio Shack, Target, Walmart</td></tr><tr><td>25</td><td>Sony</td><td>Bing, Dell, Kodak, Philips, Samsung</td></tr><tr><td>26</td><td>Staples</td><td>Best Buy, Dell, Office Max, Radio Shack, Walmart</td></tr><tr><td>27</td><td>Target</td><td>Best Buy, Kmart, Sears, Walmart, eBay</td></tr><tr><td>28</td><td>Walmart</td><td>Best Buy, Bing, Kmart, Radio Shack, Sears, Staples, Target</td></tr><tr><td>29</td><td>Yahoo</td><td>Amazon, Bing, Google, eBay</td></tr></table>

Table 2. Clustering Results

<table><tr><td>Cluster</td><td>Firms</td></tr><tr><td>1</td><td>Amazon, eBay, HSN, Google, Bing, Yahoo</td></tr><tr><td>2</td><td>Canon, Kodak, Nikon, Olympus, Philips, Samsung, Sony</td></tr><tr><td>3</td><td>Best Buy, Dell, Office Max, Radio Shack, Sears, Staples, Target, Walmart</td></tr><tr><td>4</td><td>Bonton, Buy, Circuit City, HHGregg, Kmart, NexTag, RCWilley, RitzCamera</td></tr></table>

## 3.4 Clickstream Data and Browsing Behavior

We also obtained clickstream data from a third-party data vendor for the same period in which we collected the sponsored search data. The data include consumers’ entire clickstream histories after they searched the keyword “digital camera” in Google. Similar to the methods applied in Zheng et al. (2003), we grouped contiguous visits of webpages into sessions, using an inactivity threshold of 30 minutes to denote the beginning of a new session. We identified

8,181 sessions. Since we wanted to know how the search results affect consumers’ browsing behavior, we matched the visit sessions with the search results we collected in terms of recency: the search results that appeared most recently before the beginning of a clickstream session were matched to the session. In so doing, we mimicked the search results that the consumer would most likely have seen. If the closest preceding search results were more than two hours prior to the beginning of a clickstream session, we dropped the session since these results may not closely emulate the search results for that particular session.<sup>10</sup>

As a result, we were left with 6,716 sessions with matched search results out of the total 8,181 sessions. After carefully examining the clickstream data, we observed that several sessions did not include any visits to digital camera websites after an initial Google search. We limited our attention to the sessions that had at least one keyword related to digital cameras in any one of the URLs. In the end, we were left with 1,249 sessions for our analyses. We should reiterate that, in order to investigate the impact of strategic groups on consumers’ clickstream behavior, we could not use the sponsored search data or the clickstream data to derive strategic groups; it was essential to determine them exogenously from other data sources like the Hoover’s and LexisNexis databases.

## 4 Model and Analysis

To ensure that our data captured the impact of search advertising on consumer visits to a firm’s site, we first examined whether consumers were indeed visiting a firm more often if the firm participated in sponsored search. Specifically, for each matched clickstream session, we investigated whether any of the focal firms appeared in the search results and whether the appearance influenced the likelihood of the firm being visited.

Let the variable Visit<sub>ijt</sub> denote whether or not a focal firm i from group j is visited in session t. The variable $A p p e a r _ { i t }$ denotes whether or not the focal firm i appeared in the sponsored search results matched to session t. We used the logit model shown in Equation (1) (referred to as Model 1) to capture the influence of a focal firm’s appearance on a consumer’s visit pattern. We controlled for the fixed effects both for different strategic groups (using $\lambda _ { j } )$ and for different sessions (using $\delta _ { t } ) . ^ { 1 1 }$ 1

$$
\operatorname{Logit} \left(\text { Visit } _ {\mathrm{ijt}}\right) = \beta_ {0} + \beta_ {1} \text { Appear } _ {\mathrm{it}} + \lambda_ {\mathrm{j}} + \delta_ {\mathrm{t}} + \varepsilon_ {\mathrm{ijt}}\tag{1}
$$

Table 3 presents the estimated parameters and the corresponding standard errors (in parentheses). Column 1 displays findings from a basic model without any fixed effects. It shows that the coefficient for the variable Appear is positive and significant. This indicates that when a focal firm appears in the sponsored search ads, the chance of a customer visiting this firm is significantly higher than when the firm does not appear. When we added session fixed effects $\delta _ { t }$ and group fixed effects $\lambda _ { j }$ in Columns 2 through 4, the estimated coefficients for Appear were qualitatively unchanged. Even the most conservative estimate from these models (Column 3 with fixed effects for the groups) indicates that an appearance in the sponsored search results can significantly improve the likelihood of being visited. The odds ratio corresponding to the estimate in Column 3 is 2.05 $( \mathrm { e } ^ { 0 . 7 1 8 } )$ , suggesting that the appearance of a firm would increase the odds of being visited by a factor of 2.05. Taken together, these results establish the value to a firm’s participation in search advertising.

## 4.1 The Competition Effect

A focal firm’s advertisement shows up together with many other competing ads in sponsored search results. We are interested in how the CTR of a focal firm’s advertisement is influenced by the appearance of a within-group competitor’s ads. Such information could help a firm decide whether to participate in auctions in which a competitor is also likely to appear. For H1a, we examined whether consumers were more likely to visit a focal firm if a within-group competitor appeared in the same sponsored search results. We used Model 2 (shown as Equation 2) to determine this. Compared to Model 1, this model has the added term WCAppear, indicating the appearance of any competitor from the same strategic group as the focal firm i (i.e., appearance of a within-group competitor). If the estimated $\beta _ { 2 }$ is negative, it would imply that consumers are less likely to visit the focal firm (H1a is supported); if the estimate is positive it would imply the opposite (H1a is not supported).

$$
\begin{array}{r l} \text { Logit(Visit } _ {\text { ijt }}) = & \beta_ {0} + \beta_ {1} \text { Appear } _ {\text { it }} + \beta_ {2} \text { WCAppear } _ {\text { it }} \\ & + \lambda_ {\text { j }} + \delta_ {\text { t }} + \varepsilon_ {\text { ijt }} \end{array}\tag{2}
$$

Table 4 presents the results for Model 2. The coefficient for Appear is positive and significant, consistent with the estimation for Model 1. The coefficient of interest $, \beta _ { 2 }$ (for WCAppear), is negative and significant $( p < 0 . 0 1 )$ . Thus, our results indicate that the appearance of a within-group competitor hurts the CTR of a focal firm (H1a is supported). By avoiding its within-group competitor, a focal firm can boost, on average, its odds of being clicked by a factor of 1.24 $( \mathrm { e } ^ { 0 . 2 1 8 }$ based on the most conservative estimate from Column 3). In summary, our results present strong evidence of a negative externality in sponsored search—the CTR of a firm critically depends on whether a within-group competitor also shows up. This important effect has been notably overlooked by the extant search advertising literature. Because users generally examine search results sequentially from top to bottom (Granka et al., 2004), we further expect a within-group competitor to have a stronger impact on the CTR of a focal firm if it appears above the focal firm, instead of below it. In Appendix A, we examine and confirm this possibility.

Table 3. Appearance Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Appear_{it}$ </td><td>0.883***(0.046)</td><td>0.958***(0.048)</td><td>0.718***(0.049)</td><td>0.817***(0.052)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>32,474</td><td>32,474</td><td>32,474</td><td>32,474</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.024</td><td>0.086</td><td>0.086</td><td>0.161</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Table 4. Competition Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $\text{Appear}_{it}$ </td><td>0.872***(0.046)</td><td>0.938***(0.048)</td><td>0.675***(0.051)</td><td>0.768***(0.054)</td></tr><tr><td> $\text{WCAappear}_{it}$ </td><td>-0.474***(0.056)</td><td>-0.533***(0.061)</td><td>-0.218***(0.069)</td><td>-0.237***(0.077)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>32,474</td><td>32,474</td><td>32,474</td><td>32,474</td></tr><tr><td> $Pseudo R^2$ </td><td>0.028</td><td>0.091</td><td>0.087</td><td>0.161</td></tr><tr><td colspan="5">Note: ***p&lt; 0.01, **p&lt; 0.05, *p&lt; 0.1. Standard errors in parentheses</td></tr></table>

Because of the negative impact of ads from withingroup competitors on a focal firm’s CTR, it benefits the focal firm if it is able to appear without any other within-group competitors. In other words, a focal firm can boost its CTR if it can avoid other within-group competitors. A related question (H1b) is whether firms realize this and are strategically avoiding their withingroup competitors. To answer this, we next investigate whether a focal firm was more likely to appear if none of its within-group competitors appeared.

Take, for example, a particular within-group firm pair (X, Y). P(X) denotes the likelihood that Firm X appeared in the search results and P(¬Y) the likelihood that firm Y did not appear. Firm X may have avoided Firm Y when advertising if P(X|¬Y) > P(X); namely, if the conditional probability of X appearing given that Y did not appear was larger than the unconditional probability of X appearing. Note that this is equivalent to the notion of Lift in machine learning (Witten et al., 2011, p. 168). If Lift $( \mathrm { X } , \lnot \mathrm { Y } ) = \mathrm { P } ( \mathrm { X } | \lnot \mathrm { Y } ) / \mathrm { P } ( \mathrm { X } ) > 1$ , it indicates that the absence of Y increases the likelihood for the presence of X.<sup>12</sup>

Figure 1 presents the mean and 95% confidence interval of Lift(X, ¬Y) for within-group pairs (X, Y). It also depicts, as a reference, the horizontal line corresponding to Lift = 1. Figure 1 shows that Lift for within-group firm pairs was not significantly different from 1 (p-value 0.711). Thus, the withingroup firms were not strategically avoiding (or were unable to avoid) each other even though that meant hurting each other’s click-through performances (i.e., H1b is not supported). One potential explanation is that firms might not be able to strategically avoid each other even if they would like to. For example, Amazon appeared in 96% of the search results, which essentially left few opportunities for its within-group competitors to avoid it.

## 4.2 The Co-Location Effect

We established that firms are better off if they can avoid their within-group competitors. However, the other within-group competitors may not leave the focal firm many opportunities to advertise alone. Take our data sample as an example. Only 4.7% of the observations had no other within-group competitors appearing when a focal firm was displayed. It is indeed difficult for advertisers to find this small window of opportunity to avoid competition in ad auctions, nor is this small slice of opportunity likely to be adequate for their business needs. When competition is inevitable, should a focal firm appear closer or further away from their within-group competitors? To answer this question, we calculated the rank difference (RankDiff) between a focal firm and its closest within-group competitor and examined if RankDiff had an impact on the focal firm’s CTR. Specifically, we estimated Model 3 (Equation 3), where RankDiff denotes how far away a focal firm is from its closest within-group competitor in a particular session.

$$
\operatorname{Logit} \left(\text { Visit } _ {\mathrm{ijt}}\right) = \beta_ {0} + \beta_ {1} \text { RankDiff } _ {\mathrm{it}} + \lambda_ {\mathrm{j}} + \delta_ {\mathrm{t}} + \varepsilon_ {\mathrm{ijt}}.\tag{3}
$$

![](/api/attachments/Y7G7VYN9/fulltext/images/a666d5345bf71d86980c279b0e66f95e0bf886ac8a38a2e87e06304147782f27.jpg)  
The dashed horizontal line is the reference line where Lift is 1. The height of the bar corresponds to the mean; the error bars correspond to the 95% confidence intervals

Figure 1. Lift for Within-Group Firm Pairs  
Table 5. Co-Location Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $RankDiff_{it}$ </td><td>-0.112***(0.021)</td><td>-0.130***(0.026)</td><td>-0.132***(0.022)</td><td>-0.192***(0.028)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>8,297</td><td>8,297</td><td>8,297</td><td>8,297</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.006</td><td>0.073</td><td>0.069</td><td>0.163</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses</td></tr></table>

Note: \*\*\*p < 0.01, \*\*p < 0.05, \*p < 0.1. Standard errors in parentheses.

Table 5 presents the regression results for Model 3. The coefficient on RankDiff is negative and significant at the 1% level in all four specifications. The smaller the rank difference (the closer a focal firm is to its within-group competitor), the larger the CTR for the focal firm. More specifically, by staying one rank closer to its within-group competitor, a focal firm can boost, on average, its odds of being clicked by a factor of 1.12 $( \mathrm { e } ^ { 0 . 1 1 2 }$ taken from Column 1 with the most conservative estimate). Therefore, we found support for the co-location effect stated in H2a: an advertiser received more visits when it appeared closer to the other member(s) of its strategic group. This co-location effect is consistent with the predicted dominance of the market-expansion effect over the competition effect, which has been investigated analytically (Cachon et al. 2008) and empirically (Murry & Zhou, 2019). In other words, when the focal firm was competing in the same search auction with its competitor, locating its ad closer to (co-locate with) its within-group competitors benefited the focal firm in terms of higher clickthrough rates.

The concomitant question (H2b) is whether firms recognized this and incorporated this in their advertising strategy. That is, did firms strategically colocate closer to their within-group competitors? To answer this, we investigated whether firms from the same strategic group tended to stay closer to each other compared to firms from across groups.

Figure 2 presents the differences in the ads’ ranks (RankDiff) between pairs of firms. The mean was 4.4 for RankDiff of across-group firm pairs and 3.2 for that of within-group pairs. The difference in RankDiff between within-group pairs and across-group pairs was statistically significant (p-value < 0.01). Figure 2 provides model-free evidence that within-group firm pairs indeed tended to co-locate closer to each other, compared to across-group firm pairs.

We conducted a regression analysis by controlling for other factors that might influence the rank difference between firms. We regressed the rank difference (RankDiff) on a within-group indicator (Within) with fixed-effects controls at both the strategic group and session levels. We note that the unit of analysis was firm pairs (thus the subscript p) in Model 4.

$$
\text { RankDiff } _ {\mathrm{pjt}} = \beta_ {0} + \beta_ {1} \text { Within } _ {\mathrm{pt}} + \lambda_ {j} + \delta_ {t} + \varepsilon_ {\mathrm{ijt}}\tag{4}
$$

The strategic group fixed effects $\lambda _ { \mathrm { j } }$ account for grouplevel unobserved confounds such as a group’s valuation of ranks. Table 6 presents the results for Model 4. We found the estimated coefficient of Within (β<sub>1</sub>) was close to -1. Thus, a focal firm indeed stayed approximately one rank closer to its within-group competitors in contrast to its across-group competitors as indicated by both the model-free evidence and the model-based analysis (H2b is supported). These findings are consistent with the literature on strategic groups that shows that firms tend to use other group members as reference points to make business decisions (Fiegenbaum & Thomas, 1995; Short et al., 2007).

![](/api/attachments/Y7G7VYN9/fulltext/images/5aa5e954f1c6c844a1f68d8a5da73e404a94a14bbdf5cc8ef7bb362ae2c5de94.jpg)  
Note: Heights of the bars corresponds to the mean; the error bars correspond to the 95% confidence intervals  
Figure 2. Rank Difference (RankDiff) for All Firm Pairs (Across-Group or Within-Group)

Table 6. Impact of Within-Group Membership on Rank Difference

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Within_{pt}$ </td><td>-1.145***(0.027)</td><td>-1.161***(0.028)</td><td>-1.018***(0.033)</td><td>-1.033***(0.034)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>35,580</td><td>35,580</td><td>35,580</td><td>35,580</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.040</td><td>0.031</td><td>0.041</td><td>0.032</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

## 5 Robustness Checks

Our main analyses indicate that a consumer was less likely to visit a focal firm’s site when competing firms from the same strategic group also appeared in sponsored search results. From the perspective of the advertising firms, they did not (or were unable to) strategically avoid their within-group competitors. In addition, we found that when a focal firm appeared with competitors from its strategic group, consumers were more likely to visit the focal firm when it stayed closer to its within-group competitors. The firms appeared to recognize this and strategically located closer to their within-group competitors.

Our data span the relatively long period of five months. During this time span, a consumer’s interest may shift and influence the probability of the consumer visiting a particular firm. We conducted additional analyses that used Google Trends data to control for such potential change of interests and found the results to be qualitatively unchanged. These analyses are reported in Appendix B.

Google displays both the sponsored search results and the organic search results. The presence of organic search results may alter customers’ click behavior regarding the sponsored search results, which in turn could affect the firm’s behavior. In view of this, we further conducted another set of analyses to examine whether the organic search results might confound our findings—these experiments are presented in Appendix C. As discussed there, we considered the appearance of firms in either organic search results or sponsored search results (or both) when conducting the analyses. We found that our results were robust whether the organic search results were considered or not.

Overall, these checks reinforced our findings by showing that our analyses are robust to potential confounding factors like consumers’ shifting interest and the organic search results.

## 6 Multi-Keyword Bidding<sup>13</sup>

Thus far, we have discussed the competition across different firms for the market related to the search keyword “digital camera.” In practice, firms typically advertise on many variations of the same keyword, anticipating that customers will use multiple forms of search terms when searching for a product, e.g., “camera,” “digital camera,” “digital cameras,” “best digital camera,” etc. This is true for all firms selling similar products. As a result, the bidding behavior of a firm across related keywords (i.e., multi-keyword bidding) must account for similar actions by its competitors. Therefore, we examined whether our findings carry over to the multi-keyword bidding scenario.

In view of this, we acquired another set of data from a leather product retailer (hereafter referred to as the focal firm). The firm shared its advertisement data on leather cases for iPads, one of its popular product lines. Two types of data were provided: (1) Google AdWords data that provide the average positions of its ads and the CTRs for advertisements over 22 days during April and May 2012, and (2) the search results data from Google, including the appearance and rank of other competitors, during the same period.

The marketing managers of the firm identified their main competitors from a list of leather case manufacturers that advertise frequently for keywords related to “iPad leather case” as the group they strategically compete with. Specifically, the focal company identified three other firms (Skytop Leather, Mapicases, and Saddleback Leather) as belonging to the same strategic group.<sup>14</sup>

There were 23 unique keywords related to iPad leather cases that the focal firm bid on, as shown in Table 7. As evident from that list, all these keywords are related, in terms of either synonyms (case, cases, cover) or different qualifiers (genuine leather, iPad 2). For the focal firm on each day, Google AdWords reports data that include the CTRs aggregated over the previous 30 days for each keyword. We used the log odds of the CTRs as the dependent variable. Accordingly, we also aggregated the rank of a firm over the previous 30 days to match the way the dependent variable was aggregated in the source data. Therefore, the variable Appear<sub>it</sub> (WCAppear<sub>it</sub>) indicates the proportion of search results in which the focal firm (within-group competitors) appeared over the previous 30 days. Similarly, RankDiff<sub>it</sub> represents the mean rank difference between the focal firm and other within-group competitors over the previous 30 days.

After aggregating the data across the 23 iPad-related keywords, we obtained balanced panel data where each keyword had observations for the 22 periods (506 observations in total). We repeated the regression analyses for the three main effects of interest, namely appearance, competition, and co-location effects (Models 1, 2, and 3, respectively). Since the new dataset was about only one focal firm, controlling for the group fixed effects was not necessary. In addition, because observations for each variable (i.e., CTR and appearance) were aggregated over 30 days, controls for the sessionfixed effects did not apply either. Instead, we controlled for the keyword-fixed effects to account for the timeinvariant variability across the 23 unique keywords.

Table 8 summarizes the results for the multi-keyword bidding analyses. In the “appearance” column, the estimated coefficient for Appear is positive and statistically significant. It suggests that the appearance of the focal firm’s advertisements in the sponsored search results improved its chance of being visited. In the “competition” column, the estimated coefficient for WCAppear is negative and significant. It lends support to H1a: the appearance of other within-group competitors hurt the CTR for the focal firm. In the “co-location” column, RankDiff is negative and significant, suggesting that CTRs for the focal firm’s advertisements were boosted by staying closer to its within-group competitors (i.e., H2a is supported). Taken together, the estimated coefficients in Table 8 continue to lend support to H1a and H2a, demonstrating that these two findings continue to hold in the context of multi-keyword bidding.

When a firm places bids for multiple keywords, it may be willing to settle for a lower rank relative to its competitors on some keywords in order to be ranked higher on others. We next explored whether our findings were robust regardless of whether the focal firm was winning (ranked higher) or losing (ranked lower) in the search auctions. The average rank of the focal firm’s advertisement was the highest for the keyword “leather iPad” (1.01), while being the lowest for the keyword “iPad 2 leather case” (3.44). We used the median rank position (1.97) as a threshold to split the 23 unique keywords into two subsamples. The resulting subsample analyses are presented in Tables 9 and 10. The results are by and large consistent with the ones reported in Table 8. Both H1a and H2a are supported with one exception: the colocation effect becomes insignificant for the subsample where the focal firm is ranked in the topmost positions (Table 9). This is not altogether unexpected because when the focal firm’s ad was ranked in the topmost position (which occurred very often in this subsample), the spillover of click-throughs from ads of other within-group competitors became insignificant.

We next examine H1b and H2b in the multi-keyword bidding context. The focal firm shared with us 5,375 search results for the 23 keywords of interest. A total of 164 unique firms appeared in these search results. For each of the three within-group competitors of the focal firm (i.e., Skytop Leather, Mapicases, and Saddleback Leather), we identified an across-group comparable firm by examining how close these two firms were in terms of appearance frequency in the search results.

Table 7. 23 Unique Keywords Related to iPad Leather Cases

<table><tr><td>genuine leather case for ipad 2</td><td>ipad covers leather</td><td>leather ipad case</td></tr><tr><td>ipad 2 case leather</td><td>ipad leather case</td><td>leather ipad cases</td></tr><tr><td>ipad 2 cases leather</td><td>ipad leather cases</td><td>leather ipad cover</td></tr><tr><td>ipad 2 leather case</td><td>ipad leather cover</td><td>leather ipad covers</td></tr><tr><td>ipad 2 leather case with stand</td><td>leather case for ipad</td><td>leather ipad sleeve</td></tr><tr><td>ipad 2 leather cases</td><td>leather case for ipad 2</td><td>leather ipad2</td></tr><tr><td>ipad case leather</td><td>leather ipad</td><td></td></tr></table>

Table 8. Summary of Results for Multi-keyword Bidding Analyses

<table><tr><td>Variable</td><td>Appearance</td><td>Competition</td><td>Co-Location</td></tr><tr><td> $Apear_{it}$ </td><td>2.849***(0.768)</td><td>3.067***(0.747)</td><td></td></tr><tr><td> $WCAppear_{it}$ </td><td></td><td>-0.709***(0.130)</td><td></td></tr><tr><td> $RankDiff_{it}$ </td><td></td><td></td><td>-0.096***(0.028)</td></tr><tr><td>Keyword FE</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>506</td><td>506</td><td>506</td></tr><tr><td> $R^2$ </td><td>0.028</td><td>0.084</td><td>0.023</td></tr><tr><td colspan="4">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Table 9. Subsample Analysis for Keywords Where the Focal Firm is Ranked Above the Median

<table><tr><td>Variable</td><td>Appearance</td><td>Competition</td><td>Co-Location</td></tr><tr><td> $Appear_{it}$ </td><td>1.631***(0.572)</td><td>1.825***(0.560)</td><td></td></tr><tr><td> $WCAppear_{it}$ </td><td></td><td>-0.529***(0.144)</td><td></td></tr><tr><td> $RankDiff_{it}$ </td><td></td><td></td><td>-0.034(0.022)</td></tr><tr><td>Keyword FE</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>242</td><td>242</td><td>242</td></tr><tr><td> $R^2$ </td><td>0.034</td><td>0.088</td><td>0.010</td></tr><tr><td colspan="4">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Table 10. Subsample Analysis for Keywords Where the Focal Firm is Ranked Below the Median

<table><tr><td>Variable</td><td>Appearance</td><td>Competition</td><td>Co-Location</td></tr><tr><td> $Apear_{it}$ </td><td>6.690***(1.918)</td><td>6.784***(1.863)</td><td></td></tr><tr><td> $WCAppear_{it}$ </td><td></td><td>-0.796***(0.198)</td><td></td></tr><tr><td> $RankDiff_{it}$ </td><td></td><td></td><td>-0.232***(0.062)</td></tr><tr><td>Keyword FE</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>264</td><td>264</td><td>264</td></tr><tr><td> $Pseudo R^2$ </td><td>0.046</td><td>0.104</td><td>0.053</td></tr><tr><td colspan="4">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Table 11. Across-Group Competitors Closest in Appearance Frequency

<table><tr><td>Within-group competitor</td><td>Frequency</td><td>Across-group competitor</td><td>Frequency</td></tr><tr><td>Saddleback Leather</td><td>1,989</td><td>Mac-Case</td><td>2,058</td></tr><tr><td>Skytop Leather</td><td>1,683</td><td>Cases</td><td>1,608</td></tr><tr><td>Mapicases</td><td>1,495</td><td>TheSnugg</td><td>1,580</td></tr></table>

![](/api/attachments/Y7G7VYN9/fulltext/images/5096923f719cad09d52ffb35fa0c32eeb61f7b46d2a44958ce2473a995c58ed1.jpg)  
Note: The dashed horizontal line is the reference line where Lift is 1. The height of the bar corresponds to the mean; the error bars correspond to the 95% confidence intervals

Figure 3. Lift for Within-Group Firm Pairs (Multi-Keyword Bidding Analysis)  
![](/api/attachments/Y7G7VYN9/fulltext/images/3cd55d627031582ee67da73e527c06fa55969509756ae5635e873063beb6c115.jpg)  
Note: Heights of the bars corresponds to the mean; the error bars correspond to the 95% confidence intervals  
Figure 4. Rank Difference for All Firm Pairs (Multi-Keyword Bidding Analysis)

Table 12. Impact of Within-Group Membership on Rank Difference (Multi-Keyword Bidding Analyses)

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td></tr><tr><td> $Within_{pt}$ </td><td>-0.271***(0.044)</td><td>-0.329***(0.047)</td></tr><tr><td>Keyword FE  $λ_j$ </td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>16,448</td><td>16,448</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.002</td><td>0.021</td></tr><tr><td colspan="3">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

This ensures that a priori, advertisements of these two firms were presented to consumers approximately the same number of times. This is, in principle, analogous to the popular propensity score matching method and the placebo test (Rosenbaum & Rubin, 1983). For example, for the firm Saddleback Leather, which appeared in 1,989 sponsored search results, the closest across-group firm in terms of appearance frequency was Mac-Case, which appeared in 2,058 sponsored search results (the difference is within 3% of the appearance frequency for Saddleback Leather). Thus, Mac-Case was chosen as the comparable firm. The list of comparable firms and their corresponding frequencies are presented in Table 11.

For the four within-group competitors (including the focal firm), there are six $( ^ { 4 } \mathrm { C } _ { 2 } )$ within-group pairs; for the three across-group competitors, there are twelve (4  3) across-group pairs. These pairs were used to conduct the experiments corresponding to hypotheses H1b and H2b.

We first tested whether firms were strategically avoiding their within-group competitors (H1b). Figure 3 presents the mean and 95% confidence interval of Lift(X, ¬Y) for within-group pairs (X, Y). We found that Lift for within-group firm pairs was not significantly different from 1 (p-value 0.224). Thus, the within-group firms did not (or were unable to) strategically avoid each other even though that meant hurting each other’s clickthrough performances (i.e., H1b is not supported).

To address H2b, we investigated whether firms from the same strategic group tended to stay closer to each other, compared to firms from across groups. Figure 4 presents the differences in the ads’ ranks (RankDiff) between all pairs of firms. The mean for RankDiff is 5.06 for acrossgroup firm pairs and 4.79 for within-group pairs, and the difference in the means is statistically significant (pvalue < 0.01). Therefore, the figure provides model-free evidence that within-group firm pairs tend to co-locate closer to each other, compared to across-group firm pairs. In addition, we conducted a regression analysis by controlling for other factors that might influence the rank difference between firms. Similar to Model 4, we regressed the rank difference (RankDiff) on a withingroup indicator (Within) with fixed-effects controls at the keyword level. Table 12 provides the results of this analysis. The estimated coefficient for the variable Within demonstrates that the focal firm indeed stayed closer to its within-group competitors, in comparison to its across-group competitors (H2b is supported). In sum, the analyses from a multi-keyword bidding market provide results consistent with the results from the “digital camera” market.

## 7 Conclusion

Understanding consumers’ reactions to competing advertisers is important but has received very little attention in the search advertising literature. To our knowledge, this is the first paper that conducts a largescale empirical analysis to systematically study the competitive landscape in search advertising from both the consumer and the advertiser perspectives. Extant literature has not examined how advertisers compete in the search market comprising firms from different industries with differing sizes, foci, and business models. Our paper extends current research by examining the strategic group effect on the effectiveness of advertisements in search results. To this end, we build on the strategic group theory to examine how membership in such a group plays a role in sponsored search.

We contribute to the sponsored search literature by demonstrating that firms could improve their CTRs by avoiding within-group competitors. At the same time, when competition from such firms is inevitable, it is better for firms to appear proximal to their within-group competitors. As discussed by Dranove et al. (1998), even when the group members do not collude explicitly, they may take their peers’ actions into account when acting independently. Such strategic interactions among group members become easier in sponsored search using search engine optimization tools coupled with the ease with which a firm can learn about the bidding behavior of other firms (e.g., as discussed in Edelman and Schwarz, 2010, and Varian, 2007).

This study also enriches the advertising literature by studying consumers’ reactions to the complex competitive structure of advertisers using consumers actual click behavior in the search market. Using consumer-level clickstream data enabled us to analyze individual customers’ reactions to the exposure of search results at a finer granularity than the aggregated data commonly used in previous research (Rutz & Trusov, 2011; Rutz et al., 2011). Further, using another set of data from Google AdWords reports, we were able to show that our findings are robust to multikeyword bidding scenarios.

Our findings regarding the impact of strategic groups on consumers yield practical implications. First, we find that the appearance of within-group competitors can hurt the CTR of a focal firm and that firms potentially benefit from strategically avoiding each other. For example, a firm could choose to advertise more at time slots (e.g., afternoon or evening) when its within-group competitors do not (e.g., if they usually advertise in the morning). In addition, firms could also strategically advertise at different geographic locations using location targeting (Luo et al., 2013). Second, the CTR for a focal firm is higher if its ad is closer to its within-group competitors. Therefore, a firm could reduce the negative impact of competing ads by staying proximal to its within-group competitors when it is unable to avoid competition in ad auctions. Lastly, search engines like Google typically embrace the CPC (cost per click) model in which they are paid only when consumers actually click on the links. Therefore, search engines could potentially factor in the presence of multiple firms within a strategic group when projecting the CTRs for ads.

Our paper leaves several issues open for further investigation. When estimating the impact of strategic groups, we do not drill down into the characteristics of the identified strategic groups. We only considered the broad impact incurred by firms within or across groups. It is possible that the impact on consumers might be different, depending on which specific group a firm belongs to and at what stage of consumption the consumers may be in (e.g., purchase or information collection). These possibilities warrant exploration in future research.

## References

Agarwal, A., Hosanagar, K., & Smith, M. D. (2011). Location, location, location: An analysis of profitability of position in online advertising markets. Journal of Marketing Research, 48(6), 1057-1073.

Animesh, A., Ramachandran, V., & Viswanathan, S. (2009). Quality uncertainty and the performance of online sponsored search markets: An empirical investigation. Information Systems Research, 21(1), 190-201.

Animesh, A., Viswanathan, S., & Agarwal, R. (2011). Competing “creatively” in sponsored search markets: The effect of rank, differentiation strategy, and competition on performance. Information Systems Research, 22(1), 153-169.

Benner, M. J., & Tripsas, M. (2012). The influence of prior industry affiliation on framing in nascent industries: The evolution of digital cameras. Strategic Management Journal, 33(3), 277- 302.

Bikhchandani, S., Hirshleifer, D., & Welch, I. (1992). A theory of fads, fashion, custom, and cultural change as informational cascades. Journal of Political Economy, 100(5), 992-1026.

Cachon, G. P., Terwiesch, C., & Xu, Y. (2008). On the effects of consumer search and firm entry in a multiproduct competitive market. Marketing Science, 27(3), 461-473.

Caves, R. E., & Porter, M. E. (1977). From entry barriers to mobility barriers: conjectural decisions and contrived deterrence to new competition. The Quarterly Journal of Economics, 91(2), 241.

Chakravarti, A., & Janiszewski, C. (2003). The influence of macro‐level motives on consideration set composition in novel purchase situations. Journal of Consumer Research, 30(2), 244-258.

Chen, M.-J., & Hambrick, D. C. (1995). Speed, stealth, and selective attack: how small firms differ from large firms in competitive behavior. The Academy of Management Journal, 38(2), 453- 482.

Choi, H., & Varian, H. (2012). Predicting the present with google trends. Economic Record, 88(S1), 2-9.

Cool, K. O., & Schendel, D. (1987). Strategic group formation and performance: The case of the u.s. pharmaceutical industry, 1963-1982. Management Science, 33(9), 1102-1124.

Das, A., Giotis, I., Karlin, A. R., & Mathieu, C. (2008). On the effects of competing advertisements in keyword auctions. Proceedings of the ACM Conference on Electronic Commerce (pp. 51- 63).

Desai, P. S., Shin, W., & Staelin, R. (2014). The company that you keep: When to buy a competitor’s keyword. Marketing Science, 33(4), 485-508.

Dranove, D., Peteraf, M., & Shanley, M. (1998). Do strategic groups exist? An economic framework for analysis. Strategic Management Journal, 19(11), 1029-1044.

Du, R. Y., Hu, Y., & Damangir, S. (2015). Leveraging trends in online searches for product features in market response modeling. Journal of Marketing, 79(1), 29-43.

Du, R. Y., & Kamakura, W. A. (2012). Quantitative trendspotting. Journal of Marketing Research, 49(4), 514-536.

Ebbes, P., Grewal, R., & DeSarbo, W. S. (2010). Modeling strategic group dynamics: A hidden Markov approach. Quantitative Marketing and Economics, 8(2), 241-274.

Edelman, B., & Ostrovsky, M. (2007). Strategic bidder behavior in sponsored search auctions. Decision Support Systems, 43(1), 192-198.

Edelman, B., Ostrovsky, M., & Schwarz, M. (2007). Internet advertising and the generalized second price auction: Selling billions of dollars worth of keywords. American Economic Review, 97(1), 242-259.

Edelman, B., & Schwarz, M. (2010). Optimal auction design and equilibrium selection in sponsored search auctions. American Economic Review, 100(2), 597-602.

Everitt, B. S., Landau, S., & Leese, M. (2001). Cluster analysis. Taylor & Francis.

Feng, J., Bhargava, H. K., & Pennock, D. M. (2007). Implementing sponsored search in web search engines: Computational evaluation of alternative mechanisms. INFORMS Journal on Computing, 19(1), 137-148.

Fiegenbaum, A., & Thomas, H. (1995). Strategic groups as reference groups: Theory, modeling and empirical examination of industry and competitive strategy. Strategic Management Journal, 16(6), 461-476.

Gentner, D., & Markman, A. B. (1994). Structural alignment in comparison: No difference without similarity. Psychological Science, 5(3), 152-158.

Ghani, R., Jones, R., Mladenic, D., Nigam, K., & Slattery, S. (2000). Data mining on symbolic knowledge extracted from the web. Proceedings of the Sixth International Conference on Knowledge Discovery and Data Mining (pp. 29-36).

Ghose, A., Ipeirotis, P. G., & Li, B. (2014). Examining the impact of ranking on consumer behavior and search engine revenue. Management Science, 60(7), 1632-1654.

Ghose, A., & Yang, S. (2009). An empirical analysis of search engine advertising: Sponsored search in electronic markets. Management Science, 55(10), 1605-1622.

Granka, L. A., Joachims, T., & Gay, G. (2004). Eyetracking analysis of user behavior in WWW search. Proceedings of the 27th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (pp. 478-479).

Gripsrud, G., & Grønhaug, K. (1985). Structure and strategy in grocery retailing: a sociometric approach. The Journal of Industrial Economics, 33(3), 339-347.

Harrigan, K. R. (1985). An application of clustering for strategic group analysis. Strategic Management Journal, 6(1), 55-73.

Hodgkinson, G. P., & Johnson, G. (1994). Exploring the mental models of competitive strategists: The case for a processual approach. Journal of Management Studies, 31(4), 525-552.

Hodgkinson, G. P., Tomes, A. E., & Padmore, J. (1996). Using consumers’ perceptions for the cognitive analysis of corporate-level competitive structures. Journal of Strategic Marketing, 4(1), 1-22.

Hovland, C. I., Harvey, O. J., & Sherif, M. (1958). Assimilation and contrast effects of anchoring stimuli on judgments. Journal of Experimental Psychology, 55(2), 150-155.

Huber, J., & Klein, N. M. (1991). Adapting cutoffs to the choice environment: The effects of attribute correlation and reliability. Journal of Consumer Research, 18(3), 346-357.

Jain, A. K., & Dubes, R. C. (1988). Algorithms for clustering data. Englewood Cliffs.

Jerath, K., Ma, L., & Park, Y.-H. (2014). Consumer click behavior at a search engine: The role of keyword popularity. Journal of Marketing Research, 51(4), 480-486.

Jerath, K., Ma, L., Park, Y.-H., & Srinivasan, K. (2011). A “position paradox” in sponsored

search auctions. Marketing Science, 30(4), 612- 627.

Jeziorski, P., & Segal, I. (2015). What makes them click: Empirical analysis of consumer demand for search advertising. American Economic Journal: Microeconomics, 7(3), 24-53.

Kahn, B. E. (1995). Consumer variety-seeking among goods and services: An integrative review. Journal of Retailing and Consumer Services, 2(3), 139-148.

Kotler, P., & Armstrong, G. (1989). Principles of marketing (4th ed.). Prentice-Hall.

Leask, G., & Parker, D. (2007). Strategic groups, competitive groups and performance within the U.K. pharmaceutical industry: Improving our understanding of the competitive process. Strategic Management Journal, 28(7), 723- 745.

Lu, X., & Zhao, X. (2014). Differential effects of keyword selection in search engine advertising on direct and indirect sales. Journal of Management Information Systems, 30(4), 299- 326.

Luo, X., Andrews, M., Fang, Z., & Phang, C. W. (2013). Mobile targeting. Management Science, 60(7), 1738-1756.

Ma, Z., Pant, G., & Sheng, O. R. L. (2011). Mining competitor relationships from online news: A network-based approach. Electronic Commerce Research and Applications, 10(4), 418-427.

Mas‐Ruiz, F., & Ruiz‐Moreno, F. (2011). Rivalry within strategic groups and consequences for performance: The firm-size effects. Strategic Management Journal, 32(12), 1286-1308.

Mas‐Ruiz, F., & Ruiz‐Moreno, F. (2017). How strategic groups act competitively within and across markets. Managerial and Decision Economics, 38(7), 1017-1032.

Mas‐Ruiz, F., Ruiz‐Moreno, F., & Martínez, A. L. de G. (2014). Asymmetric rivalry within and between strategic groups. Strategic Management Journal, 35(3), 419-439.

McAlister, L., & Pessemier, E. (1982). Variety seeking behavior: An interdisciplinary review. Journal of Consumer Research, 9(3), 311-322.

Medin, D. L., Goldstone, R. L., & Markman, A. B. (1995). Comparison and choice: Relations between similarity processes and decision processes. Psychonomic Bulletin & Review, 2(1), 1-19.

Murry, C., & Zhou, Y. (2019). Consumer search and automobile dealer colocation. Management Science, 66(5), 1909-1934.

Nath, D., & Gruca, T. S. (1997). Convergence across alternative methods for forming strategic groups. Strategic Management Journal, 18(9), 745-760.

Nedungadi, P. (1990). Recall and consumer consideration sets: Influencing choice without altering brand evaluations. Journal of Consumer Research, 17(3), 263-76.

Pant, G., & Sheng, O. R. L. (2015). Web footprints of firms: Using online isomorphism for competitor identification. Information Systems Research, 26(1), 188-209.

Peteraf, M. A. (1993). Intra-industry structure and the response toward rivals. Managerial and Decision Economics, 14(6), 519-528.

Porac, J. F., Thomas, H., Wilson, F., Paton, D., & Kanfer, A. (1995). Rivalry and the industry model of Scottish knitwear producers. Administrative Science Quarterly, 40(2), 203- 227.

Porter, M. E. (1979). The structure within industries and companies’ performance. The Review of Economics and Statistics, 61(2), 214-227.

Ringel, D. M., & Skiera, B. (2016). Visualizing asymmetric competition among more than 1,000 products using big search data. Marketing Science, 35(3), 511-534.

Rosenbaum, P. R., & Rubin, D. B. (1983). The central role of the propensity score in observational studies for causal effects. Biometrika, 70(1), 41-55.

Rutz, O. J., & Trusov, M. (2011). Zooming in on paid search ads: A consumer-level model calibrated on aggregated data. Marketing Science, 30(5), 789-800.

Rutz, O. J., Trusov, M., & Bucklin, R. E. (2011). Modeling indirect effects of paid search advertising: Which keywords lead to more future visits? Marketing Science, 30(4), 646- 665.

Short, J. C., Ketchen, D. J., Palmer, T. B., & Hult, G. T. M. (2007). Firm, strategic group, and industry influences on performance. Strategic Management Journal, 28(2), 147-167.

Simonov, A., Nosko, C., & Rao, J. M. (2018). Competition and crowd-out for brand keywords in sponsored search. Marketing Science.

Smith, K. G., Grimm, C. M., Young, G., & Wally, S. (1997). Strategic groups and rivalrous firm behavior: Towards a reconciliation. Strategic Management Journal, 18(2), 149-157.

Thomas, H., & Venkatraman, N. (1988). Research on strategic groups: Progress and prognosis. Journal of Management Studies, 25(6), 537- 555.

Varian, H. R. (2007). Position auctions. International Journal of Industrial Organization, 25(6), 1163-1178.

Weber, T. A., & Zheng, Z. (Eric). (2007). A model of search intermediaries and paid referrals. Information Systems Research, 18(4), 414-436.

Witten, I. H., Frank, E., & Hall, M. A. (2011). Data mining practical machine learning tools and techniques (3rd ed.). Morgan Kaufmann.

Zhang, X. (Michael), & Feng, J. (2011). Cyclical bid adjustments in search-engine advertising. Management Science, 57(9), 1703-1719.

Zheng, Z., Padmanabhan, B., & Kimbrough, S. O. (2003). On the existence and significance of data preprocessing biases in web-usage mining. INFORMS Journal on Computing, 15(2), 148-170.

## Appendix A: The Differential Impact of Within-Group Competitors When They Are Located Above or Below a Focal Firm

Users generally inspect search results sequentially from top to bottom (Granka et al., 2004). Therefore, a within-group competitor may have a stronger impact on the CTR of a focal firm if the within-group competitor appears above the focal firm instead of below it. To further understand the influence of within-group competitors’ ads, we investigate how the influence differs when a within-group competitor appears above or below the focal firm.

$$
\operatorname{Logit} \left(\text { Visit } _ {\mathrm{ijt}}\right) = \beta_ {0} + \beta_ {1} \text { Appear } _ {\mathrm{it}} + \beta_ {2} \text { WCAbove } _ {\mathrm{it}} + \beta_ {3} \text { WCBelow } _ {\mathrm{it}} + \lambda_ {\mathrm{j}} + \delta_ {\mathrm{t}} + \varepsilon_ {\mathrm{ijt}}\tag{5}
$$

In Model 5, WCAbove and WCBelow indicate if a within-group competitor appears above or below a focal firm (both may occur simultaneously within a search result). Table A1 presents the results. In all estimations, the appearance of a within-group competitor above a focal firm (WCAbove) has a negative and significant impact on the CTR of the focal firm across all model estimations. On the other hand, the estimated coefficient for WCBelow is either significantly negative (Columns 1 and 2) or insignificant (Columns 3 and 4). According to the estimations in Columns 3 and 4, a within-group competitor appearing below a focal firm does not have any significant impact on the CTR of a focal firm’s ad. Even when the estimated β<sub>3</sub> is significantly negative (as shown in Columns 1 and 2, its magnitude is not greater than that of β<sub>2</sub> (the p-value for testing the null of $\beta _ { 2 } - \beta _ { 3 } = 0$ is smaller than 0.01). Taken together, the appearance of a withingroup competitor below a focal firm does not have a strong negative impact; however, the appearance above does. These findings are consistent with consumers’ sequential investigation patterns (Granka et al., 2004).

Table A1. Competition Effect Results for Above or Below a Focal Firm

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Apear_{it}$ </td><td>1.427***(0.066)</td><td>1.575***(0.071)</td><td>0.908***(0.071)</td><td>1.034***(0.076)</td></tr><tr><td> $WCAbove_{it}$ </td><td>-0.791***(0.069)</td><td>-0.885***(0.073)</td><td>-0.493***(0.074)</td><td>-0.559***(0.080)</td></tr><tr><td> $WCBelow_{it}$ </td><td>-0.323***(0.067)</td><td>-0.373***(0.072)</td><td>0.046(0.074)</td><td>0.051(0.080)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>32,474</td><td>32,474</td><td>32,474</td><td>32,474</td></tr><tr><td> $Pseudo R^2$ </td><td>0.033</td><td>0.097</td><td>0.090</td><td>0.164</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

## Appendix B: Robustness Analyses by Controlling for Google Trends

A user’s interest in a brand may change over time, thereby influencing the likelihood of search and purchase decisions dynamically (Du et al., 2015; Du & Kamakura, 2012). A commonly used data source of users’ interest is Google Trends (www.google.com/trends), which tracks Google users’ search interests (volume) over time (Choi & Varian, 2012).

We leverage search trends extracted from Google Trends to control for dynamic consumer interests. We gathered Google Trends data for each of the 26 firms that we investigate. Figure B1 presents four search trends among United States consumers between May 1, 2009, and September 30, 2009. The trend lines illustrate that consumer online searches for brand-related keywords can vary substantially over time and follow very different patterns.

Model 1 in the main text captures the influence of a focal firm on consumers’ visiting patterns. To control for consumers’ changing interests, we used Model 6 where we added an additional control Trends to account for the search trends index for a focal firm. As expected, the regression results presented in Table B1 show that Trends for a focal firm is positively correlated with the CTRs for that firm. Importantly, the estimated coefficients for the appearance effect are very close to the estimates obtained in Table 3.

![](/api/attachments/Y7G7VYN9/fulltext/images/d476bbcc6360e62a86a09da9b9eb94fa459bd4027a930c626e44810bf92d262b.jpg)  
Figure B1. Google Trends Data for Four Camera Manufacturers.

$$
\operatorname{Logit} \left(\text { Visit } _ {\mathrm{ijt}}\right) = \beta_ {0} + \beta_ {1} \text { Appear } _ {\mathrm{it}} + \beta_ {2} \text { Trends } _ {\mathrm{it}} + \lambda_ {\mathrm{j}} + \delta_ {\mathrm{t}} + \varepsilon_ {\mathrm{ijt}}\tag{6}
$$

Similarly, we added controls for the focal firm’s trends in Models 2 and 3 (from the main body of the paper) to form Models 7 and 8. In addition, we explicitly controlled for the impact of competitors’ trends in both models, wherein WCTrends denotes the mean of trends indices for all other within-group competitors.

$$
\operatorname{Logit} \left(\text { Visit } _ {\mathrm{ijt}}\right) = \beta_ {0} + \beta_ {1} \text { Appear } _ {\mathrm{it}} + \beta_ {2} \text { WCAppear } _ {\mathrm{it}} + \beta_ {3} \text { Trends } _ {\mathrm{it}} + \beta_ {4} \text { WCTrends } _ {\mathrm{it}} + \lambda_ {\mathrm{j}} + \delta_ {\mathrm{t}} + \varepsilon_ {\mathrm{ijt}}\tag{7}
$$

$$
\operatorname{Logit} \left(\text { Visit } _ {\mathrm{ijt}}\right) = \beta_ {0} + \beta_ {1} \text { RankDiff } _ {\mathrm{it}} + \beta_ {2} \text { Trends } _ {\mathrm{it}} + \beta_ {3} \text { WCTrends } _ {\mathrm{it}} + \lambda_ {\mathrm{j}} + \delta_ {\mathrm{t}} + \varepsilon_ {\mathrm{ijt}}\tag{8}
$$

Tables B2 and B3 present the results for the competition effect estimation for Models 7 and 8, respectively. We found the estimates for the competition effect (WCAppear) in Table B2 to be consistent with those in Table 4 in the main text. Similarly, the estimated coefficient for the co-location effect (RankDiff) in Table B3 is qualitatively the same as that in Table 5.

To control for the firm trends in Model 4, we added an additional control TrendDiff for the difference in trends between a firm pair p in a particular session t in Model 9. The estimates for the variable Within are aligned with the results presented in Table 6. These results show that our estimations are robust to controlling for the shifting interest of consumers toward different firms.

$$
\text { RankDiff } _ {\text { pjt }} = \beta_ {0} + \beta_ {1} \text { Within } _ {\text { pt }} + + \beta_ {2} \text { TrendDiff } _ {\text { pt }} + \lambda_ {j} + \delta_ {t} + \varepsilon_ {\text { ijt }}\tag{9}
$$

Table B1. Appearance Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $\text{Appear}_{it}$ </td><td>0.924***(0.047)</td><td>1.005***(0.049)</td><td>0.704***(0.049)</td><td>0.805***(0.052)</td></tr><tr><td> $\text{Trends}_{it}$ </td><td>0.008***(0.002)</td><td>0.009***(0.002)</td><td>0.027***(0.002)</td><td>0.030***(0.002)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>32,474</td><td>32,474</td><td>32,474</td><td>32,474</td></tr><tr><td> $Pseudo R^2$ </td><td>0.025</td><td>0.088</td><td>0.095</td><td>0.171</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Table B2. Competition Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Apear_{it}$ </td><td>0.719***(0.049)</td><td>0.765***(0.052)</td><td>0.661***(0.051)</td><td>0.757***(0.055)</td></tr><tr><td> $WCAppear_{it}$ </td><td>-0.759***(0.064)</td><td>-0.886***(0.071)</td><td>-0.194***(0.070)</td><td>-0.201**(0.079)</td></tr><tr><td> $Trends_{it}$ </td><td>0.021***(0.002)</td><td>0.023***(0.002)</td><td>0.019***(0.003)</td><td>0.016***(0.003)</td></tr><tr><td> $WCTrends_{it}$ </td><td>-0.051***(0.004)</td><td>-0.056***(0.004)</td><td>-0.084***(0.012)</td><td>-0.114***(0.015)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>32,474</td><td>32,474</td><td>32,474</td><td>32,474</td></tr><tr><td> $Pseudo R^2$ </td><td>0.043</td><td>0.109</td><td>0.099</td><td>0.176</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Table B3. Co-Location Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $RankDiff_{it}$ </td><td>-0.109***(0.021)</td><td>-0.128***(0.026)</td><td>-0.126***(0.022)</td><td>-0.186***(0.028)</td></tr><tr><td> $Trendst_{it}$ </td><td>0.009*(0.005)</td><td>0.013**(0.006)</td><td>0.015*(0.008)</td><td>0.015(0.010)</td></tr><tr><td> $WCTrendst_{it}$ </td><td>-0.026***(0.008)</td><td>-0.023**(0.010)</td><td>-0.058*(0.030)</td><td>-0.057(0.041)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>8,297</td><td>8,297</td><td>8,297</td><td>8,297</td></tr><tr><td> $Pseudo R^2$ </td><td>0.009</td><td>0.074</td><td>0.072</td><td>0.165</td></tr><tr><td colspan="5">Note: ***p&lt; 0.01, **p&lt; 0.05, *p&lt; 0.1. Standard errors in parentheses.</td></tr></table>

Table B4. Impact of Within-Group Membership on Rank Difference in Search Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Within_{pt}$ </td><td>-1.045***(0.030)</td><td>-1.059***(0.030)</td><td>-0.942***(0.131)</td><td>-1.432***(0.141)</td></tr><tr><td> $TrendDiff_{pt}$ </td><td>0.025***(0.001)</td><td>0.028***(0.001)</td><td>0.029***(0.001)</td><td>0.032***(0.001)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>35,580</td><td>35,580</td><td>35,580</td><td>35,580</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.050</td><td>0.042</td><td>0.054</td><td>0.046</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

## Appendix C: Robustness Analyses by Considering Organic Search Results

We conducted additional analysis to examine whether the presence of organic search results might confound our findings. To rule out such explanations, we considered the firms (and their strategic group competitors) that appear in either the organic search results or the sponsored search results (or both) when examining the possibility of a consumer visiting a focal firm.

The new set of results for Models 1-4 when considering both organic and sponsored search results are shown in Tables C1-C4. As we can see from these tables, the results are qualitatively identical to those of Tables 3-6 in the main analyses. This illustrates that our results are robust whether or not the organic search results are factored in.

Table C1. Appearance Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Appear_{it}$ </td><td>0.929***(0.047)</td><td>1.007***(0.049)</td><td>0.859***(0.048)</td><td>0.977***(0.051)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>32,474</td><td>32,474</td><td>32,474</td><td>32,474</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.027</td><td>0.090</td><td>0.094</td><td>0.170</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Table C2. Competition Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Appear_{it}$ </td><td>0.888***(0.047)</td><td>0.957***(0.049)</td><td>0.821***(0.049)</td><td>0.935***(0.053)</td></tr><tr><td> $WCApea_{rit}$ </td><td>-0.909***(0.065)</td><td>-1.023***(0.072)</td><td>-0.272***(0.078)</td><td>-0.294***(0.087)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>32,474</td><td>32,474</td><td>32,474</td><td>32,474</td></tr><tr><td> $Pseudo R^2$ </td><td>0.037</td><td>0.102</td><td>0.095</td><td>0.171</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Table C3. Co-Location Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $RankDiff_{it}$ </td><td>-0.119***(0.018)</td><td>-0.151***(0.021)</td><td>-0.112***(0.019)</td><td>-0.144***(0.022)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>11,304</td><td>11,304</td><td>11,304</td><td>11,304</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.007</td><td>0.072</td><td>0.058</td><td>0.138</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Table C4. Impact of Within-Group Membership on Rank Difference

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Within_{pt}$ </td><td>-0.943***(0.027)</td><td>-0.942***(0.027)</td><td>-1.486***(0.052)</td><td>-1.035***(0.132)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>40,529</td><td>40,529</td><td>40,529</td><td>40,529</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.030</td><td>0.019</td><td>0.038</td><td>0.029</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

## Appendix D: Robustness Analyses by Considering the Rank of Advertisements

It would be amiss if we ignored the impact on CTR of the ranks of the advertisers when examining H1a and H2a. Therefore, we replicated the analyses in the paper by controlling for the ranks of the advertisers. The results are largely consistent with those reported in the main text. Similar to Model 1 in the paper, we replaced the indicator variable $A p p e a r _ { i t }$ with the rank variable $R a n k _ { i t }$ to examine the effect of the rank of the focal firm in Model 10. The results are shown in Table D1.

$$
\operatorname{Logit} \left(\text { Visit } _ {\mathrm{ijt}}\right) = \beta_ {0} + \beta_ {1} \operatorname{Rank} _ {\mathrm{it}} + \lambda_ {\mathrm{j}} + \delta_ {\mathrm{t}} + \varepsilon_ {\mathrm{ijt}}\tag{10}
$$

Table D1. Appearance (Rank) Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Rank_{it}$ </td><td>-0.062***(0.011)</td><td>-0.071***(0.012)</td><td>-0.070***(0.014)</td><td>-0.134***(0.018)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>9,939</td><td>9,939</td><td>9,939</td><td>9,939</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.005</td><td>0.070</td><td>0.097</td><td>0.218</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

In all four of the model variants shown in the table, the estimated coefficients for Rank are negative and significant. This means that focal firms are visited more frequently when they are ranked higher in the sponsored search results (i.e., with a smaller value for the Rank variable). This is consistent with the general expectation that ads displayed higher tend to be clicked more frequently. This finding provides a more nuanced observation of the appearance effect.

Similarly, in Model 11 (that examines the competition effect), we replaced the appearance indicator of a focal firm with its corresponding rank variable $R a n k _ { i t }$ as follows:

$$
\operatorname{Logit} \left(\text { Visit } _ {\mathrm{ijt}}\right) = \beta_ {0} + \beta_ {1} \operatorname{Rank} _ {\mathrm{it}} + \beta_ {2} \operatorname{WCAappear} _ {\mathrm{it}} + \lambda_ {\mathrm{j}} + \delta_ {\mathrm{t}} + \varepsilon_ {\mathrm{ijt}}\tag{11}
$$

The regression results are displayed in Table D2. The results show that, in general, the appearance of a within-group competitor $( { \mathrm { W C A p p e a r } } = 1 )$ has a negative impact on the probability of a consumer visiting a focal firm. However, the impact is statistically significant at 1% level in the first two model variants, significant at 10% level in the third variant, and not significant in the fourth variant.

Table D2. Competition Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Rank_{it}$ </td><td>-0.061***(0.011)</td><td>-0.073***(0.012)</td><td>-0.073***(0.014)</td><td>-0.134***(0.018)</td></tr><tr><td> $WCApear_{it}$ </td><td>-0.833***(0.075)</td><td>-1.193***(0.093)</td><td>-0.173*(0.101)</td><td>-0.116(0.150)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>9,939</td><td>9,939</td><td>9,939</td><td>9,939</td></tr><tr><td> $Pseudo R^2$ </td><td>0.022</td><td>0.100</td><td>0.097</td><td>0.218</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Because the results across the variants are not perfectly consistent, we further investigated the differential impact of within-group competitors that appear above or below a focal firm (analogous to Model 5 in Appendix A). In Model 12, $W C A b o \nu e _ { i t }$ and $W C B e l o w _ { i t }$ indicate whether a within-group competitor appears above or below a focal firm, respectively.

$$
\operatorname{Logit} \left(\text { Visit } _ {\mathrm{ijt}}\right) = \beta_ {0} + \beta_ {1} \text { Rank } _ {\mathrm{it}} + \beta_ {2} \text { WCAbove } _ {\mathrm{it}} + \beta_ {3} \text { WCBelow } _ {\mathrm{it}} + \lambda_ {\mathrm{j}} + \delta_ {\mathrm{t}} + \varepsilon_ {\mathrm{ijt}}\tag{12}
$$

The results are shown in Table D3. The appearance of a within-group competitor above a focal firm (WCAbove = 1) has a negative and significant impact on the CTR of the focal firm across all variants of this model. On the other hand, the estimated coefficient on WCBelow is significantly negative in Variants 1 and 2, and insignificant in Variants 3 and 4. The results indicate that the appearance of a within-group competitor below a focal firm may not have a strong negative impact while the appearance above exerts a significantly negative impact. The results indicate that if a within-group competitor is able to secure a higher rank than the focal firm, it hurts the focal firm’s CTR considerably. These results are qualitatively the same as the ones presented in Table A1 and lend support to the competition effect stated in H1a.

Table D3. Competition Effect Results for Above or Below a Focal Firm

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $Rank_{it}$ </td><td>-0.050***(0.012)</td><td>-0.062***(0.013)</td><td>-0.039**(0.017)</td><td>-0.107***(0.024)</td></tr><tr><td> $WCAbove_{it}$ </td><td>-0.695***(0.073)</td><td>-0.893***(0.081)</td><td>-0.367***(0.086)</td><td>-0.363***(0.106)</td></tr><tr><td> $WCBelow_{it}$ </td><td>-0.432***(0.072)</td><td>-0.591***(0.083)</td><td>0.014(0.095)</td><td>-0.113(0.120)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>9,939</td><td>9,939</td><td>9,939</td><td>9,939</td></tr><tr><td> $Pseudo R^2$ </td><td>0.025</td><td>0.101</td><td>0.100</td><td>0.220</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Next, we re-examined the co-location effect (H2a) by adding a control for the rank of the highest within-group competitor (WCRank) in Model 13 (similar to Model 3 in the paper):

$$
\operatorname{Logit} \left(\text { Visit } _ {\mathrm{ijt}}\right) = \beta_ {0} + \beta_ {1} \text { RankDiff } _ {\mathrm{it}} + \beta_ {2} \text { WCRank } _ {\mathrm{it}} + \lambda_ {\mathrm{j}} + \delta_ {\mathrm{t}} + \varepsilon_ {\mathrm{ijt}}.\tag{13}
$$

The results, presented in Table D4, show that the co-location effect is robust to this additional control of within-group competitors’ ranks: the smaller the rank difference (i.e., the closer a focal firm is to its within-group competitor), the larger the CTR for the focal firm (thus H2a is supported).

We also conducted rank-controlled experiments using the additional dataset for multi-keyword bidding (see Section 6 for relevant discussions). The results are summarized in Table D5. In the “appearance” column, the estimated coefficient for Rank is negative and statistically significant. It indicates that a higher position of the focal firm is associated with a higher CTR. In the “competition” column, the estimated coefficient for WCAppear is negative and significant. This offers support for H1a: the appearance of other within-group competitors hurts the CTR of the focal firm after controlling for its rank. In the “co-location” column, RankDiff is negative and significant. This indicates that the focal firm’s CTR is boosted by staying closer to its within-group competitors (H2a is supported). Taken together, the estimated coefficients in Table D5 continue to lend support to H1a and H2a.

Table D4. Co-Location Effect Results

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $RankDiff_{it}$ </td><td>-0.118***(0.021)</td><td>-0.134***(0.026)</td><td>-0.132***(0.022)</td><td>-0.188***(0.028)</td></tr><tr><td> $WCRank_{it}$ </td><td>-0.045***(0.014)</td><td>-0.048***(0.016)</td><td>0.065***(0.023)</td><td>0.088***(0.032)</td></tr><tr><td>Group  $FE \lambda_j$ </td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>Session  $FE \delta_t$ </td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>8,297</td><td>8,297</td><td>8,297</td><td>8,297</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.008</td><td>0.075</td><td>0.071</td><td>0.165</td></tr><tr><td colspan="5">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

Table D5. Summary of Results for Multi-Keyword Bidding Data

<table><tr><td>Variable</td><td>Appearance</td><td>Competition</td><td>Co-Location</td></tr><tr><td> $Rank_{it}$ </td><td>-0.185***(0.035)</td><td>-0.178***(0.034)</td><td></td></tr><tr><td> $WCApear_{it}$ </td><td></td><td>-0.655***(0.129)</td><td></td></tr><tr><td> $RankDiff_{it}$ </td><td></td><td></td><td>-0.097***(0.029)</td></tr><tr><td> $WCRank_{it}$ </td><td></td><td></td><td>-0.013(0.041)</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>Keyword FE</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Number of obs (N)</td><td>506</td><td>506</td><td>506</td></tr><tr><td>R2</td><td>0.055</td><td>0.103</td><td>0.024</td></tr><tr><td colspan="4">Note: ***p&lt;0.01, **p&lt;0.05, *p&lt;0.1. Standard errors in parentheses.</td></tr></table>

In sum, our findings are robust to adding the additional control for the ranks of the advertisers for both the “digital camera” and the multi-keyword bidding datasets.

## About the Authors

Cheng Nie is an assistant professor of information systems and business analytics at the Ivy College of Business at Iowa State University. He received his Ph.D. from the Jindal School of Management, University of Texas at Dallas. His current research interests are in sponsored search, sharing economy, and user-generated content.

Zhiqiang (Eric) Zheng is the Ashbel Smith Professor in Information Systems at the Jindal School of Management, University of Texas at Dallas. He received his Ph.D. from the Wharton School of Business. His current research interests focus on fintech, blockchain, and healthcare analytics. He currently serves as a senior editor for Information Systems Research.

Sumit Sarkar is the Charles and Nancy Davidson Chair and Professor of Information Systems in the Naveen Jindal School of Management at the University of Texas at Dallas. He received his Ph.D. from the Simon School of Business at the University of Rochester, his MBA from IIM Calcutta, and his B. Tech from IIT Delhi. His current research interests are in crowdsourcing, machine learning, personalization and recommendation technologies, sponsored search, data privacy, and information quality. He is a Distinguished Fellow of the Information Systems Society at INFORMS.
