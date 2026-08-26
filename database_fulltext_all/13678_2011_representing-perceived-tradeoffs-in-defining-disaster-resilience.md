---
otero_id: 13678
otero_key: "Q3Z2JASR"
title: "Representing perceived tradeoffs in defining disaster resilience"
authors: "Christopher W. Zobel"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.10.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Representing perceived tradeoffs in de<sup>fi</sup>ning disaster resilience

Christopher W. Zobel ⁎

Department of Business Information Technology, Virginia Polytechnic Institute and State University, Blacksburg, VA 24061-0235, United State

## a r t i c l e i n f o

Article history: Received 9 April 2010 Received in revised form 1 October 2010 Accepted 3 October 2010 Available online 30 October 2010

Keywords: Adjusted resilience Optimization Visualization Tradeoffs Decision support Preference modeling

## a b s t r a c t

Two of the primary measures that characterize the concept of disaster resilience are the initial impact of a disaster event and the subsequent time to recovery. This paper presents a new analytic approach to representing the relationship between these two characteristics by extending a multi-dimensional approach for predicting resilience into a technique for <sup>fi</sup>tting the resilience function to the preferences and priorities of a given decision maker. This allows for a more accurate representation of the perceived value of different resilience scenarios to that individual, and thus makes the concept more relevant in the context of strategic decision making.

Published by Elsevier B.V.

## 1. Introduction

As public awareness continues to grow of the long-term implications of disasters such as the 2010 Haiti Earthquake, the concept of disaster resilience is becoming more widely recognized as an important means of characterizing the ability of individuals, communities, and organizations to recover from the impacts of such events. Resilience is commonly de<sup>fi</sup>ned as “the act of rebounding or springing back” [12] from a disaster, and a resilient organization often is described as one which is able to quickly return to normal (or even improved) operations after such an event has occurred [14,15]. This ability to recover, however, can also be improved by efforts to mitigate against and prepare for the initial impact of a disaster, and therefore there also exists support for a broader de<sup>fi</sup>nition of resilience which incorporates both pre-event and post-event activities [10,17,19].

This broader de<sup>fi</sup>nition of resilience allows it to be used for strategic decision making, in the sense that it provides a means for assessing the relative risk of alternative scenarios. For example, whether planning a new hospital in an earthquake zone or expanding a supply chain into a politically unstable region, the extent to which alternative options support both initial resistance to and recovery from a possible disaster can have an impact on their long-term effectiveness. It thus can be important to be able to measure the relative amount of resilience associated with these factors for the different alternatives, in order to better inform the process of choosing between them. As a <sup>fi</sup>rst step towards measuring and comparing such resilience, Bruneau et al. [4] introduced the concept of the resilience triangle, which incorporates measures of both the robustness against initial loss due to a disaster and the rapidity of the recovery process. This initial concept was extended by Zobel [21], who de<sup>fi</sup>ned the related measure of predicted resilience and then presented a multi-dimensional approach for visually comparing resilience across different disaster scenarios.

In order to improve the utility of resilience as a comparative measure, the following discussion extends these previous efforts by introducing an approach for explicitly incorporating a decision maker's perceptions of the relative value of different resilience scenarios into a new, more representative, measure of adjusted resilience. Because different individuals may view the same resilience scenario from a variety of different perspectives, such a measure, which can be <sup>fi</sup>ne-tuned to accurately represent a speci<sup>fi</sup>c perspective, will be far more useful for a decision maker than would be a measure that represents a single <sup>fi</sup>xed interpretation of resilience. By <sup>fi</sup>tting the adjusted resilience function to the given decision maker's perspective over several different scenarios, one can help to make resilience much more consistent and meaningful for that individual and thus help to support more effective decision making.

The following discussion begins with an overview of previous work on resilience and on the resilience triangle in particular, including a look at the predicted resilience measure. It then motivates and derives a formulation for adjusted resilience and characterizes the bounds on its de<sup>fi</sup>ning parameters. After a brief discussion about capturing decision makers' preferences, an optimization model is presented for <sup>fi</sup>tting the adjusted resilience function to the stated preferences of a given decision maker, and an example is provided of its implementation. The paper concludes with a general discussion of the technique in the context of its ability to support more effective decision making in disaster operations management.

## 2. Background

## 2.1. Disaster resilience

Different aspects of the concept of resilience are currently being studied from a number of viewpoints within the academic research community [7,10,11,13,18]. In general, many such studies tend to focus on the resilience of either the physical (technological) aspects of a system [3,6] or the social (human) aspects of a system [7,9], but there is also signi<sup>fi</sup>cant discussion about studying combined human– environment interactions (socio-ecological systems) [8,19]. Given the importance of recognizing the larger context within which these factors exist [1], even the articles that focus on a speci<sup>fi</sup>c aspect of resilience will typically discuss the signi<sup>fi</sup>cance of other factors (such as legal or organizational issues) that can affect resilience overall. The resulting diversity of perspectives represented in these different approaches to the subject has led to a large number of different working de<sup>fi</sup>nitions that have been developed for the concept of disaster resilience [20].

Even with differences in opinion about the scope of the concept and about terminology, however, there is ongoing interest in developing quantitative techniques for measuring disaster resilience, in order to better support planning and decision making [8]. To be useful for this purpose, such techniques must either be focused speci<sup>fi</sup>cally on a particular aspect of resilience (such as physical resilience), or else they must be general enough to support application to both the physical and social aspects of resilience, as well as application to other important “environmental” aspects of the concept (such as economic resilience or political resilience). Because of its simplicity, the resilience triangle of Bruneau et al. [4], provides a strong basis for developing quantitative measures that can be applied to resilience in this more general context, as well as in a more focused fashion. It is due to this combination of simplicity and general applicability that the resilience triangle was chosen as the basis for the development of the adjusted resilience measure discussed in the later part.

## 2.2. Resilience triangle

Bruneau et al. [4], de<sup>fi</sup>ne disaster resilience as being characterized by the extent to which the following factors are present in either a physical or a social system:

(1) Robustness—the strength of a system, or its ability to resist the impact of a disaster event, in terms of the amount of damage or loss of functionality that results because of the event.

(2) Rapidity—the rate or speed at which a system is able to recover to an acceptable level of functionality, after the occurrence of a disaster event.

(3) Resourcefulness—the level of capability for dynamically responding to a disaster event, by identifying and implementing solutions to improve rapidity and/or robustness.

(4) Redundancy—the extent to which components of the system are substitutable, and therefore able to be replaced or augmented when functionality has been lost or reduced.

The last two factors, resourcefulness and redundancy, are generally considered to be the “means” by which disaster resilience can be improved, with the corresponding “ends” being measured by the impact of these improvements on the factors of robustness and rapidity [4].

In order to explicitly represent resilience as a combination of these <sup>fi</sup>rst two factors, Bruneau et al. [4] introduced the concept of the resilience triangle, as illustrated in Fig. 1. Based upon this concept, they then derived a simple quantitative measure for the loss of resilience in a system:

![](/api/attachments/Q3Z2JASR/fulltext/images/d9c6b3c482543a40bef2cea4323b675d291e6739c874c557b1365dbbcf1d704f.jpg)  
Fig. 1. The original resilience triangle (adapted from [4]).

$$
R = \int_ {t _ {0}} ^ {t _ {1}} [ 1 0 0 - Q (t) ] d t\tag{1}
$$

where Q(t) represents the quality of the system's infrastructure at a given time t. The vertical axis in Fig. 1 effectively represents the level of robustness of the given system, and the horizontal axis represents the associated rapidity of recovery [3].

By generalizing the concept of infrastructure beyond that of just a physical system, Bruneau et al. [4] also use Eq. (1) to discuss what they refer to as the technical, organizational, social, and economic dimensions of resilience. Thus, for example, robustness can be measured with respect to social, organizational, or economic “functionality,” as well as with respect to physical functionality. As de<sup>fi</sup>ned by Eq. (1), the resilience measure may have very different values within each of these dimensions, depending on the nature and impact of a given disaster. Chang and Shinozuka [5] extend this idea by establishing the notion of prede<sup>fi</sup>ned performance standards for both robustness and rapidity, against which actual system performance can be compared. They then de<sup>fi</sup>ne resilience as the probability that these standards will be met, in each of the technical, organizational, social, and economic dimensions.

Bruneau and Reinhorn [3] further demonstrate that redundancy can be visualized by using multiple simultaneous resilience triangles. They also offer a more precise quanti<sup>fi</sup>cation of the quality function, Q (t), in terms of both loss and performance standards, and they discuss some of the probabilistic aspects of assessing resilience. Cimellaro, Reinhorn, and Bruneau [6] provide a further extension to these ideas by explicitly de<sup>fi</sup>ning the area beneath the curve for Q(t) as a direct measure of resilience itself. This allows for a reduction in the size of a resilience triangle to be re<sup>fl</sup>ected as an increase in the corresponding resilience of the system that it represents.

## 2.3. Multi-dimensionality and non-linearity

Although there are advantages to using a single calculated value to de<sup>fi</sup>ne disaster resilience, it is also important to recognize the potential issues associated with doing so. In particular, if resilience is considered to be a function only of the area of the resilience triangle, then very different combinations of initial loss and recovery time can correspond to exactly the same resilience value. Thus, for example, a public building which suffers only slight damage in an earthquake, but which has a long recovery time due to scarcity of resources, may have exactly the same measured amount of resilience as a privately-owned building with signi<sup>fi</sup>cant initial damage but a much quicker recovery time (See Fig. 2). In reality, however, these two different scenarios may not be equivalent for a given decision maker, and he or she may actually prefer to be faced with one situation over the other (and might thus implicitly consider that situation to have greater resilience).

In order to better capture and represent such preferences, Zobel [21] introduced a multi-dimensional representation of resilience that incorporates both the resilience value and its two de<sup>fi</sup>ning characteristics of robustness and rapidity. This approach, which we will discuss in more detail in the later part, supports visually comparing different scenarios with respect to all three of these attributes at the same time, and it thus provides a more comprehensive means of assessing and differentiating between their relative levels of resilience. It is important to note, however, that Zobel's [21] approach does not provide a means for explicitly representing a particular decision maker's preferences between scenarios. Bruneau and Reinhorn [2] have suggested addressing this need by treating resilience as a nonlinear measure that could be calibrated to <sup>fi</sup>t different situational preferences. By doing so, one would allow the resilience measure to clearly and directly indicate the relative value of different situations to a particular decision maker, and thus help to capture the varying perceptions and interpretations of the actual disaster resilience inherent in a given system.

![](/api/attachments/Q3Z2JASR/fulltext/images/628e72ad320273586da63769c56b26dd511388f263f3f66a79405efad14a32a4.jpg)

![](/api/attachments/Q3Z2JASR/fulltext/images/9e1e190b7984aa3e823905582ef8064d95b7b2641b831a524c26eee06235bf07.jpg)  
Fig. 2. Two triangles representing the same resilience for different situations.

With this in mind, the primary focus of the discussion in the later part is to propose an approach for capturing the non-linearity of decision makers' preferences that also explicitly incorporates the multi-dimensional nature of resilience into its representation. We begin the discussion by de<sup>fi</sup>ning the notion of predicted resilience, as introduced in Zobel [21], and provide an overview of the multidimensional approach for visualizing the relative predicted resilience of different systems. We then develop a new dynamic formulation for resilience that allows us to <sup>fi</sup>t a resilience function to the preferences of a given decision maker, and we discuss an approach for optimizing the accuracy of this <sup>fi</sup>t.

## 3. Predicted disaster resilience

Zobel [21] de<sup>fi</sup>nes the predicted resilience for a given system to be a function of the predicted amount of initial loss and the associated recovery time for a future disaster event, where both values are estimated based on the information available before the event actually occurs. The initial loss value, X, is measured as a percentage of the total available functionality of the system (in the context of any of the four dimensions of resilience), and the recovery time, T, is measured in a relevant time unit, such as weeks or months. Although each of these measures could be represented probabilistically [3], the predicted resilience function assumes that they are deterministic estimates of the expected future behavior of the system [21]. With respect to the four factors used to characterize disaster resilience, recovery time (T) represents a measure of rapidity, and 1−X provides a measure of robustness, as in Ref. [6]. Predicted resilience is thus considered a function of these two factors.

The calculation of a value for predicted resilience is based on approximating the area under the quality curve represented by Fig. 1. Because the area above that curve may be approximated by calculating the area of the corresponding resilience triangle, the predicted resilience is generated by simply subtracting the area of that triangle from a <sup>fi</sup>xed larger area within which it is contained, and then representing the result as a percentage of that larger area (see Fig. 3).

This larger encompassing area is established by specifying a parameter T\* that serves as a strict upper bound on the set of possible values for T (assuming that beyond a certain time limit, a system has an effective resilience of 0) [21]. This allows various instances of predicted resilience to be compared on the same relative scale.

The actual predicted resilience function for the ordered pair (X, T) is then given by [21]:

$$
R (X, T) = \frac {T ^ {*} - \frac {X T}{2}}{T ^ {*}} = 1 - \frac {X T}{2 T ^ {*}} X \in [ 0, 1 ], T \in [ 0, T ^ {*} ].\tag{2}
$$

By construction, the minimum possible value for R(X, T) under this formulation (i.e., X=1 and T=T\*) is 0.5, and the corresponding maximum possible value (for X=0 or T=0) is 1.0. This is simply a result of basing the function on the area of the resilience triangle, and it is straightforward to rescale R(X,T) to the interval [0, 1], based upon the preferences of a given decision maker. We shall examine this in more detail in Section 5.1.

The relationship between X and T can now be written as:

$$
X T = (X - 0) (T - 0) = M, \text {   where   } M = (2   T ^ {*}) (1 - R),\tag{3}
$$

which is the equation of a rectangular hyperbola centered at (0,0) and with asymptotes lying on the X and T axes. Thus for a <sup>fi</sup>xed resilience value, R, (and a <sup>fi</sup>xed T\*) the set of all possible combinations of X and T describes a hyperbola. By systematically varying R, we therefore may generate a series of equilateral hyperbolas, all of the same shape, in the upper right quadrant of the plane (see Fig. 4), with larger values of R corresponding to curves closer to the origin.

Observations which lie on the lower right portion of each resilience curve represent scenarios for which the initial disasterrelated loss is very high but the recovery time is small. Such a situation may occur, for example, when an affected facility is located in an area with a very strong infrastructure and quick access to resources in support of rebuilding. In contrast, observations which lie on the upper left portion of each curve represent facilities which suffer a small initial loss but are faced with a relatively long recovery time. An example of such a case might be a well-constructed facility that is located in a relatively remote area, and for which fewer resources are immediately available for restoring functionality in a timely manner. Because both types of facility may have the same calculated resilience, however, this multi-dimensional representation offers an approach for easily differentiating between the very different situations that they represent.

![](/api/attachments/Q3Z2JASR/fulltext/images/5bae9b602d593b3b99437a5f0b859382a9b76b6d50e7d6663ba0d61480a6a9ca.jpg)  
Fig. 3. The predicted resilience triangle as a proportion of T\*

![](/api/attachments/Q3Z2JASR/fulltext/images/17600765b013433376dee9f85dd5b79f26e8633142bd490399c8be14c3184e6a.jpg)  
Fig. 4. Predicted resilience curves.

## 4. Incorporating decision maker preferences

As the previous discussion indicates, the ability to visually compare the relative resilience of multiple facilities with respect to both robustness and rapidity, as well as with respect to the predicted resilience value itself, can provide a decision maker with a more complete understanding of the impact of a potential disaster event upon their organization's assets. Furthermore, as suggested by Zobel [21], the individual preferences of that decision maker can be represented, to a certain extent, by allowing them to identify and characterize particular regions of interest within the overall resilience space.

It is important to recognize, however, that the visualization approach discussed above does not actually provide the ability for a decision maker to capture and represent their perception of the actual resilience value for a given facility. For example, Eq. (2) implies that for a given disaster event, a facility with a 10% loss of functionality and a recovery time of 20 months (assuming a maximum acceptable recovery time of T\*=100 months) would actually have a predicted resilience of 99%. This value may seem arti<sup>fi</sup>cially high to some decision makers. From the standpoint of interpreting such results and then using them to drive policy decisions, arti<sup>fi</sup>cially high values may ultimately have a negative impact on efforts to actually mitigate against the impact of a potential future disaster.

A decision maker may also wish to reduce (or increase) the differentiation between the given resilience values within a particular region of interest. For example, given a preference for smaller initial losses over smaller recovery times, a decision maker may feel that two facilities with the same predicted initial loss and a difference of only one month in recovery time should have much more similar resilience values than those that are actually produced by $\operatorname { E q . } \left( 2 \right)$ . As with the previous example, simply calculating a value for resilience is not suf<sup>fi</sup>cient if it does not match the needs of the decision maker and does not therefore support effective decision making.

In order to address this issue, and thus to make the concept of predicted resilience more applicable to actual decision makers, we introduce an approach to analytically representing a given decision maker's adjusted resilience function. This offers a means for calibrating the predicted resilience to <sup>fi</sup>t a decision maker's situational preferences, as suggested by Bruneau and Reinhorn [2], and thus it ultimately provides more value for resilience as an implementable analytic measure.

## 4.1. Representing preferences

The basis for our development of a function for adjusted resilience is the notion of threshold values for both X and T which identify the upper limits on the preferred set of values for each parameter. This idea was introduced by Chang and Shinozuka [5], in the context of de<sup>fi</sup>ning a region of acceptable resilience within which all values satisfy both constraints. We may extend this notion of a single preferred region, however, to recognize the additional regions which can be identi<sup>fi</sup>ed as “preferred” with respect to only one of the two parameters, as well as the region in which both parameters exceed their desired levels. Our approach to incorporating decision maker preferences is based upon these four regions and upon the relative perception of the resilience values within them, as provided by a given decision maker. Fig. 5 thus illustrates the subdivision of the underlying resilience domain, given speci<sup>fi</sup>c threshold values of <sup>ˆ</sup>X and <sup>ˆ</sup>T.

As an example of how different preferences may be represented in this context, we may compare the relative perception of observations in region 1 (desirable X and T) with the perception of observations in regions 2 (desirable T only) and 3 (desirable X only). If it is very important to a decision maker that values of T not exceed the threshold <sup>ˆ</sup>T, then we might expect resilience to decrease more rapidly (with respect to increases in T) in region 3 than is indicated by the original predicted resilience function. In contrast, if there is a relative indifference between values of X larger than ${ \hat { X } } ,$ for a particular T, then the relative decrease in actual resilience in region 2 (as X increases) may actually be perceived to be less than that provided by the predicted resilience. Fig. 6 provides an example of the adjusted resilience curves that might correspond to these two scenarios.

![](/api/attachments/Q3Z2JASR/fulltext/images/1bd63b80f8b2ca3ccf3eda060eed373514cb6cf3d365bae6eb1956fde9f2968a.jpg)  
Fig. 5. Resilience regions de<sup>fi</sup>ned by X̂ and T̂.

## 4.2. Assumptions

Several important assumptions are implicit in the resilience pro<sup>fi</sup>le re<sup>fl</sup>ected in Fig. 6. The <sup>fi</sup>rst assumption is that there are only four regions of interest, as described above, which represent the more or less preferred ranges of values for both X and T. Although these ranges could themselves be further sub-divided to represent more levels of preference, this initial partitioning concisely represents the opportunity for characterizing different preferences, and thus best supports the initial development of the underlying model, as given in the later part.

The second implicit assumption is that, rather than there being a discrete drop in resilience immediately above the threshold values, the adjusted resilience remains a continuous function of X and T throughout the domain (with the option to suddenly increase the rate at which resilience decreases beyond these threshold values). Thus incremental changes in X or T correspond to incremental changes in adjusted resilience.

The third assumption inherent in Fig. 6 is that adjusted resilience maintains, within each region, the basic hyperbolic nature of the original predicted resilience function. This ensures not only that increasing values of X or T will always correspond to decreasing resilience (and thus that the marginal slope of the resilience function is always decreasing) but also that the slope in a region will always be constant for any <sup>fi</sup>xed value of X or T. This constant marginal rate of change is a consequence of the triangular nature of the resilience function, and it directly re<sup>fl</sup>ects the underlying relationship between X and T.

With these assumptions in mind, we can explicitly de<sup>fi</sup>ne a formulation for the adjusted resilience function. Because different decision makers will likely have different preferences in each region, the formulation includes a number of adjustable parameters that can help <sup>fi</sup>t the function to a particular set of preferences. Following the development of the generalized model formulation, we brie<sup>fl</sup>y discuss the issue of actually collecting these preferences, and then introduce an approach for determining values for the parameters that can provide an optimal <sup>fi</sup>t for a given decision maker.

![](/api/attachments/Q3Z2JASR/fulltext/images/5d66dcab221c9f9ceb9ee48d0e0616988b6c94f04b89e1b9312b98931ad6b827.jpg)  
Fig. 6. Example of adjusted resilience curves.

## 5. Adjusted resilience function

The adjusted resilience function de<sup>fi</sup>ned in the later part incorporates three different parameters that can be used to adjust the original predicted resilience to better <sup>fi</sup>t a decision maker's preferences. The <sup>fi</sup>rst parameter, α, is used to adjust the overall slope of the resilience function, so that its value may be either reduced or increased as necessary. The other two parameters, γ and $^ { \mathsection , }$ serve a similar function, but only for the regions corresponding to “less acceptable” values for either X or T. In combination, these three parameters can provide signi<sup>fi</sup>cant <sup>fl</sup>exibility for <sup>fi</sup>tting the adjusted resilience function to the speci<sup>fi</sup>c preferences of a given decision maker or organization.

## 5.1. Adjusting resilience on the entire domain

As discussed previously, one of the potential issues with the original predicted resilience function is that it may generate values that are generally scaled higher (or lower) than a decision maker might otherwise prefer. Because resilience can be only de<sup>fi</sup>ned on the interval [0,1], however, the amount and type of change that can be applied is restricted. In particular, one cannot simply add a <sup>fi</sup>xed amount to the resilience of each observation because this will lead to a number of values greater than one. We thus introduce a parameter, $\alpha ,$ that is used to adjust the original resilience value by a proportion of the amount by which it differs from the maximum value of 1, and which therefore keeps the relative impact of this adjustment consistent for all observations in the domain.

The following equation allows for adjusting the predicted resilience de<sup>fi</sup>ned in Eq. (2), and also maintains the symmetric hyperbolic relationship between X and T.

$$
R _ {\alpha} (X, T) = 1 - \left(\frac {X T}{2 T ^ {*}}\right) + \alpha \left(\frac {X T}{2 T ^ {*}}\right) = 1 - \left(\frac {X T - \alpha X T}{2 T ^ {*}}\right) = 1 - \left(\frac {(1 - \alpha) X T}{2 T ^ {*}}\right).\tag{4}
$$

In order for $\operatorname { E q . } \left( 4 \right)$ to represent resilience, as it has been de<sup>fi</sup>ned, not only must all $R _ { \alpha } ( X , T )$ be contained within the interval [0,1] but also the choice of α must support the assumptions stated in Section 4.2. Section 6 will therefore be used to derive bounds on the set of possible values for α, as well as those for each of the other parameters discussed below.

It is important to note that setting $\alpha = 0$ in Eq. (4) gives the original predicted resilience function of Eq. (2), and setting $\alpha = - 1$ effectively rescales resilience to the interval [0, 1]. Because $R _ { \infty } ( X , T )$ is symmetric, any such changes in the value of α will have exactly the same impact on both X and T. In order to allow for adjustments associated with only one of these two variables, we must therefore introduce additional parameters, γ and δ. The following discussion describes how these parameters are subsequently incorporated into the new resilience function.

## 5.2. Adjusting resilience outside each “preferred” region individually

Let $\hat { X }$ and $\hat { T }$ represent a decision maker's chosen threshold values for X and T respectively. The speci<sup>fi</sup>cation of theses threshold values provides the opportunity to consider adjusting resilience outside of the “preferred” region for each variable. Because we are assuming that the perceived resilience function is continuous over the entire domain, however, any changes to the formulation of the resilience function as it transitions from a “more preferred” to a “less preferred” region must re<sup>fl</sup>ect this continuity. One approach to this is to restrict the adjustment of the “less preferred” resilience values to a proportion of the possible amount of available change, as we did in Section 5.1. However, rather than being bounded above by a maximum resilience value of 1, observations in the “less preferred” regions are instead bounded above by the resilience values that are achieved at the boundaries with the “preferred” regions.

The additional adjustment of the resilience function thus proceeds as follows: Let γ be the parameter used to specify the amount of change associated with T, and let δ be the corresponding parameter used to specify change in the resilience function with respect to X. Given the current adjusted resilience function, as de<sup>fi</sup>ned in Eq. (4), we may further adjust it for values of $T \geq \hat { T }$ and $X { \le } \hat { X }$ by incorporating γ in the following way:

Region 3 : $\left( X \leq \hat { X } , T \geq \hat { T } \right)$

$$
\begin{array}{l} R _ {\alpha \gamma} (X, T) = 1 - \left(\frac {(1 - \alpha) (X T)}{2 T ^ {*}}\right) \\ \qquad + \gamma \left(\left(\frac {(1 - \alpha) (X T)}{2 T ^ {*}}\right) - \left(\frac {(1 - \alpha) (X \hat {T})}{2 T ^ {*}}\right)\right) \\ \qquad = 1 - \left(\frac {(1 - \alpha) (X T + \gamma X (T - \hat {T}))}{2 T ^ {*}}\right) \\ \qquad = 1 - \left(\frac {(1 - \alpha) X (T + \gamma (T - \hat {T}))}{2 T ^ {*}}\right) \end{array}\tag{5}
$$

It can easily be seen that $R _ { \alpha \gamma } \big ( X , \hat { T } \big ) = R _ { \alpha } \big ( X , \hat { T } \big )$ for all $\boldsymbol { X } { \le } \hat { \boldsymbol { X } }$ regardless of the value of $\gamma .$ This ensures that the resilience varies continuously across T for any X in the preferred region. Furthermore, since $( 1 - \alpha ) \gamma$ in Eq. (5) is being multiplied by a non-negative value (because $T { \geq } \ddot { T } ,$ , and $X , T 2 0 )$ , the sign of $( 1 - \alpha ) \gamma$ determines whether or not the slope in Region 3 is being increased or decreased over that associated with $\operatorname { E q . } \left( 4 \right)$

In much the same way, we may also adjust Eq. (4) for values of $X { \geq } \hat { X }$ and $T { \le } \hat { T }$ by incorporating δ as follows:

Region 2 : $\left( X \geq \hat { X } , T \leq \hat { T } \right)$

$$
\begin{array}{l} R _ {\alpha \delta} (X, T) = 1 - \left(\frac {(1 - \alpha) (X T)}{2 T ^ {*}}\right) \\ \qquad + \delta \left(\left(\frac {(1 - \alpha) (X T)}{2 T ^ {*}}\right) - \left(\frac {(1 - \alpha) (\hat {X} T)}{2 T ^ {*}}\right)\right) \\ \qquad = 1 - \left(\frac {(1 - \alpha) (X T + \delta T (X - \hat {X}))}{2 T ^ {*}}\right) \\ \qquad = 1 - \left(\frac {(1 - \alpha) T (X + \delta (X - \hat {X}))}{2 T ^ {*}}\right) \end{array}\tag{6}
$$

Then, as above, $R _ { \propto \delta } \left( { \hat { X } } , T \right) = R _ { \propto } \left( { \hat { X } } , T \right)$ for all $T { \le } \hat { T } ,$ , and the combined function is continuous across X for any given T in the preferred region.

## 5.3. Adjusting resilience outside both “preferred” regions

If both X and T meet or exceed their respective thresholds at the same time, we encounter a situation in which each of α, γ, and δ may be simultaneously incorporated into the adjusted resilience function. The new function given in Eq. (7) re<sup>fl</sup>ects the overall combination of these different adjustments:

Region $4 : \left( X \geq \hat { X } , T \geq \hat { T } \right)$

$$
\begin{array}{l} R _ {\alpha \gamma \delta} (X, T) = 1 - \left(\frac {(1 - \alpha) (X T)}{2 T ^ {*}}\right) \\ \qquad + \delta \left(\left(\frac {(1 - \alpha) (X T)}{2 T ^ {*}}\right) - \left(\frac {(1 - \alpha) (\hat {X} T)}{2 T ^ {*}}\right)\right) \\ \qquad + \gamma \left(\left(\frac {(1 - \alpha) (X T)}{2 T ^ {*}}\right) - \left(\frac {(1 - \alpha) (X \hat {T})}{2 T ^ {*}}\right)\right) \\ \qquad = 1 - \left(\frac {(1 - \alpha) (X T + \delta T (X - \hat {X}) + \gamma X (T - \hat {T}))}{2 T ^ {*}}\right) \end{array}\tag{7}
$$

As with Eqs. (5) and (6), the resilience function given in Eq. (7) transitions smoothly and continuously to the corresponding functions in the adjoining regions since $R _ { \alpha \gamma \delta } \bigl ( \hat { X } , T \bigr ) = \dot { R } _ { \alpha \gamma } \bigl ( \hat { X } , \breve { T } \bigr )$ and $R _ { \alpha \gamma \delta } \left( X , \hat { T } \right) = R _ { \alpha \delta } \left( X , \hat { T } \right)$

## 5.4. Overall adjusted resilience

By combining Eqs. $( 4 ) - ( 7 )$ , we may therefore de<sup>fi</sup>ne the overall adjusted resilience function, for a given choice of α, γ and δ, as follows:

$$
R _ {(\alpha , \gamma , \delta)} (X, T) = \left\{ \begin{array}{l l} R _ {\alpha} (X, T) = 1 - \left(\frac {(1 - \alpha) X T}{2 T ^ {*}}\right) & \text { for } X \leq \hat {X}, T \leq \hat {T} \\ R _ {\alpha \gamma} (X, T) = 1 - \left(\frac {(1 - \alpha) X (T + \gamma (T - \hat {T}))}{2 T ^ {*}}\right) & \text { for } X \leq \hat {X}, T > \hat {T} \\ R _ {\alpha \delta} (X, T) = 1 - \left(\frac {(1 - \alpha) T (X + \delta (X - \hat {X}))}{2 T ^ {*}}\right) & \text { for } X > \hat {X}, T \leq \hat {T} \\ R _ {\alpha \gamma \delta} (X, T) = 1 - \left(\frac {(1 - \alpha) (X T + \delta T (X - \hat {X}) + \gamma X (T - \hat {T}))}{2 T ^ {*}}\right) & \text { for } X > \hat {X}, T > \hat {T} \end{array} \right.\tag{8}
$$

where $\mathtt { X } \in [ 0 , \ 1 ]$ and ${ \mathrm { T } } \in [ 0 , \ { \mathrm { T } } ^ { * } ] .$ . Each combination of $\alpha , \gamma$ and δ represents a different type of adjustment to the original predicted resilience function, and thus each such combination represents a different overall resilience pro<sup>fi</sup>le.

## 6. Establishing bounds on the parameter values

Given the range of possible resilience values and the assumptions presented in Section 4.2, the adjusted resilience function given above must satisfy the following for all $X { \in } [ 0 , X ^ { * } ]$ and $T \in [ 0 , T ^ { * } ]$ ]:

$$
R _ {(\alpha , \gamma , \delta)} (X, T) \geq 0\tag{9}
$$

$$
R _ {(\alpha , \gamma , \delta)} (X, T + \Delta_ {T}) \leq R _ {(\alpha , \gamma , \delta)} (X, T) \quad \forall \Delta_ {T} \in [ 0, T ^ {*} - T ]\tag{10}
$$

$$
R _ {(\alpha , \gamma , \delta)} (X + \Delta_ {X}, T) \leq R _ {(\alpha , \gamma , \delta)} (X, T) \quad \forall \Delta_ {X} \in [ 0, X ^ {*} - X ]\tag{11}
$$

These necessary conditions allow us to easily identify bounds on parameters α, γ and δ:

## 6.1. Constraint 1: negative slopes

Eqs. (10) and (11) indicate that the partial derivatives of R must be negative in each of the four quadrants. We may thus derive the following bounds on the values of the parameters α, γ and δ:

Region $1 : X { \le } \hat { X } , T { \le } \hat { T }$

$$
\frac {d R}{d X} = - \left(\frac {(1 - \alpha) T}{2 T ^ {*}}\right) \leq 0 \Rightarrow \left(\frac {(1 - \alpha) T}{2 T ^ {*}}\right) \geq 0 \Rightarrow (1 - \alpha) \geq 0 \Rightarrow \alpha \leq 1\tag{12}
$$

This same upper bound on the value of ∝ is reached by similarly analyzing dR/dT. Because α takes on a single value across all four quadrants, Eq. (12) holds for all $X { \in } [ 0 , X ^ { * } ]$ and $T \in [ 0 , T ^ { * } ]$

Region $2 : X { \geq } \hat { X } , T { \leq } \hat { T } ;$

$$
\frac {d R}{d T} = \left(\frac {(1 - \alpha) T (1 + \delta)}{2 T ^ {*}}\right) \leq 0 \Rightarrow (1 - \alpha) T (1 + \delta) \geq 0 \Rightarrow \delta \geq - 1\tag{13}
$$

This lower bound on the value of δ is independent of the values of the other parameters, and given this result, dR/dT will always also be less than or equal to zero within Region 2. Since δ must have the same value in Regions 2 and 4, Eq. (1) holds in both quadrants.

Region $3 : X { \le } \hat { X } , T { \ge } \hat { T }$

$$
\frac {d R}{d T} = \left(\frac {(1 - \alpha) X (1 + \gamma)}{2 T ^ {*}}\right) \leq 0 \Rightarrow (1 - \alpha) X (1 + \gamma) \geq 0 \Rightarrow \gamma \geq - 1\tag{14}
$$

As above, this lower bound on γ is independent of the values of the other parameters. It also leads to a result of d $\mathrm { { R } / \mathrm { { d } } X \leq 0 }$ within Region 3, and it applies to both Region 3 and Region 4.

Region $4 : X { \geq } \hat { X } , T { \geq } \hat { T } :$

$$
\begin{array}{r l} \frac {d R}{d T} = - \left(\frac {(1 - \alpha) (T (1 + \delta + \gamma) - \gamma \hat {T})}{2 T ^ {*}}\right) & \leq 0 \\ & \Rightarrow \left(\frac {(1 - \alpha) (T (1 + \delta + \gamma) - \gamma \hat {T})}{2 T ^ {*}}\right) & \geq 0 \\ & \Rightarrow (1 - \alpha) (T (1 + \delta + \gamma) - \gamma \hat {T}) & \geq 0 \\ & \Rightarrow T (1 + \delta + \gamma) & \geq \gamma \hat {T} \end{array}\tag{15}
$$

Since $( 1 + \delta )$ is non-negative and $T > { \hat { T } } ,$ this relationship is true for all $T \in \left( \hat { T } , T ^ { * } \right]$ , as long as $( 1 + \delta + \gamma ) \geq 0$ . Given $( 1 + \delta + \gamma ) < 0$ however, the relationship will hold for all $T \in \left( \hat { T } , T ^ { * } \right]$ only if it is true for T<sup>\*</sup>. The following thus provides a conditional lower bound on γ, given δ:

$$
\Rightarrow T ^ {*} (1 + \delta + \gamma) \geq \gamma \hat {T}\tag{16}
$$

Similarly, from analyzing dR/dT, we get a conditional lower bound on δ, given γ:

$$
\dots \Rightarrow X ^ {*} (1 + \delta + \gamma) \geq \delta \hat {X}\tag{17}
$$

Both of these lower bounds will apply within any quadrant that utilizes the associated parameter within its portion of the adjusted resilience function.

6.2. Constraint 2: $R ( X ^ { * } , T ^ { * } ) { > } = 0$

By de<sup>fi</sup>nition, $\mathtt { R } ( 0 , 0 ) = 1$ and all predicted resilience values must fall on the interval [0,1]. Because the marginal slope of the predicted resilience function is negative everywhere in the state space, however, this implies that the smallest possible predicted resilience must be achieved at R(X\*,T\*). We may therefore ensure that all values of R are properly constrained by requiring that $\ R ( { \mathrm { X } } ^ { * } , { \mathrm { T } } ^ { * } ) { > } = 0 .$ . This requirement provides the following relationship and establishes our <sup>fi</sup>nal bounds on α, γ and δ:

$$
R (X ^ {*}, T ^ {*}) = 1 - \left(\frac {(1 - \alpha) \left(X ^ {*} T ^ {*} + \delta T \left(X ^ {*} - \hat {X}\right) + \gamma X ^ {*} (T ^ {*} - \hat {T})\right)}{2 T ^ {*}}\right) \geq 0
$$

$$
\Rightarrow \frac {2 T ^ {*}}{(1 - \alpha)} \geq X ^ {*} T ^ {*} (1 + \delta + \gamma) - \gamma X ^ {*} \hat {T} - \delta \hat {X} T ^ {*}\tag{18}
$$

As in Eqs. (15) and (16), this derived relationship provides conditional bounds on each of the parameters. In particular, it provides a lower bound on the value of α, and an upper bound on the values of γ and δ, each relative to the values of each of the other parameters.

## 7. Fitting decision makers' preferences

Given the adjusted resilience function and the associated bounds on each of the component parameters, we may now consider the task of <sup>fi</sup>nding the set of parameter values that most accurately represents the implicit perceptions that a particular decision maker may have about the $" \mathrm { t r u e } "$ disaster resilience of a given system. In order to accomplish this task, it is necessary to <sup>fi</sup>rst capture and quantify a representative set of such “resilience perceptions” which can be used as the basis for deriving the most appropriate parameter values. There are a number of techniques in the literature which could be useful for this purpose, including the analytic hierarchy process (AHP) [16] which provides a widely used approach for establishing preferences between different alternatives.

Although it could be effective, however, a highly structured approach such as the AHP is not necessarily required to gather a decision maker's perceptions. For example, one alternative approach would be to have the decision maker directly specify what he or she perceives to be the relative resilience associated with a number of different hypothetical scenarios, based on experience and intuition. These perceived values could then be compared and validated against a baseline of calculated predicted resilience values for each individual scenario. Similarly, the decision maker could instead specify their perception of the “true” resilience of scenario by starting with the baseline values and indicating the relative amount by which these values would need to change in order to re<sup>fl</sup>ect their preferences.

For the sake of the following discussion we simply assume that a reasonable set of such values has somehow been determined, and that it can be used as the basis for choosing parameters to <sup>fi</sup>t the adjusted resilience function to a decision maker's preferences. A more in-depth look at the advantages and disadvantages of different approaches for achieving these speci<sup>fi</sup>ed resilience values is an important future research area from the standpoint of establishing alternative options for implementation.

## 7.1. Optimization model

Let S be a <sup>fi</sup>nite set of scenarios (observations) which have been chosen as the basis for collecting perceived resilience values from a decision maker. For each $( x _ { i } , t _ { i } ) \in S ,$ we may then let $R _ { ( * , * , * ) } ( x _ { i } t _ { i } )$ be the corresponding perceived resilience value that the decision maker has speci<sup>fi</sup>ed for that scenario, and de<sup>fi</sup>ne $R _ { * } ^ { S } = \{ R _ { ( * , * , * ) } ( x _ { i } t _ { i } ) : ( x _ { i } t _ { i } ) \in S \}$

Given R<sup>S</sup> and a speci<sup>fi</sup>cation for $\hat { T }$ and for X<sup>ˆ</sup> , we wish to <sup>fi</sup>nd values for α, γ and δ that will “best” <sup>fi</sup>t the adjusted resilience function $R _ { ( \alpha , \gamma , \delta ) } ( x , t )$ to the decision maker's perceived resilience structure on S. Depending on the number of different scenarios in S and the extent to which $R _ { * } ^ { S }$ accurately represents the decision maker's preferences, we may then conclude that $R _ { ( \alpha , \gamma , \delta ) } ( x , t )$ represents the overall adjusted resilience function for that particular decision maker.

The following optimization model provides a simple approach for optimizing the <sup>fi</sup>t between $R _ { ( * , * , * ) } ( x , t )$ and $R _ { ( \alpha , \gamma , \delta ) } ( x , t )$ on S, based on the de<sup>fi</sup>nition of the adjusted resilience function and the derived bounds on the individual parameter values:

$$
\begin{array}{l} \text {(P1)} \quad \min _ {\text {s.t.}} f (\alpha , \gamma , \delta) = \sum_ {i \in S} \left(R _ {(*, *, *)} (x _ {i}, t _ {i}) - R _ {(\alpha , \gamma , \delta)} (x _ {i}, t _ {i})\right) ^ {2} \\ \alpha \leq 1 \\ \delta \geq - 1 \\ \gamma \geq - 1 \\ T ^ {*} (1 + \delta + \gamma) - \gamma \hat {T} \geq 0 \\ X ^ {*} (1 + \delta + \gamma) - \delta \hat {X} \geq 0 \\ \frac {2 T ^ {*}}{(1 - \alpha)} - \left(X ^ {*} T ^ {*} (1 + \delta + \gamma) - \gamma X ^ {*} \hat {T} - \delta \hat {X} T ^ {*}\right) \geq 0 \end{array}
$$

The solution to (P1) is the set of parameters, (α, γ, and δ), that minimizes the squared error in the objective function. These parameters then serve to de<sup>fi</sup>ne the adjusted resilience function for the individual whose preferences are re<sup>fl</sup>ected by R<sup>S</sup>.

Deriving this adjusted resilience function allows us to generalize the behavior exhibited by $R _ { * } ^ { S } ,$ so that we may provide the decision maker with values for the relative resilience of new scenarios that are consistent with his or her preferences. The extent to which these new values can actually match the decision maker's “true” preferences will depend, however, on the number of observations in R<sup>S</sup>, as well as on the accuracy of each observation in R<sup>S</sup>. For this reason, it is important to consider the speci<sup>fi</sup>cation of a particular adjusted resilience function as part of an iterative process of re<sup>fi</sup>nement. As the set of analyzed scenarios, S, is expanded or updated, (P1) can be re-solved and the adjusted resilience function updated so that it re<sup>fl</sup>ects the most recent assessment of the decision maker's resilience perceptions.

## 7.2. Example

The following example illustrates the effect of applying the optimization model to a set of decision maker-speci<sup>fi</sup>ed resilience values.

Consider an organization that is planning the construction of a new warehouse facility in an area susceptible to potential hurricane damage, and suppose that the manager in charge of the planning process has speci<sup>fi</sup>ed that $\hat { T } = 3 0$ weeks and X<sup>ˆ</sup> =30% are the upper limits on what would be considered manageable levels of recovery time and infrastructure loss, respectively. Furthermore, suppose that $\mathrm { T } ^ { * } = 1 0 0$ weeks represents an overall upper limit on the projected amount of recovery time that might actually be undertaken, due to any storm that might occur.

Given these assumptions, the initial predicted resilience function (Eq. (2)) may be formulated and presented to the manager as a preliminary indication of the resilience of the facility due to different combinations of initial loss and recovery time. By using this function as a baseline, the manager can then specify the extent to which his or her perceptions differ for several representative scenarios.

This initial set, S, of representative scenarios can be chosen in such a way as to leverage the fact that, by de<sup>fi</sup>nition, the adjusted resilience function is linear within each of the regions de<sup>fi</sup>ned by X<sup>ˆ</sup> and <sup>ˆ</sup>T. In particular, the adjusted slope of the function within Regions 2 and 3 (due to the combination of α and δ or α and γ) can be determined from just two adjusted observations in each case, whereas the adjusted slope in Region 1 (due to just α) can be determined by a single adjusted observation from that region. As a simple illustration of the approach, therefore, our example uses a total of four observations: one observation on the threshold between Region 1 and Regions 2 and 3, and one more within each of Regions 2 and 3.

In general, using such a limited number of observations to de<sup>fi</sup>ne the decision maker's adjusted resilience function would typically be appropriate only in the context of an initial attempt at codifying the individual's perceptions. Not only might it be dif<sup>fi</sup>cult for an individual to accurately assess the resilience for each observation, but also he or she might be inconsistent in assessing the relative differences between the observations. As discussed previously, assessing a larger number of observations in an iterative fashion can allow for these relative differences to be more precisely balanced and re<sup>fi</sup>ned.

With this in mind, the set of scenarios given in Table 1 were chosen as the basis for generating an initial adjusted resilience function for the warehouse construction manager. Each one includes the calculated predicted resilience value as well as the manager's perceptions of the “true” resilience value.

Note that the observations in Table 1 have been chosen so that the original predicted resilience value is the same for observations 1 and 3, and also for observations 2 and 4, since each set of points lies on a single resilience curve. Additionally, observations 1 and 2 share the same value for T and observations 3 and 4 share the same value for X. This provides the opportunity for a decision maker to assess the relative resilience of a given observation with respect to at least two other points, and thus helps with the overall consistency of the assessments.

According to the perceived resilience values in Table 1, the manager believes that the actual resilience embodied in an outcome of 30% loss of functionality and 15 weeks of recovery time is (or should be) less than that provided by the predicted resilience function. The same is true for the combination of 15% loss and 30 weeks of recovery time. It is important to note that these two scenarios have had, and must have, their resilience adjusted by the same amount (if it is adjusted at all). This is because both scenarios fall within what has been identi<sup>fi</sup>ed as the “acceptable” region for both threshold values (corresponding to “small enough” values for both variables together), and thus they are only affected by changes to the α parameter. If this identical amount of adjustment is not consistent with the decision maker's perceptions of their relative value, then it indicates the need to revisit the speci<sup>fi</sup>cation of X<sup>ˆ</sup> and <sup>ˆ</sup>T. This could be accomplished by extending $R _ { ( \propto , \gamma , \delta ) } ( X , T )$ to be a function also of the parameters X<sup>ˆ</sup> and <sup>ˆ</sup>T. If these parameters are also allowed to vary within the optimization then the resulting problem can be used to further clarify the notion of the “preferred region” that they serve to de<sup>fi</sup>ne, and thus to more accurately match the decision maker's overall resilience perceptions.

The perceived resilience values in Table 1 also indicate that in comparing scenarios 2 and 4, the manager prefers a longer recovery time and less initial damage over a shorter recovery time but more loss of functionality, perhaps due to the potential for continuing to utilize part of the facility during repairs. There is also a much larger difference between the perceived resilience values for scenarios 1 and 2 than there is between the original predicted resilience values, implying that the manager feels that even with a relatively short recovery time, 50% loss of functionality is more signi<sup>fi</sup>cant than initially indicated.

Resilience scenarios for deriving an adjusted resilience function.

<table><tr><td colspan="3">Observations</td><td rowspan="2">Predicted resilience</td><td rowspan="2">Perceived resilience</td></tr><tr><td>Number</td><td>X</td><td>T</td></tr><tr><td>1</td><td>0.3</td><td>15</td><td>0.9775</td><td>0.95</td></tr><tr><td>2</td><td>0.5</td><td>15</td><td>0.9625</td><td>0.90</td></tr><tr><td>3</td><td>0.15</td><td>30</td><td>0.9775</td><td>0.95</td></tr><tr><td>4</td><td>0.15</td><td>50</td><td>0.9625</td><td>0.92</td></tr></table>

Once the perceived resilience values were speci<sup>fi</sup>ed, the optimization routine was used to identify the set of parameters that provide the closest <sup>fi</sup>t between these values and the adjusted resilience function. The routine was implemented in Microsoft Excel, using the Risk Solver Platform, version 9.0.

Table 2 provides the resulting parameter values that de<sup>fi</sup>ne the adjusted resilience function. As can then be seen in Table 3, the adjusted resilience is much closer to the stated perceived resilience than it is to the original predicted resilience, thus more accurately re<sup>fl</sup>ecting the decision maker's true preferences. The two sets of values are not identical because the parameters, and thus the adjusted resilience function, are restricted by the upper and lower bounds on their values, given the chosen values for X<sup>ˆ</sup> , <sup>ˆ</sup>T, and T\*.

Fig. 7 illustrates the difference between the adjusted resilience function given by Table 2, and the original predicted resilience function. Although further re<sup>fi</sup>nement of the adjusted resilience could consequently be based on either of these functions, one would expect quicker convergence to a truly representative set of parameters if it were the most recent adjusted resilience function that was used as the basis for updating the representation of the decision maker's preferences.

## 8. Conclusions

This research effort extends the concept of disaster resilience by providing an approach for visually and analytically representing the perceptions of an individual decision maker of the “true” resilience value associated with the predicted initial loss (X) and associated time to recovery (T) for a system within any disaster scenario. The discussion speci<sup>fi</sup>cally builds upon the notion of the resilience triangle, as introduced by Bruneau et al. [4], and the complementary measure of predicted resilience, as de<sup>fi</sup>ned by Zobel [21], and it provides for a more complete understanding of the potential signi<sup>fi</sup>cance of a given disaster event. This, in turn, allows for improved support for strategic disaster planning and mitigation.

There are a number of situations in which the ability to establish an accurate representation of the relative value of different disaster scenarios can provide such decision making support. For example, in analyzing a new construction project for a distribution center a decision maker may determine that he or she wishes the new facility to have at least as much overall resilience as an already existing center, given a potential disaster scenario. Provided with the opportunity to construct the new facility in such a way as to keep initial losses to 10%, the decision maker would then be able to identify the associated recovery time that would need to be achieved in order to then reach the desired level of resilience. Changes could then be made in the organization's overall plan in order to provide support for such activities as pre-positioning additional emergency stock in nearby facilities or establishing pre-determined contracts with suppliers or construction companies, in order to ensure that resources are available both for continuing operations at a reasonable level and for recovering in the desired time frame from the physical damage that will have occurred.

Table 2 Optimal parameter values.

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>α</td><td>-1.4203</td></tr><tr><td>γ</td><td>-0.3995</td></tr><tr><td>δ</td><td>0.1514</td></tr></table>

Table 3  
Comparative resilience results.

<table><tr><td>Predicted resilience</td><td>Perceived resilience (specified by decision maker)</td><td>Adjusted resilience</td></tr><tr><td>0.9775</td><td>0.95</td><td>0.9455</td></tr><tr><td>0.9625</td><td>0.90</td><td>0.9037</td></tr><tr><td>0.9775</td><td>0.95</td><td>0.9455</td></tr><tr><td>0.9625</td><td>0.92</td><td>0.9237</td></tr></table>

Similarly, given the existing infrastructure at the potential site, if the organization wished to achieve full recovery within 6 months, then they could estimate the maximum amount of infrastructure loss that would still allow them to attain a target of at least 90% resilience. From an infrastructure investment standpoint, the ability to balance the two factors would also allow them to consider the “true” relative value of attempting to decrease the recovery time to <sup>fi</sup>ve months, in terms of the increased amount of associated “acceptable” loss that this would then allow.

Because it is well recognized that disaster resilience is associated with more than just physical infrastructure, we must also consider the extent to which the proposed measure can be used to capture and represent the multi-dimensional nature of resilience. As an example of this in the literature, Chang and Shinozuka [5] calculate the resilience associated with each of the concept's four dimensions (technical, organizational, social, and economic) in turn, and then simultaneously present the results in the context of these multiple dimensions. A similar approach could easily be taken with adjusted resilience, so that a value for the adjusted resilience is generated for each of the dimensions in turn, and with the combined set of values (and the corresponding set of resilience curves) providing a broader, multi-dimensional view of the resilience of the entire system.

Since the process of gathering a decision maker's perceptions of resilient behavior, and then generating and visualizing their associated adjusted resilience function(s), will tend to be iterative in nature, computer-based decision support is a necessary component of incorporating the concept of adjusted resilience into the planning operations of an organization. Data management, optimization, and visualization capabilities are all critical for implementing the concept and for supporting a <sup>fl</sup>exible decision making process. Despite some complexity in its modeling and representation, however, the actual concept of adjusted resilience is relatively simple and straightforward. As such, we feel that it has the opportunity to play an important role in improving the ability of individuals and organizations to assess potential disaster resilience, and thus to make decisions that can help improve their protection against and recovery from the occurrence of a disaster event.

![](/api/attachments/Q3Z2JASR/fulltext/images/6b19fcf32dbaa5b0d7c9d95c060f80d91c6509fe316f9e89abd7f35eea37aac4.jpg)  
Fig. 7. Comparison of predicted (red) and adjusted (blue) resilience curves.

## References

[1] R. Bea, I. Mitroff, D. Farber, H. Foster, K. Roberts, A new approach to risk: the implications of E3, Risk Management 11 (1) (2009) 30–43.

[2] M. Bruneau, A. Reinhorn, Seismic resilience of communities-conceptualization and operationalization, Proceedings, International Workshop on Performance based Seismic-Design, Bled, Slovenia, June 28–July 1, 2004, Bled, Slovenia.

[3] M. Bruneau, A. Reinhorn, Exploring the concept of seismic resilience for acute care facilities, Earthquake Spectra 23 (2007) 41.

[4] M. Bruneau, S.E. Chang, R.T. Eguchi, G.C. Lee, T.D. O'Rourke, A.M. Reinhorn, M. Shinozuka, K. Tierney, W.A. Wallace, D. von Winterfeldt, A framework to quantitatively assess and enhance the seismic resilience of communities, Earthquake Spectra 19 (4) (2003) 733–752.

[5] S.E. Chang, M. Shinozuka, Measuring improvements in the disaster resilience of communities, Earthquake Spectra 20 (3) (2004) 739–755.

[6] G. Cimellaro, A. Reinhorn, M. Bruneau, Seismic resilience of a hospital system, Structure and Infrastructure Engineering 6 (1) (2010) 127–144.

[7] S. Cutter, L. Barnes, M. Berry, C. Burton, E. Evans, E. Tate, J. Webb, A place-based model for understanding community resilience to natural disasters, Global Environmental Change 18 (4) (2008) 598–606.

[8] R. Klein, R. Nicholls, F. Thomalla, Resilience to natural hazards: how useful is this concept? Global Environmental Change Part B: Environmental Hazards 5 (1–2) (2003) 35–45.

[9] S. Manyena, The concept of resilience revisited, Disasters 30 (4) (2006) 434–450.

[10] T. McDaniels, S.E. Chang, D. Cole, J. Mikawoz, H. Longstaff, Fostering resilience to extreme events within infrastructure systems: characterizing decision contexts for mitigation and adaptation, Global Environmental Change 18 (2) (2008) 310–318.

[11] D. Mendonça, Decision support for improvisation in response to extreme events: learning from the response to the 2001 World Trade Center attack, Decision Support Systems 43 (3) (2007) 952–967.

[12] Available at http://dictionary.oed.com/.

[13] M. Randles, D. Lamb, E. Odat, A. Taleb-Bendiab, Distributed redundancy and robustness in complex systems, Journal of Computer and System Sciences (in press), doi:10.1016/j.jcss.2010.01.008.

[14] A. Rose, De<sup>fi</sup>ning and measuring economic resilience to disasters, Disaster Prevention and Management 13 (4) (2004) 307–314.

[15] A. Rose, G. Adosu, S.Y. Liao, Business interruption impacts on the electric power system resilience to a total blackout of a terrorist attack of Los Angeles: customer resilience to a total blackout, Risk Analysis 27 (3) (2007) 513–531.

[16] T.L. Saaty, How to make a decision—the analytic hierarchy process, European Journal of Operational Research 48 (1) (1990) 9–26.

[17] M. Shinozuka, S.E. Chang, T.-C. Cheng, M. Feng, T.D. O'Rourke, M.A. Saadeghvaziri, X. Dong, X. Jin, Y. Wang, P. Shi, Resilience of integrated power and water systems, in: MCEER (Ed.), MCEER Research Progress and Accomplishments: 2003–2004, 2004, pp. 65–86, Buffalo, NY

[18] D.E. Snediker, A.T. Murray, T.C. Matisziw, Decision support for network disruption mitigation, Decision Support Systems 44 (2008) 954–969.

[19] K. Tierney, M. Bruneau, Conceptualizing and measuring resilience: a key to disaster loss reduction, TR News, 2007, pp. 14–17.

[20] H. Zhou, J. Wang, J. Wan, H. Jia, Resilience to natural hazards: a geographic perspective, Natural Hazards 53 (1) (2010) 21–41.

[21] C.W. Zobel, Comparative visualization of predicted disaster resilience, Proceedings of the 7th International ISCRAM Conference., 2010, Seattle, WA.

Christopher W. Zobel is an associate professor of Business Information Technology at Virginia Tech. He received the Ph.D in Systems Engineering from the University of Virginia, an M.S. in Mathematics from the University of North Carolina at Chapel Hill, and a B.A. in Mathematics from Colgate University. His primary research interests are in the area of intelligent decision support systems and knowledge management for multi-organizational networks, particularly in the realm of disaster operations management. Dr. Zobel has published articles in Decision Sciences, the International Journal of Production Research, and the European Journal of Operational Research, among others, and he is a member of the Decision Sciences Institute (DSI), the Institute for Operations Research and the Management Sciences (INFORMS), and the International Association for the Study of Information Systems for Crisis Response and Management (ISCRAM).
