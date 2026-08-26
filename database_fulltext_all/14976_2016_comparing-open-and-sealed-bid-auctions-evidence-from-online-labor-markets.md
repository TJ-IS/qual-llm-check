---
otero_id: 14976
otero_key: "JAHPATYW"
title: "Comparing Open and Sealed Bid Auctions: Evidence from Online Labor Markets"
authors: "Yili Hong; Chong (Alex) Wang; Paul A. Pavlou"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0606"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/JAHPATYW/fulltext/images/b35519c478a48401e8185a76de313dba7132b5fabceb21e90f908274963f6e17.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Comparing Open and Sealed Bid Auctions: Evidence from Online Labor Markets

Yili Hong, Chong (Alex) Wang, Paul A. Pavlou

To cite this article:

Yili Hong, Chong (Alex) Wang, Paul A. Pavlou (2016) Comparing Open and Sealed Bid Auctions: Evidence from Online Labor Markets. Information Systems Research 27(1):49-69. http://dx.doi.org/10.1287/isre.2015.0606

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/JAHPATYW/fulltext/images/a315e8a7b7ff99ae004b42430d5279b66cdfdcae9de90a62a91a490398a7301d.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Comparing Open and Sealed Bid Auctions: Evidence from Online Labor Markets

Yili Hong

W. P. Carey School of Business, Arizona State University, Tempe, Arizona 85287, hong@asu.edu

Chong (Alex) Wang

Department of Information Systems, College of Business, City University of Hong Kong, Kowloon, Hong Kong SAR, China, alex.wang@cityu.edu.hk

Paul A. Pavlou

Fox School of Business, Temple University, Philadelphia, Pennsylvania 19122, pavlou@temple.edu

nline labor markets are Web-based platforms that enable buyers to identify and contract for information technology (IT) services with service providers using buyer-determined (BD) auctions. BD auctions in online labor markets either follow an open or a sealed bid format. We compare open and sealed bid auctions in online labor markets to identify which format is superior in terms of obtaining more bids and a higher buyer surplus. Our theoretical analysis suggests that the relative advantage of open versus sealed bid auctions hinges on the role of reducing service providers’ valuation uncertainty (difficulty in assessing the cost to execute a project) and competition uncertainty (difficulty in assessing the intensity of the competition from other service providers), which largely depend on the relative importance of the common value (versus the private value) component of the auctioned IT services, calling for an empirical investigation to compare open and sealed bid auctions. Based on a unique data set of 71,437 open bid auctions and 7,499 sealed bid auctions posted by 21,799 buyers at a leading online labor market, we find that, on average, although sealed bid auctions attract 18.4% more bids, open bid auctions offer buyers \$10.87 higher surplus. Furthermore, open bid auctions are 55.3% more likely to result in a buyer’s selection of a certain service provider and 22.1% more likely to reach a contract (conditional on the buyer’s making a selection) with a provider, and they generate higher buyer satisfaction. In contrast to conventional wisdom that “the more bids the better” and industry practice of treating sealed bid auctions as a premium feature, our results suggest that the buyer surplus gained from the reduction in valuation uncertainty enabled by open bid auctions outweighs the buyer surplus gained from the higher competition uncertainty in sealed bid auctions, which renders open bid auctions a superior auction design in online labor markets.

Keywords: auction format; auction theory; open bids; sealed bids; valuation uncertainty; competition uncertainty; online labor markets; buyer surplus; auction performance

History: Gediminas Adomavicius, Senior Editor; De Liu, Associate Editor. This paper was received on September 30, 2013, and was with the authors 12.5 months for 3 revisions. Published online in Articles in Advance December 15, 2015.

## 1. Introduction

Labor, traditionally supplied primarily off-line, has also moved onto the Internet. Online labor markets, such as Freelancer, oDesk, and Elance, have emerged as a viable means for identifying and sourcing labor (Malone and Laubacher 1998). Nowadays, online labor markets have expanded their reach globally and they attract a large arsenal of professional service providers to offer information technology (IT) services, such as software development (Allon et al. 2012, Cummings et al. 2009, Snir and Hitt 2003). Online labor markets are economically and practically important, and they have been touted for their high transaction volume and societal benefits (Howe 2006). For example, Elance alone has nearly five million jobs posted and has facilitated transactions worth over \$5 billion by August 2014.<sup>1</sup>

Another leading online labor marketplace, Freelancer, has connected over 16 million buyers and service providers from over 200 countries since its inception, and buyers on Freelancer have posted over eight million projects worth over \$10 billion by August 2015.

Online labor markets facilitate buyers to identify and hire labor (service providers) with the use of buyerdetermined (BD) reverse auctions<sup>2</sup> (Asker and Cantillon 2008, Engelbrecht-Wiggans et al. 2007). Typically, in online BD auctions, a buyer who seeks a given service will create a call for bids (CFB) to elicit bids from service providers who offer to execute the project at a certain bid price. Buyers make several decisions when posting CFBs, such as project budget, auction duration, and auction design format. Among different auction design features, bid visibility (open versus sealed bid) is a key design option that has major implications for auction performance in online labor markets. Therefore, this paper seeks to answer the following research question: What are the effects of bid visibility (open versus sealed bid) on auction performance (number of bids and buyer surplus) in online labor markets?

Bid visibility—whether existing bids (bid prices and bidder information) are visible to (open bid) or hidden from (sealed bid) other bidders—shapes the interactions between bidders and buyers (Jap 2002) and among bidders (Milgrom and Weber 1982, Kannan 2012). Bid visibility is a critical design choice for auctions in online labor markets where bidders (service providers) face significant difficulty in assessing the cost to execute a project (termed “valuation uncertainty”) and in assessing the intensity of the competition from other service providers (termed “competition uncertainty”). Depending on the assumption concerning bidders’ valuation for the auctioned item (independent private value versus common value paradigm<sup>3</sup>), formal theoretical discussions make different predictions on which auction format (open versus sealed) results in better auction performance. Under the private value paradigm, the revenue equivalence theorem predicts that both auction formats offer the same level of expected surplus to the auctioneer<sup>4</sup> from the same pool of bidders (Krishna 2009), and such equivalence could break with riskaverse bidders (Holt 1980) or heterogeneous bidder valuation (Athey et al. 2011). By contrast, under the common value paradigm, the linkage principle (Milgrom and Weber 1982),<sup>5</sup> states that surplus to the auctioneer will be higher for open bid auctions by increasing information transparency and allowing bidders to learn from each others’ bids (Krishna 2009, Kagel and Levin 2009). The competing predictions from the private value versus common value auction theories call for an empirical examination to reveal the superior auction design format.

Empirical evidence on the role of bid visibility is limited, partly because “many auction markets operate under a given set of rules rather than experimenting with alternative designs” (Athey et al. 2011, p. 207). Besides, sealed bids in real-life auctions are typically unobservable to researchers. The few existing studies, mostly lab experiments, are inconclusive about whether open bid or sealed bid auctions would result in the higher buyer surplus. Whereas some studies favor sealed bid auctions (e.g., Jap 2007, Athey et al. 2011, Shachat and Wei 2012, Haruvy and Katok 2013), others favor open bid auctions (e.g., Cho et al. 2014, Kagel and Levin 2009, McMillan 1994, Perry and Reny 1999). In sum, these competing empirical findings call for an empirical investigation to reveal the preferred auction format for BD auctions for IT services in online labor markets, an increasingly important context for information systems (IS) research, practice, and society in general.

Besides academic scholars, industry practitioners in online labor markets are also interested in determining the ideal auction format. The current industry practice treats sealed bid format as a premium feature and charges buyers extra fees for using sealed bids.<sup>6</sup> The rationale behind this practice is that sealed bid BD auctions may attract more bids, which offer buyers higher diversity and presumably quality. This intuition is based on the untested assumption that “the more bids, the better.” However, it is not clear whether open versus sealed bid BD auctions actually perform better in practice in online labor markets.

Our empirical study is based on a unique proprietary panel data set obtained from a leading global online labor market with 71,437 open bid BD auctions and 7,499 sealed bid BD auctions posted by 21,799 unique buyers. This online labor market allows CFBs to be auctioned in either an open bid or a sealed bid BD format, hence enabling a within-site comparison between these auction formats. Our data cover the bidding history of projects posted between August 2009 and February 2010, which includes proprietary data of sealed bid BD auctions that are visible to the buyer (auctioneer), yet hidden from other bidders and from the public. Seeking to establish a causal inference of the effect of bid visibility (open bid versus sealed bid) on key auction performance outcomes (number of bids and buyer surplus), in addition to buyer-level fixed effects (FE) analysis, we performed propensity score matching and instrumental variable analyses. Although the intuition of industry practice is empirically verified that sealed bid auctions do attract more bids, we empirically show that open bid auctions may be a superior format in online labor markets because open bid auctions empirically render a higher buyer surplus. More importantly, we quantify the economic effects of auction format on these two auction performance outcomes. Sealed bid BD auctions do attract at least 18.4% more bids compared with open bid BD auctions. However, open bid BD auctions generate at least \$10.87 higher buyer surplus, they are 55.3% more likely to result in buyer selection, they are 22.1% more likely to reach a contract (conditional on the buyer making a selection), plus they generate higher buyer satisfaction.

To our knowledge, this is the first large-scale empirical study to examine the effect of bid visibility on auction performance by using data from an online labor market, extending our understanding of the effects of bid visibility as an auction design (Krishna 2009, Athey et al. 2011, Haruvy and Katok 2013, Cho et al. 2014). This study also adds to the emerging literature on online labor markets (Snir and Hitt 2003, Allon et al. 2012, Yoganarasimhan 2013) and offers actionable guidelines to the major stakeholders in online labor markets. The study also contributes to the broader literature on auctions in the IS literature (e.g., Ba and Pavlou 2002).

This paper proceeds as follows. Section 2 describes the background, related literature, and the context of our study. Section 3 presents the theoretical analysis, which sets the foundations for our empirical testing. Section 4 presents the data, estimation models, key findings and results, and robustness checks. Finally, §5 discusses this study’s contributions and implications for theory and practice.

## 2. Background and Related Literature

## 2.1. Research Context—Online Labor Markets

Online labor markets are Web-based platforms that connect buyers who need IT services (for example, software development) to professional service providers who possess the skills to fulfill these IT services. Many online labor markets have emerged, such as Freelancer, oDesk, and Elance, and they have attracted millions of skilled service providers from all over the globe, who actively bid on projects to win contracts.

Online labor markets have attracted considerable interest. One stream of research focuses on buyers’ hiring decisions. The past performance of service providers, such as their reputation, affects their probability of being hired in the future (e.g., Banker and Hwang 2008, Moreno and Terwiesch 2014, Pallais 2014). Yoganarasimhan (2013) estimated the return of reputation in online labor markets and found that buyers are forward looking and primarily focus on reputation (as quality signals) when selecting service providers. Besides reputation, it was also found that buyers prefer service providers with whom they have had prior interactions (Gefen and Carmel 2008) and whose work experience is independently verified by third parties (Agrawal et al. 2013). Service providers are thus motivated to seek third-party certifications (Goes and Lin 2012). Another stream of research examined bidders’ behavior in online labor markets. Snir and Hitt (2003) showed that with a nonnegligible bidding cost for service providers, low-quality service providers are more likely to bid on higher-value projects. They showed that higher-value projects attract significantly more bids but of lower quality, making online labor markets unsuitable for large projects. Carr (2003) modeled the role of bid evaluation cost on the equilibrium bidding strategy and argued that buyers may disregard promising bids simply because they could not evaluate all bids. In summary, the literature on online labor markets has focused on buyer’s bid evaluation and hiring decisions and on the bidding behavior of service providers.

To post a project in online labor markets, buyers can choose between two forms of BD auctions, namely, open bid and sealed bid. Auctions that follow the open bid format prominently show the average bidding price and number of existing bids, and they allow service providers to observe detailed competing bids and the bidders’ profiles. By contrast, sealed bid auctions only reveal information on number of bids, but they do not provide information on the average bid price, competing bids, or the bidders’ profiles. Figure 1 shows an example project page and information observable to bidders (and the public) under the two auction formats. Please refer to Online Appendix I (available as supplemental material at http://dx.doi.org/10.1287/ isre.2015.0606) for more details of the focal reverse BD auctions mechanism.

## 2.2. The Auctions Literature

Auction is an important topic that has been studied extensively in multiple disciplines, such as economics, IS, operations research, and marketing. The seminal works of Krishna (2009), Milgrom (2004), and Klemperer (2002) offer systematic reviews of previous work. Recently, researchers have been focusing on auctions on the Internet platforms that facilitate price discovery in various e-commerce contexts, including ordinary forward auctions such as eBay (e.g., Bajari and Hortaçsu 2004, Bapna et al. 2008), keyword auctions such as Google AdWords (e.g., Chen et al. 2009, Liu and Chen 2006, Liu et al. 2010), and combinatorial auctions (e.g., Adomavicius et al. 2012, 2013). In summary, there is an emerging interest in the auction mechanism design, bidding behaviors, and buyer surplus in online auctions (e.g., Bapna et al. 2010, Goes et al. 2010, Mithas and Jones 2007, Xu et al. 2011, Zhang and Feng 2011).

Recently, online reverse BD auctions emerged as a common auction design in online labor markets.

## Figure 1 Open vs. Sealed Auction Format on Freelancer

![](/api/attachments/JAHPATYW/fulltext/images/0dd6e44035c3387fb7b362d91f30a18d3c4926612c5bba0b593753c920e17e22.jpg)  
(a) Open biD auctions  
(b) Sealed biD auctions

Because of their popularity and practical importance, online BD auctions are attracting increased attention from researchers (e.g., Allon et al. 2012, Snir and Hitt 2003, Yoganarasimhan 2013). Compared with physical auctions, instead of simultaneous face-to-face bidding in a single auction, service providers in online BD auctions use a computer-mediated interface to explore CFBs, to submit and modify bids, and to observe the information of other bidders (in the case of open bid BD auctions). Also, given the global reach of online auctions, the bidder pool is significantly larger than in traditional auctions (Carr 2003).

## 2.3. Review of the Auction Literature on Bid Visibility

2.3.1. Theoretical Work. A major stream of the theoretical work in the auction literature centers on the optimality of auction format (open versus sealed bid) in different auction paradigms (independent private value versus common value), that is, comparisons between different auction formats in terms of bidding behavior and buyer surplus (e.g., Arora et al. 2007, Greenwald et al. 2010, Kannan 2012). Under the independent private value paradigm, the seminal revenue equivalence theorem states that the expected revenues from first-price (or second-price) sealed bid and open bid auctions are identical (Vickrey 1961). Much theoretical discussion has focused on extending the (in)equivalence under different model settings by relaxing assumptions such as risk preference (Harris

## Website Development

![](/api/attachments/JAHPATYW/fulltext/images/77c2e8c4dc67695d20d276322f413d7a71c0c491432392a075f276ee7d1d03f7.jpg)

I would like you to email me if your are interested and I can send you my sketches, flow chart. specifications, and what functionality I need. Then if you could send me a guote on how much you would charge me. I would also need information on how much it would cost to edit the sight in the future. As I expand I will need more pages developed and more edits made on a more frequent basis. Because of this I would also be interested in forming a partnership and bringing you on board with the company. If you are interested in strictly being paid for the job then I would need to know how much it would cost to make edits and such.

Also please send some examples of your previsou work otherwise you will not be considered

and Raviv 1981, Matthews 1987), information on the number of bidders (Harstad et al. 1990, McAfee and McMillan 1987), and bidding costs (Daniel and Hirshleifer 1998, Samuelson 1985). Revenue equivalence is proved to be robust under some of these cases (e.g., Krishna 2009, Maskin and Riley 2000), and a general theoretical prediction in independent private value auctions is that the expected revenue is higher in sealed bid auctions (versus open bid auctions) if bidders are risk averse (e.g., Holt 1980, Maskin and Riley 1984).

By contrast, in common value auctions, a different theoretical prediction was made. Theoretical analyses of common value auctions suggested that a higher surplus can be achieved by providing more information to relieve bidders’ discovery cost of the auctioned item’s value (Krishna 2009), which was shown by Kagel and Levin (1986) in a Nash Equilibrium model. The theoretical finding that open bid auctions generally lead to higher expected revenues for the auctioneers is termed the “linkage principle,” and one main explanation for the inequality is that bidders reduce valuation uncertainty about the auctioned item with information from other bidders (Milgrom and Weber 1982). Hausch and Li (1993) used a stylized model to illustrate that the selling price in a common value auction is the expected value of the auctioned item minus aggregate entry and the bidders’ cost to acquire information. Furthermore, based on numerical simulations in the common-value second-price auction model, Yin (2006) established that bidders’ uncertainty about the common value significantly decreases their bid prices. In sum, the theoretical literature on common value auctions generally suggests the superiority of open bid auctions (compared with sealed bid auctions).

Taken together, depending on the auction paradigm (independent private value versus common value), the literature has reported competing theoretical findings on the superiority of open versus sealed bid auctions.

2.3.2. Empirical Work. Formal theoretical predictions concerning the optimality of auction format (bid visibility) depend on model assumptions and often fail to fully capture the complexity of real-life auctions. Research efforts have thus been devoted to establish their empirical validity mostly using lab experiments and field observations.

With lab experiments, researchers are able to create a private or a common value auction environment. In a private value paradigm, the majority of the evidence from lab experiments points to the conclusion that higher information transparency leads to a lower surplus for auctioneers. Elmaghraby et al. (2012) found that, in procurement auctions, contrary to the predictions of game theory, rank feedback would lead to lower average prices than full-price feedback because of bidders’ impatience, suggesting a higher buyer surplus for auctions with lower information transparency. Similarly, Shachat and Wei (2012) found that the mean and variance of prices in a first-price sealed bid auction was lower than in an English auction<sup>7</sup> for the procurement of commodities, also suggesting a higher surplus for sealed bid auctions. Haruvy and Katok (2013) compared open and sealed bid auctions with different information structures, and, again, they found that sealed bid auctions provided a greater buyer surplus.<sup>8</sup> Following the common value paradigm, experimental work comparing open and sealed bid auctions mostly focused on the “winner’s curse.” It was shown that better-informed bidders are capable of achieving a higher rate of return than less-informed bidders, and public information induces bidders (a common value assumption) to revise their bids upward in a first-price forward auction (Kagel and Levin 1999), although overbidding and winner’s curse persist despite a different number of bidders (Dyer et al. 1989). Related to our work, Goeree and Offerman (2002) showed that in first-price auctions with both private and common value components, low uncertainty about the common value and increased competition raise auction revenues.

Empirical comparisons between open and sealed bid auctions using observational data are limited. Since researchers have little control over the research context, these studies largely focus on finding the most compelling theoretical mechanism of a specific market. For example, in the context of high-value timber auctions with relatively few bidders, Athey et al. (2011) found that sealed bid auctions offer a higher surplus than open bid auctions due to the potential of “bidder collusion” in open bid auctions. Cho et al. (2014) argued that used car auctions have a common value component due to quality uncertainty. They showed that average revenues were significantly higher under an English auction than under a dynamic Internet auction format that revealed less information to bidders. In the context of online procurement auctions, Millet et al. (2004) did not assume any auction paradigm; still, they empirically demonstrated the benefits of information transparency to auctioneers with data from over 14,000 auctions, revealing that both the lowest bid and bid rank of the bidders can yield greater savings than revealing either the low bid only or the rank bid only.

In summary, empirical evidence on the effect of bid visibility on the revenue (or surplus) of the auctioneer is inconclusive, and the superiority of the auction format (open versus sealed bid auctions) largely depends on the experimental setting or particular empirical context.

## 3. Theory

We theorize the effects of bid visibility on (1) the number of bids and (2) buyer surplus in BD auctions in online labor markets.<sup>9</sup> Below, we first discuss the key features of BD auctions in online labor markets: (a) IT services are proposed to have both an independent private value and a common value component, and (b) service providers face valuation uncertainty and competition uncertainty in online BD auctions.

Online labor markets facilitate the transaction of IT services, such as software development and graphical design. Compared with commodities, IT services are idiosyncratic, complex (Snir and Hitt 2003), and highly variable in their quality (Rust et al. 1999). Unlike commodities that can be easily contracted on product descriptions and warranties, IT services have many complex components that cannot be perfectly described or contracted, making it difficult for service providers to estimate the exact cost of providing the IT service based on the ex ante service requirements (Willcocks et al. 2002). This introduces a “common value” component to the valuation of the IT service (Bajari and Hortaçsu 2004). Thus, on one hand, service providers have private knowledge about their own capabilities and outside options that are independent of other service providers (termed the “private value” component). On the other hand, some costs (such as communication, coordination, requirement specificity, and project complexity) that are common to all service providers are hard to be fully evaluated up front<sup>10</sup> (the “common value” component). In summary, instead of treating IT services as either having a private value or a common value, we adopt the approach of Goeree and Offerman (2003, p. 598), and we treat the cost evaluation of IT services in online labor markets as “not exclusively common value or private value,” but a combination of both.

Service providers who bid for projects for IT services in BD auctions face two types of uncertainty,<sup>11</sup> valuation uncertainty and competition uncertainty. Specifically, valuation uncertainty refers to the difficulty to assess the cost to execute the project;<sup>12</sup> competition uncertainty refers to the difficulty to assess the intensity of the competition from other service providers. First, the relative importance between the private value component and the common value component has implications for whether bid visibility reduces bidders’ valuation uncertainty. For the private value component, each bidder has a privately observed signal of the value of the auction good, which is independent of the assessment of other bidders (Goeree and Offerman 2003, Krishna 2009). Thus, for the private value component, information from other bidders enabled by open bid auctions does not alleviate valuation uncertainty. By contrast, albeit the common value component is the same to all bidders, no bidder knows the true valuation of this common value, but each bidder has private information about the true valuation (e.g., Kagel and Levin 2009, Krishna 2009). For the common value component, information from other bidders in open bid auctions helps reduce valuation uncertainty. Second, in terms of competition uncertainty, because in open bid (versus sealed bid)

auctions bidders could observe the bids and profiles of other bidders, competition uncertainty is always lower, irrespective of the relative importance of the private or the common value component.

In summary, whether and to what extent bid visibility (open versus sealed bid auctions) reduces bidders’ valuation uncertainty depends on the relative importance of the common (versus private) value component; however, competition uncertainty is reduced in open bid auctions irrespective of the relative importance of the private value versus the common value component. This premise guides our theoretical logic below.

## 3.1. Bid Visibility and Number of Bids

Buyers in online labor markets prefer to solicit more bids from multiple service providers to expand their consideration set, ceteris paribus. Therefore, the total number of bids represents the set of service providers that a buyer could choose from, and given the variety and diversity of options for service providers, this has been proposed as one measure of auction performance (e.g., Terwiesch and Xu 2008, Yang et al. 2009).

In online BD auctions, making bids visible reduces valuation uncertainty (for the common value component). Reduction in valuation uncertainty increases prospective service providers’ expected value and encourages them to submit bids. Meanwhile, the information transparency afforded by open bid (versus sealed bid) auctions reveals the sequential and competitive bidding process to prospective service providers, thereby reducing overall competition uncertainty (e.g., Bajari and Hortaçsu 2003, Gallien and Gupta 2007, Vakrat and Seidmann 2000). By revealing the competition to prospective service providers, reduction in competition uncertainty creates a natural screening effect in open bid auctions. Simply put, bidders in open bid auctions observe all existing bids, which is likely to prevent bidders with a lower surplus provision from bidding in the presence of more competitive bids, especially given nonnegligible bidding costs (Snir and Hitt 2003). By contrast, in sealed bid auctions, service providers cannot view existing bids, and thus all bidders who ex ante are attracted to the auction are likely to place their bids. Therefore, open bid auctions may attract a smaller number of bids compared to sealed bid auctions because of the screening effect that discourages less competitive service providers from placing bids.

Taken together, although the reduction in valuation uncertainty from the information transparency of open bid auctions encourages higher participation, revealing the competing bids discourages (weak) service providers from placing bids, making it theoretically difficult to unequivocally predict whether open versus sealed bid auctions would result in a higher number of bids. Accordingly, we do not make a theoretical prediction nor pose a formal hypothesis, and we seek to empirically examine the effect of bid visibility (open versus sealed) on the number of bids in the context of online labor markets.

Table 1 Comparisons Between Open and Sealed Bid Auctions on Buyer Surplus

<table><tr><td></td><td>Open bid auctions</td><td>Sealed bid auctions</td><td>Effect on buyer surplus</td></tr><tr><td>Valuation uncertainty</td><td>Low(if a common value component exists)</td><td>High</td><td>Valuation uncertainty induces service provider&#x27;s fear of winning at a suboptimal price and results in overbidding, leading to a lower buyer surplus.</td></tr><tr><td>Competition uncertainty</td><td>Low</td><td>High</td><td>Competition uncertainty encourages risk-averse service providers to bid lower to enhance winning probability, leading to a higher buyer surplus.</td></tr></table>

## 3.2. Bid Visibility and Buyer Surplus

Although buyers seek to increase the number of bids they receive, the ultimate goal is to contract with a bidder who offers a high surplus. Given the large number of service providers in online labor markets (Carr 2003), achieving a higher buyer surplus is more important than generating a large number of bids. This ability becomes particularly critical when a large number of bids could be costly to buyers because of high bid evaluation costs (Carr 2003). Furthermore, buyer surplus is a fundamental performance measure in the auction literature, whereas the number of bids has received less attention. Therefore, we focus on theorizing how bid visibility (open versus sealed bid) would offer buyers a higher surplus. The key arguments we propose are summarized in Table 1, and they are explained in detail below.

BD auctions in online labor markets create significant valuation uncertainty of IT services for bidders, who fear “winning at a suboptimal price” (also known as the “winner’s curse”; Milgrom and Weber 1982, Athey and Haile 2002, Bajari and Hortaçsu 2003, Kagel and Levin 2009). Hence, if a service provider is not certain about the cost of offering a complex IT service (e.g., developing a customized software), he is unlikely to bid aggressively to win because of the fear of bidding lower than his actual cost to execute the project, particularly if service providers are risk averse. However, buyers can help alleviate the valuation uncertainty that service providers face. As Hausch and Li (1993) shows, when no information is given to bidders on the auctioned item valuation (for sealed bid auctions), the auctioneer indirectly pays for the bidders’ cost to acquire information<sup>13</sup> on the auctioned item’s value, which would be reflected in the (higher) bid prices.

In open bid auctions (compared with sealed bid auctions), although the cost of assessing the private value component could not be reduced by information from other bidders, such information can help service providers assess the cost of the common value component.<sup>14</sup> Notably, the average bid price is prominently shown on the bidding page (Figure 1). It has been shown, both theoretically (Goeree and Offerman 2003) and experimentally (Goeree and Offerman 2002), that when the auctioned item has a common value component (which we assume true for IT services, as explained above), buyer surplus may be higher when information about the common value is publicly available, consistent with the prediction of the “linkage principle” (Milgrom and Weber 1982). In sum, in open bid auctions, service providers can learn from others’ bids, which helps them to reduce their valuation uncertainty of the common value component, which in turn reduces their valuation discovery cost and allows them to bid lower, thus offering a higher surplus to the buyer (e.g., Milgrom and Weber 1982, Cramton 1998, Kagel and Levin 2009, Krishna 2009). Accordingly, the effect of bid visibility (open bid auctions versus sealed bid auctions) on buyer surplus is expected to be higher if there is a more substantial common value component in IT services.

In online labor markets, a large number of service providers randomly enter an auction to compete to offer IT services. Service providers face competition uncertainty, irrespective of the importance of the private value or the common value component. Risk-averse bidders seek to mitigate competition uncertainty through more aggressive bidding (Holt 1980). In other words, a risk-averse bidder in a reverse auction would prefer to win with a higher probability by sacrificing some profit margin (e.g., Maskin and Riley 1984, Menicucci 2004). Relative to sealed bid auctions, open bid auctions have lower competition uncertainty, ceteris paribus. Hence, service providers in open bid auctions are more certain about the intensity of competition they face because they can readily observe existing bids, the average bidding price, and other bidders’ profiles, especially since they can keep updating their bids as new bids arrive. With reduced competition uncertainty, risk-averse service providers no longer need to lower their bids to improve their chances of winning. Hence, the lower competition uncertainty in open bid auctions is expected to reduce buyer surplus, particularly if we assume that service providers are risk averse (which is a very common assumption in the auctions literature).

In sum, the literature offers competing theoretical predictions on the effect of bid visibility on buyer surplus, and the net effect of bid visibility on buyer surplus depends on the relative importance of the common value (versus the private value) component. If the private value component is substantial for IT services, reduction in valuation uncertainty would be small, whereas the reduction in competition uncertainty would dominate, and buyer surplus would be lower in open bid auctions versus sealed bid auctions. By contrast, if the common value component dominates, the reduction in valuation uncertainty would be substantial and would dominate the reduction in competition uncertainty; thus buyer surplus would be higher in open bid versus sealed bid auctions.

Based on the theoretical discussion, it is difficult to unequivocally determine the superior auction format. Therefore, we do not pose a formal hypothesis on whether open or sealed bid auctions would result in higher buyer surplus, but we seek to empirically assess the preferred auction format by examining the importance of the common value versus the private value components in the context of online BD auctions for IT services. While valuation uncertainty and competition uncertainty are proposed as our main theoretical underpinnings, one caveat in our theoretical analysis is that because of the complexity in real-life online BD auctions, there may be alternative theoretical explanations as to whether open or sealed bid BD auctions produce a higher surplus, such as endogenous entry of heterogeneous bidders and bidder collusion across these two auction formats. We discuss and empirically assess these alternative explanations subsequently after reporting the main results.

## 4. Empirical Methodology

In this section, we first describe the data used in the empirical analysis and introduce the model and identification strategy. Then, we examine the effects of bid visibility (open versus sealed bid BD auctions) on (1) the number of bids an auction receives and (2) the buyer surplus, as we elaborate in detail below.

## 4.1. Data and Variables

Our data include bid-level observations from a proprietary database of a leading online labor market.<sup>15</sup> Our main analysis is carried out at the project (auction) level with data between August 2009 and February 2010. The data set contains 71,503 open bid auctions and 7,433 sealed bid auctions posted by 21,799 unique buyers. We focus on four major project categories, software development, graphic design, content writing, and data coding, which account for more than 90% of all of the projects in the marketplace.<sup>16</sup> For each project, we obtained data on buyer characteristics (e.g., project experience, gold membership, and location and IP addresses), project characteristics (e.g., project budget and project category), auction characteristics (e.g., duration and format), auction outcomes (e.g., number of bids, average bid price, selected bid), and project outcome (e.g., bidder selection, contract and postproject satisfaction). We also obtained bid- and bidder-related data. Observations of auctions and bids were time stamped. To control for heterogeneity in purchasing power across countries, we obtained additional data about the purchasing power parity (PPP)-adjusted gross domestic product (GDP) per capita for all countries (GDP\_PPP) combining data sources from the CIA World Factbook.<sup>17</sup> We merged GDP\_PPP data with the main transaction data by the buyers’ country of residency based on users’ self-reported billing addresses when they signed up for the online labor market platform. Finally, to check the accuracy of the reported country of residence, we also recovered the buyers’ locations (country) using their login IP addresses,<sup>18</sup> and the results are virtually identical.

Table 2 summarizes the definition and descriptive statistics of key variables (project-level data). The correlation matrix is reported in Online Appendix II. On average, projects in our sample received about 14 bids. About 10% of the auctions in our sample were carried out using the sealed bid auction format. The average length of auction periods was about 11 days. Buyers in our sample completed an average of 18.5 projects before the focal project, and 29% of the buyers held a platform gold membership at the time of posting.

Table 2 Definition and Summary Statistics of Key Variables (Project-Level Data)

<table><tr><td>Variable</td><td>Variable definition</td><td>Mean</td><td>SD</td><td>Min.</td><td>Max.</td><td>Median</td></tr><tr><td>Num Bids</td><td>Total number of bids received in an auction</td><td>13.6</td><td>14.8</td><td>1</td><td>89</td><td>9</td></tr><tr><td>Buyer Surplus (Max.)</td><td>Buyer budget upper bound minus selected bid price</td><td>194.6</td><td>111.3</td><td>-1,000</td><td>725</td><td>202</td></tr><tr><td>Buyer Surplus (Avg.)</td><td>Buyer budget upper bound minus average bid price</td><td>171.15</td><td>132.72</td><td>-1,250</td><td>650</td><td>180.7</td></tr><tr><td>Buyer Surplus (Est.)</td><td>Estimated buyer surplus based on discrete choice model</td><td>783.11</td><td>523.23</td><td>-2,474</td><td>2,497</td><td>789.5</td></tr><tr><td>Selected Bid</td><td>Selected bid&#x27;s price in an auction</td><td>127.35</td><td>151.85</td><td>20</td><td>1,500</td><td>60</td></tr><tr><td>Selected</td><td>Whether the buyer selected any provider</td><td>0.67</td><td>0.47</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Contracted</td><td>Whether a contract is reached</td><td>0.60</td><td>0.49</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Satisfaction</td><td>The satisfaction rating a buyer gives to a provider</td><td>9.87</td><td>0.77</td><td>1</td><td>10</td><td>9</td></tr><tr><td>Open Bid</td><td>Whether the project was posted as an open auction</td><td>0.90</td><td>0.29</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Buyer GDP_PPP</td><td>Buyer&#x27;s purchasing power parity adjusted GDP per capita</td><td>33,718</td><td>16,169</td><td>370</td><td>78,409</td><td>38,663</td></tr><tr><td colspan="7">Control variables</td></tr><tr><td>Project Max Budget</td><td>The upper bound of the buyer&#x27;s budget</td><td>347</td><td>197</td><td>250</td><td>750</td><td>250</td></tr><tr><td>Auction Duration</td><td>Number of days an auction was active</td><td>10.58</td><td>15.85</td><td>1</td><td>60</td><td>5</td></tr><tr><td>Buyer Experience</td><td>Number of projects the buyer has contracted</td><td>18.54</td><td>64.21</td><td>0</td><td>1,179</td><td>3</td></tr><tr><td>Buyer Goldmember</td><td>The buyer was a gold member or not at time of an auction</td><td>0.29</td><td>0.45</td><td>0</td><td>1</td><td>0</td></tr><tr><td colspan="7">Project categories</td></tr><tr><td>PC1</td><td>Website and software development</td><td>0.47</td><td>0.50</td><td>0</td><td>1</td><td>0</td></tr><tr><td>PC2</td><td>Writing and content</td><td>0.19</td><td>0.40</td><td>0</td><td>1</td><td>0</td></tr><tr><td>PC3</td><td>Graphical design</td><td>0.24</td><td>0.43</td><td>0</td><td>1</td><td>0</td></tr><tr><td>PC4</td><td>Data entry and management</td><td>0.10</td><td>0.30</td><td>0</td><td>1</td><td>0</td></tr></table>

## 4.2. Empirical Models and Econometric Identification

4.2.1. Empirical Models. Equations (1) and (2) outline our empirical models for estimating the effect of auction format on the number of bids received in an auction and the buyer surplus generated. In other models, the effect of auction format is captured by the variable Open Bid (equal to 0 if the auction is sealed bid and 1 if the auction is open bid). Our observation is at the project level (indexed by i5. For ease of reference, we indexed the buyer of the project by u and the time of posting by t. In both equations, we controlled for observed project and auction characteristics, including project budget and auction duration; time-variant buyer characteristics, including project experience and gold membership; year-month dummies 4ym 5; and project category dummies (Category 5. To control for the unobserved buyer characteristics, we added buyer fixed effects ( 5 to the model. To address nonnormality in the variables, we took natural logarithm of the highly skewed variables (Num Bids, Auction Duration, and Buyer Experience) in the estimation<sup>19</sup>

$$
\begin{array}{l} \ln (N u m B i d s) _ {i, u, t} \\ = \beta_ {0} + \beta_ {1} \times O p e n B i d _ {i} + \beta_ {2 - 3} \times (A u c t i o n C o n t r o l s _ {i}) \\ \quad + \beta_ {4 - 5} \times (B u y e r C o n t r o l s _ {u, t}) + \delta_ {u} + y m _ {t} \\ \quad + C a t e g o r y _ {i} + \varepsilon_ {i, u, t} \end{array}\tag{1}
$$

$$
\begin{array}{l} \text {Buyer Surplus} _ {i, u, t} \\ = \beta_ {0} + \beta_ {1} \times \text {Open Bid} _ {i} + \beta_ {2 - 3} \times (\text {AuctionControls} _ {i}) \\ \quad + \beta_ {4 - 5} \times (\text {BuyerControls} _ {u, t}) + \delta_ {u} + y m _ {t} \\ \quad + \text {Category} _ {i} + \varepsilon_ {i, u, t}. \end{array}\tag{2}
$$

Note that in the instrumental variable (IV) estimation with GDP\_PPP as the IV, buyer fixed effects were not included because there is no variation within a buyer with respect to GDP\_PPP.

Buyer surplus is defined as the difference between a buyer’s willingness to pay (WTP) and the actual price paid for the IT service. Whereas we can observe the price bids, the buyer’s WTP cannot be observed. Following prior work (e.g., Bapna et al. 2008, Mithas and Jones 2007), we used the posted project budget as a proxy for the buyer’s WTP. In online labor markets, buyers are required to specify their estimated budget range with a maximum and a minimum value when posting projects. Buyers are motivated to reveal their true budget since they want to inform potential bidders to get more meaningful bids (Hong and Pavlou 2012). In the main analysis, we used maximum budget as a proxy for WTP and measured buyer surplus as Max\_Budget − Selected\_Bid (Buyer Surplus (Max.)). To check the robustness of the results, we included two alternative measures of buyer surplus: (1) the difference between the maximum budget and the average price of all bids in an auction (Buyer Surplus (Avg.)) and (2) an estimated buyer surplus (Buyer Surplus (Est.)) based on a discrete choice framework (Online Appendix IV). Overall, our results are similar, indicating that our estimation results are robust to alternative surplus measures.

4.2.2. Econometric Identification Strategies. A major challenge to identify the effect of auction format (Open Bid 5 from our observational data is that it is the buyer who decides whether to use sealed bid auction or open bid auction when the project is created. As a result, the coefficient we estimated from the model could be biased by the endogenous selection of the auction format. Selection bias could result from unobserved buyer and project characteristics. The budget estimation strategy could also affect the choice of auction format, which may render the auction format endogenous in Equation (2). To strengthen our empirical identification, besides auction-level and buyer-level time variant control variables, we included three sets of fixed effects to control for unobserved heterogeneity—buyer fixed effects (using within transformation), monthly dummies, and project-category dummies. The buyer fixed effects model helps us to alleviate the concern caused by unobserved time-invariant buyer characteristics and temporal and category differences. A similar approach was adopted by Cho et al. (2014), who compared among different auction formats with observational data. To further strengthen the causal interpretation for the estimated effects of auction format in Equations (1) and (2), we considered two alternative identification strategies—propensity score matching (PSM), and IV approaches.

Matching estimators are commonly used to address self-selection issues by creating a quasi-experimental condition for identification purposes (Abadie and Imbens 2006, Rosenbaum and Rubin 1983). The basic idea of the matching estimator is to create a sample of the control group (in our context, sealed bid BD auctions) that is statistically equivalent to the treatment group (i.e., open bid BD auctions) in all relevant observed (static and dynamic) characteristics. In the basic PSM estimation, we first estimated the propensity of each observation to receive the treatment (to be conducted in an open bid format) using the observed (matching) variables. We then matched each treated observation (open bid auctions) with an observation from the untreated group (sealed bid auctions) with a similar propensity score. PSM estimates the average treatment effect on the treated based on a comparison to the matched control group. Estimates from the PSM method are more precise than regression estimates in finite samples (Angrist and Pischke 2008). PSM is often used to address selection issues in observational studies with archival data (Aral et al. 2009, Oestreicher-Singer and Zalmanson 2013, Rishika et al. 2013). It was also used in the estimation of the effect of bid visibility in U.S. timber auctions (Athey et al. 2011). PSM is useful in our context because of the richness of the observed characteristics at the project level, which is preferable for creating matching groups using propensity scores.

Another strategy commonly adopted to tackle endogeneity is the IV approach. A valid instrument should be correlated with the potentially endogenous independent variable (in our case, auction format), but it should not relate to the dependent variable besides through the endogenous variables. Based on this rationale, we conducted an IV analysis with GDP\_PPP (purchasing power parity-adjusted GDP per capita) of the buyer’s country of residence as an IV. Purchasing power parity-adjusted GDP per capita is a key economic measure for the relative value of per capita income and often used as a proxy for the “wealth” of a country’s average resident (e.g., Gefen and Carmel 2008, Lee and Tang 2000, Lothian and Taylor 1996) The detailed rationale for using GDP\_PPP as the IV is provided as follows. In the online labor market that we study, open bid auctions are the default option when posting a project. To use sealed bid auctions, which are a premium feature, buyers need to pay an extra fee for posting (\$1 per project in the time window of our main analysis). Although the same nominal cost is incurred for all buyers, the real cost of posting a sealed bid auction, and perhaps the psychological perception of \$1, depends on the buyer’s residing country (more specifically, the purchasing power of the buyer). As such, we expect that, everything else equal, buyers from a wealthier country (with higher GDP\_PPP) would be more likely to use sealed bid auctions. Besides its effect on the use of sealed bid auction format, there is no plausible rationale for GDP\_PPP to affect auction performance since this information is not shown in any salient manner to potential service providers, and GDP\_PPP should thus have little or no impact on service providers’ bidding strategy. Results for these additional robustness checks are reported after we discuss the findings from our main analysis in §5.

## 5. Analyses and Results

## 5.1. Main Analysis

Table 3 reports the regression analysis results with buyer fixed effects (columns (2) and (4)). For comparison, we also report the results from the ordinary least squares (OLS) analysis without buyer fixed effects (columns (1) and (3)). Based on our fixed effects estimation, open bid auctions attract, on average, 22.1% fewer bids (p < 0001) than sealed bid auctions (column (2) in Table 3; the number is 18.4% according to the estimates without buyer fixed effects). Besides, according to column (4) in Table 3, buyers in open bid BD auctions enjoy \$15.76 higher surplus (p < 0001) than buyers in sealed bid BD auctions (the number is \$10.87 according to the estimates without buyer fixed effects).<sup>20</sup> Overall,

<sup>∗∗∗</sup>p < 0001.

<sup>∗∗∗</sup>p < 0001.

Table 3 Effect of Bid Visibility on Auction Outcomes (OLS and FE)

<table><tr><td rowspan="2">DV</td><td colspan="2">In (Num Bids)</td><td colspan="2">Buyer Surplus (Max)</td></tr><tr><td>(1) OLS</td><td>(2) FE</td><td>(3) OLS</td><td>(4) FE</td></tr><tr><td>Open Bid</td><td>-0.184*** (0.013)</td><td>-0.237*** (0.028)</td><td>10.871*** (1.683)</td><td>15.762*** (2.933)</td></tr><tr><td>Project Max Budget</td><td>0.0004*** (0.00002)</td><td>0.0003*** (0.00003)</td><td>0.351*** (0.005)</td><td>0.410*** (0.007)</td></tr><tr><td>ln(Auction Duration)</td><td>0.214*** (0.004)</td><td>0.295*** (0.009)</td><td>-9.820*** (0.487)</td><td>-12.30*** (0.877)</td></tr><tr><td>ln(Buyer Experience)</td><td>-0.141*** (0.003)</td><td>-0.0863*** (0.020)</td><td>2.766*** (0.273)</td><td>-9.198*** (1.469)</td></tr><tr><td>Buyer Goldmember</td><td>-0.0385*** (0.009)</td><td>-6.04e-05 (0.011)</td><td>-1.187 (0.965)</td><td>2.094 (1.314)</td></tr><tr><td>Constant</td><td>1.758*** (0.020)</td><td>1.563*** (0.044)</td><td>65.904*** (2.566)</td><td>67.143*** (4.571)</td></tr><tr><td>Buyer fixed effect</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Time effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Category effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of observations</td><td>78,936</td><td>78,936</td><td>47,413</td><td>47,413</td></tr><tr><td>R-squared</td><td>0.108</td><td>0.070</td><td>0.293</td><td>0.333</td></tr><tr><td>No. of buyers</td><td>—</td><td>21,799</td><td>—</td><td>15,388</td></tr></table>

Note. Cluster-robust standard errors are reported for the FE models.

Table 4 Estimation Using Alternative Measures of Buyer Surplus

<table><tr><td>DV</td><td>(1) Buyer Surplus(Avg.)</td><td>(2) Buyer Surplus(Est.)</td></tr><tr><td>Open Bid</td><td>41.041***(2.728)</td><td>89.923***(17.430)</td></tr><tr><td>Project Max Budget</td><td>0.368***(0.005)</td><td>-0.587***(0.0206)</td></tr><tr><td>In(Auction Duration)</td><td>-17.641***(0.749)</td><td>-42.822***(4.452)</td></tr><tr><td>In(Buyer Experience)</td><td>-7.381***(1.525)</td><td>14.842(9.484)</td></tr><tr><td>Buyer Goldmember</td><td>-0.115(1.185)</td><td>-3.262(6.770)</td></tr><tr><td>Constant</td><td>17.684***(4.265)</td><td>905.700***(25.313)</td></tr><tr><td>Buyer FE</td><td>Yes</td><td>Yes</td></tr><tr><td>Time effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Category effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>78,936</td><td>47,413</td></tr><tr><td>R-squared</td><td>0.260</td><td>0.055</td></tr><tr><td>Number of buyers</td><td>21,799</td><td>15,388</td></tr></table>

Notes. Cluster-robust standard errors are reported in parentheses. The dependent variable, Buyer Surplus (Est.) in column (2) is based on a discrete choice model (details are discussed in Online Appendix IV).

the signs and the statistical significance of the estimates remain the same when we account for unobserved buyer characteristics. This suggests that our empirical identification is not seriously compromised by the selection of unobserved buyer characteristics.

We considered alternative measures of buyer surplus as robustness checks. Table 4 reports the estimation results based on fixed effects estimation with two alternative measures of buyer surplus. Overall, our findings are consistent across different measures. This suggests that the higher buyer surplus observed in open bid auctions is attributable to actual buyer surplus rather than measurement specifications.

## 5.2. Results for PSM and Instrumental Variable Analysis

The results from the fixed effects regression analysis support the superiority of open-bid auctions in online labor markets from the buyer’s perspective. Although on average open-bid auctions attract fewer bids, they generate a higher buyer surplus. As discussed in §4, an important issue with the main model is that the auction format is a choice of the buyers, and thus the estimation is susceptible to selection bias. Although we included proper controls (including buyer fixed effects) in the model to address the possibility for self-selection, we cannot completely rule out the endogenous selection of auction format as a potential confounding effect. To further strengthen the identification and establish a causal interpretation for our findings, we report two additional analyses based on two distinct econometric identification strategies.

5.2.1. Propensity Score Matching. To implement PSM, we used observed auction, buyer, and project characteristics as matching variables. Specifically, we considered project max budget, auction duration, buyer experience, buyer gold status, buyer country dummies, and project category and year–month pair dummy variables (ym 1-ym 6). We estimated the propensity scores using a probit model on the binary treatment variable (open versus sealed). Specifically, we estimated the conditional probability of receiving a treatment (open bid auction) given a vector of observed covariates. We then matched open bid auctions (treatment observations) to sealed bid auctions (control observations) using the estimated propensity scores. The groups of open bid and sealed bid auctions with similar propensity

Table 5 Matching Estimates (Treatment Effect for Open Bid)

<table><tr><td></td><td>Num Bids</td><td>Buyer Surplus</td></tr><tr><td>1-1 matching (N = 9,584)</td><td>-1.35*** (0.41)</td><td>13.30*** (2.77)</td></tr><tr><td>Kernel matching (N = 47,832)</td><td>-2.44*** (0.20)</td><td>8.23** (2.96)</td></tr><tr><td>NN (N = 4) matching</td><td></td><td></td></tr><tr><td>No Caliper (N = 47,832)</td><td>-2.57*** (0.40)</td><td>9.15** (3.48)</td></tr><tr><td>Caliper: 0.005 (N = 47,806)</td><td>-2.56*** (0.35)</td><td>8.42*** (3.03)</td></tr><tr><td>Caliper: 0.001 (N = 47,702)</td><td>-2.60*** (0.35)</td><td>8.09*** (3.06)</td></tr></table>

Notes. Bootstrapped standard errors are reported in parentheses. NN, Nearest neighbor.

$$
^ {* *} p <   0. 0 5; ^ {* * *} p <   0. 0 1.
$$

scores are expected to have similar values across all observed covariates in aggregate. After matching the propensity scores, we identified the average treatment effect on the treated (sealed bids) versus the control (open bids) on our performance measures. The results of the one-to-one PSM analysis (Table 5) confirmed our findings from the OLS and fixed effects analyses. We also considered other matching algorithms, such as kernel matching and nearest-neighbor matching $( n = 4 ,$ with different caliper values), as reported in Table 5. Different matching algorithms yielded parameter estimates that were qualitatively the same, which further strengthened the robustness of our findings on the effect of bid visibility on the number of bids and on buyer surplus. We report the balance checks in Online Appendix III.

5.2.2. Instrumental Variables. We also conducted an IV analysis using the GDP\_PPP of the buyer’s country of residence as the IV. In our data, we observed a buyer’s country of residence from the billing address reported during registration. We further recovered country information from the buyers’ login IP addresses using the IP2Location (http://www.ip2location.com) database. In our sample, the self-reported country and IP revealed country match for over 91% of the buyers, suggesting high consistency.<sup>21</sup>

The IV model is estimated with the approach suggested by Angrist and Pischke (2008). Specifically, we used the standard linear probability approach in the first stage estimation, and we included the estimated probability of using open bid format in the second stage estimation. Estimation results are reported in Table 6 (details about the first stage estimation are provided in Online Appendix III). In column (1), we used GDP\_PPP based on buyers’ self-reported countries; in column (2), we used the GDP\_PPP based on the “IP-revealed” countries; and in column (3), we used a subsample of buyers whose self-reported countries matched the IP-revealed countries. Table 6 provides further support for the robustness of our findings from the main model. The validity of the IV is assessed with three metrics. First, there is a significant correlation $( p < 0 . 0 0 0 1 )$ between GDP\_PPP and auction format as visualized in Figure AIII.2 in Online Appendix III. Second, the first stage F statistic is significant. Third, the Cragg–Donald Wald F statistics for all of the models were well above Stock and Yogo’s (2005) critical value. Notably, the quantified effect sizes of auction format on both the number of bids and buyer surplus are higher relative to the effect sizes based on fixed effect estimations, which implies that the estimates from both OLS and fixed effect analyses are likely conservative. However, caution should be taken in interpreting the IV estimates because IV estimates may be biased (Angrist and Pischke 2008). To offer additional support, we ran another IV analysis using a different instrumental variable (price change of the sealed bid auctions from free to \$1), which yielded findings that are consistent with the main analyses (Online Appendix III).

## 5.3. Additional Analyses

In this section, we report additional analyses with observational data and a small-scale randomized field experiment that provide evidence to support (a) the existence of a common value component for IT services in online labor markets, (b) the screening effect, (c) higher valuation uncertainty in open bid auctions, and (d) insignificant concern for endogenous bidder entry. Furthermore, we discuss bidder collusion, and finally we analyze project-related outcomes— selection/contract probability and buyer satisfaction.

5.3.1. Higher Surplus from Open Bid Auctions— Testing the “Common Value” Assumption. We propose that the reduction in valuation uncertainty over the common value component is the main driver of buyer surplus gain in open bid auctions. In the theoretical discussions, we have discussed the importance of the common value component in the cost of IT services auctioned in online labor markets. We further offer some empirical evidence of the existence of a common value component for IT services.

Based on prior literature (Milgrom and Weber 1982, Paarsch 1992, Haile et al. 2003), summarized by Bajari and Hortaçsu (2003), an appropriate empirical test to distinguish between a pure private values model and an auction model with a common value component is the winner’s curse test, theoretically proposed by Milgrom and Weber (1982) and empirically developed by Athey and Haile (2002) and Haile et al. (2003). The logic of the empirical test is that in a common value auction, rational bidders will increase their bids to mitigate the winner’s curse in a reverse auction. Because the possibility of a winner’s curse is greater in auctions

Budget-weighted Average Bid

Table 6 Estimation Results Using GDP\_PPP as the Instrumental Variable

<table><tr><td rowspan="2">DV</td><td colspan="2">(1) Self-reported country</td><td colspan="2">(2) IP-revealed country</td><td colspan="2">(3) Overlapping sample</td></tr><tr><td>In (Num Bids)</td><td>Buyer Surplus</td><td>In (Num Bids)</td><td>Buyer Surplus</td><td>In (Num Bids)</td><td>Buyer Surplus</td></tr><tr><td>Open Bid</td><td>-0.450***(0.026)</td><td>19.091***(2.577)</td><td>-0.588***(0.0302)</td><td>25.460***(3.082)</td><td>-0.606***(0.034)</td><td>26.920***(3.412)</td></tr><tr><td>Project Max Budget</td><td>0.0001***(0.00003)</td><td>0.362***(0.005)</td><td>0.00002(0.00002)</td><td>0.367***(0.005)</td><td>0.00004(0.0003)</td><td>0.368***(0.006)</td></tr><tr><td>In(Auction Duration)</td><td>0.127***(0.006)</td><td>-6.088***(0.700)</td><td>0.100***(0.007)</td><td>-4.878***(0.772)</td><td>0.097***(0.008)</td><td>-4.824***(0.874)</td></tr><tr><td>In(Buyer Experience)</td><td>-0.186***(0.004)</td><td>4.631***(0.376)</td><td>-0.199***(0.004)</td><td>5.512***(0.426)</td><td>-0.218***(0.006)</td><td>5.918***(0.546)</td></tr><tr><td>Buyer Goldmember</td><td>0.043***(0.010)</td><td>-4.560***(1.091)</td><td>0.065***(0.010)</td><td>-4.936***(1.120)</td><td>0.0663***(0.0120)</td><td>-5.444***(1.300)</td></tr><tr><td>Constant</td><td>2.842***(0.074)</td><td>22.81***(7.493)</td><td>3.224***(0.086)</td><td>4.901(8.840)</td><td>3.314***(0.099)</td><td>-1.146(10.10)</td></tr><tr><td>Time effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Category effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>78,936</td><td>47,413</td><td>78,076</td><td>46,863</td><td>68,520</td><td>40,217</td></tr><tr><td>R-squared</td><td>0.110</td><td>0.293</td><td>0.110</td><td>0.293</td><td>0.111</td><td>0.295</td></tr><tr><td>Cragg-Donald Wald F</td><td>123.4</td><td>70.64</td><td>98.36</td><td>50.75</td><td>76.02</td><td>37.79</td></tr></table>

Notes. Cluster-robust standard errors are reported in parentheses. Stock and Yogo (2005) critical value for relative bias > 10% is 16.38. In all models, the Cragg–Donald Wald F > 16038, alleviating weak instrument concerns. The R-squared values for IV estimations have no natural interpretation. $^ { * * * } p < 0 . 0 1$

with more bidders, the empirical prediction, under the common value assumption, is that the average bid in an N -bidder reverse auction will be lower than the average bid in an auction with N − 1 bidders. On the contrary, in pure private value auctions, the number of bids should not have an effect on average bidding prices (Athey and Haile 2002, Haile et al. 2003, Bajari and Hortaçsu 2003). Thus, examining how the average bid price<sup>22</sup> responds to different number of bidders shed light on whether a common value component exists for IT services in online labor markets. Specifically, we test the following null hypothesis: auctions in online labor markets are purely independent private value. If a null hypothesis holds, we expect the coefficient of number of bids to be either negative or not different from zero (Bajari and Hortaçsu 2003).

As shown by Table 7, the budget-weighted average bid (average bid price divided by the maximum project budget) positively correlates with the number of bidders in the auction. Considering the potential endogeneity of the number of bids, we used auction duration as an instrument for the number of bids. Auction duration serves as a valid instrument because it increases the number of bids, but it should not be driving the budget-weighted average bid. The results from the instrumental variable estimation are consistent with the fixed effects estimation. We cautiously interpret the regression results of the winner’s curse test as suggestive evidence that IT services in online labor markets are not purely private value, but they involve a common value component. We further conducted winner’s curse tests for open bid auctions and sealed bid auctions separately. The results show that the effect of number of bids on budget-weighted average bid in open bid auctions is smaller than that in sealed bid auctions (reported in Table AIII.7 of Online Appendix III).

Table 7 Winner’s Curse Test for Common Value

<table><tr><td rowspan="2">DV</td><td colspan="2">Budget Weighted Average Bid</td></tr><tr><td>(1) FE</td><td>(2) IV 2SLS</td></tr><tr><td>In (Num Bids)</td><td>0.026*** (0.002)</td><td>0.157*** (0.009)</td></tr><tr><td>Project Max Budget</td><td>0.0002*** (0.00001)</td><td>0.0002*** (0.00001)</td></tr><tr><td>In (Buyer Experience)</td><td>0.024*** (0.005)</td><td>0.036*** (0.005)</td></tr><tr><td>Buyer Goldmember</td><td>-0.001 (0.004)</td><td>-0.001 (0.004)</td></tr><tr><td>Constant</td><td>3.558*** (0.019)</td><td>0.175*** (0.017)</td></tr><tr><td>Buyer FE</td><td>Yes</td><td>Yes</td></tr><tr><td>Time effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Category effect</td><td>Yes</td><td>Yes</td></tr><tr><td>R-squared</td><td>0.05</td><td>—</td></tr><tr><td>Cragg–Donald Wald F statistic</td><td>—</td><td>2,055.97</td></tr><tr><td>Observations</td><td>78,936</td><td>78,936</td></tr><tr><td>Number of buyers</td><td>21,788</td><td>21,788</td></tr></table>

Note. Cluster-robust standard errors are reported in parentheses. <sup>∗∗∗</sup>p < 0001.

5.3.2. Fewer Bids from Open Bid Auctions—Testing the Screening Effect in Open Bid Auctions. One reason that we expect open bid auctions to attract fewer bids is the visibility of existing bids that discourages weaker bidders, i.e., the screening effect. To examine this effect in open bid auctions, we analyzed the relationship between bid sequence and bidders’

Table 8 Estimation Results

<table><tr><td>DV</td><td>Buyer Surplus(Max)</td><td>Buyer Surplus(Estimated)</td></tr><tr><td>Bid Sequence (n)</td><td>-0.031 (0.082)</td><td>-0.677 (0.610)</td></tr><tr><td>Bid Sequence (n) × Open Bid</td><td>0.272*** (0.085)</td><td>2.124*** (0.639)</td></tr><tr><td>Constant</td><td>175.693*** (0.231)</td><td>519.93*** (1.156)</td></tr><tr><td>Project FE</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>844,307</td><td>844,307</td></tr><tr><td>Number of projects</td><td>58,782</td><td>58,782</td></tr><tr><td>F-statistic</td><td>48.22***</td><td>29.31***</td></tr></table>

Notes. Cluster-robust standard errors are reported in parentheses. We restrict the sample to auctions with at least five bids to estimate the bids’ sequentia dynamics.

$$
^ {* * *} p <   0. 0 1.
$$

surplus provision to the $\mathrm { \ b u y e r } ^ { 2 3 }$ in both sealed and open bid auctions. If the screening effect exists, compared with sealed bid auctions in which bidders cannot observe prior bids, in open bid auctions, weak bidders (measured by lower surplus provision) are less likely to bid in the auction if more competitive bidders have already submitted their bids.

In this analysis, we look at within-auction sequential dynamics of bidder surplus provision. Specifically, we constructed a variable, Bid Sequence, based on the time stamp of each bid submission (the first bid will be recorded as 1, the second bid $^ 2 , \dots ,$ , the nth bid n), and linked Bid Sequence and the interaction of Bid Sequence with Open Bid to our dependent variable: the nth bidder’s surplus provision. We used the following equation to estimate the relationship between bid sequence and surplus provision, which is suggestive of a screening effect in open bid auctions (relative to sealed bid auctions):

$$
\begin{array}{l} \text {Buyer Surplus} _ {i, n} \\ = \beta_ {1} \times \text {Bid Sequence} _ {n} + \beta_ {2} \times \text {Bid Sequence} _ {n} \times \text {Open Bid} _ {i} \\ + \beta_ {3} \times \ln \text {bid} _ {i, n} + \alpha_ {i} + \varepsilon_ {i, n}. \end{array} \tag {3}
$$

In Equation (3), i is used to index projects, and $\alpha _ { i }$ is the project-specific (fixed) effect. A positive and significant estimation of $\beta _ { 2 }$ would support the screening effect in open bid auctions. The estimation results (Table 8) show that, compared with sealed bid auctions, later bids in open bid auctions offer a higher buyer surplus in open bid auctions (positive coefficient for the interaction term Bid Sequence × Open Bid). This result provides evidence for the existence of a screening effect.

5.3.3. A Randomized Field Experiment—Assessing Endogenous Entry of Heterogeneous Bidders. We conducted a small-scale field experiment to assess the endogenous entry of heterogeneous bidders across different auction formats. A one-factor (auction format) randomized experiment was conducted in a large online labor market by posting 28 projects (14 with open bid auctions and 14 with sealed bid auctions) to observe bidding behaviors and bidder characteristics in open bid versus sealed bid auctions. Online Appendix V explains the experimental design, procedures, sample posted projects, and additional details of the results.

As discussed earlier, the theoretical comparison of buyer surplus in open versus sealed auctions is less clear cut if bidders have heterogeneous ex ante value distributions. If bidders with different characteristics (e.g., cost, quality) self-select to enter different auction formats, the effect of auction format on buyer surplus may be caused by the endogenous entry of heterogeneous $\mathrm { b i d d e r s } ^ { 2 4 }$ (Athey et al. 2011). Although it is difficult to completely rule out the role of endogenous entry of heterogeneous bidders in observational data since we can neither control entry decision nor observe ex ante bidder differences in open versus sealed bid auctions, we can reduce this concern by comparing submitted bids. Following Athey et al. (2011), if bidders use equilibrium entry strategies, potential bidders will be similar to the actual bidders in a given auction. Thus, we can assess the severity of bidders’ endogenous entry with the field experimental data by comparing whether there are systematic differences in the observed characteristics of bidders (collected from the bidders profile pages; see Figure AV.1 in Online Appendix V) who bid on open bid auctions versus those who bid on sealed bid auctions.

Using both t tests of the mean difference and also nonparametric two-sample Kolmogorov–Smirnov (K–S) tests for distributional difference (Table 9), we found no significant difference between bidders in open bid versus sealed bid auctions across all observed characteristics. The overlaid kernel density plots for all of these variables are visualized in Figure AV.2 in Online Appendix V. The results suggest that endogenous entry does not pose a serious concern since the bidders are not different in open bid auctions versus sealed bid auctions, in terms of their observed characteristics.

5.3.4. Additional Robustness Checks with Field Experiment Data. Leveraging the experimental data, we validated the main findings from our observational study, which further alleviated concerns caused by the potential endogeneity of the project budget. Furthermore, we provide some evidence on bidders’ valuation uncertainty across the two auction formats.

Even for the same project, buyers may strategically set a different budget according to the auction format they chose to use, which leads to potential budget endogeneity. To assess budget endogeneity, we examined the bid prices from the experimental data in which the project budget is controlled and is thus exogenous. We first used a nonparametric two-sample K–S test for equality of the distribution functions of all bids observed for sealed (532 bids) and open bids auctions (478 bids), and a significant distributional difference was observed $( p = 0 . 0 1 2 ;$ Figure 2). We also used independent sample t tests to assess the mean difference of average bid prices in open versus sealed bid auctions (auction level). Average bid price was significantly higher $( t = 1 . 9 8 3 , p = 0 . { \dot { 0 } } 5 8 )$ in sealed $( \mu = 7 6 . 4 3 , \sigma = 2 1 . 8 3 )$ versus open bid auctions $( \mu = 6 1 . 6 4 , \sigma = 1 7 . 3 7 )$ . This difference is visualized in Figure 3(a). In sum, both the nonparametric and the parametric tests indicate open bid auctions attract lower bids, alleviating the concern about endogenous budget specification as the driver of our findings. A similar analysis was conducted for the observational data (Online Appendix VI).

Table 9 Differences in Bidder Characteristics Between Open Bid and Sealed Bid Auctions

<table><tr><td rowspan="2">Bidder variables</td><td colspan="2">Open Bid Auctions (478 bids)</td><td colspan="2">Sealed Bid Auctions (532 bids)</td><td colspan="2">t tests</td><td>K-S tests</td></tr><tr><td>Mean</td><td>Std. dev.</td><td>Mean</td><td>Std. dev.</td><td>t stat</td><td>p value</td><td>p value</td></tr><tr><td>Reputation</td><td>4.805</td><td>0.239</td><td>4.809</td><td>0.226</td><td>-0.239</td><td>0.803</td><td>1.000</td></tr><tr><td>Project Experience</td><td>193.805</td><td>487.381</td><td>206.269</td><td>473.608</td><td>-0.412</td><td>0.681</td><td>0.330</td></tr><tr><td>Earning</td><td>5.285</td><td>1.724</td><td>5.352</td><td>1.700</td><td>-0.574</td><td>0.566</td><td>0.750</td></tr><tr><td>Completion Rate</td><td>0.818</td><td>0.147</td><td>0.822</td><td>0.137</td><td>-0.353</td><td>0.725</td><td>0.995</td></tr><tr><td>On Budget</td><td>0.985</td><td>0.045</td><td>0.988</td><td>0.040</td><td>-1.03</td><td>0.305</td><td>1.000</td></tr><tr><td>On Time</td><td>0.958</td><td>0.070</td><td>0.962</td><td>0.057</td><td>-1.09</td><td>0.273</td><td>0.914</td></tr><tr><td>Rehire Rate</td><td>0.151</td><td>0.100</td><td>0.144</td><td>0.087</td><td>1.042</td><td>0.298</td><td>0.879</td></tr><tr><td>GDP_PPP</td><td>6,229.397</td><td>9,158.502</td><td>6,018.219</td><td>9,045.711</td><td>0.350</td><td>0.726</td><td>0.970</td></tr></table>

We then tested bidders’ valuation uncertainty in open versus sealed bid auctions using experimental data. The rationale is that, if valuation uncertainty in sealed bid auctions is the same as in open bid auctions, there should be no significant difference in price dispersion across the two formats. Notably, at the auction level, the nonparametric K–S test showed price dispersion (standard deviation of bid prices) to be significantly higher in sealed bid auctions $\mathsf { \bar { \Psi } } ( p = 0 . 0 6 )$ A parametric t test for the mean difference also showed price dispersion to be significantly higher $( t = 2 . 7 5 6 ,$ $p { = } 0 . 0 1 )$ in sealed bid auctions $( \mu = 5 \bar { 1 } . 9 2 , \sigma = 1 4 . 4 1 )$ than in open bid auctions $( \mu = 3 4 . 4 8 , \sigma = 1 8 . 7 8 )$ . This difference is visualized with box plots (Figure 3(b)). Given the higher price dispersion, compared with open bid auctions, bidders in sealed bid auctions face higher valuation uncertainty.

Figure 2 Kernel Density Plots of All Bids Observed  
![](/api/attachments/JAHPATYW/fulltext/images/e8e709c696e2d5b7e0df8ca4cd5ada36f0c42959e0f8fe3c18896060ec4ca0fe.jpg)

5.3.5. Discussion of an Alternative Explanation— “Bidder Collusion.” In our theoretical analysis, we proposed that the comparison between open and sealed bid auctions hinges on the trade-off between valuation uncertainty and competition uncertainty. However, bid visibility may lead to bidder behavior other than those driven by competition uncertainty and valuation uncertainty, such as bidder collusion $( \mathrm { e . g . }$ Athey et al. 2011, Fugger et al. 2015). As Cho et al. (2014) observed, the linkage principle may fail when bidders collude since collusion is more likely to occur in open bid auctions. Because more information is available in open bid auctions than in sealed bid auctions, collusion is more likely to happen in open bid auctions. Athey et al. (2011) attributed their finding about higher buyer surplus from sealed bid timber auctions to potential bidder collusion in open bid auctions.

Bidder collusion in online labor markets is less likely to reduce buyer surplus for several reasons. First, bidders in online labor markets are from geographically dispersed countries, and their communication is restricted to within-site messages that are monitored by the marketplace. Generally, it would be risky for them to collude via communicating through messages because the marketplace could close their accounts. Second, projects auctioned in online labor markets are not like timber auctions that are high in value. Most projects have a maximum budget of \$250 and \$750, and more than 80% of the projects in online labor markets are between \$100 and $\$ 2,500$ . Thus, there may not be enough incentive for bidders to engage in such collusion, which is costly and risky. Also, in the current study, we find that in open bid auctions, bidders bid lower and thus offer a higher surplus for buyers, which is opposite to the predictions of collusive bidding. Summarizing these arguments, bidder collusion is unlikely to be the reason that drives the observed effects in this study.

Figure 3 Average Bid Price and Price Dispersion in Open vs. Sealed Bid Auctions  
![](/api/attachments/JAHPATYW/fulltext/images/155f1eea875ea2821cdf1f1a6cb69b3fa015929ed4d1bec58be4ea58380230c4.jpg)  
(a) Box plot of average bid price

5.3.6. Additional Performance Outcomes: Selection, Contract Probability, and Buyer Satisfaction. In online labor markets, buyer surplus is only realized after the service is delivered. In reality, many projects are not completed, either because the buyer does not select a bidder, or the buyer and the selected service provider do not agree on a contract. Although our analysis suggested that open bid auctions help buyers to extract a higher surplus, it is important to examine the effects of auction design format on other outcomes that are critical to value creation in online labor markets. Specifically, we examined whether the auction format affects (1) the probability of the buyer finding a satisfactory offer (Selected); (2) conditional on the buyer’s selection, the probability that a contract was signed between the buyer and the selected service provider (Contracted); and (3) finally, how satisfied the buyer was with the service delivered (Satisfaction).

Selection, contract probability, and satisfaction may vary with auction format for several reasons. First, although open bid auctions receive fewer bids, the expected buyer surplus from the submitted bids is higher in open bid auctions. Second, the cost of bid evaluation increases with the number of bids received. High bid evaluation cost may demotivate buyers from carefully evaluating all bids (Carr 2003). Therefore, buyers in open bid auctions are likely to face fewer but more attractive bids, and thus have lower evaluation costs. With easier evaluation tasks, buyers have higher confidence in their choice and are less likely to regret their selection. Third, service providers have considerable uncertainty about the cost of serving a contract. Information from other bids may strengthen their confidence in cost assessment, making it more likely that the auction would result in a contract. Similarly, since open bid auctions generate a higher buyer surplus, projects contracted under open bid auctions are more likely to result in higher buyer satisfaction. Besides, buyers in open bid auctions are more likely to make an informed choice in contracting a service provider who, at the same time, is informed about the bids of other service providers and is able to evaluate the cost more precisely before service delivery (lower valuation uncertainty). Being more informed upfront is likely to increase the buyer’s satisfaction. Furthermore, sealed bid auctions result in more bids to be evaluated, which may lead to higher buyer’s expectation. As a result, even with the same level of service quality, buyers in sealed bid auctions are less likely to have a positive confirmation of their expectations (Oliver 1980). Given that the confirmation of expectations is a strong predictor of consumer satisfaction (Anderson and Sullivan 1993), we would expect open bid auctions to result in higher buyer satisfaction than sealed bid auctions.

![](/api/attachments/JAHPATYW/fulltext/images/6df2ded7b1d7b527f2cdbada0029631c2dfcfd215c0f6e44ca266f0fbb831adb.jpg)  
(b) Box plot of standard deviation of bids

To examine the effects of auction format on the (postauction) project outcomes, we adopted a similar model specification as in the main analysis. Since selection and contract are binary outcomes, we adopted a fixed effects Logit estimation. Satisfaction was measured by buyer-reported evaluations of the contracted service providers after project completion (integer between 1 and 10). Given the ordinal nature of the measure, we adopted an ordered Logit with fixed effects model, specifically, the consistent and efficient “blow up and cluster” (BUC) estimator (Baetschmann et al. 2015).

Estimation results are shown in columns (1)–(3) in Table 10. Across the three models, we found significant effects of auction format. Using odds ratios to interpret the Logit estimation results, we found that open BD auctions have 55.3% higher odds of having a winning bid selected than sealed bid auctions. Conditional on selection, a project posted with an open bid format is 22.1% more likely to reach a contract. For contracted projects, buyers are more satisfactory with the service delivered if projects are auctioned with an open bid format. We also implemented the PSM analysis for these variables and found consistent results (Online Appendix III). These additional results indicate that the open bid auction format is not only superior in resulting in bid selection, but helps in reaching a contract and in improving the project outcome.

Table 10 Effect of Bid Visibility on Contract Probability and Buyer Satisfaction

<table><tr><td>DVEstimation method</td><td>(1) SelectedFE Logit</td><td>(2) ContractedFE Logit</td><td>(3) SatisfactionFE BUC oLogit</td></tr><tr><td>Open bid auctions</td><td>0.440***(0.053)</td><td>0.200**(0.098)</td><td>0.462*(0.250)</td></tr><tr><td>Project Max Budget</td><td>-0.002***(0.000)</td><td>-0.001***(0.000)</td><td>0.00002 (0.0005)</td></tr><tr><td>In(Auction Duration)</td><td>-0.469***(0.014)</td><td>-0.283***(0.026)</td><td>0.024 (0.083)</td></tr><tr><td>In(Buyer Experience)</td><td>-0.472***(0.037)</td><td>-0.359***(0.064)</td><td>0.426***(0.149)</td></tr><tr><td>Buyer Goldmember</td><td>-0.013 (0.029)</td><td>0.076 (0.054)</td><td>0.017 (0.146)</td></tr><tr><td>Buyer FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time effect</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Category effect</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>51,887</td><td>20,923</td><td>13,226</td></tr><tr><td>Number of buyers</td><td>6,332</td><td>2,392</td><td>708</td></tr></table>

Note. Cluster-robust standard errors are reported in parentheses.  
<sup>∗</sup>p < 001; <sup>∗∗</sup>p < 0005; <sup>∗∗∗</sup>p < 0001.

## 6. Conclusion

## 6.1. Key Findings

In this study, we compared open versus sealed bid BD auctions in the context of online labor markets. Our empirical results based on a unique proprietary data set from a leading online labor market with both sealed and open bid auctions found significant differences between auction format (bid visibility) on auction performance (number of bids and buyer surplus). Whereas sealed bid BD auctions do attract more bids, open bid BD auctions offer a higher buyer surplus. Moreover, we quantified the economic effects of auction format on BD auctions. Compared with sealed bid BD auctions, open bid BD auctions attract 18.4% fewer bids. Open bid auctions are 55.3% more likely to result in buyer selection, are 22.1% more likely to reach a contract conditional on buyer selection, extract at least \$10.87 higher buyer surplus per project, and also result in significantly higher buyer satisfaction. Table 11 summarizes the empirical findings.

Table 11 Empirical Comparisons Between Sealed and Open Bid Auctions

<table><tr><td>Performance outcome</td><td>Comparison</td></tr><tr><td>Number of Bids</td><td>Sealed &gt; Open</td></tr><tr><td>Buyer Surplus</td><td>Open &gt; Sealed</td></tr><tr><td>Winner Selection</td><td>Open &gt; Sealed</td></tr><tr><td>Contract Probability</td><td>Open &gt; Sealed</td></tr><tr><td>Buyer Satisfaction</td><td>Open &gt; Sealed</td></tr></table>

## 6.2. Implications for Theory

This research contributes to literature on (a) auction design format and (b) online labor markets by offering large-scale empirical evidence from a real-life online labor market. Specifically, we seek to fill the gap in the literature on the effect of auction format (open and sealed bid auctions) on auction performance (number of bids and buyer surplus). Our study has the following theoretical implications.

First, our study provides insights to the auctions literature with regard to the design choice between open versus sealed bid auctions using large-scale observational data from real-life online labor markets. The design choice is not straightforward for online BD auctions in practice because many countervailing factors might be at play, such as bidder collusion (Haruvy and Katok 2013, Jap 2007), which may be exacerbated in open bid auctions; valuation uncertainty, which may be mitigated by the information transparency enabled by open bid auctions (Cho et al. 2014, Kagel and Levin 2009, McMillan 1994); competition uncertainty, which may lead risk-averse bidders to bid lower (Holt 1980, Maskin and Riley 1984); and heterogeneous bidder distribution (Athey et al. 2011), which may lead to endogenous entry in either open or sealed bid auctions. We show that open bid BD auctions outperform sealed bid BD auctions in terms of buyer surplus, selection probability, contract probability (conditional on buyer selection), and also buyer satisfaction. Our study builds on several seminal empirical studies that compared open versus sealed bid auctions using field observations. Notably, our study extends the work of Athey et al. (2011), who compared auction formats in forward U.S. timber auctions, and also the work of Cho et al. (2014), who compared auction formats in forward versus reverse auctions for used automobiles. By focusing on BD auctions in a novel context (online labor markets for IT services), which are shown to have a substantial common value component, our study echoes the theoretical findings of Menicucci (2004), who showed that even when bidders are risk averse, the (down-bid) effect of valuation uncertainty dominates the (up-bid) incentive to increase the chance of winning in first-price auctions with a common value component.

Second, our study has implications for auction format as an important design problem for BD auctions and online labor markets. Auction format is a prime example of an IS design that involves the moderation of the marketplace (Allon et al. 2012), and it has a significant role in the bidding strategy of service providers and the resulting surplus for buyers. Despite the proliferation of online labor markets, research on the optimal design and corresponding performance effects of online labor markets is lacking. We theoretically propose that valuation uncertainty and competition uncertainty coexist in auctions in online labor markets. Our findings suggest that auctions for IT services in online labor markets have an important interdependent common value component. With significant valuation uncertainty, service providers benefit from observing others’ bids, which allow them to make inferences about the costs of the posted projects, resulting in lower bids and a higher buyer surplus in general. For buyers, since the common value component is substantial, reduction in valuation uncertainty through open bid auctions drives down bid prices, which outweighs the benefit that a buyer can enjoy by maintaining the competition uncertainty high by using sealed bid auctions.

Third, our empirical examination has implications for important assumptions made in theoretical studies in the auctions literature for online BD auctions, specifically the existence of a common value component. Our results imply that IT services in online labor markets have an interdependent common value component, as opposed to a purely private component. This finding echoes the theoretical and experimental results from Goeree and Offerman (2002, 2003), who showed that products with private value and common value components can coexist. Buyer surplus may be higher when the information on the common value is public. (In our case, information transparency enabled by open bid auctions allows service providers to learn the common value (cost) of the IT service from other service providers.) Also, in online labor markets, the service providers’ uncertainty mostly comes from the difficulty in valuation rather than the difficulty to assess the competition. This is because although the cost of participating in a BD auction is nonnegligible, it is relatively small compared to the cost of offering an IT service at a loss (due to the winner’s curse).

## 6.3. Implications for Practice

This study has some actionable implications for practitioners as well. First, the number of bids has been seen as a measure for auction success because more bids indicate more choices for buyers, which increases buyer surplus. Therefore, online labor market intermediaries commonly charge a fee for sealed bid auctions, which is viewed as a premium (often paid) feature. The direct implication for practitioners is that more bids do not translate into higher buyer surplus. Open bid BD auctions consistently outperform sealed bid BD auctions in terms of buyer surplus, contract probability, and buyer satisfaction, despite fewer bids received. Our study links auction format with the bidding strategy of service providers and offers support for open bid auctions as an increasingly popular auction format in online labor markets. Given that labor markets are usually buyer driven, the intermediary’s proper incentives for buyers in terms of designing appropriate auction mechanisms have practical consequences for the sustainability of online labor markets. Accordingly, charging extra fees for sealed bid auctions may be harmful for labor market intermediaries.

Second, blindly pursuing more bids by using sealed bid auctions may not be a good strategy for buyers. Posting jobs using sealed bid BD auction usually comes at a cost (e.g., Freelancer used to charge \$1 for posting a sealed bid BD auction, and the cost recently increased to \$9), which can be avoided by using the default open bid format. Moreover, more bids entail a higher evaluation cost. If the buyer cannot afford to evaluate all bids (especially low quality bids), the open bid BD auction format would be a superior choice. Nevertheless, notwithstanding lower buyer surplus, sealed bid BD auctions remain attractive in some cases. For example, the potential for collusive bidding (Athey et al. 2011) among service providers can be mitigated by sealed bid auctions. Finally, the sealed bid design also offers a higher privacy protection for service providers who are concerned about opening their bids to the public (potentially for privacy reasons).

Third, this study has implications for other practical auction contexts. We believe our results could be generalized to auctions of goods with a significant common value component where information transparency could increase buyer surplus. For example, a common value component exists when the goods have high uncertainty, such as coins and collectibles (Bajari and Hortaçsu 2003) or used automobiles (Cho et al. 2014), or when goods have a resale value (Goeree and Offerman 2003).

## 6.4. Limitations and Suggestions for Future Research

First, buyers choose to use either “sealed” or “open” auction formats to post their CFBs, leading to an endogeneity concern. In this paper, a multitude of approaches were utilized to alleviate concerns about empirical identification, including a variety of buyer and project-level controls, buyer fixed effects, PSM, and IV analyses. We also conducted additional analysis and a field experiment to provide evidence of the robustness of the key findings. Identification concerns are common in observational studies, and based on various robustness analyses, they should not compromise our findings. Although we are confident that the current study properly identified the effects of bid visibility (open versus sealed bid auctions) on auction performance, future research could use other approaches for identification; for example, large-scale randomized field experiments could be implemented to further confirm and extend our study’s findings.

Second, our theoretical discussion focused on how bid visibility mitigates the service providers’ valuation uncertainty and competition uncertainty, and a substantial common value component of the cost of IT services in online BD auctions. We acknowledge that there may be alternative explanations that are at play in online BD auctions. Because of the limitation in our data, it is not possible to completely rule out and fully assess the impact of these alternative explanations, such as the endogenous entry of heterogeneous bidders. Endogenous entry of heterogeneous bidders definitely merits further exploration with richer data and by using alternative empirical methodologies (e.g., structural econometric modeling).

Finally, we focus our attention on CFBs, where little precontract investment on the project is required. By contrast, significant precontract investment is needed in other types of online labor markets. For example, some platforms, such as 99designs and InnoCentive, employ open innovation contests and tournaments (e.g., Terwiesch and Xu 2008), where service providers not only bid with a price quote, but they need to submit a final product along with their bid. The interaction and bidding dynamics on these platforms are likely to be different and call for future research to extend the analysis of bid visibility in open innovations.

## 6.5. Concluding Remarks

Online labor markets have changed the way buyers and service providers interact and the way labor is sourced globally. One key issue facing online labor markets today is how the auction format with regard to bid visibility (open versus sealed bid auctions) affects auction performance. Despite recent progress in the auction literature, the effect of bid visibility on auction performance in BD auctions remains inconclusive. By leveraging unique proprietary data on open and sealed (hidden from the public) bid auctions from one of the world’s largest labor markets, we demonstrated the advantage of open bid BD auctions on buyer surplus. Interestingly, open bid auctions attract fewer bids, but provide higher surplus to buyers, which makes open bid auction format a superior option for buyers in online labor markets. Given that many other design features are being proposed by practitioners to facilitate the exchange of labor across the globe, our study invites

IS scholars and practitioners to look more closely at the effect of bid visibility and other auction design formats on the strategic behavior of bidders and auction performance in online labor markets.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2015.0606.

## Acknowledgments

The authors would like to thank the senior editor, associate editor, and the three anonymous reviewers for a most constructive and developmental review process. The authors also thank Lorin Hitt, Pei-yu Chen, Gordon Burtch, Sunil Wattal, Xiaoquan (Michael) Zhang, Jianqing Chen, Yixin Lu, Ni Huang, Jason Chan, Juan Feng, and seminar participants at the Workshop on Statistical Challenges in e-Commerce Research (SCECR), the Conference on Information Systems and Technology (CIST), and the City University of Hong Kong, the Hong Kong University of Science and Technology for valuable feedback. The authors acknowledge financial support from the NET Institute [Project 13-05], the Center for International Business Education and Research (CIBER) through the U.S. Department of Education, the Temple University Fox School Young Scholars Forum, and the Research Grants Council of the Hong Kong Special Administrative Region, China [Project CityU 21501014].

## References

Abadie A, Imbens GW (2006) Large sample properties of matching estimators for average treatment effects. Econometrica 74(1): 235–267.

Adomavicius G, Curley SP, Gupta A, Sanyal P (2012) Effect of information feedback on bidder behavior in continuous combinatorial auctions. Management Sci. 58(4):811–830.

Adomavicius G, Curley SP, Gupta A, Sanyal P (2013) Impact of information feedback in continuous combinatorial auctions: An experimental study of economic performance. MIS Quart. 37(1):55–76.

Agrawal AK, Lacetera N, Lyons E (2013) Does information help or hinder job applicants from less developed countries in online markets? Working paper, National Bureau of Economic Research, Cambridge, MA.

Allon G, Bassamboo A, Çil EB (2012) Large-scale service marketplaces: The role of the moderating firm. Management Sci. 58(10): 1854–1872.

Anderson EW, Sullivan MW (1993) The antecedents and consequences of customer satisfaction for firms. Marketing Sci. 12(2):125–143.

Angrist JD, Pischke J-S (2008) Mostly Harmless Econometrics: An Empiricist’s Companion (Princeton University Press, Princeton, NJ).

Aral S, Muchnik L, Sundararajan A (2009) Distinguishing influencebased contagion from homophily-driven diffusion in dynamic networks. Proc. Natl. Acad. Sci. USA 106(51):21544–21549.

Arora A, Greenwald A, Kannan K, Krishnan R (2007) Effects of information-revelation policies under market-structure uncertainty. Management Sci. 53(8):1234–1248.

Asker J, Cantillon E (2008) Properties of scoring auctions. RAND J. Econom. 39(1):69–85.

Athey S, Haile PA (2002) Identification of standard auction models. Econometrica 70(6):2107–2140.

Athey S, Levin J, Seira E (2011) Comparing open and sealed bid auctions: Evidence from timber auctions. Quart. J. Econom. 126(1):207–257.

Kagel JH, Levin D (2009) Common Value Auctions and the Winner’s Curse (Princeton University Press, Princeton, NJ).

Ba S, Pavlou PA (2002) Evidence of the effect of trust building technology in electronic markets: Price premium and buyer behavior. MIS Quart. 26(3):243–268.

Baetschmann G, Staub KE, Winkelmann R (2015) Consistent estimation of the fixed effects ordered logit model. J. Roy. Statist. Soc.: Ser. A 4Statist. Soc.5 178(3):685–703.

Bajari P, Hortaçsu A (2003) The winner’s curse, reserve prices, and endogenous entry: Empirical insights from eBay auctions. RAND J. Econom. 34(2):329–355.

Bajari P, Hortaçsu A (2004) Economic insights from Internet auctions. J. Econom. Literature 42(2):457–486.

Banker RD, Hwang I (2008) Importance of measures of past performance: Empirical evidence on quality of e-service providers. Contemporary Accounting Res. 25(2):307–337.

Bapna R, Dellarocas C, Rice S (2010) Vertically differentiated simultaneous Vickrey auctions: Theory and experimental evidence. Management Sci. 56(7):1074–1092.

Bapna R, Jank W, Shmueli G (2008) Consumer surplus in online auctions. Inform. Systems Res. 19(4):400–416.

Carr SM (2003) Note on online auctions with costly bid evaluation. Management Sci. 49(11):1521–1528.

Cason TN, Kannan KN, Siebert R (2011) An experimental study of information revelation policies in sequential auctions. Management Sci. 57(4):667–688.

Chen J, Liu D, Whinston AB (2009) Auctioning keywords in online search. J. Marketing 73(4):125–141.

Cho SJ, Paarsch HJ, Rust J (2014) Is the “linkage principle” valid? Evidence from the field. J. Indust. Econom. 62(2):346–375.

Cramton P (1998) Ascending auctions. Eur. Econom. Rev. 42(3):745–756.

Cummings JN, Espinosa JA, Pickering CK (2009) Crossing spatial and temporal boundaries in globally distributed projects: A relational model of coordination delay. Inform. Systems Res. 20(3):420–439.

Daniel KD, Hirshleifer DA (1998) A theory of costly sequential bidding. Working Paper 98028, Ross School of Business, University of Michigan, Ann Arbor.

Dyer D, Kagel JH, Levin D (1989) A comparison of naive and experienced bidders in common value offer auctions: A laboratory analysis. Econom. J. 99(394):108–115.

Elmaghraby WJ, Katok E, Santamaría N (2012) A laboratory investigation of rank feedback in procurement auctions. Manufacturing Service Oper. Management 14(1):128–144.

Engelbrecht-Wiggans R, Haruvy E, Katok E (2007) A comparison of buyer-determined and price-based multiattribute mechanisms. Marketing Sci. 26(5):629–641.

Fugger N, Katok E, Wambach A (2015) Collusion in dynamic buyerdetermined reverse auctions. Management Sci., ePub ahead of print August 5, http://dx.doi.org/10.1287/mnsc.2014.2142.

Gallien J, Gupta S (2007) Temporary and permanent buyout prices in online auctions. Management Sci. 53(5):814–833.

Gefen D, Carmel E (2008) Is the world really flat? A look at offshoring at an online programming marketplace. MIS Quart. 32(3):367–384.

Goeree JK, Offerman T (2002) Efficiency in auctions with private and common values: An experimental study. Amer. Econom. Rev. 92(3):625–643.

Goeree JK, Offerman T (2003) Competitive bidding in auctions with private and common values. Econom. J. 113(489):598–613.

Goes PB, Lin M (2012) Does information really “unravel”? Understanding factors that motivate sellers to seek third-party certifications in an online labor market. Working paper, University of Arizona, Tucson.

Goes PB, Karuga GG, Tripathi AK (2010) Understanding willingnessto-pay formation of repeat bidders in sequential online auctions. Inform. Systems Res. 21(4):907–924.

Greenwald A, Kannan K, Krishnan R (2010) On evaluating information revelation policies in procurement auctions: A Markov decision process approach. Inform. Systems Res. 21(1):15–36.

Haile P, Shum M, Hong H (2003) Nonparametric tests for common values in first-price auctions. Working paper, National Bureau of Economic Research, Cambridge, MA.

Harris M, Raviv A (1981) Allocation mechanisms and the design of auctions. Econometrica 49(6):1477–1499.

Harstad RM, Kagel JH, Levin D (1990) Equilibrium bid functions for auctions with an uncertain number of bidders. Econom. Lett. 33(1):35–40.

Haruvy E, Katok E (2013) Increasing revenue by decreasing information in procurement auctions. Production Oper. Management 22(1):19–35.

Hausch DB, Li L (1993) A common value auction model with endogenous entry and information acquisition. Econom. Theory. 3(2):315–334.

Holt CA Jr (1980) Competitive bidding for contracts under alternative auction procedures. J. Political Econom. 88(3):433–445.

Hong Y, Pavlou PA (2012) An empirical investigation on provider pricing in online crowdsourcing markets for IT services. Proc. 33rd Internat. Conf. Inform. Systems, Orlando, FL. http://aisel.aisnet.org/ icis2012/proceedings/EBusinessStrategy/8/.

Howe J (2006) The rise of crowdsourcing. Wired 14(6):1–4.

Jap SD (2002) Online reverse auctions: Issues, themes, and prospects for the future. J. Acad. Marketing Sci. 30(4):506–525.

Jap SD (2007) The impact of online reverse auction design on buyer-supplier relationships. J. Marketing 71(1):146–159.

Kagel JH, Levin D (1986) The winner’s curse and public information in common value auctions. Amer. Econom. Rev. 76(5):894–920.

Kagel JH, Levin D (1999) Common value auctions with insider information. Econometrica 67(5):1219–1238.

Kannan KN (2012) Effects of information revelation policies under cost uncertainty. Inform. Systems Res. 23(1):75–92.

Klemperer P (2002) What really matters in auction design. J. Econom. Perspect. 16(1):169–189.

Kostamis D, Beil DR, Duenyas I (2009) Total-cost procurement auctions: Impact of suppliers’ cost adjustments on auction format choice. Management Sci. 55(12):1985–1999.

Krishna V (2009) Auction Theory, 2nd ed. (Academic Press, San Diego).

Lee FC, Tang J (2000) Productivity levels and international competitiveness between Canadian and US industries. Amer. Econom. Rev. 90(2):176–179.

Lin M, Lucas HC Jr, Shmueli G (2013) Research commentary–Too big to fail: Large samples and the p-value problem. Inform. Systems Res. 24(4):906–917.

Liu D, Chen J (2006) Designing online auctions with past performance information. Decision Support Systems 42(3):1307–1320.

Liu D, Brass DJ, Chen D (2015) Friendships in online peer-to-peer lending: Pipes, prisms, and relational herding. MIS Quart. 39(3):729–742.

Liu D, Chen J, Whinston AB (2010) Ex ante information and the design of keyword auctions. Inform. Systems Res. 21(1):133–153.

Lothian JR, Taylor MP (1996) Real exchange rate behavior: The recent float from the perspective of the past two centuries. J. Political Econom. 104(3):488–509.

Malone T, Laubacher R (1998) The dawn of the e-lance economy. Harvard Bus. Rev. 76(5):144–152.

Maskin E, Riley J (1984) Monopoly with incomplete information. RAND J. Econom. 15(2):171–196.

Maskin E, Riley J (2000) Asymmetric auctions. Rev. Econom. Stud. 67(3):413–438.

Matthews S (1987) Comparing auctions for risk averse buyers: A buyer’s point of view. Econometrica 55(3):633–646.

McAfee RP, McMillan J (1987) Auctions and bidding. J. Econom. Literature 25(2):699–738.

McCune B, Grace JB (2002) Analysis of Ecological Communities (MjM Software Design, Gleneden Beach, OR).

McMillan J (1994) Selling spectrum rights. J. Econom. Perspect. 8(3): 145–162.

Menicucci D (2004) Risk aversion in first price auctions with common values. Econom. Lett. 85(1):43–46.

Milgrom PR (2004) Putting Auction Theory to Work (Cambridge University Press, New York).

Milgrom PR, Weber RJ (1982) A theory of auctions and competitive bidding. Econometrica 50(5):1089–1122.

Millet I, Parente DH, Fizel JL, Venkataraman RR (2004) Metrics for managing online procurement auctions. Interfaces 34(3):171–179.

Mithas S, Jones JL (2007) Do auction parameters affect buyer surplus in e-auctions for procurement? Production Oper. Management 16(4):455–470.

Moreno A, Terwiesch C (2014) Doing business with strangers: Reputation in online service marketplaces. Inform. Systems Res. 25(4):865–886.

Oestreicher-Singer G, Zalmanson L (2013) Content or community? A digital business strategy for content providers in the social age. MIS Quart. 37(2):591–616.

Oliver RL (1980) A cognitive model of the antecedents and consequences of satisfaction decisions. J. Marketing Res. 17(4):460–469.

Paarsch HJ (1992) Deciding between the common and private value paradigms in empirical models of auctions. J. Econometrics 51(1):191–215.

Pallais A (2014) Inefficient hiring in entry-level labor markets. Amer. Econom. Rev. 104(11):3565–3599.

Perry M, Reny PJ (1999) On the failure of the linkage principle in multi-unit auctions. Econometrica 67(4):895–900.

Rishika R, Kumar A, Janakiraman R, Bezawada R (2013) The effect of customers’ social media participation on customer visit frequency and profitability: An empirical investigation. Inform. Systems Res. 24(1):108–127.

Rosenbaum PR, Rubin DB (1983) The central role of the propensity score in observational studies for causal effects. Biometrika 70(1):41–55.

Rust RT, Inman JJ, Jia J, Zahorik A (1999) What you don’t know about customer-perceived quality: The role of customer expectation distributions. Marketing Sci. 18(1):77–92.

Samuelson WF (1985) Competitive bidding with entry costs. Econom. Lett. 17(1):53–57.

Shachat J, Wei L (2012) Procuring commodities: First-price sealed-bid or English auctions? Marketing Sci. 31(2):317–333.

Snir EM, Hitt LM (2003) Costly bidding in online markets for IT services. Management Sci. 49(11):1504–1520.

Stock JH, Yogo M (2005) Testing for weak instruments in linear IV regression. Andrews DWK, Stock JH, eds. Identification and Inference for Econometric Models: Essays in Honor of Thomas Rothenberg (Cambridge University Press, New York), 80–108.

Stoll S, Zöttl G (2012) Information disclosure in dynamic buyerdetermined procurement auctions: An empirical study. Working paper, University of Munich, Munich, Germany.

Terwiesch C, Xu Y (2008) Innovation contests, open innovation, and multiagent problem solving. Management Sci. 54(9):1529–1543.

Vakrat Y, Seidmann A (2000) Implications of the bidders’ arrival process on the design of online auctions. Sprague R, ed. Proc. 33rd Annual Hawaii Internat. Conf. System Sci. (IEEE Computing Society Press, Los Alamitos, CA).

Vickrey W (1961) Counterspeculation, auctions, and competitive sealed tenders. J. Finance 16(1):8–37.

Willcocks LP, Kern T, Van Heck E (2002) The winner’s curse in IT outsourcing: Strategies for avoiding relational trauma. California Management Rev. 44(2):47–69.

Xu L, Chen J, Whinston A (2011) Price competition and endogenous valuation in search advertising. J. Marketing Res. 48(3): 566–586.

Yang Y, Chen PY, Pavlou PA (2009) Open innovation: An empirical study of online contests. Proc. 30th Internat. Conf. Inform. Systems, Phoenix 1–16. http://aisel.aisnet.org/icis2012/proceedings/ EBusinessStrategy/8/.

Yin PL (2006) Information dispersion and auction prices. Working Paper 02-024, Stanford Institute for Economic Policy Research, Stanford University, Stanford, CA.

Yoganarasimhan H (2013) The value of reputation in an online freelance marketplace. Marketing Sci. 32(6):860–891.

Zhang J, Liu P (2012) Rational herding in microloan markets. Management Sci. 58(5):892–912.

Zhang X, Feng J (2011) Cyclical bid adjustments in search-engine advertising. Management Sci. 57(9):1703–1719.
