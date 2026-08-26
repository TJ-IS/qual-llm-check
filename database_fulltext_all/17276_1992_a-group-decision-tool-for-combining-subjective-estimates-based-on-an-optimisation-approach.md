---
otero_id: 17276
otero_key: "6MK2SP9Y"
title: "A group decision tool for combining subjective estimates based on an optimisation approach"
authors: "Madan G. Singh; J.C. Bennavail; Z.J. Chen"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90046-r"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A group decision tool for combining subjective estimates based on an optimisation approach

Madan G. Singh and J.C. Bennavail
University of Manchester, Manchester, UK

Z.J. Chen

Beijing Institute of Aeronautics and Astronautics, Beijing University, Peking, China

In this paper a powerful new approach is described for combining the subjective estimates of a number of managers into a single model by combining the model calibration with an optimization procedure. The combined model calibration and optimization procedure provides under reasonably mild restrictions, the ability to extract the underlying knowledge of a group of managers even though, superficially they may have widely varying views. The procedure has been used for developing Knowledge Support Systems to help a number of organisations to take better decisions. One of these cases is described in detail to illustrate the new concepts in the context of a practical sales force allocation problem.

Keywords: Group decision making, Decision support systems, Optimisation.

Z.J. Chen was born in the People's Republic of China. He took a Ph.D. from the Control Systems Centre at UMIST. He is currently a Professor at the Beijing Institute of Aeronautics and Astronautics. The work described in this paper was carried out whilst he was visiting the Decision Technologies Group of the Computation Department at UMIST.

![](/api/attachments/6MK2SP9Y/fulltext/images/0c7a27460ca4fb9dd44753d54827aa564a4578d0c8d26a515165f44d718c2f98.jpg)  
J.C. Bennavail is a Computer Officer in the Computation Department at UMIST. He collaborates with Professor Singh on problems of managerial decision making and decision aiding.

Correspondence to: Dr. Madan G. Singh, Computation Department, UMIST, Sackville Street, Manchester M60 1QD, UK.

## 1. Introduction

Little [4] introduced the concept of a decision calculus for formally incorporating managerial judgemental inputs for calibrating certain kinds of models used in managerial decision making. Essentially, through seeking a number of point estimates from a manager. Little showed how one could parameterise an 'S' shaped curve (a sales response curve). There has been a lively debate in the marketing literature concerning the advantages and disadvantages of 'Subjective' estimation of parameters through managerial responses to 'what-if' scenarios as compared to 'objective' parameter estimation using historical data, cf [1,5,6]. In many managerial decision making situations

![](/api/attachments/6MK2SP9Y/fulltext/images/ca11b1a2c6b150937cc1ed073af818c2ca171bcf5908eae641f2f7848f01be68.jpg)

Madan G. Singh B.Sc. (Exeter), M.Sc. (Manchester), Ph.D (Cambridge), Docteur en Science (Toulouse), C. Eng, Fellow of the IEE, Fellow of the IEEE is the Professor of Information Engineering at the University of Manchester Institute of Science and Technology (UMIST) since 1987. Professor Singh's research interests are on the application of Complex Systems and Information Engineering Methodologies to decision making problems in industry and commerce.

He was a part time Visiting Research professor of Management Science at INSEAD (the European Institute of Business Management), Fontainebleau, France, over the period 1980–84. Madan Singh is the author or co-author of 7 books, the editor or co-editor of a further 8 books, and an author or co-author of over 130 scientific articles. He is the editor-in-chief of the 8 Volume Encyclopedia of Systems and Control (Pergamon Books Ltd. 1987) and of the Series Advances in Systems, Control and Information Engineering which aims to keep the main Encyclopedia up to date by producing Supplementary Volumes and Concise Subject Encyclopedias. He is the editor-in-chief of the Journal Information and Decision technologies (North Holland) and he is on the Editorial Boards of a number of other International Journals including the IEEE Transactions on systems, Man. & Cybernetics. He is also the Coordinating Editor of 3 book series (with Pergamon, North Holland and Plenum). Madan Singh is the Chairman of the IMACS Technical Committee on Managerial Decision Making and was a Vice-Chairman of the Systems Engineering Committee of the IFAC (1981–84). He is the Vice-President (Publications) of the IEEE Systems, Man and Cybernetics Society.

there isn't enough historical data available to calibrate the models. There may therefore be significant merit in combining the meagre historical data set with subjective estimates from a number of managers. This raises the question of how to combine the views of different managers.

A number of approaches have been suggested in the literature for combining the views of the different managers. These can be split into two major categories i.e. Analyst selected pooling methods and Group Selected pooling methods [3]. The former include approaches for assigning different weights to the views of different managers based on the views of the analyst whilst the latter allows the group to produce these weights on the degree of ‘expertness’ of the different managers, either through an open dialogue or through an anonymous Delphi type approach.

In this paper we present a new way of combining subjective estimates for constant elasticity models which are commonly found in many managerial decision making applications. This new approach relies on the facts that:

(1) even where different managers have different views leading to different elasticities for the sales versus the decision variables, they often have a common view on the relativities between these elasticities.

(2) The common relativities between the elasticities could drive the decision variables to a common optimal solution.

(3) This common optimal solution is often identical to the solution obtained for a composite model where on each scenario completed independently by the different managers, the extreme values have been eliminated and the remaining values averaged.

Group Decision aids which operationalise the above procedure have been developed and tested for various practical problems $[7,8,9]$ . In this paper, the use of one of these Decision Aids for the allocation of a sales force is described as an example. In the remainder of this paper we begin in Section 2 by describing a typical constant elasticity model which has been used for resource allocation and in the context of this model we describe the operationalization of the new approach to combining subjective parameter estimates through optimisation. In Section 3 we provide both an intuitive and a mathematical justification for this new approach. In Section 4, we describe a practical sales force allocation problem as an example to illustrate the methodology and the group decision tool which operationalises it. Some conclusions are given in Section 5.

## 2. Constant elasticity models in managerial decision making

One of the most pervasive sales response models found in managerial decision making problems is the multiplicative model

$$
q_{i} = \alpha_{i}s_{i}^{\beta_{i}}\prod_{\substack{j = 1\\ j\neq i}}^{n}s_{j}^{\delta_{ij}},\tag{1}
$$

where $q_{i}$ is typically a sales response for the ith product, $s_{i}$ $i = 1, 2, \ldots, n$ are the decision variables which influence the sales $q_{i}$ , $\beta_{i}$ , $\delta_{ij}$ are constant elasticities. For example, if the $s_{i}$ $i = 1, \ldots, N$ are the shelf spaces in a retail outlet for the different products [8] then the above model could be used to describe a store with n departments (or products) with sales dependent on different amounts of shelf space allocated. The elasticity coefficients $\beta_{i}$ , $\delta_{ij}$ define the returns to scale and cross effects, respectively.

The decision making problem can typically be formulated as an optimization problem where we maximise a profit measure subject to the constraining relationships (1) and some additional inequality constraints which in the case of space allocation in retailing bound the shelf spaces to lie between certain limits, the allocation to not exceed the size of the store, etc.

## 2.1. The new subjective calibration procedure

In [8] the Resource-opt System was described. This enables the allocation of a fixed resource between a number of competing demands using a constant elasticity model and a geometric programming optimization procedure. The calibration of the model is done using a combination of experimental/historical/cross sectional data (where available) and the judgemental input of a number of managers which is extracted through their responding to a number of 'what-if' scenarios.

Formally, the optimization problem can be written as [8]

Max

$$
J = \sum_ {i = 1} ^ {n} \omega_ {i} q _ {i} - \sum_ {i = 1} ^ {n} \gamma_ {i} q _ {i} ^ {\tau_ {i}},\tag{2}
$$

Subject to $q = \alpha_{i}s_{i}^{\beta_{i}}\prod_{j = 1,j\neq i}^{n}s_{j}^{\delta_{ij}},$

(3)

$$
\sum_ {i = 1} ^ {n} s _ {i} = s _ {0},\tag{4}
$$

$$
m _ {i} \leqslant s _ {i} \leqslant M _ {i}, \quad i = 1, 2, \dots , n\tag{5}
$$

where:

$s_i$ is the decision variable, i.e. the allocation of the resource for product i; $q_i$ are the sales of product i;

$\beta_{i}$ is the direct elasticity w.r.t. the allocation of the resource for product $i$ ; $\delta_{ij}$ is the cross effect of the allocations of resource between products $i$ and $j$ ;

$\tau_{i}$ is the operating cost elasticity associated with the sales of product $i$ ; $\omega_{i}, \alpha_{i}, \gamma_{i}$ are scaling factors related to the allocation of resource for product $i$ .

The standard model calibration procedures involve using a data set (historical or judgemental) to fit equation (3) which is linearised by taking the logarithms on both sides. The judgemental data from multiple managers is given different weighting (cf [3]) and a single model emerges which is used as the basis for optimal decision making. However, this single model has involved considerable prior negotiation in terms of the weights to be assigned to the different judgemental data of different managers. The new procedure circumvents this negotiation by recognising that if the model building and optimisation is done for each manager's data, and if the managers have similar (though not identical) underlying views about the relativities between the different elasticities, then one would often end up with the same optimal solution despite the differences i.e. the optimal solution is insensitive to parametric variations if the underlying view on relative elasticities is similar.

## 2.2. Operationalization of the new procedure

The new subjective model calibration procedure has been operationalised in a Knowledge

Support System (i.e. in a computerised aid for helping Decision Makers in the performance of their cognitive tasks) in the following way:

(1) The user feeds in the constraints (4) and (5) in response to a spread sheet type of user-computer dialog.

(2) The computer generates a number of 'what-if' resource allocation scenarios based on a random number generator and a sophisticated experimental design procedure which ensures that the decision space defined by the constraints (4) and (5) is uniformly covered in a statistical sense.

(3) The 30 to 40 scenarios from (2) above are printed out and distributed to the 5 or 6 expert managers whose judgemental inputs are being sought.

(4) The computer fits the data from these 30 to 40 scenarios into equation (3) and thus builds the individual manager's models.

(5) Each model is subsequently optimized i.e. J in (2) is maximized subject to equations (3) (4) and (5) for each manager.

(6) In addition, a new ‘consensus’ model is constructed where for each scenario, the most optimistic and most pessimistic views are discarded and the rest averaged. This model is also optimized as in (5) above.

(7) The consensus building process in fact can also be used to give different weights to different managers views if desired so that the operational tool also enables one to combine the views of the experts in the standard way described in [3]. This tool has been used in a large number of real life group decision making studies in a number of British companies. It was observed that in many cases, the optimal decisions based on the different managerial views were identical even though the individual managers views yielded elasticity estimates which varied significantly.

In the next section, a mathematical as well as an intuitive justification is provided for this phenomenon.

## 3. Sensitivity analyses

In order to obtain an analytical solution of the optimal problem in the previous section, the following lemma transfers the problem into an equivalent problem which is easier to deal with. For simplicity, it is supposed that the optimal decision variables $s_i^*$ satisfy the constraints (5) and don't lie on the edges of the constraints.

Lemma. If the optimal solutions exist for the following problems

Max

$$
\begin{array}{l} J _ {1} = \sum_ {i = 1} ^ {n} \omega_ {i} q _ {i} - \sum_ {i = 1} ^ {n} \gamma_ {i} q _ {i} ^ {\tau_ {i}}, \\ J _ {2} = \sum_ {i = 1} ^ {n} \omega_ {i} ^ {\prime} \ln q _ {i} - \sum_ {i = 1} ^ {n} \gamma_ {i} ^ {\prime} \tau_ {i} \ln q _ {i}, \end{array}\tag{6}
$$

Subject to

$$
\begin{array}{l} \mathrm {q_ {i}} = \alpha_ {\mathrm{i}} \mathrm {s_ {i} ^ {\beta_ {i}}} \prod_ {j = 1, j \neq i} ^ {n} \mathrm {s_ {j} ^ {\delta_ {ij}}}, \\ \mathrm{h(s)} = \sum_ {i = 1} ^ {n} \mathrm {s_ {i}} - \mathrm {s_ {0}} = 0. \end{array}\tag{7}
$$

Then there exist certain weighting factors, $\omega_{i}$ , $\gamma_{i}$ , $\omega_{i}^{\prime}$ and $\gamma_{i}^{\prime}$ such that the optimal decisions for $J_{1}$ and $J_{2}$ are the same.

Proof. The optimal decision variables for $J_{1}$ can be obtained by solving the following equations [2] $\nabla J_{1}(s) + \lambda \nabla h(s) = 0,$ (8)

$$
h (s) = 0,
$$

then, we have

$$
\left\{ \begin{array}{c} \sum_ {i = 1} ^ {n} \omega_ {i} \frac {\partial q _ {i}}{\partial s _ {1}} - \sum_ {i = 1} ^ {n} \gamma_ {i} \tau_ {i} q _ {i} ^ {\tau_ {i} - 1} \frac {\partial q _ {i}}{\partial s _ {1}} + \lambda = 0, \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \dots \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \dots \\ \sum_ {i = 1} ^ {n} \omega_ {i} \frac {\partial q _ {i}}{\partial s _ {n}} - \sum_ {i = 1} ^ {n} \gamma_ {i} \tau_ {i} q _ {i} ^ {\tau_ {i} - 1} \frac {\partial q _ {i}}{\partial s _ {n}} + \lambda = 0, \end{array} \right.\tag{9}
$$

(10)

Suppose $s^{*}$ is the optimal decision variable vector for $J_{1}$ obtained by solving the above equations. In the same way, the optimal decision variables for $J_{2}$ can be obtained by solving the following equations

$$
\left\{ \begin{array}{c} \sum_ {i = 1} ^ {n} \frac {\omega_ {i} ^ {\prime}}{q _ {i}} \frac {\partial q _ {i}}{\partial s _ {1}} - \sum_ {i = 1} ^ {n} \frac {\gamma_ {i} ^ {\prime} \tau_ {i}}{q _ {i}} \frac {\partial q _ {i}}{\partial s _ {1}} + \lambda = 0, \\ \dots \\ \dots \\ \dots \\ \sum_ {i = 1} ^ {n} \frac {\omega_ {i} ^ {\prime}}{q _ {i}} \frac {\partial q _ {i}}{\partial s _ {n}} - \sum_ {i = 1} ^ {n} \frac {\gamma_ {i} ^ {\prime} \tau_ {i}}{q _ {i}} \frac {\partial q _ {i}}{\partial s _ {n}} + \lambda = 0, \end{array} \right.\tag{11}
$$

If we choose $\omega_{i}^{\prime}$ and $\gamma_{i}^{\prime}$ such that $\omega_{i}^{\prime} = \omega_{i}q_{i}^{*},$ $\gamma_{i}^{\prime} = \gamma_{i}q_{i}^{*\tau_{i}},$

where $q_{i}^{*}$ is the optimal value of $q_{i}$ for $J_{1}$ . Then it can be concluded that $s^{*}$ is also the optimal decision variable vector for $J_{2}$ by comparing equations (10) and (11). Therefore, by choosing appropriate weighting factors we can always transfer the study of optimal problem $J_{1}$ into the study of the optimal problem $J_{2}$ .☐

The sensitivity of the optimal allocation for optimal problem $J_{2}$ to the variations of model parameters is studied in the following theorem.

Theorem 1. Consider the nonlinear programming problem

Max

$$
J = \sum_ {i = 1} ^ {n} \omega_ {i} \ln q _ {i} - \sum_ {i = 1} ^ {n} \gamma_ {i} \tau_ {i} \ln q _ {i},
$$

Subject to

$$
\begin{array}{l} q _ {i} = \alpha_ {i} s _ {i} ^ {\beta_ {i}} \prod_ {j = 1, j \neq i} ^ {n} s _ {j} ^ {\delta_ {i j}}, \\ \sum_ {i = 1} ^ {n} s _ {i} = s _ {0}. \end{array}
$$

If the optimal decision variables are $s_{i}^{*}$ , then the necessary and sufficient condition for kth optimal decision variable, being not affected by the variations of the model parameters, is

$$
\frac {\left(\omega_ {k} - \gamma_ {k} \tau_ {k}\right) \mathrm{d} \beta k}{\sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \phi_ {i k}} = \frac {\sum_ {i = 1 , i \neq k} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \mathrm{d} \beta_ {i}}{\sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \sum_ {j = 1 , j \neq k} ^ {n} \phi_ {i j}},
$$

where

$$
\phi_ {i j} = \left\{ \begin{array}{l l} \beta_ {i} & \quad i = j, \\ \delta_ {i j} & \quad i \neq j. \end{array} \right.
$$

Proof. By using equations (8) (9), we have

$$
\left\{ \begin{array}{l} \frac {\left(\omega_ {1} - \gamma_ {1} \tau_ {1}\right) \beta_ {1}}{s _ {1}} + \frac {\left(\omega_ {2} - \gamma_ {2} \tau_ {2}\right) \delta_ {2 1}}{s _ {1}} + \dots \\ \quad + \frac {\left(\omega_ {n} - \gamma_ {n} \tau_ {n}\right) \delta_ {n 1}}{s _ {1}} + \lambda = 0, \\ \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \text {…} \\ \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \text {…} \\ \frac {\left(\omega_ {1} - \gamma_ {1} \tau_ {1}\right) \delta_ {1 n}}{s _ {n}} + \frac {\left(\omega_ {2} - \gamma_ {2} t _ {2}\right) \delta_ {2 n}}{s _ {n}} + \dots \\ + \frac {\left(\omega_ {n} - \gamma_ {n} \tau_ {n}\right) \beta_ {n}}{s _ {n}} + \lambda = 0, \\ s _ {1} + s _ {2} + \dots + s _ {n} = s _ {0}. \end{array} \right.
$$

The solution of the above equations is

$$
s _ {k} ^ {*} = \frac {s _ {0} \sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \phi_ {i k}}{\sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \sum_ {j = 1} ^ {n} \phi_ {i j}} \quad k = 1, 2, \dots , n.
$$

The sensitivity functions of kth optimal decision variables $s_{k}^{*}$ w.r.t. the variations of parameters $\beta_{j}$ are as follows

$$
\left\{ \begin{array}{l} \frac {\partial s _ {k} ^ {*}}{\partial \beta_ {j}} = - \frac {s _ {0} (\omega_ {j} - \gamma_ {j} \tau_ {j}) \sum_ {i = 1} ^ {n} (\omega_ {i} - \gamma_ {i} \tau_ {i}) \phi_ {i k}}{\left[ \sum_ {i = 1} ^ {n} (\omega_ {i} - \gamma_ {i} \tau_ {i}) \sum_ {j = 1} ^ {n} \phi_ {i j} \right] ^ {2}} \\ j \neq k, \\ \frac {\partial s _ {k} ^ {*}}{\partial \beta_ {k}} = \frac {s _ {0} (\omega_ {k} - \gamma_ {k} \tau_ {k}) \sum_ {i = 1} ^ {n} (\omega_ {i} - \gamma_ {i} \tau_ {i}) \sum_ {j = 1 , j \neq k} ^ {n} \phi_ {i j}}{\left[ \sum_ {i = 1} ^ {n} (\omega_ {i} - \gamma_ {i} \tau_ {i}) \sum_ {j = 1} ^ {n} \phi_ {i j} \right] ^ {2}} \\ j = k. \end{array} \right.
$$

when we have

$$
\begin{array}{l} \frac {n \mathrm{d} s _ {k} ^ {*}}{s _ {k} ^ {*}} \\ = \frac {\left(\omega_ {k} - \gamma_ {k} \tau_ {k}\right) \left[ \sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \sum_ {j = 1 , j \neq k} ^ {n} \phi_ {i j} \right] \mathrm{d} \beta_ {k}}{\left[ \sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \sum_ {j = 1} ^ {n} \phi_ {i j} \right] \left[ \sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \phi_ {i k} \right]} \\ - \frac {\sum_ {i = 1 , i \neq k} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \mathrm{d} \beta_ {i}}{\sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \sum_ {j = 1} ^ {n} \phi_ {i j}}. \end{array}
$$

Therefore, if and only if

$$
\begin{array}{l} \left(\omega_ {k} - \gamma_ {k} \tau_ {k}\right) \left[ \sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \sum_ {j = 1, j \neq k} ^ {n} \phi_ {i j} \right] d \beta_ {k} \\ - \left[ \sum_ {i = 1, i \neq k} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) d \beta_ {i} \right] \\ \left[ \sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \phi_ {i k} \right] = 0, \end{array}
$$

or

$$
\frac {\left(\omega_ {k} - \gamma_ {k} \tau_ {k}\right) \mathrm{d} \beta_ {k}}{\sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \phi_ {i k}} = \frac {\sum_ {i = 1 , i \neq k} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \mathrm{d} \beta_ {i}}{\sum_ {i = 1} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \sum_ {j = 1 , j \neq k} ^ {n} \phi_ {i j}},
$$

that we have $ds_{k}^{*}=0$ . □

If there are no cross effects between decision variables, the following corollaries are straightforward results from the above theorem.

Corollary 1. If $\delta_{ij}=0$ , for all i and j, then the necessary and sufficient condition for the kth optimal decision variable, being not affected by the variations of model parameters, is

$$
\frac {\mathrm{d} \beta_ {k}}{\beta_ {k}} = \frac {\sum_ {i = 1 , i \neq k} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \mathrm{d} \beta_ {i}}{\sum_ {i = 1 , i \neq k} ^ {n} \left(\omega_ {i} - \gamma_ {i} \tau_ {i}\right) \beta_ {i}}.
$$

Corollary 2. If $\delta_{ij}=0$ , for all i and j, then the sufficient condition for all optimal decision variables being not affected by the variations of model parameters is

$$
\frac {\mathrm{d} \beta_ {1}}{\beta_ {1}} = \frac {\mathrm{d} \beta_ {2}}{\beta_ {2}} = \dots = \frac {\mathrm{d} \beta_ {n}}{\beta_ {n}}.
$$

Because of the above Lemma, all the results obtained in the Theorem and Corollaries are also true for the optimal problem (2)-(5).

Implications of theorem 1 and of Corollary 1 and 2

The above theorem and corollaries provide precise mathematical conditions under which the views of different managers on expected 'sales' for different resource allocation scenarios would yield identical or near identical optimal solutions. Indeed, intuitively, one would expect that different managers would have very similar views on the relativities between the elasticities of the different products and in this case theorem 2 and the corollaries 1 and 2 show that the optimal solution will be insensitive to the parameters as has been observed in the real life case studies mentioned above.

Table 1  
Maximum and minimum sales force allocation for 1988

<table><tr><td rowspan="2">REGIONS 1988</td><td colspan="2">Scotland</td><td colspan="2">North</td><td colspan="2">Center</td><td colspan="2">South-east</td><td colspan="2">National</td><td colspan="2">Total</td></tr><tr><td>Days</td><td>People</td><td>Days</td><td>People</td><td>Days</td><td>People</td><td>Days</td><td>People</td><td>Days</td><td>People</td><td>Days</td><td>People</td></tr><tr><td>Minimum</td><td>787</td><td>3.75</td><td>1575</td><td>7.5</td><td>1837</td><td>8.75</td><td>1890</td><td>9</td><td>682</td><td>3.25</td><td>6771</td><td>32.25</td></tr><tr><td>Maximum</td><td>997</td><td>4.75</td><td>1785</td><td>8.5</td><td>2257</td><td>10.75</td><td>2520</td><td>12</td><td>892</td><td>4.25</td><td>8451</td><td>40.25</td></tr><tr><td>Current</td><td>787</td><td>3.75</td><td>1575</td><td>7.5</td><td>1837</td><td>8.75</td><td>1890</td><td>9</td><td>682</td><td>3.25</td><td>6771</td><td>32.25</td></tr></table>

Further, since the bounds given by equations (5) are often very tight, the optimal solutions for the individual managers models would usually be identical or near identical and these would, in turn, also correspond to the consensus model mentioned in section 2.2.

Finally, a practical application of this approach within the context of a real life sales force allocation decision making process is described.

## 4. The sales force allocation problem

The particular problem treated was one of allocating the sales force of a UK based company across 4 regions and for national accounts. The regions had different cost structures and the margin was also different.

The study divided the total sales force resource into selling days at the rate of 210 per person per annum. For 1988, with the additional selling days introduced as a result of recruitment, the total number of days available worked out to be 8085 from the 6771 currently available.

The total resource of 8085 selling days for 1988 was to be divided into the 5 groups: Scotland; North; Centre; South East and National.

For strategic reasons, Senior Management decided to have the minimum and maximum sales force allocations for 1988 given in table 1.

Table 1 gives the upper and lower bounds, not only in selling days, but also in people. The current allocation is also listed for reference.

Within these strategic bands, the Knowledge Support System operationalising the current approach produced 30 unique ‘what-if’ Resource Allocation scenarios for 1988. These were completed independently by the 3 managers, Mr. A, Mr. B and Mr. C. For each scenario, starting from the values of Sales, Costs and Profits associated with the current resource allocation, the managers predicted the Sales and Costs corresponding to each of the 30 scenarios in their best judgement.

The 30 completed scenarios for each manager were used to build a Knowledge Base corresponding to the views of that manager for 1988. The corresponding direct sales and cost elasticities are shown in table 2.

Table 2 shows a remarkable degree of internal consistency within the models even though they show great variation between the models. Essentially, these elasticities show that Mr. A has a fairly conservative view of sales resulting from the additional sales people, whilst Mr. B has a more robustly optimistic view. Mr. C lies between these two.

Table 2 Elasticities

<table><tr><td rowspan="2">1988REGIONS</td><td colspan="2">Mr. A</td><td colspan="2">Mr. B</td><td colspan="2">Mr. C</td></tr><tr><td>Direct sales elasticities</td><td>Cost elasticities WRT days</td><td>Direct sales elasticities</td><td>Cost elasticities WRT days</td><td>Direct sales elasticities</td><td>Cost elasticities WRT days</td></tr><tr><td>Scotland</td><td>0.28</td><td>1.00</td><td>1.05</td><td>1.00</td><td>0.80</td><td>1.00</td></tr><tr><td>North</td><td>0.23</td><td>1.00</td><td>1.08</td><td>1.00</td><td>0.75</td><td>1.00</td></tr><tr><td>Center</td><td>0.20</td><td>1.00</td><td>1.08</td><td>1.00</td><td>0.83</td><td>1.00</td></tr><tr><td>South-East</td><td>0.30</td><td>1.00</td><td>1.09</td><td>1.00</td><td>0.90</td><td>1.00</td></tr><tr><td>National</td><td>0.33</td><td>1.00</td><td>1.11</td><td>1.00</td><td>1.08</td><td>1.00</td></tr></table>

![](/api/attachments/6MK2SP9Y/fulltext/images/340cb868002198bf0230736b05f388c44e2a5849dab07fd70c8e803945903369.jpg)  
Fig. 1. Current allocations for 1988.

## 4.1. Optimisation results

As far as resource allocation is concerned, the key information used from the different models concerns the relative elasticities and these are very similar between the models. However, the sales forecasts from each model do vary considerably from model to model. Thus we would expect to be able to produce consistent resource allocations with varying sales and profit forecasts.

In the first series of resource allocation trials using the Knowledge Support System, the individual Knowledge Bases for the 3 managers were interrogated to produce their respective optimal allocations. Figure 1 shows the current allocation of the resource pie for 1988.

![](/api/attachments/6MK2SP9Y/fulltext/images/85503ed7f6fed69ebc50b6f9817201eaa0d9b00cc748a364ce5e2b595403050d.jpg)  
Fig. 2. Mr. A. optimum allocations 1988.

![](/api/attachments/6MK2SP9Y/fulltext/images/15fbf34eb67f261fd99a9e62f2ab96e31f0b996289f3238dd4f8d8bedc3b3cf3.jpg)  
Fig. 3. Mr. C. optimum allocation 1988.

Figures 2, 3, 4 show the profit maximising allocations of the increased pie for 1988 (with the additional 6.25 sales persons) which meets the strategic objectives outlined in table 1 for the 3 managers.

From figs. 2, 3, we note that the profit maximising resource allocations based on the model of Mr. A are identical to those based on the model of Mr. C and are very similar to those of Mr. C. The sales and thus profit forecasts however do vary considerably (from £3.880 million (Mr. A), to £4.657 million (Mr. B)) as one would expect, since the latter depend on the absolute values of the elasticities, whereas the resource allocations depend on the relativities between the elasticities as proved in Theorem 1, Corollary 1 and Corollary 2.

To see these resource allocation decisions in terms of the theorem in Section 3 and the Corollaries 1 and 2, let us take Mr. C. as a reference.

![](/api/attachments/6MK2SP9Y/fulltext/images/2bbbe40525dbf0a7e6db998bd22d3e4fdd6b18e4abba362efcec4f426eb7e9bb.jpg)  
Fig. 4. Mr. B. optimum allocations 1988.

<table><tr><td>Mr. C.</td><td>0.80</td><td>0.75</td><td>0.83</td><td>0.90</td><td>1.08</td></tr><tr><td>Mr. A.</td><td>0.28</td><td>0.23</td><td>0.20</td><td>0.30</td><td>0.33</td></tr><tr><td> $\Delta\beta_{i}$ </td><td>0.52</td><td>0.52</td><td>0.63</td><td>0.60</td><td>0.75</td></tr><tr><td> $\frac{\Delta\beta_{i}}{\beta_{i}}$ </td><td>0.65</td><td>0.69</td><td>0.75</td><td>0.66</td><td>0.66</td></tr><tr><td>Mr. C.</td><td>0.80</td><td>0.75</td><td>0.83</td><td>0.90</td><td>1.08</td></tr><tr><td>Mr. B.</td><td>1.05</td><td>1.08</td><td>1.08</td><td>1.09</td><td>1.11</td></tr><tr><td> $\Delta\beta_{i}$ </td><td>0.25</td><td>0.33</td><td>0.25</td><td>0.19</td><td>0.03</td></tr><tr><td> $\frac{\Delta\beta_{i}}{\beta_{i}}$ </td><td>0.31</td><td>0.44</td><td>0.30</td><td>0.21</td><td>0.03</td></tr></table>

Comparing the above three data sets of $\Delta\beta_{i}/\beta_{i}$ , the data of $\Delta\beta_{i}/\beta_{i}$ related to Mr. C. and Mr. A are almost the same. Therefore the optimal allocations related to Mr. C and Mr. A are also almost the same (see fig. 2 and fig. 3) although there is some difference between Mr. B and Mr. C which shows up in the slightly different optimal solution.

## 5. Conclusions

In this paper a powerful new approach has been suggested for combining the expertise of a group of managers in order to help them take better decisions. The approach combines the model calibration and the optimisation stages. It is shown that under fairly mild conditions, the optimal decisions for a group of managers would be identical or near identical despite significant differences in the individual models of the managers. The approach has been illustrated on a practical sales force allocation problem.

## 6. References

[1] P. Chakravarti, A. Mitchell and R. Stalin, Judgement based marketing decision models: problems and possible solutions, Journal of Marketing 45, No. 4, pp. 13–23 (1981).

[2] D.M. Himmelblau, Applied non-linear programming (McGraw-Hill, 1972).

[3] G. Lilien and P. Kotler, Marketing decision making: A model building approach (Harper and Row, New York, 1983).

[4] J.D.C. Little, Models and managers: The concept of a decision calculus, Management Science 16, pp. B466–485 (1970).

[5] S. McIntyre, An experimental study of the impact of judgement based marketing models, Management Science 28, 1, pp. 17–33 (1982).

[6] S. McIntyre and I. Currim, Evaluating judgement based marketing models: Multiple measures, comparisons and findings, In Marketing Planning Models (ed. A.A. Zoltner), pp. 185–207, TIMS Studies in Management Sciences, 18 (New York, North Holland, 1982).

[7] M.G. Singh and R. Cook, A new class of intelligent knowledge based systems with an optimisation based inference engine, Decision Support Systems 1, 4 (1985).

[8] M.G. Singh, R. Cook and M. Corstjens, A hybrid knowledge based system for retail space and other allocation problems, Interfaces 18, 5, B-22 (1988).

[9] M.G. Singh and J.C. Bennavail, Knowledge support systems for managerial decision making in B. Kelly and A. Rector (editors) R&D in expert systems A pp. 319–330, Cambridge University Press (1989).
