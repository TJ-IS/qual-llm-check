---
otero_id: 4180
otero_key: "BV478HNE"
title: "Prescribing Response Strategies to Manage Customer Opinions: A Stochastic Differential Equation Approach"
authors: "Mingwen Yang; Zhiqiang (Eric) Zheng; Vijay Mookerjee"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2018.0805"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [139.184.14.150] On: 26 April 2019, At: 09:21 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/BV478HNE/fulltext/images/cb59b31c49e84e0c6d67949905f920f4acd5eff9aaccd941400f8345e7ea1e95.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Prescribing Response Strategies to Manage Customer Opinions: A Stochastic Differential Equation Approach

Mingwen Yang, Zhiqiang (Eric) Zheng, Vijay Mookerjee

To cite this article: Mingwen Yang, Zhiqiang (Eric) Zheng, Vijay Mookerjee (2019) Prescribing Response Strategies to Manage Customer Opinions: A Stochastic Differential Equation Approach. Information Systems Research

Published online in Articles in Advance 26 Apr 2019

https://doi.org/10.1287/isre.2018.0805

Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Prescribing Response Strategies to Manage Customer Opinions: A Stochastic Differential Equation Approach

Mingwen Yang,<sup>a</sup> Zhiqiang (Eric) Zheng,<sup>b</sup> Vijay Mookerjee<sup>b</sup>

<sup>a</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195; <sup>b</sup> Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080

Contact: mwyang.wendy@gmail.com (MY); ericz@utdallas.edu (ZEZ); vijaym@utdallas.edu, http://orcid.org/0000-0001-5583-3585 (VM)

Received: April 27, 2016 Revised: March 3, 2017; December 15, 2017; May 16, 2018 Accepted: June 20, 2018 Published Online in Articles in Advance: April 26, 2019

https://doi.org/10.1287/isre.2018.0805

Copyright: © 2019 INFORMS

Abstract. Today, the reputation of a firm is profoundly influenced by user opinions expressed in online consumer reviews. Managing these opinions is, therefore, critical for the success of firms. We study the problem of devising an appropriate opinion management strategy (or response strategy) for a firm to respond to online customer reviews. To unravel the underlying mechanics of the problem, we develop a stochastic differential equation model that describes the evolution of review ratings over time for a given response strategy employed by the firm. This model is validated using data on online customer reviews and firm responses from two of the world’s largest online travel agents. When pitted against popular benchmark models, such as autoregressive moving average, generalized autoregressive conditional heteroscedasticity, moving average, exponential smoothing, and naive method, our approach not only achieves comparable (often better) predictive performance, it is also able to incorporate the response strategy into the data-generation process underlying the review ratings. Our approach, therefore, is not just predictive, but, more importantly, one that can be used in a prescriptive sense, namely to prescribe a response strategy that controls review ratings in a desired manner. We operationalize the theoretical response strategy in our stochastic model to an operational prescription that a firm can implement and show the applicability of our approach for different business objectives, such as mean control, meanvariance control, and service-level control. Finally, we demonstrate the flexibility of the stochastic differential equation model by extending it to encompass multiple state variables.

History: Kai-Lung Hui, Senior Editor; Ahmed Abbasi, Associate Editor.

Funding: This research was partially supported by the Natural Science Foundation of China [Grant 71532004].

Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2018.0805.

Keywords: stochastic differential equation model • customer opinion management • response strategy

## 1. Introduction

In today’s online economy, customers are increasingly relying on online reviews, social media, and other forms of word of mouth (WOM) to form opinions on a product or service they intend to purchase. Of these sources, online reviews have been found to have a big impact on a firm’s reputation and revenue (Jabr and Zheng 2014). Marketers have observed that online reviews influence 90% of consumers in their perception and adoption of a product or service (Gesenhues 2013). The monetary consequences of review ratings on corporate reputation and profitability are significant. For example, Luca (2011) observes that a drop of one star in a rating on Yelp translates to a 5%–9% decrease of a restaurant’s revenue. On the positive side, an extra half-star rating causes restaurants to sell out during peak hours 49% more frequently with larger impacts when alternate information is scarcer (Anderson and Magruder 2012). In addition, Anderson and Han (2016) find that a one-star improvement in an online rating on TripAdvisor increases hotel revenue by 39%.

Negative reviews, in particular, play a more prom inent role (Chevalier and Mayzlin 2006). Firms, however, continue to struggle with methods to mitigate or counter the influence of negative reviews. One approach focuses on soliciting positive reviews, for example, by sending emails to encourage positive customers to post reviews after transactions. Because recent reviews are often dis played first and most customers only read the first few pages of online reviews, negative reviews get crowded out quickly among a large number of positive ones. Some review platforms allow firms to talk to customers off line to resolve their complaints so that they may revise their negative opinions (Banjo 2012). There are also some companies that actively discourage customers from posting negative reviews. However, as a hotel in New York found out, such a policy could backfire: negative sentiments flooded in afterward, causing the hotel’s rating to plummet down to one star with more than 100 negative reviews emerging on Yelp shortly after implementing the policy (DeMers 2014).

Companies also try to manipulate reviews by fabricating fake ones. It is reported that 10%–15% of online reviews are manipulated or fake, sponsored by companies (Gartner 2012). Mayzlin et al. (2014) found evidence that some firms manufacture positive reviews for themselves and negative reviews for their competitors. Although manipulated reviews could reward a firm in the short term, manipulation runs the risk of being seen through by consumers with dire consequences for the firm’s long-term reputation. The U.S. government has begun to stipulate tighter policies to regulate the online review environment (Rushe 2013). Firms that fabricate fake reviews will face severe penalties in the form of government fines, possibility of lawsuits, and loss of reputation. Online review platforms, such as Yelp, ensure the integrity of its reviews by filtering out illegitimate, fake reviews.

Many savvy firms have found that user opinions can be managed more effectively by publicly responding to reviews. Evidence suggests that a calibrated firm response is often an effective way to tackle negative reviews. It is reported that after seeing a carefully crafted response to a negative review, 71% of customers change their perception of the brand (Bazaarvoice 2013). Proserpio and Zervas (2017) find that hotels that actively respond to reviews receive an average increase of 0.12-star rating in TripAdvisor. Gu and Ye (2014) show that publicly responding to negative reviews not only addresses a particular customer’s concerns, but also helps limit the spillover of negative opinions to other customers.

Firm responses can affect future reviews in several ways. People are more likely to write negative reviews when their experience of a product or service is different (worse) than what they have experienced (Moe and Schweidel 2012, Ho et al. 2017). Moe and Schweidel (2012) observe sequential dependency among reviews that occurs because a review writer considers what other customers have experienced and reported on a matter before writing a review. Once a complaint has been reported by other customers and acknowledged by the firm, repeating the same complaint does not have much information value. Importantly, if customers were to voice a complaint on an issue that has already been raised and responded to, they would feel obliged to express their complaint differently—referred to as the “beg to differ” effect by Moe and Schweidel (2012).

Responding to reviews is also likely to decrease the occurrence of future negative reviews because consumers feel that their reviews will be closely scrutinized (Proserpio and Zervas 2017). That is, responding increases the “cost” of leaving a negative review, especially a flaky or unfounded one. For example, consumers with negative opinions need to justify their negative posts by providing sufficient details of their complaints, thus increasing the length of negative reviews (Proserpio and Zervas 2017). We elaborate further on how management responses influence future reviews in Section 3.1 and demonstrate it empirically in Section 4.2.

Our focus in this study is on the design of a response strategy to manage user opinions. A full response strategy—one that responds to every review—wil likely be either too costly or ineffective if the responses are not adequate. Thus, firms should respond in a selective manner, but when they do, the response must be adequate to resolve the customer’s problem. To unravel the mechanics of how review ratings evolve over time, we develop a stochastic differential equation (SDE) method to model the underlying review rating-generation process. This model captures how average ratings react to the arrival of new reviews as well as the firm’s response strategy.

In the SDE model, the stochastic variable of interest (or the state) is a measure of customer value proposition, that is, a customer’s perception of quality of a product or service at any given point in time.<sup>1</sup> The state is operationalized as the average of a certain number of recent ratings provided in customer reviews. The change in the state during a small time interval is decomposed into a deterministic component and a stochastic component. The deterministic component combines the firm’s response strategy and the influence of newly arrived reviews. The stochastic component consists of a random noise term that cannot be explicitly observed or explained. With some modifications, our proposed SDE model can be transformed into a form similar to the Cox–Ingersoll–Ross (CIR) model (Cox et al. 1985).

We solve our proposed SDE model to estimate the stochastic process of the state as a function of time and other primitives, including the firm’s response strategy. This stochastic process is validated empirically using data on online customer reviews and firm responses from two of the world largest travel agents. Compared with traditional time-series forecasting methods, such as autoregressive moving average (ARMA) (Box et al. 2015), generalized autoregressive conditional heteroscedasticity (GARCH) (Engle 1982), moving average (MA) (Brown 2004), exponential smoothing (ES) (Brown 2004), and naive method (NM), our approach achieves on-par or superior predictive performance.

However, the key strength of our approach is that it is able to recover the distribution of future review ratings as a function of the response strategy used by the firm. Our approach, therefore, is not just predictive, but also one that can be used in a prescriptive sense, namely to prescribe a response strategy that controls the rating-generation process in a desired manner. We map the theoretical control in the stochastic model to an operational prescription that a real firm can implement. We next demonstrate the use of our operational prescription to achieve different control objectives that managers may have to influence customer opinions as they evolve over time. Finally, we show how the SDE approach can be extended to encompass multistate variables. This further enhances the model’s prescriptive ability and adds new practical insights because it enables a firm’s response strategy to react to a change in multiple conditions (states).

## 2. Literature Review

We review literature in the problem domain being studied (customer opinion management) as well as the main methodology being used (stochastic differential equations).

## 2.1. Customer Opinion Management

There is abundant literature on customer opinions expressed through online reviews and the impact on product sales (Chevalier and Mayzlin 2006, Forman et al. 2008). However, there is relatively less attention paid to how customer opinions can be managed over time. Among the few studies on the subject of managing opinions, some researchers have investigated how customer opinions spread, that is, how one customer’s opinion could influence the opinion of subsequent customers (Moe and Schweidel 2012, Ho et al. 2017). Other researchers address the problem of online review manipulation, when firms act as customers and fabricate reviews to inflate their own reputation while damaging those of their competitors. Dellarocas (2006) and Mayzlin (2006) analytically model manipulation strategies used by firms. Mayzlin (2006) studies a firm’s incentives to generate anonymous promotional messages, yielding a unique equilibrium wherein firms with low-quality products engage in more promotional chat. Manipulation is documented in Anderson and Simester (2014), Mayzlin et al. (2014), and Luca and Zervas (2016). Mayzlin et al. (2014) compare ratings of 3,082 U.S. hotels on TripAdvisor.com with those on Expedia.com. They find that the magnitude of manipulation on Expedia.com is much lower than that on TripAdvisor.com because of the fact that Expedia, unlike TripAdvisor, requires users to have made an actual purchase before posting a review. Within the scope of opinion management, a small but growing stream of research has begun to examine how firms can mitigate the reputational harm of negative reviews, such as by inducing buyers to revoke negative feedback (Ye et al. 2014) or by instituting a reward-for-feedback mechanism (Li et al. 2016).

Our study considers a firm response mechanism that is different from the extant literature on review manipulation. In our setting, firms choose to directly respond to some customer reviews; the response is public and visible to everyone. Some papers attempt to address this phenomenon with emphases on studying whether a firm’s response affects subsequent review ratings (Gu and Ye 2014, Proserpio and Zervas 2017, Wang and Chaudhry 2018). Proserpio and Zervas (2017) examine the impact of responses on customer reviews by contrasting two hotel review platforms: one regularly responds, and the other does not. They find that the responding hotel reaped an average increase of 0.12 star in the ratings after starting to respond. Gu and Ye (2014) measure the impact of management responses on customer satisfaction and find that online management response is highly effective among lowsatisfaction customers but has limited influence on others. Wang and Chaudhry (2018) conduct a natural experiment to examine the influences of managers’ responses to negative reviews and observe an increase in customers’ stated satisfaction after receiving responses A recent study finds that responding to reviews could decrease future ratings because it might encourage more negative reviews (Chevalier et al. 2018). In such cases, the benefit of responding would be to satisfy the customer who wrote the review, but the downside of responding would be that it could attract new negative reviews. In such situations, that is, management response has two-sided effects, cost is not the only reason to limit the frequency of responding to reviews. Additionally, Gunarathne et al. (2018) find that how promptly a firm responds to a review is affected by the customer’s social influence (popularity) and sentiment toward the firm. Ma et al. (2015) analyze how a firm’s response (service intervention) changes individual customers’ decision to voice out (post a message on Twitter)

Some recent papers focus on teasing out the effect of management response on a firm’s financial performance (Lee et al. 2016, Kumar et al. 2019). Lee et al. (2016) observe that online WOM metrics, e.g., valence and volume, moderate the effect of management response on a hotel’s revenue; their findings suggest that hotels’ response strategy should factor in the level of online WOM metrics. Kumar et al. (2019) document the significant role of management response on the performance of the focal firm’s business as well as the performance of the nearby competitors’ businesses (i.e., the spillover effect).

Unlike the emphasis of previous work, our study focuses on the best response strategy to manage online ratings. We focus on to what review a firm should respond, thus addressing a gap raised in the literature (e.g., Proserpio and Zervas 2017). Our study is also related to the complaint management literature in marketing because responding to customer reviews can be regarded as a special type of a complaint-management (or defensive marketing) strategy. Fornell and Wernerfelt (1988) analyze incentives to manage complaints and characterize industries in which complaint management is likely to be used. They show that complaint management can lower the total marketing expenditure by substantially reducing the cost of advertising (offensive marketing).

To summarize, our study differs from the past research in terms of both the problem being solved and the research methodology being used. To our knowledge, this study represents one of the first attempts to prescribe an appropriate response strategy to manage user opinions. From a methodological perspective, we develop a stochastic differential equation model to prescribe the review data-generation process. In contrast, extant literature has resorted to either analytical modeling (e.g., Dellarocas 2006) or reduced-form empirical analysis (e.g., Gu and Ye 2014, Proserpio and Zervas 2017, Wang and Chaudhry 2018). A key distinction of our stochastic differential equation model is that we model the stochastic nature of the review data-generating process, namely, how review ratings evolve over time after accounting for the response strategy used by the firm.

## 2.2. Stochastic Differential Equations

In our paper, we develop an SDE model of the dynamics of review ratings in the presence of a response strategy used by the firm. SDE has been applied in finance to model the time series of stock price movements, with which randomness is inevitable. The wellknown Black–Scholes equation (Black and Scholes 1973), modeling the price of a European call option, uses the SDE methodology. A stochastic process $X _ { t } , t \geq 0$ , models a random variable of interest that varies continuously and stochastically through time. We model the stochastic rating process as a Markov process, in which the probability distribution of the future value depends only on its current value, which subsumes the effect of past values of the process. Randomness is captured by a Wiener process (the continuous limit of random walk), a fundamental building block for randomness in stochastic processes. A stochastic process $W _ { t } , t \geq 0$ , is defined to be a Wiener process if $W _ { 0 } = { \bar { 0 } } , W _ { t }$ has stationary and independent increments and $W _ { t }$ is normally distributed with mean zero and variance dt for every t (Ross 2014).

Geometric Brownian motion (GBM) is one of the classic SDE frameworks to model price movement in finance (Dixit et al. 1994). A stochastic process $X _ { t }$ is said to follow a GBM if it satisfies $d X _ { t } = \hat { b _ { 1 } } X _ { t } d t + b _ { 2 } X _ { t } d W _ { t } ,$ where $d X _ { t }$ is the incremental change in $X _ { t }$ and $W _ { t }$ is a Wiener process. In the GBM equation, the first term is used to model deterministic trends, referred to as the drift process with the parameter $b _ { 1 } ;$ the second term models randomness, referred to as the diffusion process with the parameter b . Often there are special characteristics of interest in time-series data, such as the mean-reversion property, which allows the state variable to fluctuate around one specific level (Dixit et al. 1994), for example, in the movement of stock prices (Poterba and Summers 1988). One of the simplest mean-reverting processes, called the Ornstein–

Uhlenbeck process, follows $d X _ { t } = \alpha ( \mu - X _ { t } ) d t + \sigma d W _ { t } ,$ where α is the speed of reversion and $\mu$ represents the mean level of X . If $X _ { t }$ is greater (less) than $\mu ,$ , it is more likely to fall (rise) over the next short interval of time. The discrete format for the continuous Ornstein-Uhlenbeck process is equivalent to the first-order autoregressive process AR(1) (Dixit et al. 1994). We use a stochastic process similar to the Ornstein–Uhlenbeck process in this study.

We next develop and operationalize the proposed SDE model of how review ratings evolve over time.

## 3. Stochastic Model of Review Ratings

In this section, we first provide a theoretical background for the impact of responses on reviews. Next, we present the SDE model for review ratings.

## 3.1. Theoretical Background

There is considerable evidence that responses help boost ratings as reported in the popular press and industry reports. For example, a TripAdvisor survey shows that 84% of users feel that appropriate management responses to negative reviews improve their impression of the hotel (TripAdvisor 2012). Another study by a global customer-experience management leader reports that hotels with the highest responsiveness to social media outperform competitors in their overall social reputation (Medallia 2015).

From a theoretical point of view, there are several ways that responses could impact ratings. In general, people are more likely to write negative reviews when their experience of a product or service is different (in this case, worse) than what they have experienced (Moe and Schweidel 2012, Ho et al. 2017). As shown in Moe and Schweidel (2012), a review writer often considers what other customers have reported on the matter before writing a review. Once a complaint has been reported by other customers (and acknowledged by the firm), there does not appear to be much information value in repeating the same complaint in the same manner. If customers were to voice a complaint on an issue that has already been raised and responded to, they would feel obliged to express their complaint differently than what previous reviewers have done. Additionally, customers would also feel the need to describe the complaint in more detail. We empirically verify these assertions in Section 4.2.

Thus, when a negative review arrives and gets responded to successfully, the impetus for a reviewer to write on the (same) negative issue is lowered or suppressed, leading to improved future ratings. We believe, therefore, that a response prevents or at least reduces negative spillovers. A firm’s response to a negative review reflects the firm’s willingness and intention to solve the problem, thus creating goodwil among other customers who might otherwise have written a negative review. Responses also enable the firm to clarify misunderstandings, apologize for mistakes, and explain causes of subpar service, thus curbing the spread of a negative event. Finally, responses allow the firm to resolve problems that other customers might encounter. Thus, responding helps curb future negative reviews and, hence, boosts ratings.

## 3.2. Model Description

We consider a typical online review setting, in which reviews and ratings arrive in a chronological sequence forming time-series data. At any point of time, we capture the notion of the state (consumers’ perception of product quality) as the moving average of the last n most recent ratings.<sup>2</sup> To model the stochastic nature of the ratings process, we use the moving average of recent ratings as the state variable of interest. Another choice could have been the cumulative average. However, the cumulative average hardly changes over time, making it a poor candidate to be a state variable. Consumers also deem recent reviews to be more relevant: according to a recent industry report (BrightLocal 2015), 44% of consumers maintain that a review must be written within one month to be relevant. Academic research also finds that the most recent reviews play a more important role in sales than cumulative ratings (Duan et al. 2008). For these reasons, we construct our state variable using the moving average of the most

In time-series data, a moving average is commonly used as a measure of the state (De Gooijer and Hyndman 2006). For example, a moving average of price measures how a stock is trending, whereas, in economics, moving average is commonly used to study gross domestic product, employment rates, and other macroeconomic variables (Brown 2004). In our setting, the state of the system is affected by the arrival of new reviews as well as responses the firm may provide to improve customer value proposition.

The goal in this section is to devise a model that captures the evolution, over time, of the state of the system (x<sub>t</sub>). To model the data-generating process, we start with a simplified microstructure: the change of the state $( d x _ { t } )$ in a small time interval from t to $t + d t$ . The change in the state consists of a deterministic component and a random component.

The deterministic component models the expected change (drift) in the state, $\mathbb { E } ( d x _ { t } )$ , as a function of the arrival of reviews and firm responses if any. We assume that the arrival of reviews follows a Poisson process with rate $\lambda . ^ { 4 }$ During a small time interval, the probability of arrival of one review is λdt. A review can be either negative or positive. Let $p$ (or $1 - p )$ be the probability that a review is negative (positive). The impact of a negative review on the state depends on a damage parameter $\beta$ and the current state of the system $x _ { t }$ . The negative impact is larger for higher values of $x _ { t } ,$ or conversely, when customers already had a low opinion, a negative review causes less damage. In the extreme case when $x _ { t } = 0 ,$ , there is no further damage. On the other hand, the impact of a positive review depends on a boost parameter $\rho$ and $\left( b - x _ { t } \right)$ , the difference between the highest possible quality perception b and the current state $x _ { t }$ . When the perception of quality is already high, a positive review does not boost it as much. In the extreme case when $x _ { t } = b ,$ there is no further gain possible of a positive review. The basic idea is that consumers’ perception of quality changes more when “new” information arrives. For a product or service that already has low quality in the eyes of consumers, another negative review will not diminish the perception by much; by the same token, when the quality perception is already high, it will not increase much if a new positive review arrives. For example, when a discount airline receives another complaint about its poor service, it will likely have less of an impact than when a premium airline is reported to have a case of bad service.

Finally, let the firm use a damage control effort of $\alpha$ associated with responding to reviews. The impact of this effort on the state is $\alpha ( b - x _ { t } )$ . When the perception of quality is high, the impact of damage control diminishes. Note that it is possible that management responses may incur a negative impact on future review ratings. That is, the sign of α could possibly be negative, and when it happens, this indicates that management response does not necessarily improve future ratings (in which case, the firm should simply stop responding). Taking together the impact of all the three driving forces (the impact of a positive review, the impact of a negative review, and the impact of damage control in the form of management responses) on $x _ { t } ,$ , we can write

$$
\mathbb {E} (d x _ {t}) = (\lambda (1 - p) \rho (b - x _ {t}) - \lambda p \beta x _ {t} + \alpha (b - x _ {t})) d t.
$$

Collecting the terms and rewriting, we get the form

$$
\mathbb {E} (d x _ {t}) = k _ {1} (k _ {2} - x _ {t}) d t,
$$

where k<sub>1</sub>k<sub>2</sub> ρλ 1  p b  αb and k<sub>1</sub> α  βλp $\rho \lambda ( 1 - p )$

The stochastic component (diffusion) of the change in perception of quality (dx ) is modeled as $\sigma { \sqrt { b - x _ { t } } } d W _ { t } .$ where $d W _ { t }$ is the Wiener process used to capture white noise or randomness; $d \bar { W } _ { t } \sim N ( 0 , d t )$ . The parameter σ influences the magnitude of the random component, and the term $\sqrt { b - x _ { t } }$ ensures the state variable does not exceed the upper bound, b. When the state variable touches $b ,$ the diffusion term dissolves. Square root processes are commonly used to model stochastic movements (Brown 2004). As $\left( b - x _ { t } \right)$ becomes very small, the square root term diminishes more slowly than a linear structure, implying that the stochastic component continues to have a material impact even as $x _ { t }$ approaches b. Also, the square root structure is one among the few SDE structures that lends itself to closedform solutions. Table 1 lists the parameters in our model. To summarize, we model the change in state using the following SDE:

$$
d x _ {t} = k _ {1} (k _ {2} - x _ {t}) d t + \sigma \sqrt {b - x _ {t}} d W _ {t}.\tag{1}
$$

Regarding Equation (1), in the long run (as $t \to \infty )$ , the steady-state mean is obtained by setting and solving $\mathbb { E } ( d x _ { t } ) = 0$ . Thus, the steady-state (long-run) mean of perception of quality (k<sub>2</sub>) is given by

$$
\mathbb {E} (x _ {t}) = k _ {2} = \frac {b}{1 + \frac {\beta \lambda p}{\alpha + \rho \lambda (1 - p)}}.\tag{2}
$$

It is clear that the steady-state mean increases with the damage-control effort α. Also, if no damage-control effort is exerted by the firm to counter negative reviews $( \alpha = 0 )$ , the steady-state mean is likely to go to zero when reviews are predominantly negative. That is, the steady-state mean will tend to zero if there is no damage-control effort $( \alpha = 0 )$ and the impact of negative reviews is much larger than that of positive ones $( \beta p \gg \rho ( 1 - p ) )$ . This negative trend in posted ratings over time is consistent with observations in the literature (Li and Hitt 2008, Moe and Schweidel 2012). Generally speaking, firms would like to keep the perception of quality at a high level and perhaps would also like its fluctuations to remain within a relatively small interval.

The SDE model in Equation (1) can be transformed into a standard form using the linear transformation $y _ { t } = b - x _ { t }$ . Then using Ito’s lemma on the function $F ( x _ { t } , \ t ) = b - x _ { t }$ , we get

$$
d y _ {t} = \frac {\partial F}{\partial t} d t + \frac {\partial F}{\partial x} d x _ {t} + \frac {1}{2} \frac {\partial^ {2} F}{\partial x ^ {2}} (d x _ {t}) ^ {2} = - d x _ {t}.
$$

Hence,

$$
\begin{array}{c} \mathbb {E} (d y _ {t}) = - \mathbb {E} (d x _ {t}) = - k _ {1} (k _ {2} - x _ {t}) d t = - k _ {1} (k _ {2} + y _ {t} - b) d t \\ = k _ {1} (k _ {3} - y _ {t}) d t. \end{array}\tag{3}
$$

In Equation $( 3 ) , k _ { 3 } = b - k _ { 2 }$ . Thus, the transformed SDE model becomes

$$
d y _ {t} = k _ {1} (k _ {3} - y _ {t}) d t + \sigma \sqrt {y _ {t}} d W _ {t}.\tag{4}
$$

Table 1. Notation

<table><tr><td>Parameter</td><td>Definition</td></tr><tr><td>λ</td><td>Review arrival rate</td></tr><tr><td>p</td><td>Probability of negative review</td></tr><tr><td>β</td><td>Damage parameter</td></tr><tr><td>ρ</td><td>Boost parameter</td></tr><tr><td>α</td><td>Damage control effort</td></tr><tr><td>σ</td><td>Magnitude of the random component</td></tr></table>

We can see that the structure of the SDE model in Equation (4) is in the form of the CIR model. Cox et al. (1985) noted that the distribution of y<sub>t</sub> given $y _ { u }$ for some $u < t \ \mathrm { i s } ,$ , up to a scale factor, a noncentral chi-squared distribution. The expectation and variance for $y _ { t }$ given the initial value $y _ { 0 }$ are

$$
\mathbb {E} (y _ {t} | y _ {0}) = y _ {0} e ^ {- k _ {1} t} + k _ {3} (1 - e ^ {- k _ {1} t}),\tag{5}
$$

$$
\mathbb {V} (y _ {t} | y _ {0}) = y _ {0} \frac {\sigma^ {2}}{k _ {1}} (e ^ {- k _ {1} t} - e ^ {- 2 k _ {1} t}) + \frac {k _ {3} \sigma^ {2}}{2 k _ {1}} (1 - e ^ {- k _ {1} t}) ^ {2}.\tag{6}
$$

The CIR process can also be represented as a sum of squared Ornstein–Uhlenbeck processes. This provides one way to derive the transition density of the CIR process. Readers can refer to Shreve (2004) for more details. In the model estimation section, we provide an explicit form of the transition density of the CIR process.

## 4. Exploratory Investigation of Data

In this section, we describe our data and the results of an exploratory investigation to provide supporting evidence of the positive effect of management response on future review ratings.

## 4.1. Data

Our main data source comes from Ctrip.com, the leading online travel agent aggregator in China, accounting for more than half of the market share in the online travel market. Ctrip offers a variety of tours (products), in which the travel agent provides tourism services, including itinerary planning, hotel accommo dation, transportation, guided tour service, etc. Customers book these tours and then post reviews at Ctrip.com. A snapshot of the page for reviewers to write reviews is presented in Online Appendix $^ { 6 , }$ in which the review rating is on the scale of one to five. These tours are offered by different travel agents, and Ctrip itself is the largest travel agent on Ctrip.com. A firm (travel agent) can only respond to customer reviews of its own tours. Figure 1 provides a browser-translated (Chrome) snapshot<sup>5</sup> of a sample customer review page from a Ctrip tour with responses to these reviews.

We obtained the data for 117 random tours from April 2012 to June 2014. The average number of reviews per tour is 528 with a minimum value of 92 and a maximum value of 7,035. Review ratings for most tours lie within a narrow range. For example, among the 117 tours in the Ctrip data, more than 90% of tours have an average rating between 4.2 and 4.8. Thus, in these data, a small numerical difference can be significant; for example, a 0.1 difference corresponds to a difference of more than 16% of the range. For each tour, we collected customer review information for each posting, including a unique identifier for the reviewer, review date, review rating (from one to five), and review text.

Figure 1. (Color online) Translated Snapshot of a Firm’s Response to Customer Reviews on Ctrip.com  
![](/api/attachments/BV478HNE/fulltext/images/5a099659c5df66306795ff684148cbe7fa4942b7a34d82b9a46aa90e73353606.jpg)

If the review received a response from the firm, we record the date of response and the text of the response. Table 2 presents the frequency distribution of review ratings.

The last column in Table 2 presents the fraction of customer reviews that received responses by the star-rating of the tours. As can be clearly seen, there is more response activity when the ratings are low, indicating that firms are selective with their use of a response. The last row in Table 2 provides the total number of responses, the total number of reviews, and the proportion of reviews receiving responses.

Table 2. Distribution of Review Ratings and the Fraction of Reviews with Responses

<table><tr><td>Review rating</td><td>Number of reviews</td><td>Percentage</td><td>Number of responses</td><td>Fraction with response</td></tr><tr><td>1</td><td>538</td><td>0.87%</td><td>242</td><td>44.98%</td></tr><tr><td>2</td><td>356</td><td>0.58%</td><td>165</td><td>46.35%</td></tr><tr><td>3</td><td>2,588</td><td>4.18%</td><td>433</td><td>16.73%</td></tr><tr><td>4</td><td>15,129</td><td>24.46%</td><td>749</td><td>4.95%</td></tr><tr><td>5</td><td>43,247</td><td>69.91%</td><td>336</td><td>0.78%</td></tr><tr><td>Total</td><td>61,858</td><td>100.00%</td><td>1,925</td><td>3.11%</td></tr></table>

Next, we label a review as negative or positive in a manner described as follows. If the rating associated with a newly arrived review is above a certain threshold, the review is considered positive and otherwise negative. Because the review ratings in this industry are generally high (above four), we choose a relatively high threshold: a rating is considered to be negative if it is less than or equal to four and positive otherwise.

Prior studies show that besides the review rating, potential customers heavily rely on the actual review text when making their purchase decisions (Chevalier and Mayzlin 2006). In Online Appendix 1, we conducted a robustness check by mining the review text using sentiment analysis as an alternative way to identify positive and negative reviews. We obtain similar estimation results compared with those presented in Section 5.

## 4.2. Exploratory Study

To study the impact of management response on future ratings, we start with a model-free analysis to examine how future ratings evolve with versus without a response. First, suppose a review (say, r<sub>j</sub>) does not receive a response. The average of the next n (window size) review ratings is

$$
\frac {1}{n} \sum_ {i = j + 1} ^ {j + n} r _ {i}.
$$

To exclude any possible preexisting trend, we calculate the difference of the mean review ratings between the n reviews before review $j$ as

$$
\Delta r _ {j} = \frac {1}{n} \sum_ {i = j + 1} ^ {j + n} r _ {i} - \frac {1}{n} \sum_ {i = j - n} ^ {j - 1} r _ {i}.
$$

We repeat this calculation for each review with no response and then compute the average $\Delta r _ { j } .$ . The grand mean of $\Delta r _ { j }$ across all the tours is denoted as $\mathbb { E } ( \Delta r _ { j } )$ . We split $r _ { j }$ to negative review ratings (with ratings less than or equal to four) and positive ones (with ratings equal to five) and calculate $\mathbb { E } ( \Delta r _ { j } )$ under each situation.

Following the same calculation, we then compute $\mathbb { E } ( \Delta r _ { j } )$ for the reviews with a response. In both cases (with and without response), we only consider those reviews where the reviews before and after the focal review did not contain a response to expunge possible confounds.

Table 3 tabulates the values of $\mathbb { E } ( \Delta r _ { j } )$ for the two cases by varying n as 20, 10, 3, and 1. To empirically verify whether the mean values of the cases—with versus without response—are statistically different or not, we conduct t-test for each n value with p-value shown in Table 3. In sum, Table 3 demonstrates that the impact of responding is more when the current rating is low (rating of one, two, three, four). However, there is no significant impact of a response when the rating is high (rating of five). The effect of responding is quite consistent across different window sizes $n ,$ but the effect in the case of a window size of one is only marginally significant at the 0.1 level. Therefore, a response may not have an immediate effect. Having empirically demonstrated that there is indeed a positive impact of responding to reviews, we probe deeper to shed light on how responses may alter the way reviewers write reviews. As we discussed earlier in Section 3.1, if customers were to voice a complaint on an issue that has already been raised and responded to, they would feel obliged to express their complaint differently than what previous reviewers had done. They would also feel the need to describe the complaints in more detail, that is, better “justify” their complaints. This surfaces two, empirically testable, questions:

(1) Does a response affect the content of negative reviews after the response? We found that when there is a response (treatment group), the content similarity of negative reviews before and after the response is lower than the similarity when there is no response (control group).<sup>7</sup> To empirically verify whether the mean values of the treatment and control group are statistically different or not, we conduct a t-test for each window size. These results are presented in Table 4. For example, in Table $^ { 4 , }$ for a window size of 20, the average similarity significantly decreased $( p = 0 . 0 0 1 )$ from 0.528 (without response) to 0.451 (with response) We, therefore, believe that review writers face the additional burden of explaining the point differently if they were to write a negative review after a response.

(2) Does a response affect the length of negative reviews after the response? We found that when there is a response (treatment group), the length of negative reviews after the response increases compared with that of the no-response case (control group). To empirically verify whether the mean values of the treatment and control group are statistically different or not, we conduct a t-test for each window size. These results are presented in Table 5. For a window size of 20, the average length significantly increased $( p < 0 . 0 0 1 )$ from 41.2 words (without response) to 45.3 words (with response). We believe that this increased length reflects the additional burden negative review writers have when writing a negative review after a response.

Table 3. Improvement of Ratings After Response

<table><tr><td>Window size</td><td>Without response to negative rating</td><td>With response to negative rating</td><td>p-Value</td><td>Without response to positive rating</td><td>With response to positive rating</td><td>p-Value</td></tr><tr><td>20</td><td>0.045 (4,077)</td><td>0.079 (211)</td><td>0.013</td><td>0.048 (15,519)</td><td>0.041 (65)</td><td>0.742</td></tr><tr><td>10</td><td>0.064 (7,297)</td><td>0.116 (495)</td><td>0.000</td><td>0.065 (24,825)</td><td>0.071 (126)</td><td>0.807</td></tr><tr><td>3</td><td>0.065 (12,225)</td><td>0.099 (1,060)</td><td>0.042</td><td>0.079 (38,015)</td><td>0.106 (232)</td><td>0.392</td></tr><tr><td>1</td><td>0.057 (14,516)</td><td>0.099 (1,385)</td><td>0.093</td><td>0.089 (42,121)</td><td>0.166 (289)</td><td>0.102</td></tr></table>

Note. The number of observations is reported in parentheses.

Table 4. Average Similarity Scores of Negative Reviews

<table><tr><td>Window size</td><td>Without response</td><td>With response</td><td>p-Value</td></tr><tr><td>20</td><td>0.528 (0.184, 19,596)</td><td>0.451 (0.199, 276)</td><td>0.001</td></tr><tr><td>10</td><td>0.378 (0.173, 32,122)</td><td>0.347 (0.158, 621)</td><td>0.003</td></tr></table>

Note. The standard deviation and the number of observations are reported in parentheses.

To further mitigate the concern about whether responses really matter, we establish a more causal link between a firm’s response and future ratings. A direct field experiment with Ctrip or Expedia would have been most helpful. However, given the unavailability of such unique data, the next best alternative was to obtain casual evidence through a quasi-experimental analysis. We use difference-in-differences analysis in combination with propensity score matching (PSM) to establish the link between the firm’s response and future review ratings. Once again, the analysis shows that responses indeed boost future ratings. (Please refer to Online Appendix 2 for details on the quasiexperiment.)

## 5. Model Estimation

We apply the maximum likelihood estimation (MLE) procedure to recover the parameters in our SDE model. The parameters that need to be estimated are the response effort (α), damage (β), boost (ρ), arrival rate (λ), negative review probability (p), and magnitude of the stochastic component (σ). The value of the upper bound for the rating (b) is fixed to be five because this is the value of the highest rating allowed by the review system. The unit of analysis is a specific tour; that is, we estimate these parameters for each tour. To apply MLE, we first need to specify the probability density function of $y _ { t } ,$ which has been originally derived in Feller (1951).

For a given value of $y _ { t }$ at time $t ,$ the density of $y _ { t + s }$ at time $t + s$ is

$$
p (y _ {t + s} | y _ {t}; \alpha , \rho , \beta , \sigma , \lambda , p, s) = c e ^ {- u - v} (\frac {v}{u}) ^ {\frac {q}{2}} I _ {q} (2 \sqrt {u v}),\tag{7}
$$

where

$$
\begin{array}{r l} & c = \frac {2 k _ {1}}{\sigma^ {2} (1 - e ^ {- k _ {1} s})}, \\ & u = c y _ {t} e ^ {- k _ {1} s}, \\ & v = c y _ {t + s}, \\ & q = \frac {2 k _ {1} k _ {3}}{\sigma^ {2}} - 1, \\ & k _ {1} = \alpha + \rho (1 - p) \lambda + \beta p \lambda , \\ & k _ {3} = \frac {5 \beta p \lambda}{\alpha + \rho (1 - p) \lambda + \beta p \lambda}, \end{array}
$$

and

$$
I _ {q} (2 \sqrt {u v}),
$$

is the modified Bessel function (Hazewinkel 2002) of order $q .$ . The coefficient $k _ { 1 }$ measures the speed of reversion, and $k _ { 3 }$ is the steady-state mean of $y _ { t } .$ . The stochastic quantity $2 c y _ { t + s }$ follows a noncentral chi-squared distribution with the noncentrality parameter 2u and degrees of freedom $2 q + 2$ (Cairns $2 0 0 4 ) . ^ { 8 }$ For simplicity, we define $\theta \equiv ( \alpha , \rho , \beta , p , \lambda , \sigma )$ . The log-likelihood function for $y _ { t }$ with N observations is

$$
\ln L (\theta) = \sum_ {i = 1} ^ {N - 1} \ln p (y _ {t _ {i + 1}} | y _ {t _ {i}}; \theta , \Delta t).\tag{8}
$$

Plugging Equation (7) into Equation (8) yields

$$
\begin{array}{l} \ln L (\theta) = (N - 1) \ln c \\ \qquad + \sum_ {i = 1} ^ {N - 1} [ - u _ {t _ {i}} - v _ {t _ {i + 1}} + 0. 5 q \ln \frac {v _ {t _ {i + 1}}}{u _ {t _ {i}}} \\ \qquad + \ln I _ {q} (2 \sqrt {u _ {t _ {i}} v _ {t _ {i + 1}}}) ], \end{array}\tag{9}
$$

where $u _ { t _ { i } } = c y _ { t _ { i } } e ^ { - k _ { 1 } \Delta t } .$ and $v _ { t _ { i + 1 } } = c y _ { t _ { i + 1 } } .$ . The maximum likelihood estimate $\hat { \theta }$ is solved by maximizing the loglikelihood function described in Equation (9) over its parameter space:

$$
\hat {\theta} = (\hat {\alpha}, \hat {\rho}, \hat {\beta}, \hat {p}, \hat {\lambda}, \hat {\sigma}) = \underset {\theta} {\arg \max} \ln L (\theta).
$$

We then describe how the values of the review arrival rat λ and the negative review probability p are estimated from the data. For each tour, we observe the time stamp of every review. Taking the first difference along two consecutive reviews yields the interarrival time of reviews. The reciprocal of its average is the expected review arrival rate λ. We empirically verify with our data that the interarrival time of reviews approaches an exponential distribution, indicating reviews arrive according to a Poisson process with rate λ. The expected probability of negative review p is inferred by counting the number of negative reviews over the total number of reviews for each tour. We also empirically verify that negative reviews arrive according to a Poisson process with rate pλ, consistent with the theory that the split of a Poisson process is also a Poisson process.

Table 5. Average Length (Number of Words) of Negative Reviews

<table><tr><td>Window size</td><td>Without response</td><td>With response</td><td>p-Value</td></tr><tr><td>20</td><td>41.2 (19,596)</td><td>45.3 (276)</td><td>0.000</td></tr><tr><td>10</td><td>42.5 (32,122)</td><td>47.3 (621)</td><td>0.000</td></tr><tr><td>3</td><td>43.9 (50,240)</td><td>47.9 (1,292)</td><td>0.002</td></tr></table>

Note. The number of observations is reported in parentheses.

Next, we validate our model assumption using a representative tour with ID 5106. Figure 2(a) plots the histogram of the interarrival time (days) of reviews. Figure 2(b) presents an empirical Q-Q plot of the observed empirical quantiles of the interarrival time versus the theoretical quantiles of the exponential distribution with mean value $1 / \lambda = 0 . 6 2 7$ (one review every 0.627 days). Figure 2(b) shows that the dotted line approximates the (straight) solid line, indicating that the review interarrival time fits well with an exponential distribution with mean $0 . 6 2 7 . ^ { 9 }$ Thus, our assumption of Poisson review arrival with rate $1 / 0 . 6 2 7 = 1 . 5 9 \dot { 5 }$ (1.595 reviews per day) is reasonable.

Because we have the time stamp of every negative review, we are able to compute the interarrival time of negative reviews as well. Figure 2(c) depicts the histogram of the interarrival time of negative reviews, and Figure 2(d) delineates the Q-Q plot for the case of negative reviews with a mean value 2.121 for the theoretical exponential distribution. The agreement between the two lines indicates that the interarrival time of negative reviews approximates the exponential distribution with mean 2.121. Therefore, negative reviews arrive according to Poisson process with rate $1 / 2 . 1 2 1 = 0 . 4 7 1 4$ (0.4714 negative reviews per day) Note that the probability of negative reviews for tour

Figure 2. (Color online) Interarrival Time of Reviews and Negative Reviews for Tour ID 5106  
![](/api/attachments/BV478HNE/fulltext/images/e957b4ecc8bcfba9645771567620903daded3a38ea8a76c9537d087cfa45ede3.jpg)

![](/api/attachments/BV478HNE/fulltext/images/88b7f39611255c63aace73ec884d31b1f6b4acb7a69330ae97333b5e4645b093.jpg)

![](/api/attachments/BV478HNE/fulltext/images/37c069bf131268937d28d4eb37ada136b196eec3d712a765430f073b71c56f01.jpg)

![](/api/attachments/BV478HNE/fulltext/images/132d4bd5afa11f23447df726c4d57e0b9d29c4ba1056f10ca5dbd9dcc076bba0.jpg)

ID 5106 is $p = 0 . 2 9 8$ , and the estimated negative review arrival rate from the review arrival rate and the probability of negative reviews equals to $p \lambda = 0 . 2 9 8 / 0 . 6 2 7 =$ 0.4753 (0.4753 negative reviews per day), which is very close to 0.4714.

We further calculate Theil’s U index (Theil 1966) to test whether it is a satisfactory fit (less than the critica value 0.1) statistically. Theil’s U index is 0.06 for the case of interarrival time and is 0.05 for the case of negative interarrival time, indicating a satisfactory fit.<sup>10</sup> The results show that our assumption of Poisson arrivals is valid for this representative tour. We similarly examined each tour yielding different values of λ and p and validated the Poisson arrival assumption for all the tours.

In Equation (1), the defining feature behind our SDE model is a mean-reverting property (x<sub>t</sub> fluctuating around $k _ { 2 } )$ . We further empirically verify whether the time-series data used in this study exhibit a meanreverting characteristic by calculating the Hurst exponent H (Hurst 1951). When $0 < H < 0 . 5 ,$ , the series display a mean-reverting characteristic, and the strength of the mean-reverting behavior increases as the Hurst exponent H approaches zero. The estimated Hurst exponent H value of our data is 0.36, implying that our time-series data indeed follow a mean-reverting process. Interestingly, such a mean-reverting phenomenon in ratings is explained in the work of Moe and Schweidel (2012), in which they find that reviewers tend to beg to differ, that is, say something different from previous reviewers. Reviewers tend to post negative (positive) reviews when earlier reviews are more positive (negative), hence fostering mean reversion.

We use the Nelder–Mead simplex algorithm to numerically obtain the MLE estimates. For quick convergence, good initial values of the variables are crucial. In Online Appendix 3, we describe how good initial values for the control effort parameter, the boost parameter, the damage parameter, and the magnitude of the stochastic component are chosen. We implemented the SDE estimation procedure in MATLAB.

As an illustration, Table 6 presents estimation results for only 10 tours (because of space limitation) with the standard error in parentheses.<sup>11</sup> The estimation results for the remaining 107 tours are in Online Appendix 4. In Table $^ { 6 , }$ for each tour, we estimate the corresponding review arrival rate, the probability of negative review, the control effort parameter, the boost parameter, the damage parameter, and the magnitude of the stochastic component. Table 6 shows that there is considerable variation across all tours with respect to all these parameters, and most estimates are significant.

In understanding the estimation results across tours, comparing the estimated values of the parameter α and ρ provides us fewer insights because the impacts of the control part and positive arriving reviews to $d { x _ { t } }$ depend on $\alpha ( b - x _ { t } )$ and $\lambda ( 1 - p ) \rho ( b - x _ { t } )$ , respectively. To compare the impacts from the two forces more intuitively, we introduce $\gamma _ { 1 } = \alpha / ( \lambda ( 1 - p ) \rho )$ , which measures the normalized boosting impact of the firm’s control relative to the boosting impact of a positive review. In this sense, $\gamma _ { 1 }$ is similar to the notion of an odds ratio, with which the marginal impact of firm’s response is measured against that of a positive review. $\gamma _ { 1 } > 1$ represents that firms’ control exerts more influence in boosting the state than a positive review does on average. The eighth column in Table 6 presents the value of $\gamma _ { 1 }$ for each tour. We find there is a large variance in $\gamma _ { 1 }$ across the whole 117 tours (the average value of $\gamma _ { 1 }$ is 1.73 with a high variance 24.06), indicating that the response strategies across tours are quite different. In Section 7, we provide an operational interpretation of these response strategies and develop procedures to optimize them under different business objectives.

In a similar manner, we define $\gamma _ { 2 } = \rho ( 5 - \mathbb { E } ( x _ { t } ) ) /$ $\beta \mathbb { E } ( x _ { t } )$ to measure the relative impact of a positive review against the impact of a negative review. The last column in Table 6 shows that the relative impact of positive reviews with respect to negative ones is about the same across the whole 117 tours (the average value of $\gamma _ { 2 }$ is 0.38 with a small variance 0.12). Given $\gamma _ { 2 } < 1$ from our results, the negative review has a bigger influence (on the state) than a positive review, which is consistent with prior study (Chevalier and Mayzlin 2006). We next validate our SDE model with extensive model comparisons.

Table 6. Parameter Estimates for 10 Random Tours (out of 117 Tours)

<table><tr><td>Tour ID</td><td> $\hat{\lambda}$ </td><td> $\hat{p}$ </td><td> $\hat{\alpha}$ </td><td> $\hat{\rho}$ </td><td> $\hat{\beta}$ </td><td> $\hat{\sigma}$ </td><td> $\gamma_1$ </td><td> $\gamma_2$ </td></tr><tr><td>5106</td><td>1.595***(0.259)</td><td>0.298***(0.031)</td><td>0.032***(0.007)</td><td>0.019***(0.007)</td><td>0.009***(0.001)</td><td>0.092***(0.002)</td><td>1.55</td><td>0.17</td></tr><tr><td>72528</td><td>1.533***(0.333)</td><td>0.42***(0.052)</td><td>0.031***(0.008)</td><td>0.019**(0.009)</td><td>0.008***(0.001)</td><td>0.084***(0.003)</td><td>1.83</td><td>0.26</td></tr><tr><td>73154</td><td>2.22***(0.281)</td><td>0.358***(0.029)</td><td>0.059***(0.009)</td><td>0.020***(0.006)</td><td>0.011***(0.001)</td><td>0.115***(0.003)</td><td>2.06</td><td>0.18</td></tr><tr><td>80961</td><td>6.377***(0.817)</td><td>0.193***(0.024)</td><td>0.031(0.027)</td><td>0.019***(0.005)</td><td>0.005***(0.000)</td><td>0.232***(0.003)</td><td>0.32</td><td>0.19</td></tr><tr><td>29336</td><td>1.941***(0.644)</td><td>0.266***(0.063)</td><td>0.013*(0.010)</td><td>0.010*(0.007)</td><td>0.003***(0.001)</td><td>0.112***(0.003)</td><td>0.92</td><td>0.19</td></tr><tr><td>23222</td><td>1.633***(0.269)</td><td>0.248***(0.029)</td><td>0.052***(0.011)</td><td>0.019**(0.009)</td><td>0.011***(0.001)</td><td>0.098***(0.003)</td><td>2.23</td><td>0.10</td></tr><tr><td>30938</td><td>1.54***(0.489)</td><td>0.279***(0.053)</td><td>0.014*(0.010)</td><td>0.020**(0.009)</td><td>0.006***(0.001)</td><td>0.091***(0.003)</td><td>0.63</td><td>0.24</td></tr><tr><td>71480</td><td>3.428***(0.471)</td><td>0.261***(0.026)</td><td>0.030**(0.013)</td><td>0.020***(0.005)</td><td>0.006***(0.001)</td><td>0.156***(0.003)</td><td>0.59</td><td>0.22</td></tr><tr><td>88292</td><td>3.711***(0.539)</td><td>0.216***(0.027)</td><td>0.030*(0.023)</td><td>0.017**(0.008)</td><td>0.006***(0.001)</td><td>0.198***(0.004)</td><td>0.60</td><td>0.17</td></tr><tr><td>1618693</td><td>19.72***(1.547)</td><td>0.163***(0.013)</td><td>0.248***(0.063)</td><td>0.187***(0.004)</td><td>0.045***(0.001)</td><td>0.410***(0.002)</td><td>0.08</td><td>0.18</td></tr></table>

Notes. The estimation is based on the in-sample data for each tour. The standard error is reported in parentheses. $^ { * * * } p \leq 0 . 0 1 ; { } ^ { * * } p \leq 0 . 0 5 ; { } ^ { * } p \leq 0 . 1 0 .$

## 6. Model Validation

The best way to validate a structural model is to predict the outcomes of quasi-experiments that the world presents to us, in which a policy change occurs and the data before and after the change are available. However, such opportunities are rare. Keane (2010) advocates alternatively validating a structural model (against a reduced-form model) by resting primarily on how well the model performs in validation exercises, that is, by examining whether the model does a reasonable job of fitting the historical data and whether the model does a reasonable job at out-of-sample prediction. In our setting, because we could not apply falsification tests to validate (or invalidate) our prescriptive model that requires conducting a field experiment with the firm, we rely on comparing different models using the predictive performance. Specifically, we examine whether our proposed SDE model performs well on the basis of predictive performance as compared with conventional reducedform time-series models, including the representative ARMA, GARCH, MA, ES, and NM.

ARMA is a classic method to model time-series data. The model consists of two parts, an autoregressive part and a moving average part. The autoregressive part is a function of a lagged dependent variable, and the moving average component is a function of lagged error terms. The model normally takes the form of $A R M A ( p , q )$ where p is the order of the autoregressive part and q is the order of the moving average part. After specifying p and $q ,$ ARMA models can be estimated by least square regressions. The GARCH model is an extension of Engle’s autoregressive conditional heteroscedasticity (ARCH) model for variance heteroscedasticity. The $G A R C H ( p , q )$ model specifies p GARCH coefficients associated with lagged variances and q ARCH coefficients associated with lagged squared innovations. A simple MA uses the unweighted mean of the previous m observations to forecast the next data point (Brown 2004); and the simple ES weights the past data in an exponentially decreasing manner, analogous to the discounting of cash flows over time (Brown 2004). We choose m equal to five in our operationalization of MA and ES.<sup>12</sup> The NM myopically uses the historical mean of the in-sample as prediction of the future state.

For each tour, we use the first 70% portion as insample and the remaining as out-of-sample. We use insample to calibrate all the models considered.<sup>13</sup> For both the ARMA and GARCH, the choices of p and q are empirically determined from the data on the basis of Bayesian information criterion values for each tour. We then use the trained models to predict the out-ofsample. For SDE, $y _ { t }$ follows the data-generating process specified in Equation (4). Given an initial point of $y _ { 0 } ,$ , the conditional expectation at time t is $\hat { y } _ { t } = \bar { \mathbb { E } } \bar { ( y _ { t } | y _ { 0 } ) } = ( y _ { 0 } -$ $k _ { 3 } ) e ^ { - k _ { 1 } t } + k _ { 3 }$ and $\hat { x } _ { t } = 5 - \hat { y } _ { t }$ . The out-of-sample predictive performance is measured using root mean squared error (RMSE), mean absolute error (MAE), and symmetric mean absolute percentage error (SMAPE). RMSE is calculated following $\begin{array} { r } { R M S E = \sqrt { \sum _ { t = 1 } ^ { n } \frac { ( \hat { x } _ { t } - x _ { t } ) ^ { 2 } } { n } } , } \end{array}$ , MAE is computed as $\begin{array} { r } { M A E = \sum _ { t = 1 } ^ { n } \frac { \left| \hat { x } _ { t } - x _ { t } \right| } { n } . } \end{array}$ , and SMAPE takes the form of $\begin{array} { r } { { S M A P E } = \frac { 1 0 0 \% } { n } \sum _ { t = 1 } ^ { n } \frac { \left| \hat { x } _ { t } - x _ { t } \right| } { \left| \hat { x } _ { t } \right| + \left| x _ { t } \right| } } \end{array}$

## 6.1. In-Sample Performance

We first validate our proposed data-generating process of review ratings by comparing the estimated steadystate mean (as t goes to infinity) of the state variable $x _ { t }$ with the observed steady-state mean. The observed mean $\mu$ is derived from the data directly according to $\begin{array} { r } { \mu = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } x _ { i } . } \end{array}$ . The estimated steady-state mean of $x _ { t }$ using SDE is calculated as $\hat { \mu } _ { S D E } = 5 - \hat { k } _ { 3 }$ . The values of ${ \hat { \mu } } _ { A R M A } , \ { \hat { \mu } } _ { G A R C H } , \ { \hat { \mu } } _ { M A } ,$ and $\hat { \mu } _ { E S }$ represent the estimated steady-state means of review ratings using ARMA, GARCH, MA, and ES, respectively.<sup>14</sup>

We compare the steady-state mean of the SDE approach with the benchmark methods based on the RMSE criterion. The RMSE values of all the methods for each tour are calculated. The mean RMSE values (in increasing order) are 0.011 (SDE), 0.033 (ARMA), 0.061 (GARCH), 0.110 (MA), and 0.111 (ES). Note that SDE has the lowest mean RMSE value. We conduct a paired t-test between SDE and the benchmark methods to examine whether the two means are statistically different. These results are reported in Table 7. For robustness, we also conduct the nonparametric Wilcoxon rank sum test and find that the results of the paired ttest and the Wilcoxon rank sum test are consistent. The statistical tests confirm that the differences in the mean RMSE values for SDE and the benchmark methods are statistically significant. To summarize, the SDE method outperforms the benchmark methods in terms of its ability to predict the steady-state mean.

Table 7. Paired t-Test Results: Mean RMSE of Steady-State Mean

<table><tr><td>Comparison</td><td>t-Statistic (p-value)</td></tr><tr><td>SDE versus ARMA</td><td>-5.3145*** (0.000)</td></tr><tr><td>SDE versus GARCH</td><td>-7.6493*** (0.000)</td></tr><tr><td>SDE versus MA</td><td>-10.7183*** (0.000)</td></tr><tr><td>SDE versus ES</td><td>-10.7762*** (0.000)</td></tr></table>

\*\*\*p 0.01; \*\*p 0.05; \*p 0.10.

Table 8. Comparative Performance Results: In-Sample and Out-of-Sample

<table><tr><td></td><td>Metric</td><td>SDE</td><td>ARMA</td><td>GARCH</td><td>MA</td><td>ES</td><td>NM</td></tr><tr><td rowspan="3">In-sample</td><td>RMSE</td><td>0.1457 (0.0444)</td><td>0.1431 (0.0392)</td><td>0.1952 (0.0948)</td><td>0.2107 (0.0858)</td><td>0.2102 (0.0859)</td><td>N/A</td></tr><tr><td>MAE</td><td>0.1182 (0.0353)</td><td>0.1163 (0.0316)</td><td>0.1414 (0.0565)</td><td>0.175 (0.0791)</td><td>0.1745 (0.0791)</td><td>N/A</td></tr><tr><td>SMAPE</td><td>0.1569 (0.0572)</td><td>0.1561 (0.0574)</td><td>0.1826 (0.0758)</td><td>0.2372 (0.1095)</td><td>0.2367 (0.1103)</td><td>N/A</td></tr><tr><td rowspan="3">Out-of-sample long term</td><td>RMSE</td><td>0.1878 (0.0868)</td><td>0.1937 (0.0861)</td><td>0.2505 (0.1383)</td><td>0.2267 (0.1024)</td><td>0.2267 (0.1029)</td><td>0.183 (0.0612)</td></tr><tr><td>MAE</td><td>0.1537 (0.078)</td><td>0.1582 (0.0758)</td><td>0.1914 (0.0962)</td><td>0.1922 (0.0942)</td><td>0.1921 (0.0947)</td><td>0.1488 (0.0507)</td></tr><tr><td>SMAPE</td><td>0.1793 (0.0811)</td><td>0.1886 (0.0975)</td><td>0.2223 (0.1048)</td><td>0.2234 (0.1136)</td><td>0.2231 (0.1137)</td><td>0.1761 (0.0625)</td></tr><tr><td rowspan="3">Out-of-sample short term</td><td>RMSE</td><td>0.1353 (0.0618)</td><td>0.1547 (0.076)</td><td>0.6251 (0.7716)</td><td>0.1648 (0.0768)</td><td>0.1634 (0.076)</td><td>0.1642 (0.0785)</td></tr><tr><td>MAE</td><td>0.1129 (0.054)</td><td>0.133 (0.0701)</td><td>0.4722 (0.5508)</td><td>0.1433 (0.069)</td><td>0.1415 (0.068)</td><td>0.1448 (0.0731)</td></tr><tr><td>SMAPE</td><td>0.1377 (0.0722)</td><td>0.1615 (0.0849)</td><td>0.3103 (0.2243)</td><td>0.1734 (0.0926)</td><td>0.1715 (0.0916)</td><td>0.1755 (0.0938)</td></tr></table>

Note. The standard deviation is reported in parentheses.

Besides the steady-state mean, we also present RMSE, MAE, and SMAPE for all the methods to gauge the in-sample inference performance in Table 8 (with standard deviation in parentheses) across the 117 tours. Table 9 presents the t-statistics and corresponding p-values for the statistical comparisons pertaining to in-sample metrics. As Table 9 shows, the SDE method outperforms GARCH, MA, and ES but is comparable with ARMA. Note that the NM performance is trivial in the sense that it is true by construction: it uses the historical mean to predict the historical mean.

## 6.2. Out-of-Sample Performance

We then compare the predictive performance of the SDE model with ARMA, GARCH, MA, ES, and NM models on out-of-sample data. Here we conduct two types of predictive analyses: long term and short term. Long-term prediction refers to the ability to predict the value of x<sub>t</sub> at the end of the out-of-sample period, whereas short-term prediction refers to the ability to predict the value of x<sub>t</sub> at the end of the next 20 observations.<sup>15</sup> Table 8 presents the average of the out-ofsample metrics, including RMSE, MAE, and SMAPE (in terms of long term and short term) across the 117 tours for all the methods. Table 9 shows the t-statistics and corresponding p-values pertaining to out-of-sample metrics.<sup>16</sup> Among these methods, GARCH performs the worst. We applied the Engle test for residual heteroscedasticity (Engle 1982), and the results indicate that the autoregressive conditional heteroscedasticity effect is not significant, meaning the GARCH model does not fit our time-series data well. The SDE method achieves comparable performance with ARMA and NM for the long-term out-of-sample prediction but outperforms ARMA and NM in terms of the short-term prediction. As a whole, the SDE method performs better than GARCH, MA, and ES for both long-term and short-term out-ofsample prediction.

As summarized in Table 9, SDE is superior (or at least comparable) to all the benchmark methods, no matter what performance measure is used (RMSE, MAE, and SMAPE). The few cases in which SDE does not show superiority in long-term predictive performance is when compared against ARMA and NM. Both these methods typically perform well when predicting the long-term out of sample.

Table 9. Paired t-Test Results: In-Sample and Out-of-Sample

<table><tr><td></td><td>Comparison</td><td>In-sample</td><td>Out-of-sample Long term</td><td>Out-of-sample Short term</td></tr><tr><td rowspan="5">RMSE</td><td>SDE versus ARMA</td><td>0.4752 (0.3175)</td><td>-0.5241 (0.3003)</td><td>-2.1332** (0.017)</td></tr><tr><td>SDE versus GARCH</td><td>-5.1091*** (0.000)</td><td>-4.155*** (0.000)</td><td>-6.8437*** (0.000)</td></tr><tr><td>SDE versus MA</td><td>-7.2795*** (0.000)</td><td>-3.1381*** (0.001)</td><td>-3.2357*** (0.0007)</td></tr><tr><td>SDE versus ES</td><td>-7.2183*** (0.000)</td><td>-3.1262*** (0.001)</td><td>-3.0932*** (0.0011)</td></tr><tr><td>SDE versus NM</td><td>N/A</td><td>0.4798 (0.3159)</td><td>-3.1252*** (0.001)</td></tr><tr><td rowspan="5">MAE</td><td>SDE versus ARMA</td><td>0.4434 (0.3289)</td><td>-0.4517 (0.3259)</td><td>-2.4514*** (0.0075)</td></tr><tr><td>SDE versus GARCH</td><td>-3.7716*** (0.0001)</td><td>-3.2924*** (0.0006)</td><td>-7.0213*** (0.000)</td></tr><tr><td>SDE versus MA</td><td>-7.093*** (0.000)</td><td>-3.411*** (0.0004)</td><td>-3.742*** (0.0001)</td></tr><tr><td>SDE versus ES</td><td>-7.0335*** (0.000)</td><td>-3.3833*** (0.0004)</td><td>-3.5603*** (0.0002)</td></tr><tr><td>SDE versus NM</td><td>N/A</td><td>0.5635 (0.2868)</td><td>-3.7892*** (0.0001)</td></tr><tr><td rowspan="5">SMAPE</td><td>SDE versus ARMA</td><td>0.1153 (0.4541)</td><td>-0.7889 (0.2155)</td><td>-2.3143*** (0.0108)</td></tr><tr><td>SDE versus GARCH</td><td>-2.9251*** (0.0019)</td><td>-3.5086*** (0.0003)</td><td>-7.9258*** (0.000)</td></tr><tr><td>SDE versus MA</td><td>-7.0269*** (0.000)</td><td>-3.4182*** (0.0004)</td><td>-3.2901*** (0.0006)</td></tr><tr><td>SDE versus ES</td><td>-6.9412*** (0.000)</td><td>-3.391*** (0.0004)</td><td>-3.1329*** (0.001)</td></tr><tr><td>SDE versus NM</td><td>N/A</td><td>0.3432 (0.3659)</td><td>-3.4512*** (0.0003)</td></tr></table>

Note. The p-value is reported in parentheses.  
\*\*\*p 0.01; \*\*p 0.05; \*p 0.10.

These results do not undermine the superiority of the SDE model. First, the short-term predictive performances of NM and ARMA are rather poor. From a control perspective, knowing the future in the short term is more important because a control is a short-term intervention device rather than something like a strategic plan that has medium- to long-term implications. Further, only the SDE model is capable of prescribing a response strategy that best achieves the control objectives of the firm.

The key advantage of the SDE approach lies in its ability to perform counterfactual analyses that managers can use to anticipate the impact (on ratings) of a change in the control parameter (response strategy). That is, SDE is not just a predictive tool, it is also a prescriptive one. On the other hand, all the benchmark methods are solely predictive in nature with no prescriptive capabilities. We further demonstrate the prescriptive value of SDE in Section 7.2.

## 7. Probabilistic Response Strategy and Applications

To demonstrate the prescriptive use of our model, this section maps the control parameter (α) to a probabilistic response strategy (policy) under different business objectives, thus providing an operational interpretation for the control. We further provide some practical applications of how the probabilistic response strategy could be implemented to achieve a certain managerial goal. This is only made possible through our structural SDE model (e.g., as opposed to ARMA, GARCH, etc.).

## 7.1. Mapping to a Probabilistic Control

A theoretical control parameter is difficult to interpret in practice and raises the natural question: what does it mean for a firm to use a particular value under the control? One possible interpretation of our control parameter α is in terms of staffing (or sales-force management), with which the maximum value of the control corresponds to the maximum number of personnel that can be allocated to the job of responding to reviews. A second, more direct interpretation is that the firm could choose to respond to a certain percentage of reviews. It would be reasonable to expect this percentage to increase as $x _ { t }$ decreases, implying that the firm would respond more actively when the current perception of quality is low.

Based on this rationale, we propose a probabilistic response strategy with which the firm responds to a review with a probability of $p ( x _ { t } )$ . In other words, the probability of providing a response to the arriving review $\left( r _ { t } \right)$ at time t depends on the current state $x _ { t } .$ Using Equation (5), the expected value of the transformed perception of quality variable after the time increment $\Delta t$ is

$$
\mathbb {E} \big (y _ {t + \Delta t} | y _ {t} \big) = y _ {t} e ^ {- k _ {1} \Delta t} + k _ {3} \big (1 - e ^ {- k _ {1} \Delta t} \big),
$$

where $y _ { t }$ is the initial value of the variable at time $t .$

Because $y _ { t } = b - x _ { t } , $ , we $\mathrm { g e t } _ { \mathrm { \ell } }$

$$
\mathbb {E} (x _ {t + \Delta t} | x _ {t}) = b - (b - x _ {t}) e ^ {- k _ {1} \Delta t} - k _ {3} \big (1 - e ^ {- k _ {1} \Delta t} \big),
$$

where $k _ { 1 } k _ { 2 } = \rho \lambda ( 1 - p ) b + \alpha b , k _ { 1 } = \alpha + \beta \lambda p + \rho \lambda ( 1 - p ) ,$ and $k _ { 3 } = b - k _ { 2 }$ . The coefficient $k _ { 1 }$ measures the speed of reversion; $k _ { 2 }$ and $k _ { 3 }$ are the steady-state mean of $x _ { t }$ and $y _ { t } ,$ respectively. Theoretically, the expected change in the state variable over time span <sup>Δ</sup>t given the initial value $x _ { t }$ at time t is

$$
\Delta x = \mathbb {E} (x _ {t + \Delta t} | x _ {t}) - x _ {t} = (b - x _ {t} - k _ {3}) \big (1 - e ^ {- k _ {1} \Delta t} \big).
$$

Next, using the data for each tour, we calculate the average increment in the perception of quality following a response. To calculate this average, suppose we have M responses given the state $x _ { t }$ in a tour. For each response $i ,$ we calculate the increment of the state variable over $\Delta t ,$ denoted as $\delta _ { i } .$ . Then the average increment given the state $x _ { t }$ (denoted as δ) is

$$
\delta = \frac {1}{M} \sum_ {i = 1} ^ {M} \delta_ {i}.
$$

Over the time span $\Delta t ,$ , there are an expected $\lambda \Delta t$ number of arriving reviews, of which $p ( x _ { t } ) \lambda \Delta t$ would, on average, receive a response. The empirical average increment over the time span <sup>Δ</sup>t equals to $p ( x _ { t } ) \Delta t \lambda \delta .$ Here, λ<sup>Δ</sup>t is the probability of the arrival of a review in time <sup>Δ</sup>t. If we multiply this probability by $p ( x _ { t } )$ , we get the probability of an increase or decrease during <sup>Δ</sup>t. Note that δ represents the empirical average increase or decrease in ratings following a response after considering all effects. Equating the empirical average increment to the theoretically expected increment and setting <sup>Δ</sup>t close to zero, we have

$$
p (x _ {t}) \lambda \delta = k _ {1} (k _ {2} - x _ {t}).\tag{10}
$$

The left-hand side of Equation (10) reflects the (empirically found) net increase or decrease in the ratings per unit time. The right-hand side reflects the theoretical increase or decrease per unit time. Equation (10) directly solves for $p ( x _ { t } )$ . Using this relationship, we can represent the control parameter α in terms of a probabilistic response strategy. The probability of providing a response is clearly a decreasing function of $x _ { t }$ . Also, as the level of the control (α) increases, the probability of providing a response increases. This relationship for $p ( x _ { t } )$ shows that the probabilistic response strategy depends on the parameters for the tour: $\delta , \alpha , \lambda , \rho , \beta ,$ and $p .$ Of these parameters, the value of α can be chosen by the decision maker to achieve a prespecified goal. Having chosen an appropriate value of $\alpha$ (to be discussed next), the decision maker can implement this control using the probabilistic response strategy that corresponds to this choice of $\alpha .$

The interpretation of the process can be visualized from the data. For each tour, we split the data into insample and out-of-sample. We use in-sample to estimate αˆ and δ as well as other parameters and further calculate $\hat { p } ( x _ { t } )$ according to Equation (10) on the out-ofsample. For the same tour, we obtain the observed $p ( x _ { t } )$ from out-of-sample data. This is done by using the fraction of observations for which the perception of quality is $x _ { t }$ and a review resulted in a response. Then we compare the observed $p ( x _ { t } )$ with our fitted $\hat { p } ( x _ { t } )$ . We use tour 5106 to illustrate. In Figure $3 ( \mathrm { a } )$ , the solid line represents the observed probability of response, and the dotted line delineates $\hat { p } ( x _ { t } )$ derived from Equation (10). Figure 3(b) depicts the corresponding Q-Q plots of the observed response probability and the fitted probability. The points all are located fairly close to the reference line in general, indicating that the predicted response strategy fits well with the observed response 17 strategy.

## 7.2. Policy Recommendations and Applications

A key advantage of our proposed SDE approach lies in its ability to not only predict consumers’ perception of quality, but also to influence it by responding to customer opinions in a prescriptive sense. The firm could have different objectives concerning the manner in which it desires to influence the perception of quality. Our SDE approach enables the firm to determine how a probabilistic response strategy (policy) shall be chosen to achieve such a goal. Clearly, a purely predictive approach (especially one that does not model the underlying data-generating process) will not be of much help when it comes to intervene on the evolution of consumers’ perception of quality over time. We discuss later how our approach can be applied to three different control objectives with corresponding policy recommendations.

Figure 3. (Color online) Comparison of the Observed p x vs. the Fitted pˆ x  
![](/api/attachments/BV478HNE/fulltext/images/cd8ca8679aed7b3446d28a275ba63476859614f98f4944263083cc2632f87dd2.jpg)

Mean Control. A natural goal that firms might want to achieve is a target value of the average consumers perception of quality, $\boldsymbol { \mu } _ { g o a l }$ . We have

$$
\mu_ {g o a l} = \frac {5}{1 + \frac {\beta \lambda p}{\alpha + \rho \lambda (1 - p)}},
$$

hence, $\begin{array} { r } { \alpha = \frac { \beta \lambda p \mu _ { g o a l } } { 5 - \mu _ { g o a l } } - \rho \lambda ( 1 - p ) \ } \end{array}$ . Using Equation (10), this choice of α can then be mapped to a corresponding probabilistic response strategy.

Mean-Variance Control. A firm may want to influence not only the mean perception of quality, but also its variance because large fluctuations in consumers’ perception of quality would likely be viewed by customers as a sign of an unreliable product or service. For example, one kind of mean-variance control would be to achieve a specified value of the coefficient of variation of the state $( c _ { g } , \mathsf { s a y } )$ ). By solving

$$
\frac {\sqrt {\mathbb {V} (x _ {t})}}{\mu_ {x}} = \frac {\sqrt {\frac {k _ {3} \sigma^ {2}}{2 k _ {1}}}}{5 - k _ {3}} = \frac {\sqrt {\left(\frac {5 \beta \lambda p \sigma^ {2}}{2 (\alpha + \beta \lambda p + \rho \lambda (1 - p)) ^ {2}}\right)}}{\frac {5 (\alpha + \rho \lambda (1 - p))}{\alpha + \beta \lambda p + \rho \lambda (1 - p)}} = c _ {g},
$$

we can determine the value of the control (α) and then map this value to a corresponding probabilistic response strategy $p ( x _ { t } )$

Along similar lines, one may wish to set a lower limit $\left( \mathsf { s a y } , m _ { l } \right)$ for the mean-variance expression $\mu - \gamma \sqrt { \mathbb { V } ( x _ { t } ) }$ where $\gamma$ is a penalty for variation. Note that the mean and variance of $x _ { t }$ are both functions of $\alpha .$ . Hence, one can determine the smallest value of the control parameter α to achieve $m _ { l }$ and then map this value of α to a corresponding probabilistic response strategy.

![](/api/attachments/BV478HNE/fulltext/images/9066aaa075997a88acf5270a0b4080bc6c3a2fff5c4213b8d8fbae9e6bfa3759.jpg)

Service-Level Control. Rather than a mean-variance objective, firms may want to ensure that a certain percentage of the perception of quality is greater than a desired level d. This is especially important in service management because a high probability of poor performance (state falling below a certain level), despite a reasonable mean, indicates a poor service level. In the context of control applications, this phenomenon is referred to as “out of control” (Merchant 1982). Put differently, the objective is to provide a probabilistic guarantee that the state will not fall below a specified level over a given planning horizon. We call this servicelevel control because it is similar to provide a service-level guarantee if the ratings system (and the responsibility to respond to negative reviews) was offered as a service by a vendor.

The probability density function of 2cy<sub>i</sub> is a noncentral chi-squared distribution with $2 q + 2$ degrees of freedom and noncentrality parameter 2u. We have

$$
P \{x _ {i} \geq d \} = P \{y _ {i} \leq 5 - d \} = P \{2 c y _ {i} \leq 2 c (5 - d) \} = p _ {s},
$$

and further

$$
F _ {y} (2 c (5 - d); 2 q + 2, 2 u) = g (\alpha) = p _ {s}.
$$

Then the corresponding control parameter α is calculated through $\hat { \alpha } = g ^ { - 1 } ( \check { p } _ { s } )$ .

These three examples illustrate how firms’ potential objectives can be achieved by utilizing our SDE approach to manage an ongoing process proactively rather than merely predict its behavior reactively. Of course, firms could set different objectives and prescribe the optimal response strategy to achieve their specific objective in practice.

A Numerical Illustration. We again illustrate these policies with tour 5106. The estimated parameters for this tour are $\hat { \lambda } = 1 . 5 9 5 , \hat { p } = 0 . 2 9 8 , \hat { \rho } = \dot { 0 . 0 1 9 } , \hat { \beta } = 0 . 0 0 9 ,$ $\hat { \sigma } = 0 . 0 9 2 , \hat { \delta } = 0 . 0 3 2 9 ,$ , and $\hat { \alpha } = 0 . 0 3 2 ,$ , and the mean of the review ratings is ${ \hat { \mu } } = 4 . 6 3$ . We calculate its coefficient of variation, which is equal to 0.036, and the probability of the perception of quality greater than 4.7 is equal to 0.05. In mean control, the firm sets the target mean review rating to be 4.7, and the corresponding control parameter is $\hat { \alpha } _ { M } = 0 . 0 4 6$ . In mean-variance control, the target coefficient of variation of the review ratings is set to be 0.05, and the corresponding control parameter is $\hat { \alpha } _ { V } = 0 . 0 1 7$ . In service-level control, the firm would like to ensure that the probability that the perception of quality that is greater than 4.7 is 0.8. Here, the corresponding control parameter is $\hat { \alpha } _ { S } = 0 . 0 5 4$ . Using Equation (10), we map the value of the control to the probabilistic response strategy. When the state variable is greater than k (the target mean), the probability of providing a response is zero.

Table 10. Probabilistic Response Strategy for Different Control Objectives

<table><tr><td rowspan="2">Objective</td><td rowspan="2"> $\alpha$ </td><td colspan="8"> $x_{t}$ </td></tr><tr><td>4.0</td><td>4.1</td><td>4.2</td><td>4.3</td><td>4.4</td><td>4.5</td><td>4.6</td><td>4.7</td></tr><tr><td>Mean</td><td>0.046</td><td>0.96</td><td>0.82</td><td>0.68</td><td>0.55</td><td>0.41</td><td>0.27</td><td>0.14</td><td>0</td></tr><tr><td>Mean-variance</td><td>0.017</td><td>0.40</td><td>0.32</td><td>0.24</td><td>0.16</td><td>0.08</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Service-level</td><td>0.054</td><td>1</td><td>0.96</td><td>0.81</td><td>0.65</td><td>0.50</td><td>0.35</td><td>0.20</td><td>0.05</td></tr></table>

Table 10 tabulates the recommended probability of providing a response given the state $x _ { t }$ under the different control objectives discussed. Also shown (in th second column) is the value of the control (α) that achieves the objective (mean, mean-variance, and servicelevel). As the control (α) magnitude increases, the probability of providing a response becomes higher for the same level of the state variable.

## 8. Robustness Checks

We conduct several robustness checks in this section.

## 8.1. Robustness to Potential Review Manipulation

One may argue that, as an alternative to responding to negative reviews, a firm may opt to engage in review manipulation, for example, by posting fake reviews to self-promote its products or services (Mayzlin et al. 2014). If this occurs, it could pose an identification challenge because the increase in ratings could be confounded under the influence of two forces: management response and review manipulation.

We take two measures to address this concern.<sup>18</sup> First, we conduct a falsification test. The occasion when the firm responds to consumer complaints would indicate a moment in time when the management thinks it needs to take some form of corrective action. If indeed the firm engages in manipulating reviews, this is the time we would expect to see more manipulated reviews in the form of fake positive reviews. It is reasonable to assume that such firm-manufactured reviews will be different from customer-generated ones. If we are able to verify that the positive reviews following a management response do not systematically differ from the rest of the positive reviews, we falsify the significant presence of review manipulation (because, otherwise, we should see a significant difference between these two groups of positive reviews). This can be done through text analytics.

Specifically, we constructed a corpus consisting of all the positive reviews and applied latent dirichlet allocation (Blei et al. 2003) to extract topics from the corpus. We set the number of topics (T) to be 10. We then split all the positive reviews into two groups: those right before a response (group I) and those right after a response (group II). Group I consists of the positive reviews that are within the 10 preceding reviews that are not subject to another response; group II consists of the positive reviews among the 10 reviews after a response that are not subject to the impact of another response. Contrasting these two groups enables us to conduct an event-study type of analysis in which the responses can be regarded as events. We next examine the topic composition (i.e., what topic keywords appeared in a review) in groups I and II separately and then calculate the cosine similarity between the two vectors of keywords. The cosine similarity between positive reviews before and after response is 0.851, indicating high similarity between them. We also varied the number of topics to be 20, and the cosine similarity between positive reviews before and after response is 0.824, still suggesting high similarity. This analysis alleviates the concern that the Ctrip data are contaminated by review manipulation.

Table 11. Average Similarity Scores of Positive Reviews

<table><tr><td>Window size</td><td>Without response</td><td>With response</td><td>p-Value</td></tr><tr><td>20</td><td>0.719 (0.106)</td><td>0.720 (0.112)</td><td>0.947</td></tr><tr><td>10</td><td>0.550 (0.142)</td><td>0.548 (0.120)</td><td>0.852</td></tr></table>

Note. The standard deviation is reported in parentheses.

Alternatively, we calculate another cosine similarity score based on the term frequency-inverse document frequency values (Manning et al. 2008) with window sizes of 10 and 20 in Table 11. The t-tests show that the mean similarity scores from those two groups are not different. The main takeaway of this analysis is that the content of positive reviews does not get significantly affected by a response.

Second, to further address the potential identification concern, we incorporate into our analysis a second data set from Expedia, in which review manipulation is less of a concern. Expedia’s review platform requires authentication of reviewers, and only those customers who have stayed in a hotel are invited to post a review for the hotel. As such, Expedia’s hotel reviews are widely perceived to be free of manipulation (e.g., Mayzlin et al. 2014). We retrieved all the reviews in Expedia for the hotels in the Dallas metropolitan area provided that these hotels have at least 20 reviews and at least one management response to eliminate outliers. This process left us with 136 hotels.

The Expedia data set consists of 58,235 reviews from the period of January 2010 to May 2016. Similar to the Ctrip data set, we retrieved the star rating, review text, review time stamp, and management response if any. Table 12 reports the summary statistics for the Expedia data. The grand mean of reviews across all the hotels is 4.09.

We use the most recent 20 review ratings to construct the state variable $x _ { t }$ and estimate the SDE model by hotel.<sup>19</sup> The estimation results show that most of the estimates for the control parameter α are significant, suggesting that the SDE framework is effective in a setting that is free of manipulation as well. Out of 136 hotels, we observe that 38 of them have negative estimated values of the control parameter. This is intriguing as it suggests that the firms’ responses can have an adverse effect on future review ratings.

Our findings concerning the negative impact of responding to reviews are similar to those of Wang and Chaudhry (2018), who find that responding too often to a positive customer review could backfire. We further drilled down hotel characteristics to examine what types of hotels tend to experience a negative impact of management response. We extracted the following features for a hotel: hotel star rating, hotel affiliation (dummy variable with one for chain affiliated and zero for independent hotels), mean review rating, mean response time, the positive response fraction (the number of responses to positive reviews divided by the number of responses to all reviews), and response ratio (the number of responses divided by the number of reviews) for each hotel. We then ran a simple logistic regression with the sign of α as the dependent variable (label α > 0 as one and α 0 as zero) and hotel characteristics as independent variables. From Table 13, although a higher response ratio in general has a positive impact, a higher fraction of responses to positive reviews is harmful. This is intuitive: holding the number of responses constant, if we direct our efforts more toward positive reviews (rather than negative ones for which a response is perhaps more appropriate), it will likely lower ratings.

Table 12. Summary Statistics for the Expedia Data

<table><tr><td>Review rating</td><td>Number of reviews</td><td>Percentage</td><td>Number of responses</td><td>Fraction with response</td></tr><tr><td>1</td><td>2,641</td><td>4.54%</td><td>423</td><td>16.02%</td></tr><tr><td>2</td><td>3,525</td><td>6.05%</td><td>465</td><td>13.19%</td></tr><tr><td>3</td><td>7,093</td><td>12.18%</td><td>846</td><td>11.93%</td></tr><tr><td>4</td><td>17,856</td><td>30.66%</td><td>1,501</td><td>8.41%</td></tr><tr><td>5</td><td>27,120</td><td>46.57%</td><td>2,405</td><td>8.87%</td></tr><tr><td>Total</td><td>58,235</td><td>100.00%</td><td>5,640</td><td>9.68%</td></tr></table>

Table 13. The Logistic Regression Result

<table><tr><td>Sign of α</td><td>Coefficient</td><td>Standard error</td><td>z-Value</td><td>p-Value</td></tr><tr><td>Response ratio</td><td>1.716</td><td>0.873</td><td>1.97</td><td>0.049</td></tr><tr><td>Hotel star rating</td><td>0.538</td><td>0.323</td><td>1.66</td><td>0.096</td></tr><tr><td>Hotel affiliation</td><td>0.087</td><td>0.634</td><td>0.14</td><td>0.890</td></tr><tr><td>Mean review rating</td><td>-0.329</td><td>0.295</td><td>-1.12</td><td>0.265</td></tr><tr><td>Mean response time</td><td>0.005</td><td>0.005</td><td>1.07</td><td>0.285</td></tr><tr><td>Positive response fraction</td><td>-1.419</td><td>0.659</td><td>-2.15</td><td>0.031</td></tr></table>

We then calculate the measure $\gamma _ { 1 }$ to gauge the impact of a response relative to that of a positive review. We categorize the estimated values of $\gamma _ { 1 }$ by hotel features as shown in Table 14. We observe that the ratio of $\gamma _ { 1 }$ is larger for nonchain, two-star or lower hotels with average rating less than or equal to four. This reveals that responses tend to be more effective for low-end, independent hotels that have relatively low review ratings.

We also replicated the predictive performance analysis on the Expedia data. The results, as measured with RMSE, MAE, and SMAPE, are shown in Tables 15 and 16. The results are qualitatively the same with those of the Ctrip data. As a whole, the SDE method is comparable with ARMA and NM (long term) but outperforms GARCH, MA, ES, and NM (short term).

## 8.2. Additional Comparative Analyses

In our probabilistic response strategy, firms respond to a review with some probability depending on the state of recent review ratings. For higher values of the state, the probability of a response decreases. One might argue that this finding is nonsurprising and the probabilistic strategy (PS) could easily be replaced by a simple threshold strategy (TS) that only responds to reviews in which the rating is low (e.g., one, two, or three) and never responds to moderate or high ratings (e.g., four or five). This prompts us to probe deeper on what value our PS offers beyond the TS.

To make the analysis tractable, we begin with a simple case with a window size of one and analyze the steady-state properties (e.g., mean, standard deviation, and steady-state response probability) under TS and PS. Before response, the review ratings follow the prior distribution F $( p _ { i } , i = 1 , 2 , 3 , 4 , 5 )$ , where $p _ { i }$ is the probability that the review rating equals to i. Once a review receives a response, it will affect the distribution of the next arriving review ratings, denoted by the posterior distribution $F ^ { \prime } \ ( p _ { i } ^ { \prime } , i = 1 , 2 , 3 , 4 , 5 )$ . The probability of responding at time $t \left( q _ { t } \right)$ is the weighted sum of two components: if there was a response at the previous time $( t - 1 )$ , the review arriving at time t will follow the posterior distribution $F ^ { \prime } ;$ otherwise, it will follow the prior distribution F. Thus, we have

Table 14. Relative Impact of Management Response (Expedia Data)

<table><tr><td>Category</td><td>Group</td><td> $\gamma_1$ </td></tr><tr><td rowspan="2">Hotel affiliation</td><td>Nonchain (independent)</td><td>10.9</td></tr><tr><td>Chain</td><td>4.87</td></tr><tr><td rowspan="2">Hotel star rating</td><td>Two-star or lower</td><td>10.31</td></tr><tr><td>Three-star or higher</td><td>2.53</td></tr><tr><td rowspan="2">Mean rating</td><td>Less than or equal to four</td><td>9.70</td></tr><tr><td>Greater than four</td><td>3.44</td></tr></table>

$$
q _ {t} = q _ {t - 1} P ^ {\prime} + (1 - q _ {t - 1}) P.
$$

In this, $P \left( P ^ { \prime } \right)$ represents the probability of responding under prior (posterior) distribution. In steady state, $q _ { t } = q _ { t - 1 } = q$ . After solving the equation, we get the steady-state response probability

$$
q = \frac {P}{(1 + P - P ^ {\prime})}.\tag{11}
$$

The steady-state mean of ratings is calculated by

$$
\mathbb {E} = q \mu^ {\prime} + (1 - q) \mu ,\tag{12}
$$

where $\mu ^ { \prime } = p _ { 1 } ^ { \prime } + 2 p _ { 2 } ^ { \prime } + 3 p _ { 3 } ^ { \prime } + 4 p _ { 4 } ^ { \prime } + 5 p _ { 5 } ^ { \prime }$ and $\mu = p _ { 1 } + 2 p _ { 2 } +$ $3 p _ { 3 } + 4 p _ { 4 } + 5 \bar { p } _ { 5 }$ . The steady-state variance of ratings is computed by

$$
\mathbb {V} = \sum_ {r = 1} ^ {5} q r ^ {2} p _ {r} ^ {\prime} + \sum_ {r = 1} ^ {5} (1 - q) r ^ {2} p _ {r} - (q \mu^ {\prime} + (1 - q) \mu) ^ {2}.\tag{13}
$$

Under PS, the firm adopts a trigger that smoothly decreases with the rating. That is, given the review rating $r ,$ we denote the probability of responding as $g ( r )$ , which is decreasing as rating magnitude increases. Here we consider a linear function form $g ( r ) = k * r + d ,$ where $k < 0$ and $d > 0 .$ . To guarantee a meaningfu probability, we set $g ( r ) = 0 \bar { \big ( } g ( r ) = 1 \big )$ when $g ( r ) < 0$ $\bar { ( } g ( r ) > 1 )$ . Thus, we have

$$
\begin{array}{r l} & P ^ {\prime} (P S) = \sum_ {r = 1} ^ {5} g (r) p _ {r} ^ {\prime} \\ & \qquad = g (1) p _ {1} ^ {\prime} + g (2) p _ {2} ^ {\prime} + g (3) p _ {3} ^ {\prime} + g (4) p _ {4} ^ {\prime} + g (5) p _ {5} ^ {\prime}, \end{array}
$$

Table 15. Comparative Performance Results (Expedia Data): In-Sample and Out-of-Sample

<table><tr><td></td><td>Metric</td><td>SDE</td><td>ARMA</td><td>GARCH</td><td>MA</td><td>ES</td><td>NM</td></tr><tr><td rowspan="3">In-sample</td><td>RMSE</td><td>0.242 (0.0941)</td><td>0.244 (0.0985)</td><td>0.2645 (0.1033)</td><td>0.3435 (0.155)</td><td>0.3434 (0.1553)</td><td>N/A</td></tr><tr><td>MAE</td><td>0.1961 (0.0801)</td><td>0.1974 (0.0831)</td><td>0.2024 (0.0842)</td><td>0.2849 (0.1302)</td><td>0.2849 (0.1301)</td><td>N/A</td></tr><tr><td>SMAPE</td><td>0.1401 (0.0416)</td><td>0.1413 (0.0431)</td><td>0.1443 (0.047)</td><td>0.203 (0.0886)</td><td>0.2052 (0.0948)</td><td>N/A</td></tr><tr><td rowspan="3">Out-of-sample long term</td><td>RMSE</td><td>0.2848 (0.1866)</td><td>0.2912 (0.1965)</td><td>0.4165 (0.3506)</td><td>0.2753 (0.0975)</td><td>0.2771 (0.0986)</td><td>0.3107 (0.2142)</td></tr><tr><td>MAE</td><td>0.234 (0.1635)</td><td>0.2405 (0.1742)</td><td>0.3145 (0.2564)</td><td>0.2309 (0.0881)</td><td>0.2325 (0.0893)</td><td>0.2635 (0.1964)</td></tr><tr><td>SMAPE</td><td>0.1438 (0.0569)</td><td>0.1472 (0.0588)</td><td>0.1755 (0.0755)</td><td>0.1606 (0.1031)</td><td>0.1614 (0.1033)</td><td>0.1547 (0.051)</td></tr><tr><td rowspan="3">Out-of-sample short term</td><td>RMSE</td><td>0.1523 (0.0639)</td><td>0.1618 (0.087)</td><td>0.7016 (1.2117)</td><td>0.1788 (0.0922)</td><td>0.1756 (0.0881)</td><td>0.2501 (0.2011)</td></tr><tr><td>MAE</td><td>0.1263 (0.0538)</td><td>0.1363 (0.0791)</td><td>0.6117 (1.0361)</td><td>0.1546 (0.0829)</td><td>0.1509 (0.0792)</td><td>0.2319 (0.2014)</td></tr><tr><td>SMAPE</td><td>0.0856 (0.0482)</td><td>0.1016 (0.0865)</td><td>0.2273 (0.2266)</td><td>0.1084 (0.0771)</td><td>0.107 (0.0768)</td><td>0.1247 (0.0553)</td></tr></table>

Note. The standard deviation is reported in parentheses.

and

$$
\begin{array}{r l} P (P S) & = \sum_ {r = 1} ^ {5} g (r) p _ {r} \\ & = g (1) p _ {1} + g (2) p _ {2} + g (3) p _ {3} + g (4) p _ {4} + g (5) p _ {5}. \end{array}
$$

TS follows a zero-one trigger (always respond when the rating is less than a threshold value and otherwise not respond). For example, the firm always responds when the arriving review rating is less than or equal to two and otherwise does not respond. Therefore, we have $P ^ { \prime } ( T S ) = p _ { 1 } ^ { \prime } + p _ { 2 } ^ { \prime }$ and $P ( T S ) = p _ { 1 } + p _ { 2 }$

Based on this analysis, we conduct several comparisons. Under TS, the threshold can only take on values of one, two, three, four, or five because the ratings are discrete ranging from one to five. However, PS is more flexible because the probability of responding g r can accommodate any functional form. Next, we provide a numerical example to illustrate. We assume a prior distribution $( p _ { 1 } = 0 . 1 , p _ { 2 } = 0 . 2 , p _ { 3 } = 0 . 2 , p _ { 4 } = 0 . 4 , p _ { 5 } = 0 . 1 )$ and a posterior distribution $( p _ { 1 } ^ { \prime } = 0 . 0 2 , p _ { 2 } ^ { \prime } = 0 . 0 5 , p _ { 3 } ^ { \prime } = 0 . 0 8 ,$ $p _ { 4 } ^ { \prime } = 0 . 2 , p _ { 5 } ^ { \prime } = 0 . 6 5 )$ . Let us assume that the firm wants to achieve a target mean of 3.45. Under PS, the firm can use the response strategy given by $g ( r _ { t } ) = - 0 . 4 1 * r _ { t } + 1 . 3 9 ,$ corresponding (exactly) to the target mean of 3.45 (Equation (12)). We can calculate the steady-state variance of ratings to be 1.51 using Equation (13) and the steady-state response probability (q) to be 20.62% using Equation (11). Under TS, the firm can only choose a threshold that achieves a steady-state mean closest to the target mean. This threshold is two, the value that achieves a steady-state mean of 3.5 (closest to the target mean of 3.45). On the other hand, if a threshold value of one is chosen, the steady-state mean is 3.31, further away from the target mean of 3.45. The threshold value of two yields a variance of 1.53 and a steady-state response probability of 24.39%. In this example, we see that PS has lower variance and is more efficient (lower steady-state response probability) than TS.

When the window size n is greater than one (e.g., 20), the analysis becomes more complicated, and thus, simulation is used to investigate how the state evolves over time. The state variable $x _ { t }$ at time t is no longer equal to $\boldsymbol { r } _ { t } ,$ but will absorb the newly arriving review $r _ { t }$ at time t. We simulate N 10, 000 trajectories to smooth the randomness, and the time horizon is from t 1 to

Table 16. Paired t-Test Results (Expedia Data): In-Sample and Out-of-Sample

<table><tr><td>Metric</td><td>Comparison</td><td>In-sample</td><td>Out-of-sample long term</td><td>Out-of-sample short term</td></tr><tr><td rowspan="5">RMSE</td><td>SDE versus ARMA</td><td>-0.162 (0.871)</td><td>-0.613 (0.54)</td><td>-1.018 (0.31)</td></tr><tr><td>SDE versus GARCH</td><td>-3.914*** (0.000)</td><td>-5.616*** (0.000)</td><td>-6.769*** (0.000)</td></tr><tr><td>SDE versus MA</td><td>-6.812*** (0.000)</td><td>0.684 (0.494)</td><td>-1.908* (0.057)</td></tr><tr><td>SDE versus ES</td><td>-6.85*** (0.000)</td><td>0.723 (0.47)</td><td>-1.623* (0.100)</td></tr><tr><td>SDE versus NM</td><td>N/A</td><td>-1.07 (0.285)</td><td>-5.579*** (0.000)</td></tr><tr><td rowspan="5">MAE</td><td>SDE versus ARMA</td><td>-0.081 (0.936)</td><td>-0.626 (0.532)</td><td>-1.269 (0.205)</td></tr><tr><td>SDE versus GARCH</td><td>-2.263** (0.024)</td><td>-5.205*** (0.000)</td><td>-6.984*** (0.000)</td></tr><tr><td>SDE versus MA</td><td>-7.129*** (0.000)</td><td>0.981 (0.327)</td><td>-2.51** (0.013)</td></tr><tr><td>SDE versus ES</td><td>-7.183*** (0.000)</td><td>1.019 (0.309)</td><td>-2.148** (0.032)</td></tr><tr><td>SDE versus NM</td><td>N/A</td><td>-1.433 (0.153)</td><td>-6.366*** (0.000)</td></tr><tr><td rowspan="5">SMAPE</td><td>SDE versus ARMA</td><td>-0.359 (0.72)</td><td>-0.865 (0.388)</td><td>-1.501 (0.134)</td></tr><tr><td>SDE versus GARCH</td><td>-2.024** (0.044)</td><td>-5.306*** (0.000)</td><td>-8.961*** (0.000)</td></tr><tr><td>SDE versus MA</td><td>-6.627*** (0.000)</td><td>-1.838* (0.067)</td><td>-1.952* (0.052)</td></tr><tr><td>SDE versus ES</td><td>-6.661*** (0.000)</td><td>-1.883* (0.061)</td><td>-1.645* (0.101)</td></tr><tr><td>SDE versus NM</td><td>N/A</td><td>-1.407 (0.161)</td><td>-5.688*** (0.000)</td></tr></table>

Note. The p-value is reported in parentheses.  
\*\*\*p 0.01; \*\*p 0.05; \*p 0.10.

T <sub></sub> 2, 000 in each trajectory. The values of the prior and posterior distributions are the same as when the window size equals to one. From t <sub></sub> 1 to t <sub></sub> 20, we draw $r _ { t }$ from the prior distribution to construct the initial state. From $t = \bar { 2 } 1$ , the distribution of arriving reviews at time t depends on whether there was a response at previous time t 1 . If there was a response at time t 1 , we draw $r _ { t }$ from the posterior distribution and otherwise from the prior distribution.

Let us assume that the firm wants to achieve a target mean of 3.8. Under PS, the firm can use the response strategy given by $g ( x _ { t } ) = - 0 . 9 5 * x _ { t } + 4 . 0 8 ,$ corresponding (exactly) to the target mean of 3.8. Under PS, we observe the steady-state variance of ratings to be 0.036 and the steady-state response probability (q) to be 48.02%. Under TS, the firm can only choose a threshold that achieves a steady-state mean closest to the target mean. This threshold is four, the value that achieves a steady state mean of 3.9 (closest to the target mean of 3.8). On the other hand, if a threshold value of three is chosen, the steady-state mean is 3.65, further away from the target mean of 3.8. The threshold value of four yields a variance of 0.04 and a steady-state response probability of 57.49%. Once again, we see that PS has lower variance and is more efficient (lower steady-state response probability) than TS.

In practice, firms may often consider a simple response strategy (such as TS) to achieve their desired control objectives. However, as we have shown, a fundamental difference between PS and TS is that PS is a more flexible strategy and can precisely achieve the target set by the firm. This target could be the mean (mean control) or a more sophisticated target, such as the combination of the mean and variance (mean-variance control) or even a target that is stated in terms of the probability of the state variable (service-level control). In our simulation, we provided examples of cases in which TS has a higher variance than PS (also a higher steady-state response probability). This may not always hold for all parameter settings. The important takeaway regarding the issue of PS versus TS is that TS, because of its discrete nature, may not be able to precisely meet the control objectives of the firm.

## 9. Model Extension: Multidimensional Strategy

We further extend our model by incorporating additional information (beyond review rating) that can guide the response strategy. This enriched model provides new practical insights that are more prescriptive.

Without loss of generality, we extend our one-state model to a composite, two-state model. To do so, we construct a composite variable that is a weighted combination of two states: the sentiment of a review together with the review rating. The sentiment in a review (S ) is obtained by text mining the review text, which is elaborated in Online Appendix 1. A composite state is constructed as $Z _ { t } = w _ { 1 } \bar { X _ { t } } + w _ { 2 } S _ { t }$ . The weights $w _ { 1 }$ and $w _ { 2 }$ are determined using logistic regression with the binary response event as the dependent variable. The independent variables are the rating and the sentiment. We run the logistic regression for each tour and check whether ratings and sentiments are significant factors for evoking a response. If both coefficients are significant, we refer to the tour as a Z-strategy tour (treatment group). If only the ratings variable is significant, the tour is said to adopt an X-strategy (control group). The situation in which only the sentiment is significant can be handled in a similar manner; however, in our context, such a situation rarely arose. Hence, we do not consider this situation.

Next, we investigate the impact of the response strategy (Z or X) on the review ratings and sentiments of tours. We first use PSM to match tours based on observed tour characteristics, which are the same with what we have defined in the quasi-experiment in Online Appendix 2. We run a Probit model to match the treated and control tours based on their predicted propensity scores. The Probit model results are shown in Table 17. We use nearest neighbor matching with replacement; the PSM yields 54 tours in the treatment group and 63 tours in the control group. We focus on those pairs (matched tours) in which tour one adopts a Z-strategy (treatment) and the other adopts an X-strategy (control). We further check whether the covariates of the matched treated and control tours are balanced. Table 18 shows that, after matching, the tour characteristics are comparable. For each tour, we consider six outcomes of a response strategy: mean rating, standard deviation of rating, the proportion of very low ratings (equal to one, the lowest possible rating), mean sentiment, the standard deviation of sentiment, and the proportion of very low sentiments (equal to one, the lowest possible sentiment).<sup>20</sup>

Table 19 reports the average treatment effect for each outcome. We see that the X-strategy performs better than the Z-strategy based upon rating-related outcomes. Specifically, the X-strategy has a mean rating that is about 0.1 higher or about 2% higher. This difference might seem small; however, industry reports on lodging indicate that small differences indeed matter to revenue. For example, according to industry reports on lodging performance, a 1% reputation improvement results in a 1.42% increase in revenue per available room (Anderson 2012). On the other hand, the Z-strategy does better on sentiment-related outcomes (almost the same mean sentiment but lower standard deviation of the sentiment and smaller proportion of very low sentiments). Thus, neither strategy dominates. Our model and analyses permit a firm to study various response strategies to choose the one that best suits management goals. Adding an additional variable in our SDE model has demonstrated the power and flexibility of the SDE approach. Furthermore, the specific two-dimensional example used in the demonstration has generated insights that are more prescriptive as it factors in the nature of the review text.

Table 17. Probit Regression of Response Strategies

<table><tr><td>Treatment</td><td>Coefficient</td><td>Standard error</td><td>z-Value</td><td>p-Value</td></tr><tr><td>Length</td><td>-0.105</td><td>0.145</td><td>-0.730</td><td>0.468</td></tr><tr><td>Flexibility</td><td>-0.487</td><td>0.570</td><td>-0.850</td><td>0.393</td></tr><tr><td>Departure</td><td>-0.481</td><td>0.487</td><td>-0.990</td><td>0.324</td></tr><tr><td>Destination</td><td>0.076</td><td>0.255</td><td>0.300</td><td>0.767</td></tr><tr><td>Agent</td><td>0.180</td><td>0.928</td><td>0.190</td><td>0.846</td></tr><tr><td>Transportation</td><td>1.048</td><td>0.644</td><td>1.630</td><td>0.104</td></tr><tr><td>Type</td><td>-0.184</td><td>0.298</td><td>-0.620</td><td>0.538</td></tr><tr><td>Hotel</td><td>-0.156</td><td>0.252</td><td>-0.620</td><td>0.535</td></tr><tr><td>Price</td><td>-0.077</td><td>0.294</td><td>-0.260</td><td>0.794</td></tr><tr><td>Age</td><td>2.207</td><td>0.890</td><td>2.480</td><td>0.013</td></tr><tr><td>Intercept</td><td>-70.043</td><td>38.188</td><td>-1.830</td><td>0.067</td></tr><tr><td>Number of observations</td><td>117</td><td></td><td></td><td></td></tr><tr><td>LR chi $^{2}$ (11)</td><td>51.93</td><td></td><td></td><td></td></tr><tr><td>Probit &gt; chi $^{2}$ </td><td>0.000</td><td></td><td></td><td></td></tr><tr><td>Log-likelihood</td><td>-54.789</td><td></td><td></td><td></td></tr></table>

## 10. Conclusions

This paper studies the problem of managing online customer opinions using management response strategy. Toward this end, we develop a stochastic differential equation model to study the evolution of user opinions over time. The model incorporates a control strategy into firm response to user reviews and investigates the impact of the responses on review ratings. The model is empirically estimated using data on firm responses and online customer reviews for two of the world’s largest travel agents. The model is validated along different dimensions of its performance. First, the predicted steady-state mean obtained from the model is compared with the observed steady-state mean inferred directly from the data. We then demonstrate the superiority of our SDE model by examining its predictive performance compared with benchmark models, including ARMA, GARCH, MA, ES, and NM. Our approach achieves superior or comparable predictive performance with those benchmark models. We further provide an operational interpretation of the control by mapping it to an equivalent probabilistic response strategy. Then, we demonstrate the applicability of the probabilistic response policy under different control objectives, namely mean control, mean-variance control, and service-level control.

Finally, we enrich our model by incorporating additional information (review sentiment) garnered from the review text. This enables the firm to embrace a multidimensional response strategy. It also provides practical insights that are more prescriptive as the firm can react to the change of environment along multiple dimensions.

The main contributions of the paper are twofold. Recent research shows that publicly responding to user comments can increase online reputation. However, although predictive models of review ratings exist, there are no prescriptive models that recommend the best response strategy to decision makers to achieve a specific managerial goal. We believe what we offer in this study is a significant first step toward a prescriptive response strategy. From a methodological perspective, the stochastic differential equation approach presented here opens the black box of the data-generating process underlying review data as opposed to reduced-form models that essentially stop at estimation or prediction. Compared with other structural models, a key distinction of our approach is that we model the stochastic, timeseries nature of the review data-generating process. Most other structural approaches have emphasized a utility framework to understand the process of data generation.

Table 18. Balance Check Before and After Matching

<table><tr><td></td><td>Mean difference before matching</td><td>After matching</td><td>p-Value from t-test before matching</td><td>After matching</td></tr><tr><td>Length</td><td>0.803</td><td>-1.093</td><td>0.046</td><td>0.171</td></tr><tr><td>Flexibility</td><td>-0.209</td><td>-0.167</td><td>0.012</td><td>0.202</td></tr><tr><td>Departure</td><td>0.061</td><td>-0.111</td><td>0.253</td><td>0.282</td></tr><tr><td>Destination</td><td>0.056</td><td>0.185</td><td>0.345</td><td>0.276</td></tr><tr><td>Agent</td><td>-0.074</td><td>-0.042</td><td>0.022</td><td>0.154</td></tr><tr><td>Transportation</td><td>0.188</td><td>-0.056</td><td>0.022</td><td>0.394</td></tr><tr><td>Type</td><td>-0.497</td><td>0.296</td><td>0.017</td><td>0.269</td></tr><tr><td>Hotel</td><td>0.690</td><td>0.083</td><td>0.016</td><td>0.452</td></tr><tr><td>Price</td><td>788.675</td><td>668.241</td><td>0.004</td><td>0.166</td></tr><tr><td>Age</td><td>0.138</td><td>-0.015</td><td>0.000</td><td>0.421</td></tr></table>

Table 19. Performance of X-strategy and Z-strategy

<table><tr><td>Variable</td><td>Z-Strategy</td><td>X-Strategy</td><td>Difference</td><td>Standard error</td><td>p-Value</td></tr><tr><td>Mean rating</td><td>4.536</td><td>4.638</td><td>-0.102</td><td>0.044</td><td>0.012</td></tr><tr><td>Mean standard deviation (rating)</td><td>0.697</td><td>0.649</td><td>0.049</td><td>0.031</td><td>0.060</td></tr><tr><td>Proportion of ratings equal to one</td><td>1.082%</td><td>0.603%</td><td>0.005</td><td>0.003</td><td>0.043</td></tr><tr><td>Mean sentiment</td><td>3.558</td><td>3.592</td><td>-0.034</td><td>0.024</td><td>0.085</td></tr><tr><td>Mean standard deviation (sentiment)</td><td>0.451</td><td>0.491</td><td>-0.040</td><td>0.018</td><td>0.018</td></tr><tr><td>Proportion of sentiments equal to one</td><td>0.011%</td><td>0.222%</td><td>-0.002</td><td>0.001</td><td>0.000</td></tr><tr><td>Response ratio</td><td>0.068</td><td>0.069</td><td>-0.001</td><td>0.015</td><td>0.464</td></tr></table>

From an operational (or practical) perspective, our study offers specific guidelines (via a probabilistic strategy) on managing user opinions through controlled responses. A full response strategy—one that responds to every review—will likely be too costly or ineffective if the responses are not adequate. The cost of responding can be material, for example, the personnel costs for the assigned staff to manually respond to reviews. It is also costly to train people to investigate and professionally respond to reviews and effectively manage customer relationships. However, even if the cost of responding is ignored, it may still be better not to respond to every review because a full-response strategy may trigger opportunistic behavior from some consumers. For example, it is common for firms to send out coupons to unsatisfied consumers. If coupons were sent out for every negative comment, this practice could encourage some opportunistic consumers to deliberately post negative reviews even if they were, in fact, satisfied with the product or service. Thus, responding to every review may backfire and incur additional cost. Further, as we demonstrated, our probabilistic response strategy is more flexible than the simple threshold strategy.

Using our model, managers can fine-tune the response strategy to achieve a desired outcome, such as mean control, mean-variance control, or service-level control. Of these, the last two goals can only be achieved if the predictive model can recover the distribution of the review ratings as a function of the response strategy used by the firm.

This study has several limitations. The response strategy considered in this paper is a first attempt at constructing a prescriptive model on this subject. In general, a response strategy could include the dimensions of what, when, and how. The “what” aspect of a strategy answers the question of what review the firm should respond to. The “when” aspect of a strategy relates to the issue of delay; that is, should the response be immediate or delayed. A delayed response is likely to be less effective but, at the same time, less costly to implement. Finally, the “how” aspect of a strategy is associated with how the actual response is constructed. Clearly, all dimensions of a response strategy are important. However, our study was limited to one dimension, namely it provided insight into what review merited a response. We believe that the other dimensions of a response strategy (i.e., the when and the how) are fruitful directions for future work.

Another aspect of designing a response strategy is to allow the impact of responding to a positive review to be different from that of responding to a negative review. In our study, we did not distinguish between these impacts. However, the SDE framework lends itself well to models in which different response strategies for positive and negative reviews can be jointly optimized. This is a promising direction for future work.

Our model of the impact of a negative review (see Equation (1)) is linear in nature. However, this impact may be nonlinear in some situations. For example, one possible nonlinear model is one in which a negative review has less impact at low values and at high values of the state. That is, the maximum impact of a negative review occurs at some intermediate value of the state. In an inverted-U impact curve, firms would have little incentive to operate in the increasing portion of the curve. This is because the impact of a negative review at a point in the increasing portion of the curve is the same as the impact at a corresponding point in the decreasing portion of the curve where the rating is much higher. Further, if a firm could successfully drive its ratings to a very high value, it would have to do very little to maintain its ratings at this high value. Thus, in an inverted U-model of impact, one should expect to see many firms with ratings close to the maximum value of the range. In general, the manner in which the current state moderates the impact of a negative review can profoundly affect the response strategy. A study of nonlinear models of impact is, therefore, a useful direction for future work. Finally, competition is not modeled: the behavior or strategy of competing firms would be likely to influence the focal firm’s response strategy as well. We are currently exploring these possibilities.

## Acknowledgments

The authors gratefully acknowledge the feedback received from the senior editor, the associate editor, and anonymous reviewers. They thank the seminar participants at Georgia State University and The University of Texas at Dallas as well as participants at the 2016 POMS Conference and the 2017 CSWIM Workshop.

## Endnotes

<sup>1</sup> We hereafter use consumers’ perception of quality interchangeably with the notion of customer value proposition in the marketing literature (Anderson et al. 2006) that describes the overall experience that potential consumers could have after purchasing the product.

<sup>2</sup> In this study, we set the sliding window size n 20. This is a reasonable choice for our data given the fact that there were 10 reviews displayed on a page and that most users do not browse more than two pages of reviews (Pavlou and Dimoka 2006). We also experimented with different window sizes (e.g., n 10), and the results remained qualitatively the same as shown in Online Appendix 5.

<sup>3</sup> The ordering by time is the default setting in the review page.

<sup>4</sup> We validate our Poisson process assumption and other modeling assumptions in Section 5.

<sup>5</sup> The URL is http://vacations.ctrip.com/grouptravel/p93390s0-comment .html (last accessed on October 20, 2017).

<sup>6</sup> Alternatively, if we were to relabel a rating of four as positive (instead of negative) and ratings of one, two, or three as negative, the estimates for the various parameters would be affected. However, the predictive performance of the SDE approach and the response strategy remain largely unaffected.

<sup>7</sup> In Online Appendix 1, we describe how to calculate content similarity from the review texts.

<sup>8</sup> Later in Section 7, in which we discuss the service-level control, we map P x d to P 2cy 2c 5 d so that we are able to directly use the formula (cumulative distribution function) of noncentral chisquared distribution to calculate the probability.

<sup>9</sup> Note that the density is heavily left concentrated with a long tail on the right end. So the relative misfit on the long tail part carries less weight.

<sup>10</sup> As a contrast, Theil’s U index for the normal distribution is 0.18 for the case of interarrival time and is 0.1336 for the case of negative interarrival time.

<sup>11</sup> For each tour after the first response, we use the first 70% as in sample and the remaining data as out of sample.

<sup>12</sup> We conduct robustness checks by choosing m equal to 3 and 10, and the results are qualitatively the same.

<sup>13</sup> The coefficient estimates for the ARMA and GARCH models are presented in Online Appendix 6.

<sup>14</sup> The detailed information about the estimated and observed means for each tour as well as detailed in-sample and out-of-sample RMSE, MAE, and SMAPE are reported in Online Appendix 4.

<sup>15</sup> To make the measurement more robust, we consider multiple (randomly picked) starting states and find an average measure of predictive performance across these starting states.

<sup>16</sup> We also conduct the (nonparametric) Wilcoxon rank sum test that does not require any distribution assumptions, and the results are consistent.

<sup>17</sup> We conducted more formal analysis to test the fit. The correlation between the observed probability and fitted probability is 0.859. Then we run a regression with observed probabilities as the dependent variable and fitted probability as the independent variable. This results in a coefficient of 0.71 (significant at the 0.01 level). The R<sup>2</sup> is 0.74 with an F-statistic 22.46 ( p 0.0015). All these statistics show

a reasonably good fit although the observed probability does not vi sually appear to match the fitted probability very well.

<sup>18</sup> We thank the anonymous associate editor and reviewers for this suggestion.

<sup>19</sup> The detailed parameter estimation results for each of the 136 hotels are available upon request.

<sup>20</sup> We normalize the sentiment score from one to five, the same scale with ratings.

## References

Anderson CK (2012) The impact of social media on lodging performance. Cornell Hospitality Rep. 12(15):6–11

Anderson CK, Han S (2016) Hotel performance impact of sociall engaging with consumers. Cornell Hospitality Rep. 16(10):3–9.

Anderson ET, Simester DI (2014) Reviews without a purchase: Low ratings, loyal customers, and deception. J. Marketing Res. 51(3): 249–269.

Anderson JC, Narus JA, Van Rossum W (2006) Customer value propositions in business markets. Harvard Bus. Rev. 84(3):1–8.

Anderson M, Magruder J (2012) Learning from the crowd: Regression discontinuity estimates of the effects of an online review data base. Econom. J. 122(563) 957–989.

Banjo S (2012) Firms take online reviews to heart. Wall Street Journal (July 29), http://www.wsj.com/articles/SB1000142405270230329 2204577517394043189230?cb=logged0.448628765065223.

Bazaarvoice (2013) The conversation index. Accessed December 11, 2018, http://media.dmnews.com/documents/55/conversation\_ index\_vol\_6\_13511.pdf.

Black F, Scholes M (1973) The pricing of options and corporate liabilities. J. Political Econom. 81(3):637–654.

Blei DM, Ng AY, Jordan MI (2003) Latent dirichlet allocation. J. Machine Learn. Res. 3(January):993–1022

Box GEP, Jenkins GM, Reinsel GC, Ljung GM (2015) Time Series Analysis: Forecasting and Control (John Wiley & Sons, Hoboken, NJ)

BrightLocal (2015) Local consumer review survey. Accessed April 25, 2016, https://www.brightlocal.com/learn/local-consumer-review -survey/.

Brown RG (2004) Smoothing, Forecasting and Prediction of Discrete Time Series (Prentice Hall, Englewood Cliffs, NJ)

Cairns AJG (2004) Interest Rate Models: An Introduction (Princeton University Press, Princeton, NJ)

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Chevalier JA, Dover Y, Mayzlin D (2018) Channels of impact: Use reviews when quality is dynamic and managers respond. Marketing Sci. 37(5):688–709.

Cox JC, Ingersoll JE, Ross SA (1985) A theory of the term structure of interest rates. Econometrica 53(2):385–407.

De Gooijer JG, Hyndman RJ (2006) 25 years of time series forecasting Internat. J. Forecasting 22(3):443–473.

Dellarocas C (2006) Strategic manipulation of internet opinion forums: Implications for consumers and firms. Management Sci. 52(10):1577–1593.

DeMers J (2014) How one hotel ruined its reputation by penalizing negative reviews. Forbes (November 3), https://www.forbes .com/sites/jaysondemers/2014/11/03/how-one-hotel-ruined-its -reputation-bv-penalizing-negative-reviews/#314785184806

Dixit AK, Pindyck RS, Pindyck RS (1994) Investment Under Un certainty (Princeton University Press, Princeton, NJ)

Duan W, Gu B, Whinston AB (2008) The dynamics of online word-ofmouth and product sales—An empirical investigation of the movie industry. J. Retailing 84(2):233–242.

Engle RF (1982) Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation. Econo metrica 50(4):987–1007.

Feller W (1951) Two singular diffusion problems. Ann. Math. 54(1):173–182.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3):291–313.

Fornell C, Wernerfelt B (1988) A model for customer complaint management. Marketing Sci. 7(3):287–298.

Gartner (2012) Gartner says by 2014, 10–15 percent of social media reviews to be fake, paid for by companies. Accessed October 6, 2015, http://www.gartner.com/newsroom/id/2161315.

Gesenhues A (2013) Survey: 90% of customers say buying decisions are influenced by online reviews. Accessed October 6, 2015, https://marketingland.com/survey-customers-more-frustrated -by-how-long-it-takes-to-resolve-a-customer-service-issue-than-the -resolution-38756.

Gu B, Ye Q (2014) First step in social media: Measuring the influence of online management responses on customer satisfaction. Production Oper. Management 23(4):570–582.

Gunarathne P, Rui H, Seidmann A (2018) When social media delivers customer service: Differential customer treatment in the airline industry. MIS Quart. 42(2):489–520.

Hazewinkel M, ed. (2002) Encyclopedia of Mathematics (Kluwer Aca demic, Boston).

Ho YC, Wu J, Tan Y (2017) Disconfirmation effect on online rating behavior: A structural model. Inform. Systems Res. 28(3):626–642.

Hurst HE (1951) Long-term storage capacity of reservoirs. Trans. Amer. Soc. Civil Engrg. 116(1):770–799.

Jabr W, Zheng Z (2014) Know yourself and know your enemy: An analysis of firm recommendations and consumer reviews in a competitive environment. MIS Quart. 38(3):635–654.

Keane MP (2010) Structural vs. atheoretic approaches to econometrics. J. Econometrics 156(1):3–20.

Kumar N, Qiu L, Kumar S (2019) Exit, voice, and response in digital platforms: An empirical investigation of online management response strategies. Inform. Systems Res. Forthcoming.

Lee YJ, Xie K, Besharat A (2016) Management response to online WOM: Helpful or detrimental? Proc. Americas Conf. Inform. Systems, San Diego.

Li L, Tadelis S, Zhou X (2016) Buying reputation as a signal of quality: Evidence from an online marketplace. NBER Working Paper No. 22584, National Bureau of Economic Research, Cambridge, MA.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Luca M (2011) Reviews, reputation, and revenue: The case of Yelp. com. Working Paper (12–016), Harvard Business School NOM Unit, Boston.

Luca M, Zervas G (2016) Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Sci. 62(12):3412–3427.

Ma L, Sun B, Kekre S (2015) The squeaky wheel gets the grease—An empirical analysis of customer voice and firm intervention on Twitter. Marketing Sci. 34(5):627–645.

Manning CD, Raghavan P, Schutze H (2008) Scoring, term weighting, and the vector space model. Introduction to Information Retrieva (Cambridge University Press, Cambridge, UK).

Mayzlin D (2006) Promotional chat on the internet. Marketing Sci. 25(2):155–163.

Mayzlin D, Dover Y, Chevalier J (2014) Promotional reviews: An empirical investigation of online review manipulation. Amer. Econom. Rev. 104(8):2421–2455.

Medallia (2015) Responding to social media boosts a company’s bottom line, new research finds. Accessed November 13, 2017, https://www.medallia.com/press-release/responding-social -media-boosts-companys-bottom-line-new-research-finds/.

Merchant KA (1982) The control function of management. Sloan Management Rev. 23(4):43–55.

Moe WW, Schweidel DA (2012) Online product opinions: Incidence, evaluation, and evolution. Marketing Sci. 31(3):372–386.

Pavlou PA, Dimoka A (2006) The nature and role of feedback text comments in online marketplaces: Implications for trust build ing, price premiums, and seller differentiation. Inform. Systems Res. 17(4):392–414.

Poterba JM, Summers LH (1988) Mean reversion in stock prices: Evidence and implications. J. Financial Econom. 22(1):27–59.

Proserpio D, Zervas G (2017) Online reputation management: Esti mating the impact of management responses on consumer re views. Marketing Sci. 36(5):645–665.

Ross SM (2014) Introduction to Probability Models (Academic Press, Cambridge, MA).

Rushe D (2013) Fake online reviews crackdown in New York sees 19 companies fined. The Guardian (September 23), https://www .theguardian.com/world/2013/sep/23/new-york-fake-online -reviews-yoghurt.

Shreve SE (2004) Stochastic Calculus for Finance (Springer, New York).

Theil H (1966) Applied Economic Forecasting (North Holland Publishing Company, Amsterdam).

TripAdvisor (2012) Survey finds half of TripAdvisor users will not book a hotel that has no reviews. Accessed November 13, 2017, http://ir.tripadvisor.com/news-releases/news-release-details survey-finds-half-tripadvisor-users-will-not-book-hotel-has-no

Wang Y, Chaudhry A (2018) When and how managers’ responses to online reviews affect subsequent reviews. J. Marketing Res. 55(2): 163–177.

Ye S, Gao G, Viswanathan S (2014) Strategic behavior in online reputation systems: Evidence from revoking on ebay. MIS Quart. 38(4):1033–1056.
