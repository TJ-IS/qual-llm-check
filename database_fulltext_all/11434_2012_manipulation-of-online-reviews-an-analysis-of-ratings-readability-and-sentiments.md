---
otero_id: 11434
otero_key: "6UNSMSDS"
title: "Manipulation of online reviews: An analysis of ratings, readability, and sentiments"
authors: "Nan Hu; Indranil Bose; Noi Sian Koh; Ling Liu"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Manipulation of online reviews: An analysis of ratings, readability, and sentiments Nan Hu <sup>a</sup>, Indranil Bose <sup>b,</sup>⁎, Noi Sian Koh <sup>c</sup>, Ling Liu <sup>a</sup>

<sup>a</sup> University of Wisconsin–Eau Claire, United States

<sup>b</sup> The University of Hong Kong, Hong Kong

<sup>c</sup> Singapore Management University, Singapore

## a r t i c l e i n f o

Article history: Received 11 May 2010 Received in revised form 29 September 2011 Accepted 3 November 2011 Available online 12 November 2011

Keywords: Manipulation Online reviews Ratings Readability Runs test Sentiments Text mining

## a b s t r a c t

As consumers become increasingly reliant on online reviews to make purchase decisions, the sales of the product becomes dependent on the word of mouth (WOM) that it generates. As a result, there can be attempts by <sup>fi</sup>rms to manipulate online reviews of products to increase their sales. Despite the suspicion on the existence of such manipulation, the amount of such manipulation is unknown, and deciding which reviews to believe in is largely based on the reader's discretion and intuition. Therefore, the success of the manipulation of reviews by <sup>fi</sup>rms in generating sales of products is unknown. In this paper, we propose a simple statistical method to detect online reviews manipulation, and assess how consumers respond to products with manipulated reviews. In particular, the writing style of reviewers is examined, and the effectiveness of manipulation through ratings, sentiments, and readability is investigated. Our analysis examines textual information available in online reviews by combining sentiment mining techniques with readability assessments. We discover that around 10.3% of the products are subject to online reviews manipulation. In spite of the deliberate use of sentiments and ratings in manipulated products, consumers are only able to detect manipulation taking place through ratings, but not through sentiments. The <sup>fi</sup>ndings from this research ensue a note of caution for all consumers that rely on online reviews of books for making purchases, and encourage them to delve deep into the book reviews without being deceived by fraudulent manipulation

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Consumers are increasingly relying on opinions posted on the ecommerce websites to make a variety of decisions ranging from what movies to watch to what stocks to invest in [17]. Previously, these decisions were based on advertisements or product information provided by vendors. However, with the proliferation of e-commerce and increasing number of product reviews provided by users, it has been found that consumers have increasingly relied on online reviews for their search of information related to a variety of products. Prior research has also found that consumers <sup>fi</sup>nd such usergenerated reviews more credible and trustworthy than the traditional sources [3]. However, it is generally not known to what extent these online reviews are truthful ‘user-generated’ reviews or merely reviews provided by vendors interested to push the sales of products. In addition, it is not clear how effectively vendors can use various mechanisms to manipulate online reviews and in<sup>fl</sup>uence consumers' purchase decisions.

Following previous literature [22,23], we de<sup>fi</sup>ne reviews manipulation as vendors, publishers, writers, or any third-party consistently monitoring the online reviews and posting non-authentic online reviews on behalf of customers when needed, with the goal of boosting the sales of their products. Based on the assumption that the writing style of authentic online reviews (e.g., readability, which will be de<sup>fi</sup>ned later) should be random, we propose a non-parametric method to evaluate whether the reviews of one product, instead of individual reviews of each product, are manipulated and whether consumers understand such manipulation.

Reviews manipulation is not a hypothetical phenomenon. It is known to exist widely in popular websites related to e-commerce, travel, and music. For example, when Amazon.com's Canadian website accidentally revealed the true identities of some of its book reviewers due to software errors, it was found that a sizable proportion of these reviews were written by the book's own publishers, authors and their friends or relatives [19]. This is also con-<sup>fi</sup>rmed by our data of products with manipulated reviews (Fig. 1), in which we noticed the suspicious behavior of a customer who frequently posted positive reviews. He/she visited the website every few days to post reviews with different textual comments with very high ratings for a single item. Fig. 2 shows another case in which one reviewer plagiarized the content of another review.<sup>1</sup>

<table><tr><td>ASIN</td><td>AverageRating</td><td>TotalReviews</td><td>Rating</td><td>HelpfulVotes</td><td>CustomerId</td><td>TotalVotes</td><td>RevDate</td><td></td></tr><tr><td>0385504209</td><td>3.5</td><td>3052</td><td>4</td><td>36</td><td>A1M4NJYPOWNLBQ</td><td>52</td><td>2004-05-08</td><td>Take Only As Dir</td></tr><tr><td>0385504209</td><td>3.5</td><td>3052</td><td>4</td><td>11</td><td>A16W9E27VW9IND</td><td>36</td><td>2004-05-05</td><td>Gripping and intr</td></tr><tr><td>0385504209</td><td>3.5</td><td>3052</td><td>5</td><td>27</td><td>A2MV5ADA356BDO</td><td>56</td><td>2004-05-04</td><td>A &quot;Code&quot; Worth I</td></tr><tr><td>0385504209</td><td>3.5</td><td>3052</td><td>3</td><td>37</td><td>A3TEH90X39WC8F</td><td>43</td><td>2004-04-30</td><td>What Makes a Tl</td></tr><tr><td>0385504209</td><td>3.5</td><td>3052</td><td>5</td><td>13</td><td>A2SIE5S9TB4JI9</td><td>36</td><td>2004-04-29</td><td>I AM ENJOYING</td></tr><tr><td>0385504209</td><td>3.5</td><td>3052</td><td>1</td><td>35</td><td>A2JA9LYSXZES1A</td><td>83</td><td>2004-04-25</td><td>probably better if</td></tr><tr><td>0385504209</td><td>3.5</td><td>3052</td><td>1</td><td>35</td><td>A10ZH57J6QP844</td><td>46</td><td>2004-04-24</td><td>Buyer Beware</td></tr><tr><td>0385504209</td><td>3.5</td><td>3052</td><td>2</td><td>57</td><td>AU1XXY2S6FZQ2</td><td>86</td><td>2004-04-23</td><td>I dont get it</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>A8LB47171J0QJ</td><td>0</td><td>2000-07-20</td><td>AN ADVENTURE</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>ASNLJKAV3DBZX</td><td>0</td><td>2000-07-19</td><td>Funny, poignant,</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>4</td><td>0</td><td>A1YVCJWVGCOIAI</td><td>0</td><td>2000-07-18</td><td>A Sweet Book</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>ATVPDKIKX0DER</td><td>0</td><td>1999-10-04</td><td>One of the best b</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>ATVPDKIKX0DER</td><td>0</td><td>1999-10-03</td><td>Just great</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>ATVPDKIKX0DER</td><td>0</td><td>1999-10-03</td><td>The book was an</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>ATVPDKIKX0DER</td><td>0</td><td>1999-10-02</td><td>A Wonderful Boo</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>ATVPDKIKX0DER</td><td>0</td><td>1999-09-29</td><td>Dreams Beyond</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>AHVTCYHS5XSYM</td><td>0</td><td>1999-09-28</td><td>AN INSPIRATION</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>ATVPDKIKX0DER</td><td>0</td><td>1999-09-25</td><td>THANKS FOR Th</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>ATVPDKIKX0DER</td><td>0</td><td>1999-09-23</td><td>A wonderful book</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>A3N8ITRDS67TVO</td><td>0</td><td>1999-09-23</td><td>Fantastic</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>A3IX35WEY1Q21U</td><td>0</td><td>1999-09-09</td><td>I havent read a bc</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>ATVPDKIKX0DER</td><td>0</td><td>1999-09-03</td><td>THIS BOOK IS IS</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>A2WVAQN7UM2LDW</td><td>0</td><td>1999-09-03</td><td>Wowl</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>ATVPDKIKX0DER</td><td>0</td><td>1999-09-02</td><td>All childhood rocl</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>A19EWP1UGX12B</td><td>0</td><td>1999-08-29</td><td>Inspirational stor</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>A2THG37NXPJB6C</td><td>0</td><td>1999-08-28</td><td>A Superior Book</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>ATVPDKIKX0DER</td><td>0</td><td>1999-08-28</td><td>Americana at its</td></tr><tr><td>0385333218</td><td>5</td><td>491</td><td>5</td><td>0</td><td>A2Z9YDOWG6VBOG</td><td>0</td><td>1999-08-28</td><td>If you read only o</td></tr></table>

Fig. 1. Examples of manipulated reviews.

Reviews manipulation is not just prevalent amongst book sellers. The music industry is known to hire professional marketers who surf various online chat rooms and fan sites to post positive comments about new albums [30,39]. It also exists in the hospitability industry centered around hotels and restaurants. Insiders of the travel industry have claimed that reviews in their industry have been manipulated, either by the owners or by the competitors.<sup>2</sup> The comments made by the manipulator of restaurant reviews are an eye opener. “I began tracking feedback about my restaurant on TripAdvisors ‘rants and raves’ page. It very quickly occurred to me that I could [write] in glowing reviews about my own restaurant and up my ratings numbers. After a period of time, I began to see my rating slide a bit after some not so positive postings by supposedly ‘real’ customers. …Were they posted by my competition? Perhaps, but I didn't let it concern me too much. I simply got on TripAdvisor and bombarded them with glowing reviews about my own restaurant! Within days, I was rated a perfect 5!” The well-known publisher of travel guides Frommers remarked: “Why wouldn't a hotel submit a <sup>fl</sup>urry of positive comments penned by employees or friends? If you were a hotel owner, wouldn't you take steps to make sure that TripAdvisor contained numerous favorable write-ups of your property? Who would fail to do this?”<sup>3</sup>

Although the various pieces of evidence in the above paragraph show that online reviews manipulation is a well-established industrial malpractice and a serious problem in itself because consumers may make the wrong purchase decision based on these manipulated information, to date, there have been few studies that have investigated and reported the presence of manipulated reviews in the online review forums. To the best of our knowledge, there are only two recent research papers that have focused on proving the existence of online reviews manipulation [22,23]. However, current work does not offer ways to identify products whose reviews are manipulated. Also, [22,23] focus on using numeric ratings to detect the existence of online reviews manipulation, ignoring the rich textual contents of online reviews. In this paper, we go beyond the analysis of ratings to examine the textual content of reviews and propose a statistical ‘Runs’ test method to identify products with reviews that are manipulated.<sup>4</sup>

Since participants of online review communities can assume any identity or choose to remain anonymous, marketers are able to disguise their promotion of products as consumer recommendations. In an online context, if potential customers knew which reviews were posted by real customers who consumed the product, and which reviews were written by authors, publishers, or any third parties with sel<sup>fi</sup>sh interests, then those potential customers could undo the damages caused by these slanted reviews. Unfortunately, since all slanted reviews were written by anonymous entities or by manipulators who assumed a customer's identity, it was not easy for consumers to distinguish a slanted review from a truthful review written by a zealous customer by simply looking at the rating of a review. A manual inspection of the textual content of a single review could not totally solve that problem either because it was still dif<sup>fi</sup>cult to differentiate between truthful and manipulated reviews unless some parts of the manipulated review were identical to another review [7]. For unsuspecting customers it was almost impossible to detect the manipulation of ratings of products as well as product related emotional sentiments that were included in a review.

In this paper, we set off to discover the presence of manipulation in online reviews of products and identify the effectiveness of the promotional content within manipulated reviews on the sales of products.

We speci<sup>fi</sup>cally address the following research questions:

1. To what extent is manipulation present in online reviews?

2. How can such manipulation be detected from the ratings and textual content of reviews? What are some of the textual characteristics that can be used to identify products with manipulated reviews?

....In this well-researched, entertaining, and immensely readable book, Pinch (science & technology, Cornell Univ.) and Trocco (Lesley Univ., U.K.) chronicle the synthesizer's early heady years, from the mid-1960s through the mid-1970s.....Throughout, their prose is engagingly anecdotal and accessible, and readers are never asked to wade through

....In this well-researched, entertaining, and immensely readable book, Kettlewell chronicles the synthesizer's early, vears. from the turn of the 20th century - through the mid-1990s.....Throughout, his prose is engagingly anecdotal and accessible, and readers are never asked to wade through dense, technological jargon. Yet there are enough details to enlighten those trying to understand this multidisciplinary field of music, acoustics physics, and electronics. Highly recommended

3. What is the impact of reviews manipulation in terms of rating and writing style on the sales of products?

To answer the above questions, we need to <sup>fi</sup>nd a way to identify products with manipulated reviews. We <sup>fi</sup>rst describe the intuition behind the method for the detection of manipulated products. As writing style varies with the background of an individual, intuitively, reviews written by different consumers will be random in the case where there is no manipulation [21,24]. In other words, writing style of the reviews and review scores should be mutually independent and identically distributed with respect to time. Building on this intuition, we propose a method to detect manipulated products by examining the sequence of review ratings and writing style of the textual reviews. Subsequently, we extract products with manipulated reviews and then analyze the impact of manipulation of the reviews of the products on the sales of the products.

In the context of this research, writing style refers to how consumers construct sentences together when they write online reviews. Reviews written by individual consumers often express a personal view of their experience about the products. Thus their writing style should be different from one another. Such differences re<sup>fl</sup>ect the heterogeneity in their culture, education, occupation and so on. However, for manipulators, the situation is different. If reviews are consistently monitored and posted by manipulators, then the observed reviews will be a blend of true customer reviews and manipulators' reviews; hence the writing styles of observed reviews will not be random with the existence of manipulators.

By observing the change in the writing style over time, we can infer whether the online reviews for a product is manipulated or not because writing style is unique among individuals. Building on this intuition, we develop a model for the detection of manipulation.

The rest of the paper is organized as follows. Section 2 discusses related work in the <sup>fi</sup>eld of accounting and computer science that deals with detection of fraud, and reviews extant research on sentiments and writing style analysis. Section 3 presents our research method for the detection of manipulation in reviews. Section 4 presents the research setting, and the numerical results related to the existence of reviews manipulation and its impact on sales. Finally, Section 5 summarizes the main contributions of this paper, identi<sup>fi</sup>es the limitations of this research approach, and discusses some directions for future research in the area of online reviews manipulation.

## 2. Related work

Several researchers have actively examined the various effects of WOM e.g. [4,5,8–10,15,26,27]. Using user reviews on Yahoo! Movies, Liu [27] and Duan et al. [10] found that the valence of previous movie reviews did not have any signi<sup>fi</sup>cant impact on later weekly box of<sup>fi</sup>ce revenues. Gruhl et al. [16] showed that volume of blog postings could be used to predict spikes in actual consumer purchase decisions at the online retailer Amazon. Other researchers started to investigate various factors that could in<sup>fl</sup>uence online reviews such as the impact of online reviewers' characteristics [11,14]. Forman et al. [11] considered the effect of reviewers' online identities on the impact of reviews. They found that reviews posted by real name reviewers had a larger impact on product sales than those posted by anonymous reviewers. Hence, with the proliferation of online reviews, many people believed that online consumer reviews were a good proxy for overall WOM and could also in<sup>fl</sup>uence consumers' decisions. However, the ef<sup>fi</sup>cacy of online reviews could nonetheless be limited.

Given the power of electronic WOM, many <sup>fi</sup>rms are taking advantage of online consumer reviews as a new marketing tool [8]. Studies showed that <sup>fi</sup>rms not only regularly posted their product information and sponsored promotional chats on online forums, such as

USENET [30], they also proactively encouraged their consumers to spread the word about their products online [15]. Some <sup>fi</sup>rms even strategically manipulated online reviews in an effort to in<sup>fl</sup>uence consumers' purchase decisions [8,20]. An underlying belief behind such strategies is that online consumer reviews could signi<sup>fi</sup>cantly in<sup>fl</sup>uence consumers' purchase related decisions. Some recent studies have looked into how marketers can strategically manipulate consumers' online communications [8,30].

## 2.1. Manipulation

Manipulation of reviews occurs when online vendors, publishers, or authors write ‘consumer’ reviews by posing as real customers. Thus, manipulation here means that the posted review is not a truthful account of a real customer's experience. Manipulation or fraud is not a new area of research in the traditional business <sup>fi</sup>elds [29,31]. For example, in the area of accounting there is extant research on pro-<sup>fi</sup>ling of earnings manipulators through the identi<sup>fi</sup>cation of their distinguishing characteristics as well as development of models for the detection of earnings management [2,34]. The variables used in such models represented the effects of manipulation or preconditions that prompted <sup>fi</sup>rms to engage in such activities. Research in this area identi<sup>fi</sup>ed the existence of a systematic relationship between the probability of manipulation and some key <sup>fi</sup>nancial statement variables. As a result, the analysis of the accounting data of the companies could identify the <sup>fi</sup>rms that engaged in earnings manipulation. In fact, by comparing the accrual levels for one company over different years and under different types of <sup>fi</sup>nancial situations, the researcher was able to identify the abnormal accruals that were closely related to earnings management. Although the models used in the earnings manipulation literature were easy to implement, the <sup>fi</sup>nancial reports of the same company had to be available for several years in order for the analysis to be effective.

Even though the existence of online reviews fraud is acknowledged by online vendors, these online vendors rarely discussed publicly how they should <sup>fi</sup>ght online reviews fraud. There was no commonly agreed conceptual de<sup>fi</sup>nition of online reviews fraud based on which vendors could mandate some appropriate legal action. Similar to the case of digital rights management, vendors believed that one way to <sup>fi</sup>lter online reviews fraud was to never disclose exactly how they identi<sup>fi</sup>ed such fraudulent reviews. They had the apprehension that unethical users would take advantage of such disclosures. Due to the above challenges, a method for the determination of existence of manipulation in online reviews is crucial.

A consumer review consists of two parts: a numerical rating of the product or service being reviewed, as well as textual statements about the product or service. We believe when unethical users manipulate online reviews, they can either post reviews with a high numeric rating or manipulate the textual statements posted in the review. Hence, by investigating how the rating or writing styles change over time, we are able to detect manipulation in online reviews.

## 2.2. Writing style: sentiments and readability

In our context, writing style refers to how consumers construct sentences together when they write online reviews to indicate their passion about their own reviews. We believe that by observing the distribution of the writing style over time, we can infer whether the online reviews for a product is manipulated or not because writing style is unique to every individual. As stated before, in order to really in<sup>fl</sup>uence consumers' decisions about purchases, vendors or publishers or writers need to hire professional manipulators to write reviews while posing as consumers. Even if they do not hire professionals, they need to write the reviews in a consistent and believable manner so that they are able to catch the attention of the consumers and in<sup>fl</sup>uence their purchase decisions. Hence, we expect that the writing styles of manipulators will be different from those of the genuine consumers, and they are more likely to post reviews at certain time periods, such as when ratings decrease. These traits in the writing style of manipulators can help us identify whether a review is genuine or manipulated.

Reviews by individual consumers often express a personal view of their experience about the products. Thus their writing style may be very different from each other. Such differences re<sup>fl</sup>ect the heterogeneity in their culture, education, occupation and so on. However, for manipulators, the situation is different. Thus, across time, the writing style and readability of individual reviews vary and should be random when reviews are posted by real customers. However, if reviews are consistently monitored and posted by manipulators in certain circumstances, such as observing a decrease rate in online reviews, then the observed reviews will be a blend of true customer reviews and manipulators' reviews; hence the writing styles of observed reviews will not be random with the existence of manipulators.

We focus on two different ways of evaluating writing styles — sentiments and readability. In the attempt to write reviews that customers will believe and act upon, manipulators are likely to use certain persuasion strategies. Persuasion is the use of appeals to convince a listener or reader to think or act in a particular way. In ancient Greece, the art of using language as a means to persuade was called rhetoric. The Greek philosopher Aristotle (384–322 BC) set forth an extended treatise on rhetoric that still attracts great interest and careful study. His treatise on rhetoric discussed not only the elements of style and delivery, but also emotional appeals (pathos) and character appeals (ethos) [12]. He identi<sup>fi</sup>ed three main forms of rhetoric:

– ethos: how the character and credibility of a speaker/writer could in<sup>fl</sup>uence an audience to consider him/her to be believable.

– pathos: the use of emotional appeals to alter the audience's judgment. This could be done through the use of metaphors, emotive language, and sentiments that evoked strong emotions in the audience.

– logos: the use of reasoning to construct and support an argument (e.g., use of statistics, mathematics, and logic).

Manipulators are likely to use sentiments to slant reviews (i.e., write or present in a biased manner) so as to in<sup>fl</sup>uence a potential reader's purchase behavior. The use of such a slanting behavior is common in public relations, lobbying, law, marketing, professional writing and advertising where the goal of the writer is to in<sup>fl</sup>uence the third party's opinion or belief. For example, Kahn and Kenney [24] conducted content analysis of campaign coverage in major newspapers for 67 incumbent Senate campaigns between 1988 and 1992, and found that the papers' editorial endorsements signi<sup>fi</sup>cantly affected the tone (i.e., positive, neutral, or negative) of the incumbent coverage, and the number of criticisms published about incumbents. Such editorial slants in turn in<sup>fl</sup>uenced voters' decisions in the elections. Likewise, Gurun and Butler [19] found that when local media reported news about local companies, they used fewer negative words than when they reported about non-local companies. As the local companies spent more on advertising, the local media had more positive slant towards them. The researchers reported that on an average, an increase in local media slant by one standard deviation was associated with a 3.59% increase in the market value of the <sup>fi</sup>rm. From these examples it might be reasonable to assume that in the context of online reviews, manipulators would tend to use positive slant in the form of emotive language such as sentiments to persuade and in<sup>fl</sup>uence customers' choices.

In addition to the sentiments of writing style, another important metric that will be used to discover manipulation is readability. Readability is de<sup>fi</sup>ned as the reading ease that improves the comprehension as well as the retention of the textual material. Readability of textual data indicates the amount of effort that is needed by a person of a certain age and education level to understand a piece of text [40]. Readability is a score generated by a readability formula, and is derived from a mathematical model that assessed the reading ease of different pieces of text by a number of subjects. Based on the syntactical elements and the underlying style, the readability test would provide an indication of the understandability of a piece of text. The score obtained from most readability tests that have been used in the extant literature represented the school grade level that was required to comprehend the piece of text, and to understand the logic of the statement.

## 3. Research method

In this section, we <sup>fi</sup>rst describe the method used for determining the writing style of reviews in this study, and follow that up with the method for detection of manipulation of reviews.

<table><tr><td>ASIN</td><td>AverageRating</td><td>TotalReviews</td><td>Rating</td><td>HelpfulVotes</td><td>CustomerId</td><td>TotalVotes</td><td>RevDate</td><td>Summary</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>2</td><td>A3UN6WX5RR02AG</td><td>5</td><td>2004-10-10</td><td>Fantastically Fantastic</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>2</td><td>A3UN6WX5RR02AG</td><td>5</td><td>2004-10-10</td><td>The Best Book Ever!</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>3</td><td>A3UN6WX5RR02AG</td><td>5</td><td>2005-03-08</td><td>Fire saved our clan!</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>2</td><td>A3UN6WX5RR02AG</td><td>3</td><td>2005-01-18</td><td>The Darkest Hour</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>2</td><td>A3UN6WX5RR02AG</td><td>4</td><td>2004-10-26</td><td>Awesome......</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>5</td><td>A3UN6WX5RR02AG</td><td>6</td><td>2005-02-06</td><td>The Darkest Hour</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>2</td><td>A3UN6WX5RR02AG</td><td>3</td><td>2004-11-25</td><td>An Amazing Story</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>4</td><td>6</td><td>A3UN6WX5RR02AG</td><td>11</td><td>2005-02-15</td><td>Loved the series</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>3</td><td>A3UN6WX5RR02AG</td><td>4</td><td>2004-12-12</td><td>Warrior 6: The Darkest Hour</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>1</td><td>A3UN6WX5RR02AG</td><td>8</td><td>2004-10-06</td><td>Number6</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>3</td><td>A3UN6WX5RR02AG</td><td>4</td><td>2004-10-20</td><td>Can Fire save save the clan?</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>4</td><td>A3UN6WX5RR02AG</td><td>5</td><td>2004-10-10</td><td>Terrific!!!</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>3</td><td>A3UN6WX5RR02AG</td><td>4</td><td>2005-04-24</td><td>A wonderful series, a wonderful book!</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>6</td><td>A3UN6WX5RR02AG</td><td>6</td><td>2005-03-24</td><td>A Stunning Read</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>5</td><td>A3UN6WX5RR02AG</td><td>6</td><td>2004-11-14</td><td>One of the best books EVER!!!!!!!</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>4</td><td>A3UN6WX5RR02AG</td><td>4</td><td>2005-07-03</td><td>A Prophecy Completed</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>1</td><td>A3UN6WX5RR02AG</td><td>2</td><td>2004-11-07</td><td>Erin Hunter: Books sensational!!</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>2</td><td>A3UN6WX5RR02AG</td><td>8</td><td>2005-02-22</td><td>Great Book</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>3</td><td>A3UN6WX5RR02AG</td><td>4</td><td>2005-01-22</td><td>!!!!!!!!!</td></tr><tr><td>006000074</td><td>5.0</td><td>55</td><td>5</td><td>5</td><td>A3UN6WX5RR02AG</td><td>7</td><td>2005-02-19</td><td>The Best Book Yet!!!</td></tr><tr><td>ASIN</td><td>AverageRating</td><td>TotalReviews</td><td>Rating</td><td>HelpfulNotes</td><td>CustomerId</td><td>TotalNotes</td><td>RevDate</td><td>Summary</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>0</td><td>A3UL5K3T2T9BBG</td><td>1</td><td>2004-03-08</td><td>Monster</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2003-04-03</td><td>Monster</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>0</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2003-10-02</td><td>Great Book</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>3</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2003-11-12</td><td>MONSTER</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>2</td><td>2004-05-27</td><td>My Book Review of Monster</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2004-11-10</td><td>Monster</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-01-26</td><td>Sad but Inspiering</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-02-17</td><td>The Best Book Ive Ever Read</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-03-25</td><td>Monster Review</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-03-25</td><td>Monsters in jail</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-03-25</td><td>A heart warming tale of a boy in prison</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-03-25</td><td>Its Straight</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-03-25</td><td>A typical monster</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-03-25</td><td>Complete and Total Admiration</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-03-25</td><td>Monster Review</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-02-25</td><td>Monster- by Z. Jaquandra Motisha</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-03-25</td><td>Jake Berenson</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-03-25</td><td>Bud country review</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2005-03-25</td><td>Monster Review</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>2</td><td>A3UN8wX5RR02AG</td><td>2</td><td>2002-02-21</td><td>My review for Monster, by: Walter De Myers</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2002-03-20</td><td>MONSTER</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>0</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2002-06-04</td><td>Steve Harmon=Monster</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2002-11-25</td><td>Buy This Book NOW!</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>0</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2001-09-11</td><td>Monster_TLK</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>1</td><td>A3UN8wX5RR02AG</td><td>2</td><td>2002-12-13</td><td>***Monster***</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>5</td><td>A3UN8wX5RR02AG</td><td>6</td><td>2001-04-24</td><td>This Book Rocks......Great Insitell!</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2001-06-03</td><td>Monster</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2001-06-04</td><td>Monster By Walter Dean Myers</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>0</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2001-10-30</td><td>Monster by David N.</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>4</td><td>1</td><td>A3UN8wX5RR02AG</td><td>2</td><td>2001-11-30</td><td>Monster</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>0</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2003-01-16</td><td>An exciting book</td></tr><tr><td>0064407314</td><td>4.5</td><td>466</td><td>5</td><td>1</td><td>A3UN8wX5RR02AG</td><td>1</td><td>2002-12-13</td><td>MY REVIEW ON MONSTER</td></tr></table>

Fig. 3. Manipulated reviews posted by the same customer for one book item.

Fig. 4. Manipulated reviews posted by the same customer for one book item.

## 3.1. Writing style measurements

## 3.1.1. Readability

In this research, the readability of the reviews or the reader's ability to comprehend a text is ascertained using the Automated Readability Index (ARI) [36]. Past research in the <sup>fi</sup>eld of information science made use of readability tests for studying the qualitative characteristics of several types of texts [14,25,32]. The ARI is one of the major readability tests that were used to evaluate the readability of a text by decomposing the text into its basic structural elements. We chose this measure because unlike other indices, the determination of ARI relied on the number of characters per word, rather than the number of syllables per word. Since, the number of characters in a word could be more easily and accurately determined than the

## Customer Review

15 of 16 people found the following review helpful:

I think the book is very good and everyone should read it!, October 14, 1999 By A Customer

## This review is from: Z for Zachariah (Mass Market Paperback)

The good thing about this book is it starts out right in the action, thats what I like about books. This book starts you out in a families valley that they live in. Everything is going well when suddenly a strange green cloud peaks at the tip of the valley. The parents of Ann Burden(the main-character telling the story) tell her that they are going out of the valley and into town to see what happened. They go out but they never come back. But before they left, her brother jumped into the back of the truck without the parents knowing. The dog loyes the boy so much that it runs after him and it never comes back either until the middle of the book. But while this is all going on she is getting a long all by herself when a figure keeps getting closer and closer to the valley. She investigates to find it to be a scientist who has a biochemical suit. It protects him from the radiation. She hides in a cave because she is afraid that he might do something to her. It is a very good book to read.

I think the book is yery good and keeps your attention. The only bad thing is that it is not a good book for someone who is not over 12 because you really can't understand some of the technical terms but thats about it

I recommend this book to any student interested in a science-fiction novel and it would interest anybody else who would be interested in what the world may very well be like in the next century. I also recommend this book to teachers because they might be interested in sharing this book with the class. It is a real mindboggler in how the plot takes you right into the story.

## Fig. 5. An example of review posted by the same anonymous customer for a book

![](/api/attachments/6UNSMSDS/fulltext/images/e288eecae6a01f832f1d3c3da37f297fa544655cf01daa6da2bb22a2585b5976.jpg)  
Fig. 6. Negative review posted by manipulator.

number of syllables per word, this measure was subjected to a lower error rate as compared to other readability measures. The ARI is calculated using the following formula [36]:

ARI 4:71 Total number of characters=Total number of words 0:5

Total number of words=Total number of sentences −21:43

The value of the index approximated the minimum grade level of education that was needed to comprehend a piece of text. For instance, a score of 8.3 for the ARI for a piece of text indicated that the text could be understood by an average 8th grade student in the United States.

The readability of the review could also in<sup>fl</sup>uence the size of a writer's audience. For genuine consumers that posted reviews in order to share their evaluation of the product, the readability of the reviews might not be of great concern. In fact, the readability of a review written by a genuine customer should be random due to the variations in customers' educational background, clarity of expression, ability to communicate their thoughts appropriately, and so on. But for manipulators, whose intention would be to try to reach a large and unselected audience successfully, readability would be of great concern.

Intuitively, manipulated reviews should be consistent in terms of readability.

## 3.1.2. Measurement of sentiment in a review

Sentiment (or polarity) analysis is used to identify positive and negative language in the text. Extraction of sentiment from text has been widely studied by researchers belonging to the text mining community. Typically, the techniques employed include a combination of machine learning, natural language processing, and bags-ofwords approach [6,28,33,38]. Past research on sentiment analysis has used automatically generated sentiment lexicons, in which a list of seed words was used to determine whether a sentence contained positive or negative sentiments. Then, the polarity (i.e., positive or negative direction) of an opinion was determined on the basis of the words that were present in the review. In terms of sentiment mining of reviews, a simple machine learning approach for classifying products and services as recommended (thumbs up) or not recommended (thumbs down) was proposed by Turney [38]. Another approach for the semantic classi<sup>fi</sup>cation of product reviews was presented by Dave et al. [6].

The text mining approach that we adopted in this research made use of a simple yet ef<sup>fi</sup>cient standard term frequency measure that is commonly used by the Information Retrieval community [35]. Using this technique, we extracted strong (or weak) positive (or negative) sentiment terms from each review. We employed a standard term frequency measure to determine the polarity of the review, and also estimated the strength of sentiments in each review. The review texts were evaluated using a dictionary of 1635 positive words and 2005 negative words taken from the General Inquirer lexicon [37]. In addition, we drew upon the research conducted by Archak et al. [1], and extracted a list of 40 strong positive and 30 strong negative terms (including some phrases) from the reviews available on Amazon.com.<sup>5</sup> The list of words from the General Inquirer lexicon formed the list of ordinary (or weak) sentiment terms whereas those extracted from Archak et al. [1] formed the list of strong sentiment terms. Based on these two lists of seed words, we calculated the number of occurrences of sentiment terms/phrases in the review. Various types of sentiment scores for the ith review calculated using the following general formula given by Eq. (1):

![](/api/attachments/6UNSMSDS/fulltext/images/ee566e6f406ae4365444b986d32661874a355e1187fd54fb0bac9813aad1e035.jpg)  
Fig. 7. Same reviewer that posted reviews for a single book.

$$
s e n t i \_ s c o r e _ {i} = \frac {s e n t i \_ t y p e _ {i}}{s e n t i \_ t o t _ {i}}\tag{1}
$$

where senti\_type belongs to {str\_pos , str\_neg , ord\_pos , ord\_neg }, str\_pos is the number of strong positive terms, str\_neg is the number of strong negative terms, ord\_pos is the number of ordinary positive terms, and ord\_neg is the number of ordinary negative terms present in the review. The total number of sentimental terms (senti\_tot ) is determined by the sum of str\_pos , str\_neg , ord\_pos , and ord\_neg . In particular, we calculate the following types of sentiment scores for any review i:

Strong positive sentiment $\mathrm { s c o r e } { = } s t r \_ p o s _ { i } / s e n t i \_ t o t _ { i }$

Strong negative sentiment score=str\_neg<sub>i</sub>/ senti\_tot<sub>i</sub>

Ordinary positive sentiment score=ord\_pos /senti\_tot

Ordinary negative sentiment score=ord\_neg<sub>i</sub>/senti\_tot<sub>i</sub>

Ordinary sentiment score=(ord\_pos +ord\_neg )/senti\_tot

Strong sentiment score = (str\_pos<sub>i</sub> + str\_neg<sub>i</sub>) / senti\_tot

These scores are used to detect the existence of reviews manipulation.

## 3.2. Measurement of manipulation

If reviews were indeed written by customers, then the writing style of the reviews would be random due to the diverse background of the customers. Therefore, a simple and intuitive way to detect the randomness of the review was to conduct a statistical test of randomness of writing styles and ratings of the reviews over time for each product that was reviewed. A non-random result in such a test would indicate the existence of manipulation. For this purpose, we adopted the Wald–Wolfowitz (Runs) test to check the randomness of ratings, sentiments, and readability of the reviews over time.

## 3.2.1. Wald–Wolfowitz (Runs) test

If reviews were indeed written by customers, then the writing style of the reviews would be random due to the diverse background of the customers. Therefore, a simple and intuitive way to detect the randomness of the review is to conduct a statistical test of randomness of writing styles and ratings of the reviews across time for each product that was reviewed. A non-random result in such a test would indicate the existence of manipulation. For this purpose, we adopted the Wald–Wolfowitz (Runs) test to check the randomness of ratings, sentiments, and readability of the reviews over time.

Table 1 Descriptive statistics of books included in the sample.

<table><tr><td>Variable</td><td>Median</td><td>Mean (SD)</td></tr><tr><td> $\ln(Price)$ </td><td>2.41</td><td>2.54 (0.58)</td></tr><tr><td> $\ln(SalesRank)$ </td><td>10.11</td><td>9.92 (2.00)</td></tr><tr><td>AvgRating</td><td>4.50</td><td>4.18 (0.55)</td></tr><tr><td> $\ln(TotalReviews)$ </td><td>4.01</td><td>4.21(0.75)</td></tr><tr><td>TotalReviews</td><td>51.00</td><td>290.08 (715.30)</td></tr><tr><td>Helpful votes</td><td>2.00</td><td>6.08 (18.75)</td></tr></table>

The Wald–Wolfowitz test, also known as the Runs test for randomness, is used to test the hypothesis that a series of numbers is random [18]. The runs test is a non-parametric statistical test, therefore the interpretation of the results does not depend on any parameterized distributions. A ‘run’ of a sequence simply refers to a segment consisting of adjacent equal elements. For example, the sequence:

$$
+ + + + - - - - + + + - - - - + + + + + + - - - - -
$$

consists of 6 runs, three of which consist of + and the other three consist of −.To carry out the test, the total number of runs (R) is computed along with the number of positive and negative runs. To simplify the computations, the data are <sup>fi</sup>rst centered around their mean.<sup>6</sup> A positive run is determined as a sequence of values that are greater than zero, and a negative run is identi<sup>fi</sup>ed as a sequence of values that are less than zero. The number of positive runs (n) and negative runs (m) are checked to see if they are distributed equally in time. The test statistic is asymptotically normally distributed. The large sample test statistic Z is given by $\begin{array} { r } { Z = \frac { ( R - E ( R ) ) } { \sqrt { V ( R ) } } } \end{array}$ , where $\begin{array} { r } { E ( R ) = \frac { 2 n m } { n + m } + 1 } \end{array}$ , and $\begin{array} { r } { V ( R ) = \frac { 2 n m ( 2 n m - n - m ) } { ( n + m ) ^ { 2 } ( n + m - 1 ) } } \end{array}$ If the Runs test result is statistically signi<sup>fi</sup>cant, this means that the series of reviews posted is non-random. The Runs test result is used as a manipulation index for each product and is represented by a binary scale of 1 and 0, where 1 represents non-random (with manipulation) and 0 represents random (without manipulation). For each product, there will be a manipulation index for each of the three variables — ratings, sentiments, and readability. For the sentiment manipulation index, avg\_senti\_runs for each product j is computed as shown in Eq. (2):

$$
a v g \_ s e n t i \_ r u n s _ {j} = \frac {\left(s t r \_ p o s \_ r u n s _ {j} + s t r \_ n e g \_ r u n s _ {j} + o r d \_ p o s \_ r u n s _ {j} + o r d \_ n e g \_ r u n s _ {j}\right)}{4}\tag{2}
$$

where str\_pos\_runs is the Runs test score for strong positive sentiments in product j, str\_neg\_runs is the Runs test score for strong negative sentiments in product j, ord\_pos\_runs is the Runs test score for ordinary positive sentiments product j, and ord\_neg\_runs is the Runs test score for ordinary negative sentiments in product j.

## 3.2.2. Evidence of manipulation discovered by Runs test

To verify if our Runs test method is able to detect manipulative activity, a manual inspection is conducted. Amongst all the items that were detected to have non-random reviews, we conduct a manual check to see if the products we identi<sup>fi</sup>ed are indeed products with manipulated reviews, e.g., multiple reviews posted by the same per son for the same book item. From the items that were found to have non-random reviews, we found abundant evidence of such activities. Figs. 3 and 4 present examples of the evidence found for different book items. ‘ASIN’ refers to the unique identi<sup>fi</sup>cation of a book while

![](/api/attachments/6UNSMSDS/fulltext/images/43675413fdaa0805128abdc258081fb20dfd3594ce46246530e0eb5f31ff86da.jpg)  
Fig. 8. Distribution of readability scores for manipulated reviews.

CustomerID is the unique identity of the customer. The <sup>fi</sup>gures showed that there have been cases where an individual has posted several reviews for the same book item. These <sup>fi</sup>gures gave us con<sup>fi</sup>- dence on the effectiveness of Runs test to detect manipulation in reviews.

Fig. 5 presents an example of a review posted by a manipulator and as we see, it is dif<sup>fi</sup>cult to tell if this review is posted by a manipulator by simply reading the textual content unless we place it in sequence and conduct our test. Fig. 6 shows a negative review posted by a manipulator who has posted negative reviews for a book. Finally, Fig. 7 shows three reviews posted by a manipulator who uses similar style in the review title and sentiments for all three reviews.

## 4. Numerical experimentation

## 4.1. Data description

The data used in this research were gathered from Amazon.com using its Amazon Web Services (AWS) in July 2005. The reason for picking Amazon.com for the data was because past research had investigated manipulation of online reviews for this site [7]. The data analysis was based on data collected prior to July 15, 2005. For each book, we collected data related to the title, price, sales, and reviews. Speci<sup>fi</sup>cally, for each customer review of the book, we gathered the review date, the numeric rating for the book, the number of helpful votes, the total number of votes, and the original text of the review. To have a meaningful Runs test, we retained books that had 30 or more reviews (among 32,878 books with 967,075 reviews). The <sup>fi</sup>nal dataset consisted of information related to 4490 books, with 610,713 online reviews.

The numeric ratings for each review were on a 1-star to a 5-star scale where a 1-star corresponded to least satis<sup>fi</sup>ed, and a 5-star corresponded to most satis<sup>fi</sup>ed with the product. Product sales rank was shown in descending order where a rank of 1 represented the best selling product. Consequently, there was a negative correlation between product sales and sales rank. We used sales rank as a proxy for product sales (with the opposite sign). Some descriptive statistics is provided in Table 1.

Fig. 8 shows the histogram of the review readability scores for manipulated reviews, and it follows a bimodal distribution. On the contrary, Fig. 9 shows the same for non-manipulated reviews, and it approximately follows a normal distribution. This result of the bimodal distribution of the readability scores of manipulated reviews may be due to the existence of two distinct classes of reviews writers, namely real customers and manipulators.<sup>7</sup> In addition, as we explained before, it is more likely for manipulators to enter the scene when they observe a negative review. Fig. 10 shows that indeed this is true. The conditional probability of observing a positive review after an item received a negative review is 72%, and this is almost 2.6 times that of the conditional probability of observing a negative review after an item received a negative review.

![](/api/attachments/6UNSMSDS/fulltext/images/1b344243de8b7bb9fa726bf725f17842b23219d6c39cbb47c6c8b9a408b5e16f.jpg)  
Fig. 9. Distribution of readability scores for non-manipulated reviews

## 4.2. Determination of manipulation in reviews

Table 2 summarizes the results of sentiment manipulation that are obtained when the Runs test was used for books with different sales rank. Out of 4490 books, the sentiment expressed in reviews of 463 books was found to be non-random. The non-randomness of these reviews could be due to the manipulation of these reviews by interested parties. It seemed that manipulation was less prevalent for the most popular (i.e., sales rank between 1 and 100) and most unpopular books (i.e., sales rank more than 10,000). This indicated that manipulation of reviews of books was not affected by the popularity of the book.

## 4.3. Impact of manipulation in reviews on sales

We used a linear regression model to determine if consumers were aware of the manipulations present in the reviews, and if they were able to distinguish between manipulated reviews from nonmanipulated reviews. In fact, if consumers were able to differentiate a book review with manipulation from one without manipulation, then with all other information remaining same, a book whose review was being manipulated would either be punished (i.e., resulting in a decrease in sales or an increase in sales rank) or would not be rewarded (i.e., resulting in no change in sales or sales rank). However, if consumers were deceived by manipulation, then with all the other information remaining same, a book whose review was being manipulated would be rewarded with an increase in sales or a decrease in sales rank. In the regression model, we examined the impact of manipulation in ratings, sentiments, and readability on the sales rank of the book. Average rating was included as a control variable because previous studies had shown that products with a high average rating enjoyed a high demand. Price was included as a control variable in all regression models because it reduced the demand for a book. The total number of reviews for a book was included as well to control for the demand of the book. Amazon.com did not disclose the actual sales for the books available on their website. Instead, they reported a sales rank for each book, which ranked the demand for a book relative to other books in its category. Prior research in economics and marketing [5,13] had studied the association between these sales ranks and demand levels for products based on the experimentally observed fact, and had found that the variation of demand with respect to sales rank followed a Pareto distribution [5]. Based on this observation, it was possible to use the log of product sales rank as a proxy for the log of product demand. Given the linear relationship between ln(Sales) and ln(SalesRank), we used ln(SalesRank) as a proxy for sales of books in the log-linear regression models. To control the potential heterogeneity in the existence of manipulation across books with different popularities (as indicated in Table 2), some sales rank dummies were included in the model as well. Before checking the impact of manipulation on online reviews, we <sup>fi</sup>rst examined the basic model in which the indices representing manipulation were not included (Eq. (3)). The <sup>fi</sup>nal regression model that included the manipulation indices is shown in Eq. (4). Model 3 is the basic model where we study the impact of online reviews on sales. Model 4 studies the impact of manipulation of reviews on sales.

![](/api/attachments/6UNSMSDS/fulltext/images/61517c2bf06395fc0eb8c107168af1df8286427c7549ebb65f845d65dc590284.jpg)  
Fig. 10. Conditional probability of review characteristics.

$$
\begin{array}{l} \ln (\text { SalesRank }) = \gamma_ {1} \ln (\text { Price }) + \gamma_ {2} \ln (\text { TotalReviews }) + \gamma_ {3} (\text { AvgRating }) \\ + \gamma_ {4} (s r 2 \_ d u m m y) + \gamma_ {5} (s r 3 \_ d u m m y) + \gamma_ {6} (s r 4 \_ d u m m y) + \varepsilon \end{array} \tag {3}
$$

$$
\begin{array}{l} \ln (\text {SalesRank}) = \beta_ {1} \ln (P r i c e) + \beta_ {2} \ln (\text {TotalReviews}) + \beta_ {3} (\text {AvgRating}) \\ \quad + \beta_ {4} (\text {rating\_runs}) + \beta_ {5} (\text {avg\_senti\_runs}) + \beta_ {6} (\text {readability\_runs}) (4) \\ \quad + \beta_ {7} (\text {sr2\_dummy}) + \beta_ {8} (\text {sr3\_dummy}) + \beta_ {9} (\text {sr4\_dummy}) + \varepsilon \end{array}
$$

where Price denotes the price of each book, TotalReviews denotes the total number of reviews for each book, AvgRating denotes the average consumer rating for each book, rating\_runs denotes the Runs test result of the rating for each book and is equal to 1 if the test result is non-random, avg\_senti\_runs denotes the Runs test result of the average sentiment for each book and is equal to 1 if the test result is nonrandom, readability\_runs denotes the Runs test result of the readability for each book and is equal to 1 if the test result is non-random, sr2\_dummy denotes the dummy variable that is equal to 1 for books with sales rank greater than 101 and less than 1000, sr3\_dummy denotes the dummy variable that is equal to 1 for books with sales rank greater than 1001 and less than 10,000, sr4\_dummy denotes the dummy variable that is equal to 1 for books with sales rank greater than 10,000. Recall that the product sales rank is shown in descending order where 1 represented the best selling product.

Table 2  
Results of Runs test on randomness of sentiments expressed in book reviews.

<table><tr><td></td><td>Number of books</td><td>Percentage of books with non-random sentiments in reviews</td></tr><tr><td>1≤Sales rank&lt;100</td><td>53</td><td>9.4%</td></tr><tr><td>101≤Sales rank&lt;1000</td><td>292</td><td>12.3%</td></tr><tr><td>1001≤Sales rank&lt;10,000</td><td>3076</td><td>10.3%</td></tr><tr><td>Sales rank&gt;10,001</td><td>1069</td><td>9.9%</td></tr><tr><td>Total</td><td>4490</td><td>10.31%</td></tr></table>

Table 3  
Impact of manipulation of reviews on sales

<table><tr><td>Variable</td><td>Coefficient</td><td>Coefficient</td></tr><tr><td> $\ln(Price)$ </td><td>-0.0254</td><td>-0.0254</td></tr><tr><td> $AvgRating$ </td><td>-0.1403***</td><td>-0.1348***</td></tr><tr><td> $\ln(TotalReviews)$ </td><td>-0.2873***</td><td>-0.2905***</td></tr><tr><td> $Rating\_runs$ </td><td></td><td>0.0356</td></tr><tr><td> $avg\_senti\_runs$ </td><td></td><td>-0.2002+</td></tr><tr><td> $readability\_runs$ </td><td></td><td>-0.0439</td></tr><tr><td> $sr2\_dummy$ </td><td>1.2923***</td><td>1.2800**</td></tr><tr><td> $sr3\_dummy$ </td><td>4.3210***</td><td>4.3057***</td></tr><tr><td> $sr4\_dummy$ </td><td>6.9803***</td><td>6.9629***</td></tr><tr><td>Intercept</td><td>7.0961***</td><td>7.1175***</td></tr><tr><td>Adjusted R-square</td><td>66.19%</td><td>66.19%</td></tr><tr><td>N</td><td>4490</td><td>4490</td></tr></table>

\*\*\*pb.001; \*\*pb.01; \*pb.05; <sup>+</sup>pb.10.

Therefore, the negative correlation between any variable and sales rank indicated that a high value of that variable was associated with higher sales.

Table 3 presents the results obtained using the basic model. We observe that all variables associated with reviews are signi<sup>fi</sup>cantly associated with sales. For example, the coef<sup>fi</sup>cient of AvgRating is −0.1403 which indicated that the higher the average rating an item had, the better was its sales (since there was a negative correlation between sales rank and sales). Furthermore, the adjusted R-square of the regression model was equal to 0.6619, and it indicated that online reviews could reasonably explain most of the variability in the sales of the books.

Next we studied the impact of reviews manipulation on sales. The coef<sup>fi</sup>cients for rating\_runs, avg\_senti\_runs, and readability\_runs captured the impact of manipulation through ratings, sentiments, and readability on sales respectively. We see that the effect of the manipulation of ratings (para=0.0356) and readability (para= 0.0439) on sales rank is not signi<sup>fi</sup>cant. However, on average, the manipulation of sentiments of reviews had a relatively signi<sup>fi</sup>cant impact on sales rank (para=−0.2001, and p-value≤0.1). This implied that the promotional chat using sentiments in online reviews was effective in generating extra sales for the book. Our interpretation for the non-signi<sup>fi</sup>cant results for rating\_runs and readability\_runs is that it was relatively easier for consumers to detect reviews manipulation through ratings or readability, and hence consumers could undo the impact of manipulation of reviews through ratings and readability. The fact that these variables did not generate any signi<sup>fi</sup>cant negative impact on sales might indicate that the consumers were unsure of whether to trust these reviews. Hence, it seemed that consumers found it challenging to differentiate a manipulated review from a review written by a real customer. Hence, it was likely that consumers ignored such reviews when making their purchase decisions.

Till now, what we have documented is the correlation between the variables that indicated manipulation of reviews and the sales of books. Next, a time lag is introduced between the dependent variable (measured at time t+1) and the variables representing manipulation (measured at time t) to determine if manipulation at current time in<sup>fl</sup>uenced the sales of the books in future time. Thus, the baseline model is transformed to Eq. (5):

Table 4  
Descriptive statistics of books included in the pooled sample.

<table><tr><td>Variable</td><td>Median</td><td>Mean (SD)</td></tr><tr><td> $\ln(Price)$ </td><td>2.77</td><td>1.26 (1.43)</td></tr><tr><td> $\ln(SalesRank)$ </td><td>7.94</td><td>10.48 (11.47)</td></tr><tr><td>AvgRating</td><td>4.01</td><td>3.84 (0.86)</td></tr><tr><td> $\ln(TotalReviews)$ </td><td>4.85</td><td>6.41 (6.87)</td></tr><tr><td>TotalReviews</td><td>128</td><td>608 (961.50)</td></tr><tr><td>Helpful votes</td><td>0.56</td><td>0.69 (0.21)</td></tr></table>

Table 5  
Impact of manipulation of reviews on pooled sample

<table><tr><td>Variable</td><td>Coefficient</td></tr><tr><td>ln(Price)</td><td>0.0607</td></tr><tr><td>AvgRating</td><td>-0.3089***</td></tr><tr><td>ln(TotalReviews)</td><td>-0.5674***</td></tr><tr><td>rating_runs</td><td>0.0035</td></tr><tr><td>avg_senti_runs</td><td>-0.0628+</td></tr><tr><td>readability_runs</td><td>-0.0573</td></tr><tr><td>sr2_dummy</td><td>3.1450***</td></tr><tr><td>sr3_dummy</td><td>4.6050***</td></tr><tr><td>sr4_dummy</td><td>7.1801***</td></tr><tr><td>Intercept</td><td>8.6596***</td></tr><tr><td>Adjusted R-Square</td><td>69.98%</td></tr><tr><td>N</td><td>1693</td></tr></table>

\*\*\* pb.001; \*\* pb.01; \* pb.05; <sup>+</sup> pb.10.

$$
\begin{array}{l} \ln (\text {SalesRank}) _ {t + 1} = \beta_ {1} \ln (\text {Price}) _ {t + 1} + \beta_ {2} \ln (\text {TotalReviews}) _ {t + 1} \\ + \beta_ {3} (\text {AvgRating}) _ {t + 1} + \beta_ {4} (\text {rating} _ {-} \text {runs}) _ {t} + \beta_ {5} (\text {avg} _ {-} \text {senti} _ {-} \text {runs}) _ {t} \\ + \beta_ {6} (\text {readability} _ {-} \text {runs}) _ {t} + \beta_ {7} (\text {sr2} _ {-} \text {dummy}) _ {t + 1} + \beta_ {8} (\text {sr3} _ {-} \text {dummy}) _ {t + 1} \\ + \beta_ {9} (\text {sr4} _ {-} \text {dummy}) _ {t + 1} + \end{array} \tag {5}
$$

To test this model, we collected a panel dataset (pooled data) that was collected over 5 months from 8/9/05 to 10/1/06. For each book item, we collected the price, sales and review information at approximately three-day intervals. We identi<sup>fi</sup>ed every interval by a unique sequence number. Finally, we obtained 26 batches of review and item-level data in total. When we selected book items with at least 30 reviews, the <sup>fi</sup>nal panel dataset consisted of information related to 1693 books and 37,161 online reviews. The descriptive statistics of the panel data are shown in Table 4.

Table 5 shows the results using the panel data as pooled sample. The results shown in Table 5 are qualitatively similar to those in Table 3. The effect of manipulation through ratings and readability are still found to be ineffective in the time lagged model. On the other hand, the manipulation using sentiments was found to have a signi<sup>fi</sup>cant positive impact on sales (para=−0.0628 and pvalue≤0.10), which indicated that vendors were able to in<sup>fl</sup>uence the future book sales by manipulating online reviews.

## 5. Discussion of results

Online reviews can be a powerful promotional tool for marketing communication. Marketers and vendors have used this medium because it provides a cheap and impactful channel to reach their customers. Marketers are known to take advantage of networks of in<sup>fl</sup>uence among customers to in<sup>fl</sup>uence the purchase behavior of potential buyers. Reports have shown that promotional chat has in<sup>fi</sup>ltrated the online review forums.<sup>8</sup> However, it is not clear whether such knowledge sharing sites where customers review products and provide advice to each other are fertile grounds for running promotional campaigns of manipulators. This paper examines the extent and the impact of such manipulative actions in the online reviews environment.

In this paper, we present a simple but effective way to detect the manipulation of reviews. Our research shows that manipulators use both numeric ratings and textual comments to manipulate online reviews. However, the manipulation of ratings alone is not effective in in<sup>fl</sup>uencing the sales of books as consumers are able to discover such promotional acts. However, manipulation through a component of writing style that re<sup>fl</sup>ects the background of an individual, such as sentiments, is able to signi<sup>fi</sup>cantly in<sup>fl</sup>uence a consumer's purchase decision. An important bene<sup>fi</sup>t of this approach is that one can detect the existence of manipulation in the reviews, and assess the effectiveness of manipulation of reviews in generating sales, without having access to the backend data about customers' identity that is recorded by e-commerce websites.

The method proposed in this paper assumes that if the reviews were written by real customers, the writing styles would be random because of the diverse background of customers. However, this assumption may be valid for certain product categories like electronics but not necessarily so for other categories of products unlike books. Also, We realize that review ratings might not follow a random distribution due to the self-selection processes suggested by Li and Hitt [26]. For popular products, consumers might overlook review ratings due to the presence of information cascade. However, we believe that such biases in behavior will have a limited impact on sentiments and readability of reviews. Overall, we believe that using the Runs test to detect the manipulated products through assessment of the randomness of ratings, readability, and sentiments, is an important step in discovering the impact of manipulation of reviews.

This paper provides a new direction in the detection of online reviews manipulation. As we have elaborated before, even though online reviews manipulation has become a serious problem in the industry, there is no commonly agreed conceptual model for detecting this. At the same time, various online vendors hesitate to openly discuss how they <sup>fi</sup>ght such fraudulent reviews. The reason could be that they believe that an open discussion of how they <sup>fi</sup>ght online reviews manipulation will help manipulators learn how to trick their systems. This may encourage manipulators to game the system since the penalties are few (if any), and the amount of pro<sup>fi</sup>t that can be generated by succeeding in this gaming outweigh the costs. The responsibility of uncovering online reviews manipulation therefore falls upon the shoulders of researchers. Our research sheds light on how serious reviews manipulation is and how to detect reviews manipulation using publicly available data on online reviews of books.

However, one challenge for this research is still the lack of available data. For example, for a given review, some researchers may believe it is a manipulated review, whereas others may think that it is a review written by a real customer. Deciding between a manipulated and a non-manipulated review is a subjective matter, and so future researchers should collaborate with industry partners to come up with a clearly labeled dataset indicating manipulated and nonmanipulated reviews so that researchers can use this benchmark data to build various models to identify fraudulent reviews. Also, future research should focus on uncovering the differences between perceived fraudulent reviews and actual fraudulent reviews, and also study the impact of consumers' backgrounds in in<sup>fl</sup>uencing consumers' perceptions about fraudulent reviews.

## References

[1] N. Archak, A. Ghose, P.G. Ipeirotis, Show me the money! deriving the pricing power of product features by mining consumer reviews, Proceedings of the 13th International Conference on Knowledge Discovery and Data Mining, 2007, pp. 56–65.

[2] M.D. Beneish, The detection of earnings manipulation, Financial Analysts Journal 55 (5) (1999) 24–36

[3] B. Bickart, R.M. Schindler, Internet forums as in<sup>fl</sup>uential sources of consumer information, Journal of Interactive Marketing 15 (3) (2001) 31–40.

[4] J.A. Chevalier, A. Goolsbee, Measuring prices and price competition online: amazon.com and BarnesandNoble.com, Quantitative Marketing and Economics 1 (2) (2003) 203–222.

[5] J.A. Chevalier, D. Mayzlin, The effect of word of mouth online: online book reviews, Journal of Marketing Research 43 (3) (2006) 345–354.

[6] K. Dave, S. Lawrence, D.M. Pennock, Mining the peanut gallery: opinion extraction and semantic classification of product reviews Proceedings of the 13th International World Wide Web Conference, 2003, pp. 519–528.

[7] S. David, T.J. Pinch, Six degrees of reputation: the use and abuse of online review and recommendation systemsretrieved from, http://papers.ssrn.com/sol3 papers.cfm?abstract\_id=857505.

[8] C. Dellarocas, The digitization of word-of-mouth: promise and challenges of online feedback mechanisms, Management Science 49 (10) (2003) 407–1424.

[9] C. Dellarocas, N. Awad, X. Zhang, Exploring the value of online reviews to organi zations: implications for revenue forecasting and planning, Proceedings of the 25th International Conference on Information Systems, ACM press, New York 2004, pp. 379–386.

[10] W. Duan, B. Gu, A. Whinston, Do online reviews matter? An empirical investigation of panel data, Decision Support Systems 45 (4) (2008) 1007–1016.

[11] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Information Systems Research 19 (3) (2008) 291–313.

[12] B. Garsten, Saving Persuasion: A Defense of Rhetoric and Judgment, Harvard University Press, Boston, 2005.

[13] A. Ghose, A. Sundararajan, Evaluating pricing strategy using ecommerce data: evidence and estimation challenges, Statistical Science 21 (2) (2006) 131–142.

[14] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. (2010) IEEE Transactions on Knowledge and Data Engineering, IEEE Computer Society, Washington, DC

[15] D. Godes, D. Mayzlin, Using online conversation to study word of mouth communication, Marketing Science 23 (4) (2004) 545–560.

[16] D. Gruhl, R. Guha, R. Kumar, J. Novak, A. Tomkins, The predictive power of online chatter, Proceedings of the 11th International. Conference on Knowledge Discovery in Data Mining, New York, NY, USA, 2005, pp. 78–87.

[17] L. Guernsey, Suddenly, everybody's an expert on everything, The New York Times, February 3 2000.

[18] D.N. Gujarati, Basic Econometrics, 4th edition McGraw–Hill, Inc., New York, 2003.

[19] U.W. Gurun, A.W. Butler, Don't believe the hype: local media slant, local advertising and <sup>fi</sup>rm value, (2010) retrieved from: http://papers.ssrn.com/sol3/papers. cfm?abstract\_id=1333765.

[20] A. Harmon, Amazon glitch unmasks war of reviewers, The New York Times, February 14 2004.

[21] D.I. Holmes, Authorship attribution, Computers and the Humanities 28 (2) (1994) 87–106.

[23] N. Hu, I. Bose, Y. Gao, L. Liu, Manipulation in digital word-of-mouth: a reality check for book reviews, Decision Support Systems 50 (3) (2011) 627–635.

[24] K.F. Kahn, P.J. Kenney, The slant of the news, American Political Science Review 96 (2) (2002) 381–394.

[25] G.R. Klare, The measurement of readability: useful information for communicators, ACM Journal of Computer Documentation 24 (3) (2000) 107–121.

[26] X. Li, L. Hitt, Self-selection and information role of online product reviews, Information Systems and Economics 19 (4) (2008) 456–474.

[27] Y. Liu, Word of mouth for movies: its dynamics and impact on box of<sup>fi</sup>ce revenue, Journal of Marketing 70 (3) (2006) 74–89.

[28] B. Liu, M. Hu, J. Cheng, Opinion observer: analyzing and comparing opinions on the web, Proceedings of the International Conference on the World Wide Web, 2005 pp. 342-351.

[29] S. Majumdar, D. Kulkarni, C. Ravishankar, Addressing click fraud in content delivery system, retrieved from, Proceedings of the Infocom, 2007 http://www.cs.ucr. edu/\~smajumdar/infocom07.pdf.

[30] D. Mayzlin, Promotional chat on the Internet, Marketing Science 25 (2) (2006) 155–163.

[31] A. Metwally, D. Agrawal, A.E. Abbadi, Using association rules for fraud detection in web advertising networks, Proceedings of the 31st International Conference on Very Large Data Bases, 2005, pp. 169–180.

[32] M.K. Paasche-Orlow, H.A. Taylor, F.L. Brancati, Readability standards for informed-consent forms as compared with actual readability, The New England Journal of Medicine 348 (8) (2003) 721–726.

[33] B. Pang, L. Lee, S. Vaithyanathan, Thumbs up? Sentiment classi<sup>fi</sup>cation using machine learning techniques, Proceedings of the 2002 Conference on Empirical Methods in Natural Language Processing, 2002, pp. 79–86.

[34] S. Roychowdhury, Manipulation of earnings through the management of real activities that affect cash <sup>fl</sup>ow from operations, Unpublished dissertation, University of Rochester, 2004.

[35] G. Salton, M.J. McGill, Introduction to Modern Information Retrieval, , 1983.

[36] R.J. Senter, E.A. Smith, Automated readability indexretrieved from, http://oai.dtic. mil/oai/oai?

verb=getRecord&metadataPre<sup>fi</sup>x=html&identi<sup>fi</sup>er=AD06672731967.

[37] P.J. Stone, D.C. Dunphy, M.S. Smith, D.M. Ogilvie, The General Inquirer: A Computer Approach to Content Analysis, MIT Press, Cambridge, MA, 1966.

[38] P.D. Turney, Thumbs up or thumbs down? semantic orientation applied to unsupervised classi<sup>fi</sup>cation of reviews, Proceedings of the 40th Annual Meeting on Association for Computational Linguistic, 2002, pp. 417–424.

[39] E. White, Chatting a singer up the pop charts, The Wall Street Journal, p. B1 (Oc tober 5 1999).

[40] B.L. Zakaluk, S.J. Samuels, Readability: Its Past, Present, and Future, International Reading Association, Newark, 1988.

![](/api/attachments/6UNSMSDS/fulltext/images/80e38a6986966578ac2cc8215c675e335663a2a82b93249f9517b601c0abce97.jpg)

Nan Hu is an Assistant Professor of Accounting and Finance at the University of Wisconsin at Eau Claire. He is also an Assistant Professor of Information Systems at Singapore Management University. He received his Ph.D from the University of Texas at Dallas. Nan's research focuses on investigating the value implications and market ef<sup>fi</sup>ciency of both traditional information (e.g. company <sup>fi</sup>- nancial report, analyst forecast, corporate governance, etc.) and non-traditional information (e.g. blog opinion, online consumer reviews, etc.), using a combination of theories from accounting, <sup>fi</sup>nance, marketing, information economics, sociology, psychology, and computer science. Nan's research has appeared at JMIS (Journal of Management Information Systems), CACM (Communications of the ACM), JCS (Journal of Computer Security), MISQ (MIS Quarterly), JAAF (Journal of Accounting, Auditing, and Finance), TEM (IEEE Transactions on Engineering Management), JBR (Journal of Business Research), and IT&M (Information Technology and Management).

![](/api/attachments/6UNSMSDS/fulltext/images/737e7ecad72f78ceafbc70362153ae90f0aa6109d72c7256ef1f12d687e6c23e.jpg)

Indranil Bose is an Associate Professor at the School of Business, The University of Hong Kong. He holds a B. Tech. from the Indian Institute of Technology, MS from the University of Iowa, MS and Ph.D. from Purdue University. His research interests are in telecommunications, data mining, information security, and supply chain management. His publications have appeared in Communications of the ACM, Communications of AIS, Computers and Operations Research, Decision Support Systems, Ergonomics, European Journal of Operational Research, Information & Management, Journal of Organizational Computing and Electronic Commerce, Journal of the American Society for Information Science and Technology, Operations Research Letters etc. He is listed in the International Who's Who of Professionals 2005–2006, Marquis Who's Who in the World 2006, Marquis Who's Who in Asia 2007, Marquis Who's Who in Science and Engineering 2007, and Marquis Who's Who of Emerging Leaders 2007. He serves on the editorial board of Information & Management, Communications of AIS, and several other IS journals.

Noi Sian Koh is a Lecturer at the School of Information Technology, Nanyang Polytechnic. She received her Ph.D. in Information Systems from Singapore Management University. Her research interests are in the area of social media content and text mining.

![](/api/attachments/6UNSMSDS/fulltext/images/8a24ec708b212349f5965f4408215b23dddc0b9e2f40e3d529b711a1c7e6f6bd.jpg)

![](/api/attachments/6UNSMSDS/fulltext/images/07eb7751bb2def65d459afd4e5b16bc7d9a8770123e6f3ad590a2576f780a686.jpg)

Ling Liu is an Assistant Professor of Accounting and Finance at the University of Wisconsin at Eau Claire. She received her Ph.D. in Accounting from the University of Texas at Dallas. Her research focuses on market ef<sup>fi</sup>ciency, corpo rate governance, and relative performance evaluation. Ling's research has appeared at DSS (Decision Support System), JAAF (Journal of Accounting, Auditing, and Finance), TEM (IEEE Transactions on Engineering Management), JBR (Journal of Business Research) etc
