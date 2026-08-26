---
otero_id: 24859
otero_key: "C7W8VN2T"
title: "A Machine-Learning Approach to Automated Negotiation and Prospects for Electronic Commerce"
authors: "Jim R. Oliver"
year: "1996"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1996.11518135"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Machine-Learning Approach to Automated Negotiation and Prospects for Electronic Commerce

Jim R. Oliver

To cite this article: Jim R. Oliver (1996) A Machine-Learning Approach to Automated Negotiation and Prospects for Electronic Commerce, Journal of Management Information Systems, 13:3, 83-112, DOI: 10.1080/07421222.1996.11518135

To link to this article: http://dx.doi.org/10.1080/07421222.1996.11518135

![](/api/attachments/C7W8VN2T/fulltext/images/6be9b7d1f321c31c1d50dc26850c342d37ab833478ca021063a381a92c436bbe.jpg)

Published online: 08 Dec 2015.

![](/api/attachments/C7W8VN2T/fulltext/images/cb6245fd358b6cde2e0aad17f08422931719ee0a814bf7540020236d88158961.jpg)

Submit your article to this journal ↗

![](/api/attachments/C7W8VN2T/fulltext/images/3b2cbdb7365cbc93124705ab651b367f3cf2db454588beb7fedd2b2de6a5e5ec.jpg)

Article views: 2

![](/api/attachments/C7W8VN2T/fulltext/images/a290c3bd42db1c62dd46fa07afd1020f35f824f55ee35b63d6e2be8abc3b297d.jpg)

View related articles ↗

![](/api/attachments/C7W8VN2T/fulltext/images/aa0a9994d4735ab8205ffe5b32b4ba5622e56e87cb9983b48cf5b631a5952747.jpg)

Citing articles: 49 View citing articles ↗

# A Machine-Learning Approach to Automated Negotiation and Prospects for Electronic Commerce

JIM R. OLIVER

JIM R. OLIVER was recently a visitor at the National University of Singapore. Previously he researched, instructed, and received his Ph.D. in operations and information management at The Wharton School of Business. His research interests include automated negotiation, electronic commerce, information retrieval, and game theory. At Wharton, Dr. Oliver codeveloped a course on the business implications of the Internet and related technologies. Prior to attending Wharton, he worked in the data communications and information systems fields for Hewlett Packard and Andersen Consulting. He holds B.S. and M.S. degrees in electrical engineering from the University of Washington and Stanford University, respectively.

ABSTRACT: This paper shows how a system of artificial adaptive agents, using a genetic algorithm-based learning technique, can learn strategies that enable it to effectively participate in stylized business negotiations. The negotiation policies learned are evaluated on several dimensions including joint outcomes, nearness to the efficient frontier, and similarity to outcomes of human negotiations. The results are promising for integrating such agents into practicable electronic commerce systems. What a system might look like is discussed, as are ways in which particular classes of business negotiations could be supported or even entirely automated.

KEY WORDS AND PHRASES: electronic commerce, genetic algorithms, machine learning, negotiation support, software agents.

EVEN IN SIMPLE NEGOTIATIONS, PEOPLE OFTEN REACH SUBOPTIMAL agreements, thereby “leaving money on the table” [6, 19]. While many factors lead negotiators to miss out on gains from trade overconfidence, falsely assuming fixed pies, and the framing of the situation [2], the result is that parties fail to find mutually beneficial agreements. This well-documented fact has led researchers to develop tools to help people prepare for and participate in negotiations. This paper looks toward future electronic marketplaces and investigates not just supporting negotiators but also the possibility of fully automated business negotiations.

Acknowledgment: I wish to thank the Department of Information Systems and Computer Science at the National University of Singapore; I completed this work while visiting there.

The challenge of negotiation arises, in part, from the fact that each side has private information about their own utility function but is ignorant of the other's values and strategies. Exacerbating this situation is the negotiators' incentive to misrepresent their preferences. Finding superior agreements in this dynamic environment of mutual mistrust is extremely challenging. Given the difficulty of the search, and the failings of humans at this task, it might be nice if an information system could search the possibilities effectively for us. This paper shows how a system of autonomous agents can achieve this goal and learn effective negotiation strategies. Furthermore, the results of this study bolster the argument that these agents should be integrable into practical electronic commerce systems; not only would this leave less money on the table, but it would enable new types of transactions to be negotiated cost effectively, electronically, and automatically.

To clarify both the types of negotiations considered and the opportunities for automated systems, a simple example is presented. Although it is a narrow example, it illustrates many general issues. Consider this scenario: A manager is leaving tomorrow morning on yet another sudden business trip. She has only visited this client once before and is not very familiar with her destination. She needs to reserve a hotel room—a different one from last time, since it was not satisfactory. Generally, she prefers a hotel close to her client so that she will have time both to work out in the morning at a hotel gym and to grab a bite to eat before her meeting. Other amenities, such as room service, a pool, and laundry, are not as important. The cost of phone calls, however, is of some interest since she dials in for both voice mail and e-mail. The only unusual aspect of this trip is that she may be able to finish her business in one day and leave in the evening, rather than stay in a hotel; a hotel with a liberal cancellation policy would be worth extra to her. Clearly, an automated system that could make a satisfactory reservation for her would be useful.

Now consider the same scenario from the point of view of a prospective hotel: Suppose this hotel is close to the manager's client. Suppose further that the hotel was recently renovated, including upgraded fitness facilities and installation of some minimal food-service facilities that enable the hotel to serve an inexpensive continental breakfast. Also, the hotel is near an airport and people often arrive in the evening without a reservation, wanting a hotel nearby. Thus, if the hotel is nearly booked with advanced reservations, a few no-shows generally do not lead to lost income. Again, clearly, an automated system that would help the hotel find the guests that value its characteristics the most would be useful.

Currently, this type of routine business transaction does not involve any negotiation between the parties. There are many reasons, ranging from convention to agency issues to the costs associated with negotiating with multiple parties over multiple issues. Let's ignore the first two reasons. If negotiation were very cheap, then a dialogue between the hotel and the customer would be valuable because options could be explored, in real time, for mutual gain. The ability to create additional value is the essence of integrative bargaining (as opposed to the zero-sum distributive bargaining, such as dividing a dollar). An automated system could facilitate this value-creating dialogue and benefit all parties involved. Furthermore, these automated assistants would be even more valuable if they could learn good negotiation strategies with minimal supervision. In sum, effective automated agents could not only help with existing negotiations but possibly create new opportunities for more efficient exchange.

Although the hotel example is simple and specific, it has properties that are very general. As is usually the case, neither side knows the other's utility function: The prospective customer does not know the hotel's costs, and the hotel does not know how much the manager values each feature. While in this case, the electronic dialogue would be about hotel rooms, it should be clear that this type of dialogue generalizes to many other negotiations. That is, the promise of machine support is not a sophisticated hotel reservation system, but a general-purpose system that creates value by making better deals for each party. Such a system would be especially valuable in any situation where the product offerings are very dynamic or substantially customized.

## Research Goals

THIS STREAM OF RESEARCH IS MOTIVATED BY TWO BROAD QUESTIONS:

\- Can automated agents learn strategies that enable them to effectively participate in typical, semistructured, multi-issue, business negotiations?

• What is required and how does it work?

These general questions beg many, more specific questions. While many avenues of inquiry could be undertaken, this paper focuses on just two aspects. We create a system of artificial adaptive agents (AAAs), test them in a variety of negotiation contexts, and evaluate their performance on two dimensions: (1) the extent to which they can learn to achieve effective outcomes for the specific games, and (2) their performance compared with published human data. These investigations are an initial, but necessarily incomplete, effort at answering open-ended research questions. Based on the results, it is possible to propose a more complete system for automated negotiation in electronic commerce.

## Background and Literature Review

FOUR STREAMS OF RESEARCH INFORM THE DESIGN OF A SYSTEM of automated negotiating agents. The first involves game-theoretic models of bargaining and negotiation. Next are negotiation support systems (NSS), followed by distributed artificial intelligence (DAI), which address computer support of human agents and the design and study of distributed, computing agents respectively. The fourth stream involves evolutionary computation approaches to decision and search situations related to negotiation.

## Game Theory

The study of bargaining and negotiation has long attracted economists because it is fundamental to exchange and markets. Early foundations were laid by Nash [16, 17], and the area is still very active. Despite significant effort and progress, bargaining is incompletely understood; Linhart, Radner, and Satterthwaite $[12]$ note that “adequate theories of bargaining exist only for the degenerate, polar cases of perfect competition and monopoly” (p. 1). The following, more specific objections regarding game-theoretic models of bargaining are raised by Linhart et al. $[12]$ :

\- Common knowledge. In particular, most models assume a common prior for the valuation of the negotiated object to the buyer and seller; yet, “ordinary experience seems to indicate that what makes horse races is variation among priors” [12, p. 216].

\- Multiple equilibria. In sealed-bid bargaining under uncertainty, there is a continuum of equilibria, even if one only considers pure strategies. Even in the simple case of complete information, two prominent axiomatic solutions, the Nash and the Kalai–Smorodinsky, can predict different outcomes.

\- Single object. In most models, bargaining occurs over a single dimension, such as price, but in real negotiations, there are frequently many other issues such as quantity, quality parameters, delivery, and so forth.

These objections suggest that game-theoretic models of bargaining will be difficult to apply to natural situations. This point is also made by Raiffa [19], who notes, “I never really used the techniques of game theory—concepts and ideas, yes, but techniques, no—in my roles as negotiator.... The qualitative framework of thought was repeatedly helpful—not its detailed, esoteric, quantitative aspects. Simple back-of-the envelope analysis was all that seemed appropriate” (p. 3). Although the extent to which artificial agents can learn simple quantitative models that can be appropriately applied in new situations is not yet clear, à la back-of-the envelope, we are excited by our results in which automated agents discover rules of thumb for particular situations and which suggest that agents can appropriately modify these rules over time.

In sum, game-theoretic models have provided great insights into competitive decision making; however, they fall short of informing the specific design of computer models—in particular, machine learning models—of negotiation. In other words, game theory tells us about outcomes we can expect when rational agents bargain, whether these are artificial or not. The models do not tell, in all cases, a given agent which of many strategies to use in a given bargaining situation.

## Negotiation Support Systems

A disturbing research finding is the extent to which negotiators fail to reach the frontier of negotiation possibilities. In fact, negotiators often leave money on the table, even in relatively simple negotiations. For example, in an experiment conducted by Rangaswamy and Shell [20], only four of thirty-four dyads made a key integrative tradeoff. The experiment was a simulated international supply contract that had four negotiable issues, each of which had only four distinct options.

The challenges of negotiation and the shortcomings of human negotiators have prompted researchers to pursue computer support of negotiation, known generally as negotiation support systems (NSS). Although NSS typically emphasize support rather than automation, the implementations and computational approaches they employ are relevant to and suggestive of possibilities for artificial agents. One example of the use of computational techniques is a concession model of Matwin, Szapiro, and Haigh [14], which hard-codes a general strategy of concession in multi-issue negotiation. A very different NSS, by Rangaswamy and Shell [20], uses a computer-based method to elicit a conjoint representation of preferences. Once the parties have a better understanding of their preferences, they make proposals electronically. In controlled experiments, the supported users reach better agreements. An additional feature of the system is that it observes the offers made by each party and, by knowing the preferences of both, can suggest Pareto-improving solutions. This feature raises two issues. One has to do with incentive compatibility and possible strategic behavior. Users who are aware that a computer will make suggestions based on the utility assessment might attempt to game the system by misrepresenting their preferences. The second issue is satisfaction: Users must be comfortable with a central system knowing their preferences and observing their offers. One can imagine a secure electronic marketplace that minimizes this issue, but some users might still be hesitant.

Negotiation support systems are designed to facilitate the various phases of the bargaining process. Because negotiations are considered complex and unstructured $[5]$ , NSS functional requirements have emphasized very general support capabilities; as such, these systems are neither amenable to nor intended for full automation. The tools for support are varied; many emphasize mathematical support tools, such as decision trees, forecasting, and so forth. However, Jelassi and Foroughi $[11]$ have called for tools that address negotiators' behavioral characteristics and cognitive perspectives.

Woo and Chang [24] used speech act theory to formalize the negotiation process to make machine transmission of messages possible. Automation would result from combining this with the appropriate domain knowledge and other benefits could accrue from repetitive, similar negotiations.

Although the goals of NSS research are different from those of this research, it shares some prescriptive aims and offers important guidance and ideas for more automated negotiators, particularly in the areas of system architecture, functional requirements, and user interface.

## Distributed Artificial Intelligence

Like NSS, distributed artificial intelligence (DAI) systems provide examples of computational approaches to decision making. Bond and Gasser [3] describe the scope of DAI as considering “how the work of solving a particular problem can be divided among a number of modules . . . that cooperate at the level of dividing and sharing knowledge about the problem and about the developing solution” [3, p. 3]. The challenges are to coordinate the modules, with limited communication, in the face of possibly inconsistent knowledge. Most DAI research has assumed cooperation, or “collaborative reasoning”; conflicts have been limited to issues such as bidding for shared resources, typically computation. This nonstrategic, primarily cooperative approach, typical of most DAI research, clearly cannot be applied to all (competitive) business situations. However, recent research has begun to explore less cooperative paradigms and is more promising for strategic interaction (see, e.g., [21]).

## Evolutionary Computation

The most immediately relevant stream of research explicitly investigates machine models of competitive situations by using the techniques of evolutionary computation in systems of artificial agents. Genetic algorithms (GAs) are probably the most common evolutionary technique. These are described in more detail in the next section, but, in brief, GAs are techniques inspired by evolution—in particular the concepts of variation and natural selection. In an optimization context, a population of candidate solutions is generated and evaluated; the best solutions are assigned the highest fitness and preferentially chosen to be “parents” and combined to create new candidate solutions that comprise the next generation. These “children” are just new possible solutions, which are evaluated, and the cycle continues.

Using an evolutionary computation approach called genetic programming, Dworman, Kimbrough, and Laing [7] offer support for the idea that autonomous learning agents can discover particular and attractive equilibria in certain classes of games. Another example is that of Marimon, McGrattan, and Sargent [13], who studied a simple exchange economy in which agents must use a commodity or fiat money as a medium of exchange if trade is to occur. The artificially intelligent agents are modeled using classifier systems to make decisions. For most of the economies simulated, trading and consumption patterns converge to a stationary Nash equilibrium even if agents start with random rules. The simulations show that multiagent systems of classifiers can eventually learn to play Nash–Markov equilibria.

There are many other cases in which evolutionary algorithms (EAs) are applied to decision situations, such as the prisoners' dilemma by Ho [10], Miller [15] and Axelrod [1], sequential decisions by Oliver [18], and double auctions by Rust, Miller, and Palmer [22]. This broad stream of literature, including much else not mentioned, suggests that the goal of practical, automated negotiating agents is ambitious but attainable.

## Implementation

THE SUCCESS OF EVOLUTIONARY ALGORITHMS IN DIVERSE DOMAINS, but especially in decision and search problems [9], makes them an appropriate machine-learning approach for automated agents discovering effective negotiation strategies. In the first phase of this research, which is reported here, only genetic algorithms (GAs) were used. These are overviewed here, but an excellent introduction is Goldberg [9].

## Genetic Algorithms

In a GA, candidate solutions to the problem are encoded into “chromosomes,” which are a representation of a solution or instance of the problem at hand. While there are no hard-and-fast rules of representation, a problem is often specifically encoded into binary strings. The GA then operates on the binary (base-2) string much as genetic processes operate on our own base-4 chromosomes. While a binary coding is common, the GA does not require it.

The basic GA begins with a randomly generated population of candidate solutions. The case described here is the standard binary case; the nonbinary case is analogous. The population is the set of chromosomes, which begin as a random set of ones and zeroes. Typically, each chromosome is evaluated. For example, in the case of maximization, the chromosome is the input to the objective function, and the fitness of the chromosomes could be the value of the objective function.

A new population is created by selecting individuals to be parents for the new population. The basic selection strategy is to choose parents proportional to their fitness. Thus, an individual chromosome that has twice the fitness of another has twice the chance of being a parent for the new population. Sometimes results are improved by scaling the fitness according to a nonlinear function before the selection routine is performed.

The selected parents are used to create the next generation of the population. While, in some cases, new parents are simply preserved in the next generation, new parts of the problem space are explored by creating new chromosomes. The evolution-inspired operators of crossover and mutation are used most commonly. Single-point crossover is one particular approach; it works as follows: Assuming the sixth position is the randomly chosen crossover point, then one child is composed of the first six bits of one parent and bits after position six from the other parent. This method of crossover can be used to create two offspring from each parent. The other child gets the first six bits from the second parent and the final bits from the first.

The other primary mechanism of generating variance in the population is mutation. The following is an example of mutation: If the fifth bit of a child mutates, it changes from a zero to a one or from a one to a zero. Generally, every bit in a chromosome has a small chance of mutating. The probability of a mutation occurring for any given bit is controlled by a system parameter called the mutation rate. Thus, the number of mutations per chromosome depends on the length of the chromosome and the mutation rate.

After the new population is created, the cycle begins again. Each new chromosome is evaluated for fitness, a new population is created, and so forth. This loop is repeated until a specified stop condition is met. One that is often used is a stable average fitness. If the fitness of the population has remained rather stable for a number of generations, then continuing for more generations is not likely to yield better results. Experience with GAs and understanding the problem being solved are a significant aid to creating appropriate stopping conditions.

## Negotiation as Search

Negotiation is a search process. For example, two-player integrative bargaining can be viewed as two negotiators jointly searching a multidimensional space and then agreeing to a single point in the space. Each dimension can be discrete or real valued, although in our implementation, only discrete values are used. Each party has a multi-attribute value function over the space of possible agreement points. In the bargaining space, each dimension corresponds to an issue to be negotiated; each issue has two or more alternatives that are indexed by elements of a set. For illustration, consider a stylized business negotiation. Suppose a purchasing agent needs to obtain a particular part from a supplier quickly. The agent might be interested in the issues of price, quantity, and delivery. With regard to delivery, the buyer might have decreasing utilities for next morning, next afternoon, 2nd-day air, and (several-day) ground transport. For the price dimension, utility would be monotonically decreasing in price. The value function for the quantity dimension might be an ideal point model. In contrast to the purchaser's values, a supplier would have different, partially opposing, utilities. The space of bargaining outcomes is {price in $[0, P_{max}]$ } X {quantity in $[0, Q_{max}]$ } X {delivery from {next morning, next afternoon, 2 day, ground}} , although some points might not be feasible.

## Value Functions

In simulations reported here, simple, additive preference models are typically employed; the value for each alternative in each dimension is independent of other values. These value functions are implemented as a simple table look-up. The set corresponding to a dimension is arbitrarily indexed and a corresponding payoff set is encoded in the system. In our example, the set for the delivery dimension is {ground, 2 day, next day afternoon, next day morning} which has payoffs of, for example, {0, 7, 8, 10} to the customer and {10, 2, 1, 0} to the supplier (the maximum value of 10 is arbitrary). In general, the value, V, of a particular option $X = (x_{1}, x_{2}, \ldots, x_{n})$ is,

$$
V (X) = w _ {i} v _ {i} (x _ {i}),
$$

where $v_i$ is the value function, or the part-worth, for the alternatives for issue $i$ only, and $w_i$ is a weighting factor that may or may not be necessary depending on the scaling of the part-worths. In the previous example, the utility of the outcome (price = \$2.75, qty = 150, delivery = next morning) is $V(\$2.75, 150, \text{next morning}) = v_1(\$2.75) + v_2(150) + v_3(\text{next morning})$ .

## Strategies

A set of random, feasible, initial strategies is created. The strategies currently in use by the system are sets of simple, sequential threshold rules. The rules are meant to be intuitive, straightforward to explicate, and not too difficult to elicit. An example of the type of strategy used is the following: Consider the seller of an item, such as a car.

The strategy might be initially to accept any offer whose value is greater than a threshold $T_{1}$ . If the prospective buyer's offer does not meet that threshold, then the seller makes a counteroffer. If this counteroffer is not accepted, and the buyer comes back with a new offer, the seller compares this with another, typically different, threshold, $T_{2}$ . Again, if the threshold is not met, a counteroffer could be made. At any point, either party might choose to discontinue bargaining. This type of rule structure can be extended for an arbitrary number of rounds but, for practical purposes, the real strategies are limited in depth. The current system only uses strategies with this simple structure, but more general strategies could be used.

## Messages

Offers made by each party are communicated via messages, which are sent privately to the other party. This approach can be extended to more than two parties, to handle, for example, the cases of multiparty negotiation or sealed-bid auctions, in future work. In posted-price auctions, the messages could be broadcast or posted electronically to all participants.

## Operation

Figure 1 summarizes system operation. Each of the two artificial players is initialized with a set of random strategies, and each randomly chooses a strategy to test. Within the bargaining cycle, one player is randomly chosen to start the bargaining; this player sends an offer message. The other player's strategy evaluates the message and either accepts the offer or makes a counteroffer. This continues until agreement is reached or one of the players exhausts the strategy being tested and sends a quit message. The system continues to test strategies in this manner for a specified (a system parameter) number of times. Then the genetic algorithm is run and a new population of strategies is created. This outer loop is also continued until an exit condition is met.

The bargaining procedure just described overviews a stylized, structured form of human bargaining. To clarify the task faced by the artificial agents, the following is a concrete story of how humans would view the situation faced by the artificial agents. The scenario is a general description of a class of human bargaining experiments. Two people are each told that they will be negotiating over a set of possibilities. Each is told the specific dimensions, such as price, quantity, and delivery, and each is told of the alternatives available for each dimension, such as exact delivery options. Furthermore, each person is told privately his or her own value function over the set of possibilities. One person is selected to begin the bargaining. Offers are exchanged until there is agreement or impasse, the latter being defined by the rules of the particular bargaining game. Each person bargains to try to maximize his or her personal value from an agreement. Many permutations of this basic procedure have been performed in human experiments; the cases reported below duplicate as closely as possible the structure of the bargaining game studied.

![](/api/attachments/C7W8VN2T/fulltext/images/03f1031e2f19ba672c3f7b7132efa389141a5f0aefd271cb13559e3b58755b78.jpg)  
Figure 1. System Operation

## Comments

Earlier we looked at three limitations of typical game-theoretic models of bargaining. The bargaining games played by our artificial agents are designed with explicit awareness of these limitations. The negotiations are not over a single object but, like most business negotiations, are inherently multidimensional. All games have multiple equilibria and which is selected is specifically explored. Finally, the usual assumption of common knowledge is not required in this computational model: The artificial agents are initially devoid of any explicit knowledge about other agents and do not even explicitly know their own payoff function, which is provided by nature. This information structure is in the spirit of Young [25, p. 5], who notes: “Typically, the parties do not know each other’s utility functions with any degree of accuracy.... Usually they do not know each other’s BATNAs [best alternative to a negotiated agreement].” However, each agent does have a strategy, and the agent’s population has a distribution of strategies, which changes over time as strategies coevolve. Natural selection shapes this distribution by culling strategies that are less useful given the current distribution of opposing strategies.

## Experiments and Results

THE PERFORMANCE OF THE AAAS IS INVESTIGATED ACROSS FIVE TYPES of games. Performance is operationalized with several standard performance measures, as described below. In addition, each particular run requires specific system parameter values, also described below.

## Game Types

The first of the five game types described in the ensuing subsections is called no conflict; it has no competitive aspect but provides a useful benchmark. The next focuses on a pure distributive bargaining problem in a reduced-dimension environment. The third is a simplified integrative bargaining problem, a low-dimension, stylized business negotiation. The fourth involves a larger dimensionality example from Raiffa [19], for which human results are published; the outcomes of artificial, adaptive agents compare favorably with those of the human subjects in this stylized but fairly realistic labor negotiation. The fifth game type is a stylized international business negotiation by Rangaswamy and Shell [20].

## Performance Measures

Several statistics and measures are tracked regarding the performance of individual chromosomes (strategies), the population as a whole, and features that characterize the bargaining sessions.

The most important measures characterize the performance of individual agents and the dyads. AAAs should achieve high payoff outcomes individually. The individual payoffs are measured in terms of the agents' endowed value functions, which are known precisely; this information enables statistical tests of agent learning by comparing individual payoffs achieved after a training period with (1) agreements in the first generation that arise from agreements by the random strategies with which the agents are initially endowed, and (2) the expected payoff to each agent of a randomly selected point in the bargaining space.

Agents should not only achieve excellent individual payoffs but should achieve excellent outcomes collectively as well. As in Bottom and Studt [4] and Foroughi, Perkins, and Jelassi [8], joint payoffs were measured as the sum of the individual payoffs. The same statistical tests as above were used to compare the joint payoff with agreements in the first generation of bargaining, and the expected payoff from a random point in the feasible space.

Human negotiators often choose agreements that are below the pareto frontier. Nearness to the frontier is computed as follows: For each agreement, a list of all pareto-superior agreements on the frontier is generated, and the improvement in payoffs, for each agent, associated with these points is calculated and averaged. The averaging is both over the set of dominating points and over all the agreements in the generation. This inferiority measure has two benefits. Not only is it more encompassing than Euclidean distance to frontier alone, but keeping the measures independent for each agent means precludes interpersonal tradeoff measures.

## System Parameters

Each run of the system requires several parameters.

## Population Size

This is set to 20. These 20 chromosomes make up the strategy set for each agent. Each chromosome is a threshold decision rule that can begin and end a single bargaining session. Twenty was chosen as a small population size that consistently yielded results. Pilot tests with smaller population sizes were inconsistent in performance. Optimizing the population size is not simple and is not the goal of this work.

## Number of Sessions

This is set to 20. Each generation consists of 20 bargaining games. Because there are 20 chromosomes per agent, each chromosome will participate, on average, in one bargaining game per generation. The strategies for testing are selected randomly (uniformly), with replacement, so typically, in each generation, some strategies are tested more than once and others not at all. The random selection was used to insure that no cycles are created in which, for example, strategy one of agent one always plays the same strategy of agent two.

## Number of Generations

This is set to 20. Each run consists of 20 generations. This was adequate time for the agents to learn reasonable strategies.

## Crossover Rate

This is set to 0.5, which favors neither parent in crossover. Each part of a child's chromosome is equally likely to come from either parent.

## Mutation Rate

This is set to 0.05, which implies that, on average, one in twenty elements of the offspring will be different from both parents. Mutation occurs on individual threshold values and on individual components of the offer vectors. This mutation rate is perhaps a little higher than some GA applications but it is not unusual. Like population size, this parameter was chosen because of published GA applications and brief pilot studies; optimizing this system parameter is left to later research.

## Number of Offers

This is set to 3 for the experiments reported here. The value of 3 allows each side to make up to 3 offers before the game is terminated, assuming neither side has agreed. This parameter, like other individual parameters, could be asymmetric between agents, but this possibility is not explored in this research.

## Experiment 1: System Verification

For simply verifying the operation of the system, the artificial agents are endowed with the same value functions. Consequently, the agents should converge to the unique, joint maximum—that is, the unique pareto optimum. The absence of conflicting interests makes this test essentially two, interrelated, discrete optimizations—the difficulties of competitive coevolution are deliberately removed.

## Agent Value Functions

Figure 2 shows the value functions for the agents for six alternatives, one through six, for each of two issues, A and B. Both parties are happiest with the option (A = 6, B = 1).

## Results

Figure 3 shows the results for a single population pair (each with 20 chromosomes, or strategies), initially endowed with random strategies, after 20 generations. The smallest dots, on the line, are the possible agreement points, and the slightly larger dots are noisy plots of the actual agreements. The noise is intentionally added to show multiple agreements clearly at the same point. The pareto optimum is in the upper right corner. In this run, all but one of the agreements are the maximum possible; the one exception is in the center of the graph. This poor agreement could have resulted from a mutated strategy.

Figure 4 shows another run in which the average payoff is actually similar to that in figure 3, but the population converged early, prior to reaching the maximum. Most of the agreements are just below the maximum in the upper right-hand corner. Early convergence is a general problem of GA-based approaches. While there is no absolute solution, there are strategies that help to minimize it [9], but these are not the focus of this investigation.

![](/api/attachments/C7W8VN2T/fulltext/images/bb5ecb0e23bc5d4915575c5324ff3406ed3c8dd4df6e2aa8832b0c241337b9a0.jpg)  
Figure 2. Value (Y Axis) for Each Agent for Two Issues: Each Issue Has Six Alternatives (X Axis)

![](/api/attachments/C7W8VN2T/fulltext/images/88b4f32fa25c0cf884c654e515b5d82894ed2197d00a04dab28ec1fcd5a63cb2.jpg)  
Figure 3. No-Conflict Game

![](/api/attachments/C7W8VN2T/fulltext/images/33c5c0995da9f1974389741133fdab6aac5a31c9b3196f5129b374f2a19c48bf.jpg)  
Figure 4. No-Conflict Game

Figures 3 and 4 show bargaining agents agreeing to points that are much better than if they were just agreeing to random points in the bargaining space. To test more formally whether the agents are learning, several statistical tests were used.

\- Individual learning: A one-sided $t$ -test compared the payoff to each agent in the first five generations with those of the last five generations, assuming a pooled variance. These are averaged over ten runs.

\- Individual comparison with a random point: A one-sided $t$ -test was performed on the hypothesis that the last generation payoffs are greater than the expected value of a random point in the bargaining space.

\- Dyad learning: A one-sided $t$ -test was performed for the hypothesis that the dyad learns from the first five to the last five generations, as measured by the joint payoff.

\- Dyad comparison with a random point: A one-sided $t$ -test was performed to test the hypothesis that the joint payoffs for the dyad in the last generation are greater than the expected value of a random point in the bargaining space.

\- Nearness to the frontier: A one-sided $t$ -test compared the nearness to the frontier for each agent in the first five generations with the nearness in the last five generations, assuming a pooled variance.

Table 1 summarizes the results of the t-tests. The agents exhibit significant learning behavior; all of the hypotheses were strongly supported.

Table 1. Results of Statistical Tests for the No Conflict Game

<table><tr><td>Test</td><td>Test statistic</td><td>Degree of freedom</td><td>p value</td></tr><tr><td>Individual learning (agent 1)</td><td>6.9</td><td>8</td><td> $6.5 \times 10^{-5}$ </td></tr><tr><td>Individual learning (agent 2)</td><td>6.9</td><td>8</td><td> $6.5 \times 10^{-5}$ </td></tr><tr><td>Individual payoff better than random (agent 1, expected random payoff = 0.5)</td><td>13.8</td><td>9</td><td> $1.1 \times 10^{-7}$ </td></tr><tr><td>Individual payoff better than random (agent 2, expected random payoff = 0.5)</td><td>13.8</td><td>9</td><td> $1.1 \times 10^{-7}$ </td></tr><tr><td>Dyad learning</td><td>6.9</td><td>8</td><td> $6.5 \times 10^{-5}$ </td></tr><tr><td>Dyad payoff better than random (expected joint payoff of random agreement = 1.0)</td><td>7.2</td><td>18</td><td> $1.1 \times 10^{-7}$ </td></tr><tr><td>Nearness to frontier (agent 1)</td><td>6.8</td><td>8</td><td> $6.3 \times 10^{-5}$ </td></tr><tr><td>Nearness to frontier (agent 2)</td><td>6.8</td><td>8</td><td> $6.3 \times 10^{-5}$ </td></tr></table>

## Experiment 2: Pure Distributive Bargaining

## Agent Value Functions

Figure 5 and 6 show the value functions for the agents for six alternatives, one through six, for each of two issues, A and B. Player 1 prefers (1,1)—that is, alternative one on both issues A and B, while player 2 wants (6,6). Like games in later sections, this game has multiple Nash equilibria; however, unlike most of the games reported later, there is no prominent equilibrium—the frontier is flat, as shown in figure 7. While cooperative game theory deals explicitly with such situations, classical noncooperative game theory does not predict which equilibrium will be selected.

## Results

Figure 8 shows the results for a single run. In this case, as in other runs of the same game, there is some clumping of the agreements due to the convergence of the population of strategies. The particular location of convergence tended to vary and we defer further investigation of pure distributive bargaining to future research; the focus in this paper is on integrative bargaining because of the opportunity for mutual gain and the relevance to typical commercial-exchange situations.

No statistical results are given because the nature of the game makes all measures meaningless: All agreements are always on the frontier and all joint values are the same. The only test of interest would be individual tests to see if either agent is consistently outperforming the other. Such a result would suggest an error in the system as our agents are symmetrical. No significant differences were found.

![](/api/attachments/C7W8VN2T/fulltext/images/d71d025d35537107ffd240eebc949fe585730bb7e079f70338551ff0037a56e5.jpg)  
Figure 5. Values for Six Issue A Options

![](/api/attachments/C7W8VN2T/fulltext/images/6402b621ff154e1d291a7452a5aa64b577c6aa87e539c89b0992d127b69f1394.jpg)  
Figure 6. Values for Six Issue B Options

## Experiment 3: Simple Integrative Bargaining

This game is a stylized business negotiation that captures a simplified purchasing situation in which the agents bargain over price, quantity, and delivery. The agents have opposing value functions within each issue, but the importance across issues varies such that, rather than compromising on each issue, each player should give up everything on the issue of least importance and get the maximum on the issue of greater importance.

## Agent Value Functions

Table 2 shows the value functions for the agents. For agent 1, the most important issue is price whereas, for agent 2, the most important issue is quantity. The expected joint payoff, the sum of both agents' payoffs, from a random point in the bargaining space is 0.98. The joint maximum is 1.36.

![](/api/attachments/C7W8VN2T/fulltext/images/9f54906a9bb67d8bdeedf7947dac05c8ee92b022d2c3f5fb30ba7d8901be726b.jpg)  
Figure 7. Feasible Payoffs Graph

![](/api/attachments/C7W8VN2T/fulltext/images/1b131974f1c3812e63c75bcf19349f7433b40f4728a13bb7517bfa02f1c04580.jpg)  
Figure 8. Population after 20 Generations

Table 2. Value over Three Issues, Price, Quality, and Delivery, for Two Players

<table><tr><td rowspan="2">Issues</td><td rowspan="2">Alternatives</td><td colspan="2">Values</td></tr><tr><td>Agent 1</td><td>Agent 2</td></tr><tr><td rowspan="5">Price</td><td rowspan="4">Low</td><td>0</td><td>0.25</td></tr><tr><td>0.11</td><td>0.19</td></tr><tr><td>0.22</td><td>0.12</td></tr><tr><td>0.33</td><td>0.06</td></tr><tr><td>High</td><td>0.44</td><td>0</td></tr><tr><td rowspan="5">Quantity</td><td rowspan="4">Few</td><td>0.22</td><td>0</td></tr><tr><td>0.17</td><td>0.12</td></tr><tr><td>0.11</td><td>0.25</td></tr><tr><td>0.06</td><td>0.38</td></tr><tr><td>Many</td><td>0</td><td>0.56</td></tr><tr><td rowspan="4">Delivery</td><td>Next morning</td><td>0.33</td><td>0</td></tr><tr><td>Next afternoon</td><td>0.22</td><td>0.06</td></tr><tr><td>2nd day</td><td>0.11</td><td>0.12</td></tr><tr><td>7–10 days</td><td>0</td><td>0.19</td></tr></table>

## Results

An example of the agreements and the entire bargaining space is shown in figure 9. The large dots are the agreement points for the final generation of one run of bargaining; the smaller dots are all the possible agreements. The larger dots have noise added intentionally to clarify the number of agreements at a discrete point; all agreements are at discrete locations. In the figure, the average payoff to agent 1 is 0.66 and to agent 2 is 0.53, for a joint payoff of 1.18.

The same statistical tests, shown in Table 3, are applied to the agents as in the first game. The agents have no problem learning in this simplified business negotiation context.

The GA methodology facilitates a detailed analysis of the evolution of high-performing strategies. Figure 10 shows that agents learn not to accept an offer too soon because they might come across a better offer later. The strategy cannot wait too long, since the bargaining will be cut off. The top of figure 10 shows the population starts out by accepting many initial offers; however, in the last five generations (out of twenty), many agents do not accept until the middle of the bargaining session.

## Experiment 4: City versus AMPO

The negotiation games reported so far have been contrived and stylized, both for simplicity and to expose the operation of the automated agents in a basic but crisp manner. Real negotiations, even simple ones, are more complicated than those described so far. One important factor is complexity, especially in terms of dimensionality; high dimensionality creates a challenging negotiation environment and human subjects are more likely to accept inferior offers.

![](/api/attachments/C7W8VN2T/fulltext/images/1f21bf014ce7da93d601517beb8a430528eba3a2db510a0881862b3f9ec54edc.jpg)  
Figure 9. Results for One Run of the Integrative Game

Table 3. Statistical Test Results for Integrative Game

<table><tr><td>Test</td><td>Test statistic</td><td>Degree of freedom</td><td>p value</td></tr><tr><td>Individual learning (agent 1)</td><td>4.8</td><td>8</td><td>0.00066</td></tr><tr><td>Individual learning (agent 2)</td><td>6.1</td><td>8</td><td>0.00014</td></tr><tr><td>Individual comparison with a random point (agent 1, expected random payoff = 0.51)</td><td>2.3</td><td>9</td><td>0.023</td></tr><tr><td>Individual comparison with a random point (agent 2, expected random payoff = 0.47)</td><td>2.7</td><td>9</td><td>0.012</td></tr><tr><td>Dyad learning</td><td>27</td><td>8</td><td> $1.8 \times 10^{-9}$ </td></tr><tr><td>Dyad comparison with a random point (expected joint payoff from random agreement = 0.98)</td><td>5.5</td><td>9</td><td>0.00019</td></tr><tr><td>Nearness to frontier (agent 1)</td><td>21</td><td>8</td><td> $1.2 \times 10^{-8}$ </td></tr><tr><td>Nearness to frontier (agent 2)</td><td>17</td><td>8</td><td> $6.4 \times 10^{-8}$ </td></tr></table>

![](/api/attachments/C7W8VN2T/fulltext/images/ff055ed20e4cdd4b8065e83a86c1699868a02279ec83c945c34b6eb71303de85.jpg)

![](/api/attachments/C7W8VN2T/fulltext/images/2270553a04a775378dbede26ca9d36a0fbd3ccfcc5347653ddd36cc3cef74d8e.jpg)  
Figure 10. Acceptance Offers Early in the Run (top) and Late in the Run (bottom)

## Agent Value Functions

This section recreates an experimental game reported in $[19]$ . It is a stylized labor negotiation between a city and a police union, called AMPO. The size of the bargaining space, as implemented, is 13,219,200 possible points of agreement. There are eleven dimensions, each with anywhere from two to about a dozen alternatives. The original problem had one dimension that had a (nearly) continuous interval—the payoff was linear over a salary increase range of 500 to 750 dollars. Given that fractional amounts were unlikely, this effectively made the dimension discrete, but we more coarsely quantized the entire dimension into twelve points. As in other games, we scale the payoffs to the range of 0 to 1.

## Results

The result of one run is shown in figure 11. A visual comparison of the agreements reached by human agents versus agreements reached by the artificial agents shows no performance differences. Both the humans and the AAAs occasionally reach agreements very close to the frontier, but typically both were a similar distance away, $^{1}$ although the humans varied more than the AAAs. The results of a longer series of ten runs suggest that neither group outperforms the other, but there were some differences.

![](/api/attachments/C7W8VN2T/fulltext/images/8c8e030bcc26add9d78b60258f50e5e5d992ee239705fbc4516dc71cb4e25889.jpg)  
Figure 11. Human Agreements and AAA Agreements for One Run; Neither Outperforms the Other

The humans representing the city, on average, achieved higher average payoffs for themselves than did the AAAs: 0.70 versus 0.65. A t-test of the average AAA payoffs with the mean payoff for the humans representing the city had a p value of 0.06. Opposite results held for the agents representing AMPO. In this case, the AAAs outperformed the humans, earning mean payoffs of 0.58 versus 0.53. This difference was mildly significant (p = 0.04). Although these performance differences are interesting and deserve further investigation, a more important comparison is the joint payoff; on average, the joint payoff was the same for the human agents and the AAAs: 1.23. Thus, neither group outperformed the other.

## Experiment 5: Stylized International Business Negotiation

Rangaswamy and Shell [20] report on a four-dimensional, stylized international business negotiation. The game only has 256 discrete possible points of agreement, but unaided humans were not effective at making integrative tradeoffs: only four out of thirty-four pairs did so in a series of experiments. Using an NSS of their design, the human subjects in the assisted case performed significantly better, but even in this case fewer than 50 percent achieved the main integrative solution [20]. In this game, only ordinal preferences are induced in the laboratory. This is recreated for the AAAs by having the agents play against multiple instances of value functions that fit the ordinal preferences.

## Agent Value Functions

The experiment is a simulated international business negotiation between a U.S. health-care company and an east European medical equipment supplier. There are four issues to be negotiated: price, delivery, the currency of payment, and the location to adjudicate disputes. The options for each issue are:

<table><tr><td>Price:</td><td>180</td><td>195</td><td>210</td><td>225K$</td></tr><tr><td>Delivery</td><td>6</td><td>8</td><td>12</td><td>14 months</td></tr><tr><td>Currency:</td><td>US$</td><td>Euro$</td><td>Other hard</td><td>Hungarian</td></tr><tr><td>Dispute:</td><td>U.S.</td><td>London</td><td>ICC</td><td>Hungary</td></tr></table>

A key element of the preference structures in this game is the built-in integrative tradeoff of Hungarian currency and fourteen-month delivery. This tradeoff is the one that humans have difficulty finding, but it is the most valuable.

## Results

The human results reported by Rangaswamy and Shell [20] are measures of the frequency at which key integrative tradeoffs are made. Table 4 shows the frequency of key integrative tradeoffs, in the international game, for humans and AAAs. Remember, the primary integrative tradeoff is Hungarian currency and fourteen-month delivery. A twelve-month delivery is the second most preferred alternative, on the most important issue, for the supplier. Similarly, European currency is the second most preferred alternative, on the most important issue, for the customer. While the Hungarian–fourteen-month combination is the most integrative, the others are also beneficial; those shown in Table 4 are the ones reported by Rangaswamy and Shell [20]. The AAAs' results are summed for five types of customers. The results are that the AAAs learn to achieve outcomes that lie between the unaided and the aided humans. In general, while the AAAs frequently found the best integrative tradeoff, they settled on many more “other” agreements, as opposed to the two nearly as good tradeoffs, when compared with the human case. Presumably, this result is due, in part, to the simplicity of the GA implemented for this system. Manipulation of population size, different crossover strategies, diversity management, and other techniques could probably improve performance at least slightly, and possibly substantially.

## Relevance and Discussion

While these results are preliminary, the initial investigations strongly suggest that artificial agents can learn effective strategies for specific negotiation games. As argued before, given the difficulties humans have at low-dimensionality negotiation games, it is not obvious that cognitively simple artificial agents would be successful at such a task. The incomplete information environment that is challenging for humans is, of course, similarly challenging for artificial agents. The agents are further hindered by the fact that the genetic learning approach operates in a dynamic, coevolutionary environment, rather than in the static world of a traditional optimization. $^{2}$ The ability of such simple agents to learn the same games that humans find challenging is promising on many fronts, but especially for electronic commerce.

Table 4. Frequency of Integrative Tradeoffs Made in the International Business Negotiation

<table><tr><td rowspan="2"></td><td colspan="2">Human</td><td>Artificial adaptive agents</td></tr><tr><td>Face-to-face (unaided)</td><td>Using negotiation analyst</td><td>Total for 5 customer types</td></tr><tr><td>Hung.—14 months</td><td>4</td><td>15</td><td>358</td></tr><tr><td>Hung.—12 months</td><td>9</td><td>3</td><td>63</td></tr><tr><td>Euro.—12 months</td><td>15</td><td>6</td><td>22</td></tr><tr><td>Other</td><td>6</td><td>8</td><td>464</td></tr><tr><td>No Agreement</td><td>0</td><td>2</td><td>93</td></tr><tr><td>Total</td><td>34</td><td>34</td><td>1,000</td></tr></table>

The performance of artificial agents compares quite favorably with that of human subjects. The performance of AAAs certainly does not dominate the human case; rather, AAAs sometimes performed better and sometimes performed worse when measured in terms of ex-post efficiency and ability to make integrative tradeoffs. The circumstances in which one outperforms the other is an important area of future research, but the current successes of the AAAs are encouraging, exciting, and promising.

## Architecture of a System for Electronic Commerce

THE RESULTS PRESENTED HERE ARE PROMISING, BUT NEITHER THE SYSTEMS of AAAs developed nor the studies undertaken are the same as fielding a practical system. However, the results of the preceding section inform the design of a more complete system. This section briefly considers what it would take to implement this ability, how it might work, and what would have to be learned first.

## System Outline

A working system for electronic commerce needs to take into account user, marketplace, and functionality issues that have, until now, been ignored. Figure 12 outlines a possible system architecture, and each element of the system is discussed in turn.

## User Interface

The user interface is the point of interaction with the following system functions:

1. Eliciting preferences from user;

2. Eliciting, browsing, and manipulating strategies;

![](/api/attachments/C7W8VN2T/fulltext/images/181402cca265a4471948a51b3db899e804739e65cf59aac60216d7c7c9721d43.jpg)  
Figure 12. Architecture for Automated Negotiation System

3. Updating the database of products and services, their negotiable issues, and so forth;

4. Reporting.

The first three points are described below. The fourth, the reporting function, is primarily intended to inform a manager or principal about how agents are performing. The average length of negotiations, changes over time, and profitability of the agents are just three aspects of bargaining behavior that might be valuable for management.

## Preferences

Until now, the precise objects of negotiation have been abstract and stylized. But a practical system needs to buy and sell real products and services. This means that the system must know about the specific attributes of the products of interest, which is information that can be stored in a local or a remote database.

The utility functions for these products need to be elicited; these functions will most likely be stored locally—this is the type of information people want to be able to keep private. Many researchers, as well as commercial concerns, have developed viable computer-based approaches to utility function elicitation. Rangaswamy and Shell [20] report on one such elicitation procedure.

If new products, or new features for an existing product, become available, both the new attribute data and the user's value over that attribute need to be incorporated into the system. The PC industry offers two examples: First, manufacturers have recently started to bundle modems into new PCs; the consumer no longer needs to purchase these separately. If the consumer's DSS already knows about both PCs and modems, relatively minor changes are required; the bargaining space must be modified to include this new possibility. A second, more complicated case is processor speed. The introduction of, say, 200 MHz Pentium chips presents an alternative on the processor dimension on which the user will not have placed a value if the option did not exist when values were elicited.

## Strategies

The bargaining strategies and their modification are the centerpiece of a system of negotiating agents. This research has used simple threshold rules. A practical system needs the flexibility to support different types of strategies. Which additional types of strategies should be used or allowed by the AAAs is an important open question.

In the system created for the experiments reported above, the initial populations of rules were generated randomly. A practical system, depending on the environment in which the agents are to exist, might call for an alternative to random initialization. Humans rarely approach a novel situation de novo, and there is no reason for AAAs to do so either. Strategies could come from other agents or from humans. In the latter case, we might elicit strategies directly, or a system could watch the user and infer a strategy based on observed negotiations.

1. Random initialization: If there is an effective learning algorithm, and an appropriate venue for learning, then random starting strategies might be the most cost-effective.

2. Obtain strategies from other AAAs: Strategies of AAAs in similar situations should make a good starting point. This approach requires a way for the system, or the user, to determine which agent strategies would be appropriate for a novel situation.

3. Direct strategy elicitation: The simple threshold rules used in this work have a natural appeal because they resemble how human agents are sometimes told to negotiate for principals. For example, a human agent might be told, "Don't settle for less than $X$ ," or "Try to get $Y$ , but it's okay if you can only get $Z$ ." These types of strategies should be fairly easily elicited from a user.

Eliciting other types of strategies could require a new representation scheme; this warrants further investigation.

4. Bootstrapping: This might also be called passively seeding the system, or apprenticeship mode. A useful, but possibly difficult, undertaking would be to design an algorithm that observes actual negotiations and infers which strategies are being used by one side, or even both sides. If both sides are estimated, simulations could be run to predict the results of alternative strategies. If an effective learning algorithm is available, then even a quick and dirty bootstrap model could be useful as a starting point.

How the initial strategies are arrived at will determine whether additional modifications are needed prior to fielding agents in the marketplace. Three possibilities are as follows:

1. No learning: If the initial strategies are believed to be of a high enough quality—perhaps they were elicited from an experienced negotiator—then modifications to the initial rule set might not be required.

2. Off-line learning with simulated opponent: If a credible model of the opponent can be built, then a simulation approach can be taken to learn strategies that will be effective. An extension to a static opponent model would be to posit an adaptive procedure for the opponent. (See [23] for an overview of this line of research.)

3. Off-line learning in a practice forum: Another possibility is to conduct practice games—with other market participants and not models of them—and have agents learn in such a forgiving environment. The problem with this approach is that, if the negotiations are nonbinding, there is more incentive to misrepresent preferences, since principals might not want to reveal information or they might wish to establish a particular reputation. Anonymous practice sessions would remove any reputation-building motive, but such a scenario is still not the same as real, live, binding negotiations. $^{3}$

Finally, when the user has confidence in the strategies available for use by the system, she or he will “field” the agents to the marketplace. The user must decide whether and how these strategies continue to be modified, based on the negotiation experiences. Again, there are three possibilities:

1. Fixed strategies: One approach is to field static agents. Recall that the simple GA approach to learning occasionally created new strategies that agreed to low-value points in the bargaining space. While the effectiveness of the GA could undoubtedly be improved, users still might wish the agents to remain static, especially if the performance of the agents is stable. This is the “if-it-ain’t-broken-don’t-fix-it” philosophy. Static agents might also be justified in marketplaces that are relatively static or in cases where the downside of a poor strategy is great. Many financial transactions have a significant downside, and current automated financial trading systems are carefully controlled; significant strategy changes in most of these systems are programmed from outside the system, rather than have the system select radically new strategies on its own.

2. GA suggests: A GA or other learning algorithm might suggest new strategies but be prevented from acting on them without human approval.

3. GA modifies: In the most automated system, a GA—or any other learning algorithm—discovers and tries new strategies. The inconsistent performance of the GA approach might restrict this to less important transactions, or to games that have a smaller downside.

## Control and Communication

All of the system activities must be coordinated; this is the job of the control module. This module could also handle exceptions. For example, a supplier sends a customer a message about a product and the message includes an attribute that is not in the product database of the receiving system, or for which value function information has not been elicited.

The final module of the system is the communications module; its job is to interface to the electronic marketplace.

## Comment

The above list focuses on local systems and neglects services and features that are likely to be the domain of a centralized system, or will be distributed throughout the system. Security features, such as authentication and certification, secure payment mechanisms, and measures to protect systems from unauthorized intrusion are all needed. These security features are needed in any electronic commerce networks and are not unique to the case of negotiating agents. Significant academic and commercial efforts are currently directed toward these problems.

## Conclusions

AAAS, USING SIMPLE SATISFICING RULES, CAN, FROM A RANDOM START, learn to play negotiation games under the “direction” of a basic GA. While refinements to the GA such as improved crossover and better diversity management would likely improve effectiveness, the performance of these basic agents stands on its own merits. Systematic, statistical comparison with humans shows the ability for AAAs to perform similarly to humans and even to exceed their performance. That this level of success would be achieved was not obvious a priori; the results hint at exciting possibilities for electronic commerce.

The success of the AAAs illustrates the power of the adaptive approach. Such simple agents might not be expected to exhibit such complex behavior and to perform so well. For example, one might wonder how agents know the unknown about the other agent? In fact, the agents do not have explicit models of the other agents, yet they have strategies that are adapted to their environment, which is created by the other agents.

This research reinforces the idea that computational science in general, and evolutionary algorithms in particular, provide a rich tool for the study of bargaining and negotiation. The set of programs developed for this research allows us to put negotiation dynamics under a microscope. GAs were chosen as a robust and general learning mechanism, and the success of the simple GA in a difficult, dynamic, coevolutionary environment is encouraging. In well-defined situations, like many optimization contexts, it is possible to find a better-performing, specialized algorithm. Similarly, specialized negotiation learning algorithms might be developed; insights from this and related work should inform such efforts as the field matures.

## NOTES

1. Two features of figure 11 deserve mention: First, the scales do not cover the entire payoff range of zero to one, which highlights differences in agreements. Second, only some of the frontier points are shown, for clarity.

2. There is an important distinction between this game environment and the application of GAs to optimization. In optimization, there are no external dynamics for the GA—that is, typically, the environment does not change. Thus, a given chromosome always has the same raw fitness (algorithms to adjust the raw fitness based on population characteristics might be used to encourage population diversity). The competitive environment of coevolution is fundamentally different and more difficult.

3. "Cheap talk" is the game-theory term for low-cost, nonbinding, nonverifiable communication, which has been an active research area. See, for example, [25] for an example of how cheap talk can achieve partial coordination among market participants.

## REFERENCES

1. Axelrod, R. The evolution of strategies in the iterated prisoner's dilemma. In L. Davis (ed.), Genetic Algorithms and Simulated Annealing. Los Altos, CA: Morgan Kaufmann, 1987, pp. 32–41.

2. Bazerman, M.H., and Neale, M.A. Negotiator rationality and negotiator cognition: the interactive roles of prescriptive and descriptive research. In P.H. Young (ed.), Negotiation Analysis. Ann Arbor: University of Michigan Press, 1992, pp. 109–129.

3. Bond, A.H. and Gasser, L. Readings in Distributed Artificial Intelligence. San Mateo, CA: Morgan Kaufmann, 1988.

4. Bottom, W.P., and Studt, A. Framing effects and the distributive aspect of integrative bargaining. Organizational Behavior and Human Decision Processes, 56 (1993), 459–474.

5. Bui, T. Building DSS for negotiators: a three-step design process. In J.F. Nunamaker, Jr., and R.H. Sprague, Jr. (eds.), Twenty-Fifth Annual Hawaii International Conference on System Science, vol. 4. Kauai, HI: IEEE Computer Society Press, 1992, pp. 164–173.

6. Camerer, C. Behavioral game theory. In R.M. Hogarth (ed.), Insights in Decision Making: A Tribute to Hillel J. Einhorn. Chicago: University of Chicago Press, 1990, pp. 311–336.

7. Dworman, G.O.; Kimbrough, S.O.; and Laing, J.D. On automated discovery of models using genetic programming in game-theoretic contexts. In J.F. Nunamaker, Jr., and R.H. Sprague, Jr. (eds.), Twenty-Eighth Annual Hawaii International Conference on System Science. Maui, HI: IEEE Computer Society Press, 1995.

8. Foroughi, A.; Perkins, W.C.; Jelassi, M.T. An empirical study of an interactive, session-oriented computerized negotiation support system (NSS). Group Decision and Negotiation, 4 (1995), 485–512.

9. Goldberg, D.E. Genetic Algorithms in Search, Optimization, and Machine Learning. Reading, MA: Addison-Wesley, 1989.

10. Ho, T.H. Finite automata play repeated prisoner's dilemma with information processing costs. Journal of Economic Dynamics and Control, 20, 1–3 (January–March 1996), 173–207.

11. Jelassi, M.T., and Foroughi, A. Negotiation support systems: an overview of design issues and existing software. Decision Support Systems, 5, 2 (1989), 167–181.

12. Linhart, P.B.; Radner, R.; and Satterthwaite, M.A. Bargaining with Incomplete Information. San Diego: Academic Press, 1992.

13. Marimon, R.; McGrattan, E.; and Sargent, T.J. Money as a medium of exchange in an economy with artificially intelligent agents. Journal of Economics, Dynamics and Control, 14, 2 (May 1990), 329–373.

14. Matwin, S.; Szapiro, T.; and Haigh, K. Genetic algorithms approach to a negotiation support system. IEEE Transactions on Systems, Man, and Cybernetics, 21, 1 (January/February 1991), 102–114.

15. Miller, J.H. The coevolution of automata in the repeated prisoner's dilemma. Journal of Economic Behavior and Organization, 29, 1 (Jan 1996), 87–112.

16. Nash, J.R. The bargaining problem. Econometrica, 18 (1950), 155–162.

17. Nash, J.R. Two person cooperative games. Econometrica, 21 (1953), 128–140.

18. Oliver, J.R. Finding decision rules with genetic algorithms. AI Expert, 9, 3 (1994), 32–39.

19. Raiffa, H. The Art and Science of Negotiation. Cambridge, MA: Harvard University Press, 1982.

20. Rangaswamy, A., and Shell, R. Using computers to realize joint gains in negotiations: toward and electronic bargaining table. Working Paper, Legal Studies, The Wharton School, University of Pennsylvania, 1995.

21. Rosenchein, J.S., and Zlotkin, G. Designing conventions for automated negotiations. AI Magazine (Fall 1994), 29–46.

22. Rust, J.; Miller, J.H.; and Palmer, R. Behavior of trading automata in a computerized double auction market. In D. Friedman and J. Rust (eds.), The Double Auction Market. Reading, MA: Addison-Wesley, 1992, pp. 155–198.

23. Sebenius, J.K. Negotiation analysis: a characterization and review. Management Science, 38, 1 (January 1992), 18–38.

24. Woo, C.C., and Chang, M.K. An approach to facilitate the automation of semistructured and recurring negotiations in organizations. Journal of Organizational Computing, 2, 1 (1990), 47–76.

25. Young, P., ed. Negotiation Analysis. Ann Arbor: University of Michigan Press, 1991.
