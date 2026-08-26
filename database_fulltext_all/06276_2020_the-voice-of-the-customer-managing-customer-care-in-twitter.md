---
otero_id: 6276
otero_key: "A2SXVEWB"
title: "The Voice of the Customer: Managing Customer Care in Twitter"
authors: "Reza Mousavi; Monica Johar; Vijay S. Mookerjee"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0889"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.235.66.10] On: 17 June 2020, At: 12:49 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/A2SXVEWB/fulltext/images/f841568896bb0edf9ad9ca655a1be8ae1f46b596b70df435c66fe7dd2dfe1872.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# The Voice of the Customer: Managing Customer Care in Twitter

Reza Mousavi, Monica Johar, Vijay S. Mookerjee

To cite this article: Reza Mousavi, Monica Johar, Vijay S. Mookerjee (2020) The Voice of the Customer: Managing Customer Care in Twitter. Information Systems Research

Published online in Articles in Advance 15 Jun 2020

https://doi.org/10.1287/isre.2019.0889

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Voice of the Customer: Managing Customer Care in Twitter

Reza Mousavi,<sup>a</sup> Monica Johar,<sup>b</sup> Vijay S. Mookerjee<sup>c</sup>

<sup>a</sup> Information Technology Area, McIntire School of Commerce, University of Virginia, Charlottesville, Virginia 22904; <sup>b</sup> Belk College of Business, University of North Carolina at Charlotte, Charlotte, North Carolina 28223; <sup>c</sup> Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080

Contact: rm6uz@comm.virginia.edu, https://orcid.org/0000-0002-1990-7767 (RM); msjohar@uncc.edu,

https://orcid.org/0000-0003-3903-6804 (MJ); vijaym@utdallas.edu, https://orcid.org/0000-0001-5583-3585 (VSM)

Received: August 18, 2018<sub>Revised:</sub> Accepted: Published Online in Articles in Advance: June 15, 2020

https://doi.org/10.1287/isre.2019.088

Copyright:

Abstract. In recent years, managing customer sentiment—particularly on social media— has become crucial as more customers use social media to seek help from firms. Therefore we strive to determine an optimal strategy to manage customer sentiment on social media sites such as Twitter. We also aim to identify factors and external events that can influence the effectiveness of customer care. To understand the antecedents of digital customer care, we model a diffusion process of customer sentiment over time. This diffusion process is influenced (or controlled) by the firm through the strategy employed to respond to customer tweets. We then use real data consisting of sentiments expressed by customers directed at Twitter’s service accounts of four major U.S. telecommunication-service providers (AT&T, Verizon, Sprint, and T-Mobile) to estimate the parameters in our analytical model and shed several insights into digital customer care in this industry. First, we find a clear separation among the firms in terms of digital customer care effectiveness Second, we find that good customer care is not merely a matter of responding to customer tweets. Third, the quality of digital customer care that customers expect varies across firms: Customers of higher priced firms (e.g., Verizon and AT&T) expect better customer care. Fourth, seemingly unrelated events (such as signing an exclusive contract with a celebrity) can impact digital customer care. Our study has important implications for managers as it can help firms determine the optimal strategy to influence customer sentiment.

History: Ram Gopal, Senior Editor; Juan Feng, Associate Editor. Supplemental Material: The appendices are available as an e-companion at https://doi.org/10.1287 isre.2019.0889.

Keywords: digital customer care • customer sentiment • stochastic differential equations • forecasting • Twitter • sentiment analysis

## 1. Introduction

Given the proliferation of Web 2.0 technology, customers are able to communicate with firms through new channels of communication such as social media websites. According to Power (2013), almost twothirds of customers have used a company’s social media site to receive service. Such digitally provisioned service is attractive to customers due to its fast response, and is being increasingly preferred to more traditional service channels such as phone or email (Frumkin 2017). Firms, too, have an incentive to embrace service provision through social media. According to Hyken (2016), the average cost of a servicerelated response in Twitter is \$1, whereas the average cost of interacting with a customer through a traditional call center can be close to \$6. Furthermore, firms that use Twitter as a social care channel are seeing a 19% increase in customer satisfaction. Given that digital customer care has mutual benefits for firms and customers, it is not surprising to observe a 250% increase in customer service interactions over Twitter over the past few years (Frumkin 2017).

Although there are significant benefits of digital customer care management, it imposes certain challenges. The communication between firms and customers is public. Therefore, a firm’s response to a customer’s query could impact not only the focal customer but also other existing and potential customers. This, of course, can also be regarded as a key benefit of digital customer care, namely, that a response to one customer could potentially benefit other customers. However, it is important for firms to devise a response strategy that adequately addresses customers queries in social media. Gunarathne et al. (2017) show some evidence that firms strategically respond to customers’ queries. In particular, their study suggests that firms tend to provide a more satisfactory response to customers who are more influential in social networking websites.

Numerous examples in Twitter provide evidence that a failure to promptly respond to customers on social media may prove disastrous. For instance, when British Airways waited eight hours to respond to a dissatisfied customer, the customer’s tweet went viral rapidly disseminating negative sentiment about the airline. The ineffective response not only aggravated the focal customer, but also made the treatment observable to other social media users (social media bystanders). In another example, American Airlines responded with an automated “Thank You for Your Support” tweet to a Twitter user’s negative tweet, giving the impression that the airline’s responses are perfunctory and automatic, rather than carefully constructed to resolve customers’ problems (J.D. Power 2013).

These examples, along with many others, indicate that customers will continue to use social media channels to communicate with firms, and it is up to firms to respond effectively. According to Power (2013) “consumer expectations for social interactions vary across industries, although quality content and responsive service representatives are keys to higher satisfaction levels.” Therefore, we explore the question: What is an optimal response strategy for digital customer care management?

To answer this question, we develop a controlled diffusion model of customer sentiment. This model is a stochastic differential equation (SDE) that describes the dynamics of customer sentiment driven by the response strategy used by the firm. The control objectives of the firm are explicitly modeled to capture how a firm should optimally react to customer sentiment. We recover the parameters of this controlled diffusion process using maximum likelihood estimation (MLE) and data on social media customer care. This data were collected from Twitter’s service accounts of the Big Four telecommunications firms in the United States (AT&T, Verizon, Sprint, and T-Mobile). Sentiment analysis was used to measure customer sentiment over time for each firm during a fourmonth period. To lend credibility to our structural model, we compared the predictive performance of the diffusion model with state-of-the-art forecasting methods and found that our proposed model outperforms these models.

The main advantage of our approach is not just its predictive ability, but also its ability to prescribe an optimal response strategy for effective digital customer care management. There are several useful insights gleaned from this study. First, we find that there is a clear separation among the firms in terms of digital care effectiveness. The top two firms in the industry (AT&T and Verizon) do better—in terms of the effectiveness of care support—than Sprint and T-Mobile. Second, for all firms, we find that good digital care consists not merely of responding to tweets, but an effort-intensive activity in which customer tweets need to be carefully examined and adequately addressed. Third, customers expect better quality of care from firms that charge more for similar cellular plans. Fourth, because of its structural nature, our methodology allows us to estimate the impact of seemingly unrelated events that could significantly affect customer care (e.g., signing an exclusive contract with a celebrity can improve how customers perceive the quality of care). Our findings in that regard are that events external to the care platform (whether firm-initiated or exogenous) can profoundly influence different aspects of digital customer care. Finally, we study the theoretical structural properties of the optimal response strategy and the optimal cost.

The rest of the paper is organized as follows. We first provide a review of related work, followed by a discussion of a controlled diffusion model of how customer sentiment evolves over time. We next estimate the parameters of this controlled diffusion process using Twitter data from the service handles of four major telecommunications service providers in the United States (AT&T, Verizon, T-Mobile, and Sprint). The estimated model is validated by comparing its out-of-sample predictive performance with that of state-of-the-art prediction models. We next provide several insights into the nature of digital customer care in the telecommunications industry using a number of policy simulations and real events. Then we further explore the structure of the optimal digital customer care policy. We conclude the paper with a discussion and summary of the findings.

## 2. Literature Review

In this section, we review the literature on firm-level impacts of customer sentiment as well as the main methodology employed in this study.

## 2.1. Customer Sentiment

A basic premise of this study is that customer sentiment can be measured and is important to manage for a firm. Customer sentiment can be gauged using sentiment analysis, which is defined as “the field of study that analyzes people’s opinions, sentiments, evaluations, appraisals, attitudes, and emotions towards entities such as products, services, organizations, individuals, issues, events, topics, and their attributes” (Liu 2015, p. 7). A variety of studies in businessrelated domains find a strong relationship between customer sentiment and firm-level outcomes. Luo et al. (2013) report that social media-based metrics such as web blogs and consumer ratings are significant indicators of firm equity value. Goh et al. (2013) find that compared with user-generated content in brand communities, marketer-generated content has a weaker impact on consumer purchasing behavior. An effective way to influence customer sentiment is to use expert testimonies. In a study by Luo et al. (2017) sentiments expressed by experts on blogs are found to positively influence consumer perceptions of the focal brand. Lau et al. (2012) report that domain-specific sentiment analysis can be used to make more informed decisions about business mergers and acquisitions. Customer sentiment is not just an individual expression, but also a social phenomenon. Forman et al. (2008) report that online community members rate reviews containing identity-descriptive information more positively, and the prevalence of reviewer disclosure of identity information is associated with increases in subsequent online product sales. Lak and Turetken (2017) provide support for the positive impact of sentiment scores on the efficiency of purchase decisions (time to make a purchase decision), but do not consider their role to be influential in increasing decision effectiveness (customer’s confidence in the purchase decision). Finally, Archak et al. (2011) report that textual data can be used for the predictive modeling of future sales.

Table 1 summarizes several studies, topics, and main findings in this area. These studies suggest that customer sentiment could influence firm equity value, branding activities, merger and acquisition decisions, and product sales and purchase decisions. Although these studies suggest the importance of customer sentiment for firm success, they do not prescribe any systematic strategy to manage or influence customer sentiment. Our study intends to fill the gap, namely, to study response strategies to manage customer sentiment within social media sites such as Twitter.

## 2.2. Digital Customer Care

Like any other business function, customer service operations have been impacted by the digital transformation. According to Bianchi et al. (2014), roughly 70% of customers use online platforms to purchase telecommunications-related products and services, and almost 90% of customers use online platforms for customer service inquiries. Digital care platforms including social media websites, have empowered customers to express their opinions about firms and their products and services. Customers can take advantage of these platforms to seek better and faster response from firms. An important survey published by the Institute of Customer Service (2013), reported that one undeniable impact of the digital customer service was that customers expect better service from firms. According to the same report, although the percentage of customers who experienced a problem decreased from 17% in 2008 to 12% in 2012, the percentage of complaints increased from 72% in 2008 to 76% in 2012. Ma et al. (2015) suggest that customers decry or complement a firm on social media depending on their relationship with the firm (negative, neutral, or positive). Furthermore, interventions made by firms to modify firm-customer relationships often encourage further complaints in future.

The majority of academic and practitioner publications assert that digital care platforms have a lot to offer to firms. For instance, firms can lower their cost of providing customer service through the effective use of digital care platforms (Bianchi et al. 2014). Firms can also encourage experienced customers to support more novice customers (Lithium Technologies Inc. 2017). Finally, customer satisfaction on digital platforms appears to be higher than the same on traditional channels such as phone and mail (Bianchi et al. 2014).

Table 1. Summary of Representative Studies Related to Customer Sentiment.

<table><tr><td>Study</td><td>Topic</td><td>Main findings</td></tr><tr><td>Luo et al. (2013)</td><td>Social media and firm equity value</td><td>Social media-based metrics such as web blogs and consumer ratings are significant, leading indicators of firm equity value.</td></tr><tr><td>Goh et al. (2013)</td><td>Social media brand community and consumer behavior</td><td>Marketer-generated content has a weaker impact on consumer purchasing behavior than user-generated content in brand communities.</td></tr><tr><td>Luo et al. (2017)</td><td>Expert blogs&#x27; impacts on consumer perceptions of competing brands</td><td>Expert blog sentiments and volume on a focal brand have a positive relationship with consumer perceptions of the focal brand.</td></tr><tr><td>Lau et al. (2012)</td><td>Adaptive decision support for business mergers and acquisitions</td><td>Domain-specific sentiment analysis can be used to make more informed decisions about business mergers and acquisitions.</td></tr><tr><td>Forman et al. (2008)</td><td>Relationship between consumer reviews and product sales</td><td>Online community members rate reviews containing identity-descriptive information more positively, and the prevalence of reviewer disclosure of identity information is associated with increases in subsequent online product sales.</td></tr><tr><td>Lak and Turetken (2017)</td><td>Impact of sentiment scores on purchase decisions</td><td>Sentiment scores improve the efficiency (speed) of purchase decisions without significantly affecting decision effectiveness (confidence).</td></tr><tr><td>Archak et al. (2011)</td><td>Product features and consumer reviews</td><td>Textual data can be used for predictive modeling of future changes in sales.</td></tr></table>

## 2.3. Stochastic Differential Equations

In this study, we develop an SDE model of the dynamics of the online customer sentiment in the presence of a response strategy used by the firm. The SDE has been applied in finance to model the time series of stock price movements, where randomness is inevitable (Black and Scholes 1973). A stochastic process models the random variable of interest that varies continuously (or almost continuously) and stochastically through time. We model customer sentiment as a Markov process, where the probability distribution of the future value depends only on its current value, which subsumes the effects of past values of the process. Randomness is captured by a Weiner process (the continuous limit of random walk), a fundamental building block for randomness in stochastic processes. A stochastic process is defined to be a Wiener process if it has independent increments that are normally distributed with mean zero and variance equal to the time interval (dt) between the increments (Ross 2014). We next develop an SDE model for the evolution of customer sentiment over time.

## 3. Model Development

In this section, we develop a diffusion model of customer sentiment followed by a stochastic control model of how this diffusion model is driven by the control objectives of the firm.

## 3.1. Diffusion Model of Customer Sentiment

In a typical digital customer care setting (such as the one in Twitter), customer comments (or tweets) arrive in a chronological sequence forming time series data. We perform sentiment analysis on each tweet and generate a sentiment score corresponding to each tweet. The sentiment scores are normalized to range from zero and a maximum value M.<sup>1</sup>

On social media sites, customer sentiment arrives randomly and can differ across customers. Firms usually respond to every single tweet posted by customers, but all tweets may not need the same amount of effort to be addressed. For instance, some tweets could be replied to using a template response such as “Thank you @username for contacting our support team.” On the other hand, some customer tweets may require additional effort by the firm. Hence, in our model, a firm’s response effort u t can be interpreted as the overall problem resolution effort exerted by the firm when responding to a tweet, rather than a decision to respond or not. This effort includes both solution identification and the actual response to the tweet. This response effort is usually not publicly observable. To detect the tweets that require more effort, firms often use a ticket-generation system (Zendesk.com 2018). These systems usually use the sentiment of the customer’s post (tweet) as one of the indicators for generating tickets (Zendesk.com 2018) and effort allocation decisions. Dissatisfied customers with negative sentiments in their tweets have a higher likelihood of requiring additional effort (ticket generation). The overall response effort can be measured in terms of person-hours, whereas the effec tiveness of this effort depends on the knowledge level, responsiveness, and assurance of the customer care team (Pitt et al. 1995) as well as on the quality of the ticket-generation system.

In our setting, the aggregate customer sentiment at any point in time is affected by the arrival of new customer sentiment as well as the response effort exerted by the firm to address customer needs. If the firm can properly handle the tickets, the sentiment will likely be adjusted in future periods. The senti ment (denoted by the state variable x ) is derived from tweets posted by customers during each time period t and then computing its moving average over a chosen time window. In time series data, a moving average is commonly used as the measure of the state (De Gooijer and Hyndman 2006). For example, moving average of a stock’s price measures how that stock is trending; whereas in economics, moving average is commonly used to study the gross domestic product, employment rates, and other macroeconomic variables (Brown 2004).

The goal in this section is to model a stochastic process that captures the evolution of the state variable (x ) over time. To model this process, we start with a simplified microstructure: the change in the state (dx ) in a small interval from t to t dt. The change in the state consists of a deterministic component that is influenced by the effort the firm exerts to manage customer sentiment. In addition, it consists of a stochastic component that captures the randomness in the change in sentiment in a short time interval.

First, we discuss the deterministic component, or the expected change in the state, E dx . The deterministic component consists of a positive term and a negative term. In our model, the negative term ( k x ) can be interpreted as the overall customer expectation of the quality of customer care, which depends on the coefficient of customer expectation of care (k ) and the current sentiment (state) x .

According to Parasuraman et al. (1991), customers expect service companies to be fair and provide quality service in exchange for their money. Given that the customer expectation of care for a similar product/ service would mainly depend on the price, firms that charge more for a similar product/service would raise expectations of customer care. However, there could be other factors such as firm-initiated events that influence the exact value of $k _ { 2 }$ . The overall customer expectation of care can be thought of as being dynamic, as it depends on the effectiveness of the firm’s response effort in the past. We view the customer sentiment as a Markov process, where the value of $x _ { t }$ reflects the overall effectiveness of the firm’s response effort, not just at instant t. Hence, a high value of customer sentiment (x<sub>t</sub>) is indicative of an effective response strategy over a period of time—raising the overall care expectations of customers. On the other hand, a low value of customer sentiment $\left( x _ { t } \right)$ reflects an ineffective response strategy, lowering the care expectations of the customers.

The positive term $k _ { 1 } u ( x _ { t } , t ) ( M - x _ { t } )$ , which reflects the positive impact of the effort exerted by the firm, depends on the difference between the highest possible sentiment score (M) and the current sentiment $\left( x _ { t } \right)$ . When the sentiment is already high, the impact of effort diminishes. In the extreme case when $x _ { t } = M ,$ there is no further gain from additional effort. The basic idea is that when the sentiment is low, there is more room to grow and hence, there is a higher positive impact of the effort exerted by the firm. The response effort is given by $u ( x _ { t } , t )$ . Thus, we allow for the firm’s response effort to be dynamic, and a function of the current sentiment, $x _ { t } .$ . The impact of this effort on the state depends on the effectiveness of the response effort $\left( k _ { 1 } \right)$ . The value of $k _ { 1 }$ is firm specific and depends on the knowledge level, reliability, responsiveness, and assurance of the customer care team (Pitt et al. 1995). In addition, $\mathbf { \nabla } _ { k _ { 1 } }$ could represent the quality of the ticket-generation system (Zendesk.com 2018). Thus, the positive impact of the response effort on the state is modeled as $k _ { 1 } u ( x _ { t } , t ) ( M - x _ { t } )$ . Combining the effects on the firm’s sentiment discussed earlier, we can write:

$$
\mathbb {E} (d x _ {t}) = (k _ {1} u (x _ {t}, t) (M - x _ {t}) - k _ {2} x _ {t}) d t.\tag{1}
$$

Hence, when the firm exerts no effort to meet the customer expectations $( \mathrm { i . e . , } u ( t )$ is equal to zero), the rate of decrease in the sentiment is $\left( k _ { 2 } x _ { t } \right)$ . However, if the firm exerts effort to manage the customer sentiment $( \mathrm { i } . \mathrm { e } . , u ( t )$ is positive), the net change in sentiment $( \mathrm { i . e . , ~ } d x _ { t } )$ can be positive or negative. If the firm responds, and the response meets customer expectations $( \mathrm { i . e . , } k _ { 1 } u ( x _ { t } , t ) ( \bar { M } - x _ { t } ) \geq k _ { 2 } x _ { t } )$ , the expected change in sentiment will be positive. However, if the firm responds and its effort does not meet customer expectations $( \mathrm { i . e . , ~ } k _ { 1 } u ( x _ { t } , t ) ( M - x _ { t } ) < k _ { 2 } x _ { t } )$ , then $E ( d x _ { t } )$ will be negative.

The stochastic component (diffusion) of the change in the firm perception is modeled as $k _ { 3 } d \omega _ { t } ,$ where dω is the Wiener process used to capture the white noise or randomness, $d \omega _ { t } \overset { d } { = } N ( 0 , d t )$ . The parameter $k _ { 3 }$ influences the magnitude of the random component. To summarize, we model the change in the state using the following SDE:

$$
d x _ {t} = (k _ {1} u (x _ {t}, t) (M - x _ {t}) - k _ {2} x _ {t}) d t + k _ {3} d \omega_ {t}.\tag{2}
$$

## 3.2. Stochastic Control Problem

The firm uses knowledge of the current customer sentiment (the state variable) to determine the response effort. The cost rate $q ( x _ { t } , t ) .$ , measured in dollars (say) per unit time, is defined as

$$
q (x _ {t}, t) = \kappa u (x _ {t}, t) ^ {2} + c (M - x _ {t}) ^ {2}.\tag{3}
$$

The first term in the cost rate is the direct cost associated with the response effort. The cost of the response effort is assumed to be a quadratic function of the effort. This is consistent with other similar models (Sethi 1973), where effort is considered to be an input into a production function for producing the state (x<sub>t</sub>). The parameter κ is the cost rate per unit effort.

The second term in the cost rate is the indirect cost associated with less than perfect customer sentiment. The indirect cost depends on a damage parameter c and the current sentiment. We assume the indirect cost to be increasing and convex with the deficit in customer sentiment from its perfect value. This implies that the damage from low customer sentiment gets increasingly higher.

We write the firm’s objective as one of minimizing the total discounted cost over a planning horizon ${ \bar { T _ { \prime } } }$ by determining the optimal trajectory for the control, namely, the firm’s response effort, $u ( x _ { t } , t )$ . Moreover, customer sentiment $\left( x _ { t } \right)$ is influenced by the control in a manner described by the SDE Equation (2) that acts as a constraint to the control problem.

Assuming a discount rate $\rho ,$ , the previous contro problem can be expressed as

$$
\begin{array}{r l} & {\underset {u (x _ {t}, t)} {\mathrm{Min}} \mathbb {E} \int_ {0} ^ {T} q (x _ {t}, t) e ^ {- \rho t} d t} \\ & {\quad \equiv \underset {u (x _ {t}, t)} {\mathrm{Min}} \mathbb {E} \int_ {0} ^ {T} \big (\kappa u (x _ {t}, t) ^ {2} + c (M - x _ {t}) ^ {2} \big) e ^ {- \rho t} d t,} \end{array}\tag{4}
$$

subject to

$$
\begin{array}{c} d x _ {t} = (k _ {1} u (x _ {t}, t) (M - x _ {t}) - k _ {2} x _ {t}) d t + k _ {3} d \omega_ {t} \\ 0 \leq x _ {t} \leq M, u (x _ {t}, t) \geq 0, \end{array}
$$

where M is the maximum sentiment score, $k _ { 1 }$ is the effectiveness of the response effort, $k _ { 2 }$ is the coefficient for customer expectation of $\mathrm { c a r e } , k _ { 3 }$ is the magnitude of the random component, κ is the cost rate per unit effort, c is the damage parameter, $\rho$ is the discount rate, and $T$ is the planning horizon. Table 2 lists the main parameters used in this study for easy reference.

Table 2. Parameter Definitions

<table><tr><td>Parameter Name</td><td>Definition</td></tr><tr><td>M</td><td>Maximum sentiment score</td></tr><tr><td>k1</td><td>Effectiveness of response effort</td></tr><tr><td>k2</td><td>Coefficient for customer expectation of care</td></tr><tr><td>k3</td><td>Magnitude of the random component</td></tr><tr><td>κ</td><td>Cost rate per unit effort</td></tr><tr><td>c</td><td>Damage parameter</td></tr><tr><td>ρ</td><td>Discount rate</td></tr><tr><td>T</td><td>Planning horizon</td></tr></table>

To solve this problem, let $V ( x _ { t } , t ) .$ , known as the value function, be the expected value of the objective from t to $T ,$ when an optimal policy is followed from t to $T .$ Then, by the principle of optimality:

$$
\begin{array}{c} V (x _ {t}, t) = \underset {u (x _ {t}, t)} {\text {Min}}   \mathbb {E} \big [ \big (\kappa u (x _ {t}, t) ^ {2} + c (M - x _ {t}) ^ {2} \big) d t \\ + (1 - \rho d t) V (x _ {t} + d x _ {t}, t + d t) \big ]. \end{array}\tag{5}
$$

Using Taylor’s expansion of $V ( x _ { t } + d x _ { t } , t + d t )$ in Equation (5) and properties of stochastic calculus, we can derive the Hamilton-Jacobi-Bellman (HJB) equation for stochastic optimal control as follows:

$$
\begin{array}{l} \rho V (x _ {t}, t) = \underset {u (x _ {t}, t)} {\text { Min }} \left[ \kappa u (x _ {t}, t) ^ {2} + c (M - x _ {t}) ^ {2} + V _ {x} \left(k _ {1} u (x _ {t}, t) \right. \right. \\ \cdot \left. (M - x _ {t}) - k _ {2} x _ {t}\right) + \frac {1}{2} k _ {3} ^ {2} V _ {x x} + V _ {t} \Bigg ]. \end{array} \tag {6}
$$

Differentiating with respect to the control yields the following optimal form for the firm’s response effort:

$$
u ^ {*} (x _ {t}, t) = - \frac {k _ {1}}{2 \kappa} (M - x _ {t}) V _ {x} (x _ {t}, t).\tag{7}
$$

tNote that the optimal response effort in this expression depends both on the current state (x<sub>t</sub>) and the marginal value function $( V _ { x } )$ . To evaluate the value function, we substitute the optimal response effort into the HJB. This yields a partial differential equation (PDE) as shown in the following, that needs to be solved to obtain the value function $V ( x _ { t } , t )$

$$
\begin{array}{l} - \frac {k _ {1} ^ {2} V _ {x} ^ {2} (M - x _ {t}) ^ {2}}{4 \kappa} + c (M - x _ {t}) ^ {2} - k _ {2} x _ {t} V _ {x} + \frac {1}{2} k _ {3} ^ {2} V _ {x x} + V _ {t} \\ = \rho V (x _ {t}, t). \end{array} \tag {8}
$$

Equation (8) is a nonlinear, second-order PDE that does not lend itself to an analytical, closed-form solution. Therefore, we proceed with a numerical solution for $V ( x _ { t } , t )$ . There is a large body of literature that proposes the use of method of lines (MOL) for numerical solutions of PDEs (Sadiku and Obiozor 2000). The first step is discretization along the $x _ { t }$ (state variable). The region is divided into strips by N dividing straight lines (hence the name “method of lines”) parallel to the t (time)-axis. Since we are discretizing along $x _ { t } ,$ we replace the first and second derivatives with respect to $x _ { t }$ with its finite difference equivalent. In other words, with only one remaining independent variable (t), we have a system of ordinary differential equations (ODE) that approximate the original PDE. Thus, one of the salient features of the MOL is the use of existing, and generally wellestablished, numerical methods for ODEs for solving PDEs. In our case, we use the backward diffusion formula, which is a well-known linear multistep method for numerical integration of individual discretized ODEs. Ultimately, in this fashion, the PDE for $V ( x _ { t } , t )$ is solved along discrete lines in the $x _ { t }$ (state variable) direction, and the solution between lines is found by numerical interpolation. This allows us to numerically evaluate the optimal response effort, $\boldsymbol { u } ^ { * } ( x _ { t } , t )$

In Section 5, we use the values of the optimal response effort to estimate the parameters in the controlled diffusion process described in Equation (2). Note that the controlled diffusion process (the process obtained after substituting for the optimal control) becomes a function of the parameters $( k _ { 1 } , k _ { 2 } , k _ { 3 } ) .$ , the state variable $x _ { t } ,$ and time t. The parameter M—the highest value of the sentiment—depends on the range of sentiment values and does not need to be estimated. The values of $x _ { t }$ and t are, of course, directly observed in the data.

## 4. Data

We collected data on customer service-related queries and firm responses from the Twitter service handles of the Big Four telecommunications firms (AT&T, Verizon, Sprint, and T-Mobile) from June 16, 2016, to October 15, 2016. According to Statista.com, these four carriers secure almost 95% of the wireless communications market share in the United States (Holst 2019).

To collect this data, we made two types of application programming interface (API) calls<sup>2</sup>: API calls to obtain all of the tweets directed at these firms and API calls to obtain all of the tweets from these firms. Figure 1 shows an example of a tweet posted by a customer as well as the firm’s response to that tweet. Appendix A in the e-companion describes our data collection process. Given our focus on customer service, we only focused on tweets through support accounts (e.g., @ATTCares rather than @ATT). Table 3 reports the number of tweets directed at and from

We measure customer sentiment by performing sentiment analysis on the tweets posted by customers on a firm’s customer service account in Twitter. The package “sentimentr” in R was used to perform this task.

Figure 1. Customer Care Transaction in Twitter  
![](/api/attachments/A2SXVEWB/fulltext/images/9726f756dd553f8829ee52ad510df36f1934bdc6809fdeae8d03c87cf347e106.jpg)

Before performing sentiment analysis, the following text preprocessing steps were applied. First, the entire corpus was converted into lowercase. Next, stopwords were removed from the corpus and SnowBall stemming was applied. Finally, punctuation and numbers were removed from the corpus.

To verify the accuracy of the sentiment analysis, we hired two graduate students to manually determine the sentiment of a random sample of 1,000 tweets. We then compared the human-generated sentiments with those generated by sentimentr. A high match of 83.49% between the human-generated sentiments and sentimentr-generated sentiments was observed. Appendix B in the e-companion reports the details of our sentiment analysis approach. Since sentiment returns the scores that range from a negative minimum to a positive maximum, we used min-max transformation to transform these sentiment scores to range from 0 to 1. Scores close to 0 are from very negative tweets whereas scores close to 1 are from very positive tweets.

After determining the sentiment of each individual tweet, the mean sentiment score during each hour can be calculated. Although our approach can work with any unit of time (day, hour, minute, etc.), we use one hour as the unit of time. There are several reasons for this choice.

First, if the unit of time is too small, there are many periods with no customer tweet. On the other hand, if the unit of time is too large, there is too much aggregation of customer sentiment. According to Table 3, the number of tweets directed at firms range from 56,629 to 82,667. There were 2,928 hours in the dat collection period (June 16, 2016, to October 15, 2016) with the number of tweets ranging between 19.341 and 28.233 tweets per hour. Second, according to Hutchinson (2017), 72% of customers who complain on Twitter expect to receive a response within one hour. Therefore, firms need to prepare an hourly planning scheme to be able to keep up with the customer expectations.

The state variable $x _ { t }$ in our model, sentiment score at time t, is measured as the hourly moving average over a two-hour window; hence, $d { \dot { x } } _ { t }$ would represent the change in this hourly moving average from one period to the next. During certain hours, no tweets were posted. To address this, we used predictive mean matching to impute the missing sentiment scores for these hours. Less than 10% of hours are imputed for the four firms. Our data set includes both original tweets and retweets.

Table 4, reports the mean and Gini’s mean difference (GMD), which is a measure of variability.<sup>4</sup> Here, T-Mobile has the highest mean sentiment score, followed by Verizon, AT&T, and Sprint. The GMD is similar across the four firms. Figure 2 visualizes the hourly sentiment scores for the Big Four telecommunications firms for the period of our study.

## 5. Model Estimation

We apply the MLE procedure to recover the parameters in our model. Typically, however, MLE requires knowledge of the probability density function of $x _ { t } .$ However, deriving the value function $V ( x _ { t } , t )$ discussed in Section 3 is intractable. Hence, it is infeasible to obtain an analytical solution for the probability density of $x _ { t } .$ . Even so, the change in customer sentiment (dx<sub>t</sub>), has some useful properties that can be exploited. The density of dx<sub>t</sub> is a Gaussian, with a mean $( k _ { 1 } u ( x _ { t } , t ) ( M - x _ { t } ) - k _ { 2 } x _ { t } ) d t$ and standard deviation $k _ { 3 } \sqrt { d t }$ . In particular, the probability density function of $d { x _ { t } } ,$ which represents the change in state between t and $t + d t ,$ , can be written as

$$
p (d x _ {t} | x _ {t}, k _ {1}, k _ {2}, k _ {3}, \rho , c, \kappa) = \frac {1}{\sqrt {2 \pi (k _ {3} d t) ^ {2}}} \mathrm{exp} ^ {\frac {- (d x _ {t} - \mu (x _ {t} , t))}{2 (k _ {3} d t) ^ {2}}},\tag{9}
$$

Table 3. Number of Tweets Directed at and from Support Accounts

<table><tr><td>Firm</td><td>Tweets directed at firm’s support account</td><td>Tweets from firm’s support account</td></tr><tr><td>AT&amp;T</td><td>82,667</td><td>83,186</td></tr><tr><td>Verizon</td><td>56,629</td><td>41,572</td></tr><tr><td>Sprint</td><td>58,726</td><td>89,956</td></tr><tr><td>T-Mobile</td><td>80,051</td><td>119,113</td></tr></table>

Table 4. Mean and Variation of Sentiment Scores for the Big Four Telecommunications Firms

<table><tr><td>Firm</td><td>Mean</td><td>Gini&#x27;s mean difference</td></tr><tr><td>AT&amp;T</td><td>0.468</td><td>0.040</td></tr><tr><td>Verizon</td><td>0.472</td><td>0.040</td></tr><tr><td>Sprint</td><td>0.463</td><td>0.043</td></tr><tr><td>T-Mobile</td><td>0.480</td><td>0.040</td></tr></table>

where

$$
\mu (x _ {t}, t) = (k _ {1} u (x _ {t}, t) (M - x _ {t}) - k _ {2} x _ {t}) d t.
$$

For sentiment data with T observations, we approximate the infinitesimal quantities (namely, $d x _ { t } , \ d t )$ with their numerical analogues. Thus, we write

$$
\begin{array}{r l} & d x _ {t _ {i}} \approx \Delta x _ {t _ {i}} = x _ {t _ {i + 1}} - x _ {t _ {i}} \\ & d t \approx \Delta t = t _ {i + 1} - t _ {i}. \end{array}
$$

If we define $\pmb \theta \equiv ( k _ { 1 } , k _ { 2 } , k _ { 3 } , \rho , c , \kappa )$ , the log-likelihood function for $\Delta x _ { t }$ with $T$ observations is

$$
\ln L (\boldsymbol {\theta}) = \sum_ {i = 1} ^ {T - 1} \ln p \left(\Delta x _ {t _ {i}} \mid x _ {t _ {i}}; \boldsymbol {\theta}\right).\tag{10}
$$

By substituting the density function and simplifying we get

$$
\begin{array}{r} \ln L (\pmb {\theta}) = - \frac {T - 1}{2} \ln 2 \pi - (T - 1) \ln k _ {3} \Delta t \\ - \frac {1}{2 (k _ {3} \Delta t) ^ {2}} \sum_ {i = 1} ^ {T - 1} \bigl (\Delta x _ {t _ {i}} - \mu (x _ {t _ {i}}, t _ {i}) \bigr) ^ {2}, \end{array}\tag{11}
$$

where $\mu ( x _ { t } , t ) = ( k _ { 1 } u ( x _ { t _ { i } } , t _ { i } ) ( M - x _ { t _ { i } } ) - k _ { 2 } x _ { t _ { i } } ) \Delta t . ^ { 5 }$

For every observation $( x _ { t _ { i } } , t _ { i } )$ in the data and parameter set θ, the optimal response (control) $u ( x _ { t _ { i } } , t _ { i } )$ is obtained by using

$$
u \big (x _ {t _ {i}}, t _ {i} \big) = - \frac {k _ {1}}{2 \kappa} \big (M - x _ {t _ {i}} \big) V _ {x} \big (x _ {t _ {i}}, t _ {i} \big).\tag{12}
$$

Figure 2. State Variable (Sentiment Score) for the Big Four Telecommunications Firms  
![](/api/attachments/A2SXVEWB/fulltext/images/76c8ec670771567ab918d3fe45a367dcfcef5f781288850078a8f533b1d52fa1.jpg)

In Equation (12), $V _ { x } ( x _ { t } , t )$ is obtained as a numeric value by numerically solving

$$
\begin{array}{r l} & {- \frac {k _ {1} ^ {2} V _ {x} ^ {2} (M - x _ {t _ {i}}) ^ {2}}{4 \kappa} + c (M - x _ {t _ {i}}) ^ {2} - k _ {2} x _ {t _ {i}} V _ {x} + \frac {1}{2} k _ {3} ^ {2} V _ {x x} + V _ {t}} \\ & {\quad = \rho V (x _ {t _ {i}}, t _ {i}), V (x _ {t _ {i}}, T) = 0.} \end{array}
$$

The maximum likelihood estimate $\hat { \theta }$ is obtained by maximizing the log-likelihood function described in Equation (11) over its parameter space:

$$
\hat {\boldsymbol {\theta}} \equiv \left(\hat {k _ {1}}, \hat {k _ {2}}, \hat {k _ {3}}, \hat {\kappa}\right) = \underset {\boldsymbol {\theta}} {\arg \max} \ln L (\boldsymbol {\theta}).
$$

The state variable $x _ { t } ,$ , sentiment score at time $t ,$ is measured as the hourly moving average over a twohour window. Hence, $d { x } _ { t }$ would represent the change in this hourly moving average from one period to the next. This implies that the value of $x _ { t }$ reflects the overall effectiveness of the firm’s response effort, not just at instant $t ,$ but instead over a rolling horizon. To estimate $\hat { \theta } ,$ we need to numerically solve $V _ { x } ( x _ { t } , t )$ using the MOL approach. For this analysis, we considered a total of $1 0 ^ { 1 2 }$ possible value sets for θ. Four parameters appear in the log-likelihood expression. These are the effectiveness of effort by the firm $\left( k _ { 1 } \right)$ the coefficient for customer expectation of care $\left( k _ { 2 } \right)$ , the magnitude of the random component $\left( k _ { 3 } \right)$ , and the cost rate per unit effort $( \kappa )$ . However, we cannot separately estimate $k _ { 1 }$ and $\kappa ,$ since these parameters appear together as a ratio $\textstyle { \binom { k _ { 1 } } { \kappa } }$ . Since we are interested in the effectiveness of the response effort $\left( k _ { 1 } \right)$ , we fixed the cost rate per unit effort $( \kappa = 1 )$ . We also verified the robustness of the estimation results over a range of values of κ. The values of c and $\rho$ do not affect the estimates and were fixed at 1 and 0.0005, respectively.<sup>6</sup>

In addition, we empirically test if effort does indeed impact customer sentiment by performing a difference-in-differences (DiD) study to compare the change in customer sentiment when the firm responded to customers tweets (treatment group) with the change in customer sentiment in rare cases when the firm did not respond (control group). We show that the DiD coefficient is positive and significant (p-value < 0.01), which suggests that responding to customers within two hours significantly improves customer sentiment. We report the details of thi study in Appendix D in the e-companion.

## 6. Estimation Results

Table 5 presents the estimation results. Based on our findings, Verizon, with the largest value for effectiveness of response effort (k ), is the most effective in responding to customer sentiment, and Sprint, which has the smallest value for $k _ { 1 } ,$ , is the least effective. We note that whereas T-Mobile and Sprint have higher response rates (the number of firm-generated tweets divided by the number of customer-generated tweets), they are low on effectiveness. Our findings concerning the effectiveness of the response effort (k<sub>1</sub>) are aligned with the inverse of average monthly blended customer churn for the second quarter of 2016. This period overlaps with most of the time period of our data set (June 16, 2016, to October 15, 2016). According to a research study by Strategy Analytics (Dano 2016), Verizon’s blended customer churn during this time period was 1.19%, the lowest among the Big Four. The second spot in the report belonged to AT&T, with a blended churn rate of 1.35%. The third and fourth spots belonged to T-Mobile and Sprint, with blended churn rates of 2.22% and 2.81%, respectively. This alignment between the inverse of customer churn during the second quarter of 2016 and the effectiveness of the response effort during an overlapping period lends support to our findings.

The parameter $k _ { 2 }$ measures the quality of digital customer care that customers expect from a firm. Based on the estimates for $k _ { 2 } ,$ we can clearly divide the Big Four into two groups of firms: AT&T and Verizon and Sprint and T-Mobile. AT&T and Verizon have very similar values for $k _ { 2 } ,$ , which are greater than those of Sprint and T-Mobile. As indicated previously, a greater value of $k _ { 2 }$ is associated with a larger downward drift in customer sentiment when the firm’s effort (u) is held constant. Our findings therefore suggest that AT&T and Verizon’s customers expect better quality of care than the customers of Sprint and T-Mobile. This is consistent with the plan-price rankings of these firms, with Verizon and AT&T being more expensive than Sprint and T-Mobile.<sup>8</sup> The values of the random component $\left( k _ { 3 } \right)$ for the four firms are similar, implying that the firm’s effort does not appear to influence the underlying variability of the sentiment data.

Table 5. Maximum Likelihood Estimation Results for the Entire Data

<table><tr><td>Firm</td><td>Effectiveness of response effort ( $k_1$ )</td><td>Coefficient for customer expectation of care ( $k_2$ )</td><td>Magnitude of random component ( $k_3$ )</td></tr><tr><td>AT&amp;T</td><td>0.396***(0.011)</td><td>0.164***(0.007)</td><td>0.028***(&lt;0.001)</td></tr><tr><td>Verizon</td><td>0.408***(0.013)</td><td>0.165***(0.006)</td><td>0.025***(&lt;0.001)</td></tr><tr><td>Sprint</td><td>0.358***(0.010)</td><td>0.151***(0.005)</td><td>0.027***(&lt;0.001)</td></tr><tr><td>T-Mobile</td><td>0.393***(0.015)</td><td>0.153***(0.009)</td><td>0.025***(&lt;0.001)</td></tr></table>

Notes. Although k<sub>1</sub> is sensitive to the values of $\rho , c ,$ and $\kappa ,$ the firms’ ranks based on $k _ { 1 }$ does not change. Please refer to Appendix G in the e-companion for more details. Standard errors are reported in parentheses $\begin{array} { r } { \ast \ast \ast \dot { p } < 0 . 0 0 1 . } \end{array}$

## 6.1. Comparison with Structure-Free Models

The best validation of our structural model would have been through an experiment that allowed us to alter a firm’s response effort and compare the observed outcomes with our predictions. Unfortunately, we did not have the luxury to conduct experiments in any of the firms. According to Keane (2010), another rigorous approach to examine the validity of an structural model is to compare the predictions obtained from the model with those obtained from state of the art, but structure-free models (e.g., using time series analysis). This is the approach taken in our study.

To measure the predictive performance of a model, we use the first two-thirds of the data for building the predictive model, and the remaining one-third of the data for testing the model. Furthermore, we use onestep-ahead forecasting to generate a forecast. In onestep-ahead forecasting, we use previous forecasts to generate future forecasts. We compared the predictions from the structural model with five structurefree models: ARIMA, ARCH, GARCH, ARIMA+ GARCH, and ARIMA+apARCH. Additional details of these comparisons are provided in Appendix E in the e-companion. We next summarize the results of these comparisons.

The results in Table 6 and Table 7 show that the SDE model performs slightly better than advanced structurefree models such as ARIMA+GARCH and ARIMA+ apARCH. Figure 3 visualizes the changes in the actual data as well as the forecasts obtained from the SDE and structure-free models.

## 6.2. A Different Approach in Measuring Customer Sentiment

When measuring the customer sentiment for each hour in Section 4, we used the mean sentiment of the tweets posted within the hour. This approach may not fully capture the influence of the volume of the tweets. Therefore, in this section we have included an extension of our model that incorporates the volume of tweets based on aggregate tweets data—instead of individual tweets data. In this approach, we first add all of the tweets for each firm for each hour into a single text document. For instance if @ATTCares received five tweets during hour t, we added them together (separated by “.”) to create a new document for hour t. Then we used sentimentr to obtain the overall sentiment score for each hour for each firm Therefore, if there are more negative tweets during a given hour, there will be more negative words within the document for that hour, which results in a more negative sentiment score (i.e., due to the volume of tweets).<sup>9</sup> After obtaining the sentiment scores for each hour for each firm, we used the same original minmax approach to normalize the data so that it ranges from 0 to M (i.e., 1). Table 8 compares the mean and spread of customer sentiment data between original and new approaches. According to the results, the sentiment scores have a smaller mean and spread for all four firms in the new approach. To understand these changes, we should compare the distribution of sentiment scores in each approach. The minimum raw sentiment score in the new approach is close to the minimum raw sentiment score in the previous approach (<sup>−</sup>4.064 and <sup>−</sup>3.265, respectively) and the mean raw sentiment score in the new approach is close to the mean raw sentiment score in the previous approach (+0.301 and +0.035, respectively). But the maximum raw sentiment score in the new approach is much larger than the maximum raw sentiment score in the previous approach (+9.129 and +2.310, respectively). Since we use the min-max normalization approach, the mean of the normalized scores for each firm will be smaller in the new approach (as observed in Table 8). Also, because we are mapping a wider spread in the new approach to range from 0 and M (equals 1 in our study) as compared with the previous approach, the variation of the normalized scores will be smaller in the new approach.

Table 6. Mean Absolute Error Comparisons

<table><tr><td>Model</td><td>AT&amp;T</td><td>Verizon</td><td>Sprint</td><td>T-Mobile</td></tr><tr><td>SDE</td><td>0.011</td><td>0.011</td><td>0.010</td><td>0.009</td></tr><tr><td>ARIMA</td><td>0.014</td><td>0.014</td><td>0.013</td><td>0.012</td></tr><tr><td>ARCH</td><td>0.019</td><td>0.018</td><td>0.017</td><td>0.018</td></tr><tr><td>GARCH</td><td>0.019</td><td>0.018</td><td>0.017</td><td>0.018</td></tr><tr><td>ARIMA+GARCH</td><td>0.013</td><td>0.013</td><td>0.012</td><td>0.012</td></tr><tr><td>ARIMA+apARCH</td><td>0.013</td><td>0.013</td><td>0.012</td><td>0.012</td></tr></table>

Table 7. Symmetric Mean Absolute Percent Error Comparisons

<table><tr><td>Model</td><td>AT&amp;T</td><td>Verizon</td><td>Sprint</td><td>T-Mobile</td></tr><tr><td>SDE</td><td>2.944</td><td>2.913</td><td>2.903</td><td>2.271</td></tr><tr><td>ARIMA</td><td>3.002</td><td>2.999</td><td>2.960</td><td>2.436</td></tr><tr><td>ARCH</td><td>4.113</td><td>3.954</td><td>3.817</td><td>3.752</td></tr><tr><td>GARCH</td><td>4.107</td><td>3.933</td><td>3.829</td><td>3.752</td></tr><tr><td>ARIMA+GARCH</td><td>2.969</td><td>2.935</td><td>2.789</td><td>2.491</td></tr><tr><td>ARIMA+apARCH</td><td>2.964</td><td>2.939</td><td>2.798</td><td>2.500</td></tr></table>

After obtaining the customer sentiment data using the new approach, we replicated our estimation procedure to recover the parameter estimates for $k _ { 1 } ,$ k , and k . Table 9 reports the estimation results using the new customer sentiment data and compares them with the original estimates. Since the mean sentiment with our findings in Table 9, where the estimates for $k _ { 1 }$ are smaller and the estimates for $k _ { 2 }$ are larger for the new data. In fact, the ranking of the firms in terms of relative change in $k _ { 1 }$ is identical to the ranking based on the drop in mean customer sentiment reported in Table 8. Furthermore, Table 8 shows that the spread of customer sentiment is smaller for the firms, which justifies why $k _ { 3 }$ is also smaller for the new data in Table 9. The drop in $k _ { 3 }$ is similar across the four firms.

Figure 3. Forecasts of 100 Hours of Test Data (Actual $\mathbf { x } _ { t }$ vs. Stochastic Differential Equation Predictions vs. ARIMA+GARCH Predictions)  
(a)  
![](/api/attachments/A2SXVEWB/fulltext/images/22abfa635c7efc07f811a2e40bc06f3d153c44b6365967ac2ca3494feefc92da.jpg)

(b)  
![](/api/attachments/A2SXVEWB/fulltext/images/fda068f0c14f8f19e1029fc491d3cb0c12e4dfd23631e0b925f6f9ab8f4864ea.jpg)

(c)  
![](/api/attachments/A2SXVEWB/fulltext/images/fa7f65d8b07febda37db2420cfb023aebf2fe094552b857f7765955f18dc68e7.jpg)

(d)  
![](/api/attachments/A2SXVEWB/fulltext/images/efeb5b00bd5fac1584f09e966fb75f300f34a0de3f297f3dfd60c04daedf40fe.jpg)  
scores are smaller for the new data, it follows from Equation (1) that, for this data, either the response effectiveness (k ) should be smaller or the customer expectations should be larger or both. This is consistent

As previously, based on both $k _ { 1 }$ and $k _ { 2 } ,$ , we can clearly divide the $\mathrm { B i g }$ Four into two groups: bargain firms (Sprint and T-Mobile) and premium firms (Verizon and AT&T). The only difference with the new data is that the order of estimates for Sprint and T-Mobile have switched in the new data. Unlike before, T-Mobile now has smaller estimates for $k _ { 1 }$ and $k _ { 2 }$ when compared with Sprint. A closer look at Table 8 offers a potential explanation for this switch. T-Mobile experienced a significantly larger drop in mean customer sentiment when compared with Sprint. This finding is consistent with our event study in Section 7.2, where T-Mobile was most sensitive to an increase in the volume of tweets and led to a largest drop in firm’s response effectiveness $\left( k _ { 1 } \right)$ , across all firms. This drastic change in customer sentiment in the new data for T-Mobile can justify the switch in the ranking for T-Mobile and Sprint. Overall, we find the results from the new customer sentiment data are consistent with the results we obtained using the old data.

## 7. The Effects of Major Events

Although structure-free models work relatively wel to forecast customer sentiment, they do not help firms determine the optimal response effort needed to manage customer sentiment. In addition, the forecast from a structure-free model will only be accurate if the environmental conditions underlying the data do not change. A structural model, on the other hand, allows the firm to conduct policy simulations, that is, determine the potential impact of environmental events (such as a price change, introduction of a new phone plan, or a new marketing campaign) on the parameters that influence customer sentiment (e.g., the effectiveness of care $[ k _ { 1 } ] ,$ , or the quality of care that the customers expect from the firm [k ]). Because the directional change (up or down) in these parameters can be anticipated by the firm, the change in the optimal response effort can also be anticipated. In what follows, we consider different events that could potentially influence customer care and the optimal response effort. All these events can be considered to be external to the customer care platform, that is, we deliberately chose events that are typically not controlled by customer care managers. Furthermore, these events can be classified into two kinds of events: firminitiated events and exogenous events (not initiated or controlled by the firm).

Table 8. Comparing the Mean and Variation of Sentiment Between Original and New Approaches

<table><tr><td rowspan="2">Firm</td><td colspan="2">Original approach</td><td colspan="2">New approach</td><td colspan="2">Difference</td></tr><tr><td>Mean</td><td>GMD</td><td>Mean</td><td>GMD</td><td>Mean</td><td>GMD</td></tr><tr><td>AT&amp;T</td><td>0.468</td><td>0.040</td><td>0.3143</td><td>0.024</td><td>-0.1537</td><td>-0.016</td></tr><tr><td>Verizon</td><td>0.472</td><td>0.040</td><td>0.3144</td><td>0.022</td><td>-0.1576</td><td>-0.018</td></tr><tr><td>Sprint</td><td>0.463</td><td>0.043</td><td>0.3102</td><td>0.023</td><td>-0.1528</td><td>-0.020</td></tr><tr><td>T-Mobile</td><td>0.480</td><td>0.040</td><td>0.3194</td><td>0.026</td><td>-0.1606</td><td>-0.014</td></tr></table>

Table 9. Comparing Coefficient Estimates Between Original and New Approaches

<table><tr><td rowspan="2">Firm</td><td colspan="3">Original approach</td><td colspan="3">New approach</td><td colspan="3">Difference</td></tr><tr><td> $k_1$ </td><td> $k_2$ </td><td> $k_3$ </td><td> $k_1$ </td><td> $k_2$ </td><td> $k_3$ </td><td> $k_1$ </td><td> $k_2$ </td><td> $k_3$ </td></tr><tr><td>AT&amp;T</td><td>0.396</td><td>0.164</td><td>0.028</td><td>0.251</td><td>0.210</td><td>0.014</td><td>-0.145</td><td>0.046</td><td>-0.014</td></tr><tr><td>Verizon</td><td>0.408</td><td>0.165</td><td>0.025</td><td>0.255</td><td>0.213</td><td>0.015</td><td>-0.153</td><td>0.048</td><td>-0.010</td></tr><tr><td>Sprint</td><td>0.358</td><td>0.151</td><td>0.027</td><td>0.228</td><td>0.194</td><td>0.014</td><td>-0.130</td><td>0.043</td><td>-0.013</td></tr><tr><td>T-Mobile</td><td>0.393</td><td>0.153</td><td>0.025</td><td>0.206</td><td>0.167</td><td>0.014</td><td>-0.187</td><td>0.014</td><td>-0.011</td></tr></table>

## 7.1. Firm-Initiated Events

These events are chosen such that one could expect them to have a positive or a negative impact on customer sentiment. For instance, a price increase for popular plans is likely to draw a negative reaction from customers. The question arises: Does this reaction spill over to create negative sentiment in the care platform? If so, what is the mechanism behind the drop in sentiment? For example, the sentiment could fall if the parameter $k _ { 2 }$ increases as a result of the price increase. This is plausible since customers would expect better care from a firm that charges more. If customer care managers can anticipate the impact of a price increase, they could adapt accordingly, for example, increase the response effort. On the other hand, when an event is perceived positively by customers, they might cut the firm some slack regarding service-related issues. For instance, if a firm offers more data download for the same price, its customers may be willing to tolerate a drop in the quality of customer care. Once again, it would be beneficial for customer care managers to anticipate the change in the parameters that affect customer sentiment so that they determine a new level of response effort.

To examine the potential effects of firm-initiated events, we focus on the impact on k<sub>2</sub>, the parameter in our model that represents the quality of care that customers expect from firms. We compare the value of $k _ { 2 }$ for the three-day period before the event with its value for the three-day period after the event. To identify the events during the study period, we used Google search with the name of the firm (e.g., AT&T) as the search keyword and the study period as the interval of time. Next, we used the first Google result that was related to an action initiated by the firm as an event to study for each firm. These events are discussed next.

7.1.1. AT&T: Exclusive Contract with Taylor Swift. Our first example is an event that, at first glance, appears to be unrelated to customer care. On October 4, 2016, AT&T announced an exclusive, multiyear deal with Taylor Swift (Huddleston 2016). The deal resulted in a new service called “Taylor Swift Now,” an exclusive AT&T service that would allow AT&T customers to access exclusive content and events related to Taylor Swift. Importantly, there was no corresponding price increase. Given that the customers would react positively to this event, we tested to see if the event had a spillover effect on customer care. As reported in Table 10, the value of k decreased from 0.174 to 0.167 as a result of this event. This was a positive outcome for AT&T customer care because customer sentiment would decrease at a slower pace for the same level of response effort.

Table 10. Change in Coefficient for Customer Expectation of Care $\left( k _ { 2 } \right)$ Due to Firm-initiated Events

<table><tr><td>Firm</td><td>Value of  $k_{2}$  before the event</td><td>Value of  $k_{2}$  after the event</td><td>Change in value of  $k_{2}$ </td></tr><tr><td>AT&amp;T</td><td>0.174</td><td>0.167</td><td>-0.007</td></tr><tr><td>Verizon</td><td>0.161</td><td>0.174</td><td>+0.013</td></tr><tr><td>Sprint</td><td>0.159</td><td>0.152</td><td>-0.007</td></tr><tr><td>T-Mobile</td><td>0.160</td><td>0.153</td><td>-0.007</td></tr></table>

Notes. As a robustness check, we compare the change in k<sub>2</sub> for the focal firm with the potential changes in $k _ { 2 }$ for the other firms during the same period of time. This analysis is reported in Appendix F in the e-companion.

7.1.2. Verizon: Price Hike. On July 6, 2016, Verizon announced an increase in the price that also increased the control customers had over their data plan (King 2016). Although more control over data plans is a positive change, the increase in price is clearly not (Close 2016). As T-Mobile’s chief executive officer John Legere summarized on Twitter: “And OMG, my favorite part is that @verizon is going to charge you \$5, to promise not to charge you for overages?” Thus, the overall impact of this event is not clear.

Table 10 reports the results of the changes in $k _ { 2 }$ due to this firm-initiated event. During the three-day period before the announcement, $k _ { 2 }$ had a value of 0.161. During the three-day period after the announcement $k _ { 2 }$ increased to 0.174. This increase in $k _ { 2 }$ implies that the event was negatively perceived by Verizon’s customers. Although it may be argued that a price increase, intuitively, makes customers demand better quality of care, we substantiate this intuition as well as quantify the magnitude of the effect.

7.1.3. Sprint: “Unlimited Freedom” Plan. On August 18, 2016, Sprint launched its new “Unlimited Freedom”

plan (Vincent 2016). This plan was claimed to allow customers to use more data with lower cost (the lowest among the Big Four). Therefore, this is perceived as a positive change from the customer’s point of view. As per results reported in Table 10, the value of $k _ { 2 }$ decreased from 0.159 to 0.152. This decrease in $k _ { 2 }$ is expected as this was a positive event for Sprint’s customers.

7.1.4. T-Mobile: “Unlimited One” Plan. On the same day that Sprint announced its new “Unlimited Freedom” plan, T-Mobile announced its “Unlimited ONE” plan that gave customers the privilege to download more data without any increase in price (T-Mobile 2016). Similar to the effect of the event on Sprint’s customer care, we believe that this event should have a positive influence on T-Mobile’s customers care. According to the results reported in Table 10, k decreased to a value of 0.153 from a value of 0.160 after the announcement of the new plan.

## 7.2. External Event: Release of iPhone 7

This is an example of an external event that is not initiated by firms. On September 9, 2016, the iPhone 7 was released by Apple. Given the popularity of iPhones in the United States, many customers ordered the new iPhone immediately after its release. Did this cause a significant increase in customer care requests? For instance, the requests could increase if customers experience service issues when ordering the new iPhone, if they need assistance to complete the order, or if they have questions about delivery date and other logistical issues. Figure 4 depicts the number of customer tweets during each hour from the beginning of September 8, 2016, to the end of September 10, 2016. Figure 4, (a)–(d) clearly show that all four firms experienced a surge of customer tweets on September $^ { 9 , }$ 2016. Therefore, it is reasonable to expect that the release of the new iPhone would impact the customer care workload and could perhaps reduce the quality of customer care.

Figure 4. Surge in Customer Tweets During the iPhone 7 Release on September 9, 2016  
(a)  
![](/api/attachments/A2SXVEWB/fulltext/images/6c9c657b3a76087cad538b5fcac18bf7b9a22b2ce8045d1a457eedbeeee15d9b.jpg)  
(c)

(b)  
![](/api/attachments/A2SXVEWB/fulltext/images/318c0736aaf00a58ad251fbdbc4d0dfe8e47adc7e068518648f4ab26afe49440.jpg)  
(d)

![](/api/attachments/A2SXVEWB/fulltext/images/c4b008f65e32baac1e907964b388e6016cb980956314fef27a17d3cc2354d34e.jpg)

![](/api/attachments/A2SXVEWB/fulltext/images/520843635889ea44fcec3497f6b2b1273e418104e677db2e178f7dfc87d4fae1.jpg)

Table 11. Changes in the Effectiveness of the Response Effort $\left( k _ { 1 } \right)$ During the Release of the iPhone 7

<table><tr><td>Firm</td><td>Value of  $k_{1}$  before the event</td><td>Value of  $k_{1}$  after the event</td><td>Change in value of  $k_{1}$ </td></tr><tr><td>AT&amp;T</td><td>0.329</td><td>0.322</td><td>-0.007</td></tr><tr><td>Verizon</td><td>0.348</td><td>0.345</td><td>-0.003</td></tr><tr><td>Sprint</td><td>0.321</td><td>0.299</td><td>-0.022</td></tr><tr><td>T-Mobile</td><td>0.361</td><td>0.337</td><td>-0.024</td></tr></table>

Given that all four firms experienced a sudden increase in customer tweets caused by the release of iPhone 7, we ask: How prepared were these firms to respond to customer queries during this time? Also, did the event adversely affect the effectiveness of customer care? We estimated $k _ { 1 }$ for a three-day period before and a three-day period after the release of iPhone 7 for all four firms. Table 11 reports the changes in $k _ { 1 }$ before and after the release of iPhone 7. As expected, the estimate for $k _ { 1 }$ dropped for all four firms within the few days after the release of iPhone 7. Among the Big Four, Verizon had the smallest change in $k _ { 1 } ,$ and AT&T had the second smallest change. The other two firms (T-Mobile and Sprint) had the biggest drop in the effectiveness of the response effort. It is also worth noting that T-Mobile received more tweets during this period than other firms. The impact the iPhone release had on $k _ { 1 }$ perfectly matches the order of the number of tweets each firm received during this time period (i.e., T-Mobile, Sprint, AT&T, and Verizon).

## 8. Structural Properties: Optima Response and Cost

Our goal in this section is to study the formal characterization of the optimal response strategy and the optimal cost obtained by solving the stochastic control problem in Section 3.2. However, Equation (8) is a nonlinear second-order PDE that does not lend itself to an analytical, closed-form solution. Therefore, we first numerically solve the HJB to evaluate the value function over a large range of parameter values and make an informed guess about the form of the value function. The form of the value function provides the form of the optimal response strategy. We verify the accuracy of our approximation using the empirical data and the MOL approach outlined in Section 5. Next, using approximations, we determine the closed-form expressions for the steady state optimal response and cost functions. We validate the quality of these approximations using simulations. We also use Twitter data for each firm to study the relative sensitivity of steady state response and cost functions to various problem parameters. The results of this quantitative analysis are summarized in Table 12. In addition, managerial implications of the optimal strategy are summarized in Table 13. The details of this analysis are presented in the following sections.

## 8.1. Numerical Solution of HJB

An illustrative solution for the value function and the response effort as a function of the customer sentiment (x ) at time t is shown in Figure 5.

Table 12. Sensitivity Analysis with Respect to Model Parameters

<table><tr><td rowspan="2"></td><td colspan="4">Digital care parameters</td><td colspan="4">Financial parameters</td></tr><tr><td colspan="2">Optimal response effort</td><td colspan="2">Optimal cost</td><td colspan="2">Optimal response effort</td><td colspan="2">Optimal cost</td></tr><tr><td>Firm</td><td> $\frac{\partial u^{\star}}{\partial k_{1}}$ </td><td> $\frac{\partial u^{\star}}{\partial k_{2}}$ </td><td>Optimal response effort</td><td> $\frac{\partial q^{\star}}{\partial k_{2}}$ </td><td> $\frac{\partial u^{\star}}{\partial \kappa}$ </td><td> $\frac{\partial u^{\star}}{\partial c}$ </td><td> $\frac{\partial q^{\star}}{\partial \kappa}$ </td><td> $\frac{\partial q^{\star}}{\partial c}$ </td></tr><tr><td>AT&amp;T</td><td>-0.218</td><td>0.145</td><td>-1.143</td><td>1.581</td><td>-0.135</td><td>0.129</td><td>0.138</td><td>0.142</td></tr><tr><td>Verizon</td><td>-0.214</td><td>0.149</td><td>-1.091</td><td>1.554</td><td>-0.134</td><td>0.128</td><td>0.140</td><td>0.149</td></tr><tr><td>Sprint</td><td>-0.263</td><td>0.164</td><td>-1.396</td><td>1.774</td><td>-0.136</td><td>0.129</td><td>0.137</td><td>0.116</td></tr><tr><td>T-Mobile</td><td>-0.244</td><td>0.184</td><td>-1.199</td><td>1.693</td><td>-0.133</td><td>0.127</td><td>0.144</td><td>0.138</td></tr></table>

Table 13. Impacts of Possible Scenarios on the Cost of Social Media Customer Service for the Telecommunications Industry

<table><tr><td>Sample scenario</td><td>Impacted parameter</td><td>Impact on optimal effort (u*)</td><td>Impact on optimal cost rate (q*)</td><td>Impact on firms</td></tr><tr><td>Training social media customer service representatives</td><td>Effectiveness of response effort (k1) increases</td><td>Decrease in optimal effort</td><td>Decrease in optimal cost</td><td>There is a separation between the premium firms (AT&amp;T and Verizon) and the bargain firms (T-Mobile and Sprint). The premium firms exhibit lower marginal benefit of the effectiveness of response effort, implying that there are diminishing returns to effectiveness improvement.</td></tr><tr><td>Price increase when coefficient for customer expectation of care is low</td><td>Coefficient for customer expectation of care (k2) further increases</td><td>Increase in optimal effort</td><td>Increase in optimal cost</td><td>The cost for the bargain firms is more sensitive to an increase in coefficient for customer expectation of care. Sprint should bear the highest cost followed by T-Mobile, AT&amp;T, and Verizon.</td></tr><tr><td>Price increase when coefficient for customer expectation of care is already high</td><td>Coefficient for customer expectation of care (k2) further increases</td><td>Decrease in optimal effort</td><td>Decrease in optimal cost</td><td>There are decreasing returns of any further increase in effort and the impacts on effort and cost are negative.</td></tr><tr><td>Increased labor and design costs</td><td>Cost rate per unit effort (κ) increases</td><td>Decrease in optimal effort</td><td>Increase in optimal cost</td><td>There is not much differential impact across the firms. However, T-Mobile has the highest increase in cost.</td></tr><tr><td>The socio-technological changes make the customers less tolerant of poor customer service</td><td>Damage parameter (c) increases</td><td>Increase in optimal effort</td><td>Increase in optimal cost</td><td>There is not much differential impact across the firms. However, Verizon has the highest increase in cost followed by AT&amp;T, T-Mobile, and Sprint.</td></tr><tr><td>Upgrading the ticket-generation system when the coefficient for customer expectation of care is low</td><td>Increase in effectiveness of response effort (k1), when coefficient for customer expectation of care (k2) is low</td><td>Decrease in optimal effort</td><td>Decrease in optimal cost</td><td>The cost and effort for the bargain firms is more sensitive to an increase in coefficient for customer expectation of care and effectiveness of effort.</td></tr><tr><td>Upgrading the ticket-generation system when the coefficient for customer expectation of care is high</td><td>Increase in effectiveness of response effort (k1), when coefficient for customer expectation of care (k2) is high</td><td>Increase in optimal effort</td><td>Increase in optimal cost</td><td>The cost and effort for the bargain firms is more sensitive to an increase in coefficient for customer expectation of care and effectiveness of effort.</td></tr></table>

Figure 5(a) illustrates that the optimal effort reduces with the current state of the customer sentiment. This is intuitive as the firm should increase the response effort when customer sentiment is low. Toward the end of the planning horizon, there is less incentive to incur any additional cost of response effort. Thus, the optimal response effort has the extreme value $u ^ { * } ( x _ { t } , T ) = \bar { 0 }$ . Figure 5, (b) and (c) illustrate the impact of state variable on the value function at different points in the planning horizon. Both figures show that value function V x, t is linear and decreasing in the state variable x t . The value function represents the firms objective of minimizing the total discounted cost over a planning horizon T. A higher customer sentiment reduces cost, therefore, it is intuitive that value function is decreasing in the state variable (x t ).

Based on these observations, we propose the following functional approximation for the optimal response strategy:

$$
u ^ {*} (x _ {t}) = \alpha (M - x _ {t}) \Big (1 - \exp^ {- \beta (T - t)} \Big).\tag{13}
$$

From the MOL plot in Figure 5(a), one can infer that the natural solution (optimal effort) of the problem is more of a steady state control. The only reason the optimal effort drops at the end of the planning horizon is due to the finite time assumption. Stated differently, the only impact of the finite T assumption is a deliberate and seemingly abrupt reduction in the

Figure 5. (Color online) Response Effort and Changes in Value Function  
![](/api/attachments/A2SXVEWB/fulltext/images/806832b41f2cbcd193d47b37aa11082f78ae000d795215eb8f9871cdf2fd3147.jpg)

(b)  
![](/api/attachments/A2SXVEWB/fulltext/images/3ab24572fe9cffb585257ce6e39da8b1666b47ba4996c58e1892e133d517c247.jpg)  
Change inValue Function $\left( V ( x _ { t } , t ) \right)$ with respect to the State Variable (xt) at $t = 0$

(c)  
![](/api/attachments/A2SXVEWB/fulltext/images/adebe0bc678671b7df46333ff7d4e49076bd90f1085923e5070529769648c80e.jpg)  
Change in Value Function $\left( V ( x _ { t } , t ) \right)$ with respect to the State Variable (xt) at $\begin{array} { r } { t = \frac { T } { 2 } } \end{array}$

firm’s effort right before the end of the planning horizon. Therefore, we focus our analyses on the steady state optimal effort, which is independent of time, that is, $\bar { u ^ { * } } ( x ) = \alpha ( M - x )$ . From Equation (7), we know that $\begin{array} { r } { u ^ { * } ( x _ { t } , t ) = - \frac { k _ { 1 } } { \gamma _ { \kappa } } ( M - x _ { t } ) V _ { x } ( x _ { t } , \hat { t } ) } \end{array}$ . Thus, under steady state, the marginal value function should be constant, that is, $\begin{array} { r } { V _ { x } ( x ) = - \frac { 2 \kappa } { k _ { 1 } } \alpha } \end{array}$ . This is consistent with the observation that the value function in Figure 5, (b) and (c) is linear in the state variable.

As a robustness check, we compare the marginal value function $\left( V _ { x } ( x _ { t } , t ) \right)$ ) approximated as $- \frac { 2 \kappa } { k _ { 1 } }$ α with that obtained using the standard MOL approach for our data set. Figure 6 plots the numerical value of $V _ { x }$ (obtained using MOL) versus the analytical approximation $\begin{array} { r } { ( V _ { x } ( x _ { t } , t ) = - \frac { 2 \kappa } { k _ { 1 } } \alpha ) } \end{array}$ obtained earlier. As can be seen, the approximation performs well (less than $^ 5$ percentage point difference) over most of the planning horizon. However, as expected, we observe an increase in the percentage difference toward the end of the planning horizon, since we do not consider the exponential term involving time. We also study the average percentage difference over a range of parameter values across all four firms and find that the marginal value function is, on average, within 2% of the actual value obtained using the MOL approach.

Figure 6. Percentage Error Between the Linear Approximated Versus Optimal Marginal Value Function  
![](/api/attachments/A2SXVEWB/fulltext/images/8e42b301485cabe7c97d764114d457fcc375667abfbfa8821e18e92c7b733768.jpg)

## 8.2. Mode of the State Variable

Using the expression for the steady state effort and Equation (3), the optimal steady state cost per unit time is given by $q ^ { * } ( { \dot { x } } ) = ( \kappa \alpha ^ { 2 } + c ) { \dot { ( } } M - x ) ^ { 2 }$ . Because the expressions for the optimal effort and cost both involve the state variable $x ,$ we propose studying the behavior of the optimal effort at the most frequent value of the state, that is, its mode. Unfortunately, an exact expression for the mode cannot be found. An intuitive approximation for the mode can be found by finding the value of the state (say, xˆ) such that $\dot { \mathbb { E } ( \boldsymbol { d } \boldsymbol { x } _ { t } ) } = 0$ . As the value of $x _ { t }$ approaches ${ \hat { x } } ,$ the magnitude of the change in the state variable can be expected to diminish, implying that the process should spend maximum time in the vicinity of xˆ. We therefore have

$$
k _ {1} \alpha (M - \hat {x}) ^ {2} - k _ {2} \hat {x} = 0.
$$

This equation has two roots, but the positive root is infeasible since it is greater than M. Therefore,

$$
\hat {x} = \frac {1}{2} \left\{2 M + \frac {k _ {2}}{k _ {1} \alpha} - \sqrt {\left(\frac {k _ {2}}{k _ {1} \alpha}\right) ^ {2} + \frac {2 M k _ {2}}{k _ {1} \alpha}} \right\}.\tag{14}
$$

To check the accuracy of the given approximation, we simulated 10,000 sample paths—each consisting of 20,000 time steps—of the stochastic process in Equation (2). This process was performed for 1,000 combinations of the independent parameters, namely, $k _ { 1 } ,$ $k _ { 2 } ,$ $k _ { 3 } ,$ , and $\alpha .$ The mode of $x _ { t }$ found from simulation was found to agree, very closely, to the mode provided by the expression in Equation (14). The MSE of the approximation was less than 0.01% with a maximum error of 0.38%. We also performed a Welch two sample t-test to confirm that the means of the two populations (simulated versus predicted using Equation (14)) are not different (p-value = 0.265).

## 8.3. Steady State Effort and Cost

The approximate expressions for steady state optimal effort and cost are

$$
\begin{array}{c} {u ^ {*} (\hat {x}) = \alpha (M - \hat {x})} \\ {q ^ {*} (\hat {x}) = \big (\kappa \alpha^ {2} + c \big) (M - \hat {x}) ^ {2}.} \end{array}
$$

The value of $\hat { x }$ is obtained from Equation (14). The value of α is a function of the model parameters. For a given set of parameter values, we use singular value decomposition with an objective to minimize the least square error to determine the values of α that best fits the proposed form of the steady state marginal value function. Appendix H in the e-companion provides the details of this study. The following form for α best fits the data:

$$
\alpha = a _ {0} + \frac {a _ {1}}{k _ {1}} + \frac {a _ {2}}{k _ {2}} + \frac {a _ {3}}{\kappa} + a _ {4} c + a _ {5} \rho .\tag{15}
$$

To recall, $k _ { 1 } , k _ { 2 } ,$ , and κ—firm dependent parameters— correspond respectively to the effectiveness of the response effort, coefficient for customer expectation of care, and the cost rate per unit effort. The parameter c corresponds to the marginal cost of a reduction in customer sentiment (damage parameter) and $\rho$ is the discount rate. This coefficient estimates in Equation (15) are $a _ { 1 } = - 0 . 1 0 7 , a _ { 2 } = 0 . 0 3 5 , a _ { 3 } = 0 . 3 6 1 , a _ { 4 } = 0 . 3 4 4 ,$ and $a _ { 5 } = - 5 . 0 8 0$ . The approximation performs well with an MSE of about $3 \%$

## 8.4. Structural Properties

Table 12 provides the estimated values of the derivative $\frac { \partial u ^ { \star } } { \partial \eta }$ and $\begin{array} { r } { \frac { \partial { q } ^ { \star } } { \partial { \eta } } , } \end{array}$ where $u ^ { \star }$ is the optimal response effort, $q ^ { \star }$ is the optimal cost per unit time, and $\eta$ is a problem parameter $( \mathrm { i . e . , } k _ { 1 } , k _ { 2 } , \kappa ,$ , and c). The problem parameters $k _ { 1 }$ and $k _ { 2 }$ are directly related to customer care, whereas the parameters κ and c are financially related, and may indirectly affect customer care. Next, we first discuss the derivatives of the optimal response effort and the optimal cost per unit time with respect to digital care parameters. We then discuss the derivatives of the optimal response effort and the optimal cost per unit time with respect to financial parameters, which are indirectly related to customer care.

8.4.1. Derivatives with Respect to Digital Care Parameters $( k _ { 1 }$ and $\pmb { k } _ { 2 } )$ . The two digital care parameters, $k _ { 1 }$ and $k _ { 2 } ,$ exhibit differential impacts on the optimal response effort and the optimal cost per unit time (Table 12). In the following, we summarize our key findings:

• For all four firms, the optimal response effort decreases as the effectiveness of the response effort increases. As mentioned earlier, the value of $k _ { 1 }$ is firm specific and depends on the knowledge level, reliability, responsiveness, and assurance of the customer care team. Hence, this finding implies that if the customer care team is more effective, the firm is expected to reduce effort to achieve the same level of customer care. Also, our finding indicates that if firms upgrade the tools supporting the care platform, they could incur a lower personnel cost.

• There is a separation between the premium firms (AT&T and Verizon) and the bargain firms (T-Mobile and Sprint) such that the premium firms exhibit lower marginal benefit of the effectiveness of the response effort $( k _ { 1 } )$ This implies that there are diminishing returns to effectiveness improvement. In Table 12 the derivative of optimal response effort with respect to the effectiveness of the response effort is equal to <sup>−</sup>0.218 and <sup>−</sup>0.214 for AT&T and Verizon as compared with <sup>−</sup>0.263 and <sup>−</sup>0.244 for Sprint and T-Mobile, respectively.

• The derivative of the optimal response effort with respect to the coefficient for customer expectation of care $( k _ { 2 } )$ also shows the separation between the premium and bargain firms. Table 12 shows that the impact of $k _ { 2 }$ on the optimal response effort is positive for all four firms, implying that all four firms can be expected to increase their response effort if their customers become more demanding of care. However, our finding reveals that the customers of the premium firms, being already more demanding of better service, have a lower marginal impact on the optimal response effort (0.145 and 0.149 for AT&T and Verizon as compared with 0.164 and 0.184 for Sprint and T-Mobile).

• The optimal response effort decreases with an increase in $k _ { 1 }$ for small values $o f k _ { 2 }$ , but changes direction for larger values of $k _ { 2 }$ . That is, for large values of $k _ { 2 } ,$ , the optimal response effort increases with an increase in $k _ { 1 }$ . Not reported in Table 12 is information on how the different marginal impacts are affected by the level of another parameter, that is, other than the one that is being varied. This finding suggests that when the value of the coefficient for customer expectation of care is large $( k _ { 2 }$ is large), as the response effort gets more effective $( k _ { 1 }$ increases) more effort must be applied. However, when the value of the coefficient for customer expectation of care is small, it is beneficial for the firm to decrease the effort and benefit from the reduction in the cost of effort. From Equations (14) and (15), it can be observed that the change in optimal response effort with an increase in $k _ { 2 }$ can be positive or negative. For example, for relatively smal values of $k _ { 2 }$ , we find that the response effort increases with $k _ { 2 }$ . This is intuitive as the response effort must increase as customers become more demanding of better customer care. However, for relatively large values of $k _ { 2 } ,$ the response effort decreases as $k _ { 2 }$ increases.

• Regarding the marginal impact on the optimal cost, the two premium firms group well on the digital care parameters $k _ { 1 }$ and $k _ { 2 } .$ . This finding implies that there is a greater benefit for the bargain firms to improve the effectiveness of the response effort than for the premium firms. This is likely because the bargain firms currently operate at a lower level of response effort effectiveness. On the other hand, the cost for the bargain firms is more sensitive to an increase in $k _ { 2 }$ , the care customers expect from the firm. In Table 12, $\frac { \partial q ^ { * } } { \partial k _ { 1 } }$ ranges from <sup>−</sup>1.143 to <sup>−</sup>1.091 for the premium firms and from <sup>−</sup>1.396 to <sup>−</sup>1.199 for the bargain firms. Similarly, $\frac { \partial { q } ^ { * } } { \partial k _ { 2 } }$ ranges from 1.554 to 1.581 for the premium firms and 1.693 to 1.774 for the bargain firms.

8.4.2. Derivatives with Respect to Financial Parameters (κ and <sup>c</sup>). Key findings with respect to financial parameters (κ and c) include:

• The derivatives of the optimal response effort with respect to financial parameters do not vary much across the firms. According to Table 12, $\frac { \partial u ^ { * } } { \partial \kappa }$ ranges from <sup>−</sup>0.136 to <sup>−</sup>0.133 whereas $\frac { \partial u ^ { * } } { \partial c }$ ranges from 0.127 to 0.129 among the Big Four telecommunications firms. That is, although financial parameters clearly affect the optimal response effort, there is not much differential impact across the firms regarding these parameters. This is expected since factors such as the cost of the response effort or the marginal benefit of improving customer sentiment should affect any firm in more or less the same manner. Concerning κ, the cost rate per unit effort, it is intuitive that as this cost increases, the effort should decrease $\begin{array} { r } { ( \frac { \partial u ^ { * } } { \partial \kappa } < 0 ) } \end{array}$ . Finally, $\begin{array} { r } { \frac { \partial u ^ { * } } { \partial c } > 0 } \end{array}$ simply means that as the damage of low customer sentiment increases, it pays to put more effort into responding to customer tweets. These derivatives can be used by the firm to find how the increase in the price of a productive input (such as the salary of employees that provide customer care) can affect the cost of the digital care unit.

• The derivative of the optimal cost with respect to the cost rate per unit effort (κ) is positive $\begin{array} { r } { ( \frac { \partial q ^ { * } } { \partial \kappa } > 0 ) } \end{array}$ . Overall, the firms are more or less impacted to the same extent with respect to the changes in the cost rate per unit effort, ranging from 0.137 to 0.144.

• The derivative of the optimal cost with respect to the damage parameter (c) is positive $\begin{array} { r } { ( \frac { \partial q ^ { * } } { \partial c } > 0 ) } \end{array}$ . This finding indicates that as the damage of low customer sentiment increases, the optimal cost of responding to customer sentiment increases as well. Here again, we observe a clear separation between the premium and bargain firms. The premium firms are more sensitive to the increase in damage parameter such that $\frac { \partial { q } ^ { * } } { \partial c }$ ranges from 0.142 to 0.149 for the premium firms, whereas it ranges from 0.116 to 0.138 for the bargain firms.

In Table 13 we summarize some of the managerial implications of the optimal response strategy and cost using several illustrative examples.

## 9. Conclusion

In this study, we develop a controlled diffusion model of the dynamics of customer sentiment in the presence of a response strategy used by firms. We used the model to predict customer sentiment as well as to study the structural properties of the optimal response strategy. The optimal response strategy is a function of several firm-specific parameters and the current customer sentiment. We apply MLE to recover the parameters of the stochastic process describing the evolution of customer sentiment using data from the Big Four telecommunications firms in the United States. We also compare our model’s predictive performance on customer sentiment with the state-of-the-art structurefree models. These comparisons indicate that the predictive performance of our controlled diffusion model is better than the predictive performances of several well-known, structure-free models.

Given the availability of data from Twitter and other digital platforms, firms can easily capture, process, and monitor customer sentiment within these platforms (Fan et al. 2006, Fan and Gordon 2014). Firms can also (and do) deploy a variety of analytical tools to forecast customer sentiment over time. Al though there is mounting evidence that the leading business-to-consumer (B2C) firms monitor and respond to customers’ service-related queries in social networking websites (Twitter for Customer Service Team 2015), there is little information about how customer sentiment can be managed using an optimal response strategy. For instance, it is known that some firms prioritize customers’ tweets to efficiently allocate available resources in providing responses (Muralidhar et al. 2015, Gunarathne et al. 2017). However, there is limited research that prescribes a response strategy to respond to customer sentiment within digital platforms. The concern is that, even though firms capture, monitor, and forecast customer sentiment, many firms may not be equipped to develop a response strategy that yields the desired outcomes Therefore, our SDE model could help practitioners go beyond the existing methods used in practice.

Furthermore, our model can be used to compare firms with respect to their overall effectiveness in responding to customer sentiment as well as their customers’ expectation of care quality. With respect to the effectiveness of digital customer care management, Verizon topped the list during the period of our study, followed by AT&T, T-Mobile, and Sprint, in that order. The ranking of the effectiveness of digital customer care management of the four firms in our study perfectly aligns with their blended customer churn rates during the same time period. That is, Verizon had the lowest blended churn among the Big Four. Verizon’s blended churn was followed by those of AT&T, T-Mobile, and Sprint, respectively. Interestingly, although T-Mobile has the highest response rate (measured by the number of tweets generated by the firm divided by the number of tweets generated by customers in the care platform), it ranks low in terms of the effectiveness of care effort. This indicates that good care quality comes from carefully evaluating customer requests and responding to them in an appropriate manner. Such quality care may require a welldesigned ticket-generation system that accurately detects the tweets that require further follow-up as well as a good customer service team that can resolve the issues once the tickets are generated. Merely sending out automated tweets is not sufficient for achieving good quality care.

With respect to the coefficient for customer expectation of care, our findings suggest that AT&T and Verizon’s customers expect better care than Sprint and T-Mobile customers. This finding perfectly aligns with the prices that these firms charge (for comparable plans), with Verizon and AT&T being the most expensive followed by Sprint and T-Mobile. With respect to the net effort exerted by the firms, we find that Verizon has the best rank, followed by AT&T, T-Mobile, and Sprint, in that order.

Overall, the proposed SDE model prescribes a dynamic response strategy that allows the firm to effectively react to external events that might have a significant spillover on customer sentiment. Using real events that occurred during the time period of our study, we reveal that an event that is perceived positive by customers would lower their expectations of care quality. On the other hand, an event that is perceived as negative by customers (such as a price hike) would increase their expectation of care quality. Such analysis enables the firms to tailor their response efforts in anticipation of potentially influential events, such as a marketing campaign, a new product release, or even a data security breach. To our knowledge, quantifying the spillover effects of seemingly unrelated events on digital customer care management has not been rigorously studied in the literature. Furthermore, our study informs firms about the implications of their actions related to social media customer care department (e.g., training customer service representatives or upgrading the ticket-generation system).

Although the implications of our findings can be extended to other social media platforms such as Facebook (as long as the customer comments are public and arrive in a chronological sequence forming time series data), our study is not without limitations. We did not obtain closed-form results for the optimal response strategy. Although the current formulation of the stochastic control model does not lend itself to a closed-form solution, it is possible that other reasonable formulations could yield an analytically tractable form. We also did not consider any noise in the specification of the control problem. A noisy formulation would consider the possibility that a firm does not act optimally. This could happen for a variety of reasons. A firm may be acting optimally, but could be using signals (state variables) that the researcher is unaware of. Alternatively, the firm may be committing optimization errors. This could explain the differences between the optimal actions predicted by the model and the firm’s actual actions. Including noise in model specification can lead to a more comprehensive treatment of the problem being addressed in this study. Furthermore, we did not consider the potential impacts of one firm’s actions on the digital customer care response strategy of the other firms in the telecommunications industry. Since customer tweets and firms’ responses are publicly available, competitors may decide to react to the interactions between firms and their customers. For instance, Sprint may decide to adjust its digital customer care strategy based on actions taken by Verizon. This angle could be a promising extension to our study. Finally, although we provide some evidence that firm-initiated events could impact the coefficient for customer expectation of care (k ), we could not perform a statistical test to check if these events significantly impact k .

## Acknowledgments

The authors are thankful to the Data Science Initiative at the University of North Carolina at Charlotte for their help in collecting data for this study.

## Endnotes

<sup>1</sup> We set the value of M at 1 in our study.

<sup>2</sup> An API is a set of procedures, protocols, and tools for building software applications. APIs make it easier for programmers to develop an application by providing the building blocks. An API call or request is simply a request sent to the API for a particular transaction (e.g., logging in or posting a comment or retrieving content).

<sup>3</sup> T-Mobile and Sprint often respond to a single customer query with more than one tweet. This explains why the number of tweets from these firms exceed the number of tweets from customers. In Appendix A in the e-companion, we discuss how we identified these types of tweets.

<sup>4</sup> According to Yitzhaki (2003), GMD is a superior measure of variability as it is more informative than variance if the data are not normally distributed

<sup>5</sup> The Gaussian property of dx x may not always hold for Δx x , and hence needs to be verified in the data. Conceptually, if the data are sufficiently granular, implying that data points are not too far apart in time, the normal assumption is likely to be upheld. In Appendix C in the e-companion, the normal assumption is verified in the Twitte feed collected for all four firms

<sup>6</sup> Please refer to Appendix G in the e-companion for further details.

<sup>7</sup> Blended churn rate, as reported by U.S. wireless carriers, is a churn rate figure that is based on both pre-paid and contract customer losses. This figure is one of the main figures in evaluating wireless carriers performance

<sup>8</sup> According to a Business Insider post (Dunn 2016), during the time period of our study, the cheapest unlimited plans (unlimited talk, text, and data) offered by Sprint, T-Mobile, and AT&T were, respectively, \$60, \$70, and \$100 per month for the first line. Verizon did not offer an unlimited data plan at the time, but offered something similar with unlimited talk and text plus 24 Gbytes of data for \$110 per month (Komando.com 2016).

<sup>9</sup> This approach not only allows us to incorporate the volume of the tweets into the sentiment scores, but also prevents us from creating a noisy sentiment data that is dramatically impacted by very positive and very negative tweets.

## References

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Bianchi R, Schiavotto D, Svoboda D (2014) Why companies should care about e-care. McKinsey.com (August), http://www.mckinsey .com/business-functions/marketing-and-sales/our-insights/why -companies-should-care-about-ecare.

Black F, Scholes M (1973) The pricing of options and corporate liabilities. J. Political Econom. 81(3):637–654.

Brown RG (2004) Smoothing, Forecasting and Prediction of Discrete Time Series (Prentice-Hall, Englewood Cliffs, NJ).

Burke S (2016) Examples of the good, the bad & the ugly of customer service on social media! Spokal (June 14), http://www .getspokal.com/examples-of-the-good-the-bad-the-ugly-of -customer-service-on-social-media.

Close K (2016) Your Verizon bill is about to go up. Money.com (July 6), http://money.com/money/4394575/verizon-price-increase/.

Dano M (2016) how Verizon, AT&T, T-Mobile, Sprint and more stacked up in Q2 2016: The top 7 carriers. Fierce Wireless (August 15), http://www.fiercewireless.com/wireless/how-verizon-at-t -t-mobile-sprint-and-more-stacked-up-q2-2016-top-7-carriers.

De Gooijer JG, Hyndman RJ (2006) 25 years of time series forecasting. Internat. J. Forecasting 22(3):443–473.

Dunn J (2016) Mobile carriers are going in on “unlimited” data plans, but they’re all full of red flags. Business Insider (August 18), http://www.businessinsider.com/tmobile-unlimited-data-plan -sprint-att-verizon-2016-8/.

Fan W, Gordon MD (2014) The power of social media analytics. Comm. ACM 6(57):74–81.

Fan W, Wallace L, Rich S, Zhang Z (2006) Tapping the power of text mining. Comm. ACM 9(49):76–82.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3):291–313.

Frumkin T (2017) The 7 most important customer service stats for 2017. Coversocial (January 18), http://www.conversocial.com/ blog/the-7-most-important-customer-service-stats-for-2017.

Goh KY, Heng C-S, Lin Z (2013) Social media brand community and consumer behavior: Quantifying the relative impact of user- and marketer-generated content. Inform. Systems. Res. 24(1):88–107.

Gunarathne P, Rui H, Seidmann A (2017) Whose and what social media complaints have happier resolutions? Evidence from Twitter. J. Management Inform. Systems 34(2):314–340.

Holst A (2019) Wireless subscriptions market share by carrier in the U.S. from 1st quarter 2011 to 3rd quarter 2018. Statistica.com (September 13), https://www.statista.com/statistics/199359/ market-share-of-wireless-carriers-in-the-us-by-subscriptions/.

Huddleston T Jr (2016) All about Taylor Swift’s “multi-year” deal with AT&T. Fortune (October 4), https://fortune.com/2016/10/ 04/taylor-swift-att-deal-super-bowl/.

Hutchinson A (2017) Consumer expectations rising on social customer care. Social Media Today (August 23), https://www.socialmediatoday .com/social-business/consumer-expectations-rising-social -customer-care-report.

Hyken S (2016) How to use Twitter for customer service. Forbes (April 30), https://www.forbes.com/sites/shephyken/2016/ 04/30/how-to-use-twitter-for-customer-service/

Institute of Customer Service (2013) Handle with care: An analysis and toolkit to improve complaint handling. Report, Institute of Customer Service, London. http://www.instituteofcustomerservice .com/research-insight/research-library/handle-with-care-an -analysis-and-toolkit-to-improve-complaint-handling

J.D. Power (2013) Poor social media practices can negatively impact a businesses’ bottom line and brand image. Accessed September 1, 2019, https://www.jdpower.com/business/press-releases/2013 -social-media-benchmark-study.

Keane M (2010) Structural vs. atheoretic approaches to econometrics. J. Econometrics 156(1):3–20.

King H (2016) Verizon overhauls its data plans. CNN Money (July 6), https://money.cnn.com/2016/07/06/technology/verizon-data -plan/.

Komando.com (2016) 2016 mobile data plans—How do they compare? Komando.com (August 27), https://web.archive.org/web/ 20160830105702/www.komando.com/tips/370499/2016-mobile -data-plans-how-do-they-compare/all

Lak P, Turetken O (2017) The impact of sentiment analysis output on decision outcomes: An empirical evaluation. AIS Trans Human-Comput. Interaction 9(1):1–22.

Lau RYK, Liao SSY, Wong KF, Chiu DKW (2012) Web 2.0 envi ronmental scanning and adaptive decision support for business mergers and acquisitions. Management Inform. Systems Quart. 36(4):1239–1268.

Lithium Technologies Inc. (2017) Discussion forums: Connect product experts and brand enthusiasts through peer-to-peer discussions. Accessed October 11, https://khoros.com/platform/communities forums.

Liu B (2015) Sentiment Analysis: Mining Opinions, Sentiments, and Emotions (Cambridge University Press, Cambridge, UK).

Luo X, Zhang J, Duan W (2013) Social media and firm equity value Inform. Systems Res. 24(1):146–163.

Luo X, Gu B, Zhang J, Phang CW (2017) Expert blogs and consumer perceptions of competing brands. Management Inform. System Quart. 41(2):371–395.

Ma L, Sun B, Kekre S (2015) The squeaky wheel gets the grease—An empirical analysis of customer voice and firm intervention on Twitter. Marketing Sci. 34(5):627–645.

Muralidhar S, Sardesai C, Morya A (2015) Power to the people: Customer care and social media. White paper, Cognizant, Teaneck, NJ, http://cognizant.com/whitepapers/power-to-the -people-customer-care-and-social-media-codex1226.pdf.

Parasuraman A, Berry LL, Zeithaml VA (1991) Understanding customer expectations of service. Sloan Management Rev. 32(3): 39–48.

Pitt LF, Watson RT, Kavan CB (1995) Service quality: A measure of information systems effectiveness. Management Inform. Systems Quart. 19(2):173–187.

Ross S (2014) Variations on Brownian motion. Introduction to Prob ability Models, 11th ed. (Elsevier, Amsterdam), 612–614.

Sadiku MNO, Obiozor CN (2000) A simple introduction to the method of lines. Internat. J. Electr. Engrg. Ed. 3(37):282–296.

Sethi S (1973) Optimal control of the Vidale-Wolfe advertising model. Oper. Res. 21(4):998–1013

T-Mobile (2016) Hello un-carrier 12 ... R.I.P. data plans T-Mobile goes all in on unlimited. T-Mobile (August 18), https://www.t-mobile .com/news/rip-data-plans.

Twitter for Customer Service Team (2015) Customer service on Twitter. Report, Twitter Inc., San Francisco. http://cdn.cms-twdigitalassets .com/content/dam/marketing-twitter/downloads/customerservice -playbook.pdf.

Vincent B (2016) Sprint’s new Unlimited Freedom plan is unlim ited with a catch. Engadet.com (August 18), https://www.engadget .com/2016/08/18/sprints-unlimited-freedom-plan/.

Yitzhaki S (2003) Gini’s mean difference: A superior measure of variability for non-normal distributions. METRON—Internat. J. Statist. 61(2)285–316.

Zendesk.com (2018) Providing great social media customer service. Accessed October 11, 2019, https://www.zendesk.com/resources customer-service-through-social-media/.
