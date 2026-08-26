---
otero_id: 21803
otero_key: "ZCU7ZVR4"
title: "Impact of information quality and decision-maker quality on decision quality: a theoretical model and simulation analysis"
authors: "Srinivasan Raghunathan"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00060-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Impact of information quality and decision-maker quality on decision quality: a theoretical model and simulation analysis

Srinivasan Raghunathan )

Management Science and Information Systems Department, JO 4.4, UniÕersity of Texas at Dallas, Richardson, TX 75083, USA Accepted 20 September 1999

## Abstract

The impact of information technology IT on firm performance is widely studied but little understood. A commonŽ . perception is that IT improves the quality of information, which, in turn, improves decision quality and performance. Several studies of IT-performance relationship have used managers’ perceiÕed as opposed to actual performance. We investigate the impact of information quality and decision-maker quality on actual decision quality using a theoretical and a simulation model. We use accuracy as the measure of quality. Our analysis shows that, depending on the decision-maker quality, decision quality may improve or degrade when information quality improves. The decision quality improves with higher information quality for a decision-maker that has knowledge about the relationships among problem variables. However, the decision quality of a decision-maker that doesn’t know these relationships may degrade with higher information quality. Simultaneous improvement in information quality and decision-maker quality results in higher decision quality. The simulation model, which relaxes some of the assumptions made by the theoretical model, yields similar results. We explain how our results supplement the results of prior studies of IT-performance relationship. Our results underscore the need for including decision-maker quality in the investigation of the IT-performance relationship and the importance of developing quality decision support tools. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: DSS impact; Decision quality; Data quality; Manager quality

## 1. Introduction

The annual investment in information technology Ž . IT by US companies is hundreds of billions of dollars. The reasons for the large IT investment include drastic reduction in computer hardware price and perceived improvement in productivity associated with IT investment 17 . Higher information<sup>w</sup> <sup>x</sup> quality, increased efficiency, lower costs, and higher product variety have been cited as reasons for improved productivity and performance associated with IT 4 . We address the relationship between informa-<sup>w</sup> <sup>x</sup> tion quality and performance in this paper.

Past research has investigated several dimensions of the impact of IT on performance using different approaches. Research that used financial and economic data has yielded mixed results, engendering the term ‘‘productivity paradox’’. The results varied depending on the industry, nature of IT investment, performance measure used, nature of the firm, and the level of analysis such as firm or industry. Behavioral and organization science based theories such as Technology Acceptance Model 9 and Task-Tech-<sup>w</sup> <sup>x</sup> nology Fit Model 15 have also been used to explain<sup>w</sup> <sup>x</sup> the relationship between IT and performance. This stream of research relied often on surrogate measures of performance based on user evaluation constructs such as self-reported intention to use or actual useŽ . and perceived performance. However, Straub et al. <sup>w</sup> <sup>x</sup> 27 reported that self-reported measures were not reliable by comparing computer-recorded objective measure and self-reported subjective measure of system use. Davis and Kotteman 11 reported that users <sup>w</sup> <sup>x</sup> overestimated their performance when the system provided support that matched their view of the problem because of ‘‘illusion of control’’. The users underestimated the effectiveness when the system provided support that did not match their view of the problem because of ‘‘cognitive conceit’’. However, Marsden and Mathiyalakan 19 reported that the<sup>w</sup> <sup>x</sup> ‘‘illusion of control’’ was not present when the pay-off for the decision-makers was determined using information acquisition cost and performance.

The difficulty in measuring actual performance led many prior studies to use managers’ perceived performance in their analysis. Research on data quality 29 also emphasizes quality from the data con- <sup>w</sup> <sup>x</sup> sumer’s perspective. This stream of research assumed that higher quality from the manager’s perspective improves the use of data and performance.

Our objective in this paper is to investigate, using a theoretical and a simulation model, the relationship among information quality, decision-maker quality, problem type, and decision quality. The simulation model relaxes some of the assumptions made by the theoretical model. We use accuracy as the measure of quality.

Our theoretical analysis shows that the decisionmaker’s quality, in addition to information quality, affects the decision quality significantly. In problems characterized by exact relationships among problem variables, the decision quality improves with higher information quality for decision-makers with accurate knowledge of the relationships. However, the decision quality degrades with higher information quality for decision-makers that do not have sufficiently accurate knowledge of the relationships. Simultaneous improvement in information quality and decision-maker quality prevents the degradation of decision quality. When exact relationships among problem variables do not exist, the information quality doesn’t have any impact on the decision quality. The simulation model, which relaxes some of the restrictive assumptions made by the theoretical model, yields similar results. Simulation results also suggest that the theoretical results are robust for different measures of decision quality. The results underscore the need for including decision-maker quality in the investigation of the IT–performance relationship and the importance of developing highquality decision support tools.

The rest of the paper has the following structure. Section 2 discusses prior research in this area. Section 3 discusses our model and theoretical results. Section 4 describes the simulation experiment design and presents the simulation results. Section 5 discusses how our results relate to past findings. Finally, Section 6 concludes the paper with a summary.

## 2. Prior research

Past research has investigated different dimensions of the impact of IT on performance using behavioral, organizational, and economic theories. We summarize significant findings below.

## 2.1. BehaÕioral and organizational science approach

Early studies focused on the user acceptance of and satisfaction with IT. The argument in this approach was that since an objective measure of the benefits of IT was difficult to achieve, user acceptance could be used as a surrogate to measure the impact of IT. DeLone and McLean 12 provide a <sup>w</sup> <sup>x</sup> very good survey of research on the quest for the measurement of IT impact. Bailey and Pearson 1<sup>w</sup> <sup>x</sup> developed the first tool that attempted to measure computer user satisfaction.

Later studies attempted to determine the explanatory variables for high or low usage of IT. The organizational context and the user involvement in the development of IT were found to have an impact on the usefulness of IT to a decision-maker 14 .<sup>w</sup> <sup>x</sup> Davis 9 developed the Technology Acceptance <sup>w</sup> <sup>x</sup>

Model TAM to explain a user’s behavioral inten-Ž . tion to use IT. TAM argued that the user’s perceived usefulness of the system and the perceived ease of use determine the user’s intention to use and actual use of a system 10 .<sup>w</sup> <sup>x</sup>

Recently, Goodhue 15 proposed Task-Technol-<sup>w</sup> <sup>x</sup> ogy Fit TTF to explain the performance of an ITŽ . user. TTF model argued that the task-technology fit, measured by sixteen dimensions that included the level of detail, meaning, accessibility, and accuracy of information, explained the relationship between IT and IT user’s performance 16 .<sup>w</sup> <sup>x</sup>

The studies mentioned above generally used behaÕioral characteristics for factors such as individual, task, and technology. They also used self-reported survey data for surrogate measures of performance such as the perceived performance, intention to use, and actual use. However, Straub et al. 27<sup>w</sup> <sup>x</sup> showed that self-reported measures were not reliable by comparing computer-recorded objective measure and self-reported subjective measure of number of mails sent and received in a voice mail system. Davis and Kottemann 11 , using a production plan-<sup>w</sup> <sup>x</sup> ning experiment, reported on the impact of what-if analysis and normative rule capability of a decision support system. They showed that the what-if capability led to a user expectation of better performance. They explained this phenomenon using the theory of ‘‘illusion of control’’. They also reported that normative decision rules in a system led to ‘‘cognitive conceit’’, which resulted in an expectation of lower performance. The results cautioned against placing reliance on user acceptance as an indicator of actual performance. However, Marsden and Mathiyalakan <sup>w</sup> <sup>x</sup> 19 reported that the ‘‘illusion of control’’ was not present when decision-maker’s payoff was determined using information acquisition cost and performance. The results suggested that incentive mechanisms can be designed to alleviate problems due to ‘‘illusion of control’’ phenomenon.

## 2.2. Empirical studies using economic data

Another stream of research that relates IT and performance has focused on empirical economic data. Brynjolfsson 5 provides a summary of this research <sup>w</sup> <sup>x</sup> and suggests possible explanations for the mixed results.

In economy-wide studies, Roach 24 concluded<sup>w</sup> <sup>x</sup> that information worker productivity decreased and blue-collar worker increased with higher IT investment, but Osterman 22 concluded the opposite<sup>w</sup> <sup>x</sup> result in his study. The studies on IT investment in the manufacturing sector also yielded mixed results when performance was measured using firm and sector level financial data 5 . When less aggregate <sup>w</sup> <sup>x</sup> variables, such as capacity utilization, were used, IT investment was found to be positively related to many of the performance variables 3 . Weill 30<sup>w x</sup> <sup>w</sup> <sup>x</sup> showed that IT investment in operational problem types increased productivity whereas strategic deployment of IT was not associated with productivity gains.

Many studies in the service sector 26,25 sug-<sup>w</sup> <sup>x</sup> gested a negative relationship between IT and performance. However, Brynjolfsson and Hitt 6 reported <sup>w</sup> <sup>x</sup> a return of over 60% on IT investment in service industries. Brynjolfsson et al. 7 showed that when <sup>w</sup> <sup>x</sup> lags were considered, IT investment reduced the firm size. Dos Santos et al. 13 used the stock price<sup>w</sup> <sup>x</sup> as a measure of the IT return. They found that the average return on all IT investments was not significantly different from zero in their study whereas innovative IT investments had a positive return. In summary, past empirical research provided mixed results on the nature of the IT investment-performance relationship.

Our research differs from and supplements prior research in many respects. We assume that IT improves information quality and decision-makers use the information produced by IT. We focus on whether higher information quality improves the actual performance. We introduce decision-maker quality as an intervening variable to investigate the IT-performance relationship. This requires us to model the decision-making process explicitly. We discuss the model next.

## 3. The model

The theoretical basis for our model is the wellknown input-process-output model employed in economics, systems analysis, and decision analysis 8 .<sup>w</sup> <sup>x</sup> In this model framework, the quality of the output depends on the quality of the inputs and the quality of the process that transforms the inputs to the output. We view decision-making process as a decision production process, as modeled by Cooper 8 .<sup>w</sup> <sup>x</sup> In our decision production model, the inputs are the information produced by IT, the outputs are the decisions made by the decision-maker, and the process is the decision-maker’s decision making process Ž . Fig. 1 . We assume that the decision-maker makes his<sup>r</sup>her decision based on information produced by IT. <sup>1</sup>

![](/api/attachments/ZCU7ZVR4/fulltext/images/86ef0f7ddc96c879fd13d380492d49f0475a25ba1f570ad0f5f3496eb666b48c.jpg)  
Fig. 1.

The decision-making process can be modeled in a variety of ways. We use belief networks 23 , which<sup>w</sup> <sup>x</sup> are similar to influence diagrams used in the decision analysis literature 21 , to model the decision-making <sup>w</sup> <sup>x</sup> process. Belief networks have been employed in a variety of problems including medical decision-making, oil exploration, forecasting, auditing, and financial analysis 20 . <sup>w</sup> <sup>x</sup>

## 3.1. Belief networks

A belief network represents the decision making process using a network of nodes which represent variables in the problem domain see Fig. 2 . TheŽ . nodes on the input side model the variables that affect the outcomes, represented by the output nodes. A belief network could have intermediate nodes. However, a network with intermediate nodes can be transformed into an equivalent network with only input and output nodes. Each node assumes a value of either 1 true or 0 false . The value representsŽ . Ž . the presence<sup>r</sup>absence of evidence, a condition satisfaction<sup>r</sup>violation, or confirmation<sup>r</sup>rejection of a conclusion. A node that needs to assume more than two values can be transformed into an equivalent set of nodes in which each node assumes either 0 or 1. The links represent the relationships between input and output values. The links have uncertainties associated with them. The uncertainties capture the randomness in the values of outputs for a given set of input values.

We have to distinguish between the actual uncertainty values associated with the links and the uncertainty values believed by the decision-maker. The actual uncertainty value captures the true conditional probability of the output given the inputs. The uncertainty value used by the decision-maker represents his<sup>r</sup>her belief about the true conditional probability. These beliefs are often formed through experience, intuition, judgment, analysis of historical data, data mining, or other methods. The beliefs need not be identical to the actual probabilities. The decisionmaker’s quality is determined by how close the decision-maker’s beliefs are to the actual probability values. We illustrate belief networks using the following example.

## 3.2. Belief networks: an example

Assume that an automobile insurance manager is faced with the problem of determining insurance risk of a customer, defined as the probability that the customer is a bad driver. The risk may be influenced by several factors. We consider customer’s age, marital status, and driving history in this example. Let age be represented as a binary variable with 1 denoting <sup>)</sup>25 and 0 denoting <sup>F</sup>25. Marital status is 1 Ž . Ž . Ž . married or 0 single . Driving history is 1 good or 0 bad . The insurance risk is categorized into 1Ž . Ž . Ž . high or 0 low . Table 1 may describe the conditional probability distributions, and decision-maker beliefs.

Mathematically, a belief network that has one output node and n input nodes, is represented as follows.

Let $i \in \left\{ 1 , 2 , \ldots , \right.$ 4 n be the ith input node and C be the Cartesian Product of n input values. Let $j \in \left\{ 1 , 2 , \ldots , 2 ^ { n } \right\}$ be the jth tuple in C. C includes $2 ^ { n }$ possible combinations of input values.Let

![](/api/attachments/ZCU7ZVR4/fulltext/images/62e68ada393dfb77fb6544066ff095b9918558bdc322db49a332b0ca9c2f0ad5.jpg)  
Fig. 2.

Table 1

<table><tr><td>Input combination number</td><td>Combination values</td><td>Probability (bad driver/inputs)</td><td>Belief (bad driver/inputs)</td></tr><tr><td>1</td><td>Age = 1Marital status = 1Driving history = 1</td><td>0.1</td><td>0.2</td></tr><tr><td>2</td><td>Age = 1Marital status = 1Driving history = 0</td><td>0.4</td><td>0.3</td></tr><tr><td>3</td><td>Age = 1Marital status = 0Driving history = 1</td><td>0.2</td><td>0.2</td></tr><tr><td>4</td><td>Age = 1Marital status = 0Driving history = 0</td><td>0.6</td><td>0.9</td></tr><tr><td>5</td><td>Age = 0Marital status = 1Driving history = 1</td><td>0.2</td><td>0.6</td></tr><tr><td>6</td><td>Age = 0Marital status = 1Driving history = 0</td><td>0.6</td><td>0.5</td></tr><tr><td>7</td><td>Age = 0Marital status = 0Driving history = 1</td><td>0.7</td><td>0.2</td></tr><tr><td>8</td><td>Age = 0Marital status = 0Driving history = 0</td><td>1.0</td><td>0.7</td></tr></table>

Ž .i I <sup>s</sup> Value of input node i; $I _ { i } \in \{ 0 , 1 \}$

Ž .ii $\mathrm { C P } _ { j } = \mathrm { P r o b } ( 0 = 1 | j ) ,$ , i.e., the conditional probability that output value is 1 given that the input tuple is j.

Ž . iii $B _ { i } = { \mathrm { B e l i e v e d } }$ value of input node i, $B _ { \mathrm { i } } \in \{ 0$ 14

Ž .iv $\mathbf { C B } _ { \mathrm { i } } = \mathbf { B e l i e f } ( \mathbf { O } = 1 | c _ { i } )$ , i.e., the conditional belief that output value is 1 given that the input tuple is $j .$

Ž .v $B _ { O } = { \mathrm { B e l i e f } } ( O = 1 )$

Ž .vi $P _ { O } = { \mathrm { P r o b } } ( O = 1 )$

## 3.3. Quality measures

We use the following quality measures in our analysis.

## 3.3.1. Information quality

Information quality has several dimensions. Wang and his team on data quality research 29,28 pio- <sup>w</sup> <sup>x</sup> neered the concept of data quality from the consumer’s data user’s perspective. They have devel-Ž . oped a hierarchical representation of data quality that includes intrinsic, contextual, representational, and accessibility dimensions. While we recognize that data quality is multi-dimensional, we measure information quality using its accuracy.

We define information quality of input i as the probability that the value of i believed by the decision-maker is the actual value. Thus, the quality of input i, $q _ { i } = { \mathrm { P r o b } } ( B _ { i } = I _ { i } )$ .

## 3.3.2. Decision-maker quality

Decision-maker quality refers to the quality of the decision-making process. The conditional beliefs describe the decision-making process in our model. We again use accuracy as the measure of decision-maker quality. For a perfectly knowledgeable decisionmaker, the conditional beliefs are equal to the respective conditional probabilities, i.e., $\mathrm { C B } _ { j } = \mathrm { C P } _ { j }$ for all $j .$ In the general model, the decision-maker quality may be different for different j. Thus, we define the decision-maker quality with respect to tuple $j , m _ { j } ,$ , as $( 1 - | \mathbf { C B } _ { j } - \mathbf { C P } _ { j } | ) . \ m _ { j }$ lies between 0 and 1.

## 3.3.3. Decision quality

The decision quality refers to the quality of the decision made by the decision-maker. We measure decision quality as $( 1 - | B _ { O } - P _ { O } | )$ . While we measure decision quality using the absolute difference between the probability and the belief that output value is equal to 1 or 0 , our results do not change ifŽ . we use absolute difference in the output values to measure decision quality. The simulation results described in Section 4 also confirm this.

## 3.3.4. Exogenous Õariable problem type ( )

In the belief network model, the conditional probabilities capture the type of the problem. We define the following problem types.

Definition 1: A perfectly deterministic problem is one for which CP is either 0 or 1 for all j.

The definition states that the true relationships in a perfectly deterministic problem can be stated exactly and each input combination produces one possible output value. Davis and Kotteman 1994 foundŽ . that decision-makers underestimated the effectiveness of decision rules in such problems.

Definition 2: A perfectly non-deterministic problem is one for which $\mathrm { C P } _ { j }$ is equal to a constant $p ,$ $0 < p < 1$ , for all $j .$

The definition states that input values do not affect the actual output in a non-deterministic problem. The actual output follows its own random distribution defined by parameter $p .$ Davis and Kotteman <sup>w</sup> <sup>x</sup> 11 found that decision-makers overestimated the effectiveness of what-if analysis in such a problem context.

## 3.4. Model analysis

In the general model, information quality can vary across inputs and the decision-maker quality can vary across input tuples. We impose the following restrictions for theoretical analysis. The results from a simulation experiment that does not make these restrictions are reported in Section 4.

Ž .i The information quality is identical for all input nodes, i.e., $q _ { i } = Q$ for all i.

Ž . ii The decision-maker quality is identical for all input combinations, i.e., $m _ { j } = M$ for all $j .$

The key analytical results of our paper are discussed below. The proofs are given in Appendix A.

Result 1: In a perfectly deterministic problem, the expected decision quality is positiÕely negati ( ) Õely related to information quality for high low quality( ) decision-makers.

The result has several implications for information quality–decision quality relationship. If the decision making process is accurate, an improvement in information quality improves the decision quality. This is likely with operational level problems, where the relationships can generally be described using exact rules and the decision-making procedures are well understood. On the contrary, if the underlying decision making process is inaccurate in operational problems, the result suggests that investment to improve data accuracy may worsen the decision quality. The knowledge base of decision-makers is likely to be more error prone in strategic problem areas. The result suggests that higher information quality may not lead to higher performance. It is worthwhile to note that Weill 30 reported poor rate of return on<sup>w</sup> <sup>x</sup> IT investment in strategic problem domains. The result also suggests that as decision-maker quality improves, the relationship between IT and decision quality becomes more positive.

Result 2: In a perfectly non-deterministic decision problem, the expected decision quality is directly proportional to the decision-maker quality and is independent of information quality.

Result 2 is intuitive. In a non-deterministic problem, input values don’t affect the output values, by definition. Consequently decision quality is independent of the input quality. The key reason for this is our assumption that the decision-maker quality is the same for all links. Under this assumption, the errors cancel out, on the average, when the decision-maker uses incorrect input combinations. While the assumption limits the usefulness of result 2, the simulation experiment that does not make this assumption yields similar results.

It is worthwhile comparing the above results with those obtained by Davis and Kotteman 11 . Our<sup>w</sup> <sup>x</sup> results suggest that when the problem has a deterministic structure, higher information quality improves the decision quality of those who know the input-output rules accurately. Davis and Kotteman <sup>w</sup> <sup>x</sup> 11 reported that decision-makers do not trust such rules because of cognitive conceit and may fail to take advantage of computer based tools that use such rules. For non-deterministic problems, according to Davis and Kotteman, decision-makers tend to overestimate the effectiveness of IT because of illusion of control and would perhaps over-invest in IT. Our results suggest that for such problems investment in improvement in information quality doesn’t alter the actual decision quality. However, as pointed out by Marsden and Mathiyalakan 19 , appropriate incentive mechanisms can be designed to mitigate the problems associated with ‘‘illusion of control’’.

The first two results assumed that improved information quality has no effect on the decision-maker quality. However, decision-makers often learn about the problem-specific relationships by analyzing data. We show the following result when the decisionmaker quality improves simultaneously with an improvement in information quality.

Result 3: In a perfectly deterministic problem, if the decision-maker quality improÕes simultaneously with an improÕement in data quality, then the relationship between decision quality and IT inÕestment is nonnegatiÕe.

The principal implication of the theoretical results is that the assumption that better information leads to better decision quality is not always valid. A significant intervening variable in the relationship between information quality and decision quality is the decision-maker quality. The results underscore the need improving decision-maker quality as well as information quality. While automation through IT can improve information quality, better decision support tools can potentially improve decision-maker quality.

## 4. Simulation analysis

Our theoretical results were derived under two restrictions: the information quality is identical for all input nodes and the decision-maker quality is identical for all input combinations. The restrictions were made to obtain analytical results. In this section, we discuss the results of a simulation model that did not make these assumptions.

## 4.1. The experimental design

We controlled three factors in our experiment: problem type, decision-maker quality, and input quality. The problem type was analyzed at three levels: perfectly deterministic, perfectly non-deterministic, and partially deterministic. The decision-maker quality was analyzed at three levels: high average accuracy of 1.0 , low average accu-Ž . Ž racy of 0.0 , and average average accuracy of 0.5 . . Ž . The input quality was analyzed at six levels: average accuracy of 0.0, 0.2, 0.4, 0.6, 0.8, and 1.0. Thus, our experimental design consisted of a $3 \times 3 \times 6$ factorial design. We used a model that consisted of five inputs and one output. <sup>2</sup>

## 4.2. Experiment procedure

For each cell in our design, we simulated 10 000 observations. For each of these observations, the input values and conditional probabilities were first generated randomly. The simulated input values and the conditional probabilities were then used to calculate the output probability distribution for each observation. For instance, assume that the network contains two input nodes and an output node. Further assume that the four conditional probabilities that relate the inputs and the output are 1 for inputŽ values 00 , 0 for input values 01 , 0.6 for input . Ž . Ž values 10 , and 0.2 for input values 11 . If the. Ž . generated input values are 00, then the actual output for this input is determined to be 1. If the input values are 10, then the output will have a value of 1 with probability 0.6 and 0 with probability 0.4.

For each observation, we simulated data for the decision-maker’s beliefs about the input values and conditional beliefs according to the required input quality and decision-maker quality respectively. We then calculated the decision-maker’s belief about the output value. The decision-maker’s belief and the probability of output were used to determine the decision quality.

## 4.3. Data generation

We discuss the details of the simulation procedure below.

## 4.3.1. Input quality

The input quality determines the probability that the correct input value is used by the decision-maker. For instance, if $I _ { i }$ is 1, then an accuracy level of 0.2 is translated into $P ( B _ { i } = 1 ) = 0 . 2$ . However, as we mentioned earlier, this accuracy need not be the same for all i. To achieve a given level of average input accuracy, we first randomly generated the accuracy of all inputs except one, and calculated the accuracy of the last input using the required average input accuracy. For example, assume that an average input accuracy of 0.3 was required and there were 5 inputs. We randomly generated accuracy for 4 inputs, say 0.1, 0.3, 0.1, and 0.2, and calculated the accuracy of the 5th input as 1.5Ž <sup>y</sup>sum of accuracy for the first 4 inputs.<sup>s</sup>0.8. If the accuracy of the 5th input did not lie between 0 and 1, then we ignored that data set. Once the accuracy for each input was determined, we used these to generate $B _ { i }$ for each i. Thus, if input $i \ ' \mathrm s$ accuracy had been determined to be 0.2 and $I _ { i } = 1$ , then 20% of generated $B _ { i }$ would be 1 and the rest would be 0.

## 4.3.2. Problem type

Perfectly deterministic structure was generated by setting the conditional probabilities of half of the total number of links to 1 and others to 0. Perfectly non-deterministic structure was generated by assigning a random value between 0 and 1 to all conditional probabilities. Partially deterministic structure was generated by making half of the links to be perfectly deterministic and other half to be perfectly non-deterministic.

## 4.3.3. Decision-maker quality

High decision-maker quality was implemented by equating the conditional beliefs to the conditional probabilities. Hence, $B _ { j } = P _ { j }$ , for all j, for a high quality decision-maker. Low quality decision-maker was implemented by making the decision-maker commit the maximum possible error in his<sup>r</sup>her belief about the actual probability. Thus, for perfectly deterministic problems, low decision-maker quality was implemented by setting $B _ { j } = ( 1 - P _ { j } )$ for all j. For perfectly non-deterministic problems, $B _ { j }$ for a low-quality decision-maker was set to 1 if the random probability $p \leq 0 . 5$ and 0 otherwise. The average decision-maker quality was implemented by making the decision-maker quality high for half of the links and low for the other half.

## 4.3.4. Decision quality

Decision quality was measured as 1Ž <sup>y</sup>the absolute difference between the output probability and . <sup>3</sup> belief .

## 4.4. Simulation results

The simulation results are tabulated in Table 2. Since our objective was to investigate the correlation between information quality and decision quality, we used non-parametric tests of correlation coefficient to verify our theoretical results. Specifically we used Kendall’s Tau statistic. The Kendall’s Tau values are shown in Table 3. They show that the following hypotheses cannot be rejected at the 5% confidence level.

Table 2 Simulation results

<table><tr><td>Manager quality</td><td>Information quality</td><td>Causal decision quality</td><td>Problem structure non-causal decision quality</td><td>Mixed decision quality</td></tr><tr><td rowspan="6">High</td><td>1</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>0.8</td><td>0.89</td><td>1.00</td><td>0.93</td></tr><tr><td>0.6</td><td>0.81</td><td>1.00</td><td>0.84</td></tr><tr><td>0.4</td><td>0.70</td><td>1.00</td><td>0.77</td></tr><tr><td>0.2</td><td>0.58</td><td>1.00</td><td>0.71</td></tr><tr><td>0</td><td>0.51</td><td>1.00</td><td>0.62</td></tr><tr><td rowspan="6">Low</td><td>1</td><td>0.00</td><td>0.49</td><td>0.24</td></tr><tr><td>0.8</td><td>0.10</td><td>0.51</td><td>0.30</td></tr><tr><td>0.6</td><td>0.17</td><td>0.50</td><td>0.36</td></tr><tr><td>0.4</td><td>0.29</td><td>0.50</td><td>0.40</td></tr><tr><td>0.2</td><td>0.42</td><td>0.49</td><td>0.45</td></tr><tr><td>0</td><td>0.47</td><td>0.50</td><td>0.51</td></tr><tr><td rowspan="6">Average</td><td>1</td><td>0.53</td><td>0.75</td><td>0.63</td></tr><tr><td>0.8</td><td>0.50</td><td>0.74</td><td>0.63</td></tr><tr><td>0.6</td><td>0.51</td><td>0.76</td><td>0.62</td></tr><tr><td>0.4</td><td>0.51</td><td>0.74</td><td>0.58</td></tr><tr><td>0.2</td><td>0.51</td><td>0.74</td><td>0.57</td></tr><tr><td>0</td><td>0.47</td><td>0.75</td><td>0.55</td></tr></table>

H1: In a perfectly deterministic problem, the decision quality is positively correlated with information quality for a high quality manager.

H2: In a perfectly deterministic problem, the decision quality is positively correlated with information quality for a low quality manager.

H3: In a perfectly non-deterministic problem, the decision quality is not correlated with information quality.

In order to test the impact of simultaneous improvement in information and decision-maker quality on decision quality, we categorized an input accuracy of 0.0 and low decision-maker quality as ‘‘low’ category, input accuracy of 0.6 and average decision-maker quality as ‘‘medium’’ category, and an input accuracy of 1.0 and high decision-maker quality as ‘‘high’’ category. The Kendall’s Tau for the correlation between these categories and decision quality was 1.0, which verified the positive correlation between simultaneous improvement in information and decision-maker quality and decision quality.

Table 3  
Kendall’s Tau values

<table><tr><td rowspan="2">Manager Quality</td><td rowspan="2">Causal</td><td colspan="2">Problem structure</td></tr><tr><td>Non-causal</td><td>Mixed</td></tr><tr><td>High</td><td>1.00</td><td>0.00</td><td>1.00</td></tr><tr><td>Low</td><td>-1.00</td><td>0.07</td><td>-1.00</td></tr><tr><td>Average</td><td>0.40</td><td>0.07</td><td>0.93</td></tr></table>

In summary, the simulation model confirmed our theoretical results.

## 5. A comparison of our results with prior results

We compare our results with those obtained in prior studies in this section. Unlike prior studies, we measured performance using decision quality which can be measured accurately in a theoretical and simulation setting. Also, we did not use financial measures for IT investments and performance as done by some of the past studies. Even though there are differences between our approach and those used in past studies, a comparison of our results with those of the past research provides useful insights into some of the reasons for the mixed results.

Several studies 3,30 found positive relationship <sup>w</sup> <sup>x</sup> between IT investment and performance for operational problems. While our model does not characterize problems in the same way, we hypothesize that the relationships between inputs and outputs are likely to be exact and known in operational problems. Our result of positive relationship between information quality and decision quality in such cases is consistent with prior results. Past studies showed no relationship between IT and performance for strategic problems 30 and when aggregate economy<sup>w</sup> <sup>x</sup> wide data were used 2,22,24 . We hypothesize that<sup>w</sup> <sup>x</sup> in such cases, the decision-maker quality is likely to be mixed, and the problem type is likely to be partially causal. Our model predicts no relationship between information quality and decision quality in these cases. Studies that assumed learning effects due to IT investment have shown positive relationship between IT and performance 7,18 . Our result 3<sup>w</sup> <sup>x</sup> is consistent with this.

In addition, our results further enhance our understanding of the IT–performance relationship based on behavioral science and organization theories. As stated in Section 2, TAM 9 showed that perceived<sup>w</sup> <sup>x</sup> usefulness and perceived use of IT impact the user’s IT use, and perceived performance. In our model, if we use the decision-maker’s belief instead of probability, i.e., we replace $\mathrm { C P } _ { j }$ with $\mathrm { C B } _ { j } ,$ to measure decision quality, we can show that higher information quality will lead to better perceived decision quality. Research on TTF 18 combines technology,<sup>w</sup> <sup>x</sup> individual, and task characteristics into a single construct to explain IT user’s performance. In our model, information quality, decision-maker quality, and problem structure determine the nature of IT–performance relationship. It should be noted, however, that Goodhue derived a rich set of 16 dimensions of the TTF construct but we use a single dimension for each of these factors. Our theoretical and simulation results also supplement the experimental findings of Davis and Kotteman 11 on the impact of problem<sup>w</sup> <sup>x</sup> structure on user’s perceived and actual performance and their caution against relying on user perception and acceptance as indicators of system success.

The significance of our results lies in the following areas. The results suggest that decision-maker quality affects the IT-performance relationship significantly to the extent of changing the sign of the relationship from positive to negative, and vice versa. Therefore, the decision-maker quality should be explicitly included in the investigation of the relationship between IT and performance. The results also highlight the importance of developing high-quality decision support tools.

## 6. Conclusion

A commonly stated reason for IT investment is that higher quality information produced by IT leads to higher performance. The difficulty in measuring actual performance has led many prior studies to use the decision-maker’s perceived performance as opposed to actual performance. These studies, therefore, assumed that decision-makers knew the correct decision in a problem context. We showed, using theoretical and simulation models of decision making, that the performance can improve or degrade even when information quality improves. In problems where exact relationships among problem variables exist, the decision quality improves with improvement in information quality for decision-makers with accurate knowledge of the relationships. However, for decision-makers that do not have sufficiently accurate knowledge of the relationships, the decision quality can decrease when information quality increases. If decision-maker quality improves simultaneously with information quality, then performance improves with information quality. When exact relationships do not exist in the problem, information quality doesn’t have any impact on decision quality. The simulation model, which relaxed some of the restrictive assumptions made by the theoretical model, yielded similar results. We showed how our results supplement and explain the results of prior studies of the IT–performance relationship. The results underscore the need for including decisionmaker quality in the investigation of the IT–performance relationship and the importance of developing quality decision support tools.

The research has several limitations. First, we used only accuracy as the measure of quality. In reality, quality can be measured using a variety of measures such as timeliness. IT can affect these dimensions of quality also. Our research did not address the performance measurement problems in real life settings. In our theoretical and simulation settings, performance could be measured objectively. It is unclear as to the appropriate measure of performance in a real life setting. Further research is needed to provide additional insights into the above aspects of the complex IT–performance relationship.

## Appendix A

## A.1. Proof for result 1

Let be the expected performance, Q be the quality for any input i, and M be decision-maker quality for any link j, then we need to show that $\partial \Pi / \partial Q > 0$ for higher values of M and $< 0$ lower values of M.

Let the actual value for input i be $I _ { i } .$ The actual input combination $C _ { J } = \left( I _ { 1 } , I _ { 2 } , . . . , I _ { n } \right)$ . Let the conditional probability for $C _ { \mathrm { J } }$ be $\mathrm { C P _ { J } }$ . Hence, the correct output ${ \bf \mu } = { \bf C P } _ { J }$

Since Q<sup>s</sup>probability of using the correct value for any input i, the probability of the decision-maker using the correct values for all n inputs<sup>s</sup>probability of using the correct combination $J = Q ^ { n }$

Since M<sup>s</sup>decision-maker quality for any input combination, the conditional belief for input combination J used by the decision-maker $= \mathrm { C P } _ { J } + e$ where e can assume $( 1 - M )$ Ž . or M <sup>y</sup> 1 .

Assuming that the $( 2 ^ { n } - 1 )$ incorrect combinations are equally likely to be used by the decisionmaker, the decision-maker will derive an output of

$$
Q ^ {n} \left(\mathrm{CP} _ {J} + e\right) + (1 - Q ^ {n}) \sum_ {j \neq J} \left(\mathrm{CP} _ {j} + e\right) / \left(2 ^ {n} - 1\right).
$$

Let $K = \sum _ { \substack { j \neq J } } ( \mathbf { C P } _ { j } + e ) / ( 2 ^ { n } - 1 ) \leq 1$ Therefore ${ \cal { I I } } = 1 \ \mathrm { \bar { - } } \ { \cal { E } } ( | \mathrm { C P } _ { \cal { I } } - { \cal { Q } } ^ { n } ( \mathrm { C P } _ { \cal { I } } + e ) - ( 1 -$ $Q ^ { n } ) K | )$

We consider both possible values of $\mathrm { C P } _ { J }$

Case i: $\mathrm { C P } _ { I } = 1$

When $P _ { \mathrm { C c } } ^ { * } = 1 , e$ for the combination J can only be negative, i.e., e can be replaced with $\left( M - 1 \right)$ for this input combination. Also, the output error is negative.

So $\begin{array} { r } { \begin{array} { r } { I I = Q ^ { n } \ M + ( 1 - Q ^ { n } ) K \ \partial I I / \partial Q = n Q ^ { n - 1 } \ ( } { M - } \end{array} } \end{array}$ K ., which is $> 0$ only if $M > K$

Case ii: $\mathrm { C P } _ { J } = 0$

When ${ \mathrm { C P } } _ { J } = 0 , e$ for the combination J can only be positive, i.e., e can be replaced with $( 1 - M )$ for this input combination. Also, the output error is positive.

So $m = 1 - Q ^ { n } \left( 1 - M \right) - \left( 1 - Q ^ { n } \right)$ K $\partial \Pi / \partial Q =$ $n Q ^ { n - 1 } \left( M + K - 1 \right)$ , which is $> 0$ only if $M > 1 -$ K.

## A.2. Proof for result 2

As stated in the proof of result 1,

$$
\begin{array}{l}\Pi = 1 - E \left(\left| \mathrm{CP} _ {J} - Q ^ {n} \left(\mathrm{CP} _ {J} + e\right) \right. \right.\\\left. - (1 - Q ^ {n}) \sum_ {j \neq J} \left(\mathrm{CP} _ {j} + e\right) / (2 ^ {n} - 1) \right|\left. \right)\end{array}
$$

In the case of non-deterministic problems, ${ \mathrm { C P } } _ { j } = P ^ { * }$ a constant for all j.

Since on the average, the error in the belief is equally likely to be positive or negative,

$$
\Sigma \left(\mathrm{CP} _ {j} + e\right) / \left(2 ^ {n} - 1\right) = P ^ {*} + e
$$

Substituting the above in we get $\displaystyle { I I = 1 - | e | = M }$ Hence,  is independent of $Q$ and is directly proportional to M.

## A.3. Proof for result 3

Since we are assuming that IT investment increases both M and Q, we need to show that $\partial { \cal I } { \cal I } / \partial Q \partial { \cal M } \geq 0$ .Proof: We know from the proof of result 1 that $\partial { \cal I } / \partial Q$ is either $n Q ^ { n - 1 } \left( M - K \right)$ or $n Q ^ { n - 1 } \left( M + K - 1 \right)$ for a perfectly deterministic problem. For both of these, $\partial \Pi / \partial Q \partial M = n Q ^ { n - 1 } \geq 0 .$

## References

<sup>w</sup> <sup>x</sup> 1 J.E. Bailey, S.W. Pearson, Development of a tool for measuring and analyzing computer user satisfaction, Management Science 29 1983 530–544.Ž .

<sup>w</sup> <sup>x</sup> 2 M. Baily, A. Chakrabarti, Electronics and white-collar productivity, in: Innovation and the Productivity Crisis, Brookings, Washington, 1988.

<sup>w</sup> <sup>x</sup> 3 A. Barua, C.H. Kriebel, T. Mukhopadhyay, Information technologies and business value: an analytic and empirical investigation, Information Systems Research 6 1 1995 3–23.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 G.M. Brooke, Information technology and productivity: an economic analysis of the effect of product differentiation, PhD Thesis, University of Minnesota, MN, 1991.

<sup>w</sup> <sup>x</sup> 5 E. Brynjolfsson, The productivity paradox of information technology, Commun. ACM 36 12 1993 66–77.Ž . Ž .

6 E. Brynjolfsson, L. Hitt, Is information systems spending productive? new evidence and new Results, International Conference on Information Systems, 1993.

7 E. Brynjolfsson, T.W. Malone, V. Gurbaxani, A. Kambil, Does information technology lead to smaller firms?, Management Science 40 1994 1628–1644.Ž .

<sup>w</sup> <sup>x</sup> 8 R.B. Cooper, Decision production: a step toward a theory of decision-makerial information requirements, International Conference on Information Systems, 1983, 251–268.

<sup>w</sup> <sup>x</sup> 9 F. Davis, Perceived usefulness, perceived ease of use, and user acceptance of IT, MIS Quarterly 13 1989 319–340.Ž .

<sup>w</sup> <sup>x</sup> 10 F. Davis, R.P. Bagozzi, P.R. Warshaw, User acceptance of computer technology: a comparison of two theoretical models, Management Science 35 1989 982–1003.Ž .

<sup>w</sup> <sup>x</sup> 11 F. Davis, J.E. Kottemann, User perceptions of decision support effectiveness: two production planning experiments, Decision Sciences 25 1 1994 57–78.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 W.H. DeLone, E.R. McLean, IS success: the quest for the dependent variable, Information Systems Research, 1992, 60–95.

<sup>w</sup> <sup>x</sup>13 B.L. DosSantos, K. Peffers, D.C. Mauer, The impact of information technology investments on the market value of the firm, Information Systems Research 4 1993 1–23.Ž .

<sup>w</sup> <sup>x</sup> 14 C.R. Franz, D. Robey, Organizational context, user involvement, and the usefulness of IS, Decision Sciences 17 1986Ž . 329–356.

<sup>w</sup> <sup>x</sup> 15 D.L. Goodhue, Understanding user evaluation of IS, Management Science 41 1995 1827–1844.Ž .

<sup>w</sup> <sup>x</sup> 16 D.L. Goodhue, R.L. Thompson, Task-technology fit and individual performance, MIS Quarterly 1995 213–236.Ž .

<sup>w</sup> <sup>x</sup> 17 V. Gurbaxani, H. Mendelson, An integrative model of information systems spending growth, Information Systems Research 1 1990 23–46.Ž .

<sup>w</sup> <sup>x</sup> 18 S.E. Harris, J.L. Katz, Predicting organizational performance using information technology control ratios, Twenty-Second Hawaiian International Conference on Systems Sciences, 1989.

<sup>w</sup> <sup>x</sup> 19 J. Marsden, S. Mathiyalakan, An empirical investigation into the relationship between performance and perception of users with a what-if facility, Journal of Organizational Computing and Electronic Commerce 7 4 1997 305–326.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 I. Matzkevich, B. Abramson, Decision analytic networks in artificial intelligence, Management Science 41 1995 1–22.Ž .

<sup>w</sup> <sup>x</sup> 21 A.C. Miller, M.W. Merkhoffer, R.A. Howard, J.A. Matheson, T.R. Rice, Development of automated aids for decision analysis, SRI, CA, 1976.

<sup>w</sup> <sup>x</sup> 22 P. Osterman, The impact of computers on the employment of clerks and decision-makers, Industrial and Labor Relations Review 39 1986 175–186.Ž .

<sup>w</sup> <sup>x</sup> 23 J. Pearl, Fusion, propagation, and structuring in belief networks, Artificial Intelligence 29 1986 241–288.Ž .

<sup>w</sup> <sup>x</sup> 24 S.S. Roach, America’s white-collar productivity dilemma, Manufacturing Engineering 1989 104.Ž .

<sup>w</sup> <sup>x</sup> 25 S.S. Roach, Services under siege — the restructuring imperative, Harvard Business Review 1991 82–92.Ž .

<sup>w</sup> <sup>x</sup> 26 P.A. Strassman, The business value of computers, Information Economics Press, CT, 1990.

<sup>w</sup> <sup>x</sup> 27 D. Straub, M. Limayem, E. Karahanna-Evaristo, Measuring system usage: implications for IS theory testing, Management Science 41 8 1995 1328–1342.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 D.M. Strong, Y.W. Lee, R.Y. Wang, Data quality in context, Commun. ACM 40 1997 103–110.Ž .

<sup>w</sup> <sup>x</sup> 29 R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of MIS 12 1996Ž . 5–34.

<sup>w</sup> <sup>x</sup> 30 P. Weill, Do computers pay off?, ICIT Press, Washington, DC, 1990.

Srinivasan Raghunathan is a faculty memeber in the school of management, University of Texas at Dallas. He obtained his PhD in business administration from the University of Pittsburgh. He taught at Bowling Green State University prior to joining UT-Dallas. His current research interest lie in the role of information goods. His articles have appeared in several journals.
