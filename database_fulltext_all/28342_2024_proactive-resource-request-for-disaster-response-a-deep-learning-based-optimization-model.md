---
otero_id: 28342
otero_key: "ZNCFMYUM"
title: "Proactive Resource Request for Disaster Response: A Deep Learning-Based Optimization Model"
authors: "Hongzhe Zhang; Xiaohang Zhao; Xiao Fang; Bintong Chen"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0125"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Proactive Resource Request for Disaster Response: A Deep Learning-Based Optimization Model

Hongzhe Zhang,<sup>a</sup> Xiaohang Zhao,<sup>b</sup> Xiao Fang,<sup>c,</sup>\* Bintong Chen<sup>c</sup>

<sup>a</sup> School of Management and Economics and Shenzhen Finance Institute, The Chinese University of Hong Kong, Shenzhen 518172, China; <sup>b</sup> School of Information Management and Engineering, Shanghai University of Finance and Economics, Shanghai 200433, China; <sup>c</sup>Lerner College of Business and Economics, University of Delaware, Newark 19716, Delaware

Contact: zhanghongzhe@cuhk.edu.cn, https://orcid.org/0000-0002-9429-5748 (HZ); xiaohangzhao@mail.shufe.edu.cn, https://orcid.org/0000-0001-7766-6730 (XZ); xfang@udel.edu, https://orcid.org/0000-0002-9429-5748 (XF); bchen@udel.edu (BC)

Received: February 15, 2022 Revised: September 15, 2022; March 31, 2023 Accepted: July 25, 2023 Published Online in Articles in Advance: September 6, 2023

https://doi.org/10.1287/isre.2022.0125

Copyright: © 2023 INFORMS

Abstract. Disaster response is critical to save lives and reduce damages in the aftermath of a disaster. Fundamental to disaster response operations is the management of disaster relief resources. To this end, a local agency (e.g., a local emergency resource distribution center) collects demands from local communities affected by a disaster, dispatches avail able resources to meet the demands, and requests more resources from a central emergency management agency (e.g., the Federal Emergency Management Agency in the United States). Prior resource management research for disaster response overlooks the problem of deciding optimal quantities of resources requested by a local agency. In response to this research gap, we define a new resource management problem that proactively decides optimal quantities of requested resources by considering both currently unfulfilled demands and future demands. To solve the problem, we take salient characteristics of the problem into consideration and develop a novel deep learning method for future demand prediction. We then formulate the problem as a stochastic optimization model, analyze key properties of the model, and propose an effective solution method to the problem based on the analyzed properties. We demonstrate the superior performance of our method over prevalent existing methods using both real-world and simulated data. We also show its superiority over prevalent existing methods in a multistakeholder and multiobjective setting through simulations.

History: This paper has been accepted for the Information Systems Research Special Section on Unleashing the Power of Information Technology for Strategic Management of Disasters. Ahmed Abbasi, Robin Dillon-Merrill, H. Raghav Rao, and Olivia Sheng, Senior Editors; Huiming Zhao Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0125.

Keywords: disaster response • disaster management • proactive resource request • deep learning • temporal point process stochastic optimization

## 1. Introduction

We are living in the century of destructive disasters, which have claimed thousands of lives and caused tremendous economic losses.<sup>1</sup> In 2020 alone, 389 natural disasters affected 98.4 million people and cost 171.3 billion U.S. dollars worldwide.<sup>2</sup> Disaster management is critical to reduce adverse impacts of disasters and thus, has drawn attention from fields such as information systems (IS) and operations management (Park et al. 2015, Gupta et al. 2016). The life cycle of disaster management consists of four phases: mitigation, preparedness, response, and recovery (Altay and Green 2006). Disaster mitigation and preparedness take place before a disaster. The former aims to prevent disasters or reduce their impacts, whereas the latter makes preparations before a disaster strikes. Disaster response and recovery occur after a disaster. Disaster recovery focuses on restoring the affected community to the status before a disaster. In particular, disaster response plays an irreplaceable role in reducing fatalities and damages caused by a disaster (Fiedrich et al. 2000). It encompasses all operations conducted to save lives and reduce damages in the aftermath of a disaster, including providing resources to disaster-affected people, conducting search and rescue missions, and ensuring continuity of critical services.<sup>3</sup> Fundamental to these operations is resource management.

The goal of resource management for disaster response is to timely and effectively meet the demands for disaster relief resources from disaster-affected people (Fiedrich et al. 2000, Noyan et al. 2016). To this end, a humanitarian resource management system for disaster response is a multistakeholder and multiobjective system (Abbasi et al. 2019, 2021). Figure 1 depicts a typical humanitarian resource management system, which consists of three types of stakeholders: a central agency (e.g., the Federal Emergency Management Agency in the United States), a number of local agencies (e.g., local emergency resource distribution centers), and disasteraffected people. A local agency collects demands from its local community, dispatches available resources to meet the demands through its distribution points, and requests more resources from the central agency (Vanajakumari et al. 2016). Based on the requests from local agencies, the central agency allocates disaster relief resources to each of them. All stakeholders agree on the common objective of humanitarian resource management (i.e., minimizing the cost of delays in satisfying the demands of disaster-affected people); meanwhile, each type of stakeholders also could have its own objective (Abbasi et al. 2019, 2021). As illustrated in Figure 1, a local agency pays attention to its fill rate (i.e., ability to fulfill resource requests from its local community) (Noyan et al. 2016), whereas the central agency is concerned about fair allocation, which aims to ensure that no local agency is systematically disadvantaged in the allocation of disaster relief resources (Bertsimas et al. 2012, Huang et al. 2015).

Figure 1. A Humanitarian Resource Management System for Disaster Response  
![](/api/attachments/ZNCFMYUM/fulltext/images/880e0abb3a1ae4856db83726ad536865ea50c11c3d6653d9a36076498c01c245.jpg)

Existing resource management studies for disaster response focus on problems such as how to allocate and transport resources from the central agency to local agencies and how to locate distribution points in a disasteraffected area (Fiedrich et al. 2000, Tzeng et al. 2007, Noyan et al. 2016). These studies commonly assume the types and quantities of disaster relief resources requested by a local agency as given and overlook the problem of the local agency deciding the optimal quantity of requested resources for each resource type. A straightforward solution to this problem is to set quantities of requested resources as quantities of currently unfulfilled demands (Huang et al. 2015). For example, if demands for three units of food and two units of shelters are not fulfilled, a local agency would request three units of food and two units of shelters from the central agency. Such a solution is a reactive solution (i.e., in reaction to what has already happened). This solution neglects future demands that will arrive between the resource request time and the resource arrival time, which inevitably leads to significant time delays of satisfying these future demands. The cost incurred during disaster response is an increasing function of time delay (Holgu´ın-Veras et al. 2013); thus, significant time delays result in high costs and even loss of lives. For example, Fiedrich et al. (2000) show that the survival rate of disaster victims decreases in time, and Petrovic et al. (2012) find that suppression resources for wildfires are effective only if they reach the fire in time. Therefore, it is important to decide types and quantities of requested resources based on not only currently unfulfilled demands but also, future demands that will arrive between the resource request time and the resource arrival time.

In response, we introduce a new resource management problem for disaster response, namely a proactive resource request (PRR) problem. It aims to decide types and quantities of requested resources by considering both currently unfulfilled demands and future demands, with the objective of minimizing the cost incurred by delays in satisfying these demands. To solve the problem, we must tackle two methodological challenges: how to predict future demands and how to decide on an optimal resource request plan based on currently unfulfilled demands and predicted future demands. To address these challenges, we take salient characteristics of the problem into consideration and develop a novel deep learning method for future demand prediction. We then formulate the problem as a stochastic optimization model, analyze key properties of the model, and propose an effective solution method to the problem. Extensive empirical analyses with real-world and simulated data demonstrate that our method significantly outperforms prevalent existing methods in reducing the cost of delays in satisfying demands. Moreover, through simulations, we also show superior performance of our method over these benchmarks in a multistakeholder and multiobjective setting as depicted in Figure 1.

## 2. Related Work

## 2.1. Resource Management for Disaster Response

Existing studies on resource management for disaster response focus on four research problems: resource allocation, resource distribution, facility location, and resource procurement (Gupta et al. 2016). Resource allocation aims to decide the optimal assignment of resources to disasteraffected areas. For example, Fiedrich et al. (2000) propose a dynamic combinatorial optimization model that allocates technical response resources after a major earthquake, with the objective of minimizing the number of fatalities during the search and rescue period of disaster response. Unlike resource allocation, resource distribution plans routes to transport resources from distribution centers to affected people (Tzeng et al. 2007). To this end, Tzeng et al. (2007) adopt a multiobjective programming method to design a relief delivery system with the goal of minimizing the transportation cost and time and maximizing the satisfaction of demands simultaneously. Facility location decides how to locate distribution points in a disaster-affected region for the provision of disaster relief resources (Noyan et al. 2016). In this vein, Noyan et al. (2016) propose lastmile relief networks, which determine the locations and capacities of resource distribution points while considering the uncertainties in demands and transportation network conditions. The goal of relief networks is to maximize the expected total accessibility, which measures the ease of access to resources. Lastly, resource procurement develops policies for procuring disaster relief resources from suppliers. An exemplar study by Natarajan and Swaminathan (2014) proposes an optimal resource procurement policy that minimizes the shortages of fulfilling demands for disaster relief resources subject to the constraint of disaster relief funds.

Recent studies have solved several of the research problems elaborated simultaneously. For example, Rennemo et al. (2014) present a three-stage stochastic programming model, each stage of which models the problems of facility location, initial resource allocation, and last-mile resource distribution. To better capture real-world disaster response situations, the model treats the availability of vehicles, the demands for disaster relief resources, and the condition of transportation infrastructure as stochastic model elements. Ahmadi et al. (2015) propose a locationrouting model, which decides locations of central warehouses in the disaster preparedness phase and determines locations of local distribution centers and routes of vehicles in the disaster response phase. The model introduces novel constraints to model the golden time period of disaster response. Like Rennemo et al. (2014), Vanajakumari et al. (2016) develop an integrated logistics model that solves the facility location, resource allocation, and resource distribution problems simultaneously. They also provide empirical insights that are useful for logistic managers during the disaster response phase.

## 2.2. Inventory Control Models

Depending on how future demands are modeled, inventory control (IC) models can be classified into classical IC models and data-driven IC models. Classical IC models assume that a certain form of information on future demands is known to decision makers and that the optimal IC policy is then derived accordingly. For example, the economic order quantity model assumes that the quantities of future demands are known and deterministic, and then, it obtains a closed-form solution of optimal order quantity (Zipkin 2000, p.146). To better capture demand uncertainty, more IC models assume that future demand quantities follow a known probability distribution, such as normal distribution (Mieghem and Rudi 2002) and Poisson distribution (Guijarro et al. 2012). To develop inventory control policies that minimize the inventory cost over multiple periods, time series models have been used to model period-correlated demands. For example, Gilbert (2005) characterizes demands using the Autoregressive Inte grated Moving Average (ARIMA) model and theoretically analyzes the bullwhip effect in a multistage supply chain. In addition, a number of studies consider demand uncer tainties caused by the evolution of the model environment. An exemplar study by Hu et al. (2016) adopts a Markov modulated demand model, which assumes that demands are generated from one period to another by an evolving “state” factor characterized by a discrete-time Markov chain. Different from the literature reviewed that focuses on demand quantity information solely, a number of IC models assume richer information about future demands: both the quantity and arrival time of a future demand. They often model future demands using continuous stochastic arrival processes, such as a compound Poisson process (Zhao 2009), a Markov modulated Poisson pro cess (Arts et al. 2016), and a time-dependent phase-type process (Nasr and Elshar 2018). For example, Arts et al. (2016) investigate a repairable stocking system, in which the demand of a repairable item follows a Markov modu lated Poisson process and failed parts can be expedited with extra cost to shorten waiting time.

Classical IC models focus on the structure of optimal IC policies under various distribution or process assumptions of future demands, which may not accurately reflect true future demands. In response, various datadriven IC models are proposed more recently to predict future demand quantities or the distribution of future demand quantities from historical demand data and then, decide the optimal IC policy based on the prediction. Notably, time series methods, such as Croston-like methods and ARIMA, have gained popularity in the data-driven IC literature for predicting future demand quantities (Syntetos et al. 2009). Besides, much literature aims to predict future demand quantities using linear regression. A recent study by Ban and Rudin (2019) formulates a data-driven newsvendor problem. They estimate future demand quantities using a linear regression on observed problem features and propose an empirical risk minimization approach to solve the problem. Built on the work by Ban and Rudin (2019), Oroojlooyjadid et al. (2020) apply a deep learning method (i.e., a multilayer perceptron (MLP)) to predict future demand quantities. IC policies have also been derived based on the estimated distribution of future demand quantities. In case reasonable prior knowledge of demand distribution is available, the Bayesian method can be applied to update the posterior demand distribution as new demands arrive (e.g., Chen 2010). In addition, some studies focus on demand learning for the joint dynamic pricing and inventory control problem. For example, Chen et al. (2022, 2023) treat the expected demand quantity over each planning period as a function of price. In particular, the former fits the demand-price curve via a parametric function, whereas the latter uses a nonparametric setting. Besides demand quantity forecasting, predicting future demand quantiles has drawn attention because safety stock levels can be computed from demand quantiles directly. In this vein, Taylor (2007) proposes an exponentially weighted quantile regression to predict daily sales with high volatility and skewness. Fricker and Goodhart (2000) apply bootstrapping to estimate future demand distribution and set reorder points based on quantiles derived from the distribution.

## 2.3. Demand Forecasting and Temporal Point Process

Demand forecasting can be formulated as a regression problem, where training data consists of demand explanatory variables and corresponding demand quantities. Once the training data set is constructed, statistical and machine learning methods, such as regression models and tree-based methods, can be applied to it to predict future demands. When demand data are sequentially recorded at equal time intervals (e.g., per day), time series forecasting methods are widely used (e.g., Arunraj and Ahrens 2015). Recently, using deep learning methods to predict demands has become a growing area of research because of their advanced learning and forecasting capabilities. In particular, recurrent neural network (RNN)- based methods, such as Long Short-Term Memory (LSTM) (Tan et al. 2019) and the deep sequence-to-sequence method (Yi et al. 2022), have been employed to predict demand quantities over discrete time periods in various domains. Besides, graph convolution networks have been utilized to predict transportation demands (e.g., demands for ride hailing and bike sharing) (Ye et al. 2021).

Predicting future demands can also be formulated as a problem of predicting a sequence of future events, each of which corresponds to a demand. To solve this problem, temporal point process (TPP) can predict future demand events with continuous arrival times. Because of its solid mathematical foundation and excellent predictive performance, TPP has become the dominant technique for predicting a sequence of future events (Shchur et al. 2020). TPP is a stochastic process that models the arrival times and marks of a sequence of events (Du et al. 2016). For example, in our study, TPP models the arrival times of demand events as well as the mark (i.e., types and quantities of requested disaster relief resources)

associated with each demand. TPP has wide use cases, including intermittent demand forecasting (Turkmen et al. 2019), health event prediction (Enguehard et al. 2020), and identification of similar sequences (Gupta et al. 2022a). TPP can be characterized by its conditional intensity function (CIF), which models the instantaneous occurrence rate of an event conditioning on the history of previous events. Early TPP models usually make restrictive parametric assumptions on CIFs. For instance, the classic Hawkes process assumes that the arrival of an event temporarily raises the conditional intensity of the process (Rizoiu et al. 2017). However, the assumptions made by early TPP models might not reflect the reality, and therefore, they suffer from model misspecification errors (Du et al. 2016). To overcome these limitations, recent studies develop CIFs based on deep learning models (Du et al. 2016, Mei et al. 2022).

In particular, RNN and its variants have been widely used to encode event history because of their capabilities of capturing nonlinear dependency of an event on its previous events. In this vein, Du et al. (2016) employ a discrete-time RNN to embed past events as a vector and then, design a CIF with its parameters derived from the vector, thereby capturing the dependency of an event on its past events. Mei and Eisner (2017) construct their CIF based on vectors that summarize past events through a continuous-time LSTM, which enables their proposed TPP to model more complicated event arrival patterns. Xiao et al. (2018) also use LSTM and propose to train TPP with Wasserstein loss, which measures the distance between an event sequence in the training data and its prediction. Built on Xiao et al. (2018), Yan et al. (2018) add one additional loss that measures the mean square error between the number of events in an event sequence and that in its prediction. Deshpande et al. (2021) parti tion a training event sequence into equal time intervals and count the number of events in each time interval. They propose to train TPP by maximizing the likelihood of counts in these time intervals and the likelihood of observing each individual event in the training event sequence.

Recently, a number of studies have employed the transformer architecture to encode event history (Mei et al. 2022). For example, Enguehard et al. (2020) and Mei et al. (2022) utilize transformer blocks to represent a sequence of historical events as an embedding matrix and then, evaluate the CIF at any future time stamp by using the time stamp as the query to summarize the embedding matrix as an intensity score. A similar idea is adopted by Zhang et al. (2020) and Zuo et al. (2020), but they assume a simpler dependency of the CIF on a future time stamp. Another recent trend is to characterize TPP using a conditional probability density function instead of a CIF. For example, Shchur et al. (2020) model the conditional probability density of event interarrival times with a mixture of lognormal distributions, of which the parameters are derived from the vector representation of past events. Gupta et al. (2022b) investigate the problem of training TPP with incomplete observations of historical events. They propose to treat missing events as latent variables and model the dynamics of observed events and that of missing events via two coupled TPP models.

Our literature review suggests several research gaps. First, existing resource management studies for disaster response overlook the problem of deciding optimal quantities of resources requested by a local agency. To address this gap, we propose a new resource management problem that proactively decides the optimal quantity of requested resources for each resource type based on both currently unfulfilled demands and future demands. Second, even though our proactive resource request problem is conceptually related to IC models, adapting an existing IC model to our problem is not an effective approach. More specifically, classical IC models make assumptions on the distribution or process of future demands, which may not reflect true future demands in reality; data-driven IC models focus on predicting future demand quantities over discrete time periods. We model future demand quantities and arrival times as a stochastic arrival process in a continuous timeline and learn the process from historical demand data Third, to solve the proactive resource request problem, it is necessary to predict future demands. Most demand forecasting methods focus on forecasting future demand quantities or predicting future demand quantities over discrete time periods (e.g., Arunraj and Ahrens 2015, Yi et al. 2022). However, to effectively solve the problem, both quantities and continuous arrival times of future demands need to be modeled and predicted. Moreover, the distribution of demands is nonstationary during the outbreak of a disaster, which further complicates the task of predicting quantities and arrival times of future demands. To this end, a TPP model is applicable for modeling nonstationary demand arrival processes. However, existing TPP models are not well suited for our problem because of the following characteristics. (1) The problem requires us to model both the type and quantity of requested resources. However, existing TPP mark-embedding functions are designed to model either the type or the quantity of an event. (2) It is essential to incorporate the importance scores of different types of resources into the prediction of future demands because different types of resources are not equally important for disaster relief. Existing TPP models overlook the heterogeneous importance of disaster relief resources in demand prediction. (3) The quantities of different resource types requested in a demand could be correlated. Existing TPP models fail to capture this correlation. In response, we develop a novel TPP model that features three methodological novelties, each of which addresses one of the salient characteristics of the problem. Fourth, our proposed resource request problem requires a novel model and solution method. Accordingly, we develop a stochastic optimization model for the problem and identify its key properties. Armed with these properties, we propose an effective solution method to the problem.

## 3. Problem Formulation

Consider a disaster (e.g., a flood or earthquake) that occurs at time T<sub>�</sub>. In response to it, a local agency collects demands for disaster relief resources, dispatches available resources to meet the demands, and requests more resources from a central emergency management agency. Each demand is described by its arrival time as well as types (e.g., food, shelter) and quantities of resources requested. Let T denote the time that the local agency requests resources from the central agency. At this time, the local agency is aware of the remaining resources and unfulfilled demands and decides the types and quantities of resources that need to be requested from the central agency. Let $R _ { k }$ denote the quantity of remaining type k resources and $U _ { k }$ be the quantity of unfulfilled demands for type k resources at time T, where $k = 1 , 2 , \dots , K$ and K is the number of resource types. It is clear that either $R _ { k }$ or $U _ { k }$ is zero (i.e., $R _ { k } \times U _ { k } = \bar { 0 _ { \cdot } } \bar { k } = 1 , 2 , \dots , K )$ . We use a simple example to illustrate the calculation of $R _ { k }$ and $U _ { k } .$

Example 1. Consider a disaster that causes the follow ing demands by time T (see Table 1).

A local agency with resources of 5 units of shelters and 10 units of food dispatches 4 units of shelters to fulfill demand 1. Subsequently, it distributes six units of food and the remaining one unit of shelter to meet demand 2. Clearly, two units of shelters requested in demand 2 cannot be fulfilled by available resources, and there are four units of food left over. We thus have $U _ { s h e l t e r } = 2 , R _ { s h e l t e r } = 0 , U _ { f o o d } = 0 .$ , and $R _ { f o o d } = 4$ at time T.

At time $T ,$ for each resource type k to be requested from the central agency, the local agency needs to decide its requested quantity $x _ { k } , k = 1 , 2 , \ldots , K .$ A simple way is to decide $x _ { k }$ in a reactive manner and set it according to unfulfilled demands $U _ { k }$ for $k = 1 , 2 , \dots , K$ (Huang et al. 2015). However, resources requested at time $\dot { T }$ will arrive at a later time $T _ { + \prime }$ and there will be demands occurring during the period of T to $T _ { + }$ . Reactive decisions at time $T$ only consider currently unfulfilled demands $U _ { k }$ but neglect future demands in the period of $T$ to $T _ { + }$ , which results in significant time delays of satisfying these future demands. These time delays in turn lead to high costs and even loss of lives as the cost incurred during disaster response is an increasing function of time delay (Holgu´ın-Veras et al. 2013). Therefore, it is important to develop a proactive method that decides $x _ { k }$ based on not only currently unfulfilled demands but also, future demands in the period of $T$ to $T _ { + }$ . In addition, the transportation capacity of moving resources from the central agency to the local agency is not unlimited, and it is constrained because of damaged transportation infrastructure and the shortage of transportation equipment (Gossler et al. 2019). Consequently, transportation capacity W constrains the quantities of resources that can be received (and hence, requested) by the local agency. We are now ready to define the proactive resource request problem.

Table 1. Disaster Causes the Demands by Time T

<table><tr><td>Demand identification</td><td>Demand time</td><td>Type of resources requested</td><td>Quantity of resources requested</td></tr><tr><td>1</td><td>July 18, 2021 12:04:33</td><td>Shelter</td><td>4</td></tr><tr><td>2</td><td>July 18, 2021 16:38:26</td><td>Shelter</td><td>3</td></tr><tr><td>2</td><td>July 18, 2021 16:38:26</td><td>Food</td><td>6</td></tr></table>

Definition 1 (Proactive Resource Request Problem). A local agency requests disaster relief resources from a central agency at time T. Given the quantity $R _ { k }$ of remaining resources and the quantity $\bar { U _ { k } } ^ { - }$ of unfulfilled demands for each resource type $\dot { k , \ k } = 1 , 2 , \ldots , K ,$ as well as the transportation capacity W at time T, the local agency needs to decide the quantity $x _ { k }$ of requested resources for each resource type k such that the cost incurred by delays in satisfying unfulfilled demands by time T and future demands arrived in the period of T to $T _ { + }$ is minimized while satisfying the constraint of the transportation capacity.

Generally speaking, our study belongs to predictive and prescriptive analytics research in the IS field. Over the years, IS scholars have developed predictive analytics methods that predict future outcomes or prescriptive analytics methods that make optimal decisions informed by predictions to solve a diverse set of critical business and societal problems (Abbasi et al. 2012; Fang et al. 2013, 2021; Lin and Fang 2021; Zhu et al. 2021). Our study adds to this stream of IS research with a new research problem and a novel method.

## 4. Solution Method

To solve the PRR problem, we need to tackle its two subproblems: (1) how to predict future demands in the period of $( T , T _ { + } ]$ and (2) how to decide an optimal resource requesting plan in consideration of both currently unfulfilled demands and predicted future demands. Figure 2 illustrates the overall architecture of the proposed solution method. As shown, the method consists of two components, each of which solves its corresponding subproblem. The cost-aware neural marked (CNM)-TPP component takes the observed (historical) demands in the period of [T<sub>�</sub>, T] as inputs and summarizes these demands as a dense embedding vector. The event generation layer is designed to sample future demands given the embedding vector of historical demands. Next, the PRR component iteratively invokes the event generation layer to sample sequences of future demands. These sampled future demands, together with currently unfulfilled demands, are taken as inputs by our proposed greedy algorithm to decide the resource requesting plan. We detail each component in Sections 4.1 and 4.2, respectively.

## 4.1. Future Demand Prediction

We propose the CNM-TPP, which learns a model from observed demands in the period of $[ T _ { - } , T ]$ to predict future demands in the period of (T, T ]. CNM-TPP treats each demand as an event. Accordingly, we can represent observed demands in the period of $[ T _ { - } , T ]$ as an event sequence $S = < e _ { 1 } , e _ { 2 } , \ldots , e _ { L } >$ , where L denotes the number of events (i.e., demands) in the period and the ith event $e _ { i } = ( t _ { i } , m _ { i } )$ is described by its occurrence time $t _ { i }$ $( \mathrm { i . e . , }$ demand time) as well as its mark $m _ { i }$ indicating the types and quantities of the resources requested by the demand. To learn a model from $S ,$ it is critical to compute the likelihood p(S) of observing S (Shchur et al. 2021). Specifically, we can factorize p(S) as

Figure 2. (Color online) Overall Architecture of the Proposed Solution Method  
![](/api/attachments/ZNCFMYUM/fulltext/images/e37868fd538c3eed54ba0a70545c9897b2ea63fd09a4826cc58e24907c0f4937.jpg)

$$
p (S) = P (\tau_ {L + 1} > T - t _ {L}) \prod_ {i = 1} ^ {L} p _ {\tau} (\tau_ {i} | \mathcal {H} _ {i - 1}) p _ {m} (m _ {i} | \mathcal {H} _ {i - 1}),\tag{1}
$$

where $\mathscr { H } _ { i - 1 } = < e _ { 1 } , e _ { 2 } , \ldots , e _ { i - 1 } >$ denotes the sequence of past events before the ith event $e _ { i } , ~ i = 1 , 2 , \ldots , L$ , and $\mathcal { H } _ { 0 } = \emptyset$ . We define interarrival time $\tau _ { i } = t _ { i } - t _ { i - 1 }$ , and $p _ { \tau } ( \tau _ { i } | \mathcal { H } _ { i - 1 } )$ is the probability density that the interarrival time between the ith event and the $( i - 1 ) \mathrm { t h }$ event is $\tau _ { i }$ conditioning on past events $\mathcal { H } _ { i - 1 } ;$ let $p _ { m } ( m _ { i } | \mathcal { H } _ { i - 1 } )$ represent the probability mass that the mark of the ith event is $m _ { i }$ conditioning on $\mathcal { H } _ { i - 1 }$ . Because interarrival time $\tau _ { L + 1 } = t _ { L + 1 } - t _ { L }$ , we have $P ( \tau _ { L + 1 } > T - t _ { L } ) = P ( t _ { L + 1 } > T )$ which is the probability that the (L + 1)th event occurs after time T. The derivation of Equation (1) is given in Online Appendix A.1.

Based on the structure of Equation (1), we design CNM-TPP as a deep neural network with three building blocks: (1) a history-embedding layer that summarizes the information contained in $\bar { \mathcal { H } } _ { i - 1 } , ( 2 )$ an event generation layer that specifies probability functions $p _ { \tau } ( \ r )$ and $p _ { m } ( \boldsymbol { \mathbf { \rho } } ) ,$ , and (3) the learning objective of CNM-TPP. In what follows, we elaborate each building block in turn.

4.1.1. History Embedding. The objective of this layer is to embed the information contained in $\mathcal { H } _ { i - 1 }$ as a numeric vector $\boldsymbol { h } _ { i - 1 } \in \mathbb { R } ^ { n _ { e } }$ , where hyperparameter $n _ { e }$ is the embedding size. Given the sequential nature of the events in $\mathcal { H } _ { i - 1 }$ , it is natural to embed it with an RNN (Du et al. 2016, Shchur et al. 2020). Therefore, we have

$$
\begin{array}{l} \boldsymbol {h} _ {i - 1} = \operatorname{RNN} (\boldsymbol {h} _ {i - 2}, e _ {i - 1}) \\ \qquad = \max \{\boldsymbol {W} ^ {(h)} \boldsymbol {h} _ {i - 2} + \boldsymbol {w} ^ {(t)} \tau_ {i - 1} + \boldsymbol {W} ^ {(m)} \boldsymbol {f} _ {m} (e _ {i - 1}) + \boldsymbol {b} ^ {(h)}, 0 \}, \end{array}\tag{2}
$$

where activation function max $\left\{ v _ { 1 } , v _ { 2 } \right\}$ compares vectors $v _ { 1 }$ and $v _ { 2 }$ element wisely and returns the larger one on each dimension, $h _ { i - 2 }$ is the embedding vector of $\mathcal { H } _ { i - 2 } , \tau _ { i - 1 }$ is the interarrival time between events $e _ { i - 2 }$ and $e _ { i - 1 }$ , and $( \boldsymbol { W } ^ { ( h ) } \in \mathbb { R } ^ { n _ { e } \times n _ { e } } , \boldsymbol { w } ^ { ( t ) } \in \mathbb { R } ^ { n _ { e } } , \boldsymbol { W } ^ { ( m ) } \in \mathbb { R } ^ { n _ { e } \times n _ { e } } , \boldsymbol { b } ^ { ( h ) } \in \mathbb { R } ^ { n _ { e } } )$ are learnable parameters of the RNN model. Markembedding function $f _ { m } ( )$ represents the mark of $e _ { i - 1 }$ as a numeric vector.

Existing TPPs model either the type or the quantity of an event (Turkmen et al. 2019, Enguehard et al. 2020, Shchur et al. 2021). However, an event mark in the PRR problem contains not only the type(s) of requested resources but also, the quantity of each requested resource type. To accommodate this characteristic of the PRR problem, we represent an event mark using a vector a with K entries, and its kth entry $a _ { k }$ denotes the requested units of type k resources, $k = 1 , 2 , \dots , K$

Example 2. Consider a simple scenario of three resource types: shelter, medication, and food $( \mathrm { i . e . , } K = 3 )$ . In this scenario, we can represent an event mark requesting three units of shelters and six units of food with a vector $\mathbf { \delta } _ { a } = \left( 3 , 0 , 6 \right) ^ { T }$ , where $a _ { 1 } , ~ a _ { 2 } ,$ , and $a _ { 3 }$ denote the requested units of shelter, medication, and food, respectively.

To summarize the information in an event mark, we need to embed $a _ { k }$ for $k = 1 , 2 , \ldots , K .$ . To that end, we define an embedding function $f _ { \mathrm { q } } ( )$ adapted from Vaswani et al. (2017). The function embeds $a _ { k } \ ( \mathrm { i . e . }$ , the quantity of requested type k resources) as a numeric vector of length $n _ { e } ,$ and each entry $f _ { \ P } ( a _ { k } , x )$ of the vector is defined as

$$
f _ {\mathrm{q}} (a _ {k}, x) = \sin (a _ {k} / 1 0, 0 0 0 ^ {x / n _ {e}}),\tag{3}
$$

where sin() is the sine function and $x = 1 , 2 , \ldots , n _ { e }$ . Function $f _ { \mathrm { q } } ( )$ has two desirable properties. First, by Equation $( 3 ) _ { \cdot }$ , it embeds $a _ { k }$ as a zero vector if $a _ { k } = 0 ( \mathrm { i . e . }$ , requesting zero units of type k resources). Second, similar values of $\displaystyle \boldsymbol { a } _ { k } .$ yield embedding vectors carrying similar information.

With $f _ { \mathrm { q } } ( )$ defined, we propose the mark-embedding function $\dot { f } _ { m } ( )$ for the PRR problem as

$$
\boldsymbol {f} _ {m} (e _ {i - 1}) = \sum_ {k = 1} ^ {K} \boldsymbol {W} _ {:, k} ^ {(r)} \odot \boldsymbol {f} _ {\mathrm{q}} (a _ {k} ^ {(i - 1)}),\tag{4}
$$

where $\boldsymbol { W } ^ { ( r ) } \in \mathbb { R } ^ { n _ { e } \times K }$ is the learnable embedding matrix for resource types, its kth column $W _ { : , k } ^ { ( r ) }$ represents resource type k, $\mathbf { \Psi } \mathbf { k } = 1 , 2 , \dots , K , a _ { k } ^ { ( i - 1 ) }$ is the quantity of type k resources requested in event $e _ { i - 1 }$ , and ⊙ denotes element-wise multiplication. According to Equation (4), the embedding of an event mark, $\mathbf { \Delta } f _ { m } ( e _ { i - 1 } )$ , is the aggregation of $K$ embeddings, each of which summarizes the information about a resource type and its requested quantity in the event as $W _ { : , k } ^ { ( r ) } \odot f _ { \mathrm { q } } ( a _ { k } ^ { ( i - 1 ) } )$ . Taken together, the parameter set of the history-embedding layer is given by

$$
\Theta_ {H} = \{\pmb {W} ^ {(h)}, \pmb {w} ^ {(t)}, \pmb {W} ^ {(m)}, \pmb {b} ^ {(h)}, \pmb {W} ^ {(r)} \}.\tag{5}
$$

Our mark-embedding function differs from existing ones, which are designed to represent either the type or the quantity of an event (Turkmen et al. 2019, Enguehard et al. 2020, Shchur et al. 2021). However, an event mark in the PRR problem contains not only the type of requested resources but also, the quantity of requested resources. Therefore, the novelty of our mark-embedding function is the introduction of $\check { W } _ { : , k } ^ { ( r ) } \odot f _ { \mathrm { q } } ( a _ { k } ^ { ( i - 1 ) } )$ in Equation (4). Specifically, function $f _ { \mathrm { q } } ( )$ is designed to capture the quantity of requested resources. It is then integrated with $\boldsymbol { W } _ { : , k } ^ { ( \check { r } ) }$ through element-wise multiplication to represent both the quantity and type of requested resources.

4.1.2. Event Generation. Following Shchur et al. (2020), we model the conditional probability density $p _ { \tau } ( \ r )$ of event interarrival times as a mixture of $n _ { z }$ lognormal distributions, where $n _ { z }$ is a hyperparameter of our method. Specifically, we have

$$
p _ {\tau} (\tau_ {i} | \mathcal {H} _ {i - 1}) = \sum_ {z = 1} ^ {n _ {z}} \alpha_ {i, z} \frac {1}{\tau_ {i} \sigma_ {i , z} \sqrt {2 \pi}} \exp \left(- \frac {(\log \tau_ {i} - \mu_ {i , z}) ^ {2}}{2 \sigma_ {i , z} ^ {2}}\right),\tag{6}
$$

where parameters $\alpha _ { i , z } , \mu _ { i , z ^ { \prime } }$ and $\sigma _ { i , z }$ denote the weight, mean, and standard deviation of the zth lognormal distribution, respectively. To model the dependency of $\tau _ { i }$ on past events $\mathcal { H } _ { i - 1 }$ , we derive the parameters of Equation (6) from $h _ { i - 1 } ,$ the history-embedding vector of $\mathcal { H } _ { i - 1 }$ In particular, by following Shchur et al. (2020), we have

$$
\begin{array}{l} \alpha_ {i} = \text { Softmax } (\text { MLP } _ {1} (\boldsymbol {h} _ {i - 1})) \\ \mu_ {i} = \text { MLP } _ {2} (\boldsymbol {h} _ {i - 1}) \\ \sigma_ {i} = \exp (\text { MLP } _ {3} (\boldsymbol {h} _ {i - 1})), \end{array}\tag{7}
$$

where vectors $\pmb { \alpha } _ { i } = ( \alpha _ { i , 1 } , \alpha _ { i , 2 } , \ldots , \alpha _ { i , n _ { z } } ) ^ { T } , \pmb { \mu } _ { i } = ( \mu _ { i , 1 } , \mu _ { i , 2 } , \ldots ,$ ${ \mu _ { i , n _ { z } } ) } ^ { T } .$ , and $\pmb { \sigma } _ { i } = \left( \sigma _ { i , 1 } , \sigma _ { i , 2 } , \ldots , \sigma _ { i , n _ { z } } \right) ^ { T }$ . In Equation $( 7 ) ,$ ML $\mathrm { { . P _ { 1 } } }$ , ML $\mathrm { { . P } } _ { 2 }$ , and ML ${ \mathrm { P } } _ { 3 }$ are ML ${ \mathrm { P s } } ,$ each of which takes $h _ { i - 1 }$ as input and outputs a vector of length $n _ { z } ;$ the notation Softmax(·) denotes the softmax function; and exp(·) denotes the exponential function applied to its input element wisely.

To specify probability mass function $p _ { m } ( \boldsymbol { \mathbf { \rho } } )$ , we formulate the generation of an event mark as the generation of K nonnegative integers (conditioning on past events $\mathcal { H } _ { i - 1 } ) .$ where each integer denotes the units of a resource type requested in the event and is modeled by a Poisson distribution. Accordingly, the probability $p _ { m } ( m _ { i } | \mathcal { H } _ { i - 1 } )$ that the mark of event $e _ { i }$ is $m _ { i }$ conditioning on $\mathcal { H } _ { i - 1 }$ is given by

$$
\begin{array}{l} p _ {m} (m _ {i} | \mathcal {H} _ {i - 1}) = p _ {m} \Big (a _ {1} ^ {(i)}, a _ {2} ^ {(i)}, \ldots , a _ {K} ^ {(i)} | \mathcal {H} _ {i - 1} \Big) \\ \qquad = P \Big (a _ {1} ^ {(i)} | \mathcal {H} _ {i - 1} \Big) P \Big (a _ {2} ^ {(i)} | \{a _ {1} ^ {(i)} \}, \mathcal {H} _ {i - 1} \Big) \\ \qquad \ldots P \Big (a _ {K} ^ {(i)} | \{a _ {1} ^ {(i)}, a _ {2} ^ {(i)}, \ldots , a _ {K - 1} ^ {(i)} \}, \mathcal {H} _ {i - 1} \Big) \\ \qquad = \prod_ {k = 1} ^ {K} P \Big (a _ {k} ^ {(i)} | a _ {1: k - 1} ^ {(i)}, \mathcal {H} _ {i - 1} \Big), \end{array}\tag{8}
$$

where $a _ { k } ^ { ( i ) }$ is the units of type k resources requested in event $e _ { i }$ and $a _ { 1 : k - 1 } ^ { ( i ) } = \{ a _ { 1 } ^ { ( i ) } , a _ { 2 } ^ { ( i ) } , \ldots , a _ { k - 1 } ^ { ( i ) } \}$ with $\bar { a _ { 1 : 0 } ^ { ( i ) } } = \emptyset$ for convenience. The second step of Equation (8) follows from the chain rule in probability theory. Equation (8) captures correlations among the units of different resource types requested in a demand. For example, in a demand, the requested units of food and water might be positively correlated. In this equation, $P ( a _ { k } ^ { ( i ) } | a _ { 1 : k - 1 } ^ { ( i ) } , \mathcal { H } _ { i - 1 } )$ is specified as

$$
P \left(a _ {k} ^ {(i)} \mid a _ {1: k - 1} ^ {(i)}, \mathcal {H} _ {i - 1}\right) = \text { Poisson } (a _ {k} ^ {(i)}; \lambda_ {i, k}),\tag{9}
$$

where $\lambda _ { i , k }$ is the mean of the Poisson distribution for modeling $a _ { k } ^ { ( i ) }$ . To model the dependency of $a _ { k } ^ { ( i ) }$ on $\mathcal { H } _ { i - 1 }$ and $a _ { 1 : k - 1 } ^ { ( i ) } ,$ , we derive $\lambda _ { i , k }$ as

$$
\boldsymbol {h} _ {i, k} ^ {(\lambda)} = \operatorname{RNN} _ {\lambda} \left(\boldsymbol {h} _ {i, k - 1} ^ {(\lambda)}, \boldsymbol {W} _ {:, k - 1} ^ {(r)} \odot \boldsymbol {f} _ {\mathrm{q}} (a _ {k - 1} ^ {(i)})\right)\tag{10a}
$$

$$
\lambda_ {i, k} = \exp \Big (\boldsymbol {W} _ {:, k} ^ {(r) T} \boldsymbol {h} _ {i, k} ^ {(\lambda)} \Big),\tag{10b}
$$

where $h _ { i , 1 } ^ { ( \lambda ) } = h _ { i - 1 }$ , with $h _ { i - 1 }$ being the embedding vector of $\mathcal { H } _ { i - 1 }$ . Equation (10a) uses an RNN layer to summarize the information in $\mathcal { H } _ { i - 1 }$ and $a _ { 1 : k - 1 } ^ { ( i ) }$ into vector $h _ { i , k } ^ { ( \lambda ) }$ length $n _ { e } .$ In this equation, we use the same idea behind Equation (4) to embed the quantity $a _ { k - 1 } ^ { ( i ) }$ of type $k - 1$ resource requested in event $e _ { i }$ as $W _ { : , k - 1 } ^ { ( r ) } \odot f _ { \mathrm { q } } ( a _ { k - 1 } ^ { ( i ) } )$ . Equation (10b) derives $\lambda _ { i , k }$ from $h _ { i , k } ^ { ( \lambda ) }$ <sup>)</sup> via an exponential transformation to ensure $\lambda _ { i , k } > 0 .$ <sup>4</sup> The parameter set for the event generation layer is given by

$$
\Theta_ {E} = \{\Theta (\mathrm{MLP} _ {1}), \Theta (\mathrm{MLP} _ {2}), \Theta (\mathrm{MLP} _ {3}), \Theta (\mathrm{RNN} _ {\lambda}) \},\tag{11}
$$

where Θ(MLP ) is the parameter set of MLP for $i = 1 , 2 , 3$ and $\Theta ( \mathrm { R N N } _ { \lambda } )$ ) is the parameter set of $\mathrm { R N N } _ { \lambda }$

4.1.3. Learning Objective. Sections 4.1.1 and 4.1.2 specify a generative model of event sequences parameterized by $\Theta = \{ \Theta _ { H } , \Theta _ { E } \}$ . To learn these parameters from a training event sequence S observed in the period of $[ T _ { - } , T ]$ , a widely used strategy in the TPP literature is to minimize the negative log likelihood (NLL) of S (Shchur et al. 2021), which is formally defined as

$$
\begin{array}{l} \text { NLL } (S | \Theta) = - \log p (S) \\ \qquad = - \log P (\tau_ {L + 1} > T - t _ {L}) \\ \qquad - \sum_ {i = 1} ^ {L} \log p _ {\tau} (\tau_ {i} | \mathcal {H} _ {i - 1}) \\ \qquad - \sum_ {i = 1} ^ {L} \log p _ {m} (m _ {i} | \mathcal {H} _ {i - 1}), \end{array}\tag{12}
$$

where the likelihood $p ( S )$ of S is given by Equation (1); the time density $p _ { \tau }$ and the mark probability $p _ { m }$ are, respectively, specified by Equations (6) and (8); and $\begin{array} { r } { P ( \widehat { \tau _ { L + 1 } } > T - \widehat { t _ { L } } ) = 1 - \int _ { 0 } ^ { T - { t _ { L } } } p _ { \tau } \widehat ( \tau _ { L + 1 } | \mathcal { H } _ { L } ) d \tau _ { L + 1 } } \end{array}$ . However, learning the parameters using the NLL objective only is ineffective for the PRR problem because the NLL objective fails to cover two important features of the problem. First, the PRR problem requires to predict (infer) a sequence of events occurring in the period of $( T , T _ { + } ] .$ whereas the NLL objective trains a model to predict next event $e _ { i } = ( t _ { i } , m _ { i } )$ conditioning on the true history $\mathcal { H } _ { i - 1 }$ Such discrepancy between model training and model inference (i.e., next event prediction at model training versus next event sequence prediction at model inference) causes the model trained solely with the NLL objective not well suited to predict an event sequence in the period of $( T , T _ { + } ]$ . Second, different types of resources are not equally important for disaster relief (Pe´rez-Rodr´ıguez and Holgu´ın-Veras 2016). For example, the time delay of satisfying demands for lifesaving resources results in more severe outcomes and hence, incurs higher cost than the time delay of meeting demands for regular disaster relief resources. Therefore, it is necessary to incorporate the importance scores of different types of resources into the prediction of future demands (events) in the period of $( T , T _ { + } ]$

To capture these two features, we introduce a learning objective in addition to the NLL objective. The introduced objective trains a model to predict the next sequence of events by minimizing the expected cost-aware distance between an observed sequence and its prediction. Consider an observed sequence $S ^ { ( i , l ) }$ of l events starting from event $e _ { i } ( { \mathrm { i . e . , ~ } } S ^ { ( i , l ) } = < { \hat { e } } _ { i } , e _ { i + 1 } , \dots , e _ { i + l - 1 } >$ , which is part of the training sequence S). Using the model given in Sections 4.1.1 and 4.1.2, we can sample a prediction $\tilde { S } ^ { ( i , l ) }$ of $S ^ { ( i , l ) }$ with Algorithm 1, where $\tilde { S } ^ { ( i , l ) } = < \tilde { e } _ { i } , \tilde { e } _ { i + 1 } , . . . , \tilde { e } _ { i + l - 1 } >$ As shown, the algorithm takes the embedding vector $h _ { i - 1 }$ of past events $\mathcal { H } _ { i - 1 }$ as an input, assigns it to the historyembedding vector $\hat { h } ,$ and initializes $\tilde { \boldsymbol { S } } ^ { ( i , l ) }$ as an empty sequence (line 1). It then iteratively generates the time $\hat { t }$ (lines 3–5) and mark m ˆ (lines 6–10) of an event, conditioning on $\hat { h } ;$ updates $\hat { h }$ with the newly generated event (line 11); and adds the generated event to $\tilde { S } ^ { ( i , l ) }$ (line 12). For implementation details of sampling from the mixture lognormal distribution (line 4) and from the Poisson distribution (line 9), please refer to Online Appendix $\mathrm { { A . 3 } } .$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 (Sampling $\tilde{S}^{(l,l)}$)
Input: $h_{i-1}$: embedding vector of past events $\mathcal{H}_{i-1}, l$: sampling sequence length
Output: $\tilde{S}^{(i,l)}$
1: Set $\hat{\pmb{h}} = \pmb{h}_{i-1}, \hat{t} = t_{i-1}$, and $\tilde{S}^{(i,l)} = &lt;&gt;$
2: for $\hat{l} = 0, 1, \ldots, l-1$ do
3: Compute ($\alpha, \mu, \sigma$) from $\hat{\pmb{h}}$ via Equation (7)
4: Draw interarrival time $\hat{\tau}$ from logNormalMixture ($\alpha, \mu, \sigma$) specified by Equation (6)
5: Set event time $\hat{t} = \hat{t} + \hat{\tau}$
6: for $k = 1, 2, \ldots, K$ do
7: Compute mean of the Poisson distribution for resource type $k$ from $\hat{\pmb{h}}$ and $\hat{a}_{1:k-1}$
8: via Equation (10)
9: Sample $\hat{a}_k$ from the Poisson distribution specified by Equation (9)
10: Set $\hat{m} = (\hat{a}_1, \hat{a}_2, \ldots, \hat{a}_K)$, and $\hat{e} = (\hat{t}, \hat{m})$
11: Compute $\hat{\pmb{h}} = \text{RNN}(\hat{\pmb{h}}, \hat{e})$ via Equation (2)
12: Set $\tilde{e}_{i+\hat{l}} = \hat{e}$, $\tilde{S}^{(i,l)} = \tilde{S}^{(i,l)} \oplus &lt;\tilde{e}_{i+\hat{l}} &gt; / / \oplus$:
operator concatenating two sequences
13: return $\tilde{S}^{(i,l)}$
</div>

The cost-aware distance between an observed sequence $S ^ { ( i , l ) }$ and its prediction $\tilde { \boldsymbol { S } } ^ { ( i , l ) }$ is defined as

$$
D _ {s} (S ^ {(i, l)}, \tilde {S} ^ {(i, l)}) = \sum_ {j = 0} ^ {l - 1} D (e _ {i + j}, \tilde {e} _ {i + j}),\tag{13}
$$

where $D ( e _ { i + j } , \tilde { e } _ { i + j } )$ denotes the cost-aware distance between an observed event $e _ { i + j }$ in $S ^ { ( i , l ) }$ and its corresponding predicted event $\tilde { \boldsymbol { e } } _ { i + j }$ in $\tilde { \boldsymbol { S } } ^ { ( i , l ) }$ . In general, the cost-aware distance $D ( e , \tilde { e } )$ between an observed event e and its prediction e ˜ is defined as

$$
\begin{array}{c} D (e, \tilde {e}) = - \sum_ {k = 1} ^ {K} \log \left(\left(\frac {1}{c _ {k}}\right) ^ {(t - \tilde {t}) ^ {2}} \left(\frac {1}{c _ {k}}\right) ^ {(a _ {k} - \tilde {a} _ {k}) ^ {2}}\right) \\ = \sum_ {k = 1} ^ {K} (t - \tilde {t}) ^ {2} \log c _ {k} + \sum_ {k = 1} ^ {K} (a _ {k} - \tilde {a} _ {k}) ^ {2} \log c _ {k}, \end{array}\tag{14}
$$

where t and ${ \tilde { t } } ,$ respectively, denote the time of event e and its prediction; the notation $a _ { k }$ and $\tilde { \boldsymbol { a } } _ { k } ,$ respectively, represent the units of type k resources requested by the event and its prediction; and $c _ { k } > 1$ is the importance score of type $\hat { k }$ resources, with higher score meaning more important for disaster relief, $k = 1 , 2 , \dots , K .$ . Our design of Equation (14) is based on the intuition that the cost-aware distance between an event and its prediction is the aggregation of their discrepancies across all resource types, and the discrepancy in each resource type is assessed from two perspectives: the cost-aware time difference as measured by $( t - \tilde { t } ) ^ { 2 }$ log $c _ { k }$ and the costaware quantity difference as computed by $( a _ { k } - \tilde { a } _ { k } ) ^ { 2 }$ log $c _ { k } .$ . Importance score $c _ { k }$ models the degree of importance of satisfying demands for type k resources. According to Equation (14), prediction errors on time and quantities $( \mathrm { i . e . , ~ } ( t - \tilde { t } ) ^ { 2 }$ and $( a _ { k } - \tilde { a } _ { k } ) ^ { 2 } )$ ) lead to larger $\bar { D } ( e , \tilde { e } )$ for events requesting higher importance resources (i.e., larger $c _ { k } )$ . Consequently, a model trained to minimize $D _ { s } ( S ^ { ( i , l ) } , \tilde { S } ^ { ( i , l ) } )$ places more focus on reducing prediction errors for events requesting higher importance resources, which in turn, reduces the overall cost for disaster relief because time delays of satisfying requests for higher importance resources result in higher costs. In this sense, distances defined in Equations (13) and (14) are cost-aware distances. In addition, $D _ { s } ( S ^ { ( i , l ) }$ , $\tilde { \boldsymbol { S } } ^ { ( i , l ) } )$ ) measures the cost-aware distance between an observed sequence and its prediction; hence, a model trained on it can effectively predict a sequence of future events. In short, our design of $D _ { s } ( S ^ { ( i , l ) } , \tilde { S } ^ { ( i , l ) } )$ captures both features of the PRR problem discussed at the begin ning of this subsection.

It is more robust to sample many predictions of an observed sequence and train a model on the expected cost-aware distance between an observed sequence and its prediction. Accordingly, for an observed sequence $S ^ { ( i , l ) }$ starting from event $e _ { i }$ with length l, the expected cost-aware distance between the sequence and its prediction is given by

$$
E _ {\tilde {S} ^ {(i, l)}} \left(D _ {s} (S ^ {(i, l)}, \tilde {S} ^ {(i, l)})\right) = \int D _ {s} (S ^ {(i, l)}, \tilde {S} ^ {(i, l)}) p (\tilde {S} ^ {(i, l)} | \mathcal {H} _ {i - 1}) d \tilde {S} ^ {(i, l)},\tag{15}
$$

where $D _ { s } ( S ^ { ( i , l ) } , \tilde { S } ^ { ( i , l ) } )$ can be computed using Equation (13) and $p ( \tilde { S } ^ { ( i , l ) } | \mathcal { H } _ { i - 1 } )$ denotes the density of $\tilde { \boldsymbol { S } } ^ { ( i , l ) }$ conditioning on the observed history $\mathcal { H } _ { i - 1 }$ . The expected distance computed using Equation (15) is for a given pair of starting event $e _ { i }$ and sequence length l. We can further randomly pick an event in the training sequence $S$ as $e _ { i }$ and sample a sequence length $l . ^ { 5 }$ Accordingly, we can define our proposed learning objective, cost-aware sequence distance (CSD), as the expected cost-aware distance between an observed sequence and its prediction expected on $e _ { i } , l ,$ and $\tilde { \boldsymbol { S } } ^ { ( i , l ) }$ :

$$
\operatorname{CSD} (S | \Theta) = E _ {e _ {i}} E _ {l} E _ {\tilde {S} ^ {(i, l)}} \left(D _ {s} \left(S ^ {(i, l)}, \tilde {S} ^ {(i, l)}\right)\right).\tag{16}
$$

The CSD objective has no closed-form solution and can be computed using the Monte Carlo method (Bishop 2006), which repeatedly samples $e _ { i } , l ,$ , and $S ^ { ( i , l ) } ;$ generates a prediction S<sup>˜</sup> of S<sup>(i,</sup> <sup>l)</sup> with Algorithm $\tilde { \boldsymbol { S } } ^ { ( i , l ) }$ $S ^ { ( i , l ) }$ $1 ;$ and computes the cost-aware distance between $S ^ { ( i , l ) }$ and $\tilde { \boldsymbol { S } } ^ { ( i , l ) }$ using Equation (13) until convergence. Lastly, the learning object of CNM-TPP is given by

$$
\mathcal {L} (S | \Theta) = \mathrm{CSD} (S | \Theta) + \gamma \mathrm{NLL} (S | \Theta),\tag{17}
$$

where NLL(S|Θ) is specified by Equation (12), and hyperparameter $\gamma > 0$ controls the relative contribution of its two component objectives.

Our proposed model, CNM-TPP, is trained with the observed sequence S of events (demands) in the period of $[ T _ { - } , T ]$ , where $S = < e _ { 1 } , e _ { 2 } , \ldots , e _ { L } >$ . Specifically, the objective NLL(S|Θ) is derived with Equation (12), and the objective CSD(S|Θ) is computed according to Equation (16) with the Monte Carlo method. The model parameters Θ of CNM-TPP are then learned by optimizing its learning objective specified by Equation (17) through gradient descent. Once trained, CNM-TPP can infer a sequence of future events (demands) in the period of $( T , ^ { - } T _ { + } ]$ using a procedure similar to Algorithm 1 with two modifications. First, it takes the embedding vector h of past events $\mathcal { H } _ { L }$ as an input, where $H _ { L }$ is the training sequence S and $h _ { L }$ can be computed using Equation (2). Second, the inferred sequence of events must be within the time interval of $( T , T _ { + } ]$ . The inference procedure is given in Online Appendix A.4.

In comparison with existing TPPs, our proposed CNM-TPP features three methodological novelties. First, in consideration of the two critical features of the PRR problem (i.e., heterogeneous importance of disaster relief resources and prediction of the future sequence of demands), we develop a novel learning objective to train our CNM-TPP model. The CSD learning objective is instantiated through our proposed Equations (13), (14), and (16) as well as Algorithm 1. Second, we define a new mark-embedding function in Equation (4), which mod els an event mark containing both types and quantities of requested resources. Third, the event generation layer of our TPP effectively captures the correlations among different types of resources requested in a demand through Equations (8)–(10).

4.2. Resource Request Optimization and Solution The CNM-TPP model in Section 4.1 allows us to predict future demands between T and $T _ { + }$ . In this section, we propose a stochastic optimization model to determine the requested quantity $x _ { k }$ for each resource type $k ,$ $k = 1 , 2 , \ldots , K ,$ based on the predicted future demands.

Let $Q _ { k } = < ( t _ { i } ^ { k } , q _ { i } ^ { k } ) , j = 1 , \hat { 2 } , . . . , n ^ { k } >$ be the stochastic sequence of future demands for type k resources between T and $T _ { + , }$ , where $t _ { j } ^ { k }$ is the arrival time of the jth demand, $q _ { j } ^ { k }$ is the corresponding demand quantity, and $n ^ { k }$ is the number of demand arrivals during period $( T , T _ { + } ]$ . Denote $\textstyle | Q _ { k } | = \sum _ { j = 1 } ^ { n ^ { k } } q _ { j } ^ { k }$ to be the total amount of type k resources requested by victims during the period. Clearly, the cost because of time delays of meeting the demands for type k resources by time $\dot { T } .$ <sub>+</sub> depends on the quantity of unfulfilled demands $U _ { k }$ or the quantity of remaining resources $R _ { k }$ available at time $T ,$ , future demands $Q _ { k }$ occurring between $T$ and $T _ { + }$ , and the quantity of requested resources $x _ { k }$ . Denote the corresponding cost as $\bar { f _ { k } } ( x _ { k } , Q _ { k } , U _ { k } , R _ { k } )$ ). Let W be the transportation capacity and $w _ { k }$ be the capacity consumed while shipping one unit of resource $k , \stackrel { . } { k } = 1 , 2 , \ldots , K$ . Then, the proactive resource request problem can be formulated as the following stochastic optimization problem:

$$
\begin{array}{r l} \underset {\mathcal {X}} {\min} & E _ {\mathcal {Q}} \left(\sum_ {k = 1} ^ {K} f _ {k} (x _ {k}, Q _ {k}, U _ {k}, R _ {k})\right) \\ \text {s.t.} & \sum_ {k = 1} ^ {K} w _ {k} x _ {k} \leq W \\ & x _ {k} \in \mathbb {Z} ^ {+}, k = 1, 2, \ldots , K, \end{array}\tag{18}
$$

where the expectation is taken over the stochastic future demand sequence $\mathcal { Q } = ( Q _ { 1 } , Q _ { 2 } , \ldots , Q _ { K } )$ of all resource types, the decision variables $\mathcal { X } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { K } )$ represent the requested quantities for resources of all types, and $\mathbb { Z } ^ { + }$ consists of positive integers and zero.

We take three steps to solve the stochastic optimization problem. First, we define the cost function and convert the cost minimization problem to a cost reduction maximization problem. In the second step, because Q is a highly nonstationary stochastic process, we propose to solve the stochastic optimization problem using demand arrivals generated by the CNM-TPP model. We show that the optimal solution based on demand generation converges uniformly to that of the stochastic optimization as the sample size increases. Finally, because the optimization problem with the generated demands is an integer program and by itself an Non-deterministic Polynomial-time hardness (NP-hard) problem, we design an efficient greedy heuristic algorithm to obtain an approximate solution. To ensure the solution quality, we show that the objective function is concave and piecewise linear with respect to (w.r.t.) the decision variables (resource request allocation ${ \mathcal { X } } ) ,$ which allows us to provide a performance guarantee for the approximate solution.

4.2.1. Conversion and Simplification of Optimization Problem (18). We model the cost $f _ { k } ( )$ in the stochastic optimization Problem (18) as the deprivation cost, which measures the economic value of human suffering because of the deprivation of vital resources (Holgu´ın-Veras et al. 2013, Pe´rez-Rodr´ıguez and Holgu´ın-Veras 2016). In this study, we adopt the exponential deprivation cost widely used in postdisaster resource management models (Holgu´ın-Veras et al. 2013):

$$
\gamma (\delta) := e ^ {\phi + b c \delta} - e ^ {\phi},\tag{19}
$$

where $\delta$ is the amount of time delay it takes to meet a demand, $c$ measures the importance of the demanded resource, and $\phi$ and b are deprivation parameters originally defined in Holgu´ın-Veras et al. (2013). Now, consider a demand of one unit of type k resources that arrives at time $t \in \left( T , T _ { + } \right]$ . If at time $\dot { T } ,$ we have requested sufficient type k resources, which will arrive at time $T _ { + \prime }$ to meet this demand, the deprivation cost would be $e ^ { \phi + b c _ { k } ( T _ { + } - t ) } - e ^ { \phi }$ , where $c _ { k }$ is the importance score of type k resources introduced in Section 4.1. Otherwise, the demand will not be met until some future time $\xi _ { k } \left( \xi _ { k } > T _ { + } \right)$ such as the next delivery of resource k. In this case, the deprivation cost increases to $e ^ { \phi + b c _ { k } ( \xi _ { k } - t ) } - e ^ { \phi }$ . Consequently, the reduction in deprivation cost, because of the unit of type k resources requested at $T ,$ is given by

$$
\begin{array}{c} B ^ {k} (t) = (e ^ {\phi + b c _ {k} (\xi_ {k} - t)} - e ^ {\phi}) - (e ^ {\phi + b c _ {k} (T _ {+} - t)} - e ^ {\phi}) \\ = e ^ {\phi - b c _ {k} t} (e ^ {b c _ {k} \xi_ {k}} - e ^ {b c _ {k} T _ {+}}). \end{array}\tag{20}
$$

Clearly, the deprivation cost reduction $B ^ { k } ( t )$ is a monotone convex decreasing function of t. Therefore, fulfilling an earlier demand leads to a more significant cost reduction than fulfilling a later one, and a local agency should dispatch resources on a first come, first serve basis.

We next construct the sequence of net demands $\tilde { Q } _ { k } , k = 1 , 2 , \ldots , K ,$ , waiting to be fulfilled by time $T _ { + }$ . It depends on the arrivals of future demands $Q _ { k } ,$ and unfulfilled demands or remaining resources at time T. If the quantity of unfulfilled demands $U _ { k } \neq 0 .$ , then $| \tilde { Q } _ { k } |$ $= | Q _ { k } | + U _ { k }$ . We obtain $\tilde { Q } _ { k }$ by merging unfulfilled demands with future demands $Q _ { k } .$ . If the quantity of remaining resources $R _ { k } \neq 0 ,$ , then $| \tilde { Q } _ { k } | = | Q _ { k } \bar { | } - R _ { k }$ . We form $\tilde { Q } _ { k }$ by removing the first $R _ { k }$ units of demands from $Q _ { k }$ . We denote the sequence of net demands as $\tilde { \tilde { Q } } _ { k } = < ( \tilde { t } _ { i } ^ { k } , \tilde { q } _ { i } ^ { k } ) , j = 1 , 2 , . . . , \tilde { n } ^ { k } >$ , where $\tilde { n } ^ { k }$ is the number of demands in $\tilde { Q } _ { k } .$ . The following example illustrates the construction of $\tilde { Q } _ { k }$ .

Example 3. Continue with Example 1. Consider the following future demands between $[ T , T _ { + } ]$ (Table 2).

According to Example 1, we have $U _ { s h e l t e r } = 2 , R _ { s h e l t e r }$ $= 0 , U _ { f o o d } = 0 \AA$ , and $R _ { f o o d } = 4$ at time T. Because there are two units of unfulfilled demand for shelter at time $T$ and one unit of new request between T and $T _ { + , }$ , we form $\tilde { Q } _ { s h e l t e r } = < ( \tilde { t } _ { 1 } ^ { s h e l t e r } , \tilde { q } _ { 1 } ^ { s h e l t e r } ) , ( \tilde { t } _ { 2 } ^ { s h e l t e r } , \tilde { q } _ { 2 } ^ { s h e l t e r } ) > ,$ , where $\tilde { t } _ { 1 } ^ { s h e l t e r } = { ' } 2 0 2 1 / 0 7 / 1 8 1 6 : 3 8 : 2 6 ^ { \prime } , \tilde { q } _ { 1 } ^ { \mathrm { s h e l t e r } } = 2 , \tilde { t } _ { 2 } ^ { s h e l t e r } = { ' } 2 0 2 1 /$ $0 7 / 1 8 1 8 : 0 8 : 1 2 ^ { \prime } , \tilde { q } _ { 2 } ^ { \mathrm { s h e l t e r } } = 1 , \tilde { n } ^ { \mathrm { s h e l t e r } } = 2 ,$ , and $| \tilde { Q } _ { s h e l t e r } | = 3 .$ The agency uses four units of food remaining at time T to partially fulfill the food request in demand 3. We have $\tilde { Q } _ { f o o d } = < ( \tilde { t } _ { 1 } ^ { f o o d } , \tilde { q } _ { 1 } ^ { f o o d } ) , ( \tilde { t } _ { 2 } ^ { f o o d } , \tilde { q } _ { 2 } ^ { f o o d } ) > _ { \it { I } }$ , where $\tilde { t } _ { 1 } ^ { f o o d } = { } ^ { \prime } 2 0 2 1 /$ $0 7 / 1 8 1 8 : 0 8 : 1 2 ^ { \prime } , \tilde { q } _ { 1 } ^ { \mathrm { f o o d } } = 1 , \tilde { t } _ { 2 } ^ { f o o d } = { ' } 2 0 2 1 / 0 7 / 1 8 1 9 : 1 4 : 2 9 ^ { \prime } ,$ $\tilde { q } _ { 2 } ^ { \mathrm { f o o d } } = 3 , \tilde { n } ^ { \mathrm { f o o d } } = 2 ,$ , and $| \tilde { Q } _ { f o o d } | = 4$

We are now ready to figure out the cost reduction $g _ { k } ( x _ { k } , \tilde { Q } _ { k } )$ if $x _ { k }$ units of resources, requested at time $T ,$ will be available at time $T _ { + }$ <sub>+</sub> to meet the sequence of net demands $\tilde { Q } _ { k } , k = 1 , 2 , \ldots , K .$ . Denote $B _ { j } ^ { k } = B ^ { k } ( \tilde { t } _ { j } ^ { k } )$ , where $\tilde { t } _ { j } ^ { k }$ is arrival time of the jth demand in $\tilde { Q } _ { k }$ and $B ^ { k } ( \tilde { t } _ { i } ^ { k } )$ is given by Equation $( 2 0 ) , j = 1 , 2 , \ldots , \tilde { n } ^ { k }$ . Because $\tilde { t } _ { 1 } ^ { k } \le \tilde { t } _ { 2 } ^ { k } \le$ $\cdots \leq \tilde { t } _ { \tilde { n } ^ { k } . } ^ { k }$ , by Equation (20), we have

$$
B _ {1} ^ {k} \geq B _ {2} ^ {k} \geq \dots \geq B _ {\tilde {n} ^ {k}} ^ {k}.\tag{21}
$$

Consequently, $x _ { k }$ units of resources should be allocated to fulfill the demands according to their arrival times in $\tilde { Q } _ { k } ,$ first come, first serve. Let $J ^ { k }$ be the largest sequence index J such that $\textstyle \sum _ { j = 1 } ^ { J } { \tilde { q } } _ { j } ^ { k } \leq x _ { k }$ : Then, the total cost reduction because of $x _ { k }$ units of requested resources is given by

$$
g _ {k} (x _ {k}, \tilde {Q} _ {k}) = \left\{ \begin{array}{l l} \sum_ {j = 1} ^ {J ^ {k}} \tilde {q} _ {j} ^ {k} B _ {j} ^ {k} + \left(x _ {k} - \sum_ {j = 1} ^ {J ^ {k}} \tilde {q} _ {j} ^ {k}\right) B _ {J ^ {k} + 1} ^ {k} & \text {if x_{k} <  | \tilde {Q} _{k} |}, \\ \sum_ {j = 1} ^ {\tilde {n} ^ {k}} \tilde {q} _ {j} ^ {k} B _ {j} ^ {k} & \text {if x_{k} \geq |\tilde {Q} _{k}|}. \end{array} \right.\tag{22}
$$

Because cost minimization is equivalent to the cost reduction maximization, with this preparation, we are able to simplify the original stochastic optimization Problem (18) as follows:

Table 2. Future Demands Between [T, T ]

<table><tr><td>Demand identification</td><td>Demand time</td><td>Type of resources requested</td><td>Quantity of resources requested</td></tr><tr><td>3</td><td>July 18, 2021 18:08:12</td><td>Shelter</td><td>1</td></tr><tr><td>3</td><td>July 18, 2021 18:08:12</td><td>Food</td><td>5</td></tr><tr><td>4</td><td>July 18, 2021 19:14:29</td><td>Food</td><td>3</td></tr></table>

$$
\max _ {\mathcal {X}} \quad \mathcal {G} (\mathcal {X}) := E _ {\tilde {\mathcal {Q}}} \left(\sum_ {k = 1} ^ {K} g _ {k} (x _ {k}, \tilde {Q} _ {k})\right)
$$

$$
\begin{array}{l l} \text {subject to (s.t.)} & \sum_ {k} w _ {k} x _ {k} \leq W, \\ & x _ {k} \in \mathbb {Z} ^ {+}, \quad k = 1, 2, \ldots , K, \end{array}\tag{23}
$$

where the expectation is taken over $\tilde { \mathcal { Q } } = ( \tilde { Q } _ { 1 } , \tilde { Q } _ { 2 } , \dots , \tilde { Q } _ { K } )$

4.2.2. Sample Average Approximation of Stochastic Optimization. It is difficult to precisely evaluate the expected deprivation cost reduction $E _ { \tilde { \mathcal { Q } } } ( \dot { \sum } _ { k } g _ { k } ( x _ { k } , \tilde { Q } _ { k } ) )$ in Problem (23) because the underlying stochastic process Q <sup>˜</sup> is highly nonstationary. Instead, we follow the sample average approximation (SAA) method (Kim et al. 2015) to obtain its approximation by generating a sufficient number of samples of $\tilde { \mathcal { Q } }$ . To generate a sample of $\tilde { \mathcal { Q } } ,$ we use the inference procedure of the CNM-TPP model given in Online Appendix A.4 to predict future demands in (T, T<sub>+</sub>] and then construct a sample of $\tilde { \mathcal { Q } }$ with the predicted future demands (e.g., see Example 3). Let $\tilde { \boldsymbol { \mathcal { Q } } } ^ { ( \psi ) } =$ $( \tilde { \cal Q } _ { 1 } ^ { ( \psi ) } , \tilde { \cal Q } _ { 2 } ^ { ( \psi ) } , \dots , \tilde { \cal Q } _ { K } ^ { ( \psi ) } )$ be a sample of $\tilde { \mathcal { Q } } , \psi = 1 , 2 , \hdots , \Psi ,$ and Ψ is the number of samples. We have the following approximation for the expected deprivation cost reduction:

$$
E _ {\tilde {Q}} \left(\sum_ {k = 1} ^ {K} g (x _ {k}, \tilde {Q} _ {k})\right) \approx \frac {1}{\Psi} \sum_ {\psi = 1} ^ {\Psi} \sum_ {k = 1} ^ {K} g _ {k} (x _ {k}, \tilde {Q} _ {k} ^ {(\psi)}).\tag{24}
$$

As a result, we obtain the following SAA of the stochastic optimization Problem (23):

$$
\begin{array}{l l} \max _ {\mathcal {X}} & \mathcal {G} ^ {\Psi} (\mathcal {X}) := \frac {1}{\Psi} \sum_ {\psi = 1} ^ {\Psi} \sum_ {k = 1} ^ {K} g _ {k} (x _ {k}, \tilde {Q} _ {k} ^ {(\psi)}) \\ \text {s.t.} & \sum_ {k} w _ {k} x _ {k} \leq W, \\ & x _ {k} \in \mathbb {Z} ^ {+}, \quad k = 1, 2, \ldots , K. \end{array}\tag{25}
$$

Notice that the SAA converts a stochastic optimization problem to a deterministic optimization problem because the objective function $\mathcal { G } ^ { \Psi } ( \chi )$ is now a deterministic function of X. Even though Problem (25) remains a difficult problem to solve, the conversion allows us to explore the special structure of $\mathcal { G } ^ { \Psi } ( \mathcal { X } )$ and design an efficient and effective approximation algorithm, to be discussed in the next subsection.

Next, we provide a theoretical justification that the proposed SAA is a valid and accurate solution approach. More specifically, we show that the optimal objective function value of the deterministic optimization Problem (25) converges to that of the original stochastic optimization Problem (23) as the sample size increases.

Theorem 1. Let $\pi ^ { * }$ and $\Pi _ { \Psi } ^ { * }$ be the optimal objective function values of Problems (23) and (25), respectively. We

have

$$
\lim _ {\Psi \to \infty} \sup | \Pi_ {\Psi} ^ {*} - \pi^ {*} | = 0.
$$

Proof. See Online Appendix C. w

By Theorem $1 , \Pi _ { \Psi } ^ { * }$ is a consistent estimator of $\pi ^ { * }$ as $\Psi  \infty ,$ , which provides a theoretical support for solving the complicated stochastic optimization Problem (23) via the SAA Problem (25).

4.2.3. A Greedy Algorithm for Problem (25). The opti mization Problem (25) resulted from the SAA; however, it remains a difficult problem to be solved efficiently. As shown in the following theorem, it is a nonlinear knapsack problem and belongs to a class of NP-hard problems.

Theorem 2. The optimization Problem (25) is NP hard.

Proof. See Online Appendix D. w

Given the hardness of the problem, we design a heuristic solution procedure by careful exploring the special structure of the problem. We start by analyzing the properties of the objective function $\mathcal { G } ^ { \Psi } ( \breve { \mathcal { X } } )$ . Denote

$$
\mathcal {G} _ {k} ^ {\Psi} (x _ {k}) = \frac {1}{\Psi} \sum_ {\psi = 1} ^ {\Psi} g _ {k} (x _ {k}, \tilde {Q} _ {k} ^ {(\psi)}), k = 1, 2, \ldots , K.\tag{26}
$$

We thus have $\begin{array} { r } { \mathcal { G } ^ { \Psi } ( \mathcal { X } ) = \sum _ { k } \mathcal { G } _ { k } ^ { \Psi } ( x _ { k } ) } \end{array}$ , and Problem (25) can be rewritten as

$$
\begin{array}{l l} \max _ {\mathcal {X}} & \sum_ {k = 1} ^ {K} \mathcal {G} _ {k} ^ {\Psi} (x _ {k}) \\ \text {s.t.} & \sum_ {k} w _ {k} x _ {k} \leq W, \\ & x _ {k} \in \mathbb {Z} ^ {+}, k = 1, 2, \ldots , K. \end{array}\tag{27}
$$

It turns out that function $\mathcal { G } _ { k } ^ { \Psi } ( \cdot )$ has some nice structural properties, which allow us to design an efficient greedy heuristic to solve Problem (25).

Proposition 1. Function $\mathcal { G } _ { k } ^ { \Psi } ( \cdot )$ is (i) continuous piecewise linear, (ii) monotonically nondecreasing, and (iii) concave, $k = 1 , 2 , \ldots , K .$

Proof. Notice that $\mathcal { G } _ { k } ^ { \Psi } ( x _ { k } )$ is a linear combination (average) of $g _ { k } ( x _ { k } , \tilde { Q } _ { k } )$ . Because $g _ { k } ( x _ { k } , \tilde { Q } _ { k } )$ has the three properties, as shown by Proposition EC.1 in Online Appendix C.1, so does $\check { \mathcal { G } } _ { k } ^ { \Psi } ( x _ { k } )$ w

To design a greedy algorithm for Problem (27), we need to identify all nondifferential points (i.e., kinks) of $\mathcal { G } _ { k } ^ { \Psi } ( x _ { k } ) , k = 1 , 2 , \ldots , K$ as well as the left and right derivatives (slopes) around each kink. Because $\mathcal { G } _ { k } ^ { \Psi } ( x _ { k } )$ ) is a linear combination of $g _ { k } ( x _ { k } , \tilde { Q } _ { k } ^ { ( \psi ) } )$ , any kink of the later function is also a kink of the former function. Notice also that for each function $g _ { k } ( x _ { k } , \tilde { Q } _ { k } ^ { ( \psi ) } )$ , a kink occurs as a demand in $\tilde { Q } _ { k } ^ { ( \psi ) }$ occurs. Now, consider a kink of $\mathcal { G } _ { k } ^ { \Psi } ( x _ { k } )$ associated with the ith demand in $\tilde { Q } _ { k } ^ { ( \psi ) }$ that occurs at time $\tilde { t } _ { i } ^ { k , ( \psi ) }$ <sup>)</sup>. The corresponding location of the kink in the $x _ { k }$ axis (the quantity of requested resources $x _ { k } )$ is given by the following quantity:

$$
\begin{array}{r l} & s _ {i} ^ {k, (\psi)} = \sum_ {j = 1} ^ {i} \tilde {q} _ {j} ^ {k, (\psi)}, \quad \psi \in \{1, 2, \ldots , \Psi \}, \\ & i \in \{1, 2, \ldots , \tilde {n} ^ {k, (\psi)} \}, \quad k = 1, 2, \ldots , K. \end{array}\tag{28}
$$

Next, we show how to calculate the left and right derivatives of $\mathcal { G } _ { k } ^ { \Psi } ( x _ { k } )$ at $x _ { k } = s _ { i } ^ { k , ( \psi ) }$ . Let $J ( k , \psi , \varphi , i )$ be the first demand in $\tilde { Q } _ { k } ^ { \left( \varphi \right) }$ whose request for type k resource cannot be fully met given $s _ { i } ^ { k , ( \psi ) }$ units of type k resource, $\varphi = 1 , 2 ,$ $\ldots , \Psi$ . That is,

$$
J (k, \psi , \varphi , i) = \min j \in \{1, \dots , \tilde {n} ^ {k, (\varphi)} \} | s _ {j} ^ {k, (\varphi)} \geq s _ {i} ^ {k, (\psi)}.
$$

Then, the left derivative of $\mathcal { G } _ { k } ^ { \Psi } ( x _ { k } )$ at $s _ { i } ^ { k , ( \psi ) }$ (the slope to the left of the kink) is given by

$$
\mathcal {G} _ {k} ^ {\Psi^ {\prime}} (s _ {i} ^ {k, (\psi) -}) = \frac {1}{\Psi} \sum_ {\varphi = 1} ^ {\Psi} \left(B ^ {k} \Big (\tilde {t} _ {J (k, \psi , \varphi , i)} ^ {k, (\varphi)} \Big) \times \mathbb {1} \left(s _ {i} ^ {k, (\psi)} \leq | \tilde {Q} _ {k} ^ {(\varphi)} |\right)\right),\tag{29}
$$

and the right derivative (the slope to the right of the kink) is given by

$$
\mathcal {G} _ {k} ^ {\Psi^ {\prime}} \left(s _ {i} ^ {k, (\psi) +}\right) = \mathcal {G} _ {k} ^ {\Psi^ {\prime}} \left(s _ {i} ^ {k, (\psi) -}\right) - \frac {1}{\Psi} \left(B ^ {k} \left(\tilde {t} _ {i} ^ {k, (\psi)}\right) - B ^ {k} \left(\tilde {t} _ {i + 1} ^ {k, (\psi)}\right)\right).\tag{30}
$$

Because the second term in the right derivative is negative, the right slope is smaller than the left slope, which implies that $\mathcal { G } _ { k } ^ { \Psi } ( x _ { k } )$ is concave already defined $x _ { k } .$

Now, we are in a position to present the greedy algorithm. To facilitate the description, we relabel all kinks and slopes of $\mathcal { G } _ { k } ^ { \Psi } ( x _ { k } )$ by sorting them according to the arrival times of their associated demands. For simplicity, we assume Ψ to be a fixed constant in the remaining exposition. Let $s _ { i } ^ { k } , i = 1 , 2 , \ldots , M ^ { k }$ be all kinks of function $\mathcal { G } _ { k } ^ { \bar { \Psi } } ( x _ { k } )$ , as calculated by Equation (28), such that $0 \leq s _ { 1 } ^ { k } \leq , \ldots , \leq s _ { M ^ { k } } ^ { k }$ , where $\begin{array} { r } { M ^ { k } = \sum _ { \psi = 1 } ^ { \Psi } \tilde { n } ^ { k , ( \psi ) } } \end{array}$ . Let $\overline { { \boldsymbol B } } _ { i } ^ { k }$ be the ith slope of function $\mathcal { G } _ { k } ^ { \Psi } ( x _ { k } )$ for all $x _ { k } \in ( s _ { i - 1 } ^ { k } , s _ { i } ^ { k } )$ . Suppose $s _ { i } ^ { k }$ is the kink associated with <sup>˜</sup>ith demand in $\tilde { Q } _ { k } ^ { ( \psi ) }$ $( \mathrm { i . e . , } s _ { i } ^ { k } = s _ { \tilde { i } } ^ { k , ( \psi ) } )$ . Accordingly, $\boldsymbol { \cdot } \overline { { B } } _ { i } ^ { k }$ can be calculated by

$$
\begin{array}{l} \overline {{B}} _ {i} ^ {k} = \mathcal {G} _ {k} ^ {\Psi^ {\prime}} (s _ {i} ^ {k -}) = \mathcal {G} _ {k} ^ {\Psi^ {\prime}} (s _ {\tilde {i}} ^ {k, (\psi) -}) \\ \qquad = \frac {1}{\Psi} \sum_ {\varphi = 1} ^ {\Psi} \left(B ^ {k} \left(\tilde {t} _ {J (k, \psi , \varphi , \tilde {i})} ^ {k, (\varphi)}\right) \times \mathbb {1} \left(s _ {\tilde {i}} ^ {k, (\psi)} \leq | \tilde {Q} _ {k} ^ {(\varphi)} |\right)\right). \end{array}\tag{31}
$$

In view of Proposition 1 and the discussion, we have $\overline { { { B } } } _ { 1 } ^ { k } \geq \overline { { { B } } } _ { 2 } ^ { k } \geq , \mathrm { . . . , } \geq \overline { { { B } } } _ { M ^ { k } } ^ { k } \geq 0$ : We start by ranking all slopes in descending order according to the ratio $\overline { { B } } _ { i } ^ { k } / w _ { k }$ among all resource types $k = 1 , 2 , \dots , K$ and slopes $i = 1 , 2 , \dots ,$ $M ^ { k }$ . Suppose the resulting sequence is $\mathcal { P } .$ . Our proposed greedy algorithm decides quantities of requested resources by following sequence $\mathcal { P }$ because the ratio reflects the current effectiveness of type k resources in terms of reducing the deprivation cost, relative to its capacity consumption. Let κ(ρ) be the type of requested resource associated with the ρth slope in sequence $\mathcal { P }$ and $I _ { k } ( \rho )$ be the total number of slopes associated with type k resource request among the top $\rho$ ranked slopes in sequence $\mathcal { P } _ { \cdot }$ . The greedy algorithm then follows sequence $\mathcal { P }$ to iteratively decide the requested quantity of type k resources as follows:

$$
x _ {k} (\rho) = \left\{ \begin{array}{l l} s _ {I _ {k} (\rho)} ^ {k} & \text {if} I _ {k} (\rho) \neq 0, \\ 0 & \text {otherwise}, \end{array} \right. k = 1, 2, \ldots , K.\tag{32}
$$

The greedy algorithm stops when the shipping capacity constraint is violated for the first time. The corresponding sequence index is given by

$$
\rho_ {W} = \min \rho \in \{1, 2, \ldots , | \mathcal {P} | \} | \sum_ {k = 1} ^ {K} w _ {k} x _ {k} (\rho) \geq W.\tag{33}
$$

If the inequality in (33) holds as an equality, then we obtain an optimal solution to Problem (27): $\mathcal { X } ^ { \ast } = ( x _ { 1 } ^ { \ast } ,$ $\cdots , x _ { K } ^ { * } )$ , where $x _ { k } ^ { * } = x _ { k } ( \rho _ { W } ) , k = 1 , 2 , \ldots , K .$ Otherwise, we keep x<sup>∗</sup> for all resource types except type $\kappa ( \rho _ { w } )$ , which is currently a less effective resource type relative to others ranked higher in sequence $\mathcal { P } .$ Denote this critical type $\kappa ( \rho _ { W } )$ as $k ^ { \circ }$ . We reduce the requested quantity for resource type $k ^ { \circ }$ until the total capacity is satisfied, which results in the following maximum fractional requested quantity for resource type $k ^ { \circ }$ :

$$
\tilde {x} _ {k ^ {\circ}} = \frac {1}{w _ {k ^ {\circ}}} \left(W - \sum_ {k \neq k ^ {\circ}} w _ {k} x _ {k} (\rho_ {W})\right).\tag{34}
$$

Let $x _ { k ^ { \circ } } = \lfloor \tilde { x } _ { k ^ { \circ } } \rfloor$ be the integer portion of $\tilde { x } _ { k ^ { \circ } }$ . Then, our greedy algorithm generates the following feasible solution to Problem (27):

$$
\mathcal {X} ^ {g} = (x _ {1} ^ {g}, \ldots , x _ {K} ^ {g}), \mathrm{where}
$$

$$
x _ {k} ^ {g} = \left\{ \begin{array}{l l} x _ {k} (\rho_ {W}) & \text { if } k \neq k ^ {\circ}, \\ x _ {k ^ {\circ}} & \text { if } k = k ^ {\circ}, \end{array} \right. k = 1, 2, \ldots , K.\tag{35}
$$

To evaluate the performance of the greedy algorithm, we compare the cost reduction $\Pi _ { \Psi } ^ { g }$ by the greedy algorithm versus the optimal cost reduction Π<sup>∗</sup> of Problem $( 2 7 ) ,$ where $\Pi _ { \Psi } ^ { g } = \stackrel { \bullet } { g } ^ { \Psi } ( \mathcal { X } ^ { g } )$ and $\mathcal { X } ^ { g }$ is the solution to the problem by the greedy algorithm. We have the following performance guarantee for the greedy algorithm.

Theorem 3. $\Pi _ { \Psi } ^ { g } \ge \Pi _ { \Psi } ^ { * } - \overline { { B } } _ { I } ^ { k ^ { \circ } }$ , where $k ^ { \circ } = k ( \rho _ { W } )$ and $I ^ { \circ } =$ $I _ { k ^ { \circ } } ( \rho _ { W } )$

Proof. Consider the following continuous solution to Problem (27), which differs from $\mathcal { X } ^ { g }$ on only the requested quantity for resource type $k ^ { \circ }$ :

$$
\begin{array}{l} \mathcal {X} ^ {c} = (x _ {1} ^ {c}, \ldots , x _ {K} ^ {c}), \\ \text {where} x _ {k} ^ {c} = \left\{ \begin{array}{l l} x _ {k} (\rho_ {W}) & \text {if} k \neq k ^ {\circ}, \\ \tilde {x} _ {k ^ {\circ}} & \text {if} k = k ^ {\circ}, \end{array} \right. k = 1, 2, \ldots , K. \end{array}
$$

By Proposition 1, the objective function is continuous and concave. Consequently, $\mathcal { X } ^ { c }$ is an optimal solution for Problem (27) without the integer constraint and $\mathcal G ^ { \Psi } ( \mathcal X ^ { c } ) \geq \Pi _ { \Psi } ^ { * }$ . We have

$$
\begin{array}{r l} & {\Pi_ {\Psi} ^ {*} - \Pi_ {\Psi} ^ {g} \leq \mathcal {G} ^ {\Psi} (\mathcal {X} ^ {c}) - \Pi_ {\Psi} ^ {g}} \\ & {\qquad = (\tilde {x} _ {k ^ {\circ}} - \lfloor \tilde {x} _ {k ^ {\circ}} \rfloor) \overline {{B}} _ {I ^ {\circ}} ^ {k ^ {\circ}},} \\ & {\qquad \leq \overline {{B}} _ {I ^ {\circ}} ^ {k ^ {\circ}}} \end{array}
$$

and the theorem follows immediately. w

Note that Problem (27) is equivalent to Problem (25). The theorem guarantees that the maximum loss from using the efficient greedy algorithm we propose, rather than an optimal but time-consuming algorithm, to solve the NP-hard Problem (25), is no more than the deprivation cost of missing a demand for one unit of certain types of resources. We formally present the proposed greedy algorithm in Algorithm 2. The computational time of Algorithm 2 is dominated by the sorting operation in line 2 of the algorithm, which is known to run efficiently in log-linear time.

Algorithm 2 (A Greedy Algorithm to Solve Problem (25)) Input: W, $\{ w _ { k } | k = 1 , 2 , \ldots , K \} , \{ \tilde { \mathcal { Q } } ^ { ( \psi ) } | \psi = 1 , 2 , \ldots , \Psi \}$ Output: $\mathcal { X } ^ { g } = ( x _ { 1 } ^ { g } , \dots , x _ { K } ^ { g } )$

1: Calculate slopes $\overline { { B } } _ { i } ^ { \kappa }$ via Equation (31), $i = 1 , 2 , \dots ,$ $M ^ { k } , k = 1 , 2 , \dot { \dots } , K$

2: Obtain slope sequence P by ranking all slopes in descending order according to the ratio $\overline { { B } } _ { i } ^ { k } / w _ { k }$

3: $\rho = 1$

4: while $\textstyle \sum _ { k = 1 } ^ { K } w _ { k } x _ { k } ( \rho ) < W$ do

5: $\rho = \rho + 1$

6: Calculate $x _ { k } ( \rho )$ via Equation (32), $k = 1 , 2 , \dots , K$

$$
\rho_ {W} = \rho
$$

8: if $\begin{array} { r } { \sum _ { k = 1 } ^ { K } w _ { k } x _ { k } ( \rho _ { W } ) = W } \end{array}$ then

9: $x _ { k } ^ { g } = x _ { k } ( \rho _ { _ W } ) , \dot { k } = 1 , 2 , \ldots , K$

10: else

11: $k ^ { \circ } = \kappa ( \rho _ { W } )$

12: Obtain the maximum fractional requested quantity for resource type $k ^ { \circ } , \tilde { x } _ { k ^ { \circ } }$ via Equation (34)

13: $x _ { k } ^ { g } = \left\{ \begin{array} { l l } { \big \lfloor \tilde { x } _ { k ^ { \circ } } \big \rfloor } & { \mathrm { i f ~ } k = k ^ { \circ } , } \\ { x _ { k } ( \rho _ { W } ) } & { \mathrm { i f ~ } k \neq k ^ { \circ } , } \end{array} \right. \ k = 1 , 2 , \ldots , K$

14: return $\mathcal { X } ^ { g } = ( x _ { 1 } ^ { g } , \dots , x _ { K } ^ { g } )$

## 5. Empirical Evaluation

## 5.1. Data and Evaluation Procedure

In July 2021, severe floods struck China’s Henan Province, causing 398 deaths and \$12.7 billion in property damages.<sup>6</sup> During the response phase of this disaster, Weibo, the largest social media platform in China, became an important tool for disaster-affected people to request disaster relief resources.<sup>7</sup> Figure 3 shows a Weibo post in response to the disaster, with demand time and requested resources highlighted. Therefore, we evaluate the performance of our method and benchmark methods with data collected from Weibo posts concerning emergency demands in response to the 2021 Henan floods.

We employed a public data set extracted from 3,496 Weibo posts concerning the 2021 Henan floods during the period from July 21, 2021 to July 27, 2021.<sup>8</sup> Among these Weibo posts, we manually identified 860 demands (posts) that requested disaster relief resources. In realworld practices, disaster relief resources serving a common objective are packaged as a kit to enable rapid response and fast delivery (Vanajakumari et al. 2016). For example, resources with a common objective of saving lives, such as food, shelter, and medication, can be grouped into a kit. Therefore, we categorized resources requested in the demands into three kits: on-site support (including resources such as flashlights and inflatable boats), lifesaving (including resources such as medication and food), and damage repair (including resources such as flood barriers and pumps) according to the Catalog of Emergency Resources issued by the National Devel opment and Reform Commission of China.<sup>9</sup> As a result, there are three types of resources in our evaluation, each of which corresponds to a kit. Among the 860 demands, type 1 resources (i.e., on-site support kits) are requested in 328 demands, type 2 resources (i.e., lifesaving kits) are requested in 666 demands, and type 3 resources $( \mathrm { i . e . , }$ damage repair kits) are requested in 194 demands. The Weibo data set does not include quantities of requested resources. To overcome this limitation, we set quantities to one unit for requested resources in the data set.

Figure 3. (Color online) An Emergency Demand Post on Weibo in Response to the 2021 Henan Floods  
![](/api/attachments/ZNCFMYUM/fulltext/images/978ced2e308b307327560f53210561743af1c1cb083e496cf68f0207ecb21fa7.jpg)

Figure 4. (Color online) Timeline of Resource Requests in the Evaluation  
![](/api/attachments/ZNCFMYUM/fulltext/images/c3e123b2519eb29827f31e715c47797637385a9cc1e4b3e3d0fc6c92dd159c70.jpg)

Next, we detail the evaluation procedure. As shown in Figure 4, we used the demands that occurred on July 21, 22, and 23 to train an investigated method. Resources were then requested at hour 00:00 of July 24 $( \mathrm { i } . \mathrm { e } . , T )$ , with their quantities decided by the trained method. We set the transportation time to 12 hours. Thus, requested resources arrived at hour 12:00 of July 24 $( \mathrm { i . e . , } T _ { + } )$ . Once arrived, these resources were distributed to meet demands, and another round of resource requests was started. Hence, we reset resource request time T to hour 12:00 of July 24, trained the method using the demands that occurred in the period from hour 00:00 of July 21 to hour 12:00 of July 24, and requested resources according to their quantities decided by the trained method. We repeated the mentioned process, and the last resource request time was hour 12:00 of July 27. There could be demands not satisfied until the end of July 27. These demands were fulfilled by transportation that started at the end of July 27 and arrived 12 hours later (i.e., hour 12:00 of July 28).

The performance of a method was evaluated using the average unit demand deprivation cost incurred by the method, where the average was taken over the demands that occurred in the period from July 24 to July 27. Consider a unit demand for type k resources (i.e., a demand for one unit of type k resources), k � 1, 2, 3. We can observe its demand time and derive its fulfillment time by running the method according to the evaluation procedure elaborated. Thus, we can calculate the delay δ of fulfilling this unit demand as the difference between its fulfillment time and demand time. By Equation (19), the deprivation cost of fulfilling this unit demand is

$$
e ^ {\phi + b c _ {k} \delta} - e ^ {\phi},
$$

where $c _ { k }$ is the importance score of type k resources. Let $N _ { k }$ denote the total units of type k resources requested in the demands that occurred in the period from July 24 to

July $2 7 , k = 1 , 2 , 3 .$ . The average unit demand deprivation cost is given by

$$
\frac {1}{N} \sum_ {k = 1} ^ {3} \sum_ {i _ {k} = 1} ^ {N _ {k}} (e ^ {\phi + b c _ {k} \delta_ {i _ {k}}} - e ^ {\phi}),\tag{36}
$$

where $\delta _ { i _ { k } }$ denotes the delay of meeting the $i _ { k } \mathrm { t h }$ unit demand for type k resources and $\begin{array} { r } { N = \sum _ { k = 1 } ^ { 3 } N _ { k } } \end{array}$ is the total units of requested resources. Holgu´ın-Veras et al. (2013) estimate the deprivation parameters $\phi = 1 . 5 0 3 1$ and $b =$ 0.1172 based on disaster-affected victims’ willingness to pay for a deprived resource and calculate deprivation costs in dollar amount with these parameter values. Subsequent disaster management studies have commonly used these parameter values for the calculation of deprivation costs (e.g., Rivera-Royero et al. 2016). Therefore, we set $\phi = 1$ :5031 and $b = 0 . { \dot { 1 } } 1 7 2$ in Equation (36) by fol lowing Holgu´ın-Veras et al. (2013).

## 5.2. Benchmark Methods

Our proposed method consists of two components: the CNM-TPP model described in Section 4.1 for future demand prediction and the PRR method proposed in Section 4.2 that takes future demands predicted by CNM-TPP as an input and decides optimal quantities of requested resources. Therefore, we named our method CNM-PRR. We benchmarked our method against the current practice of resource request, which reactively sets quantities of requested resources as quantities of currently unfulfilled demands (Huang et al. 2015). We called this benchmark the reactive resource request (ReR) method. The comparison between our method and ReR not only reveals the practical value of our method but also demonstrates the benefit of the proactive resource request, the main novelty of our study.

In addition, as reviewed in Section 2.3, TPP is the dominant technique for predicting future events. Hence, we can adapt existing TPP models to predict future demands. In particular, we chose logNormMix, a state-ofthe-art TPP model proposed by Shchur et al. (2020), which has shown superior performance over other existing TPP models in various event prediction tasks. We also included three recently proposed TPP models as benchmarks: Attentive Neural Datalog Through Time (A-NDTT), Attention Monte Carlo (Attn-MC), Continuous Time Deep Renewal Process (CTDRP). Specifically, A-NDTT by Mei et al. (2022) is a state-of-the-art TPP model based on the transformer architecture, AttnMC is a deep learning-based TPP model proposed by Enguehard et al. (2020), and CTDRP by Turkmen et al. (2019) is a novel deep learning-based TPP model designed for supply chain demand forecasting. To adapt these TPP methods for future demand prediction, we replaced their mark-embedding functions with ours defined in Equation (4) because their mark-embedding function cannot capture both types and quantities of requested resources in a demand. To solve the disaster response problem, a demand forecasting method needs to be combined with a resource request method, which employs future demands predicted by the method to decide quantities of requested resources. To this end, we combine each of them with our PRR method and name the resulting methods as logNormMix-PRR (logNorm-Mix+PRR), A-NDTT-PRR (A-NDTT+PRR), AttnMC-PRR (AttnMC+PRR), and CTDRP-PRR (CTDRP+PRR).

Moreover, we benchmarked our method against stateof-the-art data-driven inventory control (IC) models because our method is a data-driven method, and datadriven IC models represent recent developments in the IC literature. Among IC problems, the newsvendor problem, which determines the optimal stock level based on future demand quantities, is most similar to the PRR problem. We thus applied state-of-the-art data-driven methods for the newsvendor problem, the linear regression-based data-driven method for the newsvendor problem (LR-NV) (Ban and Rudin 2019) and the deep learning-based data-driven method for the newsvendor problem (DL-NV) (Oroojlooyjadid et al. 2020), to solve the PRR problem and compared the performance of our method against these methods.

Also, we integrated logNormMix with a simple importance-adjusted first come, first serve (IFCFS) resource request method. Specifically, the IFCFS method first prioritized and grouped resources in the demands by their importance scores; within each importance group, resources were requested in a first come, first serve manner according to their demand times until the transportation capacity was reached. We named this benchmark the logNormMix-IFCFS method. Table 3 summarizes the methods compared in the evaluation.

Next, we discuss the implementation details of these methods. We implemented our CNM-TPP model with PyTorch, and then, we trained it with the Adam optimizor using learning rate 0.001 for 30 epochs. To tune the hyperparameters of CNM-TPP and other benchmarks, we reserved a portion of the training demands that occurred on July 21, 22, 23 as a validation data set. The hyperparameters of CNM-TPP include $n _ { e }$ (the embedding size of RNN in Equation (2)), $n _ { z }$ (the number of log normal mixture components in Equation (6)), and γ (the multiplicator in Equation (17)). We set $n _ { e } = n _ { z } = 6 4$ and γ � 1. A detailed walk-through of the computation flow of CNM-TPP under this parameter setting can be found in Online Appendix B. LogNormMix features two key hyperparameters: the embedding size of historical events and the number of lognormal mixture components. We set both as 64. Both A-NDTT and AttnMC are constructed with transformer blocks, which can be specified by two hyperparameters: embedding size and the number of layers. For both models, we set the former as 64 and the latter as 1. CTDRP has one hyperparameter, namely the size of the hidden state of an RNN layer, which is set as 64. We note that our parameter setting is comparable with those reported in Enguehard et al. (2020) and Mei et al. (2022). We defined the unit backordering cost in LR-NV and DL-NV as the cost incurred because of the lack of one unit of resources. In addition, to extend them to multiple types of resources, we added a constraint that the total capacity consumed by shipping the requested units of all resource types must not exceed the transportation capacity. DL-NV employed a multilayer perceptron with three hidden layers of sizes 128, 64, and 16.

Table 3. Summary of the Methods Compared in the Evaluation

<table><tr><td>Method</td><td>Notes</td></tr><tr><td>CNM-PRR</td><td>Our proposed method</td></tr><tr><td>ReR</td><td>Reactive resource request method</td></tr><tr><td>logNormMix-PRR</td><td>The combination of logNormMix, a state-of-the-art TPP model by Shchur et al. (2020), and our PRR method</td></tr><tr><td>A-NDTT-PRR</td><td>The combination of A-NDTT (Mei et al. 2022), a recent TPP model based on the transformer architecture, and our PRR method</td></tr><tr><td>AttnMC-PRR</td><td>The combination of AttnMC, a deep learning-based TPP model by Enguehard et al. (2020), and our PRR method</td></tr><tr><td>CTDRP-PRR</td><td>The combination of CTDRP, a novel deep learning-based TPP model by Turkmen et al. (2019) for supply chain demand forecasting, and our PRR method</td></tr><tr><td>LR-NV</td><td>A data-driven newsvendor method by Ban and Rudin (2019) predicting future demand quantities using linear regression</td></tr><tr><td>DL-NV</td><td>A data-driven newsvendor method by Oroojlooyjadid et al. (2020) predicting future demand quantities using a deep learning method</td></tr><tr><td>logNormMix-IFCFS</td><td>The combination of logNormMix and the IFCFS resource request method</td></tr></table>

## 5.3. Evaluation Results and Analysis

Following the evaluation procedure, we conducted experiments to evaluate the performance of each compared method. Recall that there are three types of resources in the evaluation: type 1 resources (i.e., on-site support kits), type 2 resources (i.e., lifesaving kits), and type 3 resources (i.e., damage repair kits). Because each type is a bundle of various-sized resources, we assume that the three types of resources consume the same transportation capacity. Accordingly, we set the transportation capacity of shipping one unit of any type of resources to one $( \mathrm { i . e . , } w _ { 1 } = w _ { 2 } = w _ { 3 } = 1 )$ . In general, it is more urgent and important to satisfy demands for lifesaving resources than the other two types. Therefore, the importance score of type 2 resources is higher than that of the other two types. We thus set the importance scores of types 1, 2, and 3 resources to two, four, and two, respectively $( { \mathrm { i . e . , } } c _ { 1 } = 2 , c _ { 2 } = 4 , { \mathrm { a n d } } c _ { 3 } = 2 )$ . We set the transportation capacity W to 200 and then, varied its value to examine the performance of the investigated methods under different transportation capacities.

Table 4 reports the average unit demand deprivation cost of each method. Recall that deprivation cost measures the economic value of human suffering because of the deprivation of vital resources (Holgu´ın-Veras et al. 2013). If a local agency employs our method to decide types and quantities of requested resources, the average economic value of human suffering because of the delay of one unit of resources is \$25.69, which is substantially lower than that of the ReR method. The enormous cost reduction by our method over ReR demonstrates the benefit of proactive resource request and reveals the practical value of our method in alleviating human suffering caused by a disaster.<sup>10</sup> Moreover, in comparison with A-NDTT-PRR, the best-performing benchmark, our method reduces costs by 15.15%. Because the only difference between A-NDTT-PRR and our method is their respective TPP models, the cost reduction is attributed to the superior performance of our proposed TPP model over A-NDTT, a state-of-the-art existing TPP model, in predicting future demands. Our method also outperforms logNormMix-IFCFS by 88.63% in cost reduction, which is because of the superiority of our TPP model over logNormMix and the performance advantage of our PRR method over the IFCFS method.

Table 4. Performance Comparison on Average Unit Demand Deprivation Cost $( W = 2 0 0 , w _ { 1 } = 1 , w _ { 2 } = 1 , w _ { 3 } = 1 ,$ $c _ { 1 } = 2 , c _ { 2 } = 4 , c _ { 3 } = 2 )$

<table><tr><td>Method</td><td>Average unit demand deprivation cost, $</td><td>Cost reduction by CNM-PRR, %</td></tr><tr><td>CNM-PRR (our method)</td><td>25.69</td><td></td></tr><tr><td>ReR</td><td>21,905.50</td><td>99.88</td></tr><tr><td>logNormMix-PRR</td><td>32.32</td><td>20.51</td></tr><tr><td>A-NDTT-PRR</td><td>30.28</td><td>15.15</td></tr><tr><td>AttnMC-PRR</td><td>31.26</td><td>17.82</td></tr><tr><td>CTDRP-PRR</td><td>37.35</td><td>31.22</td></tr><tr><td>LR-NV</td><td>70.14</td><td>63.37</td></tr><tr><td>DL-NV</td><td>58.76</td><td>56.28</td></tr><tr><td>logNormMix-IFCFS</td><td>225.95</td><td>88.63</td></tr></table>

To dig deeper into the superior performance of our method, let us examine two kinds of demands that could be considered at resource request time T. As shown in Figure 5, currently unfulfilled demands occurred before T, and future demands will arrive between T and T (i.e., resource arrival time). Because of the 12-hour transportation time, the time delay of satisfying a currently unful filled demand is inevitably greater than 12 hours. On the other hand, if a future demand is proactively requested at T, the time delay of meeting this demand is less than 12 hours. Benchmark method ReR neglects future demands and requests resources based on currently unfulfilled demands only. Consequently, the time delay of satisfying a demand by this method is long, which in turn, leads to high deprivation cost. On the other hand, an effective method that can accurately predict future demands and proactively request resources to meet these predicted demands can significantly reduce the time delay of satisfying a demand to less than 12 hours, thereby incurring much lower deprivation cost. Table 5 reports the average time delay of satisfying one unit of resource demand by each method. As reported, the average time delay of our method is 7.42 hours, which is substantially shorter than 12 hours and outperforms that of each benchmark method by a range of between 9.74% and 62.11%. The reactive ReR method, on the other hand, incurs the longest time delay, which is substan tially longer than 12 hours.

We further investigate the average percentage of future demands occurring between time T and T (see Figure 5) that are proactively requested and fulfilled. Table 6 lists the average percentage for each method. As expected, the average percentage for the ReR method is zero because it neglects future demands. Our method attains the highest average percentage, outperforming that of A-NDTT-PRR (the best-performing benchmark) by 8.55%.

Figure 5. (Color online) Demands that Could Be Considered at Resource Request Time T  
![](/api/attachments/ZNCFMYUM/fulltext/images/7a5cfd506fda1f0c0fbde06b880e9c30e6835ab2129114bbba7fef5508e7ff56.jpg)

Table 5. Performance Comparison on Average Unit Demand Time Delay (W � 200, w<sub>1</sub> � 1, w<sub>2</sub> � 1, w<sub>3</sub> � 1, $c _ { 1 } = 2 , c _ { 2 } = 4 , c _ { 3 } = 2 )$

<table><tr><td>Method</td><td>Average unit demand time delay, hours</td><td>Time delay reduction by CNM-PRR, %</td></tr><tr><td>CNM-PRR (our method)</td><td>7.42</td><td></td></tr><tr><td>ReR</td><td>19.58</td><td>62.11</td></tr><tr><td>logNormMix-PRR</td><td>8.41</td><td>11.79</td></tr><tr><td>A-NDTT-PRR</td><td>8.22</td><td>9.74</td></tr><tr><td>AttnMC-PRR</td><td>8.37</td><td>11.32</td></tr><tr><td>CTDRP-PRR</td><td>8.81</td><td>15.83</td></tr><tr><td>LR-NV</td><td>10.02</td><td>26.00</td></tr><tr><td>DL-NV</td><td>9.56</td><td>22.36</td></tr><tr><td>logNormMix- IFCFS</td><td>13.87</td><td>46.51</td></tr></table>

The evaluation demonstrates the superior performance of our proposed CNM-PRR method over each benchmark. All the performance improvements by our method reported in Tables 4–6 are statistically significant $( p < 0 . 0 1 )$ . The superiority of our method is attributed to its CNM-TPP model that can accurately predict future demands and its PRR method that can proactively decide optimal quantities of requested resources. As a result, our method achieves the best performance in future demand fulfillment (as reported in Table 6) and unit demand time delay (as reported in Table 5) among all the compared methods, thereby attaining the lowest deprivation cost.

We conducted an ablation analysis to demonstrate the contribution of each novelty of our CNM-TPP to the performance of our method. Specifically, CNM-TPP features three methodological novelties: a new mark-embedding function, a novel CSD learning objective, and the modeling of the correlations among different types of resources requested in a demand. Because the proposed markembedding function is indispensable to solve the PRR problem, our ablation analysis focuses on the contributions of the other two novelties. To inspect the contribution of the correlation modeling, we simplified the event generation layer by assuming conditional independence (CI) among different types of resources requested in a demand. We called the simplified TPP with the CI assumption CI-TPP and its integration with the PRR method CI-PRR. To evaluate the contribution of the CSD learning objective, we further dropped it from CI-TPP, and the resulted TPP was only trained with the NLL objective, like many existing TPPs (Shchur et al. 2021). We named the resulting TPP with the abbreviation NLL-CI-TPP and its integration with the PRR method NLL-CI-PRR. Table 7 compares the performance between our method, CI-PRR, and NLL-CI-PRR.

Table 6. Performance Comparison on the Average Percentage of Fulfilled Future Demands (W � 200, $w _ { 1 } = 1 , w _ { 2 } = 1 , w _ { 3 } = 1 , c _ { 1 } = 2 , c _ { 2 } = 4 , c _ { 3 } = 2 )$

<table><tr><td>Method</td><td>Average percentage of fulfilled future demands</td><td>Improvement by CNM-PRR, %</td></tr><tr><td>CNM-PRR (our method)</td><td>0.80</td><td></td></tr><tr><td>ReR</td><td>0.00</td><td>—</td></tr><tr><td>logNormMix-PRR</td><td>0.72</td><td>11.10</td></tr><tr><td>A-NDTT-PRR</td><td>0.74</td><td>8.55</td></tr><tr><td>AttnMC-PRR</td><td>0.73</td><td>10.06</td></tr><tr><td>CTDRP-PRR</td><td>0.68</td><td>17.00</td></tr><tr><td>LR-NV</td><td>0.58</td><td>37.27</td></tr><tr><td>DL-NV</td><td>0.62</td><td>28.64</td></tr><tr><td>logNormMix- IFCFS</td><td>0.42</td><td>90.46</td></tr></table>

Because CI-PRR is derived by ignoring the correlations among different types of resources requested in a demand, the superiority of CNM-PRR over CI-PRR reveals the contribution of the correlation modeling to the performance of our method. Similarly, the outperformance of CI-PRR over NLL-CI-PRR uncovers the contribution of the CSD learning objective. As reported in Table $^ { 7 , }$ both novelties contribute significantly to the performance of our method. Specifically, by modeling the correlations among different types of resources requested in a demand, CNM-PRR outperforms CI-PRR by 9.35%; by introducing the CSD learning objective, CI-PRR surpasses NLL-CI-PRR by 12.31%.

We further demonstrated the superior performance of our method in different contexts. Specifically, in Online Appendix E, we evaluated the robustness of our method’s superiority over the benchmarks by varying transportation capacity W and importance scores $c _ { k } .$ In Online Appendix F, we extended our method to the scenario where resource arrival time is stochastic and where overrequested resources incur holding costs. In Online Appendix $G ,$ we employed simulation to demonstrate the generalizability of our method.

## 5.4. Evaluation Under a Multistakeholder and Multiobjective Setting

We conducted simulations to evaluate our method and benchmark methods under a multistakeholder and mul tiobjective setting as depicted in Figure 1. As shown in the figure, all stakeholders share the common objective of minimizing the cost of delays in demand satisfactions, which can be operationalized using the average unit demand deprivation cost $( \mathrm { i . e . , }$ , Equation (36)). Moreover, each type of stakeholder could have its own specific objective (Abbasi et al. 2019, 2021). In particul $^ { \mathrm { { r , } } }$ a local agency also pays close attention to its fill rate. Let $R _ { l } ^ { f }$ denote the fill rate of local agency $l = 1 , \ldots , L ,$ , where L represents the total number of local agencies. Fill rate $R _ { l } ^ { f }$ can be measured as the percentage of resources requested by disaster-affected people being met in the area served by local agency l (Noyan et al. 2016). The central agency is concerned about the fairness in allocating resources to local agencies and aims to ensure that the allocation decision would not systematically disadvantage any local agency (Bertsimas et al. 2012, Huang et al. 2015). A common measure for the fairness of allocation is the equality of fill rates (Huang et al. 2015), which can be operationalized by the standard deviation of fill rates among local agencies:

Table 7. Ablation Analysis (W � 200, w<sub>1</sub> � 1, w<sub>2</sub> � 1, w<sub>3</sub> � 1, c<sub>1</sub> � 2, c<sub>2</sub> � 4, c<sub>3</sub> � 2)

<table><tr><td>Method</td><td>Average unit demand deprivation cost, $</td><td>Cost reduction by CNM-PRR, %</td><td>Cost reduction by CI-PRR, %</td></tr><tr><td>CNM-PRR (our method)</td><td>25.69</td><td></td><td></td></tr><tr><td>CI-PRR</td><td>28.34</td><td>9.35</td><td></td></tr><tr><td>NLL-CI-PRR</td><td>32.32</td><td>20.51</td><td>12.31</td></tr></table>

$$
\left(\frac {1}{L} \sum_ {l = 1} ^ {L} (R _ {l} ^ {f} - \overline {{R}} ^ {f}) ^ {2}\right) ^ {\frac {1}{2}},\tag{37}
$$

where $\textstyle \overline { { R } } ^ { f } = \sum _ { l = 1 } ^ { L } R _ { l } ^ { f } / L$ represents the average fill rate across all L local agencies. Clearly, high standard deviation of fill rates indicates high divergence of fill rates among local agencies and hence, low fairness of allocation.

In a simulation, we run the following procedure for our method and each benchmark method.

1. Execute a method at each local agency to decide the quantity of resources requested from the local agency for each resource type.

2. The central agency, after receiving resource requests from all local agencies, adopts the following commonly used proportional (ration) allocation policy (Chen et al. 2012). For any resource type, if the stockpile at the central agency is sufficient to meet all requests, allocate according to the requests; otherwise, allocate all available stockpiles to local agencies by the amounts proportional to their requests.

3. Evaluate the performance of the method in terms of how well each of the three objectives discussed is satisfied.

We considered three local agencies in our simulation. Using the simulation mechanism described in Online Appendix $G ,$ we simulated demands for three types of resources at each local agency. Different local areas might be affected by a disaster differently. As a result, the intensity of demand arrivals at different local agencies could be different. To simulate this situation, we set parameters $\nu$ (background trend in the self-correcting process) and $\lambda _ { 0 }$ (base occurrence rate in the Hawkes process) to be two for one local agency; we set these parameters to be 1 and 0.5 for the other two agencies. We performed 200 simulation runs. Let $\mathcal { T } _ { k }$ denote the stockpile level of resource type k at the central agency, $k = 1 , 2 ,$

3. We set $\mathcal { T } _ { k }$ as the median of the actual demands for resource type k across 200 simulation runs, which corresponds to $\bar { ( \mathcal { T } } _ { 1 } , \mathcal { T } _ { 2 } , \mathcal { T } _ { 3 } ) = ( 1 9 8 , 2 2 0 , 1 9 8 )$ . In this way, our simulation covers a wide range of degrees of inventory capacity tightness relative to the actual demand. More specifically, the actual demand for type k resources exceeds the inventory capacity 50% of the time and is below the inventory capacity 50% of the time in the simulation. Among 200 simulation runs, the level of undercapacity is as high as 80%.

Table 8 summarizes the performance of each compared method averaged across 200 simulation runs. As reported, our method significantly outperforms each benchmark in satisfying every objective $\hat { ( p } < 0 . 0 1 ) . ^ { 1 1 }$ The superior performance of our method is attributed to its CNM-TPP component that predicts future demands more accurately and its PRR component that effectively decides types and quantities of requested resources based on both currently unfulfilled demands and predicted future demands. Consequently, resource requests generated by our method not only lead to low deprivation cost but also, reflect true demands from local agencies more accurately, which in turn, increases fill rate and improves resource allocation fairness.

## 6. Discussion and Conclusion 6.1. Contributions

Disaster response is critical to save lives and reduce damages in the aftermath of a disaster. Fundamental to disaster response operations is the management of disaster relief resources. Prior resource management research overlooks the problem of deciding optimal quantities of resources requested by a local agency. In response to this research gap, we formulate a new resource management problem (i.e., the proactive resource request problem). To solve the problem, we develop a novel TPP model to predict future demands and propose an effective solution method to the problem. We demonstrate the superior performance of our method over prevalent existing methods using both real-world and simulated data.

Our study belongs to the computational genre of design science research in information systems, which develops computational methods to solve business and societal problems and aims at making methodological contributions (Rai 2017, Gupta 2018). Accordingly, one contribution of our study is the formulation of a new and important resource management problem for disaster response, which proactively decides optimal quantities of requested resources based on both currently unfulfilled demands and future demands. By solving the problem, our study adds to the extant literature with the following methodological contributions. First, we propose a novel TPP model to accommodate salient characteristics of the problem. Specifically, our proposed TPP model differs from existing TPP models in its learning objective, mark-embedding function, and event generation layer. Second, we formulate the problem as a stochastic optimization model and analyze its properties in Theorems 1 and 2. We then develop an efficient solution method to the problem based on the analyzed properties and show its effectiveness in Theorem 3.

Table 8. Performance Comparison on Objectives of Different Stakeholders $( \mathcal { T } _ { 1 } = 1 9 8 , \mathcal { T } _ { 2 } = 2 2 0 , \mathcal { T } _ { 3 } = 1 9 \bar { 8 } )$

<table><tr><td>Method</td><td>Average unit demand deprivation cost, $</td><td>Average fill rate</td><td>Average standard deviation of fill rates</td></tr><tr><td>CNM-PRR (our method)</td><td>28.01</td><td>0.927</td><td>0.063</td></tr><tr><td>logNormMix-PRR</td><td>33.54(16.49%)</td><td>0.898(3.21%)</td><td>0.085(25.53%)</td></tr><tr><td>A-NDTT-PRR</td><td>32.06(12.64%)</td><td>0.903(2.56%)</td><td>0.080(21.24%)</td></tr><tr><td>AttnMC-PRR</td><td>31.22(10.29%)</td><td>0.910(1.77%)</td><td>0.093(31.79%)</td></tr><tr><td>CTDRP-PRR</td><td>35.30(20.66%)</td><td>0.906(2.26%)</td><td>0.106(40.22%)</td></tr><tr><td>LR-NV</td><td>52.98(47.13%)</td><td>0.829(11.78%)</td><td>0.098(35.68%)</td></tr><tr><td>DL-NV</td><td>48.29(42.00%)</td><td>0.888(4.29%)</td><td>0.095(33.89%)</td></tr><tr><td>logNormMix-IFCFS</td><td>288.11(90.28%)</td><td>0.519(78.51%)</td><td>0.125(49.58%)</td></tr></table>

Note. The percentage improvement by our method over a benchmark is listed in parentheses.

## 6.2. Implications for Disaster Response Management Practices

Our study offers several design principles that guide the development of a humanitarian resource management system for disaster response. As demonstrated in our study, a predictive analytics method characterizes uncertainties and predicts future demands. Taking the predicted future demands as inputs, a prescriptive analytics method then searches through the policy space and discovers a resource request policy that optimizes the objective of disaster response. In addition, we show that, in comparison with benchmark methods, our method that integrates predictive and prescriptive analytics can attain higher fairness in allocating resources among local agencies. Without a prescriptive analytics method, a predictive analytics method alone cannot produce effective resource request decisions for disaster response. On the other hand, a prescriptive analytics method by itself cannot generate a practical resource request policy as it lacks the understanding of real-world uncertainties. Accordingly, we have design principle 1.

Design principle 1. A predictive analytics method should go hand in hand with a prescriptive analytics method in order to timely, effectively, and fairly satisfy demands for disaster relief resources in a highly volatile and uncertain environment, in which the distribu tion of demands is nonstationary.

We demonstrate substantial benefits of proactive resource request in alleviating the suffering of disasteraffected people. For example, we show that the average unit demand deprivation cost incurred by our method is significantly lower than that incurred by the reactive resource request method. As a result, we have design principle 2.

Design principle 2. Practitioners need to reconsider the current practice of reactive resource request and adopt the way of proactive resource request in designing a humanitarian resource management system, which takes both currently unfulfilled demands and future demands into consideration.

Information technology (IT), especially machine learning, enables local disaster relief agencies to predict future demands by analyzing patterns of past demands. We show that a carefully designed TPP model can effectively characterize the dynamics of nonstationary demands arising from a disaster and predict future demands. Such prediction empowers local agencies to act with foresight and avoid myopic decisions, thereby saving more lives and properties. Therefore, our study demonstrates the value of IT in general and machine learning in particular for effective disaster response. Consequently, we have design principle 3.

Design principle 3. A critical precursor to proactive resource request is the prediction of future demands.

Therefore, a humanitarian resource management system should make effective use of proper predictive analytics technologies for future demand prediction.

Finally, our study shows that it is viable to collect and analyze demand data from social media platforms to decide quantities of requested disaster relief resources. It thus demonstrates the value of social media data for effective disaster response. Considering that social media platforms have become a major means for requesting disaster relief resources, a humanitarian resource management system should have the capability of listening to the demands of disaster-affected people through social media (Abbasi et al. 2019) and allocating resources based on the demands. Therefore, we suggest design principle 4.

Design principle 4. A humanitarian resource management system should be capable of collecting demand data from social media platforms in real time, discovering demand patterns from huge amounts of collected data, and making intelligent resource request decisions based on the discovered patterns.

Social media data, however, are voluntarily contributed, and as such, the voluntary nature of social media data undermines their quality, which in turn, creates challenges for designing humanitarian resource management systems. For example, missing values in social media data could impact the accuracy of future demand prediction and the effectiveness of resource request decisions. Moreover, information sharing among central and local agencies is critical for effective disaster response, and thus, information interoperability among systems located at central and local agencies is another design challenge. To address these challenges, IS research on data quality and management could provide effective solutions (Xu et al. 2023).

## 6.3. Limitations and Future Research

Our study has limitations and can be extended in several directions. First, our CNM-TPP model is trained with a sequence of observed demands to predict future demands. Thus, like many other machine learning algorithms, CNM-TPP also has the cold-start problem (i.e., how to predict future demands when there are few or even no observed demands). To address this limitation, future work could develop a transfer learning solution, which learns a model using observed demands in other similar disasters and adapts the model to predict future demands for the focal disaster. Second, although some disaster relief resources are not reusable (e.g., food), some others are reusable (e.g., pumps). Different from nonreusable resources, a reusable resource could satisfy multiple demands. Therefore, another area worthy of future research is to extend our method to decide optimal quantities of requested resources by considering the differences between reusable and nonreusable resources. Third, our proposed method is a single-period method, which is executed in a rolling horizon manner to solve the resource request problem. Future study could extend our work to make resource request decisions for longer time periods. Given the sequential nature of the problem, a viable solution method could be one based on reinforcement learning (Sutton and Barto 2018). Finally, this study solves one resource management problem for disaster response (i.e., the resource request problem). Future work could integrate our deep learning-based proactive resource req uest method with solution methods to other important resource management problems (e.g., resources allocation and transportation problems) such that we can have a more holistic resource management method for effective disaster response.

## Acknowledgments

The authors thank the special section editors, the associate editor, and three anonymous reviewers for their guidance and constructive comments that have tremendously improved the paper. Hongzhe Zhang and Xiaohang Zhao contributed equally to the paper and are cofirst authors.

## Endnotes

<sup>1</sup> See https://slate.com/technology/2011/05/tornado-in-missouriwhy-disasters-are-becoming-more-frequent-and-what-we-can-do-about it.html (last accessed on March 23, 2023).

<sup>2</sup> See https://reliefweb.int/report/world/cred-crunch-newsletterissue-no-62-may-2021-disaster-year-review-2020-global-trends-and (last accessed on March 23, 2023).

<sup>3</sup> See https://www.fema.gov/sites/default/files/2020-05/CPG\_101\_ V2\_30NOV2010\_FINAL\_508.pdf (last accessed on March 23, 2023).

<sup>4</sup> There are two implementation considerations for the probability mass function specified in Equations (8)–(10). First, it assigns a nonzero probability to an event mark requesting no resources $( \mathrm { i . e . , } a _ { k } ^ { ( i ) }$ � 0 for $k = 1 , 2 , \ldots , K )$ . To remedy this issue, we can set $p _ { m } ( m _ { i } | \mathcal { H } _ { i - 1 } )$ � 0 for the case of $a _ { k } ^ { ( i ) } = 0 \mathrm { ~ f o r ~ } k \stackrel {  } { = } 1 , 2 , \dotsc , K$ . We then normalize the probabilities for all other cases such that these probabilities sum up to one. Second, we can simplify the function for the situation where a only takes one of the two values 0 or 1, which is discussed in Online Appendix A.2.

<sup>5</sup> Because our objective is to predict future events (demands) in the period of (T, T<sub>+</sub>], we empirically estimate the distribution of sequence lengths that are likely to be observed within a time interval of length T � T. Specifically, we count the number of events within a time interval of length T � T in the training sequence S and empirically compute the probability for each distinct count.

<sup>6</sup> See https://en.wikipedia.org/wiki/2021\_Henan\_floods (last accessed on March 23, 2023).

<sup>7</sup> See https://www.whatsonweibo.com/how-social-media-is-speedingup-zhengzhou-flooding-rescue-efforts/ (last accessed on March 23, 2023).

<sup>8</sup> The data set can be accessed at https://github.com/GiveHenanAHand/ henan-rescue-viz-website

<sup>9</sup> The Catalog of Emergency Resources broadly categorizes disaster relief resources into three groups: on-site support, lifesaving, and damage repair, with a list of resources in each group. This catalog can be accessed at https://www.ndrc.gov.cn/fzggw/jgsj/yxj/sjdt 201504/W020190906509018532631.pdf.

<sup>10</sup> The other benchmarks are also proactive resource request methods, and the significant cost reductions by these methods over ReR further confirm the benefit of proactive resource request.

<sup>11</sup> The percentage improvements by our method over benchmarks logNormMix-PRR, A-NDTT-PRR, AttnMC-PRR, and CTDRP-PRR on the fill rate are not as large as the other improvements reported in the table. This is partly because of the fact that these benchmarks employ our PRR method, which effectively decides types and quantities of resources requested from the central agency to satisfy local demands

## References

Abbasi A, Albrecht C, Vance A, Hansen J (2012) Metafraud: A meta-learning framework for detecting financial fraud. MIS Quart. 36(4):1293–1327.

Abbasi A, Dillon-Merrill R, Rao HR, Sheng O, Chen R (2021) Call for papers–Special issue of Information Systems Research— Unleashing the power of information technology for strategic management of disasters. Inform. Systems Res. 32(4):1490–1493.

Abbasi A, Li J, Adjeroh D, Abate M, Zheng W (2019) Don’t mention it? Analyzing user-generated content signals for early adverse event warnings. Inform. Systems Res. 30(3):1007–1028.

Ahmadi M, Seifi A, Tootooni B (2015) A humanitarian logistics model for disaster relief operation considering network failure and standard relief time: A case study on San Francisco district. Transportation Res. Part E Logist. Transportation Rev. 75:145–163.

Altay N, Green WG III (2006) OR/MS research in disaster opera tions management. Eur. J. Oper. Res. 175(1):475–493.

Arts J, Basten R, Van Houtum GJ (2016) Repairable stocking and expediting in a fluctuating demand environment: Optimal pol icy and heuristics. Oper. Res. 64(6):1285–1301.

Arunraj NS, Ahrens D (2015) A hybrid seasonal autoregressive integrated moving average and quantile regression for daily food sales forecasting. Internat. J. Production Econom. 170:321–335.

Ban GY, Rudin C (2019) The big data newsvendor: Practical insights from machine learning. Oper. Res. 67(1):90–108.

Bertsimas D, Farias VF, Trichakis N (2012) On the efficiency-fairness trade-off. Management Sci. 58(12):2234–2250.

Bishop CM (2006) Pattern Recognition and Machine Learning (Springer, Berlin).

Chen B, Wang Y, Zhou Y (2023) Optimal policies for dynamic pricing and inventory control with nonparametric censored demands. Working Paper, University of Illinois at Chicago, Chicago, IL, USA.

Chen B, Simchi-Levi D, Wang Y, Zhou Y (2022) Dynamic pricing and inventory control with fixed ordering cost and incomplete demand information. Management Sci. 68(8):5684–5703.

Chen L (2010) Bounds and heuristics for optimal Bayesian inventory control with unobserved lost sales. Oper. Res. 58(2):396–413.

Chen Y, Su X, Zhao X (2012) Modeling bounded rationality in capacity allocation games with the quantal response equilib rium. Management Sci. 58(10):1952–1962.

Deshpande P, Marathe K, De A, Sarawagi S (2021) Long horizon forecasting with temporal point processes. Lewin-Eytan L, Carmel D, Yom-Tov E, Agichtein E, Gabrilovich E, eds. WSDM ‘21 Fourteenth ACM Internat. Conf. Web Search Data Mining (Associa tion for Computing Machinery, New York), 571–579.

Du N, Dai H, Trivedi R, Upadhyay U, Gomez-Rodriguez M, Song L (2016) Recurrent marked temporal point processes: Embedding event history to vector. Krishnapuram B, Shah M, Smola AJ, Aggarwal C, Shen D, Rastogi R, eds. Proc. 22nd ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (Association for Computing Machinery, New York), 1555–1564.

Enguehard J, Busbridge D, Bozson A, Woodcock C, Hammerla N (2020) Neural temporal point processes for modelling electronic health records. Alsentzer E, McDermott MB, Falck F, Sarkar SK, Roy S, Hyland SL, eds. Proc. Machine Learn. Health NeurIPS Workshop vol. 119 (PMLR, New York), 85–113

Fang X, Gao Y, Hu PJ (2021) A prescriptive analytics method for cost reduction in clinical decision making. MIS Quart. 45(1):83–115.

Fang X, Hu PJH, Li Z, Tsai W (2013) Predicting adoption probabili ties in social networks. Inform. Systems Res. 24(1):128–145.

Fiedrich F, Gehbauer F, Rickers U (2000) Optimized resource allocation for emergency response after earthquake disasters. Safety Sci. 35(1–3):41–57.

Fricker RD Jr, Goodhart CA (2000) Applying a bootstrap approach for setting reorder points in military supply systems. Naval Res. Logist. 47(6):459–478.

Gilbert K (2005) An ARIMA supply chain model. Management Sci. 51(2):305–310.

Gossler T, Wakolbinger T, Nagurney A, Daniele P (2019) How to increase the impact of disaster relief: A study of transportation rates, framework agreements and product distribution. Eur. J. Oper. Res. 274(1):126–141.

Guijarro E, Cardo´s M, Babiloni E (2012) On the exact calculation of the fill rate in a periodic review inventory policy under discrete demand patterns. Eur. J. Oper. Res. 218(2):442–447.

Gupta A (2018) Traits of successful research contributions for publi cation in ISR: Some thoughts for authors and reviewers. Inform. Systems Res. 29(4):779–786.

Gupta S, Starr MK, Farahani RZ, Matinrad N (2016) Disaster management from a POM perspective: Mapping a new domain Production. Oper. Management 25(10):1611–1637.

Gupta V, Bedathur S, De A (2022a) Learning temporal point processes for efficient retrieval of continuous time event sequences. Proc. AAAI Conf. Artificial Intelligence, vol. 36 (AAAI Press, Palo Alto, CA), 4005–4013.

Gupta V, Bedathur S, Bhattacharya S, De A (2022b) Modeling continuous time sequences with intermittent observations using marked temporal point processes. ACM Trans. Intelligent Systems Tech. 13(6):103.

Holgu´ın-Veras J, Pe´rez N, Jaller M, Van Wassenhove LN, Aros-Vera F (2013) On the appropriate objective function for post-disaster humanitarian logistics models. J. Oper. Management 31(5): 262–280.

Hu J, Zhang C, Zhu C (2016) (s, s) inventory systems with correlated demands. INFORMS J. Comput. 28(4):603–611.

Huang K, Jiang Y, Yuan Y, Zhao L (2015) Modeling multiple humanitarian objectives in emergency response to large-scale disasters. Transportation Res. Part E Logist. Transportation Rev. 75:1–17.

Kim S, Pasupathy R, Henderson SG (2015) A guide to sample average approximation. Fu M, ed. Handbook of Simulation Optimization, International Series in Operations Research & Management Science, vol. 216 (Springer, New York), 207–243.

Lin YK, Fang X (2021) First, do no harm: Predictive analytics to reduce in-hospital adverse events. J. Management Inform. Systems 38(4):1122–1149.

Mei H, Eisner J (2017) The neural Hawkes process: A neurally selfmodulating multivariate point process. Guyon I, Luxburg U, Bengio S, Wallach HM, Fergus R, Vishwanathan SV, Garnett R, eds. Proc. 31st Internat. Conf. Neural Inform. Processing Systems (Neural Information Processing Systems Foundation, Inc., La Jolla, CA), 6757–6767.

Mei H, Yang C, Eisner J (2022) Transformer embeddings of irregularly spaced events and their participants. Internat. Conf. Learn. Representation (OpenReview.net).

Mieghem JAV, Rudi N (2002) Newsvendor networks: Inventory management and capacity investment with discretionary activities. Manufacturing Service Oper. Management 4(4):313–335.

Nasr WW, Elshar IJ (2018) Continuous inventory control with stochastic and non-stationary Markovian demand. Eur. J. Oper Res. 270(1):198–217.

Natarajan KV, Swaminathan JM (2014) Inventory management in humanitarian operations: Impact of amount, schedule, and uncertainty in funding. Manufacturing Service Oper. Management 16(4):595–603.

Noyan N, Balcik B, Atakan S (2016) A stochastic optimization model for designing last mile relief networks. Transportation Sci. 50(3):1092–1113.

Oroojlooyjadid A, Snyder LV, Taka´c ˇ M (2020) Applying deep learn ing to the newsvendor problem. IISE Trans. 52(4):444–463.

Park I, Sharman R, Rao HR (2015) Disaster experience and hospital information systems. MIS Quart. 39(2):317–344.

Pe´rez-Rodr´ıguez N, Holgu´ın-Veras J (2016) Inventory-allocation distribution models for postdisaster humanitarian logistics with explicit consideration of deprivation costs. Transportation Sci. 50(4):1261–1285.

Petrovic N, Alderson DL, Carlson JM (2012) Dynamic resource allocation in disaster response: Tradeoffs in wildfire suppression. PLoS One 7(4):e33285.

Rai A (2017) Editor’s comments: Diversity of design science research. MIS Quart. 41(1):iii–xviii.

Rennemo SJ, Rø KF, Hvattum LM, Tirado G (2014) A three-stage stochastic facility routing model for disaster response planning. Transportation Res. Part E Logist. Transportation Rev. 62:116–135.

Rivera-Royero D, Galindo G, Yie-Pinedo R (2016) A dynamic model for disaster response considering prioritized demand points. Socio-Economic Planning Sci. 55:59–75.

Rizoiu MA, Lee Y, Mishra S, Xie L (2017) Hawkes processes for events in social media. Chang S-F, ed. Frontiers in Multimedia Research (Association for Computing Machinery and Morgan & Claypool, New York), 191–218.

Shchur O, Bilos ˇ M, Gu¨ nnemann S (2020) Intensity-free learning of temporal point processes. Internat. Conf. Learn. Representations (OpenReview.net).

Shchur O, Tu¨ rkmen AC, Januschowski T, Gu¨ nnemann S (2021) Neural temporal point processes: A review. Zhou ZH, eds. Twenty-Ninth Internat. Joint Conf. Artificial Intelligence, vol. 5 (ijcai.org), 4585–4593.

Sutton RS, Barto AG (2018) Reinforcement Learning: An Introduction, 2nd ed. (MIT Press, Cambridge, MA).

Syntetos AA, Boylan JE, Disney SM (2009) Forecasting for inventory planning: A 50-year review. J. Oper. Res. Soc. 60(sup1):S149–S160.

Tan M, Yuan S, Li S, Su Y, Li H, He F (2019) Ultra-short-term industrial power demand forecasting using lstm based hybrid ensemble learning. IEEE Trans. Power Systems 35(4):2937–2948.

Taylor JW (2007) Forecasting daily supermarket sales using exponentially weighted quantile regression. Eur. J. Oper. Res. 178(1): 154–167.

Turkmen AC, Wang Y, Januschowski T (2019) Intermittent demand forecasting with deep renewal processes. NeurIPS 2019 Workshop Temporal Point Processes (Neural Information Processing Systems Foundation, Inc., La Jolla, CA).

Tzeng GH, Cheng HJ, Huang TD (2007) Multi-objective optimal planning for designing relief delivery systems. Transportation Res. Part E Logist. Transportation Rev. 43(6):673–686.

Vanajakumari M, Kumar S, Gupta S (2016) An integrated logistic model for predictable disasters. Production. Oper. Management 25(5):791–811

Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser L, Polosukhin I (2017) Attention is all you need. Guyon I, Luxburg U, Bengio S, Wallach HM, Fergus R, Vishwanathan SV, Garnett R, eds. Adv. Neural Inform. Processing Systems (Neural Information Processing Systems Foundation, Inc., La Jolla, CA), 5998–6008.

Xiao S, Xu H, Yan J, Farajtabar M, Yang X, Song L, Zha H (2018) Learning conditional generative models for temporal point processes. McIlraith SA, Weinberger KQ, eds. AAAI’18/IAAI’18/EAAI’18 Proc Thirty-Second AAAI Conf. Artificial Intelligence Thirtieth Innovative Appl. Artificial Intelligence Conf. Eighth AAAI Sympos. Ed. Adv. Artificial Intelligence (AAAI Press, Palo Alto, CA), 6302–6309.

Xu D, Hu PJH, Fang X (2023) Deep learning-based imputation method to enhance crowdsourced data on online business directory platforms for improved services. J. Management Inform. Sys tems 40(2):624–654.

Yan J, Liu X, Shi L, Li C, Zha H (2018) Improving maximum likelihood estimation of temporal point process via discriminative and adversarial learning. Lang J, eds. Proc. Twenty-Seventh Internat. Joint Conf. Artificial Intelligence (ijcai.org), 2948–2954.

Ye J, Sun L, Du B, Fu Y, Xiong H (2021) Coupled layer-wise graph convolution for transportation demand prediction. Proc. AAAI Conf. Arti ficial Intelligence vol. 35 (AAAI Press, Palo Alto, CA), 4617–4625.

Yi Z, Liu XC, Wei R, Chen X, Dai J (2022) Electric vehicle charging demand forecasting using deep learning model. J. Intelligent Transportation Systems 26(6):690–703.

Zhang Q, Lipani A, Kirnap O, Yilmaz E (2020) Self-attentive Hawkes process. Proc. 37th Internat. Conf. Machine Learn. vol. 119 (PMLR), 11183–11193.

Zhao Y (2009) Analysis and evaluation of an assemble-to-order system with batch ordering policy and compound poisson demand. Eur. J. Oper. Res. 198(3):800–809.

Zhu H, Samtani S, Brown R, Chen H (2021) A deep learning approach for recognizing activity of daily living (ADL) for senior care: Exploiting interaction dependency and temporal patterns. MIS Quart. 45(2):859–896.

Zipkin P (2000) Foundations of Inventory Management, Irwin/McGraw-Hill Series in Operations and Decision Sciences (McGraw-Hill New York).

Zuo S, Jiang H, Li Z, Zhao T, Zha H (2020) Transformer Hawkes process. Proc. 37th Internat. Conf. Machine Learn. vol. 119 (PMLR, New York), 11692–11702.

C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pera</sub>ti<sub>ons</sub> R<sub>esearc</sub>h & th<sub>e</sub> M<sub>anagemen</sub>t S<sub>c</sub>i<sub>ences an</sub>d it<sub>s con</sub>t<sub>en</sub>t <sub>may no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or</sub> <sub>ema</sub>il<sub>e</sub>d t<sub>o</sub> <sub>mu</sub>lti<sub>p</sub>l<sub>e</sub> <sub>s</sub>it<sub>es</sub> <sub>or</sub> <sub>pos</sub>t<sub>e</sub>d t<sub>o</sub> <sub>a</sub> li<sub>s</sub>t<sub>serv</sub> <sub>w</sub>ith<sub>ou</sub>t th<sub>e</sub> <sub>copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup> <sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use.</sub>
