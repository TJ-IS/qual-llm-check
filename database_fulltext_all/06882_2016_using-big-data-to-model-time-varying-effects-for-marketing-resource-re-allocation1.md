---
otero_id: 6882
otero_key: "KR4Z2B64"
title: "Using Big Data to Model Time-Varying Effects for Marketing Resource (Re)Allocation1"
authors: "Alok R. Saboo; V. Kumar; Insu Park"
year: "2016"
journal: "MIS Quarterly"
doi: "10.25300/misq/2016/40.4.06"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# USING BIG DATA TO MODEL TIME-VARYING EFFECTS FOR MARKETING RESOURCE (RE)ALLOCATION<sup>1</sup>

Alok R. Saboo, V. Kumar, and Insu Park

J. Mack Robinson College of Business, Georgia State University, Atlanta, GA 30303 U.S.A. {asaboo@gsu.edu} {vk@gsu.edu} {ipark8@gsu.edu}

Marketing resource allocation has been a topic of intense scrutiny, yet the literature on the topic has not paid adequate attention to the fact that the effectiveness of marketing-mix elements varies over time. Despite the fact that firms collect volumes of data on their customers, existing estimation approaches do not readily lend themselves to modeling the temporal variations for big data and provide little guidance to managers in terms of their resource allocation decisions. We address this gap and argue that marketing-mix effectiveness varies with the evolution of the consumer–brand relationship and explicitly model these temporal variations using a time-varying effects model (TVEM) that accounts for self-selection of customers into receiving marketing communications and endogeneity of the number of such communications. The proposed TVEM framework handles the complexities associated with big data analytics and provides novel insights for data-driven decision making. We combine transaction data from a Fortune 500 retailer with demographic information obtained from Acxiom Corp for over a quarter million customers to test our framework. The results provide strong support for our proposed framework. Specifically, we find that the influence of marketing mailers, other transaction characteristics (coupon redemption, returns, and cross-buy), and demographic factors (age, income, household size, and interests) on sales varies significantly over the customer life cycle and ignoring such temporal variations can lead to gross misallocation of marketing investments. Specifically, our results suggest that firms can increase their revenues by over 17 percent by just reallocating their resources based on the proposed framework. To facilitate adoption of our proposed framework, we provide guidance and actionable insights for managerial relevance.

Keywords: Time-varying effect model, TVEM, big data, dynamic marketing resource allocation, time series models, dynamic models, marketing-mix effectiveness, direct marketing

## Introduction

Firms have long been concerned with optimizing resource allocation across marketing activities such as advertising, promotions, incentives, or direct marketing to influence outcomes of interest (e.g., sales, employee turnover, and customer engagement). Firms typically base their resource allocation decisions on the effectiveness of their marketing investments such that a marketing input with a higher effectiveness (e.g., higher sales) gets more allocation than the one that is less effective (Raman et al. 2012). However, such rules of thumb can be misleading considering that marketingmix effectiveness varies over time. For example, the product life cycle theory suggests that consumers are responsive to advertising in the early stages when they are looking for information, whereas they respond to promotions in the maturity stage (e.g., Parsons 1975). Similarly, marketing-mix effectiveness can change due to other market events such as entry of new competitors (Pan and Lehmann 1993), advances in technology (Chen and Stallaert 2014), or regulatory changes (Stremersch and Lemmens 2009). Finally, the effectiveness of marketing-mix elements can change due to the evolution of the consumer–brand relationship that evolves after every interaction. All these factors suggest that resource allocations based on historical performance can be counterproductive and that managers should continuously reallocate marketing resources based on the expected returns (Kumar 2013). This frequent reallocation of marketing resources, although demanding, has been shown to provide superior shareholder returns in a recent study by McKinsey & Company (Fruk et al. 2013).

Real-time adjustment in organizational strategies requires continuous measurement and analysis of data to make information usable at a higher frequency. Fortunately, firms are now collecting huge amounts of data on their consumers and should be able to use that information to reallocate resources. Whereas the answer to “how much data is big” may vary by organizational size, the objective is to create value from the analysis of their data to provide novel insights. Yet, academics have not offered any systematic mechanism that handles the challenges associated with big data and generates real-time intelligence to guide this dynamic resource allocation problem—a gap that we seek to address through this research (e.g., Goes 2014).

Several theories explain the phenomenon through which the effectiveness of marketing inputs varies with changes in the consumer–brand relationship. As consumers become familiar with a brand either through external information (i.e., advertising) or product usage, their knowledge structure about the firm changes and decreases the uncertainty about the firm, affecting their price perceptions, purchase intentions, and willingness to pay (e.g., Rao and Monroe 1988). However, research on usage dominance suggests that once consumers become familiar with a brand and have tried the same, their personal usage experience dominates all external information as an input into the purchase decision, suggesting a reduction in effectiveness of advertising for future purchase decisions (Deighton et al. 1994). This finding is consistent with Hoch and Ha’s (1986) framing experiment where they find that advertising had no effect on the attitudes of participants who were allowed to experience the product. Similarly, psychological concepts such as habit or inertia have been documented to influence consumer purchases over time (e.g., Dubé et al. 2010). For instance, Givon and Horsky (1990) find that purchase reinforcement and habitual loyalty effects are stronger than advertising carryover effects. Thus, although there is enough evidence that marketing-mix effectiveness changes over the customer life cycle as customers learn about the firm, we are not aware of any empirical study that investigates this topic and provides managerial guidance for implementation.

We propose a time-varying effects model (TVEM) that utilizes big data to explicitly account for temporal variations (due to a variety of factors such as inertia, habit, etc.) in consumer responsiveness to a firm’s direct marketing efforts so as to enhance the ROI on marketing on a real-time basis and make both methodological and substantive contributions. Specifically, traditional methodological approaches such as panel data regression models ignore the potential variations in the impact of direct marketing efforts on sales over time and may yield misleading or, worse, incomplete insights. As an alternative approach, we use the advances in time-varying effect analysis to model the coefficients (or the parameter estimates) as a smooth (continuous) function of time (Tan et al. 2012). Further, instead of using multilevel models that impose strong parametric assumptions about the nature of change in the relationship between the two variables, we use nonparametric techniques to model the coefficient functions. The proposed TVEM framework relies on nonparametric assumptions that require large volumes of data for estimation and hence is an ideal candidate for a big data context. Thus, TVEM offers an alternate approach to the functional regression analysis, which is designed for sparse longitudinal data, where both the predictor and response are functions of a covariate such as time (Shi and Choi 2011). Of greater importance, our estimation methodology overcomes the limitations of the existing approaches highlighted by Leeflang et al. (2009). First, unlike other methodologies such as the moving window regression (Mahajan et al. 1980) or the piecewise regression (Parsons 1975) that employ arbitrary windows or utilize only a subset of the data each time, we recover the true functional form by using nonparametric techniques. We also improve upon alternative time-varying parameter models that make assumptions about the shape of the time-varying process (e.g., Foekens et al. 1994) or a priori distinguish between the effectiveness of marketing instruments based on known information such as performance regimes (Pauwel and Hanssens 2007). Our approach is immune to errors caused by incorrect specification as we do not rely on any a priori information about the shape of the time-varying proces or make any “arbitrary distinction” between performance regimes (Osinga et al. 2010, p. 175). Also, unlike Kalman filtering or dynamic linear models (DLM) that are based on state-space modeling, our approach does not assume any pre specified number of underlying states and does not take “several hours or days” to estimate despite the large transaction dataset (Leeflang et al. 2009, p. 15).

We illustrate the value of incorporating the time-varying effects of marketing inputs using a large dataset from a Fortune 500 national retailer. Our dataset comprises of over a quarter million unique customers (N = 281,150) and offers a wide variety of customer information including online and offline transactions recorded between 2007 and 2010, qualitative data regarding customers’ preferences, and demographic information. The large dataset, as we discuss subsequently, has all the principal characteristics of big data (i.e., high volume, velocity, and variety), and is in line with the demands placed by our nonparametric estimation approach that requires the estimation of additional parameters. Although the large dataset is difficult to store and analyze using existing methods, it is in line with organizational realities where firms have volumes of transaction data and are looking for ways to generate meaningful insights from it. Our time-varying approach efficiently models the effects of marketing inputs over time and the heterogeneity across customers, and, most importantly, provides actionable insights to managers. The proposed model is superior to alternate specifications and can be easily estimated within seconds or minutes (depending on the size of the data); we provide the required code for managers to implement our model using their existing infrastructure. Our results provide strong support to our framework that suggests that the effectiveness of marketing-mix elements varies over time and highlight how firms can increase their returnon-investment by incorporating these temporal variations in their resource allocation strategy. More importantly, our results are also managerially significant. Specifically, firms can increase their returns on marketing investment by over 17% by reallocating their resources in line with the proposed TVEM model without making any other changes, thereby preventing the misallocation of scarce marketing resources across customers, thus saving millions of dollars.

In summary, our TVEM approach is easy to implement within existing organizational infrastructure and provides novel insights, helping firms in analyzing and exploiting big data to increase firm value. Firms “struggling with understanding and deciding” (Goes 2014, p. vi) how to use big data for decision making can easily employ our framework for real time strategic decision making. Specifically, our research directly helps firms in four broad ways in which they can use big data to create value (e.g., Manyika et al. 2011). First, our approach can unlock significant value by making information usable at much higher frequency, allowing firms to change their strategies in real time. Second, as firms create and store more data about customers, our approach provides a more accurate and detailed description of how various factors such as transaction characteristics or demographic factors influence the desired outcomes and how the influence of these factors varies over time, allowing firms to make better decisions and adjust their business levers accordingly.<sup>2</sup> Third, our TVEM methodology allows firms to have a deeper understanding of consumer decision criteria and, in turn, precisely tailor their products or services. Fourth, our approach can substantially improve decision making and allow firms to reallocate their scarce resources efficiently. Overall, our TVEM approach is flexible enough to allow firms to use big data for basic lowfrequency forecasting to high-frequency nowcasting, for improving firm performance (Manyika et al. 2011). We are not presenting TVEM as a replacement to other longitudinal estimation techniques. We believe that TVEM should be viewed as another tool in the toolkit of scholars working on longitudinal data that offers significant value without much up-front costs.

We organize the remainder of the paper as follows. We begin by providing some motivation for our research question. Then, we discuss the basic logic behind the concept of timevarying effects modeling (or TVEM). Next, we describe in detail the estimation of such models, where we provide alternative estimation algorithms. Then, we discuss the data employed in this research and comment on the data-related opportunities and challenges associated with TVEM estimation. Thereafter, we discuss our results, and the implications of our research for both scholars and managers. We conclude with the limitations and future directions of this research.

## Motivation

## Substantive Perspective

Marketing resource allocation has gained prominence as managers are under increasing pressure to deliver results on tighter budgets. As firms limit the size of their marketing budgets, marketers must find ways to maximize the impact of their marketing dollars. Scholars have produced a rich body of literature that offers both methodological and substantive insights into the complex decisions related to marketing resource allocation. The broad theme in this stream of research is to assess the impact of marketing actions on consumer demand so as to adjust marketing resource allocation (across medium, channels, functions, geographies, products, customers, etc.) to increase firm value (Gupta and Steenburgh 2008). We briefly summarize the key themes across this research domain (interested readers should refer to review articles by Gupta and Steenburgh 2008; Kumar and Reinartz 2012; Rust et al. 2004; Shankar 2008).

The dominant theme across the marketing resource allocation domain is to identify factors that can explain and influence consumer response to marketing actions and use those insights to help managers in their resource allocation decisions. Along those lines, scholars have proposed transaction characteristics such as recency, frequency, and monetary value (e.g., Venkatesan and Kumar 2004), shopping characteristics such as return behavior (Anderson et al. 2009; Petersen and Kumar 2009) or shopping across multiple channels (Venkatesan et al. 2007; Verhoef et al. 2010), attitudinal characteristics such as satisfaction (Bendapudi and Berry 1997; Seiders et al. 2005) or loyalty (Lewis 2004; Stern and Hammond 2004), and organizational marketing efforts (Elsner et al. 2004; Manchanda and Chintagunta 2004) to explain the differences across consumer purchases. Using the insights thus gained, scholars have examined how marketing resources should be allocated across customers (Elsner et al. 2004; Kumar et al. 2013) and marketing activities such as customer acquisition and retention (Berger and Bechwati 2001; Reinartz et al. 2005), advertising and sales (Naik and Raman 2003), or value creation and appropriation (Mizik and Jacobson 2003); and markets or geographies (Elberse and Eliashberg 2003). Many of these tools or methodologies have been made available to managers to help them with their resource allocation decisions (e.g., Divakar et al. 2005; Elsner et al. 2004; Shankar et al. 2008).

Despite the significant advances in the resource allocation domain and wide acceptance of the fact that firms that strategically reallocate resources frequently based on marketplace considerations deliver superior returns (Fruk et al. 2013), a recent study by McKinsey & Co. highlights that companies continue to allocate resources based on historical allocations and rules of thumb (Doctorow et al. 2009). This is partly because the “models for dynamic resource allocation typically assume that marketing effectiveness is constant over time” (Raman et al. 2012, p. 44), an assumption that may not stand up to scrutiny. Scholars are beginning to acknowledge that the effectiveness of marketing instruments may not be constant over time and some have even explicitly modeled the same (Osinga et al. 2010), yet a majority of such studies focus on long-term effects and do not investigate the decisions that managers must make routinely (e.g., Slotegraaf and Pauwels 2008). For instance, managers must decide on the amount of resources that they need to allocate to each customer in the coming week or month and they can maintain their historic allocations or reshuffle their allocations across customers. Most academic studies overlook such short-term decisions, providing little guidance to managers who then, not surprisingly, are very “slow to reshuffle their resources,” resulting in poor firm performance (Fruk et al. 2013, p. 56). This is frustrating as firms spend huge resources in collecting volumes of data on their customers, yet most companies struggle to take advantage of their big data resources in decision making, in part due to the lack of methods that can be easily implemented in the big data realm within the existing organizational infrastructure (Chen et al. 2012; Goes 2014).

## Methodological Perspective

Our study focuses on short-term resource allocation decisions and seeks to provide some guidance to managers in their reallocation decisions. Consider a simple market response model in the most general form where each customer can have different measurement occasions and measurement window sizes:

$$
S _ {i j} = \beta_ {0} + \beta_ {1} \times X _ {i j} + \varepsilon_ {i j}; i = 1, \dots , n, j = 1, \dots , m _ {i}\tag{1}
$$

where, $S _ { i j }$ is the sales (or other outcome variable) for customer i measured at time $t _ { i j } , X _ { i j }$ is marketing input (e.g., advertising) for customer i measured at time $t _ { i j } ,$ n represents the total number of subjects, $m _ { i }$ is the number of repeated observations for subject $i , ^ { 3 } t _ { i j }$ is the measurement time of the $j ^ { \mathrm { t h } }$ observation for subject $i ,$ that is, $t _ { i j }$ are the different measurement occasions for subject i, and random errors $\mathcal { E } _ { i j }$ are assumed to be normally and independently distributed.<sup>4</sup>

The model in Equation 1 is akin to some of the initial models in this space (e.g., Parsons and Schultz 1976) and assumes constant parameter estimates, for instance, the effectiveness of advertising remains constant. However, not only can the intercept, $\beta _ { 0 } ,$ , vary over time due to market conditions, other response parameters, $\mathcal { \beta } _ { 1 }$ , also evolve over time due to a variety of factors (e.g., changes in consumer preferences, competitive landscape, or economic conditions) (Leeflang et al. 2009; Raman et al. 2012).

One way to incorporate the temporal variations in the relationship between the variables of interest is to use multilevel or hierarchical modeling and include the interactions with time or an explicit process function (e.g., Foekens et al. 1994; Mela et al. 1998). We can extend Equation 1 and write a simple multilevel linear regression model as:

$$
S _ {i j} = \beta_ {0 0} + \beta_ {0 1} t _ {i j} + (\beta_ {1 0} + \beta_ {1 1} t _ {i j}) X _ {i j} + \varepsilon_ {i j}\tag{2}
$$

where we rewrite $\beta _ { 0 }$ and $\beta _ { 1 }$ from Equation 1 as functions of time $t _ { i j } ,$ where $t _ { i j }$ is the measurement time of the $j ^ { \mathrm { t h } }$ observation for subject $i ,$ such that $\beta _ { 0 } = \beta _ { 0 0 } + \beta _ { 0 0 } t _ { i j }$ and $\beta _ { 1 } = \beta _ { 1 0 } + \beta _ { 1 1 } t _ { i j }$

Traditionally, scholars assume a shape of the coefficient functions such as linear, quadratic, or exponential. Since there is a range of admissible functional forms, the chosen functional form is almost surely mis-specified (Bierens and Pott-Buter 1991). Such a specification can be justified for panel data with small number of repeated observations where there is limited information to recover the true shape of relationship change. However, with the advent of big data, existing statistical methods that force the data into a prespecified shape may be incapable of providing a comprehensive understanding of the phenomenon. Such mis-specifications will typically result in inconsistent parameter estimates and, consequently, an incomplete, or worse, incorrect, understanding of the mechanisms of change.

The accurate portrayal of the coefficient functions provides information about (1) the shape of change and (2) peaks and troughs in the change function, which can provide an accurate depiction of how the relationship evolves over time and help managers make better decisions. Since the only way to avoid functional misspecification is to not use a functional form at all, we use nonparametric methods to let the functional form of the change function be determined by the data. Nonparametric methods have been widely used to alleviate the problems related to functional misspecification (Hollander et al. 2013), including in marketing (Leeflang et al. 2009).

## Proposed Modeling Approach

We demonstrate the merits in using time-varying effect models (TVEM) that are free of problems related to functional misspecification and recover the shape of coefficient functions using the data.<sup>5</sup> The TVEM framework provides an ideal approach to model the continuously evolving nature of the customer–brand relationship as it assumes that these functions are smooth (i.e., with no sudden jumps or break points) and does not pose any parametric assumptions on the coefficient functions.<sup>6</sup> TVEM models are an extension of the varying coefficient model proposed by Hastie and Tibshirani (1993) that allows estimating the coefficients of a variable as a smooth function of other variables. Instead of assuming constant parameter estimates (such as in Equation 1), these models increase the flexibility of linear regression models by allowing their coefficients to vary smoothly as a function of other variables. Thus, we can rewrite Equation 1 in a more general form as:<sup>7</sup>

$$
S _ {i j} = \beta_ {0} (r _ {0}) + X _ {i j} \beta_ {1} (r _ {1}) + \varepsilon_ {i j}\tag{3}
$$

where $X _ { i j }$ is the covariate, $\beta _ { 0 } ( r _ { 0 } )$ and $\beta _ { 1 } ( r _ { 1 } )$ are the associated coefficient functions such that the intercepts and the coefficients of $X _ { i j }$ vary with the values of $r _ { 0 }$ and $r _ { 1 }$ respectively. When the coefficient function is specified as a function of time, the varying coefficient model reduces to the special case of TVEM (using notations in Equation 2):

$$
S _ {i j} = \beta_ {0} (t _ {i j}) + \beta_ {1} (t _ {i j}) X _ {i j} + \varepsilon_ {i j}\tag{4}
$$

where $\beta _ { 0 } ( t _ { i j } )$ and $\beta _ { 1 } ( t _ { i j } )$ are assumed to be the continuous coefficient functions (i.e., they are continuous over the range of $t _ { i j } ) _ { : }$ , and the model suggests that the influence of $X _ { i j }$ on $S _ { i j }$ varies over time $t _ { i j } ,$ where $t _ { i j }$ is the measurement time of the $j ^ { \mathrm { { i } } \mathrm { { \check { h } } } }$ observation for subject i. This flexible model allows the timevarying effects of the covariates without assuming parametric functions.

TVEMs can estimate the changing relationship between a time-varying parameter and the dependent variable over time without making any assumptions with respect to the shape of the trajectories of the variables (Tan et al. 2012). TVEMs are “conditionally parametric because the time-varying parameters are nonparametric functions, whereas the model is parametric for a specified $t ^ { \dag }$ (Stremersch and Lemmens 2009, p. 700). The semiparametric approach is a good compromise between parametric models that are usually restrictive and less robust when the model is incorrectly specified and nonparametric models that are usually more complex and less efficient (Wu and Zhang 2006). This freedom comes at a price: We need a lot more data to fit a TVEM framework than that required by a parametric model (Leeflang et al. 2000). Fortunately, big data provides the required resources to encourage the application of such models. While the data required may be large, the suggested modeling approach takes much less time to estimate than other models such as dynamic linear models or Kalman-filtering.

## Data Description

The empirical context for our research is a large Fortune 500 retailer selling a wide assortment of products related to home improvement, gardening needs, furniture, and home appliances. For reasons of confidentiality, we cannot reveal the name of the retailer. The retailer operates more than 1,000 stores across the United States and stocks an average of 20,000 items per store with prices ranging from a few cents to several thousand dollars. The retailer started a loyalty club for its customers and we obtain our data from the members of this club. The company targets the members of this club through mailers (which is operationalized as the number of direct mail and emails sent to each customer). Given that the retailer has a fixed direct marketing budget, it currently allocates resources on the basis of the nature of customers (e.g., business versus retail customers).<sup>8</sup> Direct mail serves two primary purposes: providing product or marketing information and providing a purchase trigger. However, as customers become familiar with the firm and its offerings, the value of such marketing communications change. In addition, customers’ responsiveness to the firm’s marketing communications tends to vary with customers’ demographics and their transaction histories. These factors should be duly incorporated in a firm’s mailing strategy.

Accordingly, we obtain transaction data for 1.3 million unique customers who do not have a prior relationship with the firm over a three-year time period from 2007 to 2010. The data provide rich information on customer purchases, including instore and online transaction details such as the time of purchase, store location, purchase amount, number of items purchased, cross-buy, and the number of product returns. We also have data on firm-initiated marketing communications (e.g., direct mail, coupons, and emails), and customers responses to those communications. In addition, we were able to augment the transaction data with customer characteristics, which include age, income, marital status, population density, interests, and several others for 0.9 million out of the 1.3 million unique customers through our collaboration with Acxiom Corp., resulting in a SAS dataset of over 9.5 GB.

We drop a small number of customers from the dataset with poor coverage of the customer characteristics obtained through Acxiom, resulting in a dataset of approximately 0.76 million customers. We identify and remove any outliers. For the purpose of this study, we focus on a specific segment of customers and hence exclude B2B customers from our analysis as there may be other factors that influence their relationships with the firm (e.g., account executives). In line with our objectives to measure the influence of marketing communications, we also exclude customers who have optedout of any marketing communications from the retailer.<sup>9</sup> We observe the behavior for these customers over a period of 36 months and have data on their transactions as well as marketing interactions over the period. This time frame is well beyond the recommendation of at least 10 periods for estimating time-varying models (Tan et al. 2012; Walls et al. 2006). Our final dataset includes 36 months of customerlevel information for 281,150 unique customers with 10,121,400 customer-month observations.<sup>10</sup>

In line with Goes (2014) and Zikopoulos et al. (2012), our data have all the characteristics of big data: (1) large volume of information (detailed customer transaction records for 281,150 customers), (2) variety of information (e.g., online and offline transactions, qualitative information on preferences, demographics, and customer characteristics), and (3) high velocity (transaction summary across entire retail network recorded in real time). Specifically, our original dataset has a large number of customers and detailed transaction information on them, which represents the high volume property. Further, the sales transactions are recorded in real time at the point-of-purchase, which present high velocity property. Finally, by incorporating the information on households’ characteristics (e.g., demographics and qualitative information on preferences) from Acxiom’s database into the firm’s sales data, our dataset obtains the variety property. The availability of big data offers enough statistical power to empirically detect the temporal variations in marketing effectiveness.

The sheer volume of our data also presents several computation challenges. We employed the latest versions of scalable analytics software packages (SAS 9.3 and STATA 13) running on a Dell Supercomputer with 512GB RAM (most modern machines have around 8GB RAM), 10TB of hard drive, and a Dual Eight Core XEON processor for our empirical analyses. Neither of the analytics software packages impose any limit on the size of the dataset from a computational standpoint as long as the hardware (memory and processing speed) is adequate.

## Key Variables

We describe the key variables for our study in this section. We use the total amount of dollar sales (SALES) from each customer per month as our dependent variable. The key independent variable in this study is the number of mailers, physical as well as electronic, sent to each customer per month (MAILS). All loyalty-club customers receive anywhere from 1 to 30 (with an average of 4.43) mailers from the retailer in a month. These mailers typically include productrelated information and some coupons. If customers redeem these coupons, the transaction is recorded at their point-ofpurchase. In line with the literature that suggests that promotions (i.e., coupons) influence overall sales (e.g., Venkatesan and Farris 2012), we include the number of coupons redeemed (REDEEM) in our model.<sup>11</sup> Coupon redemption varies from 0 through 20 (with an average of 0.027), and provides us with a means to capture the differences in the prices paid by customers.

<table><tr><td>Variables</td><td>Descriptions</td></tr><tr><td>Sales (SALES)</td><td>Total amount of dollars spent each month</td></tr><tr><td>Mails (MAILS)</td><td>Number of mailers (e-mails and direct mails) received by the customer</td></tr><tr><td>Coupons Redeemed (REDEEM)</td><td>Number of coupons redeemed</td></tr><tr><td>Returns (RETURNS)</td><td>Number of products returned</td></tr><tr><td>Crossbuy (CROSSBUY)</td><td>Number of categories across which customer shops in a given month</td></tr><tr><td>Population density (PDENS)</td><td>12-point Likert scale from 1 (very rural) to 12 (very urban).</td></tr><tr><td>Seasonality (SEASON)</td><td>Dummy variable that equals 1 if the month of transaction is April or May and 0 otherwise</td></tr><tr><td>Financial stability (FSTABILITY)</td><td>12-point Likert scale from 1 (financially very unstable) to 12 (financially very stable)</td></tr><tr><td>Household size (HSIZE)</td><td>Number of people in the household</td></tr><tr><td>Interest in gardening (GARDEN)</td><td>Dummy variable that equals 1 if a customer is interested in gardening and 0 otherwise</td></tr><tr><td>Interest in home improvement (DECOR)</td><td>Dummy variable that equals 1 if a customer is interested in home improvement and 0 otherwise</td></tr><tr><td>Marriage (MARRIAGE)</td><td>Dummy variable that equals 1 if a customer is married and 0 otherwise</td></tr><tr><td>Age (AGE)</td><td>Age of the customer</td></tr><tr><td>Online purchases (ONLINEPURCH)</td><td>Dummy variable that equals 1 if a customer makes online purchases and 0 otherwise</td></tr><tr><td>Interest in general reading (MGEN)</td><td>Dummy variable that equals 1 if a customer is interested in general reading and 0 otherwise</td></tr><tr><td>Interest in news and political reading (MPOL)</td><td>Dummy variable that equals 1 if a customer is interested in news and political reading and 0 otherwise</td></tr><tr><td>Mail order responder (MOR)</td><td>Dummy variable that equals 1 if a customer responds to mail orders and 0 otherwise</td></tr></table>

Besides firm-initiated marketing communications, the customer-brand relationship develops through prior interactions with the firm such as purchases or returns (Petersen and Kumar 2009). Thus, we also include the total product returns (RETURNS) and cross-buy (CROSSBUY) in our framework. We measure product returns as the number of products returned in a month and cross-buy as the number of different product categories that a customer has bought from the firm. We also include demographic and socio-economic factors that may influence customer purchases in the home improvement, gardening, and construction category; we obtain this data through our research collaboration with Acxiom Corp. Specifically, we include population density (PDENS) measured on a 12-point scale, seasonality (SEASON) that equals 1 for summer months or moving season (April and May) and 0 otherwise, financial stability index (FSTABILITY) measured on a 12-point scale ranging from 1 (financially very unstable) to 12 (financially very stable), and household size (HSIZE) indicating the total number of people in the household ranging from 1 to 9 (indicating 9 or more people in household). See Table 1 for a summary of all our variables.

## Model Development

In this section, we discuss the issues that guide our estimation approach. First, an important consideration in testing our framework is an alternative explanation of customer selfselection. This explanation suggests that customers receiving the firm’s marketing communications may have greater preference for its products than those that opt out of such communications, and this difference rather than marketing communications may be driving sales. Second, and a related issue, are concerns regarding the potential endogeneity of the mailers received by customers. Firms choose their mailing strategy based on customer characteristics (i.e., the number of mailers sent to a customer may not be exogenous).<sup>12</sup> Finally, as discussed earlier, the goal of our TVEM model is to reveal the shape of the smooth coefficient function over time. Accordingly, we discuss our approach for estimating the unknown coefficient function.

## Accounting for Selection Bias

We use the Heckman two-step method that has been shown to be an effective approach to check and correct for potential self-selection bias (Heckman 1979). The first stage involves a probit model on the probability of opting out of retailers’ marketing communications. Let $z _ { i } ^ { O p t }$ constitute the set of exogenous variables that influence the customers’ choice of opting out of marketing communications. In line with prior studies in this domain (e.g., Kumar et al. 2014), we include a range of demographic and psychographic variables that are likely to influence customers’ choice. Specifically, we include age of the head of the household (AGE), household size (HSIZE), financial stability (FSTABILITY), marital status (MARRIAGE), and population density of the area in which they live (PDENS). We also include some psychographic variables such as whether the customers are interested in gardening (GARDEN), home improvement (DECOR), general reading (MGEN), news and politics (MPOL), and whether they make online purchases (ONLINEPURCH). Thus, we specify the following first stage probit model:

$$
O p t _ {i} ^ {*} = z _ {i} ^ {O p t} \lambda^ {O p t} + \eta_ {i} ^ {O p t}\tag{5}
$$

where $O p t _ { i } ^ { * }$ denotes the latent measurement, and the observed binary response for the $i ^ { \mathrm { t h } }$ customer is the indicator $O p t _ { i } =$ $I \{ O p t _ { i } ^ { * } > \bar { 0 } \} ; \lambda ^ { O p t }$ is the unknown parameter vector; $z _ { i } ^ { O p t }$ is a vector of exogenous variables; and the random error $\eta _ { i } ^ { O p t }$ is assumed to be normally distributed.

Next, we use the estimates $\operatorname { o f } \ z _ { i } ^ { O p t }$ from Equation 5 and the resultant estimates of $z _ { i } ^ { O p t } \lambda ^ { O p t }$ to compute the inverse Mills ratio (correction term; IMR) for each observation (e.g., Saboo et al. 2016) as follows:

$$
\begin{array}{l l} I M R _ {i} = \phi \Big (z _ {i} ^ {O p t} \lambda^ {O p t} \Big) / \Phi \Big (z _ {i} ^ {O p t} \lambda^ {O p t} \Big); & \text { if } O p t = 1 \\ I M R _ {i} = - \phi \Big (z _ {i} ^ {O p t} \lambda^ {O p t} \Big) / \Big [ 1 - \Phi \Big (z _ {i} ^ {O p t} \lambda^ {O p t} \Big) \Big ]; & \text { if } O p t = 0 \end{array}\tag{6}
$$

where  and Φ are are the probability density function and the cumulative distribution function of the standard normal distribution, respectively.

Then, we include the correction term (IMR) as additional variables in our final model. Although the model is identified by the nonlinearity of the Inverse Mills Ratio, for better identification, we exclude three variables including whether they make online purchases in general (ONLINEPURCH), whether they are interested in general reading (MGEN) or news and politics (MPOL) from our final model to meet the exclusion restriction. Both MGEN and MPOL should influence customers’ desire to receive and read mailers, but consumers’ reading habits are less likely to influence their purchases. Similarly, online purchases (ONLINEPURCH) should encourage customers to receive and read mailers, but should not influence total purchases as customers also make offline purchases, an assumption that is also empirically validated by the low correlation (ρ = -.005) between these variables.<sup>13</sup>

## Accounting for Endogeneity of Mailers

As is common in the literature, we use a control function approach to model the potential endogeneity of a firm’s mailing strategy (e.g., Petrin and Train 2010; Wang et al. 2015). Firms base their mailing strategy on the basis of customer characteristics and with an explicit objective to increase sales, suggesting that number of mailers received by a customer may be endogenous. We use the control function approach as proposed by Garen (1984) to correct for any such endogeneity.<sup>14</sup>

The control function approach requires two-stage estimation, wherein we estimate the correction term in the first stage by regressing the endogenous variable, MAILS, on a set of exogenous variables (e.g., Wang et al. 2015). Let $z _ { i j } ^ { M A I L S }$ be a vector of exogenous variables that influence the organizational choice of the number of mailers sent to the customer i in period j. Extant research suggests that customer characteristics and previous transactions influence organizational mailing strategy (e.g., Elsner et al. 2004); for example, customers who purchase frequently and in large quantities are likely to receive more mailers (Gönül and ter Hofstede 2006). Accordingly, we include customer characteristics and recent transaction history as explanatory variables that may influence organizational mailing strategy. Specifically, in terms of transaction characteristics, we include lagged sales $( S A L E S _ { i j - 1 } )$ , mailers sent in the previous period $( \overline { { M A I L S } } _ { i j - 1 } ) ,$ 15 lagged coupons redeemed $( R E D E E M _ { i j - 1 } )$ , lagged products returned $( R E T U R N S _ { i j - 1 } )$ , and the number of product categories that a customer purchased in the previous period $( C R O S S B U Y _ { i j - 1 } )$ We also include customer characteristics that should influence the mailing decision such as age (AGE), financial stability (FSTABILITY), household size (HSIZE), population density of the area they live in (PDENS), marital status (MARRIAGE), interest in gardening (GARDEN) or home improvement (DECOR), and whether the customer is interested in mail orders (MOR). Finally, given the seasonal nature of our product category, we also include seasonality (SEASON) to indicate the summer months or moving season (April and May). Thus, we specify:

$$
M A I L S _ {i j} = z _ {i j} ^ {M A I L S} \lambda^ {M A I L S} + \eta_ {i j} ^ {M A I L S}\tag{7}
$$

on deriving a proxy variable that partitions the endogenous variable into endogenous and exogenous components (Petrin and Train 2010). The control function approach requires modeling the endogenous variable (e.g., MAILS) using a set of exogenous variables, including the excluded variable, in the first stage regression and using the residuals from this stage in the second stage as a regressor with the assumption that the errors of the two stages follow a bivariate normal distribution (Luan and Sudhir 2010; Wooldridge 2010). Inclusion of the first stage residuals in the second stage “solves the endogeneity problem regardless of how the endogenous regressor appears” (Imbens and Wooldridge 2007, p. 12), offering distinct advantages for models nonlinear in endogenous variables. Having said that, we estimated another model using the classical IV method (2SLS approach) and, not surprisingly, obtained identical results to those reported in the manuscript. Moreover, the AIC and BIC values of the proposed model (using control function approach) is marginally lower (or better) than the ones with the IV approach.

where $M A I L S _ { i j }$ indicates the number of mailers sent to customer i in period $j , \lambda ^ { M A I L S }$ is the unknown parameter vector, $z _ { i j } ^ { M A I L S }$ is a vector of exogenous variables specified earlier, and the random error $\eta _ { i j } ^ { M \dot { I } L S }$ is assumed to be independently and normally distributed.

We obtain consistent estimates of $\lambda ^ { M A I L S }$ and then use the residuals $\hat { \eta } _ { i j } ^ { M A I L S }$ for mailers as additional explanatory variables in our final model shown in Equation 8. For model identification purposes, we exclude the dummy variable that indicates whether the customer is interested in mail orders (MOR) from the second stage model shown in Equation 8. Interest in mail orders is likely to be related to the number of mailers received by the customer, but less likely to be related to final sales, which can be confirmed by the relatively low correlation between interest in mail orders and sales as compared to that between interest in mail orders and the number of mailers received. The final model that we estimate is

$$
S _ {i j} = \beta_ {0} (t _ {i j}) + \beta_ {1} (t _ {i j}) X _ {i j} + \gamma_ {1} \hat {\eta} _ {i j} ^ {M A I L S} + \gamma_ {2} I M R _ {i} + \varepsilon_ {i j}\tag{8}
$$

where $\gamma _ { 1 }$ and $\gamma _ { 2 }$ are the coefficients for the correction terms.

## Estimation of Time-Varying Effect Model

In this section, we focus on the estimation of unknown coefficient functions, intercept $\beta _ { 0 } ( t _ { i j } )$ and slope $\beta _ { 1 } ( t _ { i j } )$ in Equation 8. Smoothing methods have been widely used to estimate unknown functions and provide an attractive compromise between nonparametric approaches that make no assumptions and parametric approaches that make strong assumptions about the functional form. Current popular smoothing methods include spline-based methods such as smoothing splines (e.g., cubic splines, kringing), polynomial splines (e.g., P-splines, B-Splines), and regression splines and kernel-based methods such as LOESS (or LOcal regrESSion) and local polynomial kernels (for details on smoothing methods, interested readers should refer to Fahrmeir et al. 2013; Pagan and Ullah 1999; Ruppert et al. 2003; Simonoff 1996; Wu and Zhang 2006). While each method has its pros and cons, we select the penalized-spline (P-spline) method due to its flexibility and computational efficiency (Tan et al. 2012) and the fact that it has also previously been used in marketing (Sloot et al. 2006; Stremersch and Lemmens 2009). Compared to other methods, P-splines show no boundary effects, can fit polynomial data exactly, and can conserve moments of the data (Eilers and Marx 1996). In addition, the penalty used by the P-spline approach is more general than the one used for smoothing spline. Finally, P-splines are easy to estimate using a mixed model estimation methodology and are not sensitive to knot parameter selection (Baladandayuthapani et al. 2005).

The general idea behind P-splines is that we can approximate function β(t) with lower order polynomial functions, for example, truncated power basis (Tan et al. 2012):

$$
t ^ {0}, t ^ {1}, t ^ {2}, \dots , t ^ {q}, (t - \tau_ {1}) _ {+} ^ {q}, \dots , (t - \tau_ {K}) _ {+} ^ {q}\tag{9}
$$

where the first $q + 1$ terms are the power functions of t of order $0 , 1 , 2 , . . . , q$ , and the remaining K terms are truncated q order power function determined by K truncation points of knots $\tau _ { 1 } , \tau _ { 2 } , . . . , \tau _ { K }$ over the range of t; the notation $( t - \tau ) _ { + } ^ { q }$ indicates that the function equals zero for $t \leq \tau$ and (t – τ) otherwise; we can specify quadratic splines using $q = 2$ and cubic splines using $q = 3$

The choice of q is less critical, but given that “quadratic splines are not often used” (Jain 2003, p. 269), we use $q = 3$ (or cubic splines).<sup>16</sup> We can now specify the unknown coefficient functions in Equation 4 as:

$$
\beta_ {0} \left(t _ {i j}\right) = a _ {0} ^ {0} + a _ {1} ^ {0} t _ {i j} + a _ {2} ^ {0} t _ {i j} ^ {2} + a _ {3} ^ {0} t _ {i j} ^ {3} + \sum_ {k = 1} ^ {K} a _ {3 + k} ^ {0} \left(t _ {i j} - \tau_ {k}\right) _ {+} ^ {3}\tag{10a}
$$

$$
\beta_ {1} \left(t _ {i j}\right) = a _ {0} ^ {1} + a _ {1} ^ {1} t _ {i j} + a _ {2} ^ {1} t _ {i j} ^ {2} + a _ {3} ^ {1} t _ {i j} ^ {3} + \sum_ {k = 1} ^ {K} a _ {3 + k} ^ {1} \left(t _ {i j} - \tau_ {k}\right) _ {+} ^ {3}\tag{10b}
$$

where coefficients $a _ { 3 + k } ^ { 0 }$ and $a _ { 3 + k } ^ { 1 }$ are then shrunk toward zero (or penalized) to obtain smoother estimates (Wand 2003). Inserting the above coefficient functions (Equations 10a and 10b) in Equation 4, we obtain

$$
\begin{array}{l} S _ {i j} = a _ {0} ^ {0} + a _ {1} ^ {0} t _ {i j} + a _ {2} ^ {0} t _ {i j} ^ {2} + a _ {3} ^ {0} t _ {i j} ^ {3} + \sum_ {k = 1} ^ {K} a _ {3 + k} ^ {0} (t _ {i j} - \tau_ {k}) _ {+} ^ {3} + a _ {0} ^ {1} X _ {i j} \\ \qquad + a _ {1} ^ {1} t _ {i j} X _ {i j} + a _ {2} ^ {1} t _ {i j} ^ {2} X _ {i j} + a _ {3} ^ {1} t _ {i j} ^ {3} X _ {i j} + \sum_ {k = 1} ^ {K} a _ {3 + k} ^ {1} (t _ {i j} - \tau_ {k}) _ {+} ^ {3} X _ {i j} + \varepsilon_ {i j} \end{array}\tag{11}
$$

The above model is a linear regression model that can be estimated using ordinary least squares regression. Wand (2003) suggests treating $a _ { 3 + k } ^ { 0 } , a _ { 3 + k } ^ { 1 } , k = 1 , 2 , . . . , K$ in the above equation as random variables with normal distributions to obtain optimal smoothing parameters.

$$
a _ {3 + k} ^ {0} \sim N (0, \eta_ {0}), \quad a _ {3 + k} ^ {1} \sim N (0, \eta_ {1}); \quad k = 1, 2, \dots , K\tag{12}
$$

Equation 11 can now be estimated using a linear mixed model with $a _ { i } ^ { j } , i = 1 , . . . , 3 , j = 0$ or 1 as fixed effects and $a _ { 3 + k } ^ { 0 }$ $a _ { 3 + k } ^ { 1 } , k = 1 , 2 , . . . , K$ as random effects with variances $\eta _ { 0 }$ and $\eta _ { 1 } ,$ respectively. The variable parameters effectively shrink the random effect coefficients with a small variance parameter implying that the random effect coefficients would be closer to zero and hence a smooth function, whereas a large variance parameter implies larger random effect coefficients and hence a closer fit. The optimal balance can be determined using the restricted maximum likelihood (REML) approach as demonstrated by Wand (2003). Moreover, such models can be easily estimated across several platforms (e.g., nlme package in R or S-Plus, PROC MIXED in SAS), making it an excellent practical choice. Ngo and Wand (2004) and Tan et al. (2012) provide a friendly implementation guide for SAS, R, and S-Plus.

Thus, in addition to our focal variable (MAILS), our final model includes customer demographic and psychographic characteristics and recent transaction characteristics. Specifically, we include customer characteristics such as age (AGE), financial stability (FSTABILITY), household size (HSIZE), population density of the area they live in (PDENS), marital status (MARRIAGE), and interest in gardening (GARDEN) or home improvement (DECOR). Given the seasonal nature of our product category, we also include seasonality (SEASON) to indicate the summer months (April and May). We also include recent transaction characteristics such as REDEEM, RETURNS, and CROSSBUY. Further, acknowledging that some of these transaction characteristics are known to have nonlinear effects (Petersen and Kumar 2009), we include quadratic effects of MAILS, REDEEM, RETURNS, and CROSSBUY.

Finally, to account for any serial correlation, we use a firstorder autoregressive model (e.g., Naik and Raman 2003), where we include the lagged value of our dependent variable, SALES. The presence of lagged dependent variable (SALES in Equation 13 and MAILS in Equation 7) violates the strong exogeneity assumptions. To account for the dynamic panel bias introduced due to the presence of these lagged dependent variables, we use a system-GMM estimator that relies on relatively mild restrictions (Blundell et al. 2000), where we use the lagged differences in the dependent variable as instruments for our equations in levels, i.e., $S A L E S _ { i j } = \Delta S A L E S _ { i j - 1 }$ $+ \ e _ { i j }$ (Arellano and Bover 1995; Blundell and Bond 1998). The underlying assumption behind these instruments is that past changes in the dependent variable y are uncorrelated with the current errors in levels (Roodman 2009). Thus, the final model that we estimate is:

$$
\begin{array}{l} S A L E S _ {i j} = \beta_ {0} (t _ {i j}) + \beta_ {1} (t _ {i j}) M A I L S _ {i j} + \beta_ {2} (t _ {i j}) M A I L S _ {i j} ^ {2} + \beta_ {3} (t _ {i j}) R E D E E M _ {i j} \\ \quad + \beta_ {4} (t _ {i j}) R E D E E M _ {i j} ^ {2} + \beta_ {5} (t _ {i j}) R E T U R N S _ {i j} + \beta_ {6} (t _ {i j}) R E T U R N S _ {i j} ^ {2} \\ \quad + \beta_ {7} (t _ {i j}) C R O S S B U Y _ {i j} + \beta_ {8} (t _ {i j}) C R O S S B U Y _ {i j} ^ {2} + \beta_ {9} (t _ {i j}) A G E _ {i j} \\ \quad + \beta_ {1 0} (t _ {i j}) F S T A B I L I T Y _ {i j} + \beta_ {1 1} (t _ {i j}) H S I Z E _ {i j} + \beta_ {1 2} (t _ {i j}) P D E N S _ {i j} \\ \quad + \beta_ {1 3} (t _ {i j}) M A R R I A G E _ {i j} + \beta_ {1 4} (t _ {i j}) G A R D E N _ {i j} + \beta_ {1 5} (t _ {i j}) D E C O R _ {i j} \\ \quad + \beta_ {1 6} (t _ {i j}) S E A S O N S _ {i j} + \gamma_ {1} \overline {{S A L E S}} _ {i j - 1} + \gamma_ {2} \hat {\eta} _ {i j} ^ {M A I L S} + \gamma_ {3} I M R _ {i} + \varepsilon_ {i j} \end{array}\tag{13}
$$

where $S A L E S _ { i j - 1 }$ is the predicted value of SALES from the equation $\begin{array} { r } { S A L E S _ { i j } = \Delta S A L E S _ { i j - 1 } + e _ { i j } . } \end{array}$

To provide a benchmark model comparison, we estimate the above equation using each of the three specifications: (1) no time-varying effects (baseline model), (2) multilevel model with parameter estimates as linear functions of time $t _ { i j } ,$ and (3) the proposed time-varying effects model with cubic splines.

## Results

We present the pairwise correlations and the descriptive statistics in Table 2. Next, we present the results of our estimation, starting with the results of our sample selection and endogeneity correction models. We then provide a fit comparison of various specifications, and present and discuss the results of the best model.<sup>17</sup>

## Sample Selection Procedure

We present the results of the first stage probit model as detailed in Equation 5 in Table 3. The results provide insights into consumers’ decision to receive marketing communications. The likelihood of opting-in to receive marketing communications increases with customers’ financial stability $\beta =$ $. 0 0 2 , p < . 0 0 1 )$ , household size $( \beta = . 0 0 3 , p < . 0 5 )$ , age of the head of the household $( \beta = . 0 0 2 , p < . 0 0 1 )$ , online purchases $( \beta = . 0 3 2 , p < . 0 0 1 )$ , and interest in general reading $( \beta = . 0 4 1$ $p < . 0 0 1 )$ . In contrast, the likelihood of opting-in to receive marketing communication decreases with population density $( \beta = . 0 0 4 , p < . 0 0 1 )$ and marriage $( \beta = . 0 3 0 , p < . 0 0 1 )$ . Although the results are specific to our product category, they are in the expected direction and in line with some of the studies in this domain. For example, Cotton and Babb (1978) find that household size has a positive influence on coupon usage, and Teel et al. (1980) find that coupon usage decreases with the age of the housewife. Married customers (MARRIAGE) or those living in dense (or urban) areas (PDENS) may have little time for do-it-yourself (DIY) activities and hence are less likely to opt-in to receive marketing communications from the retailer. Finally, in line with the optimum stimulation level (OSL) theory (Steenkamp and Baumgartner 1992), customers interested in general reading (MGEN) or “information seekers” pursue a higher level of external stimuli and may be more likely to opt-in to receive marketing communications than those with low OSL.

## Endogeneity Correction Procedure

Next, we present the first stage results of our control function approach to correct for the potential endogeneity of the mailers sent in Table 4. The results from Table 4 provide some insights into the retailers mailing strategy. In line with the view that firms use historical allocations to guide future resource allocation (Doctorow et al. 2009), we find that the number of mailers sent in the current period depends on the number of mailers sent in the previous period $( \beta = . 7 5 6 , p <$ .001). Similarly, the mailing strategy is influenced by recent customer transactions, and customer characteristics. The number of mailers sent is positively related to sales $( \beta =$ $. 0 0 0 0 2 , p < . 0 5 )$ , returns $( \beta = . 0 5 4 , p < . 0 0 1 )$ , and coupon redemptions $( \beta = . 7 4 1 , p < . 0 0 1 )$ , but negatively related to crossbuy $( \beta = . 0 3 2 , p < . 0 0 1 )$ of the previous period. Thus, other than the negative effect of cross-buy, our results are in line with the expectations that would suggest that the number of mailers sent to customers should increase with their interactions with the firm (Simester et al. 2006). One explanation for the negative effect could be that firms may not send as many mailers to loyal customers (as indicated by high levels of cross-buys) due to the lower return on investments for loyal customers, as compared to those sent to disloyal customers (i.e., a nonlinear effect of cross-buy on mailers).

To explore this thought further, we estimated the model with the quadratic term for cross-buy and indeed we do find a nonlinear relationship between cross-buys and the number of mailers sent, such that the number of mailers received by customers increases at a decreasing rate as cross-buy increases. This result confirms the view that customers that are loyal to the firm (as indicated by high cross-buys) require little persuasion and marketing investments (Dick and Basu 1994). Customers interested in gardening $( \beta = . 2 5 4 , p < . 0 0 1 )$ and home improvement $( \beta = . 1 8 7 , p < . 0 0 1 )$ receive more mailers than those who are not interested in such activities, which is not surprising given the retailer’s focus on these categories. As one would expect, the retailer sends more mailers to customers who respond to mail orders than those who do not $( \beta = . 1 2 4 , p < . 0 1 )$ to increase the response rate. In contrast, married customers $( \beta = - . 3 9 0 , p < . 0 0 1 )$ receive less mailers than those who are single. The negative finding is in line with Baker (2013), who argued that newly married couples, couples with young kids, and women are less likely to be interested in DIY activities (McGoldrick and Collins 2007). Similarly, the number of mailers decreases with customer’s age $( \beta = . 0 1 3 , p < . 0 0 1 )$ , in line with the view that mature customers may be less interested in DIY home improvements. Also, the retailer reduces the number of mailers sent out in summer or around summer months or moving season $( \beta = . 0 1 3 , p < . 0 0 1 )$ , as customers may require less persuasion during summer months, which is the peak season for gardening as well as home improvement projects. Finally, the retailer sends more mailers to customers who are financially stable and are likely to buy more (β = .029, p < .001) and live in densely populated areas (β = .031, $p < . 0 0 1 )$ , and less to those who live in small households as customers with larger households, who are likely to be married and with kids, are less likely to be interested in DIY activities and hence less interested in the products offered by the focal retailer (β = -.065, p < .001).

Table 2. Pairwise Correlation Coefficients

<table><tr><td></td><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td><td>(13)</td><td>(14)</td><td>(15)</td><td>(16)</td><td>(17)</td></tr><tr><td>1</td><td>SALES</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>MAILS</td><td>-0.019a</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>REDEEM</td><td>0.222a</td><td>0.041a</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>RETURNS</td><td>0.335a</td><td>-0.005a</td><td>0.132a</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>CROSSBUY</td><td>0.630a</td><td>-0.031a</td><td>0.218a</td><td>0.382a</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>PDENS</td><td>-0.008a</td><td>0.011a</td><td>-0.007a</td><td>0.012a</td><td>0.010a</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>SEASON</td><td>0.063a</td><td>-0.003a</td><td>0.039a</td><td>0.019a</td><td>0.057a</td><td>0.000</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>FSTABILITY</td><td>0.017a</td><td>0.020a</td><td>0.016a</td><td>0.012a</td><td>0.018a</td><td>-0.123a</td><td>0.000</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9</td><td>HSIZE</td><td>0.008a</td><td>-0.017a</td><td>-0.005a</td><td>-0.001c</td><td>0.011a</td><td>-0.028a</td><td>0.000</td><td>0.136a</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>GARDEN</td><td>0.002a</td><td>0.013a</td><td>0.012a</td><td>0.003a</td><td>0.009a</td><td>-0.076a</td><td>0.000</td><td>0.303a</td><td>0.156a</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11</td><td>DECOR</td><td>0.003a</td><td>0.012a</td><td>0.009a</td><td>0.003a</td><td>0.007a</td><td>-0.057a</td><td>0.000</td><td>0.324a</td><td>0.174a</td><td>0.592a</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12</td><td>MARRIAGE</td><td>0.015a</td><td>-0.028a</td><td>0.007a</td><td>0.009a</td><td>0.027a</td><td>-0.117a</td><td>0.000</td><td>0.183a</td><td>0.314a</td><td>0.182a</td><td>0.181a</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13</td><td>AGE</td><td>-0.006a</td><td>-0.025a</td><td>0.013a</td><td>0.015a</td><td>0.006a</td><td>-0.028a</td><td>0.000</td><td>0.011a</td><td>-0.065a</td><td>0.224a</td><td>0.168a</td><td>0.093a</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>14</td><td>ONLINEPURCH</td><td>-0.005a</td><td>0.039a</td><td>0.002a</td><td>-0.009a</td><td>-0.007a</td><td>-0.044a</td><td>0.000</td><td>0.299a</td><td>0.154a</td><td>0.289a</td><td>0.28a</td><td>0.116a</td><td>0.019a</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>15</td><td>MGEN</td><td>0.000</td><td>0.000</td><td>0.003a</td><td>0.002a</td><td>0.001a</td><td>-0.025a</td><td>0.000</td><td>0.048a</td><td>0.044a</td><td>0.085a</td><td>0.075a</td><td>0.048a</td><td>0.108a</td><td>0.049a</td><td>1.000</td><td></td><td></td></tr><tr><td>16</td><td>MPOL</td><td>0.001b</td><td>0.000</td><td>0.001c</td><td>0.001c</td><td>0.001a</td><td>0.003a</td><td>0.000</td><td>0.007a</td><td>0.000</td><td>0.002a</td><td>0.00aa</td><td>0.000</td><td>0.001a</td><td>0.002a</td><td>0.002a</td><td>1.000</td><td></td></tr><tr><td>17</td><td>MOR</td><td>0.003a</td><td>0.007a</td><td>0.006a</td><td>0.003a</td><td>0.007a</td><td>-0.038a</td><td>0.000</td><td>0.300a</td><td>0.186a</td><td>0.427a</td><td>0.480a</td><td>0.174a</td><td>0.126a</td><td>0.239a</td><td>0.062a</td><td>0.001a</td><td>1.000</td></tr><tr><td></td><td>Mean</td><td>65.949</td><td>4.429</td><td>0.027</td><td>0.088</td><td>0.990</td><td>5.180</td><td>0.167</td><td>14.778</td><td>3.257</td><td>0.822</td><td>0.870</td><td>0.762</td><td>51.442</td><td>0.551</td><td>0.077</td><td>0.000</td><td>0.939</td></tr><tr><td></td><td>S.D.</td><td>178.291</td><td>5.836</td><td>0.199</td><td>0.380</td><td>1.693</td><td>2.399</td><td>0.373</td><td>4.754</td><td>1.496</td><td>0.382</td><td>0.337</td><td>0.426</td><td>13.229</td><td>0.497</td><td>0.266</td><td>0.010</td><td>0.240</td></tr></table>

Notes. <sup>a</sup>p < 0.001, <sup>b</sup>p < 0.01, <sup>c</sup>p < 0.05

Table 3. Parameter Estimates for the First-Stage Probit Model to Correct for Sample Selection

<table><tr><td>Independent Variables</td><td>Parameter Estimates</td><td>Standard Errors</td><td>95% Confidence Interval</td></tr><tr><td>Financial stability index (FSTABILITY)</td><td>0.002***</td><td>0.0004</td><td>[0.001, 0.003]</td></tr><tr><td>Household size (HSIZE)</td><td>0.003*</td><td>0.001</td><td>[0.001, 0.006]</td></tr><tr><td>Population density (PDENS)</td><td>-0.004***</td><td>0.001</td><td>[-0.006, -0.003]</td></tr><tr><td>Age (AGE)</td><td>0.002***</td><td>0.0002</td><td>[0.0021, 0.0027]</td></tr><tr><td>Marriage (MARRIGE)</td><td>-0.030***</td><td>0.005</td><td>[-0.040, -0.021]</td></tr><tr><td>Interest in gardening (GARDEN)</td><td>-0.003</td><td>0.006</td><td>[-0.016, 0.010]</td></tr><tr><td>Interest in home improvement (DECOR)</td><td>0.016*</td><td>0.007</td><td>[0.001, 0.030]</td></tr><tr><td>Online purchases (ONLINEPURCH)</td><td>0.032***</td><td>0.004</td><td>[0.024, 0.040]</td></tr><tr><td>General reading (MGEN)</td><td>0.041***</td><td>0.007</td><td>[0.027, 0.055]</td></tr><tr><td>News and political reading (MPOL)</td><td>0.432</td><td>0.223</td><td>[-0.006, 0.869]</td></tr><tr><td>Constant</td><td>0.118***</td><td>0.012</td><td>[0.094, 0.142]</td></tr></table>

Notes. \*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001

Table 4. First-Stage Results for the Control Function Approach to Correct for Endogeneity of Mailers

<table><tr><td>Independent Variables</td><td>Parameter Estimates</td><td>Standard Errors</td><td>95% Confidence Interval</td></tr><tr><td> $SALES_{j-1}$ </td><td>0.00002*</td><td>0.00001</td><td>[0.0000042, 0.0000044]</td></tr><tr><td> $\overline{MAILS}_{ij-1}$ </td><td>0.756***</td><td>0.002</td><td>[0.753, 0.759]</td></tr><tr><td> $REDEEM_{j-1}$ </td><td>0.741***</td><td>0.007</td><td>[0.728, 0.754]</td></tr><tr><td> $RETURN_{j-1}$ </td><td>0.054***</td><td>0.004</td><td>[0.047, 0.062]</td></tr><tr><td> $CROSSBUY_{j-1}$ </td><td>-0.032***</td><td>0.001</td><td>[-0.034, -0.029]</td></tr><tr><td>Population density (PDENS)</td><td>0.031***</td><td>0.003</td><td>[0.025, 0.036]</td></tr><tr><td>Seasonality (SEASON)</td><td>-0.013***</td><td>0.004</td><td>[-0.012, -0.006]</td></tr><tr><td>Financial stability index (FSTABILITY)</td><td>0.029***</td><td>0.002</td><td>[0.026, 0.032]</td></tr><tr><td>Household size (HSIZE)</td><td>-0.065***</td><td>0.005</td><td>[-0.074, -0.055]</td></tr><tr><td>Interest in gardening (GARDEN)</td><td>0.254***</td><td>0.024</td><td>[0.207, 0.300]</td></tr><tr><td>Interest in home improvement (DECOR)</td><td>0.187***</td><td>0.028</td><td>[0.133, 0.242]</td></tr><tr><td>Marriage (MARRIAGE)</td><td>-0.39***</td><td>0.018</td><td>[-0.424, -0.355]</td></tr><tr><td>Age (AGE)</td><td>-0.013***</td><td>0.001</td><td>[-0.015, -0.012]</td></tr><tr><td>Mail order responder (MOR)</td><td>0.124**</td><td>0.042</td><td>[0.041, 0.207]</td></tr><tr><td>Constant</td><td>1.314***</td><td>0.053</td><td>[1.209, 1.418]</td></tr></table>

Notes: \*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001

## Model Fit Comparisons

Before we present the model fit comparison, we briefly discuss the knot selection issue. As discussed in Equation 9 above, the P-splines approach approximates the lower order polynomial function by dividing the entire time range t into (K+1) smaller regions using K truncation points or knots. We distribute the knots evenly over the entire time period. Although there is no agreement on the number of knots (K) to be selected, Wand (2003) suggests that K can be selected as a minimum number between 35 and T/4, where T is the number of distinctive measurement times. Since our dataset spans 36 months, we select $K = M I N \left( 3 5 , 3 6 / 4 \right) = 9$ for the discussion of our results.<sup>18</sup>

We compare the model fit with respect to alternate model specifications. Specifically, we compare the following models: (1) baseline model with no time-varying effects as specified in Equation 1, (2) multilevel model with parameter estimates as linear functions of time $t _ { i j } ,$ as specified in Equation 2, (3) time-varying effects model with linear, quadratic, and cubic splines for only transaction characteristics (MAILS, REDEEM, RETURNS, and CROSSBUY), and (4) the full timevarying effects model with linear, quadratic, and cubic splines for all variables as specified in Equation 13. The fit statistics are presented in Table 5, where we include the log-likelihood and various fit statistics.<sup>19</sup>

<table><tr><td colspan="5">Table 5. Comparison of Model Fit Statistics</td></tr><tr><td>Model</td><td>Trend Specification</td><td>-2 Res LL</td><td>AIC</td><td>BIC</td></tr><tr><td>Baseline (Time-invariant)</td><td>NA</td><td>1.1200E+08</td><td>1.1200E+08</td><td>1.1200E+08</td></tr><tr><td>MLM</td><td>NA</td><td>1.1182E+08</td><td>1.1182E+08</td><td>1.1182E+08</td></tr><tr><td rowspan="3">Only transaction characteristics (MAILS, REDEEM, RETURNS, and CROSSBUY) specified as time-varying</td><td>Linear spline</td><td>111,812,703</td><td>111,812,715</td><td>111,812,703</td></tr><tr><td>Quadratic spline</td><td>111,811,815</td><td>111,811,827</td><td>111,811,815</td></tr><tr><td>Cubic spline</td><td>111,811,453</td><td>111,811,465</td><td>111,811,453</td></tr><tr><td rowspan="3">All variables specified as time-varying</td><td>Linear spline</td><td>111,812,656</td><td>111,811,987</td><td>111,811,965</td></tr><tr><td>Quadratic spline</td><td>111,811,044</td><td>111,811,068</td><td>111,811,044</td></tr><tr><td>Cubic spline</td><td>111,810,744</td><td>111,810,768</td><td>111,810,744</td></tr></table>

Table 6. Parameter Estimates for the Baseline Model (Without Any Time-Varying Effects)

<table><tr><td>Independent Variables</td><td>Parameter Estimates</td><td>Standard Errors</td><td>95% Confidence Interval</td></tr><tr><td> $\overline{SALES}_{j-1}$ </td><td>0.06***</td><td>0.007</td><td>[0.047, 0.074]</td></tr><tr><td>Mails (MAILS)</td><td>0.412***</td><td>0.027</td><td>[0.359, 0.466]</td></tr><tr><td>Mails × Mails ( $MAILS^2$ )</td><td>-0.013***</td><td>0.002</td><td>[-0.016, -0.009]</td></tr><tr><td>Redeemed coupons (REDEEM)</td><td>98.065***</td><td>0.81</td><td>[96.476, 99.653]</td></tr><tr><td>Redeemed  $coupons^2$ ( $REDEEM^2$ )</td><td>-7.647***</td><td>0.277</td><td>[-8.189, -7.105]</td></tr><tr><td>Return frequency (RETURNS)</td><td>48.046***</td><td>0.531</td><td>[47.006, 49.086]</td></tr><tr><td>Return  $frequency^2$ ( $RETURNS^2$ )</td><td>0.129</td><td>0.187</td><td>[-0.237, 0.495]</td></tr><tr><td>Crossbuy (CROSSBUY)</td><td>44.926***</td><td>0.136</td><td>[44.660, 45.192]</td></tr><tr><td> $Crossbuy^2$ ( $CROSSBUY^2$ )</td><td>2.734***</td><td>0.028</td><td>[2.679, 2.790]</td></tr><tr><td>Population density (PDENS)</td><td>-1.076***</td><td>0.021</td><td>[-1.118, -1.035]</td></tr><tr><td>Seasonality (SEASON)</td><td>11.599***</td><td>0.133</td><td>[11.338, 11.860]</td></tr><tr><td>Financial stability index (FSTABILITY)</td><td>0.233***</td><td>0.012</td><td>[0.208, 0.257]</td></tr><tr><td>Household size (HSIZE)</td><td>0.311***</td><td>0.03</td><td>[0.252, 0.370]</td></tr><tr><td>Interest in gardening (GARDEN)</td><td>-1.398***</td><td>0.14</td><td>[-1.672, -1.123]</td></tr><tr><td>Interest in home improvement (DECOR)</td><td>-0.006</td><td>0.166</td><td>[-0.331, 0.319]</td></tr><tr><td>Marriage (MARRIAGE)</td><td>-1.613***</td><td>0.114</td><td>[-1.836, -1.389]</td></tr><tr><td>Age (AGE)</td><td>-0.092***</td><td>0.006</td><td>[-0.103, -0.081]</td></tr><tr><td>Residual(RESID)</td><td>-0.557***</td><td>0.018</td><td>[-0.592, -0.522]</td></tr><tr><td>Inverse Mills Ratio (IMR)</td><td>-15.211***</td><td>3.063</td><td>[-21.216, -9.206]</td></tr><tr><td>Constant</td><td>18.492***</td><td>2.699</td><td>[13.201, 23.784]</td></tr></table>

Notes: \*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001

As can be seen from the fit statistics, inclusion of temporal variations improves the model fit. Not surprisingly, the baseline model (with no time-varying effects) has the lowest fit (AIC and BIC: 1.200E+08), and the fit improves for the multilevel model (AIC and BIC: 1.1182E+08). The proposed TVEM framework provides the best fitting model (AIC and BIC: 1.1181E+08), suggesting that the effect of variables in our model varies over time. The results from the three models provide the same overall conclusion, with each subsequent model providing a more refined understanding of the relationship between the variables. To understand the differences between the baseline model and our proposed approach, we present the results of the baseline model in Table 6,<sup>20</sup> the multilevel model in Figure 1, the time-varying effects model in Figure 2, and duly discuss the effects of each of our variables.<sup>21</sup>

## Parameter Estimates

First, we highlight that both the correction terms are significant, providing due justification for our correction procedures. The negative coefficient of the inverse Mills ratio parameter estimate suggests that the customers in our sample (those that have opted-in) have fewer sales than those excluded from the sample. Further, as can be seen from the results, the sales series (SALES) exhibits significant persistence; and the lagged sales are a significant predictor of future sales (e.g., Naik and Raman 2003). Regarding the role of mailers, our results suggest that the number of mailers (MAILS) have an inverted-U shaped effect on purchases, possibly due to information overload or fatigue (e.g., Eastlick et al. 1993). Moreover the results are economically significant; results from the baseline model suggests that, on average, a one standard deviation increase in MAILS sent increases the SALES per month to \$65.73 compared to \$63.77 at the mean value of MAILS, an increase of \$1.96 or 3%. However, as can be seen from Figure 3, the nonlinear effect vanishes over the customer life cycle. Coupon redemptions (REDEEM) also have an inverted-U shaped effect on the sales, suggesting that the customers who redeem a lot of coupons (or shop only promotional goods) may hurt sales (e.g., Kopalle et al. 1999). However, as can be seen from Figure 3, the effect is far more nuanced with the relationship showing significant variations as customers develop a relationship with the retailer. Both returns (RETURNS) and cross-buy (CROSSBUY) exhibit a nonlinear effect on sales. Specifically, as the returns and cross-buys increase, sales increase at an increasing rate. This finding is in line with the view that product returns reduce the customer’s purchase risk and hence encourage future sales (Petersen and Kumar 2009). We hasten to highlight that our results are only related to sales and not profitability, which remains a fertile avenue for future research. Similarly, when customers buy across multiple categories, there is an increased likelihood of them purchasing across multiple product categories on each purchase occasion, resulting in higher sales as compared to those who do not shop across multiple categories (Kumar et al. 2008).

The parameter estimates of our control variables are also in the expected direction for a retailer specializing in home improvement, construction, and gardening. Customers that are financially stable (FSTABILITY), and live in larger households (HSIZE), purchase more than others. In contrast to our expectations, interest in gardening (GARDEN) has a significant negative effect on sales. Informal surveys with executives and customers revealed that the focal retailer has a lower reputation for gardening products as compared to another major retailer. Thus, the customers that are interested in gardening shop at a competitor’s store or other specialty retailers. Sales are lower for married customers (MARRIAGE) in line with the view that married customers (or those with young kids) have little time for home improvement or gardening activities (Baker 2013). Along similar lines, sales decrease with the age (AGE) of customers as mature customers may be less motivated to engage in such activities.

Although the basic results are interesting, the value of our TVEM model lies in its ability to highlight the temporal variations in these customer-brand relationships, as can be seen in Figure 2. The plots clearly reveal that the effect of these variables is hardly constant over the time period, a fact that is largely overlooked by traditional estimation techniques. To assess the robustness of our findings, we estimate several alternate specifications, including using different sets of exclusion variables in the self-selection and endogeneity correction models, alternate measures for some of our variables, excluding squared terms, using a first-order autoregressive model, varying the number and locations of the knots (K), and including interaction effects. Our results are highly robust to these alternate specifications and the model presented in the paper is superior to such alternate specifications.

![](/api/attachments/KR4Z2B64/fulltext/images/8c5c55a83455f89828b825c14dc1b4fb8bd37211f6858d8b45b5a51789f45277.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/f4b1c413b53c7e17757676e536daf81ddcfd0cd56fbced6f7c3d5180cf0d4a6e.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/196f1a12c2fd1cb04955ff5e06b8fdc9f1963dadc570067538dbfd8fa002b93a.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/ac251c115a1b994f5859a7b7c139abf812b4cdeef84ab1d01c99780b75743a1f.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/51823c3906a6d8cb0a979574cc7f53fb6db45d0e663929581083709f027bb03b.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/11808e18cd7cf2e34e44f11a5cb65918701cf02b216bb76cb573185a6a79539e.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/862eeacfc29e1feef6f5855bc9187cfd938b30c68ad0fb04fdebf1be0c7a19ce.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/698503ecb93a9bcf7de191a75bce2264f2d264e8860eaa57f9b0beba6d02f746.jpg)  
Notes: Plots of control variables (e.g., PDENS, HSIZE) are omitted to conserve space; the same can be requested from the authors.  
Figure 1. Results from Multilevel Linear Regression Model

## Comparison with Dynamic Linear Models

We suggested earlier that the existing state-space methodologies such as dynamic linear models (DLM) or Kalmanfilters (Petris et al. 2009; West and Harrison 1997) are not suitable for analyzing large datasets due to the assumptions regarding the underlying states and the time required to estimate such models (Leeflang et al. 2009). To illustrate this claim, we compare our TVEM approach with DLM estimation. Since DLM cannot handle the large dataset (as can be seen from Table 7), we use a synthetic dataset for this comparison.<sup>22</sup> We present the fit statistics (AIC and BIC values) along with the time required for estimating these models for different number of individuals (N) in Table 7.

![](/api/attachments/KR4Z2B64/fulltext/images/c97755436811e182aab7c0b3fb0676921b0af550df51999949a5f675682b45ca.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/9f0eed02d4b7f1f9e183613e630ec2f18f96be66df8c1f64065a2db8f17eac1e.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/150072e36f354976cba31c386492bd4829fe730d6a0fab0816037c56107ec484.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/df6a519e5083609265c86e2403e5db323d4507b8e2743b48971d738affa6b5c2.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/82abf894023afcd683f19ca1a234e37e71420f455805a333e8cf190beb520107.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/98fdb2b707a42555d557ea59d13142a04805f76eed28f4a02b0ee1eebfc7a11c.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/23d23f891957d8e1e3aa93e61fbddf50ceca00eda7997b4673976d9bff7acf02.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/0d450e6b0f45128416bbb413fcdda85bb225e3f7ce4f264b0a617150f889aaea.jpg)  
Notes: Plots of control variables (e.g., PDENS, HSIZE) are omitted to conserve space; the same can be requested from the authors.  
Figure 2. Time-Varying Effect Model with All Variables Specified as Time-Varying

As expected, DLM outperforms the TVEM approach for small Ns. However, the TVEM model provides a better fit as N increases. The number of parameters to be estimated remains constant for TVEM, whereas it increases exponentially for the DLM estimation. Moreover, even for a very small sample of N = 50, the DLM estimation takes over twenty-four hours (making it impractical for big data analytics) compared to a few seconds in case of TVEM. In sum, for large datasets, the TVEM approach not only fits better but also requires significantly less time for estimation.

## Predictive Validity

Although TVEM is an explanatory model that allows us to capture the changes in the coefficient function, managers can still use the results to make forward predictions. To demonstrate the predicitve abilities of our proposed model, we assess the predictive accuracy of our model relative to alternate specifications. Specifically, we carry out both in-sample and out-of-sample predictive validity tests and compare our model to two alternate specifications: (1) no time-varying effects

Effect of RETURNS on SALES over time

Effect of MAILS on SALES over time

![](/api/attachments/KR4Z2B64/fulltext/images/4a7d5eacf0d832df5da392728946a86d02b6f13128cd54daf2bfe7e99a246588.jpg)  
Effect of REDEEM on SALES over time

![](/api/attachments/KR4Z2B64/fulltext/images/d5386fe17773bb5dcfba09434e28bfe14e54a7fb80182f82d3bd06ae1a30a816.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/2199fd341f8a0614eb180260cf640471d2b1a11eae3e0108a2509d0f701c1d1c.jpg)

Effect of CROSSBUY on SALES over time  
![](/api/attachments/KR4Z2B64/fulltext/images/80066de4e1a7927cca0bd291cfb04c1f43be6b4abe4b89bd256fc8f55dad3e2d.jpg)

Figure 3. 3D Plots for the Effect of MAILS, REDEEM, RETURNS, and CROSSBUY on SALES Over Time

(baseline model) and (2) multilevel model with parameter estimates as linear functions of time $t _ { i j } .$ We use the root mean square error (RMSE) between the predicted and actual values for the prediction tasks. For the in-sample prediction task, we predict the sales for an average customer from month 4 through 36;<sup>23</sup> for the out-of-sample task, we predict sales for four periods (37 through 40) after our estimation period.<sup>24</sup> The results in Table 8 provide strong support for our model relative to the other models. The proposed model fits both insample and out-of-sample data well, providing credibility and confidence in the explanatory as well as the predictive power of our model.

## Accounting for Individual Heterogeneity

Pauwels et al. (2004) note that the problems associated with ignoring unobserved heterogeneity are especially significant in dynamic models. Although we account for such unobserved heterogeneity using the mixed effects specification, one could argue in favor of both the intercept and slope heterogeneity<sup>25</sup> (e.g., Pesaran et al. 1996), an issue that we discuss in this section.

First, given the nature of big-data, where we have access to large volume and variety of information about consumers, the concerns of unobserved heterogeneity are significantly mitigated. Firms literally have access to almost all of the possible information about their consumers that can be included in their estimation, partly mitigating the concerns of unobserved heterogeneity. Moreover, as has been frequently pointed out, unobserved heterogeneity is a form of selection bias or omitted variable bias (Murray 2005; Schunck 2014) and we account for the same through our control function approach. More importantly, our TVEM methodology addresses the bigger challenge presented by velocity of data, wherein firms collect data on a continuous basis, by allowing us to incorporate updated information in real time and update decisions accordingly.

<table><tr><td colspan="12">Table 7. Comparison with Dynamic Linear Models</td></tr><tr><td colspan="2"></td><td>N = 1</td><td>N = 2</td><td>N = 3</td><td></td><td>N = 20</td><td>N = 30</td><td>N = 35</td><td>N = 40</td><td>N = 45</td><td>N = 50</td></tr><tr><td rowspan="4">DLM</td><td>AIC</td><td>548.6</td><td>1163.6</td><td>1807.5</td><td></td><td>15279.9</td><td>23779.3</td><td>28720.5</td><td>33423.2</td><td>38573.0</td><td>43871.9</td></tr><tr><td>BIC</td><td>557.0</td><td>1185.9</td><td>1849.3</td><td></td><td>16506.4</td><td>26455.2</td><td>32330.3</td><td>38106.2</td><td>44468.5</td><td>51119.4</td></tr><tr><td>No. of parameters</td><td>3</td><td>8</td><td>15</td><td></td><td>440</td><td>960</td><td>1295</td><td>1680</td><td>2115</td><td>2600</td></tr><tr><td>Estimation time</td><td>0.5 min</td><td>1.5 min</td><td>3 min</td><td></td><td>2 hours</td><td>5 hours</td><td>7 hours</td><td>10.5 hours</td><td>15 hours</td><td>24.5 hours</td></tr><tr><td rowspan="4">TVEM</td><td>AIC</td><td>730.6</td><td>1527.7</td><td>2309.8</td><td></td><td>16119.3</td><td>24184.2</td><td>28469.9</td><td>32834.1</td><td>37132.9</td><td>41164.9</td></tr><tr><td>BIC</td><td>754.6</td><td>1552.5</td><td>2340.9</td><td></td><td>16151.2</td><td>24354.4</td><td>28574.3</td><td>32892.6</td><td>37241.7</td><td>41378.6</td></tr><tr><td>Number of Parameters</td><td colspan="10">28</td></tr><tr><td>Estimation time</td><td colspan="10">Less than a minute</td></tr></table>

Notes: N is the number of individuals; for TVEM, the number of knots is 10. Both models were estimated on the same machine.

<table><tr><td colspan="5">Table 8. Predictive Accuracy by Model Type</td></tr><tr><td>Prediction Task</td><td>Measure</td><td>Proposed Model (TVEM)</td><td>Baseline Model (time-invariant)</td><td>Multilevel Model</td></tr><tr><td rowspan="2">In-Sample</td><td>RMSE</td><td>1.81</td><td>15.13</td><td>9.14</td></tr><tr><td>MAD</td><td>0.25</td><td>1.82</td><td>1.23</td></tr><tr><td rowspan="2">Out-of-Sample</td><td>RMSE</td><td>2.30</td><td>5.79</td><td>2.55</td></tr><tr><td>MAD</td><td>0.97</td><td>2.59</td><td>1.22</td></tr></table>

Notes: Root mean squared error (RMSE) represents the sample standard deviation of the differences between predicted values and observed values; mean absolute deviation (MAD) is the mean of the absolute deviations between predicted and actual values.

Table 9. Comparison of Model Fit Statistics between (Baseline and TVEM) Models that Account for Heterogeneity and Those that Do Not

<table><tr><td></td><td>Model Fit (AIC value)</td><td>Model Fit (BIC value)</td></tr><tr><td>Baseline Model with Random Intercepts</td><td>37,032.5</td><td>37,164.7</td></tr><tr><td>Baseline Model with Random Coefficients</td><td>36,334.6</td><td>36,454.7</td></tr><tr><td>TVEM without Random Coefficients (Proposed One)</td><td>36,325.2</td><td>36,307.2</td></tr><tr><td>TVEM with Random Intercepts</td><td>36,317.2</td><td>36,293.2</td></tr><tr><td>TVEM with Random Coefficients</td><td>36,129.4</td><td>36,103.4</td></tr></table>

Notes: Random Coefficients include random intercepts and random slopes.

Nevertheless, TVEM can be extended to account for both intercept and slope heterogeneity by adding random coefficients (both random intercept and random slopes). A randomintercept model allows intercepts to vary with individual customers and allows us to control for unobserved heterogeneity at the customer level. Random slopes allow the parameter estimates to vary across individuals. The addition of random coefficients, however, requires a different estimation technique and significantly increases the model complexity and estimation time. Thus, one needs to weigh the relative benefits of such an approach. To establish the relative importance of time-varying effects and accounting for individual heterogeneity, we carry out additional analysis on a subsample (100 customers) to compare several models that help us tease out the relative importance of time-varying effects and individual heterogeneity.<sup>26</sup> Specifically, we estimate (1) a baseline panel data regression model with random intercepts, (2) a baseline panel data regression model with random coefficients that includes both random intercept and random slopes, (3) baseline TVEM model, (4) TVEM model with random intercepts, and (5) TVEM model with random coefficients that includes both random intercept and random slopes and present the results in Table 9.

As can be clearly seen, the baseline TVEM model without any random coefficients provides a better fit compared to a panel data model that accounts for both intercept and slope heterogeneity. Not surprisingly, the TVEM models with random intercepts and random coefficients do better than the baseline TVEM model. The results highlight that firms will be better off with the TVEM model and that the value of incorporating time varying effects will only go up as the volume of data goes up. These results also suggest that big data has its unique challenges that may be more important than issues that plague traditional estimation approaches (such as endogeneity, heterogeneity, and autocorrelation).

Given the economic significance of accounting for timevarying effects and the fact that most firms make resource allocation decisions on segments rather than on individual customers as it is extremely expensive to personalize offerings at an individual level, we instead recommend the use of segmentation techniques to model both slope and intercept heterogeneity (e.g., Andrews et al. 2002; Bago d'Uva 2005; Clark et al. 2005).<sup>27</sup> Specifically, firms can use their existing segmentation bases or segment their customers based on desirable characteristics using the K-means clustering algorithm or latent-class segmentation (Wedel and Kamakura 2000) and then run the TVEM model with random intercepts for each segment.<sup>28</sup> Firms need to choose the optimal number of segments based on costs and benefits of having multiple segments. Most firms make resource allocation decisions on segments rather than on individual customers as it is extremely expensive to personalize offerings at an individual level. Thus, our approach of analyzing the TVEM model for a segment of customer is in line with organizational realities.

As a demonstration of the above approach, we created subsegments of customers based on available demographic variables using the K-means clustering algorithm and estimated the TVEM model for each segment with the random-intercept. We varied the number of segments from 30 to 300 (with the corresponding change in the number of customers in each segment) and successfully estimated our model for each subsegment. Clearly, firms should use their managerial judgment in using the appropriate segmentation variables and the size of segments. However, in line with our overall objective, the proposed approach can easily handle both slope and intercept heterogeneity.

Next, we would like to highlight that one can easily estimate the first difference model (that eliminates any time-invariant individual characteristics) within our TVEM framework, which may eliminate any residual concerns about unobserved heterogeneity. Finally, we would also like to highlight that we estimated the random-intercepts model using a Bayesian Markov Chain Monte Carlo technique that can easily account for unobserved heterogeneity. We can share the WinBUGS code upon request. The code can be easily extended by scholars to other environments (e.g., R or C++) for future research.

## Accounting for Endogeneity of other Transactional Variables

Whereas we correct for the potential endogeneity of MAILS in the proposed model as that is the only variable that the focal firm can directly influence, one can argue that our other transactional variables may also be endogenous and should be corrected for.<sup>29</sup> For example, REDEEM may be endogenous as consumers using coupons may be qualitatively different (e.g., consumers who have higher intention to purchase may search for and use coupons actively) from other customers. Similarly, CROSSBUY and RETURNS may be considered endogenous. For example, Kumar et al. (2008) document that customers who shop across multiple product categories shop more; similarly, Petersen and Kumar (2009) demonstrate that returns increase sales by reducing the uncertainty associated with product purchases. In sum, in addition to MAILS, our estimation approach may also have to account for the potential endogeneity of REDEEM, CROSSBUY, and RETURNS.

Accordingly, we estimate an additional model to test and correct for the endogeneity of the three transactional variables (i.e., REDEEM, RETURNS, and CROSSBUY), in addition to our focal marketing variable (i.e., MAILS). Specifically, we follow the same control function approach, where we first predict the potentially endogenous variable using a set of exogenous variables (e.g., demographics) and use the correction terms (residuals) from the first stage as additional explanatory variables in our final model. We use the cumulative values of the respective variables as exclusion variables for identification purposes. The cumulative value of the respective transaction characteristics (Cum\_REDEEM, Cum\_RETURNS, and Cum\_CROSSBUY) is likely to be a good predictor of the current value of the respective variable, but is less likely to be a good predictor for current sales. Indeed, the correlations between cumulative and the current value of our transaction variable is high, whereas there is almost no correlation between the cumulative transaction variables and current sales. Thus, the final model that we estimate is as follows:

$$
\begin{array}{l} S _ {i j} = \beta_ {0} \left(t _ {i j}\right) + \dots + \gamma_ {1} \hat {\eta} _ {1 i j} ^ {M A I L S} + \gamma_ {2} \hat {\eta} _ {2 i j} ^ {R E D E E M} \\ \quad + \gamma_ {3} \hat {\eta} _ {3 i j} ^ {R E T U R N S} + \gamma_ {4} \hat {\eta} _ {4 i j} ^ {C R O S S B U Y} + \gamma_ {5} I M R _ {i} \\ \quad + \varepsilon_ {i j} \end{array}\tag{14}
$$

where $\gamma _ { i } , i = 1 , \cdots , 5$ are the coefficients for the correction terms.

While results from the final model confirm the endogeneity of our transactional variables as all the correction terms are significant, the results are qualitatively identical to the ones reported here and can be obtained from the authors, providing confidence in our results.<sup>30</sup>

## Incorporating Long-Term Effects of Marketing-Mix Elements

We include only the contemporaneous MAILS in our model. Thus, our model does not account for the long-term effects of MAILS sent in previous periods. While this may be valid for promotional material that are time sensitive and typically have a very small redemption period (typically less than 10 days, in our case), other marketing-mix elements may have persistent effects (Osinga et al. 2010).<sup>31</sup>

In line with Osinga et al. (2010, p. 174) who indicate that “persistent effects can occur only in nonstationary series,” we performed a unit root test and found overwhelming evidence against the null hypothesis of a unit root and conclude that all of our focal variables are stationary. That is, there is no evidence of any long-run (or persistent) effects in the data as there is no evolutionary or long-run component in SALES (Dekimpe and Hanssens 1995).

However, we acknowledge that other marketing mix elements may have persistent effects and that there could also be delays in consumers’ responses to marketing actions.<sup>32</sup> For such situations, the TVEM framework can be easily extended to include additional lags of marketing inputs. We recommend a cautious approach as including additional lags can cause multicollinearity issues.

## Incorporating Additional Data

As we suggested earlier, our original objective is to have firms update their resource allocations frequently as and when new data becomes available. This leads to a question about the impact of such frequent updates on the results of our model. Clearly, as new data comes in, some of the estimates will change to reflect the changes in the shape of the coefficient function. However, to establish the reliability of our approach and for managers to trust our model, it is imperative that our results do not change dramatically (e.g., change signs or large changes in the magnitudes of our estimates) every time new data comes in. To alleviate those concerns, we reestimate our model for a subsample of 259,308 customers for whom we have 40 months of transaction information and present the results in Figure 4. Minor differences aside, our results are very similar to those that we presented for the 36- months sample earlier, lending further credibility and confidence to our approach.

A related concern that one may have is whether it is optimal to use all data (starting from the first period) to estimate the model. It is possible that using use a “moving window approach” to emphasize more recent behavioral data may yield more accurate sales predictions.<sup>33</sup> Given that consumer pref-

![](/api/attachments/KR4Z2B64/fulltext/images/dc242988cedc08dceeb9b562e0007b80a578edfb0c599b0165b863b439c972d9.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/7294ebf2c3e8e5bef413e861152637ba3d6f7018ab2d6731a68b7a12b4d316d2.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/3e3b113d992938798456f4b130bdedb23e0938b9ce41aa7882a8e73fd1ff7e3b.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/9c0e09ffc8f53fd49529e40abe55ef22e7d1e4d0ce4da218b2eb3100ec22604f.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/bf0fd0e4d27d62fd548d3b8015bc15f280a5ec9c8f3897e4f4c4344bb7be2a98.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/b9bedcfb1bec30691835f82e84511af07a85a5c354bc4fe0c7acee987b3aa882.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/e510bcf72381f01f11e03fcc33bfc52ff4e2d657ab4dd81103cf7c86ceb39b73.jpg)

![](/api/attachments/KR4Z2B64/fulltext/images/e9d056e6184f7019949e24dee290f0a7d8959a3ca9d9e49c83ef84c7c4bc5ae9.jpg)  
Notes: Plots of control variables (e.g., PDENS, HSIZE) are omitted to conserve space; the same can be requested from the authors.

Results from Time-Varying Effect Model with Extended Sample (40 Months)

erences evolve, their recent behavior should be better predictor of their future actions, making the moving window approach intuitively attractive.

To test this assumption, we estimated our final model with different moving windows (most recent 12, 18, 24, 30, and 36 months of data) to predict the sales for the next month and measure the predictive accuracy using the standard measure, mean absolute deviation (MAD).<sup>34</sup> The results confirm the intuition that the recent data can produce more accurate sales predictions. In our analysis, we get the best prediction using the most recent 24 months of data to make one-month forward predictions. Specifically, the MADs for a one-month forward prediction using the most recent 12, 18, 24, 30, and 36 months data are .31, .06, .01, .31, and .55 respectively. Clearly, the interval will be different for other contexts, but these results highlight that it may not be necessary to use all of the data (starting from first period) to make better predictions and thus significantly lower the estimation complexities.<sup>35</sup> We hasten to highlight that if the objective is to understand how the coefficient function evolves so that the learning can be used for a new cohort of customers, firms may want to use the full data.

## Managerial Implications and Discussion

Firms are collecting more data on their customers than ever before, which offers both significant opportunities and challenges as firms try to convert all of this data into actionable insights. A recent McKinsey report suggesting that retailers using big data can increase their operating margin by more than 60%, duly highlights this opportunity (Manyika et al. 2011). However, Parmar et al. (2014, p. 89) argue “companies are notoriously bad at finding ways to make money” and suggest that companies use data they own (or have access to) to facilitate growth. Along this vein, the objective of our research was to utilize volumes of customer transaction data that organizations collect to guide their marketing resource allocation decision across customers. Specifically, we examine a retailer’s decision to send marketing mailers to customers. We conceptualize that customers’ response to such mailers change as they become familiar (and establish a relationship) with the company and that firms should adjust their marketing allocations accordingly on a frequent basis to increase the returns from their marketing investments. Given the dynamic environment, frequent updating of resource allocation decisions is essential as suggested by Fruk et al. (2013) who demonstrate that frequent reallocation of resources results in superior performance. Accordingly, we propose and demonstrate a time-varying effects model that explicitly accounts for the temporal changes in the effectiveness of the marketing-mix elements and provide actionable insights to managers. The proposed model relies on nonparametric assumptions and hence is ideal for the big data context. The results from our time-varying effects model provide a strong support for our framework and we urge managers to reconsider their marketing resource allocation decisions. Firms can significantly increase performance and create value by targeting customers at the right time, when they are proven to be most responsive to the firm’s communications, as opposed to sending communications on an ad hoc basis, when they are less likely to respond to organizational communications. Our results are both practically significant and academically relevant, as we discuss in this section.

same. Specific to our context, we find that firms can increase their revenues per customer from \$156.83 (under the baseline model that assumes a constant effect of marketing actions) to \$183.03, by using the proposed TVEM approach over a 36- month window (i.e., gain an increase of 17% in revenues per customer without any additional expenditure).<sup>36</sup> Stated differently, firms can achieve the same level of sales as under the baseline scenario even after reducing the number of mailers sent under the baseline scenario by a fifth, indicating savings over 20% in marketing budgets. These results provide some credence to the McKinsey report that suggests that retailers can increase their margins by more than 60% by using bigdata to its full potential (Manyika et al. 2011).

The results from our model can help managers reallocate their marketing resources to increase sales per customer by over 17% without any additional investment.<sup>37</sup> Moreover, executives can easily use the proposed model to make projections for future time periods and allocate their marketing resources accordingly.<sup>38</sup> We simulated this forward-looking resource allocation approach, wherein we used the parameter estimates at the end of the 36<sup>th</sup> month to make resource allocation decisions for the next four months (months 37 through 40). The results suggest that, on average over the four month period, firms can increase their revenues by up to 20.55% from their current levels using the TVEM approach compared to only 8.86% using the baseline (time-invariant) model without additional investments.<sup>39</sup> Although we make projections for four periods for this exercise, in line with the McKinsey report that encourages frequent reallocation of resources (Manyika et al. 2011), we encourage executives to estimate the model in every decision period to frequently update their resource allocation strategy. To investigate the value of frequent resource allocation, we repeated the forward-looking resource allocation simulation only for one period: used the results at the end of $3 6 ^ { \mathrm { t h } }$ month to allocate resources for $3 7 ^ { \mathrm { t h } }$ month. Results from the one-period forward simulation are in line with our expectations; firms can increase their revenues by over 21.54% from their current levels using the TVEM approach compared to only 12.12% using the recommendations from the baseline model. Thus, our results provide empirical support to the McKinsey study (Manyika et al. 2011) that calls for frequent resource allocation by incorporating the latest information.

While it is not surprising to learn that consumer response to marketing mailers changes over time, ours is the first research that allows managers to recover the exact pattern of behavior change (i.e., shape of the change) without forcing any assumptions about the functional form and take actions based on such changes. Most importantly, the proposed model does not impose any additional requirements and can be easily implemented by most organizations using their existing resources. Finally, unlike some of the other models in this domain that are resource intensive and can only be implemented infrequently, the proposed framework can be easily run frequently so that managers can adjust their resource allocations on a “real-time” basis. Although the TVEM frameork can be applied to a long list of variables that firms may have, we suggest that they use managerial insights and simple models (e.g., stepwise regression) to identify the important variables and use time varying effects for these variables. Given the ease of implementation of our framework, we encourage managers to run the proposed model in every period (when new data becomes available) and adjust their resource allocation accordingly. To facilitate the adoption of our approach, we direct managers to Ngo and Wand (2004) and Tan et al. (2012) who provide friendly implementation guides for SAS, R, and S-Plus; we can share the WinBUGS code for the Bayesian implementation upon request.

## Implications for Theory

In addition to the practical significance of our study, our research also contributes to the literature on marketing resource allocation, dynamic modeling, and big data analytics.

ments for including the impact of temporal variations in the effectiveness of marketing-mix elements. Although scholars acknowledge that consumer response to marketing activities can vary over time due to a variety of factors such as consumer learning (Narayanan and Manchanda 2009), effects of marketing actions (Janakiraman et al. 2008), or changes in consumer preferences (Neelamegham and Chintagunta 2004), the models for “dynamic marketing resource allocation typically assume that marketing effectiveness is constant over time” (Raman et al. 2012, p. 910).<sup>40</sup> Thus, ours is the first empirical study in the dynamic resource allocation literature to model the temporal changes in marketing-mix effectiveness and recover the change function for firms to act on it. We acknowledge that the proposed methodology may not be suitable for small panels (T < 10; Tan et al. 2012), however, with the proliferation of big data and the availability of large datasets through other sources (e.g., Wharton Research Data Services, Wharton Customer Analytics Initiative, World Bank), we hope scholars consider the temporal variations in their models.

To the dynamic modeling literature, we offer an alternative to Kalman filtering (e.g., Osinga et al. 2010; Sriram et al. 2006) and dynamic linear models (DLM) (Ataman et al. 2007; Van Heerde et al. 2004) to incorporate temporal variations in the effectiveness of marketing-mix elements. While both Kalman filtering and DLM have desirable properties and are attractive options to include time-varying parameters, they make assumptions about the underlying state-space, “take several hours or days” to estimate, and require complicated coding in matrix language (Leeflang et al. 2009, p. 15). The proposed TVEM framework does not make strong assumptions about the underlying states and can be easily implemented, providing an attractive alternative to the two established methodologies for dynamic models. More importantly, unlike Kalman filtering and DLM that assume discrete time and discrete state space (Dekimpe et al. 2008; Pauwels et al. 2004), our proposed framework can be used for continuous time and continuous state space.<sup>41</sup> Discrete time models suffer from temporal aggregation bias and depend on the observed data frequency for model development (Bergstrom and Nowman 2007). Continuous time modeling avoids such issues and, more importantly, allow predictions for shorter intervals, allowing firms to act in real-time (Bergstrom 1996).

To the marketing resource allocation literature (e.g., Montoya et al. 2010; Naik et al. 2005), we provide compelling argu-

Similarly, discrete space models are sensitive to the assumptions about the number of underlying states (Leeflang et al. 2009). Thus, our research answers the call by Leeflang et al. (2009) who argue for the importance of accounting for timevarying parameters and our study offers a potential solution for scholars looking for ways to do the same and can be easily implemented in other contexts with large panels where the relationship between variables can be expected to vary. Further, TVEM offers an alternate approach to the functional regression analysis, which is designed for sparse longitudinal data, where both the predictor and response are functions of a covariate such as time (Shi and Choi 2011).<sup>42</sup> Given our focus on the managerial application of the model where purchases (or most other covariates) do not have a smooth functional form and where firms do not suffer with limited information (or measurement) issues, the proposed TVEM approach presents a nice complement to the functional data analysis. TVEM does not assume any underlying functional form for variables and uses all of the available data without any major investments within existing organizational infrastructure, and allows firms to reap the purported benefits of big data. We firmly believe that TVEM should be viewed as another tool in the toolkit of scholars working on longitudinal data that offers significant value without much up-front costs.

Finally, our research contributes to the emerging stream of research on big data analytics. The TVEM approach allows firms to understand temporal variations in the relationships between variables of interest, enabling them to adjust strategies in real time. Thus, our research responds to the call by Goes (2014, p. vi) to help firms in the “generation of knowledge and intelligence to support decision making” using big data.

## Opportunities for Future Research

Our research addresses an important gap in the dynamic marketing resource allocation literature by incorporating temporal variations in the effectiveness of marketing-mix elements and we sincerely hope that our research will motivate scholars to consider temporal variations in their models. We outline the potential substantive as well as methodological topics that scholars can fruitfully pursue.

In terms of substantive topics, scholars can investigate the temporal effects of a variety of marketing activities. Scholars can investigate other customer-focused resource allocation activities such as targeted promotions or salesperson resource allocation. Similarly, scholars can easily extend our approach to other units of analysis; for example, one can optimize advertising spending by investigating advertising effectiveness across markets over time or make calculated market entry or exit decisions such as an airline’s decision to fly (or stop flying) to a market. One can easily tweak our approach to investigate firm-level decisions such as investments in geographical markets or product technology. Another area of future research would be to examine how marketing activities (such as mailers) influence online and offline purchases and the substitution affect of the two.<sup>43</sup>

Although our model is fairly robust and flexible to accommodate a range of topics, we believe that scholars can build upon our framework and extend it even further. First, although we account for individual heterogeneity using the random-intercept specification and slope-heterogeneity (i.e., allow for the slopes to vary across customers) using segmentation techniques, we are barely scratching the surface here. Consumers react differently to marketing stimuli and scholars can find ways to personalize marketing actions instead of estimating “average effect” to ensure the effectiveness of marketing resource allocation. Second, instead of the time factor that we use as a reference in our framework, scholars can experiment with other reference variables such as size or age. Time may not be a valid reference in many situations, thereby making our proposed approach of limited value, for example when the initiation of a relationship is not observed. Alternately, scholars can treat the unobserved starting point as a missing data problem and extend the model using data augmentation techniques to estimate the model when the starting point is not observed. Third, scholars can examine persistent or long-term effects of marketing-mix elements. Although we can easily incorporate additional lags of marketing-mix elements within the TVEM framework, other robust techniques that account for the transient and persistent effects of marketing-mix elements should be explored. Another fruitful avenue is to model how some of the other variables influence the shape of the change function and how firms can alter the shape of the change function to their advantage. For instance, our results (Figure 2) show that the effectiveness of mailers (MAILS) decreases with time and any research that can highlight ways to prevent this decline in the effectiveness of MAILS will be highly valuable. Finally, scholars can examine alternate dependent variables such as profitability (which we could not model as we do not have the cost information) or the rate of coupon redemption.<sup>44</sup>

## Acknowledgments

We thank the coeditors of the special issue on big data and the review team for their valuable guidance in the revision process. We thank the firm for providing us the data for the study. We thank Anita Luo, Denish Shah, Yi Zhao, and Gayatri Shukla for their comments on an earlier version of the manuscript. We also thank Renu for copyediting the manuscript.

## References

Anderson, E. T., Hansen, K., and Simester, D. 2009. “The Option Value of Returns: Theory and Empirical Evidence,” Marketing Science (28:3), pp. 405-423.

Andrews, R. L., Ainslie, A., and Currim, I. S. 2002. “An Empirical Comparison of Logit Choice Models with Discrete Versus Continuous Representations of Heterogeneity,” Journal of Marketing Research (39:4), pp. 479-487.

Arellano, M., and Bover, O. 1995. “Another Look at the Instrumental Variable Estimation of Error-Components Models,” Journal of Econometrics (68:1), pp. 29-51.

Ataman, M. B., Mela, C. F., and Van Heerde, H. J. 2007. “Consumer Packaged Goods in France: National Brands, Regional Chains, and Local Branding,” Journal of Marketing Research (44:1), pp. 14-20.

Bago d'Uva, T. 2005. “Latent Class Models for Use of Primary Care: Evidence from a British Panel,” Health Economics (14:9), pp. 873-892.

Baker, F. 2013. “Improving Targeting: Lessons from DIY Behaviour Online,” (http://marketingblogged.marketingmagazine.co. uk/2013/08/20/improving-targeting-lessons-from-diy-behaviouronline/; retrieved December 31, 2013).

Baladandayuthapani, V., Mallick, B. K., and Carroll, R. J. 2005. “Spatially Adaptive Bayesian Penalized Regression Splines (P-Splines),” Journal of Computational and Graphical Statistics (14:2), pp. 378-394.

Bapna, R., Jank, W., and Shmueli, G. 2008. “Price Formation and Its Dynamics in Online Auctions,” Decision Support Systems (44:3), pp. 641-656.

Bendapudi, N., and Berry, L. L. 1997. “Customers’ Motivations for Maintaining Relationships with Service Providers,” Journal of Retailing (73:1), pp. 15-37.

Berger, P. D., and Bechwati, N. N. 2001. “The Allocation of Promotion Budget to Maximize Customer Equity,” Omega (29:1), pp. 49-61.

Bergstrom, A. R. 1996. Survey of Continuous Time Econometrics, New York: Cambridge University Press.

Bergstrom, A. R., and Nowman, K. B. 2007. A Continuous Time Econometric Model of the United Kingdom with Stochastic Trends,New York: Cambridge University Press.

Bierens, H. J., and Pott-Buter, H. A. 1991. “Specification of Household Engel Curves by Nonparametric Regression,” Econometric Reviews (9:2), pp. 123-184.

Blundell, R., and Bond, S. 1998. “Initial Conditions and Moment Restrictions in Dynamic Panel Data Models,” Journal of Econometrics (87:1), pp. 115-143.

Blundell, R., Bond, S., and Windmeijer, F. 2000. “Estimation in Dynamic Panel Data Models: Improving on the Performance of the Standard GMM Estimator,” in Nonstationary Panels, Panel Cointegration, and Dynamic Panels, B. H. Baltagi (ed.),New York: Elsevier Science Inc., pp. 53-91.

Chapra, S. C. 2011. Applied Numerical Methods with Matlab for Engineers and Scientists (3<sup>rd</sup> ed.), New York: McGraw-Hill.

Chen, H., Chiang, R. H., and Storey, V. C. 2012. “Business Intelligence and Analytics: From Big Data to Big Impact,” MIS Quarterly (36:4), pp. 1165-1188.

Chen, J., and Stallaert, J. 2014. “An Economic Analysis of Online Advertising Using Behavioral Targeting,” MIS Quarterly (38:2), pp. 429-449.

Clark, A., Etilé, F., Postel Vinay, F., Senik, C., and Van der Straeten, K. 2005. “Heterogeneity in Reported Well Being: Evidence from Twelve European Countries,” The Economic Journal (115:502), pp. C118-C132.

Cotton, B., and Babb, E. M. 1978. “Consumer Response to Promotional Deals,” Journal of Marketing (42:3), pp. 109-113.

Crainiceanu, C. M., Staicu, A.-M., and Di, C.-Z. 2009. “Generalized Multilevel Functional Regression,” Journal of the American Statistical Association (104:488), pp. 1550-1561.

Deighton, J., Henderson, C. M., and Neslin, S. A. 1994. “The Effects of Advertising on Brand Switching and Repeat Purchasing,” Journal of Marketing Research (31:1), pp. 28-43.

Dekimpe, M. G., Franses, P. H., Hanssens, D. M., and Naik, P. A. 2008. “Time-Series Models in Marketing,” in Handbook of Marketing Decision Models, B. Wierenga (ed.), New York: Springer, pp. 373-398.

Dekimpe, M. G., and Hanssens, D. M. 1995. “The Persistence of Marketing Effects on Sales,” Marketing Science (14:1), pp. 1-21.

Dick, A. S., and Basu, K. 1994. “Customer Loyalty: Toward an Integrated Conceptual Framework,” Journal of the Academy of Marketing Science (22:2), pp. 99-113.

Divakar, S., Ratchford, B. T., and Shankar, V. 2005. “Practice Prize Article—CHAN4CAST: A Multichannel, Multiregion Sales Forecasting Model and Decision Support System for Consumer Packaged Goods,” Marketing Science (24:3), pp. 334-350.

Doctorow, D., Hoblit, R., and Sekhar, A. 2009. “Measuring Marketing: McKinsey Global Survey Results,” McKinsey & Company (http://www.mckinsey.com/insights/marketing\_sales/ measuring\_marketing\_mckinsey\_global\_survey\_results; accessed December 1, 2013).

Dubé, J. P., Hitsch, G. J., and Rossi, P. E. 2010. “State Dependence and Alternative Explanations for Consumer Inertia,” RAND Journal of Economics (41:3), pp. 417-445.

Eastlick, M. A., Feinberg, R., and Trappey, C. 1993. “Information Overload in Mail Catalog Shopping: How Many Catalogs Are Too Many?,” Journal of Direct Marketing (7:4), pp. 14-19.

Eilers, P. H., and Marx, B. D. 1996. “Flexible Smoothing with B-Splines and Penalties,” Statistical Science (11:2), pp. 89-102.

Elberse, A., and Eliashberg, J. 2003. “Demand and Supply Dynamics for Sequentially Released Products in International Markets: The Case of Motion Pictures,” Marketing Science (22:3), pp. 329-354.

Elsner, R., Krafft, M., and Huchzermeier, A. 2004. “Optimizing Rhenania's Direct Marketing Business through Dynamic Multilevel Modeling (DMLM) in a Multicatalog-Brand Environment,” Marketing Science (23:2), pp. 192-206.

Fahrmeir, L., Kneib, T., Lang, S., and Marx, B. 2013. Regression— Models, Methods, and Applications, New York: Springer.

Faraway, J. J. 1997. “Regression Analysis for a Functional Response,” Technometrics (39:3), pp. 254-261.

Foekens, E. W., Leeflang, P. S., and Wittink, D. R. 1994. “A Comparison and an Exploration of the Forecasting Accuracy of a Loglinear Model at Different Levels of Aggregation,” International Journal of Forecasting (10:2), pp. 245-261.

Fruk, M., Hall, S., and Mittal, D. 2013. “Never Let a Good Crisis Go to Waste,” McKinsey Quarterly (4), pp. 56-59.

Garen, J. 1984. “The Returns to Schooling: A Selectivity Bias Approach with a Continuous Choice Variable,” Econometrica (52:5), pp. 1199-1218.

Givon, M., and Horsky, D. 1990. “Untangling the Effects of Purchase Reinforcement and Advertising Carryover,” Marketing Science (9:2), pp. 171-187.

Goes, P. 2014. “Editor’s Comments: Big Data and IS Research,” MIS Quarterly (38:3), pp. iii-viii.

Gönül, F. F., and Ter Hofstede, F. 2006. “How to Compute Optimal Catalog Mailing Decisions,” Marketing Science (25:1), pp. 65-74.

Gupta, S., and Steenburgh, T. 2008. “Allocating Marketing Resources,” in Marketing Mix Decisions: New Perspectives and Practices, R. A. Kerin and R. O’Regan (eds.), Chicago: American Marketing Association.

Hastie, T., and Tibshirani, R. 1993. “Varying-Coefficient Models,” Journal of the Royal Statistical Society Series B (Methodological) (55:4), pp. 757-796.

Heckman, J. J. 1979. “Sample Selection Bias as a Specification Error,” Econometrica (47:1), pp. 153-161.

Hoch, S. J., and Ha, Y.-W. 1986. “Consumer Learning: Advertising and the Ambiguity of Product Experience,” Journal of Consumer Research (13:October), pp. 221-233.

Hollander, M., Wolfe, D. A., and Chicken, E. 2013. Nonparametric Statistical Methods (3<sup>rd</sup> ed.), Hoboken, NJ: John Wiley & Sons.

Imbens, G. W., and Wooldridge, J. M. 2007. “Control Function and Related Methods,” What’s New in Econometrics, Lecture Notes 6, Summer 2007, National Bureau of Economics Research.

Jain, M. K. 2003. Numerical Methods for Scientific and Engineering Computation, New Delhi, India: New Age International.

Janakiraman, R., Dutta, S., Sismeiro, C., and Stern, P. 2008. “Physicians’ Persistence and its Implications for Their Response to Promotion of Prescription Drugs,” Management Science (54:6), pp. 1080-1093.

Kopalle, P. K., Mela, C. F., and Marsh, L. 1999. “The Dynamic Effect of Discounting on Sales: Empirical Analysis and Norma-

tive Pricing Implications,” Marketing Science (18:3), pp. 317-332.

Kumar, V. 2013. Profitable Customer Engagement: Concept, Metrics and Strategies, Thousand Oaks, CA: SAGE Publications.

Kumar, V., Bhaskaran, V., Mirchandani, R., and Shah, M. 2013. “Creating a Measurable Social Media Marketing Strategy for Hokey Pokey: Increasing the Value and ROI of Intangibles and Tangibles,” Marketing Science (32:2), pp. 194-212.

Kumar, V., George, M., and Pancras, J. 2008. “Cross-Buying in Retailing: Drivers and Consequences,” Journal of Retailing (84:1), pp. 15-27.

Kumar, V., and Reinartz, W. 2012. Customer Relationship Management: Concept, Strategy, and Tools (2<sup>nd</sup> ed.), New York: Springer Science & Business Media.

Kumar, V., Zhang, X. A., and Luo, A. 2014. “Modeling Customer Opt-in and Opt-out in a Permission-Based Marketing Context,” Journal of Marketing Research (51:4), pp. 403-419.

Leeflang, P. S., Bijmolt, T. H., Van Doorn, J., Hanssens, D. M., Van Heerde, H. J., Verhoef, P. C., and Wieringa, J. E. 2009. “Creating Lift Versus Building the Base: Current Trends in Marketing Dynamics,” International Journal of Research in Marketing (26:1), pp. 13-20.

Leeflang, P. S. H., Wittink, D. R., Wedel, M., and Naert, P. A. 2000. Building Models for Marketing Decisions, Boston: Kluwer Academic Publishers.

Lewis, M. 2004. “The Influence of Loyalty Programs and Short-Term Promotions on Customer Retention,” Journal of Marketing Research (41:3), pp. 281-292.

Lin, M., Lucas Jr., H. C., and Shmueli, G. 2013. “Too Big to Fail: Large Samples and the P-Value Problem,” Information Systems Research (24:4), pp. 906-917.

Luan, Y. J., and Sudhir, K. 2010. “Forecasting Marketing-Mix Responsiveness for New Products,” Journal of Marketing Research (47:3), pp. 444-457.

Mahajan, V., Bretschneider, S. I., and Bradford, J. W. 1980. “Feedback Approaches to Modeling Structural Shifts in Market Response,” Journal of Marketing (44:1), pp. 71-80.

Manchanda, P., and Chintagunta, P. K. 2004. “Responsiveness of Physician Prescription Behavior to Salesforce Effort: An Individual Level Analysis,” Marketing Letters (15:2-3), pp. 129-145.

Manyika, J., Chui, M., Brown, B., Bughin, J., Dobbs, R., Roxburgh, C., and Byers, A. H. 2011. “Big Data: The Next Frontier for Innovation, Competition, and Productivity,” McKinsey Global Institute.

McGoldrick, P. J., and Collins, N. 2007. “Multichannel Retailing: Profiling the Multichannel Shopper,” International Review of Retail, Distribution and Consumer Research (17:2), pp. 139-158.

Mela, C. F., Jedidi, K., and Bowman, D. 1998. “The Long-Term Impact of Promotions on Consumer Stockpiling Behavior,” Journal of Marketing Research (35:2), pp. 250-262.

Mizik, N., and Jacobson, R. 2003. “Trading Off between Value Creation and Value Appropriation: The Financial Implications of Shifts in Strategic Emphasis,” Journal of Marketing (67:1), pp. 63-76.

Montoya, R., Netzer, O., and Jedidi, K. 2010. “Dynamic Allocation of Pharmaceutical Detailing and Sampling for Long-Term Profitability,” Marketing Science (29:5), pp. 909-924.

Murray, M. P. 2005. Econometrics: A Modern Introduction Boston: Prentice Hall.

Naik, P. A., and Raman, K. 2003. “Understanding the Impact of Synergy in Multimedia Communications,” Journal of Marketing Research (40:4), pp. 375-388.

Naik, P. A., Raman, K., and Winer, R. S. 2005. “Planning Marketing-Mix Strategies in the Presence of Interaction Effects,” Marketing Science (24:1), pp. 25-34.

Narayanan, S., and Manchanda, P. 2009. “Heterogeneous Learning and the Targeting of Marketing Communication for New Products,” Marketing Science (28:3), pp. 424-441.

Neelamegham, R., and Chintagunta, P. K. 2004. “Modeling and Forecasting the Sales of Technology Products,” Quantitative Marketing and Economics (2:3), pp. 195-232.

Ngo, L., and Wand, M. P. 2004. “Smoothing with Mixed Model Software,” Journal of Statistical Software (9:1), pp. 1-54.

Osinga, E. C., Leeflang, P. S., and Wieringa, J. E. 2010. “Early Marketing Matters: A Time-Varying Parameter Approach to Persistence Modeling,” Journal of Marketing Research (47:1), pp. 173-185.

Pagan, A., and Ullah, A. 1999. Nonparametric Econometrics, Cambridge, UK: Cambridge University Press.

Pan, Y., and Lehmann, D. R. 1993. “The Influence of New Brand Entry on Subjective Brand Judgments,” Journal of Consumer Research, pp. 76-86.

Parmar, R., Mackenzie, I., Cohn, D., and Gann, D. 2014. “The New Patterns of Innovation,” Harvard Business Review (92:1/2), pp. 86-95.

Parsons, L. J. 1975. “The Product Life Cycle and Time-Varying Advertising Elasticities,” Journal of Marketing Research (12:4), pp. 476-480.

Parsons, L. J., and Schultz, R. L. 1976. Marketing Models and Econometric Research, Amsterdam: North-Holland Publishing Company.

Pauwels, K., Currim, I., Dekimpe, M. G., Hanssens, D. M., Mizik, N., Ghysels, E., and Naik, P. 2004. “Modeling Marketing Dynamics by Time Series Econometrics,” Marketing Letters (15:4), pp. 167-183.

Pauwels, K., and Hanssens, D. M. 2007. “Performance Regimes and Marketing Policy Shifts,” Marketing Science (26:3), pp. 293-311.

Pazzani, M. J., and Billsus, D. 2007. “Content-Based Recommendation Systems,” in The Adaptive Web, P. Brusilovsky, A. Kobsa and W. Nejdl (eds.), Berlin: Springer-Verlag, pp. 325-341.

Pesaran, H., Smith, R., and Im, K. 1996. “Dynamic Linear Models for Heterogenous Panels,” in The Econometrics of Panel Data, L. Mátyás and P. Sevestre (eds.), Dordrecht, The Netherlands: Springer Netherlands, pp. 145-195.

Petersen, J. A., and Kumar, V. 2009. “Are Product Returns a Necessary Evil? Antecedents and Consequences,” Journal of Marketing (73:3), pp. 35-51.

Petrin, A., and Train, K. 2010. “A Control Function Approach to Endogeneity in Consumer Choice Models,” Journal of Marketing Research (47:1), pp. 3-13.

Petris, G., Petrone, S., and Campagnoli, P. 2009. Dynamic Linear Models with R, New York: Springer.

Raman, K., Mantrala, M. K., Sridhar, S., and Tang, Y. E. 2012. “Optimal Resource Allocation with Time-Varying Marketing Effectiveness, Margins and Costs,” Journal of Interactive Marketing (26:1), pp. 43-52.

Rao, A. R., and Monroe, K. B. 1988. “The Moderating Effect of Prior Knowledge on Cue Utilization in Product Evaluations,” Journal of Consumer Research (15:2), pp. 253-264.

Reinartz, W., Thomas, J., and Kumar, V. 2005. “Balancing Acquisition and Retention Resources to Maximize Customer Profitability,” Journal of Marketing (69:1), pp. 63-79.

Roodman, D. 2009. “A Note on the Theme of Too Many Instruments,” Oxford Bulletin of Economics and Statistics (71:1), pp. 135-158.

Rossi, P. E. 2014. “Even the Rich Can Make Themselves Poor: A Critical Examination of IV Methods in Marketing Applications,” Marketing Science (33:5), pp. 655-672.

Ruppert, D., Wand, M. P., and Carroll, R. J. 2003. Semiparametric Regression, Cambridge, UK: Cambridge University Press.

Rust, R. T., Ambler, T., Carpenter, G. S., Kumar, V., and Srivastava, R. K. 2004. “Measuring Marketing Productivity: Current Knowledge and Future Directions,” Journal of Marketing (68:4), pp. 76-89.

Saboo, A. R., Grewal, R., and Chakravarty, A. 2016. “Organizational Debut on the Public Stage: Marketing Myopia and Initial Public Offerings,” Marketing Science (35:4), pp. 656-675.

Schunck, R. 2014. Transnational Activities and Immigrant Integration in Germany, New York: Springer.

Seiders, K., Voss, G. B., Grewal, D., and Godfrey, A. L. 2005. “Do Satisfied Customers Buy More? Examining Moderating Influences in a Retailing Context,” Journal of Marketing (69:4), pp. 26-43.

Shankar, V. 2008. “Strategic Marketing Resource Allocation: Methods and Insights,” in Marketing Mix Decisions: New Perspectives and Practices, R.A. Kerin and R. O’Regan (eds.). Chicago: American Marketing Association, pp. 154-183.

Shankar, V., Azar, P., and Fuller, M. 2008. “Practice Prize Paper—BRAN\* EQT: A Multicategory Brand Equity Model and Its Application at Allstate,” Marketing Science (27:4), pp. 567-584.

Shi, J. Q., and Choi, T. 2011. Gaussian Process Regression Analysis for Functional Data, Boca Raton, FL: CRC Press.

Simester, D. I., Sun, P., and Tsitsiklis, J. N. 2006. “Dynamic Catalog Mailing Policies,” Management Science (52:5), pp. 683-696.

Simonoff, J. S. 1996. Smoothing Methods in Statistics, New York: Springer.

Sloot, L. M., Fok, D., and Verhoef, P. C. 2006. “The Short- and Long-Term Impact of an Assortment Reduction on Category Sales,” Journal of Marketing Research (43:4), pp. 536-548.

Slotegraaf, R. J., and Pauwels, K. 2008. “The Impact of Brand Equity and Innovation on the Long-Term Effectiveness of Promotions,” Journal of Marketing Research (45:3), pp. 293-306.

Sriram, S., Chintagunta, P. K., and Neelamegham, R. 2006. “Effects of Brand Preference, Product Attributes, and Marketing Mix Variables in Technology Product Markets,” Marketing Science (25:5), pp. 440-456.

Steenkamp, J. B. E., and Baumgartner, H. 1992. “The Role of Optimum Stimulation Level in Exploratory Consumer Behavior,” Journal of Consumer Research (19:3), pp. 434-448.

Stern, P., and Hammond, K. 2004. “The Relationship Between Customer Loyalty and Purchase Incidence,” Marketing Letters (15:1), pp. 5-19.

Stremersch, S., and Lemmens, A. 2009. “Sales Growth of New Pharmaceuticals across the Globe: The Role of Regulatory Regimes,” Marketing Science (28:4), pp. 690-708.

Tan, X., Shiyko, M. P., Li, R., Li, Y., and Dierker, L. 2012. “A Time-Varying Effect Model for Intensive Longitudinal Data,” Psychological Methods (17:1), pp. 61-77.

Teel, J. E., Williams, R. H., and Bearden, W. O. 1980. “Correlates of Consumer Susceptibility to Coupons in New Grocery Product Introductions,” Journal of Advertising (9:3), pp. 31-46.

Van Heerde, H. J., Mela, C. F., and Manchanda, P. 2004. “The Dynamic Effect of Innovation on Market Structure,” Journal of Marketing Research (41:2), pp. 166-183.

Venkatesan, R., and Farris, P. W. 2012. “Measuring and Managing Returns from Retailer-Customized Coupon Campaigns,” Journal of Marketing (76:1), pp. 76-94.

Venkatesan, R., and Kumar, V. 2004. “A Customer Lifetime Value Framework for Customer Selection and Resource Allocation Strategy,” Journal of Marketing (68:4), pp. 106-125.

Venkatesan, R., Kumar, V., and Ravishanker, N. 2007. “Multichannel Shopping: Causes and Consequences,” Journal of Marketing (71:2), pp. 114-132.

Verhoef, P. C., Venkatesan, R., McAlister, L., Malthouse, E. C., Krafft, M., and Ganesan, S. 2010. “CRM in Data-Rich Multichannel Retailing Environments: A Review and Future Research Directions,” Journal of Interactive Marketing (24:2), pp. 121-137.

Walls, T. A., Jung, H., and Schwartz, J. E. 2006. Multilevel Models for Intensive Longitudinal Data, New York: Oxford University Press.

Wand, M. P. 2003. “Smoothing and Mixed Models,” Computational Statistics (18:2), pp. 223-249.

Wang, R., Saboo, A. R., and Grewal, R. 2015. “A Managerial Capital Perspective on Chief Marketing Officer Succession,” International Journal of Research in Marketing (32:2), pp. 164-178.

Wedel, M., and Kamakura, W. A. 2000. Market Segmentation: Conceptual and Methodological Foundations, Boston: Kluwer Publishing.

West, M., and Harrison, J. 1997. Bayesian Forecasting and Dynamic Models, New York: Springer.

West, M., Harrison, P. J., and Migon, H. S. 1985. “Dynamic Generalized Linear Models and Bayesian Forecasting,” Journal of the American Statistical Association (80:389), pp. 73-83.

Wiesel, T., Pauwels, K., and Arts, J. 2011. “Practice Prize Paper— Marketing's Profit Impact: Quantifying Online and Off-Line Funnel Progression,” Marketing Science (30:4), pp. 604-611.

Wooldridge, J. M. 2010. Econometric Analysis of Cross Section and Panel Data (2<sup>nd</sup> ed.), Cambridge, MAL The MIT press.

Wu, H., and Zhang, J.-T. 2006. Nonparametric Regression Methods for Longitudinal Data Analysis: Mixed-Effects Modeling Approaches, Hoboken, NJ: John Wiley & Sons.

Xie, J., Song, X. M., Sirbu, M., and Wang, Q. 1997. “Kalman Filter Estimation of New Product Diffusion Models,” Journal of Marketing Research (34:3), pp. 378-393.

Zikopoulos, P., Parasuraman, K., Deutsch, T., Giles, J., and Corrigan, D. 2012. Harness the Power of Big Data, New York: McGraw Hill.

## About the Authors

Alok R. Saboo is an assistant professor of Marketing and assistant director of the Center for Excellence in Brand & Customer Management, J. Mack Robinson College of Business, Georgia State University, Atlanta.

V. Kumar (VK) is the Regents’ Professor, Richard and Susan Lenny Distinguished Chair, and Professor of Marketing, and executive director, Center for Excellence in Brand & Customer Management, J. Mack Robinson College of Business, Georgia State University, Atlanta, GA, Chang Jiang Scholar, Huazhong University of Science and Technology, China, Senior Fellow, Indian School of Business, India, and and Faculty Fellow, Texas A&M University Institute for Advanced Study, College Station, TX.

Insu Park is a doctoral student in Marketing at the Center for Excellence in Brand & Customer Management, J. Mack Robinson College of Business, Georgia State University, Atlanta.
