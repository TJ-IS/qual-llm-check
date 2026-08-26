---
otero_id: 13394
otero_key: "K29XF9XJ"
title: "Short-term prediction models for server management in Internet-based contexts"
authors: "Sara Casolari; Michele Colajanni"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.07.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Short-term prediction models for server management in Internet-based contexts

Sara Casolari, Michele Colajanni ⁎

Department of Information Engineering, University of Modena and Reggio Emilia, Italy

a r t i c l e i n f o

Article history: Received 27 April 2008 Received in revised form 17 July 2009 Accepted 29 July 2009 Available online 9 August 2009

Keywords: Runtime decision algorithm Prediction mode Internet server system Stochastic model

## a b s t r a c t

Modern Internet applications run on top of complex system infrastructures where several runtime management algorithms have to guarantee high performance, scalability and availability. This paper aims to offer a support to runtime algorithms that must take decisions on the basis of historical and predicted load conditions of the internal system resources. We propose a new class of moving filtering techniques and of adaptive prediction models that are speci<sup>fi</sup>cally designed to deal with runtime and short-term forecast of time series which originate from monitors of system resources of Internet-based servers. A large set of experiments con<sup>fi</sup>rm that the proposed models improve the prediction accuracy with respect to existing algorithms and they show stable results for different workload scenarios.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

Runtime algorithms that have to manage complex Internet-based infrastructures need adequate supports to their decisions. The common tendency of denoting the statistical properties of the external workload reaching Internet-based systems (e.g., heavy-tailed distributions [3,4,9], burst arrivals [19], hot spots [5]) does not help the algorithms to deal with the complexity and mostly unknown statistics of the system internals. Indeed, the models that are oriented to evaluate system performance through a prevalent external traf<sup>fi</sup>c view are useless to estimate and to anticipate a precise state of an internal resource. Consequently, adequate runtime decisions require the possibility of capturing the state of modern Internet applications in terms of internal system scenarios consisting of numerous I/O streams, timing information, and interactive concurrent tasks that enter and leave the system in a way that is dif<sup>fi</sup>cult to predict.

Predicting the behavior of the system resources from the internal is an original view that is necessary for supporting runtime management, such as taking decisions according to some objective rules for event detection, for triggering actions concerning data/ service placement, for anticipating resource overload. These problems occur frequently in Internet applications that are typically supported by clusters of hundreds or thousands of servers. These contexts require novel runtime models that are able to capture signi<sup>fi</sup>cant information about the past and present internal state and to predict the future state of the system resources. In this paper, we give a mathematical support to the internal system view approach and propose some prediction models that can predict at runtime the future state of the system resources in a short-term horizon which is suf<sup>fi</sup>cient to take better management decisions in terms of load balancing, load sharing, admission control, and job dispatching. We analyze the (un)predictability of some typical performance indexes deriving from the server monitors of a multi-tier Web-based system and we con<sup>fi</sup>rm that the resource measures referring to Internetbased servers are extremely variable, non-stationary [11], and tend to become obsolete quickly. In these contexts existing predictive models are not satisfactory and a new class of prediction algorithms is necessary. An important result of the statistical analysis is that raw measures of the system resources are characterized by a high frequency component (noise) that perturbs the measures and contributes to their unpredictability. The proposed algorithms <sup>fi</sup>rst reduce the noise component through a runtime smoothing process that is based on Discrete Fourier Transform functions. This smoothing process acts as a runtime moving <sup>fi</sup>lter that evidences a low frequency component. As the filtered data exhibit some short-term dependency, we have the possibility of predicting the state of the internal resources in terms of <sup>fi</sup>ltered performance indexes. Even in a context of <sup>fi</sup>ltered data, popular predictive models (e.g., Auto-Regressive, ARIMA, Exponential Weighted Moving Average, Linear Regression), when adopted at runtime in extremely variable scenarios, show a limited precision or an excessive delay with respect to a short-term horizon. Hence as a second contribution, we propose an adaptive prediction algorithm that at runtime takes into account the non-stationary effects of the data set, the time series trend and the runtime constraints. Experiments on a large set of realistic data show that the proposed prediction models are able to forecast on-the-<sup>fl</sup>y the future resource state of the Internet-based servers by improving the accuracy of the existing models. The rest of the paper is organized as follows. Section 2 presents related work and compares main contributions of this paper against the state of the art. Section 3 analyzes the statistical characteristics of the information coming from the monitors of the internal system resources and evidences the necessity of <sup>fi</sup>ltering the raw data sets. Section 4 proposes a runtime moving <sup>fi</sup>lter models that can be utilized to “clean” the raw data set at runtime. Section 5 outlines four prediction models that may be used in the context of Internet-based systems. Section 6 presents the new class of adaptive models that are proposed as runtime predictors in scenarios characterized by high variability. Section 7 reports the results of the considered prediction models for different workload scenarios. Section 8 concludes the paper with some <sup>fi</sup>nal remarks.

## 2. Related work

There are several external and internal system factors which make the problem of supporting runtime management decisions in Internet-based contexts interesting, dif<sup>fi</sup>cult and not deeply investigated. While external workload factors are well known, internal system factors have received less attention. The complexity of the middleware and applications for the support of Internet applications is continuously increasing, but no adequate characterization of the internal behavior of these systems has been presented yet. In other parallel and distributed applications [1,5,10], the resource measures are valid sources to decide about where the system is, where the system is going, whether it is necessary to activate some management process. While a measure offers an instantaneous view of the load conditions of a resource, in Internet-based contexts, it is of little help for distinguishing overload conditions from transient peaks, for understanding load trends and for anticipating future conditions.

Although predictive algorithms play a crucial role in managing Internet-based services, the large majority of prediction algorithms is based on off-line analyses that utilize measures collected from access logs or resource usage monitors [5,12,22]. For example, genetic algorithms, Support Vector Machines [13], wavelet analysis [26], and Fuzzy systems, neural network [29] may achieve a valid prediction quality after a medium–long learning time in rather stable contexts but they cannot be applied to runtime decisions [15] in extremely variable contexts characterizing Internet-based systems. Indeed, most time series forecasting models are intrinsically designed for off-line applications and medium–long-term predictions because in the considered context they would require to update their parameters every time there is a signi<sup>fi</sup>cant change in the statistical properties of the time series. One key requirement of this paper is that the regression analysis and the prediction models must be executed with limited computational overhead which is of utmost importance for achieving prediction in a short-term horizon. The models of our interest may lack the learning capabilities and the accuracy of the offline models, but in the considered context it is mandatory to achieve good (not necessarily optimal) predictions quickly, rather than looking for the optimal decision in an unpredictable amount of time. Some runtime prediction models for Internet-based systems can be inspired to models in other <sup>fi</sup>elds. This is the case of Auto-Regressive (AR, ARMA, ARIMA) and other linear models that are popular in economics. Some previous works on short-term prediction make strong assumptions on the mathematical characteristics of the workload, thus simplifying the prediction problem with respect to the conditions characterizing Internet-based systems. For example, the authors in [23] present a feedback control prediction mechanism that works well for mildly oscillating or stationary workloads. In [30] the authors explore the bene<sup>fi</sup>ts of the integration of non-linear corrective factors in a linear regression to predict FTP transfer times. In [16], a predictability study of a low variable resource such as the CPU load average is presented through different autoregressive models. The authors in [28] compute precise lower and upper bounds for the prediction interval and error of network traf<sup>fi</sup>c, which is assumed to be a Gaussian process. All these solutions do not hold for the workloads and resources behavior characterizing the considered

Internet-based systems that exhibit speci<sup>fi</sup>c statistical properties, such as heavy-tailed distributions [3,9], burst arrivals [19], hot spots [5], high variability [2], non-stationarity [11] and non-determinism. Our paper differs from most previous work because it considers realistic workloads, and when you move from ideal to realistic workload conditions, almost all the considered prediction models exhibit high precision errors. The proposed dynamic prediction algorithm works <sup>fi</sup>nely even in the typical conditions of real workload scenarios.

Although the external factors contribute to the internal complexity, the focus of this paper is on capturing the internal system behavior, managing it, and using it for accurate short-term predictions at runtime. Other results oriented to the short-term prediction in the presence of non-stationary workloads [18,20,23] consider external factors, which are turned into a measure of the future internal system load. On the other hand, we apply prediction models to a representation of the data set referring to the state of the internal resources of Internet-based servers. Prediction of Web load demands to internal system resources is a novel <sup>fi</sup>eld. Paci<sup>fi</sup>ci et al. [25] apply <sup>fi</sup>ltering techniques to predict the CPU demand of Web applications. In [2] that inspired this research on an internal system view, the same authors discuss the effects of a typical Web workload on the system resources and propose different representations of the internal resource load and their applications to several management algorithms. This paper explores the statistical foundations of that intuition, proposes more ef<sup>fi</sup>cient runtime moving <sup>fi</sup>lters, and focuses on the predictability problem in Internet-based systems. In this context, we propose a new class of adaptive prediction models which take into account the non-stationary effects of the data set and the load trend evaluation of the time series. The proposed algorithms achieve valuable results in Internet-based contexts, still satisfying runtime computational constraints.

## 3. Statistical analysis

Management and coordination of Internet-based servers are usually carried out through several algorithms that take on-the-<sup>fl</sup>y decisions on the basis of continuous information related to the state of the internal system components. These management algorithms could largely benefit of evaluations and short-term predictions about the state of internal resources. Unfortunately, it is very dif<sup>fi</sup>cult to model the complexity of internal server interactions without penalizing some realistic features because of two main causes [2]: the typical Internet workload shows unstable patterns, heavy-tailed distributions and <sup>fl</sup>ash crowds; there are unclear (from a modeling point of view) relationships among the external arrivals and the internal software/hardware components that are characterized by object-oriented distributed software, concurrent accesses to application and database servers, authentication, virtual servers, and unpredictable mutual dependencies. The literature is oriented to the analysis of the external workload models and their statistical properties (e.g., [5,19]), but it tends not to deal with the complexity and mostly unknown statistics of the system internals, even because most architectures and solutions are proprietary [18,25] and the academic community has no or limited access to fundamental information. As an example for our statistical analysis, we consider a popular Web-based system referring to a multi-tier logical architecture (Fig. 1) that is based on the implementation presented in [7]: the front-end node executes the HTTP server, the application server is deployed through the Tomcat servlet container, and the back-end node runs a MySQL database server. We generate the client requests through a set of emulated browsers, where each browser is implemented as a Java thread reproducing an entire user session with the Web site. The client requests follow the TPC-W workload model, a popular industrial benchmarking that is commonly utilized for evaluating the performance of dynamic Web-based systems (e.g., [7,8]). The WAN effects are emulated through the netem emulator. For statistical purposes, it is important to re-create in a controlled environment the entire client/server interactions, where all the external and internal request <sup>fl</sup>ows are logged through system monitors. Thanks to this testbed, we are able to know the exact periods during which the number of requests is stable, when they change, and which are the changing patterns. We captured data referring to all internal and external resources for experiments lasting for hours. For space reasons, we focus on two representative measures of the state of the system resources: CPU utilization and disk throughput. The statistical behavior of these internal resources is representative of different Internet-based servers we have analyzed when they are subject to realistic workloads.

![](/api/attachments/K29XF9XJ/fulltext/images/9e773db850e3ca07a54e035c211037726ccb9d8bfff2dfcac7647a28d9fe6446.jpg)  
Fig. 1. Experimental testbed for statistical analyses.

Data reaching the collector from the system monitors represent the historical basis for prediction models. Each historical information referring to one resource can be considered as a time series D, that is, an ordered collection of n data. Speci<sup>fi</sup>cally, for each resource, we have a time series $D = \{ d _ { 0 } , . . . , d _ { n - 1 } \} ,$ , where the elements are time ordered and correspond to the value given by the monitors at that instant. For example, if we consider that a system monitor captures one second of CPU utilization every 5 s during an observation interval of 10 min, then the raw data set corresponds to $D = \{ d _ { 0 } , . . . , d _ { 1 1 9 } \}$ . An important premise is that no prediction model can work if the analyzed time series does not exhibit some predictability factors. The raw data set has to show some temporal dependency, otherwise any prediction is unfeasible. The auto-correlation analysis on the time series allows us to show the presence of time dependence and to distinguish between the possibility of achieving long-term or just short-term prediction. A highly variable and noisy data set showing a so-called jittery behavior does not prevent predictability, but the accuracy of the prediction may be very low if it is referred to a future time that is inadequate to the statistic characteristics of the raw data set. We de<sup>fi</sup>ne prediction window k the number of predicted steps ahead. The accuracy of the prediction algorithms with respect to a certain prediction window is strictly dependent on the auto-correlation functions (inverse Fourier transforms) of the power spectra of the historical data set, that is,

$$
A C F (s) = \frac {1}{(n - 1 - s) \sigma^ {2}} \sum_ {i = 0} ^ {n - s} [ d _ {i} - \mu ] [ d _ {i + s} - \mu ]\tag{1}
$$

where $d _ { i }$ and $d _ { i + s }$ are the values at the lags i and $i + s , \mu$ is the mean value and $\sigma ^ { 2 }$ the variance of the data set. It is important to recall that a raw data set is considered predictable with an adequate accuracy for a prediction window k, if its auto-correlation function $| A C F ( k ) | \geq 0 . 3 \ [ 6 ]$ Unfortunately, the auto-correlation functions of the raw data set coming from the system monitors of the considered servers decay rapidly. As an example, in Fig. 2 we report the results of the autocorrelation analysis of raw data sets referring to three system resources (CPU utilization, network and disk throughput) of the application and database servers of the multi-tier Web system shown in Fig. 1 and subject to the Stable workload scenario described in Section 7. A point $\left( s , A C F _ { s } \right)$ denotes that the correlation between the i-th and the (i+s)-th load values is equal to $A C F _ { s } .$ . A high value of the auto-correlation function suggests that the i-th value may be used to predict the measure $d _ { i + s }$ with some degree of accuracy. The vice versa is true when the ACF between two points tends to zero. It is worth to point out that the results that are shown in Fig. 2 (very far from the threshold 0.3 as soon as the lag k is higher than 3) are representative of a very large set of data related to the internal system resources that we do not report for space limitation. The message from Fig. 2 and all other not reported results are quite clear: independently of the considered resource and type of server, the auto-correlation functions of the raw data sets decay steeply and the maximum prediction window $k _ { \mathrm { m a x } }$ is lower than 5.

a  
![](/api/attachments/K29XF9XJ/fulltext/images/027aaacf4bcf1b89ccd3920d1a8c48c5633126d2cd4cf05981a54986c08a11ec.jpg)

b  
![](/api/attachments/K29XF9XJ/fulltext/images/f5438a1d7daf5079503e244fe27be5c4352e997c513d93d1d1e2b12b60ddb9ea.jpg)  
Fig. 2. Auto-correlation functions of the raw data set (original data set).

A data set characterized by a quickly decay of the ACF values may be subject to white noise perturbation [17], hence it is important to verify the validity of this deduction. To this purpose, we evaluate the spectral analysis of the raw datasets of the most important internal resources of an Internet-based system. In Fig. 3 we show, as a representative example, the noise values that are obtained by the spectral analysis of the data values referring to the CPU utilization of the database server. As the noise that perturbs the signal is uniformly distributed in the entire frequency domain, it can be de<sup>fi</sup>ned as a white noise. Every signal that presents white noise shows an uncorrelated behavior among the data set values and any prediction is inaccurate even in a short-term period [17]. On the other hand, the presence of a white noise in the raw data sets is a positive result, because there is a large literature on <sup>fi</sup>lters that can eliminate noise from signals. A runtime <sup>fi</sup>lter that is adequate to the considered scenarios is presented in the next section. The expectation is that the <sup>fi</sup>ltered data set can augment the predictability with respect to raw observed measures.

## 4. Moving <sup>fi</sup>lter models operating at runtime

Various <sup>fi</sup>lters that can work at runtime are based on moving average models (e.g., EWMA [14,21]). Unfortunately, they are inadequate to facilitate short-time predictions in an Internet-based context because they tend to introduce an excessive representation delay when the size of the raw data set is large, while they do not eliminate all noises when the data set is small. The issue of the choice of the best data set size can be addressed when the data values are characterized by some stability, but this is not the case for the considered scenarios. Hence, we represent the system resource behavior at runtime through a new moving filter that is based on the Discrete Fourier Transform function (DFT) [24]. The Discrete Fourier Transform applied at step j to the n values of the raw data set $D _ { j } { = } \{ d _ { j - ( n - 1 ) } { , } . . . , d _ { j } \}$ is a sequence of complex numbers $D F T _ { j } ( w / n )$

$$
D F T _ {j} (w / n) = \frac {1}{\sqrt {n}} \sum_ {z = 0} ^ {n - 1} d _ {j - (n - 1)} + z e ^ {\frac {- i 2 \pi z w}{n}} \quad w = 0, \dots , n - 1.\tag{2}
$$

where e is the base of the natural logarithm, i is the imaginary unit and w/n denotes the frequency associated to each coef<sup>fi</sup>cient. The Discrete Fourier Transform allows us to represent the values of the raw data set as a linear combination of the complex sinusoids $s _ { w / n } ( z ) = \frac { e ^ { - \tilde { \imath } 2 \pi z w / n } } { \sqrt { n } }$ . By passing from the frequency domain back to the time domain, we can obtain every value of the raw data set through the inverse Fourier transform:

$$
d _ {j - (n - 1) + z} = \frac {1}{\sqrt {z}} \sum_ {w = 0} ^ {n - 1} D F T _ {j} (w / n) e ^ {\frac {i 2 \pi z w}{n}} \quad z = 0, \dots , n - 1.\tag{3}
$$

We can de-noise the raw data set by reducing the number of the n Fourier coef<sup>fi</sup>cients that are used in the representation. In particular, we are interested in a DFT <sup>fi</sup>lter that excludes from the inverse Fourier transform the coef<sup>fi</sup>cients corresponding to the high frequency components of the raw data set $D _ { j } .$ The DFT-based moving <sup>fi</sup>lter value $f _ { j }$ is de<sup>fi</sup>ned, at step j, as the sum of a subset W of the n Fourier coef<sup>fi</sup>cients $( 0 \leq W \leq n - 1 )$ :

$$
f _ {j} = \frac {1}{\sqrt {n - 1}} \sum_ {w = 0} ^ {W} D F T _ {j} (w / n) e ^ {\frac {i 2 \pi (n - 1) w}{n}}\tag{4}
$$

Each application of the DFT moving <sup>fi</sup>lter generates a novel value f<sub>j</sub>. At step j, the set of the <sup>fi</sup>ltered values that are generated by j applications of the DFT moving <sup>fi</sup>lter is denoted by $F _ { j } = \{ f _ { 1 } , . . . . , f _ { j } \} _ { }$

A DFT moving <sup>fi</sup>lter is computationally more expensive than a moving average <sup>fi</sup>lter though it has the advantage of being more reactive to changes especially when the raw data set is highly variable. In these conditions, the moving average <sup>fi</sup>lters tend to introduce a delay proportional to the size n of the raw data set [6], while the DFT is less dependent on this choice. No demonstration exists in literature but experience shows that the DFT needs a number n of values that is suf<sup>fi</sup>ciently representative (lower bound for n), compatible with runtime constraints (upper bound for $n ) ,$ , and typically chosen as a power of two [24]. The DFT algorithm is $\mathsf { a } O ( n ^ { 2 } )$ algorithm [6] and the computational cost for computing a new <sup>fi</sup>ltered value goes up rapidly as the number of points n grows (for example, for $\stackrel { - } { n } = 2 ^ { 9 } .$ , the DFT requires more than one million of multiplications [27]), hence we can consider that a value of $n < 2 ^ { 9 }$ is compatible with runtime constraints. The lower bound choice depends on the statistical characteristics of the data set. Typically, when the noise component that perturbs the data set is high, it is necessary to choose a higher value to obtain a representative <sup>fi</sup>ltered representation. For example, in our scenarios a choice of $n = 2 ^ { 6 }$ guarantees an adequate data representation.

An important parameter of the DFT-based moving <sup>fi</sup>lter is the choice of the number W of the Fourier coef<sup>fi</sup>cients considered in the representation. To this purpose, we recall that the <sup>fi</sup>lter is used to improve the predictability of the raw data set that is scarcely predictable, as shown in Section 3. Lower values of W correspond to a higher predictability of the <sup>fi</sup>ltered data set, but they imply a too much smoothed data representation that would be unable to capture some signi<sup>fi</sup>cant changes in the raw data set behavior. On the other hand, very high values of W would cause a lower predictability because the data representation would be too similar to the (not predictable) raw data set. The best compromise between a realistic representation and predictability is to choose W as the maximum value guaranteeing that the <sup>fi</sup>ltered data set is predictable on the interval de<sup>fi</sup>ned by the maximum prediction window $k _ { \mathrm { m a x } }$ of interest for the context to which the prediction should be applied. A <sup>fi</sup>ltered data set is predictable $k _ { \mathrm { m a x } }$ steps ahead if its auto-correlation function $| A C F ( k _ { \operatorname* { m a x } } ) | \geq 0 . 3$ [6]. Hence, we compute the ACF function of the <sup>fi</sup>ltered data sets F for different values of $W { > } 1 ,$ , and we choose the DFT moving <sup>fi</sup>lter corresponding to the maximum W that still satis<sup>fi</sup>es the condition $A C F ( k _ { \operatorname* { m a x } } ) { \geq } 0 . 3$

dB  
![](/api/attachments/K29XF9XJ/fulltext/images/40c15d5e5e107ed5a2f8a1784b4d3b4bc913da71ee4136863df74ac076a00f75.jpg)  
Fig. 3. Noise analysis of the internal resource measures.

For example, let us consider that we are interested to predict $k _ { \operatorname* { m a x } } = 2 0$ steps ahead a raw data set referring to the CPU utilization of a database server in a multi-tier Web system. By computing the ACF function of the data set representations generated by the DFT <sup>fi</sup>lter for different values of $W > 1$ and for $n = 2 ^ { 6 }$ , we have noticed that the $A C F ( k _ { \operatorname* { m a x } } = 2 0 )$ values decrease as W increases. The most suitable <sup>fi</sup>ltered representation is given by the DFT moving <sup>fi</sup>lter for $W { = } 6 ,$ , that is the maximum value for which the <sup>fi</sup>ltered set F satis<sup>fi</sup>es the condition $A C F ( k _ { \operatorname* { m a x } } = 2 0 ) > 0 . 3$ . We have applied this methodology to choose the parameters of the DFT moving <sup>fi</sup>lter for the CPU utilization, disk throughput and network throughput of the application server and database server of systems subject to different workload scenarios. Table 1 reports the ACF values of the raw data set and of the selected DFT moving <sup>fi</sup>lter representation for $n = 2 ^ { 6 }$ and for different k values, from 10 steps ahead to the maximum prediction window $k _ { \operatorname* { m a x } } = 2 0$ that determines the choice of the parameter W. This table con<sup>fi</sup>rms the expectation that ACF decreases for higher values of the prediction window k. However, for any system resource, a different parameterization of the DFT moving <sup>fi</sup>lter is able to guarantee the predictability of the <sup>fi</sup>ltered data set even when the raw data set is quite unpredictable (see the very low values of the ACF of the raw data sets compared to the corresponding ACF of the <sup>fi</sup>ltered data sets). As an example, Fig. 4 offers a qualitative evidence of the capability of the DFT moving <sup>fi</sup>lter to reduce the noise components of the raw data set at runtime. It compares the raw data set values, that is. the raw measures of the CPU utilization of the database server referring to Realistic scenario 1 (small dots spread in the entire picture) with their representation (line) obtained by the runtime DFT moving <sup>fi</sup>lter for $W { = } 6 .$ We should consider that this <sup>fi</sup>gure is representative of other workload scenarios and resource indexes that are typical of Internet-based systems.

## 5. Prediction models

The considered prediction models work at runtime on the set of <sup>fi</sup>ltered information. In particular, at step j we consider $F _ { j } ^ { ( r ) } =$ $\{ f _ { j - ( r - 1 ) } , \ldots , f _ { j } \}$ that is the subset of the last r values of the entire set of <sup>fi</sup>ltered data $F _ { j } .$ We propose to choose r equal to the maximum prediction window $k _ { \mathrm { m a x } }$ because $A C F ( i ) < 0 . 3$ for $i > k _ { \mathrm { m a x } } .$ . This means that after $k _ { \mathrm { m a x } }$ values the time dependency between the past <sup>fi</sup>ltered data set is low and additional past values do not add information useful to prediction purposes.

![](/api/attachments/K29XF9XJ/fulltext/images/aecb2bf1a368fb3c8fefbef213db5fbdf04244a01721684a733776bd62e4732e.jpg)  
Fig. 4. Raw data vs. DTF-based moving <sup>fi</sup>lter.

A predicted value at step j is the output of a function conditioned on $F _ { j } ^ { ( \bar { r } ) } \hat { f } _ { j + k } { = } g ( F _ { j } ^ { ( r ) } ) + \epsilon _ { j }$ in which $g ( \ u )$ is the function capturing the predictable component of the <sup>fi</sup>ltered data set, $\epsilon _ { j }$ models the possible noise, and k denotes the number of steps in the future that is, the socalled prediction window. There is a plethora of prediction models that aim to time series forecasting, but the choice of the most appropriate model depends on the context characteristics. As our focus is on runtime and short-term prediction, we are interested to achieve a high prediction accuracy through an algorithm characterized by low computational complexity. The accuracy is related to the precision in modeling the future data set in a hypothetic stable condition, but also to the capacity of the model of adapting its prediction to load variations when conditions are unstable. The rationale behind these attributes is that we want an accurate prediction, but we are also interested in the execution time to obtain it. We consider four popular classes of linear prediction models that can be applied to runtime contexts.

## 5.1. Exponential weighted moving average (EWMA)

This model predicts the future value k steps ahead as a weighted average of the last data value $f _ { j }$ and of the previously predicted value ${ \hat { f } } _ { j } \colon$

$$
\hat {f} _ {j + k} = \gamma \hat {f} _ {j} + (1 - \gamma) f _ {j}\tag{5}
$$

where $\gamma$ is typically set to $2 / ( r + 1 )$ , and r is the size of the <sup>fi</sup>ltered data set. The EWMA models are simple linear algorithms that are characterized by a very low prediction cost. Their accuracy depends on the data set characteristics. In stable conditions, they exhibit a good prediction quality even because it is possible to improve their accuracy through an adequate choice of the parameters γ and r. When the data set is unstable, the prediction quality decreases as well. Besides the accuracy problem, another main issue is that the EWMA models introduce a smoothing factor that is proportional to the size of the considered data set [21]. The smoothing factor of the EWMA model reduces its reactivity and introduces a delay in following the variations of the data set behavior. This problem may reduce the ef<sup>fi</sup>cacy of the EWMA application to the considered runtime context.

Auto-correlation values of raw and filtered data

<table><tr><td colspan="4">Application server</td><td colspan="4">Database server</td></tr><tr><td></td><td>k=10</td><td>k=15</td><td> $k_{\text{max}} = 20$ </td><td></td><td>k=10</td><td>k=15</td><td> $k_{\text{max}} = 20$ </td></tr><tr><td colspan="8">CPU utilization</td></tr><tr><td>Raw data set</td><td>0.01</td><td>0.006</td><td>0.003</td><td>Raw data set</td><td>0.02</td><td>-0.02</td><td>0.02</td></tr><tr><td>DFT moving filter (W=7)</td><td>0.69</td><td>0.46</td><td>0.33</td><td>DFT moving filter (W=6)</td><td>0.60</td><td>0.45</td><td>0.33</td></tr><tr><td colspan="8">Disk throughput</td></tr><tr><td>Raw data set</td><td>0.05</td><td>0.04</td><td>0.02</td><td>Raw data set</td><td>0.001</td><td>0.01</td><td>0.01</td></tr><tr><td>DFT moving filter (W=7)</td><td>0.70</td><td>0.46</td><td>0.35</td><td>DFT moving filter (W=4)</td><td>0.61</td><td>0.47</td><td>0.32</td></tr><tr><td colspan="8">Network throughput</td></tr><tr><td>Raw data set</td><td>0.07</td><td>0.0006</td><td>0.05</td><td>Raw data set</td><td>0.03</td><td>0.04</td><td>0.01</td></tr><tr><td>DFT moving filter (W=6)</td><td>0.56</td><td>0.45</td><td>0.31</td><td>DFT moving filter (W=5)</td><td>0.61</td><td>0.44</td><td>0.31</td></tr></table>

## 5.2. Auto-regressive (AR)

A k step ahead prediction through an AR model is a weighted linear combination of $p$ values represented by the $k - 1$ predicted values $\hat { f } _ { j + k - 1 } , . . . , \hat { f } _ { j + 1 }$ in the previous k−1 steps, and by the $p - k$ values of the <sup>fi</sup>ltered data set $( f _ { j } , . . . , f _ { j } - ( p - k ) )$ . These values are weighted by p linear coef<sup>fi</sup>cients $\varphi _ { 1 } , . . . , \varphi _ { p }$ that are the <sup>fi</sup>rst p values of the auto-correlation function evaluated on $F _ { \boldsymbol { j } } ^ { ( r ) }$ . The $p$ order of the AR process is de<sup>fi</sup>ned by a statistical test based on the partial autocorrelation function that is described in [6,21]. Higher order autoregressive models include more lagged f terms, where the coef<sup>fi</sup>cients are computed on a temporal window of r values. The last element of the AR model is the component $\epsilon _ { j }$ that is obtained as a function of the residual sequence (see [6] for additional details). Hence, an AR-based predictor at step j can be written as:

$$
\hat {f} _ {j + k} = \varphi_ {1} \hat {f} _ {j + (k - 1)} + \ldots + \varphi_ {p} f _ {j - (p - k)} + \epsilon_ {j}\tag{6}
$$

When the data set is stable, the AR models represent an appreciable solution to the trade-off between prediction cost and prediction quality [16], however the AR accuracy risks are low in the considered highly variable scenario.

## 5.3. Auto-regressive integrated moving average (ARIMA)

A k step ahead prediction through an ARIMA model is obtained by differentiating a d number of times the non-stationary sequence of the <sup>fi</sup>ltered values in $F _ { j } ^ { ( r ) }$ and by <sup>fi</sup>tting an Auto-Regressive Moving Average model (ARMA) that is composed by the auto-regressive model (AR) described in Eq. (6) with a moving average model (MA). The moving average part is a linear combination of the past $( q - k )$ noise terms, $e _ { j } , . . . e _ { j - q - k }$ weighted by the linear coef<sup>fi</sup>cient $\vartheta _ { 1 } , . . . , \vartheta _ { q - k }$ [6,21]. Hence, an ARIMA model is characterized by three parameters where p is the number of the considered data set values; q−k is the number of the residuals values; d is the number of the differentiating values. An ARIMA model for a k step ahead prediction can be written as:

$$
\begin{array}{r} \hat {f} _ {j + k} = \varphi_ {0} + \varphi_ {1} \hat {f} _ {j + (k - 1)} + \ldots + \varphi_ {p + d} f _ {j - p - d + k} + \\ + \vartheta_ {1} e _ {j} + \ldots + \vartheta_ {q - k} e _ {j - (q - k)} \end{array}\tag{7}
$$

The ARIMA prediction model requires a careful choice of the model parameters, that is typically based on the evaluation of the autocorrelation and partial auto-correlation functions [6]. In this paper, we consider two model parameter choices that originate two versions of the algorithm. The static-ARIMA version is based on the evaluation of the initial 10% values of the data set of the entire experiment. We expect that an ARIMA-based load predictor that cannot change continuously its parameters has some dif<sup>fi</sup>culties to predict accurate values when the data set is extremely variable. Hence, we consider the dynamic-ARIMA version that requires a continuous update of their parameters for every prediction of a new value $\hat { f } _ { j + k }$

## 5.4. Linear regression (LR)

Among the several linear regression models proposed in literature, we consider Baryshnikov et al.'s model [5], that is applied to the <sup>fi</sup>ltered data set $\bar { F } _ { j } ^ { ( r ) }$ . A prediction at step j of a value k steps ahead is equal to:

$$
\hat {f} _ {j + k} = \alpha_ {j} k + \beta_ {j}\tag{8}
$$

where the coef<sup>fi</sup>cients $\alpha _ { j }$ and $\beta _ { j }$ are dynamically chosen so to minimize the mean quadratic deviation $\begin{array} { r } { \dot { \sum _ { z } } ^ { j } = j - ( r - 1 ) ^ { \top } { [ \hat { f } _ { z } - f _ { z } ] ^ { 2 } } } \end{array}$ among the <sup>fi</sup>ltered data set $F _ { j } ^ { ( r ) }$ and the predicted data set ${ \hat { F } } _ { j } .$ They are equal to:

$$
\alpha_ {j} = \frac {\sum_ {z = j - (r - 1)} ^ {j} (f _ {z} - E [ F _ {j} ^ {(r)} ]) (\hat {f} _ {z} - E [ \hat {F} _ {j} ])}{\sum_ {z = j - (r - 1)} ^ {j} (f _ {z} - E [ F _ {j} ^ {(r)} ]) ^ {2}}; \quad \beta_ {j} = E [ \hat {F} _ {j} ] - \alpha_ {j} E [ F _ {j} ^ {(r)} ]\tag{9}
$$

where $E \big [ F _ { j } ^ { ( r ) } \big ]$ and $E [ \hat { F _ { j } } ]$ are the mean of the <sup>fi</sup>ltered data set values and of the predicted data set values, respectively. The simplicity of the LR model guarantees a low prediction cost. Its prediction quality is good when the data set is stable or is subject to long-term variations. On the other hand, when the data set is characterized by short-term variations, the LR model tends to overestimate the changes of the data set values with a consequent low prediction quality. We observe that these wrong predictions are a consequence of the fact that the LR model predicts the new value without considering any information about the data trend. The absence of this information limits the LR accuracy in the considered contexts that are characterized by continuous changes of data behavior.

## 6. Adaptive prediction model

The data sets deriving from the server resources, although <sup>fi</sup>ltered, are characterized by non-stationary effects. In this context, the considered prediction models satisfy the computational constraints but they may be affected by some inaccuracy. In the speci<sup>fi</sup>c context of the internal resources of Internet-based systems and runtime prediction in a short-term horizon, we think it is necessary to propose a novel class of prediction algorithms that is able to limit the drawbacks of the existing models. An ideal prediction model should combine the simplicity of the LR model, the AR and ARIMA qualities of reproducing the stochastic pattern of the data set and the EWMA ability of smoothing some noise components. The fundamental idea is that a valid prediction algorithm should not just consider the data set values or the deviation between the predicted and real values (e.g., LR predictor), but it should also be able to estimate from the data set the load trend. The load trend gives additional information that can be utilized to evaluate whether a resource load is increasing, decreasing, oscillating or stabilizing. The proposed adaptive prediction model (AP) is based on the following steps.

![](/api/attachments/K29XF9XJ/fulltext/images/a7349529237e33e0f9b0e7f083e8790113219f3e0baafb0bf6d174dc014f0e9e.jpg)  
Fig. 5. AP operations: variation trend and degrees of variation for $m = 4$ past values.

The <sup>fi</sup>rst choice for the estimation of a future value of the time series concerns the past values that the prediction model wants to consider. At step $j ,$ the model selects a subset of m values of the <sup>fi</sup>ltered data set $F _ { j } ^ { \mathrm { ( r ) } }$ . These m values are sampled from $F _ { j } ^ { \mathrm { ( r ) } }$ through a constant frequency $q ,$ from $f _ { j }$ backward to $f _ { j - ( m _ { * } - 1 ) q } .$ (Here, we consider the more general instance of $q > 1$ and $q { \leq } \frac { ( r - 1 ) } { ( m - 1 ) } \big )$ . The goal is <sup>ð Þ</sup>to utilize this subset of past values to predict at step j the value of the point ${ \hat { f } } _ { j + k }$ which is positioned at k steps ahead. In fact, the proposed model does not utilize just the plain past values $f _ { j - z q } \left( 0 { \leq } z { \leq } m - 1 \right)$ but the degree $o f$ variation $a _ { i }$ between each couple of consecutive points $f _ { j - z q }$ and $f _ { j - ( z + 1 ) q }$ for 0≤z≤m−2. For example, the degree of variation $a _ { j - z q }$ is computed as:

![](/api/attachments/K29XF9XJ/fulltext/images/74f5c0b063b43679799ef55b1fae4485af9989f912c6732fdeb750a219b81ada.jpg)

b  
![](/api/attachments/K29XF9XJ/fulltext/images/5325cb6e56a341a607ef64d5fe31d2ead09f60e1fd3bbb35f93cd19043e4e2d0.jpg)

C  
![](/api/attachments/K29XF9XJ/fulltext/images/0e85f7c976fdcaf24468a9b612c881fbbad2f7dc217544fdd62149f62e67a4e3.jpg)  
Fig. 6. Workload models.

Table 2  
CPU time (ms) for the computation of a predicted value.

<table><tr><td></td><td>EWMA</td><td>LR</td><td>AP</td><td>AR</td><td>Static-ARIMA</td><td>Dynamic-ARIMA</td></tr><tr><td>Internal resource</td><td>0.059</td><td>3.785</td><td>0.072</td><td>6.42</td><td>72.141</td><td>168.14</td></tr><tr><td>Web cluster</td><td>38.2</td><td>1170</td><td>43.6</td><td>1971</td><td>21,661</td><td>49,870</td></tr></table>

$$
a _ {j - z q} = \frac {k f _ {j - z q} - f _ {j - (z + 1) q}}{q}; \quad 0 \leq z \leq m - 2\tag{10}
$$

where $\frac { k } { a }$ represents the scaling factor which must be introduced when the size of the future window k is different from the size of the past window $q .$ In these instances, the view of the Cartesian spaces at step j and at step $j + k$ differs, hence it is necessary to adapt the degree of variation computed in the Cartesian space at step j with the degree of variation that will be utilized in the space k steps ahead. The absolute value of the degree of variation $| a _ { j - z q } |$ represents the intensity of the variation between two consecutive points $f _ { j - z q }$ and $f _ { j - ( z + 1 ) q } .$ The sign of $a _ { j - z q }$ denotes the direction of the variation: a plus represents an increment of the value between the $f _ { j - z q }$ and $f _ { j - ( z + 1 ) q }$ data; a minus denotes a decrement of the trend. Fig. 5 offers a geometric representation of the AP model operations, when we consider $m = 4$ points denoting the three segments: $( f _ { j - 3 q } , f _ { j - 2 q } ) , ( f _ { j - 2 q } , f _ { j - q } )$ and $( f _ { j - q } , f _ { j } )$ . We associate a degree of variation to each segment, thus obtaining $a _ { j - 2 q } , a _ { j - q }$ and $a _ { j } .$

a  
![](/api/attachments/K29XF9XJ/fulltext/images/754d03652af85faa99744af53211591644ebc488177d1c5533a566850b1d4f82.jpg)

b  
![](/api/attachments/K29XF9XJ/fulltext/images/48a6a3de06315cfcf73930a301d5596bf300c91e7134f865a1aad5fed6d54dd6.jpg)  
Fig. 7. Prediction error as a function of the k steps ahead—(Stable scenario)

In order to predict the value $\hat { f } _ { j + k }$ we are interested to combine the degrees of variation in the most convenient way. We evaluate the socalled variation trend ${ \bar { a } } _ { j } ,$ shown in the rightmost part of Fig. 5, as the weighted linear regression of the m−1 degrees of variation:

$$
\overline {{a}} _ {j} = \sum_ {z = 0} ^ {m - 2} v _ {z} a _ {j - z q}\tag{11}
$$

where the best choice of the $\nu _ { z }$ coef<sup>fi</sup>cients opens another space of alternatives. We investigate two possible solutions for the choice of the weight distribution.

• A uniform distribution gives equal importance to each degree of variation.

• A geometric distribution assigns decreasing weights to the less recent degrees of variation that is, $\nu _ { z } = \rho ( 1 - \rho ) ^ { z }$ <sup>z</sup>, where $z { \in } ( 0 , . . . , m { - } 2 )$ and $0 { \le } \rho { \le } 1$ . This choice actually denotes a class of alternatives where we can give or not a major importance to the more recent trend coef<sup>fi</sup>cients by increasing the $\rho$ value. (In Section 7, we consider two choices for ρ.)

a  
![](/api/attachments/K29XF9XJ/fulltext/images/da7ece3094c27a92e25be8bf25e8117527226c7a9fc9d010a37a01981d740913.jpg)  
b

c  
![](/api/attachments/K29XF9XJ/fulltext/images/b65699546a1215da3ae26bd023a46f12ee8a3db4adbb80d46d42f4922864bbfc.jpg)  
Fig. 8. Qualitative comparison of four prediction models.  
d

We can conclude by observing that the AP model predicts the future value ${ \hat { f } } _ { j + k }$ through the following linear combination of values:

$$
\hat {f} _ {j + k} = \overline {{{a}}} _ {j} k + f _ {j}\tag{12}
$$

where $\bar { a } _ { j } \mathrm { i } s$ the variation trend, k is the prediction window and $f _ { j }$ is the <sup>fi</sup>ltered value at step j. In summary, the AP model is based on the following steps.

• In the set of <sup>fi</sup>ltered data $F _ { j } ^ { ( r ) }$ it is necessary to choose m points that have a relative distance equal to q.

• The m points denote m−1 segments. Each of them is characterized by a positive or negative degree of variation.

• The combination of the $m - 1$ degrees of variation originates from the so-called variation trend ā, that is used as the fundamental parameter to estimate the future point ${ \hat { f } } _ { j + k }$ situated k steps ahead.

The AP model has many qualities: it is a simple algorithm that satis<sup>fi</sup>es the computational constraints of the runtime prediction; it is adaptable to the time varying patterns of the data sets without the need of a continuous and costly re-evaluation of the model parameters; and it is able to reproduce the patterns of the data sets that allows it to be responsive even to the most severe load variations.

![](/api/attachments/K29XF9XJ/fulltext/images/d394781d407cbd5ec7db65e20b6a6aba6271a6a2ba02eddd92892a632496a90b.jpg)

![](/api/attachments/K29XF9XJ/fulltext/images/723c9d6ab56d40b86130ac9bf7fd844f8cf7b40f2f1c841c810df671a114deee.jpg)

## 7. Evaluation of the prediction models

## 7.1. Experimental testbed

We evaluated the prediction quality and the robustness of the AP model with respect to other linear prediction models for a wide range of workload models. In this section we consider the following three representative scenarios.

Stable scenario: it describes a TPC-W workload in the ideal case of a number of clients that does not change during the experiment. (The results refer to 120 emulated browsers.) Although the number of clients is <sup>fi</sup>xed, the number and type of requests reaching the system are subject to some variations because they follow the transition state diagram of the TPC-W model. Fig. 6(a) reports the typical behavior of the number of requests generated by a stable scenario.

Realistic scenario 1 and 2: they describe two realistic Web workloads where the number of emulated browsers changes during the experiments lasting for 8000 s. The pattern of the active clients follows the pro<sup>fi</sup>les presented in [5] and shown in Fig. 6(b) and (c), respectively. In these scenarios, the number and type of requests reaching the system are highly variable.

All scenarios are representative of the typical Web-based workload that is characterized by heavy-tailed distributions [3,9]. Moreover, the real scenarios add burst arrivals [19] that contribute to augment the request skew, and they represent a more stressful testbed for prediction models.

In the adaptive prediction (AP) model, when not otherwise speci<sup>fi</sup>ed, we set $m = 3$ and $q = 5 ,$ and we consider a uniform distribution. We consider also an AP model based on a geometric distribution of the weights with $\rho { = } 0 . 7 ,$ , that characterizes a quick decay of the v values $( \nu _ { 0 } = 0 . 7 , \nu _ { 1 } = 0 . 2 1 , \nu _ { 2 } = 0 . 0 6 3 )$ and on a more smoothed geometric distribution with $\rho { = } 0 . 4$ that brings to a linear decrease of the v values $( \nu _ { 0 } = 0 . 4 , \nu _ { 1 } = 0 . 2 4 , \nu _ { 2 } = 0 . 1 2 )$ .

## 7.2. Computational cost of the prediction models

We <sup>fi</sup>rst estimate the computational cost of the prediction models in order to assess their feasibility to runtime requirements. We evaluate the CPU time required by each predictor to estimate a new value for one system resource, and then we compute the total time that a typical cluster can require to predict the internal state of their servers. The total time estimated in the Web cluster is the sum of the CPU time required to compute the predicted values and the communication time required to collect the raw data sets from the Web cluster nodes. The results are evaluated on an average PC machine and are reported in Table 2. They refer to the scenario of Fig. 4, but their costs are representative of any workload. The <sup>fi</sup>rst line of Table 2 shows the computational cost for predicting one value of one system resource. If we have to predict just a few values, we can conclude that the computational cost of any of the considered prediction models is compatible to runtime constraints. However, we have to consider that these models are typically applied to complex clusters consisting of hundreds of servers, where the state of each server may require the observations of 6–7 internal resources. For example, in the second line of Table 2 we report the total computational time of the prediction models applied to a real multi-tier Web cluster composed by 50 servers. If we consider that the reported values does not include the system times that is necessary to compute the <sup>fi</sup>ltered representation, then we can conclude that: the application of the ARIMA models to runtime contexts is critical or impossible; LR and AR models can work only if the prediction interval is not too short; EWMA and AP models are always adequate to runtime predictions for online decisions.

## 7.3. Quality of the prediction models

In this section we compare the accuracy of the AP model with respect to the state of the art predictors: EWMA, LR, AR, static and dynamic ARIMA. There are several measures to evaluate the quality of a predictor. In this paper we consider the Normalized Mean Absolute Error (NMAE) between the data obtained by the DFT-based moving <sup>fi</sup>lter and the predicted data sets [31]. The NMAE calculates the mean prediction error, and then normalizes it by the mean of the data set obtained by the DFT-based moving <sup>fi</sup>lter:

$$
\frac{\sum_{j = 1}^{N}(\hat{f}_{j} - f_{j})^{2}}{N*\overline{f}} 100\%\tag{13}
$$

where N is the total number of predictions, $\hat { f } _ { j }$ is the predicted value, $f _ { j }$ is the DFT-based <sup>fi</sup>ltered data and f ̄is the mean of the DFT-based data set.

We initially evaluate the sensitivity of the prediction results to the temporal size of the prediction window k. As we are interested to short-term prediction, we focus on k∈[1,20] steps ahead. Fig. 7(a) and (b) reports the prediction results in an ideal stable scenario concerning CPU utilization and disk throughput, respectively.

In the ideal scenario, all prediction models are valid and share similar behavior with a NMAE value below or close to 5%. On the other hand, we will see that in the realistic scenarios the prediction errors of the models will differ signi<sup>fi</sup>cantly. Fig. 8 gives a qualitative view about the behavior of different predictor models in a realistic scenario. These <sup>fi</sup>gures report the <sup>fi</sup>ltered curve (bold line) and the predicted curves $k = 1 0$ steps ahead (dotted lines) for four prediction models: AP, EWMA, static and dynamic ARIMA. The graphs indicate that the AP model achieves the most accurate prediction because the two curves are really close. The prediction models, such as EWMA (Fig. 8(b)), that tend to smooth the data variability are affected by high delays in following the data curve. This is a consequence of the smoothing effects of the lower order prediction models that do not allow them to react quickly enough to the changes of the data set pattern. The static linear models, such as static ARIMA (Fig 8(c)), are affected by too large oscillations because they tend to amplify the load variation. When the variance of the time series varies over time, the consequence is an overestimation of the data values. On the contrary, the dynamic ARIMA that is able to capture the changing in the load characteristics exhibits an accurate prediction.

a  
![](/api/attachments/K29XF9XJ/fulltext/images/3d32a17ac5a299f4da28ec360e35312b726a9e95b99b4d8ae59d05725339d81c.jpg)  
b

![](/api/attachments/K29XF9XJ/fulltext/images/91b9606ea5702ac2711452e88283a9666fcc6e6b72a1d57e33d1b17c7802860a.jpg)  
Fig. 9. Prediction error as a function of the k steps ahead—(Realistic scenario 1).

The qualitative analysis is supported by a quantitative comparison. We consider the data sets coming from the CPU utilization and disk throughput of the DB servers for the scenarios Realistic 1 and 2. The histograms in Figs. 9 and 10 denote the prediction errors (NMAE) as a function of $k \in [ 1 , 2 0 ]$ for all the considered models. These results con<sup>fi</sup>rm that the AP model has the lowest error values for any resource and scenario. This important result is the consequence of the ability of the AP model to self-adapt its trend coef<sup>fi</sup>cient ā to the data set behavior. The prediction error of the other models is higher because either they are characterized by a static choice of the coef<sup>fi</sup>cients (e.g. EMA, AR and static-ARIMA) or, when the coef<sup>fi</sup>cients are dynamically chosen (e.g., dynamic ARIMA), they do not consider any information about the trend behavior of the data set. If we choose a threshold equal to 20% as a maximum acceptable error, we can conclude that AP always achieves adequate results, but in one really critical instance corresponding to the prediction of the disk throughput for k=20. On the other hand, most static-ARIMA results are unacceptable especially for the Realistic scenario 2 that is characterized by the most variable workload. Even the LR, EWMA and dynamic-ARIMA models are always characterized by a higher prediction error than that of the AP model. Independently of the characteristics of the data sets, other not reported results con<sup>fi</sup>rm that the AP model is the best model for the runtime prediction of the behavior of the internal system resources of Internet-based servers.

a  
![](/api/attachments/K29XF9XJ/fulltext/images/a1c42dd6b04c814fe1ad07f2a61651cf0548e7ecc54997b59cdea263f8bab85e.jpg)

b  
![](/api/attachments/K29XF9XJ/fulltext/images/f15e3d190527a781243408ee6334d54021baad4097f5997d4800b077d0db4700.jpg)  
Fig. 10. Prediction error as a function of the k steps ahead—(Realistic scenario 2).

In a dynamic context, it is important to measure the quality and robustness of the AP model by evaluating the sensitivity to its main parameters that is, the past values (m−1)q and the choice of the weights of the degrees of variation. For this analysis, as a representative example, we consider the data set related to the CPU utilization of the database server subject to the Realistic scenarios 1 and 2. We initially evaluate the prediction quality of the AP models for $( m - 1 ) q$ past values where the sampling frequency q ranges from 0 to 30, $m = 3$ , and the prediction window is set to $k = 1 0$ steps ahead. Figs. 11(a) and 12(a) show the prediction errors of three AP models that use different weights for the parameters of the degrees of variation. From these <sup>fi</sup>gures, we can appreciate that the prediction quality of any AP models is preserved for a wide range of past data values and different weights. This robustness is an important attribute of the proposed model especially if we consider the high variability of the considered contexts. We can also observe that the AP model characterized by a quick decay of the weights $( \rho { = } 0 . 7 )$ outperforms the other AP models.

a  
b  
![](/api/attachments/K29XF9XJ/fulltext/images/4da5eaa61a637e4793cc530fc171cfad506a6c3e69727745fd020180cc7556a0.jpg)

![](/api/attachments/K29XF9XJ/fulltext/images/a03ce86ebde30bd17c7ff08575ba166b2b95e6a6602d968044460905a18980da.jpg)  
Fig. 11. Prediction error of the AP models for different distributions of the weights— (Realistic scenario 1).

a  
![](/api/attachments/K29XF9XJ/fulltext/images/071f63b2d4822c28831653d93851de16be21f39d20cd5544ce2de1546c697b9d.jpg)

b  
![](/api/attachments/K29XF9XJ/fulltext/images/6c511ec24a65fe5651ca99772b31e4276e9956d5305e51e321298b6357941c85.jpg)  
Fig. 12. Prediction error of the AP models for different distributions of the weights— (Realistic scenario 2).

Figs. 11(b) and 12(b) show the prediction quality of different AP models as a function of the k steps in the future by considering $( m - 1 ) q$ past values, where $q = 5$ and $m = 3 .$ As expected, the prediction error augments proportionally to the distance of the prediction, but the AP results are similar only for very short-term predictions which are characterized by $k \leq 5 .$ On the other hand, when the k value augments, the prediction errors of the AP model based on a uniform distribution tend to 20%, while the error of the AP model based on the geometric distribution of the weights for $\rho { = } 0 . 7$ remains well below 10% even for $k = 2 0$ . If we compare the AP results against those of the existing model in its best version, that is dynamic ARIMA, we can appreciate that the AP model can halve the prediction errors especially when the prediction window tends to grow $( k \ge 2 0$ in the considered workload scenario). We can conclude that the AP models are extremely robust to the variations of their parameters. Moreover, in the most variable scenarios, a geometric choice of the weights gives the most accurate predictions.

## 8. Conclusions

The systems supporting Internet applications are expected to satisfy scalability, availability, and short-time servicing requirements even under critical workload conditions. These external characteristics together with the increasing complexity of the internal architectures make runtime management decisions really dif<sup>fi</sup>cult, because the decision algorithms cannot know or predict from simple monitor observations whether a system resource is of<sup>fl</sup>oading, stable or overloading. This paper represents a <sup>fi</sup>rst contribution in the direction of investigating and predicting the performance of the internal resources of Internet-based servers in a short-term horizon. We have evidenced that observed data sets do not allow any prediction, but an adequate runtime moving <sup>fi</sup>lter can reduce noises and exhibit data sets with a sort of short-term correlation. As existing prediction algorithms achieve unacceptable results even on <sup>fi</sup>ltered data sets, we propose a new class of adaptive prediction models showing the best precision for different scenarios and data sets, and stable results for a wide range of parameters. There are several possible exploitations of the proposed models because short-term prediction of the system resource behavior is the basis of most runtime management decisions, such as load sharing, admission control, hot spot control, and request redirection.

## References

[1] T. Abdelzaher, K.G. Shin, N. Bhatti, Performance guarantees for Web server endsystems: a control-theoretical approach, IEEE Transactions on Parallel and Distributed Systems 130 (1) (2002).

[2] M. Andreolini, S. Casolari, M. Colajanni, Models and framework for supporting runtime decisions in web-based systems, ACM Transactions on the Web 20 (3) (2008).

[3] M. Arlitt, D. Krishnamurthy, J. Rolia, Characterizing the scalability of a large webbased shopping system, IEEE Transactions on Internet Technology 10 (1) (Aug. 2001).

[4] P. Barford, M.E. Crovella, Generating representative Web workloads for network and server performance evaluation, Proc. of the Joint Int. Conf. on Measurement and Modeling of Computer Systems, Madison, WI, June 1998.

[5] Y. Baryshnikov, E. Coffman, G. Pierre, D. Rubenstein, M. Squillante, T. Yimwadsana, Predictability of Web server traf<sup>fi</sup>c congestion, Proc. of the 10th Workshop of Web Content Caching and Distribution, Sophia Antipolis, FR, Sep. 2005.

[6] P.J. Brockwell, R.A. Davis, Introduction to Time Series and Forecasting, Springer, 2001.

[7] H.W. Cain, R. Rajwar, M. Marden, M.H. Lipasti, An architectural evaluation of Java TPC-W, Proc. of the 7th Symp. on High Performance Computer Architecture, Monterrey, ME, Jan. 2001.

[8] E. Cecchet, A. Chanda, S. Elnikety, J. Marguerite, W. Zwaenepoel, Performance comparison of middleware architectures for generating dynamic Web content, Proc. of the 4th ACM/IFIP/USENIX Middleware Conf., Rio de Janeiro, BR, June 2003.

[9] J. Challenger, P. Dantzig, A. Iyengar, M. Squillante, L. Zhang, Ef<sup>fi</sup>ciently serving dynamic data at highly accessed Web sites, IEEE/ACM Transactions on Networking 120 (2) (Apr. 2004).

[10] X. Chen and J. Heidemann. Flash crowd mitigation via an adaptive admission control based on application-level measurement. Technical Report ISI-TR-557, USC/Information Sciences Institute, May 2002.

[11] S. Chen, H. Wang, S. Zhou, P. Yu, Stop chasing trends: discovering high order models in evolving data, Proc. of the 24th IEEE Int. Conf. on Data Engineering, 2008.

[12] B. Choi, J. Park, Z. Zhang, Adaptive random sampling for load change detection, Proc. of the 16th IEEE Int. Conf. on Communications, Anchorage, AL, USA, May 2003.

[13] C. Cortes, V. Vapnik, Support-vector networks, Machine Learning 200 (3) (1995)

[14] J. Cowie, F. Burstein, Quality of data model for supporting mobile decision making, Decision Support Systems 430 (4) (2007).

[15] L. Devroye, L. Gyor<sup>fi</sup>, G. Lugosi, A Probabilistic Theory of Pattern Recognition, Springer-Verlag, 1996.

[16] P. Dinda, D. O'Hallaron, Host load prediction using linear models, Cluster Computing 30 (4) (Dec. 2000).

[17] P.F. Dunn, Measurement and Data Analysis for Engineering and Science, McGraw Hill, New York, 2005.

[18] D. Gmach, J. Rolia, L. Cherkasova, A. Kemper, Capacity management and demand prediction for next generation data centers, Proc. of the 5th IEEE Int. Conf. on Web Services, Salt Lake City, UT, July 2007.

[19] J. Jung, B. Krishnamurthy, M. Rabinovich, Flash crowds and denial of service attacks: characterization and implications for CDNs and Web sites, Proc. of World Wide Web Conf Honolulu HW Mav 2002

[20] N. Kandasamy, S. Abdelwahed, J.P. Hayes, Self-optimization in computer systems via on-line control: application to power management, Proc. of the 1st Int. Conf. on Autonomic Computing, New York, NY, May 2004.

[21] M. Kendall, J. Ord, Time Series, Oxford University Press, 1990.

[22] Y. Lingyun, I. Foster, J.M. Schopf, Homeostatic and tendency-based CPU load predictions, Proc. of the 17th Parallel and distributed processing Symp., Nice, FR, 2003.

[23] Y. Lu, T. Abdelzaher, L. Chenyang, S. Lui, L. Xue, Feedback control with queueingtheoretic prediction for relative delay guarantees in Web servers, Proc. of the 9th IEEE real-time and embedded technology and Applications Symp., Charlottesville, VA Mav 2003

[24] A.V. Oppenheim, R.W. Schafer, J.R. Buck, Discrete-time signal processing, Prentice Hall 1999.

[25] G. Paci<sup>fi</sup>ci, W. Segmuller, M. Spreitzer, A. Tantawi, CPU demand for web serving: measurement analysis and dynamic estimation, Dec. 2007 Performance Evaluation.

[26] D.B. Percival, A.T. Walden, Wavelet Methods for Time Series Analysis, Cambridge University Press, 2000.

[27] J.A. Resendo Macias, A. Gomez Exposito, Ef<sup>fi</sup>cient moving-window DFT algorithms, IEEE Transactions on Circuits and Systems - II 450 (2) (1998).

[28] A. Sang, S. Li, A predictability analysis of network traf<sup>fi</sup>c, Proc. of 19th Annual Joint Conf. of the IEEE Computer and Communications Societies, Tel Aviv, Mar. 2000.

[29] J.T. Spooner, M. Maggiore, R. Ordonez, K.M. Passino, Stable Adaptive Control and Estimation for Nonlinear Systems: Neural and Fuzzy Approximator Techniques, John Wiley and Sons, 2002.

[30] S. Vazhkudai, J. Schopf, Predict sporadic grid data transfers, Proc. of the 11th IEEE Symp. on High Performance Distributed Computing, Edinburgh, GBR, Jul 2002.

[31] R. Vilalte, C.V. Apte, J.L. Hellerstei, S. Ma, S.M. Weiss, Predictive algorithms in the management of computer systems, Feb. 2003.

![](/api/attachments/K29XF9XJ/fulltext/images/2658e7886b57e90e7e01249c1658eb134b26de95e4f80707e05514f758dc22e2.jpg)

Sara Casolari is a researcher assistant at the Department of Information Engineering of the University of Modena and Reggio Emilia, Italy. She received her master's degree (summa cum laude) and the Ph.D. in Computer Engineer ing from the University of Modena and Reggio Emila in information engineering in 2004 and 2008, respectively. Her research interests include stochastic models and performance evaluation of distributed systems, and modeling algorithms for supporting autonomic systems. She received a best paper award at the International Conference on Autonomic and Autonomous Systems (ICAS 2007).

![](/api/attachments/K29XF9XJ/fulltext/images/3cb1ef2af622f03346d79b1d3832474d754f32382c25459a58a76947f2876d1d.jpg)

Michele Colajanni is a Full Professor of computer engineering at the Department of Information Engineering of the University of Modena. He was formerly an Associate Professor at the same University in the period 1998–2000 and a Researcher at the University of Roma Tor Vergata. He received a Laurea degree in computer science from the University of Pisa in 1987, and a Ph.D. degree in computer engineering from the University of Roma Tor Vergata in 1991. He is the Director of the Inter-department Research Center on Security (CRIS) from its foundation in 2007. He has held research appointments with the National Research Council (CNR), visiting scientist appointments with the IBM T.J. Watson Research Center, Yorktown Heights,

NY. In 1997 he was awarded by the National Research Council for the results of his research activities on high performance Web systems during his sabbatical year spent at the IBM Research Center. His research interests include infrastructures for Internetbased services, security, distributed systems, and performance analysis. In these <sup>fi</sup>elds he has published more than 130 papers in international journals, book chapters and conference proceedings. He has lectured in several national and international seminars and conferences. Michele Colajanni serves as a permanent reviewer of scienti<sup>fi</sup>c journals and international research projects. He has served as a member of numerous organizing or program committees of the most important conferences on his research topics, e.g. World Wide Web, ACM Sigmetrics, ACM/IFIP/Usenix Middleware, and IFIP Performance. He was the scientist responsible of the national and European projects on high performance Web-based systems and performance evaluation.
