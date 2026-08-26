---
otero_id: 13216
otero_key: "72KKQYXP"
title: "Extended Kalman Filter for wireless LAN based indoor positioning"
authors: "Jaegeol Yim; Chansik Park; Jaehun Joo; Seunghwan Jeong"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.03.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Extended Kalman Filter for wireless LAN based indoor positioning

Jaegeol Yim <sup>a</sup>, Chansik Park <sup>b</sup>, Jaehun Joo <sup>c,</sup>⁎, Seunghwan Jeong <sup>a</sup>

<sup>a</sup> Department of Computer and Multimedia, Dongguk University, 707 Sukjang-Dong, Gyeongju, Gyeongbuk, 780-714, South Korea

<sup>b</sup> School of Electrical and Computer Engineering, Chungbuk National University, 410 Sungbong-Ro, Heungduk-Gu, Cheongju, Chunbuk, 361-763, South Korea

<sup>c</sup> Department of Electronic Commerce, Dongguk University, 707 Sukjang-Dong, Gyeongju, Gyeongbuk, 780-714, South Korea

## a r t i c l e i n f o

Article history: Received 10 August 2007 Received in revised form 18 March 2008 Accepted 26 March 2008 Available online 3 April 2008

Keywords: Indoor positioning Extended Kalman Filter Wireless Local Area Network Fingerprinting method K-NN Bayesian method Decision tree Trilateration

## a b s t r a c t

A WLAN (Wireless Local Area Network) based Extended Kalman Filter (EKF) method for indoor positioning is introduced in this paper. WLAN based indoor positioning is more economical than other methods because it does not require any special equipment dedicated to positioning. The most popular technique used for indoor positioning is the <sup>fi</sup>ngerprinting method, but the EKF method is easier to deploy because, unlike <sup>fi</sup>ngerprinting, it does not require a time consuming off-line phase. This paper also provides experimental comparisons of our EKF method with other indoor positioning methods.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

The location based services (LBS) provided in the ubiquitous environment require the accurate positions of the users and, as a result, positioning techniques have become one of the most important elements in ubiquitous networks [7]. The Global Positioning System (GPS) is the most representative method of positioning and is widely used in practical outdoor LBS systems. However, GPS cannot be utilized indoors because the GPS signal cannot be received if line of sight visibility to the satellites is lost.

In order to make indoor LBS possible, many indoor positioning techniques have been developed recently. Active Badge [28], which involves positioning by sensing infrared signal, Active Bat [10] and Cricket [22], which involve positioning by using the difference between the propagation times of ultrasound and RF signals, and RADAR [3], which involves positioning by using the strength of the received UDP signal, are among the most representative indoor positioning systems. These systems are highly accurate, but they also have their own shortcomings. That is, they require special equipment dedicated to positioning.

Many indoor positioning systems which do not require special equipment have also been developed. Most of them use RF-based WLAN (wireless LAN) positioning techniques. Nowadays, WLAN is available in many places including in college campuses, airports, hotels and even homes. The indoor positioning system we introduce in this paper is also a kind of RF-based WLAN positioning system. An RF-based WLAN positioning system determines a user's position by referring to the received signal strengths (RSSs) of the signals from various access points (AP). The most popular method used to determine the user's position is the <sup>fi</sup>ngerprinting method [2,3,12–14,17,18,27,30,31]. In implementation of <sup>fi</sup>ngerprinting method, we can apply any classi<sup>fi</sup>cation or decision making techniques such as the ones shown in [1,21,24,25].

The deployment of <sup>fi</sup>ngerprinting based positioning systems consists of two phases. First, in the off-line phase, the location <sup>fi</sup>ngerprints are collected by performing a sitesurvey of the RSSs from multiple APs. The vector of the RSS values at a point is called the location <sup>fi</sup>ngerprint of that point. The second phase, the on-line phase, gathers the RSSs the user receives at the present moment and matches them with these <sup>fi</sup>ngerprints to determine the user's location.

It is known that the <sup>fi</sup>ngerprinting method is fairly accurate. However, it has a serious shortcoming. That is, the off-line phase is extremely time consuming. An alternative choice is the RF propagation loss model based method [9,16]. The RF propagation loss model is a simple mathematical expression representing the relationship between the RSS and the distance between the sender and the receiver. However, the RSS is in<sup>fl</sup>uenced by many parameters and establishing an appropriate RF propagation loss model is very dif<sup>fi</sup>cult. As a result, the RF propagation loss model based positioning method is less accurate than the <sup>fi</sup>ngerprinting positioning method. Nevertheless, we propose an RF propagation loss model based WLAN positioning method in order to avoid the time consuming off-line phase process.

A mobile terminal, in an RF-based WLAN positioning system, measures the strengths of the signals received from at least three different <sup>fi</sup>xed position stations. Then, by applying an RF propagation loss model to these signal strengths, the mobile terminal estimates its distances from the stations. By applying trilateration to the distances and the coordinates of the stations, the mobile terminal can estimate its position. The variance of the indoor positions estimated by trilateration is usually quite large, because of the noise in the RF signal. To obtain a more accurate position from noisy distance measurements, the terminal repeats the estimation process a number of times and determines its position to be the average of the estimations.

Trilateration is a kinematic method which does not consider the user dynamics, while the Kalman Filter [6,8,15,19] is applicable to a dynamic system. The Kalman Filter estimates the state of a process by iteratively predicting its state and adjusting the prediction with measurements. One of the characteristics of the Kalman Filter is that it minimizes the mean of the squared error. There are hundreds of papers on the Kalman Filter, most of which involve its application to autonomous or assisted navigation [4,5,20,26], whereas there have been few reports on its application to indoor positioning or navigation.

Kotanen et al. [15] and Qasem et al. [23] used the Kalman Filter for indoor positioning. However, they used special equipments such as Bluetooth antennas [15] or radar transponders [23]. On the other hand, our experimental environment is a WLAN. WLANs are installed in most buildings, nowadays, due to the prevalence of mobile computing. Therefore, our Kalman Filter method can be easily and economically applied in practical use.

## 2. Related works

This paper introduces a WLAN-based indoor positioning method using the Kalman Filter. Therefore, WLAN-based indoor positioning techniques are summarized in this section. They can be classi<sup>fi</sup>ed into <sup>fi</sup>ngerprinting methods or RF propagation loss model based methods.

An example look-up table of K-NN (CP are the coordinates of the i-th candidate points, and AP is the MAC address of the i-th AP)

<table><tr><td></td><td> $AP_1$ </td><td> $AP_2$ </td><td> $AP_3$ </td><td> $AP_4$ </td><td> $AP_5$ </td></tr><tr><td> $CP_1$ </td><td>-39</td><td>-55</td><td>-56</td><td>-70</td><td>-67</td></tr><tr><td> $CP_2$ </td><td>-40</td><td>-56</td><td>-55</td><td>-69</td><td>-66</td></tr><tr><td> $CP_3$ </td><td>-44</td><td>-42</td><td>-62</td><td>-45</td><td>-61</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

Example training data tuples (CP are the coordinates of the i-th candidate point, AP is the MAC address of the i-th AP, and I stands for interval)

<table><tr><td></td><td> $AP_1$ </td><td> $AP_2$ </td><td> $AP_3$ </td><td> $AP_4$ </td><td> $AP_5$ </td></tr><tr><td rowspan="3"> $CP_1$ </td><td> $I_2$ </td><td> $I_1$ </td><td> $I_2$ </td><td> $I_5$ </td><td> $I_5$ </td></tr><tr><td> $I_1$ </td><td> $I_1$ </td><td> $I_2$ </td><td> $I_1$ </td><td> $I_1$ </td></tr><tr><td>...</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"> $CP_2$ </td><td> $I_3$ </td><td> $I_2$ </td><td> $I_3$ </td><td> $I_1$ </td><td> $I_2$ </td></tr><tr><td>...</td><td></td><td></td><td></td><td></td></tr><tr><td>...</td><td>...</td><td></td><td></td><td></td><td></td></tr></table>

## 2.1. Fingerprinting methods

The K-NN (K Nearest Neighbors) [3], Bayesian [11,18] and decision tree [2,29] methods are representative techniques used in <sup>fi</sup>ngerprinting positioning and they are brie<sup>fl</sup>y summarized in this section.

## 2.1.1. K-nearest neighbor

In K-NN, we build a look-up table in the <sup>fi</sup>rst phase, or offline phase. The entire area is covered by a rectangular grid of points called candidate points. At each of these candidate points, we measure the RSSIs many times. Let $\mathsf { R S S I } _ { i j }$ denote the j-th received signal strength indicator of the signal sent by $\mathsf { A P } _ { i } , \mathrm { ~ A ~ }$ row of the look-up table is an ordered pair of (coordinate, a list of RSSIs). A coordinate is an ordered pair of integers (x, y) representing the coordinates of a candidate point. A list of RSSIs consists of <sup>fi</sup>ve integers, $\mathrm { R S S I } _ { 1 } , \mathrm { R S S I } _ { 2 }$ where RSSI is the average of $\mathsf { R S S I } _ { i j }$ received at $( x , y )$ and sent by $\mathbb { A P } _ { i } .$ . An example of a look-up table is shown in Table 1.

In the second phase, or on-line phase, the positioning program gathers the RSSIs the user receives at the current moment. If the positioning program is running on the user's handheld terminal, then the terminal itself will collect the RSSIs. For example, let $X = ( - 4 0 , - 5 6 , - 5 4 , - 6 9 , - 6 6 )$ be the vector of the collected RSSIs. K-NN, then examines the lookup table and <sup>fi</sup>nds the closest candidate point, $\mathrm { C P } _ { 2 }$ in the case of Table 1, and returns it as the user's current location. If K equals 2, then it will <sup>fi</sup>nd the two closest candidate points and return the average of their coordinates as the user's current location.

## 2.1.2. Bayesian classification method

Let $X { = } ( x _ { 1 } { , } x _ { 2 } { , } { \ldots } x _ { n } )$ be the vector of collected RSSIs. The positioning program will predict that the user's position is CP if $P ( \mathrm { C P } _ { i } | X ) { > } P ( \mathrm { C P } _ { j } | X )$ for $1 \leq j \leq m , j \neq i ,$ , where, m is the number of candidate points. According to Bayes' theorem, $P ( \mathrm { C P } _ { i } \mid X ) =$ ${ \frac { P ( X \mid \mathrm { C P } _ { i } ) P ( \mathrm { C P } _ { i } ) } { P ( X ) } } . \mathsf { A s } P ( X )$ is constant for all classes, only $P ( X | C \mathbb { P } _ { i } ) P ( \mathbf { C } \mathbb { P } _ { i } )$ need be maximized. A positioning system using the Bayesian classi<sup>fi</sup>cation method <sup>fi</sup>nds the $\mathrm { C P } _ { i }$ that maximizes $P ( X | \mathbf { C P } _ { i } )$ $P ( \mathbf { C P } _ { i } )$ , and returns it as the user's position [27].

## 2.1.3. Decision tree

In the off-line phase of the decision tree method [29], we build a decision tree with the training data. An example training data set is shown in Table 2. Table 2 is similar to

![](/api/attachments/72KKQYXP/fulltext/images/a670f090fd2648a05f7a2edf9975afcb347ce21e0b22acc3141a665d6585b5d3.jpg)  
Fig. 1. A diagram to illustrate trilateration.

Table 1. The only differences are 1) the RSSIs are not averages, 2) the RSSIs are discretized into classes. The number of classes for a given training data set can be decided by the following expression: $k { = } 1 + ( \log n ) / ( \log 2 )$ , where k is the number of classes and n is the number of measurements made at a candidate point. However, our experiments showed that $k = 5$ is appropriate. A class can be represented as an interval. An example discretizing policy can be $I _ { 1 } = \{ x | x > - 3 0 \}$ $I _ { 2 } = \{ x |$ $- 4 0 < x \leq - 3 0 \} , I _ { 3 } = \{ x | - 5 0 < x \leq - 4 0 \} ,$

Given a set of training data, the decision tree method constructs a decision tree as follows. We compute I, or the expected information needed to classify a given sample, with the following expression:

$$
I (s _ {1}, s _ {2},..., s _ {m}) = - \sum_ {i = 1} ^ {m} p _ {i} \log_ {2} (p _ {i}),
$$

where m is the number of candidate points, s is the number of tuples in the training data set (rows of Table), $s _ { i }$ is the number of rows of training data set in class $\mathrm { C P } _ { i } ,$ and $\begin{array} { r } { p _ { i } = s _ { i } / s . } \end{array}$

Then, we compute the entropy, or expected information based on the partitioning of the training data set into subsets by $\mathsf { A P } _ { k }$ . Let $\mathsf { A P } _ { k }$ have v distinct values, $\{ a _ { 1 } , a _ { 2 } , . . . , a _ { \nu } \} . \mathrm { A P } _ { k }$ can be used to partition S into v subsets, $\{ S _ { 1 } , S _ { 2 } , . . . , S _ { \nu } \}$ , where $S _ { j }$ contains those samples in S that have the value $a _ { j }$ of $\mathsf { A P } _ { k } .$ . Let $S _ { i j }$ be the number of samples of class $\mathrm { C P } _ { i }$ in a subset $S _ { j } .$ The entropy $E ( \mathsf { A P } _ { k } )$ is given by

$$
E \left(\mathrm{AP} _ {k}\right) = \sum_ {j = 1} ^ {v} \frac {s _ {i j} + \dots + s _ {m j}}{s} I \left(s _ {i j}, \dots , s _ {m j}\right).
$$

Finally, we compute the information gain $G ( \mathsf { A P } _ { k } )$ by the following expression,

$$
\operatorname{Gain} \left(\mathrm{AP} _ {k}\right) = I \left(s _ {1}, s _ {2}, \dots , s _ {m}\right) - E \left(\mathrm{CP} _ {i}\right).
$$

We then create a node for the decision tree and label it $\mathsf { A P } _ { k } ,$ where Gain $( \mathsf { A P } _ { k } ) \mathsf { z G a i n } ( \mathsf { A P } _ { i } )$ for 1≤i≤number of APs. For each $a _ { j }$ of $\mathsf { A P } _ { k } ,$ we build a reduced training data set and recursively repeat the above process to create child nodes until the training data set is empty or the CP values of all of the rows are the same.

## 2.2. Positioning with range from RF propagation loss model

Trilateration and the Extended Kalman Filter are representative positioning methods using the range obtained from the RF propagation loss model and they are brie<sup>fl</sup>y summarized in this section.

## 2.2.1. Trilateration

If we measure N ranges, $r _ { 1 } , r _ { 2 } , . . . , r _ { N }$ from N base stations, $n _ { 1 } = ( X _ { 1 } Y _ { 1 } Z _ { 1 } ) ^ { T } , . . . . , n _ { N } = ( X _ { N } Y _ { N } Z _ { N } ) ^ { \mathrm { I } }$ to a mobile terminal, $\scriptstyle { m = ( x y z ) } ^ { T }$ as shown in $\mathrm { F i g . }$ 1, then we can estimate the coordinates of m by using trilateration. By squaring, we can obtain the following expression for $r _ { i } ^ { 2 . }$

$$
(x - X _ {i}) ^ {2} + (y - Y _ {i}) ^ {2} + (z - Z _ {i}) ^ {2} = r _ {i} ^ {2}, (\text { for } i = 1, 2,..., N).
$$

By subtracting $r _ { i } ^ { 2 }$ from $r _ { i } ^ { 2 } ( i { = } 2 , . . . , N ) ,$ we have ${ \cal A } \stackrel { \longrightarrow } { x } = \stackrel { \longrightarrow } { b } ,$ where

$$
\begin{array}{l} A = 2 \left[ \begin{array}{c c c} (X _ {2} - X _ {1}) & (Y _ {2} - Y _ {1}) & (Z _ {2} - Z _ {1}) \\ \vdots & \vdots & \vdots \\ (X _ {N} - X _ {1}) & (Y _ {N} - Y _ {1}) & (Z _ {N} - Z _ {1}) \end{array} \right],   \overrightarrow {x} = \left[ \begin{array}{c} x \\ y \\ z \end{array} \right] \\ \overrightarrow {b} = \left[ \begin{array}{c} (X _ {2} ^ {2} - X _ {1} ^ {2}) + (Y _ {2} ^ {2} - Y _ {1} ^ {2}) + (Z _ {2} ^ {2} - Z _ {1} ^ {2}) - (r _ {2} ^ {2} - r _ {1} ^ {2}) \\ \vdots \\ (X _ {N} ^ {2} - X _ {1} ^ {2}) + (Y _ {N} ^ {2} - Y _ {1} ^ {2}) + (Z _ {N} ^ {2} - Z _ {1} ^ {2}) - (r _ {N} ^ {2} - r _ {1} ^ {2}) \end{array} \right]. \end{array}
$$

When the coordinates are 3 dimensional, we need to have at least 4 base stations. Applying the MMSE (Minimum Mean Square Error) method, we can estimate the location of m, $\hat { \overrightarrow { \bf x } } ,$ with the following position estimates:

$$
\hat {\vec {x}} = \left(A ^ {T} A\right) ^ {- 1} A ^ {T} \overrightarrow {b}\tag{1}
$$

## 2.2.2. Extended Kalman Filter

The Kalman Filter iteratively estimates the position of the mobile terminal and updates the estimate with new measurements. In the positioning process, the measurement equation is represented as a nonlinear model, and linearization should therefore be performed to derive a linear equation. The extended Kalman Filter (EKF) considers the real-time linearization of the system function at the previous state estimate and that of the observation function at the corresponding predicted position. The measured distances, $r _ { i }$ can be expressed as follows:

$$
r _ {i} = \sqrt {(X _ {i} - x) ^ {2} + (Y _ {i} - y) ^ {2} + (Z _ {i} - z) ^ {2}} + v _ {i}
$$

where $\nu _ { i }$ represents the measurement noise and is assumed to be white Gaussian noise (AWGN) with a normal probability distribution of mean 0 and variance $\sigma _ { i } ^ { 2 }$ . Using the Taylor approximation at a nominal point $\vec { x } _ { 0 } = \left( x _ { 0 } y _ { 0 } z _ { 0 } \right) ^ { T }$ we have:

$$
r _ {i} - r _ {i 0} = \frac {\partial r _ {i}}{\partial \vec {x}} \bigg | _ {\vec {x} = \vec {x} _ {0}} \delta \vec {x} + v _ {i} = h _ {x} ^ {i} \delta x + h _ {y} ^ {i} \delta y + h _ {z} ^ {i} \delta z + v _ {i}
$$

where $r _ { i 0 } = \sqrt { ( X _ { i } - x _ { 0 } ) ^ { 2 } + ( Y _ { i } - y _ { 0 } ) ^ { 2 } + ( Z _ { i } - z _ { 0 } ) ^ { 2 } }$ is the computed distance between the nominal point and the i-th base station, $\begin{array} { r } { \left( h _ { x } ^ { i } = \frac { x _ { 0 } - X _ { i } } { r _ { i 0 } } , h _ { y } ^ { i } = \frac { y _ { 0 } - Y _ { i } } { r _ { i 0 } } , h _ { z } ^ { i } = \frac { z _ { 0 } - Z _ { i } } { r _ { i 0 } } \right) } \end{array}$ is the LOS (Line Of Sight) vector from the base location to the i-th base station, and $\delta \vec { x } = ( \delta x \delta y \delta z )$ is the position error vector to be determined. For N base stations, we have the following expression:

$$
\left[ \begin{array}{c} r _ {1} - r _ {1 0} \\ \vdots \\ r _ {N} - r _ {N 0} \end{array} \right] = \left[ \begin{array}{c c c} h _ {x} ^ {1} & h _ {y} ^ {1} & h _ {z} ^ {1} \\ \vdots & \vdots & \vdots \\ h _ {x} ^ {N} & h _ {y} ^ {N} & h _ {z} ^ {N} \end{array} \right] \left[ \begin{array}{c} \delta x \\ \delta y \\ \delta z \end{array} \right] + \left[ \begin{array}{c} v _ {1} \\ \vdots \\ v _ {N} \end{array} \right].
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Linearized state model: $\vec{x}_{k+1} = \Phi_k\vec{x}_k + \vec{w}_k, \vec{w}_k \sim N(0, Q_k)$

Linearized measurement model: $\vec{r}_k = \vec{r}_0 + H_k\delta\vec{x}_k + \vec{v}_k, \vec{v}_k \sim N(0, R_k)$

1) Initial guess: $\vec{x}_0^- = E(\vec{x}_0)$ and $P_0^- = \text{var}(\vec{x}_0)$

2) Linearizing: $\vec{r}_k = \vec{r}_0 + H_k\delta\vec{x}_k + \vec{v}_k, \vec{r}_0 = \begin{bmatrix} \sqrt{(X_1 - x_k^-)^2 + (Y_1 - y_k^-)^2 + (Z_1 - z_k^-)^2} \\ \vdots \\ \sqrt{(X_N - x_k^-)^2 + (Y_N - y_k^-)^2 + (Z_N - z_k^-)^2} \end{bmatrix}$

3) Kalman Gain: $K_k = P_k^-H_k^T(H_kP_k^-H_k^T + R_k)^{-1}$

4) Measurement update: $\hat{\vec{x}}_k = \hat{\vec{x}}_k^-$ + $K_k(\vec{r}_k - \vec{r}_0)$

5) Update error covariance: $P_k = (I - K_kH_k)P_k^-$

6) State propagation: $\hat{\vec{x}}_{k+1}^- = \Phi_k\hat{\vec{x}}_k$, $P_{k+1}^- = \Phi_kP_k\Phi_k^T + Q_k$

7) Goto step2
</div>

Fig. 2. A summary of the EKF processing.

This equation can be rewritten in the following form, where the subscript k is the index for the discrete time sequence:

$$
\delta \vec {r} _ {k} = \vec {r} _ {k} - \vec {r} _ {0} = H _ {k} \delta \vec {x} _ {k} + \vec {v} _ {k}.
$$

The measurement noise is AWGN with $\vec { \nu } _ { k } { \sim } N ( 0 , R _ { k } ) , R _ { k } =$ $\mathrm { d i a g } \big ( \sigma _ { i } ^ { 2 } \big )$ <sup>e</sup>where diag stands for diagonal matrix. If we have more than 3 measured distances, we can estimate the position of the mobile terminal by using the WLSE (Weighted Least Squares Estimate). However, by adding system models to the above measurement models and applying the Kalman <sup>fi</sup>ltering process, a more reliable position can be found. The P (Position), PV (Position Velocity) and PVA (Position Velocity Acceleration) models are generally used in navigation as a system model. In this paper, we assumed a static user and, therefore, we use the P model described by the following expression:

$$
\vec {x} _ {k + 1} = \varPhi_ {k} \vec {x} _ {k} + \vec {w} _ {k}
$$

where $\phi _ { k }$ is the state transition matrix and the system error $\vec { w } _ { k } { \sim } N ( 0 , \ Q _ { k } )$ corresponds to the modeling error. Fig. 2 sum-<sup>e</sup>marizes the EKF processing. The estimate we can obtain with these expressions is the value of $\delta \hat { \vec { x } } _ { k } ,$ and the <sup>fi</sup>nal solution, i.e. the user's location, can be obtained with the following expression: $\hat { \vec { x } } _ { k } = \vec { x } _ { 0 } + \delta \hat { \vec { x } } _ { k } .$

Since we use the P model $\phi _ { k } = I ,$ and if we further assume that the mobile node is at a <sup>fi</sup>xed position and never moves, then $Q _ { k } = 0$ . Then we can replace step 6 in Fig. 2 by the following simpli<sup>fi</sup>ed expression:

$$
\hat {\vec {x}} _ {k + 1} ^ {-} = \hat {\vec {x}} _ {k}, P _ {k + 1} ^ {-} = P _ {k}
$$

## 3. Implementation

We implemented all of the methods introduced in Section 2 on a laptop equipped with an Intel(R) PRO/Wireless 2200BG

Network Connection LAN card. We used Microsoft Visual C# 2005 as our development tool.

## 3.1. Implementation of fingerprinting methods

The implementations of positioning systems based on the K-NN (K Nearest Neighbor), Bayesian and decision tree methods are discussed in this section.

## 3.1.1. Implementation of a K-NN positioning system

As mentioned in Section 2.1.1, the K-NN method <sup>fi</sup>nds the K nearest entries in the look-up table. An example look-up table is shown in Table 1. Our K-NN algorithm is shown in Fig. 3. The look-up table (MacLookupTable), an array of signal strengths from the APs gathered by the mobile terminal at the present moment $( X ) ,$ the size of the look-up table (tablesize) and the value of K (k) are the parameters of the algorithm. Line 4-1 of the algorithm computes the Manhattan distance from X to the i-th tuple of the look-up table for all i from 1 to the size of the table. Then line 4-2 of the algorithm inserts a pair of (the Manhattan distance, the line number) into SimilarityList in non-decreasing order of the Manhattan distance. When the algorithm is at line 6, the <sup>fi</sup>rst (k-th) node of SimilarityList corresponds to the <sup>fi</sup>rst (k-th) nearest candidate point to the mobile terminal. Therefore, line 6 of the algorithm adds up the k x-coordinates (y-coordinates) of the <sup>fi</sup>rst k nodes of SimilarityList in avg\_X (avg\_Y). avg\_X (Y) divided by k, in line 8 (9), is the average of the k nearest candidate points' X (Y) coordinates. Finally, the algorithm marks (avg\_X, avg\_Y) on the GUI (graphical user interface) as the mobile terminal's current position.

## 3.1.2. Implementation of a Bayesian positioning system

A positioning system using the Bayesian classi<sup>fi</sup>cation method <sup>fi</sup>nds the $\mathrm { C P } _ { i }$ that maximizes $P ( X | \mathsf { C P } _ { i } ) P ( \mathsf { C P } _ { i } )$ . Since

```csv
Algorithm K_NN (MacLookupTable, X, tablesize, int k)
/* K_NN Determines the current position using the K-NN algorithm.
MacLookupTable is a look-up table such as Table 1
X is an array of signal strengths from the APs gathered by the mobile terminal at the present moment
tablesize is the number of rows (== the number of candidate points) of MacLookupTable
K is the K of K-NN */
1 aSimilarity // Manhattan distance between X and a tuple of MacLookupTable
2 SimilarityList[tablesize] // An array of pairs of (aSimilarity, tuple number).
Sorted by aSimilarity
3 avg_X, avg_Y // Coordinates representing user's location
4 for(i=1; i<=tablesize; i++)
4-1 aSimilarity = Manhattan distance between X and MacLookupTable[i];
4-2 insert (aSimilarity, i) into SimilarityList in nondecreasing order;
5 end loop
6 for(i=1; i<=k; i++)
6-1 avg_X += x coordinate found in SimilarityList[i];
6-2 avg_Y += y coordinate found in SimilarityList[i];
7 end loop
8 avg_X = avg_X / k;
9 avg_Y = avg_Y / k;
10 Mark (avg_X, avg_Y), the current location, on PictureBox;
end K_NN
```  
Fig. 3. K-NN algorithm.

$P ( \mathbf { C P } _ { 1 } ) { = } P ( \mathbf { C P } _ { 2 } ) { = } \ldots { = } P ( \mathbf { C P } _ { m } ) ,$ , the $\mathrm { C P } _ { i }$ that maximizes $P ( X | \mathsf { C P } _ { i } )$ also maximizes $P ( X | \mathsf { C P } _ { i } ) P ( \mathsf { C P } _ { i } )$

$$
P (X | \mathrm{CP} _ {i}) = \prod_ {k = 1} ^ {n} P (x _ {k} | \mathrm{CP} _ {i}) = P (x _ {1} | \mathrm{CP} _ {i}) ^ {*} P (x _ {2} | \mathrm{CP} _ {i}) ^ {*}... ^ {*} P (x _ {n} | \mathrm{CP} _ {i})
$$

where, $\begin{array} { r } { P ( x _ { k } | \mathrm { C P } _ { i } ) = \frac { S _ { i k } } { S _ { i } } } \end{array}$ and $s _ { i k }$ is the number of tuples whose candidate point entry is $\mathrm { C P } _ { i }$ and $\mathsf { A P } _ { k } ^ { \mathsf { \prime } } s$ entry is $x _ { k } .$ Since $S _ { 1 } = S _ { 2 } = \ldots = S _ { 5 }$ , we can ignore $s _ { i \cdot }$ That is, the CP that maximizes $\Pi _ { k = 1 } ^ { n } s _ { i k }$ is determined to be user's current location.

Since we are multiplying $s _ { i k }$ for all $k ,$ the result becomes zero if any one of $s _ { i k }$ is zero. Therefore, we should discretize the entries of the training data set, as shown in Table $^ { 2 . }$ Furthermore, in order not to browse the entire training set of data during the on-line phase, we count the number of tuples having the same value and record the result, as shown in Table 3. The value of the cell $( \mathrm { C P } _ { 1 } , \mathrm { A P } _ { 1 } )$ , which is $I _ { 1 } { : } 5 0 _ { \mathrm { \ell } }$ , is a two dimensional entry and means that among the 100 signal strengths of $\mathsf { A P } _ { 1 }$ measured at candidate point 1, 50 were greater than −30 and classi<sup>fi</sup>ed into interval 1 $\left( I _ { 1 } \right)$

Example 1. Let $X = ( - 2 8 , - 3 5 , - 4 7 , - 5 4 , - 4 2 )$ and the training data set be Table 3. For Table $3 , S _ { 1 } = S _ { 2 } = . . . = S _ { 5 } = 1 0 0$ . Let's assume that our discretizing policy is $I _ { 1 } = \{ x | x > - 3 0 \}$ $I _ { 2 } = \left\{ x \right|$ $- 4 0 < x \leq - 3 0 \} , \ I _ { 3 } = \{ x | - 5 0 < x \leq - 4 0 \} , \ . . . ,$ then our discretized X will be $X = ( I _ { 1 } , I _ { 2 } , I _ { 3 } , I _ { 4 } , I _ { 3 } )$ . Then, the probability X of belonging to $\mathrm { C P _ { 1 } }$ is proportional to $5 0 ^ { * } 2 6 ^ { * } 1 5 ^ { * } 9 ^ { * } 8$

Our Bayesian positioning algorithm is shown in Fig. 4. Line 1 of it reads the training data set, as shown in Table 3, into Table, a 2 dimensional array. An element of Table, as de<sup>fi</sup>ned as T\_entry, is itself an array whose size is the number of intervals (5 in the case of Table 3). An element of T\_entry is itself also a 2 dimensional array. For each candidate point (Line 2) and for each AP (Line 2-2) accessible from the mobile terminal, or X's entry, Line 2-2-2 multiplies $s _ { i k } ,$ or TT\_entry[X[j]] [2], by probability[i].

An example training data set constructed by the off-line phase of the Bavesian method

<table><tr><td></td><td> $AP_1$ </td><td> $AP_2$ </td><td> $AP_3$ </td><td> $AP_4$ </td><td> $AP_5$ </td></tr><tr><td> $CP_1$ </td><td> $I_1: 50$ </td><td> $I_1: 43$ </td><td>...</td><td>...</td><td>...</td></tr><tr><td> $CP_1$ </td><td> $I_2: 33$ </td><td> $I_2: 26$ </td><td>...</td><td>...</td><td>...</td></tr><tr><td> $CP_1$ </td><td> $I_3: 11$ </td><td> $I_3: 10$ </td><td> $I_3: 15$ </td><td>...</td><td> $I_3: 8$ </td></tr><tr><td> $CP_1$ </td><td> $I_4: 5$ </td><td> $I_4: ...$ </td><td>...</td><td> $I_4: 9$ </td><td>...</td></tr><tr><td> $CP_1$ </td><td> $I_5: 1$ </td><td> $I_5: ...$ </td><td>...</td><td>...</td><td>...</td></tr><tr><td> $CP_2$ </td><td> $I_1: 5$ </td><td> $I_1: ...$ </td><td>...</td><td>...</td><td>...</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm Bayesian(X, n_AP, bayesianTable)
// X is an array of intervals representing the signal strengths from the APs gathered by the mobile terminal at the present moment
// n_AP: the number of APs
// bayesianTable: The file of the training data set as shown in Table 3
probability[1..n_CP]: int; // n_CP: the number of candidate points. Probability[i] will be
 $\prod_{k=1}^{n}s_{ik}$ .
T_entry[1..n_Interval][1..2]: int; // n_Interval is the number of intervals (It is 5 in Table 3).
T_entry[i] corresponds to an entry of Table 3.
Table[1..n_CP][1..n_AP] : T_entry ; // An entry of Table is a T_entry
1. Read bayesianTable into Table;
2. for (i:=1; i&lt;= n_CP; i++) {
2-1 probability[i] = 1;
2-2 for(j:=1; j&lt;=n_AP; j++) {
2-2-1 TT_entry = Table[i][j]; // If i=1 and j=1 then Table[1][1]={{(I1 50) (I2 33) (I3 11) (I4 5) (I5 1)} given Table 3
2-2-2 probability[i] = probability[i] * TT_entry[X[j]][2];
}
}
3. Find the index, i, of the maximum entry of probability[] and mark CPi on the PictureBox;
end Bayesian
</div>

Fig. 4. Bayesian algorithm

## 3.1.3. Implementation of a decision tree positioning system

The signal strengths in the training data for the decision tree are discretized, as we mentioned in Section 2.1.3. A typical training data set is shown in Table 2. Our algorithm to construct a decision tree is shown in Fig. 5. This algorithm is recursively constructs one node of the decision tree at a time following the process explained in Section 2.1.3. There are many ways of representing a tree. Our algorithm uses an array to represent the decision tree. The third parameter, Index, of Construct\_DT is the index of the array designating the cell which corresponds to the node that the current invocation is constructing. The <sup>fi</sup>rst parameter, Table, is a training data set which is shrunk by one column (or one attribute, or an AP) at line .1 of our algorithm. The second parameter of Construct\_DT, MacList, is the list of MAC addresses for the AP's constituting Table. As in the case of most recursive algorithms, the algorithm checks the termination condition at the beginning, from A to C, of the algorithm. The expected information needed to classify Table is computed at D. . For each AP in MacList, the algorithm computes the entropy and the information gain. Among the APs, the one with the maximum gain is chosen to be the label of the current node. Then, the algorithm recursively invokes itself with the shrunk Table.

## 3.2. Implementation of RF propagation loss model based methods

The implementation of the positioning systems based on trilateration and the extended Kalman Filter are discussed in this section. We measured the received signal strengths every 1 m from an AP 300 times and found the relation of the distance and RSSI, as shown in Fig. 6. Using the propagation model, we obtain the distance from the measured signal strength.

## 3.2.1. Implementation of trilateration

The structure of our program determining the location of the mobile terminal, M, by evaluating (Expression 1) is shown in Fig. 7. When the user clicks the button, “Where am I?”, Position\_Click() is invoked. It invokes GetRSSI() to obtain the strengths of the signals from the APs. Then, it also invokes Calculation\_Distance() with the signal strengths as parameters. It calculates the distances using the trend curve. Triangular\_Surveying() determines the location of the user by evaluating (1). In the process of evaluating (1), Triangular\_ Surveying() utilizes the Inverse() function. We implemented Inverse() using Laplace's cofactor expansion. Location\_Print() marks the user's position on the picture\_box.

```txt
Algorithm Construct_DT(int[][] Table, ListType MacList, int Index)
{
    A. if (all the CPs of Table are the same, CPi) // Table with only one row satisfies this condition
    i. Tree[Index] = CPi;
    B. else if (number of rows in Table == 0)
    i. Tree[Index] = NULL;
    C. else if (number of columns in Table == 1)
    i. Tree[Index] = for each CPi in Table, probability of CPi;
    D. else { // Number of rows !=1 and !A and !B and !C
    i. Compute I;
    ii. Compute Entropies for each AP;
    iii. Tree[Index] = MacAddress of the AP with maximum Gain and array P, where P[i] is the probability of CPi in Table;
    iv. Construct subMacList;
    v. loop (i=1; i<=number of Intervals; i++) {
    1. generate subTable;
    2. subIndex = Index * number of Interval + i;
    3. Construct_DT (subTable, subMacList, subIndex);
    vi. end loop }
    E. end if }
}
End Construct_DT
```  
Fig. 5. Algorithm to construct a decision tree.

![](/api/attachments/72KKQYXP/fulltext/images/da65fddc1d9d662302d6f22c064e6b8ffbb29e1b888bdaec8fa623d4f9d35a8c.jpg)  
Fig. 6. Relation of distance and RSSI.

![](/api/attachments/72KKQYXP/fulltext/images/c343fde8a2d85877ef56ac711a7fd61fc912b27db6696de0ebcc21bc64c1bc9a.jpg)  
Fig. 7. An event <sup>fl</sup>ow diagram of our trilateration based positioning system.

## 3.2.2. Implementation of extended Kalman Filter

The structure of our program determining the location of the mobile terminal, M, by means of the Extended Kalman Filter is similar to that of the trilateration based positioning system shown in Fig. 7. The only difference is that Triangular\_Surveying() is replaced by PositioningEKF(AP\_Positions, Distances) which is shown in Fig. 8. It performs the process shown in Table 3. The parameters, AP\_Positions and Distances, are the AP's coordinates and estimated distances, respectively, obtained using the propagation model shown in

```c
Algorithm PositioningEKF(AP_Positions, Distances)
// AP_Positions: Array of APs' positions.
// Distances: Array of estimated distances from the mobile terminal to the APs.

// Step 1) Initial guess
1    initializes X_matrix and P_matrix;
// Step 2) Linearizing.
2    for (i = 0; i < number of APs; i++)
    2-1 Temp = square of (AP_Positions[i][0] - X_matrix[0])
    + square of (AP_Positions[i][1] - X_matrix[1])
    + square of (AP_Positions[i][2] - X_matrix[2]);
    2-2 r_0[i] = square root of Temp;    // computed distance between nominal point and the i-th base station
3    for (i = 0; i < number of APs; i++)
    3-1 for (j = 0; j < number of axes; j++)
    3-1-1 if (((X_matrix[j] - AP_Positions[i][j]) is 0) or (r_0[i] is 0))
    then    H_matrix[i, j] = 0;
    3-1-2 else   then    H_matrix[i, j] = (X_matrix[j] - AP_Positions[i][j]) / r_0[i];
// Step 3) Kalman Gain
4    Temporary_K = H_matrix * P_matrix * H_matrix.Transpose() + R_matrix;
5    Inverse_K = Temporary_K.Inverse();
    // If K is not invertable then terminate
6    If(Inverse_K is not the inverse of K) then return false;
7    K_matrix = P_matrix * H_matrix.Transpose() * Inverse_K;
// Step 4) Measurement update, Step 6) State propagation.
8    for (i = 0; i < number of APs; i++)
    8-1 Z_matrix[i] = Distances[i] - r_0[i];
9    X_matrix = Pie_matrix * (X_matrix + K_matrix * Z_matrix);
// Step 5) Update error covariance, Step 6) State propagation
10    P_matrix = (I_matrix - K_matrix * H_matrix) * P_matrix;
11    P_matrix = Pie_matrix * P_matrix * Pie_matrix.Transpose() + Q_matrix;
// Step 7) Goto step2
12    if(continue) then Update Distances and Goto Line 2
    else return true;
end PositioningEKF
```

Table 4  
Parameter values for our EKF

<table><tr><td>Description</td><td>Value</td><td>Unit</td></tr><tr><td> $\overline{x}_{0}$ </td><td> $[40.0\ 40.0\ 2.0]^{T}$ </td><td>m</td></tr><tr><td> $P_{0}$ </td><td> $\begin{bmatrix}100.0 & 0.0 & 0.0 \\ 0.0 & 100.0 & 0.0 \\ 0.0 & 0.0 & 100.0\end{bmatrix}$ </td><td>m</td></tr><tr><td> $R_{0}$ </td><td>0.01</td><td></td></tr></table>

Fig. 6 from the mobile terminal to the APs. The <sup>fi</sup>rst step of Table 3 initializes $\vec { x } _ { 0 } ^ { - }$ and ${ \mathfrak { p } } _ { 0 } ^ { - } .$ The variables, X\_matrix and P\_matrix, which are objects of the Matrix class de<sup>fi</sup>ned in PositioningEKF() represent $\vec { x } _ { 0 } ^ { - }$ and ${ \bar { p _ { 0 } } } ,$ respectively, and Line 1 of PositioningEKF() initializes them with the values shown in Table 4. The variables, H\_matrix, K\_matrix, I\_matrix, R\_matrix, Q\_matrix, and Pie\_matrix, which are also objects of the Matrix class, in PositioningEKF() represent the variables H, K, I, R, Q, and Φ in Table 2, respectively, r\_0[number of APs] is used to store the computed distances between the nominal point and the base stations, and Z\_matrix is used to store the result of ${ \vec { r } } _ { k }$ ${ \vec { r } } _ { 0 }$ computed at step 4 of Fig. 2.

The distances between the nominal point and the base stations are computed in Line 2. The loop of Line 3 calculates $H ,$ which is to be used in calculating the Kalman gain (Step 3 of Fig. 2). Lines 4-7 are used to compute the Kalman gain. Lines 8 and 9 compute ${ \vec { r } } _ { k } - { \vec { r } } _ { 0 }$ and $\hat { \vec { x } } _ { k + 1 } ^ { - } = \varPhi _ { k } \Big ( \hat { \vec { x } } _ { k } ^ { - } + ~ K _ { k } ( \vec { r } _ { k } - \vec { r } _ { 0 } ) \Big )$ respectively. Line 10 performs Step $5 ( P _ { k } { = } ( I { - } K _ { k } H _ { k } ) P _ { k } ^ { - } )$ of Fig. 2 and Line 11 computes $P _ { k + 1 } ^ { - } { = } \Phi _ { k } P _ { k } \Phi _ { k } ^ { T } { + } Q _ { k }$ (Step 6 of Fig. 2). Finally,

Line 12 checks the termination condition and, if it is not met, then it updates Distances and goes back to Line 2. Our termination condition is as follows:

$$
\begin{array}{l} \left(| k ^ {\text {th}} X _ {-} \text {matrix} - (k - 1) ^ {\text {th}} X _ {-} \text {matrix} | \leq \text {Threshold}\right) \\ \text {or (Number of iterations\geq Limit).} \end{array}
$$

## 4. Experimental analysis

The graphical user interface (GUI) of our trilateration based positioning system is shown in Fig. 9. The <sup>fl</sup>oor plan shown in Fig. 9 represents the 4th <sup>fl</sup>oor of the Natural Science Building, our test bed. When the button, “Location?”, is clicked, the system runs our trilateration algorithm and writes the X and Y coordinates returned by the algorithm in the box labeled “Position Info:” It also marks a big dot at (X, Y) on the <sup>fl</sup>oor plan. When the button, “Test”, is clicked, it provides dialog boxes in which the actual user's location and an integer N can be input. Then, it runs our trilateration algorithm N times and records the results in the <sup>fi</sup>le named Result. We implemented 5 positioning systems: K-NN, Bayesian, Decision Tree, Trilateration, and EKF. All the GUIs of these systems are similar to that in Fig. 9.

There are many parameters affecting the ef<sup>fi</sup>ciency of a positioning system and the number of APs with signi<sup>fi</sup>cant signal strengths is one of them. If the RSSI from an AP is less than −70 then the distance to the AP cannot readily be determined with the RSSI and we consider it insigni<sup>fi</sup>cant. In the following experiments, we had 4 APs with signi<sup>fi</sup>cant signal strengths.

![](/api/attachments/72KKQYXP/fulltext/images/7b6f6af438179c9d6b4581cdb3810736d907dc0f550c33995102852fc0ab31ea.jpg)  
Fig. 9. A typical GUI of the positioning systems.

## Accuracy ofthe three fingerprinting positioning techniques

![](/api/attachments/72KKQYXP/fulltext/images/585fb68a9c1b7896eaef3148b0221201396fb394d757e66cbe927c84086363e2.jpg)  
Fig. 10. Accuracy of three <sup>fi</sup>ngerprinting methods.

## 4.1. Fingerprinting methods

We performed experiments in which we ran the 1-NN, Bayesian and decision tree methods on the training data with $N { = } 4$ (number of APs), I=6 (number of intervals), and $M = 9 6$ (number of candidate points) in order to compare their accuracies. The test results are shown in Fig. 10. In this <sup>fi</sup>gure, the 'number of samples' is the same as the number of measurements we performed for each entry of the look-up table. An entry of the look-up table is the average of the measurements. When the number of samples is 10, the K-NN method is much more accurate than the others. However, the difference decreases as the number of samples increases and when the number of samples is 50 the accuracies of the three methods are almost the same. For this experiment, X which is the vector of RSSIs collected at the user's current location was the average of 10 measurements.

During the off-line phase the K-NN method constructs a look-up table like Table 1. The time needed to construct the look-up table is linearly proportional to the total number of measurements. The Bayesian method constructs a table like Table 3 during the off-line phase and the time need for its construction is also linearly proportional to the total number of measurements. However, the decision tree method constructs a decision tree during the off-line phase. The process of constructing a decision tree takes longer than constructing a look-up table.

The time complexity of the on-line phase of K-NN is $O ( N ^ { * } M ) ,$ because for each row of the look-up table, K-NN calculates the Manhattan distance between the row and X, the vector of measured RSSs. The time complexity of the on-line phase of the Bayesian method is $O ( I ^ { * } N ^ { * } M )$ , because we count the number of samples belonging to the same interval for each AP. The time complexity of the on-line phase of the decision tree is $O ( I ^ { * } N ) .$ Therefore, we can conclude that the decision tree method is the most ef<sup>fi</sup>cient during the on-line phase.

During the off-line phase, a <sup>fi</sup>ngerprinting method collects location <sup>fi</sup>ngerprints at every candidate point. This is a very time consuming task. One of the alternatives to the <sup>fi</sup>ngerprinting methods is the propagation model based method. The propagation model method does not require the off-line phase.

## 4.2. Propagation loss model based methods

We implemented trilateration and EKF which are propagation loss model based methods and performed experiments in which we ran our trilateration and EKF positioning algorithms at 40 different locations. At each location, we estimated the position 300 times. The results of our experiments are summarized in Fig. 11. The X-axis represents the number of iterations and the Y-axis represents the errors of the positioning results in meters. $\mathrm { ~ \mathsf ~ { ~ A ~ } ~ } ^ { \bullet } + ^ { \bullet }$ in the graph represents an error of trilateration positioning and it is the average of the errors obtained at the 40 different locations. The dashed line represents the errors of EKF positioning and the solid line represents the average error of our trilateration (ET) positioning. As the graph shows, the average of the errors of our trilateration is 4.07 m, whereas the error of EKF (EE) converges to 3.528 m. There is a difference between ET and EF which comes from the fact that ET only counts distance which is always positive. For example, consider the case where the estimates are (140, 200) and (160, 200). Our trilateration would determine the user's position to be (150, 200) and ET would be 10. On the other hand, the estimate of EKF would be close to (150, 200) and EE would be much less than 10. The standard deviation of errors for trilateration shown in Fig. 11 is 0.675 m, while that of EKF for the last 250 estimates is 0.074 m. EKF converged more quickly than trilateration. Thus, the former is more stable than the latter.

Comparison of EKF vs. Trilateration  
![](/api/attachments/72KKQYXP/fulltext/images/e71117d5d97ff575396cd07e3662ff20c965caadde80f7e563c7057a39b276c5.jpg)  
Fig. 11. Comparison of trilateration and EKF.

Comparing the average error of K-NN (2.4 m) with that of EKF (3.528 m), we can conclude that the <sup>fi</sup>ngerprinting method is more accurate than EKF. However, EKF could be considered to be more practical in a coarse-grained application domain because it does not require a time consuming off-line phase.

## 5. Conclusion

We described the design and implementation of a WLANbased EKF positioning method. We used the RF propagation loss model to estimate the distances between the mobile terminal and the Access Points (AP) in the implementation. For the experimental evaluation of the proposed method, we also implemented the Trilateration method. Our experimental results showed that our EKF positioning method converges to the average of the results of trilateration positioning.

We also implemented three <sup>fi</sup>ngerprinting methods in order to compare the accuracy of our EKF method with them. Our experimental results showed that the <sup>fi</sup>ngerprinting methods are more accurate than the RF propagation model based methods. All the averages of the errors of our <sup>fi</sup>ngerprinting methods are close to 2.4 m, whereas the average error of EKF is about 3.528 m. Even though the <sup>fi</sup>ngerprinting method is more accurate than EKF, the latter method can be more practical because the former requires a lot of effort during its off-line phase.

Our experimental results can be summarized as follows.

• While <sup>fi</sup>ngerprinting methods require a tedious and time consuming off-line phase, EKF does not. Therefore, EKF is more convenient to install and more ef<sup>fi</sup>cient to use.

• The average errors of the <sup>fi</sup>ngerprinting methods are less than that of our EKF. Our experiments showed that all the average errors of the <sup>fi</sup>ngerprinting methods are close to 2.4 m, whereas the average error of our EKF is 3.528 m. Even though our EKF is slightly less accurate than the <sup>fi</sup>ngerprinting method, it is accurate enough to determine the room or of<sup>fi</sup>ce in which the user is located. Therefore, we can develop a lot of LBS applications using our EKF WLAN-based indoor positioning method.

• Our experiments also showed that the average error of trilateration is 4.07 m, whereas the average error of our EKF is 3.528 m. Based on this result, we can conclude that our EKF can be widely used in the development of practical LBSs. In fact, developing a practical LBS is our next research topic.

In further research, we will attempt to improve the accuracy of EKF. One of the reasons for the inaccuracy of our EKF is the noise residing in the signals from the APs. We will focus on developing an EKF which eliminates the noise in the signal.

We implemented 5 different indoor positioning methods. We are planning to integrate them so that a user can choose the most adequate one for his or her application.

## References

[1] C. Antunes, L. Dias, Managing uncertainty in decision support models foreword to the special issue, Decision Support Systems 43 (4) (2007) 1451–1453.

[2] O.M. Badawy, M. Hasan, Decision tree approach to estimate user location in WLAN based on location <sup>fi</sup>ngerprinting, Proceedings of 24th National Radio Science Conference, Ain Shams Univ., Egypt, 2007, pp. 1–10.

[3] P. Bahl, V. Padmanabhan, RADAR: an in-building RF-based user location and tracking system, Proceeding of INFOCOM 2000, 2000, pp. 775–784.

[4] S. Bolognani, L. Tubiana, M. Zigliotto, Extended Kalman <sup>fi</sup>lter tuning in sensorless PMSM drives, IEEE Transactions on Industry Applications 39 (6) (2003) 1741–1747.

[5] M. Boussak, Implementation and experimental investigation of sensorless speed control with initial rotor position estimation for interior permanent magnet synchronous motor drive, IEEE Transactions on Power Electronics 20 (6) (2005) 1413–1422.

[6] R.G. Brown, P.Y.C. Hwang, Introduction to Random Signals and Applied Kalman Filtering with Matlab Exercises and Solutions, 3rd Ed.John Wiley & Sons, 1996.

[7] D. Choi, Personalized local internet in the location-based mobile web search, Decision Support Systems 43 (1) (2007) 31–45.

[8] A. Gelb, Applied Optimal Estimation, The MIT Press, London, 1974.

[9] T. Gigl, G. Janssen, V. Dizdarevic, K. Witrisal, Z. Irahhauten, Analysis of a UWB indoor positioning system based on received signal strength Proceedings of the 4th Workshop on Positioning, Navigation and Communication, Hannover, Germany, 2007, pp. 97–101.

[10] A. Harter, A. Hopper, A new location technique for the active of<sup>fi</sup>ce, IEEE Personal Communications 4 (5) (1997) 43–47.

[11] S. Ito, N. Kawaguchi, Bayesian based location estimation system using wireless LAN, Proceedings of the Third IEEE International Conference on Pervasive Computing and Communications Workshops, 2005, pp. 273–278.

[12] K. Kaemarungsi, Ef<sup>fi</sup>cient design of indoor positioning systems based on location <sup>fi</sup>ngerprinting, Proceedings of International Conference on Wireless Networks, Communications and Mobile Computing, vol. 1, 2005, pp. 181–186.

[13] K. Kaemarungsi, P. Krishnamurthy, Modeling of indoor positioning systems based on location <sup>fi</sup>ngerprinting, Proceedings of the INFOCOM 2004, Twenty-third Annual Joint Conference of the IEEE Computer and Communications Societies, vol. 2. 2004, pp. 1012–1022.

[14] K. Kaemarungsi, P. Krishnamurthy, Properties of indoor received signal strength for WLAN location fingerprinting, Proceedings of the First Annual International Conference on MOBIQUITOUS, 2004, pp. 14–23.

[15] A. Kotanen, M. Hannikainen, H. Leppakoski, T.D. Hamalainen, Experiments on local positioning with bluetooth, Proceedings of International Conference on Information Technology: Coding and Computing [Computers and Communications] (ITCC 2003), 2003, pp. 297–303.

[16] F. Lassabe, P. Canalda, P. Chatonnay, F. Spies, A Friis-based calibrated model for WiFi terminals positioning, Proceedings of the Sixth IEEE International Symposium on a World of Wireless Mobile and Multimedia Networks (WoWMoM 2005), 2005, pp. 382–387.

[17] T. Lin, P. Lin, Performance comparison of indoor positioning techniques based on location <sup>fi</sup>ngerprinting in wireless networks, Proceedings of International Conference on Wireless Networks, Communications and Mobile Computing, 2005, pp. 1569–1574.

[18] D. Madigan, E. Einahrawy, R.P. Martin, W. Ju, P. Krishnan, A.S. Krishnakumar, Bayesian indoor positioning systems, Proceedings of the IEEE 24th Annual Joint Conference of the IEEE Computer and Communications Societies (INFOCOM 2005), 2005, pp. 1217–1227.

[19] P.S. Maybeck, Stochastic Models, Estimation, and Control Vol. I, II and III, Academic Press. 1982

[20] Z. Peroutka, Design considerations for sensorless control of PMSM drive based on extended Kalman <sup>fi</sup>lter, Proceedings of 2005 European Conference on Power Electronics and Applications, 2005, pp. 1–10.

[21] D. Power, R. Sharda, Model-driven decision support systems: concepts and research directions, Decision Support Systems 43 (3) (2007) 1044-1061.

[22] N. Priyanthat, A. Chakraborty, H. Balakrishnan, The Cricket locationsupport system, Proceedings of 6th ACM International Conference on Mobile Computing and Networking, Boston, MA, 2000.

[23] H. Qasem, L. Reindl, Unscented and Extended Kalman estimators for non linear indoor tracking using distance measurements. Proceedings of the 4th Workshop on Positioning, Navigation and Communication, WPNC '07, 2007, pp, 177–181.

[24] J. Ray, A web-based spatial decision support system optimizes routes for oversize/overweight vehicles in Delaware, Decision Support Systems, 43 (4) (2007) 1171–1185.

[25] D. Song, R. Lau, P. Bruza, K. Wong, D. Chen, An intelligent information agent for document title classi<sup>fi</sup>cation and <sup>fi</sup>ltering in documentintensive domains, Decision Support Systems 44 (1) (2007) 251–265.

[26] T. Teo, J. Chai, W. Yao, Design of a positioning system for AGV navigation, Proceedings of the 7th International Conference on Control, Automation, Robotics and Vision, 2002, pp. 637–642.

[27] C. Wann, M. Lin, Data fusion methods for accuracy improvement in wireless location systems, Proceeding of the IEEE Wireless Communications and Networking Conference (WCNC 2004), 2004, pp. 471–476.

[28] R. Want, A. Hopper, V. Falcao, J. Gibbons, The active badge location system, ACM Transactions on Information Systems 10 (1) (1992) 91–102.

[29] J. Yim, Introducing a decision tree-based indoor positioning technique, Expert Systems with Applications 34 (2) (2008) 1296–1302.

[30] M. Youssef, A. Agrawala, Continuous space estimation for WLAN location determination systems, Proceedings of 13th Internationa Conference on Computer Communications and Networks, Chicago, IL, 2004, pp. 161–166.

[31] M. Youssef, A. Agrawala, A.U. Shankar, WLAN location determination via clustering and probability distributions, Proceedings of IEEE International Conference on Pervasive Computing and Communications (PerCom), 2003, pp. 143–150.

![](/api/attachments/72KKQYXP/fulltext/images/051cadd67690aaf0d8ff8233d9ebc95a4ca0cdc13957955568b55e4d99995e51.jpg)

Jaegeol Yim received the M.S. and Ph. D. degrees in Computer Science from the University of Illinois at Chicago, in 1987 and 1990, respectively. He is a Professor in the Department of Computer Science at Dongguk University at Gyeongju Korea. His professional experience includes elementary school teacher, of<sup>fi</sup>cer of Korean government (Board of Economy and Plan). and researcher of Hyundai Electronic Ltd. His current research interests include Petri net theory and its applications on Location-Based Service, computer networks, Korean Language manipulation, A

systems, and multimedia systems. He has published more than 20 journal papers, 70 conference papers (mostly written in Korean Language), and two undergraduate textbooks.

![](/api/attachments/72KKQYXP/fulltext/images/dfd64121d952c033d59aa9f064dfe5e0969ceab7f33e4686863d604a802a6375.jpg)

Chansik Park received the B.S., M.S. and Ph. D. degrees in Department of Control and Instrumentation from Seoul National University in 1984. 1986 and 1997 respectively. He is currently professor of the School of Electrical and Computer Engineering, Chungbuk National University, Cheongju, Korea. His research interests include GNSS, SDR, AJ, ITS and WSN.

![](/api/attachments/72KKQYXP/fulltext/images/9f41df4f9d3f315f5d745bbde58e58cfc94f8ab60b428ebfc984a48d2be54d21.jpg)

Jaehun Joo is a professor of Department of Electronic Commerce at Dongguk University in Korea and Editor-in-Chief, Journal of Information Systems of Korea Association of Information Systems. Also he was a Visiting Professor of Department of Management at University of Nebraska–Lincoln. He received his Ph. D. from Busan National University. His areas of research interest are electronic commerce. location-based services, Semantic Web, and knowledge management. He published many papers in Information Systems Management, International Journal of

Industrial Engineering, Expert Systems with Applications, Journal of Computer Information Systems, etc.

![](/api/attachments/72KKQYXP/fulltext/images/943d6f8ade9ef9cdc3786bc76b8869b8bd3fab0b46b56e04ea779f34a8565fe7.jpg)

S. Jeong is a student of Graduate College in Dongguk University majoring in Computer Science. He is interested in Location Based System, GIS, and IEEE 802.11.
