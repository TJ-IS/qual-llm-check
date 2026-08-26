---
otero_id: 1240
otero_key: "PVBMCFXF"
title: "The effect of intrinsic and extrinsic quality cues of digital video games on sales: An empirical investigation"
authors: "Hoon S. Choi; Myung S. Ko; Dawn Medlin; Charlie Chen"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.12.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The effect of intrinsic and extrinsic quality cues of digital video games on sales: An empirical investigation

Hoon S. Choi <sup>a,</sup>⁎, Myung S. Ko <sup>b</sup>, Dawn Medlin <sup>a</sup>, Charlie Chen <sup>a</sup>

<sup>a</sup> Department of Computer Information Systems and Supply Chain Management, Appalachian State University, 287 Rivers St, Boone, NC 28608, United State <sup>b</sup> Department of Information Systems and Cyber Security, The University of Texas at San Antonio, 1 UTSA Circle, San Antonio, TX 78249, United States

## a r t i c l e i n f o

Article history: Received 27 June 2017 Received in revised form 4 December 2017 Accepted 5 December 2017 Available online xxxx

Keywords: Intrinsic cue Extrinsic cue Signaling theory Digital video games User engagement Retro games

## a b s t r a c t

This study examines the effect of product quality cues on sales of digital video games, using signaling theory as a theoretical model. The quality cues are examined from two angles: intrinsic and extrinsic. The intrinsic cues, in this study, include company reputation, newness, and retro features and extrinsic cues include review valence, product popularity, price, and user engagement. Based on a publicly available panel data of 142,590 observations for 5415 digital video games, our empirical results suggest that both intrinsic and extrinsic quality cues affect sales of digital video games. Company reputation of a digital video game, however, does not have a significant effect on sales. Although an overall relationship between price and sales is positive, this is not the case for less popular digital video games. This study provides the implications for IS research and practice.

© 2017 Published by Elsevier B.V.

## 1. Introduction

The video game market is one of the largest and fastest growing domains in the IT industry. The global video game industry revenue, which represented approximately 20% of the global software industry revenue in 2013 [42.43], reached \$93 billion in 2013 from \$79 billion in 2012, It is expected to increase to \$118.6 billion by 2019 [98]. Video games can be categorized into several segments by their platforms, such as console, mobile, and personal computer (PC) games. PC games and console games are the two largest segments that generate 60% of the global video game industry revenue [98]. As with other IT domains, these markets have experienced significant changes in their technologies and business models. One of the most important trends is the change in distribution of media formats from physical copy (i.e., CD) to digital copy. For instance, 56% of video games in the U.S. were distributed using digital format from online marketplaces in 2015 [36]. Although console games still highly rely on physical copy format in their distribution, 92% of all PC games were sold through direct download from the digital gaming marketplaces such as steam.com, origin.com, and amazon.com in 2013 [107].

While the online market provides convenient transaction environments to both retailers and consumers, it has some limitations in delivering potential quality of a product when compared to a traditional market [129]. For example, consumers using online markets cannot easily inspect a product to assess its quality compared to those in the traditional market. Because of uncertainty about the quality of products, consumers generally examine various quality cues to infer the product quality prior to purchase [137]. According to their characteristics, there are two types of cues: intrinsic and extrinsic. Intrinsic cues represent inherent product attributes that cannot be easily changed [110]. Physical product features [1], objective product rankings, and national reputation [11] belong to this category. Extrinsic cues are productrelated attributes but not part of the physical product. Personal referrals (e.g., traditional word-of-mouth (WOM) and electronic word-of-mouth (eWOM)) are the most commonly used extrinsic cues [4,23,35,137]. Price, warranty, packaging, and advertising [11,129] are also extrinsic cues. In order to understand how such quality cues influence consumers' purchase decisions in an online market, many prior studies adopted a signaling theory as their research framework [2,9,23,85,127, 129]. They found that the quality cues affect various aspects of purchase decision and may be more influential in an e-commerce context due to the information asymmetries between consumers and sellers [9]. Although many e-commerce studies have investigated the effect of intrinsic and extrinsic quality cues based on signaling theory, there are several research gaps, which allow us further investigation into the domain. First, most of the extant literature has focused heavily on extrinsic cues, especially on eWOM factors [2,9,23,49,72,120,129,133]. To the extent of our knowledge, however, few focused on both extrinsic and intrinsic cues in their studies even though consumers use both cues in assessing product quality [129]. Second, dependent measures of the product quality cues in these studies are limited to influential factors on purchase decision, rather than actual purchase. The dependent measures include trust in the online retailer [2,72], perceived risk in the online transaction [9,133], customer satisfaction [72], and intention to purchase [27,49,129]. Although these are highly influential factors to purchase decision, the effect of the cues on actual sales remains unclear in the extant literature. Lastly, most prior empirical studies that have examined the effect of eWOM focused on extrinsic cues in the context of tangible products, such as, digital cameras [50], restaurants [136], and beauty products [23]., However, intangible digital products, such as music/movie streaming services and cloud-computing applications, have received little attention in the literature although this type of products imposes greater uncertainty about product quality [106,119].

Our study extends the extant literature in several important ways. First, we adopt signaling theory to investigate how quality cues influence product sales utilizing both intrinsic cues and extrinsic cues. Second, we employ actual sales figures as the dependent measure to identify whether both intrinsic and extrinsic cues affect sales. Third, we adopted a large market data collected on 5415 digital video games, which are intangible products that have been rarely studied in the prior research. Fourth, this study introduces unique quality cues for digital products, such as retro and user engagement, which have been overlooked in the previous research. Fifth, the findings of our study provide additional insights to the literature of signaling theory, intrinsic/extrinsic cues, and eWOM. For example, our study indicates that price effect on sales differs by product popularity, showing the moderating effect of popularity on the relationship, rather than a direct positive, negative, or insignificant impact [34,70,125,135]. Lastly, it is one of the first attempts to investigate the effect of quality cues on product sales in the context of the digital video game market. Although Zhu and Zhang [137] examined the relationship between eWOM and the sales of video games, they focused on tangible CD games, not digital video games.

The rest of the paper is organized as follows. The next section provides a literature review and theoretical foundation of this study, followed by discussion of major hypotheses of this study along with the research model. We then present the data collection process and the results of data analysis. Finally, we conclude with the theoretical and practical contributions of this study. We also address the limitations of this study and future research directions.

## 2. Literature review

## 2.1. Signaling theory

In conventional market transactions, buyers often have less information about products than sellers do (i.e., information asymmetries) and hence, need to infer overall product quality from credible information signals [75]. Signaling theory has been adopted as a theoretical framework in numerous studies to understand how consumers with information asymmetries assess product quality prior to purchase [129]. Although some previous studies considered unique quality signals in the environment of e-commerce, such as website quality [49,72,129] and eWOM [23,49,85], most of the signals in their studies are traditional signals that are available for offline stores as well, such as price, warranties, and advertising intensity. Using experiments [2,9,27,120,129,133], in addition, the majority of these studies have investigated the effect on tangible products, such as cosmetics [23], apparel [9,129], movie DVDs [49], electronics (e.g., flash drives and digital camera) [49,120], and books [71,120], which are also available at offline stores. Whereas, few discussed the effect in the context of an online service sector, including music/movie streaming services, cloud-computing applications (i.e., software-as-a-service), and digital video games. With regard to typology of quality signals, most of these studies heavily focused on extrinsic cues, such as advertising [2,9], warranties [9,133], seller reputation at online stores [9,49,72,120], website quality [72,129], price [85,120], consumer rating [23,48], and trust signs on online retailers' websites [2,133] but seldom on intrinsic cues. Extrinsic cues are generally more influential than intrinsic cues because they require less time to attain and effort to understand [31]. In e-commerce, however, consumers readily access the product specification (i.e., intrinsic cues on a product) at a retailer's website. As such, consumers can use intrinsic cues as well as extrinsic cues to assess product quality before purchase.

## 2.2. Quality signals: intrinsic and extrinsic cues

According to cue utilization theory, products consist of a wide range of quality cues such as price, brand name, packaging, and color, which indicate their potential quality to consumers [100,101]. The extant literature has categorized them into two groups by characteristics of the cues: intrinsic and extrinsic cues [110]. Intrinsic cues are attributes derived directly from a product and thus, they cannot be changed or manipulated without changing the product itself [11]. Whereas, extrinsic cues are those relatively easy to alter and are not inherent to a product. For a desktop computer product, specifications of video card, CPU, and RAM can be considered as intrinsic cues while consumer ratings (e.g., five-star rating systems) and price can be as extrinsic cues [129]. The cue typology has been adopted in numerous studies [5,38,53,93, 97,118,129] to understand how the cues affect consumers' perceived quality perception, which refers to the consumer's judgement about the excellence of a product [135]. These studies commonly reported that both intrinsic and extrinsic cues are closely associated with the perceived quality.

Limited e-commerce literature employed the framework of intrinsic and extrinsic cues to explore their relationship with purchase intention. For instance, Chen and Dubinsky [21] reported that valence of online shopping experience, e-retailer's reputation, and product price have a positive relationship with perceived product quality, which is also positively associated with purchase intention. However, their study investigated only extrinsic cues, arguing that intrinsic signals are generally not available on a website to estimate product quality. However, contemporary e-commerce websites, such as Amazon and eBay, provide affluent intrinsic cues (i.e., product specifications) of products on their websites. In addition, the authors used survey data collected from 110 respondents, which may not be sufficient for understanding the general behavior of e-commerce consumers in various market domains. Langan et al. [78] produced another e-commerce study employing utilization theory. The authors focused on how the effect of quality cues on purchase intention differs by the other quality cues. They found that higher levels of consumer review variance in consumer review (i.e., the lack of consensus among reviewers) decrease purchase intention more substantially for utilitarian products than for hedonic products. They also suggested that as brand equity of product increases, the effect of reviewer credibility on purchase intention decreases, implying that a strong brand equity can lessen the impact of online consumer reviews. The authors developed an interesting discussion on dynamics of intrinsic and extrinsic cues in e-commerce. However, they limited their discussion to behavioral intention to purchase, rather than actual purchase or sales of the consumers.

## 2.3. eWOM

Although a few e-commerce studies adopted quality cue typologies as their theoretical framework, numerous extant studies discussed the impact of eWOM, an extrinsic cue, on purchase decision or sales [4,23,35,59,89,137]. The two most commonly examined eWOM factors in the studies are the number of reviews (volume) and average ratings (valence). However, results of these studies are somewhat mixed. While Liu [89], Duan et al. [35], and Amblee et al. [4] found that the volume of eWOM significantly influences product sales, these studies did not find any significance of the review valence, which is measured by average ratings. The result indicates that the volume of reviews is an important extrinsic cue on sales [4] but not user ratings. Chevalier and Mayzlin [24] found that the impact of one-star ratings is greater in decreasing book sales than that of five-star ratings in increasing the sales. Gu et al. [51] also suggested that online reviews affect consumers' evaluation of product quality. They found that positive online reviews improve the sales of popular products more than the sales of niche products.

Table 1 summarizes the selected empirical studies that have investigated the impact of product quality cues on purchase decision.

## 3. Hypothesis development

## 3.1. Intrinsic quality cues of digital video games

## 3.1.1. Company reputation

Company reputation of a product or service (e.g., JD Power, U.S. Consumer Report, and Moody's) is an intrinsic quality cue, which is an inherent, firmly bonded to a product [11]. Although some previous studies classified similar concepts such as brand names on package [1, 135] into extrinsic cues, most considered the company brand reputation as an intrinsic quality cue of a product [11,12,80,113]. Extant literature commonly found that company brand reputation is one of the primary factors in determining consumers' perceived product quality [15,55] and purchase intention [11]. In e-commerce studies, although many researchers have examined the effect of e-retailer reputation [9,27,71], few considered company reputation in their investigation. Amblee and Bui [4] examined the effect of author's reputation on the sales of a book in an online book store. However, they estimated the reputation using the average review rating of the author's book available at the website, rather than an objective brand index estimated by a reliable organization.

We expect that company reputation of a digital video game would positively affect its sales due to the following reasons. First, the digital video game market is a highly competitive domain, where consumers can find numerous similar products. In such an environment, the reputation can offer a competitive edge to differentiate a product from its competitors [55]. Second, digital video games are experience products that do not allow consumers to fully understand real quality until actually experiencing it [30]. Consumers are less confident in buying experience products than search products (e.g., calculator) because it is more difficult to evaluate the product quality due to their intangibility. The effect of brand reputation is more significant for intangible products than the tangible ones [11,55]. For instance, Brady et al. [11] found that the effect of national brand reputation on sales is more critical for mutual funds due to its intangibility, compared to hotels and computers, which are considered more tangible services and goods than mutual funds. Therefore, we propose the following hypothesis:

Hypothesis 1. Company reputation of a digital video game has a positive impact on its sales.

## 3.1.2. Newness

Newness is one of the key indicators of perceived product quality, affecting product sales [10,91]. Overall, 25% of the consumers who have purchased a product reported that they did it due to its newness [10]. Extant literature illustrated that the positive impact of newness on sales in the context of the automotive [122], womenswear [46], digital music [105], and digital movie markets [134]. Especially for the IT products, consumers tend to perceive brand-new technologies as having better quality than old ones as they have advanced design and superior technology performance [99,108]. Digital video games are technical products, utilizing various information technologies. Therefore, we expect that brandnew games enjoy a better market performance. In addition, digital video games are hedonic products, similar to music and movies. In the digital music market, newness is a primary driver of sales growth. According to the research conducted by Pandora, an Internet music streaming service, brand-new songs have 2.31% higher sales than the others in the same category [105]. For the digital movies on Amazon and Netflix, brand-new movies tend to rank higher [134], suggesting a positive relationship between newness and sales. Therefore, we propose the following hypothesis:

Hypothesis 2. Newness of a digital video game has a positive impact on its sales.

Selected empirical e-Commerce Research on Product Quality Cues.

<table><tr><td>Article</td><td>Quality cue</td><td>Dependent measure</td><td>Product</td><td>Data source</td></tr><tr><td>Cheung et al. [23]</td><td>Action/opinion based information (eWOM)</td><td>Intention to purchase</td><td>Cosmetics</td><td>Online cosmetics community</td></tr><tr><td>Well et al. [129]</td><td>Website quality</td><td>Intention to use website to purchase</td><td>Tote bags</td><td>Experiment</td></tr><tr><td>Gregg and Walczak [49]</td><td>E-image (business name and images)</td><td>Willingness to transact</td><td>Movie DVDs and flash drives</td><td>Experiment</td></tr><tr><td>Su [120]</td><td>Price and retailer rating (reputation)</td><td>Expected value and price aversion</td><td>Digital cameras and books</td><td>Experiment</td></tr><tr><td>Yen [133]</td><td>Third party endorsement, warranty, and physical store presence</td><td>Perceived risk and intention to purchase</td><td>Sunscreen lotion</td><td>Experiment</td></tr><tr><td>Chu et al. [27]</td><td>Reputation of infomediary, retailer, and manufacturer</td><td>Intention to transact</td><td>Computer monitor</td><td>Experiment</td></tr><tr><td>Biswas and Biswas [9]</td><td>Retailer reputation warranties, and advertising</td><td>Perceived risk</td><td>Dress shirt, jeans, and music CDs</td><td>Experiment</td></tr><tr><td>Kim et al. [72]</td><td>Website quality and reputation</td><td>Trust in online store and market efficiency</td><td>Book</td><td>Experiment</td></tr><tr><td>Mavlanova et al. [92]</td><td>Perceived seller quality, perceived product quality</td><td>Purchase intention</td><td>Medicine</td><td>Experiment</td></tr><tr><td>Amblee and Bui [4]</td><td>Number of reviews, average rating, author rating</td><td>Sales rank as a proxy of actual sales</td><td>Amazon Shorts e-books</td><td>Amazon</td></tr><tr><td>Liu [89]</td><td>Volume of eWOM and positive/negative reviews</td><td>Box office revenue</td><td>Movies</td><td>Yahoo! Movies</td></tr><tr><td>Zhu and Zhang [137]</td><td>Price, average review rating, variation of ratings, number of online reviews</td><td>Sales</td><td>Video games</td><td>GameSpot.com</td></tr><tr><td>Duan et al. [35]</td><td>Number of postings, ratings</td><td>Box office sales</td><td>Movies</td><td>Yahoo! Movies, Variety.com, BoxOfficeMojo.com</td></tr><tr><td>Chevalier and Mayzlin [24]</td><td>Number of reviews, % of one-star and five-star reviews</td><td>Sales rank</td><td>books</td><td>Amazon.com, Barnesandnoble.com (bn.com)</td></tr><tr><td>Zhou and Guo [136]</td><td>Reviewer connectedness, expertise, and review valence</td><td>Review Helpfulness</td><td>restaurants</td><td>Yelp.com</td></tr><tr><td>Gu et al. [51]</td><td>Average rating, number of reviews, product age, price</td><td>Sales</td><td>books</td><td>Amazon.com</td></tr></table>

Please cite this article as: H.S. Choi, et al., The effect of intrinsic and extrinsic quality cues of digital video games on sales: An empirical investigation, Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.12.005

## 3.1.3. Retro

Retro refers to reproducing of core ideas of classic products with innovative approaches, generally utilizing new technologies [13,18]. Retro is a pervasive trend in various sectors such as movies, television dramas, fashion, electronics, and vehicles [18]. For example, major vehicle manufacturers such as Volkswagen, Fiat, and BMW, have released retro models of their classic vehicles (e.g., Beetle, Fiat 500, and Mini) in the last decade [18]. Despite an overall downward trend in the vehicle market, these models were a huge success. Retro is also one of the notable trends in the contemporary video game market. Major developers have introduced retro video games by applying modern technologies to popular classic games, maintaining core fun factors of their classic versions. Major classic arcade game companies in the 1980s and 1990s, such as Atari and Rare, recently re-released N100 of their classics through digital marketplaces such as Steam and Xbox Live [52]. Blizzard, one of the largest digital video game developers, also announced the release of a remastered StarCraft, one of the best-sellers introduced in 1998 [84].

In terms of product novelty, retro video games may have a disadvantage in their market performance because they are inherently old and trite. From the perceived product quality aspect, however, retro video games should have unique competitive advantages in the market. First, they have a nostalgic value, which has explained the success of certain historic documentaries, drama series, and movies [41,121]. The value can be the critical reason to purchase for consumers who have experienced the games in the past because it should remind them of an early memory with the games [54]. Second, they have an established brand reputation from their original versions, reducing perceived risk in purchase decision [65,67]. Therefore, retro games would be more appealing than other games even to those consumers who have not experienced the games in the past. Third, they contain qualified fun factors in their early versions, as well as simple game structures [123]. This advantage would attract light users who want to enjoy them without learning difficult tactics or controls. This discussion suggests the following hypothesis:

Hypothesis 3. Retro digital video games have higher sales than those of the other games.

## 3.2. Extrinsic quality cues of digital video games

## 3.2.1. eWOM: review valence

In e-commerce, perceived quality of a product can be presented in the form of eWOM [76,116]. eWOM refers to positive or negative statements shared by internet consumers about a product, service, brand, or company [39,76,82]. Nielson's 2011 study reported that 70% of the Internet users rely on eWOM when they make their purchase decisions [19] because it is generated by consumers who share their experience as well as details about products or services via Internet channels (e.g., social media, Internet forums) [22]. Therefore, eWOM has substantial effects on purchase decisions [22], more than traditional WOM [74]. Prior studies indicated that eWOM reviews play an important role in encouraging or discouraging the sales of various market domains, includ ing book and DVD [90], commercial software [4,35], freeware [3], movies [25,69], music [33,95], video games [30], and mobile apps [57, 88].

Review valence, one of the commonly investigated factors of eWOM, represents positive or negative experiences of previous buyers with certain products or services (e.g., five-star rating systems) [25]. Previous eWOM empirical studies reported inconsistent results on the relationship between the review valence and consumers' purchase decision. Although some studies suggested that an improvement in product review valence increases the intention to purchase [24,30,35,59], others reported that the valence does not have a significant effect on the intention [35,89] or sales [89]. In the digital video market, however, we expect that consumers would rely on review valence to make purchase decisions because the market is highly competitive, where numerous products compete for the consumers. In such an environment, consumers actively use review valence to narrow their consideration set. For instance, in online hotel reservation websites, where consumers find numerous similar hotel options, they consider review valence to be important in their purchase decisions [126]. As aforementioned, moreover, digital video games are experience products with high intangibility, imposing a significant quality uncertainty about the products. Therefore, they would depend on the valence to ease the uncertainty prior to purchase [103]. This discussion suggests the following hypothesis:

Hypothesis 4. Review valence of a digital video game has a positive impact on its sales.

## 3.2.2. User engagement

Engagement refers to “the state of being involved, occupied, retained, and intrinsically interested in something” [73] (page 361), which is different from simple acceptance (e.g., product purchase) in that it focuses on the continuous involvement of users. For Internet services such as email, search engines, and social networks, the engagement of users is one of the primary measures of their success and user satisfaction, highlighting the positive aspects of current users' experience and growth potential of the services [63,83]. Recent IT literature on user engagement also has reported its positive impact on the success of information systems [63,86].

In terms of quality cue typology, user engagement can be a distinctive extrinsic cue for Internet services, representing the perceived quality by current users. For instance, Nintendo Wii Sports released in 2006 is one of the most popular games in video game history, recorded at 82.78 million copies [124]. However, its popularity may not represent the perceived quality of the consumers in a recent market. This does not affect the current sales of the game. In addition, social or personal interaction is one of the primary reasons to play digital video games [26]. The video games, such as MMORPG's (Massively Multiplayer Online Role-Playing Games) and FPS (First Person Shooting) games, are more enjoyable as more users engage in the games because the users have greater opportunities to interact with diverse players [58]. Therefore, potential consumers perceive such an interactional aspect of the games as a product quality cue, affecting the purchase decision. This discussion leads to the following hypothesis:

Hypothesis 5. User Engagement of a digital video game has a positive impact on its sales.

## 3.2.3. Product popularity

Extant e-commerce studies demonstrated that product popularity is one of the primary factors to determine purchase decision [20,35,137]. They suggested that products purchased by more consumers are perceived as having superior quality and consequently, consumers prefer such products [23,24,44,132]. The theory of herd behavior also supports this tendency. Because consumers want to simplify their decision or avoid potential risks, they tend to follow the majority [20,61]. For technology products such as digital video games, the perceived quality increases as more users adopt them because a large user base represents technical stability, supportive contents, add-on products, and skilled labor in terms of network externalities [29,40,114]. Therefore, we predict that a popular digital video game has a better market performance.

Hypothesis 6. Popularity of a digital video game has a positive impact on its sales.

## 3.2.4. Price

Price is an important attribute that implies the potential quality of a product. In terms of perceived quality, consumers tend to perceive expensive products or services as having superior quality [34,125,135]. However, such perception on a high priced product may not always link to purchase intention. Although many prior studies have examined the relationship between price and willingness to purchase in the context of various products, such as food [6,17,32,60], electronics [34,94], and digital virtual items [70], they have found inconclusive results. High price may discourage consumers to purchase such a product due to monetary pressure [17,32,34], while perceived superior quality induced by high price may encourage consumers to buy the product [6,60]. Therefore, it may have no significant relationship with the intention because consumers would make a reasonable purchase decision considering price utility, which refers to value for price, or they simply do not mind paying high price for emotional reasons [94,135].

According to a recent study that investigated sales of digital items in a social network service, price utility does not have a significant impact on intention to purchase digital items because they are hedonic products, which are consumed for entertainment and enjoyment [70]. For hedonic products, consumers consider to be price utility less important than for utilitarian products, which are consumed for practical purposes. Similarly, digital video games are also hedonic products. Therefore, price utility should be less influential on purchase decisions. Rather, the consumers would use price as a quality cue. For example, consumers often view ‘free to play’ digital video games, as having poor quality because they are offered free of charge [112]. Furthermore, the average video game consumers, who are approximately 37 years old and generally have stable income [37], are likely to view high price as a signal of quality items and less sensitive to price. Thus, they are more likely purchase such products [68]. This discussion leads us to the following hypothesis:

Hypothesis 7a. Price of a digital video game has a positive impact on its sales.

Although high price may represent superior quality of a product and thus, positively influence its sales, the degree of the relationship would depend on user engagement. Zhu and Zhang [137] reported that the high price of less popular products has a negative impact on their sales. This suggests that although consumers consider high price as a signal of superior quality for popular products, they do not for less popular products. From the perspective of risk taking behaviors, price is one of the major risks for consumers in making their purchase decisions [8, 64,79] and thus, they are less likely to accept a high price if their desired product is less popular in the market. In the digital video game context, the impact of price on sales of digital video games would depend on the level of product popularity. Therefore, we propose the following hypothesis:

Hypothesis 7b. The impact of price on sales is negative for less popular digital video games.

Fig. 1 illustrates the research model of this study summarizing the proposed hypotheses.

## 4. Research methodology and analysis

## 4.1. Data collection

In order to test our hypotheses, we collected data from the following sources: steamspy.com, store.steampowered.com, and steamdb.info. Steamspy.com is a website to track sales of digital video games offered by Steam, one of the world's largest digital video game distributors [96,109]. Because it uses a sampling method to calculate the sales data using approximately 150,000 user accounts per day, the data might be different from the actual sales data. However, the margin of error is known as b0.33% [102] and thus, the data is close to the actual data [45]. The available data at steamspy.com include daily sales of each digital video game, the number of game owners, and user score (i.e., user rating). Store.steampowered.com is an official digital store of Steam, providing detailed description of digital video games, such as genre, release date, price, screen shots of games, and minimum PC system requirements. Steamdb.info is a third party website of Steam, providing various data collected from Steam's database. Available data at this website include active users, discount pricing deals, and average/median playtime of each game. We collected data between 8 A.M. and 10 A.M. for about four months, from November 13, 2015 to March 11, 2016 and matched the three datasets by game names and dates, constructing a dataset for 5415 digital video games, which includes 142, 590 observations.

## 4.2. Construct operationalization

## 4.2.1. Dependent measure: sales

We used the number of daily downloads of each digital video game to measure its daily sales volume, which is the dependent measure for our study, Sales

![](/api/attachments/PVBMCFXF/fulltext/images/0b7d313b12cdcdd539027df79ee6c9026cf7f671b1cd3aaabb2eaee2ef435302.jpg)  
Fig. 1. Research model.

Please cite this article as: H.S. Choi, et al., The effect of intrinsic and extrinsic quality cues of digital video games on sales: An empirical investigation, Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.12.005

Table 2  
Descriptive statistics.

<table><tr><td>Construct</td><td>Variable</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td>Sales</td><td>DailySales</td><td>4523.104</td><td>4486.793</td><td>1001</td><td>121,495</td></tr><tr><td>Newness</td><td>ProductAge</td><td>1095.057</td><td>835.704</td><td>0</td><td>4625</td></tr><tr><td>Review valence</td><td>UserScore</td><td>0.758</td><td>0.180</td><td>0.03</td><td>1</td></tr><tr><td>Popularity</td><td>Owners</td><td>367,022.500</td><td>875,112.700</td><td>1167</td><td>20,717,871</td></tr><tr><td>Price</td><td>Price</td><td>13.017</td><td>11.101</td><td>0.140</td><td>199</td></tr><tr><td>Engagement</td><td>CurrentPlayers</td><td>608.544</td><td>10,273.500</td><td>0</td><td>669,198</td></tr><tr><td></td><td></td><td colspan="2">Frequency (n = 142,590)</td><td></td><td></td></tr><tr><td>Company reputation</td><td>MajorCcompany (dummy)</td><td>28,518</td><td></td><td></td><td></td></tr><tr><td>Retro</td><td>Retro (dummy)</td><td>10,193</td><td></td><td></td><td></td></tr></table>

4.2.2. Intrinsic quality cues: company reputation, newness, and retro

Company Reputation is operationalized using annual game company rankings of metacritic.com, operated by CBS Corporation. The website provides comprehensive reviews of media products including music albums, video games, films, TV shows, and video games. The video game industry has recognized it as one of the most powerful review sources [111]. We found that 19 video game companies listed either once or more than once as major brands during 2010 and 2016. We coded Company Reputation as 1 if a digital video game is created or published by the major companies, 0 otherwise. Newness of a digital video game is estimated using age of digital video games, calculated for the difference between their release date and date of data collection. Thus, Newness has an inverse relationship with age. We estimated Retro based on the release date of the game. As major media commonly described, the games released before 2000 are considered retro video games [115]. Since Steam.com started their business in 2003, moreover, the games released before 2000 should be retro games that have been reproduced for the service platform of Steam.com. Therefore, the games released before 2000 are considered Retro, which was coded as 1 and 0 otherwise.

4.2.3. Extrinsic quality cues: review valence, product popularity, price, and user engagement

Review Valence is operationalized as the user score of each digital video game. The user score represents the overall evaluation provided by game users. Although a number of studies have explored Product Popularity, they used different measures. They include accumulated sales volume [35,61], market share [16], sales rank [35,137], online review quantity [104], the age of the product [137], and conversion rate (i.e., how many consumers who had viewed a product actually purchased it) [66]. In this study, Product Popularity is operationalized as the number of owners of digital video games, which stands for accumulated sales volume. Price is sales price of a game at each time point. When a game was offered at a discounted price, the discounted price is used for Price, not its original price. With regard to User Engagement, there are multiple measures, including the number of total clicks, average number of page views per visit, and the number of active days of a user [83]. One of the most popularly adopted measures in extant empirical studies is the number of active users, which refers to the number of distinct users who use the service for a day [28,128]. Therefore, User Engagement is operationalized as the number of active users.

## 4.3. Data analysis

As aforementioned, we collected total 142,590 observations on 5415 digital video games for this current study. Table 2 summarizes the descriptive statistics for each variable, corresponding to the major constructs. Table 3 presents the correlation matrix of the variables. Although the dependent measure, Daily Sales, has relatively strong correlations with Owners Before (0.517) and Current Players (0.454), there is no significant correlation between the independent variables.<sup>1</sup>

LowOwners ∗ Price is an interaction term of Price and LowOwners, which is a dummy variable for less popular games. Within the variable Owners that represents Product Popularity, we categorized the bottom 80% of digital video games into the less popular group, based on Pareto principle, which is also known as 80/20 rule. In business, it refers to a phenomenon that a few popular products (20%) create most market sales (80%) [14]. Likewise, in the digital video game market, a small portion of popular games has the large portion of users. In our dataset, we found that the top 20% of popular digital video games account for about 72% of the entire accumulated sales. We applied a logtransformation to DailySales, Owners, and ProductAge due to their skewed and large distributions, changing them into LnDailySales, LnOwners, and LnProductAge respectively. We incorporated two control variables, Discounted and Bundled, which seem to affect the sales of a digital video game. Each indicates whether sales price is the discounted or original price (e.g., 1 if discounted, 0 otherwise) and whether a digital video game is bundled with additional benefits such as game OST, game characters, or other video games (e.g., 1 if bundled, 0 otherwise). As Kohli and Devaraj [77] suggested, it is important to observe the effect of IT systems on individual or organizational performance over an extended time period. To consider this lagged effect, many e-commerce studies used the independent variables at t − 1 to investigate the effect of the information at e-commerce websites on product sales because the information browsed on the webpages is generally created in the previous day [56,81,88,130]. In this study, we adopted the independent variables at t − 1 (i.e., day-1) and performed a regression with sales of a digital video game at t. The empirical model including these variables is as follows:

$$
\begin{array}{r l} L n D a i l y S a l e s _ {i, t} & = \alpha_ {0} + \alpha_ {1} M a j o r C o m p a n y _ {i} + \alpha_ {2} L n P r o d u c t A g e _ {i, t - 1} \\ & + \alpha_ {3} R e t r o _ {i} + \alpha_ {4} U s e r S c o r e _ {i, t - 1} + \alpha_ {5} L n O w n e r s _ {i, t - 1} \\ & + \alpha_ {6} P r i c e _ {i, t - 1} + \alpha_ {7} L o w O w n e r s * P r i c e _ {i, t - 1} + \alpha_ {8} C u r r e n t P l a y e r s _ {i, t - 1} \\ & + \alpha_ {9} D i s c o u n t e d _ {i, t - 1} + \alpha_ {1 0} B u n d l e d _ {i} + \varepsilon_ {i, t} \end{array}
$$

where i represents product and t represents day.

Since the dataset employed in this study is a panel dataset, which is likely to have the violation of OLS (Ordinary Least Squares) assumptions, we conducted a Breusch-Pagan test for heteroscedasticity and a Wooldridge test for autocorrelation. Not surprisingly, we found both heteroscedasticity and autocorrelation (AR1) in the model. Therefore, an OLS is not a reliable estimator to test the model, suggesting that an alternative approach such as a random effects model with Hueber/ White standard error correction is necessary [47]. Although a fixed effects estimator is generally more rigorous than the random effects in analyzing panel data, it does not allow incorporating important time invariant variables such as Retro and MajorCompany in the model [62]. Further, because the dataset includes the substantially larger number of digital video games (c.f., 5415 games) than the number of timeperiods (c.f., 162 days) in the dataset, it is too costly in terms of degree of freedom.

Table 3 Correlation matrix.

<table><tr><td>Variable</td><td>Daily sales</td><td>Major company</td><td>Product age</td><td>Retro</td><td>User score</td><td>Owners</td><td>Price</td><td>Current players</td></tr><tr><td>DailySales</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MajorCompany</td><td>0.059</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ProductAge</td><td>0.132</td><td>0.019</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Retro</td><td>-0.011</td><td>-0.091</td><td>0.236</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>UserScore</td><td>0.194</td><td>0.050</td><td>0.071</td><td>0.061</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>Owners</td><td>0.511</td><td>0.021</td><td>0.180</td><td>-0.022</td><td>0.206</td><td>1.000</td><td></td><td></td></tr><tr><td>Price</td><td>0.168</td><td>0.149</td><td>-0.108</td><td>-0.068</td><td>0.089</td><td>0.140</td><td>1.000</td><td></td></tr><tr><td>CurrentPlayers</td><td>0.181</td><td>-0.007</td><td>-0.017</td><td>-0.012</td><td>0.034</td><td>0.454</td><td>0.084</td><td>1.000</td></tr></table>

## 4.4. Analysis results

Table 4 summarizes the analysis results of a random effects estimator with Hueber/White standard error correction and the regression models considering the lag effects of the independent variables on the dependent. The model significantly predicts 42.2% variance of the dependent variable, $L n D a i l y S a l e s _ { i , t }$ (Wald $^ { \chi 2 } = 2 5 , 0 8 8 . 7 1 0 , p < 0 . 0 0 )$

Contrary to our expectation, the coefficient of MajorCompany <sub>−</sub> (α ) is negative and statistically not significant $( p = 0 . 1 2 2 )$ , not supporting Hypothesis 1 that predicts a positive relationship between brand reputation of digital game companies and sales. The coefficient of LnProductAge (α ) is negative and statistically significant $( p <$ 0.01), supporting Hypothesis 2 that newness of a digital video game has a positive impact on its sales (c.f., LnProduct $\cdot A g e _ { i , t \mathrm { ~ - ~ } 1 }$ is an inverse proxy of Newness<sub>i,t − 1</sub>). The coefficient of Retro<sub>i</sub> (α<sub>3</sub>) is positive and significant $\left( p < 0 . 0 1 \right)$ . This implies that if a digital video game is retro, it is more likely to have higher sales, which supports Hypothesis 3. The coefficient of UserScor $\mathring { \mathbf { \Omega } } _ { i , t \mathrm { ~ - ~ } 1 } \left( \alpha _ { 4 } \right)$ is positive and significant $\left( p < 0 . 0 1 \right)$ , indicating that review valence is positively associated with sales of a digital video game. Thus, Hypothesis 4 is supported. LnOwne $\mathbf { \hat { S } } _ { i , t - 1 } \left( \alpha _ { 5 } \right)$ is also statistically significant $\left( p < 0 . 0 1 \right)$ , and its coefficient is positive. This supports Hypothesis 5, which predicts a positive relationship between popularity and digital video game sales. Regarding Hypothesis 6a, the coefficient of $P r i c e _ { i , t - 1 } \left( \alpha _ { 6 } \right)$ is positive and statistically significant (p b 0.01), corresponding to its prediction that price of a digital video game has a positive impact on its sales. LowOwners $\ast P r i c e _ { i , t - 1 } \left( \alpha _ { 7 } \right)$ is statistically significant $\left( p < 0 . 0 1 \right)$ and its coefficient is negative. This indicates that the positive impact of price is less for the games with low popularity. Therefore, Hypothesis 6a and Hypothesis 6b are supported. Lastly, the coefficient of CurrentPlayers <sub>−</sub> (α ) is positive and statistically significant $( p = 0 . 0 4 7 )$ , suggesting a positive relationship between user engagement and sales of a digital video game. Thus, Hypothesis 7 is supported. Concerning the control variables, $D i s c o u n t e d _ { i , t - 1 }$ is statistically significant $( p = 0 . 0 1 5 )$ and positive, indicating a positive relationship between discount pricing and the sales while Bundled $( p =$ 0.217) is not significant.

Analysis results.

<table><tr><td>R-squared (overall)</td><td></td><td colspan="2">0.422</td></tr><tr><td>F-Statistics (Wald  $x^{2}$ )</td><td></td><td colspan="2">25,088.710**</td></tr><tr><td>Dependent: LnDailySales</td><td>Coefficient</td><td>Robust standard error</td><td>p-Value</td></tr><tr><td>Constant</td><td>4.7674</td><td>0.0276</td><td>0.000**</td></tr><tr><td>MajorCompany $_{i,t}$ </td><td>-0.0103</td><td>0.0067</td><td>0.122</td></tr><tr><td>LnProductAge $_{i,t - 1}$ </td><td>-0.0308</td><td>0.0036</td><td>0.000**</td></tr><tr><td>Retro $_{i}$ </td><td>0.0355</td><td>0.0125</td><td>0.005**</td></tr><tr><td>UserScore $_{i,t - 1}$ </td><td>0.0757</td><td>0.0138</td><td>0.000**</td></tr><tr><td>LnOwners $_{i,t - 1}$ </td><td>0.3000</td><td>0.0027</td><td>0.000**</td></tr><tr><td>Price $_{i,t - 1}$ </td><td>0.0022</td><td>0.0003</td><td>0.000**</td></tr><tr><td>LowOwners * Price $_{i,t - 1}$ </td><td>-0.0032</td><td>0.0004</td><td>0.000**</td></tr><tr><td>CurrentPlayers $_{i,t - 1}$ </td><td>0.0001</td><td>0.0001</td><td>0.047*</td></tr><tr><td>Discounted $_{i,t - 1}$ (control)</td><td>0.0186</td><td>0.0008</td><td>0.015*</td></tr><tr><td>Bundled $_{i}$ (control)</td><td>0.0312</td><td>0.2529</td><td>0.217</td></tr></table>

⁎⁎ p N 0.01  
\* p N 0.05

In order to check robustness of the test results, we conducted several robustness tests. First, we conducted a time-sensitivity test, extending the time lag to t-2, t-3, and t-4. Overall, hypothesis test results remained constant although the p-value of each variable slightly changes. We also applied different definitions to major dummy variables to examine whether their hypothesis results change. For instance, we extended the definition of MajorCompany <sub>−</sub> to medium sized gaming companies. However, the test result for Hypothesis 1 stayed constant. The result for Hypothesis 3 also did not change when we applied a different definition of $R e t r o _ { i } ,$ games released before 1995 (c.f., originally before 2000).

## 5. Discussion and implications

This study investigated the impact of intrinsic and extrinsic quality cues on product sales in the context of the digital video game sector. It examined conventional quality cues, which have been recognized as having a significant relationship with product sales, as well as noble quality cues for digital video games such as retro and user engagement. While the overall results correspond to the extant literature, enhancing the theoretical foundations of this study, it provides unique findings for both IS research and practitioners in the market.

## 5.1. Discussion

Concerning company reputation, we found that the reputation does not affect sales of digital video games. This is somewhat surprising because it does not correspond to a common belief in the industry [7] and the extant literature, suggesting a positive impact of company reputation on product sales [11,55]. This unexpected finding may result from unique company brand typologies of video game companies. A digital video game generally has two types of company brands: developers and publishers. Game developers are the companies that create the games dealing with technical jobs, such as game algorithm design, graphics design, and programming, while publishers are responsible for quality assurance, marketing, and distribution of the games. Although consumers generally regard developers as important in their purchase decision, they do not consider publishers important because publishers are not significantly involved in developing the games [87]. The established gaming company brands, such as Microsoft, Konami, Sega, and Electronic Arts, are generally publishers, rather than developers. Therefore, consumers may not view them as a quality cue of digital video games. Another possible explanation for the insignificant relationship between company reputation and sales is the presence of eWOM for digital video games. According to Amblee et al. [4], consumers tend to rely on brand reputation of a product to assess the product quality when eWOM is not readily available. However, when it is available, this effect diminishes. Because consumers in the digital video game market are exposed to various forms of eWOM from multiple sources such as online communities and websites of distributors, they would be less likely to use company reputation of developers or publishers to infer potential quality of a video game.

We found that newness of a digital video game has a positive influence on its sales, corresponding to the findings of extant literature. This indicates that newness is one of the quality cues that signals novel game contents and advanced technical features of a digital video game. Review valence is found to have a positive impact on the sales of a digital video game. It suggests that a positive review valence of a digital video game is likely to increase its product sales, which is consistent with the extant eWOM literature. Popularity of a digital video game is found to have a positive impact on sales. This result is also consistent with knowledge of quality cues, eWOM, and networking effects, suggesting that popularity is a significant quality cue of a product that can encourage (or discourage) product sales. Our finding validates a positive relationship between price of a digital video game and its product sales by illustrating that sales of a digital video game increases as its price does. This finding indicates that digital video game consumers would consider high price an indicator of superior product quality [6,60]. However, a negative moderating effect for less popular games suggests that sales of less popular games decrease as their price increases because consumers do not view high price as a quality signal if digital video games are not popular.

We tested two novel extrinsic quality cues for digital video games: retro and user engagement. Retro features of a digital video game are found to have a positive relationship with its sales. This finding suggests that retro features can be a positive quality signal of a digital video game to attract consumers. It also implies that major consumers in the digital video game market, who are approximately 37 years old on average and have experienced the original of retro games [37], seem to have a favorable attitude toward retro games, stimulating their nostalgia. User engagement is found to have a positive influence on sales of a digital video game. This indicates that the degree of engagement can be an important extrinsic quality cue that represents potential quality of the games and increase sales of a digital video game.

## 5.2. Theoretical and practical contributions

This study has several theoretical contributions to the research of signaling theory, quality cues typologies, and eWOM. It is one of the first attempts to examine the theories in the context of the digital video game market. The findings of this study extend the scope of the theories to the digital video game market by providing significant empirical evidence of the relationship between quality cues and sales of games. Second, it introduces novel dimensions of quality cues for digital products by adding retro and user engagement that have been overlooked in the research for digital products, such as software [4, 35], mobile apps [57,88], and digital music [33,95]. Particularly, retro, which is pervasive in various markets, would be a noticeable product quality cue for those digital products that should be incorporated in future research. Third, although numerous IT studies have investigated the relationship between the size of technology user base and its future sales [29,114,117,131], few considered the difference between regular owners and active users of the technologies. This study shows that the number of active users of technologies is another critical factor that should be considered in future research as well as the size of the owners of technologies. Fourth, prior studies have examined the relationship between price and sales, simply investigating a direct impact [34,70, 125,135] but rarely considered the moderating effect of popularity on the relationship. This study shows that the impact of price on sales differs by popularity.

The findings discussed above provide important practical implications for the digital video game industry to promote sales of games and to improve their digital distribution channels. Concerning intrinsic cues, first, company reputation may not be critical in determining success of a digital video game. For small-medium sized developers, this study suggests that publishing games via well-known publishers may not necessarily guarantee the success of the games. Whereas, it also implies that they can succeed without the support of major publishers if they make quality games that receive a positive evaluation from users. Second, practitioners need to understand that digital video game consumers would perceive brand-new games as quality products and thus, are more likely to purchase. Therefore, they need to concentrate on their marketing effort at the early stage of the games. In the same vein, the distribution websites may consider highlighting new games at their websites. For instance, they need to prepare an independent category for new video games on their front pages to grab consumers' attention, which in turn, improves the overall sales. Third, developing retro video games would be a profitable approach because of their inherent advantages such as nostalgic value and established reputation from their original versions. Given the significantly lower development cost for retro games, particularly, retro strategy should be a more cost effective and less risky approach for their business. Practitioners in other digital product markets, such as mobile apps and digital music, may utilize the retro strategy in creating their products, recreating the successful classics. For example, mobile app game developers need to consider designing a game app adopting core features of successful classic games.

With regard to extrinsic cues, positive review valence encourages consumers to purchase digital video games. Therefore, practitioners need to consider marketing strategies to attain positive evaluations from users. For example, they may actively communicate with loyal customers, especially those with a high level of RFM (Recency, Frequency, and Monetary) to encourage them to participate in the game evaluation in the form of eWOM. Designers of the digital distribution channels should highlight the evaluation score at their websites to help consumers' purchase decisions. For instance, they may place the score near primary product information such as game name, price, and screenshots. Product popularity, operationalized with the number of game owners, is also a vital determinant of sales of digital video games. Therefore, the companies should focus on increasing the number of product owners. For instance, they may conduct member gets member (MGM) promotions or use a short-term discount pricing to boost the number of the owners, yet not to hurt perceived quality of games. They also need to focus on retaining and increasing active users to boost future sales by satisfying current game users. For the user retention and acquisition, they can adopt a community or party system in their game design to enhance social activities among the users. Concerning pricing strategy, the finding suggests that a low pricing strategy may hurt sales of digital video games. Although offering the games at low price may increase sales in certain circumstances, practitioners should be aware that it leads customers to perceive the video games as poor quality and therefore, it may lead to a sales decrease overall. However, this does not mean that high price always increases sales of digital video games. As our finding indicates, when a game is unpopular in the market, a high pricing strategy may discourage consumers from purchasing it.

## 6. Limitations and future research

This study has several limitations that can be opportunities for future research. Future research may examine or extend the findings of this study by considering the limitations. First, although Steamspy.com provides the sales data of steam.com, it only includes the sales performance of the games at the digital store. However, there are other digital marketplaces such as Xbox Live Marketplace for Xbox, PlayStation Store for PlayStation, and Amazon Digital Services. Researchers may include these distributors to understand a more comprehensive relationship between product quality cues and sales of a digital video game in various contexts. Second, although the dataset adopted in this study is large, including over 140,000 observations, it only covers a four-month period.

Researchers may examine the dynamics of the digital video game industry, including a longer period to have more solid results on the dynamics between quality cues and sales. Third, future research may consider more diverse product attributes and market conditions. For instance, although this study found that product popularity moderates the positive relationship between price and sales, there can be additional moderating factors such as game platform and presence of a demo version (i.e., a free trial version). Finally, yet importantly, future research may extend the theoretical framework of quality cue typologies, considering additional quality cues. For example, the success of previous versions could be relevant to sales of a digital video game, which is a halo effect from the previous versions' established reputation in the market (e.g., Call of Duty series, GTA series and NBA2K series). Another perceived quality factor could be eWOM shared in independent social communities for game users, which might have a substantial relationship with sales of digital video games.

## Acknowledgement

The authors would like to thank the editor and two anonymous reviewers for their valuable suggestions that significantly improved the quality of this manuscript.

## References

[1] L.B. Acebrón, D.C. Dopico, The importance of intrinsic and extrinsic cues to expected and experienced quality: an empirical application for beef, Food Quality and Preference 11 (2000) 229–238.

[2] K.D. Aiken, D.M. Boush, Trustmarks, objective-source ratings, and implied investments in advertising: investigating online trust and the context-specific nature of internet signals, Journal of the Academy of Marketing Science 34 (2006) 308–323.

[3] N. Amblee, T. Bui, Freeware downloads: An empirical investigation into the impact of expert and user reviews on demand for digital goods, AMCIS 2007 Proceedings 2007, p. 21.

[4] N. Amblee, T. Bui, Harnessing the influence of social proof in online shopping: the effect of electronic word of mouth on sales of digital microproducts, International Journal of Electronic Commerce 16 (2011) 91–114.

[5] O. Ampuero, N. Vila, Consumer perceptions of product packaging, Journal of Consumer Marketing 23 (2006) 100–112.

[6] G.A. Baker, P.J. Crosbie, Consumer preferences for food safety attributes: a market segment approach, Agribusiness 10 (1994) 319–324.

[7] A. Barsby, Developers as a Brand – Reputation is Everything, GamingQ, 2016.

[8] J.R. Bettman, Perceived risk and its components: a model and empirical test, Journal of Marketing Research (1973) 184–190.

[9] D. Biswas, A. Biswas, The diagnostic role of signals in the context of perceived risks in online shopping: do signals matter more on the web? Journal of Interactive Marketing 18 (2004) 30–45.

[10] J. Blythe, Innovativeness and newness in high-tech consumer durables, The Journal of Product and Brand Management 8 (1999) 415–429.

[11] M.K. Brady, B.L. Bourdeau, J. Heskel, The importance of brand cues in intangible service industries: an application to investment services Journal of Services Marketing 19 (2005) 401–410.

[12] R.J. Brodie, J.R. Whittome, G.J. Brush, Investigating the service brand: a customer value perspective, Journal of Business Research 62 (2009) 345–355.

[13] S. Brown, Retro-marketing: yesterday's tomorrows, today! Marketing Intelligence & Planning 17 (1999) 363–376.

[14] E. Brynjolfsson, Y. Hu, D. Simester, Goodbye Pareto principle, hello long tail: the effect of search costs on the concentration of product sales, Management Science 57 (2011)1373-1386.

[15] L.M. Cabral, Stretching firm and brand reputation, The Rand Journal of Economics (2000) 658–673.

[16] R. Caminal, X. Vives, Why market shares matter: an information-based theory, The Rand Journal of Economics (1996) 221–239.

[17] J.D.D.S. Carneiro, V.P.R. Minim, R. Deliza, C.H.O. Silva, J.C.S. Carneiro, F.P. Leão, Labelling effects on consumer intention to purchase for soybean oil, Food Quality and Preference 16 (2005) 275–282.

[18] S. Castellano, O. Ivanova, M. Adnane, I. Safraou, F. Schiavone, Back to the future: adoption and diffusion of innovation in retro-industries, European Journal of Innovation Management 16 (2013) 385–404.

[19] P. Chaney, Word of Mouth Still Most Trusted Resources Says Nielsen; Implications for Social Commerce, Digital Intelligence TodayAvailablet at http:// digitalintelligencetoday.com/word-of-mouth-still-most-trusted-resource-saysnielsen-implications-for-social-commerce/ 2012, Accessed date: 16 December 2016.

[20] Y.-F. Chen, Herd behavior in purchasing books online, Computers in Human Behavjor 24 (2008) 1977–1992

[21] Z. Chen, A.J. Dubinsky, A conceptual model of perceived customer value in ecommerce: a preliminary investigation, Psychology and Marketing 20 (2003) 323–347.

[22] C.M. Cheung, D.R. Thadani, The impact of electronic word-of-mouth communication: a literature analysis and integrative model, Decision Support Systems 54 (2012) 461–470.

[23] C.M. Cheung, B.S. Xiao, I.L. Liu, Do actions speak louder than voices? The signaling role of social information cues in influencing consumer purchase decisions, Deci sion Support Systems 65 (2014) 50–58.

[24] J.A. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book reviews, Journal of Marketing Research 43 (2006) 345–354.

[25] P.K. Chintagunta, S. Gopinath, S. Venkataraman, The effects of online user reviews on movie box office performance: accounting for sequential rollout and aggrega tion across local markets, Marketing Science 29 (2010) 944–957

[26] D. Choi, J. Kim, Why people continue to play online games: in search of critical design factors to increase customer loyalty to online contents, Cyberpsychology & Behavior 7 (2004) 11 24.

[27] W. Chu, B. Choi, M.R. Song, The role of on-line retailer brand and infomediary reputation in increasing consumer purchase intention, International Journal of Electronic Commerce 9 (2005) 115–127.

[28] J. Claussen, T. Kretschmer, P. Mayrhofer, The effects of rewarding user engagement: the case of Facebook apps, Information Systems Research 24 (2013) 186 200.

[29] K.R. Conner, Obtaining strategic advantage from being imitated: when can encouraging “clones” pay? Management Science 41 (1995) 209–225.

[30] G. Cui, H.-K. Lui, X. Guo, The effect of online consumer reviews on new product sales, International Journal of Electronic Commerce 17 (2012) 39–58.

[31] N. Dawar, P. Parker, Marketing universals: Consumers' use of brand name, price physical appearance, and retailer reputation as signals of product quality, Journal of Marketing (1994) 81–95.

[32] R. Deliza, The Effects of Expectation on Sensory Perception and Acceptance, University of Reading, 1996

[33] S. Dewan, J. Ramaprasad, Research note-music blogging, online sampling, and the long tail, Information Systems Research 23 (2012) 1056–1067

[34] W.B. Dodds, K.B. Monroe, D. Grewal, Effects of price, brand, and store information on buyers' product evaluations, Journal of Marketing Research 28 (1991) 307–319.

[35] W. Duan, B. Gu, A.B. Whinston, Informational cascades and software adoption on the internet: an empirical investigation, MIS Quarterly (2009) 23–48.

[36] Entertainment Software Association, NPD Group, Computer and video game sales in the United States from 2009 to 2015 by category. StatisticaAvailablet at https://www.statista.com/statistics/190184/us-computer-and-video-game-salesby-categorie-2010/ 2017, Accessed date: 23 November 2016.

[37] ESA, Essential Facts about the Computer Video Game Industry, Entertainment Software AssociationAvailable at http://www.theesa.com/wp-content/uploads/2015/ 04/ESA-Essential-Facts-2015.pdf 2015, Accessed date: 5 January 2017.

[38] C. Fandos, C. Flavian, Intrinsic and extrinsic quality attributes, loyalty and buying intention: an analysis for a PDO product, British Food Journal 108 (2006) 646–662.

[39] A.J. Flanagin, M.J. Metzger, R. Pure, A. Markov, User-generated ratings and the evaluation of credibility and product quality in ecommerce transactions, in: System Sciences (HICSS) (Ed.), 2011 44th Hawaii International Conference on IEEE 2011, pp. 1–10.

[40] J.M. Gallaugher, Y.-M. Wang, Understanding network effects in software markets: evidence from web server pricing, MIS Ouarterly (2002) 303–327.

[411 M.B. Garda. Nostalgia in retro game design. Proceedings of DiGRA. 2013.

[42] Gartner, Gartner Says Worldwide Video Game Market to Total \$93 Billion in 2013, Gartner, 2013.

[43] Gartner, Gartner Says Worldwide Software Market Grew 4.8 Percent in 2013, 2014.

[44] A. Ghose, P.G. Ipeirotis, Designing ranking systems for consumer reviews: The impact of review subjectivity on product sales and review quality, Proceedings of the 16th Annual Workshop on Information Technology and Systems 2006, pp. 303–310.

[45] D. Gilbert, Let's talk steam spy, Wadjeteye Games, 2015 Availablet at http://www. wadjeteyegames.com/2015/04/05/lets-talk-steam-spy/, Accessed date: 26 May 2016.

[46] G. Goldfingle, Infographic: John Lewis Sales Jump 7.3% Over the Half Term Week, ReailWeek, 2014 Availablet at https://www.retail-week.com/companies/johnlewis/infographic-john-lewis-sales-jump-73-over-the-half-term-week/5057891. article, Accessed date: 15 December 2016.

[47] W.H. Greene, Econometric Analysis, Pearson Education, India, 2003

[48] D.G. Gregg, J.E. Scott, The role of reputation systems in reducing on-line auction fraud International Journal of Flectronic Commerce 10 (2006) 95–120

[49] D.G. Gregg, S. Walczak, Dressing your online auction business for success: an experiment comparing two eBay businesses, MIS Quarterly (2008) 653–670.

[50] B. Gu, J. Park, P. Konana, Research note—the impact of external word-of-mouth sources on retailer sales of high-involvement products, Information Systems Research 23 (2012) 182-196

[51] B. Gu, Q. Tang, A.B. Whinston, The influence of online word-of-mouth on long tail formation. Decision Support Systems 56 (2013) 474–481

[52] B. Harland, The Cartridge Comeback: Retro Gaming is Back in StyleAvailablet at http://www.mintel.com/blog/technology-market-news/the-cartridge-comebackretro-gaming-is-back-in-style 2016 Accessed date: 13 April 2017.

[53] A. Heiman, B. McWilliams, D. Zilberman, Demonstrations and money-back guarantees: market mechanisms to reduce uncertainty, Journal of Business Research 54 (2001) 71-84

[54] D.S. Heineman, Public memory and gamer identity: retrogaming as nostalgia, Journal of Games Criticism 1 (2014) 1–24.

[55] P. Herbig, J. Milewicz, The relationship of reputation and credibility to brand success, Journal of Consumer Marketing 10 (1993) 18–24.

[56] N.N. Ho-Dac, S.J. Carson, W.L. Moore, The effects of positive and negative online customer reviews: do brand strength and category maturity matter? Journal of Marketing 77 (2013) 37–53.

[57] S.-C. Ho, Y.-C. Tu, The investigation of online reviews of mobile games, E-Life: Web-Enabled Convergence of Commerce, Work, and Social Life, Springer 2011, pp. 130–139.

[58] A.C. Hou, C.-C. Chern, H.-G. Chen, Y.-C. Chen, ‘Migrating to a new virtual world’: exploring MMORPG switching through human migration theory, Computers in Human Behavior 27 (2011) 1892–1903.

[59] N. Hu, N.S. Koh, S.K. Reddy, Ratings lead you to the product, reviews help you clinch it? The mediating role of online review sentiments on product sales, Decision Support Systems 57 (2014) 42–53.

[60] C.L. Huang, J. Fu, Conjoint analysis of consumer preferences and evaluations of a processed meat, Journal of International Food & Agribusiness Marketing 7 (1995) 35–53.

[61] J.H. Huang, Y.F. Chen, Herding in online product choice, Psychology and Marketing 23 (2006) 413–428.

[62] K.-L. Hui, Y.-L. Lai, S.-J. Yee, Empirical advances for the study of weblogs: Relevance and testing of random effects models, Economics, Information Systems and Electronic Commerce, 2007.

[63] M.I. Hwang, R.G. Thorn, The effect of user engagement on system success: a metaanalytical integration of research findings, Information Management 35 (1999) 229-236.

[64] J. Jacoby, L.B. Kaplan, The components of perceived risk, SV-Proceedings of the Third Annual Conference of the Association for Consumer Research, 1972.

[65] S.L. Jarvenpaa, N. Tractinsky, L. Saarinen, Consumer trust in an internet store: a cross-cultural validation, Journal of Computer-Mediated Communication 5 (1999) (0–0).

[66] H.J. Jeong, K.-N. Kwon, The effectiveness of two online persuasion claims: limited product availability and product popularity, Journal of Promotion Management 18 (2012) 83–99.

[67] S. Jiuan Tan, Strategies for reducing consumers' risk aversion in Internet shopping, Journal of Consumer Marketing 16 (1999) 163–180.

[68] R.L. Johnson, J.J. Kellaris, An exploratory study of price/perceived-quality relationships among consumer services, NA-Advances in Consumer Research Volume 15 (1988).

[69] E.V. Karniouchina, Impact of star and movie buzz on motion picture distribution and box office revenue, International Journal of Research in Marketing 28 (2011) 62–74.

[70] H.-W. Kim, S. Gupta, J. Koh, Investigating the intention to purchase digital items in social networking communities: a customer value perspective, Information Management 48 (2011) 228–234.

[71] H.-W. Kim, Y. Xu, J. Koh, A comparison of online trust building factors between potential customers and repeat customers, Journal of the Association for Information Systems 5 (2004) 13.

[72] S. Kim, R. Williams, Y. Lee, Attitude toward online shopping and retail website quality: a comparison of US and Korean consumers, Journal of International Consumer Marketing 16 (2004) 89–111.

[73] Y.H. Kim, D.J. Kim, K. Wachter, A study of mobile user engagement (MoEN): engagement motivations perceived value, satisfaction, and continued engagement intention, Decision Support Systems 56 (2013) 361–370.

[74] R.A. King, P. Racherla, V.D. Bush, What we know and don't know about online word-of-mouth: a review and synthesis of the literature, Journal of Interactive Marketing 28 (2014) 167–183

[75] A. Kirmani, A.R. Rao, No pain, no gain: a critical review of the literature on signaling unobservable product quality, Journal of Marketing 64 (2000) 66–79.

[76] N.S. Koh, N. Hu, E.K. Clemons, Do online reviews reflect a product's true perceived quality? An investigation of online movie reviews across cultures, Electronic Commerce Research and Applications 9 (2010) 374–385

[77] R. Kohli, S. Devaraj, Contribution of institutional DSS to organizational performance: evidence from a longitudinal study, Decision Support Systems 37 (2004) 103–118.

[78] R. Langan, A. Besharat, S. Varki, The effect of review valence and variance on product evaluations: an examination of intrinsic and extrinsic cues, International Journal of Research in Marketing 34 (2017) 414–429

[79] G. Laurent, J.-N. Kapferer, Measuring consumer involvement profiles, Journal of Marketing Rresearch (1985) 41–53.

[80] D. Lee, G. Ganesh, Effects of partitioned country image in the context of brand image and familiarity: a categorization theory perspective, International Marketing Review 16 (1999) 18–41.

[81] G. Lee, T.S. Raghu, Determinants of mobile apps' success: evidence from the App Store market, Journal of Management Information Systems 31 (2014) 133–170.

[82] J. Lee, J.-N. Lee, Understanding the product information inference process in electronic word-of-mouth: an objectivity–subjectivity dichotomy perspective, Information Management 46 (2009) 302–311.

[83] J. Lehmann, M. Lalmas, E. Yom-Tov, G. Dupret, Models of user engagement, User Modeling, Adaptation, and Personalization (2012) 164–175

[84] K. Leswing, Blizzard is Remaking ‘StarCraft’ With Better Graphics — And It's Making the Original Version Free, Business Insider, 2017 Availablet at http://www. businessinsider.com/starcraft-remastered-photos-details-features-release-date-2017-3 Accessed date: 13 April 2017.

[85] S. Li, K. Srinivasan, B. Sun, Internet auction features as quality signals, Journal of Marketing 73 (2009) 75–92

[86] W.T. Lin, B.B. Shao, The relationship between user participation and system success: a simultaneous contingency approach, Information Management 37 (2000) 283–295.

[87] H. Lindgren, Factors Contributing to the Buying Decision of PC and Video Games: And Their Weight in the Buying Decision Process, 2010.

[88] C.Z. Liu, Y.A. Au, H.S. Choi, Effects of freemium strategy in the mobile app market: an empirical study of Google play, Journal of Management Information Systems 31 (2014) 326–354.

[89] Y. Liu, Word of mouth for movies: its dynamics and impact on box office revenue, Journal of Marketing 70 (2006) 74–89.

[90] Y. Liu, X. Huang, A. An, X. Yu, Reviews are not Equally Important: Predicting the Helpfulness of Online Reviews, Citeseer, 2008.

[91] M.P. Lorange, M.J. Rembiszewski, From Great to Gone: Why FMCG Companies are Losing the Race for Customers, Ashgate Publishing, Ltd., 2014

[92] T. Mavlanova, R. Benbunan-Fich, G. Lang, The role of external and internal signals in E-commerce, Decision Support Systems 87 (2016) 59–68.

[93] V. Midha, P. Palvia, Factors affecting the success of Open Source Software, Journal of Systems and Software 85 (2012) 895–905.

[94] J. Moon, D. Chadee, S. Tikoo, Culture, product type, and price influences on consumer purchase intention to buy personalized products online, Journal of Business Research 61 (2008) 31–39.

[95] M. Morales-Arroyo, T. Pandey, Identification of critical eWOM dimensions for music albums, in: Management of Innovation and Technology (ICMIT) (Ed.), 2010 IEEE International Conference on IEEE 2010, pp. 1230–1235.

[96] K. Mudgal, Valve Releases PR; Steam Userbase Doubles in 2011, Big Picture Mode Coming Soon, Gamingbolt, 2012 Availablet at http://gamingbolt.com/valve-releases-pr-steam-userbase-doubles-in-2011-big-picture-mode-coming-soon, Accessed date: 26 May 2016.

[97] J. Nam, Web portal quality, service operations, logistics and informatics, 2009, SOLI'09. IEEE/INFORMS International Conference on IEEE 2009, pp. 163–168.

[98] Newzoo, The Global Games Market Reaches \$99.6 billion in 2016, Mobile Generating 37%, Newzoo, 2016.

[99] J.C. Nunes, X. Drèze, Your loyalty program is betraying you, Harvard Business Review 84 (2006) 124.

[100] J.C. Olson, Inferential belief formation in the cue utilization process, ACR North American Advances, 1978.

[101] J.C. Olson, J. Jacoby, Cue utilization in the quality perception process, ACR Special Volumes, 1972

[102] K. Orland, Introducing Steam Gauge: Ars reveals Steam's Most Popular Games, Ars Technica, 2015 Availablet at http://arstechnica.com/gaming/2014/04/introducingsteam-gauge-ars-reveals-steams-most-popular-games/, Accessed date: 26 Ma 2016.

[103] C. Park, T.M. Lee, Information direction, website reputation and eWOM effect: a moderating role of product type, Journal of Business Research 62 (2009) 61–67.

[104] D.-H. Park, J. Lee, I. Han, The effect of on-line consumer reviews on consumer purchasing intention: the moderating role of involvement, International Journal of Electronic Commerce 11 (2007) 125–148.

[105] G. Peoples, New Study From Pandora Touts the ‘Pandora Effect’ on Music Sales, Billboard, 2014 Availablet at http://www.billboard.com/articles/business/6319937/ pandora-study-calculate-promotional-effect-music-sales, Accessed date: 12 December 2016.

[106] C. Pleger Bebko, Service intangibility and its impact on consumer expectations of service quality Journal of Services Marketing 14 (2000) 9–26

[107] S. Prell, Report: 92 Percent of PC Game Sales in 2013 Were Digital. Engadget, 2014 Availablet at https://www.engadget.com/2014/08/24/report-92-percent-of-pcgame-sales-in-2013-were-digital/, Accessed date: 6 December 2016.

[108] M.E. Price, The newness of new technology, Cardozo L. Rev, 22, 2000, p. 1885.

[109] J. Reinhardt, Indie Distribution Platforms That are not Steam, Gamasutra, 2012 Availablet at http://www.gamasutra.com/blogs/JanaReinhardt/20120320/ 166531/Indie\_Distribution\_Platforms\_that\_are\_not\_Steam.php, Accessed date: 26 May 2016.

[110] P.S. Richardson, A.S. Dick, A.K. Jain, Extrinsic and intrinsic cue effects on perceptions of store brand quality, Journal of Marketing (1994) 28–36.

[111] M. Rose, Metacritic is Here to Stay, but Can We Fix It? Gamasutra, 2012.

[112] M. Rose, Chasing the Whale: Examining the Ethics of Free-to-play Games, Gamasutra, 2013 Availablet at http://www.gamasutra.com/view/feature/195806/ chasing\_the\_whale\_examining\_the\_.php?print=1, Accessed date: 13 January 2017.

[113] D.P. Roy, The impact of congruence in cause marketing campaigns for service firms, Journal of Services Marketing 24 (2010) 255–263.

[114] M.J. Salganik, P.S. Dodds, D.J. Watts, Experimental study of inequality and unpredictability in an artificial cultural market, Science 311 (2006) 854–856.

[115] J. Scott, Retro Gaming: Why Players Are Returning to the Classics, BBC News, 2017.

[116] S. Senecal, J. Nantel, The influence of online product recommendations on consumers' online choices, Journal of Retailing 80 (2004) 159–169

[117] V. Shankar, B.L. Bayus, Network effects and competition: an empirical analysis of the home video game industry Strategic Management Journal 24 (2003).375-384

[118] N. Srinivasan, S.C. Jain, K. Sikand, An experimental study of two dimensions of country-of-origin (manufacturing country and branding country) using intrinsic and extrinsic cues International Business Review 13 (2004) 65–82

[119] M. Styvén, The intangibility of music in the internet age, Popular Music and Society 30 (2007) 53–74.

[120] B.-C. Su, Consumer e-tailer choice strategies at on-line shopping comparison sites, International Journal of Electronic Commerce 11 (2007) 135–159

[121] J. Suominen, The past as the future? Nostalgia and retrogaming in digital culture, Fibreculture 11 (2008) 1–8.

[122] K. Talke, S. Salomo, J.E. Wieringa, A. Lutz, What about design newness? Investigating the relevance of a neglected dimension of product innovativeness, Journal of Product Innovation Management 26 (2009) 601–615.

[123] C.T. Tan, A. Johnston, A. Bluff, S. Ferguson, K.J. Ballard, Retrogaming as visual feedback for speech therapy, SIGGRAPH Asia 2014 Mobile Graphics and Interactive Applications, ACM, 2014.

[124] P. Tassi, Here are the Five Best-Selling Video Games of All Time, Forbes, 2016 Availablet at http://www.forbes.com/sites/insertcoin/2016/07/08/here-are-thefive-best-selling-video-games-of-all-time/#4f754ea02dee, Accessed date: 18 January 2017.

[125] G.J. Tellis, G.J. Gaeth, Best value, price-seeking, and price aversion: the impact of information and learning on consumer choices, Journal of Marketing (1990) 34–45.

[126] I.E. Vermeulen, D. Seegers, Tried and tested: the impact of online hotel reviews on consumer consideration, Tourism Management 30 (2009) 123–127.

[127] S. Wang, S.E. Beatty, W. Foxx, Signaling the trustworthiness of small online retailers, Journal of Interactive Marketing 18 (2004) 53–69.

[128] G.M. Weiksner, B. Fogg, X. Liu, Six patterns for persuasion in online social networks, International Conference on Persuasive Technology, Springer 2008, pp. 151–163.

[129] J.D. Wells, J.S. Valacich, T.J. Hess, What signal are you sending? How website quality influences perceptions of product quality and purchase intentions, MIS Quarterly (2011) 373–396.

[130] K.L. Xie, K.L. Xie, Z. Zhang, Z. Zhang, Z. Zhang, Z. Zhang, A. Singh, A. Singh, S.K. Lee, S.K. Lee, Effects of managerial response on consumer eWOM and hotel performance: evidence from TripAdvisor, International Journal of Contemporary Hospitality Management 28 (2016) 2013–2034.

[131] J. Yannis Bakos, C.F. Kemerer, Recent applications of economic theory in information technology research, Decision Support Systems 8 (1992) 365–386.

[132] Q. Ye, R. Law, B. Gu, The impact of online user reviews on hotel room sales, International Journal of Hospitality Management 28 (2009) 180–182

[133] H.R. Yen, Risk-reducing signals for new online retailers: a study of single and multiple signalling effects, International Journal of Internet Marketing and Advertising 3 (2006) 299–317.

[134] C. Yeung, G. Cimini, C.-H. Jin, Dynamics of movie competition and popularity spreading in recommender systems, Physical Review E 83 (2011), 016105.

[135] V.A. Zeithaml, Consumer perceptions of price, quality, and value: a means-end model and synthesis of evidence, Journal of Marketing (1988) 2–22.

[136] S. Zhou, B. Guo, The order effect on online review helpfulness: a social influence perspective, Decision Support Systems 93 (2017) 77–87.

[137] F. Zhu, X. Zhang, Impact of online consumer reviews on sales: the moderating role of product and consumer characteristics, Journal of Marketing 74 (2010) 133–148.

Hoon S. Choi is an Assistant Professor of the Department of Computer Information Systems and Supply Chain Management Systems at Appalachian State University. He received his Ph.D. in Information Systems and Cyber Security at the University of Texas at San

Antonio. His research interests include e-commerce, electronic Word-of-Mouth (eWOM), digital piracy, data analytics, information security, and human-computer interactions. Dr. Choi published his paper in journals such as Journal of Management Information Systems (JMIS) and Journal of Information Systems Applied Research.

Myung S. Ko is an Associate Professor of Information Systems and Cyber Security in the College of Business at the University of Texas at San Antonio. She received her Ph.D. in Business Administration with a concentration in Information Systems and Master of Accountancy from Virginia Commonwealth University, and her B.B.A. from the University of Washington. She is a Certified Public Accountant. Her research interests include impact of IT and security breach on organizations, on-line banking, electronic Word-of-Mouth (eWOM), and adoption issues with healthcare information systems. Her work has published in a number of high-quality journals such as Information & Management, Decision Support Systems, Information Systems Frontiers, Communications of the Association for Information Systems, Information Systems Journal, and Information Technology & Management.

Dawn Medlin is a Professor in the Department of Computer Information Systems and Supply Chain Management, John A. Walker College of Business, at Appalachian State University in Boone, NC. During her 28 years of teaching she has taught courses such as Ethical Hacking, Web 2.0 Technologies in Business, Introduction to Gaming, Advanced Security, and Issues in E-Commerce, Her teaching and research activities have mainly been in the area of security, health care informatics, and e-commerce. She has published in journals such as The Journal of Information Systems Security, Information Systems Security, International Journal of Electronic Marketing and Retailing, and the International Journal of Healthcare Information Systems and Informatics. In 2014, Dr. Medlin received the College of Business Research Award for Outstanding Research in her field. Additionally, she has taught at several international universities including the Université d'Angers in France, Addis Ababa University in Ethiopia, and National Chung Cheng University, Taiwan.

Charlie Chen received his Ph.D. degree in Management Information Systems from Claremont Graduate University. Dr. Chen is a professor in the Department of Computer Information Systems and Supply Chain Management at Appalachian State University. His current research interests are business analytics, project management and supply chain management. He is a Project Management Professional (PMP) certified by the Project Management Institute. He has authored N100 referred articles and proceedings, presented at many professional conferences and venues. Dr. Chen has published in journals such as International Journal of Project Management, IEEE Transactions on Engineering Management, Behaviour and Information Technology, Communications of Association for Information Systems, and Journal of Global Information Technology Management. Dr. Chen dedicates himself to be a transnational scholar and is a trip leader for study abroad programs in China, Japan, Spain, and Taiwan. He was a visiting faculty at Zhejiang University in China, Thammasat University in Thailand, and Gakushuin Women's College in Japan.
