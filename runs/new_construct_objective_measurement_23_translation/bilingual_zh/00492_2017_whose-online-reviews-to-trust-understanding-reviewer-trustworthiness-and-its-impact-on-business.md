---
otero_id: 492
otero_key: "UHPKF9MA"
title: "Whose online reviews to trust? Understanding reviewer trustworthiness and its impact on business"
authors: "Shankhadeep Banerjee; Samadrita Bhattacharyya; Indranil Bose"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.01.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Whose online reviews to trust? Understanding reviewer trustworthiness and its impact on business




---
奥特罗 ID：492
otero_key：“UHPKF9MA”
标题：“谁的在线评论值得信任？了解评论者的可信度及其对业务的影响”
作者：“Shankhadeep Banerjee；Samadrita Bhattacharyya；Indranil Bose”
年份：“2017”
期刊：《决策支持系统》
doi：“10.1016/j.dss.2017.01.006”
查询：“构造”
来源：“https://ais.kexu.win”
图片下载：假
---
# 谁的在线评论值得信赖？了解审稿人的可信度及其对业务的影响


Shankhadeep Banerjee, Samadrita Bhattacharyya, Indranil Bose




尚哈迪普·班纳吉、萨玛德里塔·巴塔查亚、因德兰尼尔·博斯


Indian Institute of Management Calcutta, India




印度管理学院 印度加尔各答


## a r t i c l e i n f o




（代码、公式、图片引用或其他非语言内容，无需翻译。）


Article history: Received 20 August 2016 Received in revised form 26 November 2016 Accepted 21 January 2017 Available online 27 January 2017




文章历史记录： 2016年8月20日收到 2016年11月26日以修订形式收到 2017年1月21日接受 2017年1月27日在线提供


Keywords: Online reviews Predictive model Regression analysis Reviewer characteristics Trustworthiness Yelp Electronic word-of-mouth Online reviewers Online trust




关键词： 在线评论 预测模型 回归分析 评论者特征 可信度 Yelp 电子口碑 在线评论者 在线信任


## a b s t r a c t




（代码、公式、图片引用或其他非语言内容，无需翻译。）


Why do top movie reviewers receive invitations to exclusive screenings? Even popular technology bloggers get free new gadgets for reviewing. How much do these reviewers really matter for businesses? While the impact of online reviews on sales of products and services has been well established, not much literature is available on impact of reviewers for businesses. Source credibility theory expounds how a communication's persuasiveness is affected by the perceived credibility of its source. So, perceived trustworthiness of reviewers should influence acceptance of reviews, and consequently should have an indirect impact on sales. Using local business review data from Yelp.com, this paper successfully tests the premise that reviewer trustworthiness positively moderates the impact of review-based online reputation on business patronages. Given the importance of reviewer trustworthiness, the next logical question is – how to estimate and predict it, if no direct proxy is available? We propose a theoretical model with several reviewer characteristics (positivity, involvement, experience, reputation, competence, sociability) affecting reviewer trustworthiness, and find all factors to be significant using the robust regression method. Further, using these factors, a predictive classification of reviewers into high and low level of potential trustworthiness is done using logistic regression with nearly 83% accuracy. Our findings have several implications - firstly, businesses should focus on building a good review-based online reputation; secondly, they should encourage top trustworthy reviewers to review their products and services; and thirdly, trustworthy reviewers could be identified and ranked using reviewer characteristics.




为什么顶级影评人会收到独家放映的邀请？即使是受欢迎的科技博主也能获得免费的新小玩意儿供审阅。这些审稿人对企业到底有多重要？虽然在线评论对产品和服务销售的影响已得到充分证实，但关于评论者对企业的影响的文献却很少。来源可信度理论阐述了传播的说服力如何受到其来源的感知可信度的影响。因此，评论者的可信度应该会影响评论的接受度，从而对销售产生间接影响。本文使用 Yelp.com 的本地商业评论数据，成功测试了评论者可信度积极调节基于评论的在线声誉对商业惠顾的影响的前提。鉴于审稿人可信度的重要性，下一个逻辑问题是——如果没有直接代理可用，如何估计和预测它？我们提出了一个理论模型，其中包含影响审稿人可信度的多个审稿人特征（积极性、参与度、经验、声誉、能力、社交能力），并使用稳健回归方法发现所有重要因素。此外，利用这些因素，使用逻辑回归对审阅者进行潜在可信度高低级别的预测分类，准确率接近 83%。我们的研究结果有几个启示：首先，企业应该专注于建立基于评论的良好在线声誉；其次，他们应该鼓励最值得信赖的评论者评论他们的产品和服务；第三，可以使用审阅者特征来识别和排名值得信赖的审阅者。


© 2017 Elsevier B.V. All rights reserved.




© 2017 Elsevier B.V. 保留所有权利。


## 1. Introduction




## 1.简介


The Internet has transformed the way consumers can decide to purchase a product or avail services of a business. Before the advent of the Internet, consumers either trusted word-of-mouth from acquaintances, or just used information provided by the seller to make a buy/no-buy decision. However, a third option has been created with the proliferation of online review sites which offer easy access to electronic wordof-mouth (eWOM) from peer consumers. eWOM can be defined as “any positive or negative statement made by potential, actual, or former customers about a product or company, which is made available to a multitude of people and institutions via the Internet” [1]. A plethora of websites like Amazon, Yelp, Glassdoor, IMDB, etc. allow peer-evaluated reviews for products, local businesses, employers, movies, etc., respectively. Internet users routinely access online reviews to obtain product information before purchasing [2], and a significant portion of these consumers report that they are influenced by online reviews in their decision-making [3]. According to BrightLocal Local Consumer Review




互联网改变了消费者决定购买产品或利用企业服务的方式。在互联网出现之前，消费者要么相信熟人的口碑，要么只是根据卖家提供的信息来做出购买/不购买的决定。然而，随着在线评论网站的激增，第三种选择已经出现，这些网站可以轻松访问同行消费者的电子口碑（eWOM）。电子口碑可以定义为“潜在的、实际的或以前的客户对产品或公司做出的任何正面或负面的陈述，这些陈述通过互联网提供给众多的人和机构”[1]。 Amazon、Yelp、Glassdoor、IMDB 等众多网站分别允许对产品、本地企业、雇主、电影等进行同行评估。互联网用户在购买前通常会访问在线评论以获取产品信息 [2]，其中很大一部分消费者表示，他们的决策受到在线评论的影响 [3]。根据 BrightLocal 当地消费者评论


Survey 2016 [4], 91% of US-based respondents have read online reviews to determine the quality of a local business. Thus, it can be expected that online reviews will have a significant impact on sales of products and services. This has been conclusively established multiple times in extant research on eWOM [5–7]. In the context of local businesses, the online reviewer communities have been found to add significantly to their revenues; for example, the average annual revenue from Yelp.com as reported by paid business accounts in a 2012 survey was US\$ 23,000 [8]. In certain categories like Home, the revenue was reported to be much higher at US\$ 54,000. Even opening a free business account on Yelp without any spending on advertising added an average annual revenue of US\$ 8000 to the local businesses. Other studies have directly linked Yelp ratings with revenue, such as a one-star increase in Yelp ratings was found to trigger 5–9% increase in revenue at restaurants [9]. So overall, it can be concluded that online reviewers do play an important role in influencing new customers in making purchase-related decisions.




2016 年调查[4]显示，91% 的美国受访者曾阅读在线评论来判断当地企业的质量。因此，可以预见，在线评论将对产品和服务的销售产生重大影响。在现有的电子口碑研究中，这一点已被多次证实[5-7]。在当地企业的背景下，在线评论社区可以显着增加他们的收入；例如，根据 2012 年付费企业账户的调查，Yelp.com 的平均年收入为 23,000 美元 [8]。据报道，在家居等某些类别中，收入要高得多，达到 54,000 美元。即使在 Yelp 上开设一个免费的企业帐户而不花任何广告费用，也能为当地企业平均每年增加 8000 美元的收入。其他研究将 Yelp 评级与收入直接联系起来，例如 Yelp 评级增加一星被发现会引发餐馆收入增加 5-9% [9]。总的来说，可以得出结论，在线评论者确实在影响新客户做出购买相关决策方面发挥着重要作用。


While there is no doubt regarding the overall importance of online reviews and reviewer communities at large, at a micro level not all individual reviews can have equal impact on consumers for making purchase-related decisions. Using feedback mechanisms on reviews like helpfulness votes, it has been observed that some reviews are more accepted and appreciated by readers than others. Reviews which are considered more helpful have been found to have a greater influence on customers' purchase decisions in comparison to other reviews [10]. Research on eWOM has discovered several factors which have been found to significantly affect helpfulness or usefulness of a review. These include review length/depth (word count) and extremity (star rating) [11]; content and style [12]; readability [13]; reader's objectives [14]; subjectivity, informativeness, and linguistic correctness [15]; etc. However, one factor which gets comparatively lesser mention is the trustworthiness of a reviewer producing a review. In our daily lives, we value opinions of people we trust, much more than those of people we do not. Source credibility theory expounds how a communication's persuasiveness is affected by the perceived credibility of the source of communication. So, applying this theory in the context of eWOM, we can expect that acceptance of a review by a prospective customer should, to some extent, get affected by the perceived trust on the reviewer. Earlier studies have conceptualized product review helpfulness as a second-order formative construct manifested through perceived source credibility, and other content-related factors [16]. For instance, reviews that are written by self-described experts have been found to be more helpful than others [17]. Even just simple disclosure of identity information by reviewers in product reviews has been found to be positively associated with acceptance of reviews, subsequently followed by better sales [7]. Thus, there seems to be ample evidence pointing to the inherent need of eWOM readers to be able to know and trust the reviewers in order to accept their reviews. Since acceptance of a review can affect the decision of a customer either in favor of or against visiting a local business, overall patronages of the business should be indirectly affected by average trustworthiness of all reviewers reviewing it. While logically the argument holds well, we are not aware of any previous research till date which has validated the proposition for local businesses. Earlier attempts to test direct impact of top reviewers on product sales did not generate support for the proposed hypothesis owing to certain limitations of data [10]. Hence, for this paper we propose to take up this research question:




虽然在线评论和整个评论者社区的整体重要性毫无疑问，但在微观层面上，并非所有个人评论都能对消费者做出购买相关决策产生同等影响。通过使用有用性投票等评论反馈机制，我们发现某些评论比其他评论更容易被读者接受和欣赏。与其他评论相比，被认为更有帮助的评论对客户的购买决策具有更大的影响力 [10]。对电子口碑的研究发现了几个显着影响评论的帮助性或有用性的因素。其中包括评论长度/深度（字数）和极端性（星级）[11]；内容和风格[12]；可读性[13]；读者的目标[14]；主观性、信息性和语言正确性[15]；然而，相对较少提及的一个因素是审稿人的可信度。在我们的日常生活中，我们更重视我们信任的人的意见，而不是我们不信任的人的意见。来源可信度理论阐述了传播来源的感知可信度如何影响传播的说服力。因此，在电子口碑的背景下应用这一理论，我们可以预期，潜在客户对评论的接受程度应该在某种程度上受到对评论者的感知信任的影响。早期的研究将产品评论的有用性概念化为通过感知来源可信度和其他内容相关因素表现出来的二阶形成性结构[16]。例如，由自称专家撰写的评论被发现比其他人更有帮助[17]。研究发现，即使是评论者在产品评论中简单地披露身份信息，也会与评论的接受度呈正相关，进而带来更好的销售[7]。因此，似乎有足够的证据表明电子口碑读者的内在需求是能够了解并信任审稿人，以便接受他们的评论。由于评论的接受可能会影响客户赞成或反对访问当地企业的决定，因此该企业的整体惠顾应该间接受到所有评论者的平均可信度的影响。虽然从逻辑上讲，这一论点是成立的，但迄今为止，我们不知道之前有任何研究为当地企业验证了这一主张。由于数据的某些限制，早期尝试测试顶级评论者对产品销售的直接影响并没有为所提出的假设提供支持[10]。因此，对于本文，我们建议探讨这个研究问题：


RQ1: Does overall trustworthiness of reviewers have any impact on the number of customers visiting the business being reviewed?




RQ1：审核者的整体可信度对访问被审核企业的客户数量有影响吗？


The managerial implication of investigating this question is that it may benefit businesses by helping them focus on identifying and targeting the most trustworthy reviewers, and encouraging them to review their products and services. This idea is very similar to the popular practice of top movie critics getting exclusive invitations to premier screenings for writing reviews, or technology companies sending new gadgets to technology bloggers for their expert public reviews. But what we are suggesting is to make the practice more widespread if the impact of reviewer trustworthiness on business patronages is found to be significant.




调查这个问题的管理意义在于，它可以帮助企业专注于识别和定位最值得信赖的评论者，并鼓励他们评论自己的产品和服务，从而使企业受益。这个想法与流行的做法非常相似，顶级影评人获得独家邀请参加首映并撰写评论，或者科技公司向科技博主发送新产品以供其专家公开评论。但我们建议的是，如果发现审稿人的可信度对企业赞助的影响很大，则应扩大这种做法。


Assuming that reviewer trustworthiness is found to have an impact on business patronages, the next logical step will be to find a way to identify the trustworthy reviewers. Some online review sites like Yelp allows one to follow reviewers one perceives to be trustworthy, therefore the number of followers of a reviewer can be a good measure of reviewer trustworthiness. However, most websites do not offer such possibilities. In such cases, the only way will be to look into some of the available reviewer profile characteristics, and try to predict the level of trustworthiness. Xu [18] has found that these profile characteristics act as cues of source trustworthiness and play an important role in consumer decision making. An extension of source credibility theory by McCroskey and Jenson [19] identify five source characteristics which can affect credibility – competence, character, sociability, composure, and extroversion. However, this has never been applied in the context of online reviews till date. So we do not know if these dimensions hold true for faceless online reviewers about whom very little personal information is shared on review sites. With the objective of trying to develop a predictive model for reviewer trustworthiness using reviewer characteristics, the following research question is also proposed:




假设评论者的可信度被发现对商业赞助有影响，下一个合乎逻辑的步骤将是找到一种方法来识别值得信赖的评论者。一些在线评论网站（例如 Yelp）允许人们关注人们认为值得信赖的评论者，因此评论者的关注者数量可以很好地衡量评论者的可信度。然而，大多数网站不提供这种可能性。在这种情况下，唯一的方法是研究一些可用的审阅者资料特征，并尝试预测可信度水平。 Xu [18]发现这些个人资料特征可以作为来源可信度的线索，并在消费者决策中发挥重要作用。 McCroskey 和 Jenson [19] 对来源可信度理论进行了扩展，确定了可能影响可信度的五种来源特征——能力、性格、社交性、沉着和外向。然而，迄今为止，这从未应用于在线评论的背景下。因此，我们不知道这些维度是否适用于不露面的在线评论者，他们在评论网站上分享的个人信息很少。为了尝试使用审稿人特征开发审稿人可信度的预测模型，还提出了以下研究问题：


RQ2: Which reviewer characteristics determine the trustworthiness of a reviewer?




RQ2：哪些审稿人特征决定了审稿人的可信度？


To find answers to the two research questions, a dataset from Yelp. com is used, which contains reviews by consumers for over 77K local businesses across multiple cities in four countries. The data includes attributes on reviewers, businesses, reviews, and check-ins (customer visiting a business), and hence is ideal for conducting this research. The number of check-ins is used as a proxy for business patronages, and average star ratings multiplied by review count is used as a proxy for online reputation of a business. We find that reviewer trustworthiness measured in terms of number of followers of reviewers, has a positive moderating effect on the relationship between online reputation and patronages of a business. This means that while better online reputation is associated with better patronages, the relationship can be further boosted if the reviewers are more trustworthy, as compared to if they are less so. Furthermore, we take help from McCroskey's research and published literature on eWOM to identify six reviewer attributes (competence, experience, sociability, reputation, involvement, and positivity) which could be hypothesized to influence trustworthiness in the context of a reviewer community. The proxy measures of these attributes are used as independent variables, and with trustworthiness as a dependent variable, a robust regression analysis is done to identify the significant factors. Finally, a logistic regression model is built to classify reviewers into ‘high’ or ‘low’ level of trustworthiness. Our results show a classification accuracy of nearly 83% implying that the model is a pretty good predictor of reviewer trustworthiness.




为了找到这两个研究问题的答案，来自 Yelp 的数据集。使用 com，其中包含消费者对四个国家多个城市超过 77,000 家本地企业的评论。这些数据包括评论者、企业、评论和签到（客户访问企业）的属性，因此非常适合进行此项研究。签到次数被用作企业光顾的代理，平均星级乘以评论数被用作企业在线声誉的代理。我们发现，以评论者的追随者数量来衡量评论者的可信度，对在线声誉和企业惠顾之间的关系具有积极的调节作用。这意味着，虽然更好的在线声誉与更好的惠顾相关，但如果评论者更值得信赖，那么与不那么值得信赖的人相比，这种关系可以进一步加强。此外，我们借助 McCroskey 的研究和已发表的 eWOM 文献来确定审稿人的六种属性（能力、经验、社交能力、声誉、参与度和积极性），这些属性可能会影响审稿人社区背景下的可信度。这些属性的代理度量被用作自变量，并且以可信度作为因变量，进行稳健的回归分析来识别重要因素。最后，建立逻辑回归模型，将评论者分为“高”或“低”可信度级别。我们的结果显示分类准确率接近 83%，这意味着该模型可以很好地预测审稿人的可信度。


Overall, this paper makes relevant contributions to literature, being the first paper (to the best of our knowledge, till date) to establish a link between trustworthiness of reviewers and business patronages. It is also one of the few works to identify and empirically validate several reviewer characteristics which can influence trustworthiness. Furthermore, the predictive model developed in this paper can be customized and used by businesses to identify trustworthy reviewers when direct information about reviewers is unavailable. Even online review sites can use it to recommend most trustworthy reviewers and their reviews to the users. Apart from practical utility, the findings from this paper have significant managerial implications for businesses as well. Firstly, businesses can focus on building a good review-based online reputation; secondly, they can encourage top trustworthy reviewers to review their products and services; and thirdly, trustworthy reviewers can be identified and ranked using reviewer-related characteristics.




总体而言，本文对文献做出了相关贡献，是第一篇在审稿人的可信度与商业赞助之间建立联系的论文（据我们所知，迄今为止）。它也是为数不多的识别和实证验证可能影响可信度的审稿人特征的少数著作之一。此外，当无法获得有关审稿人的直接信息时，本文开发的预测模型可以被企业定制和使用来识别值得信赖的审稿人。即使在线评论网站也可以使用它向用户推荐最值得信赖的评论者及其评论。除了实际用途之外，本文的研究结果对企业也具有重要的管理意义。首先，企业可以专注于建立基于评论的良好在线声誉；其次，他们可以鼓励最值得信赖的评论者评论他们的产品和服务；第三，可以使用与审阅者相关的特征来识别和排名值得信赖的审阅者。


## 2. Literature review




## 2.文献综述


Most of the eWOM literature has focused either on finding factors associated with helpfulness of reviews [15,16,20–24], or on discovering the impact of reviews on sales [7,15,25–28]. There are several studies which give importance to reviewers mostly in the context of influencing the helpfulness of reviews [15,17,18,28–32]. For the propositions related to how reviewers influence sales, mixed results have been found. One study [9] has shown a significant positive impact of reviewers certified as ‘Elite’ in Yelp on business sales whereas another study [10] has not found any significant impact of rankings of reviewers on the sales related ranks of products at Amazon.




大多数电子口碑文献要么关注于寻找与评论有用性相关的因素[15,16,20–24]，要么关注于发现评论对销售的影响[7,15,25–28]。有几项研究主要在影响评论有用性的背景下重视审稿人[15,17,18,28–32]。对于与评论者如何影响销售相关的命题，结果好坏参半。一项研究 [9] 表明，在 Yelp 中被认证为“精英”的评论者对企业销售有显着的积极影响，而另一项研究 [10] 则没有发现评论者排名对亚马逊销售相关产品排名有任何显着影响。


However, there are only few studies speci c to reviewer trustworthiness. A study by Xu [18] adopts a 2 (number of trusted members: small, large) × 2 (profile picture: without, with) × 2 (review valence: negative, positive) between-participants experiment to explore how two personal profile characteristics, reputation cue and profile picture, influence cognitive trust and affective trust towards the reviewer and perceived review credibility respectively and in a combinatorial manner. The findings of the study have shown that reputation cue and profile picture cue contributes differently to users' affective trust and cognitive trust towards the reviewer. Reputation cue that is generated by the system, is found to influence both affective and cognitive dimensions of trust, whereas the self-generated cue of profile picture only impacts affective trust. Reputation cue has a direct influence on perceived review credibility, whereas the influence of profile picture on perceived review credibility is dependent on review valence.




然而，专门针对审稿人可信度的研究很少。 Xu[18]的研究采用2（可信成员数量：小、大）×2（个人资料图片：无、有）×2（评论效价：负面、正面）参与者间实验，探讨两种个人档案特征、声誉线索和个人资料图片如何分别以组合方式影响对审稿人的认知信任和情感信任以及感知的审稿可信度。研究结果表明，声誉线索和个人资料图片线索对用户对评论者的情感信任和认知信任的贡献不同。研究发现，系统生成的声誉线索会影响信任的情感和认知维度，而个人资料图片自身生成的线索仅影响情感信任。声誉线索对感知评论可信度有直接影响，而个人资料图片对感知评论可信度的影响取决于评论效价。


But overall the area of reviewer trustworthiness is not widely studied. Hence, RQ1 is a good question to start a series of investigations on the same theme. Also, factors influencing reviewer trustworthiness are only implied in eWOM literature, mainly in the context of review credibility and usefulness. Liu and Park [33] have found that the reviewer's expertise and reputation influence the perceived value of a review. Ghose and Ipeirotis [15] have studied the impact of average helpfulness votes received per review and personal information disclosure on helpfulness of review. Otterbacher [34] has found that reviewer characteristics like the number of reviews posted by a reviewer and the number of helpful votes received by the reviewer on the whole, impacts the helpfulness vote of a review. Liu et al. [35] has discovered that reviewer expertise and writing style have an impact on review helpfulness. Ngo-Ye and Sinha [31] have employed a reviewer”'s RFM (Recency, Frequency, Monetary Value) dimensions to characterize reviewer engagement and found that inclusion of these dimensions helps improve prediction of online review helpfulness. Some reviewer characteristics that are found to impact sales (through decrease in perceived uncertainty of buyers) are reviewer quality and reviewer exposure [28]. Another key finding related to reviewers is that reviews written by a self-described expert are more helpful than those that are not [17]. Shen et al. [36] have empirically examined how online reviewers' behaviors are driven by the desire to gain attention and online reputation.




但总体而言，审稿人可信度领域并未得到广泛研究。因此，RQ1 是针对同一主题展开一系列调查的好问题。此外，影响审稿人可信度的因素仅在电子口碑文献中隐含，主要是在审稿可信度和有用性的背景下。 Liu 和 Park [33] 发现审稿人的专业知识和声誉会影响审稿的感知价值。 Ghose 和 Ipeirotis [15] 研究了每次评论收到的平均有用性投票和个人信息披露对评论有用性的影响。 Otterbacher [34] 发现，审稿人的特征（例如审稿人发布的审稿数量和审稿人收到的有用投票数量）会影响审稿的有用性投票。刘等人。 [35]发现审稿人的专业知识和写作风格对审稿的有用性有影响。 Ngo-Ye 和 Sinha [31] 采用了评论者的 RFM（新近度、频率、货币价值）维度来描述评论者的参与度，并发现包含这些维度有助于提高对在线评论有用性的预测。一些影响销售的评论者特征（通过减少买家感知的不确定性）是评论者质量和评论者曝光率 [28]。与评论者相关的另一个重要发现是，由自称专家撰写的评论比非专家撰写的评论更有帮助。 [17] Shen等人[36]实证研究了在线评论者的行为是如何受到获得关注和在线声誉的驱动的。


While there exist research that study one or more of reviewer characteristics impacting review helpfulness, we have not found any study that has tried to find the impact of reviewer characteristics on reviewer trustworthiness or credibility. This may be because most studies have treated reviewer trust as an implicit mechanism through which review helpfulness is affected by reviewer characteristics, and hence ‘trust’ is mentioned only when explaining the results. Another reason can be the absence of a good proxy to measure reviewer trustworthiness when conducting empirical analysis. The closest relevant work that can be found is by Ku et al. [30] which has attempted to discriminate reviewers with a high reputation from those with a low reputation on the basis of their web trust network and review behaviors in Epinions.com. Their results have indicated that trust intensity, average trust intensity of trustors, degree of review focus in the target category, and average product rating in the target category, have successfully discriminated reviewers into the two groups. Ku et al. have considered reviewer reputation to be the dependent variable and have classified it as high/low based on the number of helpfulness votes received; whereas trust intensity of a reviewer has been measured by his/her centrality in the community trust network. This independent factor is found to be positively associated with reputation. However, it can be argued that average review helpfulness votes is not a good measure for reputation, but rather is a better indicator of reviewer competence or expertise in writing reviews. Also, reputation can be based on external certification as well, like being branded as ‘Elite Reviewer’ in case of Yelp.com. So it can be considered to be an independent variable. Thus, both competence and reputation can be treated as independent variables affecting reviewer trustworthiness. This is the approach we adopt and measure reviewer trustworthiness on the basis of the number of followers he/she has gained, as the dependent variable, and treat reviewer characteristics as independent variables.




虽然有研究研究影响审稿有用性的一个或多个审稿人特征，但我们还没有发现任何研究试图找出审稿人特征对审稿人可信度或可信度的影响。这可能是因为大多数研究都将审稿人的信任视为一种隐性机制，审稿人的特征会影响审稿的帮助性，因此只有在解释结果时才提到“信任”。另一个原因可能是在进行实证分析时缺乏良好的代理来衡量审稿人的可信度。可以找到的最接近的相关工作是 Ku 等人的工作。 [30] 试图根据 Epinions.com 的网络信任网络和评论行为来区分声誉高的评论者和声誉低的评论者。他们的结果表明，信任强度、信任者的平均信任强度、目标类别中评论的关注程度以及目标类别中的平均产品评级，已经成功地将评论者区分为两组。库等人。将审稿人声誉视为因变量，并根据收到的有用票数将其分类为高/低；而审阅者的信任强度是通过他/她在社区信任网络中的中心地位来衡量的。研究发现这个独立因素与声誉呈正相关。然而，可以说平均评论有用性投票并不是衡量声誉的良好指标，而是评论者撰写评论的能力或专业知识的更好指标。此外，声誉也可以基于外部认证，例如在 Yelp.com 中被称为“精英评论员”。所以可以认为它是一个自变量。因此，能力和声誉都可以被视为影响审稿人可信度的自变量。这是我们采用的方法，根据评论者获得的关注者数量作为因变量来衡量评论者的可信度，并将评论者特征视为自变量。


The key literature related to online reviewers is summarized in Table 1 and shows the various relationships that have been studied in this context. Our study intends to cover the research gaps by establishing the appropriate relationship between reviewer impression (more specifically trustworthiness) and sales (or patronages); and also between a variety of reviewer related attributes and trustworthiness.




表 1 总结了与在线审稿人相关的关键文献，并显示了在此背景下研究的各种关系。我们的研究旨在通过建立评论者印象（更具体地说是可信度）和销售（或惠顾）之间的适当关系来弥补研究空白​​；以及各种审稿人相关属性和可信度之间的关系。


## 3. Hypotheses development




## 3. 假设发展


Academicians often confuse between the concepts of trust and trustworthiness, and hence most of the trust literature does not mention trustworthiness, even though most of the work relates to that [39]. Trust can be defined as “the willingness of a party to be vulnerable to the actions of another party based on the expectation that the other will perform a particular action important to the trustor, irrespective of the ability to monitor or control that other party” [40]. Thus, trust can be treated as a three-part relation where person X trusts person Y to do action A [41]. So, if Y is not able to do A, then X may lose trust on Y in doing A anymore, but Y still may be considered trustworthy by X. However, if Y betrays X in some way, then X will not consider Y to be trustworthy anymore, and hence may not trust Y even for other activities. So, trustworthiness of a person refers to how much the person is ‘deserving of trust’. Which means that trustworthiness begets trust through a causal connection [41]. If we extend the argument a bit further, trustworthiness of a person can also be a causal factor in deciding how much to trust his/her opinions on some matter. This is similar to what the Source Credibility Theory (SCT), a well-established theory in communication, also talks about.




院士们经常混淆信任和可信度的概念，因此大多数信任文献都没有提及可信度，尽管大多数工作都与可信度相关[39]。信任可以被定义为“一方愿意受到另一方行为的影响，其基础是预期另一方将执行对委托人而言重要的特定行动，而不管监督或控制另一方的能力如何”[40]。因此，信任可以被视为三部分关系，其中 X 信任 Y 执行操作 A [41]。因此，如果Y不能做A，那么X可能会在做A时失去对Y的信任，但Y仍然可能被X认为是值得信任的。然而，如果Y以某种方式背叛了X，那么X将不再认为Y是值得信任的，因此即使对于其他活动也可能不会信任Y。所以，一个人的可信度是指这个人“值得信任”的程度。这意味着可信度通过因果关系产生信任[41]。如果我们进一步扩展这个论点，一个人的可信度也可能是决定在多大程度上信任他/她对某些事情的观点的因果因素。这与传播学中成熟的理论来源可信度理论（SCT）也谈到的类似。


According to the SCT, the persuasiveness of a communication is determined in part by the perceived credibility of the source of communication [42], and trustworthiness is the most influential dimension of source credibility [43]. So, if X is trying to persuade Y to take action A, then whether Y feels persuaded enough to do A or not, will depend to some extent on how much trustworthy Y considers X. SCT has been experimentally established by Hovland and Weiss [42] by presenting identical content to subjects using sources they consider having ‘high trustworthiness’ and ‘low trustworthiness’. They have found that the immediate reaction to ‘fairness’ of presentation and ‘justifiability’ of conclusions drawn by the sources have significantly depended on the subject's initial opinion on the matter, and his evaluation of trustworthiness of source. Opinions among audience are found to have changed immediately after communication by a ‘high trustworthy’ source, than when presented by a ‘low trustworthy’ source. However, no difference is found in the factual information being learned from the communication. Thus, the SCT deals with the opinions being affected, and not factual information, based on the perceived trustworthiness of the source of communication. Multiple studies have adopted the SCT in areas of persuasive marketing, brand building, and design of logos and websites [44].




根据 SCT，沟通的说服力部分取决于沟通来源的感知可信度 [42]，而可信度是来源可信度最有影响力的维度 [43]。因此，如果 X 试图说服 Y 采取行动 A，那么 Y 是否有足够的说服力去做 A，在某种程度上取决于 Y 认为 X 的可信程度。SCT 是由 Hovland 和 Weiss [42] 实验性建立的，通过使用他们认为具有“高可信度”和“低可信度”的来源向受试者呈现相同的内容。他们发现，对消息来源所得出的结论的“公平性”和“合理性”的立即反应在很大程度上取决于受试者对此事的初步看法以及他对消息来源可信度的评估。研究发现，与“低可信度”来源相比，在“高可信度”来源沟通后，受众的观点立即发生了变化。然而，从通信中了解到的事实信息没有发现任何差异。因此，SCT 根据通信来源的感知可信度来处理受影响的意见，而不是事实信息。多项研究已在说服性营销、品牌建设以及徽标和网站设计领域采用了 SCT [44]。


Summary of key literature on online reviewers.




有关在线审稿人的主要文献摘要。


<table><tr><td>Relationship studied</td><td>Key literature</td></tr><tr><td>Reviewer attributes → Review acceptance</td><td>Average helpfulness votes received per review and personal information disclosure [15], Engagement (recency, frequency, monetary value) [31], Historical rating distribution [32], Expertise and reputation [33], Number of reviews and total helpful votes [34], Expertise and writing style [35]</td></tr><tr><td>Reviewer attributes → Sales</td><td>Quality and exposure [28], Certified elite [9]</td></tr><tr><td>Reviewer attributes → Reviewer impression</td><td rowspan="2">Reputation cue and profile picture [18], Review quality and reviewer photos [29], Centrality in trust network [30], Helpfulness votes [5-7]</td></tr><tr><td>Review acceptance → Sales</td></tr><tr><td>Reviewer impression → Review acceptance</td><td>Credibility [14,16,37]</td></tr><tr><td>Reviewer impression → Sales</td><td>Top ranked [10]</td></tr><tr><td>Others</td><td>Reviewers&#x27; strategic behaviors [36], Impact of ranking systems on reviewer well-being and engagement [38]</td></tr></table>




<table><tr><td>研究的关系</td><td>关键文献</td></tr><tr><td>审稿人属性→审稿接受</td><td>每次审稿和个人信息披露收到的平均有用票数[15]、参与度（新近度、频率、货币价值）[31]、历史评级分布[32]、专业知识和声誉[33]、评论数量和总有用票数[34]，专业知识和写作风格 [35]</td></tr><tr><td>审稿人属性 → 销售</td><td>质量和曝光度 [28]，认证精英 [9]</td></tr><tr><td>审稿人属性 → 审稿人印象</td><td rowspan="2">声誉提示和个人资料图片 [18]，审稿质量和审稿人照片 [29]，信任网络的中心地位[30]，有用票数[5-7]</td></tr><tr><td>评论接受→销售</td></tr><tr><td>评论者印象→评论接受</td><td>可信度[14,16,37]</td></tr><tr><td>评论者印象→销售</td><td>排名最高[10]</td></tr><tr><td>其他</td><td>审稿人&#x27;战略行为[36]，排名系统对审稿人福祉和参与度的影响[3​​8]</td></tr></table>


In the online context, trust plays an important role for customers in making purchase decisions since there is an information asymmetry between transacting parties. Earlier research models focused mostly on customer perceptions of the business and website, as well as consumer characteristics as the predictors of online trust. However, with the rise of social media, use of customer reviews has become a significant determinant of how trust builds up online [45]. According to the BrightLocal Local Consumer Survey 2016 [4], 84% of people trust online reviews as much as a personal recommendation, and 90% form their opinion about a business by reading less than 10 reviews. Online reviews are mostly personal opinions about products and services by peer customers, since most of the factual information is already mentioned in the item description. Thus, the SCT can apply well in the context of online reviews. It can indicate whether a customer trusts the reviews posted by a reviewer, and whether that depends on the perceived trustworthiness of the reviewer. This highlights the importance of reviewer trustworthiness in the context of online reviews, since trust and acceptance of a review's recommendation can lead a customer towards either a buy or no-buy decision, hence influencing the sales of the product or service.




在网络环境中，由于交易双方之间存在信息不对称，信任对于客户做出购买决策起着重要作用。早期的研究模型主要关注客户对业务和网站的看法，以及作为在线信任预测因素的消费者特征。然而，随着社交媒体的兴起，客户评论的使用已成为在线建立信任的重要决定因素[45]。根据 2016 年 BrightLocal 本地消费者调查[4]，84% 的人相信在线评论就像相信个人推荐一样，90% 的人通过阅读少于 10 条评论来形成对企业的看法。在线评论大多是同行客户对产品和服务的个人意见，因为大多数事实信息已经在商品描述中提及。因此，SCT 可以很好地应用于在线评论的背景下。它可以表明客户是否信任评论者发布的评论，以及这是否取决于评论者的感知可信度。这凸显了在线评论中评论者可信度的重要性，因为对评论推荐的信任和接受可以导致客户做出购买或不购买的决定，从而影响产品或服务的销售。


Impact of online customer reviews on sales is a well-researched area [2,5,7,25–27]. So it is logical to expect that the characteristics and perceptions of the sources of reviews should also have some impact on sales [9,10,28]. However, the association may not be a straightforward positive relationship, since just having reviews written by more popular and trustworthy reviewers may not necessarily lead to higher sales or to more customers visiting a business. This is because reviewers can be writing negative comments which should adversely affect customers' intent to visit. So, it is ultimately the rating and review content that will directly affect patronages and consequently, overall sales volumes. But reviews, either positive or negative, from more trustworthy sources should be better accepted as compared to less trustworthy sources. A lot of research has been done to establish the association between source credibility and attitude towards content [46,47]. So, the positive association between review-based online reputation of business and its patronages will become stronger if the level of trustworthiness of reviewers is higher. Accordingly, we propose the following two hypotheses to empirically test our arguments, specifically in the context of local business reviews:




在线客户评论对销售的影响是一个经过深入研究的领域 [2,5,7,25–27]。因此，可以合理地预期，评论来源的特征和看法也应该对销售产生一些影响 [9,10,28]。然而，这种关联可能不是一种直接的积极关系，因为仅仅由更受欢迎和值得信赖的评论者撰写的评论不一定会带来更高的销售额或更多的客户访问企业。这是因为评论者可能会撰写负面评论，这会对客户的访问意图产生不利影响。因此，最终评级和评论内容将直接影响顾客量，从而影响整体销量。但与不太值得信赖的来源相比，来自更值得信赖的来源的评论，无论是正面还是负面的，都应该更容易被接受。为了建立来源可信度和对内容的态度之间的关联，已经进行了大量的研究[46,47]。因此，如果评论者的可信度越高，基于评论的企业在线声誉与其惠顾之间的正相关关系就会变得更强。因此，我们提出以下两个假设来实证检验我们的论点，特别是在本地商业评论的背景下：


H1a. Review-based online reputation of a business is positively associ ated with the patronages generated by the business.




H1a。企业基于评论的在线声誉与企业产生的惠顾呈正相关。


H1b. Average perceived trustworthiness of reviewers reviewing a business positively moderates the association between online reputation and patronages of the business.




H1b。评论企业的评论者的平均感知可信度积极调节在线声誉与企业惠顾之间的关联。


For identifying reviewer characteristics that can affect trustworthiness, along with eWOM literature, we resorted to the classic work of McCroskey and Jenson [19] which has expounded five dimensions of source credibility. The dimensions are competence, character, sociability, composure, and extroversion, of which the first three are found to be more significant. Each dimension is further broken down into certain values (e.g., character dimension has values kindness, sympathy, selflessness, and virtue). For theory building, we have used some of these dimensions and values that seem appropriate in the context of reviewers, along with other factors identified in literature on eWOM that are found to affect helpfulness of review through latent trust on source of reviews. Accordingly, six hypotheses have been proposed.




为了识别可能影响可信度的审稿人特征以及电子口碑文献，我们求助于 McCroskey 和 Jenson [19] 的经典著作，该著作阐述了来源可信度的五个维度。这些维度包括能力、性格、社交能力、冷静和外向，其中前三个更为重要。每个维度进一步细分为某些价值观（例如，性格维度具有善良、同情、无私和美德的价值观）。为了构建理论，我们使用了一些在评论者的背景下似乎合适的维度和价值观，以及电子口碑文献中确定的其他因素，这些因素被发现通过对评论来源的潜在信任影响评论的有用性。据此，提出了六种假设。


Positivity among leaders has been found to impact followers' perceived trust and evaluation of leader's effectiveness [48]. McCroskey's character dimension also pointed to kindness and sympathy leading to more source credibility. In the online review context, these findings imply that reviewers with a tendency towards posting more sympathetic review with positive polarity in rating businesses, will be more trusted by other users. This is also proposed and verified by Fang et al. [32] using TripAdvisor data. They have found that reviewers who posted more reviews stressing the positive aspects are more likely to receive helpful votes than an author who stressed the negative aspects. In terms of star ratings, a higher average can be considered more positive and sympathetic leading to an increase in trustworthiness. This leads to the following hypothesis:




研究发现，领导者的积极性会影响追随者的信任感和对领导者有效性的评估[48]。麦克罗斯基的性格维度也表明善良和同情心会带来更多的消息来源可信度。在在线评论环境中，这些发现意味着，在对企业进行评级时倾向于发布更具同情心的正面评论的评论者将更受其他用户信任。这也是Fang等人提出并验证的。 [32] 使用 TripAdvisor 数据。他们发现，发表更多强调积极方面的评论的审稿人比强调消极方面的作者更有可能获得有用的选票。就星级评分而言，较高的平均值可以被认为更加积极和富有同情心，从而提高可信度。这导致以下假设：


H2a. Reviewer's positivity in rating businesses is positively associated with the perceived reviewer trustworthiness.




H2a。评论者对企业评级的积极性与评论者的可信度呈正相关。


Otterbacher [34] has found that the number of reviews posted by a reviewer is positively associated with the number of helpfulness votes received for the review. Liu and Park [33] too hypothesized number of reviews as one of the factors impacting review usefulness. So, it can be expected that an increase in the number of reviews, which is a measure of reviewer involvement in reviewing products or services, will be associated with an increase in trustworthiness of the reviewer. Hence, the following hypothesis is proposed:




Otterbacher [34] 发现审稿人发表的评论数量与该评论收到的有用票数呈正相关。 Liu 和 Park [33] 也假设评论数量是影响评论有用性的因素之一。因此，可以预期，评论数量的增加（衡量评论者参与评论产品或服务的程度）将与评论者可信度的增加相关。因此，提出以下假设：


H2b. The amount of reviewer's involvement in reviewing businesses is positively associated with the perceived reviewer trustworthiness.




H2b。审核者参与审核企业的程度与审核者的可信度呈正相关。


Expertise dimension of source credibility refers to perceiving the source as trained, experienced, authoritative, skilled, and informed [43]. So one of the important aspects of source credibility is experience in the area under consideration. People with more experience in a field are generally more trusted than inexperienced ones in matters pertaining to that field. In the context of online reviews, experience will refer to the time period for which a reviewer has been a member of the online review community. We can expect reviewers with more years of experience in using the review site, to be more trusted and have more followers among the community as compared to newbies. Thus, this leads to the following hypothesis:




消息来源可信度的专业维度是指将消息来源视为训练有素、经验丰富、权威、熟练且消息灵通的[43]。因此，来源可信度的重要方面之一是所考虑领域的经验。在某个领域有更多经验的人通常比没有经验的人在该领域的相关事务上更值得信任。在在线评论的背景下，经验是指评论者成为在线评论社区成员的时间段。我们可以预期，与新手相比，拥有多年使用评论网站经验的评论者会更受信任，并且在社区中拥有更多的追随者。因此，这导致了以下假设：


H2c. Reviewer's experience in online review website is positively associated with the perceived reviewer trustworthiness.




H2c。审稿人在在线审稿网站上的体验与审稿人的可信度呈正相关。


Liu and Park [33] have found that reviewer reputation affects the perceived value of a review. Consumers may infer credibility of reviewer directly from his reputation as suggested by the website or other members of community [18]. One of the values in McCroskey's competence dimension is qualification, which in the context of online reviews will be certification of being a good reviewer by the online review site. Being certified as ‘Elite’ reviewer in Yelp can be a good indicator of a reviewer's competence. It will also enhance a reviewer's reputation in the community. A quantifiable measure of reputation can be the total number of years a reviewer has been certified as ‘Elite’. It will be logical to expect that more the reputation of a reviewer, more will be the perceived trust on the reviewer. Thus, we propose the following hypothesis:




Liu 和 Park [33] 发现评论者的声誉会影响评论的感知价值。消费者可以根据网站或社区其他成员的建议直接从评论者的声誉推断评论者的可信度[18]。 McCroskey 能力维度的价值之一是资格，在在线评论的背景下，资格将是在线评论网站对成为优秀评论者的认证。在 Yelp 中被认证为“精英”审稿人可以很好地表明审稿人的能力。它还将提高审稿人在社区中的声誉。声誉的量化衡量标准可以是审稿人被认证为“精英”的总年数。合乎逻辑的是，审稿人的声誉越高，对审稿人的信任度越高。因此，我们提出以下假设：


H2d. Reviewer's reputation in online review website is positively associated with the perceived reviewer trustworthiness.




H2d。在线评论网站中评论者的声誉与评论者的可信度呈正相关。


A more competent reviewer will be able to write more useful reviews. Thus competence of a reviewer can be measured using average votes received per review by the reviewer. A competent source having more value is usually considered to be more credible, according to McCroskey's research. Ghose and Ipeirotis [15] too consider average helpfulness votes received by reviewer as one of the possible reviewer characteristics that may affect review helpfulness. Hence, it can be expected that reviewer's competence in writing useful reviews may affect reviewer trustworthiness. Thus, the following hypothesis is proposed:




更有能力的审稿人将能够写出更有用的评论。因此，可以使用审阅者每次审阅收到的平均投票来衡量审阅者的能力。根据麦克罗斯基的研究，具有更多价值的有能力的来源通常被认为更可信。 Ghose 和 Ipeirotis [15] 也将审稿人收到的平均有用性投票视为可能影响审稿有用性的审稿人特征之一。因此，可以预期审稿人撰写有用审稿的能力可能会影响审稿人的可信度。因此，提出以下假设：


H2e. Reviewer's competence in writing useful reviews is positively associated with the perceived reviewer trustworthiness.




H2e。审稿人撰写有用审稿的能力与审稿人的可信度呈正相关。


Sociability is one of the critical dimensions of source credibility according to McCroskey. One of the key values of sociability is friendliness.




麦克罗斯基认为，社交性是消息来源可信度的关键维度之一。社交的关键价值观之一是友善。


In the context of social networks, friendliness can be quantified using the number of friends a person is connected to in the community. So this will imply that number of friends a reviewer has in the community will be positively associated with the credibility of the reviewer. Liu and Park [33] have used the number of friends as one of the variables and tested its effect on usefulness of reviews. So the following hypothesis is proposed:




在社交网络的背景下，友好度可以通过一个人在社区中连接的朋友数量来量化。因此，这意味着评论者在社区中拥有的朋友数量将与评论者的可信度正相关。 Liu 和 Park [33] 使用朋友数量作为变量之一，并测试了其对评论有用性的影响。因此提出以下假设：


H2f. Reviewer's sociability as perceived by other users of a review website is positively associated with the perceived reviewer trustworthiness.




H2f。评论网站的其他用户所感知的评论者的社交性与感知到的评论者的可信度呈正相关。


A visual representation of the proposed model with all the hypotheses is presented in Fig. 1. Operationalization of constructs used in the hypotheses is provided in Table 2. Review length, commonly known to significantly influence the helpfulness of reviews [11], is being used as a control variable to isolate the influence of reviewer characteristics from review characteristics upon reviewer trustworthiness. Similarly, business category and location as business characteristics are introduced as control variables examining their possible impact on business patronages.




图 1 给出了包含所有假设的所提出模型的可视化表示。表 2 提供了假设中使用的结构的操作化。众所周知，评论长度会显着影响评论的有用性 [11]，它被用作控制变量，以隔离评论者特征与评论特征对评论者可信度的影响。同样，引入业务类别和位置作为业务特征作为控制变量，检查它们对业务光顾可能产生的影响。


A possible concern regarding the operationalization of constructs could be on the use of number of followers to measure reviewer trustworthiness. While ‘trust’ might be a major factor in causing an online user to follow other members in a community, other factors like social exchange and profile attractiveness can also play a significant role. However, Yelp provides a special context in which the number of followers can be justified to be a good proxy for measuring reviewer trustworthiness. In Yelp, the identities of followers are not revealed to the reviewers, hence restricting the mutual exchange factor. Also, Yelp provides options to ‘friend’ each other to connect on a social basis, and ‘compliment’ others, to praise reviewers for their pictures, posts, etc.




关于结构的操作化的一个可能的担忧可能是使用关注者数量来衡量审阅者的可信度。虽然“信任”可能是导致在线用户关注社区中其他成员的主要因素，但社交交换和个人资料吸引力等其他因素也可以发挥重要作用。然而，Yelp 提供了一个特殊的环境，其中关注者的数量可以作为衡量评论者可信度的良好指标。在 Yelp 中，关注者的身份不会向评论者透露，因此限制了相互交流的因素。此外，Yelp 还提供了在社交基础上相互“加好友”、“赞美”他人、赞扬评论者的图片、帖子等的选项。


Table 2  
Constructs and measuring variables.




表2  
构造和测量变量。


<table><tr><td>Constructs</td><td>Measuring variables</td></tr><tr><td>Business patronages</td><td>Total number of check-ins</td></tr><tr><td>Review-based online reputation of business</td><td>Average business rating * Number of reviews</td></tr><tr><td>Trustworthiness of reviewer</td><td>Number of followers</td></tr><tr><td>Positivity</td><td>Average review rating</td></tr><tr><td>Involvement</td><td>Number of reviews written</td></tr><tr><td>Experience</td><td>Number of years in Yelp</td></tr><tr><td>Reputation</td><td>Number of years as ‘Elite’ reviewer</td></tr><tr><td>Competence</td><td>Average number of review helpfulness votes received per review</td></tr><tr><td>Sociability</td><td>Number of friends</td></tr></table>




<table><tr><td>构造</td><td>测量变量</td></tr><tr><td>企业惠顾</td><td>签到总数</td></tr><tr><td>基于评论的企业在线声誉</td><td>平均企业评级 * 评论数量</td></tr><tr><td>企业的可信度评论者</td><td>关注者数量</td></tr><tr><td>积极性</td><td>平均评论评分</td></tr><tr><td>参与度</td><td>撰写的评论数量</td></tr><tr><td>经验</td><td>工作年数Yelp</td></tr><tr><td>声誉</td><td>作为“精英”评论者的年数</td></tr><tr><td>能力</td><td>每次评论获得的平均评论有用性票数</td></tr><tr><td>社交性</td><td>朋友数量</td></tr></table>


These limit the profile attractiveness factor for following a reviewer. Given the fact that Yelp is primarily a utility-based community where members would like to get really credible reviews, following someone's reviews anonymously would mostly be an indication of trust on the reviewer and his/her opinions. Thus, we use followership in Yelp as an approximate measure of reviewer trustworthiness.




这些限制了关注评论者的个人资料吸引力因素。鉴于 Yelp 主要是一个基于实用程序的社区，成员希望获得真正可信的评论，匿名关注某人的评论主要表明对评论者及其意见的信任。因此，我们使用 Yelp 中的关注度作为评论者可信度的近似衡量标准。


## 4. Data




## 4. 数据


A large dataset was collected from Yelp.com which has been made public as a part of the Yelp Dataset Challenge. The dataset had 2.2 million reviews of 77,000 local businesses in several cities from countries like Germany, UK, USA, and Canada. Data of about 525,000 users who visited the businesses and reviewed them were also available. The analysis required business level data to test hypotheses H1a and H1b. We used business level attributes, total check-ins, average rating, and number of reviews in our analysis. We also computed average number of followers of the reviewers of each business by combining business data and user data. Average number of followers of the reviewers of businesses was used as a measure of reviewer trustworthiness. Table 3 shows the descriptive statistics of the variables used. Initially we considered 77,445 observations for business level analysis. After cleaning the data by removing the outliers and missing values, we ended up with 53,902 records for our first level of analysis.




从 Yelp.com 收集了一个大型数据集，该数据集已作为 Yelp 数据集挑战赛的一部分公开。该数据集包含来自德国、英国、美国和加拿大等国家多个城市的 77,000 家当地企业的 220 万条评论。还提供了约 525,000 名访问过这些企业并对其进行评论的用户的数据。该分析需要业务级数据来检验假设 H1a 和 H1b。我们在分析中使用了业务级别属性、签到总数、平均评分和评论数量。我们还结合业务数据和用户数据计算了每个业务的评论者的平均关注者数量。企业评论者的平均关注者数量被用作评论者可信度的衡量标准。表 3 显示了所用变量的描述性统计。最初，我们考虑了 77,445 个观察值进行业务级别分析。通过删除异常值和缺失值来清理数据后，我们最终获得了 53,902 条记录用于第一级分析。


![](/api/attachments/UHPKF9MA/fulltext/images/3af1b369418f5b9f4ea7d2f577b68dbce763da398789066c49664f0b56abd4b8.jpg)  
Fig. 1. Theoretical model on reviewer trustworthiness




![](/api/attachments/UHPKF9MA/fulltext/images/3af1b369418f5b9f4ea7d2f577b68dbce763da398789066c49664f0b56abd4b8.jpg)  
图 1 审稿人可信度理论模型


Table 3  
Descriptive statistics of the variables used for testing hypotheses H1a–H1b.




表3  
用于检验假设 H1a-H1b 的变量的描述性统计。


<table><tr><td>Variable</td><td>Range</td><td>Mean</td><td>SD</td></tr><tr><td>Average number of followers</td><td>0–68</td><td>7.39</td><td>9.58</td></tr><tr><td>Average business rating * Number of reviews</td><td>3–1252</td><td>114.06</td><td>173.81</td></tr><tr><td>Total number of check-ins</td><td>3–1860</td><td>101.74</td><td>191.89</td></tr></table>




<table><tr><td>变量</td><td>范围</td><td>平均值</td><td>SD</td></tr><tr><td>平均关注者数量</td><td>0–68</td><td>7.39</td><td>9.58</td></tr><tr><td>平均业务评分 * 评论数量</td><td>3–1252</td><td>114.06</td><td>173.81</td></tr><tr><td>总数量签到</td><td>3–1860</td><td>101.74</td><td>191.89</td></tr></table>


To test the second part of our analysis, i.e., hypotheses H2a through H2f a user dataset with 552,339 initial observations was used. User attributes such as number of followers, number of friends, average review rating, number of reviews written, total votes per user, years of experience, and years of reputation were used for the analysis. Average length of reviews written by users was used as a control variable. After preprocessing the data set, i.e., removal of outliers and missing records, we ended up with 69,612 records. Table 4 shows the descriptive statistics of the sample data.




为了测试我们分析的第二部分，即假设 H2a 到 H2f，使用了包含 552,339 个初始观察值的用户数据集。分析中使用了用户属性，例如关注者数量、朋友数量、平均评论评分、撰写的评论数量、每个用户的总投票数、经验年数和声誉年数。用户撰写的评论的平均长度被用作控制变量。对数据集进行预处理（即删除异常值和缺失记录）后，我们最终得到 69,612 条记录。表4为样本数据的描述性统计。


## 5. Analysis and results




## 5. 分析与结果


In the first part of our analysis we tested the moderating effect of reviewer trustworthiness on the effect of online reputation of a business on its patronages. We used average number of followers of the reviewers who reviewed a business as a proxy of reviewer trustworthiness and total number of check-ins for a business as a proxy for patronages. To measure online reputation of a business we calculated the product of average business rating and the number of reviews a business (average business rating ∗ number of reviews) received over the years. We introduced an interaction variable, product of average number of followers and (average business rating ∗ number of reviews) to take into account the moderation effect [49]. We used a log transformation of the variables to adjust for skewness [50]. We also controlled for the effect of business category and location (city) by including dummy variables representing category and city in our model. The dummy variable City Code takes binary values 0 for Las Vegas and 1 for Phoenix. We considered Las Vegas and Phoenix in our analysis as these two cities appeared in the data set the most number of times. Also, the cities were located in different states of the US. The purpose was to check whether location of the business had any impact on its patronages. Two different business categories, ‘Restaurants’ and ‘Beauty and Spas’ were represented by the dummy variable Category Code. ‘Restaurants’ and ‘Beauty and Spas’ were the highest and the second highest most frequently appearing business categories in the data set. Also the type of these two businesses was significantly different and this helped us observe whether business category had any impact on patronages. After including the control variables in the analysis the data size became 7700. We also checked the correlation between the independent variables and found no significant multicollinearity among the variables [51].




在我们分析的第一部分中，我们测试了评论者可信度对企业在线声誉对其惠顾的影响的调节作用。我们使用评论企业的评论者的平均关注者数量作为评论者可信度的代表，并使用企业的签到总数作为惠顾的代表。为了衡量企业的在线声誉，我们计算了企业多年来收到的平均企业评级和评论数量的乘积（平均企业评级 * 评论数量）。我们引入了一个交互变量，即平均关注者数量和（平均商业评级*评论数量）的乘积，以考虑调节效应[49]。我们使用变量的对数变换来调整偏度[50]。我们还通过在模型中包含代表类别和城市的虚拟变量来控制业务类别和位置（城市）的影响。虚拟变量城市代码对于拉斯维加斯采用二进制值 0，对于凤凰城采用二进制值 1。我们在分析中考虑了拉斯维加斯和凤凰城，因为这两个城市在数据集中出现的次数最多。此外，这些城市位于美国的不同州。目的是检查企业的位置是否对其顾客产生影响。虚拟变量类别代码代表两个不同的业务类别“餐厅”和“美容与水疗中心”。 “餐厅”和“美容与水疗中心”是数据集中出现频率最高和第二高的业务类别。此外，这两种业务的类型也有显着不同，这有助于我们观察业务类别是否对光顾量产生影响。将控制变量纳入分析后，数据量变为7700。我们还检查了自变量之间的相关性，发现变量之间不存在显着的多重共线性[51]。


Descriptive statistics of the variables used for testing hypotheses H2a–H2f.




用于检验假设 H2a–H2f 的变量的描述性统计。


<table><tr><td>Variable</td><td>Range</td><td>Mean</td><td>SD</td></tr><tr><td>Number of followers</td><td>1–23</td><td>2.042</td><td>1.934</td></tr><tr><td>Average review rating per user</td><td>1–5</td><td>3.816</td><td>0.587</td></tr><tr><td>Number of reviews written</td><td>3–284</td><td>45.026</td><td>46.541</td></tr><tr><td>Years of experience</td><td>1–12</td><td>5.214</td><td>2.084</td></tr><tr><td>Years of reputation</td><td>0–3</td><td>0.133</td><td>0.435</td></tr><tr><td>Average review votes per user</td><td>0–8.5</td><td>2.085</td><td>1.414</td></tr><tr><td>Number of friends</td><td>1–49</td><td>7.186</td><td>9.361</td></tr><tr><td>Average review length</td><td>1–58</td><td>23.114</td><td>13.130</td></tr></table>




<table><tr><td>变量</td><td>范围</td><td>均值</td><td>SD</td></tr><tr><td>关注者数量</td><td>1–23</td><td>2.042</td><td>1.934</td></tr><tr><td>平均评价评分每个用户</td><td>1–5</td><td>3.816</td><td>0.587</td></tr><tr><td>撰写的评论数量</td><td>3–284</td><td>45.026</td><td>46.541</td></tr><tr><td>年数经验</td><td>1–12</td><td>5.214</td><td>2.084</td></tr><tr><td>声誉年数</td><td>0–3</td><td>0.133</td><td>0.435</td></tr><tr><td>平均评论票数用户</td><td>0–8.5</td><td>2.085</td><td>1.414</td></tr><tr><td>好友数量</td><td>1–49</td><td>7.186</td><td>9.361</td></tr><tr><td>平均评论长度</td><td>1–58</td><td>23.114</td><td>13.130</td></tr></table>


Hypotheses H1a and H1b were tested using the first model. We used the following linear regression equations for the analysis.




使用第一个模型测试假设 H1a 和 H1b。我们使用以下线性回归方程进行分析。


Model 1:




型号1：


Log of total checkins  β β Category code  β City code  ∈




总签到日志 β β 类别代码 β 城市代码 ε


Model 2:




型号2：


Log of total checkins $= \beta _ { 0 } + \beta _ { 1 }$ Category code β City code β Log of




总签到日志 $= \beta _ { 0 } + \beta _ { 1 }$ 类别代码 β 城市代码 β 的日志


Average business rating  Number of reviews ∈




平均商业评级 评论数 ε


Model 3:




型号3：


Log of total checkins




总签到日志


<sub>¼</sub> β<sub>0 þ</sub> β<sub>1</sub> Category code $+ \beta _ { 2 }$ City code




<sub>¼</sub> β<sub>0 þ</sub> β<sub>1</sub> 类别代码 $+ \beta _ { 2 }$ 城市代码


β Log of Average number of followers




β 平均关注者数量的对数


1 ${ \mathrm { - } } \beta _ { 4 }$ Log of Average business rating Number of reviews




1 ${ \mathrm { - } } \beta _ { 4 }$ 平均企业评级的对数 评论数量


$+ \beta _ { 5 }$ Log of Average number of followers




$+ \beta _ { 5 }$ 平均关注者数量的对数


Average business rating Number of reviews ∈




平均商业评级 评论数 ε


Model 1 incorporated only the control variables to account for the variation in our sample in terms of city and business category. Model 2 tested the main effect of online reputation on business patronages. Model 3 tested the moderating effect by introducing the interaction variable i.e., product of average number of followers and (average business rating ∗ number of reviews) [49]. Table 5 summarizes the results of the hypotheses testing for Models 1, 2 and 3.




模型 1 仅纳入控制变量来解释样本在城市和商业类别方面的变化。模型2检验了在线声誉对商业惠顾的主效应。模型3通过引入交互变量，即平均关注者数量与（平均商业评级*评论数量）的乘积来测试调节效果[49]。表 5 总结了模型 1、2 和 3 的假设检验结果。


The result supported hypothesis H1a where the relationship of review-based online reputation and patronages of business was found to be positive and significant. We observed a significant increase in the value of $R ^ { 2 }$ from Model 1 to Model 2 and Model 3. The coefficient of the interaction term was also positive and significant and thus supported hypothesis H1b. We obtained similar results using the cities Las Vegas and Edinburgh that were from different countries.




结果支持假设 H1a，其中基于评论的在线声誉和企业赞助之间的关系被发现是积极且显着的。我们观察到从模型 1 到模型 2 和模型 3，$R^{2}$ 的值显着增加。交互项的系数也是正且显着的，因此支持假设 H1b。我们使用来自不同国家的城市拉斯维加斯和爱丁堡获得了类似的结果。


In the second part of our analysis we attempted to identify the reviewer characteristics which impacted reviewer trustworthiness. Number of followers of a reviewer was used as a measure of trustworthiness of that reviewer. The descriptive statistics of the data is provided in Table 4. It was observed that the standard deviation of the variables was smaller than their mean.




在分析的第二部分中，我们试图确定影响审稿人可信度的审稿人特征。审阅者的关注者数量被用作该审阅者可信度的衡量标准。表4提供了数据的描述性统计。可以看出，变量的标准差小于其平均值。


We also checked the distribution of the variables. All variables except Number of followers, Number of reviews and Number of friends were found to be normally distributed. These three variables (Number of followers, Number of reviews and Number of friends) had shown skewness to the right. To adjust for the non-conformance to normality we used log-transformation of these variables for our analysis [50]. Next we checked the correlation matrix to identify multicollinearity, if any, among the independent variables [51]. The correlation of the variables ranged from −1.52 to +0.348 and was not found to be significant enough to cause issues with regression analysis. However, to reassure that there was no evidence of multicollinearity, we checked the VIF [52] of the independent variables and found it to be below 10.




我们还检查了变量的分布。除关注者数量、评论数量和朋友数量外，所有变量均呈正态分布。这三个变量（关注者数量、评论数量和朋友数量）呈现出向右偏态。为了调整不符合正态性的情况，我们使用这些变量的对数转换进行分析[50]。接下来，我们检查相关矩阵以确定自变量之间的多重共线性（如果有）[51]。变量的相关性范围为 -1.52 至 +0.348，并且未发现显着性足以导致回归分析出现问题。然而，为了确保不存在多重共线性的证据，我们检查了自变量的 VIF [52]，发现它低于 10。


To analyse hypotheses H2a through H2f we used the following linear regression equations:




为了分析假设 H2a 到 H2f，我们使用了以下线性回归方程：


Model 4




型号4


Log of number of followers $= \beta _ { 0 } + \beta _ { 1 }$ Average review length $+ \in$




关注者数量的对数 $= \beta _ { 0 } + \beta _ { 1 }$ 平均评论长度 $+ \in$


Results of hypotheses testing (H1a–H1b).




假设检验的结果（H1a-H1b）。


<table><tr><td>Dependent variable: Log of total number of check-ins</td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>Category code</td><td>1.391***</td><td>0.701***</td><td>0.553***</td></tr><tr><td>City code</td><td>0.389***</td><td>0.138***</td><td>0.085***</td></tr><tr><td>Log of Review based online reputation</td><td></td><td>0.899***</td><td>0.831***</td></tr><tr><td>Log of Reviewer trustworthiness</td><td></td><td></td><td>-0.027</td></tr><tr><td>Interaction effect: Log of Reviewer trustworthiness * Log of Review based online reputation</td><td></td><td></td><td>0.041***</td></tr><tr><td> $R^2$ </td><td>0.104</td><td>0.688</td><td>0.763</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.104</td><td>0.688</td><td>0.763</td></tr><tr><td>Hypothesis</td><td></td><td>H1a</td><td>H1b</td></tr><tr><td>Hypothesized relationship</td><td></td><td>Review-based online reputation → Patronages</td><td>Review-based Online reputation * Reviewer trustworthiness → Patronages</td></tr><tr><td>Results</td><td></td><td>Supported</td><td>Supported</td></tr></table>




<table><tr><td>因变量：签到总数的日志</td><td>模型1</td><td>模型2</td><td>模型3</td></tr><tr><td>类别代码</td><td>1.391***</td><td>0.701***</td><td>0.553***</td></tr><tr><td>城市代码</td><td>0.389***</td><td>0.138***</td><td>0.085***</td></tr><tr><td>日志基于评论的在线声誉</td><td></td><td>0.899***</td><td>0.831***</td></tr><tr><td>评论者可信度日志</td><td></td><td></td><td>-0.027</td></tr><tr><td>交互效果：评论者可信度日志 * Log基于评论的在线声誉</td><td></td><td></td><td>0.041***</td></tr><tr><td> $R^2$ </td><td>0.104</td><td>0.688</td><td>0.763</td></tr><tr><td>调整后的$R^2$ </td><td>0.104</td><td>0.688</td><td>0.763</td></tr><tr><td>假设</td><td></td><td>H1a</td><td>H1b</td></tr><tr><td>假设关系</td><td></td><td>基于评论的在线声誉→订阅者</td><td>基于评论的在线声誉*评论者可信度→订阅者</td></tr><tr><td>结果</td><td></td><td>支持</td><td>支持</td></tr></table>


⁎⁎⁎ Significant at the 0.001 level of significance.




⁎⁎⁎ 在 0.001 显着性水平上显着。


## Model 5




## 模型 5


Log of number of followers $\mathrm { \beta _ { 0 } + \beta _ { 1 } }$ Average review length




关注者数量的对数 $\mathrm { \beta _ { 0 } + \beta _ { 1 } }$ 平均评论长度


十 ${ \bf \nabla } \cdot \beta _ { 2 }$ Average review rating




十 ${ \bf \nabla } \cdot \beta _ { 2 }$ 平均评论评级


\+ $\beta _ { 3 }$ Log of number of reviews written




\+ $\beta _ { 3 }$ 撰写评论数量的日志


$\beta _ { 4 }$ Years of experience




$\beta _ { 4 }$ 年经验


$\beta _ { 5 }$ Years of reputation




$\beta _ { 5 }$ 年声誉


\+ $\mathrm { . \textmu \textmu \textmu \textmu } _ { \mathrm { 8 6 } }$ Average review vote per user




\+ $\mathrm { . \textmu \textmu \textmu \textmu } _ { \mathrm { 8 6 } }$ 每个用户的平均评论投票


$+ \beta _ { 7 }$ Log of number of friends ∈




$+ \beta _ { 7 }$ 好友数量对数 ε


We used linear regression after checking for the underlying assumptions. We checked the scatter plots of the dependent variable with respect to all the independent variables to identify the patterns that had appeared to be linear in nature. We considered the average length of review for each user as a control variable in order to confirm that trustworthiness of a reviewer significantly depended on the reviewer characteristics, and was not biased by the length of the review that a reviewer wrote. Model 4 in this part of analysis took into account the control variables. Model 5 studied the main effect of the independent variables. We ran a robust regression model. Robust regression was used instead of the OLS regression to take care of heteroscedasticity, and error due to outliers and highly leveraged data points [53]. The model was found to be significant at the 0.001 level of significance. All the hypotheses were supported in our analysis. Tables 6 and 7 summarize the results obtained from hypotheses testing for Models 4 and 5. The linear regression model resulted in an adjusted $R ^ { 2 }$ value of 0.366, which conformed with the goodness of fit of the robust regression model. Fig. 2 shows the proposed model with final results.




在检查了基本假设后，我们使用了线性回归。我们检查了因变量相对于所有自变量的散点图，以识别本质上看似线性的模式。我们将每个用户的评论平均长度视为控制变量，以确认评论者的可信度在很大程度上取决于评论者的特征，并且不会因评论者撰写的评论长度而产生偏差。这部分分析中的模型4考虑了控制变量。模型5研究了自变量的主效应。我们运行了一个稳健的回归模型。使用稳健回归代替 OLS 回归来处理异方差性以及异常值和高杠杆数据点引起的误差 [53]。发现该模型在 0.001 显着性水平上显着。所有的假设都在我们的分析中得到了支持。表 6 和表 7 总结了模型 4 和 5 的假设检验所获得的结果。线性回归模型得出的调整后的 $R^{2}$ 值为 0.366，这与稳健回归模型的拟合优度相符。图 2 显示了所提出的模型的最终结果。


The data size of the analysis being large (69,612 records) we had to re-confirm that the results of the regression analysis were due to correctness of the model, and not due to Type I error. To ensure that, we carried out the analysis using smaller sub-samples of the initial data set. We randomly selected around 50% of the data (30,000 records) and 25% of the data (15,000 records) and ran the regression analysis for both sub-samples. We found all hypotheses to be supported. Hypothesis H2c was supported at the 0.05 level of significance. All other hypotheses were found to be significant at the 0.001 level of significance.




由于分析的数据量很大（69,612 条记录），我们必须重新确认回归分析的结果是由于模型的正确性，而不是由于 I 类错误。为了确保这一点，我们使用初始数据集的较小子样本进行了分析。我们随机选择了大约 50% 的数据（30,000 条记录）和 25% 的数据（15,000 条记录），并对两个子样本进行回归分析。我们发现所有假设都得到支持。假设 H2c 在 0.05 显着性水平上得到支持。所有其他假设均在 0.001 显着性水平上显着。


Results of robust regression analysis (H2a–H2f).




稳健回归分析的结果（H2a–H2f）。


<table><tr><td>Dependent variable: Log of number of followers</td><td>Model 4</td><td>Model 5</td></tr><tr><td>Average review length</td><td>-0.001***</td><td>0.001***</td></tr><tr><td>Average review rating per user</td><td></td><td>0.051***</td></tr><tr><td>Log of number of reviews written</td><td></td><td>0.228***</td></tr><tr><td>Years of experience</td><td></td><td>0.004***</td></tr><tr><td>Years of reputation</td><td></td><td>0.183***</td></tr><tr><td>Average review votes per user</td><td></td><td>0.084***</td></tr><tr><td>Log of number of friends</td><td></td><td>0.120***</td></tr><tr><td> $R^2$ </td><td>0.001</td><td>0.366</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.001</td><td>0.366</td></tr></table>




<table><tr><td>因变量：关注者数量的对数</td><td>模型 4</td><td>模型 5</td></tr><tr><td>平均评论长度</td><td>-0.001***</td><td>0.001***</td></tr><tr><td>平均评论评分用户</td><td></td><td>0.051***</td></tr><tr><td>撰写评论数量的日志</td><td></td><td>0.228***</td></tr><tr><td>年数经验</td><td></td><td>0.004***</td></tr><tr><td>声誉年数</td><td></td><td>0.183***</td></tr><tr><td>平均评论票数用户</td><td></td><td>0.084***</td></tr><tr><td>好友数量记录</td><td></td><td>0.120***</td></tr><tr><td> $R^2$ </td><td>0.001</td><td>0.366</td></tr><tr><td>调整$R^2$</td><td>0.001</td><td>0.366</td></tr></table>


\*\*\* Significant at the 0.001 level of significance.




\*\*\* 在 0.001 显着性水平上显着。


Finally to test the predictive capacity of our model, we predicted the trustworthiness of a reviewer based on his/her characteristics. We divided the user dataset into two subsets: high and low trustworthiness of users depending on the mean value of number of followers. The reviewers with followers more than the average number of followers were labeled as high trustworthy reviewers and users having followers less than the average number of followers were labeled as low trustworthy reviewers. For the purpose of classification, a robust logistic regression model was built using the significant factors identified in the proposed research model. Monte Carlo cross-validation was used to repeatedly (5 times) train and test the model by splitting the data each time into random sub-samples in a proportion of 80–20. Use of the robust logistic regression took care of heteroscedastic errors and presence of outliers in the data. We calculated the average of the accuracies for the 5 data samples that were created and found that the predictive model successfully classified 82.85% of the reviewers as high or low on trustworthiness based on the underlying factors. Table 8 shows the performance measure of the predictive Model I. We obtained similar results by using other machine learning techniques like neural network and C5.0 decision tree with overall accuracy of 83.59% and 83.1% respectively.




最后，为了测试我们模型的预测能力，我们根据评论者的特征预测了他/她的可信度。我们将用户数据集分为两个子集：根据关注者数量的平均值，用户的高可信度和低可信度。关注者数量超过平均关注者数量的评论者被标记为高可信评论者，关注者少于平均关注者数量的用户被标记为低可信评论者。为了分类的目的，使用所提出的研究模型中确定的重要因素建立了稳健的逻辑回归模型。使用蒙特卡罗交叉验证重复（5次）训练和测试模型，每次将数据按80-20的比例分成随机子样本。使用稳健的逻辑回归可以解决异方差误差和数据中异常值的存在。我们计算了创建的 5 个数据样本的平均准确度，发现预测模型根据潜在因素成功地将 82.85% 的审阅者分类为可信度高或低。表 8 显示了预测模型 I 的性能指标。我们通过使用神经网络和 C5.0 决策树等其他机器学习技术获得了类似的结果，总体准确率分别为 83.59% 和 83.1%。


The Model I showed a high degree of specificity indicating that it had correctly classified more than 95% of less trustworthy reviewers. If a business aimed to target high trustworthy reviewers to write a review of that business it incurred some cost in terms of promotional expenses. Correctly classifying reviewers who had less followers had the potential to save businesses from making redundant expenses. Since the sensitivity of the model was 41.1% there was some probability of misclassifying high trustworthy reviewers. However, the overall predictability of the model was fund to be reasonably high (82.85%).




模型 I 显示出高度的特异性，表明它已正确分类了 95% 以上的不太值得信赖的审稿人。如果一家企业的目标是吸引高可信度的评论者来撰写该企业的评论，那么它就会产生一些促销费用。对关注者较少的评论者进行正确分类有可能使企业避免不必要的开支。由于该模型的敏感性为 41.1%，因此存在对高可信度审稿人进行错误分类的可能性。然而，该模型的总体预测能力相当高（82.85%）。


The sensitivity of the model was 41.1% which meant that more than 50% of actually high trustworthy reviewers would be incorrectly classified as low trustworthy. For businesses that wanted to identify as many trustworthy reviewers as possible to incentivize or encourage them to review their services, the required model should have a high value of sensitivity. We developed a cost-sensitive classification technique to address the issue, where we assigned higher penalty or cost for falsely classifying high trustworthy as low trustworthy reviewers. Model II in Table 8 showed that the performance measure of the classifier with differential mis-classification cost (Cost of false negative classification = 5 × Cost of false positive classification). The model had a sensitivity of 89.87%, which meant that the revised model was able to correctly identify more than 89% of high trustworthy reviewers.




该模型的敏感性为 41.1%，这意味着超过 50% 的实际高可信度审稿人会被错误地归类为低可信度。对于想要识别尽可能多的值得信赖的审核者以激励或鼓励他们审核其服务的企业来说，所需的模型应该具有较高的敏感性。我们开发了一种成本敏感的分类技术来解决这个问题，我们对将高可信度错误地分类为低可信度审稿人给予更高的惩罚或成本。表 8 中的模型 II 显示了具有差异误分类成本的分类器的性能度量（假阴性分类成本 = 5 × 假阳性分类成本）。该模型的灵敏度为89.87%，这意味着修正后的模型能够正确识别出超过89%的高可信审稿人。


Further, to check the robustness of the predictive model, we performed a cost-sensitive classification to predict top-10% trustworthy reviewers. The model displayed an overall accuracy of 83% and a sensitivity of 85.8%. Observations for Model III in Table 8 showed the performance measures for classifying top 10% reviewers.




此外，为了检查预测模型的稳健性，我们执行了成本敏感分类来预测前 10% 值得信赖的审稿人。该模型的总体准确度为 83%，灵敏度为 85.8%。表 8 中模型 III 的观察结果显示了对前 10% 审稿人进行分类的绩效衡量标准。


Table 7  
Results for hypotheses testing (H2a–H2f).




表7  
假设检验的结果 (H2a–H2f)。


<table><tr><td>Hypothesis</td><td>Hypothesized relationships</td><td>Coefficients</td><td>Results</td></tr><tr><td>H2a</td><td>Reviewer positivity → Reviewer trustworthiness</td><td>0.051***</td><td>All hypotheses are supported</td></tr><tr><td>H2b</td><td>Reviewer Involvement → Reviewer trustworthiness</td><td>0.228***</td><td></td></tr><tr><td>H2c</td><td>Reviewer experience → Reviewer trustworthiness</td><td>0.004***</td><td></td></tr><tr><td>H2d</td><td>Reviewer reputation → Reviewer trustworthiness</td><td>0.183***</td><td></td></tr><tr><td>H2e</td><td>Reviewer competence → &gt; Reviewer trustworthiness</td><td>0.084***</td><td></td></tr><tr><td>H2f</td><td>Reviewer sociability → Reviewer trustworthiness</td><td>0.120***</td><td></td></tr></table>




<table><tr><td>假设</td><td>假设关系</td><td>系数</td><td>结果</td></tr><tr><td>H2a</td><td>审稿人积极性→审稿人可信度</td><td>0.051***</td><td>所有假设均为支持</td></tr><tr><td>H2b</td><td>审稿人参与度→审稿人可信度</td><td>0.228***</td><td></td></tr><tr><td>H2c</td><td>审稿人经验→审稿人可信度</td><td>0.004***</td><td></td></tr><tr><td>H2d</td><td>审稿人声誉→审稿人可信度</td><td>0.183***</td><td></td></tr><tr><td>H2e</td><td>审稿人能力→>审稿人可信度</td><td>0.084***</td><td></td></tr><tr><td>H2f</td><td>审稿人社交性→审稿人可信度</td><td>0.120***</td><td></td></tr></table>


⁎⁎⁎ Significant at the 0.001 level of significance.




⁎⁎⁎ 在 0.001 显着性水平上显着。


## 6. Discussion and implications




## 6. 讨论和影响


## 6.1. Theoretical implications




## 6.1.理论意义


This paper makes several significant theoretical contributions. First, it establishes a direct positive influence of review-based online reputation of a business on its patronages, which should consequently affect sales. Earlier studies have either used the average ratings [5] or volume of ratings [6] received to find its impact on sales. However, we have created a new construct of review-based online reputation using product of average ratings and the total number of ratings. This we believe is a better measure since it takes into account the distortions created by businesses which have very few ratings. Also, most of the earlier studies have focused on online product sales, whereas we have focused on number of footfalls a local business has received.




本文做出了几项重要的理论贡献。首先，它建立了基于评论的企业在线声誉对其惠顾的直接积极影响，从而影响销售。早期的研究要么使用平均收视率 [5] 要么使用收到的收视率 [6] 来确定其对销售的影响。然而，我们使用平均评分和评分总数的乘积创建了一个基于评论的在线声誉的新结构。我们认为这是一个更好的衡量标准，因为它考虑到了评级很少的企业造成的扭曲。此外，大多数早期研究都关注在线产品销售，而我们关注的是本地企业收到的客流量。


Second, while some research works have proposed few reviewer characteristics (quality and exposure [27], elite certification [8], top ranked [9]) that can directly influence sales, this paper added a missing link to the models by introducing the perceived trustworthiness of reviewers based on their characteristics. We established reviewer trustworthiness as a significant factor in moderating the positive influence of review-based online reputation on patronages. This is a unique relationship which has not been verified before in eWOM research to the best of our knowledge.




其次，虽然一些研究工作提出了一些可以直接影响销售的评论者特征（质量和曝光度[27]、精英认证[8]、顶级排名[9]），但本文通过引入基于评论者特征的感知可信度，为模型添加了一个缺失的环节。我们将评论者的可信度确定为调节基于评论的在线声誉对惠顾的积极影响的重要因素。据我们所知，这是一种独特的关系，之前在电子口碑研究中尚未得到验证。


Third, we introduced number of followers a reviewer had as a proxy to measure reviewer trustworthiness. While this has been done in the social network literature, it has hardly been used in eWOM literature except in some cases as a reputation cue [18]. This may be because most of the online review websites do not provide any functionality to anonymously follow a trusted reviewer for getting updates on his/her review posts. In fact, reviewer trustworthiness has been mostly treated as an implicit rather than an explicit factor in online review research.




第三，我们引入了评论者的关注者数量作为衡量评论者可信度的代理。虽然社交网络文献中已经这样做了，但除了在某些情况下作为声誉提示外，它几乎没有在电子口碑文献中使用[18]。这可能是因为大多数在线评论网站不提供任何功能来匿名关注受信任的评论者以获取他/她的评论帖子的更新。事实上，在线评论研究中，评论者的可信度大多被视为隐性因素，而不是显性因素。


Fourth, past research has mostly focused on identifying one or two reviewer characteristics that can affect review helpfulness like expertise and reputation [32], number of reviews and total helpful votes [33], expertise and writing style [34], engagement [30], historical rating distribution [31], etc. For the first time, to the best of our knowledge, a number of them have been used in an integrated manner to build a model of reviewer trustworthiness. All proposed characteristics (positivity, involvement, experience, reputation, competence, sociability) have been found to be significant, and can be reused by future researchers in extending not just eWOM literature, but also research on online communities.




第四，过去的研究主要集中在识别一个或两个可能影响审稿有用性的审稿人特征，如专业知识和声誉[32]、审稿数量和总有用票数[33]、专业知识和写作风格[34]、参与度[30]、历史评分分布[31]等。据我们所知，其中的一些特征第一次被以综合的方式用于构建审稿人可信度模型。所有提出的特征（积极性、参与性、经验、声誉、能力、社交性）都被发现是重要的，并且可以被未来的研究人员重复使用，不仅可以扩展电子口碑文献，还可以扩展在线社区的研究。


![](/api/attachments/UHPKF9MA/fulltext/images/77628ddbab0e7e3e6aeaa9dbfc79f9ab28ab31c208790cd393725d7e4cb357b5.jpg)  
Fig. 2. Results of hypothesized relationships.




![](/api/attachments/UHPKF9MA/fulltext/images/77628ddbab0e7e3e6aeaa9dbfc79f9ab28ab31c208790cd393725d7e4cb357b5.jpg)  
图 2. 假设关系的结果。


Table 8  
Performance measure of the predictive models.




表8  
预测模型的性能衡量。


<table><tr><td>Performance measure</td><td>Model I: Logistic regression</td><td>Model II: Cost-sensitive</td><td>Model III: Top 10% and cost-sensitive</td></tr><tr><td>Sensitivity</td><td>41.15%</td><td>89.87%</td><td>85.79%</td></tr><tr><td>Specificity</td><td>95.10%</td><td>66.23%</td><td>82.64%</td></tr><tr><td>False positive rate for true negative data</td><td>4.90%</td><td>33.77%</td><td>17.35%</td></tr><tr><td>False negative rate for true positive data</td><td>58.85%</td><td>10.13%</td><td>14.21%</td></tr><tr><td>False positive rate for classified positive</td><td>28.83%</td><td>56.07%</td><td>57.02%</td></tr><tr><td>False negative rate for classified negative</td><td>15.39%</td><td>4.23%</td><td>2.55%</td></tr><tr><td>Correctly classified</td><td>82.85%</td><td>71.9%</td><td>83.0%</td></tr></table>




<table><tr><td>绩效衡量</td><td>模型一：逻辑回归</td><td>模型二：成本敏感</td><td>模型三：前10%和成本敏感</td></tr><tr><td>敏感度</td><td>41.15%</td><td>89.87%</td><td>85.79%</td ></tr><tr><td>特异性</td><td>95.10%</td><td>66.23%</td><td>82.64%</td></tr><tr><td>False真阴性数据阳性率</td><td>4.90%</td><td>33.77%</td><td>17.35%</td></tr><tr><td>真阳性假阴性率数据</td><td>58.85%</td><td>10.13%</td><td>14.21%</td></tr><tr><td>分类误报率阳性</td><td>28.83%</td><td>56.07%</td><td>57.02%</td></tr><tr><td>分类误报率负面</td><td>15.39%</td><td>4.23%</td><td>2.55%</td></tr><tr><td>正确分类</td><td>82.85%</td><td>71.9%</td><td>83.0%</td></tr></table>


Note: True positive data refers to high trustworthy reviewers  
True negative data refers to low trustworthy reviewers.




注：真正的阳性数据是指高度可信的审稿人  
真正的负面数据是指低可信度的审稿人。


## 6.2. Managerial implications




## 6.2.管理影响


The findings of this paper have several managerial implications as well. First, since we have found a significant positive influence of online reputation on patronages of local business, the managers can be advised to focus on increasing their number of customer reviews and to try their best to receive positive reviews. Earlier, businesses with online sales channels used to get affected by the reviews on their products, but now even brick-and-mortar businesses get affected due to reviews posted by their customers online.




本文的研究结果也具有一些管理意义。首先，由于我们发现在线声誉对本地企业的光顾具有显着的积极影响，因此可以建议管理者集中精力增加客户评论的数量，并尽力获得积极的评论。早些时候，拥有在线销售渠道的企业常常会受到产品评论的影响，但现在，即使是实体企业也会因为客户在网上发布的评论而受到影响。


Second, because of the positive moderating influence of reviewer trustworthiness on influence of online reputation on patronages, business managers may be advised to encourage top trustworthy reviewers to review their products and services. While increase in patronages is positively associated with good online reviews, it can be further boosted if reviewers have higher level of perceived trustworthiness. So the practice of inviting top online reviewers to visit and review businesses can be more popularized. The lure of getting free invitations can lead to more reviewers becoming active and quality conscious in review sites in order to gain trust of others.




其次，由于评论者的可信度对在线声誉对顾客的影响具有积极的调节作用，因此可以建议业务经理鼓励最值得信赖的评论者评论他们的产品和服务。虽然光顾量的增加与良好的在线评论呈正相关，但如果评论者具有更高的可信度，则光顾量的增加可能会进一步增加。因此，邀请顶级在线评论者来参观和评论企业的做法可以更加普及。获得免费邀请的诱惑可能会导致更多的评论者在评论网站上变得活跃并具有质量意识，以获得他人的信任。


Third, business managers can customize and use the predictive model presented in this paper to identify and rank reviewers based on their potential trustworthiness using reviewer characteristics available in the websites. This can be particularly useful for online review sites where users are not allowed to follow their trusted reviewers, thus eliminating the possibility of using the number of followers as a direct proxy to reviewer trustworthiness.




第三，业务经理可以定制和使用本文提出的预测模型，利用网站上可用的审阅者特征，根据审阅者的潜在可信度来识别审阅者并对其进行排名。这对于不允许用户关注其信任的评论者的在线评论网站特别有用，从而消除了使用关注者数量作为评论者可信度的直接代理的可能性。


Fourth, the predictive model can also be used by the online review websites to rank reviewers and even display their reviews in decreasing order of reviewer trustworthiness. This can be particularly useful in case of new reviews posted with no helpfulness votes received to decide their display order. Also, the significant factors affecting reviewer trustworthiness can be shared with reviewers, so that they can get an easy understanding of steps to take in order to gain more followers.




第四，在线评论网站还可以使用预测模型对评论者进行排名，甚至按照评论者可信度的降序显示他们的评论。如果发布的新评论没有收到决定其显示顺序的帮助投票，这可能特别有用。此外，可以与审稿人分享影响审稿人可信度的重要因素，以便他们可以轻松了解获得更多关注者所需采取的步骤。


## 6.3. Limitations and future research




## 6.3。局限性和未来研究


There are some limitations to this research, which can be overcome in future research. First, we have used data only from one review site Yelp, which only includes local businesses. So it needs to be tested whether the findings are generalizable for other product review websites as well.




这项研究存在一些局限性，可以在未来的研究中克服。首先，我们仅使用来自一个评论网站 Yelp 的数据，该网站仅包含本地企业。因此，需要测试这些发现是否也适用于其他产品评论网站。


Second, we have used check-ins to a business posted by Yelp customers, when they visit the business, as a proxy for business patronages. While it is a good indicator based on actual physical presence of a customer at the business shop, it is still limited compared to the total number of footfalls in the business since most of the customers may not be checkingin their location on Yelp. This is why the mean of total check-ins across all businesses is just 148. Future researchers can try to get sales data of businesses from financial databases and verify this model.




其次，我们使用 Yelp 客户在访问该企业时发布的企业签到信息作为企业惠顾的代理。虽然这是一个基于顾客实际出现在商店的良好指标，但与商店的总客流量相比，它仍然有限，因为大多数顾客可能不会在 Yelp 上查看他们的位置。这就是为什么所有企业的签到总数平均值仅为 148。未来的研究人员可以尝试从财务数据库中获取企业的销售数据并验证该模型。


Third, only a few of the possible control variables have been used in this study. For instance, when controlling for review characteristics, we have used length of review. However, future researchers can take some of the linguistic characteristics of reviews like sentiment, depth, bias, etc. into consideration. Similarly for business characteristics, apart from category and location, other control variables like size, age, etc. of a business can be used as control variables. An important variable that can be controlled in future studies is the online marketing expense of businesses, since that may have a positive influence on the number of check-ins. For instance, Yelp allows businesses to purchase self-service and full-service ads, with the latter having added advantages of removing competitor ads from business page, and have videographers from Yelp help produce professional videos. While it may be difficult to find out the exact advertising expenses of local businesses, the effort of marketing can be reflected by data on the sponsored ads posted by the businesses.




第三，本研究仅使用了少数可能的控制变量。例如，在控制评论特征时，我们使用了评论长度。然而，未来的研究人员可以考虑评论的一些语言特征，如情感、深度、偏见等。同样，对于企业特征而言，除了类别和位置之外，还可以使用企业规模、年龄等其他控制变量作为控制变量。未来研究中可以控制的一个重要变量是企业的在线营销费用，因为这可能对签到数量产生积极影响。例如，Yelp 允许企业购买自助服务和全方位服务广告，后者具有从企业页面删除竞争对手广告的额外优势，并让 Yelp 的摄像师帮助制作专业视频。虽然可能很难找出当地企业的确切广告费用，但营销力度可以通过企业发布的搜索广告的数据反映出来。


Fourth, more reviewer characteristics can be added to improve the predictive accuracy of the model. Some of the well-known trust inducing factors like presence of profile picture, etc. have not been considered. Even the network effect of friends has not been explored in depth. Future research can dig deeper into other reviewer characteristics. Other predictive techniques can also be used to build models either separately or in ensemble (e.g., decision tree combined with neural network) to further boost the accuracy.




第四，可以添加更多的审阅者特征来提高模型的预测准确性。一些众所周知的信任诱导因素（例如个人资料图片的存在等）尚未被考虑。就连朋友的网络效应也没有被深入探讨。未来的研究可以更深入地挖掘其他审稿人的特征。其他预测技术也可以用于单独或集成地构建模型（例如，决策树与神经网络相结合），以进一步提高准确性。


Fifth, only a cross-sectional regression analysis could be performed with the data available to us. Hence, we do not know how business patronages get impacted over time by reviewer trustworthiness, or how reviewer characteristics vary in their influence on trustworthiness over time. Future researchers can use time-stamped data to conduct a panel data regression to uncover interesting results.




第五，只能利用我们现有的数据进行横截面回归分析。因此，我们不知道随着时间的推移，评论者的可信度如何影响商业惠顾，也不知道随着时间的推移，评论者的特征对可信度的影响如何变化。未来的研究人员可以使用带时间戳的数据进行面板数据回归，以发现有趣的结果。


## 7. Conclusion




## 7. 结论


This paper puts focus on trustworthiness of reviewers as an important construct in eWOM literature. We have found reviewer trustworthiness to positively moderate the association between review-based online reputation and patronages of businesses. Furthermore, we have found reviewer trustworthiness to be positively associated with six reviewer characteristics like positivity, involvement, experience, reputation, competence, and sociability. Using these factors, we have developed a predictive model to classify reviewers into two groups based on high and low trustworthiness. This research makes significant theoretical contribution and can be used by businesses to estimate reviewer trustworthiness in order to target top reviewers to review their products or services.




本文重点关注审稿人的可信度，将其作为电子口碑文献中的一个重要结构。我们发现评论者的可信度可以积极调节基于评论的在线声誉与企业惠顾之间的关联。此外，我们发现审稿人的可信度与审稿人的六个特征呈正相关，如积极性、参与度、经验、声誉、能力和社交能力。利用这些因素，我们开发了一个预测模型，根据高可信度和低可信度将审阅者分为两组。这项研究做出了重大的理论贡献，企业可以使用它来评估评论者的可信度，以便瞄准顶级评论者评论他们的产品或服务。


## References




＃＃ 参考


[1] T. Hennig-Thurau, K.P. Gwinner, G. Walsh, D.D. Gremler, Electronic word-of-mouth via consumer-opinion platforms: what motivates consumers to articulate them selves on the Internet? Journal of Interactive Marketing 18 (2004) 38–52.




[1] T. Hennig-Thurau，K.P.格温纳，G.沃尔什，D.D. Gremler，通过消费者意见平台进行的电子口碑：是什么促使消费者在互联网上表达自己的观点？互动营销杂志 18 (2004) 38–52。


[2] F. Zhu, X. Zhang, Impact of online consumer reviews on sales: the moderating role of product and consumer characteristics, Journal of Marketing 74 (2010) 133–148.




[2] F. Zhu，X. Zhang，在线消费者评论对销售的影响：产品和消费者特征的调节作用，营销杂志 74 (2010) 133-148。


[3] X. Li, L. Hitt, Price effects in online product reviews: an analytical model and empirical analysis, MIS Quarterly 34 (2010) 809–831.




[3] X. Li, L. Hitt，在线产品评论中的价格效应：分析模型和实证分析，MIS 季刊 34 (2010) 809–831。


[4] BrightLocal, Local consumer review survey, https://www.brightlocal.com/learn/ local-consumer-review-survey/ 2016




[4] BrightLocal，本地消费者评论调查，https://www.brightlocal.com/learn/local-consumer-review-survey/ 2016


[5] J. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book reviews, Journal of Marketing Research 43 (2006) 345–354




[5] J. Chevalier, D. Mayzlin，口碑对销售的影响：在线书评，营销研究杂志 43 (2006) 345–354


[6] W. Duan, B. Gu, A. Whinston, Do online reviews matter?—an empirical investigation of panel data, Decis. Support. Syst. 45 (2008) 1007–1016.




[6] W. Duan、B. Gu、A. Whinston，在线评论重要吗？——面板数据的实证调查，Decis。支持。系统。 45（2008）1007-1016。


[7] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Information Systems Research 19 (2008) 291–313.




[7] C. Forman、A. Ghose、B. Wiesenfeld，审查评论与销售之间的关系：评论者身份披露在电子市场中的作用，信息系统研究 19 (2008) 291-313。


[8] S. DiGrande, D. Knox, K. Manfred, J. Rose, Unlocking the digital-marketing potential of small businesses, BCG perspectives, https://www.bcgperspectives.com/content/ articles/digital\_economy\_marketing\_sales\_unlocking\_digital\_marketing\_small\_ businesses/ 2013.




[8] S. DiGrande、D. Knox、K. Manfred、J. Rose，释放小型企业的数字营销潜力，BCG 观点，https://www.bcgperspectives.com/content/articles/digital\_economy\_marketing\_sales\_unlocking\_digital\_marketing\_small\_businesss/ 2013。


[9] M. Luca, Reviews, Reputation, and Revenue: The Case of Yelp.com, Harvard Business School NOM Unit Working Paper. 12–016, 2011 1–40.




[9] M. Luca，评论、声誉和收入：Yelp.com 案例，哈佛商学院 NOM 单元工作论文。 12-016，2011 年 1-40。


[10] P. Chen, S. Dhanasobhon, M.D. Smith, All Reviews Are Not Created Equal: The Disaggregate Impact of Reviews and Reviewers at Amazon.com, Heinz College Research, 2008 1–32.




[10] P. Chen、S. Dhanasobhon、M.D. Smith，所有评论并非生来平等：Amazon.com 上评论和评论者的分类影响，亨氏学院研究，2008 年 1-32。


[11] S.M. Mudambi, D. Schuff, What makes a helpful online review? A study of customer reviews on Amazon com MIS Ouarterly 34 (2010) 185–200




[11] S.M. Mudambi，D. Schuff，什么才是有用的在线评论？亚马逊 com MIS Ouarterly 上的客户评论研究 34 (2010) 185–200


[12] R. Schindler, B. Bickart, Perceived helpfulness of online consumer reviews: the role of message content and style, Journal of Consumer Behaviour 11 (2012) 234–243.




[12] R. Schindler、B. Bickart，在线消费者评论的感知有用性：消息内容和风格的作用，消费者行为杂志 11 (2012) 234–243。


[13] N. Korfiatis, E. García-Bariocanal, S. Sánchez-Alonso, Evaluating content quality and helpfulness of online product reviews: the interplay of review helpfulness vs. review content, Electronic Commerce Research and Applications 11 (2012) 205–217.




[13] N. Korfiatis、E. García-Bariocanal、S. Sánchez-Alonso，评估在线产品评论的内容质量和有用性：评论有用性与评论内容的相互作用，电子商务研究和应用 11 (2012) 205–217。


[14] H. Baek, J. Ahn, Y. Choi, Helpfulness of online consumer reviews: readers' objectives and review cues, International Journal of Electronic Commerce 17 (2012) 99 126.




[14] H. Baek、J. Ahn、Y. Choi，在线消费者评论的有用性：读者的目标和评论线索，国际电子商务杂志 17 (2012) 99 126。


[15] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Transactions on Knowledge and Data Engineering 23 (2011) 1498–1512.




[15] A. Ghose，P.G. Ipeirotis，估计产品评论的有用性和经济影响：挖掘文本和评论者特征，IEEE Transactions on Knowledge and Data Engineering 23 (2011) 1498–1512。


[16] M. Li, L. Huang, C. Tan, K. Wei, Helpfulness of online product reviews as seen by consumers: source and content features, International Journal of Electronic Commerce 17 (2013) 101–136.




[16] M. Li、L. Huang、C. Tan、K. Wei，消费者眼中的在线产品评论的有用性：来源和内容特征，国际电子商务杂志 17 (2013) 101-136。


[17] L. Connors, S.M. Mudambi, D. Schuff, Is it the review or the reviewer? A multi-method approach to determine the antecedents of online review helpfulness, Proceedings of the 44th Hawaii International Conference on System Sciences 2011, pp. 1–10.




[17] L.康纳斯，S.M. Mudambi，D. Schuff，是评论还是评论者？确定在线审阅有用性的前因的多种方法，2011 年第 44 届夏威夷国际系统科学会议论文集，第 1-10 页。


[18] Q. Xu, Should I trust him? The effects of reviewer profile characteristics on eWOM credibility, Computers in Human Behavior 33 (2014) 136–144.




[18]问徐，我应该相信他吗？审稿人资料特征对电子口碑可信度的影响，计算机在人类行为中的作用 33 (2014) 136–144。


[19] J.C. McCroskey, T.A. Jenson, Image of mass media news sources, Journal of Broadcasting 19 (1975) 169–180.




[19] J.C.麦克罗斯基，T.A. Jenson，大众媒体新闻来源的形象，广播杂志 19 (1975) 169–180。


[20] J. Devi, Estimating the helpfulness and economic impact of product reviews, Int. J. Innov. Res. Dev. 1 (2012) 232–236.




[20] J. Devi，估计产品评论的有用性和经济影响，Int。 J.Innov。资源。开发。 1（2012）232-236。


[21] P.F. Wu, In search of negativity bias: an empirical study of perceived helpfulness of online reviews, Psychology and Marketing 30 (2013) 971–984.




[21] P.F.吴，寻找消极偏见：在线评论感知有用性的实证研究，心理学与营销 30 (2013) 971-984。


[22] P. Fei Wu, H. van der Heijden, N.T. Korfiatis, The influences of negativity and review quality on the helpfulness of online reviews, International Conference on Information Systems 2011, pp. 1–10.




[22] P. Fei Wu, H. van der Heijden, N.T. Korfiatis，消极性和评论质量对在线评论有用性的影响，2011 年国际信息系统会议，第 1-10 页。


[23] D. Yin, S.D. Bond, H. Zhang, Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews, MIS Quarterly 38 (2014) 539–560.




[23] D. Yin，S.D. Bond，H.Zhang，焦虑还是愤怒？离散情绪对在线评论感知有用性的影响，MIS Quarterly 38 (2014) 539–560。


[24] M. Jensen, J. Averbeck, Z. Zhang, Credibility of anonymous online product reviews: a language expectancy perspective, Journal of Management Information Systems 30 (2013) 293–324.




[24] M. Jensen、J. Averbeck、Z. Zhang，匿名在线产品评论的可信度：语言期望视角，管理信息系统杂志 30 (2013) 293–324。


[25] K. Floyd, R. Freling, S. Alhoqail, H. Cho, T. Freling, How online product reviews affect retail sales: a meta-analysis, Journal of Retailing 90 (2014) 217–232.




[25] K. Floyd、R. Freling、S. Alhoqail、H. Cho、T. Freling，在线产品评论如何影响零售销售：荟萃分析，零售杂志 90 (2014) 217​​-232。


[26] P. De Maeyer, Impact of online consumer reviews on sales and price strategies: a review and directions for future research. The Journal of Product and Brand Management 21 (2012) 132–139.




[26] P. De Maeyer，在线消费者评论对销售和价格策略的影响：回顾和未来研究方向。产品与品牌管理杂志 21 (2012) 132–139。


[27] G. Cui, H.-K. Lui, X, Guo, The effect of online consumer reviews on new product sales. International Journal of Electronic Commerce 17 (2012) 39–57.




[27] G.崔，H.-K。吕X，郭，网络消费者评论对新产品销售的影响。国际电子商务杂志 17 (2012) 39–57。


[28] N. Hu, L. Liu, J.J. Zhang, Do online reviews affect product sales? The role of reviewer characteristics and temporal effects, Information Technology and Management 9 (2008) 201–214.




[28] 胡宁，刘丽，J.J.张，网络评论会影响产品销售吗？审稿人特征的作用和时间效应，信息技术与管理 9 (2008) 201-214。


[29] E. Lee, S. Shin, When do consumers buy online product reviews? Effects of review quality, product type, and reviewer's photo, Computers in Human Behavior 31 (2014) 356–366.




[29] E. Lee, S. Shin，消费者何时购买在线产品评论？评论质量、产品类型和评论者照片的影响，人类行为中的计算机 31 (2014) 356–366。


[30] Y.C. Ku, C.P. Wei, H.W. Hsiao, To whom should I listen? Finding reputable reviewers in opinion-sharing communities, Decis. Support. Syst. 53 (2012) 534–542.




[30] Y.C.库，C.P.魏 H.W.萧，我该听谁的？在意见共享社区中寻找信誉良好的审稿人，Decis。支持。系统。 53（2012）534-542。


[31] T.L. Ngo-Ye, A.P. Sinha, The influence of reviewer engagement characteristics on online review helpfulness: a text regression model, Decis. Support. Syst. 61 (2014) 47-58.




[31] T.L. Ngo-Ye，A.P. Sinha，审稿人参与特征对在线审稿有用性的影响：文本回归模型，Decis。支持。系统。 61（2014）47-58。


[32] B. Fang, Q. Ye, D. Kucukusta, R. Law, Analysis of the perceived value of online tourism reviews: influence of readability and reviewer characteristics, Tourism Management 52 (2016) 498–506.




[32] B. Fang，Q. Ye，D. Kucukusta，R. Law，在线旅游评论感知价值分析：可读性和评论者特征的影响，旅游管理 52 (2016) 498-506。


[33] Z. Liu, S. Park, What makes a useful online review? Implication for travel product websites, Tourism Management 47 (2015) 140–151.




[33] Z. Liu, S. Park，什么才是有用的在线评论？对旅游产品网站的影响，旅游管理 47 (2015) 140–151。


[34] J. Otterbacher, “Helpfulness” in online communities: a measure of message quality, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, Boston, Massachusetts, USA 2009, pp. 1–10.




[34] J. Otterbacher，在线社区中的“帮助”：消息质量的衡量标准，计算系统中人为因素 SIGCHI 会议记录，ACM，美国马萨诸塞州波士顿，2009 年，第 1-10 页。


[35] Y. Liu, X. Huang, A. An, X. Yu, Modeling and predicting the helpfulness of online reviews 2008 Fighth JFFE International Conference on Data Mining, JFFE 2008 pp. 443–452.




[35] Y. Liu，X. Huang，A. An，X. Yu，在线评论的建模和预测有用性2008 Fighth JFFE 国际数据挖掘会议，JFFE 2008，第 443-452 页。


[36] W. Shen, Y. Jeffrey Hu, J. Rees Ulmer, Competing for attention: an empirical study of online reviewers' strategic behavior, MIS Ouarterly 39 (2015) 683–696.




[36] W. Shen，Y. Jeffrey Hu，J. Rees Ulmer，争夺注意力：在线审稿人策略行为的实证研究，MIS Ouarterly 39 (2015) 683–696。


[37] L. Zhu, G. Yin, W. He, Is this opinion leader's review useful? Peripheral cues for online review helpfulness L. Electron, Commer, Res, 15 (2014) 267–280.




[37] 朱丽，尹刚，何伟，这个意见领袖的评论有用吗？在线评论有用性的外围线索 L. Electron, Commer, Res, 15 (2014) 267–280。


[38] J. Mosteller, C. Mathwick, Reviewer online engagement: the role of rank, well-being, and market helping behavior, Journal of Consumer Marketing 31 (2014) 464–474 http://dx.doi.org/10.1108/JCM-05-2014-0974




[38] J. Mosteller, C. Mathwick，审稿人在线参与：排名、幸福感和市场帮助行为的作用，消费者营销杂志 31 (2014) 464–474 http://dx.doi.org/10.1108/JCM-05-2014-0974


[39] R. Hardin, Trustworthiness, Ethics 107 (1996) 26–42.




[39] R. Hardin，可信度，伦理学 107 (1996) 26-42。


[40] R. Mayer, J. Davis, F. Schoorman, An integrative model of organizational trust, The Academy of Management Review 20 (1995) 709–734.




[40] R. Mayer、J. Davis、F. Schoorman，组织信任的综合模型，管理学院评论 20 (1995) 709–734。


[41] R. Hardin, Trust and Trustworthiness, Russel Sage Foundation, New York, 2002.




[41] R. Hardin，信任与可信度，罗素·塞奇基金会，纽约，2002 年。


[42] C. Hovland, W. Weiss, The influence of source credibility on communication effectiveness, Pub. Opin. Q. 15 (1951) 635–650.




[42] C. Hovland，W. Weiss，来源可信度对沟通有效性的影响，Pub。意见。问 15 (1951) 635–650。


[43] D. Berlo, J. Lemert, R. Mertz, Dimensions for evaluating the acceptability of message sources, Pub. Opin. Q. 33 (1969) 563–576.




[43] D. Berlo、J. Lemert、R. Mertz，评估消息源可接受性的维度，Pub。意见。问：33（1969）563-576。


[44] P.B. Lowry, D.W. Wilson, W.L. Haig, A picture is worth a thousand words: source credibility theory applied to logo and website design for heightened credibilit and consumer trust, International Journal of Human Computer Interaction 30 (2013) 63–93.




[44] P.B.洛瑞，D.W.威尔逊，W.L. Haig，一张图片胜过千言万语：源可信度理论应用于标志和网站设计以提高可信度和消费者信任，国际人机交互杂志 30 (2013) 63-93。


[45] S. Utz, P. Kerkhof, J. Van Den Bos, Consumers rule: how consumer reviews influence perceived trustworthiness of online stores, Electronic Commerce Research and Applications 11 (2012) 49–58.




[45] S. Utz、P. Kerkhof、J. Van Den Bos，消费者规则：消费者评论如何影响在线商店的感知可信度，电子商务研究和应用 11 (2012) 49-58。


[46] S. Chaiken, D. Maheswaran, Heuristic processing can bias systematic processing: effects of source credibility, argument ambiguity, and task importance on attitude judgment, Journal of Personality and Social Psychology 66 (1994) 460–473.




[46] S. Chaiken，D. Maheswaran，启发式处理可能会使系统处理产生偏差：来源可信度、论证模糊性和任务重要性对态度判断的影响，人格与社会心理学杂志 66 (1994) 460-473。


[47] M. Cheung, C. Luo, C. SIA, H. Chen, How do people evaluate electronic word-ofmouth? Informational and normative based determinants of perceived credibility of online consumer recommendations in China, PACIS 2007 Proceedings 2007, p. 18.




[47] 张明，罗俊，C. SIA，陈浩，人们如何评价电子口碑？基于信息和规范的中国在线消费者推荐感知可信度的决定因素，PACIS 2007 Proceedings 2007，第 14 页。 18.


[48] S. Norman, B. Avolio, F. Luthans, The impact of positivity and transparency on trust in leaders and their perceived effectiveness, The Leadership Quarterly 21 (2010) 350–364.




[48] S. Norman、B. Avolio、F. Luthans，积极性和透明度对领导者信任及其感知有效性的影响，《领导力季刊》21 (2010) 350-364。


[49] J. Jaccard, R. Turrisi, Interaction Effects in Multiple Regression - Vol. 72 (Quantitative Applications in the Social Sciences), SAGE Publications Inc., 2003




[49] J. Jaccard、R. Turrisi，多元回归中的交互作用 - 卷。 72（社会科学中的定量应用），SAGE Publications Inc.，2003 年


[50] A.C. Cameron, P.K. Trivedi, Regression Analysis of Count Data, Cambridge Universit Press, New York, 2013.




[50] A.C.卡梅伦，P.K. Trivedi，《计数数据的回归分析》，剑桥大学出版社，纽约，2013 年。


[51] T. Kumar, Multicollinearity in regression analysis, The Review of Economics and Statistics 57 (1975) 365–366.




[51] T. Kumar，回归分析中的多重共线性，《经济学与统计评论》57 (1975) 365–366。


[52] R.M. O'brien, A caution regarding rules of thumb for variance inflation factors, Quality and Quantity 41 (2007) 673–690.




[52] R.M. O'brien，关于方差膨胀因子经验法则的警告，质量与数量 41 (2007) 673–690。


[53] P. Rousseeuw, A. Leroy, Robust Regression and Outlier Detection (Wiley Series in Probability and Mathematical Statistics), Wiley, New York, 1987.




[53] P. Rousseeuw、A. Leroy，稳健回归和异常值检测（Wiley 系列概率与数理统计），Wiley，纽约，1987 年。


![](/api/attachments/UHPKF9MA/fulltext/images/a4ce692e22090210e984b91aa37ecc3386ffad5165643f6cb778ca4e53daf94e.jpg)




![](/api/attachments/UHPKF9MA/fulltext/images/a4ce692e22090210e984b91aa37ecc3386ffad5165643f6cb778ca4e53daf94e.jpg)


Shankhadeep Banerjee is a doctoral student of Management Information Systems at the Indian Institute of Management Calcutta. He holds B.Tech in Computer Science and Engineering from National Institute of Technology (Durgapur), PGDM/MBA from Indian Institute of Management Calcutta and IMP certi cate from NEOMA Business School, France. His research interests are in e-commerce, business analytics, social networks, and adoption of technology. He has prior IS research experience at Indian School of Business Hyderabad, where his research work on smart city maturity model received press coverage at national level. He also has extensive IS practitioner experience working at top technology firms like Microsoft, Amazon, and eBay.




Shankadeep Banerjee 是印度加尔各答管理学院管理信息系统专业的博士生。他拥有印度国立理工学院（杜尔加布尔）计算机科学与工程学士学位、印度加尔各答管理学院 PGDM/MBA 学位以及法国 NEOMA 商学院 IMP 证书。他的研究兴趣包括电子商务、商业分析、社交网络和技术采用。他之前在印度海得拉巴商学院拥有信息系统研究经验，他在智慧城市成熟度模型方面的研究工作受到了国家层面的媒体报道。他还拥有在微软、亚马逊和 eBay 等顶级科技公司工作的丰富 IS 从业经验。


![](/api/attachments/UHPKF9MA/fulltext/images/059b962fc22245b22dabb6f128fa6e7f8a719ed6f5e55cc239f245a0014dbba2.jpg)




![](/api/attachments/UHPKF9MA/fulltext/images/059b962fc22245b22dabb6f128fa6e7f8a719ed6f5e55cc239f245a0014dbba2.jpg)


Samadrita Bhattacharyya is a doctoral student of Management Information Systems at the Indian Institute of Manage ment Calcutta. She holds B.Tech in Electronics and Communication Engineering from West Bengal University of Technology and M.Tech in VISI Design from Indian Institute of Engineering Science and Technology, Shibpur (formerly Bengal Engineering and Science University, Shibpur). Her research interests include social networks, business analytics, optimization and algorithms, and VLSI design. Her research articles have appeared in conference proceedings of IEEE.




Samadrita Bhattacharyya 是印度加尔各答管理学院管理信息系统专业的博士生。她拥有西孟加拉理工大学电子与通信工程学士学位和印度工程科技学院什布尔分校（原孟加拉工程与科学大学什布尔分校）的 VISI 设计硕士学位。她的研究兴趣包括社交网络、业务分析、优化和算法以及超大规模集成电路设计。她的研究论文发表在 IEEE 会议论文集上。


![](/api/attachments/UHPKF9MA/fulltext/images/bd509c435665ecdbd436a49ed403d240f26048949a5253ccb6002ea67018d3dc.jpg)




![](/api/attachments/UHPKF9MA/fulltext/images/bd509c435665ecdbd436a49ed403d240f26048949a5253ccb6002ea67018d3dc.jpg)


Indranil Bose is Professor of Management Information Systems at the Indian Institute of Management, Calcutta. He acts as Coordinator of IIMC Case Research Center. He holds a B.Tech. from the Indian Institute of Technology, MS from the University of Iowa, MS and Ph.D. from Purdue University. His research interests are in business analytics, telecommunications, information security, and supply chain management. His publications have appeared in Communications of the ACM, Communications of AIS, Computers and Operations Research, Decision Support Systems, Ergonomics, European Journal of Operational Research, Information & Management International Journal ofProduction Economics Journal of Organizational Computing and Electronic Com: merce, Journal of the American Society for Information Science and Technology, Operations Research Letters etc. He is listed in the International Who”'s Who of Professionals, Marquis Who”'s Who in the World, Marquis Who”'s Who in Asia, Marquis Who”'s Who in Science and Engineering, and Marquis Who”'s Who of Emerging Leaders 2007. He serves as Senior Editor of Decision Support Systems and as Associate Editor of Communications of AIS, Information & Management, Information Technology & Management and several other IS journals.




Indranil Bose 是加尔各答印度管理学院管理信息系统教授。他担任 IIMC 案例研究中心协调员。他拥有科技学士学位。印度理工学院学士学位、爱荷华大学硕士学位、爱荷华大学硕士学位和博士学位。来自普渡大学。他的研究兴趣包括商业分析、电信、信息安全和供应链管理。他的论文发表于 Communications of the ACM、Communications of AIS、Computers and Operations Research、Decision Support Systems、Ergonomics、European Journal of Operational Research、Information & Management International Journal ofProduction Economics Journal of OrganizationalComputing and Electronic Com: Merce、Journal of the American Society for Information Science and Technology、Operations Research Letters 等。他被列入国际专业人士名人录、Marquis 世界名人录、Marquis 亚洲名人录、入选 Marquis 科学与工程名人录、Marquis Who 2007 新兴领袖人物奖。他担任《Decision Support Systems》的高级编辑，以及《AIS》、《Information & Management》、《Information Technology & Management》和其他几本 IS 期刊 Communications 的副主编。
