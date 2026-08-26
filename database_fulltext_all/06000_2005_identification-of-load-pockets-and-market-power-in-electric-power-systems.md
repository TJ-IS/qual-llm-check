---
otero_id: 6000
otero_key: "K2RS4P2M"
title: "Identification of load pockets and market power in electric power systems"
authors: "Bernard C. Lesieutre; Robert J. Thomas; Timothy D. Mount"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.09.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Identification of load pockets and market power in electric power systems

Bernard C. Lesieutre<sup>a,\*</sup>, Robert J. Thomas<sup>b</sup>, Timothy D. Mount<sup>c</sup>

<sup>a</sup>Lawrence Berkeley National Lab, 1 Cyclotron Rd, MS 90R4000, Berkeley, CA, 94720, United States <sup>b</sup>School of Electrical and Computer Engineering, Cornell University, Ithaca, NY 14853, United States <sup>c</sup>Applied Economics and Management, Cornell University, Ithaca, NY 14853, United States

Available online 6 November 2004

## Abstract

In this paper, we present a spectral method for the identification of load pockets and the application of practical techniques for the measurement of market power. Market power is a serious concern in electric energy markets, especially in the area of a load pocket. Common definitions for market power, which rely on a comparison between market prices and a so-called competitive price, are difficult to use in practice because the competitive price is not known when the market is not competitive. The competitive price cannot be computed from data naturally available to the market. Our technique focuses on the identification of participants with the ability to increase revenues by increasing prices, an ability not present in a competitive market. We then propose measures for quantifying the extent to which market power is being exercised. These measures can be computed from data available to the market; they are practical. We present results from a 30 bus, 6 generator system, which illustrates that generators in a load pocket have and can exploit joint market power. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Electricity markets; Market power; Spectral methods

## 1. Introduction

The analysis of recently restructured electric power systems has led to discussions and debates concerning the ability of market participants to manipulate the market to their advantage. Indeed, there are instances in which market manipulation has been convincingly established [11]. Our goal in this paper is to provide a definition for market power potential and provide practical and objective metrics for evaluating market power.

This is an important and difficult task. Commonly used metrics for evaluating competition and market power are lacking in detail or are not practical. The Herfindahl–Hirschman Index (HHI) for the competitiveness of a market is practical in that it is seemingly easy to apply; however, the results are not often definitive. Qualitatively, the HHI measures the concentration of market resources among participants. A high value, above 1800 on a scale of 10,000 (according to usage by the Department of Justice [10]), suggests the resources are highly concentrated and the market may not be competitive. A low value, below 1000, suggests that the resources are adequately distributed to enable a competitive market. Moderate concentrations exist with HHI indices between 1000 and 1800, and market power issues may be important. The HHI does not determine if market power is being exercised. Application of the HHI to electricity markets can be misleading due to the geographic distribution of resources, the network topology and resulting power flows, and the presence of load pockets [1].

More direct and detailed measures of market power, such as the Lerner Index, focus on market prices relative to <sup>b</sup>competitive price<sup>Q</sup>. In the context of electricity markets, the recent FERC notice of proposed rulemaking states, <sup>b</sup>Market power is the ability to raise prices above the competitive level<sup>Q</sup> [12]. The challenge with such definitions is that they require knowledge of the competitive price, which is an unverifiable benchmark that cannot be easily calculated. (If it can be easily calculated, there is no need for a market.) When a market is competitive, it defines the competitive price; otherwise, the competitive price is unknown. One might suggest that a calculation of competitive price is possible through a detailed audit of every generator’s fuel cost, efficiency data and more; however, any such calculation would be at least partially subjective. Any decision based on a calculation of competitive price would likely languish in the legal system for years. Examination of market power based on competitive price is sensible in theory, but difficult, if not impossible, in practice. (Nevertheless, after the electricity crisis in California, there have been numerous efforts to calculate competitive price [2–6]. They yield inconsistent results and interesting debate.)

In this paper, we propose a practical and objective approach to examine market power. It requires only the available information and rules used to operate the electricity market and system. We specifically seek to identify those suppliers with the ability to increase revenues by raising prices, without affecting the revenues of the remaining participants in the market. Clearly, these suppliers enjoy some measure of market power since such ability would not be possible in a competitive market in which their generation is easily substitutable.

We present this work in the context of an important instance in which the physical characteristics of the system may result in local advantage for some participants: the presence of so-called <sup>b</sup>load pockets<sup>Q</sup>. Load pockets arise when the network limitations essentially isolate a portion of the system from remaining resources [8]. In an elementary scenario, one can consider the case when all transmission lines connecting a region are at their maximum import capacities limits. Then, any additional energy required by loads within this pocket must be supplied a smaller number of generators located within the pocket. (Other constraints such as voltage and security may also contribute to the formation of load pockets.) With fewer suppliers in the load pocket, there is concern that the generators may have and find ways to exploit increased market power.

In this paper, we present a spectral method for identifying load pockets and then apply practical techniques we have developed to identify and quantify market power. The reader solely interested in market power issues may safely proceed ahead of the next section in which we present the details of our method to identify load pockets. However, it will be necessary to refer back to the example introduced in Section 2.

## 2. Load pocket identification

To distinctly group generators that enjoy placement within a load pocket, it is natural to examine a matrix of price elasticities, which maps generator energy prices to generator dispatch. Consider the optimal dispatch in a competitive market with no constrained generators and inelastic loads. If a generator were to increase its offer price profile (above its present nodal price), it would lose some of its market share. Its dispatch would decrease and be replaced by the remaining suppliers. If a generator can increase its offer price profile (above its present nodal price) without affecting its dispatch, then it enjoys some isolation from market competition. More generally, a small group of generators within a load pocket may have the ability to increase offer prices, in some proportion, without changing their dispatch.

To identify these generators from a mathematical model, we form a matrix of price elasticities, M, which relates vectors of dispatch, z, and energy price, w:

$$
z = M w\tag{1}
$$

An impediment to finding such a linear representation is that generator offers are typically represented in blocks, and the clearing nodal price may differ from the offered price in a uniform price auction. To obtain the desired incremental model, we perform two optimal power flows (OPF). The first, using all the usual market details including block offers, establishes the operating point. In the second OPF we replace the block offers with the corresponding nodal price and relax generator production limits. This second OPF yields identical results as the first. The model for the second OFP allows incremental analysis which we perform below. Please keep in mind that we are trying to identify generators in a load pocket by their ability to increase offer prices without affecting dispatch; we are not evaluating whether this ability is being used. The second OPF model allows us to do this identification.

The objective of the second OPF is to minimize $w ^ { T } z$ subject to the vector of binding constraints from the first OPF, $g ( z , y ) { = } 0$ (except the relaxed generator constraints), where y represents all relevant variables other than offer price, w, and dispatch, z. (The vector y will include load constants, reactive powers, voltage magnitudes and angles, and all other variables that may be present.) It is convenient to separate the binding constraints into

$$
g (z, y) = \left[ \begin{array}{c} g _ {1} (z, y) \\ g _ {2} (y) \end{array} \right]\tag{2}
$$

where $g _ { 1 } ( z , y )$ contains the network active power constraints at the generator buses and $g _ { 2 } ( y )$ contains the rest of binding constraints. It is important to note that dispatch terms, $z _ { i } ,$ appear linearly in the individual $g _ { 1 } ( z , y )$ constraint equations;

$$
\begin{array}{l} g _ {1 i} (z, y) = \sum_ {k} G _ {i k} V _ {i} V _ {k} \cos (\theta_ {i} - \theta_ {k}) \\ \qquad + \sum_ {k} B _ {i k} V _ {i} V _ {k} \sin (\theta_ {i} - \theta_ {k}) - z _ {i}. \end{array}\tag{3}
$$

The Lagrangian for this optimization problem is

$$
L (z, y, \lambda) = w ^ {T} z + \lambda_ {1} ^ {T} g _ {1} (z, y) + \lambda_ {2} ^ {T} g _ {2} (y)\tag{4}
$$

for which the optimal solution comes from the following equations:

$$
0 = w - \lambda_ {1} \quad (\text { since   } \mathrm{d} g _ {1 i} / \mathrm{d} z _ {i} = - 1)\tag{5}
$$

$$
0 = \frac {\partial g _ {1} (z , y) ^ {T}}{\partial y} \lambda_ {1} + \frac {\partial g _ {2} (y) ^ {T}}{\partial y} \lambda_ {2}\tag{6}
$$

$$
0 = g _ {1} (z, y)\tag{7}
$$

$$
0 = g _ {2} (y)\tag{8}
$$

Eq. (5) confirms that the nodal price solution of the second OPF is identical to the first OPF. Likewise, the remaining equations will yield identical results as well. Now, we form an incremental model of the nonlinear Eqs. (6)–(8) from which we will derive the linear relation we seek Eq. (1). We linearize around the optimal solution to obtain

$$
0 = H \Delta y + \frac {\partial g _ {1} (z , y) ^ {T}}{\partial y} \Delta \lambda_ {1} + \frac {\partial g _ {2} (y) ^ {T}}{\partial y} \Delta \lambda_ {2}\tag{9}
$$

$$
0 = - \Delta z + \frac {\partial g _ {1}}{\partial y} \Delta y\tag{10}
$$

$$
0 = \frac {\partial g _ {2}}{\partial y} \Delta y\tag{11}
$$

where the incremental variables are denoted with $\Delta { \bf \Phi } _ { { \bf S } , { \bf \Phi } }$ the values of the partial derivatives which form the matrices are evaluated at the OPF solution, and the Hessian matrix, H, is

$$
H = \sum_ {i} \lambda_ {2 i} \nabla^ {2} g _ {2 i} (y).\tag{12}
$$

Straightforward linear algebraic reduction yields

$$
\Delta z = M \Delta \lambda_ {1}\tag{13}
$$

where

$$
\begin{array}{c} M = \frac {\partial g _ {1}}{\partial y} \Bigg \{H ^ {- 1} \frac {\partial g _ {2} ^ {T}}{\partial y} \bigg (\frac {\partial g _ {2}}{\partial y} H ^ {- 1} \frac {\partial g _ {2} ^ {T}}{\partial y} \bigg) ^ {- 1} \\ \times \frac {\partial g _ {2}}{\partial y} H ^ {- 1} - H ^ {- 1} \Bigg \} \frac {\partial g _ {1} ^ {T}}{\partial y} \end{array}\tag{14}
$$

Alternatively, the matrix can be found empirically through repeated experimentation with appropriate incremental price variations.

Matrix M has an important property: it is singular and $M \lambda _ { 1 } { = } 0$ at the optimal solution.

(Hence, $\lambda _ { 1 }$ is an eigenvector associated with a zero eigenvalue.) Intuitively, this property indicates that a proportional change in nodal prices at all generators will result in zero change to dispatch.

To discuss the properties of the matrix when a load pocket is present, we separate the generators into two groups: those within the pocket, denoted below with a subscript ${ } ^ { 6 6 } \mathrm { L } ^ { 9 3 } ,$ , and those external to the pocket, denoted with a subscript $\mathrm { ^ { 6 6 } F ^ { 9 } }$ (far). Then, the incremental Eq. (13) becomes

$$
\left[ \begin{array}{c} \Delta z _ {\mathrm{L}} \\ \Delta z _ {\mathrm{F}} \end{array} \right] = \left[ \begin{array}{c c} M _ {\mathrm{LL}} & M _ {\mathrm{LF}} \\ M _ {\mathrm{FL}} & M _ {\mathrm{FF}} \end{array} \right] \left[ \begin{array}{c} \Delta \lambda_ {\mathrm{L}} \\ \Delta \lambda_ {\mathrm{F}} \end{array} \right]\tag{15}
$$

As discussed above, the nodal price profile, $\lambda _ { 1 } ,$ , is an eigenvector of M, corresponding to a zero eigenvalue. Separating and re-ordering components of $\lambda _ { 1 }$ into parts corresponding to the load pocket and external pocket (using subscripts in the obvious way), this property is written as

$$
\left[ \begin{array}{c} 0 \\ 0 \end{array} \right] = \left[ \begin{array}{c c} M _ {\mathrm{LL}} & M _ {\mathrm{LF}} \\ M _ {\mathrm{FL}} & M _ {\mathrm{FF}} \end{array} \right] \left[ \begin{array}{c} \lambda_ {1 \mathrm{L}} \\ \lambda_ {1 \mathrm{F}} \end{array} \right]\tag{16}
$$

A proportional increase change in all nodal prices results in no change in dispatch.

For a load pocket for which the incremental demand must be satisfied by the generators in the pocket

$$
\left[ \begin{array}{c} \Delta z _ {\mathrm{L}} \\ \Delta z _ {\mathrm{F}} \end{array} \right] = \left[ \begin{array}{c c} M _ {\mathrm{LL}} & M _ {\mathrm{LF}} \\ M _ {\mathrm{FL}} & M _ {\mathrm{FF}} \end{array} \right] \left[ \begin{array}{c} \Delta \lambda_ {\mathrm{L}} \\ 0 \end{array} \right] = \left[ \begin{array}{c} 0 \\ 0 \end{array} \right]\tag{17}
$$

The generators in the load pocket can increase nodal prices without affecting dispatch. With the same dispatch and imports in the pocket, the electrical solution remains unchanged throughout and the dispatch does not change in the external area.

Eq. (17) presumes that the load pocket has already been identified and the equation and variables have been sorted appropriately. Our challenge is to find this separation when it exists. A direct spectral approach is to search the space spanned by eigenvectors corresponding to zero eigenvalues for vectors whose elements can be grouped into two distinct groups, one of which has values equal to zero. In the case of a perfect load pocket, there are multiple zero-valued eigenvalues. The corresponding eigenvectors are not unique.

Consider the case when there are two zero eigenvalues with corresponding linearly independent eigenvectors $\boldsymbol { \nu } _ { 0 }$ and $\nu _ { 1 }$ such that

$$
M \left[ \begin{array}{c c} v _ {0} & v _ {1} \end{array} \right] = \left[ \begin{array}{c c} 0 & 0 \end{array} \right].\tag{18}
$$

Then, any vector of the following form will serve as an eigenvector,

$$
w = \alpha_ {0} v _ {0} + \alpha_ {1} v _ {1}\tag{19}
$$

where $\alpha _ { 0 }$ and $\alpha _ { 1 }$ are scalar constants. In this space of eigenvectors, we seek possibilities that group generators. We are aided by the knowledge that $\lambda _ { 1 }$ is one of the eigenvectors we seek. The following approach allows us to find others.

First, we normalize the incremental dispatches and nodal prices around their nominal values:

$$
\Delta z _ {i} ^ {\prime} = \frac {\Delta z _ {i}}{z _ {i}} \quad \Delta \lambda_ {i} ^ {\prime} = \frac {\Delta \lambda_ {i}}{\lambda_ {i}}\tag{20}
$$

Then,

$$
\Delta z ^ {\prime} = E \Delta \lambda^ {\prime}\tag{21}
$$

where

$$
E = \left(\operatorname{diag} (z)\right) ^ {- 1} M (\operatorname{diag} (\lambda))\tag{22}
$$

(the diag function denotes a diagonal matrix whose elements correspond to the elements of the vector argument). This scaling is arguably appropriate because we are ultimately interested in relative changes. Also, importantly, it converts the known eigenvector $\lambda _ { 1 }$ to a vector of all ones, $[ 1 \ 1 . . . 1 ] ^ { T } ,$ which we denote as $\nu _ { 0 } .$ Given that we observe two zero eigenvalues and that the corresponding eigenvectors are not unique, we choose to investigate the following pair of orthogonal eigenvectors:

$$
v _ {0} = \left[ \begin{array}{c} 1 \\ 1 \end{array} \right] v _ {1} = \left[ \begin{array}{c} V _ {\mathrm{1L}} \\ V _ {\mathrm{1F}} \end{array} \right]\tag{23}
$$

where we reorder the elements such that elements of $V _ { \mathrm { 1 L } }$ are all positive and the elements of $V _ { \mathrm { 1 F } }$ are negative. (By definition, the vectors are orthogonal and $\nu _ { 0 } ^ { T } \nu _ { 1 } { = } 0$ . Since $\nu _ { 0 }$ is a vector of all ones, $\nu _ { 1 }$ must have positive and negative elements.) Furthermore, if an ideal load pocket exists, the elements of $V _ { \mathrm { 1 F } }$ are identical so that

$$
w _ {1} = \alpha_ {0} v _ {0} + v _ {1} = \left[ \begin{array}{c} w _ {\mathrm{1L}} \\ 0 \end{array} \right]\tag{24}
$$

is a vector whose nonzero elements correspond to generators in the load pocket. (The value of $\alpha _ { 0 }$ is the magnitude of one of the elements of $V _ { \mathrm { 1 F } } \mathrm { . }$

For identification purposes, the elements in $\nu _ { 1 }$ can be used to separate generators into two groups: those in the load pocket and those outside the pocket. It is worth noting that both groups of generators have the ability to incrementally increase prices without affecting the dispatch. Nevertheless, the existence of such a dichotomy indicates that economic forces have separated the system, and the generators of most interest should be those with higher nodal prices on average.

We should emphasize that such a spectral method described above is not necessary for the obvious case when a load pocket is evident through transmission line limits that completely isolate an area. However, such obvious instances are probably not the norm. Effectively, a power line may be physically limited to some value below its rated thermal limit due to limits on other apparatus. That is, it may simply be impossible to load a particular line to its thermal limit without overloading a different line or exceeding a voltage limit first. The complete geographic area of a load pocket is difficult to identify without the aid of analyses like that proposed here.

In practice, we are not likely to observe perfect load pockets for several reasons. The limiting transmission line constraints that contribute to the formation of load pockets are expressed in terms of MVA limits that reflect both active and reactive power flows. Adjusting offer prices in the load pocket may allow some shift in active and reactive power along a limiting line and result in a small change in dispatch. Similarly, a voltage constraintinduced load pocket may allow small changes in dispatch as well. Finally, slightly elastic loads will shift demand (and dispatch) in response to variations in offer price. (The effect of mildly elastic loads can be considered more concretely by augmenting the model slightly to explicitly include these loads.) In these cases, the matrix of price elasticities will not exhibit multiple zero eigenvalues but will have relatively small eigenvalues. It is practical then to examine the small eigenvalues and the space spanned by their corresponding eigenvectors. In fact, the uniqueness of the eigenvectors should facilitate the identification process.

To demonstrate the effectiveness of this spectral approach, we introduce an example system that we will use throughout this paper.

## 2.1. 30 bus, 6 generator example system

We consider the 30 bus, 6 generator system shown in Fig. 1 (which is also used in the prior work [9]). The two lines connecting Area II to the other areas are limited to 10 MVA each. The total system load is 165 MW with 49 MW in the load pocket. The capacity for each generator is 60 MW. The total load is much lower than the capacity of the system. A base case solution for the full nonlinear AC optimal power flow is shown in Table 1. At this operating point, one line is at its import capacity limit (connecting buses 4 and 12) and the other is just below its rated limit (connecting buses 23 and 24).

The evident price differential and the line limitations connected to Area II already gives some indication that generators 5 and 6 may lie within a load pocket. This is confirmed by our analysis. The matrix of normalized price elasticities is shown in Table 2.

One may quickly verify that the matrix has at least one zero-eigenvalue by noting that the elements in each row sum to zero. This confirms our intuition that a proportional increase in nodal price throughout the system will not affect the dispatch. It is not immediately obvious from the matrix whether a load pocket exists, although the nearly opposing values in columns 5 and 6 are suggestive. Nearly equal price variations in nodal prices at generators 5 and 6 should have little affect on dispatch.

![](/api/attachments/K2RS4P2M/fulltext/images/f280fdc1a14400998d0d309ab1bd467e0dbb71609f80b57c28c1ed79b2a3dc59.jpg)  
Fig. 1. Thirty bus, six generator system.

Now, we present the results of a spectral analysis of the matrix. The eigenvalues are calculated to be

$$
[ 0. 0 0 \quad - 0. 0 5 7 \quad - 0. 5 2 5 \quad - 2 6. 0 \quad - 4 0. 5 \quad - 2 0 1 ].
$$

The corresponding eigenvectors are

<table><tr><td>[1.00]</td><td>[-0.02]</td><td>[-0.51]</td><td>[-0.16]</td><td>[0.44]</td><td>[1.00]</td></tr><tr><td>[1.00]</td><td>[-0.02]</td><td>[-0.52]</td><td>[-0.14]</td><td>[0.31]</td><td>[-0.94]</td></tr><tr><td>[1.00]</td><td>[0.03]</td><td>[0.59]</td><td>[-0.76]</td><td>[-0.52]</td><td>[0.04]</td></tr><tr><td>[1.00]</td><td>[0.03]</td><td>[0.34]</td><td>[1.00]</td><td>[-0.20]</td><td>[0.03]</td></tr><tr><td>[1.00]</td><td>[0.90]</td><td>[-0.58]</td><td>[0.07]</td><td>[-0.69]</td><td>[0.06]</td></tr><tr><td>[1.00]</td><td>[1.00]</td><td>[1.00]</td><td>[-0.10]</td><td>[1.00]</td><td>[-0.09]</td></tr></table>

In a very meaningful sense, the eigenvalues can be considered gains. When a (normalized) nodal price profile change occurs that matches the first eigenvector, the change in dispatch can be described by the price change profile multiplied by the first eigenvalue, or in that case zero. If a nodal price profile change matches the second eigenvector, then a resulting change in dispatch will be the price profile scaled by the second eigenvalue, or in that case almost zero. Any possible nodal price profile change can be represented as a sum of scaled eigenvectors, and the resulting change in dispatch can be inferred from the corresponding eigenvalues associated with the eigenvectors.

The second eigenvalue is very small and suggests the presence of a load pocket. Furthermore the corresponding second eigenvalue has large values corresponding to generators 5 and 6, and nearly zero values for the rest. This suggests that generators 5 and 6 are somewhat isolated. The eigenvalue is not exactly zero and as such the load pocket is not perfect.

Table 1  
Base case dispatch and nodal prices

<table><tr><td></td><td>G1</td><td>G2</td><td>G3</td><td>G4</td><td>G5</td><td>G6</td></tr><tr><td>Dispatch (MW)</td><td>31.7</td><td>36.0</td><td>34.0</td><td>36.0</td><td>17.6</td><td>12.0</td></tr><tr><td>Price (US$/MW h)</td><td>40.0</td><td>40.1</td><td>40.0</td><td>40.1</td><td>55.0</td><td>54.3</td></tr></table>

Table 2  
Base case price elasticities

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>-105.0</td><td>101.9</td><td>1.0</td><td>2.0</td><td>1.6</td><td>-1.5</td></tr><tr><td>2</td><td>89.5</td><td>-103.7</td><td>6.8</td><td>7.3</td><td>8.7</td><td>-8.6</td></tr><tr><td>3</td><td>0.9</td><td>7.2</td><td>-17.0</td><td>9.1</td><td>-6.9</td><td>6.7</td></tr><tr><td>4</td><td>1.8</td><td>7.3</td><td>8.5</td><td>-17.6</td><td>-10.1</td><td>9.8</td></tr><tr><td>5</td><td>2.2</td><td>13.1</td><td>-9.7</td><td>-5.3</td><td>-10.1</td><td>9.8</td></tr><tr><td>6</td><td>-3.0</td><td>-19.1</td><td>14.1</td><td>7.7</td><td>14.6</td><td>-14.3</td></tr></table>

In Section 3, we investigate whether the location of generators 5 and 6 allow them special advantage in the market.

## 3. Market power potential and metrics

As discussed in Section 1, our approach to market power involves the identification of market participants who have the ability to increase revenues by increasing prices. This approach has the benefit of clearly identifying non-competitive abilities without having to rely on an unverifiable benchmark such as <sup>b</sup>competitive price<sup>Q</sup>. In this section, we work through the technical details of this approach to determine if generators 5 and 6, located within a load pocket in our test system, enjoy and exploit some level of market power.

First, we determine if a generator or group of generators has the ability to (1) incrementally increase their own revenues by incrementally increasing nodal price, (2) without affecting the revenues of the remaining generators. Suppliers with this ability have <sup>b</sup>potential market power<sup>Q</sup>. To investigate this, we require a mapping from nodal price to revenue.

The revenue, $R _ { i } ,$ for a particular generator is given by

$$
R _ {i} = z _ {i} \lambda_ {i}\tag{25}
$$

where $z _ { i }$ is its dispatch and $\lambda _ { i }$ is its nodal price. The derivative of the revenue of the ith generator, $R _ { i } ,$ to the nodal price of the jth generator, $\lambda _ { j } ,$ , at the operating point $( z ^ { * } , \lambda ^ { * } )$ is given by

$$
\frac {\mathrm{d} R _ {i}}{\mathrm{d} \lambda_ {j}} = \lambda_ {i} ^ {*} \frac {\mathrm{d} z _ {i}}{\mathrm{d} \lambda_ {j}} + z _ {i} ^ {*}\tag{26}
$$

We presented a method for calculating $\mathrm { d } z _ { i } / \mathrm { d } \lambda _ { j }$ in the previous section. Combining the derivatives for all the generators, we obtain a linear incremental/offer price model of the form

$$
\Delta R = A \Delta \lambda\tag{27}
$$

where DR and $\Delta \lambda$ represent incremental changes in revenue and offer price from the operating point, and A is the matrix whose elements are the derivatives defined in Eq. (26). Now, our task is to examine matrix A to determine which generators or groups of generators have potential market power.

Applying this to the test system we introduced in the previous section (Fig. 1), at the base case solution (Table 1), we obtain a matrix of revenue/nodal price sensitivities shown in Table 3 below.

This matrix has a two expected features. The negative diagonal entries indicate that no generator, acting alone, can simultaneously increase revenues by increasing its own offer price. Also, the sum of each row is positive. This means that if all generators raise their offer price in the same manner, then the revenues of each generator will increase.

Without detailed analysis we can confirm by visual inspection that generators 5 and 6 can increase their revenues by increasing their nodal prices. Equal increases in both, for example, will serve to do this. Furthermore, the nearly equal and opposite signs of the remaining elements in columns 5 and 6 suggest that this increase in revenues can be accomplished with little or no affect on the revenues of the remaining generators. Additional casual investigation of the matrix shows that generators 5 and 6 are the only pair of generators with this ability.

Now, we more formally characterize our potential market power criteria. To do so, we again separate the variables and partition the matrix to distinguish between generators in the load pocket who may enjoy market power and those external to the pocket (using the same <sup>b</sup>L<sup>Q</sup> and $\mathrm { ^ { 6 6 } F ^ { 7 } } { }$ subscripts as before):

Table 3  
Base case revenue/nodal price sensitivities

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>-3298</td><td>3231</td><td>31</td><td>65</td><td>52</td><td>-49</td></tr><tr><td>2</td><td>3219</td><td>-3695</td><td>244</td><td>263</td><td>315</td><td>-310</td></tr><tr><td>3</td><td>31</td><td>244</td><td>-544</td><td>308</td><td>-234</td><td>229</td></tr><tr><td>4</td><td>65</td><td>263</td><td>307</td><td>-597</td><td>-127</td><td>125</td></tr><tr><td>5</td><td>38</td><td>230</td><td>-170</td><td>-93</td><td>-160</td><td>173</td></tr><tr><td>6</td><td>-36</td><td>-229</td><td>169</td><td>92</td><td>175</td><td>-159</td></tr></table>

$$
\left[ \begin{array}{c} \Delta R _ {\mathrm{L}} \\ \Delta R _ {\mathrm{F}} \end{array} \right] = \left[ \begin{array}{c c} A _ {\mathrm{LL}} & A _ {\mathrm{LF}} \\ A _ {\mathrm{FL}} & A _ {\mathrm{FF}} \end{array} \right] \left[ \begin{array}{c} \Delta \lambda_ {\mathrm{L}} \\ \Delta \lambda_ {\mathrm{F}} \end{array} \right].\tag{28}
$$

Our criteria for potential market power:

1. To incrementally increase revenues by incrementally increasing nodal prices implies

$$
\Delta R _ {\mathrm{L}} = A _ {\mathrm{LL}} \Delta \lambda_ {\mathrm{L}} \geq 0\tag{29}
$$

for $\Delta \lambda _ { \mathrm { L } i } { \geq } 0$ (for every element of this vector).

2. To increase revenues without affecting the revenues of other generators requires

$$
\left[ \begin{array}{c} \Delta R _ {\mathrm{L}} \\ 0 \end{array} \right] = \left[ \begin{array}{c c} A _ {\mathrm{LL}} & A _ {\mathrm{LF}} \\ A _ {\mathrm{FL}} & A _ {\mathrm{FF}} \end{array} \right] \left[ \begin{array}{c} \Delta \lambda_ {\mathrm{L}} \\ \Delta \lambda_ {\mathrm{F}} \end{array} \right] \geq \left[ \begin{array}{c} 0 \\ 0 \end{array} \right]\tag{30}
$$

which simplifies to

$$
\Delta R _ {\mathrm{L}} = \left[ A _ {\mathrm{LL}} - A _ {\mathrm{LF}} A _ {\mathrm{FF}} ^ {- 1} A _ {\mathrm{FL}} \right] \Delta \lambda_ {\mathrm{L}} \geq 0.\tag{31}
$$

Furthermore, the same increase in price must simultaneously satisfy both conditions above. The purpose of the second condition is to take into account that an increase in nodal price will usually have some (at least small) affect on the revenues of the other generators. Consequently, a reaction by these other generators to equalize their revenues should not eliminate the revenue gains for those generators with market power (presuming that they do indeed have market power). Applying these criteria to our example, criterion 1 requires

$$
\left[ \begin{array}{c} \Delta R _ {5} \\ \Delta R _ {6} \end{array} \right] = \left[ \begin{array}{c c} - 1 6 0 & 1 7 3 \\ 1 7 5 & - 1 5 9 \end{array} \right] \left[ \begin{array}{c} \Delta \lambda_ {5} \\ \Delta \lambda_ {6} \end{array} \right].\tag{32}
$$

The positive values of $\Delta \lambda _ { 5 }$ and $\Delta \lambda _ { 6 }$ that satisfy this are described by

$$
\frac {1 6 0}{1 7 3} \Delta \lambda_ {5} \leq \Delta \lambda_ {6} \leq \frac {1 7 5}{1 5 9} \Delta \lambda_ {5}.\tag{33}
$$

The condition for criterion 2

$$
\left[ \begin{array}{c} \Delta R _ {5} \\ \Delta R _ {6} \end{array} \right] = \left[ \begin{array}{c c} 1 8. 1 & - 1. 4 \\ - 1. 5 & 1 3. 8 \end{array} \right] \left[ \begin{array}{c} \Delta \lambda_ {5} \\ \Delta \lambda_ {6} \end{array} \right]\tag{34}
$$

yields the constraint

$$
\frac {1 5}{1 3 8} \Delta \lambda_ {5} \leq \Delta \lambda_ {6} \leq \frac {1 8 1}{1 4} \Delta \lambda_ {5}\tag{35}
$$

The intersection of Eqs. (34) and (35) is completely limited by Eq. (34) and is shown graphically below in Fig. 2. Any increase of nodal prices in the shaded <sup>b</sup>win/win<sup>Q</sup> region will result in an increase in revenue for both generators.

We pause to mention that the second criterion used above is sensible and necessary. While not obvious from a cursory inspection, it is possible that an increase in nodal process at generators 3, 4 and 6 can result in increased revenues for those generators.

That would satisfy criterion 1. However, criterion 2 cannot be satisfied in that case and if the remaining generators were to react to equalize their revenues, generators 3, 4 and 6 would lose revenue. Both criteria need be satisfied.

Let us continue our examination of the load pocket generators 5 and 6. We have determined that they have the incremental ability to increase revenues and nodal prices which we deem gives them <sup>b</sup>potential market power<sup>Q</sup>. It does not necessarily mean that these generators are exploiting this potential. In particular, the shaded region shown in Fig. 2 is quite small and one can reasonably question whether this region can be found in practice. We discuss that further shortly, but first we introduce two measures to aid in the analysis of market power. One involves market prices and the other uses revenues.

Notions and measures of market power typically involve discussions and comparisons of prices. Along these lines, we consider a price-based relative market power (RMP) index that compares the OPF nodal prices to two reference prices that represent cases of no market power and extreme market power. (The initial concept for this measure is found in Ref. [9] and the refinement presented here is in Ref. [7].)

![](/api/attachments/K2RS4P2M/fulltext/images/d2ee34b63286caf67b6ee2d588a3a92f996f5b1df848550d4d2b7bdd149912ee.jpg)  
Fig. 2. Win/win region for price increases.

The no market power price, $\lambda _ { \mathrm { N M P } }$ is obtained by appropriately decreasing the offers of the generators with potential market power until the matrix of revenue/price sensitivities no longer identifies these generators as having potential market power. The high reference price, k<sub>HIGH</sub>, will typically be the price cap, if defined, or some other suitable high price otherwise. (One should confirm that the generators of interest continue to maintain potential market power at $\lambda _ { \mathrm { H I G H } } . )$ With the two reference prices for each generator of interest, relative market power can be defined as

$$
\mathrm{RMP} = \frac {\lambda - \lambda_ {\mathrm{NMP}}}{\lambda_ {\mathrm{HIGH}} - \lambda_ {\mathrm{NMP}}}\tag{36}
$$

where $\lambda$ is the nodal price for a generator. By focusing on price, this definition follows traditional investigations of market power; however, we emphasize that it does not require knowledge of <sup>b</sup>competitive price<sup>Q</sup> and it is calculable using available information. It is practical. The value of RMP should be between 0 and 1, the higher the value indicating the more market power.

Since we identify potential market power using revenues, and because increased revenue obtained through market power exploitation is of obvious interest, we introduce a relative measure of the revenue increase exploited by suppliers as <sup>b</sup>market power revenue gain<sup>Q</sup> (MPRG):

$$
\mathrm{MPRG} = \frac {R _ {\mathrm{actual}}}{R _ {\mathrm{NMP}}}\tag{37}
$$

where $R _ { \mathrm { N M P } }$ (no market power) is the revenue the generator would receive if the offer prices of the potential market power generators were adjusted until the incremental market power potential criteria are no longer satisfied. A RPMG greater than 1.0 indicates that some market power advantage is being used.

For the base case example we have considered, the no-market-power prices are $\lambda _ { 5 } { = } 4 3 . 2$ and $\lambda _ { 6 } { = } 4 2 . 2$ . The RMP and MPRG indices for generators 5 and 6 are shown in Table 4.

These numbers suggest that generators 5 and 6 are receiving significantly more revenues than would be expected if their generation was easily substitutable by the other generators present. These suppliers may indeed argue that they have higher costs, etc., and that their revenues are in order. However, we have demonstrated that they have the incremental ability to simultaneously increase revenues and price and that their revenues appear in excess relative to the remaining generators. The burden is then placed on them, if deemed necessary, to argue that their revenues are sensible. In doing so, they would minimally have to agree that they could not compete with a typical type of generator in the system if it were located at their present location, or if the transmission line capacities were increased.

Table 4  
Base case RMP and MPRG

<table><tr><td></td><td>G5</td><td>G6</td></tr><tr><td>RMP</td><td>0.32</td><td>0.32</td></tr><tr><td>MPRG</td><td>1.28</td><td>1.29</td></tr></table>

## 4. Market power experiment

The preceding discussion and example have involved a static system that was constructed to specifically highlight the load pocket and market power issues addressed in this paper. However, it has not used actual market participants to truly investigate their relative ability or inability to exploit market power potential. To investigate how the market might react to the physical system use here, we designed and performed experiments with human participants. Each of the six generators was operated by a different person (Cornell students). They were provided with the marginal cost information which were specifically designed to create a load pocket and system base case solution used in this paper. A price cap was imposed at US\$80/MW h. The participants were compensated in real dollars in proportion to their actual profit over the course of the experiment.

A repeated auction was performed with some randomness added to the load. It was observed that the market participants were able to exploit the potential market power and the nodal prices gradually increased over time. The dispatch and clearing prices after 75 rounds are shown in Table 5. Had the experiment continued it is expected that the load pocket generators would have eventually achieved the price cap.

Table 5  
Experiment dispatch and nodal prices

<table><tr><td></td><td>G1</td><td>G2</td><td>G3</td><td>G4</td><td>G5</td><td>G6</td></tr><tr><td>Dispatch (MW)</td><td>37.9</td><td>34.9</td><td>30.1</td><td>34.9</td><td>14.9</td><td>14.6</td></tr><tr><td>Price (US$/MW h)</td><td>48.5</td><td>48.7</td><td>48.5</td><td>48.6</td><td>72.0</td><td>70.0</td></tr></table>

Table 6  
Experimental RMP and MPRG

<table><tr><td></td><td>G5</td><td>G6</td></tr><tr><td>MPRG</td><td>0.70</td><td>0.66</td></tr><tr><td>MPRG</td><td>1.35</td><td>1.38</td></tr></table>

The nodal prices for all six generators increased but the nodal prices for generators 5 and 6 increased significantly more than the rest. The MPRG values for the experimental solution are presented in Table 6.

Comparing the larger values of RMP and MPRG in Table 6 to those in Table 4 suggests that generators 5 and 6 were able to exploit market power in the experiment. One must be careful making such comparisons. We emphasize that the RMP and MPRG use only information about the actual state of the system, and does not presume to know any base case or <sup>b</sup>competitive<sup>Q</sup> conditions. The calculation of the numbers depends on the nodal prices of all the generators in the system. Since all the generators in the experiment achieve higher nodal prices than the base case, the higher RMP and RMPG for generators 5 and 6 definitively show that they have exploited the market power afforded them by the load pocket. In practice such a comparison will not be available. We simply have the values of these indices at a particular point in time. It is a policy decision as to whether a particular value of RMP or MPRG is acceptable, or is too high. This policy decision is beyond the scope of this paper. Our research is intended to aid those who will monitor the system.

We close out this section with a discussion about the apparent ability of generators 5 and 6 to increase prices and revenues without collusion. We perform a more careful analysis to show that the domain (space) of possible price increases that result in increased revenues for both generators is small; a clear majority of price increase combinations will result in a loss of revenue for one of the generators. Nevertheless, we argue that the two generators will naturally find their <sup>b</sup>win/win<sup>Q</sup> combinations over time, based on price and revenue signals provided by the market.

Consider the revenue/offer price relation from Table 2 for generators 5 and 6 only:

$$
\left[ \begin{array}{c} \Delta R _ {5} \\ \Delta R _ {6} \end{array} \right] = \left[ \begin{array}{c c} - 1 6 0 & 1 7 3 \\ 1 7 5 & - 1 5 9 \end{array} \right] \left[ \begin{array}{c} \Delta \lambda_ {5} \\ \Delta \lambda_ {6} \end{array} \right]\tag{38}
$$

Setting $\Delta R _ { 5 } { = } 0$ and $\Delta R _ { 6 } { = } 0$ defines the <sup>b</sup>zerorevenue increase<sup>Q</sup> lines for the generators as functions of the their nodal prices:

$$
\begin{array}{l l} Z _ {5}: & - 1 6 0 \Delta \lambda_ {5} + 1 7 3 \Delta \lambda_ {6} = 0 \\ Z _ {6}: & 1 7 5 \Delta \lambda_ {5} - 1 5 9 \Delta \lambda_ {6} = 0 \end{array}\tag{39}
$$

These lines are shown graphically in Fig. 3. The zero revenue increase lines for generators 5 and 6 are denoted by $Z _ { 5 }$ and $Z _ { 6 } ,$ respectively. Above $Z _ { 5 } ,$ generator 5 will increase revenue and, below $Z _ { 6 } ,$ generator 6 will increase revenue. Between these lines lies a win/win region for which price increases will result in increased revenue for both generators. The win/win region is clearly small, yet in the experiment, people find this region. How is this possible without direction collusion?

The sequential market forms a dynamic process. At each round the market provides price and revenue signals. Acting only on these signals generators 5 and 6 will naturally tend towards operation in the win/win region, without explicit collusion.

Consider the price increase represented by <sup>b</sup>step 1<sup>Q</sup> in Fig. 4. This particular change in offers results in a price increase and revenue decrease for generator 5. Generator 6 experiences an increase in both price and revenue. For the following round, shown as <sup>b</sup>step 2<sup>Q</sup> in Fig. 4, a reasonable response is for generator 5 is to decrease price and for generator 6 to continue to increase price. Taken together, this has the combined effect of movement towards the win/win region.

![](/api/attachments/K2RS4P2M/fulltext/images/ad8297f21f88dca207419d6236df15189e1f28565ddb18f9ce9d766802425ba9.jpg)  
Fig. 3. Win/win region for price increases.

![](/api/attachments/K2RS4P2M/fulltext/images/2369a73bcbd570f4985eab1880771d7c4fefd691f6faf2eec3d62368b1b0f7c7.jpg)  
Fig. 4. Steps towards the win/win region.

The actual dynamics will depend on the price increments the generators employ, but with the feedback signals provided by the market it should be expected that the generators will eventually learn to exploit their market power. This is observed in the experiments with human participants.

## 5. Conclusions

In this paper, we have presented a spectral method for identifying generators located within a load pocket and tested their ability to take advantage of their location. The matrix of price elasticities is natural for this task because it emphasizes the relation between nodal price and dispatch. We seek generators, or groups of generators, with the ability to adjust price with no effect on dispatch. We continued our analysis by showing that the generators located within the load pocket also have the ability to increase revenues by raising nodal prices demonstrating what we call <sup>b</sup>potential market power<sup>Q</sup>. And finally, we quantified the extent to which this ability was being exploited through the relative market power and market power revenue gain metrics.

Common sense indicates that a group of generators with the ability to raise prices without affecting dispatch obvious has potential market power (since revenue is equal to the product of price and dispatch). Nevertheless, this definition of potential market power is perhaps the most important contribution of this paper. It is a practical approach to identifying participants with market power potential that requires only the information available to run the electricity market. Given the procedures used to run the electricity market and system, which are pre-defined and known by all participants, our approach determines those (individuals or groups) who can increase revenues by increasing their prices. We can, and should, apply this potential market power definition more generally to include situations that may not involve well-defined load pockets. And the definition of potential market power can be more general to include the ability to increase revenues through means other than energy price, such as capacity withholding and inputs into ancillary service markets. We simply identify those with the ability to increase revenues through actions that are known to be ineffective in a competitive market (i.e. raising prices, withholding capacity, etc.). We emphasize again that this approach is practical. It does not rely on unverifiable benchmarks such as <sup>b</sup>competitive price<sup>Q</sup>, and since it uses only the inputs and models that are actually used to clear and operate the electricity market and system, it is completely objective.

Once a market participant is shown to have potential market power, we need to quantify how much this potential is being used to their advantage. In this paper, we pursue a sensible approach by comparing the actual price and revenues to the prices and revenues at the point at which the potential for market power disappears. Again this is a practical, objective approach that uses only the models and rules that govern market operation.

We do not presume to dictate specifically how these metrics will be used and what values should be considered acceptable or unacceptable. We do feel that some market power ability should be tolerated and is in fact useful to provide economic signals to promote needed expansion to the system. On the other hand, abuse of market power cannot be tolerated by consumers and needs to be prevented. Deciding when to take action against market power exploitation is a policy decision that market monitors will need to make. Here, we are simply providing practical and objective tools to aid in these decisions.

In the last part of this paper, we argued that a group of two generators will almost certainly be able to exploit market power by finding a <sup>b</sup>win/win<sup>Q</sup> region in nodal prices. Without explicit collusion, using only individual market signals as feedback, they will naturally tend towards this region. Experiments with human participants confirm this response. Further research and experiments are warranted to study the dynamics of such situations and to consider more complicated scenarios involving more participants.

## Acknowledgments

This project is supported in part by the US Department of Energy through the Consortium for Electric Reliability Technology Solutions (CERTS) and in part by the National Science Foundation Power System Engineering Research Center (PSERC).

## References

[1] F.L. Alvarado, Market power: a dynamic definition, Proceedings of the Bulk Power Systems Dynamics and Control (Santorini, Greece), 1998 (Aug. 24–28).

[2] S. Borenstein, J. Bushnell, F. Wolak, Measuring market inefficiencies in California’s wholesale electricity industry, American Economic Review 96 (December 2002) based on Ref. [10].

[3] S.M. Harvey, W.W. Hogan, Identifying the Exercise of Market Power in California, 2001 (Dec. 28).

[4] P. Joskow, E. Kahn, A Quantitative Analysis of Pricing Behavior in California’s Wholesale Electricity Market During Summer 2000, 2001 (Mar.).

[5] P. Joskow, E. Kahn, Identifying the Exercise of Market Power: Refining the Estimates, 2001 (Jul. 5).

[6] P. Joskow, E. Kahn, A Quantitative Analysis of Pricing Behavior in California’s Wholesale Electricity Market During Summer 2000: The Final Word, 2002 (Feb. 4).

[7] B.C. Lesieutre, R.J. Thomas, T.D. Mount, A revenue sensitivity approach for the identification and quantification of market power in electric energy markets, IEEE Power Engineering Society General Meeting (Toronto), 2003 (Jul.).

[8] C. Murillo-Sanchez, R. Zimmerman, R.J. Thomas, Kirchhoff vs. competitive electricity markets: a few examples, in: IEEE Power Engineering Society Winter Meeting, 2001, vol. 3, IEEE, 2001, pp. 1256 – 1261.

[9] C.E. Murillo-Sanchez, S.M. Ede, T.D. Mount, R.J. Thomas, R.D. Zimmerman, An engineering approach to monitoring market power in restructured markets for electricity, The 24th Annual International Association for Energy Economics International Conference (Houston, TX), 2001 (Apr.).

[10] U.S. Department of Justice and the Federal Trade Commission, Horizontal Merger Guidelines http://www.usdoj.gov/atr/ public/guidelines/horiz\_book/hmg1.html, (issued Apr. 2, 1992, revised Apr. 8, 1997).

[11] U.S. Federal Energy Regulatory Commission, Initial Report on Company-Specific Proceedings and Generic Reevaluations; Published Natural Gas Price Data; and Enron Trading Strategies Fact-Finding Investigation of Potential Manipula-

tion of Electric and Natural Gas Prices, Docket PA02-2-000 (Aug. 2002).

[12] U.S. Federal Energy Regulatory Commission, Standard Market Design, NOPR RM01-12-000, §393 (Jul. 2002).

Bernard C. Leiseutre is a Staff Scientist at the Lawrence Berkeley National Laboratory. He received his BS, MS and PhD degrees in Electrical Engineering from the University of Illinois in 1986, 1988 and 1993, respectively. From 1993 to 2001, he served as an Assistant Professor and then Associate Professor of Electrical Engineering at MIT. He has held visiting Associate Professor positions at Caltech and Cornell University. His research interests include all aspects of the electric power, simulation techniques and nonlinear dynamics.

Robert J. Thomas is a Professor in Electrical and Computer Engineering at the Cornell University. His current research interests are broadly in the areas of analysis and control of nonlinear continuous and discrete-time systems with applications to largescale electric-utility systems.

Timothy D. Mount is a Professor in Applied Economics and Management at the Cornell University. His research interests include econometric modeling and policy analysis relating to the use of fuels and electricity, and to their environmental consequences (acid rain, smog and global warming). He is currently conducting research on the restructuring of markets for electricity and the implications for (1) price behavior in auctions for electricity, (2) the rates charged to customers and (3) the environment.
