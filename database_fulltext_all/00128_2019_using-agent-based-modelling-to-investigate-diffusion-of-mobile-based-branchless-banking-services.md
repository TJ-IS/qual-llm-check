---
otero_id: 128
otero_key: "UFTP4GD7"
title: "Using agent-based modelling to investigate diffusion of mobile-based branchless banking services in a developing country"
authors: "Muhammad Adeel Zaffar; Ram L. Kumar; Kexin Zhao"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.10.015"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using agent-based modelling to investigate difusion of mobile-based branchless banking services in a developing country

![](/api/attachments/UFTP4GD7/fulltext/images/bb364f4ee59ef038c08e0db19917b2ea0d81717835d13638af9bf3e92d8b4d9e.jpg)

Muhammad Adeel Zafar<sup>a,⁎</sup>, Ram L. Kumar<sup>b</sup>, Kexin Zhao<sup>b</sup>

<sup>a</sup> Suleman Dawood School of Business, Lahore University of Management Sciences, DHA, Lahore 54792, Pakistan

<sup>b</sup> Belk College of Business, University of North Carolina at Charlotte, 9201 University City Blvd, Charlotte 28223, NC, United States of America

## A R T I C L E I N F O

Keywords: Branchless banking Agent-based modelling Innovation diffusion

## A B S T R A C T

Branchless Banking Services (BBS) were launched in 2009 in Pakistan with the promise of providing banking services to the unbanked. Since then the overall size of BBS has grown. Despite the popularity of the over-thecounter (OTC) channel. growth in m-wallets or mobile accounts (MA) has been slow. We investigate diffusion of MA through the development of an agent-based simulation model that captures the dynamics of the multi-sided BBS platform market. We identify important factors that drive MA difusion and illustrate main and interaction efects between these factors. Furthermore, we examine how the relative efects of the diferent sides of the market have evolved over the course of the MA difusion across both rural and urban consumer segments. The proposed model helps to understand the dynamics of difusion of an important financial technology innovation. It can also serve as the starting point for future -research on technology difusion in multi-sided markets.

## 1. Introduction

Mobile applications have shown dramatic growth over the last five years and are expected to record healthy future growth rates [1]. Slower growth rates in developed countries are likely to be complemented by increased global adoption, particularly in less developed countries [1]. Industries, such as the financial services sector, are affected and disrupted by the growth of mobile applications. The term “Fintech” has been used to refer to technology-enabled transformation of financial services. The Economist magazine reported that: “The magical combination of geeks in t-shirts and venture capital that has disrupted other industries has put financial services in its sights … Like other disrupters from Silicon Valley, Fintech firms are growing fast.” [2]

There are many types of innovative mobile-based financial service solutions and this research chooses to focus on adoption and difusion of branchless banking services (BBS). BBS refers to the intensive use of mobile devices (e.g., a smart phone) to perform financial transactions. As the use of various applications on smart phones becomes increasingly common, the range of BBS is likely to increase. Current mobile applications allow users to check balances, deposit checks, and perform other transactions. Payment systems using phones are relatively new. In the US, Apple pay would be an example of such a BBS. The rate of BBS adoption is sometimes higher in emerging economies than in the developed world. However, challenges remain in terms of encouraging the adoption of such services. Despite the importance of this topic, there is limited academic research towards understanding adoption and diffusion of such services, which occur in a multi-sided market environment. This research aims to understand and model the underlying mechanisms driving the difusion dynamics of BBS. The word dynamics is intended to capture the macro-level process of difusion in light of a) diferent sides of the BBS market and how they might interact with each other to afect the process of difusion, b) individual-level attributes and behaviours of key stakeholders [3].

Specifically, we use data from a developing Asian country, Pakistan, to develop our model. Understanding IT implementation in developing countries is crucial due to their unique challenges [4]. This is especially true in the case of BBS. Countries in Africa and Asia have large populations without access to financial services. However, given recent advancements in mobile phone technology, access to smart phones has considerably improved in these areas [5]. This has paved the way for providing access to mature financial services to the masses. BBS is an important mechanism for financial inclusion and has the potential to reduce poverty and improve quality of life which are important millennium development goals [6]. BBS was launched in Pakistan in 2009 with the promise of providing banking services to the unbanked. Since then the overall size of such services has grown. Two types of channels for BBS have been introduced, namely over-the counter (OTC) services, and mobile accounts (MA). With OTC an authorized BBS operator performs the financial transaction on behalf of the customer whereas with MA the customer directly performs the transaction through her phone. Despite the remarkable popularity of OTC services, growth in MA has been slow.

This paper focuses on the conditions that may promote MA adoption and difusion over the OTC channel. There are several reasons for fo cusing on MA difusion. First, from an end consumer's perspective, MA ofers greater control and independence over the financial transactions. In OTC, the end consumer has to find a BBS operator to perform the transaction. This dependence on physically finding the operator and having them perform the transaction is significantly reduced with MA. Second, with MA BBS platform providers do not have to pay any commission to BBS operators for helping end consumers perform the transactions. This improves the overall returns for the BBS platform providers which would in turn allow them to ofer more afordable services to the end consumers. Third, merchants may also prefer MA over OTC because of instantaneous payment resolution. In OTC, the payment would be routed through a BBS operator whereas with MA the end consumer would be in a position to instantaneously perform the transaction. Fourth, in addition to the benefit for merchants in general discussed in the previous point, online merchants are in a position to attract a much wider group of customers by ofering BBS as a mode of payment. Online merchants such as daraz.pk have partnered with BBS platform providers to ofer discounts to their customers when they use MA to perform transactions on their site (Press [7]). Fifth, the financial regulator prefers MA over OTC as well since the former afords greater independence to the end consumer and better transparency to the fi nancial transaction. These are important considerations for the reg ulator.

We use interview data and review of related literature to understand key factors that drive individual consumers' adoption behaviour. We then investigate the difusion of MA resulting from the collective adoption behaviour of individuals through the development of an agent-based simulation model that can capture the dynamics of the multi-sided BBS market (Fig. 1). Agent-based simulation allows us to focus our modelling at the level of individual agents who decide whether to use MA during a time period. The collective behaviour of agents in the market (difusion of MA) emerges as a result of multiple in dividual decisions. Our simulation results illustrate how main and in teraction efects drive difusion over time. Understanding the dynamics of MA adoption can help decision makers study the efect of diferent types of incentives in promoting the mobile-based BBS channel.

This paper is organized as follows. Section 2 provides an overview of the relevant literature. Section 3 discusses the data collection and model development process in detail. In Section 4 simulation model parameters and experimental conditions are discussed followed by a detailed discussion of the analyses and results in Section 5. Section 6 concludes with a brief discussion of validity of the model, key findings, limitations and ideas for future research.

## 2. Literature review

We integrate two research steams to develop our model: BBS literature and studies of multi-sided markets. Academic research on the adoption of mobile payment systems is relatively new and rapidly growing. Shaikh and Karjaluoto [8] conducted a comprehensive literature review of mobile banking adoption and suggested that related literature is still fragmented. There is a growing body of research on adoption and difusion of BBS from a consumer perspective based on interviews and survey data. The technology acceptance model and difusion of innovation theory are commonly used theories for such studies. For instance, using qualitative interview data, Mallat [9] found that factors such as lack of alternative payment methods, urgency, and queue avoidance facilitate the adoption of mobile payments. However, factors such as premium pricing, complexity, lack of critical mass, and perceived risks inhibited adoption. Perceived risks included unauthorized use of a mobile phone, lack of transaction record and documentation, errors, device and network reliability. Zhou et al. [10] integrated the task technology fit model and the unified theory of acceptance and usage of technology to explain mobile banking adoption. Their finding based on an analysis of survey data highlighted the im portance of task technology fit. Yang et al. [11] studied Chinese customers, and found that behavioural beliefs, social influences and personal traits had an efect on adoption of mobile payment services across time. Taken together, the studies on mobile-based BBS adoption highlighted the importance of factors such as perceived risk of adopting new technology, expected cost of performing transactions or pricing of mobile-based BBS as compared to alternative forms of payment, and customer-level behavioural, social and personal traits.

While BBS adoption literature has ofered a theoretical foundation to model consumer decisions, it largely ignored other types of key stakeholders in BBS difusion. These stakeholders included the BBS platform provider (typically some combination of a telecommunications provider and a financial services provider), merchants who accepted BBS (such as shops accepting mobile-based payments), and op erators who facilitated BBS providers by helping customers perform these transactions. While the BBS platform provider ofered the services, consumers, merchants, and operators represented three diferent sides of the market. They each incurred a set of costs and benefits that were impacted by BBS. More importantly, there were interactions be tween these players' costs and benefits. For example, if BBS platform providers were able to bring more BBS operators on board, the latter could attract more customers towards BBS through the OTC service. These BBS operators played an important role particularly in areas where the population was relatively uneducated and lacked the knowhow to operate their mobile devices in order to perform these transactions. However, BBS platform providers paid commission to BBS operators per OTC transaction. Therefore, while it helped to have more BBS operators, it was important for BBS providers to promote the use of MA. In the MA channel, the customer directly performed the transactions and the BBS provider received a greater return on each transaction. Similarly, if more merchants were brought on board the BBS platform, the value proposition of using BBS increased for customers. Therefore, our objective is to develop a model that allows us to study mobile-based BBS adoption and difusion as a multisided market phenomenon with same-side and cross-side network efects.

![](/api/attachments/UFTP4GD7/fulltext/images/de616a9b7b8beb69c9b2c3dc461297dc1828dbc341d3505066fe1da184c8fade.jpg)  
Fig. 1. A multisided BBS market.

Two-sided markets which bring two distinct groups of users together have been studied for nearly two decades [12,13]. Examples of two-sided markets include credit cards (merchants-customers), newspapers (advertisers-subscribers), and video games (video game makerscustomers) [14]. Existing literature, mostly in economics and strategy fields, focused on market entry, pricing of the platform under competition, and compatibility strategies, from the platform provider's perspective. It is challenging to build a successful two-sided market due to conflicting interests and complex interactions between various sides. The complexity only increases as the sides brought on board increase [15], and studies of multisided markets are still scarce. A model that ties together a variety of factors and allows an understanding of how diferent incentive mechanisms might afect BBS difusion is lacking in the literature. To fill the gap, we propose a model to specifically study MA difusion from a multisided market perspective.

## 3. Research methodology

## 3.1. Agent-based simulation model

In view of the research objectives, agent-based simulation modelling was adopted to develop the model for the following reasons. First, agent-based simulation models allow for simultaneous investigation of social and economic factors [16,17]. In fact, agent-based computational economics is a growing field that relies heavily on the use of agentbased simulation models [18]. Second, this methodology is considered ideal for modelling complex phenomenon such as difusion dynamics [19,20], since it can reveal the time varying impacts of diferent factors that drive difusion. Third, unlike analytical models agent-based mod elling allows researchers to overcome limitations of analytical tract ability [21]. Fourth, these models can be easily replicated by knowing agents' behaviours, fitness functions and other parameters used to simulate the environment [20]. We developed an agent-based model to simulate a single BBS platform-based market. BBS customers were modelled as active agents with a decision function and appropriate behaviours. Environmental factors were modelled to capture the presence of the BBS platform provider, BBS operators and merchants. Each BBS customer decided the most efective method (OTC or MA) to perform its financial transactions and we monitored difusion of MA amongst the customers over time.

## 3.2. Data collection

In order to better understand and model customer-agent behaviour and interactions in the multisided market, data were collected using three diferent mechanisms. First, a literature review was conducted focusing on studies that investigated the nature of BBS adoption and usage. Second, newsletters published by the financial regulator of the country were studied to understand both the nature of use and trends in the Pakistani BBS market. Third, interviews were conducted with BBS operators, employees and customers of one of the key BBS platform providers in two major cities in Pakistan (see Appendix 1 for details of the interviews<sup>1</sup>). Most of the customers still preferred OTC because of ease of access, ease of use and limited demands (in terms of technical competence) it places on its users, which was consistent with the findings of past empirical studies on mobile-payment adoption [9,22]. Customers' preference towards OTC was further supported by the quarterly branchless banking reports published by the State Bank of Pakistan. However, while the use of OTC has traditionally been associated with blue collar workers and people with limited to no formal education, there was some uptake of MA adoption amongst this segment who were able to either learn the use of MA or able to seek help from operators to operate their MA. This trend was supported by the interviews with customers as well. Although MA could now be created with relative ease and used on a regular basis, it was evident that with more formal education customers were aware of and more willing to use MA services ofered by the BBS provider. Furthermore, as pointed out in the literature [9] and our empirical data, both trust and fear of making the wrong transaction came across as important factors afecting customer's choice of OTC over MA. In light of the literature review and these interviews, behaviours and attributes of the customer agents modelled in the simulation are presented in the following sections.

## 4. Simulation model

## 4.1. Customer agents: attributes, behaviours and the decision function

BBS customers are modelled as agents in the simulation. Their attributes include the mode they use to perform the transactions (OTC or MA), the number of times they have used OTC/MA in the past, risk aversion towards adopting new mode of performing transactions, location in terms of being in a rural or urban location, and financial transaction profile. The financial transaction profile includes the different types of transactions they perform, the frequency with which they perform the transactions and the dollar-value of those transactions. Customer agents can perform three diferent types of transac tions: money transfer, payments and merchant transactions.

In money transfer we consider person-to-person transactions (i.e. one individual sends or receives money from another individual). Diferent transaction fees apply depending on the value of the money being transferred and whether the sender and recipient have MA or not. Payments primarily include utility bill payments where no transaction fee is charged to the customer for making the bill payment. A flat fee is charged by the BBS provider to the utility company for processing each bill. Payments may also include other types of transactions as well, such as topping up mobile account and making donations to charitable organizations etc. In these cases there is either no fee charged to the customer or the same fee is charged regardless of whether the customer is using OTC or MA. Merchant transactions are the third type of transactions which customers may perform on a day-to-day basis and ordinarily require use of cash or other cash-less payment modes (credit/ debit cards). Customers may interact with two types of merchants: brick-and-mortar or online merchants. Brick-and-mortar merchants that accept BBS will accept payment through mobile account (MA) or other conventional means of payment whereas online merchants will accept payment through both OTC and MA. Some movie theatres are examples of brick-and-mortar merchants, who allow tickets to be purchased through MA. Non-MA customers pay through cash or other means. Similarly, a popular e-commerce site daraz.pk, an example of online merchants, accepts payments through either MA or OTC.

The customer agents have only one decision to make in each time period: should they use OTC or MA to perform financial transactions. This decision is taken by comparing the aggregate estimated costs of performing the transactions using OTC or MA through the following decision function:

$$
\frac {\text {Cost of} i - \text {Cost of} j}{\text {Cost of} i} \geq (\text {risk\_aversion}) \times (1 - \% \text {of} j \text {adopters})\tag{1}
$$

The equation (Eq. (1)) shows the decision function evaluated by each customer in each time period where i is the current channel that the customer is using (OTC or MA) and j is the channel that the customer is considering to switch to. This function is designed on the basis of the theory around threshold models in difusion research, where the value or relative cost/benefit of a decision is weighed against a threshold that may represent risk preferences [23] and/or social in fluences [3]. The left-hand side of the decision function represents the average estimated cost saving from adopting payment mode j. Since all customers may not value the numeric cost saving the same way, a threshold is modelled on the right-hand side of the function. This threshold is based on the risk profile of the customer weighted with the network efect (i.e. proportion of adopters using payment mode j that the customer is looking to adopt). In other words, if more customers in the overall network are using j, the overall threshold on the right-hand side of the decision function is lower and the likelihood of the customer adopting j is greater (i.e., same-side network efects). Furthermore, the right-hand side of the decision function captures the perceived risk [9] and social influences [11] discussed in the mobile-based BBS literature.

The cost component captured in the decision function includes estimated setup costs, variable costs and transaction fees for performing the three diferent types of transactions using payment mode OTC or MA. In this case transaction fees represent the price set by the BBS platform provider for the various services ofered over the platform. As discussed in the literature, increasing this price has a negative efect on the adoption of mobile-based BBS. Following is a breakup of the costs (See Eq. (2)),

$$
C o s t o f i = S C + V C + M T C o s t + P M C o s t + M C o s t\tag{2}
$$

SC setup cost =

$$
V C = v a r i a b l e c o s t = [ \# o f m o n e y t r a n s f e r t r a n s a c t i o n s
$$

\+ +of payment transactions proportionOfOnline transactions# (

× ×of merchant transactions cost of finding operator# )]

MTCost cost of performing money transfer transactions=

= ×of MT transactions MTSendingProportion(# )

× + ×MTFee Time to perform transaction valueOfTime[ ( )]

PMCost cost of performing payment transactions =

= #of PM transactions Time to perform transaction valueOfTime× ( × )

MCost Cost of performing merchant transactions=

= ×of merchant transactions Time to perform transaction# (

× valueOfTime.)

<sup>⁎</sup>Note: the parameters used for calculating these diferent costs vary for both OTC vs. MA and rural vs. urban customers.

Table 1 provides details of the factors and parameter values used in evaluating the decision function for OTC/MA and rural/urban customers.

## 4.2. Diferences between OTC and MA in urban/rural areas

Customer agents incur diferent costs when they perform a transaction through OTC or MA and whether the transaction is originating from a rural or urban area. Although the decision function remains the same for the customer agents, the relative costs for diferent compo nents (such as setup costs, transaction fees etc.) change. Therefore, it is important to understand how the behaviour of the customer agent is diferent when choosing to perform the transaction through OTC or MA in a rural/urban setting and how this is tied to the diferent aspects of the decision function (Eq. (1)).

## 4.2.1. Over-the-counter (OTC)

When a customer chooses to perform the transaction through OTC, the customer locates a BBS operator to perform the transaction. Since the transaction itself is performed by the operator, the variable cost incurred by a customer per transaction is essentially the cost of finding the operator and waiting in line for service. This cost may vary depending on how easy it is to locate the operator and whether it is located in a busy/highly populated area. In each period the OTC customer performs one or more of the three types of transactions: money transfer, payments and merchant transactions. In case of merchant transactions, in order to pay through the OTC channel, customers print out a voucher, find the nearest BBS operator, make a payment and update the payment confirmation code online to confirm that a payment has been made.

## 4.2.2. Mobile account (MA)

When a customer chooses to perform the transaction through MA, the customer does not need to locate a BBS operator to perform any of the three types of transactions. However, MA customers do have to manage the cash in their MA which may require them to visit the nearest operator (hence incur the cost of finding the operator) or transfer money into their MA using IBFT (inter-bank fund transfer) services. There is also a setup cost involved which includes not only the one-time fee for setting up the mobile account but also finding an agent who can open the account.<sup>2</sup> Once a MA has been created, there is comparatively lower variable cost of performing the diferent types of transactions with MA than with OTC. Like OTC, there are no additional charges to MA customers for payments. In case of money transfer there are no additional charges if the recipient is a MA customer as well. However, if the recipient is not a MA customer then additional charges apply based on the amount of money being transferred. In addition to the “cost” of having to manage cash with the use of the MA, a customer also has potential benefit of transacting with merchants who may accept MA as a mode of payment. Overall, the benefits of using OTC over MA are a) the relative ease with which the transaction can be performed with the help of the operator and b) easy access to the BBS operators, particularly in rural areas.

## 4.2.3. Urban versus rural customers

In addition to the diferences described above for conducting transactions through OTC and MA, we classify customers into rural and urban segments due to their diferent transaction profiles. For example, many in the rural areas receive money from their family members who are working in urban areas. This is captured by having rural customers “receive” more money transfer transactions compared to urban customers who “send” more money transfer transactions. Furthermore, rural and urban customers have diferent risk profiles drawn from random, normal distributions to capture varying degrees of risk aversion. We assume that on average urban customers have a slightly lower risk profile compared to rural customers [25,26], but there is greater variability in the risk profile of urban customers. Greater variability is modelled into the behaviour of urban customers to capture the fact that there are urban city dwellers as well as rural migrant workers operating in the urban areas.

## 4.3. BBS operators and merchants

BBS operators and merchants are modelled indirectly in the simu lation as part of the simulated environment and their presence afects the behaviour of customers. BBS operators are created at the beginning of the simulation and the distance from the nearest operator is used by customers to calculate setup and variable costs of performing various transactions. Similarly, the presence of merchants is captured in the simulation through the use of the merchant-related-transaction distributions. Increasing proportion of merchant related transactions in the simulation over time allows us to capture the efect of more merchants coming on board the BBS platform. Furthermore, the presence of online versus brick-and-mortar merchants is captured as well. This is important because a brick-and-mortar merchant will only accept MA whereas an online merchant may accept both MA and OTC.

Table 1  
Key factors in the decision function of customers and parameter values.

<table><tr><td>Variable name</td><td>Descriptions and sources</td><td>Urban</td><td>Rural</td></tr><tr><td>Money transfer amount per transaction per customer</td><td>Random normal distribution, where the average numbers have been selected based on the interview data. The only difference between rural and urban customers is the variability.</td><td>OTC: N(13,500,1000)MA: N(13,500,1000)</td><td>OTC:N(13,500, 500);MA: N(13,500,500);</td></tr><tr><td>Number of money transfer transactions per customer.</td><td>Random normal distribution, and the numbers are based on interview data. Most customers will do a few regular transactions (e.g. rural migrant workers will send salary home). MA customers who are more comfortable with the platform will perhaps be able to do more transactions on a regular basis (money transactions with colleagues, friends etc.)</td><td>OTC: N(3,1)MA: N(6,2)</td><td>OTC: N(3, 1);MA: N(4,1);</td></tr><tr><td>Payment amount per transaction per customer.</td><td>Random normal distribution, where the average numbers are taken from interviews and greater variability has been introduced in the context of urban customers.</td><td>OTC: N(9500,3000)MA: N(9500,3000)</td><td>OTC: N(4000, 500);MA: N(4000,500);</td></tr><tr><td>Number of payment transactions per customer.</td><td>Random normal distribution, where the numbers are based on interviews. Urban customers typically have access to more services for which they will be making payments, hence a higher mean for their distribution compared to rural customers</td><td>OTC: N(6,2)MA: N(6,2)</td><td>OTC: N(3, 1);MA: N(3,1);</td></tr><tr><td>Time (in minutes) to perform merchant transactions.</td><td>Random uniform distribution, and the numbers have been chosen on the basis of interviews. They capture the fact that time required to perform transactions with OTC will be higher compared to the time taken with MA. The time it takes to perform a merchant-related transaction using MA is multiplied by the value of time [24] associated by urban or rural customers.</td><td>OTC: U(5, 15)MA: U(2, 4)</td><td>OTC:U(5, 15)MA:U(2, 4)</td></tr><tr><td>Number of merchant transactions</td><td>Random normal distribution, where the numbers are based on interviews. Urban customers will have access to more merchants who accept mobile-based BBS as a mode of payment. Therefore, the average number of merchant transactions is higher for urban customers than rural customers.</td><td>OTC: N(4,2)MA: N(4,2)</td><td>OTC: N(2, 1);MA: N(2,1);</td></tr><tr><td>Setup cost per customer.</td><td>Setup cost of using OTC is 0 since all customers are BBS customers at the start of the simulation. Random normal distribution is used to generate setup cost of MA. This setup cost is incurred each time period when the customer intends to perform transactions in that period with MA. The underlying argument is that with a new technology it takes time to get comfortable with its use. The specific numbers were chosen on the basis of other parameter values. There is an initial high setup cost of MA but each time a customer uses MA, however the next time this cost goes down. Also, this setup cost per period goes down with the availability of more and more BBS operators. The more operators there are in the system, the easier it will be for customers to perform MA transactions (as highlighted in the interviews)</td><td>Setup Cost OTC = 0Setup Cost MA N(200,200)</td><td></td></tr><tr><td>Risk aversion of each customer.</td><td>Random normal distribution. Rural customers have a higher risk profile and urban customers have a lower risk profile (but greater variability). The numbers were chosen arbitrarily to create different types of average risk aversion in the rural and urban populations.</td><td>Low:N(0.3, 0.2)Medium: N(0.5, 0.4)High:N(0.55, 0.1)</td><td>Low:N(0.55, 0.1)Medium: N(0.75, 0.2)High:N(0.8, 0.05)</td></tr></table>

Note: In addition to these parameters, transaction fees for diferent types of transactions were obtained from one of the BBS provider's website.

This approach allows us to capture the essence of multi-sided markets. Changing number of operators has an impact on the decision function of customers looking to use OTC vs MA for their transactions. Greater presence of operators means that customers find it easier to perform transactions through OTC and may not be inclined towards using MA. Similarly, greater number of merchant related transactions may also make MA more attractive for customers than OTC. In sum, we model operators and merchants via cross-side network efects in the simulation.

## 4.4. Simulation flow and experiments

Fig. 2 shows the overall flow of the simulation using a Business Process Model and Notation (BPMN) diagram. BPMN diagrams have been used in the past to describe the overall behaviour of an agentbased simulation model [27]. The simulation begins with the creation of a simulated BBS market consisting of designated areas for rural or urban customers, BBS operators and merchants (i.e., please see the first few boxes of the Environment pool lane). Then customer agents are created and assigned to rural and urban patches of the simulated en vironment (i.e., please refer to the Customer pool lane). This is followed by assignment of an existing channel for BBS services and a BBS transaction profile indicating the volume and value of BBS transactions to be conducted by each customer in each time period. Tables 1 and 2 show attributes and behaviours of agents, environmental variables and key features of the overall BBS market modelled in the simulation.

The simulation consists of agents who are BBS customers. At the beginning of the simulation a small proportion of these customers are MA customers and the rest are OTC customers. In each time period a customer decides whether to perform BBS transactions in that period using OTC or MA on the basis of the decision function (see Eq. (1) and second half of the Customer pool lane in Fig. 2). At the end of each period the number of customers who performed transactions using OTC or MA is recorded. Since MA is the new payment mode in the market, MA customers incur a setup cost each time they choose to perform transactions in a period using MA. For first time MA customers the setup cost is high. However, as MA customers continue to use MA and become familiar with the new mode of conducting BBS transactions, the setup cost drops quickly. Furthermore, this setup cost is related to the number of available operators in the simulation – higher the number of operators, lower the setup cost of MA.

A $3 \times 5 \times 5 \times 6 ~ ( = 4 5 0 )$ experiment was designed to explore the impact of 4 key variables that capture the diferent sides of the market: risk profile (low, medium, high), growth in merchant transactions (0%, 5%, 10%, 20%, 40%), growth in the number of operators (0, 5, 10, 20, 40), and proportion of online-merchants transactions (0%, 20%, 40%, 60%, 80%, 100%). The number of replications for each one of the 450 parameter combinations was 50 (hence N = 22,500). In each instance, the simulation was run for 60 time periods (or 5 years). Since each time period in the simulation represents one month, a 5-year window is good enough to investigate difusion of a particular technology. A smaller window would be too small for us to understand impacts over time and a larger window may become less meaningful as the underlying technology in the BBS market may evolve (e.g., with the arrival of 4G services). The model was developed using NetLogo [28]. Four diferent difusion criteria were defined to investigate the impact of the key variables on MA difusion over time: 25%, 50%, 100% and 150% in crease in MA adopters. In other words, difusion was said to occur if there was a 25% increase in terms of the number of MA adopters (from the start of the simulation), or a 50% increase in number of MA adopters and so on. Furthermore, this increase was measured not only at an aggregate level of the customer population but also for rural and urban customers separately. Using multiple dependent variables helped understand the relative impact of the key variables on diferent customers.

![](/api/attachments/UFTP4GD7/fulltext/images/ebf874e5170f5bbc8e8d17f8181c63c304e1ef91dc7fb5778d2be3fbf2ff9c42.jpg)  
Fig. 2. BPMN diagram for the simulation.

## 5. Results and analysis

Fig. 3 shows the average MA adoption paths for urban and rural populations across all experiments. The figure shows MA adopters as a percentage of their respective overall population (i.e. urban vs. rural) over the course of the simulation (60 time periods). For example, on average the overall rural population is 68% (of 5000 = 3400) and urban population is 32% (of 5000 = 1600). Hence, the graph shows the average urban MA adopters over the course of the simulation as a percentage of the overall urban population (1600) and the average rural MA adopters as a percentage of the overall rural population (3400). The starting point for both curves is about the same because the relative proportion of MA adopters in both urban and rural population is the same (about 35%) at the beginning of the simulation (please refer to Table 2). The shape of the curves suggests that a) on average the rate of difusion is much faster in the urban population than in the rural population; b) MA is able to penetrate the urban population more than the rural population; and c) rural MA adoption does not pick up until

## Table 2

Key factors and parameter values for the simulation model.

<table><tr><td>Description</td><td>Parameter value</td></tr><tr><td>Total number of BBS customers</td><td>5000</td></tr><tr><td>Total number of operators in the simulation</td><td>15</td></tr><tr><td>Proportion of rural customers (Pakistan Bureau of Statistics Census 2017)a</td><td>68%</td></tr><tr><td>Proportion of OTC customers in the population based on most recent industry numbers reported by the regulator [State Bank of Pakistan&#x27;s Quarterly report on Branchless Banking]</td><td>65%</td></tr><tr><td rowspan="2">Spending proportion estimates: percentage of money transfer transactions for rural and urban customers that will involve sending money (hence a fee to be incurred by the customer).</td><td>80% [rural]</td></tr><tr><td>20% [urban]</td></tr><tr><td>Merchant growth rate is a proxy for new merchants brought on board by the BBS platform provider. It captures the average percentage increase in transactions performed with merchants (both brick and mortar and online merchants). This increase takes place after every time period in the simulation (1 month).</td><td>0%, 5%, 10%, 20%, 40%</td></tr><tr><td>Proportion of online merchant related transactions. This is a proxy for capturing the effect of online merchants (e.g. daraz.pk). 0% is an indicator that merchant transactions are entirely from brick-and-mortar stores whereas 100% means merchant transactions are entirely from online stores</td><td>0%, 20%, 40%, 60%, 80%, 100%</td></tr><tr><td>Operator growth rate estimate captures the increase in number of operators after every time period (1 month) in the simulation. This value was based on overall industry growth in operators over the past several years (State Bank of Pakistan&#x27;s Quarterly reports on Branchless Banking)</td><td>0, 10, 20, 40 operators</td></tr><tr><td rowspan="2">Monetary value of time for rural and urban customers. PKR: Pakistani Rupee 1 PKR = 0.0095 USD as of Jan 5th 2016. So for example, the average rural and urban incomes are PKR 30110 and PKR 45283 respectivelyb. Assuming 240 working days in a year and a 6-day, 8-h work week, the PKR value per minute for rural customers is (30,110/240 days/480 min) 0.26 and for urban customers it is (45,283/240 days/480 min) 0.39. When an action by a rural or urban consumer is measured in terms of time, such as the time it takes to perform a money transfer transaction, the cost of that time can be calculated by multiplying it by this PKR value per minute.</td><td>0.26 [rural]</td></tr><tr><td>0.39 [urban]</td></tr><tr><td>Replications of each simulated condition</td><td>50</td></tr></table>

![](/api/attachments/UFTP4GD7/fulltext/images/ec4e3a7994e0c5a2574b02d4a3feb698b7d218d5ae7ac4a22af2064d3ed783b2.jpg)  
Fig. 3. Average MA difusion path within the rural and urban population over the course of the simulation.

there has been an uptake in the urban MA adoption.

The curves in Fig. 3 only represent average adoption paths over all experimental conditions. A diferent perspective on difusion was adopted by specifically measuring the time it took for difusion to occur within the rural and urban populations. Various difusion time measures enabled us to quantify difusion dynamics and statistically examine both main and interaction efects. Table 3 reports summary statistics for those time measures and suggests statistically significant correlation between urban MA adopters and rural MA adopters for the four diferent difusion criteria. The comparatively low correlation between time for MA difusion to occur for 25% increase in adopters shows that the difusion paths for urban and rural population tend to be diferent in the beginning of the simulation. This is supported by a visual inspection of Fig. 3. However, as the difusion criteria was changed to 50%, 100% and 150% increase, there was higher correlation between time for MA difusion to occur for both rural and urban customers. This indicates that a) there may be diferent factors that motivate adoption in the early stages amongst the two types of customers and b) eventually network efects kick in and help promote difusion across both populations in general but particularly in the rural population. Both these observations were further investigated in subsequent analyses. Interestingly, the average times for MA adopters to reach 50% or 100% increase was the same as indicated in the third and fourth col umns of Table 3. This suggests that there is a clear difference in the difusion paths at the start of the simulation but once difusion picks up in both populations it quickly spreads beyond 50–100% increase in adopters. Therefore, in subsequent analyses, only one set of numbers (i.e., 100% increase in adopters) have been reported in the paper.

A full factorial multiple analysis of variance (MANOVA) was conducted to determine whether the key variables (risk profile, growth in merchant transactions, growth in operators and growth in online mer chant transactions) had an overall impact on MA adopters in rural and urban populations [29] under diferent difusion criteria. Due to space limitations the full results have not been reported in the paper. Box's tests for equality of covariance matrices and Levene's statistic for equality of variances were significant. However, in view of comparable and large sample sizes across the groups, Pillai's Trace values generated by SPSS were used to interpret the efect of the independent variables [30] and a more stringent α = 0.01 value was adopted to test for statistical significance [31]. In addition to statistical significance, practical significance was analysed in view of the large sample sizes [32]. All factors and interaction terms that showed practical significance (partial $\eta ^ { 2 } > 0 . 1 4 )$ were retained for subsequent analyses. Univariate ANOVAs on urban and rural MA adopters were analysed to understand the relative impact of key variables and interaction terms on difusion over time [33].

## 5.1. Main efects

In multivariate tests, all main efects of risk profile, merchant related transactions, operators and online transactions were statistically (p = 0.00) and practically significant (partial $\eta ^ { 2 } > 0 . 1 4 )$ under all difusion criteria (some details of the SPSS output have been moved to Appendix 2<sup>3</sup>). However, univariate ANOVA revealed diferences in terms of the impact of these variables on time for MA difusion to occur in urban and rural populations over the course of the simulation.

## 5.1.1. Main efects: urban population

Risk profile and merchant transactions were significant over the course of MA diffusion in the urban population (Table 4a). Pairwise comparison tests showed that

Result 1. Increasing risk profile reduced time for MA difusion to occur in the urban population.

Result 2. Increasing merchant transactions reduced time for MA difusion to occur in the urban population.

Proportion of online transactions had no practical significance on

## Table 3

Summary statistics for urban/rural MA difusion over time.

<table><tr><td rowspan="2"></td><td colspan="4">Diffusion criteria</td></tr><tr><td>25% Increase</td><td>50% Increase</td><td>100% Increase</td><td>150% Increase</td></tr><tr><td>Correlation between urban and rural MA adopters</td><td>0.349*</td><td>0.610*</td><td>0.610*</td><td>0.683*</td></tr><tr><td>Urban: time for MA diffusion to occur (Mean, Std. Dev.) over all experimental conditions</td><td>6.91, 14.28</td><td>18.25, 20.41</td><td>18.25, 20.41</td><td>24.25, 21.60</td></tr><tr><td>Rural: time for MA diffusion to occur (Mean, Std. Dev)</td><td>35.25, 20.83</td><td>36.92, 20.30</td><td>36.92, 20.30</td><td>37.82, 19.97</td></tr></table>

Table 4a  
Tests of between-subjects efects for urban customers.

<table><tr><td rowspan="3"></td><td colspan="6">Urban customers</td></tr><tr><td colspan="2">25% Increase</td><td colspan="2">100% Increase</td><td colspan="2">150% Increase</td></tr><tr><td>F</td><td>Partial  $\eta^2$ </td><td>F</td><td>Partial  $\eta^2$ </td><td>F</td><td>Partial  $\eta^2$ </td></tr><tr><td>Risk profile</td><td>22562</td><td>0.67</td><td>133443</td><td>0.92</td><td>32141</td><td>0.75</td></tr><tr><td>Merchant</td><td>4313</td><td>0.44</td><td>73854</td><td>0.93</td><td>24771</td><td>0.82</td></tr><tr><td>Operators</td><td>382</td><td>0.07</td><td>2238</td><td>0.29</td><td>564</td><td>0.09</td></tr><tr><td>Online</td><td>250</td><td>0.05</td><td>469</td><td>0.10</td><td>152</td><td>0.03</td></tr></table>

Note: factors with shaded values are practically insignificant.

urban MA difusion. This makes sense because access to online mer chants required incurring a variable cost. If the customer were looking to perform the online transaction using MA then the variable cost was 0 and if the customer were looking to perform this transaction through OTC then the variable cost was the same as the cost of finding the nearest operator who would help to perform the transaction. Therefore, access to merchants was more important as it ofered greater value proposition than access to a particular type of merchant.

Similarly, the efect of number of operators was insignificant in itially (25% increase in adopters) and later on (150% increase in MA adopters) but significant in the middle (with 50% and 100% increase in MA adopters). In other words, access to operators did not kick start MA difusion in the urban population. In fact, access to more operators reduced overall cost of performing transactions through OTC. However, the increasing number of operators reduced setup costs over time in the intermediate period. Our interviews indicated that sometimes MA customers went to the operators for help with operating the MA. Once MA adoption moved beyond a certain threshold (> 100% of the starting population), more operators in the simulation made little difference to subsequent MA adoption since setup costs were relatively low. This curvilinear relationship between the increasing number of operators and difusion time was further supported by pairwise comparison tests on the diferent levels of operators.

Result 3. Increasing the number of operators initially reduced time $f o r$ urban MA difusion but the efect was weakened as the number of operators became too high.

## 5.1.2. Main efects: rural population

For rural customers, all main efects were practically significant as well (Table 4b). This is interesting because Table 3 and Fig. 2 show that, in general, difusion took longer to occur in the rural population despite this being the larger of the two types of populations modelled in the simulation. We know from past research that if the rate of difusion is fast, there are typically one or two factors driving that rapid difusion and all other factors are overshadowed and appear less important [20]. This appears to be the case for the urban population. However, in circumstances where difusion is slow (the rural population), more factors have an opportunity to impact difusion. For example, as discussed above, access to online merchants afected the use of OTC more than the use of MA as modelled in the decision function. In the urban population where difusion took place much faster on average, access to online merchants made no diference on average time for difusion to occur. On the other hand, in the case of rural population, access to online merchants was significant presumably because most of the rural customers were using OTC and online transactions could be performed with some additional cost using OTC.

Result 4. Increasing risk profile reduced time for MA difusion to occur in the rural population

Result 5. Increasing merchant transactions reduced time for MA difusion to occur in the rural population.

Result 6. Increasing number of operators initially reduced time for rural MA difusion to occur but the efect was weakened as the number of operators became too high

Result 7. Increasing online merchant transactions reduced time for MA difusion to occur in the rural population

Collectively, the results showed that all four factors were important for the difusion of MA in the rural and urban populations with two exceptions: First, presence of online merchants was not as relevant for MA difusion in the urban population as compared to the other factors. Second presence of BBS operators initially hampered MA difusion but a growing number of operators eventually helped MA difusion in the urban population

## 5.2. Interaction efects: two-way

In multivariate tests for the overall population, all two-way interaction efects for risk profile, merchant related transactions, operators and online transactions were statistically significant (p = 0.00). The interaction term between risk profile and online merchant related transactions was practically insignificant under all difusion criteria (partial $\eta ^ { 2 } < 0 . 1 4 )$ . Similarly, the interaction between risk profile and number of operators was practically insignificant for 25% increase in MA adopters and 150% increase in MA adopters. Interestingly the positive efect of all other two-way interaction terms suggested an important efect of the diferent sides of the market (merchants, operators and customers) on the overall MA difusion. This was investigated further by focusing on urban and rural populations.

## 5.2.1. Two-way interaction efects: urban population

Tests of between-subjects efects for the interaction terms revealed that nearly all the interaction terms were practically insignificant for the urban population (see Table 5a for details). One notable exception was the interaction term between risk profile and merchant related transactions (see Fig. 4). Increase in merchant related transactions on its own helped MA difusion. Increase in risk profile on its own dam pened MA difusion. The two together showed that with high risk profile, the positive efect of increasing merchant related transactions was clearly visible (greater diference between the average time for difusion to occur between the three curves). On the other hand, with low risk profile (conditions which were favourable for MA difusion), increasing merchant related transactions did not create that much of an impact on MA difusion (curves are closer to each other).

Tests of between-subjects efects for rural customers.

<table><tr><td rowspan="3"></td><td colspan="6">Rural customers</td></tr><tr><td colspan="2">25% Increase</td><td colspan="2">100% Increase</td><td colspan="2">150% Increase</td></tr><tr><td>F</td><td>Partial η2</td><td>F</td><td>Partial η2</td><td>F</td><td>Partial η2</td></tr><tr><td>Risk profile</td><td>31,029</td><td>0.74</td><td>26,227</td><td>0.70</td><td>18,739</td><td>0.63</td></tr><tr><td>Merchant</td><td>2,933,493</td><td>1.00</td><td>5,865,890</td><td>1.00</td><td>8,458,959</td><td>1.00</td></tr><tr><td>Operators</td><td>53,012</td><td>0.91</td><td>69,753</td><td>0.93</td><td>69,815</td><td>0.93</td></tr><tr><td>Online</td><td>11,549</td><td>0.72</td><td>16,078</td><td>0.79</td><td>18,015</td><td>0.80</td></tr></table>

Table 5a  
Test of between-subjects efects for the two-way interaction terms for urban customers.

<table><tr><td rowspan="3"></td><td colspan="6">Urban Customers</td></tr><tr><td colspan="2">25% Increase</td><td colspan="2">100% Increase</td><td colspan="2">150% Increase</td></tr><tr><td>F</td><td>Partial η2</td><td>F</td><td>Partial η2</td><td>F</td><td>Partial η2</td></tr><tr><td>Risk profile × merchant</td><td>4313</td><td>.61</td><td>18582</td><td>.87</td><td>3126</td><td>.53</td></tr><tr><td>Risk profile × operators</td><td>382</td><td>.12</td><td>561</td><td>.17</td><td>16</td><td>.01</td></tr><tr><td>Risk profile × online</td><td>250</td><td>.10</td><td>82</td><td>.04</td><td>0</td><td>.00</td></tr><tr><td>Merchant × operators</td><td>47</td><td>.03</td><td>317</td><td>.19</td><td>77</td><td>.05</td></tr><tr><td>Merchant × online</td><td>29</td><td>.03</td><td>31</td><td>.03</td><td>9</td><td>.00</td></tr><tr><td>Operators × online</td><td>4</td><td>.00</td><td>57</td><td>.05</td><td>13</td><td>.01</td></tr></table>

Note: factors with shaded values are practically insignificant.

The interaction terms a) operator × risk profile and b) operator × merchant related transactions are practically significant only when there is a 100% increase in MA adopters. In both cases the efect size increases and then decreases with 25%, 100% and 150% increase in MA adopters. This pattern is consistent with the main efect of operators on the difusion of MA in the urban population (Table 4a). This leads to the following conclusion:

Result 8a. Increasing risk profile strengthens the positive efect of merchant transactions in the urban population.

## 5.2.2. Two-way interaction efect: rural population

Tests of between-subjects efects for the interaction terms revealed that nearly all the interaction terms were practically significant for the rural population (see Table 5b for details). There were two exceptions. The first was the interaction term between risk profile and proportion of online merchant related transactions and the second was the interaction term between risk profile and operators.

Fig. 5 shows the interaction efect between risk profile and merchant related transactions on rural customers. In this case, unlike the case of the urban population, reducing the risk profile enhances the positive efect of adding merchant related transactions on MA difusion. In other words, in Fig. 5, there is a wider gap between the three curves with low risk profile than there is with high risk profile. In case of rural population, MA difusion is slow. In such conditions low risk profile and more merchant transactions jointly enhance difusion. On the other hand, in case of urban population, difusion is fast. In such conditions, low risk profile alone creates very favourable conditions for urban MA difusion. Additional benefits from further increasing merchant transactions tend to be less visible. Similar efects have been observed in past research as well [20]. When the overall speed of difusion is fast, there are usually one or two overriding factors that rapidly drive difusion. However, if the overall difusion is slow then factors that otherwise appeared less important do appear to impact difusion. In the present scenario it is obvious that difusion is slower in the rural population. Hence, some of the factors do appear to impact difusion in the rural population over time. On the other hand, in case of the urban population one or two factors rapidly drive difusion and dominate the impacts of other factors.

Table 5b  
Test of between-subjects efects for the two-way interaction terms for rural customers.

<table><tr><td rowspan="3"></td><td colspan="6">Rural Customers</td></tr><tr><td colspan="2">25% Increase</td><td colspan="2">100% Increase</td><td colspan="2">150% Increase</td></tr><tr><td>F</td><td>Partial η2</td><td>F</td><td>Partial η2</td><td>F</td><td>Partial η2</td></tr><tr><td>Risk profile × merchant</td><td>3938</td><td>.59</td><td>2978</td><td>.52</td><td>2627</td><td>.49</td></tr><tr><td>Risk profile × operators</td><td>519</td><td>.16</td><td>616</td><td>.18</td><td>158</td><td>.05</td></tr><tr><td>Risk profile × online</td><td>99</td><td>.04</td><td>35</td><td>.02</td><td>3</td><td>.00</td></tr><tr><td>Merchant × operators</td><td>10178</td><td>.88</td><td>11423</td><td>.89</td><td>9410</td><td>.87</td></tr><tr><td>Merchant × online</td><td>1249</td><td>.53</td><td>1622</td><td>.60</td><td>1792</td><td>.62</td></tr><tr><td>Operators × online</td><td>2622</td><td>.70</td><td>4206</td><td>.79</td><td>4373</td><td>.80</td></tr></table>

Note: factors with shaded values are practically insignificant

![](/api/attachments/UFTP4GD7/fulltext/images/9fed9f649797580b4d76e03dc6848f70cada55493a76e9c5e3da46ee15a6ee3f.jpg)  
Fig. 5. Interaction efect between risk profile and merchant related transactions for rural customers where difusion is defined as 150% increase in MA adopters.

![](/api/attachments/UFTP4GD7/fulltext/images/d03db8d270c83425c57aa19a55311d258fa8462117fe2f9ec4aed082097f93f9.jpg)  
Fig. 4. Interaction efect between risk profile and merchant related transactions for urban customers where difusion is defined as 150% increase in MA adopters.

Test of between-subjects efects for higher order interaction terms on urban customers.

<table><tr><td rowspan="2"></td><td colspan="2">25% Increase</td><td colspan="2">100% Increase</td><td colspan="2">150% Increase</td></tr><tr><td>F</td><td>Partial  $\eta^2$ </td><td>F</td><td>Partial  $\eta^2$ </td><td>F</td><td>Partial  $\eta^2$ </td></tr><tr><td>Risk profile × merchant × operator</td><td>47</td><td>.06</td><td>80</td><td>.11</td><td>25</td><td>.04</td></tr><tr><td>Risk profile × merchant × online</td><td>29</td><td>.05</td><td>8</td><td>.02</td><td>6</td><td>.01</td></tr><tr><td>Risk profile × operator × online</td><td>40</td><td>.01</td><td>15</td><td>.03</td><td>3</td><td>.01</td></tr><tr><td>Merchant × operator × online</td><td>2</td><td>.01</td><td>8</td><td>.03</td><td>3</td><td>.01</td></tr><tr><td>Risk</td><td>2</td><td>.01</td><td>2</td><td>.02</td><td>1</td><td>.01</td></tr><tr><td>profile × merchant × operator × online</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Note: factors with shaded values are practically insignificant.

Result 8b. Increasing risk profile weakens the positive efect of merchant transactions in the rural population.

In summation, one of the key findings of the two-way interaction efects was that both risk aversion of end consumers and presence of more merchants on the BBS platform unexpectedly afected MA difusion diferently across rural and urban populations.

## 5.3. Interaction efects: higher order terms

The efects of higher order interaction terms were practically in significant barring two exceptions: a) the efect between merchants, operators and online merchants was practically significant across all difusion criteria; b) the efect of risk profile, merchants and operators was practically significant initially (25% and 100% increase in MA adopters) but insignificant later on (150% increase in MA adopters). These interactions were investigated further in the context of urban and rural populations.

## 5.3.1. Three-way interaction efect: urban population

The efects of all higher order interaction terms on urban population were practically insignificant (Table 6a). This was not surprising in view of the overall practically insignificant two-way interaction efects on the urban population. Although there was strong two-way interaction between risk profile and merchant transactions (Table 5a), there was no interaction between these two variables and operators.

## 5.3.2. Three-way interaction efect: rural population

In case of the rural population only two interaction terms were significant: a) risk profile, merchant transactions and operators, and b) merchant transactions, operators and online transactions (Table 6b). Unlike the case of urban customers, online transactions had a strong impact on the difusion of MA in the rural population.

Fig. 6a–c capture the three-way interaction between risk profile, merchant transactions and operators where difusion defined as 25% increase in MA adopters. Fig. 6a is for low risk profile and 6b, 6c are for medium, and higher risk profiles. Each of the three figures shows two way interaction between merchant transactions and operators. Reading the figures from top to bottom (lower to higher risk profile) it can be

## Table 6b

Test of between-subjects efects for higher order interaction terms on rural customers.

<table><tr><td rowspan="2"></td><td colspan="2">25% Increase</td><td colspan="2">100% Increase</td><td colspan="2">150% Increase</td></tr><tr><td>F</td><td>Partial  $\eta^2$ </td><td>F</td><td>Partial  $\eta^2$ </td><td>F</td><td>Partial  $\eta^2$ </td></tr><tr><td>Risk profile × merchant × operator</td><td>276</td><td>.29</td><td>445</td><td>.39</td><td>144</td><td>.17</td></tr><tr><td>Risk profile × merchant × online</td><td>77</td><td>.12</td><td>40</td><td>.07</td><td>16</td><td>.03</td></tr><tr><td>Risk profile × operator × online</td><td>9</td><td>.02</td><td>15</td><td>.03</td><td>4</td><td>.01</td></tr><tr><td>Merchant × operator × online</td><td>654</td><td>.70</td><td>1027</td><td>.79</td><td>991</td><td>.78</td></tr><tr><td>Risk profile × merchant × operator × online</td><td>9</td><td>.06</td><td>18</td><td>.12</td><td>9</td><td>.06</td></tr></table>

Note: factors with shaded values are practically insignificant.

seen that the interaction between merchant transactions and new operators on overall time for difusion to occur is reduced with the in crease in risk profile. This result is very interesting because it clearly shows a BBS platform provider can simultaneously benefit from bringing both operators and merchants on board provided the target customers have a low risk profile. Fig. 6a shows that with 5% increase in merchant transactions (dotted line in the middle) and adding high number of operators (40), average time for difusion to occur is actually better than with adding lower number of operators (20). Of course, adding more merchants to the platform (solid line in Fig. 6a) is better than adding fewer merchants (dotted line).

Result 9. Under low risk profile the BBS platform can help rural MA difusion by bringing both merchants and operators on board.

Similarly, Fig. 7a–c capture the three-way interaction between merchant transactions, operators and online merchants where difusion is defined as 25% increase in MA adopters. Fig. 7a is for 0% online transactions, 7b shows 40% online transactions and 7c shows 80% online transactions. Reading the figures from top to bottom (increasing proportion of online transactions), it can be seen that the interaction between merchant transactions and new operators on overall time for difusion to occur is strengthened with the increase in online transactions. This efect is more accentuated particularly when you look at the diference between time for difusion to occur across the three graphs when there are 0 to 20 new operators added to the simulation.

Result 10. The positive efect of increasing merchants and operators on rural MA difusion is further strengthened if more online merchants are brought on board the BBS platform.

Collectively, the higher order interaction efects show that the three sides of the market, end-customers, BBS operators and merchants, afect each other very diferently and factors such as risk aversion and online merchants' impact MA difusion across rural and urban populations diferently as well.

## 6. Discussion

The overall objective of the research was to investigate the collective efect of key factors on difusion of MA across urban and rural populations over time. An agent-based simulation modelling approach was adopted to simultaneously model the diferent sides of the mobilebased BBS market in the context of a developing country. Our experiments revealed several important findings. First, bringing more merchants and operators on board the BBS platform significantly afected the difusion dynamics of MA amongst rural and urban customers. Second, the relative impact of key factors changed over the course of the simulation. For example, increasing BBS operators encouraged consumers to opt for OTC instead of MA in the early stages of the diffusion process (when difusion criterion was defined as 25% increase in MA adopters). However, when other factors such as risk aversion of the customers and/or increasing presence of merchants drove MA difusion and a sizeable proportion of customers switched to MA, presence of BBS operators actually further promoted MA adoption. This is because now the BBS operators were not being viewed as an alternative to MA (which had become the dominant channel in the market) but were instead being used to help manage MA for the customers (e.g., managing cash in the account and facilitating new customers in performing MAbased transactions etc.). An important implication is that from a BBS provider's perspective, not only is there a trade-of involved in bringing merchants and operators on board the BBS platform, the timing of in centivizing these diferent sides of the market is important as well. Third, the relative impact of key factors was diferent on rural and urban populations. For example, in the context of the rural population main efects and higher order interaction efects were more important than in the case of the urban population in driving MA difusion. This was because difusion of MA was slower in the case of the rural population which allowed all key factors to have an impact on the difusion process. A simple albeit important implication is that under harder difusion conditions (perhaps because of the characteristics of the target population), the technology provider needs to adopt a strategy to stimulate all sides of the market for the technology to dif fuse. Fourth, lower risk profile of target customers facilitated MA dif fusion and this efect was reinforced with the presence of more merchants and operators on board the BBS platform. Higher risk profile of target customers made it dificult for MA difusion to occur and under such circumstances increasing merchants on the BBS platform favored MA difusion more in the urban population than in the rural population. Furthermore, online merchants had a stronger impact on MA difusion in the rural population than in the urban population. In the following subsections we discuss the implications of our work for both research and practice.

![](/api/attachments/UFTP4GD7/fulltext/images/36a910886ad5093197dabadea56badb2b29d31cd03f1189a04cf3adef247c893.jpg)

![](/api/attachments/UFTP4GD7/fulltext/images/e14488907907cab092e22eadac4682e1d7c71d98783b40eb7c7978fbab59e502.jpg)

![](/api/attachments/UFTP4GD7/fulltext/images/3e166ac18a36e9e63a452033b6b578e9db30a5d56ff12bf33b74e65a79d11541.jpg)  
Increase in merchant transactions

Fig. 6. Three-way interaction between merchant transactions, operators and risk profile for rural customers. Left (6a: low risk profile), middle (6b: medium risk profile), right (6c: high risk profile).  
a  
![](/api/attachments/UFTP4GD7/fulltext/images/dfabec51dfad00de95a5404558af6c77acfe14e1e6945a49ea89594ae68d267b.jpg)

![](/api/attachments/UFTP4GD7/fulltext/images/a06b67ef1b46fc32ec58cc9a294b96e78d8071453c1bd3d6794e541c3d7cd945.jpg)

C  
![](/api/attachments/UFTP4GD7/fulltext/images/5e8819a5e64ea8bc7482f7986af3b7b3549214f047dc722f78550a7bc8cae3ab.jpg)  
Increase in merchant transactions  
Fig. 7. Three-way interaction between merchant transactions, operators and online transactions for rural customers. Left (7a: 0% online), middle (7b: 40% online), right (7c: 80% online).

## 6.1. Model validation and generalizability of findings

Although we took great care in developing the model on the basis of literature review and empirical data, it is important to discuss the validity of the model and robustness of our findings. Lazer and Friedman [34] discussed four criteria for assessing the validity of a simulation model: 1) face validity i.e. the behaviour of the model should closely follow reality. This criterion is satisfied because individual-level beha viour of the agents has been modelled on the basis of practitioner re ports, literature review and empirical data; 2) robustness i.e. the key results should not change in the face of trivial changes to the model. This criterion is satisfied because our overarching results are based on a series of experiments that involved a range of diferent parameters and multiple simulation runs; 3) replicability i.e. other researchers should be able to completely replicate the results of this study. The detailed description of the simulated environment, simulation parameters, agents, attributes and behaviours of the agents and the overall flow of the simulation ensure that any researcher will be able to replicate our study; 4) “non-obvious non-trivial results” i.e. the model should allow the researchers to put forth new and insightful findings. In this regard, some of the results reported in the study such as Results 3, 6, 8a, 8b, 9 and 10 all provide new perspectives on the difusion dynamics of MA compared to the collective understanding from past empirical studies on this topic.

Despite the fact that parameter values for key variables were chosen from the Pakistani market, we believe that the model and its findings are generalizable. First, our model accurately captures the essential elements of the multisided BBS market. Specifically, characteristics and behaviours of end customers, BBS platform providers, merchants and BBS operators have all been considered in the model. While we can argue over the specific parameter values and whether they would be applicable in the context of another country such as China, or Kenya, or Bangladesh, it can be argued that the structure of the model is sound and fairly generalizable. Second, we conducted extensive sensitivity analysis by randomly drawing samples from distributions to ensure robustness of our results. It is possible that if the model is applied in another context, the efect sizes we observe for diferent terms may vary. Nevertheless, we believe our findings are not tied to isolated scenarios or specific values. In light of these points we believe that our framework is generalizable in the context of other technologies that are part of multi-sided markets and other geographies where similar dynamics exist in the context of adopting new technologies.

## 6.2. Research implications

First. we offer a simulation based model that merges the literature on BBS adoption and difusion with the multisided nature of this market. Second, our results demonstrate the importance of simulta neously studying the efect of the multiple sides of the BBS market. In the past, empirical work had focused primarily on consumers of MA from an adoption [22] and continued use perspective [35]. However, the strong interaction efects between the diferent sides of the market provide suficient evidence of the richness and efectiveness of our approach. Third, unlike prior research that adopted a static approach towards investigation of adoption and difusion of MA (see for example [35]), a simulation-based approach allowed for an investigation of key factors and their interaction over time. Collectively, Tables 3–6b showed that the manner in which the three sides of the market (op erators, merchants and customers) interacted with each other changed over the course of the simulation as well. We demonstrated that factors such as perceived risk, which are commonly discussed in the context of technology adoption, interact with other variables and may afect MA difusion diferently for rural and urban customers. Furthermore, we demonstrated that many of the factors discussed in the literature in the context of mobile-based payment adoption have a diferent impact over the course of the difusion process. For example, factors such as ease of use (afected in this context by the availability of BBS operators) and perceived value (afected by the presence of merchants who can accept BBS as a mode of payment) change over time and can be influenced by the BBS platform providers to afect the overall difusion process. Fourth. we highlighted how the different sides of the market interact diferently for rural and urban consumer segments. BBS platform providers should be more sensitive in terms of devising strategies for promoting their solutions to urban and rural BBS customers. Our results confirm that not only do end customers weigh MA and OTC diferently, the trade-ofs involved in bringing merchants and BBS operators on board the platform are different for rural and urban customers as well Fifth, given the model has been developed on the basis of empirical data and is able to capture dynamics of the multisided markets, it can be used and extended in future research for a more rigorous investigation of competitive dynamics between multiple BBS platforms [36]. This is one of the first research studies to focus on an important, yet under researched topic. While this model provides rich insights, it is possible that a more sophisticated model development with a different decision function (and conceptualization of consumer behaviour) using addi tional data can be undertaken.

## 6.3. Practical implications

Our results also ofer important implications to BBS platform providers to promote and encourage the BBS mobile channels. Our findings suggest that BBS platform providers should diferentiate incentive strategies to rural and urban customers. First, it can be seen that in the context of the urban population low risk profile and increase in mer chant transactions are the key driving factors of MA difusion. BBS were originally introduced with the rural, un-banked population as the primary target. Despite growing popularity of these services, an efective use case for the urban population (with access to conventional banking services) on a large scale has vet to emerge. The simulation results suggest that if BBS platform providers are able to bring more merchants on board, it increases the chances of urban customers to adopt MA. Thi result is supported to some extent by past research on why the BBS markets have taken of in some countries more so than in others [37]. Second, in case of the rural population the presence of operators and online merchants both play an important role in addition to risk profile and access to merchants. This is an important result at multiple levels: a) BBS platform providers cannot adopt the same strategy that they have adopted in the past for OTC with rural customers for difusing MA; b) even within the context of MA the strategy that works with rural customers may not be as efective with urban customers. For example, access to online merchants has a stronger appeal for rural customers than it has for the urban population who in any case have greater access to brick-and-mortar merchants. Overall, it is important to coordinate stakeholders from multiple sides of the market and diferentiate incentive strategies to diferent customer segments.

The value of mathematical modelling lies in its ability to identify key variables and structure the debate of how a phenomenon of interest can be managed [38]. Our decision function can be used by BBS providers to understand and influence agent behaviour. Managers could brainstorm how diferent types of advertisements could influence components of the decision functions. Advertising could emphasize ease of learning (set up costs), reduced wait time, access to a greater range of merchants, estimated transaction volume, and other factors. Our research emphasizes the need to treat rural and urban populations diferently. The model could also influence data gathering and model enhancement to understand the dynamics of the marketplace. We hope that our research can serve as a starting point for further analysis of multisided markets that may benefit from a similar analysis such as NFC-based devices, 4G/5G mobile phones and services, mobile app platforms etc.

Supplementary data to this article can be found online at https:// doi.org/10.1016/j.dss.2018.10.015

## References

[1] D. Bolton, The growth of the apps economy is beginning to slow. The growth of the apps economy is beginning to slow, Retrieved from: https://arc.applause.com/ 2016/05/10/idc-apps-economy-growth-slows/.

[2] The Economist, The Fintech Revolution: A Wave of Startus Is Changing Finance – For the Better, (May 9. 2015)

[3] S.A. Delre, W. Jager, M.A. Janssen, Difusion dynamics in small-world network with heterogeneous consumers, Computational & Mathematical Organization Theory 13 (2007) 185–202

[4] W. Venkatesh, H. Bala, V. Sambamurthy, Implementation of an information and communication technology in a developing country: a multimethod longitudinal study in a Bank in India, Information Systems Research 27 (3) (2016) 558–579.

[5] C. Scharwatt, A. Katakam, J. Frydrych, A. Murphy, N. Naghavi, GSMA 2014 State of the Industry: Mobile Financial Services for the Unbanked, Available at https:// www.gsma.com/mobilefordevelopment/wp-content/uploads/2015/03/SOTIR 2014.pdf

[6] The Bill & Melinda Gates Foundation, Fighting Poverty, Profitably: Transforming the Economics of Payments to Build Sustainable, Inclusive Financial Systems, Special Report available at: https://docs.gatesfoundation.org/Documents/Fighting Poverty Profitably Full Report.pdf.

[7] Press Release, Daraz Oficially Announces its Black Friday Discounts, https:// propakistani.pk/2015/11/26/daraz-oficially-announces-its-black-friday-discounts of-up-to-70/, (2015).

[8] A. Shaikh, H. Karjaluoto, Mobile banking adoption: a literature review, Telematics and Informatics 32 (1) (2015) 129–142.

[9] N. Mallat, Exploring consumer adoption of mobile payments-a qualitative study, Journal of Strategic Information Systems 16 (2007) 413–432.

[10] T. Zhou, Y. Lu, B. Wang, Integrating TTF and UTAUT to explain mobile banking user adoption, Computers in Human Behavior 26 (4) (2010) 760–767.

[11] S. Yang, Y. Lu, S. Gupta, Y. Cao, R. Zhang, Mobile payment services adoption across time: an empirical study of the effect of behavioral beliefs, social influences, and personal traits, Computers in Human Behavior 28 (2012) 129–142.

[12] G.G. Parker, M.W. Van Alstyne, Two-sided network effects: a theory of information product design, Management Science 51 (10) (2005) 1494–1504.

[13] J. Rochet, J. Tirole, Two-sided markets: a Progress report, The Rand Journal of Economics 37 (3) (2006) 645–667

[14] F. Zhu, N. Iansiti, Entry into platform-based markets, Strategic Management Journa 33 (2012) 88–106.

[15] A. Hagiu, Strategic decisions for multisided platforms, MIT Sloan Management Review 55 (2) (2014) 71–82

[16] T. Chesney, S. Gold, A. Trautrims, Agent based modelling as a decision support system for shadow accounting. Decision Support Systems 95 (2017) 110–116

[17] B. Ponte, J. Costas, J. Puche, D. Fuente, R. Pino, Holism versus reductionism in supply chain management: an economic analysis, Decision Support Systems 86 (2016) 83–94.

[18] T.W. Wang, S.K. Tadisina, Simulating internet-based collaboration: a cost-benefit case study using a multi-agent model, Decision Support Systems 43 (2007).

[19] E. Kiesling, M. Günther, C. Stummer, L.M. Wakolbinger, Agent-based simulation of innovation diffusion: a review. Central European Journal of Operations Research 20 (2) (2012) 183–230.

[2o] A. Zaffar, R. Kumar, K. Zhao, Diffusion dynamics of open source software: an agent based computational economics perspective, Decision Support Systems 51 (3) (2011).597–608

[21] L. Tesfatsion, K.L. Judd, Handbook of Computational Economics: Agent-based Computational Economics, vol. 2. North-Holland, UK. 2006

[22] R. Thakur, M. Srivastava, Adoption readiness, personal innovativeness, perceived risk and usage intention across customer groups for mobile payment services in India. Internet Research 24 (3) (2014) 369–392

[23] R. Chatterjee, J. Eliashberg, The innovation difusion process in a heterogeneous population: a micromodeling approach, Management Science 36 (1990) 1057–1079.

[24] W.D. Shaw, Searching for the opportunity cost of an individual's time, Land Economics 68 (1) (1992) 107–115.

[25] J. Engle-Warnick, J. Escobal, S. Laszlo, Risk Preference, Ambiguity Aversion and Technology Choice: Experimental and Survey Evidence from Peru, V Presented at NEUCD (2006).

[26] U.S. Congress Ofice of Technology Assessment, Fueling Development: Energy Technologies for Developing Countries, OTA-E-516, U.S. Government Printing Ofice, Washington, DC, April 1992.

[27] S. Mohr, G. Wallentin, An agent-based model for the socio-economic monitoring of vis-itor streams a study using the example of the Harz National Park, Germany, GI Forum 1 (2018) 297–315.

[28] U. Wilensky, NetLogo, http://ccl.northwestern.edu/netlogo/ Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL, 1999.

[29] W. Wang, L. Qiu, D. Kim, I. Benbasat, Efects of rational and social appeals of online recommendation agents on cognition- and afect-based trust, Decision Support Systems 86 (2016) 48–60

[30] K. Corral, D. Schuf, R.D. Louis, The impact of alternative diagrams on the accurac of recall: a comparison of star-schema diagrams and entity-relationship diagrams. Decision Support Systems 42 (1) (October 2006) 450–468.

[31] H.v.d. Heijden, Mobile decision support for in-store purchase decisions, Decision Support Systems 42 (2) (2006) 656–663.

[32] J. Khalilzadeh, A.D.A. Tasci, Large sample size, significance level, and the efect size: solutions to perils of using big data for academic research, Tourism Management 62 (2017) 89–96.

[33] J.H. Heinrichs, J.S. Lim, Integrating web-based data mining tools with business models for knowledge management, Decision Support Systems 35 (1) (2003) 103-112.

[34] D. Lazer, A. Friedman, The Network Structure of Exploration & Exploitation, Management Information Systems Quarterly 52 (2007).

[35] T. Zhou, An empirical examination of continuance intention of mobile payment services, Decision Support Systems 54 (2013) 1085–1091

[36] G.T. Ozer, E.G. Andersen Jr., Innovation and Breaching Strategies in Multi-Sided Platform Markets: Insights from a Simulation Study, Thirty Sixth International Conference on Information Systems. Fort Worth. USA. 2015

[37] D.S. Evans, A. Prichio, An empirical examination of why Mobile money schemes ignite in some developing countries but flounder in Most, Review of Network Economics 13 (4) (2014) 397–451.

[38] M.J. Liberatore, A. Hatchuel, B. Weil, A.C. Stylianou, An organizational change perspective on the value of modelling, European Journal of Operational Research 125 (1) (2000) 184–194.

Muhammad Adeel Zafar is an Assistant Professor in the Suleman Dawood School of Business at the Lahore University of Management Sciences. He received his PhD from the University of North Carolina at Charlotte. His research interests include technology and innovation difusion; social networks; agent-based computational economics and healthcare operations. His research has appeared in Decision Support Systems, IEEE Transactions on Engineering Management, Simulation Modeling Practice and Theory and Operations Research for Health Care.

Ram L. Kumar is a Professor in Belk College of Business Administration at the University of North Carolina at Charlotte. He received his Ph.D. degree from the University of Maryland at College Park, where he was the recipient of the Frank T. Paine Award for Academic Merit. He has worked for major multinational corporations such as Fujitsu before entering academics. His research has been funded by organizations such as the U.S. Department of Commerce, and organizations in the financial services and energy industries. His current research interests include economics of information systems, IT portfolio and value management, service science and knowledge management. His research has been published in Communications of the ACM, Computers & Operations Research, Decision Sciences, Information and Management, Information & Management, International Journal of Production Research Journal of MIS, and other journals and book chapters.

Kexin Zhao is an Associate Professor in the Business Information Systems and Operations Management department at the University of North Carolina at Charlotte. She received her Ph.D. degree from the University of Illinois at Urbana-Champaign. Her research interests are economics of information systems, development and adoption of e-busines standards, and game theory in information management. Her papers have been published in journals such as Journal of Management Information Systems, Decision Support Systems, and Electronic Markets.
