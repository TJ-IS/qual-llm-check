---
otero_id: 10658
otero_key: "XD6AQBRH"
title: "Information transparency in prediction markets"
authors: "ShengYun Yang; Ting Li; Eric van Heck"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.05.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information transparency in prediction markets

ShengYun Yang ⁎, Ting Li, Eric van Heck

Rotterdam School of Management, Erasmus University, The Netherlands

a r t i c l e i n f o

Available online xxxx

Keywords: Field experiment Forecasting Information aggregation Information transparency Market efficiency Prediction market

## a b s t r a c t

Prediction markets are designed and conducted for the primary purpose of aggregating information so that market prices forecast future events. In such markets, a group of traders buy and sell contracts and the payoff depends on unknown future events. Information is the key in a prediction market and the success of prediction markets depends on their design. In this paper, we theoretically develop and empirically test the effects of IT-enabled information transparency on prediction market performance (information aggregation efficiency and predictive accuracy) through traders' behavior (traders' participation activity and traders' dynamic interactions). We developed twelve prediction markets and empirically tested our hypotheses using a field experiment. The results suggest that improved information transparency (disclosure of different traders' buy and sell orders) can lead to higher levels of traders' dynamic interactions. Increases in traders' participation activity and dynamic interactions lead to higher information aggregation efficiency and greater market predictive accuracy. Interestingly, however, full disclosure of information and complete transparency do not necessarily further improve traders' activities. This paper is one of the first to take an information-based view to study prediction markets and highlights the importance of information transparency in the design of prediction markets. We further discuss the managerial implications, limitations and future research.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Forecasting is a fundamental activity of management within a company because it is often required when a decision is made [2,3]. Conventional forecasting methods, however, become less accurate in contemporary environments.<sup>1</sup>1When a new product is launched statistical forecasting of demand has no sales data on which to base the demand estimate. Thus, statistical forecasting based on historical data does not perform as well for new products as it does for existing products [3,7]. Likewise, target customers in a survey may not be able to give unbiased purchase intentions without learning from early adopters [36], and opinion variance between experts is limited if they are few in number or if social pressure influences their appraisal [30,68]. Consequently, forecasts based on these methods are less accurate. Over the past decade, some in the business world have come to believe that the best forecasts emerge from neither past behavior patterns nor market analyses created by

<sup>1</sup> When a new product is launched statistical forecasting of demand has no sales data on which to base the demand estimate. Thus, statistical forecasting based on historical data does not perform as well for new products as it does for existing products [3,7]. Likewise, target customers in a survey may not be able to give unbiased purchase intentions without learning from early adopters [36], and opinion variance between experts is limited if they are few in number or if social pressure influences their appraisa [30 68], Consequently, forecasts based on these methods are less accurate

far-removed experts who may lack familiarity with front-line work [52]. Rather, the best forecasts come from crowds, particularly frontline employees who work directly with new products and services and interact daily with buyers, sellers and customers in the field, and thus have the most relevant and updated information and knowledge required for forecasting [30,52]. The aggregation of information dispersed in groups is referred to as the wisdom of crowds, collective wisdom or collective intelligence [80]. Companies are recommended to use it to make forecasts and decisions [9,16,51,53,54].

A prediction market is an elegant and well-designed method for capturing collective wisdom and predicting the outcome of a future event [80]. It can be a powerful information-processing mechanism that aggregates the views of multiple market traders to generate a prediction of the future. Since the inception of the first prediction market, the Iowa Electronic Market (IEM), the promising forecasting results of prediction markets have captured much enthusiasm from both academia (such as [30,38,51,62,78]) and the business world (such as HP, Eli Lilly, and Intel).

Our research adopts the information-based view to study prediction markets, as information is the key in a prediction market. Traders in a prediction market use and process different information in their personal estimation of a future event, reflected in their trading activities. Traders learn from the trading activities of others and the market aggregates traders' dispersed information through their trading activities. Therefore, the fundamental element in a prediction market is information and the fundamental activity between traders is information exchange.

Information transparency, defined as the level of availability and accessibility of market information to its participants [27,88], is a fundamental issue in the design of markets [8]. The success of a prediction market, like any market, depends on its design and implementation [85]. Bloomfield and O'Hara [8] stated that transparency – the realtime, public dissemination of market information – plays a fundamental role in market design, particularly, in the fairness and efficiency of the market. Extant research on prediction market design has focused on market mechanisms [32,61,85], contracts [44,58], traders [1,41,79] and incentives [31,70,73]. Little research has studied the role of market information in prediction market design. Advanced technologies have enabled the distribution of various types and amounts of market information, which allow different levels of information transparency in a market. This paper, therefore, focuses on information transparency.

Research on information transparency has evolved from the early information transparency hypothesis, that open sharing information in electronic markets is beneficial to all traders [45,75], to the recent information transparency strategy [24,81]. The literature on transparency strategy is scarce and scattered across disciplines [27]. Prior research on transparency strategy has addressed information transparency and electronic market design. These studies identified transparency design features related to information disclosure policies throughout the trading process and demonstrated a double-edged effect of information transparency: the effect of information transparency is not always beneficial or equal to different stakeholders in a market [26,77,87]. Previous literature focused on the effects of information transparency on different market positions (buyers, suppliers, and intermediaries) in business-to-consumer (B2C) [26,76,84] and business-to-business (B2B) markets [37,40,42,60,87,88]. This paper focuses on participants in a double auction (i.e., a prediction market), in which a participant is a buyer as well as a seller. Further, it examines the influences of different transparency strategies that go beyond opaque and transparent conditions [25,76,77]. This paper answers the following research question: How does information transparency influence online prediction market performance?

Understanding individuals' activities is crucial to enhance the design of online markets [5]. Traders' behavior has captured much attention in research on prediction markets, as it entails information dissemination and has major effects on market performance [7,33, 35,67]. Chen et al. [13] identified traders' participation activity and traders' dynamic interactions as two fundamental activities that enable information exchange among traders in a prediction market. The goal of this paper is to examine how information transparency affects prediction market performance by taking into account traders' behavior, namely traders' participation activity and traders' dynamic interactions.

In this paper we propose that while higher information transparency in prediction markets leads to more dynamic interactions between traders, full information transparency does not yield further improvement in traders' participation and interactions. Further, an increased level of traders' participation activity and dynamic interactions improves the market's ability to aggregate information, which subsequently leads to higher market predictive accuracy. To empirically test our hypotheses, we conducted a field experiment in an e-commerce company. We designed and developed an internal online prediction market with four different levels of information transparency: opaque, partially-transparent, semi-transparent, and fully-transparent. The traders were the employees of this company and the predicted future events were the outcomes of the company's key performance indicators (KPIs). The field experiment allowed us to investigate the impact of information transparency on traders' behavior and subsequently on prediction market performance in a real business environment.

The results show that in a prediction market the disclosure of different traders' buy and sell orders enhances dynamic interactions between traders, though disclosure does not have an impact on traders' participation activity. The disclosure of all traders' buy and sell orders, however, impedes dynamic interactions in a market rather than further improving them. Furthermore, increases in traders' participation activity and traders' dynamic interactions in a prediction market enhance the market's ability to aggregate dispersed information (i.e., information aggregation efficiency), and eventually lead to more accurate predictions (i.e., market predictive accuracy).

This paper contributes to the literature on information transparency and prediction markets. With regard to information transparency, this paper differs from prior research in two ways. First, this is the first paper to theoretically develop and empirically test the impact of information transparency in the context of prediction markets where participants are buyers as well as sellers. It extends previous studies on the effect of information transparency on different market positions that focused only on buyers, sellers or intermediaries, respectively, in B2B [37,40,42,60,87,88] or B2C markets [26,84]. Second, this paper examines the effect of different transparency levels that go beyond opaque or transparent information conditions [25,76,77], contributing to the literature on transparency strategy [27]. Unlike prior research on prediction market design that focused on market mechanisms [32,61], contracts [58], traders [1,41,79] and incentives [15,31,70,73], this paper is one of the first to take an information-based view and highlights the importance of information transparency in the design of prediction markets. Second, this paper distinguishes between information aggregation efficiency and market predictive accuracy for the analysis of prediction market performance by defining and developing a measurement of information aggregation efficiency.

This paper is organized as follows: Section 2 provides the theoretical background of the paper and develops the hypotheses related to the effects of information transparency on traders' behavior and prediction market performance. In Section 3, we present our research methods, including the experiment design and the measures of variables. In Section 4, we discuss the results drawn from the field experiment and validate the hypotheses. Section 5 discusses the results and Section 6 concludes with research findings and contributions to research and business practice

## 2. Theory and hypothesis development

In this section we review the literature on prediction markets and information transparency, present the conceptual model and develop our hypotheses. Fig. 1 summarizes our conceptual model.

## 2.1. Prediction market

Prediction markets are designed and run for the primary purpose of mining and aggregating information scattered among traders [34,83]. In such markets, a group of traders buy and sell contracts and the payoff depends on unknown future events. The use of prediction markets is based on the rational expectations hypothesis [11,33], which states that in aggregate, the expected price is an unbiased predictor of the actual price [55]. According to this theory, all information available to traders in a market is revealed by prices in the process of trading [28,47, 48].<sup>2</sup> Thus, we can use markets to aggregate dispersed information from market traders [34].

![](/api/attachments/XD6AQBRH/fulltext/images/079e6afe87ea9eb5d7ddea813b4d3c71b6830d7202c5f5776046029250061a8b.jpg)  
Fig. 1. Conceptual model.

There are three major advantages of prediction markets over traditional statistical methods (e.g., structural models) or judgmental forecasting methods (e.g., expert opinions) [85]. First, prediction markets provide incentives for truthful revelation, because the trading process is usually anonymous and the rewards as well as punishments are straightforward [30,68]. Second, prediction markets provide incentives for research and information discovery. Traders' self-interest in a prediction market is profitable trading, and thus, they must improve their personal prediction accuracy. A common approach is, thus, to take into consideration more recent information [10,51,69]. Third, the market provides an algorithm for aggregating opinions. By their structure, prediction markets automatically allow traders to use their information and bet as much money as they desire in the hope of profiting from their specialized knowledge [68]. This is how information is given more weight in the aggregation process in a prediction market. The incentives derived from prediction markets in fact provide a natural way to weigh opinions [36].

The existing discussion on prediction markets concentrates on three areas. The largest group of studies demonstrated the market's ability to accurately predict future events [22,35,86] or aggregate information [11,23,63], addressing the aggregation level of a prediction market. Another stream of studies investigated traders and their behavior in prediction markets, addressing the individual level of a prediction market. These studies focused on informed versus uninformed traders [7,82], traders' manipulations [21,33], traders' individual social networks [67], and the effect of traders' characteristics on information aggregation and the predictive accuracy of prediction markets [10,12, 20,56,67]. The third stream of literature focused on market design and identifying and discussing design aspects of a prediction market, including market mechanisms [32,61], contracts [58], traders [1,41,79], and incentives [15,31,70,73].

## 2.2. Information transparency and traders' behavior

Traders' behavior refers to individuals' activities that enable information exchange among traders in a prediction market. In this paper we focus on traders' participation activity and traders' dynamic interactions. The rational expectations hypothesis suggests that traders are sensitive to the prices of contracts, as prices are the signals they learn from to constantly update their beliefs [29,69]. Quote information is a type of pre-trade information, which allows traders to infer other traders' expectations on contracts from their pricing behavior [59]. In a prediction market, buy and sell orders are a trader's quote information. When only the highest outstanding buy order or the lowest outstanding sell order is displayed, traders can only observe the buy or sell price of a contract submitted by the most aggressive traders in the market. More informed traders benefit from that information as they can earn higher profit by trading with aggressive traders [50]. Less informed traders, nevertheless, benefit when some quote information is displayed. An increased amount of traders' quote information helps traders extract more information from other traders to form their own expectations on the contracts. Thus, we expect that the disclosure of different traders' buy and sell orders motivates traders to actively participate in a market.

Traders' dynamic interactions refer to a trader's revision of buy or sell orders on contracts [13]. Greater visibility of individual trader's orders can enhance the precision of traders' inferences about whether orders are driven by information or liquidity [59]. When traders can discern the imbalances of buy or sell orders in the market, they can learn from prices more quickly and therefore set their own prices more efficiently [8]. This suggests that greater visibility of quote information enables traders to adjust their expectations on contracts and enhances the influence of one trader's activity on other traders.

When all quote information is revealed in a prediction market, traders do not necessarily trade more actively or update their opinions more frequently. This is because information becomes overloaded against the objective limits of individuals' information processing capability [57]. Early research found that the increased information load may make it difficult to accurately identify relevant cues and may result in decreased performance, particularly when decision makers are confronted with time constraints [39,57,72]. In a prediction market, complete quote information actually makes it more difficult for traders to discern information quality or the certainty of potential outcomes. It also requires traders to spend more time analyzing market information. Moreover, when all buy and sell orders are revealed in a market, informed traders no longer actively update their opinion of the future events. This is because other traders will observe the adjusted orders in the market and may learn from the informed trader's actions. As the opinions of all traders become more similar, informed traders lose their ability to make profitable trades. Limited individual adjustments lead to even more constrained influence of one trader on another trader's learning. Consequently, full-transparency of quote information hampers traders' participation activity and dynamic interactions. Thus, we propose:

Hypothesis 1a. Information transparency and traders' participation activity hypothesis

In a prediction market, increased disclosure of different traders' quote information leads to an increase in traders' participation activity. However, the complete disclosure of traders' quote information does not further improve traders' participation activity.

Hypothesis 1b. Information transparency and traders' dynamic interaction hypothesis

In a prediction market, increased disclosure of different traders' quote information leads to an increase in traders' dynamic interactions. However, the complete disclosure of traders' quote information does not further enhance traders' dynamic interactions.

## 2.3. Traders' behavior and information aggregation efficiency

Information aggregation is the process of information dissemination from insiders to outsiders [29,65,66]. As information is aggregated in a prediction market, traders' beliefs regarding the potential outcomes of a future event begin to converge. When traders' beliefs converge, the market price will be very close to the mean of market participants' beliefs [23,86]. Information aggregation efficiency of a prediction market refers to the ability of the market to synthesize traders' mean beliefs. The deviation of transaction prices from this mean belief indicates the information aggregation efficiency — the smaller the deviation, the more efficiently the market aggregates the traders' consensus.

In a prediction market the payoff is tied to the trader's personal predictive accuracy of the future event and profit or loss is straightforward. Traders are, therefore, motivated not only to truthfully incorporate their private information and any other relevant information into their trading decisions, but also to seek information about the future event [6,56]. Consequently, prediction markets have the ability to aggregate information from individuals who filter both public and private information and weigh this information through the price formation process [6]. Traders learn and keep updating their beliefs based on different newly acquired information. This learning process is reflected in their ever-changing buy and sell orders [29,69]. Traders iteratively learn and adjust their individual expectations and as a result, their expectations will eventually converge and trade will cease in the market [17]. Until then, the convergent expectation should capture all of the information for the estimation of the future event. In other words, the traders' mean belief should be captured and reflected in the transaction price of a contract in a prediction market. Consequently, traders' participation activity and dynamic interactions affect the process of information aggregation in a positive way. We propose:

Hypothesis 2a. Traders' participation activity and information aggregation efficiency hypothesis

In a prediction market, an increased level of traders' participation activity leads to higher information aggregation efficiency.

Hypothesis 2b. Traders' dynamic interaction and information aggregation efficiency hypothesis

In a prediction market, an increased level of traders' dynamic interactions leads to higher information aggregation efficiency.

## 2.4. Information aggregation efficiency and market predictive accuracy

The rational expectations hypothesis [55] suggests that higher information aggregation efficiency leads to more accurate market prediction. Previous studies on prediction markets also demonstrated that the market can accurately predict future events by efficiently aggregating dispersed information [22,63]. These studies suggested that a prediction market can accurately forecast future events due to its ability to aggregate information, however, the positive effect of information aggregation efficiency on market predictive accuracy has not been empirically tested. Thus, in this paper, we propose:

Hypothesis 3. Information aggregation efficiency and market predictive accuracy hypothesis

Higher information aggregation efficiency of a prediction market leads to higher market predictive accuracy.

## 3. Research methods

We conducted a field experiment in collaboration with Wasu Taobao Co., Ltd.<sup>3</sup> (hereafter referred to as Wasu Taobao), an e-commerce company in China. The company wanted a prediction of its business KPIs<sup>4</sup> that reflected employees' knowledge and information derived from their daily work. To achieve this, we conducted a field experiment using 12 internal prediction markets with the company to forecast the outcomes of 12 different periodical KPIs in 2011, such as the number of transactions or the number of page views. The KPIs were general business interests of the company, and therefore, employees were familiar with these events. All KPIs in this experiment were mutually exclusive.

## 3.1. Market design and subjects

## 3.1.1. Market mechanism and contracts

To carry out the field experiment, we designed and developed a web-based prediction market. We designed the contracts together with Wasu Taobao. Due to high uncertainty about the business, the company was interested in an interval prediction rather than a point prediction, and in turn, every market had five contracts, representing five possible ranges of outcomes of a KPI. Since the company had different preferences of precision, the intervals of each contract were unequal. Table 1 lists the contracts of each market.<sup>5</sup>

## 3.1.2. Subjects and incentives

We invited representative employees and managers from all departments across the company to participate in the field experiment. The composition of the invited employees represented the actual distribution of employees over different departments in the company.

In the field experiment subjects were assigned to conditions by means of self-selection [74]. They were allowed to take part in any market during the experiment. This self-selection design is in line with traders' participation in real internal prediction markets, in which they participate based on their willingness and interest. Moreover, a between-groups design is more useful when it is impossible for an individual to participate in all experimental conditions [19].

When a market started every subject received an endowment, including 2000 Taoban, a currency developed for the markets in the experiment, and 20 shares per contract. We provided the subject who owned most shares of the contract with a prediction reward in the form of non-monetary incentives, such as a mug or a T-shirt. In each market, the subject who had the most Taoban in her account at the end of a market received a trading reward. The prediction reward was developed to motivate subjects to learn in the market and the trading reward was designed to motivate subjects to trade actively. The winners of each reward were announced to the company. Subjects who did not place any buy or sell order in the market were not eligible for the rewards.

## 3.2. Experiment procedure

Prior to the experiment, we conducted a pilot study of six internal prediction markets with the participation of a number of employees. Based on the feedbacks received, we made necessary adjustments to the market mechanism design and contract design. In the field experiment, we first gave a 30-minute introduction to all subjects, during which the General Manager introduced the potential contribution of internal prediction markets to the company's decision-making processes and the experiment administrator demonstrated the use of the prediction market. After the introduction, the subjects were allowed to register and participate in four trial markets. Since no employee had prior experience participating in a prediction market, the trial markets aimed to familiarize employees with the working of the prediction market and help them understand their task as traders.

We conducted the experiment using 12 prediction markets over three consecutive working days. Every day, four markets were listed and ran in parallel for 1 h.<sup>6</sup> We had four information transparency experimental conditions and each market corresponded with one

S. Yang et al. / Decision Support Systems xxx (2015) xxx–xxx

Table 1  
Markets, predicted events and contracts in the field experiment.

<table><tr><td>Markets</td><td>KPIs*</td><td>Operational day</td><td># of active traders</td><td>Market conditions</td><td>Contract 1</td><td>Contract 2</td><td>Contract 3</td><td>Contract 4</td><td>Contract 5</td></tr><tr><td>1</td><td>A</td><td>Day 1</td><td>14</td><td>Partially-transparent</td><td>0-49</td><td>50-99</td><td>100-299</td><td>300-499</td><td>500-1000</td></tr><tr><td>2</td><td>B</td><td>Day 1</td><td>23</td><td>Semi-transparent</td><td>0-199</td><td>200-399</td><td>400-599</td><td>600-799</td><td>800-1500</td></tr><tr><td>3</td><td>C</td><td>Day 1</td><td>15</td><td>Fully-transparent</td><td>0-5</td><td>6-9</td><td>0-14</td><td>15-19</td><td>20-100</td></tr><tr><td>4</td><td>D</td><td>Day 1</td><td>12</td><td>Opaque</td><td>0-299</td><td>300-599</td><td>600-999</td><td>1000-1299</td><td>1300-3000</td></tr><tr><td>5</td><td>E</td><td>Day 2</td><td>11</td><td>Fully-transparent</td><td>40K-60K**</td><td>61K-90K</td><td>91K-120K</td><td>121K-150K</td><td>151K-300K</td></tr><tr><td>6</td><td>F</td><td>Day 2</td><td>10</td><td>Opaque</td><td>0-10K</td><td>11K-30K</td><td>31K-60K</td><td>61K-90K</td><td>91K-200K</td></tr><tr><td>7</td><td>G</td><td>Day 2</td><td>8</td><td>Partially-transparent</td><td>0.00-3.00%</td><td>3.00%-5.99%</td><td>6.00%-8.99%</td><td>9.00%-11.99%</td><td>12.00%-20.00%</td></tr><tr><td>8</td><td>H</td><td>Day 2</td><td>7</td><td>Semi-transparent</td><td>¥0.00-¥1.99</td><td>¥2.00-¥4.99</td><td>¥5.00-¥7.99</td><td>¥8.00-¥10.99</td><td>¥11.00-¥20.00</td></tr><tr><td>9</td><td>I</td><td>Day 3</td><td>6</td><td>Semi-transparent</td><td>0-19</td><td>20-49</td><td>50-79</td><td>80-109</td><td>110-200</td></tr><tr><td>10</td><td>J</td><td>Day 3</td><td>8</td><td>Fully-transparent</td><td>0-49</td><td>50-99</td><td>100-149</td><td>150-199</td><td>200-500</td></tr><tr><td>11</td><td>K</td><td>Day 3</td><td>8</td><td>Opaque</td><td>¥0-¥4999</td><td>¥5000-¥9999</td><td>¥10,000-¥14,999</td><td>¥15,000-¥19,999</td><td>¥20,000-¥50,000</td></tr><tr><td>12</td><td>L</td><td>Day 3</td><td>6</td><td>Partially-transparent</td><td>¥0-¥99</td><td>¥10-¥399</td><td>¥400-¥699</td><td>¥700-¥999</td><td>¥1000-¥2000</td></tr></table>

⁎ We refer to the 12 different prediction markets as Market 1 to Market 12 and the predicted KPIs as A to L (e.g., the number of transactions or the number of page views) to disguise the company information in compliance with the confidentiality agreement.  
\*\* K indicates thousands.

condition. The names of the markets were listed on the experiment homepage. Subjects clicked the name of a market to enter that specific market. To account for the potential preference of subjects for a particular position in a list, we adopted a Latin Square design (Field and Hole 2003) to order the experimental market sequences on the home page.

All registered subjects were allowed to participate in all markets. During the one-hour trading time, the experiment administrator was available to answer questions and solve problems. At the end of every trading day, we sent a brief report regarding traders' participation activity (number of transactions per contract) and trading information (the highest and the lowest transaction price of each contract) to the sub jects, motivating them to further participate.

## 3.3. Operationalization and measures of variables

## 3.3.1. Information transparency

This study focuses on quote information in prediction markets, as this pre-trade information is likely to influence traders' behavior. We manipulated four experimental conditions of quote information in which traders see information on outstanding buy and sell orders in varying degrees of transparency. (1) In the opaque market, traders do not see any other traders' buy or sell orders — neither the price, nor the number of shares. (2) In the partially-transparent market, traders see the highest outstanding buy order and the lowest outstanding sell order, including the price and the total number of shares. (3) In the semi-transparent market, traders see the highest three outstanding buy orders and the lowest three outstanding sell orders. (4) In the fullytransparent market, traders see all outstanding orders.

## 3.3.2. Traders' behavior

The measurement of traders' behavior was adapted from Chen et al. [13], including traders' participation activity and traders' dynamic interactions for both individual trader level and contract level. The analysis at the individual trader level focuses on an individual trader's behavior despite how other traders respond. The contract level analysis focuses on traders' collective behavior in a market.

To measure traders' participation activity, we first identified the number of active traders because traders contribute their information to the market when and only when they buy or sell in the market. Active traders are traders who place at least one buy or sell order in a prediction market [7,15]. The traders' participation activity is measured at the contract level, including the total number of transactions and the total number of shares traded, and at the individual trader level, including the average number of buy orders/sell orders, the average number of shares in buy orders/sell orders, the average number of transactions, and the average number of shares traded [20,56].

The measurement of traders' dynamic interactions consists of two dimensions, a trader's self-revision and a trader's influence on others. A trader's self-revision is measured at the individual trader level and a trader's influence on others is measured at the contract level. We measure trader's self-revision as follows. We first identified the range containing a trader's estimation of a contract. The lower bound and the upper bound of her estimation range can be captured when she places her first buy order and sell order of that contract. As traders can observe individual buy orders, sell orders, and aggregate behavior of other traders in a prediction market, traders may revise their estimation accordingly. If in the next round, the trader's buy order or sell order on that contract is different from the previous one, we refer to this as revision behavior for that trader and refer to this new buy or sell order as a self-revision. There are two types of self-revision. Type I selfrevision occurs when a trader's following order price is different from the previous one on the same contract. Type II self-revision requires the price difference to be at least 5% based on the previous order price.

With regard to the trader's influence on others, we considered four alterative measures of influential orders based on Chen et al. [14]. (1) 1-influential order: if the next buy or sell order of the same contract is from a different trader and is also a self-revision order for that trader in the same direction. (2) 2-influential order: if the next two consecutive buy or sell orders of the same contract are from two different traders and are also self-revision orders in the same direction. (3) 3-influential order: if the next three consecutive buy or sell orders of the same contract are from three different traders and are also self-revision orders in the same direction. (4) 2Out3-influential order: if the next three consecutive buy or sell orders of the same contract are from three different traders and two of the three are also self-revision orders in the same direction.

## 3.3.3. Information aggregation efficiency

Prior studies commonly measured information aggregation efficiency in two ways. Though popularly adopted, these two measurements do not fulfill the needs of our field experiment. Before explaining our own measurement, we will explain how these two measurements are defined and what their limitations are.

One measurement is to compare the transaction prices with the competitive equilibrium price of a contract. The competitive equilibrium price corresponds with the reward, given that all private information is aggregated and reflected in the market. Therefore, the smaller the difference is between the transaction price and the competitive equilibrium price of a contract, the higher the information aggregation efficiency is (see [63]). However, this measurement is used in laboratory experiments, where the certainty of private information is ensured and the actual result is known. While the measurement can manifest the ability of a prediction market to aggregate information, it cannot be used in a real business environment, where the certainty and the availability of private information are not ensured and the result of the future event is unknown.

The other measurement compares traders' average estimation of a future event prior to market opening with the actual result. The closer the two results are, the more efficiently the information is aggregated (see [29]). A prediction market forecast reflects the market consensus and traders' average estimation represents consensus, therefore, the comparison between these two measurements indicates to what extent the market captures the traders' consensus. However, this method neglects the fact that information aggregation is a process in which traders learn during trading and bring new information into the market [10,36,69]. In turn, traders' average estimation of the future event prior to the market opening does not actually imply their consensus after learning. Alternatively, we can collect the traders' average estimation of the future event at the end of the market, after learning in the market. Nonetheless, in reality it is not ensured that all traders or even most traders will submit their personal estimate. Additionally, existing traders may leave and new traders may enter.

In this study we developed a new measurement based on the comparison between the transaction price and the dynamic equilibrium price of a contract. A trader's buy and sell orders of a contract correspond to the trader's individual estimation of a future event. When there is no difference between traders' perceived value of a contract, no shares are traded. A demand curve of a contract can be extracted based on all the buy orders of the contract. Similarly, a supply curve can be drawn based on all the sell orders of the contract. An equilibrium price is identified as the price at which the quantity demanded equals the quantity supplied. In the absence of external influences the equilibrium value will not change. The equilibrium price of a contract, based on the demand and supply curve of the contract, represents the market consensus on the estimation of the corresponding outcome. This equilibrium price of the contract evolves along with traders' learning and market development, which we refer to as the dynamic equilibrium price. To compare information aggregation efficiency between different prediction markets, we calculated the average percentage deviation of the transaction price from the dynamic equilibrium price of contracts in a market. The smaller the average percentage deviation is, the higher the information aggregation efficiency is.

## 3.3.4. Market predictive accuracy

Market predictive accuracy measures how accurately a market predicts future events. Market predictive accuracy is usually assessed against two benchmarks, the actual results (absolute accuracy) and the estimation generated from the competing forecasting mechanism (relative accuracy) [6]. Relative accuracy is commonly used, which fulfills the need of most companies for an improved forecasting mechanism compared to the existing mechanism. In this study, the company provided us with the difference between our market prediction and the actual result. Thus, we were able to measure absolute market predictive accuracy. The smaller the difference is between the prediction and the actual results, the more accurate the market prediction.

The measure of market predictive accuracy was adopted from prior research on internal prediction markets in HP [64], one of the first internal prediction markets. We follow the measurement of this prior research for four reasons. First, the future events being predicted in HP markets were sales of HP products, similar to the experimental markets in this study. Second, the contract design in HP markets was similar to our study. In both studies, each contract represented a possible range of sales. Third, the measurement of the point estimation of the market prediction adopted the uniform distribution and the mid-point of the numerical range presented by a contract. This point estimation allowed the researchers to calculate the absolute difference between the market prediction and the actual sales, precisely comparing the two numbers. Last, Plott and Chen [64] further illustrated the particular measurement of market predictive accuracy, namely, the percentage error, based on the aforementioned comparison.

## 4. Analysis and results

In this section we present analyses of traders' participation activity, traders' dynamic interactions, information aggregation efficiency and market predictive accuracy based on the data collected from the field experiment. The hypotheses are validated accordingly.

## 4.1. Overview of subjects' participation

In the field experiment, a total of 41 employees registered an account,<sup>7</sup> including 17 who were not part of the initial invitation but proactively joined based on their own interest in participating in the internal prediction markets. The average number of active traders per market was 11. The highest number and the lowest number of active traders in a market were 23 and 6. Four employees participated in all 12 markets. The small market size is in line with the characteristics of internal prediction markets and prior research, such as HP prediction markets [64].

## 4.2. Effects of information transparency on traders' behavior

Table 2 summarizes the results of the analysis of traders' behavior, including traders' participation activity and traders' dynamic interactions, as well as the result of the Kruskal Wallis test.

At the contract level, due to the different number of active traders in each market, we weighted numerical values by the ratio of traders for the measurement. A Kruskal Wallis test did not reveal any significant difference in the number of transactions and the number of shares traded in the markets with four different information transparency levels. At the trader level in each market, a Kruskal Wallis test showed no significant effect of information transparency on traders' participation activity based on the number of buy orders, number of shares in buy orders, number of sell orders, and number of shares in sell orders. The average values of measurements in different market conditions were in fact very close to each other. For instance, the average number of buy orders and sell orders in all four market conditions were very similar. With regard to the number of shares in buy orders and the number of shares in sell orders, the largest differences did not exceed 9 and 3, respectively. These results suggest that traders' participation activity does not vary because of different information transparency levels. Thus, information transparency and traders' participation activity hypothesis (Hypothesis 1a) is not supported.

According to the result of a Kruskal Wallis test, there was a significant effect of information transparency on traders' dynamic interactions based on 1-influential orders, 2-influential orders, and 2Out3-influential orders. However, we noticed that different degrees of influential orders barely occurred in the opaque, partially- and fully-transparent market conditions, indicated in Table 2 by zeros. In the opaque condition traders could not observe others' orders, and therefore, it was difficult to influence or be influenced by others. In other transparency conditions, the possible reason was related to the uncertainty of the price signals as well as the relationship between the information load and decision quality. Further discussion is presented in Section 5.1.

Table 2  
Effects of information transparency on traders' behavior.

<table><tr><td rowspan="2">Variables</td><td rowspan="2">Level of analysis</td><td rowspan="2">Measurements</td><td colspan="4">Market conditions</td><td rowspan="2">Kruskal Wallis test ( $x^{2}$ )</td></tr><tr><td>Opaque</td><td>Partially-transparent</td><td>Semi-transparent</td><td>Fully-transparent</td></tr><tr><td rowspan="6">Traders&#x27; participation activity</td><td rowspan="2">Contract</td><td># of transactions</td><td>9</td><td>14</td><td>17</td><td>13</td><td>5.6</td></tr><tr><td># of shares traded</td><td>134</td><td>217</td><td>211</td><td>176</td><td>4.4</td></tr><tr><td rowspan="4">Trader</td><td># of buy orders</td><td>2</td><td>2</td><td>3</td><td>2</td><td>4.7</td></tr><tr><td># of shares in buy orders</td><td>69</td><td>74</td><td>65</td><td>69</td><td>1.1</td></tr><tr><td># of sell orders</td><td>2</td><td>3</td><td>3</td><td>2</td><td>2.1</td></tr><tr><td># of shares in sell orders</td><td>45</td><td>47</td><td>44</td><td>44</td><td>1.7</td></tr><tr><td rowspan="6">Traders&#x27; dynamic interactions</td><td rowspan="4">Contract</td><td># of 1-influential orders</td><td>0</td><td>0</td><td>2</td><td>0</td><td>25.9*</td></tr><tr><td># of 2-influential orders</td><td>0</td><td>0</td><td>1</td><td>0</td><td>18.5*</td></tr><tr><td># of 3-influential orders</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td># of 2Out3-influential orders</td><td>0</td><td>0</td><td>1</td><td>0</td><td>15.3*</td></tr><tr><td rowspan="2">Trader</td><td># of Type I self-revisions</td><td>1</td><td>0</td><td>2</td><td>1</td><td>14.7*</td></tr><tr><td># of Type II self-revisions</td><td>1</td><td>0</td><td>2</td><td>1</td><td>14.7*</td></tr></table>

⁎ p b 0.01.

To further examine the effect of information transparency on traders' dynamic interactions we conducted a post-hoc analysis using a Mann–Whitney test with Bonferroni correction (see Table 3). The results show that 1-influential, 2-influential, and 2Out3-influential orders were significantly different between the semi-transparent condition and the other markets. No significant difference was revealed between opaque and partially-transparent markets, between opaque and fully-transparent markets, or between partially-transparent and fullytransparent markets. Comparing the mean ranks among the four different market conditions, 1-influential and 2-influential orders occurred most in semi-transparent markets, and the other three market conditions did not differ. 3-influential orders did not occur in any of the markets, thus information transparency levels did not have any effect. In sum, the aforementioned results showed that the influence of one trader's order on another's in general occurred most frequently when the market was semi-transparent.

Table 3  
Mann–Whitney tests of traders' dynamic interactions

<table><tr><td rowspan="2">Level of analysis</td><td rowspan="2">Measurements</td><td rowspan="2">Market conditions</td><td colspan="4">Market conditions</td></tr><tr><td>Opaque</td><td>Partially-transparent</td><td>Semi-transparent</td><td>Fully-transparent</td></tr><tr><td rowspan="12">Contract</td><td rowspan="4"># of 1-influential orders</td><td>Opaque</td><td></td><td>98(-0.90)</td><td>30**(-3.77)</td><td>106(-0.52)</td></tr><tr><td>Partially-transparent</td><td>98(-0.90)</td><td></td><td>37**(-3.37)</td><td>92(-1.31)</td></tr><tr><td>Semi-transparent</td><td>30**(-3.77)</td><td>37**(-3.37)</td><td></td><td>31**(-3.78)</td></tr><tr><td>Fully-transparent</td><td>106(-0.52)</td><td>92(-1.31)</td><td>31**(-3.78)</td><td></td></tr><tr><td rowspan="4"># of 2-influential orders</td><td>Opaque</td><td></td><td>105(-1.00)</td><td>71*(-2.25)</td><td>105(-1.00)</td></tr><tr><td>Partially-transparent</td><td>105(-1.00)</td><td></td><td>60**(-2.96)</td><td>113(0.00)</td></tr><tr><td>Semi-transparent</td><td>71*(-2.25)</td><td>60**(-2.96)</td><td></td><td>60**(-2.96)</td></tr><tr><td>Fully-transparent</td><td>105(-1.00)</td><td>113(0.00)</td><td>60**(-2.96)</td><td></td></tr><tr><td rowspan="4"># of 2Out3-influential orders</td><td>Opaque</td><td></td><td>105(-1.00)</td><td>77*(-1.99)</td><td>105(-1.00)</td></tr><tr><td>Partially-transparent</td><td>105(-1.00)</td><td></td><td>68**(-2.68)</td><td>113(0.00)</td></tr><tr><td>Semi-transparent</td><td>77*(-1.99)</td><td>68**(-2.68)</td><td></td><td>68**(-2.68)</td></tr><tr><td>Fully-transparent</td><td>105(-1.00)</td><td>113(0.00)</td><td>68**(-2.68)</td><td></td></tr><tr><td rowspan="8">Trader</td><td rowspan="4"># of Type I self-revisions</td><td>Opaque</td><td></td><td>383(-0.68)</td><td>380*(-2.21)</td><td>499(-0.18)</td></tr><tr><td>Partially-transparent</td><td>383(-0.68)</td><td></td><td>292**(-3.10)</td><td>414(-1.03)</td></tr><tr><td>Semi-transparent</td><td>380*(-2.21)</td><td>292**(-3.10)</td><td></td><td>424*(-2.36)</td></tr><tr><td>Fully-transparent</td><td>499(-0.18)</td><td>414(-1.03)</td><td>424*(-2.36)</td><td></td></tr><tr><td rowspan="4"># of Type II self-revisions</td><td>Opaque</td><td></td><td>383(-0.68)</td><td>380*(-2.21)</td><td>499(-0.18)</td></tr><tr><td>Partially-transparent</td><td>383(-0.68)</td><td></td><td>292**(-3.10)</td><td>414(-1.03)</td></tr><tr><td>Semi-transparent</td><td>380*(-2.21)</td><td>292** (-3.10)</td><td></td><td>424*(-2.36)</td></tr><tr><td>Fully-transparent</td><td>499(-0.18)</td><td>414(-1.03)</td><td>424*(-2.36)</td><td></td></tr></table>

Note: z-statistics are in parentheses  
⁎ p b 0.05.  
⁎⁎ p b 0.01.

Table 4  
Market information aggregation efficiency (IAE) and predictive accuracy.

<table><tr><td rowspan="2">Market</td><td rowspan="2">Market conditions</td><td colspan="4">Based on the last transaction price of a contract</td><td colspan="4">Based on the weighted average transaction price of a contract</td></tr><tr><td>IAE (%)</td><td>Level of IAE</td><td>Point estimation</td><td>Percentage error (%)</td><td>IAE (%)</td><td>Level of IAE</td><td>Point estimation</td><td>Percentage error (%)</td></tr><tr><td>1</td><td>Partially-transparent</td><td>28.64</td><td>High</td><td> $391^a$ </td><td>54.32</td><td>29.81</td><td>High</td><td> $445^a$ </td><td>48.01</td></tr><tr><td>2</td><td>Semi-transparent</td><td>19.26</td><td>High</td><td> $559^a$ </td><td>39.57</td><td>23.00</td><td>High</td><td> $609^a$ </td><td>34.16</td></tr><tr><td>3</td><td>Fully-transparent</td><td>21.03</td><td>High</td><td> $21^b$ </td><td>55.32</td><td>52.76</td><td>Low</td><td>19</td><td>59.57</td></tr><tr><td>4</td><td>Opaque</td><td>36.29</td><td>High</td><td> $1297^a$ </td><td>64.18</td><td>55.80</td><td>Low</td><td> $1166^a$ </td><td>67.80</td></tr><tr><td>5</td><td>Fully-transparent</td><td>63.24</td><td>Low</td><td> $144K^a$ </td><td>98.23</td><td>33.10</td><td>High</td><td> $155K^b$ </td><td>98.09</td></tr><tr><td>6</td><td>Opaque</td><td>42.37</td><td>Low</td><td> $109K^b$ </td><td>64.95</td><td>46.35</td><td>Low</td><td> $110K^b$ </td><td>64.63</td></tr><tr><td>7</td><td>Partially-transparent</td><td>30.02</td><td>High</td><td>8.81%</td><td>44.94</td><td>17.88</td><td>High</td><td> $9.30\%^a$ </td><td>41.88</td></tr><tr><td>8</td><td>Semi-transparent</td><td>19.54</td><td>High</td><td>¥8.96a</td><td>40.27</td><td>17.21</td><td>High</td><td>¥8.76a</td><td>41.60</td></tr><tr><td>9</td><td>Semi-transparent</td><td>23.93</td><td>High</td><td> $105^b$ </td><td>69.48</td><td>24.23</td><td>High</td><td> $101^b$ </td><td>70.64</td></tr><tr><td>10</td><td>Fully-transparent</td><td>21.07</td><td>High</td><td> $244^a$ </td><td>38.38</td><td>19.73</td><td>High</td><td> $244^a$ </td><td>38.38</td></tr><tr><td>11</td><td>Opaque</td><td>43.58</td><td>Low</td><td>¥21,249b</td><td>94.18</td><td>43.58</td><td>Low</td><td>¥19,468a</td><td>94.67</td></tr><tr><td>12</td><td>Partially-transparent</td><td>24.46</td><td>High</td><td>¥870b</td><td>44.83</td><td>45.10</td><td>Low</td><td>¥849b</td><td>46.14</td></tr><tr><td rowspan="4">Average</td><td>Opaque</td><td>40.75</td><td>Low</td><td></td><td>74.44</td><td>48.58</td><td>Low</td><td></td><td>75.70</td></tr><tr><td>Partially-transparent</td><td>27.71</td><td>High</td><td></td><td>48.03</td><td>30.93</td><td>High</td><td></td><td>62.04</td></tr><tr><td>Semi-transparent</td><td>22.91</td><td>High</td><td></td><td>49.77</td><td>21.48</td><td>High</td><td></td><td>60.64</td></tr><tr><td>Fully-transparent</td><td>35.11</td><td>High</td><td></td><td>63.98</td><td>35.20</td><td>High</td><td></td><td>58.19</td></tr></table>

<sup>a</sup> The forecasted contract was the adjacent to the accurate one.  
<sup>b</sup> The forecasted contract was the same as the actual result.

Analysis at the trader level revealed a significant effect of information transparency on both Type I self-revisions and Type II selfrevisions. The test results of these two types of self-revisions were identical, which implies that whenever a trader adjusted her expectation on a contract, the price difference between the previous and the updated order was at least 5%. Moreover, similar to the contract level analysis, self-revisions barley occurred in the partially-transparent market condition probably due to the uncertainty of price signals.

A post-hoc Mann–Whitney test with Bonferroni correction showed significant differences between opaque and semi-transparent markets, between partially-transparent and semi-transparent markets, and between semi-transparent and fully-transparent markets. The average number of self-revisions per trader in the semi-transparent market was at least two times as many as in other markets. However, the occurrence of self-revisions did not differ between opaque and partially-transparent markets, opaque and fully-transparent markets, or partially-transparent and fully-transparent markets. The average number of self-revisions per trader in these markets lay between zero and one, a very small difference. This indicates that traders adjusted their expectations on the contracts most frequently in the semitransparent market. The results drawn from the contract level and the trader level were convergent, supporting information transparency and traders' dynamic interaction hypothesis (Hypothesis 1b)

## 4.3. Effects of traders' behavior on information aggregation efficiency

We first calculated information aggregation efficiency of the prediction market, namely the percentage deviation of the transaction price from the equilibrium price. This percentage deviation measures the extent to which the transaction price reflects the market consensus, indicating how efficiently a market aggregates information from individual traders.

We used the last transaction price and the weighted average transaction price of a contract to measure information aggregation efficiency. Table 4 shows the percentage deviation of each type of transaction from the equilibrium price per market. Fig. 2a illustrates the information aggregation efficiency throughout the 12 markets. A Wilcoxon test was performed on the 12 markets, and revealed that the choice did not differ $( W ( 1 2 ) = 2 4 , z = - 0 . 8 , p > 0 . 4 2 )$ . Since the average value of the percentage deviation was slightly smaller based on the last transaction price as shown in Table 4, we adopted the last transaction price in the following analyses.

a)  
![](/api/attachments/XD6AQBRH/fulltext/images/110bfc0dd6b601f70602e27dc280a9af697c563e9da3823c4a4e752fcd89e8f5.jpg)

b)  
![](/api/attachments/XD6AQBRH/fulltext/images/19e7441d80389b1daff33ae59f592ad7eb8a50d4b265c35a31048b4d30620dbe.jpg)  
Fig. 2. a. Information aggregation efficiency. b. Market predictive accuracy. Note: Dash line — based on the last transaction price of a contract; solid line — based on the weighted average transaction price of a contract.

Please cite this article as: S. Yang, et al., Information transparency in prediction markets, Decision Support Systems (2015), http://dx.doi.org/ 10.1016/j.dss.2015.05.009

Table 5  
Effects of traders' behavior on information aggregation efficiency.

<table><tr><td>Variables</td><td>Level of analysis</td><td>Measurements</td><td>Spearman&#x27;s correlation coefficient (ρ)</td></tr><tr><td rowspan="6">Traders&#x27; participation activity</td><td rowspan="2">Contract</td><td># of transactions</td><td>-0.81**</td></tr><tr><td># of shares traded</td><td>-0.57</td></tr><tr><td rowspan="4">Trader</td><td># of buy orders</td><td>-0.23</td></tr><tr><td># of shares in buy orders</td><td>-0.20</td></tr><tr><td># of sell orders</td><td>0.06</td></tr><tr><td># of shares in sell orders</td><td>-0.32</td></tr><tr><td rowspan="6">Traders&#x27; dynamic interactions</td><td rowspan="4">Contract</td><td># of 1-influential orders</td><td>-0.66*</td></tr><tr><td># of 2-influential orders</td><td>-0.65*</td></tr><tr><td># of 3-influential orders</td><td></td></tr><tr><td># of 2Out3-influential orders</td><td>-0.65*</td></tr><tr><td rowspan="2">Trader</td><td># of Type I self-revisions</td><td>-0.83</td></tr><tr><td># of Type II self-revisions</td><td>-0.83</td></tr></table>

⁎ p b 0.05.  
\*\* $p < 0 . 0 1 .$

To test the effect of traders' behavior on information aggregation efficiency we examined the linear relationship based on Spearman's correlation coefficient (see Table 5). The results show that both traders' participation activity and traders' dynamic interactions had a positive effect on information aggregation efficiency. With regard to traders' participation activity, contract level results revealed significant correlation between the number of transactions and information aggregation efficiency. Negative correlation indicated that a higher level of traders' participation activity led to a smaller percentage deviation of the transaction price from the dynamic equilibrium price of a contract.

Nevertheless, the number of shares traded at the contract level and the indicators at the trader level, including the number of buy orders, number of shares in buyer orders, number of sell orders and number of shares in sell order, did not show a significant correlation with information aggregation efficiency. The results implied that traders' participation activity did not indicate the quality of the information carried by the traders. In our field experiment there was a high uncertainty in predicting the outcomes of real business practices in a dynamic business environment. Nevertheless, the number of transactions at the contract level, representing the agreed opinion between traders, indicated a common recognition of the quality or certainty of the information carried into the market. Therefore, this indicator manifested the positive impact of traders' participation activity to capture market consensus in an internal prediction market. Thus, traders' participation activity and information aggregation efficiency hypothesis (Hypothesis 2a) is supported.

With regard to traders' dynamic interactions, at the contract level all the indicators had a significant effect on information aggregation efficiency, including the number of 1-influential orders, 2-influential orders and 2Out3-influential orders. Again, there were no occurrences of 3-influential orders among the traders. At the trader level, the results did not reveal a significant effect of traders' self-revisions on information aggregation efficiency (the number of Type I and Type II selfrevisions was the same in all the markets, as previously discussed). This result implies that although traders updated their personal expectations on the contracts, this adjustment did not always influence another trader's adjustment. While different influential orders at the contract level had an impact on information aggregation efficiency, self-revisions at the trader level did not. Thus, traders' dynamic interaction and information aggregation efficiency hypothesis (Hypothesis 2b) is supported.

4.4. Effects of information aggregation efficiency on market predictive accuracy

We first calculated the point estimation based on the transaction prices of a market and identified the corresponding contract in each market. Table 4 exhibits the market prediction based on the last transaction price and the weighted average transaction price of contracts. The corresponding percentage error per contract compared to the actual result is also listed under different market conditions,<sup>8</sup> Fig. 2b illustrates the market predictive accuracy throughout the 12 markets.

Subsequently, we drew a scatter plot based on information aggregation efficiency and market predictive accuracy, and plotted a linear trend line. The trend lines drawn based on the last transaction price and the weighted average price of a contract (see Fig. 3a and b) showed that the prediction percentage error changes with the change of information aggregation efficiency in the same direction. This result indicated a positive correlation between the information aggregation efficiency and market predictive accuracy, supporting information aggregation efficiency and market predictive accuracy hypothesis (Hypothesis 3).

## 5. Discussions

In this section we further discuss the results drawn from the field experiment. We focus on the influence of different information transparency levels on traders' behavior and we discuss market performance in terms of information aggregation efficiency and market predictive accuracy.

## 5.1. Effect of information transparency on traders' behavior

The field experiment shows that the transparency level of quote information does not seem to affect traders' participation activity. This result is partially consistent with Bloomfield and O'Hara [8], who found that when trade information is disclosed, quote disclosure has little effect on market participation, as trade transparency provides information that cannot be obtained from knowing only quotes. However, considering the difference in experimental settings used in our study, Bloomfield and O'Hara's [8] explanation does not fully explain our research results. In their experiment trade information was very transparent, as all trade information of an individual trader was available to other traders in a market. On the contrary, in our experiment, trade information was very limited, as only the last transaction price of each contract was presented, if at all.

We argue that in prediction markets, particularly internal prediction markets where there are only a limited number of traders, the main factor that drives traders' activity is the interest and motivation of the trader, though the specific interest of each trader can be different. For example, some people are interested in the prediction of specific business practices, others are interested in observing colleagues' opinion on the potential outcomes of future events, and some have higher enjoyment in playing in the market. Moreover, prior studies suggested that a properly designed incentive scheme is able to motivate traders to trade and reveal information in prediction markets [14,15], suggesting the importance of the incentive scheme in driving traders' participation activity in an internal prediction market.

a)  
![](/api/attachments/XD6AQBRH/fulltext/images/6023880a75d77049ba2b0dff76887b6ee334912d7710c0072dd7c14f49b9ed8f.jpg)

b)  
![](/api/attachments/XD6AQBRH/fulltext/images/e784258abbda4175b905770a3e3e778fe5ecd7da622b5fd1da315c75af443fec.jpg)  
Fig. 3. a. Market performance based on the last transaction price of a contract. b. Market performance based on the weighted average transaction price of a contract.

In addition, the results show that the transparency of the highest buy order and the lowest sell order does not enhance traders' dynamic interactions compared to the absence of this information (see Table 2). A possible reason is that traders are very careful in interpreting the quote information in the market. As traders are self-interested, some traders may place buy and sell orders that in fact deviate from their true expectations so as to affect other traders' estimations and benefit from this behavior (signaling). Informed traders may recognize that the signaler's information is not true, yet they would nevertheless take advantage of the opportunity to profit by selling their shares of the contract at the high price offered by the signaler or buy the shares of the contract at the low price from the signaler. However, in a real business environment, particularly in a new and dynamic business, employees rarely know whether information is true or not in an internal prediction. As a result, to avoid being misled by the signaler, they may not adjust their expectations more frequently in the partiallytransparent market condition than in the opaque market condition. Nevertheless, when different traders' quote information is displayed for a contract, traders can better discern the quality of the information. Therefore, there is an increased level of traders' dynamic interactions in the semi-transparent market condition.

Most interestingly, we found that complete quote information does not lead to a further increase in traders' dynamic interactions. In fact, the disclosure of all quote information in the fully-transparent market condition reduces the dynamic interactions among traders compared to a semi-transparent market condition. This is probably because traders usually learn from more representative signals [4]. In a semitransparent market condition we showed the highest three outstanding buy orders and the lowest three outstanding sell orders. The prices of these outstanding buy and sell orders are the most representative signals, as they carry the most meaningful information. Another possible explanation is that due to the objective limits of traders' information processing capability, complete quote information becomes overloaded information [57], which exceeds the decision-maker's capacity to process [39,72]. Furthermore, our results are consistent with the notion of information saturation in a market: beyond a certain point, more information does not improve market performance any further [43,46]. We did not attempt to identify the point of information saturation in a market in our study, yet if it exists, disclosure of information beyond the point of saturation would yield no further improvement to market performance through traders' behavior.

## 5.2. Market performance

In this paper we examine two aspects of market performance: information aggregation efficiency and predictive accuracy. The field study demonstrates the ability of internal prediction markets to aggregate traders' agreed opinion. We conducted an ex-post analysis by dividing the information aggregation efficiency of the 12 markets into low and high categories (17–40 ➔ high; 41–64 ➔ low) (see Table 4). Based on the last transaction prices of contracts, the information aggregation efficiency of nine markets is considered to be high, whereas the information aggregation efficiency of two markets is considered to be low. Based on the weighted average transaction prices of contracts, seven markets achieved high information aggregation efficiency, whereas five markets achieved low information aggregation efficiency. In other words, approximately, 75% of the markets aggregated the information efficiently.

This result shows that even under a dynamic and uncertain circumstance, a prediction market can reflect traders' mean belief in the transaction prices of contracts. This noticeable ability to capture traders' mean belief allows practitioners to obtain employees' agreed opinions. Particularly, as the prediction market mechanism induces participants to reveal their true information [36,68], the use of prediction markets can help companies tackle the agency problem, namely that the principal cannot verify that the agent has behaved appropriately [18]. In terms of forecasting, the agency problem usually arises due to different goals or interests between the principal and the agent. For example, executives need true forecast from the employees; however, employees may reveal a lower forecast than they actually anticipate so as to receive a possible additional reward when their performance exceeds the prediction. The use of internal prediction markets can help these executives to bypass the agency problem and collect their employees' true forecast.

![](/api/attachments/XD6AQBRH/fulltext/images/9fbeba1c2d2ceb54b02122540e77f0d98c5ceb9b8c3f8109921329347bbcb953.jpg)  
Fig. 4. Information transparency and information aggregation efficiency.

To examine the direct effect of information transparency levels on the information aggregation efficiency of a prediction market, we draw their relationship in Fig. 4. It suggests a non-linear relationship, implying that the semi-transparent market condition leads to the most efficient information aggregation in a prediction market. Surprisingly, the fully-transparent market condition in fact decreases information aggregation efficiency (instead of further improving it). A possible explanation is that the performance of a prediction market well reflects the aggregated individual traders' performance. Our finding on the effect of information transparency on traders' behavior is consistent with early studies on the relationship between information load and decision-making. People possess a limit for information processing [39,72] and the relationship between decision quality and information processed follows an inverted U-shaped curve. A prediction market is usually led by marginal traders, who are relatively free of judgment bias and thus consistently buy and sell at prices very close to the equilibrium price, leading the market to be efficient [20]. The information aggregation efficiency of a prediction market in fact reflects their aggregated decision quality. When the information transparency level increases, traders receive more information leading to an increase in individual decision quality, particularly of marginal traders, and thus information aggregation efficiency improves. This continues until the amount of information exceeds the processing capacity of the traders, particularly marginal traders. In turn, their individual decision quality decreases, leading to lower information aggregation efficiency. In this paper our measurement of information aggregation efficiency is based on the comparison between the transaction price and the dynamic equilibrium price of a contract. The smaller the average percentage deviation is, the higher the information aggregation efficiency (see Section 3.3). As a result, our study suggests a U-shape between the information transparency level and information aggregation efficiency. This result manifests the ability of a prediction market to aggregate traders' agreed opinions.

With regard to market predictive accuracy, our research shows that internal prediction markets can make rather accurate predictions, even under dynamic and highly uncertain business conditions. Our field experiment environment involved new business products, a complex industry and a dynamic context. Within such a highly uncertain situation, 5 out of 12 markets (42%) yielded accurate predictions of the KPIs (the forecasted contract was the same as the actual one), while 6 out of 12 markets (50%) yielded predictions very close to the actual results (the forecasted contract was adjacent to the actual one). A previous study investigated prediction market performance under different levels of market complexity and found that the performance of a prediction market is less satisfactory in an environment characterized by higher information complexity compared to lower information complexity [35]. This difference is particularly evident when there are only a limited number of traders in a market. Thus, comparing to the results reported in the well-known research on HP internal prediction markets, where 6 out of 8 markets (75%) predicted accurately [64], our experiment is proven to be very successful.

## 6. Conclusion

In this section we summarize the key findings of this paper, present its contributions to the literature and business practice, and discuss its limitations and avenues for future research.

## 6.1. Summary of key findings

This paper examines the effect of information transparency on prediction market performance. We studied the impact of different transparency levels of quote information on market performance in internal prediction markets in a real business environment. Our empirical findings reveal that information transparency affects the information aggregation efficiency of a market through traders' behavior, particularly through traders' dynamic interactions. Different transparency levels show non-linear effects on traders' dynamic interactions. When different traders' buy and sell orders are disclosed in a prediction market: traders learn most actively and actively update their own expectations on the contracts; the influence of one trader's learning on one other trader occurs most frequently; and a trader's updated expectation on the contract sometimes influences two different traders. However, the disclosure of all outstanding buy and sell orders does not further enhance the traders' dynamic interactions.

Different information transparency levels do not impact traders' participation activity in a prediction market. This suggests that other design factors, such as incentives, perhaps need to be considered to further motivate traders to participate in internal prediction markets. For instance, Chen et al. [14] demonstrated that traders can be motivated when their trading performance is associated with the endowment they receive.

Traders' participation activity and traders' dynamic interactions positively affect the information aggregation efficiency of a prediction market. Higher participation levels and active learning behavior of traders lead to a market consensus that is closely reflected in the transaction prices of contracts. Moreover, the traders' consensus captured by the market indicates the actual outcome of the future event. A market with higher information aggregation efficiency is likely to predict more accurately. Additionally, despite the dynamic environment, prediction markets have a salient ability to make accurate predictions.

## 6.2. Theoretical contributions

This paper makes several contributions to the literature on information transparency and prediction markets. With regard to information transparency, we theoretically develop and empirically test the impacts of information transparency in the context of prediction markets. This extends previous studies on information transparency that focused on B2B [37,40,42,60,87,88] and B2C markets [26,84]. The context of prediction markets allows us to examine the effect of information transparency on traders in a double auction who are buyers as well as sellers. The research, therefore, further adds to the aforementioned studies. Second, unlike prior research that is limited to the effect of either opaque or transparent conditions of a market [25,76,77], this paper examines the impact of different information transparency levels, contributing to the research on transparency strategy [27].

With regard to the literature on prediction markets, this paper is one of the first to take an information-based view to study prediction market design and highlights the importance of information transparency in the design of prediction markets. This paper, therefore, extends the research on prediction market performance that has primarily focused on the effects of incentives (real-money vs. play-money) offered to participants [49,71,73,78], market size [36,44], market liquidity [1], composition of traders [44,80], traders' individual social networks [67], and contract design [44,85]. Second, this paper adds to the literature on prediction markets by distinguishing between information aggregation efficiency and market performance in the analysis of market performance. We defined and developed a new measurement for information aggregation efficiency and empirically tested the relationship between information aggregation efficiency and market predictive accuracy.

## 6.3. Managerial implications

The prediction markets used inside companies are usually small with a limited numbers of employees actively participating. This paper reveals that the information exchange done through the traders' dynamic interactions is crucial to market forecasting accuracy. According to our research findings, disclosure of various outstanding buy and sell orders can encourage traders in a thin prediction market to learn from their previous trading actions and other traders' decisions. Traders' dynamic interactions can be improved and information can be aggregated more efficiently, leading to more accurate predictions. Our research suggests that companies adopt a semi-transparent level, instead of a fully-transparent level, which shows a number of outstanding buy and sell orders in the market to raise dynamic interactions among a limited number of traders. Moreover, using our measurement of information aggregation efficiency proposed in this paper, managers are able to evaluate the extent to which the market outcome reflects the agreed opinions of employees. This measure may also indicate to managers whether the market forecast should be adopted.

## 6.4. Limitations and future research

We investigated traders' learning behavior in accordance with their trading activities in a market. In our field experiment, we could not observe traders' initial personal estimation of the company's KPIs before the start of the prediction markets. We attempted by inviting the employees to complete an online questionnaire, but only a few employees provided their individual predictions. Future research can compare a trader's individual estimation of a future event before and after a prediction market. This comparison can indicate whether traders indeed learn in a market.

We measured prediction market performance based on forecasting accuracy. In practice, it is also important to assess if managers think that market performance is satisfactory as they may have different criteria to evaluate a market outcome. Future research will benefit from not only exploring the managers' motivations for an internal prediction market, but also evaluating market performance based on their satisfaction because their positive evaluation can determine whether an internal prediction market will be adopted.

This paper focused only on quote information to study information transparency. Future research can examine other types of price or non-price information in prediction markets, for example, the last number of transactions of each contract and the dynamic ranking of traders.

In this paper we did not capture a trader's actual use of information sources in a prediction market, for example, what price information, to what extent and in what sequence the trader looks at different information elements. Knowing this information can help us further influence their learning behavior and further understand how information transparency affects traders' use of information sources. Future research can use eye tracking to study the details of the trader's eye movement and gain insight into what a trader finds interesting and what draws her attention, for example, using measures such as the sequence and the duration of attention on different areas of interest or information stimuli.

## References

[1] M. Abramowicz, Deliberative information markets for small groups, in: R.W. Hahn, P.C. Tetlock (Eds.), Information Markets: A New Way of Making Decisions, The AEI Press, Washington, D.C. 2006, pp. 101–125.

[2] J.S. Armstrong, Long-range Forecasting: From Crystal Ball to Computer, Wiley, New York, 1985.

[3] J.S. Armstrong, Principles of Forecasting: A Handbook for Researchers and Practitioners Kluwer Academic Publishers Massachusetts 2001

[4] L.R. Anderson, C.A. Holt, Information cascades in the laboratory, The American Economic Review 87 (5) (1997) 847–862

[5] R. Bapna, P. Goes, A. Gupta, Y. Jin, User heterogeneity and its impact on electronic auction market design: an empirical exploration, MIS Quarterly 28 (1) (2004) 21–43.

[6] J.E. Berg, T.A. Rietz, The Iowa electronic markets: stylized facts and open issues, in: R.W. Hahn, P.C. Tetlock (Eds.), Information Markets: A New Way of Making Decisions, The AEI Press, Washington, D.C. 2006, pp. 142–169

[7] J.E. Berg, F.D. Nelson, T.A. Rietz, Prediction market accuracy in the long run, International Journal of Forecasting 24 (2) (2008) 283–298.

[8] R. Bloomfield, M. O'Hara, Market transparency: who wins and who loses? The Review of Financial Studies 12 (1) (1999) 5–35.

[9] E. Bonabeau, Decisions 2.0: the power of collective intelligence, MIT Sloan Management Review 50 (2) (2009) 45–52.

[10] O. Bondarenko, P. Bossaerts, Expectations and learning in Iowa, Journal of Banking & Finance 24 (2000)1535–1555.

[11] E. Bothos, D. Apostolou, G. Mentzas, Collective intelligence with web-based information aggregation markets: the role of market facilitation in idea management, Expert Systems with Applications 39 (2012) 1333–1345.

[12] C.F. Camerer, Can asset markets be manipulated? A field experiment with race-track betting, Journal of Political Economy 106 (3) (1998) 457–482.

[13] L. Chen, P. Goes, J.R. Marsden, Z. Zhang, Design and use of preference markets for evaluation of early stage technologies, Journal of Management Information Systems 26 (3) (2009) 45–70.

[14] L. Chen, P. Goes, W. Harris, J.R. Marsden, J. Zhang, Preference markets for innovation ranking and selection, Interfaces 40 (2) (2010) 144–153.

[15] B. Cowgill, J. Wolfers, E. Zitzewitz, Using prediction markets to track information flows: evidence from Google, Working Paper, 2008.

[16] T.H. Davenport, J.G. Harris, What people want (and how to predict it), MIT Sloan Management Review 50 (2) (2009) 23–27.

[17] D.D. Davis, C.A. Holt, Experimental Economics, Princeton University Press, Princeton, New Jersey, 1993.

[18] K.M. Eisenhardt, Building theories from case study research, Academy of Management Review 14 (4) (1989) 532–550.

[19] A. Field, G. Hole, How to Design and Report Experiments, SAGE Publications, London, 2003.

[20] R. Forsythe, F. Nelson, G.R. Neumann, J. Wright, Anatomy of an experimental political stock market, American Economic Review 82 (5) (1992) 1142–1161.

[21] R. Forsythe, T. Rietz, T. Ross, Wishes, expectations and actions: a survey on price formation in election stock markets, Journal of Economic Behavior and Organization 39 (1999) 83–110.

[22] B. Gadanecz, R. Moessner, C. Upper, Economic derivatives, BIS Quarterly Review (March 2007) 69–81.

[23] S. Gjerstad, Risk aversion, beliefs, and prediction market equilibrium, Working Paper, 2004.

[24] N.F. Granados, A. Gupta, R.J. Kauffman, Transparency strategy in Internet-based selling, in: K. Tomak (Ed.), Advances in the Economics of Information Systems, Idea Group Publishing, Harrisburg, PA 2005, pp. 80–112.

[25] N. Granados, A. Gupta, R.J. Kauffman, The impact of IT on market information and transparency: a unified theoretical framework, Journal of the Association for Information Systems 7 (3) (2006) 148–178.

[26] N. Granados, A. Gupta, R.J. Kauffman, Designing online selling mechanisms: transparency levels and prices, Decision Support Systems 45 (4) (2008) 729–745.

[27] N. Granados, A. Gupta, R.J. Kauffman, Information transparency in business-toconsumer markets: concepts, framework, and research agenda, Information Systems Research 21 (2) (2010) 207–226.

[28] S.J. Grossman, An introduction to the theory of rational expectations under asymmetric information, Review of Economic Studies 48 (4) (1981) 541–559.

[29] T.S. Gruca, J.E. Berg, M. Cipriano, Consensus and differences of opinion in electronic prediction markets, Electronic Markets 15 (1) (2005) 13–22.

[30] R.W. Hahn, P.C. Tetlock, Introduction to information markets, in: R.W. Hahn, P.C. Tetlock (Eds.) Information Markets: A New Way of Making Decisions The AEl Press. Washington. D.C. 2006, pp. 1–12.

[311 R. Hanson, Decision markets, IEEE Intelligent Systems 14 (3) (1999) 16–19

[32] R. Hanson, Combinatorial information market design, Information Systems Frontiers 5 (1) (2003) 107–119.

[33] R. Hanson, Foul play in information markets, in: R.W. Hahn, P.C. Tetlock (Eds.), Information Markets: A New Way of Making Decisions, The AEI Press, Washington, D.C. 2006, pp. 126–141.

[34] F.A. Hayek, The use of knowledge in society, The American Economic Review 35 (4) (1945) 519–530.

[35] P.J. Healy, S. Linardi, J.R. Lowery, J.O. Ledyard, Prediction markets: alternative mechanisms for complex environments with few traders, Management Science 56 (11) (2010) 1977–1996.

[36] T.H. Ho, K.Y. Chen, New product blockbusters: the magic and science of prediction markets, California Management Review 50 (1) (2007) 144–158.

[37] W. Hoffman, J. Keedy, K. Roberts, The Unexpected Return of B2B, The McKinsey Quarterly, August 2002.

[38] J.W. Hopman, Using forecasting markets to manage demand risk, Intel Technology Journal 11 (2) (2007) 127–136.

[39] J. Jacoby, D.E. Speller, C.K. Berning, Brand choice behavior as a function of information load, Journal of Marketing Research 11 (1) (1974) 63–69.

[40] A. Jain, K.A. Moinzadeh, Supply chain model with reverse information exchange Manufacturing and Service Operations Management 7 (4) (2005) 360–378.

[41] A. Kambil, E. van Heck, Making Markets, Harvard Business School Press, Boston, 2002

[42] K.K. Kim, N.S. Umanath, B.H. Kim, An assessment of electronic information transfer in B2B supply-channel relationships Journal of Management Information Systems 22 (3) (2005).294–320

[43] O. Koppius, Information architecture and electronic market performance, ERIM Ph.D. Series Research in Management 13 The Netherlands 2002

[44] J.O. Ledyard, Designing information markets for policy analysis, in: R.W. Hahn, P.C. Tetlock (Eds.) Information Markets: A New Way of Making Decisions The AEl Press. Washington, D.C. 2006, pp. 37–66

[45] L. Li, Cournot oligopoly with information sharing, The Rand Journal of Economics 16 (4) (1985) 521–536.

[46] T. Li, R.J. Kauffman, E. van Heck, P. Vervest, B. Dellaert, Consumer informedness and firm information strategy, Information Systems Research 25 (2) (2014) 345–363.

[47] R.E. Lucas, Expectations and the neutrality of money, Journal of Economic Theory 4 (2) (1972) 103–124.

[48] R.E. Lucas, Asset prices in an exchange economy, Econometrica 46 (1978) 1429-1445.

[49] S. Luckner, C. Weinhardt, How to pay traders in information markets: results from a field experiment, Journal of Prediction Markets 1 (2) (2007) 147–156.

[50] A. Madhavan, Consolidation, fragmentation, and the disclosure of trading information, Review of Financial Studies 8 (3) (1995) 579–603.

[51] T.W. Malone, Bringing the market inside, Harvard Business Review 82 (4) (2004) 107–114.

[52] T.W. Malone, The Future of Work, Harvard Business School Press, Boston, Massachusetts, 2004.

[53] T.W. Malone, M. Klein, Harnessing collective intelligence to address global climate change, Innovations 2 (3) (2007) 15–26.

[54] T.W. Malone, R. Laubacher, C. Dellarocas, The collective intelligence genome, MIT Sloan Management Review 51 (3) (2010) 201–231.

[55] J.F. Muth, Rational expectations and the theory of price movements, Econometrica 29 (3) (1961) 315–335.

[56] K. Oliven, T.A. Rietz, Suckers are born but markets are made: individual rationality arbitrage and market efficiency on an electronic futures market, Management Science 50 (3) (2004) 336–351.

[57] C.A. O'Reily, Individual and information overload in organizations: is more necessarily better? Academy of Management Journal 23 (4) (1980) 684–696

[58] G. Ortner, Forecasting markets — an industrial application, Working Paper, Technical University of Vienna, 1998.

[59] M. Pagano, A. Röell, Transparency and liquidity: a comparison of auction and dealer markets with informed trading, The Journal of Finance 51 (2) (1996) 579–611.

[60] R. Patnayakuni, A. Rai, N. Seth, Relational antecedents of information flow integration for supply chain coordination, Journal of Management Information Systems 23 (1) (2006) 13–49.

[61] D. Pennock, A dynamic pari-mutuel market for hedging, wagering, and information aggregation, EC '04 Proceedings of the 5th ACM Conference on Electronic Commerce May 17–20 New York 2004, pp. 170–179.

[62] J. Pethokoukis, All Seeing All Knowing, U.S. News & World Report, August 22 2004.

[63] C.R. Plott, Markets as information gathering tools, Southern Economic Journal 67 (1) (2000) 2–15.

[64] C.R. Plott, K.Y. Chen, Information aggregation mechanisms: concept, design and implementation for a sales forecasting problem, Social Science Working Paper (1131), California Institute of Technology, 2002.

[65] C.R. Plott, S. Sunder, Efficiency of experimental security with insider information: an application of rational expectations models, Journal of Political Economy 90 (4) (1982) 663–698.

[66] C.R. Plott, S. Sunder, Rational expectations and the aggregation of diverse information in laboratory security markets, Econometrica 56 (5) (1988) 1085–1118.

[67] L. Qiu, H. Rui, A.B. Whinston, Effects of social networks on prediction markets: examination in a controlled experiment, Journal of Management Information Systems 30 (4) (2014) 235–268.

[68] R. Ray, Prediction markets and the financial ‘wisdom of crowds’, The Journal of Behavioral Finance 7 (1) (2006) 2–4.

[69] P.W. Rhode, K.S. Strumpf, Historical presidential betting markets, Journal of Economic Perspectives 18 (2) (2004) 127–142

[70] E.S. Rosenbloom, W. Notz, Statistical tests of real-money versus play-money prediction markets. Electronic Markets 16 (1) (2006) 63–69.

[71] R.D. Sauer, The economics of wagering markets, Journal of Economic Literature 36 (4) (1998) 2021–2064.

[72] H.M. Schroder, M.J. Driver, S. Streufert, Human Information Processing: Individuals and Groups Functioning in Complex Social Situations, Reinhart and Winston, Holt 1967.

[73] E. Servan-Schreiber, J. Wolfers, D.M. Pennock, B. Galebach, Prediction markets: does money matter? Electronic Markets 14 (3) (2004) 243–251.

[74] W.R. Shadish, T.D. Cook, D.T. Campbell, Experimental and Quasi-experimental Designs for Generalized Causal Inference, Houghton Mifflin, Boston, 2002.

[75] C. Shapiro, Exchange of cost information in oligopoly, The Review of Economic Studies 53 (3) (1986) 433–446.

[76] M.D. Smith, The impact of shopbots on electronic markets, Journal of the Academy of Marketing Science 30 (4) (2002) 446–454.

[77] C. Soh, M.L. Markus, K.H. Goh, Electronic marketplaces and price transparency: strategy, information technology, and success, MIS Quarterly 30 (3) (2006) 705–723.

[78] M. Spann, B. Skiera, Internet-based virtual stock markets for business forecasting, Management Science 49 (10) (2003) 1310–1326.

[79] C. Sunstein, When Crowds Aren't Wise, Harvard Business Review, September 2006.

[80] J. Surowiecki, The Wisdom of Crowds: Why the Many are Smarter Than the Few, ABACUS London 2004

[81] D. Tapscott, D. Ticoll, The Naked Corporation: How the Age of Transparency Will Revolutionize Business Free Press, New York, 2003

[82] P.C. Tetlock, Does liquidity affect securities market efficiency? Working Paper, University of Texas, Austin, 2007.

[83] G. Tziralis, I. Tatsiopoulos, Prediction markets: an extended literature review, The Journal of Prediction Markets 1 (2007) 75–91.

[84] S. Viswanathan, J. Kuruzovich, S. Gosain, R. Agarwal, Online infomediaries and price discrimination: evidence from the automotive retailing sector, Journal of Marketing 71 (3) (2007) 89–107.

[85] J. Wolfers, E. Zitzewitz, Prediction markets, Journal of Economic Perspectives 18 (2) (2004) 107–126.

[86] J. Wolfers, E. Zitzewitz, Interpreting prediction market prices as probabilities, Working Paper, 2006.

[87] K. Zhu, Information transparency in electronic marketplaces: why data transparency may hinder the adoption of B2B exchanges, Electronic Markets 12 (2) (2002) 92–99.

[88] K. Zhu, Information transparency of business-to-business electronic markets: a game-theoretic analysis, Management Science 50 (5) (2004) 670–685.

![](/api/attachments/XD6AQBRH/fulltext/images/7c6b846ed309ba768e11cfac276b0ae45d97293956a199b4d691f6ed0d189928.jpg)

ShengYun Yang ( annieshengyun@gmail.com) received her Ph.D. from Rotterdam School of Management, Erasmus University in 2014. Before joining the academia, she worked in the fashion and automotive industries. Her research interests include prediction markets, electronic commerce, smart metering, innovation management, and technology catching-up. She published business and teaching cases about Chinese e-commerce, Chinese firms catching up, and internationalization of Chinese enterprises in Financial Times, The Case Centre, and Ivey. She presented at various conferences, including the Symposium on Remote Sensing and Social Development. She is a member of the China Association for Science and Technology and an active member of several research centers in China.

![](/api/attachments/XD6AQBRH/fulltext/images/52d80f8fa1184760bf8b7ab8bbe2d104de138ed89e089a575de626c4d29dfe05.jpg)

Ting Li ( tli@rsm.nl) is an associate professor of information systems at the Rotterdam School of Management, Erasmus University in the Netherlands and a visiting associate professor at the Fox School of Business, Temple University. Her research interests include strategic and economic impacts of IT consumer decision-making in the online and mobile channels pricing and revenue management and business networks. Her work has been published in the Information Systems Research, Decision Support Systems, International Journal of Electronic Commerce, European Journal of Information Systems, and many others. She was the runner-up for Prof. Aart Bosman Dissertation Award and Accenture-PIM Marketing Science Dissertation Award. Her interdisciplinary research has been sponsored by multiple grants from the

Dutch National Science Foundation (NWO). Prior to joining academic, she worked for General Electric and IBM in the area of e-business in supply chains, web services, and grid computing. She obtained her Ph.D. in Management Science at the Erasmus University and MSc in Computational Science at the University of Amsterdam.

![](/api/attachments/XD6AQBRH/fulltext/images/549efd8034f0b1005522d2d01783cb2a78ecca8ec841165b067d77679eebee6c.jpg)

Eric van Heck ( evanheck@rsm.nl) is a professor of information management and markets at the Rotterdam School of Management, Erasmus University, in the Netherlands. He received his MSc and Ph.D. from Wageningen University. He has been a research fellow at the Center for Economic Research of Tilburg University, an assistant professor at Wageningen University, and a visiting scholar at New York University, He also worked for Cap Gemini, He is currently a research fellow at the Erasmus Research Institute of Management (ERIM). Earlier he was ERIM's director of doctoral education, a visiting professor at the Helsinki School of Economics and the Ludwig-Maximilians University in Munich, and a visiting scholar at MIT Sloan School of Management. His research focuses on the strategic and operational use of IT for companies and markets. His articles have appeared in many leading journals, and he has co-authored or coedited fourteen books, including Making Markets (HBS Press, 2002) and Smart Business Networks (Springer, 2005). He is best known for his work on how companies can create value with on-line auctions.

Please cite this article as: S. Yang, et al., Information transparency in prediction markets, Decision Support Systems (2015), http://dx.doi.org/ 10.1016/j.dss.2015.05.009
