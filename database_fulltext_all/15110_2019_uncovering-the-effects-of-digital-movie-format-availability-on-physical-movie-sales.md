---
otero_id: 15110
otero_key: "UPKNWDFH"
title: "Uncovering the effects of digital movie format availability on physical movie sales"
authors: "Matthew J. Hashim; Sudha Ram; Zhulei Tang"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.10.016"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
<table><tr><td>PII:</td><td>S0167-9236(18)30173-8</td></tr><tr><td>DOI:</td><td>https://doi.org/10.1016/j.dss.2018.10.016</td></tr><tr><td>Reference:</td><td>DECSUP 13008</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>30 July 2018</td></tr><tr><td>Revised date:</td><td>29 October 2018</td></tr><tr><td>Accepted date:</td><td>31 October 2018</td></tr></table>

## Accepted Manuscript

Uncovering the effects of digital movie format availability on physical movie sales

![](/api/attachments/UPKNWDFH/fulltext/images/dbe617225f270da9c6a3deeea5fc487a7dca3177ddde274248a841722dfd9b44.jpg)

Matthew J. Hashim, Sudha Ram, Zhulei Tang

Please cite this article as: Matthew J. Hashim, Sudha Ram, Zhulei Tang , Uncovering the effects of digital movie format availability on physical movie sales. Decsup (2018), https://doi.org/10.1016/j.dss.2018.10.016

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

Uncovering the Effects of Digital Movie Format Availability on Physical Movie Sales

Matthew J. Hashim mhashim@email.arizona.edu

Sudha Ram ram@eller.arizona.edu

Zhulei Tang zhulei.tang@gmail.com

## Abstract

The impact of multi-channel technology-enabled digital goods on the sales of the physical counterpart faces uncertainty in the electronic commerce domain. We address the issue empirically by identifying the effect of the availability of digitally-delivered movies on physical DVD movie sales. Unique to our study is our interest in not only purchased digital goods but rented digital goods as well. We construct a robust panel dataset consisting of movie data collected from Amazon and Barnes and Noble on the same day for every movie observed. A key feature of our dataset is the multi-channel availability of digital purchase and digital rental movie formats at Amazon. Our results show that the availability of the digital purchase format does not have a significant effect on DVD sales. Surprisingly, the availability of the digital rental format is associated with a significant reduction in DVD sales. The results imply that a product substitution effect may be occurring between the digital rental and the physical DVD purchase of the same movie. We also conduct robustness tests to show under which conditions the effect is greatest. Our results also provide practical implications to inform strategies regarding movie format release windows.

Keywords: digital goods, cannibalization, multi-channel, DVD movies

## 1 Introduction

The expansion of electronic commerce during the last several decades has popularized the Internet as a sales and distribution channel for traditional physical goods. Today, firms not only sell their physical products online, but we have also observed a shift to the digital delivery of many types and formats of information goods using the Internet. In fact, the digital delivery of both music and books have either already captured, or are predicted to capture, a significant market share in their respective product domains as a result of using the Internet as a distribution channel for information goods (Stone 2008). The movie industry followed precedent set by the sales and distribution of information goods such as music and e-books using the Internet (e.g., iTunes, Wal-Mart, Amazon), by digitally distributing movie titles using download and/or streaming technology.

As a multi-channel product, movies can be delivered via a physical purchase channel (e.g., mailed physical disc), downloaded/streamed via a digital purchase channel, or downloaded/streamed via a digital rental channel (e.g., Amazon Video, Apple iTunes, Google Play, to name a few). In contrast to other types of information goods however, the delivery of movies in a digital format via the Internet is a young and continually evolving distribution channel. To provide an example, the multi-channel retailer Amazon

entered the digital distribution marketplace by launching the Amazon Unbox online movie service in September 2006. The availability of this type of information good is of interest to researchers because of the ability to acquire digitally distributed movies by either a purchase transaction or by a rental transaction.<sup>3</sup> The ability to consume via purchase or rental is a unique characteristic of movies and is in contrast with the usual consumption of other types of information goods.

The introduction of a digital rental market for movies is a particularly compelling avenue for research, as it is a distinctive phenomenon for information goods and is limited to the movie-context. The phenomenon is grounded in the common practice of renting and/or buying movies using the typical physical channels. Given that the prior research has shown that digital distribution channels will continue to gain market share in comparison with physical distribution channels (Brynjolfsson et al. 2013; Carr 2011; Gong et al. 2015), our paper strives to answer the following research questions. Does the digital purchase and/or digital rental movie format displace the sales of existing physical movies as the market transitions to digital delivery channels? Or, are these alternate formats of movie consumption potentially complementary to physical sales (see e.g., Carr 2011; Shocker et al. 2004)?

To the best of our knowledge, our paper is one of the first to explore the cannibalization effects introduced by the distribution of identical information goods within a platform except for the delivery channel used to reach the consumer.<sup>4</sup> Our study is also the first effort to consider the cannibalization effect that may occur when a digital rental is introduced for a product that is otherwise available for purchase only within the same electronic commerce platform. While previous research has shown the substitution effect in other settings (see e.g., Danaher et al. 2010; Ghose et al. 2006; Yu et al., 2017), few studies have examined the integration of sales availability of an otherwise identical product within the same platform.

To answer our research questions, we collected daily movie data from two competing ecommerce websites during a period after the introduction of digital sales and before subscription models had been implemented in the marketplace. Thus, our data provides for a clear understanding free of confounding factors originating from inconsistently implemented and available subscription models,

allowing us to document the shift from the historically physical only delivery of movies, to the now common digital delivery of movies. Further, our data provide a clear set of controls in the fact that the sites differ in their availability of the digital-distribution channel—one offers digital purchases and digital rentals for some movies, whereas the other does not. Both sites sell physical DVDs and have also been used by the prior literature for other information goods studies (e.g., Brynjolfsson et al. 2013; Chevalier and Goolsbee 2003; Ghose et al. 2006; Gong et al. 2015; and others).

We construct an econometric model to analyze our data and show that the digital purchase option is not associated with a significant cannibalization effect on DVD sales, whereas the digital rental option is surprisingly associated with a significant decrease in DVD sales. We also conduct robustness tests to determine if there are any common drivers of the results. Regarding these drivers, we observe a significant decrease in DVD sales for those movies that are available as a digital rental and have the following characteristics: are new releases; have few reviews; and have a large price discount for the rental in comparison with the price of the DVD. We also duct additional robustness tests of our results by creating a matched sample of our observational data to address any remaining concerns with endogeneity, and the results remain consistent throughout the analyses.

## 2 Related Literature

The widespread use of the Internet has created opportunities to sell a variety of new products, especially digital goods, leading to potential cannibalization effects across channels. Technology has also reshaped industries including music, movies, software, books and video games (Bhattacharjee et al. 2011). Previous research has considered cross-channel effects in online versus offline channels. Ghose et al. (2006) study new and used book markets and find an associated cannibalization effect between them. Their study documents the potential for both formats reaching a new market and increasing the possibility for additional sales of the primary market. The result was previously inferred by Amazon’s CEO Jeff Bezos, in contrast to the Author’s Guild and Association of American Publishers (O’Reilly 2002) beliefs. Brynjolfsson et al. (2009) show that Internet retailers and brick-and-mortar retailers compete heavily on popular products but less so on niche products.

## ACCEPTED MANUSCRIPT

From the perspective of customer decision-making, Varian (2000) has discussed alternative ways to consume information goods, including buying, sharing, and renting. Consumers face many alternatives in every step of their decision journey (Court et al. 2009). Channel choice as well as the format to consumer information goods are among them. Gupta et al., (2004) examine factors that affect consumer switching from off-line to on-line shopping. Moeller and Wittkowski (2004) have found convenience and trend consciousness are among the factors to explain the growing consumer preference of renting over ownership of consumer goods. In the context of home video retailing, Knox and Eliashberg (2009) have explored consumer’s decision to rent versus buy for movie DVDs.

With the introduction of the online channel, and more recently digital channels, such as mobile channels and social media, researchers have studied multi-channel marketing extensively (Kannan et al. 2009; Verhoef et al. 2015). Earlier marketing literature looked at customer migration from traditional channels, such as catalog, to new channels, such as the Web (Ansari et al. 2008), and cannibalization of the Internet channel on traditional paper media (Deleersnyder et al. 2002). The online channel has also been found to increase customer profitability (Gensler et al. 2012) and to influence firm value through abnormal stock returns (Homburg et al. 2014). A more recent study by Xu et al. (2014) has found digital distribution channels, such as mobile news apps, have a spillover effect on the corresponding mobile news website. Regarding music subscription services, Aguiar and Waldfogel (2015) have shown that a subscription service such as Spotify does cannibalize the purchase of digital music and may be associated with a reduction of piracy. The addition of new channels and the integration of these new channels in online and offline settings suggest that retailing is moving from multi-channel to omni-channel (Brynjolfsson et al. 2013).

Further, the motion picture industry has been the subject of numerous studies by academic researchers. Eliashberg et al. (2006) have reviewed the academic research on the motion picture industry. Hennig-Thurau et al. (2007) study the timing and order of four traditional movie distribution channels using data from the United States, Japan and Germany. They found that the distribution structure that optimizes revenue differs significant across countries. There is also growing literature on the effect of

# ACCEPTED MANUSCRIPT

piracy on legitimate movie purchase/consumption. For example, Danaher et al. (2010) have looked at how removal and restoring of NBC content from iTunes affects DVD sales on Amazon and digital piracy. Ma et al. (2014) have analyzed whether, and how much pre-release movie piracy costs box-office sales. Smith and Telang (2009) find that movie broadcasts increase the sales of DVD movies and to a lesser extent, increase piracy of the same movie.

Despite the prevalence of discussion in the popular press about the heated competition among alternative online movie streaming services (see e.g., Flacy 2015), we are aware of just a couple other academic studies analyzing cross-channel effects of alternative formats on digital movie sales. Gong et al. (2015) have examined the impact of price discounts on sales in digital purchase and digital rental formats, whereas Yu et al. (2017) have considered the effects of subscription-based services (i.e., Netflix and Hulu) on physical DVD sales. Our work is substantially different in comparison to the previous studies comparing the sales of physical and digital counterparts. Unlike the prior work, we focus on possible cannibalization comparisons between physical, digital, and rental formats and within a particular multichannel retailer.

In summary, the existing literature has examined the cross-channel effects of online and offline sales of information goods, and the issue continues to be of interest as new digitally-enabled phenomena emerge. Although ease of piracy has been shown to be a concern of the motion picture industry, this concern has only fueled the interest in studying cross-channel effects of the digital distribution of movies. Our paper also contributes to this stream of literature. Where our paper moves beyond the existing work is our positioning with the decision-making literature such as Varian (2000), Moeller and Wittkowski (2004), and Knox and Eliashberg (2009). That is, to the best of our knowledge, our work is the first to consider potential cross-channel effects of not only the digital purchase decision, but the digital rental decision on physical movie sales. Next, we discuss the data and approach for the empirical analysis.

## 3 Data

To answer our research questions and discover if consumers are trading off physical copies of movies for digital copies, we first identified suitable data sources offering multi-channel distribution of movies.

Amazon.com and Barnesandnoble.com (BN) are popular electronic commerce platforms that also offer rich observable movie-specific data, strict differences in movie distribution channels offered, as well as clear indicators of product quality and sales.

We also carefully chose a data collection period that was after the introduction of multi-channe digital sales, but before subscription models had been implemented by retailers. By taking this approach, our data are free of potentially confounding issues that subscription models may cause (even within Amazon itself), providing a clear understanding of a shift from physical to digital delivery of movies. Another critical feature of our dataset is the existence of the digital delivery channel for some movies on Amazon. In contrast, BN does not offer a digital delivery channel for the consumption of movies. That is, we can observe product characteristics and the associated changes to sales ranking at BN, but without confounding effects from potential intra-site competition from digital formats within the BN platform. Therefore, observable product characteristics of movies from BN provide our dataset with a very strong set of controls for movie popularity.

Further, prior literature has established that observable product sales rank data is a suitable proxy for actual product sales (e.g., Brynjolfsson et al. 2003; Chevalier and Goolsbee 2003; Smith and Telang 2009) on electronic commerce platforms such as Amazon.com and BN. Initial studies of price competition between online booksellers determined that actual sales could be estimated by the product sales rank (Brynjolfsson et al. 2003; Chevalier and Goolsbee 2003). Although the prior studies focused primarily on book sales, the foundation established of using sales ranks to proxy for product sales was further expanded upon by Smith and Telang (2009) to estimate movie sales. We apply a comparable data collection technique to observe DVD movie product variables and product characteristics from Amazon and BN. We build upon the prior works by constructing a DVD movie dataset that controls for influences on the widely-used proxy for product sales, observing movie characteristics and the effects on product sales rank. Our use of secondary data from a competing website to Amazon allows us to control for common drivers of movie popularity, thereby capturing the effects of other observable variables on the popularity of DVD movies.

# ACCEPTED MANUSCRIPT

## 3.1 Data Collection

We collected movie data over a 33-day period from July 4, 2008 through August 5, 2008. Our sample is based upon the bestselling movie list from Amazon.com and is initially limited to 4,800 titles for two reasons. First, at the time of our data collection, Amazon restricted their bestselling movie list to the top 4,800 movies on any given day. Second—and more importantly—we desire to observe variation in sales formats. That is, more popular movies are more likely to have daily movement in sales rank in comparison to less popular movies, and more popular movies are more likely to be updated with customer reviews and other observable variables.

To establish a robust and repeatable data collection procedure, we launched the data collection scripts used in our study at approximately the same time for each day in the collection period for both Amazon and BN. Doing so maintains consistency in our approach to data collection, by minimizing any time-of-day effects that may be present.<sup>5</sup> We collected and extracted universal product codes (UPC) as listed on Amazon's DVD product pages for each movie in order to allow us to match and observe the identical movie from BN.<sup>6</sup> Matching on UPC code between data sources is critical to our study, especially in the context of a good that may not have a unique title. That is, the use of UPC ensures that the movies are identical across websites, because many different editions and formats are typically available for the same movie title (e.g., fullscreen, widescreen, as well as non-similar products such as books). Different editions and formats may not experience the same interest from consumers, thus the need to match the product exactly so that our empirical specification is as free of error as possible.

As discussed previously, we initially collected Amazon ASINs (Amazon standard item numbers) for 4,800 movies, but the number of movies in our final dataset is reduced dramatically after performing the following procedure. First, we must have a UPC from Amazon to match to the identical UPC at BN, otherwise it would be impossible to use BN data as controls in the analyses. Second, we limit our study to widescreen movies to maintain consistent content utility between digital and physical formats. That is, the content experienced by the consumer from the widescreen DVD format best resembles the format

# ACCEPTED MANUSCRIPT

provided by the digital delivery format. In contrast to the widescreen format, the “pan and scan” cropped video or even high definition video, provide a dissimilar experience in comparison to the digital delivery format (i.e., worse experience in the former example, superior in the latter). Third, although Amazon includes the sale of television shows in both the DVD and the digital delivery format, we removed all DVDs that were in the Television genre by isolating the final sample to the category “Movies” only. We do so for the following practical reason. If a consumer purchases a DVD of a television series, the consumer receives the entire series and/or collection of multiple television shows. Conversely, it is possible to purchase an individual episode in the digital delivery format, which introduces unwanted complication due to the aggregation of all DVD episodes under a single sales rank. Lastly, we also capture the ability for customers to pre-order DVD movies, whereas digital delivery formats cannot be pre-ordered. Our approach for creating the unique dataset leaves us with a balanced panel of 872 movies, with every movie observed for every day of the collection period.

In addition to the DVD movie data just described that we collected from Amazon and BN, we also collected data for those movies that are available for purchase or rent using the digital delivery format. To ensure our dataset includes accurate matches between the digital delivery formats and the same movie in DVD format, we captured ASINs from the digital delivery product and matched them to ASINs listed on the DVD product page. More specifically, Amazon hyperlinks all available alternative formats on the page which the consumer views when browsing a specific DVD movie. The hyperlinks for the alternative products contain the ASINs for the digital delivery formats. Further, we also collected the sales position number and sales price from both the digital purchase and digital rental bestselling pages to use in some of the analyses. Note, although sales rank is not explicitly listed on the digital format product pages, the movies are presented to consumers by bestselling position (i.e., highest selling is assigned position 1). Therefore, we assign a proxy for sales rank from the bestselling position number as this is the best data available for representing movie popularity for each digital format.

## 3.2 Controls and Other Variables of Interest

Our study is primarily concerned with the impact of digital format availability on DVD sales, so the possibility of varying preferences amongst consumers and movie popularity must be controlled. We do so by collecting BN DVD product data as already described. For example, if the digital rental or digital purchase rank at Amazon is a top seller but the associated DVD sales rank is not, we might suspect product competition and perhaps cannibalization if the DVD is popular at another site. The reason for this is we would expect the popularity of the DVD to drive a similar sales pattern at both sites as shown by prior work (Chevalier and Goolsbee 2003; Chevalier and Mayzlin 2006). Observing both these sources of data together would provide an interesting result and insight into what incorporating the digital delivery format means to average sales of DVDs at one retailer, especially given the robust specification used, and controls included in our analyses.

<table><tr><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td colspan="5">DVD Movies (n = 872)</td></tr><tr><td>Amazon DVD Sales Rank</td><td>3,366.33</td><td>3,155.07</td><td>1</td><td>46,634</td></tr><tr><td>BN DVD Sales Rank</td><td>6,854.24</td><td>6,952.46</td><td>1</td><td>68,694</td></tr><tr><td>Amazon DVD Price</td><td>15.85</td><td>11.21</td><td>3.99</td><td>209.99</td></tr><tr><td>BN DVD Price</td><td>19.97</td><td>13.76</td><td>4.99</td><td>260.99</td></tr><tr><td>Count of Days Since DVD Release $^{7}$ </td><td>940.73</td><td>1,002.25</td><td>-102</td><td>4,150</td></tr><tr><td>DVD In Stock</td><td>0.98</td><td>0.14</td><td>0</td><td>1</td></tr><tr><td>Amazon Avg. Star Rating</td><td>4.08</td><td>0.59</td><td>0</td><td>5</td></tr><tr><td>Amazon Count of Reviews</td><td>173.84</td><td>215.41</td><td>0</td><td>2,116</td></tr><tr><td>BN Avg. Star Rating</td><td>3.35</td><td>1.97</td><td>0</td><td>5</td></tr><tr><td>BN Count of Reviews</td><td>7.40</td><td>16.40</td><td>0</td><td>219</td></tr><tr><td colspan="5">Digital Purchase Movies (n = 238)</td></tr><tr><td>Amazon DVD Sales Rank</td><td>2,853.17</td><td>2,351.44</td><td>1</td><td>27,023</td></tr><tr><td>BN DVD Sales Rank</td><td>6,689.22</td><td>6,869.05</td><td>2</td><td>65,988</td></tr><tr><td>Amazon DVD Price</td><td>14.82</td><td>5.47</td><td>3.99</td><td>45.99</td></tr><tr><td>BN DVD Price</td><td>19.16</td><td>8.61</td><td>4.99</td><td>62.99</td></tr><tr><td>Count of Days Since DVD Release</td><td>883.48</td><td>1,026.77</td><td>-25</td><td>3,961</td></tr><tr><td>DVD In Stock</td><td>0.99</td><td>0.10</td><td>0</td><td>1</td></tr></table>

Regarding control variables, DVD movie-specific variables include sales rank, price, in/out-of stock status, movie customer rating (i.e., average star rating, count of reviews), count of days since the DVD release date, and the availability of digital delivery formats for a specific movie. In regards to the digital delivery formats, bestselling numbers, price, purchase and/or rental availability, and date made available (implied by the actual day the digital format appears on the site, if during our data collection window) are used for the empirical analysis. Summary statistics across the entire sample (n = 28,776; 872 DVD movies over 33 days; 238 Digital Purchase; 181 Digital Rental) are presented in Table 1.

Table 1: Movie Summary Statistics by Format

<table><tr><td>Amazon Avg. Star Rating</td><td>3.94</td><td>0.59</td><td>0</td><td>5</td></tr><tr><td>Amazon Count of Reviews</td><td>191.89</td><td>202.28</td><td>0</td><td>1,919</td></tr><tr><td>BN Avg. Star Rating</td><td>3.71</td><td>1.62</td><td>0</td><td>5</td></tr><tr><td>BN Count of Reviews</td><td>7.86</td><td>14.26</td><td>0</td><td>145</td></tr><tr><td colspan="5">Digital Rental Movies (n = 181)</td></tr><tr><td>Amazon DVD Sales Rank</td><td>3,054.42</td><td>2,810.49</td><td>1</td><td>27,023</td></tr><tr><td>BN DVD Sales Rank</td><td>6,957.24</td><td>6,981.10</td><td>12</td><td>65,988</td></tr><tr><td>Amazon DVD Price</td><td>15.36</td><td>5.78</td><td>3.99</td><td>45.99</td></tr><tr><td>BN DVD Price</td><td>20.78</td><td>8.47</td><td>4.99</td><td>62.99</td></tr><tr><td>Count of Days Since DVD Release</td><td>920.34</td><td>1,124.42</td><td>-25</td><td>4,059</td></tr><tr><td>DVD In Stock</td><td>0.98</td><td>0.12</td><td>0</td><td>1</td></tr><tr><td>Amazon Avg. Star Rating</td><td>3.92</td><td>0.65</td><td>0</td><td>5</td></tr><tr><td>Amazon Count of Reviews</td><td>174.60</td><td>169.45</td><td>0</td><td>1,146</td></tr><tr><td>BN Avg. Star Rating</td><td>3.66</td><td>1.72</td><td>0</td><td>5</td></tr><tr><td>BN Count of Reviews</td><td>6.32</td><td>7.65</td><td>0</td><td>39</td></tr></table>

## 4 Analysis

We use several panel data specifications with fixed effects to conduct the majority of our analyses. The fixed effects model allows us to assess the effect of the availability of digital purchase and digital rental formats on DVD sales over time, while controlling for individual movie effects and the possibility for date effects. Logs were taken of each of the variables, with the exceptions of the dummy variables and days since release of the DVD, following precedent set by the literature (see e.g., Chevalier and Goolsbee 2003; Chevalier and Mayzlin 2006), and providing a better fit and scale for the data. Specifically, variables such as sales rank and price may vary from very small to very large in magnitude. Therefore, we follow the log transformation in the rest of the paper.

We create dummy variables for each of the digital delivery formats to determine if the availability of digital formats have any effect on DVD sales rank. If the movie was available in the respective digital delivery format (i.e., purchase, rental) on a day in the data collection period, we assigned a one for the particular digital format for that particular day. If the particular digital format was unavailable, we assigned a zero. Note, every movie available for purchase by digital delivery does not necessarily have a digital rental option and vice versa. Overall, there are 181 movies that are available as a digital rental and 238 movies that are available as a digital purchase over the 872 DVDs, providing a reasonable representation of the digital formats for use in our analysis.

## 4.1 Econometric Model

We analyze the data and test the robustness of our dummy variable approach by using several two-way fixed effects models. First, we establish a baseline model that includes a fixed effect for each of the 872 movies represented as ??????????<sub>??</sub> as well as a fixed effect for the date represented by ?????? $e _ { t } \mathrm { i }$ :

$$
\begin{array}{c} L n (A m a z o n D V D S a l e s R a n k) _ {i t} = \beta_ {0} + \beta_ {1} D i g i t a l P u r c h a s e _ {i t} + \beta_ {2} D i g i t a l R e n t a l _ {i t} + M o v i e _ {i} + \\ D a t e _ {t} + \varepsilon_ {i t} \end{array} \tag {1}
$$

The use of fixed effects is appropriate for our model as each DVD has unique characteristics about that movie that are time invariant. For example, a movie will be assigned to a genre, include actors, filming location/s, have producer/s, and other movie specific characteristics that are both time and format invariant. Also, movie fixed effects help us to account for sources of bias due to potential endogeneity, as the fixed effect captures unobserved movie-specific characteristics. Date fixed effects are also appropriate for our model because our tests determined that the date effects were not jointly equal to zero. Therefore, we included a second fixed effect for each day in the time period to control for any variation that could possibly be explained by the particular day the data are collected.

Now that the baseline model is established, we next introduce controls to the baseline model. the coefficients of our predictor variables, as well as validate the robustness of our specification. The full model is presented in the specification below:

$$
L n (A m a z o n D V D S a l e s R a n k) _ {i t} =
$$

$$
\begin{array}{c} \beta_ {0} + \beta_ {1} \text {Digital Purchase} _ {i t} + \beta_ {2} \text {Digital Rental} _ {i t} + \beta_ {3} \text {Ln(Amazon DVD Price)} _ {i t} + \\ \beta_ {4} \text {Ln(BN DVD Sales Rank)} _ {i t} + \beta_ {5} \text {Ln(BN DVD Price)} _ {i t} + \beta_ {6} \text {Days Since DVD Release} _ {i t} + \\ \beta_ {7} \text {DVD In Stock} _ {i t} + \beta_ {8} \text {Ln(Amazon Review Count)} _ {i t} + \beta_ {9} \text {Ln(Amazon Star Rating)} _ {i t} + \\ \beta_ {1 0} \text {Ln(BN Review Count)} _ {i t} + \beta_ {1 1} \text {Ln(BN Star Rating)} _ {i t} + \text {Movie} _ {i} + \text {Date} _ {t} + \varepsilon_ {i t} \end{array} (2)
$$

As might be expected due to the daily collection of our data, serial correlation in the residuals is observed, which may inflate the standard errors while coefficient estimates remain unbiased. To address the effect that serial correlation has on standard errors, we implement a conservative approach of using robust standard errors clustered on movie. Using clustered robust standard errors minimizes inflation in the standard errors due to serial correlation (see e.g., Kezdi 2004; Petersen 2009; Wooldridge 2002). Robust standard errors also address any potential heteroskedasticity in the panels. In addition, we also conducted a Harris-Tsavalis test to address the possibility of unit roots in our panels. We found that our dataset exhibits stationarity in the panels (Harris and Tzavalis 1999), and unit roots are not a concern. Overall, our conservative approach for the analysis errs on inefficiency of the standard errors, while ensuring the coefficient estimates remain unbiased.

## 4.2 Results

We first present results from the two-way fixed-effects models specified in the prior subsection in Table 2. Column (2) builds upon the baseline model by including Amazon control variables. We omit BN control variables in Column (2) to ensure consistency of results as more controls are included. Column (3) differs from (1) and (2) in that it is a full model containing all of the control variables. In Column (1), we observe that the existence of the digital rental format has a positive and significant coefficient (0.325, pvalue < 0.01). The positive and significant result provides evidence that if the rental alternative exists, buyers may prefer the rental format instead of purchasing the DVD. The sign and significance of the result on digital rental is consistent for the no BN and full models as well as shown by Columns (2) and (3). We do not however find the same support for the digital purchase option. That coefficient is not statistically significant in any model (-0.260, p-value > 0.10; -0.216, p-value > 0.10; -0.229, p-value > 0.10). The negative sign on the coefficient is consistent in all models, suggesting the consumer may prefer the DVD to the digital purchase, although the effect is not statistically significant. The inclusion of Amazon (Columns 2 and 3) and BN (Column 3) control variables behave as expected and are consistent with the prior literature. For example, if the price of the DVD goes up at Amazon, the sales become worse (positive sign). As the BN price goes up, the Amazon sales rank gets better (negative sign), and as the BN rank becomes less popular, the Amazon rank becomes less popular (positive sign).

Overall, the results of the panel data analyses suggest that the presence of the digital rental format is associated with a significant cannibalization effect on DVD sales. In contrast, the presence of the digital purchase format does not appear to have a statistically significant effect on DVD sales.<sup>8</sup> Further, the results are consistent and stable as additional control variables from Amazon and the competing platform BN are included. We note here that endogenously controlled recommender systems could be used by

# ACCEPTED MANUSCRIPT

either site to drive consumers to particular movies. Endogenously determined marketing expenditures and pricing decisions are also used but addressed by the inclusion of movie and time fixed effects. However, the consumer’s choice once on the page to rent or buy is not endogenously determined. Said another way, the consumer acquires the movie in the format that they prefer, regardless of the existence of recommender systems, marketing expenditures, and other conceivably endogenous factors. This plays out in the baseline model where potentially endogenous variables are not included and the results still hold across models. We consider additional models as well as sample-matching later in Section 5 to further explore the data and address potential concerns. Next, we consider sales ranks for the digital formats.

Table 2: Effect of Digital Formats on Physical DVD Sales

<table><tr><td>DV: Amazon DVD Sales Rank</td><td>Baseline(1)</td><td>No BN(2)</td><td>Full Model(3)</td></tr><tr><td>Digital Purchase</td><td>-0.260(0.176)</td><td>-0.216(0.166)</td><td>-0.229(0.180)</td></tr><tr><td>Digital Rental</td><td>0.325**(0.112)</td><td>0.332**(0.114)</td><td>0.319**(0.117)</td></tr><tr><td>Amazon DVD Price</td><td></td><td>1.311***(0.063)</td><td>1.306***(0.063)</td></tr><tr><td>BN DVD Sales Rank</td><td></td><td></td><td>0.037***(0.006)</td></tr><tr><td>BN DVD Price</td><td></td><td></td><td>0.004(0.041)</td></tr><tr><td>Days Since DVD Release</td><td></td><td>0.007***(0.001)</td><td>0.007***(0.001)</td></tr><tr><td>In Stock</td><td></td><td>0.011(0.054)</td><td>-0.005(0.057)</td></tr><tr><td>Amazon Avg. Rating</td><td></td><td>0.293†(0.169)</td><td>0.306†(0.159)</td></tr><tr><td>Amazon # Reviews</td><td></td><td>-0.217(0.138)</td><td>-0.226†(0.124)</td></tr><tr><td>BN Avg. Rating</td><td></td><td></td><td>0.032(0.209)</td></tr><tr><td>BN # Reviews</td><td></td><td></td><td>0.353(0.224)</td></tr><tr><td>Constant</td><td>7.581***(0.041)</td><td>-2.267**(0.725)</td><td>-2.800***(0.798)</td></tr><tr><td>Observations</td><td>28,776</td><td>28,776</td><td>28,776</td></tr><tr><td>Movies</td><td>872</td><td>872</td><td>872</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.890</td><td>0.901</td><td>0.902</td></tr></table>

Robust standard errors are in parentheses and are clustered by Movie.  
Regressions include fixed effects for Movie and Date.  
\*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, † p < 0.10.

## 4.3 Digital Format Sales Ranks

Representing the availability of the digital formats by using of a dummy variable approach may not give us a clear understanding of the effect on DVD sales rank that may be occurring when the coefficient is not statistically significant. For example, perhaps the digital purchase format is reaching a new audience that otherwise would not have purchased the DVD, and thus the coefficient may not be statistically significant in that scenario, or others as well.

Table 3: Effect of Digital Format Sales Rank and Price on Physical DVD Sales

<table><tr><td>DV: Amazon DVD Sales Rank</td><td>(1)</td></tr><tr><td>Digital Purchase Rank</td><td>0.074**(0.026)</td></tr><tr><td>Digital Purchase Price</td><td>0.168(0.220)</td></tr><tr><td>Digital Rental Rank</td><td>-0.048*(0.020)</td></tr><tr><td>Digital Rental Price</td><td>0.081(0.083)</td></tr><tr><td>Amazon DVD Price</td><td>1.189***(0.136)</td></tr><tr><td>BN DVD Sales Rank</td><td>0.048*(0.020)</td></tr><tr><td>BN DVD Price</td><td>0.178(0.115)</td></tr><tr><td>Days Since DVD Release</td><td>0.010***(0.002)</td></tr><tr><td>In Stock</td><td>-0.420(0.259)</td></tr><tr><td>Amazon Avg. Rating</td><td>0.077(1.651)</td></tr><tr><td>Amazon # Reviews</td><td>-0.364***(0.052)</td></tr><tr><td>BN Avg. Rating</td><td>1.227***(0.287)</td></tr><tr><td>BN # Reviews</td><td>-0.186(0.342)</td></tr><tr><td>Constant</td><td>-4.603(3.143)</td></tr><tr><td>Observations</td><td>4,958</td></tr><tr><td>Movies</td><td>165</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.917</td></tr></table>

Robust standard errors are in parentheses and are clustered by Movie.  
Regression model includes fixed effects for Movie and Date.  
\*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, † p < 0.10.

To address the uncertainty, we also regress the DVD sales rank on the digital format sales rank and digital format price for both purchase and rental channels. ${ \mathrm { S o } } ,$ instead of only using dummy variables for the digital formats as independent variables, we include these continuous variables instead. The digital format sales ranks are captured from the digital format bestseller pages and provide some insight into how the popularity and price of the digital formats impact DVD sales, rather than just the existence of them as presented earlier in Table 2. In our sample of 872 movies, 165 of them are available in both digital formats on the same day. Therefore, our sample size is limited to an unbalanced panel of 4,958 observations representing the 165 movies that have both digital formats at some point during our data collection period. Results are presented in Table 3.

We find that the digital rental rank has a negative and significant coefficient (-0.048, p-value < 0.05), whereas the digital purchase rank has a positive and significant coefficient (0.074, p-value < 0.01). The results are consistent with our prior findings as the rental makes the DVD sales rank worse while the purchase format is associated with a move in the same direction as the DVD format. There seems to be a significant relationship between the popularity of the two purchase formats, as sales of both purchase formats are increasing compared to those movies that do not have a digital purchase format available. So, we propose that a new segment of consumers prefers digital ownership to physical ownership. However, two facts must be noted: first, the economic significance of the impact of sales ranks for each digital format is small; second, we do not have a measure of market segment growth. Also, the price for either format does not appear to be a significant predictor of DVD sales, but these prices do not tend to vary over time for each of the digital formats.

## 4.4 Estimating Economic Impacts

## 4.4.1 Overall Economic Interpretation

The economic effect of the existence of a digital format on DVD movie sales can be estimated by using the coefficient obtained from our regression analysis for the digital rental dummy on our proxy for sales (DVD sales rank). We focus on the results provided in Column (3) of Table 2 regarding the digital rental format. The econometric analysis used in that model is the most conservative of the approaches taken and is likely inefficient and unbiased. The technique for estimating economic effects using sales rank was first developed by Chevalier and Goolsbee (2003) for book sales at Amazon and was confirmed by Brynjolfsson et al. (2003) with actual book sales data. Similar approaches have been used for estimating App Store sales (Garg and Telang 2013). The following equation illustrates the relationship:

$$
L n (S a l e s) = \beta \times L n (A m a z o n S a l e s R a n k)\tag{3}
$$

The estimate of the relationship between sales rank and actual sales was re-calibrated by Smith and Telang (2009) for DVD movie sales at Amazon and the $\beta$ estimate updated to −1.70. They provide the subsequent equation for estimating the percentage change in sales which we update to measure the impact of the existence of the digital rental format on DVD sales.

$$
\Delta s a l e s = e ^ {\beta \times D i g i t a l R e n t a l} - 1\tag{4}
$$

Following their work, we estimate the change in sales percentage by setting ?? = −1.70 and ?????????????? ???????????? = 0.319 (Column (3) of Table 2). The result is an estimated change in sales of the DVD of −41.86%. While the estimate does appear to be quite large, it illustrates the potential for a high level of cannibalization that occurs for those movies that have the digital rental format available.

## 4.4.2 Digital Rental Format Release Window

In all of the regressions presented earlier, the coefficient capturing the effect of days since release of the DVD movie has a statistically significant effect on DVD sales rank in each of the models presented (e.g., 0.007 in Column (3) of Table 2, and 0.009 in Column (1) of Table 3; both having a p-value < 0.001). The result intuitively suggests that for every day the DVD movie gets older, the sales ranking of the DVD gets worse (i.e., numerically higher sales rank). Given that our results have also shown that the digital rental format availability is associated with a significant decrease in DVD sales rank, a question that follows is whether or not there is an interaction of these two independent variables. That is, the presence of a significant interaction could provide some insight into the number of days that it takes since release of the DVD movie for a digital format to not have an effect on the sales of the physical format. The existing literature has considered the question of optimal movie release windows (e.g., at what point after movie release to theatres should home video, streaming, etc., be released?), but primarily through a profitmaximizing lens using mathematical modeling (see e.g., August et al. 2015), or prior to the availability of streaming formats (see e.g., Mukherjee and Kadiyali, 2011). Our empirical analysis complements the existing theoretical work in that we can provide managerial insights generated from the data, without restricting the analysis to any explicit assumptions about profit-maximization.

Table 4: Interaction Effect of Days Since Release and Digital Format Availability

<table><tr><td>DV: Amazon DVD Sales Rank</td><td>(1)</td></tr><tr><td>Digital Purchase</td><td>-0.295(0.205)</td></tr><tr><td>Digital Rental</td><td>0.400**(0.126)</td></tr><tr><td>Amazon DVD Price</td><td>1.307***(0.063)</td></tr><tr><td>BN DVD Sales Rank</td><td>0.037***(0.006)</td></tr><tr><td>BN DVD Price</td><td>0.004(0.041)</td></tr><tr><td>Days Since DVD Release</td><td>0.007***(0.001)</td></tr><tr><td>Days Since Release × Digital Purchase</td><td>0.0002†(0.0001)</td></tr><tr><td>Days Since Release × Digital Rental</td><td>-0.0002**(0.0001)</td></tr><tr><td>In Stock</td><td>-0.003(0.057)</td></tr><tr><td>Amazon Avg. Rating</td><td>0.309†(0.159)</td></tr><tr><td>Amazon # Reviews</td><td>-0.230†(0.123)</td></tr><tr><td>BN Avg. Rating</td><td>0.041(0.209)</td></tr><tr><td>BN # Reviews</td><td>0.341(0.223)</td></tr><tr><td>Constant</td><td>-2.811***(0.794)</td></tr><tr><td>Observations</td><td>28,776</td></tr><tr><td>Movies</td><td>872</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.902</td></tr></table>

Robust standard errors are in parentheses and are clustered by Movie.  
Regression model includes fixed effects for Movie and Date.  
\*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, † p < 0.10.

In Table 4, we introduce an interaction effect between digital format availability and the days since release of the DVD. We observe a statistically significant interaction between the digital rental availability and the release date of the DVD movie. The result suggests it would take 2,000 days for the interaction effect to make up for the potentially harmful effect on DVD sales rank estimated by the existence of the digital rental availability (i.e., 0.400 / -0.0002). Note, the analysis assumes that the movie producer and/or electronic commerce platform does not wish to observe a cannibalization effect between the DVD movie and the digital rental format. Given that assumption, the analysis provides some insight into the optimal release window of the digital rental format.

## 5 Additional Analyses and Robustness Checks

Now that we have documented the main findings that digital rentals cannibalize physical movie sales, we next perform additional analyses to explain why this may be representative of reality. First, we present split-sample analyses that tease apart the potential drivers of movie consumption. The split-sample analyses focus on 1) price, 2) popularity, and 3) consumer signals of quality. Following that, we provide robustness checks for potential bias due to endogeneity, a discussion of multicollinearity in the data, and concluding with alternative explanations for the digital format results. All the results presented in the subsections that follow support the overall findings presented in Section 4.

## 5.1 Split-Sample Analyses

## 5.1.1 Discount Rate and Price Difference

We implement two pricing approaches for both digital formats to provide insight into how price drives cannibalization. For the first approach, we compute a discount rate for the price of the digital format in comparison to the DVD. To do so we subtract the digital purchase price from the DVD price and divide the result by the DVD price. We also do this for the rental format by subtracting the digital rental price from the DVD price, and then divide the result by the DVD price. The second pricing approach is simply the difference between the DVD price and the digital purchase price. We calculate the difference between the DVD price and the digital rental price as well. Dummy variables are then assigned values according to the mean value for each pricing approach. For example, if a particular digital rental has a discount rate higher than the mean discount rate for all digital rentals, we assign a one to Digital Rental High, and a zero otherwise. We then analyze our data by substituting the new dummy variables representing the pricing approach for the digital purchase and rental dummies used in the results presented earlier.

Table 5: Effect of Digital Format Pricing Approaches on Physical DVD Sales

<table><tr><td>DV: Amazon DVD Sales Rank</td><td>(1)</td><td>(2)</td></tr><tr><td>Digital Purchase High Discount Rate</td><td>-0.046(0.058)</td><td></td></tr><tr><td>Digital Rental High Discount Rate</td><td>0.145†(0.081)</td><td></td></tr><tr><td>Digital Purchase High Price Difference</td><td></td><td>-0.057(0.069)</td></tr><tr><td>Digital Rental High Price Difference</td><td></td><td>0.214*</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td></td><td></td><td>(0.098)</td></tr><tr><td>Amazon DVD Price</td><td>1.102***</td><td>1.060***</td></tr><tr><td></td><td>(0.177)</td><td>(0.178)</td></tr><tr><td>BN DVD Sales Rank</td><td>0.051*</td><td>0.050*</td></tr><tr><td></td><td>(0.021)</td><td>(0.021)</td></tr><tr><td>BN DVD Price</td><td>0.201†</td><td>0.212†</td></tr><tr><td></td><td>(0.119)</td><td>(0.119)</td></tr><tr><td>Days Since DVD Release</td><td>0.011***</td><td>0.011***</td></tr><tr><td></td><td>(0.002)</td><td>(0.002)</td></tr><tr><td>In Stock</td><td>-0.432†</td><td>-0.448†</td></tr><tr><td></td><td>(0.261)</td><td>(0.260)</td></tr><tr><td>Amazon Avg. Rating</td><td>0.545</td><td>0.566</td></tr><tr><td></td><td>(1.735)</td><td>(1.728)</td></tr><tr><td>Amazon # Reviews</td><td>-0.355***</td><td>-0.352***</td></tr><tr><td></td><td>(0.053)</td><td>(0.053)</td></tr><tr><td>BN Avg. Rating</td><td>1.146***</td><td>1.154***</td></tr><tr><td></td><td>(0.274)</td><td>(0.276)</td></tr><tr><td>BN # Reviews</td><td>-0.148</td><td>-0.161</td></tr><tr><td></td><td>(0.337)</td><td>(0.337)</td></tr><tr><td>Constant</td><td>-5.619†</td><td>-5.663†</td></tr><tr><td></td><td>(3.230)</td><td>(3.212)</td></tr><tr><td>Observations</td><td>4,958</td><td>4,958</td></tr><tr><td>Movies</td><td>165</td><td>165</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.916</td><td>0.917</td></tr></table>

Robust standard errors are in parentheses and are clustered by Movie.  
Regression model includes fixed effects for Movie and Date.  
\*\*\* $p < 0 . 0 0 1$ , \*\* p < 0.01, \* p < 0.05, † p < 0.10.

Our comparative pricing results are presented in Table 5. We can see in Column (1) that digital significant effect on DVD sales $( 0 . 1 4 5 , p \mathrm { - v a l u e = 0 . 0 7 ) }$ . In contrast, we do not observe a significant effect for digital purchases with a high discount rate. Consistent with the results for discount rate, only the high digital rental price difference compared to the mean price difference is statistically significant (0.214, pvalue < 0.05) in Column (2). Overall, the results echo the results presented earlier. The digital rental format appears to cannibalize physical DVD sales, especially if there is a high discount (or difference) in price compared to the DVD counterpart. The results also provide insight into the pricing strategies for the digital rental products. Both measures show that a greater relative bargain for the consumer results in greater cannibalization of the physical product.

## 5.1.2 Movie Popularity

Next, we determine if movie popularity has a role in the potential for cannibalization of DVD sales by the

# ACCEPTED MANUSCRIPT

digital formats. We examine two criteria for determining if a sample of movies should be classified as popular or niche. The first criterion is DVD sales rank as that is the clearest measure of movie popularity on Amazon's website. The second criterion is the age of the movie since the DVD release date, as exogenous press and other promotion efforts can be expected to drive popularity when a movie is newly released. To calculate each of these measures, we split the sample on the mean for the DVD sales rank (shown by Columns 1 and 3), and the mean for the days since DVD release (shown by Columns 2 and 4), and conduct the analyses on the resulting unbalanced panels for each measure accordingly (e.g., a movie can be popular on one day and unpopular on the next, resulting in an unbalanced panel).

The results presented in Table 6 are largely consistent with our prior findings. Top-selling movies in Column (1) show that the presence of the digital rental format is positive and statistically significant (0.308, p-value < 0.05). Newly released movies present a consistent result for digital rental (0.369, pvalue < 0.01) in Column (2). The story presented by these results is clear: DVD cannibalization is driven by new and popular movies that consumers will likely hav had little experience with (or access to others experience through reviews). A possible conjecture is that consumers are likely taking advantage of the low-risk sampling opportunity presented to them by the presence of the digital rental format. In contrast to Columns (1-2) of Table 6, Columns (3-4) represent movies that have a less popular sales rank and have been available on DVD for a (relatively) long time. We do not observe statistically significant results for either of the digital format dummies for the high sales rank movies (Column 3). However, in contrast to prior results, the analysis of older movies (Column 4) shows that the presence of the digital purchase format has a positive and statistically significant effect on DVD sales rank (0.127, p-value < 0.001) and the presence of the digital rental format has the opposite effect (-0.118, p-value < 0.001). The results suggest that consumers of niche movies may have experienced the movie before, or can at the very least derive a meaningful representation of the movie through the presence of the customer reviews. These movies are therefore not as likely to be sampled by consumers, and we thus do not observe cannibalization effects by the digital rental format for niche movies.

Table 6: Effect of Popular vs. Niche Movie Split-Samples on Physical DVD Sales

## ACCEPTED MANUSCRIPT

<table><tr><td>Sample Category</td><td colspan="2">Popular</td><td colspan="2">Niche</td></tr><tr><td>Sample Description</td><td>Low Sales Rank</td><td>Newer Release</td><td>High Sales Rank</td><td>Older Release</td></tr><tr><td>DV: Amazon DVD Sales Rank</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Digital Purchase</td><td>-0.366(0.259)</td><td>-0.254(0.158)</td><td>0.081(0.088)</td><td>0.127***(0.025)</td></tr><tr><td>Digital Rental</td><td>0.308*(0.133)</td><td>0.361**(0.114)</td><td>0.050(0.081)</td><td>-0.118***(0.020)</td></tr><tr><td>Amazon DVD Price</td><td>1.130***(0.074)</td><td>1.272***(0.069)</td><td>0.804***(0.064)</td><td>1.185***(0.112)</td></tr><tr><td>BN DVD Sales Rank</td><td>0.045***(0.009)</td><td>0.068***(0.008)</td><td>0.008†(0.005)</td><td>0.011(0.007)</td></tr><tr><td>BN DVD Price</td><td>-0.107†(0.059)</td><td>-0.217(0.050)</td><td>0.099*(0.042)</td><td>0.069(0.070)</td></tr><tr><td>Days Since DVD Release</td><td>0.007***(0.001)</td><td>0.002***(0.001)</td><td>0.005***(0.001)</td><td>0.003**(0.001)</td></tr><tr><td>In Stock</td><td>-0.076(0.076)</td><td>-0.050(0.078)</td><td>0.054(0.036)</td><td>0.139*(0.056)</td></tr><tr><td>Amazon Avg. Rating</td><td>0.134(0.101)</td><td>0.261†(0.147)</td><td>-0.098(0.098)</td><td>1.931(1.502)</td></tr><tr><td>Amazon # Reviews</td><td>-0.235*(0.098)</td><td>-0.277**(0.080)</td><td>0.124(0.114)</td><td>-0.003(0.155)</td></tr><tr><td>BN Avg. Rating</td><td>-0.032(0.208)</td><td>0.243(0.156)</td><td>-0.073(0.048)</td><td>-0.159*(0.074)</td></tr><tr><td>BN # Reviews</td><td>0.603*(0.302)</td><td>-0.111(0.087)</td><td>-0.003(0.115)</td><td>-0.040(0.185)</td></tr><tr><td>Constant</td><td>-2.418*(0.986)</td><td>4.213***(0.406)</td><td>1.139(0.748)</td><td>-4.695(3.215)</td></tr><tr><td>Observations</td><td>12,081</td><td>19,503</td><td>16,695</td><td>9,273</td></tr><tr><td>Movies</td><td>660</td><td>591</td><td>694</td><td>281</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.905</td><td>0.914</td><td>0.614</td><td>0.857</td></tr></table>

Robust standard errors are in parentheses and are clustered by Movie.  
Regression models include fixed effects for Movie and Date.  
\*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, † p < 0.10.

## 5.1.3 Customer Reviews

Customer reviews have important roles in affecting the product market (Dellarocas et al. 2010; Li and Hitt 2008; Zhu and Zhang 2010). The results presented in the prior sub-section implied a tendency for consumer sampling to encourage DVD movie cannibalization, therefore we should introduce a splitsample analysis based upon the number of customer reviews for each movie. The customer review approach is intuitive because a movie with fewer reviews should be a greater target for sampling as less information and experiences are available about the movie under consideration for consumption. To split the sample, we find the mean for the number of Amazon customer reviews across the entire sample, and conduct the analyses on the resulting unbalanced panels accordingly (e.g., the number of customer

reviews that a movie has may increase each day, resulting in an unbalanced panel). The results are presented in Table 7. Column (1) represents the movies that have few reviews and we observe a positive and significant result for the digital rental format (0.266, p-value < 0.05). We do not observe significant coefficients for digital rental or digital purchase in Column (2). The customer review split-sample analysis provides further evidence that cannibalization of DVD movie sales by digital rentals is prevalent for those movies where consumer experience is limited, and sampling is most likely to be pervasive.

Table 7: Effect of Customer Reviews Split-Sample on Physical DVD Sales

<table><tr><td>Sample Description</td><td>Few Reviews</td><td>Many Reviews</td></tr><tr><td>DV: Amazon DVD Sales Rank</td><td>(1)</td><td>(2)</td></tr><tr><td>Digital Purchase</td><td>-0.341(0.225)</td><td>0.142(0.121)</td></tr><tr><td>Digital Rental</td><td>0.266*(0.135)</td><td>0.008(0.117)</td></tr><tr><td>Amazon DVD Price</td><td>1.467***(0.113)</td><td>1.189***(0.065)</td></tr><tr><td>BN DVD Sales Rank</td><td>0.046***(0.011)</td><td>0.028***(0.006)</td></tr><tr><td>BN DVD Price</td><td>0.123(0.066)</td><td>-0.018(0.050)</td></tr><tr><td>Days Since DVD Release</td><td>0.007***(0.001)</td><td>0.005***(0.001)</td></tr><tr><td>In Stock</td><td>-0.118(0.106)</td><td>0.080(0.060)</td></tr><tr><td>Amazon Avg. Rating</td><td>-0.206(0.224)</td><td>0.056(1.489)</td></tr><tr><td>Amazon # Reviews</td><td>0.475†(0.264)</td><td>0.270(0.166)</td></tr><tr><td>BN Avg. Rating</td><td>-0.207(0.195)</td><td>-0.834†(0.500)</td></tr><tr><td>BN # Reviews</td><td>0.235(0.329)</td><td>0.202(0.150)</td></tr><tr><td>Constant</td><td>-2.328**(0.870)</td><td>-2.218(2.441)</td></tr><tr><td>Observations</td><td>12,909</td><td>15,867</td></tr><tr><td>Movies</td><td>400</td><td>491</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.890</td><td>0.907</td></tr></table>

Robust standard errors are in parentheses and are clustered by Movie.  
Regression models include fixed effects for Movie and Date.  
\*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, † p < 0.10.

## 5.2 Matched-Sample Analysis

Given that we have collected a secondary dataset and do not have access to primary data, it is impossible to know the exact motivations used for deciding if/when to release digital formats of physical movies. It is

# ACCEPTED MANUSCRIPT

also impossible to know why management may have chosen to offer a digital purchase format, a digital rental format, or both digital formats of a particular movie. So, there may be a potential endogeneity issue that we should consider because we do not have the information about the decisions to release a movie in a particular physical or digital format. In order to control for the potential endogeneity surrounding the release of the digital formats (beyond using time invariant movie fixed-effects and global time variant effects using date fixed-effects), we perform additional analyses using propensity score sample-matching.

In the analyses that follow, we carefully construct sample subsets based upon the observable characteristics of the movies in our complete dataset. Specifically, we consider the release of a particular movie in a particular digital format as a treatment effect, and match movies having similar characteristics to the “treated” movies to create the matched sample. In other words, we assume that the performance of similar movies would present similar information for management to consider when making the decision to release the movie in a particular physical or digital format. We use propensity score matching and the k-nearest neighbor random sample-matching approach to construct the matched samples (Caliendo and Kopeinig 2008; Rosenbaum and Rubin 1983; Rosenbaum and Rubin 1985), with each subset differentiated by the treatment variable already described (i.e., availability of digital purchase or digital rental), and also the value for the k parameter. 10

Because we have a panel dataset, we first have to create average values for each movie across the time dimension in our dataset, leaving us with 872 observations (i.e., one observation per movie). By collapsing the time dimension of the panel data and creating averages for each variable in the dataset, we can apply the k-nearest neighbor matching technique to create a matched sample. Once the movies in a matched sample are identified, we can then match those movies to the same movies in the full panel, thereby reestablishing the time dimension in the matched sample dataset.

Table 8: Comparison of Means for Non-Matched and Matched Samples (k = 10)

<table><tr><td>Treatment Variable</td><td colspan="3">Digital Purchase</td><td colspan="3">Digital Rental</td></tr><tr><td>Matching Variables</td><td>Treated</td><td>Non-Matched Control</td><td>Matched Control</td><td>Treated</td><td>Non-Matched Control</td><td>Matched Control</td></tr><tr><td>Amazon DVD Sales Rank</td><td>7.485</td><td>7.749*** (&lt;0.001)</td><td>7.470 (0.890)</td><td>7.494</td><td>7.726** (0.007)</td><td>7.459 (0.774)</td></tr><tr><td>Amazon DVD Price</td><td>2.629</td><td>2.645(0.630)</td><td>2.625(0.916)</td><td>2.662</td><td>2.634(0.445)</td><td>2.669(0.880)</td></tr><tr><td>BN DVD Sales Rank</td><td>8.119</td><td>8.159(0.673)</td><td>8.076(0.706)</td><td>8.200</td><td>8.133(0.506)</td><td>8.237(0.768)</td></tr><tr><td>BN DVD Price</td><td>2.847</td><td>2.868(0.556)</td><td>2.838(0.817)</td><td>2.944</td><td>2.839**(0.007)</td><td>2.965(0.661)</td></tr><tr><td>Days Since DVD Release</td><td>872.74</td><td>967.45(0.210)</td><td>900.13(0.756)</td><td>889.17</td><td>955.39(0.419)</td><td>902.47(0.901)</td></tr><tr><td>In Stock</td><td>0.985</td><td>0.979(0.376)</td><td>0.984(0.863)</td><td>0.984</td><td>0.980(0.596)</td><td>0.972(0.284)</td></tr><tr><td>Amazon Avg. Rating</td><td>1.587</td><td>1.627***(&lt;0.001)</td><td>1.604(0.203)</td><td>1.578</td><td>1.627***(&lt;0.001)</td><td>1.598(0.202)</td></tr><tr><td>Amazon # Reviews</td><td>4.731</td><td>4.469**(0.005)</td><td>4.857(0.229)</td><td>4.602</td><td>4.526(0.450)</td><td>4.654(0.667)</td></tr><tr><td>BN Avg. Rating</td><td>1.415</td><td>1.221***(&lt;0.001)</td><td>1.467(0.324)</td><td>1.385</td><td>1.245*(0.018)</td><td>1.407(0.736)</td></tr><tr><td>BN # Reviews</td><td>1.591</td><td>1.325**(0.002)</td><td>1.695(0.283)</td><td>1.498</td><td>1.372(0.166)</td><td>1.536(0.722)</td></tr><tr><td>Observations</td><td>246</td><td>626</td><td>567</td><td>193</td><td>679</td><td>588</td></tr></table>

The numbers in parentheses are p-values for t-tests comparing the means of the non-matched and matched samples to the treated sample. A non-statistically significant p-value suggests that the means are the same. \*\*\* $p < 0 . 0 0 1 , ^ { * * } p < 0 . 0 1 , ^ { * } p < 0 . 0 5 , \dag p < 0 . 1 0 .$

Table 8 presents the comparisons of the mean values for the variables used for matching, organized by treatment (i.e., “treated” indicates the movie was available as a digital purchase format or a digital rental format) where k = 10. If we compare the averages in the “Treated” columns to the “Non-Matched Control” columns, we can see there are some significant differences in means (e.g., Amazon DVD Sales Rank, and others). However, after we create the matched sample and compare the mean values of the observed variables, it is clear that the means are statistically identical for the “Treated” and “Matched Control” columns. Comparisons of matched samples for k = 1 (with or without replacement) and k = 5 are also qualitatively similar to k = 10 but are omitted for sake of brevity. Note, movies in the control group were never available during the sample period in a digital purchase or digital rental format. Given the results, we are confident that the observations in the matched samples are statistically identical to the observations in the treated samples, and we can replicate the analysis presented in Section 4.2.

Table 9: Effect of Digital Formats on Physical DVD Sales Using Matched Samples

<table><tr><td>Treatment Variable</td><td colspan="3">Digital Purchase</td><td colspan="3">Digital Rental</td></tr><tr><td>DV: Amazon DVD Sales Rank</td><td>k = 1(1)</td><td>k = 5(2)</td><td>k = 10(3)</td><td>k = 1(4)</td><td>k = 5(5)</td><td>k = 10(6)</td></tr><tr><td>Digital Purchase</td><td>-0.216(0.174)</td><td>-0.229(0.181)</td><td>-0.229(0.180)</td><td>-0.055(0.122)</td><td>-0.063(0.105)</td><td>-0.228(0.179)</td></tr><tr><td>Digital Rental</td><td>0.310**</td><td>0.319**</td><td>0.318**</td><td>0.227*</td><td>0.236*</td><td>0.319**</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td></td><td>(0.114)</td><td>(0.118)</td><td>(0.117)</td><td>(0.099)</td><td>(0.095)</td><td>(0.117)</td></tr><tr><td rowspan="2">Amazon DVD Price</td><td>1.159***</td><td>1.258***</td><td>1.297***</td><td>1.204***</td><td>1.233***</td><td>1.251***</td></tr><tr><td>(0.079)</td><td>(0.066)</td><td>(0.065)</td><td>(0.093)</td><td>(0.065)</td><td>(0.060)</td></tr><tr><td rowspan="2">BN DVD Sales Rank</td><td>0.044***</td><td>0.039***</td><td>0.038***</td><td>0.047***</td><td>0.040***</td><td>0.038***</td></tr><tr><td>(0.009)</td><td>(0.006)</td><td>(0.006)</td><td>(0.011)</td><td>(0.007)</td><td>(0.006)</td></tr><tr><td rowspan="2">BN DVD Price</td><td>0.032</td><td>0.004</td><td>-0.017</td><td>0.051</td><td>0.021</td><td>-0.004</td></tr><tr><td>(0.060)</td><td>(0.044)</td><td>(0.042)</td><td>(0.080)</td><td>(0.052)</td><td>(0.044)</td></tr><tr><td rowspan="2">Days Since DVD Release</td><td>0.008***</td><td>0.007***</td><td>0.007***</td><td>0.009***</td><td>0.007***</td><td>0.007***</td></tr><tr><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td></tr><tr><td rowspan="2">In Stock</td><td>-0.143</td><td>0.001</td><td>-0.005</td><td>-0.053</td><td>-0.021</td><td>-0.031</td></tr><tr><td>(0.095)</td><td>(0.063)</td><td>(0.059)</td><td>(0.090)</td><td>(0.062)</td><td>(0.063)</td></tr><tr><td rowspan="2">Amazon Avg. Rating</td><td>0.386*</td><td>0.338*</td><td>0.311†</td><td>0.442*</td><td>0.332*</td><td>0.309†</td></tr><tr><td>(0.177)</td><td>(0.164)</td><td>(0.161)</td><td>(0.220)</td><td>(0.154)</td><td>(0.158)</td></tr><tr><td rowspan="2">Amazon # Reviews</td><td>-0.277*</td><td>-0.266*</td><td>-0.229†</td><td>-0.319**</td><td>-0.263*</td><td>-0.238*</td></tr><tr><td>(0.114)</td><td>(0.127)</td><td>(0.124)</td><td>(0.099)</td><td>(0.111)</td><td>(0.119)</td></tr><tr><td rowspan="2">BN Avg. Rating</td><td>-0.019</td><td>-0.030</td><td>0.037</td><td>0.457*</td><td>0.412*</td><td>0.032</td></tr><tr><td>(0.231)</td><td>(0.214)</td><td>(0.210)</td><td>(0.206)</td><td>(0.202)</td><td>(0.212)</td></tr><tr><td rowspan="2">BN # Reviews</td><td>0.518†</td><td>0.487†</td><td>0.342</td><td>0.312</td><td>0.345</td><td>0.371</td></tr><tr><td>(0.293)</td><td>(0.249)</td><td>(0.225)</td><td>(0.274)</td><td>(0.220)</td><td>(0.229)</td></tr><tr><td rowspan="2">Constant</td><td>-3.206**</td><td>-2.573**</td><td>-2.619**</td><td>-4.421***</td><td>-3.121***</td><td>-2.618**</td></tr><tr><td>(1.074)</td><td>(0.868)</td><td>(0.824)</td><td>(1.153)</td><td>(0.859)</td><td>(0.817)</td></tr><tr><td>Observations</td><td>14,058</td><td>24,090</td><td>26,829</td><td>11,319</td><td>21,252</td><td>25,773</td></tr><tr><td>Movies</td><td>426</td><td>730</td><td>813</td><td>343</td><td>644</td><td>781</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.915</td><td>0.907</td><td>0.904</td><td>0.919</td><td>0.913</td><td>0.907</td></tr></table>

Robust standard errors are in parentheses and are clustered by Movie.  
Regression models include fixed effects for Movie and Date.  
\*\*\* $p < 0 . 0 0 1$ , \*\* p < 0.01, \* p < 0.05, † p < 0.10.

The results of the sample-matched fixed effects regressions are presented in Table 9. Columns (1- 3) are consider the digital purchase format “treatment” and Columns (4-6) are consider the digital rental format “treatment”. The columns and analyses also differ by the value used for the k parameter to conduct the sample matching. Our results are quite similar to the results found in the regressions in Section 4.2. The digital rental format remains positive and statistically significant in each of the regressions. The digital purchase format remains negative and not statistically significant, consistent with results presented earlier. The results of each of the propensity score matched regressions compare quite similarly to nonmatched results (i.e., recall in Table 2, Column 3, digital rental coefficient of 0.319, p-value < 0.01) and reinforce our belief that our data do not suffer from a significant bias due to potential endogeneity. Further, the use of sample-matching to create treated and non-treated groups provides some justification for causal inference (Dehejia and Wahba 2002) between the introduction of the rental format and the decline of physical sales.

# ACCEPTED MANUSCRIPT

## 5.3 Presence of Multicollinearity

Another possible concern that arises from our results is the potential for multicollinearity resulting from the two digital format dummy variables, as presented in the correlation matrix in Table 10. It may be reasonable to expect because there are many movies that are available in both digital formats at the same time, the potential for high correlation between these dummies would be prevalent. However, we do not believe that the presence of multicollinearity is harming the results in our study. Further, if we leave out one of the dummies in our analysis then we are subjecting our model to an obvious omitted-variable bias.

Regardless of potential concerns related to multicollinearity, the results are robust dropping one of the digital format dummies from our analysis. That is, the sign and the significance level does not change for the digital rental dummy, and the digital purchase dummy continues to have no significant statistical effect on the dependent variable. Further, a lack of substantial problems due to multicollinearity is reinforced by the results presented in Section 4.3 regarding the use of digital format ranks instead of dummy variables. The results presented there are consistent with the dummy variable approach. In sum, the inclusion of both dummy variables in our analysis avoids a clear omitted-variable bias issue. Further, any potential bias in the standard errors introduced by the presence of multicollinearity would only make it more difficult to find statistical significance, providing additional confidence in our results.

Table 10: Correlation Matrix

<table><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td></tr><tr><td>(1) Amazon DVD Sales Rank</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2) Digital Purchase</td><td>-.091</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3) Digital Rental</td><td>-.065</td><td>.649</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(4) Amazon DVD Price</td><td>-.072</td><td>-.015</td><td>.022</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(5) BN DVD Sales Rank</td><td>.440</td><td>-.003</td><td>.023</td><td>.025</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(6) BN DVD Price</td><td>-.125</td><td>-.019</td><td>.085</td><td>.865</td><td>.228</td><td>-</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(7) In Stock</td><td>.110</td><td>.039</td><td>.014</td><td>.038</td><td>-.005</td><td>-.016</td><td>-</td><td></td><td></td><td></td><td></td></tr><tr><td>(8) Days Since DVD Release</td><td>.089</td><td>-.035</td><td>-.010</td><td>-.384</td><td>-.053</td><td>-.407</td><td>.016</td><td>-</td><td></td><td></td><td></td></tr><tr><td>(9) Amazon Avg. Rating</td><td>-.093</td><td>-.111</td><td>-.110</td><td>.017</td><td>-.138</td><td>-.009</td><td>-.006</td><td>.182</td><td>-</td><td></td><td></td></tr><tr><td>(10) Amazon # Reviews</td><td>-.302</td><td>.104</td><td>.043</td><td>-.145</td><td>-.190</td><td>-.149</td><td>.060</td><td>.311</td><td>.151</td><td>-</td><td></td></tr><tr><td>(11) BN Avg. Rating</td><td>-.192</td><td>.131</td><td>.088</td><td>-.165</td><td>-.148</td><td>-.171</td><td>.010</td><td>.250</td><td>.039</td><td>.558</td><td>-</td></tr><tr><td>(12) BN # Reviews</td><td>-.269</td><td>.113</td><td>.058</td><td>-.137</td><td>-.197</td><td>-.154</td><td>.005</td><td>.259</td><td>.014</td><td>.706</td><td>.700</td></tr></table>

## 5.4 Falsification Test and Explanation for Lack of Digital Purchase Cannibalization

All the analyses until now have focused on the impacts of digital purchase and digital rental formats on

Amazon’s physical DVD sales. Results have consistently suggested a significant cannibalization effect between digital rentals and physical DVD sales, but no evidence of cannibalization from digital purchases. Interestingly, the digital rental format only exists as a method of consumption on Amazon’s website but it is not available from Barnes and Noble. So, there should be no effect of the digital rental format availability at Amazon on the sales of DVDs at Barnes and Noble, giving us the opportunity to perform a falsification test. Table 11 presents two-way fixed effects regressions using Barnes and Noble DVD sales rank as the dependent variable. Column (1) includes control variables that are specific only to Barnes and Noble, whereas Column (2) includes all control variables.

As shown by the results, the control variables behave consistent with our results presented earlier. When the BN DVD price increases, the DVD sales rank worsens. Older movies and those with many reviews are associated with worse DVD sales ranks. Movies with high ratings are associated with better DVD sales ranks. As regards the digital rental format that is available at Amazon only, we do not observe any effect. That is, the BN DVD sales rank is not significantly affected when there is a digital rental format available at Amazon. However, we do observe evidence of a statistically significant effect of the digital purchase format in Column (1) on BN DVD sales (-0.327, p-value < 0.05), as well the Column (2) full model (-0.297, p-value = 0.052). The negative coefficient is consistent with the same digital purchase variable noted in Table 2.

Table 11: Effect of Amazon Digital Formats on Barnes and Noble Physical DVD Sales

<table><tr><td>DV: BN DVD Sales Rank</td><td>No Amazon (1)</td><td>Full Model (2)</td></tr><tr><td rowspan="2">Digital Purchase</td><td>-0.327*</td><td>-0.297†</td></tr><tr><td>(0.162)</td><td>(0.153)</td></tr><tr><td rowspan="2">Digital Rental</td><td>0.168</td><td>0.161</td></tr><tr><td>(0.111)</td><td>(0.103)</td></tr><tr><td rowspan="2">Amazon DVD Price</td><td></td><td>-0.176†</td></tr><tr><td></td><td>(0.094)</td></tr><tr><td rowspan="2">Amazon DVD Sales Rank</td><td></td><td>0.138***</td></tr><tr><td></td><td>(0.020)</td></tr><tr><td rowspan="2">BN DVD Price</td><td>3.639***</td><td>3.624***</td></tr><tr><td>(0.147)</td><td>(0.146)</td></tr><tr><td rowspan="2">Days Since DVD Release</td><td>0.011***</td><td>0.010***</td></tr><tr><td>(0.001)</td><td>(0.001)</td></tr><tr><td rowspan="2">In Stock</td><td></td><td>0.073</td></tr><tr><td></td><td>(0.084)</td></tr><tr><td>Amazon Avg. Rating</td><td></td><td>0.046</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td></td><td></td><td>(0.140)</td></tr><tr><td>Amazon # Reviews</td><td></td><td>-0.260**</td></tr><tr><td></td><td></td><td>(0.088)</td></tr><tr><td>BN Avg. Rating</td><td>-0.390**</td><td>-0.320*</td></tr><tr><td></td><td>(0.150)</td><td>(0.138)</td></tr><tr><td>BN # Reviews</td><td>0.479*</td><td>0.449†</td></tr><tr><td></td><td>(0.244)</td><td>(0.238)</td></tr><tr><td>Constant</td><td>-12.338**</td><td>-11.631***</td></tr><tr><td></td><td>(1.349)</td><td>(1.372)</td></tr><tr><td>Observations</td><td>28,776</td><td>28,776</td></tr><tr><td>Movies</td><td>872</td><td>872</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.783</td><td>0.784</td></tr></table>

Robust standard errors are in parentheses and are clustered by Movie.  
Regression model includes fixed effects for Movie and Date.  
\*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, † p < 0.10.

There is a reasonable falsification test explaining the lack of effect of the digital rental format on BN DVD sales. Consider the following key fact regarding shopping at Amazon and BN websites as of our data collection window. BN does not offer a digital rental format. Assuming low search costs and the ability to find the movie at a competing website such as Amazon, it is reasonable that a shopper at BN is interested in ownership and therefore in the market to purchase a movie (or not consume at all). Accordingly, the shopper at BN would not be interested in a rental and thus there is no significant crossshopping effect of the digital rental format on BN DVD sales.

Conversely, there is a significant relationship between the Amazon digital purchase format and BN DVD sales. There are many potential reasons that could explain this relationship. As with the previous argument, the BN shopper is interested in ownership and, assuming low search costs, is also cross-shopping ownership options on the competing website. As suggested by the lack of result for the digital purchase format on Amazon DVD sales (Table 2), there must be considerations about ownership of the digital purchase format that preclude consumers from making a purchase. A reasonable and likely concern is the so-called “content trap”, where ownership of digital content is constrained to a particular platform or technology (Sullivan 2013). Further, BN offers fewer options of consumption for their shoppers (e.g., no interest in rental, no BN secondary market), so the effect of the undesirable digital purchase format becomes magnified, as evidenced by our results.

## 6 Discussion and Conclusion

The delivery of physical experience goods using a digital medium impacts existing traditional physical goods—such as DVD movies—in ways that are not completely understood. That is, multi-channel opportunities for consumption of physical and digital alternatives of movies presents us with a new technology-enabled phenomenon. Prior work has primarily focused on the cannibalization of sales of information goods where usual consumption of the good is by purchase only (e.g., music, books). We extend the prior work by also considering the effects on the purchase of the physical good from renting a digitally-distributed movie and consuming it as a limited-term experience good.

To conduct our study, we observe movie data from Amazon and Barnes and Noble for each movie on each day of data collection. We find that the availability of a digital rental version of a physical DVD is associated with a significant decrease in the sales of the DVD. In contrast, we do not find a significant effect on the DVD for the presence of a digital purchase version of a movie. We also conduct several robustness tests to further our understanding of why see these effects. Our results show that popular and newly released movies show a cannibalization effect from the digital rental format, as well as new movies that do not have many consumer reviews. These results contribute to the existing literature by showing that the lack of “experience” derived from consumer reviews would lead a consumer to prefer the rental option rather than a full purchase. Of further support, our results also provide some insight into pricing rentals and purchases, as movies that have a high discount rate (i.e., digital rentals are inexpensive in contrast with the DVD purchase), result in greater cannibalization of the physical DVD by the digital rental. We address potential concerns regarding endogeneity by our econometric approach implemented, as well as a robustness test using propensity score matching to create a matched sample analysis. We also conduct a falsification test to explore alternative explanations for our results.

Regarding practical insights of our work, it has been shown that digital media distribution products can reach maturity within several years of product launch (Stone 2008), and the impacts from our results must be considered—especially in conjunction with appropriate pricing and release window models—to maximize outcomes. In addition, although these types of services were initially met with criticism from some consumers and movie industry executives (Ouchi 2006), it appears that some

consumers want both types of purchase formats (Carr 2011), whereas others prefer to stream a rental copy of the movie. Regarding purchases, some consumers prefer to stream purchased content, whereas others prefer to collect the physical copies of the movie, and we have provided some evidence that these two purchase formats do not appear to be significantly encroaching on each other.

As with all research, our study is not without limitations. Our paper uses data that were collected prior to the implementation of subscription-based models. However, as mentioned earlier, our data are free of messy confounding issues that may arise from the existence of subscription platforms. We also suggest that a decision support system would greatly improve the ability for management to determine if and when movies should be released on the various formats and platforms that are available. Lastly, we only observe pricing and movie format release decisions and cannot explicitly capture the decisions made by management. Experimentation, whether natural or field, would be useful in addressing this limitation.

Funding: This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## References

Aguiar, L., and Waldfogel, J. 2015. “Streaming Reaches Flood Stage: Does Spotify Stimulate or Depress Music Sales?” NBER Working Paper 21653, 1-34.

Ansari, A., Mela,C.F., and Neslin, S.A. 2008. “Customer Channel Migration,” Journal of Marketing Research (45:1), 60–76.

August, T., Dao, D., and Shin, H. 2015. “Optimal Timing of Sequential Distribution: The Impact of Congestion Externalities and Day-and-Date Strategies,” Marketing Science (34:5), 755-774.

Bhattacharjee, S., Gopal, R.D., Marsden, J. R., and Sankaranarayanan, R. 2011. “Digital Goods and Markets: Emerging Issues and Challenges,” ACM Trans. on Management Information Systems (2:2).

Brynjolfsson, E., Hu, Y., and Rahman, M.S. 2013. “Competing in the Age of Omnichannel Retailing,” MIT Sloan Management Review (54:4), 23-29.

Brynjolfsson, E., Hu, Y., and Rahman, M.S. 2009. “Battle of the Retail Channels: How Product Selection

and Geography Drive Cross-Channel Competition,” Management Science (55:11), 1755-1765.

Brynjolfsson, E., Hu, Y., and Simester, D. 2011. “Goodbye Pareto Principle, Hello Long Tail: The Effect of Search Costs on the Concentration of Product Sales,” Management Science (57:8), 1373-1386.

Brynjolfsson, E., Hu, Y., and Smith, M. D. 2003. “Consumer surplus in the digital economy: Estimating the value of increased product variety at Online booksellers,” Management Sci. (49:11) 1580-1596.

Caliendo, M., and Kopeinig, S. 2008. “Some practical guidance for the implementation of propensity score matching,” Journal of Economic Surveys (22:1) Feb, 31-72.

Carr, A. 2011. “Is Streaming Video Cannibalizing Amazon's DVD Sales?” in: Fast Company, June 6, 2011 (http://www.fastcompany.com/1757702/streaming-video-cannibalizing-amazons-dvd-sales).

Chevalier, J., and Goolsbee, A. 2003. “Measuring Prices and Price Competition Online: Amazon.com and BarnesandNoble.com,” Quantitative Marketing and Economics (1:2), 203-222.

Chevalier, J. A., and Mayzlin, D. 2006. “The effect of word of mouth on sales: Online book reviews,” Journal of Marketing Research (43:3) 345-354.

Court, D., Elzinga, D., Mulder, S., and Vetvik., O. J. 2009. “The Consumer Decision Journey,” McKinsey Quarterly, 3, 96-107.

Danaher, B., Dhanasobhon, S., Smith, M. D., and Telang, R. 2010. “Converting Pirates Without Cannibalizing Purchasers: The Impact of Digital Distribution on Physical Sales and Internet Piracy,” Marketing Science (29:6), 1138-1151.

Dehejia, R. H., and Wahba, S. 2002. “Propensity Score-Matching Methods for Nonexperimental Causal Studies,” The Review of Economics and Statistics (84:1), 151-161.

Deleersnyder, B., Geyskens., I., Gielens, K., and Dekinmpe, M. G. 2002. “How Cannibalistic is the Internet Channel? A Study of the Newspaper Industry in the United Kingdom and The Netherlands,” International Journal of Research in Marketing 19, 337-348.

Dellarocas, C., Gao, G., and Narayan, R. 2010. “Are Consumers More Likely to Contribute Online Reviews for Hit or Niche Products?,” Journal of Management Information Systems (27:2), 127-157.

in Practice, Current Research, and New Research Directions,” Marketing Science (25:6), 638-661. Flacy, M. 2015. “Battle of the Streaming Giants: Which streaming service is best for you?” Digital Trends, March 1 (http://www.digitaltrends.com/home-theater/netflix-hulu-plus-amazon-instantvideo/).

Garg, R. and Telang, R. 2013. “Inferring App Demand from Publicly Available Data,” MIS Quarterly (37:4), 1253-1264.

Gensler, S., Leeflang, P., and Skiera, B. 2012. “Impact of Onlien Channel Use on Customer Revenues and Costs to Serve: Considering Product Portfolios and Self-Selection,” International Journal of Research in Marketing 29, 192-201.

Ghose, A., Smith, M. D., and Telang, R. 2006. “Internet Exchanges for Used Books: An Empirical

Gong, J., Smith, M. D., and Telang, R. 2015. “Substitution of Promotion? The Impact of Price Discounts on Cross-Channel Sales of Digital Movies,” Journal of Retailing (91:2), 343-357.

Gupta, A., Su., B., and Walter, Z. 2004. “An Empirical Study of Consumer Switching from Traditional to Electronic Channels: A Purchase-Decision Process Perspective,” International Journal of Electronic Commerce (8:3), 131-161.

Harris, R. D. F., and Tzavalis, E. 1999. “Inference for unit roots in dynamic panels where the time dimension is fixed,” Journal of Econometrics (91:2), 201-226.

Hennig-Thurau, T., Henning, V., Sattler, H., Eggers, F., and Houston, M. B. 2007. “The Last Picture Show? Timing and Order of Movie Distribution Channels,” Journal of Marketing 71, 63-83.

Homburg, C., Vollmayr, J., and Hahn, A. 2014. “Firm Value Creation Through Major Channel Expansions: Evidence from an Event Study in the United States, Germany, and China,” Journal of Marketing 78, 38-61.

Kannan, P. K., Pope, B. K., and Jain, S. 2009. “Practice Prize Winner Pricing Digital Content Product Lines: A Model and Application for the National Academies Press,” Marketing Sci. (28:4), 620-636.

Kezdi, G. 2004. “Robust Standard Error Estimation in Fixed-Effects Panel Models,” Hungarian

Statistical Review (9), 95-116.

Knox G. and Eliashberg, J. 2009. “The Consumer's Rent vs. Buy Decision in the Rentailer,” International Journal of Research in Marketing 26, 125-135.

Li, X. X. and Hitt, L. M. 2008. “Self-Selection and Information Role of Online Product Reviews,” Information Systems Research (19:4), 456-474.

Ma, L., Montgomery, A.L., Singh, P.V., and Smith, M.D. 2014. “An Empirical Analysis of the Impact of Pre-Release Movie Piracy on Box Office Revenue,” Information Systems Research (25:3), 590-603.

Moeller, S. and Wittkowski, K. 2010. “The Burdens of Ownership: Reasons for Preferring Renting,” Managing Service Quality (20:2), 176-191.

Morris, C. 2016. “Blu-Ray Struggles in the Streaming Age,” January 8 (available at

Mukherjee, A. and Kadiyali, V. 2011. “Modeling Multichannel Home Video Demand in the U.S. Motion Picture Industry,” Journal of Marketing Research 48, 985-995.

O'Reilly, T. 2002. “Jeff Bezo's Open Letter on Used Book Sales,” April 15 (available at http://www.oreillynet.com/lpt/wlg/1291).

Ouchi, M. S. 2006. “Amazon Listens to Unbox Beefs,” September 27 (available at

Petersen, M. A. 2009. “Estimating Standard Errors in Finance Panel Data Sets: Comparing Approaches,” Review of Financial Studies (22:1), 435-480.

Rosenbaum, P. R., and Rubin, D. B. 1983. “The Central Role of the Propensity Score in Observational Studies for Causal Effects,” Biometrika (70:1), 41-55.

Rosenbaum, P. R., and Rubin, D. B. 1985. “Constructing a Control Group Using Multivariate Matched Sampling Methods That Incorporate the Propensity Score,” The American Statistician (39:1), 33-38.

Shocker, A. D., Bayus, B. L., and Kim, N. 2004. “Product complements and substitutes in the real world: The relevance of “other products”,” Journal of Marketing (68:1), 28-40.

Smith, M. D., and Telang, R. 2009. “Competing with Free: The Impact of Movie Broadcasts on DVD

Sales and Internet Piracy,” MIS Quarterly (33:2), 321-338.

Stone, B. 2008. “Amazon Accelerates its Move to Digital,” April 7 (available at http://www.nytimes.com/2008/04/07/technology/07amazon.html).

Sullivan, D. 2013. “How trapped are your digital movies and TV shows?” January 31 (available at https://www.cnet.com/news/how-trapped-are-your-digital-movies-and-tv-shows/).

Varian. H. R. 2000. “Buying, Sharing and Renting Information Goods,” The Journal of Industrial Economics (48:4), 473-488.

Verhoef, P. C., Kannan, P.K., and Inman J. J. 2015. “From Multi-Channel Retailing to Omni-Channel Retailing: Intro. to the Special Issue on Multi-Channel Retailing,” J. of Retailing (91:2), 174-181.

Wooldridge, J. M. 2002. Econometric Analysis of Cross Section and Panel Data, (MIT Press: Cambridge.

Xu, J., Forman, C., Kim, J. B., and Van Ittersum, K. 2014. “News Media Channels: Complements or Substitutes? Evidence from Mobile Phone Usage,” Journal of Marketing 78, 97-112.

Yu, Y., Chen, H, Peng, C. H., and Chau, P. 2017. “The Causal Effect of Video Streaming on DVD Sales: Evidence from a Natural Experiment,” Working paper, 1-29.

Zhu, F., and Zhang, X. Q. 2010. “Impact of Online Consumer Reviews on Sales: The Moderating Role of Product and Consumer Characteristics,” Journal of Marketing (74:2), 133-148.

## Biographical Note

Uncovering the Effects of Digital Movie Format Availability on Physical Movie Sales

Corresponding Author Matthew J. Hashim mhashim@email.arizona.edu University of Arizona Department of MIS P.O. Box 210108 Tucson, AZ 85721

Matthew J. Hashim is an Assistant Professor of Management Information Systems at the Eller College of Management, University of Arizona. He received his Ph.D. in Management with a specialization in MIS from the Krannert School of Management, Purdue University. His research primarily uses experimental and behavioral economics to understand information security problems such as information privacy, digital piracy, password security, social engineering, and other security-related topics. His research has been published in premier journals such as Journal of Management Information Systems and Information Systems Research, and his research has been presented at major conferences and workshops.

Sudha Ram is the Anheuser-Busch Chair in MIS, Entrepreneurship, and Innovation, Professor of Management Information Systems, and Director of the INSITE Center for Business Intelligence and Analytics at the Eller College of Management, University of Arizona. She received her Ph.D. in Management Information Systems from the University of Illinois. Her research interests include Big Data Analytics and Enterprise Data Management, Web and Data Analytics, Large Scale Network Analysis and Data Mining, Social Media Analytics, and Semantic Interoperability among Heterogeneous Data Sources. Dr. Ram has extensively published her research at major journals and conferences such as MIS Quarterly, IEEE TKDE, Information Systems Research, IEEE Intelligent Systems, Marketing Science, Communications of the ACM, Information Systems, and other leading outlets.

Zhulei Tang is a Director of Analytics at Turner Broadcasting System, Inc. Dr. Tang is a seasoned analytics professional with broad experience in advanced analytics, big data, and quantitative research. She received her Ph.D. in Management Information Systems from the Tepper School of Business, Carnegie Mellon University. Her research specialties include: Big Data, Applied Statistical and Econometric Modeling, Advanced Analytics, Quantitative Marketing Research, Marketing Analytics, Predictive Analytics, Consumer Insights, Online Advertising, and Social Media. She has published her research in major journals such as Management Science, Journal of Management Information Systems, International Journal of Industrial Organization, and System Sciences.

# Uncovering the Effects of Digital Movie Format Availability on Physical Movie Sales

## Highlights

 Digital rentals significantly cannibalize sales of physical movies

 Digital purchases do not significantly cannibalize sales of physical movies

 Cannibalization is driven by new movies that have few reviews and large discounts

 Cannibalization diminishes after a physical movie has been released for 2,000 days
