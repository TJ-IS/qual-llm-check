---
otero_id: 3526
otero_key: "TN6HB62N"
title: "Bidding for Multiple Keywords in Sponsored Search Advertising: Keyword Categories and Match Types"
authors: "Xiaomeng Du; Meng Su; Xiaoquan (Michael) Zhang; Xiaona Zheng"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0724"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/TN6HB62N/fulltext/images/6c590430cc2b76219b3edaa6e1f22a1564b56841b6f9bcf5e291e39b95f0c728.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Bidding for Multiple Keywords in Sponsored Search Advertising: Keyword Categories and Match Types

Xiaomeng Du, Meng Su, Xiaoquan (Michael) Zhang, http:// orcid.org/0000-0002-7554-5916Xiaona Zheng

Xiaomeng Du, Meng Su, Xiaoquan (Michael) Zhang, http://orcid.org/0000-0002-7554-5916Xiaona Zheng (2017) Bidding for Multiple Keywords in Sponsored Search Advertising: Keyword Categories and Match Types. Information Systems Research

Published online in Articles in Advance 07 Aug 2017

https://doi.org/10.1287/isre.2017.0724

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/TN6HB62N/fulltext/images/575725babc3e148163db6b0bfb8edbe976abfdd9cfb9b65a1c5a3a621fa47e96.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Bidding for Multiple Keywords in Sponsored Search Advertising: Keyword Categories and Match Types

Xiaomeng Du,<sup>a</sup> Meng Su,<sup>a,</sup> <sup>b</sup> Xiaoquan (Michael) Zhang,<sup>c</sup> Xiaona Zheng<sup>b</sup>

<sup>a</sup> Baifendian Technology, Inc., 100101 Beĳing, China; <sup>b</sup> Guanghua School of Management, Peking University, 100871 Beĳing, China; <sup>c</sup> Decision Sciences and Managerial Economics, Chinese University of Hong Kong, Shatin, Hong Kong

Contact: fancia814@pku.edu.cn (XD); sumeng@gsm.pku.edu.cn (MS); zhangxiaoquan@gmail.com (X(M)Z); xzheng@gsm.pku.edu.cn, http://orcid.org/0000-0002-7554-5916 (XZ)

Received: July 1, 2013 Revised: April 30, 2014; January 5, 2016; December 30, 2016 Accepted: February 1, 2017 Published Online in Articles in Advance: August 7, 2017

https://doi.org/10.1287/isre.2017.0724

Copyright: © 2017 INFORMS

Abstract. Although keyword auctions are often studied in the context of a single keyword in the literature, firms generally have to participate in multiple keyword auctions at the same time. Advertisers purchase a variety of keywords that can be categorized as genericrelevant, focal-brand, and competing-brand keywords. At the same time, firms also have to choose how the keywords can be matched to search queries: exact, phrase, or broad. This study empirically examines how keyword categories and match types influence the performance of advertising campaigns. We build a hierarchical Bayesian model to address the endogeneity problem contained in the simultaneous equations of the click-through rate, the conversion rate, cost per click, and rank, and we use the Markov Chain Monte Carlo method to identify the parameters. Our results suggest that it is important to diferentiate among the various bidding strategies for various keyword categories and match types. We also report results related to financial performance such as number of sales, profit, and return on investment for diferent keywords. These findings shed light on the practice of sponsored search advertising by ofering insights into how to manage ad campaigns when advertisers have to bid on multiple keywords.

History: Sanjeev Dewan, Senior Editor; De Liu, Associate Editor.

Funding: This research was supported in part by the National Natural Science Foundation of China [Grants 71332006 and 71272039] and the Hong Kong Research Grants Council [Projects GRF 16504614, 694213, and CityU 11504815].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0724.

Keywords: hierarchical Bayesian model • bidding strategy • competing-brand keywords • generic keywords • focal-brand keywords • keyword auctions • purchase funnel • sponsored search advertising

## 1. Introduction

Search engine marketing plays an important role in generating sales for otherwise unknown online retailers. eMarketer estimates that paid search is the leading e-advertising model for marketers, with companies expected to double their spending on paid searches to reach a market of more than \$40 billion in 2019.<sup>1</sup> In sponsored search advertising, marketers that advertise on a search engine submit a list of keywords, along with a specific bidding price for each keyword and a total budget for a given time period. The search engine then computes the rank on the results page for each keyword based on advertisers’ bidding prices, as well as quality indexes representing the keyword’s performance.<sup>2</sup> When a visitor searches for a term on the search engine, the advertisers’ ads appear as sponsored links next to the organic search results. When the visitor clicks on an advertising link, the advertiser then pays the search engine, according to a payment mechanism known as Cost/Pay Per Click (CPC or PPC).

After about a decade of research, advertisers’ bidding strategies for a single keyword are relatively well studied (e.g., see Edelman et al. 2007 for a static model and Zhang and Feng 2011 for a dynamic model with empirical results). In theoretical works of auctions, a single keyword is often modeled as a market with multiple advertisers submitting competing bids (e.g., Katona and Sarvary 2009, Liu et al. 2010). In practice, however, advertisers have to bid on a long list of keywords to obtain the highest exposure and maximize their profit. The market in the eyes of the advertisers is more like multiple parallel markets each with many competitors who may or may not overlap across markets. This feature of multiple parallel markets is seldom observed and studied in traditional markets in economics. In this paper, we seek to contribute to this small but growing literature of multikeyword position auctions. We focus on advertisers’ choice of (1) diferent keyword categories and (2) match types to examine possible diferences in their performance metrics.

In this study, we argue that when creating the keyword list, an advertiser generally limits its attention to three categories of keywords: generic relevant (a keyword that is related to the advertiser’s product or service), focal brand (a keyword that contains the name of the advertiser, i.e., the focal firm), and competing brand (a keyword that contains a competitor’s trademark).<sup>3</sup> Note that the “generic-relevant keywords” (generic keywords for short hereafter) studied in this paper are diferent from the “generic or organic search results” referred to in the literature. A generic search result refers to a search engine result returned from some algorithm not influenced by advertisers’ payments (Yang and Ghose 2010, Rutz and Bucklin 2011, Blake et al. 2015). A generic keyword in our setting refers to a keyword that is related to the advertised product or service but not associated with a brand name. The three keyword categories reflect three diferent types of consumers the focal advertiser would like to capture. Users who search for generic keywords are most likely those still doing research and do not have a clear idea about the seller (Malthouse et al. 2013). Those who search for focal-brand keywords are probably users who would like to learn more about the focal retailer and assess its quality. Of course, an advertiser also wants to submit bids for competing-brand keywords, so that these users will learn about the alternative seller. Since the three categories appeal to three diferent groups of users, how the three strategies perform is an important empirical question.

The literature ofers very limited findings for keyword categories. Prior literature on multikeyword bidding strategies has examined whether a keyword is advertiser specific (Rutz and Bucklin 2011) or whether it contains brand names (Ghose and Yang 2009). Ghose and Yang (2009) study brand and retailer keywords, but do not discuss the three keyword categories of our study. Scott (2013) calls competing-brand keyword bidding “customer hĳacking” and reports recent developments in understanding its legal implications. Chiou and Tucker (2012) examine the outcome of one such customer-hĳacking event; they find that allowing thirdparty sellers to use trademarked brands in their advertising leads to a fourfold increase in trademark owners’ organic clicks. Rutz and Bucklin (2011) use a hierarchical Bayesian model to establish that brand-based search is often a result of generic search, because consumers may need to learn about product features before choosing from whom to buy. Using field experiments, Blake et al. (2015) demonstrate that bidding on focal-brand keywords often has no benefits at all. None of the previous empirical papers distinguish between focal- and competing-brand keywords (Ghose and Yang 2009, Rutz and Bucklin 2011, Chiou and Tucker 2012, Blake et al. 2015). Our paper is the first empirical work in the literature to systematically study generic, focal-brand, and competing-brand keywords.

In a theoretical paper, Sayedi et al. (2014) examine the competitive poaching behavior of bidding on competing-brand keywords. They find that smallerbudget advertisers tend to poach more, driving largerbudget advertisers to allocate more to traditional advertising channels. Desai et al. (2014) establish, in a competitive equilibrium, the conditions under which it is good to buy competing-brand keywords. Both firms may be worse of by engaging in such poaching behavior. These two theoretical works distinguish own versus competing brand in their respective models, but thus far there is no detailed empirical examination in the literature. Clearly, the performance implications of participating in diferent keyword categories are far from established.

In addition to choosing a keyword category, advertisers also have to make another important choice: which keyword match type to use. Match type controls when the ads will be shown to search engine users. An exact-matched keyword allows the advertiser’s webpage to appear in response to searches of the exact term, a phrase-matched keyword triggers the ads when searches are a phrase or close variations of that phrase, and a broad-matched keyword is triggered when a user searches for that phrase, similar phrases, singular or plural forms, misspellings, synonyms, stemmings (such as floor and flooring), related searches, and other relevant variations. The industry identifies keyword match type as an important but unexplored variable (Enge et al. 2015, Karwal 2015, Kershen 2016). ClickEquations (2008, p. ii) writes that “match type is the paid search option which has perhaps the highest impact, is the least understood, and is most often under-utilized.” Only two prior academic works address this topic. In their commentary article, Dhar and Ghose (2010) discuss the importance of studying it, and Amaldoss et al. (2015) develop a theoretical framework to show that search engines can tweak the accuracy of their broad-match results to maximize profits. So far, however, there are no empirical works on this issue in the literature.

In this paper, we build a unified framework on the efects of diferent keyword categories and match types and establish both first-order efects and interaction efects between the two keyword characteristics. To our knowledge, no prior work has studied keyword categories and keyword match types in a unified framework (see Table 1 for a summary of the literature).<sup>4</sup> This paper contributes to the growing literature of multikeyword bidding strategies by diferentiating various keywords into three categories, examining the performance outcomes of choosing these diferent keyword categories, and studying how keyword match types change this relationship.<sup>5</sup>

Wefind that, relative to generic keywords, focal-brand keywords are associated with higher click-through rates (CTRs) and higher conversion rates (CRs), while competing-brand keywords are associated with lower CTRs but higher CRs. Both generic and focal-brand keywords can achieve higher CTRs and CRs in more promient positions, while competing-brand keywords achieve higher CTRs in less promient positions. When considering the costs of advertising, firms tend to incur higher CPCs for generic keywords than for branded ones. In general, shorter keywords are associated with better ad performance in terms of CTRs and CRs. Relative to generic keywords, focal-brand (competing-brand) keywords are usually placed in higher (lower) positions.

Table 1. Summary of the Literature

<table><tr><td>Paper</td><td>Method</td><td>Focus/Main result</td><td>Multi-keyword</td><td>Keyword category</td><td>Keyword match type</td></tr><tr><td>Agarwal et al. (2011)</td><td>Empirical/HB</td><td>CTR&#x27;s and CR&#x27;s reaction to position</td><td>Y</td><td></td><td></td></tr><tr><td>Agarwal et al. (2012)</td><td>Empirical/HB</td><td>How organic results influence performance of sponsored results</td><td>Y</td><td></td><td></td></tr><tr><td>Amaldoss et al. (2015)</td><td>Theoretical</td><td>Search engines should set the right broad match accuracy</td><td></td><td></td><td>Y</td></tr><tr><td>Animesh et al. (2011)</td><td>Theoretical/empirical</td><td>Firm&#x27;s positioning strategy and CTR</td><td></td><td></td><td></td></tr><tr><td>Blake et al. (2015)</td><td>Empirical/experimental</td><td>Existence of organic results makes paid results less profitable</td><td></td><td>Y</td><td></td></tr><tr><td>Blankenbaker and Mishra (2009)</td><td>Survey</td><td>Consumer exploration in search</td><td></td><td></td><td></td></tr><tr><td>Chen and He (2011)</td><td>Theoretical</td><td>A market game of consumer search</td><td></td><td></td><td></td></tr><tr><td>Chiou and Tucker (2012)</td><td>Empirical</td><td>Use of trademarks by third-party sellers</td><td></td><td>Y</td><td></td></tr><tr><td>Desai et al. (2014)</td><td>Theoretical</td><td>When buying a competing-brand keyword is profitable</td><td>Y</td><td>Y</td><td></td></tr><tr><td>Dou et al. (2010)</td><td>Experimental</td><td>Brand recognition and positioning</td><td></td><td></td><td></td></tr><tr><td>Edelman et al. (2007)</td><td>Theoretical</td><td>Equilibrium outcome of generalized second price auction</td><td></td><td></td><td></td></tr><tr><td>Ghose and Yang (2009)</td><td>Empirical/HB</td><td>Keyword performance metrics</td><td>Y</td><td></td><td></td></tr><tr><td>Jerath et al. (2011)</td><td>Theoretical/empirical</td><td>Higher quality firm may bid for a lower position</td><td></td><td></td><td></td></tr><tr><td>Katona and Sarvary (2009)</td><td>Theoretical</td><td>Organic/paid search interaction and quality scores</td><td></td><td></td><td></td></tr><tr><td>Liu et al. (2010)</td><td>Theoretical</td><td>Keyword auction design with prior knowledge of advertiser quality</td><td></td><td></td><td></td></tr><tr><td>Lu et al. (2015)</td><td>Theoretical</td><td>Budget constraints</td><td></td><td></td><td></td></tr><tr><td>Rutz and Bucklin (2011)</td><td>Empirical/HB</td><td>Generic keywords&#x27; spillover effect to branded search</td><td>Y</td><td>Y</td><td></td></tr><tr><td>Sayedi et al. (2014)</td><td>Theoretical</td><td>Competitive poaching in submitting competing-brand keywords</td><td></td><td>Y</td><td></td></tr><tr><td>Scott (2013)</td><td>Commentary</td><td>Legal considerations of submitting competing-brand keywords</td><td></td><td>Y</td><td></td></tr><tr><td>Shin (2015)</td><td>Theoretical</td><td>Budget constraints</td><td></td><td></td><td></td></tr><tr><td>Weber and Zheng (2007)</td><td>Theoretical</td><td>Equilibrium bidding strategy for one keyword</td><td></td><td></td><td></td></tr><tr><td>Yang and Ghose (2010)</td><td>Empirical/HB</td><td>Relationship between organic and paid search</td><td>Y</td><td></td><td></td></tr><tr><td>Zhang and Feng (2011)</td><td>Theoretical</td><td>Equilibrium bidding strategy for one keyword</td><td></td><td></td><td></td></tr><tr><td>This study</td><td>Empirical/HB</td><td></td><td>Y</td><td>Y</td><td>Y</td></tr></table>

Notes. CR, conversion rate; CTR, click-through rate; HB, hierarchical Bayesian.

We show that keyword match types are also important and that their efects difer for the three keyword categories. Exact match is associated with the highest CTRs and CRs for generic and focal-brand keywords. For competing-brand keywords, broad match and phrase match tend to increase the CTR, while broad match tends to depress but phrase match tends to raise the CR. Exact match is associated with higher CPC than broad and phrase matches. When phrase match is chosen as the keyword match type, branded keywords are associated with higher CPCs than generic keywords. Finally, exact-matched generic and competingbrand keywords tend to have higher ranks, probably because of the extent of competitiveness and the degree of relevance, respectively. By contrast, exactmatched focal-brand keywords tend to be placed in higher positions.

This research has several theoretical and practical contributions. First, while the majority of studies on keyword auctions focus on bids, we examine some other equally interesting nonmonetary decision variables related to keyword selection. Second, the subjects of our study, keyword categories and match types, are features that are unique to multikeyword position auctions. It would be impossible to examine these issues in single-keyword position auctions. Modeling position auctions in a single-keyword market is often suficient to generate important insights. To examine keyword selection, however, we need to use a multikeyword perspective. This study demonstrates that in the multikeyword position auction setting, there exist many complex relations between seemingly simple decision variables. Both academia and the industry consider keyword match type as the paid search option that may have the highest impact but is the least understood. This study explores the efect of keyword match types (in particular, their interaction with the three keyword categories) on sponsored search advertising strategies and ofers insights into how the various limits on keywords perform diferently for consumers using diferent search terms. Finally, while most prior works treat keyword categories and match types as isolated issues (as can be seen in Table 1), our research shows that their efects on keyword performance depend on each other. Although we cannot claim that these relations will carry over to other keywords or other advertisers, or remain the same on diferent platforms (Zhang and Zhu 2011), our unified framework ofers a way for practitioners to examine nuances that are specific to their own settings.

The rest of the paper is organized as follows. We first describe the data-collection process and conduct a descriptive analysis of the data. Next, we briefly present our model and methodology. We then report the empirical results and relate them to the existing literature. We conclude the study with a discussion on its implications and limitations.

## 2. Background and Data

Our data contain daily information on sponsored search advertising from a major Chinese online B2C retailer that advertises on Google. Its product categories include apparel, shoes, handbags, jewelry, beauty products, and accessories. The data set consists of all keyword advertisements by the company from August through October 2011. Specifically, it includes 142,878 observations from a total of 4,163 unique keywords. We summarize the daily information of each keyword from three perspectives: keyword characteristics, keywordlevel performance, and financial performance.

## 2.1. Keyword Characteristics

Keyword Categories: Generic, Focal Brand, Competing Brand. When advertisers choose keywords, they tend to focus on three categories that can generate clicks. First, generic-relevant keywords include those about the general product categories ofered on the firm’s website (e.g., T-shirts, purses, etc.). Focal-brand keywords are defined as those containing information regarding this company’s brand names. Competingbrand keywords, by contrast, contain brand terms of the company’s major competitors in online retailing. For example, competing-brand keywords can be about general online retailers, such as VIPShop (China’s leading online discount retailer that went public on the NYSE in March 2012) or specialized retailers, such as Sasa (an online cosmetic seller) and UNIQLO (a casual-wear seller). The company labeled each keyword as generic relevant, focal brand, or competing brand when it designed the advertising campaign. We use two dummy variables (Focal and Competing) to indicate the keyword category, with Generic as the baseline. Out of the 4,163 keywords, 26.4% are competing-brand keywords, 70.1% are generic keywords, and 3.5% are focal-brand keywords.

Keyword Match Type: Exact, Broad, Phrase. An exact match matches a keyword exactly. For example, with an exact match, the keyword “Cartier necklace” would match neither “Cartier” nor “necklace.” “Gold Cartier necklace” also would not be matched. Exact match is the most restrictive form of keyword match type, and the advertiser has total control over what can be matched. The disadvantage of using this match type, however, is that the advertiser would have to anticipate all of the possible keywords that a consumer might be using to search for information. To match all possibilities of “gold Cartier necklace,” an advertiser would have to input all seven permutations of the three words. The cost of monitoring and changing bids for each exact-matched keyword would quickly become prohibitively expensive when the number of keywords is large.

Similar to an exact match, with a phrase match, the search query term has to be exactly matched, but it can be part of a larger search query. So Cartier necklace would be matched to such queries as gold Cartier necklace or “Cartier necklace price.” This frees advertisers from having to select too many possible keywords, but it has the disadvantage that some matches cannot be fully controlled. For example, Cartier necklace could be matched to “I hate Cartier necklace.” In this case, if consumers click on the ad, they are not likely to buy anything, thereby wasting the fee paid for the click. Even worse, if they do not click on the ad, it will drag down the quality score of the ad, making it costlier to compete in the future.<sup>6</sup>

Broad match is the most flexible of the three. A broad match is triggered when a user searches for that specific phrase, similar phrases, singular or plural forms, misspellings, synonyms, stemmings (such as floor and flooring), related searches, and other relevant variations. For example, depending on the algorithm, Cartier necklace could be broad-matched to Catier necklace,” “Cartier necklacing,” “necklace from Cartier,” “Cartier necklaces,” and “Cartier golden necklace,” etc. Broad match allows very flexible matching of keywords, but it clearly has the disadvantage that many unrelated keywords can be matched. As a result, the advertisers may either waste their advertising budget or get penalized on their quality score for poor matches. We use two dummy variables (Broad and Phrase) to indicate the three keyword match types (broad, phrase, or exact), with Exact as the baseline. Of all of the keywords, 56.2% are broad matched, 40.7% are phrase matched, and 3.2% are exact matched.

Keyword Length. We use a variable (Length) to indicate the number of characters contained in the keyword.

## 2.2. Keyword-Level Performance

To assess keyword-level performance, we utilize daily information on each keyword’s number of impressions, number of clicks, CPC, and average rank. From the raw data, we calculate the CTR (number of clicks/ number of impressions) and the CR (number of orders/number of clicks) for each keyword. The average number of daily impressions is 26.34 for generic keywords, 22.22 for focal-brand keywords, and 33.03 for competing brand keywords. The average CTR and CR are 0.04 and 0.01, respectively, for generic keywords, 0.37 and 0.05 for focal-brand keywords, and 0.02 and 0.002 for competing-brand keywords. The average CPC is 0.58, 0.41, and 0.40 Chinese Yuan, and the average rank (a lower rank corresponds to a higher position on the search results page) is 3.21, 1.16, and 3.47 for generic, focal-brand, and competing-brand keywords, respectively. A descriptive analysis of keyword-level performance variables reveals significant diferences among the three types of keywords.

## 2.3. Keyword Financial Performance

Order. The variable Order is the daily total number of orders for each keyword.

Total Revenue and Total Expenses. We also examine daily total revenue (Total Revenue), daily total expenses (Total Expenses <sup></sup> number of clicks <sup>×</sup> CPC), and daily total profit (Total Revenue <sup>−</sup> Total Expenses) for each keyword.

Table 2 displays the summary statistics.

## 3. The Modeling Approach

In Table 1’s summary, it is clear that all studies of multikeyword position auctions have adopted a hierarchical Bayesian framework (Agarwal et al. 2011, 2012; Ghose and Yang 2009, Rutz and Trusov 2011). We also adopt this framework for its power of solving (1) the simultaneity problem in variables and (2) the sparsity of the data set. There are subtle diferences between the specific estimation procedures used in our paper and those used in prior works; we provide the details in the online appendix.

The model treats CTR as the probability that an online user would click the advertising link after she enters a search term and the search engine returns a results page containing the sponsored search advertising links. Prior literature suggests that CTR is partially determined by the keyword’s rank and length (Ghose and Yang 2009). For the purpose of this study, we incorporate the keyword category dummy variables, Focal and Competing, the keyword match type variables, Broad and Phrase, as well as their interaction terms with the other variables.

Specifically, we have

$$
C T R _ {i} = \frac {e ^ {V _ {i}}}{1 + e ^ {V _ {i}}},\tag{1}
$$

where $V _ { i } = \alpha _ { 1 } + \alpha _ { 2 } R a n k _ { i } + \alpha _ { 3 } L e n g t h _ { i } + \alpha _ { 4 } C o m p e t i n g _ { i } +$ $\alpha _ { 5 } F o c a l _ { i } + \alpha _ { 6 } B r o a d _ { i } + \alpha _ { 7 } P h r a s e _ { i } + \tilde { \alpha _ { 8 } } \dot { R a n } { k _ { i } } \times C o m p e t i n \dot { g _ { i } } +$ $\alpha _ { 9 } L e n g t h _ { i } \ \times \ C o m p e t i n g _ { i } \ + \ \alpha _ { 1 0 } B r o a d _ { i } \ \times \ C o m p e t i n g _ { i } \ +$ $\begin{array} { r } { \alpha _ { 1 1 } { { P h r a s e } _ { i } } \times C o m p e t i n { { g } _ { i } } + \alpha _ { 1 2 } { { R a n } { { k } _ { i } } } \times F o c a l _ { i } + \alpha _ { 1 3 } L e n g t h _ { i } \times } \end{array}$ $F o c a l _ { i } + \alpha _ { 1 4 } B r o a d _ { i } \times F o c a l _ { i } + \alpha _ { 1 5 } P h r a s e _ { i } \times F o c a l _ { i } + \varepsilon _ { i } .$

We can similarly model the conversion rate, CR, as a probability that is determined by the covariates

$$
C R _ {i} = \frac {e ^ {U _ {i}}}{1 + e ^ {U _ {i}}},\tag{2}
$$

where $U _ { i } = \zeta _ { 1 } + \zeta _ { 2 } R a n k _ { i } + \zeta _ { 3 } L e n g t h _ { i } + \zeta _ { 4 } C o m p e t i n g _ { i } \ :$ + ζ<sub>5</sub>Focal<sub>i</sub> <sup>+</sup> ζ<sub>6</sub>Broad<sub>i</sub> <sup>+</sup> ζ<sub>7</sub>Phrase <sup>+</sup> ζ<sub>8</sub>Rank<sub>i</sub> <sup>×</sup> Competing <sup>+</sup> ζ Length <sup>×</sup> Competing <sup>+</sup> ζ Broad <sup>×</sup> Competing <sup>+</sup> $\zeta _ { 1 1 } { \cal P } { \it h r a s e } _ { i } \times { \it C o m p e t i n g } _ { i } + \zeta _ { 1 2 } { \it R a n k } _ { i } \times { \it F o c a l } _ { i } + \zeta _ { 1 3 } { \it L e n g t h } _ { i } \times$ $F o c a l _ { i } + \zeta _ { 1 4 } B r o a d _ { i } \times F o c a l _ { i } + \zeta _ { 1 5 } P h r a s e _ { i } \times F o c a l _ { i } + \sigma _ { i }$

In deciding the CPC of a keyword, advertising firms consider the past performance of a certain keyword, which could be judged by its past rank (Yang and Ghose 2010). We also include keyword characteristic variables that should be influencing the cost concerns

$$
\begin{array}{l} \log (C P C _ {i}) \\ = \gamma_ {1} + \gamma_ {2} L a g \_ R a n k _ {i} + \gamma_ {3} L e n g t h _ {i} + \gamma_ {4} C o m p e t i n g _ {i} \\ \quad + \gamma_ {5} F o c a l _ {i} + \gamma_ {6} B r o a d _ {i} + \gamma_ {7} P h r a s e _ {i} \\ \quad + \gamma_ {8} L a g \_ R a n k _ {i} \times C o m p e t i n g _ {i} + \gamma_ {9} L e n g t h _ {i} \times C o m p e t i n g _ {i} \\ \quad + \gamma_ {1 0} B r o a d _ {i} \times C o m p e t i n g _ {i} + \gamma_ {1 1} P h r a s e _ {i} \times C o m p e t i n g _ {i} \\ \quad + \gamma_ {1 2} L a g \_ R a n k _ {i} \times F o c a l _ {i} + \gamma_ {1 3} L e n g t h _ {i} \times F o c a l _ {i} \\ \quad + \gamma_ {1 4} B r o a d _ {i} \times F o c a l _ {i} + \gamma_ {1 5} P h r a s e _ {i} \times F o c a l _ {i} + \omega_ {i}. \end{array} \tag {3}
$$

Finally, we model rank, which is determined by the search engine’s algorithms. Search engines normally consider CPC (or bidding price) as the main determinant of rank, so firms ofering higher bids usually get a better rank (higher position). In addition, search engines take quality into consideration and infer it through the past CTR of the keyword (Agarwal et al. 2011, Ghose and Yang 2009, Varian 2007). Thus, we incorporate CPC and lagged CTR in the model for rank. As before, we include the variables for keywordlevel characteristics

Table 2. Summary Statistics and Correlations

<table><tr><td></td><td>Generic</td><td>Focal</td><td>Competing</td><td>Length</td><td>Broad</td><td>Phrase</td><td>Exact</td><td>CTR</td><td>CPC</td><td>CR</td><td>Rank</td></tr><tr><td>Generic</td><td>0.701(0.458)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Focal</td><td>-0.293(0.001)</td><td>0.035(0.184)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Competing</td><td>-0.917(0.001)</td><td>-0.114(0.001)</td><td>0.264(0.441)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Length</td><td>0.181(0.001)</td><td>-0.059(NS)</td><td>-0.164(0.001)</td><td>9.757(3.339)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Broad</td><td>-0.074(NS)</td><td>-0.166(0.001)</td><td>0.147(0.001)</td><td>0.179(0.001)</td><td>0.562(0.496)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Phrase</td><td>0.083(0.01)</td><td>0.141(0.001)</td><td>-0.145(0.001)</td><td>-0.128(0.001)</td><td>-0.937(0.001)</td><td>0.407(0.491)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Exact</td><td>-0.021(NS)</td><td>0.073(NS)</td><td>-0.009(NS)</td><td>-0.149(0.001)</td><td>-0.205(0.001)</td><td>-0.150(0.001)</td><td>0.032(0.175)</td><td></td><td></td><td></td><td></td></tr><tr><td>CTR</td><td>-0.042(NS)</td><td>0.393(0.001)</td><td>-0.120(0.001)</td><td>-0.028(NS)</td><td>-0.118(0.001)</td><td>0.096(0.005)</td><td>0.065(NS)</td><td>0.048(0.154)</td><td></td><td></td><td></td></tr><tr><td>CPC</td><td>0.071(NS)</td><td>-0.019(NS)</td><td>-0.066(NS)</td><td>-0.064(NS)</td><td>0.027(NS)</td><td>-0.052(NS)</td><td>0.070(NS)</td><td>0.342(0.001)</td><td>0.523(1.146)</td><td></td><td></td></tr><tr><td>CR</td><td>-0.056(NS)</td><td>0.183(0.001)</td><td>-0.018(NS)</td><td>-0.033(NS)</td><td>-0.046(NS)</td><td>0.335(0.001)</td><td>0.037(NS)</td><td>0.162(0.001)</td><td>0.070(NS)</td><td>0.004(0.049)</td><td></td></tr><tr><td>Rank</td><td>-0.002(NS)</td><td>-0.198(0.001)</td><td>0.084(0.01)</td><td>0.060(NS)</td><td>0.048(NS)</td><td>-0.047(NS)</td><td>-0.005(NS)</td><td>-0.234(0.001)</td><td>-0.141(0.001)</td><td>-0.055(NS)</td><td>3.207(1.977)</td></tr></table>

Notes. Means and (standard deviations) are shown in the diagonal cells. Bolded numbers show significant correlations at the p < 0.001 level. NS, not significant. Number of Observations: 142,878.

$$
\begin{array}{l} \log (R a n k _ {i}) \\ = \varphi_ {1} + \varphi_ {2} C P C _ {i} + \varphi_ {3} L a g \_ C T R _ {i} + \varphi_ {4} L e n g t h _ {i} \\ \quad + \varphi_ {5} C o m p e t i n g _ {i} + \varphi_ {6} F o c a l _ {i} + \varphi_ {7} B r o a d _ {i} + \varphi_ {8} P h r a s e _ {i} \\ \quad + \varphi_ {9} C P C _ {i} \times C o m p e t i n g _ {i} + \varphi_ {1 0} L a g \_ C T R _ {i} \times C o m p e t i n g _ {i} \\ \quad + \varphi_ {1 1} L e n g t h _ {i} \times C o m p e t i n g _ {i} + \varphi_ {1 2} B r o a d _ {i} \times C o m p e t i n g _ {i} \\ \quad + \varphi_ {1 3} P h r a s e _ {i} \times C o m p e t i n g _ {i} + \varphi_ {1 4} C P C _ {i} \times F o c a l _ {i} \\ \quad + \varphi_ {1 5} L a g \_ C T R _ {i} \times F o c a l _ {i} + \varphi_ {1 6} L e n g t h _ {i} \times F o c a l _ {i} \\ \quad + \varphi_ {1 7} B r o a d _ {i} \times F o c a l _ {i} + \varphi_ {1 8} P h r a s e _ {i} \times F o c a l _ {i} + v _ {i}. \end{array} \tag {4}
$$

We assume the error terms are distributed as multivariate standard normal. The variance-covariance matrix between all error terms in Equations (1)–(4) can be written as

$$
\left[ \begin{array}{c} \varepsilon \\ \sigma \\ \omega \\ v \end{array} \right] \sim \text {MVN} \left(\left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ 0 \end{array} \right], \left[ \begin{array}{c c c c} v _ {\varepsilon} ^ {2} & & & \\ v _ {\sigma \varepsilon} & v _ {\sigma} ^ {2} & & \\ v _ {\omega \varepsilon} & v _ {\omega \sigma} & v _ {\omega} ^ {2} & \\ v _ {v \varepsilon} & v _ {v \sigma} & v _ {v \omega} & v _ {v} ^ {2} \end{array} \right]\right).
$$

We closely follow Ghose and Yang’s (2009) approach. This hierarchical Bayesian model is widely used by studies of multikeyword position auctions (e.g., Agarwal et al. 2011, 2012; Yang and Ghose 2010; Rutz and Bucklin 2011).

When estimating the parameters, we use the Markov Chain Monte Carlo (MCMC) method with a Gibbs sampler (Dellarocas et al. 2007). We present the detailed estimation procedure in Online Appendix A.

## 4. Empirical Results and Discussion

Table 3 provides the estimation results for CTR, CR, CPC, and rank. In this section, we focus our discussion on the diferences in the relationships between keyword attributes (e.g., rank, length, and keyword match type) and keyword performance (e.g., CTR/CR, CPC, and rank) for diferent keyword categories.

## 4.1. Click-Through and Conversion Rates

We examine the first-order efects of Focal and Competing first. Focal is positive and significant for both CTR and CR. This means that relative to generic keywords, bidding on focal-brand keywords yields better keyword performance. Consumers are relatively more likely to click on ads targeting focal-brand keywords than those targeting generic keywords, and they are possibly more inclined to make a purchase when they do.

Our results also show that CTRs are lower for competing-brand keywords than for generic keywords. This suggests that consumers indeed have strong preferences when they search for branded keywords, and thus the strategy of poaching may not be efective in attracting visitors. Competing-brand keywords, however, have a higher conversion rate than generic keywords. This suggests that once consumers click on an ad of a competing-brand keyword, they are seriously interested in buying the product. This result supports Moe’s (2003) view that goal-directed consumers exhibiting search/deliberation behavior may switch to the focal firm if exposed to the ads. Therefore, the poaching strategy is more likely to work for this group of consumers (Zhu and Zhang 2010).

Table 3. Bayesian Estimation Results of CTR, CR, CPC, and Rank

<table><tr><td>Variables</td><td>CTR</td><td>CR</td><td>CPC</td><td>Rank</td></tr><tr><td>Con</td><td>0.093***</td><td>0.005***</td><td>0.729***</td><td>0.961***</td></tr><tr><td>Focal</td><td>0.528***</td><td>0.129***</td><td>-0.488***</td><td>-1.341***</td></tr><tr><td>Competing</td><td>-0.100***</td><td>0.004***</td><td>-0.182***</td><td>0.220***</td></tr><tr><td>Rank</td><td>-0.001***</td><td>0.00007</td><td></td><td></td></tr><tr><td>Rank × Focal</td><td>-0.048***</td><td>-0.008***</td><td></td><td></td></tr><tr><td>Rank × Competing</td><td>0.007***</td><td>-0.00004</td><td></td><td></td></tr><tr><td>Lag_Rank</td><td></td><td></td><td>-0.017***</td><td></td></tr><tr><td>Lag_Rank × Focal</td><td></td><td></td><td>0.041***</td><td></td></tr><tr><td>Lag_Rank × Competing</td><td></td><td></td><td>0.021***</td><td></td></tr><tr><td>Length</td><td>-0.001***</td><td>-0.0002***</td><td>-0.012***</td><td>0.007***</td></tr><tr><td>Length × Focal</td><td>0.001</td><td>-0.001***</td><td>0.029***</td><td>-0.004</td></tr><tr><td>Length × Competing</td><td>-0.001***</td><td>-0.0001</td><td>-0.0014</td><td>0.013***</td></tr><tr><td>Broad</td><td>-0.049***</td><td>-0.002***</td><td>-0.181***</td><td>-0.050***</td></tr><tr><td>Phrase</td><td>-0.045***</td><td>-0.002***</td><td>-0.315***</td><td>-0.030***</td></tr><tr><td>Broad × Focal</td><td>-0.359***</td><td>-0.095***</td><td>-0.0375</td><td>0.656***</td></tr><tr><td>Phrase × Focal</td><td>-0.116***</td><td>-0.063***</td><td>0.183***</td><td>0.192***</td></tr><tr><td>Broad × Competing</td><td>0.056***</td><td>-0.003***</td><td>-0.099***</td><td>-0.161***</td></tr><tr><td>Phrase × Competing</td><td>0.065***</td><td>0.0002***</td><td>0.184***</td><td>-0.302***</td></tr><tr><td>CPC</td><td></td><td></td><td></td><td>-0.020***</td></tr><tr><td>CPC × Focal</td><td></td><td></td><td></td><td>0.023</td></tr><tr><td>CPC × Competing</td><td></td><td></td><td></td><td>0.013***</td></tr><tr><td>Lag_CTR</td><td></td><td></td><td></td><td>-0.677***</td></tr><tr><td>Lag_CTR × Focal</td><td></td><td></td><td></td><td>1.598***</td></tr><tr><td>Lag_CTR × Competing</td><td></td><td></td><td></td><td>0.263***</td></tr></table>

Result 1. Relative to generic keywords, focal-brand keywords are associated with higher CTR and CR. Relative to generic keywords, competing-brand keywords are associated with lower CTR but higher CR.

The first-order efect of rank on CTR is negative. This result resonates with findings from prior research suggesting that consumers consider higher-positioned ads more persuasive (Brunel and Nelson 2003) and that they tend to browse through ads sequentially in the order displayed, rendering an advantage to advertisers listed at the top positions over those appearing lower (Animesh et al. 2011). The conversion rate, however, is not particularly determined by rank: occupying a higher rank does not guarantee that consumers who click through the ad will make a purchase.

For focal-brand keywords, relative to generic keywords, taking a higher position (low Rank) is more efective in increasing both CTR and CR. Although it is not surprising that having a higher position is associated with higher CTR, it is interesting that conversion rate is also increased in more prominent positions. This result complements previous research by highlighting the diferential efects of ranking on diferent keyword categories. Ghose and Yang (2009) also find that ads with lower ranks (higher positions) are associated with higher conversion rates. One possible explanation for this phenomenon is that consumers may associate the top positions with higher quality (Brooks 2004, Dou et al. 2010). Our findings suggest that, for consumers searching for focal-brand terms, those clicking on focal ads in top positions are likely to exhibit direct-buying behavior (Moe 2003) because of the strategic alignment between ad and keyword, and their interest in the focal brand.<sup>7</sup> For those clicking on ads in lower slots, the chance of catching them would be lower, as they may be captured by similar ads. Consistent with prior research (Chen and He 2011), these results together suggest that an advertiser should secure more prominent positions for its own branded keywords.

Relative to generic keywords, competing-brand keywords are associated with a decrease in the negative relationship between rank and CTR. Indeed, the relationship between rank and CTR reverses to become positive for competing-brand keywords. In other words, when consumers searching for a competing brand reject other options in top slots and scroll down the screen, exhibiting search/deliberation behavior, they are more likely to consider other brands (e.g., the focal firm’s listing) as an alternative.

Ranking does not afect the conversion rate of competing-brand keywords, relative to generic keywords. These results ofer a nuanced extension to the literature by demonstrating the importance of examining focaland competing-brand keywords separately.

Result 2. Relative to generic keywords, focal-brand keywords can achieve higher CTR and CR in higher positions. Relative to generic keywords, competing-brand keywords achieve higher CTR in lower positions.

We next turn to examine keyword match type, particularly its interaction with the diferent keyword categories.

Relative to an exact keyword match, the baseline efects of both broad and phrase keyword matches are negative on CTR and CR. This indicates that keywords more relevant to the searches are more efective in generating consumers’ interest to visit the advertisement link. Although broad and phrase keyword matches can capture more search terms, a well-designed exact match can increase both the exposure (CTR) and the purchase behavior (CR) significantly.

The interaction terms between focal-brand keywords and broad/phrase keyword match types suggest that the above efect is reinforced. An exact match for focal-brand keywords produces the highest advertising performance outcome. A possible explanation for this result is that focal-brand keywords on an exact match are more relevant (than those on phrase or broad matches) to queries initiated by goal-directed consumers who are in the later stages of the purchase funnel. When these consumers are searching for the focal brand, an exact match can generate a significantly higher conversion rate.

Competing-brand keywords, when used with broad or phrase keyword matches, generate higher CTRs than generic keywords. Relative to generic keywords, a broad match of competing-brand keywords is associated with lower CRs, but a phrase match of competingbrand keywords yields higher CRs. Intuitively, the mechanism behind these results can be the following: A user who is still in the exploration stage of a seller (e.g., Argus Car Hire) might type in a query, “is Argus Car Hire cheap?” In this case, if the focal firm (EconomyBookings.com) is listed on the results page of “Argus Car Hire” through a phrase match, then the consumer could be successfully poached to book, because it ofers an alternative cheap car rental option. By contrast, a broad match to this same search query may show ads about “Argus travel,” “antique cars,” etc., and thus the conversion rate could be reduced by too many irrelevant results.

This set of results related to the interplays between keyword categories (generic, focal brand, and competing brand) and keyword match types (exact, broad, and phrase) ofers interesting bidding strategy implications. Advertisers should use exact match to protect their own focal-brand keywords, but at the same time, use broad and phrase matches to attack their competitors’ brand keywords.

Overall, we can summarize the results as follows:

Result 3. Exact match is associated with the highest CTR and CR for focal-brand keywords, relative to generic keywords. Broad and phrase matches can increase the CTR of competing-brand keywords, relative to generic keywords. For competing-brand keywords, relative to generic keywords, broad match decreases but phrase match increases the CR.

Several works in the literature discuss the length of keywords (Ghose and Yang 2009, Agarwal et al. 2012). Although it is not our focus, we can report our results related to keyword categories. First, longer keywords are associated with lower CTR and CR. Focal-brand keywords reinforce this efect for CR, and competingbrand keywords reinforce it for CTR. Overall, the implication is that advertisers should use short keywords to ensure advertising efectiveness.

Result 4. Shorter keywords are generally associated with better ad performance in terms of CTR and CR.

## 4.2. Cost Per Click

In the setting of position auctions, among all of the objectives of every advertiser, the two most important are (1) increasing the exposure (CTR and CR) and (2) reducing the CPC. We now turn to examine the second aspect.

Since the firm sets the bidding price and we use the CPC as a proxy, we cannot interpret the results in a causal way. Note that the firm chooses the bidding price when faced with a competitive market (Agarwal et al. 2011). This section will nonetheless ofer insights into how various keyword types are associated with diferent cost structures of advertising strategies.

The coeficients of Focal and Competing on CPC are both negative and significant, indicating that the firm incurs a higher CPC for generic keywords than for the other two types of keywords. Generic keywords are used to create user awareness, which may lead to future branded searches or direct type-in visits (Rutz and Bucklin 2011, Rutz et al. 2011). It is inevitable for diferent advertisers to bid aggressively on common generic keywords, making generic keywords more competitive and costly. On the flipside, firms can benefit from bidding more on cheaper focaland competing-brand keywords.

Result 5. Firms tend to incur higher CPCs for generic keywords than for branded keywords.

We can also examine the results related to keyword match types. In general, CPCs are higher for exact match than for broad and phrase matches. This finding is consistent with practitioners’ insights (e.g., Geddes 2011, Lolk 2013). This efect, however, is weakened in the case of phrase match for focal- and competingbrand keywords. Strategically, this result means that, relative to generic keywords, branded keywords incur higher CPCs when combined with phrase keyword match.

Result 6. Exact match is associated with higher CPCs than broad and phrase matches. With phrase match, branded keywords are associated with higher CPCs relative to generic keywords.

## 4.3. Rank

In this section, we examine how diferent keyword types are ranked.

The coeficient of Focal on Rank is significantly negative, while that of Competing on Rank is significantly positive. Relative to generic keywords, focalbrand (competing-brand) keywords are usually in higher (lower) positions. These findings suggest that search engines tend to assign better positions to focalbrand keywords because of their relevance. By contrast, competing-brand keywords are less relevant, and advertisers probably could not place very competitive bids for competing-brand keywords anyway. Therefore, we observe lower positions for competing-brand keywords. The literature suggests that lower positions for competing-brand keywords are not necessarily detrimental. Sayedi et al. (2014) give a rationale behind this observation: Users who click on the top ad slots are systematically diferent from those who click on lower positions. Those who click on lower positions, especially for branded keywords, are likely to be nonloyal customers who are still in the exploration and research stage. Having an ad at lower positions on competing-brand keywords would help advertisers capture these users in a cost-efective way.

Result 7. Relative to generic keywords, focal-brand (competing-brand) keywords are usually in higher (lower) positions.

For the interaction efect of match type and keyword categories, we find that, relative to exact-matched generic keywords, broad- and phrase-matched generic keywords are placed in higher positions. This is consistent with our previous finding that the competition for exact-matched keywords is greater. The interaction terms between match type and focal brand are positive, suggesting that the strong efect from using focalbrand keywords together with exact match dominates the bidding strategy. Similarly, the high returns of an exact match in a lower position dominate the bidding strategy for competing-brand keywords.

Result 8. Relative to exact-matched generic keywords, broad- and phrase-matched generic keywords are generally in higher positions. When combined with focal-brand (competing-brand) keywords, exact-matched keywords are in higher (lower) positions.

Overall, relative to generic keywords, focal-brand keywords are associated with higher CTR and CR and tend to increase the CTR and CR in more prominent positions; competing-brand keywords are associated with lower CTR but higher CR and tend to increase the CTR in less prominent positions. When considering the costs of advertising, firms tend to incur higher CPC for generic keywords than for branded keywords. In general, shorter keywords are associated with better ad performance in terms of CTR and CR. Relative to generic keywords, focal-brand (competingbrand) keywords are usually in higher (lower) positions. We also show that keyword match type is important and difers for the diferent keyword categories. Exact match is associated with the highest CTR and CR for focal-brand keywords, relative to generic keywords. Broad and phrase matches can increase the CTR of competing-brand keywords. For competing-brand keywords, a broad match decreases the CR, while a phrase match increases it. Exact match is associated with higher CPC than broad and phrase matches.

Table 4. Estimation Results of Order, Profit, and ROI

<table><tr><td></td><td>Order</td><td>Profit</td><td>ROI</td></tr><tr><td>Con</td><td>-26.538***</td><td>-3.496***</td><td>0.042***</td></tr><tr><td>Focal</td><td>44.861***</td><td>4.214***</td><td>0.226***</td></tr><tr><td>Competing</td><td>5.543*</td><td>1.471***</td><td>0.007</td></tr><tr><td>Rank</td><td>-2.159***</td><td>0.160***</td><td>-0.002***</td></tr><tr><td>Rank × Focal</td><td>-8.030***</td><td>-0.292**</td><td>-0.014*</td></tr><tr><td>Rank × Competing</td><td>0.730*</td><td>-0.101***</td><td>0.000</td></tr><tr><td>Length</td><td>-0.984***</td><td>-0.072***</td><td>-0.001***</td></tr><tr><td>Length × Focal</td><td>0.143</td><td>0.130***</td><td>0.003*</td></tr><tr><td>Length × Competing</td><td>-0.574**</td><td>-0.026***</td><td>-0.000</td></tr><tr><td>Broad</td><td>-5.532***</td><td>1.014***</td><td>-0.016**</td></tr><tr><td>Phrase</td><td>-5.486***</td><td>1.635***</td><td>-0.014*</td></tr><tr><td>Broad × Focal</td><td>-21.829***</td><td>-1.977**</td><td>-0.150***</td></tr><tr><td>Phrase × Focal</td><td>-14.609***</td><td>-1.804**</td><td>-0.130***</td></tr><tr><td>Broad × Competing</td><td>-7.637***</td><td>0.017</td><td>-0.011</td></tr><tr><td>Phrase × Competing</td><td>2.409</td><td>-1.036***</td><td>-0.004</td></tr><tr><td> $R^2$ </td><td>0.1739</td><td>0.1083</td><td>0.1024</td></tr></table>

<sup>∗</sup> p < 0.05; <sup>∗∗</sup> p < 0.01; <sup>∗∗∗</sup> p < 0.001.

When a phrase match is selected as the keyword match type, branded keywords, relative to generic keywords, are associated with higher CPC. Finally, relative to exact-matched generic keywords, broad- and phrasematched generic keywords are placed in higher positions. When combined with focal-brand (competingbrand) keywords, exact-matched keywords are in higher (lower) positions.

## 5. Order, Profit, and Return on Investment

To assess advertisers’ financial performance, we utilize the data containing each keyword’s daily total number of orders (hereafter “Order”) and Total Revenue. In addition, we compute the daily Total Expenses (number of clicks <sup>×</sup> CPC) and daily Total Profit (Total Revenue <sup>−</sup> Total Expenses) for each keyword. Return on investment (ROI) is defined as the ratio of Total Profit over Total Expenses.<sup>8</sup>

Table 4 reports the results. First, we analyze the influence of keyword category on keyword financial performance. Focal is significant and positive on all three financial indicators, implying that focal keywords perform significantly better than generic keywords with regard to orders, profit, and ROI. Although Competing is not significant on ROI, it is significantly positive on Order and Profit, suggesting that competing-brand keywords could generate more orders and higher profit than generic keywords. These results imply that attracting consumers is more profitable by using focalbrand and competing-brand keywords than by using generic keywords. These results highlight the importance of focal-brand and competing-brand keywords, as they target goal-directed consumers and are thus more efective in generating orders and profit than generic keywords.

Second, the negative coeficients of Rank on Order and ROI imply that for generic keywords, a lower rank (higher position on the search listings) is associated with more orders and higher ROI. Rank is positive on Profit, however, which means that lower ad positions are actually associated with higher profit. This indicates that profits of advertisers can be eroded by severe competition at the top positions. The interaction efect of Rank and Focal implies that the negative relationship between Rank and Orders/ROI is stronger for focal keywords than for generic keywords. In other words, moving up in the listing by one position is more efective for focal keywords than for generic keywords in generating more orders and higher ROI. In addition, the coeficient of Rank <sup>×</sup> Focal is significantly negative on Profit, reversing the relationship between keyword rank and profit from positive to negative. In other words, a negative relationship exists between keyword rank and profit for focal keywords but not for generic keywords. Furthermore, the interaction efect of Rank and Competing suggests that for competing-brand keywords, the negative relationship between Rank and Orders is weaker, while the relationship between Rank and Profit is still positive. These results suggest that, for generic and competing-brand keywords, a better position (lower rank) is costly, due to the intense competition of generic keywords and the low quality of competing-brand keywords. Therefore, higher-listed generic and competing-brand keywords may actually be associated with lower profit. These findings provide insights into understanding the “position paradox” (Jerath et al. 2011), as they ofer advertisers a new perspective on bidding strategies for ad positions.

Next, for generic keywords, the coeficient of Length is significantly negative on Order, Profit, and ROI, implying that shorter generic keywords are associated with more orders, higher profit, and a greater ROI. Moreover, the coeficient of Length <sup>×</sup> Focal is significantly positive on Profit and ROI and reverses the relationship between keyword length and Profit/ROI from negative to positive for focal keywords. By contrast, the interaction efect between Length and Competing suggests that the negative relationship between Length and Order/Profit is stronger for competitors’ keywords. In other words, shorter competing-brand keywords are associated with more orders and higher profit.

Regarding keyword match types, we find that exact match is associated with more orders and higher ROI than broad and phrase matches for both generic and competing-brand keywords. Exact-matched generic and competing-brand keywords, however, are associated with lower profit than broad and phrase-matched ones. The underlying reason for these findings may be that generic and competing keywords on exact matches are more competitive and costly than those on a broad match or a phrase match. By contrast, for focal keywords, an exact-match performs better than broad and phrase matches for all three financial variables.

6. Managerial Implications and Conclusion In sponsored search advertising, consumers using different categories of search terms (e.g., generic versus branded, broad versus exact) are likely to belong to diferent groups. This requires the advertisers to go beyond their focus on bidding price and consider nonmonetary decision variables, such as keyword categories and match types. Despite the significant practical value, little academic research has explored the impact of buying diferent categories of keywords (generic, focal brand, and competing brand) and choosing keyword match types (exact, phrase, and broad) on the performance of advertising campaigns. In this research note, we analyze the diferential performance outcomes.

We use a hierarchical Bayesian estimation framework to identify a system of simultaneous equations and derive results related to how keyword categories and keyword match types are associated with performance outcomes, such as CTR, CR, CPC, and rank.

Our findings suggest the importance of considering keyword selection in multikeyword position auctions. We find that, relative to generic keywords, focal-brand keywords are associated with higher CTR and CR, and competing-brand keywords are associated with lower CTR but higher CR. This result can potentially resolve the mixed findings in the literature. Without distinguishing focal- and competing-brand keywords and treating them together as branded keywords (Ghose and Yang 2009, Rutz and Bucklin 2011), prior works are not able to identify such nuances in keyword selection. We also find that advertisers should not always look for higher positions. When they are competing on focal brand keywords, higher positions will bring them higher exposure and more orders, but if they are competing on competing brand keywords, lower positions will bring them more orders. Without our unified framework, it is not possible to isolate these issues.

Some interaction terms in the model change the direction of the main efects. We find, for example, that shorter keywords are generally associated with higher profit and ROI, but for focal-brand keywords, longer keywords perform better with higher profit and ROI. Similarly, while focal-brand keywords are associated with higher ROI, if focal-brand keywords are used with broad match type, then the benefit disappears. These examples demonstrate the importance of studying keyword characteristics in a unified framework, so that we can isolate the efects when there are many forces driving the results. With our findings, advertisers can finetune their ad campaigns and avoid wasting valuable resources on keywords that are not profitable.

Our research has several limitations. First, our data are limited to a single firm. Major search engines do not provide competitive data or allow advertisers to “backtrack” to identify which competitors were listed in the same sponsored listings (Rutz and Bucklin 2011). Thus, we do not know the keyword ranks or other performance metrics of competitors’ paid search campaigns and cannot analyze the impacts of competing firms’ strategies. Second, firms ultimately want to examine CTR and CR measures to better allocate their budget. How to develop guidelines for budget allocation among various keywords would be a natural extension of this stream of studies.<sup>9</sup> Third, when we demonstrate the importance of considering keyword match types, we recognize that missing match types in the model may result in omitted variable bias. Yet at the same time, there may be other important sources of information that we cannot capture. For example, do demand seasonality or ofline sales influence keyword selection, online search, and financial performance? Even with a unified framework, we cannot exhaustively include all possible omitted variables. Future work could adopt a more controlled-experimental approach to study these issues. Finally, firms may exhibit different poaching behaviors depending on their market positions. A dominant firm, for example, may face low competition for competing-brand keywords. It would be useful to corroborate our findings with additional data sources that provide more detailed data about advertisers’ market positions.

Irrespective of the limitations, we hope this paper can clarify some conceptual relations between keyword characteristics and serve as a basis for future research on multikeyword position auctions.

## Acknowledgments

The authors thank Xi Chen for data analysis support and useful discussions. The authors also thank the review team for their thoughtful and constructive comments, which helped improve the paper significantly. All errors of fact, opinion, and findings are the sole responsibility of the authors.

## Endnotes

<sup>1</sup>https://www.emarketer.com/Article/US-Digital-Display-Ad -Spending-Surpass-Search-Ad-Spending-2016/1013442 (accessed December 2016).

<sup>2</sup> The paid-search services of Google, Yahoo!, and Microsoft operate in the same way, in principle (Ramos and Cota 2009).

<sup>3</sup> We thank the associate editor and an anonymous reviewer for suggestions that led to this categorization. In the remainder of the paper, we refer to the classification of generic-relevant, focal-brand, and competing-brand keywords as “keyword categories.”

<sup>4</sup> We highlight the features of the studies that are related to our paper. Table 1 shows that this paper fills a gap in the literature in using a hierarchical Bayesian model to study both keyword categories and keyword match types in a unified framework of multikeyword auctions.

<sup>5</sup>Regarding landing page quality, Ghose and Yang (2009, p. 5) “hired two independent annotators to rate each landing page” based on the metrics that Google uses and then computed the weighted average of the scores. We did not have the landing pages corresponding to given keywords in our data set. The company from which we obtained the data has in its campaign the same landing page: the home page.

<sup>6</sup> An ad’s quality score is determined by its historical performance. An ad with a better match with the keyword generally has a higher quality score. To achieve the same ranking, an ad with a lower quality score will need to bid higher than one with a better quality score.

<sup>7</sup> We thank the associate editor for raising this point.

<sup>8</sup> See Online Appendix B for details of the model specification and estimation related to Section 5.

<sup>9</sup> Two notable analytical studies of budget constraints in keyword auctions, Shin (2015) and Lu et al. (2015), both focus on a single keyword.

## References

Agarwal A, Hosanagar K, Smith MD (2011) Location, location, location: An analysis of profitability of position in online advertising markets. J. Marketing Res. 48(6):1057–1073.

Agarwal A, Hosanagar K, Smith MD (2012) Do organic results help or hurt sponsored search performance? Inform. Systems Res. 26(4):695–713.

Amaldoss W, Jerath K, Sayedi A (2015) Keyword management costs and “broad match” in sponsored search advertising. Marketing Sci. 35(2):259–274.

Animesh A, Viswanathan S, Agarwal R (2011) Competing “creatively” in sponsored search markets: The efect of rank, differentiation strategy, and competition on performance. Inform. Systems Res. 22(1):153–169.

Blake T, Nosko C, Tadelis S (2015) Consumer heterogeneity and paid search efectiveness: A large-scale field experiment. Econometrica 83(1):155–174.

Blankenbaker J, Mishra S (2009) Paid search for online travel agencies: Exploring strategies for search keywords. J. Revenue Pricing Management 8(2):155–165.

Brooks N (2004) The Atlas Rank Report II: How Search Engine Rank Impacts Conversions (Atlas Institute, Seattle).

Brunel FF, Nelson MR (2003) Message order efects and gender diferences in advertising persuasion. J. Advertising Res. 43(3): 330–341.

Chen Y, He C (2011) Paid placement: Advertising and search on the Internet. Econom. J. 121(556):F309–F328.

Chiou L, Tucker C (2012) How does the use of trademarks by thirdparty sellers afect online search? Marketing Sci. 31(5):819–837.

ClickEquations (2008) More profit with better match types. White Paper, http://tinyurl.com/cewhitepaper-pdf.

Dellarocas C, Zhang X, Awad NF (2007) Exploring the value of online product reviews in forecasting sales: The case of motion pictures. J. Interactive Marketing 21(4):23–45.

Desai PS, Shin W, Staelin R (2014) The company that you keep: When to buy a competitor’s keyword. Marketing Sci. 33(4):485–508.

Dhar V, Ghose A (2010) Research commentary—Sponsored search and market eficiency. Inform. Systems Res. 21(4):760–772.

Dou W, Lim KH, Su C, Zhou N, Cui N (2010) Brand positioning strategy using search engine marketing. MIS Quart. 34(2): 261–279.

Edelman B, Ostrovsky M, Schwarz M (2007) Internet advertising and the generalized second price auction: Selling billions of dollars worth of keywords. Amer. Econom. Rev. 97(1):242–259.

Enge E, Spencer S, Stricchiola J (2015) The Art of SEO: Mastering Search Engine Optimization, 3rd ed. (O’Reilly Media, Sebastopol, CA).

Geddes B (2011) 3 simple strategies for organizing your match types. Search Engine Land (March 28), http://searchengineland.com/ 3-simple-strategies-for-organizing-your-match-types-70096.

Ghose A, Yang S (2009) An empirical analysis of search engine advertising: Sponsored search in electronic markets. Management Sci. 55(10):1605–1622.

Jerath K, Ma L, Park YH, Srinivasan K (2011) A “position paradox” in sponsored search auctions. Marketing Sci. 30(4):612–627.

Karwal S (2015) Digital Marketing Handbook: A Guide to Search Engine Optimization, Pay per Click Marketing, Email Marketing, Content

Marketing, Social Media Marketing (CreateSpace Independent Publishing, North Charleston, SC).

Katona Z, Sarvary M (2009) The race for sponsored links: Bidding patterns for search advertising. Marketing Sci. 29(2): 199–215.

Kershen J (2016) SEO: SEO Marketing: 10 Proven Steps to Search Engine Optimization Trafic from Google (Amazon Digital Services, North Charleston, SC).

Liu D, Chen J, Whinston AB (2010) Ex ante information and the design of keyword auctions. Inform. Systems Res. 21(1): 133–153.

Lolk A (2013) 6 ways to optimally use keyword match types for AdWords success. Search Engine Journal (June 20), http://www .searchenginejournal.com/6-ways-to-optimally-use-keyword -match-types-for-adwords-success/64888.

Lu S, Zhu Y, Dukes A (2015) Position auctions with budget constraints: Implications for advertisers and publishers. Marketing Sci. 34(6):897–905.

Malthouse EC, Haenlein M, Skiera B, Wege E, Zhang X (2013) Managing customer relationships in the social media era: Introducing the social CRM house. J. Interactive Marketing 27(4):270–280.

Moe W (2003) Buying, searching, or browsing: Diferentiating between online shoppers using in-store navigational clickstream. J. Consumer Psych. 13(1):29–39.

Ramos A, Cota S (2009) Search Engine Marketing (McGraw-Hill, New York).

Rutz OJ, Bucklin RE (2011) From generic to branded: A model of spillover in paid search advertising. J. Marketing Res. 48(1): 87–102.

Rutz OJ, Trusov M (2011) Zooming in on paid search ads—A consumer-level model calibrated on aggregated data. Marketing Sci. 30(5):789–800.

Rutz OJ, Trusov M, Bucklin RE (2011) Modeling indirect efects of paid search advertising: Which keywords lead to more future visits? Marketing Sci. 30(4):646–665.

Sayedi A, Jerath K, Srinivasan K (2014) Competitive poaching in sponsored search advertising and its strategic impact on traditional advertising. Marketing Sci. 33(4):586–608.

Scott C (2013) Trademark strategy in the Internet age: Customer hĳacking and the doctrine of initial interest confusion. J. Retailing 89(2):176–189.

Shin W (2015) Keyword search advertising and limited budgets. Marketing Sci. 34(6):882–896.

Varian HR (2007) Position auctions. Internat. J. Indust. Organ. 25: 1163–1178.

Weber TA, Zheng Z (2007) A model of search intermediaries and paid referrals. Inform. Systems Res. 18(4):414–436.

Yang S, Ghose A (2010) Analyzing the relationship between organic and sponsored search advertising: Positive, negative, or zero interdependence? Marketing Sci. 29(4):602–623.

Zhang X, Zhu F (2011) Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. Amer. Econom. Rev. 101(4):1601–1615.

Zhang XM, Feng J (2011) Cyclical bid adjustments in search-engine advertising. Management Sci. 57(9):1703–1719.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.
