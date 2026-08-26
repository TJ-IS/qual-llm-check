---
otero_id: 20965
otero_key: "F75BMBVJ"
title: "The Iterated Prisoner's Dilemma: early experiences with Learning Classifier System-based simple agents"
authors: "Chen-Lu Meng; Ramakrishnan Pakath"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00137-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Iterated Prisoner’s Dilemma: early experiences with Learning Classifier System-based simple agents

Chen-Lu Meng <sup>1</sup>, Ramakrishnan Pakath<sup>)</sup>

DSIS, School of Management, C.M. Gatton College of Business and Economics, UniÕersity of Kentucky, Lexington, KY 40506-0034, USA Accepted 15 November 2000

## Abstract

Prior research on artificial agents<sup>r</sup>agencies involves entities using specifically tailored operational strategies e.g., forŽ information retrieval, purchase negotiation . In some situations, however, an agent must interact with others whose strategies. are initially unknown and whose interests may counter its own. In such circumstances, pre-defining effective counter-strategies could become difficult or impractical. One solution, which may be viable in certain contexts, is to create agents that self-evolve increasingly effective strategies from rudimentary beginnings, during actual deployment. Using the Iterated Prisoner’s Dilemma IPD problem as a generic agent-interaction setting, we use the Learning Classifier System LCSŽ . Ž . paradigm to construct autonomously adapting AsimpleB agents. A simple agent attempts to cope by maintaining an evolving but potentially perennially incomplete and imperfect knowledge base. These agents operate against specifically tailored Ž . non-adaptive agents. We present a preliminary suite of simulation experiments and results. The promise evidenced leads us to articulate several additional areas of interesting investigations that we are pursuing. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Artificial agents; Adaptive systems; Learning Classifier Systems; Iterated Prisoner’s Dilemma

## 1. Introduction

For hundreds of years, games of strategy like chess and checkers have fascinated the human mind. In such games, two players take on the roles of opponents. Only one can emerge a winner. In a single game, the focus of each player is on vanquishing the opponent. There are other kinds of games of strategy. Some of these involve more complex payoff structures, involve more than two players, and are played in tournament fashion i.e., involve a Ž series of two or more games , where a win in every . game is not crucial to winning the tournament. An example of such a variant is the Iterated Prisoner’s Dilemma 1,12,13 .<sup>w</sup> <sup>x</sup>

In the classic version of Prisoner’s Dilemma, two players have the choice of either cooperating CŽ . with, or defecting D against, one another. The Ž . payoff obtained by each depends on what action CŽ or D each takes. If both cooperate, each receives a . reward of $R _ { 2 }$ . If both defect, each receives a relatively smaller reward of $R _ { 3 } .$ . If one defects while the other cooperates, the cooperating player gets a sucker’s payoff of $R _ { 4 }$ while the defector gets the highest possible payoff for the game, $R _ { 1 } .$ . The payoffs have the following properties:

$$
R _ {1} > R _ {2} > R _ {3} > R _ {4}
$$

$$
\left(R _ {1} + R _ {4}\right) / 2 <   R _ {2}.
$$

The first expression states that if both defect, each does worse than if both cooperated i.e., Ž $R _ { 2 } > R _ { 3 } )$ Thus, mutual cooperation is preferred to mutual defection. An individual player is nonetheless tempted to defect for two reasons. First, if the opponent were to cooperate, and thus be suckered, his<sup>r</sup>her payoff would be greater than with mutual cooperation i.e.,Ž $R _ { 1 } > R _ { 2 } )$ . Secondly, even if the opponent defects, the payoff with mutual defection, $R _ { 3 } ,$ , is better than that if he<sup>r</sup>she were to be suckered i.e.,Ž $R _ { 3 } > R _ { 4 } )$ The second expression stipulates that the payoff obtained through unsynchronized alterations of cooperation and defection with a given opponent should not be, on average, better than that obtained through repeated cooperation.

While mutual cooperation could yield a relatively higher payoff of $R _ { 2 }$ , two rational players would tend to both defect resulting in each earning a smallerŽ payoff of ${ R } _ { 3 } ^ { \phantom { - } } )$ and hence, the dilemma. The model is traditionally viewed as a useful tool for studying conflicts between self goals and group goals in an organizational or societal setting such as that which often occurs during an Aarms raceB between nations in a region or between criminals jointly involved in the commission of a crime. To elaborate, in the latter scenario, two prisoners are charged with the same crime. Both can be convicted if even one confesses Ž . Ž i.e., defects . If both prisoners hold out i.e., cooperate , both will be acquitted. If both confess, both will. be convicted and sentenced. If only one confesses, he will be given a lighter sentence while the other will earn a more stringent sentence than if he had also confessed.

An extension of the above scenario is the Iterated Prisoner’s Dilemma IPD game where a player hasŽ . multiple AencountersB with another, over time. Each encounter involves a move and a countermove by the two players. Here, a player has the choice of exploiting prior experience in plotting moves in subsequent encounters. An IPD AtournamentB consists of a series of IPD games, played with a single or multiple opponents.

The IPD problem is one that has received considerable research scrutiny from economists, political scientists, and social scientists. However, it is also a useful test-bed for studying adaptive agent behavior from an information systems<sup>r</sup>computational science perspective. By Aadaptive agentB we mean a special purpose, intelligent, software entity that seeks to autonomously evolve its knowledge state over time to better cope with a situation it is faced with.

Prior research e.g., Refs. 3,4,6,7 documents theŽ <sup>w</sup> <sup>x</sup>. design and functioning of agents for assisting humans or other entities with specific tasks. These include, processing email, setting up meeting schedules, filtering information e.g., data and text mining , Ž . web browsing, auditing, collaborative product design, software design, capacity planning, battle simulation, teaching, and electronic commerce-related activities e.g., buying and selling, pricing, negotiation .Ž . The vast bulk of the above settings involve either single agents or artificial agencies i.e., multi-agentŽ systems whose members are intentionally designed . to be cooperating entities. In some settings like electronic commerce, the agency encompasses both cooperating and competing entities.

Two features distinguish our work from these prior efforts. Firstly, our interest lies in examining agencies where an agent must interact with other agents whose interests may counter its own and whose operational strategies are initially unknown. Consider home buying. A buyer and a real-estate agent work with one another to purchase a new home. The buyer may or may not be up-front with the broker in regards to his<sup>r</sup>her expectations and intent<sup>r</sup>ability to purchase. Likewise, the broker may not have the buyer’s best interests at heart as his<sup>r</sup>her commission is paid entirely by a seller. Both may harbor other biases e.g., race-, age-, income-, orŽ gender-related that could motivate different behav-. ior patterns. Over time, a buyer–broker pair may learn more about one another’s operational strategies through mutual interaction. One may extend this scenario to web-based home trading where buyers, brokers, and sellers deploy artificial agents that negotiate with one another. A buyer’s agent must deal with a broker agent and discern the broker’s strategy and vice versa. Because the AopponentB is an Aunknown,B canning an effective buyer agent or broker agent beforehand becomes difficult or impractical. The situation becomes even more complex when an agent must deal with several others. Consider an extension of the above example where a buyer agent, because of the power and reach of the Internet, is deployed to deal with several brokers, each of whom represents several sellers, worldwide and the commodity involved is not limited to just homes. Where canning effective strategies is impractical for any reason, one may attempt to create agents that evolve such strategies through autonomous adaptation.

Secondly, rather than focus on a single agent or agency operating within a specific setting, like home buying, our work focuses on evaluating the performance of different adaptive agent designs in generic, competitive settings. Our agents are modeled using the Learning Classifier System LCS 2 paradigmŽ <sup>w</sup> <sup>x</sup>. and the settings involve a number of IPD tournament scenarios, some involving just a single opponent with others involving several. The opponents are pre-programmed to play specific strategies. An LCS-based agent begins its interactions with no prior knowledge of its opponent’s strategy. In early encounters, its strategies are randomly generated and, as such, it could be quite naive to begin with. Over time, it evolves its behavior in an attempt to adapt to its environment i.e., the strategies of the other play-Ž ers in the tournament . We wish to examine how. good or bad particular agent designs are at adaptation, with a view to setting the stage for other, more refined, future studies.

Our work has its roots in intriguing prior work by Axelrod 1 . We elaborate on Axelrod’s pioneering <sup>w</sup> <sup>x</sup> efforts in the following section. Section 3 discusses the design and characteristics of our LCS, the characteristics of the LCS’s opponents in the different tournaments, and contrasts our approach, and its purpose, with Axelrod’s. In Section 4, we describe our experimental design and findings. We conclude this paper in Section 5.

## 2. Axelrod’s IPD tournaments

Axelrod 1 organized three successive IPD tour-<sup>w</sup> <sup>x</sup> naments of interest to us. The first tournament involved 14 IPD strategies proposed by various researchers and a completely random player. Each strategy was repeatedly paired against each of the other strategies in round-robin fashion and the average payoff earned by each was computed. The highest average score was earned by a simple strategy called Tit-for-Tat this, and other strategies, are de- Ž scribed in the following section . A second tourna-. ment call elicited a total of 62 responses. Tit-for-Tat was again the winner.

Axelrod then examined the ability of an adaptive, genetic algorithm-based GA-based; see descriptionŽ in Appendix A system to discover superior IPD. game playing strategies when playing against opponents using known strategies and by pitting systemdiscovered strategies against one another in a tournament setting. In the former case, the GA-based system is playing in a static environment, whereas in the latter, the environment is dynamic. Our own work involves a static environment and we limit our discussions to Axelrod’s experiments in this scenario.

The eight known strategies that Axelrod used against his GA-based system were gleaned from the 62 entries in the second tournament. Together, the eight entries were shown to be representative of all entries submitted as 98% of the variance in the tournament scores could be explained by knowing any given strategy’s performance against these eight.

In Axelrod’s design, each population member is a separate, AadaptiveB IPD strategy set that, while initially randomly generated, evolves over time based on its interactions with the eight competitors who are playing predetermined strategies. We first describe the structure of each population member and then, their role in the system. Each adaptive strategy is encoded as a binary string of 70 bits, as exemplified in Fig. 1. Let odd bits record the moves made by the strategy while even bits record the opponent’s moves. Bits 1 through 6 encode the moves made by the adaptive strategy and an opponent in three hypothetical encounters prior to the beginning of the tournament. In the example, this hypothesized pre-tournament history of moves is 1, 0, 1, 0, 0, 0 where a bit Ž . value of 0 denotes AdefectedB and 1 denotes Acooperated.B ŽBits 1, 3, and 5 refer to the adaptive strategy’s moves, while bits 2, 4, and 6 refer to the opponent’s moves in the last three hypothetical encounters ..

<table><tr><td colspan="6">HYPOTHESIZED PRE-TOURNAMENT MOVE HISTORY</td></tr><tr><td>SELF BIT 01</td><td>OPPONENT BIT 02</td><td>SELF BIT 03</td><td>OPPONENT BIT 04</td><td>SELF BIT 05</td><td>OPPONENT BIT 06</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr></table>

<table><tr><td></td><td colspan="7">POSSIBLE ACTUAL MOVE HISTORIES</td></tr><tr><td>SELF→</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td>0</td><td>1</td></tr><tr><td>OPPONENT→</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td>1</td><td>1</td></tr><tr><td>SELF→</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td>1</td><td>1</td></tr><tr><td>OPPONENT→</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td>1</td><td>1</td></tr><tr><td>SELF→</td><td>0</td><td>0</td><td>1</td><td>1</td><td></td><td>1</td><td>1</td></tr><tr><td>OPPONENT→</td><td>0</td><td>1</td><td>0</td><td>1</td><td></td><td>1</td><td>1</td></tr><tr><td>RECOMMENDED</td><td>Bit 07</td><td>Bit 08</td><td>Bit 09</td><td>Bit 10</td><td>... ..</td><td>Bit 69</td><td>Bit 70</td></tr><tr><td>NEXT MOVE→</td><td>0</td><td>0</td><td>0</td><td>0</td><td>... ..</td><td>1</td><td>1</td></tr></table>

Fig. 1. Axelrod’s 70-bit knowledge representation scheme.

Bits 7 through 70 record the moves the adaptive strategy would perform given each of the $2 ^ { 6 } = 6 4$ possible actual move histories. Thus, bit 7 whichŽ has a value of 0 denoting AdefectB. is interpreted as AIf I and the opponent both defected in the last three encounters, then I must defect in the next encounter.B The remaining 63 bit positions may be similarly interpreted. By recognizing that bits 1–6 record hypothetical prior moves and by associating specific actual historical moves with specific bit locations in bits 7 through 70, one need only store a string of 70 bits $( \mathrm { e . g . , } ( 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , \ldots , 1 ,$ , 1 for the  . example strategy shown rather than the more elabo- . rate matrices shown above for our example. The initial population consists of 20 randomly generated 70-bit strings.

Given the above structure, here is how the GAbased system functions against a single opponent. Initially, all 20 strategies have equal AfitnessB Ži.e., are viewed as being equally useful and one of these. twenty strategies is randomly selected to determine the move for the very first encounter with the opponent. Bits 1–6 are examined and the move recommended for this combination of bits is read off by going to the appropriate location in bits 7 through

70. For example, if bits 1 through 6 are 1, 0, 1, 0, 0, Ž 0 the move used is that stored at bit location:.

$$
\begin{array}{c} 1 \times 2 ^ {5} + 0 \times 2 ^ {4} + 1 \times 2 ^ {3} + 0 \times 2 ^ {2} + 0 \times 2 ^ {1} \\ + 0 \times 2 ^ {0} + 7 = 3 2 + 0 + 8 + 0 + 0 + 0 + 7 = 4 7. \end{array}
$$

Suppose the move stored at this bit is A1B for AcooperateB. The system performs the recommended move. Both the system’s and the opponent’s move are recorded in a separate 6-bit Aactual historyB buffer for that opponent. The above procedure is repeated two more times until the actual history buffer is full—i.e., the system has the actual history of moves for the last three encounters. Bits 1–6 of each population member have served their purpose and the system can now rely on actual move history for subsequent encounters, with the buffer working on a FIFO basis. Given this understanding, we next provide further details on how the system evolves.

In each generation of the adaptive process, each of the 20 adaptive strategies plays independent IPD games against each of the eight competitors in turn Žseparate actual move history buffers are maintained for each opponent . Each game consists of 151 en-. counters between the two players involved. After each encounter, each of the two players involved receives a payoff one ofŽ $R _ { 1 } = 5 , \ R _ { 2 } = 3 , \ R _ { 3 } = 1$ and $R _ { 4 } = 0$ , depending on the moves made . The. total payoffs for the eight games played by an adaptive strategy in one generation are averaged to yield an average score for that strategy in that generation. ŽAxelrod uses a weighted averaging procedure with the weights chosen to provide the best possible representation of the 62 tournament 2 entries by the eight representatives. The scores obtained by the 20 . strategies are used as their fitness measures at the end of the current game. A new game begins with a new initial population determined from the current population using these fitness values.

Axelrod uses the mean and standard deviation of the population fitness values to select AparentsB for procreation. Randomly paired parents from the poolŽ of available parents are subjected to probabilistic. crossover and mutation to create two offspring. The process continues until a new generation of individuals is created. The new generation constitutes the second stage of the tournament and the players go through IPD games as in the previous generation. This process continues until 50 generations are complete. Each adaptive player in the population at this point is the result of an evolutionary process that lasted fifty generations. Their fitness values reflect how well each fared against the eight opponents. To account for the impact of the random starting population on performance, the evolutionary process was independently replicated a total of 40 times and the results aggregated.

The experiment yielded the following insights.

A.1. Most strategies evolved by the GA exhibited Tit-for-Tat-like behavior in special circumstances, as depicted below in $^ { 6 6 } \mathrm { I F }$ condition² :™THEN ² : action B rule form:

Ž .a CC CC CC™C: i.e., follow three mutual cooperations with a cooperation;

Ž . b CC CC CD ™ D: i.e., return the compliment after an unexpected defection;

Ž .c DC CD CC™C: i.e., cooperate after cooperation has been restored;

Ž . d CD CC CC ™ C: i.e., cooperate after mutual cooperation has been restored following an exploitation by the opponent;

Ž .e DD DD DD ™ D: i.e., follow three mutual defections with a defection.

A.2. The GA generally evolved populations whose median member was just as successful as Tit-for-Tat.

A.3. In 11 of the 40 replications, the median strategy actually did much better than Tit-for-Tat. This success generally came about because the strategy was willing to AexploitB an opponent while running the risk of being exploited in turn by a few other players.

In closing, Axelrod’s experiments demonstrated three things, in particular. First, it is possible to construct artificial agents capable of evolving Astrategic thinkingB abilities autonomously. Second, it is possible to construct agents that are at least as good as humans at what they do. Third, in the IPD context, strains of the best human-developed strategy— Tit-for-Tat—that outperform it, are artificially evolvable.

## 3. The Learning Classifier System and opponents

Axelrod’s adaptive agent is designed based on the following assumptions:

B.1. An adaptive agent is a compound entity. Its knowledge store is capable of storing a number Ž . 20, in Axelrod’s experiments of alternative game playing strategies. Each strategy may itself be viewed as a simple adaptive agent.Ž .

B.2. Conceptually, each such simple agent has complete strategic information. Given that the agent seeks to react on the basis of moves made in the last n encounters by both players:

Ž .a in any stored strategy, information on each player’s last n moves is known at all times—i.e., each strategy’s condition portion has length 2 n; Ž . b information about all $2 ^ { 2 n }$ possible gameplaying strategies is known at all times—i.e., $\bar { 2 } ^ { 2 \bar { n } }$ possible conditions and associated suggested Anext movesB are known.

B.3. Each simple agent has perfect strategic information—i.e., information about each of the $2 ^ { 2 n }$ possible strategies of size 2 n<sup>q</sup>1 is known unambiguously.

B.4. The compound agent plays separate IPD games against each of the eight opponents in each GA generation. Consequently, in a single IPD game, each of its constituent simple agents deals with one and only one opponent.

In sum, Axelrod modeled a compound agent $( \mathrm { i . e . }$ one made up of multiple other AsimpleB agents that. assumes that complete and perfect historical information is available. He tested this agent’s evolutionary ability against individual opponents. As we described earlier, Axelrod’s 70-bit knowledge representation scheme for a strategy mitigates much of the actual storage burden in regard to B.2. Each simple agent does not explicitly store the $2 ^ { 2 n }$ possible historical states but uses an indexing mechanism whereby a specific possible state is associated with a specific bit position in the scheme. Nonetheless, by requiring $( 2 \bar { n } + 2 ^ { 2 n } )$ bits for each simple agent, the model assumes complete knowledge and each knowledge fragment each bit position denotes one such frag- Ž ment is perfectly known i.e., must take on values 1. Ž or 0 . As. n grows, requiring complete and perfect information becomes prohibitively expensive. Further, the knowledge base contains knowledge encoded about multiple such simple agents.

Such considerations motivate our desire to explore an adaptive agent that differs from Axelrod’s in each of the above dimensions, as well as in others. Firstly, we wish to study the behavior of a single, simple adaptive agent although it is possible, even Ž with our approach, to create a compound agent .. Secondly, an agent need not possess complete information in the two senses described in B.2 above. That is, an agent could implicitly or explicitly store Ž . and process information about fewer than the 2<sup>2</sup> <sup>n</sup> possible strategies. In each strategy, an agent may choose to store information on both players’ moves or just a single player’s moves in the last n encounters i.e., each knowledge fragment may be of length Ž n or 2 n.. Because complete information in accordance with B.2. b above is not maintained, it also Ž . becomes unnecessary to identify and store next moves for all possible historical states.

Thirdly, an agent need not possess perfect strategic information as described in B.3 above. The incomplete historical information may also be uncertain or unreliable. Fourthly, historical information must be updateable. What is known with certainty may become uncertain or unknown after a while. What is uncertain or unknown, may become known with certainty subsequently. An agent should ideally be able to cope with such desirable and undesirable changes to its knowledge store and yet make decisions and evolve over time in increasingly fruitful ways. Fifthly, an agent need not operate in a world where it must play only a single opponent at a time. In a single iterated game, it may be required to play a series of opponents, possibly a different opponent in each encounter of the game. Its evolution is guided by how it fares against all of these opponents and not just one. To be successful, the simple agent, despite being armed with incomplete and imperfect knowledge, must be able to cope with all such opponents while not having the advantage of dealing with each one in isolation i.e., in separate games .Ž .

Thus, the agent modeled in this paper differs from Axelrod’s in its architecture i.e., is modeled entirely Ž as a simple agent and its underlying operating as- . sumptions assumes incomplete and imperfect infor- Ž mation . Further, apart from examining its perfor- . mance against individual opponents we also wish to see how it fares in various multi-opponent settings.

One may model the kind of agent envisaged using the Learning Classifier System LCS paradigm. Fig. Ž . 2 depicts the functionality of the LCS-based, simple adaptive agent. The LCS begins with a randomly generated set of P classifiers in its knowledge base. During repeated encounters with one or more opponents, it refines its classifiers through the use of a GA. Each classifier is a game-playing strategy defined using the alphabets 0, 1, and a, as exemplified below in the familiar AIF condition² : ² ™THEN action:B rule form:

$$
\text { Strategy   1:1011\#\# } \to 0
$$

$$
\text { Strategy   2:0\#\#\#01\to1 }
$$

$$
\text { Strategy } P: 1 0 0 \# 0 1 \rightarrow 0
$$

The condition portion of each rule in our example contains some number of values six in the exampleŽ . drawn from our ternary vocabulary set. The action portion contains one and is restricted to be either a 0 or a 1. The six values in the condition pertain to moves made by the LCS and an opponent during the preceding three games. Allowing A1B to denote Acooperate d ,Ž . Ž . B A0B to denote Adefect ed ,B and AaB to denote Aeither cooperate d or defect ed ,Ž . Ž . B Strategy 1 says:

![](/api/attachments/F75BMBVJ/fulltext/images/812fcd7490bbdfabf6767034886080d7e693cdaf5414e362ebccc99886dd6c2f.jpg)  
Fig. 2. The simple agent’s functionality in a single replication.

IF I cooperated and my opponent defected in ² Game 1 .AND. we mutually cooperated in Game 2: ² :™THEN I should defect in Game 4 .

The roles played by AaB are two-fold and require some clarification. As mentioned, the most obvious role is to denote Aeither cooperation or defectionB occurred. In other words, AaB could be interpreted to mean that the actual occurrence is currently Aunknown,B Aunclear,B or Aforgotten.B Because the behavior of our LCS is not intended to be a function of the particular interpretation attached, the exact interpretation is unimportant and we may take AaB to mean, AI don’t care.B Thus, the a symbol enables us to equip the LCS to explore a strategy that states, for example:

While I have the memory to retain and use information from up to the last three encounters, I am using just the information from the first two of these encounters, because the remaining information is currently unknown, unclear, or forgotten.

A second motivation for using the AaB as part of the vocabulary is to better facilitate the evolutionary process. Consider a scenario where an LCS has just two classifiers, as below with noŽ a signs permitted in the classifiers :.

Classifier 1: 000000™0

Classifier 2: 000000™1

Initially, the game history buffer contains a series of 6 empty slots as in,Ž . aaaaaa as no games have been played. A single encounter encounter 1 ofŽ game 1 occurs. One of the two classifiers above is. randomly selected vide step 3 of Fig. 2 , say classi- Ž . fier 2, and the move recommended by it 1 isŽ . performed by the classifier. Suppose the opponent also played a A1.B The history record now consists of the move and counter move in this one game, as in aaaa11. The fitnesses of the two classifiers undergo adjustments as shown in steps 5, 6, and 7 of

Fig. 2 the details are immaterial to this discussion .Ž . For the next encounter, the LCS attempts to find a classifier in its knowledge base that matches the history stored in memory. No such classifier exists. So, in accordance with step 9 of Fig. 2, it randomly selects based on fitnesses one of the two classifiersŽ . shown above to determine its next move. As the process continues, as long as the history buffer contains a A1B entry anywhere at all, the selection of the next classifier to fire will continue to be such a fitness-based random selection process.

Essentially, by forcing all classifiers to be perfectly specified i.e., noŽ . Aa’sB allowed , the extent to which the LCS is able to directly exploit actual historical knowledge is curtailed. In our LCS, we only use the fitness values to a help select aŽ . classifier for firing when a single, history-matching classifier cannot be located in step 9 of Fig. 2 , and Ž . Ž . Ž . b create the gene pool in step 10 of Fig. 2 . If a single, matching classifier is located in step 9 , it isŽ . fired regardless of whether it is the fittest.

Thus, the specialization and generalization operators serve a purpose similar to the mutation operator in a conventional GA-based application. Mutation, if used in sufficient doses, introduces much-needed genetic diversity in a stagnant population. So also, the generalization operator by changing 1’s and 0’s to a’s with some, small probability , serves toŽ . create classifiers that can match actual history and head off an impasse situation like the one just described in the example. The specialization operator, likewise, works in the opposite manner by attempting to curtail the creation of classifiers that are all too general—i.e., have a large number of a symbols in their antecedents. If all classifiers only had Ž a’s on their LHSs, again, any of these classifiers would match the history log and the LCS’s evolutionary process again reduces to the state described in the Ž . example above..

In actual storage, each classifier in the above example is of length $2 n + 1$ . Total storage for all P classifiers for a simple agent is $P ( 2 n + 1 )$ , as opposed to $( 2 n + 2 ^ { 2 n } )$ in Axelrod’s compound agent model. In the example, each classifier’s memory is limited to knowledge of both players’ moves in the last three encounters. Memory characteristics of a specific LCS may be different from that of another. For instance, an LCS may be programmed to recall moves made in the last 10 encounters or to remember only an opponent’s moves and not its own.

The parameters that we used in our LCS, their descriptions, and our rationale for the particular parameter settings used are as below.

## 3.1. Population characteristics

The LCS always works with a fixed population of $P = 5 0$ classifiers. The string length, $L ,$ of each classifier is a function of the number of prior encounters, n, that the LCS seeks to recall and the recall pattern, R. We used different n values for different experiments as detailed in Section 4 and Ž . one or both of two recall patterns: $R = O$ Žrecall the opponent’s moves only for the last n encounters and . $R = B$ Žrecall both the LCS’s and the opponent’s moves for the last n encounters , depending on . experiment. Thus, $L = n + 1$ if R<sup>s</sup>O and $L = 2 r$ 7 <sup>q</sup>1 if R<sup>s</sup>B.

## 3.2. Genetic operators and operator probabilities

As with a conventional, binary alphabet-based GA, we use the mutation operator to probabilistically transform a 1-bit to a 0-bit and vice versa and the crossover operator to exchange genetic material between parents during procreation when creating a new population. In addition, the ternary alphabet set used permits two more genetic operators to be defined. The generalization operator enables probabilistic transformation of a 0-bit or a 1-bit to a a Ži.e., known to unknown<sup>r</sup>unclear<sup>r</sup>forgotten and special- . ization permits similar transformation, but in the opposite direction. We set the mutation probability $p _ { \mathrm { m } } = 0 . 0 0 1$ , the crossover probabilities for the condition and action parts, $p _ { \mathrm { c c } }$ and $p _ { \mathrm { c a } } ,$ at 0.6 and 0.5, respectively, and the specialization and generalization probabilities, $p _ { \mathrm { s } }$ and p , at 0.05 and 0.001, $p _ { \mathrm { g } }$ respectively.

Our rationale for the above value choices is as follows. Our focus in this paper is not on determining optimal operator probability values. Rather, for a given set of plausible values, we wish to examine specific characteristics of the LCS’s adaptive behavior see Section 4 when pitted against opponents Ž . following different pre-programmed strategies. Consequently, to the extent possible, we relied on available guidelines, if any, in choosing values. In the absence of such guidelines we made what we felt were reasonable choices.

Insofar as mutation and crossover are concerned, prior research by DeJong 8 has shown that a muta- <sup>w</sup> <sup>x</sup> tion probability of about 0.001 and a crossover probability of about 0.6 generally work well in function optimization problem settings regardless of whether the focus is AonlineB or Aoff-lineB GA-system performance. Subsequent work 5,11,15 has focused on<sup>w</sup> <sup>x</sup> identifying values better suited for enhancing either off-line or online performance. Similarly, some work Že.g., Refs. 14,16 have been done on adaptively<sup>w</sup> <sup>x</sup>. adjusting probabilities during system operation for both function and combinatorial optimization tasks. To our knowledge, little prior work along these lines is available for machine learning applications of GAs, such as ours. While Goldberg 10 notes that <sup>w</sup> <sup>x</sup> actual machine learning applications are often concerned with maintaining a high level of online performance, determining appropriate parameter levels is, as yet, more of an art. Consequently, we have chosen to stay close to DeJong’s AcompromiseB settings of 0.001 and 0.6.

We apply mutation with the same probability to both the condition and the action portions of a classifier as mutation is a bit-wise operator and each bit position is semantically no different from any other bit position. However, we have defined separate crossover probabilities for the two portions as Ž . crossover is not a bit-wise operator and , semantically, the condition and action portions of a classifier are different from one another. We would like to be able to perform independent crossovers on these semantically different portions. However, the action portion of any classifier, unlike the condition portion, is a single bit. Performing crossover on two single bits i.e., the two action portions of two Ž classifiers is tantamount to exchanging these bits.. By setting $p _ { \mathrm { c a } }$ to 0.5 rather than 0.6 , we allow a Ž . 50-50 chance for the exchange.

Similarly, we have no knowledge of prior work on selecting suitable specialization and generalization operator probabilities. While these operators, like mutation, are intended to be used sparingly and,Ž hence, our choice of the low probability values ,. specialization is accorded an occurrence likelihood that is 50 times that of generalization, biasing the LCS to accumulate and retain perfect knowledge while allowing room for imperfection.

## 3.3. Simulation characteristics

As we mentioned in the Introduction, an IPD tournament is made up of a number of games, with each game made up of a number of encounters between opponents. Each tournament constitutes a single a run or replication in our simulation. We set the number of games per run, $G = 5 0 \mathrm { \Omega }$ , and the number of moves i.e., encounters per game,Ž . $M =$ 200. To account for the random starting population in each tournament, we performed 100 independent replications of the tournament and aggregated findings across these replications.

## 3.4. The genetic algorithm

In GA terminology, each game in a tournament constitutes a single Ageneration.B Thus, the LCS goes through 50 generations of evolution in a single simulation run. In each generation, it performs 200 moves against one or more opponents. Thus, on the whole, the LCS goes through $5 0 \times 2 0 0 = 1 0 \mathrm { , } 0 0 0$ moves in our experiments spread evenly through 50 generations.

In step 1 of Fig. 2, a constant initial fitness value, $F = 3$ , is assigned to each classifier. This value varies with time based on each classifier’s performance, but is always non-negative. In step 5, the firing classifier is charged by decreasing its current fitness $F ^ { \prime }$ by an amount $\delta F ^ { \prime } = 0 . 5$ for the privilege of being selected to fire and to discourage classifier’s that Awish to play it safeB from participation. The payoff matrix parameters used in step 6 are as Ž . follows: $R _ { 1 } = 5 , R _ { 2 } = 3 , R _ { 3 } = 1$ , and $R _ { 4 } = 0$ . Step 7 makes use of the following credit apportionment procedure to revise the fitness values of the firing classifier and all classifiers that AenabledB it to fire. Beginning with the most recently fired classifier, propagate an exponentially decreasing portion of the Ž Ž .earnings, E, i.e., wE, w 1 <sup>y</sup> w E, w $( 1 - w ) ^ { 2 } E , \dots )$ to all classifiers fired thus far, in reverse order of firing the weighting factor,Ž $w = 0 . 5 )$ . In step 9, note that a $" \# ^ { , \bullet }$ symbol at a position in a string matches any alphabet i.e., 0, 1, orŽ $\# )$ at the corresponding position in the other string. Steps 10 and 11 embody the GA that guides population evolution. Selection size, $S = 4$ , is a parameter used by the GA module to help populate the gene pool see step 10 .Ž .

## 3.5. Opponent types and opponent groupings

We wish to examine the LCS’s performance in IPD tournaments against one or a set of opponents. We discuss various experimental setups in the following section. Here, we present a brief description of the kinds of opponents used in our experiments. Drawing on Axelrod’s work, we used the following nine opponent types.

RAND: generate next move randomly regardless of what the opponent does. A AmindlessB strategy. Adaptation becomes difficult due to the chaotic behavior of the opponent.

CCC: always cooperate regardless of what the opponent does. The most AgenerousB strategy.

DDD: always defect regardless of what the opponent does. The most AhostileB strategy.

TFT Tit-for-Tat : cooperate in the first game. Ž . Thereafter, play the same move, in the current game, as your opponent did in the last game. Starts out generously and then resorts to vengeance.

TFTT Tit-for-Two-Tat : cooperate in the firstŽ . game. Thereafter, only defect in the current game, if the opponent defected in both of the last two encounters. Starts out generously. Thereafter, is less vengeful or more forgiving than TFT.Ž .

TTFT Two-Tits-for-Tat : cooperate in the first Ž . game. Thereafter, repay an opponent’s defection, with a defection in the next two games. Starts out generously. Thereafter, is more vengeful than TFT.

GTFT Generous-Tit-for-Tat : cooperate in theŽ . first game. Thereafter, defect with less than 100% certainty in the current game if your opponent defected in the last game. Begins generously. Thereafter, is less vengeful than TFT. We set the defec-Ž tion probability at 90%..

JOSS Joss’s strategy : proceed as in TFT. Occa-Ž . sionally, sabotage the opponent even if he has been cooperating—i.e., defect, with some predefined likelihood, even though TFT suggests cooperation. We Ž set the defection probability at 10%. Begins by . being generous. Thereafter, occasionally turns vengeful even without reason to.

FRDM Friedman’s strategy : start out cooperat-Ž . ing and continue cooperating until your opponent defects. Thereafter, continue defecting regardless of what the opponent does. Begins by being generous. Turns and remains permanently hostile if the opponent betrays even once.

The players in the tournament may be categorized in various ways. As noted, the LCS itself is an AadaptiveB player. Its behavior changes with time, is a function of its starting state and prior interactions with its environment, and is not wholly predictable. One way of categorizing the LCS’s opponents is as follows. Strategies RAND, CCC, and DDD belong to the class AFixed.B They are opponent-invariant as they do not take cognizance of an opponent’s prior move s . The remaining six strategies areŽ . AReactive.B All of them respond in some way to what an opponent does. Of these, the first five are TFT variants. The last, FRDM, may be viewed as an AirreversibleB strategy—once it decides to defect, there is no turning back. Another approach to classification is as follows. The strategies RAND, CCC, TFTT, and GTFT may collectively be labeled as the ANicerB strategies, whereas DDD, TFT, TTFT, JOSS, and FRDM collectively constitute the AMore HostileB class. Lastly, the strategies CCC, DDD, FRDM, TFT, TFTT, and TTFT are wholly APredictableB in their behavior whereas RAND, GTFT, and JOSS are not i.e., areŽ . AUnpredictableB .

## 4. Experiments and observations

Our experiments may be divided into five sets. In each set, we hold several of the LCS parameters constant while altering a select few. Sets 1 through 4, each involve the LCS playing against a single opponent at a time. This series of experiments sets the stage for those in Set 5, where it plays against groups of multiple opponents simultaneously.

## 4.1. Experiment Set 1

Set 1 examines the behavior of an LCS LCS 1Ž . against each of the fixed and reactive strategies described in Section 3, in separate IPD games. Set 1 may be regarded as a AbaseB scenario that we progressively perturb in the remainder of our experiments. It is characterized by the following unique settings all other parameters are set as described in Ž Section 3 :.

Number of opponents Faced: 1

Number of prior Encounters to recall, n: 5

Recall pattern, R: O

String length of each classifier, L: n<sup>q</sup>1<sup>s</sup>6.

Thus, the LCS stores historical information on the last five moves made by an opponent. Fig. 3 depicts the best and worst performances of this LCS in each of the two classes of strategies: Nicer and More Hostile. Each curve plots the relative performance of LCS 1 over the average performance of both players Ž . i.e., the LCS and an opponent for each of the 50 generations. The scores plotted are the averages of Ž . LCS’s Score-Average Score across the 100 independent replications. It records its best performance against CCC in the Nicer class and TFT in the More Hostile class. Its worst performance occurs with GTFT and DDD in the two classes, respectively. Overall, it does best against CCC and worst against DDD.

In all cases except with TTFT, there is a sharp AgainB in relative performance in the early stages of evolution i.e., within about 4 to 10 generations,Ž although this is not clearly reflected in the figure due to the scaling used after which performance drops. and then stabilizes. The sharp growth is due to the vast relative gains reaped during early stages of adaptation beginning with a random set of classifiers. As time wears on, realizing further improvement becomes harder. The drop in performance after the spurt indicates that both players are tending more to the average score. This drop to a comparatively more stable relative performance level occurs within about 4 to 17 generations following growth. Stabilization occurs no later than generation 20 or so, across all cases.

Table 1 depicts the aggregated value of LCS 1’s game-wise performance across all 50 games de- Ž noted as Sum-All 50 , against individual members of . the Nicer and More Hostile classes. Thus, Sum-All 50 tells us by how much the LCS bettered the average of both players in aggregate terms across all 50 games. Such a measure of performance is appropriate given that our interest lies in examining the extent of success of the LCS since inception or its AonlineB performance. We focus on online performance because our agent is intended to adapt from primitive beginnings against an unknown opponent.

![](/api/attachments/F75BMBVJ/fulltext/images/42deae76c5a386baa5f3ca32732e0b95858bf5f9ab687d8e80e9233e82a48d1d.jpg)  
GAME, G  
Fig. 3. Experiment Set 1—LCS 1’s relative best and worst performances.

In situations where the kind of opponent that an agent would encounter is known and one has the opportunity to train the agent before deployment, one could take advantage of the situation and release a more refined agent to play the opponent. In this case, our focus, instead, would be on an agent’s Aoff-lineB or post-evolutionary performance—i.e., the performance that accrues once the agent’s behavior has stabilized and no further improvement can be realized. For example, if our LCS were evolving for the first 20 games and its relative performance remains Ž . more or less steady for the remainder of the games, we would view the system as having stabilized at game 20 and our focus would be on its subsequent performance. In yet other situations, our interest may lie in AterminalB performance at some, pre-defined stopping point, regardless of whether stabilization has occurred or not.

We have also shown the ranking of the LCS’s performance against each opponent, with the smallest rank being ascribed to the best performance, and rank sums for the two classes of strategies. The Sum-All 50 scores range from about 1781 for GTFT to about 12,628 for CCC in the Nicer class. The LCS fares significantly worse against the More Hostile strategies. The best score 81.25 within this group is Ž . recorded against TFT and the worst Ž . <sup>y</sup>9414.71 against DDD.

Table 1  
Relative performance of LCS 1 against the nine opponents

<table><tr><td colspan="12">Experiment Set 1: n = 5; R = O; L = 6</td></tr><tr><td rowspan="2"></td><td colspan="5">Nicer strategies</td><td colspan="6">More Hostile strategies</td></tr><tr><td>RAND</td><td>CCC</td><td>TFTT</td><td>GTFT</td><td>SUM</td><td>DDD</td><td>TFT</td><td>TTFT</td><td>JOSS</td><td>FRDM</td><td>SUM</td></tr><tr><td>Sum-All 50</td><td>6272.59</td><td>12,628.33</td><td>6398.59</td><td>1781.00</td><td></td><td>-9414.71</td><td>81.25</td><td>-5660.37</td><td>-739.58</td><td>-9010.80</td><td></td></tr><tr><td>Rank</td><td>3</td><td>1</td><td>2</td><td>4</td><td>10</td><td>9</td><td>5</td><td>7</td><td>6</td><td>8</td><td>35</td></tr></table>

From the earnings, ranks, and rank sum values, observe that LCS 1’s performance against the Nicer category is far superior as expected to its perfor- Ž . mance against the More Hostile class. The relative performances against individual opponents also present an interesting picture. If we sequence all of the nine opponents in order of performance by the LCS Ž . from the best performance to the worst , we obtain: CCC, TFTT, RAND, GTFT, TFT, JOSS, TTFT, FRDM, and DDD. The extremely nice CCC and the extremely unfriendly DDD form the boundaries of this spectrum. Among the opponents, CCC and DDD are both100% predictable and persistent i.e., per-Ž form the same move repeatedly in their behavior. It. is their repetitious behavior that sets them apart from other predictable opponents such as TFT. Intriguingly, while LCS 1 records its best performance against CCC, it also records its worst against DDD. Why does this LCS find DDD such a challenge?

First, against DDD, any LCS is bound to register a non-positive Sum-All 50 value. This is because, until the LCS discerns DDD, it will be made a sucker by DDD. Once it discerns DDD and starts sustained defection itself which is the best thing to Ž do , it can only tie with the opponent in terms of. payoff. Thus, the LCS-AVG score can at best be 0, at any move of any game. Given that it is very likely that any LCS will be suckered at least once before it adapts to a state of sustained defection if at all ,Ž . Sum-All 50 can at best be 0 and in all likelihood, negative.

Secondly, one would expect any LCS’s behavior to be influenced by its design and its feedback mechanism. Let us consider LCS 1’s feedback mechanism first. The feedback it receives after each of its moves is in the form of a payoff for the move. Its payoff is $R _ { 3 } = 1$ when it defects and $R _ { 4 } = 0$ when it cooperates against DDD. Contrast this with the feedback it receives when playing CCC. There, the LCS receives a payoff of $R _ { 2 } = 3$ when it cooperates and

$R _ { 1 } = 5$ when it defects. The payoff received is propagated back using the Abucket brigadeB procedure that uses a weight of $w = 0 . 5$ . This procedure offers w<sup>=</sup>payoff to the firing classifier and propagates progressively decreasing reward portions to other, enabling classifiers. As we have noted, the firing classifier also incurs a charge of $\delta F ^ { \prime } = 0 . 5$ for firing. The net reward to the firing classifier is, therefore,Ž . $w \times \mathrm { p a y o f f } - \delta F ^ { \prime }$ . When playing CCC, this net reward is either $0 . 5 \times 3 - 0 . 5 = 1 { \mathrm { ~ o r ~ } } 0 . 5 \times 5 - 0 . 5 = 2$ When playing DDD, this net reward is either $0 . 5 \times 0$ $- 0 . 5 = - 0 . 5 \mathrm { \ o r \ } 0 . 5 \times 1 - 0 . 5 = 0$ . The magnitudes of the reward values and the comparatively much smaller value difference when playing against DDD make it harder for this LCS to discern DDD than Ž CCC causing it to continually experiment with the . two moves. Thus, observe that the plot for DDD in Fig. 3 depicts considerably greater volatility than that for CCC.

The other factor that could impact performance is the LCS’s design. LCS 1 has a memory size of 5 and records its opponent’s moves only. One would expect that altering memory size and content should also alter performance. While we examine the impacts of altering the payoff matrix values in an extension to this work, we study the memory design issue further in experiment Sets 2 and 3 described in Section 4.2 below. Let us now examine the relative positioning of the remaining opponents in the sequence.

TFT is positioned in the middle of the sequence Ž . rank is 5 . It is somewhat more generous cousin, GTFT i.e., cooperate with 10% probability whenŽ TFT recommends defection , is positioned to its left. whereas the somewhat more vengeful one, JOSS Ži.e., defect with 10% probability when TFT recommends cooperation , is positioned to its right, as we . would expect. The even more generous TFTT i.e., Ž only retaliate if the opponent defects twice in succession and even more vengeful TTFT i.e., retaliate. Ž twice in succession for every defection by an opponent are positioned to the left and right of GTFT . and JOSS, respectively. This is to be expected as TFTT is more predictably generous than GTFT and TTFT is more predictably vengeful than JOSS. The almost DDD-like FRDM i.e., begin persistent defec- Ž tion once the opponent defects is positioned imme-. diately before DDD. This, too, stands to reason as the LCS has the opportunity for mutual cooperation and suckering before FRDM becomes DDD-like and can, thus, reap greater cumulative rewards with FRDM than with DDD.

Apart from DDD’s positioning in the sequence, one other counterintuitive finding is the relative positioning of RAND. One would have expected to find RAND positioned closer to CCC in the sequence—it is a AmindlessB strategy and one that an LCS ought to be able to take advantage of, although not to the extent of the very predictably docile CCC. We felt that this anomaly was a result of LCS 1’s memory design and expected to see improved performance against RAND with design changes see Section Ž 4.2 ..

Experiment Set 1 demonstrates that LCS 1 does display adaptation capabilities, although the extent of adaptation is not sufficient enough to cause it outperform some of the More Hostile opponents. The Ž . performance just observed is for an LCS with memory of the last five moves made by an opponent. We wished to see if manipulating its memory size and content would help improve its performance. This led us to the experiment Sets 2 and 3.

## 4.2. Experiment Sets 2 and 3

Set 2 is identical to Set 1 in all respects except that R <sup>s</sup> B Ži.e., store information on both player’s prior moves . We seek to detect noticeable behav- . ioral alterations, if any, given i the larger memoryŽ . size and ii the change in the nature of its contents.Ž . Set 2 is, therefore, characterized by the following unique settings:

Number of opponents faced: 1

Number of prior encounters to recall, n: 5

Recall pattern, R: B

String length of each classifier, L: 2 n<sup>q</sup>1<sup>s</sup>11.

Fig. 4 depicts this LCS’s relative best and worst performances against the two categories of opponents. As in Set 1, the LCS displays an initial spurt in relative performance and the performance against the Nicer strategies continues to be superior to those against the More Hostile ones.

![](/api/attachments/F75BMBVJ/fulltext/images/137ac6c9e5c1ff56bc2dd367157a3f8996daf697a5122df6e6b376adad25b924.jpg)  
GAME, G  
Fig. 4. Experiment Set 2—LCS 2’s relative best and worst performances.

Table 2 summarizes the performance of LCS 2 and is very similar to Table 1 in organization. In Table 2, we also show the percentage improvement Ž . i.e., % Improvement in Sum-All 50 values for LCS 2 over LCS 1. The Sum-All 50 scores in the Nicer class now range from about 2436 for GTFT to about 15,911 for CCC. In the More Hostile group, the gain ranges between <sup>y</sup>1013 for FRDM and 115 for TFT. Although the LCS still posts negative cumulative gain values against TTFT, DDD and FRDM, its performance against all nine opponents has improved substantially with the changes to memory. In particular, LCS 2 shows a positive Sum-All 50 score against JOSS where LCS 1 had posted a loss.

If one were to sequence the opponents in decreasing order of the LCS’s performance, we obtain: CCC, RAND, TFTT, GTFT, TFT, JOSS, TTFT, DDD, and FRDM. The sequence is identical to that obtained with LCS 1 except for the relative positions occupied by RAND, DDD, and FRDM. As one would expect and unlike with LCS 1 , this LCS’sŽ . performance against RAND immediately follows that against CCC. However, while DDD followed FRDM in Set 1, they trade places in Set 2. This is counterintuitive considering that LCS 1 was able to take advantage of the initial nicety of FRDM before itŽ became DDD-like . Based on our observations in. experiment Set 3 discussed below , we believe thatŽ . this anomaly is due to the particular memory size used with R<sup>s</sup>B in LCS 2. We believe that if we were to provide the LCS with enough room to store more than five prior moves by each player say 10Ž each , FRDM should precede DDD in the sequence. . ŽWe are investigating this issue further in an extension to this work..

The % Improvement in Sum-All 50 values with LCS 2 vis-a-vis LCS 1 range from about 26% for\` CCC to about 112% for JOSS. Given the very sizable improvements, we conclude that storing information regarding both players’ prior five moves is preferable to storing information on just the opponent’s although, as noted above, the LCS still postsŽ negative gains with three of the nine opponents .. LCS 2 is vested with enough memory for recording information on a total of 10 historical moves. What if we permit the system to use the excess storage capacity to record more of an opponent’s history? It would appear that with unpredictable opponents likeŽ GTFT , an LCS ought to be more interested in . preserving knowledge about what the opponent did that resulted in the LCS earning a certain reward in a certain move as opposed to what it did . That is, aŽ . suitable R<sup>s</sup>O memory design should perform better than an R<sup>s</sup>B design with such opponents. Conversely, we felt that with a predictable and persistent player like CCC, it would be preferable to store information on what the LCS did to earn a particular reward than what the opponent did as the opponent’sŽ behavior is invariant . Such concerns led us to exper- . iment Set 3.

Set 3 is identical to Set 1 but with n<sup>s</sup>10. That is, while memory size is the same as in Set 2, content differs markedly as only an opponent’s moves are stored. Thus, Set 3 is characterized by the following unique settings:

Number of opponents faced: 1

Number of prior encounters to recall, n: 10

Recall pattern, R: O

String length of each classifier, L: n<sup>q</sup>1<sup>s</sup>11.

Fig. 5 and Table 3 depict our findings. Like in Set 2, the larger memory size for this LCS LCS 3Ž .

Table 2  
Relative performance of LCS 2 against the nine opponents  
Experiment Set 2: n<sup>s</sup>5; R<sup>s</sup>B; L<sup>s</sup>11

<table><tr><td rowspan="2"></td><td colspan="5">Nicer strategies</td><td colspan="6">More Hostile strategies</td></tr><tr><td>RAND</td><td>CCC</td><td>TFTT</td><td>GTFT</td><td>SUM</td><td>DDD</td><td>TFT</td><td>TTFT</td><td>JOSS</td><td>FRDM</td><td>SUM</td></tr><tr><td>Sum-All 50</td><td>10,775.11</td><td>15,910.51</td><td>10,178.19</td><td>2435.84</td><td></td><td>-944.13</td><td>115.14</td><td>-512.93</td><td>91.81</td><td>-1013.10</td><td></td></tr><tr><td>Rank</td><td>2</td><td>1</td><td>3</td><td>4</td><td>10</td><td>8</td><td>5</td><td>7</td><td>6</td><td>9</td><td>35</td></tr><tr><td>% Improvement</td><td>71.78</td><td>25.99</td><td>59.07</td><td>36.77</td><td></td><td>89.97</td><td>41.70</td><td>90.94</td><td>112.41</td><td>88.76</td><td></td></tr></table>

![](/api/attachments/F75BMBVJ/fulltext/images/e350717b1c05e59f03f185c89c63bfc6a07205533ef6cfda07406dd27d873c60.jpg)  
GAME, G  
Fig. 5. Experiment Set 3—LCS 3’s relative best and worst performances.

results in significantly better performance against all nine opponents when compared with LCS 1. The Sum-All 50 values now range between 2564 for GTFT and 12,982 for CCC in the Nicer class and between <sup>y</sup>1863 for TTFT and 118 for TFT within the More Hostile class. Like LCS 2, LCS 3 posts a positive score against JOSS. Once again, negative performances are recorded against the same three opponents as with LCS 2, namely, FRDM, DDD, and TTFT.

Sequencing the opponents based on LCS 3’s performance yields the following list: CCC, RAND,

TFTT, GTFT, TFT, JOSS, FRDM, DDD, and TTFT. As with LCS 2 and unlike with LCS 1 , RAND nowŽ . occupies position 2 in the list as one would expect .Ž . Also note that, unlike with LCS 2, FRDM now precedes DDD as one would expect and as we observed with LCS 1. This also suggests that the relocation of FRDM that we observed with LCS 2 is perhaps due to LCS 2’s memory bank size. We are exploring the impact of alternate bank sizes in an extension to this work. The rest of the opponents, barring TTFT, which occupies the very last position, are relatively positioned as one would expect and as Ž with LCS 1 . The gains realized against TTFT by . increasing memory bank capacity from 5 to 10Ž . with the $R = O$ model are substantially less than the gains realized for FRDM and DDD, causing TTFT to slip down to the very last position.

Table 3  
Relative performance of LCS 3 against the nine opponents  
Experiment Set 3: n<sup>s</sup>10; R<sup>s</sup>O; L<sup>s</sup>11

<table><tr><td rowspan="2"></td><td colspan="5">Nicer strategies</td><td colspan="6">More Hostile strategies</td></tr><tr><td>RAND</td><td>CCC</td><td>TFTT</td><td>GTFT</td><td>SUM</td><td>DDD</td><td>TFT</td><td>TTFT</td><td>JOSS</td><td>FRDM</td><td>SUM</td></tr><tr><td>Sum-All 50</td><td>11,929.86</td><td>12,981.62</td><td>11,328.74</td><td>2,564.44</td><td></td><td>-1691.44</td><td>118.47</td><td>-1863.30</td><td>109.28</td><td>-1420.63</td><td></td></tr><tr><td>Rank</td><td>2</td><td>1</td><td>3</td><td>4</td><td>10</td><td>8</td><td>5</td><td>9</td><td>6</td><td>7</td><td>35</td></tr><tr><td>% Improvement</td><td>90.19</td><td>2.80</td><td>77.05</td><td>43.99</td><td></td><td>82.03</td><td>45.80</td><td>67.08</td><td>114.78</td><td>84.23</td><td></td></tr></table>

The % Improvement values range from 2.80% for CCC to about 115% for JOSS. Some of the % Improvement values in Table 3 show marked differences when compared with corresponding values in Table 2. For instance, while the gains realized using LCS 2 and LCS 3 vis-a-vis LCS 1 for TFT and JOSS\` are compatible, that for players like CCC and RAND, for example, are quite different. This suggests that perhaps an LCS equipped with a single memory model is inadequate against all of the opponents studied. While we are also exploring multi-memory model LCSs in ongoing work, we focus next on understanding the relative preference for $R = B$ visa-vis\` $R = O$ in experiment sets 2 and 3.

## 4.3. RelatiÕe assessment of the two memory designs

The set 2 and 3 experiments suggest that more memory i.e., information is better than less. TwoŽ . questions arise: How much more? Which memory model is better with a given opponent type, that with R<sup>s</sup>B or with $R = O ?$ While we conduct a limited exploration of both questions in the next set of experiments, the data in Tables 2 and 3 also offer some insights on the second, for the case where $L = 1 1$ . Table 4 shows the opponent strategies in terms of the percentage difference between Set 3 and Set 2 Sum-All 50 values. Table 5 also shows, whether a strategy is Fixed FX or Reactive RE , whether a Ž . Ž . strategy belongs to the Nicer N or More Hostile Ž . Ž . Ž . H class, whether a strategy is Predictable P or Unpredictable U in its behavior, and whether Ž . R<sup>s</sup>B or R <sup>s</sup> O offers better results. A few comments are in order.

From the table, we see that the particular R<sup>s</sup>O model that we studied is preferred when playing against TFT, GTFT, RAND, TFTT, and JOSS. The R<sup>s</sup>B model studied is preferred against TTFT, DDD, FRDM, and CCC. Overall, the preferences for $R = B$ are more pronounced i.e., the % difference Ž values favoring $R = B$ have larger magnitude than . those for R<sup>s</sup>O. How may one rationalize the observations in Table 4?

Consider TFT, the opponent with the smallest preference magnitude, first. It is a predictable, reactive strategy that is also hostile in that it expects an eye for an eye. The marginal 2.89% preference for $R = O$ with TFT in our simulations suggests that either of the LCSs we studied would do almost just as well with an opponent like TFT. This is because if an properly designed LCS knows any one player’s Ž . moves, it should be able to infer the other’s moves with 100% certainty over time. Thus, there ought to be no compelling preference for one memory model over the other, all else being the same. We believe that the slight preference for $R = O$ in our experiments is because it offers a fuller information set concerning one player’s moves the opponent’s, in Ž this case in comparison with . R <sup>s</sup> B, which offers only half as much. Further experimental findings Ž that we report in Section 4.4 also substantiate this view..

Consider the TFT-variants GTFT and JOSS, next. GTFT is TFT-like but with a 10% propensity for cooperation when defection is called for and JOSS shows a 10% propensity for the opposite behavior. Thus, they are reactive, hostile strategies that are also somewhat unpredictable. With an uncertain opponent, it behooves an LCS to store more knowledge on the opponent’s prior behavior as payoff realized Ž . by the LCS is not entirely controllable by the LCS Ž . as with a predictable opponent . Similarly, the more the damage that an opponent’s uncertainty could potentially do to the LCS, the stronger the preference for such storage ought to be. Thus, we see that the R<sup>s</sup>O model is preferred with both GTFT and JOSS, but much more strongly with JOSS 19.03% thanŽ . with GTFT 5.28% . The relatively smaller prefer-Ž . ence magnitude for GTFT is because GTFT’s uncertain behavior is to the LCS’s advantage whereas JOSS’s is more damaging.

Performance differences between LCS 3 and LCS 2 against the nine opponents  
Experiment Set 3–Experiment Set 2

<table><tr><td rowspan="2"></td><td colspan="4">Nicer strategies</td><td colspan="5">More Hostile strategies</td></tr><tr><td>RAND</td><td>CCC</td><td>TFTT</td><td>GTFT</td><td>DDD</td><td>TFT</td><td>TTFT</td><td>JOSS</td><td>FRDM</td></tr><tr><td>Sum-All 50</td><td>10.72%</td><td>-18.41%</td><td>11.30%</td><td>5.28%</td><td>-79.15%</td><td>2.89%</td><td>-263.27%</td><td>19.03%</td><td>-40.23%</td></tr><tr><td>Rank</td><td>7</td><td>4</td><td>8</td><td>6</td><td>2</td><td>5</td><td>1</td><td>9</td><td>3</td></tr></table>

Consider the variants TFTT and TTFT, next. These strategies, like GTFT and JOSS, are kinder and more vengeful variants of TFT, respectively, except that they are predictably so. With the very hostile, predictable, and reactive TTFT, the R<sup>s</sup>B model is preferred, and very strongly. With TTFT, two retaliatory defections by the opponent follows every one of the LCS’s own defection, each resulting in the LCS either being suckered or forced to settle for mutual-defection. The very high price paid is a predictable consequence of the LCS’s own prior defection. Thus, the R<sup>s</sup>B model does better in our experiments—i.e., the LCS that also watches itselfŽ . does better.

With TFTT, on the other hand, the R<sup>s</sup>O model does better. The preference magnitude is about twice that for GTFT and about half of that for JOSS. TFTT, like TTFT is predictable and reactive but belongs to the Nicer category. It repays every two consecutive defections by the LCS with a single defection of its own. This single retaliatory defection could result in the LCS being suckered. However, the LCS could retaliate to this by defecting twice in succession, thereby suckering the opponent twice in return. Overall, the LCS easily learns to exploit TFTT. Watching its own prior actions, as with TTFT, is no longer a priority, and the R<sup>s</sup>O model does better.

RAND is a fixed, nicer opponent. However, it is also unpredictable. As we said earlier when discussing GTFT and JOSS, with an unpredictable opponent, it is in an LCS’s interests to store more knowledge about an opponent’s past. RAND’s behavior has both beneficial and damaging aspects to it but given its high level of unpredictability, it has the potential for severely damaging the LCS, unintentionally. Thus, as with JOSS another opponent with Ž the potential for damage to the LCS , the. R<sup>s</sup>O model does better with RAND. Also observe that, interestingly, the preference for R<sup>s</sup>O with RAND lies in the middle of the R <sup>s</sup> O preference list, with TFT and GTFT to its left and TFTT and JOSS to its right.

Consider the opponents, CCC, DDD, and FRDM. First, CCC and DDD are both predictable and persistent in their behavior. Under such circumstances, it does not pay to devote any amount of available memory to storing information about the opponent. This is because the payoff realized by an LCS is entirely in its control—its own actions can result in better or worse payoffs. Thus, the R<sup>s</sup>B model, which allows the LCS to store at least some information about its own prior behavior, is preferred to the one that eschews such knowledge completely. The bias for the R<sup>s</sup>B model with CCC can also be discerned in Figs. 4 and 5—observe the greater volatility of the CCC plot in Fig. 5 vs. that in Fig. 4. Similarly, when discussing the volatility of the DDD plot in Fig. 3, we had argued that changes in memory design as well as changes in the payoff matrix Ž values could mitigate the volatility. If one plots the. DDD data for LCS 2 and LCS 3, we obtain much smoother curves than with the DDD data for LCS 1. Also, the curves for LCS 2 and LCS 3 dominate that for LCS 1 for all 50 generations while that for LCS 2 dominates the plot for LCS 3 through much of the 50 generations.

Also observe that the preference for R<sup>s</sup>B is considerably greater with DDD than with CCC, given the extreme penalty for being a sucker. That is, if the opponent is guaranteed to cooperate in every encounter, the payoff realized is determined by what the LCS chooses to do. If the LCS also chooses to cooperate, the LCS would earn 2.5 i.e.,Ž $R _ { 2 } = 3$ less the firing fee of 0.5 . If the LCS chooses to defect. instead, it will earn its highest payoff of the game of 4.5 i.e.,Ž $R _ { 1 } = 5$ .  less 0.5 . The consequences of its actions are much more severe with DDD. The LCS could also defect and earn 0.5 i.e.,Ž $R _ { 3 } = 1$ .less 0.5 or be made a sucker and earn <sup>y</sup>0.5 i.e., Ž $R _ { 4 } = 0$ less 0.5 . Thus, it is much more imperative for the LCS. to be cognizant of its own past actions with DDD and hence the relatively more pronounced preference for R<sup>s</sup>B with DDD.

FRDM starts out as CCC and suddenly begins DDD-like behavior in the face of even a single defection by the LCS. Because the onset of this Ž . sustained reversal is sudden, but triggered by the

LCS’s own prior defection, the R<sup>s</sup>B model is preferred with FRDM just as we argued that Ž Awatching its own actionsB is imperative to the LCS with an opponent like TTFT . Because FRDM is an. amalgam of CCC and DDD, it is positioned between CCC and DDD in our list.

One other comment about JOSS is in order. We believe that as one increases the defection likelihood for JOSS, and it becomes increasingly DDD-like Ž . i.e., begins to exhibit persistence , the R <sup>s</sup> B model should become more attractive at some point as it is Ž the preferred model for DDD . However, the data for. DDD also point to the existence of a limit to how attractive the R<sup>s</sup>B model can become against such an opponent. We are investigating this issue in an extension to this work.

In closing, we would like to bring up the following. First, alternate ways of grouping the opponents ought to be explored. For example, one approach is to categorize them according to which memory model does better. Secondly, we ought to examine other memory models. For instance, a model that stores only the LCS agent’s prior moves call it theŽ R<sup>s</sup>M Ž . . for Amy prior movesB model , is likely to do better than the R<sup>s</sup>B model against persistent opponents like DDD. Thirdly, it is possible that some other n value choices could yield different relative performance results for the different memory models. While we report on a limited exploration of this issue in experiment Set 4, discussed below, more detailed investigations are underway.

## 4.4. Experiment Set 4

Experiment Sets 2 and 3 suggest that memory size and memory content could be critical determinants of LCS performance against specific opponents. In experiment Set 4, we examine an LCS’s performance for even values of n in the range 4 through 12, while playing against TFT. We chose TFT for this limited exploration of the size and content impacts given aŽ . its stature as the best man-made strategy in Axelrod’s experiments, and b the fact that many of the oppo- Ž . nents used in our tests are TFT variants. In one subset of experiments, we allowed the LCS to remember only the opponent’s moves for the five n value choices i.e., RŽ <sup>s</sup>O and $L = n + 1 )$ . In another, we allowed it to recall both players moves for each n Ži.e., R<sup>s</sup>B and $L = 2 n + 1 )$ . Apart from isolating the impacts of memory size and contents on performance, these experiments also shed some light on whether maintaining an arbitrarily large memory is warranted when playing TFT.

Fig. 6a and b shows the relative performances of the two LCSs. Unlike the case where L is fixed, when it is varied, there is no convenient cutoff applicable to all the L values by which point convergence has occurred. For low values like L<sup>s</sup>5 and 7, both LCSs continue to fluctuate widely through all 50 generations. Consequently, we adopted a different measure of relative performance in these figures. At each game, G, the graphs show Cumulative LCS-Average figures beginning with game G<sup>s</sup>1.

When R<sup>s</sup>B, values of $L \geq 9$ dominate with L<sup>s</sup>13 resulting in the highest cumulative performance values for much of the run length. While it marginally outperforms $L = 1 1$ in early games, the gap between L <sup>s</sup> 13 and L <sup>s</sup> 11 progressively widens. With R<sup>s</sup>O, on the other hand, L<sup>s</sup>13 and L <sup>s</sup> 11 post near-identical performance values throughout the 50 games. While L<sup>s</sup>13 held a slight edge until game 40, L<sup>s</sup>11 marginally outperformed L<sup>s</sup>13 during the last 10 games. These limited runs suggest that depending on the run length of interest, either L<sup>s</sup>11 or L<sup>s</sup>13 is the best of the examined choices for R<sup>s</sup>O, while L<sup>s</sup>13 is best with R<sup>s</sup>B.

Upon contrasting Fig. 6a and b, we discern some support for our earlier opinion that, given an appropriate choice of L, with TFT, neither memory model should dominate the other. Notice that the plot for L<sup>s</sup>13 for R<sup>s</sup>B is nearly identical to that for L<sup>s</sup>13 orŽ . L<sup>s</sup>11 for R<sup>s</sup>O; the net difference in relative earnings across all 50 games is almost nil—in the neighborhood of 1. However, when the L value becomes appreciably smaller than the ideal, memory content does make a difference. Thus, observe that the slope for L<sup>s</sup>5 in Fig. 6a is markedly steeper than that in Fig. 6b. The LCS is able to ascertain the Tit-for-Tat behavior of the opponent much better when it is explicitly encoded as in R Ž . <sup>s</sup> B than when it must be otherwise inferred as in RŽ . <sup>s</sup>O .

In sum, experiment Set 4 tells us that, against TFT, as one increases the classifier length L, thus enabling the storage of additional information, the performance of the LCS improves. However, one discerns increasingly diminishing returns with increasing L value and there is some evidence that more information my actually result in performance degradation over time asŽ $L = 1 1$ marginally outperforms $L = 1 3$ in the last 20% of the games for $R = O )$ . Further, while memory content makes a big difference, with $R = B$ being preferred to $R = O$ for smaller L value choices, with increasing $L ,$ either memory model would do nearly as well as the other. In other words, the LCS’s inferential abilities seem to diminish with smaller memory sizes and it needs to explicitly encode both players’ prior moves. Again, additional tests, involving a more exhaustive L value choice set and also including the R<sup>s</sup>M memory model is ongoing and should shed further light on such issues.

(a)  
![](/api/attachments/F75BMBVJ/fulltext/images/5e3d9ef5f82e6deccd9761197d41a6b6d4748dd2243da6f2821edfaf5d33f492.jpg)

(b)  
![](/api/attachments/F75BMBVJ/fulltext/images/6d57a6166c4336eea14b3406f3709149065842a7c754d17ec1d61d5ae4b6b984.jpg)  
Fig. 6. a Experiment Set 4—relative performance of Ž . R<sup>s</sup>B for five L-value choices. b Experiment Set 4—relative performance of Ž . R<sup>s</sup>O for the same five L-value choices.

We terminate the preliminary investigations of our simple agent model with a set of experiments Ž . Set 5 where we observe its performance against groups of opponents. The capacity to adapt against opponent groups is of interest in situations like that described in Section 1 involving a buyer agent that must deal with multiple broker agents each of whom represent multiple sellers.

## 4.5. Experiment Set 5

In Set 5, an LCS plays against sets of multiple opponents simultaneously. Except for the number of opponents, all parameters are as in Set $2 \left( \mathrm { i . e . , } n = 5 , \right.$ $R = B , ~ L = 1 1 )$ . We arbitrarily picked LCS 2 for this preliminary exploration. Set 5 contains four experimental subsets. One subset allowed the LCS to simultaneously play all Fixed strategies i.e., CCC,Ž DDD, and RAND . Another pits the LCS against all. of the TFT Variants i.e., TFT, TFTT, TTFT, GTFT,Ž and JOSS . The third and fourth subsets allow the. LCS to tackle all of the Nicer opponents i.e., RAND, Ž CCC, TFTT, and GTFT and the More Hostile oppo-. nents i.e., DDD, TFT, TTFT, FRDM, and JOSS ,Ž . respectively.

Fig. 7 shows the results of each tournament. The curves labeled Fixed, TFT Variants, Nicer, and More Hostile, show LCS 2’s relative earnings against each class of opponent over the 50 games. Unlike earlier experiments, here the LCS plays against all of the opponents in a set in round-robin fashion, beginning with a randomly selected opponent. Thus, in any game, the $\mathrm { L C S ^ { \circ } s }$ earnings are the result of 200 moves whereas each opponent’s earnings are based on a smaller number of moves, depending on the number of opponents in the set. Consequently, we cumulate all opponents’ earnings in a game to obtain a single dollar figure for the opponent set. The LCS’s and the cumulated opponent earnings are averaged and the plots depict, as in Figs. 3–5, the amount by which the LCS betters this average i.e.,Ž the relative earnings by the LCS . Overall, we see . from Fig. 7 that LCS 2 performs best against the Fixed group followed by the Nicer, TFT Variants and More Hostile categories, in that order.

![](/api/attachments/F75BMBVJ/fulltext/images/be96f2335f51332adc911c26cebe187e3f0f7bb8e2271008cb1cadb0670fb528.jpg)  
Fig. 7. Experiment Set 5—LCS 2’s relative performance against various opponent groups.  
GAME, G

Table 6 shows LCS 2’s cumulative relative earnings across all 50 games i.e.,Ž ASum-All 50B in row 1 against each opponent group. It also presents other. characteristics of each group, namely: the number of members comprising the group; which members are Predictable and which are not; which are Fixed opponents and which are Reactive; which are Nicer and which are More Hostile; and which memory model Ž . R<sup>s</sup>B or R<sup>s</sup>O was the preferred model against each group member in our experiments fromŽ Table 5 ..

## 4.5.1. Contrasting group performances with indiÕidual performances

If we compare the Sum-All 50 value for a group Ž . in Table 6 with the corresponding quantity for each individual member of that group shown in Table 2 ,Ž . we see that the former is smaller than the latter in all cases with one exception. The earnings of <sup>y</sup>944.13 against DDD is much smaller than the earnings of 3347.95 for the Fixed group of which DDD is a Ž member ..

One would generally expect adaptation against an individual opponent to be more successful than that against a composite opponent i.e., an opponent made Ž up of multiple opponents as the latter’s behavior is. likely to exhibit more variation. However, the exception that occurs with DDD underscores the fact that the makeup of the opponent set—i.e., its membership—also plays a key role. As we know, against DDD, the best that the LCS can hope for is mutual defection as getting suckered is the only other choice. Thus, the Sum-All 50 score is bound to be non-positive and very likely negative against DDD given that some period is likely to elapse before an LCS learns that sustained defection is the best thing to do.

Consider the Fixed category next. Because Fixed contains two other opponents, the LCS has only one-third as many encounters with DDD when playing against Fixed as when playing against DDD alone. Suppose the LCS evolves to a state of sustained defection. In this event, each encounter with CCC results in the latter being suckered, each encounter with DDD results in mutual defection asŽ when playing DDD in isolation , and encounters . with RAND result in mutual defection or RAND being suckered, with a 50-50 likelihood. Thus, the Sum-All 50 against Fixed is bound to be greater than that against DDD alone. Likewise, even if an LCS evolves to a state of sustained cooperation, its performance against Fixed will be better than its performance against DDD. It follows, therefore, that for any other behavior by the LCS i.e., some combina-Ž tion of cooperate and defect , the LCS’s performance. against DDD will be worse than that against Fixed. Thus, apart from opponent set size, opponent set makeup has significant impact on an LCS’s relative performance.

Table 5  
Which memory model does better?

<table><tr><td>TTFT</td><td>DDD</td><td>FRDM</td><td>CCC</td><td>TFT</td><td>GTFT</td><td>RAND</td><td>TFTT</td><td>JOSS</td></tr><tr><td>-263.27%</td><td>-79.15%</td><td>-40.23%</td><td>-18.41%</td><td>+2.89%</td><td>+5.28%</td><td>+10.72%</td><td>+11.30%</td><td>+19.03%</td></tr><tr><td>B</td><td>B</td><td>B</td><td>B</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td></tr><tr><td>H</td><td>H</td><td>H</td><td>N</td><td>H</td><td>N</td><td>N</td><td>N</td><td>H</td></tr><tr><td>RE</td><td>FX</td><td>RE</td><td>FX</td><td>RE</td><td>RE</td><td>FX</td><td>RE</td><td>RE</td></tr><tr><td>P</td><td>P</td><td>P</td><td>P</td><td>P</td><td>U</td><td>U</td><td>P</td><td>U</td></tr></table>

N: Nicer opponent; H: More Hostile opponent; RE: Reactive opponent; FX: Fixed opponent; B: the R<sup>s</sup>B memory model is better; O: the R<sup>s</sup>O memory model is better; P<sup>s</sup>Predictable opponent; U<sup>s</sup>Unpredictable opponent.

Table 6  
Relative performance of LCS 2 and opponent group characteristics

<table><tr><td></td><td>Fixed</td><td>Nicer</td><td>TFT Variants</td><td>More Hostile</td></tr><tr><td>Sum-All 50</td><td>3347.95</td><td>2347.27</td><td>-16,003.84</td><td>-21,868.89</td></tr><tr><td>No. of members</td><td>3</td><td>4</td><td>5</td><td>5</td></tr><tr><td>Predictable members</td><td>CCC, DDD</td><td>CCC, TFTT</td><td>TFTT, TFT, TTFT</td><td>TFT, TTFT, DDD, FRDM</td></tr><tr><td>Unpredictable members</td><td>RAND</td><td>RAND, GTFT</td><td>GTFT, JOSS</td><td>JOSS</td></tr><tr><td>Fixed members</td><td>ALL</td><td>CCC,RAND</td><td>NONE</td><td>DDD</td></tr><tr><td>Reactive members</td><td>NONE</td><td>TFTT, GTFT</td><td>ALL</td><td>TFT, JOSS, TTFT, FRDM</td></tr><tr><td>Nicer members</td><td>CCC, RAND</td><td>ALL</td><td>TFTT, GTFT</td><td>NONE</td></tr><tr><td>More Hostile members</td><td>DDD</td><td>NONE</td><td>TFT, JOSS, TTFT</td><td>ALL</td></tr><tr><td>R = B preferred with:</td><td>CCC, DDD</td><td>CCC</td><td>TTFT</td><td>TTFT, DDD, FRDM</td></tr><tr><td>R = O preferred with:</td><td>RAND</td><td>RAND, TFTT, GTFT</td><td>GTFT, TFT, JOSS, TTFT</td><td>TFT, JOSS</td></tr></table>

## 4.5.2. Contrasting group performances with one another

When contrasting group performances against one another, it is difficult to offer straightforward rationalizations like we just did in the preceding section when contrasting performances against Fixed and DDD. So also, we are unable to draw any conclusions by perusing characteristics like member predictability, reactivity, nicety or preference for R<sup>s</sup>B Ž . i.e., LCS 2 that are shown in Table 6. The picture that does emerge from Table 6 and Fig. 7 is one that we pointed out when contrasting group and individual performances in the preceding section. That is, one would expect the LCS to do better against an opponent with fewer members than against one with more, with the understanding that exceptions due to the makeup of an opponent group do occur.

Thus, we see that the LCS does best against Fixed Ž . Ž membership size of 3 , followed by Nicer membership size of 4 followed by TFT Variants and More. Hostile both having five members . In the latter case Ž . where both opponents have the same membership size 5 , we look to their makeup for possible an- Ž . swers. We see that both TFT Variants and More Hostile sets share three members. The remaining two members in the former category i.e., TFTT andŽ GTFT are more LCS-friendly than those in the latter. Ž . i.e., DDD and FRDM . However, these conclusions are as yet conjectures and may be unique to the particular opponent groupings and LCS design considered. Further investigations are ongoing.

Finally, in two of the four cases—TFT Variants and More Hostile—the LCS shows early growth but stabilizes at game-playing states where it loses to its opponents. Recall that we arbitrarily picked LCS2 for this experiment—it was not particularly designed for such i.e., opponent group tournaments. We Ž . believe that modifying the LCS’s design should result in better performance than that seen in Fig. 7 and are examining alternate designs.

## 5. Concluding remarks

In many environments, including the Internet and the WWW, increasing attention is being paid to making things more user-friendly and efficient through automation. A tool that is being widely researched and deployed is the artificial agent. Past research has focused on developing single agent and multi-agent systems agencies for particular prob- Ž . lem contexts and where agent behavior is pre-conceived and fully defined.

Our focus in this paper, instead, has been on examining the evolutionary behavior of adaptive agents, called AsimpleB agents that are equipped with potentially perennially incomplete and imperfect knowledge bases. We use the Learning Classifier System LCS computational paradigm to construct Ž . these simple adaptive agents. Rather than conduct our investigations in a particular problem context, we adopt a very generic setting involving the Iterated Prisoner’s Dilemma IPD . Within this generic set- Ž . ting, we deploy our agents against one or more AopponentB agents playing pre-defined i.e., non- Ž adaptive strategies. The agents begin operating . without any prior knowledge about an opponent’s operational strategy and, to be more effective, must acquire this knowledge over time. While the generic setting offers some assurance of generalizability of our findings, our work has several real-world application potentials. One such instance that we discuss in Section 1 is that involving buyer, seller, and broker agents in an artificial agency for trading in real estate property.

We report on five initial sets of experiments that are part of our ongoing investigations into the simple agent paradigm. In Set 1, we develop an initial AbaseB case of our agent and deploy it against nine different opponent types with varying degrees of success. Based on what we learn, we deploy two other, more refined agents against the same nine opponents in experiment sets 2 and 3, and see tremendous performance improvements. We then contrast the performances of these two agents against the nine opponents to see what agent features work better against what opponent types. This exercise reaffirms that neither of the models examined would be adequate against all nine opponents. It also leads us to articulate other potentially useful models including one that embodies multiple other simple agents i.e., aŽ . Amulti-memoryB model .

In Set 4, we conduct a limited exploration of the impact of memory size and content on agent performance by pitting the two agent models from sets 2 and 3 against a single opponent. This opponent is the best-known human-developed strategy for playing the IPD game, called Tit-for-Tat. Our examination reveals that arbitrarily increasing memory size is not advisable both due to increasingly diminishing returns and the possibility of performance deterioration beyond some threshold value—i.e., being more informed is not necessarily being better informed even in an artificial world. In the final set, we pit the agent from Set 2 an arbitrary choice against four Ž . different opponent groups i.e., a collection of two or Ž more opponents . Our group size ranged from three. to five. The adaptive task an agent faces in the opponent group scenario is tougher than that when dealing with a single opponent at a time. We see that the number of members in the group and some of their characteristics influence the agent’s performance against a given opponent group.

Our experimental findings reveal that the LCSbased simple agent paradigm postulated in this paper is worthy of further research scrutiny. We outline a number of areas for more in-depth investigations and are currently investigating several of these.

## Acknowledgements

The authors extend their grateful thanks to an Area Editor and reviewers for their critical review of an earlier draft.

## Appendix A

A GA 9,10 is a procedure for knowledge refine-<sup>w</sup> <sup>x</sup> ment that draws on the Darwinian principle of natural evolution. Species evolve in nature through processes of sexual and asexual reproduction. Reproductive activity is guided in part by a desire to cope with the environment and to ensure survival of the species. The philosophy behind a GA is that similar ideas may be applied to knowledge refinement. Existing knowledge pieces are used to generate new knowledge through using genetic AoperatorsB called crossover and mutation for sexual and asexual re-Ž production, respectively . These operators serve to. recombine and perturb Abuilding blocksB resident in current knowledge fragments to assemble new knowledge fragments through a process of genetic trial and error.

During this process, existing fragments are selected to act as procreators based on their Afitness,B and are subjected to probabilistic mutation and crossover. The net result is the creation of offspring generated through crossover alone, mutation alone, both crossover and mutation, or neither i.e., off- Ž spring are replicas of the parents . Eventually, the . hope is that one would be left with a knowledge base that is much more appropriate for dealing with the environment in question than the initial state.

## References

<sup>w</sup> <sup>x</sup> 1 R. Axelrod, The evolution of strategies in the iterated prisoner’s dilemma, in: L. Davis Ed. , Genetic Algorithms andŽ . Simulated Annealing, Pittman, London, 1987, pp. 32–41.

<sup>w</sup> <sup>x</sup> 2 L.B. Booker, D.E. Goldberg, J.H. Holland, Classifier systems and genetic algorithms, Artificial Intelligence 40 1989 235–Ž . 282.

<sup>w</sup> <sup>x</sup> 3 Communications of the ACM: Special Issue on Intelligent Agents, 37, No. 7 July 1994 . Ž .

<sup>w</sup> <sup>x</sup> 4 Communications of the ACM: Special Issue on Multiagent Systems on the Net and Agents in Ecommerce, 42, No. 3 Ž . March 1999 .

<sup>w</sup> <sup>x</sup> 5 L. Davis, Adapting operator probabilities in genetic algorithms, in: J.D. Schaffer Ed. , Proceedings of the ThirdŽ . International Conference on Genetic Algorithms, Morgan Kaufmann, San Mateo, CA, 1989, pp. 61–69.

<sup>w</sup> <sup>x</sup> 6 Decision Support Systems: Special Issue on Software Agents in Digital Community, 28, No. 3 May 2000 .Ž .

<sup>w</sup> <sup>x</sup> 7 Decision Support Systems: Special Issue on Intelligent Agents and Pricing in Electronic Commerce, 28, No. 4 June 2000 .Ž .

<sup>w</sup> <sup>x</sup> 8 K.A. DeJong, An Analysis of the Behavior of a Class of Genetic Adaptive Systems, unpublished doctoral dissertation, Department of Computer Science, University of Michigan, 1975.

<sup>w</sup> <sup>x</sup> 9 S. Forrest, Genetic algorithms: principles of natural selection applied to computation, Science 261 1993 872–878 August Ž . Ž 13 ..

<sup>w</sup> <sup>x</sup> 10 D.E. Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning, Addison Wesley, Reading, MA, 1989.

<sup>w</sup> <sup>x</sup> 11 J.J. Grefenstette, Optimization of control parameters for genetic algorithms, IEEE Transactions on Systems, Man, and Cybernetics 16 1 1986 122–128.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 Z. Michalewicz, Genetic Algorithms<sup>q</sup>Data Structures<sup>s</sup> Evolution Programs, 2nd Extended Edition, Springer Verlag.

<sup>w</sup> <sup>x</sup> 13 M. Mitchell, An Introduction to Genetic Algorithms, MIT Press, Cambridge, MA, 1996.

<sup>w</sup> <sup>x</sup> 14 R. Pakath, J. Zaveri, Specifying critical inputs in a genetic algorithm-driven decision support system: an automated facility, Decision Sciences 26 6 1995 749–779.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 J.D. Schaffer, R.A. Caruana, L.J. Eshelman, R. Das, A study of control parameters affecting online performance of genetic algorithms for function optimization, in: J.D. Schaffer Ed. ,Ž . Proceedings of the Third International Conference on Genetic Algorithms, Morgan Kauffman, San Mateo, CA, 1989, pp. 51–60.

<sup>w</sup> <sup>x</sup> 16 M. Srinivas, L.M. Patnaik, Adaptive probabilities of crossover and mutation in genetic algorithms, IEEE Transactions on Systems, Man, and Cybernetics 24 4 1994 656–667.Ž . Ž .

![](/api/attachments/F75BMBVJ/fulltext/images/c9367484acd227e4f051899e3b1e1e5094997a0be05a1d0d681d28d270dc5b14.jpg)  
Chen-Lu Meng is Executive Director of Information Architecture at MassHysteria, a major Web-based application services provider at San Diego, CA. He received his BS Industrial Design de-Ž . gree from the National Cheng-Kung University, Taiwan, his MS Computer Ž Science degree from the University of. Kentucky, and has completed all doctoral-level course requirements in Decision Science and Information Systems at the University of Kentucky.

![](/api/attachments/F75BMBVJ/fulltext/images/88701ce9b3838bf99bb4118a2118f7a11c11d031e5dd070e88142152b460e739.jpg)

Ramakrishnan Pakath is Associate Professor of Decision Science and Information Systems at the University of Kentucky. Ram holds a MSE OR andŽ IE degree from The University of Texas. at Austin and a PhD Management—Ž MIS degree from Purdue University.. His research focuses on a designing Ž . and evaluating adaptive problem processors, and b assessing information Ž . source impacts on system user performance. Ram’s research articles have ap-

peared in such forums as Decision Sciences, Decision Support Systems, European Journal of Operational Research, IEEE Transactions on Systems, Man, and Cybernetics, Information and Management, and Information Systems Research. He is author of the book Business Support Systems: An Introduction published by Copley, now in its second edition. Ram has also contributed refereed material to a number of well-known books including Handbook of Industrial Engineering, Multimedia Technology and Applications, and Operations Research and Artificial Intelligence. Ram served as Director of the MIS Research Laboratory of the College of Business and Economics, University of Kentucky, from 1993 to 1997. He is an Associate Editor for Decision Support Systems and an Editorial Board Member of Journal of End User Computing and Management.
