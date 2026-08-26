---
otero_id: 3720
otero_key: "H7K3ZEMX"
title: "Inferring App Demand from Publicly Available Data"
authors: "Rajiv Garg; Rahul Telang"
year: "2012"
journal: "MIS Quarterly"
doi: "10.25300/misq/2013/37.4.12"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# INFERRING APP DEMAND FROM PUBLICLY AVAILABLE DATA<sup>1</sup>

Rajiv Garg McCombs School of Business, The University of Texas at Austin, Austin, TX 78712 U.S.A. {Rajiv.Garg@mccombs.utexas.edu}

Rahul Telang School of Information Systems & Management. H. John Heinz III College, Carnegie Mellon University, Pittsburgh PA 15213 U.S.A. {rtelang@andrew.cmu.edu}

With an abundance of products available online, many online retailers provide sales rankings to make it easier for consumers to find the best-selling products. Successfully implementing product rankings online was done a decade ago by Amazon, and more recently by Apple’s App Store. However, neither market provides actual download data, a very useful statistic for both practitioners and researchers. In the past, researchers developed various strategies that allowed them to infer demand from rank data. Almost all of that work is based on an experiment that shifts sales or collaboration with a vendor to get actual sales data. In this research, we present an innovative method to use public data to infer the rank–demand relationship for the paid apps on Apple’s iTunes App Store. We find that the top-ranked paid app for iPhone generates 150 times more downloads compared to the paid app ranked at 200. Similarly, the top paid app on iPad generates 120 times more downloads compared to the paid app ranked at 200. We conclude with a discussion on an extension of this framework to the Android platform, in-app purchases, and free apps.

Keywords: Mobile apps, app store, sales-rank calibration, app downloads, pareto distribution, Android, Apple iTunes, in-app purchase

## Introduction

The growth of mobile phones and smart phones over the last few years has been phenomenal. Based on recently published reports, there are about 106 million users of smart phones<sup>2</sup> in the United States. Globally, there are 1.1 billion active mobile subscriptions<sup>3</sup> with over 100,000 new smart phones being sold every quarter.<sup>4</sup> As more countries deploy high speed wireless networks, users are spending an increasing amount of time on their phones. A significant reason for this growth has been attributed to the availability of mobile phone applications (apps) that are becoming ubiquitous on all mobile operating systems. In April 2012, according to Appshopper. com, there were over 787,000 apps available for the iOS platform and 50 percent of mobile phone users used the downloaded applications. Similarly as of May 2011, the total number of apps available for the Android platform was approximately 200,000 (Barra 2011). Based on AdMob’s

2010 report,<sup>5</sup> smart phone users spend about 80 minutes per day on mobile applications.

Apple’s iPhone ushered an era where developers were able to sell their innovative applications to a large consumer base through the iTunes app store platform. These apps cover a wide variety of domains including games, location services, productivity, and healthcare. In 2011, Apple announced that more than 15 billion apps had been downloaded from its app store as of July 2011.<sup>6</sup>

Clearly, the app market has found favor with customers. Mobile apps attract end consumers and create diverse opportunities for additional revenue for app developers, device manufacturers, and cellular service providers. More importantly, as users start valuing these apps more and more, app stores have an opportunity to engender strong externality. Thus, these platforms lure developers, sometimes by providing deep subsidies, to write diverse applications for them. This has resulted in growth in the number of both large and small app publishing firms entering this highly dynamic market. This increase in diversity of developers results in greater variety of software applications available to consumers (Boudreau 2012). Based on recent statistics,<sup>7</sup> there are 500,000 apps approved for the iOS platform developed by over 85,000 app developers.

The growth of app market provides a great opportunity to examine important questions around software innovation, firm entry and exit strategy, software product pricing and promotion, platform leadership, and externality. However, our understanding of this market is limited due to lack of demand data. Similar to Amazon’s book market, Apple, Google, and Nokia do not provide sales information on any application. In fact, even the app developers get somewhat aggregated data from these platform owners. For example, Apple may not provide details on applications downloaded on the iPad and iPhone separately to a developer.<sup>8</sup> Additionally, app developers themselves are reluctant to share any details on demand for competitive reasons. Thus, most individuals have access to aggregate numbers or the rank data. For example, Apple’s App Store typically provides a list of the top 200 paid apps, top 200 free apps, or top 200 highest grossing apps. Unfortunately, having access to just an app’s rank is not useful because one cannot infer the value of an app placed at a given rank. For a developer, it is hard to determine whether the cost of moving up a few ranks by promotional activities is worth the benefits. Similarly, one cannot readily determine whether a particular niche in the app market is viable or how to set various marketing mix variables. Thus, having access to demand is highly beneficial to both practitioners and researchers.

Fortunately, researchers were able to infer demand from the rank data in the case of Amazon’s book sales (Brynjolfsson et al. 2003, 2010; Chevalier and Goolsbee 2003; Chevalier and Mayzlin 2006). In these papers, rank and sales are assumed to be related via the power law (or Pareto distribution) implying that a small number of products capture a large share of the market. The typical Pareto distribution that has been estimated in extant research is

$$
s a l e s = b \times (\operatorname{rank}) ^ {- a} + \varepsilon\tag{1}
$$

Where b is the scale parameter and a is the shape parameter.

To estimate the model parameters,we need both rank and sales information for app. Rank information is generally available through the publishers of those ranks. But to get demand data, researchers either conducted experiments or collaborated with publishers. Chevalier and Goolsbee (2003) conducted a creative experiment to infer demand. They selected low-selling books (for which the demand was known or assumed to be very small) and purchased large quantities (relative to already low demand) of each book on Amazon. As the ranks for the books changed, they could infer the relationship between the sales rank and experimented demand. The downside of this approach is that such experiments are practical only for very low-selling books. Therefore, inferring the relationship at the top ranks using this approach is not entirely accurate. In their study, Brynjolfsson et al. (2003) collaborated with a book publisher to get access to demand data to establish the sales and rank relationship. In both approaches, it is imperative to get access to demand data.

Table 1 summarizes the shape parameter values as estimated in prior studies. Notice that the shape parameter is decreasing in magnitude over time. The smaller value of a suggests a flatter curve (longer tail) for equation (1).

However, the most important aspect of calibrating this relationship is that it paves the way for other interesting work. For example, Ghose et al. (2006) estimated the elasticity of substitution between new and used goods. Ghose and Sundararajan (2006) used it to study the software security product marketplace. Brynjolfsson et al. (2003) and Anderson (2004)

<table><tr><td colspan="2">Table 1. Pareto Shape Parameters Estimated by Existing Literature</td></tr><tr><td>Source</td><td>Shape Parameter Estimate</td></tr><tr><td>Chevalier and Goolsbee (2003)Data Source: Poynter (2000)</td><td>1.199</td></tr><tr><td>Chevalier and Goolsbee (2003)Data Source: Weingarten (2001)</td><td>1.05</td></tr><tr><td>Chevalier and Goolsbee (2003)(Evidence from various experiments suggesting a value between 0.9 and 1.3)</td><td>1.2</td></tr><tr><td>Brynjolfsson et al. (2003)</td><td>0.871</td></tr><tr><td>Ghose et al. (2006)Data Source: Weingarten (2001)</td><td>0.952</td></tr><tr><td>Chevalier and Mayzlin (2006)</td><td>0.78</td></tr><tr><td>Brynjolfsson et al. (2010)</td><td>0.613</td></tr></table>

used this to establish the long-tail phenomenon on the Internet. One can also study the dynamics of demand over time. In summary, use of sales rank to compute actual sales or use in lieu of sales has become common in academic research because of the unavailability of actual sales data.

With the increasing popularity of mobile apps, we expect that many researchers will be studying the dynamics of this market. In this paper, we provide a methodology to link rank with actual downloads for mobile apps using publicly available data. While our method is similar to methods proposed in prior studies, it is different on a few key dimensions. First, to calibrate the relationship between rank and sales, the prior work needed access to demand data (either from an experiment or from a book publisher). Getting demand data is quite challenging, much more so in the App market, rendering this work quite difficult. In our paper, we calibrate mobile apps rank-sales relation using publicly available data alone. Access to any demand data is not needed at all. Second, many prior studies calibrated this relationship using books with very low rank/baseline sales. This has the potential to introduce prediction inaccuracies for top selling books. In our case, we are calibrating the relationship for top ranking apps. We believe we can provide more accurate estimates for the top selling apps (which sell disproportionally more).

In recent work, Carare (2012) examines how the past rank of an app influences future demand. Since demand data is unavailable, he provides a method that overcomes lack of demand data to estimate the parameters. In our paper, we provide a framework to infer demand from publicly available rank information. This direct measure of demand then allows for estimation of other variables of interest—for example, Carare’s method cannot recover price elasticity (see page 732).

In this paper, we will illustrate that one can calibrate the rank– sales relationship using publicly available data alone. Furthermore, to the best of our knowledge, this is the first study that tries to calibrate the relationship between app rank and sales for mobile platform. The next two sections discuss our estimation method and data. We then present our results and provide some validation to our method. In the final section, we provide evidence of robustness and generalizability and present our conclusions.

## Model

Our subject for inferring the demand will be Apple’s App Store. We will discuss Google’s Android store (recently renamed Google Play Store) in a later section. A key feature of app stores is that three different rank lists are publicly available: top-free applications, top-paid applications, and top-grossing applications. The top-free list shows the mostdownloaded applications that have no upfront purchase price. The top-paid list shows the most-downloaded applications that have a non-zero price. The top-grossing list ranks the applications based on revenue generation.

Like the extant literature, we assume a Pareto distribution for inferring downloads from rank. Assuming number of downloads of an application at rank $\mathrm { { r _ { p } } }$ in the top-paid list is given by $\mathrm { d } _ { \mathrm { r p } } ,$ the Pareto distribution could be written as

$$
d _ {r _ {p}} = b _ {p} \times r _ {p} ^ {- a _ {p}} \mid 1 \leq r _ {p} \leq 2 0 0\tag{2}
$$

Here ${ \tt b } _ { \mathrm { p } }$ defines the scale factor that is dependent on the total market size for iPad or iPhone apps, and ${ \bf { a } } _ { \mathrm { { p } } }$ defines the shape of the Pareto curve.

Similarly we define the Pareto distribution of apps in the topgrossing list where $\mathrm { \ p d } _ { \mathrm { r g } }$ is the revenue generated by the application at rank $\mathrm { { r _ { g } } }$ in the list. This revenue could also be written as the product of price (p) and number of downloads $\mathrm { ( d _ { \mathrm { { r p } } } ) }$ of the same application in the top-paid list. Thus we can write the distribution for the top-grossing apps as

$$
p d _ {r _ {g}} = p \times d _ {r _ {p}} = b _ {g} \times r _ {g} ^ {- a _ {g}}\tag{3}
$$

Equation (3) assumes that the top-grossing apps generate their revenues from the upfront pricing only. Additionally, both free and paid apps may include additional features inside the application that users may purchase. Thus, paid apps may generate some additional revenue that is not reflected in (3). However, in-app features are most common for free apps. For paid apps, the dominant source of revenue is still upfront prices. In the “Discussion” section, we will discuss how our method can be adapted to in-app purchase options.

In equation (2) and in equation (3), we know the values of p, $\Gamma _ { \mathrm { p } } ,$ and $\mathrm { { r _ { g } } }$ from publicly available data. The unknown parameters that we need to estimate are $\mathsf { b } _ { \mathrm { p } } , \mathsf { b } _ { \mathrm { g } } , \mathsf { a } _ { \mathrm { p } } , \mathsf { a } _ { \mathrm { g } }$ . We can rewrite (3) after taking logs as

$$
\log \left(r _ {g}\right) = \frac {1}{a _ {g}} \times \log \left(\frac {b _ {g}}{b _ {p}}\right) + \frac {a _ {p}}{a _ {g}} \times \log \left(r _ {p}\right) - \frac {1}{a _ {g}} \times \log (p)\tag{4}
$$

or

$$
\log \left(r _ {g}\right) = \beta_ {0} + \beta_ {1} \times \log \left(r _ {p}\right) + \beta_ {2} \times \log (p)\tag{5}
$$

where

$$
\mathrm{a} _ {g} = - 1 \times (1 / \beta_ {2})\tag{6}
$$

$$
\mathbf {a} _ {p} = - 1 \times (\beta_ {1} / \beta_ {2})\tag{7}
$$

$$
\left. \frac {b _ {g}}{b _ {p}} = \exp \left(- 1 \times \left(\beta_ {1} / \beta_ {2}\right)\right) \right.\tag{8}
$$

This could be estimated using a simple truncated ordinary least square regression. For readability purposes, we do not index $\boldsymbol { \mathrm { r } } _ { \mathrm { p } }$ and $\operatorname { d r } _ { \mathfrak { p } }$ for a given app i. In other words, rank and price information for an app (i) is treated as independent cross sectional data even if the same app appears multiple times.

Notice from (8) that we can only recover the ratio of scale parameters $( \mathsf { b } _ { \mathrm { g } } / \mathsf { b } _ { \mathrm { p } } )$ Estimating individual values of the scale parameters $( \mathsf { b } _ { \mathsf { p } }$ and b ) requires additional information. Since the information for actual downloads for an individual app is not readily available, we use aggregate downloads in a day to recover $( \mathsf { b } _ { \mathsf { p } }$ and $\mathbf { b _ { \mathrm { g } } } )$ . To see this, notice that if we know aggregate downloads (D ) then

$$
D _ {t} = \sum d _ {r _ {p}} = b _ {p} \sum_ {r = 1} ^ {N} r _ {p} ^ {- a _ {p}}
$$

Thus, with the knowledge of total number of downloads of top ranked apps we can recover ${ \sf b } _ { \mathrm { p } }$ and ${ \sf b } _ { \mathrm { g } }$ from the formula above as

$$
b _ {p} = \left(\sum_ {r _ {p} = 1} ^ {N} d _ {r _ {p}}\right) / \left(\sum_ {r _ {p} = 1} ^ {N} r _ {p} ^ {- a _ {p}}\right)\tag{9}
$$

$$
\begin{array}{l} b _ {g} = \exp \left(- 1 \times \left(\beta_ {0} / \beta_ {1}\right)\right) \times \\ \left(\sum_ {r _ {p} = 1} ^ {N} d _ {r _ {p}}\right) / \left(\sum_ {r _ {p} = 1} ^ {N} r _ {p} ^ {- a _ {p}}\right) \end{array}\tag{10}
$$

In the equation above, the shape parameter $\left( \mathsf { a } _ { \mathsf { p } } \right)$ is estimated from prior equations and the integral of individual app downloads $\mathrm { ( d _ { r p } ) }$ defines the total downloads associated with all top ranked apps.

## Data

As we mentioned earlier, the top-paid rank list and topgrossing rank list are readily available from various websites such as Apple, Appshopper, AppAnnie, and Mobilewalla. Our data period was from April 2011 to May 2011. The information collected contained the top 200 paid and the top 200 grossing app rankings recorded twice for each day during this period for both iPad and iPhone. We also collected data on prices. It should also be noted that the presented methodology could be scaled to incorporate a ranking list of any size as long as data is available. The summary statistics are given in Table 2.

We observed 20 different categories for apps where 38 percent were categorized as games, 13 percent as productivity, 7 percent as entertainment, 6 percent as utilities, 5 percent as photography, 5 percent as education, 4 percent as business, 3 percent as news, and 18 percent as the remaining 12 categories. A snapshot of the categories is presented in Figure 1.

In our calibration, we did not use any app characteristics other than the rank and price of an app.<sup>9</sup> The descriptive statistics are presented only to show the differences between apps for iPad and iPhone. For example, the average app file size is smaller for the iPhone (when compared to the iPad) and app prices are lower, suggesting the possibility of fewer graphical details, potentially due to the smaller screen size on iPhones.

Table 2. Summary Statistics (from April 2011 to May 2011)

<table><tr><td></td><td>iPad (Paid)</td><td>iPad (Grossing)</td><td>iPhone (Paid)</td><td>iPhone (Grossing)</td></tr><tr><td>N</td><td>23471</td><td>19857</td><td>21855</td><td>18008</td></tr><tr><td>Average Rank</td><td>99.63 (57.91)</td><td>100.04 (57.66)</td><td>99.98 (57.78)</td><td>99.94 (57.73)</td></tr><tr><td>Average Price ($)</td><td>4.31 (4.44)</td><td>12.18 (51.03)</td><td>1.73 (1.68)</td><td>6.76 (44.68)</td></tr><tr><td>Average File Size (MB)</td><td>73.55 (127.44)</td><td>83.98 (142.14)</td><td>51.58 (110.08)</td><td>68.26 (131.49)</td></tr></table>

![](/api/attachments/H7K3ZEMX/fulltext/images/634bf10a4a57b88a0e348e72e917c1b3de6d0d7bb857fe5a645268af5c6f39ef.jpg)  
Figure 1. Share of Various Categories of App in Top 200 Paid List

Overlapping Apps on iPad and iPhone (Top 200 Paid List)  
![](/api/attachments/H7K3ZEMX/fulltext/images/01ed0fee1df5c10f52cdeefca81502ce0f4b309ab5d36933e6c4c56548d5f140.jpg)  
Figure 2. Overlapping Apps on iPad and iPhone (Top 200 Paid List)

<table><tr><td colspan="3">Table 3. Summary Statistics of Apps Ranked in Both Top Paid and Top Grossing Lists</td></tr><tr><td></td><td>iPad</td><td>iPhone</td></tr><tr><td>N</td><td>10709</td><td>8164</td></tr><tr><td>Average Rank on Top Paid List</td><td>74.00 (54.22)</td><td>64.46 (52.87)</td></tr><tr><td>Average Rank on Top Grossing List</td><td>88.67 (57.50)</td><td>93.72 (57.32)</td></tr><tr><td>Average app price</td><td>6.41 (5.11)</td><td>2.45 (2.22)</td></tr><tr><td>Average app size (MB)</td><td>94.39 (149.80)</td><td>78.94 (149.49)</td></tr></table>

![](/api/attachments/H7K3ZEMX/fulltext/images/d630cd0cf6cc5ae96800fe512f118626b2cbee6770fc69a99412c91097452503.jpg)  
Figure 3. Overlapping Apps on Top 200 Paid and Top 200 Grossing App Lists (iPad and iPhone)

We observe that, on average, 28 percent of apps overlap between iPhone and iPad lists and the average correlation between ranks is 0.46. We also found that 128 (10%) unique apps out of 1,223 have a presence in the top paid lists for both the iPad and iPhone. Similarly, 207 (13%) unique apps out of 1,638 have a presence in the top free lists for both the iPad and iPhone.

We plot the rank correlation across two different platforms in Figure 2.

For our analysis, we use apps that appear on both lists. A summary of the overlap between these two lists is provided in Table 3.

On average, 53 percent of the top 200 paid apps on iPad and 46 percent of the top 200 paid apps on iPhone are also ranked among the top 200 grossing apps list. As seen in Figure 3, there is a strong correlation (average value = 0.55 on iPad and 0.49 on iPhone) between the ranks of apps on the top-paid list and top-grossing list, which suggests that a higher rank (lower numerical value) in the paid list tends to generate larger revenue.

## Results

## Shape Parameter (a)

Table 4 presents our estimates of coefficientsrecovered with equation (4).

A positive and significant estimate β suggests that an increase in the rank on the top-paid list increases the rank on the top-grossing list as well. Estimate for price (β<sub>2</sub>) is negative and significant suggesting, all else equal, higher prices lead to more revenues and a lower numerical rank on the top grossing list.<sup>10</sup> We are not examining the effect of price on sales (or elasticity) but are simply using price to connect the two lists. All the coefficients in the regression are highly significant and a high value of R<sup>2</sup> suggests a good fit.

<table><tr><td colspan="3">Table 4. Coefficients from Truncated OLS</td></tr><tr><td>Log(rank_GROSSING)</td><td>iPhone Coef. (robust std. err.)</td><td>iPad Coef. (robust std. err.)</td></tr><tr><td>Log(rank_PAID) -  $\beta_1$ </td><td>1.098 (0.008)***</td><td>1.02 (0.009)***</td></tr><tr><td>Log(price) -  $\beta_2$ </td><td>-1.163 (0.011)***</td><td>-1.129 (0.01)***</td></tr><tr><td>Constant -  $\beta_0$ </td><td>1.014 (0.024)***</td><td>2.131 (0.025)***</td></tr><tr><td> $R^2$ </td><td>0.820</td><td>0.815</td></tr><tr><td>N</td><td>8164</td><td>10709</td></tr></table>

\*\*\*p-value < 0.001 (1% significance)

<table><tr><td colspan="3">Table 5. Estimated Pareto Shape Parameters</td></tr><tr><td></td><td>iPad</td><td>iPhone</td></tr><tr><td> $a_p$ </td><td>0.903</td><td>0.944</td></tr><tr><td> $a_g$ </td><td>0.886</td><td>0.860</td></tr></table>

As shown in equations (6,) (7), and (8), once we estimate (4), we can recover the shape parameter for both the top-grossing and top-paid apps readily. They are produced in Table 5.

The estimated values suggest that most sales occur in the “head,” so the distribution of app demand is top-heavy (even within the 200 top apps).

A true benefit of the shape parameter is that we can estimate the ratio of the number of downloads of two apps that are ranked differently during any given day in Apple’s app store.

$$
f o r i P a d: \left. \frac {d _ {p 1}}{d _ {p 2}} = \left(r _ {p 1} / r _ {p 2}\right) ^ {- 0. 9 0 3} \right.\tag{11}
$$

$$
\text {   for   iPhone:   } \left. d _ {p 1} \right/ d _ {p 2} = \left(r _ {p 1} / r _ {p 2}\right) ^ {- 0. 9 4 4}\tag{12}
$$

Therefore, an important finding of equations (11) and (12) is that one can compare the value of different ranks. We can infer the number of downloads or revenues for different ranks. For example, the number of downloads enjoyed by a top ranked iPad app is 120 times higher than the app ranked at 200. Similarly a top ranked iPhone app gets 150 times more downloads than the app ranked at 200. Also, from the shape parameters for revenue (based on the top-grossing app list), the top-ranked app grosses 1.86 times more revenue than the second ranked app on the iPad. This relative valuation is an important factor for firms when they are investing marketing dollars in promoting their applications. One can readily infer the benefit of moving up or down in rank relative to the money spent on promotions.

## Scale Parameter (b)

Usually, the shape parameter would be all we are interested in. Estimates of the shape parameters readily allow for comparison between two ranks. Moreover, the shape parameters tend to remain more stable over time. However, we can now provide a method to estimate the scale parameter as well.

To estimate the scale parameter we need additional information. Note from equation (7) that we can only recover the ratio of scale parameters. To estimate absolute scale parameters, we would need access to actual sale volume from a vendor. However, as we showed in equations (9) and (10), even the aggregate total number of downloads is enough to recover these parameters.

Fortunately, the total number of downloads is calculated and presented by various app store analytics firms. As estimated by one such analytics firm (Distimo), the total number of downloads per day for the top 300 paid iPad apps is approximately 110,680 and the total number of downloads per day for the top 300 paid iPhone apps is approximately 386,545. We can readily plug these numbers in equations (9) and (10) to estimate the scale parameter.<sup>11</sup>

Given these statistics and the coefficients from the regression above, estimated scale parameters using equations (9) and (10) are provided in the first row of Table 6.

<table><tr><td colspan="3">Table 6. Estimated Pareto Scale Parameters</td></tr><tr><td></td><td>iPad</td><td>iPhone</td></tr><tr><td>bp</td><td>13,516</td><td>52,958</td></tr><tr><td>bg</td><td>$89,206</td><td>$126,666</td></tr></table>

![](/api/attachments/H7K3ZEMX/fulltext/images/17a9fc42120593c1ad9a8440a3c2766b7390cb881bda877eaa5893f727f8f089.jpg)  
Figure 4. Number of App Downloads Versus App Rank on Top Paid List (iPad and iPhone)

Thus we can now illustrate the relationship that links the total downloads of each app for any given rank. Similarly, we can specify the function that links revenues with rank. Using our estimated parameters, these functions are as follows:

$$
d _ {i P a d} = 1 3, 5 1 6 \times r _ {p} ^ {- 0. 9 0 3}\tag{13}
$$

$$
d _ {i P h o n e} = 5 2, 9 5 8 \times r _ {p} ^ {- 0. 9 4 4}\tag{14}
$$

We expect the estimate of scale parameter to change with time as more consumers buy apps on their mobile devices. Nonetheless, aggregate download numbers allow for the estimation of scale parameter.

The graph in Figure 4 plots equations (13) and (14) for app sales as a function of app rank in the top paid list for the iPad and iPhone. Given the high value for the shape parameter, the number of downloads drop sharply. An app ranked 200 on the iPad would generate about 100 downloads per day. However, an app ranked at 1000 would generate only about 25 downloads. Given that there are more than 200,000 apps available, it is fair to conclude that most of them generate little or no demand.

## Model Validation

One challenge in testing these models is the lack of available data on downloads and app revenue. We developed three different ways to test the validity of our model.

First, recall that we estimate two different models, one estimating total downloads and the other estimating total revenue. The difference in the two is that the second model is price multiplied by the demand coming from the first model. Thus, we can cross-validate the models by estimating downloads from the first model and multiply by the app price to get the estimated revenue from the second model.

From Table 7, we can see that the values of estimated revenue are very close (confirmed by t-test) which provides confidence in the accuracy of the computed models.

Additionally, to validate the model, we partnered with two separate app developers (who have requested to remain anonymous). Developer D1 shared data on an application, its rank, and total downloads (iPad + iPhone) for a month. Developer D2 shared similar data, but her app was available for iPhone only. We cannot estimate shape parameter from

Table 7. Summary Statistics of Estimated Revenue and Price × Estimated Downloads

<table><tr><td></td><td colspan="2">iPhone</td><td colspan="2">iPad</td></tr><tr><td></td><td>N</td><td>Mean (std. dev.)</td><td>N</td><td>Mean (std. dev.)</td></tr><tr><td>Log (Estimated Downloads × Price)</td><td>8164</td><td>7.97 (0.877)</td><td>10709</td><td>7.23 (0.999)</td></tr><tr><td>Log (Estimated Revenue)</td><td>8164</td><td>8.10 (0.813)</td><td>10709</td><td>7.39 (0.930)</td></tr></table>

![](/api/attachments/H7K3ZEMX/fulltext/images/3f78bca66a9f2dbab6c8882465f7fd4944976cee7a0319f772fe38d82a905b71.jpg)  
Figure 5. Number of App Downloads Versus App Rank on Top Paid List (iPad)

D1 because the data is combined for iPhone and iPad. However, we can still compare whether the predicted total downloads from our model match the actual download numbers provided by the developer. Recall that total predicted downloads are

$$
d _ {t o t a l} = d _ {i P a d} + d _ {i P h o n e} = 1 3, 5 1 6 \times r _ {p} ^ {- 0. 9 0 3} + 5 2, 9 5 8 \times r _ {p} ^ {- 0. 9 4 4}
$$

The mean value of the actual downloads in our data is 1,737 (std. dev. = 666) and the mean value for the estimated downloads based on rank information is 1,652 (std. dev. = 543). From the paired t-test, we find the p-value = 0.388 (pvalue for unpaired t-test is 0.735). Thus, we can conclude, with some confidence, that the estimated model is predicting values that do not have a significantly different mean from the actual download numbers.

We also plot actual and predicted downloads per day for this app over the sample period, as seen in Figure 5. It is evident from the plot that the model is doing a good job of predicting the sale of a given app if the rank is known. This provides additional evidence regarding the robustness of our method.

Data from developer D2 is used to estimate shape parameter. However, D2’s app is a low-ranked app (average rank is 350). Typically Apple does not publish this rank. However, the app developer worked with an app analytics firm that claimed to have this information. The data spanned 5 months from January 2011 to May 2011. The average number of downloads during this period was 301 (std. dev. = 13). Using this data (N = 55),<sup>12</sup> we estimated the shape parameter to be 0.89. This is consistent with our estimate of 0.94. This is despite the fact that the app was in the tail while our model is estimated using top 200 data. Thus, the actual data from two separate apps provides validation for our method in general.

Finally, Distimo also shared the average daily revenue aggregated for the top 200 apps in the top grossing list to be approximately \$632,158 for iPad and \$1,014,371 for iPhone. Using these numbers and the approach suggested in equation (9), we estimated $\mathsf { b } _ { \mathrm { g } }$ as \$80,538 for the iPad and \$120,375 for the iPhone. We see that these scale parameters are close to the estimates we provided in Table 6. This further validates our approach to infer app demand from the publicly available data.

## Discussion

So far we have presented a methodology to infer the functional form of demand for Apple’s App Store (iPad and iPhone). We believe that this approach is portable to any size of ranked lists and any platform as long as the rank data from multiple lists is available publicly. This is an important contribution as it opens doors for both researchers and practitioners to investigate interesting research and marketing investment questions for mobile platforms. Since the Android platform is another fast-growing mobile platform and in-app purchases are gaining momentum, the following discussion shows how our framework can be ported. We also discuss how our approach can be extended to the free app rank list.

## Android Platform

Although the Google Android store provides crude information on the range of total lifetime downloads of an application, it does not provide any meaningful periodic demand numbers. However, similar to Apple, Google does provide both the top paid app lists and the top grossing app lists. Therefore, we can easily port our method to develop the rank-demand correlation for Android app store. We collected similar data for one week in April 2012 and reestimated the shape parameters as shown in Table 8.

We find that that the shape parameter for paid list $( \mathrm { a _ { p } } )$ is similar to the one estimated for the iOS platforms but the shape parameter for revenue $\mathrm { ( a _ { g } ) }$ is larger. It suggests that the revenue generated by apps in a top grossing app list is more skewed on the Android platform.

## In-App Purchase (IAP)

Apple’s iOS and Google’s Android platforms allow for in-app purchases of content, functionality, services, or subscriptions,<sup>13</sup> allowing app developers to generate additional revenue from either paid apps or free apps. In-app purchases allow consumers to buy these additional features after exploring the capabilities and benefits of an app.

Notice that our analysis depends on tying the paid list with the grossing list via price to generate our estimates. However, if in-app purchase options become a major source of revenue, we need to find a way to modify our estimates. In what follows, we explore this option in detail. To account for inapp purchases, we rewrite equation (3) as follows:

$$
p d _ {r g} = d _ {r _ {p}} \times \left(p + f \left(I _ {I A P}\right)\right)
$$

$$
w h e r e f \left(I _ {I A P}\right) = \theta \times I _ {I A P} = \left\{ \begin{array}{c} 0 i f a p p h a s n o I A P o p t i o n \left(I _ {I A P} = 0\right) \\ \theta i f a p p h a s I A P o p t i o n \left(I _ {I A P} = 1\right) \end{array} \right.
$$

Here $\mathrm { I } _ { \mathrm { I A P } }$ is an indicator variable identifying the availability of in-app purchase options. If there is no in-app purchase available $( \mathrm { I } _ { \mathrm { I A P } } { = } 0 )$ , our analysis boils down to what we did earlier. If in-app purchases are available $( \mathrm { I } _ { \mathrm { I A P } } = 1 )$ , θ determines the revenue generated from in-app purchases. In short, all else equal, if an app generates large revenues from in-app purchases, its position on the top grossing list will move relative to the top paid list. Since we know which apps have in-app purchase options, it allows for ready identification of θ. Taking logs of both sides reduces the regression equation to

$$
\log \left(r _ {g}\right) = \beta_ {0} + \beta_ {1} \times \log \left(r _ {p}\right) + \beta_ {2} \times \log \left(p + \theta \times I _ {I A P}\right) + \varepsilon\tag{15}
$$

Estimating the parameters using a nonlinear regression, we find that the shape parameters are consistent $( \mathsf { a } _ { \mathsf { p \ i P a d } } = 0 . 9 0 $ $\mathsf { a } _ { \mathsf { p } \_ \mathrm { i P h o n e } } = 0 . 9 3 9 )$ Thus, the addition of in-app purchase options does not change the slope parameter of our estimated distribution. We estimate the value of $\theta = 0 . 1 6$ (p-value < 0.03), which suggests that, on average, IAP revenue is approximately equal to the 16 cents per download of an app (about 7% of the revenue). Thus, our method allows us to calibrate the rank-sales relationship readily, even in the presence of inapp purchase options.

Of course, our model’s accuracy will decrease if each paid app has an in-app purchase option and generates unequal revenues from in-app purchases for unobserved reasons. Even then, if we have some observables that can predict inapp revenues, we can readily use this method.<sup>14</sup> In short, our method can be readily modified to accommodate the in-app purchase option.

## Free Apps

Our approach so far has focused on the demand estimation for the paid apps that are placed on the top 200 bestselling list and overlap with the top grossing app list. Another extension of this work is to estimate the demand for free apps, where the overlap with the top grossing list is purely because of the inapp purchases. Since free apps attract over 10 times more volume of downloads, it is even more lucrative for app developers to infer the extent of revenue generated using in-app purchases for free apps. We briefly discuss how our method can be applied to free apps.

<table><tr><td colspan="2">Table 8. Estimated Pareto Shape Parameters (Android Platform)</td></tr><tr><td></td><td>Android</td></tr><tr><td> $a_p$ </td><td>0.985</td></tr><tr><td> $a_g$ </td><td>1.165</td></tr></table>

The key difference between paid and free apps is price, so the revenues for free apps are simply

$$
p d _ {r _ {g}} = d _ {r _ {F}} \times f (I _ {I A P})
$$

$$
\text { where } f \left(I _ {I A P}\right) = \theta \times I _ {I A P} = \left\{ \begin{array}{l} 0 \text { if   app   has   no   IAP   option } \left(I _ {I A P} = 0\right) \\ \theta \text { if   app   has   IAP   option } \left(I _ {I A P} = 1\right) \end{array} \right.
$$

Using the overlap between top grossing apps and top free apps, our estimable form, similar to equation (5), reduces to

$$
\log (r _ {g}) = \beta_ {0} + \beta_ {1} \times \log (r _ {F}) + \varepsilon
$$

where the estimated parameters are related to model parameters as follows:

$$
\begin{array}{c} \beta_ {0} = \left(1 / a _ {g}\right) \times \log \left(\frac {\theta \times b _ {F}}{b _ {g}}\right) \\ \beta_ {1} = \left(a _ {F} / a _ {g}\right) \end{array}
$$

Recall, our grossing app parameter $\mathrm { a _ { g } }$ is already estimated from the paid list. Therefore, we can readily recover ${ \bf a } _ { \mathrm { F } }$ from the estimate $\beta _ { I } . ^ { 1 5 }$

In our estimation, we treat each data point as an independent observation even if the same app appears multiple times. This is because the rank of an app is driven by its sale alone. If that were not the case and some other factors affected rank, then it is possible that a higher ranked app might have lower downloads. In that case, we can rely on fixed effect models. These models assume that each app is separate and unique and has its own intercept. Our method can readily be used if

Apple were to start a ranking scheme that does not entirely rely on demand alone.<sup>16</sup>

## Conclusion

We have used publicly available rank data and presented a methodology to estimate the product sales from the rankings of apps listed in top-200 lists on Apple’s app store for both iPhone and iPad. From our analysis, we find that the number of downloads enjoyed by an iPad app ranked first on the top paid list is 120 times the number of downloads for the app ranked 200. Similarly an iPhone app ranked first gets 150 times more downloads compared to the app ranked at 200. We also show that the iPhone app ranked first on the top grossing list earns 95 times more revenue compared to the app ranked 200. The similar number for the iPad app store is 110. Thus our model allows for comparison between any two ranked apps.

We also provide a method to estimate scale parameter from aggregate data. Thus, we show that the top ranked app on the iPad is downloaded 13,516 times per day and the top ranked app on the iPhone is downloaded 52,958 times per day (April–May 2011). These estimates should help app developers and marketing professionals guide their marketing efforts.

We have validated our model in different ways, including gathering data from two separate app developers. We also consider various extensions. For example, we extend our method to Google’s Android platform to calibrate a similar relationship. We consider the possibility of how in-app purchase options could affect our estimates. We show how our method can be readily adapted to account for the expected growth of in-app purchase options in the future. We also show how our method can be extended to the free app rank list.

Most importantly, we believe that inferring demand data from rank is highly valuable for researchers. It will open doors for more exciting and interesting research that has not been possible due to the absence of reasonable demand estimates. Mobile apps are an important and fast growing technology market. Understanding this market and the opportunities it offers is important for different stakeholders. We believe our research method and results have many important implications and hence make a very useful contribution not only to academic literature, but also to managers and entrepreneurs. We also believe our methods can generalize to any platform that provides top-paid and top-grossing rankings. Top mobile platforms indeed provide such rankings.

Our research can be improved on many different dimensions. Our dataset is limited to the top 200 apps. Having access to a larger number of ranked apps (say, the top 1000) should provide a better fit. Similarly, while we verified our estimates with data from only two app providers, there are significant opportunities to expand the scope of this data collection by collecting data from more apps across different categories. Also, we assumed that both download- and revenue-based rankings follow a power law, but alternate and more precise distributions could also be developed if more data is available from app producers. We hope future research will extend and refine our methods.

## Acknowledgments

First, we would like to thank Distimo for sharing the aggregate sales and demand numbers, and our confidential sources for sharing the application sales data for Apple’s app store.

We thank Vanlal Peka for his help during the data acquisition phase. We thank Michael Smith for his support and feedback on this research project. Finally, we are grateful to the senior editor, the associate editor, and the three anonymous reviewers for helpful feedback and suggestions.

## References

Anderson, C. 2004. “The Long Tail,” Wired Magazine (12:10) (http://www.wired.com/wired/archive/12.10/tail.html).

Barra, H. 2011. “Android: Momentum, Mobile and More at Google I/O,” Official Google Blog, May 10 (http:// googleblog.blogspot.com/2011/05/android-momentum-mobileand-more-at.html).

Boudreau, K. J. 2012. “Let a Thousand Flowers Bloom? An Early Look at Large Numbers of Software App Developers and Patterns of Innovation,” Organization Science (23:5), pp. 1409-1427.

Brynjolfsson, E., Hu, Y. J., and Smith, M. D. 2003. “Consumer Surplus in the Digital Economy: Estimating the Value of Increased Product Variety at Online Booksellers,” Management Science (49:11), pp. 1580-1596.

Brynjolfsson, E., Hu, Y. J., and Smith, M. D. 2010. “The Longer Tail: The Changing Shape of Amazon’s Sales Distribution Curve” (available at SSRN: http://ssrn.com/abstract=1679991).

Carare, O. 2012. “The Impact of Bestseller Rank on Demand: Evidence from the App Market,” International Economic Review (54:2), pp. 717-742.

Chevalier, J., and Goolsbee, A. 2003. “Measuring Prices and Price Competition Online: Amazon.com and BarnesandNoble.com,” Quantitative Marketing and Economics (1:2), pp. 203-222.

Chevalier, J., and Mayzlin, D. 2006. “The Effect of Word of Mouth on Sales: Online Book Reviews,” Journal of Marketing Research (43:3), pp. 345-354.

Ghose, A., Smith, M. D., and Telang, R. 2006. “Internet Exchanges for Used Books: An Empirical Analysis of Product Cannibalization and Welfare Impact,” Information Systems Research (17:1), pp. 3-19.

Ghose, A., and Sundararajan, A. 2006. “Evaluating Pricing Strategy Using e-Commerce Data: Evidence and Estimation Challenges,” Statistical Science (21:2), pp. 131-142.

Poynter, D. 2000, June. “Publishing Poynters,” Para Publishing.

Weingarten, G. 2001. “Below the Beltway,” Washington Post September 2, p. W03 (http://www.washingtonpost.com/wp-dyn/ articles/A21499-2001Aug30.html).

## About the Authors

Rajiv Garg is an assistant professor in the McCombs School of Business at the University of Texas at Austin. He received his Ph.D. in Information Systems and Management from the Heinz College at Carnegie Mellon University. He also has graduate degrees in Computer Science and Electrical Engineering, both from University of Southern California, and an undergraduate degree in Electrical Engineering from Indian Institute of Technology, Banaras Hindu University in India. His research interests are on the intersection of economics, marketing, and information systems with a focus on digital, social, and mobile platforms. Rajiv is a senior member of IEEE and for the past decade has served on the boards of various small corporations. Rajiv’s research work has appeared in Journal of Management Information Systems and various peer-reviewed conference proceedings.

Rahul Telang is a professor of Information Systems and Management at the Heinz College, Carnegie Mellon University. He received his Ph.D. in Information Systems from the Tepper School of Business, Carnegie Mellon University. Rahul’s research interests lie in two major domains: the digital media industry and economics of information security and privacy (for which he received an NSF CAREER). Currently, he is working on a large NSA funded project on examining home users’ security and privacy behavior. Rahul has published extensively in many top journals including Management Science, Marketing Science, Information Systems Research, MIS Quarterly, and Journal of Marketing Research. He is a senior editor at Information Systems Research and MIS Quarterly. His work has been cited in major media outlets and many of his papers have received top honors at journals and conferences.
