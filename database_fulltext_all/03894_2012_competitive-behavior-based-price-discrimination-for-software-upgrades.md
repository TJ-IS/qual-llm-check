---
otero_id: 3894
otero_key: "PXF2FMJM"
title: "Competitive Behavior-Based Price Discrimination for Software Upgrades"
authors: "Amit Mehra; Ram Bala; Ramesh Sankaranarayanan"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0291"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/PXF2FMJM/fulltext/images/7dd343b674c00a84b949eccefeed6e20bdb1bcc029792f94b3e05fe83e4f03ca.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Competitive Behavior-Based Price Discrimination for Software Upgrades

Amit Mehra, Ram Bala, Ramesh Sankaranarayanan,

## To cite this article:

Amit Mehra, Ram Bala, Ramesh Sankaranarayanan, (2012) Competitive Behavior-Based Price Discrimination for Software Upgrades. Information Systems Research 23(1):60-74. http://dx.doi.org/10.1287/isre.1100.0291

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/PXF2FMJM/fulltext/images/67e20ebf70eb9a0ab1e0aae4c646c3023a264ae2842b0eadc79fd7e8e6ffb27d.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Competitive Behavior-Based Price Discrimination for Software Upgrades

Amit Mehra, Ram Bala

Indian School of Business, Hyderabad 500 032, India {amit\_mehra@isb.edu, ram\_bala@isb.edu}

Ramesh Sankaranarayanan

School of Business, University of Connecticut, Storrs, Connecticut 06269, rsankaran@business.uconn.edu

he introduction of product upgrades in a competitive environment is commonly observed in the software Tindustry. When introducing a new product, a software vendor may employ behavior-based price discrimination (BBPD) by offering a discount over its market price to entice existing customers of the competitor. This type of pricing is referred to as competitive upgrade discount pricing and is possible because the vendor can use proof of purchase of a competitor’s product as credible evidence to offer the discount. At the same time, the competitor may offer a discount to its own previous customers in order to induce them to buy its upgrade. We formulate a game-theoretic model involving an incumbent and entrant where both firms can offer discounts to existing customers of the incumbent. Although several equilibrium possibilities exist, we establish that an equilibrium with competitive upgrade discount pricing is observed only for a unique market structure and a corresponding unique set of prices. In this equilibrium, instead of leveraging its first mover advantage, the incumbent cedes market share to the entrant. Furthermore, the profits of both the incumbent and the entrant reduce with switching costs. This implies that the use of BBPD has product design implications because firms may influence the switching costs between their products by making appropriate compatibility decisions. In addition, lower switching costs result in reduced consumer surplus. Hence, a social planner may want to increase switching costs. The resulting policy implications are different from those prevalent in other industries such as mobile telecommunications where the regulators reduced switching costs by enforcing number portability.

Key words: behavior-based pricing; software upgrades; competitive strategy; switching costs; forward-looking customers

History: Vallabh Sambamurthy, Senior Editor and Associate Editor. This paper was received June 25, 2009, and was with the authors for 2 months for 2 revisions. Published online in Articles in Advance June 14, 2010.

## 1. Introduction

The introduction of product upgrades in a competitive environment is commonly observed in industries with rapid product innovation. The software industry is no exception. Moreover, today’s consumers of software are smart enough to anticipate their future options arising either from upcoming upgrades of existing products or from new products offered by competitors within the same product category. Hence, their decision to adopt a product depends on these anticipated future options. Consequently, firms have to incorporate this strategic consumer behavior in their product design and pricing decisions. There is now a significant body of academic literature exploring these issues for monopolistic firms. Although this literature has significantly advanced our understanding, the monopolistic setting is restrictive because competition does play an important role in many software product categories. There are several examples: Solver versus Evolver tools for optimization on spreadsheets, Mathematica versus Maple in the scientific analysis space and so on.

Typically, competition in a product category develops over time. The incumbent (first mover) in a product category is a temporary monopoly until others enter the market with their competing offerings. Thus the first version of Maple was released in 1982<sup>1</sup> whereas Mathematica 1.0 was released much later in 1988.<sup>2</sup> Incumbent firms may have several advantages. For example, they may be able to establish their market shares before competition starts heating up. One may think that newly entering firms can benefit from introducing a better product than the incumbent’s offering. However, the incumbent may match the entrant’s product by introducing an upgrade of its earlier offering. Thus, when introducing their products, new entrants are faced with two challenges: first, they have to ensure that their product is “state of the art” and provides comparable functionality to the incumbent’s current offering; second, given that the incumbent already has an existing market share due to sales of previous versions of its products, they must provide proper monetary incentives to the existing customers of the incumbent to buy their product. The first issue relates to the inherent technical capabilities of the entrant whereas the second issue relates to the pricing policy of the entrant firm. The latter issue is the main focus of our research.

The pricing policy of a firm is closely related to the purchase decision of the customer. So, we explore here the factors that influence the purchase decisions of customers in some more detail. When evaluating two products, customers prefer the one that is a better fit with their requirements. For example, consumers who use Scientific Word software to write technical documents may prefer to use Maple over Mathematica for their mathematical analyses because Maple integrates well with Scientific Word. Thus Wolfram Research (the company that sells Mathematica) would find that such customers are less likely to prefer Mathematica over Maple. Previous purchase history of the customers is another important factor that influences their purchase behavior. Once a customer buys a product from a firm, the decision of abandoning that product to move to another firm’s product is not costless. Customers typically incur a switching cost for this move. These costs take various forms. For example, the psychological cost of giving up the comfort of using a product that one is familiar with constitutes one type of switching cost (Brehm 1956). The effort required to translate or recreate files into a new format is also a form of switching cost. Thus, already existing files incorporating previous work of a customer may no longer be used with the competing product due to incompatibilities. For example, files created in Maple cannot be manipulated in Mathematica. The pricing decisions by firms must anticipate both the fit costs and switching costs of customers.

To counter the switching costs of existing customers of an incumbent firm, an entrant may offer a discount over its market price to encourage these customers to buy its product. This practice is known by the name “competitive upgrade discount pricing.” Such types of behavior-based price discrimination mechanisms are unique to a competitive market and are facilitated through ease of gathering and verifying previous purchase information (through digital systems such as emails or through websites of firms). Thus Stylus Studio offers an upgrade discount price to customers who can forward their purchase confirmation or key-code e-mail from a competitor (Stylus Studio 2008). An incumbent firm can try to prevent the entrant from poaching its customers by providing discounted pricing to its existing customers for its upgraded product offering. This is also a form of behavior-based price discrimination and is typically referred to as “upgrade pricing.”

Offering discounted pricing to previous customers of the incumbent provides the benefits of price discrimination to the incumbent and the entrant. But better targeting of different customer segments through different prices also intensifies price competition between them. Hence setting discounted prices for previous customers may be good or bad for the firms’ profits. An example of provision of discounted pricing for previous customers in an incumbententrant situation is seen in the Web application development engine category of products based on the ColdFusion Markup Language. This language was developed by Adobe Inc. in 1995<sup>3</sup> and the current major providers of Web application development engines based on this language are Adobe Inc. through its Adobe ColdFusion 8 product and New Atlanta through its Blue Dragon 7.0 product. Although Adobe Inc. authored the language and has since been coming up with Web application development products based on this language, New Atlanta entered the fray only in 2002 (http://en.wikipedia.org/wiki/BlueDragon). Thus Adobe is the incumbent and Blue Dragon is the entrant. New Atlanta announced a competitive upgrade discount for Adobe’s customers in conjunction with announcing the 7.0 version of its Blue Dragon product in March 2007.<sup>4</sup> On the other hand, Adobe Inc.’s product, Adobe ColdFusion 8 is also available at an upgrade discount for its existing customers (http://www.adobe.com/products/ coldfusion/—accessed in May 2008).

Clearly, the competitive setting with upgrades raises several interesting questions: What competitive upgrade discount prices should the entrant firm set? Does the incumbent firm set upgrade pricing to counter such a pricing strategy by the entrant? What is the impact of such pricing on market shares? Can there be product design implications due to this pricing structure? Finally, we would like to know the impact on consumer welfare, particularly as a function of switching cost. We provide answers to these questions in this paper and thus provide a blueprint to look at the issue of competitive behavior-based price discrimination in the software industry.

## 2. Related Literature

The purpose of price discrimination is to segment customers with different willingness to pay through different prices. The flexibility obtained by matching prices with the willingness to pay of customers results in an increase in profits. Several mechanisms for price discrimination have been studied in the literature: Narasimhan (1984) study coupons, Terwiesch et al. (2005) analyze a “name your own price channel,” Essegaier et al. (2002) look at nonlinear pricing schemes in the context of capacity constraints, Chen et al. (2001) evaluate the impact of imperfect individual targetability on profits under competition, Van Ackere and Reyniers (1995) evaluate the optimality of conditioning prices on purchase history. Some researchers like Lu and Moorthy (2007) have compared the attractiveness of different mechanisms for price discrimination. The ability to price discriminate between customers may impact a firm’s decisions along other dimensions as well: Choudhary et al. (2005) examine the impact of personalized pricing on quality choice by firms, Sundararajan (2004) finds that the firm’s choice of managing piracy through digital rights management software (DRM) depends on its ability to price discriminate, and Ghose et al. (2007) consider the trade-off between retailers’ ability to price discriminate offline versus the savings in acquisition costs of customers in an online environment at the expense of the ability to price discriminate.

The usage of past purchase history to price discriminate across consumers is called behavior-based price discrimination (BBPD) and is particularly relevant to our work. There are several papers that study various aspects of BBPD in both monopolistic and competitive settings. Fudenberg and Tirole (2000) study the issue of customer poaching through discount pricing, but in the context of competing nondurable goods. Acquisti and Varian (2005) study the ability to condition prices on past history when customers have the ability to protect their privacy. Pazgal and Soberman (2008) analyze the scenario where competing firms offering nondurable products can add benefits for past consumers as well as charge them different prices. Shin and Sudhir (2007) find conditions under which existing customers of a firm will be either rewarded or punished. Villas-Boas (2004) evaluates price cycles in the context of overlapping generations of customers. Hart and Tirole (1988) compare the impact of BBPD across durable and nondurable goods. Kennan (2001) studies the case of BBPD when consumer preferences vary over time. Zhang (2010) addresses the issue of endogenous product lines across time in a Hotelling-style duopoly model. Fudenberg and Villas-Boas (2006) and Arora et al. (2008) provide a comprehensive overview of the literature in this area.

The use of behavior-based price discrimination in the context of sequential product introduction of durable products of improving quality is the niche where our contribution is placed. When an upgrade is introduced, firms are able to price discriminate between customers based on previous purchase behavior. Customers who own an earlier version of the product have lesser value for its upgrade than new customers because of the cannibalization effect from the product they already own. In such a situation, having a single price for both types of customers may reduce profits. This provides the rationale for having a separate upgrade price for existing customers that is discounted with respect to the market price for new customers. Most of the work in this niche has analyzed the upgrade pricing decision for monopolies. The earliest paper in this context is by Dhebar (1994) that looks at the effect of product improvement on the ability of the firm to commit to future period prices. Fudenberg and Tirole (1988) look at the upgrades and trade-ins issue by considering different information structures that the monopolist has about individual customers. Ellison and Fudenberg (2000) study the effects of upgrades on social welfare, particularly in the context of network externality. Padmanabhan et al. (1997) investigate the positioning decision across periods given network externality effects for a fixed set of homogeneous customers. Other interesting papers that consider upgrade pricing and related issues are by Waldman (1996), Choi (1994), Raghunathan (2000), Waldman (1993), Moorthy and Png (1992), Sankaranarayanan (2007), Bala and Carr (2009), Erat and Kavadias (2006), Ghose and Sundararajan (2005), Levinthal and Purohit (1989), and Nahm (2004).

In our paper, we aim to specifically study the BBPD for sequential upgrade introductions of software products in a competitive environment. Because competition is pervasive in software product markets (several examples are provided in the introduction section of the paper), our analysis is a very realistic representation of such markets. The competitive aspect allows us to incorporate a new form of upgrade discount pricing over the monopoly situation where the price discount is available to even previous customers of the competitor. As described earlier, such pricing is called the competitive upgrade discount pricing. We investigate the nature of the equilibrium that supports competitive upgrade discount pricing in detail. We find that this equilibrium has the unique feature that it entails the incumbent eventually losing market share to the entrant. Clearly, such a situation does not exist for a monopoly because competitive upgrade discount pricing does not have any meaning in that context. One more factor that becomes particularly relevant in the context of competition is switching costs. These are the costs that are incurred by customers who switch from one firm’s product to the other firm’s product. Starting with Klemperer (1987 b), a rich stream of the economics literature has studied the consequences of switching costs. Farrell and Shapiro (1988) and Beggs and Klemperer (1992) analyze a competitive model with switching costs and conclude that switching costs may encourage entry by new firms.

Klemperer $( 1 9 8 7 \mathsf { a } ,$ b) find that the presence of switching costs results in firm strategies that focus on gaining market share. This focus explains the existence of limit pricing behavior by an incumbent. Klemperer (1989) further finds that switching costs results in price wars. A good overview of this literature is available in Klemperer (1995). Researchers have also studied the possibility that switching costs could be endogenous: Marinoso (2001), Cabral and Villas-Boas (2005). Switching costs have also been analyzed in various applied business fields. There are many examples. In information systems: Viswanathan (2005) and Demirhan et al. (2007), in marketing: Shi et al. (2006), and in operations management: Kamrad and Siddique (2004) and Gans (2002). We thoroughly examine the impact of switching costs when competitive upgrade discount pricing is used and show that competing firms have the incentive to design their products in a way so that the switching costs are reduced. Thus there are product design implications of our work. Our model also allows us to shed light on the policy implications of competitive upgrade discount pricing. In particular, we are able to show that an increase in switching costs could increase consumer welfare. This is unusual because switching costs are deadweight losses. This happens because firms in competitive settings reduce their prices in response to an increase of switching costs so much so that the overall benefit to consumers increases due to increase of switching costs.

To summarize our contribution, we formulate the competitive version of the sequential innovation problem with behavior-based price discrimination where firms produce software product upgrades and customers incur switching costs when they shift to a competitor’s product. This allows us to add to different streams of literature such as behavior-based price discrimination, “sequential innovation,” and the “implications of switching costs” by incorporating competition between firms producing durable goods. To the best of our knowledge, ours is the first paper to address this issue. The rest of the paper is organized as follows. Section 3 specifies the model setup and §4 characterizes the market shares of the incumbent and the entrant when competitive upgrade discount pricing is set in equilibrium. We round up this thread of the analysis in §5 by characterizing the profits of the two firms in the equilibrium where competitive upgrade discount pricing is used. Furthermore, we study the impact of switching costs on firm strategies and on consumer welfare. In §6, we consider several extensions to the original model. We finally offer our conclusions in §7. For the sake of brevity, all proofs are provided in the appendix.<sup>5</sup>

## 3. Model

Our model is derived from the well-established Hotelling model of the market. This market is characterized by customers who have value for a single unit of the software product. They are continuously distributed along a straight line of unit length in terms of their requirements and tastes and are indexed by the distance t from the left end of the market. The density function of customer type t is given by $g ( t )$ and the cumulative density function is G4t5. We assume that t is given by an IFR (increasing failure rate) distribution and the density function $g ( t )$ is symmetric in the range 601 17. This class of distributions is large and includes the uniform and normal distributions. It also includes the beta distribution for a wide range of parameters. For further details, see Lariviere (2006) for use of these distributions in a monopoly setting and Kim (2007) for a competitive setting. Consumers incur a “fit” cost if a product does not perfectly match their requirements. This cost is proportional to the distance between the location of the customer and the product and is a maximum of d.

There are two periods in this model. In the first period only the incumbent firm offers a product that is situated at the left end of the market without loss of generality. This product is offered at a price $p _ { 1 }$ and offers a utility of f per period to a customer who does not incur any fit costs with this product.

In the second period, the entrant introduces its product that is located at the other end of the market and the incumbent also simultaneously introduces an upgrade of its first period product. Both second period products provide a maximum utility $f _ { u } > f ^ { 6 }$ in this period. Thus an initial simplifying assumption is that neither the incumbent’s nor the entrant’s new product is inherently superior. By having this assumption we are able to focus purely on the pricing issues that arise due to competition. The incumbent sets an upgrade price $p _ { u }$ for its existing customers (those customers who bought in the first period) and a market price $p _ { i }$ for new customers where $p _ { u } \leq p _ { i }$ so that it is rational for the existing customers to identify themselves as previous purchasers of the firm’s product through some proof of purchase. This is similar to the “semianonymous” customer case first analyzed by Fudenberg and Tirole (1988). Such customers see both the prices set by the firm and identify themselves only if by doing so they get to buy at a lower price. The firm by itself does not have an instrument to identify one set of customers from the other. This is typically the case for software products meant for individual consumers. The entrant sets a competitive upgrade discount price $p _ { d }$ for the existing customers of the incumbent and a market price $p _ { e }$ for those customers who did not purchase in period 1. Here, again, $p _ { d } \leq p _ { e }$ so that it is incentive compatible for the incumbent’s existing customers to identify themselves to the entrant. An existing user of the incumbent’s first-period product who decides to buy the entrant’s product in the second period by availing the competitive upgrade discount price incurs a switching cost, s.

This is thus a situation that involves two firms: the incumbent and the entrant and the potential customer base of both firms. We assume full information to all constituents and employ the subgame perfect equilibrium concept. All firms and customers are forward looking and make decisions based on future period options available to them. We are interested in identifying those strategies that utilize competitive upgrade discount pricing by the entrant. Such equilibria<sup>7</sup> should encompass a segment of customers who buy from the incumbent in the first period but switch to the entrant’s product by utilizing the competitive upgrade discount price for upgrades. Performing comparative statics on these equilibria would provide deeper insights about firm behavior (incumbent and entrant) and welfare outcomes in the context of behavior-based competitive pricing strategies.

## 4. Identification of Equilibria with Competitive Upgrade Discount Pricing for Upgrades

To identify equilibria that utilize competitive upgrade discounts for upgrades, we must start by identifying the full set of possible equilibria and then find a reduced set that employs these discount prices. Because the customers’ buying decisions and the pricing strategies are closely connected, we first focus on the customers’ decisions given the prices. We assume that customers who do not buy either firm’s product have an outside option whose utility is normalized to zero. The customers have two options in period 1: buy the incumbent’s offering, or do not buy its offering. These options correspond to first-period surpluses of $f - t d - p _ { 1 }$ and zero, respectively.

In the second period, existing customers of the incumbent have one of three choices: To continue to use the incumbent’s initial product, to buy the incumbent’s upgrade, or to buy the entrant’s product. Such customers get second-period surpluses of $f - t d$ by exercising option number 1, $f _ { u } - t d - p _ { u }$ from option number 2 and $f _ { u } - ( 1 - t ) d - p _ { d } - s$ from exercising option number 3. The new customers also have three choices: Buy the entrant’s product, buy the incumbent’s new product, or do not buy. By exercising these options the customers get second-period surpluses of $f _ { u } - ( 1 - t ) d - p _ { e } , \ \check { f } _ { u } - t d - p _ { i } ,$ and zero, respectively.

Forward-looking customers correctly anticipate second-period prices in the first period. Hence their first-period decision of “buy from incumbent” or “do not $\mathrm { \ b u y ^ { \prime \prime } }$ is based on anticipation of their optimal second-period choice. Thus, the forward-looking capability of customers helps them maximize their total surplus from both periods. As pointed out earlier, any customer has three choices in the second period and two choices in the first period. This gives a total of six options to a customer at the beginning of the first period. These options and the corresponding overall surpluses from both periods are listed below:

1. Buy from incumbent in period 1 and do not buy in period 2. The net surplus is $2 f - 2 t d - p _ { 1 }$

2. Buy from incumbent in period 1 and upgrade to the incumbent’s new product in period 2. This gives a total surplus of $f + \bar { f } _ { u } - 2 t d - p _ { 1 } ^ { - } - p _ { u }$

3. Buy from incumbent in period 1 and upgrade to the entrant’s product in period 2. This gives a two period surplus of $f + f _ { u } - d - p _ { 1 } - p _ { d } - s .$

4. Do not buy the incumbent’s product in period 1 and buy the incumbent’s product in period 2. This results in a total surplus of $f _ { u } - t d - p _ { i }$

5. Do not buy the incumbent’s product in period 1 and buy the entrant’s product in period 2. This gives a surplus of $f _ { u } - ( 1 - t ) d - p _ { e }$

6. Do not buy the incumbent’s product in period 1 and do not buy any product in period 2 giving a total surplus of zero.

Out of these six options, customers choose the one that gives them the maximum surplus. Consequently, the market divides up into segments such that each market segment represents customers who exercise the same choices in periods 1 and 2. It is possible that some options may be completely dominated by others and so those will never be chosen. We define each possible configuration of market segments as a market structure. For example, a configuration of segments 2, 3, and 4 in that order constitutes a market structure. Note that the customer surpluses under each of the six options above is either a fixed number for given parameter values and prices, or is a continuous function of t (customer location). Hence, customers who favor a particular option must all be contiguous. Thus a particular segment must appear only once in a market structure. This property considerably reduces the number of possible market structures. The next result helps reduce the market structure possibilities even further.

<sup>Lemma</sup> <sup>1.</sup> The firms will set prices such that no customer will exercise option 1.

Lemma 1 shows that option (1) is always dominated and hence the possible number of segments reduce from six to five. Even then, the residual number of possibilities for market structures are very large. For example, a total of 5! market structures are possible when all the five segments are included. Analyzing such a large number of market structures is a tedious exercise because the pricing strategies and the market structures are dependent on each other. In other words, the market structures that emerge at equilibrium due to customers’ choice depend upon the prices chosen by the firms. On the other hand, because the firms’ profits depend upon the specific market structure, their pricing policies in turn are contingent on the market structure. However, in keeping with our primary objectives, we focus only on the market structures that are concomitant with competitive upgrade discount pricing for upgrades. A necessary condition for this to happen is that the customer surplus of option (3) is positive because customers exercising this particular option are the only ones who switch from the incumbent’s product in period 1 to the entrant’s product in period 2 by availing of the competitive upgrade discount price for upgrades. Note the special feature of option (3) is that the customer surplus of all customers who exercise this option is the same (because this expression is independent of t). Consequently, option (6) with zero customer surplus will always be dominated by this option for all customers. Hence, we can eliminate the market segment emerging from exercising option (6) from consideration. For due diligence, we will check later that the customer surplus by exercising option (3) is at least weakly positive when competitive upgrade discount pricing strategies are used. In the remaining options, (2), (3), (4), and (5) notice that the coefficients of the customer’s location t are −2, $0 , - 1$ , and 1. This implies that any market structure must encompass these segments only in the order (2), (4), (3), and (5) from the left (incumbent’s location). This ordering is illustrated in Figure 1. Hereon, we refer to these four segments as $\check { \mathbf { A } } , \ \mathbf { B } , \mathbf { C } ,$ and D with

A being the leftmost segment and $\mathrm { \mathrm { B } } , \mathrm { C } ,$ and D follow from left to right. Note that this does not imply that all the four segments must exist. It merely implies that the segments that do exist must follow this order.

The preceding analysis now leaves us with only eight possible market structures that include segment $C ,$ which must be nonzero for some customers to switch from the incumbent’s to the entrant’s product. These market structures are: ABCD, ACD, ABC, BCD, CD, BC, AC, and C. We continue our analysis by determining whether an equilibrium incorporating competitive upgrade discount pricing for upgrades with the market structure ABCD can exist. We pick this market structure to analyze first because it is the most general and allows for all four segments to be nonzero. To do this analysis we use the market segmentation illustrated in Figure 1. We refer to the index of the customers at the three boundary points between the segments A, B, C, and D as $M _ { 1 } , M _ { 2 } ,$ and $M _ { 3 }$ from left to right. We now determine the profit maximizing second-period prices set by the incumbent and the entrant to implement this market structure. In segment A, the upgrade price $p _ { u }$ is set so that the indifferent customer gets a weakly higher surplus from upgrading to the incumbent’s product compared to the surplus she gets from either not upgrading (individual rationality or IR) or upgrading to the entrant’s product (incentive compatibility or IC). These constraints are

$$
\begin{array}{c} f _ {u} - M _ {1} d - p _ {u} \geq f - M _ {1} d \quad (\text { individual   rationality }) \\ f _ {u} - M _ {1} d - p _ {u} \geq f _ {u} - (1 - M _ {1}) d - p _ {d} - s \\ (\text { incentive   compatibility }). \end{array}\tag{1}
$$

Because of these two constraints the price $p _ { u } =$ $\mathrm { M i n } [ f _ { u } - f , p _ { d } + d + s - 2 d M _ { 1 } ]$ . Following similar logic we find $p _ { i } = \mathsf { M i n } [ d + p _ { e } - 2 d M _ { 2 } , f _ { u } - d M _ { 2 } ] , p _ { e } =$ $\mathrm { M i n } [ p _ { i } - d + 2 d M _ { 3 } , f _ { u } - d + d M _ { 3 } ] ,$ and $p _ { d } = \mathrm { M i n } [ p _ { u } - d -$ $s + 2 d M _ { 2 } , f _ { u } - f - d - s + 2 d M _ { 2 } ]$ . An implication of

Figure 1 Market Segmentation Under Competition  
![](/api/attachments/PXF2FMJM/fulltext/images/c587e430727a3ba68505fefb1c134d87da70ea14084e5e3e3f74f57fe0f0c09f.jpg)

Lemma 1 is that $p _ { u } < f _ { u } - f$ (please refer to the proof in the appendix). Hence the last equation can be simplified to $p _ { d } = p _ { u } - d - s + 2 d M _ { 2 }$ . Because three of the second-period prices $( p _ { u } , \ p _ { i } ,$ and $p _ { e } )$ have two possibilities, the second period is characterized by one or more sets of prices out of eight possible price combinations.

Given the second-period prices, the boundary points between the segments are those where a customer gets equal total (first- and second-period) surplus from being in either segment. These can be found using the following equations:

$$
f + f _ {u} - 2 M _ {1} d - p _ {1} - p _ {u} = f _ {u} - M _ {1} d - p _ {i},\tag{2}
$$

$$
f _ {u} - M _ {2} d - p _ {i} = f + f _ {u} - d - p _ {1} - p _ {d} - s,\tag{3}
$$

$$
f + f _ {u} - d - p _ {1} - p _ {d} - s = f _ {u} - (1 - M _ {3}) d - p _ {e}.\tag{4}
$$

If an equilibrium with all four market segments exists, at least one of the eight systems of equations for the second-period prices when substituted in the firstperiod indifference Equations (2), (3), and (4), must yield the boundary points $M _ { 1 } , M _ { 2 } ,$ and $M _ { 3 }$ such that $M _ { 1 } < M _ { 2 } < M _ { 3 }$ . Using the above mentioned methodology we arrive at our next result.

<sup>Lemma</sup> <sup>2.</sup> At equilibrium, the condition $M _ { 1 } < M _ { 2 }$ $< M _ { 3 }$ cannot be satisfied. This implies that there exists no subgame perfect equilibrium in pure strategies with the market structure A, $\dot { B } , C , D$

Thus all four possible market segments can never coexist in equilibrium. An implication of Lemma 2 is that an equilibrium must be characterized by $M _ { 1 } = M _ { 2 } < M _ { 3 } ,$ or $M _ { 1 } < M _ { 2 } = M _ { 3 } ,$ , or $M _ { 1 } = M _ { 2 } = M _ { 3 } ^ { \cdot }$ This, in turn, implies that the first-period market must always be contiguous. Thus in any period (1 or 2) it will not happen that some customers to the left and right of a segment buy from a firm while customers from that segment do not. Finally, due to Lemma 2, we have eliminated one more market structure with competitive upgrade discount pricing for upgrades and are now left with the remaining seven possibilities. We now make two assumptions to enable us to focus on realistic conditions under duopoly competition. We refer to customers who buy from the incumbent in the first period as “first-period customers.” The complementary segment of customers who do not buy from the incumbent in the first period are called “non-first-period customers.”

<sup>Assumption</sup> <sup>1.</sup> In the first period, the market is neither fully covered nor fully uncovered by the incumbent’s product.

Assumption 1 ensures that the incumbent firm is really an incumbent, i.e., at least some customers buy its product in the first period. It further ensures that the incumbent firm is not so dominant that it covers the complete market in the first period itself. Thus there exist some customers in the second period who did not buy in the first period. Competitive upgrade discount pricing for upgrades in the second period is valid only when some customers in the second period are first-period customers and some are not.

<sup>Assumption</sup> <sup>2.</sup> Both the incumbent and the entrant firms are active in the second period.

Assumption 2 ensures that both firms are strategic players in the second period such that each firm acquires either some first period customers or some non-first-period customers, or both. Combining Assumptions 1 and 2 with the result of Lemma 2 provides us with a way to further trim the possible market structures with competitive upgrade discount pricing for upgrades. This is formalized in the next result.

<sup>Proposition</sup> <sup>1.</sup> The only possible market structure with competitive upgrade discount pricing for upgrades is ACD.

As a consequence of Proposition 1, we are now left with only one possible market structure that supports competitive upgrade discount pricing for upgrades. The focus of the next section is to analyze this market structure and establish the corresponding profit-maximizing prices of the incumbent and the entrant firms.

## 5. Analysis of the Equilibrium with Competitive Upgrade Discount Pricing for Upgrades

## 5.1. Characterizing the Equilibrium

The methodology of characterizing the subgame perfect equilibrium market structure ACD with competitive upgrade discount pricing for upgrades involves two steps. First, we determine the profit maximizing prices for the incumbent and entrant to implement the market structure. Second, we check that no firm has the incentive to deviate by setting different prices in the second period. For ease of exposition, we define the following notation at the outset. The profits for the entrant and incumbent are $\pi _ { e 2 }$ and $\pi _ { i 2 } ,$ respectively, in the second period; $\pi _ { i 1 }$ represents the first period profit for the incumbent, and $\pi _ { i } = \pi _ { i 1 } + \pi _ { i 2 }$ is its overall profit function across both periods.

The first-period customers are from segments A and C. Because segment B is zero, $M _ { 1 } = M _ { 2 }$ . Hence segments A and C are contiguous and in period 1 customers from both these segments make the “buy from incumbent” decision. The boundary point at the right of the two combined segments is at $M _ { 3 }$ . In period $^ { 2 , }$ the first-period customers split with customers in A making the decision to upgrade to the incumbent’s product and customers in C making the decision to upgrade to the entrant’s product. All customers to the right of $M _ { 3 }$ constitute segment D. These customers buy the entrant’s product at its market price, $p _ { e }$ . To employ the subgame perfect equilibrium concept, we solve the game backwards, $\mathrm { i . e . }$ first we solve the game in the second period and then in the first period. Accordingly, we first determine the second-period prices and the cutoff $M _ { 1 }$ between segments $\mathrm { A }$ and C in the second period given $M _ { 3 }$ . Then the second-period values of prices and market sizes are substituted back in the first-period profit function of the incumbent to determine the equilibrium value of the first-period variables.

Writing the indifference condition between segments A and C in period 2,

$$
M _ {1} = \frac {p _ {d} + s + d - p _ {u}}{2 d}.
$$

The profit functions in period 2 for the incumbent and the entrant, respectively, are

$$
\pi_ {i 2} = p _ {u} \cdot G \left(\frac {p _ {d} + s + d - p _ {u}}{2 d}\right),\tag{5}
$$

$$
\begin{array}{l} \pi_ {e 2} = p _ {d} \cdot \bigg (G (M _ {3}) - G \bigg (\frac {p _ {d} + s + d - p _ {u}}{2 d} \bigg) \bigg) \\ \qquad + p _ {e} \cdot (1 - G (M _ {3})). \end{array}\tag{6}
$$

In the entrant’s profit function note that $\begin{array} { r l } { p _ { e } } & { { } = } \end{array}$ $\mathrm { M i n } [ p _ { i } - d + 2 d \tilde { M _ { 3 } { \prime } } { f _ { u } } - d + d M _ { 3 } ]$ due to the second period IC and IR constraints of the customers in segment D (similar to Equation (1)). We can now solve for equilibrium prices in the second period for a given $\overline { { { M _ { 3 } } } } ^ { \overline { { { \bf \Phi } } } }$ . This then allows us to reformulate the incumbent’s profit function, $\pi _ { i }$ in terms of $M _ { 3 } ,$ which can be expressed in terms of the price $p _ { 1 }$ from Equation (4). Solving for $p _ { 1 }$ gives us the prices required to implement the market structure A, C, D. We state a theorem on the equilibrium prices with an ACD market structure for a distribution on t that is IFR.

<sup>Theorem</sup> <sup>1.</sup> (1) For a given $M _ { 3 }$ and $t \sim I F R ,$ $s < d ( 1 + 2 ( ( 2 - G ( M _ { 3 } ) ) / ( g ( \bar { 1 } ) ) ) )$ is a necessary condition such that there exists a unique set of second-period prices that implements market structure ACD. These prices are

$$
\begin{array}{c} p _ {u} ^ {*} = 2 d \cdot \frac {G (t ^ {*})}{g (t ^ {*})}, \\ p _ {d} ^ {*} = 2 d \cdot \left(\frac {G (M _ {3}) - G (t ^ {*})}{g (t ^ {*})}\right), \quad a n d \\ p _ {e} ^ {*} = f _ {u} - d + d M _ {3}, \end{array}
$$

where t<sup>∗</sup> is the unique solution to the following equation:

$$
t ^ {*} = \left(\frac {1}{2} + \frac {s}{2 d}\right) + \left(\frac {G (M _ {3}) - 2 G x (t ^ {*})}{g (t ^ {*})}\right).
$$

(2) For t ∼ IF R, there exists some price $p _ { 1 }$ and corresponding first-period cut-off $M _ { 3 }$ that implements the market structure ACD.

Although the above result holds for any IFR distribution on t, to check for subgame perfection and perform comparative statics, we need to impose some assumptions on the form of t. Hereon, we assume that t is uniformly distributed between zero and one. The prices that implement market structure ACD for $t \sim \hat { U } n i f o r m [ 0 , 1 ]$ are incorporated in Proposition 2.

<sup>Proposition</sup> <sup>2.</sup> For the parameter range,

$$
\begin{array}{c} f <   d \\ \max \left\{\frac {4 d - f}{5}, \frac {1 1 f + 4 d}{9}, 7 f - 4 d \right\} <   f _ {u} <   4 d - f, \\ \max \left\{\frac {3 f - 1 7 f _ {u} + 1 2 d}{8}, \frac {9 (f + f _ {u}) - 2 4 d}{4} \right\} \\ <   s <   \min \left\{f + f _ {u} - d, \frac {7 f _ {u} - 1 3 f - 2 d}{2} \right\}. \end{array}
$$

The market structure $A , \ C , \ D \ ( M _ { 1 } = M _ { 2 } < M _ { 3 } )$ can be implemented with the entrant using a competitive upgrade discount price for upgrades.

The closed form expressions for prices and corresponding market cutoffs are

$$
\begin{array}{c} p _ {1} ^ {*} = \frac {2 (f + f _ {u} - s - d)}{5}, \\ p _ {u} ^ {*} = \frac {3 (f + f _ {u}) + 2 (s + d)}{1 0}, \\ p _ {d} ^ {*} = \frac {3 (f + f _ {u} - s - d)}{5}, \\ p _ {e} ^ {*} = \frac {9 f + 2 9 f _ {u} - 4 s - 2 4 d}{2 0}, \\ M _ {1} ^ {*} = M _ {2} ^ {*} = \frac {3 (f + f _ {u}) + 2 (s + d)}{2 0 d}, \quad \text {and} \\ M _ {3} ^ {*} = \frac {9 (f + f _ {u}) - 4 (s + d)}{2 0 d}, \end{array}
$$

whereas the above expressions provide profit maximizing prices, incumbent and entrant profits over both periods are obtained by substituting the above prices and market sizes into the profit functions $\pi _ { i }$ and $\pi _ { e } ,$ respectively:

$$
\begin{array}{l} \pi_ {i} ^ {*} (A, C, D) \\ = \frac {4 d ^ {2} + 9 (f + f _ {u}) ^ {2} - 8 d (f + f _ {u} - s) - 8 (f + f _ {u}) s + 4 s ^ {2}}{4 0 d}. \end{array}\tag{7}
$$

$$
\begin{array}{l} \pi_ {e} ^ {*} (A, C, D) \\ = \frac {- 5 0 4 d ^ {2} - 9 (f + f _ {u}) (f + 2 1 f _ {u}) + 4 8 d (6 f + 1 6 f _ {u} - s) + 8 (- 9 f + f _ {u}) + 5 6 s ^ {2}}{4 0 0 d}. \end{array}\tag{8}
$$

Subgame perfection requires that neither the incumbent nor the entrant should have any incentive to deviate from setting the prices reported in Proposition 2 once period 1 has elapsed. Furthermore, customers cannot be cheated because they are forward looking and hence will recognize in the first period itself any incentive of either firm to deviate in the second period and adjust their buying choices accordingly. Hence, we must make sure that any deviations from the pricing reported in Proposition 2 is not profitable for either firm. Specifically, this requires us to consider the following three types of possible deviations:

1. Given the pricing of the incumbent as per the ACD market structure and the first-period indifferent customer indexed by $M _ { 3 } ^ { * }$ , the entrant may deviate and set prices different from $p _ { e } ^ { * }$ and $p _ { d } ^ { * }$

2. Given the pricing of the entrant as per the ACD market structure and the first-period indifferent customer indexed by $M _ { 3 } ^ { * } ,$ the incumbent may deviate by setting a price different from $p _ { u } ^ { * }$ or drop $p _ { i }$ to gain some non-first-period customers.

3. Given the first-period indifferent customer indexed by $M _ { 3 } ^ { * }$ , both the incumbent and the entrant firms may simultaneously deviate to set prices different from $p _ { u } ^ { * } , p _ { e } ^ { * }$ , and $p _ { d } ^ { * }$

We consider each of these possible deviations and report the results in the next proposition.

<sup>Proposition</sup> <sup>3.</sup> There exists a necessary and sufficient parameter range $f o r$ which the equilibrium described in Proposition 2 is subgame perfect.

The parameter range over which the ACD market structure is valid is detailed in the appendix. Because of the results presented in Propositions 1, 2, and $^ { 3 , }$ we can now assert that discount pricing for upgrades is concomitant with only one possible market structure, that of ACD. This shows the implication for market shares in a situation where discount pricing for upgrades is observed. The incumbent adopts pricing strategies that cause it to lose market share in the second period. Typically, firms are wary of giving up their market share but the results establish that this is the optimal strategy for the incumbent. Why is this strategy profitable for the incumbent? Because the incumbent gains a big market share in the first period that it cannot sustain in the face of the competitive upgrade discount pricing policy adopted by the entrant. Furthermore, the incumbent prefers to earn all its revenue in the second period from a part of its old customer base via upgrade pricing rather than engage in wasteful competition for new customers. This occurs because competing for these new customers exerts a downward price pressure on its upgrade price and the incumbent prefers to avoid this effect.

In the next section, we study the comparative statics of the firms’ profits with respect to the switching costs. Henceforth, we refer to the subgame perfect equilibrium with the ACD market structure involving competitive upgrade discount pricing for upgrades as simply the competitive upgrade discount pricing equilibrium.

## 5.2. Impact of Switching Costs on Profits of Incumbent and Entrant

Switching costs can be altered by adopting the appropriate technological configurations. For example, if the incumbent and the entrant firms adopt common file formats, then a customer who switches to the entrant may still be able to manipulate the file in her newly adopted software product, thus reducing switching costs. Consequently, it is of interest to the incumbent and the entrant to know how altering the switching costs may affect their profits. Switching costs increase the affinity of the current customers of an incumbent firm to stay with that firm in the long run. Thus they are likely to buy the upgrade offered by that firm and not switch to the competitor’s product because of the additional switching costs they incur in doing so. The reduced ability of the competitor to offer an attractive deal to the existing customers of the incumbent firm effectively relaxes price competition in the second period and therefore has a positive impact on the incumbent’s profits. However, switching costs may also reduce the profits of the incumbent because forward-looking customers realize in the first period that they will be saddled with higher prices in the second period due to the relaxed price competition (notice that $p _ { u } ^ { * }$ in the competitive upgrade discount pricing equilibrium is increasing in s). Consequently, their willingness to pay for the incumbent’s product in the first period reduces and the incumbent must accordingly lower its price in that period $( { p } _ { 1 } ^ { * }$ in the competitive upgrade discount pricing equilibrium is decreasing in s). The two opposite impacts of switching costs on the incumbent’s profits in the competitive upgrade discount pricing equilibrium points to an interesting comparative statics result.

<sup>Proposition</sup> <sup>4.</sup> In the competitive upgrade discount pricing equilibrium, the incumbent’s profits are reducing with switching costs, s.

This result shows that the negative impact on the incumbent’s profit due to reduction of price in the first period is not fully made up through the higher upgrade price in the second period. This leads to the interesting conclusion that the incumbent firm finds it profit maximizing to minimize the switching costs in the context of the competitive upgrade discount pricing equilibrium. This may seem strange at first, because the entrant provides competitive upgrade discount prices to acquire first-period customers of the incumbent who are bound to the incumbent due to high switching costs. Rather than improve its competitive advantage by further increasing the switching costs, the incumbent is seen to do better by reducing its competitive advantage. The reason is that the forwardlooking behavior of the customer poses more harm than good to the incumbent’s profits in the competitive upgrade discount pricing equilibrium.

In a similar vein as above, one may find the impact of switching cost on the entrant’s profits in the context of the competitive upgrade discount pricing equilibrium. We present that result in the next proposition.

<sup>Proposition</sup> <sup>5.</sup> In the competitive upgrade discount pricing equilibrium, the entrant’s profits are reducing with switching costs s.

We observe that the conventional wisdom that an increase in the switching cost reduces the entrant’s profit by locking customers to the incumbent’s product works well for this situation. The reason is that an increase in switching costs causes the entrant to reduce its prices, $p _ { e } ^ { * }$ and $p _ { d } ^ { * } .$ Also, the market size of segment C reduces whereas that of segment D increases. The increase in size of segment D is due to the forwardlooking behavior of the customers, and less of them buy the incumbent’s product in the first period due to the possibility of facing high prices in the second period. However, this increase in segment D is not sufficient to bolster the lost profits due to decrease in size of segment C and the reduction in prices.

Given the results in Propositions 4 and 5, the similarity in the behavior of the profit functions of the incumbent and the entrant with respect to switching costs may lead to an interesting situation where the incumbent and the entrant firms have similar incentives in product design. To the extent that both of the firms have some influence in deciding on the extent of compatibility of their products and thus the resulting switching costs, it is clear that firms are likely to “cooperate” in the product design stage and then “compete” in the selling stage. Thus, our results point that firms should adopt the “co-opetition” framework in the context of the competitive upgrade discount pricing equilibrium.

## 5.3. Impact of Switching Costs on Consumer Welfare

Switching costs between products of competitors are sometimes perceived as an artificial barrier created by firms to lock in customers to their products. If such a situation prevents customers from adopting their best suited product or causes them to incur wasteful switching costs to switch to a new product, the consumer welfare is likely to be adversely effected. Should the regulators then step in to force the firms to lower switching costs between their products? That the regulating authorities sometimes do so is evident from their decision to force mobile telecommunications firms in the United States to allow number portability if customers decide to change their service providers. Although the context of mobile telecommunications is different from that of software, it does show that questions regarding regulation of switching costs are important ones. In our context, the answer to this question requires the comparative statics of consumer welfare with respect to switching costs in the competitive upgrade discount pricing equilibrium. As Propositions 4 and 5 show, the profits of both the incumbent and the entrant firms decrease with switching costs. Thus it appears that at least in the context of the competitive upgrade discount pricing equilibrium, the incentives of the firms and the regulatory authorities in minimizing the switching costs are in alignment. The next proposition however shows that this is not the case.

<sup>Proposition</sup> <sup>6.</sup> In the competitive upgrade discount pricing equilibrium, consumer welfare is increasing in switching cost, s.

The implications of the above results are that if any regulation is at all needed to increase consumer welfare, it must be to increase rather than decrease switching costs. This happens because increase in switching costs causes the incumbent to respond by reducing the first-period price. This indirect impact is high enough to more than offset any losses in consumer welfare due to increased switching costs. Hence, a social planner may want to increase switching costs. The resulting policy implications are different from those prevalent in other industries such as mobile telecommunications where the regulators reduced switching costs by enforcing number portability.

## 5.4. Impact of Product Improvement Level on Switching Costs

In many settings, the switching cost incurred by a consumer may depend not only on the architectural differences between two competing products but also the incremental product quality obtained as a result of switching to an upgrade. The analysis thus far has been agnostic toward this possibility. To analyze this, we assume that the switching cost s consists of two components $s _ { c }$ and $s _ { c } \cdot h \cdot ( f _ { u } - f )$ such that $s =$ $s _ { c } ( 1 + h \bar { \cdot } ( f _ { u } - f ) )$ . Here, $s _ { c }$ represents the architectural difference in the two products that leads to a switching cost in the first place, and h is an additional nonnegative component of switching cost that increases as the product improvement level increases. Because we have worked out all equilibrium results with a general switching cost term s that may or may not depend on the product improvement level, all our equilibrium outcomes go through as before. The only impact is a scaling and translation of the parameter space. As for the comparative statics developed in the earlier subsections, we need to study them with respect to two parameters, $s _ { c }$ and h. However, the basic insights remain unchanged, as can be seen by evaluating the derivative of any profit function  with respect to s:

$$
\frac {d \pi}{d s _ {c}} = \frac {d \pi}{d s} \frac {d s}{d s _ {c}} = (1 + h (f _ {u} - f)) \frac {d \pi}{d s},
$$

$$
{\frac {d \pi}{d h}} = {\frac {d \pi}{d s}} {\frac {d s}{d h}} = s _ {c} (f _ {u} - f) {\frac {d \pi}{d s}}.
$$

Because $h \geq 0 , s _ { c } \geq 0 ,$ and $f _ { u } - f > 0 ,$ the sign of the derivative of the profit function with respect to the new parameters $s _ { c }$ and h are the same as that of the derivatives with respect to s. Thus the comparative statics remain unchanged with respect to the new switching cost parameters. Thus our model is robust to the incorporation of product improvement effects in the switching cost.

## 6. Model Extensions

Several extensions are possible to our current model of competitive upgrade discount pricing. We study three major extensions: the introduction of a discount factor to utilities, prices, and profits in the second period (thus reflecting the time value of money); the introduction of network externality effects (each user obtains higher utility the greater the number of users using the product); and the arrival of a new customer cohort in the second period. Each extension requires the addition of one new parameter in the model. This adds enormous complexity to the algebra and so in the interest of tractability, we incorporate each of these effects one at a time in the current model. Furthermore, to derive closed form expressions for prices and market shares, we assume that $t \sim U n i f o r m [ 0 , 1 ]$

In each of these extensions we first establish that the equilibrium with competitive upgrade discount pricing for upgrades still has the market structure ACD. This finding is very helpful because the similarity of the market structure leads to the profit functions and the consumer surplus having a similar form as in the original model. Furthermore, because the profits and consumer surplus are continuous functions of the additional parameter introduced by the model extension, we can claim that the comparative statics of the profits and consumer surplus presented in §5 will still hold as long as the newly introduced parameters do not take extreme values.

We start with incorporating a discount factor as our first extension.

## 6.1. Discount Factor in Period 2

We assume that all future period utilities, prices and cash flows in the second period are discounted by a factor 0 We take the same discount factor for the firm and the consumers. Consequently, the total consumer surplus for various options available to the consumer can be written as follows:

1. Buy from incumbent in period 1 and do not buy in period 2. The net surplus is $( 1 + \delta ) f - 2 t d - p _ { 1 }$

2. Buy from incumbent in period 1 and upgrade to the incumbent’s new product in period 2. This gives a total surplus of $f + \delta \cdot f _ { u } - ( 1 + \delta ) t d - p _ { 1 } - \delta \cdot p _ { u } .$

3. Buy from incumbent in period 1 and upgrade to the entrant’s product in period 2. This gives a two period surplus of $f + \delta \bar { \cdot { f _ { u } } } - t d - \delta \cdot ( 1 { \bar { - } } t ) d - p _ { 1 } -$ $\delta \cdot p _ { d } - \delta \cdot s .$

4. Do not buy the incumbent’s product in period 1 and buy the incumbent’s product in period 2. This results in a total surplus of $\delta \cdot f _ { u } - \delta \cdot t d - \delta \cdot p _ { i }$

5. Do not buy the incumbent’s product in period 1 and buy the entrant’s product in period 2. This gives a surplus of $\delta \cdot f _ { u } - \delta \cdot \bar { ( 1 - t ) } d - \delta \cdot p _ { e }$

6. Do not buy the incumbent’s product in period 1 and do not buy any product in period 2 giving a total surplus of zero.

The second-period pricing constraints with a discount factor are the same as in the original problem (given by Equation (1) and the discussion that follows) because decision making in the second period once the first period has elapsed does not require use of the discount factor. Writing out the consumer’s first-period choices as a function of discount factor allows us to evaluate potential market structures at equilibrium where competitive upgrade discount pricing is observed. In particular, we can show that when  is large enough $\begin{array} { r } { ( \hat { \delta } > \frac { 1 } { 2 } ) } \end{array}$ , the ACD market structure is the only viable market structure with competitive upgrade discount pricing. For a yearly interest rate of 5%, the discount factor reaches 0.5 only when the length of the period between upgrades is 15 years. Because upgrades are typically introduced much more quickly than a 15 year interval, we can take ACD market structure as the only viable one with competitive upgrade discounts for upgrades. The prices and market shares that can implement such an ACD equilibrium are

$$
\begin{array}{l} p _ {1} ^ {*} = \frac {5 f - 2 s - 2 d (1 + \delta) ^ {2} + \delta (3 f - 2 s (2 + \delta) + f _ {u} (5 + 3 \delta))}{1 4 + 6 \delta}, \\ p _ {u} ^ {*} = \frac {2 s + 3 f (3 + \delta) + (2 + \delta) (f _ {u} (7 - 3 \delta) + 2 s \delta) + 4 d (- 3 + \delta (3 + 2 \delta))}{4 \delta (7 + 3 \delta)}, \\ p _ {d} ^ {*} = \frac {2 (7 f _ {u} + s) - 2 d (3 - \delta) (2 + \delta) + 3 f (3 + \delta) + \delta ((1 - 3 \delta) f _ {u} - 2 s (5 + 2 \delta))}{2 \delta (7 + 3 \delta)}, \\ p _ {e} ^ {*} = \frac {(3 + \delta) (9 f + 1 4 + 1 5 \delta) f _ {u} - 6 s \delta - 1 2 d (1 + \delta)}{8 \delta (7 + 3 \delta)}, \\ M _ {1} ^ {*} = M _ {2} ^ {*} \\ = \frac {2 s + 3 f (3 + \delta) + (2 + \delta) (f _ {u} (7 - 3 \delta) + 2 s \delta) - 4 d (3 - \delta (3 + 2 \delta))}{8 d \delta (7 + 3 \delta)}, \\ M _ {3} ^ {*} \\ = \frac {6 (7 f _ {u} + s) + 9 f (3 + \delta) - 4 d (9 - \delta (2 + 3 \delta)) - \delta (2 s (8 + 3 \delta) - 3 f _ {u} (1 - 3 \delta))}{8 d \delta (7 + 3 \delta)}. \end{array}
$$

From these expressions, it is easy to observe that setting $\delta = 1$ provides us with the same expressions as in the original ACD equilibrium discussed in §§4 and 5. Thus, the original ACD equilibrium is a limiting case of this model. Because the prices and market sizes are continuous functions of the discount factor $\delta ,$ it is easy to see that the profits of both firms and the consumer surpluses are also continuous functions of the discount factor $\delta .$ Hence, the comparative statics results we obtained earlier will also hold for discount factors that are high enough. Thus all our earlier insights are robust to the incorporation of discount factor in the analysis.

## 6.2. Network Externality

We incorporate network externality in the model by introducing externality parameters  and k in the customer’s utility function. If q customers buy a product of quality $F ,$ then each customer derives an additional utility of $( \gamma + k \cdot F )$ ·q due to network externality effects. Here, k represents that part of network externality that depends on the quality of the product and  represents the quality independent component of these effects. As a result, each customer’s overall surpluses for different options are modified as follows:

1. Buy from incumbent in period 1 and do not buy in period 2. The net surplus is $2 f - 2 t d - p _ { 1 } + ( \gamma + k \cdot f ) \cdot$ $( \hat { M _ { 1 } } + M _ { 3 } - M _ { 2 } ) + ( \gamma + \hat { k } \cdot f ) \cdot \hat { M _ { 1 } } ^ { \dagger } \cdot$

2. Buy from incumbent in period 1 and upgrade to the incumbent’s new product in period 2. This gives a total surplus of $\bar { f } + \bar { f } _ { u } - 2 t d - \bar { p } _ { 1 } - p _ { u } + ( \gamma + \bar { k \cdot } f )$ $( M _ { 1 } + M _ { 3 } { \stackrel { - } { - } } M _ { 2 } ) + ( \gamma + k \cdot f _ { u } ) \cdot M _ { 2 } .$

3. Buy from incumbent in period 1 and upgrade to the entrant’s product in period 2. This gives a total surplus of $\bar { f } + f _ { u } - d - \bar { p } _ { 1 } - p _ { d } - s + ( \gamma \bar { + } k \cdot f )$ $( M _ { 1 } + \bar { M _ { 3 } } - M _ { 2 } ) + ( { \gamma + k \cdot f _ { u } } ) \cdot ( 1 - \bar { M _ { 2 } } ) .$

4. Do not buy the incumbent’s product in period 1 and buy the incumbent’s product in period 2. This results in a total surplus of $\mathsf { \bar { f } } _ { u } - t d - p _ { i } + \mathsf { \bar { ( } } \gamma + k \cdot f _ { u } ) \cdot M _ { 2 } ,$

5. Do not buy the incumbent’s product in period 1 and buy the entrant’s product in period 2. This gives a surplus of $f _ { u } - ( 1 - \hat { t ] } d - p _ { e } + ( \hat { \gamma + k } \cdot f _ { u } ) \cdot ( 1 - \check { M } _ { 2 } )$

6. Do not buy the incumbent’s product in period 1 and do not buy any product in period 2 giving a total surplus of zero.

As before, the second period IC and IR constraints can be rewritten as constraints on second-period prices:

$$
\begin{array}{c} p _ {u} = \text {Min} [ f _ {u} - f + (\gamma + k \cdot f _ {u}) \cdot M _ {2} - (\gamma + k \cdot f) M _ {1}, p _ {d} + d - k \\ \cdot f _ {u} + s - 2 d M _ {1} - (\gamma + k \cdot f _ {u}) \cdot (1 - 2 M _ {2}) ]; \end{array}
$$

$$
\begin{array}{r l} p _ {i} = & \operatorname{Min} [ d + p _ {e} - 2 d M _ {2} + (\gamma + k \cdot f _ {u}) \\ & \quad \cdot (1 - 2 M _ {2}), f _ {u} - d M _ {2} + (\gamma + k \cdot f _ {u}) \cdot M _ {2} ]; \end{array}
$$

$$
\begin{array}{r} p _ {e} = \mathrm{Min} [ p _ {i} - d + 2 d M _ {3} + (\gamma + k \cdot f _ {u}) \\ \cdot (1 - 2 M _ {2}), f _ {u} - d + d M _ {3} + (\gamma + k \cdot f _ {u}) \cdot (1 - M _ {2}) ]; \end{array}
$$

$$
\begin{array}{r l} p _ {d} & = \text {Min} [ p _ {u} - d - s + 2 d M _ {2} + (\gamma + k \cdot f _ {u}) \\ & \quad \cdot (1 - 2 M _ {2}), f _ {u} - f - d - s + 2 d M _ {2} - (\gamma + k \cdot f _ {u}) \\ & \quad \cdot M _ {2} + (\gamma + k \cdot f) M _ {1} ]. \end{array}
$$

Using these consumer rationality constraints in each period, we can show that the only viable market structure with competitive upgrade discount pricing is ACD for sufficiently low network externality effects. The exact condition required for this is  < min $\{ d / 5 ~ - ~ { \textstyle \frac { 3 } { 5 } } k ~ \cdot ~ f ~ - ~ { \textstyle \frac { 2 } { 5 } } k ~ \cdot ~ f _ { u } , { \textstyle \frac { 5 } { 8 } } d ~ - ~ { \textstyle \frac { 9 } { 1 6 } } k$ $\textstyle f - { \frac { 7 } { 1 6 } } k \cdot f _ { u } \}$ . When $k = 0 ,$ , this condition reduces to $\gamma < d / 5$ . Thus, the market structure at equilibrium is preserved with the addition of network externality. The closed form expressions for the prices and market structures for general  and k are quite messy.<sup>8</sup> However, the expressions at $k = 0$ are relatively shorter and are stated below:

$$
\begin{array}{r l} & p _ {1} ^ {*} = (8 (f + f _ {u} - s - d) d ^ {2} - 2 (1 1 f + 1 1 f _ {u} - 1 0 s - 1 4 d) d \\ & \qquad \cdot \gamma + (1 4 f + 1 4 f _ {u} - 1 1 s - 3 1 d) \cdot \gamma^ {2} + 1 1 \gamma^ {3}) \\ & \qquad \cdot (4 (5 d - 8 \gamma) (d - \gamma)) ^ {- 1}; \\ & p _ {u} ^ {*} = \frac {2 d (3 f + 3 f _ {u} + 2 s + 2 d) - (6 f + 6 f _ {u} + 3 s + 7 d) \gamma + 3 \gamma^ {2}}{2 0 d - 1 4 \gamma}; \\ & p _ {d} ^ {*} = \frac {6 d (f + f _ {u} - s - d) - (6 (f + f _ {u}) - 1 3 d - 7 s) \gamma - 7 \gamma^ {2}}{2 (5 d - 8 \gamma)}; \\ & p _ {e} ^ {*} = \frac {1}{1 , 5 3 6} \bigg [ 2 4 (6 f + 7 0 f _ {u} + 9 s + 5 5 \gamma) - 1, 6 9 5 d \\ & \qquad + \frac {1 9 d (1 4 4 f + 1 4 4 f _ {u} - 1 0 4 s - 3 9 d)}{5 d - 8 \gamma} - \frac {1 2 8 s d}{d - \gamma} \bigg ]; \\ & M _ {1} ^ {*} = M _ {2} ^ {*} = \frac {1}{1 9 2} \bigg [ 2 7 \frac {1 4 4 f + 1 4 4 f _ {u} - 1 0 4 s - 3 9 d}{1 0 d - 7 \gamma} + \frac {4 0 s}{d - \gamma} \bigg ] \\ & M _ {3} ^ {*} = \frac {1}{6 4} \bigg [ \frac {1 4 4 f + 1 4 4 f _ {u} - 1 0 4 s - 3 9 d}{5 d - 8 \gamma} + \frac {8 s}{d - \gamma} - 5 \bigg ]. \end{array}
$$

Substituting the value of $\gamma = 0 ,$ we get back the original (without network externality) prices and market shares. Thus, the original ACD equilibrium is a limiting case of this model and is obtained by setting both  and k to zero. Furthermore, the profits for both firms and consumer surpluses are continuous functions of the network externality parameters  and k. Hence the comparative statics results we obtained earlier will also hold for low enough network externalities. Thus all our earlier results are robust to the incorporation of network externalities.

## 6.3. New Consumer Cohort in Period 2

In all previous cases, we assumed that the total number of consumers remained static across both periods and there were no new consumers. In many realworld settings, this may not hold as new customers enter the market in later time periods. We incorporate this fact into the basic model. We normalize the sum total of the customer population in both periods to one. Let  be the size of the customer population in period 1 (where $0 \leq \alpha \leq 1 )$ and 1 −  be the size of the new customer population that arrives in period 2. This implies that as we set  = 1, we get back our original problem with no new customers entering the market in period 2. A few basic results can be shown for all values of  in the range 601 17. First, we can rule out the market structure ABCD because the system of equations encapsulating the IR and IC conditions in the second period are a superset of the system of equations in the original model. Consequently, we have a more constrained system of equations. Because the system for the original model had no solution where all four segments A, B, C, D coexist (Lemma 2), the current system of equations must have no solution as well. Thus we have the nonexistence of equilibrium with an ABCD market structure in the old market. Furthermore, applying Assumptions 1 and 2 along with the nonexistence of ABCD ensures that the only market structure in the old customer market that supports competitive upgrade discount pricing is ACD. Given that the ACD market structure holds for the old customer market, as  decreases from one the equilibrium pricing structure does not change from that for the original problem as given in Proposition 2 until  hits a threshold value. Because prices and market shares are the same as in the original problem for high enough , the profits of both firms and consumer surpluses are continuous functions of . Consequently, the comparative statics results of the original problem continue to hold for sufficiently numerous first period customers.

## 7. Conclusions

## 7.1. Discussion

We analyze competition between firms that provide a software product upgrade. This is a significant leap with respect to the extant literature that considers only a monopoly firm providing such upgrades. Because competition is pervasive in software product markets (several examples are provided in the introduction section of the paper), our paper is a more realistic representation of these markets. The competitive aspect allows us to incorporate a new form of BBPD called competitive upgrade discount pricing, where the price discount is available to even previous customers of the firm’s competitor. We then investigate the nature of the equilibrium that supports competitive upgrade discount pricing in detail. Clearly, such a situation does not exist for a monopoly because competitive upgrade discount price does not have any meaning in that context. The equilibrium with such pricing has several unique features. At this equilibrium, an extreme form of “fat cat” behavior by the incumbent is optimal; it will even cede a portion of the market share it acquired in the first period. Furthermore, the profits of both the incumbent and the entrant are decreasing in switching costs at this equilibrium. The incumbent’s profit is decreasing in switching costs because forward-looking customers are able to anticipate this switching cost and this exerts downward pressure on the incumbent’s first-period pricing. The entrant’s profit is decreasing in switching costs because switching costs compel the entrant to provide a deeper discount to first period customers. Because of this impact of switching costs, the competing firms have the incentive to design their products in a way so that these costs are reduced. Thus there are product design implications of our work. Switching costs impact consumer welfare as well. The entrant’s decision to use competitive upgrade discounts to induce some customers to upgrade to its product results in deadweight loss because these customers have to incur switching costs. Although this undermines consumer welfare, the increased competition in the second period exerts downward pressure on the incumbent’s first-period price. This increases the total number of customers who can use the product in period 1 and consequently, there is an overall positive impact on consumer welfare. Hence, a social planner may want to increase switching costs. The resulting policy implications are different from those prevalent in other industries such as mobile telecommunications where the regulators reduced switching costs by enforcing number portability.

We also extend this model to take into account the addition of a discount factor to all prices and cash flows in the second period, the addition of network effects and the introduction of a new cohort of customers in the second period. In each of these extensions, we emphasize the robustness of the equilibrium market structure for the original customer market for reasonable ranges of the new parameters. We also show how price and market share expressions in the original problem form a special case of the prices and market shares in the extended models.

Our paper has methodological implications as well. The identification of a pure strategy subgame perfect equilibrium is significantly more difficult in a competitive situation. This is due to two reasons. First, customer behavior is much more complicated leading to the possibility of multiple market structures and hence multiple potential equilibria. Consequently, one must identify the genuine equilibria from the numerous confounding candidates. Second, because both firms simultaneously set prices in the second period, we need to ensure that neither firm has the incentive to deviate from these prices. Because of multiple market structure possibilities in the second period, deviations in prices can result in discontinuities in the profit function. As a result, establishing deviationproof second-period prices is a difficult and involved exercise. In taking care of the above two issues, our paper clearly demarcates a methodological direction for analytical game-theoretic research in the context of competition with product upgrades.

## 7.2. Future Research

Our model examines a specific context involving discount pricing for upgrades: one in which there is an incumbent firm in the first period that is followed by an entrant leading to competition in the second period. Whereas there are several situations where such a model is applicable, there may be other settings where upgrade discounts may be useful. For example, there may be competition in both periods and both firms may offer competitive upgrade discounts to its competitors’ previous customers. Another issue that merits attention is to consider quality decisions by the competing firms. Depending on the cost of doing research and development, this could lead to interesting product design implications. These and other related questions await future research.

## Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http://isr.journal .informs.org/.

## References

Acquisti, A., H. Varian. 2005. Conditioning prices on purchase history. Marketing Sci. 24(3) 367–381.

Arora, N., X. Dreze, A. Ghose, J. D. Hess, R. Iyengar, B. Jing, Y. Joshi, et al. 2008. Putting one-to-one marketing to work: Personalization, customization, and choice. Marketing Lett. 19(3–4) 305–321.

Bala, R., S. Carr. 2009. Pricing software upgrades: The role of product improvement and user costs. Production Oper. Management 18(5) 560–580.

Beggs, A., P. Klemperer. 1992. Multi-period competition with switching costs. Econometrics 60(3) 651–666

Brehm, J. W. 1956. Post decision changes in the desirability of alternatives. J. Abnormal Soc. Psych. 52(3) 384–389.

Cabral, L., M. Villas-Boas. 2005. Bertrand supertraps. Management Sci. 51(4) 599–613.

Chen, Y., C. Narasimhan, Z. J. Zhang. 2001. Individual marketing with imperfect targetability. Marketing Sci. 20(1) 23–41.

Choi, J. P. 1994. Network externality, compatibility choice, and planned obsolescence. J. Indust. Econom. 42(2) 167–182.

Choudhary, V., A., Ghose, T. Mukhopadhyay, U. Rajan. 2005. Personalized pricing and quality differentiation. Management Sci. 51(7) 1120–1130.

Demirhan D., V. Jacon, S. Raghunathan. 2007. Strategic IT investments: The impact of switching cost and declining IT cost. Management Sci. 53(2) 208–226.

Dhebar, A. 1994. Durable-goods monopolists, rational consumers, and improving products. Marketing Sci. 13(1) 100–120.

Ellison, G., D. Fudenberg. 2000. The neo-luddite’s lament: Excessive upgrades in the software industry. RAND J. Econom. 31(2) 253–272.

Erat, S., S. Kavadias. 2006. Introduction of new technologies to competing industrial customers. Management Sci. 52(11) 1675–1688.

Essegaier, S., S. Gupta, Z. J. Zhang. 2002. Pricing access services. Marketing Sci. 21(2) 139–159.

Farrell, J., C. Shapiro. 1988. Dynamic competition with switching costs. RAND J. Econom. 19(1) 123–137.

Fudenberg, D., J. Tirole. 1998. Upgrades, trade-ins and buybacks. RAND J. Econom. 29(2) 235–258.

Fudenberg, D., J. Tirole. 2000. Consumer poaching and brand switching. RAND J. Econom. 31(4) 634–657.

Fudenberg, D., M. Villas-Boas. 2006. Behavior-based price discrimination and customer recognition. T. Hendershott, ed. Economics and Information Systems. Elsevier, Amsterdam, 377–436.

Gans, N. 2002. Customer loyalty and supplier quality competition. Management Sci. 48(2) 207–221.

Ghose, A., A. Sundararajan. 2005. Software versioning and quality degradation? An exploratory study of the evidence. Working paper, Stern School of Business, New York University, New York.

Ghose, A., T. Mukhopadhyay, U. Rajan. 2007. The impact of Internet referral services on a supply chain. Inform. Systems Res. 18(3) 300–319.

Hart, O., J. Tirole. 1988. Contract renegotiation and Coasian dynamics. Rev. Econom. Stud. 55(4) 509–540.

Kamrad, B., A. Siddique. 2004. Supply contracts, profit sharing, switching, and reaction options. Management Sci. 50(1) 64–82.

Kennan, J. 2001. Repeated bargaining with persistent private information. Rev. Econom. Stud. 68(4) 719–755.

Kim, J. 2007. The intensity of competition in the Hotelling model: A new generalization and applications. MPRA Working paper,

Klemperer, P. 1987a. Entry deterrence in markets with consumer switching costs. Econom. J. 97(Suppl.) 99–117.

Klemperer, P. 1987b. Markets with consumer switching costs. Quart. J. Econom. 102(2) 375–394.

Klemperer, P. 1989. Price wars caused by switching costs. Rev. Econom. Stud. 56(3) 405–420.

Klemperer, P. 1995. Competition when consumers have switching costs: An overview with applications to industrial organization, macroeconomics and trade international. Rev. Econom. Stud. 62(4) 515–539.

Lariviere, M. 2006. A note on probability distributions with increasing generalized failure rates. Oper. Res. 54(3) 602–604.

Levinthal, D., D. Purohit. 1989. Durable goods and product obsolescence. Marketing Sci. 8(1) 35–56.

Lu, Q., S. Moorthy. 2007. Coupons versus rebates. Marketing Sci. 26(1) 67–82.

Marinoso, B. G. 2001. Technological incompatibility, endogenous switching costs and lock-in. J. Indust. Econom. 49(3) 281–298.

Moorthy, S., I. Png. 1992. Market segmentation, cannibalization, and the timing of product introductions. Management Sci. 38(3) 345–359.

Nahm, J. 2004. Durable goods monopoly with endogenous innovation. J. Econom. Management Strategy 13(2) 303–320.

Narasimhan, C. 1984. A price discrimination theory of coupons. Marketing Sci. 3(2) 128–147.

Padmanabhan, V., S. Rajiv, K. Srinivasan. 1997. New products, upgrades and new releases: A rationale for sequential product introduction. J. Marketing Res. 34(4) 456–572.

Pazgal, A., D. Soberman. 2008. Behavior-based discrimination: Is it a winning play, and if so, when? Marketing Sci. 27(6) 977–994.

Raghunathan, S. 2000. Software editions: An application of segmentation theory to the packaged software market. J. Management Inform. Systems 17(1) 87–113.

Sankaranarayanan, R. 2007. Innovation and the durable goods monopolist: The optimality of frequent new-version releases. Marketing Sci. 26(6) 774–791.

Shi M., J. Chiang, B. Rhee. 2006. Price competition with reduced consumer switching costs: The case of “wireless number portability” in the cellular phone industry. Management Sci. 52(1) 27–38.

Shin, J., K. Sudhir. 2007. A customer management dilemma: When is it profitable to reward one’s own customers? Marketing Sci. 29(4) 671–689.

Stylus Studio. 2008. Accessed May 2008, https://www.stylusstudio .com/buy/upgrade.html.

Sundararajan, A. 2004. Managing digital piracy: Pricing and protection. Inform. Systems Res. 15(3) 287–308.

Terwiesch, C., S. Savin, I.-H. Hann. 2005. Markets with consumer switching costs. Management Sci. 51(3) 339–351.

Van Ackere, A., D. J. Reyniers. 1995. Trade-ins and introductory offers in an monopoly. RAND J. Econom. 26(1) 58–74.

Villas-Boas, M. 2004. Price cycles in markets with customer recognition. RAND J. Econom. 35(3) 486–501.

Viswanathan, S. 2005. Competing across technology-differentiated channels: The impact of network externalities and switching costs. Management Sci. 51(3) 484–496.

Waldman, M. 1993. A new perspective on planned obsolescence. Quart. J. Econom. 108(1) 273–283.

Waldman, M. 1996. Obsolescence and the R&D decision. RAND J. Econom. 27(3) 583–595.

Zhang, J. 2010. The perils of behavior-based personalization. SSRN working paper, http://papers.ssrn.com/sol3/papers .cfm?abstract\_id=943353.
