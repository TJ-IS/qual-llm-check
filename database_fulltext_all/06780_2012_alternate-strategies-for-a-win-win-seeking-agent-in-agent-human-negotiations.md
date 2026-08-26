---
otero_id: 6780
otero_key: "GHK8X435"
title: "Alternate Strategies for a Win-Win Seeking Agent in Agent-Human Negotiations"
authors: "Yinping Yang; Sharad Singhal; Yunjie Xu"
year: "2012"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222290307"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Alternate Strategies for a Win-Win Seeking Agent in Agent–Human Negotiations

Yinp g Yan g, Sha rad Sin gha l, and Yun jie (Ca lvin ) Xu

Yinping Yang is a scientist and an independent investigator at the Institute of High Performance Computing, Agency for Science, Technology and Research (A\*STAR), Singapore. She is also affiliated with the School of Information Systems, Singapore Management University as an adjunct assistant professor. She received her Ph.D. in information systems from the National University of Singapore. Her research interests include electronic negotiation systems, e-commerce technologies, social networking services, and economics of cloud computing. Her research has been published in Behaviour & Information Technology, Journal of Global Information Management, International Conference in Information Systems, Meetings on Group Decision and Negotiation, and proceedings of international conferences. Her research received a Best Paper Award at Hawaii International Conference on System Sciences in 2009, and a Best Prototype Award and a Best Paper Award at the Annual Workshop in Information Technologies and Systems in 2009 and 2006, respectively. She currently serves as an area editor for Electronic Commerce Research and Applications.

Sharad Singhal is a distinguished technologist at Hewlett-Packard Laboratories, where he has led teams that have developed techniques for monitoring and managing service-level agreements; methods for controlling service quality in multi-tier applications, resource allocation, and assignment algorithms; as well as architectures for management of large-scale data centers and cloud computing. He received his B.Tech. from the Indian Institute of Technology, Kanpur, and his M.S. and Ph.D. from Yale University. His current research interests include application of control theory to systems management, policy-based system management, and large-scale data center management architectures. He received the 2003 Joel S. Birnbaum prize for innovation at HP, and the Harding Bliss prize for his graduate work at Yale University. Dr. Singhal holds 29 patents and has published over 100 papers in a variety of refereed journals and conferences. He is a member of the IEEE and the Acoustical Society of America.

Yunjie (Calvin) Xu is an associate professor of information systems at the School of Management, Fudan University, Shanghai, China. He received his Ph.D. in management information systems from Syracuse University. Before joining Fudan, he was an assistant professor at the National University of Singapore. His research interests cover electronic commerce, knowledge management, online social network analysis, and information-seeking behavior. His research publication appeared in Journal of Management Information Systems, Journal of the Association for Information Systems, Journal of the American Society for Information Science and Technology, IEEE Transactions on Professional Communication, Communications of the ACM, International Journal of Electronic Commerce, Journal of Retailing, and other journals.

Abs trac t: With the growth of e-commerce and e-markets, there is an increasing potential for the use of software agents to negotiate business tasks with human negotiators. Guided by design science methodology, this research prescribes and validates a win-win seeking negotiation agent using strategies of “simultaneous-equivalent offers” and “delayed acceptance” and compares their effects against the use of conventional sequential-single offer and immediate acceptance strategies. To evaluate the alternate strategies, a negotiation agent system was implemented and an experiment was conducted in which 110 agent–human dyads negotiated over a four-issue online purchase task. Our results indicate that the proposed agent strategies can enhance the economic performance of the negotiated outcome (counterpart agreement ratio, individual utility, joint utility, and the distance to Pareto-efficient frontier) and maintain the human counterparts’ positive perceptions toward the outcome and the agent. The findings confirm the efficacy of the proposed design and showcase an innovative system to facilitate e-commerce transactions.

Key words and phras es : agent–human negotiation, delayed acceptance, design science, electronic markets, negotiation agent, simultaneous-equivalent offers, win-win negotiation.

Many c om panies have link ed Web s ales c hannels to their supply chain systems for selling products and services online. Currently, online sales take two dominant forms. For low-value or standardized purchases such as personal computers, customers can make purchases online at fixed prices. For high-value purchases such as the purchase of enterprise computer servers, customers can view the basic product information on the Web site and then contact a salespeople to negotiate the actual purchase. The human-operated sales mode enables customization but is inherently labor intensive, expensive, and not easily scalable. Like high-end customers, small and midrange customers such as a small start-up company may also want to customize their purchases through negotiation. In current Web sales channels, however, they are often forced into standard deals, as the value of their purchases is not high enough to merit the involvement of salespeople.

In today’s e-commerce practice, despite the adoption of a number of interactive Web-based technologies, each has its respective limitations to meet the need for mass customization [58]. Sites such as eBay.com allow for auction-based price discovery<sup>1</sup> but not for product configuration. Dell provides instant configuration tools<sup>2</sup> to enable customers to customize their purchase of computers, but does not allow negotiation on price, quantity, and warranty terms together. Online intermediaries such as Alibaba. com provide instant messaging tools<sup>3</sup> to facilitate communication between sellers and buyers, but human involvement in negotiation is still required. An intelligent software agent that is capable of negotiating for and with e-commerce decision makers can potentially fill this gap left by existing technologies.

In the traditional sense, negotiation is very much a complex human enterprise that is common in the social and business world [13]. Research into real-world negotiations has consistently established that humans are often inefficient and ineffective in reaching optimal outcomes due to socioemotional obstacles, cognitive biases, and limited information processing capacity and capability [15, 34]. This has motivated the design of negotiation support systems (NSSs) to help human negotiators in reaching better outcomes using computerized decision support and communication support tools [9, 28, 42, 56]. While NSSs enable negotiators to reach better outcomes, the negotiation process is still steered by human negotiators.

To free human negotiators and to scale for demand in the e-market, in automated negotiations, or agent-based negotiations, software agents are designed to act as autonomous surrogates on behalf of human decision makers [23, 29]. In comparison to human negotiators, software agents provide potential benefits to the e-market including reduced cost associated with human operation, more efficient settlements, and fewer socioemotional problems based on rational decision making [35, 43]. Therefore, agents offer opportunities to turn conventional e-market transactions into negotiated transactions in an automated, cost-efficient manner. Many artificial intelligence techniques have been developed for the design of agent-based negotiation strategies, such as heuristics models [11], genetic algorithms [35], Bayesian models [26, 57], and estimation algorithms for multi-issue trade-off [4, 12].

Several important dimensions have received limited attention in existing research in agent-based negotiations, however. First, past studies primarily focus on an agent– agent negotiation context [23], while there is little research on agent–human negotiations [29]. Systematic design and evaluation of agent strategies that incorporate a human counterpart’s perspective is lacking. Second, existing agent designs often make assumptions about the availability of the counterpart’s preferences [12] or the availability of past negotiation history [26, 35, 57]. In e-commerce settings, however, agents have to frequently deal with new customers and these assumptions are not always met. Third, existing studies focus on how to make offers (e.g., [12, 26]) but rarely explore alternate strategies on how to respond to counteroffers. A complete agent negotiation strategy requires a better design of both offer and acceptance strategies.

This paper proposes the design of a win-win seeking negotiation agent with a new offer strategy (simultaneous-equivalent offers) and a new acceptance strategy (delayed acceptance) to be useful for agent–human negotiations. According to Walls et al. [52], a design theory requires clear identification of meta-requirement, meta-design, kernel theories, testable design hypotheses, and evaluation. Hevner et al. [21] provide seven design research guidelines, addressing the purpose of an artifact, problem domain relevance, design evaluation, research novelty, research rigor, design as a search process, and research communication to tech-oriented as well as behavior-oriented audiences. More recently, Peffers et al. [37] suggested six design research activities, including problem identification and motivation, definition of the objectives, design and development, demonstration, evaluation, and communication.

Following the design science guidelines [21, 37], we first define the problem scope for the design in order to qualify its application domain. We then present the design objective of a win-win seeking negotiation agent and identify the key components required by a design theory [52]. In comparison to alternate designs, the core design features of the simultaneous-equivalent offers strategy and the delayed acceptance strategy are described and their effects are hypothesized. A system prototype is implemented and an evaluation of the design is conducted with an experimental study. Finally, we discuss the implications of the findings from the perspectives of the negotiation theory, the design science, and the e-commerce practice.

## Problem Scope

Negotiation is a joint dec is ion-m ak ing proc es by two or more parties with conflicting interests to reach an outcome. As negotiations involve many facets and settings, it is useful to clearly define our problem scope. Essentially, this research examines an agent–human negotiation setting in which a software negotiator and a human negotiator dyad negotiates over multiple issues based on an alternate offer protocol for a non-repeated negotiation.

First, prior to negotiation, parties are assumed to have common information about the negotiation task, including the issues of interest and the value options of the issues. In addition, parties have private information about their own preferences and bottom-line conditions.<sup>4</sup> As widely accepted in the negotiation analysis literature, each party’s preferences are quantitatively captured by a multi-attribute utility function [5, 40, 41]. Each party’s bottom-line condition is represented by the best alternative to a negotiated agreement (BATNA), which is a fallback deal with a third party if the current negotiation fails [13, 40].

Second, the negotiation assumes that both parties follow rules that govern their interaction.<sup>5</sup> The rules are based on a bilateral alternate offer protocol [45] in which negotiation proceeds in rounds, and parties take alternate turns to make offers in each round. All the offers are assumed to be nonretractable. An unaccepted offer expires when the next round starts. In addition, the rules include a termination mechanism by allowing each party to indicate if an offer is a “final offer.” The round at which a negotiator makes a final offer is unknown to his or her counterpart a priori. The counterpart can only accept a final offer or reject it with a final counteroffer. The negotiation terminates with an agreement if one party accepts the other’s offer or terminates with a nonagreement if a party rejects a final offer/counteroffer. The parties are not allowed to restart the negotiation, and the case of repeated negotiation is beyond the scope of this research.

Third, this paper examines negotiations over multiple issues of interest. Single-issue negotiation such as price bargaining is often a zero-sum, distributive [53], and “winlose” game as parties often have almost strictly opposing interests on that issue [40]. But in multi-issue negotiation, for example, when negotiating price, quantity, and warranty terms together, negotiation can be non-zero-sum, integrative [53], and “win-win”

Table 1. Components of the Design of a Win-Win Seeking Negotiation Agent

<table><tr><td>Components of a design theory [52]</td><td>Components of the proposed negotiation agent design</td></tr><tr><td>1. Kernel theory</td><td>Dual concern model</td></tr><tr><td rowspan="2">2. Meta-requirements</td><td>A win-win seeking negotiating agent (1) to achieve better economic outcomes for itself and (2) to achieve better economic and social-psychological outcomes for its human counterpart (3) within a reasonable number of rounds</td></tr><tr><td>Evaluation metrics that incorporate negotiation outcomes from both economic and social-psychological perspectives: counterpart agreement ratio, individual outcome, dyadic outcome, counterpart&#x27;s perception of the outcome, and counterpart&#x27;s perception of the agent</td></tr><tr><td>3. Meta-design</td><td>Two major design features, i.e., an offer strategy and an acceptance strategy, to comprise a complete negotiation strategy</td></tr><tr><td>4. Testable design product and hypotheses</td><td>An agent artifact that embodies two new strategies, i.e., the simultaneous-equivalent offers and delayed acceptance strategies, are more likely to produce better economic and social-psychological outcomes in comparison to sequential-single offer and immediate acceptance strategies</td></tr></table>

because parties have room to trade off their preferences over the issues and achieve better-for-all outcomes without forcing one side to lose [40].

## The Design of a Win-Win Seeking Negotiation Agent

Us ing Walls et al.’s m odel [52], we propose a design theory of a win-win seeking negotiation agent to be used in the above-defined problem scope. Employing the dual concern model as our kernel theory, we describe the meta-requirements of a negotiation agent that seeks to achieve desirable outcomes for both parties. We next present a meta-design that comprises an offer strategy and an acceptance strategy, and describe the simultaneous-equivalent offers and the delayed acceptance as part of our testable design product. Table 1 presents an overview of the design.

## Kernel Theory and Meta-Requirements

A design objective, or the goal that a class of design artifacts needs to pursue, should be motivated by natural or social theories, which serve as kernel theories [52]. Our high-level design objective is to create the theoretical and technical basis for a winwin seeking agent in agent–human negotiation settings.

To guide our design, we refer to the negotiation literature to understand the basic rationale behind one’s strategic choices in the presence of a conflict of interests. The dual concern model [44, 46] suggests that one’s strategy is determined by the balance between two concerns: the importance given to the negotiation outcomes for oneself and the importance given to the outcomes for the counterpart. The model results in four types of general negotiation strategies: avoidance, accommodation, competition, and collaboration [46]. An avoidance strategy implies a concern for neither party. An accommodation combines low concern for self with a high concern for the counterpart. A competition strategy is a combination of high concern for self and a low concern for the counterpart. A collaboration strategy requires and reflects a strong concern for both parties. The dual concern model predicts that a negotiator should adopt a collaboration [46] or problem-solving [44] strategy when the objective of negotiation is the establishment of a mutually beneficial agreement for both parties, which is consistent with contemporary negotiation literature that advocates the achievement of a “win-win” negotiation [32, 33, 40, 53].

Based on the dual concern model, the specific meta-requirements [52] of a winwin seeking agent are (1) to achieve better economic outcomes for itself and (2) to achieve better economic and social-psychological outcomes for its human counterpart. In the agent–human negotiation setting, as human counterparts are less likely to be engaged in prolonged negotiations, a third meta-requirement is that the agent should be designed to reach better socioeconomic agreements within a reasonable number of rounds. The human counterpart is, however, not assumed to be reciprocally seeking win-win outcomes.

## Evaluation Metrics for Negotiation

To translate the meta-requirements into measureable evaluation metrics in the negotiation context, we consider two broad perspectives in the negotiation literature: the economic perspective and the social-psychological perspective [48]. Contemporary economic models of negotiation focus on the prediction of optimal joint outcomes that should emerge from rational actions [32, 33, 45]. In terms of evaluating the outcomes, economists, game theorists, and applied mathematicians often analyze the “utility”—an economic sense of satisfaction—that is received by each negotiator from the agreement. The individual outcome is reflected as the extent to which the utility of an individual negotiator approaches an optimal value. For example, a buyer utility denotes the utility received by a buyer from the negotiated agreement.

The joint outcome (or dyadic outcome for a two-party negotiation) is the extent to which the parties’ payoffs approach a set of optimal values. Dyadic outcomes are often measured by joint utility (e.g., the simple sum of individual utilities [9, 15, 18]) or by Pareto efficiency (e.g., the distance of the agreement from the set of Pareto-efficient solutions, where a Pareto-efficient solution is the locus of optimal outcomes beyond which no additional joint gain is possible [18, 28]) (see [51] for a review of dyadic outcomes measures). Nash [32, 33] integrated the notion of fairness into the Pareto standard and defined an optimal negotiation outcome that later came to be known as the Nash solution. When distributional fairness between the buyer and the seller is considered, the distance to the Nash solution (e.g., [18, 28]) and contract balance (e.g., [9, 15]) have also been used in experimental negotiation literature. Figure 1 shows the related concepts.

![](/api/attachments/GHK8X435/fulltext/images/f91498699de5181f0ea7469c838281d157f92db81f497772e34053859598d35b.jpg)  
Figure 1. Buyer–Seller Utility Graph in a Multi-Issue Negotiation

Because not all negotiations lead to mutual agreements, it is important to consider the agreement ratio (or inversely, the impasse ratio, see [51]) on top of the utility measures of the negotiation outcomes. Finally, other metrics being equal, it is desir able to shorten the negotiation time or rounds to reach an agreement.

Compared to the economic models, sociologists, psychologists, and organization theorists have developed more descriptive theories and provided evidence that realworld negotiators are susceptible to cognitive limitations, cognitive biases, and socioemotional problems, and thus often deviate from rational behavior [27, 38]. The social-psychological perspective holds that what matters most in negotiations are the feelings and perceptions of the negotiators toward the negotiation process and outcomes [50]. Studies have looked into measures of negotiators’ perceptions of the negotiation (e.g., satisfaction with the outcome, judgments of the fairness of the procedure), perceptions of the other party (e.g., trait inferences such as the counterpart’s expertise and cooperativeness), and perceptions of the self (e.g., judgment of one’s own competency) (for a review of social-psychological negotiation measures, see [8, 50]).

While economic outcomes have received most of the attention in prior agent-based negotiation research [4, 11, 12, 26, 35, 57], the social-psychological perspective associated with the participation of human negotiators [29] is often ignored. In the agent–human negotiation setting, we envisage that an integrated metrics comprising both economic and social-psychological perspectives is necessary to guide and evaluate the design of agent strategies. Specifically, we include the counterpart agreement ratio, the individual outcome, the Pareto efficiency of the dyadic outcome, and the human counterpart’s perceptions of the outcome and of the agent as the evaluation metrics of the agent design.

## Meta-Design, Testable Design Product, and Hypotheses

Under the protocol of bilateral alternate offers [45], a negotiator has two important strategic decisions: how to make offers and how to respond to counteroffers. Correspondingly, an offer strategy should specify the plan associated with making offers, including the amount and timing of the initial offer, the concessions of subsequent offers, as well as the amount and timing of the final offer. An acceptance strategy should specify the plan associated with accepting a counteroffer. Our proposed metadesign [52] includes an offer strategy and an acceptance strategy that comprises a complete negotiation strategy for a negotiation agent. The ensuing sections elaborate on the strategy designs and hypotheses.

## Design of Offer Strategy and Hypotheses

Both the human- and agent-based negotiation literature recommends that a negotiator should set a high aspiration by starting with an offer of high self-utility and conceding in certain patterns. This baseline strategy is a sequential-single offer (SEQ) strategy. Research suggests that negotiators who start with tough offers can create an effective anchor [16] in a negotiation and gain better settlements than do those who make low or modest opening offers [6, 39, 54]. However, from a social-psychological perspective, by displaying an “attitude of toughness” [27, p. 48], the agent signals a high concern for itself and a low concern for the counterpart, and thus runs the risk of souring the relationship or of even not being able to close a deal.

In a multi-issue negotiation, however, multiple offers that have the same utility for one party but may have different utilities for the counterpart can be constructed [40, 41]. For example, a tailor can send two package offers to a client: \$135 for a suit delivered in three days or \$100 for a suit delivered in two weeks. Both offers are equal from the tailor’s perspective, but may appeal to the client, who might place greater importance on either the price or the delivery time. Based on this concept, social psychology research has proposed a negotiation method referred to as multiple equivalent simultaneous offers [22, 31]. Experimental research suggests that human-operated multiple equivalent simultaneous offers can produce better dyadic outcomes and higher negotiator satisfaction [31]. Nevertheless, an agent-operated strategy design that incorporates this concept has yet to be formalized and empirically examined.

Our design of a simultaneous-equivalent offers (SIM) strategy enables a negotiation agent to send the counterpart multiple offers in each round using the following key steps. First, offer candidates with equal or similar utility to the agent are selected based on its utility function. Second, as there can be numerous offers with equivalent utilities to the agent, these offer candidates are further selected with an “offer selection method” such that each offer favors one of the negotiation issues that matter to the counterpart. Thus, by making equivalent offers simultaneously in each round, the agent communicates a high concern for the counterpart [41] by increasing the likelihood that its offers appeal to the counterpart. The counterpart, when facing the simultaneous offers, can evaluate based on his or her private preferences and determine his or her utilities to these multiple offers accordingly. Consequently, in each round there is a higher chance that the counterpart accepts the offer with the highest utility among multiple choices as compared to the situation when he or she is presented with a single offer. Therefore, over the negotiation rounds, the overall counterpart acceptance ratio and the counterpart utility are more likely to be enhanced.

Hypothesis 1: A human counterpart is more likely to accept an offer from an agent that makes simultaneous-equivalent offers than from one that makes sequentialsingle offers.

Hypothesis 2: A human counterpart is more likely to obtain a better individual outcome after negotiating with an agent that makes simultaneous-equivalent offers than with one that makes sequential-single offers.

By making multiple offers with equivalent utility in each round, the agent can still maintain a high concern for itself (e.g., by starting from a high initial utility). Therefore, by increasing the counterpart’s utility while maintaining the agent’s utility, the SIM strategy can also help to achieve greater outcome efficiency for the agent–human dyad:

Hypothesis 3: The agent–human dyad is more likely to obtain an efficient dyadic outcome when the agent makes simultaneous-equivalent offers than when it makes sequential-single offers.

A negotiator’s satisfaction with the outcome is one of the most important socialpsychological measures of negotiation outcomes [9, 28, 36, 42]. We expect that the SIM strategy can make the counterpart experience a higher outcome satisfaction via two routes. First, as predicted in H2, simultaneous-equivalent offers enable the counterpart to achieve higher utility. Thus, a rational negotiator is more likely to feel satisfied if the outcome is associated with higher utility. Second, cognitive psychology studies indicate that a human decision maker has a tendency to assign more positive attributes to a choice he or she has made after the event of choosing (“choice-supportive bias”) [20, 30]. When the agent adopts the SIM strategy, more agreements are expected to be obtained via the human counterparts’ acceptance (H1). Accordingly, based on the choice-supportive bias, the counterparts’ evaluation of the outcome is likely to be positively reinforced. Therefore, we hypothesize:

Hypothesis 4: A human counterpart is more likely to feel satisfied with the outcome after negotiating with an agent that makes simultaneous-equivalent offers than with one that makes sequential-single offers.

In buyer–seller relationships, a critical social perception is the degree of cooperativeness that one develops toward the other party [7, 8]. One of the basic signs of cooperativeness is to give the other party choices rather than demanding an unfriendly yes or no answer to a single choice. Without changing the desired self-utility, the use of the SIM strategy allows the agent to utilize the presentation of multiple choices as a social cue [14] to communicate an apparent signal of flexibility in reaching an agreement. Therefore, given multiple choices each time, the counterpart is more likely to perceive a higher degree of cooperativeness on the part of the agent:

Hypothesis 5: A human counterpart is more likely to perceive the agent to be cooperative when the agent makes simultaneous-equivalent offers than when it makes sequential-single offers.

## Design of Acceptance Strategy and Hypotheses

Existing literature typically uses an immediate acceptance (IMM) strategy that a negotiator accepts a counteroffer when it exceeds a single decision threshold. For example, the agent accepts the first counteroffer that exceeds a certain decision threshold such as a reservation utility [12, 35, 57]. In a multi-issue negotiation where parties preferences may not be in direct conflict, even when an offer meets an agent’s reservation point, there still may be solutions that are better for both parties [40]. Therefore, the immediate acceptance of an offer runs an apparent risk of premature closure that results in less-than-desirable utilities for both parties.

We design a delayed acceptance (DLY) strategy to enable the agent to strategically explore a better deal by employing a parameter of “aspiration region” to respond to a counteroffer that meets its reservation utility. Instead of treating a negotiator’s aspiration as a single threshold, descriptive negotiation research suggests that a negotiator’s aspiration is rather a region [36, 54, 55], which can be defined by a lower threshold of a reservation utility (a subjective decision threshold below which the settlement is unacceptable) and an upper threshold of a target utility (a subjective decision threshold where the negotiator feels satisfied to conclude the negotiation). Correspondingly, our design of the DLY strategy allows the agent to maintain an adaptable aspiration region such that when a counteroffer falls in between the reservation utility and the target utility, the agent has the flexibility of withholding an immediate acceptance decision.

According to the negotiation literature, negotiators with higher aspirations tend to earn larger profits [6, 55]. Thus, the primary merit of the DLY strategy is to enhance the agent’s utility, which entails a high concern for self. When the agent delays acceptance of a counteroffer, it increases the chance that the counterpart will make a future offer with a higher utility to the agent, or the counterpart will accept the agent’s future offers. Hence, the agent is more likely to obtain a better agreement for itself. At the same time, although delayed acceptance primarily empowers the agent to achieve better utility, it does not prevent the counterpart from trading off different issues to arrive at an offer that benefits the counterpart’s utility. Therefore, the DLY strategy is also expected to increase the likelihood of obtaining better dyadic outcomes.

While delay of acceptance appears simple at the conceptual level, a strategic delay has to balance the increased chance for reaching better outcomes and the risk of reaching worse outcomes or ending up with nonagreement. Our design of the DLY strategy handles this risk with a “dynamic update method.” The agent, upon delaying the acceptance with an offer that exceeds its current reservation utility, (1) narrows down its aspiration region by setting the reservation utility to be equal to the utility of the counteroffer, (2) shortens its planned concession rounds based on the relative attractiveness of the counteroffer, and (3) saves the values of the counteroffer. Therefore, upon reaching the final round of its (shortened) planned concession rounds, or if faced with a “poorer” (i.e., a lower utility to the agent) final offer from the counterpart, the agent uses the saved counteroffer and makes it the final offer. Assuming that the counterpart is rational, he or she should be willing to accept an offer that he or she had proposed earlier as opposed to ending up with nonagreement. This method can thus help to reduce the risk associated with the delayed acceptance. Therefore, we predict that the DLY strategy will not harm the chance of agreement or the counterpart’s perception of the agent.

Hypothesis 6: An agent that uses the DLY strategy is more likely to obtain a better individual outcome than one that uses the IMM strategy.

Hypothesis 7: The agent–human dyad is more likely to obtain a better dyadic outcome when the agent uses the DLY strategy than when it uses the IMM strategy.

From a human perception perspective, studies suggest that negotiators who settle “too quickly” on an item tend to feel discomfort over the agreement that comes too easily. Such an undesirable state of affairs is a kind of “winner’s curse” [49, p. 48] as a negotiator suspects that the other party has an unseen advantage when an offer is immediately accepted [1, 2, 34]. A recent psychological study further indicates that it is because of “counterfactual thinking” that negotiators tend to feel less satisfied when the first offer is accepted [17]. On the contrary, negotiators feel better about a settlement when the negotiation involves a progression of concessions than when it does not [10]. By delaying an acceptance decision, the agent can create an opportunity for an agreement to be reached through progressive concession, thereby giving the counterpart a better feeling about the outcome:

Hypothesis 8: A human counterpart is more likely to feel satisfied with the outcome after negotiating with an agent that uses the DLY strategy than after negotiating with one that uses the IMM strategy.

## System Architecture and Strategy Implementation

The negotiation agent sy tem was developed as a Java EE Web application (Figure 2). The core functional components of the system include an Agent Configurator that was used to set the values of the task- and strategy-related parameters, and an Agent Executor that implemented the negotiation strategies. The system was configurable and reusable with regard to negotiation task scenarios and agent strategies for empirical evaluation. Without loss of generalization, the agent represented the seller and the human negotiator represented the buyer.

In the Agent Executor, the agent maintains a ranked list of all its offer alternatives in descending order using its utility function. In round 1, the agent identifies a subset of the alternatives with a utility value equal to or slightly greater than $U _ { i n i t i a l } .$ . In the SIM strategy condition, the agent applies an offer selection method that selects m offers that favor the counterpart on each of the m negotiation issues. If the counterpart accepts any of the offers, the negotiation terminates with an agreement. If the counterpart proposes a counteroffer, the agent invokes the acceptance strategy. If the acceptance strategy returns “accept,” the agent accepts the counteroffer and the negotiation terminates with an agreement. Otherwise, the agent calculates its next offer, $U _ { n e x t } ,$ by reducing it utility based on its concession pattern and selects another m offers. When the planned concession rounds, $R _ { m a x } ,$ , is reached, the agent makes a final set of offers matching $U _ { r e s e r v a t i o n } .$ The SEQ strategy differs from the SIM strategy only in that in each round one of the m offers is randomly selected and is sent to the buyer.

![](/api/attachments/GHK8X435/fulltext/images/48886fa84bb05f96351ba83e5d229e5a6ac3a16ced418e7cbe3176cc06d80d6c.jpg)  
Figure 2. The Overall Agent–Human Negotiation System Architecture

For the DLY strategy, the agent compares the counteroffer utility to check if it falls within the agent’s acceptance, rejection, or aspiration regions. If the counteroffer falls in the acceptance region (i.e., has a utility greater than $U _ { t a r g e t } )$ , the strategy returns “accept.” If the counteroffer falls in the rejection region (i.e., has a utility lower than $U _ { \mathit { r e s e r v a t i o n } } )$ , the strategy returns “offer.” If the counteroffer falls in the aspiration region, the agent uses the following dynamic update algorithm: If the counteroffer is final and has utility greater than or equal to $U _ { \mathit { r e s e r v a t i o n } } :$ , the strategy returns “accept.” Otherwise, the agent updates $U _ { \substack { r e s e r v a t i o n } }$ to be equal to the utility of the counteroffer, reduces the number of planned concession rounds $R _ { _ { m a x } }$ , saves the values of the counteroffer S, and the strategy invokes the offer strategy. For the IMM strategy, if a counteroffer has utility greater than $U _ { \substack { r e s e r v a t i o n } }$ , the strategy returns “accept.” Box 1 provides the complete pseudo code of the Agent Executor.

## Design Evaluation

## Experiment Design, Negotiation Task, and Manipulation

To em piric ally validate the des ign hy pothes es and the agent sy tem , we conducted a $2 \times 2$ factorial between-subject experiment (Figure 3). The human subjects played the role of buyer and were randomly assigned to interact with the seller agent using one of the four strategy conditions via a Web interface (Figure 4). The effects of buyers’ individual differences, target utilities, and strategies were controlled as a result of random assignment of subjects. The negotiation rules were reinforced by the Web interface and were applied to all the conditions.

Box 1. Agent Executor Pseudo Code

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Let $I_1, I_2, \ldots I_m$ be the issues under negotiation, where m is the number of negotiation issues
Let V be a vector of the value options of the issues under negotiation, i.e., $V = [v_1, v_2, \ldots v_n]T$
Let $O_k$ be a set of offer(s) computed by the agent in round k
Let $U_{BATNA}$ represent the utility at the BATNA
Let $U_{initial}, U_{target}$, and $U_{reservation}$ denote the agent's initial utility, target utility, and reservation utility
Let $R_{max}$ be the maximum number of rounds the agent is planning to negotiate

Let $C_k$ be the counteroffer received from the counterpart in response to $O_k$
Let $U(C_k)$ be the utility computed by the agent for the counteroffer $C_k$
Let S be the “best counteroffer received,” i.e., $S = C_j$ s.t. $U(C_j) &gt;= U(C_k) \forall k$
Let $d_k$ be the amount of concession the agent is prepared to make after receiving $C_k$
Let $U_{next}$ be the next offer the agent is prepared to make

Let SIM be a variable that is true if the agent uses SIM strategy, false for the SEQ strategy
Let DLY be a variable that is true if the agent uses DLY strategy, false for IMM strategy

Algorithm:
Set $k = 1$; $R = R_{max}$, $U_s = U_{reservation}$; $U_{next} = U_{target}$
while ($k \leq R$) do {
Send offer(s) to the buyer and receive response
Compute m offers with $U(O_k) \cong \text{Unext}$ &amp; select each of the offers that favor the counterpart on each of the m negotiation issues
If ($k == R$) mark $O_k$ as final
If (SIM) {
Send $O_k$ to buyer
} else {
Send a random offer from Ok to buyer
}
Receive a counteroffer from buyer and react to it
If (buyer agrees to $O_k$) {
Indicate success and terminate
} else if ($O_k$ was final) {
Compute $U_k = U(C_k)$
if ($U_k &gt;= U_{reservation}$) {
Accept counteroffer and terminate
} else {
Indicate failure and terminate
}
} else {
Set $C_k = counteroffer$
Compute $U_k = U(C_k)$
If ($U_k &gt;= U_{target}$) {
Accept counteroffer and terminate
} else if ($U_k &gt; U_s$) {
</div>

Box 1. Continued

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
If (DLY) {
    Set  $R = R_{max} * (U_{target} - U_k) / (U_{initial} - U_{BATNA})$ ;  $S = C_k$ ;  $U_s = U_k$ 
} else {
    Accept counteroffer and terminate
}
}
If ( $C_k$  is final) {
    If ( $U_k &lt; U_s$ ) {
    Propose S and get response from counterpart
    If (counterpart agrees to S) {
    Indicate success and terminate
    } else {
    Indicate failure and terminate
    }
    } else if ( $U_k &gt;= U_{reservation}$ ) {
    Accept counteroffer and terminate
    } else {
    Indicate failure and terminate
    }
}
Set  $U_{next} = U_{next} - d_k$ 
Set  $k = k + 1$ 
}
}
</div>

A four-issue buyer–seller negotiation task was adapted from the NSS literature.<sup>6</sup> Structurally, the task comprised four negotiation issues: unit price, quantity, support level, and delivery terms. There were seven value options for price, seven value options for quantity, four value options for support level, and four value options for delivery time. Thus, the combination of the value options of the four issues produced a total of $7 \times 7 \times 4 \times 4 = 7 8 4$ alternatives to the final agreement. The subjects (buyers) and agents (sellers) had different weightings over the issues and the value options (see Appendix A for the buyer’s utility specification and Appendix B for the seller’s). In game-theoretic terms, a non-zero-sum game was created that gave room for the dyad to reach win-win outcomes. To control for the effect of bargaining power, the same BATNA that represented 44 utility points was given to the buyers and sellers.

We configured the agent system with the negotiation task using the Agent Configu rator (see Appendix B). Thus, the effects of the seller’s strategic parameters (initial utility, planned concession rounds, concession pattern, target utility, and messages) were controlled to be the same across all the conditions. The Agent Executor read inputs from the Agent Configurator and evoked the alternate strategies SIM, SEQ,

<table><tr><td rowspan="2">Acceptance Strategy</td><td colspan="3">Offer Strategy</td></tr><tr><td>SEQ (sequential-single offer)</td><td>SIM (simultaneous-equivalent offers)</td><td></td></tr><tr><td>IMM(immediate acceptance)</td><td>28 subjects</td><td>26 subjects</td><td>54</td></tr><tr><td>DLY(delayed acceptance)</td><td>27 subjects</td><td>29 subjects</td><td>56</td></tr><tr><td></td><td>55</td><td>55</td><td></td></tr></table>

Figure 3. Experimental Design

![](/api/attachments/GHK8X435/fulltext/images/bbadbaff04d9b390432e586abc6672ddd55efe96edc111c6f00f8119667e8ce8.jpg)  
Figure 4. Sample Web Interface of the Seller’s Web Site

DLY, and IMM accordingly. Appendix C provides an illustration of the SIM and DLY strategies in the context of the negotiation task scenario.

## Subjects

Before the main experiment, a pilot study was conducted involving 20 executives and researchers. The experimental procedure and questionnaire items were finetuned based on their feedback. Subjects for the main experiment were recruited from an international business park in a large urban city in December 2008. The subject recruitment was announced via multiple channels (poster, flyers, and mass e-mails) with a description about the nature of the study and the reward structure and a Web link through which subjects could register for an experiment slot.

In total, 110 subjects completed the experiment procedure and made 110 agent– human dyads for the data analysis. Their average age was 30.5, and males comprised 55.5 percent. All the subjects had at least one year of working experience, and the majority (61.5 percent) had worked for 2–10 years. All the subjects had experience with group work. On average, the subjects had high computer efficacy (4.35 on a 5-point scale) and had been moderately exposed to online shopping (3.25 on a 5-point scale), business decisions (2.80 on a 5-point scale), and negotiation activities (2.42 on a 5-point scale).

A reward structure was set up to motivate the subjects to participate in the experiment and to achieve the goals prescribed in the experiment task, following an experimental economics methodology [47] that has been widely adopted in negotiation studies. Each subject received S\$20 (Singapore dollars) for participation (S\$1 ≈ U S\$0.80). Subjects who obtained higher individual utility scores on their negotiated agreements earned higher cash rewards: the top 10 percent, the second 10 percent, and the third 10 percent of the subjects received additional sums of S\$50, S\$30, and S\$20 each, respectively. The top winner also received a smart phone worth S\$750.

## Dependent Measures (Evaluation Metrics)

Economic negotiation outcomes were calculated based on the multi-attribute utility model [39]. Suppose the negotiating parties, A and B, have reached an agreement on three issues, X, Y, and Z. Based on the agreement and A’s utility function, A derives the following utilities: $U _ { x a }$ for X, $U _ { y a }$ for Y, and $U _ { z a }$ for Z. Similarly, B derives $U _ { x b }$ for X, $U _ { \mathrm { v } b }$ for Y, and $U _ { z b }$ for Z. The individual outcomes of A $( U _ { a } )$ and $B \left( U _ { b } \right)$ are calculated as $( U _ { x a } + U _ { y a } + U _ { z a } )$ and $( U _ { x b } + U _ { v b } + U _ { z b } )$ , respectively.

To access the efficiency of the dyadic outcome, two measures are adopted. The joint utility is simply the sum of $A \left( U _ { a } \right)$ and $B \left( U _ { b } \right)$ , and the Pareto efficiency is calculated as distance to the Pareto-efficient frontier as

$$
\min _ {i = 1} ^ {n} \sqrt {\left(U _ {a} - U _ {a i}\right) ^ {2} + \left(U _ {b} - U _ {b i}\right) ^ {2}},
$$

where $U _ { a i } , U _ { b i }$ denote the utilities of A and B corresponding to an efficient solution i. Here i is a sequential index of efficient solutions, and n is the total number of efficient solutions [18, 28]. For post hoc analysis, the distance to the Nash solution is calculated as

$$
\sqrt {\left(U _ {a} - U _ {a \_ n a s h}\right) ^ {2} + \left(U _ {b} - U _ {b \_ n a s h}\right) ^ {2}},
$$

where $U _ { _ { a \_ n a s h } } , U _ { _ { b \_ n a s h } }$ denote the utilities of A and B of the Nash solution [18, 28].

The social-psychological negotiation outcomes were evaluated using a postnegotiation questionnaire (Table 2). Items were adapted from previous studies for our analysis.

## Experiment Procedure

The experiment followed a three-stage procedure. In the prenegotiation stage, the subjects first read general instructions and were briefed on the procedure. The subjects were then given a task sheet (Appendix A) that described their roles as buyers. Their goal was to maximize their own utility scores over four issues for purchasing a new model of laptop computer over the seller’s Web site. It was emphasized that the higher the utility score the subjects could achieve, the higher the cash awards they would be able to receive. The subjects were asked to take a quiz to make sure that they understood the task. The subjects were also asked to record their target utility as the minimum point above which they would be satisfied to conclude an agreement. After this, the seller’s Web site and the negotiation rules were introduced. Finally, a prenegotiation questionnaire was administered to record the subjects’ past experiences for control checks.

In the second, actual negotiation stage, the subjects negotiated with the agent until they reached an agreement or until the negotiation ended with no agreement when one party rejected the other party’s final offer. No additional time limit was imposed by the experimenter.

The third stage was the postnegotiation stage. Upon completing the task, the subjects were asked to record their agreement and then to complete a questionnaire with which their postnegotiation perceptions were measured. Demographic information was also collected for control checks. When the subjects were debriefed, they were told to keep their experiences in this study confidential before receiving their participation rewards. Performance rewards were announced three weeks after the completion of all the experiment sessions.

## Data Analysis, Results, and Discussion

Construct Validity, Reliability Tests, and Control Check

Before hy pothes es tes ting, we firs t c heck ed the construct validity of the subjective dependent variables. Exploratory factor analysis with varimax rotation showed that the reversed item for perceived cooperativeness (PC\_2) did not satisfy the convergent criteria; it was thus dropped from subsequent analysis (this is supported by a reliability test that indicated that the Cronbach’s alpha increased if PC\_2 was deleted without sacrificing the content validity of the construct). The remaining items have acceptable reliability with a Cronbach’s alpha greater than 0.7, and a satisfactory convergent and discriminant validity with factor loadings on the intended constructs greater than 0.5 and loadings on unintended constructs less than 0.4 [19].

Table 2. Measurement Items of the Social-Psychological Negotiation Outcomes

<table><tr><td>Constructs</td><td>(Codes) Items</td><td>Scale</td><td>Source(s)</td></tr><tr><td>Satisfaction with the outcome</td><td>(SA_1) How satisfied are you with the utility score you earned?(SA_2) How satisfied are you with the values of the agreement?</td><td>1 = Extremely dissatisfied;4 = Indifferent; 7 = Ex-tremely satisfied1 = Extremely dissatisfied;4 = Indifferent; 7 = Ex-tremely satisfied</td><td>[8, 15, 36, 42]</td></tr><tr><td>Perceived cooperativeness</td><td>(PC_1) Do you think the seller was considerate about your interests and concerns?(PC_2) Do you think the seller was rigid in making offers to you? (R)(PC_3) Do you think the seller was friendly?(PC_4) Do you think the seller was flexible in making offers to you?(PC_5) What kind of “overall” impression did the seller make on you?</td><td>1 = Extremely inconsiderate; 4 = Moderately considerate; 7 = Ex-tremely considerate1 = Extremely flexible;4 = Moderately rigid;7 = Extremely rigid1 = Extremely unfriendly;4 = Moderately friendly;7 = Extremely friendly1 = Extremely rigid;4 = Moderately flexible;7 = Extremely flexible1 = Extremely negative;4 = Neither negative nor positive; 7 = Ex-tremely positive</td><td>[8, 15]</td></tr></table>

To examine internal validity, validation checks for controlled variables were performed to examine the effectiveness of the random assignment of the 110 subjects to the treatment conditions. The results showed no significant differences across treatment conditions due to subjects’ individual differences (i.e., age; gender; years of working experience; past experiences in group work, computer usage, online shopping, business decision making, and negotiations), their prenegotiation target utilities, and perception of the negotiation rules. Manipulation checks over the system logs were performed to ensure that the implementation of the strategies were in accordance with the conceptual level design.

## Hypotheses Testing

Overall, among the 110 agent–human dyads, 84 dyads obtained agreement and 26 dyads ended up with no agreement. No significant difference was found on the number of nonagreement cases across conditions.<sup>7</sup> The following hypothesis tests were conducted using the 110 cases.

For testing the effect of the offer strategy on counterpart agreement (H1), the results were submitted to a logistic regression where the two strategy variables were entered as between-subject predictors. The results confirmed that when the SIM strategy was used, a greater ratio of subjects decided to accept the agent’s offers than when the SEQ strategy was used (29/55 = 52.7 percent versus $1 5 / 5 5 = 2 7 . 3$ percent; $\beta = 1 . 1 0 5$ SE (standard error) = 0.408, Wald = 7.345, $p { = } 0 . 0 0 7 $ ). H1 is supported. No significant difference in counterpart acceptance was found between the DLY and IMM strategies (23/55 = 41.8 percent versus 21/55 = 38.2 percent; b = 0.270, SE = 0.405, Wald = 0.445, $p = 0 . 5 0 5 )$

A two-way multivariate analysis of variances (MANOVA) was used to investigate the effects of the two strategy variables on negotiation outcome measures. Levene’s test was performed to check the homogeneity of error variance assumption. The results suggested that this assumption was reasonably met, as the error terms for all the dependent variables except for the seller utility—Games–Howell statistics were thus used in the subsequent significant test on seller utility to minimize type I error— were equal across treatment conditions.

Table 3 summarizes the descriptive statistics and presents the MANOVA results for the main effects hypothesized in H2–H8. The interaction terms were all insignificant. An ANOVA test performed on each of the dependent variables suggested consistent results with the MANOVA results. The hypotheses tests reported above were also repeated in the subsample of the 84 agreement cases. The significance of variables did not change.

## Results and Discussion

The results confirmed that the proposed SIM strategy had significant and consistent positive effects on the economic and social-psychological negotiation outcomes for the agent–human dyads. From the economic perspective, the SIM strategy led to a higher chance that the agent’s offers would be accepted by the human counterpart (H1), resulted in greater counterpart utility (H2), as well as greater joint utility and smaller distance to the Pareto-efficient frontier (H3). From the social-psychological perspective, the subjects were more satisfied with the outcome (H4) and perceived the agent to be more cooperative<sup>8</sup> (H5) when the agent adopted the SIM strategy than when the agent adopted the SEQ strategy.

The DLY strategy allows for the achievement of significantly greater seller utility (H6), but its effect on the dyadic outcome in terms of joint utility and distance to the Pareto-efficient frontier is not significant (H7). A post hoc analysis that examined the agreement cases sample suggests that the distance to the Nash solution was significantly smaller in the delayed acceptant condition than in the immediate acceptance condition (mean = 15.26, SD [standard deviation] = 5.83 versus $\mathrm { m e a n } = 1 9 . 1 6 , \mathrm { S D } = 4 . 9 6 ,$ $F = 5 . 1 1 9 , p = 0 . 0 2 7 )$ . This indicates that DLY is a strategy that can potentially help in bringing the negotiated agreement closer to the Nash solution. No negative effects on the subjects’ (buyer) utility and their postnegotiation perceptions were detected. The results indicate that by incorporating region-based aspirations and sensitivity to the counterpart’s behavior, delayed acceptance can lead to better negotiation outcomes for the agent without adversely affecting a counterpart’s payoffs and subjective perceptions.

<sub>Descriptive</sub> <sub>Statistics</sub> <sub>and</sub> M<sup>ANOVA</sup>

<table><tr><td rowspan="2">Dependent measures</td><td colspan="2">Mean(standard deviation)</td><td rowspan="2"> $\eta_p^2$ </td><td rowspan="2">Power</td><td rowspan="2">F</td><td rowspan="2">p</td></tr><tr><td>SEQ</td><td>SIM</td></tr><tr><td>Buyer utility</td><td>59.95(11.48)</td><td>66.11(13.48)</td><td>0.061</td><td>0.736</td><td>6.834</td><td>0.010*</td></tr><tr><td>Seller utility</td><td>48.89(5.96)</td><td>48.87(7.28)</td><td>0.000</td><td>0.052</td><td>0.015</td><td>0.902</td></tr><tr><td>Joint utility</td><td>108.84(14.05)</td><td>114.98(14.95)</td><td>0.043</td><td>0.585</td><td>4.817</td><td>0.030*</td></tr><tr><td>Distance to Pareto frontier</td><td>14.62(10.32)</td><td>10.34(10.82)</td><td>0.040</td><td>0.551</td><td>4.436</td><td>0.038*</td></tr><tr><td>Distance to Nash solution</td><td>20.50(8.35)</td><td>20.87(7.73)</td><td>0.001</td><td>0.060</td><td>0.086</td><td>0.770</td></tr><tr><td>Satisfaction with outcome</td><td>3.61(1.60)</td><td>4.38(1.60)</td><td>0.056</td><td>0.700</td><td>6.290</td><td>0.014*</td></tr><tr><td>Perceived cooperativeness</td><td>3.56(0.96)</td><td>4.16(1.04)</td><td>0.085</td><td>0.873</td><td>9.784</td><td>0.002**</td></tr><tr><td>Buyer utility</td><td>63.87(12.95)</td><td>62.21(12.79)</td><td>0.006</td><td>0.122</td><td>0.618</td><td>0.433</td></tr><tr><td>Seller utility</td><td>47.07(5.27)</td><td>50.63(7.34)</td><td>0.073</td><td>0.815</td><td>8.303</td><td>0.004**</td></tr><tr><td>Joint utility</td><td>110.94(14.14)</td><td>112.84(15.42)</td><td>0.003</td><td>0.091</td><td>0.360</td><td>0.550</td></tr><tr><td>Distance to Pareto frontier</td><td>12.99(10.36)</td><td>11.99(11.18)</td><td>0.002</td><td>0.069</td><td>0.169</td><td>0.682</td></tr><tr><td>Distance to Nash solution</td><td>21.99(6.90)</td><td>19.42(8.84)</td><td>0.026</td><td>0.389</td><td>2.867</td><td>0.093</td></tr><tr><td>Satisfaction with outcome</td><td>3.98(1.72)</td><td>4.01(1.58)</td><td>0.000</td><td>0.050</td><td>0.000</td><td>0.998</td></tr><tr><td>Perceived cooperativeness</td><td>3.87(1.05)</td><td>3.85(1.05)</td><td>0.001</td><td>0.057</td><td>0.064</td><td>0.801</td></tr><tr><td colspan="7">Notes: n = 110. * p &lt; 0.05; ** p &lt; 0.01.</td></tr></table>

Contrary to H8, the results showed that the subject’s outcome satisfaction was not affected by the use of the DLY strategy versus the IMM strategy by the agent. One plausible explanation is associated with the limited manifestation of the agent’s immediate acceptance due to the incentive scheme of the experiment. The subjects were motivated to maximize their own utilities, and therefore made tough offers that were rarely accepted by the agent in the early rounds of negotiation. Consequently, the counterfactual thinking that negotiators tend to feel “settled too early” [17] was not triggered in the immediate acceptance condition. Another possible factor is the relative short total time needed for the parties to conclude the negotiation in the experimental setting as compared to real-world negotiations. Further research is warranted to confirm these postulates.

In the negotiation and marketing literature, negotiators’ outcome satisfaction [36] and a positive evaluation of their counterpart’s cooperativeness [7] are accepted as significant predictors to negotiators' desire to return to a negotiation with said counterpart in the future. As a post hoc analysis, we performed comparative linear regression tests to examine the factors affecting the subjects’ desire for future negotiation with the agent. The first regression model included all the studied variables except for the social-psychological outcomes $( n = 8 4 )$ .<sup>9</sup> The results suggested that the subjects’ (buyer) utility was as a significant factor affecting the desire for future negotiation with the agent $( \beta = 1 . 2 5 3 , p = 0 . 0 3 6 )$ . In comparison, when the social-psychological outcomes were added into the regression model, the relationship between the buyer utility and the desire for future negotiation became insignificant, and subjects’ satisfaction with the outcome $( \beta = 0 . 4 1 9 , p = 0 . 0 0 1 )$ and perceived cooperativeness of the agent $( \beta = 0 . 5 0 5$ $p = 0 . 0 0 0 )$ appeared to be the only two significant factors affecting their desire for future negotiation with the agent. The analysis shows that the effects associating social-psychological negotiation outcomes and future business relationship [7, 36] continue to hold in the agent–human negotiation context, and further supports our design theory that incorporates social-psychological metrics into the evaluation of agent negotiation strategy.

In the experiment, we adopted a negotiation task with typical additive, multi-attribute utility functions that assumes preferential independence [5, 41]. It is worth noting that the offer selection method in our SIM strategy needs to be adjusted to account for the situations where buyers are deemed to have nonadditive utility functions (see [3, 5, 41] for a discussion about nonadditive functions). Raiffa et al. [41, p. 154] suggest that nonadditive utility functions can be treated in an additive scheme by grouping the interdependent attributes as one “composite” attribute. Considering the situation in which two issues (e.g., price and quantity) of our four-issue negotiation scenario are issues preferentially interdependent on the buyers, the seller may group the two issues as a composite issue, and evoke the offer selection method by selecting three (instead of four) offers that favor the counterpart on price \* quantity, support, or delivery time. In this way, our proposed SIM strategy can be adjusted to handle situations where the counterpart may hold either additive or nonadditive utility functions.

When deployed in real-life e-market systems, the type of win-win negotiation agents could also be a potential target of exploitation, such as repeated attempts from a same buyer or collusion between buyers who exchange information about the agent’s reservation utility and preferences. We suggest the following solutions for tackling and mitigating these issues in a practical e-market system. From a managerial perspective, a human sales manager could employ software components that reinforce additional rules of negotiation for the particular type of product or service. For example, a “nonconcession detector” can be implemented such that the human sales manager will receive a notification to attend to a buyer who repeatedly submits tough offers without any concession. A “maximum sessions” policy can be implemented so that a buyer is only allowed to try a fixed number of negotiations in a given time period (e.g., one session per week). These components serve three purposes. First, they allow for a human-in-the-loop strategy, whereby a human negotiator could step in to settle anomalies. Second, a misbehaving buyer may face increased transaction costs such as longer a waiting time or even denial of service. Third, the e-market regulator can count abuses and exploitations into a buyer’s credibility profile, which could trigger further deterrence actions. Therefore, with the necessary e-market components to reinforce the negotiation protocol rules, the type of win-win seeking agents will be adequately protected against exploitation when deployed in real life.

## Implications, Limitations, and Future Research

## Implications

This res earc h propos es a theory -inform ed des ign for a negotiation agent and empirically evaluates its effects in agent–human negotiations. The first contribution of this study is the integration of negotiation theories developed in the human-based negotiation literature to make a software negotiator that strategically negotiates with high concerns for itself and its human counterpart. As two strategies with competing motivation, the concepts supporting simultaneous-equivalent offers and delayed acceptance have been proposed in the setting of human-operated negotiations. To the best of our knowledge, the current research is among the first—in both the agent-based and human-based negotiation literature—that has scrutinized both aspects of a negotiation strategy within a more comprehensive research model. The experimental results suggest that the proposed strategies produced better economic and social-psychological outcomes for both parties than conventional agent designs. Notably, the effects hold without requiring the human counterpart to be reciprocally win-win seeking; the subjects were only motivated to maximize self-utilities from the negotiated agreement and were left uncontrolled regarding their concerns and strategies.

In addition to contributing to the negotiations literature, this paper presents a design theory for a software negotiation agent in agent–human negotiations. Our design objective is a win-win seeking agent that classifies itself with a certain personality. We suggest that the dual concern model is a sensible kernel theory [52] to guide the design of such a win-win agent. Regarding the design evaluation component highlighted in Hevner et al. [21] and Peffers et al. [37], a set of evaluation metrics is identified to validate the agent strategies in the agent–human negotiation setting. As pointed out by Lin and Kraus [29], a main challenge in automated negotiations is to answer the question of “what constitutes a good negotiator?” when human factors are incorporated into the agent design. Our design theory enforces the importance of evaluating the effects of an agent in negotiations with real human counterparts to ensure that the human business partners feel satisfied with the outcome and with the cooperativeness of the agent. While existing design research on agent strategies often neglects the social-psychological implications, our study demonstrates that the proposed strategies have a consistent positive effect that appeals to, or at least does not harm, the economic and the social-psychological perspectives of negotiation outcomes. In this regard, this paper makes a bold attempt to establish the evaluation criteria for a “good agent negotiator” that potentially bridge the technical and social paradigm split in agent-based negotiation research.

On the more practical side, this research represents a step closer to the real e-commerce business settings for the creation of a win-win outcome in agent-based negotiations. First, in our experiment, while the agent is controlled to make a final offer in the ninth round, the proposed strategies have enabled the agent to obtain a higher overall acceptance ratio by the counterparts and more win-win agreements. Compared with probabilistic machine-learning techniques that require negotiation history data (e.g., [26, 35, 57]), the SIM strategy enables the agent to make sensible offers even when the agent has no information about the counterpart’s preferences in the first few rounds. Second, as suggested by Thompson [49], a good negotiation strategy should be effective with the most uncooperative negotiators. In the experiment, we created a reward structure in which the subjects were motivated to maximize their own utilities as long as an agreement could be reached. In other words, the subjects were incentivized to be “selfish” in the pursuit of their own benefits. Even in such situations, more positive outcomes were achieved when an agent used the proposed strategies. This demonstrates that “soft” relationship-selling skills such as communicating a flexible and cooperative personality on top of business goals can be built into software agents to serve as more effective surrogates for the human sales force in online e-commerce.

## Limitations and Future Research

Despite the noteworthy implications, the findings of this research should be interpreted within the defined problem scope. At the same time, several avenues open up for future research. First, we have assumed that both negotiation parties are preassigned a utility function that represents their respective preferences following the multi-attribute utility model [5, 40, 41] and have assumed that parties are capable of computing utility scores based on the utility function. It is beyond the scope of this research to claim that the strategies will work as effectively and efficiently when negotiation tasks are extremely complex such that parties’ preferences cannot be captured. It should be of interest as a topic for future research to challenge our boundaries and to examine the proposed strategies in more complex task settings.

Second, as Hevner et al. [21] have highlighted, design is a “search process” for discovering realistic information systems problems. An important strength of our SIM and DLY strategy designs are their capability to make sensible offer and acceptance decisions without requiring the agent to have prior knowledge about the counterpart’s private information or requiring history data. The research does not claim that the best, optimal negotiation agent artifact has been created in the agent–human context. There are at least two directions to extend this research from the strategy design perspective. One direction is associated with the design improvements on the SIM strategy. First, while in the present agent’s offer selection method we propose that the number of simultaneous offers should be equal to the number of issues of negotiation, it is worth noting that the extent to which the agent desires to withhold its preferences information and the counterpart’s cognitive load are considerations for the determination of the right number of simultaneous offers. Sensitivity tests should be conducted to verify if this is an optimal solution for a particular negotiation context. Second, the simultaneous offers in the present design are selected based on a method that derives equivalent offers with equal agent utility in a negotiation round. It worth examining, for example, under what conditions it would be beneficial to make the simultaneous offers of unequal self-utility values in each round and to make offers that are of equal self-utility over rounds. This direction is expected to enhance the intelligence and robustness of the negotiation agent, and deserves future research attention.

Another interesting direction is associated with extending this research to the situations where information asymmetry exists, that is, when the agent has partial information about the counterpart and/or when the counterpart has partial information about the agent. The partial information can be directly obtained from a dialog with the counterpart or it can be indirectly obtained from the offer exchange process from which the counterpart’s preferences are estimated. As the use of the simultaneousequivalent offers provides a chance for the agent to explore the counterpart’s preferences at a faster speed based on the counterpart’s response to the multiple offers [49, p. 88], the empirical findings on the effects of the SIM strategy provide an opportunity for developing new machine learning techniques [26, 35, 57].

## Conclusions

The c entral idea of this paper lies in that s uc es ful agent s trategies should balance a negotiator’s dual concern for the self and for the counterpart, and should lead to measurable positive economic and social-psychological negotiation outcomes.

Experimental results confirmed that compared to the conventional SEQ strategy, the proposed SIM strategy leads to a higher counterpart acceptance ratio, greater counterpart utility and joint utility, and more positive buyers’ outcome satisfaction and perceived cooperativeness toward the agent. Meanwhile, compared to the IMM strategy, the DLY strategy enhances the seller utility without adversely affecting other negotiation metrics.

Based on the empirical findings, we feel confident in recommending that a negotiation agent incorporating the proposed strategies be deployed to complement existing e-commerce technologies for facilitating small to medium-size online transactions. Our theory-informed design and empirical research demonstrate the significant potential of negotiation agent technologies in enhancing the efficiency of the negotiated transactions and the satisfaction of individual needs, and hence takes a step closer to fulfill the promise of mass customization for the next generation of e-commerce.

Acknowledgments: A preliminary version of this research was presented at the 30th International Conference in Information Systems in December 2009. The authors are grateful to Terence Hung, Gregory Kersten, Rob Kauffman, Hui Kai-Lung, Shang Di, and anonymous reviewers who provided constructive comments on the earlier versions of this research. They also thank Foo Yong Siang for his technical assistance in the system implementation and testing. This research is supported by the Institute of High Performance Computing, A\*STAR, Hewlett-Packard Labs, National University of Singapore, National Science Foundation of China (grant no. 71172038), Shanghai Pujiang Program, and the Program for Professor of Special Appointment (Eastern Scholar) at Shanghai Institutions of Higher Learning.

## Notes

1. See http://pages.ebay.com/help/buy/aboutbidding.html. Kersten et al. [25] provides a discussion of negotiations and auctions as two related but different e-commerce mechanisms.

2. See www.dell.com/us/soho/p/.

3. See http://trademanager.alibaba.com.

4. The private information assumption is consistent with the descriptive and prescriptive negotiation theories [13, 40] as well as research in artificial intelligence that attempts to model the counterpart’s preferences [4, 26, 35, 57]. It is in contrast with the normative, game-theoretic models, which assume “complete information” between negotiators [32, 33].

5. In practice, the negotiation protocol rules are presumably enforced by regulating e-market systems. We provide more discussion about this in the Results and Discussion section.

6. The negotiation scenario is developed from real-world supplier–buyer contract negotiations [24]. It has been validated to demonstrate sufficient face validity, content validity, and external validity in representing multi-issue business negotiations [24] and has been used in earlier NSS experiments [9, 15, 18]. In our experiment, the purchase of the engine subcomponents in the original scenario was adapted to the purchase of laptop computers because the characteristics of the latter are more familiar to the subjects who were general Internet shoppers.

7. By the “final offer” rule enforced in the experiment, nonagreement cases only occurred when subjects rejected the agent’s final offer and gave a final counteroffer that fell into the agent’s rejection region. This situation is consistently observed in the negotiation literature that “tough” negotiators with very high aspirations tend to receive backfires in counteroffers or summary rejection by their counterparts [39, 40].

8. A post hoc analysis suggests that even when the dyads failed to reach an agreement, subjects still perceived the agent to be more cooperative in the simultaneous-equivalent offer condition than they did in the sequential-single offer condition (mean = 3.96, SD = 0.74 versus mean = 3.11, $\mathrm { S D } = 0 . 9 2 ; F = 5 . 7 5 2 , p = 0 . 0 2 5 )$ . This implies that the SIM strategy can empower the agent to communicate a concern for the counterpart despite not reaching an agreement.

9. The variables include the strategy variables and their interaction (offer strategy, acceptance strategy, offer strategy \* acceptance strategy), the control variables (age, gender, years of working experience, target utility, past experiences in group work, computer usage, online shopping, business decision making, and negotiations), and the economic outcome metrics (buyer utility, seller utility, joint utility, distance to Pareto frontier, distance to Nash solution).

## Referenc es

1. Ball, S.B.; Bazerman, M.H.; and Carroll, J.S. An evaluation of learning in the bilateral winner’s curse. Organizational Behavior and Human Decision Processes, 48 (1991), 1–22.

2. Bazerman, M.H., and Samuelson, W.F. I won the auction but don’t want the prize. Journal of Conflict Resolution, 27, 4 (1983), 618–634.

3. Bichler, M. The Future of eMarkets: Multi-Dimensional Market Mechanisms. Cambridge: Cambridge University Press, 2001.

4. Chari, K., and Agrawal, M. Multi-issue automated negotiations using agents. INFORMS Journal of Computing, 19, 4 (2007), 588–595.

5. Clemen, R.T. Making Hard Decisions: An Introduction to Decision Analysis, 2d ed. Belmont, CA: Duxbury Press, 1996.

6. Cohen, W.H. The importance of expectations on negotiation results. European Business Review, 15, 2 (2003), 87–93.

7. Crosby, L.A.; Evans, K.R.; and Cowles, D. Relationship quality in services selling: An interpersonal influence perspective. Journal of Marketing, 54, 3 (1990), 68–81.

8. Curhan, J.R.; Elfenbein, H.A.; and Xu, H. What do people value when they negotiate? Mapping the domain of subjective value in negotiation. Journal of Personality and Social Psychology, 91, 3 (2006), 493–512.

9. Delaney, M.M.; Foroughi, A.; and Perkins, W.C. An empirical study of the efficacy of a computerized negotiation support system. Decision Support Systems, 20, 3 (1997), 185–197.

11. Faratin, P.; Sierra, C.; and Jennings, N.R. Negotiation decision functions for autonomous agents. Robotics and Autonomous Systems, 24, 3–4 (1998), 159–182.

12. Faratin, P.; Sierra, C.; and Jennings, N.R. Using similarity criteria to make issue trade-offs in automated negotiations. Artificial Intelligence, 142, 2 (2002), 205–237.

13. Fisher, R., and Ury, W. Getting to Yes: Negotiating Agreement Without Giving In. Boston: Houghton Mifflin, 1981.

14. Fiske, S., and Taylor, S. Social Cognition. New York: Random House, 1984.

15. Foroughi, A.; Perkins, W.C.; and Jelassi, M.T. An empirical study of an interactive, session-oriented computerized negotiation support system. Group Decision and Negotiation, 6, 4 (1995). 485–512.

16. Galinsky, A.D., and Mussweiler, T. First offers as anchors: The role of perspective-taking and negotiator focus. Journal of Personality and Social Psychology, 81, 4 (2001), 657–669.

17. Galinsky, A.D.; Seiden, V.; Kim, P.; and Medvec, V.H. The dissatisfaction of having your first offer accepted: The role of counterfactual thinking in negotiations. Personality and Social Psychology Bulletin, 28, 2 (2002), 271–283.

18. Goh, K.Y.; Teo, H.H.; Wu, H.X.; and Wei, K.K. Computer-supported negotiations: An experimental study of bargaining in electronic commerce. In S. Ang, H. Krcmar, W.J. Orlikowski, P. Weill, and J.I. DeGross (eds.), Proceedings of the 21st International Conference on Information Systems. Brisbane, Australia: Association for Information Systems, 2000, pp. 104–116.

19. Hair, J.F.; Anderson, R.E.; Tatham, R.L.; and Black, W.C. Multivariate Data Analysis: With Readings, 4th ed. Englewood Cliffs, NJ: Prentice Hall, 1995.

20. Henkel, L.A., and Mather, M. Memory attributions for choices: How beliefs shape our memories. Journal of Memory and Language, 57, 2 (2007), 163–176.

21. Hevner, A.R.; March, S.T.; and Park, J. Design science in information systems research. MIS Quarterly, 28, 1 (2004), 75–105.

22. Iyengar, S.S., and Lepper, M.R. When choice is demotivating: Can one desire too much of a good thing? Journal of Personality and Social Psychology, 79, 6 (2000), 995–1006.

23. Jennings, N.R.; Faratin, P.; Lomuscio, A.R.; Parsons, S.; Wooldridge, M.; and Sierra, C. Automated negotiation: Prospects, methods and challenges. Group Decision and Negotiation, 10, 2 (2001), 199–215.

24. Jones, B.H. Analytical mediation: An empirical examination of the effects of computer support for different levels of conflict in two-party negotiation. Ph.D. dissertation, Indiana University Graduate School of Business, Bloomington, 1988.

25. Kersten, G.E.; Noronha, S.; and Teich, J. Are all e-commerce negotiations auctions? In R. Dieng, A. Giboi, L. Karsenty, and G. De Michelis (eds.), Designing Cooperative Systems: The Use of Theories and Models. Amsterdam: IOS Press, 2000, pp. 387–398.

26. Lau, R.Y.K.; Wong, O.; Li, Y.; and Ma, L.C.K. Mining trading partners’ preferences for efficient multi-issue bargaining in e-business. Journal of Management Information Systems, 25, 1 (Summer 2008), 79–102.

27. Lewicki, R.J.; Saunders, D.M.; and Barry, B. Negotiation, 5th ed. Boston: McGraw-Hill, 2006.

28. Lim, L.H., and Benbasat, I. A theoretical perspective of negotiation support systems, Journal of Management Information Systems, 9, 3 (Winter 1992–93), 27–44.

29. Lin, R., and Kraus, S. Can automated agents proficiently negotiate with humans? Communications of the ACM, 53, 1 (2010), 78–88.

30. Mather, M.; Shafir, E.; and Johnson, M.K. Misrememberance of options past: Source monitoring and choice. Psychological Science, 11, 2 (2000), 132–138.

31. Medvec, V.; Leonardelli, G.J.; Galinsky, A.D.; and Claussen-Schulz, A. Choice and achievement at the bargaining table: The distributive, integrative, and interpersonal advantages of making multiple equivalent simultaneous offers. Paper presented at the 18th Annual Conference for the International Association for Conflict Management (IACM), Seville, Spain, June 12–15, 2005.

32. Nash, J. The bargaining problem. Econometrica, 18, 2 (1950), 155–162.

33. Nash, J. Two-person cooperative games. Econometrica, 21, 1 (1953), 128–140.

34. Neale, M.A., and Bazerman, M.H. Cognition and Rationality in Negotiation. New York: Free Press, 1991.

35. Oliver, J.R. A machine learning approach to automated negotiation and prospects for electronic commerce. Journal of Management Information Systems, 13, 3 (Winter 1996–97), 83–112.

36. Oliver, R.L.; Balakrishnan, P.V.; and Barry, B. Outcome satisfaction in negotiation: A test of expectancy disconfirmation. Organizational Behavior and Human Decision Processes, 60, 2 (1994), 252–275.

37. Peffers, K.; Tuunanen, T.; Rothenberger, M.A.; and Chatterjee, S. A design science research methodology for information systems research. Journal of Management Information Systems, 24, 3 (Winter 2007–8), 45–77.

38. Pruitt, D.G., and Rubin, J.Z. Social Conflict: Escalation, Impasse, and Resolution. Reading, MA: Addison-Wesley, 1986.

39. Pruitt, D.G. and Syna, H. Mismatching the opponent’s offers in negotiation. Journal of Experimental Social Psychology, 21, 2 (1985), 103–113.

40. Raiffa, H. The Art and Science of Negotiations. Cambridge: Harvard University Press, 1982.

41. Raiffa, H.; Richardson, J.; and Metcalfe, D. Negotiation Analysis: The Science and Art of Collaborative Decision Marking. Cambridge: Harvard University Press, 2002.

42. Rangaswamy, A., and Shell, G.R. Using computers to realize joint gains in negotiations: Towards an electronic bargaining table. Management Science, 43, 8 (1997), 1147–1163.

43. Rangaswamy, A., and Starke, K. Computer-mediated negotiations: Review and research opportunities. In A. Kent and J.G. Williams (eds.), Encyclopedia of Microcomputers, vol. 25, New York: Marcel Dekker, 2000.

44. Rubin, J.Z.; Pruitt, D.G.; and Kim, S.H. Social Conflict: Escalation, Stalemate, and Settlement, 2d ed. New York: McGraw-Hill, 1994.

45. Rubinstein, A. Perfect equilibrium in a bargaining model. Econometrica, 50, 1 (1982), 97–109.

46. Savage, G.T.; Blair, J.D.; and Sorenson, R.L. Consider both relationships and substance when negotiating strategically. Academy of Management Executive, 3, 1 (1989), 37–48.

47. Smith, V.L. Experimental economics: Induced value theory. American Economic Review, 66, 2 (1976), 274–279.

48. Thompson, L. Negotiation behavior and outcomes: Empirical evidence and theoretical issues. Psychological Bulletin, 108, 3 (1990), 515–532.

49. Thompson, L. The Mind and Heart of the Negotiator, 4th ed. Upper Saddle River, NJ: Prentice Hall, 2009.

50. Thompson, L., and Hastie, R. Social perception in negotiation. Organizational Behavior and Human Decision Processes, 47, 1 (1990), 98–123.

51. Tripp, T.M., and Sondak, H. An evaluation of dependent variables in experimental negotiation studies: The role of impasse rates and Pareto efficiency. Organizational Behavior and Human Decision Processes, 51, 2 (1992), 273–295.

52. Walls, J.G.; Widmeyer, G.R.; and El Sawy, O.A. Building an information system design theory for vigilant EIS. Information Systems Research, 3, 1 (1992), 36–59.

53. Walton, R.E., and McKersie, R.B. A Behavioral Theory of Labor Negotiations. New York: McGraw-Hill, 1965.

54. Weingart, L.R.; Thompson, L.L.; Bazerman, M.H.; and Carroll, J.S. Tactical behaviors and negotiation outcomes. International Journal of Conflict Management, 1, 1 (1990). 7–31.

55. White, S.B., and Neale, M.A. Reservation prices, resistance points, and BATNAs: Determining the parameters of acceptable negotiated outcomes. Negotiation, 7, 4 (1991), 379–399.

56. Yuan, Y.; Rose, J.; Suarga, S.; and Archer, N. A Web-based negotiation support system. International Journal of Electronic Markets, 8, 3 (1998), 13–17.

57. Zeng, D., and Sycara, K. Bayesian learning in negotiation. International Journal of Human–Computer Studies, 48, 1 (1998), 125–141.

58. Zipkin, P.H. The limit of mass customization. MIT Sloan Management Review, 42, 3 (2001), 81–87.

## Appendix A: Negotiation Task for Buyer

Tan Brothers Elec tronics is one of the top retailer companies of information technology products and services in the Asia-Pacific region. During the first three quarters of 2008, total sales increased slightly. However, as a percentage of market share, sales do not look good. Tan Brothers’ market share remained constant during the first three quarters and dropped slightly during the fourth, despite vigorous sales efforts. In an effort to reverse this trend, the marketing research department proposed launching a new laptop computer model in January 2009, which would sell with a technical support plan to its end-consumers.

Tan Brothers deals regularly with three major suppliers. Each of the suppliers offer quality laptop computers and good services, and Tan Brothers is satisfied with all aspects of previous purchase agreements. Tan Brothers is confident it can expect the same good performance in the future from these companies.

You are representing a purchasing manager of Tan Brothers to purchase a particular brand of laptop computer. In this task, you will be interacting with the sales manager from LaptopOnDemand, one of the three suppliers, through its portal Web site. The following specifies your company’s confidential guidelines for negotiating the pur chase agreement.

Table A1. Utility Table for Buyer

<table><tr><td>Unit price</td><td>S$2,050</td><td>S$2,100</td><td>S$2,150</td><td>S$2,200</td><td>S$2,250</td><td>S$2,300</td><td>S$2,350</td></tr><tr><td>Utility</td><td>39</td><td>33</td><td>27</td><td>20</td><td>13</td><td>7</td><td>0</td></tr><tr><td>Quantity</td><td>100 units</td><td>120 units</td><td>140 units</td><td>160 units</td><td>180 units</td><td>200 units</td><td>220 units</td></tr><tr><td>Utility</td><td>15</td><td>13</td><td>11</td><td>8</td><td>5</td><td>3</td><td>0</td></tr><tr><td>Support</td><td colspan="2">Platinum</td><td colspan="2">Gold</td><td colspan="2">Silver</td><td>Classic</td></tr><tr><td>Utility</td><td colspan="2">29</td><td colspan="2">19</td><td colspan="2">10</td><td>0</td></tr><tr><td>Delivery</td><td colspan="2">1 week</td><td colspan="2">2 weeks</td><td colspan="2">3 weeks</td><td>4 weeks</td></tr><tr><td>Utility</td><td colspan="2">17</td><td colspan="2">10</td><td colspan="2">5</td><td>0</td></tr></table>

## Negotiation Issues and Utility Table

The two critical issues for your company are unit price and technical support. Your company is counting on sales of this new laptop computer to reverse the trend of declining market share. The two main ways for this laptop computer to penetrate the market are through competitive pricing and an attractive service plan. Thus, the price must be kept low and the technical support level high.

Your company is also concerned about the delivery time of the first shipment. In order to capitalize on sales, your company desires an early shipment date—the earlier the better. Of course, purchase quantity is also important to your company. The quantity of purchase should be at least 100 units and not larger than 220 units (because of physical limitations on inventory storage space). With this limit, your company prefers a low purchase quantity—the lower the better. These two issues are important but are not as critical as unit price and technical support.

The utility table shown in Table A1 summarizes your negotiation task in quantified terms. Utility points represent, in a relative sense, how favorable or satisfying a value to an issue of negotiation is meant for your company. The higher the utility point, the more favorable the corresponding value. For example, S\$2,050/unit has higher utility points than S\$2,350/unit.

Your utility score is the sum of utility points for all four issues in the agreement. The higher the utility score you earn, the higher the prizes you will receive.

## The Bottom Line

As an experienced purchasing manager, you have explored possible agreements with the other two major suppliers. One supplier could not make delivery before the deadline, so you ruled that company out. The other has made the following final offer:

```yaml
Price: $2,250/unit
Quantity: 140 units
Support: Silver
Delivery: 2 weeks
```

So you know that there is no point in reaching an agreement with LaptopOnDemand if it is not at least as good as this offer. By referring to the utility table (Table A1), you can see that you are already guaranteed a utility score of 44 (i.e., 13 + 11 + 10 + 10 = 44). So, you should try to strike an agreement that is better than this offer—in a sense, this is your bottom line of this negotiation.

## Appendix B: Negotiation Task for Seller (Extract of Agent Configurator)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
&lt;AgentConfiguration name="Irene" debug="false" SIM="true" DLY="true"&gt;
    &lt;Issue name="price" units="S$/unit" min="2050" max="2350" delta="50" weight="0.15"&gt;
    &lt;UtilityFunction type="table"&gt;2050., 0., 2100., 3., 2150., 5., 2200., 8., 2250., 10., 2300., 13., 2350, 15.&lt;/UtilityFunction&gt;
    &lt;/Issue&gt;
    &lt;Issue name="quantity" units="units" min="100" max="220" delta="20" weight="0.37"&gt;
    &lt;UtilityFunction type="table"&gt;100., 0., 120., 6., 140., 12., 160., 19., 180., 25., 200., 31., 220., 37&lt;/UtilityFunction&gt;
    &lt;/Issue&gt;
    &lt;Issue name="support" weight="0.20"&gt;&lt;Labels&gt;Platinum, Gold, Silver, Classic&lt;/Labels&gt;
    &lt;UtilityFunction type="table"&gt;0.,0.,1.,7.,2.,13.,3.,20.&lt;/UtilityFunction&gt;
    &lt;/Issue&gt;
    &lt;Issue name="delivery" units="week(s)" min="1" max="4" delta="1" weight="0.28"&gt;
    &lt;UtilityFunction type="table"&gt;1.,0.,2.,9.,3.,19.,4.,28.&lt;/UtilityFunction&gt;
    &lt;/Issue&gt;
    &lt;BATNA&gt; price, 2250, quantity, 140, support, Silver, delivery, 2&lt;/BATNA&gt;
    &lt;MaxUtility value="100"/&gt;
    &lt;U$_{initial}$ value="80"/&gt;
    &lt;U$_{target}$ value="60"/&gt;
    &lt;U$_{reservation}$ value="44"/&gt;
    &lt;R$_{max}$ value="9"/&gt;
    &lt;ConcessionPattern&gt; 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0&lt;/ConcessionPattern¹&gt;
    &lt;Messages&gt; a set of messages that indicate different stages of the offer exchanges
    &lt;/Messages&gt;
    &lt;/AgentConfiguration&gt;
</div>

<sup>1</sup> The concession pattern is implemented in a “monotone-decreasing” fashion in which the utility intervals between the offers become successively smaller, signaling that one is approaching its decision threshold [40, p. 128].

## Appendix C: Illustration of the SIM and DLY Strategies

For the “offer s elec tion m ethod” in the SIM s trategy , Table C1 illustrates how the agent identifies the initial four offers to the buyer via the Web interface as shown in

Table C1. Illustration of Offer Selection Method for the SIM Strategy

<table><tr><td></td><td>Offer selection method</td><td>Resultant offer</td><td>Agent utility</td><td>Buyer utility</td></tr><tr><td>Choice 1</td><td>Favors the “price” issue for the buyer (i.e., selects the alternative that has the lowest price)</td><td>Price: 2,050.0 S$/unitQuantity: 220.0 unitsSupport: ClassicDelivery: 4.0 weeks</td><td>85</td><td>39</td></tr><tr><td>Choice 2</td><td>Favors the “quantity” issue for the buyer (i.e., selects the alternative that has the lowest quantity)</td><td>Price: 2,350.0 S$/unitQuantity: 160.0 unitsSupport: ClassicDelivery: 4.0 weeks</td><td>82</td><td>8</td></tr><tr><td>Choice 3</td><td>Favors the “support” issue for the buyer (i.e., selects the alternative that has the highest support level)</td><td>Price: 2,350.0 S$/unitQuantity: 220.0 unitsSupport: PlatinumDelivery: 4.0 weeks</td><td>81</td><td>10</td></tr><tr><td>Choice 4</td><td>Favors the “delivery” issue for the buyer (i.e., selects the alternative that has the earliest delivery date)</td><td>Price: 2,350.0 S$/unitQuantity: 220.0 unitsSupport: ClassicDelivery: 2.0 weeks</td><td>80</td><td>29</td></tr></table>

Figure 4. In round 1, the agent using the SIM strategy started from a target offer utility of 80 (up to a slightly greater upper utility threshold of 85) and identified a subset of 26 alternatives from the total 784 alternatives. Then, out of the 26 alternatives, the agent selected four offers that favored the buyer on each of the four negotiation issues. In other words, choice 1 had the lowest unit price to the counterpart, choice 2 had the lowest purchase quantity, choice 3 had the highest support level, and choice 4 had the earliest delivery time. The corresponding utilities for the four offers were equal or similar to the agent: 85, 82, 81, and 82. The buyer utilities for the four offers were 39, 8, 10, and 29, respectively.

In the next rounds, the agent presented another sets of four simultaneous-equivalent offers that can gradually make more attractive offers with higher buyer utilities (Figure C1).

For the “dynamic update method” in the DLY strategy, the agent maintains an aspiration region defined by a reservation utility that was initially set to the value of its objective BATNA utility of 44, and a target utility that was set at 60 (Figure C1). In addition, the agent maintains a dynamic variable S to memorize the “best offer received” from the counterpart. Two actual cases, presented in Table C2, from the experiment illustrate its effects.

![](/api/attachments/GHK8X435/fulltext/images/e9a1b1c64580a4aee6026718b55293540775f54b8f3c8a25bb6aae5ca734f7f7.jpg)  
Figure C1. Graphical Depiction of the SIM and DLY Strategies with the Task Setting

Table C2. Illustration of Dynamic Update Method for the DLY Strategy

<table><tr><td>Case 1</td><td>Case 2</td></tr><tr><td>In round 2, the subject “Steve” made an offer with a buyer utility of 69 and an agent utility of 45. As 45 fell into the agent’s Aspiration Region, the agent delayed the acceptance and proceeded with new offers.</td><td>In round 5, the subject “Stanley” made an offer with a buyer utility of 72 and an agent utility of 47. As 47 fell into the agent’s Aspiration Region, the agent delayed the acceptance and proceeded with new offers.</td></tr><tr><td>In round 7, Steve made a much more attractive offer with a buyer utility of 61 and an agent utility of 61. As 61 fell into the agent’s Acceptance Region, the agent accepted it and the negotiation ended with an agreement.</td><td>In rounds 6 and 7, Stanley made worse offers with agent utilities of 44 and 38, respectively. Given this, the agent made a final offer in round 8 matching the values of the offer by Stanley in round 6, and asked if Stanley would like to accept it. Stanley accepted it, and the negotiation ended with an agreement.</td></tr><tr><td>In this case, the agent with DLY strategy achieved a better individual utility outcome than it would have had it accepted the in round 2.</td><td>This case showed that by the DLY strategy, the agent can still minimize the risk of ending up with a worse outcome or nonagreement.</td></tr></table>
