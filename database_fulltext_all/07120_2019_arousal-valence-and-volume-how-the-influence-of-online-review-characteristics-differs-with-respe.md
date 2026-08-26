---
otero_id: 7120
otero_key: "BTPSGKQB"
title: "Arousal, valence, and volume: how the influence of online review characteristics differs with respect to utilitarian and hedonic products"
authors: "Jie Ren; Jeffrey V. Nickerson"
year: "2019"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2018.1524419"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Arousal, valence, and volume: how the influence of online review characteristics differs with respect to utilitarian and hedonic products

Jie Ren & Jeffrey V. Nickerson

To cite this article: Jie Ren & Jeffrey V. Nickerson (2018): Arousal, valence, and volume: how the influence of online review characteristics differs with respect to utilitarian and hedonic products, European Journal of Information Systems, DOI: 10.1080/0960085X.2018.1524419

To link to this article: https://doi.org/10.1080/0960085X.2018.1524419

![](/api/attachments/BTPSGKQB/fulltext/images/005d6469064fcd9ad764420450c1b1404ab5cbc7303aab45fce48e4ba8416e7f.jpg)

Published online: 08 Oct 2018.

![](/api/attachments/BTPSGKQB/fulltext/images/3ce9b4232bdd71419126416d7d89bb392d2f1dbc4899fb10862e3785dcabcd19.jpg)

Submit your article to this journal

![](/api/attachments/BTPSGKQB/fulltext/images/61e487f74ebc0bc0835489c8ebd6187ff747d0e7586674f5adbe9d658164a4b2.jpg)

Article views: 4

![](/api/attachments/BTPSGKQB/fulltext/images/1775f63d6f497f3d6f112624dc819b59b2884889d10285993ead566697307948.jpg)

View Crossmark data CrossMark

EMPIRICAL RESEARCH

Check for updates

# Arousal, valence, and volume: how the influence of online review characteristics difers with respect to utilitarian and hedonic products

Jie Ren<sup>a</sup> and Je<sup>f</sup>rey V. Nickerson<sup>b</sup>

<sup>a</sup>Information Systems Department, Gabelli School of Business, Fordham University, New York, USA; <sup>b</sup>School of Business, Stevens Institute of Technology, Hoboken, USA

## ABSTRACT

Online reviews in<sup>fl</sup>uence consumers’ purchase decisions. Product type – speci<sup>fi</sup>cally, whether a product is utilitarian or hedonic – can help explain how consumers react to reviews. Characteristics of reviews – in particular, valence, measured by ratings, the arousal level of the language used in the text and the volume of the reviews – provide heuristics that consumers may use in making purchase decisions. Product type moderates the e<sup>f</sup>ect of these characteristics. Empirical evidence for this claim comes from multiple sources: a panel data analysis of 26,357 Amazon products and an online experiment with 541 participants. The <sup>fi</sup>ndings of studies based on this evidence show that product type (hedonic or utilitarian) moderates the e<sup>f</sup>ect of the three heuristic attributes of online reviews (valence, volume, and arousal) on sales. The analysis uses OLS-<sup>fi</sup>xed e<sup>f</sup>ects models and Granger causality tests. These <sup>fi</sup>ndings explain why past studies have found that sometimes online review valence is more in<sup>fl</sup>uential than volume and arousal with respect to sales and why sometimes this is reversed. Our <sup>fi</sup>ndings have signi<sup>fi</sup>cant theoretical and practical implications for the design of choice architectures in online review systems.

ARTICLE HISTORY Received 30 March 2016 Revised 22 August 2018 Accepted 6 September 2018

ACCEPTING EDITOR Frantz Rowe

ASSOCIATE EDITOR Scott McCoy

KEYWORDS Online review characteristics; purchase decisions; hedonic and utilitarian products; attribute substitution; heuristics; choice architecture

## 1. Introduction

Online review systems gather, process, and display online reviews to help people make purchase decisions (Dimoka, Hong, & Pavlou, 2012; Mavlanova, Benbunan-Fich, & Koufaris, 2012; Mudambi & Schu<sup>f</sup>, 2010). Eighty per cent of consumers claim that they trust online consumer reviews as much as personal recommendations (BrightLocal, 2014). It follows that many <sup>fi</sup>rms are taking advantage of online consumer reviews as a marketing tool (Goh, Heng, & Lin, 2013; Sun, 2011). Firms believe that online consumer reviews a<sup>f</sup>ect consumers’ purchase decisions (Zhu & Zhang, 2010).

However, research has not converged (Chevalier & Mayzlin, 2006; Dellarocas, Zhang, & Awad, 2007; Liu, 2006; Ye, Law, & Gu, 2009). Some studies have found that purchase decisions are driven by the valence of online reviews. Valence expresses positive or negative sentiment, and can be measured by the star rating of a review (Chevalier & Mayzlin, 2006; Dellarocas et al., 2007; Ye, Law, Gu, & Chen, 2011). Other studies have found that volume – de<sup>fi</sup>ned as the number of reviews – drives purchase decisions (Duan, Gu, & Whinston, 2008; Hu & Liu, 2004; Pang, Lee, & Vaithyanathan, 2002). These mixed results challenge theoreticians and practitioners alike.

The goal of this paper is to explain the mixed <sup>fi</sup>ndings reported in previous online review literature. We do this by introducing a moderating variable based on a binary product characteristic: hedonic or utilitarian. Hedonic products satisfy customers’ emotional wants while utilitarian products are evaluated based on their utility (Babin, Darden, & Gri<sup>fi</sup>n, 1994; Cheema & Papatla, 2010; Chiu, Wang, Fang, & Huang, 2014; Kempf, 1999; Sen & Lerman, 2007; Van der Heijden, 2004; Wake<sup>fi</sup>eld, Wake<sup>fi</sup>eld, Baker, & Wang, 2011). This product characteristic has been shown to moderate other decision variables in information systems (IS) literature (Van der Heijden, 2004) and has been discussed in marketing literature to directly explain purchase decisions (e.g. Cheema & Papatla, 2010). In this paper, we used the theory of attribute substitution (Kahneman & Frederick, 2004) to explain how the impacts of online review characteristics on sales vary for di<sup>f</sup>erent products. In the context of online shopping, consumers have di<sup>f</sup>erent expectations when faced with hedonic or utilitarian products (Babin et al., 1994; Chiu et al., 2014). These expectations may interact with the information provided by online reviews and further in<sup>fl</sup>uence purchase decisions. Speci<sup>fi</sup>cally, consumers are likely to have di<sup>f</sup>erent target attributes – emotion or utility – for these two classes of product, and consumers are likely to focus on di<sup>f</sup>erent heuristic attributes contained in the reviews. These heuristic attributes will produce biases, which will show up as weights in regressions that predict purchase decisions. The above suggests that the product type distinction of hedonic or utilitarian may moderate how online reviews a<sup>f</sup>ect purchase decisions.

To study the moderating e<sup>f</sup>ect of product type, we studied valence (the positive or negative sentiment of reviews), volume (the number of reviews), and arousal level of the language (the intensity of the emotions embedded in the reviews). While most studies of sentiment and online reviews focus on valence, a more complex theory of sentiment posits two dimensions: valence and arousal (Russell, 1979, 1980, 2003). Arousal can be measured through the words used in the text. Intuitively, we might expect these dimensions to be highly correlated. However, analyses of language and the brain show that this is not the case (Gerdes et al., 2010; Warriner & Kuperman, 2015). Most of the sentiment-related studies suggest that the correlation that exists is weak and exhibits a U-shaped pattern (Bradley, Hamby, Löw, & Lang, 2007; Kuppens et al., 2017). Arousal and valence can function as heuristic attributes: they can be used in fast decision-making as substitutes for less accessible target attributes. People seeking entertainment may be more likely to be a<sup>f</sup>ected by arousal words because these may address the desire for emotional engagement. People with utilitarian target attributes may be more likely to be a<sup>f</sup>ected by valence because this addresses the quality of the product, which is salient for the goal of utility.

Studying online reviews in relation to sales is complex because online reviews may a<sup>f</sup>ect sales, and, over time, sales may a<sup>f</sup>ect online reviews. To address this complexity, we performed two studies. One utilised panel data on 26,357 Amazon products and the other involved an experiment with 541 participants. The results from both studies showed that the distinction between hedonic and utilitarian product type moderated purchase behaviour in response to online reviews.

This paper’s overall theoretical contribution is to provide an explanation for previous mixed <sup>fi</sup>ndings about the e<sup>f</sup>ect of online reviews on sales. Speci<sup>fi</sup>cally, product type moderates the e<sup>f</sup>ect of valence, arousal, and volume. Arousal is a less-studied characteristic of online reviews. We show it is useful for understanding and predicting consumer behaviour. These results have practical implications for the design of online review systems. In particular, such systems might sort reviews by arousal level as well as by valence. Such systems might also provide di<sup>f</sup>erent orderings of reviews depending on product type.

## 2. Theory development: online reviews and purchase decisions

## 2.1. Previous mixed <sup>fi</sup>ndings in online review systems research

Online review systems reduce information asymmetry between shoppers and retail stores. These systems have attracted researchers’ attention since their inception (Chevalier & Mayzlin, 2006; Dellarocas et al., 2007; Ren, Yeoh, Shan, & Popovič, 2018; Ye et al., 2011). The systems and their e<sup>f</sup>ects on consumers purchase decisions have been studied from many di<sup>f</sup>erent angles (Chevalier & Mayzlin, 2006; Dellarocas et al., 2007; Duan et al., 2008; Hu & Liu, 2004; Pang et al., 2002; Ye et al., 2011). Some studies have identi<sup>fi</sup>ed online review valence as an important factor in purchase decisions (Chevalier & Mayzlin, 2006; Dellarocas et al., 2007; Sen & Lerman, 2007; Ye et al., 2009) while others credit sales to online review volume (Duan et al., 2008; Liu, 2006). These studies are summarised in Table 1.

## 2.2. Online review valence

Valence is the most studied of online review characteristics (e.g. Piccoli, 2016). Studies have contrasted the e<sup>f</sup>ects of positive versus negative online reviews on purchase decisions (Chevalier & Mayzlin, 2006; Dellarocas et al., 2007; Liu, 2006; Ye et al., 2009). For example, Chevalier and Mayzlin (2006) found a positive correlation between online review valence and online book sales. A di<sup>f</sup>erent study found that online review volume and valence were both signi<sup>fi</sup>cant in forecasting movie sales (Dellarocas et al., 2007). In a study based on Chinese hotel data, online review valence a<sup>f</sup>ected the number of hotel rooms booked (Ye et al., 2009). Papers have explained the e<sup>f</sup>ects of positive and negative reviews in terms of negativity bias: people tend to avoid negatives more than they seek positives (Baumeister, Bratslavsky, Finkenauer, & Vohs, 2001). For example, customers avoid products with negative comments more than they are attracted to products with positive comments (Park & Lee, 2009). Although customers tend to post more positive reviews than negative reviews, reviews posted immediately after a customer experience tend to be more negative (Piccoli, 2016).

Interestingly, people may not always exhibit an aversion to negative online information. Research suggests that this psychological mechanism may be connected to the way our brains process information. Negative information is weighted strongly in the brain (Ito, Larsen, Smith, & Cacioppo, 1998). Negative information grabs attention (Baumeister et al., 2001; Rozin & Royzman, 2001). In the case of negative online reviews, under speci<sup>fi</sup>c conditions, negative reviews are not as harmful as presumed.

<table><tr><td rowspan="2">Year</td><td rowspan="2">Study</td><td rowspan="2">Focus</td><td rowspan="2">Data source</td><td rowspan="2">Product type</td><td rowspan="2">Products</td><td colspan="2">Findings</td></tr><tr><td>Volume drives Sales</td><td>Valence drives sales</td></tr><tr><td>2006</td><td>Clemons, Gao, and HittJournal of Management Information Systems</td><td>Valence</td><td>Ratebeer</td><td>Utilitarian and hedonic</td><td>Craft beers</td><td>na</td><td>Yes</td></tr><tr><td>2004</td><td>Chen, Wu, and YoonICIS proceedings</td><td>Volume and valence</td><td>Amazon</td><td>Utilitarian and hedonic</td><td>Books</td><td>Yes</td><td>No</td></tr><tr><td>2006</td><td>Chevalier and MayzlinJournal of Marketing Research</td><td>Valence</td><td>Amazon and Barnes and Noble</td><td>Utilitarian and hedonic</td><td>Books</td><td>na</td><td>Yes</td></tr><tr><td>2008</td><td>Li and HittInformation Systems Research</td><td>Volume and valence</td><td>Amazon</td><td>Utilitarian and hedonic</td><td>Books</td><td>Yes</td><td>Yes</td></tr><tr><td>2010</td><td>Berger, Sorensen, and RasmussenMarketing Science</td><td>Negative valence</td><td>New York Times and an experiment</td><td>Utilitarian and hedonic</td><td>Books</td><td>na</td><td>Yes</td></tr><tr><td>2011</td><td>Amblee and BuiInternational Journal of Electronic Commerce</td><td>Volume and valence</td><td>Amazon</td><td>Utilitarian and hedonic</td><td>Books</td><td>Yes</td><td>No</td></tr><tr><td>2009</td><td>Ye, Law, and GuInternational Journal of Hospitality Management</td><td>Valence</td><td>Ctrip</td><td>Utilitarian and hedonic</td><td>Hotels</td><td>na</td><td>Yes</td></tr><tr><td>2006</td><td>LiuJournal of Marketing</td><td>Volume and valence</td><td>Yahoo!</td><td>Hedonic</td><td>Movies</td><td>Yes</td><td>No</td></tr><tr><td>2007</td><td>Dellarocas, Zhang, and AwadJournal of Interactive Marketing</td><td>Volume and valence</td><td>Yahoo!, BoxOfficeMojo, and the Hollywood Reporter</td><td>Hedonic</td><td>Movies</td><td>Yes</td><td>Yes</td></tr><tr><td>2008</td><td>Duan, Gu, and WhinstonDecision Support Systems</td><td>Volume and valence</td><td>Yahoo!</td><td>Hedonic</td><td>Movies</td><td>Yes</td><td>No</td></tr><tr><td>2012</td><td>Yang, Kim, Amblee, and JeongEuropean Journal of Marketing</td><td>Volume and valence</td><td>Korean Film Council</td><td>Hedonic</td><td>Movies</td><td>Yes</td><td>Yes for non-mainstream movies, but no for mainstream movies</td></tr><tr><td>2010</td><td>Chintagunta, Gopinath, and VenkataramanMarketing Science</td><td>Volume and valence</td><td>Yahoo! and ACNielsen</td><td>Hedonic</td><td>Movies</td><td>Yes</td><td>Yes</td></tr><tr><td>2012</td><td>Cui, Lui, and GuoInternational Journal of Electronic Commerce</td><td>Volume and valence</td><td>Amazon</td><td>Utilitarian and hedonic</td><td>Computer electronics and video games</td><td>Yes for experience products</td><td>Yes for search products</td></tr><tr><td>2009</td><td>Duan, Gu, and WhinstonMIS Quarterly</td><td>Valence</td><td>CNET</td><td>Utilitarian</td><td>Software</td><td>na</td><td>Yes for non-popular software, but no for popular software</td></tr><tr><td>2016</td><td>Zhou and Duan, Journal of Management Information Systems</td><td>Volume and valence</td><td>CNET</td><td>Utilitarian</td><td>Software</td><td>Yes</td><td>Yes (but marginally)</td></tr><tr><td>2014</td><td>Zhang, Zhao, Cheung, and LeeDecision Support Systems</td><td>Volume and valence</td><td>Dianping</td><td>Utilitarian and hedonic</td><td>Unknown</td><td>Yes</td><td>Yes</td></tr></table>

Table 1. Exemplar findings from the online review literature.  
Note: na indicates findings are not available.

For example, for unknown books, negative New York Times reviews can attract awareness and, as a result, increase sales (Berger, Sorensen, & Rasmussen, 2010). Also, when the reviewer clearly outlines pros and cons and thereby provides su<sup>fi</sup>cient information to the customer, a negative review can increase sales (Ghose & Ipeirotis, 2011).

## 2.3. Online review volume

Other research has focused on online review volume. This is measured by counting the number of online reviews that are submitted to online review systems for particular products. The <sup>fi</sup>ndings have been more consistent than those of studies considering valence. For example, it is widely acknowledged in studies of movie box o<sup>fi</sup>ce performance that online review volume explains most of the variance in sales (Chintagunta, Gopinath, & Venkataraman, 2010; Dellarocas et al., 2007; Duan et al., 2008; Liu, 2006; Yang, Kim, Amblee, & Jeong, 2012). However, this does not generalise to all products. For example, online review volume does not a<sup>f</sup>ect the sales of computer electronics (Cui, Lui, & Guo, 2012).

## 2.4. Attribute substitution

Much of the literature related to online reviews has assumed that consumers are making deliberate, rational decisions. However, recent work in IS has postulated that consumers often make fast, intuitive decisions in response to the characteristics of reviews (Liu & Karahanna, 2017; Wang, Zhang, & Hann, forthcoming). Liu and Karahanna suggested that consumers construct their attribute preferences in response to the language in reviews. Their work is rooted in an in<sup>fl</sup>uential cognitive science project on heuristics that are part of fast decision-making processes and their associated biases (Gilovich, Gri<sup>fi</sup>n, & Kahneman, 2002; Kahneman, 2003; Kahneman & Egan, 2011; Kahneman & Frederick, 2004; Tversky & Kahneman, 1974). This work has attracted the attention of scholars in marketing, who have become interested in choice architectures (Goldstein, Johnson, Herrmann, & Heitmann, 2008; Johnson et al., 2012). Choice architectures are the structures that display information to be used at the time of a decision. They can be manipulated to nudge consumers towards certain behaviours (Thaler & Sunstein, 2008). All online review systems have a choice architecture, and this will a<sup>f</sup>ect consumer’s decision-making. Because such systems can a<sup>f</sup>ect economic behaviour, scholars in IS are actively studying what aspects of choice architecture, and, in particular, which characteristics of online reviews, a<sup>f</sup>ect decision-making.

According to the theory of attribute substitution, one or more target attributes will aid decision-making. For example, when buying a movie, the target attribute may be ‘how engrossing it will be’, while when buying a refrigerator, the target attribute may be ‘its product lifespan’. Target attributes may be inaccessible, so instead, a di<sup>f</sup>erent (accessible) attribute, called a heuristic attribute, will be substituted. The decision is then e<sup>f</sup>ectively and quickly made, without deliberation, on the basis of the accessible attribute (Kahneman & Frederick, 2004). A more deliberate, rational process may re-evaluate the decision, but it will be anchored by the initial fast decision. Which heuristic attributes come to mind can be a<sup>f</sup>ected by the nature of the task. For example, di<sup>f</sup>erent heuristic attributes may come to mind for a movie and a refrigerator.

Therefore, when shopping for a product, target attributes can di<sup>f</sup>er for di<sup>f</sup>erent target objects. Shopping for di<sup>f</sup>erent products involves the use of di<sup>f</sup>erent criteria (Babin et al., 1994; Chiu et al., 2014; Dhar & Wertenbroch, 2000). This mechanism may help explain why past studies of online reviews have mixed <sup>fi</sup>ndings.

## 2.5. The hedonic or utilitarian dimension of product type as a moderator

Assuming attribute substitution as an explanatory mechanism, we focus on the hedonic/utilitarian distinction (Babin et al., 1994; Childers, Carr, Peck, & Carson, 2001; Dhar & Wertenbroch, 2000). While the de<sup>fi</sup>nitions of hedonic versus utilitarian products vary slightly, previous studies agree that hedonic products satisfy people’s emotional wants and involve aesthetic and sensual pleasure and fantasy. These products relate more to fun and playfulness (Babin et al., 1994; Hirschman & Holbrook, 1982). Typical hedonic products include music albums, movies and novels. However, complex products may exhibit both dimensions. For example, hotels may be evaluated on utilitarian attributes such as safety and cleanness and on hedonic attributes related to pleasure and entertainment.

It is commonly agreed that purely utilitarian products are evaluated based on utility (Drolet, Simonson, & Tversky, 2000; Sen & Lerman, 2007). Consumers strive to maximise practical criteria when they search for these products (Strahilevitz & Myers, 1998). For utilitarian products, shopping is considered a kind of work (Babin et al., 1994) in which consumers seek convenience, broad product o<sup>f</sup>erings, detailed product speci<sup>fi</sup>cations, and monetary savings (Chiu et al., 2014).

The target attribute that will guide decisions about hedonic products will relate to engagement or emotion, while the target attribute for utilitarian products will relate to utility or functionality. Emotional cues or utility-based cues are more likely to be noticed and responded to depending on whether people are seeking hedonic or utilitarian products. Because target attributes are hard to evaluate (it is hard to know in advance if a movie will be engrossing or a refrigerator will last 10 years) consumers are likely to substitute more accessible heuristic attributes, such as the valence, volume and arousal of online reviews. The product characteristic (hedonic or utilitarian) can prime consumers to focus on di<sup>f</sup>erent characteristics of online reviews.

Online review valence is perceived to represent the quality of products (Wu & Gaytán, 2013). Negative reviews suggest low quality and positive reviews suggest high quality (Ye et al., 2009). The valence of online reviews is connected to product utility rather than emotions. For utilitarian products, evaluations are generally objective and fact-based. In contrast, evaluations of hedonic products are generally emotional, subjective and personal (e.g. Dhar & Wertenbroch, 2000). Consumers may ascribe the valence of online reviews of these products to the reviewers’ characteristics rather than the products characteristics. For hedonic products, readers of negative reviews are more likely to attribute negative opinions to the reviewer than to product quality. The opposite is the case for utilitarian products (Sen & Lerman, 2007). When selecting utilitarian products, consumers are more likely to use valence as a heuristic attribute. When facing hedonic products, consumers may be less likely to use valence as a heuristic attribute. This suggests the valence hypothesis:

H1. The hedonic/utilitarian product type moderates the efect of online review valence on sales. Online review valence is more likely to afect purchase decisions for utilitarian products than for hedonic products.

Online review volume may provide a signal of overall worth, or it may suggest social in<sup>fl</sup>uence and trigger social desirability bias, thereby driving purchase behaviour. A large number of reviews may increase the visibility of the product, and a high quantity of reviews may make a product more socially desirable (Duan et al., 2008). Therefore, online review volume may be a better indicator of emotions, such as desirability or controversy, than of quality. When selecting hedonic products, people focus on heuristic attributes that are related to emotion. Therefore, online review volume may have a greater in<sup>fl</sup>uence on purchase decisions related to hedonic products than to utilitarian products.

High volume negative reviews may also drive consumption. For example, Berger et al. (2010) showed that negative reviews have increased sales for books by unknown authors. Ghose and Ipeirotis (2011), drawing on text-mining analyses, found that when the review text was informative and detailed, products with negative online reviews were associated with increased sales. Thelwall, Buckley, and Paltoglou (2011) asserted that popular events on Twitter are typically associated with increases in negative valence strength. Another example comes from the music video Gentleman, by Psy, which has overwhelming negative reviews but hundreds of millions of views, and correspondingly high song purchases. Online review volume may not be a good indicator of the quality of utilitarian products because it might just be correlated with controversy. This leads to the volume hypothesis:

H2. The hedonic/utilitarian product type moderates the efect of online review volume on sales. Online review volume is more likely to afect purchase decisions for hedonic products than for utilitarian products.

## 2.6. Online review arousal

Arousal is de<sup>fi</sup>ned as the level of emotionality expressed in texts (e.g. Warriner, Kuperman, & Brysbaert, 2013). Most studies of online review sentiment focus on valence. However, reviews with the same valence can have di<sup>f</sup>erent levels of emotionality, according to the two-dimensional theory of a<sup>f</sup>ect (Russell, 1979, 1980, 2003). A<sup>f</sup>ect has been the subject of previous IS studies (Zhang, 2013). In particular, a<sup>f</sup>ect has been shown to in<sup>fl</sup>uence the early perception, adoption and continuous usage of IS (Beaudry & Pinsonneault, 2010; Park & Lee, 2009). A<sup>f</sup>ect has also been studied in the context of online shopping (Pengnate & Delen, 2014; Yin, Bond, & Zhang, 2014). Building on this literature, our work focuses on arousal in reviews.

A one-star review can be written in a more or less passionate way – “I am angry” versus “I am annoyed”. The valence will be the same, but the arousal that consumers feel reading these review texts will be di<sup>f</sup>erent: high arousal in relation to the former and low arousal in relation to the latter (Heilman, 1997; Russell, 1980).

High arousal words are emotional cues in online reviews. They can be related to emotions and decrease the perceptual accessibility of other thoughts, including the utility level of the product. Arousal may function as a heuristic attribute to help judge if a hedonic product will be entertaining. For example, when faced with negative emotional reviews such as “OMG, this video is so stupid!”, consumers may still want to listen to controversial popular songs by Rebecca Black or Justin Bieber (Grant, 2011). In contrast, consumers may not be sensitive to online review arousal when making purchase decisions about utilitarian products. For example, arousal might not be a good heuristic attribute in judging a product like a refrigerator while consumers have the target attribute of utility in mind. This leads to the arousal hypothesis:

H3. The hedonic/utilitarian product type moderates the efect of online review arousal on sales. Online review arousal is more likely to positively afect purchase decisions for hedonic products than for utilitarian products.

However, the e<sup>f</sup>ect of H3 may be di<sup>f</sup>erent for positive and negative reviews. People are risk averse in general – that is why negative information is quite attention-grabbing. People are wired to react to negativity (Rozin & Royzman, 2001). Even though high arousal review texts can suggest excitement and can satisfy people’s emotional wants, negative high arousal reviews may suggest more risks than positive arousal review texts. It follows that people’s purchase impulsiveness, which is ampli<sup>fi</sup>ed by reading high arousal reviews, may be inhibited more by negative reviews than by positive reviews.

While most previous literature treats valence and arousal as independent (Russell, 1979, 1980, 2003), some studies have shown that valence can in<sup>fl</sup>uence how arousal a<sup>f</sup>ects people’s decisions (e.g. Simola, Le Fevre, Torniainen, & Baccino, 2015). Accordingly, we conjecture the interaction e<sup>f</sup>ect between online review arousal and product type can also be a<sup>f</sup>ected by online review valence. That is, we propose that H3 holds more strongly for positive reviews than for negative reviews.

H4. Online review arousal is more likely to positively afect purchase decisions for hedonic products than for utilitarian products, and this efect is more apparent for positive reviews than for negative reviews.

In sum, online review valence is more likely to be used as a heuristic attribute for utilitarian products. In contrast, online review volume and arousal are more likely to be used as heuristic attributes for hedonic products (Table 2).

## 3. Method and results

To test the hypotheses, we conducted two studies. In Study 1, we used an OLS <sup>fi</sup>xed e<sup>f</sup>ects model to test Amazon panel data (e.g. Hsiao, 1986). After conducting Hausman tests to determine which model (<sup>fi</sup>xed or random e<sup>f</sup>ects) was appropriate, we adopted a <sup>fi</sup>xed e<sup>f</sup>ects model that allows for product heterogeneity and time di<sup>f</sup>erence. This model mostly suggests correlations between variables. However, in online review systems, online reviews may in<sup>fl</sup>uence purchase behaviours, and, after purchases, consumers may write reviews. Therefore, there may be a causality loop between online reviews and sales. To better understand how online reviews a<sup>f</sup>ect sales, we conducted a series of follow-up Granger causality tests with pooled time series data to check the robustness of our <sup>fi</sup>xed e<sup>f</sup>ects estimation <sup>fi</sup>ndings. In Study 2, we conducted an online experiment to better understand causality.

Online review characteristics that a<sup>f</sup>ect purchase <sup>Table 2.</sup>decisions for di<sup>f</sup>erent products.

<table><tr><td>Products (target objects)</td><td>Goals (target attributes)</td><td>Related online review characteristics (heuristic attributes)</td></tr><tr><td>Utilitarian</td><td>Utility</td><td>Valence</td></tr><tr><td>Hedonic</td><td>Emotion</td><td>Volume</td></tr><tr><td>Hedonic</td><td>Emotion</td><td>Arousal</td></tr></table>

## 4. Study 1: Amazon panel data

We collected panel data on 26,357 hedonic and utilitarian Amazon products daily for 34 days from June 25 2015 to July 28 2015.

Product type (utilitarian or hedonic) can be understood in di<sup>f</sup>erent ways. It can be understood as a binary variable or as a continuous variable with a single axis. Some researchers view it as a pair of dimensions (Babin et al., 1994; Kushwaha & Shankar, 2013). According to that interpretation, products can have both hedonic and utilitarian aspects, which can be scored along di<sup>f</sup>erent axes. Complex products, such as hotels, have both hedonic and utilitarian aspects. This may be in part because hotels combine multiple products: spas are hedonic, while business centres are utilitarian.

For the purposes of this study, to more clearly observe the di<sup>f</sup>erent e<sup>f</sup>ects of hedonic and utilitarian products, we purposely chose simple rather than compound products. We chose products that were located at the extremes of the continuum of hedonic/utilitarian products. For example, a calculator is at the utilitarian end of the continuum: customers choose to purchase a calculator more for its utility (its ability to accurately calculate), than its aesthetic value (the artistic design of the calculator). In this way, we treated the product type (utilitarian or hedonic) as binary.

Previous literature has discussed typical utilitarian and hedonic products (listed in Table 3) (Dhar & Wertenbroch, 2000; Hirschman & Holbrook, 1982; Khan, Dhar, & Wertenbroch, 2004; Strahilevitz & Myers, 1998). We used keywords to search for hedonic and utilitarian products within each relevant Amazon product category. For example, we used “<sup>fi</sup>ction novels” as keywords to search within the Amazon category of “Science Fiction & Fantasy” for science <sup>fi</sup>ction novels (hedonic products) and then collected data. We collected data from 15 product categories (e.g. Dhar & Wertenbroch, 2000): novels (Kindle), video games, entertainment novels, science <sup>fi</sup>ction novels, chemistry textbooks (Kindle), physics textbooks (Kindle), mathematics textbooks (Kindle), o<sup>fi</sup>ce furniture, o<sup>fi</sup>ce products, air conditioners, chemistry books, physics books, mathematics books, refrigerators, and computers.

Product categories in the sample.

<table><tr><td>Product type</td><td>Amazon category</td><td>Keywords</td><td>Product category</td><td>Proportion in the sample</td></tr><tr><td rowspan="5">Hedonic (Dhar &amp; Wertenbroch, 2000; Khan et al., 2004)</td><td>Kindle ebooks</td><td>Fiction novels</td><td>Novels (Kindle)</td><td>9.09%</td></tr><tr><td>xBox 360 games</td><td>Video games</td><td>Video games</td><td>11.29%</td></tr><tr><td>Humour and entertainment</td><td>Fiction novels</td><td>Entertainment novels</td><td>4.89%</td></tr><tr><td>Romance</td><td>Fiction novels</td><td></td><td></td></tr><tr><td>Science fiction and Fantasy Science</td><td>Fiction novels</td><td>Science fiction novels</td><td>5.66%</td></tr><tr><td rowspan="12">Utilitarian (Dhar &amp; Wertenbroch, 2000; Hirschman &amp; Holbrook, 1982; Strahilevitz &amp; Myers, 1998)</td><td>Kindle ebooks</td><td>Chemistry books</td><td>Chemistry textbooks (Kindle)</td><td>0.34%</td></tr><tr><td>Kindle ebooks</td><td>Physics books</td><td>Physics textbooks (Kindle)</td><td>0.45%</td></tr><tr><td>Kindle ebooks</td><td>Mathematics books</td><td>Mathematics textbooks (Kindle)</td><td>1.12%</td></tr><tr><td>Office furniture and lighting</td><td>Furniture</td><td>Office furniture</td><td>11.47%</td></tr><tr><td>Office products</td><td>Calculators Printers</td><td>Office products</td><td>21.64%</td></tr><tr><td>Tools and home improvement</td><td>Air conditioners</td><td>Air conditioners</td><td>8.75%</td></tr><tr><td>General chemistry</td><td>Chemistry books</td><td>Chemistry books</td><td>2.61%</td></tr><tr><td>Physics</td><td>Physics book</td><td>Physics books</td><td>3.99%</td></tr><tr><td>Mathematics</td><td>Mathematics books</td><td>Mathematics books</td><td>3.97%</td></tr><tr><td>Refrigerators</td><td>Fridges</td><td>Refrigerators</td><td>1.08%</td></tr><tr><td>Computers</td><td>Computers</td><td>Computers</td><td>13.64%</td></tr><tr><td>Total</td><td></td><td></td><td>100%</td></tr></table>

We (1) randomly selected products within each product category for long-term observation and (2) ensured the number of products in each product category was proportional to all products within that category at the time of data collection. Table 3 shows the proportions of the di<sup>f</sup>erent product categories. The resulting sample contained more utilitarian products than hedonic products and therefore was not balanced. To eliminate the e<sup>f</sup>ect of the imbalance, we added a robustness test to randomly select 50% of the utilitarian products. The remaining utilitarian and hedonic products were almost equal in the number of observations. We repeated the regression of Model 2 in Table 8 and reported the results in the Appendix (Table A1). The pattern in the results was consistent with the results of Model 2 presented in Table 8.

For each product, cumulative data were collected each day, including product name, product category, sales rank, purchase price, number of online reviews, average star rating, and the most recent review texts. Users may have used the website of Amazon or the mobile application of Amazon to post these reviews; we do not have data on the device used. If a product had accumulated more than 100 reviews, we collected the most recent 100. If not, we collected all review texts for this product. Less than 15% of products from our dataset had more than 100 reviews.

We used the average star rating as the measure of valence (Duan, Gu, & Whinston, 2009; Mudambi & Schu<sup>f</sup>, 2010). This is the standard method for measuring online review valence. Compared with the average star rating, the distribution of star ratings may not be a direct indicator of product quality. When facing hedonic or utilitarian products, the distribution of online reviews may not be a direct measure of emotions or utility. Rather, online review distribution may be a weight that moderates the measure of emotions or utility. It may represent the extent to which a consumer consensus has been reached regarding whether the product is emotionally satisfying or whether the product is useful. Therefore, the e<sup>f</sup>ect of rating distribution may not di<sup>f</sup>er between utilitarian and hedonic products.

We used the number of reviews to measure volume (Dellarocas et al., 2007; Duan et al., 2008). We calculated arousal scores through automated parsing of individual online review texts. An arousal score for a review text was calculated by summing up the arousal weights of emotional words identi<sup>fi</sup>ed in the dictionary by Warriner et al. (2013) and dividing by the review text length. The most recent reviews, up to 100, were averaged. Tables 4, 5 and 6 provides descriptive statistics for all products, for utilitarian products and for hedonic products, respectively.

We used sales rank as the measure of purchase decision. Sales rank was calculated by Amazon within each product category. We standardised sales rank across all product categories. Note that the higher the standardised sales rank, the lower the sales. Because the distribution of online review volume was highly skewed, we also conducted a log transformation on this variable. Because product price may a<sup>f</sup>ect purchase decisions and was also highly skewed, we log-transformed it and controlled for it in our analysis (Dawar & Parker, 1994). To increase reliability, we also excluded products with online review volume below two because such low volumes provide few useful signals for consumers.

Descriptive statistics (all products).

<table><tr><td></td><td>Mean</td><td>Median</td><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Sales rank (across all product categories)</td><td>333,500.1</td><td>5989</td><td>826,648</td><td>1</td><td>15,100,000</td></tr><tr><td>Product purchase price</td><td>125.4522</td><td>30.95</td><td>313.9852</td><td>0</td><td>9939</td></tr><tr><td>Online review valence</td><td>4.071141</td><td>4.2</td><td>.817346</td><td>1</td><td>5</td></tr><tr><td>Online review volume</td><td>95.28218</td><td>12</td><td>353.5044</td><td>1</td><td>14,077</td></tr><tr><td>Online review arousal</td><td>1.165429</td><td>1.15</td><td>0.3108056</td><td>0</td><td>6.05</td></tr></table>

Descriptive statistics (hedonic products only).

<table><tr><td></td><td>Mean</td><td>Median</td><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Sales rank (across all product categories)</td><td>578,114.3</td><td>90,367</td><td>104,2340</td><td>2</td><td>12,500,000</td></tr><tr><td>Product purchase price</td><td>25.58692</td><td>15.14</td><td>35.44308</td><td>0.01</td><td>799.99</td></tr><tr><td>Online review valence</td><td>4.059311</td><td>4.2</td><td>0.7995615</td><td>1</td><td>5</td></tr><tr><td>Online review volume</td><td>107.9644</td><td>16</td><td>455.6683</td><td>1</td><td>14,077</td></tr><tr><td>Online review arousal</td><td>1.17467</td><td>1.17</td><td>.2716725</td><td>0</td><td>4.15</td></tr></table>

Descriptive statistics (utilitarian products only).

<table><tr><td></td><td>Mean</td><td>Median</td><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Sales rank (across all product categories)</td><td>333,500.1</td><td>5989</td><td>826,648</td><td>1</td><td>15,100,000</td></tr><tr><td>Product purchase price</td><td>125.4522</td><td>30.95</td><td>313.9852</td><td>0</td><td>9939</td></tr><tr><td>Online review valence</td><td>4.071141</td><td>4.2</td><td>.817346</td><td>1</td><td>5</td></tr><tr><td>Online review volume</td><td>95.28218</td><td>12</td><td>353.5044</td><td>1</td><td>14,077</td></tr><tr><td>Online review arousal</td><td>1.165429</td><td>1.15</td><td>.3108056</td><td>0</td><td>6.05</td></tr></table>

## 5. Study 1: Amazon results

For the panel data analysis, we used OLS <sup>fi</sup>xed e<sup>f</sup>ects models (Table 8; Wul<sup>f</sup>, Hills, & Hertwig, 2014). To illustrate the regression models, we speci<sup>fi</sup>ed a mathematical equation to represent Model 1 in Table 8. The remaining models included the interactions of particular variables in Model 1 (Equation 1):

$$
\begin{array}{c} S _ {i t} = \beta_ {1} \ln (\mathrm{PP}) _ {i t} + \beta_ {2} V _ {i t} + \beta_ {3} \ln (\mathrm{ORV}) _ {i t} + \beta_ {4} A _ {i t} \\ + \beta_ {5} \mathrm{PT} _ {i} + \alpha_ {t} \end{array}\tag{1}
$$

Variable i measured product, t measured day, $S _ { i t }$ measured standardised sales rank, ln $\left( \mathrm { P P } \right) _ { i t }$ measured purchase price, $V _ { i t }$ measured review valence, ln $( \mathrm { O R V } ) _ { i t }$ measured review volume, $A _ { i t }$ measured review arousal, and $P T _ { i }$ measured product type (1 represents utilitarian and 0 represents hedonic).

Before using the variables in the four models in Table 8, we ran correlation tests (Table 7). We also ran a collinearity diagnosis for these variables. The correlation coe<sup>fi</sup>cients were very low and variance in<sup>fl</sup>ation factors (VIF) for all variables was below 2. Therefore, there was no indication of multi-collinearity and these variables could be included in the models (O’Brien, 2007).

All models demonstrated that the purchase price, a control variable, positively a<sup>f</sup>ected the standardised sales rank (i.e. negatively a<sup>f</sup>ected sales). Controlling for the control variable and the interaction terms across the four models, valence, volume, and arousal all negatively a<sup>f</sup>ected the standardised sales rank (i.e. positively a<sup>f</sup>ected sales).

In Model 2, the interaction e<sup>f</sup>ects of the three online review characteristics and product type were signi<sup>fi</sup>cant. The coe<sup>fi</sup>cients of these interactions were opposed: arousal and volume had a greater e<sup>f</sup>ect on sales for hedonic products, while valence had a greater e<sup>f</sup>ect on sales for utilitarian products.

Correlations among variables.

<table><tr><td></td><td>Arousal</td><td>Ln (online review volume)</td><td>Ln (product price)</td><td>Product type</td></tr><tr><td>Valence</td><td>0.095 [***]</td><td>0.041 [***]</td><td>-0.081 [***]</td><td>-0.005 [***]</td></tr><tr><td>Arousal</td><td></td><td>0.058 [***]</td><td>-0.042 [***]</td><td>-0.059 [***]</td></tr><tr><td>Ln (online review volume)</td><td></td><td></td><td>-0.12 [***]</td><td>-0.13 [***]</td></tr><tr><td>Ln (product price)</td><td></td><td></td><td></td><td>0.33 [***]</td></tr></table>

Note: $^ { \ast \ast \ast } p < 0 . 0 0 1 ;$ ; product type was coded as 1 for utilitarian products and 0 for hedonic products.

In Model 3, we included the interactions between every two characteristics of online reviews (valence and arousal, valence and volume, or arousal and volume) and the interactions among the three. We found that the e<sup>f</sup>ect of arousal on sales depended on the level of valence $( p < 0 . 0 0 1 )$ . In addition, when these interaction variables were considered, product type still moderated the e<sup>f</sup>ect of valence, volume, and arousal on sales.

In Model 4, we added the interaction between price and either characteristic of online reviews (price and valence, or price and volume, or price and arousal). The coe<sup>fi</sup>cient of the interaction between price and valence was positive and signi<sup>fi</sup>cantly a<sup>f</sup>ected sales rank (0.015, $\textstyle P \ < \ 0 . 0 0 1 )$ This suggests that valence a<sup>f</sup>ects sales more for expensive products than for cheap products. The coe<sup>fi</sup>cients of the interaction between price and volume and between price and arousal were negative and signi<sup>fi</sup>cantly a<sup>f</sup>ected sales rank (−0.01, $P ~ < ~ 0 . 0 0 1 ; ~ - 0 . 0 4 3 , ~ p ~ < ~ 0 . 0 0 1 )$ ). This suggests that arousal or volume a<sup>f</sup>ects sales more for inexpensive products than for expensive products. In relation to these new interactions, the <sup>fi</sup>ndings from Model 3 still held.

To test H4, we added the interaction of product type, online review valence and online review arousal (Model 5) to Model 2 in Table 8. The results showed that the coe<sup>fi</sup>cient of such three-way interaction was not signi<sup>fi</sup>cant (0.002, p > 0.1). However, the other results in this model were consistent with those in Models 2–4. This suggests that online review arousal has a greater e<sup>f</sup>ect on sales for hedonic products and this e<sup>f</sup>ect does not di<sup>f</sup>er between positive reviews and negative reviews. Therefore, H4 was not supported.

These <sup>fi</sup>xed e<sup>f</sup>ects models mainly resulted from observation. To further understand causality between the variables, we conducted a series of Granger causality tests (see below). To run these tests, we followed Baum’s (2006) method and computed means for each cross section over time. This created a new dataset with one observation per time point, including the cumulative average number of reviews, the cumulative average star ratings (valence) and the cumulative average arousal level extracted from review texts. Before conducting Granger causality tests, we used a Dickey–Fuller test for unit root to test the stationarity of the time series data. Because the p value was below 0.05, we concluded the data were stationary. To determine the suitable number of time lags for Granger causality tests, we conducted VAR and VEC diagnoses. Both diagnoses (see Table 9) showed that 6 was the appropriate time lag for the arousal model (Model 3) and 1 was the appropriate time lag for the volume and valence models (Models 1 and 2).

Granger causality tests showed that in this dataset, sales did not lead back to the three characteristics of online reviews. Therefore, the <sup>fi</sup>xed e<sup>f</sup>ects estimation may imply that (1) the three review characteristics caused sales and (2) product type moderated how they caused sales.

To further test H1–H3 that seem to be supported in Table 8, we ran <sup>fi</sup>xed e<sup>f</sup>ects models for hedonic and utilitarian products (Table 10). Because VIF was below 2, we included ln (product price) as a control variable and the three online review characteristics as independent variables in these two models. Table 10 shows that the coe<sup>fi</sup>cient for valence was signi<sup>fi</sup>cant in both the Hedonic Model and the Utilitarian Model. However, the signi<sup>fi</sup>cant negative coe<sup>fi</sup>cient in the Utilitarian Model was smaller than that in the Hedonic Model (−0.054; −0.025). A 1% increase in valence (average ratings) led to a 0.054% decrease in standardised sales rank for utilitarian products but to a 0.025% decrease in standardised sales rank for hedonic products. This suggests that valence positively a<sup>f</sup>ects product sales more for utilitarian products. This result, combined with the signi<sup>fi</sup>cant interaction e<sup>f</sup>ect between product type and valence (Table 8), supports H1.

Fixed e<sup>f</sup>ects estimation.

<table><tr><td>Variables</td><td>Model 1 coefficient (std. err.)</td><td>Model 2 coefficient (std. err.)</td><td>Model 3 coefficient (std. err.)</td><td>Model 4 coefficient (std. err.)</td><td>Model 5 coefficient (std. err.)</td></tr><tr><td>Ln (purchase price)</td><td>0.028 (0.0006) [***]</td><td>0.03 (0.0006) [***]</td><td>0.03 (0.0006) [***]</td><td>0.05 (0.0043) [***]</td><td>0.029 (0.0006) [***]</td></tr><tr><td>Valence</td><td>-0.047 (0.0012) [***]</td><td>-0.021 (0.0026) [***]</td><td>-0.075 (0.0096) [***]</td><td>-0.112 (0.0099) [***]</td><td>-0.021 (0.026) [***]</td></tr><tr><td>Ln (online review volume)</td><td>-0.065 (0.0005) [***]</td><td>-0.19 (0.0009) [***]</td><td>-0.234 (0.025) [***]</td><td>-0.19 (0.0246) [***]</td><td>-0.19 (0.0009) [***]</td></tr><tr><td>Arousal</td><td>-0.055 (0.036) [***]</td><td>-0.23 (0.0087) [***]</td><td>-0.43 (0.036) [***]</td><td>-0.26 (0.0369) [***]</td><td>-0.23 (0.0087) [***]</td></tr><tr><td>Product type</td><td>0.224 (0.002) [***]</td><td>-0.49 (0.0163) [***]</td><td>-0.524 (0.017) [***]</td><td>-0.524 (0.017) [***]</td><td>-0.479 (0.029) [***]</td></tr><tr><td>Product type × valence</td><td></td><td>-0.034 (0.0029) [***]</td><td>-0.03 (0.003) [***]</td><td>-0.05 (0.003) [***]</td><td>-0.037 (0.0063) [***]</td></tr><tr><td>Product type × ln (online review volume)</td><td></td><td>0.161 (0.001) [***]</td><td>0.162 (0.0011) [***]</td><td>0.174 (0.0012) [***]</td><td>0.161 (0.001) [***]</td></tr><tr><td>Product type × arousal</td><td></td><td>0.245 (0.009) [***]</td><td>0.256 (0.0097) [***]</td><td>0.282 (0.01) [***]</td><td>0.236 (0.023) [***]</td></tr><tr><td>Product type × arousal × valence</td><td></td><td></td><td></td><td></td><td>0.002 (0.005)</td></tr><tr><td>Valence × ln (online review volume)</td><td></td><td></td><td>0.0054 (0.0057)</td><td>0.0021 (0.006)</td><td></td></tr><tr><td>Arousal × ln (online review volume)</td><td></td><td></td><td>0.022 (0.021)</td><td>0.004 (0.021)</td><td></td></tr><tr><td>Valence × arousal</td><td></td><td></td><td>0.0368 (0.008) [***]</td><td>0.03 (0.008) [***]</td><td></td></tr><tr><td>Valence × arousal × ln (online review volume)</td><td></td><td></td><td>-0.0012 (0.0049)</td><td>0.0018 (0.0049)</td><td></td></tr><tr><td>Ln purchase price) × valence</td><td></td><td></td><td></td><td>0.015 (0.0008) [***]</td><td></td></tr><tr><td>Ln (purchase price) × ln (online review volume)</td><td></td><td></td><td></td><td>-0.01 (0.0004) [***]</td><td></td></tr><tr><td>Ln (purchase price) × arousal</td><td></td><td></td><td></td><td>-0.043 (0.003) [***]</td><td></td></tr><tr><td>R squared</td><td>0.117</td><td>0.169</td><td>0.169</td><td>0.172</td><td>0.170</td></tr></table>

Note: DV is standardised sales rank in its descending order; the higher the DV, the lower the sales; \*\*\* p < 0.001; online review volume > 1; product type is coded as 1 for utilitarian products and 0 for hedonic products; time dummies (<sup>fi</sup>xed e<sup>f</sup>ect for each day) used in estimating the model are not reported.

Results for Granger causality Wald tests.

<table><tr><td>Model #</td><td>Models</td><td>Chi-square</td><td>AIC</td></tr><tr><td>1</td><td> $\text{Valence}(t) = \sum_{j=1}^{p} A_{11j} \text{Sales}(t-j) + \sum_{j=1}^{p} A_{12j} \text{Valence}(t-j) + E_1(t)$ </td><td>2.44</td><td>-11</td></tr><tr><td>2</td><td> $\text{Volume}(t) = \sum_{j=1}^{p} A_{21j} \text{Sales}(t-j) + \sum_{j=1}^{p} A_{22j} \text{Volume}(t-j) + E_2(t)$ </td><td>0.05</td><td>-2.36</td></tr><tr><td>3</td><td> $\text{Arousal}(t) = \sum_{j=1}^{p} A_{31j} \text{Sales}(t-j) + \sum_{j=1}^{p} A_{32j} \text{Arousal}(t-j) + E_3(t)$ </td><td>4.95</td><td>-12.7</td></tr></table>

Note: Sales indicates product sales; valence indicates online review valence; volume indicates online review volume; arousal indicates online review arousal; and p indicates the <sup>fi</sup>tting number of time lags.

Fixed e<sup>f</sup>ects estimation.

<table><tr><td></td><td>Hedonic coefficient (std. err.)</td><td>Utilitarian coefficient (std. err.)</td></tr><tr><td>Ln (purchase price)</td><td>-0.024 (0.002) [***]</td><td>0.035 (0.0006) [***]</td></tr><tr><td>Valence</td><td>-0.025 (0.003) [***]</td><td>-0.054 (0.0013) [***]</td></tr><tr><td>Ln (online review volume)</td><td>-0.19 (0.001) [***]</td><td>-0.028 (0.0005) [***]</td></tr><tr><td>Arousal</td><td>-0.2 (0.0091) [***]</td><td>0.016 (0.004) [***]</td></tr><tr><td>R squared</td><td>0.3</td><td>0.03</td></tr></table>

Note: DV indicates standardised sales rank in descending order – the higher the DV, the lower the sales; $^ { * * * } p < 0 . 0 0 1 ;$ ; online review volume $> 1 ;$ product type is coded as 1 for utilitarian products and 0 for hedonic products; time dummies (<sup>fi</sup>xed e<sup>f</sup>ect for each day) used in estimating the model are not reported.

The coe<sup>fi</sup>cient for ln (online review volume) was signi<sup>fi</sup>cant in both models. The signi<sup>fi</sup>cant negative coe<sup>fi</sup>cient in the Hedonic Model was smaller than that in the Utilitarian Model (−0.19; −0.028). A 1% increase in ln (online review volume) led to a 0.19% decrease in standardised sales rank for hedonic products but to a 0.028% decrease in standardised sales rank for utilitarian products. This suggests that valence positively a<sup>f</sup>ects product sales more for hedonic products. The signi<sup>fi</sup>cant interactions between product type and ln (online review volume) (Table 8) supports H2.

The signi<sup>fi</sup>cant coe<sup>fi</sup>cient for arousal was negative in the Hedonic Model (−0.2) but not in the Utilitarian Model (0.016). This suggests that the arousal characteristic of online reviews positively a<sup>f</sup>ects sales of hedonic products but negatively a<sup>f</sup>ects sales of utilitarian products. A 1% increase in arousal led to a 0.2% decrease in standardised sales rank for hedonic products but to a 0.016% increase in standardised sales rank for utilitarian products. The signi<sup>fi</sup>cant interaction e<sup>f</sup>ect between product type and arousal supports H3.

To verify our results, we also conducted a robustness test. In the summer, as the Fall semester approaches, textbooks or o<sup>fi</sup>ce-related products can be bestsellers. We excluded products subject to this seasonal e<sup>f</sup>ect from our dataset and re-ran the test. The new results were consistent with Model 2 in Table 8. Valence was more in<sup>fl</sup>uential on sales of utilitarian products, while volume and arousal were more in<sup>fl</sup>uential on sales of hedonic products.

## 6. Study 2: online experiment

To further test the causality between variables, in Study 2 we conducted an online experiment involving 541 participants. This experiment had three parts, and these parts tested the main e<sup>f</sup>ects of the three characteristics of online reviews – valence, volume, and arousal – on hedonic and utilitarian product sales respectively. We used videos to measure participants’ real reactions to the products. We measured whether they clicked the videos and enjoyed watching the videos. Two tutorial/education-related videos were selected to represent utilitarian products and two entertainment-related videos were selected to represent hedonic products. To control for the in<sup>fl</sup>uence of product quality, for each product type, we used two videos that appeal to a general audience. These four videos all fall under a Creative Commons license for reuse, so they are suitable for experiments and publication. Tables 11 and 12 shows snapshots of the four videos and video titles that were displayed to participants in the experiment.

We used Mechanical Turk (MTurk) as the platform to collect data from participants (e.\$132#g. Ross, Irani, Silberman, Zaldivar, & Tomlinson, 2010). To measure sales, we manipulated the bonus option on MTurk. We <sup>fi</sup>rst gave each participant a bonus of \$0.2 through the bonus option and then asked, “Do you want to spend 5 cents out of the 20 cents to watch one of the videos below?” in the task (HIT). In this way, we simulated real shopping settings in which consumers have money and are ready to shop.

Videos used in the online experiment (part 1).

<table><tr><td></td><td>Utilitarian video 1</td><td>Utilitarian video 2</td></tr><tr><td>Title Snapshot</td><td>Planting Mature Plants</td><td>Introduction to DSLR Cameras</td></tr><tr><td></td><td><img src="/api/attachments/BTPSGKQB/fulltext/images/3ef1842ac566becfda8a7ee270d5437d6074404c04f9b6025df0982e7a47cab7.jpg"/></td><td><img src="/api/attachments/BTPSGKQB/fulltext/images/26ceb8acf2df64addb441c42d48b3950628f540b6a767697c3ebe6b5f3d79f53.jpg"/></td></tr></table>

Videos used in the online experiment (part 2).

<table><tr><td></td><td>Hedonic video 1</td><td>Hedonic video 2</td></tr><tr><td>Title</td><td>Frame of Mind</td><td>The Village</td></tr><tr><td>Snapshot</td><td></td><td></td></tr><tr><td></td><td><img src="/api/attachments/BTPSGKQB/fulltext/images/e423c6f594bfbefda7c74ea63ea643429d86a5c534013b74d89f4a54907f6609.jpg"/></td><td><img src="/api/attachments/BTPSGKQB/fulltext/images/995baa235b3ced7686e5a502d68ae36722fb764d9fd650ab904c82642b93a88e.jpg"/></td></tr></table>

Each of the participants was asked to <sup>fi</sup>rst compare two videos (either two hedonic videos or two utilitarian videos) and their respective titles and snapshots. In each of the sub-conditions (Tables 13–17), each video was assigned a di<sup>f</sup>erent stimulus to measure the e<sup>f</sup>ects of one of the three online review characteristics (valence, volume, and arousal). To control for the in<sup>fl</sup>uence of video content, we randomly matched videos with stimuli (Tables 13–17). For example, in sub-condition 1 of Table 13, for one participant, after the random video-stimulus matching, utilitarian video I was matched with a <sup>fi</sup>ve-star rating and utilitarian video II was matched with a one-star rating. For another participant, after the random video-stimulus matching, utilitarian video II was matched with a one-star rating and utilitarian video I was matched with a <sup>fi</sup>ve-star rating. Each of the participants was asked to purchase (click and watch) one video out of the two. Participants then provided their reasons for purchasing/not purchasing this video. They also provided their demographic information (including gender, age, and mother tongue). Participants only participated in the study once.

To measure the main e<sup>f</sup>ect of online review valence, volume or arousal on purchase behaviour for each product type, we designed an experiment with three parts based on pairwise comparisons. The dependent variable was which of the two videos participants clicked and watched. Sales were measured according to which of the two videos was clicked and watched in each sub-condition. This measure was based on MTurk workers’ actual behaviours, not their intended behaviours.

Our choice of pairwise comparisons in each subcondition was a preference evaluation method, which takes advantage of the normally skewed distribution of online participation (Salganik & Levy, 2015). Each part in the experiment was not a full factorial design. Therefore, instead of using ANOVA we conducted proportion tests to examine: (1) the main e<sup>f</sup>ects of valence, volume or arousal respectively; and (2) whether these e<sup>f</sup>ects di<sup>f</sup>er for di<sup>f</sup>erent product types (hedonic or utilitarian).

All participants were United States-based workers who had approval rates, as tabulated by Amazon, of higher than 95%. Of those workers, 39% were female and 58% were male (3% did not indicate their gender). Participants were between 19 and 71 years of age (34 years old on average), consistent with demographic results from other studies (Kittur, Chi, & Suh, 2008; Ross et al., 2010). Fifty-nine people out of 600 who initially signed up to participate said they did not plan to watch any videos. They were removed from our data pool, resulting in 541 responses. We report both the initial and <sup>fi</sup>nal number of participants in the tables.

## 7. Regarding the main e<sup>f</sup>ect of online review valence on hedonic and utilitarian product sales

In each sub-condition, one video was randomly assigned an average <sup>fi</sup>ve-star rating and the other an average one-star rating, as described above. For details, please refer to Table 13.

Experimental design regarding the main e<sup>f</sup>ect of online review valence.

<table><tr><td></td><td>Sub-condition 1</td><td>Sub-condition 2</td></tr><tr><td>Product type</td><td>Two utilitarian videos</td><td>Two hedonic videos</td></tr><tr><td>Sub-conditions</td><td>Five-star rating versus one-star rating</td><td>Five-star rating versus one-star rating</td></tr><tr><td># of MTurkers willing to participate</td><td>51 (out of 60)</td><td>50 (out of 60)</td></tr></table>

![](/api/attachments/BTPSGKQB/fulltext/images/cd7e75f7ecabb9a7eb75c6ff3ef7aa9e99ba8e99391843762ba45bd311122c09.jpg)  
The main e<sup>f</sup>ects of online review valence on video clicks and sales.Note: Error bars represent 95% con<sup>fi</sup>dence intervals.

## 8. Results

assigned to both videos. For details, please refer to Table 14.

We used one-sample proportion tests to test H1. Figure 1 indicates that participants tended to purchase the positively commented utilitarian video more frequently than the negatively commented utilitarian video (68% versus 32%; $\textstyle P < 0 . 0 5 )$ . However, participants tended to purchase the positively commented hedonic video with the same frequency as the negatively commented hedonic video (59% versus 41%; $p > 0 . 1 )$ . Therefore, H1 was supported. Some participants also explained why they chose to click on the video that received the <sup>fi</sup>ve-star rating rather than that with the one-star rating. These reasons include “Better ratings.”; “Had a higher rating”; and “The other rating was very poor. I thought I would go with the one with better rating.” These reasons suggest that participants tended to reduce risk.

## 9. Regarding the main e<sup>f</sup>ect of online review volume on hedonic and utilitarian product sales

In each review sub-condition, one video was assigned the statistic description of 1000 reviews and the other was assigned the statistic description of three reviews. We also controlled for the e<sup>f</sup>ect of online review valence. In positive valence sub-conditions, the <sup>fi</sup>vestar rating was next to both videos, while in negative valence sub-conditions, the one-star rating was

## 10. Results

We aggregated data in positive and negative valence sub-conditions (Tables 14 and 15) to test H2. After conducting one-sample proportion tests, we found that, regardless of online review valence, participants tended to purchase the hedonic video that received 1000 reviews rather than that with three reviews (61% versus 39%; $\textstyle P \ < \ 0 . 0 5 )$ . In contrast, there was no purchase di<sup>f</sup>erence for utilitarian videos with 1000 reviews versus three reviews (53% versus 47%; $p > 0 . 1 )$ . Therefore, H2 was supported (Figure 2). An example of why participants chose the video that received many reviews was “Because it has 1,000 reviews and the other only had 3”.

## 11. Regarding the main e<sup>f</sup>ect of online review arousal on hedonic and utilitarian product sales

In each positive review sub-condition, one video was assigned a most helpful, positive (<sup>fi</sup>ve-star) review that had high arousal words only and the other was assigned a most helpful, positive (<sup>fi</sup>ve-star) review that had low arousal words only (e.g. Warriner et al., 2013). In each negative review sub-condition, one video was assigned a most helpful, negative (onestar) review that had high arousal words only and the other was assigned a most helpful, negative (one-star) review that had low arousal words only. In other words, for each valence level (positive and negative), we displayed two online reviews with distinct online review arousal levels. We used high and low arousal words as measured by Warriner et al., 2013). “I LOVE this video very much!” was the high arousal positive review (arousal rating = 5.36) and “I think this video is good” (3.66) was the low arousal positive review. “This video made me very ANGRY!” (6.2) was the high arousal negative review and “This video put me to sleep” (3.6) was the low arousal negative review. Participants were assigned to see either positive reviews (high arousal or low arousal) with <sup>fi</sup>ve-star ratings or negative reviews (high arousal or low arousal) with one-star ratings. For details, please refer to Tables 16 and 17.

Experimental design regarding the main e<sup>f</sup>ect of online review volume (control variable: <sup>fi</sup>ve-star rating).

<table><tr><td></td><td>Sub-condition 1</td><td>Sub-condition 2</td></tr><tr><td>Product type</td><td>Two utilitarian videos</td><td>Two hedonic videos</td></tr><tr><td>Sub-conditions</td><td>1000 reviews versus three reviews</td><td>1000 reviews versus three reviews</td></tr><tr><td># of MTurkers willing to participate</td><td>50 (out of 60)</td><td>54 (out of 60)</td></tr></table>

Experimental design regarding the main e<sup>f</sup>ect of online review volume (control variable: one-star rating).

<table><tr><td></td><td>Sub-condition 3</td><td>Sub-condition 4</td></tr><tr><td>Product type</td><td>Two utilitarian videos</td><td>two hedonic videos</td></tr><tr><td>Sub-conditions</td><td>1000 reviews versus three reviews</td><td>1000 reviews versus three reviews</td></tr><tr><td># of MTurkers willing to participate</td><td>57 (out of 60)</td><td>53 (out of 60)</td></tr></table>

![](/api/attachments/BTPSGKQB/fulltext/images/804123863b657e5102d5ae48d4b06c5097a81f99734c818b22ffd481c94e532c.jpg)  
The main e<sup>f</sup>ects of online review volume on video clicks and sales.Note: Error bars represent 95% con<sup>fi</sup>dence intervals.

## 12. Results

Using the same method, we found that regardless of online review valence, for hedonic videos, high arousal review texts led to higher sales (64% versus 36%; $\textstyle P < 0 . 0 5 )$ . In contrast, for utilitarian videos, the arousal level in online reviews did not a<sup>f</sup>ect sales (54% versus 46%; $p > 0 . 1 )$ . Therefore, H3 was supported (Figure 3).

Participants explained why they chose the hedonic video that received the high arousal negative review. Here are some examples: “I didn’t want to be put to sleep by the other video”. “It looked cool and I didn’t want a video to put me to sleep. Putting me to sleep equals boring”. “The comment above the video was more appealing to me than the comment on the second video”. These participants’ comments suggest the pursuit of a state of emotional activation. In contrast, here are examples of why participants chose the utilitarian video that received the low arousal negative review: “I would rather be bored than angry” and “I didn’t want to watch the one with the being ANGRY comment”. These comments suggest participants’ tendency to avoid risk.

Experimental design regarding the main e<sup>f</sup>ect of online review arousal (control variable: <sup>fi</sup>ve-star rating).

<table><tr><td></td><td>Sub-condition 1</td><td>Sub-condition 2</td></tr><tr><td>Product type</td><td>Two utilitarian videos</td><td>Two hedonic videos</td></tr><tr><td>Sub-conditions</td><td>High arousal review text or low arousal review text</td><td>High arousal review text or low arousal review text</td></tr><tr><td># of MTurkers willing to participate</td><td>60 (out of 60)</td><td>55 (out of 60)</td></tr></table>

Experimental design regarding the main e<sup>f</sup>ect of online review arousal (control variable: one-star rating).

<table><tr><td></td><td>Sub-condition 3</td><td>Sub-condition 4</td></tr><tr><td>Product type</td><td>Two utilitarian videos</td><td>Two hedonic videos</td></tr><tr><td>Sub-conditions</td><td>High arousal review text or low arousal review text</td><td>High arousal review text or low arousal review text</td></tr><tr><td># of MTurkers willing to participate</td><td>58 (out of 60)</td><td>53 (out of 60)</td></tr></table>

![](/api/attachments/BTPSGKQB/fulltext/images/b00a0cf9f6fba972f09584ddffb0c191eed9ce56783a5b4a32d6a675782b1657.jpg)  
The main e<sup>f</sup>ects of online review arousal on video clicks and sales.Note: Error bars represent 95% con<sup>fi</sup>dence intervals.

To test H4, we separated the above e<sup>f</sup>ects for positive and negative reviews (see Figures 4 and 5). The results show that the three-way interaction was not signi<sup>fi</sup>cant. For hedonic videos, positive high arousal review texts led to more sales than positive low arousal review texts (69% versus 31%; $\textstyle P \ < \ 0 . 0 1 )$ . For utilitarian videos, the arousal level in positive online reviews did not a<sup>f</sup>ect sales (54% versus 46%; $p > 0 . 1 )$ . When presented with hedonic videos, 59% of participants chose to click videos with negative high arousal reviews and 41% chose videos with negative low arousal reviews $( p > 0 . 1 )$ When presented with utilitarian videos, 54% of participants chose to click videos with negative high arousal reviews and 46% chose videos with negative low arousal reviews $( p > 0 . 1 )$ . However, the di<sup>f</sup>erence between the two <sup>fi</sup>gures (between positive and negative reviews) was not signi<sup>fi</sup>cant $( p > 0 . 1 )$ . Therefore, H4 was not supported. This result was consistent with that of Study 1, in which the interaction between arousal, valence and product type was not signi<sup>fi</sup>cant.

## 13. Discussion

Findings from both studies consistently showed that the moderating e<sup>f</sup>ects of hedonic/utilitarian product type can explain the mixed <sup>fi</sup>ndings in previous studies.

We tested the conjecture of Duan et al. (2008) that di<sup>f</sup>erences in the literature could have been caused by investigators failing to consider two-way causality and product heterogeneity. To do so, we used Granger causality tests and an experiment to test the direction of causality between reviews and sales and used OLS <sup>fi</sup>xed e<sup>f</sup>ects models to control for product heterogeneity. We proposed that the distinction between hedonic and utilitarian products would moderate the e<sup>f</sup>ects of three heuristic attributes of online reviews. Addressing Duan et al.’s (Duan et al., 2008) concerns regarding con<sup>fl</sup>icts in the literature, our two studies provide an alternative explanation for the long-lasting debate regarding how online reviews a<sup>f</sup>ect sales.

![](/api/attachments/BTPSGKQB/fulltext/images/0cf4a0e0053b5c518175140ab14acee150e9fe9f2a4fad87a9f4a3064b12ca72.jpg)  
The main e<sup>f</sup>ects of online review arousal on video clicks and sales for positive reviews.Note: Error bars represent 95% <sup>Figure 4.</sup>con<sup>fi</sup>dence intervals.

![](/api/attachments/BTPSGKQB/fulltext/images/16188f58fa49d377677f2331e5e4b53cba44097167644145e37813548b170fa8.jpg)  
The main e<sup>f</sup>ects of online review arousal on video clicks and sales for negative reviews.Note: Error bars represent 95% <sup>Figure 5.</sup>con<sup>fi</sup>dence intervals.

Floyd, Freling, Alhoqail, Cho, and Freling (2014) conducted a meta-analysis of the e<sup>f</sup>ect of online review valence and volume on sales for di<sup>f</sup>erent products. Our <sup>fi</sup>ndings suggest reasons for the varied <sup>fi</sup>ndings reported in their work: online review volume drives movie sales (e.g. Chen, Wu, & Yoon, 2004; Duan et al., 2008; Liu, 2006) and online review valence drives computers sales (e.g. Cui et al., 2012) because movies are hedonic and computers are utilitarian. Movies tend to make customers think more of emotions than of utility. As a result, online review volume a<sup>f</sup>ects movie sales more than online review valence does. This argument supports Duan et al.’s (2008) <sup>fi</sup>nding that online review volume a<sup>f</sup>ects movies, but online review valence does not (Duan et al., 2008).

Another example of a study our <sup>fi</sup>ndings help explains involved book reviews in the New York Times (in which the books reviewed are mainly hedonic). Berger et al. (2010) revealed that negative reviews in the New York Times increased book sales by increasing product awareness. Our <sup>fi</sup>nding extends their work and suggests that the driver of the e<sup>f</sup>ect of negative publicity may be the volume and arousal of these reviews. Arousal in negative reviews trigger people’s purchase actions and the volume of negative reviews increase product awareness.

Our <sup>fi</sup>ndings highlight the importance of examining arousal in online reviews to understand their e<sup>f</sup>ect on sales (Ren & Nickerson, 2013, 2014; Yin et al., 2014). After controlling for the control variable and other interaction variables (Table 8), when compared with valence and volume, online review arousal had the lowest coe<sup>fi</sup>cient and the strongest e<sup>f</sup>ect on standardised sales rank (−0.23, $p \textless 0 . 0 0 1$ in Model 2; −0.43, $p ~ < ~ 0 . 0 0 1$ in Model 3). The evidence rejecting H4 suggests that the greater e<sup>f</sup>ect of emotion-charged review texts on sales for hedonic products than for utilitarian products holds true regardless of the valence of online reviews.

Emotion in reviews is associated with their helpfulness (Moore, 2015). For example, Yin et al. found that anxiety-embedded reviews a<sup>f</sup>ected helpfulness ratings more than anger-embedded reviews (Yin et al., 2014). Yin et al. used reviews of electronic goods (utilitarian products) in their experiment. We conjecture that anger-embedded reviews may be more helpful than anxiety-embedded reviews when the reviewed products are hedonic.

Moore (2015) found that reviews of utilitarian and hedonic purchases di<sup>f</sup>er because consumers had a preference regarding how reviewers expressed their opinions. Actions were preferred over reactions for utilitarian products. Therefore, non-reactive reviews were more helpful for these products (and less helpful for hedonic products). Our <sup>fi</sup>ndings are consistent with this result.

Our <sup>fi</sup>ndings also suggest that arousal distribution is not biased across hedonic and utilitarian products. The mean of arousal is not signi<sup>fi</sup>cantly higher for hedonic products than for utilitarian products (1.17 versus 1.15). Tables 5 and 6 show that arousal has similar means, medians and standard deviations for both product categories.

## 14. Limitations, future work, and practical implications

Panel data analysis on 26,357 products allowed us to address product heterogeneity and the online experiment allowed us to observe causality among variables. We examined consumer’s purchase behaviour based on the theory of attribute substitution in decisionmaking processes and provided an explanation for previous mixed <sup>fi</sup>ndings in the online review literature. This explanation has three limitations.

First, we examined products at the extreme ends of the hedonic and utilitarian continuum. It is uncertain whether or how the e<sup>f</sup>ects of online review characteristics di<sup>f</sup>er for complex products that are hedonic and utilitarian, such as hotels.

Second, we focused on heuristic attribute substitution, which is an aspect of the fast decision-making cognitive system, to explain how consumers react di<sup>f</sup>erently to di<sup>f</sup>erent types of products. The slow deliberation system is still very important, especially for purchase decisions for utilitarian products. Therefore, our results may be more relevant to hedonic product settings, in which fast decisions happen frequently, than to settings that focus on utilitarian products, particularly expensive utilitarian products. In such settings, the experiences, product knowledge and deliberative skills of consumers may play a larger role, and there may be large individual di<sup>f</sup>erences.

Third, Piccoli (2016) shows that mobile applications versus web-based applications can be consid ered as an aspect of choice architecture. That is, mobile-based versus web-based reviews have di<sup>f</sup>erent valence, perhaps because mobile reviews are triggered by emotion right after a customer experience. And this potential impact may also hold true for how online reviews a<sup>f</sup>ect sales. Thus, future research might look at the devices and associated interfaces used to post reviews, and, related to the devices, the amount of time elapsed between the customer experience and the submission of a review. It would useful to know whether in-the-moment reviews are more or less useful to prospective customers. It may be that consumers value shorter and more emotional in-themoment reviews di<sup>f</sup>erently than longer, more measured, and more considered reviews, and this di<sup>f</sup>erence might be a<sup>f</sup>ected by product type. More generally, fast and slow consumer decision-making might be a<sup>f</sup>ected by fast and slow review writing.

In sum, future studies might examine complex products that are hedonic and utilitarian. Studies might also focus on the roles of fast and slow decision-making processes, through a combination of observation, interviews and experiments on products of di<sup>f</sup>erent types and prices.

Online review systems, such as Amazon’s, have algorithms for displaying the order in which reviews occur. At the time of writing, Amazon displays reviews sorted by review helpfulness in the left column and displays reviews sorted by recency in the right column. In our analysis, we used the most recent reviews, up to 100. This set usually included the most helpful reviews because less than 15% of the products we sampled had over 100 reviews. However, future research might examine the interactions between helpfulness of reviews and valence, volume and arousal. For example, it may be that certain attributes of a review cause it to be rated as more helpful. This might magnify the review’s e<sup>f</sup>ect.

Research might also examine the sensitivity of purchase decisions to display algorithms that make use of review attributes. This might be accomplished through experiments in which consumers are randomly assigned to di<sup>f</sup>erent display algorithms for di<sup>f</sup>erent product types.

Our <sup>fi</sup>ndings are particularly important for practitioners designing choice architectures for online review systems. When viewing utilitarian products, consumers are likely to want to see valence prominently. When viewing hedonic products, consumers are likely to want to engage with the text of reviews and may be particularly sensitive to the level of arousal expressed. Current online review systems employ a number of di<sup>f</sup>erent techniques for aggregating and spotlighting reviews, including asking consumers to rank the helpfulness of reviews. Ideally, the designer of an online review system would understand what attracts the attention of a consumer and what kinds of reviews lead to purchase decisions with which the consumer remains satis<sup>fi</sup>ed (Lynch Jr & Zauberman, 2007). Our <sup>fi</sup>ndings suggest that an algorithm for summarising or highlighting reviews would need to consider the type of product, the language used in the review, star ratings, volume and the interaction between star ratings and emotion-charged review texts. Whether emotion-charged reviews lead to better or worse decision-making for particular products is a topic for future research.

## 15. Conclusions

Consumer decision-making is complex. Online review systems provide much needed data, but the amount of data can be overwhelming. Consumers use heuristics to make decisions. Which heuristics they use depends on the type of product being considered. Whether a product is utilitarian or hedonic triggers di<sup>f</sup>erent heuristics. Product type a<sup>f</sup>ects the in<sup>fl</sup>uence of three characteristics of reviews: valence, arousal and volume. Our panel data analysis of 26,357 Amazon products and an experiment with 541 participants support these claims. Online review valence is more likely to increase sales for utilitarian products, whereas online review volume and arousal are more likely to increase sales for hedonic products. This model of online reviews is one step towards a better understanding of the e<sup>f</sup>ects of online review systems and may lead to strategies for practitioners who design choice architectures for such systems.

## Disclosure statement

No potential con<sup>fl</sup>ict of interest was reported by the authors.

## Notes on contributors

![](/api/attachments/BTPSGKQB/fulltext/images/3338d46aa66184079ec568d1a5b8ae33451d0936851c9d6726b33c792998e736.jpg)

Jie Ren is an assistant professor at Gabelli School of Business, Fordham University. Her research focuses on online collective behaviors. She is inter ested in understanding the business impact of these behaviors, especially in the <sup>fi</sup>eld of marketing, innovation, and <sup>fi</sup>nance. She currently studies social media, crowdsourcing, and innovation.

![](/api/attachments/BTPSGKQB/fulltext/images/6c658626fdb96cf54050fae9aa1fead52223fb9423ea15b9f47d75d69c2a4684.jpg)

Jefrey V. Nickerson is Professor and Director of the Center for Decision Technologies in the School of Business at Stevens Institute of Technology. His research and teaching interests include social media analytics, information systems design, computersupported cooperative work, and collective creativity.

## References

Babin, B. J., Darden, W. R., & Gri<sup>fi</sup>n, M. (1994). Work and/or fun: Measuring hedonic and utilitarian shopping value. Journal of Consumer Research, 644–656.

Baum, C. F. (2006). An introduction to modern econometrics using Stata. Texas, USA: StataCorp LP.

Baumeister, R. F., Bratslavsky, E., Finkenauer, C., & Vohs, K. D. (2001). Bad is stronger than good. Review of General Psychology, 5(4), 323.

Beaudry, A., & Pinsonneault, A. (2010). The other side of acceptance: studying the direct and indirect e<sup>f</sup>ects of emotions on information technology use. MIS Quarterly, 34(4), 689–710.

Berger, J., Sorensen, A. T., & Rasmussen, S. J. (2010). Positive e<sup>f</sup>ects of negative publicity: When negative reviews increase sales. Marketing Science, 29(5), 815–827.

Bradley, M. M., Hamby, S., Löw, A., & Lang, P. J. (2007). Brain potentials in perception: Picture complexity and emotional arousal. Psychophysiology, 44(3), 364–373.

BrightLocal. (2014). Local consumer review survey. Retrieved from West St, Lewes, UK: https://www.bright local.com/learn/local-consumer-review-survey/

Cheema, A., & Papatla, P. (2010). Relative importance of online versus o<sup>fl</sup>ine information for Internet purchases: Product category and Internet experience e<sup>f</sup>ects. Journal of Business Research, 63(9), 979–985.

Chen, P. Y., Wu, S. Y., & Yoon, J. (2004). The impact of online recommendations and consumer feedback on sales. ICIS 2004 Proceedings, 58.

Chevalier, J. A., & Mayzlin, D. (2006). The e<sup>f</sup>ect of word of mouth on sales: Online book reviews. Journal of Marketing Research, 43(3), 345–354.

Childers, T. L., Carr, C. L., Peck, J., & Carson, S. (2001). Hedonic and utilitarian motivations for online retail shopping behavior. Journal of Retailing, 77(4), 511–535.

Chintagunta, P. K., Gopinath, S., & Venkataraman, S. (2010). The e<sup>f</sup>ects of online user reviews on movie box o<sup>fi</sup>ce performance: Accounting for sequential rollout and aggregation across local markets. Marketing Science, 29(5), 944–957.

Chiu, C. M., Wang, E. T., Fang, Y. H., & Huang, H. Y. (2014). Understanding customers’ repeat purchase intentions in B2C e-commerce: The roles of utilitarian value, hedonic value and perceived risk. Information Systems Journal, 24(1), 85–114.

Cui, G., Lui, H. K., & Guo, X. (2012). The e<sup>f</sup>ect of online consumer reviews on new product sales. International Journal of Electronic Commerce, 17(1), 39–58.

Dawar, N., & Parker, P. (1994). Marketing universals: Consumers’ use of brand name, price, physical appearance, and retailer reputation as signals of product quality. The Journal of Marketing, 58(2), 81–95.

Dellarocas, C., Zhang, X. M., & Awad, N. F. (2007). Exploring the value of online product reviews in forecasting sales: The case of motion pictures. Journal of Interactive Marketing, 21(4), 23–45.

Dhar, R., & Wertenbroch, K. (2000). Consumer choice between hedonic and utilitarian goods. Journal of Marketing Research, 37(1), 60–71.

Dimoka, A., Hong, Y., & Pavlou, P. A. (2012). On product uncertainty in online markets: Theory and evidence. MIS Quarterly, 36(2), 395-426.

Drolet, A., Simonson, I., & Tversky, A. (2000). Indi<sup>f</sup>erence curves that travel with the choice set. Marketing Letters, 11(3), 199–209.

Duan, W., Gu, B., & Whinston, A. B. (2008). Do online reviews matter? - An empirical investigation of panel data. Decision Support Systems, 45(4), 1007–1016.

Duan, W., Gu, B., & Whinston, A. B. (2009). Informational cascades and software adoption on the Internet: An empirical investigation. MIS Quarterly 33 (1), 23-48.

Floyd, K., Freling, R., Alhoqail, S., Cho, H. Y., & Freling, T. (2014). How online product reviews a<sup>f</sup>ect retail sales: A meta-analysis. Journal of Retailing, 90(2), 217–232.

Gerdes, A. B., Wieser, M. J., Mühlberger, A., Weyers, P., Alpers, G. W., Plichta, M. M., & Pauli, P. (2010). Brain activations to emotional pictures are di<sup>f</sup>erentially associated with valence and arousal ratings.Frontiers in human neuroscience. Available online https://doi.org/ 10.3389/fnhum.2010.00175.

Ghose, A., & Ipeirotis, P. G. (2011). Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Transactions on Knowledge and Data Engineering, 23 (10), 1498–1512.

Gilovich, T., Gri<sup>fi</sup>n, D., & Kahneman, D. (2002). Heuristics and biases: The psychology of intuitive judgment. Cambridge, UK: Cambridge university press.

Goh, K. Y., Heng, C. S., & Lin, Z. (2013). Social media brand community and consumer behavior: Quantifying the relative impact of user- and marketer-generated content. Information Systems Research, 24(1), 88–107.

Goldstein, D. G., Johnson, E. J., Herrmann, A., & Heitmann, M. (2008). Nudge your customers toward better choices. Harvard Business Review, 86(12), 99–105.

Grant. 2011 http://www.salon.com/2011/03/29/justin\_bie ber\_vs\_rebecca\_black\_most\_hated\_youtube

Heilman, K. (1997). The neurobiology of emotional experience. In The neuropsychiatry of limbic and subcortical disorders (pp. 133–142). Washington DC, USA: American Psychiatric Association Publishing

Hirschman, E. C., & Holbrook, M. B. (1982). Hedonic consumption: Emerging concepts, methods and propositions. The Journal of Marketing, 46(3), 92–101.

Hsiao, C. (1986). Analysis of Panel Data. Cambridge, UK: Cambridge University Press.

Hu, M., & Liu, B. (2004). Mining and summarizing customer reviews. Proceedings of the tenth ACM SIGKDD international conference on Knowledge discovery and data mining, 168–177.

Ito, T. A., Larsen, J. T., Smith, N. K., & Cacioppo, J. T. (1998). Negative information weighs more heavily on the brain: The negativity bias in evaluative categorizations. Journal of Personality and Social Psychology, 75(4), 887.

Johnson, E. J., Shu, S. B., Dellaert, B. G., Fox, C., Goldstein, D. G., Häubl, G., & Wansink, B. (2012). Beyond nudges: Tools of a choice architecture. Marketing Letters, 23(2), 487–504.

Kahneman, D. (2003). A perspective on judgment and choice: Mapping bounded rationality. American Psychologist, 58(9), 697.

Kahneman, D., & Frederick, S. 2004. Attribute substitution in intuitive judgment. Models of a man: Essays in memory of Herbert A. Simon. edited by, H. A. Simon, M. Augier, & G. James. March. 411–432. Boston, USA: MIT press.

Kahneman, D., & Egan, P. (2011). Thinking, fast and slow. vol. 1. New York, NY: Farrar, Straus and Giroux.

Kempf, D. S. (1999). Attitude formation from product trial: Distinct roles of cognition and a<sup>f</sup>ect for hedonic and functional products. Psychology & Marketing, 16(1), 35–50.

Khan, U., Dhar, R., & Wertenbroch, K. (2004). A behavioral decision theoretic perspective on hedonic and utilitarian choice. Unpublished manuscript.

Kittur, A., Chi, E. H., & Suh, B. (2008). Crowdsourcing user studies with Mechanical Turk. In Proceedings of the SIGCHI conference on human factors in computing systems, 453–456.

Kuppens, P., Tuerlinckx, F., Yik, M., Koval, P., Coosemans, J., Zeng, K. J., & Russell, J. A. (2017). The relation between valence and arousal in subjective experience varies with personality and culture. Journal of Personality, 85(4), 530–542.

Kushwaha, T., & Shankar, V. (2013). Are multichannel customers really more valuable? The moderating role of product category characteristics. Journal of Marketing, 77(4), 67–85.

Liu, Q. B., & Karahanna, E. (2017). The dark side of reviews: The swaying e<sup>f</sup>ects of online product reviews on attribute preference construction. MIS Quarterly, 41 (2), 427–448.

Liu, Y. (2006). Word of mouth for movies: Its dynamics and impact on box o<sup>fi</sup>ce revenue. Journal of Marketing, 70(3), 74–89.

Lynch Jr, J. G., & Zauberman, G. (2007). Construing consumer decision making. Journal of Consumer Psychology, 17(2), 107–112.

Mavlanova, T., Benbunan-Fich, R., & Koufaris, M. (2012). Signaling theory and information asymmetry in online commerce. Information & Management, 49(5), 240–247.

Moore, S. G. (2015). Attitude predictability and helpfulness in online reviews: The role of explained actions and reactions. Journal of Consumer Research, 42(1), 30–44.

Mudambi, S. M., & Schu<sup>f</sup>, D. (2010). What makes a helpful review? A study of customer reviews on Amazon.com. MIS Quarterly, 34(1), 185–200.

O’Brien, R. M. (2007). A caution regarding rules of thumb for variance in<sup>fl</sup>ation factors. Quality & Quantity, 41(5), 673–690.

Pang, B., Lee, L., & Vaithyanathan, S. (2002). Thumbs up?: Sentiment classi<sup>fi</sup>cation using machine learning techniques. In Proceedings of the ACL-02 conference on Empirical methods in natural language processing, 79-86.

Park, C., & Lee, T. M. (2009). Antecedents of online reviews’ usage and purchase in<sup>fl</sup>uence: An empirica comparison of US and Korean consumers. Journal of Interactive Marketing, 23(4), 332–340.

Pengnate, S. F., & Delen, D. (2014). Evaluating emotions in mobile application descriptions: Sentiment analysis approach. In Proceedings of the 20th Americas Conference on Information Systems.

Piccoli, G. (2016). Triggered essential reviewing: The e<sup>f</sup>ect of technology a<sup>f</sup>ordance on service experience evaluations. European Journal of Information Systems, 25(6), 477–492.

Ren, J., & Nickerson, J. V. (2013). Examining the relationship between online review sentiment and sales. In Workshops of Information Networks. New York, NY: New York University.

Ren, J., & Nickerson, J. V. (2014). Online review systems: How emotional language drives sales. Twentieth Americas Conference on Information Systems.

Ren, J., Yeoh, W., Shan, E. M., ., & Popovič, A. (2018). Online consumer reviews and sales: Examining the chicken-egg relationships. Journal of the Association for Information Science and Technology, 69(3), 449–460.

Ross, J., Irani, L., Silberman, M. S., Zaldivar, A., & Tomlinson, B. (2010). Who are the crowdworkers?: Shifting demographics in Mechanical Turk. In CHI EA’10: Proceedings of the 28th of the international conference extended abstracts on Human factors in computing systems, 2863–2872.

Rozin, P., & Royzman, E. B. (2001). Negativity bias, negativity dominance, and contagion. Personality and Social Psychology Review, 5(4), 296–320.

Russell, J. A. (1979). A<sup>f</sup>ective space is bipolar. Journal of Personality and Social Psychology, 37(3), 345.

Russell, J. A. (1980). A circumplex model of a<sup>f</sup>ect. Journal of Personality and Social Psychology, 39(6), 1161.

Russell, J. A. (2003). Core a<sup>f</sup>ect and the psychological construction of emotion. Psychological Review, 110(1), 145.

Salganik, M. J., & Levy, K. E. (2015). Wiki surveys: Open and quanti<sup>fi</sup>able social data collection. PloS one, 10(5), e0123483.

Sen, S., & Lerman, D. (2007). Why are you telling me this? An examination into negative consumer reviews on the web. Journal of Interactive Marketing, 21(4), 76–94.

Simola, J., Le Fevre, K., Torniainen, J., & Baccino, T. (2015). A<sup>f</sup>ective processing in natural scene viewing: Valence and arousal interactions in eye-<sup>fi</sup>xation-related potentials. NeuroImage, 106, 21–33.

Strahilevitz, M. A., & Myers, J. (1998). Donations to charity as purchase incentives: How well they work may depend on what you are trying to sell. Journal of Consumer Research, 24(4), 434.

Sun, M. (2011). How Does the Variance of Product Ratings Matter?. Management Science, 58(4), 696–707.

Thaler, R. H., & Sunstein, C. R. (2008). Nudge: Improving decisions about health, wealth, and happiness. New Haven: Yale University Press.

Thelwall, M., Buckley, K., & Paltoglou, G. (2011). Sentiment in Twitter events. Journal of the American Society for Information Science and Technology, 62(2), 406–418.

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124–1131.

Van der Heijden, H. (2004). User acceptance of hedonic information systems. MIS Quarterly 28(4),695-704.

Wake<sup>fi</sup>eld, R. L., Wake<sup>fi</sup>eld, K. L., Baker, J., & Wang, L. C. (2011). How website socialness leads to website use. European Journal of Information Systems, 20(1), 118–132.

Wang, A., Zhang, M., & Hann, I. H. (forthcoming). Socially nudged: A quasi-experimental study of friends’ social in<sup>fl</sup>uence in online product ratings. Information Systems Research. doi:10.1287/isre.2017.0741

Warriner, A. B., & Kuperman, V. (2015). A<sup>f</sup>ective biases in English are bi-dimensional. Cognition and Emotion, 29 (7), 1147–1167.

Warriner, A. B., Kuperman, V., & Brysbaert, M. (2013). Norms of valence, arousal, and dominance for 13,915 English lemmas. Behavior Research Methods, 45(4), 1191–1207.

Wu, J., & Gaytán, E. A. A. (2013). The role of online seller reviews and product price on buyers’ willingness-to-pay: A risk perspective. European Journal of Information Systems, 22(4), 416–433.

Wul<sup>f</sup>, D. U., Hills, T. T., & Hertwig, R. (2014). Online product reviews and the description–Experience gap. Journal of Behavioral Decision Making, 28(3), 214–223.

Yang, J., Kim, W., Amblee, N., & Jeong, J. (2012). The heterogeneous e<sup>f</sup>ect of WOM on product sales: Why the e<sup>f</sup>ect of WOM valence is mixed?. European Journal of Marketing, 46(11/12), 1523–1538.

Ye, Q., Law, R., & Gu, B. (2009). The impact of online user reviews on hotel room sales. International Journal of Hospitality Management, 28(1), 180–182.

Ye, Q., Law, R., Gu, B., & Chen, W. (2011). The in<sup>fl</sup>uence of user-generated content on traveler behavior: An empirical investigation on the e<sup>f</sup>ects of e-word-ofmouth to hotel online bookings. Computers in Human Behavior, 27(2), 634–639.

Yin, D., Bond, S., & Zhang, H. (2014). Anxious or angry? E<sup>f</sup>ects of discrete emotions on the perceived helpfulness of online reviews. MIS Quarterly, 38(2), 539–560.

Zhang, P. (2013). The a<sup>f</sup>ective response model: A theoretical framework of a<sup>f</sup>ective concepts and their relationships in the ICT context. MIS Quarterly, 37(1), 247– 274.

Zhu, F., & Zhang, X. (2010). Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. Journal of Marketing, 74(2), 133–148.

## Appendix

Fixed e<sup>f</sup>ects estimation.

<table><tr><td>Variables</td><td>Model 2 coefficient (std. err.)</td></tr><tr><td>Ln (purchase price)</td><td>0.03 (0.0008) [***]</td></tr><tr><td>Valence</td><td>-0.021 (0.0026) [***]</td></tr><tr><td>Ln (online review volume)</td><td>-0.19 (0.001) [***]</td></tr><tr><td>Arousal</td><td>-0.23 (0.0087) [***]</td></tr><tr><td>Product type</td><td>-0.49 (0.019) [***]</td></tr><tr><td>Product type × valence</td><td>-0.032 (0.0032) [***]</td></tr><tr><td>Product type × ln (online review volume)</td><td>0.161 (0.001) [***]</td></tr><tr><td>Product type × arousal</td><td>0.244 (0.01) [***]</td></tr><tr><td>R squared</td><td>0.22</td></tr></table>

Note: DV is standardised sales rank in its descending order; the higher the DV, the lower the sales; \*\*\* p < 0.001; online review volume > 1; product type is coded as 1 for utilitarian products and 0 for hedonic products; time dummies (<sup>fi</sup>xed e<sup>f</sup>ect for each day) used in estimating the model are not reported.
