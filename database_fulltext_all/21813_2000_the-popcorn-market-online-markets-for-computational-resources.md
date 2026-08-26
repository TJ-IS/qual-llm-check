---
otero_id: 21813
otero_key: "UAA9A8NF"
title: "The POPCORN market. Online markets for computational resources"
authors: "Ori Regev; Noam Nisan"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00067-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The POPCORN market. Online markets for computational resources<sup>q</sup>

Ori Regev <sup>a,)</sup>, Noam Nisan <sup>a,b</sup>

Institute of Computer Science, Hebrew UniÕersity, Jerusalem, Israel School of Computer Science, Interdisciplinary Center, Herzliya, Israel

## Abstract

The POPCORN project provides an infrastructure for globally distributed computation over the whole Internet. It provides any programmer connected to the Internet with a single huge virtual parallel computer composed of all processors on the Internet, which care to participate at any given moment. POPCORN provides a market-based mechanism for trade in CPU time to motivate processors to provide their CPU cycles for other peoples’ computations. ‘‘Selling’’ CPU time is as easy as visiting a certain web site with a Java-enabled browser. ‘‘Buying’’ CPU time is done by writing a parallel program using the POPCORN paradigm. A third entity in the POPCORN system is a ‘‘market’’ for CPU time, which is where buyers and sellers meet and trade. The POPCORN system may be visited on our web-site: http:<sup>rr</sup>www.cs.huji.ac.il<sup>r;</sup>popcorn. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Global computation; Internet; Resource allocation; Markets; Java

## 1. Introduction

There are currently millions of processors connected to the Internet. At any given moment, many, if not most of them, are idle. An obvious and appealing idea is to utilize these idle processors for running applications that require large computational power. This would allow what may be termed ‘‘global computing’’ — a single computation carried out in cooperation between many processors world wide.

Similar ideas in the context of local area networks are quite well known by now, especially due to the influence of the work on ‘‘Network of Workstations’’ <sup>w</sup> <sup>x</sup> 1 . There are several added complications, though, in the global case of cooperation over the whole Internet. First, there are major technical difficulties due to code mobility, security, platform heterogeneity, and coordination concerns. Then, there is a matter of scale as the Internet is much more ‘‘distributed’’: The communication bandwidth is smaller, the latency higher, the reliability lower. On the positive side, the potential number of processors is huge.

A much more fundamental difference is due to the distributed ownership of the processors on the Internet. Since each processor is owned and operated by a different person or organization, there is no a-priori motivation for cooperation Why should my com-Ž puter work on your problem? . Clearly, a motivation.

for cooperation, such as payments for CPU time, must be provided by a global computing system.

The POPCORN system provides an infrastructure for such ‘‘global computation’’ addressing all these difficulties. It has been implemented and was operable until recently for over a year through its web site over the Internet 38 . Descriptions of the system can<sup>w</sup> <sup>x</sup> be found in Refs. 6,21,32,37 .<sup>w</sup> <sup>x</sup>

This paper focuses on POPCORN’s approach to the last issue, that of motivating cooperation. The POPCORN system provides an online electronic market for trade-in CPU time. Buyers and sellers of CPU time connect to it via the Internet, and the market matches buyers and sellers according to economic criteria. It should be emphasized that the buyers and sellers are computer programs acting forŽ humans rather than directly humans. It seems very . likely that such totally automated electronic markets will play a large role in many forms of Internet cooperation not just for CPU time , and that generalŽ . mechanisms for such markets need to be developed and understood.

The design and implementation of such online electronic markets will of course draw on the vast literature available regarding real-world markets <sup>w</sup> <sup>x</sup> 2,11–13,35 . However, one should note that many differences exist. First, there are many technical issues of communication, implementation, etc. Second, the fact that the market is not intended for humans, but rather for programs, makes a difference. Third, in many cases, and in particular in the case of the POPCORN market, even the basic definitions of money, goods and trade need to be defined. We hope that our experiences with the POPCORN market may shed further light on several aspects of online electronic markets.

## 1.1. Paper structure

Section 2 provides an overview of the POPCORN system; further information can be found in Refs. <sup>w</sup> <sup>x</sup> 6,21,32,37 . Section 3 describes the outline of the economic notions and mechanisms that underline the POPCORN system. Section 4 provides preliminary analysis of the POPCORN markets. Section 5 describes our simulations of the POPCORN trade. In Section 6, we mention some related works and Section 7 outlines directions for further research.

## 2. An overview of the POPCORN system

The POPCORN system provides an infrastructure for global computation over the Internet. POP-CORN’s basic function is to provide any programmer on the Internet with a simple virtual parallel computer. This virtual machine is implemented by utilizing all processors on the Internet that care to participate at any given moment. The system is implemented in Java and relies on its ubiquitous ‘‘applet’’ mechanism for enabling wide-scale safe participation of remote processors.

There are three distinct types of entities in the POPCORN system.

Ž . Ž . 1 The parallel program written in Java using the POPCORN paradigm. This program acts as a CPU time ‘‘buyer’’. The program is written using the POPCORN programming paradigm that was designed to fit ‘‘global computing’’. This paradigm is described in Refs. 21,32 .<sup>w</sup> <sup>x</sup>

Ž . 2 The CPU time ‘‘seller’’ who allows its CPU to be used by other parallel programs instead ofŽ standing idle . This is done as easily as visiting a . web site using a Java-enabled browser, and requires no download of code.

Ž . 3 The ‘‘market’’ which serves as a meeting place and matchmaker for buyers and sellers of CPU time.

The POPCORN programming paradigm, used by the buyer program, achieves parallelism by concurrently spawning off many sub-computations, termed ‘‘computelets’’. The POPCORN system automatically sends these computelets to a market chosen byŽ the user , which then forwards them to connected. CPU-time sellers, who execute them and return the results. The matching of buyers and sellers in the market is dynamic, is done according to economic mechanisms, and results in a payment of the buyer to the seller.

The system is intended for coarse-grained parallelism. The computational efficiency is mostly determined by the ratio between the computation time of computelets to the communication effort needed to send them and handle the overhead. To achieve high efficiency, computelets should be relatively heavy in terms of computation time. Currently, seconds of CPU time per computelet are a minimum, and tens of seconds seem more typical. For very large-scale computations, even hours make sense. Sample application for POPCORN includes brute-force search, code breaking, simulated annealing, genetic algorithms, and game-tree evaluation.

Detailed descriptions of the POPCORN system can be found in Refs. 6,21,32 . Further, and up to<sup>w</sup> <sup>x</sup> date, information can be found on the POPCORN web site 37 .<sup>w</sup> <sup>x</sup>

## 3. A micro-economy of CPU time

## 3.1. The goods

The first thing one must ask in such an electronic market is what exactly we are trading in. The answer ‘‘CPU time’’ is not exact enough since it lacks specifics such as units, differences between processors, deadlines, guarantees, etc. A basic tradeoff in answering this question is between allowing the traders very specific description of the goods, and between maintaining a small number of uniform types of goods with larger market size. Our approach has been to emphasize uniformity in the initial implementation, but building the infrastructure to allow specialization in later versions.

Our basic goods are the ‘‘Java operations’’ JOPs .Ž . This is the Java equivalent of the commonly used, though imprecise, FLOPS. Of course, there are different types of Java operations, with different costs in different implementations, so we define a specific mix of computations and use this mix as a definition. Each computelet takes some number of JOPs to execute, and the price for a computelet is proportional to the number of JOPs it actually took to compute remotely. This is measured or actually, Ž approximated using a simple benchmark we piggy-. back on each computelet.

Our experience suggests that this mechanism works well. Still, two main disadvantages are obvious. First, the benchmark is run on the sellers’ computer and this computer may cheat and report higher numbers. Such cheating entails modificationŽ of the browser used on the sellers’ side, but is still possible with some effort. Second, it is imprecise by . nature, as well as has an overhead. We have thus also provided a second type of ‘‘good’’ that can be traded: simply the computation of a single computelet. This does not require any benchmarking, but may be troublesome for the seller since he has no a-priori control over the computation time of the computelet. Still, this simple mechanism is very proper in many situations such as the case of a repeated buyer of CPU time, the case of ‘‘friendly’’ non-financial transactions, or the case where computelet’s size is set administratively.

## 3.2. The money

One may think of several motivations for one processor to provide CPU time to another. They may belong to the same person or organization, one might donate its CPU time ‘‘for a good cause’’, the processor may get something in return, or it may get CPU time in return at a later time. As in real life, all of these motivations, as well as others, may be captured by the abstract notion of money. This ‘‘money’’ may be donated, traded, bartered, loaned, converted to other ‘‘currency’’, etc.

This is the approach taken in POPCORN: we define an abstract currency called a ‘‘popcoin’’. All trade in CPU time is ultimately done in terms of popcoins. In our current implementation, popcoins are just implemented as entries in a database managed by the market, but they can be easily implemented using any one of the electronic payment schemes. Each user of the POPCORN system has a popcoin account, paying from it for CPU time required, or depositing into it when selling CPU time. The market automatically handles these financial aspects throughout the computation. Once this mechanism exists, all of the motivations described above are obtained by administrative decisions regarding how you view popcoins. If you want to get true payment for CPU time, just provide conversion between popcoins and US\$ we do not . . . . If you areŽ . in a friendly situation, just ignore popcoin amounts. If you want to loan CPU cycles, just buy CPU time with popcoins and at another time, sell your CPU time for popcoins.

## 3.3. Buying and selling CPU time

The programmer writing a parallel POPCORN application is in fact buying CPU time. Basically, the parallel program must offer a price for the computation of each computelet. The payment is executed on sellers’ return of the answer to the market, and is deducted from the buyers’ account in the market Žwhich must be specified before the computation can proceed . Technically, each computation packet con-. structs a ‘‘contract’’ object that encapsulates the offer. The contract specifies the prices offered, whether the price is per computelet or per JOP, and the market mechanism required for this transaction Ž . see below . The contract may be hard-coded into the program; alternatively, we provide a user-level tool for specifying the contract.

Selling CPU time is done as easily as visiting a page on the web with a Java-enabled browser. This page contains an applet that starts working on the sellers’ computer and which repeatedly receives computelets and computes them. In the most direct form, a seller visits the market’s web site where he is asked to provide his account information name and Ž password . Once this information is provided, a ‘‘start.

computing’’ button starts the CPU-selling process, and all popcoins earned are deposited into this account. By default, each seller simply auctions his CPU time to the highest bidding per JOP prospec-Ž . tive buyer. Optionally, the seller may also enter his preferences for the trade, e.g., specifying pricing information Fig. 1 . Ž .

An alternative mechanism, which does not require the seller to hold an account or to be compensated in popcoins, exists. In this variant, a ‘‘seller’’ visits a web page that is of some interest to him. In addition to this interesting information, the page contains the ‘‘POPCORN logo’’. This logo has two main functions. First, it is an applet that receives computelets and executes them. Second, this logo explicitly informs the user that this is going on. In this situation, the seller is in fact bartering his CPU time for the information on the web page. This can be an on-line game, a picture, or any other type of information. We maintain a little ‘‘gallery’’ of such web pages <sup>w</sup> <sup>x</sup> 36 . In effect, we have a three-way trade here: the seller provides CPU time and gets information; the page owner ‘‘publisher’’ provides information andŽ . gets popcoins; and the buyers provide popcoins and get CPU time. Exact details on how to become a publisher can be found at Ref. 39 Fig. 2 .<sup>w</sup> <sup>x</sup> Ž .

![](/api/attachments/UAA9A8NF/fulltext/images/f57b28a76f447dd4a03e665ae4e0966ae4ec9b1d1be30ecff97c6e7cc005f156.jpg)  
Fig. 1. POPCORN seller web page.

## 3.4. The market

The most immediate function of the market is to simply serve as a well-known location which buyers and sellers come to, instead of trying to look for each other all over the Internet. There can be manyŽ different markets, but supposedly, each is in a ‘‘well-known’’ location. Obviously, this makes the . market a communication bottleneck of the whole system, but as long as the computation done by each computelet is CPU-time consuming enough, relative to the market overhead, a single market can handle large numbers of buyers and sellers. The market is a trusted intermediary and is responsible for matching buyers and sellers, for moving the computelets and results between them, as well as for handling all payments and accounts. The implementation of the market involves a server that buyers can connect to as clients, as well as a set of web pages with applets embedded in them and a supporting server for theŽ . sellers to connect to.

The most important aspect of the market is to match buyers and sellers according to economic criteria. There are two basic design goals for the market mechanism.

Ž . 1 The allocations should be economically efficient, i.e., maximize the global utility by allocating CPU time to those with the highest utility for this time. A necessary condition for this is the second requirement.

Ž . 2 The market mechanism should motivate the buyers and sellers to reveal their true utility of the CPU time i.e., the mechanism should be ‘‘incentiveŽ compatible’’ 16 . This frees them from strategic <sup>w</sup> <sup>x</sup>. considerations, and we feel especially important in an electronic market setting in which the bidding is pre-programmed rather than interactively done by humans.

![](/api/attachments/UAA9A8NF/fulltext/images/5401bd2e1228b38860416b8bc3b343d2e363b1dccf92da9832cc6a8f7a109098.jpg)  
Fig. 2. A game web page with the POPCORN logo top-right corner . Ž .

We have three different mechanisms currently available. They are currently handled as separate internal markets and each buyer and seller may choose which of these mechanisms he desires inŽ addition to choosing whether the payment is per JOP or per computelet — defaults exist for all these choices, of course . All our mechanisms are of the. sealed-bid type ‘‘fire and forget’’ . They, thus, re- Ž . quire only a single round of communication. In addition, the mechanisms are all efficiently computable usually requiring just a few hashing andŽ priority queue operations per computelet ..

The first mechanism is a repeated Vickrey auction <sup>w</sup> <sup>x</sup> 40 . Here, the CPU time of the sellers is auctioned among current buyers — separately for each computelet. The catch in a Vickrey auction is that the price paid by the buyer is not the one offered by him, but rather the second highest price offered in the auction.

The second mechanism we provide is a simple sealed-bid double auction DA 15 . In this case,Ž . both buyers and sellers offer a low price and a high price, as well as a rate of change. The sellers start with an offer of the high price — an offer that is automatically decreased at the specified rate, until a buyer is found or the low price reached . Similarly, Ž . buyers start at the low price, and their offer is automatically increased until a seller is found or theŽ high price is reached . When a buyer ‘‘meets’’ a. seller, the buyers’ computelet is sent for execution on the sellers’ machine and the payment is at the meeting price. This mechanism is very dynamic and easy to define and implement.

The third mechanism we provide is a repeated clearinghouse DA k-DA 15 . This mechanism is Ž . <sup>w</sup> <sup>x</sup> similar to the simple DA, except for the fact that in each round, more than one buyer–seller pair is matched. At fixed time intervals, all the sealed-bids of buyers and sealed-asks of sellers are used to calculate current demand and supply curves the Ž demand and supply curves are step functions . These. curves are intersected, the equilibrium price is calculated, and the single price is used for all the transactions of that round. We take the trading price to be the middle of the interval of possible clearing prices Ži.e., we use a k-DA with $k = 1 / 2 )$ .

## 4. Towards an analysis of the POPCORN market mechanisms

The basic question about these market mechanisms is whether they work well in terms of finding an economically efficient matching of buyers and sellers in the dynamic situation of the Internet. In addition, the computational efficiency of reaching this matching is of importance, as to enable the market to function online under high loads. From an economic point of view, our main interest is in checking whether the gains-from-trade that are generated by our mechanisms’ allocations are maximized. The results of our analysis of the market mechanisms are quite sensitive to the exact model of the buyers and sellers as well as to the economic utility placed on time and to the information available to the players. Some results from game theory and mechanism design literature 16 are directly or <sup>w</sup> <sup>x</sup> indirectly applicable, yielding both positive and negative results. In this section, we describe these analytical steps towards analysis, while in Section 5, we describe results of our simulation, using the same theoretical framework.

One way of analyzing a POPCORN market is to view its rules as defining a multiple-round game of incomplete information, in which the number of players may change as time progresses and the players’ actions in one round affect the future rounds. Each trade-round at the market corresponds to one round in the game. The players of the game are the selfish buyers and the sellers who seek to maximize their private utility. The game that fully corresponds to the POPCORN trade is difficult to analyze, and we make some simplifying assumptions in our discussion below.

In order to model a buyer, we assume that a buyer has a type $V _ { i } ^ { 0 }$ , drawn from a probability distribution $F .$ The buyer’s type corresponds to his Õaluation of a JOP at time 0, and once a buyer’s type was determined at time 0, his valuation of a JOP inŽ terms of time 0 decays as the calculation of that. JOP is done further into the future. Formally, buyer i’s valuation of the calculation of a JOP at period t in terms of period 0 is $V _ { i } ^ { t } = \alpha ^ { t } V _ { i } ^ { 0 }$ , where $0 \leq \alpha \leq 1$ is a discount factor common to all buyers. We also assume that if a buyer cuts a deal at time $t ,$ and buys a computation of L JOPs, at a price $p ,$ he enjoys a utility of $L ( V _ { i } ^ { t } - p )$ . A buyer generates a stream of orders, beginning with a ‘connect’ order, followed by ‘bid’ orders, and finally, a ‘disconnect’ order.

Similarly, our model of a seller states that a seller is defined by a type $e _ { i } ,$ drawn from a probabilitydistribution G. The seller’s type corresponds to his expenses per a unit of time. Another attribute of the seller is his machine’s speed of $z _ { i } \ { \mathrm { J O P s } } { \mathrm { / s } } ,$ which is drawn from a probability distribution H. We assume that if a seller cuts a deal to sell a computation of $L$ JOPs, at a price $p ,$ he enjoys a utility of $L ( e _ { i } / z _ { i } - p )$ A seller generates a stream of orders, beginning with a ‘connect’ order, followed by one or more ‘ask orders, and finally, a ‘disconnect’ order. We assume that both buyers and sellers know their type a-priori Ži.e., we assume that the independent priÕate Õalue model <sup>w</sup> <sup>x</sup> 26 holds . We also assume that the seller. publishes no information about his client’s computer, that the auction rounds are held at discrete points in time and that all the constraints imposed by the POPCORN architecture are satisfied.

## 4.1. The repeated Vickrey auction mechanism

A well-known result in auction theory is that it is a dominant strategy for a buyer in a Vickrey auction to bid his true valuation of the good being auctioned <sup>w</sup> <sup>x</sup>40 and that the Vickrey auction is a direct-reÕelation mechanism <sup>w</sup> <sup>x</sup> 16 . Thus, the outcome of a single round of the Vickrey auction satisfies the strong criterion of dominant strategy equilibrium. When the players play their equilibrium strategies, the outcome of a single round is efficient — the buyer who has the highest valuation for the good wins it.

However, our Vickrey-based mechanism is executing a Vickrey auction repeatedly and the properties of the single round do not necessarily hold. Despite this theoretical possibility, we do not know of practical ways by which programs can gainfully employ strategic reasoning in the context of the POPCORN market. If we do assume that the buyers and sellers are truth-tellers i.e., non-strategic buyersŽ and sellers and that the sellers are homogenous, then .

we can show that the mechanism maximizes the welfare of the economy. The proof is straightforward and we do not bring it here; please refer to Ref. 33<sup>w</sup> <sup>x</sup> for details.

Our assumptions about the homogeneity of the buyers and sellers are not reasonable in Internet-based markets. The machines connected to the Internet differ in their computation power, connection quality; the costs of connection differ from one ISP to another, etc. If we relax our assumption that the sellers’ costs are equal or that the sellers’ machines are identical, the efficiency breaks. The reason is obvious: the mechanism chooses the sellers arbitrarily, based solely upon their arrival time. Relaxing the assumption that the buyers and sellers know their valuations also leads to inefficient outcomes. On the other hand, the efficiency result holds when we assume asymmetric buyers 33 . Taking these issues <sup>w</sup> <sup>x</sup> into account will naturally complicate the system and may be a subject for further research.

## 4.2. The DA mechanisms

We have seen that in the general case, the repeated Vickrey mechanism described in Section 4.1 is socially inefficient. One reason for inefficiency is that it does not introduce competition among the sellers. A possible remedy is to consider DAs.

## 4.2.1. A simple DA

The simple DA resembles the simultaneous execution of two ‘‘first-price sealed bid auctions’’ <sup>w</sup> <sup>x</sup> 26,29 . Very much like in the case of first-price sealed bid auction 25,26,28–30 , there is no domi-<sup>w</sup> <sup>x</sup> nant strategy equilibrium in the simple DA. We are left with a weaker criterion of Bayesian Nash equilibrium   16 . In addition, it is not a direct-revelation mechanism, and each round of our auction is not necessarily Pareto efficient. We return to the simple DA in Section 5.

## 4.2.2. The k-DA

In Ref. 34 it is shown, for a single round of<sup>w</sup> <sup>x</sup> k-DA that if each buyer requests a single good and each seller has a single good, then as the number of buyers and sellers grows, the incentive for buyers and sellers to falsely report their types diminishes. In this case, the gains from trade converge to the maximal possible value. However, this result does not hold when each trader is interested in multiple units. Furthermore, multiple rounds may lead to inefficient results when the mechanism is executed against an adversary who seeks to minimize the gains from trade. It can be shown that the repeated clearinghouse algorithm is not  — competitive for any constant <sup>w</sup> <sup>x</sup> 33 .

Mendelson 27 analyzes a mechanism very simi-<sup>w</sup> <sup>x</sup> lar to ours, assuming that the bids and asks are uniformly distributed over some interval, that the arrival of orders from buyers and sellers are governed by identical Poisson processes, and that the players are not strategic they report their true valua- Ž tions . Mendelson’s analysis implies that ‘‘we can- . not be very far from that price that maximizes the gains from trade most of the time’’. At the time of writing these lines, we have insufficient empirical data for supporting or refuting Mendelson’s assumptions.

## 5. Trade simulation

In this section, we check the market’s behavior and characteristics by simulating the trade that results from the dynamic arrival and departure of various buyers and sellers. There are many empirically open questions, of which we consider only a few. Perhaps the most interesting issues are the allocation’s efficiency in a dynamic environment and the price response to supply and demand shocks. In addition, we check the market’s adaptivity and the relation between a seller’s or buyer’s offer and his Ž . probability of executing the trade.

We conducted most of the experiments in a constrained environment. In this environment, the buyers and sellers do not behave strategically, each buyer has a single computelet to compute, and each seller wishes to compute a single computelet. Overall, in the very simple settings of our experiments, the results are promising: the markets present the expected behavior in terms of price trends, the efficiency of their allocation is surprisingly high, the speed of the economy’s adaptation is quite high, the prices are relatively stable, and reservation prices have the expected effect.

## 5.1. A test-bed for market simulations

In order to simulate the operation of the various POPCORN market mechanisms, we have implemented a simulation test-bed. The implementation provides much flexibility in varying the parameters that influence the trade. Fig. 3, below, provides a schematic description of the simulation test-bed architecture.

The heart of the simulation test-bed is a Market Simulator object, which coordinates among the various objects. The Market Simulator is connected to the POPCORN market through a Market Adapter, which replaces the real POPCORN communication layer. This enabled us to simulate the trade without requiring hundreds of computers. The Market Simulator contains an Agents Factory, which creates the buyers and sellers according to stochastic processes of some kind. We used a Poisson Process Generator with configurable parameters in our simulations.

Upon creation, a Simulated Buyer or Seller readsŽ . his characteristics from a file. Most of the parameters that it reads define a probability distribution, from which the Simulated Buyer draws the real parameter to be used during the simulation. One important characteristic of the Simulated Buyer is his computelet spawning process, which is also governed by a stochastic event-generator. The computelet length is drawn from a uniform probability distribution.

![](/api/attachments/UAA9A8NF/fulltext/images/09a00fd1b43983e6b3267867cb3bba0ade4fe1c12c105fb3874285ec674b0c0f.jpg)  
Fig. 3. The simulation test-bed architecture.

![](/api/attachments/UAA9A8NF/fulltext/images/69effbff3fdff7b29af4b7271bcbbc0dc2c625f990d1b6a3e121c16443d8d000.jpg)  
Fig. 4. Convergence to steady state in the simple DA.

Another important characteristic of a buyer is his valuation for the good and the derived bidding strategy. A strategy is defined by an open bid, bid increment rate, and maximum bid. Simulated Sellers are very much like Simulated Buyers. Their important attributes are their ask and selling strategy, machine speed, and lifetime period.

## 5.2. Simulations and results

## 5.2.1. Price response to changes in the relatiÕe supply and demand

In this set of simulations, we measure the price as a function of the supply, while holding the demand Ž . stochastically fixed at some level. By collecting a large number of such samples, we are able to map the average price curve. The environment is consisted of truth-telling buyers and sellers, where each buyer wishes to compute a single packet of random size and each seller wishes to compute a single packet. All the sellers’ machines are identical. Buyers’ packets valuations and sellers’ costs are drawn uniformly from the interval 0, 30 . The Poisson <sup>w</sup> <sup>x</sup> process that determines the arrival of buyers remains constant, with fixed at 0.001 the time units areŽ milliseconds . The Poisson process that governs the. arrival of sellers is different in each simulation and thus, we achieve the changes in the supply. In a typical simulation, we used a few hundreds simultaneously executing agents.

We have run 40 simulations for each mechanism, three times for each value of the supply process . All measurements were made during a steady-state phase i.e., when the percentage of fulfilled requestsŽ out of the total number of requests was stable . It.

was reached after about 5 min of simulation. Two examples for convergence to steady state are given in Figs. 4 and 5.

The average duration of a simulation was 30 min. We summarized all price information in Fig. 6. Relative supply is on the x-axis and the resulting average price at steady state is on the y-axis. In general, these results comply with our intuition. It is evident that an increase in the supply results in a decrease in the average price. Consider, for example, the clearinghouse mechanism. In this case, increasing the supply process results in the flattening of the supply curve in every round. Since the prices are determined in this case by finding the crossing Ž . point of the demand and supply curves, for each value of , we get a different point on the expected demand curve.

## 5.3. Social efficiency of the allocations

In order to evaluate the economic efficiency of these allocations, we compare them to the optimaloffline mechanism. That is, we compare the generated welfare of POPCORN’s online mechanisms to that generated by a perfect mechanism that, in advance, has all the information about the buyers’ and sellers’ orders. The quotient of these two numbers represents the relative efficiency of the mechanism. This comparison is ‘‘unfair’’ towards the POPCORN online mechanisms, as they should be compared with the best online mechanism that bases its decisions on the information that is available at runtime. Nevertheless, the comparison with the optimal offline allocation is still enlightening.

![](/api/attachments/UAA9A8NF/fulltext/images/0e9d714c428d89987f66b14eb137a10ee494ef98b3438caba04edfc68e0fda36.jpg)  
Fig. 5. Convergence to steady state in the Vickrey auction.

![](/api/attachments/UAA9A8NF/fulltext/images/9be835c80cdaa92c3cd59f36d0a00357151cb2ca71d644af2b6a1142847703a9.jpg)  
Percent Of Buyers Fulfilled Requests  
Fig. 6. Prices under different buyer<sup>r</sup>seller ratios.

Fig. 7 shows that the mechanisms’ efficiency is quite high. In the case of the clearinghouse mechanism, it is very high with the average of 96%. We also see that the simple DA and Vickrey do not achieve such good results. The source of this difference is sellers with high costs that are matched to buyers instead of sellers with lower costs who arrived later. When the lower-costs sellers arrive, it is too late, since the relevant buyers have already left.

This effect has lower influence over the clearinghouse because in this mechanism, the trade is executed in fixed time intervals.

## 5.4. Price stability

For a particular mechanism, the standard deviation of prices remains stable at various supply levels. This standard deviation should be considered in conjunction with the price level and we take the quotient of the measured standard deviation with the average price level. We can use these measurements to compare the two DAs. The average value of the quotient in the clearinghouse market is 0.147, and in the simple DA, it is 0.33. Thus, the clearinghouse is much more stable. Figs. 8 and 9 below depict the price behavior in a typical run of two mechanisms.

![](/api/attachments/UAA9A8NF/fulltext/images/b09a28acab58c313d8e7a44827e30861faaa9a3c11064beda3386dbafaebb3fd.jpg)  
Fig. 7. Economic efficiency under different buyer<sup>r</sup>seller ratios.

![](/api/attachments/UAA9A8NF/fulltext/images/8f16a0efc8a98b4fc65ef5dd1c69870d2ee170049dbbfa002615584c8c28b19e.jpg)  
Fig. 8. Prices in the Vickrey auction.

## 5.5. The role of reserÕation prices

Normally, a higher buyer offer results in a higher probability of buying. Symmetrically, a lower-ask price results in a higher probability of selling. This is verified for our markets and Figs. 10 and 11 depict this property for the clearinghouse market. Note that buy offers that are lower than a certain threshold, or asks that are higher than a threshold, never execute. We obtained similar results for the repeated Vickrey auction and the simple DA.

![](/api/attachments/UAA9A8NF/fulltext/images/1274e86ba2eeb36c7d20e39c054b4349cefbb028beeb89677bfba2fd6918d37e.jpg)  
Fig. 9. Prices in the clearinghouse.

![](/api/attachments/UAA9A8NF/fulltext/images/23a0ef0413d144be42a6fc4e0b392123eff49a5af213dd5ae25e588d81607852.jpg)  
Fig. 10. The probability of executing vs. the bid in the clearinghouse auction.

## 5.6. Other market properties

In the above simulations, the demand was held fixed, and the supply varied. Qualitatively, we got similar results in the case of demand shifts. Similarly, we got the same results when buyers and sellers are interested in more than a single packet and when the sellers’ machines are heterogeneous.

## 6. Related works

The basic idea of ‘‘stealing cycles’’ on local networks is well known, and is the basis for ‘‘Network of Workstations’’ 1 and many related pro-<sup>w</sup> <sup>x</sup> jects. The same idea over the Internet, with its different considerations, is much less developed. Only recently, with the availability of the Java language, has a general mechanism for global computing been possible. Several general systems using Java have been designed, usually concentrating on a single aspect of global computation 3,5,9 . These<sup>w</sup> <sup>x</sup> systems do not base their operation on economic principles, however.

![](/api/attachments/UAA9A8NF/fulltext/images/627ddb123264acb7109147619477140a360ed0c72e0490f04064b2d148c11f2f.jpg)  
Fig. 11. The probability of selling vs. ask in the clearinghouse auction.

The idea to use economic techniques, models, and intuitions, for solving a computational problem and in particular for solving allocation problems has gained popularity in recent years 4,8,10,14,17, <sup>w</sup> 18,20,22,41 . Similarly, the allocation of network <sup>x</sup> resources and the allocation of resources over the Internet received much attention 10,17,19,20, <sup>w</sup> 22,23,31 , but we are unaware of systems that allo-<sup>x</sup> cate CPU time over the Internet and are market-oriented. The systems that allocate CPU time are generally designed to be used in LANs. For example, Spawn 41 , Enterprise 24 , and Challenger 7 may <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> <sup>w x</sup> not be applicable to the Internet due to their communication requirements.

## 7. Directions for further research

We consider extending this work in the following directions.

Ž . 1 A comprehensive efficiency analysis of the DA is still needed. We did not conclude with a strong efficiency result even for an unrealistic model and only showed evidence for the mechanism’s efficiency.

Ž . 2 An obvious extension to our simulations is to experiment with strategic buyers and sellers. Our early experiments with buyers and sellers that shade their bids and asks hint to results similar to ours in the clearinghouse.

Ž . 3 POPCORN was designed in such a way that we can replace parts of it. It is easy to plug-in a matching mechanism that bases its operation on more conventional non-economic-based load-balancing algorithms. A comparison with such mechanisms should be carried out.

Ž . 4 We view POPCORN as a case study from which we learn on a larger family of economic-oriented computational systems. The same markets may be used for other goods. This, however, may require the definition of other billing schemes.

Ž . 5 The central market is a bottleneck and the system does not scale. When connected to a 10 Megabit LAN, it can handle up to 70 buyers and sellers. This is not good enough in the context of the Internet. We consider replacing the single market with a network of cooperating and competing markets.

## Acknowledgements

Supported by a grant from the Israeli Ministry of Science.

## References

<sup>w</sup> <sup>x</sup> 1 T.E. Anderson, D.E. Culler, D.A. Patterson, A case for networks of workstations: NOW, IEEE Micro 1995 Feb. .Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 K. Arrow, F. Hahn, General Competitive Analysis, North-Holland, Amsterdam, 1978.

<sup>w</sup> <sup>x</sup> 3 A. Baratloo, M. Karaul, Z. Kedem, P. Wyckoff, Charlotte: metacomputing on the web, in: Proceedings of the 9th Conference on Parallel and Distributed Computing System,1996.

4 N.R. Bogan, Economic allocation of computation time with computation markets, Master’s thesis, Massachusetts Institute of Technology, Department of Electrical Engineering and Computer Science, May 1994.

<sup>w</sup> <sup>x</sup> 5 T. Brecht, H. Sandhu, M. Shan, J. Talbot, ParaWeb: towards word-wide supercomputing, in: Proceedings of the Seventh ACM SIGOPS, European Workshop, Connemara, Ireland, 1996, pp. 181–188, September .Ž .

<sup>w</sup> <sup>x</sup> 6 N. Camiel, S. London, N. Nisan, O. Regev, The POPCORN project — an interim report, distributed computation over the Internet in Java, in: Proceedings of the Sixth International World Wide Web conference, 1997. http:<sup>rr</sup>www. cs.huji.ac.il <sup>r</sup> <sup>;</sup> popcorn <sup>r</sup> documentation<sup>r</sup> www 6 <sup>r</sup> poster. html.

<sup>w</sup> <sup>x</sup> 7 A. Chavez, A. Moukas, P. Maes, Challenger: a multi agent system for distributed resource allocation, in: Proceedings of the First International Conference on Autonomous Agents, 1997, Marina del Ray, California, February .Ž .

<sup>w</sup> <sup>x</sup> 8 J.Q. Cheng, M.P. Wellman, The WALRAS algorithm: a convergent distributed implementation of general equilibrium outcomes, Computational Economics, in press.

<sup>w</sup> <sup>x</sup> 9 B. Christiansen, P. Cappello, M.F. Ionescu, M.O. Neary, K.E. Schauser, D. Wu, in: Javelin: Internet-Based Parallel Computing Using Java,ACM Workshop on Java for Science and Engineering Computation, 1997, June .Ž .

<sup>w</sup> <sup>x</sup> 10 R. Cocchi et al., Pricing in computer networks: motivation, formulation, and example, IEEE Transactions on Networking 1 6 1993 614–627.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 G. Debreu, Theory of Value, Wiley, New York, 1959.

<sup>w</sup> <sup>x</sup> 12 I. Domowitz, Automating the continuous double auction in

practice: automated trade execution systems in financial markets, the double auction market institutions, theories, and evidence, in: D. Friedman, J. Rust Eds. , Proceeding of TheŽ . Workshop On Double Auction Markets,1991, Santa Fe,Ž New Mexico, June ..

<sup>w</sup> <sup>x</sup> 13 W.J. Eitman, S.C. Eitman, Nine Leading Stock Exchanges, Michigan International Business Studies, The University of Michigan, Ann Arbor, 1968.

<sup>w</sup> <sup>x</sup> 14 D. Ferguson, Y. Yemini, C. Nikolaou, Microeconomic algorithms for load balancing in distributed computer systems, in: Eighth International Conference on Distributed Computing Systems, 1988.

<sup>w</sup> <sup>x</sup> 15 D. Friedman, The double auction market institution: a survey, in: D. Friedman, J. Rust Eds. , The Double AuctionŽ . Market Institutions, Theories, and Evidence, Proceeding of The Workshop On Double Auction Markets, 1991, Santa Fe,Ž New Mexico, June ..

<sup>w</sup> <sup>x</sup> 16 D. Fudenberg, J. Tirole, Game Theory, MIT Press, 1995.

<sup>w</sup> <sup>x</sup> 17 A. Gupta, D.O. Stahl, A.B. Whinston, Managing the Internet as an Economic System, University of Texas at Austin, Research Papers, 1994.

<sup>w</sup> <sup>x</sup> 18 B. Huberman, Computation as economics, in: Second International Conference in Economics and Finance, 1996.

<sup>w</sup> <sup>x</sup> 19 Y.A. Korilis, A.A. Lazar, A. Orda, Architecting noncooperative networks, Journal on Selected Areas in Communication 13 7 1995 1241–1251.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 A.A. Lazar, N. Semret, Auction for Network Resource Sharing, CTR Technical Report, CU<sup>r</sup>CTR<sup>r</sup>TR 468-97-02, Center for Telecommunications Research, Columbia University, February 1997.

<sup>w</sup> <sup>x</sup> 21 S. London, The POPCORN Tutorial, http:<sup>rr</sup>www.cs. huji.ac.il<sup>r ;</sup> popcorn<sup>r</sup>developer<sup>r</sup>tutorial<sup>r</sup>index.html.

<sup>w</sup> <sup>x</sup> 22 J.K. MacKie-Mason, H.R. Varian, Pricing congestible resources, IEEE Journal on Selected Areas in Communications 13 7 1995 1141–1149.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 J.K. MacKie-Mason, H.R. Varian, Pricing the Internet, in: B. Kahin, J. Keller Eds. , Public Access to the Internet, MITŽ . Press, 1995, pp. 269–314.

<sup>w</sup> <sup>x</sup> 24 T.W. Malone et al., Enterprise: a market-like task scheduler for distributed computing environments, in: B.A. Huberman Ž . Ed. , The Ecology of Computation, North-Holland, 1988, pp. 177–205.

<sup>w</sup> <sup>x</sup> 25 E. Maskin, J. Riley, Existence and Uniqueness of Equilibrium in Sealed High Bid Auctions, Mimeo, UCLA, March 1986.

<sup>w</sup> <sup>x</sup> 26 P. McAfee, J. McMillan, Auctions and bidding, Journal of Economic Literature 25 1987 699–738, June . Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 H. Mendelson, Market behavior in a clearing house, Econometrica 47 1982 61–74.Ž .

<sup>w</sup> <sup>x</sup> 28 F. Menezes, P. Monteiro, Sequential Asymmetric Auctions with Endogenous Participation, Economics Working Paper Archive, http:<sup>rr</sup>econwpa.wustl.edu<sup>r</sup>wpawelcome.html, ewpmic<sup>r</sup>9402001, 1994.

<sup>w</sup> <sup>x</sup> 29 P. Milgrom, Auctions and bidding: a primer, Journal of Economic Perspectives 3 3 1989 3–22, Summer .Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 P. Milgron, R. Weber, Distributional strategies for games with incomplete information, Math Operations Research 10 Ž . Ž . 1985 619–632, November .

<sup>w</sup> <sup>x</sup>31 T. Mullen, M.P. Wellman, A simple computational market for network information services, in: First International Conference on Multiagent Systems, MIT Press, San Francisco, CA, 1995.

<sup>w</sup> <sup>x</sup> 32 N. Nisan, S. London, O. Regev, N. Camiel, Globally distributed computation over the Internet — the POPCORN project, in: Proceedings for the 18th International Conference on Distributed Computing Systems,1998, Amsterdam, TheŽ Netherlands ..

<sup>w</sup> <sup>x</sup> 33 O. Regev, Economic Issues in CPU Sharing System for the Internet, Master’s Thesis, The Institute of Computer Science, The Hebrew University, Jerusalem, 1998.

<sup>w</sup> <sup>x</sup> 34 A. Rustichini, M. Satterthwaite, S. Williams, Convergence to Price-Taking Behavior in a Simple Market, D.P. 914, Center for Mathematical Studies in Economics and Management Science, 1990, December .Ž .

<sup>w</sup> <sup>x</sup> 35 D.E. Spray, The Principle Stock Exchanges of the World: Their Operation, Structure, and Development, International Economic Publishers, Washington, DC, 1964.

<sup>w</sup> <sup>x</sup> 36 The POPCORN Gallery, http:<sup>rr</sup>www.cs.huji.ac.il<sup>r ;</sup> popcorn<sup>r</sup>gallery<sup>r</sup>index.htm

<sup>w</sup> <sup>x</sup> 37 The POPCORN homepage, http:<sup>rr</sup>www.cs.huji.ac.il<sup>r ;</sup> popcorn.

<sup>w</sup> <sup>x</sup> 38 The POPCORN Market homepage, http:<sup>rr</sup>www.cs. huji.ac.il<sup>r ;</sup> popcorn<sup>r</sup>use.html.

<sup>w</sup> <sup>x</sup> 39 The POPCORN publisher homepage, http:<sup>rr</sup>www. cs.huji.ac.il<sup>r ;</sup> popcorn<sup>r</sup>publisher<sup>r</sup>index.html.

<sup>w</sup> <sup>x</sup> 40 W. Vickrey, Counterspeculation, auctions, and competitive sealed tenders, Journal of Finance 16 1961 8–37, March .Ž . Ž .

<sup>w</sup> <sup>x</sup> 41 C.A. Waldspurger et al., Spawn: a distributed computational economy, IEEE Transactions on Software Engineering 18 2Ž . Ž . Ž .1992 1, Feb .
