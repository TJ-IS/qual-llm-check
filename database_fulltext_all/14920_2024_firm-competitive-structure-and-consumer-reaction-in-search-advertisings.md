---
otero_id: 14920
otero_key: "RDRW8MV9"
title: "Firm Competitive Structure and Consumer Reaction in Search Advertisings"
authors: "Cheng Nie; Zhiqiang (Eric) Zheng; Sumit Sarkar"
year: "2024"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00835"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2024

# Firm Competitive Structure and Consumer Reaction in Search Advertisings

Cheng Nie , cheng@chengnie.com

Zhiqiang (Eric) Zheng

, ericz@utdallas.edu

Sumit Sarkar

, sumit@utdallas.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Firm Competitive Structure and Consumer Reaction in Search Advertisings

Cheng Nie,<sup>1</sup> Zhiqiang (Eric) Zheng,<sup>2</sup> Sumit Sarkar<sup>3</sup>

<sup>1</sup>Iowa State University, USA, cheng@chengnie.com <sup>2</sup>University of Texas at Dallas, USA, ericz@utdallas.edu <sup>3</sup>University of Texas at Dallas, USA, sumit@utdallas.edu

## Abstract

Sponsored search advertising has become an important venue for firms competing for consumers. As a result, many keywords attract a large number of bidders, and the competing advertisers may be quite heterogeneous. We examine whether this heterogeneity impacts how consumers perceive and react to such competitions. To this end, we draw on the theory of strategic groups to prescribe the structure of the competitive environment and investigate how strategic groups impact consumers’ clicking and website-visit behavior when viewing sponsored search results. Our unique datasets that combine search results from Google and consumers’ clickstream data enable us to disentangle such an impact. We find strong positive externality for within-group competitors relative to across-group competitors: (1) consumers are more likely to co-visit two firms that belong to the same strategic group, as opposed to two firms from different groups when both firms appear in the search results; (2) the presence of a firm in the search results primes consumers to visit other firms from the same strategic group even when the other firms do not appear in the search results. Our findings contribute to the sponsored search and strategic group literature by theorizing and empirically verifying consumers’ website-visit behaviors from the strategic group perspective.

Keywords: Strategic Group, Sponsored Search, Priming, Competitor Heterogeneity, Search Goods

Jason Bennett Thatcher was the accepting senior editor. This research article was submitted on Feb 21, 2022 and underwent three revisions.

## 1 Introduction

The sponsored search market has become a prominent advertising format over the last couple of decades, generating total revenues of over \$84.4 billion in 2021 (IAB Report, 2023). By allowing advertisers to bid on search terms entered by users in a search engine, this advertising format enables firms to target users based on their search intent (as reflected by their search terms). Because of the prevalence of this format, most firms consider this an important part of their advertising strategy. As a result, the number of firms bidding on search keywords can be quite substantial, with many of them being displayed in the same search results. This has important implications for advertisers, who need to make a number of key decisions, ranging from which keywords to bid on, how much to bid, daily or weekly budgets, etc. (Amaldoss et al., 2016; Du et al., 2017; S. Lu & Yang, 2017; Simonov & Hill, 2021; Yuan et al., 2017). These decisions hinge on who the firm’s competitors are and how consumers respond to the firm’s advertisements and those of its main competitors when searching.

Given the important business implications of this market, there has been a considerable amount of research devoted to this phenomenon. Early research, mostly analytical in nature, focused on designing auction mechanisms (Edelman et al., 2007; Feng et al., 2007; Lahaie & Pennock, 2007; Liu et al., 2010; Weber & Zheng, 2007) and examining advertisers’ bidding strategies (Edelman & Ostrovsky, 2007; Varian, 2007). These studies modeled the net click-through rate (CTR) of an advertisement as a function of its position and quality, while ignoring the nature of the competitors.

Researchers have subsequently examined the effect of competition empirically along a few dimensions. A common theme across most of these works is to study the CTR for an advertisement in a given position, based on advertisements that are shown either above or below it (e.g., Animesh et al., 2011; Jerath et al., 2011; Jeziorski & Segal, 2015; Lu & Yang, 2017). Agarwal et al. (2015) examined how competition coming from organic search results affects the CTR of advertisers appearing in sponsored search results. Simonov and Hill (2021) investigated the effects of competitors bidding on trademarked keywords belonging to a focal firm, which is also known as competitive poaching. Bhattacharya et al. (2022) identified some factors that enable successful competitive poaching.

An interesting phenomenon is that for keywords with a large number of bidders, the competing advertisers could be quite heterogeneous. This is, due, in part, to the “broad match” tools offered to advertisers (Amaldoss et al., 2016), where search engines not only match the exact keywords specified by the advertiser but also variations of the keywords that are contextually similar to the search keyword. In the air travel context, some advertisers may be online travel agents like Expedia.com or Priceline.com, whereas others may be carriers like Southwest or United Airlines. In order to develop their advertising strategies, firms need to understand how consumers navigate through advertisements of diverse sets of firms when inspecting the search results. This competitor heterogeneity motivates us to examine how consumers react to the complex competitive environment in sponsored search. Despite its importance in today’s business, the search advertising literature has yet to fully understand how consumers perceive and react to competitions among heterogeneous advertisers.

To this end, we draw upon a recent characterization of the heterogeneity across competitors in search advertising markets proposed by Nie et al. (2021). Their characterization is based on the theory of strategic groups, which was originally proposed in the management literature (Caves & Porter, 1977; Porter, 1979). Porter (1979) defined a strategic group as a set of firms that closely compete against each other within an industry, where firms that fall into the same group are similar to one another along certain structural dimensions (e.g., degree of vertical integration). The notion of the strategic group is considered one of the central constructs in the strategic management literature to diagnose the competitive structure in a market (Mas‐Ruiz et al., 2014; Short et al., 2007; Surroca et al., 2016). The strategic group characterization of competitors provides an interesting, and heretofore underexplored way of understanding consumers’ navigation behaviors.

We studied how an advertiser’s membership in strategic groups impacts consumers’ navigation (click) behaviors after viewing search results. We examined this empirically in two markets: the air travel market and the digital camera market. These two contexts offered us several empirical benefits. The advertisers in these markets came from a diverse set of firms. For example, for the air travel market, advertisers included fullservice airlines (carriers) like Delta and United, low-cost carriers like Southwest and Spirit, and online travel agents. For the digital camera market, advertisers included manufacturers and retailers. Further, they are highly competitive markets with participants advertising aggressively to attract customers. Both industries have been extensively studied by researchers in information systems, economics, and marketing (Chellappa et al., 2011; Clemons et al., 2002; Granados et al., 2012; Lu & Zhao, 2014; Nie et al., 2021).

This study aims to enrich the literature on sponsored search advertising and the strategic group theory by investigating the co-appearance effect of firms from the same group and the priming effect of within-group firms’ advertisements on consumers’ click behavior. Specifically, we examined the following research questions. First, we investigated whether the coappearance of firms from the same strategic group in the search results impacts the behavior of consumers to covisit multiple advertisers’ websites differently, compared to the co-appearance of competing advertisers from different strategic groups. Next, we studied whether the appearance of firms from a strategic group impacts a consumer’s propensity to visit the websites of other firms in that group, even when the other firms do not appear in the search result (in other words, whether the appearance of firms from a group primes the consumer to consider other firms from that group that are not displayed).

Our questions have potentially important implications for both search engines and advertisers. Because consumers typically visit multiple advertisers’ websites during a search session, the strategic group characterization of competing advertisers enabled us to examine if the co-appearance of a pair of firms from the same strategic group impacts consumers’ propensities to co-visit their websites. If this is indeed the case, it would inform search engines on which advertisers should be displayed to maximize CTR because search engines widely utilize the pay-per-click business model. Knowing whether the appearance of some members of a strategic group primes consumers to visit the websites of other members of the group who have not appeared in the search results has immediate implications for advertisers. Recognizing that consumers could visit a focal firm after seeing its within-group competitors’ ads, the focal firm could spend its advertising budget more strategically, e.g., by avoiding costly head-to-head competition when bidding for an advertising slot in a sponsored search. These questions have not been answered in practice or in the extant literature on either sponsored search or strategic groups.

To conduct our study, we obtained search results data and clickstream data for two markets, corresponding to the search terms “air travel” and “digital camera.” The search results data are from Google between May and October 2009. We further acquired clickstream data from Comscore for the air travel market and another third-party data provider for the digital camera market for the same period. By tracking which competing firms’ websites consumers chose to visit during a session, we can infer whether the consumers’ mental models regarding strategic groups for that market impacted their search sessions.<sup>1</sup>

We found strong evidence for the influence of strategic groups on consumer behavior in both markets. We found that the probability of a consumer co-visiting a pair of firms was significantly higher when both firms were from the same strategic group. Further, the group membership appears to be imprinted in users’ minds: when only some members of a strategic group showed up in the search results, the user was more likely to visit other (not displayed) members from the same group than not-displayed members from other groups (leading to a spillover effect for firms within the strategic group). These findings inform how search engines and advertisers should act differently in the presence of competing advertisers. Search engines should factor in the competitive structure of the search market when projecting the click-through rates for ads: the CTR of a pair of firms from the same strategic group would be higher than that of a pair of firms from different groups. Advertisers should reevaluate their bidding strategies and budget allocations when the spillover effect from other within-group advertisers is present.

The rest of the paper is organized as follows. In Section 2, we provide an overview of related work. Section 3 details the theory development and research hypotheses. In Section 4, we discuss the data used for the analyses. The empirical analyses and results are discussed in Section 5. In Section 6, we discuss additional experiments to rule out plausible alternative explanations for our findings. Section 7 discusses the implications of our work.

## 2 Related Work

Given the rapid growth of the sponsored search industry, it has attracted substantial interest in the economics, marketing, and information systems literatures. Auction and ranking mechanisms received much attention in early works in this area, with an examination of the payoffs to advertisers and search engine platforms under different mechanism designs (Amaldoss et al., 2015; Kelly et al., 2016; Sayedi et al., 2018). Subsequent studies have investigated budget allocations for different (multi-keyword) search markets (Yang et al., 2015) and multiple search platforms (Zia & Rao, 2019), as well as how budget constraints influence advertisers’ optimal bidding strategies (Asadpour et al., 2019; Balseiro & Gur, 2019). These studies implicitly assume that, while the CTR of an advertisement depends on its quality and its position, it does not depend on the competing advertisements appearing in other positions of the same search results.

Increasingly, researchers have started to recognize the externality effect imposed by other competing firms on the CTR of a focal firm’s advertisement. Early works that considered competitors focused only on the quality and price dimensions in a generic manner. They also restricted the competitors to a very small set. For instance, Jerath et al. (2011) modeled two advertisers in their analysis, while Animesh et al. (2011) based much of their findings on a “window-ofthree” approach where only the two advertisers that appear immediately above and below a focal advertisement were considered to be competitors. In a related vein, Jeziorski and Segal (2015) observed that the CTR on a given advertisement in a given position depends on which advertisements are shown above or below it, suggesting that the focal advertiser needs to know which advertisers it is competing with. Agarwal et al. (2015) showed that organic search results negatively affect the CTR of competing advertisers who appear in sponsored search results. Simonov and Hill (2021) examined the effect on focal firms when competitors bid on the focal firm’s brand in sponsored search (i.e., competitive poaching), showing that competitors can steal a significant portion of clickstream traffic. They suggest that the focal firm should bid on its own brand to limit the extent of clicks stolen by competitors. Bhattacharya et al. (2022) showed that the effectiveness of such competitive poaching largely depends on the quality of the brand being poached and the type of message featured in the poaching ad copy.

While the above works have provided additional insights regarding the externality effects of competitors on a firm’s advertising strategy, they have not attempted to characterize the competitive environment in a manner that can account for the heterogeneity of sponsored search listings. There are two works that have examined competitors using more formal market characterizations. Lu and Yang (2017) characterized competing advertisers along two dimensions, one as firms offering homogeneous products versus firms offering differentiated products, and another according to firms’ positions (upstream or downstream) in a distribution channel. Using these characterizations, they investigated the spillover effect of advertisers’ market entry decisions (with regard to whether or not to participate in a sponsored search auction), where the likelihood of an advertiser choosing a keyword to advertise is affected by competitors’ keyword entry decisions. They found that the spillover is positive if the new entrant appears below a focal firm’s advertisement, while the spillover could be either negative or positive if the new entrant appears above the focal firm’s advertisement. Furthermore, they found that when the search engine provides information to a firm on who else is competing in a sponsored search auction, the search engine’s revenue increases.

A recent study by Nie et al. (2021) characterized the heterogeneity across competitors using the theory of strategic groups (Caves & Porter, 1977; Porter, 1979). Using this characterization, they found that (1) the appearance of a competitor from the same strategic group leads to a lower CTR for a focal firm, and (2) the negative impact on the focal firm’s CTR is lower when it appears closer to its within-group competitors in the search results. Their work provides strong evidence of the existence of strategic groups in sponsored search environments.

As discussed earlier, the notion of the strategic group has been considered a central construct in the strategic management literature for diagnosing the competitive structure in a market (Mas‐Ruiz et al., 2014; Short et al., 2007; Surroca et al., 2016). Prior work has examined how consumers’ perceptions of strategic groups can impact their choice of stores in brick-and-mortar environments (Hodgkinson et al., 1996). This characterization provides a novel way to understand consumers’ navigation behaviors in online environments as well; therefore, we also adopt this in our work.

## 3 Hypotheses Development

We were interested in examining the following aspects of consumers’ clicking behaviors based on the strategic groups that advertisers belong to. First, we investigated how the co-appearance of firms from the same strategic group in the search results impacts the co-visit patterns of these firms in a consumer’s search session. Next, we studied whether the appearance of firms from a strategic group primes the consumer to visit the websites of other firms from that group. Drawing from the literature on strategic groups, consumer choice, and priming, we developed hypotheses that yield testable predictions.

## 3.1 The Co-Appearance Effect

Consumers use search engines to identify relevant providers (firms) for the products or services they are interested in. Based on the results provided by the search engine, consumers typically visit the sites of several competing firms during the session. What consumers see in the search results impacts their choice set (also referred to as the consideration set in the literature). The consideration set phenomenon has been used to refer to “brands that a consumer considers seriously when making a purchase and consumption decision” (Hauser & Wernerfelt, 1990). Because advertisers that show up in search results are often heterogeneous in nature, the strategic group theory can shed light on whether the competition from each advertiser has the same impact on a consumer’s consideration set, as reflected by their search session (all else being the same), or whether the impact differs depending on an advertiser’s strategic group membership.

While consumers often examine multiple firms during a search session, they are unlikely to examine too many competitors because of time and effort considerations. Instead, they are likely to pick a subset of the firms to visit and evaluate further by balancing consumption utility and evaluation cost (Hauser & Wernerfelt, 1990). The literature further notes that consumers display an innate desire to minimize effort when making such comparisons to arrive at their preferred choices (Gentner & Markman, 1994; Medin et al., 1995). Comparisons across firms are easier when they belong to the same strategic group relative to when they belong to diverse groups because of the relative proximity of products and services offered by such firms. Consequently, to simplify comparison, if a consumer’s mental model of a focal firm’s main competitors aligns with the strategic group membership of the focal firm, they will be more inclined to visit other firms within the same group during the session. This is supported by research on strategic groups, which suggests that consumers are aware of these groups and use them to mentally categorize the competitive landscape within an industry. For instance, Hodgkinson et al. (1996) found that shoppers, in the UK grocery retail sector, were more likely to visit stores within the same competitive group as their primary store than stores in different groups. This suggests that consumers are likely to focus their attention on a single group that aligns with their preferences instead of considering multiple groups when making decisions.

On the other hand, a consumer’s desire for variety could lead them to visit firms that are not very similar (Chakravarti & Janiszewski, 2003; Kahn, 1995; McAlister & Pessemier, 1982). In that case, the consumer would visit firms from different strategic groups. Therefore, when multiple firms from the same strategic group appear together (co-appear) in the search results, the consumer may not visit multiple firms from that group. Taking the air travel industry as an example, customers who are more price sensitive (and therefore predisposed toward low-cost carriers) might want to compare options from different websites since offerings from certain full-service carriers or online travel agencies might better fit their preferences (time of departure, arrival, number of connections, prices, etc.).

Consumer behavior can differ greatly between individuals, and often depends on the specific product or service in question. For instance, consumers tend to prefer variety in experience goods such as food or entertainment but seek consistency in utilitarian products or services, also known as search goods. According to Holbrook and Hirschman (1982), the preference for variety is often driven more by hedonic motives than utilitarian aspects. Trijp et al. (1996) observed that variety-seeking behavior is determined by a blend of individual and product-category characteristics.

The markets we study in this paper, air travel and digital cameras, have been recognized as examples of utilitarian goods. For instance, Anderson and Renault (2013) noted that despite some variations in seating comfort, food quality, or in-flight entertainment, the essential service of airlines—transporting passengers from one location to another—remains largely uniform across different providers. Similarly, Mudambi and Schuff (2010) stated that digital cameras, regardless of the brand, offer comparable specifications, such as image resolution and display size. In these cases, the consistency in core service or product features takes precedence over variety.

In sponsored search, this dynamic takes on a particular significance. When a search engine presents alternative products from within-group competitors, the ease of comparison impacts all customers viewing the search results. Further, as discussed above, the motivations for variety seeking are not very strong. Consequently, we expect the ease of comparison to be a stronger influence than the need for variety for the majority of the population, leading consumers to covisit firms from the same strategic group more often. To facilitate testing our conjecture, we used pairs of firms as the unit of analysis in this study; a pair of firms appearing in the search results could belong to the same strategic group or the pair could include firms from different groups. Thus, we propose the following:

H1: When a pair of firms is displayed in the search results, the probability of a consumer visiting both firms is higher if they are from the same strategic group than if they are from different strategic groups, ceteris paribus.

## 3.2 The Priming Effect

During a search session, consumers may visit the sites of firms whose advertisements appeared in the search results as well as the sites of other firms that did not appear in the search results. We expect the latter firms to be those the customer is aware of as relevant competitors of firms shown in the search results. This leads us to investigate how customers behave even when a firm of interest (i.e., the focal firm) is not shown in the search results.

We theorize from the perspective of priming developed in the psychology and marketing literatures. Priming is the activation of internal mental representations in an attempt to influence subsequent behavior (Bargh & Chartrand, 2000). Two types of priming effects can impact consumer choice behavior: perceptual priming and conceptual priming (Tulving & Schacter, 1990). Perceptual priming refers to the ease with which consumers recognize the target brand in subsequent encounters and involves processing the physical features of the considered brands. Conceptual priming reflects the ease with which the target brand comes to a consumer’s mind and pertains to the processing of meaning or perception (Lee & Labroo, 2004). The priming phenomenon has been examined in many studies related to consumer choices (Mullainathan, 2002; Dennis et al., 2013). However, priming has not been examined in the context of sponsored search.

Priming has been found to affect consumers’ brand choices. Lee (2002) and Lee and Labroo (2004) showed that some consumers’ decisions are based on information available in the physical environment (e.g., brand features) while others are memory-based in that they are based on information retrieved from memory (e.g., perceptions of a brand). These studies further revealed that the stimuli of ads shown together would enhance the conceptual fluency of consumers, rendering the stimulus more accessible in a consumer’s memory. This conceptual fluency underpins the priming effect, where consumers are predisposed to the concepts with which they are primed (more familiar).

In advertising, Nedungadi (1990) showed that memory factors aid brand retrieval because advertising cues that help a consumer retrieve and consider a target brand simultaneously increase the likelihood of considering other similar competing brands. In fact, Nedungadi (1990) further redefined a consideration set as “the set of brands brought to mind on a particular choice occasion”

(p. 264, emphasis added). Since strategic groups consist of closely competing firms, this suggests that the appearance of a firm in the search result will likely trigger the memory of other firms within the relevant group; furthermore, it may prompt consumers to consider and evaluate other firms from the same strategic group even when those firms do not appear in the search results.<sup>2</sup>

The literature on strategic groups has offered evidence that consumers recognize strategic groups in their mental model of the competitive structure in an industry. As discussed earlier, Hodgkinson et al. (1996) found that shoppers visit stores positioned in the same group of competitors as their primary store significantly more frequently than they visit stores positioned in other groups of competitors. This occurs because consumers learn over time that within-group firms closely competing with each other have similar offerings. Chernatony (1989) showed that consumers can identify which brands closely compete with which other brands. These survey-based studies have suggested that consumers consider the firm being primed (i.e., the primee) because of the stimulus from other within-group firms (i.e., the primer) in the search results. Using the clickstream data of individual consumers, we were able to objectively investigate whether such mental models impact consumers’ behaviors by analyzing what happens if the firm of interest is not displayed in the search result while other members from the same group are.

In contrast, consumers’ variety-seeking tendencies could also drive consumers to examine firms from other groups (Lee, 2002; Lee & Labroo, 2004). If variety seeking dominates priming, consumers might be more likely to visit across-group firms instead of restricting their visits to firms from one strategic group in the search results.

Therefore, when a firm (or a set of firms) within a group appears in the search results, the priming effect would drive consumers to visit other within-group firms not shown; the variety-seeking impetus would imply that consumers may visit across-group firms. As previously discussed with regard to the co-appearance effect, the variety-seeking effect is not as strong as ease of comparison for utilitarian goods because of the mental models users have. In addition, prior research in other contexts has established the importance of the priming effect on brand choice (Lee, 2002; Karremans et al., 2006). Therefore, we expect that when a firm within a strategic group appears in the search results, the priming effect would bring to the consumer’s mind other firms from that group, instead of firms from other groups. This, in turn, would lead to more visits to firms within the group. Thus, our next hypothesis is:

H2: The appearance of a firm (primer) in the search results would increase a consumer’s likelihood of visiting another firm (primee) from the same strategic group, relative to visiting a firm from a different group, ceteris paribus.

By considering both the presence of a focal firm in the search results as well as its absence, H1 and H2 together provide a set of complementary analyses of the influence of strategic groups on consumers’ perceptions in sponsored search advertising.

## 4 Data

The two markets we consider serve as ideal settings for addressing our research questions because they are competitive markets characterized by many heterogeneous firms.

## 4.1 Air Travel Data

The firms in the air travel market include leading airlines like American Airlines and United Airlines, low-cost airlines like AirTran and JetBlue, and online travel agencies like Priceline and Expedia. These firms fall into a natural grouping as characterized in prior research (Pels, 2008; Tae et al., 2020). Second, these industries are composed of many firms competing in highly rivalrous markets (Chellappa et al., 2011), where consumers search before making purchase decisions. In addition, the air travel market has been examined extensively in the literature in other contexts (Clemons et al., 2002; Granados et al., 2012; Li et al., 2014). Therefore, it provides rich soil to understand how consumers search and click when using search engines.

We collected data from two sources regarding the air travel industry: consumers’ clickstream data from Comscore and search results from Google. The Comscore data capture a representative sample of U.S. internet users’ browsing behavior and purchases and has been commonly used in extant research (e.g., Chesnes et al., 2017; Zheng et al., 2011). Comscore segments the browsing history into sessions and further categorizes sessions based on purchase categories when a purchase is made during the session. A search session would be uncategorized if no purchase occurred within the session. We obtained clickstream data from Comscore between May and November 2009. It recorded 29,444,904 sessions. For the “air travel” purchase category, there were 7,411 unique sessions (i.e., sessions with purchase). We tallied the frequency of sessions for each unique firm that Comscore tracked under the “air travel” category in Table 1. We note that more than one of the listed firms might appear in some sessions.

Table 1. Firms Appearing in Purchase Sessions in Comscore

<table><tr><td>Firm</td><td>Number of sessions</td></tr><tr><td>Southwest Airlines</td><td>2135</td></tr><tr><td>Expedia</td><td>846</td></tr><tr><td>Priceline</td><td>653</td></tr><tr><td>JetBlue Airways</td><td>580</td></tr><tr><td>Orbitz</td><td>552</td></tr><tr><td>Travelocity</td><td>488</td></tr><tr><td>American Airlines</td><td>482</td></tr><tr><td>CheapTickets</td><td>423</td></tr><tr><td>Delta Airlines</td><td>412</td></tr><tr><td>AirTran Airways</td><td>373</td></tr><tr><td>Continental Airlines</td><td>349</td></tr><tr><td>Alaska Airlines</td><td>309</td></tr><tr><td>US Airways</td><td>282</td></tr><tr><td>United Airlines</td><td>189</td></tr><tr><td>Spirit Airlines</td><td>151</td></tr><tr><td>Hotwire</td><td>115</td></tr><tr><td>Yahoo</td><td>39</td></tr><tr><td>Sabre Sonic Web</td><td>28</td></tr><tr><td>AOL</td><td>25</td></tr><tr><td>American Express Travel</td><td>15</td></tr><tr><td>wwte1</td><td>3</td></tr><tr><td>Amazon</td><td>1</td></tr></table>

In total, 16 of the 22 firms appeared in more than 100 sessions that Comscore labeled as “air travel” purchase sessions. To ensure meaningful statistical analysis, we include these 16 advertisers in our analyses. To resolve the uncertainty about price and quality, consumers might search for a product multiple times before making a purchase (Bronnenberg et al., 2016; Ursu et al., 2020); therefore, we included all the sessions related to air travel, regardless of whether the session includes a purchase. We identified the related click-stream sessions as follows: a session was considered air travel related if one of the 16 travel companies was visited. Another 503,736 sessions were identified as related to air travel in this manner.

For the search results part, we collected data from Google.com for the search term “air travel” approximately once an hour during the same time period.

In total, the “air travel” market attracted 810 distinct advertisers across the 2,305 search results we extracted.<sup>3</sup>

Since we wanted to know how the search results affected consumers’ browsing behavior, we matched the visit sessions with the search results in terms of recency following Nie et al. (2021)—the search result that appeared immediately before the beginning of a clickstream session was matched. <sup>4</sup> If the closest preceding search result was more than two hours before the beginning of a session, we dropped that session, as the results may not have closely emulated the search results for that particular clickstream session.<sup>5</sup> As a result, we were left with 74,931 unique sessions with matched search results. We note that data aggregated on a daily basis, which are typically used in the literature, ignore intraday variations and could bias the estimations for CTR (Abhishek et al., 2015). We avoided such biases by utilizing data for distinct clickstream sessions collected multiple times during the course of a day.

In order to conduct our analyses, we needed to determine the strategic group memberships of the 16 shortlisted firms from Table 1. First, there are two types of firms that are very different from each other: online travel agencies (OTAs) and airline carriers. OTAs are different from carriers in terms of their operations, asset bases, cost structures, and other dimensions of their strategic profiles, which are typically used to distinguish strategic groups (Peteraf, 1993). Further, the United States Department of Transportation (U.S. DOT) considers OTAs to be a separate group from the carriers’ groups when reporting performance metrics (The Office of Aviation Consumer Protection, 2021).

The airline carriers can be further segmented into two groups, low-cost carriers (LCCs) and full-service carriers (FSCs), as designated by the U.S. DOT and recognized in extant literature (Pels, 2008; Firestine & Guarino, 2012; Tae et al., 2020). LCCs, commonly referred to as budget airlines, refer to the airlines with a lower operating cost structure than their competitors. These airlines operate with an emphasis on minimizing operating costs by reducing some of the traditional services and amenities (e.g., beverages and carry-on luggage) included in the fare. We accordingly categorized the following four carriers as low-cost carriers (LCCs): AirTran, JetBlue, Southwest, and

Spirit. The other airlines were classified as full-service carriers. This grouping is consistent with how Porter (2008, p. 35) characterized strategic groups in the literature by outlining two fundamental ways to compete—namely, low-cost leadership (with highvolume production) and product differentiation (by specializing in markets).

Table 2 presents these three groups of firms (OTA, FSC, LCC), based on the different scopes, resource bases, and strategic profiles that help to distinguish strategic groups.

## 4.2 Digital Camera Data

The second market we investigate is for the search keyword “digital camera.” The data are from Nie et al. (2021). The Google search results are for the same period (May to November 2009), and 1,249 unique clickstream sessions were identified. Nie et al. (2021) first identified the key firms that are advertised to customers who search in Google for “digital camera,” and then found the key competitors for each firm in the Hoover’s and LexisNexis databases, which are commonly used in the industry to identify competitors. Each firm and its key competitors comprised one competitor set. They derived a distance matrix across all firm pairs based on how frequently a pair of firms appeared in the competitor sets. Finally, they used a hierarchical clustering method to identify the four strategic groups for the 26 firms that advertised for that search keyword. The four strategic groups they identified are shown in Table 3.

Table 2. Strategic Groups for the Air Travel Industry

<table><tr><td>Strategic group</td><td>Firm members</td></tr><tr><td>Online travel agency</td><td>CheapTickets, Expedia, Hotwire, Orbitz, Priceline, Travelocity</td></tr><tr><td>Full-service carrier</td><td>American Airlines, Alaska Airlines, Continental Airlines, Delta Airlines, United Airlines, US Airways</td></tr><tr><td>Low-cost carrier</td><td>AirTran Airways, JetBlue Airways, Southwest Airlines, Spirit Airlines</td></tr></table>

Table 3. Strategic Groups for Digital Camera Market (Nie et al. 2021)

<table><tr><td>Group</td><td>Firms</td></tr><tr><td>1</td><td>Amazon, eBay, HSN, Google, Bing, Yahoo</td></tr><tr><td>2</td><td>Canon, Kodak, Nikon, Olympus, Philips, Samsung, Sony</td></tr><tr><td>3</td><td>Best Buy, Dell, Office Max, Radio Shack, Sears, Staples, Target, Walmart</td></tr><tr><td>4</td><td>Bonton, Buy, Circuit City, HHGregg, Kmart, NexTag, RCWilley, RitzCamera</td></tr></table>

## 5 Models and Analyses

## 5.1 The Co-Appearance Effect

The advertisers a customer visits within a session among those displayed in Google’s search results could be from the same strategic group or from different groups. We hypothesize in H1 that consumers are more likely to visit the websites of both firms when these two firms come from the same strategic group, compared to the case when they are from different groups.

We define the variable $C o - V i s i t _ { i j s }$ to denote whether a pair of firms i and j gets co-visited in session s. The variable Within<sub>ij</sub> is 1 when firms i and j from the same strategic group are shown in the search results; it is 0 when firms i and j appearing in the search results are from different strategic groups.<sup>6</sup> For these analyses, we obtained 55,475 observations from the air travel market and 7,614 observations from the digital camera market.<sup>7</sup> The descriptive statistics for the two markets are presented in the Appendix (Tables D1-D4). The variable Within for the FSC group in the air travel market is always zero (Table D1), which indicates that the FSC members did not co-appear in the search results in our data. Therefore, we excluded the FSC group for the air travel market when testing H1. We used the logit model shown in Equation 1 to capture the influence of within-group firms’ co-appearance on consumers’ co-visiting patterns. To account for the potential impact of the ranks of the firms in the search results, we calculated the rank difference (RankDiff<sub>ijs</sub>) between a focal firm i and its competitor j and controlled for this variable in our analysis. Advertising strategies of individual firms and time trends may influence consumers’ website-visit behaviors in a way that is unobservable to researchers. To rule out such alternative explanations, we also controlled for the firm fixed effects (using terms $\lambda _ { i }$ and $\lambda _ { j } )$ and the time fixed effects at the weekly level (using $\tau _ { s } ) . ^ { 8 }$ By doing so, any bias caused by firm-specific shocks is controlled for. In addition, changes in consumers’ browsing behaviors at different time periods won’t bias our estimation results.

$$
\begin{array}{l} \text { Logit(Co - Visit } _ {\text { ijs })} = \beta_ {0} + \beta_ {1} \text { Within } _ {\text { ij }} + \beta_ {2} \text { RankDiff } _ {\text { ijs }} \\ + \lambda_ {\text { i}} + \lambda_ {\text { j }} + \tau_ {s} + \varepsilon_ {\text { ijs }}. \end{array}\tag{1}
$$

Table 4 presents the estimated parameters and the corresponding robust standard errors (in parentheses). It shows that the estimated coefficients for the variable Within are positive and significant in both markets. This indicates that when a pair of firms comes from the same strategic group, the chance of a customer visiting both is significantly higher than the case when the pair of firms comes from different strategic groups. If a pair of firms is from the same strategic group (versus from different groups), its odds of being co-visited are boosted by a factor of 1.848 $ ( = \mathsf { e } ^ { 0 . 6 \mathsf { 1 4 } }$ based on the estimated $\beta _ { 1 } )$ in the air travel market. In the digital camera market, the odds of being co-visited are increased by a factor of 1.679. Our results reveal that co-appearance with other within-group competitors improves the probability of the consumer co-visiting both firms. This novel finding has nontrivial implications for search engine platforms—all else being the same, they would benefit by displaying advertisers from the same strategic group in their search results instead of from across groups to increase the overall CTRs.

Table 4. Co-Visit Results

<table><tr><td>Variable</td><td>Air travel</td><td>Digital camera</td></tr><tr><td>Within</td><td>0.614***(0.138)</td><td>0.518***(0.133)</td></tr><tr><td>RankDiff</td><td>-0.018***(0.005)</td><td>0.033(0.022)</td></tr><tr><td>Firm FE</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td></tr><tr><td>AIC</td><td>51,578.377</td><td>3,021.891</td></tr><tr><td>Num of obs (N)</td><td>54,211</td><td>7,614</td></tr><tr><td colspan="3">Note: *** p &lt; 0.01, ** p &lt; 0.05, * p &lt; 0.1. Robust errors in parentheses.</td></tr></table>

analyses to examine whether the organic search results might have confounded our findings—these experiments are presented in Appendix A. As discussed there, we considered the appearance of firms in either organic or sponsored search results (or both) when conducting the analyses. Our results are robust whether the organic search listings are considered or not.

The results in Table 4 indicate that the probability of consumers visiting both firms increases significantly when both firms are from the same strategic group, relative to when they are from different groups. Therefore, H1 is supported in both the air travel and the digital camera markets.

## 5.2 The Priming Effect

We conjecture in H2 that consumers’ browsing behaviors reflect their corresponding mental models of strategic groups. For example, the appearance of Expedia in the search results could remind the consumer to visit Priceline, as both advertisers belong to the same strategic group of online travel agencies. If this holds, Priceline will reap a spillover effect even if only Expedia appears in the search results. Therefore, we would expect the appearance of one member of a strategic group to prime consumers to visit the websites of the other members from the same group.

To operationalize this, we constructed the following variables. The variable VisitFocal indicates if the focal firm i is visited in session s. The variable Primer<sub>is</sub> is a dummy variable that takes the value 1 if any other withingroup member(s) appeared in the search results when the focal firm did not appear. $P r i m e r _ { i s }$ is 0 when neither the focal firm nor any other within-group member appeared in the search results. The rationale is that priming for a focal firm can occur only when the focal firm does not appear in the search results but some other within-group member(s) appears in the search results. The variable Primer for the OTA group is always 1 (Table D2 in the Appendix), which indicates that at least one of the OTA firms always appears in the search results. Therefore, we removed the OTA group from the air travel market when testing H2. For the digital camera market, Primer = 1 occurs very often for Groups 1 and 3 (95% and 99% of the observations as shown in Table D4). The results we report on the digital camera market include all 4 groups. Our findings remain consistent whether or not we excluded these two groups from the digital camera data when testing H2.

To investigate the influence of priming on visits to the focal firm’s site, we used the logit model in Equation 2. We controlled for the rank of the primer (the highestranked within-group member that shows up in the search results) using the variable PrimerRank<sub>is</sub>. Similar to Equation 1, we ruled out alternative explanations by controlling for the firm fixed effects and weekly time fixed effects.

$$
\begin{array}{l} \text { Logit(VisitFocal } _ {\text { is })} = \beta_ {0} + \beta_ {1} \text { Primer } _ {\text { is }} + \beta_ {2} \text { PrimerRank } _ {\text { is }} \\ + \lambda_ {\text { i}} + \tau_ {s} + \varepsilon_ {\text { is }}. \end{array}\tag{2}
$$

Table 5 presents the results for Equation 2. For the air travel market, the coefficient for Primer is 1.577, and it is statistically significant at the 1% level. For the digital camera market, the coefficient is 0.445, which is statistically significant at the 5% level. Priming from another within-group competitor improves the odds of a consumer visiting a focal firm by a factor of 4.840 in the air travel market $\stackrel { - } { ( } = \mathbf { e } ^ { 1 . 5 7 7 }$ based on the estimated β<sub>1</sub>) and a factor of 1.560 in the digital camera market. Therefore, priming increases the likelihood of a consumer visiting a focal firm in both markets compared to when priming does not occur.

As shown in Table 5, the estimated coefficients for Primer are qualitatively unchanged from market to market. Therefore, consumers are more likely to visit the focal firm when the search results lead to priming. In sum, our analyses for both markets lend support to H2.

## 5.3 Addressing Endogeneity and Measurement Errors

There are several sources of endogeneity that may potentially bias our estimation results. Omitted relevant variables could be such a cause. In the main analyses, we added the controls for the firm ranks in the search results and the firm fixed effects and time fixed effects to absorb firm-specific and time-specific heterogeneities. In Appendix A, we validate the robustness of our results when organic search results are considered.

Measurement error could be another cause. It might be argued that the search results matched on the basis of a two-hour window might be too coarse to capture the actual search results that customers are seeing. Google presents 10 organic links in the organic search results and 11 sponsored links in the sponsored search section. Across the two markets, we observed that of the 11 advertisers that appear in sponsored search results, around 9.4 on average continued to appear in subsequent search results within a two-hour window. This indicates that the search results are quite stable over a two-hour window. To further alleviate concerns about measurement error, we conducted robustness checks using a more conservative one-hour matching window. The results are consistent with the main results and are presented in Appendix B.

Furthermore, our construction of the priming variable may be subject to measurement error as well. For example, it is possible that priming instances are misclassified as non-priming instances or vice versa when consumers use Google’s search engine multiple times during a session. We employed the MC-SIMEX (misclassification simulation extrapolation) method to factor in the potential presence of such measurement errors (Yang et al. 2018). The method first simulates multiple versions of the variable (that is subject to measurement error) with varying degrees of errors and estimates the regression coefficient of the variable (the priming variable in our context) for each version separately. It then extrapolates to the hypothetical case when the variable is not contaminated by any measurement error in order to derive the error-free coefficient accordingly.

Table 5. Priming Results

<table><tr><td>Variable</td><td>Air travel</td><td>Digital camera</td></tr><tr><td>Primer</td><td>1.577***(0.123)</td><td>0.445**(0.193)</td></tr><tr><td>PrimerRank</td><td>0.233***(0.020)</td><td>0.038**(0.017)</td></tr><tr><td>Firm FE</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td></tr><tr><td>AIC</td><td>13,982.879</td><td>6,491.277</td></tr><tr><td>Num of obs (N)</td><td>12,939</td><td>16,873</td></tr><tr><td colspan="3">Note: *** p &lt; 0.01, ** p &lt; 0.05, * p &lt; 0.1. Robust errors in parentheses.</td></tr></table>

To use the MC-SIMEX method, we needed the misclassification error rates (false negative and false positive rates). Although we did not have the ground truth observations, we were able to estimate the upper bound of the misclassification errors rates by the ratio of sessions that had more than one visit to Google. In our data, these ratios were 5.765% and 22.597% for the digital camera and air travel markets, respectively. Though multiple Google searches in a single session may lead to either false positive or false negative errors, the worst-case scenario in terms of overcounting priming instances is when all such sessions cause false positive errors (misclassify nonpriming as priming). Using this most conservative assumption with MC-SIMEX, we determined that our results were consistent with those found earlier. Specifically, the estimated coefficients pertaining to the priming effect increased to 1.732 and 0.502 for the air travel and digital camera markets respectively, as compared to 1.577 and 0.445 reported in Table 5.

Since the data span several months, it is possible that consumers’ browsing behaviors may have been affected because of marketing campaigns by different firms. We controlled for such possibilities by including firmspecific time fixed effects.<sup>9</sup> The results are qualitatively unchanged and are presented in Appendix C.

Another confounding factor is that consumers might be in different (funnel) stages of evaluation and purchase when searching for products. In Section 6, we reevaluate both hypotheses by explicitly controlling for consumers’ search stages.

Simultaneity could also cause endogeneity if firms had the ability to determine their strategic group affiliation based on consumers’ co-visit or priming patterns. However, this is unlikely to be the case in our context because the strategic group membership is derived from the literature and is exogenous from the websitevisit behavior of customers for both markets.

## 6 Search Stages and Strategic Groups

Our hypotheses implicitly assume that consumers are homogeneous in terms of their search behavior. In practice, consumers might arrive at a search engine at different stages of their evaluation and purchase process. The marketing literature has characterized the different stages that lead to a consumer’s path to purchase as a purchase funnel. A common description of a purchase funnel includes the following three stages: awareness, consideration, and purchase (Moe, 2006; Wu & Rangaswamy, 2003). Along these lines, a consumer’s search intent can be dichotomized as either focused (goal-directed) or exploratory (Janiszewski, 1998; Moe, 2003). Through exploratory search, a consumer shrinks the set of potential alternatives from the awareness set to the consideration set; through focused search, the consideration set further shrinks down to the purchase set. Janiszewski (1998) further argues that focused search involves the planned acquisition of information using a search routine stored in memory, while exploratory search involves either a screening process that identifies candidates for focused search or as an information gathering device when focused search routines are inadequate.

An identification challenge that may arise is whether the observed consumers’ clicking behaviors are merely a reflection of the consumer’s search intent (exploratory versus focused) rather than being driven by the strategic group characterization of competing advertisers. To determine whether the observed search behavior is driven by the consumers’ search intent (instead of the mental models derived from their recognition of strategic groups), we reevaluated both hypotheses by examining whether the behavior could be explained by the search intent alone, or whether both effects were manifest even when we considered consumers at different stages of the purchase funnel.

To operationalize this, we first differentiated focused sessions from exploratory ones. The Comscore data explicitly capture whether a consumer made a purchase in a session or not. We labeled those sessions in which customers made purchases as focused sessions; we labeled the rest as exploratory sessions. This classification results in 960 focused sessions (1.28%) out of the 74,931 matched sessions in the air travel market. The clickstream data for the digital camera market did not explicitly capture whether a consumer made a purchase in a session or not. What we can observe is whether the URLs visited by the consumer were under the secure https protocol or not. If a consumer visited a camera-selling domain’s URL with the https protocol, <sup>10</sup> then we would expect the consumer to be further along in the purchase funnel. We labeled such sessions as focused sessions; otherwise, we label them as exploratory sessions. This classification resulted in 219 focused sessions (17.53%) out of the 1,249 sessions. We used the variable Focused to indicate whether a particular session was a focused session for both markets. For the co-appearance effect, we added the term Focused to explore whether the effect was driven by the search stage (i.e., focused or exploratory sessions):<sup>11</sup>

$$
\begin{array}{l} \text { Logit(Co - Visit } _ {\text { ijs })} = \beta_ {0} + \beta_ {1} \text { Within } _ {\text { ij }} + \beta_ {2} \text { Focused } _ {s} \\ + \beta_ {3} \text { RankDiff } _ {\text { ijs }} + \lambda_ {i} + \lambda_ {j} + \tau_ {s} + \varepsilon_ {\text { ijs }}. \end{array}\tag{3}
$$

The coefficient $\beta _ { 1 }$ corresponding to Within<sub>ij</sub> captures the difference in the likelihood of a consumer visiting a pair of firms from the same strategic group versus from different groups. The results for estimating the two markets are presented in Table 6. All models show that the estimated coefficients for Within remain positive and significant, lending further support to H1.

Next, we reevaluated H2 using a variant of Equation 2 to investigate whether the search stage alone could explain the priming effect. This variant, as specified in Equation 4, incorporates Focused as a control for the different session types:

$$
\begin{array}{l} \text { Logit(VisitFocal } _ {\text { is })} = \beta_ {0} + \beta_ {1} \text { Primer } _ {\text { is }} + \beta_ {2} \text { Focused } _ {s} + \\ \beta_ {3} \text { PrimerRank } _ {\text { is }} + \lambda_ {i} + \tau_ {s} + \varepsilon_ {\text { is }}. \end{array}\tag{4}
$$

The results are presented in Table 7. The estimated coefficients for Primer remain positive and significant for both markets, which means that the priming effect existed in the exploratory sessions. This reinforces our findings for H2. In summary, by considering the search stage of consumers, we ruled out the alternative explanation of the search stage being the sole driver for our findings.

Table 6. Co-Visit Results with Search Stage Control

<table><tr><td>Variable</td><td>Air travel</td><td>Digital camera</td></tr><tr><td>Within</td><td>0.617***(0.138)</td><td>0.519***(0.133)</td></tr><tr><td>Focused</td><td>0.354***(0.051)</td><td>0.167(0.112)</td></tr><tr><td>RankDiff</td><td>-0.018***(0.005)</td><td>0.033(0.022)</td></tr><tr><td>Firm FE</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td></tr><tr><td>AIC</td><td>51,530.992</td><td>3,021.716</td></tr><tr><td>Num of obs (N)</td><td>54,211</td><td>7,614</td></tr><tr><td colspan="3">Note: *** p&lt;0.01, ** p&lt;0.05, * p&lt;0.1. Robust errors in parentheses.</td></tr></table>

Table 7. Priming Results with Search Stage Contro

<table><tr><td>Variable</td><td>Air travel</td><td>Digital camera</td></tr><tr><td>Primer</td><td>1.576***(0.123)</td><td>0.425**(0.192)</td></tr><tr><td rowspan="2">Focused</td><td>-0.068</td><td>0.229***</td></tr><tr><td>(0.097)</td><td>(0.075)</td></tr><tr><td>PrimerRank</td><td>0.233***(0.020)</td><td>0.038**(0.017)</td></tr><tr><td>Firm FE</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td></tr><tr><td>AIC</td><td>13,984.392</td><td>6,483.492</td></tr><tr><td>Num of obs (N)</td><td>12,939</td><td>16,873</td></tr><tr><td colspan="3">Note: *** p &lt; 0.01, ** p &lt; 0.05, * p &lt; 0.1. Robust errors in parentheses.</td></tr></table>

<sup>11</sup> We used the Chow test to examine whether there was a significant difference between the focused and exploratory sessions. At a 5% significance level, we failed to reject the null hypothesis that the two coefficients are the same. Therefore, we ran the logit model by pooling the data from the focused and the exploratory sessions together. Similar to Model (3), we performed the Chow test when evaluating the priming effect in Model (4). Once again, the test showed that the focused and exploratory sessions can be pooled in the analyses for both markets.

## 7 Conclusion

This study enriches the sponsored search literature by studying individual consumers’ reactions to the complex competitive structure of firms in the search advertising market. Using the strategic group theory to characterize the structure of heterogeneous firms competing in two different search markets, our paper extends current research by examining the effect of strategic groups on consumers’ website-visit behavior in the presence or absence of a focal firm. We found that (1) the probability of a consumer co-visiting a pair of firms is significantly higher when both firms are from the same strategic group and (2) the probability of a consumer visiting a firm is significantly higher when other within-group firms appear in the search results compared to when other within-group firms do not.

Our research contributes to the literatures on both sponsored search and strategic groups. Prior work in search advertising has mainly examined the effect of competing ads in limited contexts, such as advertisers appearing adjacent to a focal firm in the search results (e.g., Jeziorski and Segal 2015) or the effect of poaching (e.g., Bhattacharya et al 2022; Simonov & Hill 2021). We build on a previous study by Nie et al. (2021) to investigate the impact of strategic groups in the sponsored search context. By utilizing a combination of session-level search and clickstream data, instead of aggregated data commonly used in the literature (e.g., monthly AdWords report from Google), we enrich the literature by studying how a consumer’s mental model of strategic groups influences their propensity to visit a firm’s website both when the firm appears in the search results (the co-visit effect) and when it does not (the priming effect). We contribute to the literature on strategic groups (Mas‐Ruiz et al., 2014; Short et al., 2007; Surroca et al., 2016) by demonstrating the impact of such groups in the online context of search advertising, an area hitherto unexamined in this body of work.

Our findings have important practical implications. First, we found that when advertising firms come from the same strategic group, consumers tend to co-visit the firms’ websites during the session. Search engines like Google typically embrace the CPC (cost per click) model in which they are paid only when consumers actually click on the links. Therefore, search engines should factor in the presence of multiple firms within a strategic group when estimating the quality score and projecting the CTR for ads. For example, suppose Expedia will be displayed in a sponsored search list. In that case, the search engine may prefer to include other online travel agencies from the same strategic group to take advantage of consumers’ co-visit behavior. Second, our findings reveal that the appearance of firms belonging to a strategic group prime consumers to visit other firms from the same group even when the other firms are not displayed in the search results. This spillover effect for within-group firms’ advertisements could allow advertisers to reduce competition intensity. Therefore, advertising firms might reconsider their budget allocations for keywords in sponsored search auctions, anticipating additional traffic brought to their site due to the priming effect of the advertisements of other members in their strategic group. However, this may not bode well for search engines that use a CPC business model because advertisers only pay when the click comes from the search results displayed by the search engine. This subtle but important conflict of interest requires careful attention by both search engines and advertisers and deserves further research.

Our study has a few limitations. First, the two markets we studied, air travel and digital camera, both offer search goods (Anderson & Renault, 2013; Mudambi & Schuff, 2010). We cannot unequivocally claim whether the co-visit and priming effects can be generalized to other product types such as experience goods. Second, we matched the search results with the consumers’ clickstream behavior based on their temporal proximity. While we demonstrate that our results are robust to measurement errors (using MC-SIMEX), it would have been ideal to connect each search result with the associated clickstream unambiguously. Future research could potentially employ lab or field experiments to accomplish this— doing so would also enable more fine-grained analysis of related issues. These issues could include identifying (1) how the magnitude of the rank difference between within-group firms affects the covisit behavior, (2) how the specific rank of a firm from a strategic group appearing in the search results could impact co-visit and priming behavior, and (3) the impact of the number of priming firms on user behavior.

## References

Abhishek, V., Hosanagar, K., & Fader, P. S. (2015). Aggregation bias in sponsored search data: The curse and the cure. Marketing Science, 34(1), 59- 77.

Agarwal, A., Hosanagar, K., & Smith, M. D. (2015). Do organic results help or hurt sponsored search performance? Information Systems Research, 26(4), 695-713.

Amaldoss, W., Desai, P. S., & Shin, W. (2015). Keyword search advertising and first-page bid estimates: A strategic analysis. Management Science, 61(3), 507-519.

Amaldoss, W., Jerath, K., & Sayedi, A. (2016). Keyword management costs and “broad match” in sponsored search advertising. Marketing Science, 35(2), 259-274.

Animesh, A., Viswanathan, S., & Agarwal, R. (2011). Competing “creatively” in sponsored search markets: The effect of rank, differentiation strategy, and competition on performance. Information Systems Research, 22(1), 153-169.

Anderson, S. P., & Renault, R. (2013). The advertising mix for a search good. Management Science, 59(1), 69-83.

Asadpour, A., Bateni, M., Bhawalkar, K., & Mirrokni, V. (2019). Concise bid optimization strategies with multiple budget constraints. Management Science, 65(12), 5785-5812.

Balseiro, S. R., & Gur, Y. (2019). Learning in repeated auctions with budgets: Regret minimization and equilibrium. Management Science, 65(9), 3952- 3968.

Bargh, J. A., & Chartrand, T. L. (2000). Studying the mind in the middle: A practical guide to priming and automaticity research. In H. Reis & C. Judd (Eds.), Handbook of research methods in social psychology (pp. 253-285). Cambridge University Press.

Bhattacharya, S., Gong, J., & Wattal, S. (2022). Competitive poaching in search advertising: Two randomized field experiments. Information Systems Research, 33(2), 599-619.

Bronnenberg, B. J., Kim, J. B., & Mela, C. F. (2016). Zooming in on choice: How do consumers search for cameras online? Marketing Science, 35(5), 693-712.

Caves, R. E., & Porter, M. E. (1977). From entry barriers to mobility barriers: Conjectural decisions and contrived deterrence to new competition. The Quarterly Journal of Economics, 91(2), 241.

Chakravarti, A., & Janiszewski, C. (2003). The influence of macro‐level motives on consideration set composition in novel purchase situations. Journal of Consumer Research, 30(2), 244-258.

Chellappa, R. K., Sin, R. G., & Siddarth, S. (2011). Price formats as a source of price dispersion: A study of online and offline prices in the domestic U.S. airline markets. Information Systems Research, 22(1), 83-98.

Chernatony, L. de. (1989). Marketers’ and consumers’ concurring perceptions of market structure. European Journal of Marketing, 23(1), 7-16.

Chesnes, M., Dai, W. (Daisy), & Zhe Jin, G. (2017). Banning foreign pharmacies from sponsored search: The online consumer response. Marketing Science, 36(6), 879-907.

Clemons, E. K., Hann, I.-H., & Hitt, L. M. (2002). Price dispersion and differentiation in online travel: An empirical investigation. Management Science, 48(4), 534-549.

Dennis, A. R., Minas, R. K., & Bhagwatwar, A. P. (2013). Sparking creativity: Improving electronic brainstorming with individual cognitive priming. Journal of Management Information Systems, 29(4), 195-216.

Du, X., Su, M., Zhang, X. (Michael), & Zheng, X. (2017). Bidding for multiple keywords in sponsored search advertising: keyword categories and match types. Information Systems Research, 28(4), 711- 722.

Edelman, B., & Ostrovsky, M. (2007). Strategic bidder behavior in sponsored search auctions. Decision Support Systems, 43(1), 192-198.

Edelman, B., Ostrovsky, M., & Schwarz, M. (2007). Internet advertising and the generalized second price auction: Selling billions of dollars worth of keywords. American Economic Review, 97(1), 242-259.

Feng, J., Bhargava, H. K., & Pennock, D. M. (2007). Implementing sponsored search in web search engines: Computational evaluation of alternative mechanisms. INFORMS Journal on Computing, 19(1), 137-148.

Firestine, T., & Guarino, J. (2012). A decade of change in fuel prices and US domestic passenger aviation operations (Bureau of Transportation Statistics special report). United States Department of Transportation. https://www.bts.gov/sites/bts.dot. gov/files/legacy/publications/special\_reports\_and \_issue\_briefs/special\_report/2012\_03\_33/pdf/enti re.pdf

Gentner, D., & Markman, A. B. (1994). Structural alignment in comparison: No difference without similarity. Psychological Science, 5(3), 152-158.

Granados, N., Gupta, A., & Kauffman, R. J. (2012). Online and offline demand and price elasticities: Evidence from the air travel industry. Information Systems Research, 23(1), 164-181.

Hauser, J. R., & Wernerfelt, B. (1990). An Evaluation cost model of consideration sets. Journal of Consumer Research, 16(4), 393-408.

Hodgkinson, G. P., Tomes, A. E., & Padmore, J. (1996). Using consumers’ perceptions for the cognitive analysis of corporate-level competitive structures. Journal of Strategic Marketing, 4(1), 1-22.

Holbrook, M. B., & Hirschman, E. C. (1982). The experiential aspects of consumption: Consumer Fantasies, feelings, and fun. Journal of Consumer Research, 9(2), 132-140.

Google (2023). Analytics Help — How a web session is defined in Universal Analytics. https://support. google.com/analytics/answer/2731565

IAB Report. (2023). Internet advertising revenue report. https://www.iab.com/wp-content/uploads/2023/ 04/IAB\_PwC\_Internet\_Advertising\_Revenue\_R eport\_2022.pdf

Janiszewski, C. (1998). The influence of display characteristics on visual exploratory search behavior. Journal of Consumer Research, 25(3), 290-301.

Jerath, K., Ma, L., Park, Y.-H., & Srinivasan, K. (2011). A “position paradox” in sponsored search auctions. Marketing Science, 30(4), 612-627.

Jeziorski, P., & Segal, I. (2015). What makes them click: Empirical analysis of consumer demand for search advertising. American Economic Journal: Microeconomics, 7(3), 24-53.

Kahn, B. E. (1995). Consumer variety-seeking among goods and services: An integrative review. Journal of Retailing and Consumer Services, 2(3), 139-148.

Karremans, J. C., Stroebe, W., & Claus, J. (2006). Beyond Vicary’s fantasies: The impact of subliminal priming and brand choice. Journal of Experimental Social Psychology, 42(6), 792-798.

Kelly, F., Key, P., & Walton, N. (2016). Efficient advert assignment. Operations Research, 64(4), 822- 837.

Kwark, Y., Lee, G. M., Pavlou, P. A., & Qiu, L. (2021). On the spillover effects of online product reviews on purchases: Evidence from clickstream data. Information Systems Research, 32(3), 895-913.

Lahaie, S., & Pennock, D. M. (2007). Revenue analysis of a family of ranking rules for keyword auctions. Proceedings of the 8th ACM Conference on Electronic Commerce (pp. 50-56).

Lee, A. Y. (2002). Effects of implicit memory on memory-based versus stimulus-based brand choice. Journal of Marketing Research, 39(4), 440-454.

Lee, A. Y., & Labroo, A. A. (2004). The effect of conceptual and perceptual fluency on brand evaluation. Journal of Marketing Research, 41(2), 151-165.

Li, J., Granados, N., & Netessine, S. (2014). Are consumers strategic? Structural estimation from the air-travel industry. Management Science, 60(9), 2114-2137.

Liu, D., Chen, J., & Whinston, A. B. (2010). Ex ante information and the design of keyword auctions. Information Systems Research, 21(1), 133-153.

Lu, S., & Yang, S. (2017). Investigating the spillover effect of keyword market entry in sponsored search advertising. Marketing Science, 36(6), 976- 998.

Lu, X., & Zhao, X. (2014). Differential effects of keyword selection in search engine advertising on direct and indirect sales. Journal of Management Information Systems, 30(4), 299-326.

Mas‐Ruiz, F., Ruiz‐Moreno, F., & Martínez, A. L. de G. (2014). Asymmetric rivalry within and between strategic groups. Strategic Management Journal, 35(3), 419-439.

McAlister, L., & Pessemier, E. (1982). Variety seeking behavior: an interdisciplinary review. Journal of Consumer Research, 9(3), 311-322.

Medin, D. L., Goldstone, R. L., & Markman, A. B. (1995). Comparison and choice: Relations between similarity processes and decision processes. Psychonomic Bulletin & Review, 2(1), 1-19.

Moe, W. W. (2003). Buying, searching, or browsing: Differentiating between online shoppers using instore navigational clickstream. Journal of Consumer Psychology, 13(1-2), 29-39.

Moe, W. W. (2006). An empirical two-stage choice model with varying decision rules applied to internet clickstream data. Journal of Marketing Research, 43(4), 680-692.

Mudambi, S. M., & Schuff, D. (2010). Research note: What makes a helpful online review? A study of customer reviews on Amazon.com. MIS Quarterly, 34(1), 185-200.

Mullainathan, S. (2002). A memory-based model of bounded rationality. The Quarterly Journal of Economics, 117(3), 735-774.

Nedungadi, P. (1990). Recall and consumer consideration sets: Influencing choice without altering brand evaluations. Journal of Consumer Research, 17(3), 263-276.

Nie, C., Zheng, Z. (E.), & Sarkar, S. (2021). A strategic group analysis of competitor behavior in search advertising. Journal of the Association for Information Systems, 22(6), 1659-1685.

The Office of Aviation Consumer Protection. (2021). Air travel consumer report. https://www. transportation.gov/sites/dot.gov/files/2021- 12/November%202021\_ATCR.pdf

Pels, E. (2008). Airline network competition: Full-service airlines, low-cost airlines and long-haul markets. Research in Transportation Economics, 24(1), 68-74.

Peteraf, M. A. (1993). Intra-industry structure and the response toward rivals. Managerial and Decision Economics, 14(6), 519-528.

Porter, M. E. (1979). The structure within industries and companies’ performance. The Review of Economics and Statistics, 61(2), 214-227.

Porter, M. E. (2008). The five competitive forces that shape strategy. Harvard Business Review, 86(1), 78-93.

Sayedi, A., Jerath, K., & Baghaie, M. (2018). Exclusive placement in online advertising. Marketing Science, 37(6), 970-986.

Short, J. C., Ketchen, D. J., Palmer, T. B., & Hult, G. T. M. (2007). Firm, strategic group, and industry influences on performance. Strategic Management Journal, 28(2), 147-167.

Simonov, A., & Hill, S. (2021). Competitive advertising on brand search: Traffic stealing and click quality. Marketing Science, 40(5), 923-945.

Surroca, J., Prior, D., & Giné, J. A. T. (2016). Using panel data dea to measure CEOs’ focus of attention: An application to the study of cognitive group membership and performance. Strategic Management Journal, 37(2), 370-388.

Tae, C. J., Pang, M.-S., & Greenwood, B. N. (2020). When your problem becomes my problem: The impact of airline IT disruptions on on-time performance of competing airlines. Strategic Management Journal, 41(2), 246-266.

Trijp, H. C. M. V., Hoyer, W. D., & Inman, J. J. (1996). Why switch? Product category-level explanations

for true variety-seeking behavior. Journal of Marketing Research, 33(3), 281-292.

Tulving, E., & Schacter, D. L. (1990). Priming and human memory systems. Science, 247(4940), 301-306.

Ursu, R. M., Wang, Q., & Chintagunta, P. K. (2020). Search duration. Marketing Science, 39(5), 849- 871.

Vallaeys, F. (2021). See how losing broad match modified will impact your Google ads. Search Engine Journal. https://www.searchengine journal.com/measure-impact-losing-bmmkeywords/396096

Varian, H. R. (2007). Position auctions. International Journal of Industrial Organization, 25(6), 1163- 1178.

Weber, T. A., & Zheng, Z. (Eric). (2007). A model of search intermediaries and paid referrals. Information Systems Research, 18(4), 414-436.

Wu, J., & Rangaswamy, A. (2003). A fuzzy set model of search and consideration with an application to an online market. Marketing Science, 22(3), 411- 434.

Yang, M., Adomavicius, G., Burtch, G., & Ren, Y. (2018). Mind the gap: Accounting for measurement error and misclassification in variables generated via data mining. Information Systems Research, 29(1), 4-24.

Yang, Y., Zeng, D., Yang, Y., & Zhang, J. (2015). Optimal budget allocation across search advertising markets. INFORMS Journal on Computing, 27(2), 285-300.

Yuan, Y., Wang, F. Y., & Zeng, D. (2017). Competitive analysis of bidding behavior on sponsored search advertising markets. IEEE Transactions on Computational Social Systems, 4(3), 179-190.

Zheng, Z. (Eric), Fader, P., & Padmanabhan, B. (2011). From business intelligence to competitive intelligence: Inferring competitive measures using augmented site-centric data. Information Systems Research, 23(3.1), 698-720.

Zheng, Z. (Eric), Padmanabhan, B., & Kimbrough, S. O. (2003). On the existence and significance of data preprocessing biases in web-usage mining. INFORMS Journal on Computing, 15(2), 148- 170.

Zia, M., & Rao, R. C. (2019). Search advertising: Budget allocation across search engines. Marketing Science, 38(6), 1023-1037.

## Appendix A: Considering Organic Listings

We conducted additional analyses to examine whether the presence of organic listings might have confounded our findings. To rule out such explanations, we considered firms that appeared either as organic listings or in sponsored search results or both when examining the possibility of co-visiting a firm pair (H1) or visiting an undisplayed focal firm (H2). We ranked the sponsored search results from 1 to 11 and the organic listings from 12 to 21 (Google displays 10 firms in the organic listings). Tables A1 and A2 present the results of testing H1 and H2 for both markets. As we can see from these tables, the results are qualitatively unchanged from the main analyses in Tables 4–7.

Table A1. Co-Visit Findings Including Organic Listings

<table><tr><td>Variable</td><td>Air travel</td><td>Air travel with search stage</td><td>Digital camera</td><td>Digital camera with search stage</td></tr><tr><td>Within</td><td>0.599***(0.137)</td><td>0.601***(0.137)</td><td>0.487***(0.102)</td><td>0.487***(0.102)</td></tr><tr><td>Focused</td><td></td><td>0.375***(0.042)</td><td></td><td>0.112(0.090)</td></tr><tr><td>RankDiff</td><td>-0.004*(0.002)</td><td>-0.004*(0.002)</td><td>0.022**(0.010)</td><td>0.022**(0.010)</td></tr><tr><td>Firm FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>AIC</td><td>76,781.171</td><td>76,703.494</td><td>5,160.450</td><td>5,160.843</td></tr><tr><td>Num of obs (N)</td><td>92,017</td><td>92,017</td><td>17,506</td><td>17,506</td></tr><tr><td colspan="5">Note: *** p &lt; 0.01, ** p &lt; 0.05, * p &lt; 0.1. Robust errors in parentheses.</td></tr></table>

Table A2. Priming Results Including Organic Listings

<table><tr><td>Variable</td><td>Air travel</td><td>Air travel with search stage</td><td>Digital camera</td><td>Digital camera with search stage</td></tr><tr><td>Primer</td><td>3.657***(0.317)</td><td>3.656***(0.317)</td><td>0.940*(0.522)</td><td>1.054*(0.544)</td></tr><tr><td>Focused</td><td></td><td>-0.065(0.097)</td><td></td><td>1.145**(0.576)</td></tr><tr><td>PrimerRank</td><td>0.217***(0.020)</td><td>0.217***(0.020)</td><td>0.018(0.013)</td><td>0.019(0.013)</td></tr><tr><td>Firm FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>AIC</td><td>13,976.654</td><td>13,978.218</td><td>5,025.663</td><td>5,103.018</td></tr><tr><td>Num of obs (N)</td><td>12,931</td><td>12,931</td><td>14,518</td><td>14,518</td></tr><tr><td colspan="5">Note: *** p &lt; 0.01, ** p &lt; 0.05, * p &lt; 0.1. Robust errors in parentheses.</td></tr></table>

## Appendix B: Considering One-Hour Matching Period

We further examined whether the results are sensitive to the two-hour cutoff window used to match search results with clickstream sessions. Among the 74,931 matched air travel sessions derived from the two-hour window, we dropped the sessions that were matched with search results but were more than one hour apart. We were left with 51,937 (of the 74,931) unique sessions that were matched. Similarly, 878 of the 1,249 digital camera sessions were matched within an hour.

Table B1. Co-Visit Results: One-Hour Matching Window and Organic Listings

<table><tr><td>Variable</td><td>Air travel</td><td>Air travel with search stage</td><td>Digital camera</td><td>Digital camera with search stage</td></tr><tr><td>Within</td><td>0.456**(0.189)</td><td>0.457**(0.189)</td><td>0.253**(0.104)</td><td>0.254**(0.104)</td></tr><tr><td>Focused</td><td></td><td>0.439***(0.050)</td><td></td><td>0.054(0.105)</td></tr><tr><td>RankDiff</td><td>-0.004(0.003)</td><td>-0.004(0.003)</td><td>0.001(0.010)</td><td>0.001(0.010)</td></tr><tr><td>Firm FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>AIC</td><td>52,780.082</td><td>52,708.516</td><td>4,193.508</td><td>4,195.242</td></tr><tr><td>Num of obs (N)</td><td>63,029</td><td>63,029</td><td>12,254</td><td>12,254</td></tr><tr><td colspan="5">Note: *** p&lt;0.01, ** p&lt;0.05, * p&lt;0.1. Robust errors in parentheses.</td></tr></table>

The results of testing H1 and H2 are reported in Tables B1 and B2, respectively. The results are consistent with our main findings, illustrating their robustness to the choice of cutoff windows used to match the search results with clickstream sessions.

Table B2. Priming Results: One-Hour Matching Window and Organic Listings

<table><tr><td>Variable</td><td>Air travel</td><td>Air travel with search stage</td><td>Digital camera</td><td>Digital camera with search stage</td></tr><tr><td>Primer</td><td>3.323***(0.380)</td><td>3.325***(0.381)</td><td>1.110*(0.673)</td><td>0.940*(0.561)</td></tr><tr><td>Focused</td><td></td><td>-0.159(0.122)</td><td></td><td>1.185(0.723)</td></tr><tr><td>PrimerRank</td><td>0.199***(0.024)</td><td>0.199***(0.024)</td><td>0.026*(0.015)</td><td>0.020(0.016)</td></tr><tr><td>Firm FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>AIC</td><td>9,557.572</td><td>9,557.858</td><td>3,561.548</td><td>3,558.694</td></tr><tr><td>Num of obs (N)</td><td>8,898</td><td>8,898</td><td>10,189</td><td>10,189</td></tr><tr><td colspan="5">Note: *** p&lt;0.01, ** p&lt;0.05, * p&lt;0.1. Robust errors in parentheses.</td></tr></table>

## Appendix C: Considering Firm-Specific Time Fixed Effects

It is possible that consumers might change their browsing behaviors because of marketing campaigns by firms in a strategic group. To account for this, in addition to including two-way fixed effects, we added firm-specific time fixed effects (Firm × Time FE) in this robustness check. The results in Tables C1 and C2 are consistent with the main results for both markets.

Table C1. Co-Visit Results with Firm × Time FE

<table><tr><td>Variable</td><td>Air travel</td><td>Air travelWith organic</td><td>Digitalcamera</td><td>Digital cameraWith organic</td></tr><tr><td>Within</td><td>0.632***(0.145)</td><td>0.625***(0.142)</td><td>0.342**(0.154)</td><td>0.317***(0.108)</td></tr><tr><td>Focused</td><td>0.353***(0.051)</td><td>0.378***(0.042)</td><td>0.168(0.119)</td><td>0.106(0.092)</td></tr><tr><td>RankDiff</td><td>-0.015***(0.006)</td><td>-0.005*(0.003)</td><td>0.046*(0.025)</td><td>0.021*(0.011)</td></tr><tr><td>Firm FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Firm × Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>AIC</td><td>51,586.980</td><td>76,743.967</td><td>2,942.908</td><td>4,988.144</td></tr><tr><td>Num of obs (N)</td><td>54,127</td><td>92,017</td><td>7,066</td><td>16,470</td></tr><tr><td colspan="5">Note: *** p&lt;0.01, ** p&lt;0.05. * p&lt;0.1. Robust errors in parentheses.</td></tr></table>

Table C2. Priming Results with Firm × Time FE

<table><tr><td>Variable</td><td>Air travel</td><td>Air travelWith organic</td><td>Digitalcamera</td><td>Digital cameraWith organic</td></tr><tr><td>Primer</td><td>1.613***(0.129)</td><td>3.732***(0.329)</td><td>0.494**(0.217)</td><td>0.711*(0.430)</td></tr><tr><td>Focused</td><td>-0.067(0.099)</td><td>-0.060(0.098)</td><td>0.234***(0.076)</td><td>0.871(0.616)</td></tr><tr><td>PrimerRank</td><td>0.239***(0.020)</td><td>0.222***(0.020)</td><td>0.003(0.023)</td><td>0.020(0.013)</td></tr><tr><td>Firm FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Firm × Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>AIC</td><td>14,104.336</td><td>14,099.801</td><td>6,632.737</td><td>5,096.786</td></tr><tr><td>Num of obs (N)</td><td>12,939</td><td>12,931</td><td>14,124</td><td>11,683</td></tr><tr><td colspan="5">Note: *** p&lt;0.01, ** p&lt;0.05, * p&lt;0.1. Robust errors in parentheses.</td></tr></table>

## Appendix D: Descriptive Statistics

Table D1. Within and Co-Visit Statistics for the Air Travel Market

<table><tr><td>Variables</td><td>No. of obs.</td></tr><tr><td>Total</td><td>55,475</td></tr><tr><td>Within = 0*</td><td>14,219</td></tr><tr><td>Within = 1</td><td>41,256</td></tr><tr><td>Within = 1 for OTA</td><td>40,915</td></tr><tr><td>Within = 1 for FSC</td><td>0</td></tr><tr><td>Within = 1 for LCC</td><td>341</td></tr><tr><td>Co-Visit = 0</td><td>43,639</td></tr><tr><td>Co-Visit = 0 for across-group pair</td><td>13,169</td></tr><tr><td>Co-Visit = 0 for OTA</td><td>30,144</td></tr><tr><td>Co-Visit = 0 for FSC</td><td>0</td></tr><tr><td>Co-Visit = 0 for LCC</td><td>326</td></tr><tr><td>Co-Visit = 1</td><td>11,836</td></tr><tr><td>Co-Visit = 1 for across-group pair</td><td>1,050</td></tr><tr><td>Co-Visit = 1 for OTA</td><td>10,771</td></tr><tr><td>Co-Visit = 1 for FSC</td><td>0</td></tr><tr><td>Co-Visit = 1 for LCC</td><td>15</td></tr><tr><td colspan="2">*Note: The firms come from different groups in these pairs.</td></tr></table>

Table D2. Primer and VisitFocal Statistics for the Air Travel Market

<table><tr><td>Group</td><td>Total</td><td>Primer = 0</td><td>Primer = 1</td><td>VisitFocal = 0</td><td>VisitFocal = 1</td></tr><tr><td>All groups</td><td>134,559</td><td>79,092</td><td>55,467</td><td>121,842</td><td>12,717</td></tr><tr><td>OTA</td><td>43,027</td><td>0</td><td>43,027</td><td>38,562</td><td>4,465</td></tr><tr><td>FSC</td><td>52,381</td><td>51,184</td><td>1,197</td><td>48,473</td><td>3,908</td></tr><tr><td>LCC</td><td>39,151</td><td>27,908</td><td>11,243</td><td>34,807</td><td>4,344</td></tr></table>

Table D3. Within and Co-Visit Statistics for the Digital Camera Market

<table><tr><td>Variables</td><td>No. of obs.</td></tr><tr><td>Total</td><td>7,614</td></tr><tr><td>Within = 0*</td><td>5,623</td></tr><tr><td>Within = 1</td><td>1,991</td></tr><tr><td>Within = 1 for Group 1</td><td>89</td></tr><tr><td>Within = 1 for Group 2</td><td>57</td></tr><tr><td>Within = 1 for Group 3</td><td>1,393</td></tr><tr><td>Within = 1 for Group 4</td><td>452</td></tr><tr><td>Co-Visit = 0</td><td>7,115</td></tr><tr><td>Co-Visit = 0 for across-group pair</td><td>5,267</td></tr><tr><td>Co-Visit = 0 for Group 1</td><td>55</td></tr><tr><td>Co-Visit = 0 for Group 2</td><td>53</td></tr><tr><td>Co-Visit = 0 for Group 3</td><td>1,292</td></tr><tr><td>Co-Visit = 0 for Group 4</td><td>448</td></tr><tr><td>Co-Visit = 1</td><td>499</td></tr><tr><td>Co-Visit = 1 for across-group pair</td><td>356</td></tr><tr><td>Co-Visit = 1 for Group 1</td><td>34</td></tr><tr><td>Co-Visit = 1 for Group 2</td><td>4</td></tr><tr><td>Co-Visit = 1 for Group 3</td><td>101</td></tr><tr><td>Co-Visit = 1 for Group 4</td><td>4</td></tr><tr><td colspan="2">*Note: The firms come from different groups in these pairs.</td></tr></table>

Table D4. Primer and VisitFocal Statistics for the Digital Camera Market

<table><tr><td>Group</td><td>Total</td><td>Primer = 0</td><td>Primer = 1</td><td>VisitFocal = 0</td><td>VisitFocal = 1</td></tr><tr><td>All groups</td><td>16,873</td><td>2,422</td><td>14,451</td><td>15,848</td><td>1,025</td></tr><tr><td>Group 1</td><td>1,650</td><td>90</td><td>1,560</td><td>1,404</td><td>246</td></tr><tr><td>Group 2</td><td>5,706</td><td>2,212</td><td>3,494</td><td>5,380</td><td>326</td></tr><tr><td>Group 3</td><td>4,228</td><td>8</td><td>4,220</td><td>3,882</td><td>346</td></tr><tr><td>Group 4</td><td>5,289</td><td>112</td><td>5,177</td><td>5,182</td><td>107</td></tr></table>

## About the Authors

Cheng Nie is an assistant professor of information systems and business analytics at the Ivy College of Business at Iowa State University. He received his PhD from the Jindal School of Management, University of Texas at Dallas. His current research interests are in sponsored search, sharing economy, user-generated content, and blockchain.

Zhiqiang (Eric) Zheng is the Ashbel Smith Professor in Information Systems at the Jindal School of Management, University of Texas at Dallas. He received his PhD from the Wharton School of Business. His current research interests focus on fintech, blockchain, and digital asset technologies. He is a senior editor of MIS Quarterly.

Sumit Sarkar is the Charles and Nancy Davidson Chair and Professor of Information Systems in the Naveen Jindal School of Management at the University of Texas at Dallas. He received his PhD from the Simon School of Business at the University of Rochester, his MBA from IIM Calcutta, and his B. Tech from IIT Delhi. His current research interests are in crowdsourcing, machine learning, personalization and recommendation technologies, sponsored search, data privacy, and information quality. He is a Fellow of the Association for Information Systems and a Distinguished Fellow of the Information Systems Society of INFORMS.

Copyright © 2024 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
