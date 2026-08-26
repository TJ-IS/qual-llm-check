---
otero_id: 5540
otero_key: "6XUH9N7X"
title: "User participation in a corporate prediction market"
authors: "Daniel E. O'Leary"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.07.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Daniel E. O'Leary ⁎

University of Southern California Marshall School of Business 3660 Trousdale Parkway Los Angeles, CA 90089-0441, USA

## a r t i c l e i n f o

Article history: Received 25 July 2014 Received in revised form 3 June 2015 Accepted 13 July 2015 Available online 30 July 2015

Keywords: Corporate prediction market Day-of-week effect User participation Information asymmetries Social media

## a b s t r a c t

Corporate prediction markets allow companies to use external market concepts to facilitate and support corporate decision making. Recently, Google, Microsoft, GE, Best Buy, and other firms have generated and used prediction markets as a means of gathering the “collective” intelligence of their employees. Since these markets capture and aggregate information from employees and ultimately provide information for decision making, some researchers have referred to them as decision support systems or group decision support systems. Unfortunately, there has been limited theory development and empirical investigation of participation in corporate prediction markets. Accordingly, the purpose of this paper is to use theory generated about external investment markets to investigate participation behavior in an internal corporate market. Analysis of the number of unique traders by date and market leads to a number of findings, including that market traders apparently trade on specific information, there is a day-of-the-week effect of their participation, and participation is decreasing over time. Understanding the existence of such effects is important because they can influence the ability of the market to provide sufficient, timely, and quality decision support information.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Prediction markets bring concepts of investment markets into corporations to gather information from employees to price potential events, resulting in a market for predictions. As a result, prediction markets are one approach that has been promoted as being used by companies (Dvorak [17]) to gather the “wisdom of the crowd” (Surowiecki [41]). A number of leading edge technology firms have made use of prediction markets internally, including Google (Cowgill et al. [13]), Microsoft (Berg [3]), and GE (Spears et al. [38]). Further, McKinsey held a forum to study the promise of prediction markets (Dye [16]). As a result, it is not surprising that prediction markets have been featured in key publications including The New York Times (Lohr [27]) and The Wall Street Journal (Dvorak [17]).

More recently, Rydholm [37] noted that prediction markets are among the top 5 “newer techniques” that have potential to add value for corporate marketing objectives by solving business problems. In that survey, prediction markets ranked above other emerging technologies such as crowd sourcing, gamification, biometrics, and facial coding. Prediction markets were grouped with social media, big data analytics, and text analytics as providing particularly high potential.

Prediction markets, generally accepted as part of so-called “web 2.0” (e.g., Chui et al. [9] and Consensus Point [12]), introduce “stock markets” into corporations in an effort to gather and aggregate knowledge and information from participants, typically, employees. Stocks, such as “project X will be completed by June 1” are traded among participants in order to gather data from throughout the company as to estimates of the probability of such events. Thus, prediction markets are run in order to make predictions about future events (e.g., Berg and Reitz [4]) to provide information to support decisions (e.g., Hanson [22], Berg and Reitz [4] and Sprenger et al. [39]). As a result, prediction markets provide an organizational decision support system that depends on participation from a range of employees and groups within the organization.

## 1.1. User participation in markets—The human side of prediction markets

Unfortunately, there has been limited analysis of the “human side” of these markets. In particular, there has been limited empirical research into participation patterns by employees in these markets. If a prediction market is to serve as a decision support system, then it is important that the system consistently provides sufficient, timely, and quality information.

Participation is critical for the generation of sufficient information for the system. First, if there are few traders rather than more traders, then there is less likely to be the sufficient or timely information flows to the system to support decision making. For example, in the firm analyzed, there are days where there are zero traders and stocks with as few as three total traders, indicating limited information flows in such settings. Second, if there are more traders rather than few traders then market prices become more informative because the price is averaging more predictions (Grossman and Stiglitz [20]). Accordingly, prediction markets generally work “better” with more participants rather than fewer.

Further, it is important that the prediction market process gathers quality information from the crowd and embeds that information in the price of the different events. Unfortunately, apparently some tactics used by traders in prediction markets try to mislead the market rather than trading on information and building that information into the price. Other traders take approaches, such as assuming that projects will always be late, and always betting against projects finishing by their deadline. As a result, it is important to determine if there is evidence that internal traders trade on information.

Finally, the long-run viability of such systems is dependent on sufficient and continued participation from employees. As a result, it is critical to investigate apparent participation patterns in order to determine the extent to which participation in such markets continues to persist over time.

## 1.2. Purpose of this paper

Although prediction markets have been around for a number of years, the actual use of prediction markets internally for business decision making has been a relatively recent and apparently limited phenomena in corporate environments (Nocera [31]). As a result, there has been limited analysis of actual corporate markets and limited access to actual corporate data use from prediction markets. Accordingly, there has been limited theoretical development and limited analysis of their actual use in corporate settings. As a result, Rieg and Schroder ([35], p. 35) note that there have been “… hardly a handful of cases published.”

Although some companies may generate and analyze such data internally, unfortunately, data such as these generally are not made publicly available to academics. However, this paper uses access to actual corporate prediction data, in order to begin to address some of the unique issues associated with such markets in corporations. Specifically, this paper investigates some characteristics of corporate prediction markets drawing on actual participation data derived from a well-known company that has used prediction markets, Best Buy.

Accordingly, the purpose of this paper is to analyze the trader participation of two different employee groups (“corporate” and “retail”) on two different types of prediction market problems (corporate and retail), given that traders can trade on any of the stocks in the market. This analysis provides a number of findings from this data, including evidence that, as in external financial markets,

• Although traders might use multiple approaches as the basis of their trades, more corporate (retail) traders apparently trade on corporate (retail) information available to them, thus suggesting that markets are a good approach to gather decision support information about events from knowledgeable participants.

• There are “day-of-the-week” effects associated with the number of unique traders in this corporate prediction market, suggesting that such effects need to be considered when using markets to generate information or predictions within companies, particularly as a decision support system.

• There is a “beginning of the month” effect with a differential number of unique traders in the beginning of the month compared to the markets at the end of the month, suggesting that market designers consider this as they generate prediction markets for decision support.

• There is a “monthly” effect with differential numbers of unique traders involved in the markets during different months suggesting that market designers take this into account as they implement prediction markets for decision support systems.

In addition, in this corporate prediction market,

• The number of unique (daily) traders rapidly decreases over time but the rate of those decreases differs between the two groups of employees (corporate and retail). Unfortunately, the decreasing rate of participation ultimately could jeopardize the use of prediction markets as decision support systems as the number of participants drops.

In developing these findings, this paper employs theory that has been developed in finance for investment markets and uses that theory to better understand a decision support technology that is “part markets and part technology.” Further, this paper applies that theory to this context of corporate prediction markets, facilitating an understanding of such internal markets in terms of previously developed theories.

## 1.3. Outline of this paper

Section 1 of this paper has briefly introduced the notion of prediction markets, motivated the paper and discussed the purpose of the paper. Section 2 analyzes some previous research involving corporate prediction markets. Section 3 summarizes the available data and discusses the background of the company, Best Buy. Section 4 establishes expectations regarding the potential findings in the data, while section 5 examines the findings from analyzing the data. Section 6 examines some of the business implications of these markets, while Section 7 briefly summarizes the paper, its contributions and provides some extensions.

## 2. Background: Markets, open prediction markets, and corporate prediction markets

This section provides a brief summary of prediction markets and some of their characteristics, with a focus on corporate prediction markets. Corporate prediction markets differ from traditional approaches that focus on gathering knowledge and information from corporate experts, and instead make use of the so-called “wisdom of the crowds” (Surowiecki [41]), gathering knowledge that is broadly distributed among the employees. This approach is consistent with economic theory. For example, as noted by Hayek [24] “…knowledge (is) not given to anyone in its totality. Instead “…the knowledge of the circumstances of which we must make use never exists in concentrated or integrated form, but solely as the dispersed bit of incomplete and frequently contradictory knowledge which all the separate individuals possess.” As a result, it is critical for prediction markets to be able to consistently draw on broad-based participation of employees.

## 2.1. Markets: Prediction vs. investment and open vs. closed

Fig. 1 illustrates two key characteristics associated with corporate prediction market use. First, prediction markets are in contrast to investment markets, such as the New York Stock Exchange. Investment markets focus on pricing assets, whereas prediction markets focus on predicting events. For example, the Hollywood Stock Exchange (http:// www.hsx.com/) uses a market to forecast movie revenues. Second, markets can be either open or closed. Open markets accommodate virtually all interested parties, while closed markets are limited to some group or groups, such as a specific enterprise. For example, Best Buy's Tag Trade is limited to participants from Best Buy, whereas the Hollywood Stock Exchange is open to anyone who registers as a participant. Our concern in this paper is the upper right hand corner; however, we will draw on the literature of studies from the lower left hand corner to determine if similar market characteristics appear in closed prediction markets and examine how those characteristics affect prediction markets as group decision support systems.

<table><tr><td>Predict</td><td>Hollywood Stock Exchange</td><td>Best Buy&#x27;s Tag Trade</td></tr><tr><td>Invest</td><td>New York Stock Exchange</td><td>Corporate Investments</td></tr><tr><td></td><td>Open</td><td>Closed</td></tr></table>

Fig. 1. Typology of market types.

## 2.2. Investment market effects

Over the years, there has been substantial research on different investment markets finding that there are a number of characteristics in those markets. For example, researchers have found “day-of-the-week effects” and “month effects” as part of trading on the New York Stock Exchange and other exchanges (e.g., Gibbons and Hess [19]). In addition, researchers have found monthly effects on trading. For example, there is what is called a “January Effect.” Although these market characteristics have been explored in traditional open investment markets, there has been limited analysis of such effects in closed corporate prediction markets.

## 2.3. Corporate prediction markets: Some previous research

Corporate prediction markets are internal markets used by corporations or other organizations to gather knowledge from a broad base of employees in a setting where employees, using internal currency (“play money,” e.g., “Gobbles” at Google) to bid (bet) on the outcomes captured in markets designed to address decision making issues. For example, a market might involve employees bidding on two stocks, where one stock is that the project finishes by a specific due date, while the other is that the project finishes after that due date.

In this setting, estimates of the probability that the market attributes to the event would be reflected in the price of the two stocks. Classic uses of prediction markets have been done for those settings where there ultimately is a “correct” answer, e.g., the project either was or was not done on time or certain revenue forecasts were or were not met. In addition, markets can be used for those settings where there is no a priori gold standard, for example, there can be a market about the best location for a new office.

Berg and Reitz [4] analyzed prediction markets as decision support systems, examining how decisions can be supported by information derived from prediction markets. Information about the event is impounded in the price and provides insight into the event for a decision maker.

One of the primary concerns to date has been the quality of the predictions from corporate prediction markets. For example, Wolfers and Zitzewitz [43] provide a survey of different uses of prediction markets and a review of some key factors associated with prediction in generic prediction markets. Berg et al. [5] and others have investigated the accuracy of prediction markets, while Manski [28] examined the issue of interpreting the “predictions of prediction markets.”

There are a number of reasons to believe that prediction markets as used in an enterprise or other organization are “different” than either open investment markets, such as the New York Stock Exchange, or even open prediction markets, e.g., Hollywood Stock Exchange. As an example, firms do not necessarily want the outcomes of the markets to be known by all (not leaking corporate inside information). As another example, Wolfers and Zitzewitz [44] analyzed what they referred to as five questions that they felt were important to getting markets into corporate settings. In particular, they were concerned about attracting traders to the markets, market manipulation, and other issues associated such potentially small markets.

Researchers also have raised a number of other issues uniquely related to corporate internal prediction markets. Generally, corporate prediction markets do not use real dollars, but instead use “play” currencies such as H\$ (Hollywood dollars) or Google's Goobles. Typically, firms reward traders with publicity, such as listing the “top ten traders” or “prizes” for finishing as a top trader. Although there may be limited payoff associated with particular markets, the outcome of markets can have substantial influence in the real world. For example, it has been suggested that prediction markets become “self-fulfilling prophesies” (e.g., see [32] for a summary of some research). If so then a late project can mean the end of a career of a project manager. As a result, with corporate prediction markets, the direct market payoffs to participants are frequently much less than the outcome consequences of the market. Accordingly, we might anticipate potential market responses by those directly affected by the outcome of the market or by those with an axe to grind against those same organization members. Thus, there are important differences between corporate prediction markets and open prediction markets.

## 2.4. Research based on real world corporate prediction markets

Although there are a number of potential differences between open markets and closed corporate prediction markets, there has been limited research in corporate settings where corporate prediction models actually have been implemented. As an example of that limited research, an analysis of the literature covered in a 2014 review of the prediction markets literature (Horn et al. [23]) yields eight papers that address “corporate prediction markets.” Of those papers, some corporate prediction market academic researchers (e.g., Ottavani and Sorenson [34], Reig and Schoder [35], and O'Leary [33]), have analyzed how corporate prediction markets differ from other prediction markets. Another line of corporate prediction market research comes from researchers that have suggested uses for prediction markets. Abramowicz and Henderson [1] have recommended corporate prediction markets for use in corporate governance, while Waitz and Mild [45] have suggested that corporate prediction markets could be used for predicting corporate or product market shares.

The primary methodology for empirical research in the area has been in the form of data generated from particular firms. Unfortunately, those case studies are limited. Cowgill et al. [13] documented a number of biases in Google's markets, for example, noting that newly hired employees are on the optimistic side of the markets. In addition, they found correlated trading by people physically proximate to each other. Waitz and Mild [45] developed a case study about an Austrian mobile communication firm. In a more recent study, Cowgill and Zitzewitz [14] analyzed case data from three companies: Google, Ford and Koch Industries. This current study extends that tradition of empirical analysis of data generated at companies, by analyzing data generated at Best Buy.

## 3. Best Buy's “Tag Trade” and the data

The data investigated in this paper were provided by Best Buy (Keller [26]). Best Buy is used for a number of reasons. First, Best Buy has pursued a range of emerging technologies to improve information flow and decision making. For example, as noted by Dvorak [17], “Best Buy's chief executive…encourages experiments…that seek to drive decision making down the corporate ladder and information up toward the top.” Second, Best Buy has used prediction markets, generating usage data among their corporate and retail employees as a consequence of their implementation. Third, Best Buy is a well-known firm with a large number of retail and corporate employees. Those two groups of employees allow us to compare and contrast their participation in the prediction market, unlike previous studies. Fourth, previous case studies have focused on firms such as Google (e.g., Cowgill et al. [13] and Coles et al. [11]). This research expands the set to include a retail firm.

## 3.1. Background on Best Buy<sup>1</sup>

Headquartered in Richfield, Minnesota, Best Buy is a large retailer with stores located in the United States, Canada, and China. Although Best Buy has had operations in the United Kingdom and Europe, those investments have been closed or sold.

Best Buy operates as a physical retailer and through e-commerce. Best Buy offers a wide range of consumer products, typically related to technology, including audio, video, phones, and computers. Best Buy is extremely price competitive. For example, over the Christmas holidays in the United States in 2014, Best Buy used strategy of a low price guarantee. Best Buy allows trade in of electronics and has a strong credit card presence.

Best Buy also is famous for their “Geek Squad,”<sup>2</sup> that allows buyers to ask questions about their technology purchases. For example, the Geek Squad can help computer owners remove viruses and other concerns. As a result, Best Buy is not just known for the sale of technology and entertainment-based equipment, but also for their subsequent service of that equipment.

## 3.2. Best Buy's Use of Prediction Markets (Dvorak [17])

Best Buy has used an internal prediction market referred to internally as “Tag Trade” that allowed Best Buy's 115,000 employees to participate in the prediction markets. As many as 2100 of them have chosen to be a part of the prediction markets. Traders were given one million dollars of an internal currency to trade on any of the available stocks. Based on the total market value of their portfolio at the end of the trading period, the top trader for some time period would be given a \$200 gift certificate. As noted by Keller [26], at Best Buy, reportedly, in some cases, the prediction markets have been more accurate than some official forecasts. In one case, prediction markets were 99.4% accurate 4 months prior to a holiday prediction.

## 3.3. Data

The data in this study were generated by Best Buy as part of a pilot study. There were two groups of participants: corporate and retail. Retail included store, district, and regional management from a sales district in the upper Midwestern United States. Corporate traders were drawn from the corporate office. Although there were 196 registered traders, with 97 from corporate and 99 from retail, in this study there were 159 total traders participating, with 79 from corporate, and 80 from retail. Not all registered traders participated in the pilot.

In the data presented in this paper, Best Buy captured the unique number of traders both by day/date and by market, for the two different groups of employees. The information about the number of unique traders is summarized in Tables 1 and 2. Data covered 8 weeks over a 56 day time period May to June. The pilot started in May and ended in June.

The meaning of some of the market abbreviations in Table 2 is summarized in Table 3. As part of the Best Buy prediction market, those two sets of traders had access to a number of stocks covering three basic types of events: “Corporate,” “Retail,” and “Fun.” Corporate markets referred to general company-wide events. Retail markets were topics specific to the particular sales district, “Territory 4.” Fun markets drew from the world around Best Buy to include markets about NASCAR, Pirates of the Caribbean, and other non-business topics.

Table 1  
Number of unique traders by day by corporate/retail (8 weeks of data).

<table><tr><td>Number</td><td>Date</td><td>Retail</td><td>Corporate</td></tr><tr><td>1</td><td>6-May</td><td>6</td><td>6</td></tr><tr><td>2</td><td>7-May</td><td>24</td><td>42</td></tr><tr><td>3</td><td>8-May</td><td>36</td><td>28</td></tr><tr><td>4</td><td>9-May</td><td>46</td><td>42</td></tr><tr><td>5</td><td>10-May</td><td>29</td><td>29</td></tr><tr><td>6</td><td>11-May</td><td>31</td><td>26</td></tr><tr><td>7</td><td>12-May</td><td>10</td><td>5</td></tr><tr><td>8</td><td>13-May</td><td>9</td><td>8</td></tr><tr><td>9</td><td>14-May</td><td>24</td><td>24</td></tr><tr><td>10</td><td>15-May</td><td>18</td><td>20</td></tr><tr><td>11</td><td>16-May</td><td>23</td><td>25</td></tr><tr><td>12</td><td>17-May</td><td>18</td><td>19</td></tr><tr><td>13</td><td>18-May</td><td>9</td><td>18</td></tr><tr><td>14</td><td>19-May</td><td>8</td><td>2</td></tr><tr><td>15</td><td>20-May</td><td>4</td><td>3</td></tr><tr><td>16</td><td>21-May</td><td>16</td><td>27</td></tr><tr><td>17</td><td>22-May</td><td>8</td><td>20</td></tr><tr><td>18</td><td>23-May</td><td>18</td><td>21</td></tr><tr><td>19</td><td>24-May</td><td>13</td><td>21</td></tr><tr><td>20</td><td>25-May</td><td>9</td><td>22</td></tr><tr><td>21</td><td>26-May</td><td>4</td><td>4</td></tr><tr><td>22</td><td>27-May</td><td>4</td><td>3</td></tr><tr><td>23</td><td>28-May</td><td>1</td><td>4</td></tr><tr><td>24</td><td>29-May</td><td>8</td><td>26</td></tr><tr><td>25</td><td>30-May</td><td>11</td><td>17</td></tr><tr><td>26</td><td>31-May</td><td>10</td><td>13</td></tr><tr><td>27</td><td>1-Jun</td><td>10</td><td>16</td></tr><tr><td>28</td><td>2-Jun</td><td>4</td><td>2</td></tr><tr><td>29</td><td>3-Jun</td><td>1</td><td>5</td></tr><tr><td>30</td><td>4-Jun</td><td>7</td><td>11</td></tr><tr><td>31</td><td>5-Jun</td><td>4</td><td>13</td></tr><tr><td>32</td><td>6-Jun</td><td>7</td><td>13</td></tr><tr><td>33</td><td>7-Jun</td><td>8</td><td>19</td></tr><tr><td>34</td><td>8-Jun</td><td>4</td><td>13</td></tr><tr><td>35</td><td>9-Jun</td><td>3</td><td>3</td></tr><tr><td>36</td><td>10-Jun</td><td>1</td><td>2</td></tr><tr><td>37</td><td>11-Jun</td><td>6</td><td>15</td></tr><tr><td>38</td><td>12-Jun</td><td>3</td><td>10</td></tr><tr><td>39</td><td>13-Jun</td><td>9</td><td>23</td></tr><tr><td>40</td><td>14-Jun</td><td>4</td><td>14</td></tr><tr><td>41</td><td>15-Jun</td><td>8</td><td>14</td></tr><tr><td>42</td><td>16-Jun</td><td>8</td><td>5</td></tr><tr><td>43</td><td>17-Jun</td><td>5</td><td>5</td></tr><tr><td>44</td><td>18-Jun</td><td>3</td><td>13</td></tr><tr><td>45</td><td>19-Jun</td><td>2</td><td>16</td></tr><tr><td>46</td><td>20-Jun</td><td>0</td><td>12</td></tr><tr><td>47</td><td>21-Jun</td><td>4</td><td>9</td></tr><tr><td>48</td><td>22-Jun</td><td>3</td><td>10</td></tr><tr><td>49</td><td>23-Jun</td><td>2</td><td>0</td></tr><tr><td>50</td><td>24-Jun</td><td>2</td><td>2</td></tr><tr><td>51</td><td>25-Jun</td><td>3</td><td>20</td></tr><tr><td>52</td><td>26-Jun</td><td>2</td><td>8</td></tr><tr><td>53</td><td>27-Jun</td><td>1</td><td>11</td></tr><tr><td>54</td><td>28-Jun</td><td>6</td><td>16</td></tr><tr><td>55</td><td>29-Jun</td><td>7</td><td>16</td></tr><tr><td>56</td><td>30-Jun</td><td>2</td><td>3</td></tr></table>

Source: Keller [26].

The data used in this study are “researcher neutral,” in that Best Buy developed the data independent of the researcher, for their own uses. This has at least four implications. First, we take the data as an indicator of the firm's interest in the activities described by the data; otherwise, they would not have developed it and analyzed it. Second, such internal data are not usually made available to researchers. As a result, these data provide a relatively unique opportunity to glimpse the use of Best Buy's prediction market system. Third, since the data are developed by a firm about their own internal system it has substantial external validity. Best Buy thought it was important enough information to collect. Further, the data provide “real” performance information. Fourth, the data “is what it is,” in that there is no going back to get additional data or different data: the data consist of information about the participation of the number of unique traders along two key dimensions for both retail and corporate: time and market.

Table 2  
Number of unique traders by market and type.

<table><tr><td>Market</td><td>Total</td><td>Retail</td><td>Corporate</td><td>Type</td></tr><tr><td>Attach</td><td>89</td><td>44</td><td>45</td><td>1</td></tr><tr><td>CSI.May</td><td>76</td><td>35</td><td>41</td><td>1</td></tr><tr><td>IPODChoc</td><td>73</td><td>43</td><td>30</td><td>1</td></tr><tr><td>DI.Mom</td><td>69</td><td>42</td><td>27</td><td>1</td></tr><tr><td>RZMCJune</td><td>58</td><td>24</td><td>34</td><td>1</td></tr><tr><td>Fort.100</td><td>46</td><td>17</td><td>29</td><td>1</td></tr><tr><td>CD.Tues</td><td>45</td><td>23</td><td>22</td><td>1</td></tr><tr><td>Twst.Jun</td><td>42</td><td>15</td><td>27</td><td>1</td></tr><tr><td>Twst.08</td><td>41</td><td>18</td><td>23</td><td>1</td></tr><tr><td>May.ese</td><td>39</td><td>19</td><td>20</td><td>1</td></tr><tr><td>PDVD.Ju</td><td>39</td><td>15</td><td>24</td><td>1</td></tr><tr><td>PDVD.08</td><td>36</td><td>16</td><td>20</td><td>1</td></tr><tr><td>QA.Apple</td><td>35</td><td>12</td><td>23</td><td>1</td></tr><tr><td>HDA.HTI</td><td>31</td><td>18</td><td>13</td><td>1</td></tr><tr><td>DBS.New</td><td>30</td><td>15</td><td>15</td><td>1</td></tr><tr><td>PC.Setup</td><td>30</td><td>11</td><td>19</td><td>1</td></tr><tr><td>HAD.DBS</td><td>26</td><td>13</td><td>13</td><td>1</td></tr><tr><td>QA.Dell</td><td>25</td><td>11</td><td>14</td><td>1</td></tr><tr><td>GIFTCARD</td><td>22</td><td>11</td><td>11</td><td>1</td></tr><tr><td>DBS.PUGR</td><td>20</td><td>15</td><td>5</td><td>1</td></tr><tr><td>CD.Kelly</td><td>16</td><td>4</td><td>12</td><td>1</td></tr><tr><td>BSN.COM</td><td>15</td><td>6</td><td>9</td><td>1</td></tr><tr><td>IPHONEU</td><td>12</td><td>5</td><td>7</td><td>1</td></tr><tr><td>IPHONE.E</td><td>9</td><td>3</td><td>6</td><td>1</td></tr><tr><td>AI.Jordi</td><td>76</td><td>36</td><td>40</td><td>2</td></tr><tr><td>AI.Blake</td><td>73</td><td>32</td><td>41</td><td>2</td></tr><tr><td>Nascar</td><td>63</td><td>30</td><td>33</td><td>2</td></tr><tr><td>AI.Melin</td><td>59</td><td>29</td><td>30</td><td>2</td></tr><tr><td>Pirates</td><td>58</td><td>25</td><td>33</td><td>2</td></tr><tr><td>AI.Lakes</td><td>47</td><td>26</td><td>21</td><td>2</td></tr><tr><td>Shrek3</td><td>45</td><td>25</td><td>20</td><td>2</td></tr><tr><td>NBA.Clev</td><td>31</td><td>10</td><td>21</td><td>2</td></tr><tr><td>Soprano</td><td>31</td><td>11</td><td>20</td><td>2</td></tr><tr><td>PGA.PAR</td><td>18</td><td>7</td><td>11</td><td>2</td></tr><tr><td>PGA.TGR</td><td>18</td><td>8</td><td>10</td><td>2</td></tr><tr><td>PGA.PHIL</td><td>16</td><td>5</td><td>11</td><td>2</td></tr><tr><td>Rev.May</td><td>84</td><td>46</td><td>38</td><td>3</td></tr><tr><td>T4CSIMay</td><td>81</td><td>49</td><td>32</td><td>3</td></tr><tr><td>T4Labor</td><td>74</td><td>37</td><td>37</td><td>3</td></tr><tr><td>GMP.May</td><td>57</td><td>36</td><td>21</td><td>3</td></tr><tr><td>T4Memda</td><td>29</td><td>18</td><td>11</td><td>3</td></tr><tr><td>T4COMPJU</td><td>17</td><td>5</td><td>12</td><td>3</td></tr><tr><td>T4COMP08</td><td>12</td><td>3</td><td>9</td><td>3</td></tr><tr><td>T4SVCJUN</td><td>7</td><td>5</td><td>2</td><td>3</td></tr><tr><td>T4SVC08</td><td>3</td><td>2</td><td>1</td><td>3</td></tr></table>

Type 1 = Corporate, Type 2 = Fun, Type 3 = Retail.  
Source Keller [26].

## Table 3

Sample market names and detail.

<table><tr><td>Market Name</td><td>Detail on market</td></tr><tr><td>Attach</td><td>Geek squad attach rate hits 32% in May</td></tr><tr><td>CSI</td><td>National CSI index score hits 79 in May</td></tr><tr><td>DBS.New</td><td>DirecTV subs June % that are NEW subs (Scale)</td></tr><tr><td>DBS.Upgr</td><td>DirecTV subs June % that are NEW subs (Scale)</td></tr><tr><td>GMP.May</td><td>(T4) POS margin % May</td></tr><tr><td>HDA.DBS</td><td>DirecTV attach rate June (Scale)</td></tr><tr><td>HAD.HTI</td><td>HT install attach rate June (Scale)</td></tr><tr><td>May.Ese</td><td>Revenue from May exclusive sales event coupons (Scale)</td></tr><tr><td>Pirates</td><td>Pirates 3: Bigger opening weekend than Spider-Man 3?</td></tr><tr><td>Rev.May</td><td>(T4) POS sales hits or exceeds May budget</td></tr><tr><td>RZMCJune</td><td>RMZC enrollments &gt; 50,000 in June</td></tr><tr><td>T4CSIMay</td><td>(T4) CSI index score: May &gt;= 79%</td></tr><tr><td>T4Labor</td><td>(T4) Labor expense as % of budget – May (Scale)</td></tr><tr><td>T4Memday</td><td>(T4) Memorial day weekend POS revenue (Scale)</td></tr></table>

## 3.4. Importance of “number of unique traders”

The number of unique traders is a critical component of markets. First, the number of unique traders is particularly useful for the issues examined in this paper that relate specifically to participation in markets and the ability of markets to garner information based on that participation. For example, this paper examines a range of market participation characteristics, such as day-of-the-week effects that can influence the amount and timeliness of the information brought to the market, influencing the ability of the market to serve as a decision support system. Second, if there are more traders rather than fewer traders, market prices become more informative because the price is averaging more predictions (Grossman and Stiglitz [20]). Third, the number of unique traders is important since without participation by traders there are no markets. As seen below, this issue is an important concern in the data examined here.

Fourth, the number of unique traders is correlated with other market variables as seen in the following examples. The number of unique traders and has long been treated as related to the trading volume and prices in both theoretical and empirical work (e.g., Clark [10], Tauchen and Pitts [42] and others). For example, Tauchen and Pitts ([42], p. 487) suggest that “…the mean trading volume increases linearly with the number of traders.” The number of unique traders also is related to the liquidity in the market, particularly in prediction markets, since each trader starts with the same portfolio dollar value.

Finally, other researchers such as Gutierrez and Kelley ([21], p. 6) suggest that the signal-inference motive associated with the number of traders would result in a “weight” more than the actual volume traded. Accordingly, the number of unique traders provides important information with insight into market activity.

## 4. Expectations

The available data used here trace the number of unique traders over time and in the different markets for both retail and corporate. These data allow us to investigate a number of emerging issues in corporate prediction markets. The purpose of this section is to lay out the expectations regarding those issues, based on theory developed in finance for behavior in external markets.

## 4.1. Trader use of information in prediction markets

Financial theory (e.g., Easley et al. [18]) suggests that in external investment markets, traders trade on information available to them. In a corporate prediction market, firms typically hope that market participants trade on information so that information becomes embedded in the price (e.g., Cherry and Rogers [8]). For example, Lohr [27] suggests that corporate prediction traders will “…bet on what they think will actually happen, not what they hope will happen or what the boss wants.” Other researchers also have indicated that “…employees will often trade on information…” (Abramowicz and Henderson [1], p. 19). As a result, it is not surprising that in one case study, one trader in Coles et al. (11, p. 12) noted “The one time I thought I had good information…I traded like crazy on it.”

Ultimately, the success of the markets can depend on whether traders trade on information. In the case of Best Buy, Keller ([26], p. 27) noted at least three different potential information-based approaches to trading<sup>3</sup>:

• 51% “I traded on stocks based on insights I already had (I work on the team, etc.)”

• 46% “I did minimal research on the stocks (read prospectus, checked out some web sites, etc.)”

• 10% “I did extensive research”

However, alternative trading strategies have been proposed for corporate prediction markets that do not depend on information about the particular prediction. For example, as noted in Coles et al. [11], one trader said that their strategy was to bet on “negative outcomes”, e.g., a project being late. As another example in that same case, a different trader suggested that he tried to make trades that “misled” the market.

In any case, if traders trade on information, then the number of unique traders in a market is likely to reflect the extent to which information is diffused to different groups of potential market participants. As a result, at Best Buy, if “corporate” traders have unique access to information, they would be able to uniquely trade on that corporate information, while “retail” would not or if retail had unique information, they would be able to trade on that retail information, while corporate would not. This results in the following hypothesis:

Hypothesis 1. The mean number of unique corporate (retail) traders trading in corporate (retail) markets is greater than the mean number of corporate (retail) traders trading in retail (corporate) markets.

## 4.2. Day-of-the-week effect

Researchers in investment markets, such as the New York Stock Exchange, have found that there is a “day-of-the-week effect” (for example, Gibbons and Hess [19]). As an example, in a survey of the literature, Berument and Kiymaz [6] discussed a number of such effects, e.g., the “Tuesday Effect” and the “week-end” effect (Jaffe and Westerfield [25]). In addition, as noted in Jaffe and Westerfield ([25], p. 445), there are “Wednesday Effects” and a “Friday Effect.”

However, it is not clear if corporate prediction markets have such effects. Markets such as the New York Stock Exchange literally are not open on each day of the week (not on Saturday or Sunday), but corporate prediction markets can be. Further, in investment markets, participants have real money on the table, dependent on their actions, but in prediction markets, participants have limited actual assets in the market. In addition, asset markets exchange real dollars, with contract constraints associated with when payments are due, in contrast to the exchange of (play) prediction market dollars.

On the other hand, there are reasons to expect “uneven” participation by users in closed corporate prediction markets. Recently, Brooks [7] noted that Monday and Tuesday are the two most productive days of the week. If that is so, then perhaps prediction market users would find more time to participate in prediction markets on those days. However, in contrast, perhaps if workers are to be productive in their “real” work on Monday and Tuesday, then they might not have time to participate in the prediction markets on those days. Further, workers participating in corporate prediction markets have other responsibilities than the market, both in their personal and corporate lives. Workers may save personal errands for the week-end, leave work early on Friday; they may go to church on Sunday, or any of a number of other activities that influence the level of their activity in voluntary corporate prediction markets. As a result of these personal and workload requirements, we probably would expect that Saturday and Sunday would receive the fewest unique number of traders. However, there are competing theories as to which of the days Monday–Friday would have the highest number of unique traders.

Accordingly, this research also investigated the potential for a day-of-the-week effect in these corporate prediction market trader data. As a result, we have the following null hypothesis for each of retail and corporate traders:

Hypothesis 2. The mean number of unique traders is the same for each day of the week.

In addition, the above discussion suggests that Saturday and Sunday will have less participation than the other days of the week, resulting in the following hypothesis:

Hypothesis 2-A. The mean number of unique traders on Saturday and Sunday is less than the mean number of traders the other days of the week.

## 4.3. Month effect

Researchers in finance have found that although investment stock markets, such as the New York Stock Exchange, are open all year long, there are still monthly effects (e.g., Jaffe and Westerfield [25]). However, corporate prediction markets may be open for only a quarter (e.g., Google) or other periods of time. As a result, it is not clear if there will be a month effect with internal prediction markets. However, there are rationales that suggest that different months may result in differential trading. For example,

• In the first month a market is open, users could be interested or curious about this new and emerging tool or technology.

• In the second month, they may have seen the market work and they may have made observations about the markets that will lead to moderating their participation. For example, observers might notice that traders with inside information are likely to be “winners” in the markets because they can leverage that information. Accordingly, without such inside information, there may be little reason to participate.

• As time goes on, participants may become less or more interested.

In addition, there are a number of other potential causes of monthly effects related to normal family activities. For example, June is typically the start of summer vacations. As a result, we might see greater participation in May, and less in June.

However, an alternative explanation is that information shocks potentially come randomly to the markets. With random information shocks and traders acting on those shocks, we would expect there to be no difference in the number of traders between subsequent months. Finally, the actual “mechanical configuration” of the markets (whether done well or not done well) may influence the extent to which the markets facilitate capturing and embedding new information to be traded on.

Accordingly, we have the following null hypothesis for retail and corporate traders:

Hypothesis 3. The mean daily number of unique traders in months one and two is the same.

## 4.4. Beginning of month compared to end of month

Researchers in financial markets (e.g., Ariel [2] and others) also have found that markets behave differently in the first half of the month compared to the second half of the month (Ariel [2], p. 2). Accordingly, if the prediction market's behavior follows the same route as the investment market, we would expect differential activity in the first half of the month compared to the second half. As a result, this leads to the following null hypothesis for retail and corporate traders:

Hypothesis 4. The mean daily number of unique traders in the first half of the month is the same as the mean daily number of unique traders for the second half of the month for both trading months.

Table 4

## 4.5. Participation of traders over time

Researchers in financial markets have noted that the number of participants in investment markets, such as the New York Stock Exchange, have increased over time. However, in the case of prediction markets, the relationship between the number of traders and time is not clear, a priori.

In the case of prediction markets, new information and new stocks may be made available over time and draw in traders. This is critical since if prediction markets are to be used over time, personnel need to continue to participate in order to continue to provide information to the company. Unfortunately, since prediction markets do not typically provide actual compensation for participation, there is some question as to whether or not participation will be sustained over time. Further, real world discussions about corporate prediction markets suggest that participants seem interested to join in markets initially; however, there is some evidence that the number of traders may decrease over time (e.g., Keller [26]). In addition, commentators on prediction markets (e.g., Davenport [15]) have noted the difficulty of gathering participants to begin with.

In any case, we have the following null hypothesis for retail and corporate traders:

Hypothesis 5. The number of unique daily traders is not related to time.

## 5. Findings

Analysis of the Best Buy data led to a number of findings related to traders trading on information, a day-of-the-week effect, a first-halfof-the-month effect, a month effect, and in the mean number of traders in the corporate prediction market over time.

## 5.1. Trader approaches: Do traders trade on information?

If prediction market traders trade on unique information, then we would expect that there would be more unique corporate (retail) traders trading on corporate (retail) stocks rather than on retail (corporate) stocks. There is some support in Table 4, panel A, where for corporate (retail), the average number of unique traders is larger for corporate (retail) than retail (corporate) markets. Unfortunately, there is not a statistically significant difference between mean numbers of traders in the particular markets (corporate and retail) when the entire sample is considered together.<sup>4</sup>

However, at one point in Keller [26], the stocks were broken into two categories, based on the median number of total unique traders per stock. Accordingly, in this research, the stocks were divided into those same two categories (most unique traders and least unique traders) to investigate this issue. For this partition of the stocks into two sets of 22 and 23 stocks, the findings conformed in part to expectations regarding trading on information (Table 4, panels B and C). In particular, for the 22 stocks above the median, the mean numbers of retail traders in corporate (26.82) and retail (42.00) stocks were statistically significantly different, and for those retail traders, the larger number was in retail stocks as would be expected. Further, the total average number of unique traders in corporate markets (56.09) was statistically significantly different than the average number of unique traders in retail markets (74.00).

Similarly, in panel C for the 23 stocks at the median and below, the total average number of unique traders in corporate markets (23.62) is significantly different than the total average number of traders in retail markets (13.60). For the 23 stocks with the least numbers of unique traders (at the median and below), the mean numbers of corporate traders in corporate (12.85) and retail (7.00) stocks were statistically significantly different; and for those corporate traders, the larger number of traders were in corporate stocks.

Mean and standard deviation for unique traders by market type.  
Panel A: Mean number of unique traders for all stocks by retail and corporate traders.

<table><tr><td colspan="2"></td><td>Total</td><td>Retail</td><td>Corporate</td><td>Sample</td></tr><tr><td rowspan="3">Mean</td><td>(Corporate)</td><td>38.50</td><td>18.13</td><td>20.38</td><td>24</td></tr><tr><td>(Fun)</td><td>44.58</td><td>20.33</td><td>24.25</td><td>12</td></tr><tr><td>(Retail)</td><td>40.44</td><td>22.33</td><td>18.11</td><td>9</td></tr><tr><td rowspan="3">Std dev</td><td>(Corporate)</td><td>*21.24</td><td>**11.81</td><td>10.62</td><td>24</td></tr><tr><td>(Fun)</td><td>21.59</td><td>11.21</td><td>10.98</td><td>12</td></tr><tr><td>(Retail)</td><td>*33.45</td><td>**19.62</td><td>14.48</td><td>9</td></tr></table>

\*For “Total,” an F-test finds that the two are different at better than .0422 on a one-tail test.  
\*\*For “Retail,” an F-test finds that the two are different at better than .0271 on a one-tail test.

Panel B: Mean number of unique traders for stocks with most unique traders (above median)

<table><tr><td colspan="2"></td><td>Total</td><td>Retail</td><td>Corporate</td><td>Sample</td></tr><tr><td rowspan="3">Mean</td><td>(Corporate)</td><td>*56.09</td><td>**26.82</td><td>29.27</td><td>11</td></tr><tr><td>(Fun)</td><td>60.14</td><td>29.00</td><td>31.14</td><td>7</td></tr><tr><td>(Retail)</td><td>*74.00</td><td>**42.00</td><td>32.00</td><td>4</td></tr><tr><td rowspan="3">Std Dev</td><td>(Corporate)</td><td>17.81</td><td>11.80</td><td>7.90</td><td>11</td></tr><tr><td>(Fun)</td><td>10.39</td><td>2.93</td><td>7.99</td><td>7</td></tr><tr><td>(Retail)</td><td>12.08</td><td>6.48</td><td>7.79</td><td>4</td></tr></table>

\* For “Total." the two means are different than each other at better than 0288 on a one-tail t-test.  
\*\*For “Retail”, the two means are different than each other at better than .00512 on a one-tail t-test and at better than .025 on a Mann–Whitney one-tail test.

Panel C: Mean number of unique traders for stocks with least unique traders (median and below).

<table><tr><td colspan="2"></td><td>Total</td><td>Retail</td><td>Corporate</td><td>Sample</td></tr><tr><td rowspan="3">Mean</td><td>(Corporate)</td><td>*23.62</td><td>10.77</td><td>**12.85</td><td>13</td></tr><tr><td>(Fun)</td><td>22.80</td><td>8.20</td><td>14.60</td><td>5</td></tr><tr><td>(Retail)</td><td>*13.60</td><td>6.60</td><td>**7.00</td><td>5</td></tr><tr><td rowspan="3">Std dev</td><td>(Corporate)</td><td>8.77</td><td>4.87</td><td>5.47</td><td>13</td></tr><tr><td>(Fun)</td><td>7.53</td><td>2.39</td><td>5.41</td><td>5</td></tr><tr><td>(Retail)</td><td>10.09</td><td>6.50</td><td>5.14</td><td>5</td></tr></table>

\*For “Total,” the two means are different than each other at better than .0493 on a one-tail t-test and .0344 on a Mann–Whitney one-tail test.  
\*\*For “Corporate,” the two means are different than each other at better than .03343 on a one-tail t-test and .0344 on a Mann–Whitney, one tail test.

Accordingly, after partitioning the data, one explanation for these findings is that traders appear to trade on information: they participate in the markets that they know better. Since participants have limited time they likely will focus on the markets with which they are most familiar: corporate participants on corporate markets, and retail participants on retail markets. As a result, the markets likely are getting the more informed market participants. As a result, there is some evidence to substantiate hypothesis 1.

## 5.2. Is there a day-of-the-week effect?

In order to test the existence of a day-of-the-week effect, two different approaches were used to test the data sets. First, the average number of unique traders for both retail and corporate was computed for each day of the week. Then that set of actual daily averages was compared against the expected average per day, based on the sum of the averages, using a chi-squared approach. The chi-square is a very robust approach for this type of application (e.g., Moore [30] and McHugh [29]). Second, an analysis of variance (ANOVA) was used to test if there was a day-of-the-week effect in the trader data. In that ANOVA, the 8 weeks of data were placed in a 7 × 8 table, capturing day of week by week. ANOVA also is a very robust approach for this type of application (e.g., Sullivan [40]).

Table 5  
Day-of-the-week effect (days labeled 1,2,…, 7).

<table><tr><td colspan="7">Panel A: Data–Chi-square approach–average number of unique traders per day</td></tr><tr><td>Day of week</td><td></td><td colspan="3">Average retail</td><td colspan="2">Average corporate</td></tr><tr><td>1–Sunday</td><td></td><td colspan="3">4.000</td><td colspan="2">4.250</td></tr><tr><td>2–Monday</td><td></td><td colspan="3">10.500</td><td colspan="2">19.500</td></tr><tr><td>3–Tuesday</td><td></td><td colspan="3">10.125</td><td colspan="2">17.625</td></tr><tr><td>4–Wednesday</td><td></td><td colspan="3">14.375</td><td colspan="2">20.500</td></tr><tr><td>5–Thursday</td><td></td><td colspan="3">11.500</td><td colspan="2">17.500</td></tr><tr><td>6–Friday</td><td></td><td colspan="3">10.125</td><td colspan="2">16.875</td></tr><tr><td>7–Saturday</td><td></td><td colspan="3">5.125</td><td colspan="2">3.000</td></tr><tr><td colspan="7">Panel B: ANOVA–using daily data–retail</td></tr><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>630.8571</td><td>6</td><td>105.1429</td><td>1.190801</td><td>0.326885</td><td>2.290432</td></tr><tr><td>Within groups</td><td>4326.5</td><td>49</td><td>88.29592</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>4957.357</td><td>55</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7">Panel C: ANOVA–using daily data–corporate</td></tr><tr><td>Source of variation</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>P-value</td><td>F crit</td></tr><tr><td>Between groups</td><td>2575.964</td><td>6</td><td>429.3274</td><td>8.307648</td><td>3.17E-06</td><td>2.290432</td></tr><tr><td>Within groups</td><td>2532.25</td><td>49</td><td>51.67857</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>5108.214</td><td>55</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7">Panel D: One-tail test probability: Average number of traders Monday–Friday is greater than Saturday/Sunday</td></tr><tr><td></td><td>Monday</td><td>Tuesday</td><td>Wednesday</td><td>Thursday</td><td colspan="2">Friday</td></tr><tr><td>Retail-Sunday</td><td>0.0498</td><td>0.0939</td><td>0.0470</td><td>0.0226</td><td colspan="2">0.0483</td></tr><tr><td>Retail-Saturday</td><td>0.0830</td><td>0.1384</td><td>0.0428</td><td>0.0389</td><td colspan="2">0.0817</td></tr><tr><td>Corporate-Sunday</td><td>0.0042</td><td>0.0005</td><td>0.0011</td><td>0.0001</td><td colspan="2">0.0001</td></tr><tr><td>Corporate-Saturday</td><td>0.0028</td><td>0.0003</td><td>0.0010</td><td>0.0001</td><td colspan="2">0.0000</td></tr></table>

As seen in Table 5, panel A, for retail, the average number of unique traders ranged from 4 to 14.375. For corporate, the average number of unique traders ranged from 4.25 to 20.50. Saturday and Sunday had the fewest unique number of participants, as expected. Wednesday had the highest number of unique participants for both retail and corporate. Using the chi-squared test found that the daily average of the unique corporate traders was statistically significant at a probability of .0009, allowing us to reject the hypothesis that the mean number of traders for each day of the week was the same. However, for retail, the chi-square test found the probability was .2105.

The findings from a single-factor ANOVA are summarized in Table 5 (Panels B and C). Similar to the chi-square test of the averages, it was found that we could not reject hypothesis 2 for the retail data (P-value of .326885), but that the hypothesis could be rejected for the corporate data (P-value of 3.17E-06).

Accordingly, the evidence suggests that we cannot reject the hypothesis that the daily average number of unique traders was the same for retail. One potential explanation for this difference with corporate is that some retail workers work each day of the week, in contrast to corporate workers. Thus, retail workers may have been more willing to trade each day of the week, depending on their schedule. As a result, the daily average could reflect the worker's availability at work.

In order to investigate hypothesis 2-A, the day-of-the-week data were analyzed using a t-test of means with unequal variances (e.g., Ruxton [36]). The results are summarized in Table 5, panel D. In particular, for both the retail and corporate groups, the findings are statistically significant except for a comparison of Retail's Saturday vs. Tuesday. These results suggest that trader participation on Saturday and Sunday are different than the other days of the week.

## 5.3. Is there a first-half-of-the-month effect?

In order to test whether the markets were the same in the first half of the month compared to the second half of the month, the number of unique traders in each month was split into the first and second halves. May data were for 26 days, as a result for May, the data were divided in half: May 6–May 18, and May 19–May 31. For June, the data were divided into two sets of June 1–15 and Jun 16–30. For each data set, the mean number of unique traders was compared using a t-test with unequal variances, a Mann–Whitney, test and an F-test of variances. The statistical results are summarized in Table 6.

Table 6  
First half of month compared to second half of month.

<table><tr><td></td><td>Retail mean</td><td>Corporate mean</td><td>Retail std dev</td><td>Corporate std dev</td></tr><tr><td>May 6–18</td><td>21.769</td><td>22.461</td><td>11.833</td><td>11.836</td></tr><tr><td>May 19–31</td><td>8.769</td><td>14.077</td><td>4.935</td><td>9.604</td></tr><tr><td>June 1–15</td><td>5.27</td><td>11.53</td><td>2.815</td><td>6.198</td></tr><tr><td>June 16–30</td><td>3.33</td><td>9.73</td><td>2.257</td><td>5.909</td></tr><tr><td>One-tail probabilities</td><td>t-test</td><td>t-test</td><td>F-Test</td><td>F-Test</td></tr><tr><td>May</td><td>0.001066</td><td>0.029699</td><td>0.002491</td><td>0.239942</td></tr><tr><td>June</td><td>0.023810</td><td>0.211234</td><td>0.209463</td><td>0.430617</td></tr><tr><td>One-tail probabilities</td><td>Mann-Whitney</td><td>Mann-Whitney</td><td></td><td></td></tr><tr><td>May</td><td>0.0013</td><td>0.0287</td><td></td><td></td></tr><tr><td>June</td><td>0.0244</td><td>0.2207</td><td></td><td></td></tr></table>

The results suggest that the mean numbers of unique traders in the retail group were significantly different in the beginning of the month as compared to the second half for both May and June. However, the results were not as strong for the corporate group. Taken together, there is evidence to reject the third hypothesis that there was no halfmonth effect, particularly for retail in both May and June.

## 5.4. Is there a month effect?

The average number of unique traders for May and June is summarized in Table 7 for both retail and corporate traders. For retail, the decrease was roughly 72%, going from 15.27 in May to 4.30 in June. For corporate traders the decrease was roughly 42%, going from 18.27 in May to 10.63 in June.

In order to test the effect of the month, a t-test of the difference in the means with unequal variances was conducted to determine whether the months of May and June had the same mean. In both cases. the test of the mean allows us to reject the hypothesis that the means are the same. In the case of the retail traders, the t-test results in a probability of 1.72E-05. In the case of the corporate traders, the t-test results in a probability of .002017. In addition, a comparison of May and June using a Mann–Whitney test was statistically significant at better than .0001 for retail traders and at .0044 for corporate traders. Further, the variances of the number of unique traders in corporate and retail were tested using an F-Test for two samples for variances. That test found probabilities of (.000618) and (2.16E-11) for corporate and retail, respectively. Accordingly, considering both the differences in the mean and the variance, there is strong evidence to reject the fourth hypothesis that there was no month effect since both the average and the variance for the number of unique traders for both corporate and retail for May and for June were statistically significantly different.

## Table 7

Monthly effect numbers of unique traders

<table><tr><td></td><td>Retail</td><td>Corporate</td><td></td><td>Retail</td><td>Corporate</td></tr><tr><td></td><td>Mean</td><td>Mean</td><td></td><td>Std dev</td><td>Std dev</td></tr><tr><td>May</td><td>15.27</td><td>18.27</td><td>May</td><td>11.0835</td><td>11.3932</td></tr><tr><td>June</td><td>4.30</td><td>10.63</td><td>June</td><td>2.6929</td><td>6.0200</td></tr><tr><td>% Decrease</td><td>71.84%</td><td>41.82%</td><td></td><td></td><td></td></tr></table>

Table 8  
Regression—Number of retail and corporate traders as a function of time.

<table><tr><td colspan="5">Panel A-Retail</td></tr><tr><td>Linear model</td><td colspan="4">R-square = .469287</td></tr><tr><td>Term</td><td>Estimate</td><td>Std error</td><td>t Ratio</td><td>Prob &gt; |t|</td></tr><tr><td>Intercept</td><td>20.75779</td><td>1.890763</td><td>10.98</td><td>&lt;.0001</td></tr><tr><td>Time</td><td>-0.39877</td><td>0.057708</td><td>-6.91</td><td>&lt;.0001</td></tr><tr><td colspan="5">Panel B-Corporate</td></tr><tr><td>Linear model</td><td colspan="4">R-square = .197927</td></tr><tr><td>Term</td><td>Estimate</td><td>Std error</td><td>t Ratio</td><td>Prob &gt; |t|</td></tr><tr><td>Intercept</td><td>21.67078</td><td>2.359519</td><td>9.18</td><td>&lt;.0001</td></tr><tr><td>Time</td><td>-0.26288</td><td>0.072015</td><td>-3.65</td><td>0.0006</td></tr></table>

## 5.5. Participation of traders over time

The issue of the relationship between trader participation and time was analyzed using a regression analysis and correlation analysis. Each time period was numbered 1, 2,…, 56, and regression models were built using time as an dependent variable and the number of unique retail/corporate traders as the dependent variable. In both retail and corporate models, time had a negative coefficient and was statistically significant. In addition, the unique number of traders was correlated with time. The regression results are summarized in Table 8, panels A and B, and the correlation analysis is summarized in Table 9.

These results suggest that participation by both corporate and retail personnel are negatively related to time. In addition, the results in Tables 7–9, suggest that corporate and retail traders are stopping at different rates, with retail traders disengaging from participation at a faster rate. In any case, as a result, we reject the null hypothesis that the number of traders is not related to time.

## 6. Implications: Business impact of prediction markets

What are the implications of these findings for other corporate prediction market settings?

## 6.1. Trading on information

One interpretation of the analysis of the unique trader data suggests that traders do trade on information: corporate traders will trade on corporate information and retail traders will trade on retail information. However, markets appear to pull in traders from both areas. This could indicate broad information flow about these markets at Best Buy. As a result, this could be an indicator of effective information systems dispersing information broadly, removing information asymmetries. Alternatively, this could be an indicator that market participants are interested in and will participate in a range of markets, despite the existence of informational advantages for traders in their particular market areas (e.g., corporate or retail).

6.2. Impact on practice—Day-of-the-week, beginning-of-the-month, and month effects

The results indicate a day-of-the-week effect, a beginning-of-themonth effect, and a month effect for the number of unique traders for this corporate prediction market, in a manner similar to open financial markets. Clearly, the number of traders can influence the information and attention brought to the market. As a result, day-of-the-week effects, beginning-of-month effects, and month effects can influence the ability to generate decision making information from corporate prediction markets in real-time and over short-time horizons. Accordingly, the data suggest that such effects need to be accounted for in the use of prediction markets for either future prediction or decision support.

Table 9  
Correlations of unique number of traders with time (days).

<table><tr><td></td><td>Retail</td><td>Significance</td><td>Corporate</td><td>Significance</td></tr><tr><td>May &amp; June</td><td>-0.68505</td><td>&lt;0.0000001</td><td>-0.44489</td><td>0.000396</td></tr><tr><td>May</td><td>-0.62355</td><td>0.000333</td><td>-0.37938</td><td>0.027971</td></tr><tr><td>June</td><td>-0.34109</td><td>0.032548</td><td>-0.02700</td><td>Not significant</td></tr></table>

## 6.3. Impact of decreasing participation of traders over time

The decreasing participation by traders, particularly retail, is a disturbing trend. First, if traders continue to abandon the use of markets, there is concern about the long-run viability of markets as an information source. Second, if traders are abandoning the markets, then that means that the market price is becoming a less accurate predictor since the price is averaging fewer predictions (Grossman and Stiglitz [20]).

What are the causes of decreasing participation? There are a number of potential rationales. First, it may be that the markets either have received limited new information that can be traded on. Accordingly, it could be that the ways that the markets are configured limited the ability of traders to leverage new information. Second, if traders are abandoning the markets, then the prediction market experience apparently is not more rewarding than the costs associated with spending the time on the markets. As a result, market designers need to continue to generate approaches that build benefit for market participants.

This also suggests that other corporate settings be investigated to determine if there is a similar decrease in the extent of participation by traders in those markets. Perhaps the “causes” of such deterioration could be further investigated and ultimately mitigated. As additional evidence, there is limited publicly available information that indicates that prediction markets are still being used at Best Buy.

## 7. Summary, extensions, and contributions

The purpose of this final section is to summarize the paper, analyze the contributions, and examine some potential extensions.

## 7.1. Summary

This paper investigated data about the number of unique traders generated from Best Buy's internal corporate prediction market. The analysis of the data found:

• More corporate traders trade in corporate markets and more retail traders trade in retail markets. This suggests that traders leverage their available information

• There are monthly, first-half-of-the-month, and day-of-the-week effects in the average number of unique participants in the markets.

• The number of traders is decreasing over time, and that decrease could threaten the long-term use of such markets and the quality of the estimates in the prices, at least in this particular case.

Although these issues have been examined in large and open financial investment markets, there has been little analysis of them in the context of closed corporate prediction markets. Further, each of these issues can influence the viability of corporate prediction markets and the quality and timeliness of information generated from them. As a result, the existence of these findings is of direct interest to corporations examining corporate prediction markets as an approach to generating an internal group decision support tool.

## 7.2. Extensions

There are a number of potential extensions of the discussions in this paper. First, this paper presents data from a single firm, similar to the previous research in corporate prediction markets. Data from additional rms could be used to determine the extent to which these same effects are found in other settings. Second, one extension of this paper would be to analyze additional actual prediction market data, such as volume and prices, that might be available from Best Buy or integrate that data with this data. Unfortunately, at this time, there appears to be a limited amount of such data. The person who was the source of the data is no longer at Best Buy and there is limited information available about Best Buy's use of prediction markets since that time. Third, other companies might be contacted for additional related information or additional data that could be used to extend this analysis. Ultimately, a central database (repository) of such information could be compiled for various researchers to analyze. Fourth, other prediction markets could be modeled to explore some of the results in this paper. For exam ple, prediction markets in organizations with two (or more) differen groups similar to Best Buy's “corporate” and “retail,” could be developed and used to study the findings from the Best Buy data to determine the similarity of findings. Fifth, investment markets typically have large numbers of participants. However, as seen in this paper, some prediction markets may have a very limited number of traders. Unfortunately, it is not clear how many traders need to be in a market in order for the market to “work” in a corporate setting. In the Best Buy data, the number of unique traders in the markets ranged from 3 to 89. It is probable that 3 is too small (too “thin”) a number of participants. Although any market size greater than 1 has the potential to incorporate such asymmetries and capture information in the price, the smaller number of participants will limit the quality of the traders' forecasts as captured in the price. Sixth, since prediction markets have day-of-the-week effects, etc., it is likely that other forms of crowdsourcing also have similar effects. Future research could examine crowdsourcing and other social media approaches for such effects. Seventh, the analysis above finds a month effect. However. there is insufficient information to know if that effect is a sequence effect (first to second month) or a date effect (May and June). Date effects may vary by country. For example, in many European countries, large portions of the month of July are vacation days for virtually the entire country. Thus, in those settings, there likely would be very limited participation in any such market. Eighth, additional statistical approaches, such as computationally intensive approaches also could be used. Finally, there is a substantial literature that addresses the behavior of open investment markets. As seen in this paper, many of the issues associated with open markets may have comparable findings in prediction markets. Accordingly, future research could examine the extent to which those findings manifest themselves in corporate prediction markets.

## 7.3. “Fast–short markets”

The decreasing participation over time suggests that corporate prediction market participants may not be interested in markets covering periods of time such as a month. Potentially, market participation costs such as information search and monitoring different stocks over long periods of time are more costly than the benefits received. As a result, this research suggests that an important issue is the effect of the length of the market on participation.

In particular, perhaps an alternative approach of “fast–short markets” should be used in contrast to markets stretching across weeks and months. “Fast–short” markets (say 1–5 days) could be used periodically to capture information asymmetries available at the time of the market, rather than trying to embed participant information about emerging information shocks into the price over some longer time period. Such fast–short markets could be used to capture “snap-shots” of events at different times, rather than having the equivalent of a “movie” that continuously traces the probability of some event. This approach would allow participants to leverage their information, without having to continuously monitor related streams of information over time, thus potentially minimizing market participation costs.

## 7.4. Contributions

This paper has a number of contributions. First, this paper presents a study of the human side of corporate prediction markets. In particular, this paper investigated patterns of corporate prediction market use over time. In so doing, this paper facilitates an understanding of how people participate in corporate prediction markets. Second, this paper isolates particular characteristics of use of a corporate prediction market. For example, there appear to be day-of-the-week effects that correspond to participants' work weeks. Third, this paper compares the behavior of two different groups in a corporate prediction market. As a result, we were able to test issues such as participation in market where there were likely to be information asymmetries (e.g., corporate user awareness of corporate issues). Fourth, this paper used multiple statistical approaches, including both parametric and non-parametric approaches (e.g., Mann–Whitney). Throughout, the multiple approaches generated consistent results and substantiate each other. Fifth, corporate prediction markets are a hybrid decision support system: part technology and part markets. This paper used theory generated in open financial markets as a basis of generating the hypotheses. As a result, this research brings theory from economics and finance into decision support systems research and into corporate prediction markets and other social media.

## Acknowledgement

I would like to acknowledge the comments of the anonymous referees on three earlier versions of this paper. Earlier versions were presented at the University of Delaware and Rutgers University.

## References

[1] M. Abramowicz, M.T. Henderson, Prediction markets for corporate governance, Notre Dame Law Review (2007) 1343–1352 (April).

[2] R. Ariel, A monthly effect in stock returns, March 1984, Working paper 1629-84, published in Journal of Financial Economics, Vol 18 No 1, Massachusetts Institute of Technology 1987, pp. 161–174.

[3] H. Berg, Prediction Markets at Microsoft” (Prediction markets Conference, Presentation at the University of Kansas), http://people.ku.edu/\~cigar/PMConf\_2007/ HenryBerg(PredictionPoint%20KC%20071101).pdf 2007.

[4] J. Berg, T. Rietz, Prediction markets as decision support systems, Information Systems Frontiers 5 (1) (January 2003) 79–93.

[5] J.E. Berg, F.D. Nelson, T.A. Rietz, Prediction market accuracy in the long run, International Journal of Forecasting 24 (2) (2008) 285–300.

[6] H. Berument, H. Kiymaz, The day of the week effect on stock market volitility, Journal of Economics and Finance 25 (2) (Summer 2001) 181–193

[7] C. Brooks, The most productive day of the workweek is, http://www. businessnewsdaily.com/5637-the-most-productive-day-of-the-workweek-maysurprise-you.html.

[8] M. Cherry, R. Rogers, Markets for markets: origins and subjects of information markets, Rutgers Law Review Vol 58 (No 2) (2006) 339 (Winter).

[9] M. Chui, A. Miller, R. Roberts, Six Ways to Make Web 2.0 Work, http://www. boulderdowntown.com/\_files/docs/six-ways-to-make-web-2-work.pdf February 2009.

[10] P. Clark, A subordinated stochastic processes model with finite variance for speculative prices, Econometrica 41 (1973) 135–155.

[11] P. Coles, K. Lakhani, A. McAfee, Prediction Markets at Google (Harvard Business School Press). http://stanford2009 wikispaces com/file/view/HBSGooglePMCase pdf March 2007 (N9–607-088)

[12] Consensus Point, Web 2.0 has Arrived and Social Predictive Analytics is Web 2.0”, http://www.consensuspoint.com/prediction-markets-blog/tag/web-2-0 2010.

[13] B. Cowgill, J. Wolfers, E. Zitzewitz, Using Prediction Markets to Track Information Flows: Evidence from Google, http://www.weigend.com/files/teaching/stanford/ 2008/readings/PredictionMarkets%2520CowgillWolfersZitzewitz2008.pdf January 2008.

[14] B. Cowgill, E. Zitzewitz, Corporate Prediction Markets: Evidence from Google, Ford and Koch Industries”, http://www.tinbergen.nl/wp-content/uploads/2013/10/ Zitzewitz\_Oct29.pdf.

[15] T. Davenport, Prediction Markets: Is anybody really predicting? http://blogs.hbr.org/ 2008/04/prediction-markets-is-anybody/ April 17 2008

[16] R. Dye, The Promise of Prediction Markets, McKinsey Quarterly (April 2008) 83–93.

[17] P. Dvorak, Best buy taps prediction market, Wall Street Journal (September 16, 2008) http://www wsicom/articles/SB122152452811139909

[18] D. Easley, M. O'Hara, P. Srinivas, Option volume and stock prices: evidence on wher informed traders trade, The Journal of Finance 53 (2) (1998) 431–465.

[19] M. Gibbons, P. Hess, Day of the week effects and asset returns, The Journal of Business 54 (4) (0ctober 1981) 579–596

[20] S. Grossman, G. Stiglitz, On the impossibility of informationally efficient markets, American Economic Review 70 (1980) 393–408

[21] R. Gutierrez, E. Kelley, Institutional Herding: Destabilizing Buys, Stabilizing Sells, http://www.finance.sauder.ubc.ca/conferences/summer2008/files/ papers/ summer2008\_gutierrez.pdf May 2008.

[22] R. Hanson, Decision markets, IEEE Intelligent Systems (May/June 1999) 16–19.

[23] C. Horn, B. Ivens, M. Ohneberg, A. Brem, Prediction markets: a literature review 2014, The Journal of Prediction Markets 8 (2) (2014) 89–126.

[24] F. Hayek, The use of knowledge in society, The American Economic Review 35 (1945) 519-530

[25] J. Jaffe, R. Westerfield, The week-end effect in common stock returns, The Journal of Finance 40 (2) (1985) 433–454.

[26] Dawn Keller, Tag Trade: Best Buy's Prediction Market (Prediction Markets Conference, Kansas City), http://people.ku.edu/\~cigar/PMConf\_2007/DawnKeller(Prediction% 20Market%20Conference%20110107\_Best%20Buy\_for%20web).pdf November 1, 2007.

[27] S. Lohr, Betting to Improve the Odds”, The New York Times, http://www.nytimes. com/2008/04/09/technology/techspecial/09predict.html?oref=slogin&\_r=0 April 9, 2008.

[28] C. Manski, Interpreting the predictions of prediction markets, Economics Letters 91 (3) (June 2006) 425–429.

[29] M. McHugh, The chi-square test of independence, Biochemia Medica 23 (2) (June, 2013) 143–149.

[30] D. Moore, The Basic Practice of Statistics, W.H. Freeman and Company, 2010.

[31] J. Nocera, The future divined by the crowd, The New York Times (March 11, 2006) C1, C12 (B1).

[32] D.E. O'Leary, Prediction markets as a forecasting tool, Advances in Business Management and Forecasting 8 (2011) 169–184.

[33] D.E. O'Leary, Internal corporate prediction markets: from each according to his bet, International Journal of Accounting Information Systems 14 (2) (2013) 89–103.

[34] M. Ottaviani, P. Sorenson, Outcome manipulation in corporate prediction markets, Journal of the European Economic Association 5 (2–3) (2007) 554–563.

[35] R. Rieg, R. Schroder, Corporate prediction markets: pitfalls and barriers, Foresight: The International Journal of Applied Forecasting (Spring 2007) 35–40.

[36] G. Ruxton, The unequal variance t-test is an underused alternative to Student's t-test and the Mann–Whitney U test, Behavioral Ecology 17 (4) (2006) 688–690.

[37] J. Rydholm, Still Fighting the Good Fight, Quirk's Marketing Research Review (2013) 48–53 (November).

[38] B. Spears, C. LaComb, J. Interrante, J. Barnett, D. Senturk-Dogonaksoy, Examining trader behavior in idea markets: an implementation of GE'S imagination markets, The Journal of Prediction Markets 3 (1) (2009) 17–39.

[39] T. Sprenger, P. Bolster, A. Ventakeswaran, Conditional prediction markets as corporate decision support systems—an experimental comparison with group deliberations, The Journal of Prediction Markets 1 (3) (2007) 189–201.

[40] M. Sullivan, Informed Decisions Using Data, 4th edition Pearson, Addison Wesley, New York 2012

[41] J. Surowiecki, The Wisdom of Crowds, Random House, 2004.

[42] G.E. Tauchen, M. Pitts, The price variability-volume relationship on speculative markets. Econometrica 51 (2) (March 1983) 485–505

[43] J. Wolfers, E. Zitzewitz, Prediction Markets, NBER Working Paper 10504, May, 2004.

[44] J. Wolfers, E. Zitzewitz, Five Open Questions About Prediction Markets, NBER working Paper, January 21, 2005.

[45] M. Waitz, A. Mild, Corporate prediction markets: a tool for predicting market shares, Journal of Business Economics 83.3 (2013) 193–212.

Daniel O'Leary is a professor in the Marshall School of Business at the University of Southern California, focusing on prediction markets, crowdsourcing, innovations, and social media. Dan received his PhD from Case Western Reserve University. He is the former editor of IEEE Intelligent Systems and current editor of John Wiley's Intelligent Systems in Accounting, Finance and Management. His book, Enterprise Resource Planning Systems, published by Cambridge University Press, has been translated into both Chinese and Russian. Much of Professor O'Leary's research has studied emerging technologies and their use in business settings.
