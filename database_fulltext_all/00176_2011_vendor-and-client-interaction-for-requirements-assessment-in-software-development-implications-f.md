---
otero_id: 176
otero_key: "UBXCYKEY"
title: "Vendor and Client Interaction for Requirements Assessment in Software Development: Implications for Feedback Process"
authors: "Rajiv Jayanth; Varghese S. Jacob; Suresh Radhakrishnan"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1090.0248"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/UBXCYKEY/fulltext/images/bab4ffd81dc20940c851872c07a939f1c997f8b2f69b38867e781da3841cba98.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Vendor and Client Interaction for Requirements Assessment in Software Development: Implications for Feedback Process

Rajiv Jayanth, Varghese S. Jacob, Suresh Radhakrishnan,

Rajiv Jayanth, Varghese S. Jacob, Suresh Radhakrishnan, (2011) Vendor and Client Interaction for Requirements Assessment in Software Development: Implications for Feedback Process. Information Systems Research 22(2):289-305. http:// dx.doi.org/10.1287/isre.1090.0248

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/UBXCYKEY/fulltext/images/52bef2b9e15a8913755901e2bf93081499898cf180aab667f356be0a2a938ab6.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Vendor and Client Interaction for Requirements Assessment in Software Development: Implications for Feedback Process

Rajiv Jayanth, Varghese S. Jacob, Suresh Radhakrishnan School of Management, University of Texas at Dallas, Richardson, Texas 75080 {rajiv@utdallas.edu, vjacob@utdallas.edu, sradhakr@utdallas.edu}

W<sup>e</sup> <sup>study</sup> <sup>agency</sup> <sup>problems</sup> <sup>that</sup> <sup>arise</sup> <sup>when</sup> <sup>prototypes</sup> <sup>are</sup> <sup>used</sup> <sup>for</sup> <sup>requirements</sup> <sup>assessment.</sup> <sup>The</sup> <sup>precision</sup> with which the prototype helps a client assess his requirements depends on (a) the type of prototype provided by the vendor and (b) the client’s feedback effort. The vendor can provide either a neutral or nonneutral prototype: The nonneutral prototype influences the client towards one particular set of requirements that may not be the true requirement, and the neutral prototype allows the client to assess his true requirements. This leads to the vendor’s moral hazard problem. The client chooses to exert either the high or low feedback effort after the vendor provides the prototype. Because the effort is unobservable to the vendor, it can lead to the client exerting the low feedback effort: the client’s commitment problem. In this paper we develop and discuss the role of the contract payment to provide the vendor with incentives to supply the neutral prototype, as well as for the client to commit to the high feedback effort. In this setting, we also examine the “anchoring” effect, wherein even a high-feedback effort can influence the client more toward a particular set of requirements with the nonneutral prototype. Our results highlight the interplay among the feedback effort, anchoring, and vendor payments.

Key words: requirements assessment; anchoring; software prototyping; game theory; double moral hazard; incentives

History: Paulo Goes, Senior Editor; H. Raghav Rao, Associate Editor. This paper was received November 2, 2006, and was with the authors 14 months for 3 revisions. Published online in Articles in Advance January 27, 2010.

## 1. Introduction

Requirements assessment is a critical activity in software development. Improper requirements assessment has been suggested as a leading cause for information technology (IT) failures.<sup>1</sup> Ackoff (1967), Benbasat and Schroeder (1977), and Neumann and Jenkins (1982) emphasize that clients cannot completely prespecify their software requirements, i.e., software requirements are uncertain. Davis (1982) recommends mitigating such clients’ requirement uncertainty by processes such as prototyping. Prototyping and various advances in techniques for requirements assessment, conceptually rely on experimentation by the client, which in turn enables the client to assess, learn, and specify requirements.<sup>2</sup>

In a perfect world, the vendor (agent) delivers a prototype that allows the client (principal) to effectively assess and specify his requirements. In other words, if the client is unsure between two sets of requirements, experimenting with the prototype should enable the client to determine his true requirement. We call such a prototype the neutral prototype.<sup>3</sup> However, the vendor may choose to deliver a prototype that is geared towards influencing the client to a set of requirements that is easy for the vendor to deliver on, i.e., lower development costs for the vendor. We refer to this prototype as the nonneutral prototype. The set of requirements that the vendor pushes the client towards with a nonneutral prototype may not be the client’s true requirement:

the vendor’s moral hazard problem.<sup>4</sup> Thus, the nonneutral prototype influences the client towards one particular set of requirements that may not be the true requirement, and the neutral prototype provides information on the client’s true requirements.

The client receives the prototype, which is a black box, and experiments with it for determining his requirements. The ability to gather information on requirements depends on the prototype as well as the effort that the client puts into this process. As the goal of this process is to provide feedback on the requirements, we call this process the feedback process and the effort involved the feedback effort of the client. We assume that the client’s feedback effort is not observed by the vendor.<sup>5</sup> We define the “effectiveness” of the feedback effort as the probability that the client correctly identifies his true requirement when the vendor delivers the neutral prototype.<sup>6</sup> The client chooses to exert either the high- or the low-feedback effort after the vendor delivers the prototype. The sequence of the effort choice can potentially lead to the client’s commitment problem. We provide a sketch of the nature of the client’s commitment problem and discuss it in detail along with the analysis in §4.2.

Consider a standard principal-agent problem in which the vendor has to be provided adequate incentives to deliver the neutral prototype. Technically speaking, the payment to the vendor has to satisfy the incentive constraint. Furthermore, assume that the vendor is myopic in the sense that he only considers whether the payment satisfies his incentive constraint, i.e., if the incentive constraint is satisfied, the vendor will provide the neutral prototype. In this case, the client knowing that the vendor is myopic and hence has supplied the neutral prototype, will not find it beneficial to exert the high-feedback effort when the “effectiveness” of the feedback effort is small. The client is better off providing the lowfeedback effort, after he receives the neutral prototype. Can this be an equilibrium? The vendor can figure out from the contract that the client will provide the low-feedback effort if the neutral prototype is delivered. Noting that if the client exerts the lowfeedback effort, he is also more likely to identify a nonneutral prototype as neutral; the vendor’s payoff is higher if he provides a nonneutral prototype. Thus, considering a solution to the standard principal-agent problem with only the vendor’s incentive constraint is not an equilibrium. Thus, the commitment problem stems from the sequence in which the vendor’s choice of prototype and the client’s choice of feedback effort (high or low) occurs. We develop a model in which the client uses the payment to the vendor to commit ex ante that he will exert the high-feedback effort. As such, the vendor’s payment needs to also satisfy an incentive constraint for the client’s feedback effort. The commitment problem is represented as an additional constraint to the standard principal-agent problem that the vendor’s payment needs to satisfy.<sup>7</sup> If the vendor’s payment is obtained from the commitment constraint we refer to this as the commitment problem being more severe than the vendor’s moral hazard problem. On the other hand, if the vendor’s payment is obtained from the vendor’s moral hazard constraint we refer to this as the commitment problem being less severe than the vendor’s moral hazard problem.

For the client’s commitment problem to exist as described above the choice between high- and lowfeedback effort is necessary. Do client’s have a choice and, if yes, would they ever choose the low-feedback effort? Although intuition may suggest that the client will have sufficient incentive to exert the highfeedback effort, because otherwise he will “hurt” himself, empirical evidence indicates otherwise (Grudin 1991b, Wilson et al. 1997, Hunton and Beeler 1997, Davidson 1999, Elssamadisy and Schalliol 2002, Kohli and Devaraj 2004).<sup>8</sup> Organizational pressures such as budget or time constraints often preclude effective client participation. Commonly cited examples include reducing the time allocated for evaluating and providing feedback (Martin et al. 2004), reducing the resources needed (Wilson et al. 1997), reducing the number of participants involved (Wilson et al. 1997), or deploying surrogates i.e., individuals other than the actual users for providing feedback (Hunton et al. 1997, Davidson 1999, Elssamadisy et al. 2002, Kohli and Devaraj 2004). Thus, the client could invest a low feedback effort because of any of the aforementioned reasons.<sup>9</sup> This evidence suggests that client’s do not ex ante commit to high feedback effort: and of course, as discussed before, this in turn is likely to lead the vendor to provide the nonneutral prototype. Our objective is to examine how the contract is influenced when the client explicitly incorporates the commitment problem in the contract design.

To summarize, our setting incorporates the following features of requirements assessment using prototyping: (a) experimentation by the client to assess and learn his requirements, (b) the vendor’s moral hazard problem related to providing the neutral prototype, and (c) the client’s commitment problem to provide the appropriate feedback effort. We examine and provide insights into how the contract payments are influenced by the client’s commitment and the vendor’s moral hazard problems. We also incorporate the effect of anchoring in the feedback process (see Valusek and Fryback 1985).<sup>10</sup> In particular, improving the effectiveness of the feedback process (a) helps the client to assess his true requirements more precisely, if the vendor delivers the neutral prototype; and (b) makes the client get more influenced by the nonneutral prototype because of the anchoring effect.<sup>11</sup>

We show the client’s commitment problem is not an issue when the effectiveness of the feedback effort is sufficiently high. The intuition for this follows from the observation that the client finds it beneficial to exert the low-feedback effort, given that the vendor has supplied the neutral prototype only when the effectiveness of the feedback effort is small. In effect, the solution to the standard principal agent problem without considering the client’s commitment problem suffices when the effectiveness of the feedback effort is small.

It follows that the client’s commitment problem becomes less severe when the effectiveness of the feedback effort is sufficiently large. This in turn decreases the payments to the vendor resulting in an increase in the client’s profits. At higher levels of effectiveness of the feedback process, an increased effect of anchoring encourages the vendor to deliver the nonneutral prototype and influence the client. This leads to the vendor’s moral hazard problem becoming more severe than the client’s commitment problem. Thus, our results show that if higher effectiveness of the feedback process also leads to an increase in the anchoring effect, then the payment to the vendor increases with increases in the anchoring effect. This result highlights a potential cost of improving the feedback process in terms of externalities that it could impose through the anchoring effect.

## 2. Literature Review

Our study is related to two streams of literature: one that examines commitment problems, the other that examines double moral hazard problems.

## 2.1. Commitment Problem

Prior literature that examine the commitment problem are couched in either accounting information or supply chain management settings. Demski and Sappington (1993) examine the commitment problem of a buyer reporting the quality inspection of the supplier truthfully and show that making the item is preferable when the commitment problem is severe. Hwang et al. (2006) examine a supply chain with a supplier and buyer. The supplier’s quality effort is unobservable and the buyer cannot precommit to a specific inspection level, i.e., the agent’s moral hazard problem and the buyer’s commitment problem. They show that inspection leads to additional agency costs because of the presence of commitment problems, which provides a rationale for the movement away from inspections, even though the direct cost of inspection is low.

In accounting information settings, Arya et al. (1997) examine a principal-agent problem in which both the principal and the agent provide unobservable actions, and the principal cannot commit to a high effort. They examine the interaction between publicly available information and the commitment problem and show that the principal may prefer to have less information so as to alleviate the commitment problem. Arya et al. (1998) examine the principal’s commitment problem when the principal has to credibly commit not to intervene. They show that commitment problems can explain the phenomenon of earnings management. Arya et al. (2007) examine the principal’s commitment problem and show that it is neither necessary nor sufficient for signals that are more informative to be included in contracts, just because of their informativeness. As such, commitment problems generate insights above and beyond the standard principal-agent problems.

We extend these studies to software engineering settings. We do so by considering the anchoring effect in the context of software prototyping and generate insights into the feedback process as well as the contract payments.

## 2.2. Double Moral Hazard Problems

Commitment problems are a subset of the moral hazard problem where moral hazard is defined in a broad manner. Tirole (1999) defines moral hazard as, $^ { \prime \prime } \cdot \cdot$ 0 actions that are chosen by one party and unobserved to others.” Milgrom and Roberts (1992) defines it as, “Moral hazard is the form of post contractual opportunism that arises because actions that have efficiency consequences are not freely observable and so the person taking them may choose to pursue his or her private interests [emphasis added].” In our model also, similar to the double moral hazard setting, the client’s feedback effort and the vendor’s prototype choice are unobservable and uncontractible. However, in our setting the client’s feedback effort does not directly affect the vendor’s payoffs, but it influences the vendor’s behavior with respect to the prototype he chooses to deliver. As such, the commitment problem examined here is, broadly speaking, a double moral hazard problem, and thus we discuss some pertinent literature that examines double moral hazard. Baiman et al. (2000) examine penalties based on information from incoming inspections when the supplier’s design effort and the buyer’s appraisal effort are not observable, $\mathrm { i . e . , }$ a double moral hazard setting. They show that installing an information system that makes the buyer’s appraisal result contractible helps to improve product quality and the supplier’s design effort. Balachandran and Radhakrishnan (2005) examine a double moral hazard case when both the supplier’s and the buyer’s quality are not observable. They show that contract payments and penalties based on either information from incoming inspections or information from external failures induces first-best quality, and they examine whether the penalty satisfies the fairness criterion. These studies show the intricate effects of double moral hazard and incentive payments. In our model, we show that commitment problem also leads to intricate effects on incentive payments.

The rest of the paper is organized as follows: §3 develops the prototyping model, §4 analyzes the model and provides the results, §5 illustrates the main insights from the analyses with a numerical example, and §6 provides some concluding remarks.

## 3. Model

We examine a principal agent setting with the client as the principal and the vendor as the agent. The client’s requirements can either be $R _ { 1 }$ or $R _ { 2 } .$ . We let the client’s prior probability assessment that the requirement is $R _ { i }$ be $\theta _ { i }$ for $i = 1 , 2 ,$ i.e., initially, the client is not certain about his exact requirements. For example, consider a client wishing to implement an order processing system. The client may consider two alternative sets of requirements, one (referred to as $R _ { 1 } )$ in which the order processing is based on a segmentation of the customers using some measure of value, and two (referred to as $R _ { 2 } )$ in which the order processing is based on a first-come, first-served principle. Implementing the appropriate system could mean a much higher payoff for the client, as compared to the inappropriate system. However, the client may not know which of the two requirements best meets his or her needs. For this purpose, the client may ask the vendor to deliver a prototype to help assess which of the two is the correct requirement. The prior probability $\theta _ { i }$ depicts the client’s ex ante belief (priors) on the relative importance of the two sets of requirements. If $\theta _ { i } = 1$ , then the client is certain that his requirement is $R _ { i } ,$ if $\theta _ { i } = 0$ , then the client is certain that his requirement is not $R _ { i } ,$ i.e., his requirement is actually $R _ { - i }$ with certainty. Between these two extremes of cases when the client is certain about his requirements is the case $\theta _ { 1 } = \theta _ { 2 } = 0 . 5$ , wherein the client is completely fuzzy about his or her requirements. We assume $\theta _ { 1 } = \theta _ { 2 } = 0 . 5$ to emphasize the client’s uncertainty about his requirements.<sup>12</sup>

The client asks the vendor to provide a prototype that will enable him to assess his requirements. The vendor can choose to provide one of three prototypes $a \in \{ a _ { 1 } , a _ { 2 } , a _ { 3 } \} \colon$ : a nonneutral prototype $a _ { i }$ for $i = 1 , 2 ,$ geared to make the client believe that his requirement is $R _ { i } ,$ or a neutral prototype ${ a } _ { 3 } ,$ geared to help the client assess and learn his requirement. Thus, in our example, it is possible that the vendor may choose to provide a prototype that always shows segmentation is optimal (via incorrect logic or data manipulation, or otherwise). In other words the vendor can provide (a) a prototype that makes the client believe $R _ { 1 }$ is the true requirement, i.e., the nonneutral prototype, or (b) a prototype that correctly shows the relative differences between serving customers on the basis of segmentation and first come first serve, $\mathrm { i . e . , }$ a neutral prototype. In effect, whereas the neutral prototype $a _ { 3 }$ enables the client to learn his requirements, the vendor can “shirk” and deliver the nonneutral, prototype $a _ { 1 }$ or $a _ { 2 }$ that influences the client into assessing his or her requirements as $R _ { 1 }$ or $R _ { 2 } ,$ respectively. This aspect of how these prototypes can influence the client’s requirements assessment is made precise later in the section.<sup>13</sup> The vendor incurs a cost $v _ { k }$ for prototype ${ { a } _ { k } } ,$ where $k \in \{ 1 , 2 , 3 \}$ 9 and we assume that $v _ { 3 } > v _ { 1 }$ and $v _ { 3 } > v _ { 2 }$ . The prototypes $a _ { k }$ and the corresponding costs $v _ { k }$ are not jointly observable and contractible.

The client evaluates the prototype a by exerting feedback effort $b \in \{ b _ { H } , b _ { L } \}$ , with $b _ { H } > b _ { L }$ . That is, the client can exert the high feedback effort $b _ { H }$ or the low feedback effort $b _ { L }$ . Evaluation of the prototype provides the client with two signals: $f \in \{ \bar { f } _ { 1 } , f _ { 2 } \}$ and $g \in \{ g _ { 1 } , g _ { 2 } , g _ { 3 } \}$ . Signal $f$ provides noisy information on the client’s requirements with $f _ { i }$ corresponding to $R _ { i }$ for $i = 1 , 2$ . Signal $g$ provides noisy information on the vendor’s prototype with $g _ { k }$ corresponding to $a _ { k }$ for $k = 1 , 2 , 3$ . Both of these signals are jointly observable and contractible.

Signal $f$ provides information on the client’s requirement $\bar { R _ { j } } , \ j \in \{ 1 , 2 \}$ , with $\mathrm { P r o b } ( f _ { i } | a _ { k } , b _ { q } , R _ { j } ) = \delta _ { i k q j } ,$ when the vendor delivers the prototype $a _ { k }$ and the client exerts the feedback effort $b _ { q }$ where $q \in \{ H , L \}$ . The subscript j refers to the true requirement, and the subscript i refers to the inferred requirements. We assume that signal $f$ is informative, i.e., Prob $( f _ { i } | a _ { 3 } , b _ { H } , R _ { i } ) =$ $\delta _ { i 3 H i } > 0 . 5 $ Given the true requirement and the high feedback effort the neutral prototype enables the client to assess his requirement with a higher probability; the requirement is $R _ { i }$ and the signal obtained is $f _ { i } .$ . We also assume that if the client provides the low feedback effort $( b _ { L } )$ , then signal $\boldsymbol { \dot { f } }$ is not as informative, i.e., $\delta _ { i 3 H i } > \delta _ { i 3 L i }$ with $\delta _ { i 3 L i } = \beta \delta _ { i 3 H i }$ and $\beta < 1$ . Thus, the high-feedback effort of the client enables the client to assess and learn his requirement more precisely than the low feedback effort but is not perfect. The difference between $\delta _ { i 3 H i }$ and $\delta _ { i 3 L i }$ reflects the effectiveness of the high-feedback effort.

As mentioned earlier, the vendor can shirk and deliver prototype $\{ a _ { 1 } , a _ { 2 } \}$ and influence the client into believing that his requirements are $\{ R _ { 1 } , R _ { 2 } \} ,$ respectively. If the vendor provides prototype $a _ { i }$ and the client exerts the high feedback effort $b _ { H } ,$ then Prob $( f _ { i } \mid a _ { i } , b _ { H } , R _ { j } ) = \delta _ { i i H j } > \delta _ { j 3 H j }$ for any $i , j = 1 , 2$ This captures the crux of the anchoring theory in requirements determination (Valusek and Fryback 1985): the prototype serves as an anchor point for the client to establish his requirements. When the vendor delivers prototype $a _ { i } , i = 1 , 2$ , the client makes prototype $a _ { i }$ his anchor and is more likely to observe signal $\bar { \ b { f } } _ { i }$ and establish his requirement as $R _ { i }$ . Correspondingly, when the client exerts low feedback effort and the vendor delivers prototype $a _ { i } , i = 1 , 2$ , then the client is completely influenced by the nonneutral prototype, i.e., Pro $\begin{array} { r } { \gamma ( \bar { f } _ { i } \mid a _ { i } , b _ { L } , R _ { j } ) = \mathbf { \bar { \delta } } _ { i i L j } = 1 } \end{array}$ for any $\hat { i } , j = \hat { 1 , 2 }$ . In essence, the effectiveness of the feedback effort is lower with the nonneutral prototype.<sup>14</sup>

Note that the anchoring effect is captured by two characteristics: one, signal $f$ is influenced by prototype $a _ { i }$ that is delivered independent of the true requirement $R _ { j }$ and, two, $\bar { \delta } _ { i i H j } \bar { > } \bar { \delta } _ { j 3 H j } ,$ showing that the assessment of the requirement is influenced by the prototype. We let $\delta _ { i i H j } \bar { = } \phi \delta _ { j 3 H j }$ with $\phi > 1$ and consider the domain of $\delta _ { \it { i 3 H j } }$ such that $\delta _ { i i H j } < 1$

When the vendor delivers prototype $a _ { k } , k \in \{ 1 , 2 , 3 \}$ and the client exerts high-feedback effort $b _ { H } ,$ then Prob $( g _ { k } \mid a _ { k } , b _ { H } ) = \alpha _ { 1 } > 0 . 5$ for $k = 1 , 2 , 3$ and Prob $( g _ { k ^ { \prime } } | a _ { k } , b _ { H } ) = ( 1 - \alpha _ { 1 } ) / 2$ for $k , k ^ { \prime } \in \left\{ 1 , 2 , 3 \right\}$ with $k \neq k ^ { \prime }$ . Furthermore, we let Prob $( g _ { 3 } \mid a _ { k } , b _ { L } ) = 1$ . In effect, the information with respect to the prototype that the vendor delivers is informative about the prototype when the client exerts the high effort and is not informative when the client exerts the low effort. However, the information is not perfect, $\mathrm { i . e . , }$ if the vendor delivers prototype $a _ { 1 }$ or $a _ { 2 }$ and the client exerts high effort $b _ { H } ,$ the client may misidentify the prototype as $a _ { 3 }$ with probability $( 1 - \alpha _ { 1 } ) / 2 .$ 15

The vendor is paid $W \in \{ W _ { 1 } , W _ { 2 } , W _ { 3 } \}$ corresponding to signals $g _ { 1 } , g _ { 2 } , g _ { 3 }$ . Signal $g$ is observed during a postsystem audit such as an acceptance test, i.e., when the system is tested by the client to ensure that it satisfies the business needs (Dennis et al. 2002). The performance of the system at this stage is informative of the vendor’s actions at the prototyping phase. Thus, the signals $f , g$ and the payment scheme $\mathsf { \bar { W } } \in \{ W _ { 1 } , W _ { 2 } , W _ { 3 } \}$ are intended to capture the learning and monitoring roles of the client’s action. When the vendor supplies prototype $a _ { k } , k \in \{ 1 , 2 , 3 \}$ , and the client identifies his requirements as $R _ { i } , i \in \{ 1 , 2 \}$ , the vendor incurs a cost $c _ { k i }$ to develop the end system. When the vendor supplies the nonneutral prototype $a _ { i }$ for $i \in \{ 1 , 2 \}$ and the client establishes his requirements as $R _ { i } ,$ the “experience effect” from designing $a _ { i }$ aids the vendor to implement the end system, thus the vendor’s cost of implementation $( c _ { i i } )$ is small. On the other hand, this experience effect is much reduced when the vendor delivers the neutral prototype, ${ a } _ { 3 } ,$ hence, $c _ { 3 1 } > c _ { 1 1 }$ . The “learning effect” is substantially reduced when the vendor delivers $a _ { i }$ but is asked to implement the system as per $R _ { j } , i \neq j ,$ , or vice-versa. Hence, we let, $c _ { 1 1 } < c _ { 3 1 } < c _ { 1 2 }$ and $c _ { 2 2 } < c _ { 3 2 } < c _ { 2 1 }$

Table 1 Summary of the Key Variables

<table><tr><td>Variable</td><td>Summary</td></tr><tr><td> $R_{i} \in \{R_{1}, R_{2}\}$ </td><td>The client&#x27;s state of requirements</td></tr><tr><td> $\theta_{i} \in \{\theta_{1}, \theta_{2}\}$ </td><td>The prior belief (probability) that the true requirement is  $R_{i}$ </td></tr><tr><td> $a \in \{a_{1}, a_{2}, a_{3}\}$ </td><td>The type of prototype delivered;  $\{a_{1}, a_{2}\}$ : nonneutral prototypes;  $\{a_{3}\}$ : neutral prototype</td></tr><tr><td> $b \in \{b_{H}, b_{L}\}$ </td><td>Client&#x27;s feedback effort {high, low}</td></tr><tr><td> $f \in \{f_{1}, f_{2}\}$ </td><td>A signal which provides noisy information on the requirements; signal  $f_{i}$  corresponds to requirement  $R_{i}$ </td></tr><tr><td> $g \in \{g_{1}, g_{2}, g_{3}\}$ </td><td>A signal which provides noisy information on the vendor&#x27;s prototype with  $g_{k}$  corresponding to  $a_{k}$  for  $k = 1, 2, 3$ </td></tr><tr><td> $\delta_{ikqj}$ </td><td>The conditional probability  $\text{Prob}(f_{i} \mid a_{k}, b_{q}, R_{j})$ </td></tr><tr><td> $\phi$ </td><td>Anchoring factor:  $\delta_{iiHj} = \phi \delta_{j3Hj}, \phi > 1$ </td></tr><tr><td> $\alpha_{1}$ </td><td>The conditional probability:  $\text{Prob}(g_{k} \mid a_{k}, b_{H})$ </td></tr><tr><td> $W \in \{W_{1}, W_{2}, W_{3}\}$ </td><td>The vendor&#x27;s compensation scheme</td></tr><tr><td> $c_{ki}$ </td><td>The vendor&#x27;s implementation cost when prototype  $a_{k}$  is delivered and  $R_{i}$  is established as the true requirements</td></tr><tr><td> $v \in \{v_{1}, v_{2}, v_{3}\}$ </td><td>The cost of developing prototypes  $\{a_{1}, a_{2}, a_{3}\}$ </td></tr><tr><td> $x_{ij}$ </td><td>The client&#x27;s payoff when the true requirement is  $R_{i}$  and the client establishes  $R_{j}$  as the system requirement for all  $i, j \in \{1, 2\}$ </td></tr><tr><td> $\overline{H}$ </td><td>The vendor&#x27;s reservation profit</td></tr></table>

The client gets a benefit of $x _ { i j }$ when his true requirement is $R _ { i }$ and he establishes $R _ { j }$ as his system requirement for all $i , j \in \{ 1 , 2 \} . ^ { 1 6 }$ To keep the analysis simple, we let profits and costs for requirements $R _ { 1 }$ and $R _ { 2 }$ be symmetric: $x _ { 1 1 } = x _ { 2 2 } , x _ { 1 2 } = x _ { 2 1 } , c _ { 1 1 } = c _ { 2 2 } , c _ { 1 2 } = c _ { 2 1 } ,$ and $v _ { 1 } = v _ { 2 } . ^ { 1 7 }$ The vendor’s reservation profit is denoted H<sup>±</sup>: without loss of generality we let $\overline { { H } } = 0$

Table 1 provides a glossary of notation. We now proceed to analyze the model.

## 4. Analysis

4.1. Benchmark Setting: No Prototyping Regime Before proceeding to analyze the setting where the client uses the prototyping method, we examine a benchmark setting where no prototypes are developed. That is, the client directs the vendor to deliver the end system as per a particular requirement $R _ { j } .$ . In this case, we assume that the vendor incurs a cost $C _ { j }$ to implement a system, meeting requirements $R _ { j } .$ We also assume that the client can precisely verify whether the vendor provided the end system as per requirement $R _ { j } .$ In effect, there are no unobservability concerns. This is similar to the client exerting the low feedback effort and the vendor being required to deliver the end system as per requirement $R _ { j }$ in the prototyping regime. Thus, $\bar { C _ { j } } = c _ { j j } \bar { + } v _ { j } . ^ { 1 8 }$ The client pays the vendor $W _ { j }$ when $R _ { j }$ is specified as the requirement. The expected profit (U 5 for the client is

$$
U (R _ {j}) = \sum_ {i \in \{1, 2 \}} x _ {i j} \theta_ {i} - W _ {j}.\tag{UR}
$$

The vendor’s profit (V 5 is given by

$$
V (R _ {j}) = W _ {j} - C _ {j}.\tag{VR}
$$

For any requirement $R _ { j }$ , the client’s problem is given by

## Program 1

$$
\max _ {W _ {j}} U (R _ {j})\tag{OBJ-1}
$$

$$
\text { subject   to } V (R _ {j}) \geq \bar {H} = 0.\tag{IR-1}
$$

The objective function (OBJ-1) of Program 1 represents the client’s objective of maximizing expected profits. Equation (IR-1) is the participation constraint, which ensures that the contract payment to the vendor at least meets his reservation profit.

The solution to Program 1 is characterized below.<sup>19</sup>

<sup>Solution</sup> <sup>1.</sup> The solution to Program 1 is given by $W _ { j } ^ { N } = C _ { j }$ and $\begin{array} { r } { U ^ { N } ( R _ { j } ) = \sum _ { i \in \{ 1 , 2 \} } x _ { i j } \theta _ { i } - C _ { j } } \end{array}$

The solution of Program 1 is such that the vendor is paid the development costs (plus the reservation profits). This provides a benchmark for prototyping because if the client’s expected profit in this benchmark setting provided in Solution 1 is greater than that obtained with prototyping, then the client would not choose the prototyping method.

We now proceed to examine the prototyping regime.

## 4.2. The Prototyping Regime

The sequence of events unfolds as follows.

1. The client chooses the prototyping method or has the vendor directly implement the end system.

2. The client designs the incentive contract, W .

3. If the client chooses the prototyping method, the vendor chooses the type of prototype a to be developed and delivers it.

4. If the client chooses the prototyping method, the client exerts feedback effort $b ,$ observes signal $f ,$ and specifies the requirements for the end system.<sup>20</sup>

5. The vendor delivers the end system. The client observes signal $g$ and pays W to the vendor.

6. The client deploys the end system, derives benefit, x.

Figure 1 depicts a game tree for the prototyping regime.

The client has the vendor provide the neutral prototype, $a _ { 3 }$ to assess his requirement. The expected profit (U 5 for the client is given by

$$
\begin{array}{c} U (a, b, W) = \sum_ {i, j \in \{1, 2 \}} x _ {i j} \text {Prob} (f _ {i} \mid a, b, R _ {i}) \theta_ {i} \\ - \sum_ {k \in \{1, 2, 3 \}} W _ {k} \text {Prob} (g _ {K} \mid a, b) - b. \end{array}\tag{UPR}
$$

The client gets a payoff $x _ { i j }$ when his true requirement is $R _ { i }$ and he establishes $R _ { j }$ as his requirement by observing the signal $f _ { j }$ for all $i , \stackrel { \prime } { j } \in \{ 1 , 2 \}$ . The expected revenue is obtained by multiplying the payoff term $x _ { i j }$ with the probability of realizing $x _ { i j }$ , i.e., the probability of observing $\check { f } _ { j }$ when the true requirement is $R _ { i }$ 2 Prob $( f _ { i } \mid a , b , R _ { i } ) \bar { \theta _ { i } }$ for all $i , j \in \{ 1 , 2 \}$ . The expected payment to the vendor is obtained by multiplying the payment $W _ { k }$ with the probability of making a payment $W _ { k }$ which is the probability of observing the signal $g _ { k }$ for all $k \in \{ 1 , 2 , 3 \}$ 9.

The expected profit for the vendor (V 5 is given by

$$
\begin{array}{c} V (a, b, W) = \sum_ {k \in \{1, 2, 3 \}} W _ {k} \text {Prob} (g _ {K} \mid a, b) - v (a) \\ - \sum_ {i, j \in \{1, 2 \}} C _ {k j} \text {Prob} (f _ {j} \mid a _ {k}, b). \end{array}\tag{VPR) \( ^{21} \}
$$

Where Prob $\textstyle ( f _ { j } \mid a _ { k } , b ) = \sum _ { i \in \{ 1 , 2 \} } \operatorname { P r o b } ( f _ { j } \mid a _ { k } , b , R _ { i } ) \theta _ { i }$ The expected cost of making the end system is obtained by multiplying the cost of development $c _ { k j }$ when prototype $a _ { k }$ was delivered with the probability of identifying the requirement as $R _ { j } \colon \operatorname { P r o b } ( f _ { j } \mid a _ { k } , b ) { \\dot { \theta } }$ for all $i , j \in \{ 1 , 2 \}$

We examine the case where the client requires the vendor to provide the neutral prototype, ${ a } _ { 3 } ,$ and the client exerts high feedback effort, $b _ { H } .$ Settings in which a client requires the vendor to deliver $a _ { 1 }$ and $a _ { 2 }$ imply that the client does not want to $\prime \mathrm { { 1 e a r n ^ { \prime \prime } } }$ about his requirements $( \mathrm { i . e . }$ , knows his requirements) and prototyping for requirements discovery is moot. So we do not model these cases. If the client does not exert the high-feedback effort, then based on the assumption that Prob $( g _ { 3 } \mid a _ { j } , b _ { L } ) = 1$ , the vendor will never provide the neutral prototype and, hence, the idea behind prototyping is again moot. Consequently, we examine the client’s problem of designing the contract and vendor payments when the client implements $( a _ { 3 } , b _ { H } ) . ^ { 2 1 }$ The optimization problem is provided in the following program.

## Program 2

$$
\max _ {W _ {k}} U (a _ {3}, b _ {H}, W)\tag{OBJ-PR}
$$

subject to ${ \cal V } ( a _ { 3 } , b _ { H } , W ) \geq \overline { { { \cal H } } } = 0 ,$

(IR-PR)

$$
V (a _ {3}, b _ {H}, W) \geq V (a _ {1}, b _ {H}, W),\tag{ICV1-PR}
$$

$$
V (a _ {3}, b _ {H}, W) \geq V (a _ {2}, b _ {H}, W),\tag{ICV2-PR}
$$

$$
U (a _ {3}, b _ {H}, W) \geq U (a _ {3}, b _ {L}, W).\tag{ICC-PR}
$$

The individual rationality constraint (IR-PR) ensures that the vendor is paid his reservation profit H<sup>±</sup>. Constraints (ICV1-PR) and (ICV2-PR) are the incentive compatibility constraints with respect to the vendor’s prototype: the client designs the payment to the vendor to induce $a _ { 3 }$ and not $a _ { 1 }$ or $a _ { 2 } .$ . Constraint (ICC-PR) is the incentive compatibility constraint with respect to the client: the constraint ensures that the client chooses $b _ { H }$ over $b _ { L }$ when the vendor delivers the neutral prototype, ${ a _ { 3 } } . ^ { 2 2 }$ The choice of the prototype to deliver $( a _ { 1 } , a _ { 2 }$ or ${ a } _ { 3 } )$ is made by the vendor and is unobservable by the client; the choice of the feedback effort $( b _ { H } , b _ { L } )$ is made by the client and is unobservable by the vendor. In Program 2, the moral hazard problem of the vendor and the commitment problem of the client are characterized by the incentive compatibility constraints for the vendor and the client, respectively.

Figure 1 Game Tree for the Prototyping Regime  
![](/api/attachments/UBXCYKEY/fulltext/images/e1cf9a249369d72f3c0559274a50517613dcc0b7ed214797f02919897f8f1bfa.jpg)

4.2.1. The Client’s Commitment Problem: Explaining Constraint (ICC-PR). We illustrate the client’s commitment problem with the help of a numerical example. Consider the solution to the problem without constraint (ICC-PR). This is similar to the solution for the standard principal-agent problem: we refer to this program as Program 2S (“S” refers to the standard principal-agent problem). The implicit assumption in Program 2S is that the vendor is only concerned about his own incentives, i.e., the vendor is myopic and, correspondingly, the client also knows that the vendor is myopic. For the illustration consider the following parameter values: $x _ { 1 1 } =$ $1 , 0 0 0 , \ x _ { 1 2 } = 0 , \ b _ { H } = 5 0 . 0 , \ b _ { L } = 0 , \ v _ { 1 } = 0 , \ v _ { 2 } = 0 , \ v _ { 3 } =$ $1 0 5 . 0 , c _ { 1 1 } = c _ { 2 2 } = 5 , c _ { 3 1 } = c _ { 3 2 } = 1 0 , c _ { 1 2 } = c _ { 2 1 } = 1 1 , \beta =$ 00994, <sub>i3Hi</sub> = 0051,  = 1007, and $\alpha _ { 1 } = 0 . 8 .$ 0 It is easy to see that $W _ { 1 } = W _ { 2 } = 0$ is optimum. If constraint (IR-PR) is binding then $W _ { 3 }$ needs to be at least \$143075 6= 4105 + 105/0087. If (ICV-PR) is binding $W _ { 3 }$ needs to be at least \$184.92. Thus, the solution to Program 2S is $W _ { 1 } = 0 , ~ W _ { 2 } = 0 , ~ W _ { 3 } = \ S 1 8 4 . 9 2$ . The contract payment satisfies the vendor’s incentive constraint, and the vendor obtains information rents: the expected payment is greater than the reservation payment.

The client knows that the myopic vendor will supply the neutral prototype. Given that the neutral prototype is delivered, the client evaluates his expected profits for the high- and low-feedback efforts. The client’s profit if he exerts the high-feedback effort is given by $\stackrel { \triangledown } { U } ( a _ { 3 } , b _ { H } , W ) = x _ { 1 1 } \delta _ { j 3 H j } - \stackrel { \smile } { \alpha } _ { 1 } W _ { 3 } - b _ { H } = \$ 3 1 2 . 06 ;$ and, if he exerts the low-feedback effort, his or her profit is given by $U ( a _ { 3 } , b _ { L } , W ) = x _ { 1 1 } \beta \delta _ { i 3 H j } - \alpha _ { 1 } W _ { 3 } = \ S 3 5 9 . 0 1$ Thus, in this case $U ( a _ { 3 } , b _ { L } , W ) > \dot { U } ( a _ { 3 } , b _ { H } , W )$ 5 i.e., the client finds it beneficial to exert the low-feedback effort, once the neutral prototype is delivered.<sup>23</sup> The client is rational and will choose the low-feedback effort.

We now build on this example to show how the solution to Program S2 cannot be sustained in equilibrium. For this we now consider a rational vendor who is presented with a contract of $W _ { 1 } = 0 , W _ { 2 } = 0 , W _ { 3 } =$ \$184092, i.e., the solution to Program S2. This contract does not satisfy (ICC-PR), and the vendor can also verify this. So the vendor knows that the client will not exert the high-feedback effort after the prototype is delivered because $U ( a _ { 3 } , b _ { L } , W ) > U ( a _ { 3 } , \bar { b _ { H } } , W )$ The vendors’ profit if the neutral prototype is delivered and the client exerts the low-feedback effort is given by $V ( a _ { 3 } , b _ { L } , W ) = 6 9 . 9 2 \ [ = 1 8 4 . 9 2 - 1 1 5 ]$ , where we have used the assumption that the client’s lowfeedback effort results in signal g always indicating a neutral prototype. The vendor’s profit if the client exerts the low-feedback effort when he supplies $a _ { 2 }$ is given by $V ( a _ { 2 } , b _ { L } , W ) = 1 7 9 . 9 2 \ [ = 1 8 4 . 9 2 - \mathrm { \stackrel { . } { 5 } } ]$ . Thus, $V ( a _ { 3 } , b _ { L } , W ) < V ( a _ { 2 } , b _ { L } , W )$ . Hence, the vendor will supply the nonneutral prototype, and thus the purpose of providing incentives to the vendor for the neutral prototype is in vain. In other words, the solution to the standard principal agent problem Program 2S (i.e., Program 2 without considering constraint (ICC-PR)) can break down in this setting: there is no equilibrium.

The example illustrates that the solution to the standard principal-agent model is not enough to motivate the desired vendor action. The constraint (ICC-PR) is the incentive constraint of the client that addresses the client’s commitment problem. Given that the mechanism for the client to commit to highfeedback effort is the vendor’s payment, the constraint requires the vendor’s payment to be such that the client finds it optimal to choose the high-feedback effort after the vendor has chosen the neutral prototype. This constraint is similar to the principal’s incentive constraints in Hwang et al. (2006) and Arya et al. (1997).<sup>24</sup> Similar to these studies, the client cannot commit to provide the high-feedback effort, and, hence, constraint (ICC-PR) is required. Empirical evidence discussed in the introduction suggests that the client’s participation in requirements assessment can be low (Grudin 1991b, Wilson et al. 1997, Hunton and Beeler 1997, Davidson 1999, Elssamadisy and Schalliol 2002, Kohli and Devaraj 2004). This indicates that the client is unable to ex ante commit to feedback effort.

Overall, Program 2 represents the client’s problem of designing contract payments in such a way that it not only ensures that the vendor delivers the neutral prototype, but the client also commits to the high feedback effort. The myriad of examples and empirical evidence in software engineering suggests that there does not appear to be other commitment mechanisms. For instance, a simple commitment mechanism is for the client and vendor to identify the client’s personnel who will be appropriate for the feedback process at the time of contracting. However, doing so requires that all contingencies like employee attrition, penalties and rewards for not deploying, or deploying the agreed personnel must be detailed in the contract. Although this may not be impossible, it is difficult. This incompleteness in contracting with respect to commitment parameters leads to the question of whether the contract payment schedule can be used to credibly commit to the client’s feedback action. In essence, given the empirical evidence and examples of lack of commitment by the client we assume that contracts are incomplete in the sense that the feedback process is not completely defined.

4.2.2. The Solution to Program 2. Before, we proceed to characterize the solution to Program 2 we make some technical assumptions. These assumptions ensure that the solution to Program 2 has a feasible solution where problems attributable to unobservability of efforts, i.e., the vendor’s moral hazard problem and the client’s commitment problems, are sufficiently severe. In other words, the assumptions are sufficient to ensure that the incentive problem of inducing the vendor to provide the neutral prototype and the client to provide the high-feedback effort is nontrivial. Our objective is to provide insights into how unobservability of efforts can affect incentives. These assumptions are sufficient to ensure that we examine the parameter region, in which incentive concerns are present so as to gain meaningful insights.<sup>25</sup> The technical assumptions are provided below.

$$
\begin{array}{c} \text {A1:} [ c _ {3 1} + v _ {3} ] / (c _ {1 1} \delta_ {i i H j} + c _ {1 2} (1 - \delta_ {i i H j}) + v _ {1}) \geq \\ [ 2 \alpha_ {1} ] / (1 - \alpha_ {1}); \end{array}
$$

$$
\begin{array}{l} \text {A2:} \alpha_ {1} (b _ {H} - b _ {L}) > (x _ {1 1} - x _ {1 2}) (\delta_ {j 3 H j} - \delta_ {j 3 L j}) \alpha_ {1} + \\ (c _ {3 1} + v _ {3}) (1 - \alpha_ {1}); \end{array}
$$

$$
\begin{array}{l} \text { A3: } (1 / 2) (x _ {1 1} - x _ {1 2}) \alpha_ {1} (1 - \beta) > (b _ {H} - \alpha_ {1} b _ {L}) - \\ (c _ {1 1} + v _ {1}) (1 - \alpha_ {1}); \end{array}
$$

$$
\text { A4: } (x _ {1 1} - x _ {1 2}) \gg (c _ {1 2} - c _ {1 1}).
$$

Assumptions A1 and A2 ensure that the agency issues of unobservability of effort are sufficiently severe. Assumption A1 requires that the ratio of the expected cost of providing the neutral prototype to the nonneutral prototype be greater than the ratio of the effectiveness of signal g, i.e., ratio of the signal correctly identifying the neutral prototype to the signal misidentifying nonneutral prototypes as a neutral prototype. Similarly, A2 ensures that the client’s commitment problem of choosing the high-feedback effort is sufficiently severe.<sup>26</sup> Assumptions A3 and A4 require that the difference in benefits from getting the requirements correct versus incorrect is sufficiently high, such that the no prototyping regime is not the preferred regime. These assumptions define the domain over which the incentive problem is interesting, i.e., the incentive constraints are binding.

The solution to Program 2 is provided in Solution 2.

<sup>Solution</sup> <sup>2.</sup> Under assumptions A1–A4, the solution to Program 2 depends on condition (C1);

$$
\delta_ {j 3 H j} \leq \frac {(b _ {H} - b _ {L}) X + (c _ {1 2} + v _ {1} - c _ {3 1} - v _ {3}) (1 - \alpha_ {1})}{(x _ {1 1} - x _ {1 2}) (1 - \beta) X + (c _ {1 2} - c _ {1 1}) \phi (1 - \alpha_ {1})},\tag{C1}
$$

where $X = ( 3 \alpha _ { 1 } - 1 ) / 2 .$

If (C1) is satisfied, the solution to Program 2 is given by

$$
\begin{array}{c} W _ {1} ^ {*} = 0, \quad W _ {2} ^ {*} = 0, \\ W _ {3} ^ {*} = [ (b _ {H} - b _ {L}) - (x _ {1 1} - x _ {1 2}) (1 - \beta) \delta_ {j 3 H j} ] / (1 - \alpha_ {1}), \end{array}
$$

$$
\begin{array}{c} {U ^ {*} (a _ {3}, b _ {H}) = x _ {1 1} \delta_ {j 3 H j} + x _ {1 2} (1 - \delta_ {j 3 H j}) - \alpha_ {1} W _ {3} ^ {*} - b _ {H},} \\ {V ^ {*} (a _ {3}, b _ {H}) = \alpha_ {1} W _ {3} ^ {*} - c _ {3 1} - v _ {3}.} \end{array}
$$

If (C1) is not satisfied, the solution to Program 2 is given by

$$
\begin{array}{c} {W _ {1} ^ {* *} = 0, \quad W _ {2} ^ {* *} = 0,} \\ {W _ {3} ^ {* *} = [ (c _ {3 1} + v _ {3}) - (c _ {1 2} + v _ {1} + (c _ {1 2} - c _ {1 1}) \delta_ {j 3 H j} \phi ] / X,} \\ {U ^ {* *} (a _ {3}, b _ {H}) = x _ {1 1} \delta_ {j 3 H j} + x _ {1 2} (1 - \delta_ {j 3 H j}) - \alpha_ {1} W _ {3} ^ {* *} - b _ {H},} \\ {V ^ {*} (a _ {3}, b _ {H}) = \alpha_ {1} W _ {3} ^ {* *} - c _ {3 1} - v _ {3}.} \end{array}
$$

Solution 2 characterizes the whole domain over which both the vendor’s agency problem and the client’s commitment problems can occur. This is governed by which incentive constraint binds and which incentive constraint is slack. When the solution has the incentive constraint of the vendor binding and the incentive constraint of the client slack, we say that the vendor’s moral hazard problem is more severe, and vice versa. If the marginal benefit of exerting the high feedback effort, i.e., $\bar { ( } x _ { 1 1 } - x _ { 1 2 } ) ( \delta _ { j 3 H j } - \delta _ { j 3 L j } \bar { ) }$ is small (this happens when condition (C1) is satisfied), constraint (ICC-PR) is binding, and thus the client’s commitment problem becomes severe.<sup>27</sup> Hence, when the effectiveness of feedback effort is small, the client’s commitment problem is severe.

When we consider the earlier numerical example and solve Program 2, we find the (ICC-PR) constraint is binding (i.e., the client’s commitment problem is found to be severe) and obtain the following solution, $W _ { 1 } = 0 , W _ { 2 } = 0 , W _ { 3 } = \ S 2 3 4 . 7$ . In particular, note that the client’s expected profit, when he exerts the high and low feedback efforts are \$272.24: the client is now indifferent between choosing the high- or lowfeedback effort. By making himself indifferent to the high- and low-feedback effort, the client “credibly” signals his commitment to exert the high-feedback effort. The client commits to the high feedback effort by paying the vendor a higher amount made precise in Solution 2. In essence, the client gives up the marginal benefit of shirking to sustain the vendor’s choice of the neutral prototype. With such a payment scheme, the client chooses the high-feedback effort, the vendor delivers the neutral prototype, and the desired equilibrium is sustained.

4.2.3. Comparison of Prototyping and No Prototyping Regimes. To analyze Solution 2 and provide insights into how the feedback process (which determines the true requirements) and the evaluation process (which determines the type of the prototype)

affects the vendor payments and the client’s profits, we establish the parameter region over which the client chooses the prototype regime optimally. This is stated as an observation.

<sup>Observation.</sup> Under assumptions A1–A4 the client prefers the prototyping regime in which the vendor supplies the neutral prototype and the client exerts the high-feedback effort to the no prototyping regime.

The observation compares the profits in Solution 2 with that of Solution 1. By choosing the prototyping regime, the client increases the probability of correctly identifying his true requirements $R _ { j }$ from the initial prior $\theta _ { j } = 0 . 5$ to $\bar { \delta } _ { j 3 H j } > 0 . 5$ . The benefit for the client arises from assessing and learning about his requirement. The increased cost arises because of agency costs associated with moral hazard problems: specifically, the vendor is paid an amount over and above his reservation profit, i.e., the vendor commands rent. Observation 1 shows that there exist parameter regions over which the prototyping regime provides the client with profits that are higher than that of the no prototyping regime.

We proceed to analyze the solution of the prototyping regime to gain insights into the effect of the feedback process and the effectiveness of the signal with respect to the prototypes.

4.2.4. Impact of the Effectiveness of the Feedback Process. The effectiveness of the feedback process is given by Prob $( f _ { j } \mid a _ { 3 } , b _ { H } , R _ { j } ) = \delta _ { j 3 H j }$ , which is the probability that the client correctly identifies his true requirements when the vendor delivers the neutral prototype and the client exerts high-feedback effort. A large (small) value of $\delta _ { j 3 H j }$ is suggestive of a more (less) effective feedback process, i.e., the true requirements are more (less) likely to be identified correctly. Examples of a less effective feedback process include assigning fewer resources or allocating lesser time or deploying surrogates in the feedback process. The impact of increased effectiveness of the feedback process in the presence of anchoring is made precise by the following proposition.

<sup>Proposition</sup> <sup>1.</sup> (i) The payment to vendor $( W _ { 3 } )$ decreases, the profit of the vendor (V ) decreases, and the profit of the client (U) increases with increasing effectiveness of the feedback process $( \delta _ { j 3 H j } ) f o r$ low $\delta _ { \it { i 3 H j } }$ . Technically, if (C1) is satisfied, then d $W _ { 3 } ^ { * } / d \delta _ { j 3 H j } < 0 , \stackrel { \prime } { d } V ^ { * } ( a _ { 3 } , b _ { H } ) / d \bar { \delta } _ { j 3 H j } < 0 ,$ and $d \bar { U } ^ { * } ( a _ { 3 } , b _ { H } ) / d \bar { \delta _ { i 3 H j } } > 0 .$

(ii) The payment to vendor (W ) increases, the profit of the vendor (V ) increases, and the profit of the client (U) increases with increasing effectiveness of the feedback process $( \delta _ { j 3 H j } )$ for large $\delta _ { j 3 H j }$ . Technically, if (C1) is not satisfied, then $d W _ { 3 } ^ { * * } / \bar { d } \delta _ { j 3 H j } ^ { \phantom { * } } > 0 , d V ^ { * } ( a _ { 3 } ^ { \phantom { * } } , b _ { H } ^ { \phantom { * } } ) / d \delta _ { j 3 H j } > 0 .$ , and $d U ^ { * * } ( a _ { 3 } , b _ { H } ) / \bar { d } \delta _ { j 3 H j } > 0$

Proposition 1 shows the impact of a higher effectiveness of the feedback process in the prototyping regime. A higher effectiveness of the feedback process decreases the payments made to the vendor and correspondingly decreases the vendor’s profits and increases the client’s profits up until a point (see Equation (C1)). This effect is observed because, at a higher effectiveness of the feedback process $( \delta _ { j 3 H j } ) ,$ the marginal benefit of exerting the higher effort $( x _ { 1 1 } - x _ { 1 2 } ) ( \delta _ { j 3 H j } - \delta _ { j 3 L j } )$ is also higher. In essence, the client enjoys stronger incentives to invest the high effort and the commitment problem becomes less severe. Thus, the payment (role of which is to motivate the high-feedback effort and alleviate the commitment problem) decreases as a consequence. Beyond a point (given by (C1)), the payments to the vendor increase and the vendor’s profits increase, but the client’s profits also increase. This is because when the effectiveness of the feedback process is high $( \delta _ { j 3 H j }$ is high), $\delta _ { i i H j } ,$ the probability that the client determines his requirement as $R _ { i }$ when the vendor delivers $a _ { i } , i \in \{ 1 , 2 \}$ , and the client exerts the high-effort $b _ { H } ,$ is also high (because $\delta _ { i i H j } \geq \delta _ { j 3 H j } )$ Thus, as the feedback process becomes more effective, the benefit for the vendor in choosing a nonneutral prototype also increases. The benefit for the vendor increases because the vendor can influence the client’s requirements more effectively by providing a nonneutral prototype: the vendor’s moral hazard problem becomes more severe. One may find it difficult to imagine skilled personnel succumbing to the anchoring effect, but since Tversky and Kahneman (1974) demonstrated the anchoring effect using novice subjects, studies have replicated their results using “experts” or “experienced” subjects (see, for example, Joyce and Biddle 1979, Northcraft et al. 1987, and Aranda and Easterbrook 2005). In the context of our example on customer segmentation, it is possible that even though skilled personnel are assigned to the feedback process, they might be enamored by the idea of segmentation, but the segments themselves could be of no value in setting marketing goals or targeting advertisements. The potential of such an influence requires that the vendor be provided sufficient incentives in terms of higher payments to preclude this possibility. In many cases, identifying the potential for anchoring may not be possible, and we do not suggest that all improvements to the feedback process will lead to an increased anchoring possibility. However, the proposition suggests that the vendor should be provided incentives to preclude him or her from providing the nonneutral prototype. This may be costly upfront, but it would help mitigate failures at later stages.

In summary, a higher effectiveness of the feedback process beyond a point leads to the vendor’s moral hazard problem becoming more severe than the client’s commitment problem. Therefore, the payments needed to motivate the vendor to supply the neutral prototype become higher. Technically, it is the vendor’s incentive constraint ICV-PR that binds when the effectiveness of the feedback process is higher than (C1). The result that the client’s profit also increases beyond this point is attributable to the productivity effect of the feedback process: the overall profit is large enough that the client can provide an additional amount to the vendor and still be better off.

A perusal of Solution 2 shows that the optimum payment to the vendor depends on the anchoring effect $( \delta _ { i i H j } )$ through the parameter $\phi$ when (C1) is not satisfied. (Note that $\mathbf { \bar { \delta } } _ { i i H j } = \phi \delta _ { j 3 H j }$ with $\phi > 1 . )$ However, when (C1) is satisfied the optimum payment to the vendor does not depend on the anchoring effect but on the client’s feedback effort through the parameter $\beta .$ (Note that $\delta _ { j 3 L j } = \beta \delta _ { j 3 H j }$ with $\beta < 1 . )$ Also, in both of these cases, the vendor’s participation and rationality constraint (IR-PR) does not bind and, thus, the vendor gets the rent, i.e., the expected profits for the vendor is greater than his or her reservation profits.

4.2.5. Impact of Effectiveness of Prototype Evaluation. The effectiveness of prototype evaluation, i.e., effectiveness of assessing whether the vendor had delivered the correct prototype, is similar to an ex post verification mechanism. Note that the information on the type of prototype that the vendor provided is obtained after the end system is developed. However, even though the information is obtained at a later point in time, it is akin to understanding why the software project succeeded or failed. At this stage, if an assessment of the prototype delivered is made and such an assessment is effective in discerning whether a neutral or a nonneutral prototype was delivered by the vendor, this information can be used to provide appropriate incentives to the vendor.<sup>28</sup> The probability that the client correctly identifies the delivered prototype is given by Prob $\vert g _ { k } \vert a _ { k } , b _ { H } ) = \alpha _ { 1 }$ is the effectiveness of prototype evaluation. The effect of such an exercise, i.e., effectiveness of prototype evaluation and how it can be used to provide appropriate incentives is summarized in the following proposition.

<sup>Proposition</sup> <sup>2.</sup> (i) The payment to vendor $( W _ { 3 } )$ increases, the profit of the vendor (V ) increases, and the profit of the client (U) decreases with increasing effectiveness of the prototype evaluation process $\left( \alpha _ { 1 } \right)$ for large $\alpha _ { 1 }$ Technically, if (C1) is not satisfied, then $d W _ { 3 } ^ { \ast } / d \alpha _ { 1 } > 0$ $d V ^ { * } ( a _ { 3 } , b _ { H } ) / d \alpha _ { 1 } > 0 .$ , and $d U ^ { * } \bar { ( } a _ { 3 } , b _ { H } ) / d \alpha _ { 1 } < \bar { 0 }$

(ii) The payment to vendor (W ) decreases, the profit of the vendor (V ) decreases, and the profit of the client (U) increases with increasing effectiveness of the prototype evaluation process $\left( \alpha _ { 1 } \right) f o r$ small $\alpha _ { 1 } .$ Technically, if (C1) is not satisfied, then $d W _ { 3 } ^ { * * } / d \alpha _ { 1 } < 0 , d V ^ { * * } ( a _ { 3 } , b _ { H } ) / d \alpha _ { 1 } < 0 .$ , and $d U ^ { * * } ( a _ { 3 } , b _ { H } ) / d \alpha _ { 1 } > 0$

Proposition 2 shows that as the effectiveness of prototype evaluation increases, the client’s profits increase up until a point and then decrease. When the effectiveness of prototype evaluation is small, then the moral hazard problem of the vendor with respect to the prototype is more severe than that of the client’s feedback effort. In other words, when the effectiveness of prototype evaluation is small, then with a greater probability the client could assess a nonneutral prototype as a neutral prototype. Thus, the vendor could benefit more from providing the nonneutral prototype. To prevent this possibility, the payment to the vendor is made high enough such that the vendor does not find it beneficial to provide the nonneutral prototype. As the effectiveness of prototype evaluation improves the moral hazard problem with respect to the vendor’s prototype choice decreases. This leads to an improvement in the client’s profits.

However, this occurs only up to a point after which the client’s commitment problem becomes more severe. The client’s commitment problem becomes more severe because at higher levels of effectiveness of prototype evaluation, the client is more sure that the vendor provides the neutral prototype that will help him or her assess his requirements. Thus, he finds it more beneficial not to exert the high effort. To commit to exerting the high effort, the client has to provide increased payments to the vendor, an effect of the interaction between the vendor’s moral hazard problem and the client’s commitment problem.

We illustrate these aspects with a numerical example.

## 5. Numerical Example

We illustrate our results using a numerical example with parameter values in Panel A of Table 2. We let Prob $( g _ { i } \mid a _ { i } , b _ { H } ) = \alpha _ { 1 } = 0 . 5 2$ and consider changes in the effectiveness of the feedback process: specifically, we set $\beta = 0 . 9 9 4 , ~ \phi = 1 . 2 0$ , and let $\delta _ { j 3 H j }$ vary from 0.535 to 0.605. Correspondingly, $\delta _ { i i H j }$ varies from 0.642 to 0.726 and $\delta _ { j 3 L j }$ varies from 0.532 to 0.601. First, we illustrate how the effectiveness of the feedback process influences the solution to Program 2, i.e., Solution 2. Second, we illustrate the result in Proposition 1 and extend the analysis to consider the impact of different levels of the anchoring effect. Third and last, we illustrate the result in Proposition 2 and extend the analysis to consider the impact of different levels of the anchoring effect.

Table 2 Numerical Example

<table><tr><td colspan="7">Panel A: Sensitivity to effectiveness of feedback process,  $\delta_{j3Hj}$ </td></tr><tr><td rowspan="2"> $\delta_{j3Hj}$ </td><td colspan="3">No prototyping</td><td colspan="3">Prototyping</td></tr><tr><td> $W_3$ </td><td>V</td><td>U</td><td> $W_3$ </td><td> $V(a_3,b_H)$ </td><td> $U(a_3,b_H)$ </td></tr><tr><td>0.535</td><td>5.000</td><td>0.000</td><td>0.000</td><td>30.359</td><td>0.786</td><td>4.114</td></tr><tr><td>0.545</td><td>5.000</td><td>0.000</td><td>0.000</td><td>30.235</td><td>0.722</td><td>14.078</td></tr><tr><td>0.555</td><td>5.000</td><td>0.000</td><td>0.000</td><td>30.111</td><td>0.658</td><td>24.042</td></tr><tr><td>0.565</td><td>5.000</td><td>0.000</td><td>0.000</td><td>29.987</td><td>0.593</td><td>34.007</td></tr><tr><td>0.575</td><td>5.000</td><td>0.000</td><td>0.000</td><td>30.179</td><td>0.693</td><td>43.807</td></tr><tr><td>0.585</td><td>5.000</td><td>0.000</td><td>0.000</td><td>30.393</td><td>0.804</td><td>53.596</td></tr><tr><td>0.595</td><td>5.000</td><td>0.000</td><td>0.000</td><td>30.607</td><td>0.916</td><td>63.384</td></tr><tr><td>0.605</td><td>5.000</td><td>0.000</td><td>0.000</td><td>30.821</td><td>1.027</td><td>73.173</td></tr></table>

Note. Parameter values: $\theta _ { 1 } = \theta _ { 2 } = 0 . 5 , \ x _ { 1 1 } = x _ { 2 2 } = \mathfrak { H } 5 0 0 , \ x _ { 1 2 } = x _ { 2 1 } =$ $- \mathfrak { H } 4 9 0 , b _ { H } = \mathfrak { H } 1 9 . 7 5 , b _ { L } = \mathfrak { H } 2 , v _ { 1 } = \mathfrak { H } 0 , v _ { 2 } = \mathfrak { H } 0 , v _ { 3 } = \mathfrak { H } 5 , c _ { 1 1 } = c _ { 2 2 } = \mathfrak { H } 5 ,$ c = c = \$10, c = c = \$10, C = C = \$5.

The optimum for the prototyping and the no prototyping regimes are provided in Table 2 (Panel A). In the no prototyping regime the client’s expected profit is zero, i.e., $\dot { U } ^ { \mathrm { \tiny { \hat { N } } } } = [ ( 5 0 0 \times 0 . 5 ) - ( 4 9 0 \times \dot { 0 . 5 } ) - 5 ]$ , and does not depend on the effectiveness of the feedback process. The vendor’s payment is \$5 and the vendor’s expected profit is zero, which exactly equals his reservation profit.

## 5.1. Illustrating Solution 2, Severity of Client’s Commitment Problem, and Vendor’s Moral Hazard Problem

When the effectiveness of the feedback process is small, i.e., condition (C1) is satisfied (for example, see Panel A of Table 2 when $\delta _ { i 3 H j } = 0 . 5 3 5 )$ , the payment to the vendor is determined by constraint (ICC-PR), i.e., $W _ { 3 } ^ { * } = 3 0 . 3 5 9$ . The client’s expected profit when the vendor provides the neutral prototype and (a) the client exerts the high-feedback effort is 4.114, i.e., $U ^ { * } ( a _ { 3 } , b _ { H } ) = ( 5 0 0 \times 0 . { \bar { 5 } } 3 5 ) - ( 4 9 0 \times 0 . 4 6 5 ) - 1 9 . 7 5 - 1$ 4300359 × 00525 = 40114; (b) the client exerts the lowfeedback effort is also 4.114, i.e., $U ^ { * } ( a _ { 3 } , b _ { L } ) = ( 5 0 0 \times$ $0 . 5 3 5 \times 0 . 9 9 4 ) - ( 4 9 0 \times \{ 1 - ( 0 . 5 3 5 \times 0 . 9 9 4 ) \} ) - 2 -$ $3 0 . 3 5 9 \ : = \ : 4 . 1 1 4$ The payment to the vendor (the incentive scheme) is chosen to make the client indifferent between choosing the low- and high-feedback effort. The vendor’s expected profit when the client exerts the high-feedback effort, and (a) the vendor provides the neutral prototype, is 0.786, i.e., $V ^ { * } ( a _ { 3 } , b _ { H } ) =$ $( 3 0 . 3 5 9 \times 0 . 5 2 ) - 1 \hat { 0 } - 5 = \dot { 0 } . 7 8 6 ; { ( \mathrm { b } ) }$ the vendor provides the nonneutral prototype is 0.496, i.e.,

$$
\begin{array}{l} V ^ {*} (a _ {3}, b _ {L}) \\ \qquad = (3 0. 3 5 9 \times \{(1 - 0. 5 2) / 2 \}) - (5 \times 0. 5 3 5 \times 1. 2) \\ \qquad - (1 0 \times \{1 - (0. 5 3 5 \times 1. 2) \}) - 0 = 0. 4 9 6. \end{array}
$$

The vendor’s expected profit with the neutral prototype is greater than zero and higher than with the nonneutral prototype; constraints (ICV-PR) and (IR-PR) are slack. This shows that when the effectiveness of the feedback effort is low, the client’s commitment problem is more severe, i.e., the party whose incentive constraint determines the vendor’s payment intuitively drives the incentive problem.

When the effectiveness of the feedback process is large, i.e., condition (C1) is not satisfied (for example, see Panel A of Table 2 when $\delta _ { j 3 H j } = 0 . 6 0 5 )$ , the payment to the vendor is determined by constraint (ICV-PR), i.e., $W _ { 3 } ^ { * } = 3 0 . 8 2 1$ . The vendor’s expected profit when the client exerts the high-feedback effort and (a) the vendor provides the neutral prototype is 1.027, i.e., $V ^ { * } ( a _ { 3 } , b _ { H } ) = ( 3 0 . 8 2 1 \times 0 . 5 2 ) - 1 0 - 5 = 1 . 0 2 7 ;$ (b) the vendor provides the nonneutral prototype is 1.027, i.e.,

$$
\begin{array}{l} V ^ {*} (a _ {3}, b _ {L}) \\ \qquad = (3 0. 8 2 1 \times \{(1 - 0. 5 2) / 2 \}) - (5 \times 0. 6 0 5 \times 1. 2) \\ \qquad - (1 0 \times \{1 - (0. 6 0 5 \times 1. 2) \}) - 0 = 1. 0 2 7. \end{array}
$$

The payment to the vendor (the incentive scheme) is chosen to make the vendor indifferent between choosing the neutral and nonneutral prototype. The client’s expected profit when the vendor provides the neutral prototype and (a) the client exerts the high-feedback effort is 73.173, i.e.,

$$
\begin{array}{l} U ^ {*} (a _ {3}, b _ {H}) \\ \qquad = (5 0 0 \times 0. 6 0 5) - (4 9 0 \times 0. 3 9 5) - 1 9. 7 5 \\ \qquad - (3 0. 8 2 1 \times 0. 5 2) = 7 3. 1 7 3; \end{array}
$$

(b) the client exerts the low-feedback effort is 72.535, i.e.,

$$
\begin{array}{l} U ^ {*} (a _ {3}, b _ {L}) \\ = (5 0 0 \times 0. 6 0 5 \times 0. 9 9 4) - (4 9 0 \times \{1 - (0. 6 0 5 \times 0. 9 9 4) \}) \\ - 2 - 3 0. 8 2 1 = 7 2. 5 3 5. \end{array}
$$

The client’s expected profit with the high-feedback effort is higher than with the low-feedback effort, i.e., constraint (ICC-PR) is slack. The vendor’s expected profit is greater than zero, i.e., (IR-PR) is slack. This shows that when the effectiveness of the feedback effort is high, the vendor’s moral hazard problem is more severe, i.e., the party whose incentive constraint determines the vendor’s payment intuitively drives the incentive problem.

## 5.2. Illustrating and Extending Proposition 1, Anchoring, and Effectiveness of the Feedback Effort

To gain additional insights into how the anchoring effect and the effectiveness of the feedback effort influence the vendor’s incentives we vary both $\delta _ { j 3 H j }$ and $\phi .$ Figure 2 graphs Solution 2 when $\delta _ { j 3 H j }$ is varied from 0.535 to 0.605 for $\phi = 1 . 1 5 , 1 . 2 0$ and 1.25: Panel $\mathrm { A }$ provides the payment to the vendor, Panel B the vendor’s expected profits, and Panel C provides the difference in client’s expected profits when $\phi = 1 . 2 0 $ . From Panels A and B it follows that, when the effectiveness of feedback effort is not sufficiently high, the anchoring effect does not impact the vendor’s payment. This could be true for new legacy systems when the effectiveness of the feedback effort may not be very effective initially. In such cases, the anchoring effect may not be a cause for concern in designing incentives for the vendor. Correspondingly, Panel C shows that anchoring does not affect the client’s expected profit when the effectiveness of feedback effort is small. However, when the effectiveness of feedback effort is large, higher (lower) anchoring effect, i.e., $\phi = 1 . 2 5 $ 410155, leads to a large decrease (increase) in client’s profits and then the difference in profits gets muted. Therefore, when the effectiveness of feedback effort is moderate, then addressing the issues of anchoring has the greatest impact. If the effectiveness of the feedback effort is large, then mitigating the anchoring effect by designing appropriate feedback processes may not result in large increases in expected profits for the client.

## 5.3. Illustrating and Extending Proposition 2,

Anchoring, and Prototype Evaluation Process Figure 3 graphs Solution 2 when $\alpha _ { 1 }$ is varied from 0.51 to 0.58 for $\phi = 1 . 1 5 , 1 . 2 0 ,$ , and 1.25. Similar to Figure 2, Panel A provides the payment to the vendor, Panel B the vendor’s expected profits, and Panel C the difference in client’s expected profits when $\phi = 1 . 2 0 $ From Panels A and B it follows that when the effectiveness of the prototype evaluation process is sufficiently small (large), the anchoring effect does (does not) impact the vendor’s payment and client’s profits. This occurs because when the effectiveness of the prototype evaluation process is large, the vendor’s moral hazard problem is less severe: If the vendor provides the nonneutral prototype, the prototype evaluation process is likely to show it. Panel C shows that anchoring does not affect the client’s expected profit when the effectiveness of prototype evaluation process is large. However, when the effectiveness of the prototype evaluation process is small, a higher (lower) anchoring effect, i.e., $\phi = 1 . 2 5 ( 1 . 1 5 )$ , leads to a large decrease (increase) in client’s profits and then the difference in profits is substantial. In effect, when the effectiveness of prototype evaluation process is moderate, then addressing the issues of anchoring has the greatest impact and continues to be so for low effectiveness also. If the effectiveness of the prototype evaluation process is very small, then mitigating the anchoring effect by designing appropriate feedback processes could result in large increases in expected profits for the client.

Panel C: Client’s expected profits, U(a<sub>3</sub>, b<sub>H</sub>)  
Figure 2 Sensitivity to Effectiveness of Feedback Process, $\delta _ { j 3 H j }$  
![](/api/attachments/UBXCYKEY/fulltext/images/e3cda9fc9459d2b9a1dfe7144a403ad01e130e717565b9c8a597cc592360bcc5.jpg)

Panel B: Vendor’s expected profits, V(a<sub>3</sub>, b<sub>H</sub>)  
![](/api/attachments/UBXCYKEY/fulltext/images/5482644181bc4a9f753eb40f5ad5ecd69eab61dc32deea32fffd29aa85b428b7.jpg)

![](/api/attachments/UBXCYKEY/fulltext/images/17f467ca011acd65330d8128a983b30e8a65857a40b27a09a92c66bc6b755d4d.jpg)

## 5.4. Managerial Implications

The analysis provides insights into the requirements assessment phase of software development. First, we show how incentives need to be incorporated into the feedback process for the vendor. The client needs to provide additional incentives to the vendor to commit to being engaged in the feedback process. This is more likely to occur when off the shelf software is customized to fit the client’s needs. The client has an incentive to not be as engaged in the software project, because he or she could feel that the vendor has experience in implementing systems elsewhere and can figure out what is needed. In such cases, the client could provide more incentives for the vendor to commit himself or herself to provide adequate feedback.

Figure 3 Sensitivity to Effectiveness of Prototype Evaluation Process, <sub>1</sub>  
Panel A: Vendor’s payment, W<sub>3</sub>  
![](/api/attachments/UBXCYKEY/fulltext/images/32e3fbfcf6e575c197a079fd21852c2cc1a24f6571dac94c3df0cafabbf16b17.jpg)

Panel B: Vendor’s expected profits, V(a<sub>3</sub>, b<sub>H</sub>)  
![](/api/attachments/UBXCYKEY/fulltext/images/c75f6bce3e85c30008e25aceafedaf4758eaa005c4a0d68a1c43a9425c6360dc.jpg)

Panel C: Client’s expected profits, U(a , b )  
![](/api/attachments/UBXCYKEY/fulltext/images/9a1204cf7ed422778bdc4ed0b0ffed18313d7fcd7be3bd8cb84ba4976c62fb55.jpg)

Second, we provide insights into the design of the feedback process and the prototype evaluation process. We find that when either the prototype evaluation process is very good or the feedback process is poor, then the anchoring effect is muted. In other words, the prototype evaluation process and the feedback process are substitutes for providing incentives to the vendor, as well as mitigating the anchoring effect.

In cases where the prototype can be evaluated more precisely, the vendor needs to be provided incentives so that the client commits to good feedback effort. In cases where the feedback is likely to be poor, again the vendor needs to be provided incentives so that the client commits to good feedback effort. Overall, the prototype and feedback process design should be concerned about the possibility of vendor influencing the requirement assessment in an undesirable fashion when the effectiveness of the feedback process is sufficiently high.

## 6. Concluding Remarks

We examined a model of requirements assessment through prototyping and incorporated the following features: (a) experimentation by the client to assess and learn his or her requirements, (b) the vendor’s moral hazard problem, and (c) the client’s commitment problem. We considered a principal agent setting and incorporated the effect of anchoring in the feedback process. Improving the effectiveness of the feedback process (a) helps the client to asses his or her true requirements more precisely, if the vendor delivers the neutral prototype and (b) induces the client to be more influenced by the nonneutral prototype. We showed that the client has to pay the vendor a high enough amount to commit to the high-feedback effort when the effectiveness of feedback effort is low and correspondingly the client’s profits are low. When the effectiveness of feedback process is large, the anchoring effect increases, leading to higher payments to the vendor to mitigate the anchoring effect. We, th $^ { 1 S , }$ highlight the effects of the interactions between the vendor’s moral hazard problem and the client’s commitment problem on the incentive payments to the vendor and the feedback process design.

We model the anchoring effect by letting the vendor influence the requirements assessment when the feedback process is effective. We did this under the notion that effective feedback processes would require experts who may be prone to attribution and confirmation biases. However, if lesser experts are also prone to such biases, our results show that it is the degree of severity of the client’s commitment problem and the vendor’s moral hazard problem that determines the incentives. In fact, we show that vendor’s incentives can be designed such that the vendor provides the neutral prototype and the client exerts the high-feedback effort. In essence, even though concerns of anchoring exist, we show that vendor incentives can be designed so as to enable “good” and successful software development. This is a first step in analyzing the interactions between commitment concerns and behavioral notions of anchoring. Future research can examine iterative procedures and coordination effects in prototyping. Although this would complicate the analysis, numerical solutions could possibly provide additional insights. Future research can also consider other commitment issues in terms of enforceability of the signals on the vendor’s prototype.

## Appendix

<sup>Derivation</sup> <sup>of</sup> <sup>Solution</sup> <sup>1.</sup> The solution follows because (IR-1) is binding.

<sup>Derivation</sup> <sup>of</sup> <sup>Solution</sup> <sup>2.</sup> Using the symmetry assumptions, i.e., $c _ { i j } = c _ { j i } , x _ { i j } = x _ { j i } , \delta _ { 1 1 H j } = \delta _ { 2 2 H j }$ and $v _ { 1 } = v _ { 2 }$ for all $j , i = 1 , 2 ,$ the right side of (ICV1-PR) and (ICV2-PR) are identical: thus, we refer to the constraints as (ICV-PR). To see that, $W _ { 1 } = W _ { 2 } = 0$ is optimum, assume that $W _ { 1 }$ or $W _ { 2 } > 0$ is the solution. Decreasing W and W to zero does not violate any constraints and increases the objective function to establish a contradiction. The solution to program 1 is given by $W _ { 3 }$ satisfying either (ICV-PR), (ICC-PR), or (IR-PR). Assume that $W _ { 3 }$ satisfies (IR-PR), then using assumption A1 it is established that constraint (ICV-PR) is not satisfied, and using assumption A2 it is established that constraint (ICC-PR) is not satisfied. Thus, $W _ { 3 }$ satisfying (IR-PR) cannot be a solution. Solving for $W _ { 3 }$ using (ICC-PR) yields $W _ { 3 } ^ { * }$ and using (ICV-PR) yields $W _ { 3 } ^ { * * }$ in Solution 2. Thus, the solution to Program 2 is given by max8W <sup>∗</sup>1 W <sup>∗∗</sup>9. Using condition (C1) it is verified that when (C1) is satisfied $W _ { 3 } ^ { * } > W _ { 3 } ^ { * * }$ , and vice versa. The expected profits are derived by substituting W <sup>∗</sup><sub>3</sub> , $W _ { 3 } ^ { * * }$ in $U ( \cdot )$ and $V ( \cdot ) ,$ respectively.

<sup>Proof</sup> <sup>of</sup> <sup>Observation</sup> <sup>1.</sup> Use assumption A4 to establish that the expected profit for the client is increasing in $\delta _ { 1 3 H 1 }$ Thus, it is sufficient to show that at $\delta _ { j 3 H j }$ close to 0.5 the client’s expected profit in Solution 2 is greater than that of Solution 1. Noting that for $\delta _ { j 3 H j } \to 0 . 5$ the solution is given by $W _ { 3 } ^ { * }$ and $U ^ { * } ( \cdot )$ , and using assumption A3 the observation follows.

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>1.</sup> Differentiating the optimum in Solution 2 with respect to $\delta _ { 3 H }$ we get the following:

$$
\begin{array}{c} \operatorname{sign} [ d W _ {3} ^ {*} / d \delta_ {j 3 H j} ] = \operatorname{sign} [ - (x _ {1 1} - x _ {1 2}) (1 - \beta) ] <   0, \\ \operatorname{sign} [ d W _ {3} ^ {* *} / d \delta_ {j 3 H j} ] = \operatorname{sign} [ (c _ {1 2} - c _ {1 1}) \phi ] > 0, \\ \operatorname{sign} [ d V ^ {*} (a _ {3}, b _ {H}) / d \delta_ {j 3 H j} ] = \operatorname{sign} [ d W ^ {*} (a _ {3}, b _ {H}) / d \delta_ {j 3 H j} ] <   0, \\ \operatorname{sign} [ d V ^ {* *} (a _ {3}, b _ {H}) / d \delta_ {j 3 H j} ] = \operatorname{sign} [ d W ^ {* *} (a _ {3}, b _ {H}) / d \delta_ {j 3 H j} ] > 0, \\ d U ^ {*} (a _ {3}, b _ {H}) / d \delta_ {j 3 H j} = [ (x _ {1 1} - x _ {1 2}) (1 - \alpha_ {1} \beta) ] / (1 - \alpha_ {1}) > 0, \quad \text { and } \\ d U ^ {* *} (a _ {3}, b _ {H}) / d \delta_ {j 3 H j} = (x _ {1 1} - x _ {1 2}) - \alpha [ (c _ {1 1} - c _ {1 2}) \phi ] / X > 0, \end{array}
$$

where the last inequality is obtained from A4.

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>2.</sup> Differentiating the optimum in Solution 2 with respect to $\alpha _ { 1 }$ we get the following results:

$$
\begin{array}{l} \text {sign} [ d W _ {3} ^ {*} / d \alpha_ {1} ] = \text {sign} [ (b _ {H} - b _ {L}) - (x _ {1 1} - x _ {1 2}) (1 - \beta) \delta_ {j _ {3} H j} ] > 0, \\ \text {sign} [ d W _ {3} ^ {* *} / d \alpha_ {1} ] \\ \qquad = - \text {sign} [ c _ {3 1} + v _ {3} - c _ {1 2} - v _ {1} + (c _ {1 2} - c _ {1 1}) \phi \delta_ {j _ {3} H j} ] <   0, \\ \text {sign} [ d V ^ {*} (a _ {3}, b _ {H}) / d \alpha_ {1} ] = \text {sign} [ d W ^ {*} (a _ {3}, b _ {H}) / d \alpha_ {1} ] > 0, \\ \text {sign} [ d V ^ {* *} (a _ {3}, b _ {H}) / d \alpha_ {1} ] = \text {sign} [ d W ^ {* *} (a _ {3}, b _ {H}) / d \alpha_ {1} ] <   0, \\ \text {sign} [ d U ^ {*} (a _ {3}, b _ {H}) / d \alpha_ {1} ] \\ \qquad = - \text {sign} [ (b _ {H} - b _ {L}) - (x _ {1 1} - x _ {1 2}) (1 - \beta) \delta_ {j _ {3} H j} ] <   0, \quad \text {and} \\ \text {sign} [ d U ^ {* *} (a _ {3}, b _ {H}) / d \alpha_ {1} ] \\ \qquad = \text {sign} [ c _ {3 1} + v _ {3} - c _ {1 2} - v _ {1} + (c _ {1 1} - c _ {1 2}) \phi \delta_ {j _ {3} H j} ] > 0, \end{array}
$$

where the inequalities are obtained from A1 and A2.

## References

Ackoff, R. L. 1967. Management misinformation systems. Management Sci. 14(4) 147–156.

Aranda, J., S. Easterbrook. 2005. Anchoring and adjustment in software estimation. Proc. 10th Eur. Software Engrg. Conf., ACM Press, New York, 346–355.

Arya, A., J. Glover, S. Radhakrishnan. 2007. The Controllability Principle in Responsibility Accounting: Another Look, Essays in Accounting Theory in Honour of Joel S. Demski. Springer, New York, 183–198.

Arya, A., J. Glover, K. Shivaramakrishnan. 1997. The intereffort between decision and control problems and the value of information. Accounting Rev. 72 561–574.

Arya, A., J. Glover, S. Sunder. 1998. Earnings management and the revelation principle. Rev. Accounting Stud. 3(1-2) 7–34.

Baiman, S., P. E. Fischer, M. V. Rajan. 2000. Information, contracting and quality costs. Management Sci. 46(6) 776–789.

Balachandran, K. R., S. Radhakrishnan. 2005. Quality implications of warranties in a supply chain. Management Sci. 51(8) 1266–1277.

Benbasat, I., R. G. Schroeder. 1977. An experimental investigation into some MIS design variables. MIS Quart. 1(1) 37–50.

Berinato, S. 2001. How to buy and not get sold. Retrieved January 10, 2006, http://www.darwinmag.com/read/120101/ sold.html.

Berrisford, T. R., J. C. Wetherbe. 1979. Heuristic development: A redesign of system design. MIS Quart. 3 11–19.

Davidson, E. J. 1999. Joint application design (JAD) in practice. J. Systems Software 45(3) 215–223.

Davis, G. B. 1982. Strategies for information requirements determination. IBM Systems J. 21(1) 4–30.

Demski, J. S., D. E. M. Sappington. 1993. Sourcing and unverifiable performance information. J. Accounting Res. 31(1) 1–20.

Dennis, A., B. H. Wixom, D. Tegarden. 2002. System Analysis and Design: An Object Oriented Approach with UML. John Wiley and Sons, New York.

Elssamadisy, A., G. Schalliol. 2002. Recognizing and responding to “bad smells” in extreme programming. Proc. 24th Internat. Conf. Software Engineering, ACM Press, New York, 617–622.

Galloway, R. L., G. White. 1989. The internal information systems function as a service operation. Internat. J. Oper. Production Management 9(4) 19–27.

Goodrich, V., L. Olfman. 1990. An experimental evaluation of task and methodology variables for requirements definition phase success. Proc. Twenty-Third Annual Hawaii Internat. Conf. Systems Sci., IEEE Computer Society Press, Washington, DC, 201–209.

Grudin, J. 1991. Systematic sources of suboptimal interface design in large product development organizations. Human-Comput. Interaction 6(2) 147–196.

Hunton, J. E., J. D. Beeler. 1997. Effects of user participation in systems development: A longitudinal field experiment. MIS Quart. 21(4) 359–388.

Hwang, I., S. Radhakrishnan, N. Su. 2006. Vendor certification and appraisal: Implications for supplier quality. Management Sci. 52(10) 1472–1482.

I.T. Cortex. 2004. Statistics over I.T. failure. Retrieved January 9, 2006, http://www.it-cortex.com/Stat\_Failure\_Rate.htm.

Joyce, E. J., G. C. Biddle. 1979. Anchoring and adjustment in probabilistic inference in auditing. J. Accounting Res. 19(1) 120–145.

Key, P. 1998. SAP America hit with a 500M suit. Retrieved February 20, 2006, http://www.bizjournals.com/philadelphia/ stories/1998/11/02/story2.html.

Kohli, R., S. Devaraj. 2004. Realizing the business value of information technology investments: An organizational process. MIS Quart. Executive 3(1) 53–68.

Lyytinen, K., R. Hirschheim. 1987. Information systems failures: A survey and classification of the empirical literature. Oxford Surveys in Information Technology. Oxford University Press, New York, 257–309.

Martin, A., R. Biddle, J. Noble. 2004. The XP customer role in practice: Three studies. Proc. Agile Development Conf., IEEE Computer Society, Washington, DC, 42–54.

Milgrom, P., J. Roberts. 1992. Economics, Organization and Management. Prentice Hall, Englewood Cliffs, NJ.

Neumann, J. D., A. M. Jenkins. 1982. Prototyping: The new paradigm for systems development. MIS Quart. 6(3) 29–44.

Northcraft, G. B., M. A. Neale. 1987. Experts, amateurs, and real estate: An anchoring and adjustment perspective on property pricing decisions. Organ. Behav. Human Decision Processes 39(1) 84–97.

Stephens, M., D. Rosenberg. 2003. Extreme Programming Refactored: The Case Against XP. APress, Berkeley, CA.

The Standish Group. 1994. The chaos report. Accessed November 22, 2009, http://www.standishgroup.com/public.php.

Tirole, J. 1999. Incomplete contracts. Where do we stand? Econometrica 67(4) 741–781.

Tversky, A., D. Kahneman. 1974. Judgment under uncertainty: Heuristics and biases. Science 185 1124–1131.

Valusek, J. R., D. G. Fryback. 1985. Information requirements determination: Obstacles within, among, and between participants. Proc. Twenty-First Annual Conf. Comput. Personnel Res., ACM Press, New York, 103–111.

Whyte, G., A. Bytheway. 1996. Factors affecting information systems success. Internat. J. Service Indust. Management 7(1) 74–93.

Wilson, S., M. Bekker, P. Johnson, H. Johnson. 1997. Helping and hindering user involvement—A tale of everyday design. S. Pemberton, ed. Proc. SIGCHI Conf. Human Factors in Comput. Systems, CHI ’97. ACM Press, New York, 178–185.
