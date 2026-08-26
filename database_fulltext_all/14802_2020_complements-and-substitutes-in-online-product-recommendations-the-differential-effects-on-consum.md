---
otero_id: 14802
otero_key: "7ZFB8JQ6"
title: "Complements and substitutes in online product recommendations: The differential effects on consumers’ willingness to pay"
authors: "Mingyue Zhang; Jesse Bockstedt"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2020.103341"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Journal Pre-proof

Complements and Substitutes in Online Product Recommendations: The Differential Effects on Consumers’ Willingness to Pay

Mingyue Zhang, Jesse Bockstedt

![](/api/attachments/7ZFB8JQ6/fulltext/images/57213c7ffd27f82a93e97d8f96687a11e2b0dcbb219c1349948c56b9ea8f6913.jpg)

PII: S0378-7206(20)30279-2

DOI: https://doi.org/10.1016/j.im.2020.103341

Reference: INFMAN 103341

To appear in: Information & Management

Received Date: 21 August 2018

Revised Date: 26 May 2020

Accepted Date: 18 June 2020

Please cite this article as: Zhang M, Bockstedt J, Complements and Substitutes in Online Product Recommendations: The Differential Effects on Consumers’ Willingness to Pay, Information and amp; Management (2020), doi: https://doi.org/10.1016/j.im.2020.103341

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

# Complements and Substitutes in Online Product Recommendations: The Differential Effects on Consumers’ Willingness to Pay

(Authors’ names blinded for peer review)

Mingyue Zhang<sup>1</sup>

School of Business and Management, Shanghai International Studies University

1550 Wenxiang Road, Shanghai 201620, P.R. China

Email: zhangmy@shisu.edu.cn

Telephone: (+86) 130-7013-2177

Jesse Bockstedt

Goizueta Business School, Emory University

1300 Clifton Road, Atlanta, GA 30322, United States

Email: bockstedt@emory.edu

Telephone: (+1) 404-727-6628

<sup>1</sup> The corresponding author: zhangmy@shisu.edu.cn (Mingyue Zhang)

## ABSTRACT

Online product recommendations have been shown to influence consumers’ preferences and purchasing behaviors for recommended products. However, it remains an open empirical question whether and how recommendations of other products affect a consumer’s economic behavior for a focal product. In many e-commerce websites, a product is presented with copurchase and co-view recommendations, which potentially contain complementary and substitutable products, respectively. Very little research has explored differential effects of recommending complementary and substitutable products. In this study, we explore how types of other recommended products impact consumers’ willingness to pay for a focal product through interactions with prices of recommended products and consumers’ decision stages. We conducted a 2<sup>3</sup> randomized factorial experiment as well as two 2 x 2 experiments to examine these issues. Experimental results provide evidence that there is a significant interaction effect between the recommendation type and decision stage, which highlights the importance of recommendation timing on e-commerce platforms. Furthermore, it also illustrates that the effect of recommending complementary vs. substitutable products is subject to contextual factors such as consumers’ decision stages. Results of our study have significant implications for the design and application of online recommender systems.

Key words: complements; substitutes; willingness to pay; decision stage; online product recommendations; laboratory experiments.

## INTRODUCTION

Recommender systems have become integral to how consumers discover new products and have a strong influence on what consum s buy and view online. For instance, 60% of Netflix content consumption originates from re mendations, and 35% of Amazon sales are attributed to recommendations (Hosanagar et al. 2014). With the utmost importance of recommender systems for retailers, some research has shown behavioral effects of recommender systems on consumer decisions (Adomavicius et al. 2013, 2017). Specifically, prior studies have found that consumers’ preferences and willingness to pay (WTP) of products can be influenced by values displayed in personalized recommendations, and suggest that consumers’ behaviors are vulnerable toward recommendation agents. This nascent stream of research opens up many

opportunities for understanding behavioral effects of detailed features of online product recommendation. However, previous research has mainly focused on how recommender system characteristics impact the choice of specific products being recommended in isolation (Häubl and Trifts 2000; Ho et al. 2011; Oestreicher-Singer and Sundararajan 2012a). Actually, many online platforms present recommended alternative products on the same page as a specific focal product. Little research has considered the impact of recommending these related and

Consumers are often exposed to multiple relevant product recommendations when evaluating the information of a focal product. Throughout the paper, “focal product” refers to the product placed in the main section of the webpage that consumers are currently inspecting or considering to purchase (Dhar et al. 2014; Shocker et al. 2004). “Other recommended products” refer to products that are presented as contextual information on the same page as a focal product. For example, on an Amazon.com product page, the platform recommends related products that other people have viewed or purchased. Only limited research in the offline context (Shocker et al. 2004) has explored whether consumers’ purchase decisions, such as WTP of the focal product, are affected by the display of other relevant products and the type of information presented with these products. It remains an open empirical question whether these effects exist in the modern online recommender system context.

![](/api/attachments/7ZFB8JQ6/fulltext/images/2e16c0daf7c21ade0cc4038c2f18f29dcaa049971531d5af54c3a4f1582d07ec.jpg)  
Figure 1. Example of Focal Product and Other Product Recommendations on Amazon.com

The types of “other products” in a recommendation set may vary, but they can be generally categorized into substitutable products and complementary products (McAuley et al. 2015). Substitutes are products that can be purchased instead of each other, while complements are products that experience joint demand. In a typical recommendation system, both substitutes and complements may serve as good recommendation candidates. For example, when a user is evaluating a smartphone, it is reasonable to recommend other phones to better match her/his needs; it also makes sense to recommend headphones, chargers, or cases, which commonly

make up a bundle recommendation (Zhu et al. 2014). While existent studies on recommender systems emphasize advancing sophisticated algorithms to improve the recommendation accuracy, simply relying on the weight of predicted preference as a scalar number may cause apparent misadvising (Zheng et al. 2009). Without considering the complement-substitute relationship between other recommended products and a focal product, we may get unexpected effects on consumer behavior. For instance, a consumer in the final purchasing stage for a camera may find recommendations for other cameras redundant and unnecessary. Alternatively, a consumer who is earlier in the search process for a camera may focus more on comparing different brands and would consider the recommendation of a camera accessory, such as a tripod, as disruptive. This practice of recommending complement products (e.g., camera accessories) and substitute products (e.g., alternative cameras) is used widely in practice (see Figures 2 and 3) and there is an intuitive sense that these recommendation strategies may fit better with different purchasing scenarios. However, this consideration of recommendation strategy (complements vs. substitutes) seems to be largely underutilized in practice and underresearched in academia.

Clearly, these two types of recommendations of “other products” may have different influences on consumers’ perceptions of the focal product. Research has shown that consumers take into account the source or type of information when making their purchase decisions (Rao and Sieben 1992). Economic theory suggests that complements increase demand in market level for the focal product because they increase the possibility of users finding added value for the focal product (Shocker et al. 2004); whereas, substitutes decrease demand for the focal product because of competition. A handful of technical papers have developed algorithms to infer and distinguish these two types of recommendations (McAuley et al. 2015). Moreover, it has also been shown that modeling such relationships significantly improves the accuracy of recommendations (Zhao et al. 2017). Despite the extensive literature about complements and substitutes in economics and these papers that consider complements and substitutes in

recommendation algorithms, little research has studied differential effects of these other product recommendations on individual consumers’ purchase decisions.

Contextual information has been shown to have an important influence on consumer purchase decisions (Rajendran and Tellis 1994), and the price of a recommended product can be perceived as a contextual reference point. Along with the nature of cross-price elasticity of demands between complementary/substitutable goods (Mulhern and Leone 1991), the research question of how prices interact with recommendation type is of great value. It motivates us to ask the question: will the standard theory that complements/substitutes promote cross purchase with controlled prices still apply in complex e-commerce environments such that thousands of available products are accessible at a low cost? Online retailers can use such insights to optimize their display of product recommendations. Additionally, literature shows that the timing of recommendation has great influence on consumers’ preferences (Ho et al. 2011). Generally, recommended items presented in the later stage of purchase are more likely to match a consumer’s interests because recommendation agents increasingly capture consumers’ behavioral actions. But it is also less likely to be attractive compared with the best item encountered so far. If the recommendations are presented earlier, opposite observations would be expected. However, with the consideration of different types of recommendations, contradictory effects may be relieved. Recommending complementary products later can better match consumers’ interests and has little conflict with their current demand at the same time. But it is still unclear how timing interacts with recommendation type (i.e., complements or substitutes), particularly the effect on consumers’ economic behaviors for focal product. According to consumer search theory, the consumer decision-making process is often generalized into two stages<sup>2</sup> (Häubl and Trifts 2000). First, consumers screen a large set of available products to identify a subset of the most promising alternatives; and second, they

evaluate each product in this subset in more depth to make a final purchase decision. The two decision stages of consumers are good indicators of recommendation timing. Zheng et al. (2009) argue that consumers prefer different recommendations in each stage because they are driven by different goals in each stage, i.e., in stage 1 they are comparing alternatives, whereas in stage 2 they are reviewing candidates. For this reason, we expect the decision stage to be closely intertwined with the effect of complementary/substitutable product recommendations. This has not been studied previously and will also provide important insights into online retailers for the display of product recommendations. In this research, we use controlled experiments to isolate key factors in these recommendation scenarios (i.e., recommendation type, prices of recommended products, and decision stage of the purchase process) and explore how prices of recommended products and consumers’ decision stages interact with recommendation type to impact consumers’ WTP for a focal product.

The remainder of the paper proceeds as follows. We first introduce the theoretical underpinnings of this research, based on which two hypotheses are proposed. Then, we discuss the design of a randomized factorial laboratory experiment, in which we measure consumers’ WTP across different recommendation scenarios. We present results of our analyses and further conduct two additional experiments as robustness checks. Consequently, we discuss implications for online retail practices and research involving recommender systems. The investigation provides a new angle for understanding the behavioral impact of recommender systems, as well as guidelines to further improve the design of recommendation agents.

## THEORETICAL FRAMEWORK AND HYPOTHESES

Current studies on inter- and cross-category effects emphasize the impact of one product on the sale of the other (Jiang et al. 2015). Economic theory differentiates this impact associated with “other products” by classifying them into two typical categories, that is, complements and substitutes (Shocker et al. 2004). In an e-commerce context, it becomes much easier to co-

display a focal product with complementary/substitutable “other products” through recommender systems. However, most of the previous research puts great effort into examining the impact of recommendations on consumers’ purchase decisions regarding products being recommended (Häubl and Trifts 2000; Ho et al. 2011; Oestreicher-Singer and Sundararajan 2012a), and fails to consider the effect of other recommended products on the focal product. Thus, the focus in this paper is to investigate differential effects of complementary and substitutable recommendations on consumers’ WTP of a focal product through interactions with contextual factors in a recommendation scenario.

Recommendations are naturally coupled with price decisions from the perspective of product promotions (Jiang et al. 2015). Research has shown that manipulating price levels can affect consumer purchasing patterns and stimulate sales of “other products” (i.e., complements, substitutes, and unrelated products) in offline settings (Leeflang and Parreño-Selva 2012; Walters 1991). Hence, prices of “other products” in online recommendations may influence a consumer’s perceptions of the focal product by putting them side by side for comparison. Furthermore, in economics complements and substitutes are usually defined in terms of extant cross-price elasticity measures (Shocker et al. 2004), which indicates that inter- and crosscategory effects largely depend on products’ respective price levels. In this sense, it is expected that price will interfere with the type of recommendations, and therefore must be considered. Additionally, recommendations of complement and substitute products trigger different information processing when being displayed with the focal product. Substitutes can alter the desirability of focal product because they provide alternative options. Complements, on the other hand, can enhance the feasibility of focal product by introducing additional opportunities for value through the use of the focal and complementary products in combination. Specifically, desirability refers to benefits of using the product (i.e., value of the end state), which is the superordinate “why” aspects or reasons for choosing this product (Hamilton and Thompson 2007; Thompson et al. 2009). When consumers choosing among alternatives/substitutes, they will attend primarily to outcomes they anticipate from each (Cohen et al. 2008) of the products. For example, when consumers are inspecting a computer display, recommending alternative displays of other brands will naturally trigger them to compare those similar items. The advantages and disadvantages of the focal display are more prominent under such recommendations, and as a result, consumers put more consideration to the desirability of focal product. Feasibility refers to the process of using the product (i.e., ease of reaching the desired end state), which is the subordinate “how” aspects for using it (Hamilton and Thompson 2007; Thompson et al. 2009). Complementary items encourage consumers to think about how easy or difficult it will be and how many different ways there are to use the focal product to achieve product-relevant goals. Thus, recommending complements allows consumers to give more appropriate consideration to the use feasibility of product. Use the above example as an illustration, when consumers are inspecting a computer display, recommending connection wires will remind them how to use the display and how many different types of interfaces that are compatible to the display (i.e., feasibility). Construal level theory (Liberman et al. 2007) informs how these different types of recommended products could fit with a consumer’s purchasing stage. Construal level theory contends that high-level construal (thinking abstractly and looking at the bigger picture) corresponds with desirability while low-level construal (thinking concretely and being focused) corresponds with feasibility (Liberman and Trope 1998; Vallacher and Wegner 1987). Prior research has shown that a consumer’s construal level changes from high to low as their decision stages evolve in the online shopping process and they approach the final purchase decision (Lee and Ariely 2006). Thus, we expect that the effects of recommending complement or substitute products will be closely intertwined with consumers’ decision stages in the online purchasing process.

In the following, we discuss and expand on the relevant theoretical foundations that underpin the focus of our research, namely interaction effects of (1) prices of the other recommended products and recommendation type, and (2) consumers’ decision stages in the online purchase process and recommendation type, on consumers’ perceptions of a focal product. First, we review research on complementary/substitutable goods in marketing literature as well as related empirical studies in recommender system context. Second, we discuss theories describing how the price of one product might influence consumers’ WTP of another product depending on their relationships (i.e., complementary or substitutable). Finally, we discuss the related literature on consumer decision-making process and how this interacts with recommender systems.

Complements and Substitutes in Product Recommendations The study of complements and substitutes has long been a central subject in the marketing literature. Generally, products are considered complements (substitutes) if lowering (raising) the price of one product leads to an increase in sales of another (Shocker et al. 2004). Research shows that a consumer’s choice is easily influenced by context and the set of alternatives available at the time of decision (Payne et al. 1992), thus, there is a significant demand for interrelationship among substitutable and complementary goods (Mulhern and Leone 1991). Generally, two moderate or strong substitutes should be offered separately, whereas two complements should be offered as a bundle (Venkatesh and Kamakura 2003), to maximize profit. This is because the introduction of a complement may increase the possibility of buyers finding new uses or added value for existing products (Shocker et al. 2004), whereas substitutes can be consumed or used in place of one another. It has also been argued that displaying complementary goods produces superadditive utility and displaying substitutable goods produces sub-additive utility (Venkatesh and Kamakura 2003).

In the online recommendation scenario, a focal product is often presented with several recommendations of related items. Take Amazon.com as an example, where each product is featured on its own designated product page that contains detailed product information and reviews along with additional recommendations of other relevant products. Hence, a visible directed product network is created whereby products are explicitly connected by recommendation hyperlinks (Lin et al. 2017). Many e-commerce websites provide recommendations from two product networks: co-view and co-purchase product networks. Coview (co-purchase) products are products that many other consumers who viewed (purchased) the focal product have also viewed (purchased).

A few studies (Dhar et al. 2014; Oestreicher-Singer and Sundararajan 2012a, 2012b) have examined the behavioral impacts of recommendation networks with the primary focus on the co-purchase recommendation network. Only recently have their differential effects been considered (Lin et al. 2017). Importantly for our empirical context, co-purchase and co-view networks can be used to represent two recommendation strategies, that is, recommending complementary and substitutable products, respectively. Although not always the case, it is common that a co-purchased item set contains complementary products while a co-viewed product set contains substitutable products. For example, a consumer buying a laptop computer may view several laptops, but purchase only one laptop along with a complementary mouse, software, screen protector, or other accessories. Figures 2 and 3 provide an example to this extent with the co-purchase and co-view recommendations displayed on the Amazon.com product page for a Dell Inspiron 15 i5558-5718SLV laptop. Prior research in recommender system algorithm design has even used the co-purchase and co-view recommendations as the ground truth of complementary and substitutable product pairs in data experiments, such as McAuley et al. (2015) and Zhao et al. (2017).

![](/api/attachments/7ZFB8JQ6/fulltext/images/e79112809b743def6af0131846816f674a2f9835aeecc33cf1b8200a5fbd1a3d.jpg)  
Figure 2. Amazon Co-purchase Product Recommendations.

![](/api/attachments/7ZFB8JQ6/fulltext/images/363ca88108ed065cabb5a73ce1659faf4d67db19486fa79d05d6596f21eb5af4.jpg)  
Figure 3. Amazon Co-view Product Recommendations.

By definition, in microeconomics, if product A and B are complements, increased demand for product A is associated with increased demand for product B (Kotler and Armstrong 2010). This complementary product effect leads to the co-purchase network on platforms like Amazon.com. On the other hand, substitutable products have an inverse demand relationship. This leads to the co-view network because consumers tend to view and compare substitutes before making final purchase decisions. Given that recommendations of both complements and substitutes are typically presented along with the focal product on these platforms, it is of significant interest to understand their differential effects on consumer purchase decisions. Although prior literature has examined the cross-elasticity of demand differences at market level for complements and substitutes, no prior research has considered how recommendations of

complementary and substitutable products differently affect an individual’s purchase decision of a focal product. Furthermore, the substantial differences between e-commerce and traditional shopping environments motivate the need to explore these relationships.

Moreover, the WTP is the maximum price a consumer will pay for one unit of a product (Varian 1992), while the demand function is a price response function that links the behaviors of millions of customers to a given price. In other words, millions of unique consumer decisions based on her/his individual WTP shape the demand function (Koçaş and Dogerlioglu-Demir 2014). Thus, we expect recommendations of complements and substitutes to have differential effects on an individual’s WTP. Contextual factors in a recommendation scenario such as product’s price and consumer’s decision stage are naturally coupled with recommendation type to take effects. We address the interaction effects between recommendation type and these two factors in next subsections.

## Pricing

Researchers in marketing and economics have long recognized that pricing decisions sometimes incorporate more than one product. This is because consumers tend to respond to price relative to reference prices (Rajendran and Tellis 1994), such as prices of other available products in a store at the point of purchase. Both prospect theory (Kahneman and Tversky 1979) and mental accounting theory (Thaler 1985) suggest that consumers make decisions based on losses or gains relative to a reference point. When consumers compare the actual price of the focal product with other reference prices, incidental price learning (Nunes and Boatwright 2004) occurs without any explicit intention to memorize specific prices. Researchers argue that consumers evaluate price attractiveness by comparing the reference price against the offered price of a specific product, in a specific purchasing context, at a specific time (Goh and Bockstedt 2013; Niedrich et al. 2001). Specifically, reference price plays a primary role in the formation of price fairness perception and purchase intentions of consumers (Shapiro et al. 2016).

In offline physical stores, retailers can attempt to positively influence the degree to which the sales of one item affect sales of other items through in-store product locations and shelf space allocations, for example, locating two complements together. This is highly similar to our online product recommendation context where other products are codisplayed, with prices, alongside the focal product on its product page. When evaluating the focal product, prices of displayed, recommended products have the potential to act as the reference point upon which a consumer may base her/his decision to make a purchase. Thaler (1985) proposed a model in which consumers obtain “transaction value” by comparing reference prices with actual prices. It is positive if the actual price is less than the reference price, and negative if the actual price is more than the reference price. As a result, consumers’ perceived transaction value for the focal product differs when the codisplayed recommendations have lower or higher prices than the focal product. The formation of consumers’ WTP is based on the value assessment that reflects both the product’s acquisition value and the transaction value (Simonson and Drolet 2004). That is to say, higher consumers’ perceptions of a product’s total value will be expressed as a higher WTP for the product. Thus, as a general hypothesis around the effect of price, we expect that when the recommended “other product” has a higher price than the focal product, consumers will perceive a higher value for the focal product (i.e., obtain a positive transaction value through comparison to the reference price of the recommended product). This should result in a higher WTP for the focal product as compared to the situation where the recommended product has a lower price than the focal product. Multiple-product pricing is a common strategy, which concerns how the price of one item can influence the sales of another item, either in the same product line (i.e., substitutes) or in a different product line (i.e., complements). Given that the price of a recommended product has a positive impact on consumers’ WTP for the focal product through the mechanism of reference

##

price, the magnitude of its impact may be moderated by the relationship between the focal product and recommended product. As meaningful information about market prices, prices of the same product, or product in the same category will magnify the reference price effect (Nunes and Boatwright 2004). In this sense, we expect that prices of substitutable recommendations will have a stronger positive effect because they are generally from the same category with the focal product and have a high comparability. Furthermore, as we have known, there are significant cross-price elasticity among sales of substitutable and complementary products in the market level (Mulhern and Leone 1991). In particular, basic economic theory tells us that a lower price or promotion of one product can stimulate sales of a complement, whereas supplant sales of other substitutes. That is to say, when the price of a good goes down, we expect demand for that good to increase as well as demand for complementary goods. The demand for substitutable goods is expected to go down (Jin 2006), because the focal good becomes a better deal. This demand effect is expected to play a role in the market regardless of whether or not the two complementary or substitutable goods are presented together to the consumer.

In an online shopping environment, when complementary/substitutable goods are provided as recommendations, they are codisplayed with the focal product on the same webpage. It is worth noting that the focal product and recommended products are complementary or substitutable to each other. That is to say, it is a mutual relationship between complements/substitutes. Thus, lowering or increasing the price of a recommended product should influence demand for the focal product based on their cross-price elasticity of demand as discussed above. When recommended products and focal product are complements to each other, we expect the positive price effect to be weakened given their negative cross elasticity and reduced comparability. On the contrary, this positive price effect should be strengthened when recommended products are substitutes to focal product because they have positive cross elasticity and high comparability. Therefore, we hypothesize the following:

H1: In online product recommendations, the price of a recommend product will be more positively influential on consumers’ willingness-to-pay of the focal product when the recommendation type is substitute, compared to that when the recommendation type is complement.

## Consumers’ Two-Stage Decision-Making

As illustrated in the prior literature (Häubl and Trifts 2000; Liu and Arora 2011; Russo and Leclerc 1994), consumers are often not capable of evaluating all available product alternatives in great depth. Conversion funnel theory suggests that consumer decision-making involves a multistage process of awareness, information search, evaluation, purchase as well as postpurchase activity (Jansen and Schuster 2011; Kotler and Armstrong 2010). Consumers move through different stages of deliberation during their purchase processes (Bruce et al. 2012). The basic conversion funnel theorizes multiple stages, starting when a consumer is initially unaware of the product. Then, when she is exposed to an advertisement or a search result, she moves into the awareness stage. Thereafter, if she is interested in the product, she might transit to the consideration stage. Finally, based on her considerations, the consumer may decide to purchase the product or not (Howard and Sheth 1969). Several variants of the conversion funnel theory have been proposed in the literature (Bonchek and France 2014; Elzinga et al. 2009; Jansen and Schuster 2011; Mulpuru 2011; Wiesel et al. 2011). However, most researchers apply a simplified two-stage choice process that begins once a consumer is aware and interested in a product (Bettman 1979; Gensch 1987; Shocker et al. 1991). Specifically, the first stage is devoted to eliminating alternatives that do not warrant serious consideration (i.e., screening), and the second stage is aimed at identifying the best alternative among those considered (i.e., purchasing) (Beach 1993; Ge et al. 2012). In the first stage of this common treatment of the consumer choice process, consumers typically browse a large set of available options and identify a small subset of candidates for further consideration. In the second stage, they tend to thoroughly evaluate candidates and make a final purchase decision. In the second

stage, consumers’ motivation and determination to make a purchase are increased. WTP represents the last assessment step before the formation of purchase intention (Ayadi and Lapeyre 2016), and a high purchase intention results from the fact that a consumer’s WTP is higher than the price charged (Bohm 1975). Beriain et al. (2016) also found that consumers’ WTP increased with higher intent to purchase. Hence, previous studies argue that the decision stage has a main positive effect on consumers’ WTP by modeling it in the consumer choice process theory.

Next, consider the moderating effect of recommendation type, in other words, whether the recommendation type (i.e., complements or substitutes to the focal product) interacts with consumers’ decision stage to determine their WTP of the focal product. Ge et al. (2012) argue that the manner in which information is processed differs systematically between these two consumer decision stages. Their experimental results reveal that the presentation timing of specific pieces of information about alternative products across decision stages has a great impact on consumers’ choices. This difference can be attributed to shopping goals theory (Lee and Ariely 2006) and construal level theory (Liberman et al. 2007). According to Lee and Ariely (2006), people’s consumption goals are not always highly specified, but tend to change from being abstract to more precise as they move from stage 1 to stage 2 of the consumer choice process. Different levels of goal specificity may determine consumers’ sensitivity to different types of information and recommendations at different stages of consumer choice (Chan et al. 2010). Specifically, consumers are less certain of their shopping goals in the first stage of a shopping process. Thus, their thinking is more abstract in the first stage. Shopping goals become concrete when they are closer to the final purchase point in the second stage. The construal level theory posits that in the formation of consideration sets, abstract attributes of products are crucial and advertisements’ claims should accentuate the product’s core central features (Dhar and Kim 2007). Conversely, at the time of the final purchase decision, it is the low-level, concrete, or secondary peripheral features that should be emphasized (Dhar and Kim 2007).

##

Similarly, Liberman and Trope (1998) found that high-level construal corresponds with desirability while low-level construal corresponds with feasibility, which has been further validated by Thomas et al. (2006) through its effect on purchase intent for near versus distant future. Specifically, desirability pertains to the superordinate “why” aspects or reasons for performing a behavior and feasibility pertains to the subordinate “how” aspects of behavioral performance (Vallacher and Wegner 1987). When displayed with substitutes, advantages and disadvantages of the focal product are more prominent; thus highlighting its core centra features. Consumers gain a sense of awareness about “why” selecting the focal product by comparing similar items. That is to say, substitutes have an influence on the product’s desirability. This effect has also been examined by Kraiselburd et al. (2010) about how the presence of substitute products affects the desirability of vender managed inventory. Thus, recommending substitutes in early decision stage is congruent with the consumers’ abstract mindset and uncertain shopping goals, weakening the positive influence on consumers’ WTP for the focal product from stage 1 to stage 2.

Researchers have also studied the behavioral effects of recommendations beyond standard substitute recommendations. For instance, Zheng et al. (2009) propose that customers prefer different types of recommendations in different purchase stages. In the first stage of an online purchase process, customers are navigating webpages to compare a large set of similar products. Thus, we argue it is intuitive that substitute recommendations are preferred to complement recommendations in this stage. Whereas in the second stage, customers already have a clear candidate set through which to make a purchase decision. In the second stage, substitutable recommendations likely have lesser impact and recommendations of complementary products may be preferred because they introduce items that can add value to the purchase of the focal product. As mentioned above, the low-level, secondary peripheral features should be emphasized in the second stage, which corresponds with the feasibility of the product. Specifically, feasibility is the details and contextual factors involved in product acquisition and use (Cohen et al. 2008), which is more likely to occur in a complementary relationship. When a focal product is presented with complements, they seem to benefit each other, and they are perceived as having more cooperative intentions, as well as revealing the possibility of alternative uses and more applications (Shocker et al. 2004). The feasibility advantages of focal product are then highlighted because complements imply the process (the “how” aspects) of using the focal product. As a result, recommending complements in late decision stage is congruent with consumers’ concrete mindset, yielding greater receptivity as well as WTP for the focal product. Hence, we hypothesize the following moderating effect:

H2: In online product recommendations, consumers’ decision stage will be more positively influential on their willingness-to-pay of the focal product when the recommendation type is complement, compared to that when the recommendation type is substitute.

## EXPERIMENTS

Recommendations on Amazon.com and other platforms generally fall into the complement and substitute product types through the co-purchase and co-view lists. However, this is not always the case, and other contextual factors and user self-selection can impact the effect and content of these recommendations. In addition, manipulating prices and recommendations on a large scale real retail setting may not be possible for academic researchers because of access and proprietary issues. Therefore, to eliminate confounding factors, conditions, and limitations that naturally occur in the field, we first designed a randomized controlled experiment to cleanly manipulate recommendation type, recommended product’s price, and consumers’ decision stage. This controlled and randomized treatment approach allowed us to test our hypotheses and make causal inferences. As we will demonstrate, we also take great care to produce a realistic purchasing scenario in our experiment, so that our results can also be generalized and provide evidence that will inform retailers’ own experimentation.

## Experiment Design and Participants

Our hypotheses express the two two-way interaction effects (price x type and stage x type) on WTP of a focal product. Given that we have three two-level factors and are interested in multiple interactions across factors, we used a full factorial experiment in the main study to test our hypotheses efficiently<sup>3</sup>. Specifically, a 2 (recommendation type: complements versus substitutes) x 2 (recommended products’ price relative to the focal product’s price: low versus high) x 2 (consumers’ decision stage: stage 1 versus stage 2) full-factorial design was used, which resulted in eight treatment conditions. Although, the full factorial design provides the opportunity to test the three-way interaction and the price x stage interaction, our analysis focuses only on interactions identified in our hypotheses. The advantage of factorial experiment designs over randomized controlled trials (RCTs) is that they provide more statistical power with fewer participants. Generally, the objective of RCT is to compare individual experimental conditions to each other directly, while in a factorial experiment combinations of experimental conditions are compared.

We randomly manipulated three factors between subjects, who were undergraduates from a business school in a large public university in North America. These university students match the Internet user demographic data (Wang and Benbasat 2016) and prior studies have suggested that characteristics of university students are deemed to be similar to those of online shoppers (Chan et al. 2010), thus the sample is generally considered appropriate for this type of study. Subjects received extra credits for their participation in the experiment. We performed a power analysis with the assumption that the effect size of our model would be medium, i.e., ????ℎ???? $f ^ { 2 } = 0 . 1 5$ (Cohen 1988). To achieve power (1 − ??) of 0.80 and a medium effect size, as well as maintaining a significance level (??) at 0.05, the minimum sample size is 92 (the calculation was made by using the package “pwr” in R).

Approximately 400 students from a large undergraduate class were invited to participate in the study. In all, 261 students initiated the study. Participants were randomly assigned to one of the eight treatment conditions. The median time of completion was 12 minutes. Participants were informed that multiple manipulation checks would be used to determine if they took the participations. We dropped observations of 126 participants for the following reasons: not completing the study, completing the experiment in an extremely short time (e.g., less than 4 minutes), completing the study in a very long time (e.g., more than 1 hour indicating the study was started, stopped, and started again later), and not passing manipulation checks. It is a common phenomenon that response and completion rates are relatively low in online experiments (Baruch and Holtom 2008). As a result, we had 135 valid observations (51.7% response rate), which was well above our target sample size of 92 determined from our power analysis. The distribution of the valid observations across treatment groups was even as is shown in Table 1.

Table 1. Experimental Design and Sample Size per Group

<table><tr><td>Decision stage</td><td>Price</td><td>complements</td><td>substitutes</td></tr><tr><td>Stage 1</td><td>Low</td><td>16</td><td>17</td></tr><tr><td>Stage 1</td><td>High</td><td>17</td><td>18</td></tr><tr><td>Stage 2</td><td>Low</td><td>17</td><td>16</td></tr><tr><td>Stage 2</td><td>High</td><td>17</td><td>17</td></tr></table>

Experiment participants were put in the scenario of purchasing a new computer mouse on an e-commerce site like Amazon.com. During their purchase processes, product recommendations were displayed based on randomly assigned treatment conditions. We chose a computer mouse as the focal product because it is a common product, it is easy to purchase online, it has low brand association, and it has a large number of potential complements and substitutes with both low and high prices.

For the first manipulation factor (i.e., recommendation type), participants were randomly assigned to one of two different shopping interfaces: the focal product page with recommendations of complementary products, or the focal product page with recommendations of substitutable products. To eliminate potential framing effects from labeling the recommendations, we used the same title for the two recommendation sets, i.e., “We think you may also like these items.” The pages included product descriptions directly from Amazon.com. We omitted brand information in descriptions to eliminate any brand bias. Note that both the complementary and substitutable goods were derived from real recommendations on Amazon.com.

For the second manipulation factor (i.e., prices of recommended products), participants were randomly assigned to either a high or low price condition. In the high price condition, recommended products were higher in price than the focal product and in the low price condition the opposite was true. Though the e-commerce website often implements a mixed strategy in terms of recommendations’ prices, we cleanly manipulated prices such that all displayed recommended products were either below or above the focal product to fully control influential prices.

For the third manipulation factor (i.e., decision stage), we designed a two-stage shopping procedure (i.e., consider-then-choose) adapted directly from Ge et al. (2012), which participants followed prior to being measured on dependent variables. Participants were randomly assigned to one of two decision stage manipulations: complete the first and second stages of the shopping procedures before being shown the focal product page, or complete only the first stage of the shopping procedure before being shown the focal product page. For the “stage” factor, betweensubjects design is preferred over within-subjects design because a within design leads to demand or carryover effects (Charness et al. 2012). In addition, the order of stages cannot be randomized or counterbalanced, which makes it inappropriate to be a within-subject factor. The details of how we designed the two-stage shopping process are illustrated in the next subsection. In all treatment groups, the focal product and its posted price as well as descriptions remained the same.

## Stimuli and Procedures

Participants were first presented a cover story that they were participating in research focusing on consumers’ preferences and purchase behaviors. They were also told that there were no correct answers, and that they should consider only their own preferences. Following these initial instructions, participants were randomly assigned to one of the eight treatment groups.

Before the main task of the experiment, participants were asked to answer a set of basic questions about their opinions on electronic products and were asked to rate several different electronic product categories. Participants were told that their answers to these questions would be used later by our system to predict their preferences and make personalized recommendations for them. This preexperiment task was used to eliminate their doubts about the basis of recommendations in later steps.

In the main task of experiment, subjects were asked to shop for a computer mouse and make a purchase decision. We implemented the two-stage shopping decision process based on the methodology used in the marketing literature (e.g., Ge et al. 2012). In the first stage process, participants were presented with descriptions of 12 computer mice as search results on the ecommerce store. These 12 mice were randomly selected from Amazon.com with various prices and descriptions and kept the same for all participants. Particularly, we searched “mouse” on Amazon.com and selected 12 mice from the first few pages. One popular mouse with a moderate price was selected as the target focal product in later procedures. Then the remaining 11 mice

were selected to keep the product set at a high diversity level in terms of their prices and appearances. This is used to imitate the browsing stage with a reasonably sized product set for consumers to consider (see Figure A1 in Appendix A). Participants were informed that products featured on the listing page were search results for “mouse” in the current e-commerce website. Although real-world e-commerce websites typically offer a much larger set of alternatives in the browsing stage, prior experimental studies involving online shopping tasks usually focus on a much smaller set of alternatives to control the cognitive load of participants. For instance, Xu et al. (2014) kept the number of products in the experimental website constant at 32 in total, and Xiao and Benbasat (2015) used 12 digital cameras in each brand as the stimuli. Participants in our experiment were asked to browse and evaluate all the product information presented without making any decisions. They were also told that questions related to products would be asked later, and the “Next Page” button appeared only after 30 seconds had elapsed, as a means of preventing participants from moving ahead too quickly without reviewing the stage 1 products (see Figure A1 in Appendix A). After clicking the “Next Page” button, manipulation check questions were displayed to check their impressions about these initial 12 mice. Specifically, two questions were: (1) how many mice are there? (three candidate responses were provided, i.e., less than 6, about 6-10, and more than 10) (2) how would you rate the variety of these mice in terms of style? (five candidate responses were provided, i.e., very diverse, diverse, fair, similar, and very similar). These two questions were used to filter out less serious participants. If the participant’s response was far from the true answer, namely, “less than 6” for the first question and “very similar” for the second question, the data point was dropped.

In the second stage, we narrowed down the choice set to 2 mice and displayed more detailed information for each mouse. One was the target focal product. Its detailed information was collected from Amazon.com including price, style, shape, resolution, operation systems, battery life, and warranty. The other one was selected because it has the same price as the focal product. It is worth noting that when selecting the 12 mice initially, we purposely selected one mouse

##

with the same price as the focal one. The same set of attributes were also displayed except that values were manipulated to be inferior than the focal one instead of being collected from the real website. This setting follows from Xiao and Benbasat (2015) and is used to prime subjects with a preference for the target focal mouse product. Participants were asked to evaluate the two items and pick one of them as their final purchase choice (see Figure A2 in Appendix A). This setting put participants in the situation of thoroughly evaluating a small set of candidates and making a final purchase decision as if they were in the later shopping stage. As these two steps were only used to manipulate participants’ perceptions of their current decision stages, the 2 mice were fixed and kept the same for all stage 2 participants to eliminate possible product bias. Participants who were randomly assigned to groups with condition “stage 1” would only go through the first stage (i.e., browsing information). Comparably, those who w e randomly assigned to groups with condition “stage 2” would go through both the first and the second stage.

After the stage manipulation, all participants viewed a specific focal mouse product page. This focal mouse product has been shown in both the first and second stage. This is because we imitated the real online shopping process that products viewed in stage 2 were actually filtered from the ones viewed in stage 1, and the focal mouse product was selected from those viewed in stage 2. The focal mouse was evaluated by participants and used to collect WTP information in later procedures. On one hand, par cipants who experienced the stage 2 were put in the scenario that they selected one from two candidates as the final purchase decision, thus it is natural to ask them to evaluate the specific product that they actually chose in stage 2. On the other hand, we needed the evaluated product to be the same for all participants so that the measured WTP information was comparable among different treatment groups. Therefore, to satisfy the above two conditions, we conducted the following operation. In stage 2, one mouse was dominated by the other mouse as noted earlier, that is, the dominant mouse performed better on several important product attributes than the other one, but offered the same price.

##

Particularly, the inferior mouse has a resolution of 1000 DPI, 6-month battery life, one-year warranty, and does not support Windows 10 operation system. The superior mouse has a resolution of 1600 DPI, 12-month battery life, two-year warranty, and also supports Windows 10 operating system. The screenshot for stage 2 manipulation can be found in Appendix A. This process was adopted from Xiao and Benbasat (2015), and it is used to control the purchase decision of participants. Thus, the final focal product was fixed for all participants and also as per their choice. On the focal mouse product detail page, recommendations were presented according to the random treatment conditions (i.e., complements or substitutes crossed with high or low prices). Figure 4 provides screenshots of four different recommendation interfaces. In the groups with “low (high) price” condition, all recommended products’ prices were slightly lower (higher) than the price of the focal mouse. Subjects could click on the rec mmendation to view a detailed description. The number of clicks and duration on each webpage were also recorded.

After viewing the focal product page based on their treatment conditions, participants were asked to provide their WTP of the focal product (the measurement of WTP is discussed below). Upon completing the shopping task, participants responded to a set of manipulation check questions and completed a short survey with demographic questions that we used as control variables in our analyses (i.e., age, gender, level of education, computer experience, web experience, e-commerce experience, familiarity with, and attitudes toward recommender systems).

![](/api/attachments/7ZFB8JQ6/fulltext/images/368a1fc4f579c45db39f59e7b85e57b917f558e45663d23c3b31e80a6d5b5129.jpg)

![](/api/attachments/7ZFB8JQ6/fulltext/images/cbea738ead2a1cf5fce9e1aa1c25a8a0c438c180ff73132883b34830d4225eac.jpg)

![](/api/attachments/7ZFB8JQ6/fulltext/images/c83ebcd87f8d1977563a21c6aefd44625dbb206ed36a409573f5fc69eeb1f4b9.jpg)

![](/api/attachments/7ZFB8JQ6/fulltext/images/ded8a344592a42f22023deb77e15e2190987fcd3ad0b21d94c68239e24a7a92a.jpg)  
(c) Substitutes with high prices  
(d) Complements with high prices  
Figure 4. Screenshots of the Experimental Interface.

## Dependent Measure

WTP is the maximum amount an individual is willing to sacrifice to procure a product. It has long been used in economics and marketing research as a means of measuring a consumer’s perceived value of a product. Here, we adopted the method used by prior studies (Kim and Gal 2014; Rucker et al. 2014; Rucker and Galinsky 2008) to measure WTP. Participants indicated their WTP using a sliding scale where they could choose from 0% to 120% of the posted retail price. The interval (i.e., 0%-120%) is used to reduce the amount of response variance and to guard against outliers. We are interested in relative changes in WTP because of treatment effects and not in determining point estimates of WTP for specific products, thus the interval WTP metric is sufficient. Furthermore, this method and interval is commonly used in marketing studies (Kim and Gal 2014; Rucker et al. 2014). Because the market price for the focal product was given, it is not realistic to use the Becker-DeGroot-Marschak approach (Frederick 2012) or

Given the retail price is \$12.48 as listed above, how much would you be willing to pay for the wireless mouse at the top of this page? In the following slider bars, the number represents percentage of the retail price, for instance, 10 means 10% of \$12.48. Please click the bar and slide to the percentage you want to pay. The price you selected is: \$11.23

<table><tr><td rowspan="2"></td><td>0%</td><td>10%</td><td>20%</td><td>30%</td><td>40%</td><td>50%</td><td>60%</td><td>70%</td><td>80%</td><td>90%</td><td>100%</td><td>110%</td><td>120%</td></tr><tr><td>0</td><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td><td>60</td><td>70</td><td>80</td><td>90</td><td>100</td><td>110</td><td>120</td></tr></table>

Figure 5. Entering Willingness to Pay.

## RESULTS

Table 2 provides summary statistics on the demographic items collected in our post-experiment survey. It is worth noting that there is no significant demographic information difference between those valid data points and the ineligible ones that we have dropped (except for those incomplete records). For instance, among the 126 dropped data, 78.57% browse e-commerce websites more frequently than once a week, and 84.09% believe that recommender systems are helpful for finding relevant items. In addition, no significant difference was found between subjects in each of the eight experimental conditions with respect to age, gender, and past Internet, online shopping, and interaction with recommender systems experience.

Table 2. Demographic Summary Statistics

<table><tr><td>Control variables</td><td>Summary</td></tr><tr><td>Age</td><td>Mean: 21.6; SD: 3.35</td></tr><tr><td>Gender</td><td>50.37% — female</td></tr><tr><td>Primary language</td><td>88.89% — native English speaker</td></tr><tr><td>Experience with Internet</td><td>88.15% — spend more than 4 hours per day on the Internet</td></tr><tr><td>Experience with e-commerce</td><td>77.04% — browse e-commerce websites more frequently than once a week</td></tr><tr><td>Familiarity with RS</td><td>85.19% — familiar with RS</td></tr><tr><td>Attitude toward RS</td><td>82.22% — RS is helpful for finding relevant items</td></tr></table>

## Manipulation Checks

To check the saliency of our recommended product type manipulation, two manipulation check questions were asked of participants in the post-experiment survey: (1) Do you think the products in the section titled “We think you may also like these items” are complements to the mouse you evaluated? and (2) Do you think the products in the section titled “We think you may also like these items” are substitutes to the mouse you evaluated? In terms of the decision stage manipulation check, we did not directly ask subjects’ perceptions about decision stage because this may be an incomprehensible terminology. Instead, we asked them “In the previous task you just finished, which procedure(s) have you been through?”, and provided the following possible responses: (1) Evaluating a large set of alternative products as if you were gathering information in early stages of shopping and (2) Evaluating a small set of alternative products as if you were trying to choose a final one to purchase. This manipulation check about decision stage is a multiple-choice question. Subjects in “stage 1” group were expected to only select the first answer while subjects in “both stage 1 and stage 2” were expected to select both the answers. An additional question was used to check participants’ perceptions about the relative price: “What do you think of the price level of the mouse you just evaluated?”

First, to check if participants consciously distinguished between complement and substitute recommendations, we compared their responses to the two manipulation check questions about recommended product type. They responded with the following five claims: “Definitely yes” (coded as 5), “Probably yes” (coded as 4), “Maybe” (coded as 3), “Probably not” (coded as 2), and “Definitely not” (coded as 1). As expected, participants in complements group perceived recommendations as complements $( M _ { c o m p l e m e n t s } = 4 . 1 5$ , SD=0.78, $M _ { s u b s t i t u t e s } = 1 . 6 1$ SD=1.01, ??(133) = 16.17, p<0.001), and not as substitutes $( M _ { c o m p l e m e n t s } = 1 . 4 2 , \mathrm { S D } { = } 0 . 6 8 ,$ $M _ { s u b s t i t u t e s } = 4 . 6 8$ , SD=0.63, ??(133) = −28.87, p<0.001). The extremely low p-values of these tests help guard against any potential multiple comparison issues. These results support the validity of our manipulation for recommendation types. Furthermore, for the stage check question, if the subject only selected the first answer (i.e., “evaluating a large set of alternative products as if you were gathering information in early stages of shopping”) as her/his response, it was coded as 1. If the subject selected the second answer (i.e., “evaluating a small set of alternative products as if you were trying to choose a final one to purchase”) or both of the two answers as her/his response, it was coded as 2. Using $M _ { s t a g e 1 }$ and $M _ { s t a g e 2 }$ to denote mean values of participants’ responses in “stage 1” group and “both stage 1 and stage 2” group, respectively, we found that participants in different stage conditions correctly perceived their decision stages $( M _ { s t a g e 1 } = 1 . 1 9 $ , SD=0.39, $M _ { s t a g e 2 } = 1 . 9 7$ , SD=0.17, ??(133) = −14.81, p<0.001). Additionally, the average time of completion for participants in stage 1 and stage 2 conditions are 12 minutes and 15 minutes, respectively. This reasonable time of engagement (not too long or too short) indicates that participants took the purchase task seriously and were not fatigued. Finally, a successful manipulation check was also observed for the price. Likely due to the reference price effect, people in the high price recommendation condition felt the price of focal product is lower than those assigned in the low price recommendation condition $( M _ { h i g h } =$ $2 . 9 6 , \mathrm { S D } = 0 . 5 7 , \ M _ { l o w } = 3 . 3 3 , \mathrm { S D } = 0 . 6 8 , \ t ( 1 3 3 ) = - 3 . 4 5 , \mathrm { p } < 0 . 0 0 1 )$

## Main Results

Table 3 shows the mean and standard deviation of the WTP, measured as a percentage (0%- 120%) of the focal product’s original price, in each of the eight treatment groups.

Table 3. Mean (SD) Willingness to Pay (%) in Each Group

<table><tr><td>Decision stage</td><td>Price</td><td>complements</td><td>substitutes</td></tr><tr><td>Stage 1</td><td>Low</td><td>68.19 (15.86)</td><td>79.29 (17.66)</td></tr><tr><td>Stage 1</td><td>High</td><td>87.65 (13.50)</td><td>93.78 (21.81)</td></tr><tr><td>Stage 2</td><td>Low</td><td>88.29 (14.29)</td><td>81.63 (16.04)</td></tr><tr><td>Stage 2</td><td>High</td><td>93.94 (10.87)</td><td>89.53 (13.14)</td></tr></table>

To test the proposed hypotheses, we made comparisons between combinations of groups to determine interaction effects. As there are three manipulated factors in the experiment, we started by conducting a three-factor Analysis of Variance (ANOVA) and results are presented in Table 4. Because the focus of the study is on effects of complementary versus substitutable recommendations, we did not hypothesize the interaction between recommendation price and decision stage. Additionally, as the three-way interaction among these factors is complex and no prior theory provides insights in this regard, this interaction was also not hypothesized. Results in Table 4 reveal that main effects of stage and price are significant, which is congruent with previous literature. In addition, the interaction between recommendation type and stage is significant, thus supporting H2.

Table 4. Results of Three-factor ANOVA

<table><tr><td></td><td>Df</td><td>SSE</td><td>MSE</td><td>F value</td><td>Pr(&gt;F)</td></tr><tr><td>Type</td><td>1</td><td>73</td><td>73</td><td>0.279</td><td>0.5981</td></tr><tr><td>Price</td><td>1</td><td>4670</td><td>4670</td><td>17.786</td><td>4.66e-05***</td></tr><tr><td>Stage</td><td>1</td><td>1200</td><td>1200</td><td>4.570</td><td>0.0345*</td></tr><tr><td>Type x Price</td><td>1</td><td>9</td><td>9</td><td>0.036</td><td>0.8505</td></tr><tr><td>Type x Stage</td><td>1</td><td>1688</td><td>1688</td><td>6.430</td><td>0.0124*</td></tr><tr><td>Price x Stage</td><td>1</td><td>872</td><td>872</td><td>3.321</td><td> $0.0708^{+}$ </td></tr><tr><td>Residuals</td><td>127</td><td>33343</td><td>263</td><td></td><td></td></tr></table>

Significant levels: $^ { + } p \leq 0 . 1$ ${ } ^ { * } p \leq 0 . 0 5$ ${ } ^ { \ast \ast } p \leq 0 . 0 1$ $^ { \ast \ast \ast } p \leq 0 . 0 0 1$

We drew the average WTP under each combined conditions (i.e., complements vs. substitutes, low price vs. high price, stage 1 vs. stage 2) to visualize all possible main effects (see Figure 6). Specifically, there is no significant difference between participant groups with complement and groups with substitute recommendations $( M _ { c o m p l e m e n t s } = 8 4 . 7 6 , \mathrm { S D } { = } 1 6 . 6 7 .$ $M _ { s u b s t i t u t e s } = 8 6 . 2 4$ , SD=18.85, $F = 0 . 2 7 9$ , p=0.598). This is likely because the effect of recommendation type is strongly subject to other contextual factors, which we explore with our secondary independent variables (i.e., price and decision stage). In line with previous literature, we find that when prices of recommended products are relatively high, participants’ WTP is much higher than when the prices of recommended products are relatively low $( M _ { l o w } = 7 9 . 4 8$ $\mathrm { S D } { = } 1 7 . 4 8$ 2 $M _ { h i g h } = 9 1 . 2 6$ , SD=15.75, ?? = 17.786, p <0.001). Similarly, the difference between conditions in stage 1 and stage 2 is in expected directions $( M _ { s t a g e 1 } = 8 2 . 6 0 , \mathrm { S D } { = } 1 9 . 9 9$ , $M _ { s t a g e 2 } = 8 8 . 4 5$ 2 $\mathrm { S D } { = } 1 4 { \cdot } 2 6$ , ?? = 4.570, $\mathrm { p } { < } 0 . 0 5 )$ , thus indicating that consumers are willing to pay more when they are in the second decision stage.

![](/api/attachments/7ZFB8JQ6/fulltext/images/e69a8c80dde955583e0a7495b6654dcfd618accdf43055f558614853bf76b903.jpg)

##

Figure 6. Average Willingness to Pay in Combined Conditions.

For the interaction effects, Figure 7 presents differences of mean values for complement and substitute groups under different price levels and decision stages, respectively. Figure 7a shows no interaction between type and price, because both complement and substitute groups have higher WTP in high relative price conditions $( \mathrm { F } { = } 0 . 0 3 6 , \mathrm { p } { = } 0 . 8 5 1 )$ . This result indicates that the cross-price elasticity of demand between complementary and substitutable goods may not hold in online recommendation context with respect to individual WTP. Various reasons could potentially lead to this observation. First, the focal product and recommended ones may not be perfectly complementary/substitutable to each other, or at least not perfect in the view of participants because there are tremendous number of products in the same category in ecommerce retailers. Second, consumers’ behaviors differ from offline to online environments. For instance, a consumer is restricted to a limited number of products in an offline market, thus having a strong feeling about the relationship among complements or substitutes. On the contrary, she/he encounters lower search cost in online environments, and it is easy to find other exchangeable complements/substitutes besides the recommended one. Thus, she/he may not be as sensitive to prices of recommended products as in offline stores. Last but not the least, we measured WTP for each participant in the experiment and adopted the idea that WTP is a reflection of product demand in the individual level (Fuchs et al. 2010; Peck and Shu 2009). However, this may not be true because of a small sample in the experiment. Therefore, both prices of complementary and substitutable recommendations serve as reference price points, not conditioning on their different types.

The crossing lines in Figure 7b indicate a significant crossover interaction effect between type and stage $( \mathrm { F } { = } 6 . 4 3 0 , \mathrm { p } { < } 0 . 0 5 )$ . Particularly, the positive effect of decision stage is significant and stronger when recommendations are complements $( M _ { s t a g e 1 } = 7 8 . 2 1$ , SD=17.62, $M _ { s t a g e 2 } =$ 91.12, SD=12.28, $t ( 6 5 ) = - 3 . 2 9 , \mathrm { p } { < } 0 . 0 0 1 )$ , while it is not significant under substitute

conditions $( M _ { s t a g e 1 } = 8 6 . 7 4$ 2 $\mathrm { S D } { = } 2 1 . 1 8$ K $M _ { s t a g e 2 } = 8 5 . 7 0$ 2 $\scriptstyle \mathbf { S D = 1 } 5 . 1 4 .$ $t ( 6 6 ) = 0 . 2 3$ , $\scriptstyle \mathrm { p = o . } 4 1 )$ . We would like to reiterate that it is common in crossover interaction where average main effects are not significant, but slopes of effects become opposite when the second factor is introduced, which is what we show in Figure 7b.

Therefore, our hypothesis of interaction effect H2 is supported, and H1 is not supported. In the early stage, the consumer is less certain about which product to purchase and still searching for substitutes, thus having little interest for complementary recommendations. Substitutable recommendations help to highlight the core central features of the focal product, thus influencing its desirability. As a result, it is congruent with consumers’ abstract mindset in early stage. In late stage, recommending complements help the consumer find extra usage or additional value for the focal product, thus influencing its feasibility. Consequently, it is congruent with the consumers’ concrete mindset, yielding greater receptivity as well as WTP for the focal product, as shown in Figure 7b. Moreover, this crossover interaction also suggests context dependence for the effect of recommendation type. This effect may be dependent on other factors not explored in this study, such as product pictures, categories, the average rating of recommended product, etc. Thus, this interaction presents interesting opportunities for further study.

![](/api/attachments/7ZFB8JQ6/fulltext/images/e8f309f79dfd7c67d19f11a07bfaee0ff85d1457a59af6484936b69792dd3b5b.jpg)  
(a) type × price

![](/api/attachments/7ZFB8JQ6/fulltext/images/938148e0a6f4f37ea351ad156a595c6891a28db8049cda71da0cfad1e3c6ce3b.jpg)  
(b) type × stage  
Figure 7. Interaction Effects (left: type x price; right: type x stage).

To further estimate effect sizes as well as linear coefficients for each factor, we also fit a sequential linear model. First, we regressed the WTP on a set of control variables, including gender, preference to the focal product, experience with e-commerce, familiarity with and attitude toward recommender systems (i.e., Model 1). After that, we ran the linear regression model with three independent variables (i.e., recommendation type, recommendation price, and decision stage) in addition to the control variables (i.e., Model 2). Finally, we further included the two interaction variables of interests to the model (i.e., Mode 3). The type factor has two levels, either complements (0) or substitutes (1), the price factor is either low (0) or high (1), and the stage factor is either stage 1 (0) or stage 2 (1). Regression results of these three models are shown in Table 5, and the R-square increased 0.1283 after including three main effect variables and increased 0.149 after including two additional interaction variables.

Table 5. Results of the Linear Regression Models

<table><tr><td rowspan="2">Variable</td><td colspan="3">Dependent variable: Willingness to pay (%)</td></tr><tr><td>Model 1: Control (R2 = 0.1699)</td><td>Model 2: Main Effects (R2 = 0.2982)</td><td>Model 3: Full model (R2 = 0.3189)</td></tr><tr><td>Intercept</td><td>53.166*** (10.450)</td><td>44.829*** (9.930)</td><td>44.589*** (9.862)</td></tr><tr><td>Type (complements: o)</td><td></td><td>1.190 (2.652)</td><td>5.572 (4.828)</td></tr><tr><td>Price (low: o)</td><td></td><td>11.541*** (2.653)</td><td>10.353** (3.769)</td></tr><tr><td>Stage (stage 1: o)</td><td></td><td>5.200+ (2.684)</td><td>10.832** (4.008)</td></tr><tr><td>Type x Price</td><td></td><td></td><td>2.279 (5.336)</td></tr><tr><td>Type x Stage</td><td></td><td></td><td>-10.729* (5.691)</td></tr><tr><td>Preference</td><td>7.141*** (1.539)</td><td>6.826*** (1.439)</td><td>6.232*** (1.492)</td></tr><tr><td>Gender</td><td>3.255 (3.081)</td><td>2.859 (2.869)</td><td>3.803 (2.905)</td></tr><tr><td>Experience</td><td>-1.126 (1.616)</td><td>-0.726 (1.527)</td><td>-1.054 (1.527)</td></tr><tr><td>Familiarity</td><td>0.600 (1.548)</td><td>0.644 (1.445)</td><td>1.412 (1.491)</td></tr><tr><td>Attitude</td><td>-6.362* (3.032)</td><td>-6.736* (2.824)</td><td>-6.924* (2.807)</td></tr></table>

Significant levels: +?? ≤ 0.1, \*?? ≤ 0.05, \*\*?? ≤ 0.01, \*\*\*?? ≤ 0.001.

Consistent with ANOVA results, we got significant positive coefficients for price and stage, indicating that consumers have higher WTP in the high price condition (compared to low price) and stage 2 condition (compared to stage 1), which are consistent with prior studies. In addition, the interaction effect between type and stage is also significant. Coefficients in Model 3 suggest that consumers shown a recommended product with high price reported 10.353 percentage point higher WTP in terms of the retail price when recommendation is complement $( \mathrm { i . e . , }$ the reference group) and 12.632 (i.e., 10.353+2.279) percentage point higher when recommendation is substitute (i.e., the comparison group). Similarly, consumers in the second stage reported 10.832 percentage point higher WTP in terms of the retail price than those in the first stage when recommendation is complement (i.e., the reference group) and 0.103 (i.e., 10.832-10.729) percentage point higher when recommendation is substitute (i.e., the comparison group). To sum the overall main effects, the coefficients in Model 2 indicate that the main effect of price is 11.541 and main effect of stage is 5.200.

The effect size of our sequential multiple regression model is calculated by Cohen’s $f ^ { 2 } .$ . It is defined as $f ^ { 2 } = ( R _ { A B } ^ { 2 } - R _ { A } ^ { 2 } ) / ( 1 - R _ { A B } ^ { 2 } )$ , where $R _ { A } ^ { 2 }$ is the variance accounted for by a set of control variables A and $R _ { A B } ^ { 2 }$ is the combined variance accounted by A and another set of independent variables of interest B. Here, in our full model, we have $R _ { A } ^ { 2 } = 0 . 1 6 9 9$ and $R _ { A B } ^ { 2 }$ ${ \bf \ } = { \bf 0 . 3 1 8 9 }$ , resulting in a medium to large effect size of $f _ { B } ^ { 2 } = 0 . 2 1 9$ . We also conducted a post hoc power analysis. With the 135 observations and the calculated effect size, the power of our model is 0.993 while maintaining the significance level at 0.05. This provides evidence that null effects are true and not the result of a lack of power.

## Robustness Checks

To assess the robustness of our study findings, we conducted additional analyses accounting for possible violation of assumptions when conducting ANOVA and linear regression. First, we ran orthogonal contrast analysis to deal with the possible statistical dependency issues due to multiple comparisons. Afterward, as we measured the WTP by restricting participants’ choices from 0% to 120% of the stated retail price, it may result in censored and non-normal data. Thus, we estimated the model using Tobit regression accounting for the censored data. Results from additional analyses are consistent with our results discussed above, thus reinforcing the study findings. Details of the robustness checks are given in Appendix B.

## ADDITIONAL STUDIES

The reason why we used a 2 x 2 x 2 full factorial experiment design is that it provides more statistical power with fewer participants and also more realistic, that is to say, product’s price information and consumer’s decision stage naturally coexist with recommendation type in a recommendation scenario. When examining the interaction effect between recommendation type and recommendation price, we made comparisons by combining the stage 1 and stage 2 groups. Similarly, when examining the interaction effect between recommendation type and decision stage, we made comparisons by combining low and high price groups. As we did not hypothesize the three-way interaction among independent factors, we further conducted two additional 2 x 2 experiments to eliminate potential confounding effects and validate results from the original experiment.

Specifically, we recruited participants from Amazon’s Mechanical Turk (MTurk). In study 1, a 2 (recommendation type: complements versus substitutes) x 2 (decision stage: stage 1 versus stage 2) design was used. All experimental interfaces and procedures are the same as the original main study except that there is no price information for all recommended products. Participants were paid \$1 USD for compensation. We had 142 participants, among which 29 were dropped because they failed the attention check or manipulation checks. As a result, 113 observations were reserved for further analysis, with 26-30 observations per treatment condition. We first conducted statistical tests to show there was no significant difference

between subjects in each of the four conditions with respect to their demographic information (e.g., age, gender, past experience with recommender systems, etc.). Then we conducted a twofactor ANOVA to examine main effects of recommendation type and decision stage as well as their interaction effect. Results are presented in Table 6. It is clear that the effect of recommendation type on consumer’s WTP of the focal product highly depends on which decision stage the consumer is in (i.e., significant interaction effect with decision stage). Concretely, the positive effect of decision stage is significant and stronger when recommendations are complements $( M _ { s t a g e 1 } = 8 0 . 7 0 , \mathrm { S D } = 1 6 . 4 3 , \ M _ { s t a g e 2 } = 9 3 . 5 , \mathrm { S D } = 1 0 . 5 4 , $ $t ( 5 5 ) = - 3 . 5 4 , \mathrm { p } { < } 0 . 0 0 1 )$ , while it is not significant under substitute conditions $( M _ { s t a g e 1 } = 8 3 . 0 4$ SD=18.95, $M _ { s t a g e 2 } = 8 3 . 9$ , SD=13.78, $t ( 5 4 ) = - 0 . 2 0 , \mathrm { p } { = } 0 . 4 2 )$ . Thus, findings are consistent with those in the main study (see Figure 7b) and H2 is supported.

Table 6. Results of Two-factor ANOVA (type x stage)

<table><tr><td></td><td>Df</td><td>SSE</td><td>MSE</td><td>F value</td><td>Pr(&gt;F)</td></tr><tr><td>Type</td><td>1</td><td>438</td><td>438</td><td>1.931</td><td>0.1675</td></tr><tr><td>Stage</td><td>1</td><td>1335</td><td>1335</td><td>5.884</td><td>0.0169*</td></tr><tr><td>Type x Stage</td><td>1</td><td>1002</td><td>1002</td><td>4.415</td><td>0.0379*</td></tr><tr><td>Residuals</td><td>109</td><td>24735</td><td>226.9</td><td></td><td></td></tr></table>

Significant levels: $^ { + } p \leq 0 . 1 , ^ { * } p \leq 0 . 0 5 , ^ { * * } p \leq 0 . 0 1 , ^ { * * * } p \leq 0 . 0 0 1$

In study 2, a 2 (recommendation type: complements versus substitutes) x 2 (recommended products’ price relative to the focal product’s price: low versus high) design was used. To mimic the realistic shopping environment, all participants would go through the two-stage shopping procedures (i.e., consider-then-choose). Then they were randomly assigned to one of the four treatment groups and asked to give their WTP of the focal product, which was presented along with recommendations. Similarly, participants were paid \$1 USD for compensation, and those who have participated study 1 were not eligible to take the follow-up study. We had 165

participants, among which 17 were dropped because they failed the attention check or manipulation checks. As a result, 148 observations were reserved for further analysis, with 36- 39 observations per treatment condition. Results of two-factor ANOVA are shown in Table 7. We can see that the recommended products’ price has a significant positive main effect $( M _ { l o w } =$ 82.86, SD=19.42, $M _ { h i g h } = 9 1 . 5 5$ , SD=14.16, ?? = 9.600, p =0.002), and there is no interaction effect between price and recommendation type $( F = 1 . 7 1 4 , \mathrm { p } { = } 0 . 1 9 3 )$ . Specifically, when recommendations are complements to focal product, mean values of reported WTP under low price and high price conditions are $8 5 . 5 3$ and 90.56 $( t ( 7 3 ) = - 1 . 4 9 , \mathrm { p } { = } 0 . 0 7 )$ , respectively. When recommendations are substitutes to focal product, mean values of reported WTP under low price and high price conditions are 80.27 and 92.61 (??(71) = −2.76, p=0.004), respectively. Thus, there is no significant interaction effect between price and recommendation type, and H1 is not supported. These two additional user studies reach consistent findings with our prior main experiment, and thus validate the robustness of our conclusions as supportive evidence.

Table 7. Results of Two-factor ANOVA (type x price)

<table><tr><td></td><td>Df</td><td>SSE</td><td>MSE</td><td>F value</td><td>Pr(&gt;F)</td></tr><tr><td>Type</td><td>1</td><td>119</td><td>119</td><td>0.412</td><td>0.5218</td></tr><tr><td>Price</td><td>1</td><td>2761</td><td>2761</td><td>9.600</td><td>0.0023**</td></tr><tr><td>Type x Price</td><td>1</td><td>493</td><td>493</td><td>1.714</td><td>0.1925</td></tr><tr><td>Residuals</td><td>144</td><td>41412</td><td>287.6</td><td></td><td></td></tr></table>

Significant levels: $^ { + } p \leq 0 . 1$ ${ } ^ { * } p \leq 0 . 0 5$ ${ } ^ { * * } p \leq 0 . 0 1$ $^ { \ast \ast } p \leq 0 . 0 0 1$

## DISCUSSION AND CONCLUSIONS

When evaluating products, consumers are commonly affected by many contextual factors, including current marketing efforts of “other products” (Shocker et al. 2004). As a prominent marketing effort for “other products” in e-commerce, recommender systems play an important role to influence consumers’ decision-making (Adomavicius et al. 2017). Recommendations are

##

typically presented right below the image of the focal product on the web page. These presented recommendations are used to form an “internal standard of comparison” that is used in subsequent WTP judgments. Given the importance of recommendation strategy on consumers’ WTP of a focal product, knowledge about the influence of detailed features in recommendation strategy such as recommendation type and price of recommended product is scarce. Thus, the focus in this paper is to investigate differential effects of complementary and substitutable recommendations on consumers’ WTP of a focal product through interactions with contextual factors in a recommendation scenario. In this paper, we conducted several randomized experiments to examine these effects and experimental results provide evidence that there is a differential effect of complementary and substitutable recommendations, and it is subject to contextual factors. We investigated two factors that commonly present with recommendations: decision stage and the price of recommended products. Generally, consumers utilize a two-stage decision-making process when shopping online, that is, browsing a large set of options in the first stage and making a more thorough evaluation of a reduced set of candidates to make a final purchase in the second stage. Not surprisingly, we found that consumers are willing to pay more for a specific product as they move through decision stages. An interesting finding is the interaction between recommendation type and decision stage. Particularly, the positive effect of stage vanished when the recommendation is a substitute to the focal product, while it is very significant with complementary recommendations. This is consistent with intuition that customers prefer different recommendations against different purchase stages, as well as highlighting the importance of timing in recommender systems. We believe the fact that the effect of recommendation type is only obtained in an interaction with consumer decision stage is both an interesting and novel finding that has significant implications for theory and the practice of using recommendations in online retail. In line with prior findings, the price of recommended products was found to have significant positive effect on WTP of focal product. Serving as a reference point, prices of recommendations may be compared with the retail price

##

of the focal product, which could cause consumers to adjust their WTP through incidental price learning (Nunes and Boatwright 2004) and obtained transaction values. Under the condition with high recommendation prices, consumers tend to have higher WTP for the focal product and vice versa. Moreover, this positive price effect does not interact with recommendation type, which means that the cross-price elasticity of demand between complementary and substitutable goods does not hold in online recommendation context with respect to individual WTP. Possible reasons include the large volume of available complements/substitutes in ecommerce context and low search cost online, which leads consumers not sensitive to the specific recommended complementary or substitutable products’ prices. Hence, the prices of recommended products serve as reference point to consumers regardless of the relationships between recommendations and the focal product.

## Theoretical Contribution

Our research offers important theoretical contributions in following ways. First, studies on product recommendations have largely focused on consumers’ different preferences and behaviors regarding the products being recommended (Adomavicius et al. 2013, 2017). This paper extends the behavioral research on recommender systems by studying the question whether recommending “other products” on the same web page has an effect on consumers’ WTP of the focal product.

Second, prior research has not paid much attention to different types of products presented in recommendations. Deriving from economics literature, two typical relationships between products are examined, that is, complements and substitutes. We observe an interaction effect between decision stage and type of recommendations. Referring back to Figure 7b, it is apparent that in the first decision stage substitute product recommendations increase WTP relative to complements. Substitutable recommendations correspond to the “desirability” of the focal product and are consistent with consumers’ high-level construal in stage 1. In the second

decision stage the opposite effect is observed, complementary recommendations increase WTP of the focal product relative to substitutes. This is because complementary recommendations correspond to the “feasibility” of the focal product, which is consistent with consumers’ low-level construal in stage 2. This flipping of the effect of recommendation type from the first to second decision stages not only accounts for the lack of a recommendation type main effect, but also provides evidence that the standard theory of complements and substitutes may not fully apply in complex decision environments with multiple stages. Our results suggest that complementary recommendations can actually increase the perceived value of a focal product when consumers are in the late stages of evaluating candidate options. Further study on this interesting finding is warranted and encouraged.

Third, our research is one of the few studies that examine detailed recommendation features, i.e., prices of recommended products as well as consumers’ decision stages. Integrating consumers’ decision process, we have a better understanding of behavioral aspects of recommendations in online purchases.

## Implications for Practice

Beyond contributing to advancing the academic literature, our findings also have significant practical implications and may guide the platform’s recommendation strategy. The vulnerability of consumers’ WTP indicates the importance of “other products” in recommender systems. This suggests new possibilities for influencing product sales by manipulating the contextual information of recommendations. Specifically, we have shown that prices of recommended products significantly impact the willingness to pay of a consumer for a focal product. This result would suggest that online retailers are better off recommending products with higher prices relative to the focal product if their objective is to persuade consumers to buy the current focal product. Another important implication comes from the significant interaction between recommendation type and decision stage. Clearly, the timing of recommendations can have a

significant impact on a consumer’s economic decisions. Our results strongly suggest that complementary recommendations should be shown when consumers are close to making a final purchase decision, i.e., in the second decision stage. On the other hand, substitute product recommendations appear to be more beneficial if shown when consumers are early on in their purchasing process. By manipulating the timing of recommendations in this manner, retailers may be able to significantly increase consumers’ WTP for products. Given the fact that depending on the objective of platform or retailers, this study aims at providing insights from a new angle, particularly for retailers who focus on the focal product. Recommendation algorithms can be designed by taking into account the three factors (i.e., types of recommended products, prices of recommended products, and consumers’ decision stages) besides historical ratings, such as attaching different weights for complements/substitutes at different purchase stages. From a consumer’s perspective, results suggest it is good to be aware of the potential WTP bias toward reference prices presented in recommendations.

## Future Work and Conclusion

The main limitation of this study, and any controlled experiment for that matter, is that we are not observing real-world decisions. In contrast, however, an advantage is that our controlled randomized experiments allow us to make causal inferences, thus trading external validity for identification. Secondly, a highly diverse set of products may yield findings that can be generalized to more situations in which recommendations are provided. Nevertheless, it is also acceptable and common for IS researchers to use one single sample in lab experiment settings (Wang and Benbasat 2016).

Future research can be developed to explore other factors associated with recommended products, such as average ratings, number of ratings, quality, pictures of complements/ substitutes, and diversity in recommendations. Additionally, we can use observational data to further validate findings of our experiments and provide more generalizability. For instance, data from Amazon.com co-purchase and co-view recommendation networks may potentially be used as proxies for complement and substitute recommendations, respectively. By examining relationships between recommendation network properties and products’ sales, we will have additional support for the influence of complementary and substitutable product recommendations on consumers’ economic behaviors from the aggregate level. Another interesting direction is to consider the price discount when examining consumers’ purchase behavior of a bundle including the focal product with recommended complementary products.

In summary, the work presented here has provided evidence that recommendations of other products can significantly influence consumers’ WTP for a focal product in online settings. We observed significant effects of the price of other recommended products, the decision stage of the consumer, and the interaction between decision stage and recommendation type. Each of these effects provides new evidence on how product recommendations influence consumer purchasing decisions, and suggests practical implications for how online retailers design and implement their product pages and interfaces.

## Author statement

We would like to submit our manuscript, “Complements and Substitutes in Online Product Recommendations: The Differential Effects on Consumers’ Willingness-to-Pay” (authored by Mingyue Zhang and Jesse Bockstedt) for another round of consideration of possible publication in Information and Management.

In this round of revision, we firstly would like to thank the copy-editor to carefully proofread our manuscript, which greatly helped us improve our work. We have thoroughly read through the whole manuscript and revised the paper based on the editorial suggestions.

We warrant the article is original, does not infringe upon any copyright or other proprietary right of any third party, is not under consideration for publication by any other journal, and has not been published previously. All authors confirm that we have reviewed and approved the final version of the manuscript. Should there be anything that we need to do further, please let us know. Thank you very much for your kind help.

## ACKNOWLEDGMENTS

This work was supported by the National Natural Science Foundation of China [grant numbers 71802024 and 71974018] and the MOE Project of Key Research Institute of Humanities and Social Sciences at Universities [grant number 17JJD630006].

## REFERENCES

Adomavicius, G., Bockstedt, J. C., Curley, S. P., and Zhang, J. 2013. “Do recommender systems manipulate consumer preferences? A study of anchoring effects,” Information Systems Research (24:4), pp. 956–975.

Adomavicius, G., Bockstedt, J., Curley, S., and Zhang, J. 2017. “Effects of online recommendations on consumers’ willingness to pay,” Information Systems Research (29:1), pp. 84–102.

Ayadi, N., and Lapeyre, A. 2016. “Consumer purchase intentions for green products: Mediating role of WTP and moderating effects of framing,” Journal of Marketing Communications (22:4), Routledge, pp. 367–384 (doi: 10.1080/13527266.2014.888574).

Baruch, Y., and Holtom, B. C. 2008. “Survey response rate levels and trends in organizational research,” Human Relations (61:8), pp. 1139–1160 (doi: 10.1177/0018726708094863).

Beach, L. R. 1993. “Broadening the definition of decision making: The role of pre-choice screening of options,” Psychological Science (4:4), pp. 215–220.

Beriain, M. J., Sánchez, M., Insausti, K., Sarries, M. V., and Soret, B. 2016. “A comparison of sensory acceptance, purchase intention, and willingness to pay for Pirenaica beef from two different slaughter weight groups, under different consumer information scenarios,” Journal of Sensory Studies (31:6), pp. 453–464 (doi: 10.1111/joss.12236).

Bettman, J. R. 1979. “Memory factors in consumer choice: A review,” Journal of Marketing (43:2), pp. 37–53 (doi: 10.2307/1250740).

Bohm, P. 1975. “Option demand and consumer’s surplus: comment,” The American Economic Review (65:4), pp. 733–736.

Bonchek, M., and France, C. 2014. “Marketing can no longer rely on the funnel,” Harvard Business Review (17).

Bruce, N. I., Peters, K., and Naik, P. A. 2012. “Discovering how advertising grows sales and builds brands,” Journal of Marketing Research (49:6), pp. 793–806 (doi: 10.1509/jmr.11.0060).

Chan, J. C. F., Jiang, Z., and Tan, B. C. Y. 2010. “Understanding online interruption-based advertising: Impacts of exposure timing, dvertising intent, and brand image,” IEEE Transactions on Engineering Management (57:3), pp. 365–379 (doi: 10.1109/TEM.2009.2034255).

Charness, G., Gneezy, U., and Kuhn, M. A. 2012. “Experimental methods: Between-subject and withinsubject design,” Journal of Economic Behavior & Organization (81:1), pp. 1–8.

Cohen, J. 1988. Statistical power analysis for the behavioral sciences Lawrence Erlbaum Associates.

Cohen, J. B., Belyavsky, J., and Silk, T. 2008. “Using visualization to alter the balance between desirability and feasibility during choice,” Journal of Consumer Psychology (18:4), pp. 270–275.

Dhar, R., and Kim, E. Y. 2007. “Seeing the forest or the trees: Implications of construal level theory for consumer choice,” Journal of Consumer Psychology (17:2), pp. 96–100 (doi: 10.1016/S1057- 7408(07)70014-1).

Dhar, V., Geva, T., Oestreicher-singer, G., and Sundararajan, A. 2014. “Prediction in economic networks,” Information Systems Research (25:2), pp. 264–284.

Donaldson, C., Jones, A. M., Mapp, T. J., and Olson, J. A. 1998. “Limited dependent variables in willingness to pay studies: applications in health care,” Applied Economics (30:5), pp. 667–677 (doi: 10.1080/000368498325651).

Elzinga, D., Mulder, S., Vetvik, O. J., and others. 2009. “The consumer decision journey,” McKinsey Quarterly (3), pp. 96–107.

Frederick, S. 2012. “Overestimating others’ willingness to pay,” Journal of Consumer Research (39:1), pp. 1–21 (doi: 10.1086/662060).

Fuchs, C., Prandelli, E., and Schreier, M. 2010. “The psychological effects of empowerment strategies on consumers’ product demand,” Journal of Marketing (74:1), pp. 65–79.

Ge, X., Häubl, G., and Elrod, T. 2012. “What to say when: Influencing consumer choice by delaying the presentation of favorable information,” Journal of Consumer Research (38:6), pp. 1004–1021 (doi: 10.1086/661937).

Gensch, D. H. 1987. “A two-stage disaggregate attribute choice model,” Marketing Science (6:3), pp. 223– 239.

Goh, K. H., and Bockstedt, J. C. 2013. “The framing effects of multipart pricing on consumer purchasing behavior of customized information good bundles,” Information Systems Research (24:2), pp. 334– 351.

Hamilton, R. W., and Thompson, D. V. 2007. “Is there a substitute for direct experience? Comparing consumers’ preferences after direct and indirect product experiences,” Journal of Consumer Research (34:4), pp. 546–555 (doi: 10.1086/520073).

Häubl, G., and Trifts, V. 2000. “Consumer decision making in online shopping environments: The effects of interactive decision aids,” Marketing Science (19:1), pp. 4–21.

Ho, S. Y., Bodoff, D., and Tam, K. Y. 2011. “Timing of adaptive web personalization and its effects on online consumer behavior,” Information Systems Research (22:3), pp. 660–679.

Hosanagar, K., Fleder, D., Lee, D., and Buja, A. 2014. “Will the global village fracture into tribes? Recommender systems and their effects on consumer fragmentation,” Management Science (60:4), pp. 805–823.

Howard, J. A., and Sheth, J. N. 1969. The theory of buyer behavior (Vol. 14), Wiley New York.

Jansen, B. J., and Schuster, S. 2011. “Bidding on the buying funnel for sponsored search and keyword advertising,” Journal of Electronic Commerce Research (12:1), pp. 1–18 (doi: 10.1111/j.1083- 6101.2007.00393.x).

Jiang, Y., Shang, J., Liu, Y., and May, J. 2015. “Redesigning promotion strategy for e-commerce competitiveness through pricing and recommendation,” International Journal of Production Economics (167), Elsevier, pp. 257–270.

Jin, R. K. 2006. “Leveraging bidder behavior to identify categories of substitutable and complementary goods on eBay,” Harvard University.

Kahneman, D., and Tversky, A. 1979. “Prospect theory: An analysis of decision under risk,” Econometrica (47:2), pp. 263–292 (doi: 10.2307/1914185).

Kim, S., and Gal, D. 2014. “From compensatory consumption to adaptive consumption : The role of selfacceptance in resolving self-deficits,” Journal of Consumer Research (41:August), pp. 526–542 (doi: 10.1086/676681).

Koçaş, C., and Dogerlioglu-Demir, K. 2014. “An empirical investigation of consumers’ willingness-to-pay and the demand function: The cumulative effect of individual differences in anchored willingness-topay responses,” Marketing Letters (25:2), pp. 139–152 (doi: 10.1007/s11002-013-9235-4).

Kotler, P., and Armstrong, G. 2010. Principles of marketing, Pearson education.

Kraiselburd, S., Narayanan, V. G., and Raman, A. 2010. “Contracting in a supply chain with stochastic demand and substitute products,” Production and Operations Management (13:1), pp. 46–62 (doi: 10.1111/j.1937-5956.2004.tb00144.x).

Lee, L., and Ariely, D. 2006. “Shopping goals, goal concreteness, and conditional Promotions,” Journal of Consumer Research (33:June), pp. 60–71.

Leeflang, P. S. H., and Parreño-Selva, J. 2012. “Cross-category demand effects of price promotions,”

Journal of the Academy of Marketing Science (40:4), Springer, pp. 572–586.

Liberman, N., and Trope, Y. 1998. “The role of feasibility and desirability considerations in near and distant future decisions A test of temporal construal theory,” Journal of Personality and Social Psychology (75:1), pp. 5–18.

Liberman, N., Trope, Y., and Wakslak, C. 2007. “Construal level theory and consumer behavior,” Journal of Consumer Psychology (17:2), pp. 113–117 (doi: 10.1016/S1057-7408(07)70017-7).

Lin, Z., Goh, K.-Y., and Heng, C.-S. 2017. “The demand effects of product recommendation networks: an empirical analysis of network diversity and stability,” MIS Quarterly (41:2), pp. 397–426 (doi: 10.1002/fut.10121).

Liu, Q., and Arora, N. 2011. “Efficient choice designs for a consider-then-choose model,” Marketing Science (30:2), pp. 321–338 (doi: 10.1287/mksc.1100.0629).

McAuley, J., Pandey, R., and Leskovec, J. 2015. “Inferring networks of substitutable and complementary products,” in Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.

Mulhern, F. J., and Leone, R. P. 1991. “Implicit price bundling of retail products: A multiproduct approach to maximizing store profitability,” Journal of Marketing (55:4), pp. 63–76 (doi: 10.2307/1251957).

Mulpuru, S. 2011. “The purchase path Of online buyers,” Forrester Report (March), pp. 1–6.

Niedrich, R. W., Sharma, S., and Wedell, D. H. 2001. “Reference price and price perceptions: A comparison of alternative models,” Journal of Consumer Research (28:3), pp. 339–354 (doi: 10.1086/323726).

Nunes, J. C., and Boatwright, P. 2004. “Incidental prices and their effect on willingness to pay,” Journal of Marketing Research (41:4), pp. 457–466 (doi: 10.1509/jmkr.41.4.457.47014).

Oestreicher-Singer, G., and Sundararajan, A. 2012a. “Recommendation networks and the long tail of electronic commerce,” MIS Quarterly (36:1), pp. 65–83.

Oestreicher-Singer, G., and Sundararajan, A. 2012b. “The visible hand? Demand effects of recommendation networks in electronic markets,” Management Science (58:11), pp. 1963–1981.

Payne, J. W., Bettman, J. R., and Johnson, E. J. 1992. “Behavioral decision research: a constructive processing perspective,” Annual Reviews of Pyschology (43:1), pp. 87–131.

Peck, J., and Shu, S. B. 2009. “The Effect of mere touch on perceived ownership,” Journal of Consumer Research (36:October), pp. 434–447 (doi: 10.1086/598614).

Rajendran, K. N., and Tellis, G. J. 1994. “Contextual and temporal components of reference price,” Journal of Marketing (58:1), pp. 22–34 (doi: 10.2307/1252248).

Rao, A. R., and Sieben, W. a. 1992. “The effect of prior knowledge on price acceptability and the type of information examined,” Journal of Consumer Research (19:2), pp. 256–270 (doi: 10.1086/209300).

Rucker, D. D., and Galinsky, A. D. 2008. “Desire to acquire: Powerlessness and compensatory consumption,” Journal of Consumer Research (35:2), pp. 257–267 (doi: 10.1086/588569).

Rucker, D. D., Hu, M., and Galinsky, A. D. 2014. “The Experience versus the expectations of power : A recipe for altering the effects of power on behavior,” Journal of Consumer Research (41:August), pp. 381–396 (doi: 10.1086/676598).

Russo, J. E., and Leclerc, F. 1994. “An eye-fixation analysis of choice processes for consumer nondurables,” Journal of Consumer Research (21:September), pp. 274–290.

Shapiro, S. L., Dwyer, B., and Drayer, J. 2016. “Examining the role of price fairness in sport consumer ticket purchase decisions,” Sport Marketing Quarterly (25:4), pp. 227–240.

Shocker, A. D., Bayus, B. L., and Kim, N. 2004. “Product complements and substitutes in the real world: The relevance of ‘other products,’” Journal of Marketing (68:1), pp. 28–40.

Shocker, A. D., Ben-akiva, M., Boccara, B., and Nedungadi, P. 1991. “Consideration set influences on consumer decision-making and choice: Issues , models , and suggestions,” Marketing Letters (2:3), pp. 181–197.

Simonson, I., and Drolet, A. 2004. “Anchoring effects on consumers’ willingness to pay and willingness to accept,” Journal of Consumer Research (31:3), pp. 681–690 (doi: 10.1086/425103).

Thaler, R. 1985. “Mental accounting and consumer choice,” Marketing Science (4:3), pp. 199–214.

Thomas, M., Chandran, S., and Trope, Y. 2006. “The effects of temporal distance on purchase construal,” Cornell University.

Thompson, D. V., Hamilton, R. W., and Petrova, P. K. 2009. “When mental simulation hinders behavior: The effects of process-oriented thinking on decision difficulty and performance,” Journal of Consumer Research (36:4), pp. 562–574 (doi: 10.1086/599325).

Vallacher, R. R., and Wegner, D. M. 1987. “What do people think they’re doing? Action identification and human behavior,” Psychological Review (94:1), pp. 3–15 (doi: 10.1037/0033-295X.94.1.3).

Varian, H. R. 1992. Microeconomic analysis, New York: W.W. Norton.

Venkatesh, R., and Kamakura, W. 2003. “Optimal bundling and pricing under a monopoly: Contrasting complements and substitutes from independently valued products,” The Journal of Business (76:2), pp. 211–231 (doi: 10.1086/367748).

Walters, R. G. 1991. “Assessing the impact of retail price promotions on product substitution, complementary purchase, and interstore sales displacement,” Journal of Marketing (55:2), pp. 17– 28 (doi: 10.2307/1252234).

Wang, W., and Benbasat, I. 2016. “Empirical assessment of alternative designs for enhancing different types of trusting beliefs in online recommendation agents,” Journal of Management Information Systems (33:3), Routledge, pp. 744–775 (doi: 10.1080/07421222.2016.1243949).

Wiesel, T., Pauwels, K., and Arts, J. 2011. “Marketing’s profit impact: Quantifying online and offline funnel progression,” Marketing Science (30:4), pp. 604–611 (doi: 10.1287/mksc.1100.0612).

Xiao, B., and Benbasat, I. 2015. “Designing warning messages for detecting biased online product recommendations: An empirical investigation,” Information Systems Research (24:4), pp. 793–811 (doi: 10.1287/isre.2015.0592).

Xu, J. D., Benbasat, I., and Cenfetelli, R. T. 2014. “The influences of online service technologies and task complexity on efficiency and personalization,” Information Systems Research (25:2), pp. 420–436 (doi: 10.1287/isre.2013.0503).

Zhao, T., McAuley, J., Li, M., and King, I. 2017. “Improving recommendation accuracy using networks of substitutable and complementary products,” Proceedings of the International Joint Conference on Neural Networks (2017-May), pp. 3649–3655 (doi: 10.1109/IJCNN.2017.7966315).

Zheng, J., Wu, X., Niu, J., and Bolivar, A. 2009. “Substitutes or complements : Another step forward in recommendations,” Proceedings of the 10th ACM Conference on Electronic Commerce, pp. 139–145 (doi: 10.1145/1566374.1566394).

Zhu, T., Harrington, P., Li, J., and Tang, L. 2014. “Bundle recommendation in ecommerce,” Proceedings of the 37th International ACM SIGIR Conference on Research & Development in Information Retrieval, pp. 657–666 (doi: 10.1145/2600428.2609603).

## BIOGRAPHICAL NOTES

Mingyue Zhang is an associate professor of Information Management and Decision Science, The School of Business and Management, Shanghai International Studies University. She received her Ph.D. degree in Management Science and Engineering from the School of Economics and Management, Tsinghua University, in 2017. Her current research interests include recommender systems and consumer behavior analysis. Her work has been published in journals such as Decision Sciences, Decision Support Systems, Information Sciences, International Journal of Intelligent Systems, ACM Transactions on Knowledge Discovery from Data, etc.

Jesse Bockstedt is an associate professor of Information Systems and Operations Management in Goizueta Business School, Emory University. He completed his Ph.D. in Information Systems at the University of Minnesota's Carlson School of Management in 2008. Prior to joining the faculty at Emory in 2016, Bockstedt held positions at George Mason University and the University of Arizona. His primary research focus is behavioral economic issues in technology-mediated environments. His articles have been published in a number of leading journals including MIS Quarterly, Information Systems Research, Journal of MIS, and Production and Operations Management.

## APPENDIX A

Screenshots of stage 1 and stage 2 manipulations are shown in Figure A1 and Figure A2.

## Please evaluate the following products:

Suppose that you are browsing an e-commerce website, and considering to buy a mouse. Below are the search results for "mouse". Please review each product carefully. We will ask you some questions related to these items

After evaluating all the relevant information about these mice on this page, please click 'Next page' to answer questions about these products. (Note: "Next page" button will not appear at the bottom of the page until you have enough time to review these products.)

![](/api/attachments/7ZFB8JQ6/fulltext/images/b027adc04dd15f9abd8731b0791a330f0c93e0ee6f528391919be9aa44e0a7f9.jpg)  
E-3lue Cobra EMS109BK Gaming Mouse 1600dpi \$8.95

![](/api/attachments/7ZFB8JQ6/fulltext/images/41e20c0c163c5ff6fd8c56490e6ba278f0c5aa48f5f73941c4a46248f7101f26.jpg)  
HP Wireless Mouse X3000 \$12.48

![](/api/attachments/7ZFB8JQ6/fulltext/images/f877f098d124f5d32a19f9432bae5f591f615af3273c1ca973466a94c4947b5b.jpg)

![](/api/attachments/7ZFB8JQ6/fulltext/images/8082969afb2a0d092f9f3396fc1799bf9e4ed382a8d1fd60250e14ac562a002a.jpg)  
Figure A1. Screenshot of Stage 1 Manipulation (there are a total of 12 mice on the page).

## Make your purchase decision:

Now we have narrowed down your choices to 2 mice. Their detailed descriptions are shown below. Please pick the mouse below that you're more likely to purchase.

Pick one of them as your final purchase choice:

![](/api/attachments/7ZFB8JQ6/fulltext/images/46edea302706c7ec67358395c954c42fe3d6bf550040ed1b7f468b649c7f71ca.jpg)

<table><tr><td>• Price: $12.48</td></tr><tr><td>• Style: Wireless mouse, Nano receiver</td></tr><tr><td>• Shape: Trend-setting style sets it apart from the rest. Contoured shape promotes all-day comfort</td></tr><tr><td>• Resolution: 1600DPI (A mouse with higher resolution detects and reacts to smaller movement)</td></tr><tr><td>• Operation systems: Works with Windows XP, Vista, 7, 8 and 10</td></tr><tr><td>• Battery life: 12-month</td></tr><tr><td>• Warranty: Two-year - worldwide parts-and-labor limited warranty</td></tr></table>

Please explain your choice:

![](/api/attachments/7ZFB8JQ6/fulltext/images/cfda42055601c108e9354989e4d13b4e101a7d8d103ba39712da0cb06c265073.jpg)

Price: \$12.48

• Style: Wireless mouse, Nano receiver

• Shape: Soft rubber grip and contoured body deliver continuous, all-day comfort.

Resolution: 1000DPI (A mouse with higher resolution detects and reacts to smaller movement)

• Operation systems: Works with Window 98, 2000, NT, XP, Win7 and Win8

• Battery life: 6-month

Warranty: One-year - worldwide parts-and-labor limited warranty

Next page

Figure A2. Screenshot of Stage 2 Manipulation.

## APPENDIX B

## Orthogonal Contrast Analysis

A standard analysis of variance (i.e., ANOVA) provides an F-test, which is called an omnibus test because it reflects all possible differences between means of the groups analyzed by ANOVA. However, in most experiments we want to draw conclusions more precisely, which can be

obtained from contrast analysis. A contrast expresses a specific question about the pattern of results of an ANOVA and it can deal with the possible statistical dependency issues due to multiple comparisons. Both contrasts are evaluated using the same general procedures.

To construct the contrasts in our main experiment (i.e., the 2 x 2 x 2 design), we first named the eight treatment groups, that is, Gr1 (Stage 1, Low price, Complements), Gr2 (Stage 1, Low Substitutes), Gr5 (Stage 2, Low price, Complements), Gr6 (Stage 2, Low price, Substitutes), Gr7 (Stage 2, High price, Complements), and Gr8 (Stage 2, High price, Substitutes). Based on the proposed hypotheses, we have the following two contrasts:

Contrast $\phi _ { 1 }$ which is the interaction effect between recommendation type and recommended products’ prices: (Gr1, Gr4, Gr5, Gr8) vs. (Gr2, Gr3, Gr6, Gr7)

 Contrast $\phi _ { 2 }$ which is the interaction effect between recommendation type and decision stage: (Gr1, Gr3, Gr6, Gr8) vs. (Gr2, Gr4, Gr5, Gr7)

Table B1 presents the contrast coefficients and $C _ { a }$ represents the contrast coefficient in each treatment group where $a \in A = \{ G r 1 , G r 2 , \cdots , G r 8 \}$ . We know the two contrasts are mutually orthogonal as $\textstyle \sum _ { a = 1 } ^ { A } C _ { a \phi _ { 1 } } C _ { a \phi _ { 2 } } = 0$ . Afterward, the two contrasts are evaluated using the same general procedures. First, a specific F ratio (denoted as $F _ { \phi } )$ is computed. Then the F value is compared with the critical statistic to determine its significance level. In the following calculation, the sample size in each group is S=17 and $M _ { a }$ is the average willingness to pay in each group.

Table B1. Contrast Coefficients

<table><tr><td>Contrast</td><td>Gr1</td><td>Gr2</td><td>Gr3</td><td>Gr4</td><td>Gr5</td><td>Gr6</td><td>Gr7</td><td>Gr8</td><td> $\sum_{a=1}^{A} C_a$ </td></tr><tr><td> $\phi_1$ </td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>0</td></tr><tr><td> $\phi_2$ </td><td>1</td><td>-1</td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>-1</td><td>1</td><td>0</td></tr></table>

## 1. Contrast $\phi _ { 1 }$

The coefficients and mean values for computing $\phi _ { 1 }$ are illustrated in Table B2.

Table B2. Computation of $S S _ { \phi _ { 1 } }$

<table><tr><td>Group</td><td> $M_a$ </td><td> $C_a$ </td><td> $C_aM_a$ </td><td> $C_a^2$ </td></tr><tr><td>1</td><td>68.19</td><td>1</td><td>68.19</td><td>1</td></tr><tr><td>2</td><td>79.29</td><td>-1</td><td>-79.29</td><td>1</td></tr><tr><td>3</td><td>87.65</td><td>-1</td><td>-87.65</td><td>1</td></tr><tr><td>4</td><td>93.78</td><td>1</td><td>93.78</td><td>1</td></tr><tr><td>5</td><td>88.29</td><td>1</td><td>88.29</td><td>1</td></tr><tr><td>6</td><td>81.63</td><td>-1</td><td>-81.63</td><td>1</td></tr><tr><td>7</td><td>93.94</td><td>-1</td><td>-93.94</td><td>1</td></tr><tr><td>8</td><td>89.53</td><td>1</td><td>89.53</td><td>1</td></tr><tr><td>sum</td><td></td><td></td><td>-2.72</td><td>8</td></tr></table>

$$
S S _ {\phi_ {1}} = \frac {S \cdot (\sum C _ {a} M _ {a}) ^ {2}}{\sum C _ {a} ^ {2}} = \frac {1 7 \cdot (- 2 . 7 2) ^ {2}}{8} = 1 5. 7 2
$$

$$
M S _ {\phi_ {1}} = \frac {S S _ {\phi_ {2}}}{1} = 1 5. 7 2
$$

Furthermore, to obtain the Mean Square Error $( M S _ { e r r o r } )$ , we conduct a single-factor ANOVA for the eight treatment groups and the result is shown in Table B3. Thus, we get the value $M S _ { e r r o r } = 2 6 2 . 5 5$ from the within groups mean square. The F ratio is calculated as:

$$
F _ {\phi_ {1}} = \frac {M S _ {\phi_ {1}}}{M S _ {e r r o r}} = \frac {1 5 . 7 2}{2 6 2 . 5 5} = 0. 0 6 0
$$

The critical value is $F _ { 1 , A ( S - 1 ) } = F _ { 1 , 8 \times 1 6 } = F _ { 1 , 1 2 8 } = 3 . 9 1 5$ at level $\alpha = 0 . 0 5 . \mathrm { A s } \ 0 . 0 6 0 < 3 . 9 1 5$

the contrast $\phi _ { 1 }$ is nonsignificant.

Table B3. Single-factor ANOVA Result for the Eight Treatment Groups

<table><tr><td>Source of Variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>p-value</td><td>F crit.</td></tr><tr><td>Between Groups</td><td>8622.33</td><td>7</td><td>1231.76</td><td>4.69</td><td>0.0001</td><td>2.08</td></tr><tr><td>Within Groups</td><td>33343.42</td><td>127</td><td>262.55</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>41965.75</td><td>134</td><td></td><td></td><td></td><td></td></tr></table>

## 2. Contrast $\phi _ { 2 }$

The coefficients and mean values for computing $\phi _ { 2 }$ is omitted because they can be inferred from Table B1 and Table 3. Procedures are quite similar:

$$
S S _ {\phi_ {2}} = \frac {S \cdot (\sum C _ {a} M _ {a}) ^ {2}}{\sum C _ {a} ^ {2}} = \frac {1 7 \cdot (- 2 8 . 3) ^ {2}}{8} = 1 7 0 1. 8 9
$$

$$
M S _ {\phi_ {2}} = \frac {S S _ {\phi_ {3}}}{1} = 1 7 0 1. 8 9
$$

$$
F _ {\phi_ {2}} = \frac {M S _ {\phi_ {2}}}{M S _ {e r r o r}} = \frac {1 7 0 1 . 8 9}{2 6 2 . 5 5} = 6. 4 8
$$

As $6 . 4 8 { > } 3 . 9 1 5 .$ , the contrast $\phi _ { 2 }$ is significant.

To summarize, we reached the same conclusion with our three-factor ANOVA (see Table 4). $\phi _ { 1 }$ is nonsignificant and $\phi _ { 2 }$ is significant, i.e., the interaction effect between the type and stage is significant.

## Removing Normality Assumptions

As we measured the willingness to pay by restricting participants’ choices from 0% to 120% of the stated retail price, it may result in censored and non-normal data. Figure B1 shows the Quantile-Quantile (QQ) Plot for all values of willingness to pay, and it seems that some data points are censored at the end. Therefore, we conducted three normality tests for our data, that is, the Anderson-Darling normality test, Lilliefors normality test, and Cramer-von Mises normality test. The statistics and corresponding p-values are displayed in Table B4, which reject the null hypothesis about normal distribution.

![](/api/attachments/7ZFB8JQ6/fulltext/images/880da731de5dceda9e3424caa4356630a784304366f6f0d7c386de3374921363.jpg)  
Figure B1. Quantile-Quantile Plot for All Willingness to Pay

Table B4. Normality Test for Willingness to Pay

<table><tr><td></td><td>Statistic</td><td>p-value</td></tr><tr><td>Anderson-Darling normality test</td><td>A=1.243</td><td>0.003**</td></tr><tr><td>Lilliefors normality test</td><td>D=0.097</td><td>0.003**</td></tr><tr><td>Cramer-von Mises normality test</td><td>W=0.212</td><td>0.004**</td></tr></table>

Significant levels: $^ { + } p \leq 0 . 1$ $^ { * } p \leq 0 . 0 5$ ${ } ^ { * * } p \leq 0 . 0 1$ $^ { \ast \ast \ast } p \leq 0 . 0 0 1$

Thus, we performed robustness checks by removing the normality assumption in our analysis. We used a Tobit regression model, which is commonly used to model willingness to pay (Donaldson et al. 1998) as a means of dealing with the censored data. Similar procedures were applied as the linear regression, that is, first regressed willingness to pay on all control variables and then included the independent variables that we are interested in. Results of the three Tobit models are presented in Table B5, and the log likelihood of models increased from - 554.187 to -541.179. Not surprisingly, we got significant coefficients for price, stage, and the interaction term type × stage, and all of them have similar magnitude to results of our linear regression model. The reported coefficients in Tobit models indicate how a one-unit change in an independent variable alters the latent dependent variable ??<sup>∗</sup>, which is the noncensored willingness to pay in our model. Thus, to interpret estimation results, we need to adjust coefficients to get the marginal effect on the observed dependent variable ?? (censored willingness to pay). After transformation, the coefficient in Model 6 for type × stage becomes - 11.054 (5.613). The coefficient indicates the percentage point changes on the 0%-120% scale of willingness to pay.

As a final robustness check, we changed the way we coded the three manipulated factors from dummy coding (0,1) to effect coding (-1,1), and regression results are presented in Table B6. Directions and significance of coefficients remain the same as our prior analysis.

Table B5. Results of the Tobit Regression Models

<table><tr><td rowspan="2"></td><td colspan="3">Dependent variable: Willingness to pay (%)</td></tr><tr><td>Model 4: Control (Log-likelihood = -554.187)</td><td>Model 5: Main Effects (Log-likelihood = -543.292)</td><td>Model 6: Full model (Log-likelihood = -541.179)</td></tr><tr><td>Intercept</td><td>52.833*** (10.64)</td><td>44.092*** (9.994)</td><td>43.803*** (9.845)</td></tr><tr><td>Type (complements: o)</td><td></td><td>1.709 (2.672)</td><td>5.875 (4.818)</td></tr><tr><td>Price (low: o)</td><td></td><td>11.939*** (2.674)</td><td>10.303*** (3.757)</td></tr><tr><td>Stage (stage 1: o)</td><td></td><td>4.777+ (2.707)</td><td>10.629*** (3.996)</td></tr><tr><td>Type x Price</td><td></td><td></td><td>3.181 (5.338)</td></tr><tr><td>Type x Stage</td><td></td><td></td><td>-11.187* (5.681)</td></tr><tr><td>Preference</td><td>7.389*** (1.571)</td><td>7.061*** (1.453)</td><td>6.482*** (1.494)</td></tr><tr><td>Gender</td><td>3.171 (3.142)</td><td>2.826 (2.892)</td><td>3.786 (2.904)</td></tr><tr><td>Experience</td><td>-1.142 (1.645)</td><td>-0.711 (1.537)</td><td>-1.045 (1.524)</td></tr><tr><td>Familiarity</td><td>0.427 (1.577)</td><td>0.493 (1.455)</td><td>1.319 (1.489)</td></tr><tr><td>Attitude</td><td>-6.661* (3.096)</td><td>-6.991* (2.850)</td><td>-7.214* (2.811)</td></tr><tr><td>LogSigma</td><td>2.816*** (0.063)</td><td>2.732*** (0.063)</td><td>2.717*** (0.063)</td></tr></table>

Significant levels: +?? ≤ 0.1, \*?? ≤ 0.05, \*\*?? ≤ 0.01, \*\*\*?? ≤ 0.001.

Table B6. Results of Tobit Model with Effect Coding (-1,1)

<table><tr><td colspan="4">Dependent variable: Willingness to pay (%)(Log-likelihood = -541.179)</td></tr><tr><td></td><td>Coefficient (SE)</td><td>T Stat.</td><td>P – value</td></tr><tr><td>Intercept</td><td>55.205 (9.949)</td><td>5.549</td><td>2.87e-08***</td></tr><tr><td>Type(complements: -1)</td><td>0.936 (1.317)</td><td>0.710</td><td>0.477</td></tr><tr><td>Price (low: -1)</td><td>5.947 (1.317)</td><td>4.515</td><td>6.33e-06***</td></tr><tr><td>Stage (stage 1: -1)</td><td>2.518 (1.335)</td><td>1.886</td><td>0.059+</td></tr><tr><td>Type x Price</td><td>0.795 (1.335)</td><td>0.596</td><td>0.551</td></tr><tr><td>Type x Stage</td><td>-2.797 (1.420)</td><td>-1.969</td><td>0.049*</td></tr><tr><td>Preference</td><td>6.482 (1.494)</td><td>4.339</td><td>1.43e-05***</td></tr><tr><td>Gender</td><td>3.786 (2.904)</td><td>1.304</td><td>0.192</td></tr><tr><td>Experience</td><td>-1.045 (1.524)</td><td>-0.685</td><td>0.493</td></tr><tr><td>Familiarity</td><td>1.319 (1.489)</td><td>0.886</td><td>0.376</td></tr><tr><td>Attitude</td><td>-7.214 (2.811)</td><td>-2.566</td><td>0.010*</td></tr><tr><td>LogSigma</td><td>2.717 (0.063)</td><td>43.077</td><td>&lt;2e-16***</td></tr></table>

Significant levels: +?? ≤ 0.1, \*?? ≤ 0.05, \*\*?? ≤ 0.01, \*\*\*?? ≤ 0.001.
