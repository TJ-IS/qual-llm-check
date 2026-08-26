---
otero_id: 5252
otero_key: "SH3U22PG"
title: "Borrower Decision Aid for people-to-people lending"
authors: "Lauri Puro; Jeffrey E. Teich; Hannele Wallenius; Jyrki Wallenius"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.12.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Borrower Decision Aid for people-to-people lending

Lauri Puro <sup>a</sup>, Jeffrey E. Teich <sup>b</sup>, Hannele Wallenius <sup>a</sup>, Jyrki Wallenius <sup>c,</sup>⁎

<sup>a</sup> Aalto University School of Science and Technology, Department of Industrial Engineering and Management, POB 15500, FI-00076 AALTO, Finland

<sup>b</sup> New Mexico State University, Management Department, New Mexico State University, Las Cruces, NM 88003, USA

<sup>c</sup> Aalto University School of Economics, Department of Business Technology, POB 21210, FI-00076 AALTO, Finland

## a r t i c l e i n f o

Article history: Received 14 January 2009 Received in revised form 18 December 2009 Accepted 31 December 2009 Available online 18 January 2010

Keywords: People-to-people lending Decision support Reverse auctions

## a b s t r a c t

In setting up, and bidding in online auctions, people face dif<sup>fi</sup>cult strategic decisions. In this study, a Borrower Decision Aid is introduced, which will help formalize the decision making process of the sellers, or borrowers in this case, in one particular P2P loan auction site, Prosper.com. The vast amount of real-life bidding data available in this online auction enables us to build new kinds of tools for decision makers. The Borrower Decision Aid helps the borrower to quantify her strategic options, such as starting interest rate, and the amount of loan requested. We identify which variables concerning the borrower are related to the probability of successfully securing a loan and the <sup>fi</sup>nal interest rate.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

## 1.1. Background

Prosper.com is the <sup>fi</sup>rst people-to-people lending marketplace, based on an online reverse auction. In this marketplace, people make applications for loans, called listings, and then other people make bids on these listings. The winning bidders get to fund the loan and the interest rate is determined by the auction — the more competition, the lower the interest rate. In other words, the idea is to link the person in need of money with people willing to lend money without an intermediating bank. Typically a loan is funded with many bidders (lenders), because most lenders only fund \$50–\$200 per each loan. Lenders bid for these small amounts across many loans to help diversify their risk. Prosper.com was launched publicly in February 2006, and has brokered so far over \$150 million worth of loans [5,17,22].

In this study, we focus on the role of the borrower, i.e. the person who sets up the listing for a loan. The borrower has several important strategic decisions to make, which can later determine if she gets the loan funded or not. The purpose of this study is to provide decision support for the borrower when making these important decisions. In the literature there are only a few publications that discuss decision support in auctions (in general). [1,8,15,16,23,25] are some examples. Their angle is different from ours, though.

Our study has signi<sup>fi</sup>cant practical importance. Currently, borrowers set their listing parameters based on insuf<sup>fi</sup>cient data, such as the average interest rate. In this study, we introduce a framework to analyze the borrower's strategic decisions in terms of success probabilities and estimated <sup>fi</sup>nal interest rates. A Borrower Decision Aid (BDA) is described, which enables the borrower to evaluate her strategic options quantitatively. This is a signi<sup>fi</sup>cant practical improvement to the current situation where Prosper.com only provides scant advice on the starting rate and no advice on the amount of the loan.

In addition to being practically important, our study is interesting in a theoretical sense as well. Namely, the framework and the methods used in constructing the tool are interesting and could be used with other online auction sites.

## 1.2. Objectives of the research

The main objective of this study is to develop a decision support tool for the borrowers. This tool helps the borrowers evaluate their strategic options in quantitative terms. In more detail, we

1. identify the most important factors that affect the outcome of the auction, that is borrower's chances of getting the loan funded;

2. identify the most important decision variables that the borrower can change in order to in<sup>fl</sup>uence the outcome of the auction; and

3. develop a framework and methods to compare different strategic options in quantitative terms.

We look at all the information available and compare it to empirical data on Prosper.com listings. The identi<sup>fi</sup>ed factors are then divided into those which the borrower can in<sup>fl</sup>uence and those that are part of the credit report. Both types of variables are needed in this study, but naturally the ones that the borrower can in<sup>fl</sup>uence are the ones we provide advice on. We examine different methods of comparing strategic options and choose the best methods and variables for the Borrower Decision Aid. The decision support tool is then constructed and tested. This study is limited to Prosper.com auctions only. The framework and methods of constructing the borrower (or seller) decision aid can, however, be extended to other auction sites as well

## 1.3. Data and research methods

This study is based on empirical data provided by Prosper.com. Much of the data is freely available on the Prosper.com website. However, accessing the credit records requires one to register as a lender on the site. In total there were 312,562 listings made on Prosper.com (up to July 2008). Prosper allows access to these listings, which form the basic population data in our study.

The strategic decision making of the borrowers is examined with the help of multivariate statistical analyses, in particular ordinary least-squares regression and logistic regression analysis. The BDA itself is implemented as a website, which could be made available to the public and/or implemented on Prosper's own site or a so called third-party site.

## 1.4. Organization of the paper

The <sup>fi</sup>rst section of this study provided the background and objectives of this study. In Section 2, literature related to the borrowers' strategic decisions is brie<sup>fl</sup>y reviewed. In Section 3 the data used in this study is introduced and the borrower's basic strategic decisions are charted. In this section, the most in<sup>fl</sup>uential decision variables are identi<sup>fi</sup>ed for the development of the BDA. Section 4 describes the construction of the BDA and introduces the underlying methods. In Section 5, the BDA website is described and the two different methods of providing support are compared. Section 6 concludes the study.

## 2. Literature study

The amount of auction literature is vast. Several of the groundbreaking discoveries were made in the 1950s and 1960s when bidding behavior was modeled using a game-theoretic framework. The latest wave of research started after the emergence of online auctions. In particular, the online environment enabled researchers to carry out empirical studies with data gathered from real-life auctions (see, e.g., [2,18,25,26]). This was a clear improvement to previous laboratory studies with university students ([10,11]).

In the traditional auction literature, the roles of the seller and the auctioneer often coincide, although this may not be the case in online auctions. The seller is expected to be able to choose the auction design parameters freely. Much of the literature has focused on comparing different auction mechanisms in different situations and determining which mechanisms provide superior pro<sup>fi</sup>t for the seller ([19,20]); or which mechanisms are ef<sup>fi</sup>cient ([13]). In online auctions the roles of the seller and the auctioneer rarely coincide. The auctioneer is the website that facilitates the auction. The auctioneer has usually chosen some simple and universal auction mechanism that all sellers are obliged to use. Therefore, the strategic choices of the seller are constrained by the parameters of the chosen auction mechanism. This, however, makes the strategic decisions of the sellers no less important, but actually this emphasizes the importance of the few remaining decision variables at the disposal of the seller.

The classic decision variable of the seller is the starting price. The importance of the starting price depends heavily on the type of item sold and the auction mechanism. The literature on the effect of the starting price on the <sup>fi</sup>nal price is somewhat controversial. For example, [14] found empirical evidence stating that under some conditions having a lower starting price can eventually lead to higher <sup>fi</sup>nal price (in a forward auction). They suggested reduced barriers to entry and commitment of bidders as possible reasons. The sunk search and monitoring costs make it psychologically dif<sup>fi</sup>cult for the bidder to walk away from the auction.

Conversely, [9] showed that the correlation between the starting price and the <sup>fi</sup>nal price was positive. This would mean that by entering a higher starting price, the expected <sup>fi</sup>nal price is higher as well. One reason they suggested was that by entering a higher starting price, the seller is able to signal to the bidders that the item is worth at least that much. The higher starting price leads to a higher <sup>fi</sup>nal price also if competition among bidders is generally very weak. In an extreme case, with just one interested buyer, the <sup>fi</sup>nal price will equal the starting price, and therefore the higher starting price leads to higher <sup>fi</sup>nal price. Gilkeson and Reynolds [9] agreed with the theory about reduced barriers to entry and commitment, but they claimed that it would only affect the probability of the auction to succeed (i.e. the item being sold), but not to increase the <sup>fi</sup>nal rate. They studied eBay auctions that had a possibility to use a secret reservation price and they proved that higher starting price leads to lower success probability, but a higher closing price. In [18] the correlation between starting price and <sup>fi</sup>nal price was also found to be positive.

The tradeoff suggested by [9] provides an excellent framework for our study. The borrower has two aims on Prosper.com. First, she wants to get her loan funded in a successful auction event. Second, she wants the interest rate to be as low as possible. The tradeoff makes this decision dif<sup>fi</sup>cult. If the borrower wants to be sure that the loan gets funded, she must settle for a higher interest rate and a higher starting rate. But a lower starting rate may result in a lower <sup>fi</sup>nal rate but at a reduced probability of funding.

Prosper.com is a multi-unit auction, because the loan will normally be funded by multiple bidders. This makes the situation even more interesting. In multi-unit auctions, the borrower can choose the number of items (i.e. loan amount) sold in addition to the starting price. This decision has similar kind of strategic value as the starting price. Most of the previous studies on multi-unit auctions, however, look at the amount as a question about an optimal lot size in repeated auctions ([3], see also [24]). On Prosper.com, however, the same borrower creates only one or at most a couple of listings, and therefore the importance of the amount as a strategic decision variable is further emphasized.

## 3. Strategic decision making of the borrowers

This section begins by introducing the data used in this study, including an explanation of how the Prosper.com auction site operates from the borrower's viewpoint. Next, we identify the most important decision and credit variables that affect the outcome of the listing. These variables will later form the heart of the Borrower Decision Aid.

## 3.1. An example from Prosper.com website

An example of a loan listing from Prosper.com is shown in Fig. 1. Here the borrower is seeking a \$7300 loan to expand a small business. There is still over 37h left in the auction and the loan is already fully funded. The starting rate of the listing was 25.96% and it has been bid down to 13%. The borrower's credit grade is C and he is a veri<sup>fi</sup>ed homeowner. The debt-to-income ratio of the borrower is 39%. The listing includes a short description, where the borrower usually explains how she is planning to use the money. Additionally, the listing may include a picture and endorsements from friends and family.

## 3.2. Description of the data used in the study

Prosper.com offers a unique opportunity to access a vast amount of real-life online auction data ([22]). Prosper.com has been in operation since February 2006 and during this time until August 2008 there have been 312,562 listings created. Our data set starts from May 2006 and includes all non-active listings made before August 2008. The number of listings in our sample is 293,976. From these listings 26,251 (8.4%) have been funded. This data will be used as the basic population. The data is freely available on Prosper.com website, although for additional credit information one must register as a lender. The data was then imported to MS Access, where it was further analyzed.

![](/api/attachments/SH3U22PG/fulltext/images/72f931f8ddc13e061a9b156aaf0369f43100d3f6f39b57015e0a620a68137841.jpg)  
Fig. 1. Screen image from one listing on Prosper.com (Prosper.com, used with permission, 2008)

Large amounts of data are available for every listing including what is available to registered lenders from the credit report. In the Appendix, all the factors have been listed. The most important factors are amount requested, starting rate, credit grade, debt-to-income ratio, duration, funding option, homeownership, and status and end date. In addition, other demographic information is available. The credit information is pulled from Experian Scorex Plus (SM) system, which is specialized in providing people's credit information.

The terms of the loans on Prosper.com are <sup>fi</sup>xed to a three year, fully amortized, unsecured loan. The borrower can choose the loan amount freely between \$1000 and \$25,000. The average requested loan amount is \$7500 (median \$5000). The starting rate of the auction can be set anywhere between 0% and 36%. The average starting rate is 19% (median 18%). The starting rate naturally is very sensitive to the credit grade of the borrower. The credit grade (scaled between AA and HR, where AA is best and HR worst) is calculated by Experian. It takes into account all the credit information variables and grades the borrower accordingly. Debt-to-income ratio is calculated by dividing the borrower's total amount of debt with her income. The ratio is limited to between 0 and 101%. but because the income is selfreported, this statistic could be inaccurate.

The borrower can choose the duration of the auction from four alternatives: 3, 5, 7 and 10 days. 7 days is the most commonly used auction duration. The borrower has the option to end the auction as soon as the loan gets funded. This practically means that the borrower is satis<sup>fi</sup>ed with the starting rate and needs the money as quickly as possible. Otherwise the auction will be open for the full duration. The status of the listing can be completed, expired, withdrawn or cancelled. The completed status means that the listing was funded and the loan issued. The expired status means that the auction ran its full duration but never got funded. The withdrawn status means that at some point during the auction the borrower withdrew the listing. The cancelled status means that Prosper.com has cancelled the auction because of some faulty listing information. Furthermore, the listing can be active, which means that it is currently running. In this study the active listings have been excluded.

## 3.3. Identifying influential variables

In this section we identify the most important variables that affect the success probability of the listing by using pair wise correlation tests. In order to perform the tests some of the variables had to be transformed. The most important transformation was done to the ‘Status’ variable. This was transformed into a dummy variable. The status ‘completed’ was entered as 1 and ‘expired’, ‘withdrawn’ and ‘cancelled’ as 0. We do not know the reasons behind the borrower's withdrawal decision. However, the number of withdrawn listings is very signi<sup>fi</sup>cant, up to 30% of all listings. Therefore, we cannot exclude them all. It seems that a great majority of these listings has been withdrawn because of lack of interest by the bidders. Only 1% of all withdrawn listings were fully funded. Apparently, some people do not want to see their listing expire, if the bidders show only little interest in it. They would rather withdraw it and create a new listing with different listing parameters. In total, there were 140,265 borrowers who made listings on Prosper.com. Of these people, up to 67,297 (48%) had multiple listings. Most of the people who made multiple listings had done so because their <sup>fi</sup>rst listing did not get funded. Up to 77% of the people who had made multiple listings had at least one unsuccessful listing. This further underscores the point that the borrowers could really use a strategic decision support tool, which would help them in <sup>fi</sup>nding the right listing parameters the <sup>fi</sup>rst time.

For this part of the study, the credit grade scale AA–HR was transformed to numbers between 1 and 7. This is an unorthodox way of describing the credit grade, because the credit grade is ordinal scaled, not interval scaled as 1–7 would suggest. Later, this problem has been solved by calculating each credit grade individually, but this scaling allows easy preliminary examination. The funding option was transformed into a dummy variable so that “Open for duration” was entered as 1 and “Close when funded” as 0. The same approach was used with the variable ‘homeownership’.

In Table 1, the correlations between different listing variables and the ‘status’ dummy variable is presented. The pair wise correlation test was performed with all reasonable variables. Some credit information variables were omitted if they suffered from a small data sample or if they were too much alike other variables. The variables that the borrower can have an in<sup>fl</sup>uence on have been presented in the <sup>fi</sup>rst four rows of the table. The rest of the rows are credit information variables, which the borrower cannot in<sup>fl</sup>uence at least in the short-run.

As a whole, the correlations are relatively small. There are a few logical reasons for this. First of all, we have used all the data available. This enables us to see the big picture, but for example the starting rate is very sensitive to the credit grade. For example, a 15% starting rate might guarantee the success of the listing for an AA grade borrower, but the same starting rate might be too low for an HR grade borrower to get her listing funded. Therefore, in the full data set the correlations are lower than when examined one credit grade at a time. Again particularly the starting rate, i.e. “the price of the loan”, is very sensitive to common market interest rates and risk premiums. We have used data from the full two and a half years of time. During this time the federal interest rate has varied between 2 and 5.25% (Federal Reserve [7]). In addition, the recent credit crisis has increased the risk premiums substantially. Therefore, the correlations would be higher if we would look at data from shorter periods of time, where the market fundamentals would be similar for all listings.

The correlation analysis done with the full data set does enable us to compare the signi<sup>fi</sup>cance of different variables. As we can see, the credit information variables have generally higher correlations than the decision variables. This is quite logical, as people with low credit grades have dif<sup>fi</sup>culties in obtaining a loan no matter how high, for example, the starting rate is. All the correlations are statistically signi<sup>fi</sup>cant, because of the high number of observations. The ‘amount requested’ and ‘starting rate’ have higher correlations than the ‘funding option’ and the ‘duration’. The signs of these correlations are in line with [9]. A higher starting rate increases the borrowers chances of getting the loan funded (note that Prosper.com auction mechanism is reversed in the sense that high interest rate is bad for the borrower, i.e. the seller, and good for bidders). Logically, a higher amount requested decreases the borrower's chances of having a successful listing. The funding option “Open for duration”, entered as 1 increases the borrower's success probability, as is the case with the longer duration.

Pairwise correlation tests between success of the listing and listing characteristics.

<table><tr><td></td><td>Correlation</td><td>p-value</td><td>Observations</td></tr><tr><td>Amount Requested</td><td>-0.06</td><td>0.0000</td><td>293,976</td></tr><tr><td>Starting Rate</td><td>0.06</td><td>0.0000</td><td>293,976</td></tr><tr><td>Funding Option</td><td>0.03</td><td>0.0000</td><td>293,976</td></tr><tr><td>Duration</td><td>0.02</td><td>0.0000</td><td>293,976</td></tr><tr><td>Credit Grade $^{a}$ </td><td>-0.28</td><td>0.0000</td><td>293,976</td></tr><tr><td>Debt-to-Income Ratio</td><td>-0.04</td><td>0.0000</td><td>274,246</td></tr><tr><td>Homeownership</td><td>0.07</td><td>0.0000</td><td>293,976</td></tr><tr><td>Current Delinquencies</td><td>-0.14</td><td>0.0000</td><td>291,732</td></tr><tr><td>Delinquencies last 7 years</td><td>-0.10</td><td>0.0000</td><td>291,732</td></tr><tr><td>Amount Delinquent</td><td>-0.06</td><td>0.0000</td><td>220,252</td></tr><tr><td>Income</td><td>0.03</td><td>0.0000</td><td>293,976</td></tr></table>

Pairwise correlation between success of the listing and listing characteristics in credit grades A and D.

<table><tr><td rowspan="2"></td><td colspan="3">Credit Grade A</td><td colspan="3">Credit Grade D</td></tr><tr><td>Correlation</td><td>p-value</td><td>Obs.</td><td>Correlation</td><td>p-value</td><td>Obs.</td></tr><tr><td>Amount Requested</td><td>-0.24</td><td>0.0000</td><td>11,073</td><td>-0.18</td><td>0.0000</td><td>43,234</td></tr><tr><td>Starting Rate</td><td>0.11</td><td>0.0000</td><td>11,073</td><td>0.17</td><td>0.0000</td><td>43,234</td></tr><tr><td>Funding Option</td><td>-0.02</td><td>0.0441</td><td>11,073</td><td>-0.04</td><td>0.0000</td><td>43,234</td></tr><tr><td>Duration</td><td>0.03</td><td>0.0006</td><td>11,073</td><td>0.02</td><td>0.0003</td><td>43,234</td></tr><tr><td>Debt-to-Income Ratio</td><td>-0.09</td><td>0.0000</td><td>9501</td><td>-0.05</td><td>0.0000</td><td>40,033</td></tr><tr><td>Homeownership</td><td>0.00</td><td>0.9947</td><td>11,073</td><td>-0.03</td><td>0.0000</td><td>43,234</td></tr><tr><td>Current Delinquencies</td><td>-0.04</td><td>0.0000</td><td>11,035</td><td>-0.07</td><td>0.0000</td><td>42,985</td></tr><tr><td>Delinquencies last 7 years</td><td>-0.01</td><td>0.2484</td><td>11,035</td><td>-0.04</td><td>0.0000</td><td>42,985</td></tr><tr><td rowspan="2">Amount Delinquent Income</td><td>-0.01</td><td>0.2286</td><td>9568</td><td>-0.04</td><td>0.0000</td><td>37,174</td></tr><tr><td>0.02</td><td>0.0091</td><td>11,073</td><td>-0.05</td><td>0.0000</td><td>43,234</td></tr></table>

Next to the credit grade, the delinquency related variables have the second highest correlation. The ‘current delinquencies’ seem to be the most in<sup>fl</sup>uential of these variables. The ‘homeownership’ shows some correlation and the correlation of ‘debt-to-income ratio’ is relatively low. This is the case with the variable ‘income’ as well. All the signs of the variables are logical.

In Table 2 the correlation analysis is repeated for two different credit grades: A and D. This demonstrates how different the two credit grades are from each other. Now that the aggregate credit information variable is already taken into account in the data sampling itself, we can see that the decision variables become much more important. The correlations of the ‘amount’ and the ‘starting rate’ are now relatively high. The correlations of the ‘funding option’ and the ‘duration’ seem to remain at a low level. Note that the number of observations in Table 1 is different across attributes. For example, the ‘Debt to Income’ attribute was not calculated in cases where income was not reported, or it was zero.

Now that the samples already contain information about the credit grade, the correlations of the rest of the credit information variables are signi<sup>fi</sup>cantly lower. It would seem that the ‘debt-to-income ratio’ would have the highest correlation with success of the listing within a credit grade. ‘Homeownership’ seems to be problematic. In credit grade A there is no correlation at all. In credit grade D the correlation is negative, which is counter-intuitive. Owning a house seems to negatively affect the borrower's chances of getting the loan funded. Because of this inconsistency, this variable was omitted.<sup>1</sup> Apparently, the delinquency related credit information variables seem to have some correlation with the success of the listing, but this time the ‘current delinquencies’ are more heavily emphasized. The ‘amount delinquent’ and ‘delinquencies last 7 years’ seem to underperform the ‘current delinquencies’ throughout the data. The last credit information variable, the ‘income’, behaves very inconsistently. In credit grade A the correlation is very small but positive. In credit grade D the correlation is negative, which is again counter-intuitive. It could be that people expect borrowers with high income to manage their <sup>fi</sup>nancial situation better than credit grade D implies. The correlation of the income variable is relatively low, perhaps because the income is self-reported and possibly inaccurate.

Based on this analysis the most in<sup>fl</sup>uential variables are the ‘starting rate’, ‘amount requested’, ‘credit grade’, ‘debt-to-income ratio’ and ‘current delinquencies’.<sup>2</sup> The development of the borrower decision aid was designed with this set of variables.

![](/api/attachments/SH3U22PG/fulltext/images/3c55a2cc1d91a3f38184f8fb1322a8604eaeb01b2662a007144b24dfe0a98893.jpg)  
Fig. 2. Interest rates by credit grades on Prosper.com (Eric's credit community, 2008 [6]).

## 4. Borrower decision aid underlying model

In this section we develop the Borrower Decision Aid using an underlying logistic regression model and a query method, a brute force categorization of the database. They are alternative models which provide information about the probability of the listing being funded given initial parameter settings such as starting rate, loan amount, credit rating etc. The <sup>fi</sup>nal rate given these parameters is also predicted via an OLS regression model. In general, the predictions are based on the most recent six months of data, instead of the whole 2.5 years available because the market for loans has substantially changed during that time period. The Federal Funds rate has varied between 2 and 5.25% during the 2.5 years (Federal Reserve [7]). Also the market risk premiums have <sup>fl</sup>uctuated. For example the credit crisis that started in spring 2007 has increased the risk premiums signi<sup>fi</sup>cantly. In Fig. 2 we can see how the interest rates have <sup>fl</sup>uctuated on Prosper.com during the previous year for the various credit grades.

## 4.1. Logistic regression model

The Borrower Decision Aid (BDA) estimates the probability of getting the loan funded, given planned listing parameters and borrower's credit information. We opted to use the logistic regression model because normal regression does not allow a dependent variable to be binary (listing getting funded or not). Gilkeson and Reynolds [9] used logistic regression in their study to examine how the starting rate affected auction success. The logistic regression is based on the cumulative logistic probability function described below (see, e.g., [21]).

$$
f (z) = \frac {1}{1 + e ^ {- z}}
$$

where f(z) represents the probability of funding given the set of independent variables de<sup>fi</sup>ned as follows:

$$
z = \beta_ {0} + \beta_ {1} x _ {1} + \beta_ {2} x _ {2} + \beta_ {3} x _ {3} + \dots + \beta_ {k} x _ {k},
$$

otherwise the logistic regression works in similar manner as the ordinary regression model.

The logistic regression was calculated separately for all credit grades. The reason for this was that borrowers behave very differently between the credit grades as we saw in Table 2. Thus, by calculating the credit grades separately we can get more accurate results that match the current credit grade speci<sup>fi</sup>cally. Another reason for this is that the credit grade itself is an important factor in determining whether the listing gets funded or not. However, adding it to the model as a variable is dif<sup>fi</sup>cult because it is ordinal scaled, not interval scaled.

The independent variables: ‘starting rate’, ‘amount’, ‘debt-to-income ratio’ and ‘current delinquencies’ were chosen according to the analysis in Section 3.3. In Table 3 the coef<sup>fi</sup>cients of the logistic regression models have been displayed. They all have logical signs. Increasing the ‘starting rate’ increases one's chances of getting the loan funded. Conversely, increasing the requested ‘amount’, ‘debt-to-income ratio’ or ‘current delinquencies’ decreases one's chances of getting the loan funded. All the independent variables are statistically signi<sup>fi</sup>cant. In logistic regression there is no equivalent measure for the coef<sup>fi</sup>cient of determination R<sup>2</sup>. Instead we use McFadden's Pseudo-R<sup>2</sup>.

As we can see from Table 4, as we introduce new variables one after another, starting with ‘amount’, followed by ‘starting rate’, ‘debt-to-income ratio’, and ‘current delinquencies’, the Pseudo-R<sup>2</sup> increases to 0.208, but adding additional independent variables does not improve the model signi<sup>fi</sup>cantly.<sup>3</sup> We use the query method, developed below, to cross validate the model.

## 4.2. Query method

The query method is an intuitive data-driven way of determining the success probability. Based on the listing parameters entered by the borrower, the database is searched for similar listings within a certain range (+/−25%) of the value of the parameter. This ensures that the query returns an adequate number of similar kinds of listings. The ‘current delinquencies’ were queried as a binary true/false variable.

Table 3  
Logistic regression coef<sup>fi</sup>cients and Pseudo-R<sup>2</sup>s.

<table><tr><td rowspan="2">Credit Grade</td><td colspan="5">Coefficients</td><td rowspan="2">Pseudo- $R^2$ </td><td rowspan="2">Observations</td></tr><tr><td>Constant</td><td>Starting rate</td><td>Amount</td><td>DTI</td><td>Delinquencies</td></tr><tr><td>AA</td><td>-0.291</td><td>14.990</td><td>-0.000140</td><td>-0.83481</td><td>-0.788</td><td>0.170</td><td>2844</td></tr><tr><td>A</td><td>-0.773</td><td>16.895</td><td>-0.000156</td><td>-2.68859</td><td>-0.617</td><td>0.208</td><td>3562</td></tr><tr><td>B</td><td>-0.911</td><td>10.544</td><td>-0.000167</td><td>-0.93690</td><td>-0.528</td><td>0.166</td><td>5682</td></tr><tr><td>C</td><td>-0.356</td><td>7.177</td><td>-0.000268</td><td>-2.20924</td><td>-0.403</td><td>0.191</td><td>9610</td></tr><tr><td>D</td><td>-1.184</td><td>5.514</td><td>-0.000273</td><td>-1.34284</td><td>-0.399</td><td>0.162</td><td>12,482</td></tr><tr><td>E</td><td>-3.271</td><td>11.204</td><td>-0.000652</td><td>-1.53234</td><td>-0.195</td><td>0.218</td><td>11,436</td></tr><tr><td>HR</td><td>-3.424</td><td>9.357</td><td>-0.000846</td><td>-0.62510</td><td>-0.139</td><td>0.206</td><td>21,908</td></tr></table>

Then the BDA calculates the success ratio of this sample, i.e. how many listings got funded.

The logistic regression can calculate the precise success probability with exact listing parameters, whereas the query method takes a set of listings which have relatively similar listing parameters. The query method requires vast amounts of data (i.e., listings) to work properly. When there are not enough similar listings, the reliability of the query method quickly decreases. This problem arises when the given listing parameters are less frequently used. As stated previously, all the methods use 6 months of data. For the query method, however, the data sample is extended to 12 months if the number of similar listings is below 20. The user of the BDA will naturally be alerted when the sample period is increased to 12 months.

## 4.3. Regression model for the final rate

The <sup>fi</sup>nal rate of the listing was estimated with an ordinary regression model. In Table 5 the correlations between the regression variables have been calculated for credit grade A. The correlation was highest between the ‘<sup>fi</sup>nal rate’ and the ‘starting rate’. The correlation between the ‘<sup>fi</sup>nal rate’ and the ‘amount’ is also high. The ‘debt-to-income ratio’ and ‘current delinquencies’ have lower correlations with the ‘<sup>fi</sup>nal rate’, but they are still statistically signi<sup>fi</sup>cant. There is a risk of multicollinearity in the model, because the correlation between the independent variables ‘starting rate’ and ‘amount’ is 0.55. Both variables are vital for the model and therefore neither one was omitted.

The regression model is similar to the logistic regression model, but this time the dependent variable is the <sup>fi</sup>nal rate. The <sup>fi</sup>nal rate is a continuous variable and therefore an OLS regression model is appropriate.

The results of the regression model, presented separately for different credit grades, can be seen in Table 6. Each regression coef<sup>fi</sup>cient is presented with the corresponding p-value associated with the t-test. Almost all of the variables are statistically signi<sup>fi</sup>cant with 5% signi<sup>fi</sup>cance level. There are two exceptions: the variable ‘amount’ in credit grade C and the variable ‘debt-to-income ratio’ in credit grade HR.

The $R ^ { 2 }$ is between 0.5 and 0.7. The number of observations is quite equally distributed among the credit grades. The number of observations is much smaller than in the logistic regression, because here we can use only completed listings. In the last column of Table 6, the <sup>fi</sup>nal rate estimates have been calculated with the following listing parameters: ‘starting rate’ 18%, ‘amount’ \$5000, ‘debt-to-income ratio’ 40% and zero ‘current delinquencies’. As we can see, the <sup>fi</sup>nal rate estimate quickly increases as the credit grade becomes worse. As a whole the regression model predicts the <sup>fi</sup>nal rate reasonably well. Looking at the associated residual plots, it appears there is unequal (increasing) variance associated with some of the variables implying heteroskedasticity, in particular when outside the range of common values. However because we are not calculating prediction intervals in the BDA (point estimates are still unbiased), this appears less serious.

Table 4  
Improvement in Pseudo-R<sup>2</sup> when the number of variables is increased.

<table><tr><td>Explanatory variable</td><td>Pseudo- $R^{2}$ </td></tr><tr><td>Amount</td><td>0.076</td></tr><tr><td>Starting Rate</td><td>0.122</td></tr><tr><td>DTI</td><td>0.170</td></tr><tr><td>Current Delinquencies</td><td>0.208</td></tr><tr><td>All possible</td><td>0.214</td></tr></table>

Data from credit grade A.

## 4.4. Comparison of query and logistic regression methods

As a brief cross validation between the query method and the logistic regression method, we have produced Figs. 3 and 4. In Fig. 3 the BDA was run with listing parameters: credit grade A, ‘debt-to-income ratio’ 40%, zero ‘current delinquencies’ and \$5,000 requested ‘amount’. The ‘starting rate’ was increased from 1% up to 30%. In general, the two methods provide similar results. Within reasonable starting rates between 9 and 17% the results are very similar. For low starting rates (below 7%), the success rate estimates are unreliable for both methods, and probably actually are close to zero. For higher starting rates (above 17%), the actual success rates are probably in between the results produced by the two methods.

In Fig. 4, the analysis is repeated, but this time the ‘starting rate’ was <sup>fi</sup>xed to 15% and the ‘amount’ was changed from \$1000 to \$25,000. Again, the results of both methods are very similar, the query method providing an upper bound and the logistic regression a lower bound for the success rate. The query method has some <sup>fl</sup>uctuations when the number of observations is very small. This is just one crosssection of the data; however on average the two methods should produce similar results.

## 5. Borrower Decision Aid website

The BDA was implemented as a website. On the website the borrower enters the blank <sup>fi</sup>elds in the “borrower information” window as seen in Fig. 5. Then they click “Estimate” and the results for an example are presented on their screens below. First, the tool prints the listing parameters that the borrower entered and shows the search criteria for the query method. Then a sensitivity table is presented, where the borrower can see how the estimated <sup>fi</sup>nal rate and estimated success probability change with different requested amounts and starting rates. In this case, the estimated <sup>fi</sup>nal rate with the given parameters was 11.65% and the success probability 0.46. These <sup>fi</sup>gures were calculated based on the regression models. By increasing the ‘starting rate’ by 1%, the borrower can increase her chances of getting the loan funded to 0.50 but the <sup>fi</sup>nal rate increases to 12.15%. By decreasing the requested ‘amount’, however, the borrower can increase the success probability to 0.50 and decrease the <sup>fi</sup>nal rate to 11.50%. In the table, some other combinations have also been calculated allowing the borrower to decide the best option, or, repeat and recalculate.

Table 5  
Pairwise correlation table for regression variables in credit grade A.

<table><tr><td></td><td>Final Rate</td><td>Amount</td><td>Starting Rate</td><td>DTI</td></tr><tr><td>Final Rate</td><td>1</td><td></td><td></td><td></td></tr><tr><td>Amount</td><td>0.5618</td><td>1</td><td></td><td></td></tr><tr><td>Starting Rate</td><td>0.8218</td><td>0.5496</td><td>1</td><td></td></tr><tr><td>DTI</td><td>0.2155</td><td>0.0999</td><td>0.1927</td><td>1</td></tr><tr><td>Current Delinquencies</td><td>0.1601</td><td>-0.1152</td><td>0.1695</td><td>-0.0647</td></tr></table>

Table 6  
Regression model for the <sup>fi</sup>nal rate.

<table><tr><td></td><td>Starting rate</td><td>Amount</td><td>DTI</td><td>Current Delinquencies</td><td>Constant</td><td> $R^2$ </td><td>Obs</td><td>Final Rate Estimate</td></tr><tr><td>AA</td><td>0.316</td><td>0.00017</td><td>0.005</td><td>0.750</td><td>3.659</td><td>0.639</td><td>1022</td><td>10.38</td></tr><tr><td>p-value</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td></td><td></td><td></td></tr><tr><td>A</td><td>0.527</td><td>0.00013</td><td>0.009</td><td>0.391</td><td>2.717</td><td>0.693</td><td>931</td><td>13.18</td></tr><tr><td>p-value</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td></td><td></td><td></td></tr><tr><td>B</td><td>0.494</td><td>0.00014</td><td>0.004</td><td>0.330</td><td>4.624</td><td>0.565</td><td>1280</td><td>14.37</td></tr><tr><td>p-value</td><td>0.000</td><td>0.000</td><td>0.040</td><td>0.000</td><td>0.000</td><td></td><td></td><td></td></tr><tr><td>C</td><td>0.739</td><td>0.00006</td><td>0.008</td><td>0.390</td><td>0.443</td><td>0.665</td><td>1535</td><td>14.34</td></tr><tr><td>p-value</td><td>0.000</td><td>0.081</td><td>0.019</td><td>0.000</td><td>0.190</td><td></td><td></td><td></td></tr><tr><td>D</td><td>0.683</td><td>-0.0002</td><td>0.010</td><td>0.380</td><td>3.713</td><td>0.546</td><td>1284</td><td>15.33</td></tr><tr><td>p-value</td><td>0.000</td><td>0.000</td><td>0.013</td><td>0.000</td><td>0.000</td><td></td><td></td><td></td></tr><tr><td>E</td><td>0.840</td><td>0.00045</td><td>0.023</td><td>0.284</td><td>-1.005</td><td>0.509</td><td>536</td><td>17.31</td></tr><tr><td>p-value</td><td>0.000</td><td>0.002</td><td>0.048</td><td>0.000</td><td>0.436</td><td></td><td></td><td></td></tr><tr><td>HR</td><td>0.870</td><td>0.00045</td><td>0.004</td><td>0.120</td><td>-0.260</td><td>0.676</td><td>484</td><td>17.82</td></tr><tr><td>p-value</td><td>0.000</td><td>0.009</td><td>0.455</td><td>0.002</td><td>0.796</td><td></td><td></td><td></td></tr></table>

Below the sensitivity table, there are more detailed results. First, we can see the search criteria used by the query method. Then there is the <sup>fi</sup>nal rate estimate with coef<sup>fi</sup>cient of determination and number of observations. Next, the tool calculates the estimated <sup>fi</sup>nal rate according to the regression model as presented in Section 4.3. In this case the estimate is 11.63%, which is signi<sup>fi</sup>cantly below the starting rate of 15%. Below the estimated <sup>fi</sup>nal rate, the tool presents the R<sup>2</sup>, and number of observations used in constructing the model. These basic regression diagnostics give some indication of the reliability of the results.

The next analysis is the logistic regression. Here the BDA calculates the estimated success probability of the listing. In this case the probability of the listing getting funded is 46%. Again, the regression diagnostics, i.e. the Pseudo-R<sup>2</sup> and the number of observations used in constructing the particular logistic regression model, have been attached to the regression results. The <sup>fi</sup>nal analysis is the query method. Here the BDA queries the database for similar listings as the one entered by the borrower. The search criteria were shown in the very beginning of the results box. In this case there were in total 51 similar listings of which 24 were funded. The implied success probability is 47%, which is very close to the one given by the logistic regression method. Finally, the 51 similar listings have been printed individually (only the <sup>fi</sup>rst four are shown in the <sup>fi</sup>gure). The borrower can then manually check what kind of listings people have made previously and the result.

Query Method vs. Logistic Regression Method (Starting Rate)  
![](/api/attachments/SH3U22PG/fulltext/images/8fcda3d0f30da4ad4a1434665e56cf4c0a5508329c7d4c569abc135540dff2ac.jpg)  
Fig. 3. Query method compared against logistic regression method.

## 6. Conclusions

The main objective of this study was to develop a decision support tool for the borrowers in a P2P reverse auction lending environment. The underlying tool is based on regression models and data driven query methods. The tool enables the borrowers to evaluate their strategic options in quantitative terms. We found that there is a tradeoff between having a low <sup>fi</sup>nal rate and getting the loan funded, as the previous literature had suggested. In order to have a low <sup>fi</sup>nal rate, the borrower must choose a lower starting rate. This, however, decreases the borrower's chances of getting the loan funded. Therefore, the borrower must consider these two factors and make the dif<sup>fi</sup>cult tradeoff decision about the targeted <sup>fi</sup>nal rate and the acceptable risk

Query Method vs. Logistic Regression Method (Amount)  
![](/api/attachments/SH3U22PG/fulltext/images/83f00328e966d55ae0343d471b7aa981a6819eaaaeded7f80a903e947b21068c.jpg)  
Fig. 4. Query method compared against logistic regression method.

Borrower Decision Aid  
![](/api/attachments/SH3U22PG/fulltext/images/81502709867c5e47593653d00f7129ba363d593211fd24863118bd7107519dfb.jpg)  
Fig. 5. Example screen image of Borrower Decision Aid (Borrower Decision Aid, 2008 [4]).

in terms of success probability. The Borrower Decision Aid (BDA) quanti<sup>fi</sup>es this decision by calculating the estimated success probability and the estimated <sup>fi</sup>nal rate. In addition, the borrower can <sup>fi</sup>netune both the success probability and the estimated <sup>fi</sup>nal rate by changing the loan amount. By requesting a smaller loan amount the success probability increases and the <sup>fi</sup>nal rate decreases. If the borrower is not able to <sup>fi</sup>nd a satisfying starting rate that would have acceptable success probability combined with suitable <sup>fi</sup>nal rate, she must decrease the loan amount.

The BDA assists the borrower to see the listing parameters in a strategic context and provides useful quantitative information to support the <sup>fi</sup>nal decision. As such the BDA naturally works only with P2P lending sites similar to Prosper.com. However, the methods used in constructing the tool could be used in other contexts as well. Firstly, the BDA could be extended to other online auctions with suf<sup>fi</sup>cient data available. The auctions would not have to be multi-unit, but the success probability could be attached, for example to exceeding the secret reservation price (used, for example, on eBay; see [12]). The <sup>fi</sup>nal rate estimate is naturally even more widely applicable. A reliable estimate of the <sup>fi</sup>nal price would be useful for the seller in any auction. The availability of data is probably the biggest constraint in expanding the use of the BDA.

One of the bene<sup>fi</sup>ts for auction sites to provide access to their raw auction data is the possible development of third party sites providing tools to the general public. Prosper has already bene<sup>fi</sup>ted from this aspect of their philosophy and will continue to do so. We have provided our BDA to Prosper, and they are considering implementing our tool on their site.

## Acknowledgement

This research was supported by the Academy of Finland grant number #121980.

<table><tr><td>Listing Factor</td><td>Description</td></tr><tr><td>Amount Funded</td><td>The sum of bid amounts or requested amount if fully funded</td></tr><tr><td>Amount Remaining</td><td>The amount still remaining unfunded</td></tr><tr><td>Amount Requested</td><td>The amount requested in the listing</td></tr><tr><td>Bid Count</td><td>The number of bids on this listing</td></tr><tr><td>Borrower City</td><td>The home city of the borrower</td></tr><tr><td>Borrower Starting Rate</td><td>The starting rate of the listing</td></tr><tr><td>Borrower State</td><td>The home state of the borrower</td></tr><tr><td>Category</td><td>One of the following:Not availableDebt consolidationHome improvementBusiness loanPersonal loanStudent loanAuto loanOther</td></tr><tr><td>Creation Date</td><td>The date the listing was created</td></tr><tr><td>Credit Grade</td><td>The credit grade of the borrower AA-HR</td></tr><tr><td>Debt-to-Income Ratio</td><td>The debt-to-income ratio of the borrower</td></tr><tr><td>Description</td><td>The description about the listing written by the borrower</td></tr><tr><td>Duration</td><td>The duration of the listing</td></tr><tr><td>End Date</td><td>The date when the listing ends</td></tr><tr><td>Funding Option</td><td>One of the following:Open for durationClose when funded</td></tr><tr><td>Group Key</td><td>The identifier code of the group in which the borrower is a member of</td></tr><tr><td>Is Borrower Homeowner</td><td>Specifies if the borrower is a verified homeowner</td></tr><tr><td>Key</td><td>The identifier code of the listing</td></tr><tr><td>Lender Rate</td><td>The final interest rate of the listing</td></tr><tr><td>Member Key</td><td>The identifier code of the borrower</td></tr><tr><td>Start Date</td><td>The starting time of the listing</td></tr><tr><td>Status</td><td>One of the following:ActiveWithdrawnExpiredCompletedCancelledPending Verification</td></tr><tr><td>Title</td><td>The title of the listing</td></tr><tr><td>Additional Credit Information</td><td>Description</td></tr><tr><td>Amount Delinquent</td><td>The amount delinquent at the time the listing was created</td></tr><tr><td>Bankcard Utilization</td><td>The percentage of available revolving credit that is utilized at the time the listing was created</td></tr><tr><td>Borrower Occupation</td><td>The occupation of the borrower</td></tr><tr><td>Current Credit Lines</td><td>The number of credit lines</td></tr><tr><td>Current Delinquencies</td><td>The number of current delinquencies</td></tr><tr><td>Date Pulled</td><td>The date when the credit information was pulled</td></tr><tr><td>Delinquencies Last 7 Years</td><td>The number of delinquencies in the last 7 years</td></tr><tr><td>Employment Status</td><td>The employment status of the borrower</td></tr><tr><td>First Recorded Line of Credit</td><td>The date of the first recorded credit line of the borrower</td></tr><tr><td>Income</td><td>The annual income range of the borrower0 – Not displayed1 – $0 or unable to verify2 – $1–24,9993 – $25,000–49,9994 – $50,000–74,9995 – $75,000–99,9996 – $100,000+7 – Not employed</td></tr><tr><td>Inquiries Last 6 Months</td><td>The number of inquiries in the last 6 months</td></tr><tr><td>Length Status Months</td><td>The length of the employment status in months</td></tr><tr><td>Open Credit Lines</td><td>The number of open credit lines</td></tr><tr><td>Public Records Last 10 Years</td><td>The number of public records in the last 10 years</td></tr><tr><td>Public Records Last 12 months</td><td>The number of public records in the last 12 months</td></tr><tr><td>Revolving Credit Balance</td><td>Amount of revolving credit balance</td></tr><tr><td>Total Credit Lines</td><td>The number of total credit lines</td></tr></table>

Appendix A. Listing factors and additional credit information

## References

[1] G. Adomavicius, A. Gupta, Toward comprehensive real-time bidder support in iterative combinatorial auctions, Information Systems Research 16 (2005) 169–185.

[2] P. Bajari, A. Hortaçsu, The winner's curse, reserve prices, and endogenous entry: empirical insights from eBay auctions, RAND Journal of Economics 34 (2) (2003) 329–355.

[3] C. Beam, A. Segev, J.G. Shanthikumar, Electronic negotiation through Internetbased auctions, CITM Working Paper 96-WP-1019, 1996.

[4] Borrower Decision Aid, 2008, http://www.tikkunekut.org/prosper/index.php/, viewed September 10th 2008.

[5] Eric's Credit Community website, “Prosper Loan Growth Last 24 Months”, http:// www.ericscc.com/stats/prosper-loan-growth/, viewed September 5th 2008.

[6] Eric's Credit Community website, “Lender Interest Rate History”, http://www. ericscc.com/stats/interest-rate-history/, viewed September 5th 2008.

[7] Federal Reserve, “Open Market Operations”, http://www.federalreserve.gov fomc/ fundsrate.htm, viewed September 5th 2008.

[8] J. Gallien, L.M. Wein, A smart market for industrial procurement with capacity constraints, Management Science 51 (2005) 76–91.

[9] J.H. Gilkeson, K. Reynolds, Determinants of Internet auction success and closing price: an exploratory study, Psychology & Marketing 20 (6) (2004) 537–566.

[10] R.M. Harstad, Dominant strategy adoption and bidders' experience with pricing rules, Experimental Economics 3 (2000) 261–280.

[11] J.H. Kagel, R.M. Harstad, D. Levin, Information impact and allocation rules in auctions with af<sup>fi</sup>liated private values: a laboratory study, Econometrica 55 (6) (1987) 1275–1304.

[12] R. Katkar, D. Reiley, Public versus Secret Reserves in Auctions: Results from a Pokemon Field Experiment, NBER Working Paper No. W8183, 2001, Available at SSRN: http://ssrn.com/abstract=264437.

[13] R.J. Kauffman, T.J. Spaulding, C.A. Wood, Are online auction markets ef<sup>fi</sup>cient? An empirical study of market liquidity and abnormal returns, Decision Support Systems 48 (1) (2009) 3–13.

[14] G. Ku, A.D. Galinsky, J.K. Murnighan, Starting low but ending high: a reversal of the anchoring effect in auctions, Journal of Personality and Social Psychology 90 (6) (2006) 975–986.

[15] A.M. Kwasnica, J.O. Ledyard, D. Porter, C. DeMartini, A new and improved design for multiobjective iterative auctions, Management Science 51 (2005) 419–434.

[16] R. Leskelä, J. Teich, H. Wallenius, J. Wallenius, Decision support for multi-unit combinatorial bundle auctions, Decision Support Systems 43 (2) (2007) 420–434.

[17] A. Lin, J. Teich, P2P lending — a credit revolution? New Mexico business outlook, NMSU College of Business, July 2006.

[18] D. Lucking-Reiley, D. Bryan, N. Prasad, D. Reeves, Pennies from eBay: the determinants of price in online auctions, Journal of Industrial Economics 55 (2) (2007) 223–233.

[19] R.P. McAfee, J. McMillan, Auctions and bidding, Journal of Economic Literature 25 (2) (1987) 699–738.

[20] P.R. Milgrom, R.J. Weber, A theory of auctions and competitive bidding, Econometrica 50 (5) (1982) 1098–1122.

[21] R.S. Pindyck, D.L. Rubinfeld, Econometric models and economic forecasts, McGraw-Hill, Boston, 1997.

[22] Prosper.com, “Listing Summary for Listing Number #385755”, 2008, http://www. prosper.com/lend/listing.aspx?listingID=385755/, viewed September 5th 2008.

[23] T. Sueyoshi, G.R. Tadiparthi, An agent-based decision support system for wholesale electricity markets, Decision Support Systems 44 (2) (2008) 425–446.

[24] J.E. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, A multi-attribute e-auction mechanism for procurement: theoretical foundations, EJOR 175 (1) (2006) 90–100.

[25] D. Van Heijst, R. Potharst, M. Van Wezel, A support system for predicting eBay end prices, Decision Support Systems 44 (4) (2008) 970–982.

[26] J. Zhang, The roles of players and reputation: evidence from eBay online auctions, Decision Support Systems 42 (3) (2006) 1800–1818.

Lauri Puro is a recent MSc (Eng.) graduate from the Department of Industrial Engineering and Management, Helsinki University of Technology.

Jeffrey E. Teich holds a PhD from the State University of New York at Buffalo. He is Professor at New Mexico State University. His research interests focus on negotiation analysis and online auctions, in particular procurement auctions, as well as decision support.

Hannele Wallenius holds a PhD from the University of Jyväskylä, Finland. She is Professor and Department Head, Department of Industrial Engineering and Management, Aalto University School of Science and Technology and Vice Dean of her college. Her research interests focus on negotiation analysis, online auctions, in particular procurement auctions, decision support, and multiple criteria decision making.

Jyrki Wallenius holds a PhD from the Helsinki School of Economics. He is Professor and Department Head, Department of Business Technology, Aalto University School of Economics. He is a former editor in chief with the European Journal of Operational Research. Wallenius is the current President of the International Society on Multiple Criteria Decision Making, His research interests focus on negotiation analysis, online auctions, in particular procurement auctions, multiple criteria decision making decision support, and behavioural decision theory. Recipient of numerous awards, international and domestic
