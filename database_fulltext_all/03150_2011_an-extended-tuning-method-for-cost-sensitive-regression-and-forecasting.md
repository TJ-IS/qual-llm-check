---
otero_id: 3150
otero_key: "VEBX67UK"
title: "An extended tuning method for cost-sensitive regression and forecasting"
authors: "Huimin Zhao; Atish P. Sinha; Gaurav Bansal"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.01.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An extended tuning method for cost-sensitive regression and forecasting

Huimin Zhao <sup>a,</sup>⁎, Atish P. Sinha <sup>a</sup>, Gaurav Bansal <sup>b</sup>

<sup>a</sup> Sheldon B. Lubar School of Business, University of Wisconsin–Milwaukee, P. O. Box 742, Milwaukee, WI 53201–0742, United States <sup>b</sup> University of Wisconsin–Green Bay, 2420 Nicolet Dr., Green Bay, WI 54311–7001, United States

## a r t i c l e i n f o

Article history: Received 15 March 2010 Received in revised form 27 December 2010 Accepted 20 January 2011 Available online 26 January 2011

Keywords: Data mining Cost-sensitive regression Asymmetric loss Post-hoc tuning Loan charge-off forecasting

## a b s t r a c t

In many real-world regression and forecasting problems, over-prediction and under-prediction errors have different consequences and incur asymmetric costs. Such problems entail the use of cost-sensitive learning, which attempts to minimize the expected misprediction cost, rather than minimize a simple measure such as mean squared error. A method has been proposed recently for tuning a regular regression model post hoc so as to minimize the average misprediction cost under an asymmetric cost structure. In this paper, we build upon that method and propose an extended tuning method for cost-sensitive regression. The previous method becomes a special case of the method we propose. We apply the proposed method to loan charge-off forecasting, a cost-sensitive regression problem that has had a bearing on bank failures over the last few years. Empirical evaluation in the loan charge-off forecasting domain demonstrates that the method we have proposed can further lower the misprediction cost signi<sup>fi</sup>cantly

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

Real-world classi<sup>fi</sup>cation and regression problems [3,7,8,37] are often characterized by asymmetric costs (losses), which are associated with different types of prediction errors. For example, to a banking regulatory authority, incorrectly classifying a failing bank as a sound one has more serious consequences than raising a false alarm on a healthy bank [28,30]. To a real estate assessor, overestimating the value of a house incurs heavier costs to the assessor's of<sup>fi</sup>ce than underestimating the house value by the same amount [34]. Such problems entail the use of cost-sensitive learning, which attempts to minimize the expected cost due to misprediction errors, rather than minimize simple measures such as error rate (in classi<sup>fi</sup>cation) and mean squared error (in regression).

Most research on cost-sensitive learning in the data mining literature has focused on classi<sup>fi</sup>cation problems [33]. There are in general two approaches to cost-sensitive classi<sup>fi</sup>cation [42]. One is to account for the asymmetric costs prior to or during model learning, by assigning appropriate weights on different training examples [15,24,32,38] or directly modifying the objective function or learning algorithm [16,18,20,41]. The other is to tune, in a post-hoc manner, the decision threshold of a model learned by a regular learning method [1,17,29].

Regression under asymmetric losses has been studied mainly in the statistics <sup>fi</sup>eld. Much of this research has focused on correcting classical statistical regression methods, such as linear least squares, under particular asymmetric loss functions, such as LinLin (asymmetric linear), QuadQuad (asymmetric quadratic), LinEx (approximately linear on one side and exponential on the other side), and SquarEx [31,39]. While some deliberately designed loss functions, such as LinEx and SquarEx, lead to closed-form solutions, the optimal predictor under general loss structures typically does not exist in closed form, thus entailing numeric solutions or approximations (in either the predictor or the loss function) [10,11].

Recently, inspired by the post-hoc tuning method for costsensitive classi<sup>fi</sup>cation, Bansal et al. [4] proposed a method for tuning a regular regression model so as to minimize average misprediction cost under an asymmetric cost structure. This method adjusts the prediction of a regular regression model by a certain amount. The amount of adjustment that minimizes average misprediction cost, given the regular regression model, is found using a hill-climbing search algorithm. This method can deal with general cost structures and does not require modifying the underlying learning method. This is a big advantage for organizations that operate in dynamic environments where the shape and parameters of the cost structure could change over time. Empirical evaluation in the domain of bank loan charge-off forecasting shows that this tuning method signi<sup>fi</sup>- cantly reduces the average misprediction costs of models trained with several regression methods, including linear least squares, model tree, and backpropagation neural network.

In this paper, we propose an extended tuning method, which <sup>fi</sup>nds a polynomial function of the prediction of a regular regression model to make the <sup>fi</sup>nal cost-sensitive prediction. We also propose an iterative hill-climbing algorithm for <sup>fi</sup>nding the optimal coef<sup>fi</sup>cients of polynomial tuning functions. The method of Bansal et al. [4] becomes a special case of the new method, where the tuning function is linear and has a <sup>fi</sup>xed unit coef<sup>fi</sup>cient on the term of degree one. We have also empirically evaluated our proposed method in the domain of bank loan charge-off forecasting. The results demonstrate signi<sup>fi</sup>cant further performance improvement of the new method over its predecessor.

The rest of the paper is organized as follows. In the next section, we brie<sup>fl</sup>y review the related literature. We then brie<sup>fl</sup>y describe some necessary background and the tuning method proposed by Bansal et al. [4]. We next propose the extended tuning method and present the results of the empirical evaluation. Finally, we conclude the paper with a discussion of managerial implications and potential future research directions.

## 2. Literature review

In this section, we review the relevant literature on cost-sensitive learning for classi<sup>fi</sup>cation and regression problems. There is a large body of research on cost-sensitive learning for classi<sup>fi</sup>cation problems in the data mining <sup>fi</sup>eld. Several cost-sensitive classi<sup>fi</sup>cation methods have been proposed. Some of them extend particular basic classi<sup>fi</sup>- cation methods, which rely on symmetric performance measures. Fan et al. [18] proposed the AdaCost algorithm, which turns the AdaBoost algorithm into a cost-sensitive boosting method. Gama [20] proposed the Iterative Bayes method, which modi<sup>fi</sup>es Naïve Bayes to accommodate asymmetric cost structures. Drummond and Holte [16] proposed methods for cost-sensitive decision tree learning. Zhao [41] proposed a method for simultaneously building a set of alternative decision trees, each of which excels under a particular cost setting.

Besides such methods for extending particular classi<sup>fi</sup>cation methods, there are two generic approaches for converting any classi<sup>fi</sup>cation method into a cost-sensitive one: instance weighting and post-hoc tuning. Such methods are called meta methods and have broader applicability than those extending particular regular classi-<sup>fi</sup>cation methods. The instance weighting approach [15,24,32,38] weights different types of training instances based on the (asymmetric) cost structure prior to classi<sup>fi</sup>er training. This is similar to instance re-sampling (over-sampling or under-sampling) [9]. The classi<sup>fi</sup>er training method is not modi<sup>fi</sup>ed, but as fewer errors are made on the more costly type, the overall misclassification cost is lowered. The post-hoc tuning approach [1,17,29] does not modify the training data or the training method and only adjusts (tunes) the trained classi<sup>fi</sup>er. This approach follows two steps. It <sup>fi</sup>rst learns a regular cost-neutral classi<sup>fi</sup>er without considering the actual asymmetric cost structure. It then relies on the posterior class probabilities predicted by the base classi<sup>fi</sup>er and <sup>fi</sup>nds decision thresholds that minimize the average misclassi<sup>fi</sup>cation cost.

Zhao [42] showed that the two approaches lead to similar results for some base classi<sup>fi</sup>cation methods, such as Naïve Bayes, and quite different results for other methods, such as decision trees. The instance weighting approach is computationally more involved than the posthoc tuning approach, especially in dynamic environments where the cost structure could change over time, because then instance weighting requires model retraining whereas post-hoc tuning does not.

It has long been recognized that regression problems—like classi<sup>fi</sup>cation problems—can be characterized by asymmetric losses too (e.g., [2,5,19,22,34,40]) and it is inappropriate to “blindly trust in squared error loss” [39], although the main results of this literature are relatively recent [25]. Among others, Varian [34] presented one of the earliest studies of cost-sensitive regression. The particular problem studied was that of real estate assessment. Real estate assessors need to routinely estimate current market values of taxable properties based on the values of certain characteristics of the properties. Overestimates and underestimates incur different losses accruing to the assessor's of<sup>fi</sup>ce. In case of an underestimate, the loss is equal to the amount of estimation error. However, in case of overestimates, the assessor's of<sup>fi</sup>ce may be faced with complaints or appeals, which entail lengthy expensive procedures to resolve. Varian [34] suggested that the symmetric quadratic loss function of ordinary least squares procedures, which had been applied in practice, was inappropriate and proposed the LinEx loss function as an alternative. This loss function has approximately exponential losses for large overestimates and approximately linear losses for large underestimates. In a related but different context, that of property valuation by a real estate agent, Cain and Janssen [6] applied LinLin, QuadQuad, and LinEx loss functions. Zellner [39] derived optimal estimators and predictors relative to Varian's LinEx loss function for a number of wellknown models. Thompson and Basu [31] generalized Varian's LinEx to SquarEx, which has approximately quadratic losses for large underestimates and approximately exponential losses for large overestimates and includes LinEx as a special case.

Although closed-form solutions have been found for a few special cases, such as LinEx and SquarEx, it has been proven that an optimal predictor under general loss structures does not exist in closed form [10,11]. Numeric or approximate solutions are therefore needed for general loss functions. Christoffersen and Diebold [11] proposed an approximately optimal predictor via series expansions. With a different and complementary approach, Christoffersen and Diebold [10] proposed a method for <sup>fi</sup>nding the exactly optimal predictor for an approximate loss function, instead of approximating the optimal predictor for the exact loss function. This method approximates a general loss function by a piecewise-linear loss function, which is constructed by concatenating linear segments.

In addition to the extensive research on cost-sensitive regression published in the statistics literature, a few publications (e.g., [4,12,13,33]) have appeared in the data mining literature. Crone [12] and Crone et al. [13] proposed a modi<sup>fi</sup>ed back-propagation neural network training method, which assumes a LinLin cost function rather than the squared error cost used in the standard method. Torgo and Ribeiro [33] proposed a case-speci<sup>fi</sup>c, costsensitive performance measure, which is not just a function of the prediction error, but a function of the actual and predicted target values, and empirically compared a few standard regression methods using this measure. However, they did not suggest any method for optimizing or improving this performance measure.

While all previous methods for cost-sensitive regression try to directly learn a model under the actual asymmetric cost structure, the post-hoc tuning method recently proposed by Bansal et al. [4]—like the post-hoc tuning method for cost-sensitive classi<sup>fi</sup>cation problems— follows a two-step approach. It <sup>fi</sup>rst learns a regular cost-neutral regression model without considering the actual asymmetric cost structure. It then uses the regular regression model as an aggregate, intermediate explanatory variable for making the ultimate cost-sensitive prediction, reducing the problem to a univariate one, analogous to how the tuning method for cost-sensitive classi<sup>fi</sup>cation works. Unlike other costsensitive regression methods, which extend particular regular regression methods under particular cost functions, this method is a meta method and has much broader applicability. Furthermore, as this method only tunes a regular regression model in a post-hoc manner, it does not require model retraining when the cost function changes. However, the particular tuning method (adding a certain amount) proposed by Bansal et al. [4] is rather restrictive since it only adjusts the prediction of a regular regression model by a certain amount. In this paper, we propose a more general tuning method, which extends the previous method by adjusting a regular regression model with a polynomial function. The previous method then becomes a special case of the proposed method.

## 3. Background

We adopt the performance measure for cost-sensitive regression used by Bansal et al. [4]. For a regression problem with a dependent variable y and a vector of independent variables x, a regression model is a mapping $f \colon \mathbf { X } \to \mathbf { y } ,$ , learned from a training sample $S = \{ < x _ { i } , y _ { i } > \vert i = 1$ $2 , . . . , N \}$ by some learning method. If a prediction error e incurs a cost $C ( e ) _ { }$ , the average misprediction cost of model $f ,$ as estimated on S, is de<sup>fi</sup>ned as

$$
\theta = \frac {1}{N} \sum_ {i = 1} ^ {N} C (f (x _ {i}) - y _ {i}).\tag{1}
$$

Regular regression methods, such as least-squares linear regression, model tree, and neural network, presume a symmetric cost function (i.e., $C ( e ) = C ( - e )$ for any misprediction error e). For example, leastsquares linear regression minimizes mean squared error, assuming a symmetric squared-error cost function $( \mathrm { i } . \mathrm { e } . , C ( e ) = e ^ { 2 } )$

However, in many real-world regression problems, such as real estate assessment [34], system reliability estimation [31], and bank loan charge-off forecasting [4], the cost function is asymmetric since the consequences of under-prediction (negative) and over-prediction (positive) errors are different. Fig. 1 illustrates two possible cost functions: LinLin and QuadQuad. They are special cases of monomialsplined loss functions, which are comprised of two monomials splined at error zero [31]. Speci<sup>fi</sup>cally, a monomial-splined loss function with the same degree on the two sides of the spline has the following form:

$$
C (e) = c ^ {+} e ^ {m}, \text {   if   } e > 0; c ^ {-} | e | ^ {m}, \text {   otherwise. }\tag{2}
$$

LinLin and QuadQuad are special cases of such monomial-splined loss functions where $m = 1$ and $m = 2$ , respectively. The widelyapplied absolute error and squared error are further special cases of LinLin and QuadQuad where $c ^ { + } = c ^ { - } = 1$ , respectively. In the case of LinLin, the amount of cost due to a prediction error is assumed to be proportional to the magnitude of the error, but the proportions for under-prediction and over-prediction errors may be different. In the case of QuadQuad, the cost is assumed to increase with prediction error at a quadratic rate. In other more extreme cost functions, such as LinEx and SquarEx, even the shape of the cost function is different for the two types of errors. More generally, even the form of the cost function on the same side may change as the amount of error changes. For example, the unit cost (in the case of linear cost) associated with high overestimation (underestimation) may be different from that associated with moderate overestimation (underestimation).

![](/api/attachments/VEBX67UK/fulltext/images/153aed820124e3f2b9a7c6595560b3f56c0a4ccae168099b6a7e6a544be6d26b.jpg)

(b) QuadQuad  
![](/api/attachments/VEBX67UK/fulltext/images/a851a0f4fad496795b06456419a6249bfcaab387f523fb9ee326e23770390f8b.jpg)  
Fig. 1. Cost function examples.

The cost function is necessarily problem dependent. De<sup>fi</sup>ning an appropriate cost function is often an art and requires deep domain expertise in many applications. For example, Varian [34] adopted a LinEx cost function for the real estate assessment problem, while Thompson and Basu [31] suggested that SquarEx may be more appropriate than LinEx for the system reliability estimation problem. The use of such extremely asymmetric cost functions is necessarily dependent on a deep understanding of the application domain.

Apparently, models learned by regular regression methods, which are designed to minimize symmetric costs, will not be optimal when the cost function is actually asymmetric. Given an asymmetric cost function C, Bansal et al. [4] adjusted the prediction of a regular regression model f by an amount of δ so as to minimize the average misprediction cost θ, resulting in an adjusted model $f ^ { \prime } { = } f { + } \delta .$ The original model f minimizes a symmetric cost measure, whereas the adjusted model f′ minimizes the asymmetric cost measure given the original model. As θ is a convex function with regard to δ when the cost function C is convex, an ef<sup>fi</sup>cient hill climbing algorithm was employed to search for the optimal δ.

## 4. Extended tuning method

We observe that the post-hoc tuning method of Bansal et al. [4] can be generalized into a two-step scheme. First, a regression model f is learned as usual without considering the cost asymmetry. The prediction error of this regression model on instance i is $f ( x _ { i } ) - y _ { i } .$ Next, g, a function of $f ,$ is found so as to minimize the average misprediction cost θ. The <sup>fi</sup>nal prediction for the dependent variable y is given by an adjusted regression mode $f \ ( \mathbf { x } ) { = } g ( f ( \mathbf { x } ) )$ ). The prediction error of the adjusted regression model on instance i is $f ^ { \prime } ( x _ { i } ) -$ $y _ { i } = g ( f ( x _ { i } ) ) - y _ { i }$ . The tuning method of Bansal et al. [4] is a special case where the tuning function is in the form of $g ( f ) = f + \delta .$ . At the tuning step, the base regression model f is essentially treated as an aggregate, intermediate explanatory variable for making the ultimate costsensitive prediction, reducing the tuning function g to a univariate one (i.e., g is a function of f ). This contrasts to methods that try to directly learn a regression model under the actual asymmetric cost structure without using the regular model f as an intermediate variable.

Furthermore, under some conditions, the optimal tuning function g for a given base regression model f may be found ef<sup>fi</sup>ciently—i.e., in a reasonable time—using a heuristic approach such as hill climbing. For example, it can be shown (in Proposition 1 below) that, under the following assumptions, the average misprediction cost θ is convex with regard to the parameters of g and therefore any local minimum of θ is also a global minimum:

(a) The cost function, $C ( e ) ,$ , is convex with regard to prediction error, e.

(b) The tuning function g is a polynomial of f of degree m, i.e., $g ( f ) =$ $\sum _ { j = 0 } ^ { m } \ \beta _ { j } f ^ { j } , f ^ { 0 } = 1$ . The prediction error of the adjusted regression model on instance i is $\sum _ { j \mathop { = } 0 } ^ { m } \beta _ { j } f ^ { j } ( x _ { i } ) - y _ { i }$ . The average misprediction cost of the adjusted regression model can be expressed as the following function of the vector of coef<sup>fi</sup>cients $\mathsf { \pmb { \beta } } = ( \beta _ { 0 } , \beta _ { 1 , . . . , \beta _ { m } } ) ^ { \mathrm { T } }$

$$
\theta (\boldsymbol {\beta}) = \frac {1}{N} \sum_ {i = 1} ^ {N} C (g (f (x _ {i})) - y _ {i}) = \frac {1}{N} \sum_ {i = 1} ^ {N} C \left(\sum_ {j = 0} ^ {m} \beta_ {j} f ^ {j} (x _ {i}) - y _ {i}\right).\tag{3}
$$

While these assumptions put restrictions on the cost function and tuning function theoretically, we believe that the proposed method has wide applicability. All cost functions that have been studied in the literature (e.g., LinLin, QuadQuad, LinEx, and SquarEx) are convex. A large range of possible tuning functions can be closely approximated by a polynomial function with a suf<sup>fi</sup>cient degree.

Proposition 1. Under the above-mentioned assumptions, the average misprediction cost of the adjusted regression model, θ(β), is convex with regard to β.

Proof. The proof of proposition 1 is trivial. Since the adjustment, characterized by β, is applied on a regression model f after the model has been learned, the prediction of f on a given problem instance, $f ( x _ { i } )$ $i = 1 , 2 , . . . , N ,$ is constant with respect to β. Since the cost function C(e) is convex with regard to e and convexity is invariant under af<sup>fi</sup>ne maps $( x \mapsto A x + b )$ , the misprediction cost of the adjusted model on a problem instance, $C ( \sum _ { j = 0 } ^ { m } \beta _ { j } f ^ { j } ( x _ { i } ) - y _ { i } ) = C ( \mathbf { f } ^ { \mathrm { T } } \mathbf { \beta } - y _ { i } ) , \ i = 1 , \ 2 , \ . . . , \ N ,$ where $\mathbf { f } = ( 1 , f ( x _ { i } ) , f ^ { 2 } ( x _ { i } ) , . . . , f ^ { m } ( x _ { i } ) ) ^ { \mathrm { T } }$ , is convex with regard to β. The summation $\sum _ { i = 1 } ^ { N } \ C \left( \sum _ { j = 0 } ^ { m } \beta _ { j } f ^ { j } ( x _ { i } ) - y _ { i } \right)$ is then convex with regard to β. The average misprediction cost of the adjusted model, $\theta ( { \mathfrak { B } } ) =$ ${ \frac { 1 } { N } } \sum _ { i = 1 } ^ { N } ~ C { \Bigg ( } \sum _ { j = 0 } ^ { \overline { { m } } } \beta _ { j } f ^ { j } ( x _ { i } ) - y _ { i } { \Bigg ) }$ , is therefore convex with regard to β. □

When the average misprediction cost θ is convex with regard to the parameters of the tuning function and therefore any local minimum of θ is also a global minimum, the hill climbing algorithm of Bansal et al. [4] can be extended to repeatedly and alternately search on the parameters $\beta _ { i } , \ i = 0 , \ 1 , \ . . . , \ m ,$ until no further improvement is possible. Fig. 2 outlines the overall algorithm.

The algorithm (named CostSensitiveRegression) can work with any base regression method and any convex cost function. It takes a base regression method, a training sample, a convex cost function, the maximum degree of the polynomial tuning function to be found, and a given precision for adjusting the coef<sup>fi</sup>cients of the tuning function as inputs and returns an adjusted regression model as the output. First, a regular regression model is trained using the base regression method (step 1). Initially, the tuning function is simply the identity function (i.e., g(f)=f) (step 2). Then, a loop is used to repeatedly search for the optimal coef<sup>fi</sup>cients of the terms in the tuning function until no further improvement is possible (step 3). During each iteration, a nested loop is used to alternately search for the optimal coef<sup>fi</sup>cient of each term in the tuning function, given the current coef<sup>fi</sup>cients of the other terms, by calling a hill climbing procedure (step 3.2). Finally, an adjusted regression model that minimizes the average misprediction error is returned (step 4).

```txt
CostSensitiveRegression (Γ, S, C, m, p)
    Γ: A base regression method.
    S: A training sample, {<xi, yi> | i = 1, 2, ..., N}.
    C: A cost function.
    m: The maximum degree of the polynomial tuning function to be found.
    p: A given precision for adjusting the coefficients of the tuning function.

1.    f := Γ(S). /* Learn a regression model f using Γ based on S. */
2.    β = (β₀, β₁, ..., βₘ)ᵀ := (0, 1, 0, ..., 0)ᵀ.
3.    DO
3.1    β_old := β.
3.2    FOR d FROM 1 TO m
3.2.1    HillClimbing(S, C, m, p, f, β, d).
    WHILE β ≠ β_old. /* End of 3. */
4.    RETURN ∑_{j=0}^{m} β_j f^j. /* Return an adjusted regression model. */
HillClimbing(S, C, m, p, f, β, d).
    S, C, m, p: Same as above.
    f: A regression model.
    β = (β₀, β₁, ..., βₘ)ᵀ: An m-dimensional vector, containing the coefficients of the polynomial tuning function.
    d: The degree of a term in the tuning function to be tuned.

1.    β⁺ := β⁻ := β, β⁺_d := β_d + p, β̄_d := β_d - p.
2.    IF θ(β⁺) < θ(β), /* θ is defined in equation (2). */
2.1    δ := 1. /* Set the direction of adjustment. */
3.    ELSE IF θ(β⁻) < θ(β),
3.1    δ := -1.
4.    ELSE
4.1    RETURN.
5.    β⁻ := β.
6.    DO
6.1    s := 1. /* Set the initial hill climbing stride. */
6.2    β := β⁻.
6.3    DO
6.3.1    β⁺ := β⁻ := β.
6.3.2    β_d := β_d + s * p * δ.
6.3.3    s := s * 2; /* Double the stride after each step. */
6.3.4    β⁺_d := β_d + s * p * δ.
    WHILE θ(β⁺) < θ(β). /* End of 6.3. */
    WHILE s > 2. /* End of 6. */

Fig. 2. An extended tuning algorithm for cost-sensitive regression
```

The hill climbing procedure (named HillClimbing) searches for the optimal coef<sup>fi</sup>cient of a particular term in the polynomial tuning function given the current coef<sup>fi</sup>cients of the other terms. First, the direction of climbing, which leads to lower average misprediction cost, is determined via trials (steps 1 to 4). Starting with the current coef<sup>fi</sup>cients (step 5), several iterations of hill climbing in the determined direction are then carried out to approach the optimal coef<sup>fi</sup>cient of the term under search until the number of climbing steps during an iteration falls below two and thus no further climbing is promising (loop at step 6). During each iteration of hill climbing, several climbing steps are attempted until the performance does not improve any more (nested loop at step 6.3). To speed up the procedure, the climbing stride starts from the given precision of adjustment (step 6.1) and is doubled after every climbing step (step 6.3.3).

Note that a linear tuning function, including the special case of Bansal et al. [4] where the coef<sup>fi</sup>cient of the linear term is <sup>fi</sup>xed at 1, does not change the model complexity. Applying a linear tuning function on a linear regression model, for example, the resulting adjusted regression model is still a linear one. A high-degree tuning function, however, will increase the model complexity. Applying a quadratic tuning function on a linear regression model, for example, will result in a quadratic adjusted regression model.

In general, as we increase the degree of the tuning function (m) and thus the resulting model complexity, we are able to lower the average misprediction cost on the training sample. However, the performance improvement observed on the training sample may not carry on to new data, as a more complex model also runs a higher risk of overfitting the training data. The degree of the tuning function most appropriate for a particular application needs to be determined empirically. As Hand et al. [23, p. 183] note, “the issue of selecting a model of the appropriate complexity is always a key concern in any data analysis venture where we consider models of different complexities”. The user may start with the simplest tuning function and gradually increase the degree until the tuning model does not change any more or the testing performance starts to decrease.

The precision of adjustment (p) controls how closely the program can approach the optimal solution. If p is set too large, the found solution may not be satisfactorily close to the optimal; if it is too small, too much computation time is incurred. The user may experiment with different values until the solution does not change much or the computation time is not affordable any more. A straightforward enhancement in a practical tool is to allow the user to reduce p and continue with <sup>fi</sup>ner tuning on the basis of the current solution at any point without starting from scratch.

## 5. Empirical evaluation

We have implemented the extended tuning method and empirically compared it with the one presented by Bansal et al. [4]. In this section, we report on the implementation and empirical evaluation.

## 5.1. Implementation and experimental environment

We implemented the CostSensitiveRegression algorithm (Fig. 2) in Java by extending the Classifier class in the Weka machine learning toolkit [36] (http://www.cs.waikato.ac.nz/ml/weka/). The program, including source code, is available from the authors. We ran the experiment on a Dell Optiplex/GX620 workstation, con<sup>fi</sup>gured with a 3 GHz Pentium D CPU and 1 GB of RAM, running the Windows XP operating system.

The extended tuning algorithm takes <sup>fi</sup>ve inputs: a base regression method, a training sample, a convex cost function, the maximum degree of the polynomial tuning function to be found, and a given precision for adjusting the coef<sup>fi</sup>cients of the tuning function. The inputs are passed to the CostSensitiveRegression program through command options in the fashion of Weka. The program can work with any base regression method. In the experiment, we used three base regression methods available in Weka: the standard least-squares linear regression (LR), M5 model tree [26], and backpropagation neural network (NN) [27]. We retained the default parameter settings for these methods in Weka. The training sample was presented in the ARFF data <sup>fi</sup>le format of Weka.

The program can also work with any convex cost function. In the experiment, we implemented and evaluated the LinLin and QuadQuad cost functions. We evaluated linear, quadratic, cubic, and quartic tuning functions (i.e., polynomial tuning functions with a maximum degree of one, two, three, and four, respectively). The precision for adjusting the coef<sup>fi</sup>cients of the tuning functions we used in the experiment was 0.00001.

## 5.2. Problem domain

Following Bansal et al. [4], we conducted the evaluation in the domain of loan charge-off forecasting, which is characterized by asymmetric costs on misprediction errors. For a bank, underpredicting its future loan charge-off by a certain amount is riskier than over-prediction by the same amount. Taking this into account, Bansal et al. [4] decided to penalize under-predictions more heavily than over-predictions while tuning regression models.

Banks determine their loan loss reserves based on their predictions of future loan charge-off amounts. If a bank over-predicts its future loan charge-off, it will need to maintain extra funds in the loan loss reserves and thus suffer reduced earnings—the reserves are deducted from earnings—and possibly receive a lower credit score from <sup>fi</sup>nancial analysts. Under-predicting the loan charge-off, however, has more serious consequences as it presents a rosier picture of an otherwise worse scenario. Besides the bank management, outside bodies such as investors, accountants, and regulators are also interested in knowing whether a bank is adequately prepared for its future loan losses. If a bank does not have suf<sup>fi</sup>cient loan loss reserves, the consequences could be dire. Financial analysts who are responsible for a bank's credit rating also consider the bank's reserve adequacy in the rating. If a bank under-predicts its future loan chargeoff and thus does not prepare suf<sup>fi</sup>cient provision for its loan losses, it will not only face the wrath of investors, accountants, and regulators but also experience an even greater downturn in its credit rating. Hence, under-prediction is much costlier than over-prediction in the domain of loan charge-off forecasting.

## 5.3. Data and cost functions

The loan charge-off forecasting data we used came from Wharton Research Data Services (WRDS, https://wrds.wharton.upenn.edu/). We used the most recent data (of 20 quarters between 2004 and 2008) of commercial banks available in the Bank Regulatory database of WRDS. The database contains data of all banks <sup>fi</sup>ling the Report of Condition and Income (known as the “Call Report”) regulated by the Federal Reserve System, Federal Deposit Insurance Corporation, and the Comptroller of the Currency. We used the same 14 variables (listed in Table 1 with the variable codes, names, and de<sup>fi</sup>nitions from WRDS) as Bansal et al. [4], who used the <sup>fi</sup>rst 13 variables in a particular quarter as the independent variables and the loan chargeoff in the same quarter as the dependent variable in regression models. Such modeling may be appropriate for studying the effects of the independent variables on loan charge-off, but application of an asymmetric loss function for a cost-sensitive decision problem lends itself to a forecasting scenario. As Whittle [35, p. 106] note:

Table 1 Variables used in the evaluation.

<table><tr><td>No</td><td>Code</td><td>Name</td><td>Definition</td></tr><tr><td>1</td><td>1400</td><td>Total loans and leases, gross</td><td>The aggregate gross book value of total loans (before deduction of valuation reserves).</td></tr><tr><td>2</td><td>1403</td><td>Total loans and lease finance receivables: nonaccrual</td><td>Includes the outstanding balances of loans and lease financing receivables that the bank has placed in nonaccrual status. Also includes all restructured loans and lease financing receivables that are in nonaccrual status.</td></tr><tr><td>3</td><td>1407</td><td>Total loans and lease financing receivables: past due 90 days or more and still accruing</td><td>Includes loans and lease financing receivables on which payment is due and unpaid for 90 days or more. Also includes all restructured loans and leases.</td></tr><tr><td>4</td><td>2143</td><td>Intangible assets</td><td>Includes the un-amortized amount of intangible assets.</td></tr><tr><td>5</td><td>2170</td><td>Total assets</td><td>It is the sum of all asset items. It equals “total liabilities, limited-life preferred stock, and equity capital”.</td></tr><tr><td>6</td><td>3163</td><td>Goodwill</td><td>Includes the amount (book value) of un-amortized goodwill. Represents the excess of the cost of a company over the sum of the fair values of the tangible assets and identifiable intangible assets acquired less the fair value of liabilities</td></tr><tr><td>7</td><td>3200</td><td>Subordinated notes and debentures</td><td>Includes the amount of outstanding subordinated notes and debentures (including mandatory convertible debt).</td></tr><tr><td>8</td><td>3210</td><td>Equity capital, total</td><td>The sum of “perpetual preferred stock and related surplus”, “common stock”, “surplus”, “undivided profits and capital reserves”, “cumulative foreign currency translation adjustments” less “net unrealized loss on marketable equity securities”.</td></tr><tr><td>9</td><td>4010</td><td>Interest and fee income on loans, total</td><td>Includes the total of interest and fee income and similar charges levied against all assets classified as loans in Condition reports, including fees on overdrafts. Includes investigation and service charges, renewal and past due charges, commitment fees (regardless of whether the loan has been made), and fees charged for the execution of mortgages or agreements securing the bank’s loans.</td></tr><tr><td>10</td><td>4079</td><td>Total noninterest income</td><td>Includes the sum of “income from fiduciary activities”, “service charges on deposit accounts in domestic offices”, “trading gains (losses) and fees from foreign exchange transactions”, “other foreign transaction gains (losses)”, “gains (losses) and fees from assets held in trading accounts”, and “other non-interest income”.</td></tr><tr><td>11</td><td>4180</td><td>Expense of federal funds purchased and securities sold under agreements to repurchase</td><td>Includes the gross expense of all liabilities included in “federal funds purchased and securities sold under agreements to repurchase”.</td></tr><tr><td>12</td><td>4340</td><td>Net income (loss)</td><td>Includes the net income (loss) for the period.</td></tr><tr><td>13</td><td>A223</td><td>Risk-weighted assets (net of allowances and other deductions)</td><td>It is the amount of the bank’s risk-weighted assets net of all deductions. The amount reported in this item is the denominator of the bank’s total risk-based capital ratio. When determining the amount of risk-weighted assets, on-balance sheet assets are assigned an appropriate risk weight (0%, 20%, 50%, or 100%) and off-balance sheet items are first converted to a credit equivalent amount and then assigned to one of the four risk weight categories. The on-balance sheet assets and the credit equivalent amounts of off-balance sheet items are then multiplied by the appropriate risk weight percentages and the sum of these risk-weighted amounts, less certain deductions, is the bank’s gross risk-weighted assets.</td></tr><tr><td>14</td><td>4635</td><td>Charge-offs on allowance for loan and lease losses</td><td>The amount of gross charge-offs on loans and leases during the calendar year-to-date.</td></tr></table>

“In most cases the predicted value, once obtained, is used to initiate or modify a course of action... In this larger context the problem of prediction appears only as incidental, and the central problem is that of regulation, i.e., of using past values to determine present action in such a way that the future course of the process is as near as possible to the desired one”.

It is in such a context that realistic, typically asymmetric, cost functions need to be applied for building forecasting models. In our evaluation, therefore, we used all 14 variables, including loan chargeoff, in a particular quarter as the independent variables, and the loan charge-off amount in the following quarter as the dependent variable. Such modeling would be useful for a bank in predicting its loan charge-off for the next quarter based on its current <sup>fi</sup>nancial data and deciding on its loan loss reserves accordingly.

We generated 19 datasets based on the data of the 20 quarters. Each dataset contains the quantities of the 14 variables in a particular quarter as the independent variables and the quantity of the loan charge-off in the following quarter as the dependent variable. For the last quarter of 2008, only the loan charge-off was used, as the dependent variable in the 2008 quarter three dataset, since the 2009 data were not available from WRDS yet. Each dataset was used as a training set while the next dataset was used as the testing set, except that the <sup>fi</sup>rst dataset (2004 quarter one) was only used for training while the last dataset (2008 quarter three) was only used for testing.

Thus, there were 18 training datasets and 18 testing datasets. Observations with missing values were discarded. The remaining datasets contained an average of 7684 (a minimum of 7351 and a maximum of 8042) observations. As the distributions of the variables were largely skewed, (natural) logarithm transformations were applied to reduce the extent of skewness.

As discussed earlier, under-prediction is considered much costlier than over-prediction in this domain. Following Bansal et al. [4], we used a LinLin cost function with a steeper cost slope for under-prediction as compared to over-prediction. We <sup>fi</sup>xed the unit cost for over-prediction at 1 and examined the following cost ratios (under-prediction to overprediction): 100:1, 50:1, 20:1, and 10:1. To evaluate the generalizability of the proposed method, we also used a QuadQuad cost function. Again, we <sup>fi</sup>xed the unit cost for over-prediction at 1 and examined the same four cost ratios.

## 5.4. Results

Table 2 summarizes the results of conventional performance measures, including Pearson correlation coef<sup>fi</sup>cient, mean absolute error, and mean squared error. Each reported quantity is an average over the 18 training or testing datasets. We include these measures here for the sake of completeness. However, absolute error and squared error are symmetric (i.e., cost ratio between under-prediction and overprediction is 1:1) special cases of LinLin and QuadQuad cost functions, respectively, and are not suitable for the loan charge-off forecasting problem where the cost structure is clearly asymmetric. Linear tuning functions, including the special case of Bansal et al. [4], do not change the Pearson correlation coef<sup>fi</sup>cient, which remains invariant under linear transformations. High-degree tuning functions will increase the model complexity and Pearson correlation coef<sup>fi</sup>cient is not appropriate for measuring nonlinear dependence.

Table 2  
Conventional performance measures.

<table><tr><td rowspan="2">Method</td><td colspan="3">Training</td><td colspan="3">Testing</td></tr><tr><td>Pearson Correlation Coefficient</td><td>Mean Absolute Error</td><td>Mean Squared Error</td><td>Pearson Correlation Coefficient</td><td>Mean Absolute Error</td><td>Mean Squared Error</td></tr><tr><td>LR</td><td>0.782</td><td>1.118</td><td>2.115</td><td>0.608</td><td>1.262</td><td>2.657</td></tr><tr><td>M5</td><td>0.793</td><td>1.095</td><td>2.018</td><td>0.563</td><td>1.333</td><td>3.081</td></tr><tr><td>NN</td><td>0.790</td><td>1.218</td><td>2.412</td><td>0.602</td><td>1.438</td><td>3.373</td></tr></table>

Tables 3 and 4 summarize the results of the average misprediction cost under LinLin cost functions on the training and testing data, respectively. Each reported quantity is an average over the 18 training or testing datasets. “None” refers to the original regression models without tuning. “BSZ” refers to the tuning method of Bansal, Sinha, and Zhao [4]. Figs. 3 and 4 contrast the performance of the extended tuning method and that of the BSZ method on the training and testing data, respectively.

The linear tuning function outperformed the BSZ tuning function on the training data for every base regression method under every cost ratio. This performance improvement (from the BSZ tuning function to the linear tuning function) continued to hold on the testing data. A repeated-measures, factorial ANOVA under each cost ratio, with tuning function (BSZ and linear) and base regression method (LR, M5, and NN) as factors, showed that the performance difference between the two tuning functions was statistically signi<sup>fi</sup>cant (F(1, 17)N 14.1, pb 0.01). Intuitively, the linear tuning function, as compared to the BSZ tuning function, increases the <sup>fl</sup>exibility of the tuned model in <sup>fi</sup>tting the training data without increasing the model complexity, hence leading to signi<sup>fi</sup>cant performance improvement.

As the degree of the polynomial tuning function increased, the average misprediction cost of every base regression method on the training data continued to decrease, indicating that the tuned models could <sup>fi</sup>t the training data better, but the performance gradually <sup>fl</sup>attened out. However, the performance improvement did not always generalize to the testing data. The average misprediction cost of some base regression methods on the testing data started to increase at some points, indicating that over<sup>fi</sup>tting might have occurred due to the increased model complexity. Intuitively, the high-degree (quadratic, cubic, and quartic) tuning functions did not work well because such transformations increased the complexity of the base regression models and, possibly, invalidated some assumptions behind the base regression models. For example, the quadratic tuning function not only changes a linear regression model into a quadratic one but also introduces interactions among independent variables. The increased model <sup>fl</sup>exibility hardly compensated for the increase in model complexity. It turned out that none of the high-degree tuning functions improved upon the linear tuning function signi<sup>fi</sup>cantly.

Table 3  
Average misprediction costs under LinLin cost functions on the training data.

<table><tr><td rowspan="2">Method</td><td rowspan="2">Cost ratio</td><td colspan="6">Tuning method</td></tr><tr><td>None</td><td>BSZ</td><td>Linear</td><td>Quadratic</td><td>Cubic</td><td>Quartic</td></tr><tr><td rowspan="4">LR</td><td>10</td><td>6.150</td><td>2.632</td><td>2.614</td><td>2.613</td><td>2.611</td><td>2.611</td></tr><tr><td>20</td><td>11.740</td><td>3.122</td><td>3.077</td><td>3.076</td><td>3.074</td><td>3.073</td></tr><tr><td>50</td><td>28.512</td><td>3.751</td><td>3.660</td><td>3.655</td><td>3.650</td><td>3.649</td></tr><tr><td>100</td><td>56.465</td><td>4.214</td><td>4.084</td><td>4.066</td><td>4.060</td><td>4.059</td></tr><tr><td rowspan="4">M5</td><td>10</td><td>6.024</td><td>2.620</td><td>2.589</td><td>2.585</td><td>2.579</td><td>2.579</td></tr><tr><td>20</td><td>11.501</td><td>3.109</td><td>3.045</td><td>3.043</td><td>3.040</td><td>3.038</td></tr><tr><td>50</td><td>27.932</td><td>3.741</td><td>3.620</td><td>3.619</td><td>3.613</td><td>3.612</td></tr><tr><td>100</td><td>55.316</td><td>4.214</td><td>4.037</td><td>4.033</td><td>4.024</td><td>4.022</td></tr><tr><td rowspan="4">NN</td><td>10</td><td>6.287</td><td>2.596</td><td>2.563</td><td>2.555</td><td>2.547</td><td>2.547</td></tr><tr><td>20</td><td>11.920</td><td>3.072</td><td>3.010</td><td>3.005</td><td>3.001</td><td>3.000</td></tr><tr><td>50</td><td>28.819</td><td>3.690</td><td>3.578</td><td>3.568</td><td>3.565</td><td>3.564</td></tr><tr><td>100</td><td>56.984</td><td>4.160</td><td>3.992</td><td>3.979</td><td>3.969</td><td>3.967</td></tr></table>

Table 4  
Average misprediction costs under LinLin cost functions on the testing data.

<table><tr><td rowspan="2">Method</td><td rowspan="2">Cost ratio</td><td colspan="6">Tuning method</td></tr><tr><td>None</td><td>BSZ</td><td>Linear</td><td>Quadratic</td><td>Cubic</td><td>Quartic</td></tr><tr><td rowspan="4">LR</td><td>10</td><td>6.841</td><td>2.995</td><td>2.958</td><td>2.959</td><td>2.958</td><td>2.958</td></tr><tr><td>20</td><td>13.039</td><td>3.530</td><td>3.443</td><td>3.441</td><td>3.438</td><td>3.437</td></tr><tr><td>50</td><td>31.636</td><td>4.245</td><td>4.079</td><td>4.064</td><td>4.056</td><td>4.058</td></tr><tr><td>100</td><td>62.630</td><td>4.772</td><td>4.563</td><td>4.534</td><td>4.517</td><td>4.517</td></tr><tr><td rowspan="4">M5</td><td>10</td><td>6.834</td><td>3.472</td><td>3.358</td><td>3.373</td><td>3.373</td><td>3.372</td></tr><tr><td>20</td><td>12.947</td><td>4.236</td><td>4.044</td><td>4.069</td><td>4.059</td><td>4.058</td></tr><tr><td>50</td><td>31.287</td><td>5.396</td><td>5.012</td><td>5.041</td><td>5.037</td><td>5.035</td></tr><tr><td>100</td><td>61.852</td><td>6.438</td><td>5.790</td><td>5.869</td><td>5.727</td><td>5.725</td></tr><tr><td rowspan="4">NN</td><td>10</td><td>7.111</td><td>3.230</td><td>3.160</td><td>3.160</td><td>3.148</td><td>3.147</td></tr><tr><td>20</td><td>13.415</td><td>3.818</td><td>3.722</td><td>3.715</td><td>3.712</td><td>3.712</td></tr><tr><td>50</td><td>32.325</td><td>4.593</td><td>4.470</td><td>4.456</td><td>4.451</td><td>4.449</td></tr><tr><td>100</td><td>63.843</td><td>5.195</td><td>5.088</td><td>5.059</td><td>5.025</td><td>5.027</td></tr></table>

Tables 5 and 6 summarize the results of the average misprediction cost under QuadQuad cost functions on the training and testing data, respectively. Again, each reported value is an average over the 18 training or testing datasets. Figs. 5 and 6 contrast the performance of the extended tuning method and that of the BSZ method on the training and testing data, respectively.

The <sup>fi</sup>ndings from the QuadQuad cost function were similar to those from the LinLin cost function. The linear tuning function again outperformed the BSZ tuning function on both the training and testing data for every base regression method under every cost ratio. A repeated-measures, factorial ANOVA under each cost ratio, with tuning function (BSZ and linear) and base regression method (LR, M5, and NN) as factors, showed that the performance difference between the two tuning functions was statistically signi<sup>fi</sup>cant (F(1, 17) N 19.9, pb0.001).

The cost reduction from BSZ to linear appears to be small, in the range of 0.7% to 10%. However, the cost values are on a natural log scale as the variables, including loan charge-off, have gone through natural logarithmic transformations. The cost reduction on the original scale is in the range of 1.9% to 25%, which would be considered practically useful for the bank loan charge-off forecasting problem.

As the degree of the polynomial tuning function further increased, the performance of every base regression method on the training data continued to improve, but the performance gradually <sup>fl</sup>attened out. However, the average misprediction cost of some base regression methods on the testing data started to increase at some points, indicating that over<sup>fi</sup>tting might have occurred due to the increased model complexity. Especially for M5, when the degree of the polynomial tuning function increased from quadratic to cubic and quartic, the performance dramatically deteriorated, showing the possibility of severe over<sup>fi</sup>tting.

There are also some interesting <sup>fi</sup>ndings about the relative performance of the three base regression methods. The method with the least model complexity, LR, achieved the worst performance on the training data, as expected. However, it often outperformed the other two methods on the testing data, indicating that the other methods might have over<sup>fi</sup>tted the training data. This shows again the importance of selecting an appropriate level of model complexity for a particular problem [23].

For completeness, we also experimented with situations where over-prediction is costlier than under-prediction. We <sup>fi</sup>xed the unit cost for under-prediction at 1 and examined the following cost ratios (under-prediction to over-prediction): 1:100, 1:50, 1:20, and 1:10. Note, however, such cost ratios are clearly unrealistic for loan chargeoff forecasting and were used for testing the method only. The <sup>fi</sup>ndings are similar to those when the cost ratios are greater than 1.

Table 7 summarizes the model training and tuning times. The time needed by the linear tuning function was less than two seconds. As the degree of the tuning function increased, the tuning time increased too. The quartic tuning function took less than a minute.

(a) Cost Ratio = 10:1  
![](/api/attachments/VEBX67UK/fulltext/images/14f54dd6649aaf775cbd3bd2a13c13cc4b00627505c014c16ec80c3020458328.jpg)

(b) Cost Ratio = 20:1  
![](/api/attachments/VEBX67UK/fulltext/images/abed85856b010852f11290ca5dbf6e6bd0b19db9666b584db8852402100968c0.jpg)

(c) Cost Ratio = 50:1  
![](/api/attachments/VEBX67UK/fulltext/images/42210a141baeca63b31888a6dc78d0520ccd8f8e5541c4f4464bed634031163e.jpg)

(d) Cost Ratio = 100:1  
![](/api/attachments/VEBX67UK/fulltext/images/9db1043f7db13d3ad139c6731f5bc5ce6ed0a0a07acaae9a4dde2a560aa6f1eb.jpg)  
Fig. 3. Average misprediction costs of different tuning methods under LinLin cost functions on the training data.

## 5.5. Illustrative example

The linear regression model trained on the 2008 Quarter 1 dataset was

$$
\begin{array}{c} y = f (x) = - 0. 5 1 1 x _ {1} + 0. 2 0 0 x _ {2} + 0. 0 6 4 x _ {3} - 0. 1 2 8 x _ {5} + 0. 0 1 1 x _ {6} \\ \quad + 0. 1 6 8 x _ {8} + 0. 5 6 9 x _ {9} + 0. 2 0 2 x _ {1 0} + 0. 3 5 1 x _ {1 3} + 0. 4 1 7 x _ {1 4} - 4. 5 8 2. \end{array}
$$

The average misprediction cost of this basic model under the LinLin cost function with a cost ratio of 1:10 was 6.6 on the training dataset. The adjusted model after applying the BSZ tuning function was

$$
\begin{array}{l} y = f (x) + 2. 0 0 0 = - 0. 5 1 1 x _ {1} + 0. 2 0 0 x _ {2} + 0. 0 6 4 x _ {3} - 0. 1 2 8 x _ {5} \\ \qquad + 0. 0 1 1 x _ {6} + 0. 1 6 8 x _ {8} + 0. 5 6 9 x _ {9} + 0. 2 0 2 x _ {1 0} + 0. 3 5 1 x _ {1 3} \\ \qquad + 0. 4 1 7 x _ {1 4} - 2. 5 8 2. \end{array}
$$

The average misprediction cost on the training dataset reduced to 2.84. The adjusted model after applying the linear tuning function was

$$
\begin{array}{l} y = 0. 8 9 2 f (x) + 2. 3 8 3 = - 0. 4 5 6 x _ {1} + 0. 1 7 8 x _ {2} + 0. 0 5 7 x _ {3} - 0. 1 1 4 x _ {5} \\ \qquad + 0. 0 1 0 x _ {6} + 0. 1 5 0 x _ {8} + 0. 5 0 8 x _ {9} + 0. 1 8 0 x _ {1 0} + 0. 3 1 3 x _ {1 3} \\ \qquad + 0. 3 7 2 x _ {1 4} - 1. 7 0 4. \end{array}
$$

The average misprediction cost on the training dataset further reduced to 2.815. The adjusted model after applying the quadratic tuning function was

$$
y = - 0. 0 0 5 f ^ {2} (x) + 0. 9 5 3 f (x) + 2. 2 4 9.
$$

Note that the adjusted model became quadratic. The average misprediction cost on the training dataset further reduced to 2.813. The average misprediction cost of the original model, the model tuned with the BSZ function, the model tuned with the linear function, and the model tuned with the quadratic function on the testing dataset, the 2008 Quarter 2 dataset, was 5.534, 2.923, 2.879, and 2.878, respectively.

Note that the models were built for prediction and forecasting purposes, rather than for explaining the impacts of the independent variables on loan charge-off. The loan charge-off amount of the current quarter was included in the models to predict the loan chargeoff amount of the next quarter. We therefore do not attempt to interpret the coef<sup>fi</sup>cients of the independent variables in the models.

## 5.6. Experiments with other datasets

We experimented with four additional regression datasets: Abalone, Bank (8FM), House (8L), and Puma (8NH), which are available on the Weka Web site [36]. We used the same base regression methods (LR, M5, and NN), cost functions (LinLin and QuadQuad), cost ratios (1:100,

![](/api/attachments/VEBX67UK/fulltext/images/c318594a59dbf7e8ef4726d321da05b11cdf73a7c6130a355829768c1dce991d.jpg)

(b) Cost Ratio = 20:1  
![](/api/attachments/VEBX67UK/fulltext/images/74c31a7faa0b90750dd327fa3114082c604f9c937dcb0087ee5755414f7294e1.jpg)

(c) Cost Ratio = 50:1  
![](/api/attachments/VEBX67UK/fulltext/images/06df9f9396cbc587d53ed9bfc47844521655214b8f28a57c005d211f2e617882.jpg)

(d) Cost Ratio = 100:1  
![](/api/attachments/VEBX67UK/fulltext/images/55ff00e2746b512420eccd67b26ee8c68d1f4a2cdbd61d502de25bc90625f298.jpg)  
Fig. 4. Average misprediction costs of different tuning methods under LinLin cost functions on the testing data.

1:50, 1:20, 1:10, 10:1, 20:1, 50:1, and 100:1), and parameter values as before. We randomly split each dataset into a training set with two thirds of the instances and a test set with the remaining instances. We conducted such splitting 20 times for each dataset and used the average performance over the 20 runs as an estimate of the true performance.

The <sup>fi</sup>ndings are similar in general although the best degree of tuning varies (the results are available from the authors.) As the degree of tuning increased, the performance on the training data tended to improve, but the performance improvement gradually <sup>fl</sup>attened out. However, the performance on the testing data did not always continue to improve and even started to degenerate at some points. The degree of tuning that led to the best performance on the testing data varies across datasets and cost settings. While the linear tuning function appeared to be the best for the House dataset under most cost settings, performance improvement was observed when the degree of tuning increased to quadratic, cubic, and even quartic on other datasets. An appropriate degree of tuning needs to be empirically determined for a given dataset and cost setting.

Table 5  
Average misprediction costs under QuadQuad cost functions on the training data.

<table><tr><td rowspan="2">Method</td><td rowspan="2">Cost ratio</td><td colspan="6">Tuning method</td></tr><tr><td>None</td><td>BSZ</td><td>Linear</td><td>Quadratic</td><td>Cubic</td><td>Quartic</td></tr><tr><td rowspan="4">LR</td><td>10</td><td>11.401</td><td>5.756</td><td>5.716</td><td>5.713</td><td>5.709</td><td>5.709</td></tr><tr><td>20</td><td>21.720</td><td>7.426</td><td>7.327</td><td>7.319</td><td>7.312</td><td>7.309</td></tr><tr><td>50</td><td>52.676</td><td>10.077</td><td>9.829</td><td>9.806</td><td>9.792</td><td>9.780</td></tr><tr><td>100</td><td>104.268</td><td>12.415</td><td>11.988</td><td>11.938</td><td>11.915</td><td>11.899</td></tr><tr><td rowspan="4">M5</td><td>10</td><td>11.141</td><td>5.630</td><td>5.574</td><td>5.567</td><td>5.547</td><td>5.547</td></tr><tr><td>20</td><td>21.278</td><td>7.294</td><td>7.162</td><td>7.156</td><td>7.125</td><td>7.125</td></tr><tr><td>50</td><td>51.689</td><td>9.944</td><td>9.627</td><td>9.622</td><td>9.579</td><td>9.570</td></tr><tr><td>100</td><td>102.374</td><td>12.290</td><td>11.754</td><td>11.744</td><td>11.695</td><td>11.677</td></tr><tr><td rowspan="4">NN</td><td>10</td><td>11.997</td><td>5.632</td><td>5.519</td><td>5.491</td><td>5.473</td><td>5.473</td></tr><tr><td>20</td><td>22.646</td><td>7.248</td><td>7.060</td><td>7.031</td><td>7.004</td><td>7.003</td></tr><tr><td>50</td><td>54.594</td><td>9.823</td><td>9.455</td><td>9.417</td><td>9.381</td><td>9.378</td></tr><tr><td>100</td><td>107.840</td><td>12.114</td><td>11.527</td><td>11.466</td><td>11.425</td><td>11.420</td></tr></table>

Table 6  
Average misprediction costs under QuadQuad cost functions on the testing data.

<table><tr><td rowspan="2">Method</td><td rowspan="2">Cost ratio</td><td colspan="6">Tuning method</td></tr><tr><td>None</td><td>BSZ</td><td>Linear</td><td>Quadratic</td><td>Cubic</td><td>Quartic</td></tr><tr><td rowspan="4">LR</td><td>10</td><td>14.249</td><td>7.272</td><td>7.151</td><td>7.129</td><td>7.123</td><td>7.122</td></tr><tr><td>20</td><td>27.130</td><td>9.367</td><td>9.104</td><td>9.066</td><td>9.056</td><td>9.054</td></tr><tr><td>50</td><td>65.771</td><td>12.668</td><td>12.091</td><td>12.005</td><td>11.984</td><td>11.978</td></tr><tr><td>100</td><td>130.172</td><td>15.596</td><td>14.661</td><td>14.499</td><td>14.468</td><td>14.462</td></tr><tr><td rowspan="4">M5</td><td>10</td><td>16.566</td><td>9.373</td><td>8.971</td><td>9.078</td><td>12.097</td><td>12.095</td></tr><tr><td>20</td><td>31.549</td><td>12.599</td><td>11.801</td><td>11.952</td><td>17.944</td><td>17.946</td></tr><tr><td>50</td><td>76.499</td><td>18.219</td><td>16.491</td><td>16.659</td><td>28.437</td><td>28.559</td></tr><tr><td>100</td><td>151.415</td><td>23.841</td><td>20.853</td><td>20.916</td><td>38.354</td><td>39.024</td></tr><tr><td rowspan="4">NN</td><td>10</td><td>15.977</td><td>8.191</td><td>7.937</td><td>7.944</td><td>8.058</td><td>8.079</td></tr><tr><td>20</td><td>29.983</td><td>10.647</td><td>10.230</td><td>10.244</td><td>10.487</td><td>10.486</td></tr><tr><td>50</td><td>71.998</td><td>14.585</td><td>13.894</td><td>13.899</td><td>14.280</td><td>14.279</td></tr><tr><td>100</td><td>142.024</td><td>18.187</td><td>17.218</td><td>17.191</td><td>17.496</td><td>17.491</td></tr></table>

![](/api/attachments/VEBX67UK/fulltext/images/e467f7d22085d27b8c1af485cef85633cdad057dbd421ce6184788d6dadb5672.jpg)

(b) Cost Ratio = 20:1  
![](/api/attachments/VEBX67UK/fulltext/images/285421be738f2ad19ca01d578a009ebb0ba1e12177a3adcbafe88ba5db439044.jpg)

(c) Cost Ratio = 50:1  
![](/api/attachments/VEBX67UK/fulltext/images/00dcff73a238b6bbedae11ee4b4dcfa042397599784f7931218c48d86089fdf6.jpg)

(d) Cost Ratio = 100:1  
![](/api/attachments/VEBX67UK/fulltext/images/ef5ec42710289357dfa8528089482cc779972807b67905af7bc74bff71baa90b.jpg)  
Fig. 5. Average misprediction costs of different tuning methods under QuadQuad Cost functions on the training data.

## 6. Conclusions

Practical forecasting problems often exhibit asymmetry in their cost structures. Classical cost functions, such as mean squared error, although analytically convenient and widely applied, are not appropriate for use in many practical applications. More realistic cost structures should be accounted for, either during model building or in a post-hoc model tuning step.

Following Bansal et al. [4], we have proposed an extended tuning method for cost-sensitive regression. The BSZ method becomes a special case of the proposed method, where the tuning function is linear and has a <sup>fi</sup>xed unit coef<sup>fi</sup>cient on the term of degree one. The proposed method can better <sup>fi</sup>t the training data by allowing <sup>fi</sup>ner tuning. In particular, the linear tuning function is more <sup>fl</sup>exible than the BSZ method and does not increase the model complexity. Higher degree of tuning may also be found bene<sup>fi</sup>cial depending on the problem and cost setting. As this approach does not require modifying the underlying model learning method, it is applicable to a wide range of cost functions and can be easily implemented to work with models generated by commercial software packages. It can therefore be applied in practical applications, which may prescribe special cost functions and software packages. Furthermore, when a decision maker cannot precisely pin down the cost function and needs to evaluate a set of possible cost functions, this approach provides an additional advantage over methods that require model rebuilding whenever the cost function changes.

We evaluated the cost-sensitive regression models in the domain of loan charge-off forecasting using recent real-world banking data. The impressive evaluation results of our method suggest that it could be of major help to forecasters trying to <sup>fi</sup>ne-tune their forecasting process. It has implications speci<sup>fi</sup>cally in the domain of loan chargeoff prediction. Recently, the nation's largest banks were put under stress-test to determine which ones were <sup>fi</sup>t to receive federal funds [21]. Among the factors the test examined was the amount of money that would be left in the bank's reserves when its loans default. A bank that can predict its loan charge-offs effectively would be in a good position to <sup>fi</sup>gure out how much money to put in its loan loss reserves. A classic example is JPMorgan, which managed to remain <sup>fi</sup>nancially healthy when several other big banks started falling one by one, primarily because it had kept \$23 billion in its rainy-day fund [21]. Amid the current <sup>fi</sup>nancial crisis, it is even more critical for banks to have systems in place for forecasting loan losses and have adequate provisions as a safeguard against those losses. As the events during the last few months indicate, if a bank does not have suf<sup>fi</sup>cient loan loss reserves, the consequences could be dire. In the second quarter of 2009 alone, 45 banks failed, adding to a total of 81 for the <sup>fi</sup>rst two quarters, thereby exerting enormous pressure on the government's deposit insurance fund [14].

Our work also opens up several avenues for future research. First, the approach can be applied in other forecasting problems. Second, other cost functions and base regression methods can be evaluated. Third, the consequences of relaxing some of the assumptions made in

[10] P.F. Christoffersen, F.X. Diebold, Further results on forecasting and model selection under asymmetric loss, Journal of Applied Econometrics 11 (5) (1996) 561–572.

(a) Cost Ratio = 10:1  
![](/api/attachments/VEBX67UK/fulltext/images/dc9768d7d29f69cbd6a25ac1cfdc7eb5db350d05e1303b82e39e2db7f1c68de5.jpg)  
(c) Cost Ratio = 50:1

(b) Cost Ratio = 20:1  
![](/api/attachments/VEBX67UK/fulltext/images/57afc2900d78495420f7d6c155cb501bb0fc2101dd2a99451638a26fff46237e.jpg)  
(d) Cost Ratio = 100:1

![](/api/attachments/VEBX67UK/fulltext/images/1ebbdc7db9acce798ecaba46a30098bb6b342ba0cdcea7e06f38df4717a14cf9.jpg)

![](/api/attachments/VEBX67UK/fulltext/images/547ba2e3f1c1fcb92b25f06b892584dbebfae2177351b66ac346f0357594c2dd.jpg)  
Fig. 6. Average misprediction costs of different tuning methods under QuadQuad cost functions on the testing data

this paper can be studied. When the optimal tuning function of a given form under a particular cost function cannot be found by an ef<sup>fi</sup>cient algorithm due to the existence of multiple local optima, other heuristic methods, such as evolutionary computation, tabu search, and simulated annealing, may be applied. Finally, the proposed posthoc tuning approach could be compared, both analytically and empirically, with methods that explicitly incorporate cost functions during model building. In this paper, we have focused on extending the BSZ method, which is the only post-hoc tuning method for costsensitive regression available in the literature. We have demonstrated that the extended tuning method outperforms the BSZ method. Comparing the two general approaches for cost-sensitive regression, i.e., post-hoc tuning and direct cost-sensitive model building, demands extensive research, which we leave for the future.

## Table 7

Average training and tuning times (in seconds).

<table><tr><td rowspan="2">Cost function</td><td rowspan="2">Method</td><td rowspan="2">Training</td><td colspan="5">Tuning</td></tr><tr><td>BSZ</td><td>Linear</td><td>Quadratic</td><td>Cubic</td><td>Quartic</td></tr><tr><td rowspan="3">LinLin</td><td>LR</td><td>0.49</td><td>0.16</td><td>1.40</td><td>4.24</td><td>4.35</td><td>4.52</td></tr><tr><td>M5</td><td>16.56</td><td>0.20</td><td>1.71</td><td>3.54</td><td>5.43</td><td>5.98</td></tr><tr><td>NN</td><td>45.48</td><td>0.20</td><td>1.53</td><td>4.23</td><td>6.98</td><td>7.53</td></tr><tr><td rowspan="3">QuadQuad</td><td>LR</td><td></td><td>0.16</td><td>1.49</td><td>5.73</td><td>13.68</td><td>20.63</td></tr><tr><td>M5</td><td></td><td>0.20</td><td>1.68</td><td>4.03</td><td>27.94</td><td>40.67</td></tr><tr><td>NN</td><td></td><td>0.20</td><td>1.70</td><td>5.71</td><td>29.40</td><td>35.14</td></tr></table>

## References

[1] A.A. A<sup>fifi</sup>, V. Clark, Computer-Aided Multivariate Analysis, 3rd ed.Chapman & Hall, 1996.

[2] J. Aitchison, I.R. Dunsmore, Statistical Prediction Analysis, Cambridge University Press, London, 1975.

[3] E. Alfaro, N. García, M. Gámez, D. Elizondo, Bankruptcy forecasting: An empirical comparison of AdaBoost and neural networks, Decision Support Systems 45 (1) (2008) 110–122.

[4] G. Bansal, A.P. Sinha, H. Zhao, Tuning data mining methods for cost-sensitive regression: a study in loan charge-off forecasting, Journal of Management Information Systems 25 (3) (2008) 317–338.

[5] J.O. Berger, Statistical Decision Theory: Foundations, Concepts, and Methods, Springer-Verlag, New York, 1980.

[6] M. Cain, C. Janssen, Real estate price prediction under asymmetric loss, Annals of the Institute of Statistical Mathematics 47 (3) (1995) 401–414.

[7] R.A. Carbonneau, G.E. Kersten, R.M. Vahidov, Pairwise issue modeling for negotiation counteroffer prediction using neural networks, Decision Support Systems 50 (2) (2011) 449–459.

[8] M. Cecchini, H. Aytug, G.J. Koehler, P. Pathak, Making words work: Using <sup>fi</sup>nancial text as a predictor of financial events Decision Support Systems 50 (1) (2010) 164–175

[9] N. Chawla, K. Bowyer, L. Hall, W. Kegelmeyer, SMOTE: Synthetic minority oversampling technique, Journal of Arti<sup>fi</sup>cial Intelligence Research 16 (2002) 321–357.

[11] P.F. Christoffersen, F.X. Diebold, Optimal prediction under asymmetric loss Econometric Theory 13 (1997) 808-817.

[12] S.F. Crone, Training arti<sup>fi</sup>cial neural networks for time series prediction using asymmetric cost functions, Proceedings of the 9th International Conference on Neural Information Processing, 2002, pp. 2374–2380.

[13] S.F. Crone, S. Lessmann, R. Stahlbock, Utility based data mining for time series analysis: Cost-sensitive learning for neural network predictors, Proceedings of the 1st International Workshop on Utility-based Data Mining, Chicago, II. 2005. pp. 59–68.

[14] E. Dash, Bank losses drain deposit fund, F.D.I.C. reports, The New York Times, August 28, 2009.

[15] P. Domingos, MetaCost: A general method for making classi<sup>fi</sup>ers cost sensitive, Proceedings of the 5th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Diego, CA, 1999, pp. 155–164.

[16] C. Drummond, R. Holte, Exploiting the cost (in)sensitivity of decision tree splitting criteria, Proceedings of the 17th International Conference on Machine Learning Stanford, CA, 2000, pp. 239–249.

[17] C. Elkan, The foundations of cost-sensitive learning, Proceedings of the 17th International Joint Conference on Arti<sup>fi</sup>cial Intelligence, 2001, pp. 973–978.

[18] W. Fan, S.J. Stolfo, J. Zhang, P.K. Chan, AdaCost: Misclassi<sup>fi</sup>cation cost-sensitive boosting, Proceedings of the 16th International Conference on Machine Learning, Bled, Slovenia, 1999, pp. 97–105.

[19] T.S. Ferguson, Mathematical Statistics: A Decision Theoretic Approach, Academic Press, New York, 1967.

[20] J. Gama, Iterative Bayes, Intelligent Data Analysis 4 (6) (2000) 475–488.

[21] S. Gandel, How stressed is your bank? Time, March 2 (2009) 28–29.

[22] C.W.J. Granger, Prediction with a generalized cost of error function, Operational Research Quarterly 20 (2) (1969) 199–207.

[23] D. Hand, H. Mannila, P. Smyth, Principals of Data Mining, The MIT Press, Cambridge, Massachusetts, 2001.

[24] D. Margineantu, Class probability estimation and cost-sensitive classi<sup>fi</sup>cation decisions, Proceedings of the 13th European Conference on Machine Learning, Helsinki, Finland, 2002, pp. 270–281.

[25] M. Niglio, Multi-step forecasts from threshold ARMA models using asymmetric loss functions, Statistical Methods and Applications 16 (3) (2007) 395–410.

[26] J.R. Quinlan, Learning with continuous classes, Proceedings of the 5th Australian Join Conference on Arti<sup>fi</sup>cial Intelligence, World Scienti<sup>fi</sup>c, Singapore, 1992, pp. 343–348.

[27] D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning internal representations by error propagation, in: D.E. Rumelhart, J.L. McClelland (Eds.), Parallel Distributed Processing, MIT Press, Cambridge, MA, 1986, pp. 318–362.

[28] S. Sarkar, R.S. Sriram, Bayesian models for early warning of bank failures, Management Science 47 (11) (2001) 1457–1475.

[29] A.P. Sinha, J.H. May, Evaluating and tuning predictive data mining models using receiver operating characteristic curves, Journal of Management Information Systems 21 (3) (2005) 249–280.

[30] K.Y. Tam, M.Y. Kiang, Managerial applications of neural networks: the case of bank failure predictions, Management Science 38 (7) (1992) 926–947.

[31] R.D. Thompson, A.P. Basu, Asymmetric loss functions for estimating system reliability, in: D.A. Berry, K.M. Chaloner, J.K. Geweke (Eds.), Bayesian Analysis in Statistics and Econometrics, John Wiley & Sons, 1996, pp. 471–482.

[32] K.M. Ting, An instance-weighting method to induce cost-sensitive trees, IEEE Transactions on Knowledge and Data Engineering 14 (3) (2002) 659–665.

[33] L. Torgo, R. Ribeiro, Utility-based regression, Proceeding of the 11th European Conference on Principles and Practice of Knowledge Discovery in Databases, Warsaw, Poland, 2007, pp. 597–604.

[34] H.R. Varian, A Bayesian approach to real estate assessment, in: S.E. Fienberg, A Zellner (Eds.), Studies in Bayesian Econometrics and Statistics: In honor of Leonard J, Savage North-Holland Pub, Amsterdam, 1974, pp. 195–208.

[35] P. Whittle, Prediction and Regulation, 2nd Ed.University of Minnesota Press, Minneapolis. 1983.

[36] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Technigues. 2nd EdMorgan Kaufmann. 2005.

[37] J.-Y. Yeh, T.-H. Wu, C.-W. Tsao, Using data mining techniques to predict hospitalization of hemodialysis patients, Decision Support Systems 50 (2) (2011) 439–448.

[38] B. Zadrozny, J. Langford, N. Abe, Cost-sensitive learning by cost-proportionate example weighting, Proceedings of the 3rd IEEE International Conference on Data Mining, Melbourne, Florida, 2003, pp. 435–442.

[39] A. Zellner, Bayesian estimation and prediction using asymmetric loss functions, Journal of American Statistics Association 81 (394) (1986) 446–451.

[40] A. Zellner, M.S. Geisel, Sensitivity of control to uncertainty and form of the criterion function, in: D.G. Watts (Ed.), The Future of Statistics, Academic Press, New York, 1968, pp. 269–289.

[41] H. Zhao, A multi-objective genetic programming approach to developing Pareto optimal decision trees, Decision Support Systems 43 (3) (2007) 809–826.

[42] H. Zhao, Instance weighting versus threshold adjusting for cost-sensitive classi<sup>fi</sup>cation, Knowledge and Information Systems 15 (3) (2008) 321–334.

Huimin Zhao is an Associate Professor of MIS at the Sheldon B. Lubar School of Business, University of Wisconsin–Milwaukee. He earned his Ph.D. in MIS from The University of Arizona. His current research interests are in the areas of data mining and recommendation systems. His research has been published in several journals, including Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man, and Cybernetics, Information Systems, Data and Knowledge Engineering, Journal of Management Information Systems, Journal of the Association for Information Systems, and Decision Support Systems. He serves on the editorial review board of the Journal of Database Management and as the treasurer of the INFORMS College on Artificial Intelligence. He served as a co-chair of the 19th Workshop on Information Technologies and Systems in 2009 and a co-chair of the 5th INFORMS Workshop on Data Mining and Health Informatics in 2010.

Atish P. Sinha is a Professor of MIS at the Sheldon B. Lubar School of Business, University of Wisconsin–Milwaukee. He earned his Ph.D. in business, with a concentration in Arti<sup>fi</sup>cial Intelligence, from the University of Pittsburgh. His current research interests are in the areas of business intelligence, data mining, text mining, data warehousing, web analytics, and service-oriented computing. His research has been published in several journals, including Communications of the ACM, Decision Support Systems, IEEE Transactions on Engineering Management, IEEE Transactions On Software Engineering, IEEE Transactions On Systems, Man, And Cybernetics, Information Systems Research, International Journal of Human-Computer Studies, Journal of the Association for Information Systems, and Journal of Management Information Systems. Professor Sinha is a member of ACM, AIS, and INFORMS. He is currently serving as the co-chair of the 6th International Conference on Design Science Research in Information Systems and Technology (DESRIST) and served as the co-chair of the 16th Workshop on Information Technologies and Systems (WITS) in 2006.

Gaurav Bansal is an Assistant Professor of MIS/Statistics at the University of Wisconsin–Green Bay. He earned his Ph.D. in MIS from the University of Wisconsin– Milwaukee, M.B.A from Kent State University, and B.E. in Mechanical Engineering from Madan Mohan Malaviya Engineering College, UP, India. His current research interests are in the areas of information privacy and security, trust, e-commerce, and data mining. His research has been published in Journal of Management Information Systems, Decision Support Systems, and Journal of Organizational Computing and Electronic Commerce. His research was nominated for best paper award at International Conference on Information Systems (ICIS) in 2008 and Americas Conference on Information Systems (AMCIS) in 2010. He has been track chair for privacy and security mini-track at Americas Conference on Information Systems (AMCIS) in 2009. 2010. and 2011. He also served in the program committee of the 5th Midwest AIS Conference in 2010. He is also the conference chair of the 7th Midwest AIS Conference, UW-Green Bay. He is a member of the AIS
