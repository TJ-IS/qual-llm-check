---
otero_id: 22612
otero_key: "UB3TWEYA"
title: "An abductive model of group support systems"
authors: "Milam Aiken; Joseph Paolillo"
year: "2000"
journal: "Information & Management"
doi: "10.1016/s0378-7206(99)00037-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An abductive model of group support systems

Milam Aiken $^{*}$ , Joseph Paolillo

School of Business Administration, University of Mississippi University, Mississippi MS 38677, USA

Received 1 February 1999; accepted 30 July 1999

## Abstract

Few researchers have attempted to model group support system meeting behavior mathematically. Using Abductive Information Modeling (AIM), we show that group size and idea generation type are primary predictors of group process satisfaction. While similar to artificial neural networks, abduction frequently provides simpler models and yields weights for links among the model variables. Results show that the interrelationships among the model variables are non-linear. © 2000 Elsevier Science B.V. All rights reserved.

Keywords: Group support systems; Electronic meetings; Modeling; Abduction

## 1. Introduction

A relatively large quantity of experimental research has investigated isolated variables in group support system (GSS) meeting behavior $[13,24]$ . A few attempts have been made to model the interrelationships among these variables mathematically $[28]$ ; for example, one study used a linear equation to show how the number of comments generated in a meeting varies with group size $[26]$ , and another demonstrated the cost benefits of electronic meetings $[7]$ . In addition, neural networks have been used to classify groups using a GSS $[2]$ and to predict the length of the meetings $[3]$ .

The purpose of this paper is to develop a model of group process satisfaction as it relates to five other meeting variables. A meta-analysis of six model variables from 70 GSS meetings over the last eight years was conducted. Logical abduction was used on the data to determine automatically the simplest and most accurate model using the variables. The result demonstrates that group process satisfaction can be predicted with a high-order polynomial equation, providing support for our belief that the model is non-linear.

## 2. Group support systems

A group support system is a computer-based system that supports a meeting, and many studies have shown the enhanced effectiveness and efficiency of such systems for certain groups and tasks. The research model of Fig. 1 from [10], based upon the model in [16], shows how variables known before the meeting interrelate with variables determined during the meeting and results from the meeting.

Based upon a review of the literature and anecdotal evidence from experience conducting GSS meetings, we believe that group size and meeting technique (i.e., what specific type of idea generation process or GSS software) are primary determining factors for the success of such meetings. For example, a general consensus has arisen, suggesting that the benefits of electronic meetings outweigh the costs only after the group reaches a size of seven or eight $[21,23,25]$ . Although the marginal utility of larger groups in electronic meetings rises slowly after the break-even point, the decrease in traditional, oral meeting utility appears to drop exponentially $[4]$ .

![](/api/attachments/UB3TWEYA/fulltext/images/2df78f3156fa46344b92dbf72e1cb81af309ef51271681808578eacd63c0b983.jpg)  
Fig. 1. The group support system research model.

Several other studies investigated the influence of different electronic tools on group meetings (e.g., [17]). In particular, the electronic gallery writing technique [27] may be superior in terms of group process satisfaction to the electronic individual pool-writing technique used in the majority of studies in the literature [6,8,9]. However, both appear to be superior to their manual counterparts and to the traditional, oral meeting.

As shown in Fig. 2, group size and the idea generation technique used can each influence [15]:

1. Evaluation apprehension. Participants in large, oral meetings may feel more intimidated suggesting ideas, while the anonymity provided with GSS meetings reduces evaluation apprehension.

2. Rate of comment generation. The rate of comment generation (the number of comments per person per minute) decreases linearly with increasing group size in oral meetings because communication is serial (people must take turns talking), while the number of comments per person per minute in electronic meetings is relatively constant (participants can all write and read comments simultaneously).

These variables can, in turn, influence:

1. Production blocking. Participants will be more inhibited and write fewer comments with greater evaluation apprehension. Fewer comments will be generated in large, oral meetings than in large, GSS meetings because of the differences in serial and parallel communication.

2. Group process satisfaction. Because participants have less evaluation apprehension and write more comments in GSS meetings (possibly reducing overall meeting time), they are often more satisfied with the meeting process.

![](/api/attachments/UB3TWEYA/fulltext/images/22dd708295bc394555d2e4f617b372e960e1849fb3c8c4b879616af5206b46a6.jpg)  
Fig. 2. Theoretical model of group satisfaction.

## 3. Logical abduction

Logical abduction, a form of inference first developed about 130 years ago [18], was chosen as the modeling technique, based upon encouraging results from a comparison with neural networks [5]. In this study, abduction was found to be faster, easier to use, and just as accurate as neural network modeling, which is generally considered to be superior to most statistical techniques [20].

Using numeric functions to describe complex relationships, abduction differs from deduction and induction in that it may be used for problems with a high degree of uncertainty. Like induction, however, abduction learns from examples. By iteratively evaluating a large number of potential models, abduction determines the functional element coefficients, number of network elements, types of network elements, and the connectivity among the elements. Abduction utilizes a network of functions so that only the relationships among small subsets of variables need to be discovered at a time.

The Abductive Information Modeler (AIM), from Abtech Corporation, is an example of how abduction may be implemented. Using this software, the synthesized abductive network may consist of seven types of elements, described below and shown in Fig. 3 [1]:

1. Singles $w_0 + (w_1x_1) + (w_2x_1^2) + (w_3x_1^3)$

$$
\begin{array}{l l} 2. \text { Doubles } & w _ {0} (w _ {1} x _ {1}) + (w _ {2} x _ {2}) + (w _ {3} x _ {1} ^ {2}) \\ & + (w _ {4} x _ {2} ^ {2}) + (w _ {5} x _ {1} x _ {2}) + (w _ {6} x _ {1} ^ {3}) \\ & + (w _ {7} x _ {2} ^ {3}) \end{array}
$$

$$
\begin{array}{l l} 3. \text {   Triples   } & w _ {0} + (w _ {1} x _ {1}) + (w _ {2} x _ {2}) + (w _ {3} x _ {3}) \\ & + (w _ {4} x _ {1} ^ {2}) + (w _ {5} x _ {2} ^ {2}) + (w _ {6} x _ {3} ^ {2}) \\ & + (w _ {7} x _ {1} x _ {2}) + (w _ {8} x _ {1} x _ {3}) + (w _ {9} x _ {2} x _ {3}) \\ & (w _ {1 0} x _ {1} x _ {2} x _ {3}) + (w _ {1 1} x _ {1} ^ {3}) + (w _ {1 2} x _ {2} ^ {3}) \\ & + (w _ {1 3} x _ {3} ^ {3}) \end{array}
$$

4. White A linear weighted sum of all the outputs elements of the previous layer. $w_{1}x_{1} + w_{2}x_{2} + w_{3}x_{3} + \ldots$ $+w_{n}x_{n}$

5. Normalizers Normalizers transform all of the original input variables into a relatively common region with a mean of 0 and a variance of 1 using mean-sigma normalization. $w_{0} + (w_{1}x_{1})$

6. Unitizers A unitizer converts the range of the network outputs to a range with the mean and variance of the output values used to train the network. $w_0 + (w_1x_1)$

7. Wire elements Wire elements are used for a network that consists only of a normalizer and a unitizer.

AIM utilizes predicted squared error (PSE) to determine the network configuration [11]. PSE is defined as

$$
\mathrm{PSE} = \mathrm{FSE} + \mathrm{KP}
$$

![](/api/attachments/UB3TWEYA/fulltext/images/22991d3b54fd34aac6c38e1391e19dc4867b09c4641310accfab70cdd10feb39.jpg)  
Fig. 3. Four-input, three-layer abductive network.

where FSE is the fitting squared error of the model on the training data, and KP is a complexity penalty, defined as

$$
\mathbf {K P} = \mathbf {C P M} ^ {*} ((2 ^ {*} K) / N) ^ {*} s _ {p} ^ {2}
$$

where K, N, and $s_{p}^{2}$ are determined by the database of examples used to synthesize the network, and CPM, the complexity penalty multiplier, is a user-determined variable (in general, simpler, rather than more complex, models are preferred to avoid overfitting). K is the total number of coefficients, N is the number of training data, and $s_{p}^{2}$ is an a-priori estimate of the true unknown model error variance [19].

Using abduction, no assumptions, such as the underlying data distribution, independence of variables, or relationship (e.g., linear), need to be made. In this respect, the technique is similar to that used in artificial neural networks $[14,22]$ . However, there are a few differences between abduction and neural networks. Abduction (1) typically results in a network with fewer, more powerful nodes; (2) often results in faster network development; and (3) automatically determines the network architecture $[12]$ .

## 4. An abductive model

Data were gathered from a meta-analysis of 70 meetings with 1049 primarily undergraduate student participants over the past eight years. In these meetings, three groups discussed topics orally, with a transcript recorded simultaneously (designated meeting type 1); five groups discussed topics orally, with no transcript recorded (type 2); 22 discussed topics using an electronic pool-writing program (type 3); and 40 discussed topics using an electronic gallery writing program (type 4). All of the groups met face to face, and discussed ‘the campus parking problem’ and similar topics that have been used by other researchers. All measures, except group size and comments per person per minute, were obtained from self-assessed participants’ perceptions using Likert scales. Tables 1–5 show the means and standard deviations for each meeting type and for all observations.

A correlation analysis with results shown in Table 6 shows a strong positive and significant relationship among the meeting type and process satisfaction, evaluation apprehension, and production blocking. Tests of analysis of variance were also conducted. The meeting type was a significant predictor of the number of comments generated per person per minute (F = 12.41, p = 0.01), process satisfaction (F = 70.98, p = 0.01), evaluation apprehension (F = 15.11, p = 0.01), and production blocking (F = 22.04, p = 0.01). These results tend to support the model.

Abduction was applied to a training sample of 52 observations, and took five seconds on a 100 MHz PC to develop the model shown in Fig. 4 (FSE = 0.17; PSE = 0.21). Because of the CPM, only group size, idea generation type, and group satisfaction were included. That is, group size and idea generation type were found to be sufficient as determinants of the output variable. When applied to the evaluation sample of 18 observations, the mean absolute percentage error was 8.77 percent. In comparison, a multi-linear regression model had a MAPE of 44.52 percent and an $R^{2}$ of 0.49.

Table 1  
Model variable statistics (all meeting types) $(N = 70)$

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td></tr><tr><td> $Size^a$ </td><td>15.00</td><td>10.18</td></tr><tr><td> $Process\ satisfaction^b$ </td><td>3.67</td><td>0.93</td></tr><tr><td>Comments per person per  $minute^c$ </td><td>0.39</td><td>0.46</td></tr><tr><td> $Evaluation\ apprehension^d$ </td><td>3.99</td><td>0.54</td></tr><tr><td> $Production\ blocking^e$ </td><td>3.64</td><td>0.67</td></tr></table>

$^{a}$ Number of persons in meeting.  
$^{b}$ (Sat) Self-assessed evaluation of personal satisfaction with the meeting process (scale: 1, dissatisfied; 5, satisfied).  
$^{c}$ (Com) Number of comments generated during the meeting, per person per minute.  
$^{d}$ (Eval) Self-assessed evaluation of how others will criticize one’s comments (scale: 1, apprehensive; 5, not apprehensive).  
$^{e}$ (Prod) Self-assessed evaluation of how difficult it is to communicate in the meeting (scale: 1, difficult; 5, not difficult).

Table 2  
Model variable statistics (type 1: oral/writing) (N = 3)

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Size</td><td>32.67</td><td>23.59</td></tr><tr><td>Process satisfaction</td><td>3.27</td><td>0.98</td></tr><tr><td>Comments per person per minute</td><td>0.10</td><td>0.06</td></tr><tr><td>Evaluation apprehension</td><td>3.67</td><td>0.99</td></tr><tr><td>Production blocking</td><td>3.27</td><td>1.16</td></tr></table>

Table 3  
Model variable statistics (type 2: oral/no writing) (N = 5)

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Size</td><td>18.80</td><td>10.13</td></tr><tr><td>Process satisfaction</td><td>3.67</td><td>0.27</td></tr><tr><td>Comments per person per minute</td><td>0.39</td><td>1.51</td></tr><tr><td>Evaluation apprehension</td><td>3.05</td><td>0.21</td></tr><tr><td>Production blocking</td><td>3.08</td><td>0.55</td></tr></table>

Table 4  
Model variable statistics (type 3: electronic pool-writing) (N = 22)

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Size</td><td>12.50</td><td>6.60</td></tr><tr><td>Process satisfaction</td><td>2.72</td><td>0.65</td></tr><tr><td>Comments per person per minute</td><td>0.39</td><td>0.03</td></tr><tr><td>Evaluation apprehension</td><td>3.82</td><td>0.26</td></tr><tr><td>Production blocking</td><td>3.09</td><td>0.20</td></tr></table>

Table 5  
Model variable statistics (type 4: electronic gallery writing) (N = 40)

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Size</td><td>14.55</td><td>9.55</td></tr><tr><td>Process satisfaction</td><td>4.36</td><td>0.28</td></tr><tr><td>Comments per person per minute</td><td>0.29</td><td>0.05</td></tr><tr><td>Evaluation apprehension</td><td>4.24</td><td>0.47</td></tr><tr><td>Production blocking</td><td>4.04</td><td>0.56</td></tr></table>

Table 6  
Pearson correlation coefficients/Prob > |R|

<table><tr><td></td><td>Type</td><td>Sat</td><td>Com</td><td>Eval</td><td>Prod</td></tr><tr><td>Size</td><td>-0.25/0.04</td><td>-0.06/0.60</td><td>0.16/0.19</td><td>-0.02/0.86</td><td>0.02/0.84</td></tr><tr><td>Type</td><td></td><td>0.68/0.01</td><td>-0.27/0.02</td><td>0.55/0.01</td><td>0.58/0.01</td></tr><tr><td>Sat</td><td></td><td></td><td>-0.26/.02</td><td>0.56/0.01</td><td>0.70/0.01</td></tr><tr><td>Com</td><td></td><td></td><td></td><td>-0.32/0.01</td><td>-0.21/0.08</td></tr><tr><td>Eval</td><td></td><td></td><td></td><td></td><td>0.86/0.01</td></tr></table>

Another model was developed using comment rate, production blocking, and evaluation apprehension only as predictors of process satisfaction, resulting in an even more complex, non-linear equation with a

MAPE of 6.54 percent. Models using meeting type and group size to predict comment rate, evaluation apprehension, and production blocking, resulted in MAPEs of 11.76, 4.58, and 4.79 percent, respectively.

While the meta-analysis included a large number of diverse groups, tasks, and other variables, generalization of these results may be limited. For example, only a few oral meeting studies included the variables required here. However, we believe the relatively low error rate in the abductive model, along with results from the correlation analysis and analysis of variance, support the theoretical model.

![](/api/attachments/UB3TWEYA/fulltext/images/f755581fbfe21b71fe43c0b0ecbd302c569a75485987430bee1f6148c5f91543.jpg)  
Fig. 4. Abductive model of group satisfaction.

## 5. Summary

Research on GSSs from multiple perspectives may increase our understanding of these systems and provide a foundation for future research and development. Logical abduction, a relatively unknown technique, can be an additional perspective. Using an abductive model of GSS meetings, practitioners may be able to make accurate predictions of participant behavior. As this study illustrates, given a known group size and idea generation technique, practitioners may determine if the subsequent GSS meeting will be successful or not. Further, a mathematical representation of this meeting behavior may aid researchers' understanding of complex, non-linear relationships among the GSS model variables.

## References

[1] Abductive Information Modeler User's Manual, Abtech Corporation, Charlottesville, VA, 1994.

[2] M. Aiken, Artificial neural systems as a research paradigm for the study of group decision support systems, Group Decision and Negotiation 6(4), 1997, pp. 373–382.

[3] M. Aiken, B. Garner, J. Paolillo, M. Vanjani, A neural network model of group support systems, in: Proceedings of the 30th Annual Meeting of the Decision Sciences Institute, 20–23 November 1999, New Orleans, LA.

[4] M. Aiken, J. Krosp, A. Shirani, J. Martin, Electronic brainstorming in small and large groups, Information & Management 27, 1994, pp. 141–149.

[5] M. Aiken, J. Paolillo, M. Vanjani, A comparison of artificial neural networks with logical abduction, in: Proceedings of the Southwest Decision Sciences Institute, 10–13 March 1999, Houston, TX.

[6] M. Aiken, H. Sloan, J. Paolillo, L. Motiwalla, The use of two electronic idea generation techniques in strategy planning meetings, Journal of Business Communication 34(4), 1997, pp. 370–382.

[7] M. Aiken, T. Sudderth, L. Motiwalla, A group support system cost-benefit analysis, International Business Schools Computing Quarterly 9(1), 1997, pp. 1–6.

[8] M. Aiken, M. Vanjani, Idea generation with electronic poolwriting and gallery writing, International Journal of Information and Management Sciences 7, 1996, pp. 1–9.

[9] M. Aiken, M. Vanjani, J. Paolillo, A comparison of two electronic idea generation techniques, Information & Management 30, 1996, pp. 91–99.

[10] M. Aiken, M. Vanjani, T. Singleton, L. Motiwalla, A group decision support system research model, in: Proceedings of the Decision Sciences Institute, 22–25 November 1997, San Diego, CA.

[11] A. Barron, Predicted squared error: a criterion for automatic model selection, in: S. Farlow (Ed.), Self-Organizing Methods in Modeling: GMDH Type Algorithms, Marcel Dekker, New York, 1984, pp. 87–104.

[12] R. Barron, A. Mucciardi, F. Cook, J. Craig, A. Barron, Adaptive learning networks: development and application in the United States of algorithms related to GMDH, in: S. Farlow (Ed.), Self-Organizing Methods in Modeling: GMDH Type Algorithms, Marcel Dekker, New York, 1984, pp. 25–66.

[13] I. Benbasat, L. Lim, The effects of group, task, context, and technology variables on the usefulness of group support systems: a meta-analysis of experimental studies, Small Group Research 24, 1993, pp. 430–462.

[14] L. Caporaletti, M. Aiken, J. Johnson, Integrating electronic meeting systems with artificial neural systems, in: Proceedings of the 23rd Annual Meeting of the Decision Sciences Institute, November 1992, San Francisco, CA.

[15] T. Connolly, L. Jessup, J. Valacich Jr., Effects of anonymity and evaluation tone on idea generation in computer-mediated groups, Management Sciences 36, 1990, pp. 689–703.

[16] A. Dennis, J. George, L. Jessup, J. Nunamaker, D. Vogel, Information technology to support electronic meetings, MIS Quarterly 12(4), 1988, pp. 591–624.

[17] G. Easton, J. George, J. Nunamaker, M. Pendergast, Using two different electronic meeting system tools for the same task: an experimental comparison, Journal of Management Information Systems 7, 1990, pp. 85–100.

[18] K. Fann, Peirce's Theory of Abduction, Martinus Nijhoff, The Hague, 1970.

[19] S. Farlow, The GMDH algorithm, in: S. Farlow (Ed.), Self-Organizing Methods in Modeling: GMDH Type Algorithms, Marcel Dekker, New York, 1984, pp. 1–24.

[20] K. Fish, J. Barnes, M. Aiken, Artificial neural networks: a new methodology for industrial market segmentation, Industrial Marketing Management 24(5), 1995, pp. 431–438.

[21] R. Gallupe, A. Dennis, W. Cooper, J. Valacich, L. Bastianutti, J. Nunamaker, Electronic brainstorming and group size, The Academy of Management Journal 35(2), 1992, pp. 350–369.

[22] S. Haykin, Neural Networks: A Comprehensive Foundation, Macmillan, New York, 1994.

[23] H. Hwang, J. Guynes, The effect of group size on group performance in computer-supported decision making, Information & Management 26, 1994, pp. 189–198.

[24] P. McLeod, An assessment of the experimental literature on electronic support of group work: results of a meta-analysis, Human Computer Interaction 7, 1992, pp. 257–280.

[25] J. Nunamaker, A. Dennis, J. Valacich, D. Vogel, J. George, Electronic meeting systems to support group work, Communications of the ACM 34(7), 1991, pp. 40–61.

[26] J. Valacich, A. Dennis, A mathematical model of performance of computer-mediated groups during idea generation, Journal of Management Information Systems 11(1), 1994, pp. 59–72.

[27] A. Van Gundy, Idea Power: Techniques and Resources to Unleash the Creativity in your Organization, American Management Association, New York, 1992.

[28] D. Vogel, J. Nunamaker, Group decision support system

impact: a multi-methodological exploration, Information & Management 18, 1990, pp. 15–28.

![](/api/attachments/UB3TWEYA/fulltext/images/76bb31cc5dc4732c4f11db4b54b957cbde41e28de60b830343aecbf0f8580aea.jpg)  
Milam Aiken received a B.S. in Engineering and an M.B.A. from the University of Oklahoma, a B.A. in Computer Science and a B.S. in Business from the State University of New York, and a Ph.D. in Management Information Systems from the University of Arizona.

He is an Associate Professor of Management Information Systems at the University of Mississippi.

![](/api/attachments/UB3TWEYA/fulltext/images/b25622583e10dbe220222f57043a644228d201cf4acf52de9346f150854c3134.jpg)  
Joseph Paolillo received a B.S. in Chemistry from Ohio University, an M.B.A. from the University of Delaware, and a Ph.D. in Management from the University of Oregon. He is a Professor of Management at the University of Mississippi.
