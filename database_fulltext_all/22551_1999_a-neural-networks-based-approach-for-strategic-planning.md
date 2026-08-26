---
otero_id: 22551
otero_key: "4FEKVZ47"
title: "A neural networks-based approach for strategic planning"
authors: "T.William Chien; Chinho Lin; Bertram Tan; Wen Chuan Lee"
year: "1999"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00100-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A neural networks-based approach for strategic planning $^{1}$

T. William Chien $^{a,*}$ , Chinho Lin $^{b}$ , Bertram Tan $^{c}$ , Wen Chuan Lee $^{c}$

$^{a}$ Management Department, Zicklin School of Business, Baruch College, The City University of New York, 17 Lexington Avenue, Box F-1831, New York, NY 10010, USA $^{b}$ Department of Industrial Management, National Cheng Kung University, Tainan, Taiwan, ROC $^{c}$ Department of Business Administration, National Cheng Kung University, Tainan, Taiwan, ROC

Received 5 October 1997; revised 24 July 1998; accepted 8 November 1998

## Abstract

We establish a systematic approach that incorporates neural networks in conjunction with portfolio matrices to assist managers in evaluating and forming strategic plans. Based on the principle of dispersing risks, we also provide a linear integer programming model, which helps in allocating the annual budget optimally among proposed strategies. The approach has been successfully implemented for a major food industry leader in Taiwan for its annual strategic planning. Although a particular portfolio matrix model was adopted in our approach, the framework proposed here can be modified to incorporate other strategy-evaluation measures. © 1999 Elsevier Science B.V. All rights reserved.

Keywords: Neural networks; Strategic planning; Linear integer programming; Portfolio matrices

## 1. Introduction

Before working out their final strategic plan, managers must consider several feasible alternatives and contemplate various factors behind each of them. It is a very complicated task to select the best strategic plan.

At present, strategic planning approaches with procedural structures are usually employed $[8]$ ; they guide managers in establishing each level of the strategic plan so that a strategy can be completely constructed. However, issues such as which items must be discussed in each level of the plan and how to connect the various levels of the plan have not been clearly described. For example, the portfolio matrix approach $[21, 22]$ fails to establish the linkage between the factors that influence the internal and external components of a strategic business unit (SBU) and the factors that influence the whole of the SBU. Difficulties also arise in implementing the evaluation step of the strategic planning process. Since, according to Glueck and Jauch $[5]$ , the managers' past experience is needed to help evaluate the whole circumstance of an SBU using internal and external factors related to the business unit, someone without past experience cannot perform the evaluation. Furthermore, it is often impossible to describe the evaluation process in detail, either verbally or numerically and, hence, the transfer of the knowledge and experiences required for evaluating and selecting strategies usually takes a long time. Therefore, in order to construct a more workable process for conducting strategy evaluation, we have chosen to employ neural networks in conjunction with portfolio matrices.

Neural networks are massively paralleled and interconnected networks of simple elements and their hierarchical organizations. They are intended to interact with the objects of the real world in the same way as biological nervous systems. Recently, neural networks techniques have been harnessed in solving various practical problems, such as pattern recognition, knowledge data bases for stochastic information, optimization computations, robot control, and decision making $[9, 20]$ . However, the literature still lacks useful approaches that employ neural networks techniques in performing strategic planning.

The more uncertain the environment in which a firm operates, the more important the dispersal of investment risks is to the firm. One of the effective techniques developed to cope with the aforementioned concern is linear integer programming. This is “a mathematical procedure for determining optimal allocation of scarce resources, and has found practical applications in all facets of business” [17]. Such a model consists of a linear objective function and a set of linear constraints with integral decision variables. The objective function defines the ‘goal’ we are seeking, such as profit maximization or cost minimization. The set of constraints describes the limitations, physical or financial, which confine us in the goal-seeking exercise. With proper definitions of investment risks and returns, we can construct and solve a linear integer programming model to determine the strategic plans that best utilize a firm’s annual budget to maximize the potential profit generated from implementing these strategic plans.

Here, we employ neural networks techniques to ‘learn’ and ‘mimic’ the process of managers in conducting strategy evaluations, use the neural networks models to designate the suitable strategy position of an SBU in the ‘industry attractiveness-business strength’ (IABS) matrix $[7]$ based on factors considered relevant by the managers, and solve a linear integer program to determine the best budget allocation to the proposed strategies.

## 2. Framework of the approach

Our approach consists of four steps, including selecting a portfolio matrix model, selecting neural networks models, designing questionnaires, and constructing the working models.

## 2.1. Selecting a portfolio matrix model

The various portfolio matrices take into consideration different internal and external factors to describe the whole circumstance of an SBU $[4, 6, 19]$ , hence they actually represent different issues that managers consider important to their firms. Therefore, the selection of a suitable portfolio matrix model is based on managers' preferences. In our study, the managers indicated that they preferred the use of the industry attractiveness-business strength (IABS) matrix. Hence, we decided to adopt this as our model to demonstrate the use of neural networks in performing the task of strategy evaluation.

The IABS matrix was developed by General Electric and McKinsey. It uses the factors related to industry attractiveness to describe the external circumstance of an SBU, and the factors related to competitive advantage to describe the internal circumstance of an SBU. Furthermore, the IABS matrix uses a weighted sum of those factors to evaluate the whole circumstance of an SBU and then indicate the characteristics of the appropriate strategic plans for the SBU.

## 2.2. Selecting neural networks models

Methods used to ‘train’ neural networks for learning are usually divided into two classes: unsupervised and supervised. With unsupervised training models, the training set consists of input vectors only, and the outputs are determined by the networks during the course of the training $[12, 23]$ . On the other hand, for supervised neural networks, after the inputs are applied, the desired responses of the system are provided, and the networks are ‘rewarded’ for accurate classifications and associations or are ‘punished’ for yielding inaccurate responses $[10, 11]$ .

Supervised neural networks are employed here because the purpose of this research is to construct neural networks models that will learn the way that managers determine the whole circumstance of an SBU based on the various internal and external factors.

![](/api/attachments/4FEKVZ47/fulltext/images/e40a4c4498e4fff8df9fa1e7f7efa622debdc095f477d549c9dd173c512cbd5f.jpg)  
Fig. 1. The structure of factors related to competitive advantage.

## 2.3. Designing questionnaires

As indicated earlier, a supervised neural network must be trained so that the relationships between the inputs and the outputs are learned by the neural network. In our work, the inputs are those factors that affect the internal and external circumstances of an SBU and the outputs are the whole circumstance of the SBU.

In order to identify the relevant internal and external factors for the food industry, we first collected the important factors from several strategic planning cases $[1, 14, 15, 18]$ , and consulted with the managers of different departments in the company for their opinions. Then, as shown in Figs. 1 and 2, we established a structure of factors to evaluate the competitive advantage of an SBU and a structure of factors to evaluate the industry attractiveness of an SBU, respectively. Finally, based on these two sets of factors we designed two questionnaires. In each, we randomly designated each factor a numerical ranking value between 1 and 5, and asked the managers of each SBU in the company to provide their evaluations of the whole circumstance based on the internal and external circumstances of the SBU described by the numerical ranking values of the factors.

![](/api/attachments/4FEKVZ47/fulltext/images/5c70371cbbe19e42e3c2ccd612d1ace75c0786958a607d04ab112e17103a0f4e.jpg)  
Fig. 2. The structure of factors related to industry attractiveness.

## 2.4. Constructing the working models

2.4.1. Constructing the neural networks models
Each SBU sees the importance of each factor differently, therefore we constructed two neural networks models, one for evaluating the entire industry attractiveness and the other for evaluating the entire business strength for each SBU. We adopted the four-step procedure proposed by Bailey and Thompson [2, 3] to construct neural networks models as follows:

Step 1: Gather the training set. All the training and testing samples used in the research were obtained from responses to the questionnaires.

Step 2: Select the development environment. Neuralworks Explorer [13] was used to develop the models.

![](/api/attachments/4FEKVZ47/fulltext/images/a4583adc0bcc8c0dca2f355828dc143602d1bf9839aaf2198e62a62cd5709cbe.jpg)  
Fig. 3. The process for constructing the artificial neural networks model.

Step 3: Establish the neural networks. Fig. 3 contains the flow chart of the process for constructing the neural networks. Back-propagation networks were used here because the correctness rate of learning is higher, the application scope is wider, and the success rate of cases is higher than any other supervised neural networks models [16].

Step 4: Test the neural networks. Five thousand time units were used as one testing cycle. After each testing cycle was completed, we evaluated the effectiveness of the neural networks using the correctness rate of classification.

## 2.4.2. Constructing the linear integer programming model

## 2.4.2.1. Assumptions

The following assumptions are made:

1. In this model the investment costs (representing the risks of implementing alternative strategic plans) and the expected profits are the main system parameters.

2. All strategic plans are independent of one another.

3. Each SBU can only implement one strategic plan in one year.

## 2.4.2.2. The linear integer programming model The notations are as follows:

$r_{ij}$ : Unity if the jth strategic plan is implemented at the ith SBU; otherwise it is 0

$P_{ij}$ : The anticipated profit resulted from implementing the jth strategic plan at the ith SBU

$c_{ij}$ : The needed cost of implementing the $j$ th strategic plan at the $i$ th SBU

$u_{i}$ : The upper limit on the total investment amount budgeted to the ith SBU of the firm

f: The overall investment budget of the firm for the year

The profit-maximization linear integer programming model can then be stated as follows:

Maximize

$$
\sum_ {i} \sum_ {j} r _ {i j} P _ {i j}\tag{1}
$$

Subject to:

$$
\sum_ {j} r _ {i j} c _ {i j} \leq u _ {i}, \text {   for   all   } i\tag{2}
$$

$$
\sum_ {i} \sum_ {j} r _ {i j} c _ {i j} \leq f\tag{3}
$$

$$
\sum_ {j} r _ {i j} = 1, \quad \text { for   all } i\tag{4}
$$

$$
r _ {i j} = 0, \text {   or   } 1, \text {   for   all   } i, j\tag{5}
$$

Objective function (Eq. 1) is to maximize the total profit generated by the adopted strategic plans. Constraints (Eqs. 2 and 3) represent the budget limits for the ith SBU and the entire firm, respectively. Constraints (Eq. 4) make sure that each SBU will select exactly one strategic plan to implement. Finally, constraints (Eq. 5) specify the integrality restriction on the values of the decision variables $r_{ij}$ .

## 3. A real-world application

To evaluate the efficacy and applicability of the constructed models, we purposed and implemented them in a strategic planning project at the President Enterprises Corp. in Taiwan. This company, whose headquarters are located at Taiwan's old capital, Tai-nan, was formally based on the concept ‘Beneficial to the Local Community’. Starting with 82 employees and an initial capital of about US\$1 million, the company became not only a remarkable leader in the food industry in Taiwan, but also a global company with multibillion dollars in annual revenue.

In order to collect the data that reflect the managers' strategy evaluation process accurately, we first explained the purpose of this research and the meanings of the questionnaires to the managers of the four SBUs in the firm. Then, we asked the managers to fill out the questionnaires with their evaluations of each SBU based on the internal and external factors faced by the SBU. Finally, we analyzed the collected data and evaluated the accuracy of the responses.

We then constructed a total of eight neural networks models for the four SBUs. For each SBU, we constructed one model for evaluating the industry attractiveness and another for evaluating the business strength. We tested the neural networks models using the inputs and outputs data collected from the questionnaires, and found that the average accuracy rate of classification was up to 96.5%, a highly satisfactory result.

Using the neural networks models, we obtained the strategic positions of these SBUs in the IABS matrix. Based on this, managers of the four SBUs then proposed alternative strategic plans and estimated their costs and potential profits. For example, the strategic position of the third SBU was located at the 'top left' of the IABS matrix, which means that both its industry attractiveness and business strength evaluations are considered 'high' on the three-level high-medium-low scale. Three growth-oriented strategies were proposed for the third SBU – building a new factory in mainland China, building a new factory in the northeastern area of Taiwan, and expanding the original factory.

After completing the study of all four SBUs, we then presented the managers' proposals to the top management of the company. The first SBU (SBU-

1) identified four alternative strategic plans, the second (SBU-2) proposed two, the third (SBU-3) prepared three, and the fourth (SBU-4) submitted two alternative strategic plans. Top management were very concerned with the issue of effectively allocating the firm's annual budget to the proposed strategic plans provided by the SBUs. They charged us with the task of selecting the best strategic plans (one for each SBU).

With the profit estimates and cost structure information (in millions of U.S. dollars) provided by the managers of the SBUs, a corresponding linear integer program was set up as follows:

Maximize

$$
\begin{array}{r l} 1 5 r _ {1 1} + 1 4 r _ {1 2} + 9 r _ {1 3} + 7 r _ {1 4} + 8 r _ {2 1} + 5 r _ {2 2} + 3 r _ {3 1} \\ & + 2 r _ {3 2} + 5 r _ {3 3} + 2 0 r _ {4 1} + 1 5 r _ {4 2} \end{array}
$$

Subject To:

$$
\begin{array}{c} 1 0 r _ {1 1} + 5 r _ {1 2} + 8 r _ {1 3} + 5 r _ {1 4} \leq 9 \\ 3 r _ {2 1} + 2 r _ {2 2} \leq 3 \\ 4 r _ {3 1} + 7 r _ {3 2} + 1 r _ {3 3} \leq 4 \\ 1 3 r _ {4 1} + 1 0 r _ {4 2} \leq 1 0 \\ 1 0 r _ {1 1} + 5 r _ {1 2} + 8 r _ {1 3} + 5 r _ {1 4} + 3 r _ {2 1} + 2 r _ {2 2} + 4 r _ {3 1} \\ + 7 r _ {3 2} + 1 r _ {3 3} + 1 3 r _ {4 1} + 1 0 r _ {4 2} \leq 2 6 \\ r _ {1 1} + r _ {1 2} + r _ {1 3} + r _ {1 4} = 1 \\ r _ {2 1} + r _ {2 2} = 1 \\ r _ {3 1} + r _ {3 2} + r _ {3 3} = 1 \\ r _ {4 1} + r _ {4 2} = 1 \\ r _ {i j} = 0 \text { or } 1, \quad \text { for   all } i, j \end{array}
$$

Solving the above linear inter program using LINDO, a commercial mathematical programming software, we obtained the optimal solution: $r_{12} = r_{21} = r_{33} = r_{42} = 1$ , all other $r_{ij}$ 's = 0, and the maximum profit would be \$42 million. It shows that when SBU-1 and SBU-4 adopts their respective second strategic plans, SBU-2 adopts its first strategic plan, and SBU-3 adopts its third strategic plan, the entire company can maximize the profit resulting from implementing these strategic plans. Notice also that there would be \$7 million left in the annual budget (\$4 million from SBU-1 and \$3 million from SBU-3); this can be put to use elsewhere.

The top management of the company were very pleased and totally agreed with our recommendations. Furthermore, we had cut down the decision-making time for evaluation and selection of strategies from a normal two-month period to only eleven business days, a dramatic savings in time that top management had previously considered impossible. Finally, the proposed approach earned the confidence of top management and will be used by the company to conduct its annual strategic planning in future.

## 4. Conclusion

We proposed a neural networks-based approach to evaluate the strategic positions of the SBUs in a firm. The actual implementation of the approach to a strategic planning project undertaken by a major food company in Taiwan confirmed the efficacy of the approach in assessing the industry attractiveness and business position of the SBUs. With the help of a linear integer programming model, the best set of strategies was identified. The approach also dramatically reduced the time spent in the evaluation and selection of strategies. Although we adopted the IABS matrix as the portfolio model in evaluating the strategic positions of the SBUs in our study, our approach can also work with other evaluation measures.

We found:

1. Neural networks can be used as an effective instrument to capture and aggregate the thinking process and decision process of strategic planning.

2. The mathematical programming technique, if fully understood and utilized by the managers, can provide a powerful tool in selecting the best strategic plans.

3. Future experiments with fuzzy sets and multi-objective mathematical programs may provide the necessary mechanism for handling ‘between-levels’ ranking values and pursuing conflicting strategic goals by a firm.

## References

[1] D.F. Abell, J.S. Hammond, Strategic Market Planning: Problems and Analytical Approaches, Prentice-Hall, New York, 1979.

[2] D. Bailey, D. Thompson, How to develop neural-networks applications, AI EXPERT 5(6), 1990, pp. 38–47.

[3] D. Bailey, D. Thompson, Developing neural-networks applications, AI EXPERT 5(9), 1990, pp. 34–41.

[4] F.W. Gluck, Strategic choice and resource allocation, The Mckinsey Quarterly, Winter, 1980.

[5] W.F. Glueck, L.R. Jauch, Business Policy and Strategic Management, McGraw-Hill, New York, 1980.

[6] A.C. Hax, N.S. Majluf, The use of the growth-share matrix in strategic planning, Interfaces 13(1), 1983, pp. 46–60.

[7] A.C. Hax, N.S. Majluf, The use of the industry attractiveness-business strength matrix in strategic planning, Interfaces 13(2), 1983, pp. 54–71.

[8] A.C. Hax, N.S. Majluf, The Strategy Concept and Process, Prentice-Hall, New York, 1991.

[9] T. Kohonen, An introduction to neural computing, Neural Networks 1, 1988, pp. 3–16.

[10] E.Y. Li, Artificial neural networks and their business applications, Information and Management 27(5), 1994, pp. 303–313.

[11] R.W. Lodewyck, P.-S. Deng, Experimentation with a backpropagation neural network: an application to planning end user system development, Information and Management 24(1), 1993, pp. 1–8.

[12] E. Masson, Y.J. Wang, Introduction to computation and learning in artificial neural networks, European Journal of Operational Research 47(1), 1990, pp. 1–28.

[13] NeuralWorks Explorer, NeuralWare, Inc., New York, 1993.

[14] M.E. Porter, Competitive Advantage, Free Press, Macmillian Inc., London, 1985.

[15] W.E. Rothschild, How to insure the continuous growth of strategic planning, The Journal of Business Strategy 1(1), 1980, pp. 11–18.

[16] D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning internal representation by error propagation, Parallel Distributed Processing 1, 1986, pp. 318–362.

[17] L. Schrage, LINDO: An Optimization Modeling System, fourth edn., The Scientific Press, California, 1991.

[18] F.M. Sherer, Industrial Market Structure and Economic Performance, Rand McNally, IL, 1980.

[19] R.K. Srivastava, R.P. Leone, A.D. Schocker, Market structure analysis: hierarchical clustering of products based on substitution-in-use, Journal of Marketing 45(3), 1981, pp. 38–48.

[20] B. Widrow, D.E. Rumelhart, M.A. Lehr, Neural networks: applications in industry, business, and science, Communications of the ACM 37(3), 1994, pp. 93–105.

[21] Y. Wind, V. Mahajan, Design product and business portfolio, Harvard Business Review 59(1), 1981, pp. 155–165.

[22] Y. Wind, V. Mahajan, D.J. Swire, An empirical comparisons of standardized portfolio models, Journal of Marketing 47(2), 1983, pp. 89–99.

[23] J.M. Zurada, Introduction to Artificial Neural Systems, West Info Access, 1992.

![](/api/attachments/4FEKVZ47/fulltext/images/a702da8b969ae4b5537c93b8fb841181849272469a824090420703124c48b718.jpg)

T. William Chien is Associate Professor of Management, Zicklin School of Business, Baruch College, The City University of New York. He received his B.S. in applied mathematics from National Chiao Tung University in Taiwan, and Ph.D. in management science from the Krannert Graduate School of Management, Purdue University. His research interests are in

logistics, applied mathematical programming, network analysis, and production and operations management. His publications have appeared in Computers and Industrial Engineering, Computers and Operations Research, Decision Sciences, European Journal of Operational Research, Journal of Operations Research Society, Transportation Research, Transportation Science, and elsewhere. He is a member of INFORMS and DSI.  
![](/api/attachments/4FEKVZ47/fulltext/images/3bcea5c7f8a45dcb4bad641f2e7e5ac48738352ca52b9ac9ebf8742dd6912d3b.jpg)

Chinho Lin is Professor of Industrial Management Science, National Cheng Kung University in Taiwan. He has received a B.S. and an M.S. in industrial management from National Cheng Kung University, an M.S. in Operations Research from Columbia University, and a Ph.D. in business administration from The City University of New York. His research interests include maintenance system design, simulations, quality management, inventory control, applications of AI, and manufacturing strategy. His papers have been published in Decision Sciences, International Journal of Production Research, Journal of Operational Research Society, Computers and Industrial Engineering, Microelectronics and Reliability, Applied Mathematical Letters, International Transactions in Operational Research, and elsewhere.

![](/api/attachments/4FEKVZ47/fulltext/images/5781e9e0e72715d51e5d20a07a3e52681aefa0ca0dcc330bffb2391cad13049d.jpg)

Bertram Tan is Professor of Business Administration, National Cheng Kung University in Taiwan. He has received a B.S. and an M.S. in industrial management from National Cheng Kung University. He is a doctoral candidate in MIS at Nova Southeastern University. His current research interests include production and operations management, general management, and management information systems.

![](/api/attachments/4FEKVZ47/fulltext/images/2b33fcea4955161d8af01ec5bd6c3d81f4077124972e77357e7c594d1305a983.jpg)

Wen-Chuan Lee is a doctoral student at the Department of Business Administration, National Cheng Kung University, Taiwan. She has earned a B.S. in industrial engineering from Tunghai University in Taiwan and an M.S. in industrial management from National Cheng Kung University. Her research interests include production and operations management and neural networks.
