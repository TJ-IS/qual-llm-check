---
otero_id: 28473
otero_key: "4XQN4M5Q"
title: "Estimating Life Cycle Sales of Technology Products with Frequent Repeat Purchases: A Fractional Calculus-Based Approach"
authors: "Aslan Lotfi; Zhengrui Jiang; Ali Lotfi; Dipak C. Jain"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1131"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Estimating Life Cycle Sales of Technology Products with Frequent Repeat Purchases: A Fractional Calculus-Based Approach

Aslan Lotfi,<sup>a</sup> Zhengrui Jiang,<sup>b,</sup>\* Ali Lotfi,<sup>c</sup> Dipak C. Jain<sup>d</sup>

<sup>a</sup> Robins School of Business, University of Richmond, Richmond, Virginia 23173; <sup>b</sup> Business School, Nanjing University, Nanjing, Jiangsu 210093, China; <sup>c</sup> Ivey Business School, Western University, London, Ontario N6G 0N1, Canada; <sup>d</sup> China Europe International Business School Pudong, Shanghai 201206, P.R. of China

Contact: alot<sup>fi</sup>@richmond.edu (AsL); zjiang@nju.edu.cn, https://orcid.org/0000-0002-8576-7643 (ZJ); alot<sup>fi</sup>.phd@ivey.ca (AlL); dipakcjain@ceibs.edu (DCJ)

Received: February 13, 2021 Revised: September 22, 2021; January 8, 2022 Accepted: March 13, 2022 Published Online in Articles in Advance: May 11, 2022

https://doi.org/10.1287/isre.2022.1131

Copyright: © 2022 INFORMS

Abstract. Accurately predicting the sales trajectory of a product in its life cycle is critically important for <sup>fi</sup>rms’ medium- and long-term planning. Because classic product-diffusion models such as the Bass model consider only initial product purchases, they are ill-<sup>fi</sup>tted for sales prediction for today’s technology products with a shorter life cycle and frequent repeat purchases or subscription renewals. Despite the long tradition of product diffusion research, there exists no viable model option when repeat purchases constitute a large proportion of product sales. The present study introduces a new sales growth model, termed the generalized diffusion model with repeat purchases (GDMR), to <sup>fi</sup>ll this void. The GDMR formulates the growth rate of sales using a noninteger-order integral equation rather than the integer-order differential equation typically adopted in existing diffusion models. The GDMR is parsimonious and easy to implement. Empirical results show that the GDMR <sup>fi</sup>ts sales data with varying proportions of repeat purchases quite well, making it suitable for predicting sales of a wide variety of products. In addition, the GDMR can be extended to incorporate marketing mix variables, thus enhancing its applicability in business decision making. Furthermore, using both real and simulated data, we show that the GDMR can reliably recover a product’s adoption trend using only sales data, thus cementing its theoretical validity and empirical effectiveness. Finally, we show that the GDMR is superior to generic time series and machine learning models in predicting future produc sales.

History: Ram Gopal, Senior Editor; Wenjing Duan, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.1131.

Keywords: diffusion of innovations repeat purchases replacements multiunit ownerships fractional calculus

## 1. Introduction

Predictive analytics play an important role in organizations’ decision-making processes and, thus, are increasingly embraced by the information systems community (e.g., Shmueli and Koppius 2011, Fang et al. 2021). In particular, accurately predicting the sales trajectory of a product in its life cycle is critically important for <sup>fi</sup>rms’ medium- and long-term operational and strategic planning.

Empirical evidence shows that, in many product life cycles, the sales growth rate follows a bell-shaped curve or, equivalently, the cumulative sales follows an S-shaped curve (Rogers 2003), thus numerous bell- or S-shaped diffusion models are proposed to analyze and predict the sales trajectory in a product life cycle (Mahajan et al. 2000, Bass 2004). The most well-known diffusion model is probably the Bass model (Bass 1969). Since its inception, thanks to its empirical performance and ease of implementation, the Bass model has been applied in various disciplines, such as marketing, operations, and information systems (IS). In the IS literature, for instance, the Bass model and its extensions are applied to model the growth of information systems spending (Gurbaxani and Mendelson 1990), information systems outsourcing (Loh and Venkatraman 1992, Hu et al. 1997), sales of mainframe computing (Tam 1996), mobile telecommunication services (Niculescu and Whang 2012), multigeneration software platforms (Hann et al. 2016), free software products (Jiang and Sarkar 2009), and multigeneration technology products (Guo and Chen 2018, Jiang et al. 2019).

It is important to note that diffusion models, represented by the Bass model, count only <sup>fi</sup>rst-time adoptions of a product. For instance, when a consumer purchases a product for the <sup>fi</sup>rst time, the consumer turns from a “nonadopter” to an “adopter.” Subsequently, a consumer’s repurchases of the same hardware product or subscription renewals for the same software product should not be counted as new adoptions. In fact, to avoid any confusion, Bass clari<sup>fi</sup>es in his seminal work that the Bass model is concerned “only with the timing of the initial purchase” (Bass 1969, p. 215). For this reason, we use adoptions, initial purchases, and <sup>fi</sup>rst-time purchases interchangeably in this study.

Because diffusion models capture only <sup>fi</sup>rst-time purchases, they can be used to estimate sales when repeat purchases are insigni<sup>fi</sup>cant. Therefore, Bass (1969) and many subsequent studies test the Bass model using sales data for consumer durables, such as TV sets and washing machines (Mahajan et al. 2000), of which repeat purchases are infrequent at least in the initial time periods, and for the diffusion of technologies/practices (e.g., agricultural technologies, outsourcing) (Hu et al. 1997, Mahajan et al. 2000) for which recounting generally does not occur. Today’s technology products, including both hardware and software products, however, often have frequent releases of new versions or generations, and some consumers tend to keep buying new product generations or renewing subscriptions. Furthermore, unlike decades ago, consumers owning multiple units of the same (or similar) products is becoming increasingly common. In the presence of such frequent repeat purchases, traditional diffusion models are no longer applicable for predicting a product’s sales trajectory. A sales growth model that counts repeat purchases is needed.

A product’s sales growth rates with and without repeat purchases are illustrated in Figure 1. If repeat purchases are insigni<sup>fi</sup>cant, the market saturation effect comes into play; hence, after a market peak is reached, the rate of adoptions drops monotonically and asymptotically approaches zero. This trend is illustrated by the symmetric dashed curve shown in Figure 1. If repeat purchases are signi<sup>fi</sup>cant and counted, the growth of sales often exhibits an asymmetrical bell-shaped pattern as illustrated by the solid curve shown in Figure 1. Even though Bass acknowledges that his model is designed for initial purchases only, the Bass model is frequently applied to <sup>fi</sup>t sales data that include both initial and repeat purchases.

Figure 1. Sales vs. Adoptions  
![](/api/attachments/4XQN4M5Q/fulltext/images/da70724853ac88c044137d9790c097b7237318ba8f267d893cd3ce8682d35684.jpg)

When signi<sup>fi</sup>cant repeat purchases exist, the model <sup>fi</sup>tting and prediction accuracy of the Bass model is likely poor and the parameter estimates biased or misleading.

Given the need, it seems intuitive that researchers would develop robust sales growth models to account for frequent repeat purchases. Surprisingly, after an exhaustive literature search, we <sup>fi</sup>nd that this is hardly the case. As we elaborate in the next section, limited attempts have been made to model repeat purchases, and the resulting models all have some limitations. The lack of robust repeat purchase models can be attributed to the challenges in formulating repeat purchase components of sales that vary with time. Given the clear void, this study aims to develop a robust sales model that incorporates both adoptions and repeat purchases and is suitable for a wide variety of technology products.

## 2. Prior Literature on Diffusion Models with Repeat Purchases

Because of the vast body of literature on the diffusion of innovations and new product diffusions (Mahajan et al. 2000, Rogers 2003), we focus our literature review on extended diffusion models with repeat purchases. In particular, researchers propose model extensions to account for repeat product purchases made to replace existing product units or for adopting multiple product units. Olson and Choi (1985) propose a model assuming that sales comprise only adoptions and replacements and the replacement hazard function follows the Rayleigh distribution (Papoulis and Pillai 2002). The Olson–Choi model is developed for cases in which the data for the number of products in use is available. Kamakura and Balasubramanian (1987) propose a similar model that generates longterm forecasts by incorporating the adoption and replacement components of sales. Bene<sup>fi</sup>ting from a more <sup>fl</sup>exible hazard function to capture replacement purchases, their model is applicable with or without data for replacement sales. Their model uses information from similar products when data for replacement purchases is not available. Steffens and Balasubramanian (1998) further advance the modeling of replacement sales by allowing the distribution of the service life of replaced products to vary over time. Lee and Huh (2017) introduce a replacement diffusion model for the growth dynamics of technologies and evaluate the performance of their model using sales data of mobile handsets in South Korea. Lee and Huh’s (2017) model does not include multiunit ownerships.

The aforementioned models have their focus on adoptions and replacement purchases. There are other models from the prior literature that consider other components of sales, in particular, multiunit ownership purchases. Dodson and Muller (1978) propose a model that captures the type of asymmetric sales trend illustrated in Figure 1 without decomposing sales into multiple components. The market they consider comprises three groups, that is, those who are not aware of the product, those who are aware of the product but have not made a purchase, and those who have purchased the product. Although the portrayed interaction between adopters and nonadopters is insightful, their model cannot be operationalized if the data for the different market groups is not available.

Based on econometric and simulation models, Bayus et al. (1989) incorporate <sup>fi</sup>rst-time, replacement, additionalunit, and institutional sales into their analysis of color television set sales. As stated by Steffens (2003), the Bayus et al. (1989) model is developed to perform well over short terms. Steffens (2003) presents a model for sales resulting from multiunit ownership purchases based on the Bass model. His model differs from Bayus et al. (1989) in that it imposes a saturation level on multiunit ownerships, which makes the model applicable for longer time frames.

Researchers also develop models for repeat purchases for a speci<sup>fi</sup>c industry. For instance, Lilien et al. (1981) and Rao and Yamada (1988) propose a specialized model to project sales of prescription drugs as a function of a focal pharmaceutical company’s own detailing effect, competitors’ detailing effect, and word of mouth. Because these models are speci<sup>fi</sup>cally designed for prescription drugs, they cannot be used to predict sales of general product categories.

More recently, machine learning–based models have also been used to predict sales. For example, Baesens et al. (2002) use a Bayesian neural network model to capture repeat purchases in the context of direct marketing. Based on comprehensive feature engineering techniques, Liu et al. (2016) predict returning customers of a given merchant in e-commerce. Concentrating on the fashion retail industry, Loureiro et al. (2018) examine the use of deep neural networks in predicting sales in future seasons for new products. However, these approaches generally require rich data sets for predictor variables, whereas the model we propose produces fairly accurate sales predictions even if only aggregate sales data are available.

## 3. Defining Repeat Purchases

Repeat purchases may result from either product replacements (e.g., buying a new laptop computer to replace an old one) or multiunit ownerships (e.g., one household owning multiple computers). Drivers of replacement purchases vary from nondurable to durable products. For nondurable products, replacement usually occurs as the result of consumption (Kamakura and Balasubramanian 1987). For durable products, replacement typically takes place when a product under consumption fails to meet the requirements of the user.

Motivations behind multiunit adoptions may vary, including for use in different locations and acquiring extra capacity or different functionalities.

We draw on the typology of product innovation by Henderson and Clark (1990) to de<sup>fi</sup>ne our unit of anal ysis. Henderson and Clark (1990) classify product innovations based on the number of changes to a product’s core components and product architecture. For example, a product innovation is considered radi cal if it introduces a new set of designs to the core components and a new architecture that links the core components. If the design of the core components and the architecture undergo only small improvements, the innovation is deemed incremental. In this study, we count a new purchase as a repeat purchase only if the newly purchased product is the same as the original product or a variation of the original product resulting from incremental innovation. In other words, our unit of analysis is a group or line of prod ucts or innovations that differ incrementally.

## 4. Generalized Diffusion Model with Repeat Purchases

Developing models to capture a diffusion of innovation process is a central part of the diffusion of innovation research. Pioneering scholars present various models to estimate and predict the diffusion of innovation in a population. Applying a bell-shaped growth curve to capture a noncumulative diffusion process is at the center of these endeavors. This line of work is represented by the Bass model (Bass 1969), which provides the foundation of the model we propose in this study.

The Bass model stipulates that the noncumulative rate of adoptions of a product at time $t , y ( t )$ , and the cumulative number of adoptions, Y(t), satisfy the fol lowing <sup>fi</sup>rst order differential equation:

$$
\frac {d Y (t)}{d t} = y (t) = p m + (q - p) Y (t) - \frac {q}{m} Y ^ {2} (t), t \geq 0,\tag{1}
$$

where $p$ and q are the coefficient of innovation and coeffi cient of imitation, respectively, and m represents the size of the market potential. Note that Equation (1) is an integer-order differential equation. Solving this equation with the initial condition Y(0) 0 yields $\begin{array} { r } { \dot { Y ( t ) } = \frac { m ( 1 - e ^ { - \left( p + q \right) t } ) } { ( 1 + \frac { q } { p } e ^ { - \left( p + q \right) t } ) } \operatorname { a n d } y ( t ) = \frac { m \left( p + q \right) ^ { 2 } } { p } \frac { e ^ { - \left( p + q \right) t } } { \left( 1 + \frac { q } { p } e ^ { - \left( p + q \right) t } \right) ^ { 2 } } . } \end{array}$

The noncumulative version of the Bass diffusion curve, y(t), effectively captures the bell-shaped growth pattern of adoptions, whereas the cumulative version Y(t) exhibits the well-known S-shaped curve.

Newer diffusion models often generalize earlier works. Model extensions mostly concentrate on revising the right-hand side of the growth differential equation represented by Equation (1). Adopting a different modeling approach, we present a generalization that extends both the left- and right-hand sides of the equation. Speci<sup>fi</sup>cally, we draw upon a branch of mathematics called fractional calculus, which generalizes differentiation and integration so that noninteger-order differential and integral operators become possible. Interested readers can refer to Samko et al. (1993), Podlubny (1999), Kilbas et al. (2006), and Baleanu et al. (2012) for reviews of the fractional calculus literature.

We name the model we propose the generalized $d i f f u -$ sion model with repeat purchases (GDMR). As detailed in the next section, the model formulates product sales as a fractional integral of the diffusion function de<sup>fi</sup>ned by the Bass model and produces an asymmetrical bellshaped sales growth curve as illustrated in Figure 1.

4.1. Integrating Adoptions and Repeat Purchases The GDMR assumes that a noncumulative sales trend, S(t), is governed by the following fractional integral equation:

$$
S (t) = I ^ {\beta} y (t) = I ^ {\beta} (p m + (q - p) Y (t) - \frac {q}{m} Y ^ {2} (t)), t \geq 0,\tag{2}
$$

in which $Y , y , p , q ,$ and m represent cumulative adoptions, noncumulative adoptions, coef<sup>fi</sup>cient of innovation, coef<sup>fi</sup>cient of imitation, and market potential, respectively. The parameter $\beta ( 0 \leq \beta \leq 1 )$ , termed the coefficient of repeat purchases, is a new parameter added to the Bass model, and its value determines the proportion of repeat purchases. $I ^ { \beta }$ is a noninteger fractional integral of order $\beta .$ When $\beta = 0 .$ , the GDMR reduces to the Bass model; thus, the Bass model is a special case of the GDMR.

We next explain the rational for Equation (2) and the role of the newly added coef<sup>fi</sup>cient of repeat purchases. We assume that a consumer’s adoption (<sup>fi</sup>rsttime purchase) and repeat purchases do not occur at the same time. For instance, a repeat purchase made at time t corresponds to an adoption that has taken place prior to time $t ,$ that ${ \mathrm { i } } s ,$ in [0, t). Therefore, the rate of repeat purchases at t depends on the cumulative number of existing adoptions in [0, t) and the rate at which these adopters make repeat purchases at t. To understand this factor, we <sup>fi</sup>rst consider a high repeat purchase scenario in which the average frequency of repeat purchase equals one, implying that, on average, each existing adopter makes one repeat purchase in each unit time. We call this scenario the periodic repeat purchases scenario. A good example of this scenario is that consumers renew their subscription to a software product every year. Under this scenario, the rate of repeat purchases at time t equals the cumulative number of adoptions just before time t. This number is added to the instantaneous rate of adoption exactly at time t to produce the sales rate at t. This means that the sales rate at time t equals the cumulative number of adoptions up to and including time t. Mathematically, this entails that, under the periodic repeat purchases scenario, sales at time t is a <sup>fi</sup>rst order integration of adoptions in [0, t]. Formally, we have

$$
S (t) = \int_ {0} ^ {t} y (\tau) d \tau = Y (t) = I ^ {\beta = 1} y (t).\tag{3}
$$

Therefore, in this periodic repeat purchases scenario, the noncumulative sales rate at time t equals the cumulative number of adoptions at time t, hence following an S-shaped curve. The coef<sup>fi</sup>cient of repeat purchases (β) in Equation (3) and the average frequency of repeat purchases both equal one. For scenarios in which the frequency of repeat purchases is greater than one, a solution is provided in Online Appendix A.

We next examine another boundary scenario, in which no repeat purchase occurs; hence, sales comprise only adoptions. We call this the adoption-only scenario, under which the sales rate follows the noncumulative adoption rate de<sup>fi</sup>ned by the Bass model, which is essentially Equation (2) with $\beta = 0 :$

$$
S (t) = y (t) = I ^ {\beta = 0} y (t).\tag{4}
$$

In this case, the sales rate exhibits a symmetrical bell shaped curve. Here, the coef<sup>fi</sup>cient of repeat purchases (β) and the frequency of repeat purchases both equal zero.

In most practical scenarios, the average frequency of repeat purchases likely falls between the two boundary scenarios described. Speci<sup>fi</sup>cally, existing adopt ers, on average, make more than zero but less than one repeat purchases per unit time. Integrating such a rate of repeat purchases into the instantaneous adoption rate yields a sales curve that falls between the S-shaped curve (with $\beta = 1 )$ ) and the symmetrical bellshaped curve (with $\beta = 0 )$ . Mathematically, we use a fractional integral of noncumulative adoption in Equation (2) with $0 < \beta < 1$ to represent the sales rate under the intermediate scenario. In this scenario, the coef<sup>fi</sup>cient of repeat purchases (β) increases with the frequency of repeat purchases.

Under the intermediate scenario in which the order of the integral operator in Equation (2) lies between zero and one, the exact rate at which adoptions from τ $\epsilon \left[ 0 , t \right)$ result in repeat purchases at t depends on the formulation of the fractional integral we use to operationalize the GDMR. We elaborate on our choice of fractional integral for the GDMR in the next section.

The dynamics of the GDMR under the three dis cussed scenarios are illustrated in Figure 2. In this <sup>fi</sup>gure, the bottom bell-shaped curve represents the adoption-only scenario $( \beta = 0 ) .$ ; the top S-shaped curve depicts the periodic repeat purchases scenario $( \beta = 1 )$ )

Figure 2. Three Scenarios Under GDMR  
![](/api/attachments/4XQN4M5Q/fulltext/images/6e619d5331f9cf77f6e538baf5089b10410d082457fea2faaa260084a2db8be9.jpg)

In between the two boundary curves are intermediate curves corresponding to $0 < \beta < 1$ . Increasing the value of $\beta$ causes the sales curve to shift away from the symmetrical bell-shaped curve corresponding to $\beta = 0$ and move closer to the S-shaped curve corresponding to $\beta = 1$ , implying a higher sales rate resulting from more repeat purchases.

## 4.2. Model Operationalization

In order to apply the GDMR to determine the exact rate at which adoptions from $\tau \epsilon \left[ 0 , t \right)$ result in repeat purchases at t, we need to select the formulation for the fractional integral in Equation (2). We use the Reimann–Liouville integral (Kilbas et al. 2006) to operationalize the GDMR because of its superior performance. The Riemann–Liouville fractional integral of order $\theta > 0$ of a function f is de<sup>fi</sup>ned as

$$
I ^ {\theta} f (t) := \int_ {0} ^ {t} \frac {1}{\Gamma (\theta)} (t - \tau) ^ {\theta - 1} f (\tau) d \tau , \theta > 0, t > 0,\tag{5}
$$

and $\Gamma ( x )$ , the gamma function, for $x \in \mathbb { R } , x > 0 ,$ is $\Gamma ( x ) =$ $\int _ { 0 } ^ { \infty } t ^ { x - 1 } e ^ { - t } d t$ : Thus, we can also present the GDMR as

$$
S (t) = I ^ {\beta} y (t) = \int_ {0} ^ {t} \frac {1}{\Gamma (\beta)} (t - \tau) ^ {(\beta - 1)} y (\tau) d \tau , t > 0.\tag{6}
$$

Next, we elaborate on the rate of repeat purchases by adopters based on Equation (6).

In an important recent study, Tarasov (2018) proposes that fractional calculus can capture an economic process with memory in which memory is de<sup>fi</sup>ned as the dependence of an endogenous (predicted) variable at the present time on the history of the changes of an exogenous (predictor) variable in a time frame. Following Tarasov’s (2018) memory concept, we interpret that Equation (6) represents an economic process with a memory of adoptions from the past that generate repeat purchases at the present time.

## 4.3. Approximation and Dynamics of GDMR

Estimating parameters based on Equation (6) may pose challenges because of the complexity of computation associated with the fractional integral operator. Therefore, we need a mathematical operator that has desirable properties and is computationally feasible. We introduce the operator $I _ { n , k } ^ { \beta }$ instead of $I ^ { \beta }$ and reformulate the GDMR as $S ( t ) = I _ { n , k } ^ { \beta } y ( t )$ , where n and k are parameters of the approximate operator. Increasing the values of n and k results in $I _ { n , k } ^ { \beta }$ converging to $I ^ { \beta } .$ The detailed derivation of the approximate operator and its convergence to the original one are provided in Online Appendix B.

Based on the operationalization presented, we conduct numerical analysis to examine how the amount of repeat purchases changes with the coef<sup>fi</sup>cient of repeat purchases (β). The results are summarized in Figure 3, which illustrates how the GDMR sales curve varies with $\beta$ (the values of the other parameters are <sup>fi</sup>xed at $p = 0 . 0 0 5 , q = 0 . 6 ,$ , and $m = 1 )$ . This <sup>fi</sup>gure provides a clearer picture regarding how the sales curve changes with the value of the coef<sup>fi</sup>cient of repeat purchases (β). Consistent with our previous theoretical predictions, a higher $\beta$ value in the GDMR is linked to a higher sales curve, thus representing a higher level of repeat purchases.

## 4.4. Incorporating Marketing Mix Variables

It is well-understood that marketing mix variables (e.g., price and advertising) can affect a diffusion process. Likewise, it is expected that marketing mix variables can in<sup>fl</sup>uence the magnitude of repeat purchases and, subsequently, that of total sales. In this section, we examine how marketing mix variables can be incorporated into the GDMR.

Figure 3. Dynamics of GDMR with Respect to β (p <sub>-</sub> 0.005, q <sub>-</sub> 0.6, and m <sub>-</sub> 1)  
![](/api/attachments/4XQN4M5Q/fulltext/images/a09afe3d9dea930b166a43b39724a5d707720d4b7637f1633579979d4aeb13f0.jpg)

Prior research explores various ways of accounting for the in<sup>fl</sup>uence of marketing mix variables on the diffusion of products (Bass et al. 2000). Here, we implement the approach used in the generalized Bass model (GBM) (Bass et al. 1994). Speci<sup>fi</sup>cally, we incorporate possible marketing mix variables into cumulative sales in the GDMR as

$$
C u m S (t) = I ^ {\beta + 1} [ y (X (t)) ],\tag{7}
$$

where CumS(t) is cumulative sales, y is periodic adoptions, and X t is the cumulative marketing effort as de<sup>fi</sup>ned in the GBM. For instance, including price (pr) and advertising (Adv), X t can be expressed as

$$
X (t) = t + \gamma * l n \biggl [ \frac {P r (t)}{P r (0)} \biggr ] + \delta * l n \biggl [ \frac {A D V (t)}{A D V (0)} \biggr ],\tag{8}
$$

where $\gamma$ and $\delta$ are coef<sup>fi</sup>cients capturing the effects of changes in price and advertising, respectively. To differentiate it from the GDMR without marketing mix variables, we name the version with marketing mix variables the generalized diffusion model with repeat purchases and marketing mix variables (GDMRX). The GDMRX in its noncumulative form can be shown as

$$
S (t) = x (t) * I ^ {\beta} \big [ y (X (t)) \big ],\tag{9}
$$

where x(t) is noncumulative marketing effort as de<sup>fi</sup>ned in the GBM.

## 5. Performance Evaluation

We conduct empirical analyses to evaluate the performance of the GDMR against alternative models.

## 5.1. Benchmark Repeat Purchase Models

Because the GDMR captures multiple sales components, including adoptions, replacement purchases, and multiunit purchases, and all three sales components are expected to be present in our data sets, we need to compare the GDMR with alternative models that also include these components. However, because the literature on repeat purchase models is rather limited, we could not <sup>fi</sup>nd readily available models that explicitly incorporate the three components of sales. Therefore, we need to develop our own benchmarks based on models proposed in the prior literature.

We create two benchmark sales models that incorporate initial purchases, replacements, and multiunit ownerships. The <sup>fi</sup>rst model incorporates the Bass model fo initial purchases, the Kamakura and Balasubramanian (1987) (KB) replacements model, and the Bayus et al. (1989) (BHL) multiunit purchases model. We name this model the Bass–KB–BHL sales model. The second benchmark model comprises the same initial purchases and replacements models but uses a different multiunit purchase model developed by Steffens (2003). This model is named the Bass–KB–Steffens sales model. We empirically compare the GDMR against the two benchmark models in Sections 5.2 and 5.4.<sup>1</sup>

## 5.2. Model Fitting and N-Period-Ahead Prediction Using Only Sales Data

We use <sup>fi</sup>ve aggregate sales data sets to evaluate the model <sup>fi</sup>tting and N-period-ahead prediction accuracy of the GDMR and the two benchmarks. The data set include annual sales of notebook computers from years 2005 to 2014, PC total global annual sales from years 2006 to 2015 (Statista 2016a), DVD player sales in Australia from years 2003 to 2011 (Screen Australia, n.d.), iPad sales from the third quarter of year 2010 to the second quarter of 2017 obtained from Apple’s quarterly summaries, and Samsung tablet sales from year 2012 to 2019.<sup>2</sup>

For the <sup>fi</sup>rst two data sets, because of potential lefthand truncation, we add an intercept, $s _ { 0 } ,$ to the GDMR and benchmark models to help improve model estimation. For the other data sets, we do not add an intercept to the models because the more parsimonious form leads to just as good empirical results. Because our test data sets are for consumer electronics, in the benchmark models, we assume that the average life of the products is less than or equal to eight years.

Table 1. GDMR Parameter Estimates for Different Sales Processes

<table><tr><td></td><td> $\beta$ </td><td> $p$ </td><td> $q$ </td><td> $m$ </td><td> $s_0$ </td></tr><tr><td>Notebook</td><td>0.46(0.01)</td><td>0.019(0.01)</td><td>0.627(0.00)</td><td> $4.6 \times 10^8$ (0.02)</td><td> $4.8 \times 10^7$ (0.00)</td></tr><tr><td>PC</td><td>0.24(0.13)</td><td>0.014(0.18)</td><td>0.725(0.02)</td><td> $4.8 \times 10^8$ (0.07)</td><td> $2.3 \times 10^8$ (0.00)</td></tr><tr><td>DVD (Australia)</td><td>0.06(0.48)</td><td>0.08(0.00)</td><td>0.25(0.00)</td><td> $2.03 \times 10^7$ (0.00)</td><td>—</td></tr><tr><td>iPad</td><td>0.48(0.00)</td><td>0.05(0.00)</td><td>1.17(0.00)</td><td> $1.53 \times 10^8$ (0.00)</td><td>—</td></tr><tr><td>Samsung tablet</td><td>0.61(0.00)</td><td>0.09(0.00)</td><td>1.75(0.00)</td><td> $0.64 \times 10^8$ (0.00)</td><td>—</td></tr></table>

Note. Shown in parentheses are p-values used to judge statistical signi<sup>fi</sup>cance.

The GDMR estimates for the <sup>fi</sup>ve products are summarized in Table 1. As we can see from the tables, except for the parameter $\beta$ for PC global sales and DVD player sales in Australia and the parameters $p$ and m for PC sales, all other parameter estimates for all products are statistically signi<sup>fi</sup>cant, indicating a good overall model <sup>fi</sup>t. The insigni<sup>fi</sup>cant parameter estimates may be due to left-hand data truncation. The value of the coef<sup>fi</sup>cient of repeat purchases (β) ranges from 0.06 to 0.61, indicating that sales curves for these <sup>fi</sup>ve products lie between the bell- and S-shaped curves. Therefore, the traditional diffusion parameter values for $p , q ,$ and m are biased without explicitly incorporating repeat purchases in the model formulation. Furthermore, the estimate for $s _ { 0 }$ is statistically signi<sup>fi</sup>cant for the <sup>fi</sup>rst two products, showing that it is an effective way to address the left-hand data truncation issue.

We also compare the GDMR against the two benchmark models using the <sup>fi</sup>ve data sets; their model <sup>fi</sup>tting and prediction performance is summarized in Table 2. The <sup>fi</sup>tting accuracy is measured in terms of $R ^ { 2 }$ and mean absolute percentage error (MAPE). From the summary, it is clear that the GDMR, despite having fewer parameters, consistently leads to better <sup>fi</sup>ts than do the two benchmark models.

The prediction performance of the three models is evaluated based on the MAPE of one- and two-yearsahead sales predictions. The results in Table 2 show that, with the exception of the one-year-ahead prediction for notebook computers and two-years-ahead prediction for PCs, the prediction accuracy of the GDMR is better than that of the benchmark models.

The model <sup>fi</sup>tting results for the GDMR, Bass–KB– BHL, and Bass–KB–Steffens are depicted in Figure 4 for the <sup>fi</sup>ve data sets. For sales of iPads, DVD players in Australia, and Samsung tablets, the GDMR appears to <sup>fi</sup>t the data better than do the benchmarks after the sales process peaks. This can be attributed to the fact that the benchmark models overestimate the repeat purchase rate in the later stages of the product life cycle.

## 5.3. Performance Evaluation with Marketing Mix Variables

As shown in Section 4, the GDMR can be extended to the GDMRX (see Equation (7)) to incorporate the in<sup>fl</sup>uence of marketing mix variables, such as price and advertisement. We collect additional data to evaluate the performance of this extension model. Because the two benchmark models do not capture the impact of marketing mix variables, we compare the GDMRX with the baseline GDMR only.

Table 2. Comparison of Model Fit and Prediction Accuracy of GDMR and Benchmarks

<table><tr><td rowspan="3" colspan="2"></td><td rowspan="2" colspan="2">Full data fit</td><td colspan="2">Prediction accuracy</td></tr><tr><td colspan="2">Years ahead MAPE</td></tr><tr><td> $R^2$ </td><td>MAPE</td><td>One</td><td>Two</td></tr><tr><td rowspan="4">Notebook computer</td><td>GDMR</td><td>0.9995</td><td>1.68</td><td>14.46</td><td>8.79</td></tr><tr><td>Bass-KB-BHL</td><td>0.9054</td><td>10.09</td><td>6.83</td><td>31.09</td></tr><tr><td>Bass-KB-Steffens</td><td>0.9573</td><td>5.40</td><td>4.64</td><td>25.75</td></tr><tr><td>GDMR</td><td>0.9995</td><td>2.08</td><td>0.94</td><td>8.84</td></tr><tr><td rowspan="3">PC</td><td>Bass-KB-BHL</td><td>0.6731</td><td>5.25</td><td>10.28</td><td>8.35</td></tr><tr><td>Bass-KB-Steffens</td><td>0.8390</td><td>3.11</td><td>10.28</td><td>18.11</td></tr><tr><td>GDMR</td><td>0.9996</td><td>1.90</td><td>9.66</td><td>4.89</td></tr><tr><td rowspan="3">DVD player (Australia)</td><td>Bass-KB-BHL</td><td>0.7500</td><td>8.11</td><td>13.05</td><td>26.12</td></tr><tr><td>Bass-KB-Steffens</td><td>0.7500</td><td>8.11</td><td>13.05</td><td>26.12</td></tr><tr><td>GDMR</td><td>0.9999</td><td>1.34</td><td>3.10</td><td>2.16</td></tr><tr><td rowspan="2">iPad</td><td>Bass-KB-BHL</td><td>0.7763</td><td>15.31</td><td>14.55</td><td>37.84</td></tr><tr><td>Bass-KB-Steffens</td><td>0.8439</td><td>9.05</td><td>14.48</td><td>37.62</td></tr><tr><td rowspan="3">Samsung tablet</td><td>GDMR</td><td>0.9997</td><td>1.18</td><td>2.19</td><td>3.28</td></tr><tr><td>Bass-KB-BHL</td><td>0.8185</td><td>8.30</td><td>6.91</td><td>11.48</td></tr><tr><td>Bass-KB-Steffens</td><td>0.8439</td><td>9.070</td><td>15.21</td><td>37.62</td></tr></table>

![](/api/attachments/4XQN4M5Q/fulltext/images/809cf629d56ce43f732324ae78c7145dd53613915821c200ccd9b0fdb333de8e.jpg)

Figure 4. (Color online) Comparisons of Model Fitting for Different Sales Processes  
![](/api/attachments/4XQN4M5Q/fulltext/images/8aa8893587892fd9aa8416f4661bb08882f980e25a36fe7081e57803ec67f73a.jpg)

We use iPod sales from 2004 to 2014, obtained from Apple’s quarterly summaries, to illustrate the performance of the GDMRX. To obtain the average selling price of the iPod, we divide the revenue generated by iPod sales by the corresponding number of units sold. The comparison of model <sup>fi</sup>tting between the GDMR and the GDMRX is shown in Figure 5. The parameter estimates and model <sup>fi</sup>tting measures are summarized in Table 3. These results show that both the GDMR and the GDMRX perform well on the iPod sales data with the GDMRX having a slight edge in terms of sum of squared errors (SSE). This is not surprising given that the GDMRX is a more <sup>fl</sup>exible model than the GDMR.

Figure 5. (Color online) GDMR and GDMRX for the iPod Sales Data  
![](/api/attachments/4XQN4M5Q/fulltext/images/dc8b8d028f3504b2c28dee263ec1c9bf0e53b8b4d21db3426e6bbbda1227143a.jpg)

## 5.4. Performance Evaluation with Both Sales and Adoptions Data

We show that the GDMR performs well on aggregate sales data; however, we are not able to assess whether the adoption trend predicted by the GDMR closely matches the true adoption trend. To evaluate whether the GDMR can accurately recover a product’s adoption from sales data, we need to have both adoption and sales data for the same product. Such data are very rarely available in practice. Fortunately, after some extensive search, we are able to obtain separate adoption and sales data for DVD players in the United States from 1997 to 2018, and subsequently use these data to compare the GDMR with the benchmark models. The adoption data from 1997 to 2007 is derived by multiplying the penetration of DVDs in U.S. households reported by the Consumer Technology Association (Uncommon Wisdom Daily 2015) by the population of households in the United States (Statista 2016b). The corresponding sales data from 1997 to 2010 is reported by the Digital Entertainment Group (2009, 2010) and from 2014 to 2018 is reported by Statista (2019).<sup>3</sup>

Table 3. GDMR and GDMRX Parameter Estimates, $R ^ { 2 } ,$ , and SSE for iPod Sales

<table><tr><td></td><td> $\beta$ </td><td> $p$ </td><td> $q$ </td><td> $m$ </td><td> $\gamma$ </td><td> $R^{2}$ </td><td>SSE</td></tr><tr><td>GDMR</td><td>0.278(0.066)</td><td>0.037(0.004)</td><td>0.656(0.066)</td><td> $2.18 \times 10^{8}$  $(0.33 \times 10^{8})$ </td><td>—</td><td>0.9998</td><td> $9.8 \times 10^{13}$ </td></tr><tr><td>GDMRX</td><td>0.21(0.096)</td><td>0.027(0.01)</td><td>0.603(0.065)</td><td> $2.56 \times 10^{8}$  $(0.58 \times 10^{8})$ </td><td>-0.745(0.787)</td><td>0.9998</td><td> $8.4 \times 10^{13}$ </td></tr></table>

Notes. Values in parentheses represent standard errors. Estimation results are based on fitting the cumulative forms of the GDMR and GDMRX to cumulative sales data

Table 4. Parameter Estimates Based on DVD Player Adoptions and Sales in the United States (Two-Step Procedure)

<table><tr><td>Model</td><td> $R^{2}$ </td><td>SSE</td><td>Parameter</td><td>Estimate</td><td>P-value</td></tr><tr><td rowspan="3">Bass</td><td rowspan="3">0.9246</td><td rowspan="3"> $1.0 \times 10^{14}$ </td><td>p</td><td>0.003</td><td>0.23</td></tr><tr><td>q</td><td>0.769</td><td>0.00</td></tr><tr><td>m</td><td> $9.9 \times 10^{7}$ </td><td>0.00</td></tr><tr><td>GDMR</td><td>0.9923</td><td> $6.6 \times 10^{13}$ </td><td>β</td><td>0.48</td><td>0.00</td></tr></table>

Our model estimation using these data includes two steps. First, we <sup>fi</sup>t the Bass model to the noncumulative adoption data to estimate adoption parameters $p ,$ $q ,$ and m. Second, we treat the resulting adoption parameters as known and then <sup>fi</sup>t the GDMR to the sales data to estimate the coef<sup>fi</sup>cient of repeat purchases $\beta .$ The parameter estimates for the Bass model and the GDMR (β by the GDMR; $p , \ q ,$ and m by the Bass model), as summarized in Table 4, are mostly signi<sup>fi</sup>- cant. A similar estimation procedure is repeated for the benchmark models.

In addition to model <sup>fi</sup>tting, we also evaluate the models’ performance in eight-years-ahead (from 2011 to 2018) prediction of sales. The comparisons of <sup>fi</sup>ts and sales predictions are reported in Table 5 and depicted in Figure 6. From the table, it is clear that the

Table 5. Comparison of GDMR and Benchmarks Based on DVD Player Sales in the United States (Two-Step Procedure)

<table><tr><td></td><td>GDMR</td><td>Bass-KB-BHL</td><td>Bass-KB-Steffens</td></tr><tr><td>Fit  $R^{2}$ </td><td>0.9923</td><td>0.8057</td><td>0.9652</td></tr><tr><td>Fit mean squared error</td><td> $4.7 \times 10^{12}$ </td><td> $3.11 \times 10^{13}$ </td><td> $5.6 \times 10^{12}$ </td></tr><tr><td>Prediction MAPE</td><td>8.74</td><td>48.87</td><td>74.52</td></tr></table>

GDMR outperforms the two benchmarks in terms of model <sup>fi</sup>tting and sales prediction. From the <sup>fi</sup>gure, we can see that, once again, the GDMR curve matches the actual sales trend better than do the benchmark models. The GDMR’s prediction accuracy for 2014– 2018 sales is also much better than those of the benchmark models.

Note that the parameter values summarized in Table 5 and model <sup>fi</sup>tting shown in Figure 6 are obtained by <sup>fi</sup>rst <sup>fi</sup>tting the Bass model to the adoption data and subsequently the GDMR to the sales data. This two-step procedure is expected to produce more reliable adoption parameter $( m , p ,$ and $q )$ values but is unfortunately feasible only if the adoption data are available. In another test, we assume that, as in the previous cases, the adoption data are unavailable, and we <sup>fi</sup>t the GDMR directly to the sales data from 1997 to 2010 to obtain both adoption and repeat-purchase parameter values. For convenience, we term this the GDMR-sales procedure. We summarize the result of the GDMR-sales procedure when <sup>fi</sup>tting the GDMR to DVD player sales data from 1997 to 2010 in Table 6. By comparing the adoption parameter estimates in Tables 4 and 6, it is evident that the values of these parameters are remarkably similar, showing that the GDMR can effectively recover the adoption trend from just sales data.

The two-step procedure and the GDMR-sales procedure’s model <sup>fi</sup>tting performances are depicted in Figure 7. From the <sup>fi</sup>gure, we can see that the adoption and sales trends produced by the two procedures are highly consistent, further demonstrating the power of the GDMR.

Figure 6. (Color online) GDMR and Benchmarks Along with Bass Diffusion Curve Based on DVD Player Adoption and Sales in the United States (1997–2018)  
![](/api/attachments/4XQN4M5Q/fulltext/images/d2fe0dcad96167de8787221e5448a32456761177176f400f81542838146ef665.jpg)

Table 6. Parameter Estimates Based on DVD Player Sales in the United States (GDMR-Sales Procedure)

<table><tr><td> $\beta$ </td><td> $p$ </td><td> $q$ </td><td> $M$ </td><td> $R^{2}$ </td><td>SSE</td></tr><tr><td>0.47(0.06)</td><td>0.005(0.001)</td><td>0.7(0.062)</td><td> $1.0 \times 10^{8}$  $(1.4 \times 10^{7})$ </td><td>0.9967</td><td> $2.8 \times 10^{13}$ </td></tr></table>

Note. Values in parentheses represent standard errors.

Based on the DVD player data set, we also estimate the two benchmark models using a procedure similar to the GDMR-sales procedure to examine how accurately they can recover the adoption trend. The results show that Bass–KB–BHL and Bass–KB–Steffens perform signi<sup>fi</sup>cantly worse than the GDMR.

We also conduct simulations to generate adoption and sales data for a wide variety of products and then repeat the aforementioned GDMR-sales procedure using the simulated data to further evaluate the GDMR. The results again show that the GDMR is able to reliably separate repeat purchases from adoptions even when only aggregate sales data are used, thus further establishing the theoretical validity and empirical effectiveness of the GDMR. Further details of this evaluation are provided in Online Appendix C.

## 5.5. Comparison with Time Series and Machine Learning Models

In this section, we compare the GDMR with generic time series and machine learning models and elaborate on the GDMR’s theoretical and empirical advantages over these alternatives. From the theoretical perspective, generic time series and machine learning models are at a disadvantage compared with the GDMR in estimating a product’s market penetration and predicting product sales. First, these alternative models lack a structure to effectively follow the asymmetric bell-shaped sales trend that is widely observable in empirical sales data. The GDMR, on the other hand, is speci<sup>fi</sup>cally developed to estimate and predict product sales that exhibit an asymmetrical bell-shaped growth pattern. As a result, the GMDR can deliver accurate predictions of sales well into the future, whereas generic time series and machine learning models cannot. Second, as we empirically demonstrate in Section 5.4, the GDMR can not only estimate the aggregate sales trend, but also reliably recover the adoptions trend from sales data, whereas we do not believe there is a mechanism that can make generic time series and machine learning models simultaneously predict sales and adoption trends when only sales data are available. Third, as an extension of the Bass model (Bass 1969), the GDMR retains all the desirable properties of the Bass model, including the latter’s behavioral interpretations, whereas time series and machine learning models are more black box in nature and much less interpretable. Fur thermore, the GDMR allows us to draw into the huge body of knowledge in the literature on diffusion of innovations, whereas generic time series or machine learning models do not offer such an advantage.

What if we ignore the GDMR’s theoretical advantages and just compare the different models’ performance in predicting aggregate sales? We conduct a series of experiments to answer this question. Using U.S. DVD player data, we evaluate how the GDMR fares against the autoregressive integrated moving average (ARIMA), long short-term memory (LSTM), K-nearest neighbors (KNN), and random forest models in predicting future sales. In addition, we compare the GDMR with Holt’s exponential smoothing model, which is known to be suitable for time series data with a trend (Klan et al. 2008).

The U.S. DVD player sales data set has an observation window of 22 years. We try three different training/testing splits with this data set, that is, using the <sup>fi</sup>rst 14, 12, or 10 years’ data as the training set and the remaining years’ as the testing set. The comparisons of prediction performance are reported in Figure 8 and Tables 7–9. The results clearly demonstrate that the GDMR consistently outperforms the alternative models in predicting future sales.

We believe that the lackluster performance of the alternative models can be attributed to the fact that the time series and machine learning models are generalpurpose models and do not possess a mechanism to closely follow the asymmetric bell-shaped sales trend over time. By contrast, the GDMR is speci<sup>fi</sup>cally designed for such speci<sup>fi</sup>c sales trends; hence, its superior performance is not surprising.

Figure 7. (Color online) Comparison of Model Fitting for DVD Player Adoptions and Sales in the United States (1997–2010)  
![](/api/attachments/4XQN4M5Q/fulltext/images/dad0c77c2195c754beff632df0d3e9950485ccc8a93837afb1501b772d732d1a.jpg)

Figure 8. Comparison of GDMR and Generic Time Series and Machine Learning Models for DVD Players Sales in the United States  
![](/api/attachments/4XQN4M5Q/fulltext/images/dfb4dbc1872e4365560d52914fb1a140c262b0295ac453e273da556532c568cb.jpg)

![](/api/attachments/4XQN4M5Q/fulltext/images/c02f4416279138a6b482252ad15defea1ca986d1514348590b7083fc1bebf5a9.jpg)

![](/api/attachments/4XQN4M5Q/fulltext/images/767497c14ee10f5f55f8ab13d5890d114680e270cc34367ef002f71dfe33c16a.jpg)

![](/api/attachments/4XQN4M5Q/fulltext/images/9242a9a10d5be9e9577607a483681b96133b4763ff3ac37874f99d7a289cda32.jpg)

Finally, we show that the GDMR can produce accurate predictions using simple aggregate sales data, which is an important advantage. But this does not mean that the GDMR cannot take advantage of more detailed data. On the contrary, when richer data are available, the GDMR can perform estimations and predictions at a <sup>fi</sup>ner level of granularity and potentially make more accurate predictions.

## 6. Concluding Remarks

This study proposes a robust sales growth model to predict life cycle sales of technology products in the presence of frequent repeat purchases. Based on a branch of mathematics called fractional calculus, we develop a novel sales growth model, the GDMR, to account for repeat purchases that have become increasingly prevalent in today’s market of technology products, including both hardware and software products.

The GDMR represents a major advancement in the product-diffusion, repeat-purchases, and predictiveanalytics literatures because it not only <sup>fi</sup>lls a major void, but also possesses a number of important advantages. First, developed by adding only one parameter to the classic Bass model, the GDMR retains the Bass model’s parsimony and its insightfu behavioral explanation concerning adopters’ decisions in a diffusion process, which is a signi<sup>fi</sup>cant advantage compared with black-box machine learning models and other benchmark models that do not generalize a diffusion model, such as the Bass model. Second, the

Table 7. Eight-Year-Ahead Sales Prediction Accuracy Based on DVD Player Sales in the United States

<table><tr><td></td><td>GDMR</td><td>LSTM</td><td>Random forest</td><td>KNN</td><td>ARIMA</td><td>Holt</td></tr><tr><td>Mean absolute error</td><td>0.88</td><td>3.58</td><td>8.50</td><td>10.12</td><td>8.61</td><td>8.83</td></tr><tr><td>Mean squared error</td><td>1.10</td><td>23.15</td><td>76.60</td><td>110.30</td><td>88.40</td><td>92.88</td></tr><tr><td>MAPE</td><td>0.05</td><td>0.22</td><td>0.52</td><td>0.63</td><td>0.54</td><td>0.56</td></tr></table>

Table 8. 10-Year-Ahead Sales Prediction Accuracy Based on DVD Player Sales in the United States

<table><tr><td></td><td>GDMR</td><td>LSTM</td><td>Random forest</td><td>KNN</td><td>ARIMA</td><td>Holt</td></tr><tr><td>Mean absolute error</td><td>1.02</td><td>7.65</td><td>11.23</td><td>14.15</td><td>38.35</td><td>38.34</td></tr><tr><td>Mean squared error</td><td>1.48</td><td>58.84</td><td>128.16</td><td>208.47</td><td>1,916.81</td><td>1,916.31</td></tr><tr><td>MAPE</td><td>0.06</td><td>0.43</td><td>0.65</td><td>0.83</td><td>2.40</td><td>2.40</td></tr></table>

GDMR is a theoretically superior model to existing repeat-purchase models because it considers both replacement and multiunit purchases and covers a wider continuum of repeat purchase scenarios ranging from zero to highly frequent repeat purchases, making it applicable to a wide variety of products. Third, unlike the alternative repeat purchase models of which we are aware, the GDMR can incorporate the in<sup>fl</sup>uence of marketing mix variables, thus further enhancing its potential in helping <sup>fi</sup>rms make better marketing decisions. Fourth, the GDMR outperforms benchmark repeat repurchase models; generic time series models, including ARIMA and Holt; and machine learning models, such as LSTM, random forest, and Knearest neighbors by wide margins, further demonstrating the model’s superiority over alternative models. Therefore, the GDMR represents a major advancement to the literature on repeat-purchase models.

The contribution of the present research is not limited to the literature on product diffusion, repeat purchases, and predictive analytics. By accounting for repeat purchases using a fractional integral of the adoptions trend, the GDMR presents a new interpretation of fractional integral, thereby contributing to the broad literature of fractional calculus in applied mathematics and science. It is very well-known that integer-order integrals and derivatives have simple and clear geometric and physical interpretations, thus guiding numerous applications of these tools in science (Podlubny 2002). Interpreting fractional integrals and derivatives, however, proves challenging. For more than 300 years since the introduction of fractional calculus, no clear geometric and physical interpretation of fractional derivatives and integrals has been introduced (Podlubny 2002). Only in more recent years have different interpretations of fractional calculus emerged (e.g., Tarasova and Tarasov 2017). By proposing an interpretation of fractional integral in the context of product adoptions and repeat purchases, this study represents the newest contribution to the cross-disciplinary endeavor of interpreting fractional calculus. To the best of our knowledge, the present research is the <sup>fi</sup>rst in the IS literature or, more generally, management sciences literature to apply fractional calculus in the study of business problems.

Table 9. 12-Year-Ahead Sales Prediction Accuracy Based on DVD Player Sales in the United States

<table><tr><td></td><td>GDMR</td><td>LSTM</td><td>Random Forest</td><td>KNN</td><td>Holt</td></tr><tr><td>Mean absolute error</td><td>1.22</td><td>7.39</td><td>10.99</td><td>12.14</td><td>41.78</td></tr><tr><td>Mean squared error</td><td>2.17</td><td>58.33</td><td>133.84</td><td>167.42</td><td>2,129.53</td></tr><tr><td>MAPE</td><td>0.06</td><td>0.40</td><td>0.62</td><td>0.70</td><td>2.46</td></tr></table>

The present research, the fractional calculus–based model extension in particular, also lays a foundation for future work. For instance, as explained in Online Appendix A, multigeneration diffusion models (e.g., Norton and Bass 1987, Jiang and Jain 2012) differ from repeat-purchase models; the former can be used as the base for the type of repeat-purchases extension presented in this paper. Additionally, similar to the Bass model that is used as a baseline model for deriving the optimal path for marketing mix variables (e.g., Krishnan et al. 1999), the GDMR can be used to derive the optimal pricing and advertising strategy when repeat purchases constitute a signi<sup>fi</sup>cant part of sales, further helping <sup>fi</sup>rms in future planning. Furthermore, the modeling approach of this study, utilizing a spectrum of fractional calculus–based functions that run between a probability density function and its corresponding cumulative distribution function to capture the variations of a phenomenon of interest, is worth further examination. This approach may <sup>fi</sup>nd more applications in other branches of business and economics research.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for their constructive com ments and suggestions that have helped signi<sup>fi</sup>cantly improve the quality of this paper.

## Endnotes

<sup>1</sup> In Online Appendix D, for further testing, we compare the GDMR against two other benchmark models that do not incorporate three separate sales components

<sup>2</sup> Samsung tablet sales for 2012 is acquired from Ejectejecteject (2019) and for 2013 to 2019 is acquired from Statista (2022).

Sales reported by Statista for 2017 and 2018 are based on forecasts. There is some inconsistency in the two sets of data in that adoption is reported to be slightly larger than sales from 1998 to 2000 and adoption is zero in 1997, whereas the corresponding sales are nonzero. The inconsistency, however, has a negligible impact on parameter estimation. Therefore, we choose to keep the entire sample period for parameter estimation.

## References

Baesens B, Viaene S, Van den Poel D, Vanthienen J, Dedene G (2002) Bayesian neural network learning for repeat purchase modeling in direct marketing. Eur. J. Oper. Res. 138(1):191–211.

Baleanu D, Diethelm K, Scalas E, Trujillo JJ (2012) Fractional Calculus: Models and Numerical Methods, vol 3 (World Scienti<sup>fi</sup>c, Singapore).

Bass FM (1969) A new product growth for model consumer dura bles. Management Sci. 15(5):215–227.

Bass FM (2004) Comments on “a new product growth for model consumer durables the Bass model.” Management Sci. 50(12): 1833–1840.

Bass FM, Jain D, Krishnan T (2000) Modeling the Marketing-Mix Influ ence in New-Product Diffusion (Kluwer Academic Publishers, Boston).

Bass FM, Krishnan TV, Jain DC (1994) Why the Bass model <sup>fi</sup>ts without decision variables. Marketing Sci. 13(3):203–223.

Bayus BL, Hong S, Labe RP (1989) Developing and using forecasting models of consumer durables: The case of color television. J. Product Innovation Management 6(1):5–19.

Digital Entertainment Group (2009) Year-end home entertainment report. Accessed November 17, 2016, www.org.id.tue.nl/IFIP-TC14/documents/DEGsalesReport-2009.pdf.

Digital Entertainment Group (2010) Year-end home entertainment report. Accessed November 17, 2016, www.niaoren.info/pdf/ Entertainment/1.pdf.

Dodson JA Jr, Muller E (1978) Models of new product diffusion through advertising and word-of-mouth. Management Sci. 24(15):1568–1578.

Ejectejecteject (2019) 24 tablet market share statistics and analysis. Accessed March 19, 2022, https://www.ejectejecteject.com statistics/24-tablet-market-share-statistics-and-analysis/.

Fang X, Gao Y, Hu PJ (2021) A prescriptive analytics method for cost reduction in clinical decision making. Management Inform. Systems Quart. 45(1):83–116.

Gurbaxani V, Mendelson H (1990) An integrative model of informa tion systems spending growth. Inform. Systems Res. 1(1):23–46.

Guo Z, Chen J (2018) Multigeneration product diffusion in the presence of strategic consumers. Inform. Systems Res. 29(1):206–224.

Hann IH, Koh B, Niculescu MF (2016) The double-edged sword of backward compatibility: The adoption of multigenerational platforms in the presence of intergenerational services. Inform. Systems Res. 27(1):112–130.

Henderson RM, Clark KB (1990) Architectural innovation: The recon<sup>fi</sup>guration of existing product technologies and the failure of established <sup>fi</sup>rms. Admin. Sci. Quart. 35(1):9–30.

Hu Q, Saunders C, Gebelt M (1997) Diffusion of information systems outsourcing: A reevaluation of in<sup>fl</sup>uence sources. Inform. Systems Res. 8(3):288–301.

Jiang Z, Jain DC (2012) A generalized Norton-Bass model for multi generation diffusion. Management Sci. 58(10):1887–1897.

Jiang Z, Sarkar S (2009) Speed matters: The role of free software offer in software diffusion. J. Management Inform. Systems 26(3):207–240.

Jiang Z, Qu XS, Jain DC (2019) Optimal market entry timing for successive generations of technological innovations. Management Inform. Systems Quart. 43(3):787–806.

Kamakura WA, Balasubramanian SK (1987) Long-term forecasting with innovation diffusion models: The impact of replacement purchases. J. Forecasting 6(1):1–19.

Kilbas AA, Srivastave HM, Trujillo JJ (2006) Theory and Applications of Fractional Differential Equations, Elsevier Science B.V. Mathematics Studies, vol. 204 (North-Holland, Amsterdam).

Klan D, Karnstedt M, Politz C, Sattler KU (2008) Toward burst¨ detection for non-stationary stream data. LWA, 57–60.

Krishnan TV, Bass FM, Jain DC (1999) Optimal pricing strategy for new products. Management Sci. 45(12):1650–1663.

Lee CY, Huh SY (2017) Technology forecasting using a diffusion model incorporating replacement purchases. Sustainability 9(6):1038.

Lilien GL, Rao AG, Kalish S (1981) Bayesian estimation and control of detailing effort in a repeat purchase diffusion environment. Management Sci. 27(5):493–506.

Liu G, Nguyen TT, Zhao G, Zha W, Yang J, Cao J, Wu M, Zhao P, Chen W (2016) Repeat buyer prediction for e-commerce. Balaji Krishnapuram (General Chair), Shah M (General Chair), eds. Proc. 22nd ACM SIGKDD Internat. Conf. Knowl edge Discovery Data Mining, San Francisco, CA, August 13–17, 155–164.

Loh L, Venkatraman N (1992) Diffusion of information technology outsourcing: In<sup>fl</sup>uence sources and the Kodak effect. Inform. Systems Res. 3(4):334–358.

Loureiro AL, Migueis VL, da Silva LF (2018) Exploring the use of´ deep neural networks for sales forecasting in fashion retail. Decision Support Systems 114:81–93.

Mahajan V, Muller E, Wind Y, eds. (2000) New-Product Diffusion Models, vol. 11 (Springer Science & Business Media, New York).

Morgan Stanley (2015) Lowering smartphone forecast on weaker China in 1Q15. Morgan Stanley Research, https://www.morgan stanley.com/what-we-do/research.

Niculescu MF, Whang S (2012) Research note—Codiffusion of wireless voice and data services: An empirical analysis of the Japanese mobile telecommunications market. Inform. Systems Res. 23(1):260–279.

Norton JA, Bass FM (1987) A diffusion theory model of adoption and substitution for successive generations of high-technology products. Management Sci. 33(9):1068–1086.

Olson J, Choi S (1985) A product diffusion model incorporating repeat purchases. Tech. Forecasting Soc. Change 27(4):385–397.

Papoulis A, Pillai SU (2002) Probability, Random Variables, and Sto chastic Processes (Tata McGraw-Hill Education, New York).

Podlubny I (1999) Fractional Differential Equations (Academic Press, San Diego).

Podlubny I (2002) Geometric and physical interpretation of fractional integration and fractional differentiation. Fractional Calcu lus Appl. Anal. 5(4):367–386.

Rao AG, Yamada M (1988) Forecasting with a repeat purchase dif fusion model. Management Sci. 34(6):734–752.

Rogers EM (2003) The Diffusion of Innovation, 5th ed. (Simon and Schuster, New York).

Samko SG, Kilbas AA, Marichev OI (1993) Fractional Integrals and Derivatives—Theory and Applications (Gordon and Breach, Linghorne, PA).

Screen Australia (n.d.). Retail sales of DVD and BLU-Ray players, 1999–2011. Accessed August 20, 2021, www.screenaustralia.gov. au/fact-<sup>fi</sup>nders/video-and-online/audiences/in-the-archive/ dvd-player-sales.

Shmueli G, Koppius OR (2011) Predictive analytics in information systems research. Management Inform. Systems Quart. 35(3): 553–572.

Statista (2016a) Global PC sales fall to eight-year low. Accessed November 17, 2016, www.statista.com/chart/4231/global-pcshipments/.

Statista (2016b) Number of households in the US. from 1960 to 2015 (in millions). Accessed November 17, 2016, www.statista.com/ statistics/183635/pumber-of-households-in-the-us/

Statista (2019) DVD players/recorder unit shipments in the United States from 1<sup>st</sup> quarter 2014 to 4<sup>th</sup> quarter 2018 (in 1,000s). Accessed January 15, 2019, https://www.statista.com/statistics/ 220729/forecast-in-dvd-player-shipments-in-the-us/.

Statista (2022) Tablet vendor shipments worldwide from 2011 to 2021, by quarter (in millions). Accessed March 19, 2022, https:// www.statista.com/statistics/276651/global-media-tablet-shipmentssince-3rd-quarter-2011-by-vendor/.

Steffens PR (2003) A model of multiple-unit ownership as a diffu sion process. Tech. Forecasting Soc. Change 70(9):901–917.

Steffens PR, Balasubramanian S (1998) A study of the time varying mean replacement age of consumer durables. Ford JB, Honey cutt ED Jr., eds. Marketing Sci. Conf., Norfolk, Virginia, https://link. springer.com/book/10.1007/978-3-319-13084-2.

Tam KY (1996) Dynamic price elasticity and the diffusion of mainframe computing. J. Management Inform. Systems 13(2): 163–183.

Tarasov V (2018) Generalized memory: Fractional calculus approach. Fractal Fractional 2(4):23

Tarasova VV, Tarasov VE (2017) Economic interpretation of fractional derivatives. Preprint, submitted December 27, https:/ arxiv.org/abs/1712.09575.

Uncommon Wisdom Daily (2015) A fat zebra next to a hungry lion. Accessed November 17, 2016, www.uncommonwisdomdaily. com/dish-steer-clear-of-this-fat-zebra-next-to-a-hungry-lion 21806.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
