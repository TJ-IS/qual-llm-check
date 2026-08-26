---
otero_id: 26657
otero_key: "26BMW94C"
title: "Research Report—Modeling vs. Forecasting: The Case of Information Systems Spending"
authors: "Vijay Gurbaxani; Haim Mendelson"
year: "1994"
journal: "Information Systems Research"
doi: "10.1287/isre.5.2.180"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/26BMW94C/fulltext/images/9c75615e0452e2cf7a071c024ca1c5d69835037ca52e3d932fa0f083a9c1200f.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Report—Modeling vs. Forecasting: The Case of Information Systems Spending

Vijay Gurbaxani, Haim Mendelson,

## To cite this article:

Vijay Gurbaxani, Haim Mendelson, (1994) Research Report—Modeling vs. Forecasting: The Case of Information Systems Spending. Information Systems Research 5(2):180-190. http://dx.doi.org/10.1287/isre.5.2.180

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1994 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/26BMW94C/fulltext/images/6b5791de6434bb11a2bb61cc38ef38600a381fd8f1c70424cf90f6a585924a5b.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# RESEARCH REPORT

# Modeling vs. Forecasting: The Case of Information Systems Spending

Vijay Gurbaxani

Graduate School of Management

University of California, Irvine

Irvine, California 92715

Haim Mendelson

Graduate School of Business

Stanford University

Stanford, Calıfornıa 94305

Collopy, Adya and Armstrong (1994) (CAA) advocate the use of atheoretical “black box" extrapolation techniques to forecast information systems spending. In this paper, we contrast this approach with the positive modeling approach of Gurbaxani and Mendelson (1990), where the primary focus is on explanation based on economics and innovation diffusion theory. We argue that the objectives and premises of extrapolation techniques are so fundamentally different from those of positive modeling that the evaluation of positive models using the criteria of “black box" forecasting approaches is inadequate. We further show that even if one were to accept CAA's premises, their results are still inferior. Our results refute CAA's claim that linear trend extrapolations are appropriate for forecasting future IS spending and demonstrate the risks of ignoring the guidance of theory.

Information Systems Spending—Positive Models—Forecasting—Exponential Smoothing

## 1. Introduction

he growth in information systems (IS) spending was traditionally explained by factors related to the diffusion of innovations. In Gurbaxani and Mendelson (1990) (GM), we argued that models based solely on innovation diffusion were incomplete since they ignored the effect of the rapid price decline on the demand for computing. We hypothesized that in the early years of computing, IS spending growth was driven primarily by innovation diffusion, but as experience with the technology increased, technology costs became a dominant factor. We developed a model that incorporated both the sociological theories of innovation diffusion and the economic theory of demand and tested it using aggregate U.S. IS spending data The results strongly confirmed our hypothesis.

To the extent that Collopy, Armstrong and Adya (1994) (CAA) reexamined our conclusions, their results further support our hypothesis: they show that the price-adjusted models uniformly outperform, by a wide margin, their unadjusted counterparts. CAA proceed to claim, however, that atheoretical “black box" extrapolation methods such as versions of exponential smoothing result in better forecasts than those generated from positive models.

An obvious response to this type of claim is “so what?" It is well known that theories impose constraints on model parameters, and absent such constraints one can always obtain “better fits" that are nonetheless meaningless. It is also well known that ad hoc approaches such as exponential smoothing often generate excellent forecasts without any understanding of the underlying process. They are widely used in automated systems (primarily in inventory control) where the forecast figure is perceived as more important than an understanding of the markets, organizations and phenomena that generate demand. For most researchers, however, the latter is key.

In this case, a careful reading of CAA's results shows that their estimates for the price-adjusted logistic curve actually outperform their recommended equallyweighted combined forecast. Further, when we applied CAA's “black box" to the data, we found that their estimated parameters strongly suggested the inappropriateness of their equations for the problem at hand. The exponential smoothing forecasts advocated by CAA did not result in any smoothing, suggesting a misspecification, and CAA's substantive claim that linear trend extrapolations outperform growth models for forecasting future IS spending was not supported by the data. We conclude that our theory-based approach performs better even when subjected to the criteria advocated by CAA. The results also illustrate the inherent risks of using an atheoreticaapproach.

## 2. The GM Research

The stated objective of GM was to develop a model of IS spending growth. We pointed out that traditional studies had focused exclusively on the role of innovation diffusion while neglecting the effect of the price trend, which we argued was also important. We hypothesized that in the early years of computing, diffusion effects would dominate the dynamics of spending growth. However, as users gained experience with the technology, expenditures would grow exponentially due to the rapid decline in computing costs. Accordingly, we set out to test the specific hypothesis that price was a significant determinant of IS spending growth. An explicit goal was to “integrate both elements into a comprehensive model" (GM, p. 34) of IS spending growth.

We formulated a simple mathematical model of this growth phenomenon. The proposed model “accommodate(d) two patterns of growth in different periods, (1) an early transient period, when users gained familiarity with information technology and its applications, and (2) a steady state growth period, when DP expenditures continue to grow steadily as a result of decreasing prices" (GM. p. 24). We integrated the two subperiods using the model $X _ { t } = f ( t ) \cdot e ^ { \lambda \cdot t }$ , where $X _ { t }$ represents real spending in year t, f(·) is an S-curve and λ represents the price effect.

As we clearly explain (GM, p. 31), we focus on testing whether λ = 0 for any given functional form off(·). This requires a specification for the S-curve f(•) predicted by innovation diffusion theory. To show that our results were robust, we selected the S-curve functions most commonly used in diffusion studies: the logistic curve, the Gompertz curve and the modified exponential curve. In light of our objectives, we consciously did not look for the “best fitting" f(·); for example, we reported the results for the modified-exponential function that performed rather poorly.

We tested our hypothesis using aggregate IS spending data in the U.S. over the period 1960-1987. Our results clearly demonstrated the price effect. For all three specifications, the coefficient of the price-adjustment term was highly statistically significant. Indeed, the robustness of our results is repeatedly confirmed by CAA's analysis: whenever a model is compared to its price-adjusted counterpart, CAA's price-adjusted model is uniformly superior.

It is important to note that GM is not a paper about forecasting. It focuses on developing a positive model to explain IS spending growth by examining the roles of innovation diffusion and price. Indeed, our primary objective was to show the role of price, which was neglected in earlier studies. The reader may want to look at the GM paper, starting from the title, down to the key words and abstract, down to the introduction and text, to convince herself of this.

GM rejected the “best fit" approach in favor of a model-based approach. In our discussion of the data, we showed that it can be split into two periods, pre- and post-1970, and we explicitly recognized that two models—a diffusion model for the initial growth period and an exponential growth model for the later years—would provide a good fit. We rejected this approach because of our desire “to integrate both elements into a comprehensive model." The reader may want to review this issue (GM, p. 34, and Figure 3), which has a significant bearing on CAA's analysis.

CAA use extrapolation techniques such as exponential smoothing (ES) to forecast IS spending. They claim that “simple" trend extrapolations lead to better forecasts than price-adjusted diffusion models. They couch their claims in a set of“principles for examining predictive validity."

The CAA review of GM is misleading. A reader of the CAA description rather than of the paper itself might think that our empirical tests of the price-adjusted curves were conducted by using a single data point (1987) to “validate" our model. CAA state that “one can argue that their [GM's] test provided an advantage to the price-adjusted diffusion models" (p. 172), and CAA proceeded and “reexamined the results in GM, using the same series they analyzed" (p. 173). In reality, our empirical tests (GM, Table 1, p. 37) were tests of significance on the λ coefficient discussed above They were based on the complete data set, they were robust to model specification. and to the extent that CAA reexamined them, their results unequivocally support our conclusions. We did not set out to validate a forecasting system because we had not built one.

CAA's claims actually refer to an example that we used to “demonstrate the value of an underlying model of growth" in the middle of p. 42. Our example makes the simple point that positive models such as ours can be used to produce reliable forecasts. We certainly did not seek to build a forecasting system, let alone validate one, because this was not our objective. In fact, we consciously rejected models that would provide better “prediction" but were not based on theory.

In short, we believe that CAA's objectives and premises are so fundamentally different from our own that their añaiysis, regardless of its merits, has little or no bearing on GM. What complicates matters is that CAA have not been successful even on their own terms. To untangle these issues, we discuss the fundamental differences between the two approaches in §3 and evaluate CAA's analysis in §§4 and 5.

## 3. Positive Models vs. “Black Box" Forecasting

Positive models are explanatory and based on theory. In this case, they relate IS spending to fundamental factors that drive investments in IS. Drawing on economic theory and diffusion of innovation theory, the GM models attribute the demand for computing to two major determinants, price and innovation diffusion. We explain and estimate the relative contributions of each of the factors to demand and examine how they changed over time. Forecasting is only a by-product of positive modeling; the focus is on explanation.

In contrast, the “black box"forecasting approach exemplified by ES is often an atheoretical ad hoc approach. In their book on forecasting, Newbold and Bos (1990) state that “ES is a somewhat ad hoc approach to the problem of forecasting a time series on the basis of its own past."They proceed to say that “these algorithms are not models at all. Rather, they are simply a set of algebraic formulae that might be appropriate in particular instances for the generation of forecasts," and point out that “the decision to base forecasts on some ES algorithm is rather arbitrary. . . . In practice, most implementations of ES are somewhat unsystematic."

This is evidenced by CAA's “model" choices. They picked linear regression against time because “there is uncertainty about the proper form"(p. 174). They selected Brown's ES to “weight recent data more heavily" and they chose Damped Trend ES as it “offers another opportunity to improve the accuracy of the extrapolations by reducing the magnitude of the trend component based on the variation in the historical series" (p. 174). Further, CAA recommend averaging the various forecasts as this often works well. There are, however, numerous alternative extrapolation techniques. Should one use them all and generate the mean forecast? Or should one compute the weighted average of three arbitrarily-chosen techniques? To us, both CAA's choices and their weighting scheme look rather ad hoc. Moreover, since we did not propose a forecasting system, CAA proceeded to make the choices for us as well. We consider their choices inappropriate.

CAA's approach is akin to the techniques used by chartists to track stock prices. Some of these chartists may be successful, and technical market analysis—using trend lines, base lines and the like—is still widely practiced. Yet, the chartists' craft is not taken seriously in academic circles because it lacks a coherent theory and because it is so arbitrary.

The objective of positive modeling is to understand the phenomena under study; CAA's “black box" approach avoids this altogether and focuses on mechanical forecast generation. The positive approach starts from a theoretical model that suggests the relevant variables and the relationships among them, and asks whether the nature of the relationship is consistent with the data. GM identified the nature of IS spending growth as the combined result of diffusion effects in early years and price effects in later years. With regard to the future, only the latter is relevant since (as shown in GM) the diffusion period is behind us. However, for the purpose of understanding the growth process, the earlier diffusion effect is as important as the price effect. Weighting the earlier diffusion periods away in order to obtain better future predictions (which, as we show in §4, is the essence of CAA's ES forecasts) misses the whole point.

Of course, forecasting systems can be useful in a variety of applications. Inventory managers certainly appreciate the demand forecasts generated for them by automated systems, and these systems should be tested for predictive validity. CAA's validation methodology may be well-suited to such applications: it repeatedly applies the automated forecast generation algorithm and helps choose a system that would automatically produce the best forecasts. The forecasting system is then simply a system of adaptive equations that provide a mechanical fit to the data, rather than a model of the underlying phenomenon. It does not address causality, nor does it help to answer the research questions that motivate positive studies. In short, forecasting systems are not comparable to positive models, and it is not surprising that their evaluation criteria are different.

This confusion is reflected in CAA's emphasis on “ease of use," a well-justified criterion for forecasting systems. CAA seem to suggest that our price-adjusted equations should be repeatedly re-estimated by practicing managers and they complain that practitioners would “experience difficulty" in doing so (CAA, p. 173). Needless to say, positive research is designed to build the knowledge infrastructure that enables better management; we have yet to find the manager who thrives on running nonlinear statistical analyses. In our view, nonlinear least squares techniques—used by CAA to estimate both the price-adjusted models and their ES parameters—require expert human judgment and we would recommend against their blind automated use in the manner advocated by CAA. Indeed, our attempts to replicate CAA's ES results clearly demonstrated the complexity of their methods and their susceptibility to problems.

The choice of a model is driven by the researcher's objectives. Theories impose constraints on model parameters, and in the absence of such constraints, one can devise “better fits" that have little or no value from a research perspective. The notion that the model will be subsumed by the data is unacceptable in positive research. In essence, CAA build a straw man and establish a set of rules that they use to score their own performance against the straw man. Even by their own results, the straw man is doing very well. We think, however, that the reader may still benefit from further analysis of the outcomes, which will clearly demonstrate the benefits of the guidance of theory. This assessment is presented in §§4 and 5.

## 4. The CAA Methodology and Implementation

CAA's validation methodology uses thirteen rolling model-fitting periods and (up to) ten corresponding forecast periods, commencing with the fit period 1960–1974. A forecasting system is fit to the 1960–1974 data, and the fitted system is then used to derive forecasts for the period 1975–1984 (a ten-year horizon). CAA repeat the process by successively adding a year to the fit period, estimating the model and generating forecasts for subsequent years. Their measure of error is the absolute percentage error. The median absolute percentage error (MdAPE) is then computed for all nperiod ahead forecasts, where n ranges from 1 to 10. The overall measure of forecast performance is the average of the MdAPEs over the ten forecast horizons.

Note that all of the forecasts generated under the CAA methodology pertain to the 1975–1987 period. Thus, all of CAA's forecast years are in the period where (according to GM) the primary growth factor is the price decline, which leads to an exponential pattern. If one really wants to forecast IS spending in these years, an adaptive model that minimizes the weight of the diffusion years would have a natural advantage. This is shown in (GM, p. 34) and graphed in GM's Figure 3. Thus, it may not be surprising that simple extrapolation techniques seem to perform well in these years.

Yet, the ES techniques do not perform as well as the price-adjusted logistic curve that was not even designed to operate in a forecasting system,

If the sole objective is to forecast IS expenditures in the steady-state period, it is appropriate to use the steady-state behavior of the GM model for prediction. In the next section, we show that the forecasts generated using this approach outperform al of CAA's extrapolation techniques.

In order to understand what underlies CAA's results, it is necessary to start with a short overview of ES, which is the most widely used “black box" forecasting approach. We are given a time series of data $X _ { t }$ (interpreted in the inventory context as demand), and we attempt to forecast future values of the same series, say $\hat { X _ { t } }$ . Brown (1959) proposed a generalization of the moving average concept, where the forecast is driven by a “smoothing constant"α and a “demand estimate $\because S _ { t }$ that are related by

$$
S _ {t} = \alpha X _ {t} + (1 - \alpha) S _ {t - 1},\tag{1}
$$

where the constant α determines the weight given to past observations. Brown (1959) recommends smoothing constant values between 0.1 and 0.3, and this range is typical in practice (Gardner 1985). In fact, it is often recommended that a different model should be selected if α rises above (0.3 (Montgomery and Johnson 1976). This recommendation is controversial, and existing work uses the ranges $0 \leq \alpha \leq 1$ or $0 \leq \alpha \leq 2$ Large values of $\alpha$ are considered problematic as they call into question the very justification for smoothing (Newbold and Bos 1990).

Simple ES detects trend changes with a lag. Brown's “second order system" estimates the level $S _ { t }$ and trend $T _ { t }$ separately, using the equations

$$
S _ {t} = \alpha X _ {t} + (1 - \alpha) S _ {t - 1},\tag{2.1}
$$

$$
T _ {t} = \alpha (S _ {t} - S _ {t - 1}) + (1 - \alpha) T _ {t - 1}.\tag{2.2}
$$

This method, used by CAA, can be represented in a number of equivalent forms. Another second-order specification designed to track changes in trend is the Holt-Winters (HW) specification that uses two different coefficients to smooth the level (α) and trend (γ):

$$
S _ {t} = \alpha X _ {t} + (1 - \alpha) (S _ {t - 1} + T _ {t - 1}).\tag{3.1}
$$

$$
T _ {t} = \gamma (S _ {t} - S _ {t - 1}) + (1 - \gamma) T _ {t - 1}.\tag{3.2}
$$

Like the ranges for $\alpha ,$ moderate parameter values, generally below 0.3, have been recommended for these techniques (Gardner 1985). Theoretical considerations suggest that the systems are stable for $0 \leq \alpha < 2$ and $0 \leq \gamma < ( 4 - 2 \alpha ) / \alpha$ (Gardner 1985).

The more complex Damped-Trend ES (Gardner and McKenzie 1985) is given by

$$
S _ {t} = \alpha X _ {t} + (1 - \alpha) (S _ {t - 1} + \phi T _ {t - 1}),\tag{4.1}
$$

$$
T _ {t} = \gamma (S _ {t} - S _ {t - 1}) + (1 - \gamma) \phi T _ {t - 1},\tag{4.2}
$$

where the “damping coefficient"φ moderates the series'trend. Note that the HW technique (3) is a generalization of Brown's (2), and it is in turn a special case of Damped Trend ES (4).

ES forecasting requires the choice of a technique as well as its smoothing coefficients and initial values. These choices have a significant effect on the results. Given the smoothing constants and initial values, it is easy to produce the forecasts. The key, however, is the estimation of the smoothing constants, which requires nonlinear optimization. Our estimations used the RATS statistical package as well as Autocast-II, the package used by CAA.

CAA did not report how their parameters were estimated. Since we were given one month to prepare a response, we limited our replication attempts to their ES results that had included their best performers, using a range of Autocast-II options. We estimated the smoothing constants by minimizing the within-sample one-step mean squared forecast error.² Our results are presented in Table 1, which complements CAA's Table.

We first estimated the simple ES forecast, limiting the smoothing constant α to the range between zero and unity. The results had a Mean MdAPE of 27% (Table 1, line 1). The smoothing constant α was at its limit of 1 for all 13 forecasts, suggesting that either the system is inappropriate (which is indeed the case) or that we should increase the upper bound on α to 2. When we increased the upper bound, the α estimates ranged from 1.86 to 1.92 with only marginal improvement in forecasting performance (the Mean MdAPE became 25.3%; see line 2).

Next we estimated HW's system (3) with smoothing constant ranges of 0 to 1 (the program default). The result (line 3) was virtually identical to CAA's Brown system, with a Mean MdAPE of 7.1%. Both smoothing coefficients hit their upper bounds of unity in all 13 estimations. When we allowed $0 \leq \alpha , \gamma \leq 2$ , the forecast quality declined (line 4, Mean MdAPE 7.7%).

We then estimated the Damped-Trend ES system, first limiting the parameter values to $0 \leq \alpha , \gamma , \phi \leq 1$ (the program default). All three parameters again hit their upper bounds of unity. For these parameter values, the Damped Trend system collapses into the HW system which becomes equivalent to Brown's, and their forecasts are obviously identical (compare line 5 to line 3). Mathematically, when $\phi = 1$ Equations (3) and (4) are identical, and the resulting forecasts should be the same. Further, in the degenerate case $\alpha = \gamma = 1$ , systems (2) and (3) are identical. Thus, the results from the Damped Trend system are identical to those of Brown's (2) or HW (3).

When we relaxed the constraints on the values of the smoothing constants so that α and γ could range between 0 and 2 (the other range option supported by Autocast-II), forecast quality decreased somewhat (Table 1, line 6) to a Mean MdAPE of 7.7%.

In summary, all plausible ES systems, regardless of their sophistication, number of parameters or ranges underperformed the price-adjusted logistic results in CAA's Table (line 6).

It is useful to note that in our estimations of (3) and (4) with parameter values between 0 and 1, all smoothing constants hit their upper limits of unity. Then, all three ES techniques result in the following forecasts. Standing at period t, the forecast for period $t + 1$ is the value of the current observation, X,, plus the slope of the series in the previous period $X _ { t } \gets X _ { t - 1 }$ . The data from all prior periods is simply ignored. Qualitatively, the growth in the next period is predicted to be identical to the growth in the previous period, with no smoothing at all. As we demonstrate in §5, this is indicative of a misspecified linear model.

<table><tr><td rowspan="2">Method</td><td rowspan="2">Eq</td><td colspan="10">Forecast Horizon</td><td rowspan="2">Average10(4)</td><td rowspan="2">1 to 10(85)</td></tr><tr><td>Parameter Bound</td><td>1(13)</td><td>2(12)</td><td>3(11)</td><td>4(10)</td><td>5(9)</td><td>6(8)</td><td>7(7)</td><td>8(6)</td><td>9(5)</td></tr><tr><td>1 Simple exponential smoothing</td><td>(1)</td><td>1</td><td>5.6%</td><td>11.2%</td><td>16.4%</td><td>21.8%</td><td>25.4%</td><td>30.2%</td><td>33.9%</td><td>37.5%</td><td>42.3%</td><td>45.6%</td><td>27.0%</td></tr><tr><td>2 Simple exponential smoothing</td><td>(1)</td><td>2</td><td>3.0%</td><td>8.9%</td><td>15.8%</td><td>19.4%</td><td>23.7%</td><td>28.5%</td><td>33.2%</td><td>36.7%</td><td>40.1%</td><td>43.7%</td><td>25.3%</td></tr><tr><td>3 Holt-Winters exp smoothing</td><td>(3)</td><td>1</td><td>1.8%</td><td>4.3%</td><td>6.5%</td><td>7.7%</td><td>5.1%</td><td>7.7%</td><td>6.0%</td><td>11.9%</td><td>2.3%</td><td>18.1%</td><td>7.1%</td></tr><tr><td>4 Holt-Winters exp smoothing</td><td>(3)</td><td>2</td><td>1.7%</td><td>3.7%</td><td>5.5%</td><td>8.1%</td><td>7.1%</td><td>7.3%</td><td>7.4%</td><td>10.8%</td><td>7.8%</td><td>17.4%</td><td>7.7%</td></tr><tr><td>5 Damped-Trend exp smoothing</td><td>(4)</td><td>1</td><td>1.8%</td><td>4.3%</td><td>6.5%</td><td>7.7%</td><td>5.1%</td><td>7.7%</td><td>6.0%</td><td>11.9%</td><td>2.3%</td><td>18.1%</td><td>7.1%</td></tr><tr><td>6 Damped-Trend exp smoothing</td><td>(4)</td><td>2</td><td>1.9%</td><td>3.7%</td><td>5.5%</td><td>8.1%</td><td>7.1%</td><td>7.3%</td><td>7.4%</td><td>10.8%</td><td>7.8%</td><td>17.3%</td><td>7.7%</td></tr><tr><td>7 Exponential growth model</td><td>(5)</td><td></td><td>2.1%</td><td>2.1%</td><td>2.2%</td><td>1.8%</td><td>1.7%</td><td>0.8%</td><td>2.6%</td><td>4.0%</td><td>4.4%</td><td>4.1%</td><td>2.6%</td></tr><tr><td>8 Exponential growth and GNP growth</td><td>(6)</td><td></td><td>2.1%</td><td>2.2%</td><td>2.3%</td><td>1.9%</td><td>2.1%</td><td>2.0%</td><td>0.7%</td><td>2.3%</td><td>2.8%</td><td>3.3%</td><td>2.2%</td></tr></table>

This result is predictable from GM, where we have shown that in the pertinent period, the data consist mostly of a constant growth rate plus noise. What CAA are trying to do is fit a linear trend to a growing series that is characterized by an increasing slope. Then, the ES forecasts cast aside all past observations and apply as much weight as is allowable to the most recent level and trend. Thus, the ES results in fact convey a message that is contrary to the one suggested by CAA: rather than supporting a linear trend, the smoothing coefficients suggest an accelerated growth pattern.

## 5. Growth Patterns in IS Spending

CAA's substantive conclusion regarding the growth of IS spending is as follows: “It appears to be a commonly held view that spending on IS is growing in an explosive fashion. . . . If experience is any indication, one of the implications of the analysis presented here is that we are more likely to be close to true future values of spending on IS if we assume that they will continue to grow in a simple linear fashion" (CAA, “Conclusion," p. 176). This is, indeed, in stark contrast to our own conclusions: “while IS expenses initially grew following an S-curve, more recent growth has converged to an exponential pattern" (GM, p. 23). So, are the recent data more consistent with linear or exponential growth patterns?

To answer this question, we compared CAA's results to those obtained under the exponential-growth model,

$$
\log (X _ {t}) = a _ {0} + a _ {1} \cdot t + \epsilon_ {t}.\tag{5}
$$

As we indicated earlier, the GM analysis shows that this model is appropriate for the later years to which CAA's forecasts pertain. To enable a comparison with the CAA systems, we used the data from 1970 on (see GM, p. 34). The results (line 7) have a mean MdAPE of 2.58%, well below all of CAA's forecast errors. Thus, the exponential growth model provides better forecasts than the linear systems advocated by CAA.

It is surprising that CAA maintained their claims in spite of the clear warning signs provided by their own ES estimates. In particular, the fact that in the ES estimations with parameter values between 0 and 1, the smoothing coefficients hit their upper limits of unity indicates that the linear trend assumption consistently underestimates the actual growth rate. To examine this in concrete terms, consider what happens when Brown's system (2) is used in an attempt to fit a noiseless constant-growth data series, $X _ { t } = . 4 \cdot ( 1 + g ) ^ { t }$ where $g > 0 . { } ^ { 3 }$ With the initial conditions

$$
S _ {0} = \frac {A \alpha (1 + g)}{g + \alpha} \quad \text { and } \quad T _ {0} = \frac {A \alpha^ {2} g (g + 1)}{(g + \alpha) ^ {2}},
$$

Brown's level and trend series are $S _ { t } ~ = ~ S _ { 0 } ( 1 ~ + ~ g ) ^ { t }$ and ${ \cal T } _ { t } = { \cal T } _ { 0 } ( 1 + g ) ^ { t }$ , and the one-period ahead forecast error ${ \mathrm { i } } { \mathsf { s } } ^ { 4 }$

$$
E _ {t} = X _ {t} - \hat {X} _ {t} = E _ {0} \cdot (1 + g) ^ {t}, \quad \text { where } E _ {0} = \frac {A g ^ {2}}{(g + \alpha) ^ {2}}.
$$

It follows that the mean squared forecast error is a decreasing function of $\alpha ,$ and its minimum over $0 \leq \alpha \leq 1$ is at α = 1 $\alpha = 1$ . Similar results are obtained for the HW system, where α and $\gamma$ both hit their upper limits of unity, just as we obtained for the IS spending data. This happens because the ES systems assume a linear trend and, faced with an increasing trend, they attempt to catch up by increasing α to its upper bound of unity.

To further examine the effects of a linear misspecification, we ran the Damped Trend ES technique (with $0 \leq \alpha , \gamma , \phi \leq 1 )$ on the predicted values of the exponential growth model (5). Consistent with the above analysis, α and $\gamma$ hit their upper bounds in all cases. We also found that, as one might expect, thıs linear ES system consistently underestimated the growth series, with errors increasing in the forecast horizon. A similar analysis using the fitted values of the price-adjusted logistic model also resulted in parameter values of unity for both α and $\gamma$

We have thus shown that CAA's own methodology and scoring rules reject CAA's linear specification in favor of an exponential growth model. This is evidenced not only by the quality of the forecasts but, more importantly to our minds, by the structure of the estimates.

In GM, we also hypothesized that “while the long-run growth path of [IS] investments follow the pattern studied here, in the short run they will fluctuate with the business cycle" (p. 43). Since in this paper we are dealing with forecasting, we wondered whether incorporating past growth rates of GNP as explanatory variables would improve forecast accuracy. The estimation requires models of both IS spending growth and GNP growth. We estimated the simple model

$$
\log (X _ {t}) = a _ {0} + a _ {1} \cdot t + a _ {2} \cdot G _ {t - 1} + \epsilon_ {t},\tag{6}
$$

where $G _ { t }$ is the real GNP growth rate in year t, assumed to follow the autoregressive process $G _ { t } = b _ { 0 } + b _ { 1 } \cdot G _ { t - 1 } + \xi _ { t }$ . Here, the year-t forecasts use information available in prior years. The results (line 8) show that as expected, this forecast performs better than the simple logarithmic forecast, with Mean MdAPE 2.17%.

In sum, we have demonstrated that for CAA's forecasts, an exponential model, consistent with a constant-elasticity demand function, provides better forecasts than their linear model. This is consistent with theory and is borne out through extensive empirical verification. Our analysis also illustrates the risks of using “black box" forecasting techniques rather than theoretically derived models. CAA's approach assumes that there is no need to study the underlying process if one relies on simple extrapolation techniques. However. we have just seen how fragile this approach can be.

## 6. Concluding Remarks

GM's research question was whether the price effect adds explanatory power to traditional diffusion models. We proposed a model of IS spending growth that integrates the diffusion and price effects and showed that the price effect was significant. CAA's findings support this conclusion.

CAA proceeded to evaluate our model as if it were a “black box" system that successively generates annual forecasts. In doing so, CAA set up a straw man. They intended to show that techniques that were designed to operate as forecasting systems performed better as such. The reality is that they often do, but not in this case. Even using CAA's own criteria, their techniques proved inferior to the straw man they set up for comparison. In our view, this is evident even from their own paper.

Rather than repeat our discussion of CAA's method and its inherent biases, we point out that in spite of these biases, our price-adjusted logistic curve (with a mean MdAPE of 6%) outperforms all of the exponential smoothing techniques as well as CAA's final recommendation, the equal-weights forecast. Taking into account the nature of the forecast period, our estimates result in an MdAPE of 2.6%, better than every one of CAA's extrapolation techniques. We believe that our results clearly demonstrate the superiority of the positive approach. Further, they demonstrate the risks inherent in the use of an atheoretical approach. We think that CAA's model misspecification is directly linked to their reluctance to rely on theory.

This debate exhibits the tension between explanation and forecasting. Even though our approach happens to provide better forecasts, we firmly believe in the importance of explanation as the primary objective for the reasons discussed in §3 of this paper. The ongoing structural changes in the computer industry underscore our point that the forecast numbers are less relevant than an understanding of the nature of the growth process. On the one hand, the industry is segmented into horizontal subindustries. On the other hand, digital convergence results in the formation of a large “information appliance" industry whose boundaries are not well-defined. In this context, forecast numbers are not transferable, while models and insights are. We believe that the confluence of diffusion and price effects will help explain and differentiate the development of the emerging industry segments now and in the future.\*

Acknowledgements. This work was supported in part by grants from the National Science Foundation, and by the Sloan Foundation's Computer Industry Project at Stanford University.

\* Accepted by John L. King.

## References

Armstrong, J. Scott and Fred Collopy, “Error Measures for Generalizing about Forecasting Methods: Empırical Comparisons," Internattonal Journal of Forecasting, 8 (1992), 69–80

Brown, Robert G., Stattstical Forecasting for Inventory Control, McGraw-Hill, New York, 1959.

Collopy, Fred, Monica Adya and J. Scott Armstrong, “Principles for Examinıng Predictive Validity. The Case of Information Systems Spending Forecasts," Information Svstems Research, 5, 2 (1994), 170– 179

Gardner, Everette S., Jr., “Exponential Smoothing. The State of the Art." Journal of Forecasting, 4 (1985). 1-28.

and Ed McKenzie. “Forecastıng Trends in Time Series," Management Sctence, 31, 10 (1985), 1237-1246.

Gurbaxanı, Vijay and Haim Mendelson, “An Integrative Model of Information Systems Spending Growth," Informatton Systems Research, 1 (1990), 23–46.

Montgomery, Douglas and Lynwood Johnson, Forecasting and Ttme Series Analysis, McGraw-Hill, New York, 1976.

Newbold, Paul and Theodore Bos, Introductory Business Forecasttng, South-Western, Cincinnati, OH, 1990.
