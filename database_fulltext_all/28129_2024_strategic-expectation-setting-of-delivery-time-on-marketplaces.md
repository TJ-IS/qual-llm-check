---
otero_id: 28129
otero_key: "FT4PK6UT"
title: "Strategic Expectation Setting of Delivery Time on Marketplaces"
authors: "Si Xie; Siddhartha Sharma; Amit Mehra; Arslan Aziz"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0497"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Strategic Expectation Setting of Delivery Time on Marketplaces

Si Xie,<sup>a</sup> Siddhartha Sharma,<sup>b</sup> Amit Mehra,<sup>a,</sup>\* Arslan Aziz<sup>c</sup>

<sup>a</sup> Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080; <sup>b</sup> Kelley School of Business, Indiana University, Bloomington, Indiana 47405; <sup>c</sup> Meta Platforms, Inc., Vancouver, British Columbia H3B 2B2, Canada \*Corresponding author

Contact: sxx170008@utdallas.edu, https://orcid.org/0000-0002-2985-3731 (SX); sishar@iu.edu, https://orcid.org/0000-0002-6274-4086 (SS); Amit.Mehra@utdallas.edu, https://orcid.org/0000-0002-3822-9543 (AM); arslan.aziz7@gmail.com, https://orcid.org/0000-0003-3257-7130 (AA)

Received: September 23, 2021 Revised: January 26, 2023; November 21, 2023 Accepted: January 2, 2024 Published Online in Articles in Advance: February 23, 2024

https://doi.org/10.1287/isre.2021.0497

Copyright: © 2024 INFORMS

Abstract. Delivery speed is an essential component of the service provided by online delivery platforms. Because improving actual delivery speed is expensive, platforms can instead create a perception of faster delivery by showing a conservative estimate of the delivery duration when a customer places an order. We use detailed transaction-level data from a major food delivery platform to examine the effects of setting conservative delivery speed expectations on customers’ likelihood of future purchases and restaurant choices. When delivery is slower (faster) than expected, we find that customers are less (more) likely to purchase again from the platform and the focal (same) restaurant they ordered from. A reduction in purchases from the platform is expected to reduce purchases from nonfocal (other) restaurants as well; however, we find no significant impact. This is possibly because of a spillover effect, as customers may switch their purchasing to these restaurants. Our findings thus highlight the effect of setting conservative expected delivery times in a platform setting. Additionally, we provide evidence that customers with a consistent past delivery experience are less responsive to a single instance of positive or negative delivery performance. We further find heterogeneous effects of slower/faster than expected delivery on new versus existing customers and orders with zero versus nonzero delivery charges. These results suggest that the strategy to set conservative expected delivery times can be judiciously implemented for consumer segments for whom future demand is more likely to improve with a better delivery experience. Finally, we examine the trade-off between current and future demand with the setting of a conservative estimated delivery time. We do additional analysis and also conduct an experiment on Amazon Mechanical Turk to show that the gain in future demand is more than the loss in current demand, thus establishing the efficacy of our suggested strategy.

History: Ram Gopal, Senior Editor; Idris Adjerid, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0497.

Keywords: platform • delivery speed • expectancy disconfirmation • strategic management of IT

## 1. Introduction

Delivery speed is a critical component of service quality in e-commerce and offering quicker delivery increases sales (Fisher et al. 2019, Cui et al. 2020). Yet whereas the value of improving the delivery speed for platforms is clear, it is not always economically feasible to do so because of the high fixed costs of creating logistical infrastructure, such as distribution centers (Fisher et al. 2019), as well as high variable costs, such as deploying more last-mile delivery personnel. In this study, we examine if strategically setting expectations of the delivery time can improve the perception of delivery speed and, in turn, increase future purchases.

E-commerce businesses can create expectations of delivery speed by displaying an estimated time of delivery to consumers before they make a purchase. Whereas showing a low estimated time might entice users to make a purchase because of the short expected waiting time, there is another side to this story. The expectation created by the estimated time for the actual delivery time can influence the perception of delivery speed and hence affect consumer satisfaction (Tversky and Kahneman 1991). If the actual delivery duration is shorter than the estimated, this expectancy disconfirmation results in consumers having a positive experience (Ho et al. 2017), which may improve future demand, and vice versa (Cui et al. 2023).

We choose to focus our study on a distinct and notable context: food delivery platforms. In traditional food delivery setups, the delivery process is directly linked to the restaurant, as seen with popular examples like McDonald’s and Domino’s. In these cases, if a delivery is delayed, the blame is typically directed at the restaurant. However, the dynamics change when it comes to food delivery platforms. The unique two-sided market nature of these platforms adds an interesting dimension to the problem. The timeliness of a delivery experience can significantly impact a customer’s future decision to reorder, not just from the same restaurant that served the order but also from other restaurants on the platform. Further, the extent and nature of the impact could differ for the same and other restaurants. Finally, the demand on the platform is the sum total of the demand on all the restaurants. Therefore, the impact on the platform may be quite different compared with the effect on the restaurants.

Another reason we focus on food delivery platforms is that the effect on consumer demand because of the timeliness of deliveries can differ from typical e-commerce businesses. Even if consumer satisfaction improves when an order arrives earlier than expected in food delivery, it is unclear if this increase in satisfaction is significant enough to matter in influencing the future purchase behavior of consumers. The reason is that customers may not attribute much value to a few minutes of early delivery as opposed to an e-commerce setting where the actual delivery may happen even a day earlier than expected. In other words, the scope of beating delivery expectations is much larger in the context of standard e-commerce than in food delivery, and this difference may have a significant role in shaping consumer behavior.

Further, other aspects of the delivery experience, such as receiving the items that were ordered without any mistakes, may be more important in the context of food delivery. The reason is that if there are any mistakes in the order basket in an e-commerce retail setting, it is possible to return the wrong items and seek a replacement. However, any mistakes in the order basket in the context of food delivery may completely spoil the dining experience, as seeking a replacement is not a reasonable solution because of the time-sensitive nature of food consumption. Hence, consumers may value these other aspects of delivery and may not focus so much on a timely delivery experience.

Yet another difference between typical e-commerce and food delivery platforms is that consumers use the products they purchase using e-commerce multiple times (e.g., multiple use occasions of a shoe or apparel), whereas the food is consumed only once. Consumers may be reminded of a delivery experience when they repeatedly use a product. Because of such reminders, consumers may recall a delivery experience more effectively in e-commerce while making future orders. To summarize, the effect of beating delivery expectations is likely to differ in the context of food delivery compared with that in e-commerce because of multiple differences in these two contexts. Therefore, studying the impact of setting expectations for delivery times for food delivery platforms is a meaningful exercise.

To conduct our analysis, we use a large-scale transaction-level data set of more than 300,000 transactions placed on a food delivery platform in a large Asian city over a period of 10 weeks. We observe detailed information about each transaction, including the estimated delivery time displayed to the user prio to purchase, as well as the actual delivery time. Thus, we are able to directly measure both the customer’s expectations as well as the actual delivery performance. We estimate how delivery performance affects customers’ future purchase probability from the platform, from the restaurant that served their order, and from other restaurants, using propensity score weighting and multiple high-dimensional fixed effects, and we combine it with the recently developed double machine learning (DML) method for a semiparametric inference that makes the regression model robust to any misspecification (Chernozhukov et al. 2018).

We find that the extent of discrepancy between the actual and estimated delivery determines consumers future purchases. Specifically, for a given estimated time to delivery, an increase in actual delivery time leads to lower future purchases from the platform and from the same restaurant (the restaurant that served the order) while having no significant effect on the purchase probability from other restaurants. One may expect that a reduction in orders on the platform should result in a reduction in orders from other restaurants as well. This outcome does not happen because of a spillover effect that when consumers reduce their purchases from the same restaurant, they increase it from other restaurants, leading to an insignificant effect on demand. This result is because of the platform context and cannot be expected in the case of a pure online merchant. We also find that our main results remain robust to the alternative matching method of coarsened exact matching and using continuous (rather than binary) treatment measures.

Further, we examine several heterogeneous effects. First, we study how a customer’s experience on the platform moderates their response to delivery performance. We find that the effect of delivery expectations is relatively weaker for users who have experienced consistently delayed or early deliveries. Customers with a consistent recent experience are less influenced by each individual transaction’s delivery performance, likely because they learn the platform’s “true” service quality from prior purchases. Second, we analyze subsamples with orders having zero and positive delivery charges. We find that for orders with zero delivery charge, there is no effect of the delivery performance on future orders from the platform, whereas there is a relatively subdued effect on the same restaurant. Interestingly, we observe that bad delivery performance of a transaction increases future orders from other restaurants. This find ing points to a relatively stronger spillover effect for this subsample. Third, we analyze subsamples consisting of only new customers and existing customers. We find that for new customers, the effect of timely deliveries is more salient. These findings suggest that implementing an algorithm showing conservative delivery times can be more effective for new customers and in transactions with nonzero delivery charges. For existing customers, this strategy may work better when a customer has had inconsistent delivery experiences in the past.

Our suggestion to improve the perception of delivery times to increase demand is open to a challenge. Displaying a more conservative estimated time can increase repurchase probability but may deter some consumers from placing orders in the first place. If the platform loses more current orders than it gains in the future by setting a conservative expected delivery time, then our suggested strategy will not be effective. To analyze this trade-off, we need to ascertain how many orders are lost as the estimated delivery times are made more conservative. Such an analysis requires access to users’ app browsing data that we do not have. Therefore, it is not possible to directly analyze the loss in current orders at the customer level. Even under this limitation, we can assess the relative impact of longer estimated delivery times on current and future orders through two approaches. One is by aggregating our observational data at the restaurantweek level. We find that the negative effect on orders in the current week (the loss) is smaller in magnitude than the positive effect on orders in the following week (the gain), suggesting that it could be beneficial for platforms to set a conservative estimated time to delivery. Our second approach is to conduct a survey-based experiment on Amazon Mechanical Turk (AMT). In the experiment, we manipulate the estimated delivery time shown to the participants while keeping the actual delivery time the same across all treatment groups. The results from the experiment suggest that the loss in current orders is smaller than the gain in future orders, again indicating that the total demand is likely to increase with the strategy to set conservative estimated delivery times.

The roadmap for the rest of the paper is as follows. In the next section, we discuss the related literature and further clarify our contributions. After that, we discuss our hypotheses. Then, we provide the institutional details and describe our data. Next, we present our identification strategy and discuss the results. We then conduct some robustness checks, followed by a section exploring the trade-off on current versus future orders. Finally, we close the paper with some concluding remarks.

## 2. Related Literature

Our work is related to three streams of literature: the impact of delivery performance, the strategic use of reference dependence by firms to improve consumer perception, and the role of platforms’ policies on sales diversity. Here, we discuss each of these strands of research and describe how we contribute to them.

## 2.1. The Costs and Benefits of Fast Delivery

Several empirical studies have found that fast and efficient order fulfillment has a positive relationship with customer satisfaction and sales (Allon et al. 2011). Removing a quicker delivery option reduces sales and increases sales dispersion (Cui and Shin 2018), whereas an increase in delivery speed can increase sales online (Fisher et al. 2019, Cui et al. 2020). Other positive effects of quicker deliveries are the ability to set higher prices (Peng and Lu 2017), greater customer loyalty (Rosenbaum et al. 2007), and higher ratings (Deshpande and Pendem 2022).

Whereas the numerous benefits of implementing fast delivery are widely recognized, significant investment in upgrading the platform’s logistics infrastructure, such as opening more distribution centers (Fisher et al. 2019) or hiring more delivery personnel (Gao and Su 2018), is required to improve the delivery speed. Other additional costs in the food delivery context may arise from upgrading the IT infrastructure to relay requests to restaurants in real time and investing in the coordination of delivery personnel geographically. Thus, platforms need to compare the benefits of quick delivery with the costs of enabling it.

Whereas the past literature has focused on analyzing the impact of actual delivery speed, firms may influence customer satisfaction by changing delivery speed expectations by manipulating estimated delivery time. Specifically, instead of improving the actual delivery speed, firms can strategically increase the estimated delivery time to enhance the perceived delivery experience. Notably, in the context of an online retailer, Cui et al. (2023) find that a faster delivery promise increases sales, but it also increases product returns and reduces customer retention. In this paper, we contribute to this stream of literature by investigating a hitherto underexamined lever available to platforms to improve customer satisfaction without incurring the high costs of improving their logistics capacity. In particular, we measure how the discrepancy between the estimated delivery time and the actual delivery time affects a consumer’s future purchases in the context of a marketplace.

## 2.2. Strategic Use of Reference-Dependent Preferences

Reference dependence is a fundamental principle of prospect theory and behavioral economics (Tversky and Kahneman 1974). According to this principle, people realize gains and losses by evaluating outcomes relative to a reference point (Tversky and Kahneman

1991). Therefore, it is important to study how reference points are formed. Related studies suggest that consumers may utilize only certain kinds of information to form their reference point (Terzi et al. 2016, Baillon et al. 2020). In our context, if users do form a reference point based on the estimated time and the actual delivery duration is shorter than the estimated duration, then it may enhance customer satisfaction through the theory of expectancy disconfirmation (Oliver 2014, Ho et al. 2017). This theory argues that satisfaction/ dissatisfaction results from a customer’s comparison of performance (of a product or service) with predetermined standards; this is in line with the reference dependence theory applied to our customer satisfaction context.

A stream of literature focuses on the strategic use of reference points by firms (Fiegenbaum et al. 1996). For instance, Ho and Zheng (2004) study how a firm might choose a delivery time commitment to influence its customer expectation through a game-theoretic model, whereas Roels and Su (2014) theoretically analyze how a social planner may set different reference structures to influence users to achieve different goals. There is also some empirical work showcasing the strategic value of reference point formation. Yu et al. (2017) demonstrate that providing delay announcements improves a call center’s performance given the reference-dependent consumer behavior observed in data. Using driving behavior data in the context of automotive telematics, Choudhary et al. (2021) find that drivers just below the insurance-incentive thresholds exert greater effort to improve their driving. In the context of performing arts, Tereyag˘og˘lu et al. (2018) suggest policies for revenue management that exploit consumers’ reference point formation regarding ticket prices and seat utilization.

The goal of our study is to empirically investigate whether there is a strategic advantage for a platform if it is able to affect customers’ reference points by setting a higher estimated delivery time. To the best of our knowledge, there is no research study that examines reference point formation and how it may be utilized by platforms in the context of food delivery. We contribute to this literature by examining reference dependence and expectancy disconfirmation in the context of hyperlocal services. Hyperlocal services provide a unique context because estimated delivery times tend to be extremely short in this setting, often less than an hour on average, as opposed to a few days in e-commerce settings. Further, in our context of food delivery, it is possible that consumers only care about the actual delivery (waiting) time, particularly because the actual delivery time is linked with the product quality attributes such as the freshness of food. Because of these characteristics, the role of delivery time expectations can be distinct compared with standard e-commerce settings, making it an interesting empirical question to examine.

## 2.3. Impact of Platform Features on Sales Diversity

This study is also related to the growing literature on platform strategy and design (Erev and Roth 1998). Past literature on two-sided markets has studied how a platform’s policies such as the recommender systems impact the diversity of sales and finds that, typically, sales diversity at the aggregate level reduces, but individuallevel sales may become more diverse because of recommender systems (Fleder and Hosanagar 2009, Hosanagar et al. 2014, Lee and Hosanagar 2019).

In the food delivery platform context, consumers purchase repeatedly from the platform and choose whether to purchase from the same restaurant or diversify by ordering from other restaurants. Hence, in this paper, we look at how a platform’s strategic setting of the estimated delivery time can impact the exploreexploit behavior of customers across different restaurants. Current literature has, so far, not analyzed these questions, and to the best of our knowledge, we are the first to investigate the perceived aspect of service delivery performance on sales diversity.

## 3. Hypotheses Development

In this section, we hypothesize the impact of delayed delivery on the probability of a future purchase from the platform, the same restaurant, and other restaurants. We also propose additional hypotheses on how these effects may vary based on the consistency of the experience of a customer.

## 3.1. The Effect of Delayed Delivery on Future Purchases

As discussed previously, past studies have examined the effect of the absolute speed of delivery on sales. We focus not on the delivery speed but on the perceived delivery performance on repeat purchases. The perception of delivery performance could be created based on the delivery speed relative to the expectations set for the customers (Ho and Zheng 2004). This strategy is based on the theory of reference dependence, which suggests that people realize gains and losses by evaluating outcomes relative to a reference point (Tversky and Kahneman 1991). Firms can possibly create a reference point for delivery speed by setting an estimated delivery speed.

However, it is not necessary that the user processes and utilizes this information to form a reference point, perhaps because of limited attention (Kahneman 1973). Moreover, firms typically provide information about several product/service-related attributes. It is therefore possible that users may ignore the estimated delivery time provided by the platform because they could be more focused on other information such as the quality of the restaurant, or they tend to falsely conform to their preconceived notions (Walters and Hershfield 2020).

If the information regarding the estimated delivery time is indeed processed and utilized by the user, it may help form the reference point or an expectation for the actual delivery time (Lord and Maher 2002, Lindsay and Norman 2013). Based on the theory of expectancy disconfirmation (Oliver 2014), a customer’s satisfaction/dissatisfaction results from them comparing the performance of a product or service with predetermined standards (reference point). In our context, the discrepancy between the actual delivery time and the estimated delivery time set by the platform can affect customer satisfaction with the platform’s delivery service through a positive (if early) or a negative (if delayed) experience. This experience, in turn, can affect the likelihood of future purchases. Further, given that customers are very time sensitive in the context of food delivery (Allon et al. 2011), the positive effect of quicker delivery on customer satisfaction is likely to be more pronounced than in other contexts. Therefore, we hypothesize that

Hypothesis 1. The probability of a future purchase from the platform decreases when the actual delivery takes longer than the estimated time.

The direct effect of customers reducing their future orders from the platform because of the delay is likely to reduce the orders from the restaurant from where they made their focal order. In addition, there is a possibility of yet another effect. In traditional retailerconsumer contexts, customers form an expectation only regarding the retailer’s attributes, thereby impacting their transactions with the retailer. However, in a twosided platform context such as ours, the customers may use estimated time as a reference to evaluate the performance of the platform and also the restaurants (thirdparty sellers) participating on the platform. Customers make an explore-exploit decision each time they choose to purchase from the platform: whether to purchase from an untried restaurant, with uncertain rewards, or purchase from the restaurants they already know (Navarro et al. 2016). If customers believe that the restaurant is at least partly responsible for delayed delivery by not ensuring quick food preparation and smooth hand-off to the delivery personnel, then they are likely to lean less toward exploiting the same restaurant in the future. That is, even when customers make a decision to purchase from the platform, they are less likely to make a repeat purchase from the same restaurant. Because of these reasons, we hypothesize that

Hypothesis 2. The probability of a future purchase from the same restaurant decreases when the actual delivery takes longer than the estimated time.

Because a delay in delivery is hypothesized (Hypothesis 1) to reduce the probability of future orders from the platform, it can directly result in a decrease in the probability of future purchases from other restaurants. However, if the customer partly attributes the delay to the same restaurant, there can be a positive spillover effect of customers switching to other restaurants on the platform, that is, inclining toward exploring more options. Consequently, the probability of future purchases from other restaurants can increase with the delay as well. Because of these opposing possibilities, it is an open empirical question whether delayed deliveries increase or decrease future purchases from other restaurants. Therefore, we also investigate how a delayed delivery impacts future purchases from other restaurants on the platform.

## 3.2. The Moderating Effect of Consistent Experience

The hypotheses developed so far are for the effects on the average customer. However, customer characteristics such as their past experience may influence their satisfaction with the delivery (Ho and Zheng 2004). Here, we focus on how the heterogeneity of the effects is based on the consistency in the delivery experience of a customer. Specifically, compared with a customer without consistent prior experience on the platform, the delay of the focal transaction could have less impact on the future purchase probability for a customer who has consistently experienced delayed or early deliveries in the past. This behavior may result from customers forming their own opinions of the delivery performance based on consistent experiences of delivery. In case the experience has been inconsistent, then the customer would still learn something from the current focal transaction and therefore is more likely to be affected. In sum, the focal transaction’s experience would matter more when the past experiences have been inconsistent.

Hypothesis 3. The effect of delayed delivery on future purchases from the platform is weaker for users with a consistent experience.

## 4. Empirical Context and Data

Our data come from an online food delivery platform operating nationally in one of the biggest economies in Asia. When a user uses the platform’s app to order, the estimated delivery time (denoted by EstTime) is displayed prominently for each restaurant, as shown in Figure 1. The estimated time may set the expectation for the user against which they compare the actual delivery time (denoted by DelTime). The actual delivery time is measured from the moment the customer places an order to when it is delivered to the customer. The platform attempts to predict the actual delivery time through the estimated delivery time. The algorithm used to calculate the estimated delivery time is proprietary to the platform. It takes into account several factors such as the distance between the user and the restaurant, the traffic on the route, the food preparation time, and the availability of delivery personnel in the area.<sup>1</sup>

Figure 1. Mobile App Layout  
![](/api/attachments/FT4PK6UT/fulltext/images/d942947589c37c895ecf5724c00e3ba1164f7cafbd82a0c0ad1dc7daeabb133c.jpg)

A delivery is considered delayed if the actual delivery took longer than the estimated duration. We denote delayed deliveries using a binary indicator called Delayed, which takes the value of one if delayed and zero otherwise. The numerical difference between the actual and estimated delivery time is represented by Delay Length. Whether a delivery is delayed depends on both the restaurant’s and platform’s service quality. If the restaurant delays the preparation of the order, the platform’s delivery personnel have little recourse but to wait for the order to be prepared. On the other hand, even if a restaurant has prepared the order early, the delivery person may be delayed in picking up the order or completing the delivery.

We use 359,368 transactions from 81,341 customers across 2,264 restaurants that have more than one transaction on the platform in a single large city over a period of 10 consecutive weeks. For each transaction, we observe unique customer and restaurant IDs, date, estimated delivery time, actual delivery time, total delivery charge in USD (Delivery Charge), total bill amount in USD (Bill Amount), and whether the transac tion is done by a first-time user (New User). We furthe observe the feedback ratings given by the customers. A customer is prompted to offer two types of feedback ratings for each transaction, delivery feedback (Delivery Rating) and restaurant feedback (Restaurant Rating). The delivery feedback is intended to capture the customer’s satisfaction, or a lack thereof, from the delivery process, whereas the restaurant feedback is intended to reflect the customer’s satisfaction with the restaurant’s product quality. We further derive additional variables: (i) the total number of transactions of a restaurant in a particular week (Rest Week Count) to capture the timevarying popularity of a restaurant, and (ii) whether the focal transaction and the previous transaction within a week of a customer were both delayed or early through a binary indicator called Consistent Experience. Table 1 presents the variables and their descriptions.

We present the summary statistics of the data in Table 2. The customer rating of the restaurant averages 3.99, and the delivery rating has a mean value of 4.36. Thus, there is variation in how customers rate the restaurant (food) and the delivery. The means of deliv ery charge and the total bill amount are \$0.23 and \$4.72, respectively. These values are typical for the Asian country under consideration. About 11% of the transactions were conducted by first-time customers, whereas others were made by repeat customers. We also observe that there is considerable variation in the intensity of usage across customers. Half of the customers had more than six transactions during the sample period. The mean number of transactions for the restaurant per week is 40.8. For ones who had a consistent recent experience, 16% of the transactions the customer experienced consistently delayed orders. On average, for 49% of the transactions, the customer made a repeat purchase in the next seven days on the platform, of which 45% come from the same restaurant and 55% are from other restaurants. The mean Delay Length is �4.64 minutes, indicating the delivery arrives early on average. About 30% of orders are delivered late.

Table 1. Variable Descriptions

<table><tr><td>Variable</td><td>Description</td></tr><tr><td>EstTime</td><td>Estimated delivery time by the platform (in minutes)</td></tr><tr><td>DelTime</td><td>Actual delivery time (in minutes)</td></tr><tr><td>Delayed</td><td>Whether the actual delivery time is greater than the estimated (zero or one)</td></tr><tr><td>Delay Length</td><td>Difference between actual and estimated delivery times (in minutes)</td></tr><tr><td>Consistent Experience</td><td>Whether the focal transaction and the transaction in the previous week were both delayed or early (zero or one)</td></tr><tr><td>Delivery Rating</td><td>Delivery feedback (in stars)</td></tr><tr><td>Restaurant Rating</td><td>Restaurant feedback (in stars)</td></tr><tr><td>Delivery Charge</td><td>Delivery charge in USD</td></tr><tr><td>New User</td><td>Whether the transaction is by a first-time user (zero or one)</td></tr><tr><td>Bill Amount</td><td>Total bill amount in USD</td></tr><tr><td>Rest Week Count</td><td>Number of transactions of a restaurant in a week</td></tr></table>

Table 2. Descriptive Statistics

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td><td>Min</td><td>Max</td></tr><tr><td>EstTime</td><td>42.5</td><td>7.6</td><td>20</td><td>65</td></tr><tr><td>DelTime</td><td>37.8</td><td>12.6</td><td>15</td><td>80</td></tr><tr><td>Delayed</td><td>0.30</td><td>0.46</td><td>0</td><td>1</td></tr><tr><td>Delay Length</td><td>-4.64</td><td>11.83</td><td>-45</td><td>51</td></tr><tr><td>Consistent Experience</td><td>0.25</td><td>0.43</td><td>0</td><td>1</td></tr><tr><td>Delivery Rating</td><td>4.36</td><td>1.02</td><td>0</td><td>5</td></tr><tr><td>Restaurant Rating</td><td>3.99</td><td>1.36</td><td>0</td><td>5</td></tr><tr><td>Delivery Charge</td><td>0.23</td><td>0.25</td><td>0</td><td>0.71</td></tr><tr><td>New User</td><td>0.11</td><td>0.32</td><td>0</td><td>1</td></tr><tr><td>Bill Amount</td><td>4.72</td><td>3.75</td><td>0.1</td><td>100</td></tr><tr><td>Rest Week Count</td><td>40.8</td><td>55.0</td><td>1</td><td>555</td></tr></table>

## 5. Empirical Analysis

Our primary research question is to examine the impact of a delayed delivery in the focal transaction on the probability of a future purchase from the platform, the same restaurant, or other restaurants. Therefore, for any focal transaction by a customer with a restaurant, our main independent variable is whether the delivery is late (Delayed). Our main dependent variable is whether the customer makes a purchase from the platform, the same restaurant, or another restaurant in the next seven days.

We use multiple high-dimensional fixed effects because they can accommodate various factors that potentially bias our estimates. As we observe multiple transactions made by one customer, we can include customer-level fixed effects to account for unobserved heterogeneity in behavior across different customers. To resolve the selection issue because of unobserved heterogeneity across restaurants, we include restaurant-level fixed effects. In addition, we also include the date-level fixed effects that account for any time trends in purchases over the sample period. Further, to control for the effect of other potential factors that may influence the focal transaction’s delivery and future purchases, we include Del Time, Delivery Charge, Restaurant Rating, New User, and Bill Amount as covariates.

To estimate the effects, we utilize the recently developed semiparametric inference framework called double machine learning introduced by Chernozhukov et al. (2018), which can be used to consistently estimate the treatment effects. DML extends the partialling-out procedure of Frisch-Waugh-Lovell (Frisch and Waugh

1933, Lovell 1963) to use flexible nonparametric functions estimated via machine learning.

Using DML is strongly recommended in situations where it is expected that the control variables are likely to affect dependent variables nonlinearly and there is scant theoretical justification for a specific form of nonlinearity $( \mathrm { e . g . }$ , a logarithmic or a second-degree term of a control variable). In such cases, if we include the controls linearly, or even nonlinearly with the incorrect form of the nonlinear specification, then our coefficient estimate of the treatment variable will be biased because of the misspecification of the control variables (Stanley and Jarrell 2005). In our context, a key control variable is actual delivery time. This actual delivery time represents the waiting time for customers before they get their orders. It is well-known in extant literature that the psychological cost of waiting time for customers is nonlinear (Dahm et al. 2018, Lin et al. 2023). However, the form of the nonlinearity can be context specific, and it is unclear what form it would take in the context of food delivery. The strength of the DML approach is that it does not impose any specific form on nonlinearity ex ante and discovers this form from the data itself, thus alleviating the problem of bias in the treatment estimate because of misspecification of the control variable.

DML builds upon the following partially linear probability model (Robinson 1988):

$$
\begin{array}{r} Y _ {n i j t} = \beta D e l a y e d _ {n i j t} + g (X _ {n i j t}) + u _ {n i j t}, \\ \mathbb {E} [ u _ {n i j t} | D e l a y e d _ {n i j t}, X _ {n i j t} ] = 0, \end{array}\tag{1}
$$

$$
\begin{array}{r} D e l a y e d _ {n i j t} = h (X _ {n i j t}) + v _ {n j i t}, \\ \mathbb {E} [ v _ {n i j t} | X _ {n i j t} ] = 0, \end{array}\tag{2}
$$

$$
\hat {u} _ {n i j t} = \beta \hat {v} _ {n i j t} + \gamma_ {i} + \lambda_ {j} + \tau_ {t} + \epsilon_ {n i j t},\tag{3}
$$

where n represents a unique transaction (this transaction takes place between customer i and restaurant j on date t); $Y _ { n i j t }$ is the dependent variable, a binary indicator for whether customer i has made a purchase from the platform, the same restaurant j, or other restaurants $j ^ { C }$ in the following seven days; Delayed is our main independent variable, whether the delivery of the focal transaction is late or not; and $X _ { n i j t }$ is the set of control variables for the effect of other potential factors that may influence both the delay in delivery and future purchases by the customer $i , g ( )$ and h() are unknown nonparametric functions that model the covariates and are called “nuisance” parameters. $u _ { n i j t }$ and $v _ { n i j t }$ are Gaussian error terms with zero conditional mean.

We are interested in consistently estimating and per forming a valid inference on $\beta ,$ for which we adopt the DML method. The DML procedure is as follows. We estimate two nonparametric functions, $\psi ( )$ and $\phi ( ) .$ First, we estimate the conditional expectation function $\psi ( X _ { n i j t } ) = \mathbb { E } [ Y _ { n i j t } | X _ { n i j t } ]$ to get $\hat { \psi } ( \boldsymbol { \mathbf { \rho } } )$ using an ML algorithm such as gradient boosting (Yang et al. 2020). That is, we model Y based on the control variables X. We achieve this by randomly dividing the data set into two equal parts: sample A and sample B. Initially, we train a model using one of the samples, say A, and make predictions for the other sample (B). This enables us to obtain $\hat { \psi } ( \boldsymbol { \mathbf { \rho } } )$ for sample B. Next, we reverse the roles of the two subsamples, which results in $\hat { \psi } ( \boldsymbol { \mathbf { \rho } } )$ for sample A. Second, we similarly estimate the conditional expectation function $\phi ( X _ { n i j t } ) = \mathbb { E } [ D e l a y e d _ { n i j t } | X _ { n i j t } ]$ to obtain $\hat { \phi } ( \ v { r } )$ for all the points. The procedure of estimating $\hat { \phi } ( \ v u )$ is the same as that of estimating $\hat { \psi } ( \boldsymbol { \mathbf { \rho } } )$ . That is, we model Delayed based on the control variables X. Third, we calculate the outcome residuals $\tilde { Y } _ { n i j t } = Y _ { n i j t } - \hat { \psi } _ { \underline { { { \imath } } } } ( X _ { n i j t } )$ Fourth, we estimate the treatment residuals De <sup>˜</sup>layed $= D e l a y e d _ { n i j t } - \hat { \phi } ( X _ { n i j t } )$ . Last, to obtain ${ \hat { \beta } } ,$ we regress $\tilde { Y } _ { n i j t }$ on $D e l a y e \dot { d } _ { n i j t }$ while including date, restaurant, and customer fixed effects. The DML procedure guarantees ${ \sqrt { n } } .$ -consistent and asymptotically normal estimates (Chernozhukov et al. 2018).

The effect of Delayed is identified by the difference in probability of repeat purchase between delayed and early transactions after accounting for differences across different customers, restaurants, and days and also after controlling for multiple time-varying confounders.<sup>2</sup>

## 5.1. Main Results

Columns (1) to (3) of Table 3 report the estimated effects of delayed delivery on the customers’ future purchase probability on the platform, the same restaurant, and other restaurants. Note that all our analyses include date fixed effects to control for time trends.<sup>3</sup> We find that the coefficient estimates for Delayed in columns (1) and (2) are negative and statistically significant, which indicates that a late delivery reduces the probability of repeat purchase probability from the platform and the same restaurant. Specifically, the probability of a repeat purchase in the next seven days from the platform decreases by 0.24% points, which is a 0.54% decrease from the baseline probability, whereas the probability of future purchases from the same restaurant decreases by 0.72% points (3.2%). On the other hand, the coefficient of Delayed is positive in column (3) at a 10% level of significance.

This implies that a customer’s decision to order from other (nonfocal) restaurants on the platform is not significantly influenced by experiencing a delay previously. Potentially, there are two opposing effects of a delayed order on nonfocal restaurants. First, there is a negative effect because the customers might hold the platform responsible, which affects all the restaurants. Second, there is a positive spillover effect, as the customers might only hold the focal restaurant responsible for the delay and hence may switch to other restaurants on the platform. The estimates suggest that, on average, these two effects seem to result in a rather small effect on other restaurants.

However, despite including transaction-level covariates and date-, customer-, and restaurant-level fixed effects, there could remain certain selection-intotreatment biases. To further resolve such issues, in this section, we present our empirical analyses and findings using two alternative approaches. The first approach utilizes propensity scores to assign weights to delayed and early transactions before estimating the effect using DML, whereas the second approach uses interaction (cross) fixed effects between a customer and a restaurant that exploit the variation in Delayed across transactions within the same customer-restaurant pair.

## 5.2. Inverse Propensity Score Weighting

To account for the potential differences across transactions, we use inverse probability weighting using propensity scores. Specifically, we assign a weight to each observation (transaction) with the inverse of the propensity score.

We first compute the propensity score $p ( X _ { n } )$ for each transaction n using a logit model and transaction-level variables $( X _ { n } )$ such as the actual delivery time, delivery charge, rating given to the restaurant, whether the transaction is the first transaction of the customer, and the total bill amount of the transaction n. Then, we use the inverse of the propensity scores to assign weights to transactions so that the distribution of the covariates is independent of whether the transaction is delayed. The inverse probability weights are given by $W e i g h t _ { n } =$ $[ D e l a y e d _ { n } ^ { - } / p ( X _ { n } ) + \bar { ( 1 - D e l a y e d _ { n } ) } / ( \bar { 1 } - p ( X _ { n } ) ) ]$ . We check and find that, after propensity score weighting, the two groups of transactions are well balanced on all the covariates (see Section A of the online appendix). Using these computed weights, we estimate the regression model in the last step of the DML procedure.

Table 3. Impact of Late Delivery on the Probability of Repurchase (GradBoost)

<table><tr><td rowspan="2">Variable</td><td colspan="3">No matching</td><td colspan="3">IPW</td></tr><tr><td>(1) Platform</td><td>(2) Same</td><td>(3) Others</td><td>(4) Platform</td><td>(5) Same</td><td>(6) Others</td></tr><tr><td>Delayed</td><td>-0.0024**(0.0012)</td><td>-0.0072***(0.0020)</td><td>0.0055*(0.0030)</td><td>-0.0032***(0.0011)</td><td>-0.0063***(0.0019)</td><td>0.0031(0.0027)</td></tr><tr><td>Customer FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Restaurant FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>341,766</td><td>341,766</td><td>341,766</td><td>341,766</td><td>341,766</td><td>341,766</td></tr></table>

\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.  
Notes. Robust standard errors in parentheses. FE, fixed effects.

The coefficients estimated are reported in Table 3, and columns (4) to (6) show the results for the probability of a repeat purchase from the platform, the same restaurant, and other restaurants, respectively. We note that the coefficient estimates for Delayed in the fourth and fifth columns are still negative and statistically significant, which indicates that a late delivery reduces the probability of a repeat purchase from the platform and the same restaurant. Specifically, the probability of a repeat purchase in the next seven days from the platform decreases by 0.32% points (0.7%), whereas the probability of future purchases from the same restaurant decreases by 0.63% points (2.8%). However, the coefficient estimate for Delayed in column (6) is insignificant, suggesting that the probability of a repeat purchase from other restaurants is not affected by delayed transactions.

## 5.3. Restaurant <sup>3</sup> Customer Fixed Effects

Now, as an alternative approach, we exploit the variation in Delayed within the same customer-restaurant pair. This particularly reduces the bias of our estimate if a customer behaves differently across restaurants because of the variation in their preference across restaurants. We do so by including customer-restaurant fixed effects, that is, the interaction between the customer and restaurant Restaurant × Customer, thus resolving the selection issue related to a customer’s preference for a restaurant.

The results are presented in Table 4. Column (1) provides the estimates for the probability of a repeat purchase from the platform, column (2) for the same restaurant, and column (3) presents the results for other restaurants in the next seven days. Consistent with the findings based on our previous approach, the coefficient of Delayed is negative and statistically significant in columns (1) and (2) and insignificant in column (3). This implies that, on average, early delivery increases the probability of the customer making another order from the platform and the same restaurant in the next seven days.

Table 4. Impact of Late Delivery on the Probability of Repurchase with Restaurant × Customer Fixed Effects

<table><tr><td>Variable</td><td>(1) Platform</td><td>(2) Same</td><td>(3) Others</td></tr><tr><td>Delayed</td><td>-0.0077**(0.0038)</td><td>-0.0134***(0.0051)</td><td>0.0056(0.0050)</td></tr><tr><td>Restaurant × Customer FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>139,742</td><td>139,742</td><td>139,742</td></tr></table>

Note. Robust standard errors in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

## 6. Heterogeneous Effects

In this section, we analyze whether and how our effect size varies across different subsamples based on userand transaction-level characteristics. The results from the analyses in this section help us confirm the mechanism behind our main effect and also suggest groups of transactions where our proposed strategy would be more effective.

## 6.1. Consistent Experience

In addition to the effect of Delayed on the probability of repurchasing, we also analyze the moderating effect of past experience. According to our theory, one would expect that the focal transaction’s experience would play a smaller role in forming future expectations if the user can bank upon their own past experience. Specifi cally, as discussed in Hypothesis 3, if a user’s own delivery experiences on the platform have been consistently positive or negative, then one focal transaction’s effect on future decisions would be mitigated. Further, if there is a long gap between the focal and past transactions, then the customer’s experiences, although consistent, may not be fresh in that customer’s memory, and hence, the focal transaction’s delivery experience could still affect future outcomes significantly. Accordingly, we construct a variable, Consistent Experience, which indicates whether a customer has had the same deliv ery experience in the focal transaction and the previous transaction within the last seven days on the platform. This consistency could be either good (both early deliveries) or bad (both late deliveries).

In order to find the moderating effect, we rerun our analysis of Table 5 after adding the interaction between the delay and the recent experience consistency, that is, Delayed × Consistent Experience, our independent variable of interest here. Consistent with our third hypothesis, we find that the coefficient of the interaction between Delayed and having a consistent experience is positive and statistically significant (see Table 5). This implies that if the past experience of the restaurant is consistent, then the negative (positive) impact of the focal order arriving later (earlier) than the estimated time on future purchases from the platform and the same restaurant is reduced.

Table 5. Heterogeneous Effects of Recent Consistent Experience

<table><tr><td>Variable</td><td>(1) Platform</td><td>(2) Same</td><td>(3) Others</td></tr><tr><td>Consistent Experience × Delayed</td><td>0.0364***(0.0078)</td><td>0.0315***(0.0080)</td><td>0.0036(0.0078)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Restaurant × Customer FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>139,742</td><td>139,742</td><td>139,742</td></tr></table>

Note. Robust standard errors in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

Table 6. Heterogeneous Effects of Delay Window

<table><tr><td>Variable</td><td>(1) Platform</td><td>(2) Platform</td><td>(3) Platform</td></tr><tr><td>Delayed</td><td>-0.0077**(0.0038)</td><td></td><td></td></tr><tr><td>Delayed10</td><td></td><td>-0.0098***(0.0035)</td><td></td></tr><tr><td>Delayed20</td><td></td><td></td><td>-0.0144***(0.0037)</td></tr><tr><td>Restaurant × Customer FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>139,742</td><td>139,742</td><td>139,742</td></tr></table>

Note. Robust standard errors in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

## 6.2. Extent of the Delay

We find that the effect of Delayed on the future purchase probability from the platform is negative. The magnitude of this effect, however, is likely driven by the extent of delivery being late because a customer is more likely to recall an experience if that customer was significantly satisfied or dissatisfied in the past. To check if the length of the delay is indeed a factor in explaining our results, we redefine Delayed based on the absolute difference between actual and estimated delivery times. Rather than the zero-minute threshold we used earlier, an order is considered late when the actual delivery time is more than 10 or 20 minutes late. We rerun our analysis of Table 4 with the two new definitions of Delayed. Table 6 presents the results.

Column (1) presents the original Delayed definition as the benchmark case, whereas columns (2) and (3) show the results for the two new definitions. We find that the coefficient estimates of Delayed are negative and statistically significant. Importantly, we find that the magnitude of the effect increases significantly as the delay window increases. This implies that customers’ tolerance for the delivery is largely driven by the length of the delay.

## 6.3. Zero and Positive Delivery Charges

Another possible factor that could influence the effect of Delayed is the delivery fee. Customers are more likely to be forgiving of delays when they do not pay a delivery fee, and they might value a timely delivery more when they pay for it. To check if the delivery charge is indeed a factor in explaining our results, we split the sample into two subsamples based on whether the delivery charge is zero or positive and rerun our analy sis. The results are reported in Table 7. We find that the negative impact of making a delayed delivery is greater for transactions in case the delivery is not free. In fact, the impact on the platform is insignificant in the case of transactions with zero delivery charges. This implies that the strategy to use a conservative estimated time to delivery is more likely to be effective for transactions with a positive delivery fee.

Interestingly, we further find that in the case of transactions with free delivery, there is a positive spillover effect of delayed delivery by a focal restaurant on nonfocal restaurants. This result highlights the role of a twosided market scenario where a delayed delivery does not have a significant impact on the platform as the future demand gets redistributed among restaurants.

## 6.4. New vs. Existing customers

Next, we analyze how the effect of delayed deliveries on future orders is moderated by new and existing users<sup>4</sup> on the platform. The new users do not have previous delivery experiences with the platform and hence cannot set their expectations based on this experience. Existing users, on the other hand, do have previous experience and hence may rely less on the estimated time to delivery shown by the platform. Making a good initial impression matters, as previous literature finds. For example, Agnew et al. (2016)

Table 7. Heterogeneous Effects on Probability of Repurchase for Zero/Positive Delivery Charges

<table><tr><td rowspan="2">Variable</td><td colspan="3">Zero</td><td colspan="3">Positive</td></tr><tr><td>(1) Platform</td><td>(2) Same</td><td>(3) Others</td><td>(4) Platform</td><td>(5) Same</td><td>(6) Others</td></tr><tr><td>Delayed</td><td>-0.0007(0.0011)</td><td>-0.0037***(0.0014)</td><td>0.0030**(0.0013)</td><td>-0.0131***(0.0046)</td><td>-0.0165***(0.0037)</td><td>0.0033(0.0026)</td></tr><tr><td>Restaurant × Customer FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>60,141</td><td>60,141</td><td>60,141</td><td>59,788</td><td>59,788</td><td>59,788</td></tr></table>

Note. Robust standard errors in parentheses  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

Table 8. Heterogeneous Effects on Probability of Repurchase for New/Existing Customers

<table><tr><td rowspan="2">Variable</td><td colspan="3">New</td><td colspan="3">Existing</td></tr><tr><td>(1) Platform</td><td>(2) Same</td><td>(3) Others</td><td>(4) Platform</td><td>(5) Same</td><td>(6) Others</td></tr><tr><td>Delayed</td><td>-0.0100***(0.0029)</td><td>-0.0198***(0.0030)</td><td>0.0017(0.0015)</td><td>-0.0060***(0.0010)</td><td>-0.0108***(0.0030)</td><td>0.0045(0.0035)</td></tr><tr><td>Restaurant × Customer FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>16,988</td><td>16,988</td><td>16,988</td><td>122,754</td><td>122,754</td><td>122,754</td></tr></table>

Note. Robust standard errors in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

report that individuals are more likely to follow financial advice from advisers who dispense good advice first. Accordingly, we may expect that a good delivery experience may matter more for new customers. The results regarding the heterogeneous effects between new and existing users are reported in Table 8. This analysis confirms that new users are more strongly affected by delayed deliveries than existing users. This implies that the strategy to set a conservative estimated time would be more effective for relatively new customers.<sup>5</sup> Additionally, previous literature (Black and Vance 2020) also suggests that not only do first impressions matter but they may have a lasting influence. Therefore, it may even be more important to ensure a timely delivery to new customers.

## 6.5. Delayed vs. Early Orders

Based on the theory of loss aversion, one would expect the effect of discrepancy between the estimated and actual times to be stronger for transactions with delayed deliveries compared with those with early deliveries. That is, the effect of being less delayed versus more delayed should be larger than the effect of being more early versus less early. To confirm our intuition, we create two subsamples, one with delayed deliveries and the other with early deliveries. Then, we estimate the model on the two subsamples using Delay Length as the main independent variable, where a positive value of Delay Length indicates a delayed delivery.<sup>6</sup> Based on Table 9, we note that the magnitude of the impact is higher for delayed transactions than for early transactions, indicating that estimated time indeed sets a reference point for the customers against which they compare actual delivery times.

## 7. Robustness Checks

In this section, we carry out a number of additional analyses to check the robustness of our main results that delayed deliveries decrease the future probability of transacting from the platform and the same restaurant. First, we use continuous treatment measures rather than the binary Delayed variable. Second, we use an alternative method of matching/weighting to balance observations. Last, we account for potential variations in a customer’s behavior/location across weekdays and weekends.

## 7.1. Alternative Independent Variables

Previously, we looked at the impact of the binary indicator of whether the actual delivery time was greater than the estimated time. Here, we specifically look at the impact of the absolute difference between the actual and estimated times. Therefore, we estimate the same regression model in the main analysis but now with Delay Length as the main independent variable, where a positive value of Delay Length indicates a delayed delivery. The results are presented in Table 10, where one can see that, as the difference between the actual and estimated delivery times increases (either from being more to less early or from a shorter delay to a longer delay), the probability of a future purchase from the platform or the same restaurant decreases.

Table 9. Heterogeneous Effects on Probability of Repurchase for the Consumer Being Late or on Time

<table><tr><td rowspan="2">Variable</td><td colspan="3">Delayed</td><td colspan="3">Early/On Time</td></tr><tr><td>(1) Platform</td><td>(2) Same</td><td>(3) Others</td><td>(4) Platform</td><td>(5) Same</td><td>(6) Others</td></tr><tr><td>Delay Length</td><td>-0.0006**(0.0003)</td><td>-0.0009***(0.0003)</td><td>0.0003(0.0003)</td><td>-0.0002*(0.0001)</td><td>-0.0003**(0.0001)</td><td>0.0000(0.0005)</td></tr><tr><td>Restaurant × Customer FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>21,092</td><td>21,092</td><td>21,092</td><td>83,026</td><td>83,026</td><td>83,026</td></tr></table>

Note. Robust standard errors in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

Table 10. Impact of Delay Length on the Probability of Repurchase

<table><tr><td>Variable</td><td>(1) Platform</td><td>(2) Same</td><td>(3) Others</td></tr><tr><td>Delay Length</td><td>-0.0009**(0.0004)</td><td>-0.0015***(0.0003)</td><td>0.0006**(0.0003)</td></tr><tr><td>Restaurant × Customer FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>139,742</td><td>139,742</td><td>139,742</td></tr></table>

Note. Robust standard errors in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

These results imply that the longer the delay, the less likely the customer is to make a repeat purchase from the platform or the same restaurant. However, a fiveminute delay when the estimated time is 15 minutes could have a more severe impact than when the estimated time is 45 minutes. To ensure that our results are not driven by the variation in the length of the estimated delivery times, here, we estimate our main regression model using Delay/EstTime as our key independent variable to obtain a relative continuous measure of Delay Length, which is the difference between the actual and estimated delivery times scaled by the estimated delivery time. We find that our main results continue to be robust to a relative measure of delay length (see Table 11).

## 7.2. Alternative Matching Method with Coarsened Exact Matching (CEM)

In our main analysis, we used inverse propensity score weighting to mitigate any selection into treatment (i.e., delayed order). Here, we instead deploy CEM estimators to estimate the effect. Unlike the propensity score methods that use maximum-likelihood estimators to control for the differences in variables across delayed and early groups of transactions, CEM is a nonparametric matching method that allows one to ex ante bound the imbalance (both on individual variables and jointly) between the two groups by manually coarsening the variables into different-sized bins (Blackwell et al.

Table 11. Impact of Delay/EstTime on the Probability of Repurchase

<table><tr><td>Variable</td><td>(1) Platform</td><td>(2) Same</td><td>(3) Others</td></tr><tr><td>Delay Length/EstTime</td><td>-0.0261***(0.0102)</td><td>-0.0467***(0.0101)</td><td>-0.0134(0.0100)</td></tr><tr><td>Restaurant × Customer FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>139,742</td><td>139,742</td><td>139,742</td></tr></table>

Note. Robust standard errors in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

2009, Kumar et al. 2019). We then rerun the weighted regression analysis of Table 12 using the CEM weights. The results are presented in columns (1), (2), and (3) in Table 12, which are consistent with our main findings.

## 7.3. Time-Varying Popularity of Restaurants

In our main analysis, we include the restaurant fixed effects to capture the heterogeneity in fixed characteristics across different restaurants. However, it is plausible that a restaurant’s popularity could change over time, though it is unlikely because of our relatively short sample period. Nevertheless, we now include the number of orders in a particular week of a restaurant (to capture its time-varying popularity) as one of the covariates in our double machine learning model. Our main results remain robust (see Table 13).

## 7.4. Controlling for Customer-Weekend Effect

In our main analysis, we include the customerrestaurant fixed effects to take into account the unobserved heterogeneity in a customer’s preferences for different restaurants. However, it is plausible that a customer’s preference could also vary based on whether the order is made from home or the workplace. Whereas we do not have information on the location of orders, we can still account for the variation in a customer’s behavior across weekdays and week ends, which is likely to be correlated with the location of the orders. We control for this unobserved heterogeneity by including customer-weekend fixed effects (i.e., customer and weekend interaction). Table 14 presents the results. We find that the coefficient of interest is consistent with our previous estimates and statistically significant.

## 8. Exploring the Effect on Current vs. Future Orders

So far, we find that the probability of a future purchase from the platform and the same restaurant decreases when actual delivery takes longer than the estimated time. Therefore, the platform can promote the customers’ repurchase probability by displaying a more conservative estimated time. At the same time, however, a more conservative estimated time could deter some of the consumers from ordering in the first place. Therefore, there is a potential trade-off between current and future orders if the platform adopts the strategy of setting a more conservative estimated time. However, in the absence of users’ app browsing data (i.e., what users view before making an order), we cannot analyze the loss in the focal orders. In this section, we aim to quantify the relative effect of longer estimated delivery times on current and future orders, using two different approaches.

Table 12. Impact of Late Delivery on the Probability of Repurchase (CEM)

<table><tr><td rowspan="3">Variable</td><td colspan="3">Matching method</td></tr><tr><td colspan="3">CEM</td></tr><tr><td>(1) Platform</td><td>(2) Same</td><td>(3) Others</td></tr><tr><td>Delayed</td><td>-0.0029***(0.0011)</td><td>-0.0043**(0.0018)</td><td>0.0013(0.0020)</td></tr><tr><td>Customer FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Restaurant FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>341,766</td><td>341,766</td><td>341,766</td></tr></table>

Note. Robust standard errors in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

## 8.1. Based on Observational Data

In our first approach, we aggregate the customer transaction-level data we have at the restaurant-week level. Based on this aggregated data, we investigate how a longer estimated time to delivery in a specific week impacts the orders of a restaurant in the focal (current) week and also in the following (future) week. Specifically, we regress the number of orders in the focal week for restaurant i in week t on the mean estimated time to delivery while controlling for the means of restaurant rating, actual delivery time, and bill amount.<sup>7</sup> In Table 15, we find that the negative effect on orders in the current week (the loss) is smaller in magnitude than the positive effect on orders in the following week (the gain), suggesting that it could indeed be beneficial for platforms to set a higher estimated time to delivery. We see a net positive effect every week of 0.07 additional orders per restaurant by increasing the mean estimated time to delivery by one minute. This implies an increase of about 41,000 orders per year for every five-minute increase in EstTime on the platform in the city for which we have the data.<sup>8</sup>

## 8.2. Based on Online Experiment

To compare the effect of estimated time on current and future orders, we further conducted an online surveybased experiment. The experiment simulates the decisionmaking process of a user on a food delivery platform to provide evidence for the magnitude of the trade-off between current and future orders.

Table 13. Impact of Late Delivery on the Probability of Repurchase While Controlling for Weekly Number of Restaurant Transactions

<table><tr><td>Variable</td><td>(1) Platform</td><td>(2) Same</td><td>(3) Others</td></tr><tr><td>Delayed</td><td>-0.0094***(0.0029)</td><td>-0.0105**(0.0051)</td><td>0.0012**(0.0004)</td></tr><tr><td>Restaurant × Customer FE</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>139,742</td><td>139,742</td><td>139,742</td></tr></table>

Note. Robust standard errors in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

8.2.1. Experiment Design. The key idea behind our experiment design is to randomly manipulate the estimated delivery time shown to the users (participants) while keeping the actual delivery time the same across users. In the first stage, users decide whether to order from a restaurant on the food delivery platform based on the estimated time to delivery they are shown. In the second (final) stage, those who decide to make a purchase in the first stage indicate whether they are willing to make future purchases after seeing the actual delivery time. This design allows us to compare the drop in users’ propensity to order in the first stage to the increase in their propensity to order in the second stage. If the magnitude of the drop in the first stage is less than the magnitude of the increase in the second stage, it suggests that setting a conservative estimated time can be beneficial.

More details of the experiment are as follows.<sup>9</sup> In the initial part of the survey, the respondents are asked a set of questions about their demographic information, such as age, gender, education, and the frequency of using online food delivery apps. Next, in the main experiment, the respondents are first given a scenario of ordering a pizza from a restaurant on a food delivery platform based on a set of restaurant-related informa tion, such as the picture of the food and the average rating of the restaurant. Keeping everything else the same, we randomize the estimated time to delivery across users: whereas some users see an estimated time of as high as 45 minutes, others see 20, 25, 30, 35, or 40 minutes. In the first stage, they decide whether to order from the restaurant. If they do not choose to order in the first stage, the experiment ends for these users, and they directly move to a postexperiment survey. If they do choose to order in the first stage, in the second stage, we show them the actual delivery time, which is kept the same for all the users (35 minutes). We then ask them (i) how satisfied they are with the delivery experi ence, and (ii) whether they would reorder from the platform, the focal restaurant, or other restaurants on the platform in the future. Last, we ask all the respondents to complete the postexperiment survey.

Table 14. Impact of Late Delivery with Customer-Weekend Fixed Effects

<table><tr><td>Variable</td><td>(1) Platform</td><td>(2) Platform</td></tr><tr><td rowspan="2">Delayed</td><td>-0.0328*</td><td>-0.0333</td></tr><tr><td>(0.0165)</td><td>(0.0198)</td></tr><tr><td>Restaurant × Customer FE</td><td>Yes</td><td>Yes</td></tr><tr><td>Customer × Weekend FE</td><td>No</td><td>Yes</td></tr><tr><td>Observations</td><td>139,742</td><td>113,902</td></tr></table>

Note. Robust standard errors in parentheses  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

Table 15. Impact of Mean Estimated Delivery Time on the Number of Orders per Restaurant in a Week

<table><tr><td>Variable</td><td>(1)Number of orders(focal week)</td><td>(2)Number of orders(next week)</td></tr><tr><td>Avg EstTime(minutes)</td><td>-0.1056***(0.0265)</td><td>0.1757***(0.0399)</td></tr><tr><td>Week FE</td><td>Yes</td><td>Yes</td></tr><tr><td>Restaurant FE</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>21,554</td><td>20,214</td></tr></table>

Note. Robust standard errors in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

To further support our assertion that consumers consider estimated delivery times a reference point, we incorporated an additional question in the survey. If they choose to order in the first stage, they are asked whether the early/late delivery experience influenced their reorder decision in the second stage. These questions help us understand whether reference points are formed among the respondents and whether expectation disconfirmation has an impact on the decisionmaking process.

8.2.2. Results. In total, we have 245 respondents who took the survey. The demographics distribution across different groups of participants (specifically, ones seeing below and above 30 minutes EstTime) is listed in Table 16.<sup>10</sup> One can observe that the user characteristics are identical in the two groups, suggesting the randomization was successful.

We also verify the consistency in answering by the respondents. In the preexperiment survey, respondents are asked about the frequency of using food delivery apps. After the experiment, they are asked again whether they had used any food delivery app before. In total, 239 out of 245 respondents (98%) gave consistent answers to these two questions.<sup>11</sup> Out of the 245 respondents, 211 chose to order in the first stage. The results from the experiment as presented in Table 17 again suggest that the loss in orders during the first stage is smaller than the gain in orders during the second stage.

Table 16. Impact of Mean Estimated Delivery Time on the Number of Orders per Restaurant in a Week

<table><tr><td>Variable</td><td>(1) EstTime ≤ 30</td><td>(2) EstTime &gt; 30</td><td>(3) p-value</td></tr><tr><td>Age</td><td>2.86</td><td>2.84</td><td>0.72</td></tr><tr><td>Education</td><td>3.62</td><td>3.59</td><td>0.81</td></tr><tr><td>Gender</td><td>1.44</td><td>1.47</td><td>0.60</td></tr><tr><td>Location</td><td>1.41</td><td>1.44</td><td>0.81</td></tr></table>

Table 17. Online Experiment: Impact of Estimated Time of Delivery and Early Delivery

<table><tr><td>Variable</td><td>(1)Current order</td><td>(2)Platform reorder</td><td>(3)Satisfaction</td></tr><tr><td>EstTime(minutes)</td><td>-0.0231***(0.0025)</td><td>0.0442***(0.0035)</td><td>0.1433***(0.0025)</td></tr><tr><td>Observations</td><td>245</td><td>211</td><td>211</td></tr></table>

Note. Robust standard errors in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

Finally, from our experiment data, we provide two pieces of evidence for the reference formation mechanism behind our findings. First, we observe from column (3) of Table 17 that the delivery satisfaction level of the users increases with a longer estimated time to delivery. Second, among the 211 respondents who ordered in the first stage, 193 (91%) of them said late/early delivery influenced their decision to order in the future.

## 9. Conclusion

Delivery speed is an important component of the service provided by food delivery platforms. Given their delivery infrastructure, they must decide an appropriate estimate of delivery time to display to consumers. Showing an aggressive estimate of delivery time (shorter delivery time estimate) may induce customers to make an order but increases the risk of a late delivery. A late delivery would reduce customer satisfaction and hurt future demand. Clearly, whereas deciding an appropriate estimate of delivery time is critical, there seems to be a lot of discrepancy in practice in how the food delivery platforms set the delivery time estimate. A study<sup>12</sup> reports that despite being the fastest food delivery service, Uber Eats was actually late more than any other service; that is, a large number of their orders were delivered after the estimated time. This highlights that Uber Eats is more aggressive in setting its estimated delivery time compared with other platforms. Part of the reason we do not observe a consistent approach in setting estimated delivery times across platforms is the lack of a study that establishes whether a conservative estimated time actually matters in stimulating future demand and whether the magnitude of this demand can be more than the loss in current orders. Our study addresses this practical need.

We also highlight the role of setting conservative expected delivery times in a platform setting where the effect of this strategy can differ across the restaurants (suppliers) and the platform. Further, this effect can also differ across the restaurant that serves an order and the other restaurants on the platform. In this context, we find the existence of a spillover effect because of which the performance of a restaurant does not affect the demand of other restaurants. We show evidence that these findings come from customers forming a reference point based on the estimated delivery time. We also establish that the relative benefits from future demand likely exceed the loss in current demand from setting a conservative estimated time. Our findings can inform the design of algorithms used by the platforms for predicting estimated delivery times.

We also find interesting heterogeneous effects such as the fact that the strategy of setting conservative estimated time matters more for customers who have not yet formed their expectations of delivery service from the platform because of previous experiences. Such customers can be those who experienced inconsistency in delivery experiences in the past or those who are new and so have not had many experiences on the platform. Additionally, the strategy is more effective in cases when delivery is not free and consumers pay an additional charge for the delivery service.

## Endnotes

<sup>1</sup> Note that the platform does not know the actual delivery time when estimating the delivery time, so the estimated times could vary even if the actual delivery times are the same. For instance, consider two deliveries, A and B, both of which took 30 minutes to deliver. However, it is plausible that the distance for delivery A is half of the distance covered in delivery B, so the platform may estimate a shorter delivery time for A. However, because of higher unexpected traffic encountered during delivery A, the actual delivery was slower than expected.

<sup>2</sup> In Section B.1 of the online appendix, we show the robustness of our main results to alternative approaches of DML implementation, such as using LASSO or random forests as the ML model.

<sup>3</sup> The results without DML are presented in Section B.2 of the online appendix.

<sup>4</sup> Note that a “new” user is defined as a user who has never used the platform before and used it for the first time during our study period.

<sup>5</sup> Whereas we use subsample analyses here, using interaction effect with New/Existing yields a significant difference as well.

<sup>6</sup> Note that we use Delay Length instead of Delayed because there is no variation in Delayed in a subsample.

<sup>7</sup> The results remain similar if we use the median instead of the mean for aggregating.

<sup>8</sup> We use the equation 0.07 orders × 52 weeks × 2,264 restaurants × 5 minutes.

<sup>9</sup> We present our respondent recruitment process and the full questionnaire in Section C.1 of the online appendix.

<sup>10</sup> We aggregate the six groups to create two equal-sized groups to perform the tests.

<sup>11</sup> The respondent’s answer would be considered as “inconsistent” if the response is “never” to the frequency question but “yes” to the used-before question.

<sup>12</sup> See https://sports.yahoo.com/delivery-app-fastest-delivery-times-163753638.html

## References

Agnew BH, Julie R, Eckert C, Iskhakov F, Louviere J, Thorp S (2016) First impressions matter: An experimental investigation of online financial advice. Management Sci. 64(1):288–307.

Allon G, Federgruen A, Pierson M (2011) How much is a reduction of your customers’ wait worth? An empirical study of the fast-food drive-thru industry based on structural estimation methods Manufacturing Service Oper. Management 13(4):489–507.

Baillon A, Bleichrodt H, Spinu V (2020) Searching for the reference point. Management Sci. 66(1):93–112.

Black DE, Vance MD (2020) Do first impressions last? The impact of initial assessments and subsequent performance on promotion decisions. Management Sci. 67(7):4556–4576.

Blackwell M, Iacus S, King G, Porro G (2009) cem: Coarsened exact matching in Stata. Stata J. 9(4):524–546

Chernozhukov V, Chetverikov D, Demirer M, Duflo E, Hansen C, Newey W, Robins J (2018) Double/debiased machine learning for treatment and structural parameters. Econometrics J. 21(1):C1–C68.

Choudhary V, Shunko M, Netessine S (2021) Does immediate feedback make you not try as hard? A study on automotive telematics. Manufacturing Service Oper. Management 23(4):835–853.

Cui R, Shin H (2018) Sharing aggregate inventory information with customers: Strategic cross-selling and shortage reduction. Man agement Sci. 64(1):381–400.

Cui R, Li M, Li Q (2020) Value of high-quality logistics: Evidenc from a clash between SF Express and Alibaba. Management Sci. 66(9):3879–3902

Cui R, Lu Z, Sun T, Golden JM (2023) Sooner or later? Promising delivery speed in online retail. Manufacturing Service Oper. Management 26(1):233–251.

Dahm M, Wentzel D, Herzog W, Wiecek A (2018) Breathing down your neck!: The impact of queues on customers using a retail service. J. Retailing 94(2):217–230.

Deshpande V, Pendem PK (2022) Logistics performance, ratings, and its impact on customer purchasing behavior and sales in e-commerce platforms. Manufacturing Service Oper. Management 25(3):827–845.

Erev I, Roth AE (1998) Predicting how people play games: Reinforcement learning in experimental games with unique, mixed strat egy equilibria. Amer. Econom. Rev. 88(4):848–881.

Fiegenbaum A, Hart S, Schendel D (1996) Strategic reference point theory. Strategic Management J. 17(3):219–235.

Fisher ML, Gallino S, Xu JJ (2019) The value of rapid delivery in omni channel retailing. J. Marketing Res. 56(5):732–748.

Fleder D, Hosanagar K (2009) Blockbuster culture’s next rise or fall: The impact of recommender systems on sales diversity. Management Sci. 55(5):697–712.

Frisch R, Waugh FV (1933) Partial time regressions as compared with individual trends. Econometrica 1(4):387–401.

Gao F, Su X (2018) Omnichannel service operations with online and offline self-order technologies. Management Sci. 64(8): 3595–3608.

Ho TH, Zheng Y-S (2004) Setting customer expectation in service delivery: An integrated marketing-operations perspective. Management Sci. 50(4):479–488.

Ho Y-C, Wu J, Tan Y (2017) Disconfirmation effect on online rating behavior: A structural model. Inform. Systems Res. 28(3):626–642

Hosanagar K, Fleder D, Lee D, Buja A (2014) Will the global village fracture into tribes? Recommender systems and their effects on consumer fragmentation. Management Sci. 60(4):805–823.

Kahneman D (1973) Attention and Effort, vol. 1063 (Prentice Hall Englewood Cliffs, NJ).

Kumar A, Mehra A, Kumar S (2019) Why do stores drive online sales? Evidence of underlying mechanisms from a multichannel retailer Inform. Systems Res. 30(1):319–338.

Lee D, Hosanagar K (2019) How do recommender systems affect sales diversity? A cross-category investigation via randomized field experiment. Inform. Systems Res. 30(1):239–259.

Lin C-A, Shang K, Sun P (2023) Wait time–based pricing for queues with customer-chosen service times. Management Sci. 69(4): 2127–2146.

Lindsay PH, Norman DA (2013) Human Information Processing: An Introduction to Psychology (Academic Press, New York).

Lord RG, Maher KJ (2002) Leadership and Information Processing: Link ing Perceptions and Performance (Routledge, New York).

Lovell MC (1963) Seasonal adjustment of economic time series and mul tiple regression analysis. J. Amer. Statist. Assoc. 58(304):993–1010.

Navarro DJ, Newell BR, Schulze C (2016) Learning and choosing in an uncertain world: An investigation of the explore–exploit dilemma in static and dynamic environments. Cognitive Psych. 85:43–77.

Oliver RL (2014) Satisfaction: A Behavioral Perspective on the Consumer (Routledge, New York).

Peng DX, Lu G (2017) Exploring the impact of delivery performance on customer transaction volume and unit price: Evidence from an assembly manufacturing supply chain. Production Oper. Management 26(5):880–902.

Robinson PM (1988) Root-N-consistent semiparametric regression. Econometrica 56(4):931–954.

Roels G, Su X (2014) Optimal design of social comparison effects: Setting reference groups and reference points. Management Sci. 60(3):606–627.

Rosenbaum PR, Ross RN, Silber JH (2007) Minimum distance matched sampling with fine balance in an observational study of treatment for ovarian cancer. J. Amer. Statist. Assoc. 102(477):75–83.

Stanley TD, Jarrell SB (2005) Meta-regression analysis: A quantitative method of literature surveys. J. Econom. Surveys 19(3): 299–308.

Tereyag˘og˘lu N, Fader PS, Veeraraghavan S (2018) Multiattribute loss aversion and reference dependence: Evidence from the performing arts industry. Management Sci. 64(1):421–436.

Terzi A, Koedijk K, Noussair CN, Pownall R (2016) Reference point heterogeneity. Frontiers Psych. 7:1347.

Tversky A, Kahneman D (1974) Judgment under uncertainty: Heuristics and biases: Biases in judgments reveal some heuristics of thinking under uncertainty. Science 185(4157):1124–1131.

Tversky A, Kahneman D (1991) Loss aversion in riskless choice: A reference-dependent model. Quart. J. Econom. 106(4):1039–1061.

Walters DJ, Hershfield HE (2020) Consumers make different inferences and choices when product uncertainty is attributed to forgetting rather than ignorance. J. Consumer Res. 47(1): 56–78.

Yang J-C, Chuang H-C, Kuan C-M (2020) Double machine learning with gradient boosting and its application to the big n audit quality effect. J. Econometrics 216(1):268–283.

Yu Q, Allon G, Bassamboo A (2017) The reference effect of delay announcements: A field experiment. Management Sci. 67(12): 7417–7437.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
