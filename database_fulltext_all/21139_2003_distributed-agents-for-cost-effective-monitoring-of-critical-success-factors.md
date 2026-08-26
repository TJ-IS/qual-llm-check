---
otero_id: 21139
otero_key: "EAVC6BXX"
title: "Distributed agents for cost-effective monitoring of critical success factors"
authors: "Rey-Long Liu; Yun-Ling Lu"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00113-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Distributed agents for cost-effective monitoring of critical success factors

Rey-Long Liu\*, Yun-Ling Lu

Department of Information Management, Chung Hua University, HsinChu, Taiwan, ROC

Accepted 1 April 2002

## Abstract

Business managers should promptly respond to important events (e.g. exceptions) that happen on a set of critical success factors (CSF). A CSF monitoring system is thus essential in capturing the events for the managers. It monitors the information items concerning the CSF. Once an update is detected, critical events may be validated, logged, and signaled for the manager. Since CSF monitoring is often time-critical and mission-critical, a CSF monitoring system should be cost-effective: It should detect updates in a timely, complete, and robust manner without incurring heavy loading to related information servers (e.g. query overheads) and the Intranet (e.g. communication overheads). To achieve that, the monitoring tasks should be properly distributed and coordinated on the Intranet. We propose a multiagent CSF monitoring paradigm, CSFMonitor, in which distributed agents share a collective goal of cost-effective CSF monitoring. An experiment on monitoring real-world financial CSF is conducted. The delivery of CSFMonitor to businesses may robustly provide more complete and timelier information without causing serious problems to the original information processing in businesses. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Critical success factors; Cost-effective monitoring; Distributed agents; Communication overheads; Query overheads

## 1. Introduction

Management by exceptions (MBE) has been widely adopted in business administration. It suggests managers to promptly respond to the exceptions happening on a predefined set of critical success factors (CSF), without being involved with the tedious activities of monitoring and validation [3,16]. CSF monitoring is thus essential to the realization of MBE. Conceptually, a CSF consists of a critical information item and a validation procedure. The critical information item may be maintained by internal or external entities (e.g. database systems, web servers, and file servers) [14] and updated at any time [32]. Once an update on the information item is detected, the validation procedure is triggered to determine whether an exception occurs, and if so, corresponding managers are notified. By promptly responding to the exceptions happening on the CSF, the managers may maximize the wealth of their businesses.

## 1.1. Problem definition and motivation

In this paper, we explore how multiagent systems may support CSF monitoring so that managers may promptly respond to a higher percentage of exceptions. CSF monitoring is actually a kind of information monitoring, since exceptions may be detected only by monitoring the updates of their corresponding information items. However, since CSF monitoring is often more time-critical and mission-critical, it is associated with particular requirements on timely, complete, and robust (fault tolerant) update detection. That is, a CSF monitoring system should detect a higher percentage of updates in a timely manner without being crashed by any single fault or failure.

The requirements significantly increase the cost of CSF monitoring. We thus focus on the design of multiagent systems for cost-effective CSF monitoring, which aims to maximize the quality but minimize the cost of CSF monitoring. On the quality part, we are concerned with the timeliness, completeness, and robustness of update detection. On the cost part, we are concerned with the loading incurred by the monitor to the related information servers, the Intranet, and the Internet. The amount of the cost should be properly controlled; otherwise, the delivery of the system will make all the servers and the Intranet exhausted, which, in turn, deteriorates the performance of original information processing in businesses [23]. Similar situations may be found in various domains such as information inquiry through the Internet [21]. A cost-effective CSF monitor should maximize timeliness, completeness, and robustness of update detection, while simultaneously minimize the cost it incurs.

## 1.2. Major challenge

Major challenges of cost-effective CSF monitoring lie on the trade-off between the quality concerns and the cost concern. For example, timely and complete monitoring often calls for frequent inquiry to information servers, which will incur heavy loading (cost) to the servers and the Intranet. As another example, consider robust monitoring, which may be achieved by distributing the monitoring tasks (i.e. the tasks of monitoring individual CSF) to multiple machines. In that case, a fault on a machine will not cause serious problems to CSF monitoring. However, intensive communications among the distributed tasks should be avoided for not incurring a heavy burden to the Intranet.

Previous information monitoring techniques did not tackle the challenges, making them unsuitable for CSF monitoring. They often relied on a centralized site to monitor all information items [9,24,26,27,30]. This method cannot be robust, since a fault on the centralized site could stop all monitoring tasks, and thus cause a great loss to the managers. Moreover, previous techniques often predefined a frequency to periodically check for information updates. This method could not fulfill the requirements of CSF monitoring either, since critical information items may be updated at any time. They may even be updated frequently at a particular time (e.g. the daytime of some particular days in a month) but infrequently at another time. Since periodical monitoring does not estimate the timing of information updates, it may waste a great amount of efforts without finding information updates. On the other hand, the timing of information updates cannot be hypothesized by traditional forecasting techniques (e.g. moving average) either, since the monitoring system cannot know the happening time of the updates. (Note: Only the servers that maintain the information items may know the happening time. Unfortunately, in most cases, they cannot provide such information to the monitoring system.) No reliable history data may be sampled in order to forecast the happening time of the next update.

We tackle the challenges by delegating a monitoring task to an agent, which may be distributed to various sites on the Intranet. The distributed setting contributes three main benefits to CSF monitoring: load balancing, bandwidth saving, and robust monitoring. This is because the agents may be distributed according to the loading (for load balancing) and the location (for bandwidth saving) of each site. A fault on a site will not stop all the monitoring tasks (i.e. robust monitoring). Therefore, under such a distributed setting, we explore how individual agents may learn to monitor their CSF and collaborate with each other so that a limited amount of resources (i.e. query transactions and Intranet bandwidths) may be directed to those agents that are more likely to detect information updates. The amount of the communications required for the collaboration should be controlled as well, since intensive communications among the distributed agents may cause serious problems to both the efficiency of the collaboration and the loading of the Intranet.

## 1.3. Research method and organization of the paper

We first survey the environments and requirements of distributed cost-effective CSF monitoring for decision support (ref. Section 2). Based on the requirements, a multiagent paradigm CSFMonitor is developed (ref. Section 3). Each agent learns to properly work with each other to achieve cost-effective CSF monitoring. Cost-effectiveness of CSFMonitor is investigated in an experiment that simulates real-world environments of financial CSF (ref. Section 4). In the experiment, CSFMonitor significantly outperforms state-of-the-art monitoring techniques. The framework is then comprehensively evaluated from the viewpoints of its related work and future work (ref. Sections 5 and 6). We finally conclude that effective decision making may be supported by the delivery of CSFMonitor, which aims to robustly and promptly report more events happening on CSF without causing problems to original information processing in businesses.

## 2. Distributed cost-effective CSF monitoring

Distributed cost-effective CSF monitoring aims to achieve cost-bounded, timely, complete, and robust monitoring of CSF for business managers.

## 2.1. The environment

Fig. 1 illustrates the common environment in which distributed agents provide the services of CSF monitoring to managers. Businesses often rely on various kinds of information systems to support daily business operations through the Intranet. The systems may range from information servers (e.g. database management systems, file servers, web servers, etc.) to management information systems. They are often located on different Intranet segments, through which they provide and maintain a great amount of critical information for internal control and management. On the other hand, external information (e.g. information form competitors, governments, partners, and information service providers) accessed through the Internet is essential for businesses as well. It helps the businesses to fit into the dynamic environments.

Critical internal/external information items concerning the CSF for the managers are often collected by information consoles such as executive information systems. The information items may be updated at any time by their corresponding information servers/systems. For managers to conduct effective decision making, updates of the information items should be collected in a comprehensive and timely manner. Therefore, autonomous agents for monitoring the information items are helpful for the managers. Once an update is detected, critical events may be validated, logged, and signaled for the manager.

To get the benefits of fault tolerance, load balancing, and bandwidth saving, the agents may be properly distributed to different sites on the Intranet. For example, to save network bandwidth, the agent that monitors an item may be distributed to the site near (e.g. on the same Intranet segment) to the server that maintains the item. To balance loading, the agent may be distributed to low-loading sites as well. In both cases, a fault on a site will not cause serious problems to the whole monitoring system, making the system more robust. The distributed agents should work together to monitor CSF for the managers, since the resource (e.g. loading of the information servers and the Intranet) for them to conduct their tasks is often limited and globally shared in the business.

![](/api/attachments/EAVC6BXX/fulltext/images/266209559a9f56ad2484d2c74ed56157efa486601fdc0df587edd069b03ab267.jpg)  
Fig. 1. Environment of distributed CSF monitoring.

## 2.2. Major concerns

Cost-effective CSF monitoring is motivated by the needs of the managers and the delivery of the system. Its major concerns fall into two categories: quality and cost.

## 2.2.1. Quality of CSF monitoring

Table 1 defines the quality concerns of CSF monitoring. Timeliness and completeness are two major quality concerns. Timeliness measures how timely the update detection is. A CSF monitoring system is said to be timelier in update detection if it may detect updates of CSF sooner after they happen. A timely monitoring system may validate and report events promptly so that managers may have more time to respond to the events. On the other hand, completeness measures how complete the update detection is. A monitoring system is said to be more complete in update detection if it may detect a higher percentage of updates that happened. Complete update detection may help managers to capture more events that happen on the CSF.

## 2.2.2. Cost of CSF monitoring

Table 2 defines the cost concerns of CSF monitoring. Query effectiveness and communication effectiveness are two major cost concerns. Query effectiveness measures how effective the query transactions are. A monitoring system is said to be more effective in querying information servers if it may detect more information updates by querying the servers fewer times. In that case, the loading incurred on the servers effectively contributes to update detection. On the other hand, communication effectiveness measures how effective the agent communication is. A multiagent monitoring system is said to be more effective in agent communication if the agents may be coordinated to detect more updates by using fewer communications. In that case, the agents may work together to detect more updates without incurring heavy loading to the Intranet.

<table><tr><td>Table 1Quality concerns of CSF monitoring</td></tr><tr><td>Timeliness(A) Time Delay=Σ {Time of being detected – Time of happening}, for all detected updates(B) Average Time Delay=Time Delay/Number of updates detected(C) Timeliness = 1/Average Time DelayCompleteness=Number of updates detected/Total number of updates that happened</td></tr></table>

Table 2

<table><tr><td>Table 2Cost concerns of CSF monitoring</td></tr><tr><td>Query Effectiveness(A) Total Query Transactions=Σ (Qk) for all CSFk, whereQk= Times of querying the related information server for CSFk(B) Query effectiveness=Number of updates detected/Total Query Transactions</td></tr><tr><td>Communication Effectiveness(A) Total Communication Overhead=Σ (Ck) for all agent k, whereCk= Number of messages sent to and received from agent k(B) Communication Effectiveness=Number of updates detected/Total Communication Overhead</td></tr></table>

Obviously, there exist trade-offs among the concerns, although they are all motivated by the practical needs of managers. For example, timely and complete monitoring often requires more frequent inquiry to information servers, which may deteriorate query effectiveness. As another example, consider the trade-off between query effectiveness and communication effectiveness. To effectively query the information servers, the agents often need to intensively communicate with each other so that only those agents that are likely to detect updates may conduct their tasks (i.e. check for updates). Since the concerns reflect the needs of managers, a monitoring system should simultaneously perform well in terms of all the concerns.

## 3. Distributed agents for cost-effective CSF monitoring

A multiagent model CSFMonitor is developed for fulfilling the requirements of distributed cost-effective CSF monitoring.

![](/api/attachments/EAVC6BXX/fulltext/images/dc1810b9349cffd07ef6bc9fa558f580a06f9c2e212104a84aab24502349348f.jpg)  
Fig. 2. Overview of CSFMonitor.

## 3.1. Overview

Fig. 2 illustrates an overview of CSFMonitor. The agents are autonomous and hosted in different sites on the Intranet. The hosting policy may be set up by the considerations of load balancing, fault tolerance, and bandwidth saving. An agent monitors an information item (either internal or external) concerning a CSF. It dynamically estimates its need of resource consumption and accordingly issues requests to the coordinator, which is on the Intranet as well. Given an upper bound $\mu$ of resource consumption (i.e. the maximum frequency of querying the related information servers), the coordinator properly allocates resources to the agents by trying to satisfy the needs of the agents.

Obviously, the upper bound $\mu$ is a global constraint to CSF monitoring. Its existence is based on the practical concerns of delivering the multiagent system to businesses. Since each agent conducts its task by querying related information servers through the Intranet (and the gateway to the Internet if external information servers are queried), the upper bound $\mu$ facilitates the overall control of the extra loading that may be incurred on the servers and the Intranet. In practice, the upper bound may be dynamically adjusted based on current loading of the servers and the Intranet.

## 3.2. Behavior of the coordinator

Table 3 defines the behavior of the coordinator. The coordinator keeps a resource pool to accumulate the resource (i.e. frequency of querying the related servers) that may be allocated to the agents. Since the coordinator initially allocates the upper bound $\mu$ to the agents uniformly (ref. Step (1)), the resource pool is initially empty (ref. Step (2)). The coordinator is then ready to receive and grant requests from the agents. Each agent may issue two types of requests: requests for returning resource (ref. Step (3)) and requests for asking additional resource (ref. Step (4)). Upon receiving a request from an agent, the coordinator tries to satisfy the agent’s need and accordingly adjusts the resource pool (ref. Steps (3.1), (4.1.2), and (4.2.2)). Thus, the multiagent system may adapt to the environments by allocating resource to those agents that really need the resource to conduct their tasks.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 3
Behavior of the coordinator

(1) Uniformly allocate to each agent the maximum frequency  $\mu$  of querying information servers;
(2) ResourcePool = empty;
Repeat
(3) If there is an agent P returning an amount  $R_{in}$  of frequency,
(3.1) ResourcePool = ResourcePool +  $R_{in}$ ;
(4) If there is an agent Q asking for an additional amount  $R_{out}$  of frequency,
(4.1) If ResourcePool &gt;=  $R_{out}$ ,
(4.1.1) Satisfy Q's need (i.e. give Q an additional frequency  $R_{out}$ );
(4.1.2) ResourcePool = ResourcePool -  $R_{out}$ ;
(4.2) Else
(4.2.1) Partially satisfy Q's need (i.e. give Q all what ResourcePool remains);
(4.2.2) ResourcePool = empty;
Until the system is terminated
</div>

## 3.3. Behavior of each agent monitor

Table 4 defines the behavior of each autonomous agent. Upon receiving an initial frequency d from the coordinator, each agent periodically checks its corresponding CSF (ref. Step (2)). Once an update is detected (ref. Step (2.2)), critical events (e.g. exceptions) are validated and handled (e.g. event logging and user notification). Thus, the frequency d reflects the maximum amount of the resource that may be consumed by the agent.

Each autonomous agent should estimate its resource need by following a protocol recognized by the distributed agent society. The estimation is based on whether current d is enough for the agent to detect information updates. When the agent finds updates in two consecutive trials, it issues a request to the coordinator for a higher d (ref. Step (2.2.2)). In that case, the agent might require more resource for monitoring the CSF. Based on the request, the coordinator may try to satisfy the agent’s need (ref. Step (4) in Table 3). On the other hand, when the agent fails to find updates in two consecutive trials, it notifies the coordinator for releasing resource to other agents (ref. Step (2.3.1) in Table 4). Thus, each agent may adapt to the update behavior of the CSF being monitored. When the CSF is updated frequently (infrequently) at a particular period, the agent will inquire (release) resource accordingly. Thus, the agents collaborate together to monitor CSF for the manager, although they are autonomous and distributed in different sites.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 4
Behavior of each agent

(1) Accept from the coordinator an initial frequency  $\delta$  for querying the information server;
Repeat
(2) If the CSF should be checked now (according to  $\delta$ )
(2.1) Query the information server (i.e. check the information item corresponding to the CSF);
(2.2) If an update is detected,
(2.2.1) Validate whether a critical event (e.g. exception) occurs, and if so, handle the event;
(2.2.2) If an update was detected last time too,
(2.2.2.1) Ask the coordinator for an additional percentage  $\alpha$  of frequency;
(2.2.2.2)  $\delta = \delta + Frequency$  got from the coordinator;
(2.3) Else
(2.3.1) If an update was not detected last time either,
(2.3.1.1) Return a percentage  $\beta$  of frequency to the coordinator;
(2.3.1.2)  $\delta = \delta - Frequency$  returned to the coordinator;
Until the agent is terminated
</div>

The additional percentage of the resource inquired (i.e. a) and the percentage of the resource returned (i.e. b) are two system parameters. To achieve the resource redistribution, communications between the coordinator and each agent are required. They are conducted only when the agent tries to adjust its resource consumption level (i.e. the frequency d). Note that when asking for more resource, two communications are required: One is from the agent (i.e. an inquiry request; ref. Step (2.2.2) in Table 4) and the other is from the coordinator (i.e. a granting signal; ref. Step (4) in Table 3). On the other hand, when returning resource, only one communication is required (ref. Step (2.3.1) in Table 4). The coordinator does not need to reply the agent with any message (ref. Step (3) in Table 3).

## 4. Experiment

Experiments, which simulated real-world environments for financial decision support, were designed to investigate the performance of CSFMonitor. The experiments were conducted on PCs with independent and concurrent processes of two types. One was for simulating the update behaviors of CSF (ref. Section 4.1); while the other was for simulating the operations of various kinds of monitoring systems (ref. Section 4.2).

## 4.1. The CSF to be monitored

Table 5 illustrates a tree of common categories of CSF in financial management. It was derived from a prototype system running on the Internet [25]. By browsing through the category tree, managers could specify their CSF to be monitored. In this experiment, we used a simulated environment to investigate the performance of CSFMonitor. This is because the measurements of timeliness and completeness require the information of when and how many updates

Table 5 Hierarchical taxonomy of the financial CSF to be monitored (1) Operating and Tax Environment Financial Institutions Commercial Banks Credit Unions Farmers’ Credit Unions Insurance Companies Mutual Funds Investment and Trust Companies Bills Finance Companies Broker Firms Organized Exchange Taxes Income Tax Business Tax Commodity Tax Customs Duties Government (2) Investment Long-term Investments Stock Options Stocks—TWEX Stocks, OTC Stocks Futures—TWEX Stock Index Futures, SIMEX Morgan Taiwan Stock Index Futures Mutual Funds—Equity Funds, Bond Funds, Balanced Funds, Open-end Fund Bonds—Government Bonds, Bank Debentures, Corporate Bonds Short-term Investment Foreign Exchange Treasury Bills Commercial Papers—Primary market, Secondary market (3) Financing Loan Interest Rates (4) International Finance Foreign Exchange Rate—NTD to Foreign Exchange, USD to Foreign Exchange Foreign Stock Markets Foreign Interest Rates—FX Demand Deposit Interest Rate, FX Time Deposit Interest Rate Foreign Mutual Funds (5) Law Entity-related Business Laws Accounting-related Business Laws Management-related Business Laws Consumer Protection Laws

actually happened. In the simulated environment, realworld update behaviors of the information items being monitored were simulated. We could thus have adequate data to compute the performance measurements.

We set up 100 CSF and simulated their real-world update behaviors. The 100 CSF were uniformly selected from the web sites of the five categories (i.e. 20 web sites from each category). A survey was conducted for 2 months to identify their update behaviors. Table 6 summarizes the result of the survey. The items whose update intervals were very long mainly came from the 5th category (i.e. law). They were seldom updated in real-world environments. The items whose update intervals were less than 1 h mainly came from the 4th category (i.e. international finance). In addition, there were two items (one was about stocks and the other was about futures) whose update intervals were ‘‘alternating’’ in the sense that they were updated frequently at one time (e.g. one time per minute from 8:30 to 12:00) but not at other times.

There were two update modes identified: periodical update and exponential update. The former was adopted for those items that were updated for every fixed period, while the latter was adopted for those items whose update frequencies were relatively rough. In exponential update, an item was updated in the time intervals with the exponential probability distribution. The probability density function of an exponential distribution is $f ( x ) = \lambda \mathrm { e } ^ { - \lambda x }$ , where $x \geq 0$ and k is the average update frequency of an information item (k>0). Thus, given k, the probability of the item being updated in time interval c may be $P ( X \leq \gamma ) = 1 - \mathtt { e } ^ { - \lambda \gamma }$ . Most of the CSF followed the exponential update mode (71 items followed the exponential update mode, while 29 items followed the periodical update model). Since most items had update intervals less than 2 months, we simulated the update behaviors of the CSF for 2 months (i.e. 61 days or 5 270 400 s). In the simulation period, only 12 CSF were not updated, among which nine had very long update intervals (i.e. many years).

Survey of the update behaviors of the CSF being monitored

<table><tr><td rowspan="2">Update interval</td><td colspan="2">Update mode</td></tr><tr><td>Periodical update</td><td>Exponential update</td></tr><tr><td>0–1 h</td><td>2</td><td>9</td></tr><tr><td>1 h–1 day</td><td>22</td><td>4</td></tr><tr><td>1 day–2 days</td><td>0</td><td>20</td></tr><tr><td>2 days–1 month</td><td>0</td><td>23</td></tr><tr><td>1 month–2 months</td><td>0</td><td>6</td></tr><tr><td>More than 2 months</td><td>3</td><td>0</td></tr><tr><td>Very long</td><td>0</td><td>9</td></tr><tr><td>Alternating</td><td>2</td><td>0</td></tr><tr><td>Total</td><td>29</td><td>71</td></tr></table>

The other CSF were updated a huge number of times. Thus, the simulation has covered almost all the daily updates of the CSF for common managers.

## 4.2. The monitoring systems to be evaluated

To our survey, random monitors (RandomM), periodical monitors (PeriodicalM), and adaptive multiagent monitors (ACAIM [24]) may represent most state-of-the-art and commercialized monitors. Therefore, they served as the baseline systems for performance evaluation of CSFMonitor.

The setting of CSFMonitor was based on a preliminary investigation of its performance under different settings of a and b (ref. each agent’s behavior defined in Table 4). We experimented six versions of CSFMonitor with (a, b) being set to be (10%, 10%), (20%, 10%), (10%, 20%), (30%, 10%), (10%, 30%), and (20%, 20%), respectively. The resource upper bound l was set to be 1 query per 10 s. Table 7 summarizes the performance of the six versions in 1 month of simulation. Generally, the performance differences were not very significant, and no one could outperform the others in terms of all criteria. Setting a>b could generally achieve a better performance in communication effectiveness, but a poorer performance in timeliness (ref. CSFMonitor(20%, 10%) vs. CSFMonitor(10%, 20%), and CSFMonitor(30%, 10%) vs. CSFMonitor(10%, 30%)). This was because, when each agent asked more but returned less resource, it would be more difficult for the other agents to acquire enough resource to adapt to the environment in a prompt way, leading to a poorer performance in timeliness. On the other hand, when each agent asked less but returned more resource, it would require more communications to get enough resource, leading to a poorer performance in communication effectiveness.

As noted above, no one could completely outperform the others and CSFMonitor(20%, 20%) demonstrated medium performances among the six versions. Therefore, without loss of objectivity, we adopted CSFMonitor(20%, 20%) for performance comparisons with the baseline systems. The simulation for the performance comparisons was conducted for 2 months. The resource upper bound l was set to be one query per 10 s (and hence CSFMonitor was allowed to conduct at most 527 040 queries). All the experiments were repeated for 30 times to investigate the standard deviations and significance of the performance comparisons.

To have a similar basis for performance comparison, RandomM was allowed to conduct the same maximum number (i.e. 527040) of queries as CSFMonitor. For every 10 s, it randomly allowed an agent to query an information server. Therefore, in each session of random granting, only one communication (from the coordinator to the selected agent) was required. Random monitors are often employed when there is no exact idea of how to monitor CSF.

PeriodicalM is a periodical monitor, which allowed each agent to query a server periodically. It associated each agent with a predefined frequency. Each agent was thus periodically informed to query a server based on the frequency. Therefore, in each session of periodical granting, only one communication (from the coordinator to the agent) was required. Similarly, to have a similar number of queries conducted, the predefined frequencies of the agents were randomly set between 50 and 5000 s (PeriodicalM actually conducted an average number 478 600 of queries in the experiments). Periodical monitors are often employed when the frequencies of checking the CSF are available.

ACAIM is an adaptive monitor as well [24]. By intensive communications among the agents and the coordinator, it has been shown to be effective in information monitoring. Each agent in ACAIM was adaptive in the sense that it could estimate the urgency of its request based on the current update behavior of the information being monitored. A request for querying an information server was said to be more urgent if the agent felt that an update was going to happen.

Performance of CSFMonitor with different settings

<table><tr><td></td><td>Timeliness</td><td>Completeness</td><td>Query effectiveness</td><td>Communication effectiveness</td></tr><tr><td>CSFMonitor (10%, 10%)</td><td>0.01377</td><td>0.51406</td><td>0.88895</td><td>2.61968</td></tr><tr><td>CSFMonitor (20%, 10%)</td><td>0.01378</td><td>0.52220</td><td>0.88280</td><td>3.09471</td></tr><tr><td>CSFMonitor (10%, 20%)</td><td>0.01762</td><td>0.52513</td><td>0.90697</td><td>2.05869</td></tr><tr><td>CSFMonitor (30%, 10%)</td><td>0.01834</td><td>0.52787</td><td>0.88607</td><td>3.30603</td></tr><tr><td>CSFMonitor (10%, 30%)</td><td>0.02193</td><td>0.52448</td><td>0.90823</td><td>1.37478</td></tr><tr><td>CSFMonitor (20%, 20%)</td><td>0.01926</td><td>0.53729</td><td>0.89712</td><td>2.55354</td></tr></table>

Table 8  
Average performance of all monitoring systems

<table><tr><td></td><td>RandomM</td><td>PeriodicalM</td><td>ACAIM</td><td>CSFMonitor</td><td>Improvement (%)</td></tr><tr><td>Timeliness</td><td>0.00592</td><td>0.00560</td><td>0.01793</td><td>0.01742</td><td>77</td></tr><tr><td>Completeness</td><td>0.06700</td><td>0.05831</td><td>0.47316</td><td>0.53069</td><td>166</td></tr><tr><td>Query effectiveness</td><td>0.10037</td><td>0.09943</td><td>0.70964</td><td>0.91349</td><td>201</td></tr><tr><td>Communication effectiveness</td><td>0.10037</td><td>0.09943</td><td>0.21676</td><td>2.85494</td><td>1956</td></tr></table>

The coordinator granted a request from the agents based on the urgencies of the requests. Therefore, in each granting process, T + 1 requests were required, where T was the number of agents that issued requests. In the experiment, ACAIM was allowed to conduct the same maximum number (i.e. 527040) of queries as well. ACAIM was experimented for investigating whether CSFMonitor could achieve similar performance without relying on intensive communications. This is particularly important for CSF monitoring in which agents are distributed on the Intranet.

![](/api/attachments/EAVC6BXX/fulltext/images/c63c88eb7fe9b7d9c4afb6220a18e3b6866ddf96ce67e9b0f9b52439e01c21f5.jpg)  
Fig. 3. Experimental results

## 4.3. Results and analysis

Table 8 summarizes the average performance of the monitoring systems in the 30 runs of experiments. As ACAIM, PeriodicalM, and RandomM represent stateof-the-art and commercialized monitoring strategies, CSFMonitor significantly improves the cost-effectiveness of CSF monitoring. When compared with the average performance of the baseline systems, it demonstrated 77% improvement in timeliness, 166% improvement in completeness, 201% improvement in query effectiveness, and 1956% improvement in communication effectiveness. The improvements were contributed by the agents that actively adapted to the environment and, based on the adaptation, communicated for resource redistribution only when necessary.

Fig. 3 illustrates the experimental results in course of the 2-month simulation. The results were obtained by averaging the results of the 30 repeated runs as well. They showed that, in the course of the simulation, CSFMonitor and ACAIM outperformed the other two systems in all criteria. CSFMonitor was significantly better than all other systems in communication effectiveness.

Table 9 summarizes standard deviations of the results. A hypothesis test (with the significance level being set to 0.05) showed that the improvements of CSFMonitor over each baseline system were significant, except for the improvement in timeliness over ACAIM. As shown in Table 8, ACAIM actually outperformed CSFMonitor in timeliness. However, the performance difference was not significant. This indicates that CSFMonitor may achieve better communication effectiveness without significantly sacrificing the timeliness of monitoring. It also implies that CSFMonitor may reduce intensive communications without sacrificing the quality of coordination.

## 5. Discussion

The agents in CSFMonitor support distributed cost-effective CSF monitoring by a simple and effective coordination protocol. In this section, we discuss major contributions of the framework with respect to its related work.

## 5.1. Information gathering

Managers require the information gathered from internal and external sources [14,32]. Since managers often have difficulties in capturing useful information all the time by themselves, agent technology was introduced [31] and facilitated various applications such as electronic commerce [7,17]. However, previous information gathering techniques focused on intelligently locating information of interest (e.g. personalized [8] and cooperative [11,22] ways of searching for information). CSFMonitor extends the idea by gathering timely information concerning a selected set of information items. It explores the timely, complete, and robust way of monitoring (rather than locating) critical information, which is essential for the managers to promptly respond to their CSF.

## 5.2. Information monitoring

CSFMonitor explores how to monitor information (in contrast to what information to monitor [28]) for providing timely information to managers. Some commercialized information monitoring packages required the information updating systems (e.g. spreadsheet editors such as Excel) to notify the agents of the updates that happened (e.g. using the Dynamic Data Exchange technique, DDE [27]). However, most information systems currently running on the Internet and the Intranet were not originally designed with the functionality of update notification. A monitor continuously waiting for update notification cannot satisfy the practical needs of information monitoring.

Standard deviations of the results

<table><tr><td></td><td>RandomM</td><td>PeriodicalM</td><td>ACAIM</td><td>CSFMonitor</td></tr><tr><td>Timeliness</td><td>0.000236</td><td>0.001876</td><td>0.001381</td><td>0.001405</td></tr><tr><td>Completeness</td><td>0.001137</td><td>0.026757</td><td>0.003697</td><td>0.006617</td></tr><tr><td>Query effectiveness</td><td>0.001672</td><td>0.046748</td><td>0.004519</td><td>0.004995</td></tr><tr><td>Communication effectiveness</td><td>0.001672</td><td>0.046747</td><td>0.008878</td><td>0.229879</td></tr></table>

Therefore, other techniques were developed. They allowed the monitor took an active role in information monitoring. The monitor actively checked for updates by querying the sites that hosted the information items of interest. Centralized and periodical monitoring was often employed in the techniques [9,24,26,27,30]. All the monitoring tasks were conducted by a single machine, which predefined a frequency to periodically check for information updates.

However, centralized monitoring cannot be robust, since a fault on the centralized site could stop all monitoring tasks, and thus cause a great loss to the managers. CSFMonitor may coordinate a set of distributed agents (tasks) without incurring a heavy communication cost. Distributed hosting of the agents is of particular importance for CSF monitoring. In addition to robust monitoring, it contributes the benefits of load balancing and bandwidth saving. This is because the agents may be distributed according to the loading (i.e. for load balancing) and the location (i.e. for bandwidth saving) of each site. An agent may be distributed to a low-loading site that is near to the site (or even the site per se) that maintains the information being monitored. In any cases, a fault on a site will not stop all the monitoring tasks (even the coordinator is crashed, each agent may continue to monitor its CSF). Dynamic redistribution of the agents is an interesting future research direction to be discussed in Section 6.

Furthermore, periodical monitoring could not fulfill the requirements of CSF monitoring either, since critical information items may be updated at any time. A great amount of efforts could thus be wasted without finding information updates. On the other hand, to estimate the timing of information updates, traditional forecasting techniques (e.g. moving average) is not feasible either, since no reliable history data may be sampled for forecasting the happening time of the next update (i.e. the monitoring system cannot know the happening time of previous updates). Therefore, adaptive information monitoring has been explored in previous studies as well [24]. It was shown that, by intensive communications, agents could detect information updates in a timely manner. However, the technique was not suitable for distributed monitoring, since the intensive communications may cause a heavy loading to the Intranet. CSFMonitor demonstrates a simple and effective way to coordinate the distributed agents without relying on intensive communications.

## 5.3. Adaptive decision support systems (DSS)

The adaptability of DSS has been as a key factor of designing a DSS. It often aims to fit the DSS to individual users’ expectations. For example, an adaptive DSS may capture and adapt to different users’ preferences in order to provide personalized information for decision support [13]. Instead of adapting to users’ preferences, CSFMonitor adapts its monitoring strategy to the update behaviors of the CSF selected by the users. That is, it adapts to the environment in order to satisfy the users’ need. Adapting to users’ preferences helps to identify target problems, while adapting to the environment helps to solve the problems in a more effective way.

## 5.4. Multiagent technology

Each agent in CSFMonitor behaves like a reactive agent, which aims to respond to environmental changes as well [33]. However, instead of independently accepting and reacting to environmental changes, the agents are coordinated to achieve their collective goals of CSF monitoring. Previous studies also recognized the benefits of integrating deliberative agents with reactive agents so that the agents may promptly and deliberately respond to dynamic environments [6,15]. To achieve that, event monitors (agents) such as those in CSFMonitor are helpful to promptly detect environmental changes without incurring a heavy communication cost to the agents.

Coordination among the agents is required, since CSF monitoring is a cooperative domain. The agents share a limited amount of resource to monitor the CSF, which may have an integrative meaning to the decision maker. Previous studies on multiagent coordination aimed to effectively resolve conflicts among agents using predefined knowledge and constraints [5,10,12,20]. Machine learning for better coordination was also explored to identify what and when to coordinate [18,20,29]. CSFMonitor employs a centralized coordinator to resolve resource consumption conflicts among the agents. The coordinator controls the total amount of resource consumption. No complex knowledge and constraints need to be predefined for coordination. At each moment, each agent learns to estimate its own need and then expresses the estimation to the coordinator. It is the simple learning facility that allows the coordinator to allocate resource to suitable agents at suitable time, making the system adaptive to the environment.

Conceptually, each agent in CSFMonitor bids for resource to conduct its task. Therefore, the technique is related to auction-based negotiation. Previous studies on multiagent auction have identified several protocols for the agents to bid for what they want. Recent studies focused on the efficiency and quality of determining a winner combination (e.g. Refs. [1,19]). Obviously, there exist trade-offs between the efficiency and the quality concerns [2]. For a better quality of auction, the agents could learn to predict the value (e.g. usage) of each target of bidding [4]. The design of CSFMonitor is motivated by similar considerations. Each agent in CSFMonitor bids for resource based on its need, which is initially unknown and dynamically changing over time. Therefore, for a better quality of winner determination, it learns to estimate its need. The main difference is that the resource (i.e. target of bidding) in CSFMonitor is always of value for each agent. What an agent learns to estimate is the amount of the resource required at each moment (rather than whether the resource is of value for the agent).

## 6. Future work

CSFMonitor does not consider the dynamic distribution of agents to the Intranet. As mentioned above, the distribution of agents may contribute the benefits of fault tolerance, load balancing, and bandwidth saving. However, there might exist trade-offs among the benefits as well. For example, to save bandwidths, the agents may be hosted in the site near to the machines that maintain the information items being monitored. If the site is quite busy at the current moment, load balancing is violated. Moreover, if a site that hosts an agent is crashed, the system should be able to redistribute the agent to some suitable site. Obviously, the situations call for a mechanism that may dynamically distribute the agents. If the mechanism is realized in each individual agent, the agents become ‘‘mobile’’ in the sense that they may travel (if necessary) around the Intranet. If the mechanism is realized in a particular agent, the agent should be able to sense the problem situations and make global decisions to redistribute the agent society.

The policy of adjusting the resource upper bound (i.e. l) and the way of estimating the system’s quality of services (QoS) deserve exploration as well. The estimation of QoS aims to provide the system administrator (and even the manager per se) with an indicator of the agents’ current performance and resource need. The resource pool maintained by the coordinator in CSFMonitor may serve as a rough indicator of the adequacy of the resource upper bound l. For example, when many agents cannot get what they want from the resource pool, QoS of the agents will degrade. On the other hand, when the resource pool accumulates a large amount of resource, QoS of the agents may be further promoted. Therefore, when l is too high or too low, the policy of automatically adjusting l (e.g. requesting for a higher l) and allocating l to certain agents (e.g. satisfying those agents with minimum QoS requirements) deserves more exploration.

We are also incorporating CSFMonitor into a DSS running on the Internet to provide financial decision support [25]. A hierarchical taxonomy of common CSF in financial management (as shown in Table 5) is developed to serve as the interface for the users to select and specify their CSF of interest. A registered user may add his/her own CSF to the hierarchy as well. He/she may also specify a minimum frequency of checking each CSF. The minimum frequency reflects the maximum tolerable delay of checking the CSF. Each user is notified (by email) only when critical events happening on the CSF are detected. Each event is also logged for later reference.

## 7. Conclusion

It is a must for managers to effectively capture those critical events that happen on CSF. However, managers often have difficulties in monitoring the CSF by themselves all the time. Therefore, a multiagent system is helpful in monitoring the CSF on behalf of the managers. Once an agent detects a status update of a CSF, it validates and handles the events happening on the CSF. By the support from the agents, the managers may focus their attention on other important jobs while simultaneously controlling the CSF.

To develop the multiagent system, there exist two dual considerations: (1) the robust, timely, and complete update detection for managers, and (2) the smooth delivery of the system to businesses. The considerations imply that, in the CSF monitoring domain, the agents should be properly distributed and coordinated on the Intranet so that robust, timely, and complete update detection may be achieved with out incurring heavy query overheads (to the related servers) and communication overheads (to the Intranet).

A multiagent CSF monitoring model CSFMonitor is developed. Its performance is investigated in an experiment that simulates real-world environments of financial CSF. It has been shown that CSFMonitor may significantly promote the cost-effectiveness of CSF monitoring without relying on intensive communications. For those domains in which critical events of CSF comprehensively and unpredictably happen on the Intranet and the Internet, CSFMonitor may help the managers to effectively capture the events without causing problems to original information processing in businesses.

## Acknowledgements

This research was supported by the National Science Council of the Republic of China under grants 88-2213-E-216-003 and NSC 89-2213-E-216- 003.

## References

[1] A. Anderson, M. Tenhunen, F. Ygge, Integer programming for combinatorial auction winner determination, Proceedings of the 4th International Conference on MultiAgent Systems, Boston, U.S.A., IEEE Computer Society, Boston, MA, 2000, pp. 39 – 46.

[2] M. Andersson, T. Sandholm, Time – quality tradeoffs in reallocative negotiation with combinatorial contract types, Proceedings of the 16th National Conference on Artificial Intelligence, AAAI Press, Orlando, Florida, 1999.

[3] A.A. Atkinson, R.D. Banker, R.S. Kaplan, S.M. Young, Planning and control, Management Accounting, 2nd edn., Prentice-Hall, Englewood Cliffs, NJ, 1997.

[4] R. Azoulay-Schwartz, S. Kraus, Assessing usage patterns to improve data allocation via auctions, Proceedings of the 4th International Conference on MultiAgent Systems, Boston, U.S.A., IEEE Computer Society, Boston, MA, 2000, pp. 47– 54.

[5] M. Barbuceanu, Coordinating agents by role-based social constraints and conversation plans, Proceedings of the 14th National Conference on Artificial Intelligence, AAAI Press, Providence, Rhode Island, 1997.

[6] R.P. Bonasso, D. Kortenkamp, D.P. Miller, M. Slack, Experiences with an architecture for intelligent, reactive agents, in: M. Wooldridge, P.J. Muller, M. Tambe (Eds.), Intelligent Agent II: Agent Theories, Architecture, and Languages, Springer-Verlag, New York, 1996.

[7] C. Brown, L. Gasser, D.E. O’Leary, A. Sangster, AI on the WWW supply and demand agents, IEEE Expert 10 (1995) 50 – 55, Aug.

[8] H. Chen, Y-.M. Chung, R. Marshall, C.Y. Christopher, An intelligent personal spider (agent) for dynamic Internet/Intranet searching, Decis. Support Syst. 23 (1998) 41 – 58.

[9] Comshare, Comshare Decision, http://www.comshare.com, 1999.

[10] J. Cuena, S. Ossowski, Distributed models for decision support, in: G. Weiss (Ed.), Multiagent Systems—A Modern Approach to Distributed Artificial Intelligence, MIT Press, Cambridge, MA, 1999.

[11] K. Decker, V. Lesser, M.V.N. Prasad, T. Wanger, MACRON: An Architecture for Multi-Agent Cooperative Information Gathering, Proceedings of the CIKM Workshop on Intelligent Information Agents, 1995.

[12] E.H. Durfee, D. Damouth, M. Huber, T.A. Montgomery, S. Sen, The search for coordination: knowledge-guided abstraction and search in a hierarchical behavior space, Proceedings of the 4th European Workshop on Modeling Autonomous Agents in a Multi-Agent World, Springer-Verlag, New York, 1992.

[13] B. Fazlollahi, M.A. Parikh, S. Verma, Adaptive decision support systems, Decis. Support Syst. 20 (4) (1997) 297–315.

[14] M.N. Frolick, M.J. Parzinger, R.K. Rainer, N.K. Ramarapu, Using EISs for environmental scanning, Inf. Syst. Manage. 14 (1) (1997) 35 – 40.

[15] S. Giroux, Open reflective agents, in: M. Wooldridge, J.P. Muller, M. Tambe (Eds.), Intelligent Agent II: Agent Theories, Architecture, and Languages, Springer-Verlag, New York, 1996.

[16] J.A. Hall, The management reporting system, Accounting Information Systems, West Publishing, New York, 1995.

[17] S.R. Hedberg, Intelligent agents: The first harvest of softbots looks promising, IEEE Expert 10 (1995) 6 – 49.

[18] B. Horling, V. Lesser, Using Diagnosis to Learn Contextual

Coordination Rules, UMass Computer Science Technical Report 99-15 (1999).

[19] L. Hunsberger, B.J. Grosz, A combinatorial auction for collaborative planning, Proceedings of the 4th International Conference on MultiAgent Systems, Boston, U.S.A., IEEE Computer Society, Boston, MA, 2000, pp. 151 – 158.

[20] D. Jensen, M. Atighetchi, R. Vincent, V. Lesser, Learning quantitative knowledge for multiagent coordination, Proceedings of the 16th National Conference on Artificial Intelligence, AAAI Press, Orlando, FLorida, 1999.

[21] M. Koster, Guidelines for Robot Writers, http://info.webcrwaler. com/mak/projects/robots/guidelines.html, 1993.

[22] V. Lesser, B. Horling, F. Klassner, A. Raja, BIG: A Resource-Bounded Information Gathering Agent, UMass Computer Science Technical Report 1998-03, 1998.

[23] R.-L. Liu, Adaptive agents for management by exceptions: Goals, criteria, and challenges, Proceedings of Agent Technology Workshop, Taipei, Taiwan, IEEE Computer Society, Boston, MA, 2000, pp. 175– 182.

[24] R.-L. Liu, S.-Y. Lin, Adaptive coordination of agents for timely and resource-bounded information monitoring, Proceedings of the 4th International Conference on MultiAgent Systems, Boston, U.S.A., 2000.

[25] R.-L. Liu, Y.-F. Kao, Y.-L. Lu, C.-L. Yang, K.-Y. Chang, Adaptive information monitoring agents for financial decision support, Proceedings of CSIM’99, Taipei, Taiwan, 1999.

[26] Openfind, Cyberspace Information Agent 2000 (CIA2000), http://www.openfind.com.tw/About<sup>\_</sup>us/p-2-04.html, 2000.

[27] Pilot Software, Pilot Decision Support Suite, http://www. pilotsw.com, 1999.

[28] L. Seligman, P. Lehner, K. Smith, C. Elsaesser, D. Mattox, Decision-centric information monitoring, J. Intell. Inf. Syst. 14 (2000) 29– 50.

[29] T. Sugawara, V.R. Lesser, Learning to improve coordinated actions in cooperative distributed problem-solving environments, Mach. Learn. 33 (1998) 129 – 153.

[30] J. Tarnowski, Management by Exceptions, http://www. jpetromark.com/98nov/article4.htm, 1998.

[31] E. Turban, J.E. Aronson, Intelligent agents and creativity, Decision Support Systems and Intelligent Systems, Prentice-Hall, Upper Saddle River, NJ, 1998, pp. 720 – 762.

[32] L. Volonino, H.J. Waston, S. Robinson, Using EIS to respond to dynamic business conditions, Decis. Support Syst. 14 (1995) 105–116.

[33] M. Wooldridge, N.R. Jennings, Agent theories, architectures, and languages: A survey, Proceedings of ECAI’94 Workshop on Agent Theories, Architectures, and Languages, John Wiley & sons, 1994.

![](/api/attachments/EAVC6BXX/fulltext/images/b84b1320b744e6e571b7e44ac85bf6edc323db01ea172c6657df61f6780f244d.jpg)

Rey-Long Liu is currently an associate professor of the Department of Information Management, ChungHua University, Taiwan. He received his PhD degree in Computer Science from the National TsingHua University, Taiwan, 1994. His research interest lies on the development and application of intelligent information technology to businesses information management, with a special focus on adaptive information systems. His main areas of interest

include intelligent multiagent systems, information retrieval, data mining, machine learning, and knowledge management systems.

![](/api/attachments/EAVC6BXX/fulltext/images/9938b0e9660c0704a5e7eb1d6f3c74eca188a8e145918bed3aa7821343830a02.jpg)

Yun-Ling Lu is currently a master student of the Department of Information Management, ChungHua University, Taiwan. Her research interests include knowledge management, intelligent multiagent systems, and information retrieval.
