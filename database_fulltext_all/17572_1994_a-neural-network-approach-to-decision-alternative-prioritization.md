---
otero_id: 17572
otero_key: "HAXMZKF4"
title: "A neural network approach to decision alternative prioritization"
authors: "Rick L. Wilson"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90017-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A neural network approach to decision alternative prioritization

Rick L. Wilson

Oklahoma State University, Stillwater, OK, USA

A common decision problem faced by managers in organizations is that of decision alternative prioritization. There have been many proposed approaches to the problem where the decision maker constructs a pairwise comparison matrix of the alternatives under study. All existing ranking methods possess major shortcomings for the general problem. This paper illustrates the usefulness of a neural network model in such prioritization problems, which considers these shortcomings of previous methods. Use of the model is shown through the use of example ranking scenarios.

Keywords: Neural networks; Ranking; Prioritization; Decision making

![](/api/attachments/HAXMZKF4/fulltext/images/c8b045508bf8abee2e1e272f91a1229ea826709e33091b7333ff750cffd9507c.jpg)

Rick L. Wilson is currently an Assistant Professor of Management Science and Information Systems at Oklahoma State University. He received his Ph.D. in MIS from the University of Nebraska-Lincoln. Dr. Wilson has previously published in Decision Support Systems, as well as Information and Management, International Journal of Production Research, and a number of other refereed journals. His current research interests include neural networks, decision support systems and integrated management science applications.

## 1. Introduction

Many decisions faced by managers in business organizations deal with prioritization of competing decision alternatives. For instance, a manager considering the purchase of a spreadsheet software package has a number of different alternatives to choose from; somehow, he/she must determine which package is 'best'. Similarly, a personnel manager considering hiring from a pool of interviewees must prioritize these prospective employees prior to initiating job offers. There are many other examples of decision problems requiring the prioritization of decision alternatives.

Much prior research has been devoted to the topic of prioritizing alternatives $[1,2,6,9,10,14,15]$ ; unfortunately, little consensus has been reached for a general non-compensatory model of prioritization. Generally, these procedures have ranked alternatives (goals, projects, etc.) using the concept of a strength vector, inspired from social choice theory. This vector considers the overall strength of each individual object relative to others, and is typically derived from a pairwise comparison matrix enumerating all possible comparisons of objects. The main emphasis of these procedures has been to minimize the number of objects ranked ahead of other objects where dominance was not indicated, referred to as a minimum violations ranking (MVR).

These existing models of prioritization suffer from various shortcomings. First, ties often result in the ranking or prioritization process $[1,14]$ . In a managerial decision making situation, this can pose a practical problem to the decision maker. Therefore, it is desirable that a ranking procedure not result in ties. Second, while existing approaches incorporate information regarding relative dominance of one object or goal over another, they do not allow the expression of the degree or amplitude of such dominance. Third, the methods do not take into consideration all information available in the pairwise comparison matrices, such as the relative strength of dominated objects or alternatives. Finally, not all methods adequately deal with pairwise comparison matrices which are sparse (i.e., when all possible comparisons of goals are not enumerated in the decision process).

Neural Networks have been shown effective in classification or categorization business decision problems such as bankruptcy prediction $[17]$ , corporate bond rating prediction $[13]$ , and many others. Additionally, other neural network models have been proposed for classical optimization problems such as the traveling salesman problem with varying degrees of success $[7,8]$ .

The main emphasis of this paper is to present a new neural network model and algorithm useful for the general decision alternative prioritization problem. This model is developed in attempt to address the shortcomings of existing ranking methods. Furthermore, the neural network approach is easy to use and understand, easily implemented and results in meaningful prioritization of decision alternatives. The paper will focus on the benefits to the prioritization decision problem that it can provide, illustrating this through realistic, small examples. Discussion of model use and future research endeavors will also be presented.

## 2. Ranking / prioritizing goals

## 2.1. Introduction

The problem of ranking n objects (management goals, decision alternatives, teams, individuals, etc.) is a common decision situation. Such situations can include the establishment of a priority list for information system projects, the prioritization of goals or criteria in a mathematical programming model, personnel selection, ranking of sports teams, determining consumer preferences in product comparisons, examining alternative hydroelectric power projects, weighting components in measurements of productivity $[11]$ , R & D project selection $[4]$ , and so forth.

The objective in such situations is to determine the appropriate rank ordering of the objects (from best to worst) based on a comparison of the objects. The decision maker compares an object with other objects, identifying the relative superiority or inferiority of the compared objects. The process is then repeated for all objects. Typically, this determination of preference is represented in a binary (0-1) pairwise comparison matrix. Additionally, it may be appropriate to extract from the decision maker the degree or amplitude of inferiority or superiority; this data should also be considered when ranking the n objects.

The use of pairwise comparisons to collect data from the decision maker offers distinct advantages $[5]$ . It allows the decision maker to focus on the comparison of just two objects, making the observation as free as possible from extraneous influences. Additionally, pairwise comparisons generate meaningful information about the decision problem regarding consistency of choice (as compared to simultaneous comparisons) in the decision making process $[5,9]$ .

## 2.2. Past approaches to prioritization

There have been many previous non-compensatory approaches to the ranking problem. Often times, these past approaches have utilized the setting of round-robin sports tournaments to illustrate their procedures. Thus, the terminology of these past approaches will be intermixed throughout this paper along with more general, business application oriented vernacular.

One simple way is to rank an object on the basis of the ratio of the number of other objects they dominate to the total number of objects they were compared against (in sports terminology, this is equivalent to ranking an object/team on the basis of their won-loss record). Another simple approach is to rank the objects only on the basis of the total number of other objects they are judged to dominate, referred to as Kendall's score method [10]. Again, using sports terminology, this is equivalent to ranking on the basis of number of victories.

While these methods are easily understood and simple to use, they suffer from significant problems, such as ties in the rankings. While there are some instances where ties in the rank ordering may be permissible, the decision maker in this form of decision problem is looking for a distinct prioritization of objects or goals. A procedure that results in ties is, therefore, typically undesirable unless the objects which are ranked equally are exact replicas of each other (a highly unlikely occurrence).

In addition to the likely occurrence of ties, the results of these methods when a full enumeration of all possible comparisons of objects or goals is not available are meaningless. If time or other factors do not permit a total enumeration of comparisons among the goals or objects, those involved in the most comparisons will be inherently biased in the rankings. Situations where a full enumeration of all pairwise comparisons is not feasible or possible include problems where n is too large (as there are $1/2 * n * (n - 1)$ comparisons required), when the objects being compared are not all available simultaneously for comparisons (e.g., interviewing job applicants over a three day period), or, in a sports situation, when the teams do not all compete against each other.

Finally, and most significantly, these methods do not take into account the quality of the other objects involved in the comparisons. For instance, if object A dominates both object B and C, the relative strengths of B and C are not considered when evaluating the relative strength of object A.

Wei [15] and Kendall [10] discussed a method which considers the strength of some of the compared objects when determining the rank ordering of the entire set. Their process considered the strength of objects dominated by the object being examined in deriving the rank ordering. For instance, consider the case of five goals (A, B, C, D and E), where A is judged superior (more important) to B and D but inferior (less important) to C and E. In determining the relative importance of goal A, Wei and Kendall's method would consider the relative importance of goals B and D but not goals C and E. As pointed out by David [5], this method properly gives more credit to an object for dominating objects with higher relative strengths or importance. In the continuing example, if goal B had higher relative importance than goal D, then goal A should receive more credit for dominating the more important goal B than the less important goal D, as it does in the Wei and Kendall method.

However, as also pointed out in [5], this method penalizes an object less when it is judged inferior to an object with lesser relative importance than to an object with higher relative importance. This occurs in the method because it does not consider the relative importance or strength of objects which dominate the object being evaluated in the ranking process. Again returning to the aforementioned example, assume goal C has a higher relative importance than goal E. Goal A, being judged inferior to both, should be penalized more for being less important than goal E than for being less important than goal C. This desired treatment does not occur in Wei and Kendall's method.

Additionally, this method also suffers from ties, as illustrated in $[1,6,9]$ . It is also not applicable in prioritization situations when there are sparse comparison matrices, as objects which are involved with more comparisons will tend to be ranked higher regardless of performance.

Another general approach has been based upon a Minimum Violations Ranking criterion (MVR). Goddard [6] presents an approach to rank a set of objects on such a criterion. An MVR ranking attempts to minimize the number of objects ranked ahead of other objects in which dominance was not indicated in the pairwise comparisons. Goddard used a p-connectivity matrix to address the issues of ties in ranking and the consideration of the relative strength of objects involved in pairwise comparisons. Unfortunately, as pointed out in [14], Goddard's process (and the MVR criterion) suffers from both deficiencies that it was intended to avoid. Goddard's MVR neither determines a unique ranking nor does it properly utilize the relative strengths of other objects involved in the comparisons. In fact, Stob [14] showed how the MVR criterion can lead to treating dominance over a lesser object as more important than dominance over a stronger object, entirely opposite treatment of a comparison to that which Goddard (and logic) advocated.

Ali, et al. [1] expanded upon Kendall's use of ranking by the number of objects dominated [10] to address the issue of ranking ties. They referred to this method as the Iterated Kendall method (IK), and presented it as a heuristic in deriving the MVR rankings for a given prioritization problem. Basically, when ranking ties occurred, the method considered subsets of the comparison matrix which only included those tied objects. It then broke the ties by applying the Kendall score method to the subset. If ties could not be broken at this step, this subset of objects was then ranked by another heuristic approach [2]. While this method attempted to deal with ties in the rank ordering of objects, it still did not fully consider the relative strengths of the objects involved in the comparisons. Additionally, it used the MVR criterion as a basis for ranking which has the shortcomings previously identified.

## 2.3. Summary of previous approach shortcomings

All of the preceding non-compensatory methods for ranking objects suffer from one or more shortcomings. These shortcomings include the occurrence of ties in the final rankings as well as the inability of the methods to consider the strength of the objects or goals compared against. Further, existing methods are unable to properly deal with decision situations where a full enumeration of all possible comparisons are not available (sparse pairwise comparison matrix), as they tend to bias the results toward those objects with more comparisons. Additionally, few of the previous approaches allow for the expression of the degree of dominance of one alternative over another, an important omission $[3]$ .

## 2.4. Requirements for an effective prioritization process

An obvious requirement for any prioritization approach is that it result in “correct” prioritization or ranking of the objects under consideration. This is a nebulous task. One reason that there has been many previously proposed approaches to the decision problem, beside the shortcomings previously mentioned, is that the “best” ranking of a certain collection of objects is not always apparent. If, however, for a particular ranking situation, an a priori “appropriate” prioritization can be determined, then these situations can be used to validate solution approaches. Thus, given such a ranking situation, an effective prioritization approach must provide the “correct” results.

Consider the situation in Figure 1, a binary pairwise comparison matrix considering the relative importance of four hypothetical goals A, B, C, D. In this example, the decision maker has judged Goal A more important than both Goals B and C, Goal B more important than Goal C, Goal C more important than Goal D, and Goal D more important than both Goal A and B. It is of interest to note that these comparisons are not “consistent” in the sense that transitivity in the comparisons do not exist. For instance, Goal A is judged superior to Goal B, which, in turn, is judged superior to Goal C, which is judged superior to Goal D. However, Goal D is judged superior to Goal A, violating consistency in the comparisons. Such decision maker inconsistency is not unexpected in complex decision situations. A proper approach to the prioritization problem must provide the ability to still determine a rational rank ordering of decision alternatives even with the inconsistency.

<table><tr><td colspan="5">GOAL COMPARISONS</td></tr><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>A</td><td>x</td><td>1</td><td>1</td><td>0</td></tr><tr><td>B</td><td>0</td><td>x</td><td>1</td><td>0</td></tr><tr><td>C</td><td>0</td><td>0</td><td>x</td><td>1</td></tr><tr><td>D</td><td>1</td><td>1</td><td>0</td><td>x</td></tr></table>

NEURAL INTERCONNECTION WEIGHTS
FROM NEURON

<table><tr><td rowspan="2"></td><td rowspan="2">A</td><td> $\underline{\mathbf{A}}$ </td><td> $\underline{\mathbf{B}}$ </td><td> $\underline{\mathbf{C}}$ </td><td> $\underline{\mathbf{D}}$ </td></tr><tr><td> $\underline{\mathbf{x}}$ </td><td> $\underline{\mathbf{l}}$ </td><td> $\underline{\mathbf{l}}$ </td><td> $-\underline{\mathbf{l}}$ </td></tr><tr><td>TO</td><td>B</td><td> $-1$ </td><td> $\underline{\mathbf{x}}$ </td><td> $\underline{\mathbf{l}}$ </td><td> $-1$ </td></tr><tr><td rowspan="2">NEURON</td><td>C</td><td> $-1$ </td><td> $-1$ </td><td> $\underline{\mathbf{x}}$ </td><td> $\underline{\mathbf{l}}$ </td></tr><tr><td>D</td><td> $\underline{\mathbf{l}}$ </td><td> $\underline{\mathbf{l}}$ </td><td> $-1$ </td><td> $\underline{\mathbf{x}}$ </td></tr></table>

As well as addressing the shortcomings of existing approaches and provide sound prioritization, any approach must be easy to use, easy to understand, appreciated by even a naive decision maker considering the prioritization of decision alternatives. A neural network approach to the problem is presented next, designed to possess the essential characteristics for an effective prioritization process.

## 3. The neural network prioritization model

In general, neural network models are distinguishable on the basis of a number of characteristics. These include the behavior of their processing elements (neurons), the type of connections between neurons, the coefficients of these connections, the transfer function of the neurons, and the model learning laws and training or evolution algorithm. The neural network model for prioritization is presented forthwith within this framework.

## 3.1. Neurons

In this neural network model, each neuron will correspond to one decision alternative involved in the prioritization process. The neurons will be continuously valued. It is the discretion of the decision maker to determine reasonable ranges for the neuronic values (dependent on the nature of the problem). For instance, a reasonable neural value range might be from 0 to 1, or from 0 to 100, and so forth. Irrespective of the scale used, the value of the neuron associated with a particular decision alternative represents the relative importance of that alternative, as compared to other alternatives.

## 3.2. Connections and connection weights

For every pairwise comparison of objects undertaken by the decision maker (corresponding to two entries in the pairwise comparison matrix), two directed interneuronic connections are established in the neural model. For instance, again using Figure 1 as an example comparison matrix, consider the comparison of Goal A and Goal B. Goal A has been judged superior to Goal B (“1” entry in row A, column B; “0” entry in row B, column A). Thus, there will be a connection from neuron A to neuron B of weight -1, indicative of Goal B being inferior to Goal A. Similarly, there will be a connection from neuron B to neuron A of weight +1, indicative of Goal A being dominant to Goal B (from A’s perspective).

Therefore, for a prioritization problem with a full enumeration of comparisons, each neuron will be connected to all other neurons in two different directions. The coefficients (weights) of these connections will indicate whether dominance or inferiority was indicated in the comparison of objects (from one objects perspective) and, alternately, the amplitude or degree of dominance or inferiority. Thus, the interconnection weights are somewhat analogous to the pairwise comparison matrices extracted from the decision maker. Note that these weights will be fixed throughout the computation of prioritization; no adaptation (i.e., learning) will occur.

To summarize the correspondence of the neural network connections and weights to the pairwise comparison matrix (when amplitude of dominance or inferiority is not specified), a “0” entry (inferior comparison) translates to a directed neural interconnection weight of -1, while a “1” entry (dominating comparison) corresponds to a neural connection weight of +1. A table of interconnection weights of the neural model for the problem in Figure 1 is shown in the second half of the figure.

3.3. Remedying past approach shortcomings: The model transfer function

## 3.3.1. Overview of transfer function

The attractiveness of a neural network model for prioritization problems lies in its transfer and summation function. Each neuron's summation process will utilize a function which considers the incoming connection weights and the neuronic values of the corresponding connected neurons. On the basis of this, the process will generate a "value" associated with each specific comparison. This is done for all incoming connections. Implementing a transfer function which considers both the interconnection weights and the related connected neuronic values is indicative of explicitly considering the results of object comparisons and the relative importance of the compared against objects (the neuronic values). The importance of using this data in the prioritization process is well documented [1,5,6,9,14], quite desirable, and addresses a major shortcoming of previous approaches.

In determining the neuron's value (i.e., the object or decision alternatives present relative importance), the transfer function of the neuron will average all calculated comparison values. This averaging approach is in response to another documented shortcoming of prior approaches. Previous methods biased the prioritization results in favor of those objects involved in the most comparisons during the evaluation process. This averaging attribute of the transfer function will provide an accurate assessment of the neuronic value. After this averaging process, a small input bias will also be applied to the neuronic value. This will be done systematically to ensure that the sum of the neuronic values, irrespective of the value scale chosen, will remain the same throughout the evolution of the network. This bias will be further discussed in section 3.4.

## 3.3.2. Desired function characteristics

Given the overview above, the desired characteristics of the transfer function for prioritization will be discussed. These desired characteristics are based on ranking research previously summarized as well as having additional foundation in attribution theory from the management literature.

In the motivational theory literature, the use of an attributional model of motivation attempts to explain the perceived causes of the success or failure of an achievement related event by considering internal and external elements (e.g., see $[12,16]$ ). In the context of object prioritization, a success is synonymous to an object judged more important or to dominate another object. Likewise, a failure is analogous to an object judged inferior or less important than another object in a pairwise comparison.

The attribution of why an object succeeded or failed is key to the determination of the value associated with the pairwise comparison. Basically, there are two generic factors which success or failure can be attributed: internal or external. In the prioritization decision setting, internal attribution of success or failure of an object involved in a comparison would attribute its performance to the “true” relative importance of that object (internalization). External attribution would be attributing success or failure of an object to the relative importance of the object being compared against.

From the standpoint of an object under scrutiny, failure against a weak object would be strongly internalized, i.e., the failure of the object being considered would be attributed to its own weakness. However, there would be some nobility in failing against a stronger object; the attribution of failure would be externalized due to the relative high importance of the object compared against. Thus, the value of a comparison from an object's perspective increases as the attribution of failure to external factors increase.

Similarly, when an object succeeds in a comparison against a weak object, the success is attributed to external factors (weak relative importance of object). As the relative importance or strength of the comparison's target object increases, the attribution of success becomes more and more internal. Therefore, the value of a comparison to a particular object increases as the attribution of success to internal factors increases. It is also reasonable to expect that the rate of change of internalizing success exceeds the rate of change of externalizing failure as the strength of the object compared against increases. Thus, as the environment becomes more and more hostile (increasing importance of object being compared against), a success is perceived as an unexpected occurrence, and objects having such successes should have greater internal attribution relative to the increase in external attribution of failure in a similar comparison.

From the consideration of attribution theory and previous contributions of prioritization theory, one can make the following observations regarding assessing value to a particular comparison between objects and the desired behavior of a neural network transfer function:

Characteristic 1: Obviously, from an valuative standpoint, being judged dominant over a particular object should be more highly valued than being judged inferior to that same object.

Characteristic 2: If an object is judged superior over both object A and object B, and object A is considered “more important” in relative terms than object B, more relative “value” to the object under consideration should accrue from the comparison with object A than the comparison with object B.

Characteristic 3: Similarly, consider an object judged inferior to two objects; greater value to the object being evaluated should accrue from the comparison to the object possessing the “higher” relative importance.

Characteristic 4: The rate of increase in the value assessment of a comparison, as the relative importance of the compared object increases, should be greater in “dominating” comparisons (successes) than in “inferior” comparisons (failures). Characteristic 5: As a consequence of the first four characteristics, there will also exist trade-offs when contrasting the “value” of comparisons resulting from an indication of dominance over a relatively unimportant object versus a comparison indicating small inferiority to an extremely important object. That is, given such a situation, at what point does being inferior in a comparison hold more “value” (in the evaluating process)

than being superior? Only the decision maker within the problem context can truly assess this trade-off. Therefore, the transfer function must be flexible enough to handle different orientations of this decision trade-off point.

To further illustrate these five important characteristics, consider the case when, in a hypothetical prioritization process, one is trying to assess object A on the basis of a tangible measurement. In the following example, one wishes to prioritize a series of objects using pairwise comparisons on the basis of relative object weight. The decision maker determines that object A is heavier than objects B and D, but is lighter than objects C and E. Additionally, object B has a relative “weight” value larger than object D, while object C has a larger relative “weight” value than object E.

From object A's perspective, the comparison of objects A to B and objects A to D should generally contribute more value to the determination of the relative weight of A than the comparisons of objects A to C and E. This is due to the fact that A is judged to dominate B and D and inferior to C and E. Additionally, since object B has a larger relative weight than object D, one can further expect that the value of the comparison of objects A to B should contribute more value to the determination of the relative weight of object A than the comparison of objects A to D. (Likewise, there would be more value associated with A's comparison to C than with object E.)

However, it is also reasonable to expect that there are instances when the value accruing to an object from a particular comparison in which it is judged inferior may be greater than for a comparison in which an object dominates another. For instance, consider that the relative weight of object D is extremely small and the relative weight of object C extremely large. It would be possible, depending on the decision maker's explicit value assignment function, that the value associated with object A's comparison to object C would be greater than the value of the comparison to object D, even though object A was determined to be inferior to object D.

The previous discussion summarizes the important five characteristics surrounding the transfer function. Utilizing all information about the prioritization decision is a desired attribute of any ranking process, and represents the major shortcoming of past prioritization approaches. Using each comparison, associating a value to that comparison, and calculating the average comparison value as the relative importance value of a particular object better utilizes the decision information available.

alpha=0.2, gamma=40, beta=10
MAX=100  
![](/api/attachments/HAXMZKF4/fulltext/images/29a676977ce72e6ae62915ebb22f09e0ca5ec00ee33f2038affed4d460035691.jpg)  
Value of Object Compared Against (0-MAX)  
Fig. 2. Transfer function.

## 3.4. An example transfer function

There could be a variety of ways to model the prescribed five major characteristics of the neural transfer function. For this study, two linear equations were used. This approach was chosen because the linear approach satisfied the required characteristics and is easily implemented.

As Figure 2 depicts, the comparison valuation is calculated from different linear equations, depending on whether dominance or inferiority is expressed. The dichotomous linear equations addresses characteristic 1; the rate of change of both equations addresses characteristics 2 and 3; and the larger rate of change for the value function used in dominance comparisons (as contrasted with inferiority comparisons) covers characteristic 4. Visually apparent is the ability to model characteristic 5.

Formally, at time t in the network evolution, the value associated with a particular comparison from object i's perspective $(V_{ij}^{\prime})$ is a function of the incoming connection weight $(w_{ij})$ to neuron i from neuron j and the corresponding neuronic value $(V_{j}^{t-1}, \text{relative strength or importance of decision alternative } j \text{ at previous instant of time } t-1)$ . The connection weight indicates that either dominance or inferiority has been expressed in the comparison. (If binary comparisons, recall that “0” entries in the matrix correspond to -1 neural connection weights, while “1” entries correspond to +1 neural connection weights). The connections can also express amplitude of dominance or inferiority.

Considering the general case where $w_{ij}$ indicates both preference as well as additive intensity of preference in the comparison, the value of the comparison between object i and object j (viewed from object i's perspective) can be stated as:

$$
\begin{array}{r l} V _ {i j} ^ {t} = & \beta + T (w _ {i j}) * \gamma \\ & + (\alpha + T (w _ {i j}) * \Delta) * V _ {j} ^ {t - 1} + w _ {i j}, \end{array}
$$

where $T(x)$ : hard limiting function such that

$$
\begin{array}{l l} T (x) = 1 & \text {for} x > 0 \\ T (x) = 0 & \text {for} x <   0 \\ T (x) = 0. 5 & \text {for} x = 0 \end{array}
$$

$w_{ij}$ : interconnection weight incoming to neuron i from neuron j (> 0 = dominance, < 0 = inferiority)

$V_{j}^{t-1}$ : relative importance of object j (at previous instant of time)

α : slope of inferiority function

$\alpha + \Delta$ : slope of dominance function

$\beta$ : intercept value for inferiority function

$\beta + \gamma$ : intercept value for dominance function

Parameters $\beta$ , $\alpha$ , and $\gamma$ are user specified and indicative of different emphasis placed on the trade-off between judged dominance and inferiority as discussed in characteristic 5 above. The hard limiting function is necessary due to instances where the connection weight indicates both dominance or inferiority (by being either positive or negative) as well as amplitudinal information.

Using this function to determine the value of each comparison between decision alternatives, the new relative strength or importance of decision alternative i at time t is found by averaging $\Sigma V_{ij}^{t}$ (for all j) for those comparisons involving object i.

Rule-of-thumb guidelines for the specifications of the three variables $\beta$ , $\alpha$ , and $\gamma$ of the transfer function are derived in Appendix A. Essentially, the following equation represents concurrent limitations on these parameters which ensure the key five characteristics of the neural transfer function be met:

$$
\alpha + 2 \beta / \mathrm{MAX} + \gamma / \mathrm{MAX} <   1,
$$

where MAX is equal to the maximum neuron value possible as determined by the decision maker.

Specifically, as $\alpha$ increases, the slopes of the two functions increase, placing more emphasis on comparisons with objects of higher relative importance. As $\gamma$ increases, the gap is enlarged between the dominance and inferiority function. Thus, it places increased emphasis on being judged dominant over other objects in the determination of an object's importance. The value of $\beta$ is an intercept variable with minimal impact. If an amplitudinal pairwise matrix is being utilized, setting the value of $\beta$ equal to the larger possible matrix value would preclude any negative value assessment and would be a reasonable heuristic.

The $\Delta$ term is the magnitude which the slope of the dominance function exceeds the slope of the inferiority equation. In essence, the neural network model calculates the exact $\Delta$ value; it is a function of the other three model parameters and the degree of inconsistency in the decision problem. As $\alpha + 2\beta/\text{MAX} + \gamma/\text{MAX}$ becomes further away from 1, $\Delta$ increases. Thus, by choice of $\beta$ , $\alpha$ , and $\gamma$ the decision maker also has the implicit capability of identifying how the slope of the functions should differ.

The implementation of the neural network model presented in this paper uses an initial estimate for $\Delta$ based upon the three parameters. This initial estimate for consistent, fully enumerated matrices can be quite accurate. For this study, the value of $\Delta$ was estimated in the following manner. At the first calculated state of the neural network, $\Delta$ was initially set to 0, and the required input bias for network convergence (i.e., $\Sigma V_{i}^{t} = constant$ ) was calculated. For successive network states, this initial bias was used as an estimate for $\Delta$ .

However, inconsistent matrices require some adjustment to the $\Delta$ term. This is due, in part, to the network requirements for convergence to a solution. Using sports terminology, inconsistency in a comparison matrix is equivalent to the occurrence of “upsets”, where a stronger team (object) is defeated (inferior) by a weaker team (object) [14]. Thus, in comparison to a fully consistent environment, all other things being equal, the comparison values associated with the dominance function in an inconsistent environment will be higher since objects with higher relative importance are being judged inferior. One of the requirements for the network to converge is that $\Sigma V_{i}^{t}$ is constant throughout network evolution. If $\Delta$ is initially overstated, the neuronic values may violate this if not adjusted. Therefore, an input bias to each neuron systematically keeps $\Sigma V_{i}^{t}$ constant; i.e., by adjusting $\Delta$ .

The best procedure a decision maker can use in a prioritization problem is to utilize a number of different combinations of parameter values, assess their impact on the ranking outcome (if any), and then make the prioritization decision. The examples in Section 4 illustrate the relative robustness of the model to the parameter specification.

the neuron values represent the relative importance of each object under evaluation. Each step is further clarified in Figure 3.

The neural network model is constructed from the pairwise comparison matrix as discussed in Sections 3.1 and 3.2. It is assumed that user specified transfer function parameters meet the previous stated guidelines; otherwise, convergence to rational ranking may not occur. All initial neuron values should all be set equal to some predefined value. An integral part of the convergence algorithm is that the sum of the neuron's values should remain constant over each successive network time increment. Thus, this study proposes and uses an initial neural value set to MAX/2.

## 3.5. Evolution of the model to equilibrium

Figure 3 identifies the steps of the algorithm used by the neural network prioritization model to evolve to a final, static state. At this final state,

The collective computing capabilities are simulated by updating the network as time t is incrementally increased. New neuronic values are calculated by using the transfer function to determine $V_{i}^{t}$ . The new values are a function of the neuron values at previous time t - 1. Note that the neuron values are kept to a constant sum throughout the network evolution by means of an input bias (which, in essence, adjusts the estimated $\Delta$ parameter). The process of calculating $V_{i}^{t}$ for increasing t is repeated until the neuron values converge (i.e., $V_{i}^{t} = V_{i}^{t-1}$ , for all i).

For comparison matrices that are fully enumerated and can be represented as a divisible matrix (no inconsistency), it can be analytically shown that the network will converge to a proper solution (see Appendix B for a simple example) provided the user parameter specification guidelines are maintained. However, for general indivisible matrices and/or sparse matrices, it is difficult to analytically calculate or show convergence.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- Given:
- Pairwise Comparison Matrix
- User-specified Parameters
- Set Up Neural Network
- Neuron per object
- Connection weights from comparison matrix
- Initial Neuron values  $V^{0}_{i} = MAX/2$  (e.g.)
- Time = 0
- Repeat the calculation of neuron values ...
- Time = Time + 1
- Calculate using transfer function and input bias
-  $V^{t}_{i} = f(V^{t-1}_{i})$ 
- bias keeps  $\sum V^{t}_{i} = constant$ 
- Until  $V^{t}_{i} = V^{t-1}_{i}$  for all i
- Neuron Values represent object prioritization strengths
Fig. 3. Neural network convergence algorithm overview.
</div>

![](/api/attachments/HAXMZKF4/fulltext/images/be8e4e751e1f4cb06cba7ac30ac37aaa0be23c6f7ced90a0b8328f39094c5577.jpg)  
Fig. 4. Network convergence.

In this regard, though, the fact that the model forces $\Sigma V_{i}^{t}=$ constant for all t removes the possibility of the network converging to an all zero or infinity state. Additionally, matrix theory may offer some insight into proof of convergence [9]. An oversimplification (but nonetheless representative) of the neural model evolution is its similarity to taking repeated powers of a matrix where, at some power t, the result vectors of the matrix multiplication (neuron values) no longer change.

Figure 4 shows network convergence for the simple goal prioritization situation previously identified in Figure 1. Note that after 5 time units, the network has converged, with the goals prioritized as D, A, C and B.

## 3.6. Summary of neural network prioritization model

The general neural network model for decision alternative prioritization presented above extends the positive aspects of previous methods while is designed to overcome the stated shortcomings and be an effective prioritization process. It properly includes all relevant information in the decision problem. This new approach uses pairwise comparisons of objects and can be used even when the comparison matrices are sparse. It allows for the degree or amplitude of dominance in object comparisons to be included in the ranking analysis. The approach is not paralyzed by inevitable decision maker inconsistency in the pairwise comparisons of the objects.

The following section will illustrate the performance of the new model in three basic prioritization examples, comparing its performance against past proposed approaches where appropriate. These examples show how the new general neural network model offers promise in addressing the shortcomings of other ranking processes.

## 4. Example use of neural prioritization model

## 4.1. Example 1: No decision maker inconsistency

In this first example, the decision environment consists of seven decision alternatives, each of which has been compared to all other decision alternatives by the decision maker (i.e., all possible pairwise comparisons are enumerated). There is no inconsistency in this decision setting; alternative 1 is preferred to alternatives 2, 3, 4, 5, 6 and 7; alternative 2 is preferred to alternative 3, 4, 5, 6 and 7; and so forth. The comparison matrix is shown in Figure 5. Because there is no inconsistency and all possible pairwise comparisons known, an a priori “correct” ranking can be determined (alternative 1, followed by 2, 3, 4, 5, 6 and 7).

Table 1 shows the neuronic values which result when using the neural network model for prioritization. For this example, MAX = 100 and the neuron values can vary between 0 and 100, with the larger value representing the most important decision alternative (neuron). The results are consistent with the intuitive ranking of the objects. Note that as the transfer function parameters $\alpha$ , $\beta$ , and $\gamma$ are varied to place greater importance on dominance in the ranking process, the more pronounced the differences are in the relative strengths of the seven objects.

<table><tr><td></td><td> $\frac{\mathrm{o}1}{\mathrm{x}}$ </td><td> $\frac{\mathrm{o}2}{\mathrm{1}}$ </td><td> $\frac{\mathrm{o}3}{\mathrm{1}}$ </td><td> $\frac{\mathrm{o}4}{\mathrm{1}}$ </td><td> $\frac{\mathrm{o}5}{\mathrm{1}}$ </td><td> $\frac{\mathrm{o}6}{\mathrm{1}}$ </td><td> $\frac{\mathrm{o}7}{\mathrm{1}}$ </td></tr><tr><td> $\mathrm{o}1$ </td><td>x</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $\mathrm{o}2$ </td><td>0</td><td>x</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $\mathrm{o}3$ </td><td>0</td><td>0</td><td>x</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $\mathrm{o}4$ </td><td>0</td><td>0</td><td>0</td><td>x</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $\mathrm{o}5$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>x</td><td>1</td><td>1</td></tr><tr><td> $\mathrm{o}6$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>x</td><td>1</td></tr><tr><td> $\mathrm{o}7$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>x</td></tr></table>

Fig. 5. Consistent matrix.

Table 1  
Relative strength values-consistent matrix

<table><tr><td rowspan="3"></td><td colspan="3"> $(\beta = 15)$ </td></tr><tr><td> $\alpha = .4$ </td><td> $\alpha = .3$ </td><td> $\alpha = .2$ </td></tr><tr><td> $\gamma = 20$ </td><td> $\gamma = 30$ </td><td> $\gamma = 40$ </td></tr><tr><td>o1</td><td>64.91</td><td>70.28</td><td>75.89</td></tr><tr><td>o2</td><td>59.65</td><td>63.09</td><td>66.67</td></tr><tr><td>o3</td><td>54.57</td><td>56.17</td><td>57.82</td></tr><tr><td>o4</td><td>49.66</td><td>49.51</td><td>49.32</td></tr><tr><td>o5</td><td>44.92</td><td>43.09</td><td>41.16</td></tr><tr><td>o6</td><td>40.35</td><td>36.90</td><td>33.33</td></tr><tr><td>o7</td><td>35.94</td><td>30.95</td><td>25.81</td></tr><tr><td></td><td> $\alpha = .3$ </td><td> $\alpha = .2$ </td><td> $\alpha = .1$ </td></tr><tr><td></td><td> $\gamma = 20$ </td><td> $\gamma = 30$ </td><td> $\gamma = 40$ </td></tr><tr><td>o1</td><td>71.56</td><td>77.66</td><td>84.12</td></tr><tr><td>o2</td><td>63.47</td><td>67.19</td><td>71.07</td></tr><tr><td>o3</td><td>55.96</td><td>57.53</td><td>59.12</td></tr><tr><td>o4</td><td>49.00</td><td>48.62</td><td>48.16</td></tr><tr><td>o5</td><td>42.53</td><td>40.39</td><td>38.12</td></tr><tr><td>o6</td><td>36.52</td><td>32.81</td><td>28.92</td></tr><tr><td>o7</td><td>30.95</td><td>25.81</td><td>20.49</td></tr><tr><td rowspan="3"></td><td colspan="3"> $(\beta = 10)$ </td></tr><tr><td> $\alpha = .4$ </td><td> $\alpha = .3$ </td><td> $\alpha = .2$ </td></tr><tr><td> $\gamma = 20$ </td><td> $\gamma = 30$ </td><td> $\gamma = 40$ </td></tr><tr><td>o1</td><td>71.18</td><td>77.14</td><td>83.46</td></tr><tr><td>o2</td><td>63.25</td><td>66.94</td><td>70.70</td></tr><tr><td>o3</td><td>55.88</td><td>57.07</td><td>58.99</td></tr><tr><td>o4</td><td>49.03</td><td>48.67</td><td>48.23</td></tr><tr><td>o5</td><td>42.66</td><td>40.58</td><td>38.36</td></tr><tr><td>o6</td><td>36.75</td><td>33.10</td><td>29.29</td></tr><tr><td>o7</td><td>31.25</td><td>26.19</td><td>20.97</td></tr><tr><td></td><td> $\alpha = .3$ </td><td> $\alpha = .2$ </td><td> $\alpha = .1$ </td></tr><tr><td></td><td> $\gamma = 20$ </td><td> $\gamma = 30$ </td><td> $\gamma = 40$ </td></tr><tr><td>o1</td><td>78.91</td><td>85.84</td><td>93.37</td></tr><tr><td>o2</td><td>67.37</td><td>71.33</td><td>75.50</td></tr><tr><td>o3</td><td>57.10</td><td>58.54</td><td>59.96</td></tr><tr><td>o4</td><td>47.97</td><td>47.29</td><td>46.44</td></tr><tr><td>o5</td><td>39.84</td><td>37.38</td><td>34.69</td></tr><tr><td>o6</td><td>32.62</td><td>28.65</td><td>24.46</td></tr><tr><td>o7</td><td>26.19</td><td>20.97</td><td>15.57</td></tr></table>

A similar, supplemental example is illustrated in Figure 6. This prioritization environment also has no inconsistency in the comparison matrix, but is sparse. As above, an a priori correct ranking can be determined (alternative 1, followed by 2, 3, 4, 5, 6 and 7). Table 2 illustrates a small sampling of the neural network ranking. In this situation, a ranking approach based on percentage dominances would fail to correctly prioritize.

<table><tr><td></td><td> $\underline{o1}$ </td><td> $\underline{o2}$ </td><td> $\underline{o3}$ </td><td> $\underline{o4}$ </td><td> $\underline{o5}$ </td><td> $\underline{o6}$ </td><td> $\underline{o7}$ </td></tr><tr><td>o1</td><td> $\underline{x}$ </td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>o2</td><td>0</td><td> $\underline{x}$ </td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>o3</td><td></td><td>0</td><td> $\underline{x}$ </td><td>1</td><td></td><td></td><td></td></tr><tr><td>o4</td><td></td><td></td><td>0</td><td> $\underline{x}$ </td><td>1</td><td></td><td></td></tr><tr><td>o5</td><td></td><td></td><td></td><td>0</td><td> $\underline{x}$ </td><td>1</td><td></td></tr><tr><td>o6</td><td></td><td></td><td></td><td></td><td>0</td><td> $\underline{x}$ </td><td>1</td></tr><tr><td>o7</td><td></td><td></td><td></td><td></td><td></td><td>0</td><td> $\underline{x}$ </td></tr></table>

Fig. 6. Consistent sparse matrix.

Table 2  
Relative strength values-consistent sparse matrix

<table><tr><td rowspan="3"></td><td colspan="3"> $(\beta = 15)$ </td></tr><tr><td> $\alpha = .4$ </td><td> $\alpha = .3$ </td><td> $\alpha = .2$ </td></tr><tr><td> $\gamma = 20$ </td><td> $\gamma = 30$ </td><td> $\gamma = 40$ </td></tr><tr><td>o1</td><td>76.75</td><td>81.13</td><td>85.42</td></tr><tr><td>o2</td><td>54.90</td><td>54.24</td><td>53.16</td></tr><tr><td>o3</td><td>50.14</td><td>49.99</td><td>49.84</td></tr><tr><td>o4</td><td>48.82</td><td>49.09</td><td>49.35</td></tr><tr><td>o5</td><td>47.52</td><td>47.99</td><td>48.52</td></tr><tr><td>o6</td><td>43.96</td><td>44.01</td><td>44.46</td></tr><tr><td>o7</td><td>32.59</td><td>28.20</td><td>23.89</td></tr></table>

## 4.2. Example 2: Inconsistent decision environment

The data used in [14] to refute Goddards' [6] methodology will serve as the next example. In this prioritization situation, inconsistency exists in the object comparisons. The pairwise comparison matrix is shown in Figure 7. As in the first example, the pairwise comparison matrices are binary, as they indicate no additional amplitudinal information regarding dominance or inferiority.

The ranking results derived by the previously discussed methodologies in prioritizing these objects are as stated below:

Percentage Dominances/Comparisons and Kendall's Scores:

o1, o2-o3-o4-o5 tied, o6-o7 tied

MVR: o1, o3, o4, o5, o6, o7, o2 or o2, o1, o3, o4, o5, o6, o7

Kendall and Wei: o1, o2, o5, o3, o4, o7, o6
Iterated Kendall: o1, o2-o3 (\*), o4-o5

$(*)$ - ties broken arbitrarily  
Neural Network: o1, o2, o3, o5, o4, o7, o6

<table><tr><td></td><td> $\frac{01}{x}$ </td><td> $\frac{02}{0}$ </td><td> $\frac{03}{1}$ </td><td> $\frac{04}{1}$ </td><td> $\frac{05}{1}$ </td><td> $\frac{06}{1}$ </td><td> $\frac{07}{1}$ </td></tr><tr><td>o1</td><td>x</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>o2</td><td>1</td><td>x</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>o3</td><td>0</td><td>0</td><td>x</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>o4</td><td>0</td><td>0</td><td>0</td><td>x</td><td>1</td><td>1</td><td>1</td></tr><tr><td>o5</td><td>0</td><td>1</td><td>0</td><td>0</td><td>x</td><td>1</td><td>1</td></tr><tr><td>o6</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>x</td><td>1</td></tr><tr><td>o7</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>x</td></tr></table>

Fig. 7. Inconsistent matrix.

Table 3  
Relative strength values—inconsistent matrix

<table><tr><td rowspan="3"></td><td colspan="3"> $(\beta = 15)$ </td></tr><tr><td> $\alpha = .4$ </td><td> $\alpha = .3$ </td><td> $\alpha = .2$ </td></tr><tr><td> $\gamma = 20$ </td><td> $\gamma = 30$ </td><td> $\gamma = 40$ </td></tr><tr><td>o1</td><td>59.28</td><td>62.56</td><td>65.95</td></tr><tr><td>o2</td><td>50.42</td><td>50.58</td><td>50.76</td></tr><tr><td>o3</td><td>49.97</td><td>49.95</td><td>49.94</td></tr><tr><td>o5</td><td>49.84</td><td>49.78</td><td>49.71</td></tr><tr><td>o4</td><td>49.82</td><td>49.75</td><td>49.68</td></tr><tr><td>o7</td><td>45.41</td><td>43.79</td><td>42.11</td></tr><tr><td>o6</td><td>45.26</td><td>43.58</td><td>41.85</td></tr><tr><td></td><td> $\alpha = .3$ </td><td> $\alpha = .2$ </td><td> $\alpha = .1$ </td></tr><tr><td></td><td> $\gamma = 20$ </td><td> $\gamma = 30$ </td><td> $\gamma = 40$ </td></tr><tr><td>o1</td><td>62.39</td><td>65.73</td><td>69.17</td></tr><tr><td>o2</td><td>51.12</td><td>51.46</td><td>51.83</td></tr><tr><td>o3</td><td>49.87</td><td>49.83</td><td>49.78</td></tr><tr><td>o5</td><td>49.60</td><td>49.48</td><td>49.36</td></tr><tr><td>o4</td><td>49.50</td><td>49.35</td><td>49.19</td></tr><tr><td>o7</td><td>43.95</td><td>42.33</td><td>40.66</td></tr><tr><td>o6</td><td>43.56</td><td>41.82</td><td>40.02</td></tr><tr><td rowspan="3"></td><td colspan="3"> $(\beta = 10)$ </td></tr><tr><td> $\alpha = .4$ </td><td> $\alpha = .3$ </td><td> $\alpha = .2$ </td></tr><tr><td> $\gamma = 20$ </td><td> $\gamma = 30$ </td><td> $\gamma = 40$ </td></tr><tr><td>o1</td><td>62.20</td><td>65.49</td><td>68.87</td></tr><tr><td>o2</td><td>51.09</td><td>51.42</td><td>51.77</td></tr><tr><td>o3</td><td>49.87</td><td>49.83</td><td>49.79</td></tr><tr><td>o5</td><td>49.61</td><td>49.50</td><td>49.38</td></tr><tr><td>o4</td><td>49.52</td><td>49.37</td><td>49.21</td></tr><tr><td>o7</td><td>44.05</td><td>42.44</td><td>40.80</td></tr><tr><td>o6</td><td>43.66</td><td>41.95</td><td>40.18</td></tr><tr><td></td><td> $\alpha = .3$ </td><td> $\alpha = .2$ </td><td> $\alpha = .1$ </td></tr><tr><td></td><td> $\gamma = 20$ </td><td> $\gamma = 30$ </td><td> $\gamma = 40$ </td></tr><tr><td>o1</td><td>65.24</td><td>68.56</td><td>71.97</td></tr><tr><td>o2</td><td>52.05</td><td>52.55</td><td>53.10</td></tr><tr><td>o3</td><td>49.69</td><td>49.61</td><td>49.52</td></tr><tr><td>o5</td><td>49.33</td><td>49.16</td><td>48.99</td></tr><tr><td>o4</td><td>49.05</td><td>48.82</td><td>48.56</td></tr><tr><td>o7</td><td>42.67</td><td>41.09</td><td>39.46</td></tr><tr><td>o6</td><td>41.97</td><td>40.22</td><td>38.40</td></tr></table>

Table 3 indicates the values of the neurons in the neural network approach for this problem (MAX again equal to 100). Note the small difference between objects 5 and 4 in their relative strength values. This closeness is indicative of the trade-offs associated with the fact that o5 was judged inferior to o4, but was also judged to dominate o2, a stronger alternative that o4. The rank ordering listed above for the neural network approach was the same irrespective of transfer function parameter specification. A sampling of trial rankings are shown in Table 3.

In comparing the neural network approach to the other previous methods, the shortcomings of the other approaches become evident in this situation. Ties are prevalent, and some methods advocate their resolution by arbitrary means, which defeats the main purpose of a logical rank ordering scheme. The MVR approach provides two different minimum violation orderings; one has o2 as the most preferred object, the other ranking, the least preferred. Thus, as pointed out in [14], when there is the inevitable inconsistency in the prioritization problem, the MVR criterion is a poor one. While the Kendall and Wei method provides reasonable results, this is only an example where inevitable ties do not occur [1]. In this next example, the major shortcoming of the Kendall/Wei model, dealing with sparse comparison matrices, is highlighted.

## 4.3. Example 3: New hire screening

This section illustrates how the neural network ranking approach can be used in a more realistic and complex decision situation. The additional complexity typically found in prioritization decision problems (and this example) include sparse comparison matrices, unequal number of comparisons among the decision alternatives, and use of amplitudinal preference information.

Over the course of a three day period, a personnel manager in charge of hiring new sales people for a firm interviews 15 people for positions. Three are interviewed during day 1, seven during day 2, and the remaining five on day 3. At the end of each day, the personnel manager compares (in a pairwise manner) all people who had interviews, indicating on a -10 to 10 scale which interviewee was better (this scale based upon some underlying assessment criteria). Additionally, on day 2 and again on day 3, the manager compared some of the interviewees of the previous day to those of the present day for points of reference between the three sets of people interviewed.

It is anticipated that at least two people, but potentially more, will be hired. Because the environment is highly competitive, many other firms might also be interviewing (and offering jobs to) these same people. Jobs offered to the applicants might be turned down; thus, a rank ordering from best to worst applicant is necessary to fill the position. Thus, to address these two points in the analysis, the personnel manager needs to prioritize all fifteen people in rank order and have some manner of assessing the relative “strength” of each applicant.

Relative strength - job applicants

<table><tr><td rowspan="2"></td><td colspan="4"> $(\beta = 10)$ </td></tr><tr><td> $\alpha = .4$  $\gamma = 20$ </td><td> $\alpha = .3$  $\gamma = 30$ </td><td> $\alpha = .2$  $\gamma = 40$ </td><td>Kendall/Wei</td></tr><tr><td>a2</td><td>87.03</td><td>87.88 (1)</td><td>89.03 (1)</td><td>3-tie</td></tr><tr><td>a3</td><td>85.87</td><td>86.72 (2)</td><td>87.88 (2)</td><td>3-tie</td></tr><tr><td>a1</td><td>83.17</td><td>83.96 (3)</td><td>85.04 (3)</td><td>3-tie</td></tr><tr><td>a9</td><td>63.12</td><td>68.75 (4)</td><td>74.55 (4)</td><td>1st</td></tr><tr><td>a8</td><td>57.44</td><td>59.33 (5)</td><td>61.26 (5)</td><td>2nd</td></tr><tr><td>a11</td><td>51.16</td><td>53.43 (6)</td><td>55.62 (6)</td><td>11th</td></tr><tr><td>a10</td><td>49.39</td><td>51.20 (7)</td><td>53.10 (7)</td><td>8th</td></tr><tr><td>a4</td><td>44.05</td><td>41.58 (9)</td><td>39.02 (10)</td><td>6th</td></tr><tr><td>a7</td><td>42.93</td><td>41.72 (8)</td><td>40.49 (8)</td><td>7th</td></tr><tr><td>a6</td><td>42.73</td><td>41.29 (10)</td><td>39.80 (9)</td><td>10th</td></tr><tr><td>a5</td><td>40.12</td><td>36.37 (12)</td><td>32.48 (13)</td><td>9th</td></tr><tr><td>a15</td><td>37.47</td><td>36.46 (11)</td><td>35.29 (11)</td><td>12th</td></tr><tr><td>a13</td><td>37.37</td><td>36.22 (13)</td><td>34.91 (12)</td><td>14th</td></tr><tr><td>a12</td><td>30.91</td><td>28.20 (14)</td><td>25.31 (14)</td><td>15th</td></tr><tr><td>a14</td><td>30.07</td><td>27.51 (15)</td><td>24.76 (15)</td><td>13th</td></tr></table>

Figure 8 shows the pairwise comparison matrix for this personnel screening situation. For varying levels of the transfer function parameters, Table 4 illustrates the relative strength values for the fifteen applicants, and their rank order. As with the first two examples, MAX = 100, and the neuron values can take on the range between 0 and 100. Also listed is the prioritization results from the Kendall/Wei method. Other approaches fail in attempting to prioritize the applicants. The

Iterated Kendall method, because of the sparse comparison matrix, could not determine a unique ranking without extreme arbitrary rank assessments. Additionally, it has been shown that the MVR criteria is a poor one (and the IK method provides a MVR ranking). The percentage approach does not consider strength of compared against decision alternatives, and its ranking shortcomings have previously been documented.

The results in Table 4 illustrate the shortcomings of the Kendall/Wei approach to rank ordering. Note the inflated ranking of applicants 5 through 9, especially as compared with the neural network prioritization. Applicant 9 is ranked highest by Kendall/Wei since she/he is involved with a high number of comparisons and dominates them all. Unfortunately, those comparisons are mainly against other weak applicants. Applicants 2, 1 and 3, ranked highest by the neural network model, are all tied for third place in the Kendall/Wei approach. This is a good example of the undesirable occurrence of ties which can occur in ranking by Kendall/Wei.

To justify the prioritizations derived by the neural network model, consider how applicants 1, 2, 3 and 9 fared when compared against applicants 4 and 5. In almost every comparison, applicants 1, 2 and 3 were judged exceedingly more dominant than applicant 9. Thus, it is reasonable to expect applicants 2, 1 and 3 as the three highest ranked people, with applicant 9 significantly lower in relative strength in position 4. The fact that each of applicants 2, 3 and 1 were judged inferior to one other applicant should not inhibit them from being considered the top three candidates. This phenomenon is explained by considering that all three applicants similarly meet the desired criteria for the positions. Decision maker inconsistency in evaluating applicants 1, 2 and 3 against each other is not surprising if the choices are relatively indistinguishable.

<table><tr><td></td><td>a1</td><td>a2</td><td>a3</td><td>a4</td><td>a5</td><td>a6</td><td>a7</td><td>a8</td><td>a9</td><td>a10</td><td>a11</td><td>a12</td><td>a13</td><td>a14</td><td>a15</td></tr><tr><td>a1</td><td>x</td><td>-5</td><td>1</td><td>4</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>a2</td><td>5</td><td>x</td><td>-1</td><td>9</td><td>9</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>a3</td><td>-1</td><td>1</td><td>x</td><td>8</td><td>6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>a4</td><td>-4</td><td>-9</td><td>-8</td><td>x</td><td>-1</td><td>2</td><td>3</td><td>-1</td><td>-2</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>a5</td><td>-3</td><td>-9</td><td>-6</td><td>1</td><td>x</td><td>-1</td><td>6</td><td>-2</td><td>-4</td><td>-2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>a6</td><td></td><td></td><td></td><td>-2</td><td>1</td><td>x</td><td>-2</td><td>-3</td><td>-2</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>a7</td><td></td><td></td><td></td><td>-3</td><td>-6</td><td>2</td><td>x</td><td>1</td><td>-3</td><td>-2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>a8</td><td></td><td></td><td></td><td>1</td><td>2</td><td>3</td><td>-1</td><td>x</td><td>-2</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>a9</td><td></td><td></td><td></td><td>2</td><td>4</td><td>2</td><td>3</td><td>2</td><td>x</td><td>1</td><td>6</td><td>8</td><td>7</td><td>9</td><td>9</td></tr><tr><td>a10</td><td></td><td></td><td></td><td>-1</td><td>2</td><td>-1</td><td>2</td><td>-1</td><td>-1</td><td>x</td><td>4</td><td>3</td><td>6</td><td>8</td><td>8</td></tr><tr><td>a11</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-6</td><td>-4</td><td>x</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>a12</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-8</td><td>-3</td><td>-1</td><td>x</td><td>-1</td><td>2</td><td>-6</td></tr><tr><td>a13</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-7</td><td>-6</td><td>-2</td><td>1</td><td>x</td><td>5</td><td>-2</td></tr><tr><td>a14</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-9</td><td>-8</td><td>-3</td><td>-2</td><td>-5</td><td>x</td><td>1</td></tr><tr><td>a15</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-9</td><td>-8</td><td>-4</td><td>6</td><td>2</td><td>-1</td><td>x</td></tr></table>

Fig. 8. Job application example.

Also from Table 4, as the parameter specifications for the transfer function reduces the impact of the inferiority function, applicant 9 receives a higher relative strength assessment. Thus, the neural network model is moderately affected as the parameter specifications put more emphasis on dominance. However, since the neural model explicitly considers strengths of the applicant compared against, the actual ranking order of the first seven candidates remains robust. The lesser applicants may change their relative order as a result of the changes to the dominance and inferiority functions. Decision makers utilizing this neural network approach to prioritization will choose parameters to reflect their own judgment, and should perform a “sensitivity analysis” with the parameter values.

## 5. Discussion

## 5.1. Advantages of the neural network model

The examples presented in the previous section certainly do not constitute an all encompassing evaluation of the proposed neural network model for prioritization. Nonetheless, the overall results of the new ranking procedure are promising. When a priori ranking results were known, the model ranked objects correctly; when such results were not known, the neural model provided rational prioritizations. More importantly, the shortcomings of existing approaches were exposed, and the neural model did not suffer from such problems. The rest of this section reviews the potential advantages possessed by the new neural network algorithm.

The neural network approach utilizes pairwise comparisons of decision alternatives, the advantages of which are pointed out in [5]. While the other methods discussed in this study have used pairwise comparisons, the neural network approach utilizes all the available information in the comparison matrix where other methods did not. This new approach explicitly considers the relative strength or importance of the object involved in every comparison when determining the relative strength of another object.

Realistic decision situations may not have available the entire enumeration of all possible comparisons of competing decision alternatives. The neural network approach has been shown to rank order objects well irrespective of the sparsity of the comparison matrix. Other existing methods are biased toward those objects involved in the most comparisons.

This neural network approach also allows a simple expression of the degree of dominance of inferiority among objects. But, the neural network also performs well in situations where the comparison matrix does not include amplitudinal information. Thus, the neural network model may be a more general purpose approach to prioritization.

Decision maker inconsistency, inevitable in a real-world problem, is dealt with properly in the neural network approach. By considering information about both dominating comparisons and comparisons of inferiority, the neural network approach is not subject to over-penalizing or over-rewarding seemingly anomalous, inconsistent comparisons. In some decision making environments, however, inconsistency is not troublesome (for instance, ranking sports teams, since “upsets”, lesser teams defeating better teams, occur occasionally).

One of the drawbacks of previous methods was the occurrence of ties in the rankings of decision alternatives. This was discussed and shown in the preceding examples. There exists no empirical evidence that ties will not occur with the neural network prioritization approach. However, no ties occurred in the example problems, indicating initial evidence that the neural network model may have a lesser propensity for indeterminate rankings than other approaches.

The new prioritization approach has shown to provide relatively meaningful and potentially “more correct” or “more logical” prioritizations than previous methods. Other methods suffer from ties, questionable criteria (e.g., minimum violations) or biased results. The underlying concepts of the neural network algorithm are theoretically based and intuitively agreeable; the results shown above are favorable in supporting that the approach provides consistent rankings.

## 5.2. Model implementation and future research

The linear transfer function with three variable parameters used in this study was chosen only as an example. The three variable parameters allow flexibility for the decision maker in modeling the problem; this has been seen throughout the three examples in the previous section. Thus, the decision maker's own views can be specified on the trade-offs between dominance and inferiority as a function of the relative strength of objects involved in comparisons.

This flexibility is also a drawback. Behavior of ranking as a function of the parameters are exhibited in the previous examples, but at present, no inclusive, prescriptive guide of parameter impact can be provided. Future research will need to examine in more detail the implications of parameter values. However, an examination of the effect of different parameter specifications (a parameter sensitivity analysis) gives the decision maker additional information about the ranking problem in terms of prioritization robustness. From the examples seen in this paper, there does appear to be a high degree of robustness in the neural network ranking results.

The $\Delta$ parameter is not specified by the decision maker, but is somewhat representative of inconsistency in the comparison matrix. This inconsistency and the three parameters of the transfer function directly effect its value. Research continues on developing a more elegant manner in determining $\Delta$ directly from inconsistency measures of the comparison matrix, and for using $\Delta$ to convey inconsistency information to the decision maker.

The neural network prioritization approach in this study was implemented in a third generation language on a personal computer. Thus, the procedure is seemingly easily implementable and easy to use. The flexibility in the parameter specification and the ability to use any scale for the value of the neurons should also make the process easy to interpret as well as providing meaningful relative strength values to the decision maker.

## 6. Conclusion

The general prioritization problem, determining a proper rank ordering of decision alternatives on the basis of direct pairwise comparisons, is a common and much studied problem faced by managers in organizations. Past approaches have focused on minimizing violations (i.e., ranking an alternative below another alternative that it was judged to dominate). However, as shown in previous work and in this study, these approaches suffer serious shortcomings in practical use.

Neural network models, a brain metaphor of information processing, have been shown successful in a number of applications surrounding classification, forecasting and optimization problems. In this study, a new neural network model and convergence algorithm is presented to specifically address the prioritization of competing decision alternatives. This paper has shown that this new method builds on the strengths of existing ranking methods, is designed to remedy their shortcomings, is based upon sound ranking theories, and can be used and interpreted by a decision maker in a variety of situations.

This paper is still, however, an exploratory look at applying this innovative information approach to the ranking problem. A wide array of examples, more rigorous study of parameters for the linear transfer function, and examination of alternative transfer functions are all areas where future research is needed. The main emphasis of this paper was to show that the neural network approach offers promise in this area, and may indeed be superior to other methods. Future studies will determine the extent to which the promise of neural networks for prioritization is actually fulfilled.

## Acknowledgments

The authors would like to express gratitude to John Gleason, Krish Muralidhar and Kenneth Eastman for enlightening and lively discussions regarding aspects of this study. Additionally, the paper has greatly benefitted from the observations, suggestions and criticisms of two anonymous referees and editor Kar Yan Tam. We thank all for their assistance.

## References

[1] I. Ali, W. Cook, M. Kress, On the Minimum Violations Ranking of a Tournament, Management Science, 32, 1986, 660–672.

[2] W. Cook, I. Golan, M. Kress, Heuristics For Ranking Players In a Round Robin Tournament, Computers and Operations Research, Vol. 15, No. 2, 1988, 135–144.

[3] W. Cook and M. Kress, Ordinal Ranking With Intensity of Preference, Management Science, Vol. 31, No. 1, 1985, 26–32.

[4] W. Cook and L. Seiford, Priority Ranking and Consensus Formation, Management Science, Vol. 24, No. 16, 1976, 1721–1732.

[5] H. David, The Method of Paired Comparisons, Hafner Publishing, New York, 1963.

[6] S. Goddard, Ranking in Tournaments and Group Decision Making, Management Science, 29, 1983, 1384–1392.

[7] J. Hopfield and D. Tank, Neural Computation of Decisions in Optimization Problems, Biological Cybernetics, 52, 1985, 141–152.

[8] D. Ingman and Y. Merlis, Local Minimum Escape Using Thermodynamic Properties of Neural Networks, Neural Networks, Vol. 4, 1991, 395–404.

[9] M. Kendall, Further Contributions to the Theory of Paired Comparisons, Biometrics, Vol. 11, 1955, 43–62.

[10] M. Kendall. Rank Correlation Methods, 3rd Ed., Hafner Publishing, New York, 1962.

[11] K. Matta, A Goal-Oriented Productivity Index for Manufacturing Systems, International Journal of Operations and Production Management, Vol. 9, No. 4, 1989, 66–76.

[12] T. Mitchell, S. Green and R. Wood, An Attributional Model of Leadership and the Poor Performing Subordinate: Development and Validation, Research in Organizational Behavior, Vol. 3, 1981, 197–234.

[13] S. Shekhar and S. Dutta, Bond Rating: A Non-Conservative Application of Neural Networks, working paper, Computer Science Division, University of California, 1989.

[14] M. Stob, Rankings From Round-Robin Tournaments, Management Science, 31, 1985, 1191–1195.

[15] T.H. Wei, The Algebraic Foundations of Ranking Theory, unpublished thesis, Cambridge University, 1952.

[16] B. Weiner, et al., Perceiving the Causes of Success and Failure in Attribution: Perceiving The Causes of Behavior, E.E. Jones, et al. eds. Morristown NJ, Gen. Learn. Press, 1972.

[17] R. Wilson and R. Sharda, Bankruptcy Prediction Using Neural Networks, forthcoming in Decision Support Systems, 1992.

## Appendix A: Transfer function parameter guidelines

The key characteristic of the neural transfer function that limits the potential values that can be used is characteristic 4. This characteristic states that the slope of the dominance function should exceed the slope of the inferiority function. Therefore, determining at what point parameter specification violates this desired characteristic will identify parameter bounds. In essence, we will consider the parameter specifications that lead to the two functions having equal slope (i.e., $\Delta = 0$ ), and determine the appropriate inequality from this.

Consider a prioritization environment with n objects, no inconsistency and a full enumeration of pairwise comparisons of the objects. Also, let MAX equal the largest allowed neuron value. Recall that, because of the model requirements for convergence, at any time t in network evolution, $\Sigma V_{i}^{t} = n * MAX/2$ .

In an environment with n objects and a full complement of comparisons, there will be a total of $n * (n - 1)$ entries in the comparison matrix (and connections in the neural model). Ignoring the possibility of ties at this stage, $0.5 * n * (n - 1)$ of these entries will indicate dominance and $0.5 * n * (n - 1)$ will indicate inferiority. Therefore, if we separate the transfer function into distinct terms and considering the requirements for convergence stated above, sum over all object $i = 1 \ldots n$ at time t, we derive

$$
\begin{array}{r l} \sum_ {i = 1 \dots n} V _ {i} ^ {t} & = \sum_ {i = 1 \dots n} \left\{\left[ (n - 1) \beta + 0. 5 * (n - 1) \gamma \right. \right. \\ & \quad \left. + (n - 1) * \sum \alpha * V ^ {t - 1 j} \right] \Bigg \} \\ & / \{(n - 1) j = 1 \dots n, i \diamond j \}, \end{array}
$$

where the right hand side represents the calculation of each $V_{i}^{t}$ as the average of its $V_{ij}^{t}$ values and summing this for all n objects. This expression simplifies to

$$
\begin{array}{l} n \mathrm{MAX} / 2 = n \beta + 0. 5 n \gamma \\ \quad + \alpha * \sum_ {j = 1 \dots n} V _ {j} ^ {t - 1} \text { and   then   to } \end{array}
$$

$$
\begin{array}{r l} & n \mathrm{MAX} / 2 = n \beta + 0. 5 n \gamma \\ & \qquad + n \alpha * \mathrm{MAX} / 2 \text { and   finally }, \\ & 1 = 2 \beta / \mathrm{MAX} + \gamma / \mathrm{MAX} + \alpha . \end{array}
$$

This expression represents the parameter specifications where the slope of both functions are equivalent. Thus, when $\alpha + 2\beta/\text{MAX} + \gamma/\text{MAX} < 1$ , characteristic four of the transfer function is met.

## Appendix B: Convergence for simple case

Again, let us consider an prioritization environment where there is n objects, a full enumeration of pairwise comparisons and no inconsistency. Also, assume that objects are subscripted in terms of decreasing neural value (i.e., the most dominant object has i = 1, and the weakest object has i = n). One can analytically calculate through increasing neural time t how the neuron values will change.

By brute force examination of the expressions resulting from increasing t, the following expression represents the incremental difference in neural values that result between two objects i and $i + 1$ :

$$
- \gamma / (n - 1) + \alpha \gamma / (n - 1) ^ {2} - \alpha^ {2} \gamma / (n - 1) ^ {3}.
$$

Similarly, the final difference between two objects a “distance” of x from each other (i.e., o1 and o2 are a distance of 1, x = 2 - 1) is equivalent to:

$$
\left[ \begin{array}{c} - \gamma / (n - 1) + \alpha \gamma / (n - 1) ^ {2} - \alpha^ {2} \gamma / (n - 1) ^ {3} \\ * x. \end{array} \right]
$$

Since, for all t, $\sum V_{i}^{t}=n*MAX/2$ (which is a constant), then the fixed incremental difference calculated above illustrates that the model will converge. This brute force examination is intended only to be illustrative in nature. Work continues in formalizing the mathematics of convergence.
