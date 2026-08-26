---
otero_id: 3172
otero_key: "RFXN54YJ"
title: "Selection of diagnostic techniques and instrumentation in a predictive maintenance program. A case study"
authors: "M.C. Carnero"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.09.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Selection of diagnostic techniques and instrumentation in a predictive maintenance program. A case study

M.C. Carnero\*

University of Castilla-La Mancha, Technical School of Industrial Engineering, Avda. Camilo Jose Cela s/n, 13071 Ciudad Real, Spain

Received 7 October 2002; received in revised form 22 September 2003; accepted 22 September 2003 Available online 4 November 2003

## Abstract

Predictive maintenance programs (PMPs) can provide significant advantages in relation to quality, safety, availability and cost reduction in industrial plants. Nevertheless, during implementation, different decision making processes are involved, such as the selection of the most suitable diagnostic techniques. A wrong decision can lead to the failure of the setting up of the predictive maintenance program and its elimination, with the consequent economic losses, as the setting up of these programs is a strategic decision. In this article, a model is proposed that carries out the decision making in relation to the selection of the diagnostic techniques and instrumentation in the predictive maintenance programs. The model uses a combination of tools belonging to operational research such as: analytic hierarchy process (AHP) and factor analysis (FA). The model has been tested in screw compressors when lubricant and vibration analyses are integrated. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Predictive maintenance; Decision making; Analytic hierarchy process; Factor analysis

## 1. Introduction

The continuous production process requires a high degree of availability and the elimination of unexpected breakdown that could cause a prolonged stoppage in production [9]. Predictive maintenance can contribute to improving plant availability, safety, quality, reduction of maintenance costs, etc. This has led to an increase in the number of predictive maintenance programs (PMPs) applied, but, during the setting up of a PMP, there is a number of decisions involved that lack decision support systems or models. This article aims to contribute towards resolving this problem.

Although there is a limited number of decision support systems related to predictive maintenance, the following models should be taken into consideration. In Ref. [15], a proportional-hazards model with Weibull baseline hazard function and time-dependent stochastic covariates representing monitored conditions is suggested and a software is developed to assist engineers to optimize decisions. In Ref. [30], Markov models are described for establishing optimum inspection intervals for phased deterioration of monitored complex components in a system with severe down time costs. In Ref. [16], statistical analysis of vibration data is undertaken using a software package to establish the key vibration signals that are necessary for risk estimation. Ref. [19] presents a real-time neural network-based condition monitoring system for rotating mechanical equipment. In Ref. [29], condition predictors of significant items of the system are monitoring taking into account the availability and cost-effectiveness of the monitoring techniques.

In this article, a model is presented for the selection of diagnostic techniques and instrumentation in a predictive maintenance program. To construct the model, factor analysis and analytic hierarchy process are combined. The model is applied to screw compressors which are monitored by means of PMPs based on lubricant and vibration analyses and when the aforementioned techniques are applied simultaneously.

The layout of the paper is as follows. Section 2 is an introduction to predictive maintenance techniques, lubricant and vibration analyses and the integration of both techniques are presented. Section 3 describes the characteristics of the mathematical tools used in the construction of the decision support model proposed: factor analysis and analytic hierarchy process. Section 4 presents the model for the selection of diagnostic techniques and instrumentation in predictive maintenance. Section 5 describes the application of the model to a screw compressor. Section 6 presents the results obtained from applying the model to a PMP integrating lubricant and vibration analyses. Section 7 presents the conclusions.

## 2. Predictive maintenance techniques: lubricant and vibration analyses

Predictive maintenance is a maintenance policy in which selected physical parameters associated with an operating machine are sensed, measured and recorded intermittently or continuously for the purpose of reducing, analyzing, comparing and displaying the data and information so obtained for support decisions related to the operation and maintenance of the machine [5]. There are numerous predictive techniques, as can be checked in Ref. [12]: lubricant analysis, vibration analysis, thermography, penetrating liquids, radiography, ultrasound, control of corrosion, etc.; each technique is applied to a type of specific industrial equipment.

The advantages of the introduction of predictive maintenance programs (PMPs) are:

 Exclusive control of the machines that show the beginning of a malfunction.

 An increase in the availability of the industrial plants [40].

 The capacity to carry out quality checks of both internal and subcontracted maintenance interventions.

 An increase in the security of the factory [9].

 It facilitates certification and ensures the verification of the requisites of the standard ISO 9000.

 Provides the best programming of maintenance actions.

 Enables the effective programming of supplies and staff.

 Production quality is optimized by operating machinery without interruption due to failures [21].

 Support in the design phase of equipment, particularly by means of the application of modal analysis [3].

 Reduction of direct maintenance costs by checking only the equipment that is developing a fault [38].

 By keeping to delivery dates, and by satisfying the customers’ demand for quality, the image of the company is improved.

 Costs are brought down in relation to spare parts and labour [18].

 By maintaining the industrial equipment operational whilst applying the predictive tools, the measuring process does not directly affect the availability of the equipment.

 Decrease in the costs related to insurance policies as security within the factory increases.

 Historical information on each piece of equipment is completed, which helps to determine reliability parameters and to optimize maintenance planning [2]. This information on the machines and equipment is available to the management for decision making.

 Reduction of energy consumption.

Industrial plants generally possess PMPs based on vibration analysis [4], whereas medium-sized companies are starting to incorporate them in their Maintenance Departments. Their suitability for application to rotary and reciprocating machines [36], which can be considered to be the most widely used in general, as well as their high capacity of diagnosis, make them the most versatile predictive technique. In order to carry out the setting up of a PMP based on vibration analysis, it is vital to understand their technical peculiarities, regarding instrumentation, procedures and uses that make the production of diagnoses possible. The success or failure of the setting up process will depend on the program planner’s knowledge of these subjects.

According to Ref. [37], the presence of a fault in industrial equipment, whilst still in its incipient phase, will be accompanied by a detectable increase or modification of vibratory signals. There is a wide range of diagnostic techniques that can be applied in vibration analysis to identify anomalies in machinery. It is necessary to investigate which is the most appropriate technique or techniques for diagnosis in a specific machine; the operating conditions that exist, the degree of criticality of the machine, the means, as well as the personnel available for the control of the analysis, are determining factors of the analysis to be performed.

There are two types of PMPs based on vibration analysis: with portable instrumentation and on-line acquisition system. With the portable system, data are acquired at periodic intervals of time and are later downloaded onto a computer [8]. The discontinuous character hinders the obtaining of information regarding the starting up and stopping of machinery and the instants in which the process parameters change. The costs of this type of PMP are lower than an on-line system because the installation of instrumentation is not needed and the number of sensors can be reduced.

In on-line systems, the sensors are fixed in the measurement position, information being obtained online of the level of vibrations, which includes information of transitory states such as starting up and stopping [5]. The costs of implementation are very much higher than in the case of portable systems, and consequently, it is applied to critical machinery or that found in dangerous environments.

The distinction between portable systems and online systems will be illustrated in the model proposed later; different results being obtained in each case.

Lubricant analysis consists of analysis of the state of different physical and chemical parameters of oil in order to verify the condition of the lubricant and the machinery which requires investigation of the state of wear of the equipment, level of oil contamination, and oil condition and includes a recommendation outlining any corrective or preventive maintenance actions that are necessary [39]. In the PMPs based on lubricant analysis dispersion in the information available about each test has been detected in managerial and laboratory practice and there are no specifications on the collections of tests that provide the most effective information [26]. It has also been appreciated that PMPs are supported by tests that provide redundant information. There is also a shortage of information about the latest generation technology that enables this type of analysis and imprecisions in the industrial plants that try to implement a program also exist [8].

All the diagnostic techniques used in a PMP based on lubricant analysis can have top limits, bottom limits or both. The evolution of each parameter can be represented depending on the hours of operability of the lubricant. The value of the curve in the analysis of trend not only shows the evolution of the condition of the lubricant and the machine, but also the speed at which the abovementioned transformation takes place. The intersection of the line that establishes the trend with the value of the limit that is first reached, whether bottom or top, tells us the time that must pass before a state of danger is reached; this characteristic represents the remaining life time of the equipment [13].

The diagnostic techniques based on vibration and lubricant analysis that are applied at present appear in Table 1. There are diagnostic techniques that provide quantitative data (to which factor analysis will be applied) and others that give qualitative information.

The integration of lubricant and vibration analyses can provide significant profits, which so far have not been sufficiently analyzed. For this reason, we will now go on to detail the most relevant characteristics that a predictive maintenance program that integrates the analysis of vibrations and lubricants must possess.

A PMP integrating vibration and lubricant analysis involves the acquisition of information of both techniques, in order to correlate all the predictive information to obtain an early diagnosis of the root causes of the failures and the prediction of their consequences on the machinery.

Besides the benefits previously mentioned obtained through the application of a PMP, the integration of predictive techniques provides the following additional advantages:

Table 1  
Diagnostic techniques in lubricant and vibration analyses [8]

<table><tr><td>Vibration analysis</td><td>Lubricant analysis</td></tr><tr><td>Spectral analysis</td><td>ViscosityIndex of viscosity</td></tr><tr><td>Analysis of harmonic and orders</td><td>Water contentTotal acid number</td></tr><tr><td>Trend of the global value of vibration</td><td>Total basic number</td></tr><tr><td>Cepstrum</td><td>Insoluble in pentane and benzene</td></tr><tr><td>Analysis of temporary signal</td><td>Freezing pointIgniting point</td></tr><tr><td>Spike energy</td><td>Combustion pointDemulsibility</td></tr><tr><td>Bode plot</td><td>Tendency to foamingTendency to formation of coal and ash content</td></tr><tr><td>Polar plot</td><td>Corrosion to copper sheet</td></tr><tr><td>Waterfalls</td><td>Resistance to oxidationColour</td></tr><tr><td>Orbital analysis</td><td>Stain of oilPoint of aniline</td></tr><tr><td>Statistical analysis</td><td>Interfacial tensionDielectric stiffness</td></tr><tr><td>Hilbert transform</td><td>Spectroscopy of atomic emission</td></tr><tr><td>Envelope</td><td>Infrared spectroscopy through Fourier transform (FTIR)</td></tr><tr><td>Modal analysis</td><td>FerrografyParticles count</td></tr></table>

An increase in the number of pieces of equipment covered by a PMP. Vibration analysis is generally applied in industrial plants, due to the prevalence of rotary and reciprocating machinery, whereas lubricant analysis has been adopted by machine tool, maritime and terrestrial fleets and electrical substations submitted to significant operational loads, etc. [35].

 An increase in the set of anomalies that can be controlled. Certain types of damage can only be investigated by means of one of the predictive techniques [17].

Guarantee of the diagnoses provided as the information from both techniques is contrasted. All the techniques present deficiencies [5,6,20], and it is therefore advisable to confirm the diagnosis.

 Each of the predictive techniques detects deterioration in different phases of its evolution [25]. Lubricant analysis is capable of detecting the anomaly in the early phases of its development, whereas vibration analysis will only be able to evaluate it when the breakdown has already occurred.

 Detection of the root causes of the failures [24,35].

Consequently, there is an intensification and improvement of the level of information regarding incidents that can be transmitted to the personnel in charge of corrective activities.

Nevertheless, the simultaneous application of both predictive techniques does not necessarily mean their integration. The computer applications that have been reviewed have designed the databases of each of the predictive technologies on an independent basis and without establishing any link of union between them [23]. Furthermore, the instrumentation used in each of the predictive techniques usually comes from different manufacturers, which also impedes the integration of the information [22].

The capacity of integration of particle counting and ferrography techniques with spectral analysis is demonstrated in the processes of wear and pollution that lead to a mechanical breakdown [10]. The condition of the equipment can be determined by means of spectral analysis, and ferrographical analysis will determine with accuracy the element or component that is developing the anomaly; particle counting can also determine the gradient of change of the condition and determine if the initial cause of the failure is due to an external factor. The periodic use of spectra in waterfall is suggested as a diagnostic technology, as it is a technique that identifies the condition of the equipment and the failure that has developed, aspects that cannot be investigated by means of other diagnostic techniques; moreover, as it is carried out by means of comparison, it restricts the time of identification of the failure.

The application of the diagnostic techniques on an independent basis is recommended until as much knowledge as possible has been obtained using each technique individually, in order to later proceed to their integration. Once this level has been reached, it would be convenient to have software available that incorporates utilities for this integration.

3. Introduction to the tools factor analysis and analytic hierarchy process

## 3.1. Factor analysis

Factor analysis (FA) is a statistical procedure used to determine the basic essential variables underlying a large number of interrelated variables; a method of processing data comprising too many variables to allow direct analysis [27].

In FA, the researcher is usually interested in discovering which variables in a data set form a coherent subgroup that are relatively independent of one another. The specific goal of analysis may be to outline patterns of intercorrelatives among variables, to reduce a large number of variables to a smaller number of clusters while retaining maximum spread among experimental units, (to provide an operational definition (a regression equation) for an unobserved, hypothetical construct by using observed variables, or to test a theory about the nature of underlying variables.

Steps in a FA includes:

 Selecting and measuring a group of variables.

 Preparing the correlation matrix.

 Determining the number of components or factors to be considered.

 Extracting a set of components or factors from the correlation matrix.

 Rotating the components or factors to increase interpretability.

 Interpreting the results.

The correlation matrix R can be diagonalized accomplishing and premultiplying it by the matrix V and its transpose VV[1].

$$
\mathbf {L} = \mathbf {V} ^ {\prime} \mathbf {R V}\tag{1}
$$

The matrix of eigenvectors V premultiplied by its transpose produces the identity matrix:

$$
\mathbf {V} ^ {\prime} \mathbf {V} = \mathbf {I}\tag{2}
$$

so, reorganising Eq. (1):

$$
\mathbf {R} = \mathbf {V L V ^ {\prime}}\tag{3}
$$

the correlation matrix can be decomposed,

$$
\mathbf {R} = (\mathbf {V} \sqrt {\mathbf {L}}) (\sqrt {\mathbf {L}} \mathbf {V} ^ {\prime})\tag{4}
$$

If $\mathbf { V } \sqrt { \mathbf { L } }$ is called A (factor loading matrix), then

$$
\mathbf {R} = \mathbf {A A} ^ {\prime}\tag{5}
$$

this equation is called the fundamental equation for FA.

The matrix A contains correlations between factors and variables. Usually a factor is more interpretable when a few variables load highly on it and the rest do not. The factorial matrix indicates the relation between the factors and the variables. Nevertheless, it is often difficult to interpret the factors from the factorial matrix. To facilitate the interpretation the matrix is rotated.

The rotation consists of turning the axes of coordinates, which represent the factors, until they are as close as possible to the variables in which they are saturated. The saturation of factors transforms the initial factorial matrix into another matrix called a factorial rotated matrix, of easier interpretation. The factorial rotated matrix is a linear combination of the first one and explains the same quantity of initial variance [11]. Rotating is normally used after extracting to maximise high correlations and minimise low ones.

Several methods of rotation exist. The most advisable is orthogonal rotation, and of these the most used type is the varimax. The varimax technique accomplishes this aim by means of a transformation matrix  [1].

$$
\boldsymbol {\Lambda} = \left( \begin{array}{c c} \cos \psi & - \sin \psi \\ \sin \psi & \cos \psi \end{array} \right)
$$

being $\psi$ the rotation angle. Then,

$$
\mathbf {A} _ {\mathrm{unrorated}} \boldsymbol {\Lambda} = \mathbf {A} _ {\mathrm{rotated}}\tag{6}
$$

$$
\bar {\mathbf {R}} = \mathbf {A} _ {\text { unrotated }} \mathbf {A} _ {\text { unrotated }} ^ {\prime}\tag{7}
$$

$$
\mathbf {R} _ {\mathrm{res}} = \mathbf {R} - \bar {\mathbf {R}}\tag{8}
$$

the elements of this matrix must be small.

Regression coefficients for producing factor scores from variable scores are a product of the inverse of the correlation matrix and the factor loading matrix

$$
\mathbf {B} = \mathbf {R} ^ {- 1} \mathbf {A}\tag{9}
$$

Factor scores are a product of standardised scores on variables and regression coefficients.

$$
F = Z B\tag{10}
$$

Standardised scores on variables may be predicted as a product of scores on factors weighted by factor loading.

$$
Z = F \mathbf {A} ^ {\prime}\tag{11}
$$

Correlations among factors may be obtained by producing a matrix of cross products of standardised factor scores and dividing the results by the number of cases minus one.

$$
\phi = \left(\frac {1}{N - 1}\right) F F ^ {\prime}\tag{12}
$$

The structure matrix C is a product of the pattern matrix of correlating among factors.

$$
\mathbf {C} = \mathbf {A} \phi\tag{13}
$$

In the phase of interpretation, the following steps are considered to be fundamental:

 The study of the composition of the significant factorial saturations of each factor.

 The naming of the factors. The name must coincide with the structure of the saturations.

## 3.2. Analytic hierarchy process

Decision analysis is used when a decision maker wishes to evaluate the performance of a number of alternative solutions for a given problem. These alternatives can be evaluated in terms of a number of decision criteria. Often an alternative may be superior in terms of one or some of the decision criteria, but inferior in terms of some other criteria. The objective of using an analytic hierarchy process (AHP) is to identify the preferred alternative and also determine a ranking of the alternatives when all the decision criteria are considered simultaneously [33]. The use of AHP instead of another multicriteria technique is due to the following reasons:

 Quantitative and qualitative criteria can be included in the decision making.

 A large quantity of criteria can be considered.

 A flexible hierarchy can be constructed according to the problem.

With AHP, a complete classification of alternatives can be obtained. Therefore, a hierarchy must be constructed as shown in Fig. 1. In this hierarchy, the relationship between the goal, criteria, subcriteria and alternatives is established.

There are three main steps involved in using AHP:

 The relevant criteria and alternatives must be determined.

 Numerical measures must be attached according to the relative importance (weights) of the criteria and the relative performance of the alternatives to these criteria.

 The numerical values must be processed in order to determine a ranking of each alternative.

In a decision making problem, M alternatives $A _ { i }$ $( i = 1 , 2 , 3 , . . . , M )$ and N criteria $C _ { j } \left( j = 1 , 2 , 3 , . . . , N \right)$ are considered.

In order to determine the relative importance of the alternatives with regard to each of the criteria or between two criteria, linguistic terms are used that include the judgments of the decision maker. The linguistic terms are generally associated to numerical values constituting a scale [34].

![](/api/attachments/RFXN54YJ/fulltext/images/95d203784fdb0b6423fa1ec9dec07faad9c4235f00b834e79ecc808784e4c7fd.jpg)  
Fig. 1. AHP hierarchy.

The scale proposed by Saaty is shown in Table 2. The quantified judgment on pair of criteria $C _ { i }$ and $C _ { j }$ are represented by an $N \times N$ matrix A:

$$
A = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \dots & \dots & \dots & \dots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right]\tag{14}
$$

where the $a _ { i j }$ is the relative importance of $C _ { i }$ to $C _ { j } .$

The quantified judgment between alternatives with respect to criteria $C _ { i }$ is represented by an $M \times M$ matrix.

The following rules must be verified:

If $a _ { i j } = \alpha$ then $a _ { j i } = 1 / \alpha , \ : \alpha = 0 .$

If $C _ { i }$ is judged to be of equal relative importance as C<sub>j</sub>, then $a _ { i j } = a _ { j i } = 1$ , and $a _ { i i } = 1$ for all i.

If all the comparisons are perfectly consistent, then the relation:

$$
a _ {i k} = a _ {i j} a _ {j k} \quad \forall i, j, k.\tag{15}
$$

should always be true for any combination of comparisons taken from the judgment matrix.

When exact measurements of the criteria in a scale are available for carrying out the comparisons, that is to say, $w _ { 1 } , w _ { 2 } , . . . , w _ { n } ,$ a perfectly consistent matrix is obtained that verifies [28]:

$$
\frac {w _ {i}}{w _ {j}} = a _ {i j} \quad i, j = 1, 2, \ldots , n,\tag{16}
$$

From the previous expression, it can be deduced that:

$$
\frac {w _ {j}}{w _ {i}} a _ {i j} = 1 \quad i, j = 1, 2, \ldots , n,\tag{17}
$$

and then:

$$
\sum_ {j = 1} ^ {n} a _ {i j} \frac {w _ {j}}{w _ {i}} = n \quad i = 1, 2, \dots , n,\tag{18}
$$

or:

$$
\sum_ {j = 1} ^ {n} a _ {i j} w _ {j} = n w _ {i} \quad i = 1, 2, \dots , n,\tag{19}
$$

and is expressed in its matricial form as [28]:

$$
\mathbf {A} w = n w,\tag{20}
$$

where w is an eigenvector of A with eigenvalue n.

That is to say, since the comparisons matrix possesses a range 1, all the eigenvalues are zero except one with value n. The sum of the eigenvalues of a positive matrix is equal to the trace of the matrix, and the eigenvalue different to zero is named maximum eigenvalue $( \lambda _ { \mathrm { m a x } } )$

Table 2  
Scale of relative importances [28]

<table><tr><td>Intensity of importance</td><td>Verbal scale</td><td>Explanation</td></tr><tr><td>1</td><td>Equal importance</td><td>Two activities contribute equally to the objective</td></tr><tr><td>3</td><td>Weak importance of one over another</td><td>Experience and judgment slightly favour one activity over another</td></tr><tr><td>5</td><td>Essential or strong importance</td><td>Experience and judgment strongly favour one activity over another</td></tr><tr><td>7</td><td>Demonstrated importance</td><td>An activity is strongly favoured and its dominance demonstrated in practice</td></tr><tr><td>9</td><td>Absolute importance</td><td>The evidence favouring one activity over another is of the highest possible order of affirmation</td></tr><tr><td>2, 4, 6, 8</td><td>Intermediate values between the two adjacent judgments</td><td>When compromise is needed</td></tr><tr><td>Reciprocals of above numbers</td><td>If activity i has one of the above (nonzero) numbers assigned to it when compared with activity j, then j has the reciprocal value when compared with i</td><td>-</td></tr></table>

If the matrix A is not consistent and $\lambda _ { 1 } , . . . , \lambda _ { n }$ is the set of eigenvalues that contribute a solution to the previous matricial expression, the following expression is verified:

$$
\text {   If   } a _ {i i} = 1, \quad \forall i \Rightarrow \sum_ {i = 1} ^ {n} \lambda_ {i} = n\tag{21}
$$

and $w _ { i }$ approaches the average of n elements of line i in the normalized matrix N.

If w¯ is calculated from the procedure described in Ref. [28]:

$$
\alpha = \sum_ {i = 1} ^ {n} w _ {i},\tag{22}
$$

and $\bar { w }$ is replaced by:

$$
\frac {1}{\alpha} w,\tag{23}
$$

is verified [31]:

$$
\mathbf {A} \bar {w} = \lambda_ {\mathrm{max}} \bar {w},\tag{24}
$$

where $\lambda _ { \operatorname* { m a x } } \geq n .$

The closer $\lambda _ { \operatorname* { m a x } }$ is to n, the more consistent it is with the comparison matrix A or the more coherent will be the judgments provided. The consistency index (CI) is used as a measurement of the consistency of the judgments expressed [28]:

$$
\mathrm{CI} = \frac {\lambda_ {\max} - n}{n - 1}\tag{25}
$$

Therefore, the CI represents an average of the eigenvalues.

The consistency ratio (CR) is obtained by dividing the CI value by the corresponding random consistency index (RCI) value as given in Table 3. The RCI was evaluated by Saaty through the generation of a random matrix with different dimensions (n) [14,32].

In the AHP, the pairwise comparisons in a judgment matrix are considered to be adequately consistent if the corresponding CR is less than 10%. If the CR value is greater than 0.10, then a re-evaluation of the pairwise comparisons is recommended. However, perfect consistency rarely occurs in practice.

Finally, a synthesis must be performed. Synthesis is the process of weighting and combining priorities throughout the model that leads to the overall results. Synthesis from the goal node multiplies the weight of each parent node times the local priorities of its children nodes and of those children times the local priorities of their children. This process continues down to and including the alternatives.

## 4. Model for the selection of diagnostic techniques and instrumentation in a predictive maintenance program

In the design and planning phase of a PMP, the model for the selection of diagnostic techniques and instrumentation in a predictive maintenance program (MSDT-PMP) can be applied. This decision support system helps to solve an unstructured problem, in which the decision maker has doubts as to which alternative should be selected.

The decision support model proposed can be extended to any other machines or techniques getting data from the extension or globalisation phase of a PMP. This phase is characterized by the fact that the time needed to get a return on the investment has been reached and, the number of machines under control is increased or else new objectives are set.

The PMPs have been categorised at different technological levels depending on cost and diagnostic capacity [8]:

 Level 0. Setup carried out using the control of sensitive variables. The cost is practically zero and the diagnostic capacity is very low.

Table 3  
Values of random consistency index

<table><tr><td>n</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>RCI</td><td>0</td><td>0</td><td>0.58</td><td>0.90</td><td>1.12</td><td>1.24</td><td>1.32</td><td>1.41</td><td>1.45</td><td>1.49</td><td>1.51</td><td>1.48</td><td>1.56</td><td>1.57</td><td>1.59</td></tr></table>

 Level 1. Assumes the use of elementary instrumentation, like vibrometers or devices to do the crackle test.

 Level 2. Uses more sophisticated instrumentation, like vibration analyzers, data processing software, or viscometers.

 Level 3. The cost is high as sophisticated analysis machines are in use; diagnostic capacity is excellent.

The model is elaborated taking into consideration the previous technological levels of the predictive techniques, lubricant and vibration analyses and the integration of both techniques.

When a solution has been obtained from the evaluation of the viability of the setting up of the PMP, the most appropriate diagnostic technique must be selected according to the type of machinery, technical and economic characteristics and aspects related to the human resources required, etc. For this purpose, the model for the selection of diagnostic techniques and instrumentation in a predictive maintenance program (MSDT-PMP) has been designed.

The selection of lubricant and vibration analyses from the range of predictive techniques is due to the fact that these are applied in a higher number of industrial plants [9]. The introduction of the integration of both techniques is due to the fact that the results obtained in this diagnosis are different with respect to the application of the same techniques in isolation. This last alternative is the most advanced step of technological maintenance.

The differentiation between portable and on-line systems is related to the technological levels of a PMP. Therefore, in the case of on-line systems, only the technological level 3 is considered, corresponding to the most technologically evolved.

With regards to the integration of the diagnostic techniques, the technological level applied in both predictive techniques should be similar.

The procedure developed to elaborate the model consists of carrying out a factor analysis (FA) with the information supplied by the diagnostic parameters. By doing this, the aim is to eliminate the redundant information and to keep the most relevant information for a later analysis. When several predictive techniques are applied, the factor analysis also allows the obtaining of the relevant parameters that favour the integration of techniques. The application of this technique is due to the fact that the number of parameters used in predictive maintenance is high and does not always provide information or this information is redundant [26]. By using FA, we aim to get a set of variables that constitutes a coherent subgroup and with independent elements.

FA is applied to the diagnostic predictive techniques that provide quantitative data. The quantitative information supplied by the diagnostic techniques selected by the factors resulting from FA is completed with the incorporation of qualitative information coming from other diagnostic techniques, where the results of analysis do not give numerical results. The previous process is applied to each technological level of a PMP and that will be reviewed in this paper.

![](/api/attachments/RFXN54YJ/fulltext/images/4747ca774574639960135f86f879d3b4f0fbf6ecb689b8abb141e0b00ed69d5b.jpg)  
Fig. 2. Hierarchy of MSTD-PMP.

Table 4  
Pairwise comparison matrix and eigenvectors in a PMP based on lubricant and vibration analyses

<table><tr><td colspan="6">Technological level 3</td></tr><tr><td rowspan="2"></td><td colspan="4">Criteria</td><td rowspan="2">Eigenvector</td></tr><tr><td>D</td><td>Q</td><td>COST</td><td>SUP</td></tr><tr><td colspan="6">Lubricant analysis (portable system)</td></tr><tr><td>D</td><td>1</td><td>2</td><td>2</td><td>3</td><td>0.424</td></tr><tr><td>Q</td><td>1/2</td><td>1</td><td>1</td><td>2</td><td>0.227</td></tr><tr><td>COST</td><td>1/2</td><td>1</td><td>1</td><td>2</td><td>0.227</td></tr><tr><td>SUP</td><td>1/3</td><td>1/2</td><td>1/2</td><td>1</td><td>0.122</td></tr><tr><td colspan="6">Vibration analysis (portable system)</td></tr><tr><td>D</td><td>1</td><td>2</td><td>2</td><td>3</td><td>0.424</td></tr><tr><td>Q</td><td>1/2</td><td>1</td><td>1</td><td>2</td><td>0.227</td></tr><tr><td>COST</td><td>1/2</td><td>1</td><td>1</td><td>2</td><td>0.227</td></tr><tr><td>SUP</td><td>1/3</td><td>1/2</td><td>1/2</td><td>1</td><td>0.122</td></tr><tr><td colspan="6">Vibrationanalysis (on-line system)</td></tr><tr><td>D</td><td>1</td><td>2</td><td>3</td><td>3</td><td>0.455</td></tr><tr><td>Q</td><td>1/2</td><td>1</td><td>1</td><td>2</td><td>0.141</td></tr><tr><td>COST</td><td>1/3</td><td>1</td><td>1</td><td>1</td><td>0.263</td></tr><tr><td>SUP</td><td>1/3</td><td>1/2</td><td>1</td><td>1</td><td>0.141</td></tr></table>

The most significant diagnostic techniques regarding each technological level related to the factors obtained from the FA and the qualitative diagnostic techniques are incorporated as alternatives in a hierarchy to which AHP is applied. By means of this procedure, the techniques that provide redundant information and the techniques that do not give relevant information for diagnosis are eliminated and the integration of vibration and lubricant analysis is favoured.

The decision variables used to construct the hierarchy are:

 Diagnostic quality (D).

 Quantity of failures that can be analyzed ( Q).

 Cost of diagnostic technique (COST). This variable is decomposed in investment cost (INVC), setup cost (SETC) and maintenance cost (MANC) of the diagnostic technique.

 Supportability of the diagnostic technique (SUP). This variable includes: quantity of training needed to apply the technique (T), its portability ( P), negative influences on the human resources due to its application (HR), its maintainability (M) and easy use (EU).

In the case of a PMP integrating lubricant and vibration analyses, the variable capacity of integration (INT) is incorporated to favour the integration process of predictive techniques and to avoid the selection of incompatible techniques.

The hierarchy elaborated with the goal, decision variables and alternatives is shown in Fig. 2.

As examples, the pairwise matrix and eigenvectors obtained from the criteria corresponding to technological level 3 in a PMP based on lubricant analysis and vibration analysis are in Table 4 As can be appreciated in Table 4, on-line system is associated to vibration analysis, because the instrumentation in lubricant analysis is placed in laboratories and the data are always periodic.

Table 5  
Pairwise comparison matrix and eigenvectors in a PMP based on the integration of lubricant and vibration analyses

<table><tr><td rowspan="2"></td><td colspan="5">Criteria</td><td rowspan="2">Eigenvector</td></tr><tr><td>D</td><td>Q</td><td>COST</td><td>SUP</td><td>INT</td></tr><tr><td colspan="7">Technological level 0 (portable system)</td></tr><tr><td>D</td><td>1</td><td>2</td><td>2</td><td>3</td><td>1</td><td>0.298</td></tr><tr><td>Q</td><td>1/2</td><td>1</td><td>1</td><td>2</td><td>1/2</td><td>0.158</td></tr><tr><td>COST</td><td>1/2</td><td>1</td><td>1</td><td>2</td><td>1/2</td><td>0.158</td></tr><tr><td>SUP</td><td>1/3</td><td>1/2</td><td>1/2</td><td>1</td><td>1/3</td><td>0.089</td></tr><tr><td>INT</td><td>1</td><td>2</td><td>2</td><td>3</td><td>1</td><td>0.298</td></tr><tr><td colspan="7">Technological level 1 (portable system)</td></tr><tr><td>D</td><td>1</td><td>2</td><td>2</td><td>3</td><td>1</td><td>0.298</td></tr><tr><td>Q</td><td>1/2</td><td>1</td><td>1</td><td>2</td><td>1/2</td><td>0.158</td></tr><tr><td>COST</td><td>1/2</td><td>1</td><td>1</td><td>2</td><td>1/2</td><td>0.158</td></tr><tr><td>SUP</td><td>1/3</td><td>1/2</td><td>1/2</td><td>1</td><td> $1/3$ </td><td>0.089</td></tr><tr><td>INT</td><td>1</td><td>2</td><td>2</td><td>3</td><td>1</td><td>0.298</td></tr><tr><td colspan="7">Technological level 2 (portable system)</td></tr><tr><td>D</td><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>0.320</td></tr><tr><td>Q</td><td>1/2</td><td>1</td><td>1</td><td>3</td><td>1/3</td><td>0.159</td></tr><tr><td>COST</td><td>1/3</td><td>1</td><td>1</td><td>3</td><td>1/2</td><td>0.138</td></tr><tr><td>SUP</td><td>1/4</td><td>1/3</td><td>1/3</td><td>1</td><td>1/4</td><td>0.063</td></tr><tr><td>INT</td><td>1</td><td>3</td><td>2</td><td>4</td><td>1</td><td>0.320</td></tr><tr><td colspan="7">Technological level 3 (portable system)</td></tr><tr><td>D</td><td>1</td><td>2</td><td>4</td><td>6</td><td>1</td><td>0.340</td></tr><tr><td>Q</td><td>1/2</td><td>1</td><td>2</td><td>4</td><td>1/2</td><td>0.180</td></tr><tr><td>COST</td><td>1/4</td><td>1/2</td><td>1</td><td>2</td><td>1/4</td><td>0.090</td></tr><tr><td>SUP</td><td>1/6</td><td>1/4</td><td>1/2</td><td>1</td><td>1/6</td><td>0.051</td></tr><tr><td>INT</td><td>1</td><td>2</td><td>4</td><td>6</td><td>1</td><td>0.340</td></tr><tr><td colspan="7">Technological level 3 (on-line system)</td></tr><tr><td>D</td><td>1</td><td>3</td><td>6</td><td>6</td><td>1</td><td>0.365</td></tr><tr><td>Q</td><td>1/3</td><td>1</td><td>4</td><td>4</td><td>1/3</td><td>0.163</td></tr><tr><td>COST</td><td>1/6</td><td>1/4</td><td>1</td><td>1</td><td>1/6</td><td>0.053</td></tr><tr><td>SUP</td><td>1/6</td><td>1/4</td><td>1</td><td>1</td><td>1/6</td><td>0.053</td></tr><tr><td>INT</td><td>1</td><td>3</td><td>6</td><td>6</td><td>1</td><td>0.365</td></tr></table>

When a PMP is applied based on the integration of lubricant and vibration analyses, the pairwise matrix and eigenvectors obtained from the criteria corresponding to the different technological levels are in Table 5.

The diagnostic techniques to be applied are dependent on the type of machinery, and therefore the results shown have been achieved by applying the MSDT-PMP to screw compressors.

## 5. Case study of a screw compressor with the integration of lubricant and vibration analyses

A PMP was designed and set up in a petrochemical plant. The program was applied to three screw compressors.

The industrial equipment submitted to the analysis was adapted for the incorporation of an integrated PMP of vibration and lubricant analysis for the following reasons [7]:

 The equipment has high criticity; its breakdown supposes the temporary closedown of the whole plant of lubricant production.

 The equipment is rotary, and therefore, adapted for the application of a PMP based on vibration analysis.

 Most of the mechanical components of these compressors are bathed by the same lubricant, therefore this can gather information about the condition of all of them.

The compressors are placed in a petrochemical plant and within the area of influence of the plants there are two thermal plants. This factor suggests the possibility of the influence of environmental pollution, generating phenomena of grazing and corrosion.

 It is possible to trace the development of deterioration in the machinery from its initial stage, by means of lubricant analysis, up to the stage at which the mechanical damage can be demonstrated, by means of vibration analysis.

The acquisition of data used in the analysis is rather complicated due to the specificity of this kind of data in the industrial plant, the high cost of acquisition and the restricted access to the data. Nevertheless, two full years of monthly acquisition of data were developed.

The model selects a minimum of two alternatives between which integration can take place. The capacity of integration between lubricant and vibration techniques and between diagnostic techniques belonging to vibration analysis or lubricant analysis in isolation has been maintained.

The diagnostic techniques analyzed are in Table 6.

The results of applying FA to diagnostic parameters in a screw compressor when integration between lubricant and vibration analyses is applied is described.

Diagnostic techniques analyzed

<table><tr><td>Diagnostic techniques</td><td>Code</td></tr><tr><td colspan="2">Lubricant analysis</td></tr><tr><td>Water content in lubricant</td><td>WACONT</td></tr><tr><td>Colour of lubricant</td><td>COLOUR</td></tr><tr><td>Density</td><td>DENSITY</td></tr><tr><td>Content in wear metals (iron)</td><td>WEAR1</td></tr><tr><td>Viscosity index</td><td>VISCINDEX</td></tr><tr><td>Content in wear metals (lead)</td><td>WEAR2</td></tr><tr><td>Content in contamination metals (silicon)</td><td>SI</td></tr><tr><td>Total acid number</td><td>TAN</td></tr><tr><td>Viscosity to 100 °C</td><td>VISC (100)</td></tr><tr><td>Viscosity to 40 °C</td><td>VISC (40)</td></tr><tr><td colspan="2">Vibration analysis</td></tr><tr><td>Tendency of global vibration value of RMS (10–1000 Hz)</td><td>TEN1</td></tr><tr><td>Spectral analysis/density of spectral power</td><td>ES</td></tr><tr><td>Waterfalls</td><td>WA</td></tr><tr><td>Spike energy</td><td>SP</td></tr><tr><td>Harmonic tendencies/peak values</td><td>TEN2</td></tr><tr><td>Time signal analysis/form and crest factors</td><td>TEM</td></tr><tr><td>Statistical analysis (kurtosis, variance analysis)</td><td>KV</td></tr><tr><td>Bode diagram</td><td>BO</td></tr><tr><td>Polar diagram</td><td>PO</td></tr><tr><td>Orbital analysis</td><td>OR</td></tr><tr><td>Finite modal element/experimental modal analysis</td><td>FEM</td></tr><tr><td>Cepstrum/envelope</td><td>CE + EN</td></tr></table>

Table 7  
Correlation matrix between lubricant and vibration parameters in a screw compressor

<table><tr><td></td><td>WACONT</td><td>COLOUR</td><td>DENSITY</td><td>WEAR1</td><td>VISCINDEX</td><td>TEN1</td><td>WEAR2</td><td>SI</td><td>TAN</td><td>VISC (100)</td><td>VISC (40)</td></tr><tr><td>WACONT</td><td>1.00000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>COLOUR</td><td>0.55024</td><td>1.00000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DENSITY</td><td>0.36161</td><td>0.97058</td><td>1.00000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>WEAR1</td><td>0.16166</td><td>0.51704</td><td>0.63661</td><td>1.00000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>VISCINDEX</td><td>0.87632</td><td>0.28724</td><td>0.04897</td><td>-0.33333</td><td>1.00000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TEN1</td><td>0.85443</td><td>0.27343</td><td>0.03393</td><td>-0.37314</td><td>0.99889</td><td>1.00000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>WEAR2</td><td>-0.53558</td><td>0.17235</td><td>0.24485</td><td>-0.33333</td><td>-0.33333</td><td>-0.29639</td><td>1.00000</td><td></td><td></td><td></td><td></td></tr><tr><td>SI</td><td>0.38984</td><td>0.98306</td><td>0.98786</td><td>0.51011</td><td>0.13912</td><td>0.12986</td><td>0.32462</td><td>1.00000</td><td></td><td></td><td></td></tr><tr><td>TAN</td><td>-0.67486</td><td>0.05620</td><td>0.29491</td><td>0.60150</td><td>-0.93486</td><td>-0.94334</td><td>0.31162</td><td>0.19257</td><td>1.00000</td><td></td><td></td></tr><tr><td>VISC (100)</td><td>0.40582</td><td>0.98133</td><td>0.99873</td><td>0.62014</td><td>0.09914</td><td>0.08393</td><td>0.22356</td><td>0.99067</td><td>0.24712</td><td>1.00000</td><td></td></tr><tr><td>VISC (40)</td><td>0.18922</td><td>0.89371</td><td>0.97500</td><td>0.73849</td><td>-0.16644</td><td>-0.18363</td><td>0.26017</td><td>0.93635</td><td>0.49708</td><td>0.96320</td><td>1.00000</td></tr></table>

The correlation matrix between the quantitative diagnostic techniques analyzed is shown in Table 7.

The determinant of the correlation matrix is low. Consequently, there are high intercorrelations between the variables. This characteristic is necessary in order to apply factor analysis.

Due to the quantity of factors available being too high, a factor analysis has been applied, to obtain a set of variables that form a coherent, independent group. Three factors get 100% of the accumulated percentage of variance, as can be appreciated in Table 8. As a result, only the factors with eigenvalue superior to 1 are preserved (Kaiser rule).

The rotation through varimax simplifies the results (Table 9) and facilitates interpretation of the data. As can be appreciated in Table 9, each variable is only saturated in one factor and each factor has distinct load distribution. Thus factor 1 is called contamination due to the fact that it has the highest contribution in variables such as silicon, content colour, density, etc, which are indicative of a contamination process in the compressor. Factor 2 is called degradation due to its having the highest contribution of the variables total acid number or water content which are indicative of a degradation process in the lubricant with a lack of additives. Factor 3 is called wear because it brings together the two variables that analyzed the wear process in the compressor such as the lead and iron content.

The diagnostic techniques that provide more information about the contamination, degradation and wear process (results of factor analysis) in the compressor are selected as alternatives. These alternatives are introduced in the hierarchy of Fig. 2 joint with the alternatives that give qualitative information. So, the alternatives considered by technological level are in

Table 8  
Integration of diagnostic parameters in factors

<table><tr><td>Factor</td><td>Eigenvalue</td><td>Percentage of variance</td><td>Accumulated percentage of variance</td></tr><tr><td>1</td><td>5.57269</td><td>50.7</td><td>50.7</td></tr><tr><td>2</td><td>4.02062</td><td>36.6</td><td>87.2</td></tr><tr><td>3</td><td>1.40669</td><td>12.8</td><td>100.0</td></tr><tr><td>4</td><td>0.00000</td><td>0.0</td><td>100.0</td></tr><tr><td>5</td><td>0.00000</td><td>0.0</td><td>100.0</td></tr><tr><td>6</td><td>0.00000</td><td>0.0</td><td>100.0</td></tr><tr><td>7</td><td>0.00000</td><td>0.0</td><td>100.0</td></tr><tr><td>8</td><td>0.00000</td><td>0.0</td><td>100.0</td></tr><tr><td>9</td><td>0.00000</td><td>0.0</td><td>100.0</td></tr><tr><td>10</td><td>0.00000</td><td>0.0</td><td>100.0</td></tr><tr><td>11</td><td>0.00000</td><td>0.0</td><td>100.0</td></tr></table>

Table 9  
Results provided before applying a rotation through varimax

<table><tr><td rowspan="2"></td><td colspan="3">Factors</td></tr><tr><td>Contamination</td><td>Degradation</td><td>Wear</td></tr><tr><td>WATCONT</td><td>0.37138</td><td>0.83074</td><td>0.41466</td></tr><tr><td>COLOUR</td><td>0.97404</td><td>0.22638</td><td>0.00107</td></tr><tr><td>DENSITY</td><td>0.99987</td><td>-0.01477</td><td>0.00615</td></tr><tr><td>WEAR1</td><td>0.62651</td><td>-0.41484</td><td>0.65985</td></tr><tr><td>VISCINDEX</td><td>0.06332</td><td>0.99613</td><td>0.06097</td></tr><tr><td>TEN1</td><td>0.04859</td><td>0.99869</td><td>0.01623</td></tr><tr><td>WEAR2</td><td>0.24623</td><td>-0.29375</td><td>-0.92363</td></tr><tr><td>SI</td><td>0.98992</td><td>0.08373</td><td>-0.11419</td></tr><tr><td>TAN</td><td>0.28052</td><td>-0.95891</td><td>0.04237</td></tr><tr><td>VISC (100)</td><td>0.99929</td><td>0.03521</td><td>0.01315</td></tr><tr><td>VISC (40)</td><td>0.97139</td><td>-0.23196</td><td>0.05105</td></tr></table>

Table 10  
Diagnostic techniques in each technological level in a PMP based on integrating vibration and lubricant analysis

<table><tr><td colspan="4">Portable system</td><td>On-line system</td></tr><tr><td>Level 0</td><td>Level 1</td><td>Level 2</td><td>Level 3</td><td>Level 3</td></tr><tr><td rowspan="2">Content in wear and contamination metals</td><td rowspan="2">Content in wear and contamination metals</td><td>Content in wear and contamination metals</td><td>Content in wear and contamination metals</td><td>Content in wear and contamination metals</td></tr><tr><td>Spectral analysis</td><td>Spectral analysis/density of spectral power</td><td>Spectral analysis/density of spectral power</td></tr><tr><td>Vibration analysis</td><td>Tendency of global vibration value RMS (10–1000 Hz)</td><td>Viscosity to 40 °C</td><td>Viscosity to 40 and 100 °C</td><td>Viscosity to 40 and 100 °C</td></tr><tr><td rowspan="3">Colour of lubricant</td><td rowspan="3">Viscosity to 40 °C</td><td>Waterfalls</td><td>Waterfalls</td><td>Waterfalls</td></tr><tr><td>Tendency of global vibration value RMS (10–1000 Hz)</td><td>Tendency of global vibration value RMS (10–1000 Hz)</td><td>Tendency of global vibration value RMS (10–1000 Hz)</td></tr><tr><td>Spike energy</td><td>Spike energy</td><td>Spike energy</td></tr><tr><td rowspan="3">Water content</td><td rowspan="3">Water content</td><td>Harmonic tendencies/peak values</td><td>Cepstrum/envelope</td><td>Cepstrum/envelope</td></tr><tr><td>Water content</td><td>Water content/total acid number</td><td>Water content/total acid number</td></tr><tr><td>Time signal analysis/form and crest factors</td><td>Time signal analysis/form and crest factors</td><td>Polar diagram</td></tr></table>

Table 10. Each of these alternatives has associated a particular instrumentation in agreement with their technological level.

## Next, the AHP is applied.

The maximum number of alternatives permitted in AHP is nine, and therefore, this is the number of alternatives or diagnostic techniques considered in the technological levels 2 and 3 of the model. Although there are other diagnostic techniques, the more representatives have been included.

The diagnostic techniques have been adapted to each technological level. Thus, water content is included in level 0 by means of visual inspection and in level 2 by means of a Karl Fischer device. Therefore, the results include the instrumentation needed to apply each of the diagnostic techniques in each technological level.

## 6. Results

In this section, the results of the model after applying factor analysis to the data obtained in screw compressors of a petrochemical plant, and by integrating qualitative and quantitative variables from lubricant and vibration analyses are presented. As can be appreciated in Table 11, the consistency ratio has values which are inferior to 0.1 in all the cases, and therefore, is considered acceptable.

## 6.1. Portable system

## 6.1.1. Technological level 0 (Table 11)

The diagnostic techniques analyzed provide information about the degradation in colour, water content in the inspection of free water, contamination by particles and preferably wear and anomalous mechanical behaviour. The complementary nature of each technique is demonstrated by the close preferences. The existence of similar values recommends the application of all the parameters to the industrial plant, and this is beneficial when a total productive maintenance is combined with a PMP.

The model selects visual inspection of particles in lubricant and visual inspection of vibration (or use of screwdriver), favouring the integration process of lubricant and vibration analyses.

## 6.1.2. Technological level 1

Table 11 shows that the global preferences of alternatives are very close, and therefore the use of all the techniques applying the concept of complementarity is recommended, unless the plant is interested in a limited number of techniques, in which case viscosity and tendencies of global vibration value RMS between 10 and 1000 Hz can be applied. The use of the stain of oil technique can be considered as a support technique.

Table 11  
Hierarchy of the diagnostic techniques in technological levels 0, 1, 2 and 3

<table><tr><td colspan="3">Selection of diagnostic techniques in a PMP based on integrated lubricant and vibration analyses</td></tr><tr><td>Diagnostic technique</td><td>Instrumentation</td><td>Preferences</td></tr><tr><td>Technological level 0</td><td></td><td></td></tr><tr><td>Content in wear and contamination metals</td><td>Visual inspection of particles in lubricant (no instrumentation)</td><td>0.275</td></tr><tr><td>Vibration analysis</td><td>Visual inspection/use of screwdriver</td><td>0.275</td></tr><tr><td>Colour of lubricant</td><td>Visual inspection (No instrumentation)</td><td>0.225</td></tr><tr><td>Water content</td><td>Visual inspection (No instrumentation)</td><td>0.225</td></tr><tr><td>Consistency ratio = 0.00</td><td></td><td></td></tr><tr><td>Technological level 1</td><td></td><td></td></tr><tr><td>Viscosity to 40 °C</td><td>Capillary viscometer</td><td>0.305</td></tr><tr><td>Tendency of global vibration value RMS (10–1000 Hz)</td><td>Vibrometer</td><td>0.262</td></tr><tr><td>Content in wear and contamination metals</td><td>Stain of oil</td><td>0.229</td></tr><tr><td>Water content</td><td>Crackle test</td><td>0.204</td></tr><tr><td>Consistency ratio = 0.00</td><td></td><td></td></tr><tr><td>Technological level 2</td><td></td><td></td></tr><tr><td>Spectral analysis</td><td>Spectral analyzer</td><td>0.200</td></tr><tr><td>Waterfalls</td><td>Spectral analyzer</td><td>0.180</td></tr><tr><td>Content in wear and contamination metals</td><td>Particle meter</td><td>0.172</td></tr><tr><td>Viscosity to 40 °C</td><td>Capillary viscometer</td><td>0.120</td></tr><tr><td>Tendency of global vibration value rms (10–1000 Hz)</td><td>Vibrometer/spectral analyzer</td><td>0.087</td></tr><tr><td>Spike energy</td><td>IRD spectral analyzer</td><td>0.077</td></tr><tr><td>Harmonic tendencies/peak values</td><td>Spectral analyzer</td><td>0.068</td></tr><tr><td>Water content</td><td>Karl Fischer</td><td>0.053</td></tr><tr><td>Time signal analysis/form and crest factors</td><td>Spectral analyzer/ oscilloscope</td><td>0.044</td></tr><tr><td>Consistency ratio = 0.04</td><td></td><td></td></tr><tr><td>Technological level 3</td><td></td><td></td></tr><tr><td>Content in wear and contamination metals</td><td>Spectrometer of atomic absorption</td><td>0.224</td></tr><tr><td>Spectral analysis/density of spectral power</td><td>Spectral analyzer</td><td>0.150</td></tr><tr><td>Viscosity to 40 and 100 °C</td><td>Automatic viscometer</td><td>0.135</td></tr><tr><td>Waterfalls</td><td>Spectral analyzer</td><td>0.118</td></tr><tr><td>Water content/total acid number</td><td>Karl Discher/tritrador</td><td>0.109</td></tr><tr><td>Cepstrum/envelope</td><td>Advanced oscilloscope</td><td>0.080</td></tr></table>

Table 11 (continued)

<table><tr><td colspan="3">Selection of diagnostic techniques in a PMP based on integrated lubricant and vibration analyses</td></tr><tr><td>Diagnostic technique</td><td>Instrumentation</td><td>Preferences</td></tr><tr><td>Spike energy</td><td>IRD spectral analyzer</td><td>0.071</td></tr><tr><td>Tendency of global vibration value RMS (10–1000 Hz)</td><td>Vibrometer/spectral analyzer</td><td>0.060</td></tr><tr><td>Time signal analysis/form and crest factors</td><td>Spectral analyzer/ oscilloscope</td><td>0.052</td></tr><tr><td>Consistency ratio = 0.00</td><td></td><td></td></tr></table>

## 6.1.3. Technological level 2

The model supplies (see Table 11) diagnostic techniques with quality of diagnosis and capacity for integration with other techniques. The model suggested the application of spectral analysis and waterfalls, particle counting and viscosity control. Therefore, the instrumentation required is: spectral analyzer, particle meter and capillary viscometer. The other alternatives have preferences inferior to the aforementioned. It should be pointed out that the tendency of global vibration value of RMS between 10 and 1000 Hz owes its classification to the lower setup and maintenance cost, but considering that the industrial plant has a high technological level, the cost variable should not influence the selection of alternatives.

## 6.1.4. Technological level 3

The classification of alternatives shown in Table 11 suggests the application of more technological techniques to provide better quality in the diagnosis and a superior capacity for the protection of machinery, because they detect the failures and the deterioration of elements and lubricants in early phases of development. The use of spectrografy, a technique that defines the factors that are contributing to wear and contamination, together with spectral analysis that detects wear effects are the techniques that supply the most reliable and fast diagnoses. These diagnostic techniques also provide information about

Hierarchy of the diagnostic techniques in technological level 3 in a PMP based on continuous integrated lubricant and vibration analyses

<table><tr><td colspan="3">Selection of diagnostic techniques in a PMP based on integrated lubricant and vibration analyses</td></tr><tr><td>Diagnostic technique</td><td>Instrumentation</td><td>Preferences</td></tr><tr><td>Content in wear and contamination metals</td><td>Spectrometer of atomic absorption</td><td>0.222</td></tr><tr><td>Spectral analysis/density of spectral power</td><td>Spectral analyzer</td><td>0.141</td></tr><tr><td>Viscosity to 40 and 100 °C</td><td>Automatic viscometer</td><td>0.131</td></tr><tr><td>Waterfalls</td><td>Spectral analyzer</td><td>0.121</td></tr><tr><td>Water content/total acid number</td><td>Karl Fischer/tritrador</td><td>0.107</td></tr><tr><td>Polar diagram</td><td>Continuous acquisition system/displacement sensors/key phasor</td><td>0.079</td></tr><tr><td>Cepstrum/envelope</td><td>Advanced oscilloscope</td><td>0.079</td></tr><tr><td>Spike energy</td><td>IRD spectral analyzer</td><td>0.065</td></tr><tr><td>Tendency of global vibration value RMS (10–1000 Hz)</td><td>Vibrometer/spectral analyzer</td><td>0.055</td></tr><tr><td>Consistency ratio = 0.02</td><td></td><td></td></tr></table>

the most suitable moment in which to carry out the change of lubricant due to contamination or loss of protection capacity. These techniques can be complemented with viscosity and waterfalls, as the model suggests.

The model minimizes the repetitive information in the process of selection of diagnostic techniques.

## 6.2. On-line system

## 6.2.1. Technological level 3

The procedure used is similar to that in technological level 3 in a portable system, although it rejects the alternatives with the lower preferences obtained in the level 3 of a PMP based on vibration analysis. This means the analysis can be limited to nine alternatives. As can be seen in Table 12, the classification is very similar to that obtained in a portable system, although the technology applied is superior in this case, because it provides a more exact control of the state of machinery. The quantity of techniques applied in the plant depends on economic variables and the criticality of industrial machinery, which is generally very elevated in this technological level. Therefore, the use of the following instrumentation is suggested: spectrometer of atomic absorption, spectral analyzer and automatic viscometer. This allows the application of diagnostic techniques: content in wear and contamination metals, spectral analysis and density of spectral power, viscosity to 40 and 100 <sup>j</sup>C and waterfalls. The greater weight given to the polar diagram rather than the cepstrum/envelope is due to the capacity of the first to provide information about the behaviour of axis, an aspect that cannot be analyzed with any other alternatives.

![](/api/attachments/RFXN54YJ/fulltext/images/b44362c67eb22de2172059e1f33bf88a848614b5e9e8c685fa7e70945206bf2e.jpg)  
Fig. 3. Sensitivity analysis corresponding to technological level 3 in on-line system.

The sensitive analysis corresponding to the setup of a PMP based on integrating lubricant and vibration analyses provides stable results in all the technological levels. Fig. 3 shows an example of the sensitivity analysis corresponding to technological level 3 in an on-line system.

## 7. Conclusions

In the decision support model designed, technological and organizational issues have been incorporated that until now had not been sufficiently researched in the topic of a predictive maintenance program.

Vibration analysis and lubricant analysis are the most frequently applied predictive techniques at present, as a result of which the integration of both techniques in a single predictive maintenance program can provide significant benefits for the company.

A model of selection of diagnostic techniques and instrumentation in a predictive maintenance program (MSDT-PMP) has been developed. Factor analysis and AHP have been combined. The model is applied to different technological levels in PMPs based on integrated lubricant and vibration in screw compressors placed in a petrochemical plant.

The results obtained will facilitate the decision making of the planner of the predictive maintenance program, as well as favour the development of the integration of predictive techniques, an aspect that currently lacks models for making decisions, due to the technical and organizational difficulties that its application represents, aspects in which this article aims to contribute.

## References

[1] G. Barbara, S. Tabachnick, S. Linda, Using Multivariate Statistic, HarperColling Publishing, New York, 1983.

[2] F. Barbera, H. Schneider, E. Watson, A condition based main-

tenance model for two-unit series system, European Journal of Operational Research 116 (1999) 281– 290.

[3] P. Beltra´n, A. Lo´pez, El Mantenimiento Predictivo en aerogeneradores. Caso pra´ctico: estudio de averı´as, Proceedings 4<sup>j</sup>- Congreso Espan˜ol de Mantenimiento, AEM, Barcelona, 2000.

[4] J.E. Berry, Good Vibes About Oil Analysis, Practicing Oil Analysis, J. Fitch, Tulsa, 1999 (November – December).

[5] B.K.N. Rao, Handbook of Condition monitoring, Elsevier, Oxford, 1996.

[6] L. Borao, M. Garcı´a, Mantenimiento Predictivo. Implantacio´n Industrial. Implantacio´n de un programa predictivo, Mantenimiento, no. 97, 1996 (Septiembre) 13–17.

[7] M.C. Carnero, Evaluacio´n del ciclo de vida de un Programa de Mantenimiento Predictivo mediante te´cnicas multicriterio, Thesis, University of Castilla-La Mancha, ETSII, Ciudad Real, 2001.

[8] M.C. Carnero, E. La Torre, M.A. Alca´zar, J. Conde, Control of wear applied to compressor: trends in lubricant analysis, International Journal on the Science and Technology of Friction Lubrication and Wear 225 – 229 (1999) 905 – 912.

[9] A.H. Christer, W. Wang, J.M. Sharp, A state space condition monitoring model for furnace erosion prediction and replacement, European Journal of Operational Research 101 (1997) 1 – 14.

[10] Computational Systems Inc., PC-based integration of spectrographic, Ferrographic and Vibration analysis data, P/PM Technology, 1991 (January – February).

[11] M. Cuesta, F.J. Herrero, Introduccio´ n al Ana´lisis Factorial, Tutorial:DPAM#95.2, Oviedo University, 2002.

[12] D.J. Edwards, G.D. Holt, F.C. Harris, Predictive maintenance techniques and their relevance to construction plant, Journal of Quality in Maintenance Engineering 4 (1) (1998) 25– 37.

[13] J.C. Fitch, Proactive and Predictic Strategies for Setting Alarms and Limits of Oil Analysis, Noria, Tulsa, 1998.

[14] E. Forman, M.A. Selly, Decisio´n by Objetives, (World Scientific, London, 2001).

[15] A.K.S. Jardine, V. Makis, D. Banjevic, D. Braticevic, M. Ennis, A decision optimization model for condition-based maintenance, Journal of Quality in Maintenance Engineering 4 (2) (1998) 115–121.

[16] A.K.S. Jardine, T. Joseph, D. Banjevic, Optimizing conditionbased maintenance decisions for equipment subject to vibration monitoring, Journal of Quality in Maintenance Engineering 5 (3) (1999) 192 – 202.

[17] B. Johnson, Oil Analysis Success at A Power Generation Station, Practicing Oil Analysis, J. Fitch, Tulsa, 1998 (July – August).

[18] V. Kakkar, Ontario power generation’s nanticoke power plant vol. 20, no. 4, Orbit, Bently, NV, 1999.

[19] G.M. Knapp, R. Javadpour, H. Wang, An ARTMAP neural networkbased machine condition monitoring system, Journal of Quality in Maintenance Engineering 6 (2) (2000) 86 – 105.

[20] T. Lund-Hansen, Innovate condition monitoring methodologies for improved plant economics, Proceedings del Sixteenth Annual Meeting and Seminar of Canadian Machinery Vibration Association (CMVA), Toronto, Canada´, 1997 (November).

[21] M. Lupinucci, J.G. Pe´rez Davila, L. Tiseyra, Improving sheet

metal quality and producto throughput with bently’s machinery management system vol. 21, no. 3, Orbit, Bently, NV, 2000.

[22] K. Mobley, Why predictive programs fail, Plant Services, 1997 (October).

[23] K. Mobley, Predictive maintenance equipment, The 1998 CMMS, PM/PdM Handbook, Putman publishing, Itasca, IL, 1998.

[24] Nasa, Appendix H. Predictive Testing and Inspection, Working paper, Nasa handbook, Octubre, 1994.

[25] B. Johnson, Oil analysis success at a Power Generation Station, Practicing Oil Analysis, J. Fitch, Tulsa, 1998 (July – August).

[26] Preditec, Curso de Introduccio´n al Ana´lisis Predictivo de Lubricantes, Zaragoza, Julio, 1997.

[27] C.E. Reese, C.H. Lochmu¨ller, Introduction to Factor Analysis, Duke University, Durham, 1994.

[28] T.L. Saaty, The Analytic Hierarchy Process, McGraw Hill, New York, 1980.

[29] H. Saranga, Relevant condition-parameter strategy for an effective condition-based maintenance, Journal of Quality in Maintenance Engineering 8 (1) (2002) 92 – 105.

[30] D.J. Sherwin, B. Al-Najjar, Practical models for condition monitoring inspection intervals, Journal of Quality in Maintenance Engineering 5 (3) (1999) 203 – 220.

[31] H.A. Taha, Investigacio´n de operaciones, Una introduccio´n, Pearson, Me´xico, 1998.

[32] E. Triantaphyllou, S.H. Mann, Using the analytic hierarchy process for decision making In engineering applications: some challenges, International Journal of Industrial Engineering: Applications and Practice 2 (1) (1995) 35 – 44.

[33] E. Triantaphyllou, F.A. Lootsma, P.M. Pardalos, S.H. Mann, On the evaluation and application of different scales for quantifying pairwise comparisons in Fuzzy Sets, Journal of Multi-Criteria Decision Analysis 3 (3) (1994) 133 – 155.

[34] E. Triantaphyllou, B. Kovalerchuck, L.J.R. Mann, J. Knapp, Determining the most important criteria in maintenance decision making, Journal of Quality in Maintenance Engineering 3 (1) (1997) 16 – 28.

[35] D.D. Troyer, Let’s Integrate Oil Analysis and Vibration Analysis, Practicing Oil Analysis, J. Fitch, Tulsa, 1998 (July – August).

[36] A.H.C. Tsang, Strategic dimensions of maintenance management, Journal of Quality in Maintenance Engineering 8 (1) (2002) 7– 39.

[37] A. Valverde, Ana´lisis de la disponibilidad de los equipos dina´micos y su incidencia en el mantenimiento en plantas industriales, Thesis, UNED, 1994.

[38] J.M. Villar, L.O. Masson, J.A. Gomes, Proactive maintenance—a successful history vol. 21 no. 3, Orbit, Bently, NV, 2000.

[39] Wearcheck. http://www.wearcheck.com/info/about\_interpretation.asp, (2003).

[40] J.W. Weyerhaeuser, Bearing Failures Dry Up at Weyerhaeuser, Practicing Oil Analysis, J. Fitch, Tulsa, 2000 (March – April).

Ma. C. Carnero Moya received her PhD from the University of Castilla-La Mancha. Her research interests are in decision support systems, multiple criteria decision making, evaluation system of maintenance policies and in the theories and applications of condition based maintenance. She has published in different journals including International Journal of Lubrication and Wear and Quality Progress. She is a professor in the Technical School of Industrial Engineering (University of Castilla-La Mancha), and has participated in some project about Condition Based Maintenance, supported by the European Union and Regional Administration.
