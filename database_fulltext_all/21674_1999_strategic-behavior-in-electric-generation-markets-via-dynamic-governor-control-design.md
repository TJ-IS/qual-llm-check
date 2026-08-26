---
otero_id: 21674
otero_key: "EMFFVB9K"
title: "Strategic behavior in electric generation markets via dynamic governor control design"
authors: "Christopher L. DeMarco"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00079-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Strategic behavior in electric generation markets via dynamic governor control design

Christopher L. DeMarco )

Department of Electrical and Computer Engineering, UniÕersity of Wisconsin-Madison, 1415 Engineering DriÕe, Madison, WI 53706, USA

## Abstract

Previous work has demonstrated the potential for coordinated control of a group of generators in a generation market, with the goal of destabilizing other machines in the system, while maintaining nearly completely satisfactory performanceŽ . within this control group. Such action would clearly achieve an anti-competitive objective, and might be attractive strategic behavior if the entities involved believed it would go undetected. The work here examines the degree to which, among all competing generators, a subset may be specifically ‘targeted’ to experience instability. It refines the earlier design technique to demonstrate that anti-competitive control can indeed selectively target competing generators. This form of strategic behavior will be termed ‘predatory control.’ The results presented suggest that the risk of predatory control is more severe than earlier analysis might have suggested, and provides a cautionary note to indicate that entities responsible for system security must have tools to guard against such behavior. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Anti-competitive behavior in electric generation markets; Strategic behavior in electric generation markets; Electric generator governor control, eigenvector placement

## 1. Introduction and motivation

The evolving regulatory changes for electric utilities in the US and worldwide seek to force generating units to operate in a competitive manner. With this move towards competition among generators, it is typically assumed that effects related to dynamic control action operate on a time scale for which economic effects are less significant, and that relevant aspects of control performance can be monitored in a straightforward fashion by an independent system operator or equivalent entity. However, the role of a system operator in monitoring the exact nature of dynamic control at generators remains an on-going topic of discussion in the US. These debates focus in part on market mechanisms to encourage certain types of performance, under the heading of ‘pricing ancillary services,’ and in part on enforceable, system-related control performance standards. At the risk of stereo-typing these two approaches, the former may be largely associated with those possessing a market economist’s viewpoint, the latter with those having views closely related to the traditional utility analyst.

Against this backdrop, the work to be presented here is intended as a cautionary note to indicate that both viewpoints above may be overlooking potential that exists for a very subtle, high risk form of strategic behavior that might attempt to disable competitors in a generation market. In many ways, a synchronous electric power grid presents dynamic features unlike those of any other market. In a power network, two rival sets of generating units do not interact through the market alone. Rather, their electro-mechanical dynamics are tightly coupled through the electric grid. Therefore, the dynamic governor and excitation control exercised at one machine can have large impact on the dynamic response of other generating units, and on the network as a whole. Previous work 3 has demonstrated an eigenvalue <sup>w</sup> <sup>x</sup> <sup>r</sup> eigenvector placement technique that creates an unstable mode in an otherwise stable system, while guaranteeing that the participants whose control creates this instability are largely shielded from its effects. However, that design methodology was relatively crude, as it did not allow tailoring of the degree of participation in the unstable mode outside the protected group. In other words, it did not allow the targeting of specific competitors to experience instability. The goal in the work to be presented here is an extension of the earlier design techniques, so that a greater degree of ‘targeting’ of competitors is possible. Clearly, this analysis is presented not with the goal of encouraging such behavior, but rather to raise a warning flag regarding its possibility. The prospect of a predatory competitor being able to target specific rival generators makes the threat of this anti-competitive behavior more credible. It is this author’s hope that the presentation here will convince readers that means to police and protect against this form of predatory control are worthy of further investigation.

## 2. Analytic background: eigenvector and eigen value placement

The key analytic steps in this work rest upon simultaneous eigenvalue and eigenvector placement, as described in Ref. 6 . It is therefore worthwhile to<sup>w</sup> <sup>x</sup> briefly review the results of Moore 6 , which de- <sup>w</sup> <sup>x</sup> scribe all eigenvalue and right eigenvector pairsŽ . achievable by linear state feedback in a controllable system. To this end, consider the closed loop linear state equation:

$$
\dot {\mathbf {x}} = (\mathbf {A} - \mathbf {B F}) \mathbf {x}\tag{1}
$$

associated with an open loop system:

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\tag{2}
$$

to which a state feedback u<sup>sy</sup>Fx is applied. Here:

$$
\mathbf {x} \in \boldsymbol {R} ^ {n}; \quad \mathbf {u} \in \boldsymbol {R} ^ {m}; \quad \mathbf {A} \in \mathbf {R} ^ {n \times n};
$$

$$
\mathbf {B} \in \mathbf {R} ^ {n \times m}; \quad \mathbf {F} \in \mathbf {R} ^ {m \times n},
$$

where ${ \pmb R } ^ { n } \ \left( { \pmb R } ^ { n \times m } \right)$ Ž . denotes a vector matrix of n $\left( n \times m \right)$ real elements, and $C ^ { n }$ a vector of n complex elements. For a given a complex scalar , which may be viewed as the candidate eigenvalue, define the Hautus matrix:

$$
\mathbf {S} _ {\lambda} := \left[ (\lambda \mathbf {I} - \mathbf {A}) \mathbf {B} \right], \quad \mathbf {S} _ {\lambda} \in \mathbf {C} ^ {n \times (n + m)}.\tag{3}
$$

Also define the matrix $\mathbf { K } _ { \lambda } ,$ , with its row partitions along the same boundary as the partitions of columns in $\mathbf { S } _ { \lambda } . ~ \mathbf { K } _ { \lambda }$ is given by:

$$
\mathbf {K} _ {\lambda} := \left[ \begin{array}{c} \mathbf {N} _ {\lambda} \\ \mathbf {M} _ {\lambda} \end{array} \right], \qquad \mathbf {K} _ {\lambda} \in \mathbf {C} ^ {(n + m) \times m},\tag{4}
$$

and is composed of columns that span the null space of ${ \bf { S } } _ { \lambda } ;$ i.e., for any $\mathbf { h } \in C ^ { m + n }$ such that:

$$
\mathbf {S} _ {\lambda} \mathbf {h} = 0,
$$

there exists a $k \in C ^ { m }$ such that:

$$
\mathbf {h} = \mathbf {K} _ {\lambda} \boldsymbol {k}.
$$

With this notation, Proposition 1 of Moore 6 may <sup>w</sup> <sup>x</sup> be restated as follows.

Proposition 1 Žfrom Ref. 6 . Consider<sup>w</sup> <sup>x</sup>. $\left\{ \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \right.$ $\lambda _ { n } \}$ , a self conjugate set of distinct complex numbers, and a set of complex vectors $\{ \pmb { v } _ { 1 } , \pmb { v } _ { 2 } , \ . . . , \pmb { v } _ { n } \}$ . There exists a F such that $\lambda _ { i } \pmb { v } _ { i } = ( \mathbf { A } - \mathbf { B } \mathbf { F } ) \pmb { v } _ { i }$ for all $i \in \{ 1$ $2 , \ldots , n \}$ if and only if the following three conditions are satisfied for all $i \in \left\{ 1 , 2 , \ldots , n \right\}$

Ž .i The vectors $\{ \pmb { v } _ { 1 } , \ \pmb { v } _ { 2 } , \ \dots , \ \pmb { v } _ { n } \}$ form a linearly independent set within $C ^ { n }$ Žover the field of complex scalars ..

Ž . ii ${ \pmb v } _ { i } = { \pmb v } _ { j }$ ) whenever $\lambda _ { i } = \lambda _ { j } *$

iii. ${ \pmb v } _ { i } \in \mathrm { s p a n } \{ { \bf N } _ { \lambda _ { i } } \}$

Furthermore, if F exists and B is full column rank, then F is unique.

Consider the application of these results to our problem. First, observe that for any $( \lambda _ { i } , v _ { i } )$ that is in the spectrum of A, conditions i and ii are triviallyŽ . Ž . satisfied. Moreover, by definition, $v _ { i }$ lies in the null space of $\left( \lambda _ { i } \mathbf { I } - \mathbf { A } \right)$ , and hence in the span of $\mathbf { N } _ { \lambda _ { i } }$ . We conclude that however one may attempt to place a subset of eigenpairs satisfying i – iii , it is alwaysŽ . Ž . possible to leave an arbitrary number of eigenpairs invariant from their original, uncontrolled values. Therefore, if one begins with a nominal system that is stable before application of the predatory feed- Ž back control , it is always possible to leave an . arbitrary number of modes of the system unperturbed at their original, stable values after application of the proposed feedback.

## 3. Construction of targeted predatory control: full state feedback case

The construction of the desired malicious state feedback for the control group of generators requires knowledge of the linearized swing dynamics, with classical models for machines. This implies that the bulk of the information required is power flow data, which is quite likely to be available in rough form publicly, and in more precise form i.e., with breakerŽ settings and on-line machines known to good approximation by any entity operating an effective . on-line state estimator. The only data required that is unlikely to be available publicly is that associated with machine inertias and transient reactances. However, given a knowledge of the general nature and power rating of a generating unit, a reasonable estimate of its inertia and transient reactance may easily be generated.

Based on availability of the data above, we shall assume that the state matrix description for the linearized swing dynamic equations is known. Denote this quantity as A. As is true in many calculations involving swing dynamic modes e.g., coherency Ž calculations 2 , it is convenient to form a state<sup>w</sup> <sup>x</sup>. representation that is not minimal, in which all machine angles are maintained as states. In this way the choice of a reference machine does not impact the state description. For a system having a total number of machines $p ,$ the state space is then composed of $p$ generator frequency deviations from synchronous speed, denoted $\omega ,$ and $p$ phase angles that measure deviation from a synchronous reference, denoted $\delta .$

The total state dimension will be denoted as n, with $n = 2 p$ . As appropriate to a linear model, the deviations are relative to the synchronous frame that coincides with the steady state equilibrium frequency. For simplicity, let us assume that all eigenvalues of A are distinct. Denote these eigenvalues as $\left\{ \lambda _ { 1 } , ~ \lambda _ { 2 } , ~ . . . , ~ \lambda _ { n } \right\}$ . Given distinct eigenvalues, one has a full set of eigenvectors, $\{ \pmb { v } _ { 1 } , ~ \pmb { v } _ { 2 } , ~ \ldots , ~ \pmb { v } _ { n } \}$ spanning C <sup>n</sup>.

As in Ref. 3 , we adopt a labeling in which states<sup>w</sup> <sup>x</sup> corresponding to frequency deviations appear first in the ordering, angle deviations next. Moreover, within each partition frequencies and angles , those states Ž . in positions 1 through m are associated with generators in the group from which the predatory control is to be exercised. Let $\mathbf { J } _ { \mathrm { c } }$ denote the diagonal matrix of per unit normalized generator inertias for the control group. With the ordering described, $\mathbf { B } = [ \mathbf { J } _ { \mathrm { c } } ^ { - 1 } 0 ] ^ { \mathrm { T } }$ would define the control input matrix in the state description. Given the reasonable assumption of positive inertias, B has full column rank. To begin the analysis, full state feedback is assumed, i.e., all states are assumed available for measurement. Moreover, we also assume that the system is controllable from the power inputs of the control machines. A linearized swing dynamic model is typically controllable from any one machine power input, so this is not a strong assumption. Moreover, this property can be tested numerically for any system of interest, and in particular, for our example to follow.

As noted earlier, the weakness of the construction in Ref. 3 , which might lead a reader to believe that<sup>w</sup> <sup>x</sup> the threat of malicious<sup>r</sup>predatory control was not credible, lay in the fact that the control design there could only construct an unstable mode for which participation by control group generators was limited. More specifically, that design technique selected a so-called ‘sacrificial machine’ among the control group, and then guaranteed that all remaining machines in the control group had zero participation in the unstable mode. However, the degree to which the sacrificial machine participated, and the relative participation of machines outside the control group, was not dictated by the design. The preliminary examples examined in Ref. 3 showed that it was<sup>w</sup> <sup>x</sup> quite possible to obtain cases where some machines outside the control group had much larger participation than the sacrificial machine, but there was no mechanism offered to target specific machines to be most affected by the instability. For an unscrupulous competitor to be tempted to engage in predatory control, the competitive advantage obtained must be ‘worth’ the large risk involved. This is more likely the case if the design can target specific machines Ž . outside the control group to be the primary participants in the unstable mode. Below, we will outline a simple modification to the design algorithm of De-Marco et al. 3 which makes this possible. <sup>w</sup> <sup>x</sup>

To motivate the algorithm, it is useful to elaborate on the algebraic results of Section 2, to show the underlying degrees of freedom available in eigenvector placement. As in Ref. 3 , we will assume that the<sup>w</sup> <sup>x</sup> unstable mode created is obtained by shifting to the right a previously stable complex conjugate pair of eigenvalues. However, unlike in Ref. 3 , this choice <sup>w</sup> <sup>x</sup> will not be made arbitrarily. We shall illustrate in our example below, but let us assume that the mode that is perturbed to become unstable has nontrivial participation of machines that are being targeted to experience the instability. Selection of this mode fixes the target eigenvalue pair. Hence, for this target eigenvalue, the matrix $\mathbf { S } _ { \lambda }$ and the associated matrix of vectors spanning its null-space, $\mathbf { K } _ { \lambda } ,$ are known. By construction, the number of columns of $\mathbf { K } _ { \lambda }$ is equal to the number of generators in the control group, m. Moreover, any the possible eigenvector that can be achieved with the target unstable mode is in the span of $\mathbf { N } _ { \lambda } .$ , subject to a normalization constraint e.g., oneŽ might choose the 2-norm of the eigenvector be equal to 1 . Hence, roughly speaking, one has . $m - 1$ degrees of freedom in picking the eigenvector. In Ref. <sup>w</sup> <sup>x</sup> 3 , this freedom was used to ensure that $m - 1$ machines in the control group had exactly zero participation in the unstable mode. With only $m - 1$ degrees of freedom, the sacrificial machine’s eigenvector component could not be simultaneously specified.

In contrast to the approach in Ref. 3 , here we<sup>w</sup> <sup>x</sup> will exploit the degrees of freedom available in an optimization setting. Note first that any obtainable unstable eigenvector may be viewed as a linear function of an underlying vector $k \in C ^ { m }$ ; without loss of generality, we may require that $\| \pmb { k } \| = 1$ Further, let us assume that the set of machines to be targeted for instability are specified. Consider square of the 2-norm of components of the unstable eigenvector associated with states in the target machine group, and the square of the 2-norm of the eigenvector components associated with machines to be ‘protected’ from significant participation in the unstable mode. We refer to this latter group as the ‘nontarget’ machines. As will be illustrated below, each of these quantities will be a quadratic form in k, at least positive semidefinite. Therefore, the ratio of these two quantities will typically be a positive semidefinite quadratic form in the case where the denomina-Ž tor quantity is only positive semidefinite, we may make the participation of target machines infinitely large in ratio to nontarget machines . With the con- . straint that <sup>5</sup> <sup>5</sup> k <sup>s</sup> 1 2-norm , the resulting optimiza-Ž . tion becomes a simple problem in identifying the maximum singular value of the matrix realization of the quadratic form, and k is selected as the associated principal direction. For the case of large scale problems, this problem may be efficiently solved via power methods. For the small examples to follow below, direct calculation of singular values is feasible.

Let us make the discussion above more concrete. Temporarily, let us postpone description of the heuristic for selecting an unstable eigenvalue to the discussion of our example system in Section 5. Assume such a selection has been made. Any achievable eigenvector to accompany this unstable eigenvalue may be described as:

$$
\boldsymbol {v} = \mathbf {N} _ {\lambda} \boldsymbol {k}; \quad \boldsymbol {k} \in C ^ {m}; \quad \| \boldsymbol {k} \| _ {2} = 1.
$$

Let $\mathbf { N } _ { \lambda \mathrm { T } }$ denote those rows of $\mathbf { N } _ { \lambda }$ with indices corresponding to states of the target machines, $\mathbf { N } _ { \lambda \mathrm { N T } }$ rows of $\mathbf { N } _ { \lambda }$ with indices corresponding to states of the nontarget machines. The design vector k is chosen as the maximizer for the following optimization problem:

$$
\max \frac {\boldsymbol {k} ^ {\prime} \left[ \mathrm{N} _ {\lambda \mathrm{T}} \right] ^ {\prime} \mathrm{N} _ {\lambda \mathrm{T}} \boldsymbol {k}}{\boldsymbol {k} ^ {\prime} \left[ \mathrm{N} _ {\lambda \mathrm{NT}} \right] ^ {\prime} \mathrm{N} _ {\lambda \mathrm{NT}} \boldsymbol {k}}, \quad \text { subject   to } \boldsymbol {k} ^ {\prime} \boldsymbol {k} = 1,\tag{5}
$$

Ž where the prime operation denotes complex con-. jugate transpose. Note that if the matrix $[ \mathbf { N } _ { \lambda \mathrm { N T } } ] ^ { \prime } \mathbf { N } _ { \lambda \mathrm { N T } }$ fails to be positive definite, we may select k to drive the denominator of this objective function to zero. Roughly speaking, this would be the ‘best’ case for the predatory control design; the participation of target machines in the unstable mode would be infinite relative to the participation of nontarget machines. More likely, however, is the case in which $\mathbf { N } _ { \lambda \mathrm { N T } }$ is full rank. In this case, $[ \mathbf { N } _ { \lambda \mathrm { N T } } ] ^ { \prime } \mathbf { N } _ { \lambda \mathrm { N T } }$ will have a well-defined matrix square root, and the maximum for the problem above is equal to the maximum singular value of:

$$
\begin{array}{l} \mathbf {Q} := \left(\left[ \mathbf {N} _ {\lambda \mathrm{NT}} \right] ^ {\prime} \mathbf {N} _ {\lambda \mathrm{NT}}\right) ^ {- 1 / 2} \left[ \mathbf {N} _ {\lambda \mathrm{T}} \right] ^ {\prime} \mathbf {N} _ {\lambda \mathrm{T}} \\ \times \left(\left[ \mathbf {N} _ {\lambda \mathrm{NT}} \right] ^ {\prime} \mathbf {N} _ {\lambda \mathrm{NT}}\right) ^ {- 1 / 2}. \end{array}\tag{6}
$$

The associated principal direction of Q, which we may denote as $\pmb { v } _ { \mathrm { m a x } }$ , determines k via:

$$
\boldsymbol {k} = \left(\left[ \mathbf {N} _ {\lambda \mathrm{NT}} \right] ^ {\prime} \mathbf {N} _ {\lambda \mathrm{NT}}\right) ^ {- 1 / 2} \boldsymbol {v} _ {\max}.\tag{7}
$$

Once the vector k is identified from the steps above, construction of the feedback matrix F is straightforward. Let $\boldsymbol { w } _ { 1 } = \mathbf { M } _ { \boldsymbol { \hat { \lambda } } _ { 1 } } \boldsymbol { k } , \ \boldsymbol { v } _ { 1 } = \mathbf { N } _ { \boldsymbol { \hat { \lambda } } _ { 1 } } \boldsymbol { k }$ . Then construct the real matrix $\mathbf { W } \in \dot { \mathbf { R } } ^ { m \times n }$

$$
\mathbf {W} = \left[ \operatorname{Re} \{\boldsymbol {w} _ {1} \} \operatorname{Im} \{\boldsymbol {w} _ {1} \} 0 \dots 0 \right]
$$

Also construct the real, full rank matrix $\mathbf { V } \in \mathbf { R } ^ { n \times n }$

$$
\begin{array}{c} \mathbf {V} = \left[ \operatorname{Re} \{\boldsymbol {v} _ {1} \}, \operatorname{Im} \{\boldsymbol {v} _ {1} \}, \operatorname{Re} \{\boldsymbol {v} _ {3} \}, \operatorname{Im} \{\boldsymbol {v} _ {3} \}, \dots , \right. \\ \left. \operatorname{Re} \{\boldsymbol {v} _ {n - 2} \}, \operatorname{Im} \{\boldsymbol {v} _ {n - 2} \}, \boldsymbol {v} _ {n - 1}, \boldsymbol {v} _ {n} \right]. \end{array}
$$

For illustrative purposes, above the new, unstable eigenpair that is created is indexed as 1 and 2, while two real eigenvalues that are characteristic of any swing dynamic model are indexed as n<sup>y</sup>1 and n. Then $\mathbf { F } \in \mathbf { R } ^ { m \times n }$ is constructed as:

$$
\mathbf {F} = \mathbf {W V} ^ {- 1}.
$$

With F as selected above, the results of Moore 6<sup>w</sup> <sup>x</sup> guarantee that the system with feedback, whose state matrix is given by Ž . A <sup>y</sup> BF , possesses the desired eigenvalue locations and eigenvector properties.

## 4. Predatory control with only local frequency measurements

The concept of using an observer to replace the full state feedback with output feedback based on local frequency measurements is unchanged from its treatment in Ref. 3 . As a brief review of the<sup>w</sup> <sup>x</sup> presentation there, we remind the reader of the key points. First, it is important to note that the separation principle, which is usually evoked in the context of eigenvalue placement, is unchanged in this more general setting of assigning eigenvalues and eigenvectors. The question as posed in Ref. 3 was the<sup>w</sup> <sup>x</sup> following: linking of the state feedback and the state estimator preserves the location of the ‘placed’ eigenÕalues; does it also preserve for those compo-Ž nents associated with original system states the. components of the eigenÕectors? The answer is indeed yes. The proof is a simple extension of standard textbook presentations see, for example, Ref. 1 , p. Ž <sup>w</sup> <sup>x</sup> 367 ..

For our application, the outputs to be measured could be one of two possibilities. If one presumes that the control group implements real time communication of measurements among themselves, one could take the measurements to be frequency deviation at all generators within the control group. This choice improves the degree of observability. It might be argued, however, that an unscrupulous competitor implementing predatory control would not want to leave ‘evidence’ of nonstandard governor control practice that might be suggested by inter-machine communication. In that case, each machine’s governor can implement its own state observer, operating only with local frequency measurement at that machine. Such a measurement does not make the system fully observable; in particular, phase angles become observable only up to a uniform shift. However, the observable subspace is sufficient to allow the eigenvector<sup>r</sup>eigenvalue placement that is the goal of predatory control. This issue was examined in detail, with examples of observer construction, in Ref. 4 .<sup>w</sup> <sup>x</sup>

## 5. 14-Bus test system example

To allow clear comparisons to the earlier work, our demonstrations here employ the same example as in Ref. 3 ; a slightly modified version of the<sup>w</sup> <sup>x</sup> Ž . IEEE 14-bus test system. Computations are performed using the MATLAB 5 package. A one line<sup>w</sup> <sup>x</sup> diagram for the system is provided in Fig. 1, with generators appearing at buses 1, 2, 3, 6, and 8. No infinite bus is employed. With zero station load attached to the terminal bus, one may assume that the terminal bus has been algebraically eliminated, so that these five buses represent the internal voltage of the machines. For the example here, a simple classical machine model is used in constructing the dynamic state description. Hence, the state dimension is 10, consisting of five generator frequency deviations ordered consistent with the bus number-Ž ing , and five machine angle deviations. For the first. case to be examined, assume the control group consists of the generators at buses 2 and 3, with the target group being the generators at buses 6 and 8.

![](/api/attachments/EMFFVB9K/fulltext/images/ff9fc23cb93b810fa6b0f81fb23a2d1e73ee9434dbc88cd20b1530367b7a8f91.jpg)  
Fig. 1. 14-Bus system one-line diagram.

Table 1  
Original modes of uncontrolled system

<table><tr><td colspan="2">Original, uncontrolled modes</td></tr><tr><td>Mode 1</td><td>-0.3127±23.2510i</td></tr><tr><td>Mode 2</td><td>-0.7378±14.2271i</td></tr><tr><td>Mode 3</td><td>-0.5542±10.2262i</td></tr><tr><td>Mode 4</td><td>-0.3138±12.1383i</td></tr></table>

The machine at bus 1 may be viewed as an ‘innocent bystander.

For the operating point and system data employed, the Ž . A, B matrices describing the linearized dynamics and the control input appeared in Ref. 3<sup>w</sup> <sup>x</sup> as Case 1.

Our heuristic for selecting the eigenvector to be destabilized may be briefly summarized as follows. We examine all the complex oscillatory modes of Ž . the system that exist before the application of feedback. We select a mode which meets two criteria: iŽ . the control group generators must have reasonable participation in the mode, where we will measure participation of a generator by examining the magnitude of its frequency state component within the right eigenvector for the mode in question; ii theŽ . target group generators should have significant participation in the mode. For our original, uncontrolled system, we have four oscillatory modes, defined by the eigenvalue pairs in units of radians per second Ž . shown in Table 1. The corresponding participation of generators in these original, uncontrolled modes is described in Table 2.

Table 2  
Participation factors of generators in uncontrolled modes

<table><tr><td rowspan="2"></td><td colspan="4">Generator participations in uncontrolled modes</td></tr><tr><td>Mode 1</td><td>Mode 2</td><td>Mode 3</td><td>Mode 4</td></tr><tr><td>Gen 1</td><td>0.4386</td><td>0.0793</td><td>0.2470</td><td>0.4457</td></tr><tr><td>Gen 2</td><td>0.8721</td><td>0.0307</td><td>0.1639</td><td>0.1426</td></tr><tr><td>Gen 3</td><td>0.1852</td><td>0.0185</td><td>0.1393</td><td>0.8705</td></tr><tr><td>Gen 4</td><td>0.0968</td><td>0.8967</td><td>0.3541</td><td>0.1141</td></tr><tr><td>Gen 5</td><td>0.0392</td><td>0.4284</td><td>0.8706</td><td>0.0585</td></tr></table>

We select mode 3 to be destabilized. Somewhat arbitrarily, we select the target eigenvalues after control to be the reflection of the original values about the j axis, so that the new mode to be created will be at $\lambda = + 0 . 5 5 4 2 \pm 1 0 . 2 2 6 2 i$

The construction of the corresponding $\mathbf { K } _ { \lambda }$ matrix follows by definition, and our objective function is determined by the quadratic form associated with the Hermitian matrix:

$$
\mathbf {Q} = \begin{array}{l l} 1. 4 4 4 9 + 0. 0 0 0 0 i & 1. 2 9 2 8 + 1. 1 0 1 0 i \\ 1. 2 9 2 8 - 1. 1 0 1 0 i & 2. 0 1 0 1 - 0. 0 0 0 0 i \end{array} .
$$

As noted earlier, the maximum value of the ratio of target machine participation to nontarget participation is the maximum eigenvalue of this matrix, equal to 3.449, with k obtained as a linear function of the associated principal direction:

$$
\boldsymbol {k} = \begin{array}{l} 0. 4 6 9 9 + 0. 4 3 0 8 i \\ 0. 7 7 0 2 - 0. 0 1 9 8 i. \end{array}
$$

This vector k defines the eigenvector associated with the new unstable mode, as shown in Table 3.

Table 3  
Eigenvector for unstable mode created by feedback control

<table><tr><td>Eigenvector for unstable mode</td></tr><tr><td>-0.1681 - 0.3147i</td></tr><tr><td>-0.1510 - 0.1369i</td></tr><tr><td>-0.1373 - 0.1869i</td></tr><tr><td>0.3739 - 0.1322i</td></tr><tr><td>0.7780 + 0.0728i</td></tr><tr><td>0.0298 - 0.0181i</td></tr><tr><td>0.0126 - 0.0154i</td></tr><tr><td>0.0175 - 0.0144i</td></tr><tr><td>0.0149 + 0.0358i</td></tr><tr><td>-0.0030 + 0.0762i</td></tr></table>

Table 4  
Participation factors of generators in unstable mode created by feedback control

<table><tr><td colspan="2">Generator participations in unstable mode</td></tr><tr><td>Gen 1</td><td>0.1273</td></tr><tr><td>Gen 2</td><td>0.0416</td></tr><tr><td>Gen 3</td><td>0.0538</td></tr><tr><td>Gen 4</td><td>0.1573</td></tr><tr><td>Gen 5</td><td>0.6106</td></tr></table>

To confirm the design goal, the participation of the generators in the unstable mode as measured byŽ the criterion defined earlier is shown in Table 4..

## 6. Conclusions

This paper has attempted to reinforced the case for concern regarding a potentially subtle form of strategic behavior that might be exercised by an unscrupulous group of generators, acting via their governor control. An algorithm has been demonstrated for constructing a linear governor control that selectively targets groups of generators outside theŽ control group to experience primary participation in. an unstable mode, while minimizing the participation of machines not in the targeted group. A simple numerical example was provided to illustrate the feasibility of the computations involved. As stressed in the introduction, the purpose of this presentation is to raise a warning flag: entities responsible for protecting system security may need to consider how to police against this type of anti-competitive behavior.

To the reader familiar with problems of parameter estimation and control, the general structure of the analysis presented here presents a troubling picture. In particular, if the entity seeking to police against this behavior is forced to operate from information available in standard system measurements e.g., theŽ types of RTU measurements that feed a typical state estimator, local frequency measurements, or even more sophisticated real-time phasor measurements ,. the problem of identifying the specific structure of governor control being exercised at various machines becomes a nonlinear parameter estimation problem. This is clearly true even when the underlying system and controller models are linearized, small signal equivalents about an operating point. Therefore, it is quite likely that policing against predatory control will be analytically a much more challenging problem than implementing it. This observation suggests that an entity responsible for system security may need policing powers that allow it to monitor internal controller performance at otherwise independent generating entities. Such policy issues await further investigation, should the risk discussed in this paper be judged a credible one.

## References

<sup>w</sup> <sup>x</sup> 1 C.-T. Chen, Linear System Theory and Design, Holt, Rinehart & Winston, New York, 1984.

<sup>w</sup> <sup>x</sup> 2 J.H. Chow, in: J.H. Chow, P.V. Kokotovic, R.J. Thomas Ž . Eds. , New Algorithms for Slow Coherency Aggregation of Large Power Systems, Systems and Control Theory for Power Systems, Springer-Verlag, New York, 1995.

<sup>w</sup> <sup>x</sup> 3 C.L. DeMarco, J.V. Sarlashkar, F.L. Alvarado, The potential for malicious control in a competitive power systems environment, Proc. IEEE Conference on Control Applications, Dearborn, MI, Sept. 18–20, 1996, pp. 462–467 first appeared as Ž University of Wisconsin-Madison, Department of Electrical and Computer Engineering Memorandum ECE-95-10, August 1995 ..

<sup>w</sup> <sup>x</sup> 4 T. Gorski, Malicious control of a power system through eigenvector placement, Master of Science Project Report, Department of Electrical and Computer Engineering, University of Wisconsin-Madison, December 1995.

<sup>w</sup> <sup>x</sup> 5 MATLAB User’s Guide, The MathWorks, Natick, MA, 1993.

<sup>w</sup> <sup>x</sup> 6 B.C. Moore, On the flexibility offered by state feedback in multivariable systems beyond closed loop eigenvalue assignment, IEEE Trans. Automatic Control, October 1976, pp. 689–692.

Christopher L. DeMarco received his SB in Electrical Engineering from MIT, in 1980, and his PhD in the same subject from the University of California, Berkeley in 1985. Since 1985, he has been a member of the faculty of the Department of Electrical and Computer Engineering, University of Wisconsin-Madison.
