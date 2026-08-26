---
otero_id: 22454
otero_key: "9CE7REUP"
title: "Decision support with neural networks in the management of research and development: Concepts and application to cost estimation"
authors: "Jürgen Bode"
year: "1998"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00043-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applications

# Decision support with neural networks in the management of research and development: Concepts and application to cost estimation

Jürgen Bode $^{*}$

Wirtschaftswissenschaftliche Fakulät, University Leipzig, Marschnerstr. 31, D-04109 Leipzig, Germany

Received 22 February 1997; accepted 8 November 1997

## Abstract

Despite the small number of applications to date, neural networks are likely to be able to contribute to decision support in selected fields of R&D management. We identify the potential of neural networks in the application domain and compare it to ‘classical’ applications, such as the recognition of hand-written characters. Typical neural network architectures for R&D management tend to be simple, having low complexity, and only a small number of training samples are generally available. As an example, we carry out experiments for a typical R&D management application where neural networks have to estimate the final cost of a new product under development. It turns out that neural networks based on the standard backpropagation learning algorithm perform reasonably well when the ratio between highest and lowest cost is small, even for relatively small training set sizes. Otherwise the learning algorithm tends to undervalue low cost levels, so that deviations between estimated cost and real cost are intolerably high. Future research will have to investigate a modification of the error definition of the backpropagation algorithm. Finally, a number of general statements are derived from our experience, and examples are provided where neural networks are appropriate or inappropriate in the domain of R&D management. © 1998 Elsevier Science B.V. All rights reserved

Keywords: Neural networks; Management; R&D management; Cost estimation; Regression analysis

## 1. Introduction

## 1.1. Overview

Research and Development (R&D) consists of activities that attempt to obtain new knowledge about natural and cultural phenomena and/or their novel application by the use of scientific methods $[15]$ . The concept encompasses a multitude of different phases, from basic research on the one hand, which focuses purely on creating new knowledge, to application and routine development which apply well-known principles to novel problems, on the other hand. Six major tasks make up the field of R&D management [23]: goal setting, planning and budgeting, organization, staffing and leadership, design of the R&D information system, and controlling.

Saturation, globalization, and differentiation of markets, higher intensity of competition, and rapid change of technological knowledge have increased the dynamics of modern economies, resulting in reduced product life cycles. The ability to innovate has become one of the central competencies for creating competitive advantage. The increased importance of innovation has forced executives to change the position of R&D within the firm: the predominance of a purely technological point of view had to be reduced and gradually replaced by a stronger business orientation. As much as R&D has moved from an organization-wide technical support function to an instrument of the corporate strategic plan, the need for systematic management of these activities has become more obvious.

In the recent past, within R&D management research, the perceived need to reduce time-to-market (i.e. the time from conceptualization of a new product until its marketing) has attracted much attention. Shorter development times are expected to realize higher first-mover market share, as well as lower production cost resulting from the accumulation of experience along the learning curve.

Two generic approaches attempt to accelerate design: concurrency of design-related activities, and enhanced communication between separate organizational units. The former reduces development time, because several activities are dealt with in parallel instead of sequentially, the latter speeds up design because infeasible or suboptimal plans and mistakes can be corrected early. Research has coined the term Concurrent Engineering, or Simultaneous Engineering, for a collection of methods devised to reduce time-to-market $[9, 21]$ .

## 1.2. Selected application domain: Cost-oriented product development

From the large spectrum of R&D management tasks, we selected the field of cost estimation to illustrate the use of neural networks in R&D management. Cost estimation represents some characteristic properties of R&D management: considerable degree of uncertainty, little repetitiveness and similarity among tasks, low dimensionality of problem space, little explicit knowledge about quantitative cause-effect relationships, and a close interdependence between technological and managerial factors.

Cost has a close relationship to price, sales volume, and profit. In addition, development decisions have a large impact on product cost throughout all later phases of the product life cycle $[19]$ . Ford estimates that, although product design constitutes 5% of total product cost, the influence of design on production cost is 70%. Consequently, methods of cost-oriented product development have been created, such as Design-to-Cost and Target Costing $[22, 27]$ .

For cost-oriented design the ability to estimate cost is indispensable. In its thrust to uncover product cost before completion of development, cost estimation attempts to detect costly designs concurrently, during all phases of design, and thus forms an important part of Concurrent Engineering. However, R&D managers face a dilemma: as knowledge about the product increases designers know more about cost. On the other hand, the more product attributes have been determined, the less changes can be made to influence cost (Fig. 1). Reliable cost information often is obtained only late in the development process. If predicted cost is regarded as too high, further development either has to be abandoned or several, if not all, phases have to be repeated. This leads to time delays and increased development cost.

It is therefore desirable to have methods which can predict cost at an early stage of development ([18])

![](/api/attachments/9CE7REUP/fulltext/images/6c91c1523aad46f9d75fe217d158bfd7b8f708e019f5a23f9f52c7add8c277ad.jpg)  
Fig. 1. Cost estimation dilemma ([3])

terms it the ‘fuzzy front end’ of product development). The so-called parametric cost estimation methods are most common when only a few conceptual product-related attributes are known $[17, 25]$ . They identify a functional relationship (cost function) between the values of such attributes and cost. The cost function is derived using statistical regression of past case data. An important difficulty in any parametric estimation is the need to determine the shape of the cost function (the regression itself provides the parameters, not the shape, of the function). Only heuristics are available for this task, and the right guess is necessary in order to achieve accuracy in the estimation.

## 2. Application of neural networks in R&D management

## 2.1. Architecture of neural networks

Sohl and Venkatachalam have published a paper recently in Information and Management dealing with neural networks, their design and use in forecasting model selection $[24]$ . Besides recent textbooks (e.g. $[12]$ ) the reader is referred to that for background, as necessary. We will concentrate on presenting the architecture of the type of networks used in our experimental research. Surveys on neural networks can be found in $[12, 16]$ .

The main building elements of a neural network are nodes and the links connecting them. There are three types of nodes: input, output, and hidden or intermediate.

The experiments were carried out with multi-layer perceptrons, a class of feedforward neural networks. They are able to perform a mapping from a vector of input values x to a vector of output values y:

$$
\boldsymbol {x} \rightarrow \boldsymbol {y}
$$

In general, multi-layer perceptrons in the first stage (training or learning phase) are fed with sample data (training data) which contain the required target output vector t associated to each input vector x. Thus, it is possible to let a penalty-based learning function change the network parameters (supervised learning). In the second stage (the application phase) a new vector x is the input and the output is to be obtained by the network.

In general, the goal of neural network training is to determine the mapping from the training data. A distance measure between y and t is regarded as the neural network error. However, a small error during training does not necessarily imply good generalization; that is, good performance with data not seen before (problem of overfitting training data). The most prominent learning function is the error backpropagation algorithm first suggested by Werbos [12], which is also used in our research.

The number of output and input nodes depends on the number of elements of the output vector y and of the input vector x, respectively. The number of hidden nodes can, in principle, be selected freely. However, neural networks perform differently with different numbers of hidden nodes. To date, there is no reliable method to determine the optimal number of hidden nodes. Research results are able to suggest upper and lower bounds for the number of hidden nodes for narrowly defined application cases (see $[2, 11, 30]$ ).

## 2.2. Potentials of neural networks in R&D management

## 2.2.1. R&D management as an ‘untypical’ application domain of neural networks

One of the ‘classical’ applications of neural networks is pattern and character recognition; for example, of hand-written characters. These typically consist of dozens of input nodes, and 10–50 output nodes. Due to the statistical nature of neural networks their application requires the existence of a substantial body of case data. Usually the training data available range from many hundreds to tens of thousands or more.

For R&D management, as for many management applications, the situation is different. It is common to describe a management problem by only a few independent variables, resulting in a small number of neural network input nodes (resulting in low dimensionality). Further, many problems ask for a binary classification (e.g. for the prediction of bank failures where the classes are failure and nonfailure [26]), or for an approximation to a single-valued function (e.g. for cost estimation). As a result, neural networks for R&D management tend to be less complex than architectures for technical applications, because of their comparatively small numbers of input and output nodes.

Table 1  
Comparison of typical properties of neural network applications $^{a}$

<table><tr><td></td><td>‘Classical’ neural network applications</td><td>Neural networks applied to R&amp;D management</td></tr><tr><td>Example</td><td>Recognition of hand-written characters</td><td>Cost estimation</td></tr><tr><td>Number of input nodes</td><td>High (10...100)</td><td>Low (3...8)</td></tr><tr><td>Number of output nodes</td><td>High (10...40)</td><td>Low (1...3)</td></tr><tr><td>Architectural complexity</td><td>High</td><td>Low</td></tr><tr><td>Number of training samples</td><td>High (500...10,000)</td><td>Low (10...200)</td></tr><tr><td>Sensitivity of missing or inaccurate data</td><td>Robust</td><td>Sensitive</td></tr><tr><td>Computing time during training phase</td><td>Long</td><td>Short</td></tr><tr><td>Advantages from parallel computation</td><td>Reduction of computing time; robustness against component failure</td><td>Negligible benefit</td></tr></table>

$^{a}$ The properties are typical: they describe the majority of applications. But they are not exhaustive.

Furthermore, the number of training samples available in the area of R&D management usually is low, because experience in R&D cases is limited: training sets of several dozens of samples would be regarded as large.

## 2.2.2. Neural network properties

Typical classes of problems likely to be tackled successfully by neural networks resemble those of advanced statistical methods. However, neural networks have some advantage as they are non-parametric [31] and make weaker assumptions.

From the point of view of application in R&D management, an important property of neural networks is their ability to detect hidden relationships among case data and to apply these relationships to new data. They can be used to classify data (clustering), to approximate functions (curve fitting), and to extract orthogonal factors (principle components) from interdependent data.

Neural networks are robust: they are able, within limits, to deal with inexact or missing data. However, the appropriateness of the result depends on the type of application and the architecture of the network.

Another property is the robustness of neural networks against physical failure of a single component. For applications in R&D management this characteristic is secondary. The low level of complexity and the small number of training samples allow neural networks to run on a single microcomputer.

The inherent parallelism of the neural network architectures makes them easy to run on parallel processors and, thus, shortens computing time. In our experiments, training required between 2–20 minutes on a 486 processor with a rate of 56 MHz and 16 MB memory. The processing of new data subsequent to training took only fractions of a second.

Table 1 compares R&D management applications with ‘classical’ neural networks.

## 2.2.3. State of the art in research

Quite a few prototypical applications have been reported for the support of engineering design ([13, 20, 29]; overviews in [32]). They mostly concentrate on technical aspects, such as configuration of components, engineering analysis, and derivation of technical component properties from design specifications. Management-oriented neural network applications in the area of R&D are still rare, focusing on the estimation of cost and design time [4–8, 10] and the retrieval of design cases [1, 14, 28].

To date, the bottleneck for more widespread application of neural networks in R&D management seems to be the shortage of data in a suitable format. Although advanced organizations usually have much experience in R&D management the case knowledge required by neural network applications is rarely documented in a way accessible by computers. This constitutes a major drawback. However, the increased use of computer-based R&D management tools will increasingly generate case data and thus enable their exploitation by neural networks in the future.

## 2.3. Neural networks in cost estimation

A limited set of product-related properties has a major impact on cost; for example, Mileham et al. [17] show that the cost of injection-molded components can be explained by the properties' product weight, production volume, cycle time, and machine size. However, the precise relationship is unknown.

Neural network application in cost estimation is not restricted to function approximation. If the product-related properties with impact on cost are large the high dimensionality of the problem will impair estimation of cost. Neural networks might then help to detect interrelationships between properties and extract a smaller set of principal components subsequently to be used for cost estimation.

## 3. Application

## 3.1. Case description

In our experiments, neural networks were used to estimate the total cost of single-groove ball bearings. Although based on a simple principle, bearings differ considerably in geometry, material, and design. For the set of samples used in our study the outer diameter varies from 9 to 260 mm, the width ranges from 2.5 to 55 mm, and different material and design combinations can be selected according to the type of application of the bearing. Consequently, the cost varies from 6 cost units up to almost 1,000 cost units.

For our experiment it seemed straightforward to obtain costing data from a manufacturing firm. However, it was difficult to find a company that was willing to open its confidential cost information to an outside researcher. We therefore chose an indirect approach and extracted data from the price list of a large manufacturer. In the experiments, the price figures in the list were regarded as the target cost figures to be estimated by the neural networks.

It can be argued that list prices are different from cost. However, the assumption that prices equal cost (including interest on principle) generally holds in a perfect market. Markets for highly standardized machine elements, such as bearings, can usually be considered as perfect. Even if substantial rebates were common, they were likely to have a constant relationship to list prices and therefore the results of our experiments would remain unchanged. For a more detailed discussion of the perfect market assumption see $[5]$ .

## 3.2. Experimental layout

There are six attributes associated with bearing cost: inner and outer diameter, width, weight, design type, and material. We used a multi-layer perceptron with six input nodes (one for each attribute), one hidden layer of six nodes, and one output node representing the cost value. After the training period, the performance of the network was measured by entering known inputs and comparing outputs with real costs.

Neural networks were trained using a total of 573 data sets. The performance measure was:

$$
\text { relative   deviation } = \frac {\mid \text { estimated   cost } - \text { real   cost } \mid}{\text { real   cost }}
$$

We experimented with three different training set sizes of 20, 50, and 200 samples. In order to avoid biased results from random outliers we created five different training sets for each training set size and averaged the performance of the resulting neural networks. However, for training set sizes of 200 samples only two training sets were used.

## 3.3. Experimental results

The relative deviations average around 34% (Fig. 2) if all six attributes are used as network inputs (complete attribute set). This is a disappointingly low performance. It cannot even be improved by using a larger number of training inputs as set size has no significant impact on performance. This finding is unexpected as an increase of predicting accuracy is usual if more points are available.

One determining factor of neural network performance is the complexity of the topology. An increase in the number of input nodes (dimensionality of the neural network) results in an increase of free parameters of the neural network. More free parameters reduce function approximation accuracy after training with a given number of training samples. It is common practice to reduce the number of input nodes in order to improve performance by considering, or creating, only significant input attributes of the application problem (network pruning through principal component analysis, etc.).

In our experiments, we used a reduced set of four attributes by omitting the weight of the bearings, because it generally depends on the geometrical attributes, and merging design type and material to one single attribute. As expected, the deviation was reduced to levels below 30% (Fig. 2).

![](/api/attachments/9CE7REUP/fulltext/images/85128cf243ca11e16178081b857a2fe2f174f8d9314ce09409b4ba1791235cde.jpg)  
Fig. 2. Deviation of estimated cost from real cost.

The results still being unsatisfying, we analyzed the cost estimation performance in more detail. Fig. 3 shows the deviations after segregating the test sets into three cost classes. Among these, test samples in the cost interval between 100–1000 cost units exhibit a remarkable behavior. Firstly, the neural networks perform much better than test samples in the cost ranges below 100 units. Secondly, the experiments show a significant improvement of performance with increasing training set sizes, as may be expected.

This inconsistent behavior among cost ranges may be credited to the specific shape of the error function used in the backpropagation algorithm. Neural network applications often do not only rely on the results of the network alone but modify the input data (pre-processing) and/or output data (postprocessing) to achieve better results. Another method to improve performance is to consider knowledge apart from the knowledge implicitly represented in the training sets (background knowledge) during construction of the neural network. Such an approach would attempt to combine hidden knowledge acquired through training with explicit knowledge to be inserted manually during network construction.

The number of hidden nodes had only minor effects on estimation results. We tested topologies in a range from 1 to 52 hidden nodes. A pronounced optimum could not be detected. The fact that even very small hidden layers did not impair the results indicates that the structure of the application problem is simple.

Furthermore, experiments with estimation methods different from neural networks have been carried out, namely, linear and nonlinear regression analysis. These are parametric methods and therefore require to predefine the shape of the cost function before they are applied to the training sets. Besides this disadvantage, regression analysis produced greater errors than neural networks when applied to the same data $[8]$ . Neural networks clearly showed superior results.

## 3.4. Appropriateness of the learning function

The backpropagation algorithm utilizes a function of absolute error of the neural network for penalization and change of parameters during training. For example, if the required cost as represented in the test set is 940, and the cost estimated by the neural network is 950, then the absolute error is $|950 - 940| = 10$ . If required cost and estimated cost are 20 and 30, respectively, then the absolute error is $|30 - 20| = 10$ . In both cases, the errors are regarded as equal by the learning function. However, a R&D manager would consider these errors as different because they are based on different cost levels. He or she would calculate a relative deviation as a percentage.

![](/api/attachments/9CE7REUP/fulltext/images/ddbff6c90d862da489d320e8cd0aa261003589779a5489e5f43793172c01d246.jpg)  
Fig. 3. Deviations of estimated cost from real cost; reduced attribute set (4 attributes).

This suggests that the backpropagation algorithm makes the neural network train to an inappropriate objective. Both goals come close at high cost values but diverge dramatically when lowering cost. This can be seen clearly by the high deviations of lower cost ranges in Fig. 3. This behavior apparently becomes more pronounced when training set sizes increase: lower cost ranges show an untypical reduction of performance.

The inappropriateness of the backpropagation algorithm need not be severe in all cases of cost estimation by neural networks. The average performance of a neural network is impaired more when the ratio between the highest and lowest value is great, and when a large number of samples represents low rather than high values. In our case, minimum-to-maximum cost value followed a ratio of 1:150 which means that the learning function rated an error of the uppermost value 150 times higher than the error of the lower value. Applications whose outputs exhibit a min–max ratio of 1:10 can be expected to show a performance comparable to the uppermost cost range or even better.

## 4. Conclusion

## 4.1. Applicability of neural networks to R&D management

Experiments show that a few rules for the construction of neural networks (neural engineering) can be derived.

Case base: The utilization of neural networks generally requires a substantial body of known cases for training. These cases should be similar among each other, and to new cases to which neural networks are to be applied.

Functional relationship between known attribute values and required data: If any information not included in the input set of the network has significant impact on the required outputs, the result will be incorrect. However, this does not require the relationship between attribute values and outputs to be direct. If, say, lot size has an impact on cost but itself depends on geometrical attributes, then it suffices to consider the latter.

Limited problem size: The number of attributes which is assumed to be related to the required output should be small. As each attribute corresponds to one input node of the neural network, architectural complexity increases with the number of attributes.

No explicit knowledge base available: The strength of neural networks is the extraction of functional relationships among case data that are hidden, that is, unknown to the user. Other methods usually perform better whenever explicit knowledge can be applied, for example, in the form of algorithms, or rules. In the case of cost estimation, for instance, detailed expenditure-based methods are likely to excel when complete information on product structure, required work processes, and unit prices are available.

## 4.2. Summary

Despite the small number of applications to date, neural networks are likely to be able to contribute to decision support in selected fields of R&D management. Typical neural network architectures for R&D management tend to have a low complexity and only a small number of training samples is available.

As an example we carried out experiments where neural networks had to estimate the final cost of a new product under development. Poor average results required deeper analysis. It turned out that neural networks based on the standard backpropagation learning algorithm perform satisfactorily when the ratio between highest and lowest cost value is small, even for relatively small training set sizes. Otherwise the learning algorithm tends to undervalue low cost levels so that deviations between estimated cost and real cost are intolerably high.

## References

[1] A. Bahrami, C.H. Dagli, Design retrieval by fuzzy neurocomputing, J. Engineering Design 3(4), 1992, pp. 339–356.

[2] E.B. Baum, D. Haussler, What size net gives valid generalization? D.S. Touretzky (Ed.), Advances in Neural Information Processing Systems I. Morgan Kaufman, San Mateo, 1989, pp. 81–90.

[3] J. Becker, Entwurfs – und konstruktionsbegleitende Kalkulation. Kostenrechnungspraxis – Zeitschrift für Controlling (in German) 6, 1990, pp. 353–358.

[4] J. Becker, M. Prischmann, Supporting the design process with neural networks – A complex application of cooperating neural networks and its implementation, Journal of Information Science and Technology 3(1), 1993, pp. 79–95.

[5] J. Bode, S. Ren, Neural networks for cost estimation – benchmarks and pilot study. Research report, Tsinghua University, CIMS-ERC, 1996.

[6] J. Bode, S. Ren, Z. Shi, Application of 3-layer perceptrons to cost estimation, Proc. 1995 IEEE Int. Conf. Neural Networks, vol. 4, Rundle Mall/Australia, 1995a, pp. 1749–1754.

[7] J. Bode, S. Ren, S. Luo, Z. Shi, Z. Zhou, H. Hu, T. Jiang, B. Liu, Neural networks in new product development. In: Q. Sun, Z. Tang, Y. Zhang (Eds.), Computer Applications in Production and Engineering, Chapman and Hall, London, 1995b, pp. 659–666.

[8] J. Bode, Neural networks for cost estimation. Cost engineering, The International Journal of Cost Estimation, Cost/Schedule Control and Project Management 40(1), 1998, pp. 25–30.

[9] A.H.B. Duffy, M.M. Andreasen, K.J. MacCallum, L.N. Reijers, Design coordination for concurrent engineering, J. Engineering Design 4(4), 1993, pp. 251–265.

[10] K. Ehrlenspiel, S. Schaal, In CAD integrierte Kostenkalkulation, (in German), Konstruktion 44, 1992, pp. 407–414.

[11] M. Guterriez, J. Wang, R. Grondin, Estimating hidden unit number for two-layer perceptrons, Proc. Int. Joint Conf. Neural Networks, 90-SD, vol. I, 1989, 677–681.

[12] S. Haykin, Neural Networks – A Comprehensive Foundation, MacMillan, New York, 1994.

[13] Nenad Ivezic, James H. Garrett, Jr., A neural network-based machine learning approach for supporting synthesis, Artificial Intelligence for Engineering Design, Analysis and Manufacturing 8, 1994, pp. 143–161.

[14] S.V. Kamarthi, S.T. Kumara, F.T.S. Yu, I. Ham, Neural networks and their applications in component design data retrieval, Journal of Intelligent Manufacturing 1(2), 1990, pp. 639–644.

[15] W. Kern, H.-H. Schröder, Forschung und Entwicklung in der Unternehmung, (in German), Reinbek, 1977.

[16] R.P. Lippmann, An introduction to computing with neural nets, IEEE Acoustics, Speech, and Signal Processing Magazine 4(2), 1987, pp. 4–22.

[17] A.R. Mileham, G.C. Currie, A.W. Miles, D.T. Bradford, : A parametric approach to cost estimating at the conceptual stage of design, J. Engineering Design 4(2), 1993, pp. 117–125.

[18] R.K. Moenaert, A. De Meyer, W. Souder, D. Deschoolmeester, R&D marketing communication during the fuzzy front-end, IEEE Trans. Engineering Management 42(3), 1995, pp. 243–258.

[19] P.O. Grady, R.E. Young, A. Greef, L. Smith, An advice system for concurrent engineering, Int. J. Computer Integrated Manufacturing 4(2), 1991, pp. 63–70.

[20] J.L. Rogers, W.J. Lamarsh, II: Application of a neural network to simulate analysis in an optimization process. In: J.S. Gero (Ed.), Artificial Intelligence in Design '92. Kluwer, Dordrecht, 1992, pp. 739–754.

[21] A. Rosenblatt, G.F. Watson, Concurrent engineering. IEEE Spectrum, July 1991, pp. 22–26.

[22] M. Sakurai, Target costing and how to use it, J. Cost Management 3(2), 1989, pp. 39–50.

[23] H.-H. Schröder, F&E–Management. In: H. Corsten, M. Reiß (Eds.), Handbuch Unternehmungsführung – Konzepte, Instrumente, Schnittstellen (in German). Gabler, Wiesbaden, 1994, pp. 599–614.

[24] J.E. Sohl, A. R. Venkatachalam, A neural network approach to forecasting model selection, Information and Management 29(6), 1995, pp. 297–303.

[25] R.D. Stewart, R.M. Wyskida, Cost Estimator's Reference Manual. Wiley, New York, 1987.

[26] K.Y. Tam, M.Y. Kiang, Managerial applications of neural networks: The case of bank failure predictions, Management Science 38(7), 1992, pp. 926–947.

[27] M. Tanaka, Cost planning and control systems in the design stage of a product. In: Y. Monden, M. Sakurai (Eds.), Japanese Management Accounting: A World Class Approach to Profit Management, Cambridge, MA, 1989, pp. 49–71.

[28] V. Venugopal, T.T. Narendran, Neural network model for design retrieval in manufacturing systems, Computers in Industry 20, 1992, pp. 11–23.

[29] J. Wang, Y. Takefuji, Neural Networks in Design and Manufacturing, World Scientific, Singapore, 1993.

[30] P.D. Wasserman, Advanced Methods in Neural Computing, Van Nostrand Reinhold, New York, 1993.

[31] H. White, Connectionist nonparametric regression: Multilayer feedforward networks can learn arbitrary mappings, Neural Networks 3, 1990, pp. 535–550.

[32] H.C. Zhang, S.H. Huang, Applications of neural networks in manufacturing: A state-of-the-art survey, Int. J. Prod. Res. 33(3), 1995, pp. 705–728.

![](/api/attachments/9CE7REUP/fulltext/images/82672c439542ce791f3ec3be3bb51ebfbb815607b6f437cc8c7a2bf3299598bf.jpg)  
Jürgen Bode has studied at universities and business schools in Germany and France. He holds an M.S. degree in industrial engineering, a Ph.D. degree in management science, and a post-doctoral degree in automation engineering. Supported by a program of the German Academic Exchange Service (DAAD) he has worked for more than three years as an associate professor at Tsinghua University, Beijing. He is currently

teaching at Leipzig University, Germany.
