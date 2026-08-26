---
otero_id: 9664
otero_key: "SMXMTZ7J"
title: "Investigating the Effects of Dimension-Specific Sentiments on Product Sales: The Perspective of Sentiment Preferences"
authors: "Cuiqing Jiang; Jianfei Wang; Qian Tang; Xiaozhong Lyu"
year: "2021"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00668"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
3-9-2021

# Investigating the Effects of Dimension-Specific Sentiments on Product Sales: The P   erspective of Sentiment Pr   eferences

Cuiqing Jiang , jiangcuiq2017@163.com

Jianfei Wang , wjf@mail.hfut.edu.cn

Qian TANG , QIANTANG@smu.edu.sg

Xiaozhong Lyu , adolflv@mail.hfut.edu.cn

Follow this and additional works at: https://aisel.aisnet.org/jais

# Investigating the Effects of Dimension-Specific Sentiments on Product Sales: The Perspective of Sentiment Preferences

Cuiqing Jiang<sup>1</sup>, Jianfei Wang<sup>2</sup>, Qian Tang<sup>3</sup>, Xiaozhong Lyu<sup>4</sup>

<sup>1</sup>School of Management, Hefei University of Technology, China, jiangcuiq2017@163.com <sup>2</sup>Corresponding author, School of Management, Hefei University of Technology, China, wjf@mail.hfut.edu.cn <sup>3</sup>Singapore Management University, School of Information Systems, Singapore; qiantang@smu.edu.sg <sup>4</sup>Corresponding author, the 38th Research Institute of China Electronics Technology Group Corporation / Key Laboratory of Aperture Array and Space Application, China; adolflv@mail.hfut.edu.cn

## Abstract

While the literature has reached a consensus on the awareness effect of online word-of-mouth (eWOM), this paper studies its persuasive effect—specifically, dimension-specific sentiment effects on product sales. We examine the sentiment information in eWOM along different product dimensions and reveal different persuasive effects on consumers’ purchase decisions based on consumers’ sentiment preference, which is defined as the relative importance that consumers place on various dimension-specific sentiments. We use an aspect-level sentiment analysis to derive dimension-specific sentiment and PVAR (panel vector auto-regression) models, and estimate their effects on product sales using a movie panel dataset. The findings show that three dimension-specific sentiments (star, genre, and plot) are positively related to movie sales. Regarding consumers’ sentiment preferences, we find a positive relationship to movie sales that is stronger for plo sentiment, relative to star sentiment for low-budget movies. For high-budget movies, we find a positive relationship to movie sales that is stronger for star sentiment, relative to plot or genre sentiment.

Keywords: Online Word of Mouth, Dynamic Topic Model, Sentiment Analysis, Product Sales

Kenny Cheng was the accepting senior editor. This research article was submitted on July 14, 2019 and underwent three revisions.

## 1 Introduction

Online word of mouth (eWOM) is a virtual currency for companies because of its strong influence on consumer preferences, especially for experience goods that are difficult to characterize before consumption (Duan et al., 2008; Hu et al., 2008; Zhao et al., 2017). Most consumers would want to know about other consumers’ experiences before visiting a restaurant, booking a hotel, or even seeing a doctor. In fact, 82% of consumers read online reviews for local businesses and the average consumer reads 10 reviews before feeling able to trust a business.<sup>1</sup> According to a Statista survey of US online consumers conducted in November 2019, 91% of respondents reported that positive reviews made them more likely to use a business, whereas 82% of consumers reported that negative reviews made them less likely to patronize a local business.<sup>2</sup> Within five days of Canadian musician Dave Carroll posting a YouTube video called “United

Breaks Guitars” to broadcast his bad experience with United Airlines in July 2009, it was widely reported that the airline lost 10% of its market value, costing shareholders roughly \$180 million.<sup>3</sup>

However, the influence of eWOM is not always clear in practice. For example, while high ratings made box office hits of some movies such as Midnight Express, The Lion King, and Lord of the Rings, others managed to score big at the box office despite terrible reviews. For instance, Bohemian Rhapsody, with an audience rating of 85% on Rotten Tomatoes and 8 out of 10 on IMDB, was a major box office success, grossing over \$903 million worldwide with a production budget of about \$50 million. However, Clash of the Titans, dominated the box office over its first two weekends and went on to earn \$163.2 million domestically and an additional \$330 million worldwide, <sup>4</sup> despite its rating of only 28% on Rotten Tomatoes and 5.8 out of 10 on IMDB. Previous research on the effects of eWOM sentiment on product sales has also generated mixed results on the persuasive effect of eWOM, i.e., its influence on consumers’ assessment of product quality (Duan et al., 2008). Generally speaking, the persuasive effect of eWOM occurs when positive reviews affect sales positively and negative reviews affect sales negatively (Chaiken & Shelly, 1980; Ludwig et al., 2013). However, in the context of movies, some studies demonstrate that sentiment does not affect box office revenues (Liu et al., 2010; Zhang et al., 2012), while others suggest a positive effect of eWOM regardless of its sentiment (Berger et al., 2010; Hu et al., 2014; Rui et al., 2013). Such mixed findings might stem from various moderators, such as brand awareness of the product and the reputation of the communicator (King et al., 2014).

Moreover, previous literature focuses on the overall or aggregate review sentiment in studying the persuasive effects of eWOM. Although the impact of different sentiments on different product dimensions or attributes is often overlooked, it is nevertheless an important issue. According to consumers’ product preferences, different product attributes affect their purchases differently (Berry et al., 1995, 2004). Similarly, unimportant attributes and attributes of opposing sentiments can lead to insignificant or even misleading results, based on the overall sentiment, which aggregates sentiments on all product attributes (Li et al., 2019; Liang et al., 2015).

Although recent research has begun to explore the effect of multi-aspect sentiments on sales (Liang et al., 2015; Li et al., 2019), these studies mined static product dimensions without explaining why different dimensions of emotion have different effects. Thus, the difference in the persuasion effect of dimensionspecific sentiments is unclear. To address these research gaps, we aim to better understand the persuasive effect of eWOM by answering the following two research questions:

RQ1: How are dimension-specific sentiments associated with product sales?

RQ2: Among these dimensions, which dimension sentiments are more important?

To answer these questions, we define consumers sentiment preference as the relative importance placed on various dimension-specific sentiments of eWOM when evaluating a product. The higher the sentiment preference of a dimension, the more persuasive the eWOM sentiment of that dimension (Aggarwal et al., 2012). We explain the persuasive effect of dimensionspecific sentiments using multi-attribute attitude theory, which breaks down the consumer’s overall attitude of the product into different attitudes toward smaller product components that influence consumers differently (Fishbein, 1963; Hansen, 1969; Kraft et al., 1973). We extend multi-attribute attitude theory by considering the prominence of attributes in consumers’ attention, which is affected by the specific market environment for the product (Johnson et al., 1988; Tversky et al., 1988; Shavitt & Fazio, 1991).

We chose the US film industry as our research context and collected a panel dataset on movies from IMDB.com. Beyond eWOM, movie quality is mainly determined and signaled by its production budget. For movie producers, the production budget determines the allocation of resources devoted to producing the movie. For potential consumers, the production cost of the film is a powerful quality signal. High-budget movies usually imply big-name stars, spectacular special effects, lavish costumes, and other expensive elements (Holbrook & Addis, 2008). To understand the relative importance of dimension sentiments, we explore how consumers’ sentiment preference depends on the movie production budget. We first use an aspect-level sentiment analysis combining the dynamic topic model (DTM), the Stanford syntax parser, and sentiment lexicon (Schouten & Frasincar, 2016) on the texts of movie reviews to identify key dimensions and calculate the sentiment of each dimension. Then, we construct PVAR (panel vector auto-regression) models estimated by the SGMM (system generalized method of moments) method to identify sentiment effects on sales.

Our findings indicate that the sentiments of the three dimensions identified (i.e., star, genre, and plot) all have significant positive effects on movie sales. More importantly, our results show that consumers have different sentiment preferences, respectively, for highand low-budget movies. Specifically, for low-budget movies, we found that plot sentiment has stronger impacts than star sentiment on box office sales, whereas star sentiment is more influential than plot and genre sentiments for high-budget movies.

These findings contribute to the literature in terms of both theory and practice. First, while the literature on dimension sentiment effects examines the effect for each dimension individually, we focus on consumers’ sentiment preferences and on the relative effects of different dimension sentiments. Comparing the sentiment effects of different dimensions is especially important when the sentiments about different product dimensions are mixed, i.e., positive for some dimensions but negative for others. Second, in extracting the sentiments of each dimension from eWOM text data to reflect the review’s focus, we develop an aspect-level sentiment analysis framework that considers the weight of each dimension’s topic words. Our dimension mining method is also capable of identifying the temporal evolution of topic words in eWOM. Third, we develop multi-attribute attitude theory by integrating the influence of market environment on attribute importance, providing a better understanding of consumers’ product evaluation under the joint influence of brand marketing and eWOM.

We organize the remainder of this paper as follows. Section 2 reviews the related literature. Section 3 describes our research methodology, including research context, data collection, dimension and sentiment mining, hypotheses development, and the empirical model. Section 4 reports our empirical results, and Section 5 concludes the paper.

## 2 Theoretical Background

## 2.1 The Effects of eWOM Sentiment on Product Sales

The eWOM sentiment refers to affective or opinionated content provided in written text, which reflects the reviewer’s positive, negative, or neutral attitudes toward a product or service (Schouten & Frasincar, 2016). According to theories on information processing and consumer conversion, affective reviews provide relevant and influential information (Chaiken, & Shelly, 1980; Ludwig et al., 2013). The heuristic cues contained in review texts can influence respondents’ attitudes and drive potential consumers’ behavior through the persuasive effect (Lau-Gesk et al., 2009; Li & Zhan, 2011; Cui et al., 2012; Fan et al., 2017; Liu & Karahanna, 2017). Different from the awareness effect, whereby eWOM simply informs potential consumers of the product, the persuasive effect shapes consumers’ attitudes and evaluation toward a product and ultimately influences their purchase decisions (Duan et al., 2008).

Previous studies related to the effects of eWOM on product sales are summarized in Table 1. The existing literature often focuses on the numerical aspects of eWOM, such as the volume (Vol) or valence (Val) of reviews, and the effects of eWOM sentiment are only studied in literature that also examines the textual aspects of eWOM. Most of these studies only look at the overall sentiment and generate mixed findings. Some studies demonstrate that sentiment does not significantly affect book sales or movie box office revenue (Liu, 2006; Liu et al., 2010; Zhang et al., 2012), while others find a positive effect of positive sentiment and a negative effect of negative sentiment for books (Hu et al., 2014) and movies (Rui et al., 2013) or suggest a positive effect of negative eWOM for lesser-known products (Berger et al., 2010).

Given the mixed results, the literature has started to consider various moderators (i.e., product, message, reviewer, and receiver characteristics) and examine whether the effect of sentiment varies according to these moderating factors (Hovland et al., 1953; Petty & Cacioppo, 2012; King et al. 2014). For example, Cui et al. (2012) found that the product type (experience or search product) moderates the effect of review valence. Lin & Wang (2018) showed that network connection between two products impacts the effect of word-ofmouth on product sales.

In addition to moderators, the mixed findings may be attributed to the heterogeneity of dimension-specific sentiments, since the aforementioned research focuses on the overall review sentiment and does not differentiate the specific product dimension referred to. For example, for a review describing two product dimensions, its neutral overall sentiment may be caused by either similarly neutral sentiments of both dimensions or almost opposing sentiments of the two dimensions. Without considering consumers’ dimension-specific sentiment preferences, the overall sentiment simply aggregates the sentiments of all product dimensions and polarities. This assumes equal sentiment preferences for all the dimensions. The heterogeneity of different dimension-specific sentiments is lost in such information aggregation.

A few recent studies have taken the multi-aspect perspective in sentiment analyses and show that sentiments of different dimensions affect consumers differently (Liang et al., 2015; Li et al. 2019). For example, Liang et al. (2015) used human annotations to extract the sentiments of two predefined product dimensions, and Li et al. (2019) used the joint sentimenttopic model (JST) to extract four time-invariant product dimensions. While our paper is motivated by their work, we develop their research methods by utilizing a more flexible dynamic aspect-level sentiment analysis (Schouten & Frasincar, 2016) without predefining product dimensions.

Table 1. Summary of Studies on the Effect of eWOM on Sales

<table><tr><td rowspan="2">Literature</td><td colspan="2">Numerical aspect</td><td rowspan="2">Moderator</td><td>Text aspect</td><td rowspan="2">Context</td><td rowspan="2">Results on sentiment effect</td></tr><tr><td>Vol</td><td>Val</td><td>Sen</td></tr><tr><td>Chevalier &amp; Mayzlin (2006)</td><td>✓</td><td>✓</td><td></td><td></td><td>Book</td><td></td></tr><tr><td>Liu (2006)</td><td>✓</td><td></td><td></td><td>✓</td><td>Movie</td><td>Not significant</td></tr><tr><td>Clemons et al. (2006)</td><td>✓</td><td>✓</td><td></td><td></td><td>Beer</td><td></td></tr><tr><td>Dellarocas et al. (2007)</td><td>✓</td><td>✓</td><td></td><td></td><td>Movie</td><td></td></tr><tr><td>Duan et al. (2008)</td><td>✓</td><td>✓</td><td></td><td></td><td>Movie</td><td></td></tr><tr><td>Berger et al. (2010)</td><td>✓</td><td></td><td></td><td>✓</td><td>Book</td><td>Negative eWOM can increase sales of lesser-known products.</td></tr><tr><td>Liu et al. (2010)</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>Movie</td><td>Not significant</td></tr><tr><td>Zhu &amp; Zhang (2010)</td><td>✓</td><td></td><td>product popularity</td><td></td><td>Game console</td><td></td></tr><tr><td>Chintagunta et al. (2010)</td><td>✓</td><td>✓</td><td></td><td></td><td>Movie</td><td></td></tr><tr><td>Amblee &amp; Bui (2011)</td><td>✓</td><td>✓</td><td></td><td></td><td>Book</td><td></td></tr><tr><td>Archak et al. (2011)</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>Camera</td><td>Some phrases of attributes like “design,” “ease of use,” “battery life,” and “size” impact sales.</td></tr><tr><td>Cui et al. (2012)</td><td>✓</td><td>✓</td><td>product type</td><td></td><td>Electronics, Video games</td><td></td></tr><tr><td>Sun (2012)</td><td>✓</td><td>✓</td><td>product popularity</td><td></td><td>Movie, book</td><td></td></tr><tr><td>Zhang et al. (2012)</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>Book, Movie</td><td>Not significant</td></tr><tr><td>Rui et al. (2013)</td><td>✓</td><td></td><td>reviewer&#x27;s influence</td><td>✓</td><td>Movie</td><td>Positive eWOM increases movie sales whereas negative eWOM lowers movie sales.</td></tr><tr><td>Lu et al. (2013)</td><td>✓</td><td>✓</td><td>promotional marketing</td><td></td><td>Restaurant</td><td></td></tr><tr><td>Dewan &amp; Ramaprasad (2014)</td><td>✓</td><td></td><td>product popularity</td><td></td><td>Music</td><td></td></tr><tr><td>Hu et al. (2014)</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>Book</td><td>Only the sentiment of the most helpful reviews positively affects sales.</td></tr><tr><td>Liang et al. (2015)</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>Mobile app</td><td>Sentiment on service quality affects sales more than sentiment on product quality.</td></tr><tr><td>Wang et al. (2015)</td><td>✓</td><td>✓</td><td>variance and quality signal</td><td></td><td>Movie, book, and camera</td><td></td></tr><tr><td>Kostyra et al. (2016)</td><td>✓</td><td>✓</td><td>brand, price, and product attributes</td><td></td><td>eBook reader</td><td></td></tr><tr><td>Li et al. (2019)</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>Tablet computer</td><td>Only positive discussion of hardware features and hedonic experience increases sales.</td></tr></table>

## 2.2 Multi-Attribute Attitude Theory

Multi-attribute attitude theory breaks down the consumer’s overall attitude of the product into smaller components regarding each product attribute (Kraft, Granbois, & Summers, 1973). Hence, a consumer’s overall attitude toward a product is a weighted sum of preferences for the product’s individual dimensions or attributes (Fishbein, 1963). This can be shown as:

$$
A = \sum_ {i = 1} ^ {n} B _ {i} E _ {i},\tag{1}
$$

where A = overall attitude toward a product; $B _ { i } =$ belief that the product needs to possess attribute $i ; E _ { i }$ = evaluation or desirability of the product with respect to attribute ??, i.e, consumer’s preference for attribute ??; ?? = attribute 1, 2, … m. According to multi-attribute attitude theory, changes in consumers’ attitudes may stem from changes in either consumers’ evaluations or their preferences for some dimensions. The more preferred attributes, i.e., the attributes with higher $E _ { i } ,$ influence consumers’ purchase intentions more (Hansen, 1969). The persuasive effect of information, however, refers to the change in attribute evaluations because of information received.

In the context of eWOM, prior customers can freely choose how to evaluate, describe, and criticize the different dimensions of products (Jiménez & Mendoza, 2013). In terms of these different affective cues, potential consumers form attitudes towards the product through their evaluations and preferences for these dimensions. Dimensions (?? ) can be identified from the texts of eWOM, as reviewers tend to evaluate important dimensions of products in reviews (Guo et al., 2017). Then the dimension-specific evaluations $( B _ { i } )$ are shaped by dimension-specific sentiments. When eWOM reveals more positive opinions about a product dimension, consumers who read the review may believe that the product possesses the dimension attribute (Liu & Karahanna, 2017). Lastly, consumers are unlikely to consider the whole review text equally in information processing and different emotional preferences for different dimensions may arise (Li et al., 2019). Their sentiment preferences $( E _ { i } )$ are unobservable but can be inferred by the relative influence of various dimension-specific sentiments on product sales (Schouten & Frasincar, 2016).

## 2.3 The Attribute Importance in Product Evaluation

As consumers’ preferences are context dependent, the attribute importance weights used for the same product class may vary. For example, persuasive messages (Gardner, 1983), situational factors (Miller & Ginter, 1979), contextual factors like the number of levels or values an attribute takes on (Currim et al., 1981), and the order of presentation of attribute information (Anderson & Hubert, 1963) have all been found to influence attribute importance weights.

The attributes the consumer pays attention to can be affected by the market environment (Johnson et al., 1988, Tversky et al., 1988, Shavitt & Fazio, 1991). Marketers may try to influence the market environment through advertisements, packaging, or branding so that a consumer’s attention is drawn to a specific attribute. According to the marketing literature on information processing and advertisement effectiveness, an attribute that is more prominent in product advertising is more likely to be recalled and used for product evaluation (Gardner, 1983). For product comparison, if firms emphasize the same attribute, then a consumer evaluates competing products only on that attribute, whereas if firms emphasize different attributes, consumers split their limited attention across multiple attributes (Zhu & Dukes, 2017).

## 3 Methodology

## 3.1 Research Context and Data Collection

We choose the US film industry as our research context. Although successful movies are highly profitable, film production is often very risky. Six to seven of every ten films produced are unprofitable (Ghiassi et al., 2015). This paper focuses on online reviews of movies because they are more popular than other types of eWOM, such as blogs and tweets (Duan et al., 2008). IMDb.com and BoxOfficeMojo.com are the two data sources we used. We collected data on movie reviews from IMDb.com, the most popular and authoritative information source for movie reviews and ratings in the world, for approximately seven weeks following movie release dates. Then, we collected data regarding daily box office revenues, production budgets, distributor, and other movie information from BoxOfficeMojo.com. We sampled all films released from 2011 to 2016 on IMDB.com, obtaining 1317 movies. After removing movies with fewer than 100 reviews and those released for less than seven weeks (Rui & Whinston, 2011), we identified 349,269 reviews for 122 sample movies. We chose the threshold of 100 reviews to ensure sufficient reviews to train the DTM technique.

Our final sample movies are representative of all movies in the industry during our data period. Table 2 shows the comparison between the 122 movies used as our final sample and the entire dataset of 1317 movies released, indicating no significant differences in major film indexes except for movie votes, the thumb-ups given by online users. Obviously, movies with more reviews would be expected to also have more votes. Moreover, the production budget of our sample movies ranged from \$0.25 to \$245 million, with an average of

\$44.8 million. This average is very similar to the average movie budget in the film industry, which was \$42.5 million for all movies produced in the United States from 2008 to 2012. As shown in Table 3, our sample movies exhibit great diversity in terms of film distributors, movie genres, release month, and Motion Picture Association of America (MPAA) ratings.

Table 2. Descriptive Statistics for the Two Groups of Movies (122 vs. 1317)

<table><tr><td></td><td colspan="5">122 movies with over 100 reviews</td><td colspan="5">All 1317 movies</td><td colspan="2">Mean difference</td></tr><tr><td>Variable</td><td>Obs</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td><td>Obs</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td><td>diff</td><td>t</td></tr><tr><td>budget($m)</td><td>122</td><td>44.8</td><td>49.5</td><td>0.25</td><td>245</td><td>1317</td><td>48.3</td><td>42.7</td><td>0.1</td><td>250</td><td>3.7</td><td>0.84</td></tr><tr><td>revenue($m)</td><td>122</td><td>59.5</td><td>93.6</td><td>0.3</td><td>936</td><td>1317</td><td>48.2</td><td>79.7</td><td>0.2</td><td>936</td><td>-11.3</td><td>-1.61</td></tr><tr><td>time(min)</td><td>122</td><td>109</td><td>17.01</td><td>83</td><td>165</td><td>1317</td><td>108.2</td><td>16.4</td><td>66.0</td><td>180</td><td>-1.13</td><td>-0.72</td></tr><tr><td>Rating</td><td>122</td><td>6.56</td><td>0.85</td><td>4</td><td>9.1</td><td>1317</td><td>6.4</td><td>0.9</td><td>1.4</td><td>8.6</td><td>-0.13</td><td>-1.52</td></tr><tr><td>vote(m)</td><td>122</td><td>0.17</td><td>0.18</td><td>0.02</td><td>1.24</td><td>1317</td><td>0.1</td><td>0.2</td><td>0.0</td><td>1.4</td><td>-0.05***</td><td>-3.44</td></tr><tr><td>competition</td><td>122</td><td>13.9</td><td>3.5</td><td>2</td><td>20</td><td>1317</td><td>13.8</td><td>3.6</td><td>1</td><td>20</td><td>-0.08</td><td>-0.16</td></tr><tr><td>MPAA</td><td>122</td><td colspan="4">R:57 PG-13:50 PG:14 NC-17:1</td><td>1317</td><td colspan="4">R:665 PG-13:504 PG:139 NC-17:9</td><td></td><td></td></tr><tr><td colspan="13">Note: The budget, revenue and vote are in millions, and time is measured in minutes. Competition refers to the number of other movies released on the same day for each movie. *p &lt; 0.1; **p &lt; 0.05; ***p &lt; 0.01</td></tr></table>

Table 3. Movie Diversity

<table><tr><td>Distributor</td><td>Freq.</td><td>Genre</td><td>Freq.</td><td>Release Month</td><td>Freq.</td><td>MPAA ratings</td><td>Freq.</td></tr><tr><td>Warner Bros.</td><td>18</td><td>Drama</td><td>28</td><td>January</td><td>10</td><td>R</td><td>57</td></tr><tr><td>Lionsgate</td><td>16</td><td>Comedy</td><td>24</td><td>February</td><td>11</td><td>PG-13</td><td>50</td></tr><tr><td>Paramount</td><td>12</td><td>Thriller</td><td>12</td><td>March</td><td>12</td><td>PG</td><td>14</td></tr><tr><td>Weinstein</td><td>10</td><td>Action</td><td>11</td><td>April</td><td>7</td><td>NC-17</td><td>1</td></tr><tr><td>Fox</td><td>10</td><td>Sci-Fi</td><td>9</td><td>May</td><td>10</td><td>Total</td><td>122</td></tr><tr><td>Sony</td><td>9</td><td>Horror</td><td>8</td><td>June</td><td>6</td><td></td><td></td></tr><tr><td>Universal</td><td>7</td><td>Animation</td><td>8</td><td>July</td><td>7</td><td></td><td></td></tr><tr><td>Open Road Films</td><td>7</td><td>Crime</td><td>6</td><td>August</td><td>11</td><td></td><td></td></tr><tr><td>Focus Features</td><td>6</td><td>Fantasy</td><td>5</td><td>September</td><td>11</td><td></td><td></td></tr><tr><td>Roadside Attractions</td><td>6</td><td>Adventure</td><td>3</td><td>October</td><td>12</td><td></td><td></td></tr><tr><td>FilmDistrict</td><td>4</td><td>Sports</td><td>2</td><td>November</td><td>11</td><td></td><td></td></tr><tr><td>Relativity</td><td>4</td><td>Music</td><td>2</td><td>December</td><td>14</td><td></td><td></td></tr><tr><td>Buena Vista</td><td>4</td><td>Romance</td><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td>CBS Films</td><td>2</td><td>Documentary</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Bleecker Street</td><td>2</td><td>War</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>TriStar</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>A24</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Radius-TWC</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rogue Pictures</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/SMXMTZ7J/fulltext/images/54e8d60e955796736d91c1df4a6bb36c8a9be0dad7730a045a1a9c87c64fb06a.jpg)  
Figure 1. The Cumulative Distribution of Total Box Office Revenues

Table 4. Control Variables and Dependent Variable

<table><tr><td>Category</td><td>Variable</td><td>Definition (data source)</td></tr><tr><td>Dependent Variable</td><td>LogSales</td><td>Log transformation of the daily box office revenues (dollars; Box Office Mojo)</td></tr><tr><td rowspan="2">Numerical aspects of eWOM</td><td>LogVolume</td><td>Log transformation of the daily number of reviews (IMDb)</td></tr><tr><td>AvgRating</td><td>Average review ratings (IMDb)</td></tr><tr><td rowspan="3">Film factors</td><td>LogCinema</td><td>Log transformation of the daily number of cinemas for each movie (Box Office Mojo)</td></tr><tr><td>Weekend</td><td>=1 if the day falls on the weekend (Friday, Saturday, and Sunday), and 0 otherwise</td></tr><tr><td>Competition</td><td>The daily number of other movies released on the same day for each movie (IMDb)</td></tr><tr><td colspan="3">Notes: IMDb=Internet Movie Database. The time-invariant film-specific factors (i.e., genre, star power, studio, budget, MPAA, runtime, reward information) are not used as control variables because the film-specific effect will be controlled for in the estimation.</td></tr></table>

Given the opening week effect and the cumulative distribution of box office sales, we constructed a 21-day window for our panel dataset with a one-day time unit. For movies, word-of-mouth activities and box office revenues are generally highest during the opening week (Liu, 2006). As shown in Figure 1, 80% of films accumulate 80% of their total box office revenues in the first three weeks after release. Hence, the 21-day window following movie release dates provides a sufficient study period.

Before examining movie reviews’ textual information, we identified the important numerical aspects of eWOM and film factors to control for the effects of nonsentiment factors. Table 4 describes all the nonsentiment control variables and dependent variable used in our empirical analysis. Detailed descriptive statistics are presented in conjunction with sentiment information in the following section.

## 3.2 Dimension and Sentiment Mining

To understand the sentiment effects of eWOM, our research framework first extracts the key product dimensions from eWOM, deriving sentiments of these dimensions, and then analyzes their effects on sales and examines the moderating effect of product awareness (Figure 2).

For sentiment mining, we used an aspect-level sentiment analysis framework that integrates DTM, a sentiment lexicon, <sup>5</sup> the Stanford natural language processing (NLP) package (Socher et al., 2013), and a weighted sentiment algorithm to derive dimensionspecific sentiment from eWOM text. Figure 3 shows the flow of aspect-level sentiment analysis. Appendix A describes the details of the sentiment analysis. First, the review text was cleaned by removing non-English or stop words (Guo et al., 2017; Tirunillai & Tellis, 2014) as well as reviews that are full-form repetitions of other reviews. Second, we applied DTM (Blei & Lafferty, 2006) on the pooled review text of all 122 sample movies to identify the dimensions of products by extracting words describing each dimension and the weights of these words in the dimension. In applying DTM, we used the relative time of each film, i.e., the first day after the film was released was considered to be the first day of the data period, and so on.

Using DTM, we identified and labeled three movie dimensions: star, genre, and plot. According to the keywords for each dimension, star refers to movie actors and directors, genre reflects the movie category and type, and plot describes the storyline of the movie.

The three dimensions identified are consistent with the most important movie attributes examined in the literature (Ghiassi et al., 2015; Lash & Zhao, 2016). The optimal dimension number K = 3 was chosen based on both perplexity performance and interpretability (Li et al., 2019). Table 5 reports the top-10 words and their weights for each dimension. We then labeled the dimensions according to the logical connection among the most frequent words; the labels were confirmed by multiple experts. For example, we began with naming the third-dimension plot because the word plot, with a 0.5% weight, appeared at the top of the dimension word list (see Table 5). We further confirmed the name by examining its logical connection to other top words within the dimension. If we found a connection, we retained the dimension name; otherwise, we restarted the naming process.

![](/api/attachments/SMXMTZ7J/fulltext/images/3e274d696fd26351ca6388c074145c445696b26afdfa59186e2708e5ad3bbb08.jpg)  
Figure 2. Dimension-Specific Sentiment Effect Analysis Framework

![](/api/attachments/SMXMTZ7J/fulltext/images/5ecb46b7032378c5dd9442efad32f500a48d014fd7f68f83ce0081c640b7fa6a.jpg)  
Figure 3. Aspect-Level Sentiment Analysis Framework Flow  
Table 5. Dimensions and Top-10 Dimension Words Identified from DTM at a Time

<table><tr><td>Star</td><td>weight</td><td>genre</td><td>weight</td><td>plot</td><td>weight</td></tr><tr><td>cast</td><td>0.4%</td><td>comedy</td><td>0.5%</td><td>plot</td><td>0.5%</td></tr><tr><td>performance</td><td>0.3%</td><td>life</td><td>0.4%</td><td>story</td><td>0.4%</td></tr><tr><td>actor</td><td>0.3%</td><td>3d</td><td>0.3%</td><td>book</td><td>0.4%</td></tr><tr><td>tom</td><td>0.3%</td><td>family</td><td>0.3%</td><td>horror</td><td>0.3%</td></tr><tr><td>leonardo</td><td>0.3%</td><td>love</td><td>0.3%</td><td>dark</td><td>0.2%</td></tr><tr><td>glass</td><td>0.3%</td><td>short</td><td>0.2%</td><td>original</td><td>0.2%</td></tr><tr><td>acting</td><td>0.2%</td><td>joke</td><td>0.2%</td><td>scary</td><td>0.2%</td></tr><tr><td>oscar</td><td>0.2%</td><td>job</td><td>0.2%</td><td>maze</td><td>0.2%</td></tr><tr><td>director</td><td>0.2%</td><td>school</td><td>0.2%</td><td>pretty</td><td>0.2%</td></tr><tr><td>action</td><td>0.2%</td><td>market</td><td>0.2%</td><td>house</td><td>0.2%</td></tr></table>

![](/api/attachments/SMXMTZ7J/fulltext/images/c87419762a2ed0625e380b77ad9bc1bb2615a51feb0cc60dca4fb58eb03aa847.jpg)  
Figure 4. The Temporal Evolution of Topics

DTM is appropriate for our study because it can extract important product dimensions and their changes over time, including changes in keywords (e.g., the topic words listed in Table 5) and their weights within each dimension. Therefore, our method dimension mining method is able to identify the temporal evolution in review topics. Figure 4 plots the weights of all topic words on each dimension over time, showing that movie reviews are mostly about stars in the opening week and movie plot later on. The proportion of review content devoted to movie genres was relatively small and stable. To account for the temporal influence of review topics, we also obtained each dimension loading as the proportion of the number of its dimension words among the total number of words of all dimensions in daily reviews.

We then used the Stanford NLP package to extract the syntactic relationships between dimension words and words of the sentiment lexicon (i.e., sentiment words) from every review sentence. For each dimension, we calculated the dimension sentiment as the weighted sum of the sentiment values of all its sentiment words. These dimension-specific sentiments normalized to range from 0 to 1 are used to analyze the effects of dimension-specific sentiments on movie box office revenues. For most sample movies, the sentiment varies significantly across dimensions. Figure 5 plots the average sentiments of the star, genre, and plot dimensions for our sample movies. Table 6 describes all sentiment variables, and Table 7 presents their summary statistics in conjunction with other variables. Based on the the median movie production budget (\$30 million), we divided movies into a high-budget group (68 movies) and a low-budget group (54 movies). Their summary statistics are presented in Table 8.

![](/api/attachments/SMXMTZ7J/fulltext/images/2b557160fcfdd7cc62759dea3be7d3fbbe11980bc6f92cf7c70d3de49ce0ba15.jpg)  
Figure 5. Average Dimension-Specific Sentiments across All Sample Movies Over Time

Table 6. Description of Sentiment Variables

<table><tr><td>Variable</td><td>Description (Measures)</td></tr><tr><td>Star</td><td>The total sentiment of star dimension expressed in daily eWOM (normalized, 0 to 1)</td></tr><tr><td>Genre</td><td>The total sentiment of genre dimension expressed in daily eWOM (normalized, 0 to 1)</td></tr><tr><td>Plot</td><td>The total sentiment of plot dimension expressed in daily eWOM (normalized, 0 to 1)</td></tr><tr><td>Star_loadings</td><td>The proportion of star topic words to the total number of topic words expressed in daily eWOM (0 to 1)</td></tr><tr><td>Genre_loadings</td><td>The proportion of genre topic words to the total number of topic words expressed in daily eWOM (0 to 1)</td></tr><tr><td>Plot_loadings</td><td>The proportion of plot topic words to the total number of topic words expressed in daily eWOM (0 to 1)</td></tr></table>

Table 7. Summary Statistics of Key Variables

<table><tr><td>Variable</td><td>Obs</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td></tr><tr><td>LogSale</td><td>2562</td><td>12.28</td><td>1.64</td><td>2.30</td><td>17.38</td></tr><tr><td>genre</td><td>2562</td><td>0.62</td><td>0.09</td><td>0.00</td><td>1.00</td></tr><tr><td>plot</td><td>2562</td><td>0.60</td><td>0.13</td><td>0.00</td><td>1.00</td></tr><tr><td>star</td><td>2562</td><td>0.65</td><td>0.09</td><td>0.00</td><td>1.00</td></tr><tr><td>LogVolume</td><td>2562</td><td>2.66</td><td>0.64</td><td>0.69</td><td>4.66</td></tr><tr><td>LogCinema</td><td>2562</td><td>6.88</td><td>2.00</td><td>0.69</td><td>8.37</td></tr><tr><td>weekend</td><td>2562</td><td>0.43</td><td>0.50</td><td>0.00</td><td>1.00</td></tr><tr><td>rating</td><td>2562</td><td>6.69</td><td>1.30</td><td>0.00</td><td>10.00</td></tr><tr><td>genre_load</td><td>2562</td><td>0.40</td><td>0.31</td><td>0.00</td><td>1.00</td></tr><tr><td>plot_load</td><td>2562</td><td>0.36</td><td>0.29</td><td>0.00</td><td>1.00</td></tr><tr><td>star_load</td><td>2562</td><td>0.21</td><td>0.25</td><td>0.00</td><td>1.00</td></tr><tr><td>competition</td><td>2562</td><td>14.25</td><td>4.42</td><td>3.00</td><td>21.00</td></tr></table>

Table 8. Summary Statistics for High-Budget vs. Low-Budget movies

<table><tr><td></td><td colspan="5">High-budget movies (N=68)</td><td colspan="5">Low-budget movies (N=54)</td></tr><tr><td></td><td>Obs</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td><td>Obs</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td></tr><tr><td>Logsale</td><td>1428</td><td>12.30</td><td>1.66</td><td>4.26</td><td>17.38</td><td>1134</td><td>12.24</td><td>1.62</td><td>2.30</td><td>14.53</td></tr><tr><td>genre</td><td>1428</td><td>0.61</td><td>0.09</td><td>0.26</td><td>0.95</td><td>1134</td><td>0.62</td><td>0.01</td><td>0.00</td><td>1.00</td></tr><tr><td>plot</td><td>1428</td><td>0.59</td><td>0.12</td><td>0.00</td><td>0.90</td><td>1134</td><td>0.61</td><td>0.14</td><td>0.30</td><td>1.00</td></tr><tr><td>star</td><td>1428</td><td>0.67</td><td>0.08</td><td>0.00</td><td>1.00</td><td>1134</td><td>0.63</td><td>0.10</td><td>0.21</td><td>0.95</td></tr><tr><td>Logvolume</td><td>1428</td><td>2.71</td><td>0.65</td><td>1.10</td><td>4.66</td><td>1134</td><td>2.58</td><td>0.62</td><td>0.69</td><td>4.25</td></tr><tr><td>Logcinema</td><td>1428</td><td>7.40</td><td>1.71</td><td>1.39</td><td>8.37</td><td>1134</td><td>6.22</td><td>2.15</td><td>0.69</td><td>8.14</td></tr><tr><td>weekend</td><td>1428</td><td>0.43</td><td>0.50</td><td>0.00</td><td>1.00</td><td>1134</td><td>0.43</td><td>0.50</td><td>0.00</td><td>1.00</td></tr><tr><td>rating</td><td>1428</td><td>7.07</td><td>1.18</td><td>1.00</td><td>9.75</td><td>1134</td><td>6.22</td><td>1.30</td><td>0.00</td><td>10.00</td></tr><tr><td>genre_load</td><td>1428</td><td>0.38</td><td>0.31</td><td>0.00</td><td>1.00</td><td>1134</td><td>0.42</td><td>0.31</td><td>0.00</td><td>1.00</td></tr><tr><td>plot_load</td><td>1428</td><td>0.37</td><td>0.29</td><td>0.00</td><td>1.00</td><td>1134</td><td>0.35</td><td>0.29</td><td>0.00</td><td>1.00</td></tr><tr><td>star_load</td><td>1428</td><td>0.23</td><td>0.24</td><td>0.00</td><td>1.00</td><td>1134</td><td>0.20</td><td>0.26</td><td>0.00</td><td>1.00</td></tr><tr><td>competiton</td><td>1428</td><td>14.44</td><td>4.30</td><td>3.00</td><td>21.00</td><td>1134</td><td>14.02</td><td>4.56</td><td>3.00</td><td>21.00</td></tr></table>

## 3.3 Hypotheses Development

After applying an aspect-level sentiment analysis framework to movie reviews, we obtained three movie dimensions: star, genre and plot sentiment. Star concerns movie actors and directors, genre refers to the movie category and type, and plot describes the storyline of the movie. According to multi-attribute attitude theory, potential consumers’ overall preference for a movie is affected jointly by their evaluation of the movie in each dimension and their preference for that dimension. While the former is reflected by the dimension-specific sentiment, the latter measures the importance of the dimension in the consumer’s evaluation. Given the importance of the attribute in product evaluation, since all three attributes are emphasized in eWOM, consumers would split their limited attention across these attributes (Zhu & Dukes, 2017).

As an experience product, the quality of a movie cannot be fully evaluated before consumption, in contrast to many search products (i.e., mobile phones). Consumers perceive the purchase of a product with high levels of uncertainty concerning quality and performance as risky (Ho-dac et al., 2013). In order to reduce the risk, consumers tend to search for more information to better assess movies, especially in terms of movie attributes in which they are more interested. Movie reviews include prior consumers’ opinions about a movie, which can supplement insufficient quality signals for the movie. In general, higher sentiment in a movie dimension implies higher quality or performance of the movie with respect to that dimension, according to previous consumers. Therefore, higher dimension-specific sentiments should lead to consumers’ higher evaluation of a movie and thus to higher likelihood of purchase. This applies to all three dimensions of star, genre, and plot. Hence, we hypothesize as follows:

H1a: Star sentiment in movie reviews is positively related to box office revenue.

H1b: Genre sentiment in movie reviews is positively related to box office revenue.

H1c: Plot sentiment in movie reviews is positively related to box office revenue.

According to context-dependent consumer preferences, consumers may have different sentiment preferences for high- and low-budget movies. That is, the relative importance of the three dimension-specific sentiments is affected by movie budget. For potential consumers, production budget reflects the production cost of the film, which is a highly important signal from the marketer.

Among the three dimensions identified, the difference between high- and low-budget movies mostly lies in the star dimension. A-list movie stars routinely make \$15 million to \$20 million for top roles in big-budget films, whereas lesser-known actors like Gal Gadot in Wonder Woman or Henry Cavill in Man of Steel might only earn \$150,000 to \$300,000 for their roles in a lowbudget production. <sup>6</sup> Therefore, high-budget movies usually feature big-name stars (De Vany & Walls, 1999; Holbrook & Addis, 2008), whereas low-budget movies can likely only afford lesser-known actors. Because attributes that are more prominent in the market environment for the product are more likely to be recalled and used for the product evaluation (Gardner, 1983; Johnson et al., 1988; Tversky et al., 1988; Shavitt & Fazio, 1991), star dimension would be more important than plot and genre dimensions in the evaluation of high-budget movies.

Moreover, high-budget movies often advertise their star actors in prerelease marketing efforts, and consumers may only check reviews of a movie because they are attracted by the featured stars. Thus, highbudget movies create a higher consumer focus on star sentiment in reviews than on plot and genre sentiments, meaning that positive star sentiment will likely be more persuasive than plot or genre sentiments for consumers attracted to high-budget movies featuring major celebrities (Karniouchina, 2011). Hence, we hypothesize:

H2a: For high-budget movies, the positive relationship with box office revenue is stronger for star sentiment than for plot and genre sentiments.

The opposite is true low-budget movies. Compared with high-budget movies already providing substantial quality assurances (i.e., product costs, star power), low-budget movies lack credible brand signals and thus their online reviews play a more important role in convincing consumers of movie quality (Holbrook & Addis, 2008; Aggarwal et al., 2012). Low-budget movies are often less able to afford actors with star power than high-budget movies. Consumers attracted to low-budget movies would thus pay less attention to the star dimension in reviews. Instead, they would focus more on the story of the film itself (i.e., plots, genres). Thus, for low-budget movies, the persuasion effect of plot or genre sentiments is stronger than that of star sentiment. Hence, we hypothesize:

H2b: For low-budget movies, the positive relationship with box office revenue is stronger for plot and genre sentiments than star sentiment.

## 3.4 Empirical Model and Estimation

We model the interrelationship between eWOM and movie box office revenues using a panel vector autoregression (PVAR) model. The PVAR model addresses the endogeneity issue caused by two-way relationships between online reviews and product sales by letting each variable be a linear function of its own lagged terms and the lags of other endogenous variables (Ho-dac et al., 2013). It is an appropriate model for our context for three reasons: (1) The multivariate equation system treats all variables as endogenous and interdependent and thus can yield unbiased estimation of the interactions between eWOM and sales; (2) The dynamics between the variables can be assessed and visualized through by means of impulse response and forecast-error variance decomposition (Love & Zicchino, 2006; Song et al., 2019); (3) This model includes panel-fixed effects to address unobserved time-invariant heterogeneity across movies. Specifically, we employ and specify the PVAR model as follows:

$$
\begin{array}{r} \left( \begin{array}{c} s a l e _ {i t} \\ s t a r _ {i t} \\ g e n r e _ {i t} \\ p l o t _ {i t} \end{array} \right) = \sum_ {j = 1} ^ {m} \Phi_ {j} \cdot \left( \begin{array}{c} s a l e _ {i t - j} \\ s t a r _ {i t - j} \\ g e n r e _ {i t - j} \\ p l o t _ {i t - j} \end{array} \right) + \beta_ {1} v o l u m e + \beta_ {2} c i n e m a + \beta_ {3} r a t i n g + \beta_ {4} w e e k e n d + \\ \beta_ {5} c o m p e t i t i o n + \beta_ {6} s t a r l o a d + \beta_ {7} g e n r e l o a d + \beta_ {8} p l o t l o a d + f _ {t} + u _ {i} + \varepsilon_ {i t}, \end{array}\tag{2}
$$

where Φ are $4 \times 4$ matrices of slope coefficients for box office and sentiment variables. i, and t stand for movie and time (day), respectively; star, genre and plot represent the dimension sentiments of star, gender, and plot expressed in daily reviews, respectively. ?? is the number of lags included, indicating the number of past periods that affect the current period. Volume is the log transformation of the daily number of reviews; cinema is the log transformation of the daily number of cinemas screening; rating is the average review rating; weekend indicates whether the release day falls on the weekend (Friday, Saturday, and Sunday); and competition is the daily number of other movies released on the same day. starload is the proportion of star topic words to the total number of topic words expressed in daily reviews, as are genre and plot; $u _ { i }$ represents fixed effects capturing time-invariant movie characteristics such as genre, star power, studio, budget, MPAA, and runtime. $f _ { t }$ represents timespecific effects, and $\varepsilon _ { i t }$ is the idiosyncratic error term.

Table 9. Optimal Lag Length Selection

<table><tr><td colspan="4">Full sample (N=122)</td><td colspan="4">High-budget movies (N=68)</td><td colspan="4">Low-budget movies (N=54)</td></tr><tr><td>lag</td><td>AIC</td><td>BIC</td><td>HQIC</td><td>lag</td><td>AIC</td><td>BIC</td><td>HQIC</td><td>lag</td><td>AIC</td><td>BIC</td><td>HQIC</td></tr><tr><td>1</td><td>-3.87</td><td>-2.52*</td><td>-3.38*</td><td>1</td><td>-4.02</td><td>-2.75*</td><td>-3.54</td><td>1</td><td>-4.07*</td><td>-2.96*</td><td>-3.65*</td></tr><tr><td>2</td><td>-3.90*</td><td>-2.45</td><td>-3.37</td><td>2</td><td>-4.10*</td><td>-2.70</td><td>-3.57*</td><td>2</td><td>-3.98</td><td>-2.74</td><td>-3.51</td></tr><tr><td>3</td><td>-3.84</td><td>-2.26</td><td>-3.26</td><td>3</td><td>-4.02</td><td>-2.48</td><td>-3.44</td><td>3</td><td>-3.82</td><td>-2.44</td><td>-3.29</td></tr><tr><td>4</td><td>-3.77</td><td>-2.06</td><td>-3.14</td><td>4</td><td>-3.75</td><td>-2.05</td><td>-3.11</td><td>4</td><td>-3.47</td><td>-1.93</td><td>-2.88</td></tr><tr><td>5</td><td>-3.76</td><td>-1.91</td><td>-3.08</td><td>5</td><td>-3.69</td><td>-1.81</td><td>-2.97</td><td>5</td><td>-3.18</td><td>-1.46</td><td>-2.52</td></tr><tr><td colspan="12">Note: * denote significance at 5%</td></tr></table>

Table 10. Panel Unit Roots for Full Sample, High-Budget, and Low-Budget Movies

<table><tr><td>Test</td><td>LLC</td><td>BT</td><td>HT</td><td>IPS</td><td>ADF-F</td><td>Hadri LM</td><td rowspan="2">Result</td></tr><tr><td>Statistics</td><td>Adj.t</td><td>lambda</td><td>z</td><td>Z</td><td>Pm</td><td>z</td></tr><tr><td colspan="8">Full sample (N=122)</td></tr><tr><td>sale</td><td>-13.04</td><td>-7.30</td><td>-32.31</td><td>-13.31</td><td>35.01</td><td>40.74</td><td>stationary</td></tr><tr><td>star</td><td>-17.16</td><td>-18.57</td><td>-62.18</td><td>-21.94</td><td>75.00</td><td>7.68</td><td>stationary</td></tr><tr><td>genre</td><td>-14.78</td><td>-22.18</td><td>-59.71</td><td>-21.53</td><td>65.85</td><td>10.84</td><td>stationary</td></tr><tr><td>plot</td><td>-13.14</td><td>-9.67</td><td>-28.22</td><td>-13.36</td><td>25.62</td><td>42.82</td><td>stationary</td></tr><tr><td colspan="8">High-budget movies (N=68)</td></tr><tr><td>sale</td><td>-13.74</td><td>-9.69</td><td>-32.64</td><td>-13.82</td><td>36.97</td><td>19.62</td><td>stationary</td></tr><tr><td>star</td><td>-10.98</td><td>-15.00</td><td>-46.58</td><td>-16.29</td><td>48.78</td><td>7.89</td><td>stationary</td></tr><tr><td>genre</td><td>-9.22</td><td>-16.36</td><td>-43.15</td><td>-15.07</td><td>41.92</td><td>12.76</td><td>stationary</td></tr><tr><td>plot</td><td>-11.84</td><td>-7.72</td><td>-21.44</td><td>-10.74</td><td>20.81</td><td>30.02</td><td>stationary</td></tr><tr><td colspan="8">Low-budget movies (N=54)</td></tr><tr><td>sale</td><td>-7.49</td><td>-2.07</td><td>-10.07</td><td>-4.49</td><td>11.13</td><td>40.93</td><td>stationary</td></tr><tr><td>star</td><td>-12.45</td><td>-11.08</td><td>-24.64</td><td>-15.48</td><td>46.33</td><td>6.03</td><td>stationary</td></tr><tr><td>genre</td><td>-9.11</td><td>-11.95</td><td>-24.27</td><td>-16.03</td><td>40.54</td><td>1.19</td><td>stationary</td></tr><tr><td>plot</td><td>-6.62</td><td>-5.68</td><td>-14.87</td><td>-11.55</td><td>17.83</td><td>6.93</td><td>stationary</td></tr><tr><td colspan="8">Note: we omit figures with a significance level less than 0.05, given the readability of the table.</td></tr></table>

Table 11. Granger Causality Tests

<table><tr><td>Equation</td><td>Excluded</td><td colspan="2">All movies (N=122)</td><td colspan="2">High-budget movies (N=68)</td><td colspan="2">Low-budget movies (N=54)</td></tr><tr><td>sale</td><td>star</td><td>28.54***</td><td>&lt;0.001</td><td>18.83***</td><td>&lt;0.001</td><td>8.76***</td><td>0.003</td></tr><tr><td>sale</td><td>genre</td><td>27.23***</td><td>&lt;0.001</td><td>7.38***</td><td>0.007</td><td>9.64***</td><td>0.002</td></tr><tr><td>sale</td><td>plot</td><td>16.86***</td><td>&lt;0.001</td><td>5.50**</td><td>0.019</td><td>6.67**</td><td>0.01</td></tr><tr><td>sale</td><td>ALL</td><td>35.34***</td><td>&lt;0.001</td><td>19.69***</td><td>&lt;0.001</td><td>12.01***</td><td>0.007</td></tr><tr><td colspan="8">Note: ***, **, and * denote significance at 1%, 5%, and 10%, respectively.</td></tr></table>

We estimate the PVAR model using a system generalized method of moments (SGMM), where the lagged regressors are used as instruments. GMM estimation does not make distributional assumptions on the data and controls for heteroscedasticity and temporal autocorrelation in the error terms. GMM is selected instead of the within-group estimator for the fixed-effects model because the latter will be biased for dynamic panel models (Arellano, 2003; Chen & Liao, 2015).

Impulse-response functions (IRFs) are used to describe the change in one variable in response to the changes in other variables in the system (Abrigo & Love, 2016). Specifically, IRFs capture the dynamics of carryover effects over time (Love & Zicchino, 2006) and can be used to measure the short- and long-term impacts. Moreover, we can use IRFS to separate the response of movie sales to shocks coming from different dimension-specific sentiments (Tirunillai & Tellis, 2014).

## 4 Empirical Results

## 4.1 Model Validity Tests

We select the optimal lag length, ??, according to the information criterion, namely the Akaike information criteria (AIC) (Akaike, 1969), the Bayesian information criteria (BIC) (Schwarz, 1978; Rissanen, 1978), and the Hannan-Quinn information criteria (HQIC) (Hannan & Quinn, 1979). We first specify the model with a reasonably long length of lags (i.e., 5 periods) and conduct a downward testing procedure. As shown in Table 9, the optimal lag length is selected to be 1.

The PVAR model requires all endogenous variables to be stationary such that the effects of an unexpected change in endogenous variables ultimately dissipate (Luo et al., 2017). We conduct six panel unit root tests to check stationarity, including Levin-Lin-Chu test (LLC), Breintung (BT), Harris-Tzavalis test (HT), Im-Pesaran-Skin test (IPS), Fisher-ADF (ADF-F) and Hadri LM test. The first three are homogeneous unit root tests, while the latter three are heterogeneous unit root tests. As reported in Table 10, all six tests show that all the endogenous variables are stationary.

Lastly, the PVAR model also requires Granger causality between the endogenous variables, demonstrating that the variables indeed contribute to the future changes of other variables. Therefore, we conducted Granger causality tests between dimension sentiments and movie sales (Granger 1969). As shown in Table 11, all the three-dimension sentiments significantly Granger-cause movie sales both individually and jointly.

## 4.2 Results

We combine the SGMM estimation and IRFs to derive empirical results. In order to compare the sentiment preferences for different dimensions within the highand low-budget movies, we carry out an intragroup experiment (Love & Zicchino, 2006). In SGMM estimation, to preserve the orthogonality between transformed variables and lagged regressors, we utilize forward mean-differencing (the “Helmert procedure”) to remove fixed effects, and the mean difference within groups to remove time-specifc effects (Love & Zicchino, 2006; Song et al., 2019). When analyzing IRFs, standard errors are derived based on the fitted PVAR model using Monte Carlo simulation with 1,000 runs to test the statistical significance of parameters (p = 0.05) (Luo et al., 2017).

Although the PVAR model can reveal the dynamic interrelationships between all endogenous variables, we only report the estimation results of the effects of review sentiments (star, genre, plot) on box office revenue, given the focus of our study. Table 12 presents the coefficient estimates for the full sample, high-budget movies, and low-budget movies. Column A of Table 12 indicates that all three dimension-specific sentiments (star, genre, and plot) are positively associated with box office revenue and all three positive relationships are statistically significant. That is, the higher the dimension sentiment, the higher the movie box office revenue. Thus H1a, H1b, and H1c are supported. This result suggests that the three movie dimensions identified through our sentiment mining method are all important movie attributes that influence consumers’ movie-going decisions. The subsample estimations on high-budget and low-budget movies (Column B and C) further confirm the persuasive effects of review sentiments.

The results of impulse response functions also support the persuasive effects of dimension-specific sentiments and show the effects dynamically over time. As illustrated in Figure 6, with one unexpected shock in star sentiment, movie sales will immediately increase the most on the next day or two and then slowly decrease in the following week (Figure 6-a1), demonstrating that the relationship between star sentiment and sales is positive and persistent. Similar patterns are observed in the responses of product sales to shocks in genre sentiment and plot sentiment (Figure 6-a2, Figure 6-a3), which indicate that movie sales are affected by the dimensionsentiments of not only the most recent reviews but also earlier ones, with the most recent reviews having the strongest influence. The finding demonstrating the positive effects of star sentiment extends previous studies that found star power to be important for box office revenues (Nelson & Glotfelty, 2012).

There is a significant difference in the effects of dimension-specific sentiments between the two groups (high-budget vs. low-budget movies). Column B of

Table 12 reports that star sentiment has a stronger effect on sales than plot sentiment (t = 10.93, and $p = 0 . 0 0 0 9 )$ and genre sentiment $( t \ : = \ : 1 1 . 9 1 , \ : p \ : = \ : 0 . 0 0 0 6 )$ , with statistically significant differences. That is, for highbudget movies, the positive relationship between star sentiment and movie box office revenue is stronger than that between plot or genre sentiment and revenue. H2a is thus supported, suggesting that consumers have higher sentiment preferences for star sentiment than for plot and genre sentiments for high-budget movies. Column C in Table 12 indicates that plot and genre sentiments have stronger effects on sales than star sentiment for low-budget movies. Meanwhile, the different effects on movie sales are demonstrated by the t-tests of the coefficient differences (star vs. plot: t = 2.95, p = 0.08; star vs. genre: t = 0.34, p = 0.55). That is, for low-budget movies, the positive relationship between the plot sentiment and the movie box office revenue is stronger than that between star sentiment and box office revenue. This result partially supports H2b, indicating that consumers have higher sentiment preferences for plot sentiment than for star sentiment.

Table 12. SGMM Estimation Results for Full Sample, High-Budget Movies, and Low-Budget Movies

<table><tr><td></td><td colspan="2">(A) Full sample</td><td colspan="2">(B) High-budget movies</td><td colspan="2">(C) Low-budget movies</td></tr><tr><td>Sale</td><td>Coefficient</td><td>z</td><td>Coefficient</td><td>z</td><td>Coefficient</td><td>z</td></tr><tr><td>Lag.sale</td><td>0.599***</td><td>-7.5</td><td>0.361***</td><td>-4.52</td><td>1.087***</td><td>-4.27</td></tr><tr><td>Lag.star</td><td>2.931***</td><td>-4.75</td><td>2.722***</td><td>-3.84</td><td>3.592***</td><td>-2.87</td></tr><tr><td>Laggenre</td><td>2.192***</td><td>-4.74</td><td>1.050**</td><td>-2.5</td><td>3.258***</td><td>-3.02</td></tr><tr><td>Lag.plot</td><td>3.263***</td><td>-4.24</td><td>1.681**</td><td>-2.3</td><td>5.350**</td><td>-2.44</td></tr><tr><td>Volume</td><td>0.154***</td><td>-2.66</td><td>-0.021</td><td>-0.29</td><td>0.228**</td><td>-2.51</td></tr><tr><td>Cinema</td><td>0.014</td><td>-0.26</td><td>0.096*</td><td>-1.72</td><td>0.183</td><td>-1.1</td></tr><tr><td>Rating</td><td>0.938***</td><td>-3.71</td><td>0.800***</td><td>-2.7</td><td>0.899</td><td>-1.6</td></tr><tr><td>Weekend</td><td>0.213***</td><td>-4.39</td><td>0.169**</td><td>-2.54</td><td>0.258***</td><td>-3.23</td></tr><tr><td>Competition</td><td>0.289**</td><td>-2.43</td><td>0.329*</td><td>-1.73</td><td>0.164</td><td>-1.08</td></tr><tr><td>star_load</td><td>0.926***</td><td>-3.38</td><td>0.593**</td><td>-2.13</td><td>1.076**</td><td>-2.04</td></tr><tr><td>plot_load</td><td>1.079***</td><td>-3.99</td><td>0.662**</td><td>-2.56</td><td>1.266**</td><td>-2.33</td></tr><tr><td>#Obs</td><td colspan="2">2318</td><td colspan="2">1292</td><td colspan="2">1026</td></tr><tr><td colspan="7">Note: Volume, cinema, rating, weekend, competition, star loadings, and plot loadings are a set of control variables, and the estimation drops the</td></tr></table>

![](/api/attachments/SMXMTZ7J/fulltext/images/0f4608ae3ab3b59c88219ddf8bfd3ac3288adde471030db6c147c52ce8150516.jpg)  
Note: The X-axis represents response periods (day), and the Y-axis indicates the response of the endogenous response variable to one standard deviation shocks in the impulse variable. The middle solid line indicates the trend of the specific impact. the dashed line represents confidence intervals (5 to 95 percentile). For example, “IRF of sale to star” indicates that the impulse-response of product sales to one standard deviation change in star sentiment.  
Figure 6. Impulse Responses for Full Sample

![](/api/attachments/SMXMTZ7J/fulltext/images/8f7c4279823d15d64384f5fc472838fcfaebc23057404b56cf7be4056b380055.jpg)

![](/api/attachments/SMXMTZ7J/fulltext/images/418cf18ec0e8edc602e831d1c0e7334795c420a8498967308582d998eb258f84.jpg)  
Note: The middle solid line indicates the trend of the specific impact, the dashed line represents confidence intervals, and the horizontal dotted line represents the zero line. The first row shows the impact of different dimensions sentiments on box office revenue for high-budget movies (b1, b2, b3), and the second row for low-budget movies (c1, c2, c3).  
Figure 7. Impulse Responses for High- and Low-Budget Movies

The subsample results of impulse response on highbudget and low-budget movies (Figure 7) further confirm these findings. The first line (b1, b2, b3) shows that star sentiment has a greater coefficient on box office revenues, indicating that it has a greater impact than plot and genre sentiments. A similar pattern is observed in the second line (c1, c2, c3). Plot genre has a greater coefficient on box office revenues, indicating that it has a greater impact than star sentiment. Although the impact coefficient of genre and star sentiment is not different, genre sentiment is still larger than star sentiment.

## 4.3 Robustness Checks

DTM is appropriate for our study because it can extract important product dimensions and their changes over time, including changes in keywords and their weights within each dimension. Although DTM can identify topic evolution over time, it may pick up more noise in the data than LDA. As a robustness check, we used LDA instead of DTM to extract key dimensions and calculated dimension sentiments, and reestimated the sentiment effects using the LDA results. The summary statistics for sentiment variables mined using LDA are presented in Table 12. After passing model validity tests, the PVAR estimation results are shown in Table 13. The results remain consistent with the main results using DTM, and all the hypotheses are supported.

We also conducted several additional robustness checks to further confirm our results. First, as an alternative model specification, we carry out the fixedeffects model estimation instead of PVAR. Second, to verify the stability of the model results under different lag lengths, we estimate the model with two-period lags in the PVAR model. Lastly, some exogenous variables in our PVAR model such as review volume and rating may also be endogenous. In an additional robustness check, they are included as additional endogenous variables. Throughout these robustness checks, our results remain consistent with the main results in Table 12. The detailed estimations and results are given in Appendix B.

Table 13. Summary Statistics of Sentiment Variables

<table><tr><td>Variable</td><td>Obs</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td></tr><tr><td colspan="6">Full sample (N=122)</td></tr><tr><td>genre</td><td>2562</td><td>0.64</td><td>0.10</td><td>0</td><td>1</td></tr><tr><td>plot</td><td>2562</td><td>0.60</td><td>0.13</td><td>0</td><td>1</td></tr><tr><td>star</td><td>2562</td><td>0.58</td><td>0.10</td><td>0</td><td>1</td></tr><tr><td colspan="6">High-budget movies (N=68)</td></tr><tr><td>genre</td><td>1428</td><td>0.64</td><td>0.10</td><td>0.3</td><td>1</td></tr><tr><td>plot</td><td>1428</td><td>0.58</td><td>0.13</td><td>0</td><td>0.88</td></tr><tr><td>star</td><td>1428</td><td>0.60</td><td>0.08</td><td>0.21</td><td>1</td></tr><tr><td colspan="6">Low-budget movies (N=54)</td></tr><tr><td>genre</td><td>1134</td><td>0.65</td><td>0.09</td><td>0</td><td>1</td></tr><tr><td>plot</td><td>1134</td><td>0.61</td><td>0.14</td><td>0.29</td><td>1</td></tr><tr><td>star</td><td>1134</td><td>0.55</td><td>0.11</td><td>0</td><td>0.91</td></tr></table>

Table 14. Sentiment Effects Estimation with LDA Analysis

<table><tr><td></td><td colspan="2">(A)Full sample</td><td colspan="2">(B) High-budget movies</td><td colspan="2">(C) Low-budget movies</td></tr><tr><td>Sale</td><td>Coefficient</td><td>z</td><td>Coefficient</td><td>Z</td><td>Coefficient</td><td>z</td></tr><tr><td>Lag.sale</td><td>0.541***</td><td>-6.97</td><td>0.364***</td><td>-4.53</td><td>0.899***</td><td>-4.06</td></tr><tr><td>Lag.star</td><td>2.238***</td><td>-4.57</td><td>2.131***</td><td>-3.22</td><td>2.626***</td><td>-2.94</td></tr><tr><td>Lag.genre</td><td>2.063***</td><td>-4.76</td><td>1.100***</td><td>-2.62</td><td>2.948***</td><td>-3.16</td></tr><tr><td>Lag.plot</td><td>2.995***</td><td>-4.54</td><td>1.746***</td><td>-2.63</td><td>4.115**</td><td>-2.53</td></tr><tr><td>volume</td><td>0.146***</td><td>-2.61</td><td>0.001</td><td>-0.01</td><td>0.227***</td><td>-2.7</td></tr><tr><td>cinema</td><td>-0.002</td><td>-0.05</td><td>0.084</td><td>-1.51</td><td>0.111</td><td>-0.77</td></tr><tr><td>rating</td><td>0.907***</td><td>-3.74</td><td>0.820***</td><td>-2.77</td><td>0.959*</td><td>-1.88</td></tr><tr><td>weekend</td><td>0.222***</td><td>-4.71</td><td>0.189***</td><td>-2.8</td><td>0.246***</td><td>-3.58</td></tr><tr><td>competition</td><td>0.303**</td><td>-2.54</td><td>0.336*</td><td>-1.72</td><td>0.240*</td><td>-1.67</td></tr><tr><td>star_load</td><td>0.869***</td><td>-3.38</td><td>0.642**</td><td>-2.32</td><td>0.954**</td><td>-2.02</td></tr><tr><td>plot_load</td><td>1.008***</td><td>-4.02</td><td>0.719***</td><td>-2.8</td><td>1.113**</td><td>-2.32</td></tr><tr><td>#Obs</td><td colspan="2">2318</td><td colspan="2">1292</td><td colspan="2">1026</td></tr></table>

Note: Volume, cinema, rating, weekend, competition, star loadings, and plot loadings are a set of control variables, and the estimation drops the genre loadings variable because of the collinearity. The lag length for all lag variables is 1. \*\*\*, \*\*, and \* denote significance at 1%, 5%, and 10%, respectively.

## 5 Discussion and Conclusion

To summarize, this study investigates the persuasive effect of eWOM—specifically, how dimension-specific sentiments affect product sales. Consumers have different preferences for different product attributes. Similarly, consumers are influenced differently by eWOM sentiments of different product dimensions. Therefore, we introduce consumers’ sentiment preferences into this study of the sentiment effects of eWOM. Using an aspect-level sentiment analysis framework, we first extracted important product dimensions and calculated the dimension-specific sentiments from the review text, and then estimated how these dimension sentiments are associated with sales.

Our research has several notable findings. First, we found that three dimension-specific sentiments (star, genre, and plot) are positively associated with movie sales. The higher the sentiment preference of a dimension, the more persuasive the eWOM sentiment of that dimension. Second, one of the more significant findings to emerge from this study is that movie production budget moderates consumers’ sentiment preferences. Specifically, we found that for high-budget movies, the positive relationship with box office revenue is stronger for star sentiment than for plot and genre sentiments. For low-budget movies, the positive relationship with box office revenue is stronger for plot sentiment than for star sentiment. This finding demonstrates the interaction between brand-released product signaling and the signals revealed in eWOM. In particular, when brand-released information emphasizes certain product attributes, it also increases the influence of eWOM regarding those attributes.

## 5.1 Implications for Research

This paper enriches our understanding of the persuasive effect of eWOM and offers several important theoretical contributions. First, to the best of our knowledge, this is the first study to propose sentiment preferences and utilize this concept to explain why the sentiment information in eWOM along different product dimensions has different effects on consumers’ purchase decisions. Sentiment preference is the extension of attribute preference theory in the context of eWOM. It emphasizes the relative effects of different dimension sentiments. Although existing studies have generated important insights into the sentiment effects of eWOM, many are based on the overall sentiment or the absolute effects of individual dimensions (Liu, 2006; Duan et al., 2008; Ludwig et al., 2013). Absolute sentiment effects are more intuitive, whereas relative effects are more complex. The relative effects become especially important when sentiments across dimensions are mixed, i.e., positive for some but negative for others.

Moreover, our paper contributes to multi-attribute attitude theory in terms of both attribute importance and identification. First, we introduce the influence of market environment on the attribute importance in consumers’ product evaluations. Comparing consumers’ sentiment preferences for high- and low-budget movies, we provide empirical evidence for context dependence in attribute importance. Second, our method extends the use of multiattribute attitude theory to the big data environment using text mining techniques for attribute identification. For big data, traditionally used methods such as expert judgment, depth-interviews, and surveys are no longer suitable, because they are time-consuming, require significant manpower, and suffer from limitations of individual deviations, sample bias, and halo effects (Lehmann, 1971). Our method can be efficiently used even for big datasets to identify key attributes effectively. Although we apply the framework to movies only in this paper, it is applicable to other products in general.

Lastly, we propose a text mining framework for detecting key dimensions and dimension-specific sentiments over time. The multidimensional sentiment analysis (MDSA) method integrates DTM (Blei & Lafferty, 2006) and sentiment mining techniques. Our method effectively models the temporal evolution of dimension topics and sentiments, compared to other commonly used topic models. DTM can directly determine how the weight of each word in each product dimension changes over time and discover the changes in review topics over the lifecycle of the product.

## 5.2 Implications for Practice

Our findings provide important managerial implications. First, it is important for brands to identify the key product dimensions discussed in eWOM, understand their sales impacts, and make sales predictions accordingly. Such understanding can also help improve production and marketing. For the film industry specifically, given that the eWOM discussion mainly covers the dimensions of star, genre, and plot, movie distributors can achieve better accuracy in predicting box office revenues by integrating the review sentiments of these dimensions.

Second, star sentiment, plot sentiment, and genre sentiment have the strongest effects on product sales within a day or two. And their effects, although persistent, decline over time. This highlights the importance of the most recent reviews. For the film industry, reviews of the opening day and opening weekend box office sales are especially critical. Film producers and distributors need to respond quickly to newly generated reviews to seize important opportunities.

Third, marketers should emphasize their brands competitive position and allocate their marketing resources accordingly. For movies, we find that lowbudget movies should focus on the quality of genre and plot to generate higher genre and plot sentiments in reviews, while high-budget movies should emphasize the performance of actors to increase star sentiment. The relative importance of various review attributes is highly related to the emphasis of the brand’s promotional effort and targeted consumers. Satisfaction in the promoted dimensions expressed in eWOM converts more potential consumers.

## 5.3 Limitations

Our paper has several limitations. First, our sample movies comprise US films only. The effect of eWOM on sales may vary across products and regions. Future studies could include more products from different regional markets. Second, we exclude the movies that played in theaters for less than seven weeks. Thus, our sample movies may be more popular than average movies on the market. For eWOM, we consider only the product reviews on web forums. It would be valuable to include eWOM from other channels and examine their influence on sales. Channel difference is also an important issue for future research on eWOM.

## Acknowledgments

The authors thank the anonymous reviewers and senior editor for very constructive suggestions; this paper has benefited tremendously from those suggestions. This work was funded by the National Natural Science Foundation of China (Grant Nos. 71731005, 71571059).

## References

Abrigo, M. R., & Love, I. (2016). Estimation of panel vector autoregression in Stata. The Stata Journal, 16(3), 778-804.

Aggarwal, R., Gopal, R., Gupta, A., & Singh, H. (2012). Putting money where the mouths are: The relation between venture financing and electronic word-of-mouth. Information Systems Research, 23(3.2), 976-992.

Akaike, H. (1969). Fitting autoregressive models for prediction. Annals of the Institute of Statistical Mathematics, 21(1), 243-247.

Amblee, N., & Bui, T. (2011). Harnessing the influence of social proof in online shopping: The effect of electronic word of mouth on sales of digital microproducts. International Journal of Electronic Commerce, 16(2), 91-114.

Anderson, N. H., & Hubert, S. (1963). Effects of concomitant verbal recall on order effects in personality impression formation. Journal of Verbal Learning and Verbal Behavior, 2(5-6), 379-391.

Archak, N., Ghose, A., & Ipeirotis, P. G. (2011). Deriving the pricing power of product features by mining consumer reviews. Management Science, 57(8), 1485-1509.

Berger, J. A., Sorensen, A. T., & Rasmussen, S. (2010). Positive effects of negative publicity: When negative reviews increase sales. Marketing Science, 29(5), 825-827.

Berry, S., Levinsohn, J., & Pakes, A. (1995). Automobile prices in market equilibrium. Econometrica: Journal of the Econometric Society, 63(4), 841-890.

Berry, S., Levinsohn, J., & Pakes, A. (2004). Differentiated products demand systems from a combination of micro and macro data: The new car market. Journal of Political Economy, 112(1), 68-105.

Blei, D. M., & Lafferty, J. D. (2006). Dynamic topic models. Proceedings of the 23rd International Conference on Machine Learning, 113-120.

Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. Journal of Machine Learning Research, 3(January), 993-1022.

Chaiken, & Shelly. (1980). Heuristic versus systematic information processing and the use of source versus message cues in persuasion. Journal of

Personality and Social Psychology, 39(5), 752- 766.

Chevalier, J. A., & Mayzlin, D. (2006). The effect of word of mouth on sales: Online book reviews. Journal of Marketing Research, 43(3), 345-354.

Chintagunta, P. K., Gopinath, S., & Venkataraman, S. (2010). The effects of online user reviews on movie box-office performance: Accounting for sequential rollout and aggregation across local markets. Marketing Science, 29(5), 944-957.

Clemons, E. K., Gao, G. G., & Hitt, L. M. (2006). When online reviews meet the hyperdifferentiation : A study of craft beer industry. Journal of Management Information Systems, 23(2), 149- 171.

Connelly, B. L., Certo, S. T., Ireland, R. D., & Reutzel, C. R. (2011). Signaling theory: A review and assessment. Journal of Management, 37(1), 39- 67.

Cui, G., Lui, H., & Guo, X. (2012). The effect of online consumer reviews on new product sales. International Journal of Electronic Commerce, 17(1), 39-57.

Currim, I. S., Weinberg, C. B., & Wittink, D. R. (1981). Design of subscription programs for a performing arts series. Journal of Consumer Research, 8(1), 67-75.

De Vany, A., & Walls, W. D. (1999). Uncertainty in the movie industry: Does star power reduce the terror of the box office? Journal of Cultural Economics, 23(4), 285-318.

Dellarocas, C., Zhang, X., & Awad, N. F. (2007). Exploring the value of online product reviews in forecasting sales: The case of motion pictures. Journal of Interactive Marketing, 21(4), 23-45.

Dewan, S., & Ramaprasad, J. (2014). Social media, traditional media, and music sales. MIS Quarterly, 38(1), 101-121.

Driscoll, J. C., & Kraay, A. C. (1998). Consistent covariance matrix estimation with spatially dependent panel data. Review of Economics and Statistics, 80(4), 549-560.

Duan, W., Gu, B., & Whinston, A. B. (2008). Do online reviews matter? An empirical investigation of panel data. Decision Support Systems, 45(4), 1007-1016.

Fan, Z. P., Che, Y. J., & Chen, Z. Y. (2017). Product sales forecasting using online reviews and historical sales data: A method combining the

Bass model and sentiment analysis. Journal of Business Research, 74, 90-100.

Fishbein, M. (1963). An investigation of the relationships between beliefs about an object and the attitude toward that object. Human Relations, 16(3), 233-239.

Gardner, M. P. (1983). Advertising effects on attributes recalled and criteria used for brand evaluations. Journal of Consumer Research, 10(3), 310-318.

Ghiassi, M., Lio, D., & Moon, B. (2015). Preproduction forecasting of movie revenues with a dynamic artificial neural network. Expert Systems with Applications, 42(6), 3176-3193.

Guo, Y., Barnes, S. J., & Jia, Q. (2017). Mining meaning from online ratings and reviews: Tourist satisfaction analysis using latent Dirichlet allocation. Tourism Management, 59, 467-483.

Hannan, E. J., & Quinn, B. G. (1979). The determination of the order of an autoregression. Journal of the Royal Statistical Society: Series B (Methodological), 41(2), 190- 195.

Hansen, F. (1969). Consumer choice behavior: An experimental approach. Journal of Marketing Research, 6(4), 436-443.

Ho-Dac, N. N., Carson, S. J., & Moore, W. L. (2013). The effects of positive and negative online customer reviews: do brand strength and category maturity matter? Journal of Marketing, 77(6), 37-53.

Hoechle, D. (2007). Robust standard errors for panel regressions with cross-sectional dependence. The Stata Journal, 7(3), 281-312.

Holbrook, M. B., & Addis, M. (2008). Art versus commerce in the movie industry: A two-path model of motion-picture success. Journal of Cultural Economics, 32(2), 87-107.

Hovland, C. I., Janis, I. L., & Kelley, H. H. (1953). Communication and persuasion. Yale University Press.

Hu, N., Koh, N. S., & Reddy, S. K. (2014). Ratings lead you to the product, reviews help you clinch it? The mediating role of online review sentiments on product sales. Decision Support Systems, 57(1), 42-53.

Hu, N., Liu, L., & Zhang, J. J. (2008). Do online reviews affect product sales: The role of reviewer characteristics and temporal effects.

Information Technology & Management, 9(3), 201-214.

Hu, N., Pavlou, P. A., & Zhang, J. J. (2017). On Self-Selection Biases in Online Product Reviews. MIS Quarterly, 41(2), 449-471.

Jiménez, F. R., & Mendoza, N. A. (2013). Too popular to ignore: The influence of online reviews on purchase intentions of search and experience products. Journal of Interactive Marketing, 27(3), 226-235.

Johnson, E. J., Payne, J. W., & Bettman, J. R. (1988). Information displays and preference reversals. Organizational Behavior and Human Decision Processes, 42(1), 1-21.

Karniouchina, E. V. (2011). Impact of star and movie buzz on motion picture distribution and box office revenue. International Journal of Research in Marketing, 28(1), 62-74.

King, R. A., Racherla, P., & Bush, V. D. (2014). What we know and don’t know about online word-of-mouth: A review and synthesis of the literature. Journal of Interactive Marketing, 28(3), 167-183.

Kostyra, D. S., Reiner, J., Natter, M., & Klapper, D. (2016). Decomposing the effects of online customer reviews on brand, price, and product attributes. International Journal of Research in Marketing, 33(1), 11-26.

Kraft, F. B., Granbois, D. H., & Summers, J. O. (1973). Brand evaluation and brand choice: A longitudinal study. Journal of Marketing Research, 10(3), 235-241.

Lash, M. T., & Zhao, K. (2016). Early predictions of movie success: The who, what, and when of profitability. Journal of Management Information Systems, 33(3), 874-903.

Lau-Gesk, L., & Meyers-Levy, J. (2009). Emotional persuasion: When the valence versus the resource demands of emotions influence consumers’ attitudes. Journal of Consumer Research, 36(4), 585-599.

Lehmann, D. R. (1971). Television show preference: Application of a choice model. Journal of Marketing Research, 8(1), 47-55.

Li, J., & Zhan, L. (2011). Online persuasion: How the written word drives WOM: Evidence from consumer-generated product reviews. Journal of Advertising Research, 51(1), 239-257.

Li, X., Wu, C., & Mai, F. (2019). The effect of online reviews on product sales: A joint sentiment-topic

analysis. Information & Management, 56(2), 172-184.

Liang, T. P., Li, X., Yang, C. T., & Wang, M. (2015). What in consumer reviews affects the sales of mobile apps: A multifacet sentiment analysis approach. International Journal of Electronic Commerce, 20(2), 236-260.

Lin, Z., & Wang, Q. (2018). E-commerce product networks, word-of-mouth convergence, and product sales. Journal of the Association for Information Systems, 18(12), 848-871.

Liu, Q. Ben, & Karahanna, E. (2017). The dark side of reviews: The swaying effects of online product reviews on attribute preference construction. MIS Quarterly, 41(2), 427-448.

Liu, Y. (2006). Word of mouth for movies: Its dynamics and impact on box office revenue. Journal of Marketing, 70(3), 74-89.

Liu, Y., Chen, Y., Lusch, R. F., Chen, H., Zimbra, D., & Zeng, S. (2010). User-generated content on social media: predicting market success with online word-of-mouth. IEEE Intelligent Systems, 25(1), 8-12.

Love, I., Zicchino L. (2006). Financial development and dynamic investment behavior: Evidence from panel VAR. Quarterly Review of Economics and Finance, 46(2),190-210.

Lu, X., Ba, S., Huang, L., & Feng, Y. (2013). Promotional marketing or word-of-mouth? Evidence from online restaurant reviews. Information Systems Research, 24(3), 596-612.

Ludwig, S., De Ruyter, K., Friedman, M., Brüggen, E. C., Wetzels, M., & Pfann, G. (2013). More than words: The influence of affective content and linguistic style matches in online reviews on conversion rates. Journal of Marketing, 77(1), 87-103.

Luo, X., Gu, B., Zhang, J., Phang, C. W. (2017). Expert blogs and consumer perceptions of competing brands. MIS Quarterly, 41(2), 371-395.

Miller, K. E., & Ginter, J. L. (1979). An investigation of situational variation in brand choice behavior and attitude. Journal of Marketing Research, 16(1), 111-123.

Moe, W. W. & Trusov, M. (2011). The value of social dynamics in online product ratings forums, Journal of Marketing Research, 48(3), 444-456

Nan, H. U., Pavlou, P. A., & Zhang, J. (2017). Overcoming self-selection biases in online product reviews. MIS Quarterly, 41(2), 449-472.

Nelson, R. A., & Glotfelty, R. (2012). Movie stars and box office revenues: An empirical analysis. Journal of Cultural Economics, 36(2), 141-166.

Petty, R. E., & Cacioppo, J. T. (2012). Communication and persuasion: Central and peripheral routes to attitude change. Springer Science & Business Media.

Qi, P., Dozat, T., Zhang, Y., & Manning, C. D. (2018). Universal dependency parsing from scratch. Proceedings of the CoNLL 2018 Shared Task: Multilingual Parsing from Raw Text to Universal Dependencies, 160-170.

Rissanen, J. (1978). Modeling by shortest data description. Automatica, 14(5), 465-471.

Rui, H., & Whinston, A. (2011). Designing a socialbroadcasting-based business intelligence systems. ACM Transactions on Management Information Systems, 2(4), 22.

Rui, H., Liu, Y., & Whinston, A. (2013). Whose and what chatter matters? the effect of tweets on movie sales. Decision Support Systems, 55(4), 863-870.

Schouten, K., & Frasincar, F. (2016). Survey on aspect-level sentiment analysis. IEEE Transactions on Knowledge and Data Engineering, 28(3), 813-830.

Schwarz, G. (1978). Estimating the dimension of a model. The Annals of Statistics, 6(2), 461-464.

Shavitt, S., & Fazio, R. H. (1991). Effects of attribute salience on the consistency between attitudes and behavior predictions. Personality and Social Psychology Bulletin, 17(5), 507-516.

Socher, R., Perelygin, A., Wu, J., Chuang, J., Manning, C., Ng, A., & Christopher, P. (2013). Recursive deep models for semantic compositionality over a sentiment treebank. Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing, 1631-1642.

Song, T., Huang, J., Tan, Y., & Yu, Y. (2019). Using user-and marketer-generated content for box office revenue prediction: Differences between microblogging and third-party platforms. Information Systems Research, 30(1), 191-203.

Sun, M. (2012). How does the variance of product ratings matter? Management Science, 58(4), 696-707.

Tirunillai, S., & Tellis, G. J. (2014). Mining marketing meaning from online chatter: Strategic brand analysis of big data using latent Dirichlet allocation. Journal of Marketing Research, 51(4), 463-479.

Tversky, A., Sattath, S., & Slovic, P. (1988). Contingent weighting in judgment and choice. Psychological Review, 95(3), 371.

Wang, F., Liu, X., & Fang, E. (2015). User reviews variance, critic reviews variance, and product sales: An exploration of customer breadth and depth effects. Journal of Retailing, 91(3), 372- 389.

Zhang, Z., Li, X., & Chen, Y. (2012). Deciphering word-of-mouth in social media: Text-based metrics of consumer reviews. ACM

Transactions on Management Information Systems, 3(1), 1-23.

Zhao, K., Stylianou, A. C., & Zheng, Y. (2017). Sources and impacts of social influence from online anonymous user reviews. Information & Management, 55(1).

Zhu, F., & Zhang, X. (2010). Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. Journal of Marketing, 74(2), 133-148.

Zhu, Y., & Dukes, A. (2017). Prominent attributes under limited attention. Marketing Science, 36(5), 683-698.

## Appendix A: Multidimensional Sentiment Analysis Framework

Our multidimensional sentiment analysis (MDSA) method integrates the dynamic topic modeling (DTM) (Blei & Lafferty, 2006) and sentiment mining techniques. The DTM approach is used to extract the key dimensions of a product from the big data of online reviews effectively. Sentiment mining is employed to derive the sentiment values for the extracted dimensions. Overall, the MDSA consists of the following steps:

1. Identify the optimum number of dimensions,

2. Extract the key subject words of each dimension and label the dimension accordingly,

3. Calculate the dimension sentiment values.

## Dimension Mining

The graphical model DTM is shown in Figure A1. When the horizontal arrows are removed, this model reduces to a set of independent topic models (LDA). In essence, DTM is extended from the latent Dirichlet allocation (LDA) model (Blei et al., 2003) and can be observed as a set of LDA models in different time windows that are connected by some parameters over time $( \alpha _ { t }$ and $\beta _ { t } )$ . With time dynamics, the kth topic at time t has smoothly evolved from the kth topic at time t - 1 (for more details, see Blei & Lafferty, 2006).

![](/api/attachments/SMXMTZ7J/fulltext/images/c4d8a6db49c70e724910463e75ef630b0d6b6c7cb2dbfc82f8f39c90dd26bb81.jpg)  
Figure A1. Graphical Representation of a Dynamic Topic Model

DTM assumes that the generative process of each word in the review set on day ?? occurs in the following steps:

1. Draw parameter $\beta _ { t } | \beta _ { t - 1 } { \sim } N ( \beta _ { t - 1 } , \sigma ^ { 2 } I )$

2. Draw parameter $\alpha _ { t } | \alpha _ { t - 1 } { \sim } N ( \alpha _ { t - 1 } , a ^ { 2 } I )$

3. For each review,

(a) Draw dimension distribution $\scriptstyle \Pi \sim N ( \alpha _ { t } , \delta ^ { 2 } I )$

(b) For every word,

(1) Draw dimension $\mathsf { Z } = k { \sim } M u l t \big ( \pi ( \Pi ) \big ) = p ( Z = k | d , t )$

(2) Draw word $W = n { \sim } M u l t ( \pi ( \beta _ { t , k } ) ) = p ( W = n | Z = k , \ T = t ) .$

where π $\begin{array} { r } { \tau ( \beta _ { k , t } ) _ { w } = \frac { e ^ { ( \beta _ { k , t , w } ) } } { \sum _ { w } e ^ { ( \beta _ { k , t , w } ) } } . } \end{array}$ For a K-dimension model with N terms, let $\beta _ { t , k }$ denote the N-vector of the distribution of words for dimensionk ?? on day ??. The DTM parameters that must be set are parameter ??, parameter ?? and the dimension number K of the first day. ?? and $\beta$ are set according to experience: $\alpha = 0 . 1$ and $\beta = 5 0 / K \beta = 5 0 / \mathrm { K }$

The optimum number of dimensions, K, is chosen by comparing the perplexity of the topic model and the semantic content in the dimensions (Guo, Barnes, & Jia, 2017). When the perplexity value is lower, the performance of DTM is better. We formulate the perplexity of DTM for a corpus on day ?? as follows:

![](/api/attachments/SMXMTZ7J/fulltext/images/1c8ab03d6ab097275df2179be78428bc50800d47ec479328e8317ed700ae2308.jpg)  
Figure A2. Dimension Keywords and Weights of Star Dimension Identified from LDA vs. DTM

$$
p e r p l e x i t y (\boldsymbol {C} _ {t}) = e x p \left(- \frac {\sum_ {d = 1} ^ {D} \sum_ {n = 1} ^ {N _ {d}} \log \sum_ {k = 1} ^ {K} p (W = n | Z = k , T = t) p (Z = k | d , t)}{\sum_ {d = 1} ^ {D} N _ {d , t}}\right).
$$

$\pmb { C } _ { t } \mathrm { { C } _ { t } }$ is the review set on day ??. ?? is the number of review documents in $C _ { t } . \ N _ { d , t }$ is the number of words in document ?? on day ?? . K is the number of dimensions. $p ( W = n | Z = k , \ T = t )$ is the probability (weight) of word ?? in dimension ?? on day $t . p ( Z = k | d , t )$ is the weight of dimension ?? in review document ?? on day ??. We obtain $p ( Z =$ $k | d , t )$ and $p ( W = n | Z = k , \ T = t )$ from the DTM estimation using a Gibbs sampling procedure. We label the dimensions following the methods in Guo et al. (2017) and Tirunillai & Tellis (2014).

There are two advantages of DTM over LDA. First, DTM is well suited for our context of eWOM because when subsequent reviewers write reviews about movies, they are influenced by the previously posted reviews (Moe & Trusov, 2011). DTM approach can address such temporal influence of review in identifying the key dimensions. Using DTM, we can account for and directly determine the dynamics in the weight of each word in each product dimension, which cannot be obtained under the LDA model. For example, three themes are extracted from the same movie reviews by the LDA model and DTM model. Their results are shown in Figure A2.

DTM can detect words that stand out only temporarily (e.g., word $b u l g e r ^ { 7 }$ in the example shown in Figure A3). These topic words, although insignificant over a long period of time, are especially important for certain movies on certain days. However, their temporary importance for these movies would be ignored under LDA. In comparison, under DTM, the change in the weights of subject words affects the sentiment mining directly, as the sentiment words are weighted by the weights of their subject words. Therefore, the derived sentiment values can account for the temporary importance of topic words

![](/api/attachments/SMXMTZ7J/fulltext/images/37d5470e744e2f5c6c683bb2bcfa9fa18bacbc63f7d5c27a05cb4c36f565f014.jpg)  
Figure A3. Example of Dynamic Topic Words Distributed over Time (1 to 21)

## Dimension Sentiment Extraction

We combine the Stanford syntax parser and sentiment lexicon to mine dimensional sentiment (WordNet and the Harvard General Inquirer). Specifically, we extract the sentiment value of every word of a dimension by analyzing the syntactic dependency relations between the dimension word and its sentiment word in the daily review sentences. The dependency syntactic parsing aims to identify the grammatical relationship between words in a sentence in natural language processing (Qi et al., 2018), i.e., the nominal subject relationship between “movie” and “boring” in the sentence “The movie is boring.” For example, we use the Stanford syntax parser to perform dependency syntactic analysis on the sentence “Although the movie is boring and plot is loose, Leonardo performed perfectly,” and the results are shown in Figure A4. There are three dependency syntactic relationships identified about the three sentiment words: “movie” is the nominal subject of “boring,” “plot” is the nominal subject of “loose,” and “perfectly” is the adverb modifier of “Leonardo.”

Although the movie is boring and plot is loose, Leonardo performed perfectly.

![](/api/attachments/SMXMTZ7J/fulltext/images/278a7e4eca551d3b89eca4ddebe6618ce7660bb62b36a636ff053add1a01dfe7.jpg)  
Figure A4. Example of Dependency Syntactic Parsing for Sentiment Words

Then, based on the sentiment dictionary, we assign the values of the sentiment words to the corresponding subject words. Table A2 presents the main syntax relations and how sentiment values are assigned to dimension words accordingly. For example, in Table A2, “plot” is the nominal subject of “boring”, so that the sentiment value (-0.573) of “boring” is assigned to the dimension word “plot.”

Table A2. The Main Syntax Relations

<table><tr><td>Syntax relation</td><td>Example</td><td>Dimension word sentiment</td></tr><tr><td>Nominal subject</td><td>The plot is boring.</td><td>Plot: -0.573</td></tr><tr><td>Adjectival modifier</td><td>She is a good actor.</td><td>Actor: 0.723</td></tr><tr><td>Direct object</td><td>I enjoy 3D.</td><td>3D: 0.668</td></tr><tr><td>Open clausal complement</td><td>I think the actor enjoys acting.</td><td>Acting: 0.668</td></tr><tr><td>Adverb modifier</td><td>Tom performed earnestly.</td><td>Perform: 0.158</td></tr><tr><td>Relative clause modifier</td><td>I saw the actor who people dislike.</td><td>Actor: -0.438</td></tr></table>

Next, we normalize the weights of dimension words for all dimensions. For dimension word ?? of dimension ?? on day ??, its weight $w e _ { n , t , k }$ is calculated as the normalization of $p ( W _ { n } = w | Z _ { n } = k , T = t )$ such that:

$$
w e _ {n, t, k} = \frac {p (W _ {n} = w | Z _ {n} = k , T = t)}{\sum_ {n = 1} ^ {N _ {k}} p (W _ {n} | Z _ {n} = k , T = t)}.
$$

Finally, for each dimension, we calculate its daily sentiment value using the weights $( w e _ { n , t , k } )$ and sentiment values of its dimension words. Let $S _ { i , n , d }$ be the sentiment value of the ??th dimension word that appears for the ??th time in document ??, D be the number of documents on day ??, and $N _ { k }$ be the number of words in dimension ??. The sentiment of the ??th dimension on day ?? can be calculated as:

$$
s e n t i m e n t _ {k, t} = \sum_ {n = 1} ^ {N _ {k}} w e _ {n, t, k} \frac {1}{D} \sum_ {d = 1} ^ {D} \frac {1}{I} \sum_ {i = 1} ^ {I} S _ {i, n, d},
$$

and then normalized to be between 0 and 1 using the Minmax function:

$$
Z _ {k, t} = \frac {\text {sentiment} _ {k , t} - \min (\text {sentiment} _ {k , t})}{\max (\text {sentiment} _ {k , t}) - \min (\text {sentiment} _ {k , t})}.
$$

We conducted an experiment on manual labelling of dimension sentiment values to evaluate the performance of the dependency syntactic parsing. Specifically, for the 1,682 reviews from the first two weeks of the movie Revenant, we employed four volunteers to respectively label the star, plot, and genre dimensions of each review with sentiment values from -1 to 1, which were then normalized to be between 0 and 1. Their results turned out to be highly consistent according to Kappa coefficients (between 0.301 and 0.57 with significance levels less than 0.04). Then for each dimension, the sentiment values given by the volunteers were averaged to be the dimension sentiment value of a review, which is then compared with that derived under the dependency syntactic parsing with DTM. We found that the mean squared error (MSE) between the sentiments mined by our method and the manually labeled sentiments is less than 0.1.

To examine the performance impact of the topic mining method used, we also calculated the MSE between the sentiments derived under the same dependency syntactic parsing with LDA and the manually labeled sentiments. The results in Figure A5-A7 show that the sentiment MSE of DTM is smaller than LDA (by 0.05 overall) for all three dimensions. Therefore, DTM performs better than LDA in terms of dimension sentiment extraction.

![](/api/attachments/SMXMTZ7J/fulltext/images/b665efc18743d2e7c523433c42560e7448d591612d1d2f086878a5bc1a0fc0f6.jpg)

Figure A5. Star Sentiment Preference  
![](/api/attachments/SMXMTZ7J/fulltext/images/b03aac51aa89869b22da0746f100987291f8bfa083f592fcf4cb65f18415543b.jpg)  
Figure A6. Genre Sentiment Preference

![](/api/attachments/SMXMTZ7J/fulltext/images/c5d90b89326c2b074d0969f7bf3bb43ed0a6eddd22133610ee69faf0d12f8143.jpg)  
Figure A7. Plot Sentiment Preference

## Appendix B: Robustness Checks

## Fixed Effects Estimation

As an alternative model specification, we carried out a fixed-effects model estimation. The Hausman specification test established the appropriateness of a fixed-effects model over a random-effects model (Chi-square = 537.27 for full group; Chi-square = 376.94 for low-budget group; Chi-square = 158.60 for high-budget group). Following Hoechle (2007), we estimated fixed effects (within) regression models with Driscoll and Kraay standard errors (Driscoll & Kraay, 1998) that account for cross-sectional and temporal dependence. The coefficient estimates are shown in Table B1.

The estimation results on of the full sample are similar to those using the PVAR models. All three-dimension sentiments had significantly positive effects on movie box office sales. From the comparison of high-budget and lowbudget movies, the same conclusions are derived, in support of H2a and H2b. Because of consumers’ sentiment preference, sentiment information in eWOM along different product dimensions had different persuasive effects on consumers’ purchase decisions.

Table B1. Fixed Effects Estimation

<table><tr><td></td><td colspan="2">(A) Full sample</td><td colspan="2">(B) High-budget movies</td><td colspan="2">(C) Low-budget movies</td></tr><tr><td>Sale</td><td>Coefficient</td><td>t</td><td>Coefficient</td><td>T</td><td>Coefficient</td><td>t</td></tr><tr><td>Lag.sale</td><td>0.422***</td><td>-12.88</td><td>0.274***</td><td>-6.89</td><td>0.665***</td><td>-13.84</td></tr><tr><td>Lag.star</td><td>1.105***</td><td>-4.51</td><td>1.800***</td><td>-4.15</td><td>0.657**</td><td>-2.57</td></tr><tr><td>Laggenre</td><td>0.563***</td><td>-2.95</td><td>0.643**</td><td>-2.14</td><td>0.819***</td><td>-3.5</td></tr><tr><td>Lag.plot</td><td>0.604*</td><td>-1.93</td><td>0.74</td><td>-1.64</td><td>1.038**</td><td>-2.52</td></tr><tr><td>volume</td><td>0.035</td><td>-1.05</td><td>-0.013</td><td>-0.25</td><td>0.053</td><td>-1.45</td></tr><tr><td>cinema</td><td>0</td><td>-0.01</td><td>0.061</td><td>-1.65</td><td>-0.045</td><td>-1.5</td></tr><tr><td>rating</td><td>0.519***</td><td>-8.5</td><td>0.682***</td><td>-7.85</td><td>0.320***</td><td>-3.31</td></tr><tr><td>weekend</td><td>-0.077</td><td>-1.13</td><td>-0.133</td><td>-1.47</td><td>0.083</td><td>-0.93</td></tr><tr><td>competition</td><td>0.042**</td><td>-2.51</td><td>0.057***</td><td>-2.87</td><td>0.045</td><td>-1.64</td></tr><tr><td>star_load</td><td>0.155</td><td>-1.38</td><td>0.338**</td><td>-2.01</td><td>-0.048</td><td>-0.36</td></tr><tr><td>genre_load</td><td>0.278**</td><td>-2.37</td><td>0.466***</td><td>-2.7</td><td>0.026</td><td>-0.19</td></tr><tr><td>plot_load</td><td>0.267**</td><td>-2.47</td><td>0.410**</td><td>-2.5</td><td>0.1</td><td>-0.77</td></tr><tr><td>#Obs</td><td colspan="2">2440</td><td colspan="2">1360</td><td colspan="2">1080</td></tr><tr><td colspan="7">Note: The lag length for all lag variables is 1. ***, **, and * denote significance at 1%, 5%, and 10%, respectively.</td></tr></table>

## PVAR Estimation with Two-Period Lags

In our main results, the choice of a one-period-lag for the PVAR model was made according to the information criterion. As a robustness check, we estimated the model with two-period lags. Table B2 shows that the results remain qualitatively unchanged, except that the effects of plot- and genre sentiment become insignificant for high-budget movies.

Table B2. Sentiment Effects Estimation with a Two-Day Lag

<table><tr><td></td><td colspan="2">(A) Full sample</td><td colspan="2">(B) High-budget movies</td><td colspan="2">(C) Low-budget movies</td></tr><tr><td>Sale</td><td>Coefficient</td><td>z</td><td>Coefficient</td><td>z</td><td>Coefficient</td><td>z</td></tr><tr><td>Lag.sale</td><td>0.505***</td><td>-7.41</td><td>0.292***</td><td>-3.58</td><td>0.989***</td><td>-3.46</td></tr><tr><td>Lag2.sale</td><td>0.079</td><td>-1.58</td><td>0.023</td><td>-0.37</td><td>0.218</td><td>-1.3</td></tr><tr><td>Lag.star</td><td>2.596***</td><td>-5.36</td><td>2.675***</td><td>-3.97</td><td>3.099***</td><td>-2.75</td></tr><tr><td>Lag2.star</td><td>1.600***</td><td>-3.59</td><td>1.899***</td><td>-3.08</td><td>2.268*</td><td>-1.94</td></tr><tr><td>Lag genre</td><td>1.917***</td><td>-4.52</td><td>0.617</td><td>-1.58</td><td>3.743**</td><td>-2.57</td></tr><tr><td>Lag2 genre</td><td>1.765***</td><td>-4.54</td><td>0.413</td><td>-1.09</td><td>3.299**</td><td>-2.54</td></tr><tr><td>Lag.plot</td><td>3.209***</td><td>-3.6</td><td>1.137</td><td>-1.47</td><td>9.848**</td><td>-2</td></tr><tr><td>Lag2.plot</td><td>2.188***</td><td>-3.59</td><td>0.664</td><td>-1.12</td><td>5.213*</td><td>-1.81</td></tr><tr><td>volume</td><td>0.147***</td><td>-2.7</td><td>-0.021</td><td>-0.29</td><td>0.206*</td><td>-1.95</td></tr><tr><td>cinema</td><td>0.001</td><td>0.001</td><td>0.073</td><td>-1.38</td><td>0.308</td><td>-1.05</td></tr><tr><td>rating</td><td>1.015***</td><td>-3.43</td><td>0.691**</td><td>-2.3</td><td>1.08</td><td>-0.98</td></tr><tr><td>weekend</td><td>0.295***</td><td>-5.06</td><td>0.191***</td><td>-2.71</td><td>0.449**</td><td>-2.57</td></tr><tr><td>competition</td><td>0.105</td><td>-0.9</td><td>0.21</td><td>-1.12</td><td>-0.141</td><td>-0.57</td></tr><tr><td>star_load</td><td>0.882***</td><td>-3.65</td><td>0.538**</td><td>-2.19</td><td>1.526**</td><td>-1.99</td></tr><tr><td>plot_load</td><td>1.107***</td><td>-4.39</td><td>0.563**</td><td>-2.44</td><td>1.834**</td><td>-2.34</td></tr><tr><td>#Obs</td><td colspan="2">2318</td><td colspan="2">1292</td><td colspan="2">1026</td></tr></table>

Note: Volume, cinema, rating, weekend, competition, star loadings, and plot loadings are a set of control variables, and the estimation drops the genre loadings variable because of the collinearity. The lag length for all lag variables is 2. \*\*\*, \*\*, and \* denote significance at 1%, 5%, and 10%, respectively.

## Additional Endogenous Variables

Some control variables such as review volume, ratings, and number of screens may also be endogenous. As a robustness check, we assume these variables to be endogenous and conducted Granger causality tests. As shown in Table B3, we can rule out the endogeneity of number of screens but not review volume and rating. Therefore, we include volume and rating as additional endogenous variables in the PVAR model. Table B4 shows the estimated results and our main conclusions remain unchanged.

Table B3. Granger Causality Tests

<table><tr><td>Equation</td><td>Excluded</td><td colspan="2">All (N=122)</td><td colspan="2">High-budget movies (N=68)</td><td colspan="2">Low-budget movies (N=54)</td></tr><tr><td>sale</td><td>star</td><td>21.64***</td><td>&lt;0.001</td><td>16.748***</td><td>&lt;0.001</td><td>6.12**</td><td>0.013</td></tr><tr><td>sale</td><td>genre</td><td>19.42***</td><td>&lt;0.001</td><td>3.67*</td><td>0.055</td><td>7.95**</td><td>0.005</td></tr><tr><td>sale</td><td>plot</td><td>18.10***</td><td>&lt;0.001</td><td>5.01**</td><td>0.025</td><td>6.57**</td><td>0.011</td></tr><tr><td>sale</td><td>volume</td><td>10.39**</td><td>0.002</td><td>0.12</td><td>0.724</td><td>4.51**</td><td>0.034</td></tr><tr><td>sale</td><td>screen</td><td>0.02</td><td>0.878</td><td>2.02</td><td>0.155</td><td>0.86</td><td>0.352</td></tr><tr><td>sale</td><td>rating</td><td>7.54**</td><td>0.006</td><td>6.81**</td><td>0.009</td><td>0.29</td><td>0.584</td></tr><tr><td colspan="8">Note: *** **, and * denote significance at 1%, 5%, and 10%, respectively.</td></tr></table>

Note: \*\*\*, \*\*, and \* denote significance at 1%, 5%, and 10%, respectively.

Table B4. SGMM Estimation Results for Full Sample, High-Budget, and Low-Budget Movies

<table><tr><td></td><td colspan="2">(A) Full sample</td><td colspan="2">(B) High-budget movies</td><td colspan="2">(C) Low-budget movies</td></tr><tr><td>Sale</td><td>Coefficient</td><td>z</td><td>Coefficient</td><td>z</td><td>Coefficient</td><td>z</td></tr><tr><td>Lag.sale</td><td>0.630***</td><td>-7.68</td><td>0.376***</td><td>-4.75</td><td>1.178***</td><td>-4.43</td></tr><tr><td>Lag.star</td><td>3.089***</td><td>-4.91</td><td>2.753***</td><td>-3.96</td><td>3.800***</td><td>-2.88</td></tr><tr><td>Laggenre</td><td>2.323***</td><td>-4.84</td><td>1.108***</td><td>-2.63</td><td>3.441***</td><td>-3</td></tr><tr><td>Lag.plot</td><td>3.329***</td><td>-4.2</td><td>1.560**</td><td>-2.14</td><td>5.964**</td><td>-2.54</td></tr><tr><td>Lag.volume</td><td>0.189***</td><td>-3.25</td><td>0.005</td><td>-0.07</td><td>0.211**</td><td>-2.39</td></tr><tr><td>Lag.rating</td><td>0.676***</td><td>-3.46</td><td>0.647***</td><td>-2.67</td><td>0.537</td><td>-1.47</td></tr><tr><td>cinema</td><td>0.045</td><td>-0.82</td><td>0.110*</td><td>-1.87</td><td>0.257</td><td>-1.53</td></tr><tr><td>weekend</td><td>0.232***</td><td>-4.68</td><td>0.168**</td><td>-2.53</td><td>0.297***</td><td>-3.45</td></tr><tr><td>compete</td><td>0.285**</td><td>-2.38</td><td>0.329*</td><td>-1.74</td><td>0.156</td><td>-0.99</td></tr><tr><td>star_popu</td><td>1.012***</td><td>-3.55</td><td>0.595**</td><td>-2.08</td><td>1.218**</td><td>-2.15</td></tr><tr><td>plot_popu</td><td>1.188***</td><td>-4.16</td><td>0.682**</td><td>-2.55</td><td>1.426**</td><td>-2.42</td></tr><tr><td>#Obs</td><td colspan="2">2318</td><td colspan="2">1292</td><td colspan="2">1026</td></tr><tr><td colspan="7">Note: Cinema, weekend, competition, star loadings, and plot loadings are a set of control variables, and the estimation drops the genre loadings variable because of the collinearity. The lag length for all lag variables is 1. ***, **, and * denote significance at 1%, 5%, and 10%, respectively.</td></tr></table>

## About the Authors

Cuiqing Jiang is a professor in the School of Management, Hefei University of Technology. He received his PhD degree in 2007 from Hefei University of Technology. His research interests include big data analytics and business intelligence, data mining and knowledge discovery, information systems, and financial technology (Fintech). He has published in journals such as Journal of Management Information Systems, European Journal of Operational Research, Information Sciences, Decision Support Systems, and International Journal of Production Research.

Jianfei Wang is a doctoral student in the School of Management, Hefei University of Technology. His research interests include business intelligence, data mining, and financial technology (Fintech).

Qian Tang is an assistant professor in the School of Computing and Information Systems, Singapore Management University. She received her PhD in management information systems from the University of Texas at Austin in 2013. Her research interests include social media and social networks, online word of mouth, economics of IS, and information security.

Xiaozhong Lyu is an engineer at the 38th Research Institute of China Electronics Technology Group Corporation. He received his PhD degree in 2019 from Hefei University of Technology. His research interests include big data analytics and business intelligence, data mining and knowledge discovery, and information systems.

Copyright © 2021 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
