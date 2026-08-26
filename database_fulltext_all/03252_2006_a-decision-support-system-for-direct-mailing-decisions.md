---
otero_id: 3252
otero_key: "WQA23PMW"
title: "A decision support system for direct mailing decisions"
authors: "Jedid-Jah Jonker; Nanda Piersma; Rob Potharst"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.08.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A decision support system for direct mailing decisions

Jedid-Jah Jonker <sup>a</sup>, Nanda Piersma <sup>b</sup>, Rob Potharst <sup>c,\*</sup>

<sup>a</sup> Social and Cultural Planning Office (SCP), The Hague, Netherlands

<sup>b</sup> Hogeschool van Amsterdam, HES School of Economics and Business, Amsterdam, Netherlands <sup>c</sup> Erasmus University Rotterdam, Econometric Institute, P.O. Box 1738, NL-3000 DR Rotterdam, Netherlands

Received 29 September 2004; received in revised form 12 April 2005; accepted 2 August 2005 Available online 19 September 2005

## Abstract

Direct marketing firms want to transfer their message as efficiently as possible in order to obtain a profitable long-term relationship with individual customers. Much attention has been paid to address selection of existing customers and on identifying new profitable prospects. Less attention has been paid to the optimal frequency of the contacts with customers. We provide a decision support system that helps the direct mailer to determine mailing frequency for active customers. The system observes the mailing pattern of these customers in terms of the well-known R(ecency), F(requency) and M(onetary) variables. The underlying model is based on an optimization model for the frequency of direct mailings. The system provides the direct mailer with tools to define preferred response behavior and advises the direct mailer on the mailing strategy that will steer the customers towards this preferred response behavior. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Markov decision process; Direct marketing; Decision support system

## 1. Introduction

Both in business-to-business and in consumer markets direct mailings are an important means of communication with individual customers. Direct mailings allow for a (more or less) personalized way of addressing a customer. Information about past purchase behavior can be used to make offers that suit the needs of the customers. Suppose a customer has bought product A each year in the last three years, then the firm can offer product A this time at a discounted price. The advantage for the firm is that it helps to generate customer loyalty, the advantage for the customer is that (s)he can purchase the product at a discounted price.

Typically direct marketing models select addresses for a single mailing [15]. These models will predict future response behavior of individual customers from previous behavior, social demographic variables or other available information. Stochastic models that describe the response behavior of the customers include binary choice models [4], latent class models [5], neural networks [8,13] and Markov chains [3,6,12].

These mathematical models for the support of mailing decisions have a major drawback: some consumers are left alone and others (those considered as the most profitable prospects) receive a mailing at every mailing occurrence. This paper will study different mailing approaches that might overcome this <sup>b</sup>nag-them-orleave-them-alone<sup>Q</sup> observation. Its philosophy is based upon the following principles:

Principle 1. The mailing decision is how many mailings active customers will receive over a bounded time horizon.

For a direct marketing firm, a mailing is not a onetime event but part of a flow of mailings sent over a longer period of time. Making a selection for one mailing neglects the dynamics in responding to a mailing: the decision to send a mailing today influences the probability that a person will respond to the next mailing. We will consider multiple mailings and the corresponding responses over a bounded time horizon. For each customer it is decided how many mailings to send during this time period in order to create maximal response according to certain long-term profit maximizing criteria.

The resulting mailing strategy is completely different from the <sup>b</sup>single mailing<sup>Q</sup> models that are evaluated for every separate mailing occurrence. Our model is solved only once during the time horizon and decides only on the number of mailings to send during this time interval for each customer in the database. If the decision is to send at least one mailing, then the customer is selected for a future mailing; the exact mailing occurrence used for these mailings can be determined through strategies for the timing of mailings.

Principle 2. The preferred response behavior is modeled as a combination of profit maximization and response criteria and is specified by the direct mailer.

The main goal of direct marketing firms is to obtain a profitable long-term relationship with its customers. Bitran and Mondschein [3] model this goal by optimizing customer lifetime value over a number of future mailing instances. Customer lifetime value is defined as the total discounted net future profits [2]. The model of Bitran and Mondschein decides on who to mail and on the number of mailings to send to this individual at the next mailing instance. Go¨ nu¨ l and Shi [6] extend this concept by considering the total discounted profit over an infinite horizon for the mailing decision for a single mailing instance. As Bitran and Mondschein remark, it can be more profitable to postpone a mailing to a customer to the next mailing occurrence, even though the customer is more likely to respond to this mailing than other customers. Using long-term profitability instead of probability to respond to the current mailing as the objective will overcome this problem. The model by Go¨nu¨l and Shi is actually based upon comparing the expected future profit of sending a mailing to that of postponing the mailing. We feel that this concept could be further exploited. To obtain a long-term relationship with a customer one should strive at a customized strategic mailing policy. By considering mailing frequency instead of single mailing decision models, one is able to include a sparse mailing pattern for less profitable customers. This enables the direct mailer to maintain some relationship with seemingly less profitable customers.

Also, single mailing decision models cannot model different philosophies that lie behind a direct mailing campaign. If a direct mailer is interested in a large group of active customers, he is likely to send many customers mailings based on a single mailing decision model. With a multiple mailing strategy the direct mailer can alternate between sending and not sending mailings to each customer, hoping that the customer remains active without sending wasteful mailings. Other philosophies include high response, high quality response, homogeneous response, etc. One would like to incorporate these different visions and expectations in the mathematical models. Existing models do not incorporate management input. As a result, the <sup>b</sup>optimal<sup>Q</sup> direct mailing campaigns usually advise to send the most profitable customer an abundance of mailings and leave other customers alone completely. Only by incorporating all the wishes of the direct mailer can the resulting campaign be truly considered as optimal. We provide a decision support tool that adjusts the objective function according to input from the management. The possibilities for this input are further explained in the paper. Stochastic dynamic programming models are well suited to model the mailing frequency problem. Our objective is to maximize long-term profits through a mailing strategy that maximizes the probability that an individual will enter (and remain in) the most profitable states (these states are defined within the context of our model).

The model is operationalized by a decision support system built on an Excel platform using underlying Visual Basic for Applications code. This support tool allows the user to define profitable states and calculates the optimal action for every state. Also, the model returns a large number of statistics that help the user determine more profitable mailing policies beyond the expected revenue. The tool is used by a large Dutch fundraiser<sup>1</sup> and their experiences with this DSS-tool are also reported in this paper.

The remainder of this paper is as follows. In Section 2 we model the mailing frequency problem. In Section 4 we define a number of mailing scenarios that incorporate management views and intentions. The model is applied to data for a large Dutch charitable fundraising organization. We have extensively tested scenarios in cooperation with their management and report the results in Section 5. In Section 6 we take a different view, the management’ own intuition is used to find a mailing policy that fits their view. Part of the policy is set by the manager and part is based on the mathematical model. These alternative mailing policies are compared to the policies created using only the mathematical model.

## 2. Modeling the mailing decision process

## 2.1. Markov decision process

The mailing decision process is defined as a frequency problem over a series of finite time periods. In each time period the decision is how many mailings to send to each individual customer. This decision process is modeled through a Markov decision chain in the spirit of Go¨ nu¨ l and Shi [6], Bitran and Mondschein [3] and Piersma and Jonker [12].

In our model, a customer is classified into a state S according to the mailing intensity and response in the previous time period. The customers are characterized by the response history and this history is recorded by the well-known Recency, Frequency and Monetary (RFM) characteristics<sup>2</sup>, as follows. The state of a customer at the end of time period t is defined as a threedimensional vector $S [ t ] { = } ( m [ t ] , \ r [ t ] , \ d [ t ] \ )$ ). The first element m[t] reflects the number of mailings that were received in period t. The second element r[t] holds the number of mailings that the customer responded to in t and the third element d[t] gives the total amount spent (or total amount donated) by the customer in t. This amount is divided into a finite number of classes. We assume homogeneous behavior for all customers that are observed in the same state.<sup>3</sup>

Given a state S[t] of customer i at time t, the direct mailer decides on the number of mailings that this customer will receive in period t + 1. This action is taken at the beginning of time period t + 1. The states are thus measured at the end of period t, before the decision on the number of mailings for the period t + 1 is made. The next state is then observed at the end of time period t + 1. We assume that the direct mailer will take the same action whenever the customer is found in the same state. The collection of actions for all possible states is called a (mailing) policy.

Given a mailing policy, the customer may respond a number of times. This response is recorded by the total amount spent and by the number of mailings that the customer responded to. Depending on the action a of the direct mailer taken for a customer that is found in a certain state s in the previous period, there is a (onestep) transition probability $p _ { s j } ( a )$ to the state j in this period. This probability thus depends on the state in the previous period and the action taken by the fundraiser. These transition probabilities are calculated through maximum likelihood estimation. With these transition probabilities one can calculate the steady state probabilities for each state using the standard Markov equalities (e.g. Ref. [14]).

For a customer in a given state $\pmb { S } [ t ] = \pmb { S }$ we define an expected reward for period t + 1 as the total amount donated by this customer in time period t + 1 given the number of mailings sent by the direct mailer as follows. For every state s, we record a monetary value representing the average size of the contribution from customers observed in this state by $r _ { s }$ . Next, we define the expected net reward $r [ s , a ]$ for period t + 1 for a customer observed in state s at the end of a period and with action a taken by the direct mailer as:

$$
r [ s, a ] = \sum_ {j} p _ {s j} (a) ^ {*} \left(r _ {j} - c _ {a}\right),
$$

where $c _ { a }$ represent the costs of sending a mailings. An expected reward thus depends on the state of the customer and the action taken by the direct mailer.

## 2.2. Objective function

The direct marketing firm is interested in maximizing profits. Sending all the customers in the database can be a profitable strategy when the costs of sending a mailing are low. However, even when the costs are low, sending all the customers a maximum number of mailings is usually not a preferred strategy. A direct mailing company will want to minimize the <sup>b</sup>waste<sup>Q</sup> or nonresponse from a cost minimizing perspective but also from a customer perspective: sending unwanted mailings can harm the relationship with a customer, since it can lead to irritation towards the firm. This results in a careful consideration of the number of mailings that should be sent.

In practice, companies compare different mailing policies on the basis of a number of criteria. A straightforward measure is the response rate. A drawback of the use of response probability is that it could favor selections that consist of customers that respond often but spend a relatively small amount. Therefore, it is advisable to also consider some measure of the generated revenues such as the average revenue per mailing sent. This measure incorporates both response frequency and revenue. However, if a small number of people respond but spend a high amount on response, then they will score equally compared to a group that has a high response percentage but a low amount spent per response. If the company wants to make a distinction between these groups, it should consider the average amount spent by the individuals who have responded.

If one would apply a different policy every year, it is not clear which of the policies applied is responsible for an increase or decrease in revenues. Only by applying the same policy for a number of years and comparing that policy with another one that has been applied for a number of years, one can distinguish between these policies with respect to profitability. But in practice, there is not enough data for all different policies. A theoretical measure for the sum of the revenues over a period of time is the long-run average reward. This measure reflects the average total donation per year, if the same policy is followed over an infinite number of years. It can be seen as an honest comparison for the effectiveness of different policies.

Our goal is to get individuals into states that are most beneficial to the firm. These are states where revenue is high and non-response is low. Also, we want individuals to enter these states as soon as possible. We illustrate the usefulness of this approach by the following example: suppose a mailing costs 2 guilders. Consider the state (3,1,50) where the customer responds only once to three mailings with a response of 50 guilders. If one could have the same response with one mailing (state (1,1,50)), then the net reward will be higher. However, if an additional mailing would trigger an additional response (say of size 50) resulting into state (4,2,100), the net reward will increase. Clearly states (1,1,50) and (4,2,100) are preferred over state (3,1,50) with respect to net reward. However, some states are not as easily distinguished. State (1,1,10) has smaller reward than state (3,1,14) but sends fewer mailings, resulting in the same net reward. When budget restrictions are in use, state (3,1,14) may not be preferred because of the higher cost, but otherwise the mailer may prefer 3 mailings in order to enhance visibility of the direct mailer (Bitran and Mondschein also address the problem of how many mailings will trigger a response, but restrict themselves to the same mailing occurrence).

The direct mailer can prefer to minimize the number of mailings, to maximize the response percentage or to maximize response size or any combination of these three. To give the direct mailer the control over the multiple objectives, every state is assigned a weight that reflects the relative preference of this state. The optimal mailing policy is then based on the long-run average weighted probability to observe customers in certain states. When state $s ( t )$ is given weight $w _ { s ( t ) }$ then the objective can be expressed by

$$
\max _ {a} E \left[ \sum_ {t = 0} ^ {\infty} w _ {s (t)} r [ s (t), a ] \left(\frac {1}{1 + \alpha}\right) ^ {t} | s (0) \right],
$$

where $r [ s ( t ) , a ]$ is the expected net reward when action $a$ is taken in state $s ( t )$ as defined in the Previous section and $\propto$ is the discount rate for rewards in the future.

If all states have a weight of one then the objective function will become the standard total average discounted net profit criterion for stochastic dynamic programming [16, Chapter 4]. The existence of the optimal policy is guaranteed in our model for every nonnegative weight. The model can be solved by linear programming, policy iteration or value iteration. We have implemented a fast version of the value iteration algorithm [17, pp. 208, 210].

## 3. Calibration of the model

Our model is calibrated using data from a Dutch charitable organization. It consists of the complete mailing and response history from February 1994 till December 1999. There are approximately 600,000 customers in the data set. For each customer there is a record with personal information (postal code, registration number, house number), customer information (when active, how was the customer approached, current status, date inactive, reason inactive etc), and mailing information (date of each mailing, date of each response, size of the response).

The organization uses a planning horizon of one year. At the beginning of each year, it is determined who of the active donors will receive 0, 1, 2, 3 or 4 mailings. New donors are also actively recruited each year. This makes the composition of the database dynamic: there are those who enter and there are those who become inactive. The data set consisted of a number of mailings to old customers and a number of mailings to new customers in each year. We consider a subset of 325,000 customers who have been active (in the sense that there is a record with the correct address and the customer has an active status) over the time period [1994, 1999].

Table 1  
Distribution of the customers over the states in every year

<table><tr><td>States</td><td>1994</td><td>1995</td><td>1996</td><td>1997</td><td>1998</td><td>1999</td><td>#Mailings</td><td>Average gift size</td><td>#Responses</td></tr><tr><td>0</td><td>171,440</td><td>46,688</td><td>38,067</td><td>57,394</td><td>10,600</td><td>10,488</td><td>0</td><td>0.0</td><td>0</td></tr><tr><td>1</td><td>23,720</td><td>86,704</td><td>15,996</td><td>23,017</td><td>93,744</td><td>108,678</td><td>1</td><td>0.0</td><td>0</td></tr><tr><td>2</td><td>0</td><td>95,740</td><td>114,889</td><td>48,459</td><td>31,481</td><td>30,521</td><td>2</td><td>0.0</td><td>0</td></tr><tr><td>3</td><td>0</td><td>0</td><td>9800</td><td>52,313</td><td>35,481</td><td>29,922</td><td>3</td><td>0.0</td><td>0</td></tr><tr><td>4</td><td>0</td><td>0</td><td>3200</td><td>10,187</td><td>21,808</td><td>14,324</td><td>4</td><td>0.0</td><td>0</td></tr><tr><td>5</td><td>3592</td><td>13,690</td><td>2010</td><td>116</td><td>435</td><td>415</td><td>1</td><td>4.7</td><td>1</td></tr><tr><td>6</td><td>7851</td><td>978</td><td>10,185</td><td>1844</td><td>1639</td><td>3660</td><td>2</td><td>4.7</td><td>1</td></tr><tr><td>7</td><td>0</td><td>0</td><td>975</td><td>6529</td><td>5274</td><td>645</td><td>3</td><td>4.8</td><td>1</td></tr><tr><td>8</td><td>0</td><td>0</td><td>16</td><td>795</td><td>1389</td><td>1395</td><td>4</td><td>5.0</td><td>1</td></tr><tr><td>9</td><td>11,418</td><td>41,354</td><td>1594</td><td>386</td><td>1009</td><td>1315</td><td>1</td><td>10.8</td><td>1</td></tr><tr><td>10</td><td>23,949</td><td>10,021</td><td>20,191</td><td>3466</td><td>5155</td><td>11,414</td><td>2</td><td>10.8</td><td>1</td></tr><tr><td>11</td><td>0</td><td>3</td><td>13,673</td><td>21,114</td><td>13,090</td><td>5239</td><td>3</td><td>11.9</td><td>1</td></tr><tr><td>12</td><td>0</td><td>0</td><td>1729</td><td>7260</td><td>13,610</td><td>4083</td><td>4</td><td>11.5</td><td>1</td></tr><tr><td>13</td><td>5564</td><td>12,705</td><td>595</td><td>276</td><td>484</td><td>356</td><td>1</td><td>25.1</td><td>1</td></tr><tr><td>14</td><td>11,058</td><td>8830</td><td>4985</td><td>954</td><td>1996</td><td>2245</td><td>2</td><td>24.7</td><td>1</td></tr><tr><td>15</td><td>0</td><td>3</td><td>6027</td><td>6714</td><td>4530</td><td>4801</td><td>3</td><td>24.4</td><td>1</td></tr><tr><td>16</td><td>0</td><td>0</td><td>5973</td><td>9866</td><td>12,527</td><td>1614</td><td>4</td><td>25.1</td><td>1</td></tr><tr><td>17</td><td>828</td><td>1800</td><td>56</td><td>40</td><td>70</td><td>59</td><td>1</td><td>51.1</td><td>1</td></tr><tr><td>18</td><td>1552</td><td>1162</td><td>538</td><td>82</td><td>279</td><td>167</td><td>2</td><td>51.5</td><td>1</td></tr><tr><td>19</td><td>0</td><td>2</td><td>856</td><td>575</td><td>526</td><td>315</td><td>3</td><td>51.0</td><td>1</td></tr><tr><td>20</td><td>0</td><td>0</td><td>1303</td><td>2107</td><td>2371</td><td>347</td><td>4</td><td>51.7</td><td>1</td></tr><tr><td>21</td><td>313</td><td>638</td><td>22</td><td>10</td><td>29</td><td>28</td><td>1</td><td>168.9</td><td>1</td></tr><tr><td>22</td><td>652</td><td>483</td><td>154</td><td>33</td><td>89</td><td>42</td><td>2</td><td>162.7</td><td>1</td></tr><tr><td>23</td><td>0</td><td>1</td><td>332</td><td>149</td><td>221</td><td>44</td><td>3</td><td>156.8</td><td>1</td></tr><tr><td>24</td><td>0</td><td>0</td><td>684</td><td>975</td><td>1023</td><td>154</td><td>4</td><td>200.9</td><td>1</td></tr><tr><td>25</td><td>2217</td><td>6</td><td>1567</td><td>73</td><td>102</td><td>166</td><td>2</td><td>5.2</td><td>2</td></tr><tr><td>26</td><td>0</td><td>0</td><td>113</td><td>754</td><td>707</td><td>42</td><td>3</td><td>5.2</td><td>2</td></tr><tr><td>27</td><td>0</td><td>0</td><td>4</td><td>146</td><td>195</td><td>102</td><td>4</td><td>5.3</td><td>2</td></tr><tr><td>28</td><td>10,035</td><td>107</td><td>4594</td><td>245</td><td>485</td><td>848</td><td>2</td><td>11.6</td><td>2</td></tr><tr><td>29</td><td>0</td><td>0</td><td>1767</td><td>3491</td><td>2554</td><td>346</td><td>3</td><td>11.6</td><td>2</td></tr><tr><td>30</td><td>0</td><td>0</td><td>75</td><td>1395</td><td>1635</td><td>479</td><td>4</td><td>12.5</td><td>2</td></tr><tr><td>31</td><td>36,033</td><td>1800</td><td>6176</td><td>527</td><td>1695</td><td>2327</td><td>2</td><td>24.5</td><td>2</td></tr><tr><td>32</td><td>0</td><td>5</td><td>13,178</td><td>8610</td><td>6075</td><td>2167</td><td>3</td><td>23.4</td><td>2</td></tr><tr><td>33</td><td>0</td><td>0</td><td>3702</td><td>10,176</td><td>11,533</td><td>1799</td><td>4</td><td>26.7</td><td>2</td></tr><tr><td>34</td><td>12,052</td><td>1484</td><td>472</td><td>107</td><td>471</td><td>237</td><td>2</td><td>53.5</td><td>2</td></tr><tr><td>35</td><td>0</td><td>2</td><td>2479</td><td>1331</td><td>1417</td><td>599</td><td>3</td><td>52.7</td><td>2</td></tr><tr><td>36</td><td>0</td><td>0</td><td>4478</td><td>5514</td><td>5546</td><td>606</td><td>4</td><td>53.7</td><td>2</td></tr><tr><td>37</td><td>2198</td><td>264</td><td>55</td><td>17</td><td>102</td><td>32</td><td>2</td><td>141.4</td><td>2</td></tr><tr><td>38</td><td>0</td><td>1</td><td>455</td><td>123</td><td>211</td><td>27</td><td>3</td><td>142.0</td><td>2</td></tr><tr><td>39</td><td>0</td><td>0</td><td>1018</td><td>1267</td><td>1152</td><td>127</td><td>4</td><td>157.2</td><td>2</td></tr><tr><td>40</td><td>0</td><td>0</td><td>84</td><td>469</td><td>443</td><td>19</td><td>3</td><td>6.6</td><td>3</td></tr><tr><td>41</td><td>0</td><td>0</td><td>0</td><td>193</td><td>168</td><td>41</td><td>4</td><td>6.8</td><td>3</td></tr><tr><td>42</td><td>0</td><td>0</td><td>1390</td><td>1269</td><td>1136</td><td>83</td><td>3</td><td>14.9</td><td>3</td></tr><tr><td>43</td><td>0</td><td>0</td><td>12</td><td>1061</td><td>1020</td><td>140</td><td>4</td><td>15.2</td><td>3</td></tr><tr><td>44</td><td>0</td><td>1</td><td>10,348</td><td>2877</td><td>3088</td><td>463</td><td>3</td><td>31.2</td><td>3</td></tr><tr><td>45</td><td>0</td><td>0</td><td>2409</td><td>8359</td><td>7456</td><td>821</td><td>4</td><td>33.3</td><td>3</td></tr><tr><td>46</td><td>0</td><td>0</td><td>2155</td><td>570</td><td>1014</td><td>195</td><td>3</td><td>68.0</td><td>3</td></tr><tr><td>47</td><td>0</td><td>0</td><td>4221</td><td>4782</td><td>4113</td><td>393</td><td>4</td><td>69.7</td><td>3</td></tr><tr><td>48</td><td>0</td><td>0</td><td>464</td><td>104</td><td>211</td><td>15</td><td>3</td><td>161.6</td><td>3</td></tr><tr><td>49</td><td>0</td><td>0</td><td>1111</td><td>1239</td><td>1066</td><td>104</td><td>4</td><td>175.7</td><td>3</td></tr><tr><td>50</td><td>0</td><td>0</td><td>0</td><td>219</td><td>181</td><td>23</td><td>4</td><td>7.8</td><td>4</td></tr><tr><td>51</td><td>0</td><td>0</td><td>2</td><td>204</td><td>147</td><td>23</td><td>4</td><td>15.2</td><td>4</td></tr><tr><td>52</td><td>0</td><td>0</td><td>1625</td><td>7305</td><td>5872</td><td>434</td><td>4</td><td>37.0</td><td>4</td></tr><tr><td>53</td><td>0</td><td>0</td><td>2965</td><td>3539</td><td>2792</td><td>161</td><td>4</td><td>68.0</td><td>4</td></tr><tr><td>54</td><td>0</td><td>0</td><td>3703</td><td>3845</td><td>3025</td><td>170</td><td>4</td><td>143.0</td><td>4</td></tr></table>

The fund uses at most 4 mailings per year, so the response of the customers is limited to at most 4 reactions per year. Hence, each year five possible actions can be taken. A careful comparison of the donations showed that the amount donated per year can be aggregated into five intervals [0,10], (10,25], (25,50], (50,100], (100,+) (in Dfl). A representable gift size in each of these states is 7.5, 22.5, 40, 87.5 and 150, respectively. There are thus exactly 55 states (to be precise: with 5 possible donation sizes and at most 4 mailings: 0 mailings (1 state) + 1 mailing (5 	 1 + 1 (no reaction) states) + 2 mailings (5	2 +1)+3 mailings (5	3+1)+4 mailings (5 4+1)=1+6 +11+16+21=55 states). Table 1 shows the main characteristics of each state for loyal customers, defined by the customers that are active from the beginning of 1994 till the end of 1999.

## 4. Decision support tool: standard scenarios

With the definition of the states in terms of RFM variables, the direct mailer can identify preferable states in terms of customer profitability and mailing intensity. A specification of the weights for all the 55 states is defined as a scenario. Our decision support system contains four standard scenarios and the option for the customer to define other customer-specified scenarios. The support tool shows the 55 states and the weights that (can be) assigned to each state.

The standard scenarios are

1. Equal weights

All states are equally important and have weight 1. This scenario gives the standard mailing frequency problem that optimizes the long-term discounted reward.

2. Efficiency: emphasize fewer mailings

The states that will receive a high weight are those where an individual receives no more than 3 mailings per year. The states that will have a lower weight are those where an individual receives four mailings. The high weight is set to 100 and the low weight to 1. These weights <sup>b</sup>encourage<sup>Q</sup> being in a state where less than the maximum of four mailings is sent. The size of the weight is arbitrary but should be large enough to notice any effect.

3. Profitability: emphasize high profitable customers

In this scenario the customers are weighted according to their profitability. More profitable customers donate more often and donate more. We measure the profitability by the gift size and the response percentage. Specifically, weight 1 is assigned to all the states

– with gift size at most Dfl 10, i.e. gift class 0 or 1, or – with a response percentage of at most 25%.

These customers are assumed to be less profitable or need too much encouragement before they respond. Weight 50 is assigned to all the states that respond at least 25%, but

– with gift size at most Dfl 25, or

– with a response percentage no more than 60%.

The states that will receive a high weight with size 100 are those where the gift size is at least Dfl 25 and the individual responds frequently, that is with a response percentage of at least 60%.

4. Participation: emphasize responding customers This scenario steers towards maximal participation of customers, defined by at least one response per year. We therefore consider two weights:

– Weight 100: all the customers that respond at least once.

– Weight 1: all the customers that do not respond.

The user cannot change the weights of standard scenarios. However, we included an option where the user overrules the advice of the support tool by fixing the action for a certain number of states. If one then calculates the optimal policy for a scenario, the underlying model fixes the action for these states and determines only the optimal actions for the remaining states. The use of this option is exploited in Section 6.

## 5. Results

The optimal policy is determined using the Markov decision model as described before. The parameters that need to be specified to the model are the average profit for each state and action and the transition probabilities between the states under each number of mailings. All these parameters are estimated using maximum likelihood estimation, using all the customers in the database.

The profitability of the policies is evaluated for a subset of 325,000 loyal and active customers that is selected randomly from the database. For each of the customers, we record their state at the beginning of 1998. These parameters are also used as input for the support tool. We then evaluate the theoretical long-term profit for this set of customers, if a selected mailing policy is applied for an infinite number of years. The results also include the short-term expected profit.

Table 2  
Profits from sending four mailings to every customer, discount factor 0.9

<table><tr><td>Year</td><td>Reward</td><td>#Mails</td><td>#Responses</td><td>Reward/ mail</td><td>Reward/ response</td></tr><tr><td>1</td><td>15.6703</td><td>1.29789</td><td>0.4753</td><td>12.07</td><td>32.97</td></tr><tr><td>2</td><td>14.6089</td><td>1.29789</td><td>0.4606</td><td>11.26</td><td>31.72</td></tr><tr><td>3</td><td>13.7451</td><td>1.29789</td><td>0.4489</td><td>10.59</td><td>30.62</td></tr><tr><td>4</td><td>13.2244</td><td>1.29789</td><td>0.4412</td><td>10.19</td><td>29.97</td></tr><tr><td>5</td><td>12.9632</td><td>1.29789</td><td>0.4369</td><td>9.99</td><td>29.67</td></tr><tr><td>Long run</td><td>12.8571</td><td>1.29789</td><td>0.4350</td><td>9.91</td><td>29.55</td></tr></table>

The reward is given in millions of Dutch guilders. The number of mails and the number of responses are given in millions.

We do not compare our theoretical results with recorded results for a historical dataset since the mailing policy of the fund is not based on strategic decision making. Instead, we compare our theoretical results with a mailing policy that sends the maximum number (for this application the maximum is four) of mailings. We especially study the costs of management decisions using the same mathematical framework rather than comparing different mathematical models. Further justification of the mathematical model compared to other models can be found in Ref. [12].

The results are given in Dutch guilders (Dfl). We have calculated the net profit of the mailing strategy for the customer set given the distribution of these customers within one, two, up to 5 years and the long-run distribution (based on the steady state probabilities). We record the total net profit (in millions of guilders), the total number of mailings sent to the customers in the dataset (in millions of guilders), and the number of responses (in millions). Also, we give the net profit per mailing (as the total net profit divided by the total number of mailings) and the net profit per response (i.e. the total net profit divided by the total number of responses). As the initial state of the model, we use the distribution of the customers over the states in last year of the dataset.<sup>4</sup>

In Tables 2–4 we compare the optimal policy under scenario 1 with the naı¨ve policy that sends four mailings to every customer. In Table 2 the statistics for the naı¨ve strategy are recorded using a discount factor of 0.9. Tables 3 and 4 record the statistics of scenario 1 for discount factors 0.1 and 0.9, respectively. With discount factor 0.1, future expected profits are considered to be relatively unimportant in the determination of the optimal policy and current profits are dominant. For discount factor 0.9, the future expected earnings are considered to be dominant in the determination of the optimal policy.

Table 3  
Optimal strategy profits, scenario 1, discount factor 0.1

<table><tr><td>Year</td><td>Reward</td><td>#Mails</td><td>#Responses</td><td>Reward/ mail</td><td>Reward/ response</td></tr><tr><td>1</td><td>15.7931</td><td>1.28986</td><td>0.4591</td><td>12.24</td><td>34.40</td></tr><tr><td>2</td><td>15.6293</td><td>1.22631</td><td>0.4268</td><td>12.75</td><td>36.62</td></tr><tr><td>3</td><td>15.6881</td><td>1.23894</td><td>0.4262</td><td>12.66</td><td>36.81</td></tr><tr><td>4</td><td>15.5215</td><td>1.23558</td><td>0.4185</td><td>12.56</td><td>37.09</td></tr><tr><td>5</td><td>15.4149</td><td>1.23683</td><td>0.4151</td><td>12.46</td><td>37.14</td></tr><tr><td>Long run</td><td>15.2433</td><td>1.23795</td><td>0.4099</td><td>12.31</td><td>37.19</td></tr></table>

The results clearly show the profitability of mailing optimization. In Table 2 the mailing pressure remains the same over the years, but the net profit decreases. Both the number of responses and the profit per response decrease over time. Interestingly enough, the total number of responses and the total number of mailings are very high. The current practice to send out as many mailings as possible is justified by optimization criterion to maximize the total number of responses. But the total profit of the naı¨ve strategy cannot match the total profit of the optimal mailing policy even though the number of responses is less for the optimal policy. This result holds for both discount factors. The customer segmentation therefore allows for a more profitable customized mailing policy. We conclude that sending out the maximum number of mailings will result into wasteful mailings and over time causes irritation and reduced responses. However, sending three mailings to every customer will result into a long-run average expected net profit of only Dfl 3.67 million. Thus, there should be a careful tradeoff between sending enough encouragement for a preferred response and not sending too many mailings.

The results in Table 3 (discount factor 0.1, shortterm profits are dominant) and Table 4 (discount factor 0.9, long-term profits are dominant) show that maximizing long-term profit is more profitable within two years. In the first year, the short-term objective sends out many mailings (1.29 million versus 0.8 million for long-term objective), but in contrast to the maximum mailing pressure strategy the optimal short-term mailing policy can prevent the decay in the response, both in quality and in quantity. The long-term scenario will result into one <sup>b</sup>bad<sup>Q</sup> year, where many customers do not receive a mailing during the entire year. However, the expected net profit can improve with 25% compared to the short-term scenario as is apparent from Tables 3 and 4. The number of mailings and the number of responses for the long-term profitable objective is less than in Tables 2 and 3, but the quality of the responses makes up for the loss in response. So in a theoretical setting, it should be possible to induce people to donate more by sending fewer mailings.

Table 4  
Optimal strategy profits, scenario 1, discount factor 0.9

<table><tr><td>Year</td><td>Reward</td><td>#Mails</td><td>#Responses</td><td>Reward/ mail</td><td>Reward/ response</td></tr><tr><td>1</td><td>12.2709</td><td>0.82471</td><td>0.3037</td><td>14.88</td><td>40.40</td></tr><tr><td>2</td><td>21.2802</td><td>1.10371</td><td>0.4590</td><td>19.28</td><td>46.37</td></tr><tr><td>3</td><td>20.0452</td><td>0.99596</td><td>0.3941</td><td>20.13</td><td>50.86</td></tr><tr><td>4</td><td>20.4365</td><td>1.01725</td><td>0.3991</td><td>20.09</td><td>51.20</td></tr><tr><td>5</td><td>20.1622</td><td>0.99464</td><td>0.3857</td><td>20.27</td><td>52.28</td></tr><tr><td>Long run</td><td>20.2538</td><td>0.99701</td><td>0.3841</td><td>20.32</td><td>52.73</td></tr></table>

Tables 5 and 6 compare the different scenarios described in the previous section. Table 5 lists the statistics in the long run for each scenario, when a discount factor of 0.9 is used in the optimization procedure. Table 6 shows the number of states (in percentages) that receive 0, 1, 2, 3 and 4 mailings per year for each scenario. For example, for scenario 1 and 4 the optimal policy advises to send 4 mailings to 43.6% of the states. It appears that the equal weight scenario (no. 1) and the maximum participation scenario (no. 4) result into the same mailing policy. Scenario 3 emphasizes the profitable customers. Comparing scenarios 1 and 4 with scenario 3, we see in Tables 5 and 6 that there is only a slight difference in profitability and in the actions towards the states. In particular, only two states receive less mailings in the profitable states scenario, state 16 where four mailings are needed for one response and gift class 3 now receives only 1 instead of 4 mailings and state 43 with three responses to 4 mailings, but gift class 2 is considered not profitable enough for any future mailing. In the profitable states scenario (no. 3), the average reward per response is slightly higher and the number of mailings is less, as was to be expected from the set up of the scenario. The costs of this profitable strategy are approximately Dfl 92,000 per year in the long run.

Table 5  
Optimal long-term profits, scenario 1–4, discount factor 0.9

<table><tr><td>Scenario</td><td>Reward</td><td>#Mails</td><td>#Responses</td><td>Reward/ mail</td><td>Reward/ response</td></tr><tr><td>1</td><td>20.2538</td><td>0.99701</td><td>0.3841</td><td>20.32</td><td>52.73</td></tr><tr><td>2</td><td>17.3988</td><td>0.87924</td><td>0.3424</td><td>19.79</td><td>50.82</td></tr><tr><td>3</td><td>20.1612</td><td>0.96967</td><td>0.3815</td><td>20.79</td><td>52.85</td></tr><tr><td>4</td><td>20.2538</td><td>0.99701</td><td>0.3841</td><td>20.32</td><td>52.73</td></tr></table>

Table 6  
Action distribution (in %)

<table><tr><td>Scenario</td><td>Action 0</td><td>Action 1</td><td>Action 2</td><td>Action 3</td><td>Action 4</td></tr><tr><td>1 and 4</td><td>9.1</td><td>29.1</td><td>0</td><td>18.2</td><td>43.6</td></tr><tr><td>2</td><td>10.9</td><td>32.7</td><td>5.5</td><td>32.7</td><td>18.2</td></tr><tr><td>3</td><td>10.9</td><td>29.1</td><td>0</td><td>18.2</td><td>41.8</td></tr></table>

Hence, the profitable states scenario does send out fewer mailings, it will result into fewer responses, and the quality of the responses is slightly better than the standard scenario.

The efficient scenario (no. 2) seeks out to send less than four mailings, but this strategy leads to a substantial lower net profit in the short-and in the long run compared to the other scenarios. Apparently, there are a number of customer groups that need 4 encouragements. If we increase the cost of a mailing, the efficient scenario will become even more selective in the number of customer groups that receive at least one mailing. For example, if the cost per mailing is raised from 1 to 10 guilders, then the number of states receiving 0 mailings under scenario 2 is raised from 10.9% to 34.5%. For the other scenarios, the increase is not as large. As a result, scenario 2 sends too few mailings and is still outperformed in profits by the other scenarios.

## 6. Management versus model

In our decision support tool, we included the option to fix the action for states of the user’s choice. In the optimization procedure the action for such a state remains fixed and is not optimized. As a special case, we already reported the results for the option to fix the action to 4 for each state; we called this the naı¨ve scenario. But it is also possible to fix the action for only a subset of the states and to optimize the actions for the remaining states.

The management of the fund was especially interested in the customers in state 0. This state contains new customers and customers who received no mailing in the previous year. We observe that the optimal policy in all the standard scenarios is to send four mailings to the customers in state 0. We wondered what the effect on the performance will be if we decide to overrule the decision to send no mailings and use some other action in state 0. Table 7 shows the long-run statistics for the policy optimization where only state 0 has a fixed action. In first row, the results are given if the action for state 0 is fixed to 0.

Table 7  
Long-run performance when action in state 0 is fixed, scenario 1, discount factor 0.9

<table><tr><td>Action</td><td>Reward</td><td>#Mails</td><td>#Responses</td><td>Reward/ mail</td><td>Reward/ response</td></tr><tr><td>0</td><td>19.5224</td><td>0.97407</td><td>0.3869</td><td>20.04</td><td>50.45</td></tr><tr><td>1, 2, 3</td><td>20.1817</td><td>1.00696</td><td>0.4000</td><td>20.04</td><td>50.45</td></tr><tr><td>4</td><td>20.2538</td><td>0.99701</td><td>0.3841</td><td>20.32</td><td>52.73</td></tr></table>

Observe that in the long run there is no difference in the expected performance of scenario 1 if state 0 receives 1, 2 or 3 mailings. Only the extreme choices, sending inactive customers 0 or 4 mailings will lead to different performance. Sending 4 mailings (the <sup>b</sup>nag them<sup>Q</sup> scenario) is advised by the support system. When inactive customers are no longer approached, i.e. the <sup>b</sup>leave them alone<sup>Q</sup> scenario, the result will be that no other state will have the optimal action to send 0 mailings. That is, the other customers will not enter state 0. In contrast, the optimal mailing policy without the fix for state 0 contains 5 states that have optimal action 0 (Table 8). These groups are not infinitely excluded from further mailings, but the advice is to refrain from sending mailings for one year. When the customers have entered state 0, they will again receive mailings in the next year. These groups contain customers that need many mailings, respond often but donate small contributions. In the long run, 2.1% of the customers are expected to be in these states. When the inactive customers are no longer approached (fixed action 0 for state 0), the support systems advises to send these less profitable groups one mailing. Thus, only the inactive customers in the first year are left alone and more effort is made to approach the currently active customers. The same phenomenon is observed for the other standard scenarios.

The fund management was also interested in sending one mailing to customer groups that in the optimal policy received no mailings. Again, these customers are not profitable enough in the optimal policy to justify a mailing, but the management wondered what the effect is in the long-term performance if these customers are not excluded from the mailing list. Therefore, we calculated the optimal policy, fixed the action to 1 for states that have action 0 in the optimal policy and recalculated the optimal policy. The resulting policy did not include new states with action 0, so all customers receive at least one mailing.

Table 8  
Long-run performance when all states with optimal action 0 is fixed to action 1, scenario 1, discount factor 0.9

<table><tr><td>Scenario</td><td>Reward</td><td>#Mails</td><td>#Responses</td><td>Reward/ mail</td><td>Reward/ response</td></tr><tr><td>Standard</td><td>20.2538</td><td>0.99701</td><td>0.3841</td><td>20.32</td><td>52.73</td></tr><tr><td>Alternative</td><td>20.1817</td><td>1.00696</td><td>0.4000</td><td>20.04</td><td>50.45</td></tr></table>

Both in the long-run and the short-run performance the difference is small, but the comparison clearly shows that the extra mailings will trigger extra responses from these customers with small donations. The number of responses does increase but the average contribution per mailing and per response will significantly decrease in the long run.

## 7. Conclusion

In this paper we observe the mailing policy under various scenarios, showing that customer relations need to be defined carefully. Our first contribution to the literature is the development, estimation and testing of a dynamic programming model for a charity fund and showing the specific needs for this application. The model provides mailing policies for multiple time periods, thus establishing a relationship with the customer over multiple time periods rather than seeking high profitable contributors and new contributors in each mailing occasion.

Our second and main contribution is a careful discussion of the impact of objective functions on the mathematical model and the implications for the mailing policy. The results show that management goals often conflict with the optimization criteria used in the mathematical model. We compare different mailing philosophies with respect to overall profit and response percentage in the short and the long run. Optimizing long-term profits coincides with maximizing response percentage for our application. Apparently, the cost of a mailing is small enough and every customer that is likely to respond will receive a mailing at every mailing occasion. When mailing cost becomes larger (for instance for catalogs), the maximal response scenario will become less profitable.

Finally, we describe a decision support model that helps the user to quantify the loss or profit by defining either weights for the importance that the user puts on a state or even the action that user wants for certain states. In the extreme case, the user can fix the action for every state and the optimization model becomes a simple calculation tool for the profitability of the actions defined. This enables the user to evaluate previous mailing policies as well as mailing policies that the user is considering. The other extreme is to let the decision support tool decide on the action for every state and exhibit the profitability of these <sup>b</sup>optimal<sup>Q</sup> (with respect to the scenario selected) actions. The decision tool is used by the Dutch fundraiser who first used the model to answer simple management questions about the theoretical profitability of using mathematical models for mailing frequency their fund. Being satisfied with these predictions, the fund then experimented with other mailing scenarios and used the results as a basis for current mailing decisions.

A number of extensions are currently being implemented in the model. First, the support tool is converted to the new European currency Euro. As a result, the fund already observes that customers tend to round their donations to higher amounts. Since our model uses the size of the donations in the model, we will implement a correction as soon as the correction factor is known. Second, the model is being extended to use updates of the parameter data. As mentioned, the model bases its profitability on the distribution of a subset of the customers over the states in 1998. The user should have the opportunity to use other distributions. Likewise, the transition probabilities can be estimated based on the other data than the data from the time interval [1994,1999]. In Ref. [7] a bootstrap technique was used to reduce the error in the transition probabilities estimates. This correction is currently not implemented in the decision support tool. Third, in the future we want to allow the user to change the state definition and the number of states. The direct mailer is especially interested in sending more than 4 mailings per year. In order to do so, one should include an estimation procedure for the parameters of the model and link the support tool to a database. Finally, a future research direction could be to try to relax the restriction on the number of relevant variables that influence customers’ response behavior. Instead of taking into account only a few RFM variables as is the approach of this study, often firms have access to over 100 variables that affect a customer’s probability of purchase, see for example Refs. [11,10]. An appropriate reduction of the dimensionality would probably be called for to make this approach feasible, for instance using the approach of Ref. [11]. Another future research direction could be to try to include multiple media, instead of only direct mail, use the synergy between them and develop a DSS for jointly determining the optimal budget level and its allocation to alternative media (e.g. radio, TV or print) and direct mail contacts, as is done for TV and print in Ref. [9].

## Acknowledgements

The authors would like to thank the editor and two anonymous referees for some helpful comments and constructive suggestions.

## References

[1] C.L. Bauer, A direct mail customer purchase model, Journal of Direct Marketing 2 (1988) 16 – 24.

[2] P.D. Berger, N.I. Nasr, Customer lifetime value: marketing models and applications, Journal of Interactive Marketing 12 (1998) 17–30.

[3] G.R. Bitran, S.V. Mondschein, Mailing decisions in the catalog sales industry, Management Science 42 (1996) 1364– 1381.

[4] J.R. Bult, T. Wansbeek, Optimal selection for direct mail, Marketing Science 14 (1995) 378–394.

[5] W.S. DeSarbo, V. Ramaswamy, CRISP: Customer Response based Iterative Segmentation Procedures for response modeling in direct marketing, Journal of Direct Marketing 8 (1994) 7 – 20.

[6] F. Go¨nu¨l, M.Z. Shi, Optimal mailing of catalogs: a new methodology using estimable structural dynamic programming models, Management Science 44 (1998) 1249– 1262.

[7] J.J. Jonker, N. Piersma, D. Van den Poel, Joint optimization of customer segmentation and marketing policy to maximize longterm profitability, Expert Systems with Applications 2 (2004) 159– 168.

[8] N. Levin, J. Zahavi, Segmentation analysis with managerial judgment, Journal of Direct Marketing 10 (1996) 28–37.

[9] P.A. Naik, K. Raman, Understanding the impact of synergy in multimedia communications, Journal of Marketing Research 40 (2003) 375–388.

[10] P.A. Naik, C.-L. Tsai, Isotonic single-index model for highdimensional database marketing, Computational Statistics and Data Analysis 47 (2004) 775–790.

[11] P.A. Naik, M. Hagerty, C.-L. Tsai, A new dimension reduction approach for data-rich marketing environments: sliced inverse regression, Journal of Marketing Research 37 (2000) 88 – 101.

[12] N. Piersma, J.J. Jonker, Determining the optimal direct mailing frequency, European Journal of Operational Research 158 (2004) 173 – 182.

[13] R. Potharst, U. Kaymak, W. Pijls, Neural networks for target selection in direct marketing, in: Kate A. Smith, Jatinder N.D. Gupta (Eds.), Neural Networks in Business: Techniques and Applications, Idea Group Publishing, 2002, pp. 89 – 110, ISBN 1-930708-31-9.

[14] M.L. Puterman, Markov Decision Processes: Discrete Stochastic Dynamic Programming, Wiley-Interscience, 1994, ISBN: 0471619779.

[15] M.L. Roberts, P.D. Berger, Direct Marketing Management, Prentice Hall Inc., Englewood Cliffs, New Jersey, 1999.

[16] S. Ross, Introduction to Stochastic Dynamic Programming, Academic Press, New York, 1983.

[17] H.C. Tijms, Stochastic Models: An Algorithmic Approach, Wiley, 1994.

![](/api/attachments/WQA23PMW/fulltext/images/f85edc4c8cc6359c3c481dcdfa2314c94154113a5e6d15ce102ec70c8f191eb8.jpg)  
Jedid-Jah Jonker is a researcher at the Social and Cultural Planning Office of the Netherlands (SCP). He received his MSc (1997) and PhD (2002) in econometrics from the Erasmus University Rotterdam. He has published articles in Marketing Science, Journal of Applied Econometrics and European Journal of Operational Research. At the SCP he is working on analyzing and forecasting the demand for health care.

![](/api/attachments/WQA23PMW/fulltext/images/998077cc328ce5e414f43e18dcc860950777d61da4f10adac4e124d7e73670f0.jpg)

Nanda Piersma is the program manager of the bachelor program International Business and Management Studies at the HES School of Economics and Business. During the research for this article she was an assistant professor at the Econometric Institute of the Erasmus University in Rotterdam. She has published in European Journal of Operational Research, Journal on Combinatorial Optimization, Naval Research Logistics, and Journal of Revenue

Management. She received her PhD in operations research at the University of Amsterdam.

![](/api/attachments/WQA23PMW/fulltext/images/e80668a1f15a872fc5dc82cf434a594a2585b18d6fa0193018e0d8263121201e.jpg)

Rob Potharst is lecturer in computer science and marketing at the Econometric Institute of Erasmus University Rotterdam in the Netherlands. He received his MSc in mathematics from the University of Amsterdam. In 1999 he received a PhD in computer science from Erasmus University. He has published in Intelligent Data Analysis, Lecture Notes in Computer Science and Lecture Notes in Artificial Intelligence. Currently, his main focus is on decision support for

marketing decisions, employing techniques from computational intelligence.
