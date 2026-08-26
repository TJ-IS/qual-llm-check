---
otero_id: 17579
otero_key: "AASV5ZRA"
title: "A decision support system for in-sample simultaneous equation systems forecasting using artificial neural systems"
authors: "Louis E. Caporaletti; Robert E. Dorsey; John D. Johnson; William A. Powell"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90020-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for in-sample simultaneous equation systems forecasting using artificial neural systems

Louis E. Caporaletti, Robert E. Dorsey,
John D. Johnson $^{\dagger}$ and William A. Powell $^{\ddagger}$

The University of Mississippi, Mississippi, MS 38677, USA

Decision support systems have been proposed for many forecasting applications. Unfortunately no work has been done in the development of decision support systems for simultaneous equation systems (SESs) forecasting, a very complex and difficult forecasting problem. In this paper the applicability of an artificial intelligence technology, artificial neural systems, for decision support in SESs forecasting is shown. The discussion is focused on the multi-layer feed-forward neural network (MLFFNN). Performance of the MLFFNN versus traditional methods of SES forecasting is evaluated by comparing their in-sample forecast accuracy in a Monte Carlo experiment and on Klein's Model 1.

Keywords: Decision support system; Forecasting; Simultaneous equation systems forecasting; Artificial neural network; Genetic algorithm

![](/api/attachments/AASV5ZRA/fulltext/images/c46c0a90ef76847cce502dca9bcda2d1352a7109c0b8227453bbeacd22216384.jpg)

Louis E. Caporaletti is a doctoral student in the department of Management and Marketing at The University of Mississippi. His major is Production and Operations Management with minors in MIS and Quantitative Methods. His research interest include AI, ES, DSS, and Mathematical Modeling applications to POM, MIS, and Total Quality Management problems.

$^{\dagger}$ Dr.'s Dorsey and Johnson are supported in part by the U.S. Department of Education Fund for the Improvement of Post Secondary Education under grant #P116B00509 and the Research Foundation of the Institute of Chartered Financial Analysts.

$^{\dagger}$ We would like to thank the Mississippi Center for Super Computing Research for the use of their Cray XMP and Cyber 205 super-computers and an anonymous referee for helpful comments.

## 1. Introduction

This paper proposes a decision support system (DSS) using a multi-layer feed-forward neural network (MLFFNN) to aid in forecasting simultaneous equation systems (SESs). A major goal of the proposed DSS is to reduce the amount of information that a decision maker considers while preserving flexibility and interactive use. The pro-

![](/api/attachments/AASV5ZRA/fulltext/images/920eda516e168745c9ccf502db3180a9c509dae821485f75dabab4ffcc9b047a.jpg)

Robert E. Dorsey is an assistant professor in the Department of Economics and Finance at The University of Mississippi. He is currently working on the use of Genetic Algorithms in optimization and their applicability to neural networks. He is currently the co-principle investigator on two neural network related research projects. Prior to completing his doctorate, he was an administrator at the University of Arizona.

![](/api/attachments/AASV5ZRA/fulltext/images/3ee2eec4fc5b7c85003469ca4b1926a1de57bfdec8fa4490a6967f82b459df08.jpg)

John D. Johnson is an assistant professor in the department of Management and Marketing at The University of Mississippi. He is currently the co-principle investigator on two neural network related research projects. His current research involves the integration of neural nets and genetic algorithms as well as the development of new neural network training methodologies. He is the co-editor of the JAI press research annual Advances in Artificial Intelligence in Economics, Finance and Management.

![](/api/attachments/AASV5ZRA/fulltext/images/2bd3e4f9a14fde74ea3adc6355b584c4add7144216e026a766021582f4be7803.jpg)  
Models.

William A. "Artie" Powell is an assistant professor in the department of Economics and Finance at The University of Mississippi. His fields of specialty include econometrics, public economics, and risk and uncertainty. His current research interests are estimation and forecasting in simultaneous equations models both with continuous and censored dependent variables. Other interest include detection and prediction of stock volatility and estimation of Hedonic Price posed DSS achieves this goal by avoiding exact specification of the functional equations (relationships) that define the system.

Simon [55] classifies managerial decision environments along a continuum from highly structured to highly unstructured. In structured decisions the objectives are clearly defined and the procedures for obtaining the best (or at least a good enough) solution are known in advance. For these cases, managers can employ pre-defined models, whether conceptual or computer-based, to assist in the decision process. For unstructured problems, however, intuition is still the basis for decision making. The manager may seek help from experts who specialize in the particular problem area, but the final decision generally involves ad-hoc analysis and a substantial subjective element.

Decisions faced by executives concerning economic forecast models fall into both categories. Many common and routine tasks are highly structured (e.g., data gathering, aggregation, etc.). Consequently, they can be handled quite effectively by basic computer systems, readily available commercial software, and lower-level management or even clerical personnel. Unfortunately, a large number of forecast decisions faced by top-level managers are highly unstructured in nature and not easily adapted to conventional methods of computer-aided analysis and decision support. In the case of SES forecasting, these decisions include the selection of the appropriate estimation technique and model, and the inclusion/exclusion decisions on considered variables.

Help that has been available has been in the form of expert systems (ESs). These systems attempt to capture the essence of the decision-making ability of human experts. However, it is necessary to program, in the form of heuristics, the intuition or knowledge base of the experts into the ES. Unfortunately, the creation of the knowledge base is a long and expensive process, making it uneconomical to create expert systems for one-time decision problems. In addition, it is rarely clear what an expert's knowledge base includes and what heuristics are involved. As pointed out by Kuhn ([33], pp. 3–4);

Experts trained in scientific investigation but ignorant of the field of current application are likely to arrive at legitimate conclusions that are influenced by “the accidents of his investigation, and by his own individual make-up.”

Artificial neural systems (ANSs) offer an alternative source of help/assistance with distinct advantages over ESs in applications involving highly unstructured decision environments.

Neural nets can be defined as “highly simplified models of the human nervous system, exhibiting abilities such as learning, generalization, and abstraction” ([62], p. 10). Such systems have, in concept, been in existence for many years but the hardware requirements of even the most rudimentary systems had exceeded existing technology. Recent technological advances, however, have made ANSs a viable alternative for many decision support problems [18]. This paper proposes a DSS based upon ANS technology. More specifically, a DSS using a multi-layer feed-forward neural network (MLFFNN) to aid in the modelling of simultaneous equation systems (SESs) is proposed.

According to Davis and Olson [6] “The term decision support system (DSS) refers to a class of systems which support the process of making decisions...[and] allows the decision maker to retrieve data and test alternative solutions during the process of problem solving [6].” Three characteristics of a computer-based DSS are [26]:

(1) The computer must support the manager but not replace his or her judgment.

(2) The main payoff of computer support is for semi-structured problems, where parts of the analysis can be systematized for the computer, but where the decision-maker's insight and judgment are still needed to control the process.

(3) Effective problem solving is interactive and is enhanced by a dialog between the user and the system.

In this regard, a major drawback associated with traditional econometric forecasting procedures is the requirement of an exactly specified simultaneous equation model (SEM) (i.e., a maintained hypothesis). This exact specification greatly increases, not decreases, the informational requirements of any SES forecasting decision. For example, to estimate a SEM consisting of m endogenous and n exogenous variables the decision-maker must consider for each of the m equations:

(1) the inclusion or exclusion of each of the $n$ exogenous variables,

(2) the inclusion or exclusion of each of the other $(m - 1)$ endogenous variables, and

(3) the exact functional relationship between the exogenous and endogenous variables.

In short, the decision-maker is subjected to $n*(m-1)*m$ requests by the problem domain for an inclusion/exclusion decision, as well as the selection of the m proper functional forms (e.g., linear, nonlinear, etc.). Although the decision-maker's already existing perceptions or expertise (e.g., belief or knowledge of economic relationships) will filter or reduce the number of inclusion/exclusion choices [41], decisions as to functional specification have traditionally been influenced more by the needs of the econometrician and the proposed estimation procedure, than by a knowledge, on the part of the decision-maker, of the “true” underlying process.

Furthermore, in traditional forecasting, the selection of an estimation procedure is an additional choice that must be made in the decision making process. Though typically made by the econometrics expert, the choice of an estimation technique is, more often than not, made for calculation ease rather than from a consideration of any “true” functional relationship. For instance, in single equation models linearity is often imposed, not because a thorough investigation has been conducted with regards to the “true” relationship between the dependent and independent variables, but because a simple estimation procedure such as ordinary least squares can be employed. The use of two-stage least squares (2SLS) or three-stage least squares (3SLS) in SEMs plays the same type of role. Unrestricted Least Squares (ULS) is often employed in estimating the reduced form model when the degree of uncertainty associated with the SEM and its accompanying restrictions is high. The linearity restriction, however, is arbitrary and is often made to facilitate estimation. The neural network (NN) would not impose the restriction of linearity and given its fully flexible function approximation abilities will minimize à priori non-sample information (related to functional form, e.g., linearity), more so than the usual applications of ULS. It should be clear, however, that such à priori restrictions are at least as arbitrary as any other prior restrictions and impose strong and exact restrictions on the parameter space of the model.

With the ANS, on the other hand, an executive familiar with the structure of the problem selects only the proper inputs and outputs to the system $(m + n$ decisions). The weights assigned to each input (i.e., inclusion/exclusion restrictions) and the functional form of each of the m relationships are determined by the neural network, as opposed to the experts (e.g., econometrician's) explicit à priori assumptions. With regard to the specification of the functional form, the neural network does not necessarily impose linearity restrictions. This is due to the fact that the neural net “learns” the underlying functional relationship from the data itself, thus, minimizing the necessary à priori non-sample information. Indeed, a major justification for the use of a neural network as a completely general estimation device is its function approximation abilities. That is to say, its ability to provide a generic functional mapping from inputs to outputs. This eliminates the need for exact prior specification. With a neural network, the decision-maker has a tool which can aid in function approximation tasks, in the same light as a spreadsheet aids what-if-analysis. These function approximation tasks, along with many problem domains, can be characterized as a black box process as illustrated in Figure 1.

The black box system may be an actual system or represent the problem of interest. One solution strategy, in this case, is for the decision-maker to attempt a mapping between the inputs and outputs to help solve the problem of interest. In this paper the mapping abilities and ease of use of a neural network to assist the decision-maker is shown. Per the second characteristic of DSSs above, the decision-maker's insight is still required as the neural network does not totally automate forecast decision-making but acts as a tool which assists the decision-maker in very complex mapping and function approximation tasks. Per characteristic 3 above, the main interaction between the neural network and user pertains to the inclusion or exclusion of data, neural network architecture specification and analysis of the output by the decision-maker.

![](/api/attachments/AASV5ZRA/fulltext/images/387e79e7581e65c6d45d019f794136a0d523ffa59a23cd1f27f5e83c173b0258.jpg)  
Fig. 1. A black box process.

A major advantage in the application of MLFFNNs to the estimation of SEMs is related to their ability to provide a flexible mapping between inputs and outputs. The most commonly cited proof of this is the superposition theorem of Kolmogorov [30], or its improvements by Lorentz [37], and Sprecher [58]. The connection between these results and MLFFNNs has been pointed out by Hecht-Nielsen [20]. Hecht-Nielsen also discusses several function approximation results of the MLFFNN [19]. These results state that one can compute any continuous function using linear summations and a single properly chosen nonlinearity. In other words, the arrangement of the simple nodes into a multi-layer framework produces a mapping between inputs and outputs consistent with any underlying functional relationship regardless of its “true” functional form. The importance of having a general mapping between the input and output vectors is evident since it eliminates the need for unjustified à priori restrictions so commonly used to facilitate estimation (e.g., the Gauss Markoff assumptions in regression analysis). It should be noted that if these assumptions hold, eg. the Gauss Markoff assumptions, the neural network model will yield a similar solution, since the image of any underlying mapping can always be projected into a perfectly flexible mapping.

The appropriateness of OLS is an empirical question which cannot be settled in general for any finite number of observations. Thus a test of the assumptions must become a routine part of any potential application. Also, without the à priori restrictions, the decision-maker is allowed to involve, to a greater extent, his/her decision making expertise (or intuition) in the analysis of the problem.

Kolmogorov's theorem, along with its improvements, establishes a perfectly general mapping from $\mathcal{R}^{\mathrm{n}}\mapsto \mathcal{R}^{\mathrm{m}}$ as long as the correct transfer function, $g(\cdot)$ , is chosen. [In the case of the Irie and Miyake integral formulation, the squashing function $g(\cdot)$ is known but an infinite number of hidden units is required.] For these reasons the results above, though theoretically correct, are difficult to implement. Funahashi [13], Cybenko [5] and Hornik, Stinchcombe, and White [22] show however, that $g(\cdot)$ can be specified à priori as the sigmoid function (illustrated in Figure 2) without sacrificing flexibility. Hornik et. al. [22] also show that the underlying “true” functional form need not be continuous; they show that standard multi-layered feed-forward networks with as few as one hidden layer using arbitrary squashing functions can approximate any Borel measurable function. The results of Funahashi [13] and Hornik et. al. [22] show that a perfectly general approximation to the true function to any arbitrarily small error $\epsilon$ is possible given a sufficient number of hidden layer neurons. The function approximation ability of the MLFFNNs should provide the decision-maker with a reliable method for making in-sample forecasts in an SES setting. To demonstrate the neural net’s ability as a decision support tool the accuracy of these in-sample forecasts is examined. The ability of the DSS to match (or exceed) traditional econometric forecast performance of an exactly specified SEM while minimizing the requisite “intuition” (e.g., econometric specification responsibilities) of the decision-maker, provides a major justification for such a DSS.

![](/api/attachments/AASV5ZRA/fulltext/images/685028369dc82bf87ac8c5694d5487b2c310be8e3765b02cbee82a9954b65c73.jpg)  
Fig. 2. The sigmoid nonlinearity.

When employing traditional econometric techniques, SES forecast reliability depends crucially on two considerations:

(1) the underlying formulation of the maintained model, and

(2) the procedure employed to estimate the model and its associated reduced form (Maasoumi and Jeong [39]).

Generally the maintained model is influenced by an understanding of the inputs and outputs to the underlying process under consideration. For the most part, determinations of the inputs and outputs to the process are made by an executive familiar with the process. Since traditional estimation requires some à priori knowledge of the structure of the black box, an econometrician is normally needed to provide some non-sample domain specific theoretical restrictions. Given its fully flexible function approximation abilities, the neural network has no need to impose such à priori non-sample information (related to functional form), thus, the “intuition” of the econometrician is not needed in this capacity. The neural net, therefore, reduces the necessary à priori non-sample information needed in the decision process.

The purpose of this paper is to examine whether or not this more general and easier to use technique will cost the manager in terms of in-sample forecast reliability. This paper will compare the in-sample forecast performance of the multi-layer feed-forward neural network (MLFFNN) to standard econometric estimation techniques. To facilitate the comparison, a Monte Carlo experiment is employed to provide appropriate numerical information. The traditional estimators investigated here are the Unrestricted Least Squares (ULS), Two-stage Least Squares (2SLS), and Three-stage Least Squares (3SLS) estimators. In addition to the Monte Carlo study, structural forecasts for the two approaches are compared using Klein's Model I.

## 2. Review of the existing literature

## 2.1. DSS and forecasting

There have been many commercial applications of DSSs to forecasting. Most of these DSS applications pertain to assisting the decision-maker in time-series forecasting. Several examples of commercial applications are presented in [6] and [59]. Decision support for regression-based forecasting is mentioned substantially less in the applications literature [42], [57]. In the academic literature there has been interest in decision support for the Box-Jenkins forecasting technique [35], [61]. Although the authors are not aware of specific DSS applications in the literature for simultaneous equation systems forecasting, this is probably due more to the complexity of the models rather than a lack of applicability. (An obvious application is in the forecasting of business trends in supply and demand.) On the other hand, Sprague and McNurlin [57], and Er [12] suggest a very significant trend in the adaptation of artificial intelligence (AI) techniques to DSSs. An illustration of this for stock market prediction is found in Braun and Chandler [2]. This paper will demonstrate the usefulness of an AI methodology, the neural network, to a decision-maker in building simultaneous equation system in-sample forecasting models.

## 2.2. ANSs and forecasting

Application of artificial neural systems to forecasting is widespread. For example, Werbos [64] has applied his backpropagation learning rule for a recurrent gas market model which the Department of Energy regularly uses ([40], p. 395). Werbos has also applied his learning technique for forecasting and prediction in Global Crisis Models [65]. Another seemingly popular application of MLFFNNs to forecasting is in the financial arena. Such papers include Halbert White's use of a neural net to predict IBM early stock returns [67] and the forecasting of the Standard & Poor's 500 Index [69], Dutta and Shekhar's prediction of bond ratings [11], and the application of ANSs by others in the prediction of mortgage loan defaults [17], [56]. Other areas of interest include the forecasting of residential and commercial energy demand [44] and electrical appliance ownership [31], [32].

Compared to other forecasting techniques Sharda and Patil [54] found that MLFFNNs forecast about as well as the Box-Jenkins technique. Dutta and Shekhar [11] found that an ANS performed better than regression techniques. A short review of the use of MLFFNNs in forecasting is in ([40], p. 395). The authors have not yet seen or are acquainted with any research regarding neural networks (NNs) and simultaneous equation systems forecasting.

## 2.3. Neural network model

The MLFFNN used in this paper is an extension of the perceptron of Rosenblatt [50], which is a very simple artificial neuron structure (or simply neuron) as illustrated in Figure 3. This structured node sums the weighted inputs from its neighbors, compares this sum to its threshold value ( $\theta$ ) and passes the result through a function referred to as an interaction rule. The value of a typical node Y is given by:

![](/api/attachments/AASV5ZRA/fulltext/images/0dafc326b96dc8be02e56c40b9f174a001bfb45ceb7c532211ce2676f3033ab1.jpg)  
Fig. 3. A typical artificial neuron.

$$
Y = g (\cdot) = g \left(\sum_ {k = 1} ^ {n} \omega_ {k} y _ {k} - \theta\right).\tag{1}
$$

Where $\theta$ is the threshold activation level, known as the offset. As is shown in Figure 3, each node (Y) can be represented as a function of n weighted inputs. These perceptrons can be arranged in multiple, fully interconnected, layers producing a multi-layered perceptron as illustrated in Figure 4. In this network the input nodes are linked to the output nodes through one or more interconnected hidden layers. The multi-layered perceptron is referred to as a feedforward network since inputs are fed into the bottom (or input) layer and propagate forward through the network topology to the output layer.

## 2.4. Training methodology

Traditionally these MLFFNNs are trained using the backpropagation training algorithm of Werbos [64], LeCun [36], Parker [45], and Rumelhart et al. [52], [53]. Problems with the backpropagation training algorithm have been outlined by Wasserman [63] and Hecht-Nielsen [19]. These problems include the tendency of the network to become trapped in local optima, to suffer from network paralysis as the weights move to higher values, and to become temporally unstable – that is, to forget what it has already learned as it learns a new fact. Since the aforementioned flexibility (mapping and function approximation) theorems depend upon the selection of the proper weights, the utility of backpropagation as a learning rule for producing a flexible mapping is questionable. Therefore, this paper will use the genetic adaptive neural network training (GANNT) algorithm of Dorsey, Johnson, and Mayer [7], [8].

![](/api/attachments/AASV5ZRA/fulltext/images/41aa5a1d06ba9acd286428bd674f35b6e45d04b0846f13cfab2c4881bf26ebeb.jpg)  
Fig. 4. The multi-layered perceptron net.

Since the genetic algorithm does not use the derivative of the network output to adjust its weight matrices, as with gradient decent methods (e.g., the backpropagation training algorithm), the derivative (of the objective function) need not exist and thus the network can use any objective function (as long as its value can be computed in a finite amount of time) [9], [10]. This also implies that the network paralysis problem can be overcome. The paralysis problem occurs with backpropagation as the weights adjust to very large values, forcing the weight adjustments to become increasing smaller (since these values are proportional to the network output) and thus paralyze the network. Temporal instability is overcome since the network is trained in a batch mode. That is to say weights are only changed at the end of each complete sweep through the data. In addition, the network does not become trapped in local optimum since the genetic algorithm provides a global search method. In fact, as pointed out by an anonymous referee, the convergence behavior of the genetic algorithm can be controlled, compared with Backpropagation. Further, the global convergence of the algorithm is under good control of the user, providing computer time is not an issue. Globally optimal solutions are more difficult to implement with Backpropagation. This global convergence property of the GANNT algorithm provides an advantage to the user. The user can generate and compare several MLFFNN models of the SES, comparing each model in regard to convergence time and fit, as well other conditions.

Dorsey, Johnson and Mayer [8] empirically show that the genetic algorithm performs very well on a large class of problems with generic network architectures. In fact, each of the problems used one hidden layer and six hidden layer neurons. Thus they demonstrate that the genetic algorithm based training method for the selection of the appropriate weight matrices overcomes the shortcomings of backpropagation and thus produces the desired flexibility. In learning the appropriate weight matrices, the genetic algorithm iterates toward a solution through a process that in ways parallels the Darwinian process of natural selection [15]. Given a specific feed-forward neural network objective function to be optimized, the genetic algorithm starts with an initial population of candidate solutions (the first generation). A subset of the population is then chosen to act as progenitors to contribute offspring to the next generation of candidate solutions. As in natural systems, the new offspring inherit a combination of the traits from their parents whose traits were either the result of a conception propagated by progenitors in a prior generation or bestowed by the organizer of the initial population. The key to this process is selectivity. Not all population members from the previous generation are given an equal chance of producing progeny to fill the pool of the present or future population of possible solutions. Thus, it is likely that only a select few will actually contribute.

In particular, the population members with the highest probability of producing progeny are those possessing traits favorable to solving for the optimum of the specific objective function. In contrast, members of the present population least likely to contribute candidate solutions to the next generation are those possessing unfavorable traits. In this way, a new population of candidate solutions (the second generation) is built from the most desirable traits of the initial population. As iteration continues from one generation to the next, traits most favorable in finding an optimal solution for the objective function thrive and grow, while those least favorable die out. Mutation may also occur at any stage of the progression from one generation to the next. By randomly introducing new traits into the natural selection process, mutation tests the robustness of the population of possible solutions. As with traits bestowed upon members of the initial population, if these newly introduced traits add favorably to the ability of their recipients to optimize the specific objective function, then the new trait will thrive and grow. Otherwise, the effect of the mutation will die out. Eventually, the initial population evolves to one that contains an optimal solution and the evolutionary process terminates.

More specifically, in the coding scheme of the GANNT algorithm, the weight matrices of the NN are represented as a single vector. The scalar elements of the NN's initial population of 20 (Klein's Model I) or 30 (Monte Carlo Experiment) weight vectors, or strings, are drawn uniformly over the range [-100, 100]. The GANNT algorithm then conducts the following steps.

(1) Calculation of Error For each one of the 20 or 30 weight vectors (strings), or states of NN, the training input vectors are fed into the network and the NN's corresponding output vectors are compared with the training (or target) output vectors. An error value (in this paper SSE - equation (20)) is calculated for each one of the 20/30 strings.

(2) Reproduction Each one of the 20/30 strings is assigned a selection probability (p) which is inversely proportional to its error value calculated in step 1 above. A new set of 20/30 weight vectors or strings is selected from the 20/30 old strings. Each of the 20/30 old strings have probability p of being selected with replacement into the new set.

(3) Crossover The 20/30 new strings are randomly organized into 10/15 pairs. For each pair, one of the elements of the string are randomly selected. At this element each of the strings of the pair are broken into two. The pair then swaps vector elements.

(4) Mutation Next, it is decided whether any element of the 20/30 weight vectors, strings, should be changed. For each element of the 20/30 weight vectors a random number is selected and a Bernoulli trial is conducted. If the Bernoulli trial is successful (with probability equal to the mutation rate) then the element is replaced with the random number, otherwise the element remains unchanged. This is done for every element of every weight vector. With the resultant 20/30 weight vectors (strings), or new generation, one returns to step 1.

## 3. Design of experiments

## 3.1. Monte Carlo

This paper compares the in-sample forecast performance and reliability of the MLFFNN to that of traditional econometric forecasting procedures via a Monte Carlo experiment. The Monte Carlo design is identical to that of Maasoumi and Jeong [39] (see also Westbrook and Rhodes [66], Jeong [24], Maasoumi [38], or Powell [47]). With this design there are two simultaneous equation models, Model A and Model B. Each model consists of two equations and four exogenous variables with a total of two degrees of over-identification. Model A is given by the following two equations:

$$
y _ {1} - 0. 5 y _ {2} + 0. 5 x _ {1} - 0. 7 5 x _ {2} = \epsilon_ {1},\tag{2}
$$

$$
- 4. 0 y _ {1} + y _ {2} + 4. 0 x _ {3} - 1. 6 x _ {4} = \epsilon_ {2},\tag{3}
$$

or simply

$$
\mathrm{YB} + \mathrm{X} \Gamma = \epsilon ,\tag{4}
$$

$$
\text { where } \epsilon = [ \epsilon_ {1}, \epsilon_ {2} ],
$$

$$
\mathbf {B} = \left[ \begin{array}{c c} 1. 0 & - 4. 0 \\ - 0. 5 & 1. 0 \end{array} \right],\tag{5}
$$

and

$$
\Gamma = \left[ \begin{array}{c c} 0. 5 & 0. 0 \\ - 0. 7 5 & 0. 0 \\ 0. 0 & 4. 0 \\ 0. 0 & - 1. 6 \end{array} \right].\tag{6}
$$

As can be seen equations (2) and (3) above are each over-identified by one degree. The reduced form model can then be defined as:

$$
\mathbf {Y} = \mathbf {X} \Pi + V,\tag{7}
$$

where

$$
V = \left[ \epsilon_ {1}, \epsilon_ {2} \right] B ^ {- 1},\tag{8}
$$

and

$$
\Pi = - \Gamma \mathbf {B} ^ {- 1} = \left[ \begin{array}{c c} 0. 5 & 2. 0 \\ - 0. 7 5 & - 3. 0 \\ 2. 0 & 4. 0 \\ - 0. 8 & - 1. 6 \end{array} \right].\tag{9}
$$

II represents the matrix of “true” reduced form parameter values. Model B is given by the following two equations:

$$
y _ {1} - 0. 5 y _ {2} + 0. 5 x _ {1} - 0. 7 5 x _ {2} + 4. 0 x _ {3} = \epsilon_ {1},
$$

$$
- 4. 0 y _ {1} + y _ {2} - 1. 6 x 4 = \epsilon_ {2},\tag{10}
$$

$$
\text { or   simply }\tag{11}
$$

$$
\mathrm{YB} + \mathrm{X} \Gamma = \epsilon ,\tag{12}
$$

$$
\text { where } \epsilon = [ \epsilon_ {1}, \epsilon_ {2} ],
$$

$$
\mathbf {B} = \left[ \begin{array}{c c} 1. 0 & - 4. 0 \\ - 0. 5 & 1. 0 \end{array} \right],\tag{13}
$$

and

$$
\Gamma = \left[ \begin{array}{c c} 0. 5 & 0. 0 \\ - 0. 7 5 & 0. 0 \\ 4. 0 & 0. 0 \\ 0. 0 & - 1. 6 \end{array} \right].\tag{14}
$$

Here, equation (10) is just identified while equation (11) is over-identified by two degrees. Model B's reduced form is given by

$$
\mathbf {Y} = \mathbf {X} \Pi + V,\tag{15}
$$

where

$$
\Pi = - \Gamma \mathbf {B} ^ {- 1} = \left[ \begin{array}{c c} 0. 5 & 2. 0 \\ - 0. 7 5 & - 3. 0 \\ 4. 0 & 1 6. 0 \\ - 0. 8 & - 1. 6 \end{array} \right].\tag{16}
$$

The experiment analyzed here corresponds to Massoumi and Jeong's experiment 1, where the models are correctly specified. That is, data generated with model A (B) is used to estimate model A's (B's) structure. The design matrix X, consisting of the four exogenous variables, is the same for each model. The data matrix is designed such that $|\mathbf{X}'\mathbf{X}| = |T\mathbf{I}_4| = T^4$ , where $T$ is the number of observations (i.e., $T = 24$ ). Thus, multi-collinearity among the exogenous variables is eliminated and the sampling variances of OLS, 2SLS and 3SLS's structural parameter estimates will not be overexaggerated [25]. As is commonly known, multi-collinearity will increase the variance of the traditional econometric estimators ([25], p. 239). The presence of multi-collinearity, therefore, would only strengthen the comparative results below; or, in other words, in the presence of multicollinearity, the performance of the neural network would improve even more over the traditional techniques. These data matrices are identical to the ones employed by Maasoumi and Jeong [39] and were also chosen to enhance the computational accuracy (e.g., eliminate round-off error) of the traditional estimation techniques (OLS, 2SLS, and 3SLS).

For the experiment, 500 replications, based on normally distributed random disturbances, were generated. The disturbance vector $\epsilon$ has a zero mean, a structured model covariance matrix $\Sigma$ and a reduced form covariance matrix $\Omega$ . Where $\Sigma$ and $\Omega$ are identical for each of the two models and are given by:

$$
\Sigma = \left[ \begin{array}{c c} 1. 0 & 0. 5 \\ 0. 5 & 1. 0 \end{array} \right],\tag{17}
$$

$$
\Omega = \left[ \begin{array}{c c} 1. 7 5 & 6. 0 \\ 6. 0 & 2 1. 0 \end{array} \right].\tag{18}
$$

The parameter design of the two models is such that, the non-centrality parameter $\mu$ , given by:

$$
\mu = \operatorname{tr} \left(\Omega^ {- 1} \left(\frac {\Pi X ^ {\prime} X \Pi^ {\prime}}{T}\right)\right),\tag{19}
$$

is the same for both models. The non-centrality parameter is a measure of the sample variability and plays a role in determining the exact small sample distribution of the 2SLS and 3SLS estimators. The greater is the value of this parameter, the tighter will be the distribution of the econometric estimators around the true population values [49]. Specifically, Richardson [49] shows that as the non-centrality parameter increases without bound the moments of the limited-information identifiability test statistic will converge to that of the central F distribution with v numerator and $(T-K)$ denominator degrees of freedom, where v is the degrees of over-identification and K is the number of exogenous variables. For the Monte Carlo design the value of this parameter is 25.83.

Thus, given the matrix of exogenous variables, the specification of the two models, and the chosen parameter values, the design of the Monte Carlo experiment is highly favorable to the performance of the 2SLS and 3SLS estimators. That is, given the design of the experiment, the restricted reduced form estimators should perform well relative to the unrestricted reduced form estimator.

Along with these traditional estimation techniques the performance of a neural net with three layers was evaluated. The first layer was the input layer and consisted of five nodes corresponding to the four inputs and the one bias node. The input layer in Figure 4 therefore contained the four nodes $In_{1}$ to $In_{4}$ for the exogenous variables $x_{1}$ to $x_{4}$ . The second or hidden layer consisted of six nodes and the output layer had two nodes corresponding to the two outputs. Thus the output layer of Figure 4 contained only $Out_{1}$ and $Out_{2}$ corresponding to $y_{1}$ and $y_{2}$ . The hidden layer nodes also used the sigmoid function as explained in Figure 2. Each trial was trained on the twenty four data points for 15,000 generations prior to producing the in-sample forecasts. It should be noted that about 380 hours of Cyber 205 C.P.U. time was used for the neural net training (15,000 generations for 500 samples for each model). A sum of squared errors was computed using the formula

$$
\mathrm{SSE} = \sum_ {i = 1} ^ {2} \sum_ {j = 1} ^ {2 4} \left(y _ {i j} - O u t _ {i j}\right) ^ {2},\tag{20}
$$

where $y_{ij}$ refers to the observed output and $Out_{ij}$ is the neural net estimate. A population of 30 strings (weight vectors) was used for the training and a mutation rate of 0.013 was used. All weights were drawn uniformly over the range [-100, 100]. All data for the Monte Carlo study was generated on the Cyber 205 supercomputer at the University of Mississippi Center for Supercomputing Research. All programs were written in Fortran 77 and optimized using CDC Vast. Uniform deviates were generated by the random number generator on the Cyber 205 using a multiplicative congruential method with shuffling. Normal deviates were generated using the Box-Mueller algorithm [48]. See Dorsey, Johnson and Mayer [7], [8] for a more detailed discussion of the neural net optimization and estimation process.

## 3.2. Klein's Model 1

Klein's Model 1 is a macro-econometric model consisting of six equations, three of which are identities, six endogenous variables, and seven predetermined variables as follows:

$$
C = \alpha_ {0} + \alpha_ {1} P + \alpha_ {2} (w _ {1} + w _ {2}) + \alpha_ {3} P _ {t - 1} + u _ {1},\tag{21}
$$

$$
I = \beta_ {0} + \beta_ {1} P + \beta_ {2} P _ {t - 1} + \beta_ {3} K _ {t - 1} + u _ {2},\tag{22}
$$

$$
w _ {1} = \gamma_ {0} + \gamma_ {1} (Y + T - w _ {2}) + \gamma_ {2} (Y + T - w _ {2}) _ {t - 1}
$$

$$
+ \gamma_ {3} t + u _ {3},\tag{23}
$$

$$
Y + T = C + I + G,\tag{24}
$$

$$
Y = w _ {1} + w _ {2} + P,\tag{25}
$$

$$
K = K _ {t - 1} + I.\tag{26}
$$

The primary endogenous variables, as indicated by the model's specification are as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$C =$ Consumption  
$P =$ Profits  
$w_{1} =$ Private Wage Bill  
$I =$ Investment  
$Y =$ Income  
$K =$ Capital.
</div>

Variables that are exogenous to the system include:

$$
\begin{array}{r l} T & = \text { Taxes } \\ G & = \text { Government   (non   wage)   Expenditures   (27) } \\ w _ {2} & = \text { Government   Wage   Bill } \\ t & = \text { time   trend   (year   -   1931) } \end{array} \tag {28}
$$

The system is estimated on annual data for the U.S. between the two world wars. A complete description of the model and the data can be found in [27].

For the Klein model the neural net consisted of fourteen input nodes including the bias node. The thirteen input nodes correspond to the seven predetermined variables plus six of the endogenous variables. The hidden layer contained eight nodes. The output layer contained a single node that corresponds to the remaining endogenous variable. Three neural networks were constructed and trained, each of which were used to forecast C, I, and $w_{1}$ respectively. The hidden layer nodes also used the sigmoid function as explained in Figure 2. A population of 20 strings was used for the training process with a mutation rate of 0.006. All weights were drawn uniformly over the range [-100, 100].

Klein's Model 1 is employed due to its widespread use in comparing in-sample forecast reliability associated with various simultaneous equation techniques. For example, Klein [27] estimates the structural parameters of Model 1 with single-equation least squares, LIML, and FIML and calculates in-sample root-mean-square error for each of the 3 endogenous variables $C$ , $P$ , and $w_{1}$ . Chernoff and Divinsky [3], Chow [4] and Goldberger and Duncan [16] also compute FIML estimates of the structural equation parameters of Klein's Model 1. Kloek and Mennes [28] compute estimates of the model's structural parameters via 2SLS and Nagar [43] via 2SLS and classical least squares. Van der Hoek and Dijkshoorn compare FIML and full Bayesian estimation of Klein's Model 1. Their results are also discussed by Griliches and Intrilligator [14]. Maasoumi [38] and Maasoumi and Jeong [39] estimate the reduced form of Model 1 via several non-traditional Bayesian methods and calculate mean-absolute-error for the three endogenous variables.

## 4. Results

The estimates, along with the accompanying summary statistics for Klein's Model 1, as well as the summary statistics of the in-sample forecasting, were obtained using SAS Proc IML (version 6). The 2SLS estimates obtained for Klein's Model I are identical to the ones reported by SAS (SAS/ETS User's Guide, Version 5, 1984), Pindyck and Rubinfeld [46] and Kmenta [29]. Likewise, the 3SLS estimates are identical to those found in the SAS manual. There is, however, a slight difference between these estimates and those reported by Pindyck and Rubinfeld (Kmenta does not report 3SLS estimates). This difference was not resolved, but makes no difference in the comparative results below.

It is widely held that Klein's Model 1 is misspecified. When using full-information estimation techniques, such as 3SLS, misspecification of one or more equations can adversely effect the results in other equations, even if those equations are correctly specified (see for example Massoumi [38]). Klein's Model I, while yielding theoretically correct signs on the coefficient estimates, is strongly rejected by LR tests (Klein for example reports a likelihood ratio test of 94.8498. This test result, based on LIML, has a significance probability of $1.85 \times 10^{-15}$ ([27], p. 50). In fairness to Klein, it should be pointed out that Klein's Model was never intended as a definitive model of the economy. The development of the model and its subsequent use was, and is, intended as an example of simultaneous estimation procedures only.

This six-equation model of the U.S. economy, over a 22 year time period, is likely incorrect, or not equivalent to the “true” underlying model of the U.S. economy. This will likely be the case when managerial personnel, and even econometricians, attempt to specify a realisticized economic model. A technology, such as ANSs, which can facilitate and support the construction of a model would be very helpful. Even though specifying the “true” underlying model of the U.S. economy is likely improbable, the specification of relevant data is not. The user is responsible for specifying the relevant data while the neural net is responsible for model specification and estimation. Also, to managerial personnel, the complexity and economic theory of model specification is often of secondary importance, the major concern being that the final model behaves as closely as possible to the real system it represents or models. The forecast behavior (accuracy) of the final model is often an important consideration. Table 1 summarizes in-sample forecast accuracy, as measured by SSE, for each of the estimation methods. SSE is defined by the following equation:

$$
\mathrm{SSE} = \sum (y - \hat {y}) ^ {2}.\tag{29}
$$

In these experiments the data over the 22 year period was used (and in the case of 2SLS, 3SLS and ULS the appropriate specified model) to construct estimates (forecasts) of the 22 yearly-values of C, I and $w_{1}$ . For example, SSE for the MLFFNN used in forecasting C (which is 9.5356) is equal to the squared difference (or error) between the trained neural network's forecast of C and the actual value of C, summed over the 22 years. The same can be said for I and $w_{1}$ , as well as the other estimation techniques.

When the structural model was used to forecast, the MLFFNN outperformed the three econometric estimators for the primary endogenous variables as well as the total SSE for the complete model (see Table 1 last column). That is, for the consumption $(C)$ , investment $(I)$ , and the private wage bill $(w_{1})$ equations, the MLFFNN reports a smaller SSE than does the ULS estimator. For the consumption equation the SSE for the ULS estimators is 1.8750 times larger than that of the NN's. For the investment equation it is 1.3242 times as large as that reported by the NN. For the private wage $(w_{1})$ equation it is 1.01245 times as large as that reported by the NN. Because other endogenous variables are present, using ULS to estimate the structural equation for $w_{1}$ will yield inconsistent estimates.

Total sum of squared errors on Klein's Model 1 for each estimation method

<table><tr><td rowspan="2">Estimation technique</td><td colspan="4">Equation</td></tr><tr><td>C</td><td>I</td><td> $w_1$ </td><td>Total SSE (C, I,  $w_1$ )</td></tr><tr><td>Neural net</td><td>9.5356</td><td>13.0813</td><td>9.88182</td><td>32.49872</td></tr><tr><td>2SLS</td><td>21.9252</td><td>29.0469</td><td>10.00496</td><td>60.97706</td></tr><tr><td>3SLS</td><td>18.7270</td><td>43.9540</td><td>10.92056</td><td>73.60156</td></tr><tr><td>ULS</td><td>17.8794</td><td>17.3227</td><td>10.00480</td><td>45.2069</td></tr></table>

Table 2  
Monte Carlo results

<table><tr><td rowspan="2">Estimation technique</td><td colspan="2">Model A</td><td colspan="2">Model B</td></tr><tr><td> $Y_1$ </td><td> $Y_2$ </td><td> $Y_1$ </td><td> $Y_2$ </td></tr><tr><td colspan="5">In-sample RMFE</td></tr><tr><td>Neural net</td><td>1.25530</td><td>3.99546</td><td>1.00538</td><td>3.07228</td></tr><tr><td>2SLS</td><td>1.31239</td><td>4.42821</td><td>1.21995</td><td>4.34299</td></tr><tr><td>3SLS</td><td>1.32260</td><td>4.48724</td><td>1.34002</td><td>4.86554</td></tr><tr><td>ULS</td><td>1.32857</td><td>4.46391</td><td>1.26498</td><td>4.44178</td></tr><tr><td colspan="5">Ratio of experiments dominated by the NN in terms of SSE</td></tr><tr><td>NN/Total</td><td>465/500</td><td>497/500</td><td>386/500</td><td>494/500</td></tr><tr><td>NN/Total (combined)</td><td colspan="2">495/500</td><td colspan="2">450/500</td></tr></table>

Results from the Monte Carlo experiment (MCE) are more definitive of the MLFFNN's superiority. Comparison of the root mean forecast errors (RMFE) indicates that the MLFFNN outperforms the three econometric estimators for forecasting the endogenous variables in both models (See Table 2). RMFE was calculated as follows:

$$
\operatorname{RMFE} \left(Y _ {i}\right) = \sqrt {\frac {\sum_ {j = 1} ^ {5 0 0} \left(y _ {i j 1} - \hat {y} _ {i j 1}\right) ^ {2}}{5 0 0}},\tag{30}
$$

where $y_{ij1}$ is the first observation of $Y_{i}$ ( $Y_{1}$ or $Y_{2}$ ) from experiment j and $\hat{y}_{ij1}$ is the prediction (in the case of the NN this is $Out_{ij1}$ ) on the first observation of $Y_{i}$ ( $Y_{1}$ or $Y_{2}$ ) from experiment j. In Model A, the RMFEs reported by the 2SLS estimator for $Y_{1}$ and $Y_{2}$ are 1.0455 and 1.1083 times larger than those reported by the MLFFNN, respectively. In Model B they are 1.2134 and 1.4136 times larger. Recall, equation one is over-identified by one degree in Model A, while in Model B equation one is just identified. Equation two in Model A is again over-identified by one degree, while in Model B it is over-identified by two degrees. Thus, the experiment is designed to contrast the effect that differences in over-identification has on the various estimators. Since the MLFFNN dominates in all cases, degrees of over-identification have no apparent effect on its performance.

Table 2 also summarizes the relative performance of the MLFFNN for each of the 500 replications of the MCE. In Model A, the MLFFNN dominated all three of the econometric estimators in forecasting $Y_{1}$ 465 of the 500 replications. That is, of the 500 replications forecasting $Y_{1}$ , the MLFFNN reports a smaller SSE than any of the traditional econometric estimators. For $Y_{2}$ , the MLFFNN dominated 497 of the 500 replications. If $Y_{1}$ and $Y_{2}$ are combined in the MLFFNN as outputs, then the MLFFNN dominates 495 out 500 (or 99%) replications. Similar results are found for Model B (i.e., the MLFFNN dominates in the combined case 90% of the 500 replications).

The strength of the results associated with Klein's Model 1 and the Monte Carlo experiments indicates that the MLFFNN is a viable tool that can be used in the decision making process, specifically model construction and in-sample forecasting. The reader must bear in mind, however, that “experimentation can never do more than solve the problem for which” [21] the experiment was designed. The results of a particular Monte Carlo study are not an end in themselves. Rather the results of any experiment, including this one, are to be viewed as an intermediate product leading to general rules or formulas that are easily understood and applied.

For instance, as one referee correctly points out, forecast reliability may differ between in-sample and out-of-sample comparisons. It is correct that the in-sample “fitness” of a model may not necessarily lead to accurate forecast for novel data. Thus, an investigation of out-of-sample forecast reliability must be conducted to establish the value of these forecasts. The main thrust of the paper, though, is to illustrate the applicability of a MLFFNN as a tool for decision support in SES modelling. One rationale for the use of a NN, in this case, is the avoidance of manually specifying the equations of a SEM, while still allowing much flexibility in generation of a model representative of the economic system in question. Thus, the paper concentrates on in-sample forecast performance – as a measure of the NN’s degree of representation of the economic system of interest – and the ease by which a MLFFNN could generate a model of the economic system. Under this scenario the decision-maker can easily construct many different models. In addition, without the à priori restrictions (specifically those used to facilitate estimation) the decision maker is allowed to involve, to a greater extent, his/her decision making expertise (or intuition) in the analysis of the problem. The NN models would be easier to use, more understandable to, and effective for the decision-maker than if he/she only generated formulations of SEMs, especially if the decision-maker is without extensive econometric experience.

The results have clearly established that the ANS is a valid alternative to traditional econometric estimators. This is in line with the main goals of the present paper which is to establish the validity of using Artificial Neural Systems (ANS) in forecasting variables of interest from a simultaneous equations system (i.e., a Decision Support System). To accomplish this goal, the in-sample forecast reliability of the ANS was compared to that of several traditional econometric estimators using Monte Carlo techniques. Evaluation of econometric estimators in this manner is well established in the literature (e.g., Basmann et. al. [1], Maasoumi and Jeong [39], Jeong [24], among others).

In addition to the degrees of over-identification, many other considerations arise in traditional estimation. Among these are sample size, sample variability, and misspecification problems. Future research will include a comprehensive comparison of the MLFFNN and traditional econometric estimators and their relative forecasting reliability. One possibility, which was not considered before the study but which the results may indicate, is that the MLFFNN's approximation ability may allow it to approximate with great accuracy not only the SEM, but also the underlying noise generation process (or p.d.f.). To test if this is so, one should increase the sample size of each replication. In this case then, for each replication, the mean error approaches zero and this would not be an advantage for the NN over the traditional techniques. From the present study one cannot know (with certainty) if the (small) sample size was actually an advantage for the NN since "overfitting" may have occurred. As mentioned several times before, the Monte Carlo experiments were designed to give the traditional techniques substantial advantages over the MLFFNN. The authors are currently working on Monte Carlo experiments which involve larger sample sizes to address these questions, but they are beyond the scope of the present work. There has been some work indicating the ability of the MLFFNN to capture and model chaotic time-series and systems [34]. The possibility of a technique such as the MLFFNN, being powerful enough to capture or model “noise” and chaos which other techniques would fail to model, is an interesting point.

## 5. Conclusion

This paper has successfully shown that an artificial neural system (ANS) can be used as a decision support system or tool to assist a decision-maker in simultaneous equation systems (SESs) forecasting. Specifically, this paper has proposed a multi-layer feed-forward neural network (MLFFNN) to aid the decision-maker in forecasting events typically associated with SESs. The in-sample forecast reliability or accuracy of such a system was then compared to that of traditional econometric forecasting techniques. In both the Monte Carlo and Klein's Model 1 experiments the MLFFNN surpassed the performance of the econometric estimators. That is, the forecast errors of the MLFFNN, as measured by the in-sample root mean squared forecast error (RMFE) and sum of squared errors (SSE) (see tables 1 & 2) were smaller than the errors associated with the traditional econometric techniques.

With regards to forecasting, however, the ANS greatly reduces the necessary non-sample information required to arrive at a decision. With the strategy presented in this paper, the decision-maker approaches the problem domain as a black box process (e.g., Figure 1). The user's primary concern is with determining only the proper inputs and outputs to the system, for the problem at hand. This implies that the decision-maker faces, for a simultaneous equation system consisting of m endogenous and n exogenous variables, $(m+n)$ decisions or choices. Weights and functional form restrictions are determined by the NN itself. For the same system traditional econometric forecasting would require, in addition to choosing an estimation technique and, therefore, m functional forms, $m*(m-1)*n$ exclusion/inclusion restrictions on the part of the decision-maker.

The use of an ANS will allow the decision-maker to focus on the goal of the (simultaneous equations) estimation process (e.g., forecast accuracy) rather than the technical, often time-consuming, details of model specification and estimation. Using an ANS, along with other support tools specifically designed for data search and handling, will, therefore, greatly enhance the decision maker's ability to fully explore the relevancy of information and data. This should allow the decision-maker to perform better.

In using an ANS the number of hidden nodes and the length of training time is, to a certain extent, arbitrary. These two decisions, however, effect the degree of approximation accuracy of the “true” underlying simultaneous equations model. Automation of these two tasks would reduce the number of decisions faced by the decision-maker and is being investigated by the authors. In addition, to more fully explore the forecasting reliability of the ANS, both in and out-of-sample, the authors are currently investigating other experimental designs including larger sample sizes, the remaining experiments of $[38]$ and $[39]$ , nonlinear SEMs, and incomplete specifications.

## References

[1] R.L. Basmann, D.H. Richardson and R.J. Rohr, Finite Sample Distributions Associated with Stochastic Difference Equations - Some Experimental Evidence, Econometrica, 42, (1974) 825-840.

[2] H. Braun and J.S. Chandler, Predicting Stock Market Behavior through Rule Induction: An Application of the Learning-from-Example Approach, Decision Sciences, 18, Summer, (1987) 415–429.

[3] H. Chernoff and N. Divinsky, The Computation of Maximum-likelihood Estimates of Linear Structural Equations, in: W.C. Hood and T.C. Koopmans, Eds., Studies in Econometric Method, Wiley Publishing Company, New York, (1953).

[4] G.C. Chow, Two Methods of Computing Full-information Maximum Likelihood Estimates in Simultaneous Stochastic Equations, International Economic Review, 9, (1968) 100–112.

[5] G. Cybenko, Approximations by Superpositions of a Sigmoidal Function, Mathematics of Control, Signals and Systems, 2, (1989) 303–314.

[6] G.B. Davis and M.H. Olson, Management Information Systems: Conceptual Foundations, Structure, and Development, McGraw-Hill Book Company, New York, (1985).

[7] R.E. Dorsey, J.D. Johnson and W.J. Mayer, A Genetic Algorithm for the Training of Feedforward Neural Networks, forthcoming in: A.B. Whinston and J.D. Johnson, Eds., Advances in Artificial Intelligence in Economics, Finance and Management, JAI Press, Greenwhich, CT., (1992).

[8] R.E. Dorsey, J.D. Johnson and W.J. Mayer, The Genetic Adaptive Neural Network Training (GANNT) Algorithm

for Generic Feedforward Neural Networks, working paper, School of Business, The University of Mississippi, (1991).

[9] R.E. Dorsey and W.J. Mayer, Optimization Using Genetic Algorithms, forthcoming in: A.B. Whinston and J.D. Johnson, Eds., Advances in Artificial Intelligence in Economics, Finance and Management, JAI Press, Greenwhich, CT, (1992).

[10] R.E. Dorsey and W.J. Mayer, Genetic Algorithms for Estimation Problems with Multiple Optima, Non Differentiability, and Other Irregular Features, Department Working Paper, University of Mississippi Department of Economics and Finance, (1991).

[11] S. Dutta and S. Shekhar, Bond Rating: A Non-conservative Application of Neural Networks, IEEE International Conference on Neural Networks, San Diego, CA, (1988) II:443–450.

[12] M.C. Er, Decision Support Systems: A Summary, Problems, and Future Trends, Decision Support Systems, 4, (1988) 355–363.

[13] K. Funahashi, On the Approximate Realization of Continuous Mappings by Neural Networks, Neural Networks, 2, (1989) 183–192.

[14] Z. Griliches and M.D. Intriligator, Handbook of Econometrics: Volume I, North-Holland Publishing Company, New York, (1983).

[15] D.E. Goldberg, Genetic Algorithms: in Search, Optimization and Machine Learning, Addison-Wesley, Reading, MA, (1989).

[16] A.S. Goldberger and O.D. Duncan, Structural Equation Models in the Social Sciences, Seminar Press, New York, (1973).

[17] S. Ghosh, E.A. Collins and C.L. Scofield, Prediction of Mortgage Loan Performance with a Multiple Neural Network Learning System, Abstracts of the First Annual INNS Meeting, 439, (1988).

[18] D.D. Hawley, J.D. Johnson and D. Raina, Artificial Neural Systems: A New Tool for Financial Decision Making, Financial Analysts Journal, November/December, (1990).

[19] R. Hecht-Nielson, Neurocomputing, Addison-Wesley, Reading, MA, (1990).

[20] R. Hecht-Nielson, Kolmogorov's Mapping Neural Network Existence Theorem, IEEE First Int. Conf. on Neural Networks, June 21–24, (1987) III:11–14.

[21] D.F. Hendry, Monte Carlo Experimentation in Econometrics, in: Z. Griliches and M.D. Intrilligator, Eds., Handbook of Econometrics, North-Holland, (1984).

[22] K. Hornik, M. Stinchcombe and H. White, Multi-layer Feedforward Networks are Universal Approximators, Neural Networks, 2, (1989) 359–366.

[23] B. Irie and S. Miyake, Capabilities of Three-Layered Perceptrons, IEEE International Conference on Neural Networks, (1988) I:641–648.

[24] J.-H. Jeong, Stochastic Reduced Form Forecasts and Their Risk Improvements Under Structural Specification Uncertainty in a Simultaneous Equations Model, Third International Convention of Korean Economists, Aug. 2–3, (1988).

[25] J. Johnston, Econometric Methods, McGraw-Hill Book Company, New York, (1984).

[26] P.G.W. Keen, ‘Interactive’ Computer Systems for Managers: A Modest Proposal, Sloan Management Review, Fall, (1976).

[27] L.R. Klein, Economic Fluctuations in the United States, 1921–1941, John Wiley & Sons, Inc., New York, (1950).

[28] T. Kloek and L.B.M. Mennes, Simultaneous Equations Estimation Based on Principal Components of Predetermined Variables, Econometrica, 28, (1960) 45–61.

[29] J. Kmenta, Elements of Econometrics, MacMillan Publishing Company, New York, (1986).

[30] A.N. Kolmogorov, On the Representation of Continuous Functions of Many Variables by Superposition of Continuous Functions of One Variable and Addition, Dokl. Akad. Nauk USSR 114, (1957) 953–956.

[31] C.M. Kuan, Estimation of Neural Network Models, Ph.D. Dissertation, University of California, San Diego, (1989).

[32] C.M. Kuan and H. White, Predicting Appliance Ownership Using Logit, Neural Network, and Regression Tree Models, (Discussion Paper). Department of Economics, University of California, San Diego, October, (1989).

[33] T.S. Kuhn, The Structure of Scientific Revolutions, University of Chicago Press, Chicago, (1970).

[34] A. Lapedes and R. Farber, How Neural Nets Work, in: D.Z. Anderson, Ed., Neural Information Processing Systems, (Proc. of the IEEE NIPS Conf., Denver CO, 1987), Am. Inst. of Physics, New York, (1988) 442–456.

[35] K.C. Lee and S.J. Park, Decision Support in Time Series Modeling by Pattern Recognition, Decision Support Systems, 4, (1988) 199–207.

[36] Y. LeCun, Learning Processes in an Asymmetric Threshold Network, in: E. Bienenstock, F. Fogelman Souli and G. Weisbuch, Eds., Disordered Systems and Biological Organization, Springer, Berlin, (1986).

[37] G.G. Lorentz, The 13 $^{th}$ Problem of Hilbert, Proc. of Symposia in Pure Math, American Mathematical Society, 28, (1976).

[38] E. Maasoumi, Reduced Form Estimation and Prediction From Uncertain Structural Models: A Generic Approach, Journal of Econometrics, 31, (1986) 3–29.

[39] E. Maasoumi and J.-H. Jeong, A Comparison of GRF and other Reduced-form Estimators in Simultaneous Equations Models, Journal of Econometrics, 37, (1988) 115–134.

[40] A. Maren, C. Harston and R. Pap, Handbook of Neural Computing Applications, Academic Press, Inc, New York, (1990).

[41] J.L. McKenney and P.G.W. Keen, How Managers' Minds Work, Harvard Business Review, May–June, (1974) 79–90.

[42] J.T. Mentzer and R. Gomes, Evaluating a Decision Support Forecasting System, Industrial Marketing Management, 18, (1989) 313–323.

[43] A.L. Nagar, The Bias and Moment Matrix of the General k-Class Estimators of the Parameters in Simultaneous Equations, Econometrica, 27, (1959) 575–595.

[44] D.C. Park, M. El-Sharkawi, R.J. Marks II, L.E. Atlas and M. Damborg, Electric Load Forecasting Using an Artificial Neural Network, Proc. PES Winter Meeting, in press.

[45] D. Parker, Learning Logic, Technical Report TR-87, Center for Computational Research in Economics and Management Science, MIT, Cambridge, MA, (1985).

[46] R.S. Pindyck and D.L. Rubinfeld, Econometric Models and Econometric Forecasts, McGraw-Hill, New York, (1991).

[47] W.A. Powell, Limited Information Generic Reduced Form Estimation, memeo Department of Economics, Texas A & M University, (1990).

[48] Press, Flannery, Teukolsky and Vettering, Numerical Receipes, Cambridge University Press, Cambridge, (1986).

[49] D.H. Richardson, On the Distribution of the Identifiability Test Statistic, in: J. Quirk and A. Zarley, Eds., Papers in Quantitative Economics, Kansas University Press, Kansas, (1968).

[50] F. Rosenblatt, The Perceptron: a Probabilistic Model for Information Storage and Organization in the Brain, Psychological Review, 65, (1958) 386–408.

[51] H. Robbins and S. Monro, A Stochastic Approximation Method, Annals of Mathematical Statistics, 22, (1951) 400–407.

[52] D.E. Rumelhart, G.E. Hinton and R.J. Williams, Learning Internal Representation by Error Propagation, in: D.E. Rumelhart and J.L. McClelland, Eds., Parallel Distributed Processing: Exploration in the Microstructures of Cognition, MIT Press, MA, (1986) I:318–362.

[53] D.E. Rumelhart, G.E. Hinton and R.J. Williams, Learning Representations by Backpropagating Errors, Nature, 323, (1986) 533–536.

[54] R. Sharda and R.B. Patil, Neural Networks as Forecasting Experts: An Empirical Test, International Joint Conference on Neural Networks, (1990) II:491–494.

[55] H. Simon, The New Science of Management Decision, Harper and Row, New York, (1960).

[56] J.C. Smith, A Neural Network – Could It Work For You, Financial Executive, 6(3), May/June, (1990) 26–30.

[57] R.H. Sprague Jr. and B.C. McNurlin, Information Systems Management in Practice, Prentice-Hall, New Jersey, (1986).

[58] D.A. Sprecher, On the Structure of Continuous Functions of Several Variables, Trans. Amer. Math. Soc., 115, March, (1965) 340–355.

[59] R.J. Thierauf, User-Oriented Decision Support Systems, Prentice-Hall, New Jersey, (1988).

[60] G. Van der Hoek and M.W. Dijkshoorn, A Numerical Comparison of Self Scaling Variable Metric Algorithms, Report 7910/0, Erasmus University, Rotterdam.

[61] H.G. Van Dissel and H.P. Borgman, Task-Allocation between DSS and Problem Owner: The Example of Box & Jenkins Time-series Analysis, Decision Support Systems, 6, (1990) 339–345.

[62] P.D. Wasserman and T. Schwartz, Neural Network, Part 1, IEEE Expert, Winter, (1987) 10–12.

[63] P.D. Wasserman, Neural Computing: Theory and Practice, Van Nostrand Reinhold, New York, (1989).

[64] P. Werbos, Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences, Ph.D. thesis, Harvard University Committee on Applied Mathematics, (1974).

[65] P. Werbos, Advanced Forecasting Methods for Global Crisis Warning and Models of Intelligence, General Systems Yearbook, (1977).

[66] M.D. Westbrook and G.F. Rhodes Jr., Simultaneous Equations Estimators, Identifiability Test Statistics, and Structural Forms, Advances in Econometrics, 2, (1983) 129–196.

[67] H. White, Economic Prediction Using Neural Networks: The Case of IBM Daily Stock Returns, IEEE Second International Conference on Neural Networks, San Diego, (1988) II:451–458.

[68] H. White, Multi-layer Feedforward Networks can Learn Arbitrary Mappings: Connectionist Nonparametric Regression with Automatic and semiautomatic Determination of Network Complexity (Discussion Paper), Department of Economics, University of California, San Diego, CA, (1988).

[69] H. White, An Additional Hidden Unit Test for Neglected Nonlinearity in Multi-layer Feedforward Networks, Proceedings of the International Joint Conference on Neural Networks, Washington D.C., (1989).
