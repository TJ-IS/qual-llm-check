---
otero_id: 3564
otero_key: "CNAE9NFQ"
title: "Beer game order policy optimization under changing customer demand"
authors: "F. Strozzi; J. Bosch; J.M. Zaldívar"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.06.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Beer game order policy optimization under changing customer demand

F. Strozzi <sup>a,⁎</sup>, J. Bosch <sup>a</sup>, J.M. Zaldívar <sup>b</sup>

<sup>a</sup> Carlo Cattaneo University, Engineering Faculty, Quantitative Methods Institute 21053 Castellanza (VA), Italy b European Commission, Joint Research Centre, Institute for Environment and Sustainability, 21020 Ispra (VA), Italy

Received 9 January 2005; received in revised form 20 May 2006; accepted 5 June 2006 Available online 25 July 2006

## Abstract

The present work analyses the optimal Beer Game order policy when customers demand increases. The optimal policy is found by means of a Genetic Algorithms (GAs) technique. GAs are specially suited for this problem because of the high dimension of the search space, and because the objective function i.e. the global score of the chain, has many local minima. Our results show that the best performance of the chain is obtained when the sectors have different order policies. The advantage increases with the increasing change in the customer demand.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Beer game; Genetic algorithms; Supply chain

## 1. Introduction

The Beer Distribution Game (“Beer Game”), developed at the Sloan School of Management in early 1960s [7], is a classic supply chain problem widely used in graduate business programs to teach the concepts of supply chain management [9].

The goal of the participants in the game is to minimize the costs of maintaining sufficient inventories of beer while at the same time avoiding out-of-stock condition that could lead to loss of customers. The Beer Game is notable for its ability to confuse, human players [10,11], typically giving rise to instabilities in the supply chain and distortion of the expected demand [1]. The game is also used to illustrate how different decision policies influence the dynamics of a distribution system.

Sterman [11] formulated a four parameter discrete model for the order policy, based on the theory of bounded rationality [2,3] and showed that this model captures the main aspects of the decisions taken in the game by real players. Mosekilde and Larsen [8] were first to show that a time-continuous version of the Beer Game model could produce deterministic chaos and other forms of complex behaviour [15].

In this work we are going to analyse the optimal order policies, i.e. the optimal parameters of the Sterman model, when step-changes of different magnitudes occur in the customer demand. The optimal policy considered is the policy that gives the minimum cost, accounting both for the costs to maintain a stock of goods and for the costs of loosing business when it is not possible to satisfy the demand.

Two scenarios have been analysed: (i) all sectors apply the same order policies, or (ii) different policies are applied from sector to sector.

The search of the optimal solution has been performed using Genetic Algorithms [4] due to the complexity of the objective cost function, which has many local minima and, in the case of different policies, many parameters. The application of GAs optimization techniques represents a new approach in the case of the Beer Game model but Genetic Algorithms have been applied in several managerial problems such as portfolio optimization and job scheduling [14].

A description of the Beer Game and the order policy models is presented in Section 2, and the implementation and application of the Genetic Algorithms to optimise the costs are discussed in Section 3. The results, Section 4, show that it is possible to reduce the score both for the chain and for the individual participants by allowing different order policies, even when the customer demand is changing. Moreover, the advantage of different order policies increases as a function of the step-change in the customer demand. This advantage is obtained when the Factory and the Distributor pay more attention to the stock than to the supply chain, whereas the Wholesaler and the Retailer focus on the supply chain.

## 2. The beer game

The Beer Game is a representation of a production– distribution system on four levels: Factory, Distributor, Wholesaler and Retailer, see Fig. 1. The orders starting from the customer go to the Retailer, then to the Wholesaler, the Distributor, and finally reach the Factory. In the meantime, deliveries are shipped from the Factory down through the supply chain until they reach the customer. The Beer Game is widely used in management schools as a means of conveying to the students the causal relationships between their decision-making and the behaviour of supply chains. The game may also be considered as an illustration of how oscillations can arise in economic and managerial systems. Finally, the game illustrates how one can use simulation models to fit different order policies. The typical results of the game are counterintuitive, because large oscillations appear in the order rate in response to a step-increase in the customer demand [10].

In order to simplify this production–distribution system to be used by real players, several rules and structural characteristics were defined [7]: there is only one inventory at each level initialized with 12 cases of beer; the time delay for passing of orders and shipments from one stage to the next is fixed to 1 week (one time period of the game); the production time is taken to be 3 weeks, and it is assumed that the production capacity of the brewery can be adjusted without limits. Moreover, orders placed cannot be cancelled, surplus inventories cannot be returned, and deliveries must be made if covered by the available inventory. Each week customers order beer from the retailer, who supplies the requested quantity out of his inventory.

A further typical simplification is that customer demand is four cases of beer per week until week 4 and steps to eight cases of beer per week at week five. In this work we have analysed a set of customer demands that changes, at week five, from four to fifteen cases and then we have forced the system with a higher demand, i.e. forty cases, to test if the limit values found are maintained.

The objective for the participants (stock managers) in the game is to minimise cumulative sector costs at the end of the game. Considering the costs associated with inventory holding (0.50 per case per week), stocks should be kept as small as possible. On the other hand, failure to deliver on request may force customers to seek alternative suppliers. For this reason, there are also costs associated with having backlogs of unfilled orders (2.00 per case per week).

At the beginning of each week, stock managers in all the sectors have to decide, the amount of beer to be ordered from their suppliers.

## 2.1. The simulation model

The simulation model consists of a high-dimensional iterated map that represents the sequence of operations that each sector should perform. The boxes in Fig. 1 depict the state variables. Each variable has an initial letter that indicates the respective sector; thus R stands for retailer, W for wholesaler, D for distributor and F for factory. For example, in the wholesale sector, WINV is the inventory of beer, WBL the backlog of orders, WIS and WOS represent incoming and outgoing shipments, respectively, where WIO is the incoming orders, WED is the expected demand and WOP the orders placed by the wholesaler. One time step later, WOP becomes incoming orders to the distributor, DIO. The same notation is employed in the other sectors with the exception of the factory where there is a production rate, FPR, instead of placed orders and FPD1 and FPD2 represent the production delays. The exogenous customer order rate is given by COR.

![](/api/attachments/CNAE9NFQ/fulltext/images/72cb2471687e5595fde1740674d426f3bcd6284075ecbe4c62b24d18f05a2768.jpg)  
Fig. 1. Basic structure of the considered production–distribution system with state variables, order flows (left arrow) and good flows (right arrow) in the Beer Game model.

The difference equations of the model [12] that represent the operations conducted in each sector may be written for the wholesaler sector as example.

$$
\mathrm{WINV} _ {t} = \left\{ \begin{array}{l l} \mathrm{WINV} _ {t - 1} + \mathrm{WIS} _ {t - 1} - \mathrm{WBL} _ {t - 1} - \mathrm{WIO} _ {t - 1} \\ \text { if } \quad \mathrm{WINV} _ {t - 1} + \mathrm{WIS} _ {t - 1} \geq \mathrm{WBL} _ {t - 1} + \mathrm{WIO} _ {t - 1} \\ 0 \quad \text { otherwise } \end{array} \right.\tag{1}
$$

Similar expressions hold for RINV, DINV and FINV.

$$
\mathrm{WIS} _ {t} = D O S _ {\mathrm{t-1}}\tag{2}
$$

again similar expressions are used for RIS, DIS and FPD2.

$$
\mathrm{WBL} _ {t} = \left\{ \begin{array}{l l} \mathrm{WBL} _ {t - 1} + \mathrm{WIO} _ {t - 1} - \mathrm{WINV} _ {t - 1} - \mathrm{WIS} _ {t - 1} \\ \text { if } & \mathrm{WBL} _ {t - 1} + \mathrm{WIO} _ {t - 1} \geq \mathrm{WINV} _ {t - 1} + \mathrm{WIS} _ {t - 1} \\ 0 & \text { otherwise } \end{array} \right.\tag{3}
$$

Similar expressions are used for RBL, DBL and FBL.

$$
\mathrm{WIO} _ {t} = \mathrm{ROP} _ {t - 1}\tag{4}
$$

with similar expressions for DIO, FIO and FPD1.

$$
\mathrm{WOS} _ {t} = \min \left\{\mathrm{WINV} _ {t - 1} + \mathrm{WIS} _ {t - 1} + \mathrm{WIO} _ {t - 1} \right\}\tag{5}
$$

with similar expressions for DOS, FOS and shipments out of retailer's inventory.

## 2.2. The ordering policy

Consistent with the theory of bounded rationality [13] and assuming that a stock manager applies adaptive expectations, Sterman [11] has proposed that the expected demand may be expressed as follows:

$$
\mathrm{WED} _ {t} = \theta \cdot \mathrm{WIO} _ {t - 1} + (1 - \theta) \cdot \mathrm{WED} _ {t - 1}\tag{6}
$$

WED and $\mathrm { W E D } _ { t - 1 }$ are the expected demand at times t and $t - 1$ , respectively, WIO is the incoming orders, and $\theta ( 0 \leq \theta \leq 1 )$ is a parameter that controls the rate at which expectations are updated. $\theta { = } 0$ corresponds to stationary expectations, and $\theta = 1$ describes a situation in which the immediately preceding value of received orders is used as an estimate of future demand. Statistical analysis show that θ is typically 0.25 [9].

The order placed are determined in accordance with the expression

$$
\mathrm{WOP} _ {t} = \max \left\{0, \mathrm{WOP} _ {t} ^ {*} \right\}
$$

where

$$
\mathrm{WOP} _ {t} ^ {*} = \mathrm{WED} _ {t} + \mathrm{WAS} _ {t} + \mathrm{WASL} _ {t}\tag{7}
$$

i.e. the order decision has to be positive and it is a sum of the number of cases that the manager expected to be ordered $( \mathrm { W E D } _ { t } ;$ Wholesaler Expected Demand), the number of cases necessary to replace a fraction of the inventory discrepancy (WAS : Wholesaler Stock Adjustment) and the number of cases to fill a fraction of the supply chain discrepancy $\mathrm { ( W A S L } _ { t } .$ Wholesaler Adjustment of Supply Chain).The former quantities are respectively defined as follows:

$$
\mathrm{WAS} _ {t} = \alpha_ {s} (\mathrm{DINV-WINV} _ {t} + \mathrm{WBL} _ {t})\tag{8}
$$

where WDINV and $\mathrm { W I N V } _ { t }$ denote desired and actual inventories, respectively, and $\mathrm { W B L } _ { t }$ is the backlog of orders. The stock adjustment parameter $\alpha _ { s }$ is the fraction of the discrepancy between desired and actual inventory ordered in each round. DINV is assumed to be constant and equal to 14 cases of beer.

A statistical study with a significant number of participants [12] showed that the stock adjustment parameters $\alpha _ { s }$ varies between 0 and 1.

In analogy with the stock adjustments, the supply chain adjustments are expressed as:

$$
\begin{array}{l} \mathrm{WASL} _ {t} = \alpha_ {\mathrm{SL}} (\mathrm{DSL-WSL} _ {t}) \\ \mathrm{WSL} _ {t} = \mathrm{WIS} _ {t} + \mathrm{DIO} _ {t} + \mathrm{DBL} _ {t} + \mathrm{DOS} _ {t} \end{array}\tag{9}
$$

where DSL denotes the desired supply chain, which is supposed the same for the participants and constant in time, and WSL denote the real the supply chain of the wholesaler. $\mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { \Omega } \mathsf { a } _ { S L }$ is the fractional adjustment rate, $\mathrm { i . e . }$ , the fraction of the discrepancy between desired and actual supply chain ordered in each round.

Defining $\beta { = } \alpha _ { S L } / \alpha _ { S }$ and $Q { = } \mathrm { D I N V } + \beta { \cdot } \mathrm { D S L }$ , the expression for the indicated order rate becomes

$$
\mathrm{WOP} _ {t} ^ {*} = \mathrm{WED} _ {t} + \alpha_ {S} (Q - \mathrm{WINV} _ {t} + \mathrm{WBL} _ {t} - \beta \cdot \mathrm{WSL} _ {t})\tag{10}
$$

DINV, DSL, and $\beta$ are all non-negative, implying that $Q { \geq } 0$ . In [12] the case in which DINV, DBL, $\alpha _ { S } , \beta$ were the same for the participants is considered.

The supply chain does not directly influence costs, nor is it as evident as the inventory. Hence, it is reasonable to assume that $\alpha _ { S L } \leq \alpha _ { S }$ and $\beta \leq 1 . \ \beta$ may be interpreted as the fraction of the supply chain taken into account by the participants.

A couple of values of the parameters $( \alpha _ { S } , \beta )$ correspond to a specific behaviour of the participants. High values of $\alpha _ { S }$ mean high attention to the inventory, and high $\beta \mathrm { \hbar }$ values imply high attention to the supply chain in comparison with the inventory.

## 2.3. The fitness function

In this work, the main goal of each participant will be to minimise the global score i.e. the total operation costs of the chain. This results in the minimisation of the fol-

lowing objective function

$$
\begin{array}{l} J = \sum_ {i = 1} ^ {n} (2 * (\mathrm{RBL} _ {i} + \mathrm{WBL} _ {i} + \mathrm{DBL} _ {i} + \mathrm{FBL} _ {i}) \\ \quad + 0. 5 * (\mathrm{RINV} _ {i} + \mathrm{WINV} _ {i} + \mathrm{DINV} _ {i} \\ \quad + \mathrm{FINV} _ {i})) \end{array}\tag{11}
$$

where $n { = } 6 0$ is the total number of weeks. Furthermore, in accordance with Ref. [9], we restricted the search space to the $( \alpha _ { s } , \ \beta )$ plane, maintaining $Q = 1 7$ and $\theta = 0 . 2 5$ respectively.

Finally, it was decided to determine the optimal parameters for the ordering policy for two different situations. In the first case all sectors were assumed to apply the same parameter values $( \alpha _ { s }$ and $\beta ) ,$ , whereas in the second case, all four sectors had different parameters. Figs. 2 and 3 show the effective inventory (inventory-backlog) and order rate evolutions of the four sectors over 60 weeks simulations for both scenarios using the optimal parameters founded with GAs techniques.

In both cases, the effective inventories initially decrease and afterwards give rise to a set of oscillations that increase from retailer to the factory. This behaviour is a result of the change of the customer order rate at week 5 from 4 to 8 cases of beer. This change produces an increase of the orders placed by the retailer that is propagated in a wavelike manner through the supply chain to the factory, depleting the inventories one by one and producing a successive increase of the order rates to fill the generated backlogs. Once the backlogs are eliminated, the inventories show a strong increase because of the high order rates. This is specially noticeable for sectors close to factory. Finally, the inventories are again reduced through adjustments of the order rates. Despite the analogous response in both scenarios, it is noticeable that in the second scenario, when the four sectors have different order policies, the supply chain presents lower and smoother oscillations. In particular, the distributor effective inventory in the first scenario reaches one hundred cases of beer, while in the second scenario the biggest effective inventory is slightly greater than twenty units.

![](/api/attachments/CNAE9NFQ/fulltext/images/930e8d40a0ff20913cf88383a3cc24969defddb91d0d76035ab3c5a7bac2544e.jpg)

![](/api/attachments/CNAE9NFQ/fulltext/images/9c8c0ef978753a6dd5e859551691f467063492d9d000977a8296af9dba652017.jpg)  
Fig. 2. Inventory i.e. the number of cases in the stock (upper panel) and order placed (lower panel) of the retailer (continuous line), wholesaler (dashed line), distributor (dotted line) and factory (continuous pointed line). Same order policy for all sectors. Customer demand changes from 4 to 8 cases of beer per week in the fifth week. θ=0.250, Q=17, α =0.317 and β=0.016.

![](/api/attachments/CNAE9NFQ/fulltext/images/5e426ee0a209689962bae94fb42958090ced47ebfec652924af545c77234004d.jpg)

![](/api/attachments/CNAE9NFQ/fulltext/images/9d8dbd2881b55a5aa84649b715f974709bbf3a6fb81d45acebcc3acbcfc80ce1.jpg)  
Fig. 3. Inventory (upper panel) and order placed (lower panel) evolutions of the Retailer (continuous line), Wholesaler (dashed line), Distributor (dotted line) and Factory (continuos pointed line) with different order policies. θ = 0.250, Q = 17, α = 0.09400 $\beta _ { \mathrm { R } } { = } 0 . 2 5 7 0$ $\alpha _ { \mathrm { w } } { = } 0 . 9 7 9 0$ $\beta _ { \mathrm { W } } = 0 . 5 9 1 0 , \alpha _ { \mathrm { D } } = 0 . 9 9 1 0 , \beta _ { \mathrm { D } } = 0 . 6 3 2 0 , \alpha _ { \mathrm { F } } = 0 . 9 6 0 0$ and $\beta _ { \mathrm { F } } { = } 0 . 2 4 7 0$ . Customer demand changes from 4 to 8 cases.

## 3. Genetic algorithms

Genetic Algorithms (GAs) are optimisation algorithms inspired by the natural selection rules of Darwin's theory of evolution, i.e. the survival of the fittest. Building on this idea, Holland [4] developed the first GAs where an optimisation problem is turned into an evolutionary process, in which a group of individuals evolve to adapt better to a fitness function generation after generation.

Since then, GAs have been applied on many fields, the technique showing itself to be a robust and powerful optimisation tool especially suited for problems with large search spaces, and with complex or non-analytic objective functions [5].

GAs generate randomly, or based on background knowledge, an initial set of possible solutions called a population. Each potential solution is encoded into a string called the chromosome. Depending on the type of problem, chromosomes may be built-up of characters, bits, integers or real numbers. Subsequently, the fitness of each chromosome is evaluated using a pre-specified objective function. A new offspring population is generated from the actual population by using three operators: selection, crossover and mutation. The first operator selects pairs of chromosomes called parents from the actual population in order to create a mating pool for the offspring generation. This is a stochastic process where the probability of each individual is proportional to its relative fitness within the current population. The crossover operator generates two offspring chromosomes of the new population starting from two of the old ones by redistributing the information from the parent's strings. After that, the mutation operator introduces an alteration on a randomly selected point of the string. Finally, depending on the implemented replacement mode, the actual population, or a set of chromosomes of the actual population, is replaced by the new population. Iterations are typically called generations. The algorithm repeats the population generation renewal until one of the end conditions, such as number of generations or the error improvement, is satisfied.

![](/api/attachments/CNAE9NFQ/fulltext/images/133d4dd9ada68d553e2b4b286d30b155765ec4517025ba5912a64fbb1afd5fce.jpg)  
Fig. 4. Optimum order policies for different steps in the customer demand as obtained from our Genetic Algorithms routine, when the sector have the same order policy (observe that “4” means that we pass from 4 to 4 cases/week, i.e., that no step occurs).

The crossover and mutation operators are stochastic processes with defined probabilities. The crossover probability, or crossover rate, is generally high, about 80– 95%, to ensure an evolution process. By contrast, the mutation probability is often very low, generally less than 1%. This is because high mutation rates make Genetic Algorithms act as random search algorithms. On the other hand, the small contribution from mutations plays the important role of driving the evolution into new areas of the search space to avoid falling into local minima [6].

## 3.1. Beer game parameters estimation with GAs

In this work, GAs were used as optimisation techniques on the Beer Game order policy model. The election of GAs to solve this problem was based on the fact that the cost function J that we want to minimise has many local minima (see Fig. 7) and can depend on many parameters $( \beta _ { \mathrm { R } } , \alpha _ { \mathrm { R } } , \alpha _ { \mathrm { W } } , \beta _ { \mathrm { W } } , \alpha _ { \mathrm { D } } , \beta _ { \mathrm { D } } , \alpha _ { \mathrm { F } }$ and $\beta _ { \mathrm { F } }$ in the case of different behaviours).

Once the problem is defined, the following steps for a GAs implementation are definition of the fitness function and the chromosome structure. In both cases, the selected fitness function is the overall weekly cost of the four sectors: the function J defined by Eq. (11).

The chromosome structure in the first case contains two genes, one for $\alpha _ { S }$ and one for $\beta .$ It was also decided to encode chromosomes in bits. As the parameter values are contained between 0 and 1 and it was decided to use three decimal digits, each gene resulted in 10 bits, and therefore a 20 bits chromosome structure. Analogously,

![](/api/attachments/CNAE9NFQ/fulltext/images/4574115f1085ee50f7c98c567f9d378ffa73db218c1ca60d4fb5d1336c8ec56d.jpg)

![](/api/attachments/CNAE9NFQ/fulltext/images/982cf1f56fae4ed65faa7484f13eb6b8d91d03dcb4cb6bcac16a15daaf09e25e.jpg)

![](/api/attachments/CNAE9NFQ/fulltext/images/0774f11f3d1344b3f578f38502318053633aa77e3e6c81920d3cf7522b9cdee4.jpg)

![](/api/attachments/CNAE9NFQ/fulltext/images/47109d06b315cdb57accad20dd570a6e3505e4be62e9301ec144eaddf9d663ab.jpg)  
Fig. 5. The optimum order policies given by GAs, for different steps in the customer demand, when the sectors have different order policies.

Table 1

in the second case the chromosome structure contains eight genes. This is one $\alpha _ { S }$ and one β for each of the four sectors. As in the previous case, genes were encoded in 10 bits strings resulting in 80 bits chromosome.

Once the fitness function and the chromosome structures were defined, a GAs was implemented on MATLAB with the genetic operators, selection, crossover and mutation, described previously. In particular, the crossover operator implemented uses either one or two crossover points and parent's selection is carried out using the method of rank selection.

## 4. Results and discussion

For all the cases analysed, optimisation using GAs was carried out with a population size of 30 possible behaviours, a crossover rate of 90% and a mutation rate of 1% per generation. The maximum number of iterations was 500. Once an order policy was established and a step in the demand was fixed, the GAs was applied ten times in order to explore the search space. The optimal solution, from the point of view of the fitness function, was considered.

In Fig. 4 the optimum policies of the sectors are represented in the case of the first scenario when all the sectors apply the same policy. Results have shown that when the step in the demand increases from 4 to 15, $\alpha _ { S }$ moves towards 1 whereas β moves towards 0.6 increasing suddenly in connection to a step-change of 11 cases. Looking at Fig. 7, the change of the minima of surfaces J is evident.. This means that when the customer demand increases all the sectors have to increase the rate of stock adjustment. The supply chain is important in the order policy (β high) when the step does not exists (step 4) or it is very small (step 5 and 6, i.e. only one or two cases more; β decreases for step-changes of 7–10 and suddenly, after step 11, increases again moving around 0.6.

Optimal scores when the sectors apply the same order policy

<table><tr><td>Step</td><td> $J_{\text{F}}$ </td><td> $J_{\text{D}}$ </td><td> $J_{\text{W}}$ </td><td> $J_{\text{R}}$ </td><td> $J_{\text{Tot}}$ </td></tr><tr><td>4</td><td>102.5</td><td>170</td><td>159</td><td>197</td><td>628.5</td></tr><tr><td>5</td><td>115</td><td>146.5</td><td>139.5</td><td>121.5</td><td>522.5</td></tr><tr><td>6</td><td>108.5</td><td>93</td><td>69</td><td>45.5</td><td>316</td></tr><tr><td>7</td><td>454</td><td>445</td><td>360.5</td><td>359.5</td><td>1619</td></tr><tr><td>8</td><td>1120.5</td><td>877</td><td>509</td><td>460</td><td>2966.5</td></tr><tr><td>9</td><td>1664</td><td>1600.5</td><td>1000.5</td><td>458.5</td><td>4723.5</td></tr><tr><td>10</td><td>1899.5</td><td>2106.5</td><td>1918</td><td>792.5</td><td>6716.5</td></tr><tr><td>11</td><td>2261.5</td><td>2710</td><td>2549</td><td>2204</td><td>9724.5</td></tr><tr><td>12</td><td>2536</td><td>3100.5</td><td>3010</td><td>2775.5</td><td>11422</td></tr><tr><td>13</td><td>2836.5</td><td>3467.5</td><td>3431.5</td><td>3278.5</td><td>13014</td></tr><tr><td>14</td><td>3109</td><td>3922</td><td>3937.5</td><td>3895</td><td>14863.5</td></tr><tr><td>15</td><td>3376</td><td>4415</td><td>4487.5</td><td>4494</td><td>16772.5</td></tr><tr><td>40</td><td>14349</td><td>16845</td><td>16891</td><td>15761</td><td>63846</td></tr></table>

![](/api/attachments/CNAE9NFQ/fulltext/images/f6b10d0c886ab2bb670e55cc7af837736589037c83f22f666fd226ebb0ed609e.jpg)  
Fig. 6. Score of the sector and of the chain (score ${ \cal J } _ { \mathrm { T o t } } )$ when the order policies are the same (\*) or different (o) with respect to the change in the step of the customer demand.

Optimal scores when the sectors apply different order policies

<table><tr><td>Step</td><td> $J_{\text{F}}$ </td><td> $J_{\text{D}}$ </td><td> $J_{\text{W}}$ </td><td> $J_{\text{R}}$ </td><td> $J_{\text{Tot}}$ </td></tr><tr><td>4</td><td>94</td><td>166</td><td>163</td><td>169.5</td><td>592.5</td></tr><tr><td>5</td><td>88.5</td><td>104</td><td>72.5</td><td>64.5</td><td>329.5</td></tr><tr><td>6</td><td>69.5</td><td>67.5</td><td>89.5</td><td>47</td><td>273.5</td></tr><tr><td>7</td><td>181.5</td><td>120.5</td><td>130.5</td><td>147</td><td>579.5</td></tr><tr><td>8</td><td>289</td><td>208.5</td><td>205.5</td><td>342</td><td>1045</td></tr><tr><td>9</td><td>317</td><td>261.5</td><td>339</td><td>632.5</td><td>1550</td></tr><tr><td>10</td><td>434</td><td>316</td><td>498</td><td>961</td><td>2209</td></tr><tr><td>11</td><td>532</td><td>372.5</td><td>727</td><td>1300.5</td><td>2932</td></tr><tr><td>12</td><td>594.5</td><td>528.5</td><td>914</td><td>1590</td><td>3627</td></tr><tr><td>13</td><td>669</td><td>666.5</td><td>1140.5</td><td>1997.5</td><td>4473.5</td></tr><tr><td>14</td><td>875</td><td>727</td><td>1338</td><td>2325</td><td>5265</td></tr><tr><td>15</td><td>793.5</td><td>949.5</td><td>1626</td><td>2735</td><td>6104</td></tr><tr><td>40</td><td>2013</td><td>4120</td><td>8846</td><td>14720</td><td>29699</td></tr></table>

In the second scenario, when the sectors apply different order policies, solutions appear to be placed on certain regions of the parameter space depending on the involved sector in the distribution chain. In Fig. 5 the values of the optimum policies are presented for each sector. It is possible to observe that the factory optimal values of $( \alpha _ { \mathrm { F } } , \beta _ { \mathrm { F } } )$ , after a step-change of 10 cases, is concentrated around (1,0) meaning that the best order policy of the factory is the one that adjusts stocks quasiinstantaneously and does not consider the adjustment of the supply chain. On the contrary, the optimal policy for the retailer sector, after the step 5, consists in adjusting the stock slowly $( \alpha _ { R }$ small). There is no clear convergence of $\beta _ { \mathrm { F } } ,$ we thus do not have a suggestion for the retailer rate of adjustment of the supply chain.

Furthermore, if we divided the four policy spaces by their diagonal, see Fig. 5, we can observe that practically all the optimal values of the factory and the distributor are in the lower part of the square; whereas the ones of the wholesaler and the retailer are in the upper part. This means that the Factory and the Distributor have to pay more attention to the stock than to the supply chain, whereas the opposite in time for the Wholesaler and the Retailer.

In Fig. 6 the score of the sector and the global score J of the chain are presented in correspondence to the different steps in the customer demand for both scenarios. It can be seen that the advantage in having different order policies increases when the step of the demand increases.

In Tables 1 and 2 the numerical values of the scores are represented for both scenarios, respectively. It is possible to see that not only the global score for the chain, but also the scores of each participant, are smaller when using different ordering policies in comparison to all sectors using the same. As can be seen in Table 1, for the first scenario, after the step-change of 11 cases the smallest score shifts from the retailer to the factory. This occurs because the step-change in the demand approaches the initial stock value, and the participants start to have backlogs (which have a high weight in the final score values). In Table 2 we can see that, in the second scenario, after the customer demand step-change of 14 cases, the best score moves from the distributor back to the factory. For high step-changes in the demand, in both cases, the factory has the best score. Moreover in

![](/api/attachments/CNAE9NFQ/fulltext/images/ba135ba646ab6a37ad6c4fd8bd4fa91c50208897a830c7d2cbf05be64119d54b.jpg)

![](/api/attachments/CNAE9NFQ/fulltext/images/a6d181333122d2a82677c9e5e549551a3f8c8578a3c3608bec08804c208c806b.jpg)

![](/api/attachments/CNAE9NFQ/fulltext/images/56547f092e37f416c75ede3b34796197868e60bba7e34d44305db5402c04329c.jpg)

![](/api/attachments/CNAE9NFQ/fulltext/images/4ce7d1e8458aaf838605ac78e24aa17dc26087c0f0eebe1dee007827092f9b5f.jpg)  
Fig. 7. Surfaces of the score when the sectors apply the same order policy and the change in the customer demand increases.

![](/api/attachments/CNAE9NFQ/fulltext/images/337c9e75218904b06b380a2c13db3963ed0928cb341d7a4a07d3f05401491b56.jpg)  
Fig. 8. Optimal value of the score J with respect the change in the customer demand when the sectors apply the same order policy.

Table 1, when the behaviours are the same, the factory or the retailer have the best scores always i.e. one of the player on the extremes of the chain and the score increases or decreases monotonically going from one extreme to the other. In the case of different policies this does not happen and the winner can be in the middle of the chain.

In order to check the goodness of the solutions found by the GAs in the case of the first scenario, the fitness function, J, was assessed for the different steps in the customer demand (see Fig. 7). This evaluation was carried out on the entire search space with a resolution of 0.025.

It is possible to see that the minimum of the surfaces increases (see Fig. 8) when the change in the customer demand increases.

Another interesting common feature to all the surfaces of Fig. 7 is the presence of a valley around the value of $\beta { = } 0 . 6 .$ . Even if the best policy is not always located in the valley, a solution in that region it is always good (see Fig. 7). It was shown [9] analytically that the fitness function J has a global minimum, when $\beta { = } 0 . 6 .$ . The discrepancy with our results using GAs $\scriptstyle ( \beta = 0 . 0 1 6 )$ can be due to the flatness of surface J near $\beta { = } 0 . 6$ and the GAs algorithm is very slow and reaches the tolerance established in other points first. Anyway, even if GAs do not always find the best solution, the one it finds is a “good enough” solution in the sense that the fitness function assumes one of its lowest minima.

![](/api/attachments/CNAE9NFQ/fulltext/images/7a3455143d3020a9a5368b07c127791e9d8da3e7bb0c77ae1eff158b3f234891.jpg)  
Fig. 9. Contour plot of log(J ) considering one ordering policy in the $\alpha _ { S } - \beta$ space.

![](/api/attachments/CNAE9NFQ/fulltext/images/38905394d8266e922734ec41d23b2558baf43eccc64678a7baef3c47e32709da.jpg)  
Fig. 10. Surface plot of J of the area containing the lower values in the $\alpha _ { S } - \beta$ space.

For a step-change of 8 cases in the customer demand a surface with a higher resolution of 0.005 is calculated. In Fig. 9 it is possible to see the contour plot. For the area that contains the best solution a resolution of 0.001 is applied and the 3-plot is represented in Fig. 10. Very noticeable is the high number of local minima of J surface. This observation makes this problem not open to gradientbased optimisation algorithms.

When all sectors apply different ordering policies the fitness function has not been represented (for the second case) because of the high number of variables involved.

## 5. Conclusions

In the present study, the optimal parameters for the order policy of the Beer Game for a period of 60 weeks were analysed for the case where customer demand changes. Two different situations were considered: (i) all sectors having the same ordering policy or (ii) different policies were allowed for the different sectors.

The optimisation was performed using Genetic Algorithms. The technique of GAs is especially suited for this problem because of the complexity of the objective function with high number of local minima, and the many optimisation parameters involved.

Our results show that when the sectors apply the same order policy and the customer demand increases the best order policy to minimise the objective function, i.e. which ensures the minimum costs of the chain, is the one that increases the rate of adjustment of the stock when the stepchange increases. The rate of adjustment of the supply chain has to be slow until the step-change of 10 cases but after the step-change to 12 cases, which is the initial stock of the participants, the rate has to approach the 0.6 value. This value, even if is not the optimum, is always a good solution, i.e. it gives a low costs as can be seen in the 3-D plots of Fig. 7.

In the second scenario, when the participants have different order policies, solutions appear to be placed in certain regions of the parameter space, depending on the involved sector. We found that the best order policy for the Factory and the Distributor is to give more weight to the stock rather than the supply chain, whereas, the opposite applies for the Wholesaler and the Retailer.

It was shown that, for the Factory, the optimal values of $( \alpha _ { S } , \beta )$ , after a step-change of 10, are concentrated around (1,0) meaning that the Factory order policy has to try to adjust the stock quasi-instantaneously and does not need to consider the supply chain. On the contrary, the optimal order policy for the retailer sector, after a step-change of 5, consists in adjusting the stock slowly $( \alpha _ { S }$ small). This analysis gives no indications about the retailer rate of adjustment of the supply chain i.e. β varies between 0 and 1

The investigation has shown that the best policy, which ensures the minimum cost for the chain, for every customer demand step, is obtained when the sectors have different order policies.

From the point of view of the participants, in the first scenario, after a step-change of 11 the best score moves from the retailer to the factory. This happens because the step in the demand approaches the initial stock of 12 cases of beer and the participants start to have backlogs which influences the final score. The best scores are always in one of the two extremes of the chain: the Factory or the Retailer and the scores are always increasing or decreasing monotonically. In the second scenario, after the customer demand step-change of 14 cases, the winner changes from the distributor to the factory again and the winner can be any one of the four participants to the game.

Future development of this work will address the determination of the optimal policies with other forms of customer demand, for example periodic demand with changes in the frequency, and the evaluation of the optimal policy of the participants when the length of the chain increases.

## Acknowledgments

Insights and criticisms from anonymous referees significantly improved the presentation of the present work. The English revision by Dr. C. N. Murray is greatly appreciated.

## References

[1] F. Chen, Z. Drezner, J.K. Ryan, D. Simchi-Levi, Quantifying the bullwhip effect in a simple supply chain: the impact of forecasting, lead times, and information, Management Science 46 (2000) 436–443.

[2] H.L. Davis, S.J. Hoch, E.K. Easton Ragsdale, An anchoring and adjustment model of spousal predictions, Journal of Consumer Research 13 (1986) 25–37.

[3] H.J. Einhorn, R.M. Hogarth, Ambiguity and uncertainty in probabilistic inference, Psychological Review 92 (1985) 433–461.

[4] J.H. Holland, Adaptation in Natural and Artificial Systems, MIT Press, Cambridge, 1975.

[5] http://cs.felk.cvut.cz/\~xobitko/ga/.

[6] http://www.rennard.org/alife/english/gavintrgb.html.

[7] W.E. Jarmain, Problems in Industrial Dynamics, MIT Press, Cambridge, 1963.

[8] E. Mosekilde, E.R. Larsen, Deterministic chaos in the beer production–distribution model, System Dynamics Review 4 (1988) 131–147.

[9] E. Mosekilde, E. Larsen, J.D. Sterman, Coping with Complexity: Deterministic Chaos, in: J.L. Casti, A. Karlqvist (Eds.), Human Decision Making Behaviour. In Beyond Belief: Randomness, Prediction and Explanation in Science, CRC Press, Boca Raton, 1991.

[10] J.D. Sterman, Deterministic chaos in models of human behaviour: Methodological issues and experimental results, System Dynamics Review 4 (1988) 148–178.

[11] J.D. Sterman, Modeling managerial behaviour: misperceptions of feedback in a dynamic decision making experiment, Management Science 35 (1989) 321–339.

[12] J.S. Thomsen, E. Mosekilde, J.D. Sterman, Hyperchaotic phenomena in dynamic decision making, Systems Analysis Modelling Simulation 9 (1992) 137–156.

[13] A. Tversky, D. Kahneman, Judgement under uncertainty: heuristics and biases, Science (September 1974) 1124–1131.

[14] Y.-Z. Wang, Using genetic algorithm methods to solve course scheduling problems, Expert Systems with Applications 25 (2003) 39–50.

[15] Zh.T. Zhusubaliyev, E. Mosekilde, Bifurcations and chaos in piecewise-smooth dynamical systems, World Scientific, 2003.

![](/api/attachments/CNAE9NFQ/fulltext/images/a456f5280c26f85652779df35d8b26aaba51b102429289f02f08304acbb432d1.jpg)  
Dr. Fernanda Strozzi is a Contract Professor in the Engineering Department at Carlo Cattaneo University (Castellana, Italy). She graduated in Applied Mathematics from Pavia University and holds a PhD in Mathematics and Chemical Engineering from Twente University (Enschede, The Netherlands) on the application of chaos theory to chemical reactors. She was a Marie Curie fellowship from 1993 to 1995. Her current research interests include the application on complex systems theory to

logistic chains and on the analysis of financial time series.

![](/api/attachments/CNAE9NFQ/fulltext/images/71724bdf7a10676ffe7ed9b9d9e162c8f78c6b77cd64d80d96cec3e946cf95be.jpg)

Mr. Jordi Bosch Pagans is a PhD student at Manchester University. He graduated in Chemical Engineering at IQS (Barcelona, Spain) in June 2004. His PhD is focused on the development of an early warning detection system for the initiation of runaway reaction in chemical reactors using techniques from nonlinear time series analysis. He has collaborated with Castellanza University, the Joint Research Center of the European Commission (Ispra, Italy) and

the Health and Safety Laboratory (Buxton, UK) in the frame of an EU funded project (AWARD, G1RD-CT-2002-00499).

![](/api/attachments/CNAE9NFQ/fulltext/images/f66d75112d05e46315148a75bdae2e0179602d3fb6feeb79c7fa1282403d702e.jpg)

Dr. José-Manuel Zaldívar Comenges is a Senior scientist at the Institute for Environment and Sustainability of the Joint Research Centre of the European Commission where he initially joined in 1987. He obtained a MS in organic chemistry at IQS (Barcelona, Spain) and a PhD in Chemical Engineering from Twente University (Enschede, The Netherlands). He has published numerous papers in safety of chemical reactors, mathematical modelling and the

application of nonlinear dynamical systems theory to several fields. His current research interests include ecological modelling and the interactions between ecosystem and contaminants.
