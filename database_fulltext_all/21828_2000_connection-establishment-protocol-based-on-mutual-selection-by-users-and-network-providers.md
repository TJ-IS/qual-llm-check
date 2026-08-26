---
otero_id: 21828
otero_key: "ECM2PYE6"
title: "Connection establishment protocol based on mutual selection by users and network providers"
authors: "Nagao Ogino"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00075-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Connection establishment protocol based on mutual selection by users and network providers

Nagao Ogino )

ATR AdaptiÕe Communications Research Laboratories, 2-2, Hikaridai, Seika-cho, Soraku-gun, Kyoto 619-0288, Japan

## Abstract

This paper proposes a new connection establishment protocol involving several competing network providers in a multimedia telecommunications environment. This connection establishment protocol, which is based on the concept of open competitive bidding, enables mutual selection by users and network providers. By employing this proposed protocol, both network providers and users can pursue their own objectives according to their own bidding and awarding strategies. In this paper, a simple bidding strategy for network providers is presented, and the effectiveness of this strategy is evaluated by means of computer simulation. It is shown that each network provider can improve its profit by adopting this strategy. In this paper, an example of utility functions for users is presented, and the effectiveness of the mechanism to select a network provider is also evaluated by means of computer simulation. Each user can improve his<sup>r</sup>her utility by selecting an appropriate network provider based on this utility function. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Market-based network protocol; Multimedia connection establishment; Distributed resource allocation; Mutual selection; Evaluation of multi-agent systems

## 1. Introduction

Hereafter, more and more network providers are expected to be established by the introduction of the open telecommunications market. It will therefore become necessary to guarantee fair competition between all of these network providers who will set their own rates. Therefore, a mechanism is required so that each network provider can bid on every connection request based on its own judgment and inform users of its rates.

On the other hand, the connection requests of users will be varied in this multimedia telecommunications environment. Users will request connections for various media with various quality of service Ž . QoS levels. As a result, a mechanism is required so that each user can be informed of each network provider’s rates and select one of them according to his<sup>r</sup>her utility function.

In this paper, a new connection establishment protocol based on the concept of open competitive bidding 2 is proposed. This connection establish- <sup>w</sup> <sup>x</sup> ment protocol can achieve the mechanisms described above and enables mutual selection by users and network providers. Both network providers and users can pursue their own objectives based on their own bidding and awarding strategies under the proposed connection establishment protocol framework. A simple bidding strategy for network providers is presented, and the effectiveness of this strategy is evaluated by means of computer simulation. It is shown that each network provider can improve its profit by adopting this strategy. Next, an example of utility functions for users is presented, and the effectiveness of the mechanism to select a network provider is also evaluated by means of computer simulation. Each user can improve his<sup>r</sup>her utility by selecting an appropriate network provider based on this utility function.

The organization of this paper is as follows. In Section 2, related works and the difference between those works and this work are explained. In Section 3, the proposed connection establishment protocol and simple strategies for network providers and users are explained in detail. In Section 4, the effectiveness of the proposed strategies is evaluated by computer simulation. Finally, Section 5 concludes this paper and discusses future works.

## 2. Related works

Various studies on market-based distributed resource allocation have been performed. For example, Wellman 17 proposed a framework for such re-<sup>w</sup> <sup>x</sup> source allocation. Ferguson et al. 4 proposed a method for allocating CPU time and communication links to tasks. This method can achieve a globally effective allocation of CPU time and communication resources using the concept of resource pricing. Waldspurger et al. 16 proposed the Spawn system <sup>w</sup> <sup>x</sup> for allocating workstations with various levels of performance to concurrent applications. This system can achieve priority control by a monetary funding allocation mechanism.

Various market-based negotiation protocols for connection establishment have been proposed 5 .<sup>w</sup> <sup>x</sup> MacKie-Mason and Varian 8 introduced a smart<sup>w</sup> <sup>x</sup> market pricing scheme, for each packet transmitted to the Internet, to control congestion and to improve network efficiency. Cocchi et al. 1 proposed a <sup>w</sup> <sup>x</sup> priority pricing policy for multiple-service disciplines in computer networks. Generally speaking, congestion control can be achieved by introducing a congestion cost reflecting QoS deterioration, especially for best-effort type computer networks such as the present Internet.

For guaranteed QoS type networks such as ATM networks, various market-based connection establishment schemes have already been proposed. In these schemes, the network provider adjusts resource prices based on the demand and utilization levels of resources, and users decide the amounts of resources to request based on these resource prices posted by the network provider. These schemes can therefore maximize social welfare automatically by having each user maximize his<sup>r</sup>her consumer surplus.

The advantage of resource pricing is that the network provider does not need to know detailed user’s traffic parameters, and therefore there is no need for traffic policing. Low and Varaiya 7 used<sup>w</sup> <sup>x</sup> each user’s demand elasticity for bandwidth versus buffer, to improve network usage. Murphy et al. 10 <sup>w</sup> <sup>x</sup> suggested a distributed pricing policy to allocate bandwidth on the VP level and VC level. Kelly 6<sup>w</sup> <sup>x</sup> developed a pricing structure to encourage users to declare their true traffic parameters. However, the network provider had a monopoly on the resources it provides in the above schemes.

Nishibe et al. 11 suggested that a similar re-<sup>w</sup> <sup>x</sup> source pricing mechanism can balance each resource’s usage against others when there exist several resources. In this scheme, the network provider adjusts each resource price based on the demand and utilization levels of that resource, and users select a resource to maximize their surplus based on the resource prices posted by the network provider. However, such a cooperative price adjustment scheme cannot be expected when several network providers compete with one another.

MacKie-Mason and Varian 9 discussed a pricing<sup>w</sup> <sup>x</sup> structure for best-effort type congestible network resources in a competitive market. In a competitive environment, an equilibrium price and capacity will maximize the net social welfare by introducing usage prices in addition to subscription fees. For guaranteed QoS type networks, Rosenschein and Zlotkin <sup>w x</sup> <sup>w x</sup> 13 and Vickrey 15 proposed a stable connection establishment protocol in terms of a competitive telephone service environment. In this protocol, the network provider that submits the lowest bid wins but the price becomes equal to the second lowest bid.

Such literature, however, presents no realistic protocols in detail. Moreover, the telephone service is too simple. In multimedia telecommunications environments, the best bid can vary according to the attributes of user connection requests. This paper therefore proposes a realistic connection establishment protocol involving several competing network providers in a multimedia telecommunications environment. This connection establishment protocol is applicable to all the guaranteed QoS type multiservice networks such as ATM-based networks, multi-rate STM networks, and IP networks employing RSVP 18 for soft-state resource reservation. <sup>w</sup> <sup>x</sup>

## 3. Connection establishment protocol

## 3.1. Connection establishment model for proposed protocol

Fig. 1 shows a connection establishment model for the proposed protocol. In this model, each user can select one of the available network providers by using a user agent in an intelligent terminal. On the other hand, each network provider has a network agent that can select some connection requests from users. User agents and network agents select each other by exchanging messages. Each user agent selects a network agent from the viewpoint of its user’s utility. On the other hand, each network agent selects connection requests from the viewpoint of obtaining profit. No cooperation among network agents exists because the network providers are assumed to be competing against one another. For this reason, the exchange of messages exists only between user agents and network agents.

In the model shown in Fig. 1, each network provider has one optimum path to a destination and each optimum path has a different path cost between network providers. We consider this optimum path cost as a resource cost. Therefore, resource costs become different for individual pairs of a user agent and a network agent. Moreover, each network provider is assumed to have a certain bottleneck bandwidth, and cannot accommodate connection requests exceeding the capacity determined by this bottleneck bandwidth.

## 3.2. Details of connection establishment protocol

The details of the proposed connection establishment protocol are as follows.

Step 1: A user agent broadcasts a connection-request message including the attributes of the connection request to all network agents. As the attributes of the connection request, the following can be considered: required media, required QoS, estimated duration of the connection, and so on.

Step 2: Each network agent calculates the profit rate to be obtained based on the attributes of the connection request. If the profit rate is more than a predetermined threshold, the network agent returns a bid message including information on its idle bandwidth capacity and connection price to the user agent.

![](/api/attachments/ECM2PYE6/fulltext/images/b6f6ac19abaaf99a11427dca3f5cb473aa4e467807ca5508e730fd57e0afd3ae.jpg)  
Fig. 1. Connection establishment model for proposed protocol.

Step 3: The user agent calculates a utility value based on the information received from various network agents. Then it selects the best network agent, which maximizes this utility value and has a certain idle bandwidth capacity, and sends an award message to that network agent. If several network agents can maximize the utility value, the user agent selects the network agent having the maximum idle bandwidth capacity among them because that network agent will most surely admit the connection request.

Step 4: Each network agent establishes a requested connection when it receives an award message, and returns an award-acknowledgment message to the user agent.

In this negotiation scheme, mutual selection by a network agent and a user agent can be achieved in Steps 2 and 3. Connection requests in which no network agent returns a bid message are lost. Connection requests are also lost when a network agent fails to establish a requested connection in Step 4.

In this paper, the profit rate of the network is calculated as follows.

$$
\begin{array}{r l} \text { Profit   rate } & = (\text { Total   profit }) / (\text { Needed   bandwidth }) \\ & = ((\text { Connection   price }) - (\text { Resource   cost })) \\ & / (\text { Needed   bandwidth }) \end{array}
$$

Here, the resource cost indicates the path cost to the destination.

The user’s utility is calculated as follows. User’s utility

<sup>s</sup>Sum of utility values for individual streams that can be connected using a network agent

<sup>s</sup>Ý<sub>Ž</sub> Ž . Request intensity value to each stream

<sup>y</sup>Ž . Price for each stream <sub>.</sub>

In this paper, it is assumed that one multimedia connection consists of several information streams. Here, each stream corresponds to one coding layer of one information medium. Each communication user allocates a request intensity value to each stream according to the strength of the connection demand for that stream 14,19 . For example, a user who <sup>w</sup> <sup>x</sup> strongly requires high quality will allocate a relatively large request intensity value to the stream corresponding to the high coding layer. On the other hand, a user who does not require high quality will allocate a relatively small request intensity value to the stream corresponding to the high coding layer. The utility value in the above expression indicates the total degree of user satisfaction to each connection.

Fig. 2 is a message sequence chart of the proposed protocol. In the proposed protocol, one round trip of a message is added to the conventional connection establishment procedures. Therefore, the connection establishment delay may increase in the proposed protocol. The process timing in each network agent may not be synchronized. Fig. 2 indicates the start timing of a process in each network agent by a short vertical line. At this timing, each network agent begins to calculate its profit rate and returns bid messages to user agents. The start interval of processing shown in Fig. 2 corresponds to the interval at which each network agent begins the calculation and returns bid messages. The waiting time for receiving these bid messages shown in Fig. 2 corresponds to the interval from the broadcast of connection-request messages to the timing of calculating the user’s utility.

![](/api/attachments/ECM2PYE6/fulltext/images/a10288b03e03f88730874575fccad72decfc07749aaf65e679763139d5a4e375.jpg)  
Fig. 2. Message sequence chart of proposed protocol.

This waiting time should be set to the sum of the maximum round-trip time of messages and the maximum start interval of processing in the network agents. By setting the waiting time like this, the proposed protocol operates correctly even if the process timing in each network agent is not synchronized against that of others. Moreover, any increase in the connection establishment delay can be reduced by decreasing the start interval of processing in the network agents.

## 4. Evaluation of connection establishment protocol

## 4.1. EÕaluation model

The effectiveness of the proposed protocol is evaluated using computer simulation. The assumed evaluation model is as follows.

Three kinds of information media A, B, and C are considered. Each information medium is encoded to three layers, and these three layers correspond to streams I, II, and III. The number of transferred streams changes according to the required transfer quality of each information medium. Only stream I is transferred when low quality is requested for that medium. Streams I and II are transferred when middle quality is requested for that medium. Streams I, II, and III are transferred when high quality is requested for that medium.

Fig. 3 shows the needed bandwidth and price for each stream. These values are identical for all network providers. In Fig. 3, a user who requests a large bandwidth is given a price discount. In other words, the communication price per unit of bandwidth in media A is lower than that in media C.

<table><tr><td rowspan="2">Media</td><td colspan="3">Streams</td></tr><tr><td>I</td><td>II</td><td>III</td></tr><tr><td>A</td><td>10</td><td>10</td><td>10</td></tr><tr><td>B</td><td>1</td><td>1</td><td>1</td></tr><tr><td>C</td><td>3</td><td>3</td><td>3</td></tr></table>

(a ) Needed bandwidth for each stream

<table><tr><td rowspan="2">Media</td><td colspan="3">Streams</td></tr><tr><td>I</td><td>II</td><td>III</td></tr><tr><td>A</td><td>10</td><td>10</td><td>10</td></tr><tr><td>B</td><td>2</td><td>2</td><td>2</td></tr><tr><td>C</td><td>4</td><td>4</td><td>4</td></tr></table>

(b) Price for each stream  
Fig. 3. Needed bandwidth and price for each stream.

Moreover, the communication price per unit of bandwidth in media C is lower than that in media B.

The probability that stream I is requested is assumed to be 2<sup>r</sup>3 for each information medium. This means that each information medium is requested by a probability 2<sup>r</sup>3. The probability that stream II is requested is assumed to be 2<sup>r</sup>3 under the condition that stream I is requested. In the same way, the probability that stream III is requested is assumed to be 2<sup>r</sup>3 under the condition that stream II is requested. Of course, one connection request always demands at least one stream. As a result, the average bandwidth that a connection request demands becomes 20.5. The request intensity value is allocated to each demanded stream using a random number, under the condition that the maximum utility value becomes 1.0 for every connection request when the price allocation model shown in Fig. 3 is adopted. Of course, the request intensity value for a stream that is not requested is set at zero.

Here, it is assumed that the resource cost per unit of bandwidth is given by a random number between 0.0 and 1.0 for each pair of a user agent and a network agent. The number of network providers Ž . M is fixed at 5, and the bottleneck bandwidth of each network provider is assumed to be 14 000. The arrival process of connection requests is random and the average arrival interval of connection requests is 100 ms. The holding time of connections follows an exponential distribution with a mean of 300 s. At this time, the connection blocking probability becomes 0.001 if each user agent selects a network provider randomly.

Fig. 4 shows the relationship between the connection blocking probability and monitoring period for resource utilization. Here, the threshold for the profit rate is set at zero, and each network agent cannot select appropriate user agents. Therefore, this scheme corresponds to that shown in Ref. 11 . The connec-<sup>w</sup> <sup>x</sup> tion blocking probability indicates the probability that a network agent fails to establish the requested connection in Step 4. The monitoring period for resource utilization indicates the interval at which each network agent measures its resource utilization to return the information on its idle bandwidth capacity in Step 2.

If the monitoring period for resource utilization is sufficiently short, each user agent can determine the present idle bandwidth capacity of each network agent correctly. Therefore, each user agent can certainly select the network agent with the largest idle bandwidth capacity, and the connection blocking probability becomes small. This relationship can also be observed in the state-dependent dynamic routing for telephone networks 12 . As shown in Fig. 4, the <sup>w</sup> <sup>x</sup> connection blocking probability becomes less than 0.001 when the monitoring period is less than 10 s. For this reason, the monitoring period is fixed at 10 s in the following evaluation.

![](/api/attachments/ECM2PYE6/fulltext/images/ee4122fb1953dddc7dac4bdc5c70656caaa74fef255f5d434b03576b48269ad8.jpg)  
Fig. 4. Relationship between connection blocking probability and monitoring period for resource utilization.

4.2. Effect of selection mechanism for network proÕiders

Here, it is assumed that every network provider adopts the price allocation model shown in Fig. 3. In case of monopolistic network provider, its revenue can be maximized using the shadow prices, which increase as the resource utilization rate increases 3 .<sup>w</sup> <sup>x</sup> In other words, the monopolistic network provider should select only connection requests that give a large profit rate, when its resource utilization level is high. However, in case several network providers compete with each other, the probability that a network provider receives an award message becomes low when its resource utilization level is high. It is therefore supposed that competitive network providers should adopt shadow prices, which decrease as the resource utilization rate increases.

The shadow price corresponds to the threshold by which the network provider decides to return a bid message. The optimum values of this threshold are expected to be solved using the Markov decision theory as shown in Ref. 3 . However, a simple<sup>w</sup> <sup>x</sup> functional form of the threshold is assumed in this paper. The threshold for the profit rate is set as shown in Fig. 5. The threshold increases toward its predetermined maximum value 0.7 as the resource utilization rate decreases. The maximum value of the threshold is introduced to prevent the network provider from accepting few connection requests. The values of the profit rate range between 0.0 and 2.0. In this section, it is shown that the threshold for the profit rate should rather decrease as the resource utilization rate increases under the competitive environment.

Fig. 6 shows the obtained profit per network provider and the connection blocking probability when the value of Y changes and the value of X is set at 0.0. As the value of Y becomes larger, the obtained profit increases because each network agent selects only the connection requests that give a larger profit rate to that network agent. On the other hand,

![](/api/attachments/ECM2PYE6/fulltext/images/bee3d6113dbe779c0b518fa96190f7db8bf79b6e681a1a5f1c1600ca48004907.jpg)  
Fig. 5. Threshold for profit rate.

as the value of Y becomes larger, the number of connection requests to which no network agent returns a bid message increases, and therefore the connection blocking probability tends to increase. However, each network agent generally returns a bid message with a higher priority to a user agent requesting a smaller bandwidth, because a connection with a smaller bandwidth tends to give a larger profit rate for the price allocation model shown in Fig. 3.

![](/api/attachments/ECM2PYE6/fulltext/images/dde8fe8f7b7ab8d47219a8df428468632545260b36573406d2da74afb5f8b2a6.jpg)  
Fig. 6. Obtained profit per network provider and connection blocking probability.

Therefore, a user agent that sends an award message will probably require a relatively small bandwidth, and the probability that the network agent fails to establish a requested connection in Step 4 can be reduced. As a conclusion, the connection blocking probability remains less than 0.001 when the value of Y is less than 0.34.

Fig. 7 shows the obtained profit per network provider when the value of X changes and the connection blocking probability is kept at 0.001. Generally speaking, the probability that a network agent receives an award message becomes high when that network agent has a large idle bandwidth. Therefore, the obtained profit can be increased by selecting only those connection requests that give a larger profit rate when the resource utilization is relatively low. In other words, the obtained profit can be improved by increasing the value of X.

However, if the value of X is too large, the probability that no network agent returns a bid mes-

![](/api/attachments/ECM2PYE6/fulltext/images/d394e11eb7aed5995d66e99821c3fed6c55db364ae154d79f8f2d736a32634f5.jpg)  
Fig. 7. Obtained profit per network provider and the value of Y.

<table><tr><td rowspan="2">Media</td><td colspan="3">Streams</td></tr><tr><td>I</td><td>II</td><td>III</td></tr><tr><td>A</td><td>12.2</td><td>10.0</td><td>5.0</td></tr><tr><td>B</td><td>2.4</td><td>2.0</td><td>1.0</td></tr><tr><td>C</td><td>4.9</td><td>4.0</td><td>2.0</td></tr></table>

(a) Price allocation model 1

<table><tr><td rowspan="2">Media</td><td colspan="3">Streams</td></tr><tr><td>I</td><td>II</td><td>III</td></tr><tr><td>A</td><td>14.0</td><td>11.4</td><td>5.7</td></tr><tr><td>B</td><td>1.4</td><td>1.1</td><td>0.6</td></tr><tr><td>C</td><td>4.2</td><td>3.4</td><td>1.7</td></tr></table>

(b) Price allocation model 2

<table><tr><td rowspan="2">Media</td><td colspan="3">Streams</td></tr><tr><td>I</td><td>II</td><td>III</td></tr><tr><td>A</td><td>11.4</td><td>11.4</td><td>11.4</td></tr><tr><td>B</td><td>1.1</td><td>1.1</td><td>1.1</td></tr><tr><td>C</td><td>3.4</td><td>3.4</td><td>3.4</td></tr></table>

(c) Price allocation model 3  
Fig. 8. Various price allocation models.

sage becomes high. Therefore, the obtained profit decreases reversely when the value of X increases too much while the connection blocking probability is kept constant. As is shown in Fig. 7, the obtained profit becomes maximum when the value of X is 5.0 and the value of Y is <sup>y</sup>0.32. In this case, the proposed mechanism for each network provider to select appropriate connection requests gives a 21% improvement in profit, which can be obtained by each network provider.

## 4.3. Effect of selection mechanism for users

Fig. 8 shows various price allocation models. The average price for a connection in these models is identical to that in the model shown in Fig. 3. In model 1, a price discount for connection requests with a large bandwidth also exists in a medium. In model 2, a price discount for a larger bandwidth exists in a medium but pricing proportional to the required bandwidth is adopted between different media. In model 3, pricing proportional to the required bandwidth is adopted both between different media and in one medium. Compared with the price allocation model shown in Fig. 3, model 1 is advantageous to connection requests that demand high quality for each medium. Model 2 is advantageous to connection requests that demand a relatively high quality for a medium requiring a relatively large bandwidth. Model 3 is advantageous to connection requests that demand media with a small bandwidth.

Tables 1 and 2 show results of connection establishment when a network provider with a different price allocation model exists. In those tables, one network provider adopts the model shown in Fig. 8 and the rest adopt the model shown in Fig. 3. The number of connections in Tables 1 and 2 indicates the number of connections accommodated in a network provider. The network profit indicates the profit obtained by a network provider. The user’s utility indicates the utility value obtained by a user. The suffix 1 corresponds to the network provider adopting the model shown in Fig. 8. The suffix 2 corresponds to the network providers adopting the model shown in Fig. 3.

Table 1  
Results of connection establishment when X<sup>s</sup>0.0 and $Y = 0 . 3 4$  
The upper row shows results when users select a network provider randomly.

<table><tr><td>Price allocation model</td><td>Number of connections-1</td><td>Number of connections-2</td><td>User&#x27;s utility-1</td><td>User&#x27;s utility-2</td><td>Average user&#x27;s utility</td><td>Network profit-1</td><td>Network profit-2</td><td>Average network profit</td></tr><tr><td>1</td><td>11 065</td><td>10 734</td><td>0.994</td><td>1.000</td><td>0.999</td><td>166 600</td><td>166 000</td><td>166 100</td></tr><tr><td>2</td><td>11 002</td><td>10 750</td><td>0.989</td><td>1.000</td><td>0.998</td><td>169 000</td><td>164 700</td><td>165 600</td></tr><tr><td>3</td><td>10 502</td><td>10 874</td><td>0.994</td><td>1.000</td><td>0.999</td><td>165 900</td><td>164 500</td><td>164 800</td></tr><tr><td>1</td><td>9410</td><td>11 147</td><td>1.041</td><td>0.999</td><td>1.006</td><td>164 400</td><td>162 700</td><td>163 000</td></tr><tr><td>2</td><td>12 924</td><td>10 269</td><td>1.042</td><td>0.999</td><td>1.009</td><td>170 200</td><td>159 800</td><td>161 900</td></tr><tr><td>3</td><td>20 011</td><td>8497</td><td>1.038</td><td>0.999</td><td>1.013</td><td>173 500</td><td>156 200</td><td>159 700</td></tr></table>

Table 2  
Results of connection establishment when X<sup>s</sup>4.0 and $Y = - 0 . 1 8$

<table><tr><td>Price allocation model</td><td>Number of connections-1</td><td>Number of connections-2</td><td>User&#x27;s utility-1</td><td>User&#x27;s utility-2</td><td>Average user&#x27;s utility</td><td>Network profit-1</td><td>Network profit-2</td><td>Average network profit</td></tr><tr><td>1</td><td>9203</td><td>11 199</td><td>1.019</td><td>0.999</td><td>1.002</td><td>139 200</td><td>174 200</td><td>167 200</td></tr><tr><td>2</td><td>12 276</td><td>10 431</td><td>1.035</td><td>1.000</td><td>1.008</td><td>141 600</td><td>170 000</td><td>164 300</td></tr><tr><td>3</td><td>12 042</td><td>10 489</td><td>1.038</td><td>0.981</td><td>0.994</td><td>130 400</td><td>156 100</td><td>151 000</td></tr></table>

As shown in Table 1, there exists no difference between the results of connection establishment in each network provider when users select a network provider randomly. In particular, the values of ‘‘user’s utility-1’’ and ‘‘user’s utility-2’’ are almost identical around 1.0. On the other hand, the value of ‘‘user’s utility-1’’ increases when a selection mechanism for the users is introduced. This is because the utility values for a certain class of connection requests can be improved by selecting the network provider adopting the price allocation model shown in Fig. 8. The number of connections-1 in Table 1 corresponds to the number of connection requests included in such a class.

The revenue from a connection request decreases in the network provider that adopts the model shown in Fig. 8. However, this network provider can enclose sufficient connection requests, and therefore network profit-1 becomes larger than network profit-2. Though the value of network profit-2 changes according to the bandwidth demanded by the remaining connection requests, network profit-2 also becomes large in every case compared with the case in which no selection mechanism exists for the network provider. As shown in Table 1, the network provider can give users a larger utility and can improve its profit simultaneously by adopting a pricing method different from that of other network providers and by enclosing enough connection requests.

As shown in Table 2, the value of utility-1 becomes larger than 1.0, also in the case the value of X increases. However, in this case, the network provider also bids on a connection request that does not give a large profit rate if its resource utilization rate is relatively high. Therefore, network profit-1 is reduced when the network provider adopts price allocation model 1 or 2 in this case. If the network provider adopts model 3 and its resource utilization rate is low, that network provider bids on only those connection requests that give a larger profit rate and may receive award messages but only from connection requests that demand a small bandwidth. Therefore, the resource utilization rate in such a network provider remains low, and network profit-1 is also reduced when the network provider adopts price allocation model 3. As a conclusion, the network provider should set the value of X small when it improves its profit by adopting a pricing method different from that of other network providers and by enclosing enough connection requests.

## 5. Conclusions

This paper proposed a new connection establishment protocol involving several competing network providers in a multimedia telecommunications environment. This protocol is based on the concept of open competitive bidding and enables mutual selection by users and network providers. Both network providers and users can pursue their own objectives based on their own bidding and awarding strategies under the proposed connection establishment protocol framework. In this paper, a simple bidding strategy for network providers and an example of utility functions for users were presented. Each network provider can improve its profit by adopting this bidding strategy, and each user can improve his<sup>r</sup>her utility by selecting an appropriate network provider based on this utility function. Each network provider can also improve its profit indirectly by adopting a pricing method different from that of other network providers and enclosing enough connection requests.

Analysis on transition and equilibrium states when network providers adopt various rates is left as a future study item. In addition, security mechanisms against agents that may violate this basic protocol framework must be investigated, when this proposed protocol is implemented in the real world.

## Acknowledgements

The author would like to express his gratitude to Dr. B. Komiyama, president of ATR Adaptive Communications Research Laboratories, and Dr. J. Matsuda, Head of Department 1, for their encouragement and helpful discussions throughout the study.

## References

<sup>w</sup> <sup>x</sup> 1 R. Cocchi, S. Shenker, D. Estrin, L. Zhang, Pricing in computer networks: motivation, formulation, and example, IEEE<sup>r</sup>ACM Trans. Networking 1 6 1993 614–627, Dec.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 R. Davis, R.G. Smith, Negotiation as a metaphor for distributed problem solving, Artif. Intell. 20 1 1983 63–109.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 Z. Dziong, L.G. Mason, Call admission and routing in multi-service loss networks, IEEE Trans. Commun. 42 2–4Ž . Ž .1994 2011–2022, Feb.<sup>r</sup>March<sup>r</sup>April.

<sup>w</sup> <sup>x</sup> 4 D. Ferguson, Y. Yemini, C. Nikolaou, Microeconomic algorithm for load balancing in distributed computer systems, in: Proceedings of 8th International Conference on Distributed Computing System,1988, pp. 491–499.

<sup>w</sup> <sup>x</sup> 5 S. Jordan, H. Jiang, Connection establishment in high-speed networks, IEEE J. Select. Areas Commun. 13 7 1995Ž . Ž . 1150–1161, Sept.

<sup>w</sup> <sup>x</sup> 6 F.P. Kelly, On tariffs, policing and admission control for multiservice networks, Oper. Res. Lett. 15 1 1994 1–9.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 S.H. Low, P.P. Varaiya, A new approach to service provisioning in ATM networks, IEEE<sup>r</sup>ACM Trans. Networking 1 Ž . Ž . 5 1993 547–553, Oct.

<sup>w</sup> <sup>x</sup> 8 J.K. MacKie-Mason, H.R. Varian, Economic FAQs about the internet, J. Econ. Perspect. 8 3 1994 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 J.K. MacKie-Mason, H.R. Varian, Pricing congestible net-

work resources, IEEE J. Select. Areas Commun. 13 7Ž . Ž . 1995 1141–1149, Sept.

<sup>w</sup> <sup>x</sup> 10 J. Murphy, L. Murphy, E.C. Posner, Distributed pricing for embedded ATM networks, in: Proc. Int. Teletraffic Congr. Ž . ITC-14 ,1994, pp. 1053–1063.

<sup>w</sup> <sup>x</sup> 11 Y. Nishibe, K. Kuwabara, T. Suda, T. Ishida, Distributed channel allocation in ATM networks, in: Proceedings of GLOBECOM ’93 12.21993, pp. 417–423, Nov.<sup>r</sup>Dec.

12 J. Regnier, W.H. Cameron, State-dependent dynamic traffic management for telephone networks, IEEE Commun. 28 10Ž . Ž . 1990 42–53, Oct.

<sup>w</sup> <sup>x</sup> 13 J.S. Rosenschein, G. Zlotkin, Designing conventions for automated negotiation, AI Mag. 15 3 1994 29–46.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 N. Shacham, J.S. Meditch, An algorithm for optimal multicast of multimedia streams, Proceedings of IEEE Infocom ’94 7a.3 1994 856–864.Ž .

<sup>w</sup> <sup>x</sup> 15 W. Vickrey, Counterspeculation, auctions, and competitive sealed tenders, J. Finance 18 1961 8–37.Ž .

<sup>w</sup> <sup>x</sup> 16 C.A. Waldspurger, T. Hogg, B.A. Huberman, J.O. Kephart, W.S. Stornetta, Spawn: a distributed computational economy, IEEE Trans. Software Eng. 18 2 1992 103–117, Feb.Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 M.P. Wellman, A market-oriented programming environment and its application to distributed multicommodity flow problems, J. Artif. Intell. Res. 1 1993 1–23.Ž .

<sup>w</sup> <sup>x</sup> 18 L. Zhang, S. Deering, D. Estrin, S. Shenker, D. Zappala, RSVP: a new resource reservation protocol, IEEE Network 7 Ž . Ž . 5 1993 8–18, Sept.

<sup>w</sup> <sup>x</sup> 19 G. Zlotkin, J.S. Rosenschein, Compromise in negotiation: exploiting worth functions over states, Artif. Intell. 84 1996 Ž . 151–176.

![](/api/attachments/ECM2PYE6/fulltext/images/f42e3d9f12f7293d7ddc6536cd8d65bf8e9e1b165c8c3686f49d4345f4a44b8b.jpg)

Nagao Ogino received his BE, ME, and Dr. Eng. degrees in Electronic Engineering from the University of Tokyo, Japan, in 1977, 1979 and 1982, respectively. He joined the Research and Development Laboratories of Kokusai Denshin Denwa KDD in 1982, and has beenŽ . engaged in research on switching systems and traffic control in ATM networks, service creation and execution methodologies in Intelligent Networks, and telecommunication software mea-

surement. He is currently a supervisor of Department 1 at ATR Adaptive Communications Research Laboratories. His current research interests include adaptive quality control in multimedia telecommunications and multi-agent based telecommunication systems.
