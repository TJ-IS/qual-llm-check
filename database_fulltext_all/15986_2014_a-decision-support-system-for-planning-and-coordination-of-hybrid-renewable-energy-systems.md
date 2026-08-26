---
otero_id: 15986
otero_key: "EEK9WNF8"
title: "A decision support system for planning and coordination of hybrid renewable energy systems"
authors: "Kuo-Hao Chang"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.04.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for planning and coordination of hybrid renewable energy systems

Kuo-Hao Chang

Dept. of Industrial Engineering and Engineering Management, National Tsing Hua University, Hsinchu, Taiwan

a r t i c l e i n f o

Article history: Received 24 December 2013 Received in revised form 19 February 2014 Accepted 1 April 2014 Available online xxxx

Keywords: Hybrid renewable energy system Energy management Decision support systems Simulation optimization

## a b s t r a c t

Due to the growing concern about climate change and environmental sustainability, hybrid renewable energy system (HRES), which refers to a system that combines several renewable power sources and a conventional power generator to cover the power shortage when the renewable power is insuf<sup>fi</sup>cient, has gained more and more popularity over the decades. While the HRES is very attractive due to the minimal environmental and health impact compared to fossil fuels, the planning and coordination of HRES so as to supply stable power in a cost effective way are very challenging. This is mainly due to the unknown power demand, the highly volatile amount of renewable power supply and the complex topology of power network. In this paper, we model the planning and coordination of HRES in uncertain environments and develop an ef<sup>fi</sup>cient heuristic to solve the model. A decision support system(DSS) integrating the proposed model and the heuristic is developed as an ef<sup>fi</sup>cient decision tool to enable effective and ef<sup>fi</sup>cient energy management of HRES. The visualized outputs of DSS allow decision makers to gain better understanding about the management of HRES, facilitating the decision making process.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

With the United Nations predicting the world population growth from 6.6 billions in 2007 to 8.2 billions by 2030, demand for energy is expected to grow in an increasing speed over that period. According to [28], renewable energy sources, such as hydropower, solar and wind energies, only account for 19% of the total world energy demand in 2013. Renewable energies are green and clean resources. They are non-depletable, non-polluting and have minimal environmental and health impacts compared to fossil fuels. It has been long recognized that excessive fossil fuel consumption can lead to signi<sup>fi</sup>cant adverse impact on the environment through super<sup>fl</sup>uous carbon emissions, and in turn cause global climate change. While renewable energies are gaining more popularity over the decades, many countries are still resistant to increase the usage of the renewable energy, especially for the developing countries that are in dire need of power to sustain their economic growth. This is mainly due to the undesirable characteristics of renewable energies—their power supply is highly volatile and unpredictable; heavily relying on renewable energies is likely to result in instable power supply and could harm the economy.

Many countries are thus looking for other alternatives. Hybrid renewable energy system (HRES), which refers to a combination of at least one renewable energy source and a conventional power generator, is one viable and attractive choice that allows for the advantages of the renewable energies, while eliminating their disadvantages [7]. The HRES essentially utilizes renewable energies to ful<sup>fi</sup>ll the power demand and, if the power supply from the renewable energy sources is not suf<sup>fi</sup>cient, the conventional power generator is used to cover the power shortage, in turn ensuring that all power demand can be satis-<sup>fi</sup>ed. In fact, HRES has received a great deal of attention over the decade, not only because it is more environmental friendly, but also because it provides an excellent solution for electri<sup>fi</sup>cation of remote rural areas, where the grid extension is either dif<sup>fi</sup>cult or uneconomical.

Although HRES is attractive in many aspects, the planning and coordination of HRES so as to ful<sup>fi</sup>ll the power demand are very challenging. This is attributable to the unknown power demand of each area distributed in a wide region, the highly volatile renewable power supply over time, and the complex topology of power network that connects all power stations and demand areas. In addition, there are many other factors that are also linked to the effectiveness of HRES, such as properties of resources, ef<sup>fi</sup>ciencies of technologies, transmission loss, and sitespeci<sup>fi</sup>c characteristics of locations. The interaction of these factors, which is complex, nonlinear and unknown, further presents major challenges for the energy management of HRES. There is a need to develop an effective decision tool that can aid in the decision making when the HRES is intended to be implemented.

In this paper, as shown in Fig. 1, we consider a region that includes several demand areas and multiple power stations to supply all demand areas with power. There is an electricity grid that connects all power stations and demand areas to allow for power transmission, either between stations or from stations to areas, with uncertain power transmission loss to satisfy the power demand of each area. We assume that each power station includes two kinds of renewable energy sources—the solar and wind power generators, and a conventional power generator that produces power whenever the renewable power is insuf<sup>fi</sup>cient to meet the demand. Further each power station has a power storage for storing surplus power when the power supply is greater than the power demand. The research problem is to decide on the appropriate number of solar and wind power generators of each power station so as to achieve the minimum expected total cost, while satisfying the power demand of each area.

![](/api/attachments/EEK9WNF8/fulltext/images/9804db906aa691e281e6f5a05ac3303adc271b355d049f5fac0e253821561896.jpg)  
Fig. 1. An illustration for the power transmission network.

We propose a stochastic optimization model to characterize the decision problem. In particular, the model emulates the power generation, allocation and transmission within the HRES, taking into account the uncertainty that could affect the HRES, including the power demand, the renewable power supply, and the power transmission loss occurred when transmitting power within the HRES. The objective function is de<sup>fi</sup>ned as the minimum expected total cost, where the expectation is taken with respect to all uncertainty mentioned above. One challenge about the proposed model, however, is to locate its optimal solution due to that the obiective function is not analytically available, which is mainly because it involves many factors, profound uncertainty and their complex interactions. To overcome the dif<sup>fi</sup>culty, we propose a Monte Carlo simulation model, along with a sample size scheme, to obtain estimates of the objective function. Then, based on the developed simulation model, we propose a simulation optimization method, called metamodel-based simulated annealing method (MSA), to enable the ef<sup>fi</sup>cient derivation of the optimal solution. Finally, we integrate the proposed model and the solution methodology into a decision support system (DSS) as an ef<sup>fi</sup>cient decision tool for analyzing and visualizing impacts of different designs of HRES, and facilitating the decision making process. More details about the proposed methodology and the DSS will be introduced in later sections.

The remainder of this article is organized as follows. In Section 2, we review the existing literature related to this research. In Section 3, we present the mathematical model that characterizes the planning and coordination of HRES. In Section 4, we introduce the analysis methodology, MSA, developed to solve the proposed model. In Section 5, we compare the performance of MSA and other two existing algorithms based on a variety of simulated problems. In Section 6, we develop a decision support system (DSS) that integrates the proposed model and the heuristic to allow decision makers to obtain better understanding about the energy management of HRES. We conclude with future research in Section 7.

## 2. Literature review

In this section, we review the previous work related to the planning of HRES. In the literature, the feasibility and performance studies about the HRES in various forms have been extensively conducted, e.g., [7,16, 12,14]. In particular, Gorgopoulou et al. [18] proposed a multicriteria decision aid method to examine a particular case study in a Greek island and pointed out some aspects that are crucial in reaching a compromise in regional energy planning problems. Nehrir et al. [27] developed a computer-based approach for evaluating the general performance of stand-alone PV/wind generating systems. Giraud and Salameh [16] discussed the steady-state performance of a grid-connected rooftop hybrid wind–solar power system with battery storage. The system reliability, power quality, loss of supply, and effects of the randomness of the wind and the solar radiation on system design are also discussed. Alarcon-Rodriguez et al. [2] provided a timely review of the state-ofthe-art in multi-objective distributed energy resources planning, and discussed in detail the challenges, trends and latest developments in this <sup>fi</sup>eld. Hunt et al. [19] presented a new integrated tool and a decision support framework to handle complex decision making problems in the UK energy sector.

Some analysis is also presented for hybrid renewable energy systems. For example, Elhadidy [12] presented a techno-economic study to design a hybrid solar photo-voltaic–wind domestic power generating system for one site of the western coast of India. It was shown that the optimum system would be able to supply 84.16% of the annual electrical energy requirement of the site. Celik [10] proposed a technique to analyze the performance of the autonomous small-scale PV and wind hybrid energy systems. Kolhe et al. [22] provided an analysis of the performance of a photovoltaic array that complements the power output of a wind turbine generator in a stand-alone renewable energy system based on hydrogen production for long-term energy storage. Elhadidy and Shaahid [14] presented an analysis of the performance of hybrid PV/wind energy system with hydrogen energy storage for long-term utilization. The impact of variation of battery storage capacity on hybrid power generation is also explored. Rentizelas et al. [28] investigated the effect of various scenarios for emission allowance price and provided directions on which technologies are most probable to dominate the market in the future. Xydis [33] studied the wind potential of Kythira Island and provided a techno-economic analysis aiming at identifying

Please cite this article as: K.-H. Chang, A decision support system for planning and coordination of hybrid renewable energy systems, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.001

the optimum solution for the proposed Wind Farms (WF) to be installed so that this isolated island could be interconnected to the mainland.

Some research has also been done on determining the optimum size of hybrid PV/wind energy system, e.g., [17,8,9,1]. In particular, Borrowsy and Salameh [8] developed a methodology for calculating the optimum size of a PV array for a stand-alone hybrid wind/PV power system. Moreover, Chedid and Saliba [11] proposed a new formulation for optimizing the design of an autonomous wind–solar–diesel–battery–energy system. The formulation employed linear programming techniques to minimize the average production cost of electricity while meeting the load requirements in a reliable manner. Morgan et al. [25] outlined several major enhancements made to autonomous renewable energy systems (ARES), where battery is modeled with great precision. Seeling-Hochmuth [29] presented a method to jointly determine the sizing and operation control of hybrid-PV systems. The outlined approach can <sup>fi</sup>nd an optimum operation strategy for a hybrid system by carrying out a search through possible options for the system operation control. Ai et al. [1] presented a method to calculate the optimum size of hybrid PV/wind energy system, where the performance was compared on hourly basis. Bala and Siddique [4] presented an optimal design of a solar PV–diesel hybrid mini-grid system for a <sup>fi</sup>shing community in Sandwip, an isolated island in Bangladesh.

Other optimization approaches used for designing the hybrid PV/wind energy system in the most cost effective way include, for example, linear programming [21] probabilistic analysis [20,3]; iterative technique [21]; dynamic programming [26]; and multi-objective method [34]. In particular, Elhadidy and Shaahid [13], and Shaahid and Elhadidy [30] detailed a variety of aspects of PV, wind, and battery-based hybrid system including optimal sizing and operation. Karaki et al. [20] presented a probabilistic assessment for an autonomous solar–wind energy conversion system (SWECS) composed of several wind turbines (wind farm), several PV modules (solar park), and a battery storage feeding a load. Bernal-Agustí and R. Dufo-López [6] applied simulation and optimization techniques to generate better designs of stand-alone hybrid systems. Ferrer-Martí [15] proposed a mathematical programming model to optimize the design of hybrid wind–PV systems that solve the location of the wind–PV generators and the design of the microgrids.

Although extensive research has been done for determining the optimum number of PV/wind power generators, most of the models are deterministic ones where the parameters are essentially treated as known constants. Without taking the uncertainty into consideration, the resulting solution may suffer from poor performance in practice. On the other hand, some probabilistic models are proposed to predict the performance of HRES. While these models are good at answering what-if questions, they did not address the optimization problem regarding the energy management of HRES. Our proposed model bridges the gap. By taking into account the randomness of the unknown parameters and the complex interaction among factors, the resulting solution of the proposed model is expected to be of better quality and applicability in practice.

## 3. The proposed model

Consider a region that has M power stations and N demand areas. Let the unit cost of solar and wind power generators be $C _ { s }$ and $C _ { w } ,$ respectively, and the unit power generation cost due to the use of conventional power generators be $C _ { c } .$ We assume power transmission will inevitably yield power loss and the percentage of power loss from stations i to j and from station i to area k are $\eta _ { i j }$ and $\eta _ { i k } ,$ respectively. Let the planning horizon be L periods. Some notations associated with the mathematical model are introduced in Table 1.

Main decision model:

$$
\begin{array}{c} \operatorname{Min} _ {\mathrm{x}} \operatorname{E} [ G (\mathbf {x}, \omega) ] \\ 0 \leq x _ {s i} \leq \overline {{x}} _ {s i}, 0 \leq x _ {w i} \leq \overline {{x}} _ {w i} \\ i = 1, \dots , M \end{array}\tag{1}
$$

where $\mathbf { x } = [ x _ { s 1 } , x _ { s 2 } , . . . , x _ { s M } , x _ { w 1 } , x _ { w 2 } , . . . , x _ { w M } ]$ denotes the decision vector where each element refers to the number of solar/wind power generators selected to be installed in each power station; $\cdot \bar { x } _ { s i }$ and $\overline { { x } } _ { w i }$ correspond to the upper bounds of the number of the solar and wind power generators, respectively; $\omega = [ P _ { s i } , P _ { w i } , d _ { k l } , \eta _ { i j } , \eta _ { i k } ] _ { \{ 1 \leq i , j \leq M , 1 \leq k \leq N , 1 \leq l \leq L \} }$ refers to the random vector that includes all randomness underlying the problem. In particular, $G ( \mathbf { x } , \omega ) = \mu ( \mathbf { x } ) + \lambda ( \mathbf { x } , \omega ) + h ( \mathbf { x } , \omega )$ represents the total cost, which is constituted by: (1) the installation cost of renewable energy sources $\mu ( \mathbf { x } )$ , (2) the additional power generation cost, $\lambda ( \mathbf { x } , \omega )$ , due to the use of conventional power generator, and (3) the power storage cost, $h ( \mathbf { x } , \omega )$ , when there is surplus power to be stored. Note that the total cost is a function of the decision vector x and the random vector ω and thus is random as well. The objective function is in an expectation form and can be written as $\mu ( \mathbf { x } ) + \operatorname { E } [ \lambda ( \mathbf { x } , \omega ) ] + \operatorname { E } [ h ( \mathbf { x } , \omega ) ]$ . It is remarkable that, over the whole planning horizon, the installation cost is a one-time charge and can be calculated by $\mu ( \mathbf { x } ) = C _ { s } \sum \sp M _ { i } = 1 x _ { s i }$ + $C _ { w } \sum _ { i } ^ { M } { \textstyle \ i = 1 \ X _ { w i } }$ . The additional power generation cost $\lambda ( \mathbf { x } , \omega )$ and the power storage cost $h ( \mathbf { x } , \omega )$ , however, are incurred at each period l and will be accumulated till the end of the planning horizon.

A few words about the main model. This model seeks the optimal number of solar and wind power generators so as to achieve minimum expected total cost over the whole planning horizon. The determination of the number of the solar and wind power generators is actually a trade-off. Speci<sup>fi</sup>cally, if the number of solar and wind power generators is selected large, a higher installation cost is required. However, because suf<sup>fi</sup>cient renewable power will be generated by a large number of renewable power generators, it is more likely that there will be less power shortage and thus a less additional conventional power generation cost will be incurred subsequently. On the other hand, if the number of solar and wind power generators is selected small, a less installation cost is required. However, because the generated renewable energy may be insuf<sup>fi</sup>cient to satisfy the power demand, it is likely that there would be a large power shortage, which would in turn incur more conventional power generation cost subsequently.

To obtain an estimate for the additional power generation cost E[λ(x,ω)] and the power storage cost E[h(x,ω)], we propose the following model:

Power coordination model (for any period l):

$$
\begin{array}{l} \operatorname{Min} _ {b _ {i}, z _ {i j}, y _ {i k}} \sum_ {i = 1} ^ {M} C i E _ {i l} \\ \text { s.t. } \quad \sum_ {i = 1} ^ {M} \eta_ {i k} y _ {i k} \geq d _ {k l}, \text {   for   } k = 1, \dots , N \end{array}\tag{2}
$$

$$
\widetilde {I} _ {i l - 1} + b _ {i} + \sum_ {j \neq i} \eta_ {j i} z _ {j i} + E _ {i l} \geq \sum_ {k = 1} ^ {N} \eta_ {i k} y _ {i k} + \sum_ {j \neq i} \eta_ {i j} z _ {i j} \text { for } i = 1, \dots , M\tag{3}
$$

$$
\begin{array}{c} b _ {i} = P _ {s i} x _ {s i} + P _ {w i} x _ {w i} \text { for } i = 1,..., M \\ y _ {i k} \geq 0, z _ {i j} \geq 0, E _ {i l} \geq 0 \text { for } i, j = 1,..., M \text { and } k = 1,..., N. \end{array}\tag{4}
$$

For any period l, the power coordination model seeks to minimize the additional power generation cost by transmitting the generated power to the demand areas in the most ef<sup>fi</sup>cient way. In the power coordination model, Eq. (2) ascertains that the power supply, either from the solar/wind power generators or from the conventional power generator, should be at least as much as the power demand of area k when taking the power transmission loss into consideration. Eqs. (3) and (4) require that for each power station i, the amount of power at hand, including the renewable power supply, the additional power generated from the conventional power generator, the power obtained from other power stations and the amount of power stored in the power storage previously, should be equal to or greater than the power out<sup>fl</sup>ow.

Please cite this article as: K.-H. Chang, A decision support system for planning and coordination of hybrid renewable energy systems, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.001

In this power coordination model, the power demand of each area at each period $d _ { k l }$ the power supply of the solar/wind power generators at each power station $P _ { s i } , P _ { w i }$ and the power transmission loss $\eta _ { i j } , \eta _ { i k }$ are treated as random variables. The resulting optimal solution $b _ { i } ^ { * } , z _ { i j } ^ { * } , y _ { i k } ^ { * }$ and its corresponding objective value $\sum { _ i ^ { - } } _ { = 1 } ^ { \bar { M } } C i E _ { i l } ^ { * }$ are thus a function of x and ω and are random as well. Speci<sup>fi</sup>cally, for one given pair of $( { \bf x } , \omega )$ , the model would yield one value of $\sum { _ i ^ { M } } _ { = 1 } ^ { M } C i E _ { i l } ^ { * } ,$ which then serves as one observation of the additional power generation cost for the period l. Also, the amount of power needing to be stored at the power station i can be calculated by

$$
\widetilde {I} _ {i l} = \max \left\{0, b _ {i} ^ {*} + \sum_ {j \neq i} \eta_ {j i} z _ {j i} ^ {*} + \widetilde {I} _ {i l - 1} + E _ {i l} ^ {*} - \left(\sum_ {k = 1} ^ {N} y _ {i k} ^ {*} + \sum_ {j \neq i} z _ {i j} ^ {*}\right) \right\}
$$

and the power storage cost for the period l is $\textstyle \sum _ { i = 1 } ^ { M } { \tilde { r } } I _ { i l } ,$ which serves as <sup>¼</sup>one observation for the power storage cost for the period l. Based on the above discussion, the accumulated additional power generation cost and the power storage cost for the whole planning horizon can be estimated as follows:

$$
\hat {\lambda} (\mathbf {x}, \omega) = \sum_ {l = 1} ^ {L} \sum_ {i = 1} ^ {M} C i E _ {i l} ^ {*}\tag{5}
$$

$$
\hat {h} (\mathbf {x}, \omega) = \sum_ {l = 1} ^ {L} \sum_ {i = 1} ^ {M} r \tilde {I} _ {i l}.\tag{6}
$$

## 4. Solution methodology

In this section, we develop an ef<sup>fi</sup>cient heuristic to solve the proposed model and obtain the optimal number of solar and wind power generators. The developed methodology, called metamodel-based simulated annealing (MSA), is a simulation optimization method. It possesses the basic framework of the traditional simulated annealing (SAN) [32], but is further adapted by incorporating a Monte Carlo approach, along with a sample size scheme, to enable quality estimation of the objective function, and a metamodel-based search strategy to accelerate the algorithm convergence.

The traditional SAN is a random-search-based algorithm developed based on an observation of the cooling process of a liquid or solid in which molecules have higher mobility at high temperatures and the mobility is lost or declines as the temperature decreases. This concept has been successfully applied in deterministic optimization to <sup>fi</sup>nd the lowest (or highest) value of the objective function. However, one disadvantage of SAN is that because it randomly selects a solution at each iteration, it may require an excessive number of iterations to <sup>fi</sup>nd the true optimal solution, especially when the parameter space is very large. For example, if a problem has 20 decision variables, and the value of each decision variable can vary from 1 to 50, it could take $5 0 ^ { 2 0 }$ iterations to <sup>fi</sup>nd the true optimal solution. The proposed MSA addresses this issue by using a metamodel-based search strategy, which basically builds a metamodel to represent the functional behavior of the objective function and solves for the optimal solution of the built metamodel, subject to the experimental design. Because MSA explores a region of the parameter space, rather than one point, at a time, the optimal solution can be located in a more ef<sup>fi</sup>cient manner.

## 4.1. Estimation of the additional power generation cost and the power storage cost

Because the additional power generation cost and the power storage cost do not have an analytical form, we propose a simulation model to obtain an estimate. The basic idea is outlined as follows. As shown in

![](/api/attachments/EEK9WNF8/fulltext/images/3bfe43c942ef1539c7bd87f6da6bdcafc9a6117dfbe870bb8dfe637fb9d334f0.jpg)  
Fig. 2. Estimating the objective function by Monte Carlo simulation.

Fig. 2, for one given solution x, N's ω is generated according to their corresponding distributions, and the power coordination model is solved N times. Using Eqs. (5) and (6), N observations of λ<sup>^</sup> x; ω and $\hat { h } ( \mathbf { x } , \omega )$ can be produced. The additional power generation cost and the power storage cost are then estimated by the sample average of N observations.

To ensure the estimation quality, we propose the following sample size scheme to determine the sample size N using a Signal-to-Noise concept, where the signal represents the true function value $g ( \mathbf { x } _ { k } )$ (the expected additional power generation cost or the expected power storage cost) and the noise represents the associated standard deviation $\sigma ( \mathbf { x } _ { k } )$ . The sample size $N _ { k }$ is determined as follows:

$$
\left| \frac {g (\mathbf {x} _ {k})}{\sigma (\mathbf {x} _ {k}) / \sqrt {N _ {k}}} \right| \geq c.\tag{7}
$$

In Eq. (7), c is determined based on the computational budget but is suggested to be no less than 5, by which the sample size $N _ { k }$ is selected such that the average simulation output per input value x is within 20% of the true function value. Note that in a stochastic environment, both $g ( \mathbf { x } _ { k } )$ and $\sigma ( \mathbf { x } _ { k } )$ are both unknown and should be estimated.

The detailed procedure for estimating $\mathbb { E } [ \lambda ( \mathbf { x } , \omega ) ]$ ] and $\mathbb { E } [ h ( { \bf x } , \omega ) ]$ is presented as follows. Note that for each observation, it is required to generate one $\omega = [ P _ { s i } , P _ { w i } ,$ d<sub>kl</sub>, η<sub>ij</sub>, η<sub>ik</sub>]<sub>{1</sub> $\leq i , j \leq M , 1 \leq k \leq N , 1 \leq l \leq L \}$ according to the corresponding distribution, solve the power coordination model and obtain the observation through Eqs. (5) and (6).

• Step 1. Take $N _ { 0 }$ observations to estimate $g ( \mathbf { x } _ { k } )$ and $\sigma ( \mathbf { x } _ { k } )$

• Step 2. Determine the required sample size $N _ { k }$ based on $\operatorname { E q . } \left( 7 \right)$

• Step 3. If $N _ { 0 } > N _ { k }$ estimate $\mathbb { E } [ \lambda ( \mathbf { x } , \omega ) ]$ and $\mathbb { E } [ h ( { \bf x } , \omega ) ]$ by the sample average of N observations. Otherwise, take extra $N _ { k } - N _ { 0 }$ observations and estimate $\mathbb { E } [ \lambda ( \mathbf { x } , \omega ) ]$ and $\mathbb { E } [ h ( { \bf x } , \omega ) ]$ ] by the sample average of $N _ { k }$ observations.

Note that in Step 1, in order to obtain a reasonably accurate estimate for $g ( \mathbf { x } _ { k } )$ and $\sigma ( \mathbf { x } _ { k } )$ , N is suggested to be no less than 5.

## 4.2. Metamodel-based simulated annealing method

The central idea that MSA capitalizes on building metamodels to represent the objective function within the experimental region and then performing optimization in light of the built metamodel, which is either a <sup>fi</sup>rst- or second-order polynomial function. Let the current best solution be $\mathbf { x } _ { k } = [ x _ { s 1 } , . . . , x _ { s M } , x _ { w 1 } , . . . , x _ { w M } ]$ . For each iteration, the experimental region is de<sup>fi</sup>ned as

$$
B (\mathbf {x} _ {k}, \Delta) = \left\{\mathbf {x} \in \mathbb {R} ^ {p}: \| \mathbf {x} - \mathbf {x} _ {k} \| \leq \Delta \right\},\tag{8}
$$

where $| | \cdot | |$ denotes the Euclidian norm and $\Delta > 0$ is the radius of the experimental region.

The full MSA method is given as follows.

• Step 0. Set the iteration counter $k = 0 .$ . Select an initial temperature $T _ { 0 } ,$ cooling coef<sup>fi</sup>cient $\rho ,$ size of experimental region $\Delta ,$ and an initial solution $\mathrm { X } _ { 0 } .$

• Step 1. Build a metamodel to represent the objective function within the experimental region (Section 4.2.1).

Please cite this article as: K.-H. Chang, A decision support system for planning and coordination of hybrid renewable energy systems, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.001

• Step 2. Solve for the optimal solution of the metamodel subject to the experimental region x<sup>∗</sup> (Section 4.2.2).

• Step 3. Obtain estimates $\hat { Y } _ { k }$ and $\hat { Y } _ { k } ^ { * }$ for $\operatorname { E } [ G ( \mathbf { x } _ { k } , \omega ) ]$ and $\operatorname { E } [ G ( \mathbf { x } _ { k } ^ { * } , \omega ) ]$ respectively.

• Step 4. If $\hat { Y } _ { k } - \hat { Y } _ { k } ^ { * } { > } 0$ , accept $\mathbf { x } _ { k } ^ { * }$ and let $\mathbf { x } _ { k + 1 } = \mathbf { x } _ { k } ^ { * } .$ Otherwise, use the Metropolis criterion to determine whether to accept x<sup>∗</sup>. If x<sup>∗</sup> is accepted, let $\mathbf { x } _ { k + 1 } = \mathbf { x } _ { k } ^ { * }$ and go to Step 7. Otherwise, go to Step 6.

• Step 5. Randomly select a solution x<sup>∗</sup> in the parameter space. Follow Steps 3 and 4 to estimate $\hat { Y } _ { k } ^ { * } .$ . If $\hat { Y } _ { k } - \hat { Y } _ { k } ^ { * } > 0$ , accept x<sup>∗</sup> and let ${ \bf x } _ { k + 1 } =$ $\mathbf { x } _ { k } ^ { * } .$ Otherwise, use the Metropolis criterion to determine whether to accept x<sup>∗</sup>. If x<sup>∗</sup> is accepted, let $\mathbf { x } _ { k + 1 } = \mathbf { x } _ { k } ^ { * }$ . Otherwise, repeat Step 6 until the solution is accepted.

• Step 6. Repeat Steps 1–6 for some period until either the budget of function evaluations allocated for that T has been used or the system reaches some state of equilibrium.

• Step 7. Let $T = \rho T _ { 0 }$ and return to Step 1. Continue the process until the total budget for function evaluations has been used or some convergence has been satis<sup>fi</sup>ed. Return the <sup>fi</sup>nal solution.

Inheriting from the SAN, the Metropolis criterion embedded in the MSA allows the algorithm to accept inferior solutions in order to ensure that the new solution, even if it seems to be worse than the current solution, can still have a positive probability of being accepted. The Metropolis criterion employed in MSA is described as follows. Let U denote a uniform (0, 1) random variable. If U satis<sup>fi</sup>es

$$
U \leq \exp \left(\frac {\hat {Y} _ {k} - \hat {Y} _ {k} ^ {*}}{c _ {b} T}\right),\tag{9}
$$

the new solution x<sup>∗</sup> is accepted; otherwise, it is rejected. Here $c _ { b } > 0$ is the Boltzmann constant and T is the temperature of the system. Therefore, when $\hat { Y } _ { k } - \hat { Y } _ { k } ^ { * } { < } 0$ , in light of Eq. (9), the probability for the new solution to be accepted is proportional to the quality of the new solution. Speci<sup>fi</sup>cally, when the estimate of the new solution is close to that of the current solution, the new solution has a higher probability of being accepted; otherwise, the new solution has a lower probability of being accepted.

Three remarks deserve to be made about the proposed MSA algorithm. First, the MSA algorithm is to search for the optimal solution in a local area by approximating the objective function with a metamodel. Because the optimal solution is the best solution within the local area, the algorithm essentially explores a region rather than a point at one time. As will be shown later, the computational gain due to the metamodel-based search strategy increases with the problem size. Second, whenever the metamodel-based search cannot <sup>fi</sup>nd a satisfactory solution in the local area, the MSA turns to random search, which allows the algorithm to explore better solutions in the whole parameter space and thus avoid getting trapped in a local area. Third, because the MSA method incorporates a sample size scheme that is effective in governing the noise in the function measurement, the risk of wrongly accepting a solution of poor quality is reduced. The traditional SAN, on the other hand, lacks this mechanism and thus can possibly move in the wrong direction, <sup>fi</sup>nally failing to converge.

Notations used in the proposed model.

<table><tr><td> $E_{il}$ </td><td>The amount of power generated by conventional power generators in power station i at period l</td></tr><tr><td> $C_i$ </td><td>The generation cost of unit conventional power in power station i</td></tr><tr><td> $z_{ij}$ </td><td>The amount of power transmitted from power station i to power station j</td></tr><tr><td>r</td><td>The power storage cost per unit power per period</td></tr><tr><td> $y_{ik}$ </td><td>The amount of power transmitted from station i to area k</td></tr><tr><td> $P_{si}$ </td><td>The amount of power generated by solar generators in power station i</td></tr><tr><td> $P_{wi}$ </td><td>The amount of power generated by wind generators in power station i</td></tr><tr><td> $b_i$ </td><td>The amount of total power generated by the renewable energy sources in power station i</td></tr><tr><td> $d_{kl}$ </td><td>The power demand of area k at period l</td></tr><tr><td> $\widetilde{I}_{il}$ </td><td>The amount of power stored in power station i at the end of period l</td></tr></table>

Performance comparison when variance of noise is <sup>fi</sup>xed.

<table><tr><td rowspan="2"></td><td colspan="3">Competing algorithms</td></tr><tr><td>MSA</td><td>SAN</td><td>MNM</td></tr><tr><td colspan="4">ER</td></tr><tr><td>4D</td><td>0.83 (0.35)</td><td>2.14 (1.35)</td><td>3.30 (1.71)</td></tr><tr><td>12D</td><td>1.35 (0.81)</td><td>3.56 (2.11)</td><td>4.81 (2.47)</td></tr><tr><td>16D</td><td>1.77 (1.08)</td><td>6.23 (2.98)</td><td>6.43 (3.40)</td></tr><tr><td colspan="4">FR</td></tr><tr><td>4D</td><td>0.63 (0.14)</td><td>2.23 (1.21)</td><td>2.04 (1.17)</td></tr><tr><td>12D</td><td>0.98 (0.54)</td><td>3.34 (2.67)</td><td>3.82 (1.12)</td></tr><tr><td>16D</td><td>1.23 (0.86)</td><td>4.47 (3.52)</td><td>4.88 (2.17)</td></tr><tr><td colspan="4">PBS</td></tr><tr><td>4D</td><td>1.42 (0.65)</td><td>2.56 (1.27)</td><td>4.68 (2.24)</td></tr><tr><td>12D</td><td>1.52 (1.17)</td><td>3.78 (2.12)</td><td>6.16 (3.13)</td></tr><tr><td>16D</td><td>1.98 (1.88)</td><td>4.13 (2.98)</td><td>7.21 (4.10)</td></tr></table>

## 4.2.1. Metamodel construction

For any iteration k, MSA starts by employing resolution III fractional factorial designs (FFD) within the experimental region to build a <sup>fi</sup>rstorder model. Whenever the curvature test indicates that the <sup>fi</sup>rstorder model is no longer a good <sup>fi</sup>t, MSA augments the FFD to central composite designs (CCD) and <sup>fi</sup>ts a second-order model. Details about the curvature test and the construction of resolution III FFD and CCD can be found in [23].

Suppose the current solution is $\mathbf { x } _ { k } .$ Let the <sup>fi</sup>rst- and second-order models be

First‐order model

$$
r _ {k} (\mathbf {x}) = \hat {g} _ {k} (\mathbf {x} _ {k}) + \widehat {\nabla} g _ {k} ^ {T} (\mathbf {x} _ {k}) (\mathbf {x} - \mathbf {x} _ {k})\tag{10}
$$

Second‐order model

$$
\begin{array}{r} r _ {k} (\mathbf {x}) = \hat {g} _ {k} (\mathbf {x} _ {k}) + \widehat {\nabla} g _ {k} ^ {T} (\mathbf {x} _ {k}) (\mathbf {x} - \mathbf {x} _ {k}) \\ + \frac {1}{2} (\mathbf {x} - \mathbf {x} _ {k}) ^ {T} \widehat {H} _ {k} (\mathbf {x} _ {k}) (\mathbf {x} - \mathbf {x} _ {k}), \end{array}\tag{11}
$$

where $\hat { g } _ { k } ( \mathbf x _ { k } ) , \hat { \nabla } g _ { k } ( \mathbf x _ { k } ) ,$ , and $\widehat { H } _ { k } ( \mathbf { x } _ { k } )$ are the estimates of the function value, <sup>ð Þ ð Þ ð Þ</sup>gradient, and Hessian of the center point $\mathbf { x } _ { k }$ at the kth iteration.

Let X be the design matrix of FFD, and Y is the response vector where each element represents one estimate of the expected total cost at

Performance comparison when variance of noise is varying.

<table><tr><td rowspan="2"></td><td colspan="3">Competing algorithms</td></tr><tr><td>MSA</td><td>SAN</td><td>MNM</td></tr><tr><td colspan="4">ER</td></tr><tr><td>4D</td><td>1.23 (0.75)</td><td>3.44 (1.92)</td><td>2.76 (1.92)</td></tr><tr><td>12D</td><td>2.34 (1.78)</td><td>4.56 (3.11)</td><td>3.81 (2.47)</td></tr><tr><td>16D</td><td>2.89 (1.98)</td><td>5.12 (4.12)</td><td>4.29 (4.12)</td></tr><tr><td colspan="4">FR</td></tr><tr><td>4D</td><td>0.94 (0.74)</td><td>3.33 (2.21)</td><td>3.34 (2.97)</td></tr><tr><td>12D</td><td>1.28 (0.93)</td><td>5.08 (3.76)</td><td>5.23 (4.84)</td></tr><tr><td>16D</td><td>1.94 (1.23)</td><td>6.86 (4.52)</td><td>6.28 (5.17)</td></tr><tr><td colspan="4">PBS</td></tr><tr><td>4D</td><td>1.85 (0.98)</td><td>3.16 (2.81)</td><td>3.68 (2.83)</td></tr><tr><td>12D</td><td>2.18 (1.47)</td><td>4.86 (3.12)</td><td>4.71 (3.43)</td></tr><tr><td>16D</td><td>2.79 (2.12)</td><td>8.13 (4.71)</td><td>6.34 (4.29)</td></tr></table>

Please cite this article as: K.-H. Chang, A decision support system for planning and coordination of hybrid renewable energy systems, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.001

![](/api/attachments/EEK9WNF8/fulltext/images/32d52247c4324e0735160ea0ca26a818dfc7954e037357666483d4547273287a.jpg)  
Fig. 3. Interface of the DSS.

different designs of HRES. $\hat { g } _ { k } ( { \mathbf x } _ { k } )$ and $\widehat { \nabla } g _ { k } ( { \mathbf x } _ { k } )$ can be estimated by the <sup>ð Þ</sup>ordinary least squares as follows:

$$
\left(\mathbf {X} ^ {T} \mathbf {X}\right) ^ {- 1} \mathbf {X} ^ {T} \mathbf {Y}.\tag{12}
$$

It is remarkable that when second-order models are needed, X is augmented to CCD, and Eq. (12) can be used to estimate $\hat { g } _ { k } ( { \mathbf x } _ { k } )$ $\widehat { \nabla } g _ { k } ( { \mathbf x } _ { k } )$ , and $\widehat { H } _ { k } ( \mathbf { x } _ { k } )$ simultaneously.

4.2.2. Solving for the optimal solution within the experimental region

When the metamodel is produced, the MSA solves for the optimal solution of the metamodel subject to the experimental region. The problem is de<sup>fi</sup>ned as

$$
\mathbf {x} _ {k} ^ {*} \in \operatorname{argmin} \left\{r _ {k} (\mathbf {x}): x \in \mathcal {B} \left(\mathbf {x} _ {k}, \Delta\right) \right\}.\tag{13}
$$

If $r _ { k } ( { \bf x } )$ is a <sup>fi</sup>rst-order model, solving Eq. (13) is easy. However, if $r _ { k } ( { \bf x } )$ is a second-order model, solving Eq. (13) can be a dif<sup>fi</sup>cult task.

![](/api/attachments/EEK9WNF8/fulltext/images/3a0003de767917c574d06a65ec195f78ff79d83f357c32d1968f98e79b3ba775.jpg)  
Fig. 4. Input parameters.

Please cite this article as: K.-H. Chang, A decision support system for planning and coordination of hybrid renewable energy systems, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.001

K.-H. Chang / Decision Support Systems xxx (2014) xxx–xxx

![](/api/attachments/EEK9WNF8/fulltext/images/2363ccc93582bacc47be74fc31e7775c3a613ae1499779f9b3bc3ab58562d504.jpg)  
Fig. 5. Output results. (For interpretation of the references to color in this <sup>fi</sup>gure, the reader is referred to the web version of this article.)

We propose the following procedure to <sup>fi</sup>nd an approximate solution in the latter case:

• Step 1. Find the steepest descent direction $\mathbf { d } _ { k } = a r g m i n$ $\left\{ \hat { g } _ { k } ( \mathbf { x } _ { k } ) + \widehat { \nabla } g _ { k } ^ { T } ( \mathbf { x } _ { k } ) \ \mathbf { d } : \| \mathbf { d } \| \leq \Delta \right\}$

• Step 2. Choose a step size $\tau _ { k } = a r g m i n \{ r _ { k } ( \tau \mathbf { d } _ { k } ) \colon \tau > 0 , | | \tau \mathbf { d } _ { k } | | \leq \Delta \}$

• Step 3. Let $\mathbf { x } _ { k } ^ { * } = \mathbf { x } _ { k } + \tau _ { k } \mathbf { d } _ { k } .$

The proposed procedure <sup>fi</sup>rst <sup>fi</sup>nds the steepest descent direction and then determines the step size so that the solution will be within the experimental region. While this procedure only produces an approximate solution for Problem (13), it is usually a nearly optimal solution.

## 5. Numerical experiments

In this section, we conduct a numerical study to understand the effectiveness and ef<sup>fi</sup>ciency of MSA. We use an array of simulated problems to compare the performance of MSA, SAN and the modi<sup>fi</sup>ed

![](/api/attachments/EEK9WNF8/fulltext/images/390627f1b1de01ba8bcb7e70f720a20170f0886d86a298e7cd4103c0d6bc1cf2.jpg)  
Fig. 6. Sensitivity analysis of the DSS. (For interpretation of the references to color in this figure the reader is referred to the web version of this article.)

Nelder–Mead (MNM) method [5], which is one popular metaheuristic designed for simulation optimization problems.

Speci<sup>fi</sup>cally, 18 scenarios, constituted by 3 types of test functions, 3 types of dimensions, and 2 types of variance settings are created. The test problem is composed of a deterministic function with added noise, i.e., $G ( \mathbf { x } , \omega ) = g ( \mathbf { x } ) + \epsilon _ { x } .$ . Speci<sup>fi</sup>cally, for each test problem, three types of dimensions are considered: 4D, 12D and 16D, which correspond to low-, moderate-, and high-dimensional problems respectively. The added noise $\epsilon _ { x }$ is generated from $\mathcal { N } ( 0 , \sigma ^ { 2 } ( \mathbf { x } ) )$ with two types of variances: <sup>fi</sup>xed $( \sigma ( { \bf x } ) = 1 0 )$ and varying $( \sigma ( { \bf x } ) = 0 . 5 { \cdot } g ( { \bf x } ) )$ Note that in the latter setting, when the initial solution is selected far from the true optima, the function value g(x) will be large, making the response variable grossly noisy. This allows us to test the stability of algorithms.

The performance measure for comparison purposes is de<sup>fi</sup>ned a

$$
\log (g (\mathbf {x} _ {k} ^ {*}) - g ^ {*} + 1),\tag{14}
$$

where x<sup>∗</sup> and $g ^ { * }$ correspond to the best solution found when the algorithm is terminated and the true globally optimal function value, respectively. Eq. (14) refers to the gap of function values between the <sup>fi</sup>nal solution and the true optimum.

The test functions, g(x), are selected from literature in nonlinear optimization [24] and are considered dif<sup>fi</sup>cult even in deterministic settings. Speci<sup>fi</sup>cally, the <sup>fi</sup>rst type is the extended Rosenbrock function (ER),

$$
g (\mathbf {x}) = \sum_ {i = 1} ^ {p - 1} \left[ 1 0 0 \left(x _ {i} - x _ {i + 1} ^ {2}\right) ^ {2} + (1 - x _ {i}) ^ {2} \right],\tag{15}
$$

which is a multimodal function when $p \ge 4 \left[ 3 1 \right]$ . The second type is the Freudenstein and Roth function (FR),

$$
\begin{array}{l} g (\mathbf {x}) = \sum_ {i = 1} ^ {p / 2} \left[ - 1 3 + x _ {2 i - 1} + ((5 - x _ {2 i}) x _ {2 i} - 2) x _ {2 i} \right] ^ {2} \\ \quad + [ - 2 9 + x _ {2 i - 1} + ((x _ {2 i} + 1) x _ {2 i} - 1 4) x _ {2 i} ] ^ {2}, \end{array}\tag{16}
$$

which is also a multimodal function [24]. The third type is the Powell badly scaled function (PBS),

$$
g (\mathbf {x}) = \sum_ {i = 1} ^ {p - 1} \left[ 1 0 ^ {4} x _ {i} x _ {i + 1} - 1 \right] ^ {2} + \left[ \exp (- x _ {i}) + \exp (- x _ {i + 1}) - 1. 0 0 0 1 \right] ^ {2}.\tag{17}
$$

Please cite this article as: K.-H. Chang, A decision support system for planning and coordination of hybrid renewable energy systems, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.001

![](/api/attachments/EEK9WNF8/fulltext/images/4df495b365b25a7a0c0bdf70b88c91f94977954639fd71f6254e164f3a2f6ab2.jpg)  
Fig. 7. Power generation, allocation and transmission of the DSS (part I). (For interpretation of the references to color in this <sup>fi</sup>gure, the reader is referred to the web version of this article.)

For each algorithm and each scenario, we run 20 macroreplications. For each macroreplication, we terminate the algorithm when the maximum function evaluations 20,000 are reached. The performance measure as well as the associated standard deviation (given in the parenthesis) are reported. Tables 2 and 3 give the results.

From Tables 2 and 3, it is found that the convergence performance of MSA is satisfactory and is superior to the other two competing algorithms. In particular, the computational gain of MSA, compared to SAN, is in fact increasing with the problem dimension. This is because the MSA employs a metamodel-based search strategy that allows for better computational ef<sup>fi</sup>ciency than random search. Also, we can see that as the variance of noise increases, the performance of MSA is hardly affected, while that of the other two algorithms becomes worse. This shows the effectiveness of the sample size scheme and experimental design employed in MSA.

## 6. Developing a decision support system

In this section, we develop a decision support system to facilitate the decision making when implementing HRES in practice. A similar system, called HOMER Energy System, has been developed to compare the cost and feasibility of different con<sup>fi</sup>gurations; see the following website for details http://homerenergy.com/software.html. The purpose of the DSS is not only to provide the optimal solution regarding the number of solar and wind power generators, but also to give decision makers more insights into the energy management of HRES. The developed DSS is as Fig. 3 shows. In particular, the DSS has four major constructs, “Input Parameters”, “Output Results”, “Sensitivity Analysis”, and “Power Generation, Allocation and Transmission”.

![](/api/attachments/EEK9WNF8/fulltext/images/5f77782f000e991220ebbe66b03560defe3e820513961282e6b8ab1e55ef381b.jpg)  
Fig. 8. Power generation, allocation and transmission of the DSS (part II).

The “Input Parameters” allows users to provide the information about the parameters required in the model. Then, based on this information, the MSA algorithm embedded in the DSS would solve for the optimal number of solar and wind power generators of each power station and the result is shown in “Output Results.” In particular, for one realization of the power demand and the renewable power supply, the “Power Generation, Allocation and Transmission” function would show how much conventional power is needed to cover the power shortage and how the generated power be should transmitted to the demand areas in the most cost effective way.

## 6.1. Input parameters

The DSS requires users to provide the following information, which often can be obtained through historical data analysis.

• the distribution of renewable power supply of one unit of solar power generator at each power station $( P _ { s i } )$

• the distribution of renewable power supply of one unit of wind power generator at each power station $( P _ { w i } )$

• the distribution of power demand of each area for the period $l \left( d _ { k l } \right)$

• the cost of one solar power generator (C )

• the cost of one wind power generator $( C _ { w } )$

• the unit cost of conventional power generation (C )

• the number of HRES stations (M)

• the number of demand areas (N)

• the power storage cost (r)

• the distance between stations and demand areas (optional)

For demonstration purposes, we use the following setting: $P _ { s i } \sim \mathrm { N o r m a l } ( 5 , 1 ) , P _ { w i } \sim \mathrm { N o r m a l } ( 5 , 0 . 7 ) , d _ { k } \sim \mathrm { N o r m a l } ( 1 0 0 , 2 5 ) , C _ { s } = \ S 5$ $C _ { w } = \ S 5 , C _ { i } = \ S 1 0 , M = 3$ (power stations), $N = 1 0$ (demand areas). All of the parameters are input into the DSS as Fig. 4 shows. It takes around 40 s to solve the problem on the computer with Intel(R) ${ \mathrm { C o r e } } ( ^ { \mathrm { T M } } ) 2$ Duo CPU (2.26 GHz, 2.27 GHz) and 4 GB of RAM.

## 6.2. Output results

With the input parameters given in Fig. 4, the main model can be solved and the result is shown in “Output Results.” In Fig. 5, the Generator Bar Graph on the left and upper corners provides the information about how many solar and wind power generators are required for each of the three power stations, where the blue, green, and red parts represent the power station 1, 2 and 3, respectively. The total number of solar and wind power generators for all the three power stations is 95 and 126, respectively and the total cost is 1210.2. Also, the “Cost Pie Chart” shows the fraction of power generation cost by solar, wind and conventional power generators. Finally, the “Cost Bar Chart” shows the cost associated with the equipment installation cost and the conventional power generation cost, respectively.

![](/api/attachments/EEK9WNF8/fulltext/images/2cb7ac8c418a8bc65d9c633d70aa2aa2d60fd49220cb5c432a5d91bb720bc82a.jpg)  
Fig. 9. Power generation, allocation and transmission of the DSS (part III).

## 6.3. Sensitivity analysis

“Sensitivity Analysis” shows how the total cost and the optimal number of solar and wind power generators would change when one parameter of the model varies. In Fig. 6, the red portion represents the extra number of solar and wind power generators needed when the variance of power demand of each area is changed to 4.

## 6.4. Power generation, allocation and transmission

Given one con<sup>fi</sup>guration of the number of solar and wind power generators, “Power Generation, Allocation and Transmission” shows the amount of power needed from the conventional power generator to cover the power storage and the amount of power that each power station would transmit to each demand area (a blue line connecting one station and one area indicates power is transmitted between them). Also, the amount of conventional power required for each area is also given in Fig. 7.

In addition to Fig. 7, two additional <sup>fi</sup>gures are generated by the DSS. In particular, Figs. 8 and 9 provide the information regarding how much power is allocated to each power station and how much power each power station transmits to each demand area, respectively.

## 7. Conclusions

In this paper, we study the planning and coordination of HRES and propose a model to characterize the determination of the optimal number of solar and wind power generators of HRES in uncertain environments. The goal is to achieve the minimum total cost, while satisfying the power demand of each area. To solve the model, a simulation optimization method, MSA, coupled with a Monte Carlo simulation approach, is proposed. In particular, the MSA method is based on the traditional simulated annealing method, but is further adapted by incorporating a metamodel-based search strategy to accelerate the algorithm convergence. Numerical results show that in comparison with the existing methods, the proposed MSA can have superior convergence performance under the same computational budget. Finally, a decision support system (DSS) integrating the proposed model and the solution methodology is developed as an ef<sup>fi</sup>cient decision tool to enable effective and ef<sup>fi</sup>cient energy management of HRES. The visualized outputs of DSS allow decision makers to gain better understanding about the management of HRES, facilitating the decision making process.

Some future work is described as follows. First, when there is only limited historical data, it can be dif<sup>fi</sup>cult to specify the distribution of the power demand of each area and that of the renewable power supply of each power station. In this case, the decision model should account for the distribution ambiguity existing in the randomness. Second, the proposed Monte Carlo simulation method may require an excessive amount of time for generating one observation for estimating the additional power generation cost and the power storage cost, especially when the problem is of large scale, namely, the number of power stations and demand areas is large. A more ef<sup>fi</sup>cient approach should be developed to overcome the dif<sup>fi</sup>culty.

## Acknowledgments

The author would like to thank two anonymous referees and the associate editor for their insightful comments and suggestions that have signi<sup>fi</sup>cantly improved this paper. Special thanks to Ms. Hui-Hsin Cheng and Mr. Yen-Chu Chen for their help in developing the decision support system. This research is conducted under the project "Modeling and Optimization of Hybrid Renewable Energy System" (NTHU101A0144J8), subsidized by Institute for Information Industry.

## References

[1] B. Ai, H. Yang, H. Shen, X. Liao, Computer-aided design of PV/wind hybrid system, Renew. Energy 28 (10) (2003) 1491–1512.

[2] A. Alarcon-Rodriguez, G. Ault, S. Galloway, Multi-objective planning of distributed energy resources: a review of the state-of-the-art, Renew. Sust. Energ. Rev. 14 (5) (2010) 1353–1366.

[3] A. Bagul, Z. Salameh, B. Borowy, Sizing of stand-alone hybrid wind–photovoltaic system using a three-event probability density approximation, Sol. Energy 56 (4) (1996) 323–335.

[4] B. Bala, S. Siddique, Optimal design of a PV–diesel hybrid system for electri<sup>fi</sup>cation of an isolated island—Sandwip in Bangladesh using genetic algorithm, Energy Sustain. Dev, 13 (3) (2009) 137-142

[5] R. Barton, J. Ivey, Nelder–Mead simplex modi<sup>fi</sup>cations for simulation optimization, Manag, Sci, 42 (7) (1996) 954–973

Please cite this article as: K.-H. Chang, A decision support system for planning and coordination of hybrid renewable energy systems, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.001

[6] J.L. Bernal-Agustí, R. Dufo-López, Simulation and optimization of stand-alone hybrid renewable energy systems, Renew. Sust. Energ. Rev. 13 (8) (2009) 2111–2118.

[7] A. Bhave, Hybrid solar–wind domestic power generating system—a case study, Renew. Energy 17 (3) (1999) 355–358.

[8] B. Borrowsy, Z. Salameh, Optimum photovoltaic array size for a hybrid wind/PV systems, IEEE Trans. Energy Convers. 9 (3) (1994) 482–488.

[9] B. Borrowsy, Z. Salameh, Methodology for optimally sizing the combination of a battery bank and PV array in a wind/PV hybrid system, IEEE Trans. Energy Convers. 11 (2) (1996) 367–375.

[10] A. Celik, Optimization and techno-economic analysis of autonomous photovoltaic– wind hybrid energy systems in comparison to single photovoltaic and wind systems, Energy Convers. Manag. 43 (18) (2002) 2453–2468.

[11] R. Chedid, Y. Saliba, Optimization and control of autonomous renewable energy systems, Int. J. Energy Res. 20 (1996) 609–624.

[12] M. Elhadidy, Performance evaluation of hybrid (wind/solar/diesel) power systems Renew. Energy 26 (3) (2002) 401–413.

[13] M. Elhadidy, S. Shaahid, Optimal sizing of battery storage for hybrid (wind + diesel) power systems, Renew. Energy 18 (1) (1999) 77–86.

[14] M. Elhadidy, S. Shaahid, Promoting applications of hybrid (wind + photovoltaic + diesel + battery) power systems in hot regions, Renew. Energy 29 (4) (2004) 517–528.

[15] L. Ferrer-Martí, B. Domenech, A. García-Villoria, R. Pastor, A MILP model to design hybrid wind–photovoltaic isolated rural electri<sup>fi</sup>cation projects in developing countries, Eur. J. Oper. Res. 226 (2013) 293–300.

[16] F. Giraud, Z. Salameh, Steady-state performance of a grid-connected rooftop hybrid wind–photovoltaic power system with battery storage, IEEE Trans. Power Energy Convers. 16 (1) (2001) 1–7.

[17] S. Gomaa, A. Seoud, H. Kheiralla, Design and analysis of photovoltaic and wind energy hybrid systems in Alexandria, Egypt, Renew. Energy 6 (5–6) (1995) 643–647.

[18] E. Gorgopoulou, D. Lalas, L. Papagiannakis, A multicriteria decision aid approach for energy planning problems: the case of renewable energy option, Eur. J. Oper. Res. 103 (1997) 38–54.

[19] J. Hunt, R. Bañares-Alcántara, D. Hanbury, New integrated tool for complex decision making: application to the UK energy sector, Decis. Support. Syst. 54 (3) (2013) 1427–1441.

[20] S. Karaki, R. Chedid, R. Ramadan, Probabilistic performance assessment of autonomous solar–wind energy conversion systems, IEEE Trans. Energy Convers. 14 (3) (1999) 766–772.

[21] W. Kellogg, M. Nehrir, G. Venkataramanan, V. Gerez, Generation unit sizing and cost analysis for stand-alone wind photovoltaic and hybrid wind/PV systems, IEEE Trans. Energy Convers. 13 (1) (1998) 70–75.

[22] M. Kolhe, K. Agbossou, J. Hamelin, T. Bose, Analytical model for predicting the performance of photovoltaic array coupled with a wind turbine in a stand-alone renewable energy system based on hydrogen, Renew. Energy 28 (5) (2003) 727–742.

[23] D. Montgomery, Design and Analysis of Experiments, 7 edition John Wiley and Sons, New York. 2009

[24] J. More, B. Garbow, K. Hillstrom, Testing unconstrained optimization software, ACM Trans. Math. Softw. 7 (1981) 17–41.

[25] T. Morgan, R. Marshall, B. Brinkworth, ARES: a rede<sup>fi</sup>ned simulation program for the sizing and optimization of autonomous hybrid energy systems, Sol. Energy 59 (4–6) (1997) 205–215.

[26] A. Musgrove, The optimization of hybrid energy conversion system using the dynamic programming model—rapsody, Int. J. Energy Res. 12 (1988) 447–457.

[27] M. Nehrir, B. LaMeres, G. Venkataramanan, V. Gerez, L. Alvarado, An approach to evaluate the general performance of stand-alone wind/photovoltaic generating systems, IEEE Trans. Energy Convers. 15 (4) (2000) 433–439.

[28] REN21 Secretariat, Renewables 2013 Global Status Report, 2013.

[29] A. Rentizelas, A. Tolis, L. Tatsiopoulos, Investment planning in electricity production under CO price uncertainty, Int. J. Prod. Econ. 140 (2) (2012) 622–629.

[30] G. Seeling-Hochmuth, A combined optimization concept for the design and operation strategy of hybrid-PV energy systems, Sol. Energy 61 (2) (1997) 77–87.

[31] S. Shaahid, M. Elhadidy, Prospects of autonomous/stand-alone hybrid (photovoltaic + diesel + battery) power systems in commercial applications in hot regions, Renew. Energy 29 (2) (2003) 165–177.

[32] Y.-W. Shang, Y.-H. Qiu, A note on the extended Rosenbrock function, Evol. Comput. 14 (1) (2006) 119–126.

[33] J. Spall, Introduction to Stochastic Search and Optimization: Estimation, Simulation, and Control, John Wiley and Sons, New York, 2003.

[34] G. Xydis, A techno-economic and spatial analysis for the optimal planning of wind energy in Kythira island, Greece, Int. J. Prod. Econ. (2014) (in press).

Kuo-Hao Chang is an assistant professor in Industrial Engineering and Engineering Management at National Tsing Hua University. He received his PhD in Industrial Engineering from Purdue University. He won the 2012 INFORMS Bonder Scholar Research Award. He has consulted with many industrial companies including TSMC, VisEra, YOMURA, ITRI etc. Currently, he serves as the executive editor of Journal of Industrial and Production Engineering. He is also a member of INFORMS. His research interests include simulation optimization, stochastic models and Monte Carlo simulation. His email and web addresses are chang@mx.nthuedutw and https://sites.google.com/site/ssoptimizationlab/

Please cite this article as: K.-H. Chang, A decision support system for planning and coordination of hybrid renewable energy systems, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.001
