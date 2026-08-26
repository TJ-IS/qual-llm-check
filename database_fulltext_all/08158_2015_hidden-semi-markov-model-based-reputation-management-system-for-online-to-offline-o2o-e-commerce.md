---
otero_id: 8158
otero_key: "Y7WGAWK6"
title: "Hidden semi-Markov model-based reputation management system for online to offline (O2O) e-commerce markets"
authors: "Shengsheng Xiao; Ming Dong"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.05.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Hidden semi-Markov model-based reputation management system for online to offline (O2O) e-commerce markets

Shengsheng Xiao, Ming Dong

Antai College of Economics & Management, Shanghai Jiao Tong University, 535 Fahua Zhen Road, Shanghai, 200052, PR China

## a r t i c l e i n f o

Article history: Received 29 November 2012 Received in revised form 25 April 2015 Accepted 28 May 2015 Available online 5 June 2015

Keywords: Online to offline e-commerce Reputation management system Hidden semi-Markov model

## a b s t r a c t

The rapid development of information technology enables an increasing number of consumers to search and book products/services online first and then to consume them in brick-and-mortar stores. This new ecommerce model is called online to offline (O2O) e-commerce and has received significant managerial and academic attention. Compared with many extant e-commerce models (i.e., B2B, B2C and C2C), reputation management in this emerging model needs some improvement. It has to collect more raw reputation-related data, consider more reputation-related factors and show more comprehensive reputation evaluation results. As a stepping-stone in the research in O2O e-commerce, a new reputation management system (HSMM-RMS) has been developed based on a probabilistic model called the hidden semi-Markov model. By combining observable online and offline raw reputation information, the proposed system can accurately, promptly and dynamically provide O2O e-commerce participants with of ine merchants' historical and predictive reputation information. Our Monte-Carlo simulation experiments indicate that the proposed system performs significantly better than the extant hidden Markov model-based reputation management system. A case study based on a real O2O e-commerce platform demonstrates the real application of HSMM-RMS. It also shows that the proposed system can provide a realistic solution for reputation management in the O2O e-commerce market.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

The rapid development of information technology enables increasing numbers of consumers to seek and book products/services online first and then consume them in brick-and-mortar stores. This emerging trend is called “online-to-offline (O2O) e-commerce” and can be exemplified by services such as Groupon, Yelp and Dianping in the restaurant business, TripAdvisor and Hipmunk in the travel business, and Zipcar and Uber in the transportation business. According to a recent report from the IIMedia Consultation Group, the market size of O2O e-commerce in China alone amounted to 98.68 billion RMB at the end of 2012 and will increase to 418.85 billion RMB by the end of 2015 [1]. Attracted by this huge profit potential, an increasing number of companies will enter into this new market. However, the latest feedback from this market shows that the flourishing prospect of O2O e-commerce largely depends on whether offline merchants can provide consumers with consistent products/services as claimed online. That is to say, offline merchants' reputation plays a vital role in the further development of O2O e-commerce. In fact, in the e-business market, merchants' reputation can help consumers reduce information asymmetry and increase their acceptance of e-commerce [2]. For many e-commerce models (e.g., B2C, C2C and B2B), reputation management has become one of the critical factors that restrict their development [2–4], and this is also no exception to the O2O e-commerce model.

Because of the importance of reputation management, a variety of reputation management systems/models that can be used in many extant e-commerce markets have been developed during the past several years [5–8]. However, reputation management in the emerging O2O e-commerce needs some improvements. First, in the O2O ecommerce market, reputation management has to address participants from both online and offline settings (e.g., online consumers and brickand-mortar restaurants on Yelp). To provide precise reputation assessment results, the reputation management in this scenario has to collect both online and offline raw reputation-related information,<sup>1</sup> whereas extant reputation management systems/models mainly focus on the information collected from either an online or offline setting alone. Second, reputation management in O2O e-commerce has to take the fluctuant demand information and offline merchants' real service capabilities into account when evaluating their reputations. Different from these traditional e-commerce models, customers in the O2O e-commerce market consume the online-reserved products/services in brick-andmortar stores. Each offline merchant has limited service capacity; if the number of consumers who visit a merchant exceeds its maximum capacity in a certain period of time, its product/service quality may be affected. This implies that an offline merchant may not be able to provide consumers with products/services that are consistent with those claimed online. As a result, to check offline merchants' overload operation behavior, reputation management in the O2O e-commerce should consider their fluctuant demands and their real service capacities. Third, the predictive reputation information about offline merchants can help online consumers choose appropriate product/service providers and determine their consumption time in advance. The extraction of predictive reputation information, while feasible in the O2O scenario, is not considered by the extant reputation management systems.

To leverage these opportunities, we propose a new reputation management system (HSMM-RMS) based on a probabilistic model called the hidden semi-Markov model. In this system, offline merchants are modeled by HSMMs (i.e., HSMM with different parameter values). Their observable reputation-related information and hidden reputation states are denoted by observation variables and latent states in HSMMs. By collecting and processing raw reputation-related data from both online and offline settings, offline merchants' hidden reputation sequence ${ { Q } ^ { * } }$ and the “optimal” reputation state structure HSMM λ<sup>⁎</sup> (which perfectly describes offline merchants' reputation behavior given the observable data) will be quickly derived and continually updated through a modified forward and backward algorithm. The proposed system is able to improve reputation management in the O2O e-commerce.

The main contributions of our study are threefold: First, we extend traditional reputation management studies that use online reputationrelated information alone. We explore reputation management issues in the emerging O2O e-commerce setting by combining reputationrelated information from online and offline channels. Second, we establish a systematic framework for a reputation management system in the O2O setting and illustrate how the raw information can be acquired, processed and distributed within this system. Third, our study also enriches extant reputation management models from the methodological perspective. We develop a hidden semi-Markov model to describe offline merchants' reputation behavior. It relaxes many extant assumptions on reputation behavior and performs better than the HMM-based reputation management model.

The rest of this paper is organized as follows: Section 2 reviews the related literature. Section 3 provides a detailed description of our HSMM-based reputation management system (HSMM-RMS) and derives the HSMM-based reputation management model. Section 4 evaluates the performance of our model through Monte-Carlo simulations. In Section 5, a case study based on a real O2O e-commerce platform is conducted to illustrate the application of HSMM-RMS. Section 6 draws conclusions and provides future research directions.

## 2. Literature review

In this section, relevant reputation management studies are reviewed, and some probabilistic reputation management models are summarized.

## 2.1. Reputation management-related studies

There has been a steady stream of studies that address reputation management problems over the past several decades. By using a classification method similar to that of Lee et al. [9], we broadly divide the extant studies into four types (see Fig. 1). Works of the first type focus on offline reputation management issues alone, and they do not directly discuss e-commerce-related reputation management problems. The second research type mainly focuses on reputation management problems from offline to online channels. Studies of this type can be summarized by the following questions: Can offline merchants' trust and reputation be successfully transferred from offline to online channels? What factors will affect this transformation? What should be done to ensure this transformation [9–14]? Different from the first two research types, the third research type only focuses on online reputation-related problems; for example, What are the antecedents of online reputation management [12,13]? What are the constructs of online reputation [14,15]? What are the consequences of online reputation management [16]? In addition, it also discusses some extant reputation management systems used by eBay [17,18], Amazon [19,20] and Alibaba [21]. More information about this research type can be found in [3,4,6,22,23]. Research type 4 in Fig. 1 mainly concentrates on new reputation management problems that stem from online to offline channels. To the best of our knowledge, the majority of extant studies of this type focus on the following issues: Can successful online companies transfer their reputation from online to offline settings? How do successful online companies transfer their trust/reputation? Studies on how to develop a system to improve reputation management in the emerging O2O e-commerce setting are limited. As a result, one of the aims of this paper is to fill this gap.

![](/api/attachments/Y7WGAWK6/fulltext/images/39dcdb0c5c9676a87f4fe5525fc9cae170e98e417de18abaeba863bbd89ad118.jpg)  
Fig. 1. Four types of reputation management research.

## 2.2. Probabilistic models used in reputation management systems

Although researchers have introduced a variety of trust/reputation management models [5,6,24,25], we only focus on probabilistic reputation management models in this study.

## 2.2.1. Belief-based reputation management model

Based on the belief and probability theory, this model assumes that the sum of probabilities over all possible outcomes is not necessarily equal to one [6]. In this model, an agent A's personal perceived value on believing in agent B is usually expressed by a quadruple belief metric $( b , d , u , a )$ and can be calculated by $( b + a \cdot u )$ . (Here, parameters b, d and u reflect agent A's belief, disbelief, and uncertainty value toward agent B, respectively. Parameter a is the relative atomicity that represents the base rate probability in the absence of evidence [26,27]). If the belief values of all the participants are aggregated, the reputation score of each participant in this model can be obtained [28]. This model has been extended and widely used in the literature since it was systematically introduced by Falcone et al. [29–32].

The participants in this model are always assumed to be homogeneous. They have similar interactions with each other and use the same metric to evaluate their belief values. However, in many real e-commerce markets (including the O2O market), there exist many types of participants (e.g., online consumers, offline merchants and offline authoritative parties and organizations). Because the interactions between consumers and merchants are usually different from those between third parties and merchants, participants are actually inhomogeneous. Without improvement, this model has difficulty in quantifying and computing the aggregated reputation score by using the same belief metrics. In addition, although the aggregated reputation score in this model is useful, it simply reflects an agent's historical reputation information. To be more applicable in O2O e-commerce, a model should provide consumers with predictive reputation information about merchants.

## 2.2.2. Bayesian-based reputation management model

This reputation management model is based on Bayesian updating theory. In the model, each participant's behavior is represented by a Beta probability density function belt(p|α, β) that will be dynamically updated with the changes of α and β (α and β are the numbers of satisfied and dissatisfied experiences of a participant in his/her interactions with another participant. For example, if one has two satisfied experiences and three dissatisfied experiences in his/her past five visits to a restaurant, then α = 2 and β = 3) [24,26,33]. Currently, this model has been extended: On one hand, more parameters are added to the Beta function to measure more participants' reputation information [34–37]; on the other hand, “decay factors” are included to consider the time effect of reputation information [33,38,39].

However, participants in this model are assumed to have a fixed probability distribution over all possible outcomes in their interactions, and their reputation states are updated according to this distribution. In many e-commerce markets (including the O2O e-commerce market), merchants' reputation states usually do not follow any fixed distribution. As a result, it is inappropriate to use the Bayesian-based reputation model to directly describe the reputation behavior of offline merchants.

## 2.2.3. HMM-based reputation management model

The hidden Markov model (HMM) is a statistical Markov model in which the agent being modeled is assumed to follow a Markov process with many unobserved states [40]. It is usually denoted by a compact structure $\lambda = ( \pi , A , B ) . ^ { 2 }$ In the model, participants' unobservable reputation behavior is modeled by discrete reputation states and can be reflected by their observable reputation-related information. Moreover, estimated reputation states in the model can be dynamically updated once new reputation-related information is added [41,42]. Moe et al. compare the HMM-based reputation model with the Bayesian-based reputation model and find that the former performs better than the latter [43].

Unfortunately, the HMM-based reputation model has two limitations when directly used in many real e-commerce markets (including the O2O market). One is its unreasonable assumption of the duration of the reputation state [40]. In HMM, the probability that an offline merchant's reputation remains in state i for d time units can be denoted by P (d). According to the Markov assumption and probability theory, P (d) is actually the product of all of the d probabilities: $P _ { i } ( d ) =$ $a _ { i i } ^ { \phantom { \dagger } } ^ { d - 1 } ( 1 - a _ { i i } )$ (where $a _ { i i }$ is the self-loop probability of state i). It is obvious that $p _ { i } ( d )$ is a geometrically decaying function of d. If the HMMbased reputation model is directly used in the real e-commerce market, we actually assume that the probability that a participant remains in a reputation state i for exactly d time units is a geometrically decaying function of d. This is a relatively rigid assumption. Another drawback of this model is that only a limited number of observations are allowed to be emitted by each reputation state at a certain time point [44,45].

To leverage reputation management opportunities in O2O ecommerce, we propose a new probabilistic model (hidden semi-Markov-based reputation management model) by taking advantage of the extant models while mitigating their limitations. The proposed model has the same structure as the HMM model, but it relaxes the limiting assumptions [44–46]. Similar to the belief-based model, it can collect and quantify different reputation-related information, and similar to the Bayesian-based model, it can dynamically update the reputation states of offline merchants while extending their limitations.

## 3. HSMM-based reputation management systems in O2O E-commerce

In this section, we describe the framework and data flow diagram of HSMM-based reputation management system and derive the HSMM-based reputation management model.

## 3.1. The framework of HSMM-RMS

The HSMM-RMS is divided into four subsystems: the Information-Capturing Subsystem, the Database Management Subsystem, the Module Management Subsystem, and the User Interface Subsystem (see Fig. 2).

The Information-Capturing Subsystem is designed to collect raw reputation data in both online and offline settings. It is directly managed by the “customers' information management module” and the “offline merchants and third-party information management module” in the Module Management Subsystem. Data collected from online setting mainly includes the profiles of consumers and merchants, online reviews, and consumers' consumption records, etc. Data collected from an offline setting mainly refers to the information recorded by some authoritative third parties (e.g., business management associations, accreditation agencies and other government and nongovernment institutions). It includes offline merchants' service capability, credit records, accreditation status, regulatory compliance records, industry standard compliance records, health inspection records etc. Detailed descriptions of these datasets can be found in Table 1, Figs. 3 and 4.

![](/api/attachments/Y7WGAWK6/fulltext/images/71f5d48032fa03313031639eace5b4ce1beecd5fa6df9451ef8be49e4eddbee3.jpg)  
Fig. 2. Framework of HSMM-RMS.

Table 1  
Detailed data structure information about D1–D4.

<table><tr><td colspan="2">Detailed information about D1</td><td colspan="2">Detailed information about D2</td></tr><tr><td>Name</td><td>Data from consumers</td><td>Name</td><td>Offline merchant-related data</td></tr><tr><td>Description</td><td>It mainly refers to online consumers&#x27; profile data, consumption records, online reviews, etc.</td><td>Description</td><td>It mainly refers to offline merchants&#x27; profile data.</td></tr><tr><td>Data items</td><td>Customer ID, service or product booked time, consumption time, rating scores, rating time.</td><td>Data items</td><td>Offline merchant ID, type of service or product provided, address, current service ability, current reputation state, updating time, predicted reputation state.</td></tr><tr><td colspan="2">Detailed information about D3</td><td colspan="2">Detailed information about D4</td></tr><tr><td>Name</td><td>Data from third parties</td><td>Name</td><td>Processed reputation data</td></tr><tr><td>Description</td><td>It mainly refers to the supplemental offline reputation-related data from authoritative third parties. It includes offline merchants&#x27; initial registered capital, reputation-related records, etc.</td><td>Description</td><td>It is a combination of D1–D3 and can be directly provided to the HSMM-based reputation management model.</td></tr><tr><td>Data items</td><td>Offline merchant ID, initial registered capital, maximum service ability, historical credit records, accreditation status, regulatory compliance records, industry standard compliance records, health inspection records, the third party ID, time of registration.</td><td>Data items</td><td>1. Online part (offline merchant ID, rating scores, rating time, current service capacity);2. Offline part (reputation-related records such as regulatory compliance records, industry standard compliance records, health inspection records and other data items).</td></tr></table>

The Database Management Subsystem mainly manages data provided by the Information-Capturing Subsystem, and its work procedure is described in Fig. 3. First, datasets from consumers, merchants and third parties are collected and stored in separate databases. Second, with the help of the “reputation information-preprocessing module” in the Module Management Subsystem, separate data sources are cleaned, merged and reorganized. Specifically, in this step, noisy and useless data (i.e., spam reviews and advertisements) are removed, and datasets are merged according to the merchants described. The processed data, which can reflect offline merchants' reputation states, is reorganized and stored with a standard structure including online and offline parts (see D3 in Table 1).

As a core part of HSMM-RMS, the Module Management Subsystem works like a bridge that links the Database Management Subsystem and the User Interface Subsystem. In this subsystem, the “customers' information management module” and the “offline merchants and third party information management module” are designed to manage the data-collecting task. The “reputation information-preprocessing module” is used to control the data-preprocessing procedure. The “HSMMbased reputation management module” works based on the Hidden Semi-Markov Model (which will be analyzed in the next section). The “Display of offline merchants' reputation module” is employed to publish offline merchants' latest reputation information provided by the “HSMM-based reputation management module.”

The User Interface Subsystem is designed to address O2O participants' requests sent through laptops, mobile phones, and tablet computers, among others.

Fig. 4 provides a detailed data flow diagram of HSMM-RMS. In this diagram, data from online consumers, offline merchants and authoritative third parties are first collected by “customers' information management” (P1) and the “offline merchants and third party information management” (P2) before being stored in D1–D3.<sup>3</sup> Next, data flows from D1, D2 and D3 are processed by the “reputation-related datapreprocessing” procedure (P3). The processed data are stored in D4 and can be directly used by the “HSMM-based reputation management” (P4). The detailed procedures of P4 will be discussed in the next section. New reputation information from P4 will be used to update D2. Finally, offline merchants' most recent reputation information in D2 will be published through the “offline merchants' reputationdisplaying” procedure (P5). Detailed information about D1–D4 is listed in Table 1.

It should be noted that D4 is actually a time sequence dataset and contains both online and offline information. Consumers' consumption records (which contain historical demand information and consumers' product/service booking information) in D1 and offline merchants' real service capability in D2 can be used to check offline merchants overload operation behavior by calculating the number of consumers who will visit the merchant at some point in the future (henceforth, called future consumption information). Consumers in the O2O e-commerce can combine this information with offline merchants' predictive reputation information (to be provided by the proposed model) to choose the appropriate services/products providers and suitable consumption time.

## 3.2. HSMM-based reputation management model

Although the real reputation states of offline merchants are unobservable in the O2O e-commerce market, we can explore our HSMMbased reputation management model to perceive them through the observable reputation-related information.

## 3.2.1. Model setup

In our model, we use an N-state hidden semi-Markov model to describe an offline merchant's reputation behavior (N is the total number of reputation states and can be any positive integer) and let the real reputation state change within the N states (from the lowest $q _ { 1 }$ to the highest q ). That is, if we set $N = 5$ for an offline merchant, its real reputation state is allowed to change within five discrete states (from q to q ). Furthermore, if we use s to denote an offline merchant's real reputation state at time t and $O _ { a - b }$ to represent the observable reputation information from time a to b, then the initial parameters $\lambda ^ { o } = ( \pi , A , B , D )$ of our model can be explained as follows:

The parameter $\pi = \{ \pi _ { i } \}$ represents the initial distribution of the merchant's reputation states. For example, if we set $\pi _ { i } = 0 . 2 \ ( i =$ $^ { 1 , . . . , 5 ) }$ for the merchant with five states, we actually assume its initial reputation state can be either $q _ { 1 }$ or q , …or q with equal probability.

The state transition matrix, $A = \{ a _ { \mathrm { i j } } , a _ { i j } = p ( s _ { t \mathrm { ~ + ~ } 1 } = q _ { j } | s _ { t } =$ $q _ { i } ) , 1 \leq i , j \leq N \}$ , describes the probability of state transition for an offline merchant. Because the jump in each offline merchant's reputation state

![](/api/attachments/Y7WGAWK6/fulltext/images/0df29d0cd4594cc3933bb5e62fe02c8f04643920eafa0d9124417d6d223f7507.jpg)  
Fig. 3. Preprocessing procedure of raw data in the Database Management Subsystem.

can be easily perceived by consumers in O2O e-commerce, the change of an offline merchant's reputation state is always gradual because even the dramatic drop or rise in merchants' reputations will be observed and recorded as they transitions through intermediate reputation stages in a relatively short period of time. Therefore, we assume that the change in a reputation state satisfies the one-step Markov process in our model. It should be noted that this assumption is not contradictory with our previous claim that our model is able to address the changing reputation behavior of offline merchants because this can be handled by allowing for very short sojourn time between reputation states.

![](/api/attachments/Y7WGAWK6/fulltext/images/acb5130b41ab2f6433c7a33865c7c9fe04dfff130f5a96b5937478df6f293866.jpg)  
Fig. 4. Data flow diagram of HSMM-RMS. In the figure D stands for datasets and P stands for processes/subsystem components

The duration distribution of a reputation state is denoted by $D =$ $\{ p _ { \mathrm { i } } ( d ) \}$ . It indicates the probability that an offline merchant remains in q for d time units. What should be mentioned is that an offline merchant's residence time in different reputation states is independent of the time spent in previous states [42,44–46]. For example, a restaurant on Yelp can stay in a reputation state for any length of time without considering how long it has already spent in other states.

The distribution of an offline merchant's observable information in a reputation state is represented by $B = \{ b _ { i } ( V _ { a } ^ { b } ) , b _ { i } ( V _ { a } ^ { b } ) = p ( V _ { a } ^ { b } | s _ { a - b } =$ $q _ { i } ) \}$ (where $1 \leq i \leq N ,$ and $s _ { a - b }$ is merchant's reputation state from time a to b). This means that a merchant remaining in reputation state $q _ { i }$ between time a and b will emit observable data sequence $V _ { a } ^ { b }$ with probability $b _ { i } ( V _ { a } ^ { b } )$ . In our model, the observable data are summarized in D4. We use W to denote the number of valid data items that reflect at least one aspect of a merchant's reputation behavior.<sup>4</sup> $\nu _ { i a } ^ { b }$ is used to denote a data item sequence i from time a to b. If the offline merchant is in reputation q at time t, the value of $\nu _ { i a } ^ { b }$ at time t can be denoted by $o _ { i j t } .$ In the literature, discrete observation is always described by a discrete distribution, and continuous observation is modeled by a finite mixture Gaussian distribution $( c _ { j k } , \mu _ { j k } , U _ { j k } ) . ^ { 5 }$ In our system, the continuous data items in D4 (i.e., reputation-related records and service capability) enable us to use the finite mixture Gaussian distribution to describe the observations.

Fig. 5 illustrates all of the parameters used in our model. In this figure, a merchant's reputation can freely transform between its two adjacent states $( \mathrm { i . e . , } q _ { i }$ and $q _ { i + 1 } )$ with probability $a _ { i , \ ( i + 1 ) }$ or $a _ { ( i \mathrm { ~ + ~ } 1 ) , i }$ It can remain in reputation state $q _ { i } \left( q _ { i { \mathrm { ~ + ~ } } 1 } \right)$ for d $\left( d _ { i { \mathrm { ~ + ~ } } 1 } \right)$ time units with probability $p _ { i } ( d _ { i } )$ (or $p _ { ( i \mathrm { ~ + ~ } 1 ) } \big ( d _ { ( i \mathrm { ~ + ~ } 1 ) } \big ) \big )$ and emit observable information $V _ { a } ^ { a + d _ { i } } ( V _ { a + d _ { i } } ^ { a + d _ { i } + d _ { j } } )$ during its sojourn time. Some key notations used in the model are summarized in Appendix A.

## 3.2.2. Reputation management procedure

Given an offline merchant's observable reputation-related information (D4) in the past T time units, we need to find its most likely reputation state sequence ${ Q } ^ { * }$ (henceforth called the “optimal” state sequence ${ { Q } ^ { * } } )$ in the past T time units, and the most likely reputation state structure HSMM $\lambda ^ { * }$ (henceforth called the “optimal” HSMM $\lambda ^ { * } )$ . The former directly shows offline merchants' reputation states, and the latter perfectly describes the relationship between hidden reputation states and observable reputation-related information (D4). The complete computation procedure consists of the following steps:

## Step 1 Define new variables

To find a reputation state sequence, $Q = \{ q _ { 1 } q _ { 2 } \dots q _ { \mathrm { T } } \}$ , for the given observation $V _ { 1 } ^ { T } = \{ \nu _ { 1 , } ^ { T } \nu _ { 2 1 } ^ { \hat { T } } . . . \nu _ { W _ { 1 } } ^ { T } \}$ , we need to define some new variables in this step.

First, we define a forward variable $\alpha _ { t } ( i )$ . This variable denotes the probability that an offline merchant generates observation $V _ { 1 } ^ { t }$ and ends in state $q _ { i }$ during the past t time units:

$$
\alpha_ {t} (i) = P \bigl (V _ {1} ^ {t}, s _ {t ]} = i | \lambda \bigr)\tag{1}
$$

Because observations at different time points are assumed to be independent, if we use $D _ { i }$ to denote the maximal duration of reputation state $q _ { i } ,$ we will find:

$$
\begin{array}{l} \alpha_ {t} (i) = \sum_ {i = 1} ^ {N} \sum_ {d = 1} ^ {\min (D _ {i}, t)} \alpha_ {t - d} (i) a _ {i j} P _ {j} (d) b _ {j} \left(V _ {t - d + 1} ^ {t}\right) \\ = \sum_ {i = 1} ^ {N} \sum_ {d = 1} ^ {\min (D _ {i}, t)} \alpha_ {t - d} (i) a _ {i j} P _ {j} (d) \prod_ {s = t - d + 1} ^ {t} b _ {j} \left(V _ {s}\right) \end{array}\tag{2}
$$

The conditional probability that an offline merchant generates observation $V _ { 1 } ^ { T }$ given the reputation state structure HSMM λ can be written as:

$$
P \left(V _ {1} ^ {T} | \lambda\right) = \sum_ {i = 1} ^ {N} \alpha_ {T} (i)\tag{3}
$$

Similarly, we define a backward variable $\beta _ { t } ( i )$ . This variable denotes the probability that an offline merchant generates observation $\bar { V _ { t \mathrm { ~ + ~ } 1 } ^ { T } }$ beginning with state q at time t:

$$
\beta_ {t} (i) = P \left(V _ {t + 1} ^ {T} \mid s _ {[ t} = i, \lambda\right) = \sum_ {j = 1} ^ {N} \sum_ {d = 1} ^ {\min (D, t)} a _ {i j} P _ {j} (d) b _ {j} \left(V _ {t + 1} ^ {t + d}\right) \beta_ {t + d} (j)\tag{4}
$$

Because the sojourn time of reputation states and the number of observations emitted by any state are changeable in our model, three more segment-featured variables $( \alpha _ { t , t } \cdot ( i , j ) , \phi _ { t , t } \cdot ( i , j )$ and $\xi _ { t , t } , ( i , j ) )$ are defined to accurately describe an offline merchant's behavior.<sup>6</sup>

$$
\alpha_ {t, t ^ {\prime}} (i, j) = P \left(V _ {1} ^ {t ^ {\prime}}, s _ {t} = i, s _ {t ^ {\prime}} = j | \lambda\right)\tag{5}
$$

$$
\phi_ {t, t ^ {\prime}} (i, j) = \sum_ {d = 1} ^ {D _ {i}} \left[ P (d = t ^ {\prime} - t | i) \cdot P \left(V _ {t + 1} ^ {t ^ {\prime}} \mid s _ {t} = i, s _ {t ^ {\prime}} = j, \lambda\right) \right]\tag{6}
$$

$$
\xi_ {t, t ^ {\prime}} (i, j) = P \left(s _ {t} = i, s _ {t ^ {\prime}} = j \mid V _ {1} ^ {T}, \lambda\right)\tag{7}
$$

Here, $\alpha _ { t , t } ~ \cdot ( i , ~ j )$ represents the probability that an offline merchant has a reputation state $q _ { i }$ at time $t , q _ { j }$ at time $t ^ { \prime } ,$ and generates observation sequence $V _ { 1 } ^ { t ^ { \prime } } . \phi _ { t , t } \cdot ( i , j )$ is the average probability that a merchant remains in reputation state $q _ { i }$ for d time units and then moves to state $q _ { j } .$ The conditional probability of $\phi _ { t , t } \cdot ( i , j )$ given $V _ { 1 } ^ { T }$ is represented by $\xi _ { t , t } \cdot ( i , j )$ . The relationship among these new variables can be further expressed as follows:

$$
\begin{array}{c} \alpha_ {t, t ^ {\prime}} (i, j) = P \bigl (V _ {1} ^ {t}, s _ {t} = i | \lambda \bigr) \cdot P \Bigl (V _ {t + 1} ^ {t ^ {\prime}}, s _ {t ^ {\prime}} = j | V _ {1} ^ {t}, s _ {t} = i, \lambda \Bigr) \\ = \alpha_ {t} (i) a _ {i j} \phi_ {t, t ^ {\prime}} (i, j) \end{array}\tag{8}
$$

$$
\alpha_ {t ^ {\prime}} (j) = P \left(V _ {1} ^ {t ^ {\prime}}, s _ {t ^ {\prime}} = j | \lambda\right) = \sum_ {i = 1} ^ {N} \sum_ {d - 1} ^ {D _ {i}} P (d = t ^ {\prime} - t | j) \alpha_ {t, t ^ {\prime}} (i, j)\tag{9}
$$

$$
\xi_ {t, t ^ {\prime}} (i, j) = \frac {\sum_ {d = 1} ^ {D _ {i}} \alpha_ {t} (i) a _ {i j} \phi_ {t , t ^ {\prime}} (i , j) \beta_ {t ^ {\prime}} (j)}{\beta_ {0} (i = s _ {0})} \left(s _ {0} \text {   is   the   initial   reputation   state }\right)\tag{10}
$$

![](/api/attachments/Y7WGAWK6/fulltext/images/ce90025129f179c54b543d55af0347f01bc8ecda9fb6bace74fe10f696f13931.jpg)  
Fig. 5. Illustration of HSMM-based reputation management model.

These new variables can help us describe merchants' reputation states and observable information. Furthermore, they also improve the computing speed in the following two steps.

Step 2 Search for the “optimal” HSMM

Given an offline merchant's observation sequence V and the initial value of HSMM $\boldsymbol { \lambda } ^ { 0 }$ , we will search for the “optimal” HSMM λ<sup>⁎</sup> in this step. Specifically, we will use a statistical learning method called the Expectation-Modification (EM) algorithm to find the “optimal” HSMM $\lambda ^ { * } = ( \pi , A , B , D )$ through a recursive computing procedure [47]. The re-estimation formulas for the parameters in HSMM can be written as follows:

$$
\overline {{\pi}} _ {i} = \frac {\pi_ {i} \left[ \sum_ {d = 1} ^ {D _ {i}} \beta_ {d} (i) P (d | i) b _ {j} \left(o _ {1} ^ {d}\right) \right]}{P \left(o _ {1} ^ {T} | \lambda\right)}\tag{11}
$$

$$
\overline {{a _ {i j}}} = \frac {\sum_ {t = 1} ^ {T} \xi_ {t , t ^ {\prime}} (i , j)}{\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} \sum_ {t = 1} ^ {T} \xi_ {t , t ^ {\prime}} (i , j)}\tag{12}
$$

$$
\frac {b _ {i} (k)}{s . t . o _ {t} = o _ {k}} = \frac {\sum_ {t = 1} ^ {T} \alpha_ {t} (i) \left[ \frac {\phi_ {t , t ^ {\prime}} (i , j)}{\sum_ {d = 1} ^ {D _ {i}} P (d = t ^ {\prime} - t | i)} \right] \beta_ {t} (i)}{\sum_ {t = 1} ^ {T} \alpha_ {t} (i) \left[ \frac {\phi_ {t , t ^ {\prime}} (i , j)}{\sum_ {d = 1} ^ {D _ {i}} P (d = t ^ {\prime} - t | i)} \right] \beta_ {t} (i)}\tag{13}
$$

$$
\overline {{p _ {i} (d)}} = \frac {\sum_ {t = 1} ^ {T} \left\{\left[ \sum_ {j = 1} ^ {N} \alpha_ {t} (j) a _ {j i} \right] p _ {i} (d) \beta_ {t + d} (i) \prod_ {s = t + 1} ^ {t + d} b _ {i} (o _ {s}) \right\}}{\sum_ {d = 1} ^ {D _ {i}} \sum_ {t = 1} ^ {T} \left\{\left[ \sum_ {j = 1} ^ {N} \alpha_ {t} (j) a _ {j i} \right] p _ {i} (d) \beta_ {t + d} (i) \prod_ {s = t + 1} ^ {t + d} b _ {i} (o _ {s}) \right\}},\tag{14}
$$

If we use a mixture Gaussian distribution to describe the distribution of an offline merchant's observable information $b _ { j } ( V _ { k } )$

then re-estimation formulas about these coefficients in the mixture Gaussian distribution can be written as follows [40]:

$$
\begin{array}{l} \overline {{c _ {j k}}} = \frac {\sum_ {t = 1} ^ {T} \gamma_ {t} (j , k)}{\sum_ {t = 1} ^ {T} \sum_ {k = 1} ^ {M} \gamma_ {t} (j , k)} \\ \overline {{\mu}} _ {j k} = \frac {\sum_ {t = 1} ^ {T} \gamma_ {t} (j , k) \cdot o _ {t}}{\sum_ {t = 1} ^ {T} \gamma_ {t} (j , k)} \\ \overline {{U _ {j k}}} = \frac {\sum_ {t = 1} ^ {T} \gamma_ {t} (j , k) \cdot \left(o _ {t} - \mu_ {j k}\right) \left(o _ {t} - \mu_ {j k}\right) ^ {\prime}}{\sum_ {t = 1} ^ {T} \gamma_ {t} (j , k)} \\ \gamma_ {t} (j, k) = \left[ \frac {\alpha_ {t} (j) \beta_ {t} (j)}{\sum_ {j = 1} ^ {N} \alpha_ {t} (j) \beta_ {t} (j)} \right] \left[ \frac {c _ {j k} N \left(o _ {t} , \mu_ {j k} , U _ {j k}\right)}{\sum_ {m = 1} ^ {M} c _ {j m} N \left(o _ {t} , \mu_ {j k} , U _ {j k}\right)} \right] \end{array}\tag{15}
$$

<sub>ð</sub><sup>16</sup><sub>Þ</sub>

<sub>ð</sub><sup>17</sup><sub>Þ</sub>

<sub>ð</sub><sup>18</sup><sub>Þ</sub>

Step 3 Evaluate and update the reputation state

In this step, we modified the traditional forward-backward algorithm in HMM to derive an offline merchant's “optimal” state sequence ${ Q } ^ { * }$ . The modified algorithm (whose pseudo code is listed in Appendix B) utilizes all the variables and formulas mentioned above and can be further divided into two parts: the forward pass and the backward pass. The former is used to describe an offline merchant's behavior before time t, and the latter is used to explain its behavior from time t to the end. By combining these two parts, we can easily find the “optimal” reputation sequence for the merchant.

It should be noted that the ${ { Q } ^ { * } }$ and the optimal HSMM <sup>⁎</sup> will be continuously updated once new observable information about a reputation state is added to our model. Information in ${ { Q } ^ { * } }$ and $\lambda ^ { * }$ will be provided to the O2O participants through P5 in the HSMM-RMS. They will also be used to update D2 in Fig. 4.

## 3.3. Model analysis and discussion

One important part of our model is the modified forward-backward algorithm. If we let $D _ { i }$ be the maximum duration time of reputation state $q _ { i } ,$ the computational complexity of our model is $O ( N ^ { 2 } L T )$ , where $L = \sum _ { i = 1 } ^ { N } D _ { i } .$ . In HMM, however, the computational complexity is $O ( N ^ { 2 } T )$ It is obvious that our model and HMM-based reputation management model nearly have a similar magnitude of computational complexity. However, in our model, the duration of the reputation state is no longer confined to a geometrically decaying function, and each state is allowed to generate a segment of observations $( \mathrm { i . e . , } \nu _ { 1 a } ^ { b } , \nu _ { 2 a } ^ { b } , \cdots , \nu _ { W a } ^ { b } )$ during its sojourn time. As a result, our model actually performs better than the HMM-based reputation management model from the theoretical perspective.

Moreover, the proposed model is able to improve reputation management in the O2O e-commerce market. As two important outputs of our model: The reputation state sequence ${ Q } ^ { * }$ records offline merchants' most likely reputation state given the observation sequence $V ;$ The “optimal” HSMM $\lambda ^ { * }$ perfectly describes their reputation behavior. Because ${ Q } ^ { * }$ and V are estimated based on raw reputation-related data, changes in the raw data will be identified and reflected in the reputation evaluation results. If we combine ${ { Q } ^ { * } }$ with HSMM $\lambda ^ { * }$ , we can predict how long an offline merchant will remain in a reputation state.

Finally, the proposed model provides O2O participants with useful information to help them make decisions. Consumers can easily learn the hidden reputation behavior of an offline merchant through the sequence $Q$ and can choose proper service/product providers and suitable consumption time by combining the predictive reputation information of offline merchants with the disclosed future consumption information. Offline merchants are able to know their reputations in the market through $Q _ { \mathrm { { \ell } } }$ and they can take appropriate actions to improve their image. With the help of our system/model, reputation information managers on the O2O platforms such as Yelp and Dianping can provide more accurate reputation evaluation results to the customers to improve their competitiveness.

## 4. Experimental evaluation of the HSMM-RMS

In this section, four Monte-Carlo simulations are conducted to compare the performance of our model with the HMM-based reputation management model in a virtual O2O market.

## 4.1. Monte-Carlo simulation design

According to the widely used distributions of observation and state duration in HSMM [40,44–46], we design four simulation scenarios (see Table 2). In each scenario, a Monte-Carlo model is employed to simulate an offline merchant's reputation behavior in the virtual O2O market. Then, HSMM-based and HMM-based reputation management models are used to evaluate the merchant's real reputation states. Because these two models nearly have the same computational complexity, the total number of reputation states, which is accurately estimated by each model, is used as a criterion to compare their performance.

## 4.2. Experiment procedure and results

In the simulation, N is set to be 3. The one-dimensional observation is assumed to take four discrete and observable values, and is denoted by $o b s = { \left[ \begin{array} { l l l l } { 0 . 5 } & { 0 . 3 } & { 0 . 1 } & { 0 . 1 } \\ { 0 . 1 } & { 0 . 5 } & { 0 . 1 } & { 0 . 1 } \\ { 0 . 1 } & { 0 . 1 } & { 0 . 5 } & { 0 . 3 } \end{array} \right] }$ : <sup>8</sup>The state transition

Four Monte-Carlo simulation scenarios. In the table, the one-dimensional observation refers to the observation with one observable data item and the multi-dimensional observation refers to the observation with many different observable data items

<table><tr><td></td><td>One-dimensional observation with discrete distribution</td><td>Multi-dimensional observation with normal distribution</td></tr><tr><td>Poisson distribution of State duration</td><td>Scenario 1</td><td>Scenario 2</td></tr><tr><td>Normal distribution of State duration</td><td>Scenario 3</td><td>Scenario 4</td></tr></table>

matrix is $T = \left[ { \begin{array} { c c c } { 0 } & { 1 } & { 0 } \\ { 0 . 5 } & { 0 } & { 0 . 5 } \\ { 0 } & { 1 } & { 0 } \end{array} } \right]$ . The three-dimensional continuous

observation satisfies a multivariate normal distribution with mean

$\left[ { \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 3 } & { 3 } & { 3 } \\ { 5 } & { 5 } & { 5 } \end{array} } \right]$ and $\nu a r = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] }$ . The initial probability of each

reputation state is $1 / 3 ,$ , and the parameters of three Poisson state duration distribution are 3, 5, and 7. The three normal state duration distributions are assumed to have mean $\mu _ { 1 } , \mu _ { 2 } , \mu _ { 3 } = 5 , 7 , 9$ and variance $\sigma _ { 1 } , \sigma _ { 2 } , \sigma _ { 3 } = 1 , 1 , 1$

It should be noted that these predetermined parameters will not affect the accuracy of our model evaluation. First, the simulation model in each scenario is just used to simulate the reputation behavior of an offline merchant. It is independent with the abilities of the HSMMbased and HMM-based reputation management model. Second, samples generated in each scenario are random, and their size is sufficient. This provides a fair environment in which to compare these models. Third, both the HSMM-based and the HMM-based reputation management model do not use any a-priori information contained in the simulation model when evaluating reputation states. Therefore, the choice of four simulation scenarios would not put the proposed model in any favorable position in advance. Our simulation follows the following Monte-Carlo procedure:

Step 1 In each scenario, a Monte-Carlo model is used to generate a stochastic sample sequence with size 1000, and a similar generation is repeated 15 times. The ith sample is denoted by $S a m p l e _ { i } = \{ ( w _ { 1 } , u _ { 1 } ) , ( w _ { 2 } , u _ { 2 } ) , \cdots , ( w _ { 1 0 0 0 } , u _ { 1 0 0 0 } ) \}$ (w<sub>i</sub> and $u _ { i }$ represent the hidden reputation states and observation sequence generated in the ith simulation, respectively).

Step 2 In each scenario, both the HSMM-based and HMM-based reputation management models are used to estimate the real reputation states based on the observation sequences. The number of states that are correctly predicted by each model is recorded.

Step 3 In each scenario, a t-test $( \alpha = 0 . 0 5 , 0 . 1 )$ is used to test whether the proposed model performs significantly better than the HMM-based reputation management model.

The results in Fig. 6 show that the proposed model performs better than the HMM-based reputation management model in all scenarios. The results of a t-test $( \alpha = 0 . 0 5 , 0 . 1 )$ in each scenario also support our conclusion.

## 5. A case study on a real O2O e-commerce platform

In this section, a case study on a real O2O platform called Dianping (a leading Chinese O2O e-commerce platform providing all types of local services) is conducted to illustrate the real application of our system/model.

![](/api/attachments/Y7WGAWK6/fulltext/images/bb2fe96f13370a33a0b1e40b3e2d70e7ed7a352320b97c02b4347cad16df1334.jpg)  
(a) Comparison of results in scenario 1

![](/api/attachments/Y7WGAWK6/fulltext/images/40a62b59fb351f054e8f092c1107d8ad7336436cc0b364cd88fa52f24d1e4ad3.jpg)  
(b) Comparison of results in scenario 2

![](/api/attachments/Y7WGAWK6/fulltext/images/4052457f5bf52db1c02c6e32646c2fb70bbd807b951b2f31901c8534c5b89c67.jpg)  
(c) Comparison of results in scenario 3

![](/api/attachments/Y7WGAWK6/fulltext/images/d2869e8395a5c6afcc2b509a1101ad95f9177a872095e0aceb2a465fa8e85ad6.jpg)  
(d) Comparison of results in scenario 4

Fig. 6. Performance comparison of two models in different scenarios.  
![](/api/attachments/Y7WGAWK6/fulltext/images/e645b61f6db9259b42a061b0f98e52142c08688b0b4a5bf7f39cf1d78d1b59e4.jpg)  
Fig. 7. An illustration of a review posted on Dianping.com.

## 5.1. Reputation-related data collecting and pre-processing

In this case, the proposed system is used to evaluate the reputation of a restaurant on Dianping. D1 mentioned in HSMM-RMS mainly stores the online reviews related to the restaurant (from March 3, 2011 to October 6, 2012).<sup>9</sup> A detailed review posted by a consumer called qwer33 is shown in Fig. 7. It contains at least four parts: 1) the overall rating of the restaurant; 2) separate ratings of the food, environment and service quality; 3) text comments; and 4) rating time. D2 stores the restaurant's profile data (i.e., address, real service capability, current reputation state, and registration time). D1 and D2 are taken as the online reputation-related datasets in our case study. D3 mainly stores this restaurant's reputation-related records (e.g., industry standard compliance records and health inspection records) with the offline authoritative third parties and is treated as offline reputation-related data. Because this restaurant has no abnormal records and it operates within its maximum capability without changing any operation policy in the observation window, we only need to focus on the observable online review information to derive its reputation states.<sup>10</sup>

Summary statistics about some data items in D4.

<table><tr><td>Data item sequence</td><td>Observations</td><td>Mean</td><td>Std.</td><td>Median</td><td>Mode</td><td>Min</td><td>Max</td></tr><tr><td>Rating of food</td><td>590</td><td>3.161</td><td>1.002</td><td>3.000</td><td>3.000</td><td>1.000</td><td>5.000</td></tr><tr><td>Rating of environment</td><td>590</td><td>3.241</td><td>0.874</td><td>3.000</td><td>3.000</td><td>1.000</td><td>5.000</td></tr><tr><td>Rating of service quality</td><td>590</td><td>3.207</td><td>1.032</td><td>3.000</td><td>3.000</td><td>1.000</td><td>5.000</td></tr></table>

![](/api/attachments/Y7WGAWK6/fulltext/images/df02e2607544727b0a249bdbf299dc4fdc25f708608a877930a76037918fff89.jpg)  
Fig. 8. Convergence map of parameters in the HSMM-RMS.

Following the data-preprocessing procedure described in Section 3, we remove spam reviews and invalid ratings. Some redundant information is also discarded when generating D4.<sup>11</sup> The preprocessed D4 is represented by a quintuple (Restaurant ID, Rating of food, Rating of environment, Rating of quality, Rating time). The separate rating sequences in D4 reflect its reputation from different aspects, and they can be directly used by our model. Some summary statistics about data items in D4 are listed in Table 3.

## 5.2. Reputation management

Because the overall rating of a restaurant on Dianping.com is five levels, we will use a five-state HSMM to describe the reputation behavior of this restaurant. The initial state transition matrix is given by Tr. Because one month is the typical accounting cycle for Chinese enterprises, restaurant managers may monthly change some reputation state related factors (e.g., quality of food, service, and environment) which may indirectly influence the change of restaurant's reputation state. We assume the maximum duration time for each reputation state is 30 days. What should be noted here is that we do not mean the restaurant's reputation state must be changed every accounting cycle. In fact, it can still stay in the same reputation sate or change to other reputation states. But no matter what it does, it will be treated as a “new state” for the next account cycle. A five-component mixture Gaussian model is used to describe observation in D4.<sup>12</sup>

$$
T r = \left[ \begin{array}{c c c c c} 1 / 2 & 1 / 2 & 0 & 0 & 0 \\ 1 / 3 & 1 / 3 & 1 / 3 & 0 & 0 \\ 0 & 1 / 3 & 1 / 3 & 1 / 3 & 0 \\ 0 & 0 & 1 / 3 & 1 / 3 & 1 / 3 \\ 0 & 0 & 0 & 1 / 2 & 1 / 2 \end{array} \right]
$$

By combining a K-means clustering algorithm with the mixture Gaussian model, we can obtain the initial values of the mixture Gaussian model:

$$
\begin{array}{l} \mu_ {1} = \left[ \begin{array}{c} 2. 3 1 \\ 2. 6 1 \\ 2. 5 2 \end{array} \right], \mu_ {2} = \left[ \begin{array}{c} 3. 0 0 \\ 2. 9 9 \\ 3. 0 4 \end{array} \right], \mu_ {3} = \left[ \begin{array}{c} 3. 1 0 \\ 3. 2 5 \\ 3. 2 4 \end{array} \right], \mu_ {4} = \left[ \begin{array}{c} 4. 0 0 \\ 3. 7 7 \\ 3. 7 7 \end{array} \right], \mu_ {5} = \left[ \begin{array}{c} 5. 0 0 \\ 4. 5 0 \\ 5. 0 0 \end{array} \right], \\ \delta_ {1} = \left[ \begin{array}{c c c} 0. 1 2 & 0 & 0 \\ 0 & 0. 2 5 & 0 \\ 0 & 0 & 0. 2 0 \end{array} \right], \delta_ {2} = \left[ \begin{array}{c c c} 0. 0 1 & 0 & 0 \\ 0 & 0. 1 5 & 0 \\ 0 & 0 & 0. 1 5 \end{array} \right] \end{array}
$$

$$
\begin{array}{l} \delta_ {3} = \left[ \begin{array}{c c c} 0. 3 3 & 0 & 0 \\ 0 & 0. 2 7 & 0 \\ 0 & 0 & 0. 1 1 \end{array} \right], \delta_ {4} = \left[ \begin{array}{c c c} 0. 0 5 & 0 & 0 \\ 0 & 0. 2 5 & 0 \\ 0 & 0 & 0. 2 8 \end{array} \right], \\ \delta_ {5} = \left[ \begin{array}{c c c} 0. 3 5 & 0 & 0 \\ 0 & 0. 1 9 & 0 \\ 0 & 0 & 0. 1 9 \end{array} \right], \\ (c _ {1}, c _ {2}, c _ {3}, c _ {4}, c _ {5}) = (0. 3 1, 0. 2 3, 0. 1 4, 0. 1 2, 0. 2 0) ^ {\prime} \end{array}
$$

where $( \mu _ { 1 } , \mu _ { 2 } , \mu _ { 3 } , \mu _ { 4 } , \mu _ { 5 } )$ are the mean values of the observations emitted in five reputation states. $( \delta _ { 1 } , \delta _ { 2 } , \delta _ { 3 } , \delta _ { 4 } , \delta _ { 5 } )$ represent their covariance matrices, and $( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 5 } )$ are weight coefficients of the five mixture components.

So far, we have initialized the parameters of the HSMM-based reputation management model. With the help of these defined variables and re-estimation formulas in Section 3.2, we can find the “optimal” HSMM ${ \boldsymbol { \lambda } } ^ { * } = ( \pi , A , B , D )$ for this restaurant through recursive computing. Fig. 8 displays a convergence map of the parameters' re-estimation in HSMM-RMS. It indicates that an appropriate HSMM model is constructed within approximately 25 iterations. By using the modified forward-backward algorithm (see Appendix B), this restaurant's most likely reputation state sequence ${ Q } ^ { * }$ from March 3, 2011 to October 6, 2012 is found (see Fig. 9). What should be mentioned is that the state sequence ${ { Q } ^ { * } }$ and the “optimal” HSMM $\lambda ^ { * }$ will be continuously updated once new observable reputation-related information of this restaurant is added to our model.

## 5.3. Results and discussions

It can be seen from Fig. 9 that during the time surveyed, this restaurant's reputation state is at a relatively high level at first and then fluctuates between 1-star and 2-star levels and sometimes reaches 3-star and 4-star levels. Finally, it remains at the 4-star level.

![](/api/attachments/Y7WGAWK6/fulltext/images/72de4152853226c3a3a6f4153e32a729426b43bc09377abfbd3530e337ed6bfd.jpg)  
Fig. 9. Estimated hidden reputation state sequence.

According to the state duration distribution in the optimal HSMM $\lambda ^ { * }$ we know the probability that this restaurant will remain in the final reputation state for d days $( d = 1 , 2 , . . . , 3 0 )$ . Hence, we can compute the expected time that it will spend in the final reputation state

(the state at the end of the observation period) through $E ( t ) =$

$\sum _ { d = 1 } ^ { 3 0 } ( \overline { { p _ { 4 } ( d ) } } d ) = 3 . 6 8$ . That is, this restaurant will remain at the 4-star

level for approximately 3.68 days.

It should be noted that the time scale of this predictive information mainly depends on the time scale of the input, and it would be smaller if the latter is measured by a smaller time scale. Furthermore, we also conduct a comparison between HMM-RMS and HSMM-RMS in the case study, and it highlights the robustness of our results in Fig. 9. To save space and simplify this case study, the detailed results of the model comparison are not displayed.

The information provided by our system/model is useful for different participants of Dianping. Consumers can easily find restaurants' historical reputation behaviors. Furthermore, they can also choose proper restaurants and suitable consumption time by combining the predictive reputation information of the restaurants with their future consumption information. Because information contained in ${ Q } ^ { * }$ and $\lambda ^ { * }$ reflects the restaurants' reputation behaviors, they can let restaurant owners know how they are treated by the consumers. As a result, they can take appropriate actions to improve their image in the market. With the help of our system/model, reputation information managers on Dianping can also provide more accurate reputation evaluation results to the participants to improve its competitiveness.

## 6. Conclusions

In this study, a HSMM-based reputation management system (HSMM-RMS) has been established to improve reputation management in the emerging O2O e-commerce setting. By combining raw reputation-related information from both online and offline channels, the proposed system can automatically and dynamically evaluate offline merchants' reputation states. Moreover, it is able to provide O2O participants with offline merchants' historical and predictive reputation information to help them make consumption decisions. Different Monte-Carlo simulation scenarios in the virtual O2O market are conducted to evaluate the performance of the proposed model. The results indicate that our model performs better than the HMM-based reputation management model. A case study on a real O2O platform demonstrates how the proposed system/ model can be used in our daily lives.

Offline merchants and online consumers are two important parties in O2O e-commerce. We have analyzed the reputation management problems of offline merchants in this study. In future research, we will consider how to manage the reputation of consumers in this emerging e-commerce market.

## Acknowledgments

This work was supported in part by the Specialized Research Fund for the Doctoral Program of Higher Education of China (20120073110029), Interdiscipline Foundation of Shanghai Jiao Tong University (No. 11JCZ02), National Natural Science Foundation of China (No. 71371123, 71131005), and Europe-China High Value Engineering Network (EC-HVEN Project Number: 295130). The authors express their deepest gratitude to anonymous referees for their detailed comments and suggestions for this research. The presentation of the paper has significantly improved as a result of their inputs.

## Appendix A. Notations used in the HSMM-based reputation management model

N total number of hidden reputation states of an offline merchant.

π = {π } initial distribution of an offline merchant's reputation states.

A = {a<sub>ij</sub>} probability that an offline merchant jumps from reputation q<sub>i</sub> to $q _ { j } .$

$B = \{ b _ { i } ( V _ { a } ^ { b } ) \}$ probability that a merchant stays in reputation $q _ { i }$ from time a to b and emits an observable reputation-related data sequence $V _ { a \cdot } ^ { b }$

$D = \{ p _ { i } ( d ) \}$ probability that an offline merchant remains in q for d time units.

$D _ { i }$ maximum duration time of reputation state $q _ { i \cdot }$

$s _ { t } , V _ { t }$ offline merchant's hidden reputation state and observation at time t.

$Q = q _ { 1 } , q _ { 2 } , \cdots , q _ { t }$ offline merchant's real reputation state sequence from time 1 to t.

$V _ { 1 } ^ { t }$ offline merchant's observation sequence from time 1 to t.

$\nu _ { i 1 } ^ { t }$ offline merchant's observable data item sequence i (data item i in D4) from time 1 to t.

$W$ total number of data items in D4 that can reflect at least one aspect of an offline merchant's reputation.

$o _ { i j t }$ value of data item i at time t when a merchant is in state $q _ { j } .$

$\alpha _ { t } ( i )$ a forward variable that denotes the probability that an offline merchant generates ${ V _ { 1 } } ^ { t }$ and ends in $q _ { i }$ over the past t time units.

$\beta _ { t } ( i )$ a backward variable that denotes the probability that a merchant generates observation $V _ { t { \mathrm { ~ + ~ } } 1 } { } ^ { T }$ and begins with q at time t.

$\alpha _ { t , t } \cdot ( i , j )$ probability that an offline merchant has a reputation state $q _ { i }$ at time t and $q _ { j }$ at time t′ and generates observation sequence $V _ { 1 \cdot } ^ { t ^ { \prime } }$

$\phi _ { t , t } \cdot ( i , j )$ average probability that a merchant remains in reputation state $q _ { i }$ for d time units and then moves to state $q _ { j } .$

$\xi _ { t , t } \cdot ( i , j )$ conditional probability that a merchant stays in reputation state $q _ { i }$ for d time units and then moves to state $q _ { j } ,$ , given $V _ { 1 } { } ^ { T } .$

$\overline { { a _ { i j } } } , \overline { { b _ { i } ( 0 _ { k } ) } } , \overline { { \pi _ { i } } } , \overline { { p _ { i } ( d ) } }$ re-estimated parameters of $( \pi , \ A , \ B , \ D )$ in HSMM.

## Appendix B. The modified forward-backward algorithm

Algorithm $\mathrm { F } { - } \mathrm { B } _ { \mathrm { N e w } } \left( \pi , \boldsymbol { A } , \boldsymbol { B } , \boldsymbol { D } , \boldsymbol { V } \right) \left\{ \begin{array} { r l } \end{array} \right.$

Input: Parameters of the "optimal" HSMM $\lambda ^ { * } = ( \pi , A , B , D )$ obtained in Section 3.2 and preprocessed reputation-related observation V over the period surveyed.

Output: The most likely reputation state sequence O for the given observation (V)

Forward pass: {

If (t=0 and i=initialstate)

$$
\alpha_ {i} (i) = 1;
$$

Else $\begin{array} { r } { \alpha _ { 0 } ( i ) = 0 ; } \end{array}$

For $( t = 1 : T , \ 1 \leq i , j \leq N$ and 1 ≤ d ≤ Di)

$$
\left\{ \begin{array}{l} \phi_ {t, t ^ {\prime}} (i, j) = \sum_ {d = 1} ^ {D _ {i}} [ P (d = t ^ {\prime} - t \mid i) \cdot P (V _ {t + 1} ^ {t ^ {\prime}} \mid s _ {t} = i, s _ {t ^ {\prime}} = j, \lambda) ]; \end{array} \right.
$$

$$
\alpha_ {t, t ^ {\prime}} (i, j) = \alpha_ {t} (i) a _ {i j} \phi_ {t, t ^ {\prime}} (i, j)
$$

$$
\alpha_ {t ^ {\prime}} (j) = \sum_ {i = 1} ^ {N} \sum_ {d - 1} ^ {D _ {i}} P (d = t ^ {\prime} - t \mid j) \alpha_ {t, t ^ {\prime}} (i, j)
$$

Backward pass: {

$$
\beta_ {T} (i) = 1;
$$

For (t = 1: T , 1 ≤ i, j ≤ N and 1 ≤ d ≤ Di)

$$
\left\{\beta_ {t} (i) = P \left(V _ {t + 1} ^ {T} \mid s _ {t ]} = i, \lambda\right) = \sum_ {j = 1} ^ {N} \sum_ {d = 1} ^ {\min \left(D _ {t}, t\right)} a _ {i j} P _ {j} (d) b _ {j} \left(V _ {t + 1} ^ {t + d}\right) \beta_ {t + d} (j); \right.
$$

$$
\xi_ {t, t ^ {\prime}} (i, j) = \frac {\sum_ {d = 1} ^ {D _ {t}} \alpha_ {t} (i) a _ {i j} \phi_ {t , t ^ {\prime}} (i , j) \beta_ {t ^ {\prime}} (j)}{\beta_ {0} (i = \text { initialstate })};
$$

Q =optimal\_states\_finding $( \alpha _ { t } ( i ) , \phi _ { t , t ^ { \prime } } ( i , j ) , \alpha _ { t , t ^ { \prime } } ( i , j ) , \beta _ { T } ( i ) , \xi _ { t , t ^ { \prime } } ( i , j ) ) ;$

Return Q.

## References

[11 JiMedia Research. An analysis of the development of O2O e-commerce market between 2011 and 2015 in ChinaAvailable at http://www.jimedia.cn/29120.html May 21.2012

[2] S. Ruohomaa, L. Kutvonen, Trust management survey, Trust Management 3477 (2005) 77–92.

[3] Y. Wang, J. Vassileva, Toward trust and reputation based web service selection: a survey, International Transactions on Systems Science and Applications 3 (2) (2007) 118–132.

[4] S.C. Rice, Reputation and uncertainty in online markets: an experimental study, Information Systems Research 23 (2) (2012) 436–452.

[5] J. Sabater, C. Sierra, Review on computational trust and reputation models, Artificial Intelligence Review 24 (1) (2005) 33–60.

[6] A. Jøsang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online service provision, Decision Support Systems 43 (2) (2007) 618–644.

[7] M. Zhou, M. Dresner, R.J. Windle, Online reputation systems: design and strategic practices, Decision Support Systems 44 (4) (2008) 785–797.

[8] J.k. Golbeck, D. Ramachandran, Computing with social trust, in: M. wan (Ed.), Trust and Online Reputation Systems, Springer, London 2009, pp. 287–311.

[9] K.C. Lee, I. Kang, D.H. McKnight, Transfer from offline trust to key online perceptions: an empirical study, IEEE Transactions on Engineering Management 54 (4) (2007) 729–741.

[10] P.M. Doney, J.P. Cannon, An examination of the nature of trust in buyer–seller relationships The Journal of Marketing 61 (2) (1997) 35–51

[11] K.J. Stewart, Trust transfer on the world wide web, Organization Science 14 (1) (2003) 5-17

[12] W.D. Haseman, D.L. Nazareth, Proceedings of the 5th Americas Conf. Inform. Systems, Milwaukee, USA, 1999.

[13] S. Ba, P. Pavlou, Evidence of the effect of trust building technology in electronic markets: price premiums and buyer behavior, MIS Quarterly 26 (3) (2002) 243–268.

[14] E. Marchiori, L. Cantoni, The online reputation construct: does it matter for the tourism domain? A literature review on destinations' online reputation Information Technology & Tourism 13 (3) (2011) 139–159.

[15] A.R. Reuber, E. Fischer, Signalling reputation in international online markets, Strategic Entrepreneurship Journal 3 (4) (2009) 369–386.

[16] P.A. Pavlou, M. Fygenson, Understanding and predicting electronic commerce adoption: an extension of the theory of planned behavior, MIS Quarterly 30 (1) (2006) 115–143.

[17] J. Zhang, Trust-building on the Internet: Evidence from eBay, Proceedings of Pacific Asia Conference on Information Systems, Shanghai, China, 2004.

[18] A. Hortacsu, Trust and Reputation on Ebay: Micro and Macro Perspectives, Technical report, Department of Economics, UC Berkeley, 2005.

[19] A.M. Cannon, A. Reinhart, The value of a reputation: evidence from Amazon.com, Technical report, Department of Economics, Pomona College, Claremont, 2005.

[20] M. Sharif, S. Norouzi, Sentiment-based model for reputation systems in amazonReport, Available at http://cs229.stanford.edu/proj2011/SharifNorouzi-Sentiment BasedModelForReputationSystemsInAmazon.pdf.

[21] S. Wei, A pilot study on the Chinese internet environment, Education and Management 201 (2011) 617 621.

[22] H. Wang, Review of studies on online consumer trust, Proceedings of the Second International Conference on Computational Intelligence and Natural Computing (CINC), Wuhan, China, 2010.

[23] J.A. Audun, I.B. Roslan, B.A. Colin, Abstract a survey of trust and reputation systems for online service provision, Decision Support Systems 43 (2) (2006) 618–644.

[24] L. Mui, M. Mohtashemi, A. Halberstadt, A computational model of trust and reputation, Proceedings of the 35th Annual Hawaii International Conference (HICSS), Hawaii, USA, 2002.

[25] L. Liu, M. Munro, Systematic analysis of centralized online reputation systems, Decision Support Systems 52 (2) (2012) 438–449.

[26] A. Josang, Trust-based decision making for electronic transactions, in: L. Yngström, T. Svensson (Eds.), Proceedings of the 4th Nordic Workshop on Secure Computer Systems (NORDSEC'99), Stockholm University, Sweden, 1999.

[27] A. Jøsang, A logic for uncertain probabilities. International Journal of Uncertainty, Fuzziness and, Knowledge-Based Systems 9 (03) (2001) 279–311.

[28] B. Yu, M.P. Singh, An evidential model of distributed reputation management, Proceedings of the first international joint conference on Autonomous agents and multiagent systems, Bologna, Italy, 2002.

[29] R. Falcone, C. Castelfranchi, A belief-based model of trust, in: M.L. Huotari, M. Iivonen (Eds.), Trust in Knowledge Management and Systems in Organizations, Idea Group Publishing 2004 pp. 306–343

[30] C.K.Y. Tan, A belief augmented frame computational trust model, Proceedings of The Florida Artificial Intelligence Research Society Conference, Clearwater Beach, Florida, USA, 2005.

[31] J. Hu, Q. Wu, B. Zhou, Rbtrust: a recommendation belief based distributed trust management model for p2p networks, Proceedings of the 10th IEEE International Conference on High Performance Computing and Communications, Dalian, China, 2008.

[32] W. Bamberger, J. Schlittenlacher, K. Diepold, A trust model for intervehicular communication based on belief theory, Proceedings of IEEE International Conference on Social Computing, Minneapolis, Minnesota, USA, 2010.

[33] A. Jsang, R. Ismail, The beta reputation system, Proceedings of the 15th Bled Conference on Electronic Commerce, Bled Slovenia 2002

[34] M. Nielsen, K. Krukow, V. Sassone, A Bavesian model for event-based trustFestschrift for in: Gordon D. Plotkin (Ed.), Electronic Notes in Theoretical Computer Science, Elsevier, Amsterdam 2007, pp. 499–521

[35] V. Sassone, K. Krukow, M. Nielsen, Towards a formal framework for computational trust, Proceedings of the 5th Int. Symposium on Formal Methods for Components and Objects, Lecture Notes in Computer ScienceSpringer, Berlin, Germany, 2007.

[36] K. Krukow, M. Nielsen, V. Sassone, Trust models in ubiquitous computing, Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 366 (1881) (2008) 3781–3793.

[37] E. ElSalamouny, K.T. Krukow, V. Sassone, An analysis of the exponential decay principle in probabilistic trust models, Theoretical Computer Science 410 (41) (2009) 4067–4084.

[38] S. Buchegger, J.Y. Le Boudec, A robust reputation system for PP and Mobile Ad-hoc networks, Proc. of the 2nd Workshop on the Economics of Peer-to-Peer Systems. Boston, USA, 2004.

[39] V. Cahill, et al., Using trust for secure collaboration in uncertain environments, Pervasive Computing 2 (3) (2003) 52–61.

[40] L.R. Rabiner, A tutorial on hidden Markov models and selected applications in speech recognition, Proceedings of IEEE International Conference, 1989.

[41] W. Song, V.V. Phoha, X. Xu, The HMM-based model for evaluating recommender's reputation, Proceedings of the IEEE International Conference on E-Commerce Technology for Dynamic E-Business (CEC-East'04), Taipei, Taiwan, 2004.

[42] E. ElSalamouny, V. Sassone, M. Nielsen, HMM-based trust model, in: J.D. Guttman (Ed.), Formal Aspects in Security and Trust, Springer, Heidelberg 2010.pp.21-35.

[43] M. Moe, B. Helvik, S. Knapskog, Comparison of the beta and the hidden Markoy models of trust in dynamic environments in: Elena Ferrari Ninghui Li, et al., (Eds.), Trust Management III, Springer, Boston 2009, pp. 283–297.

[44] M. Dong, Y. Peng, Equipment PHM using non-stationary segmental hidden semi-Markov model, Robotics and Computer-Integrated Manufacturing 27 (3) (2011) 581–590.

[45] S.Z. Yu, Hidden semi-Markov models, Artificial Intelligence 174 (2) (2010) 215–243.

[46] M. Dong, D. He, Hidden semi-Markov model-based methodology for multi-sensor equipment health diagnosis and prognosis, European Journal of Operational Research 178 (3) (2007) 858–878.

[47] A.P. Dempster, N.M. Laird, D.B. Rubin, Maximum likelihood from incomplete data via the EM algorithm, Journal of the Royal Statistical Society: Series B: Methodological (1977) 1–38.

Shengsheng Xiao is Ph.D. candidate in Antai College of Economics & Management Shanghai Jiao Tong University. He received his Master degree in Management Information Systems from Shanghai University of Finance and Economics. His research deals with trust issues in social networks, and economics of user generated content.

Ming Dong is Professor in the Department of Operations Management, Antai College of Economics & Management, Shanghai Jiao Tong University. He received the M.S. and Ph.D. degrees from Tianjin University, Tianjin, China, respectively, all in mechanical engineering, and the Ph.D. degree in industrial engineering from Virginia Polytechnic Institute and State University. His research and teaching interests are in the areas of decision support, operations management and production optimization
