---
otero_id: 17124
otero_key: "RPTS38PV"
title: "A streamlined approach for calculating expected utility and expected value of perfect information"
authors: "Bruce R. Hartsough; John L. Turner"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90010-o"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Streamlined Approach for Calculating Expected Utility and Expected Value of Perfect Information

Bruce R. HARTSOUGH

Agricultural Engineering Department, University of California, Davis, CA 95616, USA

John L. TURNER

Department of Mechanical Engineering, University of South Carolina, Columbia, SC 29208, USA

An approach based on the criteria of maximizing expected utility was developed for comparing alternatives, and the expected value of perfect information was incorporated to indicate the relative importance of uncertainty. Multi-dimensional Gauss quadrature was used to integrate over the uncertain variables. Problem characteristics were taken into account to subdivide utility functions, reducing the amount of computation when integrating utility. Additional factors were included to streamline the calculation of expected value of perfect information. Problems were taken from the literature to test the convergence rate of the method. The quadrature results converged quickly, although the rate depended on the type of probability distributions assigned to the variables.

Keywords: Expected utility algorithm; Perfect information value; Gauss quadrature; Convergence.

## 1. Introduction

This paper deals with some computational aspects of the decision analysis problem of selecting from alternative choices when uncertainties in the available information are to be considered. This situation arises frequently in the early stages of system design where the objectives of the system performance are specified but the influence and values of many variables are not known with certainty. For example, in designing an engineering system, say a piece of equipment, several alternative concepts might be initially considered. Each concept can be represented in terms of relevant system attributes (e.g., cost, productivity, reliability, expected life, user acceptability, etc.). The attributes might be ranked in relative importance to develop a characterizing “objective” or “utility” function to be maximized for evaluating and comparing the concepts. In the initial stages, the available information for ranking attributes is usually limited. Further, the attributes themselves are frequently expressible as functions of more basic variables of the problem, whose values may be known only approximately or within ranges. In the previous example for instance the basic variables might include geometric dimensions, material properties (strength, fatigue properties, mass density), materials cost per unit volume, etc. The problem of making a rational decision as to which alternative is best under such conditions has received relatively little attention. Also, the question

![](/api/attachments/RPTS38PV/fulltext/images/7c012b8373791ac90c4e6b9e11d9bbc22e63f5f5095b28e9c2288dee22bb238b.jpg)

Bruce Hartsough graduated in Forest Engineering from the University of California at Davis 1976. He joined Weyerhaeuser Company, evaluating and developing new systems for harvesting small trees, in Oklahoma, Washington and Oregon. In 1980, he returned to U.C. Davis as a development engineer, studying logging with helicopters and modeling cable yarders and systems. He received his Ph.D. in Agricultural Engineering at Auburn University in 1986. His current re-

search involves systems analysis of eucalyptus plantations, methods for harvesting timber on steep terrain and collection of forest residues for energy.

![](/api/attachments/RPTS38PV/fulltext/images/23316aa5fd11987e19637622fb2b35d03b31d6f4773a519be3ef83471a754d89.jpg)  
John Turner received his Ph.D. in Theoretical and Applied Mechanics from the University of Illinois in 1975. He has worked in numerous areas of engineering mechanics including composite materials, biomechanics, optical methods of stress analysis, finite element analysis and vehicle mobility modeling. His current research involves thermal strain analysis by digital imaging techniques.

of assessing the value of missing or uncertain information in reaching the right decision (selecting the best alternative) is an important one that needs study. For example, determining the merit of expending additional effort and dollars to collect more information about certain problem variables to assure that an optimum solution is not overlooked would be valuable information to the design process. Decision support systems which incorporate information uncertainty at the most basic levels of analysis and deal with the questions previously posed, are needed to make contemporary design processes fully effective. Clearly, such procedures would have applications in numerous other areas as well as design.

An attractive approach to selecting from alternative choices under uncertainty is the expected utility (EU) method [10]. This approach is viable when a utility function can be described in terms of attributes whose uncertain values can be characterized with probability distributions. In many cases, the decisionmaker can express the attributes as explicit functions of basic problem variables whose values are uncertain. Traditional decision support systems do not explicitly evaluate EU in such circumstances. Instead, other approaches such as dominance [19] and mean-variance methods [18] have been used. This has been largely due to difficulties in the required integration of the utility function over the ranges of the variables. Explicit evaluation of EU has several advantages, among them the ability to calculate the expected value of perfect information (EVPI) for each of the uncertain variables [25]. EVPI is an upper bound on the amount that may be spent in order to reduce uncertainty thus it can be used to decide whether to choose an alternative now or to collect more information.

This research effort addressed the problem of explicitly evaluating EU and EVPI.

## 2. Literature Review

In the decision analysis approach to selection, the utility function is determined, then the expected utility is explicitly calculated for each alternative [9]. The calculation of EU and EVPI involve multi-dimensional integration over the ranges of the variables. In most cases, the utility functions cannot be integrated analytically.

Several alternative approaches have been considered. Expanding a part of the integrand in a Taylor series has been widely used. The value of the function at the expected value of the variable is often taken as the first term in the Taylor expansion. The utility function has also been expanded about the means of state variables $[1,5,13]$ . Pulley $[18]$ expanded a logarithmic utility function to develop several mean-variance approximations. He noted criticism of the approach because the Taylor series does not converge for many situations to which it has been applied.

Pearson and Tukey [16] developed an empirical formula for the mean of a distribution, based on fractiles. Perry and Greig [17] suggested transforming to the utility function and evaluating the utility of the fractiles of an attribute. Then EU can be approximated with the Pearson and Tukey formula. More work with this formula has shown it to give good results in some situations [7,8], however, the formula requires knowing the fractiles of an attribute, which are not available if the attribute is modeled as a function of other uncertain quantities.

Numerical techniques involve evaluating (i.e., sampling) the integrand at some discrete number of m points over the integration range. Each evaluation is multiplied by an appropriate weighting factor and the weighted evaluations are summed to arrive at an approximation to the exact integral. Within a class of techniques, the error decreases as m increases [12]. The trapezoidal rule is a simple numerical integration technique and has been commonly used in decision analysis for integration over a single variable [15,21]. Unfortunately, the technique is not very efficient. Gauss quadrature rules optimize the locations of the sampling points and thus are more efficient than any others which use sums of weighted function evaluations [2].

Product rules for numerically integrating over multiple-dimensioned regions are developed from single-dimensioned rules. A one-dimension rule requiring m points forms the basis for an $m^{n}$ -point rule for the n-dimensional region. A limitation is the exponential growth of the number of evaluations that are required for multi-dimensional integration.

Monte Carlo sampling techniques have been advocated in the decision analysis field [10] due in part to their simple structure [22]. However, they converge very slowly compared to systematic methods. The average quasi-Monte Carlo method has been shown to given poorer results than the $2^{n}$ -point product Gauss quadrature rule for any number of variables n less than 108 [23]. The systematic techniques are generally preferable to Monte Carlo methods for many practical decision analysis problems.

Although several decision support systems have been developed for comparing discrete alternatives via the explicit EU approach [e.g., 11,20,21,26], they ignore several factors which are important in many situations. All assume that attributes are probabilistically independent, and none of them treat attributes as functions of more basic problem variables. None of the multiattribute packages consider EVPI, nor do they consider uncertainty about the utility function (except in after-the-fact sensitivity analysis).

## 3. Approach

## 3.1. Attributes and Utility Functions

Any selection problem can be represented with an objective function to be maximized. The attributes included in the objective function may be, for each alternative, functions of many uncertain quantities or variables.

This work was limited to utility functions of the linear additive form:

$$
U = \sum_ {i} C _ {i} A _ {i} (\underline {{{x}}}), \quad \text { where }\tag{1}
$$

$U =$ utility

$A_{i} =$ the value of the ith attribute, which is a function of the basic problem variables

$\underline{x} =$ the array of basic problem variables

$C_{i} =$ the value of the scaling coefficient for the $i$ th attribute

It was assumed that a decisionmaker could supply, for each alternative, the functions describing the attributes $A_{i}$ in terms of the basic variables. Each of these variables is assumed independent of all others.

In this work the coefficients $C_{i}$ are defined in terms of their ratio $r_{i}$ to the first coefficient $C_{1}$ . The coefficients are scaled such that they sum to unity. In previous work, the scaling coefficients have been assumed to have constant values. This has been drawback because a decisionmaker may be as uncertain about the trade-offs between attributes as about the other variables in the problem. In the current analysis the decisionmaker is permitted to assign a range to the possible values of the scaling coefficients by stipulating a range on the $r_{i}$ . The importance of reducing these uncertainties can be studied through the approach described herein.

## 3.2. Calculating Probability Distributions

To characterize the uncertainty of the basic problem variables each variable must be assigned a probability distribution. Jaynes [6] proposed maximizing entropy, subject to the constraints imposed by known information, as a criteria for choosing a distribution. His approach was shown to be correct when the distribution of prior information is uniform [4]. Three forms of maximum entropy distributions were employed to test convergence of the proposed numerical integration scheme: If only finite upper and lower bounds are known, the distribution is uniform; for any finite range and a specified mean of a problem variable the form is a truncated exponential; when a finite range, mean and variance are specified the distribution takes on a truncated normal form. A previously-developed method [24] to calculate the distribution coefficients was modified for this work.

## 3.3. Calculating Expected Utility

In theory, the utility function is integrated over the multidimensional region of uncertain variables, but this is frequently not feasible: the integrals usually can't be evaluated analytically and a large number of variables can make precise numerical integration computationally impractical. Two steps were taken to make the problem tractable: (1) an approach was developed to divide the integrand into small blocks, each of which could be integrated separately and (2) a computationally efficient multi-dimensional Gauss quadrature procedure was employed for the integrations.

For the ith alternative, expected utility is

$$
E U _ {i} = \int_ {\underline {{r}}} \int_ {\underline {{x}}} C _ {j} (\underline {{r}}) A _ {i j} (\underline {{x}}) \mathrm{d} \underline {{x}} \mathrm{d} \underline {{r}}, \quad \text { where }\tag{2}
$$

EU = the expected utility of the ith alternative

$C_{j}(\underline{r}) =$ the value of the scaling coefficient for the $j$ th attribute, which is a function of the vector $\underline{r}$ of scaling coefficient ratios

$A_{ij}(\underline{x}) =$ the value of the $j$ th attribute for the $i$ th alternative

x = the array of problem variables which influence the attributes.

The summation and integration operators can be exchanged and, since the scaling coefficient ratios r are assumed independent of the other variables x, the expected values of the scaling coefficients can be calculated separately. The expected utility can then be expressed as

$$
E U _ {i} = \sum_ {j} \left\{E [ C _ {j} ] \int_ {\underline {{x}}} A _ {i j} (\underline {{x}}) d \underline {{x}} \right\},\tag{3}
$$

where $E[C_{j}]$ is the expected value of the jth scaling coefficient.

The decisionmaker specifies the ranges of ratios for the coefficients. In addition, the coefficients must sum to one. Since the jth coefficient can be written as its ratio times the first coefficient $C_{1}$ , the unity constraint in terms of the ratios becomes

$$
C _ {1} + \sum_ {j = 2} ^ {a} r _ {j} C _ {1} = 1, \quad \text { where }\tag{4}
$$

$C_{j} =$ the scaling coefficient for the $j$ th attribute $r_j =$ the ratio of $C_j$ to $C_1$

$a =$ the number of attributes considered in the problem

For specific values of the scaling coefficient ratios, the scaling coefficients are

$$
C _ {1} = 1 / \left(1 + \sum_ {j = 2} ^ {a} r _ {j}\right), \quad \text { and }\tag{5}
$$

$$
C _ {j} = r _ {j} C _ {1} = r _ {j} / \left(1 + \sum_ {j = 2} ^ {a} r _ {j}\right) \quad \text { for } \quad j = 2 \text {   to   } a.\tag{6}
$$

To find the expected values of the coefficients, equations (5) and (6) must be integrated over the ranges of the ratios. It is efficient to integrate all of the coefficients simultaneously.

A product Gauss quadrature approach was also used to evaluate the expected values of the attributes. An existing algorithm [2] was used to generate the quadrature points and weights. The expected value of attribute $A_{ij}$ is:

$$
E \left[ A _ {i j} \right] = \int A _ {i j} (\underline {{{x}}}) p (\underline {{{x}}}) d \underline {{{x}}}, \quad \text { where }\tag{7}
$$

$E[A_{ij}]=$ the expected value of the jth attribute for the ith alternative

$p(\underline{x}) =$ the probability density for the variables $\underline{x}$

One approach to evaluating $E[A_{ij}]$ is direct numerical integration of the function $f(\underline{x})$ where $f(\underline{x}) = A_{ij}(\underline{x}) p(\underline{x})$ . (8)

This approach converged rapidly for cases where the probability distributions were uniform or rather broad. For peaked distributions where variables had high probabilities of occurring within very small segments of the ranges, the approximations fluctuated and converged very slowly. In theory, the slow convergence is due to the large values of higher derivatives of $p(\underline{x})$ for very peaked distributions. Practically, the problem arises because few of the quadrature sampling points are located within the high probability region of the variable space.

Another choice of integrand was made to improve the rate of convergence. The cumulative probability distribution $G(x)$ is defined for a single variable as

$$
G (x) = \int_ {a} ^ {x} p (x) d x,\tag{9}
$$

where a is the lower bound for variable x.

The differential $\mathrm{d}G$ is $p(x)\mathrm{d}x$ , and substituting into (8), gives, for the single-dimensional case

$$
\begin{array}{r l} E \left[ A _ {i j} \right] & = \int_ {G (a)} ^ {G (b)} A _ {i j} (x (G)) \mathrm{d} G \\ & = \int_ {0} ^ {1} A _ {i j} (x (G)) \mathrm{d} G. \end{array}\tag{10}
$$

The variable of integration is now the cumulative probability G, and the integrand includes only the attribute function. Gauss quadrature can be applied to this integrand as long as $x(G)$ can be evaluated. This function can be found analytically for the uniform and truncated exponential distributions, but a numerical approach was required for the truncated normal distribution.

Integrating over the cumulative probability rather than over the variable x significantly improved the convergence for peaked distributions. Fig. 1 compares results for a single problem solved by each of the two approaches.

When the utility function is described as a linear combination of attributes, the EU of the ith alternative can be written as

$$
E U _ {i} = \sum_ {j} E [ C _ {j} ] E [ A _ {i j} (\underline {{x}}) ].\tag{11}
$$

![](/api/attachments/RPTS38PV/fulltext/images/3b971a02e37dfdd0a3bcbd83ca1cb5b1617664175df2a4324a5eba681f47e917.jpg)  
Fig. 1. Comparison of Convergence for Integration over the Cumulative Densities Versus Integration over the Variable Ranges.

Each of the attributes for each alternative may be a function of many variables. The integration to find the expected value of an attribute is not tractable unless the function includes approximately ten or fewer variables. However, in many cases, the integration can be subdivided into two or more smaller problems by taking advantage of two properties of the expectation operator

$$
\begin{array}{l l} E [ a + b ] = E [ a ] + E [ b ] & \text { and } \\ E [ c * d ] = E [ c ] * E [ d ] & \text { if   } c \text {   and   } d \text {   are } \\ & \text { independent }, \end{array}\tag{12}
$$

(13)

where $a, b, c,$ and $d$ are general quantities. Since the expected value of each attribute is required in order to calculate expected utility, equations (12) and (13) are applied to the functions which describe each attribute for each alternative. An algorithm was developed which insures that all possible subdivisions are made. First, operations are carried out algebraically as far as possible, eliminating as many parentheses as possible from the attribute function. For example, the function fragment $((a + b)*(c + d))$ is written as $(ac + ad + bc + bd)$ . The function is separated into its additive components and each of these is separated into multiplicative fragments. Since each element of the variable vector $\underline{x}$ is assumed independent of every other, a fragment is independent of the others if the variables included in the fragment do not occur in any of the others. The fragments are grouped into blocks which have common variables occurring in two or more fragments. These blocks represent the smallest possible subdivisions of the attribute function. The algorithm, flowcharted in fig. 2, was carried out manually for the test problems, however, it could be done symbolically within a decision support system.

Each attribute is now described as a sum of products of independent blocks, so the expected value of an attribute is

$$
E \left[ A _ {i j} \right] = \sum_ {l = 1} ^ {p} \prod_ {m = 1} ^ {q} E \left[ b _ {i j l m} \right]\tag{14}
$$

and the expected value of each block is evaluated by numerically integrating

$$
E \left[ b _ {i j l m} \right] = \int b _ {i j l m} \left(\underline {{{x}}} _ {B}\right) p \left(\underline {{{x}}} _ {B}\right) d \underline {{{x}}}, \quad \text { where }\tag{15}
$$

$$
\begin{array}{l} E [ b _ {i j l m} ] = \text { the   expected   value   of   block } b _ {i j l m} \\ \underline {{x}} _ {B} = \text { the   subset   of } \underline {{x}} \text { included   in   the   block } \end{array}
$$

Subdivision can make many large problems tractable. An ideal division would break a problem with n variables into q blocks, each with n/q variables. Using m sampling points per variable in a product Gauss quadrature scheme, only $q * m^{(n/q)}$ integrand evaluations are required for the subdivided problem, versus $m^{n}$ for the complete case. For example, if a problem with 20 variables and 10 integration points per variable is divided into 4 blocks with 5 variables each, the number of evaluations is reduced from $10^{20}$ to $4 \times 10^{5}$ .

For a single alternative, the blocks which make up its attributes are identified. For each block, the associated variables are next identified and arrays of quadrature points and weights are generated. Then the product Gauss routine is used to calculate the expected value of the block. After all blocks have been considered, the expected values of the attributes are calculated and combined with the scaling coefficient values, returning EU for the alternative. The framework is flowcharted in fig. 3.

## 3.4. Calculating EVPI

In theory, the best alternative is identified at each possible value of the variable. This alternative is termed the conditional best. The difference between the utility of the conditional best and that of the unconditional best is the loss if that specific value of the uncertain variable were actually to occur. This loss function is integrated over the probability distribution of the variable to give the EVPI.

![](/api/attachments/RPTS38PV/fulltext/images/86364e6c30debb56a4c9fb3a58943b236c8a864843fbf7ba231943444fb7ba58.jpg)  
Fig. 2. Algorithm to Subdivide Attribute Functions into Smaller Blocks.

The EVPI concerning variable k can be written as

$$
\begin{array}{r l} E V P I _ {k} & = \int_ {a _ {k}} ^ {b _ {k}} p (x _ {k}) \\ & \times \underset {i} {\text { Max }} \left\{\int_ {\underline {{x}} \ddagger x _ {k}} (U _ {i} (\underline {{x}}) - U _ {*} (x)) p (\underline {{x}}) \mathrm{d} \underline {{x}} \right\} \mathrm{d} x _ {k}, \end{array}\tag{16}
$$

where

$a_{k}, b_{k} =$ the lower and upper bounds for variable $x_{k}$

$U_{i}(\underline{x}) = \text{the utility function for the } i \text{th alternative}$ The star subscript denotes the unconditional best alternative, i.e., the one with the largest $EU$ . The integrand for the outer integration loop is the loss function.

Two problems hinder the calculations. Since the best alternative must be found at each point over the range of the variable, the number of function evaluations to calculate EVPI for a single variable is roughly the same as are required to find the EU's of all the alternatives, if no special characteristics of the problem are taken into account. Most problems deal with many more variables than alternatives, so the time requirements for EVPI calculations typically exceed those for EU by at least an order of magnitude. Secondly, the loss function is piecewise continuous, with a separate segment for each alternative that is best over some part of the range of the variable (fig. 4 displays a hypothetical example). The first and higher derivatives are not continuous at the segment junctions, so a high-order integration scheme is required in the outer loop to achieve precise results.

![](/api/attachments/RPTS38PV/fulltext/images/057b975dff681c5c851cd25a05eef8d6e832a3e1207bc42575e50fd92d08bc02.jpg)  
Fig. 3. Algorithm to Calculate EU of an Alternative.

To reduce the time requirements and eliminate the discontinuity problem, an initial screening is performed to identify the endpoints of and conditional best alternatives on each segment. Then the actual integration is carried out for each segment, considering only the conditional best alternative and the unconditional best. Rewriting in terms of the segments

![](/api/attachments/RPTS38PV/fulltext/images/97e190a612510fadebd4b5f70dd76d8d533cb709a5ad335ae2d46567c65a74e4.jpg)  
Fig. 4. Utility Functions for Three Alternatives, and the Piecewise Loss Function Assuming Alternative 2 is the Unconditional Best Alternative.

$$
\begin{array}{r l} E V P I _ {k} & = \sum_ {h} \int_ {a _ {k h}} ^ {b _ {k h}} p (x _ {k}) \\ & \times \int_ {\underline {{x}} \neq x _ {k}} \left(U _ {B h} (\underline {{x}}) - U _ {*} (\underline {{x}})\right) p (\underline {{x}}) d \underline {{x}} d x _ {k}, \end{array}\tag{17}
$$

where the Bh subscript indicates the alternative which is best on segment h, $a_{kh}$ and $b_{kh}$ are the lower and upper endpoints of the segment. As with the EU calculations, the results for Gauss quadrature are more precise when the cumulative probability is substituted for the actual variable in the integrand

$$
\begin{array}{r l} E V P I _ {k} = \sum_ {h} \int_ {G (a _ {k h})} ^ {G (b _ {k h})} \int_ {\underline {{G}} \ddagger G _ {k}} \left(U _ {B h} (\underline {{x}} (\underline {{G}}) - U _ {*} (x (G))\right) d \underline {{G}} d G _ {k}. \end{array}\tag{18}
$$

On each segment, the integral can be multiplied and divided by the integral of the cumulative probability differential over the segment

$$
\begin{array}{r l} E V P I _ {k} & = \sum_ {h} \int_ {G (a k h)} ^ {G (b k h)} \mathrm{d} G \frac {1}{\int_ {G (a k h)} ^ {G (b k h)} \mathrm{d} G} \\ & \quad \times \int_ {\underline {{G}} \ddagger G _ {k}} \left(U _ {B h} (\underline {{x}} (\underline {{G}})) - U _ {*} (\underline {{x}} (\underline {{G}}))\right) \mathrm{d} \underline {{G}} \mathrm{d} G _ {k}. \end{array}\tag{19}
$$

But the first integral is just the probability of the variable occurring within the segment, and the remaining integral can be carried out in two parts, giving the difference in EU between the two pertinent alternatives on the segment. This results in

$$
\begin{array}{r l} E V P I _ {k} = \sum_ {h} \left\{\left(G (b _ {k h}) - G (a _ {k h})\right) \right. \\ & \times \left(E _ {h} [ U _ {b h} ] - E _ {h} [ U _ {*} ]\right) \}, \end{array}\tag{where}
$$

(20)

$G(b_{kh}), G(a_{kh}) =$ the cumulative probability values for variable $x_{k}$ at the upper and lower bounds of loss segment $h$

$E_{h}[U_{Bh}]$ = the $EU$ , on segment $h$ , of the conditional best alternative

$E_{h}[U_{*}]$ = the $EU$ , on segment $h$ , of the unconditional best alternative

![](/api/attachments/RPTS38PV/fulltext/images/57fc42c354ab94f46199fc1dd3a12c5bad388ddfa9629dec1b4fd55657febc60.jpg)  
Fig. 5. Algorithm to Calculate EVPI for a Variable.

This shows that the integration on a segment develops the expected loss on the segment, weighted by the probability of the variable occurring within the segment.

A bisection routine is used to identify the segments of the loss function for the EVPI variable, continuing until the remaining distance between the search bounds for a segment transition is less than a prespecified tolerance, stated as a fraction of the range of the EVPI variable. Initially, the search bounds are set at the lower and upper bounds of the range of the variable. The best alternatives at these endpoints are identified. If both are the same as the unconditional best alternative, it is assumed that no other alternative has greater conditional utility at any point over the range of the variable, i.e. the EVPI is zero. This assumption has been found to be valid in the test problems analyzed thus far. Theoretically, there could be exceptions requiring the loss function to be evaluated at more points.

Characteristics of individual problems are considered in order to reduce the number of calculations. The alternatives are checked to identify those which do not depend on the EVPI variable. The alternative from this group with the greatest EU is considered the “base” alternative: its EU is a lower bound on conditional best EU. The rest of the unaffected alternatives can then be ignored.

Some of the blocks making up the attribute functions of the dependent alternatives may not include the EVPI variable. Since their conditional expected values are constant, the blocks do not have to be re-integrated at each value of the EVPI variable. These blocks are identified and their expected values placed in a working array of conditional block values.

At any specified value of the EVPI variable, the calculation of conditional EU's for the dependent alternatives reduces to integrating the dependent blocks over the ranges of the rest of the variables. The conditional block values are stored in the working array, then the conditional values of the attributes are calculated using the problem-specific attribute function. Finally, the utility routine is called to sum the attributes, premultiplied by the expected values of the scaling coefficients.

The unconditional best alternative is the conditional best on one or more of the segments of the range of the EVPI variable. No integration is required on these segments, as the loss and contribution to EVPI is zero.

The overall procedure for calculating EVPI of a variable is flowcharted in fig. 5. During the final integration over a segment, the product Gauss routine is used to determine the expected values of the pertinent blocks on the segment. The EU's on the segment are evaluated, then combined using equation (20) to arrive at EVPI.

A computer program incorporating the algorithms described above was written in Microsoft Fortran Version 3.0 [14], for an IBM Personal Computer with an 8087 coprocessor.

## 4. Convergence Testing

The algorithms were evaluated on a number of problems to determine the convergence characteristics of the EU and EVPI solutions as the number of quadrature points was increased. Each problem was run with one through nine integration points over the range of each variable.

Factors which were considered as having possible impacts on the convergence of the quadrature algorithms included (a) the size of the problem, indicated by the number of variables, (b) the problem structure, indicated by the block size (variables per block), (c) the level of uncertainty, as measured by the ranges of the variables, and (d) the type of distribution (uniform, exponential or normal) assumed for the variables.

Test problems were taken from the published literature on the comparison of forest harvesting systems or components. To facilitate algorithm testing, supplemental data were generated for the problems, as necessary, in order to vary the levels of the factors listed above. The test problems are described in detail in reference 3.

## 4.1. Expected Utility Convergence

Thirty-two alternatives were chosen for the analysis, half from small problems (10 variables) with small blocks (one variable per block). The rest were from large problems (70 variables), with five variables per block. All combinations of range and distribution type were represented.

Regression analysis was used to quantify the rates of convergence. The convergence response variable was

$$
L O G E R _ {E U m} = \log_ {1 0} | (E U _ {Q m} - E U _ {Q 9}) / E U _ {Q 9} |,\tag{21}
$$

where

$\text{LOGER}_{\text{EUm}} = \text{the logarithm of the magnitude of the relative error in expected utility, evaluated with m quadrature points}$

$EU_{Qm}$ = the expected utility result for m quadrature points

$EU_{Q9}$ = the results for 9 quadrature points
The number of variables and size of the blocks had no significant effect on the rate of convergence, nor did the relative range of the variables. The only important factor was the form of probability distribution: no significant difference was found between the convergence rates for the exponential and truncated normal situations, but the cases with uniform distributions converged at a higher rate:

$$
\begin{array}{l l} & \underline {{F}} \\ L O G E R _ {E U m} = & - 2. 0 4 8 \\ & - 0. 3 6 2 m \\ & - 0. 6 7 6 m U N I F \end{array} \quad \begin{array}{l l} & 1 0 6. 0 \\ & 1 2 4. 0 \end{array}\tag{22}
$$

$$
N = 2 2 2, \quad R ^ {2} = 0. 4 9,
$$

where

$$
U N I F = \left\{ \begin{array}{l l} 1 & \text { if   variable   distributions   were } \\ & \text { uniform, } \\ 0 & \text { otherwise. } \end{array} \right.
$$

This relationship, along with the data points, is plotted in fig. 6. The poorer performance with the non-uniform distributions may be attributed to the less-smooth utility functions when described in terms of the cumulative variables G. Since the precision of the Gauss quadrature approach depends on the higher derivatives of the utility function, situations with exponential and truncated normal distributions have inherent disadvantages over the uniform cases.

Even though the quadrature method did not converge as quickly for the non-uniform situations, it still gave good results in most cases (compared with the results at nine quadrature points).

![](/api/attachments/RPTS38PV/fulltext/images/457ce5b2ea812ea2cc96bfa027d2f3671216c84bd09af2612225e578166332f8.jpg)  
Fig. 6. Regression Relationships for Convergence of EU, Plotted with the Means of the Data for the Uniform and Other Distributions.

When eight points were used, the maximum relative error for any of the test problems was only 0.8 percent.

Much of the variation in convergence was not explained by any of the factors considered in the analysis. This variation is due to differences in mathematical form of the attribute functions, which are not readily quantifiable.

## 4.2. EVPI Convergence

Data were collected on eight variables, four with uniform distributions and four with truncated normal distributions. When searching for segments of the loss function, a tolerance of $10^{-4}$ gave excellent results. Tighter tolerances changed the EVPI figures by less than 0.01 percent.

Convergence over the number of quadrature points was evaluated with search tolerance set at $10^{-4}$ . The dependent variable was

$$
\begin{array}{r l} L O G E R _ {E V P I m} & = \log_ {1 0} | (E V P I _ {Q m} - E V P I _ {Q ^ {9}}) \\ & / E V P I _ {Q ^ {9}} |, \quad \text { where } \end{array}\tag{23}
$$

$$
\begin{array}{l} \text {LOGER} _ {E V P I m} = \text {the logarithm of the magnitude of} \\ \text {the relative error in EVPI,} \\ \text {evaluated with m quadrature} \\ \text {points} \end{array}
$$

$EVPI_{Qm}$ = the EVPI result for m quadrature points

$$
E V P I _ {Q 9} = \text { the   result   for   9   quadrature   points }
$$

Trends were similar to those for EU. Cases with uniform distributions converged significantly faster than those with truncated normal distributions:

F

$$
\begin{array}{r l} L O G E R _ {E V P I m} = & - 0. 7 6 0 \\ & - 0. 2 5 4 m \\ & - 1. 8 6 8 m U N I F \end{array}\tag{24.6}
$$

391.0

$$
n = 4 5, \quad r ^ {2} = 0. 9 0.\tag{24}
$$

In the worst cases, EVPI results did not converge as quickly as those for EU. This may be due to the piecewise nature of the loss functions and the errors associated with finding the ends of the loss function segments. However, the maximum error in EVPI with eight quadrature points was only three percent when compared with the result using nine points.

## 5. Conclusions

A practical method for calculating expected utility (EU) of alternative choices and expected value of perfect information (EVPI) was developed and tested. The algorithm is computationally efficient and can make an otherwise intractable calculation feasible. Example problems with up to 70 variables and up to five uncertain variables per block were effectively analyzed on a math coprocessor-equipped IBM PC. The method converged quickly for all of the test problems. The developed methodology permits consideration of uncertain information in decision analysis in a novel fashion.

## References

[1] S.E. Bodily, A Multiattribute Decision Analysis for the Level of Frozen Blood Utilization, IEEE Transactions SMC-7, Nr. 10 (1977) 683–694.

[2] P.J. Davis and P. Rabinowitz, Methods of Numerical Integration (Academic Press, New York, 1985).

[3] B.R. Hartsough, Evaluation of Alternatives Considering Uncertainty with Examples in Forest Harvesting, Auburn University Doctoral Dissertation (Univ. Microfilms, Ann Arbor, 1986).

[4] A. Hobson and B.K. Cheung, A Comparison of the Shannon and Kullback Information Measures, Journal of Statistical Physics 7, Nr. 4 (1973) 301–310.

[5] R.A. Howard, Proximal Decision Analysis, Management Science 17, Nr. 9 (1971) 507–541.

[6] E.T. Jaynes, Information Theory and Statistical Mechanics I, Physics Revue 106 (1957) 620–630.

[7] D.L. Keefer, Allocation Planning for R and D with Uncertainty and Multiple Objectives, IEEE Transactions M-25, Nr. 1 (1978) 8–14.

[8] D.L. Keefer and S.M. Pollock, Approximations and Sensitivity in Multi-objective Resource Allocation, Operations Research 28, Nr. 1 (1980) 114–128.

[9] R.L. Keeney, Decision Analysis: An Overview, Operations Research 30, Nr. 5 (1982) 803–838.

[10] R.L. Keeney and H. Raiffa, Decision With Multiple Objectives: Preferences and Value Tradeoffs (Wiley, New York, 1976).

[11] R.L. Keeney and A. Sicherman, An Interactive Computer Program for Assessing and Analyzing Preferences Concerning Multiple Objectives, Behavioral Science 21, Nr. 3 (1976) 173–182.

[12] J.N. Lyness, Quid, Qou, Quadrature?, In: D. Jacobs, Ed., The State of the Art in Numerical Analysis (Academic Press, London, 1977).

[13] M.W. Merkhofer, The Value of Information Given Decision Flexibility, Management Science 23, Nr. 7 (1977) 716–727.

[14] Microsoft Corporation, FORTRAN Compiler for the MS-DOS Operating System, Version 3.0 (Microsoft Corporation, Bellevue, 1984).

[15] A.C. Miller, M.W. Merkhofer, R.A. Howard, J.E. Matheson and T.R. Rice, Development of Automated Aids for Decision Analysis, Technical Report 3309 (SRI International, Menlo Park, 1976).

[16] E.S. Pearson and J. Tukey, Approximating Means and Standard Deviations Based on Distances Between Percentage Points of Frequency Curves, Biometrika 52 (1965) 533–546.

[17] C. Perry and I.D. Greig, Estimating the Mean and Variance of Subjective Distributions in PERT and Decision Analysis, Management Science 21, Nr. 12 (1975) 1477–1480.

[18] L.B. Pulley, Mean-Variance Approximation to Expected Logarithmic Utility, Operations Research 31, Nr. 4 (1983) 685–696.

[19] A.P. Sage and C.C. White, ARIADNE: A Knowledge-Based Interactive System for Planning and Decision Support, IEEE Transactions SMC-14, Nr. 1 (1984) 35–47.

[20] M. Sakawa and F. Seo, Integrated Methodology for Computer-Aided Decision Analysis, In: R.T. Trappl, F. De P. Hanika and R. Tomlinson, Eds., Progress in Cybernetics and Systems Research, Volume X (Hemisphere, Washington, 1982).

[21] R. Schlaifer, Computer Programs for Elementary Decision Analysis (Graduate School of Business, Harvard University, 1971).

[22] I.M. Sobol, The Monte Carlo Method (University of Chicago Press, Chicago, 1974).

[23] A.H. Stroud, Approximate Calculation of Multiple Integrals (Prentice-Hall, Englewood Cliffs, 1971).

[24] M. Tribus, Rational Descriptions, Decisions and Designs (Pergamon Press, New York, 1969).

[25] R.E. Trueman, An Introduction to Quantitative Methods for Decision-Making (Holt Rinehart and Winston, New York, 1974).

[26] Woodward-Clyde Consultants, Decision Framework for Technology Choice - Volume 2: Decision Analysis Users' Manual, Report EA-2153 (Electric Power Research Institute, Palo Alto, 1982).
