---
otero_id: 15468
otero_key: "MZR5VZQM"
title: "Responding to Online Reviews in Competitive Markets: A Controlled Diffusion Approach"
authors: "Mingwen Yang; Zhiqiang (Eric) Zheng; Vijay Mookerjee; Hongyu Chen"
year: "2023"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/16163"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# RESPONDING TO ONLINE REVIEWS IN COMPETITIVE MARKETS: A CONTROLLED DIFFUSION APPROACH<sup>1</sup>

Mingwen Yang Michael G. Foster School of Business, University of Washington Seattle, WA U.S.A. {mingweny@uw.edu}

Zhiqiang (Eric) Zheng and Vijay Mookerjee Naveen Jindal School of Management, University of Texas at Dallas Richardson, TX, U.S.A. {ericz@utdallas.edu} {vijaym@utdallas.edu}

Hongyu Chen College of Business, California State University at Long Beach Long Beach, CA, U.S.A. {hongyu.chen@csulb.edu}

We study how firms respond to online customer reviews in a competitive market where they jostle with one another for sales based on online ratings. The focus of this paper is on how firms can optimally manage their ratings through management response and how review ratings affect the sales and profit of competing firms. We develop a controlled diffusion process to model the coevolution of sales and ratings as a function of the response strategy chosen to maximize profit over time. Our model considers a variety of factors, such as profit margin and customer rating sensitivity, that influence a firm’s effort to manage ratings and subsequently its sales and profits. More response effort needs to be exerted to manage ratings when either the profit margin of a tour is very high or customers are very sensitive to ratings. We estimate our model using data on Ctrip’s tours that include each tour’s sales, reviews, prices, and tour features. We find that consumers anchor their beliefs in the mean market rating and that their purchase decisions depend on the tour’s rating relative to this anchor. Thus, relative, rather than absolute, ratings matter. Our study informs firms on how competition and other primitives impact their efforts to manage ratings and hence profit. Our methodology allowed us to conduct “what-if” analyses, for example, to study what would happen to the review ratings, sales, and profits of a tour if a firm adopted a different response strategy. We were also able to provide turnaround strategies for struggling tours, i.e., factors that a loss-making tour should change if it wishes to make a positive profit. Ultimately, we conducted a competitive analysis that allowed us to modify certain parameters that affect the intensity of competition and hence the sales and the profits of competing tours. Finally, we demonstrate the flexibility of the model by extending it to incorporate multiple state variables that might affect the response strategy.

Keywords: Social media, competition, management response, controlled diffusion processes

## Introduction

Given the ubiquitous online opinion forums that are currently available, consumers can readily glean product or service information from the experience of other consumers. In particular, online customer reviews have been found to have a large impact on a firm’s reputation and revenue (Jabr & Zheng, 2014). For example, it has been reported that a 1% reputation improvement can lead to a 1.42% increase in revenue (Anderson, 2012). Likewise, research has shown that customers spend up to 31% more on firms with excellent reviews (Carter, 2022). Given the importance of online reputations, online user opinion has become a critical marketing-mix variable in e-commerce. In a competitive market, consumers’ purchasing decisions may depend not only on the reviews of the focal firm but also on the reviews of competitors. Firms often track key social media performance indicators (KPIs) about themselves, as well as their competitors (Glassman, 2011). Referred to as competitive intelligence in Zheng et al. (2012), prior literature has examined the impact of online reviews of competing firms on a focal firm’s sales (Jabr & Zheng, 2014; Kwark et al., 2021). Online consumer reviews are analogous to consumer perceptions about firms in advertising. However, unlike traditional advertising, a key difference is that online customer reviews (and the firm’s responses to these reviews) are observable to all consumers and competing firms in the market. Thus, consumers are able to develop informed beliefs about review ratings in a competitive market. These beliefs can become an anchor when customers make their purchase decisions. Firms therefore need to account for this behavior toward the effective management of ratings and sales.

The discussion above indicates that in an online marketplace, firms face the operational challenge of how to effectively manage user opinions in the presence of competition (Kent, 2014). A common practice for managing user opinions is to publicly respond to customer reviews to address the issues that reviewers have expressed. The popular press and industry reports provide evidence that responses help ratings. According to a TripAdvisor survey, 84% of customers believe that appropriate management responses to negative reviews improve their impressions of hotels (TripAdvisor, 2012). Evidence shows that hotels with the highest responsiveness to social media outperform competitors in terms of reputation (Medallia, 2015). The literature has also demonstrated the efficacy of management response in boosting a firm’s reputation (Gu & Ye, 2014; Proserpio & Zervas, 2017; Wang & Chaudhry, 2018).

However, generating a management response is not free. Training people to investigate and professionally respond to reviews can be costly. Since response efforts are costly, firms need to determine the right level of effort (the optimal response strategy) to manage review ratings to boost their sales. In a study of the hotel industry, Anderson and Han (2016) found that sales initially increase as the level of management responses increases, but the return diminishes when the rate of response reaches a high level. Past research in this area has predominately focused on the consequences of response—namely, whether management response has an impact, e.g., on a firm’s online reputation (measured by review ratings) or financial performance (hotel quarterly revenues or restaurants check-in on Yelp) (Gu & Ye, 2014; Kumar et al., 2018; Lee et al., 2016). However, the extant studies have rarely examined the antecedents, i.e., factors underlying a firm’s best response strategy, or how the firm should act differently in the presence of competition. This study attempts to fill these gaps. Specifically, we address two main questions. First, how do the ratings of other firms affect the sales of the focal firm in a competitive market? Second, how should a firm manage its ratings via management response in a competitive market?

The first question essentially asks whether consumers care about firm ratings in an absolute sense or whether they make purchase decisions depending on how the ratings of a particular firm compare with those of other firms in the market. The answer to the second question, of course, depends on how we answer the first question. If ratings are interpreted by consumers in an absolute sense, then ratings competition would hardly be an interesting question to study. However, if ratings are relative, then the actions taken to improve ratings by one firm would impact other firms.

We assume that firms are rational and represent this optimizing behavior in a stochastic control problem that maximizes total profit over time. The stochastic variables (states) of interest are the sales and online reputation of a product or service. The online reputation at time ?? is operationalized as the average of a certain number of recent review ratings (e.g., the 10 recent ratings by time ??). A firm’s response is regarded as a control exerted to improve the online reputation. The ratings deteriorate at a rate that depends on a decay factor. Consumers can be considered to be more demanding of service as the decay factor increases. Thus, the overall evolution of ratings is modeled as a controlled diffusion process, influenced by the firm’s control effort (management response strategy) and the decay factor. A firm’s sales are impacted by its ratings, the perception of consumers about the mean market rating, price, and product features. To summarize, for each firm, we consider the stochastic differential equation (SDE), which describes the coevolution of its sales and review ratings.

We estimate our model on ratings and sales using data on tours from Ctrip.com, which is the largest online travel agent in China. For each tour, the data contain information on sales, online customer reviews, prices, and other tour features. We empirically validate the notion of an equilibrium mean market rating. That is, the belief about the mean market rating held by consumers (estimated using our controlled diffusion model) is found to closely match the mean market rating realized in the market (estimated directly from the market rating time-series).

We find that when customers are more sensitive to ratings or when the profit margin is higher, tours need to respond more actively to customer reviews. However, the increase in response effort occurs at a diminishing rate. As consumers become more demanding of service (implying that ratings decay faster), the firm can increase or decrease its response effort in the steady state of ratings. Regardless of how firms respond, a higher decay rate always hurts the firm’s profit in the steady state. Higher-priced tours often attract customers who are more sensitive to ratings. Such tours are also more vulnerable to faster rating decay. A tour’s steady state rating, relative to the mean market rating, affects how the firm’s profit (value function) changes with customer rating sensitivity. Our prescriptive methodology enabled us to answer “what-if” questions, such as what would happen to ratings (and, hence, sales and profit) if a firm were to change its response strategy? Additionally, because our approach is structural in nature, it empowered us to identify parameter conditions (e.g., the profit margin) that would turn a loss-making firm into a profit-making firm. Ultimately, we conducted a competitive analysis that allowed us to change certain parameters that affect the intensity of competition and, hence, the sales and the profits of competing tours. We also demonstrate the flexibility of the model by extending it to incorporate multiple state variables that might affect the response strategy.

## Literature Review

In this section, we discuss the related literature and how our paper builds upon and extends prior related research.

## Nature of Ratings Competition

Prior studies have shown that competitive forces affect a firm’s decision pertaining to its management of online reviews (Mayzlin, 2006; Wu & Qiu, 2016). It has been found that consumers make their purchase decisions based not only on the review ratings of the focal product but also on those of its competitors. There is a significant impact of a competitor’s ratings on the focal product’s sales (Jabr & Zheng, 2014; Kwark et al., 2021). For example, Jabr and Zheng (2014) found that the sales of a focal product drop with improvements in the review ratings of a competing product. Kwark et al. (2021) determined that the mean rating of online reviews of substitute products exerts a negative impact on the purchasing of the focal product, using a retailer’s click stream data. In practice, firms have realized the importance of review competition; many of them even resort to review manipulation as a marketing tactic in reaction to competition (Wu & Qiu, 2016). However, such behavior is less common or effective for high-end sellers (Mayzlin et al., 2014). Mayzlin (2016) found that online reviews are persuasive despite promotional chat (e.g., review manipulation) activities by competitors. Yang et al. (2021) present a generic analytical model that considers online reputation (rating) competition in a market (platform) consisting of multiple firms. The authors found that in equilibrium, a more heterogeneous market leads to a lower mean market rating and higher total profit of these competing firms (Yang et al., 2021). Their results are particularly informative for platforms regarding how to target certain firms to join; for example, growing the middle of the market (firms with average ratings) is the best option (Yang et al., 2021). Different from these prior studies, this study represents the first empirical attempt to investigate how competition impacts a firm’s response effort in managing user opinions toward profit optimization.

Rating competition bears a similarity to advertising competition. There is a considerable body of work in the advertising literature that uses methods such as stochastic optimal control and differential games (Bass et al., 2007; Naik et al., 2008; Rubel et al., 2011). While advertising competition is a useful reference area for ratings competition, there is a fundamental difference between advertising and management response. Management response is often initiated in reaction to an online review posted by a customer. That is, management response is a “pull” rather than a “push” strategy.

## Management Response

Our paper contributes to a growing body of literature related to managing online reviews through management response, especially in competitive situations. Table 1 summarizes and contrasts the relevant studies within the extant management response (MR) literature.

Among these studies, some focus on empirically investigating the causal relation between MR and future review ratings (Gu & Ye, 2014; Ma et al., 2015; Proserpio & Zervas, 2017; Wang & Chaudhry, 2018). Gu and Ye (2014) examined how MR impacts repeated reviewers and found that hotels’ responses to negative reviews increase subsequent ratings by the same reviewer. In a more generalized setting going beyond repeat reviewers, Proserpio and Zervas (2017) reported an average increase of 0.12 in ratings after responding and argue that MR increases the cost of leaving a negative review, as consumers feel that their reviews will be closely scrutinized. Therefore, consumers become less likely to submit low-quality and unsubstantiated negative reviews, leading to more positive subsequent ratings (Proserpio & Zervas, 2017). The study of Yang et al. (2019) also lends support to the positive impact of MR on subsequent ratings. Wang and Chaudhry (2018) differentiated the impact of MR on negative and positive reviews separately. MR to negative reviews is generally found to boost subsequent reviews, since MR to negative reviews is typically construed as value-adding (Wang & Chaudhry, 2018). However, MR to positive reviews may have an adverse impact, as explained by reactance theory (Wang & Chaudhry, 2018). Building on this literature, it stands to reason that the boosting effect of MR decreases with higher review ratings.

<table><tr><td colspan="6">Table 1. Management Response Literature</td></tr><tr><td>Authors</td><td>Sales</td><td>Competition</td><td>Methodology</td><td>Data sample</td><td>Research questions</td></tr><tr><td>Ye et al. (2008)</td><td>Yes</td><td>No</td><td>Difference in differences (DID)</td><td>791 hotel reviews from Ctrip.com and Elong.com</td><td>Assess the influence of MR on product sales.</td></tr><tr><td>Gu and Ye (2014)</td><td>No</td><td>No</td><td>Panel Analysis</td><td>5,831 hotel reviews from Ctrip.com</td><td>Measure the impact of MR on customer satisfaction.</td></tr><tr><td>Ma et al. (2015)</td><td>No</td><td>No</td><td>Dynamic Choice Model</td><td>714 customer tweets from Twitter</td><td>Investigate the evolution of customers&#x27; voicing decisions and firms&#x27; service interventions.</td></tr><tr><td>Lee et al. (2016)</td><td>Yes</td><td>No</td><td>Panel Analysis</td><td>730 hotel reviews from TripAdvisor and quarterly hotel revenues from local revenue comptroller offices</td><td>Investigate the performance implications of MR to online WOM.</td></tr><tr><td>Proserpio &amp; Zervas (2017)</td><td>No</td><td>No</td><td>DID</td><td>3,264 hotel reviews from TripAdvisor and Expedia</td><td>Investigate the relationship between a firm&#x27;s use of MR and its online reputation.</td></tr><tr><td>Wang &amp; Chaudhry (2018)</td><td>No</td><td>No</td><td>DID</td><td>65,099 reviews from hotels on TripAdvisor, Hotel.com, Expedia, and Orbitz</td><td>Examine the effect of publicly responding to hotel guests&#x27; reviews on subsequent reviewer ratings.</td></tr><tr><td>Kumar et al. (2018)</td><td>No</td><td>Yes</td><td>DID</td><td>730 restaurant reviews and Check-ins from Yelp</td><td>Examine the impact of MR on business performance and their spillover effect on nearby businesses.</td></tr><tr><td>Chen et al. (2019)</td><td>No</td><td>No</td><td>DID</td><td>943 hotel reviews from Ctrip.com and Elong.com</td><td>Examine the impact of MR on the volume and valence of subsequent customer reviews.</td></tr><tr><td>Yang et al. (2019)</td><td>No</td><td>No</td><td>SDE</td><td>117 tour reviews from Ctrip.com and 136 hotel reviews from Expedia</td><td>Devise response strategy for a firm to respond to online customer reviews.</td></tr><tr><td>Sun et al. (2021)</td><td>No</td><td>No</td><td>Panel Analysis</td><td>40 international airline tweets from Twitter</td><td>Examine the dynamics between social media customer complaints and brand service interventions.</td></tr><tr><td>Golmohammadi et al. (2021)</td><td>No</td><td>No</td><td>Panel Analysis and DID</td><td>375 S&amp;P 500 firm tweets from Twitter</td><td>Explore the phenomenon of complaint publicization.</td></tr><tr><td>This study</td><td>Yes</td><td>Yes</td><td>Controlled diffusion processes</td><td>Reviews and sales of 317 tours from Ctrip.com</td><td>Prescriptive model on the impact of competition on firm&#x27;s effort to manage user opinions and further sales.</td></tr></table>

However, the literature has also documented some possible adverse effects of MR on ratings. Ma et al. (2015) found that responding to complaints on a firm’s official Twitter page spurs even more complaints (referred to as redress seeking). Nevertheless, the authors still advocate the use of MR because responding helps improve the customer relationship, which leads to more positive customer voices in the future (Ma et al., 2015). The authors argue that MR’s indirect effect on customer voice through an improved relationship is stronger than the direct adverse effect, thereby leading to a positive overall effect (Ma et al., 2015). Similarly, Sun et al. (2021) showed that poor service intervention (i.e., poor MR) may trigger more complaints, while high-quality service intervention reduces future complaints.

We note that both the above papers are in the context of a firm’s Twitter page, where firms tweet to interact with their customers. Twitter pages are also venues for customers to express their opinions and make complaints, to which firms can respond. Specifically, on Twitter, whenever a firm responds to a user’s tweet (or to an existing complaint-response thread), the thread appears at the top of the firm’s page (Golmohammadi et al., 2021). Therefore, responding to complaints may reinforce customer awareness of the complaint and hurt the firm. Golmohammadi et al. (2021) refer to this phenomenon as “complaint publicization” because the act of response inadvertently increases a complaint’s potential exposure and, thus, the volume of future complaints.

While the above studies provide a case of the negative impact of firm response, the context of our paper is different, as are the findings. First, on Ctrip.com (the source of our data), each product has its own review page, where customer reviews are displayed in chronological order according to the review timestamp. Whenever the firm responds to a review does not change the order (exposure) of the review. Therefore, the phenomenon of complaint publicization is unlikely to exist in our context. In addition, while anyone can post complaints on Twitter, only verified customers who have purchased the product are allowed to post reviews (complaints) on Ctrip.com. Therefore, complaints on Ctrip.com are more credible and actionable.

Perhaps due to the unavailability of sales data, very few papers have attempted to study the influence of MR on revenues (Kumar et al., 2018; Lee et al., 2016; Ye et al., 2008). Ye et al. (2008) studied the causal link between MR and sales and found that a hotel that provides managerial responses receives 60% more online bookings than an equivalent hotel without managerial response. The authors used review volumes to approximate hotel sales, assuming that the number of reviews accurately reflects the total sales (Ye et al., 2008). Lee et al. (2016) examined the effect of MR on firms’ financial performance using a data set consisting of online reviews, managerial responses and the quarterly financial performance of 730 hotels from 2005 to 2011. Their empirical results suggest that the decision of whether to respond depends on the different levels of review metrics, such as review volume and valence (Lee et al., 2016). Ratings can also be influenced by peer response; furthermore, as expected, an improvement in ratings can be beneficial for sales (Goh et al., 2013). Kumar et al. (2018) found that MR significantly affects the performance of a focal firm’s business and its nearby competitors’ businesses, where the authors use the number of mobile check-ins on Yelp.com to approximate the restaurants performance. While the literature has mostly focused on the consequence of MR, our work systematically studies both antecedents and consequences of management strategy. That is, we prescriptively model what underlying factors impact a firm’s response strategy toward the optimal management of user opinions in a competitive environment.

## Model Description

In this study, we build an integrative model that considers both the antecedents and consequences of a firm’s decision with regard to its response strategy, assuming that the firm is rational and maximizing its profit. The firm’s response strategy can be considered a control (effort exerted over time) to improve its online reputation. A firm’s sales depend on its own online reputation and that of its competitors. We next present a conceptual model as a prelude to the mathematical model.

## Conceptual Model and Mechanism

The conceptual model is depicted in Figure 1, where a focal firm’s sales depend on not only its own rating but also the ratings of other firms in the market. We assume that customers believe that the market rating has a steady-state mean (??). Our study is consistent with the notion of an oblivious equilibrium (rather than a Nash equilibrium), where each player shares a common belief in the outcome of the equilibrium (Benkard et al., 2015). Based on this structure, each focal firm’s sales are driven by the rating of the focal firm, relative to the belief concerning the mean market rating. The constant mean market rating reflects the behavior of consumers who are more likely to have a general sense of the market rating rather than the exact market rating at any point in time.<sup>2</sup>

At a high level, the chain of influence we consider is as follows: effort applied to boost ratings (management response strategy) → ratings → sales → profit. We first explain the underlying mechanism of how management response can impact ratings. When a negative review arrives and it receives a response, possible future negative reviews on the same issue are reduced or suppressed because repeating the same complaint does not embody much information value (Yang et al., 2019). If customers were to write negative reviews, they would feel obliged to express their complaints differently, which is referred to as the “beg to differ” effect (Ho et al., 2017; Moe & Schweidel, 2012). Therefore, responding to negative reviews helps improve future ratings. In addition, responses increase the “cost” of leaving a negative review, especially a flaky or unfounded one, because consumers feel that their reviews will be closely scrutinized (Proserpio & Zervas, 2017). As a result, the urge to express negative opinions is suppressed. The mechanism of the second path (direction) of rating → sales has been well established in the extensive literature (Duan et al., 2008; Kwark et al., 2021; Zhu & Zhang, 2010).

market ratings to the public. However, potential customers can easily infer the mean market rating, as customer reviews are public and most platforms enable potential customers to filter out competitors conveniently. For example, after constraining the departure city, a consumer at Ctrip.com can find the ratings of all relevant tours and easily infer the mean market rating.

![](/api/attachments/MZR5VZQM/fulltext/images/037df9fe7ae06d109ada54a0974b3d572f535e4e27acfa06c4992f2ea0ae3db3.jpg)  
Figure 1. Conceptual Model

In Figure 1, the impact of management response on sales occurs through ratings; that is, the impact of response on sales is mediated by ratings. This reflects a world where, while making purchase decisions, customers pay close attention to review ratings but are less likely to look at previous responses by the firm to make such decisions. However, whether management response directly impacts sales is an empirical question and could be context specific. The mediation test, the Sobel test (Sobel, 1982), can be used to evaluate the possible existence of the direct path: response → sales. In our study, using the data, the result of the Sobel test adopting the approach proposed by Baron and Kenny (1986) indicates that the impact of the management response on sales is fully mediated away by ratings.<sup>3</sup> This finding lends parsimony and tractability to our framework. Due to these considerations, as shown in Figure 1, we did not consider a direct path from the response strategy to sales.

As a side note, we acknowledge that management response may not be the only strategy deployed by firms to improve their profits. Firms may simultaneously adopt a variety of strategies—for example, price, quality, and loyalty program. By focusing on management response, we do not exclude the importance of these other strategies. However, we believe that studying management response is significant in its own right, given the increasing importance of user opinions in the digital economy. Furthermore, to a large extent, management response often reflects other strategies. For example, upon receiving a complaint, firms likely need to take corrective actions first (e.g., improve the quality) and then deliver a message (in the form of MR) to inform the complaining reviewer and potential customers on how the complaint was addressed.<sup>4</sup>

## Mathematical Preliminaries

We consider two time-series or stochastic processes: (1) a focal firm ??’s sales ?? (??) and (2) the focal firm ??’s ratings $x _ { i } ( t ) . ^ { 5 }$ Since the variables of interest are continuous and stochastic over time, we apply SDE to model them.

The change in focal firm ??’s sales over a small time interval from ?? to ?? + ???? is denoted by ???? (??). This change consists of a deterministic (drift) term and a stochastic (diffusion) term. The first term of the deterministic component is proportional to the difference between the focal firm’s rating (?? (??)) and customers’ belief in mean market ratings (??). While customers are likely to be aware that there is some volatility in the market rating, we assume that they anchor on the mean value when making their purchase decisions. As the difference between the focal firm’s rating and the belief in mean market ratings increases, the magnitude of the impact on sales increment becomes larger. The parameter $\beta _ { i }$ represents the impact of ratings on sales, interpreted as customer rating sensitivity. To account for unobserved heterogeneity in sales, our model also incorporates several relevant covariates, including the price at time ?? $( p _ { i } ( t ) )$ ), the quality at time ?? $( q _ { i } ( t ) )$ , and various product/service characteristics $( \psi _ { i } )$ which will be elaborated in the next section.

The stochastic term is $\sigma _ { i } \sqrt { S _ { i } ( t ) } d Z _ { i } ( t )$ , where $d Z _ { i } ( t )$ is the increment of a Wiener process following a normal distribution with mean zero and variance $d t$ . When sales are low, incremental sales have a lower variance. To ensure that the stochastic term continues to have a material impact even when $S _ { i } ( t )$ approaches zero, we adopt the common technique by using a square root term in the stochastic term because the square root term diminishes more slowly than a linear structure (Cox et al., 1985). We use parameter $\sigma _ { i }$ to measure the magnitude of volatility in sales. To summarize, we propose the change of the focal firm’s sales, $d S _ { i } ( t )$ , as the following SDE:

$$
\begin{array}{c} d S _ {i} (t) = (\beta_ {i} (x _ {i} (t) - \mu) + \theta_ {i} p _ {i} (t) + \tau_ {i} q _ {i} (t) + \boldsymbol {\gamma} _ {i} \boldsymbol {\psi} _ {i}) d t \\ + \sigma_ {i} \sqrt {S _ {i} (t)} d Z _ {i} (t) \end{array}\tag{1}
$$

Next, we describe how a focal firm’s review ratings evolve over time in reaction to its response strategy $u _ { i } .$ . Following the same SDE framework with the change of sales, the change of the focal firm ??’s rating, $d x _ { i } ( t )$ , in a small time interval from ?? to $t + d t$ is modeled as:

$$
\begin{array}{c} d x _ {i} (t) = \left(u _ {i} \sqrt {b - x _ {i} (t)} - k _ {i} (x _ {i} (t) - a)\right) d t \\ + \zeta_ {i} \sqrt {\bigl (b - x _ {i} (t) \bigr) (x _ {i} (t) - a)} d W _ {i} (t) \end{array}\tag{2}
$$

where $u _ { i }$ denotes the control effort or the management response strategy of firm ??. Note that the control $u _ { i }$ is not necessarily constant and could depend on the state variable and time. However, we suppress these arguments for brevity of notation. The square root term in the drift component reflects the diminishing marginal effect of the control effort on ratings. That is, the marginal effect decreases as the current rating approaches its upper bound ?? $( \mathrm { e . g . , 5 } )$ . The rationale is that when the current online rating is already high, it becomes more difficult for firms to boost their ratings. The diminishing effect of control effort translates into a square root term under the SDE specification. Such a square root relationship in modeling brand awareness is widely adopted in the marketing literature (Naik et al., 2008; Rubel et al., 2011). Furthermore, in SDE, the square root term yields a mean-reverting process for the ratings after plugging the optimal control $\boldsymbol { u } _ { i } ^ { * }$ back into the rating equation. When $x _ { i } ( t )$ is above a steady-state mean, it has the tendency to decrease at a later time and vice versa, similar to the “beg to differ” effect (Moe & Schweidel, 2012).

The decay parameter $k _ { i }$ captures a common observation that consumer ratings tend to decline over time in the absence of user opinion management (Li & Hitt, 2008; Moe & Schweidel, 2012). We allow the ratings to decay at a rate that is proportional to the current rating minus the lower bound; that is, $( x _ { i } ( t ) - a )$ , where ?? is the lower bound of the ratings.<sup>6</sup> This is done to stop any further decay when the ratings reach the lower bound. The decay is faster when the current rating is high. The intuition is that online reputation changes over time when “new” information arrives. This change is a function of the current rating: when the rating is high, a negative review will have a greater impact. On the other hand, if customers already have a low reputation for a product, another negative review will not diminish the product’s reputation as much.

The stochastic term is $\zeta _ { i } \sqrt { \big ( b - x _ { i } ( t ) \big ) ( x _ { i } ( t ) - a ) } d W _ { i } ( t ) ,$ where $d W _ { i } ( t )$ is the increment of a Wiener process, and $\zeta _ { i }$ is the magnitude of the stochastic component. The reason for using the square root term in the stochastic component is similar to the one for the square root term in Equation $( 1 ) . ^ { 7 }$ We require the state variable $x _ { i } ( t )$ to be bounded between ?? and ?? (e.g., the review rating must be between 1 and 5 on Ctrip.com).<sup>8</sup> The term $\left( b - x _ { i } ( t ) \right)$ ensures that the state variable does not exceed the upper bound ??. This is because when $x _ { i } ( t )$ is equal to ??, the diffusion term vanishes, and the drift term reduces ${ \mathrm { t o ~ } } - k _ { i } ( b - a )$ , which is negative. After combining the diffusion and drift term, the value of $d x _ { i } ( t )$ turns negative, which must take the value of $x _ { i } ( t )$ to a value lower than ?? at time $t + d t$

Note that the rating equation is an Ito process where the state variable is continuous. Thus, before $x _ { i } ( t )$ exceeds ??, it must touch this value. Thus, ?? is an upper bound for $x _ { i } ( t )$ Similarly, when the state value reaches ?? (the lower bound), the diffusion term becomes zero, and the drift term reduces to $u _ { i } { \sqrt { b - a } }$ , a non-negative value. After combining the diffusion and drift terms, the value of $d x _ { i } ( t )$ turns positive (assuming $u _ { i } > 0 )$ , which will take the value of $x _ { i } ( t )$ to a value higher than ?? at time $t + d t$ . Therefore, ?? is the lower bound of the state variable.

## Stochastic Optimal Control Problem

Equations (1) and (2) model how the focal firm’s response strategy $u _ { i }$ influences its sales over time in a competitive market. The following natural question arises: What is the optimal control effort (response strategy) the firm should adopt? We assume that the firm maximizes its profit over time. The response cost (e.g., personnel cost) is assumed to be convex and increasing in regard to the control effort; i.e., as the control effort increases, the marginal cost of being more responsive increases. The firm determines its optimal level of control effort to maximize its total profit over time. We formulate a stochastic optimal control problem as follows:

$$
\underset {u _ {i}} {\mathrm{Max}} \mathbb {E} \left[ \int_ {0} ^ {\infty} e ^ {- \rho t} (\eta_ {i} S _ {i} (t) - u _ {i} ^ {2}) d t \right]
$$

subject to

$$
\begin{array}{r l} & d S _ {i} (t) \\ & = (\beta_ {i} (x _ {i} (t) - \mu) + \theta_ {i} p _ {i} (t) + \tau_ {i} q _ {i} (t) \\ & + \pmb {\gamma} _ {i} \pmb {\psi} _ {i}) d t + \sigma_ {i} \sqrt {S _ {i} (t)} d Z _ {i} (t) \end{array}
$$

$$
\begin{array}{r} d x _ {i} (t) = \Bigl (u _ {i} \sqrt {b - x _ {i} (t)} - k _ {i} (x _ {i} (t) - a) \Bigr) d t \\ + \zeta_ {i} \sqrt {(x _ {i} (t) - a) (b - x _ {i} (t))} d W _ {i} (t), \end{array}\tag{3}
$$

where $\eta _ { i }$ indicates firm ??’s profit margin (more specifically, the normalized marginal benefit relative to the control cost), and $\rho$ represents the discount factor. Objectively, the term $( \eta _ { i } S _ { i } ( t ) - u _ { i } ^ { 2 } )$ represents the focal firm’s profit at time ??, and $e ^ { - \rho t }$ is the continuous discount effect at time ??. The total profit is calculated by integrating the profit rate. Since sales $S _ { i } ( t )$ evolve stochastically over time, we take the expectation of the total profit. We summarize the parameters and variables of interest in Table 2.

## Optimal Solution to the Problem

We solve the stochastic optimal control problem in Equation (3) (see the derivation in Appendix A) to obtain the optimal response strategy as follows:

$$
u _ {i} ^ {*} = \alpha_ {i} \sqrt {b - x _ {i} (t)},\tag{4}
$$

where $\begin{array} { r } { \alpha _ { i } = \sqrt { ( \rho + k _ { i } ) ^ { 2 } + \frac { \eta _ { i } \beta _ { i } } { \rho } } - ( \rho + k _ { i } ) } \end{array}$ . Equation (4) elucidates the antecedents of response. The optimal response strategy depends on focal firm $i \ ' \mathbf { s }$ rating $x _ { i } ( t )$ ; the focal firm exerts more effort when its current rating is low.

By plugging the optimal control $\boldsymbol { u } _ { i } ^ { * }$ back into the state equations in Equation (3) and reorganizing, we obtain the trajectory of a two-dimensional stochastic process that embeds the optimal response strategy in the spirit of a structural model. The optimal response strategy is expressed in the ratings and sales processes in terms of the state variables and the primitives of the problem (including the profit margin $\eta _ { i }$ in the objective function):

$$
\begin{array}{r} d S _ {i} (t) = (\beta_ {i} (x _ {i} (t) - \mu) + \theta_ {i} p _ {i} (t) + \tau_ {i} q _ {i} (t) + \pmb {\gamma} _ {i} \pmb {\psi} _ {i}) d t \\ + \sigma_ {i} \sqrt {S _ {i} (t)} d Z _ {i} (t) \end{array}\tag{5a}
$$

$$
\begin{array}{r} d x _ {i} (t) = \lambda_ {i} \big (\nu_ {i} - x _ {i} (t) \big) d t \\ + \zeta_ {i} \sqrt {\big (b - x _ {i} (t) \big) (x _ {i} (t) - a)} d W _ {i} (t), \end{array}\tag{5b}
$$

$$
\begin{array}{r l} & {\mathrm{where} \quad \nu_ {i} = \frac {(A _ {i} - \rho) b - k _ {i} (b - a)}{(A _ {i} - \rho)}, \quad \lambda_ {i} = A _ {i} - \rho , \quad \mathrm{and} \quad A _ {i} =} \\ & {\sqrt {(\rho + k _ {i}) ^ {2} + \frac {\eta_ {i} \beta_ {i}}{\rho}}.} \end{array}
$$

<table><tr><td colspan="2">Table 2. Definition of Key Variables and Parameters</td></tr><tr><td>Notation</td><td>Definition</td></tr><tr><td> $S_i(t)$ </td><td>Sales of product (tour) i at time t</td></tr><tr><td> $x_i(t)$ </td><td>Review ratings of product i at time t</td></tr><tr><td> $p_i(t)$ </td><td>Price of product i at time t, a function of time</td></tr><tr><td> $q_i(t)$ </td><td>Quality of product i at time t</td></tr><tr><td> $\psi_i$ </td><td>Vector of product i&#x27;s characteristics</td></tr><tr><td> $\eta_i$ </td><td>Profit margin of product i</td></tr><tr><td> $\beta_i$ </td><td>Customer rating sensitivity of product i</td></tr><tr><td> $\sigma_i$ </td><td>Magnitude of volatility in sales of product i</td></tr><tr><td> $k_i$ </td><td>Rating decay factor of product i</td></tr><tr><td> $\zeta_i$ </td><td>Magnitude of volatility in ratings of product i</td></tr><tr><td> $v_i$ </td><td>Steady-state mean rating of product i</td></tr><tr><td> $\mu$ </td><td>Customers&#x27; belief in mean market ratings</td></tr><tr><td> $\rho$ </td><td>Discount factor</td></tr></table>

From Equation (5b), the optimal evolution of ratings reduces to a mean-reverting process. When $x _ { i } ( t )$ is above the steadystate mean $\nu _ { i } ,$ , it has the tendency to decrease, and vice versa. That is, $x _ { i } ( t )$ fluctuates around the steady-state mean $\nu _ { i } .$ The parameter $\lambda _ { i }$ measures the speed of reversion in the ratings. The steady-state mean of ratings $( \nu _ { i } )$ decreases with a larger rating decay factor $( k _ { i } )$ , lower profit margin $( \eta _ { i } )$ , or lower customer rating sensitivity $( \beta _ { i } )$ (see the proofs in Appendix B).

In the steady state (that is, $x _ { i } ( t ) = \nu _ { i } )$ , the focal firm exerts more effort when it has a higher profit margin $( \eta _ { i } )$ or when customers are more sensitive to ratings $( \beta _ { i } )$ . In contrast, the focal firm could exert less or more effort when its rating decays faster (higher $k _ { i } )$ (see the proofs in Appendix B).

The focal firm ??’s value function $V ( S _ { i } , x _ { i } )$ , which is the total discounted profit earned beyond ??, starting with initial values $S _ { i } ( t ) = S _ { i }$ and $x _ { i } ( t ) = x _ { i }$ under the optimal response strategy, is as follows:

$$
\begin{array}{r l} & V (S _ {i}, x _ {i}) = \frac {\eta_ {i}}{\rho} S _ {i} + 2 (A _ {i} - \rho - k _ {i}) x _ {i} - \frac {\eta_ {i} \beta_ {i} \mu}{\rho^ {2}} \\ & + 2 k _ {i} a (A _ {i} - \rho - k _ {i}) + \frac {\eta_ {i} (\theta_ {i} p _ {i} + \tau_ {i} q _ {i} + \pmb {\gamma} _ {i} \pmb {\psi} _ {i})}{\rho^ {2}} \\ & \quad + \frac {b}{\rho} \Bigl (\frac {\eta_ {i} \beta_ {i}}{\rho} - 2 (\rho + k _ {i}) A _ {i} + 2 (\rho + k _ {i}) ^ {2} \Bigr) \end{array}\tag{6}
$$

From the closed-form value function, we are able to analytically derive the marginal impact of key variables (e.g., profit margin, customer rating sensitivity, and rating decay) on the focal firm’s profit (see the derivations in Appendix B). After estimating the tour-specific parameters using real data, we are also able to analyze various economic effects for each tour, adopting a different response strategy, and a competitive analysis of the market.

## Data

The data are from Ctrip.com, which is the largest online travel aggregator in China and accounts for more than half of the market share in the online travel market in China. Ctrip.com offers tour packages (tours), which provide tourism services, including itinerary planning, hotel accommodations, transportation, and guided tour services. These tours can be provided by different travel agents (firms). Ctrip itself is the largest agent on Ctrip.com. Customers can post their reviews on Ctrip.com after consuming these tours. The review rating scales from 1 to 5. Ctrip.com allows firms (tour managers) to write management responses to their online customer reviews. However, a tour manager can only respond to customer reviews of its own tours. The management responses shown together with customer reviews are public to everyone. Figure 2 provides a translated screenshot of a sample customer review page from Ctrip tour with responses to reviews.

Our data consist of all tours on Ctrip.com that departed from Shanghai from September 2013 to June 2014. During this 10- month period, there were a total of 1,400 tours that departed from Shanghai through Ctrip.com. Because our analysis critically depends on the volume of sales and reviews, tours with too few reviews would not be meaningful.<sup>9</sup> After limiting the number of reviews to be greater than 20, we were left with 317 tours that had an adequate amount of data. For each tour, we had its daily sales (?? (??)), price $( p _ { i } ( t ) )$ , and customer reviews (including review date, review rating, and review text). For reviews that received a response, we knew the timestamp of the response and the response text.

![](/api/attachments/MZR5VZQM/fulltext/images/669824c03763b99bb91e7f027af76db6ce6d0df1b99df6bd456b98d8a31abe99.jpg)  
Figure 2. Translated Screenshot of the Management Response to Customer Reviews on Ctrip.com

In addition, we had each tour’s characteristics, including the destination $( D e s t i n a t i o n _ { i } ,$ with the value of 1 representing domestic cities in China and 0 representing cities overseas), the number of travel days $( D u r a t i o n _ { i } ,$ , with the unit of day), tour types $( T y p e _ { i } ,$ , with the value of 1 representing a guided tour and 0 otherwise), and mode of transportation (???????????????????????????? , with the value of 1 representing air and 0 otherwise). In addition, tours could be owned or provided by different firms $( A g e n t _ { i } ,$ , with the value of 1 representing Ctrip and 0 otherwise).

We extracted the tour quality from review texts using entity sentiment analysis. We used Baidu’s state-of-the-art machine learning tool for natural language processing (NLP) tasks. The API enabled us to extract all the entities mentioned in a review text along with the sentiment score for each entity. For example, the top 10 most frequent entities are service, hotel, scenery, price, environment, ticket, itinerary, room, location, and tour guide. Hence, we were able to extract each entity mentioned in a review text and the sentiment associated with it. We then averaged the entity sentiments in the last ten reviews and used this to measure the latent quality at time ?? (denoted by $q _ { i } ( t ) )$ ). Table 3 reports the summary statistics of sales, prices, quality, and tour characteristics.

Table 4 presents the summary statistics on review ratings and responses to customer reviews for all the tours. In Table 4, the last column provides the percentage of reviews that receive the firm’s responses by review rating. We see that when ratings decrease, firms are more likely to respond, thereby indicating that firms are selective when responding to reviews.

Consumers can specify the attributes of a desired tour at Ctrip.com based on features such as destination city, departure city, length of travel time, and travel type (guided tour or not). Ctrip.com returns a list of tours that meet the user-specified criteria. Since these tours share similar characteristics, they are directly competing with each other.

<table><tr><td colspan="6">Table 3. Summary Statistics of the Data</td></tr><tr><td>Variable</td><td>Obs.</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td> $S_i(t)$ </td><td>102079</td><td>2.740</td><td>7.402</td><td>0</td><td>110</td></tr><tr><td> $p_i(t)$ </td><td>102079</td><td>2945.606</td><td>3817.061</td><td>100</td><td>24523</td></tr><tr><td> $q_i(t)$ </td><td>102079</td><td>1.665</td><td>0.243</td><td>0</td><td>2</td></tr><tr><td> $Destination_i$ </td><td>317</td><td>0.539</td><td>0.499</td><td>0</td><td>1</td></tr><tr><td> $Duration_i$ </td><td>317</td><td>4.319</td><td>2.682</td><td>1</td><td>12</td></tr><tr><td> $Type_i$ </td><td>317</td><td>0.315</td><td>0.465</td><td>0</td><td>1</td></tr><tr><td> $Transportation_i$ </td><td>317</td><td>0.552</td><td>0.498</td><td>0</td><td>1</td></tr><tr><td> $Agent_i$ </td><td>317</td><td>0.965</td><td>0.183</td><td>0</td><td>1</td></tr></table>

Table 4. Distribution of Customer Review Ratings and the Fraction of Reviews with Responses

<table><tr><td>Review rating</td><td>No. of reviews</td><td>No. of responses</td><td>Fraction with response</td></tr><tr><td>1</td><td>648</td><td>550</td><td>84.88%</td></tr><tr><td>2</td><td>435</td><td>378</td><td>86.90%</td></tr><tr><td>3</td><td>3212</td><td>1396</td><td>43.46%</td></tr><tr><td>4</td><td>19042</td><td>2978</td><td>15.64%</td></tr><tr><td>5</td><td>53414</td><td>1166</td><td>2.18%</td></tr><tr><td>Total</td><td>76751</td><td>6468</td><td>8.43%</td></tr></table>

Each tour has its departure city, which defines its target market for prospective customers. Accordingly, we regard tours with the same departure city as likely competing for the same pool of customers.<sup>10</sup> Customers often compare similar tours when they make their purchase decisions. To ensure more homogeneous markets, based on the destination, we further split the tours into two markets — Market I (domestic, 171 tours) and Market II (overseas, 146 tours) — and then estimated model parameters for these two markets separately. Next, we describe our model estimation and results.

## Model Estimation and Results

In this section, we first describe how we estimated the model and then proceed to report the estimation results. Finally, we empirically verify that customers’ belief in mean market ratings $\mu ,$ as estimated from Equation (5), is close to the steady-state mean market rating estimated from Equation (11).

## Model Estimation and Identification

First, we provide the general idea of how we estimated parameters using maximum likelihood estimation (MLE). We first take a general SDE to illustrate, shown as

$$
\begin{array}{r} d y _ {i} (t) = y _ {i} (t + d t) - y _ {i} (t) \\ = f (y _ {i} (t), t) d t + g (y _ {i} (t), t) d Z _ {i} (t) \end{array}
$$

where $y _ { i } ( t )$ is the state variable, $d y _ { i } ( t )$ is the change in the state variable from time ?? to $t + d t$ , and $d Z _ { i } ( t )$ is the increment of a Wiener process, i.e., $d Z _ { i } ( t ) \sim N ( 0 , d t )$ When ???? is small, $d y _ { i } ( t )$ follows a normal distribution with mean $f ( y _ { i } ( t ) , t ) d t$ and variance $g ^ { 2 } ( y _ { i } ( t )$ , ??)????, given the state value of $y _ { i } ( t )$ at time ??. In other words, $y _ { i } ( t + d t )$ follows a normal distribution with mean $f ( y _ { i } ( t ) , t ) d t +$ $y _ { i } ( t )$ and variance $g ^ { 2 } ( y _ { i } ( t ) , t ) d t$ , conditional on the previous state $y _ { i } ( t )$ . Hence, the probability density function of $y _ { i } ( t + d t )$ conditional on the state value of $y _ { i } ( t )$ is

$$
\begin{array}{c} {p \big (y _ {i} (t + d t) \big | y _ {i} (t) \big)} \\ {= \frac {1}{\sqrt {2 \pi g ^ {2} (y _ {i} (t) , t) d t}} e ^ {- \frac {\big (y _ {i} (t + d t) - f (y _ {i} (t) , t) d t - y _ {i} (t) \big) ^ {2}}{2 g ^ {2} (y _ {i} (t) , t) d t}}.} \end{array}\tag{7}
$$

The log-likelihood function for the time series $y _ { i } ( t )$ with ?? observations is

$$
\ln L _ {i} (\Omega_ {i}) = \sum_ {t = 1} ^ {T - 1} \ln p (y _ {i} (t + d t) | y _ {i} (t); \Omega_ {i}, d t).\tag{8}
$$

For simplicity, we define $\varOmega _ { i }$ as a vector containing all the parameters to be estimated. Plugging Equation (7) into Equation (8) yields

$$
\begin{array}{c} \ln L _ {i} (\Omega_ {i}) = - \frac {(T - 1)}{2} \ln 2 \pi \\ - \frac {1}{2} \sum_ {t = 1} ^ {T - 1} \ln g ^ {2} (y _ {i} (t), t) d t - \sum_ {t = 1} ^ {T - 1} \frac {\left(y _ {i} (t + d t) - f (y _ {i} (t) , t) d t - y _ {i} (t)\right) ^ {2}}{2 g ^ {2} (y _ {i} (t) , t) d t}. \end{array}\tag{9}
$$

The maximum likelihood estimate $\hat { \varOmega } _ { i }$ is solved by maximizing the log-likelihood function described in Equation (9) over its parameter space:

$$
\hat {\Omega} _ {i} = \underset {\Omega_ {i}} {\arg \max} \ln L _ {i} (\Omega_ {i}).\tag{10}
$$

Next, we describe how we conducted the estimation for our specific controlled diffusion processes step by step.

For Equation (5a), we constructed its log-likelihood function using a conditional normal distribution. Then, we applied MLE to jointly estimate tour-specific parameters (e.g., customer rating sensitivity $\beta _ { i }$ and magnitude of volatility $\sigma _ { i }$ as defined in Equation 5a) for all the tours and the common belief in mean market ratings $\mu ,$ , using time-series data on sales $S _ { i } ( t )$ and ratings ?? (??) of all the tours.<sup>11</sup> The parameters in the sales Equation (5a) are fully identified.

It is possible that there is seasonality in the sales data; thus, we conducted a seasonality test on the time series sales data of each tour. For this, we used the ETS model, which is a family of time series models with an underlying state space model (Hyndman & Athanasopoulos, 2018). The results show that seasonality is present in 19.6% of the tours. For those tours with seasonality, we decomposed the time series and removed the seasonal component to obtain deseasonalized sales for model estimation.

For Equation (5b), we constructed its log-likelihood function using a conditional normal distribution. Then, we applied MLE to estimate the parameters for each tour separately using the time series $x _ { i } ( t )$ of tour ??. For a clear explanation, we present the rating equation as follows:

$$
\begin{array}{r l} & d x _ {i} (t) = \lambda_ {i} \big (v _ {i} - x _ {i} (t) \big) d t \\ & \qquad + \zeta_ {i} \sqrt {\big (b - x _ {i} (t) \big) (x _ {i} (t) - a)} d W _ {i} (t), \\ & \text {where} \quad v _ {i} = \frac {(A _ {i} - \rho) b - k _ {i} (b - a)}{(A _ {i} - \rho)}, \quad \lambda_ {i} = A _ {i} - \rho , \quad \text {and} \quad A _ {i} = \\ & \sqrt {(\rho + k _ {i}) ^ {2} + \frac {\eta_ {i} \beta_ {i}}{\rho}}. \end{array}
$$

We chose a discount factor of $0 . 0 5 . ^ { 1 2 } \mathrm { W e }$ set $a = 1$ and $b =$ $5 ^ { 1 3 }$ and observed that $\beta _ { i }$ and $\eta _ { i }$ always appear together. Importantly, the value of $\beta _ { i }$ was already estimated from the previous step (the sales equation). Therefore, there are three parameters $( k _ { i } , \eta _ { i }$ and $\zeta _ { i } )$ to be estimated from the rating equation; these three parameters are fully identified.

We further discuss identification issues. First, the parameters in our model are tour specific, absorbing tourspecific unobserved effects.<sup>14</sup> Second, from Equation (5a), the left-hand side $( d S _ { i } ( t ) )$ is the first difference of sales, which cancels out time-invariant fixed effects (if any). Third, we added time-variant variables—namely, quality, extracted from the review texts and price—into the sales equation. Having these two important marketing-mix variables alleviates concerns about the presence of omitted variables. Fourth, the state variable was incorporated into the diffusion term (for example, ${ \sigma } _ { i } \sqrt { { S } _ { i } ( t ) } d Z _ { i } ( t )$ and $\zeta _ { i } \sqrt { ( x _ { i } ( t ) - a ) \big ( b - x _ { i } ( t ) \big ) } d W _ { i } ( t ) )$ to directly allow for the potential correlation between the variable and the diffusion term, thus tackling the potential endogeneity. Fifth, in the sales equation, the left-hand side is the change in sales at time ?? (???? (??)), and $x _ { i } ( t )$ on the right-hand side was constructed by taking the average of the most recent review ratings by time ?? to mitigate possible simultaneity. Finally, the values for sales and ratings were measured precisely, thus precluding the possibility of measurement errors. The Nelder-Mead simplex algorithm was applied to numerically obtain the MLE estimates. We then implemented the estimation procedure in MATLAB.

## Estimation Results

We estimated the tour-specific parameters for all the tours in these two markets separately.<sup>15</sup> For brevity, we present the key parameters of the tour-level estimation results for 10 representative tours in each market in Table 5. We also calculate each tour’s steady-state mean $\nu _ { i }$ in the last column. We report the fitness performance of the current model, along with different specifications of the diffusion terms, with the results shown in Appendix C. In addition, we also checked the predictive performance of the SDE model against benchmark models, including autoregressive moving average (ARMA) (Box et al., 2015) and generalized autoregressive conditional heteroscedasticity (GARCH) (Engle, 1982), and present this with the results shown in Appendix D. To summarize, the SDE model achieves better or on-par predictive performance compared to that of benchmark models.

As seen in Table 5, there is considerable variation in the parameter estimates across the tours. From the estimated values of $k _ { i } ,$ we see that tours have different values of the rating decay factor. To investigate what drives the magnitude of the decay factor, we ran a regression of the estimated values of $k _ { i }$ on all the tours’ average prices (logarithm) in each market. The coefficient is 0.37 with a ??-value less than 0.001 for the domestic market and 0.16 with a ??-value less than 0.001 for the overseas market, thereby indicating that larger values of the decay factor are associated with products (tours) with higher prices. This implies that the ratings of higherpriced tours tend to fall more rapidly than the ratings of lowerpriced tours. Hence, consumers are more demanding (of management response) for tours with higher prices, and ratings of those tours decay faster. The parameter $\beta _ { i }$ measures customer rating sensitivity. Taking tour 53694 as an illustration, its value of $\beta _ { i }$ is 0.99, meaning that if the rating gap between the focal tour and the belief in mean market ratings increases by 1, the focal tour’s sales change will increase by approximately 1 booking on average per day. We also observe that $\beta _ { i }$ varies a great deal across different tours. To investigate what drives the magnitude of customer rating sensitivity, we ran a regression of the estimated values of $\beta _ { i }$ on the tours’ average prices (logarithm) in each market. The coefficient is 0.33 with a ??-value less than 0.001 for the domestic market and is 0.17 with a ??-value less than 0.001 for the overseas market. That is, customers are more sensitive to ratings of tours with higher prices when making their purchase decisions. In addition, a larger decay factor is correlated with higher customer rating sensitivity (for example, the correlation coefficient is 0.45 with a ??-value less than 0.001 for the domestic market). This is expected since consumers are more demanding about products or services when they become more sensitive to ratings when making their purchase decisions.

## Empirical Validation of Equilibrium

To lend support to the use of mean market ratings in our model, we empirically validated that the estimated customer belief in mean market ratings from the controlled diffusion process is close to the steady-state mean market rating directly estimated from the market rating time-series. Using all the tour ratings data in market ??, we first constructed the market rating $m _ { j } ( t )$ as time-series data. The market rating can fluctuate over time. Mathematically, the market rating $m _ { j } ( t )$ at time ?? is defined as

$$
m _ {j} (t) = \frac {\sum_ {i = 1} ^ {n _ {j}} x _ {i} (t)}{n _ {j}},
$$

where $n _ { j }$ is the total number of tours pertaining to market ??.

We know that the rating process of a particular tour has a steady-state mean, i.e., $\mathbb { E } \big ( x _ { i } ( t ) \big ) = \nu _ { i } .$ . Hence, the market rating $m _ { j } ( t )$ must also have a steady-state mean, i.e., ?? $\begin{array} { r } { \left( m _ { j } ( t ) \right) = \frac { \sum _ { i = 1 } ^ { n _ { j } } \nu _ { i } } { n _ { j } } , } \end{array}$ which is a value that is independent of time. We therefore model the market rating to follow a simple mean-reverting process, known as the Ornstein-Uhlenback (O-U) (Brown, 2004) process as follows:<sup>16</sup>

$$
d m _ {j} (t) = \gamma_ {j} (\phi_ {j} - m _ {j} (t)) d t + \xi_ {j} d \omega_ {j} (t),\tag{11}
$$

where $d m _ { j } ( t )$ is the change in market rating pertaining to market $j ,$ ??ω (??) is the increment of a Wiener process following a normal distribution with a mean of zero and variance ????, $\phi _ { j }$ is the steady-state mean of the market rating pertaining to market $j , \gamma _ { j }$ is the drift parameter quantifying the magnitude of reversion speed of market $j ,$ and $\xi _ { j }$ measures volatility of the stochastic term of market $j .$ The fluctuation in market rating is captured by the speed of reversion $\gamma _ { j }$ and volatility $\xi _ { j }$ . Taken together, these three parameters reflect the aggregate impact of each tour’s action to manage its ratings in the market.

<table><tr><td colspan="8">Table 5. Estimation Results for 10 Tours</td></tr><tr><td colspan="8">Market I (domestic)</td></tr><tr><td>Tour ID</td><td> $\eta_i$ </td><td> $\beta_i$ </td><td> $k_i$ </td><td> $\mu$ </td><td> $\sigma_i$ </td><td> $\zeta_i$ </td><td> $v_i$ </td></tr><tr><td>29336</td><td>19.442*(14.237)</td><td>4.997**(2.826)</td><td>4.202***(0.371)</td><td>4.5***(0.16)</td><td>4.231***(0.182)</td><td>2.795***(0.042)</td><td>4.620</td></tr><tr><td>70550</td><td>2.231**(1.343)</td><td>5.392***(1.597)</td><td>0.973***(0.08)</td><td>4.5***(0.028)</td><td>2.08***(0.104)</td><td>0.61***(0.01)</td><td>4.749</td></tr><tr><td>94243</td><td>0.116***(0.005)</td><td>1.308**(0.597)</td><td>0.283*(0.178)</td><td>4.5***(0.07)</td><td>1.276***(0.037)</td><td>0.234***(0.004)</td><td>4.344</td></tr><tr><td>16311</td><td>73.016***(14.659)</td><td>3.242*(2.137)</td><td>8.066***(0.446)</td><td>4.5***(0.12)</td><td>3.09***(0.158)</td><td>1.834***(0.054)</td><td>4.534</td></tr><tr><td>1621699</td><td>4.986*(3.545)</td><td>1.301**(0.675)</td><td>1.125***(0.129)</td><td>4.5***(0.053)</td><td>0.981***(0.022)</td><td>0.929***(0.019)</td><td>4.605</td></tr><tr><td>1611924</td><td>34.31***(4.26)</td><td>1.535***(0.511)</td><td>5.946***(0.231)</td><td>4.5***(0.032)</td><td>0.738***(0.014)</td><td>0.515***(0.006)</td><td>4.278</td></tr><tr><td>63798</td><td>1.691***(0.047)</td><td>2.889**(1.601)</td><td>1.422**(0.753)</td><td>4.5***(0.124)</td><td>3.035***(0.142)</td><td>0.7***(0.021)</td><td>4.428</td></tr><tr><td>72603</td><td>7.324*(5.438)</td><td>0.91*(0.612)</td><td>2.04***(0.788)</td><td>4.5***(0.184)</td><td>1.984***(0.101)</td><td>0.575***(0.013)</td><td>4.302</td></tr><tr><td>53136</td><td>12.645**(7.057)</td><td>0.844**(0.462)</td><td>2.506***(0.876)</td><td>4.5***(0.104)</td><td>1.31***(0.024)</td><td>0.419***(0.007)</td><td>4.322</td></tr><tr><td>78266</td><td>72.39***(9.22)</td><td>0.1***(0.007)</td><td>0.603***(0.01)</td><td>4.5***(0.589)</td><td>1.203***(0.041)</td><td>1.973***(0.099)</td><td>4.799</td></tr><tr><td colspan="8">Market II (overseas)</td></tr><tr><td>Tour ID</td><td> $\eta_i$ </td><td> $\beta_i$ </td><td> $k_i$ </td><td> $\mu$ </td><td> $\sigma_i$ </td><td> $\zeta_i$ </td><td> $v_i$ </td></tr><tr><td>64102</td><td>3.538*(2.599)</td><td>2.64**(1.463)</td><td>2.176***(0.741)</td><td>4.6***(0.06)</td><td>1.892***(0.07)</td><td>0.569***(0.012)</td><td>4.369</td></tr><tr><td>62460</td><td>0.154***(0.004)</td><td>3.399***(1.269)</td><td>0.528*(0.359)</td><td>4.6***(0.054)</td><td>2.551***(0.059)</td><td>0.283***(0.004)</td><td>4.348</td></tr><tr><td>79152</td><td>1.385***(0.064)</td><td>0.458**(0.264)</td><td>0.497***(0.012)</td><td>4.6***(0.176)</td><td>1***(0.012)</td><td>0.44***(0.009)</td><td>4.440</td></tr><tr><td>62904</td><td>1.493***(0.044)</td><td>1.933**(1.131)</td><td>0.933***(0.379)</td><td>4.6***(0.122)</td><td>2.549***(0.101)</td><td>0.554***(0.012)</td><td>4.510</td></tr><tr><td>53694</td><td>1.498***(0.044)</td><td>0.99**(0.446)</td><td>0.649**(0.374)</td><td>4.6***(0.068)</td><td>1***(0.013)</td><td>0.457***(0.005)</td><td>4.523</td></tr><tr><td>55173</td><td>0.798***(0.057)</td><td>3.567*(2.383)</td><td>0.6***(0.158)</td><td>4.6***(0.063)</td><td>2.567***(0.116)</td><td>1.154***(0.03)</td><td>4.681</td></tr><tr><td>72202</td><td>14.257**(7.667)</td><td>3.304***(0.987)</td><td>1.327***(0.133)</td><td>4.6***(0.075)</td><td>2.852***(0.11)</td><td>1.18***(0.034)</td><td>4.827</td></tr><tr><td>77480</td><td>5.293***(0.417)</td><td>0.501**(0.261)</td><td>0.4***(0.126)</td><td>4.6***(0.113)</td><td>0.849***(0.023)</td><td>1.008***(0.019)</td><td>4.779</td></tr><tr><td>29605</td><td>1.212***(0.045)</td><td>1.771**(0.969)</td><td>0.285*(0.18)</td><td>4.6***(0.081)</td><td>1.882***(0.082)</td><td>0.403***(0.005)</td><td>4.825</td></tr><tr><td>64358</td><td>3.842**(2.245)</td><td>0.99*(0.724)</td><td>0.792***(0.168)</td><td>4.6***(0.069)</td><td>1***(0.044)</td><td>0.233***(0.004)</td><td>4.636</td></tr></table>

Note: The estimation is based on the in-sample data for each tour. $\star \star \star \ : p \ : < \ : 0 . 0 1 ; ^ { \star \star } p \ : < \ : 0 . 0 5 ; ^ { \star } p \ : < \ : 0 . 1$ . The standard errors are reported in parentheses.

<table><tr><td colspan="4">Table 6. Estimation Results on Market Ratings</td></tr><tr><td></td><td> $\phi_j$ </td><td> $\gamma_j$ </td><td> $\xi_j$ </td></tr><tr><td>Market I</td><td>4.51***(0.011)</td><td>0.0301***(0.0122)</td><td>0.0057***(0.0002)</td></tr><tr><td>Market II</td><td>4.59***(0.085)</td><td>0.0019**(0.0009)</td><td>0.0054***(0.0002)</td></tr></table>

Note: The standard errors are reported in parentheses. \*\*\* $\displaystyle { { } ^ { \star } p < 0 . 0 1 ; { } ^ { \star \star } p < 0 . 0 5 ; { } ^ { \star } p < 0 . 1 }$

Using the time series of the market rating data, we applied MLE to estimate the parameters $\gamma _ { j } , \phi _ { j }$ , and $\xi _ { j }$ for Market I (domestic) and Market II (overseas) separately. As the O-U process follows a normal distribution, we construct the log-likelihood function using the density of the normal distribution. Table 6 shows the estimation results for both markets. We observe that the market rating has a lower level of volatility than a single focal tour’s rating. For example, for Market I, the parameters $\zeta _ { i }$ (ranging from 0.4 to 2.8 in Table 5) and $\xi _ { 1 }$ (with the value of 0.0057) measure the magnitude of volatility in a focal tour’s ratings and that in the domestic market ratings. For Market II, the parameters $\zeta _ { i }$ (ranging from 0.2 to 1.2 in Table 5) and $\xi _ { 2 }$ (with the value of 0.0054) measure the magnitude of volatility in a focal tour’s ratings and in the overseas market ratings. This is reasonable since the market rating is an aggregate of many individual tour ratings. From the raw time-series data, the mean market rating is 4.51 for Market I and 4.57 for Market II. In Table $^ { 5 , }$ the beliefs estimated from the controlled diffusion model in Equation (5) are 4.5 for Market I and 4.6 for Market II. Both mean market ratings $( \hat { \mu } _ { 1 } = 4 . 5$ and $\hat { \mu } _ { 2 } = 4 . 6 )$ estimated from Equation (5) lie close to the mean market ratings $( \hat { \phi } _ { 1 } =$ 4.51 and $\hat { \phi } _ { 2 } = 4 . 5 9 )$ directly estimated from the O-U process in Equation (11). The consistent results from both markets validate our main finding that relative, rather than absolute, ratings drive sales.

When we estimate the value of customer belief in mean market ratings (??), we allow its value to be freely chosen; i.e., it is not forced to be related to the average market rating. However, in the end, we find that the estimated value of the belief matches the steady-state mean market rating. We believe that the idea that a consumer will interpret the rating of a firm (or tour) in a relative sense is quite reasonable and intuitive. Perhaps this is why some platforms, such as Taobao.com, have begun to display the average rating of competing firms next to the rating of the focal firm. Our empirical findings also support our claim that relative rather than absolute ratings are important. If ratings were not relative, the estimated value of $\mu$ that best fits the data should not be statistically significant (or different from zero), thereby implying that the focal tour’s sales only depend on its ratings. However, our findings show that the anchor is not only significantly different from zero but that its value is close to the steady-state mean of the market rating.

## Implications

We begin with a discussion of the impact of a tour’s factors (e.g., profit margin, rating decay factor, and customer rating sensitivity) on different outcomes, namely, the optimal effort and profit. We then study the impact of a different response strategy on sales. Finally, we discuss the role of competition on these outcomes.

## Analyses of Economic Effects

First, we explore how a focal tour’s factors (e.g., profit margin, rating decay factor, and customer rating sensitivity) affect its optimal effort (response strategy) and profit.<sup>17</sup> As the optimal effort depends on the current state $x _ { i } ( t )$ , we examine the impact of the factors on the optimal effort in a steady state (i.e., let $x _ { i } ( t ) = \nu _ { i } )$ . Since we can solve the optimal response strategy and the optimal value function (profit) analytically, we can derive the closed-form expressions of the marginal impact of policyinvariance parameters on ratings and profit (see Appendix B). Hence, we can directly calculate values of marginal impact on decisions and outcomes instead of simulating the impact as is done in most of the structural modeling literature (Erdem & Keane, 1996; Huang et al., 2015; Zhang et al., 2019; Zheng et al., 2020). We calculated the marginal effect of each tour’s key factors on its optimal effort and profit using the estimated parameters (from Table 5) and the expressions of the derivatives (see Appendix B); results are presented in Table 7.

## Impact of Profit Margin

In Table 7, we see that the marginal effect of the profit margin on the optimal control effort $( \frac { \partial u _ { i } ^ { * } } { \partial \eta _ { i } } )$ is positive for all tours. An increase in the focal tour’s profit margin encourages the tour to put more effort into managing its reviews (increase ??<sup>∗</sup>). From Table 7, we can identify those focal tours where the effort is more sensitive to the profit margin. Overall, judging from the results in Tables 5 and 7, low values of profit margin ?? correspond to high values of $\cdot \frac { \partial u _ { i } ^ { * } } { \partial \eta _ { i } } ,$ , thereby implying that there is a diminishing impact of the profit margin on the increase in the optimal effort. Figure 3a illustrates this effect for representative tour 64358. This is basically a result of the square root form used for the relationship between the effort and the rating. Tour managers can use this finding to locate the tour in Figure 3a to understand how much they would need to react if the profit margin were to change.

<table><tr><td colspan="7">Table 7. Results on Marginal Effects</td></tr><tr><td colspan="7">Market I</td></tr><tr><td>Tour ID</td><td> $\frac{\partial u_i^*}{\partial \eta_i}$ </td><td> $\frac{\partial u_i^*}{\partial \beta_i}$ </td><td> $\frac{\partial u_i^*}{\partial k_i}$ </td><td> $\frac{\partial V_i}{\partial \eta_i}$ </td><td> $\frac{\partial V_i}{\partial \beta_i}$ </td><td> $\frac{\partial V_i}{\partial k_i}$ </td></tr><tr><td>29336</td><td>0.381</td><td>1.482</td><td>2.352</td><td>3154.092</td><td>235.168</td><td>-7174.572</td></tr><tr><td>70550</td><td>0.924</td><td>0.382</td><td>3.256</td><td>555.465</td><td>168.752</td><td>-2694.463</td></tr><tr><td>94243</td><td>3.475</td><td>0.308</td><td>1.343</td><td>179.283</td><td>-13.675</td><td>-239.590</td></tr><tr><td>16311</td><td>0.178</td><td>4.016</td><td>1.950</td><td>813.159</td><td>-2242.884</td><td>-10699.294</td></tr><tr><td>1621699</td><td>0.392</td><td>1.504</td><td>2.275</td><td>95.536</td><td>26.721</td><td>-1834.068</td></tr><tr><td>1611924</td><td>0.233</td><td>5.214</td><td>1.171</td><td>601.982</td><td>-5390.501</td><td>-4382.380</td></tr><tr><td>63798</td><td>1.249</td><td>0.731</td><td>1.573</td><td>1144.480</td><td>-139.976</td><td>-1446.502</td></tr><tr><td>72603</td><td>0.381</td><td>3.063</td><td>1.227</td><td>651.080</td><td>-1065.773</td><td>-1576.295</td></tr><tr><td>53136</td><td>0.274</td><td>4.105</td><td>1.277</td><td>1756.497</td><td>-1709.454</td><td>-2019.327</td></tr><tr><td>78266</td><td>0.019</td><td>14.105</td><td>3.814</td><td>30.141</td><td>7341.127</td><td>-2144.808</td></tr><tr><td colspan="7">Market II</td></tr><tr><td>Tour ID</td><td> $\frac{\partial u_i^*}{\partial \eta_i}$ </td><td> $\frac{\partial u_i^*}{\partial \beta_i}$ </td><td> $\frac{\partial u_i^*}{\partial k_i}$ </td><td> $\frac{\partial V_i}{\partial \eta_i}$ </td><td> $\frac{\partial V_i}{\partial \beta_i}$ </td><td> $\underline{\frac{\partial V_i}{\partial k_i}}$ </td></tr><tr><td>64102</td><td>0.877</td><td>1.174</td><td>1.401</td><td>641.417</td><td>-538.699</td><td>-1938.344</td></tr><tr><td>62460</td><td>4.853</td><td>0.220</td><td>1.348</td><td>78.931</td><td>-25.087</td><td>-449.189</td></tr><tr><td>79152</td><td>0.542</td><td>1.640</td><td>1.615</td><td>344.546</td><td>-161.607</td><td>-520.325</td></tr><tr><td>62904</td><td>0.992</td><td>0.766</td><td>1.857</td><td>375.926</td><td>-122.305</td><td>-1160.571</td></tr><tr><td>53694</td><td>0.697</td><td>1.054</td><td>1.909</td><td>111.001</td><td>-112.866</td><td>-835.910</td></tr><tr><td>55173</td><td>1.436</td><td>0.321</td><td>2.720</td><td>598.021</td><td>2.100</td><td>-1261.674</td></tr><tr><td>72202</td><td>0.233</td><td>1.007</td><td>4.193</td><td>596.540</td><td>1059.717</td><td>-5559.602</td></tr><tr><td>77480</td><td>0.170</td><td>1.800</td><td>3.564</td><td>52.335</td><td>270.245</td><td>-1280.494</td></tr><tr><td>29605</td><td>0.589</td><td>0.403</td><td>4.165</td><td>541.233</td><td>88.988</td><td>-1178.654</td></tr><tr><td>64358</td><td>0.372</td><td>1.442</td><td>2.444</td><td>-52.404</td><td>-73.785</td><td>-1426.380</td></tr></table>

![](/api/attachments/MZR5VZQM/fulltext/images/0cc72b2c290f7409e08d1a26b84005071911b536bc46c4fa9201bab8590a75e8.jpg)

![](/api/attachments/MZR5VZQM/fulltext/images/19ade9d823398332b4e79ab6ff51965fbc9fba3c262dc18d3910a4cb68ae57b3.jpg)  
Figure 3. The Impact of the Profit Margin on the Optimal Effort and Profit for Tour 64358

From Table 7, we see that the marginal effect of the profit margin on profit is positive for most tours except for tour 64358. This appears to be an anomaly because an increase in profit margin should not reduce profits. However, such an anomaly can occur for a tour that is operating at a loss. We plotted the profit for tour 64358 in Figure 3b and found that this is indeed the case (the profit margin estimate for this tour is 3.8). Figure 3b shows that tour 64358 must increase its margin to approximately 29 to attain a positive profit. The main takeaway of this finding applies to firms that are currently operating at a loss. For such tours, even though they follow the optimal strategy, they still suffer losses. However, they would lose more if they did not follow the optimal strategy. Based on our results, the number of tours operating at a loss is very small, i.e., less than 5%.

It is not unreasonable to see loss-making tours in reality. This may be the consequence of a tour not adopting the best response strategy or parameter conditions that do not allow the tour to make a profit, even if it uses the optimal response strategy. Our analysis could help such a tour to identify the parameter conditions it needs to achieve for turnaround, or to make a positive profit, $\mathrm { e . g . }$ , the minimum profit margin it should strive for if it wants to make a profit. This is one advantage of a structural methodology.

## Impact of Rating Decay

In Table 7, we see that the marginal effect of the decay factor $( k _ { i } )$ on effort is positive, i.e., the optimal effort increases with the magnitude of the decay factor. In Appendix B, we show that when customers are less sensitive to ratings and the profit margin is also low, it is possible that a tour manager would not have an incentive to increase effort in responding to customer reviews, even if its consumers become more demanding (corresponding to a higher value of $k _ { i } )$ . That is, it is possible that $\frac { { \partial } u ^ { * } } { { \partial } k _ { i } }$ would be negative; however, this situation did not arise in our data. On the other hand, the marginal effect of the decay factor on profit is always negative, as seen in Table 7. Thus, an increase in the rating decay factor always hurts the tour’s profit regardless of whether it increases or decreases the response effort.

## Impact of Customer Rating Sensitivity

When the primitive on customer rating sensitivity $( \beta _ { i } )$ changes, the focal tour’s strategy resonates; hence, its profit is impacted. Once again, we focus on the optimal control $\boldsymbol { u } _ { i } ^ { * }$ in the steady state to derive insights. In Table 7, we see that the marginal effect of customer rating sensitivity $( \beta _ { i } )$ on effort is positive for all tours. It is always optimal to increase effort when customers become more sensitive to ratings. However, the marginal effect of customer rating sensitivity on profit $( \frac { \partial V _ { i } } { \partial \beta _ { i } } )$ is positive for some tours and negative for others. To investigate what drives the value of $\frac { \partial V _ { i } } { \partial \beta _ { i } } ,$ we define the gap between the focal firm’s steady-state rating and mean market rating, denoted as $\delta _ { i } = \nu _ { i } - \mu .$ . Generally, when the rating gap is large, the focal firm is more affected (either positively or negatively) by the change in customer rating sensitivity $( \beta _ { i } )$ If the gap is relatively large and the focal firm’s rating is above the market mean, then an increase (decrease) in customer rating sensitivity leads to a relatively large increase (decrease) in profit. On the other hand, when the gap is large and the focal firm’s rating is below the market mean, then an increase (decrease) in customer rating sensitivity can decrease (increase) the focal firm’s profit.

## Adopting a Different Response Strategy

One key advantage of the controlled diffusion process is that it allows us to conduct analyses to answer “what-if” questions. While in the previous subsection, we presented sensitivity results (i.e., impact on different outcomes when values of the parameters change such as the profit margin), we now present the impact on different outcomes when the response strategy changes; i.e., what would happen (to ratings and sales) if the tour managers were to choose a different response strategy?

Using the parameters estimated for a tour, we can calculate the tour’s optimal response strategy, which is a function of the state (see Equation 4). What is an operational interpretation for the control $( u _ { i } ) !$ The control effort (response strategy) could represent the number of personnel (or the total number of staff hours) assigned to provide management responses. The response strategy can be static (e.g., always assigning a fixed total number of staff hours) or dynamic (e.g., the assigned number of staff hours depends on the current ratings at different times). To operationalize the response strategy, we used the response ratio (given a state value, the frequency of the state value where management responses are provided divided by the frequency of the state value), denoted as $p ( x _ { t } )$ A higher response ratio implies that the management response is more frequent; therefore, it is also likely that more resources (effort) are spent responding.

There is ample anecdotal evidence to justify the importance of response ratio as a tactic for managing reviews. For example, reviewtrackers.com maintains that calibrating the ideal response rate (to negative reviews) is one of the keys to creating an effective review response policy (Reviewtrackers, 2021). Hospitality best practices for industry professionals have come up with a rule of thumb for the best response ratio, i.e., “an appropriate objective could be to respond to 40% of reviews” (ReviewPro 2017). Liu et al. (2020) have also highlighted the importance of the response ratio as a management tool and recommended a higher response ratio for negative reviews than that for positive reviews.

As mentioned earlier, one benefit of our approach is that it enables us to conduct what-if analysis. We use tour 78266 to illustrate. For example, as shown in Figure 4a, we observe that the probability of responding $( p ( x _ { t } ) )$ for tour 78266 decreases as the state variable (?? ) increases, which is consistent with the (theoretical) optimal response strategy derived from our model. To see how this tour would perform under a different response strategy, let us hypothetically consider a constant response strategy, where the probability of responding is independent of the state value. We simulate the impact of a constant response strategy by replacing the tour’s actual response strategy in the rating equation with a constant response strategy, thereby implying that regardless of the state variable of rating, the tour has a 50% chance of responding to a review.

We next explore what the ratings and sales would be if tour 78266 used a constant response strategy instead of the optimal one.<sup>18</sup> We simulated the trajectory of ratings over time following Equation (2) and, further, the trajectory of sales over time following Equation (1). We repeated the simulation for 1,000 iterations and then took the average to smooth out the randomness. The mean ratings were 4.7 under the optimal response strategy and 4.54 under the constant response strategy. We used the out-of-sample period to plot the observed sales and a fitted trend line of observed sales in Figure 4b.<sup>19</sup> Figure 4b also displays the simulated sales figure for the out-of-sample period under the constant response strategy and the optimal response strategy.<sup>20</sup> Finally, we calculated the total sales in the out-of-sample period and found that the tour would have generated 7.5% fewer sales if it had adopted the constant response strategy.

The current response strategy mentioned above depends on ratings only. However, in practice, it is possible that the probability of responding to customer reviews depends not only on ratings but also on other factors related to the review text. Therefore, we extended our model to incorporate the other aspects of reviews to show the flexibility of our model in handling multidimensional state variables. In Appendix E, we illustrate how the response strategy could work with a composite state variable that is composed of a review rating, review text negativity, and review text specificity. The key insights gained are consistent with earlier findings. Please refer to Appendix E for more details. To implement the optimal response strategy in practice, the tour manager needs to use tour parameters to determine the optimal strategy. In the paper, the tour parameters are estimated from the observed data, assuming the firm was adopting the optimal response strategy. However, a firm cannot optimally choose its efforts before knowing the relevant parameters (a “chicken-and-egg” problem). Thus, how can firms implement an optimal response strategy before they know the relevant parameters? One reasonable approach for a firm would be to use a convenient response strategy to start with (e.g., a constant response strategy) and generate some data that can be used to estimate the relevant parameters. Then, the firm could decide on the optimal strategy using the parameters from this initial burn-in period.

## Competitive Analysis

Returning to the tour that is operating at a loss, the belief in mean market ratings could impact this focal tour’s profit. This belief could play a role in the tour’s individual rationality constraint, i.e., it could determine whether the tour would remain operative, assuming that a minimum level of profit is needed to do so. In Figure 5, we plot the profit with respect to the mean market rating for tour 64358 pertaining to the overseas market. As the mean market rating increases, this tour’s profit decreases. The current mean rating (??) of the overseas market is 4.6, and this tour incurs a negative profit. However, its profit would become positive if the mean market rating were to reduce to approximately 4.1. In a sense, this suggests that the tour would be better off targeting a lower market (e.g., a market segment with lower ratings), as far as profit is concerned.

![](/api/attachments/MZR5VZQM/fulltext/images/59261d5b3ebd963642028e29473d20085bdc017b006bf396c6c54d302a297def.jpg)

(b)  
![](/api/attachments/MZR5VZQM/fulltext/images/b638f7395d3adc7d8e77629c997978cf6d4076999ac57a8eb14c61ec5336d30d.jpg)  
Figure 4. Observed versus Simulated Response Strategies and Sales for Tour 78266

![](/api/attachments/MZR5VZQM/fulltext/images/1b16bbe36b9e2fceafad583d58b0c5e019af33c4df45f673f91a5d5a824a6364.jpg)  
Figure 5. The Impact of the Belief in Mean Market Ratings on Profit for Tour 64358

The mean market rating reflects the intensity of competition in the market. A higher value of $\mu$ indicates greater competitive intensity and hurts the sales of all tours in the market, as captured in Equation (1), where competition intensity (??) exhibits a negative impact on sales. We next numerically illustrate the impact of a parameter change (of each tour) on the optimal response strategy, the steady-state mean rating, the mean market rating (competition intensity), and further profit.

Suppose that the profit margins of all tours in the overseas market were to increase by 10% resulting from, for example, a change in tax law, travel restrictions due to COVID-19, or from a change in the minimum wage law. Using the optimal control effort from Equation (4), we can calculate the new optimal control effort for each tour. Furthermore, we can calculate each tour’s steady-state mean rating using the expression of $\nu _ { i }$ . The mean market rating is the average of all the tours’ steady-state mean ratings, that is, $\begin{array} { r } { \mu = \frac { \sum _ { i = 1 } ^ { n } \nu _ { i } } { n } } \end{array}$ , where ?? is the number of tours in a specific market. Plugging the updated mean market rating, we can simulate the impact on the sales of each tour using Equation (5a). As a result of the increase in profit margin, the mean market rating changes from 4.6 to 4.7. This increase in the mean market rating occurs because the profit margins of all the tours in the market increase. Hence, each tour expends more effort to manage its reviews, pushing its steady-state mean rating higher. This, in turn, increases the mean market rating. In other words, the increase in the profit margin motivates each tour to exert more effort to boost its ratings, thus increasing the intensity of ratings competition in the market.

From the sales equation in Equation (5a), the focal tour’s sales are hurt by the increase in the mean market rating (??), which has a direct negative impact on sales. Therefore, instead of boosting sales, the increase in profit margin hurts sales. Even though sales decrease, the increase in profit margin could compensate for the decrease in sales and thus increase profit. However, we note that for different tours, the percentage of profit (value function) change varies across tours, although all the tours have the same percentage increase in the change of profit margin (10%). For example, the profit of tour 29605 increases by 6.5%. However, tour 77480 shows a profit decrease of 3.2%. Thus, firms can gain (or lose) differently when faced with the same event in the market. Our controlled diffusion model allows us to conduct such competitive simulations for different market events.

## Conclusion

Unlike most studies that address response strategies from a single firm perspective, we consider a competitive setting where each firm in a market attempts to manage its ratings via a response strategy and the effects of their responses are interwoven. Another distinguishing feature of our study is that we develop response strategies that consider the relationship between ratings and sales and hence profit. That is, we are among the first to consider the implication chain involving both the antecedents and consequences of ratings: response strategy → ratings → sales → profit. Our unique dataset enables us to unravel this underlying mechanism, while the literature predominately focuses either on the partial path between responses and ratings or between ratings and sales (Gu & Ye, 2014; Lee et al., 2016; Proserpio & Zervas, 2017; Wang & Chaudhry, 2018).

To this end, we develop a controlled diffusion model in which a focal firm’s sales are driven by customers’ belief in mean market ratings and its own ratings that are maneuvered by the firm using a response strategy to maximize profit. Our model is estimated using data from Ctrip.com, which is the leading travel aggregator in China. Our model embeds the response strategy, allowing us to conduct analyses to answer what-if questions. For example, how would it affect ratings and further sales if a tour manager adopted some other response strategy? How would the change of some parameters impact the competition and further the profit? We also investigate the marginal impact of parameters on the optimal control effort and further profit. That is, the controlled diffusion model we develop is prescriptive in nature.

We offer several recommendations for managers responsible for managing ratings: (1) optimize, rather than maximize; (2) responding is not just a service operations issue; (3) respond strategically. We discuss these recommendations below.

## Optimize, Rather Than Maximize

Business executives often consider ratings as a “health-status indicator” for the firm. Hence, they have the tendency to implement aggressive plans to improve ratings at all costs. However, we observe that rating competition is a much more nuanced phenomenon. Specifically, we observe that the mean market rating of the tours has a direct impact on the sales of a firm. This is because customers use mean market ratings as an anchor when they interpret a particular firm’s rating. This anchor results from the joint, optimal actions of different firms in the market. The finding that ratings are relative implies that a firm does not necessarily need to maximize its ratings; rather, it needs to stay ahead of its competitors. There is a deeper implication of this finding. As a firm exerts more effort to improve its ratings, two effects emerge: a direct (positive) effect of an increase in ratings and an indirect (adverse) effect of increasing the mean market rating. For a market with a very large number of firms, the indirect effect would be expected to be minimal. However, in many markets, there are often small, fiercely competing segments (e.g., in the hotel industry, only a handful of four-star hotels in a neighborhood intensely compete with one another). When the cardinality of the competing set is small, the impact of one firm’s effort could loom large. There are multiple reasons to adopt the “optimize, rather than maximize” strategy: ratings are relative, not absolute, and a firm’s effort to improve its ratings places pressure on itself via the market.

## Responding Is Not Just a Service Operations Issue

Business executives must understand that managing response effort is not simply a service or part of “customer care” operations. Rather, the optimal response effort depends on a variety of factors that are well beyond the normal purview of a customer care department.

Customer rating sensitivity affects the correct level of service effort. When customers are more sensitive to ratings, the firm needs to exert more effort (but at a diminishing rate) to boost its mean rating. Customer rating sensitivity can be a friend or a foe, depending on the gap between the firm’s steady-state rating and the mean market rating.

The discussion above also applies to profit margins. The optimal effort always increases with the profit margin. Typically, an increase in profit margin boosts the firm’s profit. However, if the firm is already operating at a loss, increasing the profit margin may further reduce the profit.

In choosing a response effort, firms need to consider how demanding customers are of good service. High-end firms tend to have more demanding customers. As consumers become more demanding, the firm may sometimes need to decrease its effort since it is too costly to maintain a high rating. At other times, firms need to increase their effort in response to more demanding customers. As customers become more demanding, the firm’s profit decreases.

## Respond Strategically

Service managers must note that a constant response strategy is, in general, not optimal. The level of response effort must be chosen depending on the current rating. More importantly, the difference between the current rating and the maximum possible rating matters to the response effort. When the difference is low, the optimal response effort should also be low. Additionally, the optimal effort should increase slowly as the difference increases. The wider implication here is that firms need to build flexible capacity for managing reviews. Sometimes, the response activity may be intense, i.e., involving many service support personnel; however, at other times, a fewer number of personnel allocated to the job of responding may suffice. This has implications both for employee crosstraining to provide flexibility and for outsourcing service operations so that the capacity to respond can be agile. A constant response strategy is appealing from the perspective of being consistent, predictable, and easier to manage. However, our study has demonstrated that the difference between a constant response strategy and a feedback control strategy based on current ratings can be significant.

This study is not without limitations. First, we did not model certain types of dynamics, for example, the direct impact of management response in the sales equation. While this structure was acceptable in our context, in some other domains, it is possible that a direct impact may be present. Second, we did not consider a noisy specification of the firm’s control problem, thus implying, for example, that the states influencing a firm’s control were assumed to be accurately observable by the firm. Noise could be introduced in the specification of a stochastic control problem in several ways: (1) noisy observations, (2) optimization errors made by the firm, and (3) a combination of (1) and (2). This is a useful direction for future work on the estimation of controlled diffusion processes. Third, during the period of our data, customer reviews were listed according to the review date by default. It is possible that different customers may have different preferences (such as order by helpfulness of reviews) when reading reviews. This may affect how our state variable should best be constructed. Fourth, sales prediction is a challenging problem, and we acknowledge that there is room to further improve the predictive performance of our model. In this regard, SDE achieves better or comparable predictive performance compared with state-of-the-art benchmark models. However, we note that the SDE model is not just predictive but, more importantly, one that can be used in a prescriptive sense to answer what-if questions. Finally, our focus in this study was on the firm’s response strategy to manage user opinions instead of on how the actual response ought to be worded. While there are existing guidelines on how to construct a response—for example, avoiding the use of the same standard reply for every response, issuing a sincere apology, or being considerate (Bassig, 2017; TripAdvisor, 2014), a more comprehensive study of the optimal level of effort, as well as the manner in which the effort should be applied, would constitute a more complete solution to the problem.

## Acknowledgments

We greatly appreciate the constructive feedback from the senior editor, the associate editor, and the three anonymous reviewers. We also thank conference participants at CIST 2017, INFORMS Annual Meeting 2017, and Big XII+ MIS Research Symposium 2017 for their comments and feedback. Eric Zheng acknowledges grant support from National Natural Science Foundation of China (NSFC) (Grant 71831006).

## References

Anderson, K. C. (2012). The impact of social media on lodging performance. Cornell Hospitality Report, 12(15), 6-11.

Anderson, K. C., & Han, S. (2016). Hotel performance impact of socially engaging with consumers. Cornell Hospitality Report, 16(10), 3-9.

Baron, R. M., & Kenny, D. A. (1986). The moderator-mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations. Journal of

Personality and Social Psychology, 51(6), Article 1173. https://doi.org/10.1037/0022-3514.51.6.1173

Bass, F. M., Bruce, N., Majumdar, S., & Murthi, B. P. (2007). Wearout effects of different advertising themes: A dynamic Bayesian model of the advertising-sales relationship. Marketing Science, 26(2), 179-195. https://doi.org/10.1287/ mksc.1060.0208

Bassig, M. (2017). 8 Amazing examples of business owners responding to reviews. Reviewtrackers. https://www.review trackers.com/examples-responding-reviews/

Benkard, C. L., Jeziorski, P., & Weintraub, G. Y. (2015). Oblivious equilibrium for concentrated industries. The RAND Journal of Economics, 46(4), 671-708. https://doi.org/ 10.3386/w19307

Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time series analysis: forecasting and control. John Wiley & Sons.

Brown, R. G. (2004). Smoothing, forecasting and prediction of discrete time series. Prentice Hall.

Carter, R. (2022). The ultimate list of online review statistics for 2022. findstack. https://findstack.com/online-review-statistics/

Chen, W., Gu, B., Ye, Q., & Zhu, K. X. (2019). Measuring and managing the externality of managerial responses to online customer reviews. Information Systems Research, 30(1), 81-96. https://doi.org/10.1287/isre.2018.0781

Cox, J. C., Ingersoll, J. E., & Ross, S. A. (1985). A theory of the term structure of interest rates. Econometrica, 53(2), 385-407. https://doi.org/10.2307/1911242

Duan, W., Gu, B., & Whinston, A. B. (2008). The dynamics of online word-of-mouth and product sales—An empirical investigation of the movie industry. Journal of Retailing, 84(2), 233-242. https://doi.org/10.1016/j.jretai.2008.04.005

Engle, R. F. (1982). Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation. Econometrica, 50(4), 987-1007. https://doi.org/10.2307/ 1912773

Erdem, T., & Keane, M. P. (1996). Decision-making under uncertainty: Capturing dynamic brand choice processes in turbulent consumer goods markets. Marketing Science, 15(1), 1-20. https://doi.org/10.1287/mksc.15.1.1

Glassman, N. (2011). What every social media marketer should know about revinate. Adweek. http://www.adweek.com/ digital/socialmedia-apps-revinate/

Goh, K. Y., Heng, C. S., & Lin, Z. (2013). Social media brand community and consumer behavior: Quantifying the relative impact of user-and marketer-generated content. Information Systems Research, 24(1), 88-107. https://doi.org/10.1287/ isre.1120.0469

Golmohammadi, A., Havakhor, T., Gauri, D. K., & Comprix, J. (2021). Complaint publicization in social media. Journal of Marketing, 85(6), 1-23. https://doi.org/10.1177/00222429 211002183

Gu, B., & Ye, Q. (2014). First step in social media: Measuring the influence of online management responses on customer satisfaction. Production and Operations Management, 23(4), 570-582. https://doi.org/10.1111/poms.12043

Ho, Y. C., Wu, J., & Tan, Y. (2017). Disconfirmation effect on online rating behavior: A structural model. Information Systems Research, 28(3), 626-642. https://doi.org/10.1287/ isre.2017.0694

Huang, Y., Singh, P. V., & Ghose, A. (2015). A structural model of employee behavioral dynamics in enterprise social media. Management Science, 61(12), 2825-2844. https://doi.org/ 10.1287/mnsc.2014.2125

Hyndman, R. J., & Athanasopoulos, G. (2018). Forecasting: principles and practice. OTexts.

Jabr, W., & Zheng, Z. (2014). Know yourself and know your enemy: An analysis of firm recommendations and consumer reviews in a competitive environment. Management Information Systems Quarterly, 38(3), 635-654. https://doi.org/ 10.25300/MISQ/2014/38.3.01

Kent, K. (2014). Catching up with the competition: How to get more online reviews from your customers. Reviewtrackers https://www.reviewtrackers.com/catching-competition-onlinereviews-customers

Kumar, N., Qiu, L., & Kumar, S. (2018). Exit, voice, and response on digital platforms: An empirical investigation of online management response strategies. Information Systems Research, 29(4), 849-870. https://doi.org/10.1287/ isre.2017.0749

Kwark, Y., Lee, G. M., Pavlou, P. A., & Qiu, L. (2021). On the spillover effects of online product reviews on purchases: Evidence from clickstream data. Information Systems Research, 32(3), 895-913. https://doi.org/10.1287/ isre.2021.0998

Lee, Y. J., Xie, K., & Besharat, A. (2016). Management response to online WOM: Helpful or detrimental? In Proceedings of the Americas Conference on Information Systems.

Li, X., & Hitt, L. M. (2008). Self-selection and information role of online product reviews. Information Systems Research, 19(4), 456-474. https://doi.org/10.1287/isre.1070.0154

Liu, G., Fei, S., Yan, Z., Wu, C. H., & Tsai, S. B. (2020). An empirical study on response to online customer reviews and ecommerce sales: From the mobile information system perspective. Mobile Information Systems, 2020, Article 8864764. https://doi.org/10.1155/2020/8864764

Ma, L., Sun, B., & Kekre, S. (2015). The squeaky wheel gets the grease: An empirical analysis of customer voice and firm intervention on Twitter. Marketing Science, 34(5), 627-645. https://doi.org/10.1287/mksc.2015.0912

Mayzlin, D. (2006). Promotional chat on the internet. Marketing Science, 25(2), 155-163. https://doi.org/10.1287/ mksc.1050.0137

Mayzlin, D., Dover, Y., & Chevalier, J. (2014). Promotional reviews: An empirical investigation of online review manipulation. American Economic Review, 104(8), 2421-55. https://doi.org/10.1257/aer.104.8.2421

Medallia. (2015). Responding to social media boosts a company’s bottom line, new research finds. http://www.medallia.com/ press-release/responding-social-media-boosts-companysbottom-line-new-research-finds

Moe, W. W., & Schweidel, D. A. (2012). Online product opinions: Incidence, evaluation, and evolution. Marketing Science, 31(3), 372-386. https://doi.org/10.1287/mksc.1110.0662

Naik, P. A., Prasad, A., & Sethi, S. P. (2008). Building brand awareness in dynamic oligopoly markets. Management Science, 54(1), 129- 138. https://doi.org/10.1287/mnsc.1070.0755

Pavlou, P. A., & Dimoka, A. (2006). The nature and role of feedback text comments in online marketplaces: Implications for trust building, price premiums, and seller differentiation. Information Systems Research, 17(4), 392-414. https://doi.org/ 10.1287/isre.1060.0106

Proserpio, D., & Zervas, G. (2017). Online reputation management: estimating the impact of management responses on consumer reviews. Marketing Science, 36(5), 645-665. https://doi.org/10.1287/mksc.2017.1043

ReviewPro. (2017). Responding to online reviews: Speed or quantity? https://reviewproblog.shijigroup.com/respondingonline-reviews-speed-quantity/

Reviewtrackers. (2021). Powerful examples of how to respond to negative reviews and positive reviews. https://www.review trackers.com/guides/examples-responding-reviews/

Rubel, O., Naik, P. A., & Srinivasan, S. (2011). Optimal advertising when envisioning a product-harm crisis. Marketing Science, 30(1), 1048-1065. https://dx.doi.org/10.1287/ mksc.1110.0679

Sobel, M. E. (1982). Asymptotic confidence intervals for indirect effects in structural equation models. Sociological Methodology, 13, 290-312. https://doi.org/10.2307/270723

Sun, S., Gao, Y., & Rui, H. (2021). Does active service intervention drive more complaints on social media? The roles of service quality and awareness. Journal of Management Information Systems, 38(3), 579-611. https://doi.org/10.1080/ 07421222.2021.1958548

TripAdvisor. (2012). Survey finds half of TripAdvisor users will not book a hotel that has no reviews. http://ir.tripadvisor.com/releasedetail.cfm?releaseid=721288

TripAdvisor. (2014). How to add management responses to TripAdvisor traveler reviews. https://www.tripadvisor.com/ TripAdvisorInsights/n2428/how-add-management-responsestripadvisor-traveler-reviews

## About the Authors

Mingwen Yang is an assistant professor of information systems at the Michael G. Foster School of Business, University of Washington. She received her Ph.D. from the Jindal School of Management, University of Texas at Dallas. Her current research interests are social trading, fintech, and cybersecurity.

Zhiqiang (Eric) Zheng is the Ashbel Smith Professor in Information Systems and Finance at the Jindal School of Management, University of Texas at Dallas. He received his Ph.D. from the Wharton School of Business. His current research interests focus on fintech, blockchain, and healthcare analytics. He has served as a senior editor for Information Systems Research.

Wang, Y., & Chaudhry, A. (2018). When and how managers responses to online reviews affect subsequent reviews. Journal of Marketing Research, 55(2), 163-177. https://doi.org/10. 1509/jmr.15.0511

Wu, R., & Qiu, C. (2016). Seller manipulation of consumer reviews under competition. In Proceedings of the 49th Hawaii International Conference on System Sciences (pp. 3575-3583).

Yang, M., Zheng, Z., & Mookerjee, V. (2019). Prescribing response strategies to manage customer opinions: A stochastic differential equation approach. Information Systems Research, 30(2), 351-374. https://doi.org/10.1287/isre.2018.0805

Yang, M., Zheng, Z., & Mookerjee, V. (2021). The race for online reputation: implications for platforms, firms, and consumers. Information Systems Research, 32(4), 1262-1280. https://doi.org/10.1287/isre.2021.1005

Ye, Q., Gu, B., Chen, W., & Law, R. (2008). Measuring the value of managerial responses to online reviews-A natural experiment of two online travel agencies. In Proceedings of the International Conference on Information Systems.

Zhang, S., Singh, P. V., & Ghose, A. (2019). A structural analysis of the role of superstars in crowdsourcing contests. Information Systems Research, 30(1), 15-33. https://doi.org/10.1287/ isre.2017.0767

Zheng, J., Ren, F., Tan, Y., & Chen, X. (2020). Optimizing twosided promotion for transportation network companies: A Structural model with conditional Bayesian learning. Information Systems Research, 31(3), 692-714. https://doi.org/ 10.1287/isre.2019.0908

Zheng, Z., Fader, P., & Padmanabhan, B. (2012). From business intelligence to competitive intelligence: Inferring competitive measures using augmented site-centric data. Information Systems Research, 23(3), 698-720. https://dx.doi.org/10.1287/ isre.1110.0385

Zhu, F., & Zhang, X. (2010). Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. Journal of Marketing, 74(2), 133-148. https://doi.org/10.1509/jm.74.2.133

Vijay Mookerjee is the Charles and Nancy Davidson Chair Professor in Information Systems at the Jindal School of Management, University of Texas at Dallas. He received his Ph.D. from the Krannert School of Management, Purdue University. His current research interests are digital adverting, fintech, mechanism design, and cloud computing. He was named an INFORMS Information Systems Society (ISS) Distinguished Fellow in 2011. He has served in editorial positions at Information Systems Research, Management Science, Operation Research, INFORMS Journal on Computing, etc. He currently serves as a department editor for Production and Operations Management and as an editor-in-chief for Information Technology and Management.

Hongyu Chen is an associate professor in information systems at the College of Business, California State University, Long Beach. He received his Ph.D. from the Jindal School of Management, University of Texas at Dallas. His research interests are data mining theories and applications.

## Appendix A

## Solving the Stochastic Optimal Control Problem

In this part, we derive how to solve the stochastic optimal control problem in Equation (A-1). For notation simplicity, we suppress a tourspecific subscript ?? to avoid clutter:

$$
\max _ {u} \mathbb {E} \left[ \int_ {0} ^ {\infty} e ^ {- \rho t} (\eta S (t) - u ^ {2}) d t \right]
$$

$$
\mathrm{subjectto} \qquad d S (t) = [ \beta (x (t) - \mu) + \theta p (t) + \tau q (t) + \gamma \pmb {\psi} ] d t + g _ {s} d Z (t)
$$

$$
d x (t) = \left[ u \sqrt {b - x (t)} - k (x (t) - a) \right] d t + g _ {x} d W (t)\tag{\((A - 1)\}
$$

where ?? is the control effort in the form of a response strategy, ??(??) is a tour’s sales at time $t , x ( t )$ is its ratings at time $t , p ( t )$ is its price at time $t , q ( t )$ is the quality at time ??, and ?? presents the vector of time-invariant tour features. In addition, ?? (??) is the lower (upper) bound of ??(??). We use the general form $g _ { s } \left( g _ { x } \right)$ to present the coefficient of the diffusion term in the sales (rating) equation. For example, $g _ { s }$ can be $\sigma , \sigma \sqrt { S ( t ) } , \mathrm { o r } \sigma S ( t ) ; g _ { x }$ can be $\zeta , \zeta \sqrt { \big ( b - x ( t ) \big ) ( x ( t ) - a ) } , \mathrm { o r } \zeta \big ( b - x ( t ) \big ) ( x ( t ) - a )$ . The optimal control and value function do not depend on the functional forms in the diffusion terms, as shown later.

To solve the stochastic optimal control problem, the optimal control ?? should satisfy the following Hamilton-Jacobi-Bellman equation:

$$
\begin{array}{r} \rho V (S (t), x (t), p (t), q (t), \pmb {\psi}) = \underset {u} {m a x} \{(\eta S (t) - u ^ {2}) + V _ {s} [ \beta (x (t) - \mu) + \theta p (t) + \tau q (t) + \pmb {\gamma} \pmb {\psi} ] \\ + V _ {x} [ u \sqrt {b - x (t)} - k (x (t) - a) ] + \frac {1}{2} V _ {s s} g _ {s} ^ {2} + \frac {1}{2} V _ {x x} g _ {x} ^ {2} \}. \end{array}\tag{\((A - 2)\}
$$

Since we assume $d Z ( t )$ and $d W ( t )$ are uncorrelated and therefore $d Z ( t ) d W ( t ) = 0$ , we have removed the interaction term from Equation $( \mathsf { A } \cdot 2 )$ . Taking the first-order condition with respect to ??, we solve the optimal control as

$$
u ^ {*} = \frac {V _ {x} \sqrt {b - x (t)}}{2}.
$$

Let $V ( S , x )$ denote the value function for the problem, i.e., $V ( S , x )$ is the expected value of the discounted profits from time ?? to infinity, when $S ( t ) = S , x ( t ) = x ,$ , and the optimal policy $u ^ { * }$ is followed from time ?? onwards. Note that $T = \infty$ , the future looks the same from any time ??, and therefore the value function does not depend on ??. We use the mean values of $p ( t )$ and $q ( t )$ , denoted as ?? and ??, respectively, to enable a steady-state analysis. The object ?? is a vector of time-invariant variables. We define the steady-state value function as $V ( S , x )$ . We try a value function following a linear form, $V ( S , x ) = \lambda _ { 1 } S + \lambda _ { 2 } x + \lambda _ { 0 } ,$ , where $\lambda _ { 1 } > 0$ and $\lambda _ { 2 } > 0$ . Next, we derive the expressions of $\lambda _ { 1 } , \lambda _ { 2 } ,$ and $\lambda _ { 0 }$ in terms of parameters defined in the model. The partial derivatives of the value function with respect to the state variables are $V _ { s } =$ $\lambda _ { 1 } , V _ { x } = \lambda _ { 2 } , V _ { s s } = 0$ , and $V _ { x x } = 0$ . Substituting $u ^ { * } , V _ { s } , V _ { x } , V _ { s s }$ , and $V _ { x x }$ into Equation $( \mathbf { A } { - } 2 ) .$ , we obtain the following:

$$
\begin{array}{c} \rho V (S, x) = \left[ \eta S - \frac {(V _ {x}) ^ {2} (b - x)}{4} \right] + V _ {s} [ \beta (x - \mu) + \theta p + \tau q + \pmb {\gamma} \pmb {\psi} ] + V _ {x} \left[ \frac {V _ {x} (\sqrt {b - x}) ^ {2}}{2} - k (x - a) \right] \\ = \eta S + \left(- \frac {(\lambda_ {2}) ^ {2}}{4} + \lambda_ {1} \beta - \lambda_ {2} k\right) x - \lambda_ {1} (\beta \mu - \theta p - \tau q - \pmb {\gamma} \pmb {\psi}) + \frac {(\lambda_ {2}) ^ {2} b}{4} + \lambda_ {2} k a \end{array}
$$

To summarize, we have the following:

$$
\rho V (S, x) = \rho \lambda_ {1} S + \rho \lambda_ {2} x + \rho \lambda_ {0} = \eta S + \left(- \frac {(\lambda_ {2}) ^ {2}}{4} + \lambda_ {1} \beta - \lambda_ {2} k\right) x - \lambda_ {1} (\beta \mu - \theta p - \tau q - \pmb {\gamma} \pmb {\psi}) + \frac {(\lambda_ {2}) ^ {2} b}{4} + \lambda_ {2} k a
$$

The above equation should hold no matter what the (initial) values of $S$ and ?? are, so we have the following:

$$
\rho \lambda_ {1} = \eta\tag{\((A - 3a)\}
$$

$$
\rho \lambda_ {2} = - \frac {(\lambda_ {2}) ^ {2}}{4} + \lambda_ {1} \beta - \lambda_ {2} k\tag{\((A - 3b)\}
$$

$$
\rho \lambda_ {0} = - \lambda_ {1} (\beta \mu - \theta p - \tau q - \pmb {\gamma} \pmb {\psi}) + \frac {(\lambda_ {2}) ^ {2} b}{4} + \lambda_ {2} k a\tag{\((A - 3c)\}
$$

Solving the above three equations (taking the positive root for $\lambda _ { 2 } )$ , we obtain the following:

$$
\lambda_ {1} = \frac {\eta}{\rho}\tag{A - 4a}
$$

$$
\lambda_ {2} = 2 \sqrt {(\rho + k) ^ {2} + \frac {\eta \beta}{\rho}} - 2 (\rho + k)\tag{\((A - 4b)\}
$$

$$
\lambda_ {0} = \frac {- \eta \beta \mu + \eta (\theta p + \tau q + \gamma \pmb {\psi})}{\rho^ {2}} + \frac {b}{\rho} \Bigl (\frac {\eta \beta}{\rho} - 2 (\rho + k) A + 2 (\rho + k) ^ {2} \Bigr) + 2 (A - \rho - k) k a\tag{\((A - 4c)\}
$$

where $A = \sqrt { ( \rho + k ) ^ { 2 } + \frac { \eta \beta } { \rho } } .$

Therefore, the optimal control is

$$
u ^ {*} = \frac {\lambda_ {2} \sqrt {b - x (t)}}{2} = \alpha \sqrt {b - x (t)},
$$

where $\begin{array} { r } { \alpha = \sqrt { ( \rho + k ) ^ { 2 } + \frac { \eta \beta } { \rho } } - ( \rho + k ) } \end{array}$

Substituting Equation (A-4) into the value function $V ( S , x )$ , we obtain the optimal value function $V ( S , x )$ as follows:

$$
\begin{array}{c} V (S, x) = \lambda_ {1} S + \lambda_ {2} x + \lambda_ {0} = \frac {\eta}{\rho} S + 2 (A - \rho - k) x - \frac {\eta \beta \mu}{\rho^ {2}} + \frac {\eta (\theta p + \tau q + \pmb {\gamma} \pmb {\psi})}{\rho^ {2}} \\ + \frac {b}{\rho} \Bigl (\frac {\eta \beta}{\rho} - 2 (\rho + k) A + 2 (\rho + k) ^ {2} \Bigr) + 2 k a (A - \rho - k) \end{array}\tag{A - 5}
$$

where $A = \sqrt { ( \rho + k ) ^ { 2 } + \frac { \eta \beta } { \rho } } .$ ∎

## Appendix B

## Marginal Impact of Parameters

In this part, we derive the impact of parameters on a tour’s steady-state mean, control effort, and value function. For notational simplicity, we again suppress a tour-specific subscript ?? to avoid clutter.

## The Impact of Parameters on the Steady-State Mean

After plugging $u ^ { * }$ into the rating equation, we have

$$
d x (t) = \bigl (\alpha (b - x (t)) - k x (t) + k a \bigr) d t + \zeta \sqrt {(b - x (t)) (x (t) - a)} d W (t).
$$

The drift term of the above equation can be reorganized as $\begin{array} { r } { ( \alpha + k ) \left( \frac { ( \alpha b + k a ) } { ( \alpha + k ) } - x ( t ) \right) = \lambda \big ( \nu - x ( t ) \big ) } \end{array}$ . For notational simplicity, we define $\begin{array} { r } { \lambda = \alpha + k \ = \ A - \rho \ \mathrm { a n d } \nu = { \frac { ( \alpha b + k a ) } { ( \alpha + k ) } } = { \frac { ( A - \rho - k ) b + k a } { A - \rho } } . } \end{array}$

A tour’s steady-state mean is given by

$$
\nu = \frac {(A - \rho - k) b + k a}{(A - \rho)} = \frac {(A - \rho) b - k (b - a)}{(A - \rho)},
$$

where $A = \sqrt { ( \rho + k ) ^ { 2 } + \frac { \eta \beta } { \rho } }$

The partial derivative of ν with respect to ?? $\begin{array} { r } { \mathrm { i s } \frac { \partial \nu } { \partial \eta } = \frac { k ( b - a ) A _ { \eta } ^ { \prime } } { ( A - \rho ) ^ { 2 } } . } \end{array}$ , where $\begin{array} { r } { A _ { \eta } ^ { \prime } = \frac { \beta } { 2 \rho \sqrt { ( \rho + k ) ^ { 2 } + \frac { \eta \beta } { \rho } } } . } \end{array}$ Thus, we $\mathrm { h a v e } \frac { \partial \nu } { \partial \eta } > 0 .$

The partial derivative of ν with respect to $\begin{array} { r } { \beta \mathrm { { i s } } { \frac { \partial \nu } { \partial \beta } } = { \frac { k ( b - a ) A _ { \beta } ^ { \prime } } { ( A - \rho ) ^ { 2 } } } , } \end{array}$ where $\begin{array} { r } { A _ { \beta } ^ { \prime } = \frac { \eta } { 2 \rho \sqrt { ( \rho + k ) ^ { 2 } + \frac { \eta \beta } { \rho } } } . } \end{array}$ Thus, we have $\begin{array} { r } { \frac { \partial \nu } { \partial \beta } > 0 } \end{array}$

The partial derivative of ν with respect to ?? i $\begin{array} { r } { \frac { \partial v } { \partial k } = - \frac { \left( A - \rho - k A _ { k } ^ { \prime } \right) \left( b - a \right) } { ( A - \rho ) ^ { 2 } } , } \end{array}$ , where $\begin{array} { r } { A _ { k } ^ { \prime } = \frac { ( \rho + k ) } { \sqrt { ( \rho + k ) ^ { 2 } + \frac { \eta \beta } { \rho } } } . } \end{array}$ Since $0 < A _ { k } ^ { \prime } < 1$ , we have $\begin{array} { r } { \frac { \partial \nu } { \partial k } < 0 } \end{array}$ . ∎

## The Impact of Parameters on the Control Effort in a Steady State

A tour’s optimal control in the steady state is

$$
u ^ {*} = \alpha \sqrt {b - \nu} = (A - \rho - k) \sqrt {\frac {k (b - a)}{A - \rho}},
$$

where $A = \sqrt { ( \rho + k ) ^ { 2 } + \frac { \eta \beta } { \rho } } .$

The derivative of $u ^ { * }$ with respect to ?? is $\begin{array} { r } { \frac { \partial u ^ { * } } { \partial \eta } = A _ { \eta } ^ { \prime } \sqrt { \frac { k ( b - a ) } { A - \rho } } + ( A - \rho - k ) \frac { - k ( b - a ) A _ { \eta } ^ { \prime } } { 2 ( A - \rho ) ^ { 2 } \sqrt { \frac { k ( b - a ) } { A - \rho } } } = A _ { \eta } ^ { \prime } \sqrt { \frac { k ( b - a ) } { A - \rho } } \Big ( 1 - \frac { ( A - \rho - k ) } { 2 ( A - \rho ) } \Big ) } \end{array}$ . The expression of $A _ { \eta } ^ { \prime }$ is defined previously. We have $\frac { \partial u ^ { * } } { \partial \eta } > 0$

Similarly, the derivative of $u ^ { * }$ with respect to $\beta$ is $\begin{array} { r } { \frac { \partial u ^ { * } } { \partial \beta } = A _ { \beta } ^ { \prime } \sqrt { \frac { k ( b - a ) } { A - \rho } } \Big ( 1 - \frac { ( A - \rho - k ) } { 2 ( A - \rho ) } \Big ) } \end{array}$ . The expression of $A _ { \beta } ^ { \prime }$ is defined previously. We have $\frac { \partial u ^ { * } } { \partial \beta } > 0 .$

The derivative of $u ^ { * }$ with respect to ?? is as follows:

$$
\begin{array}{l} \frac {\partial u ^ {*}}{\partial k} = (A _ {k} ^ {\prime} - 1) \sqrt {\frac {k (b - a)}{A - \rho}} + (A - \rho - k) \frac {(b - a) \frac {(A - \rho) - k A _ {k} ^ {\prime}}{(A - \rho) ^ {2}}}{2 \sqrt {\frac {k (b - a)}{A - \rho}}} = \left((A _ {k} ^ {\prime} - 1) + (A - \rho - k) \frac {(b - a) \frac {(A - \rho) - k A _ {k} ^ {\prime}}{(A - \rho) ^ {2}}}{2 \frac {k (b - a)}{A - \rho}}\right) \sqrt {\frac {k (b - a)}{A - \rho}} \\ = \left((A _ {k} ^ {\prime} - 1) + (A - \rho - k) \frac {\frac {(A - \rho) - k A _ {k} ^ {\prime}}{(A - \rho)}}{2 k}\right) \sqrt {\frac {k (b - a)}{A - \rho}} \end{array}
$$

The expression of $A _ { k } ^ { \prime }$ is defined previously.

## The impact of Parameters on the Value Function (Profit)

In the steady state, a tour’s value function is as follows:

$$
\begin{array}{l} V (S, x) = \frac {\eta}{\rho} S + 2 (A - \rho - k) x - \frac {\eta \beta \mu}{\rho^ {2}} + \frac {\eta (\theta p + \tau q + \boldsymbol {\gamma} \boldsymbol {\psi})}{\rho^ {2}} \\ \qquad + \frac {b}{\rho} \Big (\frac {\eta \beta}{\rho} - 2 (\rho + k) A + 2 (\rho + k) ^ {2} \Big) + 2 k a (A - \rho - k), \end{array}
$$

where $A = \sqrt { ( \rho + k ) ^ { 2 } + \frac { \eta \beta } { \rho } } .$

The partial derivative of the value function with respect to ?? is as follows:

$$
\frac {\partial V}{\partial \eta} = \frac {S}{\rho} + 2 x A _ {\eta} ^ {\prime} - \frac {\beta \mu}{\rho^ {2}} + \frac {(\theta p + \tau q + \pmb {\gamma} \pmb {\psi})}{\rho^ {2}} + \frac {b}{\rho} \Big [ \frac {\beta}{\rho} - 2 (\rho + k) A _ {\eta} ^ {\prime} \Big ] + 2 k a A _ {\eta} ^ {\prime}
$$

The expression of $A _ { \mathfrak { \eta } } ^ { \prime }$ is defined previously.

The partial derivative of the value function with respect to $\beta$ is as follows:

$$
\frac {\partial V}{\partial \beta} = 2 x A _ {\beta} ^ {\prime} - \frac {\eta \mu}{\rho^ {2}} + \frac {b}{\rho} \left[ \frac {\eta}{\rho} - 2 (\rho + k) A _ {\beta} ^ {\prime} \right] + 2 k a A _ {\beta} ^ {\prime}
$$

The expression of $A _ { \beta } ^ { \prime }$ is defined previously.

The partial derivative of the value function with respect to $k$ is as follows:

$$
\frac {\partial V}{\partial k} = 2 x (A _ {k} ^ {\prime} - 1) + \frac {b}{\rho} [ - 2 (\rho + k) A _ {k} ^ {\prime} - 2 A + 4 (\rho + k) ] + 2 a (A - \rho - k) + 2 a k (A _ {k} ^ {\prime} - 1)
$$

The expression of $A _ { k } ^ { \prime }$ is defined previously.

## Appendix C

## Different Functional Forms in the Diffusion Terms

We tried different functional forms in diffusion terms. For the rating and sales equation, we considered three different function forms for each: constant, concave, and linear. For the concave and linear forms, the variation of the stochastic term depends on the value of the state variable at t (e.g., ?? (??) or ?? (??)). The intuition behind the square root term in the stochastic term is that the square root term diminishes more slowly than a linear structure, thereby implying that the stochastic term continues to have a material impact even as it approaches zero (e.g., $S _ { i } ( t )$ approaches zero). Since we estimate the sales and rating equations jointly, we considered the combination of different functional form in the sales and rating equations. Table C1 provides the log-likelihood values for different functional forms on Market I and II separately. For the rating and sales equations, the square root term fits the data best based on the log-likelihood values.

<table><tr><td colspan="4">Table C1. Log-Likelihood Values with Different Specifications in the Diffusion Terms</td></tr><tr><td colspan="4">Market I</td></tr><tr><td>Sales equation Rating equation</td><td> $σ_i dZ_i(t)$ </td><td> $σ_i\sqrt{S_i(t)}dZ_i(t)$ </td><td> $σ_i S_i(t)dZ_i(t)$ </td></tr><tr><td> $ζ_i dW_i(t)$ </td><td>-35603.7</td><td>-19476.4</td><td>-20092.2</td></tr><tr><td> $ζ_i\sqrt{(b - x_i(t))(x_i(t) - a)}dW_i(t)$ </td><td>-33723.0</td><td>-16166.7</td><td>-17157.3</td></tr><tr><td> $ζ_i(b - x_i(t))(x_i(t) - a)dW_i(t)$ </td><td>-41186.4</td><td>-24058.6</td><td>-24822.2</td></tr><tr><td colspan="4">Market II</td></tr><tr><td>Sales equation Rating equation</td><td> $σ_i dZ_i(t)$ </td><td> $σ_i\sqrt{S_i(t)}dZ_i(t)$ </td><td> $σ_i S_i(t)dZ_i(t)$ </td></tr><tr><td> $ζ_i dW_i(t)$ </td><td>-41084.9</td><td>-22296.2</td><td>-24777.4</td></tr><tr><td> $ζ_i\sqrt{(b - x_i(t))(x_i(t) - a)}dW_i(t)$ </td><td>-40448.3</td><td>-21651.6</td><td>-24180.6</td></tr><tr><td> $ζ_i(b - x_i(t))(x_i(t) - a)dW_i(t)$ </td><td>-54988.1</td><td>-36210.3</td><td>-38694.0</td></tr></table>

## Appendix D

## Predictive Performance

We compared the predictive performance between the SDE model and two predictive models for time series data. ARMA, which is a classic method used to model time series data, consists of an autoregressive part (a function of lagged dependent variable) and a moving average part (a function of lagged error terms) (Box et al., 2015). The model is denoted as $A R M A ( p , q )$ , where ?? is the order of the autoregressive part and ?? is the order of the moving average part. GARCH is an extension of Engle’s autoregressive conditional heteroscedasticity (ARCH) model for variance heteroscedasticity (Engle, 1982). The model is denoted as $G A R C H ( p , q )$ , where ?? is the GARCH coefficient associated with lagged variances and ?? is the ARCH coefficient associated with lagged squared innovations.

To compare different models, we evaluate the predictive performance with three metrics: root mean square error (RMSE), mean absolute error (MAE), and mean absolute percentage error (SMAPE). RMSE is calculated by $\begin{array} { r } { R M S E = \sqrt { \sum _ { t = 1 } ^ { n } \frac { ( \widehat { S } _ { t } - S _ { t } ) ^ { 2 } } { n } } , } \end{array}$ , MAE is computed as $M A E =$ $\scriptstyle \sum _ { t = 1 } ^ { n } { \frac { | { \widehat { S _ { t } } } - S _ { t } | } { n } }$ , and SMAPE is defined as $\begin{array} { r } { { S M A P E } = \frac { 1 0 0 \% } { n } \sum _ { t = 1 } ^ { n } \frac { \lvert \widehat { S _ { t } } - { S _ { t } } \rvert } { \lvert \widehat { S _ { t } } \rvert + \lvert S _ { t } \rvert } } \end{array}$ , where $\widehat { S } _ { t }$ is the predicted value of sales at time $t , S _ { t }$ is the observed value of sales at time ??, and ?? is the number of points.

For each tour, we used the first eight months as the in-sample and the last two months as the out-of-sample. First, we used an in-sample to train these models. For ARMA and GARCH, ?? and ?? were empirically determined from the data based on Bayesian information criterion (BIC) values for each tour. Next, we used the trained models to predict the out-of-sample. Table D1 presents the averages of out-of-sample metrics across all the tours in Market I and Market II for these three methods.

<table><tr><td colspan="4">Table D1. Results on Predictive Performance</td></tr><tr><td>Metric</td><td>SDE</td><td>ARMA</td><td>GARCH</td></tr><tr><td colspan="4">Market I</td></tr><tr><td>RMSE</td><td>4.185 (8.353)</td><td>3.537 (5.235)</td><td>13.715 (52.14)</td></tr><tr><td>MAE</td><td>3.089 (7.223)</td><td>2.757 (4.179)</td><td>9.279 (40.056)</td></tr><tr><td>SMAPE</td><td>0.297 (0.146)</td><td>0.326 (0.18)</td><td>0.297 (0.254)</td></tr><tr><td colspan="4">Market II</td></tr><tr><td>RMSE</td><td>4.133 (3.954)</td><td>3.498 (4.587)</td><td>6.445 (10.346)</td></tr><tr><td>MAE</td><td>3.063 (3.055)</td><td>2.729 (3.797)</td><td>4.285 (7.535)</td></tr><tr><td>SMAPE</td><td>0.325 (0.114)</td><td>0.322 (0.118)</td><td>0.295 (0.216)</td></tr></table>

Note: The standard deviation is reported in parentheses.

We conducted a paired t-test to examine whether the two sets of means (SDE versus ARMA and SDE versus GARCH) are significantly different. Table D2 shows the t-statistics and corresponding ??-values (reported in parentheses). The SDE model achieves superior or comparable predictive performance with these benchmark models when evaluated based upon predictive performance. However, the SDE model embeds the response strategy, which allowed us to conduct the “what-if” analysis and investigate the marginal impact of parameter on the optimal response strategy and further profit. That is, the SDE model we developed is prescriptive in nature, as opposed to the predictive models to which we made comparisons.

<table><tr><td colspan="3">Table D2. Paired T-Test Results</td></tr><tr><td>Metric</td><td>SDE versus ARMA</td><td>SDE versus GARCH</td></tr><tr><td colspan="3">Market I</td></tr><tr><td>RMSE</td><td>0.769 (0.443)</td><td>-2.112** (0.036)</td></tr><tr><td>MAE</td><td>0.465 (0.643)</td><td>-1.78* (0.076)</td></tr><tr><td>SMAPE</td><td>-1.466 (0.144)</td><td>-0.019 (0.985)</td></tr><tr><td colspan="3">Market II</td></tr><tr><td>RMSE</td><td>1.209 (0.228)</td><td>-2.408** (0.017)</td></tr><tr><td>MAE</td><td>0.791 (0.43)</td><td>-1.733* (0.084)</td></tr><tr><td>SMAPE</td><td>0.242 (0.809)</td><td>1.414 (0.159)</td></tr></table>

Note: The ??-value is reported in parentheses. \*\*\* ?? < 0.01; \*\* ?? < 0.05; \* ?? < 0.1.

## Appendix E

## Alternative Response Strategy Based on Composite State Variable

In our main model, the state variable is constructed using customer review ratings. Thus, the firm’s response strategy depends on the review rating. However, in practice, whether the firm decides to respond to customer reviews might likely depend on not only the review rating but also some other aspects of the reviews, for example, the negativity or specificity manifested in the review texts. That is, when the firm decides whether to respond, it may consider both the review rating and the review text, including how negative the tone of the review text is and how specific th review text is. Therefore, in this appendix, we extend our model by incorporating additional information to guide the response strategy.

The state variable $\chi _ { i } ( t )$ is now a composite variable composed of the review rating $x _ { i } ( t )$ , the review negativity $y _ { i } ( t )$ , and the review specificity $z _ { i } ( t )$ from tour ??. We simply choose equal weight (i.e., $w _ { 1 } = w _ { 2 } = w _ { 3 } = 1 / 3 )$ for each component to illustrate.<sup>21</sup> That is,

$$
\chi_ {i} (t) = w _ {1} x _ {i} (t) + w _ {2} y _ {i} (t) + w _ {3} z _ {i} (t).
$$

Replacing $x _ { i } ( t )$ with the composite state variable $\chi _ { i } ( t )$ , we obtain the stochastic optimal control problem of tour ?? as follows:

$$
\max _ {u _ {i}} \mathbb {E} \left[ \int_ {0} ^ {\infty} e ^ {- \rho t} \big (\eta_ {i} S _ {i} (t) - u _ {i} ^ {2} \big) d t \right]
$$

$$
\mathrm{subjectto} d S _ {i} (t) = [ \beta_ {i} (\chi_ {i} (t) - \mu) + \theta_ {i} p _ {i} (t) + \tau_ {i} q _ {i} (t) + \pmb {\gamma} _ {i} \pmb {\psi} _ {i} ] d t + g _ {i, s} d Z _ {i} (t)
$$

$$
d \chi_ {i} (t) = \left[ u _ {i} \sqrt {b - \chi_ {i} (t)} - k _ {i} (\chi_ {i} (t) - a) \right] d t + g _ {i, x} d W _ {i} (t)\tag{E-1}
$$

After solving the above optimization problem, the optimal control and value function are similar to the solutions of the main model. The onl difference is that we replaced the single-dimensional state variable $x _ { i }$ with the composite state variable $\chi _ { i } .$ Therefore, the model estimation procedures remain the same. Next, we elaborate how we constructed the review negativity and specificity using the data.

We used Baidu’s state-of-the-art machine learning tool for natural language processing (NLP) tasks. The API enabled us to extract all the entities mentioned in a review text and assign a probability of having a negative tone. Hence, for each review text, we were able to extract the number of entities and the probability of being negative. The larger the number of entities in a review text, the more concrete terms (specificity) are mentioned out of it. Hence, we used the number of entities to capture the review specificity and the probability of negative tone in a review text to capture the review negativity. Figure E1(a) shows the histogram of the number of entities (review specificity), and Figure E1(b) shows the histogram of the probability of being negative (review negativity); both are extracted from the review texts of all the tours.

To summarize, state $x _ { i } ( t )$ was constructed by averaging the ratings of the last 10 reviews of tour ?? by time ??, state $y _ { i } ( t )$ was constructed by averaging the negativity of the last 10 reviews of tour ?? by time ??, and state $z _ { i } ( t )$ was constructed by averaging the specificity of the last 10 reviews of tour ?? by time ??. The higher the value of review negativity, the worse the online reputation. Therefore, we transformed the negativity value by letting it be one minus the original value. Finally, we normalized the negativity and specificity scores from 1 to 5 to be consistent with the scale used for ratings. The composite state variable $\chi _ { i } ( t )$ at time ?? is constructed by taking the average of $x _ { i } ( t ) , y _ { i } ( t )$ , and $z _ { i } ( t )$ at time ??. The upper bound of $\chi _ { i } ( t )$ is 5, and its lower bound is 1.

We then replaced review ratings with this composite state variable (online reputation) in our controlled diffusion model and solved the optimal response strategy. After plugging the optimal response strategy into the composite state variable equation, we obtained a mean-reverting process of $\chi _ { i } ( t )$ . We estimated the tour-specific parameters of all the tours in each market following the estimation steps described in the Model Estimation and Identification section. Here, we again used tour 78266 to illustrate the response strategy under the composite state variable. Figure E2 plots the observed response strategy and the (theoretical) optimal response strategy based on the composite state variable. We see that the theoretical optimal response strategy, based on the composite state variable, does not match the observed strategy for this specific tour. On the other hand, the observed response strategy has a better fit with the theoretical, single-dimensional response strategy (see Figure 4b). This suggests that this tour manager might be focusing on ratings when responding to customers. Do tour managers focus not only on ratings but also review texts to determine their response? Next, we discuss and compare the response strategy based on ratings and other review aspects.

![](/api/attachments/MZR5VZQM/fulltext/images/3371f59eae10794ca94f62a26197fed8971d660cc9e4cefd5900a526559dd2ec.jpg)  
Figure E1. The Histograms of Review Negativity and Specificity

![](/api/attachments/MZR5VZQM/fulltext/images/5fbbed00228eaabc6101aa6361268d200c82506484c521886f55a4bab85916eb.jpg)

![](/api/attachments/MZR5VZQM/fulltext/images/b897f6c971ced8eeff05bb89a7d32550eeaa22dcb5f15d5b49c41afc7438ab0c.jpg)

We first ran a logistic regression for each tour and examined whether the review rating, review negativity and review specificity were significant factors in determining the response strategy. If only the rating variable was significant, we labeled the tour adopting a single dimensional strategy (control group). If all coefficients were significant, we labeled the tour adopting a multidimensional strategy (treatment group). There were 34 tours in the treatment group and 212 tours in the control group. We then explored the impact of the response strategy (single or multidimensional) on the states of review rating, review negativity, and review specificity. We used propensity score matching (PSM) to match tours based on tour characteristics (??????????????????????, ????????????????, ????????, ????????????????????????????, and ??????????). A probit model was used to determine the propensity scores. We employed nearest-neighbor matching with replacement in the matching treatment and contro tours. We focused on those pairs where one tour adopts a multidimensional strategy (treatment) and the other adopts a single-dimensional strategy (control). For each tour, we considered three outcomes of a response strategy—namely, mean state of review rating, mean state of review negativity, and mean state of review specificity. For ease of comparison, the state of review negativity was first transformed from 1 minus the original negativity value, and the states of review negativity and review specificity were normalized into a value from 1 to 5, consistent with the scale used for rating. Therefore, the higher the state value is, the better the online reputation is.

Table E1 shows the average treatment effect for each outcome. While the single-dimensional strategy performs better than the multidimensional strategy in terms of the review rating, the multidimensional strategy does better on the review negativity and review specificity than the single-dimensional strategy. Thus, neither strategy dominates. We observe that under the single-dimensional response strategy, firms achieve better performance on mean rating than that under the multidimensional response strategy. This is because firms only consider ratings in their objective function, and therefore, the optimal effort only depends on the ratings. On the other hand, under the multidimensional strategy, firms not only consider ratings but also review negativity and specificity in their objective function, and all three determine the optimal response effort. Therefore, we see that firms achieve better performance on negativity and specificity under the multidimensional strategy than under the single-dimensional strategy. An analogy would be a scenario where a student only puts effort into improving her mathematics score (Scenario I) versus another scenario where the student puts effort into improving her mathematics, chemistry, and physics scores (Scenario II). It is likely that the student would obtain a higher mathematics score in Scenario I than in Scenario II but lower chemistry and physics scores in Scenario I than in Scenario II.

To summarize, our model framework enables us to study different response strategies in order to choose the one that best fits a firm’s management goals (focusing on single or multidimensional strategies). This multidimensional illustration provides insights that are more prescriptive as it factors in the nature of the review text. The above analyses also demonstrate the power and flexibility of the SDE approach.

<table><tr><td colspan="6">Table E1. Performance of Single-Dimensional Strategy and Multidimensional Strategy</td></tr><tr><td>Outcome</td><td>Multidimensional strategy</td><td>Single-dimensional strategy</td><td>Difference</td><td>Standard error</td><td>T-statistic</td></tr><tr><td>Mean state of review rating</td><td>4.463</td><td>4.567</td><td>-0.103</td><td>0.031</td><td>-3.38</td></tr><tr><td>Mean state of review negativity</td><td>1.876</td><td>1.725</td><td>0.15</td><td>0.048</td><td>3.15</td></tr><tr><td>Mean state of review specificity</td><td>1.973</td><td>1.823</td><td>0.151</td><td>0.044</td><td>3.42</td></tr></table>

## Appendix F

## Using Different Window Sizes to Construct the State Variable

In this appendix, we examine an alternative window size by constructing the state variable $x _ { i } ( t )$ using the recent 20 reviews. Table F1 reports the estimation results of the data using a window size equal to 20. Our main results qualitatively hold. While there is no doubt that the average of overall ratings is important, there is ample evidence that potential customers also rely on and read specific reviews when making their purchase decisions. Prior studies have found that customers rarely examine reviews beyond the first webpage, while none of them read reviews beyond the first two webpages (Pavlou & Dimoka, 2006). At Ctrip.com, each page shows 10 customer reviews. This supports why we use an average rating of 10 reviews or 20 reviews to define the state variable ?? (??) in our analyses. Another main reason why we use the recent ?? ratings rather than the overall review rating is that the latter is cumulative over the entire history of reviews (up to the current time). This makes the overall rating a poor candidate for the SDE model when the number of reviews is large because there would be not much variance in the overall rating during a short period of time. For example, for 54% of tours, their variations of the overall ratings (keeping one decimal digit, consistent with what was shown on each tour’s webpage) are close to zero when the number of accumulated reviews is greater than 100. SDE works when there is substantial change in the state over time.

Table F1. Estimation Results with a Window Size of 20

<table><tr><td colspan="8">Market I</td></tr><tr><td>Tour ID</td><td> $\eta_i$ </td><td> $\beta_i$ </td><td> $k_i$ </td><td> $\mu$ </td><td> $\sigma_i$ </td><td> $\zeta_i$ </td><td> $v_i$ </td></tr><tr><td>29336</td><td>3.486***(1.39)</td><td>7.229*(4.613)</td><td>2.027***(0.296)</td><td>4.5***(0.112)</td><td>4.286***(0.166)</td><td>0.92***(0.027)</td><td>4.640</td></tr><tr><td>70550</td><td>0.281***(0.004)</td><td>6.065*(3.914)</td><td>0.408**(0.203)</td><td>4.5***(0.025)</td><td>2.097***(0.109)</td><td>0.18***(0.003)</td><td>4.719</td></tr><tr><td>94243</td><td>0.384***(0.01)</td><td>0.99**(0.452)</td><td>0.31*(0.195)</td><td>4.5***(0.072)</td><td>1***(0.019)</td><td>0.195***(0.004)</td><td>4.547</td></tr><tr><td>16311</td><td>3.966**(2.173)</td><td>8.076***(2.27)</td><td>2.999***(0.742)</td><td>4.5***(0.048)</td><td>3.056***(0.152)</td><td>0.886***(0.025)</td><td>4.529</td></tr><tr><td>1621699</td><td>1.274***(0.027)</td><td>2.462**(1.217)</td><td>0.719***(0.216)</td><td>4.5***(0.028)</td><td>0.965***(0.019)</td><td>0.41***(0.009)</td><td>4.636</td></tr><tr><td>1611924</td><td>1.959*(1.281)</td><td>2.061**(1.222)</td><td>1.953***(0.483)</td><td>4.5***(0.024)</td><td>0.739***(0.017)</td><td>0.281***(0.004)</td><td>4.147</td></tr><tr><td>63798</td><td>0.773***(0.011)</td><td>7.551**(4.032)</td><td>1.533**(0.776)</td><td>4.5***(0.048)</td><td>3.042***(0.135)</td><td>0.403***(0.011)</td><td>4.436</td></tr><tr><td>72603</td><td>1.697*(1.277)</td><td>4.16**(2.154)</td><td>2.083***(0.803)</td><td>4.5***(0.04)</td><td>1.974***(0.103)</td><td>0.237***(0.005)</td><td>4.307</td></tr><tr><td>53136</td><td>27.37**(14.405)</td><td>1.205***(0.256)</td><td>5.537***(1.357)</td><td>4.5***(0.073)</td><td>1.311***(0.027)</td><td>0.3***(0.008)</td><td>4.156</td></tr><tr><td>78266</td><td>15.165***(2.047)</td><td>1.038***(0.219)</td><td>1.135***(0.05)</td><td>4.5***(0.058)</td><td>1.195***(0.039)</td><td>0.983***(0.047)</td><td>4.744</td></tr><tr><td colspan="8">Market II</td></tr><tr><td>Tour ID</td><td> $\eta_i$ </td><td> $\beta_i$ </td><td> $k_i$ </td><td> $\mu$ </td><td> $\sigma_i$ </td><td> $\zeta_i$ </td><td> $v_i$ </td></tr><tr><td>64102</td><td>6.437*(3.903)</td><td>1.365***(0.58)</td><td>2.131***(0.646)</td><td>4.6***(0.114)</td><td>1.858***(0.067)</td><td>0.305***(0.007)</td><td>4.363</td></tr><tr><td>62460</td><td>0.176***(0.003)</td><td>4.496**(2.235)</td><td>0.596***(0.004)</td><td>4.6***(0.041)</td><td>2.579***(0.051)</td><td>0.186***(0.002)</td><td>4.401</td></tr><tr><td>79152</td><td>0.318***(0.008)</td><td>1.122***(0.352)</td><td>0.491***(0.006)</td><td>4.6***(0.121)</td><td>1.687***(0.051)</td><td>0.214***(0.004)</td><td>4.266</td></tr><tr><td>62904</td><td>1.443***(0.014)</td><td>4.271***(1.252)</td><td>1.588**(0.681)</td><td>4.6***(0.055)</td><td>2.546***(0.099)</td><td>0.286***(0.007)</td><td>4.431</td></tr><tr><td>53694</td><td>2.171***(0.021)</td><td>0.99*(0.727)</td><td>0.803*(0.573)</td><td>4.6***(0.068)</td><td>1***(0.015)</td><td>0.184***(0.004)</td><td>4.510</td></tr><tr><td>55173</td><td>0.278***(0.01)</td><td>3.757**(1.937)</td><td>0.372**(0.164)</td><td>4.6***(0.059)</td><td>2.554***(0.102)</td><td>0.394***(0.01)</td><td>4.672</td></tr><tr><td>72202</td><td>1.303***(0.033)</td><td>5.118**(2.274)</td><td>0.472***(0.178)</td><td>4.6***(0.048)</td><td>2.829***(0.109)</td><td>0.472***(0.01)</td><td>4.836</td></tr><tr><td>77480</td><td>2.813**(1.645)</td><td>0.946**(0.471)</td><td>0.355***(0.058)</td><td>4.6***(0.059)</td><td>0.843***(0.021)</td><td>0.489***(0.006)</td><td>4.804</td></tr><tr><td>29605</td><td>0.862***(0.014)</td><td>2.526**(1.122)</td><td>0.399**(0.183)</td><td>4.6***(0.056)</td><td>1.861***(0.083)</td><td>0.211***(0.004)</td><td>4.757</td></tr><tr><td>64358</td><td>4.777**(2.556)</td><td>0.99***(0.326)</td><td>0.501***(0.07)</td><td>4.6***(0.069)</td><td>1***(0.051)</td><td>0.127***(0.003)</td><td>4.793</td></tr></table>

Note: The estimation is based on the in-sample data for each tour. \*\*\* ?? < 0.01; \*\* ?? < 0.05; \* ?? < 0.1. The standard errors are reported in parentheses.

## Appendix G

## Incorporating the Latent Class Model into SDE

To address the unobserved heterogeneity, in this appendix, we propose a deterministic method in which each firm belongs to a fixed latent class irrespective of time that incorporates a latent class model (LCM) into SDE.

Tours are sorted into ?? different latent classes. For each class ??, the probability of assigning tour ?? to class ?? is modeled as

$$
H _ {i q} = \frac {\exp (Z _ {i} \beta_ {q})}{\sum_ {k = 1} ^ {Q} \exp (Z _ {i} \beta_ {k})},
$$

where $Z _ { i }$ is a vector of characteristics of tour ?? that could affect its latent class and $\beta _ { q }$ is the vector of coefficients corresponding to class ??. Note that $H _ { i q }$ is independent of time (?? is not part of the notation).

Tours classified into the same class share the same parameters in the SDE. The stochastic optimal control problem of tour ?? is as follows:

$$
\max _ {u _ {i}} E \left[ \int_ {0} ^ {\infty} e ^ {- \rho t} \big (\eta_ {q} S _ {i} (t) - u _ {i} ^ {2} \big) d t \right]
$$

subject to

$$
d S _ {i} (t) = \big (\beta_ {q} (x _ {i} (t) - \mu) + \theta_ {q} p _ {i} (t) + \tau_ {q} q _ {i} (t) \big) d t + \sigma_ {q} \sqrt {S _ {i} (t)} d Z _ {i} (t)
$$

$$
d x _ {i} (t) = \Big (u _ {i} \sqrt {b - x _ {i} (t)} - k _ {q} (x _ {i} (t) - a) \Big) d t + \zeta_ {q} \sqrt {(x _ {i} (t) - a) (b - x _ {i} (t))} d W _ {i} (t)\tag{G - 1}
$$

We remove the tour characteristics from the sales equation, as we have used them to construct the probability of latent class assignment. After solving the stochastic optimal control and plugging ??<sup>∗</sup> into the above state equations, we obtain the following:

$$
d S _ {i} (t) = \big (\beta_ {q} (x _ {i} (t) - \mu) + \theta_ {q} p _ {i} (t) + \tau_ {q} q _ {i} (t) \big) d t + \sigma_ {q} \sqrt {S _ {i} (t)} d Z _ {i} (t)\tag{G - 2a}
$$

$$
d x _ {i} (t) = \lambda_ {q} (\nu_ {q} - x _ {i} (t)) d t + \zeta_ {q} \sqrt {(b - x _ {i} (t)) (x _ {i} (t) - a)} d W _ {i} (t)\tag{G - 2b}
$$

The likelihood for tour ?? is

$$
P _ {i} = \sum_ {q = 1} ^ {Q} H _ {i q} f _ {q},
$$

where $f _ { q }$ is the likelihood of Equation (G-2) assuming that tour ?? is classified into class ??. Furthermore, the overall log-likelihood is

$$
\ln L = \sum_ {i = 1} ^ {N} \ln P _ {i},
$$

where ?? is the total number of tours. Here, the parameters are now class-specific instead of tour-specific. The steady-state mean $\nu _ { q }$ is also class-specific instead of tour-specific.
