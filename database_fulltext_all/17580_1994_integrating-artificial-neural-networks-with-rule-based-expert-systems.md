---
otero_id: 17580
otero_key: "TQUVNDV4"
title: "Integrating artificial neural networks with rule-based expert systems"
authors: "Youngohc Yoon; Tor Guimaraes; George Swales"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90021-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrating artificial neural networks with rule-based expert systems \*

Youngohc Yoon

Southwest Missouri State University, Springfield, MO, USA

Tor Guimaraes

Tennessee Technological University, Cookeville, TN, USA

George Swales

Southwest Missouri State University, Springfield, MO, USA

The Rule-Based (RB) and the Artificial Neural Network (ANN) approaches to expert systems development have each demonstrated some specific advantages and disadvantages. These two approaches can be integrated to exploit the advantages and minimize the disadvantages of each method used alone. An RB/ANN integrated approach is proposed to facilitate the development of an expert system which provides a “high-performance” knowledge-based network, an explanation facility, and an input/output facility. In this case study an expert system designed to assist managers in forecasting the performance of stock prices is developed to demonstrate the advantages of this integrated approach and how it can enhance support for managerial decision making.

Keywords: Artificial neural network, Rule-based approach, Integrated expert system, Financial expert system, Hybrid expert system

![](/api/attachments/TQUVNDV4/fulltext/images/c4f14d17cfb02005a43a62b0d0d4c5175c0a716d574221963477ea1c5426eb11.jpg)

Youngohc Yoon is an assistant professor in the Department of Computer Information Systems at Southwest Missouri State University. She received her M.S. from the University of Pittsburgh and her Ph.D. from the University of Texas at Arlington. She has recently published articles in the Journal of Neural Network Computing and Expert Systems. Dr. Yoon is a member of the Decision Sciences Institute, International Neural Network Society, American Association for Ar tificial Intelligence, ACM SIGBDP, and IEEE Computer Society.

## 1. Introduction

Expert System (ES) technology has earned the attention and commitment from business and information systems managers, as well as knowledge engineers. They have become critical components in many products and services, as well as in many decision-making processes $[17]$ . The extensive list of ES success stories is widely known and well documented in the literature. Leading business organizations in this area have now implemented ES for a wide variety of applications which range in cost from a few thousand dollars to a few million dollars $[20]$ .

As the size of the investment and company

![](/api/attachments/TQUVNDV4/fulltext/images/22c3b2628b158701591734b907e26ab07b3d5a780355ece010a0c9f759c9558b.jpg)

Tor Guimaraes holds the J.E. Owen Chair of Excellence in IS at Tennessee Technological University. In addition to his Ph.D. in MIS from the University of Minnesota, he has an M.BA. from the California State University, Los Angeles. He was a Professor and Chairman of the MIS Department at St. Cloud State University. Before that, he was an Assistant Professor and Director of the MIS Certificate Program at Case-Western Reserve University. He has spoken at

numerous meetings sponsored by professional organizations including ACM, IEEE, ASM, DPMA, INFOMART, and Sales and Marketing Executives. He has consulted on several IS topics with many leading organizations including TRW, American Greetings, AT & T, IBM and the Department of Defense. He has published over forty articles in leading journals such as Communications of the ACM, MIS Quarterly, OMEGA, Computers and Operations Research, Information and Management, and Database.  
![](/api/attachments/TQUVNDV4/fulltext/images/8fc502f24c4977d8f99fe7beefa0625081e648ef8034f95b9d0a8e2a5e2ffac0.jpg)

George S. Swales, Jr. is an associate professor of finance and acting department head of the Department of Finance and General Business at Southwest Missouri State University. He received his bachelor and MBA degrees from George Mason University and his Ph.D. from the University of Arkansas. His recent publications have appeared in the Financial Analysts Journal, Journal of Finance and Economics, Business Insights, Regional Business Review, and the Southern

Ohio Business Review. Dr. Swales is a member of the Financial Management Association and the Mid-South Academy of Economics and Finance.

Correspondence to: Tor Guimaraes, J.E. Owen Chair of Excellence in IS, Tennessee Technological University, P.O. Box 5022, Cookeville, TN 38505, USA.

dependence on ES grows, users become more demanding and managers expect improved return on investment in ES technology. As a result, knowledge engineers are forced to constantly improve the effectiveness of systems and the efficiency of the ES development process [39]. An important challenge for ES developers today is to ensure the quick construction of ES which are sophisticated, economical, evolvable, and most important, able to satisfy user requirements.

Rule-Based (RB) expert systems emerged in the early 1970s, have widespread use and represent the bulk of ES applications today. New promising approaches to ES development have been developed in the last few years to circumvent some of the limitations associated with the RB development approach. Appropriately selecting the approach to be used is a key factor to success [38]. A few approaches have been developed to overcome the difficulties involved in generating the knowledge base for ES developed with the RB approach. For example, automatic knowledge acquisition tools, were developed to elicit relevant domain knowledge from experts [21]. These tools have proven somewhat useful for creating and maintaining an expert system, but they are unable to totally remove the major obstacle for the RB approach: the difficulty of generating a knowledge base. Inductive methods have also been developed to derive rules from examples and thereby automate the generation of the knowledge base [23,28,32]. However, the performance of inductive approaches needs to be improved in order to provide more accurate results, especially under noise and incomplete data. Among these new approaches to ES development, one of the most promising and widely used is the Artificial Neural Network (ANN) approach which is one of the two methods used to develop the hybrid (integrated) ES in this case study.

The strengths and limitations of the two methods (RB and ANN) encouraged the exploration of an integrated approach to ES construction. By highlighting the advantages and overcoming the disadvantages of each method used alone, the hybrid approach can be beneficial to the development of more powerful ES to model expert thinking and support managerial decision-making processes. The following sections of this article will respectively discuss the motivation for a hybrid approach (RB and ANN) to ES development, illustrate the development of an ES with a case study, describe the hybrid ES components, discuss the results from ES performance evaluation, and, finally, advance some conclusions and recommendations for ES developers and managers to proceed.

## 2. Motivating a hybrid approach to ES development

The following discussion of the contrasting characteristics of the two development approaches (RB and ANN) suggest that an integrated approach could be beneficial to ES development by highlighting the advantages and overcoming the disadvantages of each method used alone.

The primary advantage of RB expert systems, compared to their ANN counterparts, is the “readability” of the process the system used to make decisions. Knowledge embedded in the system is easy to read and easy to understand since it uses explicit rules (condition-and-action relationships). Providing explanations for the decisions made by an ES developed with the RB approach is also easy since the antecedents of rules specify exactly what conditions activate the rule $[7]$ . Furthermore, in the RB case the ES can be easily programmed to display the rules and variables that the system uses to reach a conclusion in order to explain the reasoning process.

However, generation of a knowledge base has proved to be a difficult task in ES developed with the RB approach due to their inherent requirement for explicit rules. This problem arises because much of human knowledge is implicit $[27]$ , especially expert knowledge. A domain in which knowledge is implicit does not allow for clear and complete decision rules explicitly defined $[25,40]$ . Although implicit knowledge can be cast into explicit rule(s), such knowledge acquisition process can lead to loss of critical information. Furthermore, domain experts are often unable to articulate their reasoning process due to the implicit nature of their knowledge. Under these circumstances, a knowledge engineer, who is generally a novice in the domain, must obtain additional knowledge through self-study and observations, which takes an inordinate amount of time and effort. Moreover, a sophisticated knowledge base needs to be evolved from a simple one by adding knowledge learned from experience [14]. Unfortunately, a RB expert system is incapable of learning new knowledge from experience [4].

In lieu of extracting explicit rules from domain experts through a series of interviews and/or observations, the ANN approach uses a learning algorithm to automatically extract the functional relationships between input and output presented in a set of historical data (called training examples) and encodes it in connection weights $[35,6]$ . An ANN has proven to be capable of extracting the mapping from input to output, although the data may be noisy, incomplete, and impartial $[16]$ . In a comparison with an inductive method, an ANN demonstrated slightly higher accuracy than the ID3 inductive method under noise and missing data $[24]$ . If the training examples are readily available, an ANN is also capable of capturing a large volume of information in a shorter period of time (hours compared to several months or years of knowledge acquisition for the RB approach) $[11]$ . Furthermore, an ANN approach uses a distributed representation in which a single concept is distributed over many computational weights in a network $[9,12,31]$ . An individual weight in a network does not contain a condition-action relationship; however, a number of weights and units represent implicit decision rules. Thus, an ANN provides a high degree of fault tolerance since damage to a few units and weights is not fatal to the overall network performance $[18,22]$ . These features indicate that, if the number of data points to be analyzed or the range of values for each data point is quite large, or the reasoning about the data is fuzzy and ill-defined, an ANN is a viable alternative method to generate a knowledge base.

Unfortunately, reading and understanding the knowledge is difficult in an ANN system since knowledge is distributed over the entire network. Profiling the characteristics of input variables and explaining why a particular conclusion is reached by an ANN system is also difficult because it does not employ explicit decision rules $[3,13,37]$ . This is a major limitation since the ability to explain the reasoning process is among the most innovative and important qualities of expert systems $[36]$ .

Given the complementary strengths of the RB and ANN approaches, a hybrid development approach becomes quite promising. To empirically test this hybrid (integrated) approach, a case study is presented next. The reader should keep in mind that the primary objective of this research is to demonstrate the technical and operational feasibility of a hybrid ES. To develop this hybrid ES as an effective business tool for predicting company stock performance is only a secondary objective in this case.

## 3. The hybrid (integrated) ES: a case study

In this case study the hybrid approach is applied to the development of an Integrated Finance Expert System (IFES) for the prediction of stock price performance. This financial problem involves the interaction of many diverse variables whose relationships are unclear, unstructured, and ill-defined, making the prediction of the outcome very difficult. The difficulty in outcome prediction is compounded by the fact that many of the variables used in forecasting are outside the direct control of the investors. On the other hand, some variables, such as those involving a firm's financial data, are directly observable. Both of these sets of variables may have a relatively strong association with stock price performance, which may not be consistent over time.

The large number of participants in the market, together with the speed and quality of information flow, contribute to the general “efficiency” of stock markets. Markets are said to be efficient if security prices fully reflect, quickly and accurately, all known information. Many attempts have been made to build models that assist investors in their decision-making in today’s relatively efficient stock market.

The ES in this case attempts to predict the performance of a firm's stock price with its financial ratios. The data set for this study was gathered from two information sources that are frequently used by investors: The Fortune 500 [5] and Business Week's "Top 1000" [33]. These sources provided the total return (dividends paid and stock price appreciation) and market valuation data, respectively, for well known companies. In practice, a stock's total return and market valuation are commonly used by investors and financial analysts as company stock performance measures and for predicting future earnings, dividends, and stock prices. Therefore, we can safely claim that the ratios used for this study are well known and widely used in financial management and investment analysis. Further, these ratios are discussed in detail in the finance literature $[1,2,26]$ .

The original data set for this study was comprised of the top 30 and the bottom 30 of the Fortune 500 and the Business Week Top 1000 lists of companies for a total of 120 organizations. Several companies were dropped due to missing data reducing the sample size to 108. That was deemed dangerously low, possibly compromising the validity of the study. Therefore, the next 35 companies at the top and the next 35 at the bottom of the Fortune 500 list were included in the sample. Again, due to missing data several companies were eliminated. The final sample composition is 56 companies from the top and 47 from the bottom of the Fortune 500 list, plus 24 from the top and 24 from the bottom of the Business Week Top 1000 list, for a final total of 151 organizations used in this study.

For the 151 companies in the sample, thirteen ratios which are commonly used to determine a firm's financial position were calculated from data available on COMPUSTAT. Of the 13 ratios, four were found to be significant in the SAS Stepwise Discriminant procedure. The four ratios included to develop the model are the current ratio (CR), return on equity (ROE), price to earnings (PE), and price to sales (PS). These ratios, of course, are quantitative and continuous variables. The CR is a measure of liquidity and is the prime indicator of the firm's ability to meet its short-term obligations. ROE, PE, and PS are measures commonly used in investment decisions. Both the PE and PS ratios indicate how much investors should be willing to pay for each dollar's worth of earnings or sales.

The architecture proposed for this hybrid ES consists of three modules: a knowledge base with a computation engine, an explanation facility, and an input/output facility, as shown in Figure 1. The knowledge base is an ANN network whose connection weights specify the decision rules in an implicit manner. The computation engine is an ANN system whose purpose is to compute an output value when given the list of input values. We chose to use ANN instead of linear regression method to build a model because ANN often outperforms regression and/or discriminant analysis methods [3,19,30]. If the explanation capability is the most crucial aspect in any system, the linear regression or discriminant analysis method would have been our choice. However, in general, explanation of the system's operation is less important than high performance. Therefore, we chose a technique which would provide us with high performance in predicting the stock price performance. As discussed later, in our study the ANN outperformed discriminant analysis. The explanation module is a RB system in which knowledge implicitly encoded in the knowledge-based network has been translated into an "if-then" format. The Input/Output (I/O) facility provides interface with a user, the computation engine, and an explanation facility. The I/O facility is capable of interpreting numeric output values transferred from the computation engine to meaningful conclusions.

![](/api/attachments/TQUVNDV4/fulltext/images/83dfb69314d005eac51a7f3cba0e7ecf74b2b54faa4da22f4dfa9bf56eb8ca72.jpg)  
Fig. 1. Architecture of IFES.

The methodologies used for developing the three components (the knowledge-based network with an computation engine, the explanation facility, and the I/O facility) for the IFES are discussed in more detail in the following sections.

## 3.1. Knowledge base and computation engine

This part describes the structure and training process of a network and the computation engine for the IFES. An ANN technique is mainly employed to generate the knowledge-based network and the computation engine.

## 3.1.1. The structure of the knowledge base

In general, the ANN component is structured as a multi-layered network consisting of computational units connected by links with variable weights. Each unit represents a variable in a problem space (and is a node in the network), and each connection weight represents the strength of association between variables.

![](/api/attachments/TQUVNDV4/fulltext/images/e113f55bbbf1da07559d36bb4078772ae0482e4bad534144340a1c415a70f7e1.jpg)  
Fig. 2. Knowledge-based network of IFES. Four input units represent four independent variables and two output units represent the two possible outcomes of the model. The number of hidden units is arbitrarily chosen to represent a knowledge-based network and is usually determined by a series of experiments to obtain the best results.

The knowledge base of the IFES is a multi-layered network which consists of an input layer, one hidden layer, and an output layer, as shown in Figure 2. The input layer contains four input units to represent the four input variables, respectively. The output layer consists of two output units to represent the two distinct outcomes of the system. Although two possible outcomes could be represented by one output unit with the values scaled from 0 to 1, two output units are often chosen to represent two outcomes [8]. In this study, two output units were employed to ease the analysis of the effect of each independent variable on each outcome for developing the IFES explanation facility. Hidden units were used to augment the input data when computing the function from input units to output units [8,34]. Note that the number of hidden units in Figure 2 is arbitrarily chosen to represent a knowledge-based network and it is empirically determined to produce the best possible result. The Kolmogorow's theorem states that any real function can be implemented by a three layered network; however, a method of finding such a network is not known yet [10]. Therefore, researchers search for an optimal network by testing many different types of networks. A four-layered network often outperformed a three-layered one [30]. This study now uses the three-layered network employing a single hidden layer not because of the theorem, but to simplify the process of rule extraction from a trained network. Section 4.1 discusses the findings of an optimal number of hidden units in this application.

## 3.1.2. The learning process for building the knowledge-based network

This study was conducted on an ANN simulator developed by the authors with C programming language and run under the VAX 11/750. The back propagation algorithm was chosen to compute the connection weights for the network, due to its simplicity and its usually good performance [29]. Back propagation uses a gradient descent algorithm by which network connection weights are iteratively modified to reduce the overall mean square error between desired and actual output values for all output units over all input patterns. For the development of the knowledge-based network, the data set of 151 samples was randomly divided into two sets using a 50:50 ratio. One set of 76 companies was used to build the model, and the other set of 75 companies was used to test the model. The 50:50 ratio has been often used in developing an ANN application and is considered to be an appropriate ratio for the holdout sample approach [8].

In this application, a number of epochs for all 76 companies were repeated for 2500 times. An epoch is considered completed after the network sees all of the input and output pairs for all 76 companies. In order to avoid the problem of overfitting the network, the iterative learning process was terminated when the change in the overall mean square error between desired and actual output values over all 76 input patterns became negligible. Through the learning process, the knowledge about the mapping from input to output which the ANN has learned to compute is encoded in the magnitudes of the weights for the connections.

## 3.1.3. The computation engine

The computation engine for the IFES is also the back propagation algorithm, excluding the process of propagating the amount of error back to the connection weights. When using a network in testing mode or in actual practice, the computation engine receives the input values from the input facility and proceeds to calculate the output value as follows. The computation engine initially fixes a vector of the four input values as the output vector of input units. The output vector propagates forward to each of the hidden layers in turn, and then to the output layer as described earlier in the section on the learning process for building the computation engine. The output values of each layer are determined by the output function. Finally, the output values of the final layer are transferred to the output facility to determine the final conclusion by the system.

## 3.2. The explanation facility

This part presents the method designed to extract rules from the network in order to provide the needed explanation capability. A description of the interpretation method is followed by the explanation of generating rules using information obtained from the method.

## 3.2.1. Interpretation method

In the interpretation method used in this study, the strength of the relationship between each input and each output variable is measured by the following statistic:

$$
R S _ {j i} = \frac {\sum_ {k = 0} ^ {n} \left(W _ {k i} ^ {*} W _ {j k}\right)}{\sum_ {i = 0} ^ {m} A B S \left(\sum_ {k = 0} ^ {n} \left(W _ {k i} ^ {*} W _ {j k}\right)\right)},\tag{1}
$$

where $RS_{ji}$ is the relative strength between the ith input and the jth output variable, $W_{ki}$ is the weight between the kth hidden unit and the ith input unit, and $W_{jk}$ is the weight between the jth output unit and the kth hidden unit. In multivariate analysis, this approach is used frequently to determine the proportion of variation of one variable in relation to all the others [15].

This statistic measures the strength of the relationship between the ith input and the jth output variable to the total strength of all of the input and output variables. The numerator measures the relationship between the ith input variable and the jth output variable and can be either positive or negative depending on the weights. The denominator measures the “total” relationship or “total strength” between all of the input and output variables. The absolute value in the denominator is necessary because the positive relationships should not cancel out the negative relationships between the input and output variables. Thus this descriptive measure can be thought of as the strength between an input variable and an output variable in relation to all the input variables and an output one.

```txt
RULE EXPLAIN-ROE-EFFECT
IF ROE > 0.0
AND
CONCLUSION IS WELL-PERFORMING-FIRMS
THEN EFFECT-OF-ROE := WELL-OUTPUT * ROE *
RS-ROE-WELL / SUM-OF-RS
AND
DISPLAY POS-ROE-EFFECT
DISPLAY POS-ROE-EFFECT
The input variable, ROE, has increased the output value of the output unit representing "well-performing-firms" by [EFFECT-OF-ROE]
```  
Fig. 3. Rule of the explanation facility.

## 3.2.2. Explanation approach

An approach to providing an explanation involves the development of a rule-based system using the relative strength extracted from a network. The effect of the ith input variable upon the output value of the jth output unit, $E_{ji}$ , at a certain situation is computed according to

$$
E _ {j i} = O _ {j} * \frac {\left(I _ {i} * R S _ {j i}\right)}{\sum_ {k = 0} ^ {n} \left(I _ {k} * R S _ {j k}\right)},\tag{2}
$$

where $O_{j}$ is the output value of the jth output unit, $I_{i}$ is the input value of the ith input variable, and $RS_{ji}$ is the relative strength between the ith input unit and the jth output unit. Rules are written to suggest which output value ( $O_{j}$ ) and relative strength ( $RS_{ji}$ ) are to be used in computing the effect, $E_{ji}$ . Once the value of the effect is computed, rules display the value with interpretation. An example is presented in Figure 3. The “RULE EXPLAIN-ROE-EFFECT” states that, if an input variable return on equity (ROE) is non-zero and the system’s conclusion is “well-performing-firms”, then the effect of the input variable is computed with the output value of the output unit representing “well-performing-firms”, the input value of the variable ROE, the relative strength of ROE to the output unit, and the summation of weighted relative strengths.

The explanation facility also generates a graphic display showing the cumulative effects of all input variables on the output value of the output unit representing the system's conclusion. In this section, an example of the IFES graphical display is not presented since the graph may be more understandable once the readers know the relative strengths of each input variable in this application. Thus, the presentation of the example of a graphical display is withheld until the values of relative factors are analyzed in section 4.2.

## 3.3. The I/O facility

For the inquiry process, the sequence of questions is predetermined. The input facility asks a user to supply the value of each input variable. The question is accompanied by the definition of each variable to assist a user in understanding the variable. Once the values of the four input variables are known, the input facility transfers them to the computation engine that is responsible for computing the value of output units.

When the output facility receives the values for the two output units from the computation engine, the conclusion (that the input describes a firm whose stock performs well or performs poorly) is determined by which output unit has a higher output value for the given set of input values. The rule “RULE-DETERMINE-CONCLUSION” in Figure 4 states that the value of an output unit should be greater than 0.5 and greater than that of the other output unit for

<table><tr><td>RULE</td><td>DETERMINE-CONCLUSION</td></tr><tr><td>IF</td><td>WELL-OUTPUT &gt; POOR-OUTPUTANDWELL-OUTPUT &gt; 0.5</td></tr><tr><td>THEN</td><td>CONCLUSIVE IS YESANDCONCLUSION-NAME IS WELL-PERFORMING-FIRMS</td></tr><tr><td>RULE</td><td>CHECK-DEFINITIVE</td></tr><tr><td>IF</td><td>CONCLUSIVE IS YESAND(ABS (WELL-OUTPUT - POOR-OUTPUT) &gt; 0.3)</td></tr><tr><td>THEN</td><td>CONCUSION-CERTAINTY IS DEFINITIVE</td></tr><tr><td>RULE</td><td>CHECK-VERY-LIKELY</td></tr><tr><td>IF</td><td>CONCLUSIVE IS YES AND(ABS (WELL-OUTPUT - POOR-OUTPUT) &lt; 0.3 ANDABS (WELL-OUTPUT - POOR-OUTPUT) &gt;= 0.2)</td></tr><tr><td>THEN</td><td>CONCUSION-CERTAINTY IS VERY-LIKELY</td></tr></table>

Fig. 4. Rules of the output facility.

IFES to reach a conclusion. Two output units are competing with each other to respond to the incoming input pattern; thus, when the output value of an output unit is greater than 0.5, that of the other is less than 0.5. However, when the output values of both units are less than 0.5, the system cannot reach a conclusion and fails to classify the given input pattern.

The certainty level of conclusions is dependent upon the difference of the output values of the two output units. The “RULE CHECK-DEFINITIVE” and “RULE CHECK-VERY-LIKELY” in Figure 4 determines the certainty of the system’s conclusion. The “RULE CHECK-DEFINITIVE” states that the system’s conclusion is definitive when the difference between the output values of the two output units is greater than 0.3. The “RULE CHECK-VERY-LIKELY” states that the conclusion is very likely when their difference is less than 0.3 and greater than 0.2. These ranges are determined by the domain expert. After carefully examining the output values of the 75 test cases, our domain expert established the certainty level to a system’s conclusion. If the difference between the output values of two output units is greater than 0.3, the system’s conclusion is definitive. If the difference is less than 0.3 and greater than 0.2, the conclusion is very likely. When the difference is less than 0.2, the conclusion is likely.

## 4. ES performance evaluation

This section presents the results obtained from an evaluation of the trained network and the interpretation method. A network performance is largely affected by the number of hidden units. A series of experiments was conducted to analyze the effects of varying the number of the hidden units on the network performance. The findings are presented in this section.

## 4.1. Results of knowledge-based network

The performance of the system was tested with the data set of 75 companies. The effect of the number of hidden units on the network performance was tested. In this application the performance of the three layered ANN improved by increasing the number of hidden units up to a certain limit (7 hidden units). However, as the number of hidden units was increased beyond the limit, the performance of the model started declining in terms of the percentage of correct classification of observations in the test data set (Figure 5).

The final ANN model that was chosen as the IFES knowledge-based network is a three-layered network which consists of 4 input units, 7 hidden units, and 2 output units. Given the complexity of predicting stock price performance and the wide variations in the individual cases of the testing data, the achieved correct classification of 76% percent was deemed to be high. A final test of performance was a comparison of the ANN model results against a Multivariate Discriminant Analysis model which was able to produce 63% percent correct classification. Therefore, we consider the system a good predictor of stock price performance.

## 4.2. Results of interpretation method

The interpretation method was applied to the chosen knowledge-based network (a three-layered network) in order to determine the strength of the relationship between each of the four input and two output values. The bar graph in Figure 6 represents the relative strength of the relationship between each input unit and the output unit that represents firms whose stock performs well.

The results of the interpretation method corroborates the importance of ROE as a major positive indicator of stock price performance. In practice, ROE is frequently used by stockholders to provide an indication of how effective a firm's management is. If a company's ROE is below the industry average, or is on the wane, stockholders would be reluctant to purchase the stock. If, on the other hand, ROE is above the industry average and/or is steadily increasing, investors would judge this to be a desirable situation since management seems to be effectively accomplishing the critical objective of maximizing stockholder wealth.

![](/api/attachments/TQUVNDV4/fulltext/images/594e186a6e4778a757dbc6775b21fa7462e9eeccc64f38d8189b9328e3661d6f.jpg)  
Fig. 5. Effect of varying the number of hidden units on performance in a three-layered network.

![](/api/attachments/TQUVNDV4/fulltext/images/68d77d08ee572454c93f209a41a554649fa59121f0d1cb83541e9a615a2054e4.jpg)  
Fig. 6. Relative strength between each input variable and the output unit representing well-performing firms.

As said earlier, the PE and PS variables are also recognized in practice as positive indicators of stock price performance. There is a direct relationship between changes in earnings and changes in stock prices. Increases in earnings generally result in increases in the price of a firm's stock. Likewise, a decrease in earnings is usually related to stock price declines. In a similar manner, especially for new firms without an established earning record or in the case of smaller firms, sales are a particularly important consideration to the investor. New firms are likely to have relatively high start-up costs or higher selling expenses than established firms, and little or no net income. Consequently, someone contemplating investment in such a firm looks closely at sales as a predictor of future sales and earnings potential.

Contrary to expectations, the current ratio (CR) variable had a negative coefficient. The current ratio is a measure of liquidity and indicates the firm's ability to meet its short-term obligations. A likely explanation for the negative coefficient is that the data base used for this study consisted primarily of large firms which generally have ready access to money and capital markets. Investors, realizing that the larger companies have this advantage are likely not to value stringent short-term liquidity requirements for large firms as they would for smaller firms. In fact, the opposite is likely to be true. Excess liquidity may indicate too much cash or inventory at hand and, therefore, suggest unwise management of current assets.

Since two output units compete with each other, the relative strength between each input variable (CR, ROE, PE, PS) and the output unit representing poorly-performing-firms is the opposite of those values shown in Figure 6 which are related to well-performing firms. The absolute values of relative strength between an input and an output variables are almost equal for poorly-performing and well-performing firms, but the signs are opposite.

A possible limitation of this interpretation method is that for a more complicated network (four layers or more), the results reliability may decrease. Further, as the network complexity increases, the statistic measures of relative strength between input and output variables become less intuitive. However, in the context of this study, this interpretation method provides good estimates of the relative strength of association between input and output variables. A domain expert asked to critique these results largely agrees with the relative strength between input and output variables except for the negative coefficient for current ratio which was explained above. Thus, these measures of relative strengths were used to develop the rule-based explanation facility of IFES which consisted of 12 rules.

The explanation facility also utilized these relative strengths between input and output variables to present a graphical display of the output value as a function of cumulative input values. An example of the change in the output values with each additional input value is presented in Figure 7. This graph demonstrates the value of the output unit representing firms whose stock performs well. The output value was decreased by CR (X1) since its input value was moderate and its relative strength was negative, and it was substantially increased by ROE (X2), whose relative strength was fairly large although input value was moderate. The output value was slightly increased by PE (X3) and PS (X4), whose relative strengths and input values are small. With the display of each input variable's effect on the output value, the explanation facility enables a user to understand how the system reaches a particular conclusion.

![](/api/attachments/TQUVNDV4/fulltext/images/c010a192495b887f67238ab82fcccb00558e6162ae45336afc1f46dbb66550f0.jpg)  
Fig. 7. The graph represents the output value as a function of additional information added in the sequence of CR, ROE, PE, and PS.

## 5. Conclusions and recommendations

The integration of a rule-based system and an artificial neural network has enabled us to construct an expert system that consists of a knowledge-based network, an explanation facility, and an input/output facility. The knowledge base of IFES is generated with experiential data instead of a series of interviews with a domain expert. The relatively good success of this system indicates that it is possible to automatically construct a knowledge base from historical data, easing the task of constructing an ES. The ANN learning algorithm can learn the mapping from input to output, even if it is non-linear, fuzzy, and imprecise. With the use of ANN, the capability of ES is no longer limited to well-defined problems which provide the complete specifications of decision rules. The benefits of an expert system can be expanded to ill-defined problem areas that high-level management frequently confronts, such as the prediction of a firm's bankruptcy and bond ratings.

On the other hand, the explanation facility of the IFES utilizes a set of explicit rules to provide a clear explanation of the system's conclusion. Such a facility enhances the quality of the IFES by addressing the ANN's inability to justify the reasoning process. Therefore, integrating these two techniques has clearly been shown to be very useful in building an ES to effectively support managerial decision-making and improve the productivity of managerial tasks where managers need to understand the ES reasoning process.

IFES currently is producing the correct classification of 76 percent of the cases when forecasting the performance of stock price. The plan for the next phase of the system development is to improve the performance of the knowledge-based network by training with a larger data set and to expand the capability of its input/output facility by incorporating hypertext and/or a natural language facility, thus providing a more user-friendly interface.

ES developers should seriously consider using this RB/ANN hybrid approach to ES development for difficult problem domains where RB/ANN complementary strengths are most suitable: difficult to find experts, difficult for experts to express their knowledge, available input data to build the ANN network, need to justify (explain) the ES process used to make a decision, etc.

An integrated system can be developed in various ways. The easiest way to build an integrated system is to utilize a commercial ANN simulator to train a network and save the set of weights in a file. The developers then can utilize a supplementary facility provided through the ANN simulator to read the weight data. In order to interpret the set of trained weights and develop the I/O and explanation facilities, developers need to write their own codes embedded in the supplementary facility. For example, Brain Maker Professional provides a supplementary system (called Run-Time System), programmed in C, to interface with ANN trained networks; thus, developers can easily add additional code to build I/O and explanation facilities. However, many other simulators provide only the run-time library (executable code only) to read the trained weights. In this case, developers should write separate programs to implement the I/O and explanation facilities, and then link them to the run-time library.

An alternative way to develop an integrated system is to use a commercial simulator and write the necessary programs for the supporting facilities and for reading the ANN trained weights. The difficulty of this approach is that developers must know the file formats used by the commercial simulator in order to correctly import the weights into their program, but some vendors are not willing to release this information.

Finally, the developers can always construct a complete system by themselves, which would involve writing source code for simulating an ANN system as well as for the supporting facilities. The difficulties of interfacing with commercial software would be eliminated; however, this approach will take considerable time and effort.

The evidence from this case study amply supports the concept of hybrid ES. Managers responsible for ES development resources should encourage experimentation in this area with different domains and development techniques. Very likely, in the future, ES development facilities will provide more than one approach to development (RB, ANN, Model-Based Reasoning, Case-Based Reasoning, etc.) in an integrated fashion. Meanwhile, companies willing to experiment in this area are likely to gain significant benefits. A whole new set of knowledge domains can now become unlocked by the use of hybrid ES.

## References

[1] E.F. Brigham and L.C. Gapenski, Financial Management: Theory and Practice, Dryden Press, Sixth Ed. (1991) 874–913.

[2] J.B. Cohen, E.D. Zinbarg and A. Zeikel, Investment Analysis and Portfolio Management, Richard D. Irwin, Inc., Fifth Ed. (1987) 335–367.

[3] S. Dutta and S. Shekhar, Bond rating: a Non-Conservative Application of Neural Networks, Proceedings of the IEEE International Conference on Neural Networks (July 1988) II443–450.

[4] M.W. Firebaugh, Artificial Intelligence: Knowledge-based Approach, Boyd & Fraser Publishing Co., Boston (1988).

[5] Fortune 500, Fortune Magazine (April 23, 1990) 346–364.

[6] S.L. Gallent, Connectionist Expert Systems, Communication of the ACM 31, Nr.2 (February 1988) 152–169.

[7] J. Giarratano and R. Riley, Expert Systems: Principles and Programming, PWS-Kent Publishing Co., Boston (1989) 31.

[8] R. Gorman, and T. Sejnowski, Analysis of Hidden Units in a Layered Network trained to Classify Sonar Targets, Neural Networks 1, Nr. 1 (1988) 75–89.

[9] S. Grossberg, How does a Brain build Cognitive Code? Psychological Review 87, (1980) 1–51.

[10] R. Hecht-Nielsen, Neurocomputing, Addison-Wesley Pub. (1990) 122–123.

[11] D. Hillman, Integrating Neural Nets and Expert Systems, AI Expert (June 1990) 54–59.

[12] G. Hinton, L. McClelland and D. Rumelhart, Distributed representations. In D.E. Rumelhart & J.L. McClelland (eds.), Parallel distributed processing: Exploration in the microstructure of cognition, MIT Press, Cambridge (1986) 77–109.

[13] W. Hutchison and R. Kenneth, Integration of Distributed and Symbolic Knowledge Representation, Pro-

ceedings of the IEEE International Conference on Neural Networks (June 1987) II395–398.

[14] P. Jackson, Introduction to Expert Systems, Addison-Wesley Publishing Co., Reading (1986).

[15] R.A. Johnson and D.W. Wickern, Applied Multivariate Statistical Analysis, Prentice Hall (1982).

[16] T. Kohonen, An Introduction to Neural Computing, Neural Networks 1, Nr. 1 (1988) 3–16.

[17] J. Liebowitz, Introducing Expert Systems into the Firm, Expert Systems for Business and Management, Englewood Cliffs, N.Y.: Yourdon Pres (1990) 1–12.

[18] R. Lippmann, An Introduction to Computing with Neural Nets, IEEE ASSP Magazine (April 1987) 4–22.

[19] R.P. Lippmann and B. Gold, Neural Net Classifiers Useful For Speech Recognition, In Proceedings of IEEE International Conference of Neural Networks (June 1987) 417–425.

[20] M. Lu and T. Guimaraes, Expert Systems Project Selection and Development Strategies, Systems Development Management (December 1988). Reprinted in Journal of Information Systems Management (Spring 1989) and Expert Systems (Summer 1989).

[21] S. Marcus (ed), Automating Knowledge Acquisition for Expert Systems, Kluwer Academic Publishing Co., Boston (1988).

[22] J. McClelland, D. Rumelhart and G.E. Hinton, The Appeal of Parallel Distributed Processing, In D.E. Rumelhart & J.L. McClelland (eds.), Parallel distributed processing: Exploration in the Microstructure of Cognition, MIT Press, Cambridge (1986) 3–44.

[23] R. Michalski and R. Chilausky, Knowledge Acquisition by Encoding Expert Rules versus Computer Induction from Examples: a case study involving soybean pathology, International Journal of Man-Machine Studies 12 (1980) 63–87.

[24] R. Mooney, J. Shavlik, G. Towell and A. Gove, An Experimental Comparison of Symbolic and Connectionist Learning Algorithms, Proceedings of IJCAI (1989) 775-780.

[25] C. Negoita, Expert Systems and Fuzzy Systems, Benjamin Cummings, Menlo Park (1985).

[26] G.E. Pinches, Essentials of Financial Management, Harper Collines Pub., Fourth Ed. (1992) 641–651.

[27] M. Polanyi, Personal Knowledge, University of Chicago Press, Chicago (1958).

[28] J.R. Quinlan, Learning Efficient Classification Procedures and Their Application to Chess End Games, In S. Michalski, R.S., Carbonell, J.O., and Mitchell, T.M. (eds.), Machine Learning: An Artificial Intelligence Approach, Tioga Publishing Co., Palo Alto (1983) 463–482.

[29] D. Rumelhart, G. Hinton and R. Williams, Learning Internal Representation by Error Propagation, In D.E. Rumelhart & J.L. McClelland (eds.), Parallel distributed processing: Exploration in the microstructure of cognition, MIT Press, Cambridge (1986) 318–362.

[30] A.J. Surkan and J.C. Singleton, Neural Networks for Bond Rating Improved By Multiple Hidden Layers, Proc. IEEE International Conference on Neural Networks (1990) 11157–162.

[31] H. Szu, Three Layers of Vector Outer Product Neural Networks for Optical Pattern Cognition, SPIE Optical and Hybrid Computing 634 (1986) 312–330.

[32] K.Y. Tam, Automated Construction of Knowledge-Based From Examples Information System Research 1, Nr. 2 (1990) 144–167.

[33] Top 1000: America's Most Valuable Companies, Business Week, special issue (1989) 166–219.

[34] D. Touretzky and D. Pomerleau, What's hidden in the hidden layers? BYTE (August 1989) 227–233.

[35] R. Trippi and E. Turban, The Impact of Parallel and Neural Computing on Managerial Decision Making, Journal of Management Information Systems 6, Nr. 3 (1989/90) 65–84.

[36] D. Waterman, A Guide to Expert Systems, Addison-Wesley Publishing Co., Reading (1986) 28.

[37] Y. Yoon, R. Brobst, P. Bergstresser and L. Peterson, A Desktop Neural Network for Dermatology Diagnosis, Journal of Neural Network Computing 1, Nr. 1 (1989) 43–54.

[38] Y. Yoon, T. Guimaraes, Selecting Expert System Development Techniques, Information & Management 24, Nr. 4 (1993) 209–223.

[39] Y. Yoon, T. Guimaraes, Toward Using an Expert System Development Life Cycle, In: Proceedings of Decision Sciences Institute (1992) 765–767.

[40] L. Zadeh, Commonsense Knowledge Representation based on Fuzzy Logic, IEEE Computer 16, Nr. 10 (1982) 61–65.
